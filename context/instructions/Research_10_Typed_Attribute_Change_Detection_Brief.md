# Research 10 Brief — Typed Attribute Change-Detection Semantics for State Derivation

*Target: HomeSynapse Core M4 (Workstream A — WU M4.0b-2; Workstream B — WU M4.B3 AttributeValue expansion). Hand this to the research surface. Output must follow the mandatory research format below.*

## Why this research exists

M4's production `DerivationRule` derives a `state_changed` event when an inbound `state_reported` changes an entity's canonical attribute value. The existing change-detect logic (the `EchoStateRule` test fixture) is **string-only**: it stringifies values via `rawValue().toString()` and compares strings. M4 simultaneously expands the `AttributeValue` sealed hierarchy (Research 8 REC-24/27/29 add `QuantityValue`, `ArrayValue`, `DegradedAttributeValue`). String comparison of typed values is both lossy and noisy — `21.0` vs `21.00`, a `QuantityValue` with the same magnitude in different units, or float jitter all produce wrong "changed/unchanged" verdicts, and every spurious `state_changed` will (once automation arrives in M7) wake triggers incorrectly. We need defined, deterministic, typed change-detection semantics before M4.0b-2 is briefed. This was never a research topic; it's a concrete design gap.

## The questions (what we need answered)

1. **Per-type "changed" semantics.** For each `AttributeValue` permit, what is the right definition of "the value changed"?
   - `BooleanValue`, `EnumValue`, `StringValue`: presumably exact equality — confirm and note edge cases (case, whitespace, null).
   - `IntValue`: exact.
   - `FloatValue`: exact, or with an epsilon/tolerance? NaN handling? `-0.0` vs `0.0`?
   - `QuantityValue` (magnitude + unit): unit normalization before comparison? A tolerance/deadband? Is `21.0°C` "changed" from `21.001°C`? From `294.15 K`?
   - `ArrayValue` (full-replacement semantics per REC-27): element-wise equality, order-sensitive? Size-then-content? Deep vs shallow?
   - `DegradedAttributeValue` (the fallback for un-deserializable values): does it ever count as a change, or is it inert?
2. **Deadband / hysteresis / significant-change.** Smart-home sensors report continuously (temperature every N seconds). Should change-detection apply a **deadband** (suppress sub-threshold deltas) and/or **hysteresis**, and should that be **per-attribute-configurable** (a deadband declared on the capability/attribute schema) or a global policy? What do real platforms do, and what are the failure modes (missed real changes vs. event storms)?
3. **Determinism constraints.** The comparison runs inside the projection's READ phase and **re-executes on every replay** (AMD-41 §3.2.2) — so it must be a pure, clock-independent, deterministic function of (prior canonical value, inbound reported value). What change-detection techniques violate determinism (e.g., time-based deadbands, rate-of-change windows, "report at most every N seconds") and how do systems keep significant-change logic deterministic and replay-safe?
4. **Typed vs. serialized comparison + event payload shape.** Today `StateChangedEvent` carries `oldValue`/`newValue` as **Strings** and the rule stringifies before comparing. Should change-detection compare **typed** `AttributeValue`s (then serialize for the event), and should `StateChangedEvent` carry typed values or remain string-valued? Trade-offs for correctness, storage, and downstream consumers (conditions/triggers in M7).
5. **Unit handling.** For `QuantityValue`, is there a canonical-unit normalization step (and where does it live — the rule, the capability schema, a units library)? What does the smart-home world do about unit drift between adapters reporting the same physical quantity?
6. **Floating-point and rounding discipline.** Across the float/quantity cases: comparison epsilon vs. display rounding vs. stored precision — keep these distinct and recommend a single coherent policy.

## Platforms / prior art to survey (primary sources required)

At least: **Home Assistant** — its `significant_change` component / `async_check_significant_change` per-domain logic (this is the closest direct analog: HA explicitly computes whether a state change is "significant" per device class, with per-domain tolerances), plus its state-vs-attributes model. **Matter** — attribute reporting: "reportable change," min/max reporting intervals, the quantization of reportable change. **Zigbee (ZCL)** — `Configure Reporting` with `reportable change` thresholds per attribute. **Z-Wave** — reporting/threshold configuration. **Time-series historians** — OSIsoft PI **swinging-door / exception+compression deadband**, InfluxDB/Prometheus delta/`changes()` semantics — for the mature theory of "is this a meaningful change." Optional: Kafka/Debezium change-data-capture dedup, and any units library prior art (`javax.measure` / Unit-API / Indriya) for the unit-normalization question — note that adding a units dependency is governed by LTD-10 (version-catalog amendment process), so flag dependency implications.

For each: how it defines a significant/reportable change, ≥1 primary-source quote + URL, known pain points (storms, missed changes, locale/precision bugs), and the specific HomeSynapse lesson.

## Verified HomeSynapse context — use these EXACT facts; do not invent type names

(Prior research repeatedly fabricated type names without source access. Ground everything here. Anything beyond this list: write "VERIFY against source," do not invent.)

