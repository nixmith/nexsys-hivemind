# NexSys / HomeSynapse Development Workflow Audit

**Auditor:** Claude (read-only inspection)
**Date:** 2026-05-01
**Scope:** nexsys-hivemind (every file), homesynapse-core (structure), homesynapse-core-docs (structure)

---

## Executive Summary

- The hivemind is a genuinely impressive context-engineering system — one of the most rigorous AI-agent governance setups I've seen. The two-agent architecture (PM + Coder) with shared context, lesson logs, handoff files, and a formal Work Unit Completion Protocol is well-conceived and has demonstrably caught real bugs (the M2.2/M2.4 arch-debt incident).
- **The system's biggest risk is its own staleness.** PROJECT_SNAPSHOT.md references M2.5 (Apr 11) but the repo HEAD is at M2.9 (Apr 15) — four milestones of drift. No weekly plan exists after W15 (Apr 6–12). No monthly plan exists for May. Both March and April end-of-month reports were never filled in. The weekly cadence that the April governance overhaul was designed to enforce has already lapsed.
- **Dead references to removed directories** persist in README.md, both CLAUDE.md files, and the strategic-context-map. The `context/queue/` directory was removed in the Apr 11 overhaul, but at least 6 files still reference it as if it exists, including session-start protocols that tell agents to check it.
- **homesynapse-core is healthy.** 588 Java files (30,441 main LOC, 17,808 test LOC), 146 test files, CI via GitHub Actions, 19 JPMS modules, all MODULE_CONTEXT.md files populated. Build is GREEN as of M2.9.
- **homesynapse-core-docs is healthy but under-governed.** 38,474 lines of markdown across 14 design docs, 6 amendments, 20+ research papers, governance artifacts. No CI, no README, no .gitignore at root.
- The three `.docx` strategy files in `context/strategy/` are effectively dead weight — Claude Code agents cannot read .docx natively, no agent protocol references them as required reading, and their content (revenue model, data strategy, institutional strategy) is summarized in the `.md` strategy files anyway.
- The PM and Coder skill files are coherent with each other and internally consistent. The Apr 11 overhaul successfully synchronized them. Minor drift exists in queue references that survived the overhaul.
- **Velocity is exceptional.** Phase 2 landed in 7 days against a 10-week budget. Persistence subsystem (M2.1–M2.9) landed 7+ weeks ahead of plan. The project is materially ahead of the 37-week master plan.
- **The governance layer is over-engineered relative to the team size** (solo developer + AI agents), but this is a deliberate and defensible choice given the 37-week timeline and the risk of context rot across hundreds of AI sessions.

---

## Hivemind Inventory Table

