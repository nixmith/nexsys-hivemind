# VERIFY-72H-A return — export · grader · attestations · METER-3b (Sun 2026-09-27 23:26Z / 18:26 CT)

## §0 The card
Baseline: nexsys-bench `58b5b45`, porcelain 0, `selftest: 38 check(s), 0 failure(s)`; core pins read at `e96dce8` via `git show` (HEAD 1f1d1e0). Nothing touched the Pi; no git add/commit/push; no token printed; python 3.10.12.
- **P1 HOLDS** — test_engine.py 38/0 → **41 check(s), 0 failure(s)** (M3b T1–T3 :1741/:1786/:1832; RED first at 41/3).
- **P2 HOLDS** — test_verify72h.py **25 check(s), 0 failure(s)** (RED first: 6/6 → 19/13 → 19/1 before each row's code).
- **P3 HOLDS** — T4a/T4c→(i), T5→(ii), T6a→(iii), T6b/T6c→(v) FLAGGED, T7a→(iv) CANNOT-GRADE, T8b→opaque CANNOT-GRADE, T9a/b/c→A1/A2/A3 with the other two PASS; the clean fixture PASSes with frozen words only (T7b walks verdict.json + ast-scans every `say()`/`outcome()` literal).
- **P4 HOLDS** — T1a 14 rows = the middle hour's 14, window.json counts equal; T3a/T8c MANIFEST digests re-computed equal.
- **P5 HOLDS** — 108 vs 100 at ±5 %, bias 8.0: OUTSIDE → **WITHIN**; `ratio 1.080000` retained, `corrected_ratio 1.000000`, `judged_on corrected_ratio`.
- **P6 HOLDS** — `status --porcelain -uall` = 9: M constants.yaml · M bench.sh · M engine.py · M test_engine.py · ?? corpus/runs/README.md · ?? tools/verify72h/{README.md,export.py,grader.py,test_verify72h.py}.
- Lint `suite all --list` → `listed 13 leg(s) — all load lawfully`; `bash -n` ok.
- `wc -c` before→after: bench.sh 4897→5913 · engine.py 124386→126554 · test_engine.py 79638→88314 · constants.yaml 39784→43910 · new: export.py 20159 · grader.py 45749 · test_verify72h.py 64202 · verify72h/README.md 7999 · corpus/runs/README.md 3608.
- Guarded scripts `_scratch/v83/v72h_*.py` (anchors ==1): baseline + script `cmp`-IDENTICAL to each working file.

## §1 The export (`export.py`; `bench.sh export <label> <from-utc> <to-utc>` → `~/hs-bench/exports/<label>-%Y%m%dT%H%M%SZ/`)
SQL :57 `SELECT global_position, event_id, event_type, schema_version, ingest_time, event_time, subject_ref, subject_type, correlation_id, causation_id, event_category, payload_size, payload, payload_iv, dek_ref FROM events WHERE ingest_time BETWEEN ? AND ? ORDER BY global_position`; store `mode=ro` :171; `ingest_time` = the store's epoch µs (SqliteEventStore:471); BLOB(16) → 26-char Crockford ULID (Ulid.java:61, the payloads' form). `payload` = UTF-8 JSON when `payload_iv IS NULL` and decodes+parses, else `{"opaque": base64}` :139. Files: events.jsonl · app-log.jsonl (date from `bench-%F-%H%M%S.log` + rollover >12 h :254; unstamped lines ride the prior stamp as `continuation`; clock host-local or `--log-utc-offset`) · bundles/<name>/{api-captures.json,verdict.txt} of in-window bundles :308 · window.json (from/to, rows, min/max position, db bytes, tool sha256s) · MANIFEST.txt `<sha256>  <path>` GNU form :348. Refusals exit 2 (T2b).

## §2 The grader (`grader.py`; `bench.sh verify <dir>` → verdict.json + report.md; exit 0 PASS · 2 FAIL/FLAGGED · 3 CANNOT-GRADE)
| inv | rule as code | fixture that fails it | test |
|---|---|---|---|
| (i) | `classify` :280 = StandardExplanationService:943–:1000; terminal = state_confirmed · timed_out · result ∉{acknowledged}; open beyond `EDGE_GRACE_S` 60 or a duplicate kind → FAIL :475/:469; opaque result → CANNOT-GRADE :487 | T4a (6th command, by event_id); T4c ack-only, double confirmed | :785/:867 |
| key | PINNED: every terminal carries the run's correlation (ledger :375/:617/:892/:900/:917) — necessary, not unique; precise = causation==command id (:404/:667, Zigbee :345) · one hop via dispatched (CommandRoutingSubscriber:283) · payload commandEventId; fallback (correlation, subject, commandType, oldest open) = ledger N-6 :673–:680, named in `matched_by` :309–:362 | T4b | :833 |
| (ii) | triggered(runId) → completed(runId) ∨ cancelled(cancelledRunId) :522; skipped = no Run (StandardRunManager :331/:341), counted | T5 | :910 |
| (iii) | confirmed ∧ (failure∨unconfirmed∨timeout) → FAIL :537 | T6a | :933 |
| (iv) | type ∉ CATALOG or unmatched partition row beyond grace → CANNOT-GRADE naming the first :550/:370; `AMBIENT_WHITELIST` :128 = EventTypes@e96dce8 − partition | T7a | :1010 |
| (v) | report on subject+attribute in [issued, terminal] ≠ expectation (own state_confirmed payload, else `EXPECTATIONS`) → FLAGGED :590 | T6b, T6c | :953/:980 |
| (vi) | `say`/`outcome` :85/:92 refuse foreign words; `check_vocabulary` :653 | T7b | :1058 |
| (vii) | per UTC hour: events, payload bytes, log lines, availability_link lines + frames_since_summary Σ; tokens per ZigbeeIntegrationAdapter:1495 :660 | T8a | :1100 |

