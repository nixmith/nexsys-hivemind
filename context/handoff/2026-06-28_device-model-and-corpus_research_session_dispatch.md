<!--
file: context/handoff/2026-06-28_device-model-and-corpus_research_session_dispatch.md
purpose: Dispatch brief for a write-isolated deep-research Cowork session (Stream B) — how HomeSynapse should represent, store, and manage its device/component compatibility model + characterization corpus, objectively benchmarked against the prevailing models, returning a concrete corpus + onboarding-pipeline recommendation that REALIZES the ratified D5 and feeds Doc 02/08 + M9 + the nexsys-bench harness.
audience: a fresh research Cowork conversation (write-isolated; web-backed); returns route to the PM hub for reconciliation into Doc 02/08 governance + the nexsys-bench Phase-2 model.
state-type: research dispatch
status: READY — authored 2026-06-28 (v10 hub). Launch as its own Cowork conversation, parallel to the bench (Stream A Phase 0/1); upstream of Stream A Phase 2.
anchors: context/decisions/2026-06-28_bench-test-and-truth-engine_decision-record.md (R5 + the three sharpenings) · context/decisions/2026-06-25_deeper-M7-automation-architecture_decision-record.md (D5 RATIFIED — adapt-the-data + curated-subset fallback; this research REALIZES it) · homesynapse-core-docs/design/02-device-model.md (Locked) · design/08-zigbee-adapter.md §3.5 · INV-CE-04 (protocol agnosticism) · device-model confirmation types (ConfirmationMode, ExpectedOutcome, Expectation) · project-knowledge/device-corpus/ (the corpus this model governs).
-->

# Research Dispatch (Stream B) — the device-representation model that realizes D5

## The question (precise)

**How should HomeSynapse represent, store, code-for, and maintain its device/component compatibility model and characterization corpus — to be objectively better, for our specific architecture, than the prevailing approaches — and what is the concrete corpus schema + device-onboarding pipeline we should adopt?**

This is NOT greenfield. It must **realize the already-RATIFIED D5** (adapt-the-data + curated-subset fallback) and conform to **Locked Doc 02 (device model)** + Doc 08 §3.5 (cluster→capability) + INV-CE-04 (protocol agnosticism). Frame the output as "the corpus model that realizes D5," never as a design that could contradict locked decisions — if the research finds tension with a locked decision, surface it as an escalation, do not silently diverge.

## Survey targets (benchmark these objectively)

Compare how each represents devices — data-vs-code balance, version-control/diff story, graceful degradation for unknown devices, ZCL alignment, multi-protocol generalization, scale/rot resistance, licensing (already partly settled by D5):
- **Home Assistant** — the `components/` integration model (code-per-integration).
- **Zigbee2MQTT** — the converters DB + the `exposes` capability model (data-driven, one external DB) — the D5 "adapt-the-data" source.
- **zigpy / `zha-device-handlers`** — "quirks" (code-as-patches per device).
- **deCONZ DDF** — JSON device descriptors (the most "data, not code" model).
- **Matter** — the standardized device-type / cluster spec (a type system).

## Evaluate against OUR constraints

Local-first; **event-sourced** (the model must produce/consume our event-log cleanly — it feeds the nexsys-bench replay fixtures + M9); **ZCL-aligned**; **must-degrade-honestly** (an unknown device surfaces honestly, never a silent wrong abstraction — the INV-SA-03 / never-silent-blank ethos); scale to thousands of entries across protocols without rotting (the truth-hierarchy/pointer-not-copy discipline).

## Three sharpenings (bind the output)

1. **Realize D5 + Locked Doc 02.** The recommended model is how D5's "adapt-the-data + curated-subset fallback" becomes a concrete schema, consistent with Doc 02. Cite the specific Doc-02 contracts it satisfies; flag any gap as a Doc-02/08 amendment candidate.
2. **First-class the confirmation semantics.** The corpus must represent *whether and how a device confirms* — its expected-outcome / `ConfirmationMode` (EXACT_MATCH/TOLERANCE/ENUM_MATCH/ANY_CHANGE/DISABLED) — so the corpus directly supports the `confirmed | unconfirmed | failed` moat, not just cluster/attribute description. A device entry must answer "does this device let us render a true CONFIRMED, and when does it honestly become UNCONFIRMED?"
3. **Return the onboarding pipeline.** Deliver the end-to-end: interview → corpus entry → device-model mapping → M9 acceptance. That pipeline is the durable thing the nexsys-bench harness seeds; the recommendation must say how a new device flows through it (and how the bench's captured fixtures + the M9 adapter's interview/codec relate to it).

## Deliverable + discipline

A cited report returning: (a) the comparative survey with an objective scorecard; (b) **the recommended corpus schema** (realizing D5, first-classing confirmation, ZCL-aligned, degrade-honest); (c) **the onboarding-pipeline design**; (d) any Doc-02/08 amendment candidates; (e) licensing/maintenance notes (pin-version-and-record-license per D5's hedge). **Web-backed source discipline** — every load-bearing claim VERIFIED with a primary source, honest `UNVERIFIED` flags, no fabricated citations (the standing research-return bar). **Write-isolated:** the session returns the report to `context/assessments/`; the hub reconciles it into Doc 02/08 governance + the nexsys-bench Phase-2 model. It writes no production code and no spine.
