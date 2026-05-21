# Source Verification Report: Supervisor DLQ Wiring

**Task:** Supervisor DLQ Wiring — Source Verification & Instruction Refinement
**Date:** 2026-05-19
**Codebase state:** Commit `56aaa4b` on main, build GREEN
**Scope:** READ-ONLY verification — no code modifications

---

## STOP Gate Assessment

All five STOP gates evaluated. **None triggered.**

| STOP Gate | Result | Evidence |
|---|---|---|
| Supervisor has EventEnvelope at catch point | CLEAR | `deliver(Subscriber, EventEnvelope, SubscriberRuntime)` — envelope is a method parameter, in scope at lines 98-131 |
| Supervisor has Clock injection | CLEAR | Constructor at line 69: `SubscriberSupervisor(String subscriberId, Clock clock, SubscriberDlq dlq)` |
| DlqEntry/DeadLetter field conflict | CLEAR | DlqEntry is a strict subset (6 fields) of DeadLetter (11 fields); no overlapping semantics conflicts |
| Delivery loop handles retries externally | CLEAR — but requires nuance | The bus does NOT retry. The supervisor does NOT retry. Failed events are parked and skipped. See Section 5 for full analysis. |
| More than 5 callers of `park(DlqEntry)` | CLEAR | Exactly 2 callers: `SubscriberSupervisor.deliver()` line 102, `TransitionCoordinator.drainAndPromote()` line 155 |

---

## Section 1: Assumption Verification Matrix

| # | Assumption | Status | Evidence |
|---|---|---|---|
| A1 | Supervisor has Clock injection | **CONFIRMED** | `SubscriberSupervisor.java` constructor at line 69: `SubscriberSupervisor(String subscriberId, Clock clock, SubscriberDlq dlq)`. Clock stored as `private final Clock clock` at line 58. |
| A2 | Supervisor catches RuntimeException in deliver() | **CONFIRMED** | `deliver()` at line 98: `catch (RuntimeException e)`. Separate catch blocks for `Error` (line 121) and checked `Exception` (line 125). |
| A3 | Supervisor has access to EventEnvelope at catch point | **CONFIRMED** | `deliver()` signature at line 93: `DeliveryResult deliver(Subscriber subscriber, EventEnvelope envelope, SubscriberRuntime runtime)`. The `envelope` parameter is in scope at all three catch blocks. |
| A4 | DlqEntry is constructed with limited fields (no eventId, no sequenceKey) | **CONFIRMED** | `DlqEntry` record at `SubscriberDlq.java` line 158: `record DlqEntry(long eventPosition, String causeClass, String causeMessage, int attemptCount, Instant firstSeenAt, Instant lastAttemptAt)`. Six fields only. Missing vs DeadLetter: `dlqId`, `subscriberId`, `sequenceKey`, `eventId`, `diagnostics`. |
| A5 | Crash window is rolling 10-min/5-crash | **CONFIRMED** | `CRASH_WINDOW = Duration.ofMinutes(10)` at line 55. `CIRCUIT_BREAKER_THRESHOLD = 5` at line 52. `crashTimestamps = new ArrayDeque<>()` at line 60. `recordCrash()` evicts entries older than 10 min, adds current timestamp (lines 139-146). `crashCount()` re-evicts and returns `crashTimestamps.size()` (lines 153-159). |
| A6 | Checkpoint advancement is handled by bus delivery loop, not supervisor | **CONFIRMED** | `InProcessEventBus.liveLoop()` at lines 416-417: `checkpointStore.writeCheckpoint(subscriberId, envelope.globalPosition())` — only on `SUCCESS`. The supervisor returns `DeliveryResult` enum; it never touches `checkpointStore`. |
| A7 | CAUGHT_UP_TRANSITION uses eventPosition = -1L | **CONFIRMED** | `TransitionCoordinator.java` line 53: `static final long CAUGHT_UP_TRANSITION_MARKER = -1L`. Used at line 155-161 in the `onCaughtUp()` catch block to construct a `DlqEntry` with this marker as `eventPosition`. |
| A8 | SubjectRef.toString() gives Crockford Base32 ULID string | **CORRECTED** | `SubjectRef.java` lines 117-119: `return type.name().toLowerCase() + ":" + id`. Output format is `"entity:01HXYZ..."` — includes the SubjectType prefix, NOT just the bare ULID. |
| A9 | SubscriberMaxRetries.DEFAULT = 5 | **CONFIRMED** | `SubscriberMaxRetries.java` line 26: `public static final SubscriberMaxRetries DEFAULT = new SubscriberMaxRetries(5)`. Validates `value >= 1` in compact constructor. |

