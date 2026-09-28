<!-- REHEARSAL 1 (D-v81-1) return, Mon 2026-09-28 12:19–13:4x CT. Running core 1f1d1e0 (BENCH-CORE-5; hub's correction 12:41). Pi clock = EDT; Pi stamps converted to CT. -->

# §0 The pre-registrations
- **P1 HELD** — `rows<=461489: 461489` (= N). COUNT 461489 (12:21 CT) → 464483 (core dead, 13:02) → 464682 (13:06); contiguous at every read; `integrity ok` ×3. Kill 18:00:15Z = 13:00:15 CT; `launched` 14:03:25 Pi = 13:03:25 CT; down ≈ 3 min 10 s.
- **P2 HELD on `devices=9 entities=9`; the `position ≥ MAX-before` clause REFUTED AS WRITTEN** — `position=201201` < 461489, but 201201 is the value at all five boots on record (BC-3 ×2 Sun AM; BC-5 ×3 Sun PM; ≈344k–384k rows then; folder-verified): the field is the last registry event's position, not the store head; the clause cannot hold here (July's `25065` = the head only because nothing else was written). Re-specify; `entities-equal: 9/9` decided the replay.
- **P3 HELD** — `formed=0 resumed=1 relinked=9 permit=0 cache=device_cache_loaded: 9`; RADIO UP after 16 s; `network_resumed: channel=20 panId=0x774c` 14:03:41.617 Pi = 13:03:41 CT; the nine relinked IEEEs identical to BC-3's; failure tokens empty ×2.
- **P4 REFUTED (inverse arm)** — 13:10 CT (≈ 6.5 min after `launched`, NOT the pre-registered 90 s): `G4-1 AVAILABLE age=2s ver=126187 · G4-2 AVAILABLE age=2s ver=122111 · TR3 AVAILABLE age=40s ver=8459`; the 90-s window was not sampled. Exclusion rule moot: the baseline's non-AVAILABLE entity is the Hue bulb `01KX1PA4HSJ581GASYB7DHE40F` (UNAVAILABLE before AND after; lastReported epoch 1784422155 ≈ 2026-07-18 CT), not a plug — action 1's EXPECT `9 AVAILABLE` was wrong on the script's own "Hue off-network" premise.
- **P5 HELD on trigger + run; command clause NOT-REACHED (not observed)** — bench-hero run `01M3MM0QXR3QF7MDX5AJ60H05W` triggeredAt 18:21:45.268594Z = 13:21:45 CT (Pi) vs Nick's walk 13:21:47 ±1 CT (PC clock); `run_body_entered` 14:21:45.274 Pi; COMPLETED, terminalReason null. `occupied=true` not read directly (harvest 13:23:49 CT; sensor cleared 13:23:16, 92 s after the walk); a run's triggeredAt equals the sensor's own change-time (proven on the wave run) and stands in. Command clause: `bench.sh events | tail -8` returned the OLDEST 8 of a newest-first page (Sun 03:31 CT S31 legs) and the log grep `command_` matches nothing in any log on file — both instruments mis-aimed. Caveat: the 03P was handled/moved DURING the walk (Nick 13:38).
- **P6 HELD** — `turn_off` http 202 cmd `01M3MN349RC2K8HQXHVS4WQ7Y8` acceptedAt 13:40:32 CT → +20 s `on=False W=0.0 age=-0s`, lamp dark; `turn_on` http 202 cmd `01M3MN5FJAMC2T9RQ6BGSQTH44` 13:41:49 CT → +20 s `on=True W=42.0 age=2s`, lamp lit. Before: plug 42.0 W / 0.34 A / 124.0 V vs Kill A Watt 42.2 W.
- Notes: `runs-before: 50` = the page limit, not a count · four bench-hero runs today in the log: 13:12:42 (wave), 13:21:45 (walk), 13:34:19 and 13:43:47 CT (rig build / rig down, sensor moved) · 03P clear-time 63 s after the wave, 92 s after the walk.

