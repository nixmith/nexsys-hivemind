<!--
file: context/strategic-context-map.md
purpose: Map of the entire NexSys knowledge base; routes agents to the right context before acting.
audience: All
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# Strategic Context Map

This is the NexSys development system's map of the entire knowledge base. Use it to quickly locate relevant context before acting on any request. Nick maintains strategic context via claude.ai Projects; the PM and Coder use this map for operational context.

**Last structural update:** 2026-05-20 (staleness audit — §1/§2/§6 updated to post-M3.6b state, module table expanded to 20, amendment/invariant counts updated)
**Update this file** whenever new context files are added, moved, or retired.

---

## 1. The Company and Its Products

### NexSys (the company)
An infrastructure company building the operating system and trust layer for the connected home. Privately held, self-funded, no external investors. Patient capital alignment preserves the trust brand.

**Founder:** Nick (nick@nexsys.io)
**Domains:** nexsys.io (company), homesynapse.com (product)
**Current phase:** P3 — Implementation (test-first). Pre-revenue. 14 design docs Locked. **~476+ production Java files across 16 JPMS-compiled modules** (plus 3 scaffold-only modules: platform-systemd, test-support, dashboard; plus 1 classpath-only test module: testing/integration-tests — 20 Gradle modules total). Phase 2 FROZEN 2026-03-20 after Blocks A–S. Phase 3 through M3.6d-a complete (2026-05-20); next work unit M3.6d-b.

### Product Constellation

| Product | Type | Phase | Status |
|---|---|---|---|
| **HomeSynapse Core** | Smart home OS (free, Apache 2.0) | P3 Test-First Impl | 14 design docs Locked; Phase 2 FROZEN; 20 Gradle modules (16 JPMS-compiled + 3 scaffold + 1 IT); **~476+ production Java files**; ~1,465+ tests; M3.6d-a complete 2026-05-20, M3.6d-b NEXT |
| **HomeSynapse Connect** | Cloud subscription ($7.99/mo) | Phase 1 | Spec'd, not built |
| **HomeSynapse Cloud Pro** | Premium cloud ($14.99/mo) | Phase 1 | Spec'd, not built |
| **HomeSynapse Hub** | Hardware ($149) | Phase 1 | Spec'd, no manufacturing |
| **HomeSynapse Energy** | Energy management surface | Phase 2 | Planned |
| **NexSys Grid** | B2B VPP aggregation | Phase 2 | Planned |
| **NexSys Assure** | Insurance verification | Phase 3 | Planned |
| **NexSys Care** | Aging-in-place monitoring | Phase 3 | Planned |
| **HomeSynapse Professional** | Installer channel | Phase 3 | Planned |
| **HomeSynapse Property** | MDU management | Phase 3 | Planned |
| **NexSys OS** | OEM licensing | Phase 4+ | Planned |
| **NexSys Trust Mark** | Device certification | Phase 4+ | Planned |

---

## 2. The Two Repositories + Operational Context

NexSys uses a two-repo model plus an operational context directory:

- **`homesynapse-core-docs/`** — Authoritative knowledge store. Design docs, governance, research, reviews. For humans, agents, and future homesynapse.com documentation.
- **`homesynapse-core/`** — Code + code-adjacent artifacts only. Java source, MODULE_CONTEXT.md files, traceability maps, work-unit handoffs, ADRs.
- **`nexsys-hivemind/context/`** — Operational state and agent routing. Status, planning, handoffs, lessons, queue. The "control plane" for agent sessions.

### A. `homesynapse-core-docs/` — Authoritative Knowledge Store

#### `design/` — 14 Design Documents (All Locked)

Production order (from MVP §9.3) with dependency chain:

