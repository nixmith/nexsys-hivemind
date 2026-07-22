<!--
file: context/instructions/2026-07-22_CMD-API_command-write-surface_coding-instruction.md
purpose: CMD-API — the command write surface (POST issue + GET status). The last unwired plane; the keystone WU for the Aug-14 gate (C2/C3/H2 producers + B2/B3 + M14 stack behind it).
audience: Coder (host-CC lane, homesynapse-core)
status: ISSUE-READY
baseline: core 355a711 (re-verify at dispatch; drift => STOP). Pre-verification: context/pre-verifications/WU-CMD-API.md (P0-P16 — read FIRST).
-->

# Coding Task: CMD-API — Command Write Surface (issue + status)

**Subsystem:** REST API (`api/rest-api`) + one composition-root wiring line (`lifecycle`)
**Design Doc:** Doc 09 REST API (Locked) §3.2/§3.4/§4.3-4.5 + AMD-08 idempotency; wire-casing per Nick's 2026-07-22 ruling (b): the LIVE camelCase per-endpoint reality outranks the Doc-09 snake_case module row (the recorded AB-1-class currency nit).
**Phase:** 3-Implementation. Tests BEFORE implementation (stage-A red -> stage-B green).
**Task brief:** v36 charge 1 (the ~Jul-24 tripwire WU). North star: never-false-CONFIRMED — the status read may report CONFIRMED only from a `state_confirmed` event.

## What This Implements

The command plane's HTTP write surface. The full command pipeline already runs end-to-end (M7.4/M9.4 era): `command_issued` -> co-located dispatch subscriber -> integration -> `command_result` -> confirmation/`state_confirmed` or timeout, with the pending-command ledger tracking by causation. What is missing is the LAST plane: no HTTP route can create a `command_issued` (P6: zero `app.post` in the repo). This WU adds exactly two endpoints — POST issue and GET lifecycle status — as thin adapters over the existing pipeline: validate, publish ONE root event, read ONE correlation chain. No pipeline logic is duplicated; the subscribers do everything they already do.

## Files to Read Before Starting

| File | Why |
|---|---|
| `context/pre-verifications/WU-CMD-API.md` | Every source-state pin (P0-P16) |
| `api/rest-api/MODULE_CONTEXT.md` | Type inventory, contracts, gotchas (idempotency spec, envelope idiom, casing) |
| `api/rest-api/src/main/java/module-info.java` | VERBATIM embed below — zero changes pinned |
| `core/automation/MODULE_CONTEXT.md` | Dispatch/ledger/supersession/disposition gotchas |
| `RestFilters.java` | The install-gateway + auth + error idioms to match exactly |
| `ListEntitiesEndpoint.java`, `GetEntityStateEndpoint.java` | The live handler + envelope + casing pattern |
| `StandardActionExecutor.java` `:260-:310` | The SOLE existing `command_issued` emitter — mirror its draft construction + timeout/idempotency precedence |
| `EndpointResponses.java`, `ProblemType.java`, `IdempotencyEntry.java`, `CommandRequest/Accepted/Status/Phase/Detail` | The Phase-2 contract types this WU realizes |
| `EventPublisher.java`, `EventStore.java` (`readByCorrelation`), `EventOrigin.java`, `EventTypes.java`, `CommandIssuedEvent.java` | The pipeline seams (P9/P10) |
| `CommandValidator.java` + `StandardCommandValidator` | The 422 instrument |
| `HomeSynapseCore.java` `bringUpHttpSurface()` region | The wiring insertion point (P12) |
| Test: `ListEntitiesEndpointTest.java`, `RecordingEndpointContext.java`, `RestFiltersAuthTest.java` | Test conventions to match |

