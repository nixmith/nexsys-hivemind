<!--
file: context/handoff/2026-06-13_M7-AMD-block_session_prompt.md
purpose: Next-PM-session brief — draft the M7 entry-gate AMD block (6 families) + the bundled DOCS review prompt (block + B2 C8/C9) + strategy-refresh drafts. Carries a PINNED STATE block so the session spends its window on amendment precision, not state re-derivation.
audience: PM (next Cowork session), Nick
status: READY — authored 2026-06-12 EOD at the R14/R15-cycle closeout (PM). Everything below is committed (core `e5ea76f`, docs `ed5cf91`, hivemind `fbf3124`) except this file itself.
-->

# Session Brief — M7 Entry-Gate AMD Block (draft) → Bundled DOCS Review Prompt → Strategy-Refresh Drafts

PM session (nexsys-project-manager skill). **Read `context/process/cowork-environment-model.md` FIRST** — note especially §2's truncated-tail artifact and §4's git index.lock hazard (both paid for 2026-06-12; use `git --no-optional-locks` for read-only VM git, treat host file tools as truth). Then run the freshness preflight against the PINNED STATE below as the answer key — one verification glance per check; investigate only divergent lines.

## PINNED STATE (verified 2026-06-12 EOD at the R14/R15-cycle closeout — trust, then spot-verify)

