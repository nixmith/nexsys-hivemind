<!--
file: context/assessments/2026-05-22_Research_5_PM_Assessment.md
purpose: PM assessment of Research 5 (Configuration System Patterns for Constrained IoT Runtimes) — dispositions, modifications, source-verified §7 issues, decision questions for Nick.
audience: PM, Nick
state-type: current
status: v2 (post Nick review — 5 PM-missed/under-traced items corrected; FINAL verdicts in §v2 Addendum at bottom; v1 body preserved for traceability)
last-verified: 2026-05-22 (v2 addendum at bottom)
-->

# Research 5 — PM Assessment (v2 — post Nick review)

**v2 note (2026-05-22, later in same day):** Nick reviewed the v1 assessment and surfaced 5 factual corrections, three of which I missed entirely (F3 `.internal` sub-package fabrication, F4 broken generic on records, F5 should-have-cited INV-CE-01) and two of which I caught the symptom of but didn't trace back to the canonical source (F1: LTD-09 already locks the library *choice* itself — `snakeyaml-engine` and `networknt/json-schema-validator` are not new dependencies needing AMD-64/AMD-65 for adoption; only Phase 3 wiring needs AMD coverage. F2: Jackson 2.x lock is already locked by LTD-08, not just "PM recommendation"). The v1 disposition table below is partially superseded; **the v2 Addendum at the bottom contains the FINAL verdicts**. v1 body retained for traceability. NQ-1..6 are mostly resolved by Nick's review (LTD lookups, INV-CE-01 citation, and the corrected listener shape close most of them) — see §v2 NQ resolution.

---

# Research 5 — PM Assessment (v1 — pre Nick review)

**Date:** 2026-05-22
**Document:** Research 5: Configuration System Patterns for Constrained IoT Runtimes
**RECs assessed:** REC-53 through REC-61 (9 total)
**AMDs proposed by researcher:** AMD-64 through AMD-71 (8 candidates)
**Researcher:** Claude Project
**Protocol:** 6-step A–F processing per PM research pipeline
**Verification base:** `config/configuration/MODULE_CONTEXT.md` + verbatim `module-info.java`, `homesynapse-core/gradle/libs.versions.toml` (at HEAD `76288af`), Doc 06 §§3.3/3.4/3.6/3.7/8.4/8.5/8.6, Research 6 v1 NQ-1/NQ-2 + F1-F8 catalogue, Research 4 v3 AMD-52 (event flat-package precedent), Research 8 v2 REC-28 (DispatchingProjectionAdvancer).

---

## Headline

**Grade: A-. Cleanest research document of the 6-document batch. Researcher discipline visibly improved across all dimensions Research 6 v1 flagged.**

§5.4 explicitly enumerates conflicts with the verified MODULE_CONTEXT inventory and resolves them against the inventory's authority (`ConfigurationValidationException` stays in `com.homesynapse.event`; `schemaVersion` shape change handled as a proposed AMD, not a silent contradiction). §5.1 self-flags the SnakeYAML Engine `org.snakeyaml.engine` module name as inferred-not-verbatim. §3.3 over-abstraction analysis distinguishes DEFENSE from RETRACTION CANDIDATE per claim. The package-name fabrication pattern (Research 3/8) and JPMS-module-name fabrication pattern (Research 6) are both absent. Type-level fabrications are absent.

**The §7 issues that remain are all MODIFY-level, not fabrications:** two are oversights the researcher would have caught with one additional verified input (`libs.versions.toml` for REC-53/REC-54 version state), one is an implicit interface extension that needs explicit AMD coverage (REC-57's `ConfigurationAccess#credentialsFor`), one is an event-package omission that AMD-52 precedent resolves (REC-59's `config.validation_completed` package landing).

