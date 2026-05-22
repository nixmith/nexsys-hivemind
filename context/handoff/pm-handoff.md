<!--
file: context/handoff/pm-handoff.md
purpose: PM session continuity — current task, work-unit status, open risks, outstanding instructions.
audience: PM, Coder
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-05-22 against commit dfb045e
-->

# PM Session Handoff

**Last updated:** 2026-05-22 (WUCP Phase 2 — M3.6d-b closure, OR-M3-14 RESOLVED, OQ-05-03 RESOLVED)

## Current Task

None. M3.6a/b/c/d-a/d-b all PM-accepted and on `main` (M3.6d-b at `dfb045e`, 2026-05-21). Build GREEN at HEAD (full `./gradlew check` PASS). WUCP Phase 2 complete for all five M3.6 sub-WUs through d-b. Next work unit is **M3.6e.1** — StateQueryService + REST gate (M3.6 capstone, first of two e sub-WUs).

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
| **M3.6d-b** | PersistenceFactory + HomeSynapseCore (composition-root wiring) — WriteCoordinator.queueSize(), SqliteSubscriberReadConnectionFactory, SqlitePersistenceLifecycle 6-store expansion, PersistenceFactory public gateway, HomeSynapseCore 12-step bootstrap | **DONE 2026-05-21** | `dfb045e` (4-commit cohort: `a33ee40`..`dfb045e`) |
| **M3.6e.1** | StateQueryService + REST gate (M3.6 capstone) | **NEXT** | — |

## Design Doc Status

All 14 design documents Locked. Phase 2 interface specification frozen as of 2026-03-20. M3 governance bundle (AMD-41/42/43) APPLIED 2026-05-16. DEC-M3-14/15 added 2026-05-17. PLAN-M3-CONSOLIDATED-02 is the authoritative M3 implementation plan.

### New M3 design artifacts (committed since prior pm-handoff)

| Artifact | Path | Date | Notes |
|---|---|---|---|
| Cross-tier deployment audit | `nexsys-hivemind/context/audits/2026-05-19_cross-tier-deployment-audit.md` | 2026-05-19 | Closed-out audit. Informed M3.6 composition root design. |
| M3 audit gap-closure research (Artifact 1) | `homesynapse-core-docs/research/2026-05-20_M3_Audit_Gap_Closure_v1.md` | 2026-05-20 | Identified and closed audit-trail gaps prior to M3.4b/M3.6. |
| M3.6 Composition Root Design | `homesynapse-core-docs/design/2026-05-20_M3.6_Composition_Root_Design.md` | 2026-05-20 | Authoritative design that M3.6 implements against. |

## Outstanding Coding Instructions

None. M3.6d-b delivered and PM-accepted. PM to produce **M3.6e.1 coding instruction** (StateQueryService + REST gate) this session. Remaining M3.6 sub-WUs: M3.6e.1 → M3.6e.2.

## Unresolved Deviations

None requiring PM action. M3.5b's 5 non-blocking concerns (CheckpointSerializer size guardrail, AtomicCheckpointWriter duplication, no concurrent-access tests for SqliteStateStore, no post-shutdown defensive handling, MODULE_CONTEXT type count off-by-one) are tracked under PROJECT_SNAPSHOT "Tracked Gaps" — none block M3.4b. The Supervisor DLQ wiring source-verification audit (`2026-05-19_supervisor-dlq-source-verification.md`) corrected one assumption (A8: `SubjectRef.toString()` returns `"type:id"`, not bare ULID) — incorporated into the coding instruction before execution; no post-hoc cleanup needed.

## Next Tasks (Priority Order)

1. **Produce M3.6e.1 Claude Code task instruction.** StateQueryService + REST gate — M3.6 capstone. Scope: `MaterializedStateQueryService` implementing `StateQueryService`, `ReadinessFilter` Javalin `before` handler, Javalin server bootstrap in `HomeSynapseCore`, thread pool sizing on `DeploymentProfile`. Estimated 4–5h Coder time.
2. **M3.6e.2 coding instruction** (after M3.6e.1 ships). Admin endpoints (DlqAdminEndpoint, ProjectionRebuildEndpoint, ProjectionStatusEndpoint) + 6 ArchUnit rules.
3. **Phase 2 traceability debt** — 10 stub indexes remain (docs 02–11, 13, 14). Low priority; batch later.

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
- **Resolution:** RESOLVED 2026-05-21. All three prerequisite pieces shipped as part of the M3.6d-b 4-commit cohort: `WriteCoordinator.queueSize()` at `a33ee40`, production `SqliteSubscriberReadConnectionFactory` at `a59b64e`, `SqlitePersistenceLifecycle` 6-store expansion + `PersistenceFactory` at `725353d`, `HomeSynapseCore` composition root at `dfb045e`. Build GREEN at `dfb045e`.

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

## Decisions Made This Session (2026-05-22)

