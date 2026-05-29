<!--
file: context/planning/research-agenda.md
purpose: Research agenda for Claude Project — structured briefs for M3.7 through M9+.
audience: PM, Nick
update-cadence: ad-hoc
state-type: planning
status: CURRENT
last-verified: 2026-05-22
-->

# HomeSynapse Core — Research Agenda

*Produced 2026-05-22 by PM (Cowork). Companion to Research 2 (Smart Home Entity Modeling). Defines what the Claude Project should investigate, in what order, in what format, and how findings feed into architectural decisions.*

---

## 0. Research Philosophy and Format Specification

### Why Research, Not Just Build

HomeSynapse Core is infrastructure software with a 5+ year horizon. Every subsystem we implement commits us to contracts — sealed hierarchies, event schemas, JPMS module boundaries — that downstream code will depend on. Research before implementation means we make commitments with evidence, not intuition. Research 2 already proved this: the `staleAfter + Clock` model survives competitive scrutiny *because* we can articulate precisely how it differs from HA's `expire_after` and why the difference matters.

### Mandatory Format for All Research Documents

Every research document produced by the Claude Project must follow this structure. Non-negotiable sections are marked **[M]**; optional sections are marked **[O]**.

```
# Research {N}: {Title} — {Subtitle}

*Target: HomeSynapse Core {milestone(s)}. Date: YYYY-MM-DD.*

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
  - REC-XX format. Numbered globally across all research documents
    (Research 2 used REC-01 through REC-12; Research 3 starts at REC-13).

## 5. Caveats and Open Questions [M]
  - Source reliability notes.
  - Unresolved tensions between platforms.
  - Questions that require empirical validation (spike/prototype).

## 6. Appendix: Sources [M]
  - URL families grouped by platform.
  - Every factual claim must be traceable to a source listed here.

## 7. HomeSynapse Code-Level Implications [O — include when research
     directly affects Java types]
  - Specific records, interfaces, sealed hierarchy changes.
  - Event schema additions.
  - MODULE_CONTEXT impact (which modules gain/change types).
  - JPMS module-info impact.
  - Migration considerations (V00x).
```

### What Makes Research Maximally Useful to the PM

1. **Verdicts, not surveys.** Every section must conclude with a recommendation. "Platform X does Y" is raw data; "Platform X does Y, and HomeSynapse should adopt / reject / defer Y because Z" is research.

2. **Concept mapping tables are the highest-value artifact.** Research 2's §3.1 table is the model. These tables let the PM verify coverage, spot gaps, and produce coding instructions that reference the correct prior art.

3. **Pain-point citations are load-bearing.** When Research 2 cites HA core#65558 (MQTT expire_after race condition), that's not decoration — it's the evidence that our `staleAfter` model avoids a real failure mode. Every recommendation must cite at least one pain point it addresses.

4. **Code-level implications save a full PM session.** When research says "add `EntityCategory` enum," the PM still needs to determine: what package? what module? what events change? what projection logic? Research that includes §7 (Code-Level Implications) eliminates that translation step.

5. **Ranked recommendations with effort estimates let Nick make scope decisions.** Research 2's REC-01 through REC-12 ranking is the model. Nick can draw a line: "everything above REC-05 goes into M4; below defers."

---

## 1. Research Queue — Ordered by Milestone Dependency

### Research 3: Integration Testing Patterns for Event-Sourced HTTP Systems
**Target milestone:** M3.7 (E2E integration tests)
**Priority:** IMMEDIATE — blocks next implementation work
**Estimated research effort:** 3-4 hours

#### What to investigate

M3.7 must exercise the full stack: SQLite → event bus → state projection → materialized query service → Javalin → HTTP response → assertion. No existing HomeSynapse test does this. The composition root (`HomeSynapseCore`) is a 16-step bootstrap; E2E tests must start it, publish events, wait for LIVE mode, hit HTTP endpoints with a real client, and assert correctness.

#### Specific questions to answer

1. **Javalin embedded testing patterns.** Javalin 6.x ships with `JavalinTest` — what is its API? Does it start a real Jetty server on a random port? Can it coexist with JPMS `module-info.java`? What's the alternative if `JavalinTest` doesn't work under JPMS (manual `Javalin.create().start(0)` + `java.net.http.HttpClient`)? Cite Javalin's own test suite and any community patterns.

