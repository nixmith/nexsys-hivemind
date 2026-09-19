<!--
file: context/audits/2026-09-19_BENCH-METER-1b_return.md
purpose: BENCH-METER-1b return — the two subtractions, on_outside/VOID, min:, the witness, the real file walked live-path; 4 M + 0 A on 764e537.
-->
# BENCH-METER-1b — return (bench lane, Sat 2026-09-19 CT)

## §0 The card
- **Baseline:** `764e537 bench: BENCH-METER-1`, porcelain empty, `ENGINE_VERSION` at :91 as cited. Premise rows re-grepped at 764e537 before the first edit: all at their cited lines; one drift — `requires:` is `metering-known-load.yaml:75`, not `:78`.
- **Census (EXACT):** ` M scenarios/SCENARIO_FORMAT.md` · ` M scenarios/metering-known-load.yaml` · ` M tools/runner/engine.py` · ` M tools/runner/test_engine.py` — **4 M + 0 A + 0 D**; `diff --cached` empty (staged nothing, committed nothing); `constants.yaml` no diff; `provenance` absent from the diff; the format 4 lines added, 0 removed; no hardware, no Pi.
- **P1** HELD. **P2** red-then-green HELD; the count MISSED as worded: +5 `check_fn` rows (31 → 36; T5 re-cut in place), each multi-case (≈ 16 cases). **P3** 13 legs, `metering-known-load tier=OPERATOR requires=metering-plug,command-api` — HELD. **P4** TR3 rep 1 `4.591 %` alone / `3.755 %` tared WITHIN; G4-2 rep 1 `4.472 %` OUTSIDE; the close names one line — HELD. **P5** `reference_effective 78.9`, WITHIN — HELD. **P6** 43/0 — HELD. Inside the half-day (≈ 25 min).

## §1 Rows
- **R1** `FIELD_WITHIN_OPTIONAL_KEYS` · `field_within_check(…, reference_subtract, field_subtract)`: Decimal per operand, `ref_eff ≤ 0` → `void` before the value is read; receipt +`reference_subtract/reference_effective/field_subtract/value_effective/on_outside`. **R2** `on_outside` linted (`record` ⇒ tier OPERATOR); state `recorded` → `run.recorded` + `recorded_close()` in the live loop AND the fixture arm; deadline-VOID via `void_at_deadline()`; default `fail` = BENCH-METER-1 byte-for-byte. **R3** `print_rep()` as the datum is decided. **R4** `min:` (lint shape; capture refuses below the floor; receipt keeps it). **R5** `FRESHNESS_WITNESS_KEY = "data.lastReported"` (WCAP capture-5 :76; s31-nightly-0902 raw) → `witness_key`/`witness`, null when absent, never asserted. **R6** `ENGINE_VERSION = "BENCH-METER-1b-2026-09-19-subtract-record"`.
- **S1** `requires: [metering-plug, command-api]`, REQUIRES paragraph gone. **S2** header (a)–(g), METHOD verbatim. **S3** 22 entries per plug G4-1 · TR3 · G4-2 (tare + offset `min: 0`, volts ×2, A ×3 each behind a LOAD STEP), CHAR-AFTER last. **S4** nine asserts +`reference_subtract` +`field_subtract` +`on_outside: record`, `within: 10s` and tolerances unchanged. Format §5: one REOPENED/CLOSED bullet + three mechanics, additive.

## §2 Red → green
Tests alone on 764e537: **36 checks / 7 failures**, each for the predicted reason — T1 `unknown key(s) ['reference_subtract']`; T2 `['on_outside']`; T6 `['min']`; T3-walk `unmet_requirements == []` (operator); T4 and T5 `requires` still `['operator', …]`; T3-list `requires=operator,…`. Engine landed: 4 red (the scenario rows). Scenario landed: **36 / 0**.

## §3 The instruments, verbatim (on the tree, 12:31 UTC)
- `python3 -B tools/runner/test_engine.py` → `selftest: 36 check(s), 0 failure(s)`
- `python3 -B tools/runner/nightly_digest.py --selftest` → `selftest: 43 check(s), 0 failure(s)`
- `python3 -B tools/runner/runner.py suite all --list` → `runner BENCH-METER-1b-2026-09-19-subtract-record @ 764e537` · `[LOAD] metering-known-load tier=OPERATOR requires=metering-plug,command-api` · `listed 13 leg(s) — all load lawfully`

## §4 The walk's nine REP lines (T3, printed by the selftest)
```
REP a_watts_g4_1_r1 — power_w=80.1 − 0.0 = 80.1 vs A=80.9 − 0.5 = 80.4 → r=0.996269 |r−1|=0.373 % vs 3.03 % → WITHIN
REP a_watts_g4_1_r2 — power_w=79.4 − 0.0 = 79.4 vs A=80.8 − 0.5 = 80.3 → r=0.988792 |r−1|=1.121 % vs 3.03 % → WITHIN
REP a_watts_g4_1_r3 — power_w=80.3 − 0.0 = 80.3 vs A=80.9 − 0.5 = 80.4 → r=0.998756 |r−1|=0.124 % vs 3.03 % → WITHIN
REP a_watts_tr3_r1 — power_w=76.9 − 0.0 = 76.9 vs A=80.6 − 0.7 = 79.9 → r=0.962453 |r−1|=3.755 % vs 4.03 % → WITHIN
REP a_watts_tr3_r2 — power_w=80.0 − 0.0 = 80.0 vs A=80.7 − 0.7 = 80.0 → r=1.000000 |r−1|=0.000 % vs 4.03 % → WITHIN
REP a_watts_tr3_r3 — power_w=80.0 − 0.0 = 80.0 vs A=80.6 − 0.7 = 79.9 → r=1.001252 |r−1|=0.125 % vs 4.03 % → WITHIN
REP a_watts_g4_2_r1 — power_w=76.9 − 0.0 = 76.9 vs A=81.0 − 0.5 = 80.5 → r=0.955280 |r−1|=4.472 % vs 3.03 % → OUTSIDE
REP a_watts_g4_2_r2 — power_w=80.0 − 0.0 = 80.0 vs A=80.9 − 0.5 = 80.4 → r=0.995025 |r−1|=0.498 % vs 3.03 % → WITHIN
REP a_watts_g4_2_r3 — power_w=80.3 − 0.0 = 80.3 vs A=81.0 − 0.5 = 80.5 → r=0.997516 |r−1|=0.248 % vs 3.03 % → WITHIN
```
TR3 rep 1 alone: `76.9 vs 80.6 → 4.591 % OUTSIDE at 4.03`. The close: `FAIL — 8/9 positive WITHIN; 1 recorded OUTSIDE/VOID (on_outside: record): positive[6] a_watts_g4_2_r1 OUTSIDE (|r−1| 4.472 % > 3.03 %)`; 22 typed + 9 read receipts in the bundle.

## §5 Deviations and limits
- [INFO] VOID under `fail` ends the run as FAIL (OUTSIDE's class); a non-numeric reference/subtract is FAIL-now under both modes (a defect, not a result); a bare `subtract:` is lint-REFUSED by name. T5's second check also forces `command-api` TRUE (no live value read).
- [REVIEW] `tools/runner/README.md` describes field_within at BM1 — not in the table, untouched.
- Limits: the desktop file tool was down, so the four files were edited in the session workspace and written back to the tree (checksums verified both ways); the instruments ran on the tree. No Pi banner check (Thursday's).

RETURNED nexsys-hivemind/context/audits/2026-09-19_BENCH-METER-1b_return.md 5780