§1–§6 quality is the best of the batch. Executive summary verdicts are all defensible. Platform deep dives all carry verbatim primary-source quotes with URLs (Spring Cloud Commons #846, HA developers docs verbatim, networknt pom.xml moditect block, Jackson 3.0 wiki, OpenHAB PR #3330 reviewer comment, Kura Javadoc verbatim). §3.4 competitive assessment explicitly retracts two claims that don't survive scrutiny.

---

## Disposition Table

| REC | Title | Disposition | Target | AMD | Risk | v1 notes |
|---|---|---|---|---|---|---|
| REC-53 | SnakeYAML Engine 3.0.1 as YAML 1.2 parser | **ACCEPT (MODIFY)** | M6 | AMD-64 (downgrade to version-bump scope) | LOW | **`snakeyaml-engine` 2.9 already integrated** in `libs.versions.toml` (line 18). 2.9 already satisfies Doc 06's YAML 1.2 requirement (the engine line has always been YAML 1.2 — that is what distinguishes it from classic SnakeYAML). REC's substantive case is therefore version-bump 2.9 → 3.0.1, not new dependency. AMD-64 should be re-scoped accordingly. The safe-by-default / no-Jackson-transitive arguments still stand. |
| REC-54 | `com.networknt:json-schema-validator` 3.0.2 | **ACCEPT (MODIFY — stay on 1.5.6)** | M6 | AMD-65 (downgrade to "Phase 3 implementation only", no version change) | LOW-MEDIUM | **`json-schema-validator` 1.5.6 already integrated** in `libs.versions.toml` (line 27). The researcher correctly flagged in §5.1 that v3.x requires Jackson 3.x; HomeSynapse Jackson is **2.18.6** (verified in libs.versions.toml line 16; LTD-19 floor 2.18.4). networknt 1.5.x is the supported line for Jackson 2.x. **Stay on 1.5.6.** Phase 3 implementation work (composition, error mapping) proceeds as REC-54 specifies; the dependency version stays put. Migration to networknt 3.x is coupled to the eventual Jackson 2→3 migration and explicitly out of Research 5 scope. |
| REC-55 | `ConfigurationChangeListener<S>` sealed-typed interface | **ACCEPT** | M6 | AMD-66 | LOW | Sealed-with-non-sealed-permits design is defensible — `Hot<S>` / `RequiresRestart<S>` markers enable type-system enforcement while permitting downstream subsystem implementations. Method returns `ReloadClassification` (3-value enum, verified) — reconciles cleanly with existing `ConfigChangeSet.reload: ReloadClassification` field. Synchronous-before-publish contract matches Doc 06 §3.3. Listener key `sectionPath()` matches existing `ConfigSection.path` shape. See NQ-3 for whether the sealed-marker complexity is worth the type-system enforcement vs a plain non-sealed interface relying on the return-value dynamic. |
| REC-56 | `ConfigMigrator` → `(major, minor)` pairs; `ConfigModel` 5 → 6 fields | **ACCEPT** | M6 | AMD-67 | MEDIUM | **Reconciles directly with Research 6 REC-41 (`migrate(fromMajor, fromMinor, toMajor, toMinor, IntegrationConfig)`) and Research 6 NQ-2 (PM recommended "introduce `configSchemaMajor` + `configSchemaMinor` alongside the existing single int").** Researcher chose the cleaner option (b — both shapes become `(major, minor)`), not NQ-2's hedge — and the case for cleanliness over hedging is correct (matching adapter migration semantics removes a conceptual seam). The existing interface has 3 methods → 5 methods after the change; no production `ConfigMigrator` implementations exist yet per the verified MODULE_CONTEXT Phase 3 Notes, so the breaking change has zero downstream blast radius. `ConfigModel` 5 → 6 fields (replace `schemaVersion: int` with `configSchemaMajor: int` + `configSchemaMinor: int`) is internal-only — `ConfigModel` is consumed only inside `com.homesynapse.config`. |
| REC-57 | `SecureCredentialBundle` as layered record over `SecretStore` | **ACCEPT (MODIFY)** | M6 | AMD-68 (expand to cover `ConfigurationAccess.credentialsFor(String)` method addition) | MEDIUM | Composition (not replacement) of `SecretStore` is correct. Per-integration scoping via `integration.<id>.*` key prefix aligns with Research 6 REC-45 PM recommendation (NQ-1 — aggregator pattern) and with how `IntegrationContext` already routes per-adapter access. **§7.2 implicitly adds `ConfigurationAccess#credentialsFor(String integrationId)` as a new interface method** — the existing `ConfigurationAccess` has exactly 4 methods (`getConfig`, `getString`, `getInt`, `getBoolean`) per verified inventory. AMD-68 must explicitly cover the interface extension (record + method), not just the record. |
| REC-58 | Argon2id KDF with RFC 9106 §4 "SECOND RECOMMENDED" parameters | **ACCEPT** | M6 | AMD-69 | MEDIUM | Parameter choice is RFC-defended (verbatim §4 second-recommended for memory-constrained environments). Spike Q2 (Pi 4 derivation timing 250–700 ms) blocks merge — acceptable budget for one-time startup derivation. BouncyCastle dependency choice is a Phase 3 implementation detail; see NQ-2 for whether to commit to BC vs leave the JCE-provider selection open. Threat model (§7.9) is the strongest defended threat-model statement of any research document so far — T1/T2 in-scope with specific defenses; T3 (on-device root + `/proc/<pid>/mem`) explicitly out-of-scope with TPM2 hardware reality cited. |
| REC-59 | `config.validation_completed` + `config.section_reloaded` events | **ACCEPT (MODIFY)** | M6 | AMD-70 | LOW-MEDIUM | Dot-namespaced naming correct. Observability-only classification correct. ProjectionEventHandler registration via Research 8 REC-28's `DispatchingProjectionAdvancer` correct (REC-28 lands M4.0, REC-59 implementation lands M6 — sequencing checks out). **§7.6 omits the package landing.** Per AMD-52 (Research 4 v3) precedent, new domain event types land in `com.homesynapse.event` (flat package), not in `com.homesynapse.config`. The legacy `config_changed` / `secret_added` / `secret_removed` events also live in event-model (consistent with AMD-52). Make AMD-70 explicit on this. |
| REC-60 | Hybrid directory layout (root + `integrations/` subdir + `secrets.yaml.enc` + `schemas/` cache) | **ACCEPT** | M6 | AMD-71 | LOW | Clean design. One-level-deep `!include` is the right hedge against HA's chained-include footguns. `SchemaRegistry` composition timing (compose-after-merge) matches the existing JSON-text-String parameter contract — no library-type leakage. Path-traversal protection called out (good — that's the kind of detail Research 6 missed). |
| REC-61 | `config.section_reloaded` carries `ReloadResult` breakdown | **ACCEPT** | M6 | (none — covered by AMD-70) | LOW | Pure additive consumption of existing `ReloadResult` (3 fields: `newModel`, `changeSet`, `issues`); does not modify the record. Clean. |

**Summary: 5 ACCEPT, 4 ACCEPT+MODIFY, 0 REJECT. 8 AMDs ratifiable (AMD-64 through AMD-71), all subject to the modifications noted above.**

---

## §7 Source-Verified Issues (Fabrication Catalogue — Research 5)

Research 5 is the cleanest research document of the batch. The "F1-F8" catalogue pattern produced 8 module-name fabrications in Research 6 and ~29 type-name errors in Research 4. Research 5 produced **zero verifiable fabrications**. The issues below are §7 MODIFY-level — omissions, implicit-not-explicit changes, or version-state oversights — not fabrications.

