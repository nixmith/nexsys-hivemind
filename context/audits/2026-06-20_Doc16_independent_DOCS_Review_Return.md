<!--
file: context/audits/2026-06-20_Doc16_independent_DOCS_Review_Return.md
purpose: INDEPENDENT, context-isolated, scope-independent DOCS-Project second-opinion review of homesynapse-core-docs/design/16-superior-automation.md (DRAFT 32afb3f) before Lock. Its distinct value over the prior (same-lineage) review is INDEPENDENCE ON SCOPE: it pressure-tests whether Doc 16's scope CUT is right, not only whether the doc executes it. Produces a scope verdict + a document verdict + a consolidated edit list + the §7.2 source cross-check re-run at core 60d50ce. Review ONLY — edits are NOT folded here (review-separate-from-fold; Nick folds → mints [SA-INV-*] + bumps the watermark at Lock → ratifies → Locks). Doc 16 Lock clears the M7.2b entry-gate.
audience: Nick (ratify/fold/Lock), the Doc 16 fold session
state-type: review return (independent design-doc review)
status: COMPLETE 2026-06-20 — SCOPE VERDICT: the cut is RIGHT (independently affirmed). DOCUMENT VERDICT: RATIFY-WITH-EDITS (7 edits, all NON-BLOCKING; no BLOCKING/REVISE finding). §7.2 cross-check RE-RUN at core 60d50ce → M7.1-UNAFFECTED holds.
reviewed: docs Doc 16 DRAFT 32afb3f (host-authoritative file tools; HEAD 4a41494 = AMD-94 on top, no Doc 16 fold landed — doc still at DRAFT state). Source cross-checks at core 60d50ce (M7.1 + AB-3), re-derived independently (prior review cross-checked at beb4bc3).
independence: run as a fresh, context-isolated conversation. Part B of 2026-06-18_app-bootstrap-and-superiority-scope_decisions.md (the scope rationale) was NOT read; the superiority research-vector proposal was NOT read; the prior session's planning narrative was NOT read. Scope was judged on the doc's own merits + the Locked dependency docs + the spine current-state only. Own view formed first, THEN reconciled against the prior review return.
-->

# Doc 16 (Superior Automation Layer) — INDEPENDENT DOCS-Project Review Return

This is the project's standard pre-Lock independent second opinion (the discipline Doc 15 passed before Locking), run as a **fresh, context-isolated, scope-independent** session. Its charge differs from the prior review (`2026-06-19_Doc16_DOCS_Review_Return.md`): that review — by its own caveat — was run by the lineage that **set** Doc 16's scope, so it could only validate that the doc *executes* its declared splits, not whether the **cut itself** is right. **This review pressure-tests the scope.** I formed my own view first and only then reconciled against the prior return.

---

## A. SCOPE VERDICT (the headline) — the cut is **RIGHT**

**Independently affirmed: the three-first-class-surfaces + two-non-preclusion-seams cut is the correct Phase-1 superiority boundary, and it rests on a sound discriminating criterion.** Three NON-BLOCKING scope-clarity refinements are noted (S1–S3); none changes the verdict.

### A.1 The discriminating criterion is principled (this is why the cut holds)
Doc 16's cut is not arbitrary — it follows a single, defensible rule: **a property belongs in this Phase-1 doc iff it shapes the unbuilt M7.2 run/action/dispatch contract; otherwise it is a separate, later doc.** This is the forward-shape-never-reshape discipline (SP4) applied to *scope* rather than to contracts. It is the right criterion, because anything that touches the run model must be designed before M7.2 freezes it (or it reshapes a frozen contract in arrears), while a system-wide property can be designed afterward without disturbing M7.2. Judged against this criterion:
- **Expressiveness-without-a-DSL (§3.2)** shapes M7.2 (computed-parameter resolution at run init) → correctly IN.
- **Explainability/causal-chain (§3.3)** is a read-projection that mints nothing but anchors what the run trace must carry → correctly IN.
- **Run-coupled reliability (§3.4)** is *defined as* the half of reliability that touches the Run model → correctly IN.
- **Cross-cutting reliability, full federation, full honest-hybrid** do not touch the M7.2 run contract → correctly OUT (their own docs).

