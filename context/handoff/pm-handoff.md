# PM Session Handoff

**Last updated:** 2026-05-20 (WUCP Phase 2 — M3.6c + M3.6d-a closure, DEC-M3-17 logged, M3.6d sub-divided into d-a + d-b)

## Current Task

None. M3.6a/b/c/d-a all PM-accepted and on `main` (M3.6d-a at `25bc23b`, 2026-05-20). Build GREEN at HEAD (full `./gradlew check` PASS, 137 actionable tasks). WUCP Phase 2 complete for all four sub-WUs. Next work unit is **M3.6d-b** — PersistenceFactory + HomeSynapseCore (composition-root wiring) — PM owes a revised coding instruction addressing OR-M3-14 prerequisite infrastructure gaps.

## Phase 3 Work Unit Status

| Work Unit | Scope | Status | Commit |
|---|---|---|---|
| AMD-33 | DomainEvent permanently non-sealed | DONE 2026-04-10 | `768a4e4` |
| M2.1–M2.5 | Full persistence layer (EventType through SqliteEventStore) | DONE 2026-04-10/11 | `b2c8b78`..`5279e7a` |
| M2 (complete) | SqlitePersistenceLifecycle boot + shutdown | DONE 2026-05-01 | — |
| M2-bridge | AMD-34..37, V001→25 cols, V002 DLQ, V003 snapshots, 10 new types | DONE 2026-05-02 | — |
| D1 spike | WAL Pathology Validation — bounded reader is load-bearing | DONE 2026-05-15 | — |
| AMD-38/39 | AMD-38 APPLIED, AMD-39 WITHDRAWN, DeploymentProfile corrected | DONE 2026-05-15 | — |
| Deliverable 0 | ProjectionAdvancer.advance 3-param signature | DONE 2026-05-16 | — |
| M3 governance | AMD-41/42/43 APPLIED, PLAN-M3-CONSOLIDATED-02, DEC-M3-01..13 | DONE 2026-05-16 | — |
| M3.1 | InProcessEventBus core: mode FSM, isolation, supervisor, DLQ, circuit breaker | DONE 2026-05-17 | — |
| M3.2 | REPLAY→TRANSITION→LIVE bus-side: ReplayDriver, TransitionCoordinator, wiring | DONE 2026-05-17 | `0bade6a`. First CC milestone |
| M3.3 | Backpressure, metrics, observability: BusMetrics, health check, rate limiter | DONE 2026-05-17 | `a5d4b2a`. DEC-M3-14/15. |
| M3.5a | StateProjection vertical slice | DONE 2026-05-18 | `a2aff9c`. DerivedPublishGate adapter seam (G4). Third CC milestone. |
| **Bus-Fix Piece A** | `DerivedWriteRateLimit` package-private → public (one-line visibility change) | **DONE 2026-05-18** | `fceafe8`. Closes M3.5a G4 mismatch. |
| **M3.5b** | StateProjection production persistence — `SqliteStateStore`, `SqliteDeadLetterStore`, `PersistentDlqWriter`, `CheckpointSerializer`, V004 indices, ObjectMapper divergence, three-way atomic write | **DONE 2026-05-18** | `08d0136`. 19 files, +2,674 lines. Independent review PASS w/ 5 non-blocking concerns. |
| **Projection-checkpoint wiring** | `StateCheckpointSource` interface in state-store + 10 MB advisory guardrail | **DONE 2026-05-19** | `56aaa4b`. Closes M3.5b non-blocking concern #1. |
| **Supervisor DLQ wiring** | `SubscriberSupervisor.deliver()` constructs `DeadLetter` and routes through `park(DeadLetter)` | **DONE 2026-05-19** | `ed5862c`. 12 new `SubscriberSupervisorTest` methods. |
| **M3.4a** | Integration-tests module + harness + BurstLoadIT + HeapBudgetIT | **DONE 2026-05-19** | `5ae7912`. New testing module #20. Full check GREEN; profile-gated tests GREEN. |
| **M3.4b** | Pi4SustainedLoadIT, Pi4D1SpikeIT, CrashRecoveryIT, ThrottledWriteCoordinator, pi4-validation.sh | **DONE 2026-05-19** | `adf04d2` |
| **M3.6a** | Profile-driven persistence config (audit C-01, D1-05, D1-13, D2-11, D5-04) | **DONE 2026-05-20** | `17c40b6` |
| **M3.6b** | EventBusConfig + InProcessEventBus visibility (audit D1-07, D4-09; DEC-M3-16) | **DONE 2026-05-20** | `df2743a` |
| **M3.6c** | Per-module event-class manifests (Q3 gap closure) | **DONE 2026-05-20** | `38d3e30` |
| **M3.6d-a** | Composition-root satellite changes (SqliteStateStore→StateCheckpointSource, DEC-M3-17 visibility chain, ReadinessSource, ReconciliationTest 4/5, Tier 9 un-disabled, HomeSynapseConfig + SharedScheduler + ThrowingStateQueryService skeletons, SLF4J wiring) | **DONE 2026-05-20** | `25bc23b` |
| **M3.6d-b** | PersistenceFactory + HomeSynapseCore (composition-root wiring) | **NEXT** | — |

## Design Doc Status

All 14 design documents Locked. Phase 2 interface specification frozen as of 2026-03-20. M3 governance bundle (AMD-41/42/43) APPLIED 2026-05-16. DEC-M3-14/15 added 2026-05-17. PLAN-M3-CONSOLIDATED-02 is the authoritative M3 implementation plan.

### New M3 design artifacts (committed since prior pm-handoff)

