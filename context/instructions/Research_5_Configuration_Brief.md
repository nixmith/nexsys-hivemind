<!--
file: context/instructions/Research_5_Configuration_Brief.md
purpose: Self-contained prompt for the Claude Project to produce Research 5 (Configuration System Patterns for Constrained IoT Runtimes).
audience: Nick (paste into Claude Project conversation)
state-type: ephemeral
-->

# RESEARCH BRIEF: Research 5 — Configuration System Patterns for Constrained IoT Runtimes

You are the PM/architect for HomeSynapse Core, a local-first event-sourced smart home runtime in Java 21 targeting Raspberry Pi 4/5. Your task is to produce a research document following the exact format specified below.

## Mandatory Format

Every research document must follow this structure. Non-negotiable sections are marked **[M]**; optional sections are marked **[O]**.

```
# Research 5: {Title} — {Subtitle}

*Target: HomeSynapse Core M6 (Configuration System), with M4-amendment-window coupling. Date: YYYY-MM-DD.*

## 1. Executive Summary [M]
  - 5-8 bullet points, each a **verdict** with a bold claim and one-sentence defense.
  - Every bullet must take a position. "X is worth investigating" is banned.
    Use "X should be adopted because Y" or "X should be rejected because Y."
  - Flag the single highest-impact finding explicitly.

## 2. Platform / Literature Deep Dives [M]
  - One subsection per platform or prior-art system studied.
  - Each subsection must include:
    (a) How the platform solves the problem under investigation.
    (b) At least one direct quotation from primary source (docs, issue tracker,
        maintainer statement) with URL.
    (c) Known pain points / failure modes from community reports.
    (d) Specific lesson for HomeSynapse (not generic observation).

## 3. Cross-Cutting Analysis [M]
  - Concept Mapping Table: HomeSynapse concept | Platform A | Platform B | ...
  - Gap Analysis: concepts present in 2+ platforms that HomeSynapse lacks,
    ranked by impact.
  - Over-Abstraction Analysis: concepts HomeSynapse has that no one needs,
    with defense or retraction for each.
  - Competitive Assessment: where HomeSynapse is genuinely differentiated,
    with the precise qualifying language that survives scrutiny.

## 4. Amendment Recommendations [M]
  - Ranked by (impact × confidence) / cost.
  - Each REC must include: Gap citation, Lesson source, Change (specific
    record/interface/event shape), Backward compat assessment, Effort estimate.
  - REC-XX format. Numbered globally: Research 6 used REC-41 through REC-52.
    This document starts at REC-53.

## 5. Caveats and Open Questions [M]
  - Source reliability notes.
  - Unresolved tensions between platforms.
  - Questions that require empirical validation (spike/prototype).

## 6. Appendix: Sources [M]
  - URL families grouped by platform.
  - Every factual claim must be traceable to a source listed here.

## 7. HomeSynapse Code-Level Implications [M — required for this research]
  - Specific records, interfaces, sealed hierarchy changes.
  - Event schema additions.
  - MODULE_CONTEXT impact (which modules gain/change types).
  - JPMS module-info impact.
  - Migration considerations (V00x for SQLite; config-file schema versioning).
```

---

## SCOPE

The Configuration System is the runtime-mutable surface that every other subsystem consumes through `ConfigurationAccess`. Doc 06 specifies YAML 1.2 loading, JSON Schema validation, AES-256-GCM encrypted secrets, hot-reload with a sync-before-event listener pattern, and forward-only schema migrations. The Phase 2 type inventory (verified below) is complete; what's missing is empirical validation against production smart-home configuration systems, threat-model justification for the secrets layer, and an articulated answer to the M4-amendment-window coupling questions raised by Research 4 v3, Research 6 v1, and Research 8 v2.

This research is sequenced now (after Research 6 v1) because three M4-bound decisions touch the configuration system directly: (a) Research 6 REC-41's `migrate(fromMajor, fromMinor, toMajor, toMinor, oldConfig)` adapter hook needs to align with `ConfigMigrator`'s existing fromVersion/toVersion shape; (b) Research 6 REC-45's `SecureCredentialBundle` type lives in `com.homesynapse.config` and needs a relationship to the existing `SecretStore` interface; (c) Research 4 REC-39's automation event schema landed in `com.homesynapse.event` (flat package) — but the *YAML* automation definition schema lives in the configuration system, and the relationship between event-schema and YAML-schema matters for the operator-facing surface.

### Specific questions to answer

