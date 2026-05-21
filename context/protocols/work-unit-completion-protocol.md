<!--
file: context/protocols/work-unit-completion-protocol.md
purpose: Mandatory work-unit completion protocol (WUCP) for Phase 2 blocks and Phase 3 milestones.
audience: PM, Coder
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# Work Unit Completion Protocol (WUCP)

**Authority:** This protocol is mandatory for every work unit completion in Phase 2 and Phase 3. A work unit is not DONE until all applicable WUCP phases are complete.

**Location:** `nexsys-hivemind/context/protocols/work-unit-completion-protocol.md`
**Last updated:** 2026-04-11 (generalized from Block Completion Protocol v1)
**Owner:** Nick (process governance)

---

## The Prime Rule

> **No work unit is "done" until both WUCP phases have been executed. Completion of a work unit is a prerequisite for starting the next work unit.**

This rule is non-negotiable. If WUCP Phase 2 has not run for the most recent work unit, the next work unit cannot begin. A session that discovers a stale hivemind must run WUCP Phase 2 retroactively before doing anything else — this is enforced by the session-start freshness preflight (`project-manager/references/freshness-preflight.md`).

This rule exists because of the 2026-04-11 retrospective: BCP Phase 2 did not execute for ~3 weeks across five milestones, latent arch-rule violations shipped through two of them, and the staleness compounded exponentially the longer it went unchecked. See `context/audits/2026-04-11_m2.5-arch-debt-retrospective.md`.

---

## Vocabulary: What Is a Work Unit?

A **work unit** is a coherent compile-and-commit unit with test coverage. In Phase 2, work units were called **Blocks** (letters A–S). In Phase 3, work units are called **Milestones** (M{major}.{minor}, e.g., M2.5). The WUCP applies uniformly to both — the phase vocabulary changes but the protocol does not.

Where this file says "work unit," substitute the current phase's vocabulary:
- Phase 2 block → "Block N complete"
- Phase 3 milestone → "Milestone M2.5 complete"

---

## Why This Protocol Exists

A work unit is not "done" when the compile gate passes. A work unit is "done" when the state of the project documentation accurately reflects the state of the code. Without an enforced closeout sequence, documentation drifts silently — MODULE_CONTEXT files go unpopulated, traceability indexes fall behind, PROJECT_SNAPSHOT stops reflecting reality, and deferred build gates are forgotten. Each gap compounds: the next agent session starts with less context, makes more assumptions, and produces more drift.

This protocol makes documentation updates a **gate**, not an afterthought.

---

## Protocol Structure

The WUCP runs as a two-phase sequential chain. Each phase produces a visible checklist artifact that the next agent verifies.

```
Compile Gate passes (or is deferred + tracked)
        │
        ▼
┌─ WUCP Phase 1: Coder Closeout ─┐
│  MODULE_CONTEXT.md              │
│  coder-handoff.md               │
│  coder-lessons.md               │
│  cross-agent note (if needed)   │
│  Deferred build gate flag (if)  │
│  Checklist in Completion Report │
└────────────┬────────────────────┘
             │
             ▼
┌─ WUCP Phase 2: PM Closeout ────┐
│  Freshness preflight (pass)     │
│  Verify Coder Phase 1 complete  │
│  Traceability index             │
│  Milestone backlog              │
│  pm-handoff.md (incl. risks)    │
│  pm-lessons.md                  │
│  PROJECT_SNAPSHOT.md            │
│  Weekly plan progress           │
│  Deferred build gate audit      │
│  Drift check (all artifacts)    │
│  Dual skill-location sync check │
│  Inter-agent message sweep      │
│  Checklist appended to review   │
└─────────────────────────────────┘
```

Both phases run per work unit, immediately after completion. Do not defer to a later session.

---

## Phase 1: Coder Closeout

**Trigger:** Compile gate (`./gradlew check` or `./gradlew compileJava` with `-Xlint:all -Werror`) passes for the work unit's module — OR is explicitly deferred to Nick's sandbox-external environment with a documented flag.

**Timing:** Immediately after the compile gate (or deferral), in the same session. Do not defer to a later session.

### Step 1 — Update MODULE_CONTEXT.md

For every module touched in this work unit, update (or create) the MODULE_CONTEXT.md file at `homesynapse-core/[module-path]/MODULE_CONTEXT.md`.

