<!--
file: project-knowledge/HomeSynapse_Current_State.md
purpose: Authoritative current-state document for HomeSynapse Core; uploaded to the Claude Project.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-05-29 against M4.0b-2 closeout source tree (M4.0a/M4.0b-1/M4.0b-2 COMPLETE, build GREEN at 7610296)
-->

# HomeSynapse Core — Current State

Last updated: 2026-05-29 (M4.0b-2 COMPLETE, committed `7610296` — AMD-50 version-transition backfill + `projectionVersion` 1→2 on the production string change-detect rule. Workstream A (projection/derivation) substantially done. Next: M4.B3 → M4.0b-3.)

---

## 1. Current Milestone Status

**M4 — Foundation (projection/derivation + device-model expansion + integration-api freeze) — IN PROGRESS.** Workstream A (projection/derivation) is substantially **COMPLETE**: **M4.0a** (atomic subscriber+view checkpoint coupling, AMD-45, `a441fdf`, 2026-05-29), **M4.0b-1** (production `ProductionDerivationRule` + `DispatchingProjectionAdvancer` REC-28, `cf1a97e`, 2026-05-29), **M4.0b-2** (AMD-50 version-transition backfill + `projectionVersion` 1→2, `7610296`, 2026-05-29). State-based behavior is now LIVE — the materialized `attributes` map populates from derived `state_changed`, and a version transition reconstructs historical attributes via the AMD-50 one-shot backfill. Only **M4.0b-3** (typed comparator/payload AMD-51/52) remains in Workstream A. **Next: M4.B3** (device-model `AttributeValue` expansion, AMD-47; gated on P4) **→ M4.0b-3** (gated on M4.B3). Workstream C (integration-api freeze) gated on P3.

**M3 (Event Distribution + State Materialization) — COMPLETE** (2026-05-27). All seven sub-milestones (M3.1–M3.7) shipped across nineteen Claude Code work units.

**M4.0b-2 (Version-Transition Reconciliation Backfill + `projectionVersion` 1→2) — COMPLETE** (committed 2026-05-29 `7610296`, build GREEN — 139 tasks). Implements ratified AMD-50 for the 1→2 transition: `backfillActive` provenance gate (set in `StateProjection.initialize()` reconciliation branch, cleared at `onCaughtUp()`); non-emitting one-shot backfill on BOTH `onEvent` and `processBatch` via the narrow `applyBackfillAttribute` (attributes + event-time `lastChanged`, no second `stateVersion` increment, INV-01); gate-conditional supersession in `applyToState` (§2.2); `Clock` removed from `DerivationContext` (§2.4). 7 files modified, 0 created, no module-info/Gradle. PM Phase 2 confirmed targets A–J against source; AMD-50-INV-01..04 upheld. Interim mixed-`lastChanged` (event-time in backfill, wall-clock in LIVE) is a conscious, documented interim — timestamp unifier is a separate WU. Twentieth Claude Code WU.

**M4.0b-1 (Production `DerivationRule` + `DispatchingProjectionAdvancer`) — COMPLETE** (committed 2026-05-29 `cf1a97e`, build GREEN). Amendment-free Workstream-A vertical slice: `ProductionDerivationRule` (package-private in `com.homesynapse.state`, lifted from `EchoStateRule`, string change-detect, publishes `state_changed` on LIVE → populates `attributes`) + REC-28 `DispatchingProjectionAdvancer`, both via DEC-M3-16 gateways. `MinimalProjectionAdvancer` **deleted**; `projectionVersion` stays 1. OR-M3-17/18 fully closed. Nineteenth Claude Code WU.

**M4.0a (Atomic Checkpoint Coupling + Reconciliation Plumbing) — COMPLETE** (committed 2026-05-29 `a441fdf`, build GREEN). AMD-45 coupled checkpoint via the new `AtomicCheckpointSink` seam; all three bus checkpoint writers gated (LIVE + both REPLAY, the D-1 correction); reconciliation metadata populated (OR-M3-13 resolved); REC-80 metric; REC-82 guard. First M4 WU.

**M3.7 (E2E Integration Tests + Checkpoint Fix) — COMPLETE** (committed 2026-05-27, build GREEN — 139 tasks, 0 failures, confirmed by Nick). Eighteenth and nineteenth Claude Code work units (two Coder briefs: abandon/stub + checkpoint fix).

