<!--
file: context/lessons/archive/README.md
purpose: Archive directory for phase-group rotation of coder-lessons.md. Populated by Batch F.
audience: Coder, PM
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-05-21 against `homesynapse-core` commit `dfb045e`
-->

# Lessons Archive

Archive directory for phase-group rotation of `coder-lessons.md`. Populated by **Batch F** of the 2026-05-20 reorganization (see `REORGANIZATION_PLAN_2026-05-20.md §4c` for the rotation rule).

## Rotation trigger

Major-phase-group transitions — e.g., when M4 starts, Phase 2 + M1.x + M2.x + M3.x lessons consolidate into archive bundles and the active file resets to the new phase's running log. Unlike the handoffs (monthly), lessons rotate **on phase boundaries** because lesson content stays cited across many milestones and benefits from larger contiguous bundles.

## Expected contents (post-Batch F)

- `coder-lessons-phase-2.md` — Phase 2 (Blocks A–S) lessons, 2026-03-15 through 2026-03-20.
- `coder-lessons-2026-04-m1-m2.md` — M1.x and M2.x lessons (currently no M1.x entries existed at archive time; reserved for the convention).
- *(future)* `coder-lessons-2026-05-m3.md` — M3.x lessons, populated when M4 starts and M3.x bundles archive.

Every archive file carries `state-type: history`, `status: ARCHIVED`, and an inline header recording the source path and rotation trigger.

## Why phase-group, not monthly

Coder lessons are reference material the active Coder reads back into context months after they were written (cf. `pm-lessons.md`, `strategic-lessons.md`). Coarse-grained archives keep the cross-citations stable and avoid month-boundary churn. Handoffs, by contrast, are session-state continuity — they rotate monthly because the active surface only needs the most recent WU.
