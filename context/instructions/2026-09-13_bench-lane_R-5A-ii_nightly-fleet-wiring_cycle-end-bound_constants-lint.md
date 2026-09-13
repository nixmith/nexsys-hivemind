<!--
file: context/instructions/2026-09-13_bench-lane_R-5A-ii_nightly-fleet-wiring_cycle-end-bound_constants-lint.md
purpose: The R-5 Part A follow-up (three small rows the intake ruled): the nightly's fleet wiring (fail-safe), the harness cycle-end bound (SD-A4 extended to `at + off_for`), and the constants lint in `suite --list` (the duplicate-key class the Part A lane hit). Lands on the same bench card as Part A.
audience: the bench lane (a fresh Cowork conversation) · the hub · Nick (§3 is his paste)
state-type: lane instruction (small; the Files table governs)
status: EXECUTED — returned 2026-09-13 (`context/audits/2026-09-13_R-5A-ii_return.md`, 6,045 B; 11 paths with Part A), audited ACCEPT at v73 beat 6, landed bench `f3631cb` — banked v73 beat 7 (Sun 2026-09-13 ~18:1x CT; instrument 2026-09-13T23:18:34Z).
-->

# R-5A-ii — the nightly's fleet wiring, the cycle-end bound, the constants lint

## §0 The contract
- `date -u` first; the desk only; no device; `--dry-run` and the selftests are the only things you run. Baseline: `nexsys-bench` at `1201368` with Part A UNCOMMITTED (porcelain = the nine Part A paths; index empty); stop and report otherwise. Never `git add`/`commit`; every git call `--no-optional-locks`.
- **The return:** `nexsys-hivemind/context/audits/<your CT date>_R-5A-ii_return.md` (≤6 KB; §0 card first: the census of YOUR rows and the combined tree's census, P1–P3, the gates with counts; the last line `RETURNED <path> <bytes>`, printed to Nick).
- **Predictions:** P1 — your rows touch only the §1 files (the combined porcelain = Part A's nine + your additions, declared). P2 — each new check red at HEAD by construction, green after; the three gates (`test_harness.py`, `--selftest`, `test_engine.py`) grow and stay at 0 failures. P3 — `bash -n tools/nightly.sh` passes and a nightly composer line with `fleet: unread` is produced by the selftest fixture for the read-failure path.

## §1 The rows (the table governs)
| # | Path | A/M | What |
|---|---|---|---|
| 1 | `tools/nightly.sh` | M | after the suite, read the card's registry ids through the runner's existing read (the same read Part A's `fleet_from_reads` uses) and pass adopted/expected/re-seen to the digest composer; ANY failure ⇒ `fleet: unread` (never a red, never an early exit); the HANDS-OFF's intent is kept — additive to the line, no re-grade |
| 2 | `tools/runner/nightly_digest.py` + its selftest | M | the composer accepts the wired call shape; the fixture covers the read-failure path (`unread`) and the value path |
| 3 | `tools/harness/harness.py` + `test_harness.py` | M | SD-A4 extended: a cycle whose `at + off_for` exceeds `windowSeconds` is REFUSED (the window bounds the whole cycle); one red-first test |
| 4 | the `suite --list` path (`tools/runner/runner.py` or where `--list` lives — ground it) + `test_engine.py` | M | `--list` resolves `${C.*}` and REFUSES a scenario file or `constants.yaml` with a duplicate top-level key (PyYAML keeps the last silently — the Part A regression's class); one red-first test that feeds a duplicated key |
**Census claim: 6 M (+ the Part A tree unchanged).**

## §2 What to watch out for
The nightly runs on the bench card under the s31/nightly HANDS-OFF until R-5 Part B — your row 1 must not change what the suite RUNS or how the floor is graded; only what the digest line carries. Register C in every string; no product name.

## §3 The dispatch line (Nick pastes into a FRESH Cowork conversation with `ClaudeFolder` connected)
```
date -u first. You are the R-5A-ii bench lane for NexSys/HomeSynapse. Baseline: nexsys-bench at 1201368 with R-5 Part A uncommitted (porcelain = nine paths; index empty). Read nexsys-hivemind/context/instructions/2026-09-13_bench-lane_R-5A-ii_nightly-fleet-wiring_cycle-end-bound_constants-lint.md WHOLE, then the R-5 charter's §A1–§A2 for the ground. Apply the four rows, each check red before its edit, then green; run the three gates and bash -n tools/nightly.sh; no live command anywhere; never git add/commit; every git call --no-optional-locks. Write the return to nexsys-hivemind/context/audits/<today CT>_R-5A-ii_return.md (≤6 KB; §0 card first; the last line `RETURNED <path> <bytes>`) and say that line to Nick.
```
