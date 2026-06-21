<!--
file: context/decisions/2026-06-21_dashboard-read-API-contract-freeze.md
purpose: The FROZEN dashboard read-API contract (v1) — the binding interface the Web-UI lane builds against and the Core lane must not break silently. Pins the EXISTING REST shapes (source-verified at core 1541446) and DEFINES the frozen-but-unbuilt shapes (events, health, the causal-chain hero, the automations list) the frontend mocks against and Core implements TO. The hard prerequisite for launching the frontend-dev lane (V1 record wave step 2).
audience: the frontend-dev lane (builds against this), the Core lane (implements/preserves it), the hub (adjudicates any change as a cross-lane event), Nick (public-API shape is his call)
state-type: decision / frozen contract (v1)
status: FROZEN 2026-06-21 (v3 hub). Source-verified against core 1541446 (post-M7.2a-1): api/rest-api endpoints + RestFilters + StandardAuthMiddleware + the response DTOs. Changes route through the hub (§6).
anchors: homesynapse-core-docs/design/09-rest-api.md (Locked) · design/13-web-ui-observability-mvp.md (Locked) · design/16-superior-automation.md (RunCausalChain — the hero) · context/decisions/2026-06-20_V1-launch-scope_decision-record.md (device/event/health views + the thin causal-query API; no-WS poll 1–2s)
-->

# Dashboard Read-API Contract — FROZEN v1 (2026-06-21)

**Why this exists.** The Web-UI lane is the long pole among non-Core lanes (~6–8 wks, no slack) and must start now, against a **frozen** contract — launching it against a moving API invites exactly the cross-lane rework the parallel model exists to prevent (V1 record, wave step 2; "freeze the dashboard read-API contracts EARLY"). This document is that freeze. Two classes of contract below: **(A) EXISTING** — built and source-verified, the frontend consumes the real endpoints; **(B) FROZEN-UNBUILT** — not yet in Core, the frontend builds against these shapes as mocks and Core implements **to** them. Any change to either class is a **cross-lane event** routed through the hub (§6) — the Core lane does not alter a frozen read shape without the hub telling the Web-UI lane.

---

## 0. Transport + cross-cutting contract (binds every endpoint)

- **Base + bind:** loopback default `http://127.0.0.1:{httpPort}` (AB-1; LAN = explicit authenticated opt-in). No TLS in the loopback MVP.
- **Auth (AB-1, source-verified `StandardAuthMiddleware`):** every `/api/*` and `/internal/*` request carries `Authorization: Bearer {token}`.
  - Missing / blank / non-`Bearer` → **401** `authentication-required` (response sets `WWW-Authenticate: Bearer`).
  - Well-formed but absent / revoked / expired token → **403** `forbidden`.
  - Valid token → access (Tier-1 binary; a valid token grants access). The identity surfaced server-side is `ApiKeyIdentity{keyId, displayName, createdAt}` — the raw token is never echoed or logged.
  - **Bootstrap credential:** the first-run **pairing token** is written to `config/initial_api_token` (operator reads it once). The frontend's auth flow takes a token the operator pastes; there is **no pre-auth enumeration / no shared bootstrap secret**.
- **Error model (RFC 9457, source-verified `ProblemDetail` + `ProblemType`):** non-2xx bodies are `application/problem+json`:
  ```json
  { "type": "<slug>", "title": "...", "status": <int>, "detail": "...",
    "instance": "...", "correlationId": "...", "errors": [ { "field": "...", "message": "..." } ] }
  ```
  Frozen `ProblemType` taxonomy (slug, status): `not-found`(404), `entity-disabled`(409), `integration-unhealthy`(503), `invalid-command`(422), `invalid-parameters`(400), `authentication-required`(401), `forbidden`(403), `rate-limited`(429), `command-not-found`(404), **`state-store-replaying`(503)**, `internal-error`(500), `idempotency-key-conflict`(409), `device-orphaned`(503).
  - **The frontend MUST handle `state-store-replaying` (503):** on boot the projection catches up; reads return 503 until LIVE. Render a "starting up / catching up" state, retry with backoff — do not treat it as a hard error.
