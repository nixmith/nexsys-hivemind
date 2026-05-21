# Nexsys Hivemind — Reorganization Plan

**Author:** Claude Code (Opus 4.7), Phase 2 design
**Date:** 2026-05-20
**Companion:** `AUDIT_2026-05-20.md` (Phase 1 findings — read first)
**Status:** Awaiting Nick's authorization. **No files will be modified until Nick explicitly approves.**

This plan is the artifact Nick reviews before authorizing destructive changes. Every numbered subsection below is a discrete proposal. Items can be approved individually, rejected, or amended. The "diff summary" at the end totals the expected scope.

---

## 0. Goals, Non-Goals, Operating Principles

**Goals (in priority order):**

1. **Eliminate per-session friction** caused by dead references and contradictions (queue/, traceability/ contradiction, stale "M3.x will be downstream").
2. **Constrain active-read budget.** Every file an agent reads at session start should fit ~3–5 min of reading. Hub files ≤ ~10K. Entry points ≤ ~5K.
3. **Introduce structure that survives the next 5 weeks.** Frontmatter, footers, single-source-of-truth assignments, eviction policies, and a typed-message protocol.
4. **Add the foresight layer.** Open Questions register and pre-WU verification artifacts to prevent the M3.6d-a 7-mismatch class of incident.
5. **No content loss.** Every byte removed from an active file lands in an archive file; nothing is deleted unless it's a true duplicate of a clearly-canonical source.

**Non-goals:**

- Not restructuring how the two source repos work.
- Not rewriting SKILL.md or CLAUDE.md from scratch — surgical edits only on those.
- Not changing the benchmarks directory structure or scoring history.
- Not touching .docx files.
- Not touching MODULE_CONTEXT.md files (out of scope).

**Operating principle I'll apply throughout this plan:** when in doubt between adding a new file and adding a section to an existing file, prefer the existing file. Each new file is a new lookup tax — the brief's principle 8.

---

## 1. Front-Matter Standard

### 1a. Proposed header block

Every `.md` file under `nexsys-hivemind/` (except `MEMORY.md`-style indexes if any, and benchmark answer-keys/scoring-history which are append-only ledgers) gets the following header. Block fits in ~80 tokens.

```markdown
<!--
file: <path-from-hivemind-root>
purpose: <one sentence, ≤ 18 words>
audience: <Coder | PM | Cowork | Nick | All>
update-cadence: <per-session | per-WU | per-milestone | per-week | per-month | ad-hoc | append-only | frozen>
state-type: <current | history | future | comms | reference>
status: <CURRENT | ARCHIVED | DEPRECATED>
last-verified: <YYYY-MM-DD against commit <SHA>>
-->
```

**Field semantics:**

- `audience`: who reads this at session start. If multiple, list comma-separated.
- `update-cadence`: how often the file should be touched. `frozen` means no further edits (e.g., `phase-2-block-backlog.md`). `append-only` means add-at-end-only, no reordering (e.g., lessons logs, scoring history).
- `state-type`: matches the brief's principle 3 separation.
  - `current` — what IS (snapshot, current handoff, current backlog row)
  - `history` — what WAS (archives, prior milestone closeouts, lessons)
  - `future` — what WILL BE (planning, design proposals)
  - `comms` — what's BEING COMMUNICATED (cross-agent notes, open questions)
  - `reference` — atemporal (skill references, governance, glossary)
- `status`: `ARCHIVED` and `DEPRECATED` are distinct — archived files are kept for history and should not be read at session start; deprecated files are kept as a back-compat redirect with a one-line pointer.
- `last-verified`: filled in by whoever edits the file substantively. State-dependent files also get a verification footer (§2).

### 1b. Example

```markdown
<!--
file: context/handoff/coder-handoff.md
purpose: Coder session continuity — current task, deferred build gate, next WU.
audience: Coder, PM
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# Coder Session Handoff
```

### 1c. Why HTML comments, not YAML frontmatter

Two reasons. (1) The SKILL.md files already have YAML frontmatter (the `name:` / `description:` pair is load-bearing for the skill system). Using HTML comments avoids any chance of collision or accidental parsing. (2) HTML comments render as nothing in any markdown viewer, including Cowork's preview and the Claude Project UI, so the headers don't add visual noise.

A `coder/SKILL.md` and `project-manager/SKILL.md` will gain a SECOND comment block immediately after their existing YAML frontmatter, not replace it.

### 1d. Files that get frontmatter

All .md files under `nexsys-hivemind/` (63 files) **except**:

- The two SKILL.md files keep their existing YAML AND get a comment block.
- `benchmarks/scoring-history.md` and `benchmarks/regression-bank/history.md` (per project brief — append-only ledgers, "don't restructure"). I'll add a `<!-- ... -->` block only if Nick wants it; default: skip.
- `benchmarks/answer-keys/category-d-reasoning.md` (treat as data; skip).

`.yaml`, `.docx`, and `.sh` files do **not** get frontmatter.

### 1e. Cost

Adding the header to ~58 files. ~50 added lines total. Pure additive, lowest risk. Suggested as Phase 3 Batch A.

---

## 2. Verification Footer Standard