- **OR-M3-14 RESOLVED:** All three prerequisite infrastructure pieces shipped in M3.6d-b's 4-commit cohort. See OR-M3-14 entry above.
- **OQ-05-03 RESOLVED:** The three prerequisite gaps were bundled into M3.6d-b (not split into a separate WU).

### Decisions from prior sessions (carried for reference)

- **DEC-M3-17 (2026-05-20):** HealthSignal + HealthLevel public visibility (DEC-M3-16 addendum). APPLIED in M3.6d-a `25bc23b`.
- **DEC-M3-16 (2026-05-20):** Composition-root visibility strategy. InProcessEventBus → public (M3.6b `df2743a`). SqlitePersistenceLifecycle → factory pattern via PersistenceFactory (M3.6d-b `725353d`). QueueSaturationHealthCheck + HealthSignal + HealthLevel → public (M3.6d-a `25bc23b`, DEC-M3-17).
- **M3.6e scope expansion approved:** +Javalin server, +3 admin endpoints (M3.5b gap — DlqAdminEndpoint, ProjectionRebuildEndpoint, ProjectionStatusEndpoint), +6 ArchUnit rules. Splits into M3.6e.1 (StateQueryService + REST gate) / M3.6e.2 (admin endpoints + ArchUnit rules).
- **M3.7 ingress:** EventPublisher.publish() directly (no HTTP ingress endpoint).
- **ReadinessFilter:** Javalin `before` handler (option a).
- **Javalin thread pool on DeploymentProfile:** STUDIO(1/4), HOME(2/8), PERFORMANCE(4/16).

## Audit Findings Closure Update (2026-05-20)

- **CLOSED (M3.6a):** C-01, D1-05, D1-13, D2-11, D5-04
- **CLOSED (M3.6b):** D1-07, D4-09
- **CLOSED (M3.6d-a):** D3-08 (`DerivedWriteRateLimit.refill()` + `QueueSaturationHealthCheck.tick()` scheduler wired via `SharedScheduler`)
- **DEFERRED (MINOR / future WU):** D1-02, D1-16, D1-19, D5-08, D5-09

## Critical Path

M3.6e.1 → M3.6e.2 → M3.7 (M3.6a/b/c/d-a/d-b all DONE; d-b at `dfb045e` 2026-05-21)

## Open Risks/Concerns from M3 Closeout Readiness Deliberation

1. **M3.6e scope (9-12h, largest single WU)** — split into M3.6e.1/e.2 mitigates.
2. ~~**SqlitePersistenceLifecycle factory pattern needed (M3.6d)** — DEC-M3-16.~~ RESOLVED: `PersistenceFactory` public gateway shipped M3.6d-b `725353d`.
3. **Admin endpoint gap from M3.5b** — DlqAdminEndpoint, ProjectionRebuildEndpoint, ProjectionStatusEndpoint bundled into M3.6e.2.
4. **6 missing ArchUnit rules** — bundled into M3.6e.2.
5. ~~**@Disabled("M3.5a") reconciliation test** — un-disable in M3.6d.~~ RESOLVED: un-disabled in M3.6d-a `25bc23b`.
6. **bus.resume() VT re-spawn** — NOT M3 blocker (tracked for M4).

## Completed Since Last Update (2026-05-22)

| WU | Commit | Date | Scope |
|---|---|---|---|
| M3.6d-b | `dfb045e` | 2026-05-21 | PersistenceFactory + HomeSynapseCore composition-root wiring (4-commit cohort: `a33ee40`..`dfb045e`). WriteCoordinator.queueSize(), SqliteSubscriberReadConnectionFactory, SqlitePersistenceLifecycle 6-store expansion, PersistenceFactory public gateway, HomeSynapseCore 12-step bootstrap. 20 files, +1,432 lines. OR-M3-14 RESOLVED. |

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

## M3.6d-b — PM Closeout — 2026-05-22

**Work unit:** M3.6d-b — PersistenceFactory + HomeSynapseCore Composition-Root Wiring
**Coder surface:** Claude Code
**Build gate:** RESOLVED. Full `./gradlew check` GREEN at `dfb045e`. Build confirmed by Nick.

**Scope:** Delivers the composition-root wiring deferred from M3.6d-a, plus the three OR-M3-14 prerequisite infrastructure pieces. Shipped as a 4-commit cohort:

1. **`a33ee40` — WriteCoordinator.queueSize():** Added `int queueSize()` to the `WriteCoordinator` interface and implementation, exposing the internal `AsyncWriteQueue` size for the bus's writer-queue-depth `IntSupplier` (DEC-M3-14).
2. **`a59b64e` — Production SqliteSubscriberReadConnectionFactory:** New `SqliteSubscriberReadConnectionFactory` (public) + `SqliteSubscriberReadExecutor` (package-private) in `core/persistence`. Provides production `SubscriberReadConnectionFactory` implementation (previously only testFixtures `RecordingReadConnectionFactory` existed).
3. **`725353d` — PersistenceFactory + SqlitePersistenceLifecycle 6-store expansion:** `PersistenceFactory` (public final, implements `AutoCloseable`) wraps package-private `SqlitePersistenceLifecycle` per DEC-M3-16 factory pattern. `SqlitePersistenceLifecycle` expanded from 4 stores to 6 (added `SqliteStateStore` + `SqliteDeadLetterStore`). 8 accessor methods on `PersistenceFactory`. Static `start(Path, PersistenceConfig, Clock, HomeId, List<Class<? extends DomainEvent>>)` factory.
4. **`dfb045e` — HomeSynapseCore composition root:** Public final class implementing `ReadinessSource`. 4-arg constructor `(Path, HomeSynapseConfig, Clock, HomeId)`. 12-step bootstrap sequence: PersistenceFactory.start → BusMetrics.jfr → InProcessEventBus(7-arg) → DerivedWriteRateLimit → StateProjection.create(11-param) → subscribeRuntime → healthSignalHandler → QueueSaturationHealthCheck → SharedScheduler → started=true → CompletableFuture.completedFuture. NO_OP_DERIVATION (OR-M3-15) and NO_OP_ADVANCER (OR-M3-16) stubs. `stateQueryService()` returns `ThrowingStateQueryService` placeholder. `stop()` tears down in reverse order. Module-info gained `requires com.homesynapse.integration` (non-transitive, for `IntegrationEvents` aggregation).

**Stats:** 20 files changed, +1,432 insertions, -14 deletions across persistence and lifecycle modules.

**Deviations:** None. All shipped code matches the revised M3.6d-b coding instruction (which incorporated OR-M3-14 prerequisite infrastructure).

**OR-M3-14 RESOLVED:** All three prerequisite infrastructure gaps closed — `WriteCoordinator.queueSize()` (`a33ee40`), `SqliteSubscriberReadConnectionFactory` (`a59b64e`), `SqlitePersistenceLifecycle` 6-store expansion (`725353d`).

**OQ-05-03 RESOLVED:** The three prerequisite gaps were bundled into M3.6d-b (not split into a separate WU).

**WUCP Phase 2 completed:**
- [x] PROJECT_SNAPSHOT.md updated (type counts, code state, tracked gaps closed, M3.6d-b row)
- [x] pm-handoff.md updated (this entry)
- [x] coder-handoff.md updated
- [x] open-questions.md OQ-05-03 moved to Resolved
- [x] phase-3-milestone-backlog.md M3.6d-b marked DONE; M3.6e.1 NEXT
- [x] 2026-W21 weekly plan updated
- [x] HomeSynapse_Current_State.md updated
- [x] HomeSynapse_Knowledge_Primer.md updated
- [x] Dual-skill sync check

**Next work unit:** M3.6e.1 — StateQueryService + REST gate.

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

## Prior PM Closeouts (archived)

| Closeout | Commit | Date | One-line scope |
|---|---|---|---|
| M3.6c | `38d3e30` | 2026-05-20 | Per-Module Event-Class Manifests — `EventTypes.CORE_PRODUCTION_EVENT_CLASSES` + `IntegrationEvents.LIFECYCLE_EVENT_CLASSES` aggregated at composition root |
| M3.6b | `df2743a` | 2026-05-20 | `EventBusConfig` record + `InProcessEventBus` public visibility (DEC-M3-16) |
| M3.6a | `17c40b6` | 2026-05-20 | Profile-Driven Persistence Configuration — DeploymentProfile threaded through PersistenceConfig → DatabaseExecutor (closes C-01) |
| M3.4b | `adf04d2` | 2026-05-19 retroactive | Sustained-Load + Crash-Recovery ITs; ThrottledWriteCoordinator decorator |
| M3.4a | `5ae7912` | 2026-05-19 retroactive | Integration Test Module Scaffold + Harness (new `testing/integration-tests` module) |
| Supervisor DLQ Wiring | `ed5862c` | 2026-05-19 retroactive | `SubscriberSupervisor.deliver()` → `DeadLetter` via `SubscriberDlq.park`; 12-method test class |
| Projection-Checkpoint Wiring | `56aaa4b` | 2026-05-19 retroactive | `StateCheckpointSource` interface + 10 MB advisory guardrail |
| M3.5b | `08d0136` | 2026-05-19 retroactive | StateProjection Production Persistence — `SqliteStateStore` + `SqliteDeadLetterStore` + `CheckpointSerializer` + V004 |
| Bus-Fix Piece A | `fceafe8` | 2026-05-19 retroactive | `DerivedWriteRateLimit` package-private → public; closes M3.5a G4 mismatch |

Full PM closeout bodies for each row live in `archive/pm-handoff-2026-05.md`.

---

**Last verified against:** `homesynapse-core` commit `dfb045e` on `2026-05-21`.