M3.7 shipped in two Coder brief executions:
1. **Abandon + MinimalEventBusStub brief:** `abandon()` contract on `PersistenceFactory`, `InProcessEventBus`, `HomeSynapseCore`; `MinimalEventBusStub` test double; `NotifyingEventPublisher` fix; `HomeSynapseE2eHarness`; `MinimalProjectionAdvancer` (the real package-private advancer class in lifecycle, closes OR-M3-18) + the no-op `MINIMAL_DERIVATION_RULE` constant lambda in `HomeSynapseCore` (closes OR-M3-17 — there is **no** `MinimalDerivationRule` class; the production no-op derivation is a `DerivationRule` `@FunctionalInterface` lambda); `CrashRecoveryHttpIT`, `EndpointE2eIT`, `InFlightRequestShutdownIT`; `LiveModeAwaiter`, `TestEvents` test support.
2. **Checkpoint fix brief:** `"entity_state"` → `"state_projection"` key mismatch fix in `SqlitePersistenceLifecycle`; `FixedCheckpointPolicy.TESTING` constant (1 event / 100ms); `HomeSynapseConfig` expanded to 4 components (added `checkpointPolicy`); `CrashRecoveryHttpIT` TESTING policy wiring.

AMD-45 (Atomic Subscriber+View Checkpoint Coupling) **RATIFIED + applied in M4.0a** (`a441fdf`, 2026-05-29) — resolved the architectural issue where the bus subscriber checkpoint outran the projection view checkpoint under HOME_DEFAULT policy (the coupled `AtomicCheckpointSink` is now the sole writer for the projection; all three bus writers gated, incl. both REPLAY writes per the D-1 correction).

**Previous: M3.6e.2 (Admin Endpoints + ArchUnit Rules) — COMPLETE** (committed 2026-05-22 `76288af`).

**Previous: M3.6e.1 (MaterializedStateQueryService + REST Readiness Gate + Javalin Bootstrap) — COMPLETE** (committed 2026-05-22 `b71ed37`).

`MaterializedStateQueryService` (public final in state-store, static factory `create(StateProjection)`, implements all 5 `StateQueryService` methods — returns `Optional.empty()` / empty `Map` when projection not LIVE). `ReadinessFilter` (package-private in rest-api, Javalin `before` handler, 503 + JSON when not LIVE). `RestFilters` (public final in rest-api, DEC-M3-16 gateway with `Object`-typed parameter erasing `io.javalin.Javalin` from public API surface). `ProblemType.STATE_STORE_REPLAYING` (new enum constant). `HomeSynapseCore` 14-step bootstrap (expanded from 12: added `MaterializedStateQueryService.create(stateProjection)` wiring + Javalin server on port 7070 with readiness filter). `DeploymentProfile` gains `httpThreads()` and `httpMaxThreads()` (STUDIO 1/4, HOME 2/8, PERFORMANCE 4/16). Two fix rounds: (1) `-Xlint:exports` on `ReadinessFilter` — demoted to package-private, `RestFilters` gateway created per DEC-M3-16; (2) Gradle/JPMS scope alignment — `implementation` → `api` for state-store in rest-api `build.gradle.kts`. 6 files created, 13 modified, +22 test methods. Sixteenth work unit via Claude Code.

**Previous: M3.6d-b (PersistenceFactory + HomeSynapseCore) — COMPLETE** (committed 2026-05-21 `dfb045e`, build GREEN)

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

**2026-05-27 M3.7 Closeout + Project Knowledge Update (Cowork)** — M3.7 COMPLETE. M3 milestone COMPLETE. OR-M3-17/OR-M3-18 RESOLVED (OR-M3-18 by the `MinimalProjectionAdvancer` class; OR-M3-17 by the no-op `MINIMAL_DERIVATION_RULE` constant lambda in `HomeSynapseCore` — **not** a `MinimalDerivationRule` class, which does not exist in source). AMD-45 drafted. Both repos committed. All project-knowledge files updated for M4 readiness. Nineteen CC WUs total.

**2026-05-22 WUCP Phase 2 — M3.6e.2 (Cowork)** — Governance/context maintenance session closing M3.6e.2 (`76288af`). M3.6 milestone COMPLETE. OR-M3-17 (NO_OP_DERIVATION placeholder) + OR-M3-18 (NO_OP_ADVANCER placeholder) logged as open. Seventeen CC WUs total. All hivemind artifacts updated.

