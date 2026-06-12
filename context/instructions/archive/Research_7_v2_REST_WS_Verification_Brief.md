<!--
file: context/instructions/Research_7_v2_REST_WS_Verification_Brief.md
purpose: Research 7 v2 brief — re-anchored verification + extension of the REST/WebSocket API research (v1 graded C-, 15 §7 fabrications). Dispatch to the HomeSynapse CORE Claude Project.
audience: External researcher (Claude Project), PM
state-type: instruction
status: READY TO DISPATCH — authored 2026-06-05, source-verified vs HEAD `e73e199`
predecessor: context/assessments/2026-05-22_Research_7_PM_Assessment.md (v1 dispositions are the canonical baseline)
-->

RESEARCH BRIEF: Research 7 v2 — REST and WebSocket API Design for Event-Sourced Smart Home Systems (Verification + Re-Anchor)

**AUTHORITATIVE STATE HEADER (per your custom instructions, this is the only source of "now"):** `homesynapse-core` HEAD `e73e199` · amendment watermark **AMD-53** · `projectionVersion` **5** · M4.B-S2 (EntityRole) in flight. Your knowledge-base ledger files (Current_State, Knowledge_Primer, etc.) predate this state — the GitHub connector (`main`) and the verbatim embeds below are authoritative; the ledger orients only.

You are the PM/architect for HomeSynapse Core, a local-first event-sourced smart home runtime in Java 21 (JPMS, Gradle multi-module, SQLite event store, virtual threads, Javalin HTTP). Produce a research document with EXACTLY these sections (the mandatory format — self-contained here, do not look for it elsewhere): **§1 Executive Summary** (verdict-led); **§2 Platform Deep Dives** (primary-source-cited); **§3 Cross-Cutting Analysis**; **§4 Amendment Recommendations** (numbered RECs with positions, evidence, effort-in-LOC); **§5 Caveats and Open Questions**; **§6 Appendix: Sources** (URLs); **§7 Code-Level Implications** (subject to the QUOTE-BACK RULE below).

**Design-doc access note:** this Project holds the live code, not the design docs. The design-contract facts you need (Doc 09 §4.3–§4.5 command surface, Doc 10 filter semantics, AMD-44 §3 REST/WS additions) are embedded below as verified facts. If a question genuinely turns on fuller design-doc text, list it in §5 as an excerpt request for the PM — do not assume the contents.

## Why a v2 exists (read first)

Research 7 v1 (2026-05-22) was assessed at grade **C-**: its §1–§3 analysis was strong (bcrypt timing analysis, three-stage backpressure defense, INV-SE-02 disclosure discipline), but its **§7 contained 15 source-verified fabrications** — the worst of any research document — including a CRITICAL fully-fabricated JPMS `module-info.java` block (F12) that ignored the verbatim embeds in the brief. The PM's corrected disposition table (6 ACCEPT, 7 ACCEPT+MODIFY, 1 REJECT across REC-62..75) is **canonical** and is reproduced below. v2 has three jobs:

1. **Repair §7 against the verbatim source embedded below** — every type, module, package, dependency, and event name quoted back exactly.
2. **Cover the API surface that has appeared since v1's baseline** (`76288af` → `e73e199` — the codebase moved substantially; deltas below).
3. **Pressure-test the seven pending NQ leans with external evidence** — NQ-1..7 are Nick's open calls; bring prior-art evidence for or against each lean. Do not assume they are decided.

## MANDATORY QUOTE-BACK RULE (new, non-negotiable)

In §7, before proposing ANY change to a module, **quote the verbatim `module-info.java` block embedded in this brief back into your document**, then show your proposed diff against it. Any §7 claim about an existing type must cite the verified inventory lines below. A §7 that paraphrases module or type names will be rejected without assessment. (This rule exists because v1 recurred the Research 6 JPMS-fabrication failure mode at greater scale despite full embeds.)

## Canonical v1 baseline (do not re-litigate without new evidence)

