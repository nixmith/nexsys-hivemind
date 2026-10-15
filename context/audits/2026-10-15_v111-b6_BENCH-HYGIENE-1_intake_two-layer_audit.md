<!--
file: context/audits/2026-10-15_v111-b6_BENCH-HYGIENE-1_intake_two-layer_audit.md
purpose: the two-layer intake of BENCH-HYGIENE-1's return (five bench instruments, staged on `bench-hygiene-1/tools-prewarm-wear-timing` off `5cf3bd0`; tree `7a76220b…`): layer 1 the return against the charter §6; layer 2 the staged tree by `git archive` with every suite run in the desk VM, the RED re-run against the PARENT tree's files (D-v111-32's second line), the diff's one hunk, the constants md5, the boot line on D1's stamps; the deviations ruled; the findings → the register; the landing card → BP11.
audience: the hub · Nick (§0; the card)
state-type: audit (filed once; never edited)
status: FILED v111 beat 6 (Thu 2026-10-15 ~09:3x CT; instrument 2026-10-15T14:39:41Z)
-->
# BENCH-HYGIENE-1 — the intake (two layers)

## §0 Verdict
**INTAKEN — ACCEPT; the five instruments LAND as BP11.** The return (11,856 B, md5 `c2c0af8dadafa6cd151cc1c04b9f584e`) meets §6 line by line (§1). Layer 2 (§2): the staged tree `7a76220bb7f8373e931bce036d90ce0f233231e8` extracted by `git archive` runs `bench.sh selftest 44/0` · `verify72h 66/0` · `breakdown 10/0` · `test_engine 48/0` · `test_harness 29/0` · `nightly_digest --selftest 54/0` here; **with `5cf3bd0`'s files under the staged tests the new checks go RED exactly as recorded** — `grader.py`/`export.py` → 66/2 (U8-1, U8-2); `bench.sh` → 44/1 (pw1); `nightly_digest.py` + no `boot_timing.py` → 48/6 (WR-1..3, BT-1..3) — the tests bite, not only pass. `git diff --cached -U0 -- tools/bench.sh` = ONE hunk (`-263,0 +264,9`, the `pre-warm)` arm), 0 lines naming `do_start`/`radio_wait`/`unit_start`, `tools/systemd/*` untouched — the Oct 19 sitting's dry-run stands. `constants.yaml` `9b0af47b3376` in the tree. `boot_timing.py` on D1's stamps → `Loaded=+2.337 projection_live=+22.758 network_resumed=+31.596` (the b2 audit's numbers); `pre-warm` prints its line and exits 0. D1–D11 ruled (§3); the findings IR-216 and the five rows' cells by id (§4). The landing card in Nick's form (§5).

## §1 Layer 1 — the return against the charter (§6)
| §6 asks | the return | verdict |
|---|---|---|
| §0b's eight rows re-run and pasted | §1: all eight hold; the "after" reads given for the hub (row 4 `… 264`; row 7 `4`, all in `test_verify72h.py`) | met |
| five deliverables staged (or §1.5 stopped with its finding) | staged=8; §1.1–§1.5 each with its hunk; TB-1 not RED today (the grader reads keys by name) — pinned by mutation | met |
| each new check RED first with the text pasted, then GREEN | U8-1/U8-2 · pw1 (pw2 a pin, RED by mutation M1/M2) · WR-1..3 (+ the empty-tsv case) · BT-1..3 · TB-1 (by mutation) — the texts verbatim, stamped | met |
| every suite GREEN in the VM | 44 · 66 · 10 · 48 · 29 · 54 — before → after → the archive | met; re-run here (§2) |
| `constants.yaml` unchanged · the `bench.sh` diff = the arm only · zero commits · `write-tree` in §0 and the RETURNED line · ≤ 15,000 B by 18:00 | `9b0af47b3376` · one hunk, 0 start-path lines · HEAD `5cf3bd0`, 0 ahead · `7a76220b…` both places · 11,856 B at 12:31Z (07:31 CT) | met, ten hours early |

