<!--
file: context/handoff/2026-07-02_Doc18-plugin-ecosystem_research-and-charter_session_prompt.md
purpose: Dispatch brief for the Doc-18 research-and-charter lane (fresh, independent Cowork conversation) — (a) deep internet research into the successes, failures, and brilliant ideas of other smart-home ecosystems and best-in-class plugin platforms; (b) synthesize that evidence into a precisely-articulated REQUIREMENTS CHARTER for Doc 18 — Extension & Plugin Architecture (seam reservation, Doc-17 mold). The lane produces the evidence base and the charter; the PM hub authors the actual design doc against it (Mode 1), targeted to Lock BEFORE M9.3 freezes the profile registry.
audience: Research/strategy lane (fresh Cowork conversation; no role skill required — this is a research dispatch); Nick (rules the charter's decision points at review); the v14+ PM hub (two-layer audits the return).
state-type: session prompt (lane dispatch).
status: READY — authored 2026-07-02 by the v14 hub at beat 53, on Nick's ruling (R-A: research-first Doc-18 authorization).
baseline (RE-VERIFY at launch): core ec2e3b4 · docs 1509b34 (watermark AMD-97; invariants 172/51) · hivemind 7d65b35+ · bench 5ceff3b. Write-isolation: this lane writes ONLY its two deliverable files + a cross-agent note + _scratch commit prep. NO writes to design/, governance/, code, or the spine.
-->

# Doc-18 Research & Charter Lane — study the ecosystem wars, then articulate what Doc 18 must reserve

You are a research-and-synthesis lane for NexSys HomeSynapse. Take the time this deserves — depth over speed (Nick's directive: "as much time and effort as necessary"). Your product must be adversarially auditable: the hub source-checks load-bearing claims before anything folds.

## §1 The charge, two phases

**Phase A — the ecosystem study.** Deep web research into how other smart-home platforms and best-in-class plugin ecosystems actually won, lost, and scarred their users — extension/plugin architecture specifically, not general product history.

**Phase B — the Doc-18 requirements charter.** Convert the evidence into a precise, section-by-section articulation of what **Doc 18 — Extension & Plugin Architecture** must contain: what it reserves (builds nothing — the Doc-17 mold), the invariant candidates it mints, the decision points Nick must rule, and the evidence behind every requirement.

## §2 Ground FIRST (ordered; read before any web research)

1. `context/process/cowork-environment-model.md` (operating rules; §10 pre-commit audit) + `context/process/truth-hierarchy-and-pointer-not-copy-discipline.md`.
2. **`context/assessments/2026-07-02_extensibility-and-plugin-ecosystem_PM-assessment.md` — your foundation.** Its §2 gap inventory and §4 R-A reservation list are the requirements skeleton your charter fleshes out; its verdicts frame what Doc 18 does NOT need to solve.
3. `homesynapse-core-docs/design/17-aiot-and-cloud-readiness.md` — **the structural mold**: how a builds-nothing seam-reservation doc is shaped, how it pins non-preclusion invariants (AIOT-INV-1), how it keeps principles unminted.
4. `homesynapse-core-docs/design/16-superior-automation.md` §3.2 (component model) + §15-Q2 (**AX-7** — the unresolved versioning/deprecation gate; your charter must frame it with market evidence so Nick can rule).
5. `context/assessments/2026-06-27_smart-home-ecosystem-currency_research-return.md` — the prior research pass (its anti-fabrication tagging is your format precedent; do not re-research what it already verified — extend it).
6. `homesynapse-core/integration/integration-api/MODULE_CONTEXT.md` — the frozen SPI a third party would implement today (2 types; the plugin contract Doc 18 names).
7. Strategy pointers: `context/strategic-context-map.md` §2 → the Revenue/Licensing .md (Apache-2.0 rationale: community + commercial coexistence; the Connect "community integration repository access" line — R-C context, Nick's to rule, yours to evidence) + the Platform-to-Institution .docx (SDK 0–12 mo, marketplace 12–24 mo promises).

## §3 The research agenda (Phase A)

**Smart-home platforms (primary; per-platform: extension MODEL · distribution/trust mechanics · versioning/compat story · community dynamics · the sharpest failure · the most brilliant idea):**
- **Home Assistant**: core integrations vs HACS vs add-ons vs blueprints; the integration quality scale; breaking-changes cadence and community cost; why HACS exists OUTSIDE core and what that split teaches; supply-chain/security posture.
- **Zigbee2MQTT / zigbee-herdsman-converters**: the data-driven external-converter model (our D5 already keys on it) — contribution pipeline, quality control, what scales and what rots.
- **SmartThings**: the Groovy → Edge-driver migration — the canonical ecosystem-breaking transition; what promises were broken, what developers did, quantified fallout where sources allow.
- **Homebridge / HomeKit**: npm-based plugins, the verified-plugin program, unmaintained-plugin rot, child-bridge isolation (their answer to our RESERVED_SUBPROCESS question).
- **openHAB**: bindings/add-ons + marketplace history (an older, cautionary marketplace arc).
- **Hubitat, ESPHome, Node-RED** (lighter passes): Hubitat's app/driver code model; ESPHome config-as-data extensibility; Node-RED palette dynamics.
- **Matter** ecosystem trajectory only as it bears on plugin/bridge strategy (the currency research already ruled the V1 deferral — do not relitigate).
**Adjacent best-in-class (trust/marketplace mechanics we should steal):**
- **VS Code extensions**: manifest/permission model, marketplace signing + verification, the extension-host process-isolation architecture (directly informs our subprocess seam).
- **Browser extensions (Chrome MV2→MV3)**: permission manifests, review pipelines, a second famous breaking-migration case study.
- One deliberate wildcard of your choosing (e.g., Obsidian, Minecraft modding, Raycast) if it sharpens a specific Doc-18 question — justify the inclusion.
**Cross-cutting questions the charter must answer from this evidence:** What makes third-party ecosystems trustworthy (signing? review? permissions? tiers?)? What versioning/deprecation policies actually held communities together (→ AX-7)? Where is the in-process/out-of-process isolation line drawn and at what cost? How do data-driven extension models (converters, profiles) govern quality at scale? What licensing/commercial coexistence models worked for Apache-2.0-class cores? What namespace/identity governance prevents type-collision chaos? What do marketplaces need at MINIMUM viable trust?

**Discipline:** every claim tagged **VERIFIED** (source + access date + where it says it) / **INFERRED** (from what) / **UNVERIFIED** (why it stays in). Prefer primary sources (docs, ADRs, changelogs, post-mortems, maintainer statements) over blog folklore. Unfetchable/paywalled → UNVERIFIED, never guessed.

## §4 Fixed constraints (NOT yours to relitigate)

The six-battlefields anti-breadth wedge · local-first (cloud additive, never required) · Doc 18 BUILDS NOTHING (reserves seams; V1 scope untouchable) · the invariants and LTDs stand (LTD-16/17 amendable only by the recorded process — your charter may PROPOSE the amendment shape, not assume it) · AIOT-INV-1 + INV-SA-01..04 bound any AI/component interplay · free-tier posture is Nick's (R-C: evidence the market patterns, flag the tension, do not rule) · the frozen SPI is the plugin contract's starting point, not a redesign surface.

## §5 Deliverables (exactly two files + a note)

1. **`context/assessments/2026-07-0X_plugin-ecosystem-wars_research-dossier.md`** (≤ ~8 K words): per-platform findings (model · mechanics · versioning · community · failure · brilliant idea), the cross-cutting answers, and a distilled "lessons ledger" (numbered L-1..L-n, each one sentence + evidence pointer) the charter cites by number.
2. **`context/planning/2026-07-0X_Doc-18_requirements-charter.md`** (≤ ~3 K words): proposed Doc-18 section map (Doc-17 mold) with per-section content requirements each citing lessons L-n + assessment-§2 gaps; **invariant candidates** (named, one-line, AIOT-INV-1 style); the **reservation list** finalized (dynamic loading / operation registry / event-manifest layering / trust-boundary ladder / namespace-identity governance / packaging-distribution / marketplace-minimum-trust); **decision points for Nick** marked BLOCKING/NON-BLOCKING — AX-7 framed with the market versioning evidence, R-C framed with the market monetization evidence, the isolation-line recommendation; and an honest "what Doc 18 should NOT attempt" section.
3. Cross-agent note (short) + staged commit message in `_scratch/` carrying the env-model §10 audit (exact path count; all .md).

## §6 Session mechanics

File tools for all writes (host-side authoritative); lock-free git reads only (`git --no-optional-locks status --porcelain`, `git log`); NO commits (Nick commits host-side); no writes outside §5's files. Web via the sanctioned search/fetch tools only. If the session saturates mid-arc: capture state in the dossier file (partial, marked DRAFT), note the resume point in the cross-agent note, and close cleanly — a marked-partial return beats an unmarked-confident one.

## §7 Done-when

Both deliverables filed at final status · every load-bearing claim tagged per §3's discipline · the charter's every requirement traces to a lesson or an assessment gap · AX-7 + R-C + the isolation line each carry a framed decision point with a recommendation · the §10-audited commit prep staged · the return routes to the PM hub for two-layer audit before anything folds into Doc 18 authoring.