### A.2 Is any Phase-1 superiority surface MISSING? — No, with one boundary to make explicit (S1)
I brainstormed the candidate superiority surfaces a reader could expect and tested each against the criterion:
- **Conflict / precedence resolution** (two automations contending for the same entity). Doc 16 keeps **load-time shadow/duplicate detection IN** (the `AutomationLinter`, §3.2/§8.1) and defers **runtime write-arbitration at scale (vector A2) OUT** to M8. This is a defensible line — load-time static analysis is the part that needs the analyzable substrate this doc builds; runtime arbitration genuinely rides a real engine at scale. **But the line is stated only parenthetically in §3.2.** A reader of a doc titled "Superior Automation" may reasonably expect conflict handling and not find it called out in §2.2 (does-not-own). → **S1 (scope-clarity edit).**
- **Dry-run / simulation ("what would this do before I deploy it?")** — a real competitor gap. Correctly *implicitly* deferred: it builds on the same statically-analyzable expanded model (§3.2) and the explanation surface (§3.3) is its post-hoc twin. Not a Phase-1 omission.
- **Scheduling / temporal expressiveness** — baseline Doc 07 trigger territory (AMD-25 `for_duration`, etc.), not superiority. Correctly absent.
- **Notification/alerting on automation health** — covered by §11 observability. Present.

**Conclusion:** no surface that belongs in a Phase-1 automation-superiority doc is missing. The only adjustment is to make the conflict-handling boundary explicit (S1), not to add a surface.

### A.3 Is anything INCLUDED that should be split out (the "epic-under-one-label" risk)? — No
Tested against the M4-retrospective P1 smell test (a unit that spawns >~3 sub-pieces is too big):
- **§3.2 expressiveness is the heaviest surface** — a component model + a typed-parameter model + a bounded computed-value sublanguage + a linter (6 new types, 3 interfaces). It is at the edge. It is *not* an epic-under-a-label because (a) it is one coherent capability (parameterized reuse), and (b) it is bounded hard enough to stay analyzable: no I/O, no recursion, no string templating, only bounded folds, plus config ceilings (`max_expansion_depth`, `max_expanded_definitions`, `max_fold_entities`). It is, however, **the area to watch for scope creep at M7.2 build time** — flagged for the implementing milestone, not a Doc-16 defect.
- **The enterprise audit projection is bundled into §3.3.** This is the seam to the entire institutional/enterprise product tier, so it is the natural place to ask "is this smuggling an epic?" It is contained correctly: it is a **read-only projection over the same log** bound to Doc 15's `chain_hash`, default-OFF (SP6), "a licensing + API tier over the identical runtime, never a separate audit pipeline." The full institutional API (attestation, dispatch verification, RPM summaries) is correctly deferred. **Caveat:** the pre-chain enterprise-audit claim is currently over-stated (the prior review's E2; `chain_hash` is all-zero today) — so the containment is sound **conditional on E2 being folded.**

### A.4 Are the two seams genuinely non-precluding, or do they smuggle a design decision? — Seam B clean; Seam A clean-with-a-caveat (S2)
- **Seam B — the hybrid cut-line (§3.6): genuinely non-precluding, smuggles nothing.** It is an *application* of an existing constitutional invariant (INV-LF-01/02), not a new design: "all automation decisioning is local; any remote accelerator is an optional, failure-isolated outbound port the engine does not depend on for correctness." The one concrete commitment — the composition root wires only-local dependencies — is structural enforcement of INV-LF-02's three-level model (verified against INV-LF-02's body), coordinated with app-bootstrap. The doc correctly states the cut-line invariant "is owned in full by the honest-hybrid doc; this layer states it so the engine is not foreclosed." Clean.
- **Seam A — the federation identity/scoping seam (§3.5): legitimate, but it makes one persisted-shape-adjacent commitment that should be named as a formal-AMD-on-materialization.** The seam reserves (a) globally-unique-by-construction identity (already true — ULIDs/LTD-04, no new commitment) and (b) an additive, optional `ScopeRef` discriminator defaulting to "this site," **at the envelope/metadata level**. Reserving scope at the envelope level is the *minimal non-precluding* choice (putting it in the domain payload would force the exact log migration the seam exists to prevent), so it is appropriately Doc 16's call. **However:** "reserve an envelope-level field" is an envelope-shape-adjacent claim that intersects Doc 01's envelope and the in-flight AMD-94 1-byte-envelope-version work. The doc marks `ScopeRef` "(new, reserved seam) … Design-only; not populated at MVP," so nothing persists at MVP — but the doc should state explicitly that **actually materializing `ScopeRef` later is itself a formal AMD (an envelope-shape change through the pipeline), even though it is designed to be additive**, and that its envelope-level reservation must be confirmed compatible with the AMD-94 envelope-version slot it claims to "mirror." → **S2 (scope-clarity edit).** This does not make the seam wrong; it keeps the non-preclusion honest.

