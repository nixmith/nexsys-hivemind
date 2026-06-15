<!--
file: context/planning/2026-06-14_automation-engine-superiority_research-vector_proposal.md
purpose: PM research-vector proposal (Nick-requested 2026-06-14, Track-4) — the candidate research avenues to make the HomeSynapse automation engine FAR superior to Home Assistant / Apple Home / Google Home, top-tier across local-first, cloud-dependent, and hybrid deployments, and safely scalable to arbitrarily large/complex homes AND enterprise. This is a PROPOSAL the PM hands to Nick for approval/sequencing — not a decision and not a research brief itself. Candidate briefs registered here feed the research agenda.
audience: Nick (approves + sequences), PM, the M7.x design sessions, the Track-2 app-bootstrap charter session
state-type: planning / research-vector proposal
status: DRAFT 2026-06-14 — registered in research-agenda.md (Track-3/4 addendum). Dispatch sequencing: AFTER the M7.1/M7.2 design beats land, so each brief pressure-tests a real engine, not a blank sheet (the same discipline that made R-δ land — assess against shipped ground, not aspiration).
baseline: homesynapse-core HEAD 1eddd9a (M6 COMPLETE 4-of-4; M7.1 trigger/condition path ISSUED). Grounds: the R-δ competitive deep-dive + assessment (AX-1..AX-10); Doc 07 (Automation Engine, Locked + AMD-25); AMD-88/89/90/91/92/93; the merged-disposition M7/M8 charter; the M7.1 instruction (SD-1..SD-9).
-->

# Automation-Engine Superiority + Safe-Scaling — Research-Vector Proposal

## The goal, stated sharply

Three asks, one engine:
1. **Far superior** to Home Assistant, Apple Home, and Google Home — not "has more integrations," but *correct, debuggable, and trustworthy where they are fragile, opaque, and silent.*
2. **Top-tier across all three deployment models** — local-first (our brand), cloud-dependent (users who want remote/voice/cross-site), and hybrid — without the bricking risk that killed Revolv/Insteon/Wink and strands HA users.
3. **Safely scalable** from a one-bedroom flat to a sprawling estate to an enterprise (property managers, multi-site, MDU/hospitality) — *without* the engine degrading, racing, or becoming undebuggable as entity/automation count climbs.

The central tension to hold honestly: **our deepest moat is local-first determinism (event-sourced, on-box, no mandatory cloud) — and "cloud-dependent + hybrid + enterprise scale" pushes directly on that moat.** The winning posture is not "abandon local-first to scale" but "extend the local-first guarantees into cloud/hybrid/enterprise so the guarantee *survives* the scale." Every vector below is judged against: does it preserve "works during an internet outage, user owns the keys, every decision is explainable"?

## What we already have that is ahead of the field (bank these — don't re-research)