1. **YAML loading library choice (SnakeYAML vs Jackson YAML vs alternatives).** Doc 06 specifies YAML 1.2. SnakeYAML 2.x is the standard Java library but has had CVEs (CVE-2022-1471 the most cited). Jackson YAML uses SnakeYAML internally — does this transitive dependency leak the same risk surface? What does HA do? (Answer: HA uses PyYAML, not Java — but the choice reasoning is informative.) What does OpenHAB do? (Answer: SnakeYAML + custom parser.) What about Eclipse Kura? (Properties + JSON via Karaf, not YAML.) What's the right call for a constrained runtime: minimize dependency surface (SnakeYAML directly), align with existing Jackson usage (Jackson YAML — Jackson is already the LTD-19 serialization library), or roll a strict YAML 1.2 subset parser? Performance benchmarks on a Pi 4 for a representative ~500-line config?

2. **JSON Schema validation library and composition.** Doc 06 specifies JSON Schema validation. The configuration system has a `SchemaRegistry` interface that composes core + integration schemas (`registerCoreSchema`, `registerIntegrationSchema`, `getComposedSchema`). What library implements the validation? networknt/json-schema-validator? everit-org/json-schema (archived)? Justify Java 21 + JPMS compatibility. How does HA validate config? (voluptuous in Python — not directly relevant.) How does OpenHAB? (XSD for thing-types — explicit schema files, similar pattern.) How does Eclipse Kura? (OSGi MetaType — annotation-driven, not file-based.) What's the right composition strategy when a new integration installs at runtime — recompose and re-validate, or validate per-integration?

3. **Secret management threat model and key derivation.** Doc 06 specifies AES-256-GCM encrypted secrets. **What is the threat model?** The brief left this partly open. Possible answers: (a) protect against on-device attackers with filesystem-read access (requires hardware-backed key — TPM2 on Pi 5); (b) protect against backups/exfil (requires user-supplied passphrase + PBKDF2/Argon2id KDF); (c) defense-in-depth against an integration adapter reading another integration's secrets (process-level secrets are insufficient — requires per-integration ACL on `SecretStore`); (d) all of the above. How does HA handle this? (`secrets.yaml` is plaintext, not encrypted — explicit decision.) How does OpenHAB? (Karaf JCEKS keystore — encrypted with a single keystore password.) How does Matter? (Operational keys + DAC PKI — not directly applicable but instructive.) For HomeSynapse, propose a defensible threat model and pick the smallest KDF + key-storage combination that satisfies it. How does this interact with Research 6 REC-45's `SecureCredentialBundle` (per-integration credential lifecycle)?

4. **Hot reload with atomic swap and the `ConfigurationChangeListener` pattern.** Doc 06 specifies `ConfigurationChangeListener` fires synchronously before the `config_changed` event is published. **This type does not exist yet in the codebase** (verified: only `ConfigurationValidationException` is imported from event-model in the current `ConfigurationService.java`). What pattern does HA use? (HA reloads integrations individually via `async_reload`.) OpenHAB? (`handleConfigurationUpdate` per ThingHandler — sync.) Kura? (`@Modified` annotation — sync, with snapshot/rollback.) Spring Boot? (`@RefreshScope` — bean-level lazy reload, not directly applicable.) What's the right shape for `ConfigurationChangeListener`? Specific question: should it be a typed interface per-subsystem (`PersistenceConfigListener`, `EventBusConfigListener`) or a single generic `ConfigurationChangeListener` keyed by section path? The existing `ConfigChangeSet` record (5 fields including `ReloadClassification`) gates `HOT` vs `INTEGRATION_RESTART` vs `PROCESS_RESTART` — how do listeners signal "I can apply this in-place" vs "I need a restart"?

5. **Config file organization and multi-file `!include`.** HA uses a directory tree (`configuration.yaml`, `automations.yaml`, `scripts.yaml`, `scenes.yaml`, plus `!include` directives). OpenHAB uses `/conf/things/`, `/conf/items/`, `/conf/rules/`. What's the right file organization for HomeSynapse? Single file? Directory tree? Per-integration files? How does this interact with: (a) the `SchemaRegistry` composition (integration schemas registered at startup vs at file-load time); (b) hot reload (does adding a new `automations.yaml` file trigger reload, or only edits to known files); (c) the operator's mental model (is "edit this one file" easier than "find which file contains key X").

