<!--
file: context/audits/2026-09-26_METER-2_return.md
purpose: METER-2 lane return — the CHAR scenario's prompts re-cut to the one-cord rig; BM1b T3 made band-independent.
status: RETURNED 2026-09-26T14:07Z (Sat 09:07 CT). Tree at df4a2d7, two files M, nothing committed.
-->

# METER-2 return

## §0 Verdict
- VERDICT: DONE. Both edits landed; the selftest is green; nothing else in the tree moved.
- Selftest before any edit: `selftest: 36 check(s), 1 failure(s)` (BM1b T3; `_scratch/v81/meter2_selftest_before.txt`).
- After the test_engine.py edit alone: `selftest: 36 check(s), 0 failure(s)` (`meter2_selftest_mid_full.txt`).
- After the prompt edits: `selftest: 36 check(s), 0 failure(s)` (`meter2_selftest_after.txt`). Lint: `lint ok`.
- Porcelain: ` M scenarios/metering-known-load.yaml` / ` M tools/runner/test_engine.py`. diff --stat: scenario 41+/39−, test 9+/1−.
- wc -c: scenario 24421 → 25294 (348 → 350 lines); test_engine.py 65629 → 66025.
- Grep on the scenario (post-edit lines; the header shifted +1 after :28, +2 after :76): `80 W` 3 (:16 :26 record; :78 new note); `two 40` 1 (:15 record); `3.03` 2 (:26 :76 record); `4.03` 1 (:76 record); `~20` 1 (:17 record); `photo` 0; `dashboard` 2 (:29 new note "no dashboard toggle"; :40 the format record line, untouched). Nothing below `stimulus:` carries any of them.
- Scratch: `_scratch/v81/meter2_t3_pin.py`, `meter2_recut_a.py` (19 anchors, counts asserted before the write), the selftest outputs.

## §1 The prompt edits (`let:` names, order, types, `min:`, `evidence:` asserts, `requires:` untouched; T4 green)
`<PLUG>` ∈ {G4-1, TR3, G4-2}.