**2026-05-22 WUCP Phase 2 — M3.6e.1 (Cowork)** — Governance/context maintenance session closing M3.6e.1 (`b71ed37`). OR-M3-15 (Xlint:exports gateway pattern) + OR-M3-16 (Gradle/JPMS scope alignment) logged and resolved. M3.6e.2 coding instruction produced. All hivemind artifacts updated.

**2026-05-22 WUCP Phase 2 — M3.6d-b (Cowork)** — Governance/context maintenance session closing M3.6d-b (`dfb045e`). OR-M3-14 RESOLVED. OQ-05-03 RESOLVED. M3.6e.1 coding instruction produced.

**2026-05-20 WUCP Phase 2 — M3.6c + M3.6d-a + DEC-M3-17 (Cowork)** — Governance/context maintenance session closing M3.6c (`38d3e30`) and M3.6d-a (`25bc23b`). M3.6d sub-divide propagated through Current_State/Knowledge_Primer/backlog/weekly plan. DEC-M3-17 logged (HealthSignal + HealthLevel transitive promotion; DEC-M3-16 addendum). coder-handoff.md "FOUR OPEN" framing corrected to "ZERO OPEN" (all four 2026-05-20 WUs were GREEN at commit). OR-M3-12 (resolved in this closeout), OR-M3-13 (reconciliation metadata feature gap), OR-M3-14 (M3.6d-b prerequisite infrastructure) added.

**2026-05-20 WUCP Phase 2 — M3.6a + M3.6b (Cowork)** — Governance/context maintenance session closing both M3.6 sub-WUs. Four PM-side artifacts updated. Coder-side artifacts (MODULE_CONTEXTs, coder-handoff) already updated by Claude Code. DEC-M3-16 applied. Hivemind: PASS.

**2026-05-19 WUCP Phase 2 Reconciliation (PM)** — Retroactive closeout for six work units (Bus-Fix Piece A through M3.4b) and two design sessions. Hivemind brought from STALE to PASS. `testing/integration-tests/MODULE_CONTEXT.md` populated (module 20). Freshness preflight: all 10 checks PASS.

**2026-05-19 Cross-Tier Deployment Audit (Cowork)** — Six-dimension audit against the six deployment tiers (Constrained → Multi-instance). Verdict: **NEARLY READY**. One BLOCKING finding (C-01) revised to SIGNIFICANT by PM; nine SIGNIFICANT findings all foldable into M3.6 composition-root work. Report: `nexsys-hivemind/context/audits/2026-05-19_cross-tier-deployment-audit.md`.

**2026-05-20 M3 Gap-Closure + Composition-Root Design (Cowork)** — Two design artifacts produced. **Artifact 1** (`homesynapse-core-docs/research/2026-05-20_M3_Audit_Gap_Closure_v1.md`) answers four architectural questions the audit missed (`globalPosition` contiguity, `chain_hash` cross-backend, event-type registration portability, `home_id` on `EventEnvelope`). All four answers benign — zero architectural surprises. **Artifact 2** (`homesynapse-core-docs/design/2026-05-20_M3.6_Composition_Root_Design.md`) specifies M3.6 as five sub-WUs (M3.6a..M3.6e) folding the audit findings into the composition-root work, with M3.6e being the `StateQueryService` capstone per PLAN-M3 §10.

### Next sequence

**M4 scoping is COMPLETE (2026-05-28).** Authoritative plan: `homesynapse-core-docs/design/HomeSynapse_Core_M4_Implementation_Plan_PLAN-M4-CONSOLIDATED.md`.

**M4 scope = Canonical** (Nick, 2026-05-28). M4 is the foundation milestone — three workstreams:
- **A — Projection/derivation foundation — substantially DONE:** M4.0a (`AtomicCheckpointWriter`/AMD-45, `a441fdf`) ✓, M4.0b-1 (`DispatchingProjectionAdvancer` REC-28 + real `ProductionDerivationRule`, `cf1a97e`) ✓, M4.0b-2 (AMD-50 one-shot backfill on the `projectionVersion` 1→2 reconciliation replay, `7610296`) ✓. State-based behavior is now LIVE; only **M4.0b-3** (typed comparator/payload AMD-51/52) remains, gated on M4.B3.
- **B — Device-model expansion — NEXT (M4.B3):** Research 8 REC-23–REC-30 + ratified-but-unbuilt **AMD-44** (Floor/EntityRole) + **AMD-47** (`AttributeValue` expansion: `QuantityValue`/`ArrayValue`/`DegradedAttributeValue`/`AttributeValueUpcaster`). **Gated on P4** (Doc 02/05 currency).
- **C — Integration-api interface freeze:** Research 6 REC-41–REC-51 (interface only; supervisor impl is M9). **Gated on P3** (Research 6 NQ-1..6).

