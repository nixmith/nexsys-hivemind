<!--
file: context/audits/2026-09-11_FIX-2b-i_intake_two-layer-audit_v70-b9.md
purpose: The hub's two-layer intake audit of FIX-2b-i's return (context/audits/2026-09-11_FIX-2b-i_return.md, 12,215 B): the claims, the hub's re-execution at the bytes, the ruling on R1 (the passthrough form), what the runner's next red will carry.
audience: the hub · Nick (§0)
state-type: intake audit (filed; never rewritten)
status: FILED at v70 beat 9 (Fri 2026-09-11 ~22:1x CT; instrument 2026-09-12T03:13:45Z) — the post-close intake, on Nick's word.
-->

# FIX-2b-i intake — two layers (v70 beat 9)

## §0 Verdict
**ACCEPT.** 13 = 11 M + 2 A with row C in, exactly the Files table; nothing staged; the HERO-1b lane's files untouched. P1–P4 HELD, P2 on its main arm (`jcmd` attaches to the test JVM on the desk: `bus.thread_dump: threads=22 shown=1 file=…`). The desk suites are green: event-bus 230, rest-api 152, lifecycle 82 → 83; `spotlessCheck` green. One `[REVIEW]` ruled below in the lane's favour. From this landing a runner red carries `pending=<n>` on every subscriber line and the frames of every `hs-*` thread and every thread with a `com.homesynapse` frame in `<system-out>`, plus the JDK's pinned-thread trace if a virtual thread pins.

## §1 Layer 1 — the claims, read critically
Red-first in stages: compile-red (the seven-argument constructor and the missing class), the six rest-api sites red after the record change, behaviour-red on an inert seam, then green. The lane probed the JDK's dump grammar before pinning it (`-format=plain|json`; `text` works by fall-through — I1). It measured all three arms of the loop override (property 3 → 3; env 3 → 3; neither → 20). It corrected the instruction's javadoc claim ("0 in REPLAY/TRANSITION") after reading `resume()` — the LIVE queue is not cleared on SUSPENDED → REPLAY — and worded the field honestly.

## §2 Layer 2 — the hub's re-execution at the bytes (device, 2026-09-12T03:13:45Z)
1. **Census at porcelain, scoped to `core api lifecycle build-logic`:** 11 M + 2 A. The eleven M: `DlqStatusEndpointTest.java` (6/6), `homesynapse.java-conventions.gradle.kts` (+15), `core/event-bus/MODULE_CONTEXT.md` (2/2), `InProcessEventBus.java` (+1), `SubscriberSnapshot.java` (+15), `lifecycle/lifecycle/MODULE_CONTEXT.md` (6/1), the five FIX-2a test files; the two A: `BusThreadDump.java` (283 lines), `BusThreadDumpTest.java` (116).
2. **The conventions diff, read whole:** `jvmArgs("-Djdk.tracePinnedThreads=short")` and `providers.systemProperty("homesynapse.soak.loops").orNull?.let { systemProperty(…, it) }` — the conditional form; nothing else.
3. **The record:** `pendingDepth` after `dlqDepth`; `buildSnapshot` passes `runtime.pendingPositions().size()`; `new SubscriberSnapshot(` sites still 6 + 1 + 3.
4. **The dump on the timeout paths:** `BusThreadDump.capture` referenced twice in the hero IT and twice in the census IT; `BusSoakIT` calls the census IT's diagnostic (0 direct references, as the instruction allowed).
5. **The XML sets on the desk:** event-bus 230 testcases / 0 failing suites; rest-api 152 / 0; lifecycle 83 / 0.
6. **Wall-clock:** `System.currentTimeMillis()` once, in the dump file's name, documented in the javadoc.
**Not re-executed (disclosed):** the `jcmd` probe and the three override arms (taken from the return's measured tokens).

## §3 Rulings
- **R1 — ACCEPT the conditional passthrough.** The instruction's literal `getOrElse("20")` would have set the property on every run and made the env-var fallback dead; the lane shipped what the FIX-2a audit had docketed and measured it. The instruction's sentence was the hub's error.
- **I1 (`-format=plain`) — noted.** **O2's caveat** (the pinned-thread trace prints from the pinned thread; if a run ever hangs at a pin, drop the flag) — carried into the OR-BUS row.
- **What the next red must show:** `pending=` per subscriber and the `bus.thread:` / `bus.thread_frame:` lines; FIX-2b-ii is authored on that reading against H1–H4 of the cc05a54 audit.

## §4 The landing (Nick's hands)
The thirteen files by explicit path (never `-A`: the HERO-1b files share the tree) → the commit from `_scratch/2026-09-11_core_FIX-2b-i_commit-msg.txt` → push. Its `ci` run is sample #11, the first that can name the blocked frame; a lifecycle red there is the reading — its log archive and `test-reports` go under `_scratch/v71/ci-<sha>/`.
