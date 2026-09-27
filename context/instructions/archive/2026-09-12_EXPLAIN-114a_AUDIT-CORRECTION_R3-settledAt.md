<!--
file: context/instructions/2026-09-12_EXPLAIN-114a_AUDIT-CORRECTION_R3-settledAt.md
purpose: The hub's one correction to EXPLAIN-114a before it lands (arc 30 form: a correction paste-block headed "AUDIT CORRECTION — do not re-run the WU"). The lane's R3 named it: a superseded DISPATCHED action renders `settled: true` with `settledAt: null`. On the v1.1.4 wire that pair is a contradiction a client will trip on, and v1.1.4 freezes at the landing, so it is fixed before the freeze, not after. The invariant: `settledAt != null ⇔ settled`. Everything else in the return is ACCEPTED as delivered (the audit: context/audits/2026-09-12_v71-b5_EXPLAIN-114a_intake_two-layer-audit.md).
audience: the EXPLAIN-114a Coder lane (the same Claude Code session if it still holds; else a fresh one in homesynapse-core on the uncommitted tree) · Nick (§3 is the paste)
state-type: audit correction (a delta on an unlanded return; never a re-run)
status: EXECUTED (v71 beat 6 — the correction returned 23:39Z, automation 229, landed in `5f918c7`; flipped at v72 beat 1, 2026-09-13T00:53:13Z, for Check 12). Was: ISSUE-READY (authored v71 beat 5, Sat 2026-09-12 ~17:4x CT; instrument 2026-09-12T22:36:16Z). Dispatches on Nick's paste. The census stays 13 = 13 M + 0 A (the same files); the return gains a §5. Then Nick's core card.
baseline: homesynapse-core `72efb42` + the lane's 13 uncommitted M (the tree as the return left it; `git status --porcelain | wc -l` = 13).
-->

# AUDIT CORRECTION — EXPLAIN-114a R3: `settledAt` follows `settled` — do not re-run the WU

## §1 The ruling
`RunExplanation.ActionView.settled` (v1.1.2, the Q1b rule) is true for a superseded DISPATCHED action; v1.1.4's `settledAt` is the settling instant. The two must agree on the wire: **`settledAt != null ⇔ settled`.** The superseded `command_result` envelope IS the settling record (the ledger dropped the command at that instant; nothing further arrives), so its instant is the value. Bare and acknowledged DISPATCHED stay provisional and carry neither instant. `confirmedAt` is unchanged (`null` unless CONFIRMED).

## §2 The edits (exact; `core/automation` only; the census stays 13 M)
1. `StandardExplanationService.deriveOutcome` — beside `CommandResultEvent lastResult = null;` add `EventEnvelope lastResultEnv = null;`; in the `case CommandResultEvent p ->` arm, beside `lastResult = p;` add `lastResultEnv = e;`. Replace the final return (the `// DISPATCHED: no classifying event, so no settling instant…` comment and the `return new Outcome(RunExplanation.ActionOutcome.DISPATCHED, null, resultOutcome, null, null);` line) with:
   ```java
   // DISPATCHED: no classifying event. A superseded result settles the Q1b flag (the ledger
   // dropped the command; nothing further arrives), so that envelope's instant is settledAt —
   // settledAt != null ⇔ settled (v1.1.4, the EXPLAIN-114a R3 ruling). A bare or acknowledged
   // DISPATCHED is provisional and carries neither instant.
   boolean settledByResult = resultOutcome != null && !OUTCOME_ACKNOWLEDGED.equals(resultOutcome);
   Instant settledAt = settledByResult ? instantOf(lastResultEnv) : null;
   return new Outcome(RunExplanation.ActionOutcome.DISPATCHED, null, resultOutcome, settledAt, null);
   ```
   (`settledByResult` mirrors `Outcome.settled()`'s predicate for the DISPATCHED branch exactly; on that branch a non-null, non-acknowledged `resultOutcome` can only be `superseded` — failure-class and `unconfirmed` results took the earlier branches.)
2. The `deriveOutcome` javadoc sentence "DISPATCHED has no classifying event and carries neither" → "a superseded DISPATCHED carries the superseding result's instant as `settledAt` (`settledAt != null ⇔ settled`); a bare or acknowledged DISPATCHED carries neither".
3. `StandardExplanationServiceTest` T7 (the `@DisplayName("DISPATCHED carries no settling instant: both null, a superseded DISPATCHED included (T7)")` test): split the assertion — the bare and the acknowledged DISPATCHED: `settledAt` and `confirmedAt` null; the superseded DISPATCHED: `settledAt` equals the superseded `command_result` envelope's instant (eventTime, else ingestTime — the fixture's), `confirmedAt` null. Rename the display name accordingly. Add one assertion over every fixture the class already builds (T7c): `assertThat(action.settledAt() != null).isEqualTo(action.settled())` — the invariant pinned once.
4. `core/automation/MODULE_CONTEXT.md` — the v1.1.4 paragraph's DISPATCHED sentence → the §1 rule.
5. Optional, zero-risk consistency: in `buildTrigger`, `Instant matchedAt = instantOf(triggered);` replaces the inline `eventTime != null ? … : ingestTime` (the helper now exists; one rule, one place). Take it or leave it; say which.

## §3 Nick's paste (into the EXPLAIN-114a Claude Code session if it is still open; else a fresh session in `homesynapse-core` on the same uncommitted tree)
```
AUDIT CORRECTION — do not re-run the WU. Apply ../nexsys-hivemind/context/instructions/2026-09-12_EXPLAIN-114a_AUDIT-CORRECTION_R3-settledAt.md §2 exactly (rows 1–4; row 5 is optional — say which). date -u first. STOP if `git status --porcelain | wc -l` is not 13 or HEAD is not 72efb42. Test first: T7's superseded case red (settledAt null), then green; T7c green. Re-run the gate line verbatim: `./gradlew :core:automation:test :api:rest-api:test :lifecycle:lifecycle:compileJava spotlessCheck --offline` — green. Never run git add, git commit or git push. Append a `## §5 Audit correction (R3)` to ../nexsys-hivemind/context/audits/2026-09-12_EXPLAIN-114a_return.md — the red/green lines with timestamps, the automation test count (228 → 229 or 230), the census still 13 = 13 M — and re-cut its last line to `RETURNED <path> <bytes>` with the new byte count (the NNNN fixed point; the file may pass 12 KB by the §5 alone — say the number).
```
Report back one line: `EXPLAIN: CORRECTED <path> <bytes>` (the return's new last line).
