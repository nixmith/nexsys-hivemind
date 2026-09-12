<!--
file: context/audits/2026-09-12_CI-bd5d35e_frame-read_bus-idle-run-handoff_v70-b10.md
purpose: The read of ci sample #11 (core bd5d35e, run 34670078359) — the first lifecycle red carrying pending= and the thread dump — against the four mechanisms pre-registered in the cc05a54 audit §2. The frame falsifies H1, H2 and the parked-past-wake half of H3 and moves the class out of the bus: the engine's virtual thread is idle with an empty queue, every reader and the writer are idle, no thread is pinned, and the run pipeline did not continue after publishing automation_triggered. Also: the census's missed=1 is a checkpoint-lag artefact — writeCheckpoint is fire-and-forget.
audience: v71 (FIX-2b-ii's authoring input) · Nick (§0)
state-type: audit (filed evidence; a later read appends)
status: FILED at v70 beat 10 (Sat 2026-09-12 ~10:2x CT; instrument 2026-09-12T15:17:47Z). Evidence: _scratch/v71/ci-bd5d35e/ (checkout sha bd5d35e3a070da503ba4d0b6ec07f81c67ba534d); sample #12 (6af76f7, run 34670103244) under _scratch/v71/ci-6af76f7/, not yet read.
-->

# Sample #11 — the frame (v70 beat 10)

## §0 Verdict surface
- **Red at lifecycle again, two suites:** `BusPositionCensusIT` (the census after the hero loop never settled: `store_head=24 awaited=24`, the engine and the ledger at 23) and `BusSoakIT` (loop 14 of 20: `store_head=183 awaited=182`, the engine and the ledger at 182). The hero IT itself passed this time. The pinned-thread trace printed nothing.
- **`pending=0` on every subscriber in every failure.** The position after the motion report (`automation_triggered`) is NOT sitting in the engine's queue.
- **The engine's virtual thread is parked idle in `liveLoop`** (`InProcessEventBus.java:536`, the `position == null` branch) — not blocked in a read, not inside `deliver`, not waiting for a carrier. Every `hs-sub-read-*` thread and `hs-read-0` are WAITING (idle); `hs-write-0` is WAITING (idle); `hs-sched-0` TIMED_WAITING (idle); no thread carries a `StandardActionExecutor` or `StandardRunManager` frame; no unnamed virtual thread with a `com.homesynapse` frame exists. 36 threads dumped, 20 shown.
- **What that falsifies:** H1 (pinning / carrier starvation — nothing pinned, nothing waiting for a carrier), H2 (read-executor saturation — every reader idle), H3-parked (parked past its wake — the queue is empty, so there was nothing to wake for). **What survives:** H3-never-offered only if the engine did not deliver `automation_triggered`; but see the next point.
- **The checkpoint in the snapshot lags delivery.** `SqliteCheckpointStore.writeCheckpoint` submits to the write coordinator and does not wait (`:176–:184`: `submit(WritePriority.STATE_PROJECTION, …)`, no `get`). So `checkpoint=182` with `head=183` does not prove 183 was not delivered — only that its checkpoint write had not executed when the snapshot was taken. With the writer idle for ten seconds that is unlikely but not excluded; it also means the census IT's `missed=1` on an idle bus is an artefact of the token's definition (TR-1 §1 reason 1 assumed a synchronous write), and the census must read the checkpoint AFTER a writer drain or use the bus's in-memory last-delivered position.
- **The reading that stands:** the bus is idle and consistent; the automation run was initiated (`automation_triggered` is in the store, published from `StandardRunManager:651` on the engine's own thread during `onEvent`) and its first action never started; no thread is executing it. **The class has moved from the bus's delivery to the run pipeline's hand-off after `automation_triggered`** — whatever runs the actions was not scheduled, or was scheduled and dropped, on the two-processor runner. OR-BUS-SILENT-DROP keeps its name for the record; its mechanism is now "the run does not continue", and the bus instruments have done their job.

## §1 The greps (re-runnable; under `_scratch/v71/ci-bd5d35e/report/lifecycle/lifecycle/build/test-results/test/`)
```
grep -h -o 'bus\.await_[a-z]*: [^&<]*' TEST-*.xml                 # pending=0 on every line
grep -o 'bus\.thread: name=[^ ]* state=[^ ]* virtual=[a-z]*' TEST-com.homesynapse.lifecycle.BusSoakIT.xml | sort | uniq -c
awk '/bus.thread: name=hs-sub-automation_engine/{f=1;c=0} f{print;c++} c>=9{f=0}' TEST-com.homesynapse.lifecycle.BusSoakIT.xml   # park → liveLoop:536
cat TEST-*.xml | grep -c '<== monitors'                              # 0 (no pinned trace)
```

## §2 The next reads (v71; FIX-2b-ii is authored on them)
1. `StandardRunManager.java:600–:720` — what follows `publish(AUTOMATION_TRIGGERED)` at `:651`: the condition step, and HOW the actions are handed off (a run executor? the SharedScheduler `hs-sched-0`? the engine's own thread on a later event?). Name the thread and the queue. If it is a scheduled task with a delay derived from the injected `Clock`, compare that clock to the scheduler's.
2. `SubscriberSupervisor.deliver` (`:95–:150`) — every result other than SUCCESS and what `liveLoop` does with it; whether a swallowed exception in `onEvent` after `:651` could return non-SUCCESS without a DLQ entry (`dlq=0`) and without a log line.
3. `SqliteCheckpointStore.writeCheckpoint` — make the census read the delivered position, not the persisted one (the bus keeps it in memory; `SubscriberSnapshot` could carry `lastDelivered`), or drain the writer before the census.
4. Sample #12 (`6af76f7`) under `_scratch/v71/ci-6af76f7/`: the same greps; if its frame matches, two samples confirm the hand-off reading.
**The instrument that settles it in one push:** one INFO line in `StandardRunManager` after `:651` naming the hand-off taken (`automation.run_handoff: runId= mode= executor=`), and one at the executor's entry (`automation.action_step_started: runId= index=`). Their absence on the next red names the step.

## §3 What changes in the record
- The bus instruments (FIX-2a, FIX-2b-i) stay: they are what produced this frame. CI-1 takes the amplifier off the gate.
- FIX-2b-ii's scope moves to `core/automation` (the run hand-off) with the two INFO lines as its red-first instrument; a bus change is not indicated by this sample.
- TR-1's census definition gains a caveat: the persisted checkpoint lags delivery; `missed` must be computed after a writer drain.