Dispositions (PM-corrected, canonical): REC-62 ACCEPT-MODIFY (reuse `PagedResponse<T>`, place `EventQueryService` question in event-model where `EventStore` lives); REC-63 **REJECT** (existing Doc 09 §4.3–§4.5 command surface stands; only genuine addition = nullable `timedInteractionMs` on `CommandRequest`); REC-64 ACCEPT-MODIFY (annotation processor approach OK; `@Capability` must be renamed — clash with device-model sealed `Capability`); REC-65 ACCEPT-MODIFY (8 net-new `WsSubscriptionFilter` fields; RE2/J = new catalog dependency); REC-66 ACCEPT-HEAVY-MODIFY (scope enum renamed `ApiKeyScope`-style; drop `legacy(...)` factory); REC-67 ACCEPT-MODIFY (webhooks; separate webhook DLQ from subscriber DLQ); REC-68 ACCEPT-MODIFY (RFC 9457 everywhere; `urn:` scheme lean; actual type is `ErrorMsg`, NOT `WsErrorMsg`); REC-69 ACCEPT (`CaughtUpMsg`); REC-70 ACCEPT-MODIFY (`PingMsg`/`PongMsg` ALREADY EXIST — REC is semantics only; WsCloseCode collisions must renumber per NQ-5); REC-71 ACCEPT-MODIFY (bcrypt-then-cache; fix the broken `byte[]` map key; patrickfav/bcrypt = new catalog dependency); REC-72 ACCEPT-MODIFY (COALESCED policy; real event names; `(entityId, attributeKey)` key lean); REC-73 ACCEPT (signed-URL WS command); REC-74 ACCEPT (CLI first-key bootstrap); REC-75 ACCEPT (reject mTLS/IP-whitelist/wildcard-CORS).

The 15-fabrication catalogue (F1–F15) and the full disposition rationale are in `context/assessments/2026-05-22_Research_7_PM_Assessment.md` — treat it as part of this brief.

**Pending NQ-1..7 (Nick's calls — pressure-test, don't assume):** NQ-1 keep Doc 09 `/commands` surface + `timedInteractionMs` field; NQ-2 rename API scope enum (`ApiKeyScope`); NQ-3 `ProblemType.typeUri()` → `urn:homesynapse:problem:<slug>`; NQ-4 separate webhook DLQ store + `/internal/webhook-failures`; NQ-5 conservative WsCloseCode renumbering (keep existing 5 untouched); NQ-6 coalescing key `(entityId, attributeKey)`; NQ-7 annotation rename (`@CapabilityType`/`@ApiCapability`). For each: cite how HA, openHAB, EventStoreDB, Hue Bridge v2, or comparable systems resolved the analogous choice, and either CONFIRM the lean or argue the override with evidence.

## What changed since v1's baseline `76288af` (v2 must account for ALL of these)

1. **New `core/value-model` module** (`com.homesynapse.value`, leaf, `java.base`-only): the `AttributeValue` sealed hierarchy (8 variants: BooleanValue, IntValue, FloatValue, StringValue, EnumValue, QuantityValue, ArrayValue, DegradedAttributeValue) + `AttributeType` relocated out of device-model (M4.0b-4a).
2. **Typed `StateChangedEvent` payload (AMD-52, shipped):** `oldValue`/`newValue` are now typed `com.homesynapse.value.AttributeValue` (nullable `oldValue`), serialized in persistence as a compact tagged union `{"t":<AttributeType>,"v":…[,"u":…]}` with bit-anchored float identity and non-finite sentinels; per-event `schema_version` discriminator 1→2. **v2 question Q-A:** what should REST event-history responses and WS event frames expose for attribute values — the same `{"t","v"[,"u"]}` envelope, a flattened JSON-native form, or both behind a representation parameter? Survey how EventStoreDB/HA WS API expose typed payloads; mind INV-SE-02 and the Pi-4 serialization budget.
3. **AMD-53 (shipped):** all three `EntityState` activity timestamps (`lastChanged`/`lastUpdated`/`lastReported`) are event-time-deterministic. **v2 question Q-B:** confirm REST entity-state representations should expose all three + `stale`/`staleAfter` (wall-clock carve-out) and how peers present the same split.
4. **AMD-44 Stage 1 (shipped) + Stage 2 (in flight, M4.B-S2):** Floor/Area aggregates + EntityRole. This adds a REST/WS surface v1 never saw — **the main genuinely NEW research scope for v2 (Q-C):**
   - `/api/v1/floors` CRUD incl. **DELETE cascade protection** (Decision 11: 409 + `affectedAreaIds` unless `?force=true`; `area_floor_unassigned` events emitted before `floor_deleted`) — survey prior art for cascade-delete REST conventions and pitfalls (HA 2024.4 floors, Hue rooms/zones).
   - `?floorId=` / `?entityRole=` query filters on entity collections.
   - WS subscription filter semantics (Decision 10): `"floorId": null` = unassigned bucket; **absent** = no floor filtering — same for `entityRole`. Survey how peers disambiguate null-vs-absent in subscription filters and where that bites.
   - Pagination/filter interaction with the existing `WsSubscriptionFilter` 10-field record (verified inventory below).