### rest-api module-info.java — VERBATIM (zero changes; P13)
```java
module com.homesynapse.api.rest {
    requires transitive com.homesynapse.state;
    requires com.homesynapse.event.bus;
    requires com.homesynapse.automation;
    requires com.fasterxml.jackson.databind;
    requires io.javalin;
    requires org.slf4j;
    exports com.homesynapse.api.rest;
}
```
(Comment blocks elided here only; the on-disk file keeps them. `com.homesynapse.event`/`device`/`platform` types are readable via automation's `requires transitive` closure — verify with the targeted compileJava; if Gradle's compile path is missing them, add `implementation(project(":core:event-model"))` (and `:core:device-model` if needed) to `api/rest-api/build.gradle.kts` — plain implementation, NEVER `api` (no exported-surface exposure exists).)

## STOP-on-Mismatch Gates

| Gate | Check |
|---|---|
| G-1 | HEAD == `355a711`, clean tree; baseline `:api:rest-api:test` + `:lifecycle:lifecycle:test` RE-DERIVED forced-fresh, counts reported (never carried) |
| G-2 | `RestFilters.java`: 9 `app.get` routes, zero `app.post`; `installAuth` at `:346` |
| G-3 | `CommandIssuedEvent` has EXACTLY the 5 components of P9; `IdempotencyEntry` exactly the 5 of P4 |
| G-4 | `EventOrigin.USER_COMMAND` present; `EventStore.readByCorrelation(Ulid)` present; `EventPublisher.publishRoot(EventDraft)` present |
| G-5 | `bringUpHttpSurface()` contains `installAutomationQueryEndpoints` (the insertion anchor) and the composition root has locatable EventPublisher + EntityRegistry fields |
| G-6 | `CommandLifecyclePhase` constants exactly `{ACCEPTED, DISPATCHED, ACKNOWLEDGED, CONFIRMED, CONFIRMATION_TIMED_OUT}` |

## Files to Create or Modify

| Action | File | Description |
|---|---|---|
| MODIFY | `api/rest-api/.../RestFilters.java` | `installCommandEndpoints(...)` gateway + 2 routes |
| CREATE | `api/rest-api/.../IssueCommandEndpoint.java` | package-private POST handler |
| CREATE | `api/rest-api/.../GetCommandStatusEndpoint.java` | package-private GET handler |
| CREATE | `api/rest-api/.../IdempotencyCache.java` | package-private LRU+TTL cache (DP-4) |
| MODIFY | `lifecycle/.../HomeSynapseCore.java` | ONE install call in `bringUpHttpSurface()` |
| CREATE | `api/rest-api/src/test/.../IssueCommandEndpointTest.java` | stage-A red first |
| CREATE | `api/rest-api/src/test/.../GetCommandStatusEndpointTest.java` | stage-A red first |
| CREATE | `api/rest-api/src/test/.../IdempotencyCacheTest.java` | stage-A red first |
| CREATE | test fakes as needed (package-local recording EventPublisher, fake EntityRegistry, fake EventStore) | match `FakeStateQueryService` conventions |
| MODIFY | `api/rest-api/MODULE_CONTEXT.md` | inventory + gotchas update (spec below) |

## Settled Decision Points (NOT open questions)

