<!--
file: context/handoff/2026-05-30_AMD51_external_review_source_companion.md
purpose: Verbatim source companion for the AMD-51 external review (HomeSynapse Core Claude Project). Every type the comparator touches, source-verified against HEAD 60b4185 via the Read tool (the in-sandbox git/grep truncates this synced folder and is distrusted).
audience: external reviewer (HomeSynapse Core Claude Project)
state-type: reference (point-in-time snapshot)
status: CURRENT — HEAD 60b4185 (M4.B3, AMD-47 committed)
-->

# AMD-51 Review — Source Companion (verbatim, HEAD `60b4185`)

This bundles every type the AMD-51 typed comparator interacts with, copied verbatim from `homesynapse-core` at HEAD `60b4185`. It exists so the review can check that the AMD-51 contract is implementable against the **actual** types, not an assumed shape. License headers are elided for brevity; signatures, Javadoc contracts, and constructor validation are verbatim. If a claim in AMD-51 contradicts anything here, the source wins.

---

## 1. The sealed value hierarchy (`com.homesynapse.device`)

### `AttributeValue` (sealed interface — 8 permits)

```java
public sealed interface AttributeValue
        permits BooleanValue, IntValue, FloatValue, StringValue, EnumValue,
                QuantityValue, ArrayValue, DegradedAttributeValue {
    Object rawValue();              // never null
    AttributeType attributeType();  // never null
}
```

### The five primitives

```java
public record BooleanValue(boolean value) implements AttributeValue {
    public Object rawValue() { return value; }
    public AttributeType attributeType() { return AttributeType.BOOLEAN; }
}

// long-backed (brightness 0–100, battery 0–100, LQI 0–255, etc.)
public record IntValue(long value) implements AttributeValue {
    public Object rawValue() { return value; }
    public AttributeType attributeType() { return AttributeType.INT; }
}

// double-backed; continuous measurements (temp, humidity, power, energy)
public record FloatValue(double value) implements AttributeValue {
    public Object rawValue() { return value; }
    public AttributeType attributeType() { return AttributeType.FLOAT; }
}

public record StringValue(String value) implements AttributeValue {  // value non-null
    public StringValue { Objects.requireNonNull(value, "StringValue value must not be null"); }
    public Object rawValue() { return value; }
    public AttributeType attributeType() { return AttributeType.STRING; }
}

public record EnumValue(String value) implements AttributeValue {    // value non-null
    public EnumValue { Objects.requireNonNull(value, "EnumValue value must not be null"); }
    public Object rawValue() { return value; }
    public AttributeType attributeType() { return AttributeType.ENUM; }
}
```

### `QuantityValue` — canonicalized at construction (AMD-47-INV-03 / REC-93)

The constructor converts the supplied `(value, unit)` to the dimension's **canonical unit** and stores the canonical magnitude + canonical unit symbol. Two `QuantityValue`s of the same dimension are directly magnitude-comparable on `value()`. Fail-closed on null/blank/unrecognised unit or non-finite magnitude — **never** produces a `DegradedAttributeValue`.