# §1 The SAY lines (verbatim; actions 4 and 10 cut to their decisive lines — §3)
1: `pid 32925 · boot bench-2026-09-28-043130.log` / `store-before: 461489|461489 integrity ok` / `entities-before: 9 entities; 8 AVAILABLE` / `runs-before: 50`
2: `killing 32925 at 18:00:15Z` / `dead`
3: `store-dead: 464483|464483 integrity ok`
4: `[OK] launched pid 33988 -> …/bench-2026-09-28-140325.log` / `[OK] RADIO UP after 16s` / `projection_live: devices=9 entities=9 position=201201` / 9× `device_relinked … re-pairing, no new adoption` / `network_resumed: channel=20 panId=0x774c` / failure tokens empty ×2 / `formed=0 resumed=1 relinked=9 permit=0 cache=device_cache_loaded: 9`
5: `store-after: 464682|464682 integrity ok` / `entities-equal: 9/9 (the moving measurements excluded)`
6: `rows<=461489: 461489`
7: `G4-1 AVAILABLE on=False W=0.0 ver=126187 age=2s` / `TR3 AVAILABLE on=True W=0.0 ver=8459 age=40s` / `G4-2 AVAILABLE on=False W=0.0 ver=122111 age=2s`
8: (no typed `8:` line) 13:13 CT: occupied false ver 3758 lastChanged 1790540972.375 → [hand wave] occupied true ver 3760 lastChanged 1790619162.278; 13:18 CT: occupied false ver 3762 lastChanged 1790619225.971
9: `9: walked at 13:21:47 +/- 1`
10: (B10.txt, byte-complete) occupied false ver 3767 lastReported 1790619796.848 / runs: `01M3MM0QXR3QF7MDX5AJ60H05W … 18:21:45.268594Z … COMPLETED`, `01M3MKG5NHP71FFXAX8QRJ45MG … 18:12:42.278026Z` / events: `325019|command_dispatched|1790497881343200` … `325010|command_issued|1790497874134709`
11: `11: on=true A=42.2` / `moved 03P during the walk` (read: 0.34 A, 42.0 W, 64.0 Wh, 124.0 V, on true)
12: `http 202` commandId `01M3MN349RC2K8HQXHVS4WQ7Y8` acceptedAt `2026-09-28T18:40:32.056202364Z` / `G4-1 on=False W=0.0 age=-0s` / "Confirmed: the lamp went dark"
13: `http 202` commandId `01M3MN5FJAMC2T9RQ6BGSQTH44` acceptedAt `2026-09-28T18:41:49.130747545Z` / `G4-1 on=True W=42.0 age=2s` / "Can confirm that the lamp lit."
14: `14: rig down`
15: `ls`: A1.txt 144 · A5.txt 95 · B10.txt 10690 · boot-and-run-lines.txt 3232 · entities-after.json 3735 · entities-before.json 3737 / `16`
16: —

# §2 Everything else Nick said (verbatim, CT)
- 12:19 `STATE: plugs in wall · rig on desk · windows A and B open`
- 12:21 "Ensure all results throughout this entire conversation are being articulately and accurately as possible for the hub/orchestration session to make the best, most sound decisions possible based on the best data and feedback (not necessarily what's "expected" or "correct") we could provide."
- 12:41 "CONTINUE — the hub's ruling. The 8/9 baseline is data, not a fault: nothing has run, and P4's own header anticipates a Gen4 down. Record it in §3 as your one departure exactly as you wrote it. Adjudicate P4 at the end AGAINST the baseline: a plug already not AVAILABLE before the kill is excluded from sample 4 (the other Gen4 decides; name the excluded plug in §0 once entities-before.json says which). One correction for the return: the core on the card is 1f1d1e0 (BENCH-CORE-5, Sun 18:02 CT), not d22a8a4 — d22a8a4 is your header's FLOOR, not the running sha; 04:31:30 Pi = 03:31:30 CT is this morning's nightly restart on 1f1d1e0. No added reads. Next action."
- 13:13 "Two commands, separated by one hand wave in front of the 03P:"
- 13:25 "Here are the results. Let me know if we need to re-run anything. I have positioned the 03P somewhere I can "more easily use" for walking in a designated field of view, and with a little bit better lighting."
- 13:33 "One quick clarification to "lamp into G4-1": you mean the clamp lamp, and not the lamp with the Hue smart bulb screwed in, correct?" (guide: the clamp lamp)
- 13:38 "moved 03P during the walk"

# §3 The guide's departures
- Continued past action 1's EXPECT mismatch — 8/9 AVAILABLE, a pre-existing fleet condition, on Nick's call: the guide put STOP/CONTINUE to Nick instead of stopping; the hub's ruling came back 12:41 CT.
- The STATE line named the floor sha `d22a8a4` (BC-3's return) as "the core"; the running sha is `1f1d1e0` (BC-5) — hub-corrected, folder-verified.
- Read the ClaudeFolder on Nick's PC (never the Pi) five times beyond the script (pre-conditions; 1f1d1e0; projection_live history; reh1 files; log tokens + IEEEs). No Pi reads added; no DO block edited.
- Continued through two operator departures (hand wave before the walk; 03P moved during the walk) and action 8's missing typed line — nothing at risk; all recorded. Asked for two extras beyond the SAY lines: `moved 03P before|after` (action 11); the Kill A Watt reading on 12/13 (not given).
- §1 cuts actions 4 and 10 to their decisive lines (action 10 byte-complete in B10.txt; relink lines verbatim in boot-and-run-lines.txt; the script did not tee action 4); §0 carries notes after P6. Action 7 ran ≈ 6.5 min after `launched`, not 90 s — the script's order.

# §4 Files under `_scratch/v81/mon0928/reh1/`
A1.txt 144 · A5.txt 95 · B10.txt 10690 · boot-and-run-lines.txt 3232 (16 lines; zero `command_` matches) · entities-before.json 3737 · entities-after.json 3735
RETURNED _scratch/v81/mon0928/REHEARSAL-1_return.md 8187
