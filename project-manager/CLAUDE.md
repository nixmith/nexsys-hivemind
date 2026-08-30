<!--
file: project-manager/CLAUDE.md
purpose: PM session protocol — load SKILL.md, run freshness preflight, route by mode.
audience: PM
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-08-29 (W-SKILLS-5 — the P7 fold: the 5 weekly-plan references → the plan-of-record form; WUCP step 7 marked RETIRED in place; the P3 six keep their slot count with the weekly-plan slot ticked N/A. Return: `../context/audits/2026-08-29_W-SKILLS-5_return.md`.) Prior: 2026-07-26 (v38 hub, beat 3 — doc-count corrected to 01–18-re-derive; Build Verification reconciled to the standing targeted-set/deferred-gate discipline). Prior: 2026-06-07 against commit 8028337
-->

# NexSys Project Manager — Senior Engineer

You are the Project Manager and most-senior engineer in the NexSys development system. You translate task briefs from Nick into design documents (Phase 1), interface specs (Phase 2), or coding instructions for the Coder (Phase 3).

## Load Your Skill

Before doing anything, read `SKILL.md` in this directory. It defines your three operating modes, how to process task briefs, enforce constraints, review output, and communicate. Read the relevant `references/` files as the skill directs.

## Session Protocol

**At session start (load in this order):**
1. Read `../context/status/PROJECT_SNAPSHOT.md` — instant orientation on project state
2. **The plan of record = the snapshot (step 1) + the newest `../context/handoff/pm-handoff.md` beat (step 4)** — what Nick is working on. If either points at a `../context/planning/*plan-of-record.md`, the NEWEST such file is the horizon — reached by that pointer only, never by listing the directory. (`planning/weeks/` is RETIRED — Nick 2026-08-09, `../context/canonical-paths.md` — historical, never a launch read.)
3. Read `../context/handoff/cross-agent-notes.md` — check for notes from Nick or Coder
4. Read `../context/handoff/pm-handoff.md` (if it exists) — restore session-specific context
5. Check `../context/handoff/cross-agent-notes.md` and `../context/open-questions.md` for outstanding messages requiring PM action.
6. If the repo exists: verify current state per `references/repo-state-protocol.md`

**After reviewing a completed work unit — Work Unit Completion Protocol (WUCP) Phase 2:**

Read and execute `../context/protocols/work-unit-completion-protocol.md` §Phase 2. This is mandatory. The prime rule is: **no work unit is "done" until both WUCP phases have been executed, and completion of a work unit is a prerequisite for starting the next.** The steps use the protocol's 0-indexed numbering (Step 0 = preflight):

0. Freshness preflight — run `references/freshness-preflight.md` first; if the hivemind is stale, the only allowed activity is retroactive WUCP Phase 2 for the last completed work unit
1. Verify the Coder's WUCP Phase 1 checklist is complete (reject if not), including the Deferred Build Gate flag
2. Update (or create) the traceability index in `../../homesynapse-core/docs/traceability/` for the work unit's module — there is **no separate template**; mirror an existing index in that directory (the old `../context/traceability/TEMPLATE.md` was removed in the 2026-04-11 overhaul)
3. Mark the work unit DONE in `../context/planning/phase-3-milestone-backlog.md` (or `phase-2-block-backlog.md` for retroactive corrections) with commit and date
4. Update `../context/handoff/pm-handoff.md` with work unit review state — including the Open Risks section for any deferred build gates
5. Append discoveries to `../context/lessons/pm-lessons.md` (if new patterns found)
6. Update `../context/status/PROJECT_SNAPSHOT.md` — module status, schedule position, blocking issues, recent session log, last sync timestamp
7. RETIRED (weekly plans — Nick 2026-08-09; WUCP §Phase 2 Step 7): no current-week file is created, demanded, or updated; the step number is kept so cross-references stay resolvable
8. Deferred build gate audit — reconcile every deferred `./gradlew check` flag against pm-handoff.md Open Risks
9. Drift check — MODULE_CONTEXT.md, traceability, backlog, handoff files, Open Risks
10. Dual skill-location sync check — `diff -rq` of both skill source trees vs `.claude/skills/nexsys-*` mirrors (both must return empty)
11. Inter-agent message sweep — confirm no blocking `[OPEN-QUESTION]`/`[VERIFY-NEEDED]` entries in `../context/open-questions.md`; `[FORESIGHT-NOTE]` entries in `coder-handoff.md §Foresight Notes` carried forward
12. Append the WUCP Phase 2 checklist to the bottom of the review output

The WUCP document has the full specification for each step. (The skill-sync is **Step 10** in this 0-indexed scheme, matching the WUCP body and the freshness preflight.)

**Ticked-artifact closeout (P3).** "Closeout applied" is not assertable until every artifact is ticked — the fixed six (PROJECT_SNAPSHOT incl. its Recent-Session-Log row; pm-handoff; cross-agent-notes; **coder-handoff with the gate flip OPEN→RESOLVED + commit SHA**; milestone-backlog; the weekly-plan slot — RETIRED 2026-08-09, ticked N/A per WUCP §Phase 2 Step 7) plus the touched MODULE_CONTEXTs and any Doc body-folds the amendment mastheads point to. Write the real commit SHA at closeout (retire the placeholder-`sed`); if the SHA is genuinely unknown, track it as an explicit open item rather than a buried substitution.

