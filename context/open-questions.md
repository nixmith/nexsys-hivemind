<!--
file: context/open-questions.md
purpose: Inter-agent register of open questions and verify-needed items. PM consults before issuing instructions; Coder consults before executing.
audience: PM, Coder
update-cadence: per-WU
state-type: comms
status: CURRENT
last-verified: 2026-05-21 against `homesynapse-core` commit `dfb045e`
-->

# Open Questions Register

Inter-agent typed-message surface for `[OPEN-QUESTION]` and `[VERIFY-NEEDED]`. See `coder/CLAUDE.md §Message Protocol` and `project-manager/CLAUDE.md §Message Protocol` for the routing rules, and `REORGANIZATION_PLAN_2026-05-20.md §5b` for the entry template.

- **Active** items live above the `---` separator and must be resolved (or explicitly carried forward) before any WU they `Blocking:` can close.
- **Resolved** items move below the separator for one milestone, then archive on the same cadence as the handoffs.
- Numbering follows `OQ-MM-NN` per PLAN §5c. The current series (`OQ-05-*`) restarts numbering for the 2026-05 milestone and back-references prior `OR-M3-NN` entries in `pm-handoff.md` via the `Context:` field.

## Active

## [OPEN-QUESTION] OQ-05-02 — `StateCheckpointSource` extension to thread reconciliation metadata
**Posed by:** Coder (M3.6d-a closeout)
**Posed:** 2026-05-20
**Blocking:** none directly; blocks AMD-41 §3.2.4 completion (5th `ReconciliationTest` method `reconciliationRecordsMetadataInDataSlot`). Likely M4 scope.
**Question:** Should `StateCheckpointSource` be extended to thread reconciliation metadata (`reconciledAt`, `reconciledFromVersion`, `reconciledToVersion`) through the projection's checkpoint contract, and if so, which milestone owns the work?
**Context:** AMD-41 §3.2.4 requires that the reconciliation path record metadata in the data slot. `StateProjection.writeCheckpoint(Instant)` currently passes only plain `projectionVersion` to `StateCheckpointSource.serializeCheckpoint(int)`; `SqliteStateStore.serializeCheckpoint(int)` forwards `null` for the three metadata fields. M3.6d-a's `ReconciliationTest` ships 4 of 5 brief tests — the 5th was deferred because it would fail trivially against the current contract. Implementing the feature requires extending the `StateCheckpointSource` interface and threading the metadata through `StateProjection.initialize`'s reconciliation path. Cross-reference: `pm-handoff.md` OR-M3-13.
**Resolution:** _(open)_

---

## [OPEN-QUESTION] OQ-05-03 — M3.6d-b prerequisite infrastructure: bundle into the brief or split into its own WU?
**Posed by:** Coder (mid-M3.6d execution)
**Posed:** 2026-05-20
**Blocking:** M3.6d-b (PersistenceFactory + HomeSynapseCore composition-root wiring).
**Question:** Are the three M3.6d-b prerequisite gaps (SqlitePersistenceLifecycle constructing SqliteStateStore + SqliteDeadLetterStore, `WriteCoordinator.queueSize()` exposure, production `SubscriberReadConnectionFactory`) bundled into the revised M3.6d-b coding instruction, or split into a separate prerequisite WU before M3.6d-b begins?
**Context:** The original M3.6d brief assumed all three existed; they do not. (1) `SqlitePersistenceLifecycle` constructs only the four main stores today (EventStore, EventBusCheckpointStore, ViewCheckpointStore, WriteCoordinator) — must also construct `SqliteStateStore` + `SqliteDeadLetterStore`. (2) `WriteCoordinator` interface needs `queueSize()` exposure for the bus's writer-queue-depth `IntSupplier` (DEC-M3-14). (3) Today only the testFixtures `RecordingReadConnectionFactory` exists; M3.6d-b needs a production `SubscriberReadConnectionFactory`. Estimated work-unit-size impact: bundling grows M3.6d-b from 6–8h to 10–12h. Cross-reference: `pm-handoff.md` OR-M3-14. *Note: as of 2026-05-21 the source repo is at `dfb045e` (M3.6d-b 4/4 shipped), so this question has been answered by execution; the hivemind catches up to that state in a future WUCP Phase 2 — not in this batch.*
**Resolution:** _(open)_

---

## Resolved (this milestone)

## [OPEN-QUESTION] OQ-05-01 — DEC-M3-16 addendum to record the transitive 3-type promotion chain
**Posed by:** PM (M3.6d-a closeout)
**Posed:** 2026-05-20
**Blocking:** M3.6d-a closeout (governance hygiene).
**Question:** Does DEC-M3-16's authorization cover only the named class (`QueueSaturationHealthCheck`) or also the types its public constructor transitively leaks (`HealthSignal`, `HealthLevel`)? If transitive, do we need a new DEC entry recording the chain?
**Context:** `QueueSaturationHealthCheck`'s public constructor accepts `Consumer<HealthSignal>`, and `HealthSignal` has a `HealthLevel` enum field. `-Xlint:exports` requires all three types to be public simultaneously — the chain is the minimum viable visibility unit. The promotion shipped with M3.6d-a `25bc23b`, but DEC-M3-16 (authored before the chain was understood) named only `InProcessEventBus` and `SqlitePersistenceLifecycle`. Cross-reference: `pm-handoff.md` OR-M3-12.
**Resolution:** RESOLVED 2026-05-20. New entry DEC-M3-17 ("HealthSignal + HealthLevel public visibility — DEC-M3-16 addendum") appended to `project-knowledge/HomeSynapse_Current_State.md §3`, `project-knowledge/HomeSynapse_Core_Locked_Decisions.md §16`, and `context/decisions/phase-3-cross-module-decisions.md`. The 3-type chain (QueueSaturationHealthCheck + HealthSignal + HealthLevel) is now formally on record as the minimum viable promotion.
