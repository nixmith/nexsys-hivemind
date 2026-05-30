<!--
file: context/handoff/pm-handoff.md
purpose: PM session continuity — current task, work-unit status, open risks, outstanding instructions.
audience: PM, Coder
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-05-30 — P4r AMD-47 ratification mechanics (governance/docs/KB only; no code; HEAD unchanged at `7610296`). Prior: 2026-05-29 against M4.0b-2 closeout working tree.
-->

# PM Session Handoff

**Last updated:** 2026-05-30 (P4r governance-mechanics session — **AMD-47 RATIFIED**; AMD-47-INV-01..05 registered (`Architecture_Invariants_v1.md` §20); Doc 02 §3.7/§8.2 folded current; watermark stays AMD-50; **P4 Doc-02 half DONE → M4.B3 UNBLOCKED, NOT started**; no code, HEAD `7610296`. Prior: 2026-05-29 M4.0b-2 COMPLETE.)

## Current Task

**P4r — AMD-47 RATIFICATION MECHANICS COMPLETE (2026-05-30) — governance/docs/KB only, no code; HEAD unchanged `7610296`.** Executed the bounded, deterministic ratification of **AMD-47** (device-model `AttributeValue` expansion) that Nick authorized. Six edit clusters landed: (1) AMD-47 file PROPOSED→**RATIFIED** + Date applied 2026-05-30 + §2.5 fork annotated **RESOLVED: `QUANTITY` added** (1:1 value↔type; FLOAT-reuse rejected) + §9 checklist marked `[x]`; (2) **AMD-47-INV-01..05 registered** into `Architecture_Invariants_v1.md` as new **§20** (mirrors the §19 amendment-section precedent; §17 index + §0.3 prefix table + §18 traceability updated in the same commit; total 94→99 invariants); (3) Doc 02 §3.7 primitives table + §8.2 key-types **folded current** (PENDING-AMD-47 wrappers removed; the stale §8.2 `QuantityValue … wrapping JSR 385 Quantity<?>` row corrected to `(double value, String unit)` hand-rolled; ArrayValue/DegradedAttributeValue/`AttributeValueUpcaster` rows added; masthead → RATIFIED); (4) KB ledger (`HomeSynapse_Current_State` / `Knowledge_Primer` / `Decisions_Quick_Reference` / `Navigation_Index`) logs AMD-47 RATIFIED, REC-93 (hand-rolled units supersede deferred JSR-385), AMD-47-INV-01..05, and the **watermark note (stays AMD-50)**; (5) this snapshot/handoff update; (6) cross-agent-notes pointer rotated. **On-disk amendment watermark unchanged at AMD-50** (47 < 50 — ratification records RATIFIED, does not raise the ceiling). **No `.java`/`module-info`/Gradle/`projectionVersion` touched.** §7 source embeds re-verified intact vs HEAD `7610296` (module-info `com.homesynapse.device`; 5-variant `permits`; `AttributeType {BOOLEAN,INT,FLOAT,STRING,ENUM}`). Dual-skill `diff -rq` PASS (no skill-tree files touched). **M4.B3 is now UNBLOCKED (AMD-47 ratified ✓ + Doc 02 current ✓) but NOT started** — it is the next, separate fresh Mode-3 session. **Reconciliation note:** AMD-47 §4/§6 said invariant registration would occur "at M4.B3 closeout"; the ratification decision (this brief + cross-agent-notes + Next-Tasks #0a-iii) moved it to ratification time — followed the brief; the AMD-47 §6 line is the only residual that still reads "at M4.B3 closeout" (left as authored, superseded by the ratification mechanics).

**M4.0b-2 COMPLETE (2026-05-29, `7610296`) — WUCP Phase 2 done this session.** Implements ratified **AMD-50** for the 1→2 transition on M4.0b-1's string change-detect rule. Delivered: `projectionVersion` 1→2 at `HomeSynapseCore` (the trigger); a `backfillActive` provenance gate in `StateProjection` (set in `initialize()`'s version-mismatch reconciliation branch, cleared at `onCaughtUp()`); a non-emitting one-shot backfill applied on **both** `onEvent` and `processBatch` (the D-1 lesson) via the narrow `applyBackfillAttribute` (attributes + event-time `lastChanged` only; preserves `stateVersion`/`lastReported`/`lastUpdated`; no second increment, INV-01; never publishes); gate-conditional supersession in `applyToState`'s `state_changed` branch (§2.2 generality); `Clock` removed from `DerivationContext` (§2.4). 7 files modified (state-store + one-line lifecycle bump), 0 created, **no** `module-info`/Gradle changes. 8 AMD-50 §5 tests + the event-time-`lastChanged` headline + the processBatch D-1 twin. **PM Phase 2 read every changed file against source (not the report) and confirmed targets A–J**: gate-both-paths ✓, event-time `lastChanged` not wall-clock ✓, genuine supersession (would fail without the suppression fork) ✓, INV-01 no-double-increment ✓, one-shot ✓, `projectionVersion=2` ✓, clock removal at all 6 sites ✓, INV-04 audit ✓, no `module-info`/Gradle ✓. Deviations D-A `[REVIEW]` (processBatch backfill applied in-callback not post-advance — evidence-based, ACCEPT), D-B `[REVIEW]` (conscious interim mixed-`lastChanged`, ACCEPT — unifier is a separate WU), D-C/D-D `[INFO]` (determinism-test rename; verified-harmless test interaction). Build GREEN (139 tasks) + `:core:state-store:check` + `:lifecycle:lifecycle:check`; Nick committed `7610296`. **AMD-50-INV-01..04 upheld. No new Open Risks; no open deferred build gates.**

**Next: M4.B3 → M4.0b-3.** **M4.B3** = device-model `AttributeValue` expansion (`QuantityValue`/`ArrayValue`/`DegradedAttributeValue`/`AttributeValueUpcaster`, AMD-47) — now **UNBLOCKED** (AMD-47 RATIFIED ✓ + Doc 02 currency DONE ✓), the next forward WU but **NOT started** (separate fresh Mode-3 coding-instruction session). **M4.0b-3** = typed comparator (AMD-51) + typed `StateChangedEvent` (AMD-52), gated on M4.B3 — a clean rule-swap that reuses AMD-50's backfill path unchanged for the 2→3 transition (the supersession test is the standing N→M regression guard for that reuse). **Open prereqs / doc-currency follow-ups (none block the M4.0b-2 commit):** P3 (Research 6 NQ-1..6, Nick's calls) → Workstream C; **P4 Doc-05 half** (Integration-Runtime integration-api currency) still open + **P3-gated** → Workstream C (not M4.B3); propagate the M4.0b-2 re-scope + M4.0b-3 row into PLAN-M4-CONSOLIDATED-v2 §3; KB M4.0b-2 currency punch-list; the timestamp-model unifier WU. See Next Tasks for the ordered list.

## Phase 3 Work Unit Status

