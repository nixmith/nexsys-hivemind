<!--
file: context/assessments/2026-06-26_aiot-safety-frame-and-ai-authoring_research.md
purpose: FORWARD research maturing the Doc 17 AIoT direction ("AI proposes, the deterministic engine disposes") from a reserved principle into a researched architecture. Surveys the 2026 state of safe-AI-in-the-home + LLM-agent-safety (planner -> verifier/safety-gate -> deterministic-executor); maps it onto HomeSynapse (AI-as-author over the sealed model + the load-time static checks as the verification layer; the composition-root proposer-only port for Doc 17 E3; the explanation projection for AI-as-reasoner); sets the AX-7 component-versioning gate; renders the moat-vs-table-stakes verdict + honest claim language; flags V1-non-preclusion seams. Builds on (verifies, does not just repeat) the 2026-06-23 prior-art study. It matures Doc 17 + the moat/claim; it changes NO V1 scope. Any seam V1 must not preclude is an ESCALATION to the hub, never a V1 change.
audience: the v6 PM hub (reconciles the v2 fan-out); Nick; the future AIoT-milestone author; the Doc 17 fold/Lock session.
state-type: assessment (forward research return)
status: RETURNED 2026-06-26 by SESSION V2-C (write-isolated research sub-session of the v2 parallel fan-out). Read-only on the spine; writes ONLY this file. Mints nothing; edits no design doc; runs no git.
sources-discipline: ANTI-FABRICATION ENFORCED. Every claim is tagged with a confidence tier -- (i) VERIFIED (primary source retrieved + linked), (ii) PATTERN-REAL (architectural pattern widely attested; NO single primary paper attributed), (iii) INFERENCE (own synthesis). The arXiv citations were independently re-verified by a verification pass (search + abstract-page fetch); one citation carried by the prior-art study (SafeGate) could NOT be retrieved and is flagged UNVERIFIED rather than repeated as authority. Sources table + tier-tagged link list at the end; only links actually opened are cited.
-->

# Doc 17 AIoT Safety-Frame + AI-Authoring -- Forward Research Return

This is the FORWARD research the v2 fan-out commissioned: take Doc 17 §3.3's reserved principle -- **"AI proposes, the deterministic engine disposes"** -- and turn it into a *researched* architecture, so a future AIoT milestone is built against verified ground and the "safest AIoT" claim is defensible rather than aspirational. It builds on the 2026-06-23 prior-art study (which found planner -> verifier -> deterministic-executor to be the emerging consensus) but **verifies rather than repeats**: the prior study's own PM assessment flagged its AI-safety arXiv citations as possibly fabricated and said "we use the pattern, not the papers." This pass re-checked them against primary sources -- most resolve; one does not, and is flagged.

---

## 0. Bottom-line synthesis

1. **The pattern is real and now multiply-attested in primary sources.** The "probabilistic planner -> deterministic verifier / pre-execution safety gate -> deterministic executor, with an audit trail" shape is documented across several *retrievable* 2025-26 arXiv papers (VeriMAP, Blueprint-First, VeriPlan, the f-secure information-flow design) and is codified as a security pattern (plan-then-execute) by OWASP's Agentic-AI work. HomeSynapse's frame is not a bet against the field -- it **is** the field's consensus, expressed in the system's existing architecture. (VERIFIED for the named papers below; PATTERN-REAL for the generic shape.)

2. **HomeSynapse's genuine differentiator is not "we have the safety pattern" -- it is the LOAD-TIME STATIC VERIFICATION LAYER that the sealed component model makes possible.** Because AI-as-author emits `AutomationComponent` instances that *expand into the sealed permits* (Doc 16 INV-SA-01) rather than into a DSL string, the `AutomationLinter` can statically reject a bad AI-authored automation -- unresolved refs, type mismatches, unreachable conditions, self-shadowed/duplicate triggers -- **before it ever runs**. Every surveyed safety architecture *verifies the plan*; HomeSynapse additionally **type-checks the authored artifact against a sealed schema at load**, which the planner/verifier papers do not have a substrate for. This is the defensible moat. (INFERENCE, grounded in VERIFIED Doc 16 mechanisms + the VERIFIED survey.)

