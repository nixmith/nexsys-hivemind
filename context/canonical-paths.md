<!--
file: context/canonical-paths.md
purpose: Single registry of directory and file-naming conventions. Brief authors reference this before writing path references. Role-indexed navigation (where truth lives per role × task) is `context/truth-map.md`; this file carries paths and naming only.
audience: All
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-08-18 (R-11 lane — REBUILT at the same path per the rebuild-or-archive charge; the ⚠ quarantine banner of 2026-08-10 (v50 beat 6, W-COHERE gap row 3) is LIFTED with this rebuild. Directory census re-derived from the live tree at hivemind 45dd100; the wrong "no-longer-exist" entries (context/governance/ · context/research/ — both load-bearing) are corrected; every post-May directory class added. Worktree only; the hub audits, Nick commits.) Prior: 2026-05-21 against `homesynapse-core` commit `dfb045e`
-->

# Canonical Paths Registry

## Hivemind directories (census 2026-08-18 — re-verify with one `ls context/` at use)

- The spine: `context/status/PROJECT_SNAPSHOT.md` + `context/handoff/pm-handoff.md` (hub-only; each carries its own How-to-read line)
- Wayfinding: `context/truth-map.md` (role-indexed) · this file (paths/naming) · `context/strategic-context-map.md` (the full catalog) · `context/process/edit-procedure-register.md` (who writes what + owners)
- Handoff: `context/handoff/` — `coder-handoff.md`, orchestrator prompts (`*_PM-mission-control_v*_orchestrator_session_prompt.md`; superseded → `archive/`), operator packets, `cross-agent-notes.md` (RETIRED 2026-08-18 — pointer stub)
- Instructions/briefs: `context/instructions/` (coding instructions, lane briefs, research briefs; consumed → `archive/`)
- Audits/returns: `context/audits/` (+ `archive/`)
- Assessments: `context/assessments/` · Research returns intake: see the placement RULE below
- Decisions: `context/decisions/` · Rationale index: `context/process/decision-rationale-index.md`
- Process (cold-boot + standing disciplines): `context/process/` (env-model, playbook, truth-hierarchy, working-with-nick, infrastructure-map, this register's sibling files)
- Protocols: `context/protocols/work-unit-completion-protocol.md` (+ `archive/`)
- Planning: `context/planning/` — `phase-3-milestone-backlog.md`, `master-release-plan.md`, `research-agenda.md`, `months/`, `weeks/` (**weekly plans RETIRED** — Nick 2026-08-09; historical only), `archive/`
- Strategy: `context/strategy/` + subtrees `brand-program/` · `counsel-package/` · `fusion-program/` (inventory + read rules: `context/strategy/README.md`)
- Governance: `context/governance/project-instructions.md` (thin front door — EXISTS and is load-bearing)
- Research: `context/research/` (charter inputs + research-lane returns landing in the hivemind — EXISTS and is load-bearing)
- Lessons: `context/lessons/{coder,pm,strategic}-lessons.md` (+ `archive/`)
- Also live: `context/open-questions.md` (CLOSED channel — historical register) · `context/pre-verifications/` · `context/programs/matter-design/` · `context/coding-instructions/archive/` · `context/relay/archive/` · `context/status/archive/`

## File naming

- Audits/returns: `audits/YYYY-MM-DD_topic.md` — **dated by the operator-day FILED (America/Chicago), never the due date** (minted v54 beat 1). Two grandfathered due-date filenames are committed history, do not rename: `2026-08-20_RS1_…` and `2026-08-21_RS2_…` (both filed 2026-08-17)
- Orchestrator prompts: `handoff/YYYY-MM-DD_PM-mission-control_vNN_orchestrator_session_prompt.md` (newest non-archived = the standing prompt of record)
- Lane briefs / instructions: `instructions/YYYY-MM-DD_<name>_lane_brief.md` / `…_coding-instruction.md` / `…_bench-instruction.md`
- Operator packets: `handoff/YYYY-MM-DD_<name>_operator-packet.md`
- Archives: `archive/<source-name>-…-rotated-YYYY-MM-DD.md`; every archive file carries an inline header recording source path + rotation date (`context/handoff/archive/README.md`)
- Weekly/monthly plan names (`weeks/YYYY-WNN_monDD-monDD.md`, `months/YYYY-MM_month.md`) are historical conventions — weekly plans are retired
- Design docs (homesynapse-core-docs): `design/NN-name.md` for the core docs; `design/YYYY-MM-DD_topic.md` for ad-hoc; amendments at `design/amendments/`

## Source repos (the five-repo model)

- `homesynapse-core`: `[module-group]/[module-name]/MODULE_CONTEXT.md` (one per module); traceability at `docs/traceability/`; the FE territory at `web-ui/dashboard/`
- `homesynapse-core-docs`: `design/`, `governance/`, `foundations/`, `research/`, `archive/`, `website/`
- `nexsys-bench`: the bench corpus + tools/scenarios/harness
- `nexsys-skills`: `orchestrators/` (the FE role skill) + `design/` (the skills-architecture corpus)

## Research document placement (RULE, added 2026-06-05 — the Research 6/7v2/12 loose-file lesson; still standing)

- **Raw research RETURNS** produced from a docs-repo-consumed brief → `homesynapse-core-docs/research/returns/YYYY-MM-DD_Research_N_<Short_Title>.md`, committed **verbatim, unedited, at intake**. Research-LANE returns chartered by hivemind briefs file to the brief's named path (`context/audits/` or `context/research/` as the brief states).
- **PM assessments** → `nexsys-hivemind/context/assessments/`.
- **Research briefs** → `nexsys-hivemind/context/instructions/`, archived once consumed.
- Any session that receives a research return as an upload/paste MUST include "commit the return to its named home" in its closeout actions for Nick.

## Inter-agent message kinds (SUPERSEDED 2026-08-18)

The typed-message channels are retired — the beat spine absorbed them (W-COHERE gap row 7; ruled at the R-11 disposition, hub ratifies): questions, escalations, and cross-agent facts ride pm-handoff beats, lane returns, and dispatch packets. `context/open-questions.md` is a closed historical register; `cross-agent-notes.md` is an archived pointer stub; the `[FORESIGHT-NOTE] → coder-handoff §Foresight Notes` route pointed at a section that never existed in the live file and is void.

## Directories that NO LONGER EXIST (catch stale references — corrected 2026-08-18)

- `context/queue/` (+ subdirs) and the legacy `hivemind/` agent directory — removed 2026-04-11
- `context/design/` — moved to `homesynapse-core-docs` 2026-04-11
- `context/traceability/` — template-only tree, removed in the 2026-04-11 overhaul (real indexes: `homesynapse-core/docs/traceability/`)
- **Corrections of the prior list:** `context/governance/` and `context/research/` were WRONGLY listed here as removed — both exist and are load-bearing (the W-COHERE row-3 conviction; the misdirection this rebuild retires)