2. **Port binding in parallel test execution.** `HomeSynapseCore` currently binds port 7070. JUnit 5 runs test classes sequentially by default but methods can be parallel. What's the correct pattern for ephemeral port allocation in Javalin? Does `Javalin.create().start(0)` work (port 0 = OS-assigned)? How do you retrieve the assigned port afterward? What about `SO_REUSEADDR` and `TIME_WAIT` between tests?

3. **Mode transition timing in tests.** The bus transitions REPLAY → TRANSITION → LIVE. E2E tests must wait for LIVE before hitting query endpoints (ReadinessFilter returns 503 otherwise). What's the correct synchronization pattern? Polling `bus.subscribers().get(0).mode()` with timeout? A `CountDownLatch` injected into `ReadinessSource`? What do Axon Framework, EventStoreDB, and Marten (the three most production-proven event-sourcing frameworks) do for integration test synchronization?

4. **Crash recovery at the HTTP level.** `CrashRecoveryIT` already tests event-level crash recovery. M3.7 should add HTTP-level crash recovery: start core → publish events → abandon (simulate crash) → restart core → wait LIVE → hit endpoints → assert state is complete. What edge cases exist? What about in-flight HTTP requests during shutdown?

5. **Test data factories for HTTP assertions.** Entity state returned via HTTP is JSON. What's the cleanest pattern for asserting JSON response bodies in Java 21 without pulling in AssertJ-JSON or Hamcrest-JSON? `java.net.http.HttpClient` + Jackson `ObjectMapper.readTree()` + JUnit assertions? Or is there a lighter approach?

6. **What should `NO_OP_DERIVATION` and `NO_OP_ADVANCER` actually do?** These are placeholder `ProjectionAdvancer` implementations in `HomeSynapseCore`. For E2E tests to observe meaningful state projection, these need real implementations. What's the minimum viable `ProjectionAdvancer.advance()` that processes `state_changed` events into `EntityState` updates? This is the bridge between M3.7 and M4.

