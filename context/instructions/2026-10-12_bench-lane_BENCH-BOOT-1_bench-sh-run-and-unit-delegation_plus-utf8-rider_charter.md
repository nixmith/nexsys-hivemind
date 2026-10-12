<!--
file: context/instructions/2026-10-12_bench-lane_BENCH-BOOT-1_bench-sh-run-and-unit-delegation_plus-utf8-rider_charter.md
purpose: BENCH-BOOT-1 — one bench lane (Claude Code on Nick's desk, in `nexsys-bench` on `main` at `ceb08c5`), the code half of the `bench-boot` user unit (the unit cards file §A.1, refined in §1), so the Oct 19 sitting installs a unit around code that already exists and dry-run #2 runs "on bench-boot": (A) `bench.sh run` (the foreground launch the unit's ExecStart calls); `start`/`stop`/`restart` delegating to the unit when — and only when — it is enabled; `status` reading the unit; `tools/systemd/bench-boot.service` with the packaged unit's eight restart lines. (B) The UTF-8 rider (IR-183): the four selftest entry points write UTF-8 whatever the console's code page.
audience: the BENCH-BOOT-1 lane (reads WHOLE; executes §0 exactly) · Nick (dispatches §7; lands by card after the intake) · the hub that intakes (two layers at the bytes)
state-type: lane charter (bench; LOCAL desk; two units, one branch)
status: DISPATCHED Mon 15:01 CT — running at v109's close (its relayed progress: the v109 DR §2); its intake is v110's. Was: DISPATCH-READY — cut v109 beat 3 (Mon 2026-10-12 ~14:5x CT; instrument 2026-10-12T19:55:22Z) at bench `ceb08c5` and core `176adad` (the Pi runs `37f05a9` · bench `cddac94`); every §0b row run by the hub on the device shell first; the prior-ledger gate: the unit cards file §A (v108 b5 — its A.2–A.3 refined in §1) and GRADER-S31-1's return §3–§4 (the temp objects; the full volume). Flips to EXECUTED at the hub's intake.
-->

# BENCH-BOOT-1 — `bench.sh run`, the delegation to `bench-boot` when it is enabled, and the selftests in UTF-8

