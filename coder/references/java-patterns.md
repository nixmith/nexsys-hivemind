<!--
file: coder/references/java-patterns.md
purpose: Concrete Java 21 patterns used throughout HomeSynapse Core (ULIDs, sealed types, SQLite, Jackson).
audience: Coder
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-06-07 against commit 8028337
-->

# Java Implementation Patterns for HomeSynapse

Concrete code patterns used throughout HomeSynapse Core. Reference this when writing any Java code.

---

## 1. Typed ULID Wrappers (LTD-04)

Every addressable object has a typed ID wrapper. Never use raw `String` or `Ulid` for identifiers.

```java
/**
 * Typed wrapper for entity identifiers. Provides compile-time
 * discrimination between entity IDs and other ULID-based identifiers.
 */
public record EntityId(Ulid value) implements Comparable<EntityId> {

    public byte[] toBytes() {
        return value.toBytes();
    }

    public static EntityId fromBytes(byte[] bytes) {
        return new EntityId(Ulid.from(bytes));
    }

    public static EntityId of(Ulid value) {
        return new EntityId(value);
    }

    public static EntityId parse(String encoded) {
        return new EntityId(Ulid.parse(encoded));
    }

    @Override
    public String toString() {
        return value.toString(); // Crockford Base32 — for API/logs ONLY
    }

    @Override
    public int compareTo(EntityId other) {
        return value.compareTo(other.value);
    }
}
```

**Generating IDs.** The identity wrappers expose only `of(Ulid)` / `parse(String)` / `fromBytes(byte[])` — there is **no `EntityId.generate()`** (a common mistake that does not compile). Generate via the constructor with a ULID from the hand-rolled `UlidFactory` (in platform-api; `ulid-creator` was removed, DECIDE-02), passing an injected `Clock` in non-whitelisted modules (§11):
```java
EntityId id  = new EntityId(UlidFactory.generate(clock));  // entity IDs
EventId  evt = new EventId(UlidFactory.monotonic());       // event IDs — monotonic within a millisecond
```

**Database operations** — always BLOB(16):
```java
// Writing
preparedStatement.setBytes(1, entityId.toBytes());

// Reading
EntityId id = EntityId.fromBytes(resultSet.getBytes("entity_id"));
```

**Jackson serialization** — register custom serializer/deserializer:
```java
public class EntityIdSerializer extends JsonSerializer<EntityId> {
    @Override
    public void serialize(EntityId value, JsonGenerator gen,
                          SerializerProvider provider) throws IOException {
        gen.writeString(value.toString()); // Crockford Base32 on the wire
    }
}
```

---

## 2. Sealed Interface Hierarchies

Use sealed interfaces for type-safe event hierarchies, capability types, and action types.

```java
/**
 * Root of the domain event type hierarchy. Every event payload
 * implements this interface. The sealed constraint ensures exhaustive
 * pattern matching in switch expressions.
 */
public sealed interface DomainEvent
    permits DeviceEvent, AutomationEvent, SystemEvent, ConfigEvent {
}

public sealed interface DeviceEvent extends DomainEvent
    permits StateChanged, CommandIssued, CommandResult, DeviceAdopted,
            DeviceRemoved {
}

public record StateChanged(
    EntityId entityId,
    String attributeKey,
    AttributeValue oldValue,
    AttributeValue newValue
) implements DeviceEvent {}
```

**Pattern matching in switch** (Java 21):
```java
switch (event) {
    case StateChanged sc -> handleStateChange(sc);
    case CommandIssued ci -> handleCommand(ci);
    case CommandResult cr -> handleResult(cr);
    default -> log.debug("Unhandled event type: {}", event.getClass().getSimpleName());
}
```

---

## 3. Record Types for Data

Records for all value types, event payloads, configuration structures, and DTOs.

```java
/**
 * Immutable event envelope carrying all 14 fields plus the typed payload.
 * actorRef was promoted from CausalContext to enable direct indexing
 * for multi-user audit trails (INV-MU-01).
 */
public record EventEnvelope(
    EventId eventId,
    String eventType,
    int schemaVersion,
    Instant ingestTime,
    @Nullable Instant eventTime,
    SubjectRef subjectRef,
    long subjectSequence,       // long, not int — per-subject monotonic
    long globalPosition,
    EventPriority priority,
    EventOrigin origin,
    List<EventCategory> categories,  // unmodifiable via List.copyOf()
    CausalContext causalContext,
    @Nullable Ulid actorRef,         // 14th field — nullable for system/autonomous events
    DomainEvent payload
) {}
```

