<!--
file: context/assessments/2026-07-02_extensibility-and-plugin-ecosystem_PM-assessment.md
purpose: PM assessment answering Nick's strategic question (2026-07-02): is HomeSynapse Core built so that (a) integration breadth scales easily, (b) V1 stays leverageable with hardware/software advances, (c) the system can foster a plugin community/ecosystem, (d) we can dominate on software implementation + AI integration + plugin capability?
audience: Nick (rulings R-A/R-B/R-C), PM (binding obligations), future doc-18 author.
state-type: assessment (PM synthesis over two source-grounded surveys).
status: FILED 2026-07-02 (v14 hub, beat 52). Evidence base: two read-only survey agents over core HEAD ec2e3b4 + the docs/hivemind repos; every load-bearing claim carries a file/section pointer (re-derivable).
method: grounding-subagent-before-authoring — Survey A (code seams, 46 tool calls) + Survey B (strategy/governance alignment, 39 tool calls); hub synthesis + spot-checks. Maintenance-intensity verification posture.
-->

# Extensibility & Plugin-Ecosystem Assessment (V1 trajectory vs the dominance ambition)

## §0 Verdict summary

**D1 — Integration breadth: YES, by architecture.** The adapter SPI is a 2-type, ~6-method, frozen (AMD-54..64), self-contained contract with shipped test fixtures; the device/capability/confirmation models are genuinely protocol-agnostic; breadth strategy is breadth-by-data (D5 converter-corpus ingestion + the bench onboarding pipeline), which scales without per-device code. Named caveats bind at M9.3 (§3).

**D2 — AI/AIoT leverage: THE SUBSTRATE IS THE MOAT.** Immutable replayable log with provenance + causal chains + pure-projection explanations (INV-SA-03) + the confirmation ledger (honest confirmed/unconfirmed actuation labels — unaddressed on every platform surveyed) + `DRY_RUN` in the vocabulary + the AI-safety frame (AIOT-INV-1: AI proposes, the deterministic engine disposes; INV-AI-01..05). "Local-first, cloud, and AI are the same log read differently" is built and CI-enforced, not aspirational.

**D3 — Plugin ecosystem: NOT YET — and this is the one honest gap.** Today "plugin" means "recompile the app": static composition is triple-enforced (DECIDE-04 + LTD-16/17 + ArchUnit NO_SERVICE_LOADER), the highest-value extension surfaces are sealed or reserved-empty, and the third-party trust boundary exists on paper only. Crucially, the architecture did NOT preclude plugins — it reserved the right seams (RESERVED_SUBPROCESS, InvokeIntegrationAction, CustomCapability, per-module event manifests, SchemaRegistry, the amendable-LTD-17 clause) — but "plugins/extensions" is the ONE seam class the non-precluding discipline has never formally reserved, while the strategy layer promises an SDK (months 0–12) and a marketplace (12–24) with zero governance footprint.

**D4 — Longevity/scalability: YES, with named dependencies.** Event-sourced core + JPMS boundaries + freeze/CI discipline + deterministic replay is the survivable shape; local-first removes cloud-API rot; Apache 2.0 was chosen expressly so community and commercial integrations coexist. Watch items: AX-7 (unresolved, gates both community components AND AI-as-author), SPIKE-DC (dual-coordinator, no field precedent), GraalVM/FFM spikes, Matter/Thread seams (correctly reserved-not-built per the 2026-06-27 ecosystem research).

**Bottom line:** the foundation genuinely supports the ambition — the log substrate, the frozen SPI, the confirmation moat, and the AI-safety frame are real, enforced, and differentiated. What is missing is not architecture but a GOVERNED RESERVATION of the third-party seam class plus a bridge plan from curated-Wave-1 to the strategy's "fifty rock-solid + community wave." Reserving that seam is cheap now and expensive after M9.3/M14 freeze more surfaces.

## §1 What is built for it (evidence, telegraphic)

- SPI: `IntegrationFactory` (2 methods) + `IntegrationAdapter` (4 mandatory + 4 default AMD-55 hooks) + optional `CommandHandler`; one `requires com.homesynapse.integration`; testFixtures shipped (`StubIntegrationContext`/`TestAdapter`). Frozen M4.C.
- Hosting: per-adapter supervise thread (VT/platform by IoType) + single-thread command executor; INV-RF-01 classification; descriptor-driven backoff; 30 s bounded boot (a hanging integration never blocks start).
- Protocol-agnostic core: `HardwareIdentifier(namespace, value)` open namespaces; `ConfirmationPolicy` × `Expectation` expressed purely in attribute-report terms (any reporting protocol confirms; DISABLED = honest unconfirmable); all ZCL/Tuya/Xiaomi confined to `integration-zigbee`.
- Per-integration config scoping LIVE (`ConfigurationAccess.scoped`, M9.1); secrets AES-256-GCM with runtime rotation seam; deterministic integration identity (DP-B ruled: permanent policy).
- AI substrate: `EventStore.readByCorrelation/...` + `EventOrigin`/`actorRef` provenance; `ExplanationService` pure log projections; `PendingCommandLedger` = labeled actuation ground truth; INV-ES-09 replay purity pinned at every acting subscriber; privacy scopes encrypted-from-genesis (consent-scoped shredding architectural).
- Breadth-by-data: D5 ratified (adapt-the-data; Z2M corpus → HomeSynapse-owned IR; licenses pinned at ingest); bench = repeatable device-onboarding pipeline; Zigbee profile user-override JSON channel already proves data-extensibility.

