<!--
file: README.md
purpose: Top-level orientation to NexSys's two-agent (PM + Coder) development system and directory layout.
audience: All
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# NexSys Development System — Two-Agent Architecture

Two agents working in a chain of command to develop HomeSynapse Core with engineering rigor and quality control at every layer. Nick (founder) handles strategic direction directly via claude.ai Projects.

## Architecture

```
Nick (Founder) ──► Project Manager ──► Coder
  Strategy          project-manager/     coder/
  Task briefs       Architecture         Implementation
  (claude.ai)       Design docs          Tests + code
                    Interface specs
                    Coding instructions
```

Each agent has:
- `CLAUDE.md` — Role identity, session protocol, file paths
- `SKILL.md` — Complete behavioral specification (the "brain")
- `references/` — Detailed reference files loaded on demand by the skill

## Directory Structure

```
~/Desktop/Code/ClaudeFolder/
├── nexsys-hivemind/              ← This directory
│   ├── project-manager/          ← PM agent
│   ├── coder/                    ← Implementation agent
│   └── context/                  ← Shared knowledge base
│       ├── strategy/             ← Business docs
│       ├── status/               ← PROJECT_SNAPSHOT.md — shared ground-truth
│       ├── planning/             ← Release plan, monthly plans, weekly plans
│       │   ├── master-release-plan.md
│       │   ├── months/           ← Monthly plans with end-of-month updates
│       │   └── weeks/            ← Weekly plans with day-by-day + retrospectives
│       ├── lessons/              ← Append-only lesson logs (PM, Coder, strategic)
│       ├── handoff/              ← Session continuity files + cross-agent notes
│       ├── traceability/         ← TEMPLATE.md only (real indexes in homesynapse-core/docs/traceability/)
│       └── protocols/            ← Block Completion Protocol
├── homesynapse-core/             ← Code repo (clone here)
└── homesynapse-core-docs/        ← Docs repo (clone here)
```

## Setup

### 1. Run the setup script
```bash
cd ~/Desktop/Code/ClaudeFolder/nexsys-hivemind && bash setup.sh
```

### 2. Populate context files
Copy your existing project documents into the appropriate `context/` subdirectories.

### 3. Clone repos (when ready)
```bash
cd ~/Desktop/Code/ClaudeFolder
git clone <core-repo-url> homesynapse-core
git clone <docs-repo-url> homesynapse-core-docs
```

## Usage

### Claude Code (separate terminals or sessions)
```bash
cd ~/Desktop/Code/ClaudeFolder/nexsys-hivemind/project-manager && claude
cd ~/Desktop/Code/ClaudeFolder/nexsys-hivemind/coder && claude
```

### Workflow
Nick maintains strategic context and produces task briefs via claude.ai Projects. The PM and Coder operate as Claude Code agents.

Nick gives tasks directly to the PM (in claude.ai or via Claude Code), and the PM gives instructions to the Coder (in conversation or by appending to `coder-handoff.md`). The `queue/` directory was removed 2026-04-11; instructions no longer use a file-based queue. Inter-agent messages use the typed protocol (`[OPEN-QUESTION]`, `[VERIFY-NEEDED]`, `[DECISION-REQUESTED]`, `[SCOPE-CHANGE-PROPOSED]`, `[FORESIGHT-NOTE]`); see `context/canonical-paths.md` for routing.

### Session Continuity
Each agent reads/writes a handoff file in `context/handoff/` to maintain continuity across sessions. The CLAUDE.md files instruct agents to read their handoff file at session start and update it at session end. Agents also read `context/status/PROJECT_SNAPSHOT.md` for instant project orientation and check `context/handoff/cross-agent-notes.md` for inter-agent messages.

### Planning & Tracking
Weekly plans in `context/planning/weeks/` provide day-by-day breakdowns and end-of-week retrospectives. Monthly plans in `context/planning/months/` track phase-level progress. The master release plan defines the 37-week roadmap to launch. Agents read the current week's plan at session start for context on active work.

### When to Skip the Chain
- **Direct to PM:** Specific technical task that doesn't need strategic decomposition
- **Direct to Coder:** Fully specified, narrow coding task
- **Never skip for:** Architecture decisions, scope changes, new subsystems, locked decision changes
