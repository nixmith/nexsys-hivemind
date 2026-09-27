<!--
file: context/audits/2026-09-27_METER-3_return.md
purpose: METER-3 bench CODE lane return (charter context/instructions/2026-09-27_bench-lane_METER-3_…_charter.md). Fresh Cowork session; device_bash. `date -u`: start 16:54:14Z (11:54 CT); filed 17:3xZ (12:3x CT), Sun 2026-09-27.
-->
# METER-3 return — Sun 2026-09-27 (v81)

## §0 Verdict and the instruments
**DONE — every §1 decision implemented; nothing committed; nothing talked to the Pi; no token printed.** Baseline: `f1c2f9a bench: METER-2 — …`; porcelain 0.
- Selftest BEFORE any edit: `selftest: 36 check(s), 0 failure(s)` · AFTER: `selftest: 38 check(s), 0 failure(s)` (36 + M3 T1 + M3 T2). After the engine edit ALONE (no scenario/test touched): still `36 check(s), 0 failure(s)` — "byte-identical without the key" demonstrated.
- Lint: `runner.py suite all --list` → `listed 13 leg(s) — all load lawfully`.
- Porcelain = §3's five (` M` boot-health.yaml, constants.yaml, metering-known-load.yaml, engine.py, test_engine.py); `diff --stat` +545 −59.
- `wc -c` before → after: metering-known-load.yaml 25813 → 35504 · constants.yaml 35762 → 39784 · engine.py 117609 → 124386 · test_engine.py 66025 → 79638 · boot-health.yaml 3048 → 3652.
- Greps (metering-known-load.yaml): `confirm: enter` 0 (0 below `stimulus:`) · `fresh_within_s:` 9 · `photo` 0 · `~20` 1 (:17, header quote, pre-existing) · `dashboard` 2 (:29, :41, header comments, pre-existing; none in a prompt) · `permit_join_opened` 1 active entry in scenarios/ (boot-health.yaml:67; 4 raw grep lines: comments :20–21, constants.yaml:15).
- Evidence re-read at the bytes: ages G4-1 1.7/2.1/0.2 s · TR3 164.5/87.1/105.3 · G4-2 152.6/375.6/598.7 (one witness thrice) = the audit's table; under the new windows TR3 stands, G4-2's three VOID.
- Scripts (guarded; anchor counts asserted before writing): `_scratch/v81/sun0927/meter3_*.py` (9) + `meter3_selftest_{before,after}.txt`.

## §1 The engine (engine.py; hunks :93–110, :337, :376–390, :1660–1675, :1704–1717, :1735–1742, :1818, :2323–2382)
- `FIELD_WITHIN_OPTIONAL_KEYS` += `fresh_within_s`, `bias_pct`; lint: a number or one whole reference, `fresh_within_s` < 0 REFUSED.
- `eval_field_within` (def :1677; the calls :1714–1717) — `read_at` once; after the witness lands: `apply_freshness(state, receipt, fresh_within_s, read_at.timestamp())`, then `apply_bias(receipt, bias_pct)`. `apply_freshness` :2323 — key set AND a decided datum: receipt gains `fresh_within_s`, `witness_age_s`; `age > window` (edge fresh) → `void`, `verdict: VOID`, `reason: "stale witness: age <a> s > <w> s"`, `ratio`/`deviation_pct` KEPT. Key absent → untouched. The VOID reaches the close by the EXISTING route (eval_api_line `void` + `record` → `recorded` → `record_result` → `recorded_close`; under `fail` → FAIL).
- `print_rep`: a stale VOID prints its ratio + `→ VOID (stale witness: …)`; the r=undefined line unchanged; with `bias_pct` every REP line ends ` · bias=<b> % r_corr=<corrected_ratio>`. `recorded_close`: a stale VOID's figure = its reason. `apply_bias` :2363: `corrected_ratio = (value_eff / reference_eff) / (1 + bias/100)`, Decimal, 6 places; the verdict untouched.

