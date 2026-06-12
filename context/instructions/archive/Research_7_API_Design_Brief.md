<!--
file: context/instructions/Research_7_API_Design_Brief.md
purpose: Self-contained prompt for the Claude Project to produce Research 7 (REST and WebSocket API Design for Event-Sourced Smart Home Systems).
audience: Nick (paste into Claude Project conversation)
state-type: ephemeral
-->

# RESEARCH BRIEF: Research 7 — REST and WebSocket API Design for Event-Sourced Smart Home Systems

You are the PM/architect for HomeSynapse Core, a local-first event-sourced smart home runtime in Java 21 targeting Raspberry Pi 4/5. Your task is to produce a research document following the exact format specified below.

## Mandatory Format

Every research document must follow this structure. Non-negotiable sections are marked **[M]**; optional sections are marked **[O]**.

```
# Research 7: {Title} — {Subtitle}

*Target: HomeSynapse Core M10 (REST API) + M11 (WebSocket API). Date: YYYY-MM-DD.*

## 1. Executive Summary [M]
  - 5-8 bullet points, each a **verdict** with a bold claim and one-sentence defense.
  - Every bullet must take a position. "X is worth investigating" is banned.
    Use "X should be adopted because Y" or "X should be rejected because Y."
  - Flag the single highest-impact finding explicitly.

## 2. Platform / Literature Deep Dives [M]
  - One subsection per platform or prior-art system studied.
  - Each subsection must include:
    (a) How the platform solves the problem under investigation.
    (b) At least one direct quotation from primary source (docs, issue tracker,
        maintainer statement) with URL.
    (c) Known pain points / failure modes from community reports.
    (d) Specific lesson for HomeSynapse (not generic observation).

## 3. Cross-Cutting Analysis [M]
  - Concept Mapping Table: HomeSynapse concept | Platform A | Platform B | ...
  - Gap Analysis: concepts present in 2+ platforms that HomeSynapse lacks,
    ranked by impact.
  - Over-Abstraction Analysis: concepts HomeSynapse has that no one needs,
    with defense or retraction for each.
  - Competitive Assessment: where HomeSynapse is genuinely differentiated,
    with the precise qualifying language that survives scrutiny.

## 4. Amendment Recommendations [M]
  - Ranked by (impact × confidence) / cost.
  - Each REC must include: Gap citation, Lesson source, Change (specific
    record/interface/event shape), Backward compat assessment, Effort estimate.
  - REC-XX format. Numbered globally: Research 5 used REC-53 through REC-61.
    This document starts at REC-62.

## 5. Caveats and Open Questions [M]
  - Source reliability notes.
  - Unresolved tensions between platforms.
  - Questions that require empirical validation (spike/prototype).
  - Section 5.4 MANDATORY: explicit conflict-with-inventory disclosure — if any
    finding contradicts the verified MODULE_CONTEXT inventory or the locked
    decisions register embedded below, surface it here rather than silently
    breaking the inventory. This is the Research 5 lesson encoded.

## 6. Appendix: Sources [M]
  - URL families grouped by platform.
  - Every factual claim must be traceable to a source listed here.

## 7. HomeSynapse Code-Level Implications [M — required for this research]
  - Specific records, interfaces, sealed hierarchy changes.
  - Event schema additions.
  - MODULE_CONTEXT impact (which modules gain/change types).
  - JPMS module-info impact.
  - For each proposed type change, specify: (a) exact module, (b) exact package,
    (c) public vs package-private visibility, (d) whether it requires an AMD.
```

---

## SCOPE

The REST API (Doc 09) and WebSocket API (Doc 10) are HomeSynapse's external surface to operators, dashboards, the Web UI, the future Companion App, third-party integrations, and the NexSys cloud relay. Phase 2 type vocabularies are complete for both modules: rest-api has 28 public types + 10 package-private types (38 total post-M3.6e.2); websocket-api has 26 Java files including the full WsMessage sealed hierarchy (13 subtypes) and the three-stage backpressure model (NORMAL → BATCHED → COALESCED). M3.6e.1 added the readiness gate; M3.6e.2 added five package-private endpoint handlers (three entity query endpoints under `/api/*` + two admin endpoints under `/internal/*`) and two new `RestFilters` gateway methods.

What's missing is empirical validation against production smart-home and event-sourcing systems, gap analysis against the verified type inventory, and explicit answers to five M10/M11-bound design questions that will shape the full surface beyond the M3.6e.2 MVP slice. This research is sequenced now (after Research 5 v2 FINAL and after Research 6 v1) because **Research 7 is the only remaining MEDIUM-priority pre-M4 research item** and because it interacts with all four upstream research outputs:

- **Research 4 REC-39** lands 11 new automation event records in `com.homesynapse.event` (flat package) per AMD-52 — the WebSocket `WsSubscriptionFilter.eventTypes` must support filtering on these.
- **Research 5 REC-59** adds two new observability events `config.validation_completed` + `config.section_reloaded` in `com.homesynapse.event` per AMD-70 — WebSocket clients consuming validation diagnostics need filter support.
- **Research 6 REC-44** adds four new `IntegrationLifecycleEvent` records (dot-namespaced) per AMD-56 — WebSocket subscription filters must handle them.
- **Research 8 REC-23** adds `EntityCategory` to `Entity` — REST list endpoints will likely want category filtering, which interacts with `ListEntitiesEndpoint`'s current pagination contract (no category filter today).

### Specific questions to answer

