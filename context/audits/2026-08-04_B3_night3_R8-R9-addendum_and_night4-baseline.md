<!--
file: context/audits/2026-08-04_B3_night3_R8-R9-addendum_and_night4-baseline.md
purpose: Addendum to the BLOCK-R adjudication — the R-8/R-9 reads land the boot-timeline measurement (the leg fires 0.772 s after EMBER_NETWORK_UP), the report-cadence bracket (~5-min-scale, sparse), the coincidence arithmetic that upgrades EDGE-OCCURRED to effectively PROVEN, and the re-pinned night-4 baseline with its single-read discriminator.
audience: Hub (v45), Nick, the fix-ruling beat
state-type: adjudication addendum (point-in-time)
status: FILED 2026-08-04 (v45 hub, beat 4) — before the night-4 fire
provenance: Nick's R-8/R-9 paste (2026-08-04 00:33–00:38 UTC = Aug-3 evening local) + his early dry-run of the Aug-4 gate form (harmless; re-runs after the fire). Parent: 2026-08-04_B3_night3_blockR-adjudication_v45-beat-3.md.
-->

# R-8/R-9 Addendum — the boot-window measured · the night-4 baseline (v45 beat 4)

## 1. R-8 — the suite-boot timeline, now measured to the millisecond

The suite boot (`bench-2026-08-03-043039.log`, 88 lines, read whole): process start 04:30:40.342 → RUNNING (quiesced, automations=0) 04:30:43.445 → transport 04:30:49.282 → ASH 04:30:50.884 → **`network_resumed`/EMBER_NETWORK_UP 04:30:51.004 → the s31 turn_on ACCEPTED 04:30:51.776 — the asserted command enters a mesh that has been up for 772 ms.** DISPATCHED at +4 ms; CONFIRMATION_TIMED_OUT 5.19 s later. The comparison points from the same hour: the settle CONFIRMED in 3.59 s at ~+45 s post-resume — **10 s after the usb leg's deliberate dongle power-cycle recovery** (port died 04:31:21, watchdog reopened 04:31:26 after two expected-failed attempts under the 10-s power-off) — and the Aug-2 settle CONFIRMED in 143 ms at ~+40 s. The boot-adjacent cold-mesh window is no longer an inference; it is the measured difference between +0.77 s (times out) and +40–55 s (confirms fast, even straight through a port power-cycle).

Also on the record from R-8: the identify leg's honest-unconfirmed register verbatim (`command_result: outcome=unconfirmed … no confirmation surface exists for 'identify'; the command was issued and is not tracked`) — a clean honesty exhibit; and the usb-cycle recovery arc (`reopen_no_target` → RSTACK → reopened, attempts 1–2 failed under the 10-s off-window BY DESIGN) — benign, the watchdog working as built.

## 2. R-9 — the cadence bracket, and the edge-proof upgrade

Two state reads 3 min apart (00:33:48 / 00:36:48 UTC) + the 00:38:23 dry-run read: `stateVersion` 4717 → 4717 → 4717; `lastReported` frozen at 00:33:25Z across all three. Spanning back to R-5 (23:48:25Z, version 4708): **+9 versions in 45 minutes ≈ one device-originated report per ~5 minutes, irregular, with ≥5-minute quiet stretches.** Consequence for §1 of the parent adjudication: at ~0.0033 reports/s, the probability that the Aug-2 settle's 143 ms CONFIRMED was a coincidental periodic report is ~0.05% (and ~1.2% for the Aug-3 3.59 s case; joint ≈ 10⁻⁵). **EDGE-OCCURRED on both FAIL nights is upgraded from strongly-favored to effectively PROVEN** — the turn_ons fired the relay; the ON-edge evidence was late/absent inside the window. The exact source of the ~5-min day traffic (native reporting vs ping-adjacent bookkeeping) stays a curiosity, not load-bearing.

## 3. The night-4 baseline, RE-PINNED (supersedes the beat-3 pin)

**`stateVersion=4717` · `lastChanged=1785745896.014 = 08:31:36.014Z Aug-3` · `on=false` · `lastReported≈00:33:25Z`** (read 00:38:23Z). The morning discriminator is ONE field: **`lastChanged`.** An Aug-4 timestamp (~08:30:5x–08:31:4xZ) ⇒ the relay edged (PASS, or FAIL-with-late-report — the margin class confirmed either way). Frozen at `08:31:36.014Z Aug-3` with the settle reading no-change ⇒ genuine no-edge ⇒ H-2b revives at the delivery layer. `stateVersion` deltas are corroborating only (day traffic makes them noisy). On a FAIL, `post-window-state.json` reads per the parent's pre-stated view-lag caveat: `on=true` proves the edge; `on=false` proves nothing. Nick's early run of the gate form (before the fire) was harmless; the form re-runs after ~04:35.

## 4. Standing

Hands off the S31 through the fire. The fix ruling waits for the morning arithmetic; REC unchanged (the F1-class suite-position amendment — the settles prove the path healthy at +40–55 s). Beat-3 landed `56ab964` (exactly 3, pushed). The pm-handoff rotation is flagged as a lull candidate (the file is at ~218 KB; not tonight — hot-file discipline).