| Work Unit | Scope | Status | Commit |
|---|---|---|---|
| AMD-33 | DomainEvent permanently non-sealed | DONE 2026-04-10 | `768a4e4` |
| M2.1–M2.5 | Full persistence layer (EventType through SqliteEventStore) | DONE 2026-04-10/11 | `b2c8b78`..`5279e7a` |
| M2 (complete) | SqlitePersistenceLifecycle boot + shutdown | DONE 2026-05-01 | — |
| M2-bridge | AMD-34..37, V001→25 cols, V002 DLQ, V003 snapshots, 10 new types | DONE 2026-05-02 | — |
| D1 spike | WAL Pathology Validation — bounded reader is load-bearing | DONE 2026-05-15 | — |
| AMD-38/39 | AMD-38 APPLIED, AMD-39 WITHDRAWN, DeploymentProfile corrected | DONE 2026-05-15 | — |
| Deliverable 0 | ProjectionAdvancer.advance 3-param signature | DONE 2026-05-16 | — |
| M3 governance | AMD-41/42/43 APPLIED, PLAN-M3-CONSOLIDATED-02, DEC-M3-01..13 | DONE 2026-05-16 | — |
| M3.1 | InProcessEventBus core: mode FSM, isolation, supervisor, DLQ, circuit breaker | DONE 2026-05-17 | — |
| M3.2 | REPLAY→TRANSITION→LIVE bus-side: ReplayDriver, TransitionCoordinator, wiring | DONE 2026-05-17 | `0bade6a`. First CC milestone |
| M3.3 | Backpressure, metrics, observability: BusMetrics, health check, rate limiter | DONE 2026-05-17 | `a5d4b2a`. DEC-M3-14/15. |
| M3.5a | StateProjection vertical slice | DONE 2026-05-18 | `a2aff9c`. DerivedPublishGate adapter seam (G4). Third CC milestone. |
| **Bus-Fix Piece A** | `DerivedWriteRateLimit` package-private → public (one-line visibility change) | **DONE 2026-05-18** | `fceafe8`. Closes M3.5a G4 mismatch. |
| **M3.5b** | StateProjection production persistence — `SqliteStateStore`, `SqliteDeadLetterStore`, `PersistentDlqWriter`, `CheckpointSerializer`, V004 indices, ObjectMapper divergence, three-way atomic write | **DONE 2026-05-18** | `08d0136`. 19 files, +2,674 lines. Independent review PASS w/ 5 non-blocking concerns. |
| **Projection-checkpoint wiring** | `StateCheckpointSource` interface in state-store + 10 MB advisory guardrail | **DONE 2026-05-19** | `56aaa4b`. Closes M3.5b non-blocking concern #1. |
| **Supervisor DLQ wiring** | `SubscriberSupervisor.deliver()` constructs `DeadLetter` and routes through `park(DeadLetter)` | **DONE 2026-05-19** | `ed5862c`. 12 new `SubscriberSupervisorTest` methods. |
| **M3.4a** | Integration-tests module + harness + BurstLoadIT + HeapBudgetIT | **DONE 2026-05-19** | `5ae7912`. New testing module #20. Full check GREEN; profile-gated tests GREEN. |
| **M3.4b** | Pi4SustainedLoadIT, Pi4D1SpikeIT, CrashRecoveryIT, ThrottledWriteCoordinator, pi4-validation.sh | **DONE 2026-05-19** | `adf04d2` |
| **M3.6a** | Profile-driven persistence config (audit C-01, D1-05, D1-13, D2-11, D5-04) | **DONE 2026-05-20** | `17c40b6` |
| **M3.6b** | EventBusConfig + InProcessEventBus visibility (audit D1-07, D4-09; DEC-M3-16) | **DONE 2026-05-20** | `df2743a` |
| **M3.6c** | Per-module event-class manifests (Q3 gap closure) | **DONE 2026-05-20** | `38d3e30` |
| **M3.6d-a** | Composition-root satellite changes (SqliteStateStore→StateCheckpointSource, DEC-M3-17 visibility chain, ReadinessSource, ReconciliationTest 4/5, Tier 9 un-disabled, HomeSynapseConfig + SharedScheduler + ThrowingStateQueryService skeletons, SLF4J wiring) | **DONE 2026-05-20** | `25bc23b` |
| **M3.6d-b** | PersistenceFactory + HomeSynapseCore (composition-root wiring) — WriteCoordinator.queueSize(), SqliteSubscriberReadConnectionFactory, SqlitePersistenceLifecycle 6-store expansion, PersistenceFactory public gateway, HomeSynapseCore 12-step bootstrap | **DONE 2026-05-21** | `dfb045e` (4-commit cohort: `a33ee40`..`dfb045e`) |
| **M3.6e.1** | MaterializedStateQueryService + ReadinessFilter + RestFilters + Javalin bootstrap + DeploymentProfile thread pool sizing. Two follow-up fix rounds (Xlint:exports gateway, Gradle/JPMS scope). 7 deviations (none blocking). 6 created, 13 modified. | **DONE 2026-05-22** | `b71ed37` |
| **M3.6e.2** | Admin endpoints (DlqStatusEndpoint, ProjectionStatusEndpoint) + entity query endpoints (ListEntitiesEndpoint, GetEntityEndpoint, GetEntityStateEndpoint) + EndpointContext SPI + 2 RestFilters gateway methods + 2 ArchUnit rules + HomeSynapseCore 16-step bootstrap. 15 created, 6 modified, 19 test methods. 5 deviations (none blocking). M3.6 COMPLETE. Seventeenth CC WU. | **DONE 2026-05-22** | `76288af` |
| **M3.7** | E2E HTTP integration tests + abandon() contract + checkpoint key fix + TESTING checkpoint policy. 5 Cowork fix rounds + 2 CC briefs. 18 modified + 3 new files. CrashRecoveryHttpIT passes. M3 COMPLETE. Eighteenth CC WU. | **DONE 2026-05-27** | `78264a0` (+ `8930721`) |
| **M4.0a** | Atomic subscriber+view checkpoint coupling (AMD-45-INV-01) via new `AtomicCheckpointSink` seam; `SubscriberInfo.atomicCheckpoint` (Option A); all three bus checkpoint writers gated (LIVE + both REPLAY — D-1 correction); reconciliation-metadata population (OR-M3-13); H2 `executeInTransaction`; REC-80 metric; REC-82 sentinel guard. 1 created + ~19 modified. Build GREEN. First M4 WU. | **DONE 2026-05-29** | `a441fdf` |
| **M4.0b-1** | Amendment-free Workstream-A vertical slice: production `ProductionDerivationRule` (lifted from `EchoStateRule`, string change-detect, publishes `state_changed` on LIVE) + REC-28 `DispatchingProjectionAdvancer` (pkg-private `EnvelopeHandler` map, no `ServiceLoader`, forward-all cursor parity), both via DEC-M3-16 gateways; composition-root rewire, `projectionVersion` stays 1; `MinimalProjectionAdvancer` deleted. OR-M3-17/18 fully closed. 4 created (3 prod + 1 test) + 5 modified + 1 deleted. 11 new test methods. No module-info/Gradle changes. Build GREEN. | **DONE 2026-05-29** | `cf1a97e` |
| **M4.0b-2** | AMD-50 version-transition reconciliation backfill for the 1→2 transition on the string change-detect rule: `projectionVersion` 1→2 trigger; `backfillActive` provenance gate (set in `initialize()` reconciliation branch, cleared at `onCaughtUp()`); non-emitting one-shot backfill on **both** `onEvent` and `processBatch` via narrow `applyBackfillAttribute` (attributes + event-time `lastChanged`, no second `stateVersion` increment, INV-01); gate-conditional supersession in `applyToState` (§2.2); `Clock` removed from `DerivationContext` (§2.4). 7 modified, 0 created, no module-info/Gradle. 8 §5 tests + event-time-`lastChanged` headline + processBatch D-1 twin. PM Phase 2 confirmed A–J vs source. AMD-50-INV-01..04 upheld. Build GREEN (139). Twentieth CC WU. | **DONE 2026-05-29** | `7610296` |

## Design Doc Status

All 14 design documents Locked. Phase 2 interface specification frozen as of 2026-03-20. M3 governance bundle (AMD-41/42/43) APPLIED 2026-05-16. DEC-M3-14/15 added 2026-05-17. PLAN-M3-CONSOLIDATED-02 is the authoritative M3 implementation plan.

### New M3 design artifacts (committed since prior pm-handoff)

| Artifact | Path | Date | Notes |
|---|---|---|---|
| Cross-tier deployment audit | `nexsys-hivemind/context/audits/2026-05-19_cross-tier-deployment-audit.md` | 2026-05-19 | Closed-out audit. Informed M3.6 composition root design. |
| M3 audit gap-closure research (Artifact 1) | `homesynapse-core-docs/research/2026-05-20_M3_Audit_Gap_Closure_v1.md` | 2026-05-20 | Identified and closed audit-trail gaps prior to M3.4b/M3.6. |
| M3.6 Composition Root Design | `homesynapse-core-docs/design/2026-05-20_M3.6_Composition_Root_Design.md` | 2026-05-20 | Authoritative design that M3.6 implements against. |

## Outstanding Coding Instructions

None. M3.6e.2 executed and committed at `76288af`. M3.6 is COMPLETE.

## Unresolved Deviations

None requiring PM action. M3.5b's 5 non-blocking concerns (CheckpointSerializer size guardrail, AtomicCheckpointWriter duplication, no concurrent-access tests for SqliteStateStore, no post-shutdown defensive handling, MODULE_CONTEXT type count off-by-one) are tracked under PROJECT_SNAPSHOT "Tracked Gaps" — none block M3.4b. The Supervisor DLQ wiring source-verification audit (`2026-05-19_supervisor-dlq-source-verification.md`) corrected one assumption (A8: `SubjectRef.toString()` returns `"type:id"`, not bare ULID) — incorporated into the coding instruction before execution; no post-hoc cleanup needed.

## Next Tasks (Priority Order)

