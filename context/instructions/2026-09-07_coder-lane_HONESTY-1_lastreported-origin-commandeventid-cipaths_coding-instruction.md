<!--
file: context/instructions/2026-09-07_coder-lane_HONESTY-1_lastreported-origin-commandeventid-cipaths_coding-instruction.md
purpose: THE HONESTY BATCH — one small Core WU, four value corrections and no wire-shape change (the assessment §3 "the honesty batch"; D6): (A) LASTREPORTED-1 — `StateProjection.initialEntityState` seeds `lastReported` NULL until the first `state_reported` (HERO-0 F1; Nick's D4 word `F1: seed-null`; the AMD-53 §1.5 correction paragraph the hub applied to the docs tree rides Nick's docs commit FIRST); (B) ORIGIN-1 — `command_dispatched` and the router's own `command_result` INHERIT the issued envelope's `origin` + `actorRef` on the bus path, and the in-process primitive stamps `UNKNOWN` (TR-0 TR0-3; `EventOrigin`'s own law); (C) TR0-1 — the `CommandEnvelope.commandEventId` javadoc says what the router actually passes (the `command_issued` id); (D) CI-PATHS-1 — install-smoke's push path filter DROPPED in both copies (every Java push builds the `.deb`; the F-R4-1b audit's docket). One lane; one commit by Nick; CI on his push is the gate of record and the sample.
audience: the Coder lane (host-side Claude Code in homesynapse-core) · the hub (audit) · Nick (dispatches; commits docs then core; pushes)
state-type: coding instruction
status: EXECUTED (v69 beat 1 — LANDED core `94ae99d` Thu 2026-09-10, ci GREEN, install-smoke per push; audit filed v68 b4). Was: ISSUE-READY (v67 beat 4, Mon 2026-09-07; instrument 2026-09-07T23:5xZ). baseline: core `39c8dd3` (F-R4-1b landed; porcelain 0 at authoring). Dispatches on Nick's paste after `PELTON: sent` (the core slot is free; TR-1 is read-only and off the core tree — two lanes under the cap).
-->

# Coding Task: HONESTY-1 — four value corrections (lastReported · origin · commandEventId javadoc · the install-smoke paths)

**Subsystems:** `core/state-store` (A) · `core/automation` (B) · `integration/integration-api` (C, javadoc only) · `.github/workflows` + `distribution/ci` (D). **No new types, no new public methods, no module-info change, no schema/wire-shape change** — every event and DTO keeps its keys; three VALUES become true and one filter goes.
**Design Docs:** Doc 03 (state store; AMD-53 RATIFIED, §1.5 as CORRECTED 2026-09-07 — the paragraph is on the docs tree, Nick commits it before your landing) · Doc 01 §3.9 (Event Origin — evidence-based; `UNKNOWN` is the default) · Doc 07 §3.11.2 (command causality) · the v1.1.3 dashboard read-API freeze (`api/rest-api/MODULE_CONTEXT.md` §A1: `lastReported` "the projection holds none" → `null`).
**Task Brief Reference:** `context/planning/2026-09-06_v66_STATE-OF-THE-PROGRAM_assessment_trajectory_and_hygiene-program.md` §3 "the honesty batch" · HERO-0 audit F1 (`context/audits/2026-09-06_HERO-0_intake_two-layer-audit_v66-b6.md` :12–:15) · TR-0 audit TR0-1 + TR0-3 (`context/audits/2026-09-06_TR-0_intake_two-layer-audit_v66-b5.md` :26, :28) · F-R4-1b audit CI-PATHS-1 (`context/audits/2026-09-06_F-R4-1b_intake_two-layer-audit_v66-b8.md` :43).

## §0 The lane contract (read first)
- **`date -u` FIRST**; state your instrument limit; re-derive CT as UTC−5 once.
- **Return path:** `nexsys-hivemind/context/audits/<CT-filing-date>_HONESTY-1_return.md` — ONE file. §0 card FIRST (≤3 KB: the census `N = a M + b A` with exact paths · the red-first table · deviations by tag · P1–P4 adjudicated) · §1 what changed per file · §2 the gates run + counts (each module's `:test` suite count before/after; `compileJava` under the build's `-Werror`; `spotlessCheck`) · §3 pushback/observations · §4 the WUCP Phase-1 checklist. **≤10 KB is a CEILING, not a target; the §0 card is what the hub reads first; a shorter return with the same receipts is a better return.** Last line: `RETURNED <path> <bytes>`.
- **Baseline:** `39c8dd3`, porcelain empty — verify `git log -1 --format=%h` and `git status --porcelain` (STOP and report if not). Every `:line` cite below was read at `39c8dd3`.
- **Build discipline:** targeted Gradle on your desk (`./gradlew :core:state-store:test :core:automation:test :core:persistence:test :core:state-store:compileJava :core:automation:compileJava spotlessCheck --offline`); the full `./gradlew check` is CI on Nick's push = the gate of record. **You commit nothing; stage nothing.** Nick lands it as ONE commit.
- **Tests first** (red-first): every new test RUNS RED at HEAD before the production edit, except the rows marked green-by-construction (law #18) — those are disclosed, not claimed.
- **No words to give.** A deviation is filed in §0 with its cause; a `[REVIEW]` is a question the hub answers at audit, never a reason to stop.

## What This Implements
Four honesty fixes the hero's three questions read: (A) `lastReported` means "the last report" — never the registration instant; (B) `command_dispatched.origin` is the issuing envelope's origin (a REST command reads `USER_COMMAND`, an automation's reads `AUTOMATION`), and `actorRef` travels with it; (C) the envelope javadoc names the id the router really passes; (D) every push on `main`/`develop` builds and smoke-installs the `.deb` — the R-4c artifact and a CI sample per push.

## Files to Read Before Starting (minimum read set — MANDATORY)
1. `core/state-store/src/main/java/com/homesynapse/state/StateProjection.java` — `initialEntityState` (`:976–:1001`), the `applyToState` LIVE branches that carry `prior.lastReported()` (`:839–:875`), the backfill path (`:962–:972`), the class javadoc on the three timestamps (`:773–:784`, `:907–:935`).
2. `core/state-store/src/main/java/com/homesynapse/state/EntityState.java` — the record (`:64–:93`): `lastReported` is an `Instant` component with no non-null check; the javadoc `:73`.
3. `core/state-store/src/test/java/com/homesynapse/state/ReconciliationTest.java` — the AMD-53 §5 group (`:638` onward; #2 at `:642–:657`, the null-fallback at `:713–:733`, #4 at `:740`).
4. `core/persistence/src/main/java/com/homesynapse/persistence/CheckpointSerializer.java` `:236–:300` (the `SerializableEntityState` record; `staleAfter` already round-trips null) + `CheckpointSerializerTest.java`.
5. `api/rest-api/src/main/java/com/homesynapse/api/rest/ListEntitiesEndpoint.java` `:203–:204` (already `null`-safe — read, do not touch) + `api/rest-api/MODULE_CONTEXT.md` `:299` (the freeze row).
6. `core/automation/src/main/java/com/homesynapse/automation/StandardCommandDispatchService.java` WHOLE (243 lines): `dispatch` `:135–:146`, `onEvent` `:165–:178`, `route` `:187–:203`, `publishDispatched`/`publishResult` `:217–:229`, `publish` `:231–:243` (the `EventDraft` at `:233–:235` with `EventOrigin.AUTOMATION, payload, null, null`).
7. `core/event-model/src/main/java/com/homesynapse/event/EventOrigin.java` (the javadoc law `:7–:20`; `UNKNOWN` at `:82`) · `EventDraft.java` `:66–:76` (the record: `origin`, `actorRef` components) · `EventEnvelope.java` `:105–:112` (`origin()`, `actorRef()` accessors).
8. `core/automation/src/test/java/com/homesynapse/automation/AutomationTestSupport.java` `:386–:398` (`commandIssued(target, commandType, correlationId, causationId)` — hard-codes `EventOrigin.AUTOMATION` and `actorRef = null`) · `CommandDispatchSubscriberTest.java` (the bus-path tests, `:60–:90`) · `StandardCommandDispatchServiceTest.java` (the primitive's tests) · `testing/test-support/.../assertions/EventEnvelopeAssert.java` `:79` (`hasOrigin`).
9. `integration/integration-api/src/main/java/com/homesynapse/integration/CommandEnvelope.java` `:38–:52` (the javadoc) · `integration/integration-runtime/src/main/java/com/homesynapse/integration/runtime/CommandRoutingSubscriber.java` `:181–:231` (`routeDispatched`: `causationId = event.causalContext().causationId()` of the `command_dispatched` envelope = the `command_issued` id; passed as the envelope's `commandEventId` at `:229`).
10. `.github/workflows/install-smoke.yml` `:19–:26` and `distribution/ci/install-smoke.yml` (its header `:10–:14` explains the pair: the lane-owned source and the wired copy; the trigger blocks are byte-identical at HEAD).
11. `MODULE_CONTEXT.md` of `core/state-store` (§Cross-Module Contracts) · `core/automation` (§Cross-Module Contracts, §Gotchas) · `integration/integration-api` (§Gotchas — the `CommandEnvelope` gotcha).

## STOP-on-Mismatch Gates (read, then confirm before any edit)
- G1: `initialEntityState` passes `seed` three times (`:993–:1001`) — if the constructor call has changed shape, STOP.
- G2: `StandardCommandDispatchService.publish` builds `new EventDraft(eventType, SCHEMA_VERSION, null, SubjectRef.entity(targetRef), priority, EventOrigin.AUTOMATION, payload, null, null)` at `:233–:235` — if the draft carries anything but `AUTOMATION`/`null`/`null` there, STOP.
- G3: `EventOrigin.UNKNOWN` exists (`:82`); `EventEnvelope` exposes `origin()` and `actorRef()` — if either is absent, STOP.
- G4: no production reader filters command events by `origin` (`git grep -n 'origin()' -- '*.java' | grep -v src/test` returns only `EventEnvelopeAssert`) — if a reader exists, STOP and name it.
- G5: the two install-smoke trigger blocks are identical (`diff` the `on:` blocks) — if they differ, STOP.

## Files to Create or Modify (the Files table governs — addition #2)
| Path | Change | Part |
|---|---|---|
| `core/state-store/src/main/java/com/homesynapse/state/StateProjection.java` | `initialEntityState`: `lastReported` → `null`; the method javadoc + the class javadoc sentence on the seed re-worded (two of three timestamps seed; `lastReported` is owned by `state_reported` alone) | A |
| `core/state-store/src/test/java/com/homesynapse/state/ReconciliationTest.java` | + `#4b` in the AMD-53 §5 group (RED at HEAD) | A |
| `core/persistence/src/test/java/com/homesynapse/persistence/CheckpointSerializerTest.java` | + null-`lastReported` round-trip (green-by-construction, disclosed) | A |
| `core/state-store/MODULE_CONTEXT.md` | §Cross-Module Contracts: the `lastReported`-null bullet; §Amendments in force: AMD-53 §1.5 as corrected 2026-09-07 | A |
| `core/automation/src/main/java/com/homesynapse/automation/StandardCommandDispatchService.java` | `onEvent` captures the issued envelope's `origin()` + `actorRef()`; `dispatch` (the primitive) supplies `EventOrigin.UNKNOWN` + `null`; both are threaded `route → publishDispatched/publishResult → publish` and land on the `EventDraft` (`origin`, `actorRef`); javadocs on `dispatch`/`onEvent`/`publish` say so | B |
| `core/automation/src/test/java/com/homesynapse/automation/AutomationTestSupport.java` | + an OVERLOAD `commandIssued(target, commandType, correlationId, causationId, EventOrigin origin, Ulid actorRef)`; the existing 4-arg helper delegates to it with `AUTOMATION, null` (every current caller unchanged — the internal-consumer survey, law #1) | B |
| `core/automation/src/test/java/com/homesynapse/automation/CommandDispatchSubscriberTest.java` | + T-B1, T-B2 (RED at HEAD), T-B4 (green-by-construction, disclosed) | B |
| `core/automation/src/test/java/com/homesynapse/automation/StandardCommandDispatchServiceTest.java` | + T-B3 (RED at HEAD) | B |
| `core/automation/MODULE_CONTEXT.md` | §Cross-Module Contracts: the command-event provenance bullet; §Gotchas: the primitive stamps `UNKNOWN` | B |
| `integration/integration-api/src/main/java/com/homesynapse/integration/CommandEnvelope.java` | the `commandEventId` javadoc (`:46–:49`) — text in Part C | C |
| `integration/integration-api/MODULE_CONTEXT.md` | the `CommandEnvelope` gotcha gains one sentence (Part C) | C |
| `.github/workflows/install-smoke.yml` · `distribution/ci/install-smoke.yml` | the `push:` `paths:` line REMOVED in BOTH (the `branches`, the `pull_request` block and `workflow_dispatch` unchanged); the pair stays byte-identical in the `on:` block | D |
**Predicted census: 12 M + 0 A.** Zero new files; zero `module-info.java` edits (validated: no new public type, no new edge — Part B threads two existing types already imported; SLF4J already required).

## Technical Specification
### Part A — LASTREPORTED-1 (`core/state-store`)
`initialEntityState(entityId, seed)` returns `new EntityState(entityId, Map.of(), Availability.UNKNOWN, 0L, seed, seed, null, null, false)` — positions: `lastChanged = seed`, `lastUpdated = seed`, **`lastReported = null`**, `staleAfter = null`, `stale = false`. Every LIVE and backfill branch already carries `prior.lastReported()` forward and only the `state_reported` branch writes it — verify by reading, change nothing there. Determinism (AMD-53 §4) holds: `null` is a pure function of the log. `staleAfter` semantics untouched (AMD-53-INV-02). The serializer: `SerializableEntityState.lastReported` is a Jackson `Instant` that already carries `null` (as `staleAfter` does) — prove it with the round-trip test, change no code. The read-API already renders `null` (`ListEntitiesEndpoint:203–:204`). **Docs:** the AMD-53 §1.5 correction paragraph is hub-applied to the docs tree; Nick's docs commit precedes the core landing — you do not touch the docs repo.

### Part B — ORIGIN-1 (`core/automation`)
Thread a provenance pair through the router. Recommended shape (the observable contract is the tests; the threading is yours): `route(EntityId, String, Map, CausalContext, EventOrigin origin, Ulid actorRef)` → `publishDispatched(…, origin, actorRef)` / `publishResult(…, origin, actorRef)` → `publish(…, origin, actorRef)` → `new EventDraft(eventType, SCHEMA_VERSION, null, SubjectRef.entity(targetRef), priority, origin, payload, actorRef, null)`. Sources: **bus path** `onEvent` → `event.origin()`, `event.actorRef()` (the `command_issued` envelope is the evidence — Doc 01 §3.9); **in-process primitive** `dispatch(commandEventId, …)` → `EventOrigin.UNKNOWN`, `null` (no envelope in hand; the enum's law: "the system never guesses origin"; `AUTOMATION` here was a guess). A private record `Provenance(EventOrigin origin, Ulid actorRef)` is acceptable if it stays package-private (no public type → no module-info/export change). `idempotencyKey` stays `null` on the router's drafts (unchanged). The `CommandDispatchService` INTERFACE is untouched.

### Part C — TR0-1 (`integration/integration-api`, javadoc only)
Replace the `commandEventId` javadoc (`:46–:49`) with: *"the event ID of the originating `command_issued` event — the supervisor's `CommandRoutingSubscriber` passes the `command_dispatched` envelope's causation id, which is the `command_issued` id (Doc 07 §3.11.2); used as the causation ID of the resulting `command_result` event; never `null`"*. Behaviour unchanged; no test. (Whether the router's OWN failure results should chain to the same id is a B-2 question — TR0-2 — not this WU.)

### Part D — CI-PATHS-1 (both install-smoke copies)
Delete the `paths: [ 'distribution/**', 'app/**', 'lifecycle/**', 'api/**', 'gradle/**', 'build-logic/**', '.github/workflows/install-smoke.yml' ]` line under `push:` (`.github/workflows/install-smoke.yml:22` and the identical line in `distribution/ci/install-smoke.yml`). Leave `branches: [ main, develop ]`, the whole `pull_request:` block and `workflow_dispatch: {}` as they are. Validate both files parse (`python3 -c "import yaml,sys; yaml.safe_load(open(sys.argv[1]))" <file>` or the repo's lint step). Effect: every push on `main`/`develop` runs install-smoke; its artifact is R-4c's `.deb`.

## Locked Decisions That Apply
AMD-53 (RATIFIED; §1.5 as corrected 2026-09-07) · AMD-53-INV-01/-02 · Doc 01 §3.9 (`UNKNOWN` default; no heuristics) · Doc 07 §3.11.2 (correlation = the Run's, causation = the `command_issued` id — untouched) · the v1.1.3 read-API freeze (keys and dialects untouched; one null arm becomes reachable) · LTD-15 (no SLF4J on exported API — unchanged).

## Invariants That Must Hold
- No `EntityState` shape change; no event key added or removed; `schema_version`s untouched.
- `stateVersion`, `lastChanged`, `lastUpdated` seeding and advancement exactly as at HEAD.
- Correlation/causation chains exactly as at HEAD (T-B1/T-B2 assert them unchanged beside the new fields).
- `CommandDispatchService`'s public surface unchanged (its shape is consumed by the assembly and the tests).

## P2 Consumer/Pin (Fan-Out) Survey (done at authoring at `39c8dd3`; re-run the greps)
- `lastReported()` production readers: `ListEntitiesEndpoint:203–:204` (null-safe) · `CheckpointSerializer:241/:262/:284` (pass-through) · `MaterializedStateQueryService:234/:285` (pass-through to a summary record — confirm the summary's component is a plain `Instant` with no non-null check; if one exists, it is a `[REVIEW]` with the line). `RestFilters:157` mentions it in a javadoc only.
- `lastReported()` test readers that could flip: `ReconciliationTest:657/:682/:707/:730/:794–:802` — each follows a `state_reported`; prediction: **0 go red**. `EntityStateTest:113` constructs the record directly — unaffected.
- `command_dispatched`/`command_result` origin readers: production **none** (G4); tests: `HeroLoopHardwareFreeIT`, `RunPipelineConfirmWiringTest`, `CommandRoutingSubscriberTest` consume AUTOMATION-origin issued fixtures → still `AUTOMATION` after inheritance; prediction: **0 go red**.
- `AutomationTestSupport.commandIssued` callers: every call site keeps the 4-arg shape (the overload adds; nothing edits).
- **ARCH-RULE-REACH:** no new cross-module publish or edge; `NO_DIRECT_TIME_ACCESS` reach unchanged (no clock reads added).

## Test Requirements (tests first; red at HEAD unless marked)
| Id | Home | Assertion | At HEAD |
|---|---|---|---|
| A-#4b | `ReconciliationTest` (AMD-53 §5 group) | adopt an entity through a `state_changed` (LIVE) at event-time T0 → `lastChanged == T0`, `lastUpdated == T0`, **`lastReported == null`**, `staleAfter == null`, `stale == false`; then a `state_reported` at T1 → `lastReported == T1`, `lastChanged` unchanged | **RED** (first assertion) |
| A-ser | `CheckpointSerializerTest` | an `EntityState` with `lastReported == null` round-trips to `null` (and a non-null one to itself) | green-by-construction — DISCLOSED |
| T-B1 | `CommandDispatchSubscriberTest` | a `USER_COMMAND` issued envelope with `actorRef = X` → the `command_dispatched` envelope has `origin == USER_COMMAND` and `actorRef == X`; correlation/causation as at HEAD (`:76–:79`) | **RED** |
| T-B2 | `CommandDispatchSubscriberTest` | the same envelope on an UNROUTABLE target → the router's `command_result` has `origin == USER_COMMAND`, `actorRef == X` | **RED** |
| T-B3 | `StandardCommandDispatchServiceTest` | `dispatch(commandEventId, …)` → `command_dispatched.origin == UNKNOWN`, `actorRef == null` | **RED** |
| T-B4 | `CommandDispatchSubscriberTest` | an `AUTOMATION` issued envelope → `origin == AUTOMATION` (regression) | green-by-construction — DISCLOSED |
Use `Clock.fixed(…)` fixtures as the existing tests do; use `EventEnvelopeAssert.hasOrigin` where it fits.

## MODULE_CONTEXT.md Update
Three files, one bullet/gotcha each as the Files table says; date each entry 2026-09-07 (HONESTY-1).

## What to Watch Out For
- **Tests must inject `Clock`.** Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` in this module's test code. Use `Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC)` injected via constructor/`@BeforeEach`. **Enforcement reach:** `NO_DIRECT_TIME_ACCESS` runs from `com.homesynapse.app`'s test classpath, so it mechanically catches PRODUCTION code in every non-whitelisted module (plus app's own tests) — it does **not** scan this module's test source set. Clock-injection here is a self-enforced project convention that PM review, not `./gradlew check`, enforces.
- Do not "fix" `lastChanged`/`lastUpdated` seeding — AMD-53 §1.5 keeps them event-time-seeded; only `lastReported` changes.
- Do not add an `origin` parameter to the `CommandDispatchService` interface — the primitive stamps `UNKNOWN`; widening the interface is a different WU.
- Do not touch `CommandRoutingSubscriber` or the Zigbee handler (TR0-1 is a javadoc; the causation convention is TR0-2/B-2's).
- Keep the two install-smoke files identical in their `on:` blocks; do not touch the jobs.
- `-Werror` is on: an unused parameter or import fails the build.

## Coder Pushback Welcome
If a `lastReported()` reader with a non-null contract exists that the survey missed, or if threading provenance through `route` reads worse than a small package-private record, say so in §3 with the line — the hub rules at audit.

## Out of Scope
`firstSeen` (rejected by the F1 word) · any EXPLAIN v1.1.4 key · the FE (FE-NULL-1 is its own lane) · the causation convention (TR0-2 → B-2) · a store read to derive the primitive's origin · the docs repo (hub-applied; Nick's commit) · the bench.

## Success Criterion (binary)
The five targeted tests A-#4b, T-B1, T-B2, T-B3 go RED at HEAD and GREEN after; the disclosed two stay green; every existing suite count is unchanged or +1 per added test; `compileJava` (`-Werror`) and `spotlessCheck` clean; both YAML files parse and their `on:` blocks are identical. Then, on Nick's push: `ci` GREEN (the passive sample) AND `install-smoke` RUNS on the push (P-D) with both jobs GREEN and the `distribution-artifacts-arm64` artifact present = R-4c's `.deb` (Act 12 retired).

## Predictions (pre-registered; adjudicate in §0)
P1 census `12 M + 0 A` · P2 the four RED rows are red at HEAD for the reason stated (a value, not a compile error) · P3 zero existing tests go red (the survey) · P4 (Nick's push) install-smoke runs without a manual dispatch and both jobs are green.

## Work Unit Completion (WUCP Phase 1)
After your desk gates pass: the three MODULE_CONTEXT entries; the `coder-handoff.md` entry (Deferred Build Gate: YES — the full `./gradlew check` is CI on Nick's push; NEXT WU pointer: the hub's audit → the msg file + census card → Nick's docs commit (AMD-53 §1.5 correction) → the core commit + push → CI green + install-smoke green = the gate → **the v1.1.4 EXPLAIN batch** (the assessment §3)); a `coder-lessons.md` note only if you learned one; the checklist in the return.

### DISPATCH LINE (Nick pastes into a host-side Claude Code session in `~/Desktop/Code/ClaudeFolder/homesynapse-core`; the core slot is free at `39c8dd3`)
```
date -u first. Boot as the nexsys-coder skill. Baseline: this tree must be at 39c8dd3 and clean — verify with `git log -1 --format=%h` and `git status --porcelain` (STOP and report if not). Execute nexsys-hivemind/context/instructions/2026-09-07_coder-lane_HONESTY-1_lastreported-origin-commandeventid-cipaths_coding-instruction.md exactly: read its §0 contract and the minimum read set first; confirm gates G1–G5. Tests first (A-#4b, T-B1, T-B2, T-B3 red at HEAD; A-ser and T-B4 disclosed green-by-construction), then the four parts A–D, then the MODULE_CONTEXT entries and the coder-handoff entry. Targeted Gradle only; commit nothing, stage nothing. Write nexsys-hivemind/context/audits/<today's CT date>_HONESTY-1_return.md (≤10 KB, §0 card first, P1–P4 adjudicated). Your last line: RETURNED <path> <bytes>. You report to the hub.
```
