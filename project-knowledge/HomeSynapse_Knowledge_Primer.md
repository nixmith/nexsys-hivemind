<!--
file: project-knowledge/HomeSynapse_Knowledge_Primer.md
purpose: Compressed architectural mental model of HomeSynapse Core (modules, types, gotchas).
audience: All
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-06-07 against `7f44bed` — **M5-A COMPLETE + M5-B/B1 DONE** (platform-systemd `PlatformPaths`/`HealthReporter` impls + the AMD-87 `Expectation` persisted codec; **Doc 15 Cryptographic Architecture LOCKED** — the 15th design doc; AMD-86 + AMD-87 RATIFIED; watermark **AMD-87**; `projectionVersion` 5). Prior spine state: `8ef9e9f` (M4 COMPLETE, watermark AMD-64).
-->

# HomeSynapse Core — Knowledge Primer

Compressed architectural context for the HomeSynapse Core Claude project. This file provides the "mental model" — what each module does, how they connect, where types actually live, and the gotchas that cause mistakes. For full type inventories, read the MODULE_CONTEXT.md files (paths in the Navigation Index).

---

## Architecture in Brief

HomeSynapse Core is a local-first, event-sourced smart home runtime. Java 21 on Amazon Corretto, targeting Raspberry Pi 4/5 with 4 GB RAM. Multi-module Gradle project with JPMS enforcement. All state is derived by replaying immutable events from an append-only SQLite store (WAL mode). Virtual threads for concurrency; no `synchronized` anywhere (ReentrantLock only). No cloud dependency; no external message broker.

The source repo (`homesynapse-core`) contains the code. The companion repo (`homesynapse-core-docs`) contains design documents, governance, and research. Phase 2 (public API contracts — interfaces, records, enums, sealed hierarchies) is complete across all modules (~330+ public Java types). A new **`core/value-model`** leaf module was added in M4.0b-4a (holds the relocated `AttributeValue` hierarchy) — 21 Gradle modules now (17 JPMS-compiled production + 3 scaffold + 1 integration-tests).

**M0 (Prerequisites & Cleanup) completed 2026-04-04.** All CRITICAL/HIGH/MEDIUM audit findings resolved. AMD-31 (command execution order guarantees) created and applied. Traceability indexes populated for Docs 02–11 (161+ type-to-design-doc mappings). MODULE_CONTEXT files updated across 7 modules. Automation critical review fully categorized (28 issues → 4 already addressed, 2 became AMD-31, 16 Phase 3 notes, 10 Tier 2 deferrals).

**M1 (Contract Tests & In-Memory Implementations) completed 2026-04-09.** 9 sub-tasks (M1.1–M1.9) producing 102 contract/fixture test methods across 5 abstract contract test suites. Every interface that will have a production SQLite implementation now has a proven behavioral contract. All MODULE_CONTEXT files updated post-M1 to reflect test infrastructure. Total test suite: ~1,150+ @Test methods (as of M2-bridge completion). Full build: GREEN.

**M2 (Persistence Layer) completed 2026-05-01.** 9 sub-tasks (M2.1–M2.9) producing MigrationRunner, DatabaseExecutor, PlatformThreadWriteCoordinator, ReadExecutor, SqliteEventStore (24-bind INSERT, 25-column V001 schema), AtomicCheckpointWriter, SqlitePersistenceLifecycle. Total test suite: ~1,150+ @Test methods across ~584 Java files. Full build: GREEN.

**M2-bridge (Structural Hardening) completed 2026-05-02.** AMD-34 through AMD-37 applied. V001 schema expanded from 17 to 25 columns (home_id, idempotency_key, payload_size, batch_id, external_ref, intent_kind, logical_time, node_id, chain_hash tightened to NOT NULL). V002 migration added (subscriber_dead_letters table, 11 columns, LOCAL-ONLY). EventDraft expanded from 8 to 9 fields (added idempotencyKey, AMD-35). SqliteEventStore: HomeId injection as 5th constructor param, 24-bind INSERT, ZERO_HASH for chain_hash. Schema reservation pattern established: columns exist in SQLite, populated at INSERT, invisible to Java API until feature ships.