- **Freshness + polling (the no-WebSocket anchor — D-OPEN-3 firm):** **every read response carries `meta: { "viewPosition": <long>, "timestamp": "<ISO-8601>" }`** (source-verified `ResponseMeta`). `viewPosition` is the monotonic projection cursor. **The frontend polls at 1–2s and compares `viewPosition`** to detect advancement (cheap change-detection without a push channel). This reads as real-time for a home dashboard. **No WebSocket client in V1.**
- **Caching:** responses support `ETag` + `Cache-Control` (source-verified `ApiResponse{eTag, cacheControl}`); the frontend SHOULD send `If-None-Match` and handle `304`.
- **Pagination (cursor-based, source-verified `PaginationMeta`):** list endpoints take `?limit=<n>&cursor=<opaque>&sort=ASC|DESC` and return `pagination: { "nextCursor": <string|null>, "hasMore": <bool>, "limit": <int> }`. Cursors are opaque — the frontend echoes `nextCursor`, never constructs one.

---

## A. EXISTING contracts (built + source-verified — consume the real endpoints)

### A1. `GET /api/v1/entities` — device list (ListEntitiesEndpoint)
Query: `?limit=<n>&sort=ASC|DESC&cursor=<opaque>`. Response:
```json
{ "data": [ { "entityId": "<ulid>", "availability": "AVAILABLE|UNAVAILABLE|UNKNOWN", "stale": false } ],
  "meta": { "viewPosition": 12345, "timestamp": "2026-06-21T..." } }
```
The list summary is the **3-field hot-path projection** (`entityId`, `availability`, `stale`) — by design, for fast dashboards. For full attributes, follow up with A2/A3.

### A2. `GET /api/v1/entities/{entityId}` — entity detail (GetEntityEndpoint)
Returns `entityId` + `availability` + a **small set of always-rendered attributes** (hot-path detail). `{data, meta}` envelope. `404 not-found` if absent.

### A3. `GET /api/v1/entities/{entityId}/state` — full entity state (GetEntityStateEndpoint)
Returns the materialized `EntityState` (Doc 03 §4.1): `entityId`, `availability`, typed `attributes` map (the `{"t":<AttributeType>,"v":…}` typed-value envelope — AMD-52), `stateVersion`, the activity timestamps (`lastChanged`/`lastUpdated`/`lastReported`, event-time-deterministic per AMD-53), `stale`/`staleAfter`. `{data, meta}` envelope. **`stale` is computed at read time** — re-poll refreshes it.

### A4. `GET /internal/projection` — projection/replay health (ProjectionStatusEndpoint)
Behind auth. Reports projection mode (REPLAY/TRANSITION/LIVE), `viewPosition`/lag, `projectionVersion`. The frontend's **health view** reads this for the "system catching up vs live" signal.

### A5. `GET /internal/dlq` — dead-letter health (DlqStatusEndpoint)
Behind auth. Reports DLQ depth / parked-subscriber status. Health-view input (an at-a-glance "is anything wedged" signal).

---

## B. FROZEN-UNBUILT contracts (mock these now; Core implements TO them — NEW Core obligations)

These shapes do **not** exist in Core at `1541446`. The frontend builds against them as mocks; Core delivers them to this exact shape on the sequence below. **Each is a flagged new Core read obligation** (hub-tracked).

### B1. `GET /api/v1/events` — event history/feed  *(NEW — small Core read-slice; sequence with the frontend's event view)*
The event view (V1 record IN-list) has **no endpoint today**. Frozen contract:
Query: `?since=<cursor>&limit=<n>&type=<eventType>&subjectId=<ulid>&sort=DESC`. Response: `{data, pagination, meta}` where each `data[]` element is a flattened event summary:
```json
{ "eventId": "<ulid>", "type": "state_changed", "category": "STATE",
  "occurredAt": "<ISO>", "viewPosition": 12345,
  "subjectRef": { "type": "ENTITY", "id": "<ulid>" },
  "correlationId": "<ulid>", "summary": "<short human string>" }
```
Poll-tail with `since=<last nextCursor>` for new events (the 1–2s poll model; no push). Payload-bearing detail is a follow-up `GET /api/v1/events/{eventId}` if needed — **kept thin** (event LIST + on-demand detail; not a full query language).

