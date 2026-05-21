<!--
file: context/planning/phase-3-milestone-backlog.md
purpose: Active Phase 3 milestone backlog — DONE/NEXT/PLANNED/FUTURE rows for every milestone.
audience: All
update-cadence: per-milestone
state-type: current
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# Phase 3 Milestone Backlog — ACTIVE

**Current phase:** P3 Implementation (test-first).
**Phase started:** 2026-03-27 (first test commits) / 2026-04-10 (first production implementation via M2.1).
**Frozen Phase 2 record:** `phase-2-block-backlog.md`.

Phase 3 uses **Milestone** vocabulary (M{major}.{minor}) instead of Phase 2's Block letter vocabulary. A milestone is a single work unit — a coherent compile-and-commit unit with test coverage — and is governed by the Work Unit Completion Protocol (WUCP) in `context/protocols/work-unit-completion-protocol.md`.

**Status key:** DONE | NEXT | PLANNED | FUTURE

---

## Major M1 — Test-First Preparation

Test fixtures, contract tests, and in-memory reference implementations written BEFORE any production code. Not formally tracked as M1.x milestones at the time — captured here retroactively for continuity.

| Milestone | Scope | Module | Status | Commits |
|---|---|---|---|---|
| M1.a | Event model unit tests (59 methods) | event-model | DONE 2026-03-27 | `9714885`, `ad74ee1`, `a98d232`, `9e4e71b` |
| M1.b | InMemoryEventStore — 27/27 contract tests pass | event-model | DONE 2026-03-27 | `022fd83` |
| M1.c | TestEventFactory + TestCausalContext fixtures | event-model | DONE 2026-03-28 | `388f947` |
| M1.d | SQLite WAL spike validation benchmarking | persistence | DONE 2026-04-02 | `d48df13` |
| M1.e | Traceability index population, LTD citation fix, S4 gotchas | multiple | DONE 2026-04-04 | `7ee5a22` |
| M1.f | Test fixtures + contract tests for device-model, event-bus, state-store, integration-api, configuration | 5 modules | DONE 2026-04-07 | `9ae1a47`, `177e190`, `54efbd2` |
| M1.g | EventBusContractTest (18 methods) + InMemoryEventBus | event-bus | DONE 2026-04-08 | `477b7f4` |
| M1.h | WriteCoordinatorContractTest (11 methods) + InMemoryWriteCoordinator | persistence | DONE 2026-04-08 | `c350f15` |
| M1.i | EntityState/StateSnapshot/Availability/StateQueryService tests (27 methods) | state-store | DONE 2026-04-09 | `b545ad7` |

## Amendment M-AMD-33

| Milestone | Scope | Module | Status | Commit |
|---|---|---|---|---|
| AMD-33 | DomainEvent permanently non-sealed, codebase alignment | event-model | DONE 2026-04-10 | `768a4e4` |

*Note: Amendments AMD-34 through AMD-43 were ratified during M2-bridge through M3 governance. See `homesynapse-core-docs/design/amendments/` for the full list. AMD-41/42/43 (M3 governance bundle) APPLIED 2026-05-16.*

## Major M2 — Persistence Subsystem Implementation

The first real production implementation. M2.x delivers the event-sourced storage foundation that every downstream subsystem will depend on.