5. **Javalin remains 6.7.0**; rest-api wiring now real (readiness gate 503 + RFC 9457 body, entity/admin endpoints, 16-step `HomeSynapseCore` bootstrap, port 7070).

## VERIFIED IDENTIFIERS YOU MUST USE (verbatim — quote back in §7)

`api/rest-api/src/main/java/module-info.java` at `e73e199`:
```java
module com.homesynapse.api.rest {
    requires transitive com.homesynapse.state;
    requires com.homesynapse.event.bus;

    requires io.javalin;
    requires org.slf4j;

    exports com.homesynapse.api.rest;
}
```
(Javadoc/comments elided here only; the module declaration above is exact. Single flat package `com.homesynapse.api.rest`.)

`api/websocket-api/src/main/java/module-info.java` at `e73e199`:
```java
module com.homesynapse.api.ws {
    requires transitive com.homesynapse.api.rest;

    exports com.homesynapse.api.ws;
}
```
(Single flat package `com.homesynapse.api.ws`. Phase 3 will add event-model/event-bus/state-store/device-model/Jackson edges — propose them as diffs, never as fabricated module names.)

Verified type facts (from the PM assessment's source verification — use exactly):
- WebSocket types are ONLY: `WsCloseCode`, `WsSubscriptionFilter` (10 fields), `WsMessage` (sealed), `WsSubscription`, `WsClientState`, plus message permits incl. `PingMsg (id)`, `PongMsg (id, serverTime)`, and `ErrorMsg (id?, errorType, detail, fatal)` — there is **no `WsErrorMsg`**.
- `WsCloseCode` existing 5 values: `AUTH_FAILED(4403)`, `AUTH_TIMEOUT(4408)`, `CLIENT_TOO_SLOW(4429)`, `SUBSCRIPTION_LIMIT(4409)`, `MALFORMED_MESSAGES(4400)`.
- REST command surface (Doc 09 §4.3–§4.5, existing): `POST /api/v1/entities/{entity_id}/commands` + `CommandRequest` (3 fields) + `CommandAcceptedResponse` (6 fields) + `GET /api/v1/commands/{command_id}` → `CommandStatusResponse` (8 fields). Pagination container: `PagedResponse<T>` (data, pagination, meta).
- Error model: `ProblemDetail` (7 fields) + `ProblemType` (13 values + `STATE_STORE_REPLAYING`; `typeUri()` currently `https://homesynapse.local/problems/<slug>`).
- Event naming convention: snake_case legacy (`state_changed`, `state_reported`, `config_changed`) + subsystem-dot-form for new events (`automation.run.started`, `config.section_reloaded`). **No `homesynapse.*` prefix. No `EntityStateChanged`.**
- Identity: typed ULID wrappers (LTD-04), now NINE: DeviceId, EntityId, AreaId, IntegrationId, AutomationId, PersonId, HomeId, SystemId, **FloorId** (Crockford Base32 at API boundaries).
- Dependency catalog (`gradle/libs.versions.toml`): `javalin = "6.7.0"`; Jackson 2.x locked by LTD-08 at the catalog pin. `com.google.re2j`, `at.favre.lib:bcrypt`, swagger-core are **NOT in the catalog** — any use requires an explicit catalog-addition proposal with version pin (F13 lesson).

## CONSTRAINTS
- Take positions. "X is worth investigating" is banned.
- Cite primary sources (docs, issue trackers, maintainer statements) with URLs.
- Every REC: effort estimate in LOC.
- Keep REC-62..75 identifiers for revisions of v1 items; NEW recommendations number from **REC-106** (REC-100..105 consumed by Research 11).
- AMD integers: do NOT assign. The v1 AMD-72..85 labels are assign-at-milestone placeholders (P2 renumbering decision); refer to RECs only.
- INV-SE-02 (network security surface), LTD-08 (Jackson 2.x), LTD-09 (YAML config), LTD-11 (ReentrantLock, no synchronized — virtual threads), no `ServiceLoader` (DECIDE-04), Javalin abstraction only — no direct Jetty/`jakarta.servlet` requires (F14).
- §7 must follow the QUOTE-BACK RULE above.

OUTPUT: a single complete markdown document in the mandatory format. Do not truncate.
