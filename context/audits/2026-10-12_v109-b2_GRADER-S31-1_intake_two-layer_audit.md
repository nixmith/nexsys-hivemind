<!--
file: context/audits/2026-10-12_v109-b2_GRADER-S31-1_intake_two-layer_audit.md
purpose: The hub's two-layer intake of GRADER-S31-1's return (`audits/2026-10-12_GRADER-S31-1_return.md`, 7,654 B): the claims read, then re-executed at the bytes; the two [REVIEW] items ruled; the findings to the register; the landing card.
audience: the hub · Nick
state-type: intake audit
status: FILED — v109 beat 2 (Mon 2026-10-12 ~13:1x CT; instrument 2026-10-12T18:04:10Z → 18:06:46Z). Verdict: ACCEPT — LANDING-READY; LANDED `ceb08c5` (§6, verified 18:42:08Z).
-->

# GRADER-S31-1 — the intake, two layers

## §0 Verdict
**ACCEPT — LANDING-READY.** Unit A (the cause of a timeout) and Unit B (the catalog) sit on `grader-s31-1/timeout-cause` over `32bac40`: three files staged (+747/−1), zero commits. Every claim the hub could re-execute held at the bytes; both [REVIEW] items are ACCEPTED. The landing card is `_scratch/v109/b2/card_bench_land.txt`, with no rig gate: tonight's dry-run reads the Pi's bench sha and pulls nothing (its packet greps 0 pulls). BP10 = the landing sha, pulled onto the Pi at BC10 beside BP9.

## §1 Layer 1 — the claims, read
- The twelve premise rows re-run by the lane at 17:36Z, all held; they match the hub's own runs (16:5x–17:0xZ).
- RED 57/9 at 17:47:50Z, the nine texts quoted (GS-1…GS-6 and GS-8: no `timeout_causes` block; GS-7: no emitter; GS-9: (iv) CANNOT-GRADE naming `probe_answered`); GREEN 57/0 at 17:50:09Z; ≈ 25 min of the 2-h budget.
- 13 mutants of the rule, each caught; the final test text against `32bac40`'s grader red 9/9.
- §3: two [REVIEW], four [INFO]. §4: F1–F4. §6: the limits disclosed (fixtures only; the block's window by `global_position`, (v)'s by `ingest_time`).

## §2 Layer 2 — re-executed by the hub (18:04–18:07Z, the device shell; `TMPDIR` on `/tmp`, IR-181)
1. **The tree:** HEAD `32bac40` · branch `grader-s31-1/timeout-cause` · staged 3 · unstaged 0 · untracked 0 · no lock. Numstat: `grader.py` +247/−0 · `test_verify72h.py` +475/−0 · `README.md` +25/−1 (the one removed line: the (iv) row at `:43`, re-cut). No existing test line changed.
2. **The four suites on the staged tree:** 57/0 · 42/0 · 54/0 · 27/0. `constants.yaml` md5 `9b0af47b3376`.
3. **§0b row 7 on the staged blob** (`git show :tools/verify72h/grader.py`): prints nothing.
4. **The rule, read at the bytes:** `timeout_causes()` `:814` (the timeout-arm filter: UNCONFIRMED, a timeout, no `unconfirmed` result) and `timeout_row()` `:875` — step 1; the walk back from the issue keeping the FIRST opaque row met and walking on to the first readable row of `a`; the window scan (`state_reported` only, after the issue; inside = before the timeout's position; `late` = the first match after it, then stop); the ladder in the charter's order (opaque before · no prior · bench · not dispatched · matched inside · opaque inside · device). `cause_word()` `:136` is the one emitter: `unattributed` takes exactly one reason of five, `bench`/`device` none.
5. **Unit B** (`:225`–`:232`): the PJ-2/J2 form; its construction sites re-grepped at `176adad`: `ZigbeeIntegrationAdapter.java:2172` (`new ProbeAnsweredEvent`) · `StandardAvailabilityTracker.java:784` (and `:777`).
6. **The hub's own fixtures** (`_scratch/v109/b2/v109b2_layer2_fixtures.py`: the pre-existing `Export` class at `:598`, never the lane's builders; each command on its own subject over `clean_export()`): bench → `bench` · device → `device` · device + a report 12 s after the timeout → `device` with `late` · no prior → `no-prior-value` · a matching report inside the window → `matched-in-window` · not dispatched → `not-dispatched` · the prior read from a `state_confirmed` (turn_off twice) → `bench` · Unit B → (iv) PASS, whitelist 70. **8 of 8 as expected; every case exits 0 with (iv) PASS — the block moves no verdict.**
7. **Trailers:** 0 in the staged diff, 0 in the return.