| # | File Path | Size (KB) | ~Tokens | Last Modified | Purpose | Actionable? | Issues |
|---|-----------|-----------|---------|---------------|---------|-------------|--------|
| 1 | `README.md` | 4.3 | 1,100 | Mar 24 | Top-level orientation for the hivemind repo | Stale | References removed dirs: `hivemind/`, `context/queue/`, `context/traceability/`. Directory tree diagram is wrong. |
| 2 | `setup.sh` | 3.4 | 870 | Apr 11 | Idempotent directory scaffold creator | Active | Correctly notes removed dirs in "Notes on removed directories" section, but doesn't create `context/decisions/` which exists. |
| 3 | `coder/CLAUDE.md` | 7.1 | 1,810 | Apr 11 | Coder agent identity, session protocol, file paths | Active | Lines 16, 86: references `../context/queue/instructions/` — directory doesn't exist. |
| 4 | `coder/SKILL.md` | 21.2 | 5,420 | Apr 11 | Complete behavioral spec for the Coder agent | Active | Core brain of the Coder. Well-structured. No stale references detected. |
| 5 | `coder/references/deviation-and-quality.md` | 16.1 | 4,120 | Apr 11 | Self-review checklist, deviation severity definitions, comment standards | Active | Working reference. Used at end of every coding task. |
| 6 | `coder/references/freshness-preflight.md` | 7.1 | 1,810 | Apr 11 | Session-start freshness checks for the Coder | Active | Newer than PM version. Checks are specific and actionable. |
| 7 | `coder/references/homesynapse-mental-model.md` | 18.0 | 4,610 | Apr 11 | System architecture mental model for the Coder | Active | Required reading before any coding. Comprehensive. |
| 8 | `coder/references/java-patterns.md` | 17.0 | 4,340 | Apr 11 | Java 21 coding patterns (ULIDs, sealed interfaces, virtual threads, SQLite, Jackson) | Active | Core reference. 11 sections covering all major patterns. |
| 9 | `coder/references/testing-standards.md` | 12.6 | 3,220 | Apr 11 | Test-first discipline, JUnit 5 patterns, ArchUnit rules | Active | Directly governs test output quality. |
| 10 | `project-manager/CLAUDE.md` | 6.6 | 1,690 | Apr 11 | PM agent identity, session protocol, file paths | Active | Lines 16-17, 81-82, 93: references `../context/queue/` — directory doesn't exist. |
| 11 | `project-manager/SKILL.md` | 27.5 | 7,030 | Apr 11 | Complete behavioral spec for the PM agent | Active | Core brain of the PM. Largest single file. Well-structured. |
| 12 | `project-manager/references/coding-instruction-format.md` | 16.1 | 4,130 | Apr 11 | Template and rules for PM → Coder coding instructions | Active | Defines the handoff format between agents. |
| 13 | `project-manager/references/constraint-enforcement.md` | 13.0 | 3,320 | Mar 24 | How PM enforces LTDs and invariants during review | Active | Older than other PM refs (Mar 24 vs Apr 11). May need refresh. |
| 14 | `project-manager/references/cross-subsystem-awareness.md` | 14.3 | 3,650 | Mar 16 | Cross-module dependency map for PM planning | Stale-risk | Oldest PM reference (Mar 16). Predates Phase 3 entirely. Module dependency details may not reflect M2.x additions. |
| 15 | `project-manager/references/freshness-preflight.md` | 11.2 | 2,860 | Apr 11 | Session-start freshness checks for the PM | Active | Different from Coder's version (PM-specific checks). |
| 16 | `project-manager/references/repo-state-protocol.md` | 11.7 | 3,000 | Mar 24 | How PM reads and interprets repo state | Active | Older (Mar 24). May not account for M2.6–M2.9 patterns. |
| 17 | `project-manager/references/review-and-quality.md` | 10.9 | 2,790 | Apr 11 | PM review checklist for Coder output | Active | Governs acceptance criteria. |
| 18 | `context/audits/2026-03-20_block-n-bcp-audit.md` | 27.8 | 7,110 | Mar 20 | Post-mortem of Block N (websocket-api) BCP execution | Historical | Valuable retrospective. Findings were acted upon. Now archival. |
| 19 | `context/audits/2026-04-11_m2.5-arch-debt-retrospective.md` | 11.2 | 2,870 | Apr 11 | Forensics on M2.2/M2.4 arch-rule violations | Historical | Critical incident doc. Led to WUCP and freshness preflight. Archival but referenced by current protocols. |
| 20 | `context/decisions/phase-3-cross-module-decisions.md` | 13.5 | 3,460 | Apr 11 | Register of 7 cross-module decisions made during Phase 3 | Active | Living document. Should be updated as M3+ decisions land. |
| 21 | `context/handoff/coder-handoff.md` | 5.4 | 1,390 | **Apr 16** | Coder session continuity — current task, next unit, deviations | **Freshest** | Most recently modified hivemind file. References M2.9 completion. |
| 22 | `context/handoff/cross-agent-notes.md` | 11.6 | 2,970 | Apr 11 | Shared bulletin board for inter-agent messages | Active | All notes currently archived (none active). Working as designed. |
| 23 | `context/handoff/pm-handoff.md` | 5.4 | 1,380 | Apr 11 | PM session continuity — current task, governance state | Stale | References M2.5 as latest. Repo is at M2.9. PM hasn't run since Apr 11. |
| 24 | `context/lessons/coder-lessons.md` | 24.3 | 6,220 | **Apr 16** | Append-only log of 26 coding discoveries | **Active** | Second-freshest file. Last entry from M2.9 session. Working as designed. |
| 25 | `context/lessons/pm-lessons.md` | 12.9 | 3,310 | Apr 11 | Append-only log of 9 PM discoveries | Active | Last entry from Apr 11 governance overhaul. No entries for M2.6–M2.9. |
| 26 | `context/lessons/strategic-lessons.md` | 25.7 | 6,580 | Apr 11 | Append-only log of 14 strategic discoveries | Active | Last entry from Apr 11. No entries since. |
| 27 | `context/planning/BLOCK_BACKLOG.md` | 0.1 | 35 | Apr 11 | Redirect to split backlogs | Active | One-liner redirect. Correct and minimal. |
| 28 | `context/planning/master-release-plan.md` | 34.6 | 8,860 | Apr 11 | 37-week roadmap (Mar 13 – Nov 25, 2026) | Active | Annotated with Phase 3 progress. Core planning artifact. Schedule annotations stop at M2.5. |
| 29 | `context/planning/months/2026-03_march.md` | 3.0 | 770 | Mar 14 | March monthly plan | **Incomplete** | End-of-month section never filled in: `[to be filled]` placeholders remain. |
| 30 | `context/planning/months/2026-04_april.md` | 4.6 | 1,190 | Apr 11 | April monthly plan | **Incomplete** | End-of-month section never filled in. Written Apr 11 but April isn't over yet — however, today is May 1 and it's still blank. |
| 31 | `context/planning/phase-2-block-backlog.md` | 6.1 | 1,560 | Apr 11 | FROZEN historical record of Phase 2 blocks A–S | Archival | Complete and frozen. All 17 blocks DONE. |
| 32 | `context/planning/phase-3-milestone-backlog.md` | 10.4 | 2,660 | Apr 11 | ACTIVE backlog for Phase 3 milestones | **Stale** | Lists M2.6+M2.7 as NEXT but M2.6–M2.9 have landed. Not updated since Apr 11. |
| 33 | `context/planning/weeks/2026-W12_mar13-mar22.md` | 13.3 | 3,410 | Mar 15 | Week 1 sprint plan + retrospective | Complete | End-of-week report filled in. Valuable velocity calibration data. |
| 34 | `context/planning/weeks/2026-W12b_mar16-mar22.md` | 8.9 | 2,270 | Mar 15 | Week 1b sprint plan (waves 2–3) | **Incomplete** | End-of-week section never filled in: `[to be filled]` placeholders remain. |
| 35 | `context/planning/weeks/2026-W13_mar23-mar29.md` | 2.3 | 590 | Apr 11 | Week 2 (retroactively reconstructed) | Complete | Marked as retroactive. Terse but accurate per git log. |
| 36 | `context/planning/weeks/2026-W14_mar30-apr05.md` | 2.2 | 560 | Apr 11 | Week 3 (retroactively reconstructed) | Complete | Marked as retroactive. Terse but accurate. |
| 37 | `context/planning/weeks/2026-W15_apr06-apr12.md` | 5.1 | 1,290 | Apr 11 | Week 4 (partially retroactive, partially forward) | Complete | Most detailed retroactive weekly. Covers the arch-debt incident well. |
| 38 | `context/protocols/block-completion-protocol.md` | 1.0 | 260 | Apr 11 | Redirect to WUCP | Active | Clean redirect with rationale. Correctly points to successor. |
| 39 | `context/protocols/work-unit-completion-protocol.md` | 24.8 | 6,360 | Apr 11 | Mandatory work-unit closeout protocol (Phase 1 + Phase 2) | Active | The governance backbone. Comprehensive and well-structured. |
| 40 | `context/status/PROJECT_SNAPSHOT.md` | 11.5 | 2,950 | Apr 11 | Shared ground-truth project status | **Stale** | References M2.5 as current. Repo HEAD is M2.9. Four milestones of drift. "Last updated: 2026-04-11." |
| 41 | `context/strategic-context-map.md` | 27.8 | 7,120 | Apr 11 | Master knowledge-base map for all agents | Active | Comprehensive routing document. References `queue/` directory (line 44, 197) which no longer exists. |
| 42 | `context/strategy/Revenue_Model_and_Licensing_Strategy.md` | 6.8 | 1,740 | Mar 9 | Revenue model and Apache 2.0 licensing rationale | Archival | Pre-development strategic document. Not referenced by any agent protocol. |
| 43 | `context/strategy/Six_Battlefields_MVP_Strategy.md` | 7.4 | 1,890 | Mar 9 | Competitive strategy (6 battlefields) | Archival | Pre-development strategic document. Not referenced by any agent protocol. |
| 44 | `context/strategy/From_Platform_to_Institution...docx` | 33.5 | ~8,600 | Mar 7 | Institutional strategy (Word doc) | **Dead weight** | .docx cannot be read by Claude Code agents. Never referenced as required reading. |
| 45 | `context/strategy/HomeSynapse_MVP_Data_Readiness...docx` | 26.2 | ~6,700 | Mar 7 | Data readiness specification (Word doc) | **Dead weight** | Same issue — unreadable by agents. |
| 46 | `context/strategy/NexSys_Data_Value_Engine...docx` | 28.9 | ~7,400 | Mar 7 | Data value engine strategy (Word doc) | **Dead weight** | Same issue — unreadable by agents. |
| 47 | `coder.zip` | 40.7 | — | Apr 11 | Packaged Coder skill for distribution | Active | Used for skill installation. Should be rebuilt if skill files change. |
| 48 | `project-manager.zip` | 44.4 | — | Apr 11 | Packaged PM skill for distribution | Active | Used for skill installation. Should be rebuilt if skill files change. |