1. **REST API design for event-sourced reads — pagination, filtering, response envelopes.** M3.6e.2 delivered an MVP endpoint set (`GET /api/v1/entities`, `GET /api/v1/entities/{id}`, `GET /api/v1/entities/{id}/state`, `GET /internal/dlq`, `GET /internal/projection`). The Phase 2 contract specifies keyset pagination with opaque Base64 `CursorToken` (3 fields: `sortValue`, `sortDimension`, `direction`), weak/strong ETag categories, and a 5-plane consistency model. **What additional endpoints does the full M10 surface need?** Survey Home Assistant's REST API, Matter's Interaction Model (Read, Write, Subscribe, Invoke), OpenHAB's REST API, EventStoreDB's HTTP API, Hubitat Maker API, SmartThings API. What pagination patterns survive contact with production? Is keyset universally correct or are there read patterns (e.g., "events in time range") where offset+limit is acceptable? What response envelope conventions (data + meta vs HAL vs JSON:API) reduce client coupling? Should the REST API expose a versioned schema endpoint (`GET /api/v1/schema`) that returns the full type vocabulary the WebSocket clients also consume?

2. **WebSocket subscription protocol — catch-up, persistent, framing.** Phase 2 specifies WebSocket-based event subscriptions with backpressure. The `WsMessage` sealed hierarchy has 13 subtypes covering authentication (`AuthenticateMsg`, `AuthResultMsg`), subscription lifecycle (`SubscribeMsg`, `SubscriptionConfirmedMsg`, `UnsubscribeMsg`, `SubscriptionEndedMsg`), event delivery (`EventsMsg` with `List<Object>` payload to avoid event-model leak, `StateSnapshotMsg`), backpressure signals (`DeliveryModeChangedMsg`), reliability (`ReplayQueuedMsg`), keepalive (`PingMsg`, `PongMsg`), and errors (`ErrorMsg`). **Is the existing protocol shape correct against production validators?** How does HA's WebSocket API frame events (persistent connection + `subscribe_events` command + JSON-RPC-like protocol)? How does EventStoreDB's subscription protocol handle catch-up vs persistent semantics? How does Matter's Interaction Model differ? Should HomeSynapse adopt explicit catch-up (replay from `lastSeenPosition`) vs persistent (start from live) modes, or is the current `fromGlobalPosition` field on `SubscribeMsg` sufficient? What's the right framing for `EventsMsg` — JSON text frames (current), JSON lines (one event per frame), or WebSocket binary frames with length-prefix?