## §2 The constants (constants.yaml `metering:` :200–:238; `provenance.metering` :626–:638)
`fresh-within-s: {g4-1: 30, tr3: 180, g4-2: 30}` · `step-s: {g4-1: 15, tr3: 90, g4-2: 15}` · `bias-pct: {g4-1: 2.3, tr3: 8.0, g4-2: 2.9}` — copied from the charter §1.2/§1.3, never re-derived. One provenance row per key: `bundle: "metering-known-load-20260926T225552Z"` (verified at the capture's MANIFEST.txt) · `basis:` (fresh: the nine ages, Gen4 ≈ 5 s ×6, TR3 165 s ×3; step: ≥ the cadence; bias: 2.19/2.44 → 2.3, 7.108/7.824/8.867 → 8.0, 2.941 → 2.9) · `audit: "hivemind context/audits/2026-09-26_v81-b4_CHAR-bundle_intake_two-layer-audit.md §…; copied from the METER-3 charter §1.x"`. `check_ulid_provenance` (:844) reads `card` + `ulids` only; `ulids` unchanged.

## §3 The prompts (metering-known-load.yaml)
| where | before → after |
|---|---|
| CHAR-BEFORE act | "…and press ENTER." + `confirm: enter` → "…The four prompts that follow ask for CHAR-BEFORE's numbers from the sheet…"; no `confirm:` |
| `let:` head | + `char_before_{b1_offset,b1_spread,b2_offset,b2_spread}_w`: `type: number`, no `min:`; each prompt names the subtraction (B − A, sign kept), ÷ 3 or max − min, "Type that … in watts" |
| 9 REP prompts | "at least 15 s… lit value again (the TR3 up to a minute)" → "at least `${C.metering.step-s.<plug>}` seconds… lit value AND its report is newer than the step (a report older than `${C.metering.fresh-within-s.<plug>}` s at the read is VOID)" |
| 3 REP-1 notes | + "(the plug's measured bias, `${C.metering.bias-pct.<plug>}` %, prints beside it as r_corr — recorded, never the verdict's)" |
| CHAR-AFTER | `char_after_readings` → `char_after_*` ×4, the passes in the first prompt |
| 9 asserts | + `fresh_within_s: "${C.metering.fresh-within-s.<plug>}"` · `bias_pct: "${C.metering.bias-pct.<plug>}"` |
| header | + one METER-3 line; FRESHNESS bullet "now also asserted" |
Resolved: G4-1 "15 seconds … 30 s"; TR3 "90 … 180".

## §4 The tests (test_engine.py)
- Imports `time`, `Decimal` (:33–34). **M3 T1** :1589 (live path, `record`, OPERATOR): fresh 2 s → WITHIN + `bias_pct 2.3` + `corrected_ratio`; stale 152.6 s via `${C.metering.fresh-within-s.g4-2}` → VOID with reason, ratio 1.001250 kept on the REP line, the close names `positive[1] fixed VOID (stale witness: …)`; no key + 600 s → WITHIN, NONE of the new receipt keys. **M3 T2** :1653: lint refuses −5 / "thirty" / bias "x" / `fresh_within:`; `fail` mode FAILs now (line 2 unread); no witness + key → VOID "no numeric data.lastReported"; edge 30.0 fresh, 30.1 stale; `apply_bias(43.7/40.8, 8.0)` → 0.991739; bias −100 refused.
- **T3** pins: keyboard 22 → 29 (`2.2 0.3 -0.1 0.1` first, `2.3 0.3 -0.1 0.1` last, "20" gone); witnesses `1789800000.0 + 60·i` → `time.time() − 3 + i`; the three maps pinned in memory (METER-2's rule); `lets`/`typed`/`resolved.let` 22 → 29; `char_after_readings == 20.0` → the four signed values; per receipt `fresh_within_s`, `witness_age_s ≤ 30`, no `reason`, `bias_pct`, `corrected_ratio` recomputed; REP lines end `· bias=… % r_corr=`. Verdicts unchanged: 6 WITHIN, OUTSIDE, WITHIN, WITHIN.
- **T4**: `want` 22 → 29; per assert the two references; CHAR entries no `min:`, "subtract"/"Type" present; REP prompts carry `step-s`, "newer than the step", `fresh-within-s`; no `confirm` on the act; the REAL constants = the mint + 3 provenance rows.

## §5 Deviations
1. §0 "two new keys" vs §1.3's `${C.metering.step-s.<plug>}` — a third map (§1.3 controls). 2. §0 scopes engine.py to "the VOID path"; §1.5's bias on the REP line/receipt needs the engine — the optional `bias_pct` key. 3. A missing/non-numeric witness WITH the key set → VOID ("never a pass by absence"); the charter names only `age > window` — one word flips it. 4. The stale VOID's REP line keeps the ratio and names the reason; `recorded_close` prints the reason — §3's "VOID's reason string" latitude. 5. M3 T1's first run failed on MY assert string (`% r` = a `%r` conversion) — `meter3_tests_fix1.py`; the engine was right. 6. `meter3_scenario.py`'s first run stopped at its own guard (my comments said `confirm: enter` twice); nothing written; reworded. 7. §2.4's fork: T3 carries fresh witnesses; stale→VOID proven in M3 T1 (same live route). 8. Constants comment says "G4-2's first read 2.94" (152.6 s old at the bytes), not "one fresh rep"; the number is the charter's. 9. Three METER-3 notes in the scenario's header comments.

## §6 Not re-executed
Nothing on the Pi; no live run; boot-health not run against a boot (lint + selftest only); nightly.sh untouched; the b5 audit's "≈ 66 s idle" and the 5-s store cadence copied from the charter; core `ZigbeeIntegrationAdapter.java:922` grep-read at `e96dce8`; the 40-W bands untouched.

RETURNED nexsys-hivemind/context/audits/2026-09-27_METER-3_return.md 8143
