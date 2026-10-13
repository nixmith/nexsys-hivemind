<!--
file: _scratch/v107/dr1/DRY-RUN-1_guide-notes.md
purpose: DRY-RUN-1's guide notes for MONDAY, PROVISIONAL (SOAK-NIGHT-2's practice). Tuesday's `DRY-RUN-1_guide-return.md` supersedes this file and leaves it in place. Contents: D2's slots, the provisional line, the record of D0a · D0b (amended, D-v110-11) · K4 · F1 · the sudo probe · D1 · D1-W2 (W1-CONTINGENCY yes), the deviations, the observations, and the pre-registrations read so far. The guide recorded and never adjudicated; every number below is from the dr1 files, which match Nick's pastes byte for byte.
clocks: CT = Nick's; Pi log names and lines = EDT = CT + 1 h; Z = UTC = CT + 5 h. Every conversion and difference was run in code.
written: Mon 2026-10-12 ≈ 20:1x CT by the DRY-RUN-1 guide session (a fresh Cowork conversation; ClaudeFolder connected).
-->

# DRY-RUN-1 — guide notes, Monday (provisional)

## For Tuesday's guide: D2's slots (from D1-W2.txt, NOT from D1.txt)
- `<LOG1>` = `bench-2026-10-12-210302.log` · `<MARK1>` = `11406` · `<POS1>` = `1877415`. D2's first line becomes `ssh pi "bash -s bench-2026-10-12-210302.log 11406 1877415" <<'EOF_D2' …`.
- **VOID:** D1.txt's `LOG1=bench-2026-10-12-205319.log MARK1=4068 POS1=1877395` belong to the W1 relaunch, which exited 99. They do not mark the start of the window.
- **The window opened** on the pre-warmed relaunch: launched 21:03:02 EDT (= 20:03:02 CT = 01:03:02Z); `network_up` at 21:03:33.596 EDT (= 20:03:33.596 CT); MARK1b read at 01:03:53Z (= 20:03:53 CT). **+24 h = Tue 2026-10-13 20:03:53 CT.** The packet's "≈ 19:00 CT" assumed the window would open at about 19:00. The hub names D2's hour.
- The v110 hub may hand D2 back amended with IR-56's 90-s read (v110's row (ii)). If so, run the card the hub hands, with the slots above.
- The nightly restart at about 03:30 CT starts a second log; the D2 card already reads both. P12″ looks at that nightly boot.

## The provisional line (Monday)
`DRY-RUN-1 (Mon): deployed 37f05a9 · BACKUP copy=940978176 md5-match=yes integrity=ok (one-step, D-v110-11) · K-4 PASS old=7971 new=4 · F1 total=1876566 avail-rows=481 top=[state_reported=1202395 · state_changed=631933 · automation_action_completed=14364] · SCAN 1.21s WALK 1.07s · DU store=940.6MB wal=4.2MB free=101.3GB retention=none · COLD startup_failed +49.6s (card +91s) · W1 FAIL exit 99 +43.5s · W1-again pre-warmed (W1-CONTINGENCY yes) booted: LOG1=bench-2026-10-12-210302.log MARK1=11406 POS1=1877415 · timedatectl yes · D2 Tue ≈ 20:04 CT (+24 h) · NOTES _scratch/v107/dr1/DRY-RUN-1_guide-notes.md`

## §0 The pre-registrations as read so far (§P″ order; the hub adjudicates)
- **P0″ THE PREMISE — HELD.** D0a: `deployed=37f05a9 ref=HEAD bench=cddac94`. Desk free space 1.2T (needs ≥ 3 GB). The card has `free=101282185216` (needs ≥ 2 GB).
- **P1″ THE COLD START's "before" (IR-148) — the EXPECTED arm.** The cache was dropped (`cache=326M`). Cold launch `bench-2026-10-12-205143.log` (20:51:43 EDT = 19:51:43 CT = 00:51:43Z). `Loaded 10 entities … at position 1877389` at 20:51:47.130. `lifecycle.startup_failed: phase=CORE_DOMAIN subsystem=state-store` at 20:52:32.568 EDT (= 19:52:32.568 CT), then `IllegalStateException: registry projection did not reach LIVE within ~30s during startup`, then `HomeSynapse Core exiting: code=99 (UNEXPECTED_ERROR)`.
  - **Launch → startup_failed: 49.568 s** (± 1 s, because the log name is to the second). Loaded → startup_failed: 45.438 s (PKG-FRESH-1 measured the same interval at 44.8 s and 38.3 s).
  - The card printed `COLD: startup_failed at +91 s`. That is the detection time, not the failure time: bench.sh at cddac94 (`do_start`) waits its full 90 s for `zigbee.network_up` or `integration.failed`, never for `startup_failed` or the pid, and the card only checks afterward.
  - `network_formed`: none (the failure happens before the Zigbee phase).