3. **Event filtering at the API layer — server vs client.** `WsSubscriptionFilter` has 10 nullable fields (6 list fields, 1 String, 1 Boolean, 2 Integer) using AND-across-fields, OR-within-arrays semantics. The MODULE_CONTEXT notes the filter resolves materialized subject refs via `EntityRegistry`/`CapabilityRegistry`, caches them (max 500), and applies the resolved set at delivery time. **What filter capabilities do production clients actually need?** Survey HA's WebSocket event subscription (it allows event-type filtering but not entity-filtered subscriptions natively — clients filter client-side), EventStoreDB's filter expressions, OpenHAB's WebSocket. What's the performance model — filter on server (current HomeSynapse design) or send everything and filter client-side (HA's choice)? At what scale (events/sec, subscribers/process) does server-side filtering become a bottleneck on Pi 4? Should `WsSubscriptionFilter` support time-range filters (`fromTimestamp`, `toTimestamp`) for replay scenarios, or is `fromGlobalPosition` sufficient?

4. **Backpressure in WebSocket streams — when slow clients fall behind.** Phase 2 specifies the three-stage `DeliveryMode` (NORMAL → BATCHED → COALESCED) driven by per-connection buffer thresholds. The `DeliveryModeChangedMsg` signals transitions to the client. Close code `CLIENT_TOO_SLOW (4429)` is reserved for clients who exceed the COALESCED budget. **What's the right model under sustained client slowness?** HA drops events silently when WebSocket clients fall behind. EventStoreDB has subscription checkpointing — slow subscribers re-catch-up from their last checkpoint, no event loss. Marten (C#/.NET event sourcing framework) has per-subscription parking. What's the appropriate buffer threshold per stage on a Pi 4 with 4 GB RAM and (potentially) ~20 connected clients? Should COALESCED-stage coalescing be per-entity (last-write-wins for `attribute_changed` events) or global (drop oldest)? What close-code semantics work for typical web client behavior (browser tab backgrounded, intermittent network)?

5. **Authentication and rate-limiting — local-first auth model.** Phase 2 specifies `Authorization: Bearer {key}` with bcrypt hash validation, `ApiKeyIdentity` (3 fields: `keyId`, `displayName`, `createdAt`), per-key token-bucket rate limiting (`RateLimiter` returns `RateLimitResult(allowed, retryAfterSeconds)`), and mandatory authentication on every request per INV-SE-02. The Phase 2 `RateLimiter` interface is defined but the key-store backing it is unspecified. **What's the right auth model for a local-first hub that may also be reachable over LAN?** Survey HA's long-lived access tokens (with a creation UI in HA Settings → People → User → Long-Lived Access Tokens). OpenHAB's API token model. Hubitat's per-app token model. What's the right key-rotation cadence and revocation mechanism? Should HomeSynapse support short-lived (1 hour) bearer tokens issued by a longer-lived refresh credential, or are long-lived tokens sufficient for the home-server threat model? How should the operator bootstrap the first API key (CLI command? first-run wizard?)? Does mTLS make sense for HomeSynapse, or is Bearer-only correct? What about IP whitelist as defense-in-depth — should `127.0.0.1` always work without auth for local CLI tooling, or is INV-SE-02's "no local trust exception" absolute?

### Platforms / prior art to survey

- Home Assistant REST API (`developers.home-assistant.io/docs/api/rest/`) and WebSocket API (`developers.home-assistant.io/docs/api/websocket/`) — production-validated against 1M+ installs, the canonical comparison
- OpenHAB REST API (`openhab.org/docs/configuration/restdocs.html`) and WebSocket support
- EventStoreDB HTTP API and subscription protocol (catch-up subscriptions, persistent subscriptions, `$all` stream patterns)
- Marten (C#/.NET event sourcing) — async daemon subscription model
- Matter 1.4 Interaction Model — Read, Write, Subscribe, Invoke; explicit Subscribe Request / Response Interaction
- Hubitat Maker API (`docs2.hubitat.com/en/apps/maker-api`)
- SmartThings API
- json:api specification, HAL, and JSON-RPC 2.0 for response envelope precedents
- RFC 9457 Problem Details (already adopted by HomeSynapse — see existing `ProblemType` enum)
- RFC 6455 WebSocket Close Codes (already partially adopted — see existing `WsCloseCode` enum with 5 values in the 4400–4429 range)
- json-schema-validator's API surface (already in version catalog at 1.5.6) for any schema-validated request payloads

---

## CONTEXT YOU NEED

- HomeSynapse Core Knowledge Primer (uploaded to project knowledge — refreshed 2026-05-22, package annotations corrected)
- HomeSynapse Current State (uploaded to project knowledge)
- Doc 09 (REST API) — the governing design document for the REST surface
- Doc 10 (WebSocket API) — the governing design document for the WebSocket surface
- Research 3 PM Assessment — establishes the M3.7 E2E test harness patterns that this research's recommendations must be testable under
- Research 4 v3 PM Assessment — establishes the automation event flat-package precedent (AMD-52)
- Research 5 v2 FINAL PM Assessment — establishes the LTD + INV cross-reference discipline; new config events land in `com.homesynapse.event` flat per AMD-70
- Research 6 v1 PM Assessment — establishes the integration lifecycle event additions per AMD-56
- Research 8 v2 FINAL PM Assessment — establishes the `DispatchingProjectionAdvancer` pattern; `EntityCategory` registry-property contract on `Entity` (REC-23)

### Key context from completed upstream research (M10/M11-coupling for Research 7):

- **Research 4 REC-39 / AMD-52:** Eleven new automation event records (e.g., `automation.run.started`, `automation.run.completed`, `automation.run.failed`) land in `com.homesynapse.event` flat package, dot-namespaced. **`WsSubscriptionFilter.eventTypes` must accept these strings.** Decision needed: should `WsSubscriptionFilter` add a `namespacePrefix` field (e.g., subscribe to `automation.*`) or require explicit enumeration of every event type a client cares about?

- **Research 5 REC-59 / AMD-70:** Two new observability events (`config.validation_completed`, `config.section_reloaded`) land in `com.homesynapse.event` flat package, dot-namespaced. **REST API should consider a `GET /internal/config/issues` endpoint** projecting the validation-issue view (Research 5 §7.6 specified an in-memory `ValidationIssueProjection` keyed by `(sectionPath, issueId)`). This is observability surface, not state surface — gate via `/internal/*` like the existing M3.6e.2 admin endpoints, not via `/api/*` with the `ReadinessFilter`.

- **Research 6 REC-44 / AMD-56:** Four new `IntegrationLifecycleEvent` records (dot-namespaced) added to integration-api. **WebSocket subscribers monitoring integration health** would benefit from these. REST should consider exposing `GET /api/v1/integrations` and `GET /api/v1/integrations/{id}/health` endpoints projecting `IntegrationSupervisor.allHealth()` and `IntegrationSupervisor.health(IntegrationId)` (existing methods on `IntegrationSupervisor` interface, see embedded MODULE_CONTEXT below).

- **Research 8 REC-23 / AMD-44:** `EntityCategory` field added to `Entity` record (NOT to `EntityState`). The current `ListEntitiesEndpoint` (M3.6e.2) returns `EntityState` summaries from `StateQueryService` and does NOT join `Entity.category` at query time. Doc 09 §3.2 framed StateQueryService as not supporting filtered/joined queries (per Research 8 v2 design boundary). **Research 7 must reconcile:** does category filtering on `GET /api/v1/entities` require a new `EntityCategoryFilter` query parameter that the endpoint resolves by joining at the API layer (acceptable per Research 8 v2 §"design boundary"), or does it require a new `StateQueryService` method? The first option is the design-boundary-respecting choice.

### Cross-research-arc fabrication patterns to avoid

The prior six research documents have been increasingly cleaner — Research 5 v2 was the cleanest with zero type-name and zero JPMS-module-name fabrications. The fabrication classes to specifically avoid:

- **Type-name fabrications** (Research 3/4/8 historical pattern): every type referenced in §7 must match the verified MODULE_CONTEXT inventory below exactly. No abbreviations, no pluralizations, no renames.
- **JPMS-module-name fabrications** (Research 6 v1 historical pattern): every module name must match the verbatim `module-info.java` blocks embedded below. The websocket-api JPMS module is `com.homesynapse.api.ws` (NOT `com.homesynapse.api.websocket` — the latter is an old scaffold package that's deprecated and benign).
- **Sub-package fabrications** (Research 5 v2 F6 pattern): every module uses a single flat package. Do not propose `com.homesynapse.api.rest.internal` or similar — package-private is enforced via JPMS exports at the module-info level, not via sub-packaging.
- **Version-state misses** (Research 5 v2 F1/F2 pattern): the `libs.versions.toml` rows embedded below show what's already integrated. Do not propose "new dependency adoption" for libraries already in the catalog. If a version bump is genuinely needed, propose the bump explicitly with the current → target version.
- **Records-cannot-be-extended fabrications** (Research 5 v2 F7 pattern): records are implicitly `final`. Generic bounds `<T extends SomeRecord>` are mechanically unsound. Verify every proposed type shape compiles in your head before writing it.
- **Locked-decision miss** (Research 5 v2 F1 pattern): cross-reference both the version catalog AND the LTD entries embedded below before treating any library choice as open.
- **Invariant-citation miss** (Research 5 v2 F8 pattern): cross-reference the INV entries embedded below before treating any "design question" as open. INV-SE-02 settles "should authentication be mandatory" before it can be asked.

---

## CONSTRAINTS

- Take positions. "X is worth investigating" is banned. Use "X should be adopted because Y" or "X should be rejected because Y."
- Cite primary sources (docs, issue trackers, maintainer statements) with URLs.
- Every REC must include effort estimate in lines of code.
- Number RECs globally: Research 5 used REC-53 through REC-61. **This document starts at REC-62.**
- AMD numbering: AMD-01 through AMD-71 are allocated/proposed (AMD-47/AMD-61 withdrawn, AMD-64/AMD-65 retired post-Research-5-v2, AMD-67/AMD-71 deferred). New amendments start at **AMD-72**.
- Include §7 (Code-Level Implications) — MANDATORY. Specify exact Java records, interfaces, sealed hierarchy changes, event schema additions, module-info changes.
- For each proposed type change, specify: (a) the exact module, (b) the exact package, (c) public vs package-private visibility, (d) whether it requires an AMD.
- **Use the verbatim type and module identifiers embedded below. Do not paraphrase package names, module names, or type names.**
- **No `@Nullable` annotations in proposed signatures.** HomeSynapse codebase convention is Javadoc-only nullability (`{@code null} if …` patterns). Confirmed in every MODULE_CONTEXT Gotchas section.
- **No new ServiceLoader usage.** DECIDE-04 locks: factories are instantiated directly, no classpath scanning.
- **One flat package per module.** Do NOT propose sub-packages like `com.homesynapse.api.rest.internal`.

### Verified module identifiers (verbatim `module-info.java` contents)

**`api/rest-api/src/main/java/module-info.java`:**

```java
module com.homesynapse.api.rest {
    requires transitive com.homesynapse.state;
    requires com.homesynapse.event.bus;

    requires io.javalin;
    requires org.slf4j;

    exports com.homesynapse.api.rest;
}
```

**JPMS module name:** `com.homesynapse.api.rest`. **Java package:** `com.homesynapse.api.rest` (single flat). **Note:** zero-`requires` Phase 2 state ended with M3.6e.1 — the four `requires` directives above are post-M3.6e.1 + M3.6e.2 state.

**`api/websocket-api/src/main/java/module-info.java`:**

```java
module com.homesynapse.api.ws {
    requires transitive com.homesynapse.api.rest;

    exports com.homesynapse.api.ws;
}
```

**JPMS module name:** `com.homesynapse.api.ws` (NOT `com.homesynapse.api.websocket`). **Java package:** `com.homesynapse.api.ws` (single flat). The transitive on rest-api is load-bearing — `ApiKeyIdentity` and `ApiException` from rest-api appear in websocket-api's exported API. Phase 3 will add direct requires for event-model, event-bus, state-store, device-model, Jackson.

**`core/state-store/src/main/java/module-info.java`** (referenced by rest-api's `requires transitive`):

```java
module com.homesynapse.state {
    requires transitive com.homesynapse.platform;
    requires transitive com.homesynapse.device;
    requires transitive com.homesynapse.event;
    requires transitive com.homesynapse.event.bus;

    requires org.slf4j;

    exports com.homesynapse.state;
}
```

**`integration/integration-runtime/src/main/java/module-info.java`** (referenced for `IntegrationSupervisor` REST endpoint exposure):

```java
module com.homesynapse.integration.runtime {
    requires transitive com.homesynapse.integration;

    exports com.homesynapse.integration.runtime;
}
```

---

### Verified `gradle/libs.versions.toml` rows (relevant subset)

```toml
[versions]
java-language         = "21"
jackson               = "2.18.6"
javalin               = "6.7.0"
slf4j                 = "2.0.17"
json-schema-validator = "1.5.6"
snakeyaml-engine      = "2.9"

[libraries]
jackson-core              = { module = "com.fasterxml.jackson.core:jackson-core", version.ref = "jackson" }
jackson-databind          = { module = "com.fasterxml.jackson.core:jackson-databind", version.ref = "jackson" }
jackson-datatype-jsr310   = { module = "com.fasterxml.jackson.datatype:jackson-datatype-jsr310", version.ref = "jackson" }
javalin                   = { module = "io.javalin:javalin", version.ref = "javalin" }
slf4j-api                 = { module = "org.slf4j:slf4j-api", version.ref = "slf4j" }
json-schema-validator     = { module = "com.networknt:json-schema-validator", version.ref = "json-schema-validator" }
snakeyaml-engine          = { module = "org.snakeyaml:snakeyaml-engine", version.ref = "snakeyaml-engine" }
```

**Implications:** Jackson is on the 2.x line (`com.fasterxml.jackson.*` groupIds). Javalin 6.7.0 is already integrated. **Do NOT propose Jackson 3.x** or networknt 3.x — both require a coupled Jackson 2→3 migration which is explicitly out of Research 7 scope (per Research 5 v2 NQ-1 resolution). Do NOT propose new YAML or JSON libraries — they're already locked by LTD-09.

---

### Verified Locked Decisions (LTD) cross-references

Per `homesynapse-core-docs/governance/HomeSynapse_Core_Locked_Decisions.md`:

- **LTD-01 (Java 21 LTS):** Virtual threads for all request handling. Each incoming REST request and each WebSocket connection dispatched on its own virtual thread. **Phase 3 implementation must use virtual threads** for `RestApiServer.registerRoute` handler dispatch and for WebSocket connection handlers.
- **LTD-04 (ULID for Event and Entity Identity):** All wire-boundary IDs are 26-character Crockford Base32 strings. Phase 3 endpoint handlers perform `String` ↔ typed ID conversion at the API boundary.
- **LTD-08 (Jackson JSON for All Serialization):** Jackson 2.18+ (`com.fasterxml.jackson.*`). **SNAKE_CASE property naming.** `ApiRequest.body` is typed `Object` (not `JsonNode`) to avoid Jackson dependency leak; Phase 3 casts to `JsonNode` at usage site.
- **LTD-09 (YAML 1.2 for User-Facing Configuration):** Already locks `snakeyaml-engine` 2.9+ and `networknt:json-schema-validator` (currently 1.5.6 in catalog). Research 7's request-payload validation (if any) should use the same networknt validator, not introduce a new validation library.
- **LTD-11 (No External Message Broker):** Reinforces that the WebSocket API is an *external* delivery surface for events; the WebSocket Event Relay is a single `EventBus` subscriber (Doc 10 §3.6) that distributes to N clients, NOT a message-broker bridge.
- **LTD-15 (Structured JSON Logging via SLF4J + Logback + JFR):** REST endpoints and WebSocket handlers must log via SLF4J (already imported in rest-api's module-info). Resolved secret values must be redacted per the schema's `x-sensitive: true` annotations.
- **LTD-17 (In-Process Compiled Integrations):** Reinforces that REST/WebSocket are the boundary for external surfaces — integration adapters do NOT expose their own HTTP endpoints. All cross-process surface goes through these two modules.
- **LTD-19 (Event Payload Serialization via EventTypeRegistry + PersistenceJacksonModule + DegradedEvent fallback):** Extends LTD-08. WebSocket `EventsMsg.events` (List<Object>) is serialized using the same `EventTypeRegistry` that persistence uses — keeps the wire format aligned with the persistence format. **Do NOT propose a separate WebSocket event serialization path.**

---

### Verified Architecture Invariants (INV) cross-references

Per `homesynapse-core-docs/governance/Architecture_Invariants_v1.md`:

- **INV-SE-02 (Authentication Required for All External Interfaces):** Mandatory on every REST request and WebSocket connection. **There is no "local trust" exception.** A `127.0.0.1`-binding optimization or LAN-trust shortcut is forbidden — if Research 7 surveys patterns that rely on local trust, surface them but flag rejection per INV-SE-02.
- **INV-ES-01 (Events Are Immutable Facts):** Single-event REST responses are byte-identical on every subsequent request — justifies strong ETags and aggressive `Cache-Control` headers for `GET /api/v1/events/{event_id}` (when added). Paginated event lists are NOT immutable (page boundaries shift as new events append).
- **INV-ES-04 (Write-Ahead Persistence):** Command acceptance (`202 Accepted` from `POST /api/v1/entities/{entity_id}/commands`) guarantees the `command_issued` event is durably persisted, NOT that the device has executed. Research 7 should reinforce this contract in any new command-related endpoint.
- **INV-RF-01 (Integration Isolation):** REST/WebSocket cannot cause integration adapters to fail. Endpoints reading from `IntegrationSupervisor` are pure observers.
- **INV-PR-01 (Constrained Hardware Is the Primary Design Target):** All proposed endpoints + WebSocket protocol additions must work within Pi 4 budgets (4 GB RAM, ~10–20 concurrent clients realistic upper bound). Memory-heavy patterns (large in-memory schema documents, per-connection event buffers > 1 MB) need explicit Pi 4 budget justification.
- **INV-TO-03 (No Hidden State):** The `viewPosition` field in State Query responses lets clients detect staleness at the API boundary. Any new query endpoint must include the existing `ResponseMeta(viewPosition, timestamp)` envelope for State Query plane responses.
- **INV-CE-01 (Canonical, Human-Readable Configuration):** Reinforces that config edits go through the YAML file via `POST /api/config/reload` — NOT through a hypothetical REST endpoint that would create an event-sourced config write path.

---

### Verified type inventory — `api/rest-api/MODULE_CONTEXT.md` (28 public + 10 package-private = 38 types)

**Public enums (3):**
- `ProblemType` (13 values) — RFC 9457 error type identifiers. Values: `NOT_FOUND`, `ENTITY_DISABLED`, `INTEGRATION_UNHEALTHY`, `INVALID_COMMAND`, `INVALID_PARAMETERS`, `AUTHENTICATION_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `COMMAND_NOT_FOUND`, `STATE_STORE_REPLAYING`, `INTERNAL_ERROR`, `IDEMPOTENCY_KEY_CONFLICT`, `DEVICE_ORPHANED`. Three fields per value: `slug` (String), `defaultStatus` (int), `title` (String). Method: `typeUri() → "https://homesynapse.local/problems/" + slug`.
- `CommandLifecyclePhase` (5 values) — `ACCEPTED`, `DISPATCHED`, `ACKNOWLEDGED`, `CONFIRMED`, `CONFIRMATION_TIMED_OUT`.
- `SortDirection` (2 values) — `ASC`, `DESC`.

**Public data records (12):**
- `FieldError` (2 fields): `field`, `message`.
- `ProblemDetail` (7 fields): `type` (ProblemType), `title`, `status` (int), `detail`, `instance` (nullable), `correlationId`, `errors` (List<FieldError>, nullable).
- `ApiKeyIdentity` (3 fields): `keyId`, `displayName`, `createdAt`.
- `RateLimitResult` (2 fields): `allowed` (boolean), `retryAfterSeconds` (long).
- `CursorToken` (3 fields): `sortValue`, `sortDimension`, `direction` (SortDirection).
- `PaginationMeta` (3 fields): `nextCursor` (nullable), `hasMore` (boolean), `limit` (int).
- `ResponseMeta` (2 fields): `viewPosition` (long), `timestamp` (Instant).
- `ApiRequest` (7 fields): `method`, `pathPattern`, `pathParams` (Map, unmodifiable), `queryParams` (Map<String, List<String>>, unmodifiable), `body` (Object, nullable), `identity` (ApiKeyIdentity), `correlationId`.
- `ApiResponse` (5 fields): `statusCode` (int), `headers` (Map, unmodifiable), `body` (Object, nullable), `eTag` (nullable), `cacheControl` (nullable).
- `PagedResponse<T>` (3 fields, generic): `data` (List<T>, unmodifiable), `pagination` (PaginationMeta), `meta` (ResponseMeta, nullable).
- `CommandRequest` (3 fields): `capability`, `command`, `parameters` (Map<String, Object>, unmodifiable).
- `CommandAcceptedResponse` (6 fields): `commandId`, `correlationId`, `entityId`, `status`, `acceptedAt`, `viewPosition` (long).
- `LifecyclePhaseDetail` (3 fields): `at` (Instant), `eventId`, `details` (Map, nullable).
- `CommandStatusResponse` (**8 fields, not 7**): `commandId`, `correlationId`, `entityId`, `capability`, `command`, `lifecycle` (Map<CommandLifecyclePhase, LifecyclePhaseDetail>), `currentPhase`, `terminal` (boolean).
- `IdempotencyEntry` (5 fields): `idempotencyKey`, `commandId`, `correlationId`, `viewPosition` (long), `createdAt`.

**Exception (1):**
- `ApiException` extends `RuntimeException` — single field `problemDetail` (ProblemDetail, **transient**). Two constructors.

**Service interfaces (8):**
- `EndpointHandler` (@FunctionalInterface) — `handle(ApiRequest) → ApiResponse throws ApiException`.
- `AuthMiddleware` — `authenticate(String authorizationHeader) → ApiKeyIdentity throws ApiException`.
- `RateLimiter` — `check(String apiKeyId) → RateLimitResult`.
- `ETagProvider` — `fromViewPosition(long)`, `fromEventId(String)`, `fromDefinitionHash(String)`.
- `PaginationCodec` — `encode(CursorToken) → String`, `decode(String) → CursorToken throws ApiException`.
- `ProblemDetailMapper` — `map(Exception, String correlationId, String requestPath) → ProblemDetail`.
- `RestApiServer` — `registerRoute(String method, String pathPattern, EndpointHandler)`, `start(String host, int port)`, `stop(int drainSeconds)`, `isRunning()`, `port() → int`.
- `RestApiLifecycle` — `start()`, `stop()`.

**M3.6e.1 — Readiness gate (1 public + 1 package-private):**
- `RestFilters` (public final utility class, DEC-M3-16 gateway): `static void installReadinessGate(Object javalinApp, ReadinessSource readinessSource)`, `static void installEntityQueryEndpoints(Object, StateQueryService, LongSupplier, Clock)` (M3.6e.2), `static void installAdminEndpoints(Object, Object bus, ReadinessSource, StateQueryService, LongSupplier)` (M3.6e.2). The `javalinApp` and `bus` parameters are typed `Object` to keep `io.javalin.Javalin` and `com.homesynapse.event.bus.EventBus` out of the exported API surface.
- `ReadinessFilter` (package-private final, implements `io.javalin.http.Handler`): gates `/api/*` with `503` + RFC 9457 problem detail (`ProblemType.STATE_STORE_REPLAYING`) + headers (`X-HomeSynapse-Projection-State`, `Retry-After: 5`) until `SubscriberMode.LIVE`.

**M3.6e.2 — Endpoint handlers + SPI (8 package-private):**
- `EndpointContext` (package-private interface, 5 methods): `pathParam`, `queryParam`, `status`, `header`, `json` — narrow SPI mirroring the subset of Javalin's `Context` actually consumed.
- `JavalinEndpointContext` (package-private final, adapter): `Context ctx` field; forwards to Javalin's Context.
- `EndpointResponses` (package-private final utility): `problem(EndpointContext, ProblemType, String detail)` for shared RFC 9457 construction.
- `ListEntitiesEndpoint` (package-private final, implements `io.javalin.http.Handler`): `GET /api/v1/entities`. Query params: `limit` (default 50, clamped to `[1, 100]`), `sort` (ASC/DESC, default ASC). Sorts by entity ULID lexicographically. Returns `{data: [...summaries...], meta: {viewPosition, timestamp}}` + `X-HomeSynapse-View-Position` header. Summary fields: `entityId`, `availability`, `stale` (NOTE: `subjectType` was in PLAN-M3 §10.6 sketch but omitted because `EntityState` has no such field). Constants: `DEFAULT_LIMIT = 50`, `MAX_LIMIT = 100`, `VIEW_POSITION_HEADER = "X-HomeSynapse-View-Position"`.
- `GetEntityEndpoint` (package-private final): `GET /api/v1/entities/{entityId}`. Path param parsed via `EntityId.of(Ulid.parse(...))`. 400 on parse fail, 404 on `Optional.empty()` from query service, 200 + `{data: <EntityState>, meta}` on success.
- `GetEntityStateEndpoint` (package-private final): `GET /api/v1/entities/{entityId}/state`. Same shape as `GetEntityEndpoint` for MVP per PLAN-M3 §10.6 ("distinction is cosmetic"). Kept separate for planned M5+ divergence.
- `DlqStatusEndpoint` (package-private final): `GET /internal/dlq`. NOT gated by `ReadinessFilter`. Returns `{subscribers: [...{subscriberId, mode, dlqDepth, crashCount}...]}`. Field shape deviates from brief's sketch (`parkedCount`/`oldestParkedAt`) — those are not on `SubscriberSnapshot` (5 fields: `subscriberId`, `mode`, `checkpoint`, `dlqDepth`, `crashCount`).
- `ProjectionStatusEndpoint` (package-private final): `GET /internal/projection`. NOT gated. Returns `{mode, viewPosition, entityCount, ready}`.

**ArchUnit rules enforcing the read-only nature of the REST surface (in `homesynapse-app`):**
- `QUERY_SERVICE_READ_ONLY` (M3.6e.2) — rest-api must not access persistence directly.
- `REST_ENDPOINTS_NO_EVENT_PUBLISHING` (M3.6e.2) — rest-api must not depend on `EventPublisher`.

---

### Verified type inventory — `api/websocket-api/MODULE_CONTEXT.md` (26 Java files, all Phase 2 complete)

**Public enums (2):**
- `DeliveryMode` (3 values): `NORMAL`, `BATCHED`, `COALESCED` — three-stage backpressure delivery strategy.
- `WsCloseCode` (5 values, RFC 6455 4000–4999 application range): `AUTH_FAILED (4403)`, `AUTH_TIMEOUT (4408)`, `CLIENT_TOO_SLOW (4429)`, `SUBSCRIPTION_LIMIT (4409)`, `MALFORMED_MESSAGES (4400)`.

**Filter record (1):**
- `WsSubscriptionFilter` (10 nullable fields): 6 list fields + 1 String + 1 Boolean + 2 Integer. AND across fields, OR within arrays.

**WsMessage sealed hierarchy (1 sealed interface + 13 subtypes):**
- `WsMessage` (sealed interface, `Integer id()` accessor — note `Integer` not `int` for nullable server-initiated messages).

Client→Server:
- `AuthenticateMsg` (2 fields): `id`, `apiKey`.
- `SubscribeMsg` (4 fields): `id`, `filter`, `fromGlobalPosition` (Long?), `includeInitialState` (Boolean?).
- `UnsubscribeMsg` (2 fields): `id`, `subscriptionId`.
- `PingMsg` (1 field): `id`.

Server→Client:
- `AuthResultMsg` (6 fields): `id`, `success`, `connectionId`?, `serverTime`?, `errorType`?, `errorDetail`?.
- `SubscriptionConfirmedMsg` (4 fields): `id`, `subscriptionId`, `filter`, `replayFrom`?.
- `EventsMsg` (4 fields): `id` (null for server-initiated), `subscriptionId`, `deliveryMode`, `events` (List<Object> — NOT List<EventEnvelope>, avoids event-model leak).
- `StateSnapshotMsg` (4 fields): `id` (null), `subscriptionId`, `viewPosition`, `entities` (List<Object>).
- `DeliveryModeChangedMsg` (5 fields): `id` (null), `subscriptionId`, `oldMode`, `newMode`, `reason`.
- `ErrorMsg` (4 fields): `id`?, `errorType` (String slug, NOT ProblemType enum — wire format), `detail`, `fatal`.
- `PongMsg` (2 fields): `id`, `serverTime`.
- `SubscriptionEndedMsg` (4 fields): `id` (null), `subscriptionId`, `reason`, `lastGlobalPosition`?.
- `ReplayQueuedMsg` (5 fields): `id` (null), `subscriptionId`, `positionInQueue`, `estimatedWaitMs`, `lastSeenPosition`.

**State records (2):**
- `WsSubscription` (8 fields): `subscriptionId`, `connectionId`, `filter`, `deliveryMode`, `replayCursor`?, `stateChangeOnly`, `minIntervalMs`?, `maxIntervalMs`?.
- `WsClientState` (7 fields): `connectionId`, `apiKeyIdentity` (ApiKeyIdentity from rest-api), `authenticatedAt`, `activeSubscriptions` (Map), `bufferBytes`, `deliveryMode`, `malformedMessageCount`.

**Service interfaces (6):**
- `WebSocketHandler` — connection event callbacks (`onConnect`, `onMessage`, `onClose`, `onError`).
- `MessageCodec` — JSON↔WsMessage. `decode(String) throws ApiException`, `encode(WsMessage) → String`.
- `ClientConnection` — per-connection state and send/close.
- `SubscriptionManager` — `subscribe throws ApiException`, `unsubscribe throws ApiException`, `subscriptions`, `removeAll`.
- `EventRelay` — single bus subscriber → N clients. `start`, `stop`, `addClient`, `removeClient`, `currentPosition`, `connectedClientCount`.
- `WebSocketLifecycle` — `start()` (Phase 5), `stop()` (shutdown step 3, before REST).

---

### Verified NON-existent types and surfaces (do not invent)

The Research 7 brief explicitly checked the source — these are referenced or implied in the design docs but NOT yet implemented:

- **API key storage / persistence.** `ApiKeyIdentity` is the in-memory authenticated identity, but the bcrypt hash store (the "what's in the keystore") is not yet specified. **Research 7 §Q5 should propose this** — file format, on-disk location, rotation/revocation primitives.
- **CORS middleware.** Not in Phase 2. Web UI access from the dashboard module will need CORS. Research 7 should propose the configuration surface (allowlist of origins, header allowlist, preflight handling).
- **OpenAPI 3.1 spec generation.** Not in Phase 2 or current MVP scope. Research 7 may comment on whether OpenAPI generation should be MVP or Tier 2.
- **Replay admission queue.** Doc 10 §3.9 mentions "max 1 concurrent replay (FIFO queue)" but no concrete implementation. `ReplayQueuedMsg` is defined; the admission control is Phase 3 work.
- **Per-connection rate limiting.** Doc 10 §3.10 says "Per-connection rate limiting, not per-IP, not per-API-key." `RateLimiter` exists in rest-api but its application to WebSocket connection-level rate limiting is unspecified.
- **WebSocket close-code 4429 (`CLIENT_TOO_SLOW`) trigger criteria.** Defined but the exact buffer-threshold + sustained-duration semantics that escalate from COALESCED → close are unspecified.
- **WebSocket auth-timeout 4408 semantics.** Defined as 5-second timeout in §3.5 but the exact behavior on timeout (close immediately vs send `AuthResultMsg` first) is unspecified.
- **`GET /api/v1/integrations/*` endpoints.** Implicit in the existence of `IntegrationSupervisor.allHealth()` etc., but not yet specified or implemented.
- **`GET /internal/config/issues` endpoint.** Implied by Research 5 REC-59's `ValidationIssueProjection`, but not yet specified.

### Verified upstream constraints (do not propose changes — outside Research 7 scope)

- `ApiException.problemDetail` is `transient` — do not propose making it persistable. The exception is never serialized over the wire; it's caught in-process and converted to an HTTP response.
- `EventsMsg.events` is `List<Object>` — do not propose typing it as `List<EventEnvelope>`. The Object typing avoids leaking event-model into the websocket-api exported API.
- `ApiRequest.body` is `Object` — do not propose typing it as `JsonNode`. Same reason — keeps Jackson out of the exported API.
- `ProblemDetail.errors` is nullable — do not "fix" it to be an empty list when no errors. The null/non-null distinction carries semantic meaning per RFC 9457.
- `ApiResponse.headers` is `Map<String, String>` (single-valued) — multi-valued headers are out of Phase 2 scope.
- `RateLimiter.check(...)` returns `RateLimitResult` (allowed + retryAfterSeconds) — do not propose changing to `boolean`. The `Retry-After` header value needs the seconds.
- `WsMessage.id()` returns `Integer` (boxed) — null for server-initiated messages. Do not propose changing to `int`.
- `ErrorMsg.errorType` is String (slug) not ProblemType enum — wire format uses slug strings for stability across protocol versions.
- `CommandStatusResponse` has **8 fields**, not 7. The `terminal` boolean is the 8th component.
- `RestFilters` gateway methods use `Object`-typed framework parameters — do not propose typing them as `io.javalin.Javalin` or `EventBus`. The Object typing is the DEC-M3-16 gateway pattern that keeps non-transitive `requires` from leaking through the exported API.

### Event naming convention

Legacy events use snake_case with underscores: `command_issued`, `entity_registered`, `device_reachable_changed`. New events use dot-separated namespacing: `automation.run.started`, `config.validation_completed`, `integration.lifecycle.started`. Both patterns are permanent. **Any new event proposed by Research 7 should use dot-separated namespacing** (e.g., `api.request.failed` if a request-failure event is proposed — though such events are typically observability, not domain, and may not need persistence).

---

## OUTPUT

A single markdown document following the mandatory format above. Do not truncate. Produce the complete document. Target length: ~600–800 lines.

When you reach §7 (Code-Level Implications), structure proposals around these specific surfaces:

1. **Additional REST endpoints beyond the M3.6e.2 MVP set.** Specify the exact path, HTTP method, query parameters, response body shape (referencing existing `PagedResponse<T>`, `ResponseMeta`, `ProblemDetail` records), and which existing service interface backs it (`StateQueryService`, `EventStore`, `IntegrationSupervisor`, `AutomationRegistry`, `ConfigurationService`, etc.). Specify whether each endpoint lives under `/api/*` (gated by `ReadinessFilter`) or `/internal/*` (admin/operational, ungated).

2. **`WsSubscriptionFilter` extensions (if any).** The existing 10-field shape supports event-type, entity, capability, area, label, subject filtering with AND/OR semantics. Propose specific new fields with exact types and Javadoc-only nullability semantics. Justify each against the platform survey.

3. **WebSocket protocol extensions (if any).** New `WsMessage` subtypes (sealed hierarchy permits expansion via the `sealed`/`permits` clause), new `WsCloseCode` values, new `DeliveryMode` semantics. Justify each.

4. **Authentication implementation surfaces.** API key store (file format, location, rotation), CLI bootstrap command (`homesynapse key generate`, `homesynapse key revoke`, `homesynapse key list`), token-lifetime policy (long-lived vs refresh-rotated), interaction with `SecretStore` from Research 5 (does the API key bcrypt hash live in the encrypted secrets store, or in a separate keystore?). Specify whether new public types are added to rest-api or live in a new `auth` module.

5. **Rate-limiting and CORS implementation surfaces.** Token-bucket parameter defaults (per-key requests/min, burst size — current defaults are 300/min, burst 50 per Doc 09 §9). Per-connection rate limiting for WebSocket (different from per-key for REST). CORS configuration surface (allowlist, header whitelist, preflight handling).

6. **New event types (if any).** `@EventType` strings (dot-namespaced recommended), payload schemas, **state-changing vs observability-only classification** (required for `DispatchingProjectionAdvancer` handler registration per Research 8 REC-28). Package landing: `com.homesynapse.event` flat per AMD-52 precedent. **Strongly favor observability-only events** for API-layer concerns (e.g., a hypothetical `api.request.failed` event for rate-limit observability) — state-changing events from the API layer are an anti-pattern (the API layer should only produce events that already exist via command/lifecycle paths).

7. **`module-info.java` impact.** rest-api currently requires `com.homesynapse.state` (transitive), `com.homesynapse.event.bus`, `io.javalin`, `org.slf4j`. websocket-api currently requires `com.homesynapse.api.rest` (transitive). What additional `requires` directives are needed for the Phase 3 implementation work this research informs? Are they transitive (types appear in exported public API) or non-transitive (implementation-only)?

8. **OpenAPI / schema-endpoint deliverable.** If recommending an OpenAPI 3.1 spec for the REST surface or a `GET /api/v1/schema` endpoint for WebSocket clients, specify the generation strategy (hand-authored YAML vs derived from types vs runtime-generated) and the impact on the existing `SchemaRegistry` interface (which currently handles config schemas, not API schemas — overlap?).

### Coder Pushback Welcome

If Research 7 uncovers a contradiction between Doc 09/Doc 10 §3.x and the verified MODULE_CONTEXT type inventory above, flag it explicitly in §5.4. The MODULE_CONTEXT is authoritative for type-level facts (verified 2026-05-22 at HEAD `76288af`). Doc 09/Doc 10 are authoritative for behavioral contracts. If they diverge, that's a PM action item, not a researcher fabrication.

If Research 7 finds that one of the open Nick decisions from prior research assessments is actually answerable from API-side evidence, surface it in §5 — the PM will reconcile across assessments. Specifically:
- Research 5 REC-56 (`(major, minor)` schema versioning) is deferred on Research 6 REC-41 — Research 7 might find independent evidence either way (e.g., HA's WebSocket API exposing the config schema version in its messages).
- Research 6 NQ-1 (`SecurityServices` aggregator) might have implications for how REST/WebSocket auth surfaces interact with per-integration credential rotation.

### Spike candidates to flag in §5.3

Three classes of empirical question are likely to surface:

- **Server-side filter scaling on Pi 4.** At what events/sec + subscribers count does server-side `WsSubscriptionFilter` evaluation become the bottleneck? Spike target: synthetic 100 ev/s × 20 subscribers with diverse filters.
- **WebSocket connection memory residency.** Per-connection state (`WsClientState` + active subscriptions + buffer) — what's the actual heap cost per connection? Target: <100 KB per connection so 20 connections fit comfortably in <2 MB.
- **bcrypt hash validation latency.** Per-request bcrypt cost — at default bcrypt cost factor (10 or 12), what's the per-request latency on Cortex-A72? Target: <50ms p99. If exceeds, propose a cached-hash-validity window (e.g., remember "this Authorization header was valid 30s ago" to skip re-hashing — security tradeoff to evaluate).