| let / place | old → new |
|---|---|
| CHAR-BEFORE `act` | "Chain wall → A → B1 → B2 → LAMP (three meters in series; no plug). The CHAR chain's T1, its THREE tares: LAMP unplugged, 30 s, then write A, B1 and B2 on the CHAR sheet. LAMP in; after thermal settle (>= 5 min on) take ~20 simultaneous readings of A, B1 and B2 (a photo of the three displays per reading); then press ENTER" → "Pass 1: chain wall → A → cord → B1 → LAMP (A and B1 in series; no plug). Tares: LAMP out of B1 for 30 s, then write A and B1 on the CHAR sheet. LAMP in; two minutes; then three simultaneous readings of A and B1, written as pairs. Pass 2: the same chain with B2 in B1's place — the tares, two minutes, three A/B2 pairs. Re-chain wall → A → cord → LAMP (no meter, no plug) and press ENTER." |
| CHAR-BEFORE `note` | "The load is ${C.metering.load_w} W (the two 40 W lamps)." → "… (one 40 W lamp)." (rest verbatim) |
| `tare_watts_<plug>` prompt ×3 | "Chain wall → A → LAMP (no plug). After 30 s read A's watts → W1, on the sheet. Re-chain wall → A → <PLUG> → LAMP, <PLUG>'s relay ON, wait ≥ 30 s, read A → W2. Type W2 − W1 (<PLUG>'s own draw as A sees it; below A's 0.2 A floor read direct — hence the difference). If negative, type 0 and note the pair on the sheet." → "Chain wall → A → cord → LAMP (no plug). After 30 s read A's watts → W1, on the sheet. Move <PLUG> from its wall socket into the cord's end and the LAMP into <PLUG>: wall → A → cord → <PLUG> → LAMP. Read <PLUG>'s relay at the api in the meter-reader window; if OFF, press its button and read again until `on: true`. Wait 30 s, read A → W2. Type W2 − W1 (<PLUG>'s own draw as A sees it; if negative, type 0 and note the pair on the sheet)." Note unchanged (already the charter's text). |
| `plug_offset_w_<plug>` prompt ×3 | "LAMP OUT of <PLUG>, relay ON; wait until the dashboard's `power_w` for <PLUG> settles (the TR3 up to a minute); type it (DEVICE-SET's OFFSET — expect 0.0). Then LAMP back into <PLUG>." → "LAMP out of <PLUG>, relay ON (as read at the api). Wait until `power_w` for <PLUG> settles in the meter-reader window (the TR3 up to a minute); type it (DEVICE-SET's OFFSET — expect 0.0). Then LAMP back into <PLUG>." |
| `a_volts_*` ×6 | unchanged |
| `a_watts_<plug>_r<n>` prompt ×9 | "THE LOAD STEP: on the dashboard toggle <PLUG>'s relay OFF, wait ≥ 15 s, ON (or unplug the LAMP from <PLUG> for ≥ 15 s and back). WAIT until the dashboard's `power_w` for <PLUG> shows the lit value again (the TR3 up to a minute), then ≥ 5 s more. Read A's watts, type, ENTER — the platform's read follows within 10 s." → "THE LOAD STEP: LAMP out of <PLUG> for at least 15 s, then back in. WAIT until `power_w` for <PLUG> in the meter-reader window shows the lit value again (the TR3 up to a minute), then 5 s more. Read A's watts, type, ENTER — the platform's read follows within 10 s." |
| `a_watts_<plug>_r<n>` goal ×9 | "— band 3.03 %)" → "— band ${C.metering.band_pct} %)" (×6); "— 4.03 %)" → "— ${C.metering.band_pct_tr3} %)" (×3). `engine.substitute` walks every key, so `goal` is substituted: against the live constants the goals render "band 3.65 %" / "3.53 %" (checked). No 3.65 / 3.53 literal in any prompt. |
| `a_watts_<plug>_r<n>` note ×9 (§3.1) | "Rep sheet: A_W and the dashboard's power_w." → "Rep sheet: A_W and the meter-reader window's power_w." |
| `char_after_readings` prompt | "Re-chain wall → A → B1 → B2 → LAMP. The CHAR chain's THREE tares again (LAMP unplugged, 30 s: A, B1, B2 on the CHAR sheet); LAMP in, thermal settle (>= 5 min on), ~20 simultaneous readings of A, B1 and B2 (a photo of the three displays per reading). Then type how many readings the sheet holds" → "Pass 1: wall → A → cord → B1 → LAMP — the tares (LAMP out 30 s: A and B1 on the CHAR sheet); LAMP in; two minutes; three A/B1 pairs. Pass 2: the same with B2. Then type how many pairs the sheet holds from BOTH halves of the bracket (CHAR-BEFORE + CHAR-AFTER; twelve if every reading was taken)." Note unchanged (it held no "~20" wording). |
| `evidence:` comments :244/:278/:312 | "— band 3.03 %); each rep" → "— the constants' band_pct); each rep" (×2); "— 4.03 %); each rep" → "— the constants' band_pct_tr3); each rep" (×1). Text only. |
| header note, one line at :29 | "# METER-2 (2026-09-26): the prompts below are re-cut to the one-cord rig — one 40 W lamp (constants load_w 40, bands 3.65 / 3.53 at df4a2d7), two CHAR passes on one cord, three pairs per pass, two-minute settles, no dashboard toggle; the record above stands as the method's origin." |
| header note, one line at :77 | "# METER-2 (2026-09-26): the bands named above are the 80 W record's; at df4a2d7 the constants carry band_pct 3.65 · band_pct_tr3 3.53 for the one 40 W lamp (T4b), and the prompts below read them as ${C.metering.band_pct} / ${C.metering.band_pct_tr3}, never as literals." |

## §2 The T3 change (`t_bm1b_real_file_walk`, after the plug-id loop, before `unmet_requirements`)
```
    # METER-2 (2026-09-26): the charter's bands pinned in memory — a
    # constants re-mint (T4b: 3.65 / 3.53 at 40 W) must never flip this
    # walk; the live bands are the live scenario's business, not this
    # test's.
    constants["metering"]["band_pct"] = 3.03
    constants["metering"]["band_pct_tr3"] = 4.03
    constants["metering"]["load_w"] = 80
```
check_fn string: "(ids and flags overridden in memory, " → "(ids, flags and the charter's bands " "overridden in memory, ". T3 reads the bands only through `engine.substitute(scenario, constants, {}, defer_lets=True)` on the overridden dict (no other `band_pct` in its path). The walk now prints "3.755 % vs 4.03 % → WITHIN" (TR3 r1) and "4.472 % vs 3.03 % → OUTSIDE" (G4-2 r1).

## §3 Deviations
1. The nine REP `note` strings changed (table row): §2(e) names prompt and goal only, but the note prints at the same prompt and §1 says there is no dashboard. Revert = one replace of 9 occurrences.
2. The T3 comment is one comment over four physical lines (79-column file). The header notes are one physical line each.
3. A second scratch script (`meter2_t3_pin.py`) for the test edit.
4. CHAR-AFTER's note unchanged: no "~20" wording to replace.

## §4 Not re-executed
No scenario run against the Pi; no `bench.sh`; no add, commit or push; `constants.yaml` read only at :155–:200; no token.
RETURNED nexsys-hivemind/context/audits/2026-09-26_METER-2_return.md 8149