| Artifact | Path | Date | Notes |
|---|---|---|---|
| Cross-tier deployment audit | `HomeSynapse_Core_CrossTier_Deployment_Audit.md` (workspace root) | 2026-05-19 | Closed-out audit. Informed M3.6 composition root design. |
| M3 audit gap-closure research (Artifact 1) | `homesynapse-core-docs/research/2026-05-20_M3_Audit_Gap_Closure_v1.md` | 2026-05-20 | Identified and closed audit-trail gaps prior to M3.4b/M3.6. |
| M3.6 Composition Root Design | `homesynapse-core-docs/design/2026-05-20_M3.6_Composition_Root_Design.md` | 2026-05-20 | Authoritative design that M3.6 implements against. |

## Outstanding Coding Instructions

None. PM to produce a **revised M3.6d-b coding instruction** addressing the three prerequisite infrastructure gaps documented in OR-M3-14 below: (a) `SqlitePersistenceLifecycle` constructing `SqliteStateStore` + `SqliteDeadLetterStore` in addition to today's four main stores, (b) `WriteCoordinator.queueSize()` accessor for the bus's writer-queue-depth `IntSupplier`, (c) production `SubscriberReadConnectionFactory` (today only the testFixtures `RecordingReadConnectionFactory` exists). Remaining M3.6 sub-WUs after d-b: M3.6e.1 → M3.6e.2.

## Unresolved Deviations

None requiring PM action. M3.5b's 5 non-blocking concerns (CheckpointSerializer size guardrail, AtomicCheckpointWriter duplication, no concurrent-access tests for SqliteStateStore, no post-shutdown defensive handling, MODULE_CONTEXT type count off-by-one) are tracked under PROJECT_SNAPSHOT "Tracked Gaps" — none block M3.4b. The Supervisor DLQ wiring source-verification audit (`2026-05-19_supervisor-dlq-source-verification.md`) corrected one assumption (A8: `SubjectRef.toString()` returns `"type:id"`, not bare ULID) — incorporated into the coding instruction before execution; no post-hoc cleanup needed.

## Next Tasks (Priority Order)

1. **Produce revised M3.6d-b Claude Code task instruction.** PersistenceFactory + HomeSynapseCore composition-root wiring, augmented with the three prerequisite infrastructure pieces from OR-M3-14. ~10–12 hours estimated Coder time (was 6–8h before discovery; growth attributable to the prerequisite work).
2. **Phase 2 traceability debt** — 10 stub indexes remain (docs 02–11, 13, 14). Low priority; batch later.
3. **Knowledge Primer M3.6d-a corrections** — done in this session (event-bus type count + ReadinessSource + lifecycle module map + visibility-promotion gotcha added).

## Open Risks

#### OR-M3-12 — DEC-M3-17 governance entry (NEW 2026-05-20)
- **Severity:** LOW (governance hygiene)
- **Detail:** HealthSignal and HealthLevel were promoted to public alongside QueueSaturationHealthCheck during M3.6d-a because the constructor's `Consumer<HealthSignal>` parameter chain leaks both types and `-Xlint:exports` would have failed otherwise. The promotion shipped with M3.6d-a `25bc23b`; DEC-M3-16 (which authorized only InProcessEventBus + SqlitePersistenceLifecycle) needed an addendum to record the 3-type promotion chain (QueueSaturationHealthCheck + HealthSignal + HealthLevel) as the minimum viable visibility unit.
- **Resolution:** RESOLVED in this WUCP Phase 2 closeout (2026-05-20). DEC-M3-17 entries appended to `HomeSynapse_Current_State.md` §3 ledger, `HomeSynapse_Core_Locked_Decisions.md` Phase 3 milestone section, and `context/decisions/phase-3-cross-module-decisions.md`.

#### OR-M3-13 — ReconciliationRecordsMetadataInDataSlot feature gap (NEW 2026-05-20)
- **Severity:** LOW (feature gap, not regression — AMD-41 §3.2.4 metadata-recording requirement was never fully implemented at any prior milestone)
- **Detail:** `StateProjection.writeCheckpoint(Instant)` passes plain `projectionVersion` to `StateCheckpointSource.serializeCheckpoint(int)`. The interface has no surface to accept `reconciledAt`, `reconciledFromVersion`, `reconciledToVersion`. `SqliteStateStore.serializeCheckpoint(int)` forwards `null` for those three fields to `CheckpointSerializer.serialize(...)`. M3.6d-a's `ReconciliationTest` ships 4 of 5 brief tests; the 5th (`reconciliationRecordsMetadataInDataSlot`) is deferred because it would fail trivially against the current contract. Implementing the feature requires extending the `StateCheckpointSource` interface and threading the metadata through `StateProjection.initialize`'s reconciliation path.
- **Resolution:** Track as a separate enhancement WU — likely M4 scope since it touches the projection's checkpoint contract.

#### OR-M3-14 — M3.6d-b prerequisite infrastructure (NEW 2026-05-20)
- **Severity:** MEDIUM (blocks M3.6d-b until addressed in the coding instruction)
- **Detail:** M3.6d-b requires three pieces of new persistence-layer infrastructure that the original M3.6d brief assumed already existed but do not: (1) `SqlitePersistenceLifecycle` must construct `SqliteStateStore` + `SqliteDeadLetterStore` (today constructs only the 4 main stores: EventStore, EventBusCheckpointStore, ViewCheckpointStore, WriteCoordinator); (2) `WriteCoordinator` interface needs `queueSize()` exposure for the bus's writer-queue-depth `IntSupplier` (DEC-M3-14); (3) a production `SubscriberReadConnectionFactory` implementation (today only the testFixtures `RecordingReadConnectionFactory` exists). PM owes a revised M3.6d-b coding instruction addressing these before issue.
- **Resolution:** PM responsibility for the next session. Estimated work-unit size impact: M3.6d-b grows from 6–8h to 10–12h.