Contents must include:
- **Purpose:** One-sentence module responsibility
- **Type Inventory:** Every public type (interface, record, enum, sealed interface) with one-line description
- **Dependencies:** Which modules this module requires (matches module-info.java)
- **Consumers:** Which modules depend on this one
- **Cross-Module Contracts:** Behavioral promises this module makes to its consumers
- **Constraints:** Which LTDs and INVs are active in this module
- **Gotchas:** Non-obvious pitfalls discovered during implementation
- **Phase 3 Notes:** Implementation considerations for when tests and code are written

**If MODULE_CONTEXT.md already exists:** Update the Type Inventory and any sections affected by this work unit's changes. Do not rewrite sections that haven't changed.

**If a cross-module update touched another module:** Update that module's MODULE_CONTEXT.md too (at minimum, the Type Inventory and Cross-Module Contracts sections).

### Step 2 — Update coder-handoff.md

Overwrite `nexsys-hivemind/context/handoff/coder-handoff.md` with:
- Work unit completed (identifier + module name)
- Files created/modified (count + module breakdown)
- Compile gate result (pass, warnings, or **DEFERRED** — see Step 2a)
- Cross-module updates made (if any)
- Deviations pending PM review (if any)
- Next expected work unit (from the relevant backlog)

### Step 2a — Deferred Build Gate Flag (conditional)

