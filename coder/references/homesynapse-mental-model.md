<!--
file: coder/references/homesynapse-mental-model.md
purpose: Internalized architectural understanding of HomeSynapse Core; reason-from-it rather than rules-to-follow.
audience: Coder
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-06-07 against commit 8028337
-->

# HomeSynapse Mental Model

This is the internalized understanding of HomeSynapse Core. Not rules to follow — understanding to reason from. When instructions are incomplete or a detail is unspecified, this mental model tells you what the correct choice is.

---

## 1. The Event Log Is Everything

Every meaningful thing that happens in HomeSynapse produces an immutable event. The event log is the single source of truth. All observable state — device states, automation history, system health — is derived by replaying events.

**Why this matters to you as the Coder:**
- You never mutate state directly. You publish an event, and a subscriber (projection) updates the materialized state.
- If you're writing code that "sets" a device state, you're doing it wrong. You publish a `state_changed` event. The State Store subscriber materializes it.
- If you need to know the current state, you query the State Store — never the event log directly for current values.
- If you need to know the history, you query the event log with a time range or correlation chain.
- If the state store is corrupted, events are replayed from a checkpoint and state is rebuilt. Your code must produce the same state from the same events every time (determinism).

**The event flow:**
```
Physical world → Integration adapter → EventPublisher.publish()
    → SQLite WAL commit (durable)
    → Method returns to caller
    → Event bus dispatches to subscribers (async, virtual threads)
        → State Store projection updates materialized state
        → Automation Engine evaluates triggers
        → WebSocket broadcasts to connected clients
        → Observability system records metrics
```

The CRITICAL boundary: the WAL commit happens BEFORE subscriber notification. If the system crashes between publish and notification, recovery replays persisted-but-undelivered events. This is INV-ES-04.

## 2. The Event Envelope

Every event is wrapped in a standard envelope. Know these fields cold — you'll work with them constantly.

| Field | Type | Purpose | Your Implementation Note |
|---|---|---|---|
| `event_id` | EventId (ULID) | Unique identity | `UlidFactory.monotonic()` — hand-rolled in platform-api (the `ulid-creator` library was removed, DECIDE-02); monotonic within millisecond |
| `event_type` | String | Dotted taxonomy key | e.g., `device.state_changed`, `automation.triggered` |
| `schema_version` | int | Payload schema version | Starts at 1. Upcasters handle migration. |
| `ingest_time` | Instant | When appended to log | System clock. Stored as microseconds since epoch. |
| `event_time` | Instant (nullable) | When it happened in the real world | From device/integration. Null if unreliable clock. |
| `subject_ref` | SubjectRef | What this event is about | SubjectRef pairs Ulid + SubjectType discriminator. |
| `subject_sequence` | long | Per-entity ordering | Monotonic within one subject. `(subject_ref, subject_sequence)` is unique. |
| `global_position` | long | Cross-entity ordering | SQLite rowid. Subscribers checkpoint against this. |
| `priority` | EventPriority | CRITICAL / NORMAL / DIAGNOSTIC | Use `severity()` (0/1/2) for comparison, not `ordinal()`. |
| `origin` | EventOrigin | Where it came from | PHYSICAL, USER_COMMAND, AUTOMATION, etc. |
| `categories` | List\<EventCategory\> | Consent-scope categories | Static eventType→category lookup at creation. |
| `causal_context` | CausalContext | Correlation + causation | 2-field record: `correlationId` (non-null), `causationId` (nullable for root). |
| `actor_ref` | Ulid (nullable) | Who caused this event | PersonId, AutomationId, or SystemId. Null for system/autonomous. Top-level for indexing (INV-MU-01). |
| `payload` | DomainEvent | Event-type-specific data | Sealed interface hierarchy |

**Note:** EventEnvelope has 14 fields total. CausalContext has 2 fields (correlationId, causationId only — actorRef is on the envelope). EventDraft has **9 fields** (eventType, schemaVersion, eventTime, subjectRef, priority, origin, payload, actorRef, idempotencyKey — the 9th field `idempotencyKey` added per AMD-35). EventPublisher.publishRoot(EventDraft) takes a single parameter — actorRef comes from the draft.

**Two ordering systems coexist:**
- `subject_sequence` — strict monotonic per entity. Used for optimistic concurrency. Two different entities can have the same sequence number.
- `global_position` — SQLite rowid, monotonic across all entities. Used for subscriber checkpoints and catch-up reads.

