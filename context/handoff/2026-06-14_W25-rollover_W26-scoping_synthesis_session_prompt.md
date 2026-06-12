<!--
file: context/handoff/2026-06-14_W25-rollover_W26-scoping_synthesis_session_prompt.md
purpose: Next-PM-session brief — THE CONVERGE SESSION: W24→COMPLETE rollover + W25→IN_PROGRESS + W26 scoping + the M6.3-vs-M7 ordering-call DECISION PACKAGE, synthesizing whatever the two diverge lanes (R16 assessment · M5-C Increment 1) have produced by run time. Also the designated governance window (backlog DONE-row compression + advisory queue).
audience: PM (a FRESH Cowork conversation), Nick (rules the ordering call)
status: READY — authored 2026-06-12 at the returns-intake closeout. CALENDAR-BOUND: run Sunday 2026-06-14 evening (the W25 charter's rollover slot) OR after both diverge sessions complete, whichever comes first. Runs correctly even if one or both diverge lanes haven't executed — it synthesizes the ACTUAL state, never assumes lane completion.
-->

# Session Brief — The Converge: W25 Rollover + W26 Scoping + the Ordering-Call Package

PM session (nexsys-project-manager skill). **Read `context/process/cowork-environment-model.md` FIRST**, then the freshness preflight vs the PINNED STATE below. This session's defining job is SYNTHESIS: three parallel lanes may have advanced independently (R16 assessment · M5-C Increment 1 · Nick's interviews) — discover their ACTUAL state from the trackers, never from assumption, and converge everything into one coherent ground for W26.

## PINNED STATE (verified 2026-06-12 at the returns-intake closeout — EXPECT DRIFT, that is the point)

- **SHAs at authoring:** hivemind `d70f8d1` + the returns-intake commit (reconcile the real chain at Step-0 — UP TO THREE further writers may have landed: the R16-assessment session, the M5-C session, Nick edits) · core **`01841ba`** (substantive `7c73c91` — GREEN 147, pins 55/24/36, pv 5; a `scripts/dev/OUTPUT_CONVENTIONS.md` commit MAY exist if the R16 session shipped its gate-free deliverable) · docs `d7ea212` (+ possible R16 raw-return archival commit). Check 9: known one-file STALE acceptable.
- **Ground at authoring:** OQ-15-2 ✅ RESOLVED (set CONFIRMED `[identity, presence_personal]`) · M6.3 1-of-3 (interviews the sole open evidence gate) · M7 rows 1–2+5 ✅, row 3 ⛔ (interview half), row 4 ⛔ (M5-C Increment 1) · R16 returns intake-validated on disk, assessment pending · W24 still IN_PROGRESS (no rollover yet) · W25 chartered, starts Mon Jun 15.
- **Lane-state discovery (Step-0, after preflight):** pm-handoff top record + cross-agent CURRENT POINTER + `ls context/assessments/` (R16 assessment artifacts?) + `ls homesynapse-core/scripts/dev/` (OUTPUT_CONVENTIONS.md?) + the M5-C venue (`homesynapse-core-docs/website/` or as ruled) + W25 Lane-2(b) (interviews scheduled/run?). Record a three-lane state table before any synthesis.

## TASK (strict order)

1. **Step-0:** preflight; reconcile ALL new HEADs + the three-lane state table; archive this prompt when consumed.
2. **W24 → COMPLETE** with the scorecard (the W25 charter's "Landed in one window" + misses block is the seed; add: OQ-15-2 RESOLVED 5 days early + pi4-validation first exercise + the R16 cycle state + whatever the lanes delivered). **W25 → IN_PROGRESS** (it begins Mon Jun 15).
3. **THE ORDERING-CALL DECISION PACKAGE (the session's payload — Nick rules it, the PM assembles it):** the M6.3-vs-M7.1 sequencing decision, ready for one veto-or-default ruling. Assemble: (a) M6.3 readiness — OQ-15-2 set verbatim, the M6.2 carry pins, the cold-start cipher-warmup beat, OR-M6-NONCE co-design scope, interview signal state (if interviews still haven't run, state plainly that row 3 remains undecidable and the package defaults to "M6.3 instruction-authoring waits; M7.1 path depends on row 4"); (b) M7.1 readiness — rows 1–2+5 closed, row-4 state from the M5-C lane, the M7.1 instruction carries already logged (construction-site sweep, C1-interim pin, AMD-93 schema fragment, event slice + survey, FIX-07 wiring); (c) the PM recommendation with explicit reasoning from the assembled evidence. Do NOT author the winning instruction this session — that is the NEXT session, on a fresh window, per discipline.
4. **W26 scoping** (the W25 charter mandates the rollover session scopes it): shape W26 from the actual lane states — the decision tree at authoring: interviews done + row 4 done → "M6.3-or-M7.1 issue week" per the ruling; interviews missing → "M5-C Increment 2 + R16 consequence week + interview push"; in between → blend. Charter it with lanes + done-whens on the W25 pattern.
5. **Governance window (this session is the designated one):** the **backlog DONE-row compression** (76K → target ≤40K; git-object-sourced per environment-model §5, host-verified tails — the queued item deliberately deferred twice) + surface the advisory queue for Nick rulings: the pi4-validation.sh script fix (F1/F3: PI_HOST default→`pi`, BatchMode, tar-pipe fallback — one small core commit), spike-dir `git rm`, DOCS-connector deselection, the optional Pi-4 confirmation run, the FUTURE-AMD queue, the Doc 15 §9/§15.2 currency-note hygiene call (still Nick's).
6. **Synthesis deliverable — the "final state":** the snapshot masthead rewritten to the converged ground (one entry, all three lanes integrated); Current_State refreshed if gate rows moved (spine re-upload flag for Nick); cross-agent CURRENT POINTER = the converged state; the next-session prompt authored for whatever the ordering call selected (M6.3 instruction-authoring session OR M7.1 instruction-authoring session OR the interview-wait blend).
7. **Closeout:** WUCP drift check; handoffs; commit messages handed over (no `!` or use `git commit -F`).

## TOKEN DISCIPLINE

Lane states come from the TRACKERS (pm-handoff tops, cross-agent pointer, W25 masthead, the assessment/disposition artifacts' §summary lines) — do NOT re-read the R16 returns (the assessment carries them), the microbench spec (resolved), or any Locked doc. The backlog compression is the session's bulk-edit risk item — git-object-sourced, asserts-before-writes, host tail verification, per the rules paid for on 2026-06-12.

## STANDING NICK-PACED ITEMS (surface, don't block on)

Energy/erasure interviews (if still open they remain THE bottleneck — say so loudly in the scorecard) · spine re-uploads · R16-A's M5-C-COPY bucket → M5-C Increment 2 · the soak-suite item (never run) · D-1..D-7 vetoes if the M5-C session hasn't consumed them.
