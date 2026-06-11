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

Archived from `context/handoff/pm-handoff.md` on 2026-05-21 (Batch E; PLAN §4b). Covers PM closeouts 2026-05-19 → 2026-05-20. **Extended 2026-06-10:** the late-May session records (2026-05-30 → 2026-05-31) were rotated in at the M6.1 sha-reconciliation + cleanup session — see the "Rotated 2026-06-10" section at the bottom; content preserved verbatim.

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

---

# Rotated 2026-06-10 — late-May session records (2026-05-30 → 2026-05-31)

Rotated from active `pm-handoff.md` on 2026-06-10 (monthly cadence per `archive/README.md` §4; executed at the M6.1 sha-reconciliation + cleanup session). Content preserved verbatim.

## This Session — M4.B-S1 WUCP Phase 2 Review + Closeout (2026-05-31, latest)

**Mode-3 Director → WUCP Phase 2.** Received the M4.B-S1 (AMD-44 Stage 1) Claude Code completion report + Nick's build-gate result; reviewed **against source, not the report** (Read tool; sandbox `git`/`grep` distrusted — the bash mount served truncated copies again this session). Freshness preflight at session start: **PASS** after remediating a sandbox-mount working-tree truncation (host repos intact, committed HEADs whole; see cross-agent-notes — bash mount served truncated/locked copies, the file tools read host directly).

- **Verdict: APPROVE.** Read all 9 created + 8 modified files vs AMD-44 §2.1/2.2/2.6/4.1/4.2 + the instruction. `FloorId` mirrors `AreaId` exactly (of/parse/compareTo/toString, null-guarded, Jackson-free); `Floor`/`Area` compact-ctor validation (null-guard id/name/createdAt, name ≤100, `List.copyOf(aliases)` on Floor, nullable icon/floorId per Decisions 7/5); `FloorRegistry`/`AreaRegistry` **interface-only** with full Javadoc — getAll ordering (Decision 8), delete-rejects-when-areas-assigned (Decision 11), LTD-11 ReentrantLock note *with the why*, AreaRegistry read-only (AMD-45 deferral). `hardwareIdentifiers` `List`→`Set` on the three types with new defensive-copy compact ctors; `AreaId` Javadoc de-conflated. **EntityRole + `EntityType`/`Entity`/`ProposedEntity` untouched — Stage-2 fence held.**
- **Coder exceeded spec twice:** FloorRegistry Javadoc explains *why* ReentrantLock not `synchronized` (virtual-thread pinning); the `ProposedDevice` compact ctor copies **both** collections, closing a pre-existing `proposedEntities` immutability leak. Both verified safe (build GREEN; no null-caller).
- **Build gate RESOLVED:** Nick ran `:platform:platform-api:check` (38) + `:core:device-model:check` (26) + full `./gradlew check` (143, incl. ArchUnit `NO_DIRECT_TIME_ACCESS` + `NO_JACKSON_IN_DOMAIN_MODEL` + spotless) → GREEN; **COMMITTED `e73e199`** (17 files; +1026/−42). No open deferred gates.
- **3 `[INFO]` deviations accepted:** new `ProposedDeviceTest` (no prior test to extend); `platform-api/MODULE_CONTEXT.md` update (WUCP "every module touched"); standalone `FloorIdTest` (AreaId is covered by the parameterized `TypedIdTest`). **Minor follow-up logged:** fold `FloorId` into `TypedIdTest`'s parameterized cross-type distinctness list in a future platform/device WU (FloorId is a 9th wrapper; `FloorIdTest` covers it standalone, so coverage is complete).
- **Maintainability/scalability:** typed-ULID `FloorId` makes a deeper hierarchy (Building above Floor / Zone below Area) a same-pattern add; the deliberate 1:N nullable-`floorId` (Decision 5, M:N rejected) is the right base for future 3D/AR spatial mapping; `Set<HardwareIdentifier>` fits multi-protocol discovery. Caveat: Stage 1 is **headless** (no persistence/events/first-boot synthetic-Area) — realizing the model depends on AMD-45 (Area maturation) + registry impls.
- **Closeout applied (this session):** PROJECT_SNAPSHOT (M4.B-S1 COMPLETE, latest `e73e199`); milestone backlog (M4.B-S1 DONE `e73e199`); W22 plan (goal 14); coder-handoff (both M4.B-S1 **and** the stale M4.0b-5 deferred gates flipped RESOLVED — the lag flagged at session start); this handoff; cross-agent-notes (PM pointer). device-model MODULE_CONTEXT 52→56 + platform-api 12→13 were committed by the Coder in `e73e199`.
- **Earlier this session (B Stage 1 issue prep, committed `fc222d8` in hivemind):** issued the M4.B-S1 instruction (milestone tag confirmed by Nick), added the AMD-renumber notice to the Research 6 assessment (AMD-53..63 stale; integration block re-bases 54+), produced the Workstream C gate-status note (`context/planning/2026-05-31_Workstream-C_gate-status.md` — surfaces NQ-1..6 + PM leans + Doc-05 currency + post-B dependency), archived the spent M4.0b-5 review prompt.
- **Next forward:** **(1) cleanup pass** — PLAN-M4-CONSOLIDATED-v2 §3 currency (owes M4.0b-2 re-scope + 0b-3/4a/4b/5 + B-S1 rows); AMD-44 Doc 02 §11.2 floor-event taxonomy + AreaId-Javadoc doc-fold (docs repo, PM task); coder-handoff stale-gate prune; dual-skill-mirror sync. **(2) Workstream B Stage 2 — EntityRole** (AMD-44 §2.5 — enum, `EntityType.legalRoles`/`allows(...)` matrix, `ProposedEntity`/`Entity.entityRole`, `entity_profile_changed` oldRole/newRole; PM authors the Stage-2 coding instruction; note adapter-author coordination is the real Stage-2 cost per AMD-44 §4.1). **(3) Workstream C** — integration-api freeze, gated on Research 6 NQ-1..6 (surfaced) + post-B device model.