### A.5 Is the §7.2 M7-coupling boundary correct? — Yes (independently source-verified at 60d50ce; see §D)
The verdict M7.1 UNAFFECTED / M7.2 SHAPED / M7.3 UNAFFECTED is correct and is confirmed against landed source at the post-AB-3 HEAD. The three M7.2 beats (computed-param resolution at run init; component attribution via `definitionHash`→`ComponentRef`; the run-coupled reliability contract) are genuinely run-model-level and add no permit and no event. The honestly-stated contingency (a future computed-condition needing a *new* `ConditionDefinition` permit = an AMD-89-class change that re-sequences M7.1) is carried as NON-BLOCKING OQ1, not done silently. Boundary correct.

### A.6 Scope bottom line
The cut is right. It avoids the epic-under-one-label failure, draws the run-coupled / cross-cutting reliability line in the right place (on the M7.2-coupling criterion), and the seams are genuinely non-precluding. The prior review affirmed the doc *executes* its splits; this review independently affirms the **splits themselves are the right ones** — with three NON-BLOCKING clarifications (S1 conflict boundary; S2 ScopeRef-materialization-is-a-formal-AMD; S3 = E2, audit containment conditional on the tamper-evidence honesty caveat).

---

## B. DOCUMENT VERDICT — **RATIFY-WITH-EDITS** (7 edits, all NON-BLOCKING)

No BLOCKING and no REVISE finding (review-and-quality §5: the doc does not misunderstand its subsystem, does not violate an unpatchable invariant, introduces no dependency-direction violation, and silently changes no Locked contract). Doc 16 is fundamentally sound, template-complete, source-accurate on its M7 interlock, and Lock-ready after the fold. My edit list is larger than the prior review's three because the independent invariant scan and the Glossary/terminology check surfaced additional items — but every one folds cleanly and none gates the Lock.

