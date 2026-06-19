<!--
file: context/decisions/2026-06-18_app-bootstrap-and-superiority-scope_decisions.md
purpose: The decision record for the 2026-06-18 app-bootstrap-decisions + superiority-scope session. Captures Nick's rulings on Part A (A1 bind posture, A2 auth model, A3 read contract, A4 Doc 15 §6 amendment + F1 tag) and Part B (the Phase-1 superiority design-doc scope ruling + the M7 interlock). Nick ruled; the PM assembled the packages and recorded here.
audience: Nick, PM, the future app-bootstrap coding-instruction session, the Architect-mode Doc 16 session
state-type: decision record
status: COMPLETE 2026-06-18 — Part A (A1-A4) RULED + recorded; Part B superiority Phase-1 scope RULED + Architect-mode authoring dispatched. Charter finalized; backlog/snapshot/W26 updated; commit messages handed over.
baseline: core 03f16dc (substantive 1eddd9a) / docs f2e064d / hivemind <converge> ; M6 COMPLETE 4-of-4 ; M7.1 ISSUED-awaiting-build ; watermark AMD-93 (invariants 163/47) ; Doc 15 LOCKED.
preflight: PASS (all 11 checks) 2026-06-18. Step 0: CC-1 (bind-address spike) + R-γ (crypto-agility envelope-versioning) BOTH still in flight (dispatched 2026-06-14, no returns) — the expected residual.
-->

# Decisions — App-Bootstrap (A1–A4) + Superiority Phase-1 Scope (Part B)

Session: 2026-06-18 converge follow-on (fresh Cowork, nexsys-project-manager). **Nick rules every decision; the PM assembled each package and records the ruling here.** Freshness preflight **PASS**; HEADs reconciled to the pinned baseline; Step 0 return-state: **CC-1 and R-γ both still in flight** (dispatched 2026-06-14; no return files; confirmed by the 2026-06-18 cross-agent note). That return-state sets A1 to rule-now-with-CC-1-as-confirm-gate and A4 to reserve-the-tag-now.

---

## PART A — App-bootstrap decisions (RULED 2026-06-18)

### A1 — C1 bind posture (INV-SE-02) → **RULED: loopback-default.**
**Ruling (Nick):** Bind **loopback by default**; LAN exposure is an explicit, **authenticated** opt-in the user configures. **Never bind-all-by-default.** Never treat an interface as "internal" — `/internal/*` goes behind auth too. Rationale: secure-by-default is non-negotiable for a trust-brand product, and all-interfaces-by-default is literally the **CVE-2026-34205 (CVSS 9.7)** failure class R-δ web-verified. Loopback-default does not block LAN use — it makes LAN exposure deliberate. Options (2) all-interfaces+auth and (3) block-on-CC-1 both **rejected** (the latter a false blocker).
**CC-1 disposition:** CC-1 has not returned, but it only **confirms bind mechanics** — it does not change the posture. **Do not block on it.** It rides the AB-1 coding instruction as a *confirm-mechanics* gate (assert the bound socket answers only on loopback unless LAN opt-in is configured; `grep -rn "\.host(" lifecycle api`).
**Lands in:** AB-1 (C1/INV-SE-02). Closes the A1 charter gate. Carries the R-δ AX-1 path-canonicalization-before-auth pin (CVE-2023-27482 traversal lesson).

### A2 — AB-1 auth model → **RULED: token issuance.**
**Ruling (Nick):** Adopt a **token-issuance model.** Bearer tokens minted at first-run/pairing; the **WebSocket is an external interface and is authenticated**; zero-config stays **authenticated** — **no default/shared bootstrap secret** (Mirai default-credential class), **no pre-auth account enumeration** (HA 2023.12 username-leak class), no unauthenticated stream/media path ever (Eufy/VLC class). Rationale: this is the highest-stakes, hardest-to-reverse call (public-API shape), so optimize for the long horizon. A single API key is a shared secret with no per-client revocation or scoping — a corner the moment there is a web UI + mobile + the enterprise/federation direction. Session-cookie+CSRF is browser-centric and awkward for the WS/API surfaces. Options (2) single-API-key and (3) session-cookie+CSRF **rejected**.
**Binding caveat (Nick — carry into the design):** **design the token model now to anticipate enterprise scoping (per-scope / per-site claims),** even if MVP issues them simply. Cheap-now hook for the dual-market (home + enterprise/federation) direction set this session; retro-fitting scoped claims after users hold tokens is the expensive path.
**Lands in:** AB-1 (auth). Closes the A2 charter gate. **Strategy-adjacent** (public-API shape) — recorded as a ruled Nick-call, not a PM-local decision.

