<!--
file: context/audits/2026-10-03_VERIFY-72H-B_return.md
purpose: VERIFY-72H-B's RETURN — (viii) action-effect · the link_summary column + table · A1a/A1b · the declared loads; LOCAL desk form, plan-first, GO's 8 riders applied.
lane: Nick's desk · plan 23:17Z, GO 00:09Z, return 00:33Z (19:33 CT, 2026-10-03) · nexsys-bench v72b/action-effect-link-a1-loads: 0232c69 → fd43838 (red) → ba846c2 (green) · core cites at 5b0e20c
-->
# VERIFY-72H-B — RETURN

## §0 the card — DELIVERED
- `python3 -B tools/verify72h/test_verify72h.py` → `verify72h selftest: 44 check(s), 0 failure(s)` (was 26/0; +18) · `python3 tools/test_bench_sh.py` → `bench.sh selftest: 27 check(s), 0 failure(s)` · porcelain 0 at `ba846c2`; `git fsck` clean; no trailer in either commit (grep 0).
- `git --no-optional-locks diff --stat 0232c69..HEAD`: README.md 33 · export.py 77 · grader.py 345 · test_verify72h.py 620 — `4 files changed, 986 insertions(+), 89 deletions(-)`.
- RED at `fd43838` (44 checks, 22 failures): V1–V4 `KeyError: 'viii'` · V5 `AssertionError: ['i', …, 'vii']` · L1 `KeyError: 'link_summary_lines'` · L2 `KeyError: 'link_devices'` · A1-1…A1-6 `KeyError: 'A1a'`/`'A1b'` · A1-7 `AssertionError` (the whitelist) · X1–X3 `AssertionError: export.main raised SystemExit(2) — a flag argparse does not know` (caught; the runner survives) · R1 `KeyError: 'loads'` · the moved pins: T9a `AssertionError: ['A1', 'A2', 'A3']`, T9b/T9c `KeyError: 'A1a'`, A2 R1 `AttributeError: module 'grader' has no attribute 'RUN_SUCCESS'`.
- §0b re-run — the 13 rows as the plan's (✓; core tree df2bc62, cites at 5b0e20c unchanged); the bench anchors moved with the diff (§1).

