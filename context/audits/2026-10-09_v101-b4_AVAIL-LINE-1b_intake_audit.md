<!--
file: context/audits/2026-10-09_v101-b4_AVAIL-LINE-1b_intake_audit.md
purpose: AVAIL-LINE-1b (the wrapper hop ordered at D-v101-12) intaken two-layer at the v101 close: the lane's §7 read, the hub's re-execution on the staged tree (the five files; the wrapper hunk; the static check; the four selftests; the syntax check), the lock the lane met and whose it was, the landing card. The ruling is D-v101-18 in the v101 DR.
audience: the v101 hub · Nick (the landing card) · the v102 boot (by grep; BENCH-PULL-8's premise)
state-type: audit (one intake)
status: FILED — v101 beat 4 (Fri 2026-10-09 ~13:0x CT; instrument 2026-10-09T18:07:01Z)
-->

# AVAIL-LINE-1b — intake, two layers (Fri 2026-10-09 ~13:0x CT)

## §1 Layer 1 — the return's §7 (`context/audits/2026-10-09_AVAIL-LINE-1_return.md`, now 10,976 B; `RETURNED … staged=5` its last line)
Resumed 12:54 CT in the same Claude Code session. **STOP at a lock, 17:54:27Z:** `.git/index.lock` in `nexsys-bench`, 0 B, mtime 09:21:34 CT, no `git.exe` running — the lane stopped and wrote the row (THE LANE STOPS AT A LOCK). The lock was the hub's: the residue of the `git write-tree` this hub ran at 09:21 CT from a shell that cannot delete (disclosed at D-v101-12); Nick removed it by hand at ≈ 12:58 and the lane resumed on the hub's word. Then: the static check RED first (`want: ['--fleet-avail $NB_FLEET_AVAIL', '--fleet-rows $NB_FLEET_ROWS', '--fleet-stale $NB_FLEET_STALE'] / got : []` → 54/1), the wrapper edit (`nightly.sh:308–:313` the three pairs in the file's own continuation form; `:314` the echo gains ` · avail: a/r`), GREEN (54/0); `bash -n` clean; the four closing lines on the desk (54/0 · 46/2 Windows-only · 42/0 · 27/24 Windows-only); five files staged, tree `f50d45b29ad296cb9e454ce6a6b5d258e66023ca`, 0 commits; `constants.yaml` md5 unchanged. D6 [INFO]: two comments in `nightly.sh` (:295, :324) still say "three" — untouched per "nothing else"; D7 [INFO]: the return now exceeds §0's 8,192-B ceiling by the append the 1b instruction ordered.

## §2 Layer 2 — the hub, on the device (Linux shell)
`branch=avail-line-1/ir118-join-rejected head=ba846c2 ahead=0 locks=0`; `diff --cached --name-only` = the five (`tools/nightly.sh` · `tools/runner/README.md` · `tools/runner/nightly_digest.py` · `tools/verify72h/grader.py` · `tools/verify72h/test_verify72h.py`); unstaged 0; untracked 0. The wrapper hunk read whole: the three pairs after `--fleet-reseen`, the echo with ` · avail: $NB_FLEET_AVAIL/$NB_FLEET_ROWS` — the line the operator reads now carries the field (the lesson of beat 4). The static check's asserts in the selftest hunk read. Re-run by the hub: `selftest: 54 check(s), 0 failure(s)` · `42/0` · `verify72h selftest: 46 check(s), 0 failure(s)` · `bench.sh selftest: 27 check(s), 0 failure(s)` (the Windows-only classes green here, as before) · `bash -n tools/nightly.sh` clean · 0 trailers in the cached diff. Not re-executed: the Pi's own nightly (Saturday 03:30 is the first run of the line with the field; SOAK-NIGHT-2's P10′ reads it).

## §3 The ruling — ACCEPT; the landing card
D6 → a two-word follow-on on IR-118's row, not a blocker; D7 → governed by the rider, accepted. The landing: `_scratch/v101/b4/card_bench_land.txt` — the commit from the staged tree on the branch (the hub's message, 0 trailers), `git switch main`, the ff-merge, the push → `BENCH: LANDED <sha>`; BC9a's STATE line then carries `AVAIL-LINE-1: LANDED <sha>` and Part B pulls it to the Pi (`nightly-flags ≥ 1`); IR-118 CLOSES when Saturday's digest line reads `avail: n/10`.