- **homesynapse-core:** HEAD **`e5ea76f`** (docs-only MODULE_CONTEXT permit-count fix 27→30; substantive HEAD **`7c73c91`** = M6.2). Full `./gradlew check` GREEN (147). `projectionVersion` **5**. Event pins **55 / 24 / 36**. No open deferred build gates. Automation surface frozen; MODULE_CONTEXT current (incl. the count fix).
- **homesynapse-core-docs:** HEAD **`ed5cf91`** (the 3 raw R14/R15 returns archived to `research/returns/2026-06-12_*`). ⚠ Known nit: `ed5cf91` carries the hivemind commit message (Nick-acknowledged); append-only bias → NO history rewrite; log at Step-0 and move on. On-disk amendment watermark **AMD-87**.
- **nexsys-hivemind:** HEAD **`fbf3124`** (R14/R15 cycle closeout). Only untracked file should be THIS prompt. **Step-0:** archive the consumed `2026-06-12_W0_R14-briefs_session_prompt.md` → `handoff/archive/`; reconcile `fbf3124`/`ed5cf91` into the tracker mastheads (the snapshot's reconciled-sha line predates the closeout commit itself); rollover check (Jun 14/15 — if passed: W24 → COMPLETE w/ scorecard, W25 → IN_PROGRESS); verify Nick deleted `.git/index.lock.cleared-by-cowork-2026-06-12` (if present, re-flag).
- **Check 9:** STALE expected — still the ONE file (`project-manager/references/coding-instruction-format.md`) until Nick's mirror sync. CONFLICTED is abnormal.
- **W25 charter:** RE-CHARTERED 2026-06-12 EOD (`weeks/2026-W25_jun15-jun21.md`) — Lane 1 DONE pre-window; Lane 3 re-scoped to AMD-block/review closure; Lane 5 folded into the bundled review; Lane 6 (strategy refresh) NEW; §Weekend-bridge names THIS session as the Sat Jun 13 work. Check-2 answer key: W24 IN_PROGRESS until the Jun 14/15 flip; W25 status reads RE-CHARTERED until then.
- **Research state:** cycle COMPLETE — high-water **REC-185**. **`context/planning/2026-06-12_M7-blueprint_merged-disposition.md` is THE authority** (6 AMD families §2a; per-piece obligations §2b; M8 rows §2c; FUTURE-AMD queue §2d: +166/168/153b; M5-C backlog §2e; strategy drafts §2f; coverage attestations §2g). Assessments: `context/assessments/2026-06-12_Research_14B/14A/15_PM_Assessment.md`. Charter: `context/planning/2026-06-12_M7-M8-charter-skeleton.md` (POPULATED; 5-row entry-gate). **Both R14 runs were DOCS-connector-blind** — Nick to check connector reach before any future research dispatch.
- **M7 entry-gate rows at authoring:** (1) AMD block — content enumerated, NOT drafted (THIS session) · (2) B2 C8/C9 — PROPOSED, review pending (bundle below) · (3) M6.3-vs-M7 ordering — open until W25/W26 w/ Lane-2 evidence (microbench target Wed Jun 17; interviews slipping) · (4) Lane-4 M5-C Increment 1 — not started (§2e backlog ready) · (5) MODULE_CONTEXT/§4c currency — ✓.

## TASK (recommended order)

1. **Step-0** (per PINNED STATE above).
2. **Draft the M7 entry-gate AMD block** — six PROPOSED amendments per merged disposition §2a (F1 triggers / F2 selectors / F3 actions+ConfirmationPolicy / F4 RunCausalChain / F5 event vocabulary / F6 definition-schema posture), the AMD-66..71 pattern (use one of those files as the structural reference). Drafting pins:
   - **Derive next-free AMD numbers from the docs nav-index at drafting** (expect AMD-88+; do NOT trust memory — P2 assign-at-milestone).
   - **F4 formally supersedes AMD-04**; F3 carries the merged 33⊕143⊕144⊕161 content (named default + `confirmation_timeout_ms` key + calibration-spike note); F2's `includedCategories` is BREAKING → construction-site sweep stated; F1 promotions are field-additions (no new switch cases) — say so.
   - **F5 decides type-residency:** PM default = FLATTEN run/status identifiers to event-resident primitives (bare `Ulid`/`String`, the AMD-70 E70-1 precedent) — relocating `RunId` would make an automation-internal ID shared, contrary to its design. State as default for the review to confirm. F5 embeds BOTH module-infos verbatim (automation + event-model at the drafting sha), enumerates the Doc-07 event inventory (incl. `automation_run_skipped`/`run_cancelled` + the F4 cycle diagnostic), and states the per-slice manifest fan-out (55/24/36 → +n) + survey obligation incl. publish-count pins.
   - **C8 is cited as PROPOSED-pending** wherever F5 touches stamping semantics — the bundled review resolves both together; the block must not silently assume C8 ratified.
   - Anti-requirements 151/155/162 appear in the relevant §7s as explicit non-goals.
   - Each family: invariant candidates (AMD-NN-INV-xx), §0 quote-back-able mastheads, Locked-doc anchors. Self-review per `references/review-and-quality.md`.
3. **Author the bundled DOCS review prompt** — the M7 AMD block + **B2 C8/C9 ratification review in ONE dispatch** (PM default per the 2026-06-12 sequencing; Nick veto-or-default — if vetoed, C8/C9 reviews first, block second). Hand R14-A's provenance evidence (Hubitat REC-146 citations) to the C8 half.
4. **Strategy-refresh drafts** (merged disposition §2f, six items + the file-4-vs-file-2 data-monetization reconciliation line) — PM drafts, Nick vetoes content. P2 within the session: defer to the M5-C session if the window runs short (they feed the same copy).
5. *Stretch (Lane-4):* if window remains, start **M5-C Increment 1** content drafts from §2e (config-superiority page + ledger dossier page skeletons).
6. Standard closeout: WUCP drift check, handoffs, commit messages handed over (`git commit -F` if any message contains `!`).

## TOKEN DISCIPLINE

Do not re-read the raw returns (the three assessments carry everything dispositive) or re-derive the research cycle/sha chain — pinned above and in pm-handoff. High-value reads: **the merged disposition (THE spec)**, `context/decisions/2026-06-08_B2_schema_decisions_C8_C9.md` (for the bundle), ONE AMD-66..71 file (pattern), Doc 07 §8.1/§8.2 + `core/automation/MODULE_CONTEXT.md` (exact type shapes for F1–F4), Doc 01 §4.3 + event-model MODULE_CONTEXT (F5 landing site), the W0 delta (§2.5 obligations), `context/process/cowork-environment-model.md` (first). The amendments are the session's precision items — spend the window there.

## STANDING NICK-PACED ITEMS (surface, don't block on)

**Pi-4 microbench (target Wed Jun 17) + energy/erasure interviews — the M6.3 gates AND the row-3 ordering input; a third slip makes the W25/W26 call undecidable** · DOCS-connector reachability check (before any next research dispatch) · M5-C Increment 1 (Lane-4 gate) · skill-mirror sync (Check 9, one file) · delete the stale renamed index.lock (if still present) · FUTURE-AMD queue (REC-136 annotated · 138/§12.4 · tag-preserving emitter · 166 · 168 · 153b) at a quiet governance window.