### B2. `GET /api/v1/health` — consolidated health  *(NEW — thin aggregation; or the frontend composes A4+A5)*
Frozen contract (Core may implement as an aggregation of A4/A5 + lifecycle health):
```json
{ "data": { "phase": "RUNNING", "projection": { "mode": "LIVE", "viewPosition": 12345, "lagEvents": 0 },
            "dlq": { "depth": 0, "parkedSubscribers": [] },
            "integrations": [ { "id": "zigbee", "health": "HEALTHY|DEGRADED|UNHEALTHY|UNKNOWN" } ] },
  "meta": { "viewPosition": 12345, "timestamp": "<ISO>" } }
```
Until B2 ships, the frontend composes the health view from A4 + A5 (both exist). B2 is a convenience consolidation, not a blocker.

### B3. THE HERO — causal-chain read (the thin causal-query API)  *(NEW — lands after M7.2b; must NOT balloon into all of M12)*
This is the differentiator's read surface. It reads the AMD-91 **`RunCausalChain`** + the run-lifecycle/dispatch events (AMD-92 rows the M7.2a slice mints). **Frozen thin contract — three reads, no more for V1:**

- **`GET /api/v1/runs?automationId=<id>&since=<cursor>&limit=<n>`** → recent runs (the "why did this fire?" entry list):
  ```json
  { "data": [ { "runId": "<ulid>", "automationId": "<ulid>", "automationName": "...",
                "triggeredAt": "<ISO>", "status": "COMPLETED|FAILED|SKIPPED|CANCELLED|INTERRUPTED",
                "terminalReason": "<string|null>" } ],
    "pagination": {...}, "meta": {...} }
  ```
- **`GET /api/v1/runs/{runId}/causal-chain`** → the hero "why did this fire?" tree:
  ```json
  { "data": { "runId": "<ulid>", "automationId": "<ulid>", "automationName": "...",
      "trigger": { "type": "...", "subjectRef": {...}, "matchedAt": "<ISO>", "firingValue": "..." },
      "conditions": [ { "expression": "...", "evaluated": true, "result": true,
                        "observedState": [ { "entityId": "...", "attribute": "...", "value": "..." } ] } ],
      "actions": [ { "type": "...", "targetRef": {...}, "command": "...", "params": {...},
                     "outcome": "DISPATCHED|CONFIRMED|FAILED|SKIPPED", "reason": "<string|null>" } ],
      "outcome": { "status": "...", "reason": "<string|null>", "durationMs": 0,
                   "actionCount": 0, "commandCount": 0 },
      "cascade": { "parentRunId": "<ulid|null>", "depth": 0 } },
    "meta": { "viewPosition": <long>, "timestamp": "<ISO>" } }
  ```
  This maps 1:1 onto `RunCausalChain`/`ChainLink` + the AMD-92 event rows (trigger=row1, condition-evaluated=row4, action=rows5/6, conflict=row9, completed=row2). **`observedState` is the trigger-time snapshot the M7.2a-2 `RunConditionGate` captures** (the real `stateSnapshotPosition` 2a-2 wires). The "why did it NOT fire?" case is the same shape with `conditions[].result=false` / `status=SKIPPED` + reason.
- **`GET /api/v1/automations`** → the component-based automation list (supporting surface #1 — present, not built out): `{ "data": [ { "automationId", "name", "enabled", "components": [ {"type","summary"} ], "lastRunId": "<ulid|null>" } ], ... }`.

**Scope guard (binds B3):** these three reads are the V1 causal surface. The contract must NOT grow into the full M12 observability/query language — no arbitrary event-graph traversal, no cross-run analytics, no audit projection. Hero + the run list + the automation list. That is the whole V1 causal read API.

---

## C. Sequencing the frontend against these contracts
1. **Now:** build shell + design system + auth (A0) + the **device views (A1–A3, real endpoints)** + the **health view (A4+A5, real endpoints)**. Zero Core dependency — all built.
2. **Soon (small Core read-slices):** the **events view (B1)** — flag to Core as a near-term read obligation; the frontend mocks B1 until it lands.
3. **The scheduled seam:** the **hero view (B3)** integrates as the **thin causal-query API lands after M7.2b**. The frontend builds the hero UI against the B3 mock now; swaps to the real endpoint when Core delivers it. A known, scheduled dependency — not a blocker.

## D. Change discipline (the cross-lane rule)
This contract is **v1, frozen**. Any Core change to an A-class shape, or any deviation from a B-class frozen shape at implementation time, is a **cross-lane event**: the Core/PM hub records it and notifies the Web-UI lane before it lands. Additive, backward-compatible fields are low-friction; renames / removals / type changes are breaking and require the hub to re-sync both lanes. **public-API shape is Nick's call** — a breaking change escalates.