| # | Researcher wrote | Verified actual value | Affects | Severity |
|---|---|---|---|---|
| F1 | "Add Maven dependency `org.snakeyaml:snakeyaml-engine:3.0.1`" framed as new dependency (REC-53) | **Already present** at `libs.versions.toml:18` as `snakeyaml-engine = "2.9"`. Version 2.9 already satisfies Doc 06's YAML 1.2 requirement (the entire engine line is YAML 1.2). | REC-53, AMD-64 scope | LOW (re-scope AMD as version-bump 2.9 → 3.0.1, not new-dependency adoption) |
| F2 | "Add `com.networknt:json-schema-validator:3.0.2`" framed as new dependency (REC-54) | **Already present** at `libs.versions.toml:27` as `json-schema-validator = "1.5.6"`. The Jackson coordination hazard the researcher correctly flagged in §5.1 resolves cleanly: HomeSynapse Jackson is **2.18.6** (line 16; LTD-19 floor 2.18.4) → networknt must stay on the 1.5.x or 2.x line. **Stay on 1.5.6.** | REC-54, AMD-65 scope | MEDIUM (no version change; Phase 3 implementation work proceeds as specified — composition, error mapping, validator-bridge) |
| F3 | `ConfigurationAccess#credentialsFor(String integrationId)` referenced in §7.2 as if it exists | Existing `ConfigurationAccess` interface has exactly 4 methods (`getConfig`, `getString`, `getInt`, `getBoolean`) per verified MODULE_CONTEXT. REC-57 implicitly adds a 5th method but §7.2 does not explicitly call out the interface extension. | REC-57, AMD-68 scope | MEDIUM (AMD-68 must explicitly cover record + interface method, not just record) |
| F4 | §7.6 specifies new event types `config.validation_completed` + `config.section_reloaded` but omits the package | Per AMD-52 precedent (Research 4 v3), domain event records land in `com.homesynapse.event` (flat package). Legacy `config_changed` / `secret_added` / `secret_removed` events also live there. | REC-59, AMD-70 scope | LOW (make explicit in AMD-70; package landing is `com.homesynapse.event`) |
| F5 | "Module name `org.snakeyaml.engine` (Multi-Release, Java 11+)" — REC-53 §7.4 | Researcher self-flagged in §5.1 as inferred from OSGi metadata, not verbatim-verified against a packaged MANIFEST.MF. | REC-53 / `module-info.java` directive `requires org.snakeyaml.engine;` | LOW (Coder must verify against the actual 2.9 → 3.0.1 jar before merging the `module-info.java` change; fallback to `Bundle-SymbolicName`-derived name if needed) |

**No type-name fabrications. No package-name fabrications. No `module-info.java` JPMS-module-name fabrications (the one inferred name is self-flagged).** F1/F2 are version-state misses; F3 is an implicit-not-explicit interface change; F4 is a §7 omission resolved by AMD-52 precedent; F5 is a self-flagged inference.

---

## Open Questions for Nick (NQ-1 through NQ-6)

| # | Question | PM recommendation |
|---|---|---|
| NQ-1 | **Jackson 2→3 migration sequencing.** REC-54's researcher-preferred networknt 3.0.2 requires Jackson 3.x. HomeSynapse Jackson is 2.18.6. Stay on networknt 1.5.6 (Jackson 2.x) for M6, or couple a Jackson 2→3 migration with M6? | **Stay on 1.5.6.** Jackson 2→3 is a cross-cutting migration affecting LTD-19 (event payload serialization), persistence (`PersistenceObjectMapper`), state-store (`CheckpointSerializer`), rest-api (`EndpointResponses`), and every test using `ObjectMapper`. It deserves its own dedicated WU and its own assessment — not a coupling to Research 5. The networknt 1.5.x line will receive maintenance updates and is production-grade. |
| NQ-2 | **REC-58 BouncyCastle vs JCE-native Argon2id.** Researcher proposes BouncyCastle (`org.bouncycastle:bcprov-jdk18on`, ~5 MB jar, large API surface). Java 21 does not include native Argon2id in `java.security` providers. Alternative: pure-Java port (smaller, less battle-tested). | **Commit to BouncyCastle in AMD-69 with Phase 3 implementation freedom to substitute.** BC is the production-validated path; the jar size is acceptable for a Pi 4/5 runtime. Spike Q2 (Pi 4 wall-clock 250–700 ms) blocks merge regardless. If the spike reveals BC's Argon2id implementation is too slow on Cortex-A72, Phase 3 can substitute (e.g., phc-winner-argon2 Java port) without re-issuing AMD-69 — the AMD specifies the algorithm and parameters, not the provider. |
| NQ-3 | **REC-55 sealed-marker pattern vs plain interface.** Proposed: `sealed interface ConfigurationChangeListener<S> permits Hot, RequiresRestart` where `Hot`/`RequiresRestart` are `non-sealed` markers. Alternative: plain `interface ConfigurationChangeListener<S>` with the `ReloadClassification` return value being the only differentiator. | **Adopt the sealed-marker pattern as proposed.** The type-system enforcement is non-trivial — a `Hot` listener that returns `INTEGRATION_RESTART` is a programming error that the marker can flag at the registration site. The `non-sealed` workaround correctly admits downstream-module implementations without forcing them to be `permits` members of `com.homesynapse.config`'s sealed declaration. Cost is small (two marker interfaces, zero behavioral code); benefit is permanent type-level documentation of intent. |
| NQ-4 | **REC-57 `ConfigurationAccess` interface extension scope.** `credentialsFor(String integrationId)` extends the existing interface (verified 4 methods → 5 methods). Should the extension live on `ConfigurationAccess` directly, or on a separate `CredentialAccess` interface composed alongside it? | **Extend `ConfigurationAccess` directly.** It is already the integration-scoped read interface (verified MODULE_CONTEXT: "Read-only, integration-scoped configuration access"). Splitting credentials into a separate interface adds a coupling point in `IntegrationContext` without conceptual benefit — both are read-only integration-scoped views of configuration state. The `IntegrationContext`'s existing `configAccess` field continues to provide the entry point. |
| NQ-5 | **REC-59 new config event records — confirm package landing.** §7.6 does not specify; AMD-52 precedent says `com.homesynapse.event` (flat). | **Confirm `com.homesynapse.event`** (flat package, per AMD-52). Update AMD-70 to specify package explicitly. This also keeps `EventTypes.CORE_PRODUCTION_EVENT_CLASSES` as the canonical roster (M3.6c pattern) — new config events get added to the list. |
| NQ-6 | **Spike Q1/Q2/Q3 sequencing.** Three pre-merge spikes blocking REC-53 / REC-54 / REC-58. All require Pi 4/5 hardware. Run before any M6 coding instruction, run during M6 in parallel with Phase 3 implementation, or run only when each REC is about to land? | **Run Q1 (SnakeYAML Engine throughput) and Q3 (networknt memory residency) before the M6 coding instruction is issued** — these inform the Phase 3 design (e.g., schema-cache strategy, parser-reuse pattern). **Defer Q2 (Argon2id) until immediately before REC-58 implementation** — the secrets path is the last M6 increment and has the most flexibility on KDF parameter tuning if the budget is overrun. Hardware: dev Pi 5 (`hs-dev-1`) per the established M3.4b validation pattern. |

