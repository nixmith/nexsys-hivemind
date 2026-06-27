<!--
file: project-knowledge/README.md
purpose: Explains that project-knowledge/ holds the writable source for files uploaded to the Claude Project.
audience: All
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-06-15 — **STALE (do not trust the body; see the governance banner below).** The five curated copies here were last regenerated 2026-06-14 and are now ~5+ milestones behind: actual spine is core `b296e76` (M7.3 + Track-A) / docs **watermark AMD-95, invariants 170/50, Doc 16 + Doc 17 Locked** / M7.4a ISSUE-READY. Truth lives in `homesynapse-core-docs/governance/` + the code, never here.
-->

# Project Knowledge — Canonical Source Files

> **⚠ GOVERN-OR-RETIRE (skills-initiative SD-10 / inventory F2, flagged 2026-06-27).** The five curated quick-reference copies here (`Invariants_Quick_Reference`, `Decisions_Quick_Reference`, `HomeSynapse_Knowledge_Primer`, `HomeSynapse_Navigation_Index`, `HomeSynapse_Current_State`) are **derived copies of the authoritative registers**, and they have **rotted** — the only layer in the project that has (the code and the Locked docs have not). They are ~5+ milestones stale (last regenerated 2026-06-14). **Discipline (the skills truth-hierarchy):** truth is code > Locked-docs/registers (`homesynapse-core-docs/governance/`) > hivemind; these copies are **operational convenience only** and must be **regenerated-from-source before any re-upload — never hand-maintained**. `HomeSynapse_Current_State.md` is **redundant** with `context/status/PROJECT_SNAPSHOT.md` (the live state). **Nick's decision (open):** before the next Claude-Project upload, either (a) **regenerate** all five from source, or (b) **retire** the Claude-Project RAG path in favor of the pointer-not-copy skills system (the skills-initiative direction). Until then, treat the bodies below as **stale**. The `device-corpus/` subdir is **current** (the live Wave-1 bench knowledge) and is NOT part of this staleness.

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
| Invariants_Quick_Reference.md | Architecture_Invariants_v1.md | Constitutional-invariants index (163/47 as of 2026-06-12 — ALWAYS re-derive the total from the §17 table, never cite this cell) | Rarely (senior architect lock) |
| Decisions_Quick_Reference.md | HomeSynapse_Core_Locked_Decisions.md | LTD + DEC-M3 + D-NN register (token-efficient index) | When new decisions are locked |
| HomeSynapse_Knowledge_Primer.md | HomeSynapse_Knowledge_Primer.md | Compressed architectural context | At documentation checkpoints + milestone completions |
| HomeSynapse_Navigation_Index.md | HomeSynapse_Navigation_Index.md | File path registry, amendment status | When milestones land or amendments apply |
| HomeSynapse_Current_State.md | HomeSynapse_Current_State.md | Current milestone, decisions, workflow | After every milestone completion |

## Do NOT add to this directory without PM approval

The Claude Project has a hard ceiling of 12 files before RAG mode triggers
(empirical finding — quality degrades above 12 files regardless of token count).
Currently at 5 files. Every addition must justify its token budget.