| Milestone | Scope | Module | Status | Commit | Notes |
|---|---|---|---|---|---|
| M2.1 | `@EventType` annotation + application to 22 event records (7 tests), MODULE_CONTEXT updated | event-model | DONE 2026-04-10 | `b2c8b78` | — |
| M2.i | Intermission — apply `@EventType` to IntegrationLifecycleEvent subtypes | integration-api | DONE 2026-04-10 | `e9e7827` | Not a numbered milestone; consistency follow-up |
| M2.2 | Migration framework + V001 initial event store schema | persistence | DONE 2026-04-10 | `696ac37` | MigrationRunner + Flyway-style semantics. Build gate deferred to Nick — latent NO_DIRECT_TIME_ACCESS violation (`Instant.now()` in MigrationRunner) shipped, caught by M2.5's test run. |
| M2.3 | DatabaseExecutor + platform-thread write/read executors (31 tests) | persistence | DONE 2026-04-10 | `d24f628` | — |
| M2.4 | Serialization infrastructure — EventTypeRegistry, ULID serde, EventPayloadCodec (62 tests) | persistence | DONE 2026-04-10 | `4b20786` | Build gate deferred — latent NO_DIRECT_TIME_ACCESS violation (`System.nanoTime()` in JacksonWarmup) shipped, caught by M2.5's test run. |
| Arch-debt | Clock injection into MigrationRunner + DatabaseExecutor, JacksonWarmup simplification, test-side Clock.fixed propagation | persistence | DONE 2026-04-11 | `d6a6065` | Resolves latent violations from M2.2 and M2.4. |
| M2.5 | SqliteEventStore + TimeConversion + EventCategoryMapping; V001 schema amendment (`subject_type` column); TestPayload `@EventType`; DatabaseExecutor.readConnections() accessor; 46 new tests | persistence + event-model testFixtures | DONE 2026-04-11 | `5279e7a` | Deviations D-01..D-06 documented in coder-handoff. Contract tests: 27 inherited + 10 TimeConversion + 9 EventCategoryMapping. |
| M2.6–M2.9 | Combined: SqlitePersistenceLifecycle, boot-order, full persistence wiring | persistence + lifecycle + app | DONE 2026-05-01 | — | Persistence subsystem complete. |
| M2-bridge | AMD-34..37, V001→25 columns, V002 DLQ table, V003 snapshots, 10 new Phase 2 types | state-store + persistence | DONE 2026-05-02 | — | Schema reservations, snapshot table, redundant index drop. |
| D1 spike | WAL Pathology Validation — bounded reader is load-bearing | spike/wal-validation | DONE 2026-05-15 | — | AMD-38 APPLIED, AMD-39 WITHDRAWN. |
| AMD-38/39 | AMD-38 APPLIED, AMD-39 WITHDRAWN, DeploymentProfile corrected | persistence | DONE 2026-05-15 | — | |
| Deliverable 0 | ProjectionAdvancer.advance 3-param signature | state-store | DONE 2026-05-16 | — | Consumer<EventEnvelope> callback. |

## Major M3 — Event Bus & Downstream Subsystem Implementation

