<!--
file: context/audits/2026-09-11_CI-cc05a54_red-read_first-diagnostic_v70-b8.md
purpose: The read of the ci red on core cc05a54 (FIX-2a's landing; run of 2026-09-12T01:42Z) — the first runner sample that carries FIX-2a's diagnostic. Three failures, one shape. What the checkpoints prove, what they cannot, and the four mechanisms the next instrument must separate.
audience: the hub (FIX-2b's instructions cite it) · Nick (§0)
state-type: audit (filed evidence; a later read appends)
status: FILED at v70 beat 8 (Fri 2026-09-11 ~21:2x CT; instrument 2026-09-12T02:08:54Z). Evidence: _scratch/v70/ci-cc05a54/ (log/ + report/; checkout sha cc05a5423086cc69b2b7f5c92864d5c84fbf43bb).
-->

# The cc05a54 red — the first diagnostic-bearing sample (v70 beat 8)

## §0 Verdict surface
- **The gate of record on cc05a54 is RED** at `:lifecycle:lifecycle:test`: 82 run, 3 failed — `BusPositionCensusIT` (01:45:28Z), `BusSoakIT` (01:45:38Z), `HeroLoopHardwareFreeIT.heroLoop_motionToHonestConfirmed` (01:45:50Z). No other module failed. `bus.delivery_anomaly` lines in the 20 XML files: 0. This is OR-BUS-SILENT-DROP sample #10, RED, and the first with a reading.
- **The runner:** `bus.soak_host: available_processors=2 vt_parallelism=default` (the desk: 24; pinned to 2 it stayed green). The soak on the runner: 18 of 20 loops ok, one timed out (loop 18), `p50_ms=20 p99_ms=202` — fast when it works, then a discrete ten-second stall, not a slow drift.
- **One shape, three times.** `store_head = awaited + 1` in every failure: exactly one event follows the motion report, and it is the engine's own `automation_triggered` (the run pipeline's first event; `automation_action_started` and `command_issued` follow from `StandardActionExecutor:367/:274` and never appeared). Every subscriber is LIVE, every DLQ empty. `command_dispatch_service` had nothing to deliver. So the ten seconds are spent **between the run's initiation and its first action** — inside the automation engine's run pipeline or in what it waits on — not in the bus's delivery to the dispatch service.
- **The engine's checkpoint tells two stories.** Hero IT: `automation_engine checkpoint=14 = head` — the engine delivered its own `automation_triggered` and returned SUCCESS; the action step (asynchronous to that delivery, or sleeping inside it) then stalled. Census IT and the soak: `automation_engine checkpoint = awaited` (13; 230) with the soak's census reading `automation_engine matched=231 delivered=230 missed=1 first_missed=231` — the engine did NOT deliver `automation_triggered` within ten seconds while `state_projection` (also `all()`) delivered it at once. Either the engine's virtual thread was blocked (inside `deliver(231)`, or in `readLivePosition(231)` on the read executor), or 231 sat in its queue with the loop parked, or it was never offered.
- **What the checkpoints cannot settle:** which of those. The snapshot carries no queue depth (`SubscriberSnapshot` has `checkpoint`, `dlqDepth`, `crashCount`, `oldestParkedAt` — `InProcessEventBus.buildSnapshot :729`) and no thread state. **FIX-2b-i adds exactly the two instruments that separate the four mechanisms in §2: the pending-queue depth per subscriber, and a thread dump (virtual threads included) at the timeout.**

## §1 The greps (re-runnable on the device; all under `_scratch/v70/ci-cc05a54/report/lifecycle/lifecycle/build/test-results/test/`)
```
grep -o 'bus\.soak_host[^&<]*\|bus\.soak:[^&<]*\|bus\.position_census[^&<]*' TEST-com.homesynapse.lifecycle.BusSoakIT.xml
grep -o 'bus\.await_[a-z]*: [^&<]*' TEST-com.homesynapse.lifecycle.HeroLoopHardwareFreeIT.xml TEST-com.homesynapse.lifecycle.BusPositionCensusIT.xml
cat *.xml | grep -c 'bus.delivery_anomaly'      # 0
grep -c -i 'automation\.\|RunManager\|ActionExecutor' *.xml   # 0 — the run pipeline logs nothing at INFO on this path
```
The hero IT's timeline: `zigbee.device_adopted` ×2 at 01:45:52.918/.929 → the motion edge (no log line) → the diagnostic at ~01:46:02.9 → `HomeSynapseCore stopped` 01:46:03.012.

## §2 The four mechanisms, pre-registered against FIX-2b-i's instruments
| # | Mechanism | The dump and the depth would show | The fix it would call for |
|---|---|---|---|
| H1 | **Carrier pinning / starvation** on a 2-carrier scheduler (JDK 21 does not compensate a virtual thread pinned in `synchronized` while it blocks; sqlite-jdbc's JNI is the AMD-26/27 case) | `jdk.tracePinnedThreads` output on the runner; the engine's VT or the run's VT waiting for a carrier; other VTs pinned in native/synchronized frames | move the pinning call off the VT (the AMD-26/27 pattern), or set the scheduler floor for production |
| H2 | **Read-executor saturation**: `readLivePosition` and the `readCheckpoint` calls in `notifyEvent` all go through `dbExecutor.readExecutor()` (`SqliteCheckpointStore:151`); a slow or blocked read backs the queue up and every reader waits | the engine's VT blocked in a `Future.get`/queue take under `readExecutor`; `pending ≥ 1` for the engine | a separate read lane for the bus, or a bounded wait that emits an anomaly |
| H3 | **Lost wake-up / not offered**: the position never reached the engine's `pendingPositions`, or the loop parked past its unpark | the engine's VT parked in `liveLoop` with `pending=0` (never offered) or `pending ≥ 1` (parked past the offer) | the FIX-2b design: read forward from the checkpoint on every wake, the notification as a hint, a bounded idle tick |
| H4 | **The run pipeline sleeps or polls** (`StandardActionExecutor:210 Thread.sleep(delay)`, `:346 Thread.sleep(poll)`) waiting for a condition the runner satisfies late | the run's thread in `sleep` inside the executor with the awaited condition visible in its frames | the executor's wait made event-driven or bounded with an anomaly |
Each row is falsifiable by the dump; the instruction lands the dump before any fix. A fifth outcome — the dump shows nothing blocked and `pending=0` — is the strongest case for H3's fan-out and is recorded as such.

## §3 What this does to the record
- OR-BUS-SILENT-DROP: the class is real on 2-vCPU hosts and reproduces at roughly one loop in twenty there (the soak: 1 of 20; the hero and census loops: 2 of 2 on this run). The passive count restarts at cc05a54 with the soak in the suite; every push is a sample with a reading.
- The gate of record is red at HEAD. EXPLAIN-114a stays held on the strict reading of the law; the sequencing question is put to Nick in H10 form (beat 8).
- FIX-2 splits: FIX-2a (landed, instruments) → **FIX-2b-i** (the two discriminating instruments + the runner's pinned-thread trace; small; authored at v70 beat 8) → **FIX-2b-ii** (the fix, authored on the first dump-bearing red).