| # | Document | File | Depends On |
|---|---|---|---|
| 01 | Event Model & Event Bus | `01-event-model-and-event-bus.md` | None |
| 02 | Device Model & Capability System | `02-device-model-and-capability-system.md` | 01 |
| 03 | State Store & State Projection | `03-state-store-and-state-projection.md` | 01, 02 |
| 04 | Persistence Layer | `04-persistence-layer.md` | 01, 03 |
| 05 | Integration Runtime | `05-integration-runtime.md` | 01 |
| 06 | Configuration System | `06-configuration-system.md` | 01 |
| 07 | Automation Engine | `07-automation-engine.md` | 01, 02, 06 |
| 08 | Zigbee Adapter | `08-zigbee-adapter.md` | 02, 05 |
| 09 | REST API | `09-rest-api.md` | 02, 03, 07 |
| 10 | WebSocket API | `10-websocket-api.md` | 01 |
| 11 | Observability & Debugging | `11-observability-and-debugging.md` | 01, 03 |
| 12 | Startup, Lifecycle & Shutdown | `12-startup-lifecycle-shutdown.md` | All preceding |
| 13 | Web UI (Observability MVP) | `13-web-ui-observability-mvp.md` | 09, 10, 11 |
| 14 | Master Architecture Document | `14-master-architecture-document.md` | All preceding |

**Amendments:** `design/amendments/` — Ratified through AMD-43 as of 2026-05-16. Highlights: **AMD-25** Temporal Duration Trigger Modifier (fully integrated); **AMD-26** sqlite-jdbc virtual-thread pinning fix; **AMD-27** persistence platform-thread executor (LTD-11 exception); **AMD-32** persistence internal types (WriteCoordinator, WritePriority); **AMD-33** DomainEvent permanently non-sealed (ratified 2026-04-10, codebase aligned in `768a4e4`); **AMD-34–37** M2-bridge structural amendments (V001→25 columns, V002 DLQ, V003 snapshots); **AMD-38** checkpoint policy revision (APPLIED post-D1 spike); **AMD-39** journal_size_limit revision (WITHDRAWN post-D1 spike); **AMD-40** retention execution model (APPLIED); **AMD-41/42/43** M3 governance bundle — State Projection Execution Model, Subscriber Lifecycle/Isolation, Backpressure/Observability (APPLIED 2026-05-16). Read `homesynapse-core-docs/design/amendments/` for the full list and integration status of each AMD.

#### `foundations/` — Foundational References

| File | Contains |
|---|---|
| `HomeSynapse_Core_v1_Glossary.md` | Canonical vocabulary, three-layer contract (concept/UI/serialization terms). All code and docs must match. |
| `HomeSynapse_Identity_and_Addressing_Model_v1.md` | Identity model, ULID usage, addressing scheme, slug generation |

#### `governance/` — Architecture Rules & Standards

| File | Contains | Authority Over |
|---|---|---|
| `Architecture_Invariants_v1.md` | ~94 non-negotiable system properties (INV-XX-NN identifiers) across ~18 categories (72 original + 13 M3 governance: INV-BUS-01..03, INV-PROJ-01/04/NEW-01, INV-WRITER-01, INV-SUB-ISO-01..06 + others) | What the system MUST do |
| `HomeSynapse_Core_Locked_Decisions.md` | 18 locked implementation choices (LTD-01 through LTD-18), decision dependency graph | What technologies and patterns are used |
| `HomeSynapse_Core_v1_Project_MVP.md` | MVP scope, tiered strategy, performance budgets, development process, 14-document production order | What's in/out of the MVP |
| `DAS_Consolidated_Reference_v1.md` | Documentation and writing standards, three voice registers, content types | How we write |
| `DESIGN_DOC_TEMPLATE.md` | Mandatory template for all design documents, quality checklist, review process | How design documents are structured |
| `HomeSynapse_Core_Refined_Repo_Architecture_v2.md` | Repository architecture (supersedes v1) | How the codebase is organized |
| `Design_Review_Amendments_v1.md` | Design review amendment tracking | How amendments are processed |

#### `research/` — Market & Technical Research

Informational, not authoritative. Files inform decisions but do not constrain them. Includes market research, competitive intelligence, technical investigations, and spike results. Named descriptively or with `YYYY-MM-DD_topic.md` convention.

