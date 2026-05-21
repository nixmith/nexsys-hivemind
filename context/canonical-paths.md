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

## Inter-agent message kinds (see §Message Protocol in CLAUDE.md files)
- [OPEN-QUESTION], [VERIFY-NEEDED] → `context/open-questions.md`
- [DECISION-REQUESTED], [SCOPE-CHANGE-PROPOSED] → `cross-agent-notes.md`
- [FORESIGHT-NOTE] → `coder-handoff.md §Foresight Notes`

## Directories that NO LONGER EXIST (catch stale references)
- `context/queue/`, `context/queue/briefs/`, `context/queue/instructions/` (removed 2026-04-11 — task instructions flow via direct conversation and `coder-handoff.md`)
- `hivemind/` (legacy agent directory, removed 2026-04-11)
- `context/governance/`, `context/design/`, `context/research/` (moved to homesynapse-core-docs, removed 2026-04-11)
- `context/traceability/` for indexes (template only; real indexes live in `homesynapse-core/docs/traceability/`)
