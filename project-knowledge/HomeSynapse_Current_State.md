<!--
file: project-knowledge/HomeSynapse_Current_State.md
purpose: Authoritative current-state document for HomeSynapse Core; uploaded to the Claude Project.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-05-22 against commit dfb045e
-->

# HomeSynapse Core — Current State

Last updated: 2026-05-22 (post-M3.6d-b WUCP Phase 2 — OR-M3-14 RESOLVED, OQ-05-03 RESOLVED, composition root fully wired)

---

## 1. Current Milestone Status

**M3.6d-b (PersistenceFactory + HomeSynapseCore Composition-Root Wiring) — COMPLETE** (committed 2026-05-21 `dfb045e`, build GREEN — confirmed by Nick).

Shipped as 4-commit cohort (`a33ee40`..`dfb045e`): (1) `WriteCoordinator.queueSize()` accessor for bus writer-queue-depth `IntSupplier`; (2) production `SqliteSubscriberReadConnectionFactory` + `SqliteSubscriberReadExecutor` in core/persistence; (3) `PersistenceFactory` public gateway wrapping package-private `SqlitePersistenceLifecycle` (DEC-M3-16 factory pattern) + `SqlitePersistenceLifecycle` 6-store expansion (added `SqliteStateStore` + `SqliteDeadLetterStore`); (4) `HomeSynapseCore` public final class implementing `ReadinessSource` — 12-step bootstrap (PersistenceFactory.start → BusMetrics.jfr → InProcessEventBus → DerivedWriteRateLimit → StateProjection.create → subscribeRuntime → healthSignalHandler → QueueSaturationHealthCheck → SharedScheduler → started=true). 20 files changed, +1,432 lines, -14 deletions. OR-M3-14 RESOLVED (all three prerequisite infrastructure gaps closed). Fifteenth work unit via Claude Code.

**Previous: M3.6d-a (Composition-Root Satellite Changes) — COMPLETE** (committed 2026-05-20 `25bc23b`, build GREEN)

**Previous: M3.6c (Per-Module Event-Class Manifests) — COMPLETE** (committed 2026-05-20 `38d3e30`, build GREEN)
`EventTypes.CORE_PRODUCTION_EVENT_CLASSES` (22 classes) + `IntegrationEvents.LIFECYCLE_EVENT_CLASSES` (5 classes) aggregated via `Stream.concat(...).toList()` at composition root. Replaces 27 inline class imports across `AllEventClasses` (core/persistence) and `IntegrationTestHarness`. `IntegrationEvents` is a NEW public final class in `integration/integration-api`. Closes Q3 gap-closure Artifact 1. 1 new file + 4 modified. Refactor-only — no net test additions. Thirteenth work unit via Claude Code.

**Previous: M3.4b (Sustained-Load + Crash-Recovery Integration Tests) — COMPLETE** (committed 2026-05-19 `adf04d2`, build GREEN — `./gradlew check` + `./gradlew :testing:integration-tests:test -PpiProfile=throttled -PsustainedMinutes=10` both pass)

ThrottledWriteCoordinator disk test double in persistence testFixtures (baseline 10ms + 200ms spike at 0.5%, decorator pattern via `Function<WriteCoordinator, WriteCoordinator>`). Three new integration tests: Pi4SustainedLoadIT (100 ev/s sustained), Pi4D1SpikeIT (50 ev/s with D1 spike simulation, 30 min), CrashRecoveryIT (5,000 events, abandon at ≥3,000, restart, verify exactly-once delivery from checkpoint). DatabaseExecutor and SqlitePersistenceLifecycle gain package-private decorator constructor overloads. SLF4J API added to integration-tests test classpath. scripts/pi4-validation.sh on-device runner. Eighth work unit executed via Claude Code.

**Previous: M3.4a (Integration Test Module Scaffold) — COMPLETE** (committed 2026-05-19 `5ae7912`)
Creates the 20th module (`testing:integration-tests`). `IntegrationTestHarness`, `BurstLoadIT` (6 assertions), `HeapBudgetIT` (4 assertions). Seventh Claude Code WU.

**Previous: Supervisor DLQ Wiring WU — COMPLETE** (committed 2026-05-19 `ed5862c`)
Replaces 6-field `DlqEntry` with 11-field `DeadLetter` in `SubscriberSupervisor.deliver()`. 12 new tests. Sixth work unit via Claude Code.

**Previous: Projection-Checkpoint Wiring WU — COMPLETE** (committed 2026-05-19 `56aaa4b`)
Introduces `StateCheckpointSource` injection seam + 10 MB advisory checkpoint-size guardrail. Fifth work unit via Claude Code.

