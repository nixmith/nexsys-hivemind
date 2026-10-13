<!--
file: context/audits/2026-10-12_v110-b1_BENCH-BOOT-1_intake_two-layer_audit.md
purpose: The hub's two-layer intake of BENCH-BOOT-1's return (`audits/2026-10-12_BENCH-BOOT-1_return.md`, 8,017 B, md5 e7f044c92e29…): layer 1 the claims read against the charter's §0b/§3/§6; layer 2 the hub's own re-execution on the device shell against the staged tree `a17a7754…`. Verdict: ACCEPT; D1–D4 ruled; F1–F5 routed.
audience: the v110 hub · Nick (the landing card `_scratch/v110/b1/card_bench_land.txt`)
state-type: intake audit
status: FILED v110 beat 1 (Mon 2026-10-12 ~18:2x CT; instrument 2026-10-12T23:24:34Z)
-->
# BENCH-BOOT-1 intake — two layers

## §0 Verdict
**ACCEPT.** Unit A (`bench.sh run`, the unit file, the file-keyed delegation) whole; Unit B (the UTF-8 reconfigure) at six of §3's seven paths — the seventh (`nightly_digest.py`) already reconfigures at `:708` (D2, verified). §6's `row 7 = 0 0 0 0` is NOT met literally — it reads `1 0 0 0` — and the miss is the charter's, not the lane's: the criterion was cut on the premise that each suite's own output was the only cp1252 hazard; T3c runs `export.py` and `grader.py` as children and they print `→` (`export.py:525`) and `—` (`grader.py:1522`, `:1525`) — both outside §3's table, which binds ("nothing else is written"). The lane obeyed the table over the criterion, measured the fix in a /tmp copy and struck it [REVIEW]. The hub rules: the two tools' reconfigure lines are **a register row (IR-183 widened: the tool half), to ride the next bench lane** — not a rider on this landing (a rider has no dry-run of its own; it would change a staged tree whose write-tree the return records).

## §1 Layer 1 — the claims against the charter
| Claim (return) | Charter | Read |
|---|---|---|
| §0b nine rows re-run, all hold (row 7 `1 1 0 0` at `ceb08c5`) | §0b | consistent with the hub's own greps at the charter's cut |
| four suites GREEN on the staged tree: 57/0 · 42/0 · 54/0 · 42/0 | §6 | ≥ 36/0 met (42) |
| RED observed on every new check — 42/13 against `ceb08c5`'s `bench.sh` with no unit file; r0/r2 green by construction (D6) | §6 | the red texts quoted per check |
| row 7 `1 0 0 0` | §6 says `0 0 0 0` | D1 — ruled in §0 |
| `constants.yaml` md5 `9b0af47b3376`; nightly.sh/scenarios cached diff empty | §6 | — |
| exactly §3's seven paths staged → **six** | §6 | D2 — the seventh needs no change (verified) |
| zero commits; `git write-tree` `a17a7754d4c12f27ad48d9f14ebdb1e5ccb8f9e9` in §0 and the RETURNED line | §6 | — |
| D3 the case arms byte-identical; the switch redefines `do_start`/`do_stop` when enabled | §1 (T3b pins the arms) | ACCEPT — the design the charter wanted; T3b 57/0 proves the arms |
| D4 two guards past §1.3 (the delegated start refuses while an app runs outside the unit; the delegated stop names a survivor, exit 1, no pkill) | §1.3 | ACCEPT — conservative: a race becomes a stop. Consequence F1 (below) |
| D7 `XDG_RUNTIME_DIR` set on the systemctl calls only | §1 | ACCEPT |

