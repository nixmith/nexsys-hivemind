<!--
file: project-manager/references/repo-state-protocol.md
purpose: Defines what the PM verifies about the codebase and context files before issuing any work product.
audience: PM
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-06-07 against commit 8028337
-->

# Repository State Protocol

The PM must always know the current state of the codebase and context files before issuing any work product. Incorrect assumptions about what exists lead to instructions that don't compile, design docs that contradict existing decisions, or tests that target nonexistent interfaces.

This protocol defines what to verify, when, and how.

---

## 1. State Categories

The PM tracks six categories of state:

### A. Design Document State
Where each of the 15 design documents (01–15) sits in the lifecycle — all currently Locked.

| Status | Meaning | PM Action |
|---|---|---|
| **Not Started** | No document exists | Can be produced when dependencies are met |
| **Draft** | Under active development | Content may change. Don't reference specific decisions as authoritative. |
| **Review** | Believed complete, under review | Content is stable but not locked. Reference with caution. |
| **Locked** | Finalized. Changes require formal revision. | This is authoritative. All references to this subsystem's design use this document. |
| **Superseded** | A newer version exists | Use the new version. Old version is historical only. |

**How to check:** Look in `homesynapse-core-docs/design/` for the document. Read the `**Status:**` field in the metadata header.

**Before issuing any work product:** Verify that every dependency document is at the required status (usually Locked). The production order and dependency graph are in MVP §9.3.

### B. Interface Specification State (Phase 2+)
Which subsystems have Phase 2 specs completed.

**How to check:** Look in the repo for the subsystem's module. Check for:
- Package structure (`src/main/java/com/homesynapse/[subsystem]/`)
- Public interfaces (`.java` files that are interfaces or sealed interfaces)
- Types (records, enums)
- Package-level `package-info.java` with Javadoc

**Before issuing Phase 3 instructions:** Verify the interface spec exists and the interfaces compile.

### C. MODULE_CONTEXT.md State
Which modules have populated MODULE_CONTEXT.md files.

**How to check:** Read the `MODULE_CONTEXT.md` at the root of each module directory. A populated file has substantive content in all sections. An unpopulated file has only the empty template with HTML comment placeholders.

| State | Meaning | PM Action |
|---|---|---|
| **Empty template** | Module has not completed Phase 2, or Phase 2 completed but context not yet populated | Cannot be relied on. Read design doc and source files directly. |
| **Populated** | Module has completed Phase 2 and context is current | Primary reference for cross-module understanding. Read this instead of re-reading entire design docs. |
| **Stale** | Module has been modified since MODULE_CONTEXT.md was last updated (e.g., Phase 3 changes altered contracts) | Needs update. Check git log for changes since MODULE_CONTEXT.md was last modified. |

**Modules (22 Gradle modules as of HEAD `8028337`).** `homesynapse-core/settings.gradle.kts` is the source of truth for the module list; **each module's `MODULE_CONTEXT.md` header is the source of truth for its type count — do not hardcode counts here, they drift every milestone.**
- `platform/platform-api` — dependency root, identity types (typed ULID wrappers, `UlidFactory`)
- `core/event-model` — event vocabulary (`EventEnvelope`, `DomainEvent`, `EventPublisher`, `EventStore`, `EventId`)
- `core/value-model` — **leaf** holding `AttributeValue` + `AttributeType`; relocated from device-model in M4.0b-4a to break the event↔device JPMS cycle (both event-model and device-model depend on it)
- `core/event-bus` — subscription model + active runtime (`InProcessEventBus`)
- `core/device-model` — device/entity/capability model, Floor/Area aggregates, EntityRole
- `core/state-store` — materialized view + state projection
- `core/persistence` — SQLite storage, payload/checkpoint codecs, migrations
- `core/automation` — rule engine (sealed trigger/condition/action hierarchies)
- `config/configuration` — YAML config + schema validation
- `integration/integration-api` — adapter contracts (frozen at M4.C, AMD-54..64)
- `integration/integration-runtime` — supervisor
- `integration/integration-zigbee` — Zigbee 3.0 adapter
- `api/rest-api` — HTTP command interface
- `api/websocket-api` — real-time event streaming
- `observability/observability` — health/trace/metrics
- `lifecycle/lifecycle` — startup/shutdown composition root (`HomeSynapseCore`)
- `app/homesynapse-app` — assembly apex (+ `HomeSynapseArchRules`)
- `platform/platform-systemd` — deployment-tier `PlatformPaths`/`HealthReporter` impls (**populated in M5-A**)
- `testing/test-support` — shared test fixtures: TestClock, SynchronousEventBus, NoRealIoExtension, InMemoryEventStore (**populated**)
- `testing/integration-tests` — on-device IT tests (`-PpiProfile`; excluded from default `check`)
- `spike/wal-validation` — throwaway WAL spike (not production)