3. **The Doc 17 E3 ask -- operationalize the frame STRUCTURALLY -- is correct and has a precise analog already in the codebase.** The structural enforcement is a composition-root **proposer-only port**: a future AI module is wired behind an inbound proposed-definition/proposed-command port with **no actuation capability and no outbound dispatch dependency** -- the exact analog of INV-LF-02's three-level "core has no outbound network capability" denial. This converts AIOT-INV-1 from an *asserted* principle into a *testable* invariant ("wire a mock AI module; assert it cannot reach `ActionExecutor`/dispatch except via a proposed definition the engine governs"). (INFERENCE, grounded in VERIFIED INV-LF-02 + the independent review's E3.)

4. **AX-7 (component versioning/deprecation -- Doc 16 OQ2) is the real gate before any AI-authoring milestone**, because an AI author is a *high-volume, low-stewardship* producer of versioned components: it will emit many components, share them, and re-emit variants, so the version/deprecation/compat policy that protects human-authored components from silent breakage is a *hard prerequisite*, not a nicety, once authorship is automated.

5. **Honest claim language:** defensible today = "an architecture in which **AI is structurally prevented from autonomously actuating** -- every AI-originated effect is a *proposal* that passes through a deterministic, statically-verified, no-autonomous-retry engine, and every AI decision is **explainable and auditable** as a pure projection of the immutable log." NOT defensible without hedging = any unqualified superlative ("the safest AIoT system," "AI can never misfire"), absolute-uniqueness claims, or safety claims about the *AI model's* outputs (we govern the *frame around* the model, not the model's correctness). The moat is the **frame and the static-verification layer**, stated precisely; the superlative needs counsel + the open patent/vendor search before it ships in marketing.

---

## 1. The surveyed safety-frame architecture (with explicit confidence tiers)

### 1.1 The consensus shape (PATTERN-REAL; multiply VERIFIED in instances)

Across the retrievable literature and practitioner sources, safe LLM-in-control systems converge on a three-stage decomposition:

```
   (probabilistic)        (deterministic)              (deterministic, least-privilege)
   LLM PLANNER  ───────▶  VERIFIER / SAFETY GATE  ───▶  EXECUTOR  ───▶  real-world effect
   proposes a plan        checks the plan against        carries out ONLY a
   or a structured        rules/contracts/a model;       verified, governed action;
   artifact               REJECTS unsafe plans           no autonomous re-planning
        │                        │                              │
        └────────────────────────┴──────────────────────────────┴───▶ AUDIT TRAIL (immutable record of plan, decision, outcome)
```

The **generic pattern** (plan-then-execute with a verification/gate stage and an audit trail) is **PATTERN-REAL: broadly attested across multiple independent sources; safe to assert as the field's direction.** The *specific instances* below are each VERIFIED against a primary source I opened.

### 1.2 The tiered evidence table

