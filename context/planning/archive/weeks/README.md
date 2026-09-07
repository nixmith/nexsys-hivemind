<!--
file: context/planning/weeks/README.md
purpose: Documents the W16–W20 gap in the weekly-plan series — the cadence shift from weekly-plan-as-primary to milestone-cadence-as-primary.
audience: All
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-05-21 against `homesynapse-core` commit `dfb045e`
-->

# Weekly Plans

Day-by-day breakdowns and end-of-week retrospectives for each ISO week of NexSys development.

## W16–W20 gap (2026-04-13 → 2026-05-17)

There is no weekly plan file for ISO weeks **2026-W16 through 2026-W20**. This is a deliberate cadence shift, not missed obligation.

**What changed.** During Phase 2 (Blocks A–S, ISO 2026-W11 through W13), the weekly plan was the primary scheduling artifact — day-by-day tasks, end-of-week retrospectives, sprint-shaped granularity. Around the Phase 2 → Phase 3 transition (2026-04-11 governance overhaul; see `context/audits/2026-04-11_m2.5-arch-debt-retrospective.md`), Phase 3's milestone-granularity (M2.1, M2.2, …, M3.1, M3.2, …) replaced sprint-week-granularity as the real scheduling cadence: each milestone is a single compile-and-commit unit with test coverage and a WUCP closeout, much narrower than a "week of work."

**Net effect.** Weekly plans stopped tracking active scheduling between mid-April and mid-May because the milestone backlog became the authoritative cadence. `context/planning/phase-3-milestone-backlog.md` records the real per-milestone progress for that period (M2.5 through M3.5b roughly). `context/strategic-context-map.md §8` (Staleness Rules) and `master-release-plan.md` Phase 3 Progress Annotation are the other live cross-references for the same window.

**Why W21 resumed.** `2026-W21_may18-may24.md` exists because Nick chose to reintroduce a weekly file at the start of the M3.6 cohort to capture day-grained context for the M3.6a → M3.6e composition-root push. Whether weekly files persist past M3.6 will depend on Phase 3's remaining shape.

## What this means for agents

- **Do not** treat the W16–W20 absence as missing data. The `phase-3-milestone-backlog.md` is authoritative for what happened in that window.
- **Do not** retroactively backfill W16–W20 weekly files. Per N-2 (`REORGANIZATION_PLAN_2026-05-20.md §13`), the cadence shift is recorded here as documentation, not as work to do.
- **Do** treat any future week file the same way W21 was created — when day-grained scheduling adds value for a specific cohort, not as an ongoing weekly obligation.

## Filename convention

`weeks/YYYY-WNN_monDD-monDD.md` (e.g., `2026-W21_may18-may24.md`). See `context/canonical-paths.md`.
