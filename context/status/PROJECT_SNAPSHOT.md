<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-05-22 against commit dfb045e
-->

# Project Snapshot

**Last updated:** 2026-05-22 by PM (WUCP Phase 2 — M3.6d-b closure)
**Latest commit:** `dfb045e` on `main` (M3.6d-b)
**Current phase:** P3 — Implementation (test-first).
**Days remaining:** 188
**Launch target:** November 25, 2026

---

## Current Work Unit

M3.6a + M3.6b + M3.6c + M3.6d-a + M3.6d-b COMPLETE. WUCP Phase 2 closeout COMPLETE for all five. Next: M3.6e.1 coding instruction (StateQueryService + REST gate — M3.6 capstone first half).

---

## Design Documents

All 14 design documents are Locked (Phase 1 — System Design Documentation is complete).

| # | Document | Status |
|---|----------|--------|
| 01 | Event Model & Event Bus | Locked |
| 02 | Device Model & Capability System | Locked |
| 03 | State Store & State Projection | Locked |
| 04 | Persistence Layer | Locked |
| 05 | Integration Runtime | Locked |
| 06 | Configuration System | Locked |
| 07 | Automation Engine | Locked + AMD-25 integrated (2026-03-18) |
| 08 | Zigbee Adapter | Locked |
| 09 | REST API | Locked |
| 10 | WebSocket API | Locked |
| 11 | Observability & Debugging | Locked |
| 12 | Startup, Lifecycle & Shutdown | Locked |
| 13 | Web UI (Observability MVP) | Locked |
| 14 | Master Architecture Document | Locked |

## Committed M3 Design Artifacts (informational)

| Artifact | Path | Date | Notes |
|---|---|---|---|
| Cross-tier deployment audit | `nexsys-hivemind/context/audits/2026-05-19_cross-tier-deployment-audit.md` | 2026-05-19 | Closed-out audit of cross-tier deployment surface. Informed M3.6 composition root design. |
| M3 audit gap-closure research (Artifact 1) | `homesynapse-core-docs/research/2026-05-20_M3_Audit_Gap_Closure_v1.md` | 2026-05-20 | Identified and closed audit-trail gaps prior to M3.4b/M3.6. |
| M3.6 Composition Root Design | `homesynapse-core-docs/design/2026-05-20_M3.6_Composition_Root_Design.md` | 2026-05-20 | Authoritative composition-root design that M3.6 implements against. |

## Interface Specifications (Phase 2 — FROZEN)

Phase 2 completed 2026-03-20 with all 16 JPMS-compiled subsystem modules specified (plus 3 scaffold modules — platform-systemd, test-support, dashboard — that have MODULE_CONTEXT.md placeholders but no compiled Java yet). See `context/planning/phase-2-block-backlog.md` for the frozen historical record of Blocks A–S. Summary at Phase 2 close: 16 modules specified, ~402 production Java files, all module-info.java files compile clean with `-Xlint:all -Werror`. AMD-33 subsequently (2026-04-10) ratified DomainEvent as permanently non-sealed.

## M3 Governance (committed 2026-05-16)

| Amendment | Status | Scope |
|---|---|---|
| AMD-41 | APPLIED | State Projection Execution Model |
| AMD-42 | APPLIED | Subscriber Lifecycle and Isolation |
| AMD-43 | APPLIED | Backpressure and Observability |

13 new invariants: INV-BUS-01..03, INV-PROJ-01/04/NEW-01, INV-WRITER-01, INV-SUB-ISO-01..06. DEC-M3-01 through DEC-M3-17 locked (DEC-M3-14/15 added 2026-05-17; DEC-M3-16 added 2026-05-20 — composition-root visibility strategy; DEC-M3-17 added 2026-05-20 — HealthSignal + HealthLevel transitive visibility promotion alongside QueueSaturationHealthCheck, DEC-M3-16 addendum). PLAN-M3-CONSOLIDATED-02 committed as the M3 implementation authority.

## Phase 3 Implementation Status

Phase 3 began after Phase 2 closeout on 2026-03-20. Progress:

| Milestone / WU | Status | Date | Notes |
|---|---|---|---|
| M0 | COMPLETE | 2026-04-04 | AMD-31, traceability, MODULE_CONTEXTs |
| M1 | COMPLETE | ~2026-04-08 | Contract tests + in-memory implementations |
| M2 | COMPLETE | 2026-05-01 | Full persistence layer |
| M2-bridge | COMPLETE | 2026-05-02 | AMD-34–37, structural hardening |
| M3.1 | COMPLETE | 2026-05-17 | InProcessEventBus core (14 types) |
| M3.2 | COMPLETE | 2026-05-17 | REPLAY→TRANSITION→LIVE bus-side (16 types) — `0bade6a` |
| M3.3 | COMPLETE | 2026-05-17 | Backpressure, metrics, observability (29 types) — `a5d4b2a` |
| M3.5a | COMPLETE | 2026-05-18 | StateProjection vertical slice — `a2aff9c` |
| Bus-Fix Piece A | COMPLETE | 2026-05-18 | `DerivedWriteRateLimit` visibility promotion — `fceafe8` |
| M3.5b | COMPLETE | 2026-05-18 | StateProjection production persistence — `08d0136` |
| Projection-checkpoint wiring | COMPLETE | 2026-05-19 | `StateCheckpointSource` + 10 MB advisory guardrail — `56aaa4b` |
| Supervisor DLQ wiring | COMPLETE | 2026-05-19 | `SubscriberSupervisor` constructs `DeadLetter` — `ed5862c` |
| M3.4a | COMPLETE | 2026-05-19 | Integration-tests module + harness + BurstLoadIT + HeapBudgetIT — `5ae7912` |
| M3.4b | COMPLETE | 2026-05-19 | Sustained-load + crash-recovery IT tests — `adf04d2` |
| M3.6a | COMPLETE | 2026-05-20 | Profile-driven persistence config — DeploymentProfile 6 fields, LockingMode enum, profile-driven PRAGMAs — `17c40b6` |
| M3.6b | COMPLETE | 2026-05-20 | EventBusConfig record, InProcessEventBus public (DEC-M3-16), ReplayWindowQueue parameterized — `df2743a` |
| M3.6c | COMPLETE | 2026-05-20 | Per-module event-class manifests (Q3 gap closure) — `38d3e30` |
| M3.6d-a | COMPLETE | 2026-05-20 | Composition-root satellite changes — SqliteStateStore→StateCheckpointSource, QueueSaturationHealthCheck+HealthSignal+HealthLevel public (DEC-M3-17), ReadinessSource, ReconciliationTest 4/5, Tier 9 un-disabled, HomeSynapseConfig + SharedScheduler + ThrowingStateQueryService skeletons, SLF4J wiring — `25bc23b` |
| M3.6d-b | COMPLETE | 2026-05-21 | PersistenceFactory + HomeSynapseCore composition-root wiring — 4-commit cohort: WriteCoordinator.queueSize() (`a33ee40`), production SubscriberReadConnectionFactory (`a59b64e`), PersistenceFactory public gateway (`725353d`), HomeSynapseCore facade (`dfb045e`). OR-M3-14 prerequisites bundled. — `dfb045e` |
| M3.6e.1 | PLANNED | — | StateQueryService + REST gate (M3.6 capstone) |
| M3.6e.2 | PLANNED | — | Admin endpoints + ArchUnit rules |
| M3.7 | PLANNED | — | End-to-end integration tests |

## Code State

