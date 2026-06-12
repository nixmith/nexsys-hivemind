<!--
file: context/handoff/2026-06-12_W0_R14-briefs_session_prompt.md
purpose: Next-PM-session brief — W0 Research-4 currency delta + author the three R14/R15 research briefs + M7/M8 charter skeleton. Carries a PINNED STATE block so the session spends its window on brief precision, not state re-derivation.
audience: PM (next Cowork session), Nick
status: READY — authored 2026-06-11 EOD at the M6.2 closeout (PM). Everything below is committed (core `7c73c91`, hivemind `d161ca9`) except this file itself.
-->

# Session Brief — W0 Currency Delta → R14/R15 Brief Authoring → M7/M8 Charter Skeleton

PM session (nexsys-project-manager skill). **Read `context/process/cowork-environment-model.md` FIRST** — it carries the mount-lag/write-collision rules this prompt's predecessors paid for. Then run the freshness preflight against the PINNED STATE below as the answer key — one verification glance per check; investigate only divergent lines.

## PINNED STATE (verified 2026-06-11 EOD at the M6.2 closeout — trust, then spot-verify)

- **homesynapse-core:** HEAD **`7c73c91`** = M6.2 COMPLETE (on `62a81e6` M6.4 / `7e0bce8` docs-only / `9035110` M6.1a / `b7bc65c` M6.1b). Full `./gradlew check` GREEN (147 tasks, ZERO gate-fix rounds). `projectionVersion` **5**. Event pins **55 / 24 / 36** (M6.2 changed none). **No open deferred build gates.**
- **M6 state:** M6.1 ✅ · M6.4 ✅ · M6.2 ✅ (all committed + reconciled) · **M6.3 triple-gated — do NOT issue** (OQ-15-2 microbench + AMD-86 §3 interview signal + OR-M6-NONCE; Nick-paced; W25 Lane 2 calendar-bounds them). **M6.3 instruction carry pins live in the backlog M6.3 row** (IV/nonce fence; never-reuse versions; HKDF zero-salt → pin in the Doc-15-touching amendment; R-1 posture; PersistenceFactory = the wiring step).
- **nexsys-hivemind:** committed **`d161ca9`** (M6.2 closeout + hygiene pass + R14/R15 architecture + W25 charter). Only untracked file should be THIS prompt. **Step-0 at session start:** archive the consumed `2026-06-11_M6.2-return_W25-charter_session_prompt.md` → `handoff/archive/`; if the rollover (Jun 14/15) has passed, flip W24 → COMPLETE (scorecard skeleton is in the W25 charter §W24-scorecard-input) and W25 → IN_PROGRESS.
- **Check 9:** STALE expected — ONE file (`project-manager/references/coding-instruction-format.md`, now incl. the 2026-06-11 additions: internal-consumer survey, table-governs, minimum read set, verbatim vectors, §4c caveat) until Nick's mirror sync. CONFLICTED is abnormal.
- **Research state:** high-water **REC-140** (Research 13). Reserved ranges: **R14-A 141–155 · R14-B 156–170 · R15 171–185**. Architecture: `context/planning/2026-06-11_M7-blueprint_research-architecture.md` (PROPOSED — Nick veto-or-default at dispatch) + the research-agenda addendum. **FUTURE-AMD queue:** REC-136; REC-138/§12.4 + tag-preserving YAML emitter (one family per the M6.2 Coder rec). **Open questions:** the NO_DIRECT_TIME_ACCESS-reach OQ (2026-06-11) — do NOT fold into M6.3; instructions must not assert the rule reaches non-app test code.

## TASK (recommended order)

1. **W0 — Research-4 currency delta** (PM-internal; precedes brief authoring). Re-anchor REC-31..40 dispositions against source at `7c73c91`: REC-39 (HIGH-risk automation event schema) vs the post-AMD-52 typed-payload + 55/24/36 pin discipline + the publish-count-pin survey category; REC-36 vs current `RunContext`; REC-31/34/35 permit arithmetic vs the actual sealed permits. Refresh the DQ-1/2/3/5 escalation list for Nick (they gate the M7 AMD block, not the dispatch). Fold B2 C8 (`actorRef` stamps `AutomationId`) as an M7 contract dependency. Output: a compact delta note (assessments/ or a planning note) the briefs and charter cite.
2. **Author the three briefs** per the architecture doc + the NEW format-skill additions. Each self-contained: §0 quote-back gate; verbatim `core/automation` `module-info.java` at `7c73c91`; MODULE_CONTEXT inventory summary; the Doc 07 § anchors scoped per register; minimum read set stated; REC range + mandatory disposition table; guardrails (Locked ground gap-relative only; no M6.3 creep; R15 cannot mint code obligations). Self-review ×3 via `references/review-and-quality.md`. Dispatch: R14-A/R14-B → DOCS Project (web search required); R15 → generic deep research permitted for evidence, disposition pass in-Project.
3. **M7/M8 charter skeleton** (P1 multi-piece — expect ≥3 first-class M7.x rows visible at scoping: trigger/condition path, action/dispatch path, ledger). Dependencies row: M7 AMD block (post-returns), B2 C8 RATIFIED, M6 wrap state, the W25 Lane-4 structural gate (no new Core instruction until M5-C Increment 1 is DONE).
4. Standard closeout: WUCP drift check, handoffs, commit message handed over (use `git commit -F` if the message contains `!`).

## TOKEN DISCIPLINE

Do not re-derive M6 history, the sha chain, or the hygiene-pass record — pinned above and in pm-handoff. High-value reads: the architecture doc (the spec for everything here), `context/assessments/2026-05-22_Research_4_PM_Assessment.md`, `core/automation/MODULE_CONTEXT.md` (top-loaded — JPMS block + inventory) + its `module-info.java`, `instructions/archive/Research_13_Config_System_Market_Superiority_Brief.md` (pattern reference only), `context/process/cowork-environment-model.md` (first). The briefs are the session's precision items — spend the window there.

## STANDING NICK-PACED ITEMS (surface, don't block on)

**Pi-4 microbench (target Wed Jun 17) + energy/erasure interviews — the M6.3 gates, the M6 critical path** · skill-mirror sync (Check 9, one file) · **M5-C Increment 1 (the W25 Lane-4 structural gate — PM drafts, Nick vetoes content)** · B2 C8/C9 ratification (C8 on the M7 critical path) · R14/R15 dispatch veto-or-default · FUTURE-AMD queue at a quiet governance window.