**Records are immutable.** No setters. If you need a modified copy, use a builder or `with`-style method:
```java
public EventEnvelope withGlobalPosition(long position) {
    return new EventEnvelope(eventId, eventType, schemaVersion, ingestTime,
        eventTime, subjectRef, subjectSequence, position, priority, origin,
        categories, causalContext, actorRef, payload);   // 14 fields — match the record above
}
```

---

## 4. Virtual Thread Patterns (LTD-01, LTD-11)

**Spawning virtual threads for subscriber dispatch:**
```java
private final ExecutorService subscriberExecutor =
    Executors.newVirtualThreadPerTaskExecutor();

private void notifySubscribers(EventEnvelope envelope) {
    for (Subscriber subscriber : subscribers) {
        subscriberExecutor.submit(() -> {
            try {
                subscriber.onEvent(envelope);
            } catch (Exception e) {
                log.error("Subscriber {} failed on event {}",
                    subscriber.id(), envelope.eventId(), e);
            }
        });
    }
}
```

**ReentrantLock instead of synchronized:**
```java
private final ReentrantLock writeLock = new ReentrantLock();

public long append(EventEnvelope envelope) {
    writeLock.lock();
    try {
        // SQLite write — single-writer serialization
        return persistToWal(envelope);
    } finally {
        writeLock.unlock();
    }
}
```

**Named virtual threads for diagnostics:**
```java
Thread.ofVirtual()
    .name("subscriber-", 0)  // subscriber-0, subscriber-1, ...
    .factory();
```

**Structured concurrency for coordinated tasks (when applicable):**
```java
try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {
    var task1 = scope.fork(() -> queryState(entityId));
    var task2 = scope.fork(() -> queryHistory(entityId, range));
    scope.join().throwIfFailed();
    return new EntityDetail(task1.get(), task2.get());
}
```

---

## 5. SQLite via JDBC (LTD-03)

**Connection setup with required PRAGMAs:**
```java
private Connection createConnection(Path dbPath) throws SQLException {
    var conn = DriverManager.getConnection("jdbc:sqlite:" + dbPath);
    try (var stmt = conn.createStatement()) {
        stmt.execute("PRAGMA journal_mode = WAL");
        stmt.execute("PRAGMA synchronous = NORMAL");
        stmt.execute("PRAGMA cache_size = -128000");
        stmt.execute("PRAGMA mmap_size = 1073741824");
        stmt.execute("PRAGMA temp_store = MEMORY");
        stmt.execute("PRAGMA busy_timeout = 5000");
    }
    return conn;
}
```

**Prepared statements for event insertion** (simplified — the production `events` table is **25 columns** as of V001/M2-bridge; see `homesynapse-mental-model.md` §6 for the full schema, and bind `subject_sequence` with `setLong`, not `setInt`):
```java
private static final String INSERT_EVENT = """
    INSERT INTO events (
        event_id, event_type, schema_version, ingest_time, event_time,
        subject_ref, subject_sequence, priority, origin,
        correlation_id, causation_id, payload
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """;

private long insertEvent(Connection conn, EventEnvelope env) throws SQLException {
    try (var ps = conn.prepareStatement(INSERT_EVENT)) {
        ps.setBytes(1, env.eventId().toBytes());
        ps.setString(2, env.eventType());
        ps.setInt(3, env.schemaVersion());
        ps.setLong(4, env.ingestTime().toEpochMilli() * 1000); // microseconds
        ps.setObject(5, env.eventTime() != null
            ? env.eventTime().toEpochMilli() * 1000 : null);
        ps.setBytes(6, env.subjectRef().toBytes());
        ps.setInt(7, env.subjectSequence());
        ps.setString(8, env.priority().name());
        ps.setString(9, env.origin().name());
        ps.setBytes(10, env.correlationId().toBytes());
        ps.setObject(11, env.causationId() != null
            ? env.causationId().toBytes() : null);
        ps.setString(12, serializePayload(env.payload()));
        ps.executeUpdate();

        // Return the auto-assigned rowid (global_position)
        try (var keys = ps.getGeneratedKeys()) {
            keys.next();
            return keys.getLong(1);
        }
    }
}
```

