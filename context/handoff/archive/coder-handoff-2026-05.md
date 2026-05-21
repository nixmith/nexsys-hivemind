<!--
file: context/handoff/archive/coder-handoff-2026-05.md
purpose: Archived historical closeouts evicted from active coder-handoff.md as part of Batch E (2026-05-21).
audience: Coder, PM
update-cadence: frozen
state-type: history
status: ARCHIVED
last-verified: 2026-05-21 against `homesynapse-core` commit `dfb045e`
-->

# Coder Handoff — Archive 2026-05

Archived from `context/handoff/coder-handoff.md` on 2026-05-21 (Batch E; PLAN §4a). Covers closeouts 2026-05-15 → 2026-05-19.

---

## M3.4a — Integration Test Module Scaffold + Harness (2026-05-19)

**Commit:** `5ae7912`
**Build:** GREEN (full `./gradlew check`; `./gradlew :testing:integration-tests:test -PpiProfile=throttled`)
**Modules:** `testing/integration-tests` (NEW, #20); `core/persistence` (testFixtures dep additions); `core/event-bus` (testFixtures factory bridge)

### Delivered
- New Gradle module `testing/integration-tests` registered in `settings.gradle.kts`
- `testing/integration-tests/build.gradle.kts` — Pi-profile-gated test task; standard `homesynapse.library-conventions`; testImplementation deps on every production module under test + testFixtures of event-model/event-bus/state-store/persistence + test-support; sqlite-jdbc at testRuntime
- `testing/integration-tests/src/main/java/module-info.java` — empty `com.homesynapse.it` named module; tests run on the unnamed-module classpath
- `testing/integration-tests/src/test/resources/pi4-throttled.properties` — Pi-profile config
- `testing/integration-tests/src/test/java/com/homesynapse/it/IntegrationTestHarness.java` — composes the full production stack against a `@TempDir` SQLite file
- `testing/integration-tests/src/test/java/com/homesynapse/it/BurstLoadIT.java` — 500-event burst, 6 assertions
- `testing/integration-tests/src/test/java/com/homesynapse/it/HeapBudgetIT.java` — 3,000-entity heap bound, 4 assertions
- `core/persistence/build.gradle.kts` — promoted relevant testFixtures deps to `testFixturesApi` so cross-module fixture types are visible at compile time

### Deferred Build Gate
RESOLVED — full `./gradlew check` GREEN on `5ae7912`; profile-gated tests GREEN.

### Next Work Unit
M3.4b: `ThrottledWriteCoordinator`, `Pi4SustainedLoadIT`, `Pi4D1SpikeIT`, `CrashRecoveryIT`, `scripts/pi4-validation.sh`.

---

## Supervisor DLQ Wiring (2026-05-19)

**Commit:** `ed5862c`
**Build:** GREEN (full `./gradlew check`)
**Module:** `core/event-bus`

### Delivered
- `SubscriberSupervisor.deliver()` constructs `DeadLetter` (11 fields) instead of `DlqEntry` (6 fields) in the `RuntimeException` catch block
- Field construction: `subscriberId=this.subscriberId`, `sequenceKey=envelope.subjectRef().toString()` (yields `"type:id"` format), `eventPosition=envelope.globalPosition()`, `eventId=envelope.eventId().value()` (unwraps `EventId` → `Ulid`), `causeClass=e.getClass().getName()`, `causeMessage=e.getMessage() != null ? e.getMessage() : ""` (null-guard), `attemptCount=1`, `firstSeenAt=lastAttemptAt=clock.instant()`, `diagnostics=null`
- Routes through new `SubscriberDlq.park(DeadLetter)` overload — dual write to in-memory ring + `PersistentDlqWriter`
- `InProcessEventBus.subscribeRuntime()` upgraded DLQ identity: `new SubscriberDlq(info.subscriberId(), PersistentDlqWriter.noop())` instead of no-arg constructor
- `TransitionCoordinator.park(DlqEntry)` preserved — `CAUGHT_UP_TRANSITION_MARKER = -1L` is intentionally outside `DeadLetter`'s `eventPosition >= 0` domain
- New `SubscriberSupervisorTest.java` (12 test methods) — first dedicated unit test for the supervisor

### Deferred Build Gate
RESOLVED — full `./gradlew check` GREEN.

### Notes
- Source-verification audit `context/audits/2026-05-19_supervisor-dlq-source-verification.md` validated 9 assumptions before execution (1 corrected: `SubjectRef.toString()` returns `"type:id"`, not bare ULID). Saved one revision cycle.
- Retry loop (`MAX_RETRIES=5`, `computeBackoff`, `sleepForBackoff`) remains dead code per M3.1 design — `attemptCount=1` is correct for current single-attempt semantics. When the retry loop lands (M3.2-followup or M3.6), `recordCrash()` must move from per-attempt to post-exhaustion to preserve "one poison event = one crash."

---

## Projection-Checkpoint Wiring (2026-05-19)

**Commit:** `56aaa4b`
**Build:** GREEN (full `./gradlew check`)
**Module:** `core/state-store`

### Delivered
- `StateCheckpointSource` interface in `com.homesynapse.state` — `Optional<byte[]> serializeCheckpoint(int projectionVersion)`
- `StateProjection` wired to call `source.serializeCheckpoint(projectionVersion)` instead of holding the byte[0] stub from the vertical slice
- Advisory 10 MB checkpoint-size guardrail: WARN log + structured metric when serialized checkpoint exceeds 10 MB. No hard fail.

### Deferred Build Gate
RESOLVED — full `./gradlew check` GREEN.

### Notes
- Closes M3.5b independent review non-blocking concern #1 (no size guardrail on `CheckpointSerializer`).
- Composition root still owes the ALWAYS-configured ObjectMapper wiring for `SqliteStateStore` — that's M3.6 scope.

---

## M3.5b — StateProjection Production Persistence (2026-05-18)

**Commit:** `08d0136`
**Build:** GREEN at module level (`./gradlew :core:event-bus:check :core:persistence:check :core:state-store:check`); full `./gradlew check` GREEN via subsequent commits on top.
**Modules:** `core/event-bus`, `core/persistence`, `core/state-store`

### Delivered
- **event-bus (3 new public types):** `DeadLetter` (11-field record), `SubscriberMaxRetries` (record, `DEFAULT = new SubscriberMaxRetries(5)`), `PersistentDlqWriter` (interface with `noop()` factory)
- **persistence:** `SqliteStateStore` (ConcurrentHashMap-backed; eager-loads from `ViewCheckpointStore` on construction; package-private accessors `serialize(int)`, `loadedProjectionVersion()`, `viewName()` for checkpoint integration), `SqliteDeadLetterStore` (UPSERT on `(subscriber_id, event_position)`; frozen `first_seen_at`), `CheckpointSerializer` (Jackson JSON; preserves null `staleAfter` and null attribute values; explicit `HashMap.put` to avoid `Map.copyOf` null rejection), `CheckpointData` (record), `AtomicCheckpointWriter.writeAtomicCheckpointWithDlqPark()` (three-way atomic write — subscriber checkpoint + view checkpoint + DLQ park, all in one transaction)
- **persistence migration:** `V004__dlq_operational_indices.sql` (CREATE INDEX IF NOT EXISTS pattern — non-breaking)
- **persistence MODULE_CONTEXT:** ObjectMapper divergence gotcha at line 381 — `PersistenceObjectMapper.create()` is `NON_NULL`; `CheckpointSerializer` requires `ALWAYS`-configured mapper, constructed at composition time
- **state-store:** `SubscriberDlq` backward-compat — preserved no-arg constructor (delegates to `new SubscriberDlq("", PersistentDlqWriter.noop())`); new two-arg constructor takes `subscriberId` and `PersistentDlqWriter`
- **testing:** `DeadLetterStoreContractTest` (10 tests, abstract — in event-bus testFixtures), `SqliteDeadLetterStoreContractTest` (subclass), `AtomicCheckpointWriterDlqTest` (3 tests), `CheckpointSerializerTest` (12+ tests including `nullStaleAfterPreserved`, `nullAttributeValuesPreserved`, `largeStateMap` with 1,000 entities), `SqliteStateStoreTest` (12 tests including crash recovery + corrupt checkpoint recovery)

### Deferred Build Gate
RESOLVED — module-level GREEN at commit; full project GREEN via subsequent stack commits.

### Independent Review
PASS with 5 non-blocking concerns. See `context/audits/2026-05-18_m3.5b-review-report.md`. Concern #1 (no size guardrail) closed by projection-checkpoint wiring (`56aaa4b`). Remaining concerns tracked in PROJECT_SNAPSHOT.

### Notes
- The composition root must wire an ALWAYS-configured `ObjectMapper` for `SqliteStateStore` — `PersistenceObjectMapper.create()` is `NON_NULL` and will drop null `staleAfter` / null attribute values. Tracked for M3.6.
- Each ObjectMapper configuration is correct for its use case: `NON_NULL` for event payloads (compactness; nulls are absences), `ALWAYS` for checkpoints (round-trip fidelity; null is a distinct value).

---

## Bus-Fix Piece A — DerivedWriteRateLimit Visibility Promotion (2026-05-18)

**Commit:** `fceafe8`
**Build:** GREEN — implicit via subsequent M3.5b build GREEN on top.
**Module:** `core/event-bus`
**Executor:** Nick (direct one-line edit, not a Claude Code session)

### Delivered
- `DerivedWriteRateLimit` class declaration changed from package-private to `public`
- MODULE_CONTEXT update moved the row from the package-private table to the public table; row text now describes the promotion and notes which accessors remain package-private

### Notes
- Closes the G4 mismatch from M3.5a — cross-module consumers (composition root, state-store `DerivedPublishGate` method reference) can now reach the type directly.
- The `DerivedPublishGate` adapter seam introduced in M3.5a remains in place — it isolates the bus-side rate-limit primitive from state-store callers via a narrow interface; visibility promotion is orthogonal.
- The original Bus-Fix WU also included Tier 9 `reconciliationOnVersionMismatch` enablement and the `bus.resume()` VT re-spawn fix. Both deferred — they require lifecycle wiring that belongs to M3.6.

---

## Prior Milestones (Archive)

### M3.5a — StateProjection Vertical Slice (2026-05-18)

**Commit:** `a2aff9c`. First cross-module M3 milestone (state-store → event-bus). 7 new production types (StateProjection, SelfProducedFilter pkg-private, StateStore, DerivationRule, DerivationContext, DerivedPublishGate, ProjectionId). 2 testFixture fixtures (InMemoryStateStore, InMemoryProjectionAdvancer). 2 abstract contract tests (StateProjectionContractTest 9 methods, SubscriberContractTest 4 methods). 4 concrete test classes (InMemoryStateProjectionTest 13, InMemoryProjectionAdvancerTest 11, SelfProducedFilterTest 6, StateProjectionVerticalIT 5). G4 BLOCKING-RESOLVED: DerivedWriteRateLimit was package-private — DerivedPublishGate interface introduced as adapter seam. StateStore.clear() added (3-method spec expanded to 4). StateProjection.processBatch(int) added — batch entry point for advancer-driven two-phase discipline.

### M3.3 — Backpressure, Metrics, Observability (2026-05-17)

**Commit:** `a5d4b2a`. AMD-43 §3.6.1–§3.6.4. JFR-native bus metrics (7 canonical names), `QueueSaturationHealthCheck` (hysteresis), `DerivedWriteRateLimit` (token bucket). 13 new production types, 3 new test classes (27 tests), 6 Tier 10 contract tests. Type count 16→29. DEC-M3-14 (IntSupplier injection for writer queue depth), DEC-M3-15 (M3.5a STOP gate removal pattern). Build ran clean on second pass (first pass failed due to missing `requires jdk.jfr;` — PM-originated error in task instruction, corrected by Coder; lesson propagated).

### M3.2 — REPLAY→TRANSITION→LIVE (Bus-Side) — 2026-05-17

**Commit:** `0bade6a`. New files: `ReplayDriver`, `TransitionCoordinator`, `ReplayTransitionIT`. Modified: `InProcessEventBus`, `ReplayWindowQueue`, `SubscriberRuntime`, `EventBusContractTest`, event-bus MODULE_CONTEXT, .gitignore. Compound-atomic via `ReplayWindowQueue.lock()/unlock()` fuses mode-read + routing in `notifyEvent` with empty-check + CAS in `TransitionCoordinator`. Tier 5 mode-equality assertions from M3.1 relaxed (`isIn(REPLAY, TRANSITION, LIVE)`) — empty store completes COLD→LIVE in microseconds.

### AMD-38 finalization, AMD-39 withdrawal, DeploymentProfile correction (2026-05-15)

Promoted AMD-38 (checkpoint policy: 200 events / 2 s) DRAFT → APPLIED. Withdrew AMD-39 (proposed journal_size_limit raise to 64 MB). Corrected `DeploymentProfile.{STUDIO, HOME, PERFORMANCE}.journalSizeLimitBytes()` to the uniform LTD-03 value of `6_144_000L` (6 MB) validated by D1.

### D1 WAL Pathology Validation Spike (2026-05-15)

Phase 1 spike producing `D1WalStarvationTest.java` under `spike/wal-validation/`. Three runs confirming bounded-reader is load-bearing, 6 MB journal limit safe without active checkpointing.

### M2→M3 Bridge — Amendments, V003 Migration, Phase 2 Interfaces (2026-05-15)

AMD-34..40, V001→25 columns, V002 DLQ table, V003 snapshots + index drop, 10 new Java types (state-store: 5, persistence: 5).