#### M3.4b — Pi4SustainedLoadIT event-count tolerance
- **Severity:** LOW (informational assertion, not load-bearing)
- **Detail:** Task instruction specified ±2% event-count tolerance. Actual implementation uses lower-bound 25%. The ±2% was a calibration error — ThrottledWriteCoordinator's 10ms baseline makes 100 ev/s unachievable. The lag-bound assertion (≤50 events) is the load-bearing check.
- **Resolution:** Accepted by PM. No action needed unless the lag assertion fails in future runs.

#### M3.4b — CrashRecoveryIT Windows @TempDir caveat
- **Severity:** LOW (test infrastructure, not production)
- **Detail:** @TempDir(cleanup = CleanupMode.NEVER) required because abandoned harness holds SQLite file handles on Windows. Temp directories accumulate across test runs.
- **Resolution:** Accepted. OS handles cleanup. No production impact.

#### H2: AtomicCheckpointWriter code duplication (from M3.5b Cowork review)
- **Severity:** LOW (code quality, not correctness)
- **Detail:** Two-way and three-way methods duplicate transaction wrapper. Extract shared `executeInTransaction` helper.
- **Resolution:** Standalone cleanup WU or fold into M3.6d.

#### Supervisor retry loop activation (from supervisor-DLQ-wiring)
- **Severity:** MEDIUM (dead code in production)
- **Detail:** computeBackoff(), sleepForBackoff(), MAX_RETRIES=5 are dead code. Current behavior parks on first failure. Activating requires moving recordCrash() to post-exhaustion path.
- **Resolution:** Separate WU. Not blocking M3.6.

#### bus.resume() does not re-spawn the VT (from M3.2)
- **Severity:** MEDIUM (blocks Tier 9 reconciliationOnVersionMismatch test)
- **Resolution:** Tracked for dedicated bus-fix Piece B WU.

## Decisions Made This Session (2026-05-20)

- **DEC-M3-17 (NEW):** HealthSignal + HealthLevel public visibility (DEC-M3-16 addendum). Required by the `-Xlint:exports` transitive accessibility check on `QueueSaturationHealthCheck`'s public constructor (`Consumer<HealthSignal>` leaks both types). The 3-type chain (QueueSaturationHealthCheck + HealthSignal + HealthLevel) is the minimum viable promotion. APPLIED in M3.6d-a `25bc23b`.
- **M3.6d sub-divided into d-a + d-b (Option A):** Coder pushback during M3.6d execution identified seven source-vs-brief mismatches (visibility gaps in HealthSignal/HealthLevel, missing `WriteCoordinator.queueSize()`, no production `SubscriberReadConnectionFactory`, `SqlitePersistenceLifecycle` does not construct SqliteStateStore/SqliteDeadLetterStore, SubscriberInfo/SubscriptionFilter constructor shapes differ from brief). User chose Option A: ship the independent satellite changes as M3.6d-a, defer the wiring to M3.6d-b after addressing the prerequisite infrastructure.
- **DEC-M3-16 (prior session):** Composition-root visibility strategy. InProcessEventBus → public (applied M3.6b `df2743a`). SqlitePersistenceLifecycle → public factory (ships M3.6d-b). QueueSaturationHealthCheck → promoted to public in M3.6d-a (DEC-M3-17 records the transitive HealthSignal/HealthLevel chain).
- **M3.6e scope expansion approved:** +Javalin server, +3 admin endpoints (M3.5b gap — DlqAdminEndpoint, ProjectionRebuildEndpoint, ProjectionStatusEndpoint), +6 ArchUnit rules. Splits into M3.6e.1 (StateQueryService + REST gate) / M3.6e.2 (admin endpoints + ArchUnit rules).
- **M3.7 ingress:** EventPublisher.publish() directly (no HTTP ingress endpoint).
- **ThrowingStateQueryService stub** lands in M3.6d-a (replaces null return; package-private final, all 5 methods throw `IllegalStateException("StateQueryService not yet wired — available after M3.6e")`).
- **ReadinessFilter:** Javalin `before` handler (option a).
- **Javalin thread pool on DeploymentProfile:** STUDIO(1/4), HOME(2/8), PERFORMANCE(4/16).

## Audit Findings Closure Update (2026-05-20)

- **CLOSED (M3.6a):** C-01, D1-05, D1-13, D2-11, D5-04
- **CLOSED (M3.6b):** D1-07, D4-09
- **CLOSED (M3.6d-a):** D3-08 (`DerivedWriteRateLimit.refill()` + `QueueSaturationHealthCheck.tick()` scheduler wired via `SharedScheduler`)
- **DEFERRED (MINOR / future WU):** D1-02, D1-16, D1-19, D5-08, D5-09

## Critical Path

M3.6d-b → M3.6e.1 → M3.6e.2 → M3.7 (M3.6a/b/c/d-a all DONE 2026-05-20)

## Open Risks/Concerns from M3 Closeout Readiness Deliberation

1. **M3.6e scope (9-12h, largest single WU)** — split into M3.6e.1/e.2 mitigates.
2. **SqlitePersistenceLifecycle factory pattern needed (M3.6d)** — DEC-M3-16. Accessor return types are package-private; direct promotion triggers `-Xlint:exports`.
3. **Admin endpoint gap from M3.5b** — DlqAdminEndpoint, ProjectionRebuildEndpoint, ProjectionStatusEndpoint bundled into M3.6e.2.
4. **6 missing ArchUnit rules** — bundled into M3.6e.2.
5. **@Disabled("M3.5a") reconciliation test** — un-disable in M3.6d.
6. **bus.resume() VT re-spawn** — NOT M3 blocker (tracked for M4).

## Completed Since Last Update (2026-05-20)