## §1 what changed (spans at ba846c2)
1. `grader.py` — docstring :3–:10/:61–:74; whitelist +2 :181–:185; `RUN_SUCCESS = "COMPLETED"` + the PJ/action constants :188–:196; the link_summary/permit_join tokens :223–:232 (`:922`→`:964`); `parse_link_at()` :270–:300 (nine digits → six; epoch; `-` → None); `grade()`: `loads`/`declared_windows` :523–:531, `invariants["viii"]` :688, `order` +viii :700; `soak_numbers` :747–:835 (`link_summary_lines`, `link_devices`); `action_effect()` :844–:917 (correlation AND span; `cascade`; `actions` by run_id; never CANNOT-GRADE); A1a/A1b :942–:973; `report_md` :1100–:1200 (loads block, "eight", (vii)/(viii) detail, the attestations table, the column, the link table, the (viii) table).
2. `export.py` — docstring :27–:32; the two flags :401–:409; `load_loads()` :413–:453, `parse_declared_windows()` :456–:467; validated in `run()` BEFORE mkdir :489–:490; the two window keys :515–:516.
3. `test_verify72h.py` — `RUN_COMPLETED`, `EXPORT1_COMPLETED_PAYLOADS` (4 real rows verbatim), `EXPORT1_LINK_SUMMARY_LINES` (2 real lines verbatim) :569–:595; the fixture helpers (`completed(status, actions, commands)`, `action_started`, `join_opened/closed`, `join_line`, `key_line`, `link_summary`; `write()`'s two optional keys) :606–:783; the clean fixture (run 600 at t2−2 s, `c2 … corr=600`, completed t2+1 s; ISO `last_link_at`) :833–:870; T8a 11/3 :1203–:1225; T9a rewritten :1276–:1304; T9b/T9c :1327/:1368; `REAL_PAYLOAD_KEYS["automation_action_started"]` :1472; A2 R1 (c3 in span, `COMPLETED`, the VALUE pin, (viii) PASS) :1513–:1661; the 18 checks :1684–:2085.
4. `README.md` — :3/:6; :29 window.json keys; :32 flags; :34 the additive note; :43 (iv)'s deviation; :46–:47 (vii)/(viii); :69–:73 A1a/A1b (the stale `:922`/"NOT an event type" gone); :80–:82 loads; :88–:93 selftest.

## §2 the tests (18 new; red → green on the desk's Python 3.10.12)
V1 FLAGGED + reason, `actions {CommandAction: 2}` · V2 PASS, issued 1, `cascade` [id] in the report · V3 FAIL "disagrees", layer FAIL exit 2 · V4 `FAILED`/cc 0 → PASS; carried-in → issued null, FLAGGED · V5 the fold (i…viii; layer FLAGGED exit 2) · L1 1/0/2 per hour; device A lines 2, min LQI 200, min RSSI −45, last `…02.807Z` from the real nine-digit line, age 243657.192 s · L2 dark → nulls, "never" · A1-1 A1a FAIL file:line · A1-2 A1b FAIL 1/0, (iv) PASS · A1-3 PASS 1/1 · A1-4 2/1 FAIL · A1-5 0/0 PASS · A1-6 1/2 FAIL · A1-7 both types ambient, `closed_events` 1 · X1 loads verbatim; `[]`/0 written · X2 seven refusals naming the row, no dir · X3 1 → 1; −1/"two" refused · R1 the block, `no loads declared`, the `—` for null watts. Moved: T8a, T9a, T9b, T9c, A2 R1.

## §3 deviations
- D-1 [INFO] the commits: the desk's sandbox shell has no git identity and cannot unlink, so `git commit` stalled on its own leftovers (0-byte `index.lock`/`HEAD.lock`, 5 `tmp_obj_*`) — not the desk's rule. Both commits carry the repo's own author (`Nick Smith <nickdsmith1@gmail.com>`, every prior commit's) via `-c`; the green object was written before its ref lock failed — after Nick's one-click delete grant the stale locks went and the branch was pointed at that object (`update-ref`: parent `fd43838`, tree == the staged index, message identical). `fsck` clean; nothing else deleted.
- D-2 [REVIEW] the fixture's `SUCCEEDED` → `COMPLETED` (:646/:1477/:1535 at 0232c69): `RunStatus` has no SUCCEEDED; the wire (EXPORT-1 ×4) reads `COMPLETED`.
- D-3 [REVIEW] the clean fixture's run owns its command (`corr=600`, in span; re-timed into h0 → T8a 11/3): a run completing `command_count 1` with no correlated command is a shape the store never produces.
- D-4 [REVIEW] `permit_join_opened`/`_closed` in `AMBIENT_WHITELIST` — the named deviation from e96dce8 (README :43); `constants.yaml:493` UNTOUCHED (the hub's line).
- D-5 [REVIEW] the fixtures' `last_link_at` epoch floats → the adapter's ISO form.
- D-6 [INFO] `attestations()` gains `declared_windows=0`; the report's "three attestations" → "The attestations (A1a · A1b · A2 · A3)".
- D-7 [INFO] `REAL_PAYLOAD_KEYS` gains `automation_action_started` (so (viii)'s reads are pinned); the A2 R1 fixture gains c3, the run's command.
- D-8 [INFO] the re-grade copies: `../_scratch/v72b/rehearsal-1-{before,after}/` (+ `grader_0232c69.py`, `report.archived.md`); the archive untouched.

## §4 the re-grade — EXPORT-1 (rehearsal-1; 6,953 events, 183 log lines) on a copy
BEFORE (grader @ 0232c69): `[OK] VERIFY-72H PASS`, exit 0. AFTER (ba846c2): `[!!] VERIFY-72H FLAGGED`, exit 2 — `(viii) FLAGGED — 4 completed run(s); flagged [01M3MKG5…, 01M3MM0Q…, 01M3MMQR…, 01M3MN93…]`; every other row PASS; A1a/A1b PASS (0/0); A2/A3 NOT-APPLICABLE. Report diff (bar the dir): `PASS` → `FLAGGED`; +"no loads declared"; seven → eight; (vi) 11 → 17 words; (vii) +"72 link_summary line(s) over 9 device(s)"; A1 → A1a/A1b; +the column (36 · 36); +the link table, 9 × 8 lines (e.g. `0x00124B002FA8D1C5 | 8 | 248 | -38 | 2026-09-28T18:39:02.843Z | 657.157`; two devices `never`); +"Action-effect (viii) — 4 completed run(s), 4 flagged, 0 failed", each `COMPLETED | CommandAction ×5, DelayAction ×4 | 0 | 0 | — | FLAGGED | completed with actions and no command`. **Adjudicated: 4× FLAGGED, layer FLAGGED, exit 2 — as pre-registered.**

## §5 findings for the register
- F1 the bench pinned `SUCCEEDED` six days; the wire says `COMPLETED` (RunStatus.java:42) — a (viii) keyed on the guess would have flagged nothing. Pin a literal from the enum's file, never from a word.
- F2 `Instant::toString` prints nine fractional digits (59/72 of EXPORT-1's link_summary lines); Python 3.10's `fromisoformat` takes six — a bench parser of a core instant must truncate (`parse_iso` would raise).
- F3 `0xF044D3FFFE1C1E8E`'s eight lines: `last_lqi=188 last_rssi_dbm=-53 last_link_at=2026-09-28T11:58:07Z` ×4, then `-` ×4 — the tracker DROPPED a last-link reading mid-window; `0x00178801101A09BB` dark all window. J1/IR-118's domain; the table shows the LAST line by design.
- F4 the charter's close cite is A:1007/A:1016 (not A:1033); EXPORT-1's full export lives under `../_archive/runs/`, not `_scratch/` (the corpus copy is verdict/report/window only — not gradeable).

## §6 bench-handoff entry
`2026-10-03 · VERIFY-72H-B (D-v92-29; IR-96; IR-107) · nexsys-bench v72b/action-effect-link-a1-loads fd43838+ba846c2 on 0232c69 · grader (viii) action-effect (COMPLETED + actions + no command → FLAGGED; command_count vs the correlated commands in span → FAIL; cascade listed), (vii) link_summary lines/h + per-device table, A1 → A1a (key_ignored) / A1b (opened EVENTS vs window.json.declared_windows), window.json.loads (export --loads/--declared-windows), permit_join_opened/closed whitelisted (PJ-2 deviation) · selftest 44/0, bench.sh 27/0 · EXPORT-1 re-grade PASS → FLAGGED (4 runs) · landing: squash onto main (IR-101) + BENCH-PULL (IR-76).`

## §7 instrument limits
The desk shell: a no-delete sandbox, no git identity (D-1). The container's Python is 3.13 (fromisoformat takes nine digits there) — every run cited is the desk's 3.10.12. The "before" grader = `git show 0232c69:…grader.py`. Nothing on the Pi; no ssh; core read-only.

## §8 the commit messages
Committed, not staged — `git log -2 --format=%B`; no trailer.

RETURNED ../nexsys-hivemind/context/audits/2026-10-03_VERIFY-72H-B_return.md 9215 ba846c2
