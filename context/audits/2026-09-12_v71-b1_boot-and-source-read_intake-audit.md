<!--
file: context/audits/2026-09-12_v71-b1_boot-and-source-read_intake-audit.md
purpose: The v71 beat-1 intake: the boot as executed (the read budget, the five HEADs, the twelve preflight checks), the frame audit's §2 reads done at source by range, and the two samples re-grepped. It corrects one claim of the v70 frame audit at the bytes (the checkpoint write is synchronous) and records what the reads leave open. FIX-2b-ii's instruction is authored on this file and the frame audit together.
audience: the v71 hub (the authoring input) · Nick (§0) · REV-1 (the claims to attack)
state-type: audit (filed evidence)
status: FILED at v71 beat 1 (Sat 2026-09-12 ~11:1x CT; instrument 2026-09-12T16:14:36Z). Evidence: _scratch/v71/ci-bd5d35e/ and _scratch/v71/ci-6af76f7/ (both read this beat); homesynapse-core at ff1a6e1.
-->

# v71 beat 1 — the boot and the source reads

## §0 Verdict surface
- **Boot:** read set 44.4 KB against the 45 KB budget (the prompt 13,017 B · the chain line 2,324 B · the v70 b10 beat 2,474 B · the snapshot 3,480 B · the brief 10,493 B · the decision record §3 1,969 B · the plan of record §3 1,001 B · the assessment §3 5,399 B · pm-lessons after the 09-07 fold 4,200 B of 4,920 B). HEADs at the instrument: core `ff1a6e1` · hivemind `e16eb06` (act 1 landed) · skills `c630c5c` · bench `4539f13` · docs `73c204b`; porcelain 0 and push count 0 in all five. The record's five lines verified.
- **Preflight:** STALE on two checks, both hygiene; forward work is lawful (§1).
- **The hand-off, at source:** a per-run virtual thread `automation-run-<automationId>-<runId>` (`StandardRunManager:570–:575`), started at `:320` (admitted) or `:539` (drained) right after `publishTriggered`; `runBody` (`:459`) → `StandardActionExecutor.execute` (`:172`) → `publishStarted` (`:183`) before any action. Not a scheduler, not the engine's thread on a later event. In sample #11 the head was `automation_triggered` (the v70 read), so the executor's loop never published `action_started`; the VT either never mounted or died before `:183`. Neither is excluded by the dump (§2.2).
- **The correction:** `WriteCoordinator.submit` returns the operation's result; `PlatformThreadWriteCoordinator.submit` blocks on `future.get()` (`:69–:97`); the interface's javadoc says so (`:40–:42`). `SqliteCheckpointStore.writeCheckpoint` is therefore synchronous from `liveLoop`'s view, and the write connection is autocommit (`grep -rn 'setAutoCommit(false)' core/persistence/src/main` = `AtomicCheckpointWriter:271`, `MigrationRunner:386`). The v70 frame audit's "fire-and-forget" and its "checkpoint-lag artefact" are withdrawn. The census's `automation_engine matched=24 delivered=23 missed=1 first_missed=24 checkpoint=23 dlq=0 pending=0` — byte-identical in samples #11 and #12 — is a real miss of the head position by a subscriber whose filter is `SubscriptionFilter.all()`. TR-1's definition needs no caveat.
- **What the reads leave open (three survivors):** (a) the run VT started and never mounted; (b) it mounted and died on an `Error` before `:183` (`runBody` catches `RuntimeException` only, `:486`; no `Exception in thread` text in either sample's XML); (c) the engine's miss of the head — the offer path's one silent branch is `notifyEvent`'s checkpoint guard (`InProcessEventBus:369–:373`). FIX-2b-ii (i) instruments all three; REV-1 and REPRO-1 are chartered because the reads did not settle the class (Nick's condition).

## §1 The preflight, one line per check
1. PASS — snapshot `last-verified: 2026-09-12` = today; the chain line names v70 beat 10, the snapshot names v70 beat 10.
2. PASS — both spines name v70 beat 10; `context/planning/2026-09_september_plan-of-record.md` resolves.
3. PASS — snapshot core `ff1a6e1` = `git log -1` `ff1a6e1`.
4. PASS (historical) — `phase-3-milestone-backlog.md` last-verified 2026-08-01, 29 DONE rows; no milestone closed since; not re-walked row by row this boot (disclosed).
5. PASS — `## Open Risks` at pm-handoff `:95`, newest date in the section 2026-09-12.
6. PASS — coder-handoff's newest entry (CI-1, `:17`) carries a NEXT WU pointer (the hub's audit → the card → the next instruction); the spine names it FIX-2b-ii.
7. PASS — 21 `MODULE_CONTEXT.md` tracked in core, none under 1,500 B (`settings.gradle.kts` has 22 `include(` lines; the difference not chased — the one unmatched include is not a Phase-2 module the spine tracks).
8. PASS — `cross-agent-notes.md` 1,024 B, no active entry.
9. STALE — 27/28 identical at the bytes; `project-manager/SKILL.md` differs (source `bda340b1…`, synced `76bf4ce6…`); the synced tree lags the source (Nick's sync); hub reads ride SOURCE, so authoring is lawful.
10. PASS — 97 cited paths in `strategic-context-map.md`; the only unresolved basenames are the three template placeholders (`YYYY-MM-DD_topic.md`, `YYYY-MM_month.md`, `YYYY-WNN_monDD-monDD.md`).
11. PASS — `StandardRunManager`, `InProcessEventBus`, `SqliteCheckpointStore`, `SubscriberSupervisor` each resolve once in `git ls-files`.
12. STALE — four executed instructions still carried `status: ISSUE-READY` (CI-1 landed `ff1a6e1`, FIX-2a `cc05a54`, FIX-2b-i `bd5d35e`, HERO-1b `6af76f7`); flipped to EXECUTED at this beat (a status-line edit, bodies unchanged). One LIVE prompt (v67). `context/planning/weeks/` tracks 0 files. The H8-a packet stays LIVE (the run is owed) and RS3-WMARKET-2 stays on its cadence.

## §2 The reads at the bytes
### 2.1 `StandardRunManager` (830 lines)
- `:225–:330` the `onEvent` path: (5) the trigger-time snapshot (`stateQuery.getSnapshot()`, a failed read → `failClosedRead` `:450–:452`, which publishes `automation_triggered` then `automation_completed FAILED`); (7) the condition gate at `:271–:275` — `CONDITION_NOT_MET` publishes `automation_triggered` (`:273`) then `automation_completed` and starts NO thread; (8) admission under `stateLock` — `startRun(run)` (`:568–:576`: `Thread.ofVirtual().name("automation-run-" + automationId + "-" + runId).unstarted(() -> runBody(run))`, registered in `activeRuns`, `liveRunThreads`, `statuses RUNNING`), then outside the lock `publishTriggered(run); run.vt.start();` (`:319–:320`); the QUEUED path defers both to the drain (`:538–:539`).
- `:459–:500` `runBody`: `actionExecutor.execute(run.resolvedActions, run.context, run.triggeringEvent)` (`:472`); `catch (RuntimeException)` only (`:486`); `finalizeRun` publishes `automation_completed`; `finally` removes the VT from `liveRunThreads`. An `Error` escapes: no log, no terminal event, the run stays in `activeRuns`.
- `:728–:741` `publish`: `SequenceConflictException` → `LOG.error("Failed to publish {} …")` and swallowed. Both samples' XML: `grep -c 'Failed to publish'` = 0, `grep -ci 'sequence conflict'` = 0.
- Logging in the module: three ERROR sites (`:450`, `:738`; `StandardActionExecutor:404`); no INFO line on the run path.
### 2.2 The dump's reach (`lifecycle/…/BusThreadDump.java`)
- A thread is shown if its name starts with `hs-` (`:67`) or any of its first `FRAMES_SHOWN = 12` frames (`:71`, `:253–:260`) contains `com.homesynapse`. `bus.thread_dump: threads=36 shown=20` in sample #11: 16 threads hidden. A started, never-mounted virtual thread carries a name that starts with `automation-run-` and, if the dump lists it at all, only JDK frames — so it is hidden (reasoned from the filter, not measured on a dump; REV-1's second question); a VT that died is gone. `grep -c 'automation-run-'` over both samples' XML = 0. The dump therefore does not separate (a) from (b) in §0.
### 2.3 `SubscriberSupervisor.deliver` (`:97–:150`) and `liveLoop` (`:526–:575`)
- `RuntimeException` from `onEvent` → a `DeadLetter` parked (`dlq.park`, `:122`) → `PARKED`, or `CIRCUIT_BREAKER_TRIPPED` after the threshold (SUSPENDED); `Error` and checked `Exception` → SUSPENDED, `INFRASTRUCTURE_FAILURE`, no DLQ entry and no log line. `liveLoop` writes the checkpoint only on `SUCCESS` (`:557–:566`). With `dlq=0` and `mode=LIVE` on every subscriber in both samples, every delivery that happened returned `SUCCESS`; the engine's checkpoint one behind the head means the head was not delivered to it.
### 2.4 The offer path (`InProcessEventBus.notifyEvent` `:316–:386`, `routeByMode` `:593–:615`)
- `NotifyingEventPublisher.publish` (`lifecycle:44–:49`) appends, then `bus.notifyEvent(position)` on the publisher's thread. For each active subscriber whose filter matches: `readCheckpoint` (a blocking read on `hs-read-*`), `if (checkpoint >= globalPosition) continue;` (`:371–:373`, silent), else `routeByMode`: LIVE → `pendingPositions.offer` + `LockSupport.unpark(vt)` (`:608–:611`); REPLAY/TRANSITION → the replay window queue; COLD/SUSPENDED → return (silent). The run pipeline is wired with the notifying publisher (`HomeSynapseCore:573`, `:713–:721`); the engine subscribes with `SubscriptionFilter.all()` (`:733`).
### 2.5 `SqliteCheckpointStore.writeCheckpoint` (`:166–:184`) and the coordinator
- `dbExecutor.writeCoordinator().submit(WritePriority.STATE_PROJECTION, () -> { upsert })`. `PlatformThreadWriteCoordinator.submit` (`:69–:97`): `queue.offer(item); return future.get();` — the caller blocks until `hs-write-0` runs the upsert. `pendingPositions` is a `LinkedBlockingQueue<Long>` (`SubscriberRuntime:38`).
### 2.6 The two samples by the same greps (`_scratch/v71/ci-<sha>/report/lifecycle/lifecycle/build/test-results/test/`)
- #11 `bd5d35e`: red `BusPositionCensusIT` + `BusSoakIT`; timeouts `store_head=24 awaited=24` and `On frame #15 reaching the scripted NCP (loop 14 of 20) store_head=183 awaited=182`; `pending=0` on every line; pinned 0; `automation-run-` 0; `Exception in thread` 0.
- #12 `6af76f7`: red `BusPositionCensusIT` only; the same census line for the engine (`missed=1 first_missed=24 checkpoint=23`); the soak green; pinned 0; `automation-run-` 0.
- Both: the census's other five subscribers `missed=0`; `state_projection matched=24 delivered=24 checkpoint=24 atomic=true`.

## §3 Not re-executed (disclosed)
- The v70 read that the soak's head 183 IS `automation_triggered` (this beat re-read the await lines, not the store dump).
- Whether the census's position 24 is an event the engine published from inside its own delivery (the store's event types were not grepped from the XML — the census prints positions, not types). REV-1's first question.
- Check 4 row by row; Check 7's 22nd `include(`.

## §4 What changes in the record
- The class has two faces, not one: the soak's (the run does not continue after `automation_triggered`) and the census's (the engine does not receive the head). The frame audit's §3 sentence "a bus change is not indicated by this sample" holds for the soak and is withdrawn for the census.
- FIX-2b-ii (i) is four log lines in `core/automation` plus one anomaly kind at the guard in `core/event-bus` (the bus has no logger; its channel is the injected anomaly consumer, which the soak already counts). Nick's dispatch named two lines; the reads named the other three sites; the instruction says which is which.
- TR-1's census definition stands unchanged.
- REV-1 and REPRO-1 are chartered at beat 2 (Nick's condition met: the reading is ambiguous after the §2 reads).