```java
public record QuantityValue(double value, String unit) implements AttributeValue {

    private record Conversion(String canonicalUnit, DoubleUnaryOperator toCanonical) { }
    private static final Map<String, Conversion> CATALOGUE = buildCatalogue();

    private static Map<String, Conversion> buildCatalogue() {
        Map<String, Conversion> m = new HashMap<>();
        // Temperature — canonical °C. K and °F are affine (offset), not pure scale.
        m.put("°C", new Conversion("°C", v -> v));
        m.put("K",  new Conversion("°C", v -> v - 273.15));
        m.put("°F", new Conversion("°C", v -> (v - 32.0) * 5.0 / 9.0));
        // Power — canonical W. Multiplicative.
        m.put("W",  new Conversion("W", v -> v));
        m.put("kW", new Conversion("W", v -> v * 1000.0));
        m.put("mW", new Conversion("W", v -> v * 0.001));
        // Energy — canonical Wh. Multiplicative.
        m.put("Wh",  new Conversion("Wh", v -> v));
        m.put("kWh", new Conversion("Wh", v -> v * 1000.0));
        m.put("J",   new Conversion("Wh", v -> v / 3600.0));
        m.put("kJ",  new Conversion("Wh", v -> v / 3.6));
        // Illuminance — canonical lux. Multiplicative.
        m.put("lux", new Conversion("lux", v -> v));
        m.put("klx", new Conversion("lux", v -> v * 1000.0));
        // Ratio / percent — canonical %.
        m.put("%", new Conversion("%", v -> v));
        return Map.copyOf(m);
    }

    public QuantityValue {  // compact constructor — normalizes, fails closed
        Objects.requireNonNull(unit, "QuantityValue unit must not be null");
        if (unit.isBlank()) throw new IllegalArgumentException("QuantityValue unit must not be blank");
        if (Double.isNaN(value) || Double.isInfinite(value))
            throw new IllegalArgumentException("QuantityValue magnitude must be finite, got " + value);
        Conversion conversion = CATALOGUE.get(unit);
        if (conversion == null) throw new IllegalArgumentException("Unrecognised unit: " + unit);
        value = conversion.toCanonical().applyAsDouble(value);
        unit  = conversion.canonicalUnit();
    }

    public Object rawValue() { return value; }            // canonical magnitude, boxed Double
    public AttributeType attributeType() { return AttributeType.QUANTITY; }
}
```

### `ArrayValue` — full-replacement (AMD-47-INV-05)

```java
public record ArrayValue(List<AttributeValue> elements) implements AttributeValue {
    public ArrayValue { elements = List.copyOf(elements); }  // unmodifiable, null-free, may be empty
    public Object rawValue() { return elements; }
    public AttributeType attributeType() { return AttributeType.ARRAY; }
}
// No delta/patch semantics: a new ArrayValue wholly replaces the prior. Element homogeneity is
// a schema-level concern (AttributeValidator), not enforced here. Nesting is type-permitted.
```

### `DegradedAttributeValue` — upcast-failure sentinel (AMD-47-INV-04)

```java
public record DegradedAttributeValue(
        String originalTypeName, String rawForm, String failureReason) implements AttributeValue {
    public DegradedAttributeValue {
        Objects.requireNonNull(originalTypeName, "originalTypeName must not be null");
        Objects.requireNonNull(rawForm,          "rawForm must not be null");          // blank permitted
        Objects.requireNonNull(failureReason,    "failureReason must not be null");
        if (originalTypeName.isBlank()) throw new IllegalArgumentException("originalTypeName must not be blank");
        if (failureReason.isBlank())    throw new IllegalArgumentException("failureReason must not be blank");
    }
    public Object rawValue() { return rawForm; }
    public AttributeType attributeType() { return AttributeType.DEGRADED; }  // sentinel
}
// Produced only by AttributeValueUpcaster lenient mode. Strict mode never produces it and it is
// never written to canonical state. AttributeType.DEGRADED may never appear in an AttributeSchema.
```

### `AttributeType` (enum)

```java
public enum AttributeType { BOOLEAN, INT, FLOAT, STRING, ENUM, QUANTITY, ARRAY, DEGRADED }
// DEGRADED is a sentinel-only classifier; never declared in an AttributeSchema (AMD-47-INV-04).
```

### `AttributeSchema` (the per-attribute metadata carrier)

```java
public record AttributeSchema(
        String attributeKey,
        AttributeType type,
        Number minimum,             // INT/FLOAT bound, null if N/A
        Number maximum,
        Number step,                // UI slider granularity
        Set<String> validValues,    // ENUM set, null otherwise
        String unitSymbol,          // display unit ("°C","W","%"), null if dimensionless
        String canonicalUnitSymbol, // SI canonical unit for storage normalization, null if N/A
        Set<Permission> permissions,
        boolean nullable,
        boolean persistent) {
    public AttributeSchema {  // rejects DEGRADED as a declared type (AMD-47-INV-04); no other validation
        if (type == AttributeType.DEGRADED)
            throw new IllegalArgumentException("AttributeType.DEGRADED is a sentinel and must not be declared in an AttributeSchema");
    }
}
```

### `AttributeValueUpcaster` SPI — stored-value migration (no unit parameter)

This is the SPI AMD-51 §2.6 deliberately leaves **unchanged**. Note the signature carries `(storedTypeName, rawForm, fromSchemaVersion)` — **no unit** — and its purpose is migrating *already-stored* values across type changes, not parsing a fresh inbound report.