**Previous: M3.5b (StateProjection Production Persistence) — COMPLETE** (committed 2026-05-18 `08d0136`)
**Previous: Bus-Fix Piece A — COMPLETE** (committed 2026-05-18 `fceafe8`)
**Previous: M3.5a (StateProjection Vertical Slice) — COMPLETE** (committed 2026-05-18 `a2aff9c`)
**Previous: M3.3 / M3.2 / M3.1 — COMPLETE** (2026-05-17 / 2026-05-17 / 2026-05-16)

M3.6a (Profile-Driven Persistence Configuration) — COMPLETE (committed 2026-05-20, build GREEN)
Wired `DeploymentProfile` through `PersistenceConfig` into `DatabaseExecutor`. SQLite PRAGMAs render from active profile instead of hardcoded literals. `DeploymentProfile` gained `busyTimeoutMs`, `lockingMode` (LockingMode enum), `readThreadCount`. `PersistenceLifecycle` Javadoc scrubbed of SQLite-specific language. 14 files touched (1 created, 13 modified). 5 tests added/modified. Ninth work unit via Claude Code.

M3.6b (EventBusConfig + InProcessEventBus Visibility) — COMPLETE (committed 2026-05-20, build GREEN)
Created `EventBusConfig` record (replayQueueCapacity, publisherBlockedDepthThreshold) with `HOME_DEFAULT`. `ReplayWindowQueue` capacity parameterized. `InProcessEventBus` promoted to `public` (DEC-M3-16). 8 files touched (3 created, 5 modified). 9 tests added/modified. Tenth work unit via Claude Code.

### Recent governance work (no code, design-only)

**2026-05-22 WUCP Phase 2 — M3.6d-b (Cowork)** — Governance/context maintenance session closing M3.6d-b (`dfb045e`). OR-M3-14 RESOLVED (all three prerequisite infrastructure gaps closed). OQ-05-03 RESOLVED (prerequisites bundled into M3.6d-b). All hivemind artifacts updated to reflect composition root fully wired.

**2026-05-20 WUCP Phase 2 — M3.6c + M3.6d-a + DEC-M3-17 (Cowork)** — Governance/context maintenance session closing M3.6c (`38d3e30`) and M3.6d-a (`25bc23b`). M3.6d sub-divide propagated through Current_State/Knowledge_Primer/backlog/weekly plan. DEC-M3-17 logged (HealthSignal + HealthLevel transitive promotion; DEC-M3-16 addendum). coder-handoff.md "FOUR OPEN" framing corrected to "ZERO OPEN" (all four 2026-05-20 WUs were GREEN at commit). OR-M3-12 (resolved in this closeout), OR-M3-13 (reconciliation metadata feature gap), OR-M3-14 (M3.6d-b prerequisite infrastructure) added.

**2026-05-20 WUCP Phase 2 — M3.6a + M3.6b (Cowork)** — Governance/context maintenance session closing both M3.6 sub-WUs. Four PM-side artifacts updated. Coder-side artifacts (MODULE_CONTEXTs, coder-handoff) already updated by Claude Code. DEC-M3-16 applied. Hivemind: PASS.

**2026-05-19 WUCP Phase 2 Reconciliation (PM)** — Retroactive closeout for six work units (Bus-Fix Piece A through M3.4b) and two design sessions. Hivemind brought from STALE to PASS. `testing/integration-tests/MODULE_CONTEXT.md` populated (module 20). Freshness preflight: all 10 checks PASS.

**2026-05-19 Cross-Tier Deployment Audit (Cowork)** — Six-dimension audit against the six deployment tiers (Constrained → Multi-instance). Verdict: **NEARLY READY**. One BLOCKING finding (C-01) revised to SIGNIFICANT by PM; nine SIGNIFICANT findings all foldable into M3.6 composition-root work. Report: `nexsys-hivemind/context/audits/2026-05-19_cross-tier-deployment-audit.md`.

**2026-05-20 M3 Gap-Closure + Composition-Root Design (Cowork)** — Two design artifacts produced. **Artifact 1** (`homesynapse-core-docs/research/2026-05-20_M3_Audit_Gap_Closure_v1.md`) answers four architectural questions the audit missed (`globalPosition` contiguity, `chain_hash` cross-backend, event-type registration portability, `home_id` on `EventEnvelope`). All four answers benign — zero architectural surprises. **Artifact 2** (`homesynapse-core-docs/design/2026-05-20_M3.6_Composition_Root_Design.md`) specifies M3.6 as five sub-WUs (M3.6a..M3.6e) folding the audit findings into the composition-root work, with M3.6e being the `StateQueryService` capstone per PLAN-M3 §10.

### Next sequence