| # | Source / instance | Tier | What it actually says (one line) | What HomeSynapse takes from it |
|---|---|---|---|---|
| S1 | **VeriMAP** -- arXiv 2510.17109, "Verification-Aware Planning for Multi-Agent Systems" | **VERIFIED** | The planner "encodes planner-defined passing criteria as subtask **verification functions** (VFs) in Python and natural language." | The principle that a plan should ship *with* machine-checkable verification criteria -- HomeSynapse's analog is the sealed-permit schema the authored artifact must satisfy. (Note: spelled **VeriMAP**; VFs are *planner-defined*, not a separate post-hoc generator -- phrase accordingly.) |
| S2 | **Blueprint First, Model Second** -- arXiv 2508.02721 (Alibaba) | **VERIFIED** | An expert procedure is "codified into a source code-based Execution Blueprint... executed by a **deterministic engine**. The LLM is... never [used] to decide the workflow's path." A "Double-Check node acts as a safety gate." | The strongest external validation of "AI proposes, the deterministic engine disposes": the *path* is owned by a deterministic engine, not the model. Directly mirrors HomeSynapse's "expansion into sealed permits, engine governs execution." |
| S3 | **VeriPlan** -- arXiv 2502.17898 (CHI '25; cs.HC) | **VERIFIED** | "applies the probabilistic model checker **PRISM** to verify that an LLM-generated plan... satisfies a set of user-defined constraints." | Formal model-checking of an LLM plan against user constraints is real and shipped (as an HCI end-user tool). **Scope caution:** this is an *end-user planning* tool, NOT a generic LLM-safety framework -- cite it for "formal verification of LLM plans is feasible," not as a control-plane architecture. |
| S4 | **f-secure LLM system** -- arXiv 2409.19091 ("System-Level Defense against Indirect Prompt Injection... Information Flow Control") | **VERIFIED** | Coins "an **f-secure LLM system** [that] disaggregates the components... into a context-aware pipeline with dynamically generated structured executable plans, and a **security monitor** filters out untrusted input into the planning process." | The "security monitor on the planning input" idea -- relevant to a future AI-author's prompt-injection surface. **Corrections vs the prior study:** the paper says "context-aware pipeline" (not "rule-based executor"); the "SEPF" acronym was NOT confirmed in the abstract -- do not assert it. (Distinct from the F-Secure company.) |
| S5 | **SafeGate** -- claimed arXiv 2604.05427 (pre-execution safety gate + task safety contracts for LLM-controlled robots) | **UNVERIFIED -- DO NOT CITE THE ID** | The *concept* (pre-execution safety gating for LLM-robot commands) is real and attested by adjacent confirmed work; but no page naming this paper was retrievable, and the claimed ID 2604.05427 returned an anomalous empty body on every fetch. | Take the *concept* (a pre-execution gate with explicit safety contracts) as PATTERN-REAL; **do not** attribute it to this paper. The prior-art study (§2.10/§8) listed SafeGate as a FACT citation -- this pass downgrades it. (See Escalation H-2.) |
| S6 | **Plan-then-Execute as a security pattern** -- arXiv 2509.08646 ("Architecting Resilient LLM Agents... Secure Plan-then-Execute") + OWASP Agentic-AI work | **VERIFIED (pattern doc) + VERIFIED (OWASP)** | Decoupling planning from execution is framed as a *security* control (limits the blast radius of a compromised/hallucinated plan). | Validates the frame as a *security* posture, not just a correctness one -- the argument that the deterministic disposer is a containment boundary. |
| S7 | **HA Assist -- deterministic-first / LLM-fallback** -- home-assistant.io/voice_control + developers.home-assistant.io/docs/core/llm | **VERIFIED** | "Assist will handle commands first. Only questions or commands it can't understand will be sent to the AI" (the "prefer handling commands locally" option). Only intents/exposed entities are reachable by the LLM. | The closest *production* analog: the deterministic path handles known intents; the LLM is a fallback, and the LLM can only reach a curated, governed action surface (intents) -- a real-world proposer-only-ish boundary. Validates the two-tier shape ships today. |
| S8 | **OWASP -- LLM Top 10 + Top 10 for Agentic Applications / Agentic AI Threats** -- owasp.org + genai.owasp.org (Agentic released Dec 2025) | **VERIFIED** | Prompt injection (LLM01) and autonomous-agent risks (excessive agency, unsafe tool use) are codified industry threat taxonomies. | The threat model the AI-author seam must answer to: prompt injection into the author, and "excessive agency" -- both *structurally* answered by the proposer-only port (the AI cannot act, only propose) + human confirmation. |
| S9 | **NIST AI RMF 1.0** (NIST AI 100-1) + GenAI Profile (AI 600-1) -- nist.gov | **VERIFIED** | The recognized governance framework (Govern/Map/Measure/Manage) for AI risk. | The governance vocabulary to map the claim onto for enterprise buyers; the audit projection is the "Measure/Manage" evidence substrate. |

### 1.3 What is NOT in the literature (the gap = the moat) -- INFERENCE

Every surveyed system **verifies the plan** (against contracts, a model checker, verification functions, or information-flow rules). **None of them has a sealed, statically-analyzable authoring substrate that the authored artifact is type-checked against at load time before any execution path exists.** They verify *behavior* (will this plan violate a constraint?); HomeSynapse can additionally verify *form* (does this authored component even resolve, type-check, and compose against the sealed permits?) -- a cheaper, earlier, more total check, because the target is a sealed model, not free-form code or a DSL. That gap is HomeSynapse's defensible position (developed in §2). **(INFERENCE, grounded in the VERIFIED survey + VERIFIED Doc 16 INV-SA-01.)**

---

## 2. The HomeSynapse mapping

### 2.1 AI-as-author + the load-time static checks (the differentiator) -- INFERENCE on VERIFIED mechanisms

**The seam.** AI-as-author = natural language -> `AutomationComponent` instances that **expand into the existing sealed `TriggerDefinition`/`ConditionDefinition`/`ActionDefinition` permits** (Doc 16 §3.2 / INV-SA-01). The author emits the *analyzable target* (a sealed-permit composition), never a runtime DSL or template string. This is exactly the "generate a *structured* artifact, not free-form code" discipline the prior-art study's Decision 3 prescribed -- and it is already the V1 component model's shape.

**Why this is a verification layer no surveyed competitor has.** Doc 16 §3.2 + §8.1 already specify the `AutomationLinter` running, at load time and at REST edit time, over the *expanded* definition:
- **unresolved references** (an entity/selector/component the author hallucinated that does not exist),
- **type mismatches** (a parameter bound to the wrong `AttributeValue` kind),
- **unreachable conditions**, and
- **self-shadowed / duplicate triggers** (Doc 16 §3.2, the "vector A1" static checks).

For a *human* author these are quality-of-life. For an *AI* author they are a **verification gate**: the single largest failure mode of an LLM author -- emitting a plausible-but-invalid automation (a dangling entity ref, a wrong-typed value, a contradictory trigger) -- is caught **deterministically at load, before the automation can ever run**, and is *explainable* (the `config_error` carries the component name + reason + line, Doc 16 §6.1 / AMD-93). This maps the surveyed "verifier/safety-gate" stage onto a mechanism HomeSynapse **already has and competitors structurally cannot have** without a sealed model. The frame becomes: **AI proposes a component -> the linter statically verifies it against the sealed schema (reject-before-run) -> human confirms (pre-execution gate) -> the engine governs execution (no-autonomous-retry, pure-function-replay) -> the log + explanation projection make it auditable.** That is the planner -> verifier -> deterministic-executor consensus, with a *stronger* verifier stage.

**Honest scope of the static layer (INFERENCE).** The linter verifies *form and resolvability*, not *semantic intent* -- it cannot tell that "unlock the front door at 3am when motion is detected" is a bad *idea*; it can only tell that the automation is well-formed. Semantic-intent safety is what the **human-confirmation pre-execution gate** is for (and, later, optional policy constraints -- see Escalation H-4). The claim must not overstate the linter as semantic safety; it is *structural* verification. The combination (structural static check + human confirmation + deterministic governed execution + audit) is the defensible whole.

### 2.2 The structural proposer-only port for Doc 17 E3 -- INFERENCE on VERIFIED INV-LF-02

Doc 17 §3.3 currently *asserts* "no AI code path actuates a device or mutates state outside the engine." The independent review's **E3** correctly flags this as asserted-not-structural and names the fix: pin the *mechanism*, mirroring INV-LF-02's three-level enforcement. Here is the structural shape the future AIoT milestone should build (research output; **builds nothing in V1**):

**The analog.** INV-LF-02 ("Cloud Enhancement, Never Cloud Dependence") is enforced *structurally* by a composition-root denial: core subsystems are wired with **no outbound network capability** -- the capability is absent, not policy-checked, so "core makes an external call" is not a runtime guard that can be forgotten but a *type/wiring impossibility*. (VERIFIED: INV-LF-02's three-level no-outbound-capability enforcement is cited in Doc 16 §3.6 / §5.2 and resolved in the independent review §C.)

**The proposer-only port (the AI analog).** A future AI module is wired at the composition root as a **proposer-only adapter behind an inbound port** whose only outputs are a `ProposedDefinition` or a `ProposedCommand` -- design-only names; not built in V1. Structurally:
- the AI adapter has **no reference to `ActionExecutor`, `CommandDispatch`, or any actuation/dispatch collaborator** in its wiring (the capability is *absent*, exactly as core has no outbound-network capability);
- its *only* affordance is to submit a proposal *into* the engine through the inbound port;
- the engine then governs that proposal through the *unchanged* path -- expansion into sealed permits, the linter (§2.1), condition/mode/cascade governance, the no-autonomous-retry contract (INV-SA-04 / AMD-90-INV-01), and pure-function-replay (decision-record D2);
- every proposal, the verification result, the human decision, and the outcome are logged (auditable).

**The test that makes AIOT-INV-1 a real invariant (not a principle).** The analog of INV-LF-02's enforcement test: **wire a mock AI module at the composition root; assert it cannot reach `ActionExecutor`/dispatch except via a proposed definition the engine governs** -- i.e. assert the actuation capability is structurally absent from the AI adapter's surface, and that the *only* path from an AI proposal to a real-world command runs through the governed engine. This is the composition-root gate the independent review's E3 calls for, and it is what upgrades AIOT-INV-1 from "AI is never an autonomous actuator (asserted)" to "AI is never an autonomous actuator (structurally enforced + CI-tested)." **(INFERENCE; the V1 build precludes none of this -- see Escalation H-1.)**

### 2.3 The explanation projection for AI-as-reasoner -- VERIFIED mechanism

AI-as-reasoner consumes the **causal-chain / explanation projection** (Doc 16 §3.3 / INV-SA-03) to answer "why did/didn't this fire?", summarize, and diagnose. The load-bearing property (VERIFIED against Doc 16 §3.3 + INV-SA-03): **explanation is a *pure projection of the immutable log* -- there is no parallel trace store.** Consequences for the AI reasoner:
- it reads the **same substrate** as the dashboard and the auditor (`RunExplanation` / `NonFiringExplanation` / `RunCausalChain`) -- there is no AI-specific trace DB to build, populate, or trust;
- the "why did this *not* fire?" surface (Doc 16 §3.3, the higher-value half: `MODE_SUPPRESSED` / `CASCADE_LOOP` / `CONDITION_NOT_MET` / `DEFINITION_NOT_LOADED` / ...) is *durable* (a projection of the immutable log), unlike Home Assistant's ephemeral in-memory traces (default 5, evicted, never created when a trigger never matches -- VERIFIED in the prior study). An AI reasoner over HomeSynapse can answer absence questions that an AI reasoner over HA structurally cannot, because the substrate exists.

**This is why AIOT-INV-3 ("every AI decision is explainable and auditable as a pure projection of the log") is real but should stay a principle** (the independent review's verdict): the testable content is already carried by INV-SA-03's "no parallel trace store." The forward implication for the AIoT milestone: the AI reasoner/author must be *required to read the projection, never build its own decision store* -- which INV-SA-03 already reaches. **(VERIFIED mechanism; the "keep as principle" disposition is the independent review's, restated here as non-precluding.)**

---

## 3. The AX-7 component-versioning gate (the AI-authoring prerequisite)

**What AX-7 is (VERIFIED).** AX-7 = Doc 16 OQ2 (confirmed in the independent review §C as a real Doc 16 §15 NON-BLOCKING open question): the **version / deprecation / compatibility policy for the `AutomationComponent`** -- the named, *versioned* surface (Doc 16 §3.2/§4; governed by INV-CS-01 semantic-versioning + INV-CS-06 deprecation discipline, AMD-93-aligned forward-only/non-destructive).

**Why an AI author makes AX-7 a hard gate, not a nicety (INFERENCE).** A human author produces few components, slowly, and stewards them. An AI author is a *high-volume, low-stewardship* producer: it will emit many components, emit *variants* of the same intent, and (once shareable) seed a library others depend on. Without a versioning/deprecation/compat policy:
- an AI re-emitting a component under the same id can **silently break dependents** (the exact INV-CS-01/06 failure the policy exists to prevent), and
- a *shareable* AI-authored component with no version contract has no safe upgrade/deprecation path across the homes that imported it.

So the policy the AI-authoring seam needs, before shipping, is concretely:
1. **Identity + version on every authored component** -- `(componentId, version)` with enforced semantic versioning (INV-CS-01); an AI re-emission is a *new version*, never a silent in-place mutation.
2. **A deprecation/compat discipline** (INV-CS-06): a breaking change deprecates-then-supersedes; dependents are warned, never silently broken; forward-only/non-destructive (AMD-93) -- no destructive migration of an imported component, mirroring the immutable-log anti-requirement.
3. **Provenance on authored components** -- the originating author (which AI/model/version, or human) recorded, so a shareable component's lineage is auditable (this rides the same `definitionHash` -> `ComponentRef` attribution Doc 16 §3.2/§3.3 already specifies; INFERENCE that provenance should be first-class on the authored/shareable form).
4. **The shareable-component gate** -- AX-7 must be *set* before any component can be marked shareable or AI-authored-and-published; Doc 17 §3.2/§4 already names AX-7 as exactly this gate ("the gate before shareable/AI-authored components ship"). This research confirms the dependency direction: **AX-7 is a prerequisite of the AI-authoring milestone, sequenced before it, not concurrent.**

**Disposition:** AX-7 is a Doc 16 open question that becomes *load-bearing* the moment authorship is automated. It does not gate V1 (the component model exists; authoring UX + versioning policy are deferred -- Doc 17 §4). It **must** be tracked as the named prerequisite to any AI-authoring milestone (Doc 17 §7-Q4 already asks for this confirmation; this research answers: yes, confirm it).

---

## 4. Moat vs table-stakes + honest claim language

### 4.1 The verdict

| Capability | Verdict | Why |
|---|---|---|
| "We have an LLM / NL automation authoring" | **TABLE-STAKES** | HA Assist ships LLM authoring + a "Suggest" button today (VERIFIED). Having AI is not a differentiator. |
| Planner -> verifier -> deterministic-executor frame | **TABLE-STAKES (as a pattern)** | It is the *consensus* (VERIFIED instances S1-S7). Claiming the pattern as ours would be false; it is the field's. |
| Two-tier deterministic-first / LLM-fallback | **TABLE-STAKES** | HA Assist does this in production (S7, VERIFIED). |
| **AI-authored artifact STATICALLY type-checked against a sealed permit schema at load (reject-before-run)** | **MOAT** | Requires the sealed, no-DSL component model (INV-SA-01). Surveyed systems verify plan *behavior*; none type-checks the authored *form* against a sealed schema, because none has one. (INFERENCE on VERIFIED mechanisms.) |
| **Structural composition-root proposer-only enforcement** (capability-absent, not policy-checked) | **MOAT (architecturally)** | The INV-LF-02-analog structural denial -- "AI *cannot* actuate" as a wiring impossibility, not a guard -- is stronger than a policy/gate that can be misconfigured. (INFERENCE.) |
| **Durable "why did this NOT fire?" auditability of AI decisions** (pure projection of the immutable log, no parallel trace store) | **MOAT** | The prior study found *no mainstream platform* durably answers non-firing; HA's traces are ephemeral (VERIFIED). An AI reasoner inherits this substrate (INV-SA-03). |
| No-autonomous-retry + pure-function-replay under AI proposals | **MOAT (composed)** | INV-SA-04 / AMD-90-INV-01 + D2 mean an AI proposal cannot cause an autonomous re-fire and cannot re-fire on replay. (VERIFIED mechanisms; composition is the differentiator.) |
| SBOM / signed-update / vuln-disclosure | **TABLE-STAKES (regulatory)** | CRA/PSTI-driven; reserve, do not lead. |

**The moat in one sentence (INFERENCE):** not "we have AI," but **"HomeSynapse is the architecture where an AI author's output is *statically verified against a sealed schema before it can run*, the AI is *structurally incapable of actuating* (only of proposing), and every AI decision is *durably explainable and auditable as a projection of the immutable log* -- so an AI automation cannot silently be malformed, cannot autonomously misfire, and is never unexplained."**

### 4.2 Honest claim language (defensible vs needs-hedging)

**DEFENSIBLE (architecturally true, mechanism-backed):**
- "AI proposes; the deterministic engine disposes -- **structurally**: an AI module is wired as a proposer-only adapter with no actuation capability; the only path from an AI proposal to a real-world command runs through a deterministic, statically-verified, no-autonomous-retry engine." (Once E3's structural port + test exist.)
- "An AI-authored automation is **statically type-checked against a sealed permit schema and rejected before it can run** if it is malformed -- a verification layer the DSL/template-based competitors structurally cannot offer."
- "Every AI decision is **explainable and auditable** as a pure projection of the immutable log -- including *why an automation did not fire* -- with no parallel AI trace store to trust."
- "AI **can never autonomously retry or re-fire** a command, and no AI effect re-fires on log replay." (INV-SA-04 / AMD-90-INV-01 / D2.)

**NEEDS HEDGING / COUNSEL (do not ship unqualified):**
- **"The safest AIoT system" / "the safest, most reliable AIoT ecosystem"** -- a *superlative* and a *comparative* claim. Defensible *as an architectural posture* ("designed so that..."); NOT defensible as an unqualified market superlative without (a) the open patent/vendor-doc search (prior study Q1, still open) to substantiate uniqueness, and (b) marketing/legal counsel on comparative-advertising exposure. **Hedge to:** "architected to be among the safest -- AI is structurally a proposer, never an autonomous actuator." (FLAG: counsel + Q1.)
- **"AI can never misfire" / "AI can never cause harm"** -- overclaims. The frame prevents *autonomous actuation* and catches *malformed* automations; it does not make the *AI model's proposals semantically correct*, and a human can confirm a bad-but-well-formed proposal. **Hedge to:** "AI cannot *autonomously* actuate; every AI-originated effect is a proposal gated by deterministic verification and (for actuation) human confirmation."
- **"Formally verified AI automations"** -- do NOT claim formal verification (model-checking) unless/until it is actually built; the static linter is *type/resolvability* checking, not formal verification. VeriPlan (S3) shows model-checking is *feasible*, but HomeSynapse does not do it today. **Hedge to:** "statically verified against the sealed model" (true), not "formally verified" (not yet true).
- **Absolute-uniqueness** ("the only system that...") -- the prior study's "nobody durably does why-not" is *absence of evidence*, not proof. **Hedge to:** "to our knowledge, no mainstream platform durably answers..." until Q1 closes.

---

## ESCALATIONS TO THE HUB (V1 non-preclusion checks)

These are seams this research surfaced that V1 must NOT preclude. **They are flagged for the hub to check against V1 non-preclusion; this session acts on none of them and changes no V1 scope.**

- **H-1 -- The proposer-only port (E3) must remain wireable at the composition root.** The future AI-author/proposer enters as an inbound-port adapter with actuation capability *structurally absent* (the INV-LF-02 analog, §2.2). **V1 non-preclusion check:** V1's composition-root wiring and the inbound command/definition path must not bake in an assumption that *only the engine's own collaborators* can submit a definition/command in a way that would make adding a proposer-only inbound adapter a re-architecture. The existing `RunManager.initiateRun(...)` / `AutomationRegistry.load(...)` shapes (Doc 16 §7) appear to leave this open (a proposal becomes a governed definition/command the same way a human-authored one does) -- **hub: confirm V1 forecloses no part of the inbound proposed-definition/proposed-command seam.** (This is exactly the kind of structural seam the independent review's E3 wants pinned; pinning it is Doc 17/AIoT-milestone work, not a V1 change.)

- **H-2 -- The prior-art study carries an UNVERIFIED citation (SafeGate, claimed arXiv 2604.05427).** Not a V1-scope issue, but a *source-integrity* escalation: `context/assessments/2026-06-23_smart-home-architecture-prior-art_research-return.md` §2.10/§8 lists "SafeGate" as a FACT-tier arXiv citation; this pass could not retrieve any page naming it and the claimed ID returned an anomalous empty body. **Hub: flag for the next time that study is cited as authority** -- the *pattern* (pre-execution safety gating) is real and supported by other VERIFIED sources, so no decision built on the pattern is affected, but the specific named citation should not be repeated as verified. (The PM assessment already hedged the arXiv set as "verify before quoting as authority"; this confirms one did not verify.)

- **H-3 -- AX-7 provenance-on-components may want an envelope/attribution touchpoint.** §3 item 3 proposes recording *authoring provenance* (which AI/model/version vs human) on authored/shareable components, riding the existing `definitionHash` -> `ComponentRef` attribution. **V1 non-preclusion check:** this is a *read-side/registry* concern (Doc 16 §3.2/§3.3 says attribution adds no event field, AMD-92 untouched), so it appears non-precluding by construction -- **hub: confirm V1's component/`definitionHash` attribution path leaves room to associate authoring provenance later without an event-schema change.** If provenance ever needs to be *event-resident*, that is a formal AMD (out of scope here; flag the dependency).

- **H-4 -- Optional semantic-policy constraints on AI proposals are a *future* seam the frame should not foreclose.** §2.1/§4.2 are explicit that the static linter checks *form*, not *intent*; semantic-intent safety rests on human confirmation today. A future AIoT milestone may want optional, declarative *policy constraints* ("AI may never propose unlocking an exterior door without explicit confirmation") evaluated at the verification stage -- the analog of the surveyed "task safety contracts." **V1 non-preclusion check:** V1 should not foreclose adding a policy/constraint evaluation step at the proposal-verification boundary. This is *almost certainly* already open (policy would compose over the sealed model + the proposer-only port, both additive) -- **hub: light-touch confirm, no V1 action.** Note for Doc 17: this is a candidate to *name* as a reserved sub-seam of the AI-safety frame, but naming it is Doc 17 work, not a V1 change.

- **H-5 -- The "prefer local intents" two-tier (deterministic-first) is a UX-layer seam, not a V1 build, but should not be foreclosed.** HA Assist's deterministic-first/LLM-fallback (S7) is the production-validated shape; a HomeSynapse voice/NL layer would want the same (deterministic intent handling first, LLM only for unrecognized requests -- also a *latency* necessity, per the prior study's "reasoning models are catastrophic for voice latency"). **V1 non-preclusion check:** purely a future-layer concern over the existing engine; **hub: confirm nothing in V1 assumes an LLM-primary path.** (Low risk; V1 builds no AI path at all.)

---

## Sources (tier-tagged; only links actually opened are listed)

**VERIFIED -- primary source retrieved and read (or its abstract page opened):**
- VeriMAP -- "Verification-Aware Planning for Multi-Agent Systems," arXiv 2510.17109 -- https://arxiv.org/abs/2510.17109 (abstract page opened; planner-defined verification functions).
- "Blueprint First, Model Second: A Framework for Deterministic LLM Workflow," arXiv 2508.02721 -- https://arxiv.org/abs/2508.02721 (deterministic engine owns the path; Double-Check safety-gate node).
- VeriPlan -- "Integrating Formal Verification and LLMs into End-User Planning," arXiv 2502.17898 (CHI '25) -- https://arxiv.org/abs/2502.17898 (PRISM model-checking of LLM plans vs user constraints; HCI end-user tool -- scope-limited).
- f-secure LLM system -- "System-Level Defense against Indirect Prompt Injection Attacks: An Information Flow Control Perspective," arXiv 2409.19091 -- https://arxiv.org/abs/2409.19091 (coins "f-secure LLM system"; security monitor on planning input; "SEPF" NOT confirmed).
- "Architecting Resilient LLM Agents: A Guide to Secure Plan-then-Execute Implementations," arXiv 2509.08646 -- https://arxiv.org/abs/2509.08646 (plan-then-execute as a security control).
- Home Assistant Assist / voice control -- https://www.home-assistant.io/voice_control/ and developer LLM API -- https://developers.home-assistant.io/docs/core/llm/ (deterministic-first "handle commands first," LLM fallback; LLM reaches only intents/exposed entities). Plus the "prefer handling commands locally" behavior corroborated at https://www.home-assistant.io/blog/2025/09/11/ai-in-home-assistant/.
- NIST AI Risk Management Framework (AI RMF 1.0 / NIST AI 100-1) -- https://www.nist.gov/itl/ai-risk-management-framework (PDF: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf); GenAI Profile AI 600-1 referenced.
- OWASP Top 10 for LLM Applications -- https://owasp.org/www-project-top-10-for-large-language-model-applications/ ; OWASP Top 10 for Agentic Applications / Agentic AI (released Dec 2025) -- https://genai.owasp.org/2025/12/09/owasp-genai-security-project-releases-top-10-risks-and-mitigations-for-agentic-ai-security/ .

**PATTERN-REAL -- architectural pattern broadly attested; no single primary paper attributed:**
- The generic "probabilistic planner -> deterministic verifier/safety-gate -> deterministic executor + audit trail" shape -- attested across S1-S7 above plus the plan-then-execute security framing; assert as the field's direction, not as any one group's result.
- Pre-execution safety gating with explicit safety contracts (the *concept* SafeGate names) -- real and supported by adjacent VERIFIED work; **the specific paper/ID is UNVERIFIED (see below).**

**UNVERIFIED -- could NOT retrieve; DO NOT cite as authority:**
- "SafeGate" / claimed arXiv 2604.05427 -- no page naming it was retrievable; the ID returned an anomalous empty body on every fetch. Concept real; this citation not confirmed. (Escalation H-2.)

**Spine inputs (read, not re-verified -- internal authoritative docs):**
- Doc 17 DRAFT (`homesynapse-core-docs/design/17-aiot-and-cloud-readiness.md`); Doc 16 LOCKED §3.2/§3.3/§5/§6/§7/§8 (`design/16-superior-automation.md`); the 2026-06-26 independent Doc 17 DOCS review (E3, the AIOT-INV verdicts, the id source-verification); the 2026-06-25 deeper-M7 decision record (D2 pure-function-replay; the reserved AI-safety-frame seam); the 2026-06-23 prior-art study + its PM assessment (the planner/verifier/executor consensus finding + the explicit arXiv-fabrication hedge this pass acted on).

*Returned 2026-06-26 by SESSION V2-C. This report matures Doc 17 and the moat/claim; it changes no V1 scope and mints nothing. The hub reconciles it, checks the V1-non-preclusion escalations (H-1..H-5), and owns any spine/Doc-17 fold.*
