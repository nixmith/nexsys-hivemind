<!--
file: context/audits/2026-09-13_v72-b7_P-1_intake_two-layer-audit.md
purpose: The hub's two-layer intake of P-1's return (the power harness as a bench verb, dry-run only): the return read critically, the gate and the regression re-run on the device inside the splice, the six open questions ruled, the bench card handed.
audience: Nick (§0, §3) · the hub (R-5's charter carries the fold rulings) · the bench lane
state-type: intake audit
status: FILED Sun 2026-09-13 ~13:2x CT (instrument 2026-09-13T18:22:51Z); verdict ACCEPT; the bench card handed (4 files)
-->

# P-1 — intake, two layers

## §0 The verdict
**ACCEPT.** The return (`context/audits/2026-09-13_P-1_return.md`, 12,286 B, `RETURNED` last line) is repo-complete on bench `4539f13`: 3 A + 1 M (`tools/harness/harness.py` 22,749 B · `tools/harness/test_harness.py` 15,249 B · `docs/2026-09-13_P-1_power-harness_design.md` 8,176 B · `scenarios/constants.yaml` +57/−0), nothing staged, no commit by the lane. P1–P4 held; the gate is green on the device; the fence (no live command, no network call) is enforced by the tests themselves. Six defects the lane found in its own driver are fixed with regression checks. The bench card is Nick's next act; the S31 stays `harness-candidate` until his word.

## §1 Layer 1 — the return, read critically
The card leads with the census, the RED→GREEN gate (16/16 failures at HEAD, 19/19 checks after), zero live commands and zero network calls under an instrumented chokepoint, and a design doc 16 bytes under its ceiling. P4 found five wrong cites in the hub's charter: `tools/runner/README.md` names no test framework (the repo has no `test_*.py`, pytest is not installed), the charter's core pin `1e26912` is superseded by `a458a64`, `constants.yaml` already carries a top-level `plugs:` map at :336 with a different shape, "stdlib only" cannot coexist with reading `constants.yaml` (the lane used `yaml.safe_load` as `engine.py:107` does and filed it), and the exit-code vocabulary differs from the engine's. The self-audit's worst find: the test suite could not detect deletion of the factory-reset-hazard guard (the fixture's cap refused first and the assertion was a disjunction) — it now goes RED; two safety holes (a negative `--off-for` that would have commanded off and never restored; a caller-chosen `--window` label that reset the factory-reset budget) are closed. The lane removed a 0-byte `.git/index.lock` after asking Nick's permission.

## §2 Layer 2 — the hub's re-executions at the bytes (run inside this beat's splice; the splice refuses on a mismatch)
1. Bench porcelain: exactly ` M scenarios/constants.yaml`, `?? docs/2026-09-13_P-1_power-harness_design.md`, `?? tools/harness/` (two files); HEAD `4539f13`; nothing staged; no `.git/index.lock`.
2. The gate: `python3 -B tools/harness/test_harness.py` → `selftest: 19 check(s), 0 failure(s)`, exit 0, the last check `[ok] THE FENCE — zero network calls made across the whole gate`. The regression: `python3 -B tools/runner/nightly_digest.py --selftest` → `21 check(s), 0 failure(s)`.
3. `constants.yaml`: `git diff --numstat` = 57 insertions, 0 deletions — additive; the new block is `harness:` (a list of rows) and names the pre-existing top-level `plugs:` map at :336 as a different collection.
4. The driver imports `urllib.request`/`urllib.error` for the live leg only; the dry-run path is the one the tests run under sockets monkeypatched to raise, and the gate's fence check passes.
**Not re-executed, disclosed:** the six defect fixes were not read line by line (the gate that pins them was run); the vendor figures behind `rating_w: 1800` were not re-sourced (they are marked provisional by the lane and gated below).

## §3 The six open questions, ruled
1. **`rating_w: 1800` provisional — the pairing ACCEPTED, with the label read scheduled.** A retail listing is not a safety fact. The label is read at the next rig slot (H8-a's): one line, `S31-LABEL: <A> <W>`, and the profile gains `rating_source: label` when it matches; the `HARNESS-PLUG:` promotion is refused by the driver until then. No separate gate word.
2. **The R-5 fold: extend the reserved `plug:` stimulus key** in `SCENARIO_FORMAT.md` §1 rather than mint a parallel `harness:` key — one spelling for one act. Ruled now for R-5's charter (v73); the scenario format stays closed until then.
3. **Exit codes:** the harness adopts the engine's vocabulary (`REFUSED`=2) at the fold; until then its own table stands and is printed by `--dry-run`.
4. **The per-window cap gains a time bound** (`windowSeconds`) at the fold; the caller-supplied, never-defaulted `--window` label stays required as today.
5. **The label collision (`constants.yaml:283`, "MINTED … from the P-1 paste" — the quiesce arc's P-1, 2026-07-31):** two WUs share a name across two months. Disambiguated in the record as P-1 (quiesce, 2026-07-31) and P-1 (power harness, 2026-09-11); the comment at :283 gains the year-month at the fold. No file is renamed.
6. **Live mode has never executed:** agreed. The first live run gets its own operator packet — through THE PRIOR-LEDGER GATE — after R-5 or `HARNESS-PLUG:`, with the Hue's fourth uninstrumented silence (R-4c) as its first target.

## §4 Hub-owned misses (the charter's five wrong cites)
The test-runner cite; the stale core pin (the charter was cut before `a458a64`); the `plugs:` namespace; the stdlib clause vs the YAML read; the exit-code vocabulary. The prior-ledger gate covers the first and third (both live in the bench's own files); the pin would have been caught by the re-pin rule now applied to every packet.

## §5 The landing
The bench card: `git add --` the four paths, `staged: 4`, the trailer grep, `git commit -F ../_scratch/v72/2026-09-13_bench_P-1_commit-msg.txt`, push → `BENCH: LANDED <sha>`. The S31 stays `harness-candidate`; nothing fires live until Nick's word.