---

## §1–§6 Strengths (kept for the record)

- **§1 verdict 3 correctly identifies the single highest-impact finding** (config-as-event vs config-as-file tension) and resolves it the right way: file is source of truth, events are observability. The HA `.storage/` opacity argument is the load-bearing defense.
- **§2.1 HA, §2.2 OpenHAB, §2.3 Kura, §2.4 Spring** all carry verbatim primary-source quotes with URLs. §2.4 specifically cites Spring Cloud Commons issue #846 (record-based `@ConfigurationProperties` cannot refresh) — directly disqualifying Spring's proxy approach for HomeSynapse's record-first codebase. The quality here is materially better than Research 6's §2.
- **§2.7 networknt** verifies the JPMS module name verbatim from the pom.xml moditect block (`com.networknt.schema`). This is exactly the discipline Research 6 v1 lacked when it fabricated F1–F5 module names.
- **§3.1 concept-mapping table** is the strongest single artifact in the document. 9 rows × 6 platforms; every cell is substantive. Rivals Research 2 §3.1 as the gold standard.
- **§3.3 over-abstraction analysis** annotates each item with DEFENSE or RETRACTION CANDIDATE — only the third research document to apply this self-critical posture (Research 2 and Research 6 did similarly; Research 4 and Research 8 did not).
- **§3.4 competitive assessment** explicitly retracts two claims ("First Java smart-home runtime with JSON Schema validation" — too strong; "Only platform with secrets encryption" — too strong). This is exactly the calibration Research 6 §3.4 attempted but Research 5 executes more rigorously.
- **§5.4 conflict-with-inventory disclosure** is the discipline Research 6 v1 lacked. Two conflicts explicitly listed, both resolved against the inventory's authority. This is the model for future research documents.
- **§7.9 threat-model statement** is the strongest of any research document so far. T1/T2 defended with specific cryptographic primitives + RFC citations; T3 explicitly out-of-scope with the TPM2-on-Pi-4-absent hardware reality cited; T4/T5 explicitly listed as out-of-scope. This is what the Research 5 brief §8 deliverable asked for and the only research document that has produced one.

---

## §1–§6 Weaknesses

- **REC-53 / REC-54 missed the `libs.versions.toml` integration state.** The brief embedded LTD-19 (Jackson 2.18.6 floor) in prose but did not embed `libs.versions.toml` verbatim. The researcher inferred "new dependency" framing where the actual state is "version-bump (or stay)." This is a brief-side gap, not a researcher fabrication — but it propagated into AMD scoping for both RECs. **Lesson for future briefs: embed `libs.versions.toml` verbatim alongside `module-info.java` whenever the research touches dependency choice.**
- **§7.2 `ConfigurationAccess.credentialsFor(String)` interface extension is implicit, not explicit.** REC-57 introduces `SecureCredentialBundle` but the accompanying interface-extension to `ConfigurationAccess` is mentioned only in the method-call reference. AMD-68 must explicitly cover the interface method addition or it gets lost during ratification.
- **§7.6 omits the package landing for new event records.** AMD-52 precedent resolves this (`com.homesynapse.event` flat package), but explicit is better than implicit — AMD-70 should state the package.
- **§5.1 SnakeYAML Engine module name self-flagged as inferred.** Acceptable — but a Phase 3 Coder must verify against the actual 2.9 → 3.0.1 jar's MANIFEST.MF before the `module-info.java` directive `requires org.snakeyaml.engine;` lands. Pre-verification artifact (per the `context/pre-verifications/` convention) recommended for this WU.

---

## M6 Implementation Order

Sequencing for the M6 work, ranked to minimize rework:

1. **Spike Q1 + Spike Q3** (REC-53 + REC-54 prerequisites) — Pi 4 throughput + networknt memory residency. Empirical inputs for the Phase 3 design.
2. **AMD-67** (REC-56 `ConfigMigrator` + `ConfigModel` major/minor) — interface change first; everything downstream depends on the schema-version shape. **Reconciles with Research 6 REC-41 — both must land at the same time** to preserve the (major, minor) adapter-config alignment.
3. **AMD-66** (REC-55 `ConfigurationChangeListener` sealed-typed interface) — public-API addition with the sealed-marker pattern.
4. **AMD-65** (REC-54 networknt Phase 3 implementation, no version change) — `JsonSchemaCompositeValidator` + error-to-`ConfigIssue` mapping + integration-schema-on-install hook. Production `ConfigValidator` implementation.
5. **AMD-64** (REC-53 SnakeYAML Engine — version-bump 2.9 → 3.0.1 *if* 3.0.1 is required for a specific feature; otherwise stay at 2.9). Production `YamlLoader` package-private utility + safe-by-default `LoadSettings`.
6. **AMD-71** (REC-60 hybrid directory layout) — composition wiring with the layout. Path-traversal protection.
7. **Spike Q2** (REC-58 Pi 4 Argon2id timing) — informs final KDF parameters.
8. **AMD-69** (REC-58 Argon2id KDF + BouncyCastle dependency) — secrets persistence path. Threat-model document committed to repo at `doc/secrets-threat-model.md`.
9. **AMD-68** (REC-57 `SecureCredentialBundle` record + `ConfigurationAccess.credentialsFor(String)` interface extension) — depends on AMD-69 secrets infrastructure.
10. **AMD-70** (REC-59 `config.validation_completed` + `config.section_reloaded` events + REC-61 surfacing) — observability layer; depends on all preceding for full payload.

**Reconciliation gate with Research 6:** AMD-67 (REC-56 file-schema major/minor) and Research 6 REC-41 (adapter-config major/minor) must ratify together. If Nick approves NQ-2 of the Research 6 assessment differently (single-int retention) and approves REC-56 here, this is a forced inconsistency to resolve before either lands.

---

## Cross-Research Coherence Check

The three coherence requirements the prompt flagged:

| Surface | Status |
|---|---|
| §Q3 `SecureCredentialBundle` ↔ Research 6 REC-45 `SecurityServices` (NQ-1) | **ALIGNED.** REC-57 layers over existing `SecretStore` (composition, not replacement). Research 6 REC-45's `SecurityServices` aggregator (NQ-1 PM-recommended) routes per-adapter access via `IntegrationContext`. `SecureCredentialBundle` is the per-integration view that the aggregator's `CredentialRotator` operates on. Coherent. |
| §Q6 schema versioning ↔ Research 6 REC-41 (`migrate(fromMajor, fromMinor, toMajor, toMinor, ...)`) + Research 6 NQ-2 | **ALIGNED.** REC-56 changes `ConfigMigrator` to `(fromMajor, fromMinor, toMajor, toMinor, migrate)` — exactly the shape Research 6 REC-41 specifies for adapter migration. The single int → pair change on `ConfigModel.schemaVersion` (5 → 6 fields) carries through. NQ-2 of Research 6 had two options (rename existing field + add pair, or change both); Research 5 chose the cleaner unified option. PM endorses the cleaner option. |
| §Q4 `ConfigurationChangeListener` ↔ existing `ConfigChangeSet.ReloadClassification` field | **ALIGNED.** Listener method returns `ReloadClassification` (3-value enum, verified locked). `ConfigChangeSet.changes: List<ConfigChange>` carries per-change classification. The listener-returned classification is the *aggregated* decision per section; the per-change classifications inside the set are the inputs. Two halves of the same protocol. |

All three coherence checks pass. Research 5 v1 is internally and externally consistent.

---

## Key Insights Internalized

1. **Embedding `libs.versions.toml` in the brief eliminates an entire fabrication class** — the version-state-misses (F1, F2) would not have happened if the brief embedded the relevant catalog rows verbatim alongside the `module-info.java` and MODULE_CONTEXT. Add to research-agenda.md §2 CONSTRAINTS: every brief that touches dependency choice must embed verbatim `libs.versions.toml` rows for the relevant libraries.
2. **Researcher discipline scales with brief discipline.** Research 5 is the cleanest of the batch because the brief was the most thoroughly constrained — verbatim `module-info.java` for the config module *and* for the upstream `com.homesynapse.event` and `com.homesynapse.integration` modules; verbatim 22-type MODULE_CONTEXT inventory; explicit "VERIFIED NON-existent types" list; explicit "VERIFIED upstream constraints (do not propose changes — outside Research 5 scope)" list. The researcher had nowhere to fabricate.
3. **§5.4 conflict-with-inventory disclosure is now the bar.** Research 6 v1 produced 8 source-verified fabrications partly because the brief didn't have a "what to do if you find a contradiction" instruction. Research 5 produced zero in part because §5.4 explicitly gave the researcher a place to surface contradictions rather than silently break the inventory. Adopt this as a research-agenda CONSTRAINTS bullet.
4. **The (major, minor) schema-version pattern is now a system-wide invariant after AMD-67.** Both file-schema (`ConfigModel.configSchemaMajor/Minor`) and adapter-config-schema (Research 6 REC-41) align on `(major, minor)`. Any future research touching schema versioning must use this pair.
5. **The cleanest threat model is one that defines the threats out of scope.** §7.9 explicitly enumerates T3 (on-device root attacker), T4 (cold-boot/DRAM-remanence), T5 (compromised passphrase) as out-of-scope, with hardware-reality citations for T3 specifically. This is the right framing — every cryptographic design that doesn't articulate what it doesn't defend against eventually gets attacked at exactly that surface.
6. **Sealed-with-non-sealed-permits is a legitimate Java pattern for cross-module type-system enforcement.** REC-55's design uses sealed declaration in the defining module + non-sealed markers to admit downstream implementations. This is the Java 17+ idiom for "closed-set of intent categories, open-set of implementations." Worth codifying as a pattern in `pm-lessons.md` for future use.

*Note: v1 lesson #6 above was retracted in v2 — the generic bound `<S extends ConfigSection>` is mechanically broken because `ConfigSection` is a record (implicitly final). See v2 F7 below.*

---