**Totals:** 48 files. ~553 KB of markdown/shell content. ~141,000 estimated tokens across all readable files.

---

## Repo State Summary

### homesynapse-core

| Metric | Value |
|--------|-------|
| Total Java files | 588 |
| Main source LOC | 30,441 |
| Test source LOC | 17,808 |
| Test files | 146 |
| Test-to-main ratio | 0.58:1 (LOC), good for this stage |
| JPMS modules | 19 |
| MODULE_CONTEXT.md files | 19 (all populated) |
| Gradle convention plugins | 4 (java, library, application, test-fixtures) |
| CI | GitHub Actions (`ci.yml`) — `./gradlew check` on push to main/develop, PR to main |
| Build command | `./gradlew check` |
| Latest commit | `1bb8641` — M2.9: SqlitePersistenceLifecycle (Apr 15) |
| CLAUDE.md at root | **No** — has `CONTEXT.md` instead (2.1 KB) |
| AGENTS.md at root | **No** |
| .gitignore | Comprehensive and sane (Gradle, JVM, IDEs, secrets, runtime, Node, coverage) |
| Pre-commit hooks | **None** |
| Formatter config | **None visible** (.editorconfig, checkstyle, Spotless config not found at expected locations) |
| License | Proprietary (NexSys 2026) |

