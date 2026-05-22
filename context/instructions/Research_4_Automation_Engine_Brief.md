<!--
file: context/instructions/Research_4_Automation_Engine_Brief.md
purpose: Self-contained prompt for the Claude Project to produce Research 4.
audience: Nick (paste into Claude Project conversation)
state-type: ephemeral
-->

# RESEARCH BRIEF: Research 4 — Automation Engine Architecture: Trigger/Condition/Action Pipeline Design

You are the PM/architect for HomeSynapse Core, a local-first event-sourced smart home runtime in Java 21 targeting Raspberry Pi 4/5. Your task is to produce a research document following the exact format specified below.

## Mandatory Format

Every research document must follow this structure. Non-negotiable sections are marked **[M]**; optional sections are marked **[O]**.

```
# Research 4: {Title} — {Subtitle}

*Target: HomeSynapse Core M7/M8. Date: YYYY-MM-DD.*

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
  - REC-XX format. Numbered globally: Research 8 used REC-23 through REC-30.
    This document starts at REC-31.

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
  - Migration considerations (V00x).
```

---

## SCOPE

The automation engine is the *consumer* of every upstream subsystem. Decisions we make in M4 (device model), M5 (platform API), and M6 (configuration) are constrained by what the automation engine needs. Research 2 already surfaced this: REC-07 (ConfirmationPolicy.NONE) and the Expectation hierarchy assessment both depend on understanding how automations will *use* commands. If we build M4-M6 without understanding M7's requirements, we'll need amendments.

Doc 02 already defines the sealed hierarchies (Selector, TriggerDefinition, ConditionDefinition, ActionDefinition) and the behavioral contracts (AMD-03 positional state snapshots, AMD-04 cascade depth limiting, AMD-31 command execution ordering). What's missing is empirical validation against production automation systems.

### Specific questions to answer

1. **Trigger evaluation models.** How does Home Assistant evaluate triggers? (State triggers, event triggers, time triggers, template triggers, webhook triggers.) How does OpenHAB evaluate rules? (JSR 223 scripting, Blockly, DSL.) How does NodeRED evaluate flows? What's the canonical "motion sensor → turn on light for 5 minutes → turn off" pattern in each? How do they handle re-triggering during the active period? Doc 02's `TriggerDefinition` sealed hierarchy has 8 permits — are there trigger types we're missing?

2. **Condition evaluation timing.** HA evaluates conditions *at trigger time*. OpenHAB rules evaluate conditions inline. Does anyone evaluate conditions *at action time* (i.e., re-check just before executing)? AMD-03's "positional state snapshots" approach is unusual — validate it against real-world automation patterns. What failure modes does each timing model produce?