### 2a. Proposed footer

Every file whose content depends on codebase state gets this one-line footer:

```markdown
---

**Last verified against:** `homesynapse-core` commit `<SHA>` on `<date>`.
```

If the file references multiple repos, list them.

### 2b. Why a footer in addition to the frontmatter

The frontmatter `last-verified` is metadata, easy to lie about. A visible bottom-of-file footer is a contract — a reader can tell at a glance whether the file is older than the codebase. When the file is read end-to-end (e.g., a PM pulling up `PROJECT_SNAPSHOT.md`), the footer is the last thing they see. It's the natural trigger for "verify-or-refresh."

### 2c. Files that get footers

State-dependent files only. My count: ~22 files.

- `PROJECT_SNAPSHOT.md`
- `Current_State.md` / `Locked_Decisions.md` / `Knowledge_Primer.md` / `Navigation_Index.md`
- `coder-handoff.md`, `pm-handoff.md`
- `strategic-context-map.md`
- `phase-3-milestone-backlog.md`
- All weekly plans (current/recent)
- All audit files (the SHA-at-time-of-audit is the verification)
- All MODULE_CONTEXT.md files — **out of scope** per brief, noting only for completeness.

Files that do **not** get footers:

- SKILL.md / CLAUDE.md / reference files (atemporal procedural content; principles 6 and 9 don't require a footer here, and adding one risks rapid invalidation — every codebase commit would technically stale them).
- Append-only ledgers (lessons logs, scoring history, regression-bank history).
- Strategy files (mostly atemporal product positioning).
- Frozen files (`phase-2-block-backlog.md`).

### 2d. How to set the SHA

The current HEAD as of last edit. `git rev-parse HEAD` output. If the PM updates two files in one closeout against the same commit, both get the same SHA. Files updated against an uncommitted working tree note that explicitly: `**Last verified against:** working tree at `25bc23b` + uncommitted edits` (rare case).

---

## 3. Single-Source-of-Truth Assignments

### 3a. DEC ledger (DEC-M3-NN)

**Canonical home:** `project-knowledge/HomeSynapse_Current_State.md` §3 (already canonical today).

**Mirror in `project-knowledge/HomeSynapse_Core_Locked_Decisions.md` §16:** keep — it's by design and acceptable. Update the mirror header to read:

> **Canonical home:** `HomeSynapse_Current_State.md §3 — M3 Locked Decisions Ledger`. This file mirrors only entries with cross-amendment or long-term locking significance (currently DEC-M3-16 and DEC-M3-17). Update both files when adding a new mirrored entry.

**Cross-module decisions in `context/decisions/phase-3-cross-module-decisions.md` (D-NN scheme):** keep — orthogonal scheme, different scope. The audit confirmed this is not a duplicate. Add a clarifying paragraph at the top explaining how D-NN relates to DEC-M3-NN.

**Rule for new entries:** new decisions go into one of the two registers based on type (milestone-locked → DEC-M3-NN in Current_State; cross-module implementation pattern → D-NN in cross-module-decisions). Pre-PR self-check: a decision with both flavors is rare and gets entries in both, cross-anchored.

### 3b. Milestone status (current WU, next WU)

**Canonical home:** `PROJECT_SNAPSHOT.md §Current Work Unit` and `§Phase 3 Implementation Status`.

**Mirrors (rewritten as cross-references):**

- `coder-handoff.md §Current Task` keeps Coder-specific state (current files modified, in-session deviations). For "what milestone is this?" it references `PROJECT_SNAPSHOT.md §Current Work Unit`.
- `pm-handoff.md §Current Task` keeps PM-specific state (Coding instructions outstanding, design-doc status changes). For milestone state it references `PROJECT_SNAPSHOT.md §Current Work Unit`.
- `phase-3-milestone-backlog.md` keeps the *full table* of milestones (this IS its canonical purpose) — but the "currently-NEXT" row should be the source for everyone, including PROJECT_SNAPSHOT.
- **Refinement:** `phase-3-milestone-backlog.md` is canonical for the *historical milestone roll-up* (DONE rows). `PROJECT_SNAPSHOT.md` is canonical for *current operational state*. Both should agree at all times, but their roles differ.

### 3c. Module status text (per-module type counts, recent changes)

**Canonical home:** `PROJECT_SNAPSHOT.md §Code State`.

**Mirror cleanup:** `strategic-context-map.md` and `Current_State.md` should reference rather than duplicate. Replace duplicated paragraphs with one-line pointers like "See `PROJECT_SNAPSHOT.md §Code State` for current type counts."

### 3d. Project state references

| Concept | Canonical home | Mirrors → become references |
|---|---|---|
| Current milestone | `PROJECT_SNAPSHOT.md §Current Work Unit` | coder-handoff, pm-handoff |
| Open Risks | `pm-handoff.md §Open Risks` (existing) | PROJECT_SNAPSHOT references it |
| Open Questions | `context/open-questions.md` (NEW — see §6) | pm-handoff cross-references |
| DEC-M3 ledger | `Current_State.md §3` | Locked_Decisions.md §16 (selective mirror) |
| D-NN cross-module | `context/decisions/phase-3-cross-module-decisions.md` | none |
| Module type inventory | `homesynapse-core/[mod]/MODULE_CONTEXT.md` (in source repo — out of scope) | PROJECT_SNAPSHOT.md §Code State references |
| LTD register | `project-knowledge/HomeSynapse_Core_Locked_Decisions.md` | strategic-context-map references |
| INV register | `project-knowledge/Architecture_Invariants_v1.md` | strategic-context-map references |
| Glossary | `homesynapse-core-docs/foundations/HomeSynapse_Core_v1_Glossary.md` (source-repo) | all .md files reference |
| Directory conventions | `context/canonical-paths.md` (NEW — see §8) | every CLAUDE.md and SKILL.md references |

### 3e. Skill-references duplication (freshness-preflight pair)

**Decision: keep both.** They share ~60% but role-specific deltas are real. Add an explicit "Shared protocol" anchor at the top of each so they reference each other:

```markdown
## Shared protocol
Outcome model (PASS/STALE/CONFLICTED) and response format are shared with the
[PM version](../../project-manager/references/freshness-preflight.md#shared-protocol).
Diverging here will cause drift — edit both together.
```

---

## 4. Eviction Policies for Oversized Files

### 4a. `coder-handoff.md` (70K → target ~12K)

**Active scope:** Most recent WU's full closeout block, plus the "Current Task" / "Next Work Unit" / "Build Status" / "Deferred Build Gate" sections at top.

**Eviction rule:**

- Inline: the *current* WU's full closeout (Files delivered, STOP Gate Results, Deviations, Lessons).
- Inline: a small "Recent prior WUs" summary table (~5 rows) — milestone, commit, date, one-line scope. Cross-reference the archive file for details.
- Move out: every prior WU's full body. Goes to `context/handoff/archive/coder-handoff-YYYY-MM.md` (one file per month, the body of every WU closed that month).

**Specific archive proposal for this rotation:** create `context/handoff/archive/coder-handoff-2026-05.md` containing M3.4a, M3.4b, Supervisor DLQ Wiring, Projection-Checkpoint Wiring, M3.5b, Bus-Fix Piece A, M3.5a, M3.3, M3.2, AMD-38/39, D1 spike, M2→M3 Bridge sections (everything from L283 downward in current `coder-handoff.md`). The active file keeps M3.6a/b/c/d-a inline because they all landed within the last 7 days and the next WU (M3.6d-b) depends on context from M3.6d-a directly.

**Rotation trigger:** at the next month boundary, or when the active file exceeds ~15K, whichever comes first. The PM does this in the next WUCP Phase 2 after the trigger.

**Cost:** one-time setup (move historical content). After that, the rotation is mechanical (a `cat ... >> archive/coder-handoff-YYYY-MM.md` operation).

**Estimated active file size after eviction:** ~12K (currently 70K → cut by ~83%).

### 4b. `pm-handoff.md` (39K → target ~10K)

Same pattern. Active file keeps:

- Current Task, Phase 3 Work Unit Status (top table — keep current)
- Outstanding Coding Instructions
- Unresolved Deviations
- Next Tasks
- Open Risks (active risks only — closed risks move to archive)
- Decisions Made This Session (current session only — older move to archive)
- Critical Path, Audit Findings Closure Update (current session)

Move out: every prior "PM Closeout" section block from "## M3.6c — PM Closeout" downward. Archive to `context/handoff/archive/pm-handoff-2026-05.md`.

**Estimated active file size after eviction:** ~10K (currently 39K → cut by ~75%).

### 4c. `coder-lessons.md` (56K → target ~25K)

**This is the most delicate eviction.** Lessons are referenced by future Coder sessions and the value isn't time-bounded the way handoff closeouts are. Cautious approach:

- Inline: lessons from the current major milestone group (M3.x) and the prior one (M2.x).
- Move out: lessons from Phase 2 (Blocks A–S, 2026-03-15 through 2026-03-20 entries — about 8 entries). Archive to `context/lessons/archive/coder-lessons-phase-2.md`.
- Move out: lessons from Phase 3 prep / M1.x (any 2026-03-27 through 2026-04-09 entries). Archive to `context/lessons/archive/coder-lessons-2026-04-m1-m2.md`.

After eviction, the active file holds 2026-04-10 onward (M2.5 arch-debt + M2.5/M2.9 entries + all of M3.x). Best estimate: ~25K, manageable.

**Rotation trigger:** at major-phase-group transitions (e.g., when M4 starts).

**Preservation guarantee:** every archived lesson is greppable from the same directory. Future sessions doing `grep -r "EVENT_BUS_DOES_NOT_IMPORT_SQLITE_DRIVER" context/lessons/` find it whether it's in the active or archive file.

### 4d. `strategic-lessons.md` (26K → target unchanged, fix cadence)

Not oversized. The issue is cadence (no entries since 2026-04-11). Either:

- Add catch-up entries for the M3 era (M3.1 prompt format, M3.6d sub-divide pattern, source-vs-brief class).
- Or document that strategic lessons now live elsewhere (Nick's claude.ai Project).

Recommended: catch-up entries. ~3 entries added.

### 4e. `cross-agent-notes.md` (18K → target ~10K)

Already has the archive separator mechanism. The current "Archived" section runs ~150 lines (most of the file). Two options:

- Leave as-is (the separator does the job — active is small).
- Move the entire archived section to `context/handoff/archive/cross-agent-notes-2026-Q1.md` and `-2026-Q2.md` and replace with a one-line breadcrumb.

Recommended: option 2 — the separator design is correct but the archived section has crossed 150 lines and is no longer useful in-file. Move it out. Active file becomes ~5K.

---

## 5. Inter-Agent Message Protocol

Currently inter-agent messages are unstructured prose. The proposal below introduces five typed message kinds. Each agent type knows how to react to each kind. Templates live in `context/canonical-paths.md` (the new file) or in a dedicated `context/handoff/MESSAGE_TEMPLATES.md` — Nick decides which (recommendation: include in canonical-paths).

### 5a. Message kinds

| Kind | Trigger | Author | Audience | Lives in | Expected action |
|---|---|---|---|---|---|
| `[OPEN-QUESTION]` | A factual question whose answer blocks or affects future work | PM or Coder | The other agent or Nick | `context/open-questions.md` (active section) | Recipient answers; question gets resolved + archived |
| `[VERIFY-NEEDED]` | A claim that should be checked against actual source before the next coding session uses it | PM or Coder | PM (typically) | `context/open-questions.md` (active section) | PM verifies before issuing the next instruction; result captured |
| `[DECISION-REQUESTED]` | A decision needed from Nick that has both engineering and strategic flavor | PM | Nick | `cross-agent-notes.md` (active) | Nick decides; PM logs the resolution |
| `[SCOPE-CHANGE-PROPOSED]` | The Coder discovers a brief's scope is wrong by ≥50% (e.g., M3.6d-a's 7 mismatches) | Coder | PM, Nick | `cross-agent-notes.md` (active) | PM evaluates; Nick approves sub-divide or re-scope |
| `[FORESIGHT-NOTE]` | The current WU implies non-obvious follow-up work that the next WU's brief should account for | Coder | PM | `coder-handoff.md §Foresight Notes` (new section) | PM reads when drafting the next brief |

### 5b. Template syntax

```markdown
## [OPEN-QUESTION] OQ-MM-NN — <one-line summary>
**Posed by:** <Coder | PM | Nick>
**Posed:** <YYYY-MM-DD>
**Blocking:** <which WU(s), or "none — informational">
**Question:** <full statement>
**Context:** <2–4 sentences — what triggered the question, what's been ruled out>
**Resolution:** _(filled in when resolved)_

---
```

Same pattern for `[VERIFY-NEEDED]` (substitute "Verify-target" for "Question"), `[DECISION-REQUESTED]` (substitute "Options" + "Recommendation"), `[SCOPE-CHANGE-PROPOSED]` (substitute "Original scope" + "Discovered gaps" + "Proposed split"), `[FORESIGHT-NOTE]` (just title + 2–4 sentences).

### 5c. ID schemes

- `OQ-MM-NN` for open questions: `OQ-05-01` = first open question opened in 2026-05.
- `VN-MM-NN` for verify-needed.
- `DR-MM-NN` for decision-requested.
- `SC-MM-NN` for scope-change-proposed.
- Foresight notes don't get IDs (they live inline in handoffs and rotate out with archives).

### 5d. Routing rules

- `[OPEN-QUESTION]` and `[VERIFY-NEEDED]`: live in `context/open-questions.md`. PM consults BEFORE issuing the next coding instruction. Coder consults BEFORE executing if any are flagged blocking-against-this-WU.
- `[DECISION-REQUESTED]` and `[SCOPE-CHANGE-PROPOSED]`: surface in `cross-agent-notes.md` (this matches the file's current design — bulletin board for inter-agent comms).
- `[FORESIGHT-NOTE]`: lives in `coder-handoff.md §Foresight Notes` (new section, positioned between "Build Status" and "Last Completed Milestone"). PM reads when drafting next brief.

### 5e. How the protocol shows up in CLAUDE.md / SKILL.md

The two CLAUDE.md files gain a short "Message Protocol" section listing the five kinds, where they live, and what action to take when they appear. ~12 lines each, surgical edit, no narrative restructure.

---

## 6. New Files

### 6a. `context/open-questions.md` (NEW)

**Purpose:** Running register of open questions and verify-needed items. PM consults before issuing instructions; Coder consults before executing.

**Initial content:** seed with current open items extracted from `pm-handoff.md` Open Risks:

- OR-M3-12 (RESOLVED — should still appear with `Resolution:` filled in, then archived to bottom)
- OR-M3-13 (active — reconciliation metadata feature gap)
- OR-M3-14 (active — M3.6d-b prerequisite infrastructure)

Format per §5b. ~3K total. Replaces the implicit Open Risks-as-open-questions pattern with an explicit dedicated surface.

Note: `pm-handoff.md §Open Risks` doesn't go away — it tracks build-gate deferrals and other risk items that aren't shaped like questions. Open Questions is the *foresight* surface; Open Risks is the *tracking* surface. Both are kept.

### 6b. `context/canonical-paths.md` (NEW)

**Purpose:** Single registry of directory and file-naming conventions. Every brief author references this before writing path references.

**Initial content:**

```markdown
# Canonical Paths Registry

## Hivemind directories
- Operational state: `context/`
- Status: `context/status/PROJECT_SNAPSHOT.md` (THE current-state hub)
- Handoff: `context/handoff/coder-handoff.md`, `pm-handoff.md`, `cross-agent-notes.md`
- Open questions: `context/open-questions.md`
- Lessons: `context/lessons/{coder,pm,strategic}-lessons.md`
- Planning: `context/planning/{master-release-plan.md, phase-3-milestone-backlog.md, weeks/, months/}`
- Decisions: `context/decisions/phase-3-cross-module-decisions.md`
- Protocols: `context/protocols/work-unit-completion-protocol.md`
- Audits: `context/audits/`
- Archives: `context/handoff/archive/`, `context/lessons/archive/`

## File naming
- Weekly plans: `weeks/YYYY-WNN_monDD-monDD.md` (e.g., `2026-W21_may18-may24.md`)
- Monthly plans: `months/YYYY-MM_month.md` (e.g., `2026-05_may.md`)
- Audits: `audits/YYYY-MM-DD_topic.md`
- Archives: `archive/<source-name>-YYYY-MM.md` (rotate at month boundaries)
- Design docs (homesynapse-core-docs): `design/NN-name.md` for the 14 core docs, `design/YYYY-MM-DD_topic.md` for ad-hoc

## Source repos
- homesynapse-core: `[module-group]/[module-name]/MODULE_CONTEXT.md` (one per module)
- homesynapse-core-docs: `design/`, `governance/`, `foundations/`, `research/`, `archive/`

## Inter-agent message kinds (see §Message Protocol in CLAUDE.md files)
- [OPEN-QUESTION], [VERIFY-NEEDED] → `context/open-questions.md`
- [DECISION-REQUESTED], [SCOPE-CHANGE-PROPOSED] → `cross-agent-notes.md`
- [FORESIGHT-NOTE] → `coder-handoff.md §Foresight Notes`

## Directories that NO LONGER EXIST (catch stale references)
- `context/queue/`, `context/queue/briefs/`, `context/queue/instructions/` (removed 2026-04-11 — task instructions flow via direct conversation and `coder-handoff.md`)
- `hivemind/` (legacy agent directory, removed 2026-04-11)
- `context/governance/`, `context/design/`, `context/research/` (moved to homesynapse-core-docs, removed 2026-04-11)
- `context/traceability/` for indexes (template only; real indexes live in `homesynapse-core/docs/traceability/`)
```

**Why this file:** every recurring path-inconsistency bug is rooted in a brief author not knowing the canonical convention. Centralizing the registry costs one file but eliminates one whole class of friction. The "directories that no longer exist" section is a particularly cheap defense against the queue/ residue recurring.

**Size:** ~3K.

### 6c. `context/pre-verifications/` (NEW directory)

**Purpose:** Pre-WU verification artifacts. The PM, before issuing a complex coding instruction, drops a short verification file here listing the actual source signatures the instruction depends on. The brief references this file. The Coder reads it before starting.

**Filename:** `pre-verifications/WU-<id>.md` (e.g., `pre-verifications/WU-M3.6d-b.md`)

**Initial state:** empty directory with a `README.md` explaining the convention. Optionally, seed with a worked example (`WU-M3.6d-b.md`) listing the OR-M3-14 prerequisites the PM has verified.

**Trigger:** the PM creates a pre-verification when (a) a WU touches ≥3 modules, OR (b) the brief depends on a class signature, method shape, or visibility level that's worth pinning to source before specifying. Single-module narrow WUs don't need this.

**Cost:** one new directory, one or two seed files, ~2K total.

### 6d. `context/handoff/archive/` (NEW directory)

For the eviction policy (§4). Initial contents: `coder-handoff-2026-05.md`, `pm-handoff-2026-05.md`, `cross-agent-notes-2026-Q1.md`, `cross-agent-notes-2026-Q2.md`. Each is the historical content extracted from the active file. README in the directory explains the rotation rule.

### 6e. `context/lessons/archive/` (NEW directory)

For coder-lessons eviction (§4c). Initial contents: `coder-lessons-phase-2.md`, `coder-lessons-2026-04-m1-m2.md`. README explains.

### 6f. Files NOT proposed (and why)

- A new top-level `INDEX.md` or `INVENTORY.md`. The `README.md` already serves orientation and the `strategic-context-map.md` is the routing hub. Adding another would be redundant.
- A separate `DECISIONS_INDEX.md`. The two existing ledger files plus the new canonical-paths.md cover discoverability. A third index would be a maintenance liability.
- A separate `OPEN_RISKS.md`. The existing `pm-handoff.md §Open Risks` is correctly placed (PM owns it). The new file is `open-questions.md` (different shape, foresight-focused).

---

## 7. Directory Restructuring

**Proposal: conservative.** Only the two new archive directories and the new `pre-verifications/` directory. No moves of existing directories.

**Rejected restructurings I considered:**

- Moving `context/strategy/` into `project-knowledge/strategy/`. Argument for: PM-Mode-1 reads strategy; project-knowledge is the upload zone. Argument against: strategy is intentionally NOT in the Claude Project upload — it stays local. Reject.
- Renaming `context/handoff/` to `context/comms/`. Argument for: matches the `state-type: comms` taxonomy. Argument against: bookmark cost, every reference in skills/refs/protocols needs updating. Reject.
- Promoting `project-knowledge/` to a sibling of `context/` rather than a top-level concern. Reject — current shape is fine.

---

## 8. Path Canonicalization Decisions

| Decision | Choice | Rationale |
|---|---|---|
| What to call the "instructions flow"? | `context/handoff/coder-handoff.md` (no separate queue) | Matches `setup.sh` and current practice |
| Where do governance findings file? | New: a section in `pm-handoff.md` (or `cross-agent-notes.md` if cross-agent) — NOT `../context/queue/briefs/` | Matches the `[DECISION-REQUESTED]` routing in §5 |
| Where do traceability indexes live? | `homesynapse-core/docs/traceability/[NN]-[module].md` | Matches current source-repo reality |
| Where does the template for traceability live? | `nexsys-hivemind/context/traceability/TEMPLATE.md` (unchanged) | Matches PM CLAUDE.md L85 |
| Weekly plan filename | `YYYY-WNN_monDD-monDD.md` | Current convention — keep |
| Archive filename | `archive/<source-name>-YYYY-MM.md` or `archive/<source-name>-YYYY-QN.md` for quarterly | New convention introduced here |

---

## 9. Skill File Refresh Scope

Both SKILL.md files encode hard-won discipline (preflight, refuse-to-close, deferred build gate, WUCP, dual-mirror sync, exception taxonomy, JPMS lessons). **Surgical edits only.** Specific line-level edits proposed:

### 9a. `project-manager/SKILL.md`

- **L139:** Replace the sentence "M1.x was test-first preparation, M2.x is the persistence subsystem, M3.x will be downstream subsystems." with "M1.x was test-first preparation, M2.x was the persistence subsystem, M3.x is the event-bus/state-projection/composition-root cohort (currently in execution). M4+ will be the downstream subsystems."
- No other edits proposed.

### 9b. `coder/SKILL.md`

- No edits proposed. The audit found no staleness here.

### 9c. `coder/CLAUDE.md`

- **L16:** Replace "Check `../context/queue/instructions/` for any instructions with status `PENDING`" with "Check `../context/handoff/coder-handoff.md` Current Task section for the next assignment, or wait for a direct task instruction in conversation."
- **L86:** Remove the `../context/queue/instructions/` line from the Context Locations list. Replace with: "Task instructions flow via `../context/handoff/coder-handoff.md` or direct conversation. The `context/queue/` directory was removed 2026-04-11."

### 9d. `project-manager/CLAUDE.md`

- **L16, L17:** Remove queue-check steps. Replace with: "Check `../context/handoff/cross-agent-notes.md` and `../context/open-questions.md` for outstanding messages requiring PM action."
- **L26:** Replace `../context/traceability/` (as index home) with `homesynapse-core/docs/traceability/`. (Brings it in line with L85.)
- **L82, L83:** Remove queue path lines from Context Locations.
- **L93:** Replace "When producing coding instructions, write them to `../context/queue/instructions/` using:" with "When producing coding instructions, deliver them via direct conversation to the Claude Code session (the current workflow), or append them to `../context/handoff/coder-handoff.md` Current Task section. The `context/queue/instructions/` directory was removed 2026-04-11."

### 9e. Reference files

- `coder/references/freshness-preflight.md` — add the §1c frontmatter, add a "Shared protocol" anchor cross-referencing the PM version. No other edits.
- `project-manager/references/freshness-preflight.md` — same.
- `project-manager/references/constraint-enforcement.md` L185 — replace `../context/queue/briefs/` reference with the new flow (file the finding as `[DECISION-REQUESTED]` in `cross-agent-notes.md` or escalate to Nick in conversation).
- `project-manager/references/review-and-quality.md` L191 — replace `../context/traceability/` reference with `homesynapse-core/docs/traceability/`.
- `project-manager/references/repo-state-protocol.md` — reconcile 19-vs-20 module count phrasing (one-line clarification).
- `project-manager/references/cross-subsystem-awareness.md` — minor: clarify 14-vs-13+1 subsystem-count phrasing if Nick wants. Optional.
- `project-manager/references/coding-instruction-format.md` — no edits required. (Audit found no staleness.)
- `coder/references/{deviation-and-quality, homesynapse-mental-model, java-patterns, testing-standards}.md` — no edits required.

### 9f. WUCP (`context/protocols/work-unit-completion-protocol.md`)

- **L177–178:** Change traceability index home from `nexsys-hivemind/context/traceability/[NN]-[module-name].md` to `homesynapse-core/docs/traceability/[NN]-[module-name].md`. (Bring WUCP in line with the established convention.)
- **L248:** Same fix in the Drift Check table row.
- **L266–267:** Replace hardcoded `/sessions/awesome-admiring-clarke/...` with path-traversal pattern matching the freshness-preflight files.
- Add `[OPEN-QUESTION]` / `[VERIFY-NEEDED]` / `[FORESIGHT-NOTE]` handling references in Phase 1 and Phase 2 step lists (one or two lines).

### 9g. `README.md` (top level)

- Replace the stale directory tree with current reality (no `hivemind/`, no `queue/`, no `traceability/`).
- Replace the workflow section (lines 72–80) with: "Nick gives tasks directly to the PM (in claude.ai or via Claude Code), and the PM gives instructions to the Coder (in conversation or by appending to `coder-handoff.md`). The `queue/` directory was removed 2026-04-11; instructions no longer use a file-based queue."
- Add `[OPEN-QUESTION]` / `[VERIFY-NEEDED]` / `[FORESIGHT-NOTE]` overview pointing to canonical-paths.md.

### 9h. `strategic-context-map.md`

- **L17, L109, L342:** Update M3.6c-as-next references to M3.6d-b-as-next.
- **L200:** Replace `queue/` description block with: "**Task flow:** Direct conversation (Nick → PM, PM → Coder), supplemented by `coder-handoff.md` for asynchronous handoff. The legacy `context/queue/` directory was removed 2026-04-11."

---

## 10. Risk Register

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| **Frontmatter mass-add introduces a parsing error** | Low | Low | Frontmatter is HTML comments — markdown viewers ignore them. Worst case: a stray `-->` mid-file. Sanity check during Batch A: grep for `-->` count, should equal frontmatter count. |
| **Eviction archives lose searchability** | Low | Medium | The archived files live in the same directory tree and are .md format. `grep -r` finds content equally well. Verify by running a grep for a known archived lesson after eviction. |
| **Cross-reference fix-up misses a file** | Medium | Low | Phase 4 verification (next chapter) does `grep -r "context/queue"` across the directory and reports any remaining matches. |
| **Skill-file surgical edit accidentally changes load-bearing discipline** | Low | High | Edits are line-numbered and explicit (§9). Each is a single-line substitution, not a rewrite. Diff review by Nick before commit. |
| **New `open-questions.md` becomes another file nobody reads** | Medium | Low | Explicitly named in both CLAUDE.md session protocols (§9c, §9d), so it's loaded every session. Watch for cadence drift in the first 2 PM sessions after rollout. |
| **`pre-verifications/` directory becomes work-for-its-own-sake** | Medium | Low | Trigger condition is narrow (≥3 modules OR signature-dependent specifics). Most WUs will skip it. The seed example for WU-M3.6d-b is justified — it directly addresses OR-M3-14. |
| **DEC ledger drift after mirror canonicalization** | Low | Medium | The mirror update header explicitly states the rule ("update both"). PM owns this; verifies in WUCP Phase 2 drift check. |
| **Nick's claude.ai Project uploads get out of sync after eviction** | Medium | Medium | Files in `project-knowledge/` are uploaded to the Project. None of the eviction targets are in `project-knowledge/`. Safe. |
| **A reorganization batch breaks an external bookmark or script** | Low | Low | The only external consumers are Nick's own habits and the `.claude/skills/nexsys-*` mirror. Mirror sync runs every WUCP Phase 2; will catch drift. Bookmarks are Nick's problem. |
| **Mass edits make `git diff` unreadable** | Medium | Low | Working in batches (§Batches in Phase 3 below) keeps each diff focused. Nick can review one batch at a time. |

**Rollback plan:** Since the repo is not a git repo (confirmed in Phase 1), there's no native rollback. **Strong recommendation:** before Phase 3 begins, copy the entire `nexsys-hivemind/` directory to `nexsys-hivemind-backup-2026-05-20/` as a safety net. If any batch produces an unwanted result, the backup is the restore point. This is cheap insurance (a few MB) and is the cleanest rollback for a non-git working tree.

Alternative: `git init` the hivemind directory before Phase 3 — gives a per-batch rollback granularity. Nick decides; the backup approach is sufficient.

---

## 11. Diff Summary

The numbers below count *files touched*, not lines or hunks. They include the new files this plan proposes.

| Change category | Files | Notes |
|---|---|---|
| **Modified** | ~30 | Headers added to ~58 files (across multiple batches); but each file is modified at most twice (once for header, once for content fix). The "Modified" count is unique files. |
| **Created** | ~10 | `AUDIT_2026-05-20.md` (already created), `REORGANIZATION_PLAN_2026-05-20.md` (this file), `context/open-questions.md`, `context/canonical-paths.md`, `context/pre-verifications/README.md`, `context/pre-verifications/WU-M3.6d-b.md` (seed example), `context/handoff/archive/coder-handoff-2026-05.md`, `context/handoff/archive/pm-handoff-2026-05.md`, `context/handoff/archive/cross-agent-notes-2026-Q1.md`, `context/handoff/archive/cross-agent-notes-2026-Q2.md`, `context/lessons/archive/coder-lessons-phase-2.md`, `context/lessons/archive/coder-lessons-2026-04-m1-m2.md`. |
| **Archived (renamed, content moved)** | ~1 | Top-level `AUDIT_REPORT.md` (2026-05-01) moves to `context/audits/2026-05-01_workflow-audit.md` with a one-line breadcrumb at the top level if Nick prefers. Or simply delete the top-level copy — its findings are superseded by this audit. |
| **Renamed** | 0 | No renames proposed beyond the AUDIT_REPORT archival. |
| **Deleted** | 0 | No deletes. |

**Total: ~30 modified, ~10 created, ~1 archived, 0 renamed, 0 deleted.**

**Top 5 highest-impact changes (for Nick's at-a-glance approval):**

1. Fix all dead `context/queue/` references in 6 files (≤11 lines edited).
2. Add `context/open-questions.md` + seed OR-M3-13 and OR-M3-14 as `[OPEN-QUESTION]` entries.
3. Evict 80%+ of `coder-handoff.md` and 75%+ of `pm-handoff.md` to `archive/` (~110K → ~22K active).
4. Add canonical-paths.md registry to make every brief author path-correct by construction.
5. Fix `project-manager/SKILL.md` L139 stale "M3.x will be downstream" claim.

These five alone capture ~80% of the value. Phase 3 batches A–C cover them. Batches D–H are progressively lower priority — Nick can stop after any batch.

---

## 12. Proposed Execution Order (Phase 3 Batches)

If authorized, the work runs in the following batches. Each batch is one cohesive `git diff` for Nick to review. After each batch I'll pause and let Nick inspect before proceeding.

- **Batch A — Frontmatter standardization (~58 files).** Pure additive HTML-comment headers. Low risk. Single git diff, easy to review.
- **Batch B — Verification footers (~22 files).** Same risk profile.
- **Batch C — Path fixes / queue residue elimination.** README.md, both CLAUDE.md, both freshness-preflight files (no edits needed but verified), constraint-enforcement.md L185, review-and-quality.md L191, strategic-context-map.md L200, WUCP L177–178 + L266–267, project-manager/SKILL.md L139. Surgical line-level edits.
- **Batch D — New files: canonical-paths.md, open-questions.md (with OR-M3-13/14 seeded), pre-verifications/ directory + WU-M3.6d-b.md seed.** All additive.
- **Batch E — Archive directories created and historical content moved.** `coder-handoff.md`, `pm-handoff.md`, `cross-agent-notes.md` content extracted to `archive/`. Active files trimmed.
- **Batch F — `coder-lessons.md` eviction.** Highest-risk eviction; do last among evictions. Phase 2 + M1.x lessons move to archive.
- **Batch G — Cross-reference fix-up + skill-file message-protocol additions.** Coder/PM CLAUDE.md gain Message Protocol sections referencing canonical-paths and open-questions.
- **Batch H — `AUDIT_REPORT.md` (May 1) archival** + final verification (Phase 4).

Each batch is a single `git status` + `git diff --stat` check, then I pause for Nick's review.

---

## 13. Coder Discretion Areas — Items I'd Like Nick's Explicit Steer On

A few items are judgment calls. Nick's preferred resolution affects the plan:

1. **Archive `AUDIT_REPORT.md` (May 1) vs delete.** Its findings have been carried into this audit. Archive is safe; delete is cleaner. *My recommendation: archive at `context/audits/2026-05-01_hivemind-workflow-audit.md` (rename to fit the audit naming convention).*
2. **W16–W20 weekly-plan gap.** Retroactively reconstruct (mirror the W13/W14/W15 retroactive approach), or document that the cadence has shifted from weekly-plans-as-primary to milestone-cadence-as-primary? *My recommendation: document the shift in `strategic-context-map.md §8` and leave the gap as-is.*
3. **`strategic-lessons.md` cadence.** Add catch-up entries or document the cadence shift? *My recommendation: add 3 catch-up entries (M3 prompt patterns, M3.6d sub-divide pattern, source-vs-brief mismatch class).*
4. **Whether to `git init` the hivemind.** Brings per-batch rollback granularity. Adds GitHub commitment if pushed; no need to push. *My recommendation: yes, `git init` only locally (no remote), with `.gitignore` for `archive/` if Nick wants archives untracked.*
5. **Where to file governance findings (replacement for `../context/queue/briefs/`).** Options: (a) `cross-agent-notes.md` as `[DECISION-REQUESTED]`, (b) `pm-handoff.md §Escalations`, (c) a new `context/escalations.md` file. *My recommendation: option (a) — cross-agent-notes already handles this and has the archive separator.*
6. **Move this file (REORGANIZATION_PLAN_2026-05-20.md) to `context/audits/` after authorization?** Or keep it top-level alongside AUDIT_2026-05-20.md? *My recommendation: move both AUDIT_2026-05-20.md and REORGANIZATION_PLAN_2026-05-20.md to `context/audits/` once Phase 4 verification completes — the top level should only hold `README.md` and `setup.sh`.*

---

**Plan complete. Awaiting Nick's authorization to proceed to Phase 3. No files in `nexsys-hivemind/` will be modified beyond `AUDIT_2026-05-20.md` and `REORGANIZATION_PLAN_2026-05-20.md` until Nick explicitly authorizes.**

**Last verified against:** `homesynapse-core` HEAD `25bc23b` (M3.6d-a, 2026-05-20). Hivemind file inventory captured 2026-05-20.