**Summary:** 8 CONFIRMED, 1 CORRECTED (A8).

---

## Section 2: Task Instruction Corrections

### CORRECTION #1: SubjectRef.toString() for sequenceKey construction

**Section affected:** DeadLetter construction in the supervisor's RuntimeException catch block

**WRONG:** The task instruction assumes `envelope.subjectRef().toString()` yields a bare Crockford Base32 ULID string suitable for the `sequenceKey` field.

**RIGHT:** `SubjectRef.toString()` returns `type.name().toLowerCase() + ":" + id` — e.g., `"entity:01HXYZ..."`. This is a type-prefixed format, not a bare ULID.

**IMPACT:** The implementation must decide which format to use for `sequenceKey`:

- **Option A — Use `SubjectRef.toString()` as-is.** The `sequenceKey` becomes `"entity:01HXYZ..."`. This is actually *better* for retry tooling: it preserves the subject type category, enabling per-type DLQ queries. AMD-36's `sequence_key` column documentation says "the per-entity sequence key (e.g., subject reference)" — `SubjectRef.toString()` IS the subject reference.
- **Option B — Use `envelope.subjectRef().id().toString()`.** The `sequenceKey` becomes just the ULID string. Leaner, but loses the type discriminator.

**PM Recommendation:** Option A. The DeadLetter Javadoc at line 56-58 explicitly says `sequenceKey` is "the per-entity sequence key (e.g., subject reference)." Using `SubjectRef.toString()` — which IS the subject reference — is the natural match. The coding instruction should specify `envelope.subjectRef().toString()` and document that this produces the type-prefixed format.

### CORRECTION #2: Retry loop does not exist — task instruction must account for single-attempt semantics

**Section affected:** The overall wiring approach

**WRONG (implicit assumption):** The task instruction context says the supervisor will "construct full DeadLetter records after exhausting retry attempts." This implies a retry loop exists that exhausts attempts before parking.

**RIGHT:** No retry loop exists in the current supervisor. `MAX_RETRIES = 5` at line 49 is **dead code**. `computeBackoff()` (line 175) and `sleepForBackoff()` (line 190) exist but are **never called**. The Javadoc at lines 78-86 explicitly states: "Does NOT retry within this call — retries are driven by the subscriber's VT loop re-delivering from the pending queue." However, the bus's `liveLoop()` does NOT re-deliver parked positions either — it just continues to the next `pendingPositions.poll()`.

**IMPACT:** In the current M3.1 implementation, every failed delivery is a single attempt that immediately parks to DLQ and moves on. The `attemptCount` is always hardcoded to `1` (line 106). The DLQ wiring WU has two options:

- **Option A — Wire DeadLetter construction at the existing single-attempt park site.** Replace the `DlqEntry` construction at lines 102-109 with a `DeadLetter` construction. `attemptCount` stays `1`. This is the minimal change that achieves the WU's goal of persistent DLQ parking.
- **Option B — Simultaneously add the retry loop.** Add the `for` loop with `MAX_RETRIES`, backoff, and attempt counting, then park to `DeadLetter` only after exhaustion. This is a larger change that goes beyond the stated WU scope.

**PM Recommendation:** Option A for this WU. The retry loop is explicitly deferred to M3.2 per the Javadoc at lines 83-86. The DLQ wiring WU should replace `park(DlqEntry)` with `park(DeadLetter)` at the existing single-attempt catch site. The `attemptCount` field should be `1` for now, and the M3.2 coding instruction will introduce the retry loop later.

---

## Section 3: Additional Watch-Out Items

### Watch-Out #1: SubscriberDlq no-arg constructor uses subscriberId=""

