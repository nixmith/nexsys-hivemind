<!--
file: coder/references/testing-standards.md
purpose: Test-first discipline, JUnit 5 patterns, test categories, and ArchUnit rules for HomeSynapse Core.
audience: Coder
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# Testing Standards for HomeSynapse

Tests define "correct." Write them first. Make them fail. Then implement.

---

## 1. Test-First Discipline

This is a rule, not a preference. The sequence is always:

1. **Write the test** against the Phase 2 interface. The test should compile but fail (no implementation exists).
2. **Run the test.** Confirm it fails for the right reason (missing implementation, not a compilation error).
3. **Write the implementation.** Make the test pass.
4. **Refactor.** Clean up the implementation while keeping the test green.

If you find yourself writing implementation code before the test, stop. Write the test first.

---

## 2. JUnit 5 Patterns

### Test Class Naming
Mirror the production class: `EventPublisher` → `EventPublisherTest`. Integration tests: `EventPublisherIntegrationTest`. Performance tests: `EventPublisherBenchmark`.

### Test Method Naming
Describe the scenario, not the implementation:
```java
// GOOD — describes behavior
@Test
void append_withNewEntity_assignsSequenceOne() { }

@Test
void append_withExistingEntity_incrementsSequence() { }

@Test
void append_withDuplicateSequence_throwsSequenceConflict() { }

@Test
void publishRoot_setsCorrelationIdToOwnEventId() { }

@Test
void publish_inheritsCorrelationIdFromCause() { }

// BAD — describes implementation
@Test
void testInsertIntoDatabase() { }

@Test
void testHashMapContainsKey() { }
```

### Test Structure
Use Arrange-Act-Assert with blank lines between sections:
```java
@Test
void append_withNewEntity_assignsSequenceOne() {
    // Arrange
    var entityId = EntityId.generate();
    var event = new StateChanged(entityId, "brightness",
        new IntValue(0), new IntValue(100));

    // Act
    var envelope = publisher.publishRoot(event);

    // Assert
    assertThat(envelope.subjectSequence()).isEqualTo(1);
}
```

### Assertion Library
Use AssertJ for fluent assertions:
```java
assertThat(result).isNotNull();
assertThat(result.eventType()).isEqualTo("device.state_changed");
assertThat(result.globalPosition()).isGreaterThan(0);
assertThat(events).hasSize(3).extracting("eventType")
    .containsExactly("device.state_changed", "device.state_changed", "automation.triggered");
```

### Exception Testing
```java
@Test
void append_withDuplicateSequence_throwsSequenceConflict() {
    var entityId = EntityId.generate();
    publisher.publishRoot(new StateChanged(entityId, "on", off, on));

    assertThatThrownBy(() ->
        publisher.publishRoot(new StateChanged(entityId, "on", on, off)))
        .isInstanceOf(SequenceConflictException.class)
        .hasMessageContaining("sequence conflict");
}
```

---

## 3. Test Categories

### Unit Tests
Test a single class in isolation. Mock collaborators only when they cross a subsystem boundary.

**What to mock:**
- External services (network, file system for config loading)
- Other subsystem interfaces (e.g., mock `EventStore` when testing `AutomationEngine`)

**What NOT to mock:**
- SQLite — use real in-memory SQLite for persistence tests
- Records and value types — they're immutable data, not behavior
- Internal collaborators within the same subsystem

### Integration Tests
Test subsystem interactions end-to-end.

**SQLite integration test setup:**
```java
@BeforeEach
void setUp() throws SQLException {
    // In-memory SQLite — fresh database per test
    connection = DriverManager.getConnection("jdbc:sqlite::memory:");
    try (var stmt = connection.createStatement()) {
        stmt.execute("PRAGMA journal_mode = WAL");
        stmt.execute("PRAGMA synchronous = NORMAL");
    }
    createSchema(connection); // Run DDL from the design doc
    eventStore = new SqliteEventStore(connection, objectMapper);
    publisher = new EventPublisherImpl(eventStore, subscriberRegistry);
}

@AfterEach
void tearDown() throws SQLException {
    connection.close();
}
```

