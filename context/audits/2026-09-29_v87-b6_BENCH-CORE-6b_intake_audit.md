<!--
file: context/audits/2026-09-29_v87-b6_BENCH-CORE-6b_intake_audit.md
purpose: v87 beat 6 — BENCH-CORE-6b (core `1f1d1e0` → `40412f9` PINNED on the bench card) intaken at its outputs file: the pinned form's reads, the deploy, the pre-registrations of the v85 b3 audit §2 adjudicated mismatches-first, sample 5's arm, Tuesday's nightly line.
audience: the v87 hub · the v88 boot (by §0; it copies the guide's notes when they exist)
state-type: audit (a bench-card intake)
status: FILED — Tue 2026-09-29 ~17:4x CT (instrument 2026-09-29T22:46:26Z)
-->

# v87 beat 6 — BENCH-CORE-6b intake

## §0 Verdict
**BC6b DONE — ACCEPT.** The Pi runs core `40412f9` (pinned; `main` untouched on the clone) with bench `d093a95`. Every pinned read matched its EXPECTED line; boot-health 6/6 · 0 forbidden; both PI-PROBE-3 arms PREDICTED; P4 sample 5 the inverse arm (all fresh — IR-56's unit not queued); Tuesday's nightly MATCHED the pre-registered pair. Wednesday's nightly pair: (`40412f9`, `d093a95`). Owed: the guide's one line and its notes file.

## §1 The record and the reads (Layer 1 the outputs file; Layer 2 the hub's reads of the same file)
`_scratch/v87/2026-09-29_BENCH-CORE-6b_outputs.txt` — 8,587 B; `=== B0 22:30:04Z · B0b 22:30:56Z · B1 22:31:37Z · B2 22:32:50Z · B2-poll 22:33:35Z · B3 22:34:33Z · B4 22:37:25Z` (UTC; the Pi's own log names are UTC−4). Copied verbatim into `context/audits/2026-09-29_BENCH-CORE-6b_outputs.txt`.
| Block | EXPECTED | Read |
|---|---|---|
| B0 | `clone: 1f1d1e0 · porcelain=0 · target=commit · target-ahead-of-clone=2 · main-ahead-of-target=2 · ref=main · bench: d093a95 · ok` | all as expected (lines 4–7, 16) |
| B0b | `key-lines=0` · every 2026-09-29 boot log `permit_join_opened=0` · Tuesday's nightly line | `zigbee.yaml: 571 B sha256 513b2c0171b84d50 key-lines=0` · `nightly: 2026-09-29 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · fleet: 9/9 · re-seen 9 · bench-hero RESTORED ✓ · ON-latency 0.31s` |
| B2 | `HEAD is now at 40412f9 …` · `clone: 40412f9` · `BUILD pid=` | `HEAD is now at 40412f9 feat(state-store,lifecycle): IR-61b — …` · `clone: 40412f9 …` · `BUILD pid=38205 log=~/hs-bench/build-20260929T223251Z.log` |
| B2-poll | `BUILD SUCCESSFUL` | `BUILD SUCCESSFUL in 23s` |
| B3 | stopped → launched → RADIO UP · boot-health 6/6 · `network_resumed` ch 20 / 0x774c · formed 0 resumed 1 relinked 9 · `deployed=40412f9` · `ir61b-class-in-tree=2` · the live order · the TR3 immediate | `[OK] stopped · launched pid 38400 · RADIO UP after 18s` · `[PASS] boot-health — 6/6 positive · 0 forbidden` · `zigbee.network_resumed: channel=20 panId=0x774c` · `formed=0 resumed=1 relinked=9 adopted=0 config_issue=0 cache_loaded=device_cache_loaded: 9` · `registry rows=9` · `deployed=40412f9` · `jvm pid=38542 start=Tue Sep 29 18:35:25 2026` (the boot-health relaunch; Pi-local) · `ir61b-class-in-tree=2 jar=state-store-0.1.0-SNAPSHOT.jar` · live-order and TR3-immediate — §2 |
| B4 | `jvm pid=<n> start=<UTC>` · two PLUGS lines · the night's boot logs `permit_join_opened=0` | `jvm pid=38542 start=22:35:25Z` · `PLUGS@+121s` and `PLUGS@+180s` (§2) · `bench-2026-09-29-183525.log · -183440.log · -043131.log: permit_join_opened=0` |

## §2 The pre-registrations (the v85 b3 audit §2) — mismatches first: none
| # | Predicted | Observed | Arm |
|---|---|---|---|
| PI-PROBE-3 (a) | `registry.projection_live` BEFORE `StateProjection … caught up at position` | `18:35:34.690 … registry.projection_live: devices=9 entities=9 position=201201` then `18:35:34.706 … StateProjection state_projection caught up at position 590036; projection.replay.duration_ms=0 events_replayed=1` — registry first by 16 ms | **PREDICTED** — IR-61b's gate observed |
| PI-PROBE-3 (b) | the TR3's `staleAfter` SET at the immediate read, before its first post-boot report | `TR3-immediate@22:35:45Z: avail=AVAILABLE stale=False staleAfter=1790722401.020825 lastReported=1790721201.020825` — SET; staleAfter − lastReported = 1200.000 s; `lastReported` = 2026-09-29T22:33:21Z, 124 s before the JVM start (22:35:25Z) | **PREDICTED** — the checkpoint's replayed report found its entity through the gate; BC5 obs. 9 closed |
| P4 sample 5 | a Gen4 UNAVAILABLE or `age` > 60 s on the +90 s line (the predicted arm) vs all fresh | `PLUGS@+121s (22:37:26Z)`: G4-1 AVAILABLE age=1s · TR3 AVAILABLE age=89s · G4-2 AVAILABLE age=1s; `PLUGS@+180s (22:38:25Z)`: G4-1 age=2s · TR3 age=148s · G4-2 age=3s; every `stale=False`, every `staleAfter` set (3/3 at +180 s) | **INVERSE** — samples 1–5 clean on app restarts; IR-56's Java unit not queued; the next instrument a plug power-cycle at rehearsal 2 |
| the deploy | 6/6 · 0 forbidden · ch 20 / 0x774c · formed 0 · relinked 9 · adopted 0 · rows 9 · `deployed=40412f9` · `ir61b-class-in-tree=2` · boot logs `permit_join_opened=0` · `staleAfter@180s` 3 set | all read (§1) | **as pre-registered** |
| Tuesday's nightly | on (`1f1d1e0`, `352296d`): `8/9 PASS · fleet: 9/9 · re-seen 9`, 0 forbidden | `2026-09-29 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · fleet: 9/9 · re-seen 9 · bench-hero RESTORED ✓ · ON-latency 0.31s` | **MATCH** — `NIGHTLY:` banked |
The +121 s offset: the card's own rule (the true offset is the sample's value; written, never a STOP). Two JVMs in Block 3 (the restart's pid 38400 at 18:34:40, the boot-health relaunch's pid 38542 at 18:35:25) — the card's known shape.

## §3 Observations (not defects)
- The TR3 reported once after the boot (22:35:57Z → `staleAfter=1790722557.54`) and not again through 22:38:25Z (age 148 s) at a constant 8.4 W: a report-on-change device under a steady load is silent up to its max interval. IR-61's `power_meter` default (180 s) would read it stale at ≈ 22:38:57Z had the read continued; the threshold's true source is the read-back max interval (IR-80 — after the run, §7 row 12). A reading for that AMD, not a row.
- The pinned form (D-v87-4) cost nothing at the rig: the fetch + detach in Block 2 ran inside the same ssh as the build kick; the clone is detached at `40412f9` until BH-3's card returns it to `main`.
- Not re-executed: the Pi's lines themselves (read from the teed file, written by the Pi and the guide's tee); the guide's notes (not yet written at this intake).

## §4 The next
Wednesday's 03:30 CT nightly on (`40412f9`, `d093a95`) — the same pre-registered line. BH-3 (Wed, cloud) lifts the fence; BC7 then puts PJ-2's core on the card. The guide's one line + notes: v88 copies the notes when they exist and flips nothing (the card is EXECUTED at this file).