Current files include: competitive architecture analyses, event system design research, device model research, observability research, automation engine review, framework research, portability architecture, repository structure research, demand response research, regulatory tailwind analysis, DAS dependency mapping, context engineering research, and AI slop anatomy.

#### `archive/` — Completed Phase 1 Artifacts

Contains completed Phase 1 governance artifacts whose findings have been fully applied:
- `phase-2-transition-guide.md`
- `Critical_Design_Review_Session_Synopsis.md`
- `Doc_12_Cross_Audit_Report.md`
- `Virtual_Thread_Risk_Audit_Report.md`
- `reviews/` — The 6 architecture validation steps (Step_1 through Step_6) plus Block_H validation

### B. `homesynapse-core/` — Code Repository

#### Module Structure (20-module Gradle scaffold)

Phase 2 closed all block-level interface specification on 2026-03-20. All 16 JPMS-compiled modules have populated `module-info.java` and populated `MODULE_CONTEXT.md`. Three scaffold-only modules (platform-systemd, dashboard, test-support) carry stub MODULE_CONTEXT.md files and no Java source yet — their implementation is deferred to later phases. Module #20 (`testing/integration-tests`) was added in M3.4a (2026-05-19) — classpath-only test code (no module-info.java), Pi-profile gated.

| Group | Module | Status | Phase 2 Block |
|---|---|---|---|
| platform/ | `platform-api` | Phase 2 spec complete; in active Phase 3 use | Block F |
| platform/ | `platform-systemd` | Scaffold only (no Java source yet) | — |
| core/ | `event-model` | Phase 2 spec complete; `@EventType` applied M2.1/M2.i | Blocks A, B, D |
| core/ | `event-bus` | Phase 2 spec complete; **Phase 3 active** — InProcessEventBus (33 types), EventBusConfig, full REPLAY→LIVE | Block E |
| core/ | `device-model` | Phase 2 spec complete | Block G |
| core/ | `state-store` | Phase 2 spec complete; **Phase 3 active** — StateProjection, StateCheckpointSource, 19 types | Block H |
| core/ | `persistence` | Phase 2 spec complete; **Phase 3 active** — SqliteEventStore, profile-driven PRAGMAs, 45 types | Block J |
| core/ | `automation` | Phase 2 spec complete | Block L |
| integration/ | `integration-api` | Phase 2 spec complete | Block I |
| integration/ | `integration-runtime` | Phase 2 spec complete | Block O |
| integration/ | `integration-zigbee` | Phase 2 spec complete | Block P |
| config/ | `configuration` | Phase 2 spec complete | Block K |
| api/ | `rest-api` | Phase 2 spec complete | Block M |
| api/ | `websocket-api` | Phase 2 spec complete | Block N |
| observability/ | `observability` | Phase 2 spec complete | Block Q |
| web-ui/ | `dashboard` | Scaffold only (no Java source yet) | — |
| lifecycle/ | `lifecycle` | Phase 2 spec complete | Block R |
| app/ | `homesynapse-app` | Phase 2 spec complete | Block S |
| testing/ | `test-support` | Scaffold only (no Java source yet) | — |
| testing/ | `integration-tests` | **Phase 3 active** — M3.4a scaffold + M3.4b sustained-load/crash-recovery | M3.4a/M3.4b |
| — | `build-logic/` | Convention plugins | n/a |

#### `MODULE_CONTEXT.md` Files

Located at `[module-path]/MODULE_CONTEXT.md` within homesynapse-core. Each contains: purpose, type inventory, dependencies, consumers, cross-module contracts, constraints, gotchas, Phase 3 notes.