## 3. The Device Model

Devices are containers. Entities are the atomic units of behavior. This distinction matters everywhere.

```
Device (physical product)
  └── Entity 1 (light)          ← automation targets THIS
  │     ├── Capability: on_off
  │     └── Capability: brightness
  └── Entity 2 (power meter)    ← automation targets THIS
        └── Capability: energy_meter
```

- **DeviceId** identifies the physical hardware. Used for device lifecycle events (adopted, removed, firmware update).
- **EntityId** identifies the functional unit. Used for state events, commands, automation targeting.
- **Capabilities** are typed behavioral contracts. A `brightness` capability guarantees a `brightness` attribute (with range constraints defined in `AttributeSchema` — minimum, maximum, step — not as separate named attributes) and commands (set_brightness with a level parameter).

**Key insight:** When an integration discovers a device, it doesn't create entities directly. It produces a `ProposedDevice` with proposed entities and capabilities. The Device Model validates and adopts them through the discovery pipeline. The integration never touches the `DeviceRegistry` or `EntityRegistry` directly.

## 4. The Integration Boundary

This is the most important boundary for reliability (INV-RF-01).

**Integrations receive a composed API surface (`IntegrationContext`):**
- `EventPublisher` — to publish device events
- `EntityRegistry` — read-only access to entities this integration manages
- `StateQueryService` — read-only access to current entity state
- `ConfigAccess` — this integration's configuration section
- `SchedulerService` — to schedule periodic tasks
- `HealthReporter` — to report health status
- `TelemetryWriter` — for high-frequency telemetry samples
- `ManagedHttpClient` (optional) — for cloud-connected adapters

**Integrations CANNOT access:**
- Another integration's entities
- Core internals (event bus implementation, state store implementation)
- Global configuration
- Direct SQLite access

This boundary is enforced at build time by `modules-graph-assert` (Gradle module dependency rules) and at test time by ArchUnit (package import rules). If your code compiles but ArchUnit fails, you've crossed a boundary.

## 5. Concurrency Model

**Virtual threads for network I/O, sleep, and timers. Platform threads for serial I/O (jSerialComm JNI) and SQLite I/O (sqlite-jdbc JNI).**

Virtual threads (JEP 444) are lightweight threads managed by the JVM. They unmount from their carrier thread when they block on I/O (socket reads, `BlockingQueue.take()`, `ReentrantLock.lock()`). This means you can have hundreds of concurrent subscribers, integration adapters, and API handlers without a thread pool.

**Serial I/O exception:** JNI calls (serial I/O via jSerialComm) pin the carrier thread permanently. The Zigbee adapter uses a dedicated platform thread for serial reads, feeding a `BlockingQueue` that a virtual thread drains.

### sqlite-jdbc JNI Carrier Thread Pinning (AMD-26/AMD-27)

The "virtual threads for everything except serial I/O" rule has a second critical exception: **all SQLite database operations**. The xerial sqlite-jdbc driver's `NativeDB.java` declares every method as `synchronized native` — a worst-case double-pinning pattern for Java 21 virtual threads. The virtual thread is pinned by both the monitor entry AND the JNI native call. JEP 491 (Java 25) eliminates the `synchronized` pinning but JNI pinning persists on ALL Java versions.

**Impact on Pi 5:** With 4 carrier threads, as few as 4 concurrent sqlite-jdbc operations exhaust the carrier pool, stalling all other virtual threads system-wide. This affects EventPublisher.publish() (the core write path), every State Projection write, every EventStore query, and every persistence maintenance operation.

**Mandatory mitigation — platform thread executor pattern (LTD-03):** All sqlite-jdbc operations — reads AND writes — must be submitted to a bounded platform thread executor (`Executors.newFixedThreadPool(N)`), never executed directly on virtual threads. Virtual threads submit database work via `CompletableFuture.supplyAsync(dbCall, dbExecutor)` and await the result. This confines all carrier pinning to dedicated platform threads.

**Executor sizing:**
- Write executor: 1 platform thread (single-writer model)
- Read executor: 2–3 platform threads (matching WAL concurrent reader capacity)

The executor is owned by the Persistence Layer and exposed through the `EventStore` and `StateStore` interfaces — callers never interact with sqlite-jdbc directly. This mirrors the platform thread isolation designed for jSerialComm in Doc 05 §3.2.

