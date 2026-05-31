<!--
file: context/instructions/Research_11_Typed_Event_Payload_Persistence_Brief.md
purpose: Deep-research brief dispatched to the HomeSynapse Core Claude Project. Scoped ONLY to the genuine AMD-52 (typed StateChangedEvent payload) design forks surfaced by the OQ-05-08 design beat. Informs the AMD-52 go/no-go gate (G1 serializer, G2 replay determinism).
audience: HomeSynapse Core Claude Project (researcher), PM
state-type: instruction
status: ISSUED 2026-05-31
companion: homesynapse-core-docs/design/2026-05-31_AMD-52_Typed_Payload_Serializer_Replay_Design_Beat.md (the design beat this brief serves — read it first)
-->

# Research 11 — Typed Event Payload Persistence: Polymorphic Serialization, Schema Versioning, and Replay-Deterministic Upcasting for an Event-Sourced Store

**RECs start at:** **REC-100** (deliberate gap after Research 10's REC-90..95; PM reconciles global numbering at assessment).
**Target WU / gate:** AMD-52 (typed `StateChangedEvent` payload) — gates **G1 (serializer)** and **G2 (replay determinism)** in the design beat §9. Research 11 returns → PM 6-step A–F assessment → Nick adjudicates → author AMD-52.
**Mandatory format:** the 7-section research format in `context/planning/research-agenda.md §0.3` (Exec Summary, Platform/Literature Deep Dives, Cross-Cutting Analysis, Amendment Recommendations REC-100+, Caveats/Open Questions, Sources, §7 Code-Level Implications). Concept-mapping tables are the highest-value artifact. Every recommendation cites at least one real-world pain point.

---

## 0. Why this research, and the ONE scope rule

HomeSynapse Core is an event-sourced, local-first smart-home OS on constrained hardware (Pi-class, 256 MiB heap). M4.0b-3 (AMD-51, committed `98f705b`) shipped a **typed change-detection comparator** but deliberately kept the `StateChangedEvent` payload as **String** `oldValue`/`newValue`. AMD-52 will carry the **typed `AttributeValue`** in the event and materialize it — which crosses the **serializer**, the **event-store shape**, and **replay determinism** at once. The design beat already DECIDED two sub-questions (no event-store row migration; AMD-52 is a separate `projectionVersion` 3→4 bump on the frozen AMD-50 backfill) and DECIDED the discriminator *mechanism* (a custom Jackson (de)serializer in `core/persistence`, **no `@JsonTypeInfo`**). What remains OPEN — and what this brief exists to inform — is a small, named set of forks.

**THE SCOPE RULE (do not violate):** research **ONLY** the six forks in §3 below. Do **not** re-open or re-litigate the DECIDED items (the discriminator mechanism, the no-row-migration finding, the 3→4 staging) — they are settled against source in the design beat. Do **not** invent new problems, new abstractions, or new dependencies. If you believe a DECIDED item is wrong, flag it in §5 (Caveats) with source evidence — do not silently redesign around it.

**The Research-6 anti-fabrication rule (load-bearing):** every HomeSynapse type name, module name, and library version you cite must come from the verbatim CONSTRAINTS block (§2) — not invented, not recalled. Prior research fabricated type names (Research 3/4/8 §7) and JPMS module names (Research 6 §7.8) when they were not embedded. They are embedded here. Use them exactly.

---

## 1. The HomeSynapse problem, precisely (so prior art maps cleanly)

- **The event today:** `StateChangedEvent(String attributeKey, String oldValue, String newValue, EventId triggeredBy)` — a `DomainEvent` record, serialized to UTF-8 JSON in the `events.payload` BLOB by the sole codec `EventPayloadCodec` (over the locked `PersistenceObjectMapper`). The event's *own* polymorphism is resolved by an explicit `events.event_type` column + `EventTypeRegistry`, **never** `@JsonTypeInfo`.
- **The change:** `oldValue`/`newValue` become **`AttributeValue`** — a **sealed 8-variant** sum type (`BooleanValue`, `IntValue`, `FloatValue`, `StringValue`, `EnumValue`, `QuantityValue`, `ArrayValue`, `DegradedAttributeValue`). So AMD-52 embeds a **nested polymorphic sum type inside a JSON event payload**, and must (de)serialize it durably, deterministically, and version-tolerantly.
- **The replay reality:** the historical log holds **String-payload** `state_changed` (per-event `schema_version = 1`). The projection re-derives state from the **immutable** `state_reported` log on a `projectionVersion` bump (AMD-50 reconciliation backfill — FROZEN; reused unchanged for 3→4). Events are **append-only and never mutated**. The per-event `events.schema_version` column is the existing forward seam.
- **The constraints that make this *stricter* than most systems:** replay must be **bit-deterministic** (no `Clock` in derivation; AMD-50-INV-03); Jackson is confined to one module and `@JsonTypeInfo` is **banned** on events; the runtime is Pi-class with a 256 MiB heap; floats can be `NaN`/`±Inf` (`FloatValue` has no finite-guard).

Your survey should treat HomeSynapse's replay-determinism + no-`@JsonTypeInfo` + constrained-hardware combination as the lens: many mature systems relax one of these, and the interesting findings are where their solution *survives* all three or where it *fails* one.

---

## 2. CONSTRAINTS — verbatim source embeds (cite these exactly; do not paraphrase type/module/version names)

### 2.1 Verbatim `module-info.java` — three modules (HEAD `98f705b`)

```java
// core/event-model/src/main/java/module-info.java
module com.homesynapse.event {
    requires transitive com.homesynapse.platform;
    exports com.homesynapse.event;
}

// core/device-model/src/main/java/module-info.java
module com.homesynapse.device {
    requires com.homesynapse.event;
    requires transitive com.homesynapse.platform;
    exports com.homesynapse.device;
}

// core/persistence/src/main/java/module-info.java  (Jackson lives ONLY here)
module com.homesynapse.persistence {
    requires transitive com.homesynapse.platform;
    requires transitive com.homesynapse.state;
    requires transitive com.homesynapse.event;
    requires transitive com.homesynapse.event.bus;
    requires java.sql;
    requires org.slf4j;
    requires com.fasterxml.jackson.core;
    requires com.fasterxml.jackson.databind;
    requires com.fasterxml.jackson.datatype.jsr310;
    requires com.fasterxml.jackson.module.blackbird;
    exports com.homesynapse.persistence;
}
```

JPMS module names are exactly `com.homesynapse.event`, `com.homesynapse.device`, `com.homesynapse.persistence`, `com.homesynapse.state` (flat-package-per-module — **NOT** `…event.model`/`…device.model`/`…state.store`). **Persistence is the only module that `requires` Jackson** — any serde code AMD-52 adds lives here.

### 2.2 Verbatim Jackson version-catalogue rows (LTD-08 lock) — `gradle/libs.versions.toml`

```toml
jackson                   = "2.18.6"
jackson-core              = { module = "com.fasterxml.jackson.core:jackson-core", version.ref = "jackson" }
jackson-databind          = { module = "com.fasterxml.jackson.core:jackson-databind", version.ref = "jackson" }
jackson-annotations       = { module = "com.fasterxml.jackson.core:jackson-annotations", version.ref = "jackson" }
jackson-datatype-jsr310   = { module = "com.fasterxml.jackson.datatype:jackson-datatype-jsr310", version.ref = "jackson" }
jackson-module-blackbird  = { module = "com.fasterxml.jackson.module:jackson-module-blackbird", version.ref = "jackson" }
```

Locked `PersistenceObjectMapper.create()` config (LTD-08 / DECIDE-M2-04): `PropertyNamingStrategies.SNAKE_CASE`; `JsonInclude.Include.NON_NULL`; `DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES` **disabled** (forward-compat, INV-ES-07); `SerializationFeature.WRITE_DATES_AS_TIMESTAMPS` **disabled**; `SerializationFeature.INDENT_OUTPUT` **disabled** (compact BLOB); `JavaTimeModule` + `BlackbirdModule` + `PersistenceJacksonModule`; `JsonRecyclerPools.newConcurrentDequePool()`. **No new Jackson artifact may be proposed** — recommend within this set (a custom `JsonSerializer`/`JsonDeserializer` is in `jackson-databind`, already present).

### 2.3 Verbatim types AMD-52 touches (HEAD `98f705b`)

```java
@EventType(EventTypes.STATE_CHANGED)
public record StateChangedEvent(String attributeKey, String oldValue, String newValue, EventId triggeredBy)
        implements DomainEvent { /* compact ctor: all non-null */ }

public sealed interface AttributeValue
        permits BooleanValue, IntValue, FloatValue, StringValue, EnumValue,
                QuantityValue, ArrayValue, DegradedAttributeValue {
    Object rawValue();              // never null
    AttributeType attributeType();  // never null — the 8-value discriminator
}
// BooleanValue(boolean) | IntValue(long) | FloatValue(double) [CAN carry NaN/±Inf — no ctor guard]
// StringValue(String) non-null | EnumValue(String) non-null
// QuantityValue(double value, String unit) [canonicalized at construction; rejects non-finite]
// ArrayValue(List<AttributeValue> elements) [List.copyOf, ordered, full-replacement]
// DegradedAttributeValue(String originalTypeName, String rawForm, String failureReason)

// The value-layer migration SPI — keyed by stored type-name + per-event schema version; NO ServiceLoader.
public interface AttributeValueUpcaster {
    boolean canUpcast(String storedTypeName, int fromSchemaVersion);
    AttributeValue upcast(String storedTypeName, String rawForm, int fromSchemaVersion);   // strict — throws on failure
    default AttributeValue upcastLenient(String storedTypeName, String rawForm, int fromSchemaVersion) { /* → DegradedAttributeValue on failure */ }
}
```

The S1 serde boundary is `EventPayloadCodec.encode(DomainEvent) → byte[]` / `decode(String eventType, int schemaVersion, byte[] payload) → DomainEvent` — `decode` **already threads the per-event `schema_version`**; on parse failure it returns a `DegradedEvent` (lossy). The S2 boundary is `CheckpointSerializer` (materialized-view snapshot in `view_checkpoints.data` BLOB; today flattens attributes to `Map<String,String>`).

### 2.4 LOCKED decisions — treat as immovable CONSTRAINTS (a recommendation that violates one is invalid)

- **`@JsonTypeInfo` is BANNED on event types** — ArchUnit Rule 7 `NO_JSON_TYPE_INFO_IN_EVENTS`; polymorphism is by explicit discriminator (DECIDE-M2-06). The nested `AttributeValue` discriminator must be an **explicit `AttributeType` tag emitted by a custom (de)serializer**, not reflection-driven type info.
- **Jackson-isolation HARD RULE** — Jackson is confined to 9 package-private classes in `com.homesynapse.persistence`; no event/device type may carry a Jackson annotation; no other module imports `com.fasterxml.jackson.*`. The `AttributeValue` codec lives in persistence and treats `AttributeValue` as plain data.
- **No `ServiceLoader`** (DECIDE-04) — all SPIs (incl. `AttributeValueUpcaster`) are constructor-injected.
- **D-01** — no exhaustive `switch` over **event** types (`DomainEvent` is non-sealed, AMD-33). NOTE: an exhaustive `switch` over the **sealed `AttributeValue`** is *permitted and idiomatic* (D-01 is event-type-scoped; AMD-51-INV-01 already uses one). The codec's variant dispatch SHOULD be total over the 8 `AttributeType` values (no silent catch-all).
- **AMD-50 backfill is FROZEN** — the N→M reconciliation-backfill / one-shot provenance gate / cursor-as-log-position / supersession discipline is reused unchanged for 3→4. Do not propose a new backfill mechanism.
- **AMD-51 §2.7 + §2.6 erratum** — the String `StateChangedEvent` payload is preserved until AMD-52 ratifies; the materialized prior is currently always a `StringValue`, and the no-schema case is a `StringValue` string-compare fallback. AMD-52 ends the "materialized String-only" regime — your replay analysis must respect that the prior side becomes natively typed.
- **No `Clock` in derivation** (AMD-50 §2.4 / AMD-50-INV-03) — replay/derivation is a pure function of inputs; serializer/upcaster determinism is mandatory, not aspirational.
- **Constrained hardware** — Pi-class, **256 MiB heap**, SQLite, virtual-thread event bus; BLOB compactness (INV-PR-01) and GC pressure are first-order.

---

## 3. The forks to research — and ONLY these (mapped to required questions)

### Fork 1 — Polymorphic / sum-type payload serialization for durability (design beat §2.2a)
The exact durable on-wire encoding of an 8-variant sealed sum type **without framework reflection**. Tagged-union envelope shape (e.g. compact `{"t":"FLOAT","v":…}` vs nested vs tag-prefixed scalar); how `ArrayValue` recurses; compactness under `Include.NON_NULL` on a 256 MiB heap.
- **Required question:** how do mature event-sourced systems serialize polymorphic/sum-type payloads for durability with an **explicit** (non-reflective) discriminator?
- **Prior art (mandatory):** **Axon Framework** custom serializers (and why Axon supports both `XStreamSerializer` and `JacksonSerializer`, and how typed payloads are tagged); **Kafka Schema Registry** Avro **unions** + Protobuf `oneof` (the canonical explicit sum-type-on-the-wire encodings); **Akka Persistence** custom `SerializerWithStringManifest` (the *manifest* idea — an explicit string discriminator carried beside the bytes, exactly HomeSynapse's `event_type`/`AttributeType` philosophy); **EventStoreDB** JSON-vs-binary payload conventions.

### Fork 2 — Deterministic value encoding (design beat §2.2b/c) — the determinism keystone
Two precise sub-problems: (a) a **canonical `double`→text** rendering that is byte-stable across JVM versions/platforms (matters for forensic equality, idempotency, and the reserved `chain_hash`); (b) a **lossless, JSON-valid, deterministic encoding of `NaN`/`±Inf`/`−0.0`** (standard JSON has no `NaN`/`Infinity`; `FloatValue` can carry them; Jackson `ALLOW_NON_NUMERIC_NUMBERS` emits **non-standard** bare tokens — likely rejected).
- **Required question:** how do durable event stores guarantee **floating-point byte-stability** and encode IEEE-754 edge values in a JSON-valid, lossless, deterministic way?
- **Prior art (mandatory):** Avro/Protobuf binary float handling (do they sidestep the text-rendering problem entirely?); Jackson's float-serialization options and the shortest-round-trip (`Double.toString` vs Ryū-style) debate; any event-store guidance on canonical JSON (e.g. JCS RFC 8785-style canonicalization) for hashable payloads; how systems represent `NaN`/`Inf`/`-0.0` (sentinel strings vs binary vs prohibition).

### Fork 3 — Payload schema versioning without breaking replay (design beat §3/§4)
The per-event `schema_version` upcaster seam: how a `schema_version = 1` (String) `state_changed` is migrated forward at read time without rewriting it.
- **Required question:** how is payload schema **versioning** done so an old payload remains readable after the type evolves — without in-place mutation?
- **Prior art (mandatory):** **Axon upcaster chain + `@Revision`** (the canonical reference — chained, incremental, stream-based upcasting keyed by a revision tag); EventStoreDB / Marten schema-evolution patterns; Kafka Schema Registry compatibility modes (BACKWARD/FORWARD/FULL) as the *contract* model for "old reader, new writer" and vice-versa.

### Fork 4 — Deterministic replay across schema versions (design beat §4 — Path A vs Path B)
HomeSynapse has two replay surfaces: **Path A** re-derives typed state from the immutable `state_reported` log during the 3→4 backfill (authoritative, rides AMD-50/AMD-51 unchanged); **Path B** is reading a historical String-payload `state_changed` *as a typed event* for forensic/observability (today → lossy `DegradedEvent`). The fork: does AMD-52 wire the `AttributeValueUpcaster` into the **decode** path (version-branched lift) or accept `DegradedEvent` for legacy rows?
- **Required question:** when do mature systems **re-derive** from source events vs **upcast** the stored derived payload, and how is the upcast made bit-deterministic and verifiable?
- **Prior art (mandatory):** Axon's distinction between upcasting events and rebuilding projections; how Akka Projections / EventStoreDB handle "rebuild the read model from the log" vs "migrate stored events"; any guidance on proving an upcaster is a pure/total/deterministic function (testing patterns — HomeSynapse will extend its `Double.doubleToLongBits` bit-identity tests to every String→typed lift).

### Fork 5 — Inline-blob vs normalized-column storage tradeoffs on constrained hardware (design beat §3 / §10.5)
The beat DECIDED the typed payload stays **inline** in the `payload` BLOB (no normalization, no migration). Pressure-test that against Pi-class / 256 MiB-heap reality.
- **Required question:** inline-JSON-blob vs normalized/columnar payload storage — read/write amplification, BLOB size, GC pressure, and query needs — on constrained single-node hardware?
- **Prior art (mandatory):** EventStoreDB and SQLite-backed event stores (e.g. Marten-on-Postgres JSONB as a *contrast* — what HomeSynapse deliberately does NOT have); the general "store the event as an opaque serialized blob, index metadata in columns" event-sourcing consensus; any measured guidance at ~256 MiB heap.

### Fork 6 — Explicit anti-patterns to avoid (design beat §10.6) — name them, source them
- **Required question:** what are the documented failure modes — **in-place event mutation**, **lossy upcasts**, **serializer nondeterminism** — and the war stories behind each?
- **Prior art (mandatory):** event-sourcing literature on "never mutate the event log"; lossy-upcast incidents (data silently dropped during migration); serializer-nondeterminism failures (map/field ordering, locale-dependent float formatting, reflection-order instability) — especially any that broke replay or a hash chain. Map-ordering is **already cleared** for HomeSynapse (no `Map` inside any `AttributeValue` variant; `ArrayValue` is an ordered `List`) — confirm that reasoning and focus the nondeterminism findings on float rendering and reflective type tags.

---

## 4. Amendment Recommendations expected (REC-100+)

Produce ranked RECs (impact × confidence / cost, the Research 2 model) that let Nick draw a scope line, each targeting a specific fork and citing ≥1 real pain point. At minimum: a recommended **tagged-union envelope** (Fork 1); a **canonical float + IEEE-edge encoding** (Fork 2); a **version-branched decode vs DegradedEvent** call for Path B (Fork 4); a **confirm-inline-BLOB** REC with the constrained-hardware evidence (Fork 5); and an **anti-pattern checklist** the AMD-52 author and coder must gate against (Fork 6). Number from **REC-100**. Do **not** recommend anything that violates a §2.4 LOCKED decision; if a fork seems to *require* such a violation, that is a §5 Caveat for the PM/Nick, not a REC.

## 5. Caveats / Open Questions
Flag anything you could not source, any place a §2.4 constraint appears to conflict with best practice (with evidence), and any HomeSynapse fact in §2 you could not reconcile. Honest "cannot verify" beats fabrication.

## 6. Sources
Primary-source, densely cited (Axon reference docs + `@Revision`/upcaster Javadoc; Avro/Protobuf spec language on unions/`oneof`; Akka `SerializerWithStringManifest` docs; EventStoreDB docs; RFC 8785 / Jackson float-serialization issues). The Research 10 bar (≈28 traceable URLs) is the target.

## 7. HomeSynapse Code-Level Implications [include]
Map each REC onto the §2.3 types and the two serde boundaries (`EventPayloadCodec` / `CheckpointSerializer`) and the `AttributeValueUpcaster` SPI. **Use ONLY the names/modules/versions in §2 — do not invent any.** State, per REC, which of the design beat's gates (G1–G4) it closes. This §7 is the input the PM source-verifies against HEAD `98f705b` before it informs AMD-52 authoring — fabricated names will be caught and the §7 graded down (the Research 10 §7 lesson).

---

**Issued by:** PM (Cowork). **Companion design beat:** `homesynapse-core-docs/design/2026-05-31_AMD-52_Typed_Payload_Serializer_Replay_Design_Beat.md`. **On return:** fresh Cowork session runs the 6-step A–F assessment, source-verifies §7 against HEAD, frames the forks for Nick, then (post-adjudication) authors AMD-52.
