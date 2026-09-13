<!--
file: context/handoff/archive/pm-handoff-beats-v70b4-rotated-2026-09-12.md
purpose: v70 beat 4 rotated VERBATIM out of pm-handoff.md at v71 beat 6 (the live cap is 12 blocks). bytes(kept) + bytes(archived body) + 1 = bytes(before), asserted.
status: ARCHIVED 2026-09-12 (v71 beat 6)
-->

## 2026-09-11 (v70 beat 4 — FIX-2a authored: the instrument half, test-only; the paste handed, Fri 2026-09-11 ~18:1x CT (instrument 2026-09-11T23:19:53Z))

**Grounded at `1e26912`** (every claim with its line): `awaitTrue` at `HeroLoopHardwareFreeIT:607–:615` throws a bare message; `core.eventBus().subscribers()` (`InProcessEventBus:467`) already exposes `SubscriberSnapshot(subscriberId, mode, checkpoint, dlqDepth, crashCount, oldestParkedAt)`; `liveLoop` (`:525–:592`) parks on an empty `pendingPositions` queue and writes the checkpoint only on `SUCCESS` and only for non-atomic subscribers; the anomaly handler (`HomeSynapseCore:557`) has six kinds, none naming the hero loop's silence; the census definition and the frozen tokens are TR-1's (§1, §3). So the instrument needs no production seam. **Authored:** `context/instructions/2026-09-11_coder-lane_FIX-2a_bus-silent-drop_instrument-first_coding-instruction.md` (24434 B): (A) `BusAwaitDiagnostic` + its unit test + the hero IT's failure path (store head · awaited position · one line per subscriber); (B) `BusPositionCensusIT` (TR-1b's IT: the manifest of six, `bus.position_census*` tokens, `missed=0` asserted for non-atomic subscribers with an empty DLQ); (C) `BusSoakIT` (K=20 loops, three runs, `bus.soak:` line with p50/p99/max and the anomaly count via a `ListAppender`). Files 6 = 2 M + 4 A; module-info unchanged; eleven STOP gates with lines; P1–P4 each with its inverse arm and the artifact it is read from — P2 is the frequency claim (the class reproduces on the desk at least once in three runs of 20). FIX-2b (checkpoint-driven LIVE delivery; the AMD to Doc 01 §3.4) is authored on the lane's §7, not before. **Handed:** the §14 paste as the one act (the Java slot; unattended while Nick is at the rig); the beats 3–4 card held behind it. **Next:** the H8-a paste at 18:45 by the send · b5 HERO-1b's charter · b6 P-1 · the intakes. Order: hivemind 8 = 4 M + 4 A, beats 3–4 in one card (computed from porcelain inside the splice). ctx: beat 4 · calls ≈50 · read ≈205 KB · wrote ≈85 KB

**Leverage line:** the desk reproduces the class under a diagnostic before anyone touches the bus; FIX-2b starts from a distribution, not a guess.
**The alternative shape, rejected:** the structural fix now — a bus change with no failing test that names the drop is the unmeasured hop the ledger forbids.
**2029 test:** the tokens are TR-1's frozen grammar; every gate cites its line.

