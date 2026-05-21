<!--
file: context/strategy/README.md
purpose: Inventory of Nick's strategic artifacts in context/strategy/ and the rules for how agents read them.
audience: PM, Nick
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-05-21 against `homesynapse-core` commit `dfb045e`
-->

# Strategy

Long-form strategic artifacts authored by Nick. The PM reads these in Mode 1 (Architect) when decomposing task briefs that touch product positioning, revenue, data strategy, or institutional framing. Per D-4 (`REORGANIZATION_PLAN_2026-05-20.md §13`), these files are deliberately **not** edited by agents — leave them alone.

## Files

| File | Type | When the PM reads it |
|---|---|---|
| `Six_Battlefields_MVP_Strategy.md` | Markdown | Task briefs that touch feature prioritization, competitive framing, or MVP scope decisions |
| `Revenue_Model_and_Licensing_Strategy.md` | Markdown | Any discussion of monetization, licensing, pricing, or revenue-adjacent features; canonical source for the Non-Negotiable Revenue Principles |
| `From_Platform_to_Institution_NexSys_Strategic_Report.docx` | Word | Strategic-framing decisions, institutional positioning, long-horizon trajectory |
| `HomeSynapse_MVP_Data_Readiness_Specification.docx` | Word | MVP data-readiness questions, telemetry obligations, data-strategy alignment |
| `NexSys_Data_Value_Engine_Strategy.docx` | Word | Data-value engine decisions, monetization-via-data questions |

## Read rules

- **`.docx` files are authoritative.** Nick maintains them in Microsoft Word. Agents read them via the `docx` skill (see `project-manager/SKILL.md §Mode 1 Step 5`). Do not convert, edit, or shadow them with `.md` copies.
- **`.md` files are also authoritative.** They live here because they're long-form prose Nick maintains in Markdown by preference, not because they're a degraded export of anything else.
- **Strategy files are NOT in the Claude Project upload zone** (`project-knowledge/`) — by design. `project-knowledge/` holds *current-state* hub files agents read at session start; strategy files are read on-demand by the PM only when a task brief invokes one. The boundary keeps Tier-1 context lean.

## Cross-references

- `context/strategic-context-map.md` §6 lists the strategy layer alongside other context surfaces and notes when the PM is expected to consult it.
- `project-manager/SKILL.md §Mode 1` (Architect) is the only place where strategy files enter active consideration during a session.
