<!--
file: context/instructions/Research_8_Device_Model_Brief.md
purpose: Self-contained prompt for the Claude Project to produce Research 8.
audience: Nick (paste into Claude Project conversation)
state-type: ephemeral
-->

# RESEARCH BRIEF: Research 8 — Device Model Implementation: Sealed Hierarchy Expansion and AttributeValue Extensions

You are the PM/architect for HomeSynapse Core, a local-first event-sourced smart home runtime in Java 21 targeting Raspberry Pi 4/5. Your task is to produce a research document following the exact format specified below.

## Mandatory Format

Every research document must follow this structure. Non-negotiable sections are marked **[M]**; optional sections are marked **[O]**.

```
# Research 8: {Title} — {Subtitle}

*Target: HomeSynapse Core M4. Date: YYYY-MM-DD.*

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
  - REC-XX format. Numbered globally: Research 3 used REC-13 through REC-22.
    This document starts at REC-23.

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

Research 2 produced REC-01 through REC-10, covering EntityCategory, reachable boolean, QuantityValue, SemanticTag, ArrayValue, and Capability hierarchy expansion at the conceptual level. Before we commit to amendments, we need deeper analysis of the code-level implications. This research is the "§7 Code-Level Implications" that Research 2 deferred.

### Specific questions to answer

1. **EntityCategory enum placement and projection impact.** REC-01 says "add EntityCategory." Where exactly? On `Entity` (device-model module)? On `EntityState` (state-store module)? Both? What event carries it? `entity_registered` already exists — does it gain a field, or is there a separate `entity_category_set` event? What projection logic changes? How does the REST API filter by category?

2. **QuantityValue design space.** REC-03 proposes `QuantityValue(double value, String unitSymbol, QuantityDimension dimension)`. But: should `dimension` be a sealed enum or an open string? JSR 385 (Units of Measurement) is the Java standard — what's the adoption cost? Is there a lighter alternative? What about unit conversion at projection time vs adapter time? OpenHAB's QuantityType wraps `javax.measure.Quantity<T>` — is this the right model for a constrained runtime?

3. **ArrayValue implications for event schema.** REC-05 proposes `ArrayValue`. What events does this affect? `attribute_changed` currently carries a single `AttributeValue`. If the value is an array, is it the whole array or a delta (add/remove/reorder)? What about deeply nested structures? Matter's list-typed attributes (PartsList, GroupKeyMap) — how are updates expressed? Full replacement? Individual mutations?

4. **SemanticTag vs labels.** REC-04 proposes `SemanticTag(namespace, value)`. How does this interact with existing `labels: List<String>`? Should labels be migrated to `SemanticTag(namespace="user", value=label)`? What Matter namespaces should be reserved? What's the adapter contract — does the Zigbee adapter emit semantic tags, or only the Matter adapter?

5. **The `reachable` boolean lifecycle.** REC-02 proposes `reachable: boolean` distinct from `stale`. What event carries reachability changes? `device_reachable_changed(deviceId, reachable, at)` — but is this a device-level or entity-level concept? HA has per-entity `available`. Matter has per-endpoint `Reachable` on Bridged Device Basic Info (device-level, not endpoint-level). Which is correct for HomeSynapse?

6. **Sealed hierarchy versioning strategy.** The Capability sealed hierarchy has 15 permits + CustomCapability. When we add permits (per Research 2's "expect 25-30"), every exhaustive `switch` breaks at compile time. What's the migration strategy? Do we add all anticipated permits at once (batch), or one at a time as adapters need them? What about backward compatibility for stored events that reference capabilities by name?

7. **(NEW — from Research 3 findings) MinimalProjectionAdvancer extension strategy.** M3.7 ships a `MinimalProjectionAdvancer` in `core/state-store` handling exactly 3 event types (`entity_registered`, `state_changed`, `device_registered`) with last-write-wins merge semantics and `AdvanceResult.skipped()` for unhandled events. Given this starting point, what is the correct extension pattern for M4? Should M4 modify the existing advancer (add handlers for new event types like `entity_category_set`, `device_reachable_changed`), replace it with a richer implementation, or use a chain-of-responsibility / composite pattern where advancers compose? What event types beyond the initial 3 does the advancer need to handle for M4's entity modeling features (EntityCategory, reachable boolean, SemanticTag, etc.)? What is the impact on the existing `ProjectionAdvancer` SPI?

### Platforms / prior art to survey
- Matter Application Cluster Spec (attribute types, list semantics, Semantic Tag cluster)
- JSR 385 (Units of Measurement) API and implementation (Indriya)
- OpenHAB QuantityType implementation and UoM architecture
- Home Assistant device_class and entity_category source code (core and frontend)
- Jackson polymorphic serialization patterns for sealed types in Java 21
- Marten projection advancer patterns (for question 7 — projection extension strategies)
- Axon event upcasting (for sealed hierarchy versioning — question 6)

---

## CONTEXT YOU NEED

- HomeSynapse Core Knowledge Primer (uploaded to project knowledge)
- HomeSynapse Current State (uploaded to project knowledge)
- Research 2 findings (REC-01 through REC-10) — the conceptual recommendations this research provides code-level grounding for

### Key context from Research 3 (completed, processed by PM):

Research 3 (Integration Testing, REC-13 through REC-22) was accepted by the PM. Key findings relevant to Research 8:

- **REC-20 (ACCEPTED for M3.7):** `MinimalProjectionAdvancer` ships in `core/state-store` handling `entity_registered`, `state_changed`, `device_registered`. This is production code — the starting point that M4 extends.
- **OR-M3-17 (`NO_OP_DERIVATION`)** remains open. The `Function.identity()` derivation function stays as a placeholder through M3.7. Derived events are M4 scope — Research 8 should address when derivation logic ships and what events it produces.
- **OR-M3-18 (`NO_OP_ADVANCER`)** is resolved by REC-20.
- **The `ProjectionAdvancer` SPI** is: `advance(fromPosition, maxRows) → AdvanceResult`, ≤500 rows per call, ≤2 s read transaction, bounded-window contract (close/reopen transaction between chunks to prevent WAL growth).

### Key architectural constraints:
- `AttributeValue` is a sealed hierarchy in `device-model` (`com.homesynapse.device`). Any new permits (QuantityValue, ArrayValue) affect exhaustive switches across the codebase.
- `Entity` is the atomic addressable unit, NOT `Device`. All state events target `EntityId`. A Device groups Entities.
- `EntityState` has 9 fields (9th is `stale`, derived at read time from `staleAfter + Clock`).
- The event model lives in `com.homesynapse.event` (event-model module). Domain event payload records are defined here.
- Jackson serialization of events uses `EventTypeRegistry + PersistenceJacksonModule + DegradedEvent` fallback (LTD-19).
- The V001 events table has 25 columns. V002 adds dead_letters. V003 adds snapshots. Any new schema changes would be V004+.

---

## CONSTRAINTS

- Take positions. "X is worth investigating" is banned.
- Cite primary sources (docs, issue trackers, maintainer statements) with URLs.
- Every REC must include effort estimate in lines of code.
- Number RECs globally: Research 3 used REC-13 through REC-22. This document starts at **REC-23**.
- Include §7 (Code-Level Implications) — this is MANDATORY for Research 8. Specify exact Java records, interfaces, sealed hierarchy changes, event schema additions, module-info changes, and any V00x migration implications.
- For each proposed type change, specify: (a) the exact module, (b) the exact package, (c) public vs package-private visibility, (d) whether it requires an AMD (amendment to a Phase 2 interface).
- For sealed hierarchy changes (AttributeValue, Capability), specify the exact `permits` clause change and assess the compile-time impact on downstream switches.

---

## OUTPUT

A single markdown document following the mandatory format above. Do not truncate. Produce the complete document. Target length: comparable to Research 3 (~640 lines).