```java
public interface AttributeValueUpcaster {
    boolean canUpcast(String storedTypeName, int fromSchemaVersion);

    // Strict: core projections. Throws on failure; never produces a DegradedAttributeValue.
    AttributeValue upcast(String storedTypeName, String rawForm, int fromSchemaVersion);

    // Lenient (default): diagnostic/forensic. Failure -> DegradedAttributeValue; never throws.
    default AttributeValue upcastLenient(String storedTypeName, String rawForm, int fromSchemaVersion) {
        try {
            if (!canUpcast(storedTypeName, fromSchemaVersion))
                return new DegradedAttributeValue(storedTypeName, rawForm,
                        "no upcaster for type " + storedTypeName + " at version " + fromSchemaVersion);
            return upcast(storedTypeName, rawForm, fromSchemaVersion);
        } catch (RuntimeException e) {
            String reason = (e.getMessage() == null) ? e.toString() : e.getMessage();
            return new DegradedAttributeValue(storedTypeName, rawForm, reason);
        }
    }
}
// SPI is constructor-injected; NO ServiceLoader (DECIDE-04). Lives in com.homesynapse.device.
// When wired into the projection (a later WU = M4.0b-3), it MUST run strictly before
// DerivationRule.evaluate() on BOTH onEvent and processBatch (AMD-47-INV-02).
```

---

## 2. The event records (`com.homesynapse.event`)

### `StateReportedEvent` — the inbound (all-String; carries `unit`)

```java
@EventType(EventTypes.STATE_REPORTED)
public record StateReportedEvent(
        String attributeKey,
        String value,            // canonical value in serialized form (SI/standard units).
                                 // Javadoc: "Phase 3 introduces typed AttributeValue."
        String unit,             // canonical unit for physical quantities; null for dimensionless
        String rawProtocolValue, // pre-canonical-conversion; null when no conversion
        String rawProtocolUnit   // protocol-native unit; null when rawProtocolValue null
) implements DomainEvent {
    public StateReportedEvent {
        Objects.requireNonNull(attributeKey, "attributeKey must not be null");
        Objects.requireNonNull(value, "value must not be null");
    }
}
```

### `StateChangedEvent` — the derived output (String payload; AMD-51 preserves it)

```java
@EventType(EventTypes.STATE_CHANGED)
public record StateChangedEvent(
        String attributeKey,
        String oldValue,         // previous canonical value, serialized form; non-null
        String newValue,         // new canonical value, serialized form; non-null
        EventId triggeredBy      // the EventId of the state_reported that caused this; non-null
) implements DomainEvent {
    public StateChangedEvent {
        Objects.requireNonNull(attributeKey, "attributeKey must not be null");
        Objects.requireNonNull(oldValue, "oldValue must not be null");
        Objects.requireNonNull(newValue, "newValue must not be null");
        Objects.requireNonNull(triggeredBy, "triggeredBy must not be null");
    }
}
// NOTE: linking field is `triggeredBy` (not "causingEventId"). old/new are String — AMD-52, not AMD-51,
// would make them typed AttributeValue.
```

---

## 3. The derivation seam (`com.homesynapse.state`)

### `DerivationContext` — no clock (AMD-50 §2.4)

```java
public record DerivationContext(EntityState priorState, EventEnvelope envelope) {
    public DerivationContext { Objects.requireNonNull(envelope, "envelope must not be null"); }
}
// priorState may be null (first event for the entity). "there is deliberately no clock" —
// AMD-50 §2.4 removed the formerly-injected Clock so the rule is a pure function of inputs.
```

### `DerivationRule` — strategy + gateway factory

```java
@FunctionalInterface
public interface DerivationRule {
    List<EventDraft> evaluate(DerivationContext context);  // immutable/defensive-copy list, never null
    static DerivationRule production() { return new ProductionDerivationRule(); }  // DEC-M3-16 gateway
}
// Contract: MUST NOT publish; MUST NOT mutate StateStore; MUST be deterministic (INV-PROJ-01);
// derived eventTime inherits from the causing envelope, never Instant.now().
```

### `ProductionDerivationRule` — the CURRENT string change-detect (the AMD-51 modification site, C4)

