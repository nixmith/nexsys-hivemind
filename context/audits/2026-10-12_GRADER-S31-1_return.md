# GRADER-S31-1 return — a timeout names its cause (device · bench · unattributed); the catalog follows the deploy

## §0 The card — DELIVERED
Lane: `nexsys-bench`, branch `grader-s31-1/timeout-cause` off `32bac40`; core `176adad` read-only (show/grep). Clock: `date -u` 2026-10-12T17:27:55Z (12:27 CT) → branch 17:35:28Z → RED 17:47:50Z → GREEN 17:50:09Z → staged 17:52:36Z (≈ 25 min of 2 h). Porcelain 0 before the first act; zero commits (HEAD `32bac40`); no `.git/*.lock` met.
§0b re-run 17:36:01–:16Z (all twelve hold):
1 `32bac40` · `0` ✓
2 `verify72h selftest: 48 check(s), 0 failure(s)` · `selftest: 42 check(s), 0 failure(s)` (first run) · `selftest: 54 check(s), 0 failure(s)` · `bench.sh selftest: 27 check(s), 0 failure(s)` ✓
3 `120` · `216` · `347` · `384` · `734` ✓
4 `671` · `686` · `688` ✓
5 `749` ✓
6 `0` · `123` · `129` ✓
7 `probe_answered` · `availability_contract_declared` (78 constants) ✓
8 three lines, each `5000L` ✓
9 `:81` `Map.entry(0x0006, new DefaultRow(0x0000, 0x10, 0, 3600, 0)),` ✓
10 `AvailabilityContractDeclaredEvent.java:40` · `ProbeAnsweredEvent.java:45` · `EventCategoryMapping.java:107` · `:109` ✓
11 `176adad has` · `e11ae20 has` · `ba08dd8 has` · `37f05a9 lacks` ✓
12 `9b0af47b3376` ✓
Staged tree (17:53Z): `test_verify72h.py` `verify72h selftest: 57 check(s), 0 failure(s)` · `test_engine.py` `selftest: 42 check(s), 0 failure(s)` · `nightly_digest.py --selftest` `selftest: 54 check(s), 0 failure(s)` · `test_bench_sh.py` `bench.sh selftest: 27 check(s), 0 failure(s)`; md5 `9b0af47b3376`; row 7 on the staged blob prints nothing; staged blobs == worktree.
`diff --cached --stat`: `tools/verify72h/README.md | 26 ++-` · `tools/verify72h/grader.py | 247 +++…` · `tools/verify72h/test_verify72h.py | 475 +++…` · `3 files changed, 747 insertions(+), 1 deletion(-)` (the one: README `:43`).
RED, `verify72h selftest: 57 check(s), 9 failure(s)` (the 48 green): GS-1…GS-6 `AssertionError: verdict.json carries no timeout_causes block — its keys: verdict, vocabulary, window, graded_at, export, loads, opaque, invariants, attestations, commands, runs` · GS-7 `AssertionError: grader.py has no cause_word() emitter / check_causes() walk` · GS-8 `AssertionError: ('clean_export: verdict.json carries no timeout_causes block', […])` · GS-9 `AssertionError: ('(iv)', 'CANNOT-GRADE', [{… 'event_type': 'probe_answered', 'why': 'not in the EventTypes catalog'}])`.

## §1 What changed
- `grader.py` (+247/−0): `:77–:86` docstring, the block ADDITIVE · `:125–:147` `CAUSE_WORDS`, `CAUSE_REASONS`, `cause_word()` (the one refusing emitter) · `:225–:232` Unit B, the third NAMED DEVIATION block · `:754–:755` `verdict["timeout_causes"]` after `runs` · `:774` `check_causes()` after `check_vocabulary()` · `:808–:1004` `timeout_causes()` (the timeout-arm filter, totals), `timeout_row()` (the five steps, the evidence), the walk, `timeout_line()` · `:1492–:1497` report.md's last section, "Timeouts by cause".
- `test_verify72h.py` (+475/−0): `:18–:20` docstring · `:2225–:2696` GS-1…GS-9 and their builders (`s31_timeout`, `t4a_export`, `pinned_form`, `PIN_32BAC40`).
- `README.md` (+25/−1): `:43` (iv)'s AVAIL-API-1 clause · `:69–:92` the cause block.

