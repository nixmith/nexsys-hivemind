<!--
file: context/instructions/2026-10-12_unit-cards_BENCH-BOOT-1_and_PI-2-MIGRATION_drafts.md
purpose: THE TWO UNIT CARDS the v108 text orders before Oct 22 (row (vi)), as DRAFTS with their design rows settled from the record: (A) BENCH-BOOT-1 — `bench-boot`, the small systemd unit around the bench's existing launcher (`RESTART: bench-boot` RULED D-v105-26; dry-run #2 on Oct 22–23 tests the power cut on it; the run Oct 30 – Nov 2 rides it), its `Restart=`/`StartLimit*` lines as design detail, the nightly's relaunch form kept, the exit-99 class bounded, the restore before any gap; (B) PI-2-MIGRATION — the second Pi (arrives Tue Oct 20) brought up on the PACKAGED build ("test what you ship") with the rig's data copied across, the logs' readers, the postinst's start fenced, the restart limit after REGISTRY-COLD-1 — and the kit's storage slot OPEN until `KIT-STORAGE:` (SD vs SSD; the H10 after dry-run #1's F1 number).
audience: the hub (cuts each LIVE card after its dry-run through the stub ssh — THE QUOTING-LAYER LAW, pm-lessons 2026-10-11 (BC9)) · the bench lane (A's code half: a `run` subcommand and the delegation in `bench.sh`) · Nick (the sitting; the words `BENCH-BOOT: mon19 | tue20 | wed21` and `KIT-STORAGE:`)
state-type: operator cards (DRAFT; the dry-run DEFERRED — the session VM's shell is down this window, D-v108-16; a card goes LIVE only after its blocks have crossed the stub transport)
status: §A.2 LIVE (v110 b4, Tue 2026-10-13 — the re-cut on IR-185/186/187; its stub-ssh dry-run passed; the sitting after BC10's pull, on `BENCH-BOOT:`); §B DRAFT — LIVE at v111 after the probe/reflash block (IR-202: a new MG24 stick ships v14; the flasher and the 7.4.5.0 file named after a web check), the [SSD] image branch and the one-step copy. Was: DRAFT v1 — cut v108 beat 5 (Mon 2026-10-12 ~07:4x CT). NOT LIVE. §A.1 CHARTERED v109 b3 as BENCH-BOOT-1 (`instructions/2026-10-12_bench-lane_BENCH-BOOT-1_…`), whose §1 refines A.2–A.3 — the delegation keyed on the enabled unit's link, not on `systemctl --user is-enabled`; one named failure when the user bus is unreachable; the delegated start's new-log wait, then the 90-s radio wait — and wins where they differ. Inputs read at the bytes: `nexsys-bench/tools/bench.sh` (`do_start` `:41`–`:60`: `nohup "$APP" >"$log" 2>&1 &`, `ln -sf "$log" "$CUR"`; `do_stop` `:29`–`:39`: `pkill -f "$PAT"`, the 5-s port-release grace; `HOMESYNAPSE_HOME="$HOME/hs-bench"` `:6`; `APP=` `:7`) · `nexsys-bench/tools/nightly.sh` (`"$BENCH_SH" restart` at `:198` and `:244`; the suite engine restarts the app itself for fresh-boot legs `:384`; every bench operation goes through `bench.sh` — the playbook law `:14`) · `homesynapse-core/distribution/systemd/homesynapse.service` at `ba08dd8` (the packaged unit: `StartLimitIntervalSec=300` `:20`, `StartLimitBurst=5` `:21`, `Restart=always` `:70`, `RestartSec=10`, `RestartPreventExitStatus=10` (CONFIG-ERROR-1's deterministic failure), `SuccessExitStatus=143`, `TimeoutStopSec=90`, `MemoryMax=2G`; the DANGER note on `Type=notify`) · D-v105-26 and D-v105-24 (v)/(vi) · IR-148 (the exit-99 class: a cold SD's registry rebuild past its 30-s limit; one read warms the cache; REGISTRY-COLD-1 `6a03403` on `main` reads the type index — deployed at BC10).
-->

# The two unit cards — BENCH-BOOT-1 and PI-2-MIGRATION (drafts)

## A. BENCH-BOOT-1 — `bench-boot`, a unit around the launcher

### A.0 The design, settled from the record (each row a decision; refutable by `REVERT A.n`)
| # | Decision | The record it rests on |
|---|---|---|
| A.1 | **A USER unit with linger**, not a system unit: `~/.config/systemd/user/bench-boot.service`; `loginctl enable-linger <bench user>` so the user manager starts at boot without a login; `systemctl --user` needs no sudo, so the nightly and the suite engine keep calling `bench.sh` unchanged | D-v105-26 "a small unit around the existing launcher (same paths, logs and tooling)"; the nightly's playbook law (`nightly.sh:14`); no new sudo surface on the rig |
| A.2 | **`bench.sh` gains a FOREGROUND form, `bench.sh run`:** computes the per-boot log name and the `current.log` symlink exactly as `do_start` does (`:43`–`:46`), then `exec "$APP" >"$log" 2>&1` — the unit's `ExecStart`; the 90-s radio wait of `do_start` (`:48`–`:60`) is NOT in `run` (a unit's start is not gated on the radio; `bench.sh health` reads it as today) | the launcher's own lines; `Type=exec` (the packaged unit's choice; `Type=notify` BRICKS — the unit file's DANGER note) |
| A.3 | **`bench.sh start / stop / restart` DELEGATE when the unit is installed** (`systemctl --user is-enabled bench-boot` → `systemctl --user start/stop/restart bench-boot`; else the nohup/pkill path as today) — so `nightly.sh:198/:244` and the suite's fresh-boot legs go through the unit without an edit to the nightly | one path to the app (the playbook law); the nightly's relaunch form kept |
| A.4 | **The restart lines — the packaged unit's, verbatim:** `Restart=always` · `RestartSec=10` · `StartLimitIntervalSec=300` · `StartLimitBurst=5` · `RestartPreventExitStatus=10` · `SuccessExitStatus=143` · `KillSignal=SIGTERM` · `TimeoutStopSec=90` | D-v105-26's four lines read at the unit file; one restart contract for the rig and the package ("test what you ship") |
| A.5 | **The exit-99 class is bounded, not prevented:** a cold SD's registry rebuild exits 99 inside the 30-s limit (IR-148); `Restart=always` relaunches after 10 s and the second launch's cache is warm (IR-148's own observation; the restore sitting's D2b 6/6 after one read); `StartLimitBurst=5` per 300 s bounds a card that never warms — the unit goes start-limited and `bench.sh status` says so; after BC10 (`6a03403`'s type-index rebuild) the class should not recur, and the bound stays | IR-148; D-v105-26 "the restart limit after REGISTRY-COLD-1" |
| A.6 | **The ten-second gap:** `RestartSec=10` is longer than `do_stop`'s 5-s port-release grace (`:38`) — the relaunch never races the port | the launcher's "death-rattle lesson" |
| A.7 | **Logs:** the app's stdout/stderr go to the per-boot file as today (the bench's readers, the graders, `current.log`); the unit's own lines go to the user journal (`journalctl --user -u bench-boot`) — a start-limited unit is read there | "same paths, logs and tooling" |
| A.8 | **The restore before any gap:** the card's LAST block before a pause is the one that returns the rig to the form the next sitting expects — once the unit is enabled and verified (one `bench.sh restart` through it, `bench.sh health` green), the unit IS the form of record and stays; if the verify fails, the card's restore block disables the unit and relaunches by `bench.sh start`'s nohup path, and the sitting ends in the state it began | THE RESTORE RUNS BEFORE THE GAP (the brief's §WHAT YOU DO NOT DO) |
| A.9 | **When:** before Oct 22, in its own ≤ 1-h sitting, no other hardware act in the hour; the hub's lean **Mon Oct 19 evening** (Sun Oct 18 holds the rollback + BC9b; Tue Oct 20 is PI-2's; Wed Oct 21 the last code day). `BENCH-BOOT: mon19 \| tue20 \| wed21` is Nick's word | the calendar (D-v107-25); hardware in series |