```java
final class ProductionDerivationRule implements DerivationRule {
    ProductionDerivationRule() { }  // stateless, package-private

    @Override
    public List<EventDraft> evaluate(DerivationContext context) {
        EventEnvelope env = context.envelope();
        if (!(env.payload() instanceof StateReportedEvent sr)) return List.of();

        String key = sr.attributeKey();
        String newValue = sr.value();                                 // <-- inbound is String
        String oldValue = priorValue(context.priorState(), key);      // <-- prior stringified
        if (Objects.equals(oldValue, newValue)) return List.of();      // <-- THE STRING COMPARE AMD-51 REPLACES

        String oldNonNull = (oldValue == null) ? "" : oldValue;
        StateChangedEvent payload = new StateChangedEvent(key, oldNonNull, newValue, env.eventId());
        EventDraft draft = new EventDraft(
                EventTypes.STATE_CHANGED, 1, env.eventTime(), env.subjectRef(),
                EventPriority.NORMAL, EventOrigin.SYSTEM, payload, env.actorRef(), null);
        return List.of(draft);
    }

    private static String priorValue(EntityState prior, String key) {
        if (prior == null) return null;
        AttributeValue value = prior.attributes().get(key);
        if (value == null) return null;
        return (value instanceof StringValue sv) ? sv.value() : value.rawValue().toString();
    }
}
```

### `EntityState` — the prior side (typed attributes map)

```java
public record EntityState(
        EntityId entityId,
        Map<String, AttributeValue> attributes,  // <-- prior side is TYPED; unmodifiable; values may be null
        Availability availability,
        long stateVersion,                        // advances on EVERY processed event; idempotency cursor
        Instant lastChanged,                      // driven by state_changed; "last activity"
        Instant lastUpdated,                      // any processed event
        Instant lastReported,                     // last state_reported (staleness)
        Instant staleAfter,                       // nullable
        boolean stale) { }
```

---

## 4. Module graph (verbatim `module-info.java`, ×3)

Placement is dependency-valid: `state requires transitive device + event`, so the comparator in state-store sees `AttributeValue` / `AttributeSchema` / the upcaster / `StateReportedEvent` with no cycle. No `module-info` change is required by AMD-51.

```java
// core/device-model/src/main/java/module-info.java
module com.homesynapse.device {
    requires com.homesynapse.event;
    requires transitive com.homesynapse.platform;
    exports com.homesynapse.device;
}

// core/state-store/src/main/java/module-info.java
module com.homesynapse.state {
    requires transitive com.homesynapse.platform;
    requires transitive com.homesynapse.device;
    requires transitive com.homesynapse.event;
    requires transitive com.homesynapse.event.bus;
    requires org.slf4j;
    exports com.homesynapse.state;
}

// core/event-model/src/main/java/module-info.java
module com.homesynapse.event {
    requires transitive com.homesynapse.platform;
    exports com.homesynapse.event;
}
```

---

## 5. Frozen constraints the reviewer must respect (do not propose changes that violate these)

- **Replay determinism (INV-PROJ-01 / AMD-50-INV-03):** the rule and comparator MUST be pure functions of `(priorState, envelope)` — no clock, no I/O, no randomness, no registry reads. This rules out every time-based change-detection mechanism (debounce, min/max interval, Z-Wave 30s rule, swinging-door). The comparator must re-execute identically during a replay-from-zero backfill.
- **Sealed exhaustiveness (AMD-47-INV-01):** the comparator's `switch` over `AttributeValue` must be exhaustive with no `default` — a future 9th permit must break compilation.
- **No `ServiceLoader`; constructor injection (DECIDE-04).**
- **D-01 is event-type-scoped** (no exhaustive switch over `DomainEvent`); an exhaustive switch over `AttributeValue` is permitted.
- **AMD-50 backfill / supersession / cursor-as-log-position is FROZEN** — AMD-51 rides the 2→3 transition on it unchanged.
- **AMD-47 typed hierarchy (8 variants) + canonicalize-at-construction is FROZEN.**
- **String `StateChangedEvent` payload is preserved** (typed payload = AMD-52, staged behind OQ-05-08 — out of scope).
- **Deadband is deferred** (REC-95 — reserve only; not for M4.0b-3).
