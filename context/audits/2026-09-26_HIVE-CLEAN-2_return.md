<!--
file: context/audits/2026-09-26_HIVE-CLEAN-2_return.md
purpose: HIVE-CLEAN-2's return — run Sun 2026-09-27 (13:58Z) on 8de29cb. Companion: 2026-09-26_HIVE-CLEAN-2_census.tsv (every file touched; every citer of a moved path).
audience: the v82 hub (§3 is its list) · Nick (§4 the card)
state-type: lane return
status: RETURNED — HIVE-CLEAN-2 (2026-09-26). Two verbs; no deletions; no body edits; nothing protected touched.
-->

# HIVE-CLEAN-2 — return

## §0 Census: before (13:58Z) → after
- **Live `context/**/*.md`** 660→590 (70 moved under `archive/`). Classes: `<none>` 41→0 · ARMED 2→0 · v1 5→0 · AUTHORED 10→1 · CHARTERED 10→4 · CURRENT 35→26 · PAUSED 10→2 · DRAFT 4→2 · LIVE 11→8 · EXECUTED 46→18 · FILED 186→222 · HISTORICAL 11→30 · SUPERSEDED 2→5 · DISPATCH-READY 6 (gated).
- **Tracked per live dir (after; +archived):** audits 339 (+12) · strategy 105 · assessments 68 · planning 46 (+35) · instructions 17 (+180) · research 46 · handoff 7 (+264) · programs 15 · decisions 15 · process 14 · pre-verifications 8 (+11). Handoff root 25→7. Instructions 62→17 (12 md + 5 scripts).
- **Disagreements (acted on the measurement):** (1) "nine" texts = 10 files (v76 ×2); "seven" one-offs = 8. (2) R3 After = 7 not 8: three spine files in the root (the snapshot is in `status/`). (3) R4 After = 17 not ≤10 (eight gated 09-26/27 files). (4) "8 DRs live": the v74 DR read `LIVE — v74 CLOSED…` → CLOSED, moved with v75–v79; the v80 DR moved per DELTA (b). (5) R2 measures 76 (CURRENT 35 incl. two CRLF): 40 re-statused · 35 CONFIRMED-LIVE · 1 left — under ≥60: 26 of 35 CURRENT are spine, lessons, process, wayfinding. (6) The two PART… sit in `instructions/`. (7) OPEN mints 11→14. (8) `cross-agent-notes` reads ARCHIVED-WITH-POINTER (left).

## §1 Acts (rows: the TSV; porcelain `-uall` 151 = 81 M + 64 R + 6 RM; `numstat` +87 −46 over 87 files)
- **R1 — 41 `<none>` → inserted:** last frontmatter line 33 · top HTML comment 6 (no frontmatter) · line 2 after a one-line frontmatter 2 (the R-5B operator record; the 08-02 skills return). 40 × `FILED — historical record`; `READ-ME-FIRST.md` → `REFERENCE` (its three pointers hold). Assert `<none>` = 0.
- **R2 — 40 of 76 re-statused, `Was:` kept:** ARMED→EXECUTED 2 (pelton card — the word arrived 08-31; G2 addendum — "CONFORMED v58 b9") · AUTHORED 9 (4 HISTORICAL · 2 SUPERSEDED · A2 return FILED · v61-b2 card, RS10-RS11 prompts EXECUTED) · CHARTERED→EXECUTED 6 (RS5 "NOT DISPATCHED" yet its return RETURNED 08-30; RS6–RS11 returned) · CURRENT→HISTORICAL 9 (7 assessments, 2 audits, all pre-plan) · PAUSED 7 (A1–A5 dispatches → EXECUTED, a return beside each; A1/A5 returns → FILED) · DRAFT 2 (06-12 website rulings → HISTORICAL; 08-10 pelton email → SUPERSEDED, the 08-13 reply) · v1→HISTORICAL 5.
- **LIVE 3 (bold in §1):** MOMENTUM-MAP → SUPERSEDED (uncited); v74 DR → CLOSED; R-4c prompt → FILED. **Also:** BLOCK6 READY → EXECUTED (docs `8262a3c`); the two PART… → EXECUTED (part ii RULED; R-5B CLOSED v77 b6).
- **R3 — 18 `git mv`:** 10 texts → `handoff/archive/dispatch-texts/`; 8 one-offs → `handoff/archive/one-off/` (the matter prompt keeps PAUSED). `ls` root = 7.
- **R4 — 45 `git mv`** (terminal status, dated 08-22…09-21) → `instructions/archive/` (135→180). Live: THURSDAY 3 + scripts 5 + this charter + eight 09-26/27.
- **R5 — 7 `git mv`:** DRs v74–v80 → `planning/archive/decision-records/`. STALE BASELINE ×3 untouched; live DRs: v81 + the v66 synthesis.
- **R6 —** statuses only (assessments 13 · strategy 11 · audits 2).
- **R7 — 15 `mv -n`, `ls`-proved:** 6 trademark files → `legal/NexSys-LLC/trademark/`; root plans ×2 → `_archive/root-plans/`; `Claude outputs/` → `_archive/`; `_scratch/{h3,_transfer,v66,v70,v71,fe-null-1_nm.tgz}` → `_archive/scratch/` (v75–v81, thu0924 stay). Root: `START_HERE.md` + 7 dirs. `START_HERE.md` (read whole) names `nexsys-hivemind/START_HERE.md` as the way in → one HTML-comment line prepended (stable prompt · brief · v82 text); the stale sentence: "read nexsys-hivemind/START_HERE.md — the canonical cold-boot entry point (…)" (that file is CURRENT).

