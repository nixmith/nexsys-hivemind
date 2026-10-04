<!--
file: context/audits/2026-10-03_VERIFY-72H-B_plan.md
purpose: VERIFY-72H-B's PLAN (W9): rows re-run, forks settled, Files census, red-first tests, risks. STOPS at PLAN-RETURNED.
lane: Nick's desk · 2026-10-03T23:17:45Z (18:17 CT) · nexsys-bench 0232c69, porcelain 0 → branch v72b/action-effect-link-a1-loads · core cites at 5b0e20c via `git show` (tree at df2bc62 = J1)
-->
# VERIFY-72H-B — PLAN

## §0 the premise rows (✓ = holds at the pin)
1 ✓ `AutomationCompletedEvent(Ulid runId, String finalStatus, long durationMs, int actionCount, int commandCount, String failureReason, String abortReason)` :54–:62.
2 ✓ SRM :481 `= 0`, :491 `= result.actionCount()`, :702 `terminal.name(), durationMs, actionCount, commandCount`. The builder `StandardActionExecutor.execute` :172–:206: `actionCount++` :190 BEFORE `applyAction` :192 (`issued++` :259) → actions STARTED (= executed on a COMPLETED run; a failed one counts too, :202).
3 ✓ `build_runs` :383; run rows :518–:525 carry no payload → (viii) reads `runs` (:462). LINKABLE: the run's correlation = `triggeringEvent.causalContext().correlationId()` (SRM :218; published :693/:705); every command it issues carries the same (`CausalContext.chain(…)`, StandardActionExecutor :405–:407) → `c.correlation == triggered["correlation_id"]`.
4 ✓ `zigbee.link_summary: device={} frames={} last_lqi={} last_rssi_dbm={} last_link_at={}` A:654–:657; `NO_LINK_READING = "-"` A:200; `Instant::toString` :674; `LINK_SUMMARY_PERIOD` 10 min SAT:79. The wire: `last_link_at=2026-09-28T17:19:02.807726985Z` — NINE fractional digits; py3.10 `fromisoformat` rejects >6 → truncate; dark → `-`.
5 ✓ WARN `permit_join_key_ignored: configured={}s …` A:921; INFO `permit_join_opened: duration={}s reason={} actor={}` A:964; grader :193's `:922` → `:964`.
6 ✓ A1 :750–:757 as charted; README :72. 7 ✓ `soak_numbers` :664–:720 (the log loop :691–:704 keys `parse_iso(line["ts"])`); table :925–:933. 8 ✓ CLI :381–:396; `run()` validates :400–:417 BEFORE `mkdir` :422; `window.json` :432–:447.
9 ✓ :76–:78 OUTCOME_WORDS = DISPATCHED CONFIRMED UNCONFIRMED FAILED SKIPPED; VERDICT_WORDS = PASS FAIL FLAGGED CANNOT-GRADE NOT-APPLICABLE; `order` :617; fold :620–:629; `detail` :892–:907; "seven" :890/:3. README :34 "the invariants FROZEN at the plan §16 (4)": (viii) is ADDITIVE — the seven untouched, an eighth row, no new word.
10 ✓ runner :7; 25 `@check_fn`. BASELINE GREEN `verify72h selftest: 26 check(s), 0 failure(s)`; `bench.sh selftest: 27 check(s), 0 failure(s)`.
12 ✓ claim / ✗ guess: `terminal.name()` :702; `enum RunStatus` (RunStatus.java:20) = EVALUATING RUNNING COMPLETED(:42) FAILED ABORTED CONDITION_NOT_MET INTERRUPTED — NO `SUCCEEDED`; SRM :500 `terminal = RunStatus.COMPLETED`; the wire agrees (rehearsal-1, ×4). SUCCESS = `"COMPLETED"`; the fixture's `SUCCEEDED` (:646/:1477/:1535) is never on the wire → [REVIEW], corrected.
13 ✓ `PERMIT_JOIN_OPENED` :306, `_CLOSED` :312; published A:961 (open), A:1007/A:1016 (close; not A:1033); grader `permit_join` ×3; neither whitelisted → (iv) CANNOT-GRADE today.
11 `_scratch`: none. FOUND `../_archive/runs/2026-09-28_rehearsal-1/` = EXPORT-1 FULL: 6,953 events; 183 log lines (72 `link_summary`, 0 `availability_link`, 0 `permit_join`); 4 runs COMPLETED ac 9 cc 0 — each 5 CommandAction + 4 DelayAction, all `success`; 0 commands by correlation. Re-grade YES on a copy (§6); PRE-REGISTERED 4× FLAGGED, layer FLAGGED, exit 2.