## This Session — M4.0b-5 WUCP Phase 2 Review + Closeout (2026-05-31)

**Mode-3 Director → WUCP Phase 2.** Received the M4.0b-5 (AMD-53 timestamp-model unifier) Claude Code completion report + build-gate result and reviewed **against source, not the report**. Freshness preflight at session start: **PASS** (committed state coherent at M4.0b-4b; the AMD-53/M4.0b-5 work was uncommitted working-tree — this session's closeout target; Check 9 STALE-pending-sync expected). Standing sandbox caution reconfirmed hard: the Linux mount served **stale/truncated** copies of synced files (PROJECT_SNAPSHOT short ~20 lines, W22 cut mid-word) and `.git/index.lock` was host-held/unremovable — so every source fact came from the **Read tool on the working tree** (the M4.0b-5 edits are uncommitted, so `git show HEAD:` shows the pre-WU code), and all commits route through host git.

- **Verdict: APPROVE.** Read all five changed files vs AMD-53 and confirmed AMD-53-INV-01/02. Event-time `stamp = eventTimestamp(envelope)` computed once and used for every activity-timestamp write in **every** `applyToState` branch (`state_reported`→`lastUpdated`/`lastReported`; LIVE `state_changed`→`lastChanged`/`lastUpdated`; supersession→`lastUpdated`, `lastChanged` suppressed per AMD-50 §2.2; availability/other→`lastUpdated`); `applyToState` no longer reads `clock`; shared `eventTimestamp` (`eventTime ?? ingestTime`) helper; `initialEntityState(EntityId, Instant seed)` adoption seeding event-time (§1.5 hole closed); `projectionVersion` literal **5** at `HomeSynapseCore`; `clock` retained only for reconciledAt/checkpoint/replay-metric/staleness.
- **The two load-bearing gates verified against source.** **§5 #1** (`liveEqualsReplayFromZeroForAllThreeActivityTimestamps`): multi-entity LIVE≡replay-from-zero asserts the `(lastChanged, lastUpdated, lastReported)` triple is identical per entity AND equals the corpus event-times, with the projection clock (2026-01-01) distinct from the corpus times (2025-09) — a wall-clock regression in any of the three, in either path, fails. **§5 #5** (`reconciliation4to5HealsLegacyWallClockActivityTimestamps`): a legacy wall-clock entity (`stateVersion` 42, attr "999") is healed by a genuine 4→5 reconciliation to all-three event-time == fresh-from-zero replay, `stateVersion`→2, attr→"20" — proving Nick's §2.4 caveat (complete only because `applyToState`'s `state_reported` branch + adoption seeding are event-time, not just the backfill helper; AMD-50-INV-01, no double-increment). §5 #2 (sourcing + null→ingest fallback), #3 (carve-out via the public `materialized` read path), #4 (adoption determinism), #6 (no-op keeps `lastChanged`) all confirmed.
- **Carve-out + scope.** `staleAfter`/`stale` untouched, stay wall-clock (AMD-53-INV-02). Scope §6 clean — host `git status` = exactly 5 core files (`StateProjection`, `HomeSynapseCore`, state-store MODULE_CONTEXT, the two tests); **no** `module-info`/`build.gradle.kts`/codec/event-model/`EntityState`/`stateVersion` change (EntityState still 9-field). NO_DIRECT_TIME_ACCESS holds (new tests inject `Clock`; build GREEN includes ArchUnit).
- **One `[INFO]` ACCEPT:** `backfillTimestamp`→`eventTimestamp` rename (private static, no external surface; Tech-Spec-invited; documents the now-shared rule). No `[REVIEW]`/`[BLOCKING]`; no amendment authored (AMD-53 already RATIFIED).
- **Build gate RESOLVED:** Nick ran `:core:state-store:check` + `:lifecycle:lifecycle:check` (58 tasks) + full `./gradlew check` (143 tasks) → GREEN. No open deferred gates remain.
- **Closeout applied (this session):** PROJECT_SNAPSHOT (M4.0b-5 COMPLETE, latest `c99b425`, `projectionVersion`=5, watermark AMD-53, Workstream A complete); milestone backlog (M4.0b-5 ISSUED→DONE `c99b425`); W22 plan (goal 13 + HEAD/watermark/version); cross-agent-notes (PM pointer); this handoff. state-store MODULE_CONTEXT updated + committed by the Coder. AMD-53-INV-01/02 registered §23 in docs, committed alongside the milestone (watermark AMD-52→AMD-53). **Two cleanups** delivered as the host-git script `apply-cleanups-host.sh` (the sandbox cannot write these repos' git — mount stale + lock held): `.gitattributes` (`text=auto eol=lf`) + renormalization to kill the CRLF/stale-mount churn, and archive of the 10 spent handoff prompts. **At-handoff:** host working trees hold the uncommitted M4.0b-5 (core 5 files) + AMD-53 docs + this closeout; the `c99b425` placeholder is filled by one `sed` with the real core SHA at commit; renormalization runs on the clean tree after.
- **Next forward:** **(1) Workstream B Stage 1** (M4.B-S1, AMD-44 — `FloorId`/`Floor`/`FloorRegistry` + minimal `Area`/`AreaRegistry` + `AreaId` Javadoc + `List`→`Set<HardwareIdentifier>`; EntityRole fenced to Stage 2) — instruction authored + verified vs `72596cb` (device-model/platform-api anchors orthogonal to M4.0b-5); **issue once M4.0b-5 is committed** (one-uncommitted-milestone-at-a-time). **(2) B Stage 2** (EntityRole, same AMD-44). **(3) Workstream C** — integration-api freeze, P3-gated on Research 6 NQ-1..6 + P4 Doc-05 currency; **freeze against the post-B device model** (Research 6 capability surface depends on B's Entity/EntityRole). **AMD-renumber ripple:** the Research 6 assessment's `AMD-53/56/59` are stale placeholders (53 is now the unifier) — annotate renumber-at-milestone (integration block re-bases to 54+).

## This Session — M4.0b-4b WUCP Phase 2 Review + Closeout (2026-05-31)

**Mode-3 Director → WUCP Phase 2.** Freshness preflight at session start: initial **STALE** (Check 4 + weekly plan — the M4.0b-4a closeout commit `451cc63` had not propagated to the milestone backlog or W22 plan) → **reconciled** (4a/4b split recorded) → re-run **PASS**. Build gate **GREEN** (Nick ran `./gradlew check`, 143 tasks incl. ArchUnit + spotless, + the targeted module set, 92 tasks). Dual skill-location `diff -rq` **PASS** (both empty — no skill-tree files touched). Every claim verified with the **Read tool on the working tree**, not the completion report (in-sandbox `git diff` confirmed mangling `HomeSynapseArchRules` to show `checkAll` deleted — line-ending churn; the Read tool showed it intact).

- **Verdict: APPROVE.** Read all eight contract surfaces vs source at `72596cb` and confirmed AMD-52-INV-01..07: typed `StateChangedEvent` (nullable `oldValue`, no Jackson annotation — INV-01); `AttributeValueSerializer`/`Deserializer` exhaustive no-`default` 8-arm switch, `"t"` string discriminator (not `@JsonTypeInfo`), bit-anchored `Double.doubleToLongBits` float + `"NaN"`/`"+Inf"`/`"-Inf"` sentinels + `−0.0`→`+0.0` (INV-02/03/04), strict decode with **no upcaster consulted** (INV-05); `EventPayloadCodec` Path-B gate at the codec layer (`StateChangedEvent.class && schemaVersion==1` → `DegradedEvent`, raw preserved — F2 faithful); `ProductionDerivationRule` emits typed at `EventDraft(…, schemaVersion=2, …)` with `env.eventTime()`; typed materialization + null-guarded typed `shouldPublishDerived`; `CheckpointSerializer` `LinkedHashMap` typed envelope preserving the `ALWAYS` null round-trip; `projectionVersion` literal **4** riding AMD-50's frozen backfill (INV-07); **no `module-info` change** (the event-model STOP-gate correctly did NOT fire — the typed field rides the legal `event → value` edge 4a wired).
- **`[REVIEW]` adjudicated ACCEPT:** the Coder added a new ArchUnit rule `NO_JACKSON_IN_DOMAIN_MODEL` (dependency-level over `value`/`event`/`device`/`state`) instead of the AMD-52 §5#2-suggested Rule-7 *predicate extension*. This is a HOW choice, not a contract change — it enforces the Jackson-isolation HARD RULE / AMD-52-INV-02 more completely (Rule 7 is event-package-scoped and cannot reach the now-`value`-resident `AttributeValue`), lives in the canonical app arch-rules location, and is green (proving all four packages are Jackson-free). **Rule 10 subsumes the §5#2 suggestion — no AMD erratum needed.** Two `[INFO]` (snake_case Degraded field literals — self-consistent across serde; null-guarded `currentValue.equals` — safe) noted, no action.
- **Deferred build gate RESOLVED:** the M4.0b-4b gate flagged in coder-handoff is cleared — Nick ran the full + targeted `check` GREEN against `72596cb`. No open deferred gates remain.
- **Closeout applied (this session):** PROJECT_SNAPSHOT (4b COMPLETE, latest `72596cb`, `projectionVersion`=4, Workstream A complete); milestone backlog (4b NEXT→DONE `72596cb`, M4 parent row); W22 plan (goal 12 + forward sequence); this handoff; **Doc 01/03/04 body-fold** (the AMD-52 mastheads pointed to "body-fold pending M4.0b-4"). AMD-52-INV-01..07 already registered §22 — no invariant work. MODULE_CONTEXTs (event-model/persistence/state-store) were updated by the Coder and committed in `72596cb`; PM spot-confirmed currency.
- **Next forward (sequence locked with Nick 2026-05-31):** **(1) timestamp-model unifier** — `lastChanged` is event-time-sourced in the AMD-50 backfill but wall-clock-sourced in LIVE `applyToState`; AMD-52 made the 3→4 reconciliation a live path, so the field now diverges across every `projectionVersion` bump (a replay-determinism gap adjacent to AMD-50-INV-03). Resolve via a **small AMD** (which timestamp model wins — leaning event-time-everywhere, which makes `lastChanged` replay-deterministic; the LIVE envelope carries `eventTime`) then a Coder WU. The honest last mile of Workstream A. **(2) Workstream B** — device-model breadth; **AMD-44 is RATIFIED (pending implementation)**, staged Stage 1 (Floor + `Set<HardwareIdentifier>` + minimal Area) → Stage 2 (EntityRole); Research 8 PM assessment on file; gate = PM authors the staged coding instruction (can run in parallel with the unifier). **(3) Workstream C** — integration-api freeze; **after B** (Research 6 PM assessment NQ-3/NQ-4: the capability surface — `CapabilityAdded`/`CapabilityRemoved`, capability identity, `Entity.capabilities`— is shaped by B's device-model decisions, so freeze once against the post-B shape); still P3-gated on Research 6 NQ-1..6 and needs AMD-53/56/59 authored; consumers are M8/M9.

## This Session — Research 11 Assessment + AMD-52 Authored & RATIFIED (2026-05-31)

**Mode-1 Architect → ratification mechanics (documents-only; no code; no `projectionVersion` bump; HEAD stays `98f705b`).** Freshness preflight at session start: **PASS** (HEAD `98f705b`, `projectionVersion` 3, watermark AMD-51, Workstream A COMPLETE; Check 9 STALE-pending-sync expected post-edit). Every source claim verified with the **Read tool** on the working tree (in-sandbox `git`/`grep` distrusted — and confirmed truncating `Architecture_Invariants_v1.md` to §19 this session; the Read tool showed §20/§21 present and §22 was appended correctly).

- **Research 11 assessed (6-step A–F):** `context/assessments/2026-05-31_Research_11_PM_Assessment.md`. Grade **A−**; 6 RECs (REC-100..105) all ACCEPT (REC-104 ACCEPT-WITH-NARROWING; REC-103 ACCEPT-AS-VALIDATION); 0 REJECT. **§7 source-verified against HEAD `98f705b`** — every type/module/version real (Research-6 guard held). Three refinements folded into AMD-52: codec needs **no new module edge** (`persistence → transitive state → transitive device`, proven by `CheckpointSerializer` importing the device types); base class is `JsonSerializer`/`JsonDeserializer` (the `UlidSerializer` precedent, not `StdSerializer`); ArchUnit Rule 7 is event-package-scoped, so the device-resident `AttributeValue` is governed by the Jackson-isolation HARD RULE. Corroboration the research missed: `PersistenceJacksonModule`/`PersistenceObjectMapper` Javadocs pre-declare the `AttributeValue` serde (DECIDE-M2-03). Mechanism seam confirmed: `schema_version` is a per-draft field (`EventDraft.schemaVersion()`, default 1, `SqliteEventStore:316`); `ProductionDerivationRule` emits `EventDraft(STATE_CHANGED, 1, …)` today — AMD-52 bumps to `2` and carries the already-computed typed values.
- **Four PM-under-delegation fork calls (Nick, 2026-05-31):** **Q1** bit-anchored float identity (`Double.doubleToLongBits` after AMD-51 §2.3 canonicalization; stored text round-trippable, not byte-frozen; `chain_hash` stays inert AMD-37) — dissolves the Schubfach JDK-18→19 break; **Q2** Path B = defined `DegradedEvent` for legacy `schema_version=1` rows (version-gated in `EventPayloadCodec.decode`; **no** upcaster pushed into the codec — a deliberate narrowing of REC-104, chosen to avoid the layering inversion); **Q3** accept REC-100/102/103; **Q4** author this session.
- **AMD-52 AUTHORED + RATIFIED:** `homesynapse-core-docs/design/amendments/AMD-52_Typed_StateChangedEvent_Payload_Serializer_and_Replay.md`. Authored as PROPOSED with F1/F2 flagged, then **RATIFIED as-authored by Nick + an independent HomeSynapse Core Claude Project review** (both forks CONFIRMED; the review independently re-derived the load-bearing source facts). Specifies S1 (typed payload + `AttributeValue` codec, compact `{"t":…,"v":…}` envelope, no `@JsonTypeInfo`, no new module edge/Jackson artifact), S2 (`CheckpointSerializer` typed envelope, `ALWAYS` null round-trip preserved), the `schema_version` 1→2 seam, the G2 replay contract (Path A authoritative; Path B defined-degrade), the G4 consumer-migration table (all benign; `oldValue` nullable for first-report), and `projectionVersion` **3→4** on AMD-50's frozen backfill. AMD-52-INV-01..07.
- **Ratification mechanics applied (WUCP Phase 2, doc-only):** AMD-52 Status→RATIFIED + Date applied + ratification block + §9 boxes `[x]`; **watermark AMD-51→AMD-52** (`00-navigation-index.md` §38 + AMD-52 amendments-table row; fixed stale AMD-51 "not yet started"→"committed `98f705b`"); **AMD-52-INV-01..07 registered** into `Architecture_Invariants_v1.md` (new **§22** + §0.3 prefix [added missing AMD-51 + new AMD-52 rows] + §17 index 7 rows + §18 traceability §22 row); **Doc 01/03/04 masthead currency notes** (RATIFIED, body-fold pending M4.0b-4); state-store MODULE_CONTEXT header forward-pointer. **No `.claude/skills/` mirror touched. No code; no deferred build gate; no new Open Risks.**
- **Next forward = the M4.0b-4 coding instruction** (PM Mode-3, fresh session) — UNBLOCKED; implements AMD-52 §2.1–§2.7; reuses AMD-50 backfill for 3→4; **must include the §4c arch-rule test-`Clock` reminder** (persistence + state-store both non-whitelisted).

## This Session — AMD-52 Design Beat (OQ-05-08) + Research 11 Dispatch (2026-05-31)

**Mode-1 Architect, documents-only (no code, no amendment authored, no `projectionVersion` bump).** Ran the OQ-05-08 design beat for AMD-52 (typed `StateChangedEvent` payload) and dispatched the deep-research brief. Freshness preflight at session start: PASS (KB current at `605b5d1`; HEAD `98f705b`; `projectionVersion` 3; watermark AMD-51; Workstream A COMPLETE — trusted as ground truth per session brief). Every source claim verified with the **Read tool** on the working tree (in-sandbox git/grep distrusted — synced-folder churn).

- **Deliverable 1 — design beat** (`homesynapse-core-docs/design/2026-05-31_AMD-52_Typed_Payload_Serializer_Replay_Design_Beat.md`). Settled the four OQ-05-08 sub-questions from source, coherent with AMD-51 §2.7 + §2.6 erratum: **DECIDED** — (a) no event-store / `view_checkpoints` row migration; typed payload stays in the `events.payload` BLOB; per-event `events.schema_version` is the string↔typed discriminator (closes gate G5); (b) AMD-52 = its own `projectionVersion` **3→4** bump riding AMD-50's frozen backfill unchanged; (c) serializer *mechanism* — custom `AttributeValue` Jackson (de)serializer in `core/persistence`, explicit `AttributeType` tag, **no `@JsonTypeInfo`** (ArchUnit Rule 7 `NO_JSON_TYPE_INFO_IN_EVENTS` + Jackson-isolation HARD RULE). **OPEN (→ research/Nick)** — the tagged-union wire-form, deterministic `double` + `NaN`/`±Inf`/`−0.0` JSON encoding (G1), and the replay-determinism contract: Path A (re-derive typed from the immutable `state_reported` log during the 3→4 backfill — authoritative) vs Path B (version-branched decode of historical String payloads via `AttributeValueUpcaster`) (G2). Key structural finding: **two serialization surfaces** — `EventPayloadCodec` (S1, the event payload) and `CheckpointSerializer` (S2, the materialized-view checkpoint, which already anticipates a "typed envelope per entry"). Go/no-go gate: GO only when G1+G2 settle; G3/G4 are then authoring work; G5 CLOSED by the beat.
- **Deliverable 2 — Research 11 brief** (`context/instructions/Research_11_Typed_Event_Payload_Persistence_Brief.md`, REC-100+). Scoped ONLY to the beat's OPEN forks; surveys Axon `@Revision`/upcaster chain (canonical), EventStoreDB, Akka Persistence `SerializerWithStringManifest`, Kafka Schema Registry Avro/Protobuf unions. Embeds verbatim `module-info.java` ×3, the `libs.versions.toml` Jackson rows (LTD-08, `jackson = 2.18.6`), and the locked CONSTRAINTS (no `ServiceLoader`; D-01; AMD-50 frozen; AMD-51 §2.7/§2.6 erratum; the `@JsonTypeInfo` ban) so the researcher cannot fabricate names/versions (Research 6 lesson).
- **Deliverable 3 — trackers (WUCP-light):** milestone backlog gains **M4.0b-4** (AMD-52 typed payload) as **PLANNED — GATED** (proposed id per the M4.0b-x / projection-block-50–52 scheme, AMD-50→51→**52** — confirm with Nick, not locked); M4 major-row + header refreshed to `98f705b`. research-agenda gains a Research 11 addendum + OQ-05-08 marked CLOSED. New AMD-52 design-track note (`context/planning/2026-05-31_AMD-52_design-track-note.md`) seeded as successor to the CLOSED M4.0b-3 map (referenced as predecessor, not reopened). **No `.claude/skills/` mirror touched.**

**Guardrails honored:** AMD-52 not authored; no coding instruction issued; `projectionVersion` not bumped; AMD-50 backfill / no-`Clock` / no-`ServiceLoader` / D-01 / AMD-47 8-variant hierarchy / the frozen String `StateChangedEvent` payload all untouched. **Docs uncommitted across both repos — ready for Nick to commit.** Suggested message: `AMD-52 OQ-05-08 design beat + Research 11 brief + trackers (M4.0b-4 PLANNED-GATED)`. **Next forward action = AMD-52 design beat done → research dispatched** (await Research 11 → PM assessment → Nick adjudicates → author AMD-52).

## This Session — M4.0b-3 (AMD-51) COMPLETE + Independently Reviewed (2026-05-30, latest)

**M4.0b-3 shipped + committed `98f705b`.** Claude Code implemented AMD-51 (typed comparator); Nick ran the build gate GREEN (`:core:device-model:check` + `:core:state-store:check` + `:lifecycle:lifecycle:check` + full `./gradlew check`, 139 tasks) and committed. **A fresh Cowork session then independently reviewed every changed `.java` file against AMD-51 source (not the completion report) → APPROVE.** Confirmed: external `AttributeValueComparator` in `com.homesynapse.state` (pkg-private `StructuralAttributeValueComparator`, exhaustive **no-`default`** 8-arm switch, full IEEE-754 totality with `Inf−Inf` handled before the arithmetic, total-form `1e-9` epsilon, order-sensitive array deep-compare, HA-mirrored Degraded — AMD-51-INV-01/02/03/04); **symmetric both-sides reconstruction** (the prior `StringValue` IS reconstructed — the load-bearing INV-05 trap — with a direct no-spurious-emit test); **DP-K** `StandardCapabilities` in device-model **main** as an immutable injected snapshot (not a live registry → AMD-50-INV-03 holds), `TestCapabilityFactory` delegates, no FLOAT mis-typed as QUANTITY, fail-fast on key/type collision; **String `StateChangedEvent` payload preserved** (AMD-52 staged); `projectionVersion` **2→3**; both-paths by construction; **no** `module-info`/Gradle/`CheckpointSerializer` change. Independently re-verified no stray `default` arm and no direct time access in the new state-store code.

**Build gate RESOLVED.** The `-PpiProfile=throttled` IT suite was not held to completion — `Pi4D1SpikeIT` is a deliberately fixed **30-minute soak** (`@Timeout 45 min`), not a hang; it is gated out of the default `./gradlew check` (56 s) and AMD-51 does not touch the bus/WAL throughput path it exercises (every IT uses non-catalog keys → string-fallback → identical to M4.0b-2). Not a blocker.

**Deviation disposition (the Coder's three `[REVIEW]` items — all ACCEPT, none BLOCKING):**
- **D-1 — missing-schema → `StringValue` string-compare fallback** (NOT §2.6's literal "Degraded / no-emit"). **ACCEPT — judged *more* correct than the literal spec:** Degrade-on-no-schema would freeze any unschematized attribute permanently (a worse regression than the phantom-change problem AMD-51 fixes); the StringValue fallback reproduces exact M4.0b-2 semantics for unknown keys, keeps the no-arg `production()` gateway back-compatible (the whole pre-existing suite stays green), and `StandardCapabilities` covers all standard production traffic. **Governance follow-up:** this contradicts AMD-51 §2.6's error table — recommend a small **AMD-51 §2.6 erratum** (see Open Risks / Open Items) so the ratified spec matches shipped code; the PM did not silently edit the ratified amendment.
- **D-2 — ARRAY reconstruction degrades** (no element-type metadata in `AttributeSchema`; comparator's array path is implemented + unit-tested; latent — no standard ARRAY attribute). **ACCEPT.**
- **D-3 — parse-failure → Degraded-inbound no-emit, not strict halt** (§2.6 left the choice to the coding instruction; DoS-safety; no Degraded reaches canonical state). **ACCEPT.**

**WUCP Phase 2 closeout (this session):** milestone backlog M4.0b-3 + M4.B3 marked DONE (`98f705b` / `60b4185`); PROJECT_SNAPSHOT (commit, `projectionVersion`=3, build gate, session log); W22 plan; design-track-map → track CLOSED; cross-agent-notes pointer rotated; this handoff; pm-lessons appended. Dual-skill `diff -rq` PASS (both empty — no skill files touched). Freshness preflight at session start: STALE on Check 3 only (post-commit, hivemind behind `98f705b`) → remediated by this retroactive closeout → re-run PASS. **No new code Open Risks; the only open item is the optional D-1 spec erratum (docs repo).** **Docs uncommitted — ready for Nick to commit** (suggested msg in cross-agent-notes).

## This Session — AMD-51 Authoring + Ratification (2026-05-30, latest)

**AMD-51 authored and RATIFIED.** `design/amendments/AMD-51_Typed_AttributeValue_Change_Detection_Comparator.md` — external `AttributeValueComparator` in `core/state-store` (Mode-1 governance/authoring, then ratification closeout). Built strictly from the Research-10 v2 ratification + the four strategic calls; every type/module claim source-verified against HEAD `60b4185` with the **Read tool** (the in-sandbox `git`/`grep` was observed truncating this synced folder again — distrusted, per the standing mount lesson). C1–C7 confirmed. Authored §1 problem, §2 contract (per-variant semantics; pinned total-form epsilon + IEEE totality; units-free-via-AMD-47; Degraded rule; comparator placement/gateway; OQ-05-09 reconstruction; 2→3; String-payload preservation), §3 worked scenarios, §4 AMD-51-INV-01..05, §5 tests, §6 scope, §7 module-info ×3 + C1–C7 embeds, §8 WUs, §9 checklist, §10 review disposition.

**External review (HomeSynapse Core Claude Project) → RATIFY-AS-IS, 0 blocking.** PM ran the Research-6 confabulation guard: the review asserted facts about `CheckpointSerializer` / `StateProjection.applyToState` that were **not** in the source companion, so PM verified them against source — **CONFIRMED**, including the load-bearing finding: the materialized prior side is **always a `StringValue`** (`applyToState` line 819 + `applyBackfillAttribute` line 928 write `new StringValue(...)`; `CheckpointSerializer` "only writes StringValue"; `state_reported` never writes attributes). PM **elevated this above the review's "non-blocking"**: a naive comparator would compare a prior `StringValue` against a reconstructed `FloatValue`, hit the type-mismatch arm, and emit on every report. Fix folded pre-ratification: §1.2 reworded, §2.6 now requires **symmetric reconstruction of both operands**, AMD-51-INV-05 sharpened. Other accepted points → coding-instruction gates (emit-predicate naming; `canonicalUnitSymbol`-fallback WARNING + adapter-`unit` audit; conversion-noise §5 #5b + catalogue-expansion §5 #9 tests). **PM-added finding:** the existing string-based `shouldPublishDerived` dedup (`StateProjection` ~line 758) must stay coherent with the typed verdict (§5 #10). Epsilon **LOCKED at 1e-9** (conversion-noise ceiling ≈ 6.6e-16 rel worst case °F→°C, ~5 orders below; verified by §5 #5b, no sensor-capture gate). Full disposition: AMD-51 §10.

**Sequencing correction (caught a second-opinion error).** A proposed procedure claimed M4.B3 was a pending prerequisite session (chain `AMD-51 → M4.B3 → M4.0b-3`). **Wrong:** M4.B3 is COMMITTED at HEAD `60b4185`; its DP-1 upcaster-wiring carry lands *inside* M4.0b-3. Correct chain: **AMD-51 RATIFIED → M4.0b-3** (no intermediate session).

**Ratification closeout (WUCP Phase 2, doc-only, this session):** AMD-51 Status → RATIFIED + Date applied 2026-05-30; `Architecture_Invariants_v1.md` §21 DRAFT qualifier cleared + §18 traceability now RATIFIED (§17 index 5 rows + total 104/21 were pre-registered at authoring); state-store MODULE_CONTEXT Constraints (AMD-51-INV-01..05) + Amendments-in-force row + header; `00-navigation-index.md` amendments table caught up (AMD-44/45/47/50/51 added; **watermark raised AMD-50 → AMD-51**); PROJECT_SNAPSHOT + cross-agent-notes pointer + design-track-map (NQ-10-1/5/6 + OQ-05-09 RESOLVED-BY-AMD-51) + this handoff. **No new Open Risks; no open deferred build gates.** Hivemind edited → freshness Check 9 STALE-pending Nick's external mirror sync (normal). **Docs uncommitted — ready for Nick to commit** (suggested msg in cross-agent-notes). **Next forward WU = M4.0b-3 coding instruction** (recommended fresh Mode-3 session).

## This Session — Research 4 DQ + STALE Reconciliation + Research 10 Ratification (2026-05-30)

**Research 10 returned + ratified (latest action this session).** Assessment at `context/assessments/2026-05-30_Research_10_PM_Assessment.md` (6-step A–F; all §7 corrections source-verified against HEAD `60b4185` — the research ran on a stale pre-M4.0b-2/pre-M4.B3 baseline: C1 no-Clock, C2 wrong milestones, C3 AMD-47 types already shipped, C4 fixture-not-production-rule, C5 inbound-is-String keystone, C6 `canonicalUnitSymbol` already exists). 6 ACCEPT / 0 REJECT (REC-90..95), all retargeted M4.0b-3. **Nick delegated the 4 strategic calls; PM ratified them under delegation**, each re-verified against committed source: defer deadband (REC-92, → future `AttributeSchema` field); FP-noise **total-form** epsilon + IEEE edge totality (REC-91); hand-roll units — already satisfied by AMD-47's construction-time `QuantityValue` canonicalization, no Indriya/LTD-10 (REC-93); **stage AMD-51 before AMD-52** (REC-94). NQ-10-5 → external `AttributeValueComparator` in `core/state-store` (refines the assessment's device-model-method lean to keep the `ComparisonPolicy`/epsilon out of the data layer); NQ-10-6 → normalize at reconstruction. **OQ-05-06 RESOLVED → M4.0b-3 design-unblocked.** Two follow-ups: **OQ-05-08** (AMD-52 typed-payload serializer/replay design beat — gates AMD-52 only, riskiest item) + **OQ-05-09** (AMD-51 upcaster unit-threading for QUANTITY; `StateReportedEvent` carries `unit`). Ledger catch: REC-93 double-booked (reconcile next freshness pass). **Next forward action = author AMD-51** (M4.0b-3; String `StateChangedEvent` payload preserved). **Assessment + these updates uncommitted — ready for Nick to commit** (DEC-M3-12; Nick retains veto on any call).

**Research 4 DQ deliberation (earlier this session).** Nick resolved DQ-1/2/3/5 (all match v3 PM recs) — v4 addendum to `context/assessments/2026-05-22_Research_4_PM_Assessment.md`: promote `PresenceTrigger`; rename `ActivateSceneAction`→`InvokeAutomationAction` + promote; same `DispatchingProjectionAdvancer`/separate handlers; geofence→M8. The assessment's "AMD-48..52" are pre-P2 placeholders — **Research 4 unblocks M7/M8 automation amendment authoring, NOT M4.0b-3.**

**STALE reconciliation (session start).** Preflight flagged STALE (not CONFLICTED): state hub lagged `7610296`→`60b4185` (M4.B3 committed); no W22 plan. Reconciled: PROJECT_SNAPSHOT + this handoff + coder-handoff + KB ledger flipped to committed `60b4185`; W22 weekly plan created; stale-content scan clean. Preflight re-run PASS.