**Handling the unique constraint violation (sequence conflict):**
```java
try {
    return insertEvent(conn, envelope);
} catch (SQLException e) {
    if (e.getErrorCode() == 19) { // SQLITE_CONSTRAINT
        throw new SequenceConflictException(
            "Event sequence conflict: expected next after %d, received %d for subject %s"
                .formatted(currentSequence, envelope.subjectSequence(),
                    envelope.subjectRef()));
    }
    throw e;
}
```

---

## 6. Jackson Serialization (LTD-08)

**ObjectMapper configuration:**
```java
public static ObjectMapper createMapper() {
    return JsonMapper.builder()
        .addModule(new JavaTimeModule())
        .addModule(new HomeSynapseModule())   // custom serializers
        .disable(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS)
        .disable(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES)
        .build();
}
```

**The HomeSynapse module registers ULID type serializers:**
```java
public class HomeSynapseModule extends SimpleModule {
    public HomeSynapseModule() {
        super("HomeSynapse");
        addSerializer(EntityId.class, new EntityIdSerializer());
        addDeserializer(EntityId.class, new EntityIdDeserializer());
        addSerializer(EventId.class, new EventIdSerializer());
        addDeserializer(EventId.class, new EventIdDeserializer());
        // ... other typed ID wrappers
    }
}
```

---

## 7. CausalContext Propagation

Every event carries causality information. The `EventPublisher` enforces correct propagation.

```java
// Publishing a root event (external stimulus, no prior cause)
// actorRef goes on the EventDraft, not as a separate parameter
var draft = new EventDraft(..., actorRef);  // actorRef is the 8th field
publisher.publishRoot(draft);
// → publisher constructs CausalContext.root(newEventId)
// → correlation_id = new event's own event_id
// → causation_id = null
// → envelope.actorRef() = draft.actorRef()

// Publishing a caused event (reaction to a prior event)
// actorRef inherited from causing event's envelope
var derivedDraft = new EventDraft(..., causingEnvelope.actorRef());
publisher.publish(
    derivedDraft,
    CausalContext.chain(causingEnvelope.causalContext().correlationId(),
                        causingEnvelope.eventId().value())
);
// → correlation_id = inherited from causalContext
// → causation_id = the triggering event's event_id
// → envelope.actorRef() = draft.actorRef()
```

**Never construct CausalContext manually in application code.** It flows through the system. When your subscriber receives an event, extract its CausalContext and pass it when publishing downstream events.

**Derived event time rule:** When a subscriber produces a derived event (e.g., State Projection producing `state_changed` from `state_reported`), the `eventTime` field must be **inherited from the causing event or set to null**. Never use `Instant.now()` — the publisher assigns `ingestTime` as the system timestamp. Using `Instant.now()` for `eventTime` conflates processing time with real-world occurrence time and breaks `COALESCE(event_time, ingest_time)` time-range queries.

```java
// CORRECT — inherit eventTime from the causing event
var derivedDraft = new EventDraft(
    "state_changed", 1,
    causingEnvelope.eventTime(),    // inherit, may be null
    causingEnvelope.subjectRef(),
    EventPriority.NORMAL, EventOrigin.SYSTEM,
    new StateChangedEvent(/* fields */),
    causingEnvelope.actorRef()      // inherit actorRef too
);

// WRONG — never do this for derived events
var badDraft = new EventDraft(
    "state_changed", 1,
    Instant.now(),                  // NO — this is processing time, not event time
    ...
);
```

---

## 8. SLF4J Structured Logging (LTD-15)

```java
private static final Logger log = LoggerFactory.getLogger(EventPublisherImpl.class);

// Structured context for every event-related log
log.info("Event published: type={} subject={} sequence={} correlation={}",
    envelope.eventType(),
    envelope.subjectRef(),
    envelope.subjectSequence(),
    envelope.correlationId());

// Error with full context
log.error("Subscriber {} failed processing event {} at position {}",
    subscriber.id(), envelope.eventId(), envelope.globalPosition(), exception);
```

**Rules:**
- No `System.out.println` or `System.err.println`
- Include `entity_id`, `event_type`, and `correlation_id` in event-related logs
- Use `{}` placeholders, not string concatenation
- Exception goes as the LAST argument (SLF4J auto-extracts the stack trace)

