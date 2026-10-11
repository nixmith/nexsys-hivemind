<!--
file: context/audits/2026-10-11_v107-b3_DRY-RUN-1_packet-cut_audit.md
purpose: The cutting beat's audit for DRY-RUN #1's packet (`context/instructions/2026-10-12_DRY-RUN-1_BACKUP-1-K-4-F1-A4-R4_operator-session-prompt.md`): the sources it was cut from, the dry-run on the corpus through the quoting layers (both cold-start arms), the prior-ledger gate (SOAK-NIGHT-2's D1–D10; BC9's D-BC9-1..8) with the greps listed, the day-name pass, and what the packet does not verify.
audience: the hub (v107 b3; v109's intake Tuesday) · Nick (what Monday's hour buys)
state-type: audit (a packet cut)
status: FILED v107 beat 3 (Sun 2026-10-11 ~18:1x CT; instrument 2026-10-11T23:19:06Z).
-->

# DRY-RUN #1 — the packet cut (b3): the dry-run, the gate, the day-names

## §0 What the packet is
Six cards over two sittings (Mon 2026-10-12 ≈ 19:00 CT: D0a the state · D0b BACKUP-1 Part 0 · K4 on the copy · F1 on the copy · D1 the cold start LAST; Tue 2026-10-13 ≈ 19:00 CT: D2 the harvest at +24 h), thirteen pre-registrations P0″–P12″ + BACKUP-1 DONE, the household sentences recorded as a rehearsal of dry-run #2's grader, one line back with its banked fields named (`COLD` · `K-4` · `F1 rows-24h` · `SCAN`/`WALK` · `DU`/`growth-24h`/`free` · `GATE-R4` · `FLAPS` · `md5-match`). 32,300 B, md5 `dc9931cda0a5727acf9230a1eede1cb9`. **The order is the safety:** the copy is taken and verified (md5 on the Pi's copy and the desk's copy — never the live file; `PRAGMA integrity_check`) and K-4/F1 run on the desk BEFORE the cold start — a `37f05a9` exit 99 with the copy not yet taken is the one ordering that could lose the hour (Nick, 18:06).

