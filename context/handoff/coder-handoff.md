<!--
file: context/handoff/coder-handoff.md
purpose: Coder session continuity — current task, deferred build gate, next WU, recent closeouts.
audience: Coder, PM
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# Coder Session Handoff

**Last updated:** 2026-05-20 (M3.6d-a delivered — Independent satellite changes for the composition root; M3.6d split into d-a + d-b)

Canonical Coder handoff file referenced by the nexsys-coder skill (`../context/handoff/coder-handoff.md`). A duplicate at `homesynapse-core/docs/handoff/coder-handoff.md` (created during a Cowork session) was consolidated into this file on 2026-05-15 and removed.

---

## Deferred Build Gate

**Status:** ZERO OPEN — all resolved at commit. M3.6a (`17c40b6`), M3.6b (`df2743a`), M3.6c (`38d3e30`), and M3.6d-a (`25bc23b`) all reached GREEN at their respective commit times. The prior "FOUR OPEN" framing was inaccurate: it conflated "Nick has not yet run the build" with "the build gate is open." A.6a/b/c were GREEN at commit (verified post-hoc); only M3.6d-a was actually pending Nick's verification at the time this section was written. All four are now PM-accepted and GREEN.

### Resolved at commit

### M3.6d-a — Composition-Root Satellite Changes (2026-05-20)
**Commit:** `25bc23b`. **Build:** GREEN at HEAD (full `./gradlew check` PASS, 137 actionable tasks). Resolved 2026-05-20 after SLF4J follow-up fix.

**Follow-up patch (2026-05-20, same session):** Nick's first `./gradlew check` failed with `package org.slf4j does not exist` at `SharedScheduler.java:18–19`. Root cause: the lifecycle module-info added during M3.6d-a did NOT declare `requires org.slf4j`, and SLF4J was not transitively available because persistence/state-store both declare it at `implementation` scope (not propagated to consumers). Fix: added `requires org.slf4j;` (non-transitive, matching the persistence/state-store pattern) to `lifecycle/lifecycle/src/main/java/module-info.java` plus `implementation(libs.slf4j.api)` to `lifecycle/lifecycle/build.gradle.kts`. `lifecycle/lifecycle/MODULE_CONTEXT.md` updated to document both. No code changes to `SharedScheduler.java` — the SLF4J usage is correct, only the dependency declaration was missing. This pattern is exactly the trap documented in coder-lessons.md M3.4b entry #4 ("SLF4J transitivity under `implementation` scope") — the lifecycle module needed the same explicit declaration that state-store and persistence both have.

`./gradlew check` and `./gradlew :testing:integration-tests:test -PpiProfile=throttled` were NOT run in-session — Nick owns the compile gate per project CLAUDE.md. The change spans 4 modified production files (+1 doc-only Javadoc edit), 1 new public interface, 1 new public record, 2 new package-private classes, 2 new test files, 2 modified test files, 1 modified module-info (+1 follow-up edit), 1 modified build.gradle.kts (+1 follow-up edit), and MODULE_CONTEXT updates across 4 modules (+1 follow-up edit).

**Commands Nick must run against the working tree:**
1. `./gradlew :core:persistence:check` — verifies `SqliteStateStore` now compiles with `implements StateCheckpointSource`, the renamed `serializeCheckpoint(int)` method (3 callsites updated in `SqliteStateStoreTest`), and the promoted-to-public `loadedProjectionVersion()`. `StateCheckpointSource` is already in scope via the existing `requires com.homesynapse.state` directive.
2. `./gradlew :core:event-bus:check` — verifies the three visibility promotions (`QueueSaturationHealthCheck`, `HealthSignal`, `HealthLevel` all now `public`), the un-disabled Tier 9 `reconciliationOnVersionMismatch` contract test (subscribe → process → unsubscribe → externally reset checkpoint → re-subscribe → assert full re-replay), and that the removal of `import org.junit.jupiter.api.Disabled` left no other usages.
3. `./gradlew :core:state-store:check` — verifies the new `ReadinessSource` interface compiles (transitive `SubscriberMode` from event-bus is in scope) and that `ReconciliationTest` passes its 4 tests (upgrade mismatch discards, allow-stale-snapshots preserves, idempotent across instances, downgrade mismatch discards).
4. `./gradlew :lifecycle:lifecycle:check` — verifies the three new types compile, the new module-info `requires transitive` directives resolve, and `SharedSchedulerTest` passes its 5 tests (refill cadence, tick cadence, shutdown without throwing, shutdown idempotent, task-failure-survives-cadence).
5. `./gradlew check` (full project) — catches any consumer that broke against the SqliteStateStore method rename (none expected — `SqliteStateStore` is package-private, only `SqliteStateStoreTest` calls `serialize(int)`).
6. `./gradlew :testing:integration-tests:test -PpiProfile=throttled` — verifies the existing integration tests still pass after the event-bus visibility promotions (no behavioural change expected).

**Risk profile:** Low–medium. The risks are:
- **(a)** The Tier 9 reconciliation test is new and exercises a code path (unsubscribe → externally reset checkpoint → re-subscribe with same ID) that hasn't been explicitly covered before. If the bus's `subscribeRuntime` does not correctly re-read the checkpoint on the second subscription, the test will fail and reveal a real defect. The test deliberately uses 5-second `awaitMode` budgets to absorb scheduling variance.
- **(b)** `SharedSchedulerTest`'s cadence tests rely on `Thread.sleep` + counter assertions. CI scheduling variance could produce flakes if the test machine is heavily contended; the `>=` lower-bound assertions provide some margin.
- **(c)** The promotion of three event-bus types to `public` is a one-way API expansion — once shipped, downstream code may depend on them. The brief authorized only `QueueSaturationHealthCheck` promotion; `HealthSignal` and `HealthLevel` were promoted only because `-Xlint:exports` would have failed otherwise (see Deviation D-1 in the Completion Report).

