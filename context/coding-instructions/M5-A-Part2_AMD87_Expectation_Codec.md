<!--
file: context/coding-instructions/M5-A-Part2_AMD87_Expectation_Codec.md
purpose: Standalone M5-A Part 2 coding instruction — the AMD-87 Expectation persisted codec. Extracted from M5-A_Platform_Impls_AMD87_FloorId.md §Part 2 and un-gated now that AMD-87 is RATIFIED; Parts 1 (platform impls) + 3 (FloorId registration) already shipped in 8028337.
audience: Coder (Claude Code), PM
status: ISSUE-READY — AMD-87 RATIFIED 2026-06-07; Part 2 UN-GATED. Hand to Claude Code.
baseline: homesynapse-core HEAD 8028337 (M5-A Part 1+3 committed; full ./gradlew check GREEN, 147 tasks). Re-verify at issue.
-->

# Coding Task: M5-A Part 2 — AMD-87 `Expectation` Persisted Codec

**Subsystem:** `core/persistence` (codec) + the `persistence → device` JPMS edge
**Design Doc / Amendment:** **AMD-87** (`Expectation` Persisted Sealed-Type Codec — **RATIFIED 2026-06-07**, `design/amendments/AMD-87_Expectation_Persisted_Codec.md`); AMD-87-INV-01 §36 in `Architecture_Invariants_v1.md`; AMD-52 (the bit-anchored-float precedent).
**Phase:** 3-Implementation
**Task Brief Reference:** M5 window charter (`context/planning/weeks/2026-W24_jun08-jun14.md`), lane M5-A. This is the de-gated continuation of `M5-A_Platform_Impls_AMD87_FloorId.md` (Parts 1+3 already committed `8028337`).

## What This Implements

A hand-rolled `Expectation` sealed-type (de)serializer in `core/persistence` so a **command-bearing `CapabilityAdded`** round-trips. A `CapabilityAdded` carrying a full `CapabilityInstance` (AMD-59-INV-02) embeds `CommandDefinition → ExpectedOutcome → Expectation`; `Expectation` has no codec today, so it decodes to `DegradedEvent`. This codec closes that gap and clears the **M9 prerequisite** (M9 must not publish command-bearing `CapabilityAdded` until this lands). **Deliberately small** — codec only; do not expand.

**Already done (do NOT redo):** Part 1 (platform-systemd `PlatformPaths`/`HealthReporter` impls) and Part 3 (`FloorId` registered in `PersistenceJacksonModule`) shipped in `8028337`. **`PersistenceJacksonModule` already imports and registers `FloorId` — do not touch the FloorId line; add only the `Expectation` registrations.**

## Files to Read Before Starting

| File | Why |
|---|---|
| `design/amendments/AMD-87_Expectation_Persisted_Codec.md` | the spec — implement to §2 exactly (RATIFIED) |
| `core/persistence/MODULE_CONTEXT.md` + `src/main/java/module-info.java` | verbatim module-info below; the Jackson-isolation HARD RULE |
| `core/persistence/src/main/java/com/homesynapse/persistence/AttributeValueSerializer.java` + `AttributeValueDeserializer.java` | **the precedent this codec mirrors** — tagged-union `{"t":…,"v":…}`, `Double.doubleToLongBits` bit-anchored float, non-finite sentinels, `−0.0`→`+0.0`, exhaustive no-`default` switch keyed on the interface |
| `core/persistence/src/main/java/com/homesynapse/persistence/PersistenceJacksonModule.java` | the registration site — `addSerializer(AttributeValue.class, …)` at the bottom is where the `Expectation` pair slots in; `FloorId` is **already registered** (line ~84) |
| `core/device-model/src/main/java/module-info.java` | verbatim below — the new `persistence → device` edge target; confirms acyclic |
| `core/device-model/src/main/java/com/homesynapse/device/Expectation.java` + `ExactMatch`/`WithinTolerance`/`EnumTransition`/`AnyChange.java` | the 4 permit shapes the codec serializes (verified shapes below) |
| `core/persistence/src/test/java/com/homesynapse/persistence/EventPayloadCodecTest.java` | the `capabilityAdded_onOff_roundTrips` acceptance test to un-disable — **its annotation literally reads `@Disabled("AMD-65 pending")` at HEAD** (AMD-65 is the *retired* number; just delete the annotation, do not re-number) + `TestEventSamples.capabilityAddedOnOff()` |

