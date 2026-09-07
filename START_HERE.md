<!--
file: START_HERE.md (nexsys-hivemind root — the canonical front door; a thin pointer copy sits at ClaudeFolder/START_HERE.md)
purpose: Cold-boot entry point for a Claude instance with ZERO conversational memory. Everything needed to become a productive agent in this system is on disk; this file tells you where the thread starts.
audience: Any fresh Claude (Cowork hub, Claude Code lane, or Cowork lane); Nick.
state-type: reference (deliberately state-free — pointer-not-copy)
status: CURRENT
last-verified: 2026-09-07 (HIVE-CLEAN-1 lane — every pointer re-checked on disk after the hygiene pass: the standing prompt is the STABLE v67 form (one non-archived file; retired versions in `context/handoff/archive/prompts/`); the operator's entry = the newest `*_OPERATOR-BRIEF_for-Nick.md` §HELD; lane dispatches live in `context/instructions/` (executed ones in its `archive/`); the archive convention is registered in `context/canonical-paths.md`. All process/spine paths in §Boot resolve.) Prior: 2026-07-04 (v19 hub, currency pass — FULL read: pointer-cleanliness HELD (the file is deliberately state-free; zero stale claims found); the PM launch line verified against Nick's actual v19 launch (matched the template verbatim); no content edits needed)
-->

# START HERE — cold boot for a memory-less Claude

You are joining the NexSys / HomeSynapse development system. **Nothing you need lives in anyone's memory. The repositories ARE the memory.** Trust files over recollection, the spine over summaries, and source over every document (`nexsys-hivemind/context/process/truth-hierarchy-and-pointer-not-copy-discipline.md`).

## Boot sequence (in order, no steps skipped)

1. **Identify your role** from Nick's launch line (below). Load the matching skill: `nexsys-project-manager` (PM/orchestrator hub — Cowork) · `nexsys-coder` (implementation — usually Claude Code) · `nexsys-frontend` (web-UI/website/brand lanes — Cowork).
2. **Read the standing orchestrator prompt** — the NEWEST file matching `nexsys-hivemind/context/handoff/*_PM-mission-control_v*_orchestrator_session_prompt.md` that is NOT in `archive/`. Since v67 (2026-09-06) this is the STABLE prompt — one file, the laws by reference; it boots on the newest `context/handoff/*_OPERATOR-BRIEF_for-Nick.md` (§HELD = the operator's wait-state ledger and Nick's entry point) + the newest spine beat. Lane agents instead read the dispatch Nick names (in `context/instructions/`). **The archive convention (2026-09-07):** an executed prompt/instruction/packet lives in its directory's `archive/` with an `EXECUTED`/`SUPERSEDED` status prefix; a cited path not found is looked up in `<dir>/archive/` (`context/canonical-paths.md` § The archive convention).
3. **Run your skill's freshness preflight before any work.** The PM's 11-check preflight re-derives all volatile state (HEADs, milestone status, watermark, counts) from source. Never trust a masthead's state claims — including this file's.
4. **Read the operating context** (the PM skill mandates these; lanes read what their dispatch names): `context/process/cowork-environment-model.md` (the paid-for environment rules — path duality, mount lag, git locks, anchor hygiene) · `context/process/working-with-nick.md` (the operator contract) · `context/process/infrastructure-map.md` (repos, remotes, CI, toolchain) · `context/process/decision-rationale-index.md` (why the big rulings are what they are).
5. **Then work the loop** your skill and the standing prompt define. The spine files (`context/status/PROJECT_SNAPSHOT.md`, `context/handoff/pm-handoff.md`, `context/handoff/coder-handoff.md`, `context/handoff/cross-agent-notes.md`) are the single source of operational truth; the hub is the single spine-writer.

## Nick's launch lines (copy-paste)

- **PM hub (Cowork):** `Follow all instructions in nexsys-hivemind/context/handoff/<newest v*_orchestrator_session_prompt>.md — /nexsys-project-manager`
- **Coder lane (Claude Code, in homesynapse-core):** `Read nexsys-hivemind/context/instructions/<named instruction>.md and its pre-verification, then execute — /nexsys-coder`
- **Frontend/research/hygiene lane (fresh Cowork):** `Read nexsys-hivemind/context/instructions/<named lane dispatch>.md WHOLE and execute it — /nexsys-frontend` (or the role the dispatch names)

## The one-paragraph orientation

HomeSynapse is a local-first, event-sourced smart-home OS (Java 21, JPMS, SQLite, Gradle) built as long-lived infrastructure by NexSys (Nick, founder). Five repos under `ClaudeFolder/`: `homesynapse-core` (the product), `homesynapse-core-docs` (design docs, governance, website), `nexsys-hivemind` (the shared brain — protocols, spine, lessons, instructions), `nexsys-bench` (the hardware test-and-truth engine), `nexsys-skills` (skill sources beyond coder/PM). Everything runs through: Locked design docs → PM coding instructions → lane implementation → Nick's host-side build gate (CI is the gate of record) → two-layer hub audit → spine record. Work units aren't done until WUCP Phase 1 (lane) AND Phase 2 (PM) complete. Nick rules strategy; the hub owns "how"; lanes are write-isolated; nobody commits except Nick.
