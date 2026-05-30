<!--
file: context/open-questions.md
purpose: Inter-agent register of open questions and verify-needed items. PM consults before issuing instructions; Coder consults before executing.
audience: PM, Coder
update-cadence: per-WU
state-type: comms
status: CURRENT
last-verified: 2026-05-30 against `homesynapse-core` commit `60b4185` (Research 10 ratification: OQ-05-06 → Resolved; OQ-05-08 [AMD-52 serializer beat] + OQ-05-09 [upcaster unit-threading] added. Prior: OQ-05-02/04 → Resolved).
-->

# Open Questions Register

Inter-agent typed-message surface for `[OPEN-QUESTION]` and `[VERIFY-NEEDED]`. See `coder/CLAUDE.md §Message Protocol` and `project-manager/CLAUDE.md §Message Protocol` for the routing rules, and `REORGANIZATION_PLAN_2026-05-20.md §5b` for the entry template.

- **Active** items live above the `---` separator and must be resolved (or explicitly carried forward) before any WU they `Blocking:` can close.
- **Resolved** items move below the separator for one milestone, then archive on the same cadence as the handoffs.
- Numbering follows `OQ-MM-NN` per PLAN §5c. The current series (`OQ-05-*`) restarts numbering for the 2026-05 milestone and back-references prior `OR-M3-NN` entries in `pm-handoff.md` via the `Context:` field.

## Active

## [OPEN-QUESTION] OQ-05-08 — AMD-52 typed `StateChangedEvent` payload — serializer/replay design beat (gates AMD-52 only, NOT AMD-51/M4.0b-3)
**Posed by:** PM (Research 10 ratification)
**Posed:** 2026-05-30
**Blocking:** authoring **AMD-52** (typed event payload). Does **NOT** block AMD-51 (the comparator ships with the String payload preserved) or the M4.0b-3 comparator coding instruction.
**Question:** Resolve the 5-item serializer/replay scoping checklist before authoring AMD-52: Jackson polymorphism for the sealed `AttributeValue`; replay determinism via the upcaster; event-store on-disk shape; consumer blast radius; `CheckpointSerializer`/`EnumTransition` interaction.
**Context:** REC-94 ratified "staged" — AMD-51 first (comparator, boolean verdict, String payload), AMD-52 second behind this beat. Full checklist in `context/assessments/2026-05-30_Research_10_PM_Assessment.md` §"AMD-52 design-beat scoping checklist." This is the single riskiest item in the M4.0b-3 track.
**Resolution:** _(open — its own design beat after AMD-51 ships)_

## [OPEN-QUESTION] OQ-05-09 — AMD-51 upcaster unit-threading for QUANTITY reconstruction
**Posed by:** PM (Research 10 ratification)
**Posed:** 2026-05-30
**Blocking:** AMD-51 authoring (narrow sub-question; not a milestone blocker).
**Question:** `AttributeValueUpcaster.upcast(AttributeType, String)` takes type but no unit; reconstructing a `QuantityValue` from a bare reported String needs a unit. Either (a) the reported String encodes the unit and the upcaster parses it, or (b) reconstruction threads `AttributeSchema.canonicalUnitSymbol` in (richer than the 2-arg upcaster). Settle against the integration contract — what do adapters put in `StateReportedEvent.value` for a QUANTITY attribute?
**Context:** Research 10 ratification §"upcaster unit-threading wrinkle." Does not change any of the four ratified calls. Cross-ref: `core/device-model` `AttributeValueUpcaster`/`AttributeSchema`/`QuantityValue`.
**Resolution:** _(open — AMD-51 author settles before coding)_

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

## [RESOLVED] OQ-05-06 — Typed attribute change-detection design (gated M4.0b-3)
**Resolved:** 2026-05-30 (Research 10 PM assessment + v2 ratification, `context/assessments/2026-05-30_Research_10_PM_Assessment.md`). REC-90..95 dispositioned (6 ACCEPT, all retargeted M4.0b-3); Nick's 4 strategic calls RATIFIED under delegation — defer deadband (REC-92); FP-noise total-form epsilon `|a−b| ≤ max(absEps, relEps·max(|a|,|b|))` + IEEE edge totality (REC-91); hand-roll units / skip Indriya — already satisfied by AMD-47's construction-time `QuantityValue` canonicalization (REC-93); stage AMD-51 (comparator, String payload preserved) before AMD-52 (typed payload) (REC-94). NQ-10-5 → external `AttributeValueComparator` in `core/state-store`; NQ-10-6 → normalization at reconstruction, not compare. **M4.0b-3 is design-unblocked; next forward action = author AMD-51.** Residual sub-questions split out as OQ-05-08 (AMD-52 serializer beat) + OQ-05-09 (upcaster unit-threading). (Posed by Cowork, M4 scoping, 2026-05-28.)

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
