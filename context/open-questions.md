<!--
file: context/open-questions.md
purpose: Inter-agent register of open questions and verify-needed items. PM consults before issuing instructions; Coder consults before executing.
audience: PM, Coder
update-cadence: per-WU
state-type: comms
status: CURRENT
last-verified: 2026-05-30 against `homesynapse-core` commit `60b4185` (reconciled: OQ-05-02/04 → Resolved; OQ-05-06..10 added to match PROJECT_SNAPSHOT).
-->

# Open Questions Register

Inter-agent typed-message surface for `[OPEN-QUESTION]` and `[VERIFY-NEEDED]`. See `coder/CLAUDE.md §Message Protocol` and `project-manager/CLAUDE.md §Message Protocol` for the routing rules, and `REORGANIZATION_PLAN_2026-05-20.md §5b` for the entry template.

- **Active** items live above the `---` separator and must be resolved (or explicitly carried forward) before any WU they `Blocking:` can close.
- **Resolved** items move below the separator for one milestone, then archive on the same cadence as the handoffs.
- Numbering follows `OQ-MM-NN` per PLAN §5c. The current series (`OQ-05-*`) restarts numbering for the 2026-05 milestone and back-references prior `OR-M3-NN` entries in `pm-handoff.md` via the `Context:` field.

## Active