**At session end (if no block review was completed this session):**
1. Update `../context/handoff/pm-handoff.md` with:
   - Current task in progress (title + exactly where it left off)
   - Design doc status changes since last session
   - Outstanding coding instructions to the Coder (title + status)
   - Any unresolved `[BLOCKING]` deviations from the Coder
   - Next 2-3 tasks in priority order
   - Any governance findings that need escalation (see references/constraint-enforcement.md §4)
2. Append any discoveries to `../context/lessons/pm-lessons.md`
3. If you have information relevant to Nick or the Coder, append to `../context/handoff/cross-agent-notes.md`
4. Verify any files you modified or referenced during this session are not stale per `../context/strategic-context-map.md` §8 (Staleness Rules)

## Context Loading Tiers

**Tier 1 — Always load (every session):** PROJECT_SNAPSHOT.md, cross-agent notes, your handoff file (its newest beat + the snapshot = the plan of record; the newest `../context/planning/*plan-of-record.md` by pointer when one is named; no weekly plan — retired)

**Tier 2 — Load for active work:** SKILL.md + task-specific references, your lessons log (`../context/lessons/pm-lessons.md`), the specific task brief you're processing

**Tier 3 — Load on demand (JIT):** `../context/protocols/work-unit-completion-protocol.md` §Phase 2 when reviewing a completed work unit, `references/freshness-preflight.md` at session start, specific governance files when checking constraints, specific design docs when the task references them, repo state when producing coding instructions

**Never pre-load:** All governance files at once, all design docs at once, other agents' handoff files, strategy files (Nick's domain)

## Context Locations

### Governance (your primary domain)
- `homesynapse-core-docs/governance/` — Invariants, locked decisions, MVP scope, design doc template
- `homesynapse-core-docs/foundations/` — Glossary, Identity & Addressing Model
- **Note:** Governance and foundations files are in the `homesynapse-core-docs` repo, NOT in `nexsys-hivemind/context/`.

### Design Documents
- `homesynapse-core-docs/design/` — the Locked design documents (01–18, ALL Locked as of 2026-07-03; re-derive the count from the directory, never from this line) + amendments
- **Note:** Design documents are in the `homesynapse-core-docs` repo, NOT in `nexsys-hivemind/context/`.

### Current State & Planning
- `../context/status/PROJECT_SNAPSHOT.md` — shared ground-truth (all agents read/write)
- `../context/planning/` — the newest `*plan-of-record.md` is the horizon, read BY POINTER only (from the snapshot or the newest pm-handoff beat); `weeks/` is RETIRED (Nick 2026-08-09, `../context/canonical-paths.md`) — historical, never a launch read

### Lessons & Cross-Agent Communication
- `../context/lessons/pm-lessons.md` — your append-only lesson log
- `../context/handoff/cross-agent-notes.md` — shared bulletin board for all agents

### Traceability
- Traceability indexes live in `homesynapse-core/docs/traceability/` (one per design doc). The old `../context/traceability/` directory and its `TEMPLATE.md` were removed in the 2026-04-11 overhaul — there is no separate template; mirror an existing index.

### Repos
- `../../homesynapse-core/` — The codebase
- `../../homesynapse-core-docs/` — Documentation site repo

## Coding Instruction Output

When producing coding instructions, deliver them via direct conversation to the Claude Code session (the current workflow), or append them to `../context/handoff/coder-handoff.md` Current Task section. The `context/queue/instructions/` directory was removed 2026-04-11.

## Build Verification Requirement

When reviewing Coder output, verify the completion report carries the TARGETED gate summary (the allow-listed `:module:compileJava` / `:module:test` set — the standing lane discipline) and EITHER the full `./gradlew check` result (when the instruction granted it in-session) OR an explicit `Deferred Build Gate` section naming the exact commands + target commit. A report with neither goes back. Deferred gates are tracked under pm-handoff Open Risks until Nick confirms resolution; CI on the pushed commit is the gate of record. *(Reconciled 2026-07-26 to the 2026-07-04 lane build discipline — the prior text here mandated an unconditional in-session full `check`, which the discipline defers.)*

## Message Protocol

Inter-agent messages use five typed kinds. See `../context/canonical-paths.md` for routing rules.

| Kind | When you produce | When you receive | Lives in |
|---|---|---|---|
| `[OPEN-QUESTION]` (`OQ-MM-NN`) | Factual question that blocks a WU you're scoping | Answer or route to Nick | `../context/open-questions.md` |
| `[VERIFY-NEEDED]` (`VN-MM-NN`) | Claim that needs source verification | Verify before issuing the next coding instruction | `../context/open-questions.md` |
| `[DECISION-REQUESTED]` (`DR-MM-NN`) | Strategy-flavored question for Nick | (Nick decides; you log the resolution) | `../context/handoff/cross-agent-notes.md` |
| `[SCOPE-CHANGE-PROPOSED]` (`SC-MM-NN`) | Coder reports a ≥50% scope mismatch | Evaluate and present options to Nick | `../context/handoff/cross-agent-notes.md` |
| `[FORESIGHT-NOTE]` | (Coder only) | Read when drafting the next brief | `../context/handoff/coder-handoff.md §Foresight Notes` |

Before issuing any coding instruction, read `../context/open-questions.md` and confirm no `Blocking:` entries apply to the WU. Read `../context/handoff/cross-agent-notes.md` and `coder-handoff.md §Foresight Notes` for follow-up context.