## §0 The lane contract (read whole before any command; every line binds)
- You are in `~/Desktop/Code/ClaudeFolder/nexsys-bench` on `main` at `ceb08c5`. `date -u` FIRST; every stamp from it (CT = UTC − 5). If a write fails with "No space left on device", `export TMPDIR=/tmp` (the VM's `/sessions` volume is full — IR-181). Run python as `PYTHONIOENCODING=utf-8 python3 -B …` until Unit B is green (IR-183). `git --no-optional-locks status --porcelain` EMPTY before your first act; your first act is `git switch -c bench-boot-1/run-and-delegation`; every write on that branch; **you STAGE (`git add -- <the §3 paths>`) and NEVER COMMIT** — the landing is Nick's card after the hub's intake (THE LANE STOPS AT A LOCK: any `.git/*.lock` you meet is a STOP and a line in the return, never a sweep). Any `.git/objects/*/tmp_obj_*` file `git add` leaves behind is named in §3 by its EXACT path (the landing card deletes by exact path, never a glob). Never `main`, never `git push`, never a merge. Nothing on the Pi; no ssh; **no `systemctl` or `loginctl` on any real machine** — every systemd and process call in a check runs against a stub on `PATH` under a temp `HOME`.
- **THE PREMISE TABLE IS RE-RUN FIRST (§0b) and pasted at the top of the return; a row that fails at the pinned shas STOPS the lane before any write (BLOCKED).** The Files table (§3) is the plan.
- Tests first, red observed: `tools/test_bench_sh.py` (27/0 at `ceb08c5`) gains §3's checks, each RED first, then GREEN; `test_verify72h.py` (57/0), `test_engine.py` (42/0) and `nightly_digest.py --selftest` (54/0) stay green. Python 3.10 stdlib and bash only. Write ONLY §3's rows; `scenarios/constants.yaml` is NOT touched (md5 `9b0af47b3376`); `tools/nightly.sh` is NOT touched (its two `"$BENCH_SH" restart` calls go through the delegation unchanged).
- **The budget is ≤ 2 h of your clock.** At 2 h you stop, stage what is green, and return the rest under §3 as [REVIEW] — Unit A alone, returned on time, is a landable unit.
- THE RETURN: `../nexsys-hivemind/context/audits/<CT-date>_BENCH-BOOT-1_return.md` — §0 the card (DELIVERED/BLOCKED; the four test commands and their closing lines; `git --no-optional-locks diff --cached --stat`; **`git write-tree` of the staged index** — the landing card asserts the commit's tree equals it; the red texts; §0b's rows re-run, one line each) · §1 what changed (per file, line spans) · §2 the tests (names; red; green) · §3 deviations ([INFO]/[REVIEW]/[BLOCKING]) · §4 findings for the register · §5 the bench-handoff entry text (one paragraph) · §6 instrument limits. **≤ 8,192 B is a CEILING, not a target.** The last line of the FILE: `RETURNED <path> <bytes> bench-boot-1/run-and-delegation staged=<n> tree=<write-tree sha>`.
- No attribution trailer anywhere (there is no commit; the rule still binds any text you write). `{{NAME}}` for the product where a name would go (none is expected here).

### §0b The premise table (the hub's greps at bench `ceb08c5` and core `176adad`, Mon 2026-10-12 19:4x–19:5xZ on the device shell; re-run each, paste the output line)
| # | Command (from `~/Desktop/Code/ClaudeFolder/nexsys-bench`) | Expected |
|---|---|---|
| 1 | `git --no-optional-locks log -1 --format=%h && git --no-optional-locks status --porcelain \| wc -l` | `ceb08c5` · `0` |
| 2 | the four test commands of §0 (with `PYTHONIOENCODING=utf-8`), each `\| tail -1` | `verify72h selftest: 57 check(s), 0 failure(s)` · `selftest: 42 check(s), 0 failure(s)` · `selftest: 54 check(s), 0 failure(s)` · `bench.sh selftest: 27 check(s), 0 failure(s)` |
| 3 | `grep -n '^do_stop() {\|^do_start() {\|nohup "\$APP"\|ln -sf "\$log" "\$CUR"\|sleep 5   # port-release\|^  restart) do_stop; do_start ;;\|^  start)   do_start ;;\|^  stop)    do_stop ;;' tools/bench.sh \| cut -d: -f1` | `29` · `38` · `41` · `45` · `46` · `141` · `142` · `143` — `do_stop`; its 5-s grace; `do_start`; the nohup; the symlink; the three verbs |
| 4 | `grep -n '"$BENCH_SH" restart' tools/nightly.sh \| cut -d: -f1` | `198` · `244` |
| 5 | `git -C ../homesynapse-core --no-optional-locks show 176adad:distribution/systemd/homesynapse.service \| grep -n '^StartLimitIntervalSec\|^StartLimitBurst\|^Type\|^KillSignal\|^SuccessExitStatus\|^TimeoutStopSec\|^Restart=\|^RestartSec\|^RestartPreventExitStatus' \| cut -d: -f1` | `20` · `21` · `24` · `58` · `60` · `62` · `70` · `71` · `72` — the packaged unit's restart contract |
| 6 | `ls tools/systemd 2>&1` | `No such file or directory` |
| 7 | `for t in "tools/verify72h/test_verify72h.py" "tools/runner/test_engine.py" "tools/runner/nightly_digest.py --selftest" "tools/test_bench_sh.py"; do PYTHONIOENCODING=cp1252 python3 -B $t >/dev/null 2>&1; echo -n "$? "; done` | `1 1 0 0` — two suites crash under cp1252 today (IR-183) |
| 8 | `grep -n '^def run(home\|^def check_fn' tools/test_bench_sh.py \| cut -d: -f1` | `215` · `251` — the harness the new checks reuse |
| 9 | `md5sum scenarios/constants.yaml \| cut -c1-12` | `9b0af47b3376` |

## §1 What this implements
**Unit A — the code half of `bench-boot`** (the unit cards file §A.0–A.1, v108 b5; refined below where the draft left a hazard — this charter wins where they differ):
1. **`bench.sh run`** — the foreground launch: the per-boot log name and the `current.log` symlink exactly as `do_start` makes them (`:43`–`:46`), then `exec "$APP" >"$log" 2>&1`. No radio wait (a unit's start is not gated on the radio); `Type=exec` in the unit, so the app is the unit's main process and `KillSignal=SIGTERM` reaches it (exit 143 = a clean stop).
2. **The delegation is decided by the unit FILE, never by the bus.** The unit is enabled when `$HOME/.config/systemd/user/default.target.wants/bench-boot.service` exists (the link `systemctl --user enable` makes). Enabled → `start`/`stop`/`restart` go through `systemctl --user start|stop bench-boot`; not enabled → the nohup/pkill path, byte for byte as at `ceb08c5`. **Why not `systemctl --user is-enabled`:** the nightly's calls (`nightly.sh:198`, `:244`) may run with no user bus (cron sets no `XDG_RUNTIME_DIR`); a bus-dependent check would read "not enabled", take the legacy path, `pkill` the unit's app and race `Restart=always`. So `bench.sh` sets `XDG_RUNTIME_DIR` to `/run/user/$(id -u)` when it is unset, and when the unit is enabled but a `systemctl --user` call fails, the verb exits non-zero with ONE line naming the cause — never the legacy path.
3. **The delegated `start` keeps the legacy contract:** an active unit → the legacy guard's line ("already running — use: bench.sh restart"), exit 1; otherwise `systemctl --user start bench-boot`, then a bounded wait (≤ 30 s) for `current.log` to point at a NEW per-boot log (the one `run` made after this start — so the wait never reads the previous boot's `zigbee.network_up`), then `do_start`'s 90-s radio wait (`:48`–`:60`) on that log, with its exits: 0 at "RADIO UP", 1 at a named failure. The nightly's relaunch depends on `restart` returning only then. The delegated `stop` keeps the 5-s port-release grace (`:38`).
4. **`status`** — when enabled, one more line: the unit's `ActiveState`, `SubState`, `Result` and `NRestarts` (`systemctl --user show bench-boot -p …`).
5. **`tools/systemd/bench-boot.service`:** `[Unit]` `StartLimitIntervalSec=300` · `StartLimitBurst=5`; `[Service]` `Type=exec` · `ExecStart=%h/nexsys-bench/tools/bench.sh run` · `WorkingDirectory=%h/hs-bench` · `Environment=HOMESYNAPSE_HOME=%h/hs-bench` · `Restart=always` · `RestartSec=10` · `RestartPreventExitStatus=10` · `SuccessExitStatus=143` · `KillSignal=SIGTERM` · `TimeoutStopSec=90`; `[Install]` `WantedBy=default.target`. The eight restart lines are the packaged unit's (row 5): one restart contract for the rig and the package.

**Why it is safe to land before the sitting:** BC10 (Sat Oct 17) pulls the bench onto the Pi two days before the Oct 19 sitting enables the unit. With no unit enabled every verb behaves as at `ceb08c5` — check 2 proves it — so the pull changes nothing on the rig. BC10's bench pull names its sha (the hub's card).

