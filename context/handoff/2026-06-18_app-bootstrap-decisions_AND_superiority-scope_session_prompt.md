<!--
file: context/handoff/2026-06-18_app-bootstrap-decisions_AND_superiority-scope_session_prompt.md
purpose: Dispatch-ready brief for a FRESH Cowork session that drives two decision payloads to closure — (A) the app-bootstrap design decisions (C1 bind posture, AB-1 auth model, C2 confidentiality-vs-availability contract, the Doc 15 §6 currency amendment) and (B) the Phase-1 SCOPE RULING for a new Locked design doc on market superiority in home automation AND reliability, explicitly aimed at winning BOTH home users AND business/enterprise users. Nick rules; the PM/Architect assembles each decision package, records the rulings, and dispatches the design-doc authoring.
audience: PM/Architect (a FRESH Cowork conversation, nexsys-project-manager skill — Mode 3 for Part A decisions, Mode 1 Architect for Part B scoping), Nick (rules every decision)
state-type: session prompt (decisions + Phase-1 scoping)
status: READY — authored 2026-06-18 at the converge session. Run as a fresh Cowork conversation. Spine is freshly reconciled to PASS as of 2026-06-18.
baseline: core 03f16dc (substantive 1eddd9a) / docs f2e064d / hivemind <the converge commit> ; M6 COMPLETE; M7 contracts ratified (AMD-88..93); M7.1 ISSUED-awaiting-build; energy/erasure interview gate RETIRED.
reads (in order):
  - context/process/cowork-environment-model.md (FIRST)
  - context/status/PROJECT_SNAPSHOT.md (the 2026-06-18 masthead note) + weeks/2026-W26_jun22-jun28.md
  - context/planning/2026-06-15_app-bootstrap_charter.md (Part A — the AB-1..AB-4 decomposition + entry-gate; already advanced 2026-06-18)
  - context/audits/2026-06-15_core-review_CONVERGE_synthesis.md (C1/C2/C9 + Seam 1) + the R-α and R-δ PM assessments (the read-contract + auth/bind/startlevel/key-portability evidence)
  - context/handoff/2026-06-18_automation-superiority_Phase1-design_session_prompt.md (Part B — the vector detail + the M7 interlock) + context/planning/2026-06-14_automation-engine-superiority_research-vector_proposal.md (the 10 vectors)
  - homesynapse-core-docs/design Doc 07 (Automation, Locked), Doc 12 (Lifecycle), Doc 14 (Master Arch), Doc 15 §3.8/§5/§6 ; the strategy layer (context/strategy/; catalog in strategic-context-map.md §2) ; DESIGN_DOC_TEMPLATE.md
-->

# Session Brief — App-Bootstrap Decisions + Superiority Design Phase-1 Scope

PM/Architect session (**nexsys-project-manager** skill). Read `context/process/cowork-environment-model.md` FIRST, then run the freshness preflight against the pinned baseline above (the spine was reconciled STALE→PASS on 2026-06-18; Check 9 should be clean — Nick ran the mirror sync). This session has **two payloads**; do them in order. Nick rules every decision; you assemble the package, record the ruling in the right places, and hand over commit messages. Do not edit any Locked design doc except via the formal re-open→review→ratify pipeline.

**Step 0 (both payloads):** preflight; reconcile HEADs; **check whether CC-1 (bind-address spike) and R-γ (crypto-agility envelope-versioning) have returned** — they were dispatched but may not be back. Their return-state changes how Part A's A1/A4 resolve (see below). Note the state explicitly and proceed; do NOT block the session on them.

---

## PART A — App-bootstrap decisions (drive to rulings; this finalizes the charter)

The app-bootstrap milestone is the runnability unlock and a high-density latent-defect milestone — `main()` wires `HomeSynapseCore`, the cipher activates, and the HTTP surface opens, all at once (charter §1, Seam 1). The design evidence is largely in hand (R-α assessed, R-δ assessed); these are now Nick's rulings. For each, present the options + the evidence-backed PM recommendation, get Nick's ruling, and record it.

**A1 — C1 bind posture (INV-SE-02).** PM rec (R-δ AX-1, web-verified CVE class): **loopback-default; LAN exposure is explicit, authenticated opt-in; never bind-all-by-default; never treat an interface as "internal" (`/internal/*` goes behind auth too).** If CC-1 has returned, fold its empirical bind finding; if not, rule the posture now and mark CC-1 as a *confirm-mechanics* gate on the coding instruction (not on this decision).

**A2 — AB-1 auth model.** The open design decision (charter §7). PM rec (R-δ AX-1(S)): **a token-issuance model; the WebSocket is an external interface that needs auth; zero-config stays authenticated with no default/shared bootstrap secret and no pre-auth account enumeration.** Nick rules the scheme. This is the one with the broadest public-API-shape implication — settle it deliberately.

**A3 — C2 confidentiality-vs-availability contract (the read path).** R-α is assessed (charter §3 = CLOSED). PM rec: **fail-closed at MVP** (GCM-auth-fail / missing-or-corrupt root key → fail the read batch closed with a distinct loud error), **design the degrade seam now** (cause-carrying `DegradedEvent`, `(scope,key_version)` cause lookup) but keep the *degrade behavior* OUT (it ships with the crypto-shred WU), and carry the **rotate-DEK-on-restore boot invariant**. Confirm the **F4 chain-liveness sequencing pin** (the degrade/chain-validity parts must not enable until `chain_hash` + startup verification are live). Nick rules the contract.