**Not re-executed (disclosed):** the 13 mutants; GS-8's golden sha256 against a fresh `32bac40` checkout; a real export (none on the desk; SOAK-NIGHT-3 is the first real read).

## §3 Rulings
- **[REVIEW] `matched-in-window` — ACCEPT.** The charter's own §4 sends a case its five steps do not decide to `unattributed` with its reason; a matching report inside the window beside a timeout is exactly that case. It is also the most informative reason of the five: the device DID report, so the question is the core's (the ledger's match against its own timer — a race, or overlapping commands), neither the device's nor the bench's. The closed set holds five reasons from this landing.
- **[REVIEW] `opaque` in two more places — ACCEPT.** An unreadable state row met first walking back may be the prior; an unreadable report inside the window may be the edge. Neither is read as absent (never guessed).
- **[INFO]** the extra keys (`by_reason`, `words`, `prior.kind`, `opaque_event_id`) and `check_causes()` — accepted, inside the one block. GS-8's golden pin — accepted; a fixture or invariant change re-cuts it. A1-8's label "(68)" — IR-182.
- **F2** (the cause is the export's: a change the window does not hold leaves an older reading as the prior) — accepted as the instrument's limit. P-GS1 measures the S31's report rate at SOAK-NIGHT-3; IR-51's runner read is the corroboration.

## §4 To the register
- **IR-180** (status cell): not reproduced — 42/0 on the lane's three runs (the first cold) and on the hub's run with `TMPDIR` on `/tmp`; the likely mechanism is IR-181 (unverified).
- **IR-181** (new): the device VM's `/sessions` volume is full (`df` 0 B free at 18:04Z) and `TMPDIR` points into it; `du` sees ≈ 1.3 MB of it; `/tmp` has 3.8 GB free.
- **IR-182** (new): verify72h text drift — the README's (iv) row never named J2's `join_rejected` deviation (F1); A1-8's label still reads "(68)".

## §5 The landing
`_scratch/v109/b2/card_bench_land.txt` (Nick's hands, Git Bash): sweep the three temp objects; the gates (HEAD `32bac40`, the branch, no lock, 0 trailers, staged 3); commit on the branch; fast-forward `main`; push; the sha; `verify72h selftest: 57 check(s), 0 failure(s)`. The bench has no CI, so the selftest on `main` after the merge is the gate. BC10's card pulls BP9 + BP10 onto the Pi with THE BENCH-PULL BLOCK (arc 59).

## §6 The landing, verified (v109 b2; instrument 2026-10-12T18:42:08Z)
Nick's card (13:3x CT): the three temp objects swept (3 → 0); every gate held; `ceb08c5` committed on the branch, `main` fast-forwarded `32bac40..ceb08c5`, pushed. Re-read at the instrument: `main` = `origin/main` = `ceb08c5`; porcelain 0; temp objects 0; no lock; `git fsck --no-dangling` clean; `diff --shortstat 32bac40 ceb08c5` = 3 files, +747/−1 (the return's stat); the landed `grader.py` blob `28f91ce9…` = the staged copy this audit read in §2. The four suites on `main` in the VM: 57/0 · 42/0 · 54/0 · 27/0. The card's last line did not print on the desk: Windows Python wrote cp1252 into the pipe, and a check name holds U+2192 (eight names; seven since before `32bac40`). That is not a test failure; the gate is banked from the VM (disclosed) and the defect is IR-183.
