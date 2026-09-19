<!--
file: context/audits/2026-09-18_BENCH-METER-1_return.md
purpose: BENCH-METER-1's return — the metering scenario, the two additive mechanics, the link-quality skeleton. Desk only.
audience: the hub (intake; the card is cut from §0) · Nick (Thu 09-24)
state-type: lane return
charter: context/instructions/2026-09-18_bench-lane_BENCH-METER-1_metering-known-load_field-within_link-quality-skeleton_charter.md
baseline: nexsys-bench f3631cb, porcelain empty at entry; HEAD unchanged at exit; nothing staged.
-->

# BENCH-METER-1 — bench lane return (Fri 2026-09-18 CT · UTC−5)

## §0 Card
- **DELIVERED, desk only.** `date -u` 21:44:28Z. Bench HEAD `f3631cb` in and out; nothing staged or committed; no hardware, rig, s31 or nightly touched.
- **Census 4 M + 2 A = the Files table:** M `constants.yaml` · `engine.py` · `test_engine.py` · `SCENARIO_FORMAT.md` (§5 +3 bullets, additive); A `metering-known-load.yaml` · `link-quality.yaml` (untracked `??`).
- **I-1 `suite all --list`:** 13 legs, all load lawfully, exit 0 — the 11 of f3631cb + both new, `requires` as chartered.
- **I-2 selftests:** `test_engine.py` RED 31/12 at the old engine → **31 checks, 0 failures**; digest **43/0** (= baseline). Dry run: `SKIPPED: [operator], [metering-plug]`.
- **I-3 git:** porcelain = the six rows; `diff --stat -- scenarios/*.yaml` = `constants.yaml` only.
- **P1 HELD · P2 HELD · P3 HELD, mechanism refined · P4 HELD, instrument blind to untracked rows** (§2).
- **Deviations** (§3): D-1 `plug-entity` is a three-plug map · D-2 URL-safe placeholder · D-3 no `plug_entity` let · D-4 per-plug tares, per-rep entries · D-5 CHAR-AFTER typed at the close · D-6 banner bumped.
- **Hub, before Thu 09-24:** **F-1** mint `capabilities.operator` true with the flip — else the run SKIPs on [operator] · **F-2** rule the ratio: A_W or A_W − TARE · **F-4** provenance rows for the three plug ULIDs.

## §1 The three instruments, as measured (device VM: Python 3.10.12, PyYAML 6.0.3)
**I-1** — `python3 -B tools/runner/runner.py suite all --list`, exit 0:
```
runner BENCH-METER-1-2026-09-18-field-within @ f3631cb
[LOAD] boot-health tier=AUTO requires=-
[LOAD] command-confirm-s31 tier=AUTO requires=command-api
[LOAD] command-confirm tier=AUTO requires=command-api,hue-online
[LOAD] command-identify-honest tier=AUTO requires=command-api
[LOAD] command-s31-settle tier=AUTO requires=command-api
[LOAD] command-supersession tier=AUTO requires=command-api
[LOAD] command-timeout-absent tier=AUTO requires=command-api
[LOAD] link-quality tier=AUTO requires=link-read
[LOAD] metering-known-load tier=OPERATOR requires=operator,metering-plug,command-api
[LOAD] rejoin-race-operator tier=OPERATOR requires=command-api
[LOAD] timeout-honesty-no-change tier=AUTO requires=command-api
[LOAD] usb-reenumeration-manual tier=OPERATOR requires=-
[LOAD] usb-reenumeration tier=AUTO requires=usb-power
listed 13 leg(s) — all load lawfully
```
**I-2** — `python3 -B tools/runner/test_engine.py` (it carries a `__main__`). RED of record, tests first: `selftest: 31 check(s), 12 failure(s)` — T1 ×5 `unknown api assert(s) ['field_within']`; T2 ×3 `let[0]: unknown key(s) ['operator']`; T2+T1 ×2 (field_within refused first); T3 ×2 (files and flags absent); T3's second half `[ok]`, GREEN-BY-CONSTRUCTION. After the engine: `31 check(s), 2 failure(s)` (T3, files not yet written). After the files: **`selftest: 31 check(s), 0 failure(s)`**, exit 0. `nightly_digest.py --selftest`: `selftest: 43 check(s), 0 failure(s)`, exit 0.
**I-3** — lock-free (the final tree, 22:15:50Z; every instrument re-run, unchanged):
```
$ git --no-optional-locks status --porcelain
 M scenarios/SCENARIO_FORMAT.md
 M scenarios/constants.yaml
 M tools/runner/engine.py
 M tools/runner/test_engine.py
?? scenarios/link-quality.yaml
?? scenarios/metering-known-load.yaml
$ git --no-optional-locks diff --stat -- scenarios/*.yaml
 scenarios/constants.yaml | 56 ++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 56 insertions(+)
```
numstat: engine 358/6 (6 lines replaced in place) · test_engine 476/0 · constants 56/0 · format 3/0; `diff --cached` empty.
**The dry run**, `--against bench-logs/2026-07-soak-exit/bench-2026-07-13-214029.log` (a captured app log): `[SKIP] metering-known-load — SKIPPED: [operator], [metering-plug] — capability 'operator' not declared available in constants.yaml; …`, exit 0. Api-only, no log assert: the lint and the gate are its instrument. `link-quality`: `SKIPPED: [link-read]`.
**Beyond the charter (scratch):** the REAL file walked (flags/ids overridden in memory, drivers tripwired, reads and keys scripted): PASS 9/9 in script order, TR3 at 4.03, CHAR-AFTER last; TR3 r1 76.9 vs 80.6 → FAIL there, `4.591 % > tolerance 4.03 %`.