---

## 9. Error Message Voice (Register C)

Error messages use Register C: direct, neutral, no self-reference, no apology, no celebration.

```java
// GOOD — direct, factual, actionable
"Event sequence conflict: expected %d, received %d for entity %s"
"Configuration validation failed: field '%s' requires a value between %d and %d"
"Integration '%s' exceeded restart limit (%d restarts in %d seconds)"
"Entity '%s' does not support capability '%s'"

// BAD — self-referential, apologetic, vague
"Sorry, we couldn't process your event"
"HomeSynapse encountered an error while saving"
"Something went wrong with the device"
"Please try again later"
```

---

## 10. Gradle Module Conventions (LTD-10)

**Module naming:** Gradle project paths are `{group}:{name}` (e.g. `core:event-model`, `core:value-model`, `platform:platform-api`, `api:rest-api`, `integration:integration-api`); JPMS module names are `com.homesynapse.{subsystem}` (e.g. `com.homesynapse.event`, `com.homesynapse.value`). Always cross-check the JPMS name against the actual `module-info.java` — never infer it from the Gradle path or the Knowledge Primer.

**Convention plugins in `build-logic/`:**
```kotlin
// build-logic/src/main/kotlin/homesynapse.java-conventions.gradle.kts
plugins {
    java
}

java {
    toolchain { languageVersion = JavaLanguageVersion.of(21) }
}

tasks.withType<JavaCompile>().configureEach {
    options.release = 21
}
```

**Version catalogs in `gradle/libs.versions.toml`:**
```toml
[versions]
jackson = "2.18.6"
sqlite-jdbc = "3.51.2.0"
slf4j = "2.0.17"
logback = "1.5.32"
junit = "5.14.3"

[libraries]
jackson-databind = { module = "com.fasterxml.jackson.core:jackson-databind", version.ref = "jackson" }
sqlite-jdbc = { module = "org.xerial:sqlite-jdbc", version.ref = "sqlite-jdbc" }

[bundles]
jackson = ["jackson-databind", "jackson-datatype-jsr310"]
```

**Never add a dependency that isn't in `libs.versions.toml`.** If you need a new dependency, flag it as a `[REVIEW]` deviation.

---

## 11. Clock Injection and NO_DIRECT_TIME_ACCESS (Arch Rule)

HomeSynapse Core enforces an ArchUnit rule named `NO_DIRECT_TIME_ACCESS` that **applies to both production and test code** in non-whitelisted modules. The rule fails the build when any class calls:

- `Instant.now()`, `Instant.now(Clock)` with an ambient clock
- `LocalDateTime.now()`, `LocalDate.now()`, `ZonedDateTime.now()`, `OffsetDateTime.now()`
- `System.currentTimeMillis()`, `System.nanoTime()`
- `new Date()`, `Calendar.getInstance()`
- `Clock.systemUTC()`, `Clock.systemDefaultZone()`, `Clock.system(...)`

**Whitelist (the only modules allowed direct time access):**
- `com.homesynapse.app..` — composition root binds the real clock
- `com.homesynapse.platform..` — platform-api provides the `Clock` abstraction
- `com.homesynapse.test..` — test utilities that wire fixed clocks

**Everything else — including core, event-model, event-bus, device-model, persistence, state-store, integrations, AND their test sources — must receive a `java.time.Clock` via constructor injection.**

### Production code pattern

```java
public final class EventPublisherImpl implements EventPublisher {
    private final Clock clock;
    private final EventStore eventStore;

    public EventPublisherImpl(Clock clock, EventStore eventStore) {
        this.clock = Objects.requireNonNull(clock, "clock");
        this.eventStore = Objects.requireNonNull(eventStore, "eventStore");
    }

    @Override
    public EventEnvelope publishRoot(DomainEvent event) {
        Instant ingestTime = clock.instant(); // CORRECT
        // Instant ingestTime = Instant.now(); // WRONG — arch rule fails
        ...
    }
}
```

### Test code pattern — fixed clocks

Tests must never call `Instant.now()` or `Clock.systemUTC()` directly. Use `Clock.fixed(...)` with a deterministic instant:

```java
private static final Clock FIXED_CLOCK =
    Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC);

@BeforeEach
void setUp() {
    publisher = new EventPublisherImpl(FIXED_CLOCK, eventStore);
}
```