- **P2″ THE WARM RELAUNCH BOOTS — FAILED as written.**
  - W1 (`sleep 5; bench.sh start`) launched `bench-2026-10-12-205319.log` (20:53:19 EDT = 19:53:19 CT). `Loaded …` at 20:53:21.737; `startup_failed` at 20:54:02.530 EDT (= 19:54:02.530 CT); exit 99. Launch → fail 43.530 s; Loaded → fail 40.793 s. `W1 status: [!!] NOT running`.
  - Then **W1-CONTINGENCY yes** (the hub, 20:01 CT): a read-only pre-warm, then W1 again (one start). It **booted**: `registry.projection_live: devices=10 entities=10 position=849602` at 21:03:24.758 EDT, i.e. **22.758 s after launch and 20.421 s after Loaded** (about 9.6 s inside the ≈ 30-s gate); `network_resumed: channel=20 panId=0x774c` and `network_up` at 21:03:33.596 (31.596 s); `W2 status: [OK] running (pid 12899)`.
  - The Core was down for about 12 min (the D1 stop at ≈ 19:51:3x CT → network_up at 20:03:33.596 CT).
- **P3″ K-4 — PASS on the real store.** `BUILD SUCCESSFUL in 17s`. The test ran (not skipped), per the XML: `tests=1 skipped=0 failures=0 errors=0 time=9.216`. The IT's line: `registry-cold.k4: head=1876566 old_way: rows_walked=1876566 parked=0 suspended=false ms=7971 | new_way: rows_passed=20 skipped=0 ms=4 | devices=10 entities=10`. Run on the desk at core `176adad` (the EXPECT's `2a54145` is stale: J3 landed Monday morning; the IT and every lifecycle/persistence main source are unchanged between the two).
- **P8″ A4 (desk floors).** SCAN 1.21 s (236,209,434 payload bytes) · WALK 1.07 s · K-4's old way 7,971 ms (1,876,566 rows).
- **P9″ timedatectl (D0 half).** `NTPSynchronized=yes Timezone=America/New_York` at D0a. D2 reads the other half.
- **BACKUP-1 Part 0 — DONE.** md5-pi = md5-desk = `6dfd6e3c7441fb5a224b7ee666cc0d16`; 940,978,176 B on both sides; `integrity-pi=ok`; `copy-rows=1876566` = `rows-now`. Pi copy: `/home/homesynapse/hs-bench/backups/homesynapse-events-2026-10-12.db`. Desk (off-device) copy: `~/hs-bench/backups/homesynapse-events-2026-10-12.db` (C:\Users\Nick\hs-bench\backups\).
- **P6″ R4 (D0 half).** `homesynapse-events.db=940638208` · `-wal=4202432` · `-shm=32768` · `dir=944884021` · `free=101282185216` · `card= 117G 95G 16%` · **retention keys: none printed** (the grep of `~/.nexsys`, `~/hs-bench/*.yaml|*.yml`, `~/hs-bench/config` came back empty) · `home_id:` empty. D2 supplies the other half.
- **P7″ F1 (the store, all time).** 23 types; `total=1876566` equals the sum of the type lines (checked). See the record. `rows-24h` comes from D2.
- P4″, P5″, P10″, P11″, P12″, the second half of P6″, the second half of P9″, and the household sentences: Tuesday (D2).

