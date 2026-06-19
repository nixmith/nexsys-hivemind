<!--
file: context/handoff/2026-06-18_automation-superiority_Phase1-design_session_prompt.md
purpose: Dispatch-ready session brief — a PHASE-1 (Architect-mode) design session to design the DIFFERENTIATING automation layer (the superiority vectors) BEFORE M7.2/M7.3 implement the baseline engine, so the implementation targets the differentiator rather than a baseline it will outgrow. Output: a scoping memo + (on Nick's scope ruling) a new Locked design doc draft (Doc 16 candidate).
audience: PM/Architect (a FRESH Cowork conversation, nexsys-project-manager skill, Mode 1 Architect), Nick (rules the Phase-1 scope + the eventual Lock)
state-type: session prompt (planning → design)
status: SCOPE RULED 2026-06-18 — DISPATCH-READY. Nick ruled the Phase-1 scope at the app-bootstrap-decisions session (decision record `context/decisions/2026-06-18_app-bootstrap-and-superiority-scope_decisions.md`, Part B). The scope decision package is NO LONGER this session's job — it is settled (see "RULED SCOPE" below). This session now enters Mode-1 Architect and authors the Doc 16 draft to that ruled scope. Run as a fresh Cowork conversation (a Locked design doc deserves an unloaded session).
baseline: core 03f16dc (substantive 1eddd9a) / docs f2e064d / hivemind b7a893e; M6 COMPLETE; M7 contracts ratified (AMD-88..93); M7.1 ISSUED-awaiting-build.
anchors: context/planning/2026-06-14_automation-engine-superiority_research-vector_proposal.md (the 10 vectors + lock points + sequencing) · context/planning/2026-06-12_M7-M8-charter-skeleton.md (M7/M8 pieces) · homesynapse-core-docs/design/Doc 07 (Automation Engine, Locked) · Doc 14 (Master Architecture) · the strategy layer (context/strategy/; catalog in strategic-context-map.md §2)
-->

# Session Brief — Superior-Automation Phase-1 Design (the differentiator, ahead of the build)

PM/Architect session (**nexsys-project-manager skill, Mode 1 — Architect**). Read `context/process/cowork-environment-model.md` FIRST, then run the freshness preflight. This session designs the automation layer that is the product's selling point — **as design, not code, and ahead of M7.2/M7.3** — so the eventual implementation builds toward the differentiator instead of toward Doc 07's baseline.

## RULED SCOPE (2026-06-18, Nick — build exactly this; the scope is settled, do NOT re-litigate)

Author **Doc 16** as a Locked design doc with **three first-class sections** + two seams + the M7-impact section:

1. **Expressiveness-without-a-DSL** — reusable/parameterized automation components, computed conditions, typed parameters; static-analyzable; **no templating DSL** (hard anti-requirement). This is the core "design-before-M7.2" surface — it shapes the M7.2 action model.
2. **Explainability / causal-chain as a first-class product surface** — AMD-91 `RunCausalChain` elevated to "why did this fire?" for a non-expert; an enterprise audit surface too. (Not too thin — this is half the home-user differentiator.)
3. **Run-coupled reliability** — honest degradation of a *running* automation + deterministic/safe behavior under failure. **Only the run-coupled half of "reliability" lives here** (it touches the M7.2 run model). The cross-cutting half is a separate doc (below).
- **Federation-readiness seam (identity/scoping non-preclusion ONLY)** — design single-site automation/entity/event identity so a future federation layer never forces an immutable-event-log migration. Do **not** design federation here.
- **Hybrid cut-line** — the local/remote boundary + the never-a-dependency invariant, **coordinated with the app-bootstrap charter** (pin the seam in the composition root). Do **not** design the full cloud-accelerator feature here.
- **§4 M7-contract-impact section (MANDATORY)** — a one-line verdict per M7.x. The ruled expectation to hold/verify: **M7.1 trigger/condition contracts UNAFFECTED** (so M7.1's ride-along build is cleared) · **M7.2 SHAPED, builds into this doc** (do not freeze its action contract first) · **M7.3 UNAFFECTED** (D2/REC-162 stays the separately-escalated M7.2 question). Any contract change → formal AMD/supersession, never a silent reshape.

**Split out — NOT in Doc 16 (each its own doc; numbering pinned at authoring):**
- **Cross-cutting reliability-as-a-product-property** (multi-year longevity, observability-as-product, system-wide self-healing) — own **co-equal** doc, sequenced **right after** Doc 16; not M7-gating.
- **B3 multi-site / enterprise federation** — own **post-M8** doc; implies new invariants (cross-site boundaries, federated identity, WAN-partition autonomy). Doc 16 reserves only the identity/scoping seam.
- **C1 honest-hybrid deployment** — own **tight** doc sequenced with app-bootstrap (local/remote boundary + never-a-dependency invariant only).

**Deferred to M7.2/M8 research briefs (do not design here):** A2 conflict-at-scale · B1 cost-curve · B2 concurrency/backpressure · D2 expected-state-vs-re-issue (REC-162) · E2 reachability asleep-vs-dead.

---

## Why now (the strategic frame — recorded at the 2026-06-18 converge)

A smart-home product wins or loses on its automation engine. The M7.x already chartered (M7.1 trigger/condition, M7.2 run/action/dispatch, M7.3 pending-command ledger) implements **Doc 07's baseline** — correct and necessary, but *table stakes*. The differentiation is a strategic layer on top, and if it is the selling point it must be **designed before M7.2/M7.3 freeze their contracts**, or those contracts get reshaped in arrears. Designing it now is the same Phase-1-before-Phase-3 discipline the whole project runs on. **M7.1 is deliberately held as a ride-along until this design confirms its trigger/condition contracts are unaffected** (see the interlock in §4).

## The candidate vectors (from the 2026-06-14 superiority proposal — READ IT FIRST)

The proposal enumerates 10 vectors, each mapped to a lock point + priority + sequencing. The strategically load-bearing clusters:

- **B3 — Multi-site / enterprise federation.** Automations + state spanning multiple homes/sites (the Assure/Care institutional positioning; the "enterprise" smart-home segment). Likely the single biggest differentiator AND the biggest design — almost certainly its own Locked doc and new invariants (cross-site event/state boundaries, identity, trust).
- **C1 — Honest-hybrid deployment.** Local-first with an *honest* cloud-optional story (no hidden cloud dependency; the trust brand). Touches the composition root + the WebSocket/REST boundary + Doc 12 lifecycle.
- **Expressiveness-without-a-DSL.** Richer automation expressiveness while honoring the hard anti-requirement **(no templating DSL)** — the design challenge is power without a Turing tarpit. Touches the trigger/condition/action model directly (so it has the tightest M7 interlock).
- **Correctness/trust + observability vectors.** Determinism, explainability ("why did this fire?"), the run-causal-chain (AMD-91) as a first-class product surface — these reinforce the existing trust positioning and the M5-C explainability copy.

## This session's job (strict order)

1. **Step-0:** preflight; reconcile HEADs; read the inputs (the vector proposal, Doc 07 + its MODULE_CONTEXT, the M7/M8 charter skeleton, Doc 14, the strategy layer for positioning/revenue framing, DESIGN_DOC_TEMPLATE.md, references/cross-subsystem-awareness.md + constraint-enforcement.md).
2. **Assemble the SCOPE DECISION PACKAGE for Nick (the Phase-1 scope is HIS call — a new Locked doc is strategically significant).** For each cluster: the differentiator thesis, the lock point, the design size (P1 sizing smell-test — federation and hybrid likely each exceed one doc), the cross-subsystem blast radius, and whether it implies new invariants. **Recommend a primary pick** (PM rec: lead with expressiveness-without-DSL if the goal is to harden M7 itself, or with federation/B3 if the goal is the enterprise differentiator — present the tradeoff, let Nick rule).
3. **On Nick's ruling:** enter Architect mode and draft the new design doc (**Doc 16 candidate**) per DESIGN_DOC_TEMPLATE — all 13 mandatory sections substantive, every cited INV/LTD addressed by a specific decision, open questions marked BLOCKING/NON-BLOCKING. If Nick splits the scope (e.g., federation as its own doc), produce the scoping memo + the first doc.
4. **Self-review** via references/review-and-quality.md before handing to Nick for the DOCS review → Lock.

## §4 — The M7 interlock (do NOT skip)

The deliverable MUST include an explicit **M7-contract-impact section**: for every design decision, state whether it reshapes any ratified M7 contract (AMD-88..93) or the M7.1 trigger/condition surface. Rules:
- If a vector needs a contract change, it moves through the **formal AMD/supersession pipeline** — never a silent reshape of a Locked/ratified contract.
- Produce a one-line verdict per M7.x piece: *does this design change M7.1 / M7.2 / M7.3 as currently scoped?* This verdict is what un-blocks (or re-sequences) the M7.1 ride-along build. If M7.1's trigger/condition contracts are unaffected, say so explicitly so M7.1 can build in parallel; if affected, name the AMD and the sequencing consequence.

## Anti-requirements (bind the design — non-negotiable)
No templating DSL (expressiveness must come another way) · no engine retry · no destructive forced migration · never lead with commodity encryption · local-first is inviolate (any cloud/hybrid element is honest and optional). These are the standing automation anti-requirements; the superiority design lives entirely inside them.

## Done-when
A scope decision package delivered to Nick AND — on his ruling — a Doc 16-candidate design-doc draft (or scoping memo + first doc if split), self-reviewed, with the §4 M7-impact section complete, ready for the DOCS review → Lock pipeline. Escalate to Nick: the Phase-1 scope itself; any new invariants the design implies; any M7-contract reshape it surfaces.
