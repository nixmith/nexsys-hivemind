#!/bin/bash
# NexSys Hivemind — Directory Structure Setup
# Run from: ~/Desktop/Code/ClaudeFolder/nexsys-hivemind/
#
# This script creates the directory tree for a fresh hivemind checkout.
# It is idempotent — safe to run on an existing installation. It does NOT
# populate content; it only ensures the directory structure exists.
#
# Last updated: 2026-04-11 (hivemind overhaul — aligned to actual tree)

set -e

echo "Setting up NexSys Hivemind directory structure..."

# Agent skill directories (writable source of truth)
mkdir -p project-manager/references
mkdir -p coder/references

# Context subsystem — operational state (agents read/write)
mkdir -p context/status                  # PROJECT_SNAPSHOT.md — shared ground truth
mkdir -p context/planning                # master-release-plan, phase-N backlogs
mkdir -p context/planning/months         # monthly plans
mkdir -p context/planning/weeks          # weekly plans and retrospectives
mkdir -p context/handoff                 # pm-handoff, coder-handoff, cross-agent-notes
mkdir -p context/lessons                 # append-only lesson logs per agent
mkdir -p context/protocols               # WUCP and legacy BCP redirect
mkdir -p context/audits                  # retrospectives and audits
mkdir -p context/strategy                # Nick's strategy docs (read-only for agents)

echo ""
echo "Directory structure ready."
echo ""
echo "Directories created:"
echo "  project-manager/  coder/         — Agent skills (writable source)"
echo "  context/status/                  — PROJECT_SNAPSHOT.md"
echo "  context/planning/                — release plan + backlogs"
echo "  context/planning/months/         — monthly plans"
echo "  context/planning/weeks/          — weekly plans + retrospectives"
echo "  context/handoff/                 — handoff files + cross-agent notes"
echo "  context/lessons/                 — append-only lesson logs"
echo "  context/protocols/               — WUCP and related protocols"
echo "  context/audits/                  — retrospectives and governance audits"
echo "  context/strategy/                — Nick's strategy docs (read-only)"
echo ""
echo "Next steps:"
echo "  1. Create context/status/PROJECT_SNAPSHOT.md"
echo "  2. Create context/strategic-context-map.md at the context root"
echo "  3. Create context/protocols/work-unit-completion-protocol.md (WUCP)"
echo "  4. Populate context/strategy/ with Nick's strategy documents"
echo "  5. Clone repos as siblings to this directory:"
echo "     cd .. && git clone <url> homesynapse-core"
echo "     cd .. && git clone <url> homesynapse-core-docs"
echo "  6. The .claude/skills/nexsys-{coder,project-manager}/ mirrors are"
echo "     maintained by Nick's external sync — agents never write to them."
echo ""
echo "Notes on removed directories (2026-04-11 overhaul):"
echo "  - context/governance/   — moved to homesynapse-core-docs/governance/"
echo "  - context/design/       — moved to homesynapse-core-docs/design/"
echo "  - context/research/     — no longer used (strategy docs absorbed it)"
echo "  - context/queue/        — no longer used (task briefs go via direct"
echo "                            conversation; coding instructions live in"
echo "                            context/handoff/coder-handoff.md)"
echo "  - context/traceability/ — moved to homesynapse-core/docs/traceability/"
echo "  - hivemind/             — legacy agent directory, now unused"
echo ""
echo "Done."