**Populated with real content (17 total):** platform-api, event-model, event-bus, device-model, state-store, persistence, configuration, automation, integration-api, integration-runtime, integration-zigbee, rest-api, websocket-api, observability, lifecycle, homesynapse-app, testing/integration-tests. Most recently updated: `core/event-bus/MODULE_CONTEXT.md` (2026-05-20, M3.6b — EventBusConfig, InProcessEventBus public), `core/persistence/MODULE_CONTEXT.md` (2026-05-20, M3.6a — DeploymentProfile 6 fields, LockingMode), `core/state-store/MODULE_CONTEXT.md` (2026-05-19, projection-checkpoint wiring), `testing/integration-tests/MODULE_CONTEXT.md` (2026-05-19, WUCP Phase 2 reconciliation).

**Scaffold stubs (3 total):** platform-systemd, test-support, dashboard. These modules exist as Gradle directories with placeholder MODULE_CONTEXT.md files but contain no Java source yet; their implementation is deferred.

#### `docs/handoff/` — Work-Unit Handoffs

Active template: `docs/handoff/TEMPLATE.md` (generalized for both Phase 2 blocks and Phase 3 milestones under WUCP). Historical Phase 2 block handoffs (block-b through block-s, 17 files) were archived 2026-04-11 into `docs/handoff/archive/phase-2-blocks/` — see that directory's README.md for the index. The canonical execution record for Phase 2 is `nexsys-hivemind/context/planning/phase-2-block-backlog.md` (FROZEN). For Phase 3, work unit instructions flow through the PM's coding-instruction format (see `project-manager/references/coding-instruction-format.md`) rather than long-lived handoff files in this directory.

#### `docs/traceability/` — Design-to-Code Traceability Indexes

14 files (01 through 14, matching design docs). Only `01-event-model.md` (44 entries) and `12-lifecycle.md` (2 entries) are populated. 10 stubs remain — traceability debt for completed Blocks G through O.

#### `docs/decisions/` — ADRs

Currently: `template.md` + `0001-adr-adoption.md`.

#### Root-Level Documentation

- `CONTEXT.md` — Root-level agent orientation file
- `docs/ARCHITECTURE.md` — Repo-level architecture overview
- `docs/TESTING.md` — Testing strategy

### C. `nexsys-hivemind/context/` — Operational State

#### `status/`

| File | Contains | Update Frequency |
|---|---|---|
| `PROJECT_SNAPSHOT.md` | Shared ground-truth for all agents: current phase, days remaining, design doc status, interface spec status, code state, blocking issues, schedule position, recent session log | Every session end, or after completing a work unit |

**This is the single authoritative source for current project state.** Must be read at every session start and updated at every session end.

#### `planning/`

| File / Directory | Contains | Update Frequency |
|---|---|---|
| `master-release-plan.md` | 37-week roadmap (7 phases, 5 workstreams, weekly deliverables, risk register) | When phase boundaries or major milestones shift |
| `phase-2-block-backlog.md` | **FROZEN** — historical Phase 2 block execution record (Blocks A–S) | No further edits |
| `phase-3-milestone-backlog.md` | **ACTIVE** — Phase 3 milestone backlog (M1.x prep, M2.x persistence, M3.x+ planned) | Update after every milestone completion (WUCP Phase 2) |
| `BLOCK_BACKLOG.md` | Thin redirect stub pointing to both backlogs above (retained for back-compat) | Not edited directly |
| `months/YYYY-MM_month.md` | Monthly plans with strategic focus, milestones, capacity, risks, end-of-month updates | Created at month start, updated at month end |
| `weeks/YYYY-WNN_monDD-monDD.md` | Weekly plans with day-by-day breakdowns, objectives, agent directives, end-of-week retrospectives | Created Sunday night, retrospective written following Sunday |

#### `handoff/`

| File | Contains | Update Frequency |
|---|---|---|
| `pm-handoff.md` | Current task, design doc status, outstanding instructions, deviations | Every PM session end |
| `coder-handoff.md` | Current task, files modified, test/build status, deviations, pattern discoveries | Every Coder session end |
| `cross-agent-notes.md` | Shared bulletin board for inter-agent messages (any agent can append, all agents read at session start) | Whenever one agent has info for another |