**v1 Assessment completed:** 2026-05-22 by PM (Cowork session).
**v1 Status:** v1 — PM-verified against `config/configuration/MODULE_CONTEXT.md` + verbatim `module-info.java` + `gradle/libs.versions.toml` (at HEAD `76288af`) + Doc 06 §§3.3/3.4/3.6/3.7/8.4/8.5/8.6 + Research 4 v3 / Research 6 v1 / Research 8 v2 cross-research coherence. **Superseded by v2 Addendum below.**

---

## v2 Addendum (2026-05-22 — Post Nick Review)

Nick reviewed v1 and surfaced **five corrections**, all of which I should have caught:

- Three I missed entirely: F6 (`.internal` sub-package fabrication in §7.7 violates the one-flat-package-per-module invariant), F7 (broken generic — `<S extends ConfigSection>` is unsound because `ConfigSection` is a record and records are implicitly final), F8 (INV-CE-01 already canonically answers §Q7 — file is source of truth — making it a constitutional invariant citation, not a research finding).
- Two I caught the symptom of but didn't trace to the canonical source: F1 in v1 catalogue was a version-state miss, but the deeper truth is that **LTD-09 already locks the library *choice* itself** — `snakeyaml-engine` and `networknt/json-schema-validator` are not new dependencies needing AMD-64/AMD-65 for adoption; only Phase 3 wiring needs AMD coverage. F2 same story for networknt; Jackson 2.x lock is itself by LTD-08, which should have been a citation rather than my "PM recommendation" framing in NQ-1.

The v1 disposition table is partially superseded. The FINAL disposition table is below. v1 body retained above for traceability.

### v2 Final Disposition Table

| REC | v1 verdict | v2 FINAL verdict | AMD outcome | Blocker |
|---|---|---|---|---|
| REC-53 | ACCEPT (MODIFY) — version-bump scope | **CONFIRMED.** Library already locked via LTD-09 ("YAML 1.2 (SnakeYAML Engine)"); version 2.9 already in `libs.versions.toml`. No adoption AMD needed. Phase 3 wiring AMD when `module-info.java` gains `requires org.snakeyaml.engine;`. | AMD-64 **RETIRED** for adoption; Phase 3 wiring AMD TBD | Spike Q1 |
| REC-54 | ACCEPT (MODIFY — stay on 1.5.6) | **CONFIRMED.** Library already locked via LTD-09 ("JSON Schema validation (networknt)"); version 1.5.6 already in `libs.versions.toml`. No adoption AMD needed. Phase 3 wiring AMD when `module-info.java` gains `requires com.networknt.schema;`. **`ethlo:itu` exclusion claim must be verified against v1.5.6's actual dependency tree** — may be v3.x-only transitive. | AMD-65 **RETIRED** for adoption; Phase 3 wiring AMD TBD | Spike Q3 |
| REC-55 | ACCEPT (sealed-marker pattern) | **ACCEPTED IN PRINCIPLE — shape corrected.** v1 missed that `<S extends ConfigSection>` is mechanically broken (records are implicitly final and cannot be extended). Corrected shape: plain interface (no generics, no sealed hierarchy), returns `ReloadClassification`. Hot vs RequiresRestart distinction is already conveyed by the return value — encoding it in the type hierarchy adds complexity without utility. Default-to-`INTEGRATION_RESTART` when no listener registered for a section (Kura `@Modified`-absent semantics). | AMD-66 **ACTIVE** with corrected shape | — |
| REC-56 | ACCEPT (with cross-research gate) | **DEFERRED to Nick's REC-41 decision.** PM-recommended option (b — `(major, minor)` for both file and adapter migration) per Research 6 NQ-2; cannot proceed until REC-41's fate is decided. If REC-41 is rejected, single-int can remain. `MigrationPreview` also needs `fromMajor/fromMinor/toMajor/toMinor` if REC-56 proceeds. | AMD-67 **DEFERRED** on Research 6 REC-41 | Research 6 REC-41 decision |
| REC-57 | ACCEPT (MODIFY) — `credentialsFor` on `ConfigurationAccess` | **ACCEPTED with corrections.** v1 wrongly proposed extending `ConfigurationAccess` — that interface is read-only config, not secrets. Integrations already get secrets via `SecretStore.resolve()`. The `credentialsFor(String integrationId)` convenience accessor belongs on **`SecretStore`** (new method) or a factory, not on `ConfigurationAccess`. Composition over replacement, per-integration scoping by `integration.<id>.*` key prefix — both unchanged from v1. | AMD-68 **ACTIVE** with corrected accessor placement (extends `SecretStore`, not `ConfigurationAccess`) | — |
| REC-58 | ACCEPT | **ACCEPTED.** Two-tier threat model (T1 backup/exfil + T2 cross-integration; T3/T4/T5 explicitly out-of-scope) is correctly scoped for Pi 4/5 hardware. RFC 9106 §4 SECOND RECOMMENDED parameters (t=3, p=4, m=2^16) defended. BouncyCastle as JCE provider is standard. `secrets.yaml.enc` envelope with `version` field is forward-looking. **§7.9 threat-model statement is publication-ready** — commit to `docs/secrets-threat-model.md` after correcting the "§4 SECOND RECOMMENDED option" reference to include the full parameter citation. | AMD-69 **ACTIVE** (BouncyCastle dependency) | Spike Q2 |
| REC-59 | ACCEPT (MODIFY) — explicit package landing | **ACCEPTED.** Payload `(schemaMajor, schemaMinor, issues, severityCounts)` is contingent on REC-56 — reverts to single `schemaVersion` if REC-56 doesn't proceed. Observability-only classification correct (does not participate in state derivation). New events need `@EventType` annotations and `EventTypeRegistry` registration (in `EventTypes.CORE_PRODUCTION_EVENT_CLASSES` — the M3.6c manifest pattern). Package landing: `com.homesynapse.event` flat per AMD-52 precedent. | AMD-70 **ACTIVE** (includes REC-61 functionality) | (contingent on REC-56) |
| REC-60 | ACCEPT | **ACCEPTED IN PRINCIPLE; AMD deferred to M6.** Layout (`homesynapse.yaml` root + `integrations/*.yaml` + `secrets.yaml.enc` + `schemas/`) is clean. One-level-deep `!include` restriction is a good simplification. Schema-composition timing (compose-after-merge) and path-traversal protection are correctly identified. **No M4 types depend on this** — defer the AMD filing to M6 planning. | AMD-71 **DEFERRED to M6 planning** | — |
| REC-61 | ACCEPT (additive on REC-59) | **MERGED into REC-59.** Not a separate recommendation — implementation detail of `config.section_reloaded` event payload. v1 correctly noted "covered by AMD-70" but treated it as a distinct row anyway. Drop REC-61 as a separate entry. | (none — folded into AMD-70) | — |