**Issue:** `InProcessEventBus.subscribeRuntime()` at line 256 constructs `new SubscriberDlq()` — the no-arg constructor, which sets `subscriberId = ""` (SubscriberDlq.java line 46). When the supervisor constructs a `DeadLetter`, it needs a non-empty `subscriberId`. The supervisor already has `this.subscriberId` (its own field, set at construction from `info.subscriberId()`), so it can source the subscriberId from there. However, this means the supervisor's `subscriberId` and the DLQ's `subscriberId()` will be inconsistent — the supervisor says `"state-projection-devices"` while the DLQ says `""`.

**File/line:** `InProcessEventBus.java` line 256, `SubscriberDlq.java` line 45-46.

**How Claude Code should handle it:** The supervisor should use its own `this.subscriberId` field (not `dlq.subscriberId()`) when constructing `DeadLetter`. This works correctly today. A separate concern: `InProcessEventBus.subscribeRuntime()` should migrate from `new SubscriberDlq()` to `new SubscriberDlq(info.subscriberId(), PersistentDlqWriter.noop())` so the DLQ's identity is consistent. This may or may not be in scope for this WU — the PM should decide.

### Watch-Out #2: EventId vs Ulid type mismatch

**Issue:** `DeadLetter.eventId` is typed as `Ulid` (DeadLetter.java line 81). `EventEnvelope.eventId()` returns `EventId` (EventEnvelope.java line 100), which is `record EventId(Ulid value)`. To extract the `Ulid` for DeadLetter construction, the expression is `envelope.eventId().value()`, NOT `envelope.eventId()`.

**File/line:** `DeadLetter.java` line 81 (`Ulid eventId`), `EventEnvelope.java` line 100 (`EventId eventId`), `EventId.java` line 30 (`record EventId(Ulid value)`).

**How Claude Code should handle it:** The DeadLetter construction must use `envelope.eventId().value()` to unwrap the `EventId` wrapper and extract the raw `Ulid`. This is a compile error if done wrong, so it will be caught, but the coding instruction should specify the correct expression to avoid a discovery loop.

### Watch-Out #3: DeadLetter.causeMessage requires non-null

**Issue:** `DeadLetter`'s compact constructor at line 111 validates `Objects.requireNonNull(causeMessage, ...)`. But `RuntimeException.getMessage()` can return `null` (e.g., `new NullPointerException()` with no message). The current `DlqEntry` construction at line 105 passes `e.getMessage()` directly without null-guarding. This works because `DlqEntry` has no validation. But `DeadLetter` will reject null.

**File/line:** `DeadLetter.java` line 111, `SubscriberSupervisor.java` line 105.

**How Claude Code should handle it:** The DeadLetter construction must null-guard the cause message: `e.getMessage() != null ? e.getMessage() : ""`. The TransitionCoordinator already handles this pattern at lines 152-154 with a null check and fallback to `t.getClass().getSimpleName()`. The coding instruction should specify the null-guard pattern.

### Watch-Out #4: diagnostics field decision

**Issue:** `DeadLetter` has a nullable `diagnostics` field (line 88) described as "free-form diagnostic text (e.g., serialized stack trace)." The coding instruction needs to decide what to put here. Options: `null`, a truncated stack trace, or the exception's `toString()`. This is a product-level decision that affects operator tooling.

**File/line:** `DeadLetter.java` line 88.

**How Claude Code should handle it:** PM should specify the value. Recommendation: pass `null` for M3.1 simplicity. Stack trace serialization adds complexity (string conversion, truncation policy, memory pressure) that belongs in a future enhancement. The field is nullable precisely for this reason.

### Watch-Out #5: Two callers of park(DlqEntry) — TransitionCoordinator also needs consideration

**Issue:** The task instruction focuses on `SubscriberSupervisor.deliver()` as the park site to rewire. But `TransitionCoordinator.drainAndPromote()` at lines 155-161 also calls `park(DlqEntry)` for the `onCaughtUp()` synthetic failure. This is a separate concern — the onCaughtUp DLQ entry uses `CAUGHT_UP_TRANSITION_MARKER = -1L` as the eventPosition, which would fail DeadLetter's `eventPosition >= 0` validation.