1. **M3.6e.1 coding instruction** — PM produces (this session). StateQueryService + REST gate: `MaterializedStateQueryService`, `ReadinessFilter` Javalin `before` handler, Javalin server bootstrap in `HomeSynapseCore`, thread pool sizing on `DeploymentProfile`. Estimated 4–5h Coder time.
2. **M3.6e.1 execution** — Claude Code.
3. **M3.6e.2** (admin endpoints + ArchUnit rules) → **M3.7** (E2E integration tests). Total M3.6/3.7 remaining: **~15–20h** Coder time.

**Build:** GREEN at `dfb045e`. ~1,550+ @Test methods across ~700+ Java files, 20 modules.

**Active governance:** AMD-41/42/43 APPLIED (2026-05-16). DEC-M3-14, DEC-M3-15 added (2026-05-17). DEC-M3-16 added (2026-05-20). DEC-M3-17 added (2026-05-20 — DEC-M3-16 addendum, HealthSignal + HealthLevel transitive promotion). No pending amendments.

---

## 2. Implementation Order (DEC-M3-11, with approved reordering)

```
M3.1  InProcessEventBus core                ← COMPLETE (2026-05-16)
M3.2  REPLAY→TRANSITION→LIVE (bus-side)      ← COMPLETE (2026-05-17)
M3.3  Backpressure, metrics, observability   ← COMPLETE (2026-05-17)
M3.5a StateProjection vertical slice         ← COMPLETE (2026-05-18) a2aff9c
      Bus-fix Piece A (DerivedWriteRateLimit)← COMPLETE (2026-05-18) fceafe8
M3.5b StateProjection prod persistence       ← COMPLETE (2026-05-18) 08d0136
      Projection-checkpoint wiring WU         ← COMPLETE (2026-05-19) 56aaa4b
      Supervisor DLQ wiring WU                ← COMPLETE (2026-05-19) ed5862c
M3.4a Integration-test scaffold (Pi profile)  ← COMPLETE (2026-05-19) 5ae7912
M3.4b Sustained-load + crash-recovery tests   ← COMPLETE (2026-05-19) adf04d2

      ─── 2026-05-19 cross-tier audit (Cowork)
      ─── 2026-05-20 gap-closure + M3.6 design (Cowork)
      ─── WUCP Phase 2 reconciliation           ← COMPLETE (2026-05-19)

M3.6a Profile-driven persistence config      ← COMPLETE (2026-05-20) 17c40b6
M3.6b EventBusConfig + InProcessEventBus     ← COMPLETE (2026-05-20) df2743a
M3.6c Per-module event-class manifests       ← COMPLETE (2026-05-20) 38d3e30
M3.6d-a Composition-root satellite changes   ← COMPLETE (2026-05-20) 25bc23b
M3.6d-b PersistenceFactory + HomeSynapseCore ← COMPLETE (2026-05-21) dfb045e (4-commit cohort)
M3.6e.1 StateQueryService + REST gate        ← NEXT — M3.6 CAPSTONE (PLAN-M3 §10)
M3.6e.2 Admin endpoints + ArchUnit rules
M3.7  End-to-end integration tests
```

M3.6d was sub-divided into d-a (satellite changes — landed 2026-05-20 `25bc23b`) and d-b (composition-root wiring — landed 2026-05-21 `dfb045e`) per the user's Option A decision after Coder pushback identified 7 source-vs-brief mismatches. M3.6d-b incorporated all three OR-M3-14 prerequisite infrastructure pieces and shipped as a 4-commit cohort. OR-M3-14 RESOLVED.

The M3.6 sub-WUs are specified in `homesynapse-core-docs/design/2026-05-20_M3.6_Composition_Root_Design.md`. Critical path: M3.6e.1 → M3.6e.2 → M3.7. M3.6e scope expanded (2026-05-20): +Javalin server, +3 admin endpoints (M3.5b gap), +6 ArchUnit rules. Split into M3.6e.1/M3.6e.2 to manage risk.

Estimated total Coder time remaining for M3.6 + M3.7: M3.6e.1 (4–5h) + M3.6e.2 (5–7h) + M3.7 (6–8h) = **15–20h** spread across three separate compile-and-commit units.

---

## 3. M3 Locked Decisions Ledger (DEC-M3-01 through DEC-M3-17)