- **Deterministic cascade-cycle detection (AMD-91 `RunCausalChain`).** R-δ banked this: HA has NO loop detector (Issue #115042 froze HA on a `repeat` loop). We are ahead by construction.
- **Event-sourced replay/determinism.** The decision substrate is an immutable, hash-chained log → time-travel, dry-run, and "why" are *architecturally available*, not bolted on. Apple/Google/HA cannot answer "why did this fire?" — we can.
- **Sealed Trigger/Condition/Action model + no templating DSL.** R-δ banked both (Node-RED spaghetti; HA template silent-fail + maintainer refusal). Safety-by-construction.
- **Fail-closed-at-load (R-δ AX-5)** — now a first-class M7 loading contract (M7.1 SD-9). HA loads broken automations into a silently-dead state; we reject-and-surface.
- **Per-scope crypto + typed identity (name ≠ identity).** Rename-safety + privacy that the others lack.

These are the spine of the superiority claim. The research below is about *widening the lead* and *making it hold at scale and across deployment models.*

## The candidate research vectors

Grouped by the dimension of superiority. Each is a candidate brief: **goal · what we have · the gap · the research question · lock point · priority.**

### Group A — Correctness & "it never silently misbehaves" (the trust moat)

- **A1 · Automation static analysis & linting (load-time + edit-time).** *Have:* fail-closed-at-load (SD-9), schema validation. *Gap:* we reject *invalid* automations but don't yet *analyze* valid-but-dangerous ones. *Question:* what's the field-proven set of static checks — unreachable conditions, two automations fighting one entity (write-conflict), shadowed/duplicate triggers, missing-entity references, infinite-intent loops not caught by cycle detection — and which are computable at load on constrained hardware? *Lock point:* M7.x loading contract + the explainability surface. *Priority:* **HIGH** (pure differentiator; nobody does this well).
- **A2 · Automation interaction & conflict model at scale.** *Have:* AMD-91 cycle detection; AMD-31 sequential-within-Run ordering. *Gap:* cycle detection ≠ conflict detection. At 1k automations two can race on one entity with no cycle. *Question:* what is a deterministic, bounded conflict/precedence model (priority, last-writer, declared-owner, mutual-exclusion groups) that does NOT become a DSL and survives replay? *Lock point:* M8 (cascade governance / concurrency modes). *Priority:* **HIGH for enterprise scale.**
- **A3 · Dry-run / simulation / "what would this do?"** *Have:* event-sourced replay. *Gap:* no user-facing simulation. *Question:* can we offer "test this automation against last Tuesday's event stream" and "preview the next run" as a first-class feature (re-derive-never-re-execute, §3.10)? *Lock point:* M7.2 action-model + M10/M13 UI. *Priority:* **MED-HIGH** (a category-defining debugging feature; HA/Apple/Google have nothing).

### Group B — Scale to large/complex homes AND enterprise

- **B1 · Trigger-evaluation & state-snapshot cost curve.** *Have:* O(1) trigger index; single AMD-03 snapshot per Run. *Gap:* unmeasured at 10k entities / 1k automations / storm load on Pi-class AND on bigger enterprise hardware. *Question:* where does the eval path, snapshot capture, and cascade governance degrade; what indexing/pruning/partial-match keeps it bounded; what's the honest ceiling per hardware tier? *Lock point:* performance pins + M7.2 + the REC-157 storm-bench harness (already in M7.1 tests). *Priority:* **HIGH** (the credibility of every scale claim rests here).
- **B2 · Concurrency & backpressure at storm scale.** *Have:* virtual-thread-per-Run (LTD-01), per-subscriber checkpoints. *Gap:* VT scheduling fairness, backpressure, and cascade-storm governance under thousands of concurrent Runs. *Question:* the field-proven storm controls (HA modes single/restart/queued/parallel + `max`/`max_exceeded` — R-δ AX-5) mapped onto our sealed model + AMD-91; fair scheduling + bounded queues without unbounded memory. *Lock point:* M8 concurrency modes. *Priority:* **HIGH for enterprise.**
- **B3 · Multi-home / multi-site / federation — the enterprise architecture question (the big one).** *Have:* a local-first single-box engine. *Gap:* enterprise = property managers, MDU/hospitality, multi-site estates — many homes, central policy, per-site autonomy. *Question:* does a "hub-of-hubs" / federation model extend the architecture WITHOUT breaking local-first (each site still runs during a WAN outage; central is policy + observability, not a runtime dependency)? Event-log shipping / CRDT sync / hierarchical policy. This is the single largest unknown and the one no local-first competitor has solved. *Lock point:* a NEW post-M8 architecture design doc (Doc 16-class). *Priority:* **STRATEGIC — schedule deliberately; it may reshape the roadmap.**

### Group C — Deployment-model superiority (local-first / cloud / hybrid)

- **C1 · The honest hybrid model — "cloud as optional accelerator, never a dependency."** *Have:* no-mandatory-cloud brand (R-δ AX-9, validated by the graveyard). *Gap:* users legitimately want remote access, voice, cross-property, and heavy compute — served today by the very cloud-dependency that bricks competitors. *Question:* the design pattern where cloud is an *optional* edge (remote-access relay, voice bridge, cross-site sync, offload for compute-heavy ML automations) such that **every automation still runs locally during a WAN outage** and **no cloud service holds the keys.** Where exactly is the local/cloud cut line that preserves the guarantee? *Lock point:* the app-bootstrap charter + a hybrid-architecture design doc. *Priority:* **HIGH** (this is the literal answer to "top-tier for cloud-dependent or hybrid setups").
- **C2 · Conflict-free state sync for hybrid/remote.** *Have:* an immutable event log (a natural sync primitive). *Gap:* no defined sync/merge semantics for a home whose state is observed/edited from multiple places. *Question:* log-shipping vs CRDT vs single-writer-with-relay; offline-edit reconciliation; preserving causal order + the hash chain across a sync boundary. *Lock point:* C1's hybrid design doc + persistence. *Priority:* **MED-HIGH** (gates credible remote/multi-device).

### Group D — Expressive power WITHOUT a DSL (win the power-user without becoming HA/Node-RED)

- **D1 · Reusable automation components / "blueprints" the safe way.** *Have:* sealed, declarative model; no DSL. *Gap:* power users need reuse + parameterization (HA blueprints, Apple Shortcuts, Node-RED subflows) — the demand that historically forces a DSL. *Question:* how to deliver parameterized, shareable, composable automation components within a sealed declarative model — computed conditions, typed parameters, a component registry — without reintroducing a template language or losing static-analyzability (Group A). *Lock point:* M7.2/M8 + config schema. *Priority:* **MED-HIGH** (this is the frontier where we either win "powerful AND safe" or lose "too rigid").
- **D2 · Expected-state verification vs bounded re-issue (the REC-162 tension — already escalated).** *Have:* the `Expectation` model + AMD-90 confirmation. *Gap:* R-δ AX-5 surfaced strong field demand for HA's `retry` integration (`expected_state`/`retry_id`). *Question (already escalated to Nick as an M7.2 action-model decision):* is the demand satisfied by Expectation + confirmation, or does a *guarded* (expected-state-gated, idempotent) bounded re-issue belong in the sealed model? Do NOT flip REC-162 silently. *Lock point:* M7.2 action model. *Priority:* **MED** (decision-bearing; tied to D1).

### Group E — Observability superiority (the B3 "Ask your home why" differentiator)

- **E1 · Automation-debugging & causal-chain UX.** *Have:* event-sourced causal chains; the explainability strategy page. *Gap:* the actual debugging surface — "why did/didn't this run?", causal-chain visualization, per-run trace. *Question:* the best-in-class debugging-UX teardown applied to an event-sourced engine; what makes automation behavior *legible* to a non-expert (the WTH/porch-light pain corpus from R16/R-δ). *Lock point:* M12 observability + M10/M13 UI + strategy. *Priority:* **MED-HIGH** (named differentiator; partial overlap with the R16 output-conventions work already done).
- **E2 · Failure-state surfacing (reachability/Matter lesson, R-δ AX-8).** *Have:* `ReachabilityTrigger` (M7.1). *Gap:* `Availability` granularity (asleep-vs-dead). *Question:* the reachability/health vocabulary that distinguishes legitimate-asleep from dead to avoid false-alarm automations (already flagged as an M7.1 watch-out + M7/integration verify). *Lock point:* M7 + integration runtime. *Priority:* **MED** (folds into B1/E1).

## Sequencing recommendation (PM)

1. **Now → next (M7.1/M7.2 window):** none of these dispatch *before* M7.1/M7.2 design beats land — they must pressure-test a real engine. Hold A1, B1, D2/E2 as the *first* cluster to author once M7.2's action model is drafted (they sharpen M7.2/M8 directly and are cheap to ground).
2. **Mid (post-M8 scoping):** A2, B2, D1, E1 — the conflict/concurrency/expressiveness/observability cluster; these shape M8.
3. **Strategic (deliberate, possibly roadmap-reshaping):** **B3 (federation/enterprise)** and **C1 (honest hybrid)** are the two that most directly answer the "cloud/hybrid/enterprise" half of the ask and are the largest. Recommend each gets its own design-doc-grade research cycle, sequenced after the single-box engine (M7/M8) is real — authoring them too early risks designing for an engine that doesn't exist yet. C1 is also an input the app-bootstrap charter will eventually want.
4. **Discipline:** route each as a DOCS-Project brief on the existing two-lens, primary-sourced, quote-back-anchored pattern (the one that made R-δ land A−). Each declares its connector-blind gaps and spawns follow-ups. Anti-requirements bind all of them (no DSL, no mandatory cloud, no engine retry unless D2 reopens it, no destructive migration).

## What this intersects (carry, don't decide)

- **The retry-vs-REC-162 tension (D2)** and **the AX-7 versioning/deprecation-policy commitment** are already standing escalations to Nick — both are inputs to this superiority story and should be resolved as the action model (M7.2) and the user-authoring lock-in approach.
- **B3 (federation) and C1 (hybrid)** likely imply a NEW Locked design doc (Doc 16-class) — a Phase-1 architect-mode entry, which is Nick's scope call, not the PM's.
- This proposal is registered in `research-agenda.md` (Track-3/4 addendum). It is a menu for Nick to approve + sequence; nothing here is dispatched without his go.