3. **Command confirmation and the Pending Command Ledger.** Research 2 §3.3 flagged the 4-type Expectation hierarchy as unique. Go deeper: how does HA handle "I sent dimmer to 50% but it's at 48%"? (Answer: it doesn't — fire and forget.) How does Matter handle command confirmation? (Timed commands, interaction model.) How does Z-Wave handle command confirmation? (Supervision CC.) What percentage of real automations actually need confirmation? Is the Pending Command Ledger over-engineered, or is it the right abstraction for reliable home automation?

4. **Cascade governance.** AMD-04 limits cascade depth. How do HA, OpenHAB, and NodeRED handle automation-triggers-automation chains? Are infinite loops a real production problem? What's the failure mode? HA has `max_exceeded` on `repeat` — is that sufficient? What about cross-automation cascades (Automation A triggers state change → Automation B fires)?

5. **Temporal triggers and the clock.** AMD-25 introduced temporal-duration trigger modifiers. How do HA, OpenHAB handle "motion detected for 5 minutes" vs "motion detected, wait 5 minutes, then act"? The `for:` modifier in HA vs OpenHAB's `changed ... for` — what edge cases do they produce? How does clock injection (DEC-M3-09) interact with temporal trigger testing?

6. **Scene/routine/script abstraction.** HA has Scripts (reusable action sequences), Scenes (state snapshots to restore), and Automations (trigger→condition→action). OpenHAB has Rules, Scenes, and Profiles. Doc 02 has only Automations. Is a separate Scene primitive needed, or is it an automation that fires on command with no trigger? What about "routines" (HA helpers, Google Home routines)?

7. **Rule storage and versioning.** How are automations persisted? HA uses YAML + UI-generated JSON. OpenHAB uses file-based + REST API. How do they handle versioning, undo, and debugging? Doc 02's event-sourced approach means automation definitions are themselves events — what does `automation_created`, `automation_updated`, `automation_disabled` event schema look like?

8. **(NEW — from Research 8 findings) EntityCategory interaction with automations.** Research 8 (REC-23) adds `EntityCategory { PRIMARY, CONFIG, DIAGNOSTIC }` to the Entity record. How should automations interact with entity categories? Should DIAGNOSTIC entities be excluded from automation triggers by default (as HA excludes them from cloud/voice assistants)? Should the `Selector` sealed hierarchy support category-based filtering?

9. **(NEW — from Research 8 findings) SemanticTag-based automation selectors.** Research 8 (REC-26) replaces `labels: List<String>` with `tags: List<SemanticTag>`. How should automations use semantic tags for entity selection? HA uses `labels` in automations for grouping (e.g., "all entities with label 'outdoor'"). Should `Selector` support tag-namespace-aware filtering (e.g., "all entities tagged hs.user:outdoor")?

10. **(NEW — from Research 8 findings) DeviceReachableChanged as an automation trigger.** Research 8 (REC-25) adds a device-level `device_reachable_changed` event. How should automations trigger on reachability changes? Use cases: "when the Zigbee bridge goes offline, send a notification"; "when a device comes back online, re-sync its state." Is this a new `TriggerDefinition` permit, or handled by the existing event-trigger mechanism?

11. **(NEW — from Research 8 findings) Automation event types for the projection advancer.** Research 8 (REC-28) introduces a `DispatchingProjectionAdvancer` with a handler-per-event-type pattern. If automations produce events (`automation_triggered`, `automation_completed`, `automation_failed`, `automation_created`, `automation_updated`, `automation_disabled`), each needs a `ProjectionEventHandler`. Enumerate the complete set of automation event types and their payload schemas. Which of these events need projection handlers (state-changing) vs which are observability-only (no projection impact)?

### Platforms / prior art to survey
- Home Assistant automations (core architecture, trigger/condition/action evaluation, Scripts, Scenes)
- OpenHAB rules (JSR 223, DSL, Blockly, rule engine internals)
- NodeRED flow evaluation model
- Apple HomeKit automation model
- Google Home routines
- Zigbee2MQTT automations (if any native)
- Matter 1.4 Scenes cluster
- Academic: ECA (Event-Condition-Action) rule systems literature

---

## CONTEXT YOU NEED

- HomeSynapse Core Knowledge Primer (uploaded to project knowledge)
- HomeSynapse Current State (uploaded to project knowledge)
- Research 2 findings (REC-01 through REC-10) — the conceptual entity model recommendations
- Doc 02 (Device Model & Capability System) — defines the Selector, TriggerDefinition, ConditionDefinition, ActionDefinition sealed hierarchies

### Key context from Research 8 (completed, processed by PM):

Research 8 (Device Model Implementation, REC-23 through REC-30) was processed by the PM. Key findings relevant to Research 4:

- **REC-23 (ACCEPTED for M4.0):** `EntityCategory { PRIMARY, CONFIG, DIAGNOSTIC }` added to Entity record. Category is a registry property set at registration time, NOT mutable state. Carried on the existing `entity_registered` event (extended with nullable `category` field).

- **REC-25 (ACCEPTED for M4.0):** `device_reachable_changed(DeviceId, boolean reachable, Instant at)` event at the DEVICE level (not entity level). Entities inherit unreachability transitively at read time via the projection. This is a new event type that automations may want to trigger on.

- **REC-26 (MODIFIED + ACCEPTED for M4.0):** `SemanticTag(namespace, value)` replaces `labels: List<String>` on `Entity`. Reserved namespaces: `matter.common`, `matter.device.{type}`, `hs.user`, `hs.system`. User labels become `SemanticTag("hs.user", label)`. This affects how automations select entities by tag.

- **REC-28 (MODIFIED + ACCEPTED for M4.0):** `DispatchingProjectionAdvancer` replaces `MinimalProjectionAdvancer`. Map-based dispatch by event type string. Constructor-injected handlers (NOT ServiceLoader — per DECIDE-04). Each new event type in the system needs a `ProjectionEventHandler` implementation. Automation event types need handlers too.

- **OR-M3-17 (NO_OP_DERIVATION):** Stays open through M3.7. Closes at M4.0 when handler-specific derivation functions replace `Function.identity()`. Research 4 should consider whether automation events produce derived state.

### Key architectural constraints:
- The automation module is `core/automation` with package `com.homesynapse.automation` + subpackages.
- 4 sealed hierarchies: Selector (N permits), TriggerDefinition (8 permits), ConditionDefinition (N permits), ActionDefinition (N permits).
- AMD-03: Conditions evaluate against positional state snapshots (`getStatesAtPosition` + `ConsistentSnapshot`).
- AMD-04: Cascade depth limiting (prevents infinite automation loops).
- AMD-25: Temporal-duration trigger modifiers.
- AMD-31: Command execution ordering.
- DEC-M3-09: Clock injection for testability.
- RunStatus has 7 values (INTERRUPTED was added by architecture benchmark).
- DECIDE-04: No ServiceLoader. Factories instantiated directly.
- The event model lives in `com.homesynapse.event`. All domain event payload records are defined here.
- Event naming convention: legacy events use underscore (`entity_registered`); new events use dot-separated namespacing (`device.reachable_changed`). Both patterns are permanent.

---

## CONSTRAINTS

- Take positions. "X is worth investigating" is banned.
- Cite primary sources (docs, issue trackers, maintainer statements) with URLs.
- Every REC must include effort estimate in lines of code.
- Number RECs globally: Research 8 used REC-23 through REC-30. This document starts at **REC-31**.
- Include §7 (Code-Level Implications) — this is MANDATORY for Research 4. Specify exact Java records, interfaces, sealed hierarchy changes, event schema additions, module-info changes.
- For each proposed type change, specify: (a) the exact module, (b) the exact package, (c) public vs package-private visibility, (d) whether it requires an AMD (amendment to a Phase 2 interface).
- **Package name accuracy is critical.** The automation module's package is `com.homesynapse.automation`. The event model is `com.homesynapse.event`. The state store is `com.homesynapse.state`. The device model is `com.homesynapse.device`. The persistence module is `com.homesynapse.persistence`. The rest-api module is `com.homesynapse.api.rest`. Do NOT invent package names. Prior research documents (Research 3 and Research 8) both had systematic package-name errors that required PM correction — do not repeat.
- When enumerating automation event types, specify which events are state-changing (need `ProjectionEventHandler` in the advancer) vs observability-only (no projection impact).
- **Type accuracy is critical.** Use these verified type details:
  - `Entity` (device-model) has 11 fields: `entityId` (EntityId), `entitySlug` (String), `entityType` (EntityType), `displayName` (String), `deviceId` (DeviceId, nullable), `endpointIndex` (int), `areaId` (AreaId, nullable), `enabled` (boolean), `labels` (List\<String\>), `capabilities` (List\<CapabilityInstance\>), `createdAt` (Instant).
  - `EntityState` (state-store) has 9 fields: `entityId`, `attributes` (Map\<String, AttributeValue\>), `availability` (Availability), `stateVersion`, `lastChanged`, `lastUpdated`, `lastReported`, `staleAfter`, `stale` (boolean, derived at read time). EntityState does NOT carry structural entity metadata (category, capabilities, device grouping). `StateQueryService` serves runtime state; the API layer joins structural and runtime data at query time.
  - `AttributeValue` (device-model) is a sealed interface with 5 permits: `BooleanValue`, `IntValue`, `FloatValue`, `StringValue`, `EnumValue`. NOT `BoolValue`, `LongValue`, `DoubleValue`, `InstantValue`, `JsonValue` (those are phantom types from prior research errors).
  - `Availability` (state-store) is an enum: `AVAILABLE`, `UNAVAILABLE`, `UNKNOWN`. Already used by the projection to model entity-level availability.
  - `Capability` (device-model) is a sealed interface with 16 permits (15 standard + `CustomCapability`). The existing standard permits include `Motion`, `Occupancy`, `Contact` among others.
  - `CapabilityInstance` (device-model) wraps capability metadata (featureMap, version, namespace, attributes schema, commands, confirmation policy). Entity carries `List<CapabilityInstance>`, NOT `Set<Capability>`.

---

## OUTPUT

A single markdown document following the mandatory format above. Do not truncate. Produce the complete document. Target length: ~700-800 lines (this is the largest single research item in the agenda).