#### `lessons/`

| File | Contains | Update Frequency |
|---|---|---|
| `strategic-lessons.md` | Strategic planning patterns, calibration observations, context engineering findings (maintained by Nick) | Appended when strategic insights emerge |
| `pm-lessons.md` | Architecture patterns, constraint application insights, cross-subsystem observations | Appended during or after each session |
| `coder-lessons.md` | Implementation patterns, pitfalls, workarounds, testing discoveries | Appended during or after each session |

#### Task flow

Direct conversation (Nick → PM, PM → Coder), supplemented by `coder-handoff.md` for asynchronous handoff. The legacy `context/queue/` directory was removed 2026-04-11.

#### `strategy/`

The strategy layer holds Nick's long-form strategic artifacts. These are read by the PM in Mode 1 (Architect) when decomposing task briefs that touch product positioning, revenue, data strategy, or institutional framing. The `.docx` files are authoritative (Nick maintains them in Word) and should be read via the `docx` skill when extracting structured content.

| File | Contains | When PM reads it |
|---|---|---|
| `Six_Battlefields_MVP_Strategy.md` | Six competitive battlefields, MVP positioning, differentiation strategy | Task briefs that touch feature prioritization, competitive framing, or MVP scope decisions |
| `Revenue_Model_and_Licensing_Strategy.md` | Revenue model, licensing approach, pricing strategy, Non-Negotiable Revenue Principles | Any discussion of monetization, licensing, pricing, or revenue-adjacent features; canonical source for the Non-Negotiable Revenue Principles |
| `From_Platform_to_Institution_NexSys_Strategic_Report.docx` | Long-horizon strategic arc — platform-to-institution thesis, governance model, institutional positioning | Briefs about long-term direction, institutional framing, governance questions, or partnerships beyond MVP scope |
| `HomeSynapse_MVP_Data_Readiness_Specification.docx` | Data-readiness requirements for MVP launch — what data HomeSynapse Core must expose, in what shape, to feed the data layer downstream | Briefs that touch telemetry, event enrichment, data contracts, observability surfaces, or anything the Data Value Engine will consume |
| `NexSys_Data_Value_Engine_Strategy.docx` | Data value engine strategy — how HomeSynapse data becomes a durable asset, the downstream products it enables, the economics of the data layer | Briefs that ask "why does this data matter" or touch the long-term data moat; read alongside the Data Readiness Specification |

#### `traceability/`

Contains `TEMPLATE.md` only. Actual traceability indexes live in `homesynapse-core/docs/traceability/`.

#### `protocols/`

| File | Contains | Authority Over |
|---|---|---|
| `work-unit-completion-protocol.md` | Mandatory two-phase closeout sequence for every completed work unit (Phase 2 block or Phase 3 milestone). Defines what the Coder and PM must do after a work unit is finished. Supersedes the Phase-2-era Block Completion Protocol. | Work unit completion gates, documentation update obligations, drift prevention, deferred-build-gate tracking |
| `block-completion-protocol.md` | Thin redirect to `work-unit-completion-protocol.md`. Preserved so historical references continue to resolve. | — |

**This protocol is mandatory.** Every agent's CLAUDE.md references it. The Coder reads §Phase 1 after the compile gate (or upon deferring it). The PM reads §Phase 2 after reviewing Coder output. The prime rule is: **no work unit is "done" until both WUCP phases have been executed, and completion of a work unit is a prerequisite for starting the next.**

---

## 3. Frequently Needed Sections Index

Quick-reference for agents to find the parts of design docs and governance files they reference most often.

### Design Document Key Sections
- **Key Interfaces** for each design doc: §8 (every design doc has this section)
- **Architecture & Data Model** for each design doc: §3, §4

### Locked Decisions Register
`homesynapse-core-docs/governance/HomeSynapse_Core_Locked_Decisions.md` — 18 LTDs.