### A3 — C2 confidentiality-vs-availability read contract → **RULED: fail-closed at MVP + design the degrade seam now.**
**Ruling (Nick):** On a read-path decrypt failure (GCM-auth-fail / missing-or-corrupt root key / chain-hash failure) → **fail the read batch closed with a distinct, loud error** at MVP. **Design the degrade seam now** (the cause-carrying `DegradedEvent` type + the `(scope, key_version)`-keyed cause lookup + the chain-validity check) but keep the **degrade behavior OUT** — it ships with the crypto-shred WU. Carry the **rotate-DEK-on-restore boot invariant** (refuse to encrypt in a scope until a fresh DEK is installed or the persisted counter is proven ≥ all prior nonces — R-α REC-235). Rationale: option (2) flat catch-and-degrade is **disproven**, not merely dispreferred — R-α (grade A, **REC-234**) showed it masks CASE-b corruption/tampering as if intended = a silent security hole. (1) beats (3) because the seam is **design-only** (zero MVP risk; the degrade behavior still ships later with crypto-shred), making the future degrade cheap.
**Binding caveat (Nick — F4 pin):** the **degrade half and the chain-validity check stay DISABLED until `chain_hash` computation + mandatory startup verification are live.** They are 32-byte ZERO for every event today. The MVP fail-closed half does **not** need a live chain. Wire fail-closed now; gate the chain-dependent parts on chain activation.
**Lands in:** AB-2 (fail-closed half + seam) / crypto-shred WU (degrade half). Closes the A3 charter beat. Sharpens OR-RF-DECRYPT.

### A4 — Doc 15 §6 currency amendment (rotate-DEK-on-restore) + F1 envelope version tag → **RULED: ratify the amendment now + reserve the 1-byte tag now.**
**Ruling (Nick):** **Bind rotate-DEK-on-restore** as the restore contract ("rotate = **additive new DEK version, retain priors**" per Track-3 F6, so pre-restore rows stay readable); **demote carry-high-water-mark to a defense-in-depth cross-check** (assert resumed counter ≥ carried max, never the sole guarantee). This closes **OR-M6-NONCE restore-half** on ratification (R-α Problem 1). **AND rule the 1-byte envelope version discriminator IN now** — it is irreversible after the first encrypted write, and that write happens at app-bootstrap; waiting for R-γ and adding a discriminator afterward means migrating an immutable (soon hash-chained) log. **Reserve the slot now: v1 = the current envelope.** R-γ later refines the version *policy*, not whether the slot exists. Options (2) defer-tag and (3) queue-both **rejected**.
**Binding process caveat (Nick — Doc 15 is LOCKED):** the §6 amendment runs the **formal re-open → DOCS review → ratify pipeline** with a **watermark bump (AMD-93 → AMD-94)** and is **authored as an AMD**, not a silent edit to the Locked doc. Same for recording the F1 discriminator decision and the rotate-on-restore binding into Doc 15 §3.4/§6. The PM authors the AMD; DOCS reviews; Nick ratifies.
**Lands in:** AB-4 (envelope-finalization gate, F1) + the Doc 15 §6 AMD. Closes the A4 charter gate **on AMD ratification** (the ruling is made; the doc edit is the pipeline step).