## §2 The tests (each RED, then GREEN)
GS-1 `bench`: prior on=true, turn_on dispatched, timed out; evidence + totals · GS-2 `device`, late none · GS-3 `device`, late +12 s = the FIRST match · GS-4 prior = the park's `state_confirmed` (`expected_value`, its id); + no row for a timeout beside a failure result, an `unconfirmed` result or a `state_confirmed` (§4's timeout arm) · GS-5 `unattributed` × the four reasons, one fixture each · GS-6 in-window mismatch → `device`, count 1, (v)'s flag byte-same; in-window match → `matched-in-window`; in-window opaque → `opaque` · GS-7 6 stray emits and 2 planted strays refused; no cause word under `verdict`/`outcome`; every `cause_word()` site literal · GS-8 clean + T4a: verdict sha256 == 32bac40's pin (block lifted, `whitelist_size` 70→68; graded_at/dir blanked) · GS-9 the two types → (iv) PASS, 70.
Beyond: the final test text against `32bac40`'s grader (a /tmp copy) → 9/9 GS red; 13 mutants of the rule (bench↔device, last-match late, `value` read off a `state_confirmed`, each step dropped, any-subject prior, every timeout given a cause, Unit B removed, emitter or walk disarmed) each caught.

## §3 Deviations
- [REVIEW] A fifth reason, `matched-in-window`: `device` requires no matching report in the window, and the five steps decide nothing when one is there (the device reported; the ledger timed out anyway — a race, or overlapping commands). Not `device`, no fourth cause: `unattributed` naming it. Struck, the case needs a ruling.
- [REVIEW] `opaque` past step 2's letter: an opaque state row met first walking back counts with NO readable prior behind it too (it may be the prior); an opaque `state_reported` inside the window → `opaque` (step 5's "no matching report" is unreadable).
- [INFO] Extras inside the one block: `by_reason`, `words`, `prior.kind`, `opaque_event_id`; the grader's own `check_causes()` (the block only).
- [INFO] GS-8's pin: a golden sha256 computed here at `32bac40` (Python 3.10.12); `t4a_export()` checked row for row against T4a's own rows. A fixture or invariant change re-cuts it.
- [INFO] `git add` could not unlink `.git/objects/28/tmp_obj_lcLj5G`, `8b/tmp_obj_hU2Q9H`, `d9/tmp_obj_1RbOOK`; not locks; left.
- [INFO] A1-8's name still reads "(68)"; its assertion reads the tuple (70).

## §4 Findings for the register
- F1 README (iv) never named J2's `join_rejected` deviation (in the code since AVAIL-LINE-1).
- F2 The cause is the EXPORT's: a change it does not hold (before the window, or never reported) leaves an older reading as the prior — `device` or `no-prior-value` while the relay may have held ON. P-GS1's rate and IR-51's precondition read corroborate.
- F3 The desk VM's `/sessions` volume is full (0 B) and `TMPDIR` points into it; the suites ran, but a tempfile-heavy one could fail on space, not code.
- F4 IR-180 did not recur: `test_engine.py` 42/0 on all three runs today, the first cold.

## §5 Bench-handoff entry
GRADER-S31-1 (2026-10-12; branch `grader-s31-1/timeout-cause` off `32bac40`, staged, uncommitted): the grader names a CAUSE for every command UNCONFIRMED by the timeout arm — `bench` (the newest reading before the issue already held the commanded value), `device` (dispatched, an edge asked, no matching report in the window) or `unattributed` with its reason — in an ADDITIVE `verdict.json` block, `timeout_causes` (per timeout: prior, dispatch delay, timeout delay and window, result, in-window mismatches, the first LATE report; totals per cause, reason, subject), and a report section, "Timeouts by cause"; no invariant reads it and no verdict word moves (GS-8 pins 32bac40's bytes). AVAIL-API-1's `probe_answered` and `availability_contract_declared` join the AMBIENT whitelist as a third NAMED DEVIATION (70), so (iv) grades windows after BC10. Selftest 57/0. Lands as BP10 at BC10; SOAK-NIGHT-3 reads it.

## §6 Instrument limits
Fixtures only: no real export with a timeout was graded; SOAK-NIGHT-3 is the first real read. Opaque rows are never read as a match. The window is by `global_position`, (v)'s by `ingest_time`. The export alone: no runner `/state` (IR-51/52 are the runner's) and no probe-to-entity map. Scratch lived in the device VM's `/tmp`.
RETURNED ../nexsys-hivemind/context/audits/2026-10-12_GRADER-S31-1_return.md 7654 grader-s31-1/timeout-cause staged=3