**File/line:** `TransitionCoordinator.java` lines 155-161, `DeadLetter.java` line 114.

**How Claude Code should handle it:** Do NOT convert the TransitionCoordinator's `park(DlqEntry)` call to `park(DeadLetter)` in this WU. The synthetic marker with `eventPosition = -1L` is intentionally outside DeadLetter's domain. The `park(DlqEntry)` method must be preserved (not deprecated) for this use case. Only the supervisor's call site should be rewired.

### Watch-Out #6: Import for Ulid type

**Issue:** `SubscriberSupervisor.java` currently does not import `com.homesynapse.platform.identity.Ulid` or `com.homesynapse.event.EventId` or `com.homesynapse.event.SubjectRef`. It only imports `com.homesynapse.event.EventEnvelope`. To construct a `DeadLetter`, it will need to access `envelope.eventId().value()` (returning `Ulid`) and `envelope.subjectRef()` (returning `SubjectRef`). Since `EventEnvelope` is already imported and the method chains resolve through it, the supervisor may need to add an import for `DeadLetter` (which is in the same package, so no import needed) but DOES need to verify that `Ulid` is accessible through the JPMS module graph.

**File/line:** `SubscriberSupervisor.java` imports at lines 7-16, `module-info.java`.

**How Claude Code should handle it:** Check that the `event-bus` module's `module-info.java` already requires `platform-api` (for `Ulid`) and `event-model` (for `EventEnvelope`, `SubjectRef`, `EventId`). `DeadLetter` is in the same package — no import needed. The key new import would be `com.homesynapse.platform.identity.Ulid` only if used directly in a type declaration; if only used as a method-chain return type, it may not need an explicit import (but best practice is to add it).

---

## Section 4: Crash Window vs MaxRetries Interaction Analysis

### 4.1: What exactly counts as a "crash" in the current implementation?

Every `RuntimeException` caught in `deliver()` counts as a crash. The flow is:

1. `subscriber.onEvent(envelope)` throws `RuntimeException` (line 98)
2. `dlq.park(new DlqEntry(...))` — parks the event (lines 102-109)
3. `recordCrash(now)` — adds a timestamp to the crash window (line 112)
4. `crashCount() >= CIRCUIT_BREAKER_THRESHOLD` check (line 115)

There is no distinction between "park-worthy" and "crash-worthy" exceptions. Every `RuntimeException` is both parked AND counted as a crash. `Error` and checked `Exception` bypass the crash window entirely — they go straight to `SUSPENDED` via `INFRASTRUCTURE_FAILURE`.

### 4.2: If the supervisor parks an event to DLQ (successfully), should that count as a crash?

**Argument for YES (current behavior):** A DLQ park is evidence of subscriber dysfunction. Five poison events in 10 minutes is a credible signal that the subscriber is fundamentally broken, not just encountering isolated bad data. The circuit breaker exists to protect the system from a subscriber that's churning through events and failing on all of them. If you don't count parks as crashes, a subscriber with a systematic bug could poison-park thousands of events without ever tripping the breaker.

**Argument for NO:** A successful DLQ park means the system handled the failure gracefully — the poison event was quarantined. The crash window should only count events that represent *system instability*, not graceful degradation. If the subscriber encounters 5 genuinely unprocessable events (corrupt payloads, for instance) over 10 minutes during normal operation, suspending it punishes the subscriber for correctly encountering bad data.

**Assessment:** The current behavior (YES) is correct for M3.1 where there is no retry loop. Every RuntimeException is a single-attempt failure immediately parked. With the M3.2 retry loop, this question becomes more nuanced: should each individual retry attempt count as a crash, or only the final exhaustion? The answer should be: **only the final DLQ park after retry exhaustion should count as one crash.** If each retry attempt counted as a crash, then a single poison event with 5 retries would trip the circuit breaker by itself.

### 4.3: Can 5 consecutive DLQ parks trigger SUSPENDED?

**Yes, absolutely.** In the current implementation, 5 RuntimeExceptions within 10 minutes triggers `SUSPENDED` regardless of whether they are for the same event or different events. Each park calls `recordCrash()`. After 5 parks, `crashCount() >= 5` returns true, and the supervisor returns `CIRCUIT_BREAKER_TRIPPED`.