**Hygiene gaps:**
- No `CLAUDE.md` at repo root — agents rely on `nexsys-hivemind/coder/CLAUDE.md` instead, which is fine for the two-agent workflow but means a fresh Claude Code session opened directly in homesynapse-core has no orientation file.
- No `.editorconfig` or formatter enforcement. Code style consistency depends entirely on the Coder skill's `java-patterns.md` reference, which is AI-enforced, not tooling-enforced.
- No pre-commit hooks. Nothing prevents a human commit from violating ArchUnit rules or style conventions.
- CI is minimal — single job, no matrix testing, no coverage reporting, no artifact publishing.
- The `spike/` directory contains throwaway code that probably shouldn't be on `main`.

### homesynapse-core-docs

| Metric | Value |
|--------|-------|
| Total markdown LOC | 38,474 |
| Design documents | 14 (all Locked) |
| Amendments | 6 (AMD-25 through AMD-33) |
| Research papers | 20+ |
| Governance docs | 10+ |
| Latest commit | `f7919ab` (Apr 15) |
| CLAUDE.md at root | **No** |
| AGENTS.md at root | **No** |
| README.md at root | **No** |
| .gitignore at root | **Not found** |
| CI/CD | **None** |
| License | Present (`LICENSE` file) |

**Hygiene gaps:**
- No README.md — a docs repo with no README is ironic and makes onboarding harder.
- No .gitignore — OS files (.DS_Store, Thumbs.db) could leak into commits.
- No CI — no link checking, no spell checking, no markdown lint. For a project that cares deeply about documentation quality (the DAS writing standard is 285 lines), the docs repo has zero automated quality enforcement.
- Archive directory has a typo: `archive/benchmmarks/` (double 'm').

