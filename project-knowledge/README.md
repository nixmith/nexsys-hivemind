<!--
file: project-knowledge/README.md
purpose: Explains that project-knowledge/ holds the writable source for files uploaded to the Claude Project.
audience: All
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-05-27 against M3.7 closeout
-->

# Project Knowledge — Canonical Source Files

This directory holds the writable source copies of all files uploaded to the
HomeSynapse Core Claude Project's project knowledge.

## Relationship

nexsys-hivemind/project-knowledge/ (writable source)
    ↓ Nick uploads to Claude Project
Claude Project knowledge (read-only mirror)

## Update Protocol

1. Cowork or Claude Code updates files HERE (in this directory)
2. Nick reviews the changes
3. Nick uploads the updated file(s) to the Claude Project's project knowledge
4. Nick verifies the upload by asking the Claude Project to search for a known term

## Files

| File | Claude Project Upload Name | Purpose | Update Cadence |
|------|---------------------------|---------|----------------|
| Invariants_Quick_Reference.md | Architecture_Invariants_v1.md | Constitutional-invariants index (152/41 as of 2026-06-09 — ALWAYS re-derive the total from the §17 table, never cite this cell) | Rarely (senior architect lock) |
| Decisions_Quick_Reference.md | HomeSynapse_Core_Locked_Decisions.md | LTD + DEC-M3 + D-NN register (token-efficient index) | When new decisions are locked |
| HomeSynapse_Knowledge_Primer.md | HomeSynapse_Knowledge_Primer.md | Compressed architectural context | At documentation checkpoints + milestone completions |
| HomeSynapse_Navigation_Index.md | HomeSynapse_Navigation_Index.md | File path registry, amendment status | When milestones land or amendments apply |
| HomeSynapse_Current_State.md | HomeSynapse_Current_State.md | Current milestone, decisions, workflow | After every milestone completion |

## Do NOT add to this directory without PM approval

The Claude Project has a hard ceiling of 12 files before RAG mode triggers
(empirical finding — quality degrades above 12 files regardless of token count).
Currently at 5 files. Every addition must justify its token budget.