**Out-of-session scope:** The brief asked for a full composition root (PersistenceFactory + HomeSynapseCore + wiring). Reading the actual codebase revealed the assumed prerequisites do not exist:
- `SqlitePersistenceLifecycle` does not construct `SqliteStateStore` or `SqliteDeadLetterStore` and does not expose a `WriteCoordinator` accessor.
- `WriteCoordinator` has no `queueSize()` method (the `IntSupplier` in the bus's 7-arg constructor needs one).
- No production `SubscriberReadConnectionFactory` exists — only the testFixtures `RecordingReadConnectionFactory`.
- `HealthSignal` and `HealthLevel` are package-private (the brief said `QueueSaturationHealthCheck` promotion was "clean — no `-Xlint:exports` risk").
- `SubscriberInfo` and `SubscriptionFilter` constructor shapes differ from the brief's snippets (no `displayName` field; 3rd `SubscriptionFilter` arg is `SubjectType`, not a String).

Per the user's M3.6d sub-divide decision (Option A), this WU (M3.6d-a) delivers only the independent satellite changes. M3.6d-b will land the `PersistenceFactory` + `HomeSynapseCore` wiring after the persistence-side infrastructure work it depends on.

### M3.6c — Per-Module Event-Class Manifests (2026-05-20)
**Commit:** `38d3e30`. **Build:** GREEN at HEAD (full `./gradlew check` PASS). Resolved 2026-05-20.

`./gradlew check` and `./gradlew :testing:integration-tests:test -PpiProfile=throttled` were NOT run in-session — Nick owns the compile gate per project CLAUDE.md ("You do NOT run builds, compilation, or tests"). The change spans 1 new production file + 4 modified files across `core/event-model`, `integration/integration-api`, `core/persistence` (test sources), and `testing/integration-tests` (test sources). No `module-info.java` files were modified — all dependency edges already existed.

**Commands Nick must run against the working tree:**
1. `./gradlew :core:event-model:check` — verifies `EventTypes` still compiles cleanly with the new `CORE_PRODUCTION_EVENT_CLASSES` field and the updated class-level Javadoc; existing `EventTypeAnnotationTest` and `EventTypesTest` remain unchanged.
2. `./gradlew :integration:integration-api:check` — verifies the new `IntegrationEvents` public final class compiles, the existing `IntegrationEventTypeAnnotationTest` still passes against the same 5 lifecycle subtypes, and `module-info.java` exports `com.homesynapse.integration` (unchanged).
3. `./gradlew :core:persistence:check` — verifies `AllEventClasses` still compiles with the new aggregation pattern (now imports `EventTypes` and `IntegrationEvents` instead of 27 individual class imports) and all existing callers (`EventTypeRegistryTest`, `EventPayloadCodecTest`, `JacksonWarmupTest`, `SqliteEventStoreTest`, `SqlitePersistenceLifecycleTest`, `EventCategoryMappingTest`) still resolve `AllEventClasses.ALL_EVENTS` / `CORE_EVENTS` / `INTEGRATION_EVENTS` correctly.
4. `./gradlew :testing:integration-tests:test -PpiProfile=throttled` — verifies `IntegrationTestHarness.ALL_PRODUCTION_EVENT_CLASSES` still resolves to the same 27 classes after the refactor and that `BurstLoadIT`, `HeapBudgetIT`, `Pi4SustainedLoadIT`, `Pi4D1SpikeIT`, and `CrashRecoveryIT` continue to pass.
5. `./gradlew check` (full project) — catches any unexpected consumer that imported the now-redundant 27 individual event class imports from `IntegrationTestHarness` or `AllEventClasses` (none expected; both files only used the imports internally).

**Risk profile:** Very low. The aggregation is behaviour-preserving: `EventTypes.CORE_PRODUCTION_EVENT_CLASSES` is exactly the same 22 classes in the same order as the previous inline list, and `IntegrationEvents.LIFECYCLE_EVENT_CLASSES` is exactly the same 5 classes. The composition is `Stream.concat(...).toList()` which produces an immutable `List` (`List.copyOf` semantics under the hood — same as `List.of(...)` callers rely on). No ArchUnit rules are affected. No `module-info.java` files modified — `core/persistence`'s and `testing/integration-tests`' test source sets already had `testImplementation(project(":integration:integration-api"))` in `build.gradle.kts`.

### M3.6b — ReplayWindowQueue Capacity Parameterisation + EventBusConfig (2026-05-20)
**Commit:** `df2743a`. **Build:** GREEN at HEAD (full `./gradlew check` PASS). Resolved 2026-05-20.

`./gradlew check` and `./gradlew :testing:integration-tests:test -PpiProfile=throttled` were NOT run in-session — Nick owns the compile gate per project CLAUDE.md ("You do NOT run builds, compilation, or tests"). The change spans 1 new production file + 2 new test files + 5 modified files inside `core/event-bus` (and 0 modifications to `testing/integration-tests` — the integration harness keeps using `InProcessEventBusFactory.createWithMetrics(...)` which now delegates to `createWithConfig(..., EventBusConfig.HOME_DEFAULT)` so observed behaviour is unchanged).

**Commands Nick must run against the working tree (HEAD will be set when Nick commits):**
1. `./gradlew :core:event-bus:compileJava` — DEC-M3-16 visibility-promotion verification. If this fails with `-Xlint:exports` warnings, STOP and report the exact method and leaked type per the brief's "Pre-promotion verification" — the factory approach would be needed instead.
2. `./gradlew :core:event-bus:check` — module-level GREEN; verifies `EventBusConfigTest` (4 tests), `ReplayWindowQueueTest` (4 tests), the renamed `replayWindowOverflowAtConfiguredCapacityIsCriticalAlert` Tier-9 contract test, and the existing `InProcessEventBusTest`/`InMemoryEventBusTest` suites.
3. `./gradlew check` (full project) — catches any unexpected cross-module consumer that constructed `InProcessEventBus` directly (only `InProcessEventBusTest` does, in-package) or that referenced `InProcessEventBus.PUBLISHER_BLOCKED_DEPTH_THRESHOLD` (no such consumers grep'd at instruction time).
4. `./gradlew :testing:integration-tests:test -PpiProfile=throttled` — verifies `BurstLoadIT` (M3.4a) and the M3.4b sustained-load tests still pass on `EventBusConfig.HOME_DEFAULT`.

**Risk profile:** Low. Surface is confined to `core/event-bus`. The 10,000 / 5,000 defaults are preserved exactly via `EventBusConfig.HOME_DEFAULT`, so behavioural risk is limited to (a) the `-Xlint:exports` check on the `public` class declaration (verified in pre-promotion analysis: every `EventBus` interface method uses public types), and (b) the contract-test rename (renamed test still exercises identical scenario, just with derived thresholds). NO_DIRECT_TIME_ACCESS verified locally via grep — no `Instant.now`/`Clock.systemUTC()`/`System.currentTimeMillis()` invocations introduced.

### M3.6a — Profile-Driven Persistence Configuration (2026-05-19)
**Commit:** `17c40b6`. **Build:** GREEN at HEAD (full `./gradlew check` PASS). Resolved 2026-05-20.

`./gradlew check` and `./gradlew :testing:integration-tests:test -PpiProfile=throttled` were NOT run in-session — Nick owns the compile gate per project CLAUDE.md ("You do NOT run builds, compilation, or tests"). The change spans 13 modified files + 1 new file across `core/persistence` and `testing/integration-tests`.

**Commands Nick must run against the working tree (HEAD will be set when Nick commits):**
1. `./gradlew :core:persistence:check` — verifies the constructor/PRAGMA refactor + the new per-profile PRAGMA verification tests.
2. `./gradlew :testing:integration-tests:test -PpiProfile=throttled` — verifies `BurstLoadIT` and `HeapBudgetIT` still pass on `PersistenceConfig.HOME_DEFAULT` (the prior implicit default made explicit).
3. `./gradlew check` (full project) — catches any unexpected consumer of the old `DatabaseExecutor(int, Clock)` or `SqlitePersistenceLifecycle(Path, int, Clock, HomeId, List)` signature outside `core/persistence` and `testing/integration-tests`.

**Risk profile:** Low — surface is constrained to two modules and all known call sites were updated. Highest risk is an arch-rule regression in a test file (NO_DIRECT_TIME_ACCESS) — verified locally via grep, no `Instant.now`/`Clock.systemUTC()`/`System.currentTimeMillis()` invocations introduced.

### Prior deferred gates — RESOLVED

- **M3.1 (2026-05-17):** Resolved at M3.2 commit — `./gradlew :core:event-bus:check` GREEN.

### Prior deferred gates — RESOLVED

- **M3.1 (2026-05-17):** Resolved at M3.2 commit — `./gradlew :core:event-bus:check` GREEN.
- **M3.2 (2026-05-17):** Resolved — `./gradlew :core:event-bus:check` GREEN on `0bade6a`.
- **M3.3 (2026-05-17):** Resolved — `./gradlew :core:event-bus:check` GREEN on second pass at `a5d4b2a`.
- **M3.5a (2026-05-18):** Resolved — full `./gradlew check` passed on `a2aff9c`.
- **Bus-Fix Piece A (2026-05-18):** Resolved — implicit via subsequent M3.5b build GREEN on top of `fceafe8`.
- **M3.5b (2026-05-18):** Resolved — module-level GREEN at `08d0136`; full project GREEN through subsequent commits.
- **Projection-checkpoint wiring (2026-05-19):** Resolved — full `./gradlew check` GREEN on `56aaa4b`.
- **Supervisor DLQ wiring (2026-05-19):** Resolved — full `./gradlew check` GREEN on `ed5862c`.
- **M3.4a (2026-05-19):** Resolved — full `./gradlew check` GREEN on `5ae7912`; `./gradlew :testing:integration-tests:test -PpiProfile=throttled` GREEN.
- **M3.4b (2026-05-19):** Resolved — `./gradlew check` and `./gradlew :testing:integration-tests:test -PpiProfile=throttled -PsustainedMinutes=10` GREEN on `adf04d2`.
- **DeploymentProfile correction (2026-05-15):** Nick ran `./gradlew check` — passed.
- **D1 WAL Pathology Validation Spike (2026-05-15):** Nick ran `:spike:wal-validation:compileJava`, `:spotlessCheck`, and `:runD1` on 2026-05-15. All three gates passed.
- **M2→M3 Bridge interface specifications (2026-05-15 earlier session):** 10 new Java types (state-store: 5, persistence: 5) + V003 migration compiled cleanly; full `./gradlew check` passed.

---

## Current Task

None. Awaiting M3.6d-b coding instruction from PM. M3.6a/b/c/d-a all committed and GREEN at HEAD `25bc23b`. PM is producing a revised M3.6d-b instruction addressing the three OR-M3-14 prerequisite infrastructure gaps (SqlitePersistenceLifecycle store-construction expansion, `WriteCoordinator.queueSize()`, production `SubscriberReadConnectionFactory`).

## Last Completed Milestone

**M3.6d-a — Composition-Root Satellite Changes** (2026-05-20). Build gate DEFERRED (see Deferred Build Gate section).

Files delivered (3 new production types + 1 new public test + 1 new public production interface + 1 modified disabled test + 4 modified production files + 1 modified test + 1 module-info + 1 build.gradle.kts + 4 MODULE_CONTEXT files):

**`core/persistence`:**
- `SqliteStateStore.java` (MODIFIED) — added `implements com.homesynapse.state.StateCheckpointSource`; renamed `serialize(int)` → `serializeCheckpoint(int)` (public, `@Override`); promoted `loadedProjectionVersion()` to public (`@Override`). Class-level Javadoc updated. The class itself stays package-private; composition root will expose the same instance via the two interface types.
- `SqliteStateStoreTest.java` (MODIFIED) — 3 callsites updated from `serialize(int)` to `serializeCheckpoint(int)`.

**`core/event-bus`:**
- `QueueSaturationHealthCheck.java` (MODIFIED) — class declaration `final class` → `public final class`; constructor `public`; `tick()` method `public`; `CHANNEL_SATURATING` and `CHANNEL_RECOVERED` constants `public`. DEC-M3-16 part 3.
- `HealthSignal.java` (MODIFIED) — record `record HealthSignal(...)` → `public record HealthSignal(...)`; compact constructor `public`. Promoted because `QueueSaturationHealthCheck`'s public constructor takes `Consumer<HealthSignal>` and `-Xlint:exports` would have failed otherwise. **Deviation D-1.**
- `HealthLevel.java` (MODIFIED) — `enum HealthLevel` → `public enum HealthLevel`. Promoted with `HealthSignal` (same `-Xlint:exports` chain).
- `EventBusContractTest.java` (MODIFIED, testFixtures source set) — removed `@Disabled("M3.5a")` from Tier 9 `reconciliationOnVersionMismatch`; implemented test body (publish 10 events → subscribe → wait LIVE → unsubscribe → externally reset checkpoint to 0 → re-subscribe → assert all 10 events re-replayed). Removed now-unused `import org.junit.jupiter.api.Disabled`.

**`core/state-store`:**
- `ReadinessSource.java` (NEW) — public interface with single method `SubscriberMode mode()`. Composition root implements via delegation to `StateProjection.currentMode()`. M3.6e's `MaterializedStateQueryService` consumes it for REST/WebSocket gating.
- `ReconciliationTest.java` (NEW) — focused concrete test class in `src/test/java/com/homesynapse/state/`. 4 of the brief's 5 reconciliation tests implemented (upgrade mismatch discards checkpoint, allow_stale_snapshots preserves, idempotent across repeated mismatch, downgrade also discards). 5th brief test (`reconciliationRecordsMetadataInDataSlot`) deferred as a documented feature gap — see Deviation D-2.

**`lifecycle/lifecycle`:**
- `HomeSynapseConfig.java` (NEW) — public record with 2 fields (`PersistenceConfig persistence`, `EventBusConfig eventBus`); compact constructor enforces non-null; `HOME_DEFAULT` constant pairs `PersistenceConfig.HOME_DEFAULT` with `EventBusConfig.HOME_DEFAULT`.
- `SharedScheduler.java` (NEW) — package-private final class. Two constructors: production form takes `DerivedWriteRateLimit + QueueSaturationHealthCheck`; test-friendly form takes `Runnable refillTask + Runnable tickTask` (the production form delegates to it). `Executors.newSingleThreadScheduledExecutor` with daemon thread `hs-sched-0`. `scheduleAtFixedRate` for both tasks (50 ms refill, 1 s tick). Tasks wrapped in `safelyInvoke` so a thrown RuntimeException is logged but does NOT cancel the schedule. `shutdown()` calls `shutdownNow()` + `awaitTermination(2 s)`; idempotent.
- `ThrowingStateQueryService.java` (NEW) — package-private final class implementing `StateQueryService`. All 5 methods throw `IllegalStateException(NOT_WIRED_MESSAGE)` where `NOT_WIRED_MESSAGE = "StateQueryService not yet wired — available after M3.6e"`.
- `SharedSchedulerTest.java` (NEW) — 5 tests (refill cadence, tick cadence, shutdown without throwing, shutdown idempotent, task-failure-survives-cadence).
- `module-info.java` (MODIFIED) — added `requires transitive` for `com.homesynapse.persistence`, `com.homesynapse.event.bus`, `com.homesynapse.state`.
- `build.gradle.kts` (MODIFIED) — added `api` deps for the same three modules + `testImplementation(project(":testing:test-support"))`.

**MODULE_CONTEXT.md updates:**
- `core/persistence/MODULE_CONTEXT.md` — SqliteStateStore row updated (now implements StateCheckpointSource; method rename + promotion documented).
- `core/event-bus/MODULE_CONTEXT.md` — header type count 16 public + 17 package-private → 19 public + 14 package-private; QueueSaturationHealthCheck/HealthSignal/HealthLevel moved conceptually to public table (entries added in public table; pointer left in package-private table for navigation); Tier 9 disabled-count updated 5 active+1 disabled → 6 active; two new gotchas (tick() now public; HealthSignal/HealthLevel promotion chain).
- `core/state-store/MODULE_CONTEXT.md` — header type count 19 → 20; new "M3.6d-a Readiness-source seam" subsection with `ReadinessSource` entry; total file count 21 → 22; new M3.6d-a deliverables section in Phase 3 Cross-Module Context.
- `lifecycle/lifecycle/MODULE_CONTEXT.md` — header rewritten from "Scaffold" to "7 public + 2 package-private types"; new module-info dependencies listed and explained; build.gradle.kts updated; new "M3.6 Composition-Root Primitives (M3.6d-a)" subsection with three new type entries; new "M3.6d-a deliverables" Phase 3 Note.

**STOP Gate Results:**
- G1 (SqlitePersistenceLifecycle 5-arg constructor): ✓ — package-private, 5-arg production constructor confirmed (line 125–133).
- G2 (InProcessEventBus 7-arg public constructor): ✓ — public class, public 7-arg constructor confirmed (line 140–158).
- G3 (QueueSaturationHealthCheck pre-promotion verification): ✗ **FAILED** — `HealthSignal` and `HealthLevel` are package-private. Per the brief's pre-promotion STOP gate, this should have stopped the work. Resolved by promoting both transitively. Documented in Deviation D-1.
- G4 (SqliteStateStore current state): ✓ — package-private; serialize(int) was package-private; loadedProjectionVersion() was package-private; did NOT yet implement StateCheckpointSource. All three confirmed before modification.
- G5 (StateProjection.create 11-param): ✓ — exactly 11 params confirmed (line 208–219).
- G6 (StateQueryService 5 methods): ✓ — exactly 5 methods confirmed.
- G7 (lifecycle module-info baseline): ✓ — confirmed `com.homesynapse.persistence`, `com.homesynapse.event.bus`, `com.homesynapse.state` not yet required before this WU.
- G8 (Tier 9 `@Disabled("M3.5a")` location): ✓ — confirmed at line 1473–1478 in EventBusContractTest.java.

**Deviations:**

- **D-1 [REVIEW] — promoted `HealthSignal` AND `HealthLevel` to public (brief only authorized `QueueSaturationHealthCheck`).** The brief asserted the QueueSaturationHealthCheck promotion was "clean — no `-Xlint:exports` risk" and listed the pre-promotion STOP gate. Reading the source revealed both `HealthSignal` (a record carried in the constructor's `Consumer<HealthSignal>` parameter) and `HealthLevel` (the enum nested in the record) are package-private. Per Java's accessibility rules, a public class cannot expose package-private types through its public constructor without `-Xlint:exports` warnings (which become errors under `-Werror`). The minimum-viable promotion was therefore a 3-class chain, not 1. The promotions are pure visibility changes — no behaviour, signature, or contract changes. PM should verify against DEC-M3-16 whether the broader chain matches design intent.

- **D-2 [INFO] — `ReconciliationTest` ships with 4 of the brief's 5 tests; `reconciliationRecordsMetadataInDataSlot` is deferred as a feature gap.** The brief described a test that asserts reconciliation metadata (reconciledAt, fromVersion, toVersion) is recorded in the checkpoint data blob. Reading `StateProjection.writeCheckpoint(Instant)` shows it passes plain `projectionVersion` to `checkpointSource.serializeCheckpoint(int)` — there is no API surface on `StateCheckpointSource` to receive the three metadata fields, and `SqliteStateStore.serializeCheckpoint(int)` passes `null` for the three optional metadata args to `CheckpointSerializer.serialize(...)`. Recording reconciliation metadata in the data slot is a real feature gap, not a test issue. Implementing it requires: extending `StateCheckpointSource` with an overload (or a tracker callback), threading the metadata through `StateProjection.initialize`'s reconciliation path so the NEXT `writeCheckpoint` after reconciliation passes the captured `reconciledAt`/`fromVersion`/`toVersion` values, and an updated `SqliteStateStore` that forwards them. **Recommendation:** track this as a separate enhancement WU after M3.6d-b.

- **D-3 [INFO] — `SharedScheduler` has a second constructor taking two `Runnable`s for testability.** The brief specified a single constructor `(DerivedWriteRateLimit, QueueSaturationHealthCheck)`. Both collaborators are `final` classes, so they cannot be mocked. The clean test pattern is a package-private secondary constructor taking the two scheduled tasks as `Runnable`s; the production constructor delegates by method-reference (`rateLimit::refill`, `healthCheck::tick`). This preserves the brief's specified constructor signature exactly while making the scheduler unit-testable.

- **D-4 [INFO] — `SharedSchedulerTest` ships with 5 tests, not 4.** The brief's 4 tests (refill cadence, tick cadence, shutdown < 2 s, shutdown idempotent) are all present. A 5th test (`taskFailureDoesNotSilenceCadence`) verifies that `SharedScheduler.safelyInvoke` correctly catches a thrown `RuntimeException` so the scheduler keeps firing — without this, a single transient fault would silently disable the rate limiter or the saturation health check. The test pattern was added because `ScheduledExecutorService.scheduleAtFixedRate` cancels future executions of a throwing task by default, and `safelyInvoke` is the load-bearing defence.

- **D-5 [INFO] — `shutdownTerminatesWithin2Seconds` renamed to `shutdownTerminatesWithoutThrowing` to honor NO_DIRECT_TIME_ACCESS.** The brief's test name implies measuring elapsed wall-clock time, which would require `System.nanoTime()` (banned in non-whitelisted modules per the arch rule). The test instead delegates the timing guarantee to `SharedScheduler.shutdown()` itself, which calls `executor.awaitTermination(2_000ms)`; the test merely verifies `shutdown()` returns without throwing within the JUnit per-test budget.

- **D-6 [INFO] — Major scope reduction from original M3.6d brief.** Per the user's Option A decision after pushback (logged in this session), M3.6d was sub-divided into M3.6d-a (this WU — independent satellite changes) and M3.6d-b (the next WU — `PersistenceFactory` + `HomeSynapseCore` wiring). The M3.6d-a delta is exactly the work that does NOT depend on `SqlitePersistenceLifecycle` constructing new stores, `WriteCoordinator.queueSize()`, or a production `SubscriberReadConnectionFactory`. See the M3.6d-a Deferred Build Gate section's "Out-of-session scope" paragraph for the gap analysis.

**M3.6d-a Lessons:**

1. **Pre-promotion verification must check transitively, not just the class being promoted.** The brief stated DEC-M3-16 part 3 promotion was "clean," meaning the class declaration could simply gain the `public` modifier. Reading the source revealed three transitively package-private types in the constructor's parameter type chain (`HealthSignal` carries `HealthLevel`). A class promotion is only clean if every type appearing in its public method signatures (constructors, methods, fields) is itself already public — checking the class itself is insufficient. The cost of missing this: a build that compiles cleanly today but fails the next time `-Werror` runs.

2. **Sub-dividing a large WU when prerequisites are missing is better than guessing.** The original M3.6d brief assumed prerequisites that did not exist: persistence-side construction of `SqliteStateStore` and `SqliteDeadLetterStore`, a `WriteCoordinator.queueSize()` method, a production `SubscriberReadConnectionFactory`, public `HealthSignal`/`HealthLevel`. The user's Option A (sub-divide) let M3.6d-a land the independent satellite changes cleanly while M3.6d-b can address the prerequisites as a focused next WU. Pattern: when a brief's "Files to Create or Modify" table grows past ~18 entries during discovery, sub-dividing is usually the right move — large WUs compound risk and review burden.

3. **`final` collaborators in a constructor require a test-friendly secondary constructor.** `DerivedWriteRateLimit` and `QueueSaturationHealthCheck` are both `final` (correctly so — they have invariant state). The production constructor `SharedScheduler(DerivedWriteRateLimit, QueueSaturationHealthCheck)` cannot be unit-tested directly because the collaborators cannot be mocked. The clean pattern is a package-private overload `SharedScheduler(Runnable, Runnable)` accepting the two scheduled tasks directly; the production form wraps `rateLimit::refill` and `healthCheck::tick` and delegates. This preserves the brief's specified production API while making the scheduler testable.

### Prior Last-Completed Milestone

**M3.6c — Per-Module Event-Class Manifests** (2026-05-20). Build gate DEFERRED (see Deferred Build Gate section).

Files delivered (1 new + 4 modified):

- `integration/integration-api/src/main/java/com/homesynapse/integration/IntegrationEvents.java` (NEW) — public final utility class with `private` constructor and single `public static final List<Class<? extends DomainEvent>> LIFECYCLE_EVENT_CLASSES` constant listing the 5 `IntegrationLifecycleEvent` subtypes (`IntegrationStarted`, `IntegrationStopped`, `IntegrationHealthChanged`, `IntegrationRestarted`, `IntegrationResourceExceeded`). Class-level Javadoc cites M3.6c, DECIDE-04, and Q3 gap closure; explains forcing-function semantics.
- `core/event-model/src/main/java/com/homesynapse/event/EventTypes.java` (MODIFIED — see Deviation D-1) — added one `public static final List<Class<? extends DomainEvent>> CORE_PRODUCTION_EVENT_CLASSES` field listing the same 22 core `DomainEvent` payload records that previously lived inline in `IntegrationTestHarness.ALL_PRODUCTION_EVENT_CLASSES` and `AllEventClasses.CORE_EVENTS`. New `import java.util.List;`. Class-level Javadoc updated to describe the dual role (string constants + class manifest); the existing 46 string constants are untouched. New section header `// ========== Core Production Event Class Manifest (M3.6c, DECIDE-04) ==========`.
- `core/persistence/src/test/java/com/homesynapse/persistence/AllEventClasses.java` (MODIFIED) — replaced the inline `List.of(...)` lists with `EventTypes.CORE_PRODUCTION_EVENT_CLASSES` / `IntegrationEvents.LIFECYCLE_EVENT_CLASSES` aliases. `ALL_EVENTS` now constructed via `Stream.concat(EventTypes.CORE_PRODUCTION_EVENT_CLASSES.stream(), IntegrationEvents.LIFECYCLE_EVENT_CLASSES.stream()).toList()` — the same aggregation pattern the M3.6d composition root will perform. All 27 individual event class imports removed; new imports for `EventTypes`, `IntegrationEvents`, and `java.util.stream.Stream`. Field names `CORE_EVENTS`, `INTEGRATION_EVENTS`, `ALL_EVENTS` preserved unchanged because 7 caller sites (`EventTypeRegistryTest`, `EventPayloadCodecTest`, `JacksonWarmupTest`, `SqliteEventStoreTest`, `SqlitePersistenceLifecycleTest`, `EventCategoryMappingTest`) reference them. Class Javadoc updated to describe the M3.6c aliasing.
- `testing/integration-tests/src/test/java/com/homesynapse/it/IntegrationTestHarness.java` (MODIFIED) — replaced the 27-element inline `List.of(...)` with the same `Stream.concat(...).toList()` aggregation pattern. All 22 core event imports removed plus the 5 fully-qualified `com.homesynapse.integration.*` references; new imports for `EventTypes`, `IntegrationEvents`, and `java.util.stream.Stream`. Field Javadoc updated to cite the canonical per-module manifests.
- `core/event-model/MODULE_CONTEXT.md` (MODIFIED) — `EventTypes` row updated: kind unchanged (still `final class (utility, no instantiation)`), purpose updated to "Canonical registry of core event type string constants AND the canonical roster of core event payload classes (M3.6c)", key-details cell extended to describe the new `CORE_PRODUCTION_EVENT_CLASSES` field, its role in the composition root, DECIDE-04 + ArchUnit Rule 3 enforcement, and the forcing-function semantics. Type count unchanged (47) because the field is added to an existing class, not a new type.
- `integration/integration-api/MODULE_CONTEXT.md` (MODIFIED) — header type count 21 → 22; opening paragraph updated to mention the new utility class; new "Utility Classes (1)" section added immediately after "Exception (1)" with the `IntegrationEvents` row (purpose, dependency relationship with `EventTypes`, DECIDE-04 enforcement, forcing-function semantics).

**STOP Gate Results:**
- G1: `IntegrationTestHarness.ALL_PRODUCTION_EVENT_CLASSES` count = 27 (22 core + 5 integration) ✓ matches design doc
- G2: `AllEventClasses` exists in `core/persistence/src/test/java/...`; it is a `final class` (utility, package-private, private constructor) with three `static final List<Class<? extends DomainEvent>>` fields (`CORE_EVENTS`, `INTEGRATION_EVENTS`, `ALL_EVENTS`) ✓
- G3: `core/event-model/src/main/java/module-info.java` exports `com.homesynapse.event` ✓ (line 7)
- G4: `integration/integration-api/src/main/java/module-info.java` exports `com.homesynapse.integration` ✓ (line 25)

**Count Verification (post-modification):**
- `EventTypes.CORE_PRODUCTION_EVENT_CLASSES.size()` = 22 ✓ (matches prior `IntegrationTestHarness.ALL_PRODUCTION_EVENT_CLASSES` core slice and `AllEventClasses.CORE_EVENTS` content exactly)
- `IntegrationEvents.LIFECYCLE_EVENT_CLASSES.size()` = 5 ✓
- `AllEventClasses.ALL_EVENTS.size()` = 27 ✓ (preserved)
- `IntegrationTestHarness.ALL_PRODUCTION_EVENT_CLASSES.size()` = 27 ✓ (preserved)

**Deviations:**
- **D-1 [REVIEW] — `EventTypes` MODIFIED rather than CREATED.** The PM's coding instruction said CREATE `core/event-model/src/main/java/com/homesynapse/event/EventTypes.java`, but the file already exists as the M2.1-added holder for the 46 `@EventType`-string constants (referenced by every annotation and registered with `EventTypeRegistry`). The most natural fit is to add the new `CORE_PRODUCTION_EVENT_CLASSES` constant to the existing `EventTypes` class — both the string constants and the class list are forms of "the canonical core event roster," and keeping them in one class avoids splitting the canonical place across two siblings. The alternative (a new `EventClasses` sibling) would have diverged further from both the design-doc naming and the PM's specified file path. Behavioral contracts are preserved; the public API gains exactly one new field. The Javadoc and MODULE_CONTEXT.md were updated to describe the dual role. **PM should verify** that this resolution matches their intent for the design-doc text, and confirm whether the design doc §5 should be retroactively annotated to reflect that `EventTypes` already existed at M3.6c-time.
- **D-2 [INFO] — Field name `AllEventClasses.ALL_EVENTS` preserved (PM brief said `AllEventClasses.ALL`).** The existing field is `ALL_EVENTS`; renaming would have broken 6 caller sites for no semantic gain. The aggregation pattern (Stream.concat) is applied exactly as specified; only the field name differs from the brief.
- **D-3 [INFO] — `AllEventClasses.CORE_EVENTS` / `INTEGRATION_EVENTS` preserved as upstream-aliasing fields.** The brief did not specify whether to keep these constants. Two of them (`CORE_EVENTS` and `INTEGRATION_EVENTS`) are used by `EventTypeRegistryTest` independently of `ALL_EVENTS`. Keeping them as aliases to the new manifests (rather than removing them) preserves the test API while still exercising the manifest pattern.

**M3.6c Lessons:**

1. **Pre-existing class with matching name is a structural conflict, not a coder choice.** When a PM coding instruction says CREATE but the target file already exists with a different purpose, the conflict is the right thing to surface — but the resolution is usually clear from intent: merge the roles if they're semantically adjacent (both = "canonical roster of core events"), or escalate if they're not. Always cite the existing file's role in the deviation report so the PM can verify the merger preserved their design-doc intent.

2. **Field-name preservation when refactoring test utilities.** When refactoring a test-only constant that has many callers in the same module, preserve the field name even if a brief specifies a different one. Renames force unrelated edits across the test suite and add noise to the diff; the brief's name was almost certainly illustrative rather than load-bearing. Flag the divergence as `[INFO]` for transparency.

### Prior Last-Completed Milestone

**M3.6b — ReplayWindowQueue Capacity Parameterisation + EventBusConfig** (2026-05-20). Build gate DEFERRED (see Deferred Build Gate section).

Files delivered (1 new production type + 2 new tests + 5 modified):

- `core/event-bus/src/main/java/com/homesynapse/event/bus/EventBusConfig.java` (NEW) — public record with 2 fields (`replayQueueCapacity`, `publisherBlockedDepthThreshold`), compact constructor `>= 1` validation, `HOME_DEFAULT = new EventBusConfig(10_000, 5_000)` constant.
- `core/event-bus/src/main/java/com/homesynapse/event/bus/ReplayWindowQueue.java` (MODIFIED) — new `ReplayWindowQueue(int maxCapacity)` constructor with `maxCapacity >= 1` validation; no-arg form retained and delegates with `MAX_CAPACITY = 10_000`. `MAX_CAPACITY` promoted to `public` and re-documented as the default-value reference; `enqueue()` now checks the instance `maxCapacity` field. Javadoc updated to describe the parameterisation and cite M3.6b / audit D4-09.
- `core/event-bus/src/main/java/com/homesynapse/event/bus/InProcessEventBus.java` (MODIFIED) — class declaration promoted from package-private to `public` (DEC-M3-16). New canonical public 7-arg constructor `(EventStore, CheckpointStore, Clock, SubscriberReadConnectionFactory, BusMetrics, IntSupplier, EventBusConfig)`. Existing 4-arg and 6-arg constructors remain package-private and delegate (4-arg → 6-arg → 7-arg) with `EventBusConfig.HOME_DEFAULT`. The static `PUBLISHER_BLOCKED_DEPTH_THRESHOLD = 5000` constant removed; replaced with instance `final int publisherBlockedDepthThreshold` initialised from `config.publisherBlockedDepthThreshold()`. `subscribeRuntime` constructs the per-subscriber `ReplayWindowQueue` with `config.replayQueueCapacity()`.
- `core/event-bus/src/testFixtures/java/com/homesynapse/event/bus/InProcessEventBusFactory.java` (MODIFIED) — added `createWithConfig(EventStore, CheckpointStore, Clock, SubscriberReadConnectionFactory, BusMetrics, IntSupplier, EventBusConfig) → EventBus`. Existing `create(...)` and `createWithMetrics(...)` retained and delegate with `EventBusConfig.HOME_DEFAULT`. Class Javadoc updated to reflect the M3.6b visibility promotion.
- `core/event-bus/src/testFixtures/java/com/homesynapse/event/bus/test/EventBusContractTest.java` (MODIFIED) — Tier-9 `replayWindowOverflowAt10000IsCriticalAlert` renamed to `replayWindowOverflowAtConfiguredCapacityIsCriticalAlert`; the overflow publish count and unique-delivery assertion now derive from `EventBusConfig.HOME_DEFAULT.replayQueueCapacity()` instead of literal 10,000. Added `EventBusConfig` to the imports list.
- `core/event-bus/src/test/java/com/homesynapse/event/bus/EventBusConfigTest.java` (NEW) — 4 tests covering `HOME_DEFAULT` exposing the prior hard-coded values, and three validation rejections (zero capacity, zero threshold, negative capacity).
- `core/event-bus/src/test/java/com/homesynapse/event/bus/ReplayWindowQueueTest.java` (NEW) — 4 tests: overflow at custom capacity (5), default-capacity backward compatibility (10,000 — slow but verifies the legacy bound directly), constructor rejects zero, constructor rejects negative.
- `core/event-bus/MODULE_CONTEXT.md` (MODIFIED) — header type count 32 → 33; new `EventBusConfig` row in the public-types table (16 public types); `InProcessEventBus` row moved out of the package-private table into the public-types table (with the new 7-arg constructor and the `publisherBlockedDepthThreshold` instance-field note); `ReplayWindowQueue` row updated to describe the parameterised constructor; `InProcessEventBusFactory` row in the testFixtures section gained the `createWithConfig` overload; new M3.6b Phase 3 Note block added immediately before "Performance targets".

**STOP Gate Results:**
- G1: `ReplayWindowQueue.MAX_CAPACITY = 10_000` confirmed; previously package-private `static final`; single no-arg constructor ✓
- G2: `InProcessEventBus` previously `final class` (package-private); two constructors (4-arg, 6-arg); `PUBLISHER_BLOCKED_DEPTH_THRESHOLD = 5000` constant present ✓
- G3: `InProcessEventBusFactory` public class with `create(...)` + `createWithMetrics(...)` factory methods ✓

**Deviations:** None. SD-1 (default unchanged) preserved via `HOME_DEFAULT`. SD-2 (two-field config) preserved — no third field added. SD-3 (backward compat) preserved via delegation chain; the test-time integration harness (`testing/integration-tests/IntegrationTestHarness`) needed zero modifications because `createWithMetrics(...)` is the entry point and it now delegates with `HOME_DEFAULT`. SD-4 (DEC-M3-16 visibility promotion) applied to `InProcessEventBus`.

**DEC-M3-16 Visibility Verification:** Deferred to Nick's compile gate. Pre-promotion audit (in-session): every method on `InProcessEventBus` is either an `EventBus` interface override (all 8 use public types — `String`, `long`, `SubscriberInfo`, `Subscriber`, `SubscriberSnapshot`, `List<SubscriberSnapshot>`) or a package-private method (`subscribeWithHandler`, `reset`) which doesn't fall under `-Xlint:exports` because it isn't part of the public API of the module. Expected outcome: PASS.

### Prior Last-Completed Milestone

**M3.6a — Profile-Driven Persistence Configuration** (2026-05-19). Build gate DEFERRED (see Deferred Build Gate section).

Files delivered (1 new + 13 modified):
- `core/persistence/src/main/java/com/homesynapse/persistence/LockingMode.java` (NEW) — package-private enum `NORMAL`/`EXCLUSIVE`. Cited in `DeploymentProfile.lockingMode()` accessor and `DatabaseExecutor.connectionPragmas(profile)`.
- `core/persistence/src/main/java/com/homesynapse/persistence/DeploymentProfile.java` (MODIFIED) — added 3 fields: `busyTimeoutMs` (5,000 ms uniform), `lockingMode` (`NORMAL` uniform), `readThreadCount` (2/2/4 for STUDIO/HOME/PERFORMANCE). Six fields total; accessor count goes from 3 → 6. `lockingMode()` is package-private; the rest are public.
- `core/persistence/src/main/java/com/homesynapse/persistence/DatabaseExecutor.java` (MODIFIED) — production constructor changed from `(int readThreadCount, Clock)` to `(DeploymentProfile, Clock)`; decorator overload from `(int, Clock, Function)` to `(DeploymentProfile, Clock, Function)`. Hardcoded `CONNECTION_PRAGMAS` list replaced by `connectionPragmas(profile)` rendering method — 8 elements for NORMAL, 9 for EXCLUSIVE. `journal_mode = WAL` remains mandatorily first. `cache_size` rendered as `-<profile.cacheSizeKiB()>`. Constructor validates `profile.readThreadCount() ∈ [1, 8]` (LTD-03 ceiling).
- `core/persistence/src/main/java/com/homesynapse/persistence/SqlitePersistenceLifecycle.java` (MODIFIED) — production constructor changed from `(Path, int, Clock, HomeId, List)` to `(Path, PersistenceConfig, Clock, HomeId, List)`; decorator overload follows. `start()` passes `config.profile()` into `DatabaseExecutor`. Package-private visibility preserved (do not promote to public — 5 `-Xlint:exports` errors).
- `core/persistence/src/main/java/com/homesynapse/persistence/PersistenceLifecycle.java` (MODIFIED) — interface Javadoc scrubbed of `WAL`/`PRAGMA`/`SQLite`/`sqlite` outside `@see` tags. Replaced with engine-neutral phrasing ("Opens databases, runs migrations, prepares connections"; "Closes connections, flushes pending writes, releases resources"). Implementation class retains SQLite-specific Javadoc.
- `core/persistence/src/testFixtures/java/com/homesynapse/persistence/PersistenceTestHarness.java` (MODIFIED) — all three factories (`start`, `startWithWriteCoordinator`, `startThrottled`) now accept `PersistenceConfig` instead of `int readThreadCount`.
- `core/persistence/src/test/java/com/homesynapse/persistence/DatabaseExecutorTest.java` (MODIFIED) — added 3 per-profile PRAGMA verification tests (STUDIO/HOME/PERFORMANCE) + 1 locking_mode default-not-emitted test. Existing PRAGMA assertions rewritten to derive expected values from the profile. Replaced literal `2`/`3` integers in `DatabaseExecutor(...)` calls with `DeploymentProfile.HOME`/`DeploymentProfile.PERFORMANCE`.
- `core/persistence/src/test/java/com/homesynapse/persistence/SqlitePersistenceLifecycleTest.java` (MODIFIED) — `READ_THREAD_COUNT = 2` replaced with `CONFIG = PersistenceConfig.HOME_DEFAULT`. `createLifecycle()` passes `CONFIG` through.
- `core/persistence/src/test/java/com/homesynapse/persistence/AtomicCheckpointWriterTest.java` (MODIFIED) — `READ_THREAD_COUNT` → `PROFILE = DeploymentProfile.HOME`.
- `core/persistence/src/test/java/com/homesynapse/persistence/AtomicCheckpointWriterDlqTest.java` (MODIFIED) — same substitution.
- `core/persistence/src/test/java/com/homesynapse/persistence/SqliteCheckpointStoreTest.java` (MODIFIED) — same substitution.
- `core/persistence/src/test/java/com/homesynapse/persistence/SqliteDeadLetterStoreContractTest.java` (MODIFIED) — same substitution.
- `core/persistence/src/test/java/com/homesynapse/persistence/SqliteEventStoreTest.java` (MODIFIED) — same substitution.
- `core/persistence/src/test/java/com/homesynapse/persistence/SqliteViewCheckpointStoreTest.java` (MODIFIED) — same substitution at both call sites (default `dbExecutor` plus the microsecond-precision `isolatedExecutor`).
- `testing/integration-tests/src/test/java/com/homesynapse/it/IntegrationTestHarness.java` (MODIFIED) — `DEFAULT_READ_THREAD_COUNT = 2` replaced with `DEFAULT_PERSISTENCE_CONFIG = PersistenceConfig.HOME_DEFAULT`. Both `PersistenceTestHarness.start[Throttled](...)` call sites updated.
- `core/persistence/MODULE_CONTEXT.md` (MODIFIED) — `DeploymentProfile` entry (3→6 fields), `DatabaseExecutor` entry (profile-driven PRAGMAs), `SqlitePersistenceLifecycle` entry (PersistenceConfig), `PersistenceTestHarness` entry (factory signatures), added `LockingMode` to package-private types table, added M3.6a Phase 3 Note entry, added profile-driven-PRAGMA gotcha, updated 4 stale references to the prior hardcoded PRAGMA list / `DatabaseExecutor(readThreadCount, clock)` signature.

**STOP Gate Results:**
- G1: DeploymentProfile enum values = 3 (STUDIO, HOME, PERFORMANCE) ✓, fields = 3 before (cacheSizeKiB, mmapSizeBytes, journalSizeLimitBytes) ✓
- G2: Hardcoded literal grep — `-128000`/`1073741824` confirmed in `DatabaseExecutor.java` + `DatabaseExecutorTest.java`; both replaced with profile-driven rendering and assertion ✓. Spike module references (`spike/wal-validation/PragmaConfig.java`, `D1WalStarvationTest.java`) intentionally left in place — spike code is out of scope per design doc §3.
- G3: `SqlitePersistenceLifecycle` 5-arg production constructor + 6-arg decorator overload, package-private ✓
- G4: `PersistenceConfig` 2 fields + `HOME_DEFAULT` constant ✓; record shape unchanged (`readThreadCount` lives on the profile per SD-5)
- Post-strip grep: `PersistenceLifecycle.java` returns ZERO matches for `WAL|PRAGMA|SQLite|sqlite` outside `@see` tags ✓

### Prior Last-Completed Milestone

M3.4b (adf04d2) — Sustained-Load + Crash-Recovery Integration Tests (2026-05-19). Build GREEN.

Files delivered (8 new + 4 modified):
- `core/persistence/src/testFixtures/java/com/homesynapse/persistence/ThrottledWriteCoordinator.java` (NEW) — disk test double, package-private final class wrapping any `WriteCoordinator`. Delay runs inside the write thread (10 ms baseline + 200 ms spike at 0.5% by default). `withDefaults(delegate)` factory + 4-arg explicit constructor.
- `core/persistence/src/test/java/com/homesynapse/persistence/ThrottledWriteCoordinatorTest.java` (NEW) — 9 unit tests (delegation, baseline delay, spike at p=1, no spike at p=0, exception propagation, shutdown forwarding, defaults factory, constructor validation × 3). Placed in `src/test/java` mirroring `InMemoryWriteCoordinatorTest`; brief allowed either source set.
- `core/persistence/src/testFixtures/java/com/homesynapse/persistence/PersistenceTestHarness.java` (MODIFIED) — added `startWithWriteCoordinator(...)` (Function-decorator factory), `startThrottled(...)` (Pi-4 defaults convenience), `abandonForCrashSimulation()` (no-op proxy for `close()`). The existing `start(...)` factory delegates to `startWithWriteCoordinator(..., Function.identity())`.
- `core/persistence/src/main/java/com/homesynapse/persistence/SqlitePersistenceLifecycle.java` (MODIFIED) — added package-private 6-arg constructor accepting a `Function<WriteCoordinator, WriteCoordinator>` decorator. Public 5-arg constructor delegates with `Function.identity()`.
- `core/persistence/src/main/java/com/homesynapse/persistence/DatabaseExecutor.java` (MODIFIED) — added package-private 3-arg constructor accepting the decorator. Field type of `writeCoordinator` widened from `PlatformThreadWriteCoordinator` to `WriteCoordinator` (interface) to accept the decorator's wrapper. The `shutdown()` method already routed through the `WriteCoordinator.shutdown()` interface method, so no change needed there. Production 2-arg constructor delegates with `Function.identity()`.
- `core/event-bus/src/testFixtures/java/com/homesynapse/event/bus/InProcessEventBusFactory.java` (MODIFIED) — added `createWithMetrics(..., BusMetrics, IntSupplier)` overload routing through the production 6-arg `InProcessEventBus` constructor. Existing `create(...)` delegates to `createWithMetrics(..., BusMetrics.noop(), () -> 0)`.
- `testing/integration-tests/src/test/java/com/homesynapse/it/IntegrationTestHarness.java` (MODIFIED) — added `startThrottled(Path, Clock, BusMetrics, IntSupplier)`, `startForCrashSimulation(Path, Clock)`, `abandon()` instance method. `start(Path, Clock)` and the three new factories all share a private `startInternal(...)` helper.
- `testing/integration-tests/src/test/java/com/homesynapse/it/Pi4SustainedLoadIT.java` (NEW) — sustained 100 ev/s test (10/60 min via `-PsustainedMinutes`). 50 rotating entities, BusMetricsRecorder-driven lag assertions, WAL/heap/checkpoint freshness checks. Event count assertion loosened from the brief's ±2% to lower-bound 25% — see Open risks.
- `testing/integration-tests/src/test/java/com/homesynapse/it/Pi4D1SpikeIT.java` (NEW) — 50 ev/s for 30 min with spike-induced lag transients; lag drain assertion within 5 s of final publish; WAL ceiling.
- `testing/integration-tests/src/test/java/com/homesynapse/it/CrashRecoveryIT.java` (NEW) — 5 000 events → wait for checkpoint ≥ 3 000 → abandon → restart → assert every globalPosition in [1, 5000] observed exactly once across both lifetimes; bus reaches LIVE; checkpoint at head; event store intact. Uses `@TempDir(cleanup = CleanupMode.NEVER)` because abandoned harness holds SQLite file handles on Windows.
- `scripts/pi4-validation.sh` (NEW) — on-device runner for hs-dev-1. Bash with `set -euo pipefail`. Rsync source → run gradle remotely → pull JUnit XML + HTML reports + JFR. Supports `--dry-run` for safe validation; SUSTAINED_MINUTES positional arg (default 60); standard help banner. `chmod +x` applied.

MODULE_CONTEXT.md updated: `core/persistence/MODULE_CONTEXT.md` (added M3.4b gotchas, extended testFixtures inventory, added M3.4b Phase 3 note) and `core/event-bus/MODULE_CONTEXT.md` (extended `InProcessEventBusFactory` entry with `createWithMetrics`).

---

## Next Work Unit

**M3.6d-b.** The actual composition-root wiring (`PersistenceFactory` + `HomeSynapseCore`) — what the original M3.6d brief described, minus the satellite changes already delivered in M3.6d-a. The brief must be revised to address the prerequisite gaps M3.6d-a discovered:

1. **`SqlitePersistenceLifecycle` must construct `SqliteStateStore` and `SqliteDeadLetterStore`** during `start()`. Today it constructs only `SqliteEventStore`, `SqliteCheckpointStore`, `SqliteViewCheckpointStore`, and `AtomicCheckpointWriter`. The new constructions require a separate `Include.ALWAYS`-configured `ObjectMapper` for `CheckpointSerializer` (the existing `PersistenceObjectMapper.create()` is `NON_NULL` and would drop nullable `staleAfter` and null attribute values — documented divergence gotcha).

2. **`WriteCoordinator` interface needs a `queueSize()` method** (or `PersistenceFactory` needs another way to expose the writer queue depth as an `IntSupplier` to `InProcessEventBus`'s 7-arg constructor). Today the interface has only `submit(WritePriority, Callable)` and `shutdown()`.

3. **A production `SubscriberReadConnectionFactory` implementation is needed.** Today only the testFixtures `RecordingReadConnectionFactory` exists. Production wiring needs per-subscriber dedicated platform-thread executors with their own SQLite read connections (the M3.4a harness Javadoc explicitly notes M3.6 production wiring would introduce this).

4. **`SqlitePersistenceLifecycle` accessors needed** for `stateStore()` (returning `StateStore`), `stateCheckpointSource()` (returning `StateCheckpointSource` — the M3.6d-a promotion means both can return the same underlying `SqliteStateStore`), `deadLetterStore()` (or a `PersistentDlqWriter` adapter).

5. **`PersistenceFactory` itself** is the bridge from the now-richer `SqlitePersistenceLifecycle` to consumers outside the persistence module — pure delegation through public-interface return types.

6. **`HomeSynapseCore`** + `HomeSynapseCoreTest` wires it all together using the M3.6d-a primitives (`HomeSynapseConfig`, `SharedScheduler`, `ThrowingStateQueryService`) plus the now-public `QueueSaturationHealthCheck` / `HealthSignal` / `HealthLevel` and the now-implementing `SqliteStateStore`.

Once Nick's compile gate resolves the M3.6a, M3.6b, M3.6c, and M3.6d-a deferrals, M3.6d-b can land on top. Awaiting PM coding instruction.

### Key context for the next coder session

1. **M3.6 design is committed.** Read `homesynapse-core-docs/design/2026-05-20_M3.6_Composition_Root_Design.md` — it specifies the five sub-WUs and their scope. M3.6a (§3) covers profile-driven persistence config (audit C-01, D1-05, D1-13, D2-11, D5-04). M3.6b (§4) covers `EventBusConfig` + DEC-M3-16 visibility promotion of `InProcessEventBus` (audit D1-07, D4-09).
2. **`EventBusConfig` is now the canonical bus-tuning seam.** The composition root (M3.6d) consumes it via the public 7-arg `InProcessEventBus` constructor; cross-module test code reaches it via `InProcessEventBusFactory.createWithConfig(...)`. `HOME_DEFAULT` reproduces the prior 10,000 / 5,000 behaviour exactly, so adopting it produces zero behaviour change. Per-deployment tuning is a future operational concern — `EventBusConfig` may eventually derive from `DeploymentProfile` like `PersistenceConfig` does.
3. **`InProcessEventBus` is now public (M3.6b, DEC-M3-16).** The composition root can construct it directly without going through the testFixtures factory. `QueueSaturationHealthCheck` remains package-private and is M3.6d scope (DEC-M3-16 part 3).
4. **`IntegrationTestHarness` has three factory methods (M3.4b).** `start(Path, Clock)` for standard, `startThrottled(Path, Clock, BusMetrics)` for disk simulation, `startForCrashSimulation(Path, Clock)` for crash tests. All three were untouched by M3.6b because `createWithMetrics(...)` delegates with `HOME_DEFAULT`. M3.6d may simplify this by routing through `HomeSynapseCore` facade.
5. **Decorator-function injection pattern is established.** `Function<WriteCoordinator, WriteCoordinator>` parameter on `DatabaseExecutor` and `SqlitePersistenceLifecycle` constructors. M3.6a may need to extend this pattern for PRAGMA parameterization.

### M3.6b Lessons (2026-05-20)

1. **Config-record promotion preserves backward compatibility cheapest.** Adding a new 7-arg constructor and delegating from the existing 4-arg/6-arg with a `*_DEFAULT` constant avoided every call-site change in `testing/integration-tests` and in-package tests. Pattern: introduce the canonical constructor as the most-explicit form; chain delegation `convenience → mid → canonical` so each step adds exactly one argument resolved from the default constant. This is the same pattern M3.4b used for `Function<WriteCoordinator, WriteCoordinator>` decoration on `DatabaseExecutor`.

2. **`-Xlint:exports` pre-promotion audit needs only the interface contract.** Before promoting a class to `public`, audit (a) every interface method override (since the interface is already public, all such methods use public types by definition) and (b) any class-only public methods. Package-private methods don't fall under `-Xlint:exports`. For `InProcessEventBus`, every public method came from `EventBus` — the audit was a one-pass grep with no surprises.

3. **Static constants on package-private classes are awkward when defaults move to a config.** When a static constant (`PUBLISHER_BLOCKED_DEPTH_THRESHOLD`) is referenced from tests that should match the production default, the constant either has to stay (and the config has to read from it) or the test has to derive from the config. The cleaner direction is "tests derive from the config" — fewer cross-class assumptions, and the constant can simply go away (as it did in M3.6b for the threshold; `MAX_CAPACITY` was kept only as a documentation reference for the no-arg constructor's default).

### M3.4b Lessons (2026-05-19)

1. **Decorator-function injection for package-private types.** `Function<WriteCoordinator, WriteCoordinator>` as a constructor parameter lets testFixtures wrap package-private production types without exposing them publicly. Pattern: production constructor defaults to `Function.identity()`; test constructor accepts the decorator. Applied to `DatabaseExecutor` and `SqlitePersistenceLifecycle`.

2. **testFixture factories are the bridge pattern for JPMS package-private types.** `PersistenceTestHarness.startThrottled()` encapsulates `ThrottledWriteCoordinator` construction internally, so cross-module test code never references the package-private type by name. Same pattern as M3.4a's `InProcessEventBusFactory`.

3. **@TempDir cleanup on Windows with abandoned resources.** Crash-simulation tests that deliberately leave file handles open (abandoned SQLite connections) must use `@TempDir(cleanup = CleanupMode.NEVER)`. `ON_SUCCESS` still attempts cleanup and throws IOException when handles are held.

4. **SLF4J transitivity under `implementation` scope.** When module A declares `implementation(libs.slf4j.api)`, consumers of module A's testFixtures do NOT get SLF4J on their compile classpath. Explicit `testImplementation(libs.slf4j.api)` required in the consuming module.

---

## Build Status

Working tree clean. HEAD at `25bc23b` on `main`. Last GREEN full-project `./gradlew check`: `25bc23b` (2026-05-20, post-SLF4J follow-up fix; 137 actionable tasks, 134 executed + 3 up-to-date). M3.6a (`17c40b6`), M3.6b (`df2743a`), M3.6c (`38d3e30`), and M3.6d-a (`25bc23b`) all committed and GREEN.

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

---

**Last verified against:** `homesynapse-core` commit `dfb045e` on `2026-05-21`.