| WU | Commit | Date | Scope |
|---|---|---|---|
| M3.6a | `17c40b6` | 2026-05-20 | Profile-driven persistence config — DeploymentProfile 6 fields, LockingMode, PRAGMAs |
| M3.6b | `df2743a` | 2026-05-20 | EventBusConfig + InProcessEventBus public (DEC-M3-16) |
| M3.6c | `38d3e30` | 2026-05-20 | Per-module event-class manifests (Q3 gap closure) |
| M3.6d-a | `25bc23b` | 2026-05-20 | Composition-root satellite changes (DEC-M3-17 visibility chain, ReadinessSource, ReconciliationTest 4/5, Tier 9 un-disabled, lifecycle skeletons, SLF4J wiring) |

## Completed Since Last Update (2026-05-18 through 2026-05-19)

| WU | Commit | Date | Scope |
|---|---|---|---|
| Bus-Fix Piece A | `fceafe8` | 2026-05-18 | DerivedWriteRateLimit visibility promotion |
| M3.5b | `08d0136` | 2026-05-18 | StateProjection production persistence |
| Proj-Checkpoint Wiring | `56aaa4b` | 2026-05-19 | StateCheckpointSource + size guardrail |
| Supervisor DLQ Wiring | `ed5862c` | 2026-05-19 | 11-field DeadLetter + PersistentDlqWriter |
| M3.4a | `5ae7912` | 2026-05-19 | Integration-test scaffold (module 20) |
| M3.4b | `adf04d2` | 2026-05-19 | Sustained-load + crash-recovery tests |

## What Will Be Different Going Forward

- **Freshness preflight** runs at the start of every PM session. If the hivemind is declared stale, the only allowed task is running WUCP Phase 2 retroactively for the last completed work unit. See `project-manager/references/freshness-preflight.md`. **This is exactly what triggered today's session** — 5 work units accumulated PM-side without WUCP Phase 2; this catch-up restored PASS state.
- **Deferred build gate risk tracking** is a PM responsibility. Every coder-handoff that defers `./gradlew check` must be listed here under "Open Risks" until Nick resolves it.
- **No work unit is "done" until both WUCP phases have been executed.** Completion of a work unit is a prerequisite for starting the next.
- **Dual-skill sync check** runs at WUCP Phase 2 step 10. Any edit to files under `ClaudeFolder/nexsys-hivemind/{coder,project-manager}/` must be mirrored into `.claude/skills/nexsys-{coder,project-manager}/`, verified by `diff -rq`. None of today's five WUCP closeouts touched skill files; sync check expected PASS.
- **M3 prompt pattern:** Settled decision points from deliberation documents go into Cowork prompts as fixed constraints (not open questions). STOP-on-Mismatch gates include interface-shape tests. Specify `default` vs abstract for new interface methods. For any type the brief asserts is cross-module accessible, include a visibility-gate that verifies the `public` modifier on the class declaration (lesson from M3.5a G4 — codified in `coding-instruction-format.md`).

---

## M3.6d-a — PM Closeout — 2026-05-20

**Work unit:** M3.6d-a — Composition-Root Satellite Changes
**Coder surface:** Claude Code
**Build gate:** RESOLVED. Full `./gradlew check` GREEN at `25bc23b` (post-SLF4J follow-up fix). 137 actionable tasks (134 executed, 3 up-to-date).