0. **~~Nick: issue M4.0b-2~~ — DONE 2026-05-29, committed `7610296`, WUCP Phase 2 closed.** AMD-50 backfill + `projectionVersion` 1→2 shipped and PM-reviewed against source (A–J confirmed). The M4.0b-2 instruction is consumed → archived to `context/coding-instructions/archive/`.

   **THE M4 CRITICAL PATH (next forward work, in dependency order):**
   - **M4.B3** (device-model `AttributeValue` expansion — `QuantityValue`/`ArrayValue`/`DegradedAttributeValue`/`AttributeValueUpcaster`, AMD-47). **GATED on P4** (Doc 02/05 currency — see task #0a). This is the next WU once P4 clears.
   - **M4.0b-3** (typed comparator AMD-51 + typed `StateChangedEvent` AMD-52). **GATED on M4.B3.** A clean rule-swap that reuses AMD-50's backfill path unchanged for the 2→3 transition — the supersession test is the standing N→M regression guard.
   - **Workstream C** (integration-api interface freeze, Research 6 REC-41–51). **GATED on P3** (Research 6 NQ-1..6 — task #1).
   Nothing in this chain is blocked by M4.0b-2; the gates are the open research/doc-currency items below.

0a. **DOC-CURRENCY CLEANUP PUNCH-LIST (do before / alongside M4.B3 — these are the "gaps in understanding" that can mislead a future Claude Code/Cowork session).** None are in the hivemind repo; all are in `homesynapse-core-docs` (Nick already committed the M4.0b-2 docs, so these are a fresh, separate docs commit). PM can execute on request:
    - **(i) PLAN-M4-CONSOLIDATED-v2 §3** — propagate the M4.0b-2 re-scope (backfill+version-bump on string change-detect, typed work split out) + the new **M4.0b-3** row. P2 and the plan must not silently disagree.
    - **(ii) KB currency** — `HomeSynapse_Current_State.md` / `Knowledge_Primer`: derivation is **real** (`ProductionDerivationRule`, no `MinimalDerivationRule` phantom), OR-M3-17/18 **closed**, `projectionVersion` is now **2**, AMD-50 RATIFIED + on-disk watermark **AMD-50**, the interim mixed-`lastChanged` semantics. Stale KB here is the highest-risk poison for future agent sessions.
    - **(iii) P4 Doc-02 half — DONE (2026-05-30, P4r ratification mechanics session).** **AMD-47 is RATIFIED** (Status→RATIFIED, Date applied 2026-05-30; fork resolved → `AttributeType.QUANTITY` added, 1:1 value↔type, FLOAT-reuse rejected; §9 checklist marked `[x]`). On ratification the PM: recorded AMD-47 RATIFIED (watermark **unchanged at AMD-50** — 47 < 50), registered **AMD-47-INV-01..05** into `Architecture_Invariants_v1.md` **§20** (+ §17 index/§0.3/§18 in the same commit), **folded the Doc 02 §3.7/§8.2 PENDING-AMD-47 blocks into the body** (and corrected the stale §8.2 JSR-385 `QuantityValue` row), and logged AMD-47 across the KB ledger (`Current_State`/`Knowledge_Primer`/`Decisions_Quick_Reference`/`Navigation_Index`). **M4.B3 is now UNBLOCKED** (both gates clear: AMD-47 ratified ✓ + Doc 02 currency ✓) but **NOT started** — it is the next, separate fresh Mode-3 session (the implementation WU: three records + SPI + 3 AttributeType constants + §5 contract tests + upcaster wiring per AMD-47-INV-02; no `projectionVersion` bump). **P4 Doc-05 half STILL OPEN + P3-gated:** Doc 05 (Integration Runtime) integration-api freeze content (Research 6 REC-41–51) cannot be brought current until Nick resolves Research 6 NQ-1..6 (task #1); integration AMD numbers are assign-at-milestone (P2 §4). Doc 05 gates **Workstream C**, not M4.B3 — not authored this session.
0b. **NEW FOLLOW-UP WU (tracked, not yet scheduled): timestamp-model unifier.** Move the projection's `lastChanged`/`lastReported`/possibly `lastUpdated` from projection wall-clock to event-time, retiring the M4.0b-2 interim mixed-`lastChanged`. Needs a design beat first (behavioral-contract change to `EntityState`/Doc 03, likely touches AMD-11 staleness; read-path blast radius into `MaterializedStateQueryService` + query/observability surfaces) — possibly amendment-worthy. Do NOT fold into any in-flight WU; it gets its own design pass.
0c. **~~P2 — AMD renumbering~~ — RATIFIED 2026-05-29** (`context/decisions/2026-05-29_P2_AMD_Renumbering_Decision.md`, rev. 2). Device 46–49, projection 50–52 fixed; integration assign-at-milestone (post-P3). AMD-50 authored + ratified + implemented (M4.0b-2). All prior assessment AMD numbers ≥46 are non-binding placeholders; on-disk watermark = AMD-50.
1. **Nick: NQ-1..6 strategic calls** for Research 6 v1 (`context/assessments/2026-05-22_Research_6_PM_Assessment.md`) — now **P3**, gating the M4 Workstream-C integration-api freeze content. PM recommendations recorded inline. Once Nick decides NQ-1..6, Research 6 finalizes and the integration-api amendments (renumbered per P2) proceed to ratification (AMD-61/REC-49 already withdrawn).
2. **Nick: DQ-1/2/3/5 strategic calls** for Research 4 v3. PM recommendations recorded in v2 body; DQ-4 already resolved. Once Nick decides DQ-1/2/3/5, Research 4 finalizes and AMD-48..52 firm up.
3. **Research 5 v2 FINAL post Nick review** (`context/assessments/2026-05-22_Research_5_PM_Assessment.md` v2 Addendum at bottom). All 6 NQs resolved by Nick's review — closed by LTD-08/LTD-09 lookups (Q1/Q2), INV-CE-01 (Q7), corrected listener shape (Q3), SecretStore placement (Q4), AMD-52 precedent (Q5), agreed spike sequencing (Q6). **AMD allocation:** AMD-66 (corrected non-generic `ConfigurationChangeListener`), AMD-68 (`SecureCredentialBundle` + `SecretStore.credentialsFor(String)`), AMD-69 (Argon2id + BouncyCastle), AMD-70 (`config.validation_completed` + `config.section_reloaded` events in `com.homesynapse.event`) — **4 ACTIVE, ratifiable**. AMD-64/AMD-65 **RETIRED** (REC-53/REC-54 confirm already-locked LTD-09 library choices). AMD-67 **DEFERRED** on Research 6 REC-41 (REC-56 file-schema `(major, minor)` cannot proceed until REC-41 is decided — must land in lockstep). AMD-71 **DEFERRED** to M6 planning (REC-60 directory layout — no M4 types depend). **Only remaining REC-56 decision is the Research 6 REC-41 dependency captured in task #1.** Phase 3 wiring AMDs TBD when `module-info.java` gains `requires com.networknt.schema; requires org.snakeyaml.engine; requires org.bouncycastle.provider;` directives during M6 implementation.
4. **Nick: NQ-1..7 strategic calls for Research 7 v1** (`context/assessments/2026-05-22_Research_7_PM_Assessment.md`). PM recommendations recorded inline. Key strategic decisions: (NQ-1) REC-63 vs Doc 09 §4.3-§4.5 conflict — PM recommends KEEP existing surface, add `CommandRequest.timedInteractionMs` field; (NQ-2) `Capability` enum naming clash — PM recommends rename to `ApiKeyScope`; (NQ-3) `ProblemType.typeUri()` URL scheme — PM recommends adopt `urn:homesynapse:problem:<slug>`; (NQ-4) webhook DLQ separation — PM recommends SEPARATE from subscriber DLQ; (NQ-5) WsCloseCode collision resolution — PM-proposed conservative renumbering; (NQ-6) coalescing key — PM recommends `(entityId, attributeKey)`; (NQ-7) `@Capability` annotation naming — PM recommends `@CapabilityType`. **§7 fabrication-heavy disposition** — 15 source-verified §7 issues catalogued; PM-corrected disposition table is canonical. 14 AMDs allocated (AMD-72..AMD-85) — REC-63 may collapse to 0 AMDs per NQ-1. Consider requesting Research 7 v2 from Claude Project to address §7 systematically, or proceed with PM-corrected disposition as canonical.
5. **PM: Pre-M6 spikes — Spike Q1 (SnakeYAML Engine 3.0.1 throughput on Pi 4, 500-line config), Spike Q3 (networknt 1.5.6 memory residency for core + 10 integration schemas on 256 MiB heap), Spike Q2 (Argon2id 64 MiB/3 iter/4 lanes wall-clock on Pi 4 Cortex-A72).** All three block their respective REC merges per Research 5 §5.3. Q1/Q3 before M6 coding instruction; Q2 immediately before REC-58 implementation. Hardware: dev Pi 5 (`hs-dev-1`) per established M3.4b validation pattern.
6. **~~M3.7 coding instruction~~** — **DONE 2026-05-22.** Instruction issued at `context/instructions/M3.7_E2E_Integration_Tests.md`. Four scoping decisions made and logged as D-09..D-12 in `context/decisions/phase-3-cross-module-decisions.md`. The original "after the M4 amendment-deliberation window closes" gate was removed — Decision 3 (D-11) established that M3.7 has zero technical coupling to the pending M4 amendment work. Pre-M3.7 OR-M3-17/OR-M3-18 placeholders are closed in M3.7 via `MinimalProjectionAdvancer` (Decision 1, D-09 — per Research 3 REC-20 + Research 8 v2 §M3.7 Impact). HTTP IT for M3.6e.2 endpoints and DLQ `oldestParkedAt` plumbing absorbed into M3.7 (Decision 2, D-10). Next action: Nick pastes the instruction into Claude Code (acceptEdits, Opus 4.7 xhigh) — workflow per Decision 4 (D-12). Coder produces files; Nick runs build gate + commits if GREEN.
7. **Phase 2 traceability debt** — 10 stub indexes remain (docs 02–11, 13, 14). Low priority; batch later.

## Research Pipeline Status

| Research | Status | Assessment | Next |
|---|---|---|---|
| Research 2 (Smart Home Entity Modeling) | COMPLETE (baseline) | pre-PM pipeline | — |
| Research 3 (Integration Testing) | COMPLETE | processed; all accepted | feeds M3.7 |
| Research 8 (Device Model Implementation) | COMPLETE (FINAL) | `2026-05-22_Research_8_PM_Assessment.md` | feeds M4.0 |
| Research 4 (Automation Engine) | COMPLETE (v3) | `2026-05-22_Research_4_PM_Assessment.md` | DQ-1/2/3/5 pending Nick |
| Research 6 (Integration Runtime) | COMPLETE (v1) | `2026-05-22_Research_6_PM_Assessment.md` | NQ-1..6 pending Nick |
| **Research 5 (Configuration System)** | **COMPLETE (v2 FINAL — post Nick review)** | **`2026-05-22_Research_5_PM_Assessment.md`** | **REC-56 deferred on Research 6 REC-41; other RECs ratifiable** |
| **Research 7 (REST/WebSocket API)** | **COMPLETE (v1)** | **`2026-05-22_Research_7_PM_Assessment.md`** | **NQ-1..7 pending Nick; 14 AMDs proposed AMD-72..AMD-85; 15 §7 fabrications catalogued** |

**Global allocation:** RECs allocated through REC-75 (Research 7 used REC-62..REC-75); new RECs start at REC-76. AMDs allocated/proposed through AMD-85 (AMD-47/AMD-61 withdrawn; AMD-64/AMD-65 retired post Research 5 v2; AMD-67/AMD-71 deferred; AMD-72..AMD-85 proposed by Research 7 v1 subject to NQ-1..7 dispositions). Next active block starts at AMD-86. **Research 5 v2 active AMD set: AMD-66, AMD-68, AMD-69, AMD-70. Research 7 v1 active AMD set (post-NQ resolution): tentatively AMD-72/73/74/75/76/77/78/79/80/81/82/83/84/85 — REC-63's slot retires if NQ-1 accepts existing-surface reuse, dropping to 13 AMDs.**

**Research pipeline now COMPLETE for the pre-M5 window.** All 6 research items processed; Research 7 is the last. Remaining strategic decisions for Nick: Research 4 DQ-1/2/3/5, Research 6 NQ-1..6, Research 5 NQ-resolved-but-REC-56-blocked-on-REC-41, Research 7 NQ-1..7. Once the four NQ batches are resolved, the M4 / M6 / M9 / M10 / M11 amendment-ratification + coding-instruction sequencing can begin.

**Research 5 v2 lesson encoded for future briefs:** every brief touching dependency choice must embed (a) verbatim `libs.versions.toml` rows for the relevant libraries, (b) verbatim `HomeSynapse_Core_Locked_Decisions.md` entries that lock the library *choice* (LTD-08/LTD-09 etc.), and (c) verbatim relevant `Architecture_Invariants_v1.md` entries that may make a "research question" a settled invariant (e.g., INV-CE-01 making file-vs-event source-of-truth a constitutional, not deliberative, matter). Should be added to `research-agenda.md` §2 CONSTRAINTS during the Research 7 brief authoring pass.

## Open Risks

#### OR-M3-17 — NO_OP_DERIVATION placeholder (NEW 2026-05-22)
- **Severity:** MEDIUM (placeholder blocks M3.7 E2E tests)
- **Detail:** `HomeSynapseCore` step 5 uses `NO_OP_DERIVATION` as the derivation function.
- **Resolution:** RESOLVED in M3.7. Renamed to `MINIMAL_DERIVATION_RULE = context -> List.of()`. Full derivation lands at M4.0 with REC-28.

#### OR-M3-18 — NO_OP_ADVANCER placeholder (NEW 2026-05-22)
- **Severity:** MEDIUM (placeholder blocks M3.7 E2E tests)
- **Detail:** `HomeSynapseCore` step 5 uses `NO_OP_ADVANCER` as the `ProjectionAdvancer`.
- **Resolution:** RESOLVED in M3.7. Replaced by `MinimalProjectionAdvancer` (package-private, lifecycle module) — reads from `EventStore` via bounded-window contract.

#### OR-M3-15 — Xlint:exports gateway pattern (NEW 2026-05-22)
- **Severity:** LOW (lesson learned, not regression)
- **Detail:** M3.6e.1 hit `-Xlint:exports` failures because `ReadinessFilter` (public class in exported package) referenced `io.javalin.http.Handler` from a non-transitive `requires io.javalin`. Fix: demote `ReadinessFilter` to package-private, create public `RestFilters` gateway with `Object`-typed parameter that erases the framework type from the public API surface. This is DEC-M3-16's gateway pattern applied to REST infrastructure. Two follow-up fix rounds required.
- **Resolution:** RESOLVED in M3.6e.1 at `b71ed37`. Pattern codified for future REST endpoints.

#### OR-M3-16 — Gradle/JPMS scope alignment (NEW 2026-05-22)
- **Severity:** LOW (lesson learned, not regression)
- **Detail:** M3.6e.1 second fix round: `requires transitive com.homesynapse.state` in rest-api's module-info.java required corresponding `api(project(":core:state-store"))` in build.gradle.kts (was `implementation`). Without `api`, downstream modules can't see the transitive dependency through JPMS. Pattern: `requires transitive` → `api`; plain `requires` → `implementation`.
- **Resolution:** RESOLVED in M3.6e.1 at `b71ed37`. Rule added to coder-lessons.md.

#### OR-M3-12 — DEC-M3-17 governance entry (NEW 2026-05-20)
- **Severity:** LOW (governance hygiene)
- **Detail:** HealthSignal and HealthLevel were promoted to public alongside QueueSaturationHealthCheck during M3.6d-a because the constructor's `Consumer<HealthSignal>` parameter chain leaks both types and `-Xlint:exports` would have failed otherwise. The promotion shipped with M3.6d-a `25bc23b`; DEC-M3-16 (which authorized only InProcessEventBus + SqlitePersistenceLifecycle) needed an addendum to record the 3-type promotion chain (QueueSaturationHealthCheck + HealthSignal + HealthLevel) as the minimum viable visibility unit.
- **Resolution:** RESOLVED in this WUCP Phase 2 closeout (2026-05-20). DEC-M3-17 entries appended to `HomeSynapse_Current_State.md` §3 ledger, `HomeSynapse_Core_Locked_Decisions.md` Phase 3 milestone section, and `context/decisions/phase-3-cross-module-decisions.md`.

#### OR-M3-13 — ReconciliationRecordsMetadataInDataSlot feature gap (NEW 2026-05-20)
- **Severity:** LOW (feature gap, not regression — AMD-41 §3.2.4 metadata-recording requirement was never fully implemented at any prior milestone)
- **Detail:** `StateProjection.writeCheckpoint(Instant)` passes plain `projectionVersion` to `StateCheckpointSource.serializeCheckpoint(int)`. The interface has no surface to accept `reconciledAt`, `reconciledFromVersion`, `reconciledToVersion`. `SqliteStateStore.serializeCheckpoint(int)` forwards `null` for those three fields to `CheckpointSerializer.serialize(...)`. M3.6d-a's `ReconciliationTest` ships 4 of 5 brief tests; the 5th (`reconciliationRecordsMetadataInDataSlot`) is deferred because it would fail trivially against the current contract. Implementing the feature requires extending the `StateCheckpointSource` interface and threading the metadata through `StateProjection.initialize`'s reconciliation path.
- **Resolution:** RESOLVED in M4.0a (2026-05-29, `a441fdf`). `StateCheckpointSource.serializeCheckpoint(...)` extended to accept the three reconciliation fields; `StateProjection.initialize()` populates `reconciledFrom/ToVersion` (+ `reconciledAt` from the injected `Clock`) on the version-mismatch reconciliation; `SqliteStateStore` writes them instead of `null`. `ReconciliationTest`'s 5th method un-deferred and passing (asserts `reconciledToVersion == 2`). M4.0b's backfill gate binds to this field.

#### OR-M3-14 — M3.6d-b prerequisite infrastructure (NEW 2026-05-20)
- **Severity:** MEDIUM (blocks M3.6d-b until addressed in the coding instruction)
- **Detail:** M3.6d-b requires three pieces of new persistence-layer infrastructure that the original M3.6d brief assumed already existed but do not: (1) `SqlitePersistenceLifecycle` must construct `SqliteStateStore` + `SqliteDeadLetterStore` (today constructs only the 4 main stores: EventStore, EventBusCheckpointStore, ViewCheckpointStore, WriteCoordinator); (2) `WriteCoordinator` interface needs `queueSize()` exposure for the bus's writer-queue-depth `IntSupplier` (DEC-M3-14); (3) a production `SubscriberReadConnectionFactory` implementation (today only the testFixtures `RecordingReadConnectionFactory` exists). PM owes a revised M3.6d-b coding instruction addressing these before issue.
- **Resolution:** RESOLVED 2026-05-21. All three prerequisite pieces shipped as part of the M3.6d-b 4-commit cohort: `WriteCoordinator.queueSize()` at `a33ee40`, production `SqliteSubscriberReadConnectionFactory` at `a59b64e`, `SqlitePersistenceLifecycle` 6-store expansion + `PersistenceFactory` at `725353d`, `HomeSynapseCore` composition root at `dfb045e`. Build GREEN at `dfb045e`.

#### M3.4b — Pi4SustainedLoadIT event-count tolerance
- **Severity:** LOW (informational assertion, not load-bearing)
- **Detail:** Task instruction specified ±2% event-count tolerance. Actual implementation uses lower-bound 25%. The ±2% was a calibration error — ThrottledWriteCoordinator's 10ms baseline makes 100 ev/s unachievable. The lag-bound assertion (≤50 events) is the load-bearing check.
- **Resolution:** Accepted by PM. No action needed unless the lag assertion fails in future runs.

#### M3.4b — CrashRecoveryIT Windows @TempDir caveat
- **Severity:** LOW (test infrastructure, not production)
- **Detail:** @TempDir(cleanup = CleanupMode.NEVER) required because abandoned harness holds SQLite file handles on Windows. Temp directories accumulate across test runs.
- **Resolution:** Accepted. OS handles cleanup. No production impact.

#### H2: AtomicCheckpointWriter code duplication (from M3.5b Cowork review)
- **Severity:** LOW (code quality, not correctness)
- **Detail:** Two-way and three-way methods duplicate transaction wrapper. Extract shared `executeInTransaction` helper.
- **Resolution:** RESOLVED in M4.0a (2026-05-29, `a441fdf`) as plan item H2. Shared `executeInTransaction(context, work)` helper extracted in `AtomicCheckpointWriter`; both the two-way and three-way methods route through it. Scoped to the atomic-write path.

#### Supervisor retry loop activation (from supervisor-DLQ-wiring)
- **Severity:** MEDIUM (dead code in production)
- **Detail:** computeBackoff(), sleepForBackoff(), MAX_RETRIES=5 are dead code. Current behavior parks on first failure. Activating requires moving recordCrash() to post-exhaustion path.
- **Resolution:** Separate WU. Not blocking M3.6.

#### bus.resume() does not re-spawn the VT (from M3.2)
- **Severity:** MEDIUM (blocks Tier 9 reconciliationOnVersionMismatch test)
- **Resolution:** Tracked for dedicated bus-fix Piece B WU.

## Decisions Made This Session (2026-05-22 — M3.7 scoping session)

- **D-09 — Placeholder strategy: ship `MinimalProjectionAdvancer` in M3.7.** Closes OR-M3-17 and OR-M3-18. Per Research 3 REC-20 and Research 8 v2 §M3.7 Impact ("M3.7 proceeds as planned with `MinimalProjectionAdvancer`; OR-M3-17 stays open through M3.7; closes at M4.0 with REC-28"). The full `DispatchingProjectionAdvancer` (Research 8 REC-28) lands at M4.0. `NO_OP_DERIVATION` renamed to `MINIMAL_DERIVATION_RULE` (empty-list path IS the M3.7 closure semantic); `NO_OP_ADVANCER` replaced by a real `MinimalProjectionAdvancer` (package-private in `lifecycle/lifecycle`) that reads from `EventStore` via the bounded-window contract and forwards every envelope to the processor.
- **D-10 — Pre-M3.7 bundling: absorb both follow-ups into M3.7.** (a) HTTP IT for the 5 M3.6e.2 endpoints (real Jetty + `java.net.http.HttpClient` + `json-unit-assertj`) — exactly what `HomeSynapseE2eHarness` exists to do. (b) DLQ `oldestParkedAt` field plumbing (closes M3.6e.2 D-2 deviation) — `Instant parkedAt` capture in `SubscriberDlq`, surface through `SubscriberSnapshot` (5→6 fields), populated in `DlqStatusEndpoint` response. No M3.6f split.
- **D-11 — M4-amendment posture: M3.7 proceeds in parallel.** Zero technical coupling: M3.7 exercises the M3 stack only; none of the pending M4 amendments (Research 4 DQs, Research 6 NQs, Research 5 REC-56 deferred on REC-41) change anything M3.7 touches. Original "after the M4 amendment-deliberation window closes" framing was conservative. Next Tasks #6 updated to remove the gate.
- **D-12 — Claude Code workflow: established M3.6 pattern.** acceptEdits mode, Opus 4.7 xhigh, deny `git commit`/`git push`/`./gradlew` per CLAUDE.md. Coder produces files + completion report + STOP-gate results; Nick reviews diff + runs build gate + commits if GREEN. Seventeen prior CC WUs validate the pattern.
- **REC-13 reinterpreted: no `isLive()` on `EventBus`.** `LiveModeAwaiter` polls `harness.mode()` (via `HomeSynapseCore.mode()` → `StateProjection.currentMode()`). Bus-level liveness is not a meaningful concept; liveness is per-subscriber via `SubscriberSnapshot.mode`.
- **REC-15 reinterpreted: `boundHttpPort()` placement.** Brief said "DeploymentProfile.testing() factory + boundHttpPort() accessor." `DeploymentProfile` is an enum (factory method nonsensical) and `boundHttpPort` is a runtime value (cannot live on a hardware-tier enum). Reinterpretation: 4th `TESTING` enum value on `DeploymentProfile`; `httpPort: int` field added to `HomeSynapseConfig` (2→3 fields) + `HomeSynapseConfig.testing()` static factory (port 0); `boundHttpPort() → int` on `HomeSynapseCore` (reads `javalinApp.port()` after `start()`); harness delegates.
- **No new DECs.** All scoping is implementation-pattern level; no architecture changes that warrant DEC-M3-NN.

## Decisions Made Earlier 2026-05-22 (Pre-M3.7-scoping)

- **M3.6e.2 WUCP Phase 2 completed.** All governance artifacts updated. Seventeen CC WUs total. M3.6 COMPLETE.
- **M3.6e.2 delivered and committed at `76288af`.** 5 endpoint handlers, 2 RestFilters gateway methods, 2 ArchUnit rules, EndpointContext SPI, 16-step bootstrap. 5 deviations (all non-blocking, PM-accepted).
- **OR-M3-17 + OR-M3-18 logged (open).** NO_OP_DERIVATION and NO_OP_ADVANCER placeholders in HomeSynapseCore. Must be resolved before M3.7 → **now scheduled for M3.7 itself per D-09**.
- **OR number collision fixed.** Coder's OR-M3-15/OR-M3-16 (NO_OP placeholders) renumbered to OR-M3-17/OR-M3-18 to avoid collision with PM's OR-M3-15 (Xlint:exports) and OR-M3-16 (Gradle/JPMS scope), both RESOLVED.

### Decisions from prior sessions (carried for reference)

- **DEC-M3-17 (2026-05-20):** HealthSignal + HealthLevel public visibility (DEC-M3-16 addendum). APPLIED in M3.6d-a `25bc23b`.
- **DEC-M3-16 (2026-05-20):** Composition-root visibility strategy. InProcessEventBus → public (M3.6b `df2743a`). SqlitePersistenceLifecycle → factory pattern via PersistenceFactory (M3.6d-b `725353d`). QueueSaturationHealthCheck + HealthSignal + HealthLevel → public (M3.6d-a `25bc23b`, DEC-M3-17).
- **M3.6e scope expansion approved:** +Javalin server, +3 admin endpoints (M3.5b gap — DlqAdminEndpoint, ProjectionRebuildEndpoint, ProjectionStatusEndpoint), +6 ArchUnit rules. Splits into M3.6e.1 (StateQueryService + REST gate) / M3.6e.2 (admin endpoints + ArchUnit rules).
- **M3.7 ingress:** EventPublisher.publish() directly (no HTTP ingress endpoint).
- **ReadinessFilter:** Javalin `before` handler (option a).
- **Javalin thread pool on DeploymentProfile:** STUDIO(1/4), HOME(2/8), PERFORMANCE(4/16).

## Audit Findings Closure Update (2026-05-20)

- **CLOSED (M3.6a):** C-01, D1-05, D1-13, D2-11, D5-04
- **CLOSED (M3.6b):** D1-07, D4-09
- **CLOSED (M3.6d-a):** D3-08 (`DerivedWriteRateLimit.refill()` + `QueueSaturationHealthCheck.tick()` scheduler wired via `SharedScheduler`)
- **DEFERRED (MINOR / future WU):** D1-02, D1-16, D1-19, D5-08, D5-09

## Critical Path

**M4.0a coding instruction.** M3 COMPLETE; M4 scoping COMPLETE (PLAN-M4-CONSOLIDATED, canonical scope). The critical path within M4 is **Workstream A**: M4.0a (AMD-45 atomic checkpoint) → M4.0b (`DispatchingProjectionAdvancer` REC-28 + real `DerivationRule` + one-shot backfill on the `projectionVersion` 1→2 reconciliation replay). All state-based behavior is dark until M4.0b lands. Research 9 (projection rebuild/backfill) + Research 10 (typed change-detection) inform M4.0b; P2 (AMD renumbering) + P3 (Research 6 NQ-1..6) gate the broader M4 amendments. Research 4 DQ-1/2/3/5 and Research 7 NQ-1..7 remain open but are M7/M10/M11 — they do not gate M4.

## Open Risks/Concerns from M3 Closeout Readiness Deliberation

1. **M3.6e scope (9-12h, largest single WU)** — split into M3.6e.1/e.2 mitigates.
2. ~~**SqlitePersistenceLifecycle factory pattern needed (M3.6d)** — DEC-M3-16.~~ RESOLVED: `PersistenceFactory` public gateway shipped M3.6d-b `725353d`.
3. **Admin endpoint gap from M3.5b** — DlqAdminEndpoint, ProjectionRebuildEndpoint, ProjectionStatusEndpoint bundled into M3.6e.2.
4. **6 missing ArchUnit rules** — bundled into M3.6e.2.
5. ~~**@Disabled("M3.5a") reconciliation test** — un-disable in M3.6d.~~ RESOLVED: un-disabled in M3.6d-a `25bc23b`.
6. **bus.resume() VT re-spawn** — NOT M3 blocker (tracked for M4).

## Completed Since Last Update (2026-05-22)

| WU | Commit | Date | Scope |
|---|---|---|---|
| M3.6e.2 | `76288af` | 2026-05-22 | Admin endpoints (DlqStatusEndpoint, ProjectionStatusEndpoint) + entity query endpoints (ListEntitiesEndpoint, GetEntityEndpoint, GetEntityStateEndpoint) + EndpointContext SPI + 2 RestFilters gateway methods + 2 ArchUnit rules (QUERY_SERVICE_READ_ONLY, REST_ENDPOINTS_NO_EVENT_PUBLISHING) + HomeSynapseCore 16-step bootstrap. 15 created, 6 modified, 19 test methods. 5 deviations (none blocking). Seventeenth CC WU. M3.6 COMPLETE. |
| M3.6e.1 | `b71ed37` | 2026-05-22 | MaterializedStateQueryService + ReadinessFilter + RestFilters (DEC-M3-16 gateway) + Javalin bootstrap (14-step) + DeploymentProfile thread pool sizing. Two fix rounds (Xlint:exports, Gradle/JPMS scope). 7 deviations (none blocking). 6 created, 13 modified, +22 test methods. Sixteenth CC WU. |
| M3.6d-b | `dfb045e` | 2026-05-21 | PersistenceFactory + HomeSynapseCore composition-root wiring (4-commit cohort: `a33ee40`..`dfb045e`). WriteCoordinator.queueSize(), SqliteSubscriberReadConnectionFactory, SqlitePersistenceLifecycle 6-store expansion, PersistenceFactory public gateway, HomeSynapseCore 12-step bootstrap. 20 files, +1,432 lines. OR-M3-14 RESOLVED. |

## Completed Since Last Update (2026-05-20)

| WU | Commit | Date | Scope |
|---|---|---|---|
| M3.6a | `17c40b6` | 2026-05-20 | Profile-driven persistence config — DeploymentProfile 6 fields, LockingMode, PRAGMAs |
| M3.6b | `df2743a` | 2026-05-20 | EventBusConfig + InProcessEventBus public (DEC-M3-16) |
| M3.6c | `38d3e30` | 2026-05-20 | Per-module event-class manifests (Q3 gap closure) |
| M3.6d-a | `25bc23b` | 2026-05-20 | Composition-root satellite changes (DEC-M3-17 visibility chain, ReadinessSource, ReconciliationTest 4/5, Tier 9 un-disabled, lifecycle skeletons, SLF4J wiring) |

## Completed Since Last Update (2026-05-18 through 2026-05-19)

| WU | Commit | Date | Scope |
|---|---|---|---|
| Bus-Fix Piece A | `fceafe8` | 2026-05-18 | DerivedWriteRateLimit visibility promotion |
| M3.5b | `08d0136` | 2026-05-18 | StateProjection production persistence |
| Proj-Checkpoint Wiring | `56aaa4b` | 2026-05-19 | StateCheckpointSource + size guardrail |
| Supervisor DLQ Wiring | `ed5862c` | 2026-05-19 | 11-field DeadLetter + PersistentDlqWriter |
| M3.4a | `5ae7912` | 2026-05-19 | Integration-test scaffold (module 20) |
| M3.4b | `adf04d2` | 2026-05-19 | Sustained-load + crash-recovery tests |

## What Will Be Different Going Forward

- **Freshness preflight** runs at the start of every PM session. If the hivemind is declared stale, the only allowed task is running WUCP Phase 2 retroactively for the last completed work unit. See `project-manager/references/freshness-preflight.md`. **This is exactly what triggered today's session** — 5 work units accumulated PM-side without WUCP Phase 2; this catch-up restored PASS state.
- **Deferred build gate risk tracking** is a PM responsibility. Every coder-handoff that defers `./gradlew check` must be listed here under "Open Risks" until Nick resolves it.
- **No work unit is "done" until both WUCP phases have been executed.** Completion of a work unit is a prerequisite for starting the next.
- **Dual-skill sync check** runs at WUCP Phase 2 step 10. Any edit to files under `ClaudeFolder/nexsys-hivemind/{coder,project-manager}/` must be mirrored into `.claude/skills/nexsys-{coder,project-manager}/`, verified by `diff -rq`. None of today's five WUCP closeouts touched skill files; sync check expected PASS.
- **M3 prompt pattern:** Settled decision points from deliberation documents go into Cowork prompts as fixed constraints (not open questions). STOP-on-Mismatch gates include interface-shape tests. Specify `default` vs abstract for new interface methods. For any type the brief asserts is cross-module accessible, include a visibility-gate that verifies the `public` modifier on the class declaration (lesson from M3.5a G4 — codified in `coding-instruction-format.md`).

---

## M3.6e.2 — PM Closeout — 2026-05-22

**Work unit:** M3.6e.2 — Admin Endpoints + ArchUnit Rules
**Coder surface:** Claude Code (seventeenth CC WU)
**Build gate:** RESOLVED. Full `./gradlew check` GREEN at `76288af`. Build confirmed by Nick.

**Scope:** Delivers the final M3.6 sub-WU — admin/operational endpoints, entity query endpoints, and architectural enforcement rules. M3.6 is COMPLETE after this WU.

**Key deliverables:**
1. **5 endpoint handlers** (all package-private in rest-api): `ListEntitiesEndpoint`, `GetEntityEndpoint`, `GetEntityStateEndpoint`, `DlqStatusEndpoint`, `ProjectionStatusEndpoint`.
2. **`EndpointContext` SPI** (package-private interface + `JavalinEndpointContext` adapter): Implementation-level abstraction isolating endpoint handlers from Javalin framework types. Not in the original coding instruction — Coder-introduced for testability.
3. **`EndpointResponses`** (package-private utility): Shared response serialization helpers.
4. **2 `RestFilters` gateway methods** (`addEntityEndpoints`, `installAdminEndpoints`): Public entry points with `Object`-typed parameters per DEC-M3-16.
5. **2 ArchUnit rules** (`QUERY_SERVICE_READ_ONLY`, `REST_ENDPOINTS_NO_EVENT_PUBLISHING`): Enforce read-only discipline and event-publish isolation for REST endpoints. Total ArchUnit rules now 9.
6. **`HomeSynapseCore` 16-step bootstrap** (expanded from 14): Steps 13–14 register entity query endpoints and admin endpoints via `RestFilters` gateway.
7. **19 test methods** across 5 test classes + 2 test helpers (`RecordingEndpointContext`, `FakeStateQueryService`).

**Deviations (5, none blocking):**
1. **[REVIEW] D-1** — `ListEntitiesEndpoint` omits `subjectType` field (not on `EntityState` record).
2. **[REVIEW] D-2** — `DlqStatusEndpoint` uses `dlqDepth`/`crashCount` from `SubscriberSnapshot` instead of brief's `parkedCount`/`oldestParkedAt`.
3. **[REVIEW] D-3** — `REST_ENDPOINTS_NO_EVENT_PUBLISHING` uses `accessClassesThat().belongToAnyOf(EventPublisher.class)` instead of brief's `callMethodWhere` form.
4. **[INFO] D-4** — Both `LongSupplier` args at `RestFilters.installAdminEndpoints` wired to `stateProjection::cursorPosition`.
5. **[INFO] D-5** — Extra `sortDescReversesOrder` test (19 total instead of brief's ~18).

**OR number collision fixed:** Coder's OR-M3-15 (NO_OP_DERIVATION) and OR-M3-16 (NO_OP_ADVANCER) renumbered to OR-M3-17 and OR-M3-18 to avoid collision with PM's OR-M3-15 (Xlint:exports, RESOLVED) and OR-M3-16 (Gradle/JPMS scope, RESOLVED).

**Stats:** 15 files created, 6 modified. +19 test methods.

**WUCP Phase 2 completed:**
- [x] PROJECT_SNAPSHOT.md updated (M3.6e.2 DONE, M3.6 COMPLETE, M3.7 NEXT, code state, seventeen CC WUs)
- [x] pm-handoff.md updated (this entry)
- [x] coder-handoff.md updated (OR collision fixed, deferred gate resolved, M3.6e.2 content)
- [x] phase-3-milestone-backlog.md M3.6e.2 marked DONE; M3.7 NEXT
- [x] 2026-W21 weekly plan updated
- [x] HomeSynapse_Current_State.md updated
- [x] HomeSynapse_Knowledge_Primer.md updated
- [x] Locked Decisions — no new DECs needed
- [x] Dual-skill sync check
- [x] OR-M3-17 + OR-M3-18 logged (open)
- [x] MODULE_CONTEXT.md files — already updated by Coder during M3.6e.2 (rest-api + lifecycle); cannot verify from this session (homesynapse-core repo not mounted)

**Next work unit:** M3.7 — E2E integration tests (scoping via research pipeline).

---

## M3.6e.1 — PM Closeout — 2026-05-22

**Work unit:** M3.6e.1 — StateQueryService + REST Readiness Gate
**Coder surface:** Claude Code (sixteenth CC WU)
**Build gate:** RESOLVED. Full `./gradlew check` GREEN at `b71ed37`. 139 tasks, 0 failures. Two follow-up fix rounds required before GREEN.

**Scope:** Delivers the StateQueryService implementation, REST readiness infrastructure, and Javalin HTTP server bootstrap. This is the first M3.6 sub-WU where the composition root becomes externally observable (HTTP port 7070).

**Key deliverables:**
1. **`MaterializedStateQueryService`** (public final in state-store): Implements `StateQueryService` with 5 methods delegating to `StateProjection`. Static factory `create(StateProjection)`. Returns `Optional.empty()` / empty `Map` when projection not LIVE (no exceptions for callers to catch).
2. **`ReadinessFilter`** (package-private in rest-api): Javalin `before` handler checking `ReadinessSource.mode() == LIVE`. Returns 503 with JSON `{"error":"Service not ready","mode":"..."}` when not LIVE. Package-private due to `-Xlint:exports` (references `io.javalin.http.Handler`).
3. **`RestFilters`** (public final in rest-api): DEC-M3-16 gateway wrapping `ReadinessFilter`. `readinessFilter(ReadinessSource)` returns `Object` (erases Javalin type from public API surface). Callers cast at registration site.
4. **`ProblemType.STATE_STORE_REPLAYING`** (new enum constant in rest-api): HTTP 503 problem type for readiness-gated responses.
5. **Javalin bootstrap in `HomeSynapseCore`**: 14-step bootstrap (expanded from 12). Steps 13–14: `MaterializedStateQueryService.create(stateProjection)` + Javalin server on port 7070 with readiness filter. `DeploymentProfile` gains `httpThreads()` and `httpMaxThreads()` (STUDIO 1/4, HOME 2/8, PERFORMANCE 4/16).
6. **22 new test methods** across `MaterializedStateQueryServiceTest` (7 unit), `ReadinessFilterTest` (6 unit), `RestFiltersTest` (2 unit), `HomeSynapseCoreTest` updates (7 additions).

**Fix rounds:**
- **Fix round 1 (Xlint:exports):** `ReadinessFilter` was initially public but referenced `io.javalin.http.Handler` from non-transitive `requires io.javalin`. Fix: demote to package-private, create `RestFilters` gateway per DEC-M3-16 pattern. OR-M3-15.
- **Fix round 2 (Gradle/JPMS scope):** `requires transitive com.homesynapse.state` in rest-api module-info required `api(project(":core:state-store"))` in build.gradle.kts (was `implementation`). OR-M3-16.

**Deviations (7, none blocking):**
1. `MaterializedStateQueryService` uses static factory instead of public constructor — matches DEC-M3-16 pattern.
2. `ReadinessFilter` package-private instead of public — forced by `-Xlint:exports`.
3. `RestFilters` gateway added (not in original instruction) — DEC-M3-16 pattern.
4. `ProblemType.STATE_STORE_REPLAYING` added — needed for 503 response body.
5. `DeploymentProfile` thread pool fields added inline — not split to separate commit.
6. `HomeSynapseCoreTest` expanded beyond instruction scope — additional bootstrap assertions.
7. rest-api `build.gradle.kts` `implementation` → `api` for state-store dependency — JPMS transitive requirement.

**Stats:** 6 files created, 13 modified. +22 test methods.

**WUCP Phase 2 completed:**
- [x] PROJECT_SNAPSHOT.md updated (M3.6e.1 DONE, M3.6e.2 NEXT, code state, rest-api module, lifecycle 14-step, state-store MaterializedStateQueryService, sixteen CC WUs)
- [x] pm-handoff.md updated (this entry)
- [x] coder-handoff.md updated
- [x] phase-3-milestone-backlog.md M3.6e.1 marked DONE; M3.6e.2 NEXT
- [x] 2026-W21 weekly plan updated
- [x] HomeSynapse_Current_State.md updated
- [x] HomeSynapse_Knowledge_Primer.md updated
- [x] Locked_Decisions.md — no new DECs (DEC-M3-16 gateway pattern already logged; applied again here)
- [x] Dual-skill sync check
- [x] OR-M3-15 + OR-M3-16 logged and resolved

**Next work unit:** M3.6e.2 — Admin endpoints + ArchUnit rules (coding instruction produced this session).

---

## M3.6d-b — PM Closeout — 2026-05-22

**Work unit:** M3.6d-b — PersistenceFactory + HomeSynapseCore Composition-Root Wiring
**Coder surface:** Claude Code
**Build gate:** RESOLVED. Full `./gradlew check` GREEN at `dfb045e`. Build confirmed by Nick.

**Scope:** Delivers the composition-root wiring deferred from M3.6d-a, plus the three OR-M3-14 prerequisite infrastructure pieces. Shipped as a 4-commit cohort:

1. **`a33ee40` — WriteCoordinator.queueSize():** Added `int queueSize()` to the `WriteCoordinator` interface and implementation, exposing the internal `AsyncWriteQueue` size for the bus's writer-queue-depth `IntSupplier` (DEC-M3-14).
2. **`a59b64e` — Production SqliteSubscriberReadConnectionFactory:** New `SqliteSubscriberReadConnectionFactory` (public) + `SqliteSubscriberReadExecutor` (package-private) in `core/persistence`. Provides production `SubscriberReadConnectionFactory` implementation (previously only testFixtures `RecordingReadConnectionFactory` existed).
3. **`725353d` — PersistenceFactory + SqlitePersistenceLifecycle 6-store expansion:** `PersistenceFactory` (public final, implements `AutoCloseable`) wraps package-private `SqlitePersistenceLifecycle` per DEC-M3-16 factory pattern. `SqlitePersistenceLifecycle` expanded from 4 stores to 6 (added `SqliteStateStore` + `SqliteDeadLetterStore`). 8 accessor methods on `PersistenceFactory`. Static `start(Path, PersistenceConfig, Clock, HomeId, List<Class<? extends DomainEvent>>)` factory.
4. **`dfb045e` — HomeSynapseCore composition root:** Public final class implementing `ReadinessSource`. 4-arg constructor `(Path, HomeSynapseConfig, Clock, HomeId)`. 12-step bootstrap sequence: PersistenceFactory.start → BusMetrics.jfr → InProcessEventBus(7-arg) → DerivedWriteRateLimit → StateProjection.create(11-param) → subscribeRuntime → healthSignalHandler → QueueSaturationHealthCheck → SharedScheduler → started=true → CompletableFuture.completedFuture. NO_OP_DERIVATION (OR-M3-15) and NO_OP_ADVANCER (OR-M3-16) stubs. `stateQueryService()` returns `ThrowingStateQueryService` placeholder. `stop()` tears down in reverse order. Module-info gained `requires com.homesynapse.integration` (non-transitive, for `IntegrationEvents` aggregation).

**Stats:** 20 files changed, +1,432 insertions, -14 deletions across persistence and lifecycle modules.

**Deviations:** None. All shipped code matches the revised M3.6d-b coding instruction (which incorporated OR-M3-14 prerequisite infrastructure).

**OR-M3-14 RESOLVED:** All three prerequisite infrastructure gaps closed — `WriteCoordinator.queueSize()` (`a33ee40`), `SqliteSubscriberReadConnectionFactory` (`a59b64e`), `SqlitePersistenceLifecycle` 6-store expansion (`725353d`).

**OQ-05-03 RESOLVED:** The three prerequisite gaps were bundled into M3.6d-b (not split into a separate WU).

**WUCP Phase 2 completed:**
- [x] PROJECT_SNAPSHOT.md updated (type counts, code state, tracked gaps closed, M3.6d-b row)
- [x] pm-handoff.md updated (this entry)
- [x] coder-handoff.md updated
- [x] open-questions.md OQ-05-03 moved to Resolved
- [x] phase-3-milestone-backlog.md M3.6d-b marked DONE; M3.6e.1 NEXT
- [x] 2026-W21 weekly plan updated
- [x] HomeSynapse_Current_State.md updated
- [x] HomeSynapse_Knowledge_Primer.md updated
- [x] Dual-skill sync check

**Next work unit:** M3.6e.1 — StateQueryService + REST gate.

---

## M3.6d-a — PM Closeout — 2026-05-20

**Work unit:** M3.6d-a — Composition-Root Satellite Changes
**Coder surface:** Claude Code
**Build gate:** RESOLVED. Full `./gradlew check` GREEN at `25bc23b` (post-SLF4J follow-up fix). 137 actionable tasks (134 executed, 3 up-to-date).

**Scope:** Delivers the independent pieces of the composition root that do NOT depend on persistence-side infrastructure work the original M3.6d brief assumed already existed. `SqliteStateStore implements StateCheckpointSource` (method rename `serialize` → `serializeCheckpoint`, public promotion via interface; class itself stays package-private). `QueueSaturationHealthCheck` + `HealthSignal` + `HealthLevel` promoted to public per DEC-M3-17 (transitive 3-type chain). `ReadinessSource` public interface in `core/state-store` (single method `mode() → SubscriberMode`; consumed by M3.6e's MaterializedStateQueryService for REST/WebSocket readiness gating). `ReconciliationTest` (4 of 5 brief methods; metadata-recording test deferred as feature gap — OR-M3-13). Tier 9 `reconciliationOnVersionMismatch` un-disabled and implemented (subscribe → wait LIVE → unsubscribe → externally reset checkpoint to 0 → re-subscribe → assert 10 events re-replayed). Lifecycle module skeletons: `HomeSynapseConfig` (public record), `SharedScheduler` (package-private final — 50 ms refill + 1 s tick, daemon thread `hs-sched-0`, `safelyInvoke` cadence defence), `ThrowingStateQueryService` (package-private final — all 5 methods throw `IllegalStateException("StateQueryService not yet wired — available after M3.6e")`). Module-info gained `requires transitive` for persistence/event.bus/state-store + non-transitive `requires org.slf4j` for SharedScheduler's internal logging. 18 files (6 new + 12 modified). Same-day SLF4J follow-up fix added `requires org.slf4j` to lifecycle module-info and `implementation(libs.slf4j.api)` to build.gradle.kts (canonical M2.2 pattern from `core/persistence`).

**M3.6d sub-division decision:** original M3.6d brief assumed prerequisites that don't exist: `SqlitePersistenceLifecycle` doesn't construct `SqliteStateStore`/`SqliteDeadLetterStore`; no `WriteCoordinator.queueSize()`; no production `SubscriberReadConnectionFactory`; `HealthSignal`/`HealthLevel` are package-private; `SubscriberInfo`/`SubscriptionFilter` shapes differ from the brief. User chose Option A (sub-divide). M3.6d-a covers the independent satellite changes; M3.6d-b addresses the prerequisite infrastructure plus actual `PersistenceFactory` + `HomeSynapseCore` wiring.

**Deviations:**
- **D-1 [REVIEW]:** HealthSignal + HealthLevel public promotion (not authorized by brief). The 3-type chain was required by `-Xlint:exports` analysis. Logged as DEC-M3-17.
- **D-2 [INFO]:** ReconciliationTest ships 4 of 5 methods (5th deferred as OR-M3-13).
- **D-3 [INFO]:** SharedScheduler has a secondary `(Runnable, Runnable)` constructor for testability (final collaborators cannot be mocked).
- **D-4 [INFO]:** SharedSchedulerTest ships 5 tests; the 5th (`taskFailureDoesNotSilenceCadence`) pins `safelyInvoke` behaviour.
- **D-5 [INFO]:** `shutdownTerminatesWithin2Seconds` renamed to `shutdownTerminatesWithoutThrowing` to honor `NO_DIRECT_TIME_ACCESS`.
- **D-6 [INFO]:** Major scope reduction from original M3.6d brief per Option A.

**Audit findings closed:** D3-08 (scheduler wiring for refill+tick via SharedScheduler).

**Tier 9 gap closed:** the `@Disabled("M3.5a")` reconciliationOnVersionMismatch contract test is now active. M3.2 carry-forward gap #1 (Tier 9 disable) RESOLVED.

**WUCP Phase 2 completed:**
- [x] HomeSynapse_Current_State.md updated
- [x] HomeSynapse_Knowledge_Primer.md updated
- [x] HomeSynapse_Core_Locked_Decisions.md updated (DEC-M3-17 logged)
- [x] PROJECT_SNAPSHOT.md updated
- [x] pm-handoff.md updated (this entry)
- [x] coder-handoff.md "FOUR OPEN" correction (now ZERO OPEN; all four 2026-05-20 WUs resolved at commit)
- [x] phase-3-milestone-backlog.md M3.6d-a marked DONE; M3.6d sub-divide noted; M3.6d-b NEXT
- [x] 2026-W21 weekly plan updated
- [x] context/decisions/phase-3-cross-module-decisions.md D-08 added (visibility-promotion transitive verification pattern)

**Open risks added:** OR-M3-12 (DEC-M3-17 entry — RESOLVED in this closeout), OR-M3-13 (reconciliation metadata feature gap), OR-M3-14 (M3.6d-b prerequisite infrastructure).

**Next work unit:** M3.6d-b.

---

## Prior PM Closeouts (archived)

| Closeout | Commit | Date | One-line scope |
|---|---|---|---|
| M3.6c | `38d3e30` | 2026-05-20 | Per-Module Event-Class Manifests — `EventTypes.CORE_PRODUCTION_EVENT_CLASSES` + `IntegrationEvents.LIFECYCLE_EVENT_CLASSES` aggregated at composition root |
| M3.6b | `df2743a` | 2026-05-20 | `EventBusConfig` record + `InProcessEventBus` public visibility (DEC-M3-16) |
| M3.6a | `17c40b6` | 2026-05-20 | Profile-Driven Persistence Configuration — DeploymentProfile threaded through PersistenceConfig → DatabaseExecutor (closes C-01) |
| M3.4b | `adf04d2` | 2026-05-19 retroactive | Sustained-Load + Crash-Recovery ITs; ThrottledWriteCoordinator decorator |
| M3.4a | `5ae7912` | 2026-05-19 retroactive | Integration Test Module Scaffold + Harness (new `testing/integration-tests` module) |
| Supervisor DLQ Wiring | `ed5862c` | 2026-05-19 retroactive | `SubscriberSupervisor.deliver()` → `DeadLetter` via `SubscriberDlq.park`; 12-method test class |
| Projection-Checkpoint Wiring | `56aaa4b` | 2026-05-19 retroactive | `StateCheckpointSource` interface + 10 MB advisory guardrail |
| M3.5b | `08d0136` | 2026-05-19 retroactive | StateProjection Production Persistence — `SqliteStateStore` + `SqliteDeadLetterStore` + `CheckpointSerializer` + V004 |
| Bus-Fix Piece A | `fceafe8` | 2026-05-19 retroactive | `DerivedWriteRateLimit` package-private → public; closes M3.5a G4 mismatch |

Full PM closeout bodies for each row live in `archive/pm-handoff-2026-05.md`.

---

**Last verified against:** `homesynapse-core` commit `76288af` on `2026-05-22`.
