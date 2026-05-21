<!--
file: project-knowledge/HomeSynapse_Knowledge_Primer.md
purpose: Compressed architectural mental model of HomeSynapse Core (modules, types, gotchas).
audience: All
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# HomeSynapse Core — Knowledge Primer

Compressed architectural context for the HomeSynapse Core Claude project. This file provides the "mental model" — what each module does, how they connect, where types actually live, and the gotchas that cause mistakes. For full type inventories, read the MODULE_CONTEXT.md files (paths in the Navigation Index).

---

## Architecture in Brief

HomeSynapse Core is a local-first, event-sourced smart home runtime. Java 21 on Amazon Corretto, targeting Raspberry Pi 4/5 with 4 GB RAM. Multi-module Gradle project with JPMS enforcement. All state is derived by replaying immutable events from an append-only SQLite store (WAL mode). Virtual threads for concurrency; no `synchronized` anywhere (ReentrantLock only). No cloud dependency; no external message broker.

The source repo (`homesynapse-core`) contains the code. The companion repo (`homesynapse-core-docs`) contains design documents, governance, and research. Phase 2 (public API contracts — interfaces, records, enums, sealed hierarchies) is complete across all 19 modules (~330+ public Java types). All Phase 3 Conditional GO criteria are satisfied.

**M0 (Prerequisites & Cleanup) completed 2026-04-04.** All CRITICAL/HIGH/MEDIUM audit findings resolved. AMD-31 (command execution order guarantees) created and applied. Traceability indexes populated for Docs 02–11 (161+ type-to-design-doc mappings). MODULE_CONTEXT files updated across 7 modules. Automation critical review fully categorized (28 issues → 4 already addressed, 2 became AMD-31, 16 Phase 3 notes, 10 Tier 2 deferrals).

**M1 (Contract Tests & In-Memory Implementations) completed 2026-04-09.** 9 sub-tasks (M1.1–M1.9) producing 102 contract/fixture test methods across 5 abstract contract test suites. Every interface that will have a production SQLite implementation now has a proven behavioral contract. All MODULE_CONTEXT files updated post-M1 to reflect test infrastructure. Total test suite: ~1,150+ @Test methods (as of M2-bridge completion). Full build: GREEN.

**M2 (Persistence Layer) completed 2026-05-01.** 9 sub-tasks (M2.1–M2.9) producing MigrationRunner, DatabaseExecutor, PlatformThreadWriteCoordinator, ReadExecutor, SqliteEventStore (24-bind INSERT, 25-column V001 schema), AtomicCheckpointWriter, SqlitePersistenceLifecycle. Total test suite: ~1,150+ @Test methods across ~584 Java files. Full build: GREEN.

**M2-bridge (Structural Hardening) completed 2026-05-02.** AMD-34 through AMD-37 applied. V001 schema expanded from 17 to 25 columns (home_id, idempotency_key, payload_size, batch_id, external_ref, intent_kind, logical_time, node_id, chain_hash tightened to NOT NULL). V002 migration added (subscriber_dead_letters table, 11 columns, LOCAL-ONLY). EventDraft expanded from 8 to 9 fields (added idempotencyKey, AMD-35). SqliteEventStore: HomeId injection as 5th constructor param, 24-bind INSERT, ZERO_HASH for chain_hash. Schema reservation pattern established: columns exist in SQLite, populated at INSERT, invisible to Java API until feature ships.