### Verbatim `module-info.java` (embedding rule — do not paraphrase module names)

**persistence (current at HEAD `8028337` — this WU adds ONE `requires`):**
```java
module com.homesynapse.persistence {
    requires transitive com.homesynapse.platform;
    requires transitive com.homesynapse.state;
    requires transitive com.homesynapse.event;
    requires transitive com.homesynapse.event.bus;
    requires com.homesynapse.value;
    requires java.sql;
    requires org.slf4j;
    requires com.fasterxml.jackson.core;
    requires com.fasterxml.jackson.databind;
    requires com.fasterxml.jackson.datatype.jsr310;
    requires com.fasterxml.jackson.module.blackbird;
    exports com.homesynapse.persistence;
}
// THIS WU adds:  + requires com.homesynapse.device;
```
**device-model (unchanged — the edge target; confirms acyclic, device does NOT require persistence):**
```java
module com.homesynapse.device {
    requires transitive com.homesynapse.value;
    requires com.homesynapse.event;
    requires transitive com.homesynapse.platform;
    exports com.homesynapse.device;
}
```
The edge is acyclic and good JPMS hygiene: persistence already *reads* device transitively (`persistence → transitive state → transitive device`); this makes that readability direct because persistence now imports `com.homesynapse.device.Expectation` + the 4 permits.

## Files to Create or Modify

| Action | File Path | Description |
|---|---|---|
| MODIFY | `core/persistence/src/main/java/module-info.java` | **+ `requires com.homesynapse.device;`** (the JPMS STOP-gate — verify acyclic at the build gate) |
| CREATE | `core/persistence/src/main/java/com/homesynapse/persistence/ExpectationSerializer.java` | package-private `JsonSerializer<Expectation>` — tagged-union over the 4 permits |
| CREATE | `core/persistence/src/main/java/com/homesynapse/persistence/ExpectationDeserializer.java` | package-private `JsonDeserializer<Expectation>` — reads the `"t"` tag, reconstructs the permit |
| MODIFY | `core/persistence/src/main/java/com/homesynapse/persistence/PersistenceJacksonModule.java` | **+ `addSerializer(Expectation.class, new ExpectationSerializer());` + `addDeserializer(Expectation.class, new ExpectationDeserializer());`** (next to the existing `AttributeValue` pair) **and the `import com.homesynapse.device.Expectation;`**. **Do NOT re-add `FloorId` — it is already registered (Part 3).** |
| MODIFY | `core/persistence/src/test/java/com/homesynapse/persistence/EventPayloadCodecTest.java` | delete the `@Disabled("AMD-65 pending")` on `capabilityAdded_onOff_roundTrips` (it must now pass) |
| MODIFY | `core/persistence/src/test/java/com/homesynapse/persistence/TestEventSamples.java` | retire the stale `AMD-65` Javadoc reference (~line 315 — "the `@Disabled` AMD-65 acceptance test; it degrades on decode until…") now that the codec lands; reword to reflect the codec exists (housekeeping, same WU) |
| CREATE | `core/persistence/src/test/java/com/homesynapse/persistence/ExpectationSerdeTest.java` | per-permit round-trip suite (see Test Requirements) |

## Technical Specification — implement exactly to AMD-87 §2