### A.1 The code half (a bench lane: BENCH-BOOT-1; ≤ 60 lines; red first)
- `tools/bench.sh`: the `run` subcommand (A.2); the delegation in `do_start`/`do_stop`/`restart` (A.3); `status` prints the unit's `ActiveState`/`Result` when installed; `test_bench_sh.py` gains three cases (run's log + symlink; delegation when enabled; the legacy path when not). The unit file ships in the bench repo at `tools/systemd/bench-boot.service` with the eight lines of A.4 and `ExecStart=%h/nexsys-bench/tools/bench.sh run`, `WorkingDirectory=%h/hs-bench`, `Environment=HOMESYNAPSE_HOME=%h/hs-bench`, `[Install] WantedBy=default.target`.
- The lane: the bench domain is FREE after GRADER-S31-1 (Tue Oct 13); BENCH-BOOT-1 is its own small charter, landed by Nick's card as `BENCH: LANDED <sha>`; the Pi pulls it at BP10/BC10 or by its own `git pull` in the card below.

### A.2 The operator card — LIVE (v110 b4, 2026-10-13): the re-cut on BENCH-BOOT-1's F1/F2/F4 (IR-185 the legacy stop BEFORE `enable` · IR-186 `reset-failed` · IR-187 the unit's PATH); every remote block a `bash -s` heredoc; the stub-ssh dry-run PASSED against the landed tree `a17a7754` = `6a40a10` (the record `audits/2026-10-13_v110-b4_unit-card-A2_stub-ssh-dry-run.md`); the prior-ledger gate: BENCH-BOOT-1's return §3–§4 grepped for every reused string (D1–D4, F1–F5 carried by id). The Pi must be at `6a40a10` first (BC10's bench pull, Sat Oct 17); `BENCH-BOOT: mon19 · tue20 · wed21` picks the evening; ≤ 2 h; never after 21:30; no other hardware act that hour.
```
# BLOCK 1 — the state (read-only): the bench sha on the Pi (6a40a10 after BC10's pull); the unit file in the clone; the unit absent; the app running by nohup; the user manager's PATH (IR-187)
ssh hs-dev-1 'bash -s' <<'EOF_B1'
cd ~/nexsys-bench && git --no-optional-locks log -1 --oneline && ls tools/systemd/bench-boot.service
systemctl --user is-enabled bench-boot 2>&1 | head -1
pgrep -af '[c]om.homesynapse.app.Main' | head -1 | cut -c1-80
readlink -f ~/hs-bench/current.log
echo "unit-PATH: $(systemctl --user show-environment 2>/dev/null | grep '^PATH=' | cut -c1-120) · java: $(readlink -f "$(command -v java)")"
EOF_B1
# EXPECT: `6a40a10 feat(bench.sh,systemd): BENCH-BOOT-1 …` · `tools/systemd/bench-boot.service` · "Failed to get unit file state" or "disabled" (absent) · one Main pid · the current log's path · `unit-PATH: PATH=…` that CONTAINS the directory of `java:` (else STOP: the unit would fail at ExecStart — IR-187; the fix is an `Environment=PATH=…` drop-in, a separate card).

# BLOCK 2 — the legacy stop FIRST (IR-185: not enabled → ceb08c5's pkill path), then install, enable, linger (the write)
ssh hs-dev-1 'bash -s' <<'EOF_B2'
cd ~/nexsys-bench && tools/bench.sh stop && mkdir -p ~/.config/systemd/user && cp tools/systemd/bench-boot.service ~/.config/systemd/user/ && systemctl --user daemon-reload && loginctl enable-linger "$USER" && systemctl --user enable bench-boot && systemctl --user is-enabled bench-boot && loginctl show-user "$USER" -p Linger
EOF_B2
# EXPECT: `[OK] stopped` (the legacy path; the 5-s grace) · `Created symlink …/default.target.wants/bench-boot.service` · `enabled` · `Linger=yes`. The app is DOWN between BLOCK 2 and BLOCK 3 — paste BLOCK 3 at once.

# BLOCK 3 — the handover: the DELEGATED start (bench.sh's own: the guard, the NEW log ≤ 30 s, the radio wait, the health), then the unit's state (the one relaunch of the sitting)
ssh hs-dev-1 'bash -s' <<'EOF_B3'
cd ~/nexsys-bench && tools/bench.sh start && systemctl --user show bench-boot -p ActiveState -p NRestarts -p Result && readlink -f ~/hs-bench/current.log
EOF_B3
# EXPECT: `[OK] started bench-boot -> …/bench-<stamp>.log` · `[OK] RADIO UP after <n>s` · the health tokens with `zigbee.network_up` · `ActiveState=active` · `NRestarts=0` (1 if the cold cache cost one exit 99 — read the log's `registry` lines then) · `Result=success` · the NEW log's path. A `[!!] … failed (exit 1): … start-limit-hit` → `systemctl --user reset-failed bench-boot` once, then BLOCK 3 again (IR-186). A `status=203/EXEC` or `java: not found` in `journalctl --user -u bench-boot -n 20` → BLOCK 5 (IR-187).

# BLOCK 4 — the delegation proof: the nightly's own call (`bench.sh restart`) goes through the unit; a NEW per-boot log
ssh hs-dev-1 'bash -s' <<'EOF_B4'
cd ~/nexsys-bench && tools/bench.sh restart && systemctl --user show bench-boot -p ActiveState -p NRestarts && readlink -f ~/hs-bench/current.log && tools/bench.sh status | head -3
EOF_B4
# EXPECT: `[OK] stopped (bench-boot)` · `[OK] started bench-boot -> …` · `[OK] RADIO UP after <n>s` · `ActiveState=active` · `NRestarts=0` · a NEW current.log path (a fresh per-boot log — the unit relaunched through bench.sh) · `status`'s unit line `unit bench-boot (enabled): ActiveState=active SubState=running Result=success NRestarts=0`.

# BLOCK 5 — THE RESTORE (only if BLOCK 3 or 4 failed; else skipped and the unit stays): disable, reset-failed, the legacy start
ssh hs-dev-1 'bash -s' <<'EOF_B5'
systemctl --user disable --now bench-boot; systemctl --user reset-failed bench-boot 2>/dev/null; cd ~/nexsys-bench && tools/bench.sh start | tail -3
EOF_B5
# EXPECT: `Removed …/default.target.wants/bench-boot.service` · the nohup path's `[OK] RADIO UP` · the sitting ends as it began (the unit file stays in ~/.config/systemd/user, disabled).
```
The one line back: `BENCH-BOOT: <sha> · active · NRestarts=<n> · current=<log name> · restored=no|yes` (+ `unit-PATH ok|STOP` from BLOCK 1).