**Is this desirable?** For M3.1 (no retries), yes — it's the only protection against runaway failure. For M3.2+ (with retries), the interaction needs redesign: a single poison event with 5 retry attempts should not trip the breaker. The `recordCrash()` call should move from the per-attempt site to the post-exhaustion park site.

### 4.4: Recommendation

**For this WU (DLQ wiring, no retry loop change):** Keep the current behavior. Every RuntimeException records a crash AND parks a DlqEntry (now DeadLetter). The `recordCrash()` call stays at its current location (line 112), immediately after the park call. This is the correct M3.1 behavior.

**For M3.2 (when the retry loop is added):** Move `recordCrash()` to execute only after the retry loop exhausts `MAX_RETRIES`. Individual retry attempts within the backoff loop should NOT call `recordCrash()`. This way, one poison event = one crash, regardless of how many retries it took. The circuit breaker then correctly measures "how many distinct events have we failed to process in 10 minutes" rather than "how many delivery attempts have failed."

**Design note for the coding instruction:** The DLQ wiring WU should NOT move `recordCrash()`. It should leave it exactly where it is (line 112). The M3.2 retry-loop WU will restructure the `catch (RuntimeException e)` block with the retry `for` loop, and at that point `recordCrash()` moves to the post-exhaustion path. Splitting this across two WUs keeps each change minimal and testable.

---

## Section 5: Checkpoint Advancement Path

### 5.1: How does the cursor advance after successful delivery?

The complete path for a successful live-mode delivery:

1. **`liveLoop()`** polls `runtime.pendingPositions().poll()` → gets a `Long position` (line 386)
2. The position is loaded from the event store via `runtime.readExecutor().executeRead(...)` → gets an `EventEnvelope` (lines 394-400)
3. Filter check: `filter.matches(envelope)` — if false, loop continues to next poll without checkpoint (lines 409-411)
4. `runtime.supervisor().deliver(runtime.subscriber(), envelope, runtime)` → returns `DeliveryResult` (lines 413-415)
5. **On `SUCCESS` only:** `checkpointStore.writeCheckpoint(subscriberId, envelope.globalPosition())` at line 417
6. Lag metrics recorded (lines 419-429)
7. Loop continues to next `pendingPositions.poll()`

The position is consumed from the `pendingPositions` queue by `poll()` at step 1. Once polled, it is gone from the queue regardless of delivery outcome. The checkpoint write at step 5 is the only durable record of progress.

### 5.2: After the supervisor parks an event and returns PARKED, does the bus advance past it?

**Yes and no — this is the critical subtlety.**

**Queue advancement:** Yes. The position was already removed from `pendingPositions` by `poll()` at line 386. The loop continues to `poll()` the next position. The parked event will not be re-delivered from the queue.

**Checkpoint advancement:** No. The `liveLoop()` only writes a checkpoint on `SUCCESS` (line 416). On `PARKED` or `CIRCUIT_BREAKER_TRIPPED`, no checkpoint is written. This means:

- If the subscriber restarts (JVM crash, resume after SUSPENDED), it will replay from the last checkpointed position
- The parked event's position will be re-encountered during replay
- The same event will fail again and be re-parked (or, with M3.2 retries, re-attempted)

**This is intentional.** The checkpoint gap ensures no event is permanently lost — even events that fail delivery will be re-encountered after restart. The DLQ serves as an in-memory (and soon persistent) record that the event was seen and failed, but the checkpoint gap preserves the ability to re-attempt on restart.

**However, there is a consequence the coding instruction should note:** After a parked event, the next successful delivery WILL advance the checkpoint past the parked event's position (since `globalPosition` is monotonically increasing). So the "re-encounter on restart" guarantee only applies if the subscriber suspends or crashes BEFORE processing any later event successfully. In steady-state operation where only occasional events fail, the checkpoint will advance past failed positions as later events succeed.

### 5.3: What return type does supervisor.deliver() have?

`DeliveryResult deliver(Subscriber subscriber, EventEnvelope envelope, SubscriberRuntime runtime)` — returns the `DeliveryResult` enum (defined at lines 224-233):