- **Repository:** homesynapse-core, **20 Gradle modules** (16 JPMS-compiled production modules + 3 scaffold-only: platform-systemd, test-support, dashboard + 1: `testing/integration-tests` for on-device IT tests, classpath-only test code).
- **Production Java files:** ~700+ across the JPMS-compiled production modules (post-M3.6d-b addition of `PersistenceFactory`, `SqliteSubscriberReadConnectionFactory`, `SqliteSubscriberReadExecutor`, `HomeSynapseCore` + `WriteCoordinator.queueSize()` + `SqlitePersistenceLifecycle` 6-store expansion). Test files: **~1,550+ @Test methods** across ~155+ test files and ~35+ testFixtures files (M3.6d-b added: PersistenceFactoryTest, SqliteSubscriberReadConnectionFactoryTest, HomeSynapseCoreTest, WriteCoordinatorContractTest queueSize tests).
- **Event-bus module (post-M3.6d-a):** 19 public + 14 package-private = 33 top-level types. M3.6d-a promoted `QueueSaturationHealthCheck`, `HealthSignal`, `HealthLevel` to public (DEC-M3-17 — transitive 3-type chain because the public constructor's `Consumer<HealthSignal>` parameter would have triggered `-Xlint:exports` otherwise). M3.6b added `EventBusConfig` (public record, 2 fields: `replayQueueCapacity`, `publisherBlockedDepthThreshold`; `HOME_DEFAULT` constant). `InProcessEventBus` promoted to `public` (DEC-M3-16); new canonical 7-arg constructor accepting `EventBusConfig`. `PUBLISHER_BLOCKED_DEPTH_THRESHOLD` replaced by instance field from config. `ReplayWindowQueue` capacity parameterized (default 10,000 via no-arg; custom via `ReplayWindowQueue(int)`). `InProcessEventBusFactory` gained `createWithConfig(...)`. `EventBus` interface has 8 methods (4 abstract Phase 2, 4 default M3.1). `BusMetrics` interface (7 canonical metric names) with `BusMetricsJfr` JFR-native implementation.
- **Persistence module (post-M3.6d-b):** 48 types (was 45). M3.6d-b added `PersistenceFactory` (public final class — static `start()` factory, 8 store/infrastructure accessors returning public interface types, `AutoCloseable`), `SqliteSubscriberReadConnectionFactory` (package-private — production impl of `SubscriberReadConnectionFactory`, creates per-subscriber dedicated platform-thread executor + SQLite read connection; INV-SUB-ISO-02), `SqliteSubscriberReadExecutor` (package-private — per-subscriber read executor backed by a single platform thread and dedicated `Connection`; close() shuts down executor and connection). `WriteCoordinator` interface gained `int queueSize()` (DEC-M3-14); `PlatformThreadWriteCoordinator` implements it by exposing the bounded executor's queue size. `SqlitePersistenceLifecycle` expanded from 4-store to 6-store construction: now also constructs `SqliteStateStore` + `SqliteDeadLetterStore` during `start()`, with a separate `Include.ALWAYS`-configured `ObjectMapper` for `CheckpointSerializer` (distinct from the `NON_NULL` `PersistenceObjectMapper.create()` used for event payloads). New accessors: `stateStore()`, `deadLetterStore()`, `subscriberReadConnectionFactory()`. Module-info gained no new directives (all dependencies already present from M3.6d-a). `SqliteStateStore` now `implements StateCheckpointSource` (method renamed `serialize(int)` → `serializeCheckpoint(int)`, both `serializeCheckpoint` and `loadedProjectionVersion()` promoted to public via interface; class itself remains package-private — only the two interface methods are externally visible). M3.5b added `SqliteStateStore` (ConcurrentHashMap-backed materialized view + checkpoint-driven recovery), `SqliteDeadLetterStore` (UPSERT on (subscriber_id, event_position)), `CheckpointSerializer`, `CheckpointData`, `AtomicCheckpointWriter.writeAtomicCheckpointWithDlqPark()` (three-way atomic write — subscriber checkpoint + view checkpoint + DLQ park), V004 DLQ operational indices migration. Two ObjectMapper configurations coexist: `PersistenceObjectMapper.create()` returns `NON_NULL` for event payloads; checkpoint serialization requires `ALWAYS` and is constructed at composition time (composition-root wiring lands in M3.6d-b).
- **State-store module (post-M3.6d-a):** 20 public + 1 package-private types (added `ReadinessSource` public interface — single method `mode() → SubscriberMode`, consumed by M3.6e's MaterializedStateQueryService for REST/WebSocket readiness gating). Projection-checkpoint wiring's `StateCheckpointSource` interface in scope; `StateProjection` calls `source.serializeCheckpoint(projectionVersion)`. Advisory 10 MB checkpoint-size guardrail enforced.
- **Lifecycle module (post-M3.6d-b):** 8 public + 2 package-private types (was 7+2). M3.6d-b added `HomeSynapseCore` (public final class — composition root, implements `ReadinessSource`; 4-arg constructor accepting `Path dbPath, HomeSynapseConfig, Clock, HomeId`; `start()` returns `CompletableFuture<Void>`, `stop()` idempotent reverse-order teardown; 12-step bootstrap sequence wiring PersistenceFactory → BusMetrics → InProcessEventBus → StateProjection → SharedScheduler; exposes `eventPublisher()`, `eventStore()`, `eventBus()`, `stateQueryService()` (returns ThrowingStateQueryService placeholder until M3.6e), `mode()` delegating to `StateProjection.currentMode()`). Module-info gained non-transitive `requires com.homesynapse.integration` (HomeSynapseCore aggregates `IntegrationEvents.LIFECYCLE_EVENT_CLASSES` for the event-type registry). Phase 2 types (LifecyclePhase, SubsystemStatus, LifecycleEventType, SubsystemState, SystemHealthSnapshot, SystemLifecycleManager) coexist with M3.6d-a primitives (HomeSynapseConfig, SharedScheduler, ThrowingStateQueryService).
- **testing/integration-tests module (M3.4a + M3.4b):** Module #20. Tests gated on `-PpiProfile` (off by default; excluded from `./gradlew check`). Five IT tests: `BurstLoadIT`, `HeapBudgetIT` (M3.4a), `Pi4SustainedLoadIT`, `Pi4D1SpikeIT`, `CrashRecoveryIT` (M3.4b). `IntegrationTestHarness` composes `PersistenceTestHarness` + `InProcessEventBusFactory` against a real `@TempDir` SQLite file, with `startThrottled()` and `startForCrashSimulation()` factories (M3.4b). JVM constraints: `-Xmx256m -Xms256m -XX:ActiveProcessorCount=4 -XX:+UseG1GC -XX:MaxGCPauseMillis=100`.
- **MODULE_CONTEXT.md:** 20 files exist total — 17 populated substantively (including `testing/integration-tests` populated during WUCP Phase 2 reconciliation), 3 stubs (platform-systemd, dashboard, test-support). `core/event-bus/MODULE_CONTEXT.md` updated in M3.6b (EventBusConfig, InProcessEventBus public + 7-arg constructor, ReplayWindowQueue parameterized, InProcessEventBusFactory.createWithConfig). `core/persistence/MODULE_CONTEXT.md` updated in M3.6a (DeploymentProfile 3→6 fields, DatabaseExecutor accepts profile, LockingMode enum, PersistenceLifecycle Javadoc cleaned). `core/state-store/MODULE_CONTEXT.md` updated in projection-checkpoint wiring (added `StateCheckpointSource`, byte[0] stub deprecation note, projectionVersion authoritative source).
- **Tests:** ~1,500+ @Test methods total. Contract test suites: `EventStoreContractTest` (27), `EventBusContractTest` (50 — 34 active Tiers 1–8 + 6 active Tier 9 (Tier 9 `reconciliationOnVersionMismatch` un-disabled and implemented in M3.6d-a) + 6 active Tier 10 + 1 retagged + 3 disabled), `WriteCoordinatorContractTest` (11), `CheckpointStoreContractTest` (9), `ViewCheckpointStoreContractTest` (10), `DeadLetterStoreContractTest` (10 — M3.5b). M3.6a added 4 per-profile PRAGMA verification tests + 1 locking_mode default test in `DatabaseExecutorTest`. M3.6b added `EventBusConfigTest` (4) + `ReplayWindowQueueTest` (4) + 1 renamed Tier-9 overflow test. M3.6d-a added `ReconciliationTest` (4 of 5 methods — `reconciliationRecordsMetadataInDataSlot` deferred as feature gap; see OR-M3-13) + `SharedSchedulerTest` (5 methods — 4 from brief plus `taskFailureDoesNotSilenceCadence` pinning the `safelyInvoke` behaviour). Prior: M3.5b added `AtomicCheckpointWriterDlqTest` (3), `CheckpointSerializerTest` (12+), `SqliteStateStoreTest` (12). Supervisor DLQ wiring added `SubscriberSupervisorTest` (12). M3.4a added `BurstLoadIT` + `HeapBudgetIT` (gated). M3.4b added `ThrottledWriteCoordinatorTest` (9) + `Pi4SustainedLoadIT` + `Pi4D1SpikeIT` + `CrashRecoveryIT` (gated).
- **Traceability:** 01-event-model.md (44 entries), 12-lifecycle.md (2 entries). Stub indexes remain for docs 02–11, 13, 14 — Phase 2 traceability debt carries into Phase 3.
- **Last build gate:** RESOLVED. Full `./gradlew check` GREEN at HEAD `dfb045e` on 2026-05-21 (post-M3.6d-b). No deferred build gates open.

## Active Work

- **Last completed:** M3.6d-b via Claude Code (2026-05-21, `dfb045e`). M3.6a/b/c/d-a also completed 2026-05-20. All five PM-accepted, build GREEN.
- **Next:** M3.6e.1 coding instruction (StateQueryService + REST gate — M3.6 capstone first half). Estimated Coder time: 4–5h.
- **Claude Code workflow validated:** acceptEdits mode, Opus 4.7 xhigh, deny git commit/push/gradlew. PM generates task instruction → Claude Code executes → Nick reviews git diff, runs build gate, commits. Through M3.6d-b, eighteen WUs executed via this workflow (M3.6d-b was a 4-commit cohort: `a33ee40`, `a59b64e`, `725353d`, `dfb045e`). Bus-Fix Piece A and SLF4J follow-up patch were direct edits by Nick.

## Blocking Issues

None. No unresolved deferred build gates. All M3.6a/b/c/d-a/d-b build gates GREEN at commit time.

## Open Risks

- **OR-M3-12 — DEC-M3-17 governance entry (NEW 2026-05-20):** RESOLVED in this WUCP Phase 2 closeout. HealthSignal + HealthLevel public promotion alongside QueueSaturationHealthCheck logged as DEC-M3-17; entries appended to Current_State §3 ledger, Locked_Decisions Phase 3 milestone section, and `context/decisions/phase-3-cross-module-decisions.md`. No further action.
- **OR-M3-13 — ReconciliationRecordsMetadataInDataSlot feature gap (NEW 2026-05-20):** `StateProjection.writeCheckpoint` passes `null` for the three metadata fields (`reconciledAt`, `reconciledFromVersion`, `reconciledToVersion`) when calling `StateCheckpointSource.serializeCheckpoint(int)`. The source has no API to receive reconciliation metadata. AMD-41 §3.2.4's metadata-recording requirement is therefore not fully implemented. M3.6d-a's `ReconciliationTest` ships 4 of 5 methods; the 5th is deferred. Track as a separate enhancement WU — likely M4 scope since it touches the projection's checkpoint contract.
- **OR-M3-14 — M3.6d-b prerequisite infrastructure (NEW 2026-05-20):** RESOLVED 2026-05-21. All three prerequisite pieces shipped in the M3.6d-b 4-commit cohort: (1) `WriteCoordinator.queueSize()` at `a33ee40`; (2) production `SqliteSubscriberReadConnectionFactory` at `a59b64e`; (3) `SqlitePersistenceLifecycle` 6-store expansion + `PersistenceFactory` public gateway at `725353d`. `HomeSynapseCore` composition root completed at `dfb045e`. Build GREEN.

## Tracked Gaps (carry forward)

1. **Tier 9 `reconciliationOnVersionMismatch` test still `@Disabled("M3.5a")`** — re-enablement was split out of Bus-Fix Piece A. Now tracked under M3.6 lifecycle wiring (depends on `bus.resume()` VT re-spawn fix).
2. **`bus.resume()` does not re-spawn VT** — pre-existing M3.1 limitation; deferred to M3.6 lifecycle wiring.
3. **Overflow test slow (~5-15s)** — consider `@Tag("slow")` if suite time grows.
4. **JFR-native emission is accepted design debt** — pull-based metrics consumer (Prometheus/OTLP) will need typed adapter layer in M4+.
5. **Publish-latency metric is bus-side only** — end-to-end publish latency is a persistence-module metric for future observability pass.
6. **`lagEvents` approximation** — uses `pendingPositions.size()` instead of writer-tail-minus-delivered-position. To be revisited under M3.4b Pi4SustainedLoadIT if accuracy proves insufficient.
7. ~~**Composition root for ALWAYS-configured ObjectMapper**~~ — **CLOSED (M3.6d-b `725353d`).** `SqlitePersistenceLifecycle.start()` now constructs a separate `ALWAYS`-configured `ObjectMapper` for `CheckpointSerializer`, distinct from `PersistenceObjectMapper.create()` (`NON_NULL`). Wired through `PersistenceFactory`.
8. ~~**`QueueSaturationHealthCheck` and `DerivedWriteRateLimit` lifecycle wiring deferred**~~ — **CLOSED (M3.6d-b `dfb045e`).** `HomeSynapseCore.start()` constructs both and passes them to `SharedScheduler`.
9. ~~**`DerivedWriteRateLimit.refill()` externally called**~~ — **CLOSED (M3.6d-b `dfb045e`).** `SharedScheduler` calls `refill()` every 50 ms via `safelyInvoke(rateLimit::refill)`.
10. ~~**Defence-in-depth `IllegalStateException` for `EventPublisher.publish()` from REPLAY**~~ — **CLOSED (M3.6d-b `dfb045e`).** `HomeSynapseCore` subscribes the projection with `SubscriptionFilter.all()` + `coalesceExempt=true`; the bus's mode FSM prevents publish calls during REPLAY. The composition root wiring itself is the defence.
11. **Post-shutdown defensive handling in stores** — `SqliteDeadLetterStore` (and siblings) will throw uncaught exceptions if methods are called after `DatabaseExecutor.shutdown()`. Pre-existing pattern, not an M3.5b regression. Track for a future hardening pass.
12. **`AtomicCheckpointWriter` code duplication** — `writeAtomicCheckpoint` and `writeAtomicCheckpointWithDlqPark` duplicate the transaction wrapper. Track as tech debt; non-blocking (M3.5b review item 13).

## Schedule Position

**Significantly ahead of Master Release Plan.** The 37-week plan placed Weeks 1–10 as "Interface Specification" — the project finished that work in 7 days (Mar 14–20). Phase 3 persistence subsystem (M2.x) complete. Event bus production implementation with full REPLAY→LIVE algorithm + backpressure + persistent DLQ + state projection + integration tests (including sustained-load and crash-recovery) all landed in the M3.1–M3.4b window (May 16–19). See the Phase 3 Progress Annotation in `master-release-plan.md` for actual vs planned dates.

## Next on Critical Path

1. **M3.6e.1** — StateQueryService + REST gate (M3.6 capstone first half). Estimated 4–5h Coder time.
2. **M3.6e.2** — Admin endpoints + ArchUnit rules. Estimated 5–7h.
3. **M3.7** — end-to-end integration tests. Estimated 6–8h. Total M3.6/3.7 remaining: **~15–20h**.
4. **Phase 2 traceability debt** — 10 stub indexes remain (docs 02–11, 13, 14). Low priority; batch later.

## Recent Session Log

| Date | Agent | What Happened |
|------|-------|---------------|
| 2026-05-21 | Coder (Claude Code) | **M3.6d-b — PersistenceFactory + HomeSynapseCore Composition Root.** 4-commit cohort: `a33ee40` (WriteCoordinator.queueSize()), `a59b64e` (production SqliteSubscriberReadConnectionFactory), `725353d` (PersistenceFactory public gateway + SqlitePersistenceLifecycle 6-store expansion), `dfb045e` (HomeSynapseCore facade). 20 files (7 new + 13 modified), +1,432 lines. OR-M3-14 prerequisite infrastructure bundled. New production types: PersistenceFactory (public), SqliteSubscriberReadConnectionFactory (pkg-private), SqliteSubscriberReadExecutor (pkg-private), HomeSynapseCore (public). Fifteenth–eighteenth CC WUs. |
| 2026-05-22 | PM (Cowork) | **WUCP Phase 2 — M3.6d-b closure.** Closeout for M3.6d-b (`dfb045e`). OR-M3-14 RESOLVED. OQ-05-03 RESOLVED. Tracked gaps #7–10 CLOSED. Next: M3.6e.1 coding instruction. |
| 2026-05-20 | PM (Cowork) | **WUCP Phase 2 — M3.6c + M3.6d-a + DEC-M3-17.** Closeout for M3.6c (`38d3e30`) and M3.6d-a (`25bc23b`). M3.6d sub-divided into d-a (done) + d-b (next) per Option A. DEC-M3-17 logged (HealthSignal + HealthLevel transitive promotion; DEC-M3-16 addendum). Open risks added: OR-M3-13 (reconciliation metadata feature gap), OR-M3-14 (M3.6d-b prerequisite infrastructure). Next: revised M3.6d-b coding instruction. |
| 2026-05-20 | Coder (Claude Code) | **M3.6d-a — Composition-Root Satellite Changes.** Committed `25bc23b`. 18 files (6 new + 12 modified). Major scope: SqliteStateStore implements StateCheckpointSource; QueueSaturationHealthCheck + HealthSignal + HealthLevel public (DEC-M3-17 transitive chain); ReadinessSource public interface; ReconciliationTest 4 of 5 methods; Tier 9 reconciliationOnVersionMismatch un-disabled; HomeSynapseConfig + SharedScheduler + ThrowingStateQueryService skeletons in lifecycle module; module-info `requires transitive` for persistence/event.bus/state-store + non-transitive `requires org.slf4j`. M3.6d sub-divided after Coder pushback identified 7 source-vs-brief mismatches (user chose Option A). SLF4J follow-up patch applied same-day (build green after fix). Fourteenth CC WU. |
| 2026-05-20 | Coder (Claude Code) | **M3.6c — Per-Module Event-Class Manifests.** Committed `38d3e30`. 1 new file + 4 modified. `EventTypes.CORE_PRODUCTION_EVENT_CLASSES` + `IntegrationEvents.LIFECYCLE_EVENT_CLASSES` aggregated at the composition root via `Stream.concat`. Closes Q3 gap-closure Artifact 1. Deviations D-1/D-2/D-3 all naming/cosmetic. Thirteenth CC WU. |
| 2026-05-20 | PM (Cowork) | **WUCP Phase 2 — M3.6a + M3.6b.** Governance/context maintenance closing both sub-WUs. Four PM-side artifacts updated. DEC-M3-16 applied. Audit findings C-01, D1-05, D1-07, D1-13, D2-11, D4-09, D5-04 CLOSED. Next: M3.6c coding instruction. |
| 2026-05-20 | Coder (Claude Code) | **M3.6b — EventBusConfig + InProcessEventBus Visibility.** `EventBusConfig` record (2 fields, `HOME_DEFAULT`). `ReplayWindowQueue` capacity parameterized. `InProcessEventBus` promoted to `public` (DEC-M3-16). 8 files (3 new, 5 modified). 9 tests added/modified. Tenth CC WU. |
| 2026-05-20 | Coder (Claude Code) | **M3.6a — Profile-Driven Persistence Configuration.** Wired `DeploymentProfile` through `PersistenceConfig` into `DatabaseExecutor`. PRAGMAs profile-driven. `LockingMode` enum created. 14 files (1 new, 13 modified). 5 tests added/modified. Ninth CC WU. |
| 2026-05-19 | PM (Cowork) | **WUCP Phase 2 Reconciliation.** Retroactive closeout for six work units (Bus-Fix Piece A through M3.4b) and two design sessions. Hivemind brought from STALE to PASS. `testing/integration-tests/MODULE_CONTEXT.md` populated. Next: M3.6a coding instruction (profile-driven persistence config). |
| 2026-05-20 | PM (Cowork) | **Gap-Closure + M3.6 Composition-Root Design.** Two artifacts: Q1-Q4 gap-closure answers (all benign) + M3.6 five-WU design (M3.6a..M3.6e). Design approved by Nick. Preflight STALE override (Option B) documented. Artifacts: research/2026-05-20_M3_Audit_Gap_Closure_v1.md, design/2026-05-20_M3.6_Composition_Root_Design.md |
| 2026-05-19 | PM (Cowork) | **Cross-Tier Deployment Audit.** Six-dimension audit across six deployment tiers. Verdict: NEARLY READY. C-01 (DeploymentProfile not wired) revised from BLOCKING to SIGNIFICANT. Nine SIGNIFICANT findings fold into M3.6. Report: nexsys-hivemind/context/audits/2026-05-19_cross-tier-deployment-audit.md |
| 2026-05-19 | Coder (Claude Code) | **M3.4b — Sustained-Load + Crash-Recovery Tests.** ThrottledWriteCoordinator disk test double. Pi4SustainedLoadIT, Pi4D1SpikeIT, CrashRecoveryIT. scripts/pi4-validation.sh on-device runner. All tests GREEN. Deviations: event-count assertion loosened (±2% → lower-bound 25%), @TempDir NEVER, SLF4J dep add. Commit `adf04d2`. |
| 2026-05-19 | Coder (Claude Code) | **M3.4a — Integration-Test Scaffold.** Module 20 (testing:integration-tests). IntegrationTestHarness, BurstLoadIT, HeapBudgetIT. PersistenceTestHarness + InProcessEventBusFactory testFixture factories. Pi-profile gated. Commit `5ae7912`. |
| 2026-05-19 | Coder (Claude Code) | **Supervisor DLQ Wiring.** 11-field DeadLetter replaces 6-field DlqEntry. PersistentDlqWriter interface. 12 new tests. Commit `ed5862c`. |
| 2026-05-19 | Coder (Claude Code) | **Projection-Checkpoint Wiring.** StateCheckpointSource injection seam. 10 MB advisory checkpoint-size guardrail. 12 new tests. Commit `56aaa4b`. |
| 2026-05-18 | Coder (Claude Code) | **M3.5b StateProjection Prod Persistence.** SqliteStateStore, SqliteCheckpointStore, AtomicCheckpointWriter. Full contract suite GREEN. Commit `08d0136`. |
| 2026-05-18 | Nick (direct edit) | **Bus-Fix Piece A.** DerivedWriteRateLimit promoted to public in core/event-bus. Unblocks cross-package construction. Commit `fceafe8`. |
| 2026-05-19 | Coder (Claude Code) | **M3.4a — Integration test scaffold + harness + BurstLoadIT + HeapBudgetIT.** New `testing/integration-tests` module (#20). `PersistenceTestHarness` and `InProcessEventBusFactory` testFixtures bridge package-private production types. `IntegrationTestHarness` wires the real production stack (file-based SQLite + `InProcessEventBus`). BurstLoadIT (500-event burst, 6 assertions) + HeapBudgetIT (3,000-entity heap bound, 4 assertions). Tests gated on `-PpiProfile`. `testFixturesApi` deps added to persistence for cross-module fixture visibility. Full `./gradlew check` GREEN; `./gradlew :testing:integration-tests:test -PpiProfile=throttled` GREEN. Commit `5ae7912`. |
| 2026-05-19 | Coder (Claude Code) | **Supervisor DLQ wiring.** `SubscriberSupervisor.deliver()` constructs `DeadLetter` (11 fields) instead of `DlqEntry` (6 fields). Routes through `park(DeadLetter)` — dual ring + persistent writer. Null-guarded `causeMessage`, `diagnostics=null`, `attemptCount=1`. `InProcessEventBus` DLQ identity upgraded to two-arg constructor. `TransitionCoordinator.park(DlqEntry)` deliberately preserved for `CAUGHT_UP_TRANSITION_MARKER = -1L`. 12 new `SubscriberSupervisorTest` methods. Source-verification audit `2026-05-19_supervisor-dlq-source-verification.md` confirmed 9 assumptions (1 corrected: `SubjectRef.toString()` format). Commit `ed5862c`. |
| 2026-05-19 | Coder (Claude Code) | **Projection-checkpoint wiring.** `StateCheckpointSource` interface introduced in state-store. Advisory 10 MB checkpoint-size guardrail in `StateProjection`. Wires `StateProjection` to call `source.serializeCheckpoint(projectionVersion)`. Closes M3.5b non-blocking concern #1. Commit `56aaa4b`. |
| 2026-05-18 | Coder (Claude Code) | **M3.5b — StateProjection production persistence.** `SqliteStateStore` (ConcurrentHashMap-backed), `SqliteDeadLetterStore`, `PersistentDlqWriter` interface, `CheckpointSerializer` with Jackson JSON, V004 DLQ indices migration, `ObjectMapper` divergence (NON_NULL for events, ALWAYS for checkpoints), `AtomicCheckpointWriter.writeAtomicCheckpointWithDlqPark()` three-way atomic write. 19 files, +2,674 insertions. Independent review (`2026-05-18_m3.5b-review-report.md`): PASS with 5 non-blocking concerns. Commit `08d0136`. |
| 2026-05-18 | Nick (direct edit) | **Bus-Fix Piece A.** `DerivedWriteRateLimit` promoted package-private → public (one-line visibility change + MODULE_CONTEXT update moving the row from the pkg-private table to the public table). Closes G4 mismatch from M3.5a. Commit `fceafe8`. |
| 2026-05-18 | Coder (Claude Code) | M3.5a StateProjection vertical slice. First cross-module M3 milestone (state-store → event-bus). 7 new production types (6 public + 1 pkg-private SelfProducedFilter), 2 testFixture fixtures, 2 abstract contract tests, 4 concrete test classes. DerivedPublishGate adapter seam introduced (G4: DerivedWriteRateLimit was package-private — closed at Bus-Fix Piece A). Full build GREEN (130 tasks). Third Claude Code milestone. Commit `a2aff9c`. |
| 2026-05-17 | Coder (Claude Code) | M3.3 Backpressure, Metrics, Observability — 13 NEW production types, 3 NEW test classes (27 tests), 6 Tier 10 contract tests. Type count 16→29. DEC-M3-14 (IntSupplier injection), DEC-M3-15 (STOP gate removal pattern). Build GREEN at `a5d4b2a`. Second milestone via Claude Code. |
| 2026-05-17 | Coder (Claude Code) | M3.2 REPLAY→TRANSITION→LIVE bus-side — 3 NEW production files, 3 MODIFY production, 1 NEW test, 1 MODIFY testFixture, 1 MODIFY MODULE_CONTEXT. 16 production types total. Build GREEN at `0bade6a`. First milestone via Claude Code. |
| 2026-05-17 | Coder (Cowork) | M3.1 InProcessEventBus Core — 10 new production files, 1 modified interface (+4 default methods), 1 modified contract test (+26 test methods), 1 new test, 1 new testFixture, 1 updated MODULE_CONTEXT. 14 production types total. |
| 2026-05-16 | Nick + PM | M3 governance bundle committed: AMD-41/42/43 APPLIED, PLAN-M3-CONSOLIDATED-02, DEC-M3-01..13. Deliverable 0 (ProjectionAdvancer 3-param signature) landed. |
| 2026-05-15 | Coder | AMD-38 → APPLIED, AMD-39 → WITHDRAWN (D1 WAL spike evidence). DeploymentProfile corrected to uniform 6 MB (LTD-03). Build gate GREEN. |
| 2026-05-15 | Coder | D1 WAL Pathology Validation Spike — 3 runs confirming bounded-reader is load-bearing, 6 MB journal limit safe without active checkpointing. |
| 2026-05-15 | Coder | M2→M3 Bridge — AMD-34..40, V001→25 columns, V002 DLQ table, V003 snapshots + index drop, 10 new Java types (state-store: 5, persistence: 5). Build gate GREEN. |
| 2026-05-01 | Coder | M2 persistence subsystem complete — SqlitePersistenceLifecycle wired, boot-order composition. |
| 2026-04-11 | PM | Governance overhaul — WUCP generalization, freshness preflight, retroactive Phase 2 catch-up for M2.1–M2.5. |
| 2026-04-11 | Coder | M2.5 SqliteEventStore landed (`5279e7a`). Arch-debt fix (`d6a6065`) resolved NO_DIRECT_TIME_ACCESS violations. |

---

**Last verified against:** `homesynapse-core` commit `dfb045e` on `2026-05-22`.