**Scope:** Delivers the independent pieces of the composition root that do NOT depend on persistence-side infrastructure work the original M3.6d brief assumed already existed. `SqliteStateStore implements StateCheckpointSource` (method rename `serialize` → `serializeCheckpoint`, public promotion via interface; class itself stays package-private). `QueueSaturationHealthCheck` + `HealthSignal` + `HealthLevel` promoted to public per DEC-M3-17 (transitive 3-type chain). `ReadinessSource` public interface in `core/state-store` (single method `mode() → SubscriberMode`; consumed by M3.6e's MaterializedStateQueryService for REST/WebSocket readiness gating). `ReconciliationTest` (4 of 5 brief methods; metadata-recording test deferred as feature gap — OR-M3-13). Tier 9 `reconciliationOnVersionMismatch` un-disabled and implemented (subscribe → wait LIVE → unsubscribe → externally reset checkpoint to 0 → re-subscribe → assert 10 events re-replayed). Lifecycle module skeletons: `HomeSynapseConfig` (public record), `SharedScheduler` (package-private final — 50 ms refill + 1 s tick, daemon thread `hs-sched-0`, `safelyInvoke` cadence defence), `ThrowingStateQueryService` (package-private final — all 5 methods throw `IllegalStateException("StateQueryService not yet wired — available after M3.6e")`). Module-info gained `requires transitive` for persistence/event.bus/state-store + non-transitive `requires org.slf4j` for SharedScheduler's internal logging. 18 files (6 new + 12 modified). Same-day SLF4J follow-up fix added `requires org.slf4j` to lifecycle module-info and `implementation(libs.slf4j.api)` to build.gradle.kts (canonical M2.2 pattern from `core/persistence`).

**M3.6d sub-division decision:** original M3.6d brief assumed prerequisites that don't exist: `SqlitePersistenceLifecycle` doesn't construct `SqliteStateStore`/`SqliteDeadLetterStore`; no `WriteCoordinator.queueSize()`; no production `SubscriberReadConnectionFactory`; `HealthSignal`/`HealthLevel` are package-private; `SubscriberInfo`/`SubscriptionFilter` shapes differ from the brief. User chose Option A (sub-divide). M3.6d-a covers the independent satellite changes; M3.6d-b addresses the prerequisite infrastructure plus actual `PersistenceFactory` + `HomeSynapseCore` wiring.

**Deviations:**
- **D-1 [REVIEW]:** HealthSignal + HealthLevel public promotion (not authorized by brief). The 3-type chain was required by `-Xlint:exports` analysis. Logged as DEC-M3-17.
- **D-2 [INFO]:** ReconciliationTest ships 4 of 5 methods (5th deferred as OR-M3-13).
- **D-3 [INFO]:** SharedScheduler has a secondary `(Runnable, Runnable)` constructor for testability (final collaborators cannot be mocked).
- **D-4 [INFO]:** SharedSchedulerTest ships 5 tests; the 5th (`taskFailureDoesNotSilenceCadence`) pins `safelyInvoke` behaviour.
- **D-5 [INFO]:** `shutdownTerminatesWithin2Seconds` renamed to `shutdownTerminatesWithoutThrowing` to honor `NO_DIRECT_TIME_ACCESS`.
- **D-6 [INFO]:** Major scope reduction from original M3.6d brief per Option A.

**Audit findings closed:** D3-08 (scheduler wiring for refill+tick via SharedScheduler).

**Tier 9 gap closed:** the `@Disabled("M3.5a")` reconciliationOnVersionMismatch contract test is now active. M3.2 carry-forward gap #1 (Tier 9 disable) RESOLVED.

**WUCP Phase 2 completed:**
- [x] HomeSynapse_Current_State.md updated
- [x] HomeSynapse_Knowledge_Primer.md updated
- [x] HomeSynapse_Core_Locked_Decisions.md updated (DEC-M3-17 logged)
- [x] PROJECT_SNAPSHOT.md updated
- [x] pm-handoff.md updated (this entry)
- [x] coder-handoff.md "FOUR OPEN" correction (now ZERO OPEN; all four 2026-05-20 WUs resolved at commit)
- [x] phase-3-milestone-backlog.md M3.6d-a marked DONE; M3.6d sub-divide noted; M3.6d-b NEXT
- [x] 2026-W21 weekly plan updated
- [x] context/decisions/phase-3-cross-module-decisions.md D-08 added (visibility-promotion transitive verification pattern)

**Open risks added:** OR-M3-12 (DEC-M3-17 entry — RESOLVED in this closeout), OR-M3-13 (reconciliation metadata feature gap), OR-M3-14 (M3.6d-b prerequisite infrastructure).

**Next work unit:** M3.6d-b.

---

## M3.6c — PM Closeout — 2026-05-20

**Work unit:** M3.6c — Per-Module Event-Class Manifests (Q3 Gap Closure)
**Coder surface:** Claude Code
**Build gate:** RESOLVED. Full `./gradlew check` GREEN at `38d3e30` (verified against subsequent M3.6d-a build).

**Scope:** `EventTypes.CORE_PRODUCTION_EVENT_CLASSES` (22 classes) + `IntegrationEvents.LIFECYCLE_EVENT_CLASSES` (5 classes) aggregated at composition root via `Stream.concat(...).toList()` (immutable). Replaces 27 inline class imports across `AllEventClasses` (core/persistence) and `IntegrationTestHarness` (testing/integration-tests). `IntegrationEvents` is a NEW public final class in `integration/integration-api`. `EventTypes` modified to add the new `CORE_PRODUCTION_EVENT_CLASSES` field; `EventTypeRegistryTest` references to `AllEventClasses.CORE_EVENTS` / `INTEGRATION_EVENTS` / `ALL_EVENTS` preserved as aliases (renaming would have broken 6 caller sites).

**Deviations:**
- **D-1 [INFO]:** `EventTypes` MODIFIED (not CREATED) — file pre-existed as M2.1 holder for 46 string constants; adding the class list is a natural extension.
- **D-2 [INFO]:** `AllEventClasses.ALL_EVENTS` field name preserved (brief said `ALL`) — 6 caller sites would have broken.
- **D-3 [INFO]:** `CORE_EVENTS` / `INTEGRATION_EVENTS` aliases preserved — `EventTypeRegistryTest` references them independently.

**Closes:** Q3 (gap-closure Artifact 1) — per-module event-class manifests aggregated at the composition root.

**WUCP Phase 2 completed:**
- [x] PROJECT_SNAPSHOT.md updated
- [x] pm-handoff.md updated (this entry)
- [x] coder-handoff.md M3.6c entry
- [x] phase-3-milestone-backlog.md M3.6c marked DONE
- [x] 2026-W21 weekly plan updated

**Open risks:** None.

**Next work unit (at the time):** M3.6d (subsequently sub-divided into M3.6d-a + M3.6d-b).

---

## M3.6b — PM Closeout — 2026-05-20

**Work unit:** M3.6b — EventBusConfig + InProcessEventBus Visibility Promotion
**Coder surface:** Claude Code
**Build gate:** RESOLVED. `./gradlew check` + `:core:event-bus:check` + `:testing:integration-tests:test -PpiProfile=throttled` GREEN.

**Scope:** Created `EventBusConfig` record (2 fields: `replayQueueCapacity`, `publisherBlockedDepthThreshold`) with `HOME_DEFAULT = new EventBusConfig(10_000, 5_000)`. Parameterized `ReplayWindowQueue` capacity via constructor. Promoted `InProcessEventBus` from package-private to `public` per DEC-M3-16 (composition-root visibility strategy). New canonical public 7-arg constructor. `PUBLISHER_BLOCKED_DEPTH_THRESHOLD` replaced by instance field from config. `InProcessEventBusFactory` gained `createWithConfig(...)`. 8 files touched (3 created, 5 modified). 9 tests added/modified. Tenth Claude Code work unit.

**Deviations:** None. All four SD constraints satisfied (SD-1 defaults preserved, SD-2 two-field config, SD-3 backward compat, SD-4 DEC-M3-16 visibility).

**Audit findings closed:** D1-07, D4-09.

**WUCP Phase 2 completed:**
- [x] HomeSynapse_Current_State.md updated
- [x] HomeSynapse_Knowledge_Primer.md updated
- [x] PROJECT_SNAPSHOT.md updated
- [x] pm-handoff.md updated (this entry)
- [x] core/event-bus/MODULE_CONTEXT.md updated (Coder Phase 1)
- [x] coder-handoff.md M3.6b entry + points to M3.6c

**Open risks:** None.

---

## M3.6a — PM Closeout — 2026-05-20

**Work unit:** M3.6a — Profile-Driven Persistence Configuration
**Coder surface:** Claude Code
**Build gate:** RESOLVED. `./gradlew check` + `:core:persistence:check` + `:testing:integration-tests:test -PpiProfile=throttled` GREEN.

**Scope:** Wired `DeploymentProfile` through `PersistenceConfig` into `DatabaseExecutor`. SQLite PRAGMAs now render from the active deployment profile instead of hardcoded literals. `DeploymentProfile` gained 3 new fields: `busyTimeoutMs` (long), `lockingMode` (`LockingMode` enum — package-private: NORMAL, EXCLUSIVE), `readThreadCount` (int). `DatabaseExecutor` constructor changed from `(int readThreadCount, Clock)` to `(DeploymentProfile, Clock)`. Hardcoded `CONNECTION_PRAGMAS` replaced by `connectionPragmas(DeploymentProfile)` rendering method. `SqlitePersistenceLifecycle` constructor changed from `(Path, int, Clock, HomeId, List)` to `(Path, PersistenceConfig, Clock, HomeId, List)`. `PersistenceLifecycle` interface Javadoc scrubbed of SQLite-specific language. PRAGMA value shift: old hardcoded values were PERFORMANCE-tier; under `PersistenceConfig.HOME_DEFAULT` they drop to 16 MB cache / 256 MB mmap (architecturally correct — this was C-01's purpose). 14 files touched (1 created, 13 modified). 5 tests added/modified. Ninth Claude Code work unit.

**Deviations:** 7 additional test files beyond the brief's list were updated (constructor signature ripple). Zero spec deviations.

**Audit findings closed:** C-01, D1-05, D1-13, D2-11, D5-04.

**WUCP Phase 2 completed:**
- [x] HomeSynapse_Current_State.md updated
- [x] HomeSynapse_Knowledge_Primer.md updated
- [x] PROJECT_SNAPSHOT.md updated
- [x] pm-handoff.md updated (this entry)
- [x] core/persistence/MODULE_CONTEXT.md updated (Coder Phase 1)
- [x] coder-handoff.md M3.6a entry

**Open risks:** None.

---

## M3.4b — PM Closeout — 2026-05-19 (retroactive)

**Work unit:** M3.4b — Sustained-Load + Crash-Recovery Integration Tests
**Coder surface:** Claude Code
**Build gate:** RESOLVED. Full `./gradlew check` GREEN + `./gradlew :testing:integration-tests:test -PpiProfile=throttled -PsustainedMinutes=10` GREEN on `adf04d2`.

**Scope:** ThrottledWriteCoordinator disk test double in persistence testFixtures (baseline 10ms + 200ms spike at 0.5%, decorator pattern via `Function<WriteCoordinator, WriteCoordinator>`). Three new integration tests: Pi4SustainedLoadIT (100 ev/s sustained), Pi4D1SpikeIT (50 ev/s with D1 spike simulation, 30 min), CrashRecoveryIT (5,000 events, abandon at ≥3,000, restart, verify exactly-once delivery from checkpoint). DatabaseExecutor and SqlitePersistenceLifecycle gain package-private decorator constructor overloads. SLF4J API added to integration-tests test classpath. scripts/pi4-validation.sh on-device runner. 9 unit tests (ThrottledWriteCoordinatorTest) + 3 integration tests. Eighth work unit executed via Claude Code.

**PM-accepted deviations:**
- Event-count assertion loosened from ±2% to lower-bound 25% (calibration error in task instruction — ThrottledWriteCoordinator's 10ms baseline makes 100 ev/s unachievable).
- @TempDir(cleanup = CleanupMode.NEVER) for CrashRecoveryIT (abandoned harness holds SQLite file handles on Windows).
- SLF4J API dependency added to integration-tests build.gradle.kts (not in original task instruction scope).
- `startForCrashSimulation` shares wiring with `start` (semantic alias, not separate code path).
- ThrottledWriteCoordinatorTest in src/test/ (not testFixtures).

**WUCP Phase 2 completed (retroactive):**
- [x] PROJECT_SNAPSHOT.md updated
- [x] pm-handoff.md updated (this entry)
- [x] coder-handoff.md M3.4b entry
- [x] phase-3-milestone-backlog.md M3.4b marked DONE
- [x] 2026-W21 weekly plan updated
- [x] testing/integration-tests/MODULE_CONTEXT.md populated
- [x] HomeSynapse_Current_State.md updated
- [x] core/persistence/MODULE_CONTEXT.md updated (Coder Phase 1 — ThrottledWriteCoordinator, decorator gotcha)
- [x] core/event-bus/MODULE_CONTEXT.md updated (Coder Phase 1 — InProcessEventBusFactory.createWithMetrics)

**Open risks:** See Open Risks section above (two LOW, two MEDIUM).

**Next work unit:** M3.6a.

---

## M3.4a — PM Closeout — 2026-05-19 (retroactive)

**Work unit:** M3.4a — Integration Test Module Scaffold + Harness + first 2 IT tests
**Coder surface:** Claude Code
**Build gate:** RESOLVED. Full `./gradlew check` GREEN on `5ae7912`. Profile-gated tests also GREEN: `./gradlew :testing:integration-tests:test -PpiProfile=throttled` (BurstLoadIT + HeapBudgetIT).

**Scope:** New `testing/integration-tests` module (#20). `module-info.java` (empty `com.homesynapse.it` named module — tests run on the unnamed-module classpath). `build.gradle.kts` (Pi-profile-gated test task with `-Xmx256m -Xms256m -XX:ActiveProcessorCount=4 -XX:+UseG1GC -XX:MaxGCPauseMillis=100`; optional `-PsustainedMinutes` system property plumbed). `IntegrationTestHarness` composes `PersistenceTestHarness.start(...)` + `InProcessEventBusFactory.create(...)` + `RecordingReadConnectionFactory` against a `@TempDir` SQLite path; exposes the full canonical 27-event class list. `BurstLoadIT` (500-event burst, 6 assertions). `HeapBudgetIT` (3,000-entity heap bound, 4 assertions). `testFixturesApi` deps added to persistence so cross-module fixtures are visible at compile time.

**Deviations:** None reported.

**WUCP Phase 2 completed (retroactive):**
- [x] PROJECT_SNAPSHOT.md updated
- [x] pm-handoff.md updated (this entry)
- [x] coder-handoff.md M3.4a entry
- [x] phase-3-milestone-backlog.md M3.4a marked DONE, M3.4b NEXT
- [x] 2026-W21 weekly plan updated
- [ ] HomeSynapse_Current_State.md — update at next refresh cadence
- [ ] Dual skill-location sync: no skill changes in M3.4a — verify `diff -rq` at next session start
- [ ] Traceability index updates: deferred (Phase 2 traceability debt batch)

**Open risks:** None.

**Next work unit:** M3.4b.

---

## Supervisor DLQ Wiring — PM Closeout — 2026-05-19 (retroactive)

**Work unit:** Supervisor DLQ Wiring
**Coder surface:** Claude Code
**Build gate:** RESOLVED. Full `./gradlew check` GREEN on `ed5862c`.

**Scope:** `SubscriberSupervisor.deliver()` constructs `DeadLetter` (11 fields) instead of `DlqEntry` (6 fields) in the `RuntimeException` catch block. Routes through `dlq.park(DeadLetter)` — dual write to the in-memory ring AND the `PersistentDlqWriter`. Field construction: `subscriberId = this.subscriberId`, `sequenceKey = envelope.subjectRef().toString()` (yields `"entity:01HXYZ..."` per source verification A8), `eventPosition = envelope.globalPosition()`, `eventId = envelope.eventId().value()` (unwrap `EventId` → `Ulid`), `causeClass = e.getClass().getName()`, `causeMessage = e.getMessage() != null ? e.getMessage() : ""` (null-guard per Watch-Out #3), `attemptCount = 1` (single-attempt semantics — retry loop is M3.2-deferred dead code), `firstSeenAt = lastAttemptAt = clock.instant()`, `diagnostics = null`. `InProcessEventBus.subscribeRuntime()` upgraded the DLQ identity to `new SubscriberDlq(info.subscriberId(), PersistentDlqWriter.noop())`. `TransitionCoordinator.park(DlqEntry)` deliberately preserved for the `CAUGHT_UP_TRANSITION_MARKER = -1L` synthetic case (DeadLetter validates `eventPosition >= 0`). 12 new `SubscriberSupervisorTest` methods (the supervisor had no dedicated test class prior to this WU).

**Deviations:** None — the source-verification audit (`context/audits/2026-05-19_supervisor-dlq-source-verification.md`) was incorporated into the coding instruction before execution. All 9 assumptions confirmed (1 corrected pre-flight: A8 `SubjectRef.toString()` returns `"type:id"`, not bare ULID).

**WUCP Phase 2 completed (retroactive):**
- [x] PROJECT_SNAPSHOT.md updated
- [x] pm-handoff.md updated (this entry)
- [x] coder-handoff.md supervisor DLQ wiring entry
- [x] phase-3-milestone-backlog.md row added
- [x] event-bus MODULE_CONTEXT.md updated for DLQ identity upgrade (Coder Phase 1)

**Open risks:** None.

**Tracked gaps (carry forward to PROJECT_SNAPSHOT.md):**
- Retry loop remains dead code (`MAX_RETRIES = 5`, `computeBackoff`, `sleepForBackoff`). Restructuring belongs to M3.2-followup or M3.6.
- Crash window currently counts each `RuntimeException` as a crash. When the retry loop lands, `recordCrash()` must move from per-attempt to post-exhaustion to preserve "one poison event = one crash."

---

## Projection-Checkpoint Wiring — PM Closeout — 2026-05-19 (retroactive)

**Work unit:** Projection-Checkpoint Wiring
**Coder surface:** Claude Code
**Build gate:** RESOLVED. Full `./gradlew check` GREEN on `56aaa4b`.

**Scope:** `StateCheckpointSource` interface introduced in state-store (`Optional<byte[]> serializeCheckpoint(int projectionVersion)`). Advisory 10 MB checkpoint-size guardrail in `StateProjection` (WARN log + structured metric when exceeded; no hard fail). Wires `StateProjection` to call `source.serializeCheckpoint(projectionVersion)` instead of holding the byte[0] stub from the vertical slice.

**Deviations:** None.

**WUCP Phase 2 completed (retroactive):**
- [x] PROJECT_SNAPSHOT.md updated (Tracked Gap #7 closure noted — composition root still owes ALWAYS-configured ObjectMapper wiring, which is M3.6 scope)
- [x] pm-handoff.md updated (this entry)
- [x] coder-handoff.md projection-checkpoint wiring entry
- [x] phase-3-milestone-backlog.md row added
- [x] state-store MODULE_CONTEXT.md updated (Coder Phase 1) — added `StateCheckpointSource`, byte[0] stub deprecation note, projectionVersion authoritative source

**Open risks:** None.

**Tracked gaps (carry forward):**
- Composition root for ALWAYS-configured ObjectMapper wiring → M3.6.

---

## M3.5b — PM Closeout — 2026-05-19 (retroactive)

**Work unit:** M3.5b — StateProjection Production Persistence
**Coder surface:** Claude Code
**Build gate:** RESOLVED. Module-level GREEN on commit (Coder ran `./gradlew :core:event-bus:check :core:persistence:check :core:state-store:check`). Full `./gradlew check` GREEN on Nick's machine, confirmed via the subsequent commits (`56aaa4b`, `ed5862c`, `5ae7912`) all building clean on top.

**Scope:** `SqliteStateStore` (ConcurrentHashMap-backed materialized view + checkpoint-driven recovery), `SqliteDeadLetterStore` (UPSERT on `(subscriber_id, event_position)`, frozen `first_seen_at`), `PersistentDlqWriter` interface (with `noop()` factory), `CheckpointSerializer` with Jackson JSON (preserves null `staleAfter` and null attribute values; explicit `HashMap.put` avoidance of `Map.copyOf` which throws on nulls), `CheckpointData` record, `AtomicCheckpointWriter.writeAtomicCheckpointWithDlqPark()` three-way atomic write (subscriber checkpoint + view checkpoint + DLQ park, all in one transaction), V004 DLQ operational indices migration, `ObjectMapper` divergence (NON_NULL for events via `PersistenceObjectMapper.create()`; ALWAYS for checkpoints, constructed at composition time). 19 files, +2,674 insertions.

**Deviations:** None blocking. Independent review (`context/audits/2026-05-18_m3.5b-review-report.md`) returned PASS with 5 non-blocking concerns, all tracked under PROJECT_SNAPSHOT "Tracked Gaps." Items 1, 2, 3, 4, 11, 12 in the snapshot map to review findings 1, 2 (CheckpointSerializer size — closed by projection-checkpoint wiring 10 MB guardrail), 12 (duplication), 14 (no concurrent tests for SqliteStateStore), 15 (post-shutdown defensive handling), and 13 (AtomicCheckpointWriter duplication) respectively. Item 5 in PROJECT_SNAPSHOT (publish-latency metric is bus-side only) is a pre-existing M3.3 finding, not M3.5b.

**WUCP Phase 2 completed (retroactive):**
- [x] PROJECT_SNAPSHOT.md updated
- [x] pm-handoff.md updated (this entry)
- [x] coder-handoff.md M3.5b entry
- [x] phase-3-milestone-backlog.md M3.5b marked DONE
- [x] event-bus, persistence, state-store MODULE_CONTEXT.md updated (Coder Phase 1)
- [x] Independent review report filed at `context/audits/2026-05-18_m3.5b-review-report.md`

**Open risks:** None.

**Tracked gaps (carry forward — all non-blocking):**
1. CheckpointSerializer 10 MB advisory guardrail — closed by projection-checkpoint wiring (`56aaa4b`).
2. `AtomicCheckpointWriter` code duplication between two-way and three-way methods.
3. No concurrent-access tests for `SqliteStateStore` (ConcurrentHashMap backing provides correctness by construction).
4. No post-shutdown defensive handling in `SqliteDeadLetterStore` (sibling stores share the pattern).
5. event-bus MODULE_CONTEXT type count clarification (32 top-level vs 35 including inner types — see supervisor DLQ wiring source-verification audit §7 for the definitive count). Header documentation should clarify the convention.

---

## Bus-Fix Piece A — PM Closeout — 2026-05-19 (retroactive)

**Work unit:** Bus-Fix Piece A — `DerivedWriteRateLimit` visibility promotion
**Coder surface:** Nick (direct one-line edit)
**Build gate:** RESOLVED — implicit via subsequent M3.5b build GREEN on top.

**Scope:** Single class declaration changed from package-private to `public` (with `acquire()` and `refill()` accessors). MODULE_CONTEXT update moved the row from the package-private table to the public table; row text now describes the promotion and notes which accessors remain package-private. Closes the G4 mismatch from M3.5a — cross-module consumers (composition root, state-store `DerivedPublishGate` method reference) can now reach the type directly. The `DerivedPublishGate` adapter seam introduced in M3.5a remains in place (the seam is independent of visibility; it isolates the bus-side rate-limit primitive from state-store callers via a narrow interface).

**Deviations:** Scope split. The original Bus-Fix WU as briefed also included (a) enabling the `@Disabled("M3.5a") reconciliationOnVersionMismatch` Tier 9 test in `EventBusContractTest` and (b) fixing the `bus.resume()` VT re-spawn limitation. Both deferred — they require lifecycle wiring that belongs to M3.6. Tracked under PROJECT_SNAPSHOT "Tracked Gaps" #1 and #2.

**WUCP Phase 2 completed (retroactive):**
- [x] PROJECT_SNAPSHOT.md updated (Open Risks "Bus-Fix WU" entry removed; Tracked Gaps #1 and #2 carry forward the deferred portion)
- [x] pm-handoff.md updated (this entry; the prior pm-handoff "Open Risks: Bus-Fix WU" entry is now RESOLVED)
- [x] coder-handoff.md Bus-Fix Piece A entry
- [x] phase-3-milestone-backlog.md row added
- [x] event-bus MODULE_CONTEXT.md updated (commit `fceafe8` includes the table-row move)

**Open risks closed:**
- **Bus-Fix WU — DerivedWriteRateLimit Visibility (tracked 2026-05-18)** → CLOSED 2026-05-18 by `fceafe8`. The split-out Tier 9 test enablement and `bus.resume()` fix are now tracked as M3.6 dependencies, not as standalone risks.

**Next work unit (at the time):** M3.5b (subsequently DONE).