```
enum DeliveryResult {
    SUCCESS,
    PARKED,
    CIRCUIT_BREAKER_TRIPPED,
    INFRASTRUCTURE_FAILURE
}
```

The bus uses the return value to decide whether to write a checkpoint (only on `SUCCESS`). On `CIRCUIT_BREAKER_TRIPPED`, the mode is already set to `SUSPENDED` by the supervisor (line 116), and the `liveLoop()` will exit on the next iteration's mode check (line 382). On `INFRASTRUCTURE_FAILURE`, same — mode set to `SUSPENDED` by the supervisor (lines 123, 129).

**For the DLQ wiring WU:** No change needed to the return type or the bus's checkpoint logic. The supervisor will continue returning `PARKED` after parking a `DeadLetter` instead of a `DlqEntry`. The bus's behavior is unchanged.

---

## Section 6: Recommended Test Approach

### 6.1: Available test infrastructure

From `InProcessEventBusTest.java`:

- **`MutableClock`** — test clock with controllable time (imported, not local to the test). Satisfies `NO_DIRECT_TIME_ACCESS`.
- **`InMemoryEventStore`** — in-memory event store implementation for fast tests
- **`InMemoryCheckpointStore`** — in-memory checkpoint store
- **`RecordingReadConnectionFactory`** — creates `SubscriberReadExecutor` instances that record access patterns
- **`BusMetricsRecorder`** — recording implementation of `BusMetrics` for assertion
- **`EventBusContractTest`** — abstract contract test base class (in `testFixtures` source set) that `InProcessEventBusTest` extends

No dedicated `SubscriberSupervisorTest.java` exists anywhere in the test tree. The supervisor is currently tested only indirectly through `InProcessEventBusTest`.

### 6.2: Cleanest test approach

**Recommendation: Create a dedicated `SubscriberSupervisorTest.java` unit test.**

Rationale:

- The supervisor is the unit being modified. Direct unit testing gives precise control over inputs (envelope, subscriber behavior) and precise assertion over outputs (DeadLetter field values, crash window state, DeliveryResult).
- Integration testing through `InProcessEventBus` is too indirect — you'd need to set up the full bus, publish events, subscribe, trigger failures, then inspect the DLQ. The bus adds layers of complexity (replay, transition, live loop) that obscure the supervisor's behavior.
- The supervisor's constructor takes only 3 dependencies: `String subscriberId`, `Clock clock`, `SubscriberDlq dlq`. All three are trivially constructable in a test without mocking.

**Suggested test structure:**

```
SubscriberSupervisorTest
├── deliver_success_returnsSuccess()
├── deliver_runtimeException_parksDeadLetterWithCorrectFields()
├── deliver_runtimeException_nullMessage_usesEmptyString()
├── deliver_runtimeException_recordsCrash()
├── deliver_fiveCrashesInWindow_tripsCircuitBreaker()
├── deliver_crashesOutsideWindow_doNotCount()
├── deliver_error_returnInfrastructureFailure_noDeadLetter()
├── deliver_checkedException_returnInfrastructureFailure_noDeadLetter()
├── deadLetter_fieldsMatchEnvelopeContext()
├── deadLetter_sequenceKeyUsesSubjectRefToString()
├── deadLetter_eventIdUnwrapsFromEventId()
├── deadLetter_dlqIdIsUnassigned()
├── deadLetter_attemptCountIsOne()
```

**Test dependencies (all real, no mocks needed):**
- `Clock.fixed(...)` or `MutableClock` for deterministic time
- `new SubscriberDlq()` — real in-memory DLQ ring
- A trivial `Subscriber` lambda that throws on demand
- A test `EventEnvelope` constructed with known values
- A trivial `SubscriberRuntime` (or a minimal stub that captures `transitionTo()` calls)

### 6.3: Test helpers to reuse

- **`MutableClock`** — already exists in the test infrastructure. Use it for crash window tests that need time advancement.
- **`InMemoryEventStore`** — not needed for direct supervisor tests, but available if integration tests are added.
- **Test `EventEnvelope` construction** — check if a builder or factory exists in the test fixtures. If not, construct directly using the record constructor (14 fields). The `EventBusContractTest` likely has helper methods for creating test envelopes.