6. **Schema versioning, migration, and Research 6 REC-41 alignment.** The existing `ConfigMigrator` interface has `fromVersion() → int`, `toVersion() → int`, `migrate(Map<String, Object>) → MigrationResult`. Research 6 REC-41's adapter `migrate(int fromMajor, int fromMinor, int toMajor, int toMinor, IntegrationConfig oldConfig)` uses a **(major, minor) pair**. **Reconcile this.** Should `ConfigMigrator` change to (major, minor) pairs? Should adapter `migrate(...)` simplify to a single int? Should the *file* schema version be (major, minor) but the *adapter config schema* be a single int? Cite HA's migration pattern (`async_migrate_entry` with `entry.version` as a single int + `entry.minor_version` as a separate int — actual HA shape). What's the precise relationship between `ConfigModel.schemaVersion` (single int, currently) and the adapter schema versions?

7. **Config-as-event vs config-as-file: the event-sourcing tension.** HomeSynapse is event-sourced. The current design has the YAML *file* as the source of truth, with `ConfigModel.fileModifiedAt` as the optimistic concurrency token. But `config_changed` is also a domain event. Is the YAML file the source of truth, or is the event log? What happens if the file is edited externally between two `config_changed` events — does the event log diverge from disk? How do other event-sourced systems handle config? (EventStoreDB: config is process-level, not event-sourced. Marten: same. Akka Persistence: separate config layer.) For HomeSynapse, articulate the canonical answer: file is source of truth, events are observability; OR events are source of truth, file is a projection. Defend the choice.

8. **Operator UX for config errors.** The three-tier error model (`FATAL` / `ERROR` / `WARNING`) is good. But how is it surfaced? HA shows config errors in the UI repairs panel + log. OpenHAB shows ThingStatusDetail. The configuration system produces `ConfigIssue` records (6 fields including `severity`, `path`, `message`, `appliedDefault`, `yamlLine`). How does the operator see these? Doc 11 (observability) covers some of this, but what's specifically the contract between the configuration system and the REST API / observability surface? Should the configuration system publish a `config_validation_completed` event with the issue list?

### Platforms / prior art to survey

- Home Assistant configuration (secrets.yaml, !include, config flow, async_migrate_entry, repairs panel)
- OpenHAB configuration (Karaf config admin, .things/.items/.rules files, thing-types-update.xml, JCEKS keystore)
- Hubitat configuration model (proprietary but operator-visible patterns)
- Spring Boot externalized configuration (for comparison — mature Java ecosystem; `@ConfigurationProperties`, `@RefreshScope`)
- Micronaut configuration (for constrained Java comparison — designed for AOT/GraalVM)
- Eclipse Kura ConfigurationService + OSGi MetaType (constrained-IoT-platform precedent)
- networknt/json-schema-validator (the most-maintained JVM JSON Schema library — verify license, JPMS support, dependency surface)
- SnakeYAML 2.x security history (CVE-2022-1471 trust model change, SafeConstructor default)
- Apache Tika ConfigStore (constrained-runtime config patterns)

---

## CONTEXT YOU NEED

- HomeSynapse Core Knowledge Primer (uploaded to project knowledge — refreshed 2026-05-22, package annotations corrected)
- HomeSynapse Current State (uploaded to project knowledge)
- Doc 06 (Configuration System) — the governing design document for this research
- Research 4 v3 PM Assessment — establishes the M4-amendment-window pattern; REC-39 automation event schema landing in `com.homesynapse.event`
- Research 6 v1 PM Assessment — establishes the `module-info.java` embedding rule; REC-41 adapter `migrate(...)` shape; REC-45 `SecureCredentialBundle` placement in `com.homesynapse.config`
- Research 8 v2 PM Assessment (FINAL) — establishes the `DispatchingProjectionAdvancer` pattern; `EntityCategory` registry-property contract

### Key context from completed upstream research (M4-coupling for Research 5):

- **Research 6 REC-41 (PENDING Nick decisions):** Adapter `migrate(int fromMajor, int fromMinor, int toMajor, int toMinor, IntegrationConfig oldConfig)` uses (major, minor) pairs. Research 5 §Q6 must reconcile this with the existing `ConfigMigrator.fromVersion()` / `toVersion()` (single int each) AND with `ConfigModel.schemaVersion` (single int, currently). PM open question NQ-2 (Research 6) recommended introducing `configSchemaMajor` + `configSchemaMinor` alongside the existing single int.