## §1 The record: clocks, slots, and Nick's words whole
| CT (Mon) | what | file in dr1 (bytes · md5) |
|---|---|---|
| 19:16 | session opened: "Read and follow all instructions to guide me through this session, such that we can provide the best possible feedback and data/results to the hub/orchestration session as possible." + the packet pasted whole (32,329 B, md5 `0f6609fa38bb1cebd7da39e885b786c1` = the hivemind's committed copy at `5f951d7`) | — |
| 19:2x | guide pre-flight (read-only on the desk folder): desk HEADs hivemind `e6a7ecc` · core `176adad` · bench `6a40a10` (BENCH-BOOT-1 landed 18:36; not on the Pi) | — |
| 19:28 | STATE (printed by the guide's desk-only helper): `STATE: HIVE: LANDED e6a7ecc \| CORE: main 176adad (not deployed) \| the Pi: 37f05a9 since Sat 12:00 CT (BC9's Part A) \| the time is 19:28 CT \| DESK-FREE: 1.2T` | — |
| 19:30:49 | D0a (00:30:49Z; Pi 20:30:49 EDT). LOG0=`bench-2026-10-12-043246.log` (04:32:46 EDT = 03:32:46 CT, the nightly) MARK0=494463 POS0=1875960 | D0a.txt 765 · `97cd7f504abd5317fe31ff3cd91080c3` |
| 19:39 | Nick (the hub's ruling), whole — see "Nick's words" below | — |
| 19:40:02–19:40:40 | D0b amended (00:40:02Z–00:40:40Z); then scp | D0b.txt 504 · `90ec619c0a6db9f97e2b5286427fce9c` |
| 19:42:32–19:42:52 | K4 (00:42:32Z–00:42:52Z); the XML's timestamp 00:42:42Z | K4.txt 194 · `2166dc5ee56efd6d8a7e6c26f53eb266` + K4_TEST-com.homesynapse.lifecycle.RegistryRealStoreComparisonIT.xml 3,819 · `ebf9335d08207e06fdd3de549f46a35b` |
| 19:47:37–19:47:42 | F1 (00:47:37Z–00:47:42Z) | F1.txt 1,339 · `80f11574b35122d3df419660563577d9` |
| 19:50:31 | sudo probe (00:50:31Z): `user=homesynapse` · `sudo-n: OK (passwordless)` | D1-pre_sudo.txt 99 · `ef9adebb39b54ae2e80aa77f034d1ac9` |
| 19:51:32–19:55:11 | D1 (00:51:32Z–00:55:11Z): cold exit 99, then W1 exit 99 | D1.txt 2,815 · `742649886abaa1d0b70357be95255202` |
| 20:01 | Nick (the hub's W1-CONTINGENCY ruling), whole — see below | — |
| 20:02:31–20:03:53 | D1-W2 (01:02:31Z–01:03:53Z): pre-warm 31 s (buff/cache 943 → 1296 MB), then W1 again booted | D1-W2.txt 1,666 · `7e9de188a1c45de84ac4ef6c836409e7` |

**Nick's words, 19:39 CT (whole):**
> `AMEND` — run D0b with the one-step copy, exactly the command the guide tested (no edit by me to a tested line).
> Why, in three lines (the hub’s own read, not the guide’s word): the `sqlite3` shell’s `.backup` loops `sqlite3_backup_step(p, 100)` with no sleep; SQLite’s documented rule is that a write from another process between two steps restarts the backup from page 1 — on a store the Core commits to about once a second, a 941-MB copy that needs tens of seconds never finishes. Python’s `Connection.backup()` with its default `pages=-1` is ONE step: a single consistent snapshot under WAL, writers never blocked, nothing to restart. The guide measured both ways and ran the amended card through stand-ins; that is the dry-run the rule requires.
> Conditions the guide carries: the `method:` line in `D0b.txt`; every other field, the guard (exit 7), the scp and both md5 checks unchanged; the +10-min STOP still stands if no `backup:` line prints; the return records this as a hub-approved deviation (I rule it at the line’s intake — it will be D-v110-11). D0a’s numbers are banked as printed (941 MB store; 101 GB free; the empty retention keys recorded, not a STOP). D1 by 20:30 CT.

**Nick's words, 20:01 CT (whole):**
> `W1-CONTINGENCY: yes` — one relaunch, with the store pre-warmed first. The one allowed restart is the warm relaunch the packet already names (W1 again); the addition is a read-only act before it, so the single shot is as warm as it can be made.
> Why (the hub’s reading, IR-148’s row): the exit 99 is the registry’s cold-boot gate — `awaitRegistryProjectionLive` ≈ 30 s after the store loads, with the registry paging the WHOLE log at every boot on `37f05a9`. Tonight the store is 941 MB (Oct 10’s was 829 MB when “warm, it passes” was written); one failed launch cached only the part of the file the replay reached in ~45 s, the second launch replayed from position 0 again and died 40.8 s after load. Each launch warms more, but at this size a third plain launch is a coin-flip, and a third exit 99 ends the evening with no window. Reading the file once makes the cache warm end to end.
> Should I run the following command next? *(a pre-warm-only heredoc: `DB=$(find …)`; `du -b "$DB" "$DB-wal"`; `cat "$DB" "$DB-wal" > /dev/null`; `free -m`)*. The guide folded that pre-warm (the WAL read only if present; `free -m` before and after) into ONE block with W1 again (one `bench.sh start`) plus the read-only slot reads (`LOG1b/MARK1b/POS1b`), teed to D1-W2.txt, and dry-ran it through stand-ins before showing it.

## §2 Per-card verdicts against EXPECT
- **D0a — every EXPECT met.** `startup_failed=0` on the nightly's log · `formed=0 relinked=10 pings-so-far=765 dark-so-far=0` · `presence-rows=0` (K-4's precondition) · `avail-rows-total=481` · POS0 = rows = 1,875,960 · the four store reads finished within the card's single second.
- **D0b (amended) — BACKUP-1 Part 0 DONE.** `method:` line present · `backup: 28 s bytes=940978176 md5-pi=6dfd6e3c… integrity-pi=ok copy-rows=1876566 free-after=100340580352` · `scp: 16 s bytes=940978176 md5-desk=6dfd6e3c…` (≈ 58.8 MB/s). The copy is 339,968 B (83 pages) larger than D0a's main file because the WAL's frames are folded in. Free space dropped by 941,604,864 B.
- **K4 — PASS (P3″).** See §0. The console shows only `BUILD SUCCESSFUL`; the IT's lines live in the XML, which the guide copied next to K4.txt.
- **F1 — done.** 27 columns: `global_position event_id home_id event_type schema_version ingest_time event_time subject_ref subject_type subject_sequence priority origin actor_ref idempotency_key correlation_id causation_id event_category payload_size batch_id external_ref intent_kind logical_time node_id payload chain_hash payload_iv dek_ref`. No `occurred_at`, so `first=None last=None` (as the packet allows). Types: state_reported 1,202,395 · state_changed 631,933 · automation_action_completed 14,364 · automation_action_started 14,364 · command_dispatched 3,009 · command_issued 3,009 · command_confirmation_timed_out 1,714 · automation_completed 1,596 · automation_triggered 1,596 · command_result 1,129 · availability_changed 481 · integration_started 346 · integration_stopped 317 · state_confirmed 185 · integration_restarted 28 · device_discovered 22 · integration_health_changed 18 · join_rejected 18 · device_adopted 10 · device_registered 10 · entity_registered 10 · permit_join_closed 6 · permit_join_opened 6. `avail-rows=481`.
- **D1 — P1″'s expected arm; P2″ failed** (see §0). The `pgrep` lines `1274 login -- homesynapse` and `12117 sshd-session: homesynapse [priv]` are a console login and this ssh session, not the Core. `page cache dropped: used=550M free=3265M cache=326M`.
- **D1-W2 — booted; the window is open** (see §0). `POS1b=1877415`.

## §3 Observations (recorded, not ruled)
1. **The `.backup` liveness finding (D-v110-11).** The sqlite3 CLI's `.backup` steps 100 pages at a time and restarts from page 1 whenever another connection commits between steps. The guide measured this in its container (sqlite3 3.45.1, a 488,701,952-B WAL db of this shape):
   - no writer: 0.80 s
   - 4 commits/s: 30.4 s (38 × baseline)
   - the CLI's step size via `backup(pages=100)` under the same writer: 35.4 s, 140 restarts
   - **12 commits/s: not finished at 120 s**, leaving a partial 379,699,200-B file plus a `-journal` behind
   - the one-step `backup()` under 12 commits/s: 0.86 s · `VACUUM INTO`: 0.96 s, `integrity_check` ok on both

   On the Pi the one-step copy took 28 s. At the Core's rate (1,875,960 − 1,691,217 = 184,743 rows in 46 h 22 min 15 s since SOAK-NIGHT-2's S0 = 1.107 rows/s ≈ 95.6 k/day), the CLI copy would have needed a 28-s write-free gap. A killed CLI copy over non-tty ssh would most likely have kept running on the Pi and left a file that trips exit 7. Any later packet that backs up a live store (BACKUP-NIGHTLY, BC10's "backup first") inherits this.
2. **K4's console cannot show the IT.** `build-logic/…/homesynapse.java-conventions.gradle.kts` sets `testLogging { events("failed"); showStandardStreams = false }` and `isOutputPerTestCase = true`. The card's grep therefore sees only `BUILD SUCCESSFUL`, whether the IT ran or was skipped. The evidence is the per-test XML (`skipped`, `<system-out>`). The desk's earlier XML (2026-10-12T13:26:05Z, an unfiltered run without the env var) read `skipped=1`. Git Bash passed the env var as `C:\Users\Nick\hs-bench\backups\…` (the IT printed `source=C:\…`).
3. **D1's `+<s>` is detection time** in the exit-99 arm (bench.sh cddac94's 90-s wait; see P1″). bench.sh's `tail -4` also cuts the `launched pid` and `RADIO UP after` lines. The log stamps are the instrument.
4. **IR-148 reproduced deterministically.**
   - Cold: exit 99. Immediate warm relaunch: exit 99 again. Only a full read of the file made the boot pass.
   - The cache after the drop was 326 MB; after two failed launches it was 943 MB; the pre-warm added 353 MB more (to 1,296), in 31 s.
   - Warm boot, 941 MB store: projection_live 20.4 s after Loaded. The gate is ≈ 30 s, so the warm margin is about 9.6 s and shrinks as the store grows (≈ 95.6 k rows/day).
   - A household Pi after a power cut would loop on exit 99 until enough of the file happened to be cached.
5. **F1.txt holds one cp1252 byte (0x97, at offset 1280)**: the WALK line's em dash, written by the desk's Windows Python with stdout piped (cp1252). `grep` calls the file binary (`grep -a` reads it). It showed as "□" in Nick's terminal. IR-146 class; cosmetic.
6. `command_confirmation_timed_out` = 1,714 against `command_issued` = 3,009 (57 %), all-time. Recorded for the hub's attention; not a row of this packet.
7. F1's time columns are `ingest_time` and `event_time`; one query on the copy gives the store's span for R-H's per-day constant (D2's `rows-24h` gives the 24-h volume directly).
8. The Pi is a 4 GB board (`Mem: 4049`); the store (941 MB) fits the cache with room to spare (3.5 GB available after the boot).

## §5 Card discipline (deviations, for the hub's rulings)
- **Two-message rule** kept for every card: the SAY in one message, the block alone in the next. The hub question was a separate copy-ready message.
- **Guide-added, read-only:**
  - the STATE helper (desk);
  - the sudo probe `sudo -n sh -c true` (D1-pre_sudo.txt), because D1's drop runs over non-tty ssh;
  - the K4 XML copied into dr1 (the source is the build dir, which the next build would overwrite).
- **D0b amended (D-v110-11, hub-approved 19:39 CT).** One changed command: `sqlite3 "$DB" ".backup '$C'"` → `python3 -c "import sqlite3,sys; s=sqlite3.connect(sys.argv[1]); d=sqlite3.connect(sys.argv[2]); s.backup(d); d.close(); s.close()" "$DB" "$C"`, plus one `method:` line. Everything else is byte-identical. Tested in the container and dry-run through stub ssh/scp (exit 7 still refuses) before it was shown.
- **K4 at core `176adad`**, not the EXPECT's `2a54145` (stale; the IT is unchanged). Recorded, not a STOP.
- **W1-CONTINGENCY (hub yes, 20:01 CT).** D1-W2 = a read-only pre-warm, then W1 again (one `bench.sh start`), then the slot reads, all in one block. The labels `LOG1b/MARK1b/POS1b` avoid reusing D1's `LOG1/MARK1/POS1` (BC9's D-BC9-4). Stub dry-run before showing.
- Nothing deleted on the Pi; no config written; no pairing window opened; no `network_formed`; no hardware touched. The rig acts were D1's two restarts and D1-W2's one.