Most frequently cited:
- **LTD-04** — Typed ULIDs for all entity identifiers
- **LTD-05** — Per-entity monotonic sequences
- **LTD-08** — Jackson JSON for all serialization
- **LTD-09** — YAML for all human-facing configuration
- **LTD-11** — No `synchronized` keyword; virtual-thread-safe concurrency
- **LTD-15** — SLF4J for all logging
- **LTD-17** — IntegrationContext as the integration boundary

### Architecture Invariants
`homesynapse-core-docs/governance/Architecture_Invariants_v1.md` — ~94 invariants across ~18 categories (72 original + M3 governance additions).

Most frequently cited:
- **INV-ES-01** — Event immutability (events are append-only facts)
- **INV-ES-02** — State derivability (state is always reconstructable from events)
- **INV-ES-04** — Write-ahead persistence (events persisted before publish)
- **INV-LF-02** — No outbound network calls from core modules
- **INV-RF-01** — Integration crash isolation (adapter crash cannot take down core)

### Glossary
`homesynapse-core-docs/foundations/HomeSynapse_Core_v1_Glossary.md` — Canonical terminology. All code identifiers and documentation must match the Glossary.

### MODULE_CONTEXT.md Files
Located at `[module-path]/MODULE_CONTEXT.md` within homesynapse-core. Each contains: purpose, type inventory, dependencies, consumers, cross-module contracts, constraints, gotchas, Phase 3 notes. **Read the relevant module's MODULE_CONTEXT before any work touching that module.**

---

## 4. Dependency Web

Understanding how documents depend on each other prevents issuing task briefs for work whose dependencies aren't met.

### Strategy → Governance Dependencies
- Revenue Model → defines which products exist → constrains MVP scope
- Six Battlefields Strategy → defines competitive positioning → constrains feature priorities
- Strategic doctrine (embedded in strategy docs) → defines non-negotiables → constrains Architecture Invariants

### Governance → Design Dependencies
- Architecture Invariants → every design doc must satisfy applicable INVs
- Locked Decisions → every design doc must comply with cited LTDs
- MVP Scope → defines what's in/out for each subsystem
- Design Doc Template → mandates structure for all design docs
- Glossary → mandates terminology for all design docs and code

### Design → Design Dependencies (the critical path)
```
01 Event Model ──┬──▶ 02 Device Model ──┬──▶ 03 State Store ──▶ 04 Persistence
                 │                       │
                 ├──▶ 05 Integration RT  ├──▶ 07 Automation ◀── 06 Configuration
                 │                       │
                 ├──▶ 06 Configuration   ├──▶ 09 REST API
                 │                       │
                 └──▶ 10 WebSocket API   └──▶ 08 Zigbee Adapter ◀── 05 Integration RT

                 09 ──┐
                 10 ──┼──▶ 11 Observability ──▶ 13 Web UI
                 11 ──┘

                 All ──▶ 12 Startup/Lifecycle ──▶ 14 Master Architecture
```

### Design → Code Dependencies (Phase 2/3)
Each design doc produces interface specs (Phase 2) which produce tests and implementations (Phase 3). Implementation of subsystem N cannot begin until subsystem N's design doc is Locked and its interface spec is complete.

---

## 5. Non-Negotiable Quick Reference

These are documented in the strategy files and governance documents. They constrain ALL decisions at every level.

**Identity:**
- No advertising, ever
- No data monetization, ever
- No feature-gating of core functionality
- No per-device fees
- No mandatory subscriptions (free tier fully functional)
- No VC funding that demands hypergrowth at expense of trust
- Apache 2.0 for core platform

**Architecture:**
- Local-first by design (internet enhances, never controls)
- Event-sourced (events are immutable facts, state is derived)
- Privacy by architecture, not policy (data stays local by default)
- Crash isolation (integration crash cannot take down core)
- Deterministic behavior (same events → same state)

**Revenue:**
- Every revenue stream must create direct value for the user
- Revenue through progressive value, never extraction
- Self-funding growth model

---

## 6. Current Development State

