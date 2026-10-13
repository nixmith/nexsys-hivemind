# BENCH-BOOT-1 return — `bench.sh run`, the delegation to `bench-boot`, the selftests in UTF-8

## §0 The card — DELIVERED (Unit A whole; Unit B with D1/D2 [REVIEW])
`nexsys-bench` branch `bench-boot-1/run-and-delegation` off `ceb08c5`; core `176adad` read-only. `date -u`: 20:00:53Z → branch 20:03:30Z → RED 20:19:53Z → GREEN 20:22:06Z → staged 21:02:42Z (62 min of 2 h). Porcelain 0 first; zero commits; no `.git/*.lock`; `git add` left no `tmp_obj_*`.
§0b re-run 20:02–20:03Z, all nine hold (rows 2, 7 in WSL `Ubuntu` 3.10.12, §6): 1 `ceb08c5` · `0` · 2 `verify72h selftest: 57 check(s), 0 failure(s)` · `selftest: 42 check(s), 0 failure(s)` · `selftest: 54 check(s), 0 failure(s)` · `bench.sh selftest: 27 check(s), 0 failure(s)` · 3 `29 38 41 45 46 141 142 143` · 4 `198 244` · 5 `20 21 24 58 60 62 70 71 72` · 6 `ls: cannot access 'tools/systemd': No such file or directory` · 7 `1 1 0 0` · 8 `215 251` · 9 `9b0af47b3376`
Staged tree (`git archive` of it, 21:03:09Z): `verify72h selftest: 57 check(s), 0 failure(s)` · `selftest: 42 check(s), 0 failure(s)` · `selftest: 54 check(s), 0 failure(s)` · `bench.sh selftest: 42 check(s), 0 failure(s)`; row 7 `1 0 0 0` (D1); md5 `9b0af47b3376`; `diff --cached -- tools/nightly.sh scenarios` empty; staged == worktree.
`diff --cached --stat`: `README.md | 4 +` · `tools/bench.sh | 73 ++++-` · `tools/runner/test_engine.py | 3 +` · `tools/systemd/bench-boot.service | 35 +++` · `tools/test_bench_sh.py | 587 +++…` · `tools/verify72h/test_verify72h.py | 3 +` · `6 files changed, 704 insertions(+), 1 deletion(-)`
`git write-tree`: `a17a7754d4c12f27ad48d9f14ebdb1e5ccb8f9e9`
RED — the final test text against `ceb08c5`'s `bench.sh`, no unit file (21:00:01Z; first at 20:19:53Z, 41/12): `bench.sh selftest: 42 check(s), 13 failure(s)`: r1 `exit was 2, want 143 (the app's)` · r3, r5 `['pgrep -f [c]om.homesynapse.app.Main', 'nohup …/homesynapse-app', 'sleep 1'…]` · r4 `start: exit 0` · r6 `[]` · r7 `['pgrep -f [c]om.homesynapse.app.Main']` · r8 no unit line · r9 `no …/tools/systemd/bench-boot.service` · r10 `'systemctl --user start bench-boot' is not in list` · r11 `exit 0, want 1` · r12 `already running — use: bench.sh restart` · r13 no `run` usage line · r14 `[…, 'pkill -f [c]om.homesynapse.app.Main', …]` (re-run 21:05:40Z, 42/13). r0, r2 green there (D6). Unit B's red: row 7 `1 1 0 0`.

## §1 What changed
- `tools/bench.sh` (+72/−1): `:48–:69` `radio_wait()` = `:48–:64` verbatim · `:144–:156` comment, `UNIT_LINK`, `unit_enabled` (`-L || -e`) · `:158–:163` `do_run` · `:165–:171` `sd()` · `:173–:178` `unit_stop` · `:180–:193` `unit_start` · `:195–:200` `unit_status` · `:204–:207` the switch (D3) · `:213` `run)` · `:214` status · `:267` usage.
- `tools/systemd/bench-boot.service` (new, 35): §1.5 + `Description=` + comments.
- `tools/test_bench_sh.py` (+587): `:25–:30` · `:534–:1111` the rig, r0–r14 · `:1127–:1129` Unit B. `test_verify72h.py` `:2700–:2702`, `test_engine.py` `:1921–:1923` Unit B only · `README.md` `:45–:48`.

## §2 The tests (RED above, then GREEN 42/0)
r0 stubs only, no real tool reachable · r1 run execs (same pid; 143) · r2 not enabled = ceb08c5's calls + lines · r3 delegated start/stop, OK lines, grace · r4 one named line, no legacy call; a failing start → its first line · r5 old log's `network_up` ignored · r6 `/run/user/<uid>` · r7 active → guard; failed/activating → start · r8 unit line order · r9 unit file · r10 exits 0/1/1 · r11 bounded · r12 app outside · r13 usage · r14 dangling link. Review (21 agents, a skeptic per finding) + 22 mutants: four survived → r3/r4/r7 tightened, r14 added (each red at `ceb08c5` and on its mutant); every non-equivalent mutant now caught. r2's red: m1 (`is-enabled`-keyed) and m15 (an extra legacy line). No flake in 7 runs (2 loaded).

## §3 Deviations
- [REVIEW] D1 Row 7 reads `1 0 0 0`. All four closing lines now print under cp1252 (`tail -1` = `verify72h selftest: 57 check(s), 1 failure(s)`), but T3c's children inherit the page: `export.py:525` prints `→`, `grader.py` `—`; both crash after their work, T3c reds (57/0 under UTF-8). Both outside §3, not written. Measured in a /tmp copy: two reconfigure lines in EACH tool's `__main__` → T3c green (in `main()` they break nine in-process checks). Struck → a §3 row for the two tools, or row 7 re-cut.
- [REVIEW] D2 `nightly_digest.py` NOT modified — 6 of §3's 7 paths staged: `selftest()` already calls `_utf8_stdout()` (`:708`; `:76–:86`) first; row 7 reads 0 for it at `ceb08c5`; another reconfigure is dead code. Struck → one line.
- [REVIEW] D3 The `start`/`stop`/`restart` arms stay byte-identical — `test_verify72h` T3b (`:515–:520`) pins them (inline arms: 57/1, seen 20:23Z) — so the switch is `:204–:207`: enabled → `do_start`/`do_stop` are the unit's.
- [REVIEW] D4 Two guards past §1.3: the delegated start refuses while the app runs and the unit is not active; the delegated stop names a survivor outside the unit, exit 1, no pkill (r12). They turn F1's race into a stop.
- [INFO] D5 `bench.sh` +72 vs ≈ 60: 52 code, 11 comment, 9 blank.
- [INFO] D6 r2 is green at `ceb08c5` by construction (golden = ceb08c5's own run; r0 never runs bench.sh); their reds are mutants'. r2's draft golden missed `do_stop`'s `:33` third `pgrep` (red at ceb08c5), fixed before code.
- [INFO] D7 `XDG_RUNTIME_DIR` is set on the systemctl calls only; the legacy app's env is unchanged. r0, r10–r14 are beyond §3's nine.

## §4 Findings for the register
- F1 The card's BLOCK 3 (unit cards §A.2) runs `bench.sh stop` AFTER BLOCK 2's enable: the stop goes to the inactive unit, the nohup app survives; this code prints `STILL RUNNING outside bench-boot`, exits 1, `&&` halts (unguarded: a second app races the first). Re-cut: the legacy `bench.sh stop` BEFORE `enable`, then `bench.sh start`.
- F2 The start limit (5 / 300 s) counts manual starts: a delegated restart refused after its stop leaves the app down until `systemctl --user reset-failed bench-boot` (README says so).
- F3 IR-183's tool half (D1): on a cp1252 console `bench.sh export` exits 1 after writing the export.
- F4 The unit runs in the user manager's environment, not a login shell's; BLOCK 3's health read is the check (a reviewer read java launched by the nightly's user unit in the record; not re-checked).
- F5 The runner's 300-s timeout (`drivers.py:50`) covers the delegated worst case (≈ 225 s).

## §5 Bench-handoff entry
BENCH-BOOT-1 (2026-10-12; `bench-boot-1/run-and-delegation` off `ceb08c5`, staged, uncommitted): `bench.sh run` makes the per-boot log and `current.log` as `start` does and `exec`s the app — the `ExecStart` of the user unit `tools/systemd/bench-boot.service` (`Type=exec`, the packaged unit's eight restart lines). Once the unit is enabled (the wants link, never the bus) `start`/`stop`/`restart` go through `systemctl --user` under the legacy contract (guard, a NEW log ≤ 30 s, the radio wait's exits, the 5-s grace); a failing call is one named line, exit 1; `XDG_RUNTIME_DIR` defaults for cron; `status` adds the unit's state. Not enabled: `ceb08c5`'s bytes (r2). Selftests reconfigure to UTF-8 (IR-183). 42/0 · 57/0 · 42/0 · 54/0. BC10 pulls it; the Oct 19 sitting enables it (F1).

## §6 Instrument limits
Rows 2, 7 and every suite: WSL `Ubuntu` (3.10.12, bash 5.1) — the device shell's proxy, not it (the Windows desk reads 57/3, 42/38: bash = the WSL launcher). No real systemd ran: the unit in every check is the stub's model; systemd 257's semantics are read, not executed. r2 proves the call set and the output, not the order around do_start's `&` (`ln` unstubbed, nohup's place dropped) — the source proves that (`:41–:47` unchanged but `radio_wait`). The Pi untouched.
RETURNED ../nexsys-hivemind/context/audits/2026-10-12_BENCH-BOOT-1_return.md 8017 bench-boot-1/run-and-delegation staged=6 tree=a17a7754d4c12f27ad48d9f14ebdb1e5ccb8f9e9