## §2 CONFIRMED-LIVE — the proving line
- CURRENT 26: the 3 spine + 3 lessons (protected) · wayfinding 4 (`canonical-paths`, `strategic-context-map`, `truth-map`, `governance/project-instructions`) · `decisions/phase-3-cross-module-decisions` (a register) · `pre-verifications/README` · `process/*` ×9 + `protocols/*` (CLEAN-1 §0 KEEP LIVE) · `strategy/README` · `Revenue_Model…` (README :28) · `Six_Battlefields…` (:27) · `07-10_acceptance-arc-positioning-notes` (:35 "Standing notes").
- CHARTERED 4: fusion-program lane charters — map :257 "4 lane charters"; undispatched.
- PAUSED 3: `matter-design/00_PROGRAM_STATUS`, `…phase-C_design-charter`, the matter hub prompt — plan :63 "Refuse: … Matter".
- DRAFT 2: `decisions/09-06_B-7…ADR-draft` — plan :156 "the B-7 ADR's first file … owed"; `Substrate_Thesis_v0` — README :20.
- LIVE 8: stable prompt · v82 text · brief · plan · register (protected) · `measurement-record` (v81 b4) · `process/deep-work-window_protocol` · `brand-program/09-02_successor-name_plan-of-record_two-track` (the 07-05 naming files' `superseded-by:` name it).
- LEFT 1: `brand-program/08-02_conditions-to-copy_translation-template` (AUTHORED) — no citer, return or superseder found; v82's call.

## §3 For v82
- **R8:** `OR-NIGHTLY-0902-S31` pm-handoff :87–:96 (:94 "this row closes with it") → into `OR-S31-INTERMITTENT` :78. Saturday-RED: pm-handoff :66 (v80 b2 Order: "pre-registered RED on boot-health (devices=7 vs the constant 6; D-v80-11)") — lifted by T4 + T5 (`a45686f`).
- **R9:** map :195–:196 (`months/`, `weeks/` rows) + :193 (`phase-3-milestone-backlog` **ACTIVE** vs STALE BASELINE) → the map re-cut; `planning/months/archive/2026-03_march.md` still tracked. Moved paths: 51 of 70 basenames cited by 79 live files (166 cites; TSV). Spine citers: `pm-handoff` :70 + the v81 text → v80 DR · `coder-handoff` :8 → IR40-IR44 · `improvement-register` :34 → DUR-1/HASH-1, MEASURE-1 · the plan → DEVICE-SET, ENERGY-READ · `matter-design/*` ×6 → the matter prompt; the rest are records. All resolve by canonical-paths' archive rule.
- **R10:** `homesynapse-core-docs` `7221ddc`, 182 md, porcelain 0: `<none>` 132 · RATIFIED 30 · DRAFT 8 · CURRENT 3 · 11 singletons. `nexsys-bench` `f1c2f9a`: untracked 0 · modified 0.
- **R11:** 14 OPEN mints (`pm-lessons.md` :343–:382: the 11 + THE ACTION IS THE UNIT · RE-SEEN IS ARITHMETIC · A PI TIMESTAMP IS CONVERTED) → W-SKILLS-10: `SKILL.md` §3 · `references/laws-ledger.md` · `references/coding-instruction-format.md` · the FE/coder mirrors.

## §4 The card (N = 153 = 81 M + 70 R + 2 A; renames already staged by `git mv`)
```
cd nexsys-hivemind
git --no-optional-locks add --pathspec-from-file=../_scratch/hygiene/2026-09-26_HIVE-CLEAN-2_stage-paths.txt
git --no-optional-locks diff --cached --name-status | wc -l   # 153
git --no-optional-locks diff --cached --name-status | grep -c '^R'   # 70
git --no-optional-locks status --porcelain -uall | grep -vc '^[MRA]  '   # 0
grep -c 'Co-Authored\|Claude-Session' ../_scratch/hygiene/2026-09-26_hivemind_HIVE-CLEAN-2_commit-msg.txt   # 0
git --no-optional-locks commit -F ../_scratch/hygiene/2026-09-26_hivemind_HIVE-CLEAN-2_commit-msg.txt
git --no-optional-locks push
```
Then `HIVE: LANDED <sha>`.

## §5 Deviations
- The per-file table (87 + 70 + 17) and 166 cites exceed 8 KB → the companion TSV (CLEAN-1's shape). The stamp is the charter's literal `(2026-09-26)`; the run was 2026-09-27.
- `chmod u+w` on one read-only file (`assessments/06-21_explainability-UX…`; filemode false, no mode in the diff). The cite grep ran as one `xargs grep -oHF` pass.
- Beyond the rows' lists, each with `Was:`: BLOCK6, MOMENTUM-MAP, the v74 DR (+moved); the v80 DR moved (DELTA b). Pre-existing `PASTED`/`FILED.`/`LIVE.` spellings left.

RETURNED context/audits/2026-09-26_HIVE-CLEAN-2_return.md 8176 bytes