**M2→M3 Bridge (Phase 2 Interface Specifications) completed 2026-05-15.** Three amendments finalized: AMD-38 APPLIED (checkpoint policy: 200 events / 2 s, driven by D1 WAL pathology spike), AMD-39 WITHDRAWN (journal_size_limit stays at LTD-03's 6 MB — bounded-window reader alone prevents WAL growth), AMD-40 APPLIED (retention execution on writer executor, interval-based, bounded chunks). V003 migration ready (snapshots table + redundant idx_events_subject dropped). Ten Phase 2 interfaces added: CheckpointPolicy sealed hierarchy, ProjectionAdvancer, AdvanceResult (state-store); DeploymentProfile, PersistenceConfig, RetentionPolicy, MaintenanceSubscriber, MaintenanceResult (persistence). D1 WAL Pathology Validation Spike empirically confirmed that a continuous reader causes WAL growth to 20.6 MB at 5 events/s; bounded-window reader (close/reopen every 500 rows) keeps WAL at ~4 MB. Write amplification: ~34 KB WAL per ~600 B event (50×) due to 7 indexes.

**M3.1 (InProcessEventBus Core) completed 2026-05-16.** Production InProcessEventBus with 14 types (9 public + 5 package-private — see event-bus MODULE_CONTEXT for full inventory). Full subscriber lifecycle: Subscriber interface, SubscriberMode FSM, SubscriberSupervisor (backoff, circuit breaker), SubscriberDlq, ReplayWindowQueue, SubscriberRuntime. EventBusContractTest expanded from 18 to 44 methods (Tiers 1–8 active, Tiers 9–10 @Disabled). AMD-41/42/43 applied (state projection execution model, subscriber lifecycle/isolation, backpressure/observability). Architecture Invariants expanded to 94 (§19: BUS, PROJ, WRITER, SUB-ISO). **(As of M4 the register is at 133 across 32 categories — AMD-47 §20, AMD-51 §21, AMD-52 §22, AMD-53 §23, and the AMD-54..64 integration block §24–§34.)** Total test suite: ~1,200+ @Test methods across ~600+ Java files. Full build: GREEN.

**M3 (Event Distribution + State Materialization) COMPLETE (2026-05-27).** M3.1 through M3.7 complete (nineteen Claude Code WUs). 7 sub-milestones (M3.1–M3.7). M3.7 shipped the full E2E integration test suite: `HomeSynapseE2eHarness` (composition-root lifecycle harness with real HTTP), `CrashRecoveryHttpIT` (crash + restart with state verification), `EndpointE2eIT` (all five REST endpoints), `InFlightRequestShutdownIT` (graceful shutdown with in-flight requests). Also shipped: `abandon()` contract across `PersistenceFactory`, `InProcessEventBus`, `HomeSynapseCore`; `MinimalEventBusStub` (test double); `MinimalProjectionAdvancer` (real class, closes OR-M3-18) + the no-op `MINIMAL_DERIVATION_RULE` constant lambda in `HomeSynapseCore` (closes OR-M3-17; there is **no** `MinimalDerivationRule` class — corrected 2026-05-28); checkpoint key mismatch fix (`"entity_state"` → `"state_projection"`); `FixedCheckpointPolicy.TESTING` constant; `HomeSynapseConfig` expanded to 4 components (added `checkpointPolicy`). (The M3.7 `MinimalProjectionAdvancer` + no-op `MINIMAL_DERIVATION_RULE` placeholders were **superseded in M4.0b-1** — see the M4 entry below.)

**M4 — Foundation — ✅ COMPLETE (2026-06-05, `8ef9e9f`).** Build GREEN (145 tasks); `projectionVersion` **5**; watermark **AMD-64**. **Workstream A** (projection/derivation): M4.0a (AMD-45 atomic checkpoint, `a441fdf`) → M4.0b-1 (`ProductionDerivationRule` + `DispatchingProjectionAdvancer` REC-28, `cf1a97e`) → M4.0b-2 (AMD-50 backfill + `projectionVersion` 1→2, `7610296`) → M4.0b-3 (AMD-51 typed comparator + 2→3, `98f705b`) → **M4.0b-4a** (relocate the `AttributeValue` hierarchy → new **`com.homesynapse.value`** leaf module to break a JPMS event↔device cycle; AMD-52 §11 erratum; `971cfa1`) → **M4.0b-4b** (AMD-52 typed `StateChangedEvent` payload + tagged-union codec + schema-versioned replay + `projectionVersion` 3→4; `72596cb`) → **M4.0b-5** (AMD-53 timestamp-model unifier, all three activity timestamps event-time-sourced, `projectionVersion` 4→5; `c99b425`) — **typed end-to-end + event-time-deterministic**. **Workstream B** (device-model): M4.B3 (AMD-47 8-variant `AttributeValue` + Upcaster SPI, `60b4185`) → M4.B-S1 (AMD-44 Stage 1: `FloorId`/`Floor`/`Area` + registries + `hardwareIdentifiers` `Set`, `e73e199`) → M4.B-S2 (AMD-44 Stage 2: `EntityRole` + `EntityType` 6×3 legality matrix + `Entity` 11→12, `e76b925`). **Workstream C** (integration-api freeze): M4.C (AMD-54..64, `8ef9e9f`) froze the adapter-facing surface — integration-api 22→40 types; descriptor 8→14, context 10→12, RequiredService 3→5, lifecycle permits 5→10 + 2 capability events; supervisor impl = M9; contract-only, no `module-info`/`projectionVersion` change. **M4.C debt RESOLVED in M5-A Part 2:** the `Expectation` codec (AMD-65 → reassigned AMD-87) is RATIFIED + IMPLEMENTED (`7f44bed`); command-bearing `CapabilityAdded` round-trips; **M9 prerequisite CLEARED.** **M5 window (current):** **M5-A COMPLETE** (`7f44bed`) — platform-systemd `PlatformPaths`/`HealthReporter` impls + the AMD-87 codec + `FloorId` registration; **M5-B/B1 DONE** — **Doc 15 (Cryptographic Architecture) LOCKED** + AMD-86 (INV-PD-07/03 privacy posture) + AMD-87 RATIFIED, watermark **AMD-87**; **M5-D** evidence (Pi-4 microbench → OQ-15-2; energy/erasure interview guide → AMD-86 §3; sd_notify matrix) authored + reviewed. **Next: M6 (Configuration + secrets/crypto)** — see the W24 plan in `nexsys-hivemind/context/planning/weeks/2026-W24_jun08-jun14.md`.

Phase 3 implementation follows a **contract-test-first approach** — M1 built all contract test suites and in-memory implementations before any production code ships (M2+). InMemoryEventStore (27/27 contract tests passing) was the first implementation target (2026-03-27) and serves as the model for all subsequent contract test suites.

---

## Module Map

Modules listed in dependency order. Each module has one flat Java package under `com.homesynapse.*` — verified against MODULE_CONTEXT.md and source on 2026-05-22 (PM Research 4 DQ-4 resolution). Earlier revisions of this section appended "+ subpackages" to a few modules (automation, device-model, integration-zigbee); that annotation was incorrect and has been removed below. The one-flat-package invariant per module is upheld across all 16 JPMS-compiled production modules. MODULE_CONTEXT.md files have enriched first lines with package, type count, and architectural role for quick identification.

### platform-api — `com.homesynapse.platform` + `com.homesynapse.platform.identity`
Dependency root. Zero project dependencies. Typed ULID identity system (**9 wrappers**: DeviceId, EntityId, IntegrationId, AreaId, **FloorId** (added M4.B-S1/AMD-44), AutomationId, PersonId, HomeId, SystemId). The Ulid value type and UlidFactory are separate from the typed wrappers. Platform abstraction interfaces (PlatformPaths, HealthReporter).

### event-model — `com.homesynapse.event`
Most important module. Universal event vocabulary. EventEnvelope (the immutable event wrapper, 14 fields), EventPublisher (sole write path), EventStore (read-side query), EventDraft (pre-publish builder, 9 fields including idempotencyKey added in M2-bridge AMD-35), all domain event payload records, the HomeSynapseException hierarchy, and EventTypes constants. Everything in the system either produces or consumes events defined here.

### value-model — `com.homesynapse.value`
Leaf module (java.base only) added in M4.0b-4a (`971cfa1`, AMD-52 §11 erratum). Holds the relocated sealed **`AttributeValue` hierarchy (8 variants: BooleanValue/IntValue/FloatValue/StringValue/EnumValue/QuantityValue/ArrayValue/DegradedAttributeValue)** + `AttributeType`. Both event-model and device-model `requires com.homesynapse.value` (transitive), which is why `event` no longer reaches `device` (the cycle the typed AMD-52 payload would have created is structurally gone). `AttributeSchema`/`AttributeValueUpcaster` stayed in device-model. `QuantityValue` canonicalises units at construction (AMD-47-INV-03); the typed comparator (AMD-51) and the typed `StateChangedEvent` payload codec (AMD-52) operate over these types.

### event-bus — `com.homesynapse.event.bus`
Pull-based, notification-driven event distribution. 33 production types (19 public + 14 package-private) after M3.6d-a — three types (QueueSaturationHealthCheck, HealthSignal, HealthLevel) promoted to public alongside the M3.6b InProcessEventBus promotion. See MODULE_CONTEXT for full inventory. Key public types: EventBus (8 methods including subscribeRuntime/resume/subscribers), Subscriber, SubscriberInfo, SubscriptionFilter, CheckpointStore, SubscriberMode (5-value FSM), SubscriberSnapshot, SubscriberReadConnectionFactory, SubscriberReadExecutor, EventBusConfig (M3.6b — 2-field record for operator-tunable bus parameters), InProcessEventBus (public as of M3.6b, DEC-M3-16 — canonical 7-arg constructor accepting EventBusConfig; `PUBLISHER_BLOCKED_DEPTH_THRESHOLD` is now an instance field from config, not a static constant), QueueSaturationHealthCheck + HealthSignal + HealthLevel (M3.6d-a, DEC-M3-17 — the 3-type chain is the minimum viable promotion because the constructor's `Consumer<HealthSignal>` parameter would trigger `-Xlint:exports` otherwise). Bus notifies via LockSupport.unpark(); subscribers pull from EventStore. Never pushes EventEnvelopes directly. ReplayWindowQueue capacity is parameterized (default 10,000 via no-arg constructor; custom via `ReplayWindowQueue(int maxCapacity)` — M3.6b).

### device-model — `com.homesynapse.device`
Physical and logical device model. One flat package. Entity (not Device) is the atomic addressable unit — a single physical device may produce multiple entities. Sealed Capability hierarchy. **NOTE (M4.0b-4a, `971cfa1`): the sealed `AttributeValue` hierarchy NO LONGER lives here — it was relocated to the new `core/value-model` module (`com.homesynapse.value`) to break a JPMS event↔device cycle. `AttributeSchema` + `AttributeValueUpcaster` stayed in device-model.** **AMD-44 (Floor/EntityRole, M4.B-S1/S2)** added: `Floor`/`Area` records + `FloorRegistry`/`AreaRegistry` interfaces (no impl); the `EntityRole` enum (PRIMARY/DIAGNOSTIC/CONFIG) + `EntityType` 6×3 legality matrix (`allows`/`legalRoles`); `Entity` 11→12 + `ProposedEntity` 3→4 (`entityRole`, null→PRIMARY coercion + construction-time matrix guard); `hardwareIdentifiers` `List`→`Set`. `StandardCapabilities` (device-model **main**, M4.0b-3 / DP-K) is the production catalogue of the standard capabilities + their `AttributeSchema`s — the future `CapabilityRegistry` seed. device-model 57 types.

### state-store — `com.homesynapse.state`
Materialized view over the event stream. EntityState projects current state from events. StateProjection subscribes with coalesceExempt=true (must see every event). Availability enum lives here. ViewCheckpointStore (different from event-bus CheckpointStore). **The staleAfter + Clock staleness model is HomeSynapse's #1 architectural differentiator — proven at the data level by EntityStateTest (12 methods, M1.9).** M3.6d-a added the `ReadinessSource` public interface (single method `mode() → SubscriberMode`). M3.6e.1 added `MaterializedStateQueryService` (public final, static factory `create(StateProjection)`, implements all 5 `StateQueryService` methods — returns `Optional.empty()` / empty `Map` when projection not LIVE, no exceptions for callers). Total post-M3.6e.1: 21 public types + 1 package-private (`SelfProducedFilter`) = 22 production types.

M2→M3 bridge added 5 types: CheckpointPolicy (sealed interface: shouldCheckpoint(events, elapsed, readerLag)), FixedCheckpointPolicy (HOME_DEFAULT: 200 events / 2 s per AMD-38; TESTING: 1 event / 100ms added M3.7 for test determinism), AdaptiveCheckpointPolicy (reserved for post-MVP pressure-aware mode), ProjectionAdvancer (interface: advance(fromPosition, maxRows) → AdvanceResult, ≤500 rows, ≤2 s read transaction, bounded-window contract), AdvanceResult (record).

### persistence — `com.homesynapse.persistence`
SQLite storage. Two databases: main (events, state) and telemetry. TelemetryWriter uses a ring buffer per RetentionTier. WriteCoordinator (AMD-06/AMD-32, package-private) serializes all writes with priority ordering; `queueSize()` method added in M3.6d-b for bus writer-queue-depth observation (DEC-M3-14). WritePriority (package-private, 5 levels: EVENT_PUBLISH → STATE_PROJECTION → WAL_CHECKPOINT → RETENTION → BACKUP). WAL mode is always on. **LTD-19 governs event payload serialization: EventTypeRegistry + PersistenceJacksonModule + DegradedEvent fallback.** V001 events table has 25 columns including schema reservations for multi-home (home_id, AMD-34), persistent idempotency (idempotency_key, AMD-35), tamper-evidence (chain_hash NOT NULL with zero-vector default, AMD-37), and 6 Tier 2 reservation columns (payload_size, batch_id, external_ref, intent_kind, logical_time, node_id). V002 adds subscriber_dead_letters table for poison event parking (AMD-36, LOCAL-ONLY sync scope). SqliteEventStore constructor takes HomeId as 5th parameter (AMD-34). Schema reservation pattern: reserved columns populated at INSERT time, not exposed on EventEnvelope until their features ship.

M2→M3 bridge added 5 public types: DeploymentProfile (enum: STUDIO/HOME/PERFORMANCE with per-profile PRAGMA values; 8 fields — 3 original + 3 added in M3.6a: busyTimeoutMs, lockingMode, readThreadCount + 2 added in M3.6e.1: httpThreads, httpMaxThreads), PersistenceConfig (bundles profile + retention), RetentionPolicy (per-priority retention durations, SOURCE_DEFAULT from EventPriority Javadoc: 7d/90d/365d), MaintenanceSubscriber (interface: writer-executor-only, interval-based, bounded chunks per AMD-40), MaintenanceResult (record). V003 migration adds snapshots table and drops redundant idx_events_subject. M3.6a added package-private `LockingMode` enum (NORMAL, EXCLUSIVE). `DatabaseExecutor` constructor now accepts `DeploymentProfile profile` instead of `int readThreadCount`; hardcoded `CONNECTION_PRAGMAS` list replaced by `connectionPragmas(DeploymentProfile)` rendering method. `SqlitePersistenceLifecycle` constructor now accepts `PersistenceConfig config` instead of `int readThreadCount`; expanded from 4 stores to 6 in M3.6d-b (added `SqliteStateStore` + `SqliteDeadLetterStore`). M3.6d-a: `SqliteStateStore` now `implements StateCheckpointSource` (method renamed `serialize(int)` → `serializeCheckpoint(int)`; both `serializeCheckpoint` and `loadedProjectionVersion()` promoted to public via the interface). Class itself remains package-private. M3.6d-b added `PersistenceFactory` (public final, implements `AutoCloseable`) — wraps package-private `SqlitePersistenceLifecycle` per DEC-M3-16 factory pattern. Static `start(Path, PersistenceConfig, Clock, HomeId, List<Class<? extends DomainEvent>>)` factory; 8 accessor methods returning public interface types. Also added `SqliteSubscriberReadConnectionFactory` (public) + `SqliteSubscriberReadExecutor` (package-private) — production `SubscriberReadConnectionFactory` implementation.

### automation — `com.homesynapse.automation`
Rule engine. **One flat package** — all ~52 types in `com.homesynapse.automation` (verified against `core/automation/MODULE_CONTEXT.md` line 55 and source tree on 2026-05-22; resolves Research 4 DQ-4). No `dispatch` or `evaluator` or `policy` sub-packages exist. Trigger → Condition → Action pipeline. Has 4 sealed hierarchies (Selector, TriggerDefinition, ConditionDefinition, ActionDefinition) — the highest concentration of any module. Conditions evaluate against positional state snapshots (AMD-03). Cascade depth limiting (AMD-04). Command execution ordering (AMD-31).

### configuration — `com.homesynapse.config`
YAML 1.2 config loading, JSON Schema validation, AES-256-GCM encrypted secrets. ConfigModel is Map-based in Phase 2 (typed config objects are Phase 3+). ConfigurationChangeListener fires synchronously before the config_changed domain event is published.

### integration-api — `com.homesynapse.integration`
The one module every protocol adapter depends on. Re-exports all core modules via `requires transitive`. Defines IntegrationFactory, IntegrationAdapter, IntegrationContext (large DI record), CommandHandler. DECIDE-04: direct factory construction, no ServiceLoader. **FROZEN at M4.C (AMD-54..64, `8ef9e9f`) — 22→40 types** (contract-only; supervisor impl = M9): `IntegrationDescriptor` 8→14 (config-schema versioning, soft-deps, isolation level, planned-restart-timeout), `IntegrationContext` 10→12 (nullable `security`/`discovery`), `RequiredService` 3→5 (DISCOVERY/SECURITY), `IntegrationAdapter` 4→8 (four `default` lifecycle hooks), `IntegrationLifecycleEvent` 5→10 permits (dot-namespaced `integration.*` event strings); NEW: `CapabilityEvent` sealed iface + `CapabilityAdded`/`CapabilityRemoved` (+`CapabilityRemovalReason`), `CapabilityPublisher`, `CredentialRotator` (`rotate(Map)`), `SecurityServices`/`DiscoveryServices` aggregators, `BackoffParameters`, `ReauthOutcome`/`ConfigUpdateOutcome`(+REJECTED)/`MigrationOutcome`/`IsolationLevel`, code-bearing `PermanentIntegrationException` ctor pair. All with back-compat convenience ctors. **The `Expectation` persisted codec (AMD-65 → AMD-87) IMPLEMENTED in M5-A Part 2 (`7f44bed`) — command-bearing `CapabilityAdded` now round-trips; M9 prereq CLEARED.**

### integration-runtime — `com.homesynapse.integration.runtime`
OTP-style one-for-one supervisor (**impl = M9**, not yet built — only the Phase-2/AMD-54..64 contract surface exists). Manages adapter lifecycle, health monitoring, restart with backoff. ExceptionClassification **3→4** at M4.C (+`AUTH_FAILED`, last) drives retry decisions. M4.C added `HealthDetail` (12-value enum) + `IntegrationHealthRecord` 13→14 (+`detail`). Kahn's algorithm for startup ordering (AMD-14).

### integration-zigbee — `com.homesynapse.integration.zigbee`
Zigbee 3.0 coordinator adapter. One flat package (verified 2026-05-22). First and only MVP protocol adapter. IEEEAddress is a raw 64-bit long (NOT a ULID). Sealed ZigbeeFrame and ManufacturerCodec hierarchies. CoordinatorTransport (not thread-safe) vs CoordinatorProtocol (thread-safe). Route health monitoring (AMD-07).

### rest-api — `com.homesynapse.api.rest` + subpackages
HTTP command interface. RFC 9457 problem types. 4-phase command lifecycle (ISSUED → DISPATCHED → EXECUTING → result). Idempotency keys (AMD-08). ApiRequest.body is Object, not JsonNode. M3.6e.1 added `ReadinessFilter` (package-private Javalin `before` handler — returns 503 + JSON when not LIVE), `RestFilters` (public final utility, DEC-M3-16 gateway wrapping `ReadinessFilter` with `Object`-typed parameter to erase Javalin from public API surface), and `ProblemType.STATE_STORE_REPLAYING` (new enum constant for 503 responses). M3.6e.2 added 8 package-private types: `EndpointContext` (SPI interface), `JavalinEndpointContext` (adapter), `EndpointResponses` (utility), `ListEntitiesEndpoint`, `GetEntityEndpoint`, `GetEntityStateEndpoint`, `DlqStatusEndpoint`, `ProjectionStatusEndpoint`. `RestFilters` gained 2 new public gateway methods (`addEntityEndpoints`, `installAdminEndpoints`). Module-info now has `requires transitive com.homesynapse.state`, `requires com.homesynapse.event.bus`, `requires io.javalin`, `requires org.slf4j`. 38 production types total (28 Phase 2 + 2 M3.6e.1 + 8 M3.6e.2).

### websocket-api — `com.homesynapse.api.websocket`
Real-time event streaming. WsMessage sealed hierarchy. Three-stage backpressure: NORMAL → BATCHED → COALESCED. Commands are NOT accepted over WebSocket (read-only). WebSocket does NOT produce domain events.

### observability — `com.homesynapse.observability`
Health model (HealthStatus, HealthTier, LifecycleState), trace model, metrics, log control, JFR integration. HealthTier provides hierarchical aggregation (entity → integration → subsystem → system). Local-first tracing, not OpenTelemetry.

### lifecycle — `com.homesynapse.lifecycle`
Process-level lifecycle orchestration. After M4.0b-1: 8 public + **3** package-private types (`NotifyingEventPublisher`, `SharedScheduler`, `ThrowingStateQueryService`). The M3.7 `MinimalProjectionAdvancer` was **DELETED in M4.0b-1** — the production advancer is now `DispatchingProjectionAdvancer` (package-private in **state-store**, `com.homesynapse.state`, reached via `ProjectionAdvancer.dispatching(EventStore)`), and the no-op `MINIMAL_DERIVATION_RULE` lambda is retired in favour of `DerivationRule.production()` (`ProductionDerivationRule`). `HomeSynapseCore` now passes `projectionVersion = 3` (M4.0b-3 / AMD-51 typed comparator — was 2 at M4.0b-2) and wires the typed `DerivationRule.production(comparator, policy, AttributeSchemaResolver.of(StandardCapabilities.attributeSchemas()))`. Phase 2 types (LifecyclePhase enum, SubsystemStatus enum, LifecycleEventType utility class, SubsystemState record, SystemHealthSnapshot record, SystemLifecycleManager interface) coexist with M3.6 composition-root types: `HomeSynapseConfig` (public record, 4 components: `PersistenceConfig persistence` + `EventBusConfig eventBus` + `CheckpointPolicy checkpointPolicy` + static `HOME_DEFAULT`/`testing()` factory — expanded from 2→4 in M3.7 checkpoint fix), `HomeSynapseCore` (public final, implements `ReadinessSource` — 16-step bootstrap after M3.6e.2: PersistenceFactory.start → BusMetrics.jfr → InProcessEventBus → DerivedWriteRateLimit → StateProjection.create → subscribeRuntime → healthSignalHandler → QueueSaturationHealthCheck → SharedScheduler → started=true → MaterializedStateQueryService.create → Javalin server on port 7070 with readiness filter; `DeploymentProfile` thread pool sizing: STUDIO 1/4, HOME 2/8, PERFORMANCE 4/16; 4-arg constructor `(Path, HomeSynapseConfig, Clock, HomeId)`; `stateQueryService()` returns real `MaterializedStateQueryService` — M3.6e.1; `stop()` tears down in reverse order), `SharedScheduler` (package-private final, 50 ms refill + 1 s tick — M3.6d-a), `ThrowingStateQueryService` (package-private final, kept as dead code — replaced by MaterializedStateQueryService in M3.6e.1). Module-info includes `requires transitive` for persistence, event.bus, state-store, plus non-transitive `requires org.slf4j`, `requires com.homesynapse.integration`, `requires com.homesynapse.api.rest`, `requires io.javalin`, `requires org.eclipse.jetty.util`. 10-phase sequential startup, no backward transitions. Fatal vs non-fatal subsystem classification. 30-second shutdown budget.

### homesynapse-app — `com.homesynapse.app`
Assembly apex. All `requires` are non-transitive. No exports. ApplicationAssembler wires all subsystems together — manual DI, no framework.

### Scaffold modules
**platform-systemd** — systemd integration (sd_notify, watchdog). **test-support** — shared test fixtures (11 types: TestClock, SynchronousEventBus, EventCollector, TestSubscriber, NoRealIoExtension, RealIo, GivenWhenThen, plus 4 custom AssertJ assertions). **dashboard** — Preact web UI, separate build pipeline.

---

## Dependency Graph

```
platform-api (root — zero dependencies)
    │
event-model
    │
┌───┴────────────┬──────────────┐
event-bus     device-model    persistence
    │             │
    └──────┬──────┘
       state-store
           │
┌──────────┼──────────────┐
automation  configuration  observability
    │            │              │
    └──────┬─────┘              │
     integration-api ───────────┘
     (re-exports all core modules)
           │
┌──────────┼──────────────┐
integration-runtime  integration-zigbee
           │
┌──────────┼──────────┐
rest-api  websocket-api  lifecycle
           │
     homesynapse-app
     (requires all, exports nothing)
```

---

## Boot Order

```
CREATED → INITIALIZING → CONFIGURING → PERSISTENCE_READY →
EVENT_SYSTEM_READY → CORE_SERVICES_READY → INTEGRATIONS_READY →
API_READY → RUNNING → SHUTTING_DOWN (30-second budget, reverse order)
```

---

## Build Infrastructure State

**Convention plugins** (4 files in `build-logic/src/main/kotlin/`):
- `homesynapse.java-conventions.gradle.kts` — Base: Java 21 toolchain, `-Xlint:all -Werror`, Spotless copyright headers, JUnit 5, Maven Central
- `homesynapse.library-conventions.gradle.kts` — Extends java-conventions + `java-library`. Applied by 11 library modules.
- `homesynapse.test-fixtures-conventions.gradle.kts` — Extends library-conventions + `java-test-fixtures`. Applied by 6 modules (event-model, device-model, state-store, persistence, integration-api, configuration).
- `homesynapse.application-conventions.gradle.kts` — Extends java-conventions + `application`. Applied by homesynapse-app only.

**Dependency enforcement:** `modules-graph-assert` 2.7.1 configured in root `build.gradle.kts` with layer-based allowed/restricted rules. Prevents core→integration, core→API, platform→core reverse dependencies. Includes intra-API-layer rule (`api:.* -> api:.*`) for websocket-api → rest-api dependency.

**testFixtures source sets:** Created on 6 modules (event-model, device-model, state-store, persistence, integration-api, configuration). All populated with contract tests and in-memory implementations as of M1.9.

**CI:** `.github/workflows/ci.yml` — `./gradlew check` on push to main/develop and on PRs. Amazon Corretto 21. 15-minute timeout.

**Version catalog:** `gradle/libs.versions.toml` is complete. All dependencies pinned. Jackson at 2.18.6 (floor: 2.18.4 per LTD-19).

**Traceability indexes:** Populated for Docs 02–11 with 161+ type-to-design-doc mappings (completed during M0). Docs 01, 12, 13, 14 still use their prior format.

---

## Type Location Reference

Types that are commonly looked for in the wrong module:

| Type | Actually in | Not in |
|------|------------|--------|
| EventId | event-model (`com.homesynapse.event`) | platform-api |
| AutomationId | platform-api (`com.homesynapse.platform.identity`) | automation |
| RunId | automation (`com.homesynapse.automation`) | platform-api |
| Availability | state-store (`com.homesynapse.state`) | device-model |
| HomeSynapseException | event-model (`com.homesynapse.event`) | a "common" module |
| ConfigurationValidationException | event-model (`com.homesynapse.event`) | configuration |
| ConfigurationLoadException | configuration (`com.homesynapse.config`) | event-model |
| CheckpointStore | event-bus (`com.homesynapse.event.bus`) — stores `long` positions | state-store |
| ViewCheckpointStore | state-store (`com.homesynapse.state`) — stores `byte[]` data | event-bus |
| WriteCoordinator | persistence (`com.homesynapse.persistence`) — **package-private** | event-model or event-bus |
| WritePriority | persistence (`com.homesynapse.persistence`) — **package-private** | event-model |
| PermanentIntegrationException | integration-api (`com.homesynapse.integration`) | event-model |
| HealthStatus | observability (`com.homesynapse.observability`) | lifecycle or platform-api |
| PlatformPaths | platform-api (`com.homesynapse.platform`) | lifecycle |
| HealthReporter | platform-api (`com.homesynapse.platform`) | observability |
| ConsistentSnapshot | state-store (`com.homesynapse.state`) — AMD-03 | not StateSnapshot |
| InMemoryEventStore | event-model testFixtures (`com.homesynapse.event.test`) | `com.homesynapse.event` (stale copy deleted M1.9) |
| InMemoryEventBus | event-bus testFixtures (`com.homesynapse.event.bus.test`) | test-support (SynchronousEventBus is a different, simpler fixture) |
| EventBusConfig | event-bus (`com.homesynapse.event.bus`) — public record, `core/event-bus` | persistence or configuration |
| LockingMode | persistence (`com.homesynapse.persistence`) — **package-private** enum, `core/persistence` | event-bus or platform-api |
| ReadinessSource | state-store (`com.homesynapse.state`) — public interface (M3.6d-a) | event-bus or lifecycle |
| HomeSynapseConfig | lifecycle (`com.homesynapse.lifecycle`) — public record (M3.6d-a) | app or platform-api |
| SharedScheduler | lifecycle (`com.homesynapse.lifecycle`) — **package-private** final (M3.6d-a) | observability or app |
| ThrowingStateQueryService | lifecycle (`com.homesynapse.lifecycle`) — **package-private** final (M3.6d-a) | state-store |
| QueueSaturationHealthCheck | event-bus (`com.homesynapse.event.bus`) — public (M3.6d-a, DEC-M3-17) | observability |
| HealthSignal | event-bus (`com.homesynapse.event.bus`) — public record (M3.6d-a, DEC-M3-17) | observability |
| HealthLevel | event-bus (`com.homesynapse.event.bus`) — public enum (M3.6d-a, DEC-M3-17) | observability |
| MaterializedStateQueryService | state-store (`com.homesynapse.state`) — public final (M3.6e.1) | lifecycle or rest-api |
| ReadinessFilter | rest-api (`com.homesynapse.api.rest`) — **package-private** (M3.6e.1) | lifecycle or state-store |
| RestFilters | rest-api (`com.homesynapse.api.rest`) — public final utility (M3.6e.1, DEC-M3-16 gateway; expanded M3.6e.2 with `addEntityEndpoints` + `installAdminEndpoints`) | lifecycle |
| EndpointContext | rest-api (`com.homesynapse.api.rest`) — **package-private** interface (M3.6e.2 SPI) | lifecycle or state-store |
| JavalinEndpointContext | rest-api (`com.homesynapse.api.rest`) — **package-private** (M3.6e.2 adapter for EndpointContext) | lifecycle |

---

## Critical Gotchas

These are the specific mistakes that AI agents commonly make on this codebase. Each one has caused incorrect code or analysis in past sessions.

**M3.7 corrections (2026-05-27):**
- `HomeSynapseConfig` has **4 components** (not 2 or 3). M3.7 added `checkpointPolicy` (defaults to `FixedCheckpointPolicy.HOME_DEFAULT`; `testing()` factory uses `FixedCheckpointPolicy.TESTING`).
- `SqlitePersistenceLifecycle` uses `"state_projection"` as the view checkpoint key (not `"entity_state"` — that was a key mismatch bug fixed in M3.7). The canonical key is `HomeSynapseCore.PROJECTION_SUBSCRIBER_ID = "state_projection"`.
- lifecycle module has **11 types** after M4.0b-1 (8 public + 3 package-private). The 3 package-private types are `NotifyingEventPublisher`, `SharedScheduler`, `ThrowingStateQueryService`. **`MinimalProjectionAdvancer` was DELETED in M4.0b-1** (`cf1a97e`) — the production advancer is `DispatchingProjectionAdvancer` (package-private in **state-store**). The no-op `MINIMAL_DERIVATION_RULE` lambda is retired; the real derivation is `DerivationRule.production()` → `ProductionDerivationRule` (package-private in state-store). There never was a `MinimalDerivationRule` class (that was a phantom, corrected 2026-05-28).
- `FixedCheckpointPolicy` has **two constants**: `HOME_DEFAULT` (200 events / 2s) and `TESTING` (1 event / 100ms). The TESTING constant exists for deterministic checkpoint triggering in integration tests.
- `abandon()` is a test-only lifecycle method on `HomeSynapseCore`, `PersistenceFactory`, and `InProcessEventBus` — releases OS resources without durability operations. Used by `HomeSynapseE2eHarness` to simulate `kill -9`. Not part of the normal `stop()` path.

**M3.6e.2 corrections (2026-05-22):**
- `HomeSynapseCore` bootstrap is **16 steps**, not 14. M3.6e.2 added entity query endpoint registration + admin endpoint registration via `RestFilters` gateway.
- rest-api has **38 production types** (28 Phase 2 + 2 M3.6e.1 + 8 M3.6e.2). The 8 new types are all package-private (5 endpoint handlers + EndpointContext SPI + JavalinEndpointContext adapter + EndpointResponses utility).
- ArchUnit rules are now **9** (7 original + 2 M3.6e.2). New: `QUERY_SERVICE_READ_ONLY` (REST endpoints cannot access persistence directly) and `REST_ENDPOINTS_NO_EVENT_PUBLISHING` (REST endpoints cannot publish events). The latter uses `accessClassesThat().belongToAnyOf(EventPublisher.class)` form.
- `RestFilters` now has **3 public methods** (1 from M3.6e.1 + 2 from M3.6e.2): `installReadinessGate`, `addEntityEndpoints`, `installAdminEndpoints`. All use `Object`-typed parameters per DEC-M3-16.

**M3.6e.1 corrections (2026-05-22):**
- DeploymentProfile has **8 fields**, not 3 or 6. M3.6a added 3 (busyTimeoutMs, lockingMode, readThreadCount); M3.6e.1 added 2 (httpThreads, httpMaxThreads).
- `HomeSynapseCore` bootstrap is **16 steps** (14 from M3.6e.1, expanded to 16 in M3.6e.2). M3.6e.1 added MaterializedStateQueryService wiring + Javalin server on port 7070.
- `stateQueryService()` returns **MaterializedStateQueryService**, not `ThrowingStateQueryService`. Replaced in M3.6e.1.
- rest-api is no longer "zero requires" — M3.6e.1 added `requires transitive com.homesynapse.state`, `requires com.homesynapse.event.bus`, `requires io.javalin`, `requires org.slf4j`.
- `ReadinessFilter` is **package-private** (not public). DEC-M3-16 gateway pattern: `RestFilters.installReadinessGate(Object, ReadinessSource)` is the public entry point. The `Object` parameter deliberately erases `io.javalin.Javalin`.
- **Gradle/JPMS scope rule:** `requires transitive` in module-info → `api` in build.gradle.kts; plain `requires` → `implementation`. Mismatching causes downstream compilation failures.

**M3.6a/M3.6b corrections (2026-05-20):**
- InProcessEventBus is **public** (not package-private). Promoted in M3.6b per DEC-M3-16.
- DatabaseExecutor accepts `DeploymentProfile`, not `int readThreadCount`. Hardcoded PRAGMAs are gone — all tuning goes through the profile.

**M3.6c/M3.6d-a corrections (2026-05-20):**
- `EventTypes.CORE_PRODUCTION_EVENT_CLASSES` (22 classes) lives in `core/event-model`; `IntegrationEvents.LIFECYCLE_EVENT_CLASSES` (5 classes) lives in `integration/integration-api`. Aggregation at composition root via `Stream.concat(...).toList()`. Do NOT re-introduce per-call-site inline class imports (M3.6c removed 27 of them across AllEventClasses + IntegrationTestHarness).
- `QueueSaturationHealthCheck` + `HealthSignal` + `HealthLevel` are all **public** (M3.6d-a, DEC-M3-17). The 3-type chain is the minimum viable promotion: the constructor's `Consumer<HealthSignal>` parameter chains both types, and `-Xlint:exports` enforces transitive accessibility. Pre-promotion check: every type appearing in the class's public constructor signature, public method signatures, public field types, and return types must itself already be public.
- `SqliteStateStore` is **still package-private**, but `serializeCheckpoint(int)` and `loadedProjectionVersion()` are **public via the StateCheckpointSource interface** (M3.6d-a). The composition root exposes the same instance via the interface type.
- `ReadinessSource` (state-store, M3.6d-a) is a public interface with one method `mode() → SubscriberMode`. Consumed by M3.6e's MaterializedStateQueryService. Implemented by the composition root via delegation to `StateProjection.currentMode()`.
- Lifecycle module is no longer "scaffold-only" — M3.6d-a added `HomeSynapseConfig` (public record), `SharedScheduler` (package-private final), `ThrowingStateQueryService` (package-private final). `requires transitive` for persistence, event.bus, state-store; non-transitive `requires org.slf4j`.

**Pattern lesson (M3.6d sub-divide, 2026-05-20):** When a brief's "Files to Create or Modify" table grows past ~18 entries during discovery, sub-dividing is usually the right move. M3.6d was sub-divided into M3.6d-a (satellite changes, 2026-05-20 `25bc23b`) and M3.6d-b (composition-root wiring, pending PM instruction) per the user's Option A decision after Coder pushback identified seven source-vs-brief mismatches. Large WUs compound risk and review burden. See coder-lessons.md M3.6d-a entry #2.

**Field counts that get hallucinated wrong:**
- EventEnvelope has **14 fields** (not 13). The 14th is `actorRef` (Ulid, nullable).
- CausalContext has **2 fields** (not 3). `actorRef` was promoted to EventEnvelope.
- EventDraft has **9 fields** (not 7 or 8). The 8th is `actorRef`, the 9th is `idempotencyKey` (String, nullable, max 128 chars — AMD-35).
- EntityState has **9 fields**. The 9th is `stale` (boolean, derived at read time from `staleAfter` + Clock).
- CommandStatusResponse has **8 fields** (not 7). The 8th is `terminal` (boolean — true when the command lifecycle is complete).
- IntegrationContext has **12 fields** (M4.C added nullable `security`/`discovery`; was 10). It's a large DI record.
- IntegrationHealthRecord has **14 fields** (M4.C added `detail` after `state`; was 13) including a weighted `healthScore` and `plannedRestart`.

**Virtual thread carrier pinning (AMD-26 — CRITICAL for Phase 3):**
- ALL sqlite-jdbc operations MUST run on platform threads, NOT virtual threads. The xerial sqlite-jdbc driver uses `synchronized native` methods that double-pin carrier threads (JNI call holds the carrier even after the monitor is released).
- Mandatory pattern: `CompletableFuture.supplyAsync(dbCall, platformThreadExecutor)`. Executor sizing: 1 write thread (single-writer), 2–3 read threads.
- This affects: persistence (EventStore, TelemetryWriter, MaintenanceService), state-store (ViewCheckpointStore), event-bus (CheckpointStore writes), and any subscriber that reads from EventStore.
- JEP 491 (Java 25) does NOT fix this — it eliminates `synchronized`-monitor pinning but NOT JNI pinning. The platform thread executor is required on ALL Java versions.
- Source: AMD-26, Virtual Thread Risk Audit finding B-4, LTD-03 specification.

**Bounded-window reader pattern (AMD-38 / D1 spike — CRITICAL for M3):**
- The State Projection (and any future subscriber reading from EventStore) MUST close and reopen its read transaction between chunks. A held read transaction prevents WAL checkpoint advancement — D1 spike proved WAL grows to 20.6 MB in 120 seconds at just 5 events/s with a continuous reader.
- The ProjectionAdvancer interface enforces this: each advance() call is an independent read transaction, ≤500 rows, ≤2 s duration.
- The active checkpoint cycle (30 s PASSIVE) is defense-in-depth, not load-bearing. The bounded-window pattern working with SQLite's default wal_autocheckpoint is sufficient.
- Write amplification on the V001 schema is ~34 KB WAL per ~600 B event (50×) due to 7 indexes + autoindex. This means 30 seconds of starved writes at 5 events/s costs ~5 MB of WAL.

**Semantic traps:**
- Entity is the atomic unit, NOT Device. All state events target EntityId. A Device groups Entities.
- Empty `eventTypes` in SubscriptionFilter means subscribe to ALL events, not none.
- `coalesceExempt` on SubscriptionFilter is critical — State Projection and Pending Command Ledger must see every event.
- EventPublisher.publishRoot() takes **1 parameter** (not 2). `actorRef` is on the EventDraft.
- EventPriority.severity() is the correct accessor (not ordinal). CRITICAL=0, NORMAL=1, DIAGNOSTIC=2.
- Ulid.compareTo() uses **unsigned comparison** (Long.compareUnsigned). Do NOT use Long.compare().
- Ulid.toString() is **Crockford Base32** (not RFC 4648 standard Base32).
- IEEEAddress in zigbee is a **raw 64-bit long**, not a ULID.
- CoordinatorTransport is **NOT thread-safe**; CoordinatorProtocol IS.
- ApiRequest.body is **Object**, not JsonNode. Framework-agnostic.
- WebSocket is **read-only**. Commands go through REST only. WebSocket does NOT produce domain events.
- SubscriberId is a **plain String**, not a typed wrapper.
- rest-api had **zero requires directives** in Phase 2. M3.6e.1 added 4: `requires transitive com.homesynapse.state`, `requires com.homesynapse.event.bus`, `requires io.javalin`, `requires org.slf4j`.
- ConfigModel is **Map-based** in Phase 2. Typed config objects are Phase 3+.
- IdempotencyClass uses `CONDITIONAL` across all documents (Doc 01, Doc 02, Doc 07). Doc 02 was corrected 2026-03-21. CONDITIONAL is canonical.
- RunStatus has **7 values** (INTERRUPTED was added by architecture benchmark).

**Test infrastructure traps:**
- InMemoryEventBus and SynchronousEventBus are **different tools for different fidelity levels.** SynchronousEventBus (test-support) invokes all handlers regardless of filter — simple unit tests. InMemoryEventBus (event-bus testFixtures) evaluates SubscriptionFilter.matches(), checks checkpoint positions, requires EventStore + CheckpointStore injection — contract tests and integration-level testing.
- The stale `InMemoryEventStore` copy at `com.homesynapse.event.InMemoryEventStore` was **deleted in M1.9.** Only the canonical version at `com.homesynapse.event.test.InMemoryEventStore` exists. Do not recreate the deleted file.
- testFixtures dependencies require BOTH `testFixturesImplementation(testFixtures(...))` AND `testImplementation(testFixtures(...))` declarations. The java-conventions plugin only adds JUnit/AssertJ to `testImplementation`, not `testFixturesImplementation`.

**EventStore query traps:**
- `readBySubject` pagination: `EventPage.nextPosition` carries the last **subjectSequence** (not globalPosition), because `readBySubject` accepts `afterSequence` as its cursor parameter. `readFrom` and `readByType` use globalPosition. Mixing up the cursor type silently returns wrong results.
- `readByTimeRange` uses `COALESCE(event_time, ingest_time)` as the effective time. Range is `[from, to)` — inclusive start, exclusive end.
- `readByCorrelation` returns `List<EventEnvelope>`, NOT `EventPage`. Causal chains are bounded (Doc 01 §4.5 warns at depth 50).
- InMemoryEventStore assigns `List.of(EventCategory.SYSTEM)` as a default category for all events. Production `SqliteEventStore` will implement the full eventType→category mapping from Doc 01 §4.4. Contract tests only validate non-null and non-empty.

**Cross-module contract traps:**
- ConfigurationChangeListener fires **synchronously before** the config_changed event. This is the guaranteed-ordering path.
- CheckpointStore (event-bus) and ViewCheckpointStore (state-store) are **different interfaces** with different data types (long vs byte[]).
- Automation conditions MUST use positional state snapshots (getStatesAtPosition + ConsistentSnapshot per AMD-03), not current state reads.
- EventPublisher has exactly two methods: `publish(EventDraft, CausalContext)` and `publishRoot(EventDraft)`. Both are **synchronous and WAL-durable** (INV-ES-04). There is no async/best-effort path on EventPublisher. The `emit()` method does not exist.
- Core modules CANNOT import integration-runtime types. Cross-layer communication uses EVENTS, not direct type imports. Example: planned restart uses `integration_stopped(reason: planned_restart)` events, not direct method calls.

**GOTCHA: `EVENT_BUS_DOES_NOT_IMPORT_SQLITE_DRIVER` is NOT an ArchUnit rule — it does not exist anywhere in the codebase.** The M3 Plan §4.5 originally prescribed it as an ArchUnit rule, but implementation used JPMS module-info enforcement instead (compile-time, stronger than test-time ArchUnit). There are exactly 9 ArchUnit rules (7 original + 2 added in M3.6e.2), all in `HomeSynapseArchRules.java` in `homesynapse-app` test. The event-bus module has NO ArchUnit rules of its own. JDBC isolation for event-bus is a JPMS compile-time guarantee only. Do not reference this as an ArchUnit rule.

**GOTCHA: `NO_SYNCHRONIZED_METHODS` catches synchronized METHODS only, not synchronized blocks.** Synchronized blocks are bytecode-level (`monitorenter`/`monitorexit`) and invisible to ArchUnit's reflection-based analysis. Synchronized blocks are enforced by grep in the CI pipeline. The ArchUnit rule and the CI grep together cover the full LTD-11 "no synchronized" mandate.

---

## Key Invariants (Quick Reference)

| ID | Constraint |
|----|-----------|
| LTD-04 | ULID for all identity. BLOB(16) in SQLite, Crockford Base32 at API boundary. |
| LTD-08 | Jackson JSON for all serialization. |
| LTD-11 | No `synchronized`. Only ReentrantLock. Virtual thread compatibility. |
| LTD-19 | Event payload serialization: EventTypeRegistry + PersistenceJacksonModule + DegradedEvent fallback. Extends LTD-08. |
| LD#10 | All inter-module `requires` default to `requires transitive`. |
| DECIDE-04 | No ServiceLoader. Factories instantiated directly. |
| INV-CS-02 | EntityId is STABLE across hardware replacements. DeviceId is NOT. |
| INV-PD-07 | PersonId is the crypto-shredding boundary for privacy compliance. |
| INV-ES-02 | All observable state is derivable from the event log. |
| INV-ES-04 | Write-ahead persistence — events are durable before acknowledgment. |
| INV-RF-01 | Integration isolation — one adapter's failure cannot crash the core. |
| INV-PR-01 | Constrained hardware — all designs must work within Pi 4 (4 GB RAM). |
| INV-TO-02 | Deterministic automation execution (given same event sequence). |

For the full invariant definitions, read `Architecture_Invariants_v1.md` in project knowledge.

---

## Configuration Reload Contract

1. **Direct callbacks fire synchronously** — ConfigurationChangeListener for subsystems that must act before others see the change (Automation Engine uses this path).
2. **config_changed event published** — After all direct listeners complete.
3. **Event bus subscribers notified asynchronously** — Normal pull-based mechanism.

---

## Test Infrastructure (Current as of M1.9)

### Contract Tests (5 suites, 101 methods total)

| Suite | Methods | Module | testFixtures Package |
|---|---|---|---|
| EventStoreContractTest | 27 | event-model | `com.homesynapse.event.test` |
| CheckpointStoreContractTest | 9 | event-bus | `com.homesynapse.event.bus.test` |
| EventBusContractTest | 44 (10 @Nested tiers; Tiers 5–8 active M3.1, Tiers 9–10 @Disabled) | event-bus | `com.homesynapse.event.bus.test` |
| ViewCheckpointStoreContractTest | 10 | state-store | `com.homesynapse.state.test` |
| WriteCoordinatorContractTest | 11 (4 @Nested tiers) | persistence | `com.homesynapse.persistence` (same package as interface for package-private access) |

### In-Memory Implementations (passing all contract tests)

| Fixture | Module | Key Details |
|---|---|---|
| InMemoryEventStore | event-model testFixtures | ReentrantReadWriteLock, Clock-injected, implements EventPublisher + EventStore |
| InMemoryCheckpointStore | event-bus testFixtures | ConcurrentHashMap, reset() for isolation |
| InMemoryEventBus | event-bus testFixtures | Full filter evaluation, EventStore + CheckpointStore injection, subscribeWithHandler() callback bridge, ReentrantReadWriteLock |
| InMemoryViewCheckpointStore | state-store testFixtures | ConcurrentHashMap, Clock-injected, defensive byte[] copy |
| InMemoryWriteCoordinator | persistence testFixtures | ReentrantLock, volatile shutdown flag, synchronous execution on calling thread |

### Test Factories

| Factory | Module | Key Methods |
|---|---|---|
| TestEventFactory | event-model testFixtures | draft(), draftFor(), draftBuilder(), envelope(), envelopeBuilder(), subject(), deviceSubject(), etc. |
| TestCausalContext | event-model testFixtures | Helpers for CausalContext construction |
| StubIntegrationContext | integration-api testFixtures | defaults() factory producing valid IntegrationContext |
| TestAdapter | integration-api testFixtures | noop(), echo(), failing(), Builder |
| StubCommandHandler | integration-api testFixtures | accepting(), rejecting(), conditional() |
| InMemoryConfigAccess | configuration testFixtures | empty(), of(), builder() |
| TestConfigFactory | configuration testFixtures | minimalModel(), modelWithSection(), section() |
| TestDeviceFactory | device-model testFixtures | Device construction helpers |
| TestEntityFactory | device-model testFixtures | Entity construction helpers |
| TestCapabilityFactory | device-model testFixtures | Capability construction helpers |

### Cross-Cutting Test Support (`com.homesynapse.test`)

TestClock, SynchronousEventBus, EventCollector, TestSubscriber, NoRealIoExtension, @RealIo, GivenWhenThen, custom AssertJ assertions (EventEnvelopeAssert, CausalContextAssert, SubjectRefAssert, HomeSynapseAssertions).

### ArchUnit Rules (9 rules in homesynapse-app)

NO_SYNCHRONIZED_METHODS, NO_DIRECT_TIME_ACCESS, NO_SERVICE_LOADER, NO_REVERSE_DEPENDENCIES, NO_DIRECT_FILESYSTEM_IN_CORE, NO_INTERNAL_PACKAGE_ACCESS, NO_JSON_TYPE_INFO_IN_EVENTS, QUERY_SERVICE_READ_ONLY (M3.6e.2 — REST endpoints cannot access persistence directly), REST_ENDPOINTS_NO_EVENT_PUBLISHING (M3.6e.2 — REST endpoints cannot publish events via EventPublisher).

**JPMS-enforced constraint (not ArchUnit):** event-bus `module-info.java` does not `requires java.sql` — prevents event-bus from importing JDBC types at the module system level.

---

## M2 Persistence Layer — Completed

**All 9 sub-tasks completed (M2.1–M2.9).** Followed by M2-bridge structural hardening pass (AMD-34 through AMD-37 + Tier 2 Schema Reservations).

**Key deliverables:**
- SqliteEventStore (27/27 contract tests passing on real SQLite)
- SqliteCheckpointStore (9/9 contract tests)
- SqliteViewCheckpointStore (10/10 contract tests)
- PlatformThreadWriteCoordinator (11/11 contract tests, 5 WritePriority tiers)
- MigrationRunner (V001 + V002 applied, checksum-verified)
- EventTypeRegistry + PersistenceJacksonModule (LTD-19, DegradedEvent fallback)
- AtomicCheckpointWriter (same-transaction subscriber + view checkpoint)
- SqlitePersistenceLifecycle (capstone — start/publish/stop/restart cycle)

**M2-bridge schema hardening (AMD-34–37):**
- V001 expanded from 17 to 25 columns (home_id, idempotency_key, payload_size, batch_id, external_ref, intent_kind, logical_time, node_id + chain_hash NOT NULL)
- V002 subscriber_dead_letters table (DLQ, 11 columns, LOCAL-ONLY)
- EventDraft expanded from 8 to 9 fields (added idempotencyKey)
- SqliteEventStore: HomeId injection, 24-column INSERT, ZERO_HASH chain_hash binding
- Schema reservation pattern established

**Key M2 decisions (all locked):**
- Single-event transactions (batching deferred to measured optimization)
- Connection-per-thread model (1 write + 2-3 read connections)
- SqliteEventStore does NOT call EventBus.notifyEvent() — lifecycle coordinator wires this
- In-memory SQLite for contract tests, file-based for WAL/crash recovery tests

---

## M3 Event Distribution + State Materialization — COMPLETE (2026-05-27)

**7 sub-milestones completed (M3.1–M3.7).** Implemented the M2→M3 bridge Phase 2 interfaces (CheckpointPolicy, FixedCheckpointPolicy, ProjectionAdvancer, AdvanceResult, DeploymentProfile, PersistenceConfig, RetentionPolicy, MaintenanceSubscriber, MaintenanceResult) as production code with full contract test coverage. Nineteen Claude Code work units total.

**Architectural inputs locked by the M2→M3 bridge:**
- AMD-38 APPLIED: FixedCheckpointPolicy.HOME_DEFAULT = (200 events, 2 s, 1 s min interval). The 2 s `maxInterval` is the load-bearing safety mechanism — forces the projection's read transaction to close on a known cadence so wal_checkpoint can advance.
- AMD-39 WITHDRAWN: journal_size_limit stays at LTD-03's 6 MB across all profiles. Bounded-window reader pattern alone keeps the WAL at ~4 MB peak under nominal load.
- AMD-40 APPLIED: MaintenanceSubscriber runs on the writer executor, interval-based (DEFAULT 6 h), bounded purge chunks (DEFAULT_PURGE_BATCH_SIZE = 1,000), ≤ 2 s lock-hold per chunk.

**Phase 3 deliverables (all shipped):**
- Production `InProcessEventBus` with REPLAY→LIVE transition (AMD-02), backpressure/coalescing (SubscriptionFilter.coalesceExempt), platform-thread subscriber dispatch (AMD-26/AMD-29)
- Production `DispatchingProjectionAdvancer` (M4.0b-1, REC-28 — package-private in state-store, constructor-injected `EnvelopeHandler` map, forward-all bounded-window via `EventStore.readFrom()`) reached via `ProjectionAdvancer.dispatching(EventStore)`. (The M3.7 interim `MinimalProjectionAdvancer` was deleted in M4.0b-1.)
- Production `ProductionDerivationRule` (M4.0b-1 — package-private in state-store, string change-detect, publishes derived `state_changed` on LIVE) via `DerivationRule.production()`, plus the AMD-50 version-transition reconciliation backfill (M4.0b-2 — `projectionVersion` 1→2, `backfillActive` gate, non-emitting one-shot backfill, supersession, `Clock` removed from `DerivationContext`)
- Production `FixedCheckpointPolicy` consumer wiring into the projection loop, plus `TESTING` constant (1 event / 100ms) for test determinism
- Production `StateProjection` building EntityState from the event stream
- Production `MaterializedStateQueryService` (M3.6e.1) exposing current state queries; positional snapshots (AMD-03) deferred
- `HomeSynapseCore` composition root with 16-step bootstrap, `abandon()` contract for crash-recovery testing, `HomeSynapseConfig` with operator-configurable checkpoint policy
- Full E2E integration test suite (M3.7): `HomeSynapseE2eHarness`, `CrashRecoveryHttpIT`, `EndpointE2eIT`, `InFlightRequestShutdownIT`

**Validation reference:** D1 WAL Pathology Validation Spike (2026-05-15). Reproduces continuous-reader pathology and validates bounded-window reader as the load-bearing mitigation. Results captured in AMD-38 and AMD-39 Validation Gate sections.

**Projection-checkpoint wiring WU** completed 2026-05-19. New public interface StateCheckpointSource (2 methods + stub() factory) in state-store. StateProjection wired to call source.serializeCheckpoint(projectionVersion) and source.loadedProjectionVersion(). Advisory 10 MB checkpoint size guardrail. State-store type count: 19→20. Total test suite: ~1,365+.

---

## Phase 3 Watch Items

Two cross-amendment interaction points identified during the M0 amendment traceability audit. These require careful attention during implementation:

**S5-CF1: Snapshot freshness during duration timer expiry.** When an AMD-25 temporal duration timer fires, the automation engine must re-evaluate conditions against a **fresh** state snapshot (via `getStatesAtPosition` per AMD-03), not the stale snapshot from when the timer was started. A timer that was valid when set may fire after the triggering condition has been resolved.

**S5-CF2: Orphan transition timing.** When AMD-17 orphan transition occurs (integration removed, entities orphaned), the orphan's `Availability` must be set to `STALE` **immediately** upon transition — not deferred until AMD-11's 30-second periodic scan cycle. The scan cycle handles natural staleness; orphan transition is an explicit lifecycle event with immediate effect.

---

## Hardware Environment

**Dev Pi 5 (`hs-dev-1`):** Raspberry Pi 5 with Kioxia BG4 256GB 2230 NVMe. Connected to dev machine via Tailscale. Accessible via `ssh pi`. Username: `homesynapse`. Target setup: Amazon Corretto 21 via apt, systemd service unit with `MemoryMax=2G`/`MemoryHigh=1536M`, NVMe mounted at `/var/lib/homesynapse` with `noatime`, ext4 with label `homesynapse-data`.

**Dev machine:** Windows (Git Bash / MINGW64). GitHub credential manager account: `nixmith`. Both repos use HTTPS remotes.

---

---

**Last verified against:** `homesynapse-core` **`7f44bed` (M5-A COMPLETE + M5-B/B1 DONE)** on 2026-06-07. M4 + M5-A shipped; **Doc 15 Cryptographic Architecture LOCKED**; AMD-86 + AMD-87 RATIFIED, watermark **AMD-87**; `projectionVersion` 5; AMD-87 Expectation codec IMPLEMENTED (M9 prereq cleared); **135 invariants across 34 categories**. Next: **M6 (Configuration + secrets/crypto)**.