## §2 The plugin-ecosystem gap (honest inventory)

Closed/unenforced today: dynamic loading (triple-banned; amendable by written intent in `IntegrationFactory` javadoc); sealed automation hierarchies (the designed seam `InvokeIntegrationAction` is an empty reserved record awaiting an "integration operation registry"); event vocabulary governance-closed behind the hardcoded 3-manifest composition-root aggregation (the per-module manifest pattern would layer; the aggregation point is the single gate); REST/UI routes hardcoded, contract frozen; `CustomCapability`/`CapabilityRegistry` specified, no impl; `SchemaRegistry.registerIntegrationSchema` built but never wired (plugin config rides unvalidated); `EntityType` closed 6-enum (THERMOSTAT/LOCK/COVER need core edits); one-instance-per-type (no second MQTT broker) with no type-namespace governance; adapters cannot subscribe to events (blocks reactive plugins AND AI-as-device-intelligence).
Trust boundary paper-only: unscoped `EntityRegistry`/`StateQueryService` injected (LTD-17 isolation unenforced); full `EventPublisher` (permitted-publish-types check unbuilt); in-JVM-only isolation (RESERVED_SUBPROCESS rejected per AMD-63-INV-01 — the seam is designed, deferred); INV-RF-02 quotas unimplemented.
Strategy/governance misalignments (Survey B §8): SDK+marketplace promised with zero governance footprint; AX-7 unresolved though M7.2b froze the action model; Connect paywall lists "community integration repository access" vs the free-tier-fully-functional non-negotiable (unrevisited); the day-one non-precluding directive lives only in rotating hub prompts; DP-B/DP-C/DP-D one-liners ruled but not landed; strategic-context-map 5 weeks stale.

## §3 Non-preclusion watchlist — surfaces that bind NOW

1. **M9.3 profile registry (the next Coder-lane freeze):** registry shape must be protocol-namespaced or explicitly Zigbee-scoped-with-a-general-seam-note; keep the third-party-profile data channel (user-override precedent) first-class; do not let `DeviceProfile`'s Zigbee vocabulary become the generic profile contract silently.
2. **Website IA (lane launches after FE-1b):** the strategy's 0–12-month SDK promise needs a public developer/integrations surface (even a truthful "SDK maturing — the adapter contract is frozen and documented" posture); integration claims match shipped truth at publish.
3. **M9.2 identity binding:** DP-B ruled permanent — land the governance one-liner (with DP-C/DP-D subset recordings) at the next docs pass BEFORE device adoption makes identity one-way; adopt a type-string namespace convention at the same time (plugin naming governance keys on it).
4. **AX-7 (Doc 16 §15-Q2):** the unresolved versioning/deprecation policy gates BOTH shareable community components AND AI-as-author. One ruling, two futures.

## §4 Recommendations (owner-tagged)

- **R-A (Nick ruling):** authorize **Doc 18 — Extension & Plugin Architecture** in the Doc-17 mold (builds nothing; reserves the third-party seam class formally): names the frozen SPI as the plugin contract; reserves dynamic loading (JPMS child-ModuleLayer at the composition root, gated on the LTD-17 amendment + security evaluation the javadoc already anticipates); reserves the integration operation registry (fills `InvokeIntegrationAction`); makes the event-class aggregation layerable (per-module manifests join at a governed gate); reserves the trust-boundary ladder (scoped context wrappers → publish permissions → INV-RF-02 quotas → RESERVED_SUBPROCESS); adopts type-namespace/ownership governance; mints 1–2 non-preclusion invariants (AIOT-INV-1 style). Timing: post-M9.2, before M9.3 freezes the profile registry. PM authors on your word.
- **R-B (Nick ruling):** resolve **AX-7** (component version/deprecation/compat policy) — highest-leverage single ruling for the community+AI future.
- **R-C (Nick strategy call, flag only):** the Connect "community integration repository access" paywall line vs the free-tier non-negotiable — revisit before any public pricing page.
- **R-1 (PM, next docs pass):** land the DP-B permanence + DP-C/DP-D V1-subset one-liners (ecosystem-keyed records); refresh strategic-context-map currency.
- **R-2 (PM, M9.3 authoring):** fold watchlist item 1 into the M9.3 instruction's design constraints.
- **R-3 (PM, website lane prompt):** developer/integrations page stub in the IA (watchlist item 2).
- **R-4 (backlog, FUTURE rows — name them now so they are never forgotten):** scoped context wrappers (LTD-17 enforcement) · adapter publish-permission enforcement · adapter subscribe/read seam (unlocks reactive plugins + AI-as-device-intelligence) · INV-RF-02 quotas · RESERVED_SUBPROCESS implementation · `CapabilityRegistry` impl + `EntityType` opening strategy · multi-instance-per-type.
- **R-5 (verification, post-M9):** audit the Data Readiness Specification's MVP obligations against the invariants register/backlog — "the event log is the training dataset" must be governance-verified, not asserted.

## §5 Provenance

Survey A (code seams, core `ec2e3b4`): SPI/hosting/isolation/composition/extension-matrix/device-generality/config-identity/AI-substrate + 10 gaps — agent ab982e9d6b64d7da6, 46 tool calls. Survey B (strategy+governance): wedge/AIoT-doctrine/Doc-16-seams/non-precluding-instances/ecosystem-research/deferred-seams/DP-B-verbatim + 5 misalignments — agent a5977e49dd63812b2, 39 tool calls. Hub synthesis: v14 beat 52. Full evidence pointers inline in the survey returns (session-recorded) and re-derivable from the cited paths.