---

## Coherence and Drift Findings

### 1. Dead Queue References (Critical)

The `context/queue/` directory was removed in the Apr 11 overhaul. The `setup.sh` correctly documents it as removed. But **6 files still reference it as if it exists:**

| File | Lines | Reference |
|------|-------|-----------|
| `README.md` | 38, 75-76 | Directory tree shows `queue/`, workflow instructions reference `context/queue/briefs/` and `context/queue/instructions/` |
| `coder/CLAUDE.md` | 16, 86 | Session protocol says "Check `../context/queue/instructions/`"; Context Locations lists it |
| `project-manager/CLAUDE.md` | 16-17, 81-82, 93 | Session protocol says check queue; Context Locations lists both dirs; instruction output path references queue |
| `strategic-context-map.md` | 44, 197 | Lists `queue/` as part of context subsystem |

**Impact:** Every PM session starts by checking a directory that doesn't exist. Every Coder session does the same. This is a silent failure — the agents won't crash, they'll just get a "not found" and move on, but it's governance noise that erodes trust in the instructions.

### 2. Dead Directory References in README.md (Moderate)

README.md also references:
- `hivemind/` — "Strategic references (maintained by Nick)" — directory doesn't exist
- `context/traceability/` — "Design-to-code traceability indexes" — directory doesn't exist (moved to `homesynapse-core/docs/traceability/`)

The directory tree in README.md is materially wrong relative to actual structure.

### 3. PROJECT_SNAPSHOT Staleness (Critical)

| Field | Snapshot Value | Actual Value |
|-------|---------------|--------------|
| Current work unit | M2.5 (landed Apr 11) | M2.9 landed Apr 15 |
| Latest commit cited | `5279e7a` | `1bb8641` (8 commits later) |
| Last updated | Apr 11 | — |
| Days since update | 20 days | — |

The freshness preflight was designed to catch exactly this. Either it's not running, or sessions since Apr 11 haven't triggered it.

### 4. Phase-3 Milestone Backlog Staleness (Moderate)

The backlog lists M2.6+M2.7 as "NEXT (combined scope TBD by Nick)." In reality, M2.6 (SqliteCheckpointStore), M2.7 (SqliteViewCheckpointStore), M2.8 (AtomicCheckpointWriter), and M2.9 (SqlitePersistenceLifecycle) have all landed. The backlog doesn't reflect this.

### 5. PM/Coder Skill Coherence (Good)

The PM and Coder SKILL.md files are well-synchronized:
- Both reference the same WUCP protocol
- Both use the same deviation severity definitions
- Both reference MODULE_CONTEXT.md as authoritative
- The PM's coding-instruction-format.md aligns with what the Coder expects to receive
- The freshness preflight files are role-appropriate variants of the same concept

**Minor drift:** The PM's CLAUDE.md still references writing instructions to `context/queue/instructions/` (line 93), which contradicts the actual workflow where instructions go via `context/handoff/coder-handoff.md` or direct conversation.

### 6. Planning Cadence Breakdown (Critical)

| Artifact | Expected Cadence | Last Instance | Gap |
|----------|-----------------|---------------|-----|
| Weekly plan | Weekly | W15 (Apr 6–12) | **3 weeks missing** (W16, W17, W18) |
| Monthly plan | Monthly | April | **May missing** (today is May 1) |
| Monthly retrospective | End of month | Never completed | **Both March and April have `[to be filled]` placeholders** |
| W12b retrospective | End of week | Never completed | `[to be filled]` placeholders remain |

The Apr 11 governance overhaul explicitly identified the weekly planning gap as a governance failure and established the freshness preflight to prevent it. The same failure has recurred within 3 weeks.

### 7. Strategy .docx Files Are Inert (Low)