**Scaffold/stub status:** only **`web-ui/dashboard`** remains a stub (Preact SPA, separate build pipeline, no compiled Java). platform-systemd and test-support are no longer scaffolds. All production JPMS modules have populated MODULE_CONTEXT.md files — Phase 2 completed **2026-03-20**; value-model's was created with the M4.0b-4a relocation.

**Before issuing any work product:**
1. Check if MODULE_CONTEXT.md exists and is populated for every module in the dependency chain
2. If populated, use it as your primary reference for type inventories, contracts, and gotchas
3. If empty or stale, read the design doc and source files directly
4. After Phase 2 completion for any module, populate its MODULE_CONTEXT.md before moving to Phase 3

### D. Code State (Phase 3+)
Which modules have implementation code, which tests exist, which tests pass.

**How to check:** Examine the repo:
```
homesynapse-core/
├── build-logic/                    # Convention plugins
├── gradle/libs.versions.toml      # Dependency versions
├── core/event-model/               # Event model module
│   ├── src/main/java/...          # Implementation
│   └── src/test/java/...          # Tests
├── core/device-model/              # Device model module
│   └── ...
├── platform/platform-api/          # Platform API module
├── integration/integration-api/    # Integration API module
└── ...
```

**Before issuing coding instructions:**
1. Verify the module exists in the Gradle build
2. Verify the interfaces from Phase 2 are present
3. Check existing tests in the module — new code must not break them
4. Check existing implementation — new code must integrate with it

### E. Build State
The Gradle project structure, module dependencies, and build configuration.

**Key files to check:**
- `settings.gradle.kts` — which modules are included
- `gradle/libs.versions.toml` — which dependencies and versions are available
- `build-logic/src/main/kotlin/` — convention plugins
- Each module's `build.gradle.kts` — module-specific configuration and dependencies

**Before issuing any coding instruction:**
- Verify the target module exists in `settings.gradle.kts`
- Verify any dependency the Coder will need is in `libs.versions.toml`
- If a new module is needed, include its creation in the coding instruction

### F. Context File State
The status of governance, strategy, and research files.

**Critical files to verify currency:**
- `nexsys-hivemind/context/status/PROJECT_SNAPSHOT.md` — is it up to date?
- `homesynapse-core-docs/governance/` — have any governance docs been amended since you last checked?
- `homesynapse-core-docs/design/` — have any design docs changed status?

---

## 2. Verification Timing

### Before processing any task brief:
1. Check design document status for all cited dependencies
2. Check PROJECT_SNAPSHOT.md and the current week's plan for any changes since the task brief was written
3. **Read MODULE_CONTEXT.md for all modules in the dependency chain** — this gives you the complete picture of existing types, contracts, and gotchas without re-reading every source file
4. If Phase 3: check repo for module existence and current code state

### Before producing a design document:
1. Verify all dependency documents are at Locked status
2. Read the full content of each dependency document (not just the status)
3. **Read MODULE_CONTEXT.md for all dependency modules** — understand what types and contracts already exist
4. Check if any adjacent subsystem's design doc has been updated since your last read