- **`AttributeValue`** is a sealed interface in `core/device-model` (`com.homesynapse.device`). Source-verified real permits (5): `BooleanValue`, `IntValue`, `FloatValue`, `StringValue`, `EnumValue`. (`LongValue`/`DoubleValue`/`InstantValue`/`JsonValue` are **phantom** — they do not exist.) M4 adds, per Research 8 (Nick-source-verified): `QuantityValue`, `ArrayValue` (full-replacement semantics — non-negotiable), and `DegradedAttributeValue` (**public**, the subtype-level fallback for un-deserializable values, paralleling `DegradedEvent`). An `AttributeValueUpcaster` SPI (REC-29) handles versioning.
- **`DerivationRule`** (`@FunctionalInterface`, `core/state-store`): `List<EventDraft> evaluate(DerivationContext context)`. The `DerivationContext` carries prior `EntityState` + inbound `EventEnvelope` + injected `Clock`. The rule MUST be deterministic (INV-PROJ-01), MUST NOT call `EventPublisher.publish` or mutate the `StateStore`, and SHOULD inherit `eventTime` from the causing envelope (never `Instant.now()`).
- **Current change-detect reference** (`EchoStateRule`, testFixtures): if inbound is `StateReportedEvent`, look up the prior canonical value for the attribute key, compare; if unequal, emit a `StateChangedEvent`. Today `lookupAttribute` stringifies via `(v instanceof StringValue sv) ? sv.value() : v.rawValue().toString()` and the comparison is `Objects.equals(oldString, newString)`.
- **`StateChangedEvent`** (`com.homesynapse.event`) currently carries `attributeKey`, `oldValue`, `newValue` (Strings), and the causing `EventId`. Whether it should carry typed values is **in scope for this research** (question 4).
- **`applyToState`**: writes attributes only on `state_changed`, via `newAttrs.put(key, new StringValue(value))` — i.e., the materialized attribute is currently stored as `StringValue` regardless of source type. Whether the materialized store should preserve typed values is related to question 4.
- **`EntityState.stateVersion`** advances on every processed event (idempotency cursor) — a spurious `state_changed` inflates it and produces noise, so over-reporting is a real cost, not just cosmetic.
- Capability/attribute metadata lives on **`Entity.capabilities` (`List<CapabilityInstance>`)** — `CapabilityInstance` wraps feature map, version, namespace, **attributes schema**, commands, confirmation policy. If a per-attribute deadband is recommended, this schema is the likely home for it (VERIFY the exact `CapabilityInstance` shape against source before proposing a field).

## Constraints on the output

- Follow the mandatory format below. Every factual claim traceable to §6 sources.
- **REC numbering starts at REC-90** (Research 9 runs in parallel and provisionally holds REC-76–89; the PM reconciles any overlap at assessment — deliberately leaving a gap to avoid the kind of numbering collision M4 is already untangling). Each REC: gap citation, lesson source, the specific change (comparison policy / schema field / event-payload shape), backward-compat assessment, effort, and target WU (M4.0b-2 / M4.B3).
- The recommended change-detection policy must be **deterministic and replay-safe** — explicitly reject any technique that depends on wall-clock, processing rate, or external state. Call this out in §5.
- Keep three things distinct and recommend one coherent policy for each: **comparison epsilon** (is it a change?), **stored precision** (what we materialize), **display rounding** (not our concern, but say so to avoid conflation).
- Surface any conflict with the verified inventory in §5 rather than silently breaking it. Flag dependency implications (LTD-10) if a units library is recommended.

## Mandatory research format

```
# Research 10: Typed Attribute Change-Detection Semantics for State Derivation — {subtitle}
*Target: HomeSynapse Core M4 (M4.0b-2 / M4.B3). Date: YYYY-MM-DD.*

## 1. Executive Summary [M]   — 5–8 verdict bullets, each a bold claim + one-sentence defense; flag the single highest-impact finding (likely: per-type policy + whether deadbands are in-scope for M4 or deferred).
## 2. Platform / Literature Deep Dives [M]   — HA significant_change, Matter reportable-change, ZCL Configure Reporting, Z-Wave, PI swinging-door, (optional) units libraries; each with primary-source quote + URL, pain points, HomeSynapse lesson.
## 3. Cross-Cutting Analysis [M]   — concept-mapping table (HomeSynapse AttributeValue type | HA device-class tolerance | Matter reportable change | ZCL reportable change | time-series deadband); gap analysis; over-abstraction analysis (is per-attribute deadband worth it for MVP, or is exact-equality-with-float-epsilon enough?); competitive assessment.
## 4. Amendment Recommendations [M]   — REC-90+ ; the per-type comparison policy, the typed-vs-string payload decision, the deadband decision (in-M4 vs deferred to a later tier), and the unit-normalization decision should each yield a concrete REC.
## 5. Caveats and Open Questions [M]   — determinism rejections; what needs Nick's call (e.g., per-attribute deadband config) vs. what the literature settles; dependency (LTD-10) implications.
## 6. Appendix: Sources [M]
## 7. HomeSynapse Code-Level Implications [O]   — the concrete comparison function per AttributeValue permit, the StateChangedEvent payload shape, where deadband config lives if recommended, MODULE_CONTEXT impact.
```