Hand-rolled `Expectation` `JsonSerializer`/`JsonDeserializer` pair, **keyed on the `Expectation` interface** (Jackson `SimpleSerializers` walks superclasses/interfaces, exactly as the `AttributeValue` pair is keyed on its interface — do NOT register per-permit). Compact tagged-union envelope `{"t":"<permit-simple-name>", …}` mirroring `AttributeValueSerializer`. **Exhaustive `switch` over the 4 permits with NO `default`** (a future 5th permit must be a compile-time break — the established discipline).

**The 4 permit shapes (verified at HEAD `8028337` — re-confirm against source):**

| Permit | Record shape (HEAD) | Wire form | Notes |
|---|---|---|---|
| `ExactMatch` | `ExactMatch(AttributeValue expectedValue)` | `{"t":"ExactMatch","v":<AttributeValue>}` | `v` delegates to the **existing** `AttributeValue` codec — call the registered serializer/deserializer, do not re-encode |
| `AnyChange` | `AnyChange(AttributeValue previousValue)` | `{"t":"AnyChange","v":<AttributeValue>}` | `v` delegates to the existing `AttributeValue` codec |
| `EnumTransition` | `EnumTransition(String expectedValue)` | `{"t":"EnumTransition","v":"<string>"}` | plain string |
| `WithinTolerance` | `WithinTolerance(double target, double tolerance)` | `{"t":"WithinTolerance","target":<bits>,"tolerance":<bits>}` | **AMD-52 bit-anchored-float treatment** — `Double.doubleToLongBits` text-round-trippable encoding + JSON-valid non-finite sentinels (`"NaN"`/`"+Inf"`/`"-Inf"`) + `−0.0`→`+0.0`. **Reuse the `AttributeValueSerializer` float helper; do not re-invent the encoding.** |

`Expectation` and its permits stay **annotation-free** (no `@JsonTypeInfo`, no domain Jackson annotations — the `"t"` discriminator is written by the serializer). Jackson-isolation HARD RULE + `NO_JACKSON_IN_DOMAIN_MODEL` (ArchUnit Rule 10).

## Locked Decisions That Apply
- **LTD-08 (Jackson):** all serde in `core/persistence` only; `Expectation`/permits stay Jackson-annotation-free.
- **AMD-52 (float determinism):** `WithinTolerance`'s two doubles use the bit-anchored / non-finite-sentinel discipline already implemented for `AttributeValue` — reuse it.

## Invariants That Must Hold
- **AMD-87-INV-01 (§36):** every `Expectation` permit round-trips losslessly through `EventPayloadCodec`; `WithinTolerance`'s two doubles survive encode→decode bit-identically (so `0.1` and a `NaN` sentinel are exact). Test: the un-`@Disabled` acceptance + the per-permit round-trip suite.
- **`NO_JACKSON_IN_DOMAIN_MODEL` (ArchUnit Rule 10):** the codec lives in persistence; `Expectation`/permits gain no annotations. Test: `./gradlew check` ArchUnit.