**Thread model summary:**

| I/O Type | Thread Type | Reason |
|---|---|---|
| Network I/O (MQTT, HTTP, WebSocket) | Virtual thread | JEP 444 unmounts on socket I/O |
| Serial I/O (Zigbee via jSerialComm) | Platform thread | JNI pins carrier permanently |
| SQLite I/O (all database operations) | Platform thread executor | JNI `synchronized native` pins carrier |
| Sleep/park/timers | Virtual thread | No carrier pinning |

**The critical rule:** `synchronized` blocks also pin carrier threads. On a Pi with 4 cores ≈ 4 carrier threads, one pinned carrier is a 25% capacity loss. ALWAYS use `ReentrantLock`. Check transitive dependencies — third-party code with `synchronized` blocks will pin too.

```java
// WRONG — pins carrier thread
private synchronized void updateState(EntityId id, AttributeValue value) { ... }

// RIGHT — virtual thread unmounts while waiting for lock
private final ReentrantLock stateLock = new ReentrantLock();
private void updateState(EntityId id, AttributeValue value) {
    stateLock.lock();
    try { ... }
    finally { stateLock.unlock(); }
}
```

## 6. SQLite as the Event Store

SQLite in WAL mode is the persistence layer. Single-writer, unlimited-reader concurrency. The write path serializes through the event publisher — this is an architectural simplification, not a limitation.

**Key PRAGMA settings you'll see in tests and configuration:**
```sql
PRAGMA journal_mode = WAL;          -- Write-Ahead Logging
PRAGMA synchronous = NORMAL;        -- fsync on checkpoint, not every commit
PRAGMA cache_size = -128000;        -- 128 MB page cache
PRAGMA mmap_size = 1073741824;      -- 1 GB memory-mapped I/O
PRAGMA busy_timeout = 5000;         -- Wait 5s for write lock
```

**ULID storage:** BLOB(16) in SQLite. Never TEXT. SQLite byte-comparison on BLOB(16) preserves ULID lexicographic ordering. Convert to Crockford Base32 string ONLY at API boundaries (REST responses, log output). In Java, use `EntityId.toBytes()` for database writes and `EntityId.fromBytes()` for reads.

**The domain event store table (V001, 25 columns as of M2-bridge 2026-05-02):**
```sql
CREATE TABLE events (
    global_position   INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id          BLOB(16) NOT NULL,     -- ULID as 16-byte binary
    home_id           BLOB(16) NOT NULL,     -- AMD-34: home identity
    event_type        TEXT     NOT NULL,
    schema_version    INTEGER  NOT NULL DEFAULT 1,
    ingest_time       INTEGER  NOT NULL,     -- Unix microseconds
    event_time        INTEGER,               -- Unix microseconds, nullable
    subject_ref       BLOB(16) NOT NULL,
    subject_type      TEXT     NOT NULL,     -- M2.5: SubjectType discriminator
    subject_sequence  INTEGER  NOT NULL,
    priority          TEXT     NOT NULL DEFAULT 'NORMAL',
    origin            TEXT     NOT NULL DEFAULT 'UNKNOWN',
    actor_ref         BLOB(16),              -- nullable; person/actor ULID (INV-MU-01)
    idempotency_key   TEXT,                  -- AMD-35: persistent idempotency
    correlation_id    BLOB(16) NOT NULL,     -- ULID; equals event_id for root events
    causation_id      BLOB(16),
    event_category    TEXT     NOT NULL,     -- JSON array of category strings
    payload_size      INTEGER  NOT NULL,     -- byte count of payload BLOB
    batch_id          BLOB(16),              -- schema reservation (nullable)
    external_ref      TEXT,                  -- schema reservation (nullable)
    intent_kind       TEXT     NOT NULL DEFAULT 'UNSPECIFIED',  -- reservation
    logical_time      INTEGER  NOT NULL DEFAULT 0,             -- reservation
    node_id           INTEGER  NOT NULL DEFAULT 0,             -- reservation
    payload           BLOB     NOT NULL,     -- serialized event payload
    chain_hash        BLOB(32) NOT NULL DEFAULT x'00...00',    -- AMD-37: tamper evidence
    UNIQUE(subject_ref, subject_sequence)
);
```

