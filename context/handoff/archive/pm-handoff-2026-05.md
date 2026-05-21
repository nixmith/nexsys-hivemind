<!--
file: context/handoff/archive/pm-handoff-2026-05.md
purpose: Archived historical PM closeouts evicted from active pm-handoff.md as part of Batch E (2026-05-21).
audience: PM, Coder
update-cadence: frozen
state-type: history
status: ARCHIVED
last-verified: 2026-05-21 against `homesynapse-core` commit `dfb045e`
-->

# PM Handoff — Archive 2026-05

Archived from `context/handoff/pm-handoff.md` on 2026-05-21 (Batch E; PLAN §4b). Covers PM closeouts 2026-05-19 → 2026-05-20.

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

**Deviations:** Scope split. The original Bus-Fix WU as briefed also included (a) enabling the `@Disabled("M3.5a") reconciliationOnVersionMismatch` Tier 9 test in `EventBusContractTest` and (b) fixing the `bus.resume()` VT re-spawn limitation. Both deferred — they require lifecycle wiring that belongs to M3.6.

**WUCP Phase 2 completed (retroactive):**
- [x] PROJECT_SNAPSHOT.md updated (Open Risks "Bus-Fix WU" entry removed; Tracked Gaps #1 and #2 carry forward the deferred portion)
- [x] pm-handoff.md updated (this entry; the prior pm-handoff "Open Risks: Bus-Fix WU" entry is now RESOLVED)
- [x] coder-handoff.md Bus-Fix Piece A entry
- [x] phase-3-milestone-backlog.md row added
- [x] event-bus MODULE_CONTEXT.md updated (commit `fceafe8` includes the table-row move)

**Open risks closed:**
- **Bus-Fix WU — DerivedWriteRateLimit Visibility (tracked 2026-05-18)** → CLOSED 2026-05-18 by `fceafe8`. The split-out Tier 9 test enablement and `bus.resume()` fix are now tracked as M3.6 dependencies, not as standalone risks.

**Next work unit (at the time):** M3.5b (subsequently DONE).