## §3 The attestations (grader :742–:846)
- **A1** `zigbee.permit_join_opened` lines in app-log.jsonl (+ any event type containing `permit_join`, none at e96dce8); pre-registered 0; FAILS on >0, lines `file:line` (T9a).
- **A2** each 200 `/state` capture joined to the store's last state_reported ≤ read_at: `stale:true` at silence < staleAfter → false stale FAIL; `stale:false` at silence ≥ staleAfter+60 → missed stale FAIL; staleAfter ∉ {1200,7200} reported; `null` → NOT-APPLICABLE, never PASS; availability recorded beside (T9b).
- **A3** each REP receipt: WITHIN/OUTSIDE with `witness_age_s > fresh_within_s` or no witness → FAIL; VOID on stale = rule kept; no `fresh_within_s` = unchecked; none → NOT-APPLICABLE (T9c).

## §4 METER-3b — the ONE decision-site edit
`engine.py` eval_field_within: `state` first decided by field_within_check :1700–:1703; the edit replaced :1712–:1731 (now :1712–:1758; two diff hunks around unchanged `operands`): `apply_bias` (unchanged, the recorder) runs first; a DECIDED within/outside gains `judged_on:"ratio"`; with `bias_pct` set: `corrected=(val_eff/ref_eff)/(1+bias/100)` exact Decimal, `corrected_deviation_pct`, `judged_on:"corrected_ratio"`, state re-decided on the same band, `verdict` updated; THEN `apply_freshness` (unchanged) voids the judged verdict. Evidence quotes raw then judged figures. Unset bias → verdict, REP line, evidence byte-identical (M3b T2). Figures stay 2.3/8.0/2.9; constants :231–:238 re-cut; provenance under `provenance.verify72h`.

## §5 Deviations
1. **BM1b T3 re-cut** (`v72h_test_engine_bm1b.py`, 6 anchors): the real-file walk scripts reads AT the reference while overriding the measured biases — under tolerate TR3 (r_corr 0.891/0.926/0.927 at 4.03 %), G4-2 (0.928/0.967/0.969 at 3.03) and G4-1 r2 (3.34 %) are OUTSIDE. `WALK_VERDICTS` :1317 → `["WITHIN","OUTSIDE","WITHIN"]+["OUTSIDE"]*6`; two REP-tail asserts + docstring moved; raw figures (3.755, 4.472 %) untouched; `judged_on` asserted. A real consequence of the rule: a plug declared 8 % high that reads the reference is judged 7.4 % low.
2. `permit_join_opened` is not an EventTypes constant at e96dce8 (only the log line, ZigbeeIntegrationAdapter:922) → A1 rides app-log.jsonl.
3. Added: `payload_size` to the SELECT ((vii) needs it); bundles' captures copied into the export (A2/A3 offline); `corrected_deviation_pct` beside `judged_on`.
4. `edge-grace-s: 60` (not chartered): open within 60 s of `to` = `edge_open`; orphans within 60 s of `from` = `carried_in`; run terminals with no triggered are carried in (long runs); 0 = strict.
5. Residual, NOT edited (outside the one site): `print_rep` :1660–:1676 and `recorded_close` :1824 print the RAW `|r−1|` on a corrected judgment ("|r−1| 4.000 % > 5 %" beside `r_corr=0.888889`); receipt/evidence carry the judged figures. Hub's call.
6. METER-3b provenance row moved from `provenance.metering` (BM1b T4 pins it to three rows) to `provenance.verify72h` (`v72h_constants_fix.py`; the original script corrected).
7. Grader loads events.jsonl whole — fine for the 4-h rehearsal; grade a 72-h export on the desktop copy.

## §6 Not re-executed
The Pi (live export/verify = EXPORT-1; §7's probe); VERIFY-72H-B; a decrypting export; apply_freshness/apply_bias bodies, nightly, boot-health, scenario files; the S31; any dashboard read.

RETURNED context/audits/2026-09-27_VERIFY-72H-A_return.md 8172