| ID | Subject | Locking Authority | Key Constraint |
|----|---------|-------------------|----------------|
| DEC-M3-01 | Projection read/write discipline | AMD-41 §3.2.1 | Two-phase: READ then PUBLISH then CHECKPOINT. No interleaving. |
| DEC-M3-02 | Self-produced event detection | AMD-41 §3.2.2 | `SelfProducedFilter` (60s TTL, lazy eviction) + `stateVersion` defence-in-depth. |
| DEC-M3-03 | REPLAY→LIVE transition | AMD-42 §3.4.2 | Three-phase: REPLAY (catch-up) → TRANSITION (drain queue) → LIVE. |
| DEC-M3-04 (modified) | State projection checkpoints | AMD-41 §3.2.3 | MVP uses `ViewCheckpointStore`; `SqliteSnapshotStore` deferred. |
| DEC-M3-05 | Snapshot format | AMD-41 §3.2.3–4 | Jackson JSON with `snapshotVersion` + `projectionVersion` headers. V003 table created; impl deferred. |
| DEC-M3-06 (augmented) | Subscriber isolation | AMD-42 §3.4.4–6 | INV-SUB-ISO-01..06 catalog — per-subscriber VT, connection, DLQ, mode, queue, filter. |
| DEC-M3-07 | Coalescing | AMD-43 §3.6.5 | DEFERRED past M3. `coalesceExempt` retained but inert. |
| DEC-M3-08 (rejected, replaced) | Backpressure | AMD-43 §3.6.1 | No publish blocking on queue depth. Natural backpressure from single-writer. Rate limit (200/s) for StateProjection. |
| DEC-M3-09 | Clock injection | ArchUnit rule | Single `Clock` per JPMS module. `NO_DIRECT_TIME_ACCESS` enforced. NOT an AMD. |
| DEC-M3-10 | State_changed derivation | AMD-41 (scope) | Lives in `StateProjection` (core/state-store), NOT in writer. Writer is semantic-free. |
| DEC-M3-11 | Implementation order | PLAN-M3 §1.2 | M3.1 → M3.5a → M3.2 → M3.3 → M3.4 → M3.5b → M3.6 → M3.7. |
| DEC-M3-12 (modified) | Pi 4 support | AMD-43 §3.6.6 | Universal defaults at MVP. Platform-aware tuning deferred to M3.4 outcome. |
| DEC-M3-13 | Integration-test module placement | PLAN-M3 §8.2 | `testing:integration-tests` module — **created in M3.4a, 2026-05-19**. |
| **DEC-M3-14** | **Writer queue depth observation** | **M3.3 deliberation; Nick-approved 2026-05-17** | **Writer queue depth via `IntSupplier` injection at construction time. Overrides PLAN-M3 §7.2/§7.9. Re-open if multiple cross-module observable values emerge requiring the same pathway.** |
| **DEC-M3-15** | **M3.5a STOP gate removal pattern** | **M3.2 precedent; formalized M3.3; Nick-approved 2026-05-17** | **M3.5a STOP gates removed where the gated component is independently testable without StateProjection. Test: can the type be exercised with mock subscribers + injected deps without StateProjection code existing? If yes, gate removed.** |
| **DEC-M3-16** | **Composition-root visibility strategy** | **PM decision (2026-05-20)** | **InProcessEventBus → promoted to `public` (APPLIED M3.6b `df2743a`). SqlitePersistenceLifecycle → `PersistenceFactory` public gateway (APPLIED M3.6d-b `725353d`). QueueSaturationHealthCheck → promoted to public (APPLIED M3.6d-a `25bc23b`; transitive chain captured as DEC-M3-17). ALL THREE APPLIED.** |
| **DEC-M3-17** | **HealthSignal + HealthLevel public visibility (DEC-M3-16 addendum)** | **Implementation discovery during M3.6d-a; ratified by PM 2026-05-20** | **Promoted to public alongside QueueSaturationHealthCheck (`25bc23b`) because the constructor's `Consumer<HealthSignal>` parameter chain leaks both types; `-Xlint:exports` would have failed otherwise. The 3-type promotion chain (QueueSaturationHealthCheck + HealthSignal + HealthLevel) is the minimum viable visibility unit. Pattern lesson: pre-promotion `-Xlint:exports` verification must check transitively — every type appearing in the class's public constructor signature, public method signatures, public field types, and return types must itself already be public. See coder-lessons.md M3.6d-a entry #1.** |

No new decisions locked since DEC-M3-17 (2026-05-20). The 2026-05-19 audit's revised severities (C-01 BLOCKING→SIGNIFICANT; D1-04 SIGNIFICANT→MINOR; D2-01 NEARLY PLUGGABLE→PLUGGABLE; D3-06 SIGNIFICANT→INFO) are recorded in the audit report, not as DEC entries.

For full decision rationale and future re-opening conditions, see `PLAN-M3-CONSOLIDATED-02` §12 (searchable via project knowledge).

---

## 4. Workflow Architecture

### Three Claude Surfaces

| Surface | Role | Primary Output |
|---------|------|----------------|
| **This Claude Project** | PM / architect | Task instructions, design decisions, governance artifacts, architecture compliance |
| **Claude Code** | Java implementation | Production code, tests, MODULE_CONTEXT updates (**M3.1 through M3.6d-b executed via Claude Code — fifteen WUs**) |
| **Cowork** | Documentation, audits, design docs, context relay | Documentation updates, cross-tier audits, design sessions (e.g. 2026-05-19 cross-tier audit, 2026-05-20 gap-closure + M3.6 composition-root design), spot-check reviews |