### Part A done-when — status
- A1–A4 all **RULED** (none parked). ✅
- App-bootstrap charter **finalized** to the ruled state (status + §3 entry-gate table updated; see the charter). ✅
- AB-1..AB-4 milestone rows **added** to `phase-3-milestone-backlog.md`. ✅
- **One-line residual blocking the first AB coding instruction:** only the **empirical/mechanical confirmations** remain — **CC-1** (bind mechanics, rides AB-1 as a confirm-gate), **R-γ** (refines the version-tag policy; the slot is already reserved), and **AMD-94 ratification** of the Doc 15 §6 amendment (PM authors → DOCS → Nick). No decision gate remains open. Sequencing on issue: **AB-3 first** (lifecycle substrate), then **AB-1 + AB-2 + AB-4 together** (the Seam-1 go-live event).

---

## PART B — Superiority design Phase-1 scope ruling (RULED 2026-06-18)

**The thesis:** design the layer that makes HomeSynapse win on home automation AND reliability, for BOTH home and business/enterprise users, as **design (Phase 1) before M7.2/M7.3** freeze the baseline-engine contracts. Strategy-layer ground (digested this session): enterprise/institutional value (Assure insurance-attestation, Care aging-in-place, fleet) is a **same-runtime licensing + API tier, not a fork**; MVP is obligated only to the **structural preconditions** (consent-scoped categories, multi-tier aggregates, attestation-ready log), not the enterprise APIs. The 10 vectors (proposal Groups A–E) collapsed into five candidate clusters; each was packaged for Nick (thesis home|enterprise · lock point · size · blast radius · new invariants · M7-impact).

### The scope ruling (Nick) — the document landscape

