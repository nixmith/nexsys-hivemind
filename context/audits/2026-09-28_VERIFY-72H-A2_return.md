# VERIFY-72H-A2 return — the grader reads the wire's keys (Mon 2026-09-28 13:11Z / 08:11 CT)

## §0 The card
Baseline: nexsys-bench `9fa2382` (main), porcelain 0; before the lane `verify72h selftest: 25 check(s), 0 failure(s)` · `selftest: 41 check(s), 0 failure(s)`; core records read at `1f1d1e0` via `git show` (HEAD 40412f9; all eight unchanged there). No Pi; no git add/commit/push; python 3.10.12.
- **P1 HOLDS on RED, MISSES the count by one** — R1 RED against `9fa2382` naming **7** distinct keys (10 per-type misses + both BC5 lines; §2). The 8th, `expectedValue`, hides behind `:571`'s `and` (attributeKey None → never asked); state_reported's `attributeKey` (:586) behind the skipped expectation branch. After R2 all nine sites are exercised.
- **P2 HOLDS** — `verify72h selftest: 26 check(s), 0 failure(s)` · `selftest: 42 check(s), 0 failure(s)`.
- **P3 MISSES by the unit** — `grep -c '\.get("[a-z]*[A-Z]' grader.py` = **3** LINES: `staleAfter` :780 · `lastReported` :790 AND :802 — exactly the two `/state` keys; no deviation; pinned against a REAL capture (§5.1): unchanged.
- **P4 HOLDS** — porcelain = M engine.py · M test_engine.py · M verify72h/README.md · M grader.py · M test_verify72h.py (5 M, 0 new).

## §1 What changed
- `grader.py` R2 — `:255–:260` command_type / confirmation_timeout_ms (+4 comment lines) · `:347` command_event_id · `:366` command_type (fallback) · `:387` run_id · `:396` run_id / cancelled_run_id · `:524` final_status · `:575–:576` attribute_key / expected_value (the `.get` pair AND the two subscripts) · `:590` attribute_key. `/state` reads :780/:790/:802 untouched (labels: §5.3).
- `test_verify72h.py` — `:19 import inspect` · R3 `:174–:177` + `:599–:664`: 35 lines of payload keys → snake_case; `state_body` `:706–:710` camelCase kept; T7b untouched · R1 `:1315–:1538`: REAL_PAYLOAD_KEYS (8 types; each key `":NN component"`), BC5_PROBE_LINES, REAL_STATE_KEYS, `real()`, the check.
- `engine.py` R4 — `print_rep` `:1673–:1684`: judged_on corrected_ratio ∧ verdict WITHIN/OUTSIDE → `|r_c−1|=<corrected_deviation_pct> % (raw |r−1|=<deviation_pct> %) vs <tol> %`; VOID and unbiased lines byte-identical; the `· bias= r_corr=` tail unchanged · `recorded_close` `:1867–:1870`: `|r_c−1| X % > T % (raw |r−1| Y %)`.
- `test_engine.py` — `:1874–:1917` A2 R4 (108→WITHIN, 96→OUTSIDE, 96 stale→VOID: the REP and close text) · `:1406–:1407`, `:1410–:1411` BM1b T3 re-cut (§3.1).
- `README.md` — `:57–:66` the paragraph.

## §2 The tests
R1 RED against `9fa2382` (26/1), verbatim: `AssertionError: the grader asks for 7 key(s) the wire never carries — command_issued: commandType, confirmationTimeoutMs; command_result: commandType; state_confirmed: attributeKey, commandEventId; command_confirmation_timed_out: commandEventId; automation_triggered: runId; automation_completed: finalStatus, runId; automation_run_cancelled: cancelledRunId; BC5 :30 {"target_entity_ref":"01…: commandType; BC5 :31 {"target_entity_ref":"01…: commandType`. GREEN after R2; R3 re-greens the 25. R4 RED first (42/1: the 108 line printed `|r−1|=8.000 % vs 5 % → WITHIN`), GREEN after the edit; BM1b T3 then RED on its own `3.755 % vs 4.03 % → OUTSIDE` (§3.1). The instrument: `grader.payload_of` swapped for a dict subclass recording every get/[]/in per event_type over one graded export (2 commands, 2 runs); after the fix (i)(ii)(v) PASS, 0 duplicates, c1 CONFIRMED by `payload:commandEventId`, final_status SUCCEEDED/None.

## §3 Deviations
1. **BM1b T3 :1406/:1409 re-cut** — they asserted the raw figure against the band (`3.755 % vs 4.03 % → OUTSIDE`, `4.472 % vs 3.03 %`): deviation 5's residual, pinned by its own test. Now `|r_c−1|=10.884 % (raw |r−1|=3.755 %) vs 4.03 % → OUTSIDE` · `|r_c−1|=7.164 % (raw |r−1|=4.472 %) vs 3.03 %`; raw figures still asserted; tails untouched.
2. BC5's lines are cut at 80 chars → "verbatim" = a prefix parse: `target_entity_ref` the one whole key; `command_t` the cut key, the head of `command_type` alone among the record's.
3. R1 covers eight types: the charter's seven + `command_confirmation_timed_out` (the same `command_event_id` read); the charter's `automation_run_completed` is `automation_completed` (EventTypes :135).
4. R4 prints the judged figure on WITHIN/OUTSIDE only: a stale-witness VOID on a corrected line keeps the raw line (M3b T3 :1636's bytes) — a VOID judged nothing.
5. `:107 NON_NULL`: R1's fixtures omit null components as the wire does; the ⊆ is against each record's full key set.

## §4 The survey as re-run
`grep -n '\.get("' grader.py` → 48 lines, camelCase 12 → 3 (P3). Fixture grep `'"[a-z]\+[A-Z][A-Za-z]*":'` → 39 lines / 38 keys → 4 lines (`:706–:710`, all `state_body`). BC5 :30–:31 read. CHAR capture: 9 `/state` reads, `data` keys = REAL_STATE_KEYS on 9/9. `git diff --stat 1f1d1e0 HEAD` empty for all eight records.

## §5 Findings
1. `/state` is camelCase on the REAL wire (CHAR capture 9/9) though `ApiResponse.java:14`'s Javadoc claims the SNAKE_CASE mapper (the intake audit §2 cites it); no `PropertyNamingStrateg` in rest-api.
2. `EventId`/`Ulid` serialize as plain strings (`PersistenceJacksonModule.java:90/:105`) → `command_event_id` matches `event_id` on a real export.
3. Residual naming, not reads: `matched_by` labels `payload:commandEventId` / `fallback:…+commandType` (grader :349/:367; README; T4b :862) and the docstring :17–:40; touching the labels changes `verdict.json` bytes — hub's call.

## §6 Not re-executed
The Pi; any real export (EXPORT-1); the export verb; VERIFY-72H-B; the vocabulary; the attestations' logic; core files; `bash -n bench.sh`; `suite all --list`.

RETURNED nexsys-hivemind/context/audits/2026-09-28_VERIFY-72H-A2_return.md 5831