**Always check `nexsys-hivemind/context/status/PROJECT_SNAPSHOT.md` for the latest state.** The summary below may be stale — the snapshot is always authoritative.

**Phase:** P3 — Implementation (test-first). Phase 2 Interface Specification frozen 2026-03-20.
**Revenue:** Pre-revenue
**Code:** 20-module Gradle layout (16 JPMS-compiled production modules + 3 scaffold-only: platform-systemd, test-support, dashboard + 1 classpath-only test module: testing/integration-tests); **~476+ production Java files** across the 16 compiled production modules; ~145+ test files, ~35+ testFixtures files. Reproducible: `find homesynapse-core -path "*/src/main/java/*.java" | wc -l` — always exclude worktrees and build outputs.
**Tests:** **~1,465+ @Test methods** across the full test suite. Contract test suites: EventStoreContractTest (27), EventBusContractTest (50), WriteCoordinatorContractTest (11), CheckpointStoreContractTest (9), ViewCheckpointStoreContractTest (10), DeadLetterStoreContractTest (10). Integration tests (Pi-profile gated): BurstLoadIT, HeapBudgetIT, Pi4SustainedLoadIT, Pi4D1SpikeIT, CrashRecoveryIT.
**Interface specs complete:** 16 modules (Phase 2 Blocks A–S) — FROZEN
**Current milestone:** M3.6a + M3.6b + M3.6c + M3.6d-a COMPLETE 2026-05-20. M3.6d-b NEXT (PersistenceFactory + HomeSynapseCore wiring).
**Next critical path:** M3.6d-b → M3.6e.1 → M3.6e.2 → M3.7 (end-to-end integration tests).
**Schedule:** Significantly ahead of the original 37-week Master Release Plan. The 37-week plan placed Weeks 1–10 as "Interface Specification" — finished in 7 days (Mar 14–20). Phase 3 persistence subsystem (M2.x) complete. Event bus production implementation with full REPLAY→LIVE algorithm + backpressure + persistent DLQ + state projection + integration tests all landed in the M3.1–M3.4b window (May 16–19). M3.6a/M3.6b composition-root prep landed May 20. See Phase 3 Progress Annotation in `master-release-plan.md` for actuals.
**Launch target:** November 25, 2026
**Design docs:** All 14 Locked. Amendments through AMD-43. DEC-M3-01 through DEC-M3-16 locked.
**Nick's timeline:** College student, 3–4 hour blocks on school days, full days weekends

---

## 7. Agent Loading Protocol

Role-specific checklist of what to read at session start. Nick handles strategic direction directly (via claude.ai Projects) — no separate Hivemind agent session.

### PM Session Start
0. **Freshness preflight** — run `project-manager/references/freshness-preflight.md` (10 checks) BEFORE any forward work
1. `nexsys-hivemind/context/status/PROJECT_SNAPSHOT.md`
2. `nexsys-hivemind/context/handoff/pm-handoff.md`
3. `nexsys-hivemind/context/handoff/cross-agent-notes.md`
4. `nexsys-hivemind/context/planning/phase-3-milestone-backlog.md` (active) — `phase-2-block-backlog.md` is frozen reference
5. The relevant design doc from `homesynapse-core-docs/design/`
6. The relevant MODULE_CONTEXT.md from `homesynapse-core/`
7. `nexsys-hivemind/context/decisions/phase-3-cross-module-decisions.md` (if touching a Phase 3 cross-module concern)

### Coder Session Start
0. **Freshness preflight** — run `coder/references/freshness-preflight.md` mirror
1. `nexsys-hivemind/context/status/PROJECT_SNAPSHOT.md`
2. `nexsys-hivemind/context/handoff/coder-handoff.md`
3. `nexsys-hivemind/context/handoff/cross-agent-notes.md`
4. The PM-issued coding instruction for the current milestone (Phase 3 instructions live in the PM→Coder handoff; Phase 2 block handoffs are archived at `homesynapse-core/docs/handoff/archive/phase-2-blocks/` for historical reference only)
5. The relevant MODULE_CONTEXT.md files for the target module AND its dependencies
6. `nexsys-hivemind/context/lessons/coder-lessons.md` (recent entries)