#### Platforms / prior art to survey
- Javalin documentation (javalin.io) and GitHub test suite
- Axon Framework integration test patterns
- EventStoreDB client test patterns
- Marten (C#/.NET but architecturally relevant) test patterns
- Spring Boot `@SpringBootTest` with embedded server (for comparison)

---

### Research 4: Automation Engine Architecture — Trigger/Condition/Action Pipeline Design
**Target milestone:** M7/M8 (Automation Engine)
**Priority:** HIGH — longest-lead research item; influences M4 device model decisions
**Estimated research effort:** 8-12 hours (largest single research item)

#### Why this is high priority despite being M7/M8 scope

The automation engine is the *consumer* of every upstream subsystem. Decisions we make in M4 (device model), M5 (platform API), and M6 (configuration) are constrained by what the automation engine needs. Research 2 already surfaced this: REC-07 (ConfirmationPolicy.NONE) and the Expectation hierarchy assessment both depend on understanding how automations will *use* commands. If we build M4-M6 without understanding M7's requirements, we'll need amendments.

Doc 02 already defines the sealed hierarchies (Selector, TriggerDefinition, ConditionDefinition, ActionDefinition) and the behavioral contracts (AMD-03 positional state snapshots, AMD-04 cascade depth limiting, AMD-31 command execution ordering). What's missing is empirical validation against production automation systems.

#### Specific questions to answer

1. **Trigger evaluation models.** How does Home Assistant evaluate triggers? (State triggers, event triggers, time triggers, template triggers, webhook triggers.) How does OpenHAB evaluate rules? (JSR 223 scripting, Blockly, DSL.) How does NodeRED evaluate flows? What's the canonical "motion sensor → turn on light for 5 minutes → turn off" pattern in each? How do they handle re-triggering during the active period? Doc 02's `TriggerDefinition` sealed hierarchy has 8 permits — are there trigger types we're missing?

2. **Condition evaluation timing.** HA evaluates conditions *at trigger time*. OpenHAB rules evaluate conditions inline. Does anyone evaluate conditions *at action time* (i.e., re-check just before executing)? AMD-03's "positional state snapshots" approach is unusual — validate it against real-world automation patterns. What failure modes does each timing model produce?

3. **Command confirmation and the Pending Command Ledger.** Research 2 §3.3 flagged the 4-type Expectation hierarchy as unique. Go deeper: how does HA handle "I sent dimmer to 50% but it's at 48%"? (Answer: it doesn't — fire and forget.) How does Matter handle command confirmation? (Timed commands, interaction model.) How does Z-Wave handle command confirmation? (Supervision CC.) What percentage of real automations actually need confirmation? Is the Pending Command Ledger over-engineered, or is it the right abstraction for reliable home automation?

4. **Cascade governance.** AMD-04 limits cascade depth. How do HA, OpenHAB, and NodeRED handle automation-triggers-automation chains? Are infinite loops a real production problem? What's the failure mode? HA has `max_exceeded` on `repeat` — is that sufficient? What about cross-automation cascades (Automation A triggers state change → Automation B fires)?

5. **Temporal triggers and the clock.** AMD-25 introduced temporal-duration trigger modifiers. How do HA, OpenHAB handle "motion detected for 5 minutes" vs "motion detected, wait 5 minutes, then act"? The `for:` modifier in HA vs OpenHAB's `changed ... for` — what edge cases do they produce? How does clock injection (DEC-M3-09) interact with temporal trigger testing?

6. **Scene/routine/script abstraction.** HA has Scripts (reusable action sequences), Scenes (state snapshots to restore), and Automations (trigger→condition→action). OpenHAB has Rules, Scenes, and Profiles. Doc 02 has only Automations. Is a separate Scene primitive needed, or is it an automation that fires on command with no trigger? What about "routines" (HA helpers, Google Home routines)?

7. **Rule storage and versioning.** How are automations persisted? HA uses YAML + UI-generated JSON. OpenHAB uses file-based + REST API. How do they handle versioning, undo, and debugging? Doc 02's event-sourced approach means automation definitions are themselves events — what does `automation_created`, `automation_updated`, `automation_disabled` event schema look like?

#### Platforms / prior art to survey
- Home Assistant automations (core architecture, trigger/condition/action evaluation, Scripts, Scenes)
- OpenHAB rules (JSR 223, DSL, Blockly, rule engine internals)
- NodeRED flow evaluation model
- Apple HomeKit automation model
- Google Home routines
- Zigbee2MQTT automations (if any native)
- Matter 1.4 Scenes cluster
- Academic: ECA (Event-Condition-Action) rule systems literature

---

### Research 5: Configuration System Patterns for Constrained IoT Runtimes
**Target milestone:** M6 (Configuration System)
**Priority:** MEDIUM — feeds M6 but not blocking M3.7/M4
**Estimated research effort:** 4-6 hours

#### Specific questions to answer

1. **YAML loading pipeline.** Doc 02 specifies YAML 1.2. What YAML library should HomeSynapse use? (SnakeYAML 2.x is the standard Java library but has had CVEs; Jackson YAML uses SnakeYAML internally.) How do HA and OpenHAB load config? What validation patterns exist? JSON Schema validation of YAML — how do HA addons validate `config.yaml`? What's the performance cost of schema validation on a Pi 4?

2. **Secret management on constrained hardware.** Doc 02 specifies AES-256-GCM encrypted secrets. How does HA handle secrets? (`secrets.yaml` with `!secret` YAML tag — plaintext file, not encrypted.) How does OpenHAB? What's the right key derivation for a headless Pi? PBKDF2? Argon2id? Hardware-backed key storage (TPM2 on Pi 5)? What's the threat model — who are we protecting secrets from?

3. **Hot reload with atomic swap.** Doc 02 mentions `ConfigurationChangeListener` firing synchronously before the `config_changed` event. How do production systems handle config reload? HA reloads integrations individually. OpenHAB has `handleConfigurationUpdate(Configuration)`. What about partial reload vs full restart? What about config validation before swap (fail-fast)?

4. **Multi-file config organization.** HA uses a directory tree (`configuration.yaml`, `automations.yaml`, `scripts.yaml`, `scenes.yaml`, plus `!include` directives). OpenHAB uses `/conf/things/`, `/conf/items/`, `/conf/rules/`. What's the right file organization for HomeSynapse? Single file? Directory tree? Per-integration files?

5. **Config migration across versions.** When HomeSynapse ships v1.1 with new config fields, how is the v1.0 config migrated? HA has no formal migration — breaking changes documented in release notes. OpenHAB has thing-types-update.xml. What's the right pattern for a system that may run unattended for months?

#### Platforms / prior art to survey
- Home Assistant configuration (secrets.yaml, !include, config flow)
- OpenHAB configuration (karaf config admin, .things/.items/.rules files, thing-types-update.xml)
- Hubitat configuration model
- Spring Boot externalized configuration (for comparison — mature Java ecosystem)
- Micronaut configuration (for constrained Java comparison)
- Eclipse Kura (IoT gateway config patterns)

---

### Research 6: Integration Runtime — Supervisor Patterns for Protocol Adapters
**Target milestone:** M9 (Integration Runtime)
**Priority:** MEDIUM — influences IntegrationContext lifecycle decisions in M4
**Estimated research effort:** 5-7 hours

#### Why this matters for M4

Research 2's REC-08 (Formalize IntegrationContext lifecycle: Reauth, Reconfigure, OptionsFlow analogs) touches integration runtime territory. The adapter lifecycle — discovery → setup → running → error → restart → reconfigure — must be designed holistically. If we implement M4's IntegrationContext without understanding M9's supervisor, we'll build the wrong lifecycle hooks.

#### Specific questions to answer

1. **Erlang/OTP supervision in Java.** HomeSynapse Doc 05 specifies OTP-style one-for-one supervision. What Java libraries exist? (Akka/Pekko typed actors, but HomeSynapse is explicitly not actor-based.) How do you implement restart intensity (max N restarts in T seconds) with virtual threads? What's the failure taxonomy? Doc 05's `ExceptionClassification(TRANSIENT/PERMANENT/SHUTDOWN_SIGNAL)` — is this the right granularity?

2. **Adapter lifecycle FSM.** OpenHAB's ThingStatus (UNINITIALIZED → INITIALIZING → ONLINE / OFFLINE / UNKNOWN, with REMOVING and REMOVED) is well-documented. HA's ConfigEntry lifecycle (LOADED → SETUP_IN_PROGRESS → SETUP_RETRY → LOADED, or SETUP_ERROR / MIGRATION_ERROR). What's the right FSM for HomeSynapse? How many states? What transitions?

3. **Health aggregation.** When 5 of 20 integrations are OFFLINE, how do you present system health? HA shows per-integration status. OpenHAB has Thing status detail (HANDLER_MISSING_ERROR, CONFIGURATION_ERROR, etc.). What should HomeSynapse's `HealthReporter` aggregate?

4. **Dynamic capability discovery post-adoption.** Research 2 §2.3.3 surfaced OpenHAB's pain with dynamic channel creation (openhab-core#4048). When a Zigbee device firmware-updates and gains a new cluster, how should HomeSynapse handle the new capability? Event-driven (`capability_discovered`)? Polling? What about capability *removal*?

5. **Startup ordering with dependency graphs.** Doc 05 specifies Kahn's algorithm (AMD-14) for startup ordering. What real dependencies exist between integrations? (Zigbee coordinator must start before Zigbee devices; Matter bridge must start before bridged devices.) How do HA and OpenHAB handle this? (HA uses `after_dependencies` in manifest.json.)

#### Platforms / prior art to survey
- Erlang/OTP supervisor documentation (canonical reference)
- Akka/Pekko typed supervision (Java adaptation)
- Home Assistant integration lifecycle (setup, config entry, coordinator)
- OpenHAB binding lifecycle (ThingHandler, ThingStatus, ThingStatusDetail)
- Eclipse Kura container services
- Android service lifecycle (for comparison — constrained platform)

---

### Research 7: REST and WebSocket API Design for Event-Sourced Smart Home Systems
**Target milestone:** M10/M11 (REST API + WebSocket API)
**Priority:** LOW-MEDIUM — long lead time, but API shape influences M4 entity design
**Estimated research effort:** 6-8 hours

#### Specific questions to answer

1. **REST API design for event-sourced reads.** M3.6e.2 delivered MVP endpoints. What should the full REST API look like? HA's REST API (developers.home-assistant.io/docs/api/rest/). Matter's Interaction Model (Read, Write, Subscribe, Invoke). OpenHAB's REST API (openhabcloud, Swagger). What pagination model? (Keyset vs offset — keyset is better for event-sourced.) What filtering? What response envelopes?

2. **WebSocket subscription protocol.** Doc 11 specifies WebSocket-based event subscriptions with backpressure. How does HA implement WebSocket? (Persistent connection, `subscribe_events` command, JSON-RPC-like protocol.) How does EventStoreDB's subscription work? (Catch-up subscriptions, persistent subscriptions.) What's the right framing protocol? (JSON lines? WebSocket binary frames? Custom protocol?)

3. **Event filtering at the API layer.** Doc 11 mentions `WsSubscriptionFilter`. What filter capabilities do clients need? (By entity, by event type, by area, by time range.) How granular? HA allows subscribing to specific event types but not entity-filtered subscriptions natively. What's the performance model — filter on server or send everything?

4. **Backpressure in WebSocket streams.** When a slow client can't keep up with event production, what happens? HA drops events silently. EventStoreDB has subscription checkpointing. What's the right model for HomeSynapse? Buffer + drop oldest? Checkpoint + replay? Disconnect slow clients?

5. **Rate limiting and authentication.** Doc 02 defers auth. What's the minimal auth model for a local-first system? (Token-based? mTLS? IP whitelist?) What rate limiting makes sense for a Pi 4? HA uses long-lived access tokens with a creation UI.

#### Platforms / prior art to survey
- Home Assistant REST API and WebSocket API
- OpenHAB REST API
- EventStoreDB HTTP API and subscription protocol
- Matter Interaction Model
- Hubitat Maker API
- SmartThings API
- GraphQL for IoT (any examples?)

---

### Research 8: Device Model Implementation — Sealed Hierarchy Expansion and AttributeValue Extensions
**Target milestone:** M4 (Device Model implementation)
**Priority:** HIGH — directly feeds M4 coding instructions
**Estimated research effort:** 5-7 hours

#### Context

Research 2 produced REC-01 through REC-10. Before we commit to amendments, we need deeper analysis of the code-level implications. This research is the "§7 Code-Level Implications" that Research 2 deferred.

#### Specific questions to answer

1. **EntityCategory enum placement and projection impact.** REC-01 says "add EntityCategory." Where exactly? On `Entity` (device-model module)? On `EntityState` (state-store module)? Both? What event carries it? `entity_registered` already exists — does it gain a field, or is there a separate `entity_category_set` event? What projection logic changes? How does the REST API filter by category?

2. **QuantityValue design space.** REC-03 proposes `QuantityValue(double value, String unitSymbol, QuantityDimension dimension)`. But: should `dimension` be a sealed enum or an open string? JSR 385 (Units of Measurement) is the Java standard — what's the adoption cost? Is there a lighter alternative? What about unit conversion at projection time vs adapter time? OpenHAB's QuantityType wraps `javax.measure.Quantity<T>` — is this the right model for a constrained runtime?

3. **ArrayValue implications for event schema.** REC-05 proposes `ArrayValue`. What events does this affect? `attribute_changed` currently carries a single `AttributeValue`. If the value is an array, is it the whole array or a delta (add/remove/reorder)? What about deeply nested structures? Matter's list-typed attributes (PartsList, GroupKeyMap) — how are updates expressed? Full replacement? Individual mutations?

4. **SemanticTag vs labels.** REC-04 proposes `SemanticTag(namespace, value)`. How does this interact with existing `labels: List<String>`? Should labels be migrated to `SemanticTag(namespace="user", value=label)`? What Matter namespaces should be reserved? What's the adapter contract — does the Zigbee adapter emit semantic tags, or only the Matter adapter?

5. **The `reachable` boolean lifecycle.** REC-02 proposes `reachable: boolean` distinct from `stale`. What event carries reachability changes? `device_reachable_changed(deviceId, reachable, at)` — but is this a device-level or entity-level concept? HA has per-entity `available`. Matter has per-endpoint `Reachable` on Bridged Device Basic Info (device-level, not endpoint-level). Which is correct for HomeSynapse?

6. **Sealed hierarchy versioning strategy.** The Capability sealed hierarchy has 15 permits + CustomCapability. When we add permits (per Research 2's "expect 25-30"), every exhaustive `switch` breaks at compile time. What's the migration strategy? Do we add all anticipated permits at once (batch), or one at a time as adapters need them? What about backward compatibility for stored events that reference capabilities by name?

#### Platforms / prior art to survey
- Matter Application Cluster Spec (attribute types, list semantics)
- JSR 385 (Units of Measurement) API and implementation (Indriya)
- OpenHAB QuantityType implementation
- Home Assistant device_class and entity_category source code
- Jackson polymorphic serialization patterns for sealed types

---

## 2. Research Execution Protocol

### How to Issue a Research Brief to the Claude Project

Each research item above becomes a self-contained prompt to the Claude Project. The prompt format:

```
RESEARCH BRIEF: Research {N} — {Title}

You are the PM/architect for HomeSynapse Core, a local-first event-sourced
smart home runtime in Java 21. Your task is to produce a research document
following the exact format specified below.

[Paste the "Mandatory Format" from §0 of this document]

SCOPE: [Paste the "Specific questions to answer" section for this research item]

PLATFORMS TO SURVEY: [Paste the "Platforms / prior art to survey" list]

CONTEXT YOU NEED:
- HomeSynapse Core Knowledge Primer (uploaded to project knowledge)
- HomeSynapse Current State (uploaded to project knowledge)
- [Any additional design docs relevant to this research item]

CONSTRAINTS:
- Take positions. "X is worth investigating" is banned.
- Cite primary sources (docs, issue trackers, maintainer statements) with URLs.
- Every REC must include effort estimate in lines of code.
- Number RECs globally: Research 2 used REC-01 through REC-12.
  This document starts at REC-{next}.
- Include §7 (Code-Level Implications) — specific Java records, interfaces,
  events, module-info changes.
- **Use the verbatim type and module identifiers embedded below. Do not
  paraphrase package names, module names, or type names.** Prior research
  documents fabricated type names (Research 3/4/8 §7) and module names
  (Research 6 §7.8) when these were not embedded verbatim — same failure
  mode, different layer of the cake. Both layers must be embedded.

VERIFIED IDENTIFIERS YOU MUST USE:
- For every module the research touches, embed the verbatim contents of
  `{module-path}/src/main/java/module-info.java` here. The JPMS module name
  (e.g., `com.homesynapse.state`, NOT `com.homesynapse.state.store`) and the
  exact `requires` / `requires transitive` / `exports` directives are
  authoritative — do not paraphrase, do not infer from Knowledge Primer
  summaries.
- For every module the research touches, embed the verbatim
  `MODULE_CONTEXT.md` §"Complete Type Inventory" (or equivalent) here. Use
  these type names exactly — do not abbreviate, pluralize, or rename.

OUTPUT: A single markdown document following the mandatory format.
Do not truncate. Produce the complete document.
```

### Execution Order

```
Research 3 (Integration Testing)     ← IMMEDIATE  — blocks M3.7 coding instruction
Research 8 (Device Model Impl)       ← NEXT       — feeds M4 amendment decisions
Research 4 (Automation Engine)       ← HIGH        — longest lead, influences M4-M6
Research 6 (Integration Runtime)     ← MEDIUM      — influences IntegrationContext
Research 5 (Configuration System)    ← MEDIUM      — feeds M6
Research 7 (REST/WebSocket API)      ← LOW-MEDIUM  — long lead, can wait
```

Research 3 should be executed before M3.7 scoping begins. Research 8 should be executed before M4 amendment deliberation. Research 4 should be executed as early as possible because its findings influence M4/M5/M6 scope.

### How Findings Feed Back

Each completed research document produces:
1. **Amendment candidates** (REC-XX) that Nick evaluates for scope inclusion.
2. **Concept mapping tables** that the PM uses when writing coding instructions.
3. **Pain-point citations** that validate (or invalidate) our design decisions.
4. **Code-level implications** that accelerate PM coding instruction production.

The PM's job after each research document lands:
- Read the executive summary verdicts.
- Evaluate each REC for inclusion in the target milestone.
- Update the phase-3-milestone-backlog with any new sub-WUs.
- Update Knowledge Primer and Current State if findings change the architectural narrative.

---

## 3. Research 2 Assessment — What It Got Right, What's Missing

### What Research 2 Got Right

1. **The staleAfter competitive assessment is rigorous.** The qualifying language — "no other surveyed platform formalizes staleness as a first-class, read-time-derived property orthogonal to availability" — is the correct framing. The HA `expire_after` acknowledgment is honest and strengthens the claim.

2. **Device replacement analysis is the strongest section.** The Frenck quotation from architecture#1088 is devastating for HA's position. HomeSynapse's `DeviceReplacementService` + INV-CS-02 is genuinely differentiated. The 8 replacement scenarios (§3.5) are the right validation framework.

3. **The concept mapping table (§3.1) is production-quality.** 25 rows covering every major abstraction. This table alone saves hours of PM deliberation when writing M4 coding instructions.

4. **Amendment recommendations are well-ranked.** The (impact × confidence) / cost ranking is the right formula. REC-01 (EntityCategory) is correctly ranked #1 — highest impact, lowest cost, no controversy.

### What Research 2 Is Missing (and What Subsequent Research Must Cover)

1. **No analysis of event schema implications.** Research 2 recommends adding `EntityCategory`, `reachable`, `QuantityValue`, `SemanticTag`, `ArrayValue` — but doesn't specify what domain events change, what new events are needed, or how the projection logic adapts. This is Research 8's job.

2. **No automation engine implications.** The Expectation hierarchy and ConfirmationPolicy assessment (§3.3) is thin. "SHIP AS-IS" with "instrument adapter-friction metric" is a holding pattern, not a decision. Research 4 must go deeper.

3. **No configuration system analysis.** Doc 02's configuration model (YAML + JSON Schema + AES-256-GCM secrets) is mentioned only in passing. Research 5 fills this gap.

4. **No integration runtime lifecycle analysis.** REC-08 touches the surface (Reauth, Reconfigure, OptionsFlow) but doesn't analyze the supervisor patterns, health FSM, or crash isolation that M9 needs. Research 6 fills this gap.

5. **No testing pattern analysis.** M3.7 is the immediate next milestone and Research 2 provides zero guidance on how to test the full stack. Research 3 fills this gap.

6. **"Research 1: Event Sourcing Battle Scars" is referenced but not on disk.** It was apparently provided in a prior conversation. It should be committed to `homesynapse-core-docs/research/` so future sessions can reference it. If it covered event store design patterns, schema evolution, and projection rebuilds, that's foundational context for Research 3 and Research 8.

---

## 4. Cross-Research Dependencies

```
Research 2 (Entity Modeling) ──────────────► Research 8 (Device Model Impl)
    │                                              │
    │ REC-01..REC-10 feed                          │ Code-level implications feed
    ▼                                              ▼
Research 4 (Automation Engine) ◄────────── M4 Amendment Decisions
    │
    │ Trigger/condition/action
    │ requirements constrain
    ▼
Research 5 (Configuration) + Research 6 (Integration Runtime)
    │
    │ Config + adapter lifecycle feed
    ▼
Research 7 (REST/WebSocket API)
    │
    │ API shape validates upstream decisions
    ▼
M10/M11 Implementation

Research 3 (Integration Testing) ──► M3.7 Implementation (independent path)
```

Research 3 is independent and should execute first. Research 8 depends on Research 2 (already complete). Research 4 should execute before Research 5 and 6 because automation requirements constrain both config and integration runtime design.

---

## Addendum — Research 9 & 10 (added 2026-05-28, M4 Workstream A)

The original queue (Research 2–8) covered event model, device model, automation, config, integration runtime, and API. M4 scoping surfaced one area never given dedicated research: the **projection/derivation foundation** (M4.0b — the real `DerivationRule` + `DispatchingProjectionAdvancer` + the one-shot backfill on the `projectionVersion` 1→2 reconciliation replay). Two briefs close that gap; both target M4 Workstream A and follow the mandatory format above.

- **Research 9 — Event-Sourced Projection Rebuild, Versioning, and Backfill.** Brief: `context/instructions/Research_9_Projection_Rebuild_Backfill_Brief.md`. RECs start at **REC-76**. Surveys Axon / EventStoreDB / Marten / Akka Projections / Home Assistant restore. Informs the backfill-gating mechanism, snapshot-store activation threshold, determinism discipline, and idempotency-cursor safety. **Introduce first** into the M4 plan-verification window.
- **Research 10 — Typed Attribute Change-Detection Semantics.** Brief: `context/instructions/Research_10_Typed_Attribute_Change_Detection_Brief.md`. RECs start at **REC-90** (a deliberate gap from Research 9 to avoid the AMD-44/45-style numbering collision while both run in parallel; PM reconciles at assessment). Surveys HA `significant_change`, Matter/ZCL reportable-change, PI swinging-door. Informs per-type comparison policy, the deadband decision, and the typed-vs-string `StateChangedEvent` payload question. **Introduce second** (it refines a detail inside the structure Research 9 settles).

Both briefs embed the source-verified HomeSynapse type inventory and an explicit "VERIFY, don't invent" rule — the standing counter-measure to the §7 type-name fabrication seen in Research 3/4/6/7/8.

---

**Last updated:** 2026-05-28 (Research 9 & 10 added for M4 Workstream A)