**A4 — Doc 15 §6 currency amendment (rotate-DEK-on-restore).** Quick ratification gate (charter §3). Rule whether to ratify now ("rotate = additive new DEK version, retain priors" per Track-3 F6) or queue it; if F1 envelope-discriminator (R-γ) is back, fold that ruling here too (PM rec if R-γ absent: **rule the 1-byte version tag in now** — it is cheap-now / irreversible-after-first-write, so default to the tag rather than implicit-v1).

**Part A done-when:** each of A1–A4 ruled or explicitly parked with a named trigger; the app-bootstrap charter finalized to that state; the entry-gate table updated; a one-line statement of what still blocks the first AB coding instruction (expected residual: CC-1/R-γ empirical confirmations only). Add the **app-bootstrap milestone rows** (AB-1..AB-4) to `phase-3-milestone-backlog.md`.

---

## PART B — Superiority design: Phase-1 SCOPE RULING (a new Locked design doc)

**The thesis (Nick's framing):** design the layer that makes HomeSynapse *win on home automation AND reliability* — for **both** home users and business/enterprise users. This is the differentiator, and it must be designed (Phase 1) **before** M7.2/M7.3 implement the baseline engine, so the build targets it. Output of this part: a **Phase-1 scope ruling** + the dispatch of the Architect-mode design-doc authoring (or the first doc draft if the scope is small enough to start in-session).

**Frame the scope decision around two co-equal superiority axes and two market segments** (this is the lens for ranking the vectors — detail in the 2026-06-18 superiority brief + the vector proposal):

1. **Automation superiority** — expressiveness-without-a-DSL (power without a Turing tarpit; the hard anti-requirement holds), explainability / the AMD-91 run-causal-chain as a first-class product surface ("why did this fire?"), determinism.
2. **Reliability superiority** — the differentiator the user named co-equally: crash-safety, self-healing, honest degradation, the "runs for years on a Pi without intervention" promise made *legible and provable* to a buyer. This likely draws on the existing event-sourced spine + Doc 12 lifecycle + the observability surface, elevated into a *product* claim, not just an internal property.
3. **Dual-market fit** — what wins **home users** (trust, local-first, zero-config, explainability) vs **enterprise/business** (B3 multi-site/enterprise federation, fleet management, audit/compliance posture, the Assure/Care institutional positioning). Some vectors serve one segment; federation + reliability + honest-hybrid serve both.

**Assemble the scope decision package for Nick** — for each candidate cluster (expressiveness-without-DSL · explainability/causal-chain · reliability-as-a-product-claim · B3 federation · honest-hybrid deployment): the **per-segment differentiator thesis** (home vs enterprise), the **lock point**, the **design size** (P1 sizing smell-test — federation and reliability-as-a-claim may *each* exceed one doc), the **cross-subsystem blast radius**, **new invariants implied**, and the **M7-contract impact**. **Recommend a primary scope** (PM rec to present, Nick rules): a strong default is to anchor the new doc on the **two axes that win both segments at once — reliability-as-a-provable-product-property + the expressiveness/explainability automation surface — with B3 federation either folded as a first-class section or split into its own doc** if sizing demands (P1).

**The M7 interlock (do NOT skip — charter §4 of the superiority brief):** for the ruled scope, produce a one-line verdict per M7.x piece — *does this reshape M7.1 / M7.2 / M7.3 as currently scoped?* If M7.1's trigger/condition contracts are unaffected, say so explicitly (this un-blocks the M7.1 ride-along build); if affected, name the AMD/supersession and the sequencing consequence. Any contract change moves through the formal pipeline — never a silent reshape.

**Part B done-when:** a Phase-1 scope ruling recorded (which vectors → the new **Doc 16 candidate**, what splits into its own doc, what defers); the M7-impact verdict stated; and EITHER the Architect-mode design-doc authoring dispatched (`2026-06-18_automation-superiority_Phase1-design_session_prompt.md` updated with the ruled scope) OR — if scope is tight — the first DESIGN_DOC_TEMPLATE draft started in-session (all 13 sections, every cited INV/LTD addressed, open questions BLOCKING/NON-BLOCKING, self-reviewed).

---

## Anti-requirements (bind both parts — non-negotiable)
No templating DSL (expressiveness comes another way) · no engine retry · no destructive forced migration · never lead with commodity encryption · **local-first is inviolate** — any cloud/hybrid/enterprise-federation element is honest and optional, never a hidden dependency. The enterprise story must not compromise the home-user trust brand.

## Closeout (record the decisions where they belong)
Write the rulings to `context/decisions/2026-06-18_app-bootstrap-and-superiority-scope_decisions.md` (a new decision record); finalize the app-bootstrap charter; update PROJECT_SNAPSHOT (masthead + Current-WU), the backlog (AB rows + the Doc 16 row), and the W26 lanes; run the WUCP drift check; hand over commit messages (bang-free / `git commit -F`). Escalate anything that implies a new invariant or an M7-contract reshape — those are Nick's Phase-1 calls.