## §2 Layer 2 — the hub's re-execution (device shell, Python 3.10.12, bash; `TMPDIR=/tmp`)
1. **The index:** `git diff --cached --name-status` = 6 (README.md M · tools/bench.sh M · tools/runner/test_engine.py M · tools/systemd/bench-boot.service A · tools/test_bench_sh.py M · tools/verify72h/test_verify72h.py M); `diff --cached --stat` = `6 files changed, 704 insertions(+), 1 deletion(-)`; unstaged diff 0 lines (worktree == index); branch `bench-boot-1/run-and-delegation` at `ceb08c5` = `main` = `origin/main` (ff-only merge possible); `git write-tree` = **`a17a7754d4c12f27ad48d9f14ebdb1e5ccb8f9e9`** (= the RETURNED line). `diff --cached -- tools/nightly.sh scenarios` 0 B; `constants.yaml` md5 `9b0af47b3376`.
2. **The four suites on `git archive a17a7754…` → /tmp/bb1 (86 files), `PYTHONIOENCODING=utf-8`:** `verify72h selftest: 57 check(s), 0 failure(s)` · `selftest: 42 check(s), 0 failure(s)` · `selftest: 54 check(s), 0 failure(s)` · `bench.sh selftest: 42 check(s), 0 failure(s)`. **Row 7 (cp1252):** `1 0 0 0`.
3. **RED re-executed:** the staged tests over `ceb08c5:tools/bench.sh` → `bench.sh selftest: 42 check(s), 12 failure(s)` (the return says 13: its RED had no unit file; the hub's copy kept the staged unit file, so r9 is green — the difference is explained by construction, not a disagreement).
4. **The delegation against the hub's OWN stubs** (`/tmp/bb1-h`: stub `systemctl` keyed on a state file, stub `pgrep`/`pkill`/`nohup`/`curl` that log their calls; a temp HOME; the wants link made by hand): (A) not enabled, `stop` → `pgrep` only, "nothing was running", no `systemctl` call; (B) enabled, inactive, app down, `start` → `systemctl --user show -p ActiveState --value bench-boot` with `XDG=/run/user/1524`, `pgrep`, `systemctl --user start bench-boot`; a NEW log behind `current.log`; `[OK] started bench-boot -> …` · `[OK] RADIO UP after 1s`; **no `nohup`, no `pkill`**; (C) enabled, `stop` → `systemctl --user stop bench-boot`, `pgrep`, `[OK] stopped (bench-boot)`, no `pkill`; (D) enabled, `systemctl start` failing → `[!!] bench-boot is enabled but systemctl --user start bench-boot failed (exit 1): Failed to start bench-boot.service: Unit not found. — the nohup path is not taken`, exit 1, no `nohup`; (E) enabled and active → `[!!] already running — use: bench.sh restart`, exit 1; (E2) enabled, inactive, an app running outside → the D4 guard line, exit 1; (G) `status` → the running line, then `unit bench-boot (enabled): ActiveState=… SubState=… Result=… NRestarts=…`.
5. **D1's mechanism:** `grep -nP '[^\x00-\x7F]'` over the two tools' `print` lines → `export.py:525` (`→`), `grader.py:1522`, `:1525` (`—`). **D2:** `nightly_digest.py` `_utf8_stdout()` defined `:76`, called `:708` and `:1031`. **The unit file:** `StartLimitIntervalSec=300` · `StartLimitBurst=5` · `Type=exec` · `ExecStart=%h/nexsys-bench/tools/bench.sh run` · `KillSignal=SIGTERM` · `SuccessExitStatus=143` · `TimeoutStopSec=90` · `Restart=always` · `RestartSec=10` · `RestartPreventExitStatus=10` — the packaged unit's eight.
6. **Not re-executed (disclosed):** no real systemd ran here either (the device VM has no user manager for this HOME); the 22 mutants; the 7-run flake check; the lane's WSL rows. The source reading of `do_start`'s `&`/`ln` order (return §6) stands on `:41–:47` unchanged.
7. **A hazard the hub's own call made:** `git write-tree` on the device left `.git/index.lock` it could not unlink (the no-delete rule); renamed to `.git/stale-index-lock-v110b1-231126Z` (named in the card; deleted there by exact path). Lesson: on the device, read the lane's tree with `git archive <tree-sha>`; never run an index-writing git verb there.

## §3 The rulings and the routing
- **D1 → IR-183 widened** (the tool half): `export.py` and `grader.py` reconfigure stdout/stderr in `__main__` (two lines each; `main()` placement breaks nine in-process checks — measured by the lane); the instrument: row 7 reads `0 0 0 0`. Rides the next bench lane.
- **D2 → ACCEPT**, no row. **D3, D4, D7 → ACCEPT.** D5, D6 → INFO.
- **F1 → IR-185 + the unit cards' input (row (iv)):** §A.2's BLOCK 3 order — the legacy `bench.sh stop` BEFORE `systemctl --user enable`, then `bench.sh start` (delegated); the current order stops an inactive unit and leaves the nohup app, which D4's guard turns into a halt.
- **F2 → IR-186:** the start limit (5 / 300 s) counts manual starts; a refused delegated restart leaves the app down until `systemctl --user reset-failed bench-boot` — the unit cards and BC10's rollback carry the `reset-failed` line.
- **F4 → IR-187:** the unit runs in the user manager's environment (no login shell): `java` on the app launcher's PATH / `JAVA_HOME` is a premise for the Oct 19 sitting; BLOCK 3's health read is its instrument; a reviewer's read of the nightly's user unit is not evidence.
- **F3 = D1. F5 → INFO** (the runner's 300-s timeout covers ≈ 225 s).
- **The landing:** `_scratch/v110/b1/card_bench_land.txt` (Nick's rules, D-v109-12: the one deletion by exact path; `HEAD^{tree}` asserted = `a17a7754…`; porcelain 0 as the last read); the message `_scratch/v110/b1/2026-10-12_bench_BENCH-BOOT-1_commit-msg.txt` (3,475 B; 0 trailers). BC10's bench pull names the landed sha beside BP9 + BP10 (`ceb08c5`); the unit is enabled at the Oct 19 sitting, not before.
