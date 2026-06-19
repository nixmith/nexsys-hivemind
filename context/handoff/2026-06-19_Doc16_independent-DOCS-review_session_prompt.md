<!--
file: context/handoff/2026-06-19_Doc16_independent-DOCS-review_session_prompt.md
purpose: Dispatch-ready brief for a FRESH, CONTEXT-ISOLATED Cowork session that runs the INDEPENDENT DOCS-Project second-opinion review of Doc 16 (Superior Automation Layer) before Lock. Its distinct value over the prior review is INDEPENDENCE ON SCOPE — it must pressure-test whether Doc 16's scope is the right cut, which the prior (same-lineage) review could not. Produce a verdict + consolidated edit list. Review ONLY — do not fold. Doc 16 Lock clears the M7.2b entry-gate.
audience: a FRESH Cowork conversation acting as an independent DOCS reviewer (nexsys-project-manager skill, Mode-1 review discipline), Nick (ratify/fold/Lock)
state-type: session prompt (independent design-doc review)
status: READY — authored 2026-06-19. OFF the AB-3 critical path (Doc 16 Lock gates only M7.2b, which sits behind AB-3 → AB-1/2/4 → M7.2a), so this runs fully in parallel and delays nothing. Run as its OWN fresh conversation, SEPARATE from the AMD-94 session (see the independence rule below).
baseline: docs `32afb3f` (Doc 16 DRAFT — confirm; if Nick has pre-folded E1/E2 the SHA will differ, that is fine) / core `beb4bc3` (the landed M7.1 reality to cross-check §7.2 against). Confirm at a light preflight.
reads (in order):
  - context/process/cowork-environment-model.md (FIRST — the truncated-tail mount artifact; host file tools authoritative)
  - context/status/PROJECT_SNAPSHOT.md (current state ONLY — for grounding, not for scope rationale)
  - homesynapse-core-docs/design/16-superior-automation.md (THE DOCUMENT UNDER REVIEW — read in full)
  - the LOCKED dependency docs Doc 16 builds on, to check it composes correctly over them: design/07-automation-engine.md (§3.4/§3.7/§3.7.1/§3.8/§3.9/§3.10/§3.11/§3.12/§6/§8/§11.2), design/01-* (§4.1 CausalContext), design/03-* (§3.1 StateQuery), design/06-* (§3.2 SchemaRegistry/§3.3 reload/§7 paths), design/12-* (lifecycle/composition root), design/15-* (§3 chain_hash) + governance/Architecture_Invariants_v1.md (the §17 index — to independently scan for uncited invariants)
  - context/audits/2026-06-19_Doc16_DOCS_Review_Return.md (the PRIOR review return — E1/E2/E3 — as INPUT to validate/extend, NOT to rubber-stamp)
  - references/review-and-quality.md §1 (the design-doc review checklist) + references/constraint-enforcement.md
-->

# Session Brief — Independent DOCS-Project Review of Doc 16 (pressure-test the scope)

You are a **fresh, independent DOCS reviewer** for Doc 16 (Superior Automation Layer), the Phase-1 design doc that precedes M7.2/M7.3. This is the project's standard pre-Lock independent review (the same discipline Doc 15 passed before Locking). Read `context/process/cowork-environment-model.md` FIRST, then a light preflight (confirm the docs HEAD + that core is `beb4bc3` for the §7.2 cross-check).

## The independence rule (the reason this session exists — read carefully)
A prior review (`context/audits/2026-06-19_Doc16_DOCS_Review_Return.md`) already validated the doc's *execution* and found three edits (E1/E2/E3). But that review was run by the lineage that **set Doc 16's scope** (the 2026-06-18 Part-B superiority-scope ruling), so by construction it could not question whether the **scope itself** is right — only whether the doc executes it well. **Your distinct job is to pressure-test the scope.** Therefore:
- **DO NOT read the scope rationale.** Specifically, do **not** read Part B of `context/decisions/2026-06-18_app-bootstrap-and-superiority-scope_decisions.md` (the superiority-scope ruling), nor the superiority research-vector proposal, nor the prior session's planning narrative. Judge the scope on the doc's own merits + the Locked dependency docs + the spine. (If you must touch that decision record for any reason, stop and note it — it compromises this review's independence.)
- Form your **own** view first; only then reconcile against the prior review return.

## Your charge — four parts, scope first

1. **Pressure-test the scope (the headline).** Doc 16 claims three first-class surfaces — (a) expressiveness-without-a-DSL, (b) explainability/causal-chain, (c) run-coupled reliability — plus two non-preclusion seams (federation identity/scoping; the hybrid local/remote cut-line), with everything else (cross-cutting reliability, full federation, full hybrid) split into separate docs. Independently judge: **Is this the right cut?** Probe specifically: Is any surface that belongs in a Phase-1 automation-superiority doc *missing*? Is anything *included* that should have been split out (an epic-under-one-label risk)? Is the **run-coupled / cross-cutting reliability boundary** drawn in the right place? Are the two seams genuinely non-precluding, or do they smuggle in a design decision that should be its own doc? Is the §7.2 M7-coupling boundary (what shapes M7.2 vs what is M7.2's own) correct? State your independent verdict on scope with reasoning.

2. **Full design-doc review** per review-and-quality.md §1: template completeness (13+ mandatory sections substantive), invariant coverage (independently scan the §17 index for invariants Doc 16 should cite but doesn't), Locked-decision compliance, precision (testable claims, quantitative targets, config types/ranges, failure modes), consistency (terminology vs Glossary — spot-check ≥10; event types vs the AMD-92 taxonomy; cross-refs cite sections), decision quality, open-question discipline (BLOCKING/NON-BLOCKING).

3. **Validate/extend the prior edits.** For E1 (RunCausalChain "Existing (AMD-91)" → ratified-but-built-at-M7.2a), E2 (audit tamper-evidence inert until chain_hash live), E3 (mint [SA-INV-1..4] at Lock): agree / modify / reject each with reasoning, and add any edits the prior review missed.

4. **Cross-check §7.2 against landed source** at core `beb4bc3`: confirm Doc 16 adds no sealed `TriggerDefinition`/`Selector`/`ConditionDefinition` permit and no AMD-92 event type, and leaves the `ConditionEvaluator.evaluate(...)` contract M7.1 implemented unchanged — so the **M7.1-UNAFFECTED** verdict holds and no AMD-89-class re-sequencing is hidden.

## Anti-requirements to verify the doc holds
No templating DSL · no engine retry (AMD-90-INV-01; D2/REC-162 must be *deferred*, not resolved or pre-empted) · no destructive forced migration · never lead with commodity encryption · local-first inviolate. Confirm each is operationalized, not merely asserted.

## Done-when
An **independent review return** on disk (`context/audits/2026-06-DD_Doc16_independent_DOCS_Review_Return.md`) with: a **scope verdict** (is the cut right — your independent reasoning), a **document verdict** (RATIFY / RATIFY-WITH-EDITS / REVISE), a **consolidated edit list** (the prior E1/E2/E3 as validated/modified + anything new), and the §7.2 source cross-check result. **Do NOT fold edits into Doc 16** (review-separate-from-fold). Hand the return to Nick → he folds the consolidated edits → mints [SA-INV-*] + bumps the watermark at Lock → ratifies → **Doc 16 Locks → the M7.2b entry-gate clears.** Hand over a bang-free commit message for the review return.