---

## 8. Staleness Rules

These rules make update obligations explicit. Agents cannot end sessions without maintaining the files they're responsible for.

| File | Must Be Updated When | By Whom |
|---|---|---|
| `PROJECT_SNAPSHOT.md` | Every session end, or after completing a work unit | Whichever agent ran the session |
| `phase-3-milestone-backlog.md` | Milestone status changes (PLANNED→NEXT→DONE) | PM when producing coding instruction, Coder when completing |
| `phase-2-block-backlog.md` | Frozen — retroactive corrections only | PM |
| Agent handoff files (`pm-handoff.md`, `coder-handoff.md`) | Every session end | The agent that ran the session |
| `pm-handoff.md` Open Risks section | Every session end; every deferred build gate logged until resolved | PM |
| `cross-agent-notes.md` | Corrections discovered, JPMS lessons, cross-module changes | Any agent discovering something others need |
| `strategic-context-map.md` (this file) | New files added/moved/retired, phase transitions | Nick or PM |
| `MODULE_CONTEXT.md` | After a module's interface spec or implementation changes | Coder (WUCP Phase 1 Step 1) |
| Traceability indexes | After each work unit completion | PM (WUCP Phase 2 Step 2) |
| Dual skill mirrors (`.claude/skills/nexsys-*`) | Every WUCP Phase 2 | PM (Step 10 — `diff -rq` must return empty) |

**Enforcement mechanism:** The Work Unit Completion Protocol (`context/protocols/work-unit-completion-protocol.md`) is the primary enforcement mechanism. Each agent's CLAUDE.md references the WUCP as a mandatory gate. The PM's WUCP Phase 2 drift check verifies all artifacts are current, and the session-start freshness preflight (`project-manager/references/freshness-preflight.md`) blocks forward work if the hivemind is stale. The PROJECT_SNAPSHOT.md "Recent Session Log" table serves as an audit trail — if a session appears in the log but didn't update the corresponding handoff file, that's a process failure.

---

## 9. How to Use This Map

**Before decomposing ANY request:**
1. Check this map to understand which context files are relevant
2. Verify the current state in `nexsys-hivemind/context/status/PROJECT_SNAPSHOT.md`
3. Trace the dependency chain to confirm prerequisites are met
4. Identify which constraints apply

**When Nick mentions something you're unsure about:**
1. Check if it's defined in the Glossary (`homesynapse-core-docs/foundations/HomeSynapse_Core_v1_Glossary.md`)
2. Check if it's a locked decision in the LTD register (`homesynapse-core-docs/governance/HomeSynapse_Core_Locked_Decisions.md`)
3. Check if it's an invariant in the Architecture Invariants (`homesynapse-core-docs/governance/Architecture_Invariants_v1.md`)
4. Check if it's a product in the strategy files (`nexsys-hivemind/context/strategy/`)
5. If it's not in any of these, it may be a new concept that needs to be recorded

**When you need to cite a specific fact:**
- Strategy/revenue → `nexsys-hivemind/context/strategy/Revenue_Model_and_Licensing_Strategy.md` or `Six_Battlefields_MVP_Strategy.md`
- Architecture rules → `homesynapse-core-docs/governance/Architecture_Invariants_v1.md`
- Implementation rules → `homesynapse-core-docs/governance/HomeSynapse_Core_Locked_Decisions.md`
- Phase/scope rules → `homesynapse-core-docs/governance/HomeSynapse_Core_v1_Project_MVP.md`
- Terminology → `homesynapse-core-docs/foundations/HomeSynapse_Core_v1_Glossary.md`
- Market/competitive data → `homesynapse-core-docs/research/`

---

**Last verified against:** `homesynapse-core` commit `dfb045e` on `2026-05-21`.