*Updated 2026-05-20 (Post-M3.6c + M3.6d-a WUCP Phase 2 closure; M3.6d sub-divided; DEC-M3-17 logged).* M3 governance (AMD-41/42/43, PLAN-M3-CONSOLIDATED-02, DEC-M3-01..17) defines the authoritative implementation plan and milestone ordering. DEC-M3-11 specifies: M3.1 → M3.5a → M3.2 → M3.3 → M3.4 → M3.5b → M3.6 → M3.7. The actual landing order (driven by Nick's session sequencing) is: M3.1 → M3.2 → M3.3 → M3.5a → Bus-Fix Piece A → M3.5b → projection-checkpoint wiring → supervisor DLQ wiring → M3.4a → M3.4b → M3.6a → M3.6b → M3.6c → M3.6d-a. M3.6d-b NEXT.

### M3 Milestones and intra-milestone work units

| Milestone / WU | Scope | Module(s) | Status | Commit | Notes |
|---|---|---|---|---|---|
| **M3.1** | InProcessEventBus core: mode FSM, subscriber isolation, supervisor/DLQ, circuit breaker | event-bus | **DONE 2026-05-17** | — | 14 production types. Build gate deferred and resolved by M3.2. |
| **M3.2** | REPLAY→TRANSITION→LIVE bus-side: ReplayDriver, TransitionCoordinator, replay window drain, gap detection | event-bus | **DONE 2026-05-17** | `0bade6a` | First Claude Code milestone. |
| **M3.3** | Backpressure and observability: BusMetrics, QueueSaturationHealthCheck, DerivedWriteRateLimit | event-bus | **DONE 2026-05-17** | `a5d4b2a` | Second CC milestone. DEC-M3-14/15. JFR-native metrics. |
| **M3.5a** | StateProjection vertical slice — first Subscriber implementation, end-to-end path | state-store + event-bus | **DONE 2026-05-18** | `a2aff9c` | First cross-module M3 milestone. Third CC milestone. DerivedPublishGate adapter seam (G4 — DerivedWriteRateLimit pkg-private). |
| **Bus-Fix Piece A** | `DerivedWriteRateLimit` promoted package-private → public (one-line visibility change + MODULE_CONTEXT update). Enables cross-module consumers (composition root, state-store `DerivedPublishGate` method reference) to reach the type directly. | event-bus | **DONE 2026-05-18** | `fceafe8` | Closes the G4 mismatch from M3.5a. Tier 9 reconciliation-test enablement and `bus.resume()` VT re-spawn fix split out — remain tracked under M3.6 lifecycle wiring. |
| **M3.5b** | Production persistence for StateProjection: `SqliteStateStore` (ConcurrentHashMap-backed), `SqliteDeadLetterStore`, `PersistentDlqWriter` interface, `CheckpointSerializer` (Jackson JSON), V004 DLQ indices migration, `ObjectMapper` divergence (NON_NULL for events, ALWAYS for checkpoints), `AtomicCheckpointWriter.writeAtomicCheckpointWithDlqPark()` three-way atomic write | event-bus + persistence + state-store | **DONE 2026-05-18** | `08d0136` | 19 files, +2,674 lines. Independent review report `2026-05-18_m3.5b-review-report.md`: PASS with 5 non-blocking concerns. |
| **Projection-checkpoint wiring** | `StateCheckpointSource` interface introduced in state-store. Advisory 10 MB checkpoint-size guardrail in `StateProjection`. Wires `StateProjection` to call `source.serializeCheckpoint(projectionVersion)` — closes M3.5b non-blocking concern #1 (no size guardrail). | state-store | **DONE 2026-05-19** | `56aaa4b` | Composition root still owes the ALWAYS-configured ObjectMapper wiring (deferred to M3.6). |
| **Supervisor DLQ wiring** | `SubscriberSupervisor.deliver()` constructs `DeadLetter` (11 fields) instead of `DlqEntry` (6 fields). Routes through `park(DeadLetter)` — dual ring + persistent writer. Null-guarded `causeMessage` (`""` fallback for null `RuntimeException.getMessage()`), `diagnostics=null`, `attemptCount=1`. `InProcessEventBus` DLQ identity upgraded to two-arg constructor (`new SubscriberDlq(info.subscriberId(), PersistentDlqWriter.noop())`). 12 new `SubscriberSupervisorTest` methods. | event-bus | **DONE 2026-05-19** | `ed5862c` | `TransitionCoordinator.park(DlqEntry)` deliberately preserved for the `CAUGHT_UP_TRANSITION_MARKER = -1L` synthetic case (`DeadLetter` validates `eventPosition >= 0`). Source-verification audit `2026-05-19_supervisor-dlq-source-verification.md` confirmed all 9 assumptions (1 corrected: `SubjectRef.toString()` format). Retry loop remains M3.2-deferred dead code; `attemptCount=1` is correct for current single-attempt semantics. |
| **M3.4a** | Integration test module scaffold + harness + first 2 IT tests. New `testing/integration-tests` module (#20). `PersistenceTestHarness` and `InProcessEventBusFactory` testFixtures bridge package-private production types. `IntegrationTestHarness` wires the real production stack (file-based SQLite + `InProcessEventBus`). `BurstLoadIT` (500-event burst, 6 assertions). `HeapBudgetIT` (3,000-entity heap bound, 4 assertions). Tests gated on `-PpiProfile`. `testFixturesApi` deps added to persistence for cross-module fixture visibility. | testing/integration-tests + persistence (testFixtures) + event-bus (testFixtures) | **DONE 2026-05-19** | `5ae7912` | Full `./gradlew check` GREEN; `./gradlew :testing:integration-tests:test -PpiProfile=throttled` GREEN (BurstLoadIT + HeapBudgetIT). |
| **M3.4b** | Sustained-load + crash-recovery integration tests + on-device script. ThrottledWriteCoordinator disk test double, Pi4SustainedLoadIT, Pi4D1SpikeIT, CrashRecoveryIT, scripts/pi4-validation.sh. | testing/integration-tests + persistence (main + testFixtures + test) + event-bus (testFixtures) | **DONE 2026-05-19** | `adf04d2` | 9 unit tests (ThrottledWriteCoordinatorTest) + 3 IT tests. Both `./gradlew check` and Pi-profile tests GREEN. PM-accepted deviations: event-count assertion loosened (±2% → lower-bound 25%); @TempDir NEVER; SLF4J dep add; startForCrashSimulation shares wiring. |
| **M3.6a** | Profile-driven persistence configuration. DeploymentProfile 3→6 fields (busyTimeoutMs, lockingMode, readThreadCount added). LockingMode enum. PersistenceConfig record. DatabaseExecutor accepts profile. SQLite PRAGMAs profile-driven. Closes audit C-01, D1-05, D1-13, D2-11, D5-04. First of five M3.6 sub-WUs. | persistence + event-bus + testing/integration-tests | **DONE 2026-05-20** | `17c40b6` | 14 files (1 new, 13 modified). 5 tests added/modified. Ninth CC WU. |
| **M3.6b** | EventBusConfig record (replayQueueCapacity, publisherBlockedDepthThreshold; HOME_DEFAULT). ReplayWindowQueue capacity parameterized. InProcessEventBus promoted to public (DEC-M3-16). InProcessEventBusFactory.createWithConfig. Closes audit D1-07, D4-09. Second of five M3.6 sub-WUs. | event-bus | **DONE 2026-05-20** | `df2743a` | 8 files (3 new, 5 modified). 9 tests added/modified. Tenth CC WU. |
| **M3.6c** | Per-module event-class manifests. `EventTypes.CORE_PRODUCTION_EVENT_CLASSES` (22) + `IntegrationEvents.LIFECYCLE_EVENT_CLASSES` (5) aggregated via `Stream.concat` at composition root. Closes Q3 gap closure (Artifact 1). Third of five M3.6 sub-WUs. | core/event-model + integration/integration-api + core/persistence (test) + testing/integration-tests (test) | **DONE 2026-05-20** | `38d3e30` | 1 new file + 4 modified. Refactor-only — no net test additions. Thirteenth CC WU. |
| **M3.6d-a** | Composition-root satellite changes. SqliteStateStore implements StateCheckpointSource (serialize → serializeCheckpoint rename + public via interface). QueueSaturationHealthCheck + HealthSignal + HealthLevel promoted to public (DEC-M3-17 — transitive chain). ReadinessSource public interface in core/state-store. ReconciliationTest 4 of 5 methods (5th deferred — OR-M3-13). Tier 9 reconciliationOnVersionMismatch un-disabled + implemented. Lifecycle module skeletons: HomeSynapseConfig (public record) + SharedScheduler (package-private final, 50 ms refill + 1 s tick) + ThrowingStateQueryService (package-private final). Module-info `requires transitive` for persistence/event.bus/state-store + non-transitive `requires org.slf4j`. SLF4J follow-up fix applied same-day. Closes audit D3-08. Fourth of six (was five — d-a + d-b split) M3.6 sub-WUs. | core/persistence + core/event-bus + core/state-store + lifecycle | **DONE 2026-05-20** | `25bc23b` | 18 files (6 new + 12 modified). Tests added: SharedSchedulerTest (5) + ReconciliationTest (4) + Tier 9 un-disabled (1). Fourteenth CC WU. |
| **M3.6d-b** | PersistenceFactory + HomeSynapseCore (composition-root wiring). Requires prerequisite infrastructure work per OR-M3-14: (1) SqlitePersistenceLifecycle must construct SqliteStateStore + SqliteDeadLetterStore; (2) WriteCoordinator.queueSize() accessor; (3) production SubscriberReadConnectionFactory. Fifth of six M3.6 sub-WUs. | persistence + lifecycle + app + state-store | **NEXT** | — | PM coding instruction pending revision. Estimated 10–12h Coder time (grown from 6–8h due to prerequisite work). |
| **M3.6e.1** | StateQueryService + REST gate (M3.6 capstone). First half of expanded M3.6e scope. | state-store + rest-api | **PLANNED** | — | M3.6e scope expansion: split into e.1 (query + REST) and e.2 (admin + ArchUnit). |
| **M3.6e.2** | Admin endpoints + ArchUnit rules. Second half of expanded M3.6e scope. | rest-api + multiple | **PLANNED** | — | — |
| **M3.7** | End-to-end integration tests across the full subsystem graph. | testing/integration-tests + multiple | **PLANNED** | — | Sequenced after M3.6 (composition root must exist before E2E can wire the full stack). |

### Committed M3 design artifacts (not milestones — informational)

These are referenced from milestone instructions but are not themselves work units. They are recorded here so the milestone backlog accurately reflects the design state that downstream work depends on.

| Artifact | Type | Path | Date | Notes |
|---|---|---|---|---|
| Cross-tier deployment audit | Audit | `HomeSynapse_Core_CrossTier_Deployment_Audit.md` (workspace root) | 2026-05-19 | Closed-out audit of cross-tier deployment surface. Informed M3.6 composition root design. |
| M3 audit gap-closure research | Research | `homesynapse-core-docs/research/2026-05-20_M3_Audit_Gap_Closure_v1.md` | 2026-05-20 | Artifact 1 of the gap-closure pass. Identified and closed audit-trail gaps prior to M3.4b/M3.6. |
| M3.6 Composition Root Design | Design | `homesynapse-core-docs/design/2026-05-20_M3.6_Composition_Root_Design.md` | 2026-05-20 | Authoritative composition-root design that M3.6 implements against. |

### Future Major Groups (provisional skeleton from Alignment Pass #2)

| Major group | Subsystem | Dependencies | Status | Notes |
|---|---|---|---|---|
| **M3** | Event Bus (production impl) | persistence (M2) | **ACTIVE** | M3.1–M3.4b + M3.6a/b/c/d-a + intra-milestone WUs done (fourteen Claude Code WUs total). M3.6d-b NEXT. M3.6e.1/e.2 + M3.7 PLANNED. See M3 Milestones above. |
| **M4** | State Store (projection impl) | event-bus (M3), persistence (M2) | PLANNED | Largely delivered via M3.5a + M3.5b vertical-slice approach. Remaining M4 scope: full StateQueryService implementation and the rest of the projection surface. |
| **M5** | Platform API + test-support | no hard deps (can run parallel with M3/M4 scaffold work) | PLANNED | PlatformPaths implementations (Linux, development); HealthReporter; test-support module produces InMemoryEventStore / SynchronousEventBus / TestClock / NoRealIoExtension. |
| **M6** | Configuration System | state-store (M4), persistence (M2.10) | PLANNED | YAML loading pipeline; JSON Schema validation; secret store (AES-256-GCM); hot reload with atomic swap; `ConfigurationAccess` + `ConfigurationProvider` impls |
| **M7** | Automation Engine (core) | event-bus (M3), state-store (M4), configuration (M6) | PLANNED | Trigger/condition/action pipeline; AMD-25 temporal-duration trigger modifier; command ledger basics |
| **M8** | Automation Engine (advanced) | automation core (M7) | PLANNED | Command ledger full; cascade governance; concurrency modes; AMD-17 orphan-detection interaction |
| **M9** | Integration Runtime | event-bus (M3), state-store (M4), configuration (M6), lifecycle (M2.8) | PLANNED | Supervisor tree; health FSM; crash isolation; restart intensity; `IntegrationContext` composition; planned-restart lifecycle (Doc 05 §3.14) |
| **M10** | REST API | state-store (M4), configuration (M6), integration-runtime (M9) | PLANNED | All 5 endpoint planes; error format; pagination; rate limiting; auth |
| **M11** | WebSocket API | event-bus (M3), rest-api (M10) | PLANNED | Subscriptions, resume, backpressure; protocol-compliant framing; `WsSubscriptionFilter` dispatch via `@EventType` registry (D-01) |
| **M12** | Observability & Debugging | event-bus (M3), persistence (M2.10), state-store (M4), lifecycle (M2.8) | PLANNED | Health aggregation; JFR recording; trace storage; causal-chain assembly; trace query service |
| **M13** | Startup & Lifecycle (full wiring) | all prior M* | PLANNED | Seven-phase init; graceful shutdown drains events; watchdog; boot-order correctness across the full subsystem graph — the first milestone that runs the complete app. Largely subsumed by M3.6 for the M3 slice; M13 extends coverage to all subsystems. |
| **M14** | Zigbee Integration | integration-runtime (M9), lifecycle (M13) | PLANNED | Adapter integration; ZCL + Tuya + Xiaomi codecs; dual-coordinator strategy (Z-Stack + EZSP per LD); device interview protocol |
| **M15** | Full system integration + performance benchmarks | M13 + M14 | PLANNED | App starts, serves APIs, projects state, fires automations end-to-end. Benchmark event throughput (>500/sec sustained), state-query latency (<5ms p99), memory profile under 50-entity simulated load per MVP §8.2 budgets |

**Ordering invariant:** The dependency graph above is the sole determinant of milestone ordering. A milestone cannot start until every dependency listed has reached its `.10` integration-test milestone (or equivalent closeout). This discipline was explicitly missing in the original Master Release Plan week-by-week ordering and is added here as a hard constraint.

**Sizing assumption:** Based on M2.x cadence (~3-hour milestones in Nick's school-day blocks, ~full-day on weekends), each major group above is expected to decompose into 3–8 individual `M{n}.{y}` milestones. The first milestone of each group (`M{n}.1`) is typically the minimal slice that makes a contract test pass; subsequent milestones round out the subsystem until `.10` (integration tests) closes it.

**Replacement for Master Plan week numbers:** The Master Release Plan's original Weeks 13–26 subsystem ordering is superseded by this skeleton for operational planning purposes. The plan remains the schedule-anchoring document for launch-date tracking; this skeleton is the execution-anchoring document for the Coder/PM loop.

---

## WUCP Phase 2 Reconciliation Closeout Entries (2026-05-19)

*Six work units closed out retroactively during the 2026-05-19 WUCP Phase 2 reconciliation session. These entries supplement the summary rows in the M3 Milestones table above.*

### Bus-Fix Piece A — DerivedWriteRateLimit Visibility
- **Status:** DONE
- **Commit:** `fceafe8` (2026-05-18)
- **Scope:** Promoted DerivedWriteRateLimit from package-private to public in core/event-bus.
- **Tests:** No new tests (existing suite GREEN).
- **Build gate:** GREEN.

### M3.5b — StateProjection Production Persistence
- **Status:** DONE
- **Commit:** `08d0136` (2026-05-18)
- **Scope:** SqliteStateStore, SqliteCheckpointStore, AtomicCheckpointWriter in core/persistence. StateProjection wired to real SQLite persistence.
- **Tests:** Full StateStoreContractTest + CheckpointStoreContractTest suites GREEN against SQLite implementations.
- **Build gate:** GREEN.

### Projection-Checkpoint Wiring
- **Status:** DONE
- **Commit:** `56aaa4b` (2026-05-19)
- **Scope:** StateCheckpointSource injection seam in core/state-store. 10 MB advisory checkpoint-size guardrail. End-to-end projection checkpoint persistence.
- **Tests:** 12 new tests.
- **Build gate:** GREEN.

### Supervisor DLQ Wiring
- **Status:** DONE
- **Commit:** `ed5862c` (2026-05-19)
- **Scope:** 11-field DeadLetter replaces 6-field DlqEntry. PersistentDlqWriter interface + noop default.
- **Tests:** 12 new tests in event-bus.
- **Build gate:** GREEN.

### M3.4a — Integration-Test Scaffold (Pi Profile)
- **Status:** DONE
- **Commit:** `5ae7912` (2026-05-19)
- **Scope:** Module 20 (testing:integration-tests). IntegrationTestHarness + BurstLoadIT (6 assertions) + HeapBudgetIT (4 assertions). PersistenceTestHarness + InProcessEventBusFactory testFixture factories. Pi-profile gated behind -PpiProfile=throttled.
- **Tests:** 10 new test methods.
- **Build gate:** GREEN.
- **Note:** MODULE_CONTEXT.md populated in WUCP Phase 2 reconciliation (this session).

### M3.4b — Sustained-Load + Crash-Recovery Integration Tests
- **Status:** DONE
- **Commit:** `adf04d2` (2026-05-19)
- **Scope:** ThrottledWriteCoordinator disk test double. Pi4SustainedLoadIT (100 ev/s sustained), Pi4D1SpikeIT (50 ev/s + D1 spikes, 30 min), CrashRecoveryIT (5,000 events, abandon + restart). scripts/pi4-validation.sh. SLF4J API dependency. DatabaseExecutor + SqlitePersistenceLifecycle decorator constructor overloads.
- **Tests:** 9 unit tests (ThrottledWriteCoordinatorTest) + 3 integration tests. Total: 12 new.
- **Build gate:** GREEN (both ./gradlew check and Pi-profile tests).
- **PM-accepted deviations:** Event-count assertion loosened (±2% → lower-bound 25%); @TempDir NEVER; SLF4J dep add; startForCrashSimulation shares wiring.

## WUCP Phase 2 Closeout Entries — M3.6a + M3.6b (2026-05-20)

### M3.6a — Profile-Driven Persistence Configuration
- **Status:** DONE
- **Date:** 2026-05-20
- **Scope:** Wired `DeploymentProfile` (3→6 fields: added `busyTimeoutMs`, `lockingMode`, `readThreadCount`) through `PersistenceConfig` into `DatabaseExecutor`. SQLite PRAGMAs now profile-driven. `LockingMode` enum created (NORMAL, EXCLUSIVE). `PersistenceTestHarness` and `IntegrationTestHarness` updated to pass `PersistenceConfig.HOME_DEFAULT`. 14 files (1 new, 13 modified).
- **Tests:** 4 per-profile PRAGMA verification tests + 1 locking_mode default test in `DatabaseExecutorTest`.
- **Build gate:** DEFERRED to Nick (resolved GREEN 2026-05-20).
- **Audit findings closed:** C-01, D1-05, D1-13, D2-11, D5-04.
- **Decisions applied:** DEC-M3-16 (composition-root visibility strategy — applied in M3.6b).

### M3.6b — EventBusConfig + InProcessEventBus Visibility
- **Status:** DONE
- **Date:** 2026-05-20
- **Commit:** `df2743a`
- **Scope:** `EventBusConfig` record (2 fields: `replayQueueCapacity`, `publisherBlockedDepthThreshold`; `HOME_DEFAULT` constant). `ReplayWindowQueue` capacity parameterized (default 10,000 via no-arg; custom via `ReplayWindowQueue(int)`). `InProcessEventBus` promoted to `public` (DEC-M3-16). New canonical 7-arg constructor accepting `EventBusConfig`. `InProcessEventBusFactory.createWithConfig(...)`. 8 files (3 new, 5 modified).
- **Tests:** `EventBusConfigTest` (4) + `ReplayWindowQueueTest` (4) + 1 renamed Tier-9 overflow test = 9 tests added/modified.
- **Build gate:** GREEN at commit.
- **Audit findings closed:** D1-07, D4-09.

## WUCP Phase 2 Closeout Entries — M3.6c + M3.6d-a (2026-05-20)

### M3.6c — Per-Module Event-Class Manifests
- **Status:** DONE
- **Date:** 2026-05-20
- **Commit:** `38d3e30`
- **Scope:** `EventTypes.CORE_PRODUCTION_EVENT_CLASSES` (22 classes) + `IntegrationEvents.LIFECYCLE_EVENT_CLASSES` (5 classes) aggregated via `Stream.concat(...).toList()` at composition root. Replaces 27 inline class imports across `AllEventClasses` (core/persistence) and `IntegrationTestHarness` (testing/integration-tests). `IntegrationEvents` is a NEW public final class in `integration/integration-api`. 1 new file + 4 modified across `core/event-model`, `integration/integration-api`, `core/persistence` (test), `testing/integration-tests` (test).
- **Tests:** Refactor-only — no net test additions; existing `EventTypeAnnotationTest`, `IntegrationEventTypeAnnotationTest`, `EventTypeRegistryTest`, `EventPayloadCodecTest`, `JacksonWarmupTest`, `SqliteEventStoreTest`, `SqlitePersistenceLifecycleTest`, `EventCategoryMappingTest` all continue to pass against the new aggregation pattern.
- **Build gate:** GREEN at commit.
- **Closes:** Q3 gap closure (Artifact 1) — per-module event-class manifests aggregated at the composition root.
- **Deviations:** D-1 (`EventTypes` MODIFIED not CREATED — file pre-existed as M2.1 holder for 46 string constants), D-2 (`AllEventClasses.ALL_EVENTS` field name preserved; brief said `ALL` — 6 caller sites would have broken), D-3 (`CORE_EVENTS`/`INTEGRATION_EVENTS` aliases preserved — `EventTypeRegistryTest` references independently).
- **Status:** CLOSED. No follow-up actions.

### M3.6d-a — Composition-Root Satellite Changes
- **Status:** DONE
- **Date:** 2026-05-20
- **Commit:** `25bc23b`
- **Scope:** 18 files (6 created + 9 modified + 3 MODULE_CONTEXT + 1 module-info + 1 build.gradle.kts — split from the count this way reflects what each delivers) across `core/persistence`, `core/event-bus`, `core/state-store`, `lifecycle/lifecycle`. Delivers the independent satellite changes from the original M3.6d brief: SqliteStateStore implements StateCheckpointSource (rename `serialize` → `serializeCheckpoint`, public via interface; class itself stays package-private). QueueSaturationHealthCheck + HealthSignal + HealthLevel promoted to public (DEC-M3-17 — transitive 3-type chain). ReadinessSource public interface in core/state-store (single method `mode() → SubscriberMode`). ReconciliationTest 4 of 5 brief methods (5th `reconciliationRecordsMetadataInDataSlot` deferred as feature gap — OR-M3-13). Tier 9 `reconciliationOnVersionMismatch` un-disabled and implemented. Lifecycle module skeletons: HomeSynapseConfig (public record) + SharedScheduler (package-private final, 50 ms refill + 1 s tick, `safelyInvoke` cadence defence) + ThrowingStateQueryService (package-private final). Module-info `requires transitive` for persistence/event.bus/state-store + non-transitive `requires org.slf4j`. SLF4J follow-up fix applied same-day (canonical M2.2 pattern).
- **Sub-division context:** Original M3.6d brief sub-divided into d-a (this WU) and d-b (next WU) per Option A. Coder pushback identified seven source-vs-brief mismatches: HealthSignal/HealthLevel are package-private (brief said `QueueSaturationHealthCheck` promotion was "clean"); `SqlitePersistenceLifecycle` does not construct `SqliteStateStore`/`SqliteDeadLetterStore`; no `WriteCoordinator.queueSize()` method; no production `SubscriberReadConnectionFactory`; `SubscriberInfo` and `SubscriptionFilter` constructor shapes differ from brief snippets (no `displayName`; 3rd `SubscriptionFilter` arg is `SubjectType` not String).
- **Tests:** SharedSchedulerTest (5 — 4 from brief plus `taskFailureDoesNotSilenceCadence` pinning `safelyInvoke` behaviour) + ReconciliationTest (4) + Tier 9 un-disabled (1) = 10 net @Test additions.
- **Build gate:** GREEN at commit (after SLF4J follow-up fix). Full `./gradlew check` PASS at HEAD, 137 actionable tasks.
- **Audit findings closed:** D3-08 (scheduler wiring via SharedScheduler).
- **Deviations:** D-1 [REVIEW] HealthSignal + HealthLevel promotion (logged as DEC-M3-17). D-2 [INFO] ReconciliationTest 4/5 (OR-M3-13). D-3 [INFO] SharedScheduler secondary `(Runnable, Runnable)` constructor for testability (final collaborators). D-4 [INFO] SharedSchedulerTest 5 tests (brief specified 4). D-5 [INFO] `shutdownTerminatesWithin2Seconds` renamed to `shutdownTerminatesWithoutThrowing` (`NO_DIRECT_TIME_ACCESS`). D-6 [INFO] Major scope reduction from original M3.6d brief per Option A.
- **Status:** CLOSED. Three follow-up items tracked: OR-M3-12 (DEC-M3-17 governance entry — RESOLVED in this closeout), OR-M3-13 (reconciliation metadata feature gap), OR-M3-14 (M3.6d-b prerequisite infrastructure).

---

## Notes

- Milestones are produced just-in-time: each M{x}.{y} is briefed after the prior milestone's WUCP Phase 2 completes.
- This backlog is the high-level roadmap only; the authoritative spec for each milestone lives in its coding instruction.
- Deferred-build-gate risk: if a coder-handoff defers `./gradlew check`, the PM must track it here under the milestone row until resolved.
- Intra-milestone work units (Bus-Fix Piece A, projection-checkpoint wiring, supervisor DLQ wiring) are tracked as standalone rows when they ship as independent commits, even if they don't carry a `M{x}.{y}` identifier. Each still requires a full WUCP Phase 2 closeout.

---

**Last verified against:** `homesynapse-core` commit `dfb045e` on `2026-05-21`.
