<!--
file: context/instructions/2026-06-27_D2-replay-invariant_registration-proposal_review-dispatch.md
purpose: The governance half of M7.4d -- a PROPOSAL to register D2 (pure-function-replay) as a canonical invariant in Architecture_Invariants_v1.md, routed through the normal review->ratify fold. The PM proposes; the PM does NOT self-mint the canonical id (the D2 record is explicit). Nick co-signs / dispatches the review; the register fold + the canonical number happen at ratification.
audience: Nick (co-sign / route to independent review); the DOCS reviewer; the v9 PM hub (folds at ratification)
status: RATIFIED + FOLDED 2026-07-01 (Nick co-signed at the v13 consolidated governance pass) — registered as **INV-ES-09** (§2, the PM-recommended ES category), **watermark-neutral** doc-currency fold per the decision-record's own authorization + the SA/AC precedent; invariant total 170→172 in the same pass (with AMD-97-INV-01); the AIOT-INV-1 "pending registration at M7.4b" citation fixed in both register locations; the candidate text folded WITH the review edit crediting both the bus FSM and the per-subscriber guard (this dispatch's own traceability table cites the subscriber-level unit test). PRIOR: PROPOSED -- awaiting Nick's review->ratify. Pairs with the M7.4d coding instruction (the CI test that enforces this invariant).
baseline: docs HEAD 75d0345 (watermark AMD-95; invariants 170/50; AC = §50). core db8ab5f at authoring -> now 9ec5949 (M7.4d COMMITTED `4e31aed`; the enforcing test `RunPipelineReplaySafetyTest` is LANDED + CI-green — so this proposal is fully ready to route, not pending its test). Authored by the v9 PM hub 2026-06-27; currency-confirmed route-ready by the v11 hub 2026-06-28.
-->

# D2 Pure-Function-Replay — Canonical Invariant Registration Proposal (review -> ratify)

## Why this exists

The §1 deeper-M7 architecture decision record (2026-06-25) RATIFIED **D2 (pure-function-replay)** as a first-class architecture invariant, but explicitly **deferred the canonical register entry to a governance fold**: *"The canonical invariant-register entry (an `INV-…` id in `Architecture_Invariants_v1.md`) is a governance mechanic … registered through the normal review->ratify fold … The PM does **not** mint the canonical id unilaterally."* This document is that proposal. Two facts make it due now:

1. **The enforcing test is landing.** M7.4d's coding instruction (`2026-06-27_M7.4d_d2-pure-function-replay-CI-gate_coding-instruction.md`) adds the composition-root seeded-log replay CI gate. An invariant backed by a green CI test but with no canonical register id is exactly the "claimed gate / unregistered contract" drift the truth-hierarchy warns about.
2. **`AIOT-INV-1` already cites D2 as a dangling reference.** The register (§50, `AC` category) records AIOT-INV-1 as "a citing composition of INV-SA-04 + AMD-90-INV-01 **(+ decision-record D2, pending registration at M7.4b)**." That parenthetical points at a decision record, not a canonical invariant — it should cite a real `INV-…` id once D2 is registered.

## The candidate invariant (verbatim text for review)

> **Pure-function replay.** Log replay is a pure function over the event log: replaying the persisted log to rebuild projections, ledgers, or any in-memory state MUST produce **zero external side-effects**. Device dispatch, adapter/network I/O, notifications, and any action observable outside the log run **only** on new-command handling in **LIVE** mode — **never** during `REPLAY`. A side-effect on replay re-fires real-world commands (the canonical, safety-critical event-sourcing failure). The property is realized structurally by the event bus's `REPLAY -> TRANSITION -> LIVE` mode FSM (a subscriber acts only in LIVE) and is **CI-pinned** by a composition-root seeded-log replay test that asserts zero dispatch/run/confirmation side-effects (M7.4d).

## What the reviewer must decide (the open governance points — PM does not self-rule these)

1. **Category + canonical id.** PM **recommendation: register under `ES` (Event Sourcing Guarantees, §2)** as the next `INV-ES-NN` — D2 is fundamentally an event-sourcing replay-purity guarantee. *Alternatives for the reviewer:* (a) an amendment-scoped id if the reviewer prefers an AMD vehicle; (b) a citing-composition note under `SA`/`AC` given D2's role in the AIoT safety frame. **The PM does not assign the number** — §17 Invariant Index assigns it at ratification. (Per INV-GA convention, ids are permanent + never reused.)
2. **Watermark treatment.** PM **recommendation: doc-currency registration, watermark-neutral** — the SA (§49, Doc 16 Lock) and AC (§50, Doc 17 Lock) precedent registered categories/invariants without an amendment-watermark bump. D2 was ratified in the §1 record (already co-signed), so this is a registration of an already-ratified decision, not a new amendment. *Reviewer may prefer a small AMD* (the D2 record allows either).
3. **AIOT-INV-1 reconciliation.** On ratification, update the §50 `AC` text: replace "(+ decision-record D2, pending registration at M7.4b)" with the new canonical id (e.g., "+ INV-ES-NN"). This is a same-commit currency edit, not a re-Lock of Doc 17.

## Traceability (for the reviewer + the fold)

| Element | Source | Enforcement |
|---|---|---|
| The rule | §1 decision record 2026-06-25, **D2** (RATIFIED, Nick co-signed) | — |
| Structural realization | D1 event-driven/co-located shape; the bus `REPLAY->TRANSITION->LIVE` FSM; subscriber-acts-only-in-LIVE | unit: `CommandDispatchSubscriberTest.onCommandIssued_inReplay_doesNotDispatch` |
| CI gate (integration) | M7.4d coding instruction | `RunPipelineReplaySafetyTest` (composition-root seeded-log replay -> zero side-effects), run by `./gradlew check` -> `ci.yml` |
| Empirical validation | V2-A spike (`spike/dispatch-latency-and-log-growth/` B1) | 1e6 replayed `command_issued` -> zero dispatch (tested template) |
| Cited-by | `AIOT-INV-1` (§50, `AC`) | currently cites "decision-record D2" -> update to the canonical id at ratification |

## The fold at ratification (what the PM executes once Nick rules — NOT now)

Per the §19/§20 register precedent (register here + §17 Invariant Index + §18 Traceability Matrix in the **same commit**, host-side, anti-clobber / git-object-sourced): add the candidate text under the ruled category with the ruled id; add the §17 row; add the §18 traceability row; update §0.3 if a new category prefix is introduced (not expected if `ES`); update the §50 `AC` AIOT-INV-1 citation; bump the invariant total **170 -> 171** (one new invariant) — re-derive from the §17 table, do not propagate; watermark per the reviewer's ruling (neutral on the doc-currency recommendation). Then mark this proposal RATIFIED and record it in the snapshot/pm-handoff.

## Recommendation summary (PM)

Register D2 as **`INV-ES-NN` (number assigned at ratification)**, **watermark-neutral doc-currency fold**, reconciling the AIOT-INV-1 citation in the same commit, with `RunPipelineReplaySafetyTest` (M7.4d) as the enforcing test. **Routing:** Nick co-signs or dispatches a lightweight DOCS review (the §1 record is already ratified, so this is a registration mechanic, not a new architectural decision) -> the PM folds at ratification. **Blocking:** non-blocking for the M7.4d *test* (the test can land + go green independently); blocking only for closing the "D2 canonical id registered" governance item + the AIOT-INV-1 citation cleanup.