## §1 the forks, settled
- F1 → (a) `A1a` + `A1b` flat; pins moving :1194–:1195, :1199–:1201, :1224, :1264. A1b = `declared` (window.json, default 0) · `observed` = `permit_join_opened` EVENTS · `events` ids · `lines` file:line · PASS iff observed == declared. A1-2…A1-7's fixtures carry the event AND its INFO line (A:961/:964); a line without an event (T9a's old shape) → a `lines_without_events` note, never a verdict.
- F2 → (a) `--loads <path>`; validated in `run()` before mkdir (ExportError → `export refused`, exit 2); `--declared-windows` as text → int ≥ 0 the `--log-utc-offset` way.
- (viii): SUCCESS = `COMPLETED`; FLAG text "completed with actions and no command"; `issued` = the commands carrying the run's correlation (`triggered is None` → null); per run `actions` = Counter of `action_type` over `automation_action_started` by payload `run_id` ("which actions"); CANNOT-GRADE never; `final_status` under its own key, no `outcome` key in the rows (the walker :646).
- (iv): both permit_join types appended to `AMBIENT_WHITELIST` (`# PJ-2 @ 5b0e20c — a named deviation from e96dce8`).

## §2 Files (6 rows = §3's) — the census at 0232c69
1 M grader.py — docstring :3/:55–:58; constants + `parse_link_at()` at :190–:193 (`:922`→`:964`); whitelist +2 at :164; `action_effect(runs, commands, events)` after :606, `viii` in `order` :617; `attestations(…, declared_windows)` :746 (A1a/A1b for :750–:757); `soak_numbers` +`link_summary_lines`/h + `link_devices`; `grade()` +`verdict["loads"]` after :452; `report_md`: "eight" :890, `detail["viii"]`, the loads block after :883, A1a/A1b rows at :913–:915, the column :926–:933, +2 tables (link per device; action-effect naming each FLAGGED/FAILED run). ≈ +170/−25.
2 M export.py — the two flags at :396; their loaders; `run()` :417; `window` :432 +2 keys. ≈ +45.
3 M test_verify72h.py — `completed(…, status="COMPLETED", actions=1, commands=1)` :646; :1477/:1535 → `COMPLETED`; the clean fixture `c2 = ex.issued(t2, "turn_on", corr=600)` :757 (the run owns c2; T8a untouched); :345/:776–:778 `last_link_at` → ISO; T9a–c pins; +16 checks. ≈ +260/−12.
4 M README.md — :3/:34 eight + the note; a (viii) row after :46; :46 the column/table; :29 +2 keys; :32 the flags; :72 → A1a/A1b rows (its "NOT an event type at e96dce8" is stale); :43 the deviation. ≈ +14/−4.
5 A this plan · 6 A the return.

## §3 tests first (the red predicted at 0232c69)
V1–V4 `KeyError: 'viii'` (V2 corr-linked, cc 1 → PASS; V3 cc 2, 1 issued → FAIL; V4 `FAILED`, cc 0 → PASS) · V5 (layer FLAGGED, exit 2) `AssertionError: ('PASS', 0)` · L1 (3 lines, 2 devices, 2 h; min LQI/RSSI; a 9-digit ISO `last_link_at`; age vs `to`) `KeyError: 'link_summary_lines'` · L2 (`-` → null, "never") `KeyError: 'link_devices'` · A1-1…A1-7 `KeyError: 'A1a'`/`'A1b'` (A1-7 also (iv) CANNOT-GRADE) · X1–X3: argparse rejects `--loads` → `SystemExit(2)`, escaping the runner's `except Exception` — the X checks catch it, raising `AssertionError("--loads is not a flag")` · R1 `AssertionError: 'The loads (declared)' not in report`. The moved pins land in the same red commit; T7b's `>= 12` grows (~+9 `say()` sites).

## §4 risks · pushback
- R1 [REVIEW] `SUCCEEDED` was never on the wire; a (viii) keyed on it would flag nothing real → `COMPLETED`.
- R2 [REVIEW] the clean fixture's run completes `cc 1` owning no command → under (viii) T7b/T8c/T9b/T9c FAIL; `corr=600` on c2 fixes the shape. T5's run 600 adds a (viii) FAIL beside (ii)'s; asserted.
- R3 a correlation-only link over-counts a cascade (a child run inherits the parent's correlation, SRM :218) → a spurious FAIL. Default = the charter's key (EXPORT-1 unaffected). `GO with: span` adds `triggered.ingest_time ≤ issued_us ≤ terminal.ingest_time` — then the clean run re-times into h0 (T8a :1121/:1125 move).
- R4 `parse_iso` :221 rejects 9 fractional digits → `parse_link_at()` truncates to 6, accepts epoch seconds, `-`/empty → null.
- R5 `attestations()` gains `declared_windows`; no test calls it directly. R6 [INFO] `constants.yaml:493` `whitelist-home` names e96dce8 — not in the Files table; untouched. R7 "The three attestations" → "The attestations (A1a · A1b · A2 · A3)"; no test pins the prose. R8 core HEAD df2bc62 ≠ 5b0e20c; every cite read at the pin; only the adapter moved (+21/+49, formats identical).

## §5 the return cap
3 KB + 1 KB × 6 Files rows = 9,216 B (a ceiling); the re-grade diff (§6) in the return's §4, trimmed to the (viii)/A1/link rows.

PLAN-RETURNED ../nexsys-hivemind/context/audits/2026-10-03_VERIFY-72H-B_plan.md 8177