- **DP-1 (Scope).** Exactly two routes: `POST /api/v1/entities/{entityId}/commands`, `GET /api/v1/commands/{commandId}`. **The webhook plane is OUT** — the 4-grep census result of record: Doc 09 defines NO inbound webhook route; `WebhookTrigger`'s producer event is "named and minted by the M10 REST amendment" (P15). Batch, If-Match, subscriptions: OUT (Tier 2).
- **DP-2 (Wire shape — token-freeze day one; the bench binds these bytes).** Both responses use the LIVE `{data, meta}` hand-built-LinkedHashMap camelCase idiom (P8). 202 body: `data` = the `CommandAcceptedResponse` fields verbatim (`commandId, correlationId, entityId, status, acceptedAt, viewPosition`), `meta` = `{viewPosition, timestamp}`. Status 200 body: `data` = the `CommandStatusResponse` shape (`commandId, correlationId, entityId, capability, command, lifecycle, currentPhase, terminal`) with lifecycle map keys and `currentPhase` serialized as `CommandLifecyclePhase.name()` (UPPERCASE — the bench's pinned phase list; P16), `meta` = `{viewPosition, timestamp}`. `LifecyclePhaseDetail` renders `{at, eventId, details}` camelCase (details map keys stay as P3 names: `integration_id`, `result`, `match_type` — they are payload-derived tokens, not envelope keys). Both endpoints set `Cache-Control: no-store` and `X-HomeSynapse-View-Position`. Timestamps ISO-8601 (`Instant.toString()` per live idiom); IDs as 26-char ULID strings.
- **DP-3 (Publish semantics).** On accept: serialize `parameters` to a JSON string via jackson-databind (rest-api is the JSON boundary, M7.5a precedent). Resolve `confirmationTimeoutMs` + `CommandIdempotency` by MIRRORING `StandardActionExecutor`'s capability precedence (`:260-:310`; default = the same config-sourced default the executor receives — pass it through the install gateway as `int defaultConfirmationTimeoutMs`; unresolvable idempotency => `NOT_IDEMPOTENT`, the never-silently-re-fire default). Build the `EventDraft` field-for-field like the sole existing emitter EXCEPT: origin = `EventOrigin.USER_COMMAND` (P10) — match its event type, schema version, `SubjectRef.entity(target)`, and priority exactly (report the observed priority as `[INFO]`). Publish via `publishRoot` (durability precedes the 202 — INV-ES-04 rides the publisher contract). `commandId` = the returned envelope's eventId string; `correlationId` = the same (root event). NO ledger writes, NO dispatch calls — the subscribers own those.
- **DP-4 (Idempotency).** Package-private `IdempotencyCache`: `ReentrantLock` (LTD-11, never synchronized), LinkedHashMap access-order LRU cap 10,000, TTL 24h from `createdAt` via INJECTED `Clock`, not persisted. Internal record wraps `IdempotencyEntry` + a body fingerprint (SHA-256 hex over the canonical string `entityId + "\n" + capability + "\n" + command + "\n" + <parameters serialized with sorted keys>`). Semantics per P4/P15: no header => bypass; key > 128 chars => 400 `INVALID_PARAMETERS`; hit+same-fingerprint => replay 202 rebuilt from the stored entry (same commandId/correlationId/viewPosition; `acceptedAt` = entry `createdAt`) WITHOUT publishing; hit+different => 409 `IDEMPOTENCY_KEY_CONFLICT`; miss => proceed, store after successful publish.
- **DP-5 (Status assembly — the honesty contract).** Parse `{commandId}`; unparseable ULID OR empty `readByCorrelation` chain OR chain whose `command_issued` eventId != commandId => 404 `COMMAND_NOT_FOUND`. Map the chain: `command_issued` -> ACCEPTED; `command_dispatched` -> DISPATCHED (+`integration_id`); `command_result` -> ACKNOWLEDGED (+`result` = the outcome string VERBATIM — the live ten-value vocabulary), **terminal iff outcome != "acknowledged"**; `state_confirmed` -> CONFIRMED (+`match_type`), terminal; `command_confirmation_timed_out` -> CONFIRMATION_TIMED_OUT, terminal. `currentPhase` = the latest phase reached; `lifecycle` contains only reached phases. **CONFIRMED derives ONLY from `state_confirmed` — no other path may render it (never-false-CONFIRMED; AMD-97-INV-01).**
- **DP-6 (Validation order + V1 subset).** (1) body parse/shape failures => 400 `INVALID_PARAMETERS` with `errors[]` FieldErrors; (2) entity resolve failure (bad ULID or absent) => 404 `NOT_FOUND` (the live entity-endpoint precedent); (3) `StandardCommandValidator` (construct inside the install gateway over the passed registry) invalid => 422 `INVALID_COMMAND`, reason verbatim in `detail`; (4) idempotency per DP-4; (5) publish; (6) 202. **V1-SUBSET RECORDED:** `entity-disabled` (409) and `integration-unhealthy` (503) checks DEFERRED — the registries expose no enabled/health read at `355a711`; the ProblemTypes stand ready; this is the standing "V1 ships a subset of a Locked doc" record class. The `command_issued` payload does NOT gain an `idempotency_key` field — the event shape is FROZEN 5-component (P9); Doc 09's payload-field sentence is deferred with this same record (idempotency is fully realized at the REST layer).
- **DP-7 (Zero-change pins).** Zero event-type/schema mints. Zero module-info edits (both modules — P13/P14). Zero config-schema changes. Zero NEW public types (handlers + cache package-private; the ONLY public delta = the `installCommandEndpoints` static method on `RestFilters`). Zero changes to dispatch/ledger/confirmation code.
- **DP-8 (Auth).** No auth code in this WU: `installAuth`'s `before(*)` already covers the new routes (P6). Token-freeze day one = no changes to `OpaqueTokenStore` or token semantics.

### `installCommandEndpoints` gateway (match the DEC-M3-16 idiom)
```java
public static void installCommandEndpoints(Object javalinApp,
                                           Object eventPublisher,   // EventPublisher, cast internally
                                           Object entityRegistry,   // EntityRegistry, cast internally
                                           Object eventStore,       // EventStore, cast internally
                                           int defaultConfirmationTimeoutMs,
                                           LongSupplier viewPositionSupplier,
                                           Clock clock)
```
Constructs the validator, cache, and both handlers internally; registers `app.post(...)` and `app.get(...)`. Composition root: insert the call after `installAutomationQueryEndpoints`, passing the existing composition-root publisher/registry/eventStore fields + the SAME default-timeout config value the action executor receives (locate both; G-5).

## P2 Consumer/Pin (Fan-Out) Survey

No enum/registry/event-type/sealed-set changes => no count-pin fan-out. Swept: `EventCategoryMapping` untouched (no mints); no publish-site changes on EXISTING paths (the new publish site only fires via the new endpoint — lifecycle publish-count pins such as `RunPipelineConfirmWiringTest` are unaffected; re-grep `lifecycle` tests for `command_issued` count pins at execution and report `[INFO]`); module-info zero-change validated against every DP (#14 walk: no new exported types/signatures); `RestFilters` shape tests: none exist pinning method counts (verify by grep, report).

## Invariants / Locked Decisions

- **AMD-97-INV-01 / never-false-CONFIRMED** — DP-5's CONFIRMED rule; test-locked below.
- **INV-ES-04** — 202 only after `publishRoot` returns (durable).
- **INV-SE-02** — rides `installAuth` (DP-8); no new surface escapes `before(*)`.
- **LTD-04** — IDs are typed ULIDs internally, 26-char strings at the boundary only.
- **LTD-11** — `ReentrantLock` only; no `synchronized` anywhere in new code.
- **LTD-08** — rest-api is the JSON boundary; jackson-databind only here.
- **D2 pure-function-replay** — untouched (no subscriber changes).

## Test Requirements (stage-A red FIRST; fixture-paired per the doctrine — every assert proves its PASS and its false-verdict boundary)

`IssueCommandEndpointTest`: happy-path 202 (exact camelCase key set data+meta pinned byte-for-byte; published draft captured: type/origin USER_COMMAND/subject/payload fields incl. serialized parameters + resolved timeout/idempotency); 404 absent entity; 404 unparseable entityId; 422 undeclared command (reason verbatim); 400 missing/blank fields (FieldErrors); 400 oversize Idempotency-Key (129 chars); replay same-key-same-body => identical commandId + ZERO second publish (the recording publisher proves it); 409 same-key-different-body; no-header => two publishes two ids; `Cache-Control: no-store` + view-position header present.
`IdempotencyCacheTest`: TTL expiry at exactly 24h via Clock advance (23h59m hit / 24h01m miss — the boundary pair); LRU eviction at 10,001; fingerprint sensitivity (parameters order-insensitive via sorted-key canonicalization; value change => different).
`GetCommandStatusEndpointTest`: 404 unknown/unparseable; ACCEPTED-only chain (non-terminal, lifecycle size 1); +DISPATCHED; result outcome "acknowledged" => ACKNOWLEDGED non-terminal; result outcome "rejected" => terminal at ACKNOWLEDGED with result verbatim (repeat for one disposition outcome, e.g. "superseded" — proves the != "acknowledged" rule, not an enum list); full chain to `state_confirmed` => CONFIRMED terminal with match_type; `command_confirmation_timed_out` => CONFIRMATION_TIMED_OUT terminal; **the never-false-CONFIRMED lock: a chain with result "acknowledged" and NO state_confirmed must NOT render CONFIRMED** (the mutation target); phase tokens UPPERCASE pinned; envelope keys pinned.
**Mutation verification (LEARN-PERSIST precedent, cmp-proven restores):** M1 delete the `outcome != "acknowledged"` terminal guard — named kill in the disposition test; M2 make CONFIRMED derive from `command_result` acknowledged — named kill in the never-false-CONFIRMED lock; M3 delete the fingerprint comparison — named kill in the 409 test.

## What to Watch Out For

- **Tests must inject `Clock`.** Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` in this module's test code. Use `Clock.fixed(...)` / a mutable test clock injected via constructor. (§4c — rest-api is not whitelisted; convention applies everywhere.)
- **Record/factory name-collision STOP-check** on any new record (component accessor vs static factory).
- The `{data, meta}` envelope is the INLINE idiom — do not extract a shared helper (MODULE_CONTEXT M7.5c-a note).
- `X-Correlation-ID` request header is propagated to logs/responses but NEVER injected into event envelopes — `publishRoot` self-correlates.
- `ApiRequest`/`EndpointHandler` (Phase-2) are NOT the live seam — live handlers are `io.javalin.http.Handler` + package-private `apply(EndpointContext)` (P7). Match the live pattern.
- Jackson body parse: `FAIL_ON_UNKNOWN_PROPERTIES=false` posture — unknown body fields ignored, MISSING required fields are 400s.
- The dispatch subscriber consumes the published event asynchronously in LIVE mode — endpoint tests assert the PUBLISH, never downstream effects (those are the pipeline's proven property).
- Javalin route registration happens inside the erased-Object cast idiom — copy an existing install method wholesale as the skeleton.

## Coder Pushback Welcome
If any DP is impractical, contradicts a MODULE_CONTEXT gotcha, or has a better same-contract shape — raise it with evidence. DP-2's envelope duplication of `viewPosition` (data + meta) is deliberate (Phase-2 record fidelity + live meta idiom); push back if you find a live counter-precedent.

## Out of Scope
Webhooks (M10 amendment), batch commands, entity-disabled/integration-unhealthy checks, idempotency persistence, any dispatch/ledger/confirmation change, any event-model change, B2's bench port (separate WU), SKIP-VIS (separate WU), OpenAPI artifacts.

## Success Criterion — DONE when
1. Stage-A: all new tests written and RED for right reasons (reported per-test).
2. Stage-B: `:api:rest-api:test` + `:lifecycle:lifecycle:test` forced-fresh GREEN; full `./gradlew check` GREEN.
3. M1-M3 mutations killed with named kills + cmp-proven byte-identical restores + post-restore re-green.
4. Zero-change pins hold (module-infos, event-model, config schema byte-identical; `git diff --stat` corroborates).
5. MODULE_CONTEXT.md updated: inventory (+3 package-private), the wire-shape gotcha (DP-2 keys = frozen tokens the bench binds), the V1-subset record (DP-6), the install-gateway row.
6. WUCP Phase 1 checklist complete; completion report enumerates every DP with its evidence; the hub's two-layer audit precedes ANY commit.

## Build Discipline
Host-CC lane: targeted `./gradlew :api:rest-api:compileJava :api:rest-api:test :lifecycle:lifecycle:compileJava :lifecycle:lifecycle:test` during the loop; ONE full `./gradlew check` at the end. CI on the pushed commit remains the gate of record (push on the hub's order, via Nick).