If `./gradlew check` was **not** run during this session (deferred to Nick's sandbox-external environment), the coder-handoff must include an explicit `Deferred Build Gate` section at the top with:

- Which commands need to run (`./gradlew check`, `./gradlew :core:persistence:test`, etc.)
- Which commit the gate must run against (usually the most recent commit in this work unit)
- A note that this deferral must be tracked on `pm-handoff.md` under Open Risks until resolved

**Without this flag, the PM's freshness preflight cannot track the deferral, and the violation that caused the 2026-04-11 retrospective will recur.**

### Step 3 — Append to coder-lessons.md

If this work unit produced any pattern discovery, pitfall, or workaround, append to `nexsys-hivemind/context/lessons/coder-lessons.md` using the established format.

If no new patterns were discovered, skip this step. Do not append a "no discoveries" entry.

### Step 4 — Post cross-agent note (conditional)

If this work unit produced information that the PM or Nick needs to act on — cross-module changes, deviation discoveries, JPMS lessons, compile-gate surprises, deferred build gate flags — append to `nexsys-hivemind/context/handoff/cross-agent-notes.md`.

If nothing needs cross-agent attention, skip this step.

### Step 5 — Append WUCP Checklist to Completion Report

At the bottom of the Completion Report (after deviations), append:

```
## WUCP Phase 1: Coder Closeout

- [x/ ] MODULE_CONTEXT.md updated for: [list module names]
- [x/ ] coder-handoff.md updated
- [x/ ] Deferred build gate flag: [YES / NO]
- [x/ ] coder-lessons.md appended: [summary or "No new patterns"]
- [x/ ] Cross-agent note posted: [summary or "Not needed"]
- Timestamp: YYYY-MM-DD HH:MM UTC
```

Format is canonical. Use the exact checkbox syntax shown above. Do not substitute tables or alternative formats — the PM verifies completion by parsing this exact structure.

**Gate:** If any required box is unchecked, the Completion Report is incomplete. The PM should reject incomplete reports.

---

## Phase 2: PM Closeout

**Trigger:** Coder Completion Report received with WUCP Phase 1 checklist complete.
**Timing:** During the PM's review of the Coder output, in the same session. If the work unit was completed in a prior session and WUCP Phase 2 is running retroactively, flag every artifact update with "retroactive" and the true current date.

### Step 0 — Freshness Preflight

Before any other step, run the session-start freshness preflight per `project-manager/references/freshness-preflight.md`. The preflight determines whether the hivemind is current relative to the codebase. If the preflight reports staleness, the only allowed WUCP Phase 2 activity is the retroactive closeout for the last completed work unit — no forward work until freshness is restored.

### Step 1 — Verify Coder Phase 1 Complete

Check the WUCP Phase 1 checklist in the Completion Report. Verify:
- MODULE_CONTEXT.md exists and is current for every module the work unit touched
- coder-handoff.md reflects the completed work unit
- Deferred build gate flag is set correctly
- Lessons and cross-agent notes are posted if warranted

**If Phase 1 is incomplete:** Return the Completion Report to the Coder with specific items to address. Do not proceed with Phase 2 until Phase 1 is done.

### Step 2 — Update Traceability Index

Update (or create) the traceability file for this work unit's module.

**Location:** `homesynapse-core/docs/traceability/[NN]-[module-name].md`
**Template:** `nexsys-hivemind/context/traceability/TEMPLATE.md`

For Phase 2 (interface specification), populate:
- **Design Decision → Interface mapping:** Every design doc decision that produced an interface or type
- **Invariant Coverage:** Which interfaces satisfy which INVs
- **LTD Compliance:** Which types/interfaces enforce which LTDs

For Phase 3 (implementation), also populate:
- **Phase 3 Class column:** Implementation classes
- **Test Class.method column:** Test methods that verify each decision

### Step 3 — Update the Relevant Backlog

**Phase 2 work units** → update `nexsys-hivemind/context/planning/phase-2-block-backlog.md` (frozen; only touched for retroactive corrections).
**Phase 3 work units** → update `nexsys-hivemind/context/planning/phase-3-milestone-backlog.md`.

1. Change the work unit's status from `NEXT` (or `IN_PROGRESS`) to `DONE`
2. Add commit SHA and completion date
3. If applicable, advance the next work unit to `NEXT` status
4. If a deferred build gate was flagged, add a Notes column entry referencing the open risk

### Step 4 — Update pm-handoff.md (including Open Risks)

Overwrite `nexsys-hivemind/context/handoff/pm-handoff.md` with:
- Work unit reviewed (identifier + module name + status)
- Traceability index status for this module
- Deviations approved/rejected
- Next expected PM work (next work unit's coding instruction, or other PM tasks)
- Any escalations pending
- **Open Risks section** — every deferred build gate logged with a specific closure condition ("resolved when Nick reports successful `./gradlew check` on commit X"). The risk remains open until that condition is met.

### Step 5 — Append to pm-lessons.md

If this work unit's review produced any new pattern, constraint application insight, or cross-subsystem observation, append to `nexsys-hivemind/context/lessons/pm-lessons.md`.

### Step 6 — Update PROJECT_SNAPSHOT.md

Update `nexsys-hivemind/context/status/PROJECT_SNAPSHOT.md`:
- Module status table: update status and file counts for completed work unit(s)
- Schedule position: recalculate days ahead/behind vs. master release plan
- Blocking issues: add or resolve as needed
- Next on critical path: update to reflect current state
- Recent session log: add entry for the work unit completion(s)
- MODULE_CONTEXT.md status line: update to reflect which modules have current MODULE_CONTEXT files
- Last sync timestamp

### Step 7 — Update Weekly Plan Progress

In the current week's plan (`nexsys-hivemind/context/planning/weeks/`), add completion notes for the work unit(s):
- Which work units completed
- Actual vs. planned timing
- Any scope adjustments made

If the current week's plan file does not exist, create it.

### Step 8 — Deferred Build Gate Audit

For each coder-handoff completed since the last PM-side closeout, check the `Deferred Build Gate` section:

- Every deferred `./gradlew check` must be logged on `pm-handoff.md` under "Open Risks" with a specific closure condition
- If Nick has reported a successful run of a deferred gate since the last closeout, remove the risk from Open Risks and note its resolution in the pm-handoff
- If any deferred gate from a previous work unit is unresolved AND a new work unit is about to begin, escalate to Nick before approving the new work unit

### Step 9 — Drift Check

Verify documentation state is current. Check each item:

| Artifact | Check | Source of Truth |
|---|---|---|
| MODULE_CONTEXT.md | Exists and current for every module with a completed work unit | `homesynapse-core/[module]/MODULE_CONTEXT.md` |
| Traceability index | Exists for every module with a completed work unit | `homesynapse-core/docs/traceability/` |
| Milestone backlog | All completed work units marked DONE with commits and dates | `phase-3-milestone-backlog.md` |
| Agent handoff files | PM and Coder handoffs reflect current state | `nexsys-hivemind/context/handoff/` |
| Cross-agent notes | No unresolved active items older than 1 week | `nexsys-hivemind/context/handoff/cross-agent-notes.md` |
| Open Risks | Every deferred build gate tracked; every resolved risk removed | `pm-handoff.md` |

**If any item fails the drift check:** Post a cross-agent note identifying the gap, the responsible agent, and what needs to be done. If the gap is critical, escalate to Nick.

### Step 10 — Dual Skill-Location Sync Check

The hivemind maintains two copies of each agent skill directory:

- Writable source: `ClaudeFolder/nexsys-hivemind/{coder,project-manager}/`
- Mirror (what agents actually load): `.claude/skills/nexsys-{coder,project-manager}/`

Both must be byte-identical at the end of every WUCP Phase 2. Resolve `$SESSION_ROOT` via path traversal at runtime (matching `project-manager/references/freshness-preflight.md`), then run:

```
diff -rq "$SESSION_ROOT/mnt/ClaudeFolder/nexsys-hivemind/coder" "$SESSION_ROOT/mnt/.claude/skills/nexsys-coder"
diff -rq "$SESSION_ROOT/mnt/ClaudeFolder/nexsys-hivemind/project-manager" "$SESSION_ROOT/mnt/.claude/skills/nexsys-project-manager"
```

Both commands should return empty when the mirror is in sync with the source.

**Interpreting the output:**

- **Empty output (both commands):** PASS. The mirror matches the source. Record `Dual skill-location sync check: PASS (both diffs empty)` in the checklist.
- **`Only in ClaudeFolder/...` entries:** STALE — expected. The PM has edited source files that Nick has not yet externally mirrored. `.claude/skills/` is a read-only mount; the PM cannot write to it. Record `Dual skill-location sync check: STALE (N files awaiting Nick's external sync)` and post a cross-agent note requesting the sync. This does NOT fail the closeout on its own, but every pending file must be listed in the cross-agent note so Nick can complete the mirror in one pass.
- **`differ` entries:** CONFLICTED — abnormal. A file exists in both locations with divergent content. This means either (a) the mirror was partially updated, (b) an older edit was made directly to the mirror, or (c) the source was rolled back but the mirror was not. Record `Dual skill-location sync check: CONFLICTED` and STOP the closeout. Escalate to Nick with `[BLOCKING]` severity before any forward work resumes.
- **`Only in .claude/skills/...` entries:** CONFLICTED. A file exists in the mirror that is not in the source. This should never happen under normal operation — escalate to Nick with `[BLOCKING]` severity.

**The PM never writes to `.claude/skills/`.** All edits go to the `ClaudeFolder/nexsys-hivemind/{coder,project-manager}/` source tree. Nick runs the external mirror sync. The PM's role is verification, not propagation.

### Step 11 — Inter-Agent Message Sweep

Confirm no unresolved `[OPEN-QUESTION]` or `[VERIFY-NEEDED]` entries in `nexsys-hivemind/context/open-questions.md` are blocking the next work unit. Confirm any `[FORESIGHT-NOTE]` entries in `nexsys-hivemind/context/handoff/coder-handoff.md §Foresight Notes` have been incorporated into the next brief or explicitly carried forward.

### Step 12 — Append WUCP Checklist to Review Output

At the bottom of the PM's review response, append:

```
## WUCP Phase 2: PM Closeout

- [x/ ] Freshness preflight: PASS / STALE-remediated
- [x/ ] Coder WUCP Phase 1 verified complete
- [x/ ] Traceability index updated: [module name] ([N] entries)
- [x/ ] Backlog updated: [work unit] marked DONE (commit, date)
- [x/ ] pm-handoff.md updated (Open Risks section current)
- [x/ ] pm-lessons.md appended: [summary or "No new patterns"]
- [x/ ] PROJECT_SNAPSHOT.md updated (timestamp: YYYY-MM-DD HH:MM UTC)
- [x/ ] Weekly plan updated for [work unit]
- [x/ ] Deferred build gate audit: [N open / N resolved this session]
- [x/ ] Drift check results:
  - MODULE_CONTEXT current: [yes / no — list gaps]
  - Traceability current: [yes / no — list gaps]
  - Backlog current: [yes / no — list gaps]
  - Handoff files current: [yes / no — list gaps]
  - Open Risks current: [yes / no — list gaps]
- [x/ ] Dual skill-location sync check: PASS (both diffs empty)
- [x/ ] Inter-agent message sweep: no blocking `[OPEN-QUESTION]`/`[VERIFY-NEEDED]`; `[FORESIGHT-NOTE]` entries carried forward.
- Timestamp: YYYY-MM-DD HH:MM UTC
```

---

## Cascade Protocols

### Weekly Closeout (end of each week)

All work-unit WUCPs from the week must be complete through Phase 2. Additionally:

1. **Weekly retrospective** written in the week plan file — what was planned vs. what happened, velocity observations, process adjustments
2. **PROJECT_SNAPSHOT** verified current with all work units completed that week
3. **Milestone backlog** verified — all DONE entries have commits and dates, next work units identified

### Monthly Closeout (last day of month)

1. **Monthly plan end-of-month update** written in `context/planning/months/YYYY-MM_month.md`
2. **Master release plan** checked for phase boundary drift
3. **Full context audit:** Every file in the Staleness Rules table (strategic-context-map.md §8) verified against its update obligation
4. **Accumulated technical debt** from deviations catalogued and prioritized

### Subsystem Closeout (when a subsystem reaches a major milestone)

1. **Velocity** recorded in `strategic-lessons.md` (estimated vs. actual time per work unit)
2. **Next subsystem's** work-unit sequence confirmed
3. **Phase transition check:** If the subsystem completes a phase gate, verify all gate criteria before advancing

---

## Failure Recovery

If the WUCP was not followed for a completed work unit (the scenario that caused this protocol to be generalized from the BCP on 2026-04-11):

1. **Identify the gap:** Which WUCP phases were skipped? Which artifacts are stale? Which build gates were never tracked?
2. **Retroactive closeout:** Run the skipped phases now, using the Coder's completion report and git history to reconstruct what was done
3. **Record the failure:** Append to the responsible agent's lessons log AND create an audit file under `context/audits/` if the gap was large enough to warrant forensics
4. **Timestamp all retroactive updates** with the actual date, not the work unit completion date, and note they are retroactive

---

## Quick Reference Card

**Coder — after compile gate passes (or is deferred):**
1. MODULE_CONTEXT.md for touched modules
2. coder-handoff.md (with Deferred Build Gate flag if applicable)
3. coder-lessons.md (if new patterns)
4. Cross-agent note (if needed)
5. WUCP Phase 1 checklist in Completion Report

**PM — after reviewing Coder output:**
1. Freshness preflight
2. Verify Coder Phase 1 complete
3. Traceability index for the module
4. Milestone backlog mark DONE
5. pm-handoff.md (including Open Risks)
6. pm-lessons.md (if new patterns)
7. PROJECT_SNAPSHOT.md
8. Weekly plan progress
9. Deferred build gate audit
10. Drift check (all artifacts)
11. Dual skill-location sync check
12. WUCP Phase 2 checklist in review output

---

## Symmetric Examples — Phase 2 Block vs. Phase 3 Milestone

The WUCP is phase-agnostic. The vocabulary changes but the obligations do not. Two parallel worked examples make the symmetry concrete.

### Example A — Phase 2 Block closeout (Block N, websocket-api)

**Coder Phase 1 (after compile gate GREEN):**

1. **MODULE_CONTEXT.md** — `homesynapse-core/api/websocket-api/MODULE_CONTEXT.md` populated with all 26 files, the `requires transitive com.homesynapse.api.rest` JPMS fix rationale, the nullable-collection defensive-copy pattern for `WsSubscriptionFilter`, and gotchas for subscription filter semantics.
2. **coder-handoff.md** — Block N marked complete; Block O flagged as next.
3. **coder-lessons.md** — Append entries for nullable collection defensive copies and JPMS `requires transitive` rule expansion.
4. **Cross-agent note** — Flag the JPMS rule expansion to PM so future block handoffs assume `requires transitive` by default.
5. **Completion Report** — Include the full WUCP Phase 1 checklist.

**PM Phase 2 (same session or next session):**

1. **Freshness preflight** — 10 checks; PASS required before forward work.
2. **Verify Coder Phase 1** — MODULE_CONTEXT populated, handoff updated, lesson logged, cross-agent note filed.
3. **Traceability index** — `homesynapse-core/docs/traceability/10-websocket-api.md` updated with all 26 types mapped to Doc 10 sections.
4. **Block backlog** — `phase-2-block-backlog.md` Block N row marked DONE with commit SHA. (Note: this backlog is FROZEN post-2026-03-20; retroactive corrections only.)
5. **pm-handoff.md** — Block N closed, Block O as next, any new Open Risks added.
6. **PROJECT_SNAPSHOT.md** — Completed Phase 2 blocks count incremented, Recent Session Log entry added.
7. **Drift check + dual skill-location sync check.**
8. **WUCP Phase 2 checklist** included in review output.

### Example B — Phase 3 Milestone closeout (M2.5, SqliteEventStore)

**Coder Phase 1 (after compile gate GREEN or deferred):**

1. **MODULE_CONTEXT.md** — `homesynapse-core/core/persistence/MODULE_CONTEXT.md` updated with `SqliteEventStore`, `TimeConversion`, `EventCategoryMapping`, V001 schema amendment note (`subject_type` column), category-CSV encoding gotcha, and the `DatabaseExecutor.readConnections()` accessor.
2. **coder-handoff.md** — M2.5 marked complete; M2.6 + M2.7 (combined) flagged as next. **If the build gate was deferred**, flag it with `[DEFERRED BUILD GATE]` and cite the commit of the last successful `./gradlew check`. This is the single entry that prevents another M2.2/M2.4-style latent violation.
3. **coder-lessons.md** — Append entries for `NO_DIRECT_TIME_ACCESS` rule scope (fires on test code too) and JUnit 5 `@BeforeEach` parent-first ordering exploitation.
4. **Cross-agent note** — Flag any working-copy anomalies discovered (like the M2.5 pre-truncated `build.gradle.kts`), and any pattern that will bite the next milestone.
5. **Completion Report** — Include the full WUCP Phase 1 checklist, every Deviation D-NN documented, and an explicit statement of whether `./gradlew check` ran or was deferred.

**PM Phase 2 (same session — retroactive Phase 2 is a governance failure):**

1. **Freshness preflight** — 10 checks; PASS required. The preflight is what catches the "my snapshot is 3 weeks behind" state that caused the 2026-04-11 arch-debt retrospective.
2. **Verify Coder Phase 1** — MODULE_CONTEXT populated, handoff updated with deferred-build-gate flag if applicable, lessons logged.
3. **Traceability index** — `homesynapse-core/docs/traceability/04-persistence.md` updated. (Stub indexes acceptable during Phase 3 catch-up batch.)
4. **Milestone backlog** — `phase-3-milestone-backlog.md` M2.5 row marked DONE with commit SHA, deviations documented.
5. **pm-handoff.md** — M2.5 closed, M2.6+M2.7 as next, **every deferred build gate logged in Open Risks** until Nick resolves it with a GREEN `./gradlew check`.
6. **pm-lessons.md** — Append entries for any new pattern (e.g., the "deferred build gate must be tracked as risk" governance lesson).
7. **PROJECT_SNAPSHOT.md** — Current milestone updated to NEXT, Recent Session Log entry added, file counts refreshed if they changed.
8. **Weekly plan** — Current week's plan file updated with the milestone completion.
9. **Deferred build gate audit** — If the Coder deferred the gate, do not mark the milestone DONE until Nick confirms GREEN. If an earlier deferred gate has gone unresolved for more than one session, open an audit under `context/audits/`.
10. **Drift check** — PROJECT_SNAPSHOT, milestone backlog, pm-handoff, MODULE_CONTEXT, and strategic-context-map.md must all agree on the current state.
11. **Dual skill-location sync check** — `diff -rq` between ClaudeFolder source and `.claude/skills/` mount must be empty (or STALE pending Nick's external mirror sync, which is the normal post-edit state).
12. **WUCP Phase 2 checklist** included in review output with every item PASS / FAIL / N/A.

### The symmetry rule

Every item in Example A has a counterpart in Example B. The only differences are:
- Phase 2 blocks update `phase-2-block-backlog.md` (frozen); Phase 3 milestones update `phase-3-milestone-backlog.md` (active).
- Phase 3 adds **deferred build gate tracking** (an explicit obligation that did not exist in BCP v1 and was the proximate cause of the M2.2/M2.4 latent violations).
- Phase 3 adds **Phase 3 Cross-Module Decisions register** cross-referencing in MODULE_CONTEXT.md updates when the milestone makes a cross-module decision worth recording.

Everything else — the freshness preflight, the drift check, the dual skill-location sync, the lessons log, the pm-handoff Open Risks section — applies identically to both phases.