**For file-based SQLite tests (when WAL behavior matters):**
```java
@TempDir
Path tempDir;

@BeforeEach
void setUp() throws SQLException {
    Path dbPath = tempDir.resolve("test-events.db");
    connection = DriverManager.getConnection("jdbc:sqlite:" + dbPath);
    // WAL mode only works on real files, not :memory:
}
```

### Crash Recovery Tests
Test that the system survives kill -9 and recovers correctly.

**Pattern:**
```java
@Test
void crashRecovery_allPersistedEventsDeliveredAfterRestart() {
    // Publish events
    for (int i = 0; i < 100; i++) {
        publisher.publishRoot(createTestEvent());
    }

    // Simulate crash: destroy subscriber state but keep the event store
    subscriberRegistry.clearAllCheckpoints();

    // Restart: subscribers catch up from their last checkpoint
    subscriberRegistry.recoverAll();

    // Verify: all 100 events were delivered to subscribers
    assertThat(testSubscriber.receivedEvents()).hasSize(100);
}
```

### Performance Tests
Reference MVP §8 targets. Always document test hardware and conditions.

```java
@Test
void eventThroughput_sustainedAbove500PerSecond() {
    var start = System.nanoTime();
    int eventCount = 5_000;

    for (int i = 0; i < eventCount; i++) {
        publisher.publishRoot(createTestEvent(EntityId.generate()));
    }

    var elapsed = Duration.ofNanos(System.nanoTime() - start);
    var eventsPerSecond = eventCount / (elapsed.toMillis() / 1000.0);

    assertThat(eventsPerSecond).as("Sustained event throughput")
        .isGreaterThan(500.0);
}

@Test
void stateQueryLatency_p99Below5ms() {
    // Populate state
    populateTestEntities(50);

    var latencies = new ArrayList<Long>();
    for (int i = 0; i < 1000; i++) {
        var start = System.nanoTime();
        stateStore.getCurrentState(randomEntityId());
        latencies.add(System.nanoTime() - start);
    }

    Collections.sort(latencies);
    var p99 = latencies.get((int) (latencies.size() * 0.99));
    assertThat(Duration.ofNanos(p99).toMillis())
        .as("State query p99 latency")
        .isLessThan(5);
}
```

---

## 4. What to Test for Each Pattern

### Event Publishing
- Root event gets `correlation_id == event_id` and `causation_id == null`
- Caused event inherits `correlation_id` from cause and gets `causation_id == cause.event_id`
- `subject_sequence` increments per entity, not globally
- Duplicate `(subject_ref, subject_sequence)` throws `SequenceConflictException`
- Event is queryable from `EventStore` immediately after `publish` returns
- Subscribers receive the event after publish completes
- `ingest_time` is set by the publisher, not the caller

### Subscriber Delivery
- Subscriber receives events in `global_position` order
- Slow subscriber doesn't block other subscribers
- Subscriber crash doesn't crash the event bus
- Checkpoint persists correctly — after restart, subscriber resumes from checkpoint
- Catch-up read delivers all events between last checkpoint and current position

### State Projections
- State reflects the most recent event for each attribute
- Replaying the same events produces identical state (determinism)
- State survives checkpoint + restore
- Querying state for a nonexistent entity returns empty, not error

### Integration Adapters
- Adapter only uses `IntegrationContext` interfaces (ArchUnit test)
- Adapter crash doesn't affect core or other adapters
- Adapter restart resumes without event loss
- Adapter produces events with correct event types (within its permitted namespace)

### Configuration
- Valid YAML loads successfully
- Invalid YAML fails with a specific, actionable error message (Register C)
- Missing required fields are caught by JSON Schema validation
- Configuration reload produces `config_changed` events

---

## 5. ArchUnit Rules

Module boundary enforcement in test code:

```java
@ArchTest
static final ArchRule integrationsMustNotImportCoreInternals =
    noClasses()
        .that().resideInAPackage("..integration..")
        .should().accessClassesThat()
        .resideInAPackage("..internal..");

@ArchTest
static final ArchRule coreSubsystemsMustNotImportNetworkLibraries =
    noClasses()
        .that().resideInAPackage("..events..")
        .or().resideInAPackage("..state..")
        .or().resideInAPackage("..automation..")
        .should().accessClassesThat()
        .resideInAnyPackage("java.net..", "java.net.http..",
            "okhttp3..", "org.apache.http..");
```

---

## 6. Test Data Helpers

Create reusable test factories. Don't repeat event construction across tests:

```java
public final class TestEvents {
    private TestEvents() {} // utility class

    public static StateChanged brightness(EntityId entityId, int from, int to) {
        return new StateChanged(entityId, "brightness",
            new IntValue(from), new IntValue(to));
    }

    public static DeviceAdopted adopted(DeviceId deviceId, EntityId... entities) {
        return new DeviceAdopted(deviceId, List.of(entities));
    }
}
```

Keep test helpers in `src/test/java` in a `testutil` package. They're test infrastructure, not production code.

---

## 7. @BeforeEach Ordering — Parent-First Idiom

JUnit 5 runs `@BeforeEach` methods from the **parent class first, then the subclass**. This ordering is defined and deterministic — rely on it when building test class hierarchies where the parent sets up shared infrastructure (e.g., a SQLite connection, a fixed clock, a Jackson ObjectMapper) and the subclass layers on scenario-specific fixtures.

### Canonical pattern

```java
abstract class SqliteTestBase {
    protected Connection connection;
    protected Clock clock;

    @BeforeEach
    void setUpSqliteBase() throws SQLException {
        connection = DriverManager.getConnection("jdbc:sqlite::memory:");
        try (var stmt = connection.createStatement()) {
            stmt.execute("PRAGMA journal_mode = WAL");
            stmt.execute("PRAGMA synchronous = NORMAL");
        }
        createSchema(connection);
        clock = Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC);
    }

    @AfterEach
    void tearDownSqliteBase() throws SQLException {
        if (connection != null) connection.close();
    }
}

class EventPublisherIntegrationTest extends SqliteTestBase {
    private EventPublisher publisher;

    @BeforeEach
    void setUpPublisher() {
        // Parent @BeforeEach already ran — connection and clock are ready
        var eventStore = new SqliteEventStore(connection, objectMapper());
        publisher = new EventPublisherImpl(clock, eventStore);
    }

    @Test
    void publishRoot_persistsEventToSqlite() { ... }
}
```

### Rules

- **Do not re-initialize parent fields in the subclass `@BeforeEach`.** The parent has already set them.
- **Do not use `@BeforeAll` for SQLite connections or Clock instances.** Each test must get a fresh connection; static shared state leaks between tests.
- **Give parent and subclass `@BeforeEach` methods distinct names.** JUnit will invoke both regardless, but distinct names make the ordering obvious in stack traces.
- **If ordering matters within a single class**, use `@Order` on `@TestMethodOrder(OrderAnnotation.class)` — but prefer refactoring to avoid ordered tests entirely.
- **Mirror `@AfterEach` ordering** — JUnit runs subclass `@AfterEach` first, then parent. Close resources in the opposite order you opened them.

### Why this matters for HomeSynapse tests

Many persistence and event-bus tests need both a SQLite connection and a fixed clock. Extracting them to a shared parent class eliminates ~15 lines of duplicated setup per test class and guarantees every subclass uses the same `Clock.fixed(...)` instant, keeping deterministic event times consistent across the module's test suite.

---

## 8. Arch Rules Apply to Test Code

The `NO_DIRECT_TIME_ACCESS` ArchUnit rule (see `java-patterns.md §11`) runs against `src/test/java` in every non-whitelisted module. This means:

- **No `Instant.now()` in tests.** Inject a `Clock` (typically `Clock.fixed(...)`) and call `clock.instant()`.
- **No `System.currentTimeMillis()` for timing assertions.** Use `System.nanoTime()` only inside a `testutil` helper class that lives in the whitelisted `homesynapse-test` module.
- **No `new Date()` in test fixtures.** Use `Instant.parse("...")` with an explicit ISO-8601 string.
- **No `LocalDateTime.now()` even in assertion messages.** Format from a fixed instant.

**Before running `./gradlew check` on any new test file, grep it:**

```bash
grep -nE 'Instant\.now|System\.currentTimeMillis|new Date|Clock\.systemUTC|LocalDate(Time)?\.now' \
    src/test/java/path/to/YourTest.java
```

If the grep returns anything, fix it before the ArchUnit gate fails. This is the specific pattern that shipped arch-debt in M2.2 and M2.4 (see `context/audits/2026-04-11_m2.5-arch-debt-retrospective.md`). The arch rule was tightened in response — violations in test code now fail the build identically to production violations.

---

## 9. Contract Test Capability Hooks (M3.1 Pattern)

When a contract test base class has multiple concrete subclasses with different capability levels, use a `boolean` capability method with `assumeTrue()` guards to prevent new test tiers from breaking existing subclasses.

### Problem

`EventBusContractTest` is extended by both `InMemoryEventBusTest` (Phase 2 fixture, passive bus only) and `InProcessEventBusTest` (M3.1, full active runtime). Adding abstract methods (e.g., `createActiveRuntime()`) to the contract test would break `InMemoryEventBusTest` — it cannot implement active-runtime harness methods.

### Solution

```java
abstract class EventBusContractTest {

    // Capability hook — subclasses override to declare support
    protected boolean supportsActiveRuntime() {
        return false;  // default: no active runtime support
    }

    @Nested
    class Tier5_ModeStateMachine {
        @Test
        void subscribe_startsInColdMode() {
            assumeTrue(supportsActiveRuntime());
            // ... test body only runs for capable implementations
        }
    }
}

class InProcessEventBusTest extends EventBusContractTest {
    @Override
    protected boolean supportsActiveRuntime() {
        return true;  // this impl supports full runtime
    }
}

class InMemoryEventBusTest extends EventBusContractTest {
    // inherits default false — Tiers 5-10 are skipped via assumeTrue
}
```

### Rules

- **One capability hook per major capability boundary.** Don't add a hook for every individual test — group related tests into tiers and guard the tier.
- **Default must be `false` (least-capable).** Existing subclasses inherit the safe default without modification.
- **Use `assumeTrue()`, not `@EnabledIf`.** `assumeTrue` produces clear "test skipped" output in the JUnit report without requiring annotation processing.
- **Document the tier structure.** Use `@Nested` classes named `Tier{N}_{Description}` so the test report shows which tiers ran.

---

## 10. Interface Shape Tests

When a module has a test that asserts on interface method count or structure, that test MUST be updated when the interface is extended. Include these tests in STOP-on-Mismatch gates for any prompt that modifies an interface.

### Pattern

```java
class EventBusTest {
    @Test
    void interfaceShape_declaredMethodCount() {
        Method[] methods = EventBus.class.getDeclaredMethods();
        assertThat(methods).hasSize(8);  // 4 abstract + 4 default (M3.1)
    }

    @Test
    void interfaceShape_abstractMethodCount() {
        long abstractCount = Arrays.stream(EventBus.class.getDeclaredMethods())
            .filter(m -> Modifier.isAbstract(m.getModifiers()))
            .count();
        assertThat(abstractCount).isEqualTo(4);
    }
}
```

### Rules

- **Every interface in the module should have a shape test** that asserts total declared methods and (optionally) abstract vs default counts.
- **Shape tests live in `src/test/java`**, not testFixtures — they test a specific interface's structure, not a contract that implementations must satisfy.
- **When extending an interface, update the shape test FIRST** (test-first discipline applies here too). The shape test should fail with the old count, then pass after you add the new methods.
- **Include shape tests in Cowork prompt STOP-on-Mismatch gates.** The PM must list the shape test in "Files to Modify" for any prompt that adds methods to an interface.