**M2→M3 Bridge (Phase 2 Interface Specifications) completed 2026-05-15.** Three amendments finalized: AMD-38 APPLIED (checkpoint policy: 200 events / 2 s, driven by D1 WAL pathology spike), AMD-39 WITHDRAWN (journal_size_limit stays at LTD-03's 6 MB — bounded-window reader alone prevents WAL growth), AMD-40 APPLIED (retention execution on writer executor, interval-based, bounded chunks). V003 migration ready (snapshots table + redundant idx_events_subject dropped). Ten Phase 2 interfaces added: CheckpointPolicy sealed hierarchy, ProjectionAdvancer, AdvanceResult (state-store); DeploymentProfile, PersistenceConfig, RetentionPolicy, MaintenanceSubscriber, MaintenanceResult (persistence). D1 WAL Pathology Validation Spike empirically confirmed that a continuous reader causes WAL growth to 20.6 MB at 5 events/s; bounded-window reader (close/reopen every 500 rows) keeps WAL at ~4 MB. Write amplification: ~34 KB WAL per ~600 B event (50×) due to 7 indexes.

**M3.1 (InProcessEventBus Core) completed 2026-05-16.** Production InProcessEventBus with 14 types (9 public + 5 package-private — see event-bus MODULE_CONTEXT for full inventory). Full subscriber lifecycle: Subscriber interface, SubscriberMode FSM, SubscriberSupervisor (backoff, circuit breaker), SubscriberDlq, ReplayWindowQueue, SubscriberRuntime. EventBusContractTest expanded from 18 to 44 methods (Tiers 1–8 active, Tiers 9–10 @Disabled). AMD-41/42/43 applied (state projection execution model, subscriber lifecycle/isolation, backpressure/observability). Architecture Invariants expanded to 94 (§19: BUS, PROJ, WRITER, SUB-ISO). Total test suite: ~1,200+ @Test methods across ~600+ Java files. Full build: GREEN.

**M3 (Event Distribution + State Materialization) is the current milestone.** M3.1 complete; M3.2 (REPLAY→TRANSITION→LIVE, bus-side) is next. 7 sub-milestones total (M3.1–M3.7). Produces REPLAY→LIVE transition, backpressure/coalescing, StateProjection, StateQueryService implementation, and end-to-end integration tests.

Phase 3 implementation follows a **contract-test-first approach** — M1 built all contract test suites and in-memory implementations before any production code ships (M2+). InMemoryEventStore (27/27 contract tests passing) was the first implementation target (2026-03-27) and serves as the model for all subsequent contract test suites.

---

## Module Map

Modules listed in dependency order. Each module has one flat Java package under `com.homesynapse.*`. MODULE_CONTEXT.md files have enriched first lines with package, type count, and architectural role for quick identification.

### platform-api — `com.homesynapse.platform` + `com.homesynapse.platform.identity`
Dependency root. Zero project dependencies. Typed ULID identity system (8 wrappers: DeviceId, EntityId, IntegrationId, AreaId, AutomationId, PersonId, HomeId, SystemId). The Ulid value type and UlidFactory are separate from the typed wrappers. Platform abstraction interfaces (PlatformPaths, HealthReporter).

### event-model — `com.homesynapse.event`
Most important module. Universal event vocabulary. EventEnvelope (the immutable event wrapper, 14 fields), EventPublisher (sole write path), EventStore (read-side query), EventDraft (pre-publish builder, 9 fields including idempotencyKey added in M2-bridge AMD-35), all domain event payload records, the HomeSynapseException hierarchy, and EventTypes constants. Everything in the system either produces or consumes events defined here.

### event-bus — `com.homesynapse.event.bus`
Pull-based, notification-driven event distribution. 33 production types (19 public + 14 package-private) after M3.6d-a — three types (QueueSaturationHealthCheck, HealthSignal, HealthLevel) promoted to public alongside the M3.6b InProcessEventBus promotion. See MODULE_CONTEXT for full inventory. Key public types: EventBus (8 methods including subscribeRuntime/resume/subscribers), Subscriber, SubscriberInfo, SubscriptionFilter, CheckpointStore, SubscriberMode (5-value FSM), SubscriberSnapshot, SubscriberReadConnectionFactory, SubscriberReadExecutor, EventBusConfig (M3.6b — 2-field record for operator-tunable bus parameters), InProcessEventBus (public as of M3.6b, DEC-M3-16 — canonical 7-arg constructor accepting EventBusConfig; `PUBLISHER_BLOCKED_DEPTH_THRESHOLD` is now an instance field from config, not a static constant), QueueSaturationHealthCheck + HealthSignal + HealthLevel (M3.6d-a, DEC-M3-17 — the 3-type chain is the minimum viable promotion because the constructor's `Consumer<HealthSignal>` parameter would trigger `-Xlint:exports` otherwise). Bus notifies via LockSupport.unpark(); subscribers pull from EventStore. Never pushes EventEnvelopes directly. ReplayWindowQueue capacity is parameterized (default 10,000 via no-arg constructor; custom via `ReplayWindowQueue(int maxCapacity)` — M3.6b).

### device-model — `com.homesynapse.device` + subpackages
Physical and logical device model. Entity (not Device) is the atomic addressable unit — a single physical device may produce multiple entities. Sealed Capability hierarchy, sealed AttributeValue hierarchy. Service interfaces for registries, validation, and discovery pipeline.

### state-store — `com.homesynapse.state`
Materialized view over the event stream. EntityState projects current state from events. StateProjection subscribes with coalesceExempt=true (must see every event). Availability enum lives here. ViewCheckpointStore (different from event-bus CheckpointStore). **The staleAfter + Clock staleness model is HomeSynapse's #1 architectural differentiator — proven at the data level by EntityStateTest (12 methods, M1.9).** M3.6d-a added the `ReadinessSource` public interface (single method `mode() → SubscriberMode`) consumed by M3.6e's MaterializedStateQueryService for REST/WebSocket readiness gating. Total post-M3.6d-a: 20 public types + 1 package-private (`SelfProducedFilter`) = 21 production types.

M2→M3 bridge added 5 types: CheckpointPolicy (sealed interface: shouldCheckpoint(events, elapsed, readerLag)), FixedCheckpointPolicy (HOME_DEFAULT: 200 events / 2 s per AMD-38), AdaptiveCheckpointPolicy (reserved for post-MVP pressure-aware mode), ProjectionAdvancer (interface: advance(fromPosition, maxRows) → AdvanceResult, ≤500 rows, ≤2 s read transaction, bounded-window contract), AdvanceResult (record).

### persistence — `com.homesynapse.persistence`
SQLite storage. Two databases: main (events, state) and telemetry. TelemetryWriter uses a ring buffer per RetentionTier. WriteCoordinator (AMD-06/AMD-32, package-private) serializes all writes with priority ordering. WritePriority (package-private, 5 levels: EVENT_PUBLISH → STATE_PROJECTION → WAL_CHECKPOINT → RETENTION → BACKUP). WAL mode is always on. **LTD-19 governs event payload serialization: EventTypeRegistry + PersistenceJacksonModule + DegradedEvent fallback.** V001 events table has 25 columns including schema reservations for multi-home (home_id, AMD-34), persistent idempotency (idempotency_key, AMD-35), tamper-evidence (chain_hash NOT NULL with zero-vector default, AMD-37), and 6 Tier 2 reservation columns (payload_size, batch_id, external_ref, intent_kind, logical_time, node_id). V002 adds subscriber_dead_letters table for poison event parking (AMD-36, LOCAL-ONLY sync scope). SqliteEventStore constructor takes HomeId as 5th parameter (AMD-34). Schema reservation pattern: reserved columns populated at INSERT time, not exposed on EventEnvelope until their features ship.

M2→M3 bridge added 5 public types: DeploymentProfile (enum: STUDIO/HOME/PERFORMANCE with per-profile PRAGMA values; 6 fields — 3 original + 3 added in M3.6a: busyTimeoutMs, lockingMode, readThreadCount), PersistenceConfig (bundles profile + retention), RetentionPolicy (per-priority retention durations, SOURCE_DEFAULT from EventPriority Javadoc: 7d/90d/365d), MaintenanceSubscriber (interface: writer-executor-only, interval-based, bounded chunks per AMD-40), MaintenanceResult (record). V003 migration adds snapshots table and drops redundant idx_events_subject. M3.6a added package-private `LockingMode` enum (NORMAL, EXCLUSIVE). `DatabaseExecutor` constructor now accepts `DeploymentProfile profile` instead of `int readThreadCount`; hardcoded `CONNECTION_PRAGMAS` list replaced by `connectionPragmas(DeploymentProfile)` rendering method. `SqlitePersistenceLifecycle` constructor now accepts `PersistenceConfig config` instead of `int readThreadCount`. M3.6d-a: `SqliteStateStore` now `implements StateCheckpointSource` (method renamed `serialize(int)` → `serializeCheckpoint(int)`; both `serializeCheckpoint` and `loadedProjectionVersion()` promoted to public via the interface). Class itself remains package-private; only the two interface methods are exposed to external consumers — they reach the instance through the `StateCheckpointSource` interface type.

### automation — `com.homesynapse.automation` + subpackages
Rule engine. Trigger → Condition → Action pipeline. Has 4 sealed hierarchies (Selector, TriggerDefinition, ConditionDefinition, ActionDefinition) — the highest concentration of any module. Conditions evaluate against positional state snapshots (AMD-03). Cascade depth limiting (AMD-04). Command execution ordering (AMD-31).

### configuration — `com.homesynapse.config`
YAML 1.2 config loading, JSON Schema validation, AES-256-GCM encrypted secrets. ConfigModel is Map-based in Phase 2 (typed config objects are Phase 3+). ConfigurationChangeListener fires synchronously before the config_changed domain event is published.

### integration-api — `com.homesynapse.integration`
The one module every protocol adapter depends on. Re-exports all core modules via `requires transitive`. Defines IntegrationFactory, IntegrationAdapter, IntegrationContext (large dependency injection record), CommandHandler. DECIDE-04: direct factory construction, no ServiceLoader.

### integration-runtime — `com.homesynapse.integration.runtime`
OTP-style one-for-one supervisor. Manages adapter lifecycle, health monitoring, restart with backoff. ExceptionClassification (TRANSIENT/PERMANENT/SHUTDOWN_SIGNAL) drives retry decisions. Kahn's algorithm for startup ordering (AMD-14).

### integration-zigbee — `com.homesynapse.integration.zigbee` + subpackages
Zigbee 3.0 coordinator adapter. First and only MVP protocol adapter. IEEEAddress is a raw 64-bit long (NOT a ULID). Sealed ZigbeeFrame and ManufacturerCodec hierarchies. CoordinatorTransport (not thread-safe) vs CoordinatorProtocol (thread-safe). Route health monitoring (AMD-07).

### rest-api — `com.homesynapse.api.rest` + subpackages
HTTP command interface. RFC 9457 problem types. 4-phase command lifecycle (ISSUED → DISPATCHED → EXECUTING → result). Idempotency keys (AMD-08). Unique: zero `requires` directives in Phase 2 (implementation will add them). ApiRequest.body is Object, not JsonNode.

### websocket-api — `com.homesynapse.api.websocket`
Real-time event streaming. WsMessage sealed hierarchy. Three-stage backpressure: NORMAL → BATCHED → COALESCED. Commands are NOT accepted over WebSocket (read-only). WebSocket does NOT produce domain events.

### observability — `com.homesynapse.observability`
Health model (HealthStatus, HealthTier, LifecycleState), trace model, metrics, log control, JFR integration. HealthTier provides hierarchical aggregation (entity → integration → subsystem → system). Local-first tracing, not OpenTelemetry.

### lifecycle — `com.homesynapse.lifecycle`
Process-level lifecycle orchestration. After M3.6d-a: 7 public + 2 package-private types. Phase 2 types (LifecyclePhase enum, SubsystemStatus enum, LifecycleEventType utility class, SubsystemState record, SystemHealthSnapshot record, SystemLifecycleManager interface) coexist with M3.6 composition-root primitives added by M3.6d-a: `HomeSynapseConfig` (public record, 2 fields `PersistenceConfig persistence` + `EventBusConfig eventBus`, `HOME_DEFAULT` constant), `SharedScheduler` (package-private final, 50 ms refill + 1 s tick, daemon thread `hs-sched-0`, `safelyInvoke` cadence defence against task-fault silencing), `ThrowingStateQueryService` (package-private final, all 5 methods throw `IllegalStateException("StateQueryService not yet wired — available after M3.6e")`). M3.6d-b will add the `HomeSynapseCore` facade. Module-info gained `requires transitive` for persistence, event.bus, state-store plus a non-transitive `requires org.slf4j` for SharedScheduler's internal logging (canonical M2.2 pattern from `core/persistence`). 10-phase sequential startup, no backward transitions. Fatal vs non-fatal subsystem classification. 30-second shutdown budget.

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

---

## Critical Gotchas

These are the specific mistakes that AI agents commonly make on this codebase. Each one has caused incorrect code or analysis in past sessions.

**M3.6a/M3.6b corrections (2026-05-20):**
- DeploymentProfile has **6 fields**, not 3. M3.6a added `busyTimeoutMs`, `lockingMode`, `readThreadCount`.
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
- IntegrationContext has **10 fields**. It's a large DI record.
- IntegrationHealthRecord has **13 fields** including a weighted `healthScore` and `plannedRestart` (boolean, added 2026-03-21 by architecture benchmark).

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
- rest-api has **zero requires directives** in Phase 2 (unique). Implementation will add them.
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

**GOTCHA: `EVENT_BUS_DOES_NOT_IMPORT_SQLITE_DRIVER` is NOT an ArchUnit rule — it does not exist anywhere in the codebase.** The M3 Plan §4.5 originally prescribed it as an ArchUnit rule, but implementation used JPMS module-info enforcement instead (compile-time, stronger than test-time ArchUnit). There are exactly 7 ArchUnit rules, all in `HomeSynapseArchRules.java` in `homesynapse-app` test. The event-bus module has NO ArchUnit rules of its own. JDBC isolation for event-bus is a JPMS compile-time guarantee only. Do not reference this as an ArchUnit rule.

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

### ArchUnit Rules (7 rules in homesynapse-app)

NO_SYNCHRONIZED_METHODS, NO_DIRECT_TIME_ACCESS, NO_SERVICE_LOADER, NO_REVERSE_DEPENDENCIES, NO_DIRECT_FILESYSTEM_IN_CORE, NO_INTERNAL_PACKAGE_ACCESS, NO_JSON_TYPE_INFO_IN_EVENTS.

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

## M3 Event Distribution + State Materialization — Current

**7 sub-milestones planned (M3.1–M3.7).** Implements the M2→M3 bridge Phase 2 interfaces (CheckpointPolicy, FixedCheckpointPolicy, ProjectionAdvancer, AdvanceResult, DeploymentProfile, PersistenceConfig, RetentionPolicy, MaintenanceSubscriber, MaintenanceResult) as production code with full contract test coverage.

**Architectural inputs locked by the M2→M3 bridge:**
- AMD-38 APPLIED: FixedCheckpointPolicy.HOME_DEFAULT = (200 events, 2 s, 1 s min interval). The 2 s `maxInterval` is the load-bearing safety mechanism — forces the projection's read transaction to close on a known cadence so wal_checkpoint can advance.
- AMD-39 WITHDRAWN: journal_size_limit stays at LTD-03's 6 MB across all profiles. Bounded-window reader pattern alone keeps the WAL at ~4 MB peak under nominal load.
- AMD-40 APPLIED: MaintenanceSubscriber runs on the writer executor, interval-based (DEFAULT 6 h), bounded purge chunks (DEFAULT_PURGE_BATCH_SIZE = 1,000), ≤ 2 s lock-hold per chunk.

**Expected Phase 3 deliverables:**
- Production `InProcessEventBus` with REPLAY→LIVE transition (AMD-02), backpressure/coalescing (SubscriptionFilter.coalesceExempt), platform-thread subscriber dispatch (AMD-26/AMD-29)
- Production `ProjectionAdvancer` implementation enforcing the bounded-window contract (close/reopen read transaction every 500 rows, ≤ 2 s duration)
- Production `FixedCheckpointPolicy` consumer wiring into the projection loop
- Production `StateProjection` building EntityState from the event stream
- Production `StateQueryService` exposing positional snapshots (AMD-03) and current state queries
- Optional `ActiveCheckpointService` issuing wal_checkpoint(PASSIVE) at AMD-38's cadence (defense-in-depth; D1 demonstrated this is redundant under nominal load but cheap and protective under degraded conditions)
- End-to-end integration tests covering crash recovery, REPLAY→LIVE handoff, and the WAL bounded-growth property

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
