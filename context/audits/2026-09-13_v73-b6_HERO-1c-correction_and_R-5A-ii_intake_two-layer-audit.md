<!--
file: context/audits/2026-09-13_v73-b6_HERO-1c-correction_and_R-5A-ii_intake_two-layer-audit.md
purpose: One combined two-layer intake of the two follow-up returns — the HERO-1c AUDIT CORRECTION (its §5, appended to context/audits/2026-09-13_HERO-1c_return.md; the file now 14,157 B) and R-5A-ii (context/audits/2026-09-13_R-5A-ii_return.md, 6,045 B) — and the two landings they release: the web-ui card (frontend CI the gate) and the bench card.
audience: Nick (§0, §3) · the hub (WUCP Phase 2 for HERO-1c and R-5 Part A at their landings)
state-type: audit (filed once)
status: FILED — v73 beat 6, Sun 2026-09-13 ~17:5x CT (instrument 2026-09-13T22:57:38Z)
-->

# The HERO-1c correction and R-5A-ii — intake, two layers each

## §0 Verdicts
**HERO-1c + its correction — ACCEPT; the web-ui card is the act.** 20 M + 3 A, all under `web-ui/dashboard`; `npm run verify` exit 0 on the desk (24 files, 441 tests; 70.1 of 100 KB); the two D2 rows at SPEC `:280`–`:281` byte-identical to the instruction block with `## §8` at `:283`; the primitives default to the app's `ui.*` pair and the four hero mounts pass the `explain.*` rows; the one remaining `help:` literal inside `actionVerdict` is the skipped mode's empty string, by design. **R-5 Part A + ii — ACCEPT; one bench card lands both.** Porcelain 11 (Part A's nine + `tools/nightly.sh` + `tools/runner/runner.py`); the three gates re-run on the device 29/0 · 43/0 · 18/0; `bash -n tools/nightly.sh` passes; the fence checks green.

## §1 Layer one — the claims, read critically
The correction lane worked from the same session as HERO-1c (its baseline check re-derived the 18 M + 3 A tree first), sorted its reds honestly (the devices-page assertion RED at HEAD; the not-recorded pin red only because the key was absent — the same sentence, now keyed, as the instruction anticipated), kept §5 under 2 KB on a second pass, and ended the return with ONE `RETURNED` line. R-5A-ii grounded `--list` at `cmd_suite_list` (`runner.py:211`) and chose `yaml.compose()` so duplicate top-level keys are seen before `safe_load` collapses them; its red-first fixture is the real hazard (a scenario whose later `requires: []` overrode `requires: [harness-plug]` at HEAD); the nightly reads the registry after the post-restore read so an empty registry is never sampled mid-boot; `fleet_numbers()` holds the fail-safe law in one pure function. It flagged one judgement: `/api/v1/entities` is now spelled twice in `nightly.sh` because a constants key would have touched a Part A file outside its table — bounded (a wrong route lands on `unread`), and a row for the next bench WU (IR-10).

## §2 Layer two — the hub's re-executions at the bytes (device, 2026-09-13T22:57:38Z)
1. Core porcelain: 23 rows, all under `web-ui/dashboard/` (20 ` M` + 3 `??`); index empty; HEAD `fed99e8`. SPEC `:280`–`:281` are the D2 keys; `## §8 Accessibility` at `:283`. `feedback.tsx` `label = t('ui.loading')`; `Resource.tsx` carries `labels`; `RunChainView` ×1, `WhyNotView` ×2, `ExplainHubView` ×1 pass them; `'ui.loading'` in the catalog; `awk '/export function actionVerdict/,0' verdicts.ts | grep -c "help: '"` = 1. The return's §5 present; one `RETURNED` line; 14,157 B as stated.
2. Bench porcelain: the eleven paths; index empty; HEAD `1201368`. The gates on the device: `test_harness.py` 29/0 · `--selftest` 43/0 · `test_engine.py` 18/0; `bash -n tools/nightly.sh` ok; `grep -c '/api/v1/entities' tools/nightly.sh` = 2 (the flagged spelling).
3. **Not re-executed, disclosed:** `npm run verify` (no toolchain in the VM) — `frontend.yml` on the push is the gate of record.

## §3 Rulings and the landings
- HERO-1c: the correction ACCEPT as applied; the charter and the correction go EXECUTED at the landing. The web-ui card: `git add -A web-ui/dashboard` (23), the message file `_scratch/v73/2026-09-13_core_HERO-1c_commit-msg.txt`, the push → `CI: <sha> frontend <green|red> check <green|red> bus-soak <green|red>` (the push is also a `bus-soak` sample for the counter — 3/20 on green). HERO-1d (D5's keyless set; IR-8's lint) and FE-114 follow on the web-ui slot.
- R-5 Part A + ii: ACCEPT; the bench card by the eleven explicit paths; the message file `_scratch/v73/2026-09-13_bench_R-5A_commit-msg.txt` → `BENCH: LANDED <sha>`; IR-9 retires on that landing; IR-10 (one spelling for the entities route — a constants key) is the next bench WU's row or Part B's prep. The nightly's first line after the card is the pre-baseline `fleet:` datum; the s31/nightly HANDS-OFF's intent is kept (additive, never a re-grade).