If the test needs time to advance, use a mutable test clock:

```java
MutableClock clock = MutableClock.at("2026-01-01T00:00:00Z");
publisher = new EventPublisherImpl(clock, eventStore);

publisher.publishRoot(event1);
clock.advance(Duration.ofSeconds(30));
publisher.publishRoot(event2);
```

`MutableClock` lives in the shared test utility module (`homesynapse-test`) — it's whitelisted for direct time access and exposes `advance(Duration)` and `setTo(Instant)`.

### Why the rule exists on test code

M2.2 and M2.4 shipped with production code that passed the arch rule but test code that called `Instant.now()` directly, causing nondeterministic failures on CI and masking event time vs. ingest time bugs (see `context/audits/2026-04-11_m2.5-arch-debt-retrospective.md`). The arch rule was tightened to cover `src/test/java` specifically because the violations were landing there.

**Rule for the Coder:** Before committing any new test file in a non-whitelisted module, grep it for `Instant.now`, `System.currentTimeMillis`, `new Date`, and `Clock.systemUTC`. If any match, replace with an injected `Clock.fixed(...)` or `MutableClock` before running `./gradlew check`.

---

## 12. Default Methods for Interface Evolution Under JPMS (M3.1 Pattern)

When extending an interface that has existing implementations in testFixtures (which cannot be modified in the current milestone scope), new methods must be `default` to preserve backward compatibility.

### Problem

The `EventBus` interface (4 abstract methods) has an implementation `InMemoryEventBus` in testFixtures. M3.1 needs to add 4 new methods. Making them abstract would require `InMemoryEventBus` to implement all 4 — but `InMemoryEventBus` is a Phase 2 passive fixture that cannot support active-runtime methods.

### Solution

```java
public interface EventBus {
    // Original 4 abstract methods (Phase 2)
    void subscribe(SubscriberInfo info);
    void unsubscribe(String subscriberId);
    void notifyEvent(long globalPosition);
    long subscriberPosition(String subscriberId);

    // New methods (M3.1) — default with UnsupportedOperationException
    default void subscribeRuntime(SubscriberInfo info, Subscriber subscriber) {
        throw new UnsupportedOperationException(
            "subscribeRuntime requires active runtime (InProcessEventBus)");
    }

    default void resume(String subscriberId) {
        throw new UnsupportedOperationException(
            "resume requires active runtime (InProcessEventBus)");
    }

    default Optional<SubscriberInfo> subscriberInfo(String subscriberId) {
        throw new UnsupportedOperationException(
            "subscriberInfo requires active runtime (InProcessEventBus)");
    }

    default List<SubscriberSnapshot> subscribers() {
        throw new UnsupportedOperationException(
            "subscribers requires active runtime (InProcessEventBus)");
    }
}
```

### Rules

- **The production implementation (`InProcessEventBus`) overrides ALL defaults** with real implementations. The `default` bodies exist only for backward compatibility with Phase 2 fixtures.
- **Use `UnsupportedOperationException` with a message naming the required implementation.** This makes the error actionable when someone accidentally calls a default method on the wrong implementation.
- **Do NOT use `default` methods for optional behavior.** In HomeSynapse, `default` methods are strictly an interface evolution mechanism — not a "some implementations skip this" pattern. Every production implementation must override every default.
- **Update the interface shape test** when adding default methods. The shape test should assert both total method count and abstract method count separately.
- **JPMS module boundary note:** Since `InMemoryEventBus` lives in testFixtures (a separate source set with its own compilation unit), the compiler will verify it against the interface at compile time. If you make methods abstract, `InMemoryEventBus` fails to compile even though it's not in the production source set.

#### Platform Module ≠ Auto-Required (M3.3 lesson)

JDK modules like `jdk.jfr`, `java.sql`, `java.naming`, `jdk.management` ship with the JDK (no Maven/Gradle dependency needed) but are NOT automatically available under JPMS. Only `java.base` and modules transitively reachable from your declared `requires` directives are resolved.

**Before using any JDK module type in a HomeSynapse module:**
1. Check if it's in `java.base` → no `requires` needed.
2. Trace the `module-info.java` chain from your module. Example: `com.homesynapse.event.bus` → `com.homesynapse.event` → `com.homesynapse.platform` → `java.base`. If the JDK module is not in this chain, add `requires <jdk.module>;` to your `module-info.java`.
3. No Gradle dependency change is needed — these modules ship with the JDK. Only the JPMS `requires` directive is needed.