- **Research 6 REC-45 (PENDING Nick decisions):** `SecureCredentialBundle` type lives in `com.homesynapse.config` (NOT `com.homesynapse.configuration` — that fabrication was caught in Research 6 v1 F4). The proposed `CredentialRotator` service is delivered via a `SecurityServices` aggregator field on `IntegrationContext`. Research 5 must specify the storage shape: does `SecureCredentialBundle` reuse the existing `SecretStore` interface (which stores `SecretEntry(key, value, createdAt, updatedAt)` records — verified) or is it a distinct per-integration credential abstraction layered on top?

- **Research 4 REC-39 (PENDING Nick decisions):** Automation event records (11 types) land in `com.homesynapse.event` (flat package). The YAML automation definition schema lives in the configuration system. Q5 of this research asks how multi-file YAML organization interacts with the schema-composition contract.

- **Research 8 REC-28 (FINAL, M4.0 scope):** `DispatchingProjectionAdvancer` with constructor-injected handlers (DECIDE-04 — NO ServiceLoader). If Research 5 §Q8 proposes a `config_validation_completed` event, it needs a `ProjectionEventHandler` registration just like the integration lifecycle events.

### Cross-research-arc fabrication patterns to avoid

The prior three research documents (Research 3, 4, 8) fabricated **type names** when MODULE_CONTEXT was not embedded; Research 6 fabricated **JPMS module names** when `module-info.java` was not embedded. **Both layers are now embedded below for this brief.** Use the verbatim identifiers — do NOT paraphrase, do NOT infer from Knowledge Primer summaries, do NOT invent.

---

## CONSTRAINTS

- Take positions. "X is worth investigating" is banned. Use "X should be adopted because Y" or "X should be rejected because Y."
- Cite primary sources (docs, issue trackers, maintainer statements) with URLs.
- Every REC must include effort estimate in lines of code.
- Number RECs globally: Research 6 used REC-41 through REC-52. **This document starts at REC-53.**
- AMD numbering: AMD-01 through AMD-63 are allocated/proposed (AMD-47 withdrawn, AMD-61 withdrawn). New amendments start at **AMD-64**.
- Include §7 (Code-Level Implications) — MANDATORY. Specify exact Java records, interfaces, sealed hierarchy changes, event schema additions, module-info changes.
- For each proposed type change, specify: (a) the exact module, (b) the exact package, (c) public vs package-private visibility, (d) whether it requires an AMD.
- **Use the verbatim type and module identifiers embedded below. Do not paraphrase package names, module names, or type names.** Prior research documents fabricated type names (Research 3/4/8 §7) and module names (Research 6 §7.8) when these were not embedded verbatim — both layers are now embedded.
- **No `@Nullable` annotations in proposed signatures.** HomeSynapse codebase convention is Javadoc-only nullability (`{@code null} if …` patterns). Confirmed in every MODULE_CONTEXT Gotchas section.

### Verified module identifiers (verbatim `module-info.java` contents)

**`config/configuration/src/main/java/module-info.java`:**

```java
module com.homesynapse.config {
    requires transitive com.homesynapse.event;

    exports com.homesynapse.config;
}
```

**JPMS module name:** `com.homesynapse.config` (NOT `com.homesynapse.configuration`). **Java package:** `com.homesynapse.config`. **Single transitive dependency:** `com.homesynapse.event` (event-model).

**`core/event-model/src/main/java/module-info.java`** (event-model, the only direct dependency):

```java
module com.homesynapse.event {
    requires transitive com.homesynapse.platform;

    exports com.homesynapse.event;
}
```

**JPMS module name:** `com.homesynapse.event` (NOT `com.homesynapse.event.model`). **Java package:** `com.homesynapse.event`.

**`integration/integration-api/src/main/java/module-info.java`** (cited by REC-41/REC-45 cross-research alignment):

```java
module com.homesynapse.integration {
    requires transitive com.homesynapse.platform;
    requires transitive com.homesynapse.event;
    requires transitive com.homesynapse.device;
    requires transitive com.homesynapse.state;
    requires transitive com.homesynapse.persistence;
    requires transitive com.homesynapse.config;
    requires transitive java.net.http;

    exports com.homesynapse.integration;
}
```

**JPMS module name:** `com.homesynapse.integration` (NOT `com.homesynapse.integration.api`). **Java package:** `com.homesynapse.integration`.

### Verified type inventory — `config/configuration/MODULE_CONTEXT.md` (configuration, 22 public types)