**Note:** The `NO_DIRECT_TIME_ACCESS` ArchUnit rule applies to test code in `com.homesynapse.event.bus`. All tests MUST use `Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC)` or `MutableClock`. Do NOT use `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()`.

---

## Section 7: Type Count Verification (H5)

### Raw counts

**Top-level Java source files** in `core/event-bus/src/main/java/com/homesynapse/event/bus/` (excluding `package-info.java` and `module-info.java`): **32 files**.

**Inner/nested types** found in those files:

1. `SubscriberDlq.DlqEntry` — package-private inner record (line 158)
2. `SubscriberSupervisor.DeliveryResult` — package-private inner enum (line 224)
3. `InProcessEventBus.PassiveRegistration` — private inner record (line 494)

**Total types:** 32 top-level + 3 inner = **35 types**.

### Visibility breakdown

**Public types (14):**

1. `BusMetrics` (interface)
2. `CheckpointStore` (interface)
3. `DeadLetter` (record)
4. `DerivedWriteRateLimit` (final class)
5. `EventBus` (interface)
6. `PersistentDlqWriter` (interface)
7. `Subscriber` (interface)
8. `SubscriberInfo` (record)
9. `SubscriberMaxRetries` (record)
10. `SubscriberMode` (enum)
11. `SubscriberReadConnectionFactory` (interface)
12. `SubscriberReadExecutor` (interface)
13. `SubscriberSnapshot` (record)
14. `SubscriptionFilter` (record)

**Package-private top-level types (18):**

1. `BusMetricsJfr`
2. `BusPublishLatencyEvent`
3. `BusPublisherBlockedEvent`
4. `BusSubscriberLagEvent`
5. `BusWriteAcceptedEvent`
6. `BusWriteParkedEvent`
7. `BusWriterQueueDepthEvent`
8. `HealthLevel`
9. `HealthSignal`
10. `InProcessEventBus`
11. `NoopBusMetrics`
12. `QueueSaturationHealthCheck`
13. `ReplayDriver`
14. `ReplayWindowQueue`
15. `SubscriberDlq`
16. `SubscriberRuntime`
17. `SubscriberSupervisor`
18. `TransitionCoordinator`

### Verdict

The **MODULE_CONTEXT.md header count of 32** (14 public + 18 package-private) refers to top-level types only and is **correct** for top-level source files. If the count is meant to include inner types, the actual total is 35. The review report's claim of 33 is incorrect — the count is either 32 (top-level only) or 35 (including inner types).

**Recommendation:** MODULE_CONTEXT.md should clarify whether its count includes inner types. If it does, update to 35. If top-level only (the more common convention), 32 is accurate.

---

## Summary of Findings for PM Action

### Before issuing the coding instruction:

1. **Specify `envelope.subjectRef().toString()`** for the `sequenceKey` field (CORRECTION #1). Document that this produces `"entity:01HXYZ..."` format.
2. **Clarify that this WU does NOT add a retry loop** (CORRECTION #2). The `attemptCount` stays `1`. The `park(DeadLetter)` replaces `park(DlqEntry)` at the existing single-attempt site.
3. **Add Watch-Outs #1-#6** to the coding instruction's "What to Watch Out For" section. Critical ones: `EventId.value()` unwrap (#2), `causeMessage` null-guard (#3), do not touch TransitionCoordinator's `park(DlqEntry)` (#5).
4. **Specify `diagnostics = null`** in the DeadLetter construction (Watch-Out #4).
5. **Include the `NO_DIRECT_TIME_ACCESS` ArchUnit reminder** for test code (§4c).
6. **Recommend creating `SubscriberSupervisorTest.java`** as a new dedicated unit test class.

### Design decisions confirmed:

- Crash window behavior: no changes for this WU (Section 4.4)
- Checkpoint advancement: no changes needed (Section 5)
- DeliveryResult enum: no changes needed (Section 5.3)
- `park(DlqEntry)` method: preserved for TransitionCoordinator use, not deprecated (Watch-Out #5)