### Full design-doc review (review-and-quality.md §1)
- **Template compliance — PASS.** All 14 MANDATORY sections (0,1,2,3,5,6,7,8,9,10,11,13,15,16) present and substantive; both relevant CONDITIONAL sections included with their conditions met (§4 Data Model — defines new types; §12 Security — trust boundary + external read surface); §14 (optional) included. Metadata complete; dependencies cite specific sections; dependents populated. Quality-checklist sub-items: every §1 principle (SP1–SP6) is referenced by a §16 decision (verified); one minor gap — `AutomationLinter` (§8.1) is not tied to a §7.1 interaction row (→ E7).
- **Invariant coverage — PASS-WITH-EDITS (E4).** Every invariant Doc 16 cites **exists with the stated meaning** (independently verified all 21 base INVs + the AMD-88/90/91/92/93 invariants against the §17 index). The independent §17 scan found **relevant-but-uncited** invariants (→ E4): most importantly **INV-PD-08** (Tamper-Evident System Integrity) and **INV-ES-01** (Events Are Immutable Facts) — the exact two invariants that **Doc 15, the dependency Doc 16 consumes for `chain_hash`, cites** for its tamper-evidence; plus the household-operability family (**INV-HO-04 / INV-HO-02**) the non-expert explanation + honest-degradation surfaces serve (Doc 07 itself maps contract C8→INV-HO-04, and Doc 16 inherits C8); plus **INV-CS-01 / INV-CS-06** for the versioned-component surface.
- **Locked-decision compliance — PASS.** LTD-01/04/08/09/11/15/17 cited and honored; no decision contradicts a Locked doc. The INV-PR-02 gloss ("automation eval p99 < 100 ms") is **accurate** — that is a constitutional target stated verbatim in INV-PR-02's body; and §10's targets are correctly framed as operational budgets / investigation triggers (matching INV-PR-02's two-tier model). The INV-LF-02 "three-level enforcement / no outbound network capability" citation (§3.6) matches INV-LF-02's body exactly.
- **Precision — PASS.** Behavioral claims are test-backed (C-SA-1..7 each map to a §13 test); §10 targets are quantitative with Pi-4 context; §9 config options have types/defaults/ranges; §6 failure modes give trigger/impact/recovery/events.
- **Consistency — PASS-WITH-EDITS (E5, E6).** All nine diagnostic/lifecycle event types §3.3/§6 read (`automation_triggered`, `automation_completed`, `automation_run_skipped`, `cascade_loop_detected`, `cascade_depth_exceeded`, `automation_condition_evaluated`, `automation_action_completed`, `automation_disabled`, `config_error`) **exist in the ratified corpus** (AMD-25/70/91/92) — confirming "mints no new event types." Forbidden-synonym check clean (no `EventRepository`/`handler`/`device_identifier`). **Two consistency findings:** the central new noun **"Component"** collides with a Glossary term the project explicitly avoids (→ E5); and §6.5 conflates contract C7 (original *definition*) with AMD-03 (original *snapshot*) (→ E6).
- **Decision quality — PASS.** §16: every decision has a principle/constraint-grounded rationale and a section ref; alternatives realistic (templating-DSL rejected on the silent-failure corpus; expressiveness-only too thin); tradeoffs explicit.
- **Open-question discipline — PASS.** §15: 5 OQs, all NON-BLOCKING; Q2 (AX-7 component versioning) and Q5 (D2/REC-162) are correctly flagged as M7.2/user-authoring escalations, not Doc-16-Lock gates; "No BLOCKING question remains." Verified that the two escalations are genuinely not Lock gates.

---

## C. CONSOLIDATED EDIT LIST (the prior E1/E2/E3 validated/extended + the new edits)

> Disposition key: **AGREE** = prior edit confirmed as-is · **AGREE+EXTEND** = confirmed and broadened · **NEW** = surfaced by this independent review. All edits are **NON-BLOCKING**. "Resolve at Lock" items are ratification mechanics to apply in the fold commit, not Draft defects.

### E1 — `RunCausalChain` "Existing (AMD-91)" → ratified-but-built-at-M7.2a. **[AGREE — re-validated at 60d50ce]**
- The prior finding is correct and **still holds at the post-AB-3 HEAD** (the prior review verified it at `beb4bc3`; I re-derived it at `60d50ce`). Source evidence at `60d50ce`: `RunContext.java` still declares `int cascadeDepth`, and its own Javadoc states the `cascadeDepth(int)`→`causalChain(RunCausalChain)` reshape "is **M7.2 work** (AMD-91 §2.2/§8) and is intentionally **not yet** applied to this record"; no `RunCausalChain.java` exists in the source tree. Because the explainability/audit surfaces (§3.3) **read** `RunCausalChain`, they inherently sequence after M7.2a builds it.
- Edit (as the prior review framed it): in §4 (data-model table) and §8.2, change `RunCausalChain`'s "Existing (AMD-91)" → "**Ratified (AMD-91); the type is built at M7.2a (the `RunContext.cascadeDepth(int)` → `causalChain(RunCausalChain)` swap). The explainability/audit surfaces that read it build with/after M7.2a.**"
- **Independent test of whether E1 should be broadened (it should not):** I checked the two adjacent "Existing" markers a reader might suspect of the same gap. Both **are** built in source at `60d50ce`, so Doc 16's "Existing" is accurate for them and E1 correctly isolates `RunCausalChain` as the *single* ratified-but-unbuilt type: (i) `RunStatus.INTERRUPTED` **is present** in `RunStatus.java` (7 values in source); (ii) `AutomationCompletedEvent.java` **exists** with `failureReason`/`abortReason`. One adjacent currency note for the fold session (not a Doc 16 defect): the canonical **Locked Doc 07 §8.2 table lists only 6 `RunStatus` values** while source carries 7 — Doc 07 §8.2 already self-flags this in a 2026-06-12 currency note, so when Doc 16 §3.4 lists `INTERRUPTED` as existing, it is source-true but ahead of the Doc 07 table; cite the §8.2 currency note.

### E2 — audit tamper-evidence is inert until `chain_hash` is live; state the dependency. **[AGREE+EXTEND]**
- The prior finding is correct: per AMD-37 / app-bootstrap A3-F4 (and Doc 16's own §6.3), `chain_hash` is **32-byte zero for every event today** and the chain-validity / mandatory-startup-verify machinery is gated on chain activation (post-MVP, ships with crypto-shred). So the audit projection's core value — tamper-evidence — is inert until then, and §3.3/§12 should say so (a clause cross-referencing §6.3 / A3-F4; `audit.enabled` already defaults off, so this is honesty, not a behavior change).
- **Extend:** pair the honesty caveat with the invariant fix in **E4** — the audit projection (C-SA-6) and the "log is the source of truth, no parallel trace store" property (SP2) should **cite INV-PD-08 (Tamper-Evident System Integrity) and INV-ES-01 (Events Are Immutable Facts)** in §5.2. These are precisely the invariants Doc 15 (the `chain_hash` owner) lists as governing, so consuming `chain_hash` without citing them is the coverage gap behind E2.

### E3 — register the candidate invariants `[SA-INV-1..4]` at Lock. **[AGREE — refine the minting]**
- Correct as ratification mechanics: per INV-GA-02, the canonical identifiers are assigned at ratification; the fold session must mint them in the §17 index + §18 traceability matrix in the **same commit** as the Lock and bump the watermark (AMD-93 → next).
- **Refinement (apply when minting):** confirm each candidate is **non-duplicative** of an existing invariant and register the genuinely-novel ones as first-class while relating (not duplicating) the derived ones:
  - `[SA-INV-1]` (expressiveness expands to the sealed model; no runtime template/expression/scripting engine) — **novel** (formalizes the no-DSL anti-requirement, AMD-88 §6/REC-155, as an invariant). Register.
  - `[SA-INV-4]` (federation non-preclusion: no site-local-sequential persisted identity; scope additive absent-defaults-to-local) — **novel** (no existing invariant covers scope-reservability). Register.
  - `[SA-INV-2]` (explanation is a pure projection of the log) — **overlaps INV-ES-06 + INV-ES-01 + INV-TO-03.** Register as a subsystem-specific strengthening ("no parallel trace store") *related to* those parents, or fold into the E4 citations rather than minting a near-duplicate.
  - `[SA-INV-3]` (running automations degrade deterministically) — **overlaps INV-RF-06 + INV-TO-02 + AMD-90-INV-01.** Same treatment: register as a composition that *cites* its parents.
  - Decide the identifier family: a new **`INV-SA-NN`** semantic category (the `[SA-INV-n]` provisional tags imply this) vs **`AMD-NN-INV`** amendment-scoped IDs tied to the Doc 16 Lock. Either is defensible; pick one and apply INV-GA-02.

### E4 — **[NEW]** Invariant coverage: cite the uncited-but-on-point invariants in §5.2.
The independent §17 scan (the review-and-quality §1 + constraint-enforcement §4 deliverable) found these relevant invariants that Doc 16 does not cite. Add each with a mechanism:
- **INV-PD-08 (Tamper-Evident System Integrity)** — governs the audit projection (C-SA-6, §3.3/§12). *Doc 15 cites it for `chain_hash`; Doc 16 consumes `chain_hash` and must cite it too.* **[the most on-point missing invariant]**
- **INV-ES-01 (Events Are Immutable Facts)** — the load-bearing substrate for SP2 ("derived from the log, not stored beside it"), the "no parallel trace store" property, and audit tamper-evidence. *Doc 15 cites it; Doc 16 should too.*
- **INV-HO-04 (Self-Explaining Errors)** + **INV-HO-02 (Operable Under Degradation)** — the non-expert "why did this fire?" surface (§3.3) and the honest-degradation contract (§3.4) are the household-operability value proposition, not only transparency mechanisms. *Doc 07 already maps contract C8→INV-HO-04, and Doc 16 inherits C8 (§3.4); citing INV-HO ties the surfaces to the invariants that justify them as superiority features.*
- **INV-CS-01 (Semantic Versioning Is Enforced)** + **INV-CS-06 (Deprecation Discipline)** — the `AutomationComponent` is "named, **versioned**," and OQ2/AX-7 is explicitly the component version/deprecation policy. Cite these where component versioning is discussed (§3.2/§9/§15-Q2).
- *(Optional, lower)* **INV-PR-04 (Architecture Must Accommodate 1,000 Devices)** — the deferred B1 cost-curve (10k entities / 1k automations) and the bounded-fold ceiling (`max_fold_entities`) are scale claims INV-PR-04 governs.

### E5 — **[NEW]** Terminology: the "Component" vocabulary collides with a Glossary term the project explicitly avoids. **[NON-BLOCKING; resolve at Lock — one-way door for public API/config]**
- The Glossary entry for **"Component"** states it was "renamed to 'Integration' by HA itself because 'component' was too generic. **HomeSynapse follows the renamed term.**" Doc 16's central new vocabulary — `AutomationComponent`, `ComponentRegistry`, `ComponentExpander`, `ComponentRef`, `ComponentParameter`, and the `automation.components.*` config keys — reuses exactly the term the project moved away from, in a *different* sense (a reusable automation fragment, ≈ HA blueprints / Node-RED subflows). This is the Glossary-enforcement "common violation" class (constraint-enforcement.md §Glossary), and it hardens into public API + YAML config (a one-way door).
- Edit (preferred, lighter): at the Lock fold, **add an `AutomationComponent` Glossary entry minting it as a distinct canonical term** with an explicit one-line disambiguation from the deprecated Integration-sense "Component," and add a single disambiguating sentence in §3.2. Alternative (heavier): rename — but avoid "template"/"blueprint," which collide with the no-DSL framing; candidates: `AutomationModule` / `DefinitionFragment`. Recommend the Glossary-addition path; the term is well-understood in the automation-reuse domain.

### E6 — **[NEW, minor]** §6.5 conflates contract C7 with AMD-03.
- §6.5 reads "in-progress component-expanded definitions complete on their **original snapshot** (C7)." Doc 07 **C7** governs the original *definition* in effect at trigger time; the original *state snapshot* is **AMD-03**. Edit: "complete on their **original definition** (C7); conditions evaluate against the captured AMD-03 snapshot." Trivial precision fix.

### E7 — **[NEW, minor/optional]** forward-shaped signatures + a §8↔§7 mapping gap.
- (i) `RunManager.initiateRun(...)` (§3.2/§7.2) is presented as a method, but Doc 07 §8.1 defines `RunManager` only at responsibility level (no method signatures — those are Phase-2/M7.2). Mark `initiateRun` as a **forward-shaped M7.2 method name**, consistent with the SHAPED framing, so it is not read as an existing Doc 07 signature. (ii) `AutomationLinter` (§8.1) is not referenced by any §7.1 interaction row (template quality-checklist item) — tie it to the Configuration (load-time) / REST (edit-time validation) row. Both LOW; fold opportunistically.

---

## D. §7.2 SOURCE CROSS-CHECK — RE-RUN at core `60d50ce` (M7.1 + AB-3) → **M7.1-UNAFFECTED HOLDS**

Re-derived independently at the post-AB-3 HEAD (the prior review cross-checked at `beb4bc3`; the brief requires re-confirmation at `60d50ce` because AB-3 landed in between). Every claim in Doc 16's §7.2 interlock is source-accurate:

| Check (Doc 16 §7.2 claim) | Source result at `60d50ce` | Verdict |
|---|---|---|
| No sealed `TriggerDefinition` permit added | `TriggerDefinition.java` sealed, **12 permits** (AMD-88 baseline: StateChange/State/Event/…); none added by Doc 16 | ✅ |
| No sealed `ConditionDefinition` permit added | `ConditionDefinition.java` sealed, **6 Tier-1 + 1 Tier-2 reserved**; none added | ✅ |
| No sealed `Selector` permit added | sealed `Selector`, **7 permits** (AMD-89: Area/Compound/DirectRef/Label/SemanticTag/Slug/Type); none added | ✅ |
| No sealed `ActionDefinition` permit added | `ActionDefinition.java` sealed, **5 Tier-1 + 3 Tier-2 reserved** (AMD-90 baseline); none added | ✅ |
| No AMD-92 event type added | `EventTypes.CORE_PRODUCTION_EVENT_CLASSES` = **32** (clean count); unchanged from M7.1 | ✅ |
| `ConditionEvaluator.evaluate(ConditionDefinition, StateSnapshot)` left unchanged | `ConditionEvaluator.java` line: `boolean evaluate(ConditionDefinition condition, StateSnapshot snapshot);` — **byte-identical to the M7.1-implemented contract** | ✅ |
| AB-3 wired the engine into the composition root but did NOT touch these contracts | `git diff --stat beb4bc3 60d50ce` over the event-model contracts + every sealed permit + `ConditionEvaluator`/`RunContext`/`RunStatus` = **empty**. AB-3's only `core/automation` change is **new** `AutomationEngineAssembly.java` (a wiring-only `final class`: `return new AutomationEngineSubscriber(evaluator)`) + a `module-info.java` adjustment | ✅ |
| E1 dependency reality | `RunContext` still `int cascadeDepth`; no `RunCausalChain.java`; the swap is source-documented as "M7.2 work, not yet applied" | ✅ (E1) |

**Result: no sealed trigger/condition/selector/action permit, and no AMD-92 event type, is introduced; the `ConditionEvaluator.evaluate(...)` contract M7.1 implemented is unchanged; AB-3 added only composition-root wiring. The M7.1-UNAFFECTED verdict holds and no AMD-89-class re-sequencing is hidden.** The M7.1 ride-along build remains cleared to proceed in parallel.

---

## E. ANTI-REQUIREMENTS — each verified *operationalized*, not merely asserted

| Anti-requirement | Operationalized by | Verdict |
|---|---|---|
| **No templating DSL** | Expansion-into-sealed-permits (SP1/§3.2) + computed values are bounded/total/side-effect-free with no string templating + the `AutomationLinter` + `max_expansion_depth`/`max_fold_entities` ceilings + `[SA-INV-1]` + §12 "no injection surface." | ✅ mechanism, not assertion |
| **No engine retry** (AMD-90-INV-01; D2/REC-162 must be **deferred**, not resolved/pre-empted) | SP3/§3.4 keep no-retry as the current contract; C-SA-5 test asserts "no re-dispatch"; D2/REC-162 is explicitly left to the M7.2 action-model decision in §3.4, §7.2, §14, and §15-Q5 — **neither resolved nor pre-empted** (matches the 2026-06-19 R2 ruling). | ✅ correctly deferred |
| **No destructive forced migration** | §6.1 fail-closed valid-subset loading (never partial expansion) + AMD-93-INV-01 forward-only/non-destructive + §16 row. | ✅ |
| **Never lead with commodity encryption** | §12: the audit/integrity story rests on the event-sourced tamper-evident log + Doc 15's established primitives, "not on a bespoke or headline encryption claim." | ✅ |
| **Local-first inviolate** | §3.6 cut-line + INV-LF-01/02 three-level enforcement (composition root wires only-local deps; core has no outbound network capability) + §12. | ✅ structural |

---

## F. Cross-checks performed (provenance)
- **Reads (independence-preserving):** environment model; PROJECT_SNAPSHOT (current-state only); Doc 16 in full; the Locked dependency docs (Doc 07 §3.4/§3.7/§3.7.1/§3.8/§3.10/§6.2/§8.1/§8.2/§11.2 + C1/C7/C8; Doc 01 §4.1; Doc 03 §3.5/§8.1 snapshot; Doc 06 schema fragment; Doc 12 composition root; Doc 15 §3 `chain_hash` + its invariant set; AMD-90/91/92/93); the Architecture Invariants §0.3 + §17 index (independently scanned for uncited invariants); the Glossary (≥14-term spot-check); the design-doc template (mandatory-section verification); review-and-quality §1; constraint-enforcement.
- **NOT read (independence rule honored):** Part B of `2026-06-18_app-bootstrap-and-superiority-scope_decisions.md` (the scope rationale); the superiority research-vector proposal; the prior session's planning narrative. Scope was judged on the doc + the Locked deps + the spine current-state. Own view formed first, then reconciled against the prior return.
- **Source cross-check:** core `60d50ce` (M7.1 + AB-3), with the `beb4bc3..60d50ce` diff to isolate AB-3's footprint. (Prior review cross-checked at `beb4bc3`; re-confirmed here at the post-AB-3 HEAD.)
- **Baseline confirmed at preflight:** docs HEAD `4a41494` (AMD-94 PROPOSED on top of `32afb3f` Doc 16 DRAFT — **no Doc 16 fold has landed; the doc is reviewed at its DRAFT state**); core `60d50ce` present (a trivial `.gitignore` commit `2174fcc` sits on top).

---

## G. Reconciliation with the prior review
| Item | Prior review (same-lineage) | This independent review |
|---|---|---|
| Scope | Affirmed the doc *executes* its splits cleanly ("epic-under-one-label avoided") — but, by its own caveat, could not question the cut | **Independently pressure-tested the cut → RIGHT**, on the M7.2-coupling criterion; added S1/S2 + the conditional-on-E2 containment |
| Document verdict | RATIFY-WITH-EDITS (3 edits) | RATIFY-WITH-EDITS (7 edits) — same disposition, larger edit list |
| E1 / E2 / E3 | Found | **All validated**; E1 re-confirmed at `60d50ce` and tested-for-broadening (correctly isolates `RunCausalChain`); E2 extended into E4; E3 minting refined |
| New | — | **E4** (uncited invariants INV-PD-08/ES-01/HO-04/HO-02/CS-01/CS-06), **E5** (Component vs Glossary), **E6/E7** (precision); **S1/S2** scope-clarity |
| §7.2 cross-check | at `beb4bc3` | **re-run at `60d50ce`** — holds |

---

## H. DONE-WHEN / hand-off to Nick
**Review only — edits are NOT folded here** (review-separate-from-fold). The path: Nick folds the consolidated edits (E1, E2/E4, E5, E6/E7 + the S1/S2 scope-clarity clauses) → mints `[SA-INV-1..4]` per E3 (de-duplicated, family chosen) and adds the E4 citations → bumps the watermark (AMD-93 → next) in the §17 index + §18 matrix in the Lock commit → ratifies → **Doc 16 Locks → the M7.2b entry-gate clears.** None of the edits gates the Lock; all are NON-BLOCKING clarifications/additions. The scope verdict (the cut is right) requires no doc change beyond the S1/S2 clauses.

### Suggested commit message (bang-free; use `git commit -F`)
```
docs(audit): add independent DOCS-Project review of Doc 16 (Superior Automation) - scope cut affirmed, RATIFY-WITH-EDITS

Fresh, context-isolated, scope-independent second opinion on
homesynapse-core-docs/design/16-superior-automation.md (DRAFT 32afb3f).
Distinct from the prior same-lineage review: pressure-tests whether the
scope CUT is right, not only whether the doc executes it.

SCOPE VERDICT: the three-surfaces + two-seams cut is RIGHT. Basis: the
run-model-coupling criterion (a property belongs here iff it shapes the
unbuilt M7.2 run/action/dispatch contract). No surface missing; nothing
is an epic-under-one-label; the run-coupled/cross-cutting reliability
line is well-placed; both seams are genuinely non-precluding. Three
NON-BLOCKING scope-clarity refinements (S1 conflict boundary, S2
ScopeRef-materialization-is-a-formal-AMD, S3=E2 audit containment).

DOCUMENT VERDICT: RATIFY-WITH-EDITS (7 edits, all NON-BLOCKING; no
BLOCKING/REVISE). E1/E2/E3 validated and extended; E4 (uncited
invariants INV-PD-08/ES-01/HO-04/HO-02/CS-01/CS-06), E5 (Component
terminology vs Glossary), E6/E7 (minor precision) added.

7.2 source cross-check RE-RUN at core 60d50ce (M7.1+AB-3):
M7.1-UNAFFECTED holds - no sealed permit added (Trigger 12 / Condition
6+1 / Selector 7 / Action 5+3), no AMD-92 event type added (inventory
32), ConditionEvaluator.evaluate(ConditionDefinition, StateSnapshot)
byte-identical, AB-3 added only composition-root wiring
(AutomationEngineAssembly + module-info). E1 re-validated: RunContext
still int cascadeDepth, no RunCausalChain.java.

Review only - edits NOT folded (review-separate-from-fold). Nick folds
-> mints [SA-INV-*] de-duplicated + bumps watermark at Lock -> ratifies
-> Doc 16 Locks -> M7.2b entry-gate clears.
```