**Enums (3):**
- `Severity` — 3 values: `FATAL`, `ERROR`, `WARNING`. Validation issue severity (three-tier error model, §3.6).
- `ReloadClassification` — 3 values: `HOT`, `INTEGRATION_RESTART`, `PROCESS_RESTART`. Runtime impact of a config change, derived from `x-reload` JSON Schema annotation.
- `ChangeType` — 5 values: `KEY_RENAMED`, `KEY_ADDED`, `KEY_REMOVED`, `VALUE_TRANSFORMED`, `SECTION_RESTRUCTURED`. Migration change kinds.

**Data Records (11):**
- `ConfigIssue` (6 fields): `severity`, `path` (JSON Schema path), `message`, `invalidValue` (nullable), `appliedDefault` (nullable), `yamlLine` (Integer, nullable).
- `SecretEntry` (4 fields): `key`, `value` (plaintext after decryption), `createdAt`, `updatedAt`. All non-null.
- `ConfigMutation` (3 fields): `sectionPath`, `key`, `newValue` (nullable — null means remove key).
- `ConfigSection` (3 fields): `path` (e.g., `"persistence.retention"`), `values` (unmodifiable Map), `defaults` (unmodifiable Map).
- `ConfigChange` (5 fields): `sectionPath`, `key`, `oldValue` (nullable), `newValue` (nullable), `reload` (ReloadClassification). The reload-pipeline diff record.
- `MigrationChange` (5 fields): `type` (ChangeType), `path`, `oldValue` (nullable), `newValue` (nullable), `reason`. Renamed from Doc 06's second `ConfigChange` to avoid collision.
- `ConfigChangeSet` (2 fields): `timestamp`, `changes` (unmodifiable List<ConfigChange>). Complete reload diff.
- `MigrationResult` (2 fields): `migratedConfig` (unmodifiable Map), `changes` (unmodifiable List<MigrationChange>).
- `MigrationPreview` (4 fields): `fromVersion` (int), `toVersion` (int), `plannedChanges` (unmodifiable List), `requiresUserReview` (boolean — true when migrations remove keys or lossy-transform values).
- `ConfigModel` (5 fields): `schemaVersion` (int — **single int, not a (major, minor) pair**), `loadedAt`, `fileModifiedAt` (optimistic concurrency token for write path), `sections` (unmodifiable Map), `rawMap` (unmodifiable Map). **Phase 2 simplification:** Map-based sections, not typed subsystem records.
- `ReloadResult` (3 fields): `newModel`, `changeSet`, `issues` (unmodifiable List — only WARNING survives; FATAL/ERROR cause rejection).

**Exceptions (2):**
- `ConfigurationLoadException` extends `HomeSynapseException` — error code `config.load_failed`, HTTP 503.
- `ConfigurationReloadException` extends `HomeSynapseException` — error code `config.reload_failed`, HTTP 422.

**Note:** `ConfigurationValidationException` is in **`com.homesynapse.event`**, NOT in `com.homesynapse.config` (verified via source import in `ConfigurationService.java:7`).

**Service Interfaces (6):**
- `ConfigurationService` — `load() → ConfigModel`, `reload() → ReloadResult`, `getCurrentModel() → ConfigModel`, `getSection(String) → Optional<ConfigSection>`, `write(List<ConfigMutation>, Instant) throws ConfigurationValidationException, ConcurrentModificationException`.
- `ConfigurationAccess` — read-only, integration-scoped. `getConfig() → Map<String, Object>` (unmodifiable), `getString(String) → Optional<String>`, `getInt(String) → Optional<Integer>`, `getBoolean(String) → Optional<Boolean>`.
- `SecretStore` — `resolve(String) → String` (throws if not found), `set(String, String)`, `remove(String)`, `list() → Set<String>` (unmodifiable).
- `ConfigValidator` — `validate(Map<String, Object>, String) → List<ConfigIssue>` (unmodifiable). String parameter is JSON text, NOT a file path.
- `ConfigMigrator` — `fromVersion() → int`, `toVersion() → int`, `migrate(Map<String, Object>) → MigrationResult`. Idempotent. **Single int versions, not (major, minor) pairs.**
- `SchemaRegistry` — `registerCoreSchema(String, String)`, `registerIntegrationSchema(String, String)`, `getComposedSchema() → String`, `writeComposedSchema(Path)`. All schema parameters are **String (JSON text), NOT a JsonSchema library type**.

**Total: 22 public types + module-info.java + package-info.java = 24 Java files.** Single flat package `com.homesynapse.config`.

### Verified NON-existent types (do not invent)

The Research 5 brief explicitly checked the source — these types referenced in Doc 06 or in informal discussions do NOT exist in the current codebase:

- **`ConfigurationChangeListener`** — referenced in Doc 06 (sync-before-event-publish listener pattern) but NOT implemented. Phase 3 type. Research 5 §Q4 should propose its exact shape — this is a primary deliverable.
- **`SecureCredentialBundle`** — proposed by Research 6 REC-45, not yet implemented. Research 5 §Q3 should propose its exact shape and relationship to existing `SecretStore`.
- **`configSchemaMajor`/`configSchemaMinor`** — proposed by Research 6 NQ-2, not yet implemented. Research 5 §Q6 should resolve the (major, minor) vs single-int tension.

### Verified upstream constraints (do not propose changes — outside Research 5 scope)

- `ConfigModel.rawMap` is `Map<String, Object>`, NOT typed subsystem records. Per "Phase 2 simplification" — typed configs are Phase 3 work.
- `SchemaRegistry` parameters are JSON text Strings, NOT a JsonSchema library type. Library choice is internal to Phase 3 implementation.
- All collection fields in records use `List.copyOf()` / `Map.copyOf()` defensive copies. New records must follow this pattern.
- `Severity` is the 3-value enum; do not propose a 4th severity. The `FATAL` / `ERROR` / `WARNING` model is locked.

### Event naming convention

Legacy events use snake_case with underscores: `config_changed`, `secret_added`, `secret_removed`. New events use dot-separated namespacing: `config.validation_completed`, `config.section_reloaded`. Both patterns are permanent. When proposing new events in §7, use whichever style fits the cluster (existing `config_*` events use underscore; new ones may use either — recommend dot-separated for clarity, as Research 4 REC-39 and Research 6 REC-44 both adopted).

---

## OUTPUT

A single markdown document following the mandatory format above. Do not truncate. Produce the complete document. Target length: ~550–700 lines.

When you reach §7 (Code-Level Implications), structure proposals around these specific surfaces:

1. **`ConfigurationChangeListener` interface — propose the exact shape.** Method signature(s), nullability semantics (use Javadoc, not annotations), thread-safety contract, ordering guarantee (sync-before-event-publish), the subsystem-vs-generic question from §Q4. State whether it's a new public type in `com.homesynapse.config` and whether it requires an AMD (likely yes — extends the configuration system's public API).

2. **`SecureCredentialBundle` record (or interface) — propose the exact shape.** Relationship to existing `SecretStore` (composition? replacement? layered on top?). Per-integration scoping mechanism. State the AMD requirement.

3. **`ConfigMigrator` (major, minor) reconciliation — three options.** (a) Keep single int, adapter `migrate(...)` simplifies to single int; (b) Change both to (major, minor); (c) Different shapes for file-schema (single int) vs adapter-schema (major, minor). Pick one with defense.

4. **YAML library + JSON Schema validator dependency choices.** Specific library + version + license + JPMS-module name. Effort to integrate. Performance budget on a Pi 4 (target: load ~500-line config in <500ms).

5. **`ConfigSection` and multi-file organization.** Single config file, directory tree, or hybrid? How does `!include` interact with `SchemaRegistry`?

6. **New event types (if any).** Specify `@EventType(...)` strings (dot-namespaced recommended), payload schemas, and **state-changing vs observability-only classification** (required for `DispatchingProjectionAdvancer` handler registration per Research 8 REC-28).

7. **`module-info.java` impact.** The configuration module currently requires only `com.homesynapse.event` transitively. Does the YAML library / schema validator require additional `requires`? Are they internal (`implementation` scope, no `requires` directive) or do their types leak into the public API (need `requires`)?

8. **Threat-model documentation deliverable.** A short defended threat-model statement that the secrets layer implements against. This is a §7 output (it shapes the `SecretStore` + `SecureCredentialBundle` choices) and a §5 caveat (operator-facing implications).

### Coder Pushback Welcome

If Research 5 uncovers a contradiction between Doc 06 §3.x and the verified MODULE_CONTEXT type inventory above, flag it explicitly in §5. The MODULE_CONTEXT is authoritative for type-level facts (verified 2026-05-22). Doc 06 is authoritative for behavioral contracts. If they diverge, that's a PM action item, not a researcher fabrication.

If Research 5 finds that one of the open questions from Research 6 (NQ-1 through NQ-6, specifically NQ-2 on schema versioning and the indirect NQ-1 implication for `SecurityServices` aggregator membership) is actually answerable from configuration-system-side evidence, surface that in §5 — the PM will reconcile across both assessments.