Claude Code is the primary implementation surface. M3.1 through M3.6d-b validated the workflow across fifteen work units: PM generates task instruction → Claude Code executes in `acceptEdits` mode with `git commit/push/gradlew` denied → Nick reviews with `git diff`, runs build gate, commits. Cowork handles documentation-only tasks, audits, and design sessions where the output is markdown rather than code.

### Claude Code Configuration

- **Working directory:** `~/Desktop/Code/ClaudeFolder/homesynapse-core`
- **Permission mode:** `acceptEdits` (file writes auto-approved; bash commands require pre-approval)
- **Model:** Opus 4.7, effort `xhigh`
- **Denied commands:** `git commit/push/merge/reset/rebase`, `./gradlew`, `javac` — Nick owns the compile gate
- **Config files:** `.claude/settings.json` + `CLAUDE.md` at repo root (both `.gitignore`'d)

### nexsys-hivemind Repo

`nexsys-hivemind/` lives on Nick's machine (not synced to this Claude Project). It is the coordination layer between Claude surfaces:

- `context/` — PROJECT_SNAPSHOT.md, strategic-context-map.md, backlogs, weekly plans, audits
- `coder/` and `project-manager/` — Skill source files (writable copies)
- Cross-agent files: `coder-handoff.md`, `pm-handoff.md`, `cross-agent-notes.md`
- Skills mirror to this Claude Project at `/mnt/skills/user/nexsys-{coder,project-manager}/`
- `project-knowledge/` — Canonical source copies of all project knowledge files

### Work Unit Completion Protocol (WUCP)

Every work unit requires two phases before the next unit can start:
1. **Phase 1 (Coder):** Code written, tests pass, coder-handoff produced
2. **Phase 2 (PM):** PROJECT_SNAPSHOT updated, pm-handoff updated, backlog updated, drift check, dual skill-location sync verified

A stale hivemind (WUCP Phase 2 not run) blocks all forward work. The PM skill's freshness preflight enforces this.

**CURRENT:** M3.6d-b reconciled in WUCP Phase 2 (2026-05-22). Hivemind status: PASS. No outstanding prerequisites block M3.6e.1.

---

## 5. Prompt Format Conventions

### Claude Code Task Instructions (Java implementation — PRIMARY)

Leaner than Cowork prompts because Claude Code can read the repo directly. Structure:

- Reference-by-path (point to files to read, don't inline their content)
- Constraint citations by identifier (LTD-11, AMD-26) — Claude Code looks up the full text
- Behavioral contracts stated precisely; implementation approach left to Claude Code's judgment
- MODULE_CONTEXT files listed as mandatory pre-reads
- STOP-on-Mismatch gates (verify file state before writing)
- Binary success criterion (`./gradlew :module:check` GREEN — Claude Code does NOT run this; Nick does)
- Completion report format at end

### Cowork Prompts (documentation, audits, design)

Self-contained documents. All context is inlined because Cowork has no persistent state. Used for documentation updates, cross-tier audits, design sessions, and hivemind artifact maintenance. The 2026-05-19 cross-tier audit and the 2026-05-20 gap-closure + composition-root design session are both Cowork outputs.

### Common Rules (Both Surfaces)

- Implementation classes default to package-private under JPMS
- Constructor signatures must be verified against actual source before being specified
- Tests inject `Clock` — no `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()`
- `JacksonWarmup` requires platform threads (not virtual threads)
- No compilation, Gradle runs, or build verification in prompts — Nick owns the compile gate

---

## 6. Open Items

### WUCP Phase 2 Reconciliation — COMPLETE (2026-05-19)

Six work units reconciled: Bus-Fix Piece A (`fceafe8`), M3.5b (`08d0136`), Projection-Checkpoint Wiring (`56aaa4b`), Supervisor DLQ Wiring (`ed5862c`), M3.4a (`5ae7912`), M3.4b (`adf04d2`). Two design sessions logged: cross-tier deployment audit (2026-05-19), gap-closure + M3.6 design (2026-05-20). `testing/integration-tests/MODULE_CONTEXT.md` populated. Freshness preflight: PASS.

**No outstanding prerequisites block M3.6e.1.**

### Audit Findings Folded into M3.6 (2026-05-19 cross-tier audit + 2026-05-20 design)

| Audit ID | Description | Closes in | Status |
|---|---|---|---|
| C-01 | DeploymentProfile not wired into DatabaseExecutor (hardcoded `cache_size=-128000`, `mmap_size=1073741824`) | M3.6a | **CLOSED** (2026-05-20) |
| D1-05 | `busy_timeout=5000` hardcoded; Docker Desktop / NAS need different values | M3.6a | **CLOSED** (2026-05-20) |
| D1-07 | `ReplayWindowQueue.MAX_CAPACITY=10_000` hardcoded; Enterprise burst risk | M3.6b | **CLOSED** (2026-05-20) |
| D1-13 | `readThreadCount=2` default; under-provisions 64-core servers | M3.6a | **CLOSED** (2026-05-20) |
| D2-11 | `PersistenceLifecycle` Javadoc references WAL/PRAGMAs (leaks impl into public interface) | M3.6a | **CLOSED** (2026-05-20) |
| D3-08 | `DerivedWriteRateLimit.refill()` + `QueueSaturationHealthCheck.tick()` scheduler not wired | M3.6d-a | **CLOSED** (2026-05-20) — `SharedScheduler` skeleton wired both via `safelyInvoke(rateLimit::refill)` + `safelyInvoke(healthCheck::tick)`; actual instantiation lands in M3.6d-b composition root |
| D4-09 | Enterprise REPLAY overflow restart loop on burst | M3.6b | **CLOSED** (2026-05-20) |
| D5-04 | Docker Desktop WAL-shm incompatibility (`locking_mode=EXCLUSIVE` needed) | M3.6a | **CLOSED** (2026-05-20) |

Audit findings NOT addressed in M3.6 (stay open as documented MINOR per audit verdict):
- D1-02 (`page_size` as profile field) — MINOR
- D1-16 (thread-name PID prefix for multi-instance) — MINOR
- D1-19 / D5-08 (cross-platform storage-type detection beyond Linux `mmcblk`) — SIGNIFICANT, deferred to a future operational-resilience WU
- D5-09 (backup not implemented) — SIGNIFICANT, deferred per PERSISTENCE plan (post-M2 scope)

### Gap-Closure Q1–Q4 Outcomes (2026-05-20 Artifact 1)

| Q | Answer | M3.6 impact |
|---|---|---|
| Q1 — `globalPosition` contiguity | Gap-tolerant by construction. No `position + 1` arithmetic anywhere in `core/`. `readFrom(pos - 1, 1)` idiom is exclusive-`afterPosition` semantics, not contiguity. | None. Optional `EventStore.readFrom` Javadoc clarification rides along with M3.6a if convenient. |
| Q2 — `chain_hash` cross-backend | Reserved schema, not active. `ZERO_HASH` bound unconditionally. Multi-writer safe today. | None. AMD-37 annotation deferred to crypto-chain WU. |
| Q3 — Event type registration | Static list at composition root (per DECIDE-04). Each module publishes `public static final List<...>`. | M3.6c (new `EventTypes.CORE_PRODUCTION_EVENT_CLASSES` + `IntegrationEvents.LIFECYCLE_EVENT_CLASSES`). |
| Q4 — `home_id` on `EventEnvelope` | 14-field envelope; `home_id` populated on every write but never read back. | Defer to multi-hub WU. No optional accessor. |

### Tracked Follow-Ups from M3.5b / Wiring WUs (largely resolved)

**Projection-checkpoint wiring — RESOLVED** (2026-05-19 `56aaa4b`).
**Supervisor DLQ wiring — RESOLVED** (2026-05-19 `ed5862c`).
**SqliteStateStore implements StateCheckpointSource — RESOLVED** (2026-05-20 `25bc23b` / M3.6d-a). `serialize(int)` renamed to `serializeCheckpoint(int)` and promoted to public via the interface; `loadedProjectionVersion()` promoted to public via the interface. Class itself remains package-private — only the two interface methods are externally visible.
**Composition-root wiring — COMPLETE** (M3.6d-a `25bc23b` + M3.6d-b `dfb045e`). M3.6d-a shipped skeletons (`HomeSynapseConfig`, `SharedScheduler`, `ThrowingStateQueryService`). M3.6d-b shipped the actual wiring: `PersistenceFactory` (public gateway, 8 accessors), `HomeSynapseCore` (12-step bootstrap, implements `ReadinessSource`), plus three OR-M3-14 prerequisite pieces. The `stateQueryService()` method currently returns `ThrowingStateQueryService` — replaced by `MaterializedStateQueryService` in M3.6e.1.

### Tracked Items from M3.6d-a (2026-05-20)

**OR-M3-13 — Reconciliation records metadata in data slot (feature gap).** `StateProjection.writeCheckpoint(Instant)` passes plain `projectionVersion` to `StateCheckpointSource.serializeCheckpoint(int)`. The interface has no surface to accept `reconciledAt`, `reconciledFromVersion`, `reconciledToVersion`. `SqliteStateStore.serializeCheckpoint(int)` forwards `null` for those three fields to `CheckpointSerializer.serialize(...)`. M3.6d-a's `ReconciliationTest` ships 4 of 5 brief tests; the 5th (`reconciliationRecordsMetadataInDataSlot`) deferred because it would fail trivially. AMD-41 §3.2.4's metadata-recording requirement is not fully implemented. Track as a separate enhancement WU — likely M4 scope since it touches the projection's checkpoint contract.

**OR-M3-14 — M3.6d-b prerequisite infrastructure — RESOLVED** (2026-05-21 `dfb045e`). All three prerequisite infrastructure gaps closed in M3.6d-b's 4-commit cohort: `WriteCoordinator.queueSize()` at `a33ee40`, production `SqliteSubscriberReadConnectionFactory` at `a59b64e`, `SqlitePersistenceLifecycle` 6-store expansion + `PersistenceFactory` at `725353d`.

**Tier 9 reconciliationOnVersionMismatch test — RESOLVED** (2026-05-20 `25bc23b` / M3.6d-a). Un-disabled and implemented (subscribe → wait LIVE → unsubscribe → externally reset checkpoint to 0 → re-subscribe → assert 10 events re-replayed). M3.2 carry-forward gap #1 closed.

### Hardening Items from Cowork Review (2026-05-18)

**H1: CheckpointSerializer size guardrail — RESOLVED** (2026-05-19).
**H2: AtomicCheckpointWriter code duplication.** Two-way and three-way methods duplicate transaction wrapper. Extract shared `executeInTransaction` helper. Standalone cleanup or fold into M3.6d.
**H3: No concurrent access tests for SqliteStateStore.** ConcurrentHashMap is correct by construction but unproven under concurrent load. Fold into M3.4b (sustained-load) or M3.7 (E2E).
**H4: Post-shutdown defensive handling across all SQLite stores.** `park()` after `DatabaseExecutor.shutdown()` throws uncaught `RejectedExecutionException`. Pre-existing pattern. Fold into M3.7 or dedicated hardening pass.
**H5: event-bus MODULE_CONTEXT type count — RESOLVED.** 32 top-level types (14 public + 18 package-private) verified correct.

### Tracked Items from Supervisor DLQ Wiring (2026-05-19)

**Supervisor retry loop activation.** `computeBackoff()`, `sleepForBackoff()`, `MAX_RETRIES = 5` are dead code. Current behavior parks on first failure (`attemptCount = 1`). Activating the retry loop is a separate WU that also requires moving `recordCrash()` to the post-exhaustion path.
**`PersistentDlqWriter.noop()` wired but exercises no real persistence — RESOLVED in M3.6d-b.** `HomeSynapseCore` wires `persistenceFactory.deadLetterWriter()` (which returns `PersistentDlqWriter` backed by `SqliteDeadLetterStore`) into the bus's DLQ path.
**`DeadLetter.diagnostics` is null.** Stack-trace serialization deferred to a future enhancement.

### Tracked Items from M3.4a (2026-05-19)

**Pi-profile gate behind `-PpiProfile=throttled`.** Default `./gradlew check` does NOT run BurstLoadIT or HeapBudgetIT. Operators must explicitly enable. Documented in `testing/integration-tests/build.gradle.kts`.
**`testing/integration-tests/MODULE_CONTEXT.md` — RESOLVED.** Populated during WUCP Phase 2 reconciliation (2026-05-19).
**M3.4b sustained-load tests planned.** Optional `-PsustainedMinutes` override exists in the build script (default 60, CI proposed 10). Tests are tagged `@Tag("soak")` and run manually pre-release per PLAN-M3 §13.8 default. M3.4b is the next milestone after reconciliation.

### Tracked Items from M3.4b (2026-05-19)

**Pi4SustainedLoadIT event-count tolerance.** Task instruction specified ±2% tolerance; implemented as lower-bound 25%. The ±2% was a calibration error — ThrottledWriteCoordinator's 10ms baseline makes 100 ev/s unachievable under the test's own throttling profile. The lag-bound assertion (≤50 events) is the load-bearing check. PM accepted this deviation.
**CrashRecoveryIT @TempDir cleanup on Windows.** Uses `CleanupMode.NEVER` because abandoned harness holds SQLite file handles. Temp directories accumulate. OS handles cleanup.
**BusMetricsRecorder reuse.** Reused from `EventBusContractTest` (public static nested class) rather than extracting to a standalone testFixtures class. Acceptable for now; extract if M3.6d or M3.7 needs it.
**Full 60-minute sustained-load test on hs-dev-1 not yet run.** The 10-minute desktop run validates mechanism. The 60-minute Pi 5 run validates endurance. Schedule for pre-M3.7 or a quiet evening.
**scripts/pi4-validation.sh not yet exercised on hs-dev-1.** Created and chmod +x verified on Windows. First on-device run is manual.

### Tracked Gaps from M3.2

**Defence-in-depth for EventPublisher.publish from REPLAY mode** — Production `EventPublisher` guard is deferred to persistence module Phase 3. M3.5a implemented the first layer (StateProjection checks mode). Not blocking.
**`bus.resume()` does not re-spawn the VT** — Pre-existing M3.1 limitation. Blocks the Tier 9 `reconciliationOnVersionMismatch` bus-side test. Tracked for a dedicated bus-fix Piece B WU (separate from Piece A which is complete).
**Overflow test is slow (~5-15s)** — `replayWindowOverflowAt10000IsCriticalAlert`. Consider `@Tag("slow")` if test suite time becomes a concern.

### Tracked Items from M3.3

**JFR-native emission is accepted design debt.** Typed primitive adapter layer needed when a pull-based metrics consumer (Prometheus/OTLP) is introduced — likely M4+.
**Publish-latency metric measures bus-side fan-out, not end-to-end.** End-to-end publish latency is a persistence-module metric for a future observability pass.
**`lagEvents` is an approximation.** Under-reports by one delivery interval during burst catch-up. If M3.4b reveals insufficiency, add a `LongSupplier writerTailSupplier` following the DEC-M3-14 pattern.

### Tracked Items from M3.5a

**`StateProjection.processBatch` does not advance cursor on partial publish failure.** State mutations applied inside the read-tx callback are NOT rolled back. Crash recovery replays from the last checkpoint. Not blocking.
**`Map.copyOf` and null attribute values.** `EntityState.attributes()` may contain null values per the contract; `Map.copyOf` throws on nulls. All code paths use `LinkedHashMap` or `HashMap` instead. Any future refactor to `Map.copyOf` is wrong.

### JPMS Lessons

**`jdk.jfr` requires an explicit `requires` directive (M3.3).** PM-originated error corrected by Coder.
**Verify visibility modifiers against source, not documentation (M3.5a — G4).** When a PM brief states a type is public, verify by reading the source declaration line. M3.3 landed `DerivedWriteRateLimit` as package-private despite plans; M3.5a introduced `DerivedPublishGate` adapter; Bus-Fix Piece A subsequently promoted to public.

### Documentation Updates Deferred (per Q2 / Q4 of gap-closure)

**AMD-37 cryptographic-chain activation annotation** — deferred to the crypto-chain WU (post-MVP). The `chain_hash` column is reserved schema today (always `ZERO_HASH`); activation requires single-writer or partition-local chain construction.
**AMD-34 / `EventEnvelope.homeId` Java-side exposure** — deferred to multi-hub WU. Column populated, never read back. Breaking record-constructor change has no MVP consumer.

### Standing Items

**Test Hardening Backlog (TB-01 through TB-16):** 21 test additions across 12 groups. Foldable into M3 sub-milestones opportunistically.
**Cloud-Readiness Test Additions:** 21 additions organized by cloud tier. Foldable into M3+ work.
**Doc 05 §3.14 Amendment:** Specify event-based communication path for planned restart. Believed still open.
**Academic Research:** GCVSP benchmark on HomeSynapse TCA schema. Background activity.

---

## 7. Quick Reference

```bash
# Build
./gradlew check                                                # full build: compile + test + Spotless + ArchUnit + dependency rules
./gradlew :core:state-store:check                               # single module
./gradlew :testing:integration-tests:test \
    -PpiProfile=throttled -PsustainedMinutes=10                 # M3.4a+M3.4b Pi-profile integration tests (5 tests, ~40 min)
scripts/clean.sh                                                # clean before full check runs

# SSH to Pi 5
ssh pi                                  # via Tailscale, username: homesynapse

# Repos
git@github.com:nexsys-io/homesynapse-core.git        # source code
git@github.com:nexsys-io/homesynapse-core-docs.git   # design/governance (including 2026-05-20 audit-gap-closure + M3.6 design)
# nexsys-hivemind — local on Nick's machine, not on GitHub

# Claude Code
cd ~/Desktop/Code/ClaudeFolder/homesynapse-core
# Config: .claude/settings.json (acceptEdits, deny git commit/push/gradlew)
# Context: CLAUDE.md at repo root
# Both are .gitignore'd

# Today's design artifacts
homesynapse-core-docs/research/2026-05-20_M3_Audit_Gap_Closure_v1.md     # Q1-Q4 answers
homesynapse-core-docs/design/2026-05-20_M3.6_Composition_Root_Design.md  # M3.6a..M3.6e WU sequence
nexsys-hivemind/context/audits/2026-05-19_cross-tier-deployment-audit.md # 2026-05-19 audit report
```

---

**Last verified against:** `homesynapse-core` commit `dfb045e` on `2026-05-21`.
