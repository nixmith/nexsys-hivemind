<!--
file: context/audits/2026-09-27_v82-b3_METER-3-intake_audit.md
purpose: The v82 beat-3 audit — METER-3's return intaken two-layer (the lane's claims read critically; the hub's own selftest, lint, byte counts, greps and code reads on the bench tree); the deviations ruled; `BIAS:` asked with the rec; BENCH-PULL-1 cut (the Pi's bench clone must take the landing before the next nightly); the beat rotation. The non-re-executions named.
audience: the hub (the record) · Nick (§0)
state-type: intake audit
status: FILED — v82 beat 3 (Sun 2026-09-27 ~12:4x CT; instrument 2026-09-27T17:46:47Z)
-->

# v82 beat 3 — METER-3 intaken; the bench card; BENCH-PULL-1; the rotation (Sun 2026-09-27 ~12:4x CT)

## §0 The verdicts
- **METER-3's return** (`context/audits/2026-09-27_METER-3_return.md`, 8,143 B; RETURNED 12:3x CT; the second read-only check the lane ran caught five cite slips, corrected before RETURNED): **ACCEPT.** Every claim the hub could re-execute holds (§1); the nine deviations ruled (§2); one word asked — `BIAS:` (§3).
- **The bench card** run by Nick → **`BENCH: LANDED 58b5b45`** (12:42:41 CT; porcelain 0; ahead 0; no trailer; the message `_scratch/v82/2026-09-27_bench_METER-3_commit-msg.txt`); the bench has no CI — the hub's own selftest run is the gate of record, and it reads `38 check(s), 0 failure(s)`.
- **BENCH-PULL-1 cut and EXECUTED** (`context/instructions/2026-09-27_BENCH-PULL-1_the-Pi-takes-METER-3_operator-card.md`; the outputs filed as `context/audits/2026-09-27_BENCH-PULL-1_outputs.txt`, 276 B): the Pi's `~/nexsys-bench` is the tree the nightly and `~/bench.sh` run from, and no bench-deploy card pulls it (BC3/BC4 pull the core clone only; the CHAR sitting's card 1 carried the pull) — without it Monday's nightly would have run boot-health without BH-2. At 17:42:45Z: `before: f1c2f9a` · `porcelain=0` · `Updating f1c2f9a..58b5b45` · `Fast-forward` · `after: 58b5b45` · `bh2=3 fresh=1` · the Pi's own `selftest: 38 check(s), 0 failure(s)` — every EXPECTED value matched. A standing rule from this (IR-76): every bench landing is followed by a BENCH-PULL block before the next nightly, and the nightly's digest should print the bench sha it ran on.
- **The beat rotation:** v80 b1–b4 (4 blocks) → `context/handoff/archive/pm-handoff-beats-v80b1-v80b4-rotated-2026-09-27.md`, verbatim; live 12 → 9 with this beat; bytes asserted inside the splice.
- **Beat 4's deliverables named:** VERIFY-72H's charter (the three attestations as gates) and IR-61's pre-verification + instruction on the rec (D-v82-15) — after BENCH-CORE-4's intake tonight.