## §1 The sources (by id)
- The form: SOAK-NIGHT-2's packet (`_scratch/v101/soak2/soak2_packet.md`; its S0/S2 cards, the clocks paragraph, the ceiling paragraph, the guide's rules). Every remote block is a `bash -s` heredoc (`ssh pi 'bash -s' <<'EOF_…'`) — the SQL's quotes never cross a shell wrapper (BC9's D-BC9-1; the lesson of 2026-10-11).
- The rows: the plan forward §6 (F1's type counts; the timed scan of BACKUP-1's copy) · D-v102-22 (B: `du` + the retention keys + the 72-h projection — R4; C: what BACKUP-1 carries and omits; the `timedatectl` line) · the plan review §4/§6 (BACKUP-1 Part 0 ON TIME Mon Oct 12; K-4 on the copy; STARTER-1 NOT here — ruled to BC10 LAST, D-v106-21; the kit's storage H10 takes F1's number; §6.4 the five household sentences) · REGISTRY-COLD-1's instruction §7 (K-4 opt-in by `-Dhomesynapse.registryCold.store=` or `HOMESYNAPSE_REGISTRY_COLD_STORE`; the copy must be a file no Core has open; ~830 MB in `@TempDir`; the presence-row precondition) and the IT's source at `2a54145` (`RegistryRealStoreComparisonIT.java:57` the env var, `:71` the property-or-env read, `:45` the encrypted-scope failure) · IR-148's "before" (PKG-FRESH-1's D2: `startup_failed` at ≈ 45 s, twice — `audits/2026-10-10_v104-b1_boot_restore_PKG-FRESH-1_intake_two-layer_audit.md`) · `tools/bench.sh` at `32bac40` (`start`/`stop`/`status`/`entities`; `do_start` waits 90 s for `zigbee.network_up`; `:144` the status block's shape — IR-165).
- The clocks and the fleet: the five mains IEEEs and the Hue's from the soak packet; the sensor's `link_summary` device; the two entity ULIDs.

## §2 The dry-run on the corpus — THROUGH THE QUOTING LAYERS (`_scratch/v107/b3/dr1_dry-run.sh`)
Every fenced block extracted and run with `HOME` pointed at a FIXTURE desk; `ssh` a stub that PRINTS the remote command string it received (`[stub ssh] host=pi remote-cmd=<<bash -s>>`; for D2 `<<bash -s bench-… 197 200>>` — the three slots arrive as `$1 $2 $3`) and runs the heredoc under `bash -s` in a fixture Pi home (BC9's kept log as `current.log`; a fixture `events` table with `global_position · event_type · payload · occurred_at`; stub `bench.sh`, `timedatectl`, `sudo`, `scp`, a python-backed `sqlite3` incl. `.backup`, a stub `gradlew`); D2's slots filled from D1's output file as the guide would. **Run A (the booted arm): 6/6 blocks exit 0** (`dr1_dry-run.txt`, 7,592 B). **Run B (`DR1_COLD_ARM=fail` — the stub's first `start` writes `startup_failed` and dies): 6/6 exit 0** (`dr1_dry-run_cold-arm.txt`): `COLD: startup_failed at +2 s (the EXPECTED exit 99 arm)` · `COLD status: [!!] NOT running` · `W1: relaunch (warm)` · `LOG1=… MARK1=197` · `W1 status: [ok] running (pid 4242)` → D2 ran on those slots. The D0b → `scp` → md5 chain verified on the fixture (`md5-pi` = `md5-desk`). Two defects the dry-run found and the packet fixed before filing: D1 read the status block's LAST line (`--- failure tokens ---` — BC9's D-BC9-6, IR-165) → the card greps the `running|NOT running` line; a stray `=== D0 end` echo from the pre-split D0 card → removed.
**Not exercised by the fixture (disclosed):** the real `./gradlew` K-4 run (a stub printed the IT's lines; the real run is Monday's); `sudo` and the page-cache drop (a stub; the Pi's `sudo` must be passwordless for `sh -c` — if it prompts, Nick types the password once in the ssh session, the card continues); the real `sqlite3` CLI's `.backup` on an 830 MB WAL store under writes (the API restarts on concurrent writes and completes; `copy-rows` vs `rows-now` reads the drift); `timedatectl show -p …` on the Pi's systemd version (the stub printed the three keys; an older systemd prints the whole block — RECORD either way); the retention-key and `home_id` greps against the Pi's real config paths (`~/.nexsys`, `~/hs-bench/*.yaml|*.yml|config`) — an empty line means the paths differ, RECORDED, not a STOP.

## §3 The prior-ledger gate (law 15; `coding-instruction-format.md` #31) — the greps, as run on the packet
- **BC9 D-BC9-1** (the SQL's quotes inside a single-quoted ssh string): `grep -c "^ssh pi '[^']*[\"'][^']*'" packet` = 0; every remote block is a `<<'EOF_…'` heredoc (5); the one `ssh pi "bash -s <LOG1> <MARK1> <POS1>"` carries only the three slots in double quotes (SOAK-NIGHT-2's S2 form, which ran).
- **BC9 D-BC9-4** (a card reusing another's labels): `MARK0`/`POS0` in D0a only; `MARK1`/`POS1` minted at D1 and consumed at D2; `POS2` at D2 — each card its own.
- **BC9 D-BC9-6** (the status block's last line): `grep -c 'status 2>&1 | tail'` = 0 after the fix; both status reads grep the `running|NOT running` line.
- **BC9 D-BC9-2/-3/-5** (a block run late; a retry; sequencing waits): no retry is written into a card except D0b's `scp` ONCE and D1's `start` ONCE (the guide's rule); D2 at +24 h "at the hour" (SOAK-NIGHT-1's D4; SOAK-NIGHT-2's D8 — 46 min late RECORDED).
- **SOAK-NIGHT-2 D3** (IR-137's F-2: `seen_during_probe` reads the reply on `ok`): the field RECORDED per class, never ruled.
- **SOAK-NIGHT-2 D4 + D6** (two blocks shown together): THE TWO-MESSAGE RULE stated twice in the guide's text (IR-159).
- **SOAK-NIGHT-2 D5** (a python one-liner garbled under Git Bash's code page): the two `python3 -c` one-liners are ASCII-only (`grep -P '[^\x00-\x7F]'` on those lines = 0; IR-146); F1's python is a heredoc, not a one-liner.
- **SOAK-NIGHT-2 D7** (the EXPECT pinned a line order): no EXPECT pins order; counts and presence only.
- **SOAK-NIGHT-2 D9** (`device_relinked` in the log, absent from the store): the packet counts it in the log only; no store expectation.
- **SOAK-NIGHT-2 D1/D2/D10**: D1 (a relink during the day) RECORD-only; D2 → IR-158 (the sensor's `lastSeenAt` UNCHANGED is the expected reading, P10″); D10 resolved.
- **The reviewer's F8 / the lane's R-3 on K-4** (Nick 17:58 (2)): the copy is SQLite's online backup, not a file copy; the presence query runs on the live store (`mode=ro`) at D0a and on the copy at K4; the desk's free space is in the STATE line.

## §4 The day-name pass (Nick 17:58 (1)) — every date in the packet re-derived from the calendar
Oct 11 Sun (today) · **Oct 12 Mon** (D0a–D1) · **Oct 13 Tue** (D2) · Oct 16 Fri (the go/no-go) · **Oct 17 Sat** (BC10 — "Fri Oct 17" in the inherited texts was wrong; the packet says Sat) · Oct 18 Sun (BC9b; SOAK-NIGHT-3's morning) · Oct 20 Tue (PI-2) · Oct 22–23 Thu–Fri (dry-run #2 → the freeze) · Oct 30 Fri – Nov 2 Mon (the run). `grep -c 'Fri Oct 17' packet` = 0.

## §5 What the packet does not verify (for the intaking hub, v109)
- The Pi's `sudo` for the page-cache drop (a password prompt is handled by Nick in the session; `[stub sudo]` in the dry-run).
- K-4's real duration on an 830 MB store (the copy to `@TempDir` + two rebuilds; minutes, not seconds — the card says 5–15 min).
- Whether `occurred_at` is the events table's time column (F1 prints `columns:` first and tolerates its absence).
- The retention keys' location in the Pi's config (the grep covers four paths; an empty result is RECORDED).
- The exit-99 arm's timing on the real SD (PKG-FRESH-1's 45 s is the prior; the card waits 100 s).
- `probe_answered` / `availability_contract_declared` rows: 0 by construction (the Pi runs `37f05a9`; AVAIL-API-1 reaches it at BC10).
