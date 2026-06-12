<!--
file: context/handoff/2026-06-14_M7-review-fold_session_prompt.md
purpose: Next-PM-session brief — assess the bundled DOCS review return (AMD-88..93 + B2 C8/C9), fold edits, and (on Nick's explicit ratify call) execute the full ratification mechanics so the M7 entry-gate rows 1–2 close. Carries a PINNED STATE block + a rollover conditional + the Cowork-fallback review variant.
audience: PM (next Cowork session), Nick
status: READY — authored 2026-06-13 at the M7-AMD-block session (same conversation, post-spine-regeneration). Valid whenever the review return lands; do not start the fold without the return on disk.
-->

# Session Brief — Bundled Review Return: Assess → Fold → (Nick ratifies) → Mechanics

PM session (nexsys-project-manager skill). **Read `context/process/cowork-environment-model.md` FIRST** (truncated-tail artifact + index.lock hazard both ACTIVE as of 2026-06-13; `git --no-optional-locks` for read-only VM git; host file tools are truth). Then the freshness preflight against the PINNED STATE below — one glance per check, investigate divergence only.

## PINNED STATE (verified 2026-06-13 at the AMD-block session closeout — trust, then spot-verify)

- **homesynapse-core:** HEAD `e5ea76f` (substantive `7c73c91` = M6.2; docs-only count fix on top). GREEN 147. `projectionVersion` 5. Event pins **55 / 24 / 36**. No open deferred gates. Core is NOT touched by this session (documents-only).
- **homesynapse-core-docs:** expect HEAD = Nick's AMD-block commit (the six `design/amendments/AMD-88..93_*.md` files on `ed5cf91`) — reconcile the real sha at Step-0. On-disk watermark **AMD-87** (the block raises it to 93 ONLY at ratification, this session's mechanics). `Architecture_Invariants_v1.md` last touched `539ed48` (152/41 regenerated).
- **nexsys-hivemind:** expect HEAD = Nick's closeout commit (review prompt + strategy drafts + trackers + spine regeneration + both consumed prompts archived). Untracked should be ONLY this prompt (or Nick committed it — either is fine, message-verify). **Step-0:** archive the consumed `2026-06-13_M7-AMD-block_session_prompt.md` if not already in `handoff/archive/`; reconcile shas into mastheads; **rollover conditional: if today ≥ Jun 15 (or Nick says the weekend passed): W24 → COMPLETE + finalize its scorecard (input block already in the W25 file), W25 → IN_PROGRESS**; verify `.git/index.lock.cleared-by-cowork-2026-06-12` deleted (fourth flag if not).
- **Check 9:** STALE expected (the ONE file `project-manager/references/coding-instruction-format.md`) UNLESS Nick ran the mirror sync — then PASS. CONFLICTED is abnormal.
- **THE INPUT THIS SESSION CANNOT START WITHOUT:** the review return at `context/audits/2026-06-DD_AMD-88-93_C8-C9_DOCS_Review_Return.md` (Nick saves it verbatim). If absent: STOP after Step-0, do allowed-under-STALE hygiene only, and tell Nick what's missing.
- **Answer keys for the fold:** the dispatched prompt `context/instructions/2026-06-13_AMD-88-93_C8-C9_Bundled_DOCS_Review_Prompt.md` (the 10 §A adversarial items + every [R*] flag + the §B C8/C9 gates) and each AMD's §9 ratification checklist. The 11 invariant candidates are listed in `project-knowledge/Invariants_Quick_Reference.md` §PENDING.
- **Spine state:** all 5 `project-knowledge/` files regenerated 2026-06-13 (M6 3-of-4 + PROPOSED-block ground). They carry PROPOSED fences that this session FLIPS at ratification — they are an output of this session too.

## TASK (strict order)