The three `.docx` files in `context/strategy/` (total 91 KB):
- Cannot be read by Claude Code agents (agents use `Read` tool which doesn't parse .docx)
- Are not referenced by any agent session protocol, SKILL.md, or CLAUDE.md as required reading
- Their content overlaps with the two `.md` strategy files (Revenue Model, Six Battlefields) which agents can read
- Last modified: March 7 — pre-development artifacts that have not been updated

These are Nick's strategic thinking artifacts stored for reference but never consumed by the agent system.

---

## Gaps a Senior Engineer Would Flag

### Process Gaps

1. **No automated staleness enforcement.** The freshness preflight is a document agents are asked to read and follow. There's no tooling that prevents a session from proceeding when PROJECT_SNAPSHOT is 20 days stale. A `pre-session.sh` script that checks file modification dates and emits warnings would be trivial and high-value.

2. **No `CLAUDE.md` in homesynapse-core.** The CONTEXT.md file exists but isn't the conventional name. A fresh `claude` session opened in the repo root won't auto-load it. Either rename to CLAUDE.md or symlink.

3. **No May planning artifacts.** Today is May 1. There is no May monthly plan and no W16+ weekly plans. The planning pipeline has stalled for 3 weeks.

4. **No code coverage reporting.** 146 test files exist but there's no JaCoCo or similar configured. Coverage percentage is unknown. For a project that targets "years of unattended operation on a Raspberry Pi," knowing coverage is essential.

5. **No dependency vulnerability scanning.** No Dependabot, no OWASP dependency-check, no Snyk. The Gradle version catalog exists but nothing audits it.

6. **No release/versioning strategy in the repo.** `version = "0.1.0-SNAPSHOT"` in build.gradle.kts but no versioning policy, no CHANGELOG, no release process documentation.

### Documentation Gaps

7. **homesynapse-core-docs has no README.** A documentation repository should be self-documenting.

8. **No onboarding document for a human contributor.** The hivemind is exhaustively documented for AI agents but there's no "Getting Started" guide for a human developer who isn't Nick. The `operations/pi5-developer-setup-guide.md` exists in core-docs but it's the only ops doc.

9. **No architecture decision records (ADRs) in homesynapse-core.** The `docs/` directory exists in the repo but ADRs live scattered across `homesynapse-core-docs/design/amendments/` and `nexsys-hivemind/context/decisions/`. A single canonical location would help.

### Tooling Gaps

10. **No formatter enforcement.** No .editorconfig, no Spotless, no Checkstyle. The Coder skill's `java-patterns.md` defines style rules but nothing machine-enforces them. A human commit could introduce style violations silently.

11. **No pre-commit hooks.** ArchUnit rules only run during `./gradlew check`. A pre-commit hook running a fast subset (compile + ArchUnit) would catch violations before they reach CI.

12. **No branch protection rules documented.** CI exists but there's no evidence of branch protection on `main` (required reviews, required CI pass). For a solo developer this is low-risk but becomes critical if a contributor is ever added.

---

## Specific Audit Questions Answered

### Q1: Which hivemind files are doing real work vs. just sitting there?

**Doing real work (read and acted upon regularly):**
- `coder/SKILL.md` + all 5 references — loaded every Coder session
- `project-manager/SKILL.md` + all 6 references — loaded every PM session
- Both `CLAUDE.md` files — session protocol
- `context/status/PROJECT_SNAPSHOT.md` — read at every session start
- `context/handoff/coder-handoff.md` — updated most recently (Apr 16)
- `context/handoff/cross-agent-notes.md` — checked every session
- `context/lessons/coder-lessons.md` — actively appended (26 entries)
- `context/protocols/work-unit-completion-protocol.md` — governs every milestone closeout
- `context/planning/phase-3-milestone-backlog.md` — tracks active work
- `context/decisions/phase-3-cross-module-decisions.md` — referenced during coding
- `context/strategic-context-map.md` — routing/index document

**Just sitting there:**
- `context/strategy/*.docx` (3 files) — never consumed by agents
- `context/strategy/*.md` (2 files) — rarely if ever referenced; pre-development artifacts
- `context/audits/2026-03-20_block-n-bcp-audit.md` — historical, findings already acted upon
- `context/planning/phase-2-block-backlog.md` — frozen Phase 2 record
- `context/planning/BLOCK_BACKLOG.md` — one-line redirect
- `context/protocols/block-completion-protocol.md` — redirect to WUCP
- `context/planning/weeks/2026-W12_mar13-mar22.md` and `W12b` — completed sprints
- `README.md` — stale orientation doc, not loaded by agents

**In between (should be active but aren't):**
- `context/planning/months/*.md` — cadence broken, end-of-month never filled
- `context/planning/weeks/W13-W15` — retroactively created, no new ones since
- `context/handoff/pm-handoff.md` — stale (Apr 11), PM hasn't run
- `context/lessons/pm-lessons.md` — no entries since Apr 11
- `context/lessons/strategic-lessons.md` — no entries since Apr 11

### Q2: Where is the same information stored in more than one place?

1. **Freshness preflight** exists in both `coder/references/freshness-preflight.md` and `project-manager/references/freshness-preflight.md`. These are intentionally different (role-specific) but share ~60% of their content. Changes to shared concepts must be made in both.

2. **Session protocol** is defined in both `CLAUDE.md` and `SKILL.md` for each agent. CLAUDE.md defines the file-loading order; SKILL.md defines behavioral rules. The boundary is clear but there's overlap in what they say about WUCP execution.

3. **Milestone status** is tracked in three places: `phase-3-milestone-backlog.md`, `PROJECT_SNAPSHOT.md`, and `coder-handoff.md`. All three have diverged — the handoff is freshest (M2.9), snapshot is at M2.5, backlog is at M2.5.

4. **Cross-module dependency knowledge** lives in `project-manager/references/cross-subsystem-awareness.md` AND in the MODULE_CONTEXT.md files in the repo AND in `context/strategic-context-map.md`. The cross-subsystem-awareness file (Mar 16) is the stalest of the three.

5. **The master release plan** (`master-release-plan.md`) and the **phase-3 milestone backlog** both track Phase 3 progress but with different granularity. Schedule annotations in the release plan also stop at M2.5.

### Q3: What's missing that a senior engineer would expect to see?

See "Gaps a Senior Engineer Would Flag" section above. Top items: code coverage, dependency scanning, formatter enforcement, CLAUDE.md in repo root, onboarding docs, release process.

### Q4: Are the PM and Coder SKILL.md files coherent with each other?

**Yes, substantially coherent.** The Apr 11 governance overhaul synchronized them. Both reference:
- The same WUCP protocol
- The same deviation severity framework ([INFO], [REVIEW], [SCOPE], [BLOCKING])
- MODULE_CONTEXT.md as the authoritative per-module reference
- The same freshness preflight concept (role-specific implementations)

**Minor drift:**
- PM CLAUDE.md still tells the PM to write instructions to `context/queue/instructions/`, but the actual workflow uses `coder-handoff.md` or direct conversation
- The PM's `cross-subsystem-awareness.md` (Mar 16) predates all Phase 3 work and may not reflect current module state

### Q5: Is the weekly cadence actually being maintained?

**No.** The cadence broke after W15 (Apr 6–12). No weekly plans exist for W16 (Apr 13–19), W17 (Apr 20–26), or W18 (Apr 27 – May 3). This is the same failure mode the Apr 11 governance overhaul was designed to fix. The freshness preflight was supposed to catch this, but either no PM sessions have run since Apr 11, or the preflight didn't trigger the planning artifact creation.

Additionally, W13 and W14 were retroactively reconstructed (not authored in real time), and W12b's end-of-week report was never filled in. Only W12 has a complete plan + retrospective cycle.

### Q6: Are the strategy .docx files ever consumed by Claude?

**No.** They are stored in `context/strategy/` but:
- Claude Code agents use the `Read` tool which returns raw bytes for .docx (not parseable text)
- No agent protocol, SKILL.md, CLAUDE.md, or freshness preflight references them as required reading
- The `strategic-context-map.md` lists strategy files but only names the `.md` ones as agent-readable
- Their content (revenue model, data strategy, institutional positioning) is either summarized in the `.md` strategy files or is Nick-facing strategic thinking that doesn't influence day-to-day coding

**Recommendation:** Convert the substantive content to markdown, or explicitly mark them as "Nick-only reference, not for agent consumption."

### Q7: What's the freshest meaningful artifact?

| Artifact | Date | Content |
|----------|------|---------|
| `coder-handoff.md` | Apr 16 | M2.9 completion, build gate GREEN |
| `coder-lessons.md` | Apr 16 | Last entry from M2.9 session |
| Repo HEAD (homesynapse-core) | Apr 15 | Commit `1bb8641` — M2.9 |
| Repo HEAD (homesynapse-core-docs) | Apr 15 | Commit `f7919ab` — research updates |
| PROJECT_SNAPSHOT.md | Apr 11 | M2.5 state (stale by 4 milestones) |
| Most recent weekly plan | Apr 11 | W15 (covers Apr 6–12, reconstructed) |

**Freshest meaningful artifact:** `coder-handoff.md` at **April 16, 2026** — 15 days ago.

### Q8: What's the staleness gap between PROJECT_SNAPSHOT and repo HEAD?

| Dimension | PROJECT_SNAPSHOT | Repo HEAD |
|-----------|-----------------|-----------|
| Date | 2026-04-11 | 2026-04-15 |
| Milestone | M2.5 | M2.9 |
| Commit | `5279e7a` | `1bb8641` |
| Commits behind | — | **8 commits** |
| Milestones behind | — | **4 milestones** (M2.6, M2.7, M2.8, M2.9) |
| Calendar gap | — | **4 days** (but 20 days since any hivemind update) |

The snapshot doesn't know about: SqliteCheckpointStore (M2.6), SqliteViewCheckpointStore (M2.7), AtomicCheckpointWriter (M2.8), or SqlitePersistenceLifecycle (M2.9). The entire persistence capstone is invisible to agents reading PROJECT_SNAPSHOT.

---

## Top 10 Highest-Leverage Improvements (Ranked by ROI)

### 1. Fix dead `queue/` references across 6 files
**Effort:** 30 minutes. **Impact:** Eliminates governance noise in every agent session. Every PM and Coder session currently encounters a phantom directory reference in their startup protocol.
*Files:* README.md, coder/CLAUDE.md, project-manager/CLAUDE.md, strategic-context-map.md

### 2. Update PROJECT_SNAPSHOT.md to M2.9 state
**Effort:** 20 minutes. **Impact:** Restores the shared ground-truth that every agent session reads first. Currently 4 milestones stale. This is the single highest-information-density file in the hivemind.

### 3. Update phase-3-milestone-backlog.md
**Effort:** 15 minutes. **Impact:** Reflects M2.6–M2.9 as DONE, identifies the actual next milestone. Currently tells agents that M2.6+M2.7 are "NEXT" when they're already complete.

### 4. Create May monthly plan + W16–W19 weekly stubs
**Effort:** 1 hour. **Impact:** Restores the planning cadence. The governance overhaul identified broken cadence as the root cause of drift; the cadence is broken again. Even minimal stubs with retroactive reconstruction (as done for W13–W14) would close the gap.

### 5. Rename `CONTEXT.md` to `CLAUDE.md` in homesynapse-core
**Effort:** 5 minutes. **Impact:** Any fresh Claude Code session opened in the repo will auto-load the orientation file. Currently requires manual discovery.

### 6. Convert strategy .docx files to .md (or delete them)
**Effort:** 30 minutes. **Impact:** Either makes 91 KB of strategic content agent-readable or removes dead weight that creates the illusion of maintained context.

### 7. Add JaCoCo coverage reporting to CI
**Effort:** 1–2 hours (Gradle plugin + CI artifact upload). **Impact:** Establishes a coverage baseline for a codebase that will eventually run unattended on embedded hardware. Currently coverage is unknown despite 146 test files.

### 8. Add `.editorconfig` + Spotless to homesynapse-core
**Effort:** 1–2 hours. **Impact:** Machine-enforces the code style that's currently only defined in prose (`java-patterns.md`). Prevents style drift from human commits or future contributors.

### 9. Fill in March and April end-of-month retrospectives
**Effort:** 45 minutes. **Impact:** These retrospectives are where velocity calibration happens. March was the calibration month (3–4x velocity surprise); that data exists in W12's retrospective but not in the monthly summary. April had the governance overhaul and the arch-debt incident. Capturing these makes the May plan more accurate.

### 10. Add a `pre-session.sh` freshness check script
**Effort:** 1 hour. **Impact:** Automates what the freshness preflight document asks agents to do manually. A script that checks modification dates of PROJECT_SNAPSHOT, weekly plans, and handoff files against configurable thresholds and emits warnings would prevent the exact class of staleness failures that have occurred twice now.

---

*Report generated 2026-05-01. All findings based on read-only inspection. No files were modified.*