## P2 Consumer/Pin (Fan-Out) Survey (re-confirm at code time)
- **Acceptance pin:** the only consumer/pin is `EventPayloadCodecTest.CapabilityEvents.capabilityAdded_onOff_roundTrips` (`@Disabled` → un-disable). No count-pin, no manifest aggregator, no exhaustive `switch` over `Expectation` anywhere else (the codec's own no-`default` switch is the only one — intended to compile-break on a future permit).
- **No new event type:** the codec round-trips `capability.added`/`capability.removed` payloads (already-registered types). Event-class manifests / category tables untouched.
- **module-info:** the only JPMS change is persistence `+requires com.homesynapse.device`. Verify acyclic at the gate.

## Test Requirements
### Unit (`core/persistence`)
- **`ExpectationSerdeTest`:** per-permit round-trip for all 4 (`ExactMatch`/`AnyChange` wrapping a representative `AttributeValue`; `EnumTransition` with a string; `WithinTolerance` with `0.1`). `WithinTolerance` bit-identity edge cases: `0.1`, `NaN`, `+Inf`, `-Inf`, `−0.0`→`+0.0`.
- **Acceptance:** the un-`@Disabled` `capabilityAdded_onOff_roundTrips` passes — full `CapabilityAdded` round-trip (command-bearing `onOff` via `TestEventSamples.capabilityAddedOnOff()`), decoding to the real event, **not** `DegradedEvent`.

### §4c Arch-Rule Reminder (persistence test code — non-whitelisted)
> **Tests must inject `Clock`.** Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` in `core/persistence` test code — the `NO_DIRECT_TIME_ACCESS` ArchUnit rule scans non-whitelisted test classes and fails `./gradlew check`. The serde tests likely need no clock at all; but if any fixture (e.g. an `EventEnvelope` sample) needs a timestamp, use `Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC)` / a fixed `Instant`, never wall-clock.

## What to Watch Out For
- **STOP-on-mismatch — the `persistence → device` JPMS edge (the load-bearing gate).** Adding `requires com.homesynapse.device` must keep the module graph acyclic. Verified at authoring: `com.homesynapse.device` requires `value`/`event`/`platform` only, NOT persistence. If `./gradlew check` (moduleGraphAssert) reports a cycle, **STOP and report** — do not restructure the codec silently.
- **Key on the `Expectation` *interface*, not per-permit** — Jackson walks interfaces; mirror exactly how `AttributeValue` is keyed.
- **Reuse the `AttributeValue` float helper** for `WithinTolerance` — do not re-implement `doubleToLongBits` / sentinel handling. And **delegate `ExactMatch`/`AnyChange`'s `v`** to the existing `AttributeValue` codec rather than re-encoding it.
- **`WithinTolerance.evaluate()` still throws "deferred to Phase 3"** — that is correct. AMD-87 is the *codec*, not the evaluator (automation, M7/M8). Do **not** implement `evaluate()`.
- **`FloorId` is already registered (Part 3, `8028337`)** — add only the `Expectation` pair to `PersistenceJacksonModule`; do not duplicate the FloorId line.
- **`@Disabled` text says "AMD-65 pending"** (the retired number) — just delete the annotation; do not re-number it to AMD-87.

## Coder Pushback Welcome
Raise anything via the escalation format rather than silently diverging: if the `Expectation` interface keying, the `AttributeValue` delegation, the float reuse, or the `persistence → device` edge looks wrong or has a cleaner same-contract form, flag it.

## Out of Scope
- Composition-root wiring / tier-detection (lifecycle / M13).
- `Expectation.evaluate()` implementations (automation, M7/M8).
- Any crypto / at-rest encryption / `chain_hash` activation, DEK/key-management, secret store, `CredentialRotator` (Doc 15 / M6 — separate; Doc 15 is Locked).
- New event types, event-store migration, `projectionVersion` bump (none — this is additive serde).

## Build Gate (deferred to Nick)
Coder produces files only (CLAUDE.md discipline — no `./gradlew`/`javac`/`git`). Nick runs `./scripts/clean.sh && ./gradlew check --continue` (full — ArchUnit `NO_DIRECT_TIME_ACCESS` + `NO_JACKSON_IN_DOMAIN_MODEL` + moduleGraphAssert + spotless). Flag the deferred gate in coder-handoff so the PM tracks it under Open Risks (§4b). Target: GREEN in one round.

## Work Unit Completion (WUCP Phase 1)
After the gate passes (or is deferred), execute WUCP Phase 1: update `core/persistence/MODULE_CONTEXT.md` (the Expectation codec + the new `requires com.homesynapse.device` edge); update coder-handoff.md (flip the next-WU pointer off M5-A Part 2 — next is the PM's M6 instruction or another M5 lane; set the Deferred Build Gate flag); append to coder-lessons.md if the JPMS edge or the interface-keying bit you. Not done until the checklist is complete.