## B. PI-2-MIGRATION — the second Pi on the packaged build

### B.0 The design, settled from the record
| # | Decision | The record it rests on |
|---|---|---|
| B.1 | **PI-2 runs the PACKAGE (`homesynapse.service`, the `.deb`), not `bench-boot`:** "test what you ship" moves to PI-2's pre-pilot run (Oct 20+); the rig (hs-dev-1) keeps `bench-boot` for the run | D-v105-26 |
| B.2 | **The storage slot RULED `KIT-STORAGE: a` (Nick, 2026-10-13; D-v110-20/21): the SSD on the Pi 5's PCIe (the official SSD Kit 256 GB) — the image step takes the [SSD] branch; the first boot measures boot-to-ready, RSS and the replay rate (RUNTIME-1's first point).** Was: SD or SSD is `KIT-STORAGE:` — the H10 after dry-run #1's F1 per-device-per-day count (`VOLUME:`), because IR-148's cold cache is the SD's read path and an SSD changes the cold-boot profile and the pilot's hardware line; the card is written for either, with the image step as the one branch | D-v105-24 (v); the v108 text's H10 words |
| B.3 | **The four points, in order:** (1) the data copied across — the event store, the config (`zigbee` keys and network parameters, so the fleet re-adopts without a re-join), the registry's checkpoint — by SQLite's online backup to a closed copy (BACKUP-1's form; md5 on both COPIES, never the live file), restored into `/var/lib/homesynapse` under the service's user and mode 0700; (2) the logs' readers — the package logs to journald (`SyslogIdentifier=homesynapse`), the bench reads files: the readers point at `journalctl -u homesynapse -o cat` or the service gains a file sink by drop-in (`StandardOutput=append:`) — the hub's lean: the drop-in, so the graders read the same shape on both Pis; (3) the postinst's start FENCED — the `.deb` starts the service at install; the card masks the unit before `apt install` and unmasks after the restore of (1), so the first boot is on the copied data, never on an empty store that the fleet would then re-adopt into; (4) the restart limit after REGISTRY-COLD-1 — the package at BC10's sha carries `6a03403`; the first boot on the copied store is the cold-rebuild test of record on PI-2's storage, and its line (`registry.projection_rebuilt: … skipped=0`) is the evidence line | D-v105-26's four points; BACKUP-1's copy law (D-v107 b3: md5 on both copies); the unit file's `StateDirectoryMode=0700`; PKG-FRESH-1b (Wed Oct 14) rehearses the fresh install on hs-fresh first |
| B.4 | **The sitting:** Tue Oct 20 (the board arrives) or the next evening; ≤ 2 h; the rig's dongle NEVER in PI-2 (the identity gate: cards named by hostname; the dongle in only after the identity gate — the brief's standing fence); PI-2 gets its own coordinator only when the pilot's kit is assembled | the brief's §WHAT YOU DO NOT DO; hostnames only |
| B.5 | **The restore before any gap:** PI-2's bring-up touches nothing on hs-dev-1 but the one read-only backup copy; a failed step leaves PI-2 powered off and the rig untouched | THE RESTORE law |

