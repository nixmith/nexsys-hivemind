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

| File | Purpose | Update Cadence |
|------|---------|----------------|
| Architecture_Invariants_v1.md | 94 constitutional invariants | Rarely (senior architect lock) |
| HomeSynapse_Core_Locked_Decisions.md | LTD register | When new LTDs are locked |
| HomeSynapse_Knowledge_Primer.md | Compressed architectural context | At documentation checkpoints + milestone completions |
| HomeSynapse_Navigation_Index.md | File path registry, amendment status | When milestones land or amendments apply |
| HomeSynapse_Current_State.md | Current milestone, M3 decisions, workflow | After every milestone completion |

## Do NOT add to this directory without PM approval

The Claude Project has a hard ceiling of 12 files before RAG mode triggers
(empirical finding — quality degrades above 12 files regardless of token count).
Currently at 5 files. Every addition must justify its token budget.