## §2 Layer 2 — the hub's own re-execution (the desk VM; `/tmp/bh1` from `git archive 7a76220b…`)
1. The six suites, the staged tree: `bench.sh selftest: 44 check(s), 0 failure(s)` · `verify72h selftest: 66 check(s), 0 failure(s)` · `breakdown selftest: 10 check(s), 0 failure(s)` · `selftest: 48 check(s), 0 failure(s)` (engine) · `selftest: 29 check(s), 0 failure(s)` (harness) · `selftest: 54 check(s), 0 failure(s)` (the digest's pinned examples).
2. **The RED re-run against the parent** (`git show 5cf3bd0:<file>` swapped into the extracted tree, one deliverable at a time, the staged tests kept): `tools/verify72h/{grader,export}.py` → `66 check(s), 2 failure(s)`; `tools/bench.sh` → `44 check(s), 1 failure(s)`; `tools/runner/nightly_digest.py` with `boot_timing.py` removed → `48 check(s), 6 failure(s)`; the staged files restored → 48/0.
3. The diff: `git diff --cached -U0 -- tools/bench.sh` → 1 hunk (`-263,0 +264,9`, under `case "${1:-}" in`); `grep -c 'do_start\|radio_wait\|unit_start'` over the cached diff of `tools/bench.sh` and `tools/systemd` → 0; `tools/systemd` has no cached change. `scenarios/constants.yaml` in the tree → `9b0af47b3376`.
4. The instruments on fixtures here: `boot_timing.py` on a five-line log carrying D1's stamps → `boot: launched=21:03:02.000 Loaded=+2.337 projection_live=+22.758 network_resumed=+31.596 network_up=+31.596 startup_failed=none`; `HS_STORE=<400-B file> bash tools/bench.sh pre-warm` → `pre-warm: read 400 B in 0.00 s · Cached 620784 → 620784 kB`, exit 0.
5. **Not re-executed:** the mutation runs (M1/M2; TB-1's in-process grader) — the lane's own record; the Windows desk (the lane measured in the VM; IR-183's instrument on the desk is the first card that runs a tool there); the Pi (the digest's wear row writes on the first nightly after BC10's pull).

## §3 Deviations ruled
D1 ACCEPT — a correction of IR-183's text: U+2014 sits in cp1252 (0x97) and never raised; the crash was U+2192's (`export.py:525`); the strict-UTF-8 check is the right instrument (the row amended by id). D2 INFO (the charter cited `6a40a10`'s lines; `5cf3bd0` moved them +204). D3 ACCEPT — the read-only python open in `export.py`'s form; no CLI. D4 ACCEPT — the boot id as the fifth field; a counter that restarted is no baseline. D5 ACCEPT — the template literal; one format string. D6 INFO. D7 ACCEPT — `-U0` and the sha256 pins of the three functions and the unit file: a later lane that changes the start path updates the pins on purpose. D8 INFO (exit 1 on a failed read). D9 INFO (102 lines / 79 code; the 120 holds). D10 INFO. D11 INFO (the `tmp_obj_*` leftovers; not locks).

## §4 Findings → the register
- **IR-216 (new):** `tools/nightly.sh:332` sends `compose`'s stderr to `/dev/null`, so the wear `[--]` line (and any digest stderr) reaches no Pi log; the `wear.tsv` row is written regardless, so the first reading is readable from the file. The fix is one wrapper line (`2>>` the nightly log) at the next bench touch; dry-run #2's packet reads `~/hs-bench/state/wear.tsv` directly meanwhile.
- **IR-183 → CLOSED** (the tool half landed; the row's U+2014 sentence corrected per D1; the desk instrument is the first Windows card that runs a tool).
- **IR-189 → the verb LANDED** (`bench.sh pre-warm`); the unit's `ExecStartPre=` stays OPEN for a later lane after the Oct 19 sitting, if the household power-cut case still wants it.
- **IR-190 → the instrument LANDED** (`boot_timing.py`); the packet text (dry-run #2) still owed — OPEN, narrowed.
- **IR-213 → the digest line LANDED**; OPEN until the first number (two nightly rows on the Pi after BC10's pull; IR-216's wrapper line for the `[--]` case).
- **IR-214 → the TB-1 pin LANDED** (the grader indifferent to the eighth component); the bump itself still owed post-run — OPEN.

## §5 The landing (Nick's form)
`_scratch/v111/b6/card_bench_land_bh1.txt` — gated on HEAD `5cf3bd0`, branch `bench-hygiene-1/tools-prewarm-wear-timing`, staged = 8, trailers 0, `git write-tree` = `7a76220bb7f8373e931bce036d90ce0f233231e8`; the commit; `HEAD^{tree}` asserted; `git switch main`; `merge --ff-only`; the push; porcelain 0 → `BENCH: LANDED <sha>` = **BP11**. The message `_scratch/v111/b6/2026-10-15_bench_BENCH-HYGIENE-1_commit-msg.txt`. The §A.2 unit card's BLOCK 1 EXPECT is re-stamped from `6a40a10` to BP11's sha in the b6 hivemind splice (Nick's gap 2).