**Doc 16 (the anchor — dispatched now, Architect-mode Mode-1) = three first-class sections:**
1. **Expressiveness-without-a-DSL** (D1 reusable/parameterized components, computed conditions, typed parameters — static-analyzable, no templating DSL). Tightest M7 interlock — shapes the M7.2 action model. This is the core "design-before-M7.2" justification.
2. **Explainability / causal-chain as a first-class product surface** (AMD-91 `RunCausalChain` → "why did this fire?"). Half the home-user differentiator (the top opacity complaint in the HA/SmartThings pain corpus) AND an enterprise audit surface — so option 2 (expressiveness-only) was rejected as too thin.
3. **Run-coupled reliability** — honest degradation of a *running* automation + deterministic/safe behavior under failure. This is the part of "reliability" that touches the run model and **shapes the M7.2 contracts**, so it belongs in Doc 16.
- **Plus a federation-readiness SEAM** (B-2): identity/scoping non-preclusion only — so a future federation layer never forces an immutable-log migration.
- **Plus a hybrid cut-line** (B-3): the local/remote boundary + never-a-dependency invariant, **coordinated with app-bootstrap** (the seam is pinned in app-bootstrap's composition root).
- **Plus the mandatory M7-contract-impact section** (§4 of the superiority brief — see the verdict below).

**B-1 refinement (Nick — the key sharpening):** "reliability" is **two architecturally-distinct things; only the run-coupled half belongs in Doc 16.** The **cross-cutting reliability-as-a-product-property** half — multi-year longevity claims, observability-as-product, system-wide self-healing — is distinct (lifecycle/persistence/observability), **not M7-gating, and large enough to be its own epic.** Folding it into Doc 16 would reproduce the M4-retrospective "epic hidden under one label" failure. → **It becomes its own co-equal doc, sequenced right after Doc 16** (it doesn't gate M7, so it follows without stalling the engine; reliability stays co-equal in the thesis — arguably *elevated* by its own first-class doc).

**Splits (each its own doc; numbering pinned at authoring):**
- **Cross-cutting reliability-as-a-product-property** — own co-equal doc, sequenced right after Doc 16. NOT M7-gating.
- **B3 multi-site / enterprise federation** (B-2 → option 1, ratified) — own post-M8 doc. Implies several new invariants (cross-site event/state boundaries, federated identity, WAN-partition autonomy). Doc 16 reserves only the **identity/scoping seam** — cheap insurance against an irreversible event-log foreclosure (the same cheap-now / irreversible-later logic as A4's version tag). Fold-now (option 2) rejected as a P1 violation; defer-with-no-seam (option 3) rejected because identity/scoping is foundational and retrofitting it means migrating the immutable log.
- **C1 honest-hybrid deployment** (B-3 → option 1, scoped tight) — own doc, sequenced with/after app-bootstrap. **Scope: the local/remote boundary + the never-a-dependency invariant only** (the full future cloud-accelerator feature defers). Rationale: "cloud-optional, never a dependency" is a brand-critical architectural boundary — burying it as an ad-hoc charter constraint would under-design the promise the trust brand rests on. (Lean fallback, not taken: cut-line into the charter + a committed future doc.)

**Deferred to M7.2/M8 research briefs (ride a real engine, not a blank sheet):** A2 (conflict-at-scale), B1 (cost curve), B2 (concurrency/backpressure), D2 (expected-state vs bounded re-issue / REC-162 — the standing escalation), E2 (reachability/asleep-vs-dead). These sharpen M7.2/M8 directly and are cheap to ground once the action model is drafted.

### The M7 interlock verdict (the ride-along un-block)
- **M7.1 (trigger/condition path) — UNAFFECTED** by the ruled scope. ②/③ consume the spine/run-chain; ① expressiveness is designed as a parameterization/composition *layer over* the sealed model, not a change to the sealed trigger/condition types. **M7.1 is cleared to build in parallel** — contingent on Doc 16 §4 holding this line. If the expressiveness design finds it *must* change a condition contract, that becomes a formal AMD that re-sequences M7.1 (never a silent reshape).
- **M7.2 (run/action/dispatch) — SHAPED by Doc 16** (the expressiveness/action-model surface + the run-coupled reliability section). **Do NOT freeze M7.2's action contract before Doc 16 Locks; M7.2 builds *into* it.** No shipped/ratified contract is reshaped (M7.2 is unbuilt) — this is forward-shaping, which is the whole point of designing now.
- **M7.3 (pending-command ledger) — UNAFFECTED** by the ruled scope. D2/REC-162 stays the separately-escalated M7.2-action question; it touches M7.3 only if folded in (it is not, here).

### B-4 — authoring dispatch → **RULED: dispatch a fresh Architect-mode session.**
The ruled scope is not tight (an automation-model doc with two seams + a coordinated hybrid doc + a queued reliability doc), so the "start in-session only if tight" condition is not met; and a Locked design doc in full Architect discipline (13 substantive sections, every INV/LTD addressed, self-review, DOCS review → Lock) deserves a fresh unloaded session (this one has already done Part A + Part B scoping). **Action:** the superiority Phase1-design session prompt (`context/handoff/2026-06-18_automation-superiority_Phase1-design_session_prompt.md`) is updated with the ruled scope and is ready to dispatch.

### New invariants / escalation note (Nick's Phase-1 calls — flagged per skill §4)
- **B3 federation** implies **several new invariants** (cross-site boundaries, federated identity, WAN-partition autonomy) — owned by the future federation doc, not minted here. Doc 16 only reserves the identity/scoping seam.
- **C1 honest-hybrid** implies the **local/cloud cut-line invariant** (every automation runs locally during a WAN outage; no cloud service holds the keys) — owned by the hybrid doc; a precise statement of the existing local-first-inviolate principle.
- **No ratified M7 contract is reshaped** by this ruling. M7.2 is *forward-shaped* (unbuilt). Any contract change the Doc 16 authoring surfaces moves through the formal AMD/supersession pipeline.

### Part B done-when — status
- Phase-1 scope ruling **recorded** (Doc 16 anchor + 3 sequenced split docs + 5 deferred vectors). ✅
- M7-impact verdict **stated** (M7.1 unaffected / M7.2 shaped / M7.3 unaffected). ✅
- Architect-mode authoring **dispatched** (session prompt updated with the ruled scope; B-4). ✅

---

## Closeout summary

**Net document landscape set this session:** **Doc 16** = expressiveness-without-DSL + explainability/causal-chain + run-coupled reliability, with a federation (identity/scoping) seam and a hybrid cut-line coordinated with app-bootstrap, plus the M7-contract-impact verdict per M7.x; **cross-cutting reliability** and **federation** as their own sequenced docs; **honest-hybrid** as its own tight doc with app-bootstrap. Anti-requirements bind throughout (no templating DSL · no engine retry · no destructive forced migration · never lead with commodity encryption · local-first inviolate, any cloud/hybrid/enterprise element honest and optional; the enterprise story must not compromise the home-user trust brand).

**Files updated this session:** this decision record (new); `context/planning/2026-06-15_app-bootstrap_charter.md` (finalized to ruled state); `context/planning/phase-3-milestone-backlog.md` (AB-1..AB-4 + Doc 16 + split-doc rows); `context/handoff/2026-06-18_automation-superiority_Phase1-design_session_prompt.md` (ruled scope folded; dispatch-ready); `context/status/PROJECT_SNAPSHOT.md` (masthead + Current-WU); `context/planning/weeks/2026-W26_jun22-jun28.md` (lanes); `context/handoff/cross-agent-notes.md` (rulings note). WUCP drift check run; commit messages handed to Nick (bang-free, `git commit -F`).

---

## Addendum — 2026-06-18 (later): M7.1 composition-root wiring deferral (PM adjudication of Coder pushback)

During the M7.1 build the Coder surfaced an evidence-based blocker (skill §4a pushback — **ACCEPTED**): the composition root assembles no production `ConfigurationService` and no Entity/Device/Area registry impls, so the `automation_engine` subscriber cannot be wired into `start()` and the mandated lifecycle wiring test cannot be written as specified. The trigger/condition core + the AMD-92 event slice are fully buildable against injected/stubbed deps.

**Ruling (PM): proceed per Option 1 — build the M7.1 core now; defer the subscriber-into-`start()` wiring + the lifecycle wiring test to app-bootstrap AB-3.** Composition-root assembly is app-bootstrap's chartered deliverable (C9/AB-3 — `main()` is a stub, the lifecycle is unwired), **not** M7.1's (charter §4: "M7.1 touches no composition root"). The core is buildable test-first against the existing exported interfaces; deferring the wiring is honest (no fake composition root to test against) and debt-free. **Option 2 (full pivot) rejected** — app-bootstrap is not issue-ready (CC-1/R-γ/AMD-94 residual open; no AB coding instruction authored), so pausing the buildable core just wastes the slot. **Option 3 (wire deps in this WU) rejected** — scope creep into the composition root + device-model breadth + C9, building the composition root ad hoc outside app-bootstrap's lifecycle/auth/phase design (the spike-becomes-production anti-pattern).

**Conditions on the Coder (Option 1 as accepted):** (1) build + test the core against injected/stubbed deps; (2) ship the `automation_engine` subscriber as a **wireable seam** (design-not-precluded — unit/behaviorally tested against a stubbed bus/registries) so app-bootstrap wires it with zero rework — the M6.3 "DP-D non-preclusion" pattern; (3) document the exact deferred wiring + its inbound deps for AB-3; (4) escalate it as **[BLOCKING]-on-app-bootstrap**, not a silent skip; (5) confirm no ratified contract (AMD-88..93) is touched and M7.1's trigger/condition contracts are unchanged (consistent with the Doc 16 **M7.1-UNAFFECTED** verdict).

**Inbound dependency created → app-bootstrap AB-3** (formalize at the M7.1 WUCP Phase 2 return — deferred now to avoid colliding with the concurrently-active M7.1 Code + Doc 16 Cowork sessions, per cowork-environment-model §2): AB-3 must (a) assemble `ConfigurationService` (impl exists, M6.1 — needs wiring) + production Entity/Device/Area registries into the composition root, (b) wire the `automation_engine` subscriber into `start()` with subscribe-after-state-store-catch-up, (c) carry the M7.1 lifecycle wiring test.

**Flag to Nick:** the Entity/Device/Area **registry production impls may not exist yet** (device-model breadth — AMD-44 Floor/EntityRole, Research-8 REC-23–30), distinct from `ConfigurationService` which exists and only needs wiring. So app-bootstrap's composition-root wiring may pull in some device-model breadth — a real input to app-bootstrap's true size/sequencing. Not a blocker for the M7.1 core build.