### Before producing coding instructions:
1. Verify the design document is Locked
2. Verify Phase 2 interface specs exist in the repo
3. **Verify the target module's MODULE_CONTEXT.md is populated** — if not, populate it first
4. **Read MODULE_CONTEXT.md for all dependency modules** — use the gotchas and cross-module contracts to populate the coding instruction's "What to Watch Out For" section
5. Verify the target module exists in the Gradle build
6. Run or check the existing test suite to understand current state
7. Check `libs.versions.toml` for available dependencies

### Before reviewing Coder output:
1. Verify the Coder's code compiles in the context of the existing repo
2. Verify existing tests still pass (regression check)
3. Verify new tests are present and meaningful
4. **Verify the Coder's code respects the cross-module contracts documented in MODULE_CONTEXT.md** — especially the behavioral contracts that aren't captured in method signatures

### After Phase 2 completion:
1. **Populate the module's MODULE_CONTEXT.md** — this is a mandatory deliverable, not optional documentation
2. Verify every public type in the source appears in the Type Inventory section
3. Document cross-module contracts, sealed hierarchies, constraints, gotchas, and Phase 3 notes

### After Phase 3 changes that affect contracts:
1. **Update the module's MODULE_CONTEXT.md** if implementation revealed new gotchas or changed cross-module contracts
2. **Update downstream MODULE_CONTEXT.md files** if the change affects their Consumers or Cross-Module Contracts sections

---

## 3. State Tracking Between Sessions

Claude Code sessions don't persist memory. At the start of each session, perform a state sync:

**Quick state sync (start of every session):**
```
1. Read nexsys-hivemind/context/status/PROJECT_SNAPSHOT.md
2. List homesynapse-core-docs/design/ to see which design docs exist and their status
3. Read MODULE_CONTEXT.md for every module that has one — these are your compressed memory
4. If repo exists: list the module structure to understand what code exists
5. If repo exists: check recent git log for changes since last known state
```

**Full state sync (when starting a major task):**
```
1. Quick state sync
2. Read every design doc that's a dependency of the current task
3. Read the governance files relevant to the current task
4. Read MODULE_CONTEXT.md for every module in the dependency chain
5. Examine the repo modules that the current task touches
6. Run the test suite to confirm current state
```

MODULE_CONTEXT.md files are specifically designed to make state syncs faster and more reliable. A populated MODULE_CONTEXT.md for a 57-file module gives you the complete picture in one read, instead of reading 57 individual Java files.

---

## 4. When State Is Uncertain

If you're unsure whether something exists or is current:

- **Design doc status:** Read the file. Don't assume.
- **Code existence:** List the directory. Don't assume.
- **Test status:** Run the tests. Don't assume.
- **Build configuration:** Read `build.gradle.kts`. Don't assume.
- **MODULE_CONTEXT.md currency:** Check if the file's last-modified date is after the most recent Java file change in the module. If in doubt, re-verify against the source files.
- **Sandbox git is NOT authoritative.** In-sandbox `git status`/`git diff` show spurious line-ending churn and can even mangle a file's diff (e.g. report a method deleted that isn't). The **Read tool on the working tree is authoritative** for current content; commits go through host git, not the sandbox. Never base a state claim on sandbox `git diff` — read the actual file.

Never issue a coding instruction based on assumed state. The five minutes spent verifying saves hours of debugging incorrect instructions.

---

## 5. Reporting State to Nick

When Nick asks about project state, or when you report task completion, include:

```
STATE REPORT
Design docs: [list with status for each]
Phase 2 specs: [which subsystems have completed specs]
MODULE_CONTEXT.md: [which modules have populated context files, any noted as stale]
Code modules: [which exist, which have passing tests]
Blocking issues: [anything preventing forward progress]
Next on critical path: [what should be worked on next, per dependency graph]
```

Keep Nick informed about state without being asked — if you discover a blocking issue during verification, report it immediately rather than waiting for the next task brief.