**Indexes (post-V003 — `idx_events_subject` dropped in V003 as redundant with `sqlite_autoindex_events_1`):**
```sql
-- idx_events_subject was DROPPED in V003 (duplicate of UNIQUE constraint autoindex)
CREATE INDEX idx_events_type        ON events(event_type, global_position);
CREATE INDEX idx_events_correlation ON events(correlation_id, global_position);
CREATE INDEX idx_events_ingest_time ON events(ingest_time);
CREATE INDEX idx_events_event_time  ON events(COALESCE(event_time, ingest_time));
CREATE INDEX idx_events_actor       ON events(actor_ref) WHERE actor_ref IS NOT NULL;
CREATE UNIQUE INDEX idx_events_idempotency
    ON events(home_id, idempotency_key) WHERE idempotency_key IS NOT NULL;
```

## 7. Processing Modes and Subscriber Lifecycle

Events are processed in different contexts. Your code must handle all four processing modes:

| Mode | When | Behavior Difference |
|---|---|---|
| `LIVE` | Normal operation | Full processing. Side effects execute. Commands dispatch. Notifications send. |
| `REPLAY` | State recovery from checkpoint | State projections update. Side effects DO NOT execute. Commands DO NOT dispatch. |
| `PROJECTION` | Building a read model | State updates only. No side effects. No notifications. |
| `DRY_RUN` | Testing automations | Evaluation occurs. Actions are recorded but not executed. |

**Critical for your code:** If your subscriber has side effects (sends a command, triggers a notification, writes to an external system), check `ProcessingMode` before executing them. During REPLAY, only state updates happen.

**Subscriber Lifecycle Mode (`SubscriberMode`, M3.1):** Separate from the processing-context modes above, each active subscriber has a lifecycle mode governing its runtime state machine (per AMD-42):

| SubscriberMode | Meaning |
|---|---|
| `COLD` | Registered but not yet started. No VT running. |
| `REPLAY` | Catching up from checkpoint to head. Side effects suppressed. |
| `TRANSITION` | Draining replay window while live events arrive. |
| `LIVE` | Processing live events in real time. Side effects execute. |
| `SUSPENDED` | Halted due to circuit breaker or infrastructure failure. |

Transitions are atomic via `AtomicReference` with CAS. The mode FSM is managed by the `InProcessEventBus` (M3.1 production implementation). The subscriber's `onEvent()` callback receives events regardless of mode — it is the subscriber's responsibility to check whether to execute side effects based on the processing context.

## 8. The Subsystem Map

Know where each subsystem lives and what it owns:

| # | Subsystem | Owns | Key Interfaces |
|---|---|---|---|
| 01 | Event Model & Event Bus | Event envelope, type taxonomy, publish-subscribe, active runtime | `EventPublisher`, `EventStore`, `EventBus` (8 methods), `Subscriber`, `SubscriberMode`, `SubscriberSnapshot`. Production impl: `InProcessEventBus` (M3.1). |
| 02 | Device Model & Capabilities | Device/entity records, capability contracts, discovery pipeline | `DeviceRegistry`, `EntityRegistry`, `CapabilityRegistry` |
| 03 | State Store | Materialized state from events, state queries, projection cursor | `StateStore`, `StateQueryService`, `ProjectionAdvancer` (3-param signature, Deliverable 0). |
| 04 | Persistence Layer | SQLite management, WAL tuning, retention, telemetry ring store | `CheckpointStore`, `TelemetryWriter` |
| 05 | Integration Runtime | Adapter lifecycle, thread allocation, crash isolation, health model | `IntegrationSupervisor`, `IntegrationContext` |
| 06 | Configuration System | YAML loading, JSON Schema validation, reload pipeline | `ConfigurationService`, `ConfigurationAccess`, `SchemaRegistry` |
| 07 | Automation Engine | Trigger evaluation, condition checking, action execution, runs | `AutomationRegistry`, `TriggerEvaluator`, `ActionExecutor` |
| 08 | Zigbee Adapter | ZCL cluster mapping, coordinator communication, mesh management | First integration — exercises the Integration Runtime |
| 09 | REST API | HTTP endpoints, request validation, response serialization | Javalin routes, OpenAPI spec |
| 10 | WebSocket API | Real-time event streaming, subscription management | Event stream, state change notifications |
| 11 | Observability | Metrics, health checks, diagnostic endpoints | Health aggregation, JFR integration |
| 12 | Startup/Lifecycle | Boot sequence, shutdown orchestration, recovery | Ordered startup, graceful shutdown |
| 13 | Web UI | Browser dashboard, event trace viewer, device control | Observability-focused MVP UI |