**v2 Summary: 2 CONFIRMED (REC-53/54) / 1 ACCEPTED IN PRINCIPLE — shape corrected (REC-55) / 1 ACCEPTED with correction (REC-57) / 2 ACCEPTED (REC-58/59) / 1 ACCEPTED IN PRINCIPLE — AMD deferred (REC-60) / 1 DEFERRED on cross-research gate (REC-56) / 1 MERGED (REC-61).**

### v2 AMD Allocation

| AMD | Status | Scope |
|---|---|---|
| AMD-64 | **RETIRED** | REC-53 adoption — library already locked via LTD-09 |
| AMD-65 | **RETIRED** | REC-54 adoption — library already locked via LTD-09 |
| AMD-66 | **ACTIVE** | REC-55 `ConfigurationChangeListener` (corrected shape — no generics, no sealed hierarchy) |
| AMD-67 | **DEFERRED** | REC-56 file-schema `(major, minor)` — pending Nick's REC-41 decision |
| AMD-68 | **ACTIVE** | REC-57 `SecureCredentialBundle` record + `SecretStore.credentialsFor(String)` (corrected from `ConfigurationAccess`) |
| AMD-69 | **ACTIVE** | REC-58 Argon2id KDF + BouncyCastle dependency |
| AMD-70 | **ACTIVE** | REC-59 `config.validation_completed` + `config.section_reloaded` events (in `com.homesynapse.event`) |
| AMD-71 | **DEFERRED** | REC-60 directory layout — to M6 planning |
| Phase 3 wiring AMDs | TBD | When `com.homesynapse.config` `module-info.java` gains `requires com.networknt.schema;`, `requires org.snakeyaml.engine;`, `requires org.bouncycastle.provider;` directives |

**Active AMDs: 4 (AMD-66, 68, 69, 70). Deferred: 2 (AMD-67, 71). Retired: 2 (AMD-64, 65). New AMDs start at AMD-72.**

### v2 Fabrication Catalogue Additions (F6, F7, F8)

The v1 catalogue listed F1–F5. Nick's review identified three more researcher errors I missed:

| # | Researcher wrote | Verified actual value | Affects | Severity |
|---|---|---|---|---|
| F6 | §7.7 `module-info.java` comment: `// implementation packages not exported: com.homesynapse.config.internal` | **No `.internal` sub-package exists or should exist.** Every HomeSynapse module uses a single flat package (verified one-flat-package-per-module invariant, Knowledge Primer §Module Map). Package-private classes in `com.homesynapse.config` are already invisible to other modules because JPMS exports control visibility at the type level for non-public types. Implementation classes (`YamlLoader`, `JsonSchemaCompositeValidator`, `Argon2idKeyDerivation`) are package-private in `com.homesynapse.config`, not in a sub-package. | REC-53 / REC-54 / REC-58 implementation placement | MEDIUM (would create a real fabrication if Coder followed §7.7 verbatim) |
| F7 | `public sealed interface ConfigurationChangeListener<S extends ConfigSection> permits Hot, RequiresRestart` in §7.1 | **`ConfigSection` is a record (3 fields: `path`, `values`, `defaults`), and records are implicitly `final`.** The generic bound `<S extends ConfigSection>` is mechanically unsound — no type can extend a record. The sealed-with-non-sealed-permits pattern compounds the issue: `Hot<S>` and `RequiresRestart<S>` carry the same broken bound. Corrected shape: plain non-generic interface receiving `ConfigSection` directly for the section it's registered on. | REC-55, AMD-66 | HIGH (cannot compile as proposed) |
| F8 | §7.3 frames the file-vs-event source-of-truth choice as a research finding ("The single highest-impact finding is the config-as-event vs config-as-file tension"); §1 verdict 3 presents it as a derived conclusion | **INV-CE-01 already canonically answers this:** "The configuration file is the sole source of truth. ConfigModel is always derived from the YAML file on disk. No runtime state modifies configuration outside the write path." This is an architecture invariant, not a recommendation. The platform survey is good *supporting evidence* for INV-CE-01, but the answer was never in question. | §1 verdict 3 framing | LOW (the researcher's conclusion is correct — the framing is wrong) |

**Updated catalogue total: 5 (v1) + 3 (v2) = 8 §7 issues. Still zero type-name fabrications and zero JPMS-module-name fabrications in the Research 6 sense. F6 is a real fabrication (would propagate to code if uncaught); F7 is a Java mechanics error; F8 is a citation/framing error.**

### v2 NQ Resolution

All 6 NQs from v1 are now resolved by Nick's review:

| # | v1 question | v2 resolution |
|---|---|---|
| NQ-1 | Jackson 2→3 migration sequencing | **RESOLVED by LTD-08.** Jackson 2.x is locked; networknt 1.5.6 stays. Jackson 2→3 is a separate cross-cutting migration explicitly out of Research 5 scope. |
| NQ-2 | BouncyCastle commitment for Argon2id | **RESOLVED.** BC is the standard JCE provider for Argon2id; AMD-69 commits to BC with Phase 3 substitution freedom if Spike Q2 reveals performance issues. |
| NQ-3 | Sealed-marker vs plain interface for `ConfigurationChangeListener` | **RESOLVED by F7.** The generic bound was mechanically broken regardless of the sealed pattern question. Corrected shape: plain non-generic interface. |
| NQ-4 | `ConfigurationAccess` extension scope for `credentialsFor` | **RESOLVED — corrected to `SecretStore`.** `ConfigurationAccess` is config-only, not secrets. `SecretStore.credentialsFor(String integrationId)` is the right home. |
| NQ-5 | New config events package landing | **RESOLVED — `com.homesynapse.event`** per AMD-52 precedent. Also register in `EventTypes.CORE_PRODUCTION_EVENT_CLASSES` per M3.6c manifest pattern. |
| NQ-6 | Spike Q1/Q2/Q3 sequencing | **RESOLVED — agreed sequencing:** Q1 + Q3 before M6 coding instruction; Q2 immediately before REC-58 implementation. |

**Only remaining open decision: REC-56's fate, which is itself blocked on Nick's Research 6 REC-41 decision (already on the Next Tasks list as item #1).**

### v2 M6 Implementation Order (final)

1. **Spike Q1 + Spike Q3** — Pi 4 SnakeYAML Engine throughput + networknt 1.5.6 memory residency. Hardware: dev Pi 5 (`hs-dev-1`).
2. **AMD-66** (REC-55 `ConfigurationChangeListener` — corrected non-generic shape) — public-API addition.
3. **AMD-68** (REC-57 `SecureCredentialBundle` record + `SecretStore.credentialsFor(String)`) — depends on AMD-69 secrets infrastructure for actual credential resolution but the API can land first.
4. **Spike Q2** (Pi 4 Argon2id timing) — informs final KDF parameters.
5. **AMD-69** (REC-58 Argon2id KDF + BouncyCastle dependency) — secrets persistence path. Commit `docs/secrets-threat-model.md` from §7.9.
6. **AMD-70** (REC-59 `config.validation_completed` + `config.section_reloaded` events) — observability layer; payload shape contingent on REC-56 (revert to single `schemaVersion` if REC-56 doesn't proceed).
7. **Phase 3 wiring AMDs** (TBD when `module-info.java` gains `requires com.networknt.schema;`, `requires org.snakeyaml.engine;`, `requires org.bouncycastle.provider;`).
8. **AMD-67** (REC-56 file-schema `(major, minor)`) — *if and only if* Nick approves Research 6 REC-41. Must land in lockstep with REC-41.
9. **AMD-71** (REC-60 hybrid directory layout) — deferred to M6 planning; no M4 types depend.

### v2 Lessons Internalized (PM-side)

I should have caught all five of Nick's corrections. The lessons:

1. **Check the Locked Decisions register, not just `libs.versions.toml`.** v1 caught the version state (`snakeyaml-engine = "2.9"`, `json-schema-validator = "1.5.6"`) but didn't cross-reference LTD-09, which already locks the library choices themselves. The two-step check (catalog + Locked Decisions) is the right protocol. Add to the PM skill's "Files to Read for library-touching RECs" — `homesynapse-core-docs/governance/HomeSynapse_Core_Locked_Decisions.md` is mandatory alongside `libs.versions.toml`.
2. **Check the Architecture Invariants register before treating any "design question" as open.** F8 (Q7 file-vs-event) is a settled invariant (INV-CE-01); the research's framing as "the single highest-impact finding" was wrong. PM should have noted "INV-CE-01 makes this not an open question — researcher's analysis is supporting evidence for the invariant." Add invariant cross-check to the §1 verdict review step.
3. **The one-flat-package-per-module invariant must be on the explicit §7 verification checklist.** F6 (`.internal` sub-package) is a real fabrication that would propagate to code if uncaught. Knowledge Primer §Module Map explicitly verifies this for all modules — PM should have flagged any proposed sub-package as a fabrication.
4. **Apply Java mechanics review to every proposed type shape.** F7 (`<S extends ConfigSection>` with records) is basic Java: records are implicitly `final`. The PM should have run the proposed signatures through a mental compiler before approving REC-55's sealed-generic structure. Add "type-mechanics soundness check" to the per-REC verification step.
5. **`credentialsFor` interface placement was a v1 PM oversight in REC-57.** I recommended extending `ConfigurationAccess` directly because the researcher implied it; I should have asked "does this method belong on this interface conceptually?" Config and secrets are separate concerns — `ConfigurationAccess` is read-only config, `SecretStore` is the secrets surface. Cross-interface convenience method placement deserves its own design beat.

These five lessons go into `pm-lessons.md` as 2026-05-22 entries titled "Research 5 v2 — what the v1 assessment missed."

---

**v2 Assessment completed:** 2026-05-22 by PM (Cowork session, post Nick review).
**v2 Status:** FINAL — all NQs resolved; only REC-56 / AMD-67 deferred on Nick's Research 6 REC-41 decision (already on Next Tasks). 4 AMDs active (AMD-66/68/69/70), 2 deferred (AMD-67/71), 2 retired (AMD-64/65).
**Next step:** Nick decides Research 6 REC-41 (unblocks REC-56); AMD-66/68/69/70 proceed to ratification; Spike Q1/Q3 scheduled before M6 coding instruction; Spike Q2 scheduled before REC-58 implementation. Research 7 brief remains the next research-agenda authoring task — must embed verbatim `libs.versions.toml` rows AND cross-reference LTD register AND cross-reference Architecture_Invariants register per Research 5 v2 lessons.