## §1 METER-3 — two layers
**Layer 1:** the return read whole (8,143 B ≤ 8 KB): §0 the instruments (the selftest 36 → 36 with the engine alone → 38; the lint 13 legs; porcelain the five; `wc -c` before/after; the greps; the nine ages re-read; nine scripts) · §1 the engine hunks · §2 the constants' three maps + provenance · §3 the prompt table · §4 the tests (M3 T1, M3 T2; T3/T4 re-pinned) · §5 nine deviations · §6 not re-executed.
**Layer 2 (the hub, on the bench working tree at `f1c2f9a` + the edits):**
| The claim | The instrument | Result |
|---|---|---|
| the selftest `38 check(s), 0 failure(s)` | `cd tools/runner && python3 -B test_engine.py` — the hub's own run; the two M3 lines printed `[ok]` | CONFIRMED |
| the lint: 13 legs load | `python3 -B runner.py suite all --list` → `listed 13 leg(s) — all load lawfully` | CONFIRMED |
| porcelain = the five files; +545 −59; nothing staged | `git status --porcelain -uall`; `diff --stat`; `diff --cached` | CONFIRMED (5 ` M`; cached 0) |
| `wc -c` after: 35504 · 39784 · 124386 · 79638 · 3652 | `wc -c` | CONFIRMED |
| the greps: `confirm: enter` 0 · `fresh_within_s:` 9 · `bias_pct:` 9 · `photo` 0 · `~20` 1 · `dashboard` 2 | `grep -c` on the scenario | CONFIRMED |
| the three maps at `constants.yaml` :217/:225/:235 with the charter's figures; three provenance rows :627/:631/:635 | `sed -n`; `grep -n` | CONFIRMED (30/180/30 · 15/90/15 · 2.3/8.0/2.9) |
| BH-2: `zigbee.permit_join_opened` forbidden; the core's line | `boot-health.yaml` :67 (+ the comment :20–:21); `ZigbeeIntegrationAdapter.java` :922 at `e96dce8` — `log.info("zigbee.permit_join_opened: duration={}s", duration)` | CONFIRMED |
| `apply_freshness` (:2323) and `apply_bias` (:2363); the call site after the witness lands | the functions read whole: key absent → untouched; only a decided datum; `age = read_epoch − witness` (0.1 s); no numeric witness → VOID "never a pass by absence"; `age > window` → VOID with the reason, `verdict: VOID`, the ratio kept; `corrected_ratio = ratio / (1 + bias/100)` six places; `bias ≤ −100` refused; the call at :1714–:1718 | CONFIRMED |
| the witness's unit: `data.lastReported` is epoch seconds on the wire | the CHAR captures (`api-captures.json`: `lastReported":1790452428.435897`); the engine's WIRE PIN comment :114–:122 | CONFIRMED — a real read computes a real age |
| `nightly.sh` and the digest untouched | `git diff --name-only | grep nightly\|digest` → 0 | CONFIRMED |
Not re-executed: a live run against the Pi (none by the charter); boot-health against a boot (lint + selftest only — Monday's nightly is the instrument, after BENCH-PULL-1); the nine scripts replayed (their anchor asserts are the lane's).

## §2 The deviations, ruled
1–2 (the third constants map `step-s`; the `bias_pct` engine hook) — ACCEPTED: the charter's §1.3 and §1.5 needed them; §0's "two keys" and "the VOID path" were the charter's undercount. 3 (no numeric witness with the key set → VOID) — ACCEPTED: the strategy line's own rule — a sample vetoes a green, never grants one. 4 (the VOID's reason on the REP line and in the close) — ACCEPTED (§3's latitude). 5–6 (the lane's two script stumbles, nothing written) — disclosed at honest severity; no finding. 7 (T3 carries fresh witnesses; stale → VOID proven on the live route in M3 T1) — ACCEPTED. 8 (the constants comment names G4-2's first read, 152.6 s old, as the bias's basis) — ACCEPTED as honest; the figure is the charter's. 9 (three METER-3 notes in the scenario header) — fine.

## §3 `BIAS: tolerate | exclude` — asked with the rec
As landed, the verdict stays on the raw ratio and the bias rides beside it, so the TR3 (+7.1…+8.9 % over three steady reads) would read OUTSIDE its band on the run's loads every time. **Rec `tolerate`:** the offset is systematic and steady; the raw ratio is retained; a small bench unit (METER-3b, IR-75, ≤ 1 h, with VERIFY-72H's charter) judges the verdict on `corrected_ratio` when `bias_pct` is set — the TR3 stays in the run as the second vendor with its known offset removed. **`exclude`:** the TR3 leaves the run's loads; nothing else changes. Refutable-by: the next CHAR sitting's TR3 bias outside 8 ± 1 % (then exclude). Silence = tolerate.

## §4 BENCH-PULL-1 and the rotation
BENCH-PULL-1: one block, `bash -n` clean; before/after shas, porcelain, the fast-forward word, `bh2=3` (two comment lines + the entry) and `fresh=1`, the Pi's own selftest 38/0. The rotation: v80 b1–b4 → the archive named in §0; the archive map's row and the LIVE sentence re-cut; bytes(kept) + bytes(archived body) = bytes(before) asserted before the write.

## §5 Not re-executed, disclosed
The bench commit and push (Nick's hands; verified at the instrument after); BENCH-PULL-1's remote side (the Pi's lines are Nick's paste, filed; the desk side re-read at the outputs file); BENCH-CORE-4 (running or not yet started at this beat — its line is beat 4's first intake); the model METER-3 ran on.