**Unit B — the UTF-8 rider (IR-183).** Each of the four selftest entry points (`test_verify72h.py`, `test_engine.py`, `nightly_digest.py --selftest`, `test_bench_sh.py`) calls `sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")`, and the same on `sys.stderr`, before its first print. Then a desk run piped through `tail -1` prints its closing line under any code page: row 7 reads `0 0 0 0`.

## §2 Files to read before starting (by range; `grep -n` first)
- `tools/bench.sh` whole (198 lines).
- `tools/test_bench_sh.py` — `:1`–`:60`, `:170`–`:265` (the temp `HOME`, `run()`, `check_fn`), and one existing check end to end.
- `tools/nightly.sh` — `:190`–`:250` (the two restart calls and what reads their exits).
- `../nexsys-hivemind/context/instructions/2026-10-12_unit-cards_BENCH-BOOT-1_and_PI-2-MIGRATION_drafts.md` — `:11`–`:65` (§A: the design and the sitting's blocks).
- Core at `176adad`, read-only: `distribution/systemd/homesynapse.service` `:14`–`:72`.

## §3 Files to create or modify (the Files table governs; nothing else is written)
| Path | Change |
|---|---|
| `tools/bench.sh` | `run`; the file-keyed delegation with the `XDG_RUNTIME_DIR` default and the one-line failure; the delegated start's guard, new-log wait and radio wait; the delegated stop's grace; `status`'s unit line — ≈ 60 lines, a ceiling to argue with in §3, not a target |
| `tools/systemd/bench-boot.service` | new — §1.5 |
| `tools/test_bench_sh.py` | Unit A's checks, each RED first, each under a temp `HOME` with stub `systemctl`, `pgrep`, `pkill`, `nohup` and a stub `$APP` on `PATH` that log their calls: (1) `run` makes the per-boot log and the symlink, then execs the app; (2) not enabled → `start`/`stop`/`restart` issue exactly `ceb08c5`'s call sequence; (3) enabled → `systemctl --user start|stop bench-boot`, no `nohup`, no `pkill`; (4) enabled and `systemctl` failing → exit ≠ 0 with the named line, no legacy call; (5) the delegated start ignores the previous log's `zigbee.network_up` and returns at the new log's; (6) `XDG_RUNTIME_DIR` unset → `/run/user/<uid>` in the `systemctl` call's environment; (7) enabled and active → the guard's line, exit 1; (8) `status` prints the unit line when enabled; (9) the unit file's eight restart lines equal row 5's. Unit B's reconfigure lines at its entry |
| `tools/verify72h/test_verify72h.py` · `tools/runner/test_engine.py` · `tools/runner/nightly_digest.py` | Unit B: the reconfigure lines at each selftest entry, nothing else |
| `README.md` | one paragraph: `bench.sh run`, and the delegation when `bench-boot` is enabled |

## §4 What to watch out for
- The not-enabled path is byte-for-byte: no reordering, no new output line; check 2 compares the stub call logs.
- The new-log wait compares `readlink -f "$CUR"` before and after the start; it is bounded and fails with a named line, never hangs.
- `run` must `exec` the app — no subshell, no `&`.
- `tools/nightly.sh` is not edited; its two restart calls must exit through the delegation exactly as through the legacy path (0 at RADIO UP, 1 at a named failure).
- The unit file's `ExecStart` path is the Pi's clone, `%h/nexsys-bench` (the dry-run #1 packet reads `~/nexsys-bench` on the Pi); invent no other path.
- No real `systemctl`/`loginctl`/`pkill` ever runs: a stub missing from `PATH` is a check failure, not a fallback to the real binary.

## §5 Out of scope
Installing, enabling or starting the unit anywhere, and linger (the Oct 19 sitting's card); `nightly.sh`; the runner; the scenarios; `constants.yaml`; the grader; the Pi; the core.

## §6 Success criterion (binary)
`test_bench_sh.py` GREEN after an observed RED on every new check (≥ 36/0); the other three suites green; row 7 reads `0 0 0 0` on the staged tree; `constants.yaml` md5 `9b0af47b3376`; `git --no-optional-locks diff --cached -- tools/nightly.sh scenarios` empty; exactly §3's seven paths staged; zero commits; `git write-tree` in §0 and in the `RETURNED` line; the return under its cap with §0b's rows re-run and the red texts quoted.

## §7 The dispatch (Nick pastes into Claude Code in `~/Desktop/Code/ClaudeFolder/nexsys-bench`; handed Mon 10-12 after GRADER-S31-1's landing)
```
You are the BENCH-BOOT-1 bench lane on my desk. Read ../nexsys-hivemind/context/instructions/2026-10-12_bench-lane_BENCH-BOOT-1_bench-sh-run-and-unit-delegation_plus-utf8-rider_charter.md WHOLE, then its §2 set by range. Execute §0 exactly: date -u first; export TMPDIR=/tmp if a write fails for space; PYTHONIOENCODING=utf-8 for python; porcelain empty; the branch; the nine §0b rows re-run and pasted at the top of the return (a failed row = BLOCKED, no write); tests red first; no real systemctl anywhere; STAGE, never commit; record git write-tree; ≤ 2 h; the return at its path with RETURNED as its last line.
```
Say back to the hub: `BENCH-BOOT-1: running` at the paste; then `BENCH-BOOT-1: RETURNED <path> <bytes> staged=<n> tree=<sha>` (or `BENCH-BOOT-1: BLOCKED <row>`). The hub intakes two-layer (re-runs the four suites and row 7 on the staged tree; reads the diff; runs the delegation against its own stubs; checks `write-tree`; greps the trailer) and cuts the landing card in Nick's form (exact-path deletes; `HEAD^{tree}` = the recorded tree; `git status` clean last).
