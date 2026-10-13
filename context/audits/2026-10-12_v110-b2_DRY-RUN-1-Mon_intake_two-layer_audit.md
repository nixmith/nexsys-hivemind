<!--
file: context/audits/2026-10-12_v110-b2_DRY-RUN-1-Mon_intake_two-layer_audit.md
purpose: The hub's two-layer intake of dry-run #1's Monday half (D0a · D0b · K4 · F1 · D1 · D1-W2) — the provisional line read against the packet's EXPECTs and §P″; the hub's own re-reads of the guide's raw outputs and the core history; the deviations ruled; the findings routed. The guide's record is `audits/2026-10-12_DRY-RUN-1_Mon_guide-notes.md` (verbatim) and `…_raw-outputs.md`.
audience: the v110 hub · v111 (D2's intake) · Nick
state-type: intake audit
status: FILED v110 beat 2 (Mon 2026-10-12 ~20:5x CT; instrument 2026-10-13T01:54:34Z); D2 Tue 2026-10-13 20:04 CT → v111
-->
# DRY-RUN-1 (Mon) intake — two layers

## §0 Verdict
**INTAKEN — the window is OPEN (20:03:53 CT Mon; D2 at 20:04 CT Tue, +24 h at the hour).** P0″ HELD · P1″ the EXPECTED arm (cold exit 99, 49.6 s from launch, 45.4 s from `Loaded`) · **P2″ FAILED AS WRITTEN** — the plain warm relaunch exited 99 again (43.5 s / 40.8 s); the window opened only on the hub-approved contingency (a 31-s read of the store file, then one `bench.sh start`: the registry live 20.4 s after `Loaded`, 9.6 s inside the ≈ 30-s gate) · P3″ K-4 PASS (the IT ran: `skipped="0"`; old way 7,971 ms, new way 4 ms on 1,876,566 rows) · BACKUP-1 Part 0 DONE on the one-step copy (md5 both sides `6dfd6e3c…`, 940,978,176 B, `integrity-pi=ok`) · P6″ / P7″ / P8″ / P9″ their Monday halves RECORDED · P4″ P5″ P10″ P11″ P12″ at D2. Two deviations hub-approved in the sitting (D-v110-11, D-v110-12); four more ruled below. Five findings → the register (IR-148's cell; IR-188..191).

## §1 Layer 1 — the line against the packet
| Field | The line | The packet | Read |
|---|---|---|---|
| `deployed 37f05a9` · bench `cddac94` | D0a | P0″ | HELD |
| `BACKUP copy=940978176 md5-match=yes integrity=ok (one-step)` | D0b amended | §13 | DONE; the amendment ruled D-v110-11 |
| `K-4 PASS old=7971 new=4` | K4 at core `176adad` | P3″ (EXPECT names `2a54145`) | PASS; the sha is stale text, the IT unchanged between them — ACCEPT |
| `F1 total=1876566 avail-rows=481 top=[…]` · `SCAN 1.21s WALK 1.07s` | F1 | P7″ / P8″ | RECORDED (23 types; the sum checked by the guide) |
| `DU store=940.6MB wal=4.2MB free=101.3GB retention=none` | D0a | P6″ (D0 half) | RECORDED; the retention keys came back EMPTY — read at D2's gate |
| `COLD startup_failed +49.6s (card +91s)` | D1 | P1″ | the EXPECTED arm; `+91` is the card's detection delay (bench.sh's 90-s wait), not the failure — IR-190 |
| `W1 FAIL exit 99 +43.5s` | D1 | P2″ | **FAILED as written** |
| `W1-again pre-warmed … booted: LOG1=bench-2026-10-12-210302.log MARK1=11406 POS1=1877415` | D1-W2 | D-v110-12 | the window's slots (D1.txt's `LOG1/MARK1/POS1` are VOID — the failed relaunch's) |
| `timedatectl yes` | D0a | P9″ (D0 half) | HELD |
| `D2 Tue ≈ 20:04 CT` | the guide's +24 h | the packet said ≈ 19:00 | **the hub names 20:04 CT** |

## §2 Layer 2 — the hub's own reads
1. **The raw outputs** (`_scratch/v107/dr1/`, copied into `…_raw-outputs.md`): `D1-W2.txt` — `pre-warm 01:02:31Z … db=941400064 … -wal=0` · `Mem: 4049 … 943` → `pre-warm done 01:03:02Z` · `Mem: … 1296` (31 s; +353 MB cached; a 4-GB board) · `registry.projection_live: devices=10 entities=10 position=849602` at `21:03:24.758` EDT · `zigbee.network_resumed: channel=20 panId=0x774c` at `21:03:33.596` · `LOG1b=bench-2026-10-12-210302.log MARK1b=11406` · `POS1b=1877415` · `W2 status: [OK] running (pid 12899)`. `D0b.txt` — the `method:` line; `backup: 28 s bytes=940978176 md5-pi=6dfd6e3c7441fb5a224b7ee666cc0d16 integrity-pi=ok copy-rows=1876566`; `scp: 16 s … md5-desk=6dfd6e3c…` (equal). The K4 XML — `tests="1" skipped="0" failures="0" errors="0"`; `registry-cold.k4: source=C:\Users\Nick\hs-bench\backups\homesynapse-events-2026-10-12.db bytes=940978176`. `F1.txt` — `total=1876566` · `avail-rows=481` · `SCAN … seconds=1.21` · `WALK … seconds=1.07` (one cp1252 byte at offset 1280, the WALK line's dash — IR-146/183's desk class). The line's every number is in the files.
2. **The fix's ancestry** (`git log 37f05a9..176adad`, read-only): REGISTRY-COLD-1 T1 `af46e11` (the registries rebuild from their four event types) and T2 `6a03403` (RegistryGate: fails only when the replay stops progressing) precede `2a54145`; `merge-base --is-ancestor 2a54145` = yes for `ba08dd8`, `e11ae20` and `176adad` — **every Friday candidate carries the fix.** `maxPolls = 1_500` still reads at `HomeSynapseCore.java:1556` (T2's gate is progress-based beside it).
3. **The margin arithmetic** (the hub's, from the guide's stamps): warm, 1,877,389 events replayed in 20.4 s ≈ 92 k events/s; the gate ≈ 30 s → ≈ 2.76 M events; the store grows ≈ 95.6 k rows/day (184,743 in 46 h 22 min since SOAK-NIGHT-2's S0) → **`37f05a9`'s WARM boot overruns the gate at ≈ 2.76 M events ≈ Oct 22** (dry-run #2's day); cold, it fails today. Sun Oct 18's binary rollback (≈ 2.45 M events, a ≈ 3-s warm margin) lands on the edge; the run's rollback target must be a post-fix build (`ba08dd8` at the oldest) — Friday's go/no-go input (D-v110-16).
4. **The `.backup` mechanism** (the hub's reading of the sqlite3 shell and the backup API's documented restart rule, D-v110-11): confirmed; the guide's container measurement (12 commits/s → unfinished at 120 s; one step → 0.86 s) is read, not re-run here — DISCLOSED. The one-step form is BACKUP-1's form from tonight (IR-188).
5. **Not re-executed:** the Pi's clocks (the guide converted EDT → CT with the offset named); the K4 run itself (the XML is the evidence; the desk's console hides the IT by the build convention — IR-190); the desk's 1.2 T free.

## §3 Deviations ruled
- **D-v110-11 D0b AMEND** (hub, 19:39 CT): the one-step Python backup for the CLI's `.backup`; one `method:` line; tested and stub-dry-run by the guide before it was shown — ACCEPT.
- **D-v110-12 W1-CONTINGENCY yes** (hub, 20:01 CT): a read-only pre-warm (`cat db db-wal > /dev/null`, `free -m`), then one `bench.sh start`; the `LOG1b/MARK1b/POS1b` labels (D-BC9-4) — ACCEPT; the rig acts were three restarts in all (D1's two, D1-W2's one); nothing written, no hands.
- K4 at `176adad` (the EXPECT's `2a54145` stale since J3 landed Monday 09:3x) — ACCEPT, no row. The guide-added read-only helpers (the STATE helper; `sudo -n sh -c true`; the K4 XML copied beside K4.txt) — ACCEPT. The two-message rule kept.

## §4 The findings → the register
- **IR-148's cell:** tonight's deterministic reproduction; the warm margin (9.6 s at 941 MB) and its ≈ Oct 22 expiry at `37f05a9`; the pre-warm (31 s / 941 MB) as the pre-fix mitigation; the fix's shas in every Friday candidate; the rollback-target rule.
- **IR-188** `sqlite3 .backup` restarts on every concurrent commit — BACKUP-1's form is the one-step copy (BC10's "BACKUP-1 first", `BACKUP-NIGHTLY:`, PI-2's BLOCK 1).
- **IR-189** the pre-warm as a launcher step (`bench.sh start` / `ExecStartPre`) for a pre-fix binary and the household power-cut case.
- **IR-190** the packet form for dry-run #2's cut: D1's `+<s>` is detection time (bench.sh's 90-s wait; `tail -4` cuts the lines; the log stamps are the instrument); K4's console cannot show the IT (`testLogging` in the conventions — the XML is the evidence); the desk's python calls under `PYTHONIOENCODING=utf-8` (IR-183's card rule; F1's card predates it).
- **IR-191** the copy on the desk is a read-only instrument: the all-time `command_confirmation_timed_out` share (1,714 of 3,009 `command_issued`, 57 %) by device and by week — the hero's own claim (IR-184) and OR-HUE-REPORTING-DEAD; R-H's per-day constant from `ingest_time`.
