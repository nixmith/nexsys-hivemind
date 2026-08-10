<!-- ⚠⚠ STALE — QUARANTINED 2026-08-10 (v50 beat 6; Nick's cleanup directive). ACTIVELY MISDIRECTING: its "Directories that NO LONGER EXIST" list names context/governance/ and context/research/ as removed — BOTH EXIST AND ARE LOAD-BEARING TODAY — and every post-May directory class (process/, strategy/ + its three program subtrees, pre-verifications/, programs/, instructions/) is missing. Convicted by the W-COHERE audit (context/audits/2026-08-09_WCOHERE_navigation-audit_return.md, gap row 3). Do NOT navigate from this file; use the newest orchestrator prompt → the spine. This file is the natural HOME of the chartered role-indexed truth-map (post-gate) and will be rebuilt as it. Prepend-only banner — nothing below it was edited. -->
<!--
file: context/canonical-paths.md
purpose: Single registry of directory and file-naming conventions. Brief authors reference this before writing path references.
audience: All
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-05-21 against `homesynapse-core` commit `dfb045e`
-->

# Canonical Paths Registry

## Hivemind directories
- Operational state: `context/`
- Status: `context/status/PROJECT_SNAPSHOT.md` (THE current-state hub)
- Handoff: `context/handoff/coder-handoff.md`, `pm-handoff.md`, `cross-agent-notes.md`
- Open questions: `context/open-questions.md`
- Lessons: `context/lessons/{coder,pm,strategic}-lessons.md`
- Planning: `context/planning/{master-release-plan.md, phase-3-milestone-backlog.md, weeks/, months/}`
- Decisions: `context/decisions/phase-3-cross-module-decisions.md`
- Protocols: `context/protocols/work-unit-completion-protocol.md`
- Audits: `context/audits/`
- Archives: `context/handoff/archive/`, `context/lessons/archive/`

## File naming
- Weekly plans: `weeks/YYYY-WNN_monDD-monDD.md` (e.g., `2026-W21_may18-may24.md`)
- Monthly plans: `months/YYYY-MM_month.md` (e.g., `2026-05_may.md`)
- Audits: `audits/YYYY-MM-DD_topic.md`
- Archives: `archive/<source-name>-YYYY-MM.md` (rotate at month boundaries)
- Design docs (homesynapse-core-docs): `design/NN-name.md` for the 14 core docs, `design/YYYY-MM-DD_topic.md` for ad-hoc

## Source repos
- homesynapse-core: `[module-group]/[module-name]/MODULE_CONTEXT.md` (one per module)
- homesynapse-core-docs: `design/`, `governance/`, `foundations/`, `research/`, `archive/`

## Research document placement (RULE, added 2026-06-05 — the Research 6/7v2/12 loose-file lesson)
- **Raw research RETURNS** (the document a Claude Project produces from a brief) → `homesynapse-core-docs/research/returns/YYYY-MM-DD_Research_N_<Short_Title>.md`, committed **verbatim, unedited, at intake** (before or alongside the PM assessment). The docs repo is connected to the DOCS Claude Project, so committed returns stay permanently reachable for fidelity reviews — never leave a return as a loose file outside the repos.
- **PM assessments** → `nexsys-hivemind/context/assessments/YYYY-MM-DD_Research_N_PM_Assessment.md` (unchanged).
- **Research briefs** (PM-authored dispatch prompts) → `nexsys-hivemind/context/instructions/`, archived once consumed (unchanged).
- Any session that receives a research return as an upload/paste MUST include "commit the return to `research/returns/`" in its closeout actions for Nick. (Companion rule: `context/planning/research-agenda.md` §2 "How Findings Feed Back" Step 0.)

## Inter-agent message kinds (see §Message Protocol in CLAUDE.md files)
- [OPEN-QUESTION], [VERIFY-NEEDED] → `context/open-questions.md`
- [DECISION-REQUESTED], [SCOPE-CHANGE-PROPOSED] → `cross-agent-notes.md`
- [FORESIGHT-NOTE] → `coder-handoff.md §Foresight Notes`

## Directories that NO LONGER EXIST (catch stale references)
- `context/queue/`, `context/queue/briefs/`, `context/queue/instructions/` (removed 2026-04-11 — task instructions flow via direct conversation and `coder-handoff.md`)
- `hivemind/` (legacy agent directory, removed 2026-04-11)
- `context/governance/`, `context/design/`, `context/research/` (moved to homesynapse-core-docs, removed 2026-04-11)
- `context/traceability/` for indexes (template only; real indexes live in `homesynapse-core/docs/traceability/`)