1. **Step-0** (per PINNED STATE; includes the rollover conditional).
2. **Assess the return** (the 2026-06-09 AMD-66..71 fold pattern): verify the reviewer re-derived at the right baseline; walk every per-AMD + C8 + C9 verdict; check each §A item 1–10 and every [R*] flag got an explicit ruling; grade the return (A–F headline + discards if any). **Source-verify every proposed edit against `7c73c91`/the AMD text BEFORE folding** (the 2026-06-07 E1 lesson — reviewers miss occurrences; re-derive each edit's full blast radius).
3. **Fold RATIFY-WITH-EDITS deltas** into the six AMD files / the C8-C9 decision record. Folding ≠ ratifying. Any REJECT or contract-changing finding → ESCALATION format to Nick, do not fold around it. Update each AMD's §10 Review Disposition with the verdict + fold record.
4. **STOP — Nick's ratify call.** Present the folded state + a per-item ratify/defer recommendation. Mechanics run ONLY for items Nick explicitly ratifies (the PM never ratifies — skill §6).
5. **Ratification mechanics** (for ratified items; the 2026-06-09 execution pattern):
   - Six AMD mastheads/statuses/checklists → RATIFIED (date); C8/C9 record → RATIFIED.
   - Invariants: register the surviving candidates in `Architecture_Invariants_v1.md` (§42+), **REGENERATE the §17 total from the table** (do not add arithmetic — the 135/34 lesson), same-commit §0.3/§17/§18 touches.
   - Nav-index (docs `00-navigation-index.md`): six rows + preamble; **watermark AMD-87 → 93** (above-watermark block — the ceiling RAISES, unlike AMD-66..71).
   - **AMD-04 SUPERSEDED banner** in `governance/Design_Review_Amendments_v1.md` (per AMD-91 §2.4's element ledger).
   - Doc 07 + Doc 01 currency edits exactly per each AMD §9 checklist (incl. the `automation_invoked` §3.7 row and the `automation_disabled` priority correction per the review's R92-3 ruling); C8 → Doc 01 currency note; C9 → Doc 02 currency note.
   - Trackers: charter entry-gate rows 1–2 → CLOSED; snapshot/pm-handoff/cross-agent/W25; **the 5 spine files** (flip PROPOSED fences → RATIFIED; pending-invariants section → registered §42+; re-derive totals); milestone backlog M7.x rows stay gated on rows 3–4.
6. **Closeout:** WUCP drift check, handoffs, commit messages handed over (`git commit -F` if any message contains `!`). **State plainly in the report: ratification closes entry-gate rows 1–2 ONLY — M7.1 stays blocked on row 3 (the M6.3-vs-M7 ordering call; Lane-2 evidence) and row 4 (M5-C Increment 1, the P6 structural gate). The next forward work after this session is M5-C Increment 1 + Nick's microbench/interviews, NOT an M7.1 instruction.**

## FALLBACK — if the DOCS Project route is unusable (connector/capacity)

Run the review INSIDE Cowork but as a SEPARATE, fresh conversation BEFORE this one — paste the bundled prompt file as the entire instruction, with: no PM skill, no prior-session context, re-derive everything from source, write the return to `context/audits/` in the verdict format the prompt specifies. Independence here is conversational (fresh context, adversarial charter), weaker than the DOCS Project's separate knowledge base — acceptable as fallback, log it as a process deviation in the return masthead. THEN run this fold session on that return. Never review and fold in the same conversation.

## TOKEN DISCIPLINE

Read the RETURN first and fully — it drives everything. Do NOT re-read the six AMDs end-to-end (the PM authored them; read only the sections each edit touches). High-value reads: the return, the dispatched prompt (answer key), `context/decisions/2026-06-08_B2_schema_decisions_C8_C9.md` (§B fold target), the per-AMD §9 checklists, `references/review-and-quality.md` §1 for the assess pass, the 2026-06-09 return (`context/audits/2026-06-09_AMD-66-71_DOCS_Review_Return.md`) ONLY if the fold pattern needs a precedent glance. The §17 regeneration and watermark/nav-index edits are the precision items — spend the window there.

## STANDING NICK-PACED ITEMS (surface, don't block on)

Pi-4 microbench (was targeted Wed Jun 17) + energy/erasure interviews — gates M6.3 AND entry-gate row 3 · **M5-C Increment 1 — entry-gate row 4 + W25 Lane-4; the §2e backlog is ready; a third missed window makes it the single thing blocking M7** · strategy-draft vetoes D-1..D-7 (fold approved items at the M5-C session) · skill-mirror sync (Check 9) · index.lock.cleared deletion · FUTURE-AMD queue (REC-136 annotated · 138/§12.4 · tag-preserving emitter · 166 · 168 · 153b) at a quiet governance window.