---

## 13. JPMS Exports Discipline & the `requires transitive` ↔ Gradle `api` Lockstep

This is the most-recurring build defect in the project — **three occurrences (M2.9, M3.6e.1, M5-A)**, twice from an instruction's *embedded* `module-info`. Internalize it.

**The rule.** A `public` class in an **exported** package must not expose, on its public API surface (a supertype in `implements`/`extends`, a return type, a parameter, a public field, a thrown exception), either:
- a **package-private** type, or
- a type from a module you only `requires` (non-transitive).

Either trips `javac -Xlint:exports` → with `-Werror`, a **hard compile failure**. `-Xlint:exports` is **main-source only** — green unit tests do NOT clear it; only `compileJava` (or the full `check`) surfaces it.

**The lockstep.** `module-info.java` and `build.gradle.kts` must agree, in the same direction:
- `requires transitive X`  ⇔  `api(project(":…X"))`
- plain `requires X`        ⇔  `implementation(project(":…X"))`

If JPMS says transitive but Gradle says `implementation`, downstream modules get `module not found` at compile time; the reverse leaks a dependency you meant to hide.

**Two resolutions when a public exported type would leak a foreign/internal type:**
1. **Promote the dependency** to `requires transitive` + `api(...)` — correct when that type genuinely belongs in your module's public contract (e.g. platform-systemd's impls legitimately expose platform-api's `PlatformPaths`/`HealthReporter`; M5-A made platform-api `requires transitive` + `api`).
2. **Make the class package-private + add a public gateway** that hides the foreign type behind same-package wiring — correct when the dependency is an implementation detail (e.g. `RestFilters.installReadinessGate(Object app, …)` types the Javalin app as `Object` to keep `io.javalin` off rest-api's public surface; M3.6e.1). A `static` factory on the public interface (`StateQueryService.materialized(...)`) is the same move for construction.

**Self-check before handoff (and before the PM embeds a `module-info`):** for each public type in an exported package, does any public signature name a foreign-module or package-private type? If yes, that module needs `requires transitive` + `api`, or the type goes package-private behind a gateway. A targeted `./gradlew :module:compileJava` is the ~20s way to surface `[exports]` (and redundant-cast / unused-import) before the deferred gate does. Do **not** honor a non-transitive embed blindly when the module exports impls of another module's types — flag it as a `[REVIEW]` correction.

### `-Werror` also bites: redundant `(Type) null` casts
A `(Type) null` cast is flagged by `-Xlint:cast` (→ `-Werror`) **unless** it disambiguates a genuine overload. `new LinuxSystemPaths((Path) null)` (one single-arg ctor) → drop the cast. `new SystemdHealthReporter((String) null)` (two reference-typed ctors) → the cast is required. Decide per overload-set, not by habit (M5-A).

### Spotless reality (this repo)
The convention plugin runs only `licenseHeader` + `removeUnusedImports` + `trimTrailingWhitespace` + `endWithNewline` — **no** `googleJavaFormat` / `importOrder`. So Spotless does **not** reformat indentation or sort imports, but it **fails `check` on any unused import** (a Javadoc `{@link}` counts as usage). Match each file's existing indentation (some files are tab-indented, most are 4-space) and the byte-exact copyright header; don't hand-sort imports it won't sort (M4.C).

### Seam-isolation for JDK APIs that compile but aren't supported at runtime
When a JDK API compiles but throws at runtime on the target (e.g. JDK-21 has no AF_UNIX `SOCK_DGRAM`, so sd_notify's datagram send is unavailable), isolate the unsupported call behind a package-private seam (`interface NotifyTransport { void send(byte[]); }`), put the real impl behind it, and inject a capturing double in tests so `check` stays GREEN. The runtime gap is then confined to the composition root (the only place that constructs the real impl) — and you must say so **loudly** in the handoff + a cross-agent note, because a "looks-done" impl can otherwise hide a non-functional deployment path (M5-A; real transport deferred to M13).

**Origin:** M3.3 task instruction incorrectly said "Do NOT add `requires jdk.jfr`." Build failed. Coder corrected it. PM-originated error — see `coder-lessons.md` 2026-05-17.
