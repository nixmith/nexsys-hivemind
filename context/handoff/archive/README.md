<!--
file: context/handoff/archive/README.md
purpose: Archive directory for monthly/quarterly rotation of handoff state. Populated by Batch E.
audience: PM, Coder
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-05-21 against `homesynapse-core` commit `dfb045e`
-->

# Handoff Archive

Archive directory for monthly rotation of `coder-handoff.md` and `pm-handoff.md`, and quarterly rotation of `cross-agent-notes.md`. Populated by **Batch E** of the 2026-05-20 reorganization (see `REORGANIZATION_PLAN_2026-05-20.md §4` for rotation rules).

## Expected contents (post-Batch E)

- `coder-handoff-YYYY-MM.md` — historical M-series closeout blocks evicted from active `coder-handoff.md`.
- `pm-handoff-YYYY-MM.md` — historical PM closeouts evicted from active `pm-handoff.md`.
- `cross-agent-notes-YYYY-QN.md` — quarterly bundles of archived cross-agent notes (rotation is coarser than handoffs because note volume is lower).

## Rotation rules (§4)

- **Active `coder-handoff.md`:** retain most recent WU plus the running "Recent prior WUs" summary table; everything older moves here on a monthly cadence.
- **Active `pm-handoff.md`:** retain most recent PM closeout plus the running "Prior PM Closeouts" table; everything older moves here on a monthly cadence.
- **Active `cross-agent-notes.md`:** retain the active items above the `## Archived` separator plus a small breadcrumb pointer below it; archived entries older than ~2 weeks bundle into the quarter file here.

Every archive file carries `state-type: history`, `status: ARCHIVED`, and an inline header recording the source path and rotation date.
