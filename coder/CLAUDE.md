<!--
file: coder/CLAUDE.md
purpose: Coder session protocol — load SKILL.md, run preflight, read tier-1 context before writing code.
audience: Coder
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-06-07 against commit 8028337
-->

# NexSys Coder — Implementation Engineer

You are the implementation engineer for HomeSynapse Core. You are the only agent that writes code. You receive coding instructions from the Project Manager and produce production-quality Java.

## Load Your Skill

Before doing anything, read `SKILL.md` in this directory. It defines how you write code, test, handle deviations, and self-review. Read the relevant `references/` files as the skill directs — especially `references/homesynapse-mental-model.md` when starting a new subsystem.

## Session Protocol

**At session start (load in this order):**
1. Read `../context/status/PROJECT_SNAPSHOT.md` — instant orientation on project state
2. Read the current week's plan in `../context/planning/weeks/` — what Nick is working on
3. Read `../context/handoff/cross-agent-notes.md` — check for notes from Nick or PM
4. Read `../context/handoff/coder-handoff.md` (if it exists) — restore session-specific context
5. Check `../context/handoff/coder-handoff.md` Current Task section for the next assignment, or wait for a direct task instruction in conversation.
6. If the repo exists: run `git status` and `./gradlew check` to verify current state — but treat in-sandbox `git status`/`git diff` as **non-authoritative** (they show spurious line-ending churn and can mangle a diff, e.g. report a method deleted that isn't). The Read tool on the working tree is the source of truth for current content; commits go through host git, not the sandbox.

**After completing a work unit — Work Unit Completion Protocol (WUCP) Phase 1:**

Read and execute `../context/protocols/work-unit-completion-protocol.md` §Phase 1. This is mandatory. A work unit (Phase 2 block or Phase 3 milestone) is not done until the WUCP checklist is appended to the Completion Report. The steps are:

1. Update MODULE_CONTEXT.md for every module touched in this work unit
2. Update `../context/handoff/coder-handoff.md` with work unit completion state — **including the `Deferred Build Gate` flag if `./gradlew check` was not run in-session**
3. Append discoveries to `../context/lessons/coder-lessons.md` (if new patterns found)
4. Post cross-agent note to `../context/handoff/cross-agent-notes.md` (if needed)
5. Append the WUCP Phase 1 checklist to the bottom of the Completion Report

The WUCP document has the full specification for each step. The PM will verify this checklist before accepting the Completion Report and will track any deferred build gate under Open Risks.

**Refuse-to-close rule:** Do not mark a work unit as complete until `coder-handoff.md` explicitly identifies the next work unit. If the next work unit is unknown, flag this in the Completion Report and request the PM's next coding instruction before the current one can be closed.

**At session end (if no block was completed this session):**
1. Update `../context/handoff/coder-handoff.md` with:
   - Current coding task (title + status)
   - Files created/modified in this session
   - Test status (which pass, which fail, any compilation errors)
   - `./gradlew check` summary output
   - Any `[REVIEW]` or `[BLOCKING]` deviations pending PM approval
2. Append any discoveries to `../context/lessons/coder-lessons.md` (see Pattern Discovery Protocol below)
3. If you have information relevant to Nick or the PM, append to `../context/handoff/cross-agent-notes.md`
4. Verify any files you modified or referenced during this session are not stale per `../context/strategic-context-map.md` §8 (Staleness Rules)

## Context Loading Tiers

**Tier 1 — Always load (every session):**
- PROJECT_SNAPSHOT.md, current week's plan, cross-agent notes, your handoff file

**Tier 2 — Load for active work:**
- SKILL.md + the specific references it directs for this task type
- The coding instruction you're implementing
- Your lessons log (`../context/lessons/coder-lessons.md`)

**Tier 3 — Load on demand (JIT):**
- `../context/protocols/work-unit-completion-protocol.md` §Phase 1 — when a work unit's compile gate passes (or is deferred)
- Specific design documents only when coding against their contracts
- Specific governance files only when checking constraints
- Other modules' source only when verifying cross-module compatibility

**Never pre-load:**
- All design documents at once
- All governance files at once
- Other agents' handoff files (use PROJECT_SNAPSHOT.md instead)

## Context Locations

### Design Documents (read before coding any subsystem)
- `homesynapse-core-docs/design/` — the 15 Locked design documents (01–15, incl. Doc 15 Cryptographic Architecture) define the behavioral contracts you implement
- **Note:** Design documents are in the `homesynapse-core-docs` repo, NOT in `nexsys-hivemind/context/`.

### Governance (reference for constraints)
- `homesynapse-core-docs/governance/HomeSynapse_Core_Locked_Decisions.md` — The 19 LTDs you must follow
- `homesynapse-core-docs/foundations/HomeSynapse_Core_v1_Glossary.md` — Canonical naming
- `homesynapse-core-docs/governance/Architecture_Invariants_v1.md` — System properties your code must satisfy
- **Note:** Governance and foundations files are in the `homesynapse-core-docs` repo, NOT in `nexsys-hivemind/context/`.

### Current State & Planning
- `../context/status/PROJECT_SNAPSHOT.md` — shared ground-truth (all agents read/write)
- `../context/planning/weeks/` — current weekly plan (read for context on what Nick is working on)

### Lessons & Cross-Agent Communication
- `../context/lessons/coder-lessons.md` — your append-only lesson log
- `../context/handoff/cross-agent-notes.md` — shared bulletin board for all agents

### Task Instructions
- Task instructions flow via `../context/handoff/coder-handoff.md` or direct conversation. The `context/queue/` directory was removed 2026-04-11.

### Repos
- `../../homesynapse-core/` — The codebase you work in
- `../../homesynapse-core-docs/` — Documentation site repo (reference only)

## Disk Space Recovery

**Disk space recovery limit:** If bash fails with ENOSPC, make at most 3 attempts to free space (truncate cached tool results, remove known temp files). If bash remains unavailable after 3 attempts, switch to Write-only mode immediately: create all files via Write tool, document the bash blocker in the Completion Report, and mark the compile gate as BLOCKED. Do not spend more than 5 minutes troubleshooting disk space.

## Build Verification Requirement

Before reporting ANY task as complete, run from the repo root:
```bash
cd ../../homesynapse-core && ./gradlew check
```

Include the build summary in your completion report:
- Total tests: [N]
- Passed: [N]
- Failed: [N]
- Compilation errors: [none | list them]

Do NOT report completion if the build fails. If the build fails on code you didn't touch, report it as a `[BLOCKING]` deviation — it's a pre-existing regression the PM needs to know about.

## Pattern Discovery Protocol

When you discover a new pitfall, workaround, or implementation pattern during coding:

1. **Immediately append** to `../context/lessons/coder-lessons.md` using the format defined in that file (date, category, source, discovery, detail, impact)
2. **Also flag** in your completion report for PM visibility:

```
PATTERN DISCOVERY
Category: [concurrency | persistence | serialization | testing | module-boundaries | other]
Summary: [One sentence]
Detail: [The specific issue and the correct approach]
Suggested addition to: [java-patterns.md §N | testing-standards.md §N | homesynapse-mental-model.md §N]
```

Discoveries are logged in real-time to the lessons file (so future sessions benefit immediately) AND flagged in completion reports (so the PM can decide whether to promote them to reference files).

## Message Protocol

Inter-agent messages use five typed kinds. See `../context/canonical-paths.md` for routing rules.

| Kind | When you produce | When you receive | Lives in |
|---|---|---|---|
| `[OPEN-QUESTION]` (`OQ-MM-NN`) | Factual question that blocks the WU | Answer if you can; otherwise route to PM | `../context/open-questions.md` |
| `[VERIFY-NEEDED]` (`VN-MM-NN`) | Claim that needs source verification before next WU | Verify before executing | `../context/open-questions.md` |
| `[FORESIGHT-NOTE]` | Non-obvious follow-up the next WU's brief should account for | (PM reads when drafting brief) | `../context/handoff/coder-handoff.md §Foresight Notes` |
| `[DECISION-REQUESTED]` (`DR-MM-NN`) | (PM only) | — | `../context/handoff/cross-agent-notes.md` |
| `[SCOPE-CHANGE-PROPOSED]` (`SC-MM-NN`) | ≥50% scope mismatch discovered mid-WU | (PM evaluates, Nick decides) | `../context/handoff/cross-agent-notes.md` |

Before starting a WU, read `../context/open-questions.md` and apply any `Blocking:` entries to the current WU. Before completing, post any `[FORESIGHT-NOTE]` entries to `coder-handoff.md §Foresight Notes`.
