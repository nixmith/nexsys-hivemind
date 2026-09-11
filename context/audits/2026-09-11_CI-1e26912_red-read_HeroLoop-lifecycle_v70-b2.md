<!--
file: context/audits/2026-09-11_CI-1e26912_red-read_HeroLoop-lifecycle_v70-b2.md
purpose: The read of the ci red on core 1e26912 at the correct artifact (run 34650129654), by grep, against the three predictions pre-registered in pm-handoff v70 beat 1. It decides FIX-2's opening branch.
audience: the hub (FIX-2's instruction cites it) · Nick (the verdict surface is §0)
state-type: audit (filed evidence; never rewritten — a later read appends)
status: FILED at v70 beat 2 (Fri 2026-09-11 ~18:0x CT; instrument 2026-09-11T23:01:19Z)
-->

# The 1e26912 red, read at the bytes (v70 beat 2)

## §0 Verdict surface
- **The artifact is the right one.** `_scratch/v70/ci-1e26912/`: checkout sha `1e269127152157aa91138de8002dc0d0545350a0`; `0_Build & Check.txt` opens at 2026-09-11T21:35:40Z; the suite `HeroLoopHardwareFreeIT` ran at 21:38:36Z (5 tests, 1 failure, 13.165 s). Nick's line: `ARTIFACT: 1e26912 · run 34650129654 · sha verified · reports: yes`.
- **P2 holds; P1 fails; P3 holds.** The failing test's stdout carries no `bus.delivery_anomaly` line and no `DeliveryAnomaly` token; none appears in any of the 42 lifecycle report files or in the 25,759-byte Run check log (three greps, three zeros). The kinds the emitter can name are: NOTIFY_NOT_VISIBLE LIVE_READ_EMPTY LIVE_READ_FAILED TRANSITION_READ_EMPTY LIVE_READ_EXHAUSTED TRANSITION_READ_EXHAUSTED . WARN lines from other loggers are present in the same stdout, so the absence is the detector's silence, not the log level's.
- **What the bytes show.** The test reached step 3. Both baseline reports passed their awaits: `occupied=false` then `occupied=true` were read back from the store by `reportedValues("occupied")` (`HeroLoopHardwareFreeIT.java:98–103`), so the motion edge is durably in the event store. Then the journal is empty for ten seconds: after `zigbee.device_adopted` at 21:38:40.031 the next line is `HomeSynapseCore stopped` at 21:38:50.114. No `zigbee.command_result`, no frame at the scripted NCP, no anomaly. The await at `:115` (`awaitTrue`, 500 polls, `:614`) timed out on `sentFrame(0x0006, 0x01)`.
- **The class.** OR-BUS-SILENT-DROP, sample #9 RED on the FIX-1b bytes: an event the store holds that the automation engine's LIVE subscriber did not act on inside the window, and the FIX-1a detector saw nothing to report. The commit under test touched only `web-ui/dashboard/design/`; the Java is `eabdbb1`'s.
- **FIX-2's opening branch (per the pre-registration): the instrument, not the fix.** (I1) the hero-loop IT's await gains a timeout diagnostic — on timeout it prints, per subscriber, the last delivered global position and the checkpoint, beside the store's head position; (I2) TR-1b's position-census ITs are the red-first tests; (I3) a bench `bus-soak` verb: N hero loops under load, delivery latency p50/p99, anomaly count. The structural fix (checkpoint-driven LIVE delivery: read forward from the checkpoint on every wake, the notification as a hint, a bounded idle tick; an AMD to Doc 01 §3.4) is the designed candidate and dispatches on the instrument's reading, not before.

## §1 The greps (re-runnable on the device)
```
cd _scratch/v70/ci-1e26912
grep -c 'DeliveryAnomaly\|bus.delivery_anomaly' reports/lifecycle/lifecycle/build/test-results/test/TEST-com.homesynapse.lifecycle.HeroLoopHardwareFreeIT.xml   # 0
cat reports/lifecycle/lifecycle/build/test-results/test/*.xml | grep -c 'DeliveryAnomaly\|bus.delivery_anomaly'                                            # 0
grep -c 'bus.delivery_anomaly' 'log/Build & Check/5_Run check.txt'                                                                                         # 0
grep -o '1e26912[0-9a-f]*' 'log/Build & Check/2_Checkout.txt' | head -1                                                                                    # 1e269127152157aa91138de8002dc0d0545350a0
```
The XML read: `md5 78db6356aa12…`, 51,699 B, 344 lines; the failing testcase at line 269, its stdout at lines 271–329.

## §2 What the hub could not re-execute
A green run's stdout for the same test, to place the engine's normal lines beside this silence — no green artifact of the hero loop is on disk (the August log is a red). The engine's firing has no log line of its own in source (`git grep` for `automation.fired`/`automation_fired` in `core/automation/src/main` returns nothing), so "no dispatch" rests on the absent `zigbee.command_result` and the absent frame, not on an absent engine line. The `bus-soak` instrument is how that comparison gets made.