## §2 P1–P4
- **P1 HELD** — 4 M + 2 A; the A rows read `??` because nothing is staged.
- **P2 HELD** — +13 checks (18 → 31); no fix round: the first run after the engine had T1 5/5 and T2 5/5 green, the first after the files 31/0. Disclosed: before any engine edit the RED run was re-cut once, so T2's own red names `operator`, not `field_within`.
- **P3 HELD, mechanism refined** — the listing prints `requires=` (I-1), never availability; the `false` values live in constants. A direct run SKIPs both (the dry runs). The nightly never reaches them: `suite auto --list` still lists its 9 legs, neither new; `suite all` DEFERS metering-known-load (OPERATOR) before its gate.
- **P4 HELD in substance** — no existing scenario YAML changed; the instrument names only `constants.yaml` because git diff never lists untracked files (the porcelain shows both).

## §3 Deviations, design, findings
- **D-1** `metering.plug-entity` is a map (`.g4-1 · .tr3 · .g4-2`): §3's 3 plugs × 3 reps read three devices; one id would read one plug nine times.
- **D-2** Placeholder `UNSET-minted-at-the-first-adoption-Thu-09-24`: with the network stubbed, the charter's `"<UNSET — minted…>"` raises `http.client.InvalidURL` out of `drivers.api_request`, uncaught — a "runner internal error"; the URL-safe one reaches the request, so a pre-mint run FAILs at the read: the charter's own "fails at the api read, honestly".
- **D-3** No `plug_entity` let: §5 binds from `api:`/`other_of:` only; a third form would be a third mechanic (STOP). Paths use `${C.metering.plug-entity.<plug>}`, command-confirm's idiom.
- **D-4** `tare_watts_<plug>` ×3, `a_watts_<plug>_r<n>` ×9: one binding, one value, one receipt; the rep chain's one tare is per plug. TR3 reps use `band_pct_tr3`.
- **D-5** CHAR-AFTER is a typed entry (`char_after_readings`, the sheet's reading count), typed at the close — nothing else can follow an api-only scenario's last read. CHAR-BEFORE is the one stimulus act.
- **D-6** `ENGINE_VERSION` bumped (B2 rider #4); R-5 changed the engine at f3631cb without one — the banner still read B3.1.
- **DESIGN** (the §5 text): entries are typed in `let:` order when a line first reads them, before its `within:` clock, unread ones at the close (ungated acts fire before the evidence; `after:` takes log tokens only). The first numeric read is the datum — OUTSIDE fails at once (re-polling would be a false-PASS channel); absent pends to the deadline. Exact decimal: 77.576 vs 80 at 3.03 % is 3.0300000000000105 in floats. OPERATOR tier only; piped stdin refused. Receipt in `api-captures.json`; `bundles.py` untouched. Skeleton: `field_within` 127.5 ± 100 % = LQI [0, 255] on the S31.
- **F-1** `operator` is not a declared capability; `unmet_requirements` counts it unmet, so the scenario SKIPs on [operator] even after the metering-plug flip (the dry run says so). The flip re-mint must mint `operator` true too, or requires drops it.
- **F-2** As chartered, r = power_w / A_W; the record's DIV row is r = (power_w − OFFSET)/(A_W − TARE) (DEVICE-SET §2 :54). A reads the plug's own draw and the plug's meter does not: a T W tare reads r low by ≈ T/A_W — 1.25 % per watt at 80 W, against a 3.03 % band. Not taken (a format change); the tares are banked, so r is recomputable per bundle. One shape: `reference_less: "${let.tare_watts_<plug>}"`.
- **F-3** Fail-fast: an OUTSIDE rep ends the run; the rest need a fresh run. Continuing past one is a format change — the hub's call.
- **F-4** At the mint, declare the three ULIDs in `provenance:` (SD-A6).
- **F-5** "The three files of §3" (dispatch line) vs six rows: the table governs (§0).
- **Pushback (§5):** the `let:` entry kept — a stimulus-level capture also fires before the evidence; no `tolerance_w` (the band is relative; quantization sits inside the constant); receipt as above.

## §4 Next
LINK-READ's `link-quality.yaml` asserts (its charter names the keys); VERIFY-72H (hub, Thu 09-24). Hivemind: only this file added (the tree already carried the hub's b6 beat, 8 M + 3 `??`).

RETURNED nexsys-hivemind/context/audits/2026-09-18_BENCH-METER-1_return.md 8948