### B.1 The card's blocks (DRAFT; the dry-run DEFERRED; the image step is the `KIT-STORAGE:` branch)
```
# BLOCK 0 — the image: [SD] the same image class as hs-fresh (PKG-FRESH-1b's)  |  [SSD] the imager's SSD target, boot order set — the branch `KIT-STORAGE:` picks; hostname `hs-pi2`; the bench user; Tailscale joined (`TAILSCALE: expiry-off`)
# BLOCK 1 — the copy on hs-dev-1 (read-only on the rig; BACKUP-1's form = the ONE-STEP python backup, IR-188 — the sqlite3 CLI's .backup never finishes on the live store): the online backup to a closed copy; md5 on the copy; integrity_check on the copy
# BLOCK 2 — PI-2: mask the service; apt install the BC10 `.deb`; the postinst must NOT start it (the mask proves it); restore the copy into /var/lib/homesynapse (user homesynapse, 0700); the config in /etc/homesynapse
# BLOCK 3 — the file-sink drop-in (B.3 (2)); daemon-reload; unmask; start; the readiness probe (ExecStartPost); the first boot's registry line; health
# BLOCK 4 — the readers: the bench's graders pointed at PI-2's log path; one `bench.sh health` equivalent on PI-2 (the package's own health-probe.sh)
# BLOCK 5 — THE RESTORE on failure: PI-2 powered off; the copy on hs-dev-1 deleted or kept per `du`; the rig untouched
```
The one line back: `PI-2: <sha> · storage=<sd|ssd> · boot=<ok|exit99×n> · registry=<rebuilt skipped=0 | …> · readers=<ok>`.

## C. What the hub does next
- A's code half LANDED as BENCH-BOOT-1 (`6a40a10`, Mon 2026-10-12 18:36); A's card is LIVE (v110 b4) after its stub-ssh dry-run and the prior-ledger gate against BENCH-BOOT-1's own return; Nick's `BENCH-BOOT:` word picks the evening, after BC10 puts `6a40a10` on the Pi.
- B's card is cut LIVE at v111 (`KIT-STORAGE: a` ruled; PKG-FRESH-1b Wed Oct 14): the [SSD] image branch; BLOCK 1 in the one-step form (IR-188); the coordinator probe + the 7.4.5.0 reflash block BEFORE the stick meets the Core (IR-202); the first-boot measurements; its own stub-ssh dry-run.
- Neither card runs after 21:30; neither shares an hour with another hardware act.