## 9. Shared Types and Where They Live

Types used across multiple subsystems live in shared API modules, not in subsystem-internal modules.

**Identity types** (platform-api, shared identity module):
`EntityId`, `DeviceId`, `AutomationId`, `PersonId`, `HomeId`, `AreaId`, `IntegrationId`, `SystemId` — all typed ULID wrappers.

> **Note:** EventId lives in event-model (`com.homesynapse.event`), not platform-api, despite being a typed ULID wrapper.

**Event types** (event-model module, `com.homesynapse.event`):
`EventEnvelope`, `DomainEvent` (sealed interface), `CausalContext`, `EventPriority`, `EventOrigin`, `ProcessingMode`, `EventDraft` (9 fields), `EventPublisher`, `EventStore`.

**Event bus types** (event-bus module, `com.homesynapse.event.bus`):
`EventBus` (8 methods), `Subscriber`, `SubscriberMode`, `SubscriberSnapshot`, `SubscriberInfo`, `SubscriptionFilter`, `CheckpointStore`, `SubscriberReadConnectionFactory`, `SubscriberReadExecutor`. These live in event-bus, not platform-api or event-model.

**Device types** (device-model module, `com.homesynapse.device`):
`Capability` (sealed interface), `EntityType`, `CommandDefinition`, the Floor/Area spatial aggregates, `EntityRole`.

**Value types** (value-model module, `com.homesynapse.value`):
`AttributeValue` (sealed interface, 8 variants) + `AttributeType` — the **leaf** both event-model and device-model depend on. Relocated here from device-model in M4.0b-4a so an event-model record can carry an `AttributeValue` without forcing an `event → device` JPMS edge. Do not look for `AttributeValue` in device-model.

**Rule:** If you're about to define a type that another subsystem will need, it goes in a shared API module. If you're defining a type that only your subsystem uses internally, it goes in your subsystem's internal module.

## 10. MODULE_CONTEXT.md — Your Cross-Session Memory

Each module that has completed Phase 2 has a `MODULE_CONTEXT.md` file at its root directory. These files are the project's persistent memory across agent sessions. They contain:

- **Complete type inventory** — every public type in the module, its kind, purpose, and key fields/methods
- **Cross-module contracts** — behavioral promises not captured in method signatures (e.g., "EventPublisher.publish() is synchronous — durable before return")
- **Sealed hierarchies** — full permits lists and exhaustive switch patterns
- **Constraints** — which LTDs and INVs actively apply to this module
- **Gotchas** — non-obvious things that caused bugs during Phase 2
- **Phase 3 notes** — implementation guidance, testing strategy, performance targets

**When to read them:** ALWAYS read the MODULE_CONTEXT.md for the module you're working on and all its dependency modules before writing any code. These files exist because design docs are too long to re-read every session, and Java source files don't capture behavioral contracts.

**Where they live:**
```
homesynapse-core/
├── platform/platform-api/MODULE_CONTEXT.md     ← dependency root (read for everything)
├── core/event-model/MODULE_CONTEXT.md          ← event vocabulary (read for event work)
├── core/event-bus/MODULE_CONTEXT.md            ← subscription model (read for subscriber work)
├── core/device-model/MODULE_CONTEXT.md         ← device/entity/capability model
├── core/state-store/MODULE_CONTEXT.md          ← state projection + read model
├── core/persistence/MODULE_CONTEXT.md          ← event store + migrations (Phase 3 active)
└── ...                                          ← + core/value-model (AttributeValue leaf); one per module; only web-ui/dashboard remains a stub
```

**Status (as of HEAD `8028337`, 2026-06-07 — a point-in-time observation, NOT current-by-construction; re-derive at need):** All production JPMS modules have populated MODULE_CONTEXT.md files — including `core/value-model` (created in the M4.0b-4a relocation), `platform/platform-systemd` (populated in M5-A), and `testing/test-support` (populated). The **only remaining stub is `web-ui/dashboard`** (Preact SPA, no compiled Java). `settings.gradle.kts` is the authoritative module list (22 Gradle modules). Prefer MODULE_CONTEXT.md over the design doc for quick orientation — it's a curated, agent-optimized summary — and fall back to the design doc when MODULE_CONTEXT is a stub or you need full specification detail.