## [OPEN-QUESTION] OQ-05-06 — Typed attribute change-detection design (gates M4.0b-3)
**Posed by:** Cowork (M4 scoping)
**Posed:** 2026-05-28 (logged 2026-05-30)
**Blocking:** authoring the real **AMD-51** (typed comparator) + **AMD-52** (typed `StateChangedEvent`) → blocks the **M4.0b-3** coding instruction.
**Question:** Comparison semantics per `AttributeValue` variant, threshold/deadband model + where it's declared, comparator contract shape, and typed-event payload — now that `AttributeValue` is 8 typed variants (AMD-47, M4.B3 `60b4185`) but the projection still compares as strings.
**Context:** Driven by **Research 10** (issued 2026-05-28, running in the HomeSynapse Core Claude Project). No `Research_10_PM_Assessment.md` exists yet. The highest-risk sub-problem is the AMD-52 typed-event serializer/replay blast radius (`CheckpointSerializer`/Jackson + replay determinism + upcaster). Design-track map: `context/planning/2026-05-30_M4.0b-3_design-track-map.md`. Cross-ref: `context/instructions/Research_10_Typed_Attribute_Change_Detection_Brief.md`; `core/state-store/MODULE_CONTEXT.md`; `core/device-model/MODULE_CONTEXT.md`.
**Resolution:** _(open — pending Research 10 results → PM assessment → Nick's NQ-10-* calls)_

## [OPEN-QUESTION] OQ-05-07 — Research 9 residuals (operator rebuild / partial backfill / observability / failure semantics)
**Posed by:** Cowork (M4 scoping)
**Posed:** 2026-05-28 (logged 2026-05-30)
**Blocking:** none on the M4 critical path — AMD-50 shipped the core backfill mechanism (M4.0b-2). Residuals are forward/operational (M5+).
**Question:** Operator-triggered rebuild, partial/per-entity backfill, backfill observability, and backfill failure semantics — the four NQ-9 residuals that extend (do not redesign) the frozen AMD-50 mechanism.
**Context:** Research 9 (issued 2026-05-28, Claude Project) is largely superseded by AMD-50. No `Research_9_PM_Assessment.md` exists yet. Do NOT reopen the frozen mechanism. Cross-ref: `context/instructions/Research_9_Projection_Rebuild_Backfill_Brief.md`.
**Resolution:** _(open — deferrable; revisit at M4.0b-3 close or when an operator-rebuild need surfaces)_

## [OPEN-QUESTION] OQ-05-05 — Research 6 NQ-1..6 confirmations (P3)
**Posed by:** Cowork (M4 scoping)
**Posed:** 2026-05-28
**Blocking:** finalizing the M4 Workstream-C integration-api interface freeze (NOT M4.0b-3).
**Question:** Confirm or override the PM recommendations for Research 6 NQ-1..6 (SecurityServices aggregator; schemaVersion split; capability identity = sealed `Capability` permit + `CapabilityInstance`; no new SQLite table; reject REC-49; keep 1/60s restart default with per-descriptor override).
**Context:** These shape the *content* of the integration-api amendments that ride the M4 freeze (supervisor impl stays M9). PM recommendations inline in `context/assessments/2026-05-22_Research_6_PM_Assessment.md`. NOTE: the M4.0b attribute-backfill question is **already decided** (one-shot backfill, Nick 2026-05-28) and is not open.
**Resolution:** _(open — Nick's calls)_

---

## Resolved (this milestone)

## [RESOLVED] OQ-05-02 — `StateCheckpointSource` reconciliation-metadata threading
**Resolved:** 2026-05-29 (M4.0a, `a441fdf`). `StateCheckpointSource.serializeCheckpoint(...)` extended to accept `reconciledAt`/`reconciledFromVersion`/`reconciledToVersion`; threaded through `StateProjection.initialize()`'s version-mismatch branch; `SqliteStateStore` writes them instead of `null`; `ReconciliationTest`'s 5th method un-deferred and passing. (Posed by Coder, M3.6d-a closeout, 2026-05-20; OR-M3-13.)

## [RESOLVED] OQ-05-04 — M4 AMD renumbering allocation (P2)
**Resolved:** 2026-05-29 (P2 RATIFIED, `context/decisions/2026-05-29_P2_AMD_Renumbering_Decision.md`). Device 46–49, projection 50–52 fixed; integration assign-at-milestone; **all prior-assessment AMD numbers ≥46 are non-binding placeholders.** AMD-50 authored/ratified/implemented (M4.0b-2). (Posed by Cowork, M4 scoping, 2026-05-28.)

## [OPEN-QUESTION] OQ-05-03 — M3.6d-b prerequisite infrastructure: bundle into the brief or split into its own WU?
**Posed by:** Coder (mid-M3.6d execution)
**Posed:** 2026-05-20
**Blocking:** M3.6d-b (PersistenceFactory + HomeSynapseCore composition-root wiring).
**Question:** Are the three M3.6d-b prerequisite gaps (SqlitePersistenceLifecycle constructing SqliteStateStore + SqliteDeadLetterStore, `WriteCoordinator.queueSize()` exposure, production `SubscriberReadConnectionFactory`) bundled into the revised M3.6d-b coding instruction, or split into a separate prerequisite WU before M3.6d-b begins?
**Context:** The original M3.6d brief assumed all three existed; they do not. (1) `SqlitePersistenceLifecycle` constructs only the four main stores today (EventStore, EventBusCheckpointStore, ViewCheckpointStore, WriteCoordinator) — must also construct `SqliteStateStore` + `SqliteDeadLetterStore`. (2) `WriteCoordinator` interface needs `queueSize()` exposure for the bus's writer-queue-depth `IntSupplier` (DEC-M3-14). (3) Today only the testFixtures `RecordingReadConnectionFactory` exists; M3.6d-b needs a production `SubscriberReadConnectionFactory`. Estimated work-unit-size impact: bundling grows M3.6d-b from 6–8h to 10–12h. Cross-reference: `pm-handoff.md` OR-M3-14.
**Resolution:** RESOLVED 2026-05-21. Bundled into the revised M3.6d-b coding instruction. All three prerequisite pieces shipped as part of the M3.6d-b 4-commit cohort: `WriteCoordinator.queueSize()` at `a33ee40`, production `SqliteSubscriberReadConnectionFactory` at `a59b64e`, `SqlitePersistenceLifecycle` 6-store expansion + `PersistenceFactory` at `725353d`, `HomeSynapseCore` composition root at `dfb045e`. Build GREEN at `dfb045e`.

## [OPEN-QUESTION] OQ-05-01 — DEC-M3-16 addendum to record the transitive 3-type promotion chain
**Posed by:** PM (M3.6d-a closeout)
**Posed:** 2026-05-20
**Blocking:** M3.6d-a closeout (governance hygiene).
**Question:** Does DEC-M3-16's authorization cover only the named class (`QueueSaturationHealthCheck`) or also the types its public constructor transitively leaks (`HealthSignal`, `HealthLevel`)? If transitive, do we need a new DEC entry recording the chain?
**Context:** `QueueSaturationHealthCheck`'s public constructor accepts `Consumer<HealthSignal>`, and `HealthSignal` has a `HealthLevel` enum field. `-Xlint:exports` requires all three types to be public simultaneously — the chain is the minimum viable visibility unit. The promotion shipped with M3.6d-a `25bc23b`, but DEC-M3-16 (authored before the chain was understood) named only `InProcessEventBus` and `SqlitePersistenceLifecycle`. Cross-reference: `pm-handoff.md` OR-M3-12.
**Resolution:** RESOLVED 2026-05-20. New entry DEC-M3-17 ("HealthSignal + HealthLevel public visibility — DEC-M3-16 addendum") appended to `project-knowledge/HomeSynapse_Current_State.md §3`, `project-knowledge/HomeSynapse_Core_Locked_Decisions.md §16`, and `context/decisions/phase-3-cross-module-decisions.md`. The 3-type chain (QueueSaturationHealthCheck + HealthSignal + HealthLevel) is now formally on record as the minimum viable promotion.