**Explicitly NOT M4:** configuration = M6; automation engine = M7/M8 (its Phase 2 interface spec already exists on disk — M7/M8 is implementation, not interface design); integration-runtime impl = M9; REST/WebSocket = M10/M11.

**Open gates (decisions/doc-currency, not blocking the committed work):** **P2 RATIFIED** (2026-05-29 — device 46–49, projection 50–52 fixed; integration assign-at-milestone). Remaining: **P3** — Research 6 NQ-1..6 confirmations (gates Workstream C); **P4** — Doc 02/05 currency vs ratified amendments (gates M4.B3). Doc-currency follow-up: propagate the M4.0b-2 re-scope + M4.0b-3 row into PLAN-M4-CONSOLIDATED-v2 §3.

**Research 9/10 — CONSUMED:** they informed **AMD-50** (version-transition backfill / cursor determinism), now RATIFIED + implemented in M4.0b-2. The independent plan-verification pass is complete (fed P2 rev. 2 + AMD-50).

**Next concrete action:** **M4.B3** (device-model `AttributeValue` expansion, AMD-47) — gated on P4 (Doc 02/05 currency); then **M4.0b-3** (typed comparator/payload, gated on M4.B3 — a clean rule-swap reusing AMD-50's backfill path unchanged). P3 (Research 6 NQ-1..6) gates Workstream C independently and can be resolved in parallel.

**Build:** GREEN at `7610296` (M4.0b-2 — `./gradlew check` 139 tasks + `:core:state-store:check` + `:lifecycle:lifecycle:check`). Test/file counts last source-counted 2026-05-28 (**1,422** @Test methods / **724** Java files, 20 modules); M4.0a/M4.0b-1/M4.0b-2 added tests and modified files (not re-counted — no new modules).

**Active governance:** AMD-41/42/43 APPLIED (2026-05-16). **AMD-44 RATIFIED** (Floor/EntityRole — impl pending in the M4.B path). **AMD-45 RATIFIED + applied** (M4.0a, `a441fdf`). **AMD-50 RATIFIED + applied** (M4.0b-2, `7610296`) — **on-disk amendment watermark = AMD-50.** **P2 RATIFIED** (AMD renumbering). DEC-M3-14 through DEC-M3-17 + D-09 through D-12 locked. No pending amendments before M4.B3 (which authors AMD-47).

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
M3.6e.1 StateQueryService + REST gate        ← COMPLETE (2026-05-22) b71ed37
M3.6e.2 Admin endpoints + ArchUnit rules     ← COMPLETE (2026-05-22) 76288af
M3.7  E2E integration tests + checkpoint fix  ← COMPLETE (2026-05-27) [two Coder briefs]
```

M3.6d was sub-divided into d-a + d-b per the user's Option A decision. M3.6e was split into e.1 (StateQueryService + REST gate) and e.2 (admin endpoints + ArchUnit rules). M3.7 executed as two sequential Coder briefs (abandon/stub + checkpoint fix).

**M3 is COMPLETE.** All seven sub-milestones shipped across nineteen Claude Code work units (2026-05-16 through 2026-05-27). M4 Workstream A then shipped (M4.0a/M4.0b-1/M4.0b-2, through 2026-05-29 `7610296`). Next: M4.B3 → M4.0b-3.

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
| **Claude Code** | Java implementation | Production code, tests, MODULE_CONTEXT updates (**M3.1 through M3.7 executed via Claude Code — nineteen WUs**) |
| **Cowork** | Documentation, audits, design docs, context relay | Documentation updates, cross-tier audits, design sessions (e.g. 2026-05-19 cross-tier audit, 2026-05-20 gap-closure + M3.6 composition-root design), spot-check reviews |

Claude Code is the primary implementation surface. M3.1 through M3.7 validated the workflow across nineteen work units: PM generates task instruction → Claude Code executes in `acceptEdits` mode with `git commit/push/gradlew` denied → Nick reviews with `git diff`, runs build gate, commits. Cowork handles documentation-only tasks, audits, and design sessions where the output is markdown rather than code.

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

**CURRENT:** M4.0b-2 closeout reconciled (2026-05-29, `7610296`). Hivemind status: PASS. M4 Workstream A substantially COMPLETE (M4.0a/M4.0b-1/M4.0b-2). All three repos committed (core, core-docs; hivemind closeout pending Nick's commit). Next: M4.B3 → M4.0b-3.

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

**M3 COMPLETE. M4 Workstream A substantially COMPLETE (M4.0a/M4.0b-1/M4.0b-2). Next forward WU is M4.B3 (device-model expansion, AMD-47), gated on P4 doc currency.**

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
**Composition-root wiring — COMPLETE** (M3.6d-a `25bc23b` + M3.6d-b `dfb045e` + M3.6e.1 `b71ed37` + M3.6e.2 `76288af`). M3.6d-a shipped skeletons. M3.6d-b shipped the actual wiring: `PersistenceFactory` (public gateway), `HomeSynapseCore` (12-step bootstrap). M3.6e.1 expanded to 14-step bootstrap: added `MaterializedStateQueryService` wiring + Javalin HTTP server on port 7070 with readiness filter. M3.6e.2 expanded to 16-step bootstrap: added entity query endpoints + admin endpoints via `RestFilters` gateway methods. The composition root is now externally queryable with full endpoint coverage.

### Tracked Items from M3.6e.2 (2026-05-22) — ALL RESOLVED

**OR-M3-17 — FULLY CLOSED (M4.0b-1, `cf1a97e`, 2026-05-29).** The M3.7 interim was the no-op `MINIMAL_DERIVATION_RULE = context -> List.of()` lambda (there is **no** `MinimalDerivationRule` class — that was a phantom). M4.0b-1 retired the no-op lambda and shipped the real production **`ProductionDerivationRule`** (package-private in `com.homesynapse.state`, string change-detect, publishes a derived `state_changed` on LIVE so the `attributes` map populates), reached via the `DerivationRule.production()` gateway (DEC-M3-16). M4.0b-2 then added the AMD-50 version-transition backfill on top.

**OR-M3-18 — FULLY CLOSED (M4.0b-1, `cf1a97e`, 2026-05-29).** The M3.7 interim `MinimalProjectionAdvancer` (package-private lifecycle class) is **DELETED**. M4.0b-1 shipped the real **`DispatchingProjectionAdvancer`** (Research 8 REC-28 — package-private in `com.homesynapse.state`, constructor-injected `EnvelopeHandler` map, no `ServiceLoader`, forward-all → exact cursor parity), reached via the `ProjectionAdvancer.dispatching(EventStore)` gateway.

### Tracked Items from M3.6e.1 (2026-05-22)

**OR-M3-15 — Xlint:exports gateway pattern — RESOLVED.** `ReadinessFilter` (public) referenced `io.javalin.http.Handler` from non-transitive `requires io.javalin`. Fix: demote `ReadinessFilter` to package-private, create `RestFilters` public gateway with `Object`-typed parameter per DEC-M3-16 pattern. Pattern codified for future REST endpoints: any public class in an exported package that references a framework type from a non-transitive dependency must use the gateway pattern.

**OR-M3-16 — Gradle/JPMS scope alignment — RESOLVED.** `requires transitive com.homesynapse.state` in rest-api module-info required `api(project(":core:state-store"))` in build.gradle.kts (was `implementation`). Rule: `requires transitive` → `api`; plain `requires` → `implementation`. Lesson added to coder-lessons.md.

### Tracked Items from M3.6d-a (2026-05-20)

**OR-M3-13 — Reconciliation records metadata in data slot — RESOLVED (2026-05-29, M4.0a `a441fdf`).** `StateCheckpointSource.serializeCheckpoint(...)` was extended to accept `reconciledAt`/`reconciledFromVersion`/`reconciledToVersion`; `StateProjection.initialize()` populates them on the version-mismatch reconciliation; `SqliteStateStore` writes them instead of `null`. `ReconciliationTest`'s 5th method (`reconciliationRecordsMetadataInDataSlot`) is un-deferred and passing (asserts `reconciledToVersion == 2`). **M4.0b-2's backfill gate binds to `reconciledToVersion`.** AMD-41 §3.2.4's metadata-recording requirement is now met.

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

**Last verified against:** `homesynapse-core` M4.0b-2 closeout commit `7610296` on `2026-05-29`. M4 Workstream A substantially complete (M4.0a/M4.0b-1/M4.0b-2); AMD-44/45/50 ratified, watermark AMD-50, P2 ratified. Next: M4.B3 → M4.0b-3.
