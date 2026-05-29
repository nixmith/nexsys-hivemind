# HomeSynapse Core — Codebase Investigation Report

**Date:** 2026-05-28
**Investigator:** Claude Cowork
**Purpose:** PM knowledge consolidation for strategic architecture deliberation (Rust substrate port, edge-AI M4–M6, neuromorphic/HE long-horizon bets)
**Method:** Direct source reading of `homesynapse-core`, `homesynapse-core-docs`, and `nexsys-hivemind`. Sections A, B, F authored from first-hand file reads; Sections C, D, E, G, H gathered by sub-investigations and spot-verified against source. No build commands run; no source files modified. Every load-bearing claim is cited to a repo-root-relative path with line numbers or symbol names.

---

## Investigation Summary

The five findings most consequential for the deliberation — including direct contradictions of the stated baseline:

- **"M4 = automation engine" is wrong per the repo's own planning.** `nexsys-hivemind/context/planning/phase-3-milestone-backlog.md:105-119` puts **M4 = State Store projection**, **M6 = Configuration**, and the **Automation Engine at M7 (core) + M8 (advanced)**. `PROJECT_SNAPSHOT.md` confirms the immediate next step is "M4.0 scoping" (State Store), not automation. The automation module (`core/automation`, 53 types) is **100% Phase-2 scaffolding with zero executable behavior and no `src/test` directory at all** — so "M4 automation engine is next" overstates both the milestone and the readiness by a wide margin. *This single correction reshapes the M4–M6 edge-AI timeline assumption.*

- **There is no crypto subsystem to port — it is greenfield.** `SecretStore` (`config/configuration`) is an **interface with zero implementations**; AES-256-GCM exists only in Javadoc. `chain_hash` is an unconditional 32-byte `ZERO_HASH` bind (`SqliteEventStore.java:116,353`). Crypto-shredding (INV-PD-07) is only the `event_category` column boundary — no shredding logic. Key management does not exist. For the Rust deliberation: the crypto subsystem is a design surface, not a port target.

- **The four "open architecture questions" are already resolved** (in `homesynapse-core-docs/research/2026-05-20_M3_Audit_Gap_Closure_v1.md`, not the 2026-05-19 audit): globalPosition is gap-tolerant by design, chain_hash is reserved-zero, event-type registration is implemented at the composition root, home_id is written-but-not-exposed (deferred to multi-hub). **But two of the prescribed doc updates were never made** (AMD-34 and AMD-37 annotations), and **AMD-37's body is stale relative to shipped code** — a governance-trail inconsistency the PM should not mistake for an open technical question.

- **Several baseline counts are low.** There are **10 abstract contract suites, not 3** (the largest is `EventBusContractTest` = 47 `@Test`); **9 ArchUnit rules, not 7**; **~1,396 `@Test` methods** total. The bounded-window numbers are conflated in the baseline: the **replay read page is 500 rows** (`ReplayDriver.MAX_REPLAY_PAGE`), while **200 events / 2 s is the *checkpoint cadence*** (`CHECKPOINT_EVENT_THRESHOLD` / `CHECKPOINT_MAX_INTERVAL_SECONDS`), not the read window.

- **Two "it's specified" items are actually dead or unwired in production.** (1) The subscriber supervisor's **exponential-backoff retry loop is dead code** — `computeBackoff`/`sleepForBackoff`/`MAX_RETRIES` are never invoked; every callback failure parks once with `attemptCount=1` (`SubscriberSupervisor.java:84-87`). (2) `AtomicCheckpointWriter` (the AMD-45 mechanism) is fully built and tested but **not wired** — the live loop still calls the single-table `checkpointStore.writeCheckpoint(...)` (`InProcessEventBus.java:500`), and the bus constructs its DLQ with `PersistentDlqWriter.noop()` (`InProcessEventBus.java:338`), so persistent DLQ is off by default. Also note `SelfProducedFilter` lives in `core/state-store` (AMD-41), **not** the event-bus, contrary to the brief's framing.

A secondary correction worth flagging up front: `EventEnvelope.actorRef` is an **untyped `Ulid`**, not a `PersonId` (`PersonId` exists but is used only for `SubjectRef.person(...)` and JSON serde) — person attribution today is by convention, not by type.

---

## Section A: Components Most Likely to be Ported to Rust

### A1. PlatformThreadWriteCoordinator (`core/persistence`)

File: `core/persistence/src/main/java/com/homesynapse/persistence/PlatformThreadWriteCoordinator.java` — **267 lines**, `final class ... implements WriteCoordinator`, package-private (wired into `DatabaseExecutor` at startup; never referenced by module consumers).

**Public + package-private API surface.** It implements the three-method `WriteCoordinator` interface (`WriteCoordinator.java`):

- `<T> T submit(WritePriority priority, Callable<T> operation)` (`:69-98`) — enqueues a `WorkItem` and blocks the caller on `CompletableFuture.get()` until the write thread completes it. NPE on null args; `IllegalStateException` if shut down; checked exceptions are unwrapped (`SequenceConflictException` surfaces via `unwrap`, `:199-211`).
- `int queueSize()` (`:100-103`) — returns `queue.size()`. Contract (per `WriteCoordinator.java:70-83`): used by `QueueSaturationHealthCheck` (AMD-43 §3.6.3, DEC-M3-14); the composition root surfaces it as an `IntSupplier` so the event-bus never references persistence types; "Returns 0 when idle or shut down," always `>= 0`. (The Javadoc attributes it to AMD-43/DEC-M3-14; the brief's "added in M3.6d-b" is consistent but not stated in-file.)
- `void shutdown()` (`:105-136`) — idempotent (guarded by `lifecycleLock`); sets the `volatile boolean shutdown` flag, enqueues a poison-pill `WorkItem` (rank `Integer.MAX_VALUE`), joins the writer thread for `SHUTDOWN_JOIN_TIMEOUT_MS = 5_000`ms, and interrupts if still alive.
- Package-private test accessor `boolean awaitTermination(long, TimeUnit)` (`:263-266`).

**Threading model.** A **single daemon platform thread** named `hs-write-0`, created and started in the constructor (`Thread.ofPlatform().name("hs-write-0").daemon(true).unstarted(this::runLoop)`, `:60-66`). Not a pool. This is the AMD-26 mitigation: all sqlite-jdbc JNI calls execute on this one thread so virtual-thread callers never pin a carrier.

**Work queuing & priority ordering.** Work is a `PriorityBlockingQueue<WorkItem>` (`:53`). `WorkItem implements Comparable` (`:224-253`): orders by `rank` ascending, with an `AtomicLong sequence` (`:54`) as a **FIFO tiebreaker within the same priority**. So ordering is **priority-on-dequeue, FIFO within a priority — not preemptive**: an in-flight operation is never interrupted; priority only decides which queued item runs next. The `runLoop` (`:142-166`) does a blocking `queue.take()`, returns on poison, else `operation.call()` and completes the future (or `completeExceptionally`). `drainAndCancel` (`:168-179`) fails remaining futures with `IllegalStateException` on shutdown.

**Bus-notification interaction.** None directly. The coordinator is purely a write serializer; bus notification (`notifyEvent`) is orchestrated above it by the publish path (see B1) after the WAL commit returns. The coordinator has no reference to the event bus.

**Complexity:** ~267 lines, two of the codebase's three `@SuppressWarnings("unchecked")` (generic erasure in `completeUnchecked`/`WorkItem`). A clean, self-contained candidate; the port's subtlety is the `Callable`/`CompletableFuture` blocking-handoff and exception-unwrap contract, not the data structures.

### A2. SqliteEventStore (`core/persistence`)

File: `core/persistence/src/main/java/com/homesynapse/persistence/SqliteEventStore.java` — **827 lines**, `final class SqliteEventStore implements EventPublisher, EventStore`, package-private (consumed via the `PersistenceLifecycle` facade as the public interfaces only). It is the sole write path (LTD-03) and primary read path.

**Connection topology.** Two executors owned by `DatabaseExecutor` (`:56-73`):

- **Write:** one platform thread (`hs-write-0`) via the `WriteCoordinator`; every `publish`/`publishRoot` routes through `dbExecutor.writeCoordinator().submit(EVENT_PUBLISH, ...)` and uses the single `dbExecutor.writeConnection()`. Single-writer ⇒ no `UNIQUE(subject_ref, subject_sequence)` race.
- **Read:** a bounded pool of platform threads (`hs-read-*`) via `ReadExecutor`. Each read thread is assigned **one** `Connection` on first use from `dbExecutor.readConnections()` via a round-robin `AtomicInteger readConnectionCursor` and holds it in a `ThreadLocal<Connection>` for the store's lifetime (`executeRead`, `:749-766`). Pool size matches the read-connection-list size, so each thread gets a unique connection. This is the AMD-26/27 JNI-pinning mitigation; VT callers park while a platform thread does the JDBC.

**The 24-bind INSERT (`INSERT_SQL`, `:129-138`; binds `:313-353`).** `global_position` is omitted (SQLite `AUTOINCREMENT`; retrieved via `Statement.getGeneratedKeys()`, `:364-371`). Bind order (load-bearing serialization path):

| # | Column | Source |
|---|--------|--------|
| 1 | event_id | `eventId.value().toBytes()` |
| 2 | home_id | `homeId.value().toBytes()` (AMD-34) |
| 3 | event_type | `draft.eventType()` |
| 4 | schema_version | `draft.schemaVersion()` |
| 5 | ingest_time | `TimeConversion.toMicros(ingestTime)` |
| 6 | event_time | micros, or `setNull(INTEGER)` |
| 7 | subject_ref | `subject.id().toBytes()` |
| 8 | subject_type | `subject.type().name()` |
| 9 | subject_sequence | `nextSequence` |
| 10 | priority | `draft.priority().name()` |
| 11 | origin | `draft.origin().name()` |
| 12 | actor_ref | bytes, or `setNull(BLOB)` |
| 13 | idempotency_key | string, or `setNull(VARCHAR)` (AMD-35) |
| 14 | correlation_id | `causalContext.correlationId().toBytes()` |
| 15 | causation_id | bytes, or `setNull(BLOB)` |
| 16 | event_category | `encodeCategories(...)` — comma-joined wire values |
| 17 | payload_size | `payloadBytes.length` (Tier 2) |
| 18 | batch_id | `setNull(BLOB)` (reserved) |
| 19 | external_ref | `setNull(VARCHAR)` (reserved) |
| 20 | intent_kind | `"UNSPECIFIED"` (reserved) |
| 21 | logical_time | `0L` (reserved) |
| 22 | node_id | `0` (reserved) |
| 23 | payload | `payloadBytes` |
| 24 | chain_hash | `ZERO_HASH` (32 zero bytes, AMD-37) |

24 binds + `global_position` (autoincrement) = the 25-column V001 schema (`src/main/resources/db/migration/events/V001__initial_event_store_schema.sql`). `subject_sequence` is computed by `nextSubjectSequence` (`:392-407`): `SELECT MAX(subject_sequence) WHERE subject_ref=?`, then `+1` (or `1`). Safe under the single writer.

**Reads.** Six `EventStore` methods: `readFrom`, `readBySubject`, `readByCorrelation`, `readByType`, `readByTimeRange`, `latestPosition` (`:429-571`). **No prepared-statement caching** — each call constructs its `PreparedStatement` in a try-with-resources from one of the static SQL constants (`SELECT_COLS` projects 16 columns in canonical envelope order, `:148-153`). Pagination is `... ORDER BY <key> ASC LIMIT ?`; `hasMore` is computed by a **separate `SELECT 1 ... LIMIT 1` probe** when the page fills (`:578-634`); `nextPos` = last row's position/sequence. `readByCorrelation` has **no `LIMIT`** (unbounded result). Row→envelope mapping is `fromRow` (`:654-703`), which calls `codec.decode(...)` (DegradedEvent fallback, see B4).

**chain_hash.** Not computed — `ps.setBytes(24, ZERO_HASH)` unconditionally (`:116`, `:353`); Javadoc: "Actual hash computation is deferred to the crypto milestone" (`:90-93`).

**HomeId injection.** `homeId` is a constructor field (`:189`, `:239`), bound at position 2 of every INSERT (AMD-34). It is supplied by the composition root. Note: `home_id` is **written but never read back** — `SELECT_COLS` does not project it and `fromRow` never reads it (corroborates H1(d): home_id is not exposed on `EventEnvelope`).

**Error handling / retry.** A `UNIQUE` violation on insert is translated to `SequenceConflictException` via `isUniqueConstraintViolation` (checks SQLSTATE `23xxx` or message substring, `:416-423`); the `WriteCoordinator` wraps it and `appendOnWriteThread` (`:272-289`) unwraps it back to the declared `throws`. Other `SQLException`/`IOException` propagate. **No retry** — single insert attempt. The decode path never throws (DegradedEvent fallback). Constructor accepts an `EventTypeRegistry` that is "currently unused at the store level" (`:210-214`).

### A3. InProcessEventBus (`core/event-bus`)

File: `core/event-bus/src/main/java/com/homesynapse/event/bus/InProcessEventBus.java` — **582 lines**, `public final class InProcessEventBus implements EventBus`.

**Public + package-private API.** Three constructors (4-arg test, 6-arg, and the canonical **7-arg** taking `EventBusConfig`, `:141-159`). `EventBus` interface methods: `subscribe(SubscriberInfo)`, `unsubscribe(String)`, `notifyEvent(long)`, `subscriberPosition(String)`, `subscribeRuntime(SubscriberInfo, Subscriber)`, `resume(String)`, `subscriberInfo(String)→SubscriberSnapshot`, `subscribers()→List<SubscriberSnapshot>`. Additional `public void abandon()` (`:217-232`, crash-sim / emergency shutdown). Package-private `subscribeWithHandler(SubscriberInfo, Consumer<Long>)` and `reset()`. Two registries (`ConcurrentHashMap`): `passiveRegistry` (callback bridge) and `activeRegistry` (full runtime). The registry is guarded by a `ReentrantReadWriteLock` (LTD-11, no `synchronized`): fan-out takes the read lock, mutations the write lock (`:62`).

**Notification = position, not data (pull model).** `notifyEvent(long globalPosition)` (`:235-321`) samples the writer-queue depth (record-only, INV-BUS-02), then **loads the event once** via `eventStore.readFrom(globalPosition-1, 1)` to evaluate subscription filters at fan-out. For passive subscribers it invokes the callback with the position; for active subscribers it routes the **position** by mode (under the per-subscriber queue lock): COLD/SUSPENDED → drop; REPLAY/TRANSITION → `replayWindowQueue.enqueue(position)`; LIVE → `runtime.pendingPositions().offer(position)` then `LockSupport.unpark(vt)`. The subscriber's VT then **re-reads** the full envelope from the store via its own dedicated read executor (`liveLoop`, `:460-515`). So the cross-thread handoff carries a `long` position; the bus's one-time read is only for filter matching.

**Per-subscriber virtual thread (INV-SUB-ISO-01).** `subscribeRuntime` (`:331-366`) builds a `SubscriberRuntime` bundle (read executor, `SubscriberSupervisor`, `SubscriberDlq` constructed with `PersistentDlqWriter.noop()`, `ReplayWindowQueue` sized from `config.replayQueueCapacity()`), then spawns `Thread.ofVirtual().name("hs-sub-"+id).start(() -> subscriberLoop(runtime))` and stores the handle. `subscriberLoop` (`:435-448`) runs the three phases: `ReplayDriver.run()` → `TransitionCoordinator.drainAndPromote()` → `liveLoop`. Shutdown: `unsubscribe`/`abandon`/`reset` call `runtime.close()` (`SubscriberRuntime.java:255-266`) which interrupts the VT, closes the read executor, and clears the DLQ + replay queue.

**State machine.** The `AtomicReference<SubscriberMode>` is held **per-subscriber in `SubscriberRuntime`** (`SubscriberRuntime.java:33,97`, initialized `COLD`), exposed via `mode()`, `transitionTo()`, `compareAndTransition()`. `SubscriberMode` (`SubscriberMode.java`): `COLD, REPLAY, TRANSITION, LIVE, SUSPENDED`. Transitions: `ReplayDriver` CAS `COLD→REPLAY` then on tail-reach CAS `REPLAY→TRANSITION` (`ReplayDriver.java:113,159-165`); `TransitionCoordinator` CAS `TRANSITION→LIVE` once the replay queue drains, under the queue lock to close the race with `notifyEvent` (`TransitionCoordinator.java:131-143`); any infra failure/circuit-trip → `SUSPENDED`; `resume()` does `SUSPENDED→REPLAY` (`:369-388`).

**ReplayWindowQueue** (`ReplayWindowQueue.java`, 197 lines). Bounded `ArrayDeque<Long>` under a `ReentrantLock`; capacity is a **constructor parameter** from `EventBusConfig` (default constant `MAX_CAPACITY = 10_000`, `:57`). `enqueue` returns `false` and latches an `AtomicBoolean overflowed` when full (`:100-112`); `ReplayDriver` observes the flag and **restarts REPLAY from the persisted checkpoint** — overflow is recoverable, not data loss (`ReplayDriver.java:126-134`). It exposes `lock()`/`unlock()` so callers can fuse mode-read+enqueue and empty-check+CAS. Lifetime is per-subscriber (REPLAY entry → drain); it is **cleared, not GC'd, at transition**, and GC'd only when the `SubscriberRuntime` is dropped on close.

**SelfProducedFilter — note: lives in `core/state-store`, not event-bus.** File `core/state-store/src/main/java/com/homesynapse/state/SelfProducedFilter.java` (156 lines), a `StateProjection` concern (AMD-41 §3.2.2, INV-SUB-ISO-06), not a bus component. `DEFAULT_TTL = Duration.ofSeconds(60)` (`:68`). It is a thread-confined `HashMap<Ulid, Instant>` (no synchronization — single VT). `record(eventId)` stamps `clock.instant()`; `isSelfProduced(eventId, mode)` returns `false` unconditionally during REPLAY/TRANSITION, otherwise runs **lazy O(N) eviction** (`evictExpired`, sweep against `now − ttl`, `:146-155`) then `containsKey`. Bounded by publish-rate × TTL (≈200/s × 60s = 12,000 entries).

**DLQ integration.** `SubscriberDlq` (`SubscriberDlq.java`, 209 lines) is a per-subscriber in-memory ring, `CAPACITY = 1024`, oldest evicted when full; **not thread-safe** (VT-confined). Two `park` overloads: `park(DlqEntry)` (caller-built, used by `TransitionCoordinator` for the synthetic `onCaughtUp` marker; ring only) and `park(DeadLetter)` (full identity; ring **and** flush to `PersistentDlqWriter`). "Who decides poison": the `SubscriberSupervisor.deliver(...)` (`SubscriberSupervisor.java:97-151`) — **any `RuntimeException` from `subscriber.onEvent()` parks a `DeadLetter`** (with `attemptCount=1`) and records a crash; `Error`/checked `Exception` (infrastructure) bypass the DLQ and go straight to `SUSPENDED`. Because the bus constructs the DLQ with `PersistentDlqWriter.noop()` (`InProcessEventBus.java:338`), **persistent DLQ is not active via the bus's own runtime** — the in-memory ring is the only path unless the composition root wires a real writer.

**Material reality in the supervisor:** the exponential-backoff retry path (`computeBackoff`, `sleepForBackoff`, `MAX_RETRIES=5`, MIN=3s/MAX=30s/jitter=0.2) is **dead code** — explicitly documented as "reserved for a future WU" (`SubscriberSupervisor.java:84-87`). The circuit breaker (5 crashes / 10-min rolling window → SUSPENDED) **is** live.

### A4. Crypto subsystem

**There is no unified crypto module, and effectively no crypto implementation at all.** Findings:

- **AES-256-GCM secrets store (INV-PD-03): interface only, zero implementations.** The only secrets types are `config/configuration/src/main/java/com/homesynapse/config/SecretStore.java` (a 4-method `public interface`: `resolve`, `set`, `remove`, `list`) and `SecretEntry.java` (a 4-field record holding the **plaintext** value). A repo-wide search for `implements SecretStore` returns nothing, and the only occurrences of `AES`/`GCM`/`javax.crypto`/`Cipher`/`SecretKeySpec`/`KeyStore` in `src/main` are the **Javadoc strings** in `SecretStore.java:15` and `SecretEntry.java:15`. No actual encryption code exists.
- **Hash chain (chain_hash, AMD-37): all ZERO_HASH placeholders.** Computation is not implemented anywhere; `SqliteEventStore` binds 32 zero bytes (A2). The only other `chain_hash` references are in the throwaway WAL spike.
- **Key management: does not exist.** No key store, no rotation, no key-derivation code. (`AreaId`/`HomeId`/etc. are ULID identity wrappers, not cryptographic keys.)
- **Crypto-shredding (INV-PD-07): column-level boundary concept only.** Referenced solely in Javadoc on `EventCategory.java:11`, `EventEnvelope.java:74`, `EventCategoryMapping.java:37-38`, and `PersonId.java:19-20` — the `event_category` (esp. `presence`) is documented as the crypto-shred boundary, but no shredding logic is implemented.

For the Rust deliberation: crypto is a **design surface, not an existing implementation** — nothing to port; everything to specify.

### A5. ULID generation hot path (`platform-api`)

File: `platform/platform-api/src/main/java/com/homesynapse/platform/identity/UlidFactory.java` — **118 lines**, `public final class` utility (private constructor).

- `generate()` → `generate(Clock.systemUTC())`; `generate(Clock)` (`:79-117`) supports deterministic testing.
- **Thread safety / contention.** A **single static `ReentrantLock LOCK`** (`:32`) guards a small critical section; `SecureRandom RANDOM` (`:33`) and the monotonic state (`lastTimestamp`/`lastMsb`/`lastLsb`, static) are JVM-process-global. `ReentrantLock` (not `synchronized`) is the deliberate LTD-11 choice to avoid VT carrier pinning. Under load every `generate()` call serializes on this one lock, but the critical section is pure arithmetic (no I/O), so contention is brief; the global lock is nonetheless a single point of serialization for *all* ID generation across the process. Within a millisecond, successive calls increment the 80-bit random component (carry from `lsb` into the low 16 bits of `msb`), throwing `IllegalStateException` only on >2⁸⁰ generations in one ms; on clock-backwards it reuses `lastTimestamp` (`:85-107`).
- **Performance target measured? No benchmark found.** There is no JMH harness or perf assertion for `UlidFactory` anywhere in the repo (the hivemind `benchmarks/` directory is the agent-eval grading harness, unrelated). The only adjacent perf artifacts are in the throwaway `spike/wal-validation` module (`SpikeUlidGenerator.java`, `LatencyStats.java`, `Pi4D1SpikeIT.java`), which validate WAL write latency with a *separate* spike ULID generator — not `UlidFactory`, and not a sub-microsecond ID-generation benchmark. So the sub-microsecond target is stated as a goal but **not measured** in code.

---

## Section B: End-to-End Event Flow Reality

### B1. Publish path

1. **Caller → `EventPublisher`.** An adapter/subscriber calls `EventPublisher.publish(EventDraft, CausalContext)` (derived) or `publishRoot(EventDraft)` (root). The two-method API enforces causality at compile time (`EventPublisher.java:57-128`). `EventDraft` (`EventDraft.java`, a 9-field record) carries the caller-owned fields (`eventType`, `schemaVersion`, `eventTime`, `subjectRef`, `priority`, `origin`, `payload`, `actorRef`, `idempotencyKey`) and validates them in its compact constructor (blank eventType, `schemaVersion>=1`, idempotency key ≤128 chars).
2. **ULID assignment + causal context.** In `SqliteEventStore` (the production `EventPublisher`), `publish` generates `EventId.of(UlidFactory.generate(clock))` and passes the caller's `CausalContext`; `publishRoot` generates the ULID, builds `CausalContext.root(ulid)` (self-correlation), and uses it (`SqliteEventStore.java:246-265`).
3. **Submit to the write coordinator.** `appendOnWriteThread` wraps `doAppend` in a `Callable` and calls `dbExecutor.writeCoordinator().submit(WritePriority.EVENT_PUBLISH, op)` (`:272-289`) — so the actual insert runs on `hs-write-0`.
4. **Serialize + persist.** On the write thread, `doAppend` (`:298-390`) computes `nextSubjectSequence`, sets `ingestTime = clock.instant()`, derives categories via `EventCategoryMapping.categoriesFor(eventType)`, encodes the payload via `codec.encode(payload)` (Jackson → UTF-8 JSON bytes), binds the 24 columns (A2), `executeUpdate()`, retrieves `global_position` from `getGeneratedKeys()`, and returns a fully-populated 14-field `EventEnvelope`. The WAL commit happens before `publish` returns (INV-ES-04), so the event is immediately readable.
5. **Bus notification.** Subscriber notification is **not** invoked inside `SqliteEventStore` — `publish` returns the envelope and the orchestrating layer calls `EventBus.notifyEvent(globalPosition)` afterward (the bus's Javadoc and `notifyEvent`'s "EventPublisher orchestrates the full publish path above this layer" note, `InProcessEventBus.java:315-318`, confirm the persist/notify split). *Caveat:* the explicit production wiring that calls `notifyEvent` after each `publish` is a composition-root concern; within the modules read here the two are deliberately decoupled (the bus holds an `EventStore`, not an `EventPublisher`).
6. **Subscriber wakeup → pull.** `notifyEvent` routes the position to LIVE subscribers' `pendingPositions` and `LockSupport.unpark`s their VT; `liveLoop` polls the position, re-reads the envelope via the dedicated `SubscriberReadExecutor`, applies the filter, and delivers through the supervisor (A3, B2).

### B2. Subscriber pull / resume-from-checkpoint path

- **Checkpoint position.** `ReplayDriver.run()` reads the persisted position via `checkpointStore.readCheckpoint(subscriberId)` (`ReplayDriver.java:109`) and sets it as both the paging cursor and `lastReplayedPosition`.
- **Read query + pagination.** It pages with `eventStore.readFrom(currentPosition, MAX_REPLAY_PAGE)` where **`MAX_REPLAY_PAGE = 500`** (`ReplayDriver.java:62,141`) — i.e., the `SELECT ... WHERE global_position > ? ORDER BY global_position ASC LIMIT 500` from A2, run on the subscriber's dedicated read thread (AMD-26/27). The "≤2 s" in the brief is the **checkpoint cadence**, not the page: `CHECKPOINT_EVENT_THRESHOLD = 200` events **or** `CHECKPOINT_MAX_INTERVAL_SECONDS = 2` (`:65-68`, `shouldCheckpoint` `:195-201`).
- **Checkpoint advance.** During REPLAY, `checkpointStore.writeCheckpoint(subscriberId, currentPosition)` fires on the 200/2 s cadence and once more at tail (`:155-158, 184-189`). In LIVE, `liveLoop` writes a per-event checkpoint **after each successful delivery**: `checkpointStore.writeCheckpoint(subscriberId, envelope.globalPosition())` (`InProcessEventBus.java:500`).
- **AtomicCheckpointWriter coupling (AMD-45).** `AtomicCheckpointWriter` (`core/persistence/.../AtomicCheckpointWriter.java`, 285 lines) writes `subscriber_checkpoints.last_position` **and** `view_checkpoints.position` (same value) in **one** SQLite transaction on the write thread at `WritePriority.STATE_PROJECTION` (`writeAtomicCheckpoint`, `:128-184`; a three-way variant also parks a DLQ row, `:213-284`), with `setAutoCommit(false)` → commit/rollback → autoCommit restored in `finally`. **Reality:** this class is fully implemented and tested but **not on the production live-delivery path** — the bus's `liveLoop` still calls the single-table `checkpointStore.writeCheckpoint(...)`. Wiring it in is exactly AMD-45's M4.0 work (see H3).

### B3. Causal context propagation

The mechanism lives in `core/event-model`: `CausalContext(correlationId, causationId)` (both raw `Ulid`; `CausalContext.java`), with `root(id)` (causation null, self-correlation) and `chain(correlationId, causationId)` (`:74-97`). For a derived event, the producer builds `CausalContext.chain(causingEvent.causalContext().correlationId(), causingEvent.eventId().value())` and passes it to `publish(draft, cause)`; the publisher stores it verbatim (`SqliteEventStore.doAppend` binds correlation/causation at positions 14/15) and `fromRow` reconstructs it on read (`:675-680`). **`actorRef` is carried separately** on `EventDraft`/`EventEnvelope` (an untyped `Ulid`), not on `CausalContext`; the caller inherits it from the causing event and the publisher copies it through (`EventPublisher.java:73-79`).

**Where this actually happens:** the **only** production caller of `publish(draft, cause)` / `CausalContext.chain(...)` is `StateProjection` (`core/state-store/.../StateProjection.java:400-404, 512-516`). So causal propagation is real **only for the state-projection's derived `state_changed` events**. The "integration receives a command and emits a result event" path the question describes is **not wired** — `CommandDispatchService` and `IntegrationSupervisor` are interface-only (see D4), so no production code carries `correlation_id`/`causation_id`/`actorRef` from a command envelope to a result event yet. The plumbing exists; the integration-side caller does not.

### B4. Serialization boundaries

- **Java `DomainEvent` → SQLite BLOB.** `EventPayloadCodec.encode(DomainEvent)` (`EventPayloadCodec.java:104-116`) serializes **only the inner payload** (the envelope metadata goes to discrete columns) to UTF-8 JSON via a pre-warmed Jackson `ObjectWriter` (`JacksonWarmup`). The `ObjectMapper` is built by `PersistenceObjectMapper`, which installs `PersistenceJacksonModule` — registering serde for **10 ULID-based types** (`Ulid` + `EntityId, DeviceId, AreaId, AutomationId, PersonId, HomeId, IntegrationId, SystemId, EventId`) so they round-trip as bare 26-char Crockford Base32 strings (`PersistenceJacksonModule.java:55-102`). Encoding an unregistered class (including `DegradedEvent`) throws `IllegalArgumentException`.
- **SQLite BLOB → Java `DomainEvent` (DegradedEvent fallback).** `EventPayloadCodec.decode(eventType, schemaVersion, payload)` (`:135-170`): **Stage 1** — if `eventType` is not in the `EventTypeRegistry`, return a `DegradedEvent` with reason `"Unknown event type: ..."`. **Stage 2** — if the class is found but Jackson throws (malformed JSON, missing required field, compact-constructor validation failure), catch `IOException|RuntimeException` and return a `DegradedEvent`. Metadata is sanitized first (`schemaVersion` clamped to ≥1, blank/null `eventType` → `"unknown"`) so the fallback itself never throws (LTD-19 / DECIDE-M2-06/07). `SqliteEventStore.decodeCategories` similarly falls back to `SYSTEM` on a corrupt `event_category`.
- **Java `EventEnvelope` → REST JSON response.** **No production code for this boundary was found.** `api/rest-api/src/main` has **no `new ObjectMapper`/`JsonMapper.builder` construction, no dedicated REST Jackson module, and no `EventEnvelope`-referencing serializer/DTO.** REST responses are built from response records (`ApiResponse`, `CommandAcceptedResponse`, entity/state DTOs); the existing read endpoints (`GetEntityEndpoint`, `ListEntitiesEndpoint`, `ProjectionStatusEndpoint`, `DlqStatusEndpoint`) return query-view shapes via `StateQueryService`, not raw envelopes. The "different-from-persistence REST serializer config" the brief anticipates does **not exist yet** — it is a Phase-3 gap, consistent with D4's finding that the command surface is unimplemented.
- **REST JSON request → Java command object.** The request type `CommandRequest` (record) exists (`api/rest-api/.../CommandRequest.java`), but there is **no handler that deserializes it into a dispatched command** (D4). So this boundary is also specified-not-built.

---

## Section F: Cross-Cutting State

### F1. Total code volume

- **Production Java files (`src/main`, excl. spike):** 506 (`find ... -path "*/src/main/*"`).
- **Test Java files (`src/test`):** 173. **`src/testFixtures`:** 41.
- **Production LOC (`src/main`, excl. spike):** **38,829** lines (`wc -l` over all production `.java`).
- `@Test` methods total: **~1,396** (anchored count; see E1).

### F2. Per-module public type counts (`src/main`)

Counts of top-level `public` type declarations (`class`/`interface`/`enum`/`record`):

| Module | Public types | | Module | Public types |
|---|---|---|---|---|
| core/device-model | 57 | | api/rest-api | 28 |
| core/automation | 53 | | api/websocket-api | 25 |
| core/event-model | 46 | | config/configuration | 22 |
| integration/integration-zigbee | 38 | | integration/integration-api | 22 |
| core/state-store | 20 | | core/event-bus | 19 |
| observability/observability | 18 | | core/persistence | 17 |
| platform/platform-api | 12 | | testing/test-support | 10 |
| lifecycle/lifecycle | 8 | | integration/integration-runtime | 4 |
| app/homesynapse-app | 2 | | web-ui/dashboard | 0 |

Largest: **device-model (57)**, **automation (53)**, **event-model (46)**, **zigbee (38)**. Note that `core/persistence` exposes only **17 public types** despite being the most behaviorally dense module — it deliberately hides implementation behind a small facade surface (most classes are package-private, as seen throughout Section A). Smallest non-empty: integration-runtime (4), app (2). web-ui/dashboard has **no Java** (0 production files).

### F3. JPMS state

- **17** of the production modules carry `module-info.java`. **Two modules with `src/main/java` lack one:** `platform/platform-systemd` (1 source file) and `testing/test-support` (intentionally classpath-distributed — its fixtures live in `src/main` and are consumed as a normal dependency, and the ArchUnit harness similarly runs on the classpath to avoid a JPMS automatic-module + `-Werror` clash). `web-ui/dashboard` has no Java at all.
- **`requires` patterns:** **35 `requires transitive`** vs **33 plain (non-transitive)** `requires`, and **0 `requires static`**. So while LD#10's default leans transitive, roughly half of all `requires` are deliberately non-transitive — the codebase actively curates its re-export surface rather than blanket-transitive. (No `requires static`/optional-dependency usage anywhere.)

### F4. Pi 5 (`hs-dev-1`) hardware execution

**Yes — HomeSynapse code has run on the Pi 5 dev board.** `nexsys-hivemind/context/handoff/pm-handoff.md:40` records milestone **M3.4b** ("Pi4SustainedLoadIT, Pi4D1SpikeIT, CrashRecoveryIT, ThrottledWriteCoordinator, pi4-validation.sh") as **DONE 2026-05-19** (commit `adf04d2`), and `:76` states the validation hardware is "**dev Pi 5 (`hs-dev-1`) per established M3.4b validation pattern.**" So the **SQLite WAL-validation spike (the D1 starvation / sustained-load ITs) has been executed on real Pi hardware**, and a `pi4-validation.sh` script exists for it. Naming nuance to avoid confusion: the test classes are named `Pi4...` because **Pi 4 is the performance-target/baseline tier**, whereas the physical dev board is a **Pi 5** (`hs-dev-1`); `coder/references/homesynapse-mental-model.md:122` reasons about carrier-thread exhaustion "on Pi 5" specifically. Day-to-day development/build is on Nick's Windows machine, and **CI is `ubuntu-latest` (no Pi in CI)** — hardware validation is a manual, milestone-gated step on `hs-dev-1`.

### F5. Formatting / lint debt

Essentially none. `build-logic/src/main/kotlin/homesynapse.java-conventions.gradle.kts:29` sets `options.compilerArgs.addAll(listOf("-Xlint:all", "-Werror"))` for all modules. Across **all** production source there are only **3 `@SuppressWarnings`**: two `("unchecked")` for unavoidable generic erasure in `PlatformThreadWriteCoordinator.java:188,231` and one `("deprecation")` in `JacksonWarmup.java:106`. No suppression clusters, no `-Xlint` opt-outs — the `-Werror` posture is genuinely clean, not papered over.

---

## Section C: Automation Engine Current State

**Milestone-vocabulary correction (important for the PM):** The brief labels the next milestone "M4 (automation engine)." The repository's planning documents do **not** support that mapping. Per `nexsys-hivemind/context/planning/phase-3-milestone-backlog.md:108-112`, **M4 = State Store**, **M6 = Configuration**, and the **Automation Engine is M7 (core) + M8 (advanced)**. `nexsys-hivemind/context/status/PROJECT_SNAPSHOT.md:13,25` confirms the immediate next step is "M4.0 scoping" (State Store). The automation track is "Research 4," milestoned to **M7** (`2026-05-22_Research_4_PM_Assessment.md:29-41`). Everything below describes `core/automation`'s current on-disk state.

**Headline:** `core/automation` is a **pure Phase-2 contract module — 100% interface/record/enum scaffolding, zero executable behavior.** No `src/test` tree, no `*Impl` class, no method body anywhere except `RunId.compareTo`/`toString`.

### C1. Production types in `core/automation/src/main/java`

All types live in the single flat package `com.homesynapse.automation` (`MODULE_CONTEXT.md:55`; no subdirectories). **53 types + `module-info.java` + `package-info.java` = 55 files**. By role:

- **(a) Sealed hierarchy roots — 4 (interface only, empty bodies):** `Selector`, `TriggerDefinition`, `ConditionDefinition`, `ActionDefinition` (see C2).
- **(b) Sealed permit records — 27** (real = fields + validating compact constructor; reserved = 0-field placeholder). Selector(6 real), Trigger(5 real + 4 reserved), Condition(6 real + 1 reserved), Action(5 real + 3 reserved).
- **(c) Service interfaces — 9 (interface only, NO default methods, NO impls):** `AutomationRegistry`, `TriggerEvaluator`, `ConditionEvaluator`, `ActionExecutor`, `RunManager`, `CommandDispatchService`, `PendingCommandLedger`, `SelectorResolver`, `ConflictDetector` (signatures in C3).
- **(d) Supporting data records — 4 (real records, validation only):** `AutomationDefinition` (12 fields, `:L56-89`), `RunContext` (8 fields, `:L55-81`), `PendingCommand` (8 fields, `:L52-78`), `DurationTimer` (8 fields incl. a `java.lang.Thread`, `:L51-76`).
- **(e) Typed ULID wrapper — 1 (the only file with executable logic):** `RunId` — `record RunId(Ulid value) implements Comparable<RunId>`, methods `compareTo` (`:L37-40`) and `toString` (`:L42-45`), both one-line delegations.
- **(f) Enums — 5 (value enums, no methods):** `ConcurrencyMode`, `RunStatus`, `PendingStatus`, `UnavailablePolicy`, `MaxExceededSeverity`.
- **(g) Module/package descriptors — 2:** `module-info.java` (`requires transitive` platform/event/device/state; `exports com.homesynapse.automation`), `package-info.java`.

No type contains Phase-3 logic; none is "mixed" (every service interface is purely abstract).

### C2. Sealed hierarchies (verbatim permits; Tier 1 = real, Tier 2 = reserved 0-field)

**TriggerDefinition** (`TriggerDefinition.java:45-49`) — 5 real + 4 reserved:
```java
public sealed interface TriggerDefinition
        permits StateChangeTrigger, StateTrigger, EventTrigger,
                AvailabilityTrigger, NumericThresholdTrigger,
                TimeTrigger, SunTrigger, PresenceTrigger, WebhookTrigger {}
```
Real: `StateChangeTrigger`(5 fields), `StateTrigger`(4), `EventTrigger`(2, no `forDuration` by design), `AvailabilityTrigger`(3), `NumericThresholdTrigger`(5). Reserved (0-field): `TimeTrigger`, `SunTrigger`, `PresenceTrigger`, `WebhookTrigger`.

**ConditionDefinition** (`:37-40`) — 6 real + 1 reserved:
```java
public sealed interface ConditionDefinition
        permits StateCondition, NumericCondition, TimeCondition,
                AndCondition, OrCondition, NotCondition, ZoneCondition {}
```
Real: `StateCondition`(3), `NumericCondition`(4), `TimeCondition`(2), `AndCondition`/`OrCondition`(List), `NotCondition`(1). Reserved: `ZoneCondition`. *Spot-check note:* `TimeCondition` (`:21-25`) is a real 2-field record but has **no compact constructor** — its "at least one of after/before non-null" rule is deferred to YAML-load (Phase 3), and `MODULE_CONTEXT.md:111` slightly overstates it as enforced.

**ActionDefinition** (`:36-40`) — 5 real + 3 reserved:
```java
public sealed interface ActionDefinition
        permits CommandAction, DelayAction, WaitForAction,
                ConditionBranchAction, EmitEventAction,
                ActivateSceneAction, InvokeIntegrationAction, ParallelAction {}
```
Real: `CommandAction`(4, incl. `UnavailablePolicy`), `DelayAction`(1), `WaitForAction`(3), `ConditionBranchAction`(3, recursive), `EmitEventAction`(2). Reserved: `ActivateSceneAction`, `InvokeIntegrationAction`, `ParallelAction`.

**Selector** (`:33-36`) — 6 permits, all real (no reserved):
```java
public sealed interface Selector
        permits DirectRefSelector, SlugSelector, AreaSelector,
                LabelSelector, TypeSelector, CompoundSelector {}
```

### C3. Service interfaces (verbatim signatures, all pure-abstract)

- `AutomationRegistry`: `void load(List<AutomationDefinition>)`; `Optional<AutomationDefinition> get(AutomationId)`; `Optional<AutomationDefinition> getBySlug(String)`; `List<AutomationDefinition> getAll()`; `void reload(List<AutomationDefinition>)`.
- `TriggerEvaluator` (`:41,52,59`): `List<AutomationId> evaluate(EventEnvelope)`; `void cancelDurationTimer(AutomationId, int)`; `int activeDurationTimerCount()`.
- `ConditionEvaluator` (`:33`): `boolean evaluate(ConditionDefinition, StateSnapshot)`.
- `ActionExecutor` (`:35`): `void execute(List<ActionDefinition>, RunContext)`.
- `RunManager` (`:55-91`): `Optional<RunId> initiateRun(AutomationDefinition, EventEnvelope, List<Integer>, Map<String,Set<EntityId>>, int)`; `Optional<RunContext> getActiveRun(RunId)`; `RunStatus getStatus(RunId)`; `int activeRunCount()`; `int activeRunCount(AutomationId)`.
- `CommandDispatchService` (`:43-44`): `void dispatch(EventId, EntityId, String, Map<String,Object>)`.
- `PendingCommandLedger` (`:40-64`): `void trackCommand(PendingCommand)`; `Optional<PendingCommand> getCommand(EventId)`; `List<PendingCommand> getPendingForEntity(EntityId)`; `int pendingCount()`.
- `SelectorResolver` (`:34`): `Set<EntityId> resolve(Selector)`.
- `ConflictDetector` (`:40`): `void scanForConflicts(EventId, List<RunContext>)`.

### C4. Can an automation rule execute end-to-end today? No.

Entirely interface scaffolding awaiting M7: (1) a Glob of `core/automation/src/main/java/**/*.java` returns only the 55 files above — no `*Impl`, no concrete service. (2) A Grep for `UnsupportedOperationException|TODO|class .*Impl|abstract class` across main source returns **zero**; method-body openers match **only `RunId.java`**. The behavioral methods don't exist as stubs — they're abstract declarations. (3) **No `src/test` directory** in the module. (4) `MODULE_CONTEXT.md:9,284-302` lists all engine behavior as Phase 3. (Compiled `build/` artifacts are just the Phase-2 types; no build run.)

### C5. M4/automation scoping docs & WU plan

- **Authoritative backlog** `phase-3-milestone-backlog.md`: Automation = **M7 (core) + M8 (advanced)** (`:105-119`), deps event-bus(M3)/state-store(M4)/config(M6); M7 scope = "Trigger/condition/action pipeline; AMD-25 temporal-duration modifier; command ledger basics" (`:111`); M8 = "Command ledger full; cascade governance; concurrency modes; AMD-17 orphan-detection" (`:112`). **No M7.x/M8.x work units broken out yet** — only the M7/M8 placeholders (`:123` notes 3–8 WUs per group, briefed JIT).
- **Status** `PROJECT_SNAPSHOT.md:13,25`: M3 complete; next = M4.0 (State Store); Doc 07 (Automation) "Locked + AMD-25 integrated."
- **Research 4** brief (`instructions/Research_4_Automation_Engine_Brief.md:19`, target "M7/M8") and PM assessment (`assessments/2026-05-22_Research_4_PM_Assessment.md`): **complete**, dispositions REC-31..40 (8 ACCEPT / 2 MODIFY+ACCEPT / 0 REJECT, `:42`), allocates **AMD-48..52** (`:175-183`), 10-step "M7 Implementation Order" (`:224-236`), with 4 open decision-questions for Nick (DQ-1/2/3/5). New automation work it surfaces: ~3 new trigger permits, a `SemanticTagSelector`, a `RunCausalChain` replacing `RunContext.cascadeDepth`, ~11 new automation event records + ~5 projection handlers.
- **Master release plan** `master-release-plan.md:172-173,287-288`: "Automation Engine (core/advanced)" = Week 20–21, consistent with M7/M8.

**Bottom line:** No "M4 automation" doc exists because automation is M7/M8 here. Scoping is advanced at the research/amendment level (Research 4 + AMD-48..52 → M7); **no implementation WUs authored yet**; immediate next is M4 (State Store).

---

## Section D: Integration Boundary Reality

**Overarching finding:** The integration boundary is almost entirely Phase-2 spec. Across the three integration modules and the command path there is **one concrete production class of note**; the only working `EntityRegistry`, `IntegrationContext` assembly, and `CommandHandler` are **test fixtures** (`src/testFixtures`). Supervisor, command dispatch, scoped registries, REST command handler, and all Zigbee protocol logic are unimplemented.

### D1. IntegrationContext composition

`IntegrationContext` is a **record** (`integration/integration-api/.../IntegrationContext.java:93-104`) with a null-validating compact constructor — **10 fields, 7 mandatory, 3 optional (nullability, not `Optional<>`):**

```java
public record IntegrationContext(
    IntegrationId integrationId, String integrationType,
    EventPublisher eventPublisher, EntityRegistry entityRegistry,
    StateQueryService stateQueryService, HealthReporter healthReporter,
    ConfigurationAccess configAccess, SchedulerService schedulerService,
    TelemetryWriter telemetryWriter, ManagedHttpClient httpClient) {
```
Mandatory (`requireNonNull`, `:112-119`): integrationId, integrationType, eventPublisher, entityRegistry, stateQueryService, healthReporter, configAccess. Optional (`null` unless declared via `RequiredService`): schedulerService, telemetryWriter, httpClient (`:120-122`). It is the single entry point handed to an adapter ("no god object," `:18-23`).

### D2. Least-privilege (INV-SE-04) — NOT ENFORCED IN CODE

**`INV-SE-04` does not appear anywhere in the repository** (no source, doc, or test — repo-wide grep, zero matches), so its text can't be quoted. The "integration sees only its own entities" property is **documented in Javadoc but enforced nowhere executable:** (1) `IntegrationContext.java:25-32` asserts the registry "filter[s] by `integration_id`" via "build-time + JPMS" enforcement — narrative, no code. (2) `EntityRegistry` (`core/device-model/.../EntityRegistry.java:32-110`) is an interface whose `listAllEntities()` (`:56`) returns **all** entities — no `integration_id` parameter on any method, no scoped overload. (3) **No production `implements EntityRegistry`** exists. (4) The only impl is the test stub `StubEntityRegistry` (`integration-api/src/testFixtures/.../StubIntegrationContext.java:350-467`), whose `listAllEntities()` returns the whole map unfiltered, and which builds the **production record directly** (no scoped wrapper). **Verdict:** scoping is deferred/unimplemented — neither runtime check, type constraint, nor wrapper object.

### D3. integration-zigbee (Block P) — Phase-2 only

**38 `.java` types + 1 `module-info.java`** in `src/main`; **zero test files**. By kind: 19 records, 8 interfaces (2 sealed/non-sealed), 7 enums, plus `ZigbeeAdapter`/`ZigbeeAdapterFactory`. Organized by concern: adapter lifecycle/factory; coordinator transport/protocol (`CoordinatorTransport`, `CoordinatorProtocol`, `EzspFrame`/`ZnpFrame`/`ZclFrame`, `ZigbeeFrame` sealed); network/topology (`NetworkParameters`, `NeighborTableEntry`, `NodeDescriptor`, `RouteHealth`, `EndpointDescriptor`, `IEEEAddress`, `RouteStatus`); commissioning (`InterviewResult`, `InitializationWrite`, `InterviewStatus`); cluster/attribute (`ClusterHandler`, `ValueConverter`, `AttributeReport`, `ClusterOverride`, `ReportingOverride`, `CommandType`); device profiles (`DeviceProfile`, `ManufacturerModelPair`, `DeviceProfileRegistry`, `ZigbeeDeviceRecord`, `DeviceCategory`, `ZoneType`); manufacturer codecs (`ManufacturerCodec` sealed, `TuyaDpCodec`/`XiaomiTlvCodec` non-sealed, `TuyaDatapointMapping`, `XiaomiTagMapping`, `TuyaDpType`); availability (`AvailabilityTracker`, `AvailabilityReason`).

**Zero Phase-3 implementation.** Only executable code = record compact-constructor validation (e.g. `EndpointDescriptor.java:48`, `NetworkParameters.java:43-47`), enum accessors (`CommandType.java:52,61`), and small pure helpers (`IEEEAddress.toHexString/fromHexString`). No serial I/O, no ZNP/EZSP framing, no ZCL codec. The documented impls `ZnpTransport`/`EzspAshTransport` (`CoordinatorTransport.java:10-12`), `ZigbeeAdapterFactoryImpl` (`ZigbeeAdapterFactory.java:31`), and Tuya/Xiaomi parsing (`TuyaDpCodec.java:15`, `XiaomiTlvCodec.java:20` — "Phase 3 implements parsing") are named in prose but **absent from source**.

### D4. CommandHandler routing — unimplemented at every hop

The intended chain — `POST /api/v1/entities/{id}/commands` → emit `command_issued` → `CommandDispatchService.dispatch()` → resolve integration via `DeviceRegistry` → emit `command_dispatched` → `IntegrationSupervisor` filters by `integrationId` → `adapter.commandHandler().handle(CommandEnvelope)` → adapter emits `command_result` — is **specified in interfaces/records/Javadoc with no concrete implementation at any hop:**

1. **REST entry — record only.** `CommandRequest` (record, `api/rest-api/.../CommandRequest.java:31`) and response records exist, but there is **no endpoint handler that consumes `CommandRequest`** — the only concrete endpoints are read-only (`GetEntityEndpoint`, `ListEntitiesEndpoint`, `ProjectionStatusEndpoint`, `DlqStatusEndpoint`); `EndpointHandler` is a `@FunctionalInterface`.
2. **Dispatch contract — interface only.** `CommandDispatchService` (`core/automation/.../CommandDispatchService.java:32-45`, "separate subscriber on its own VT in Phase 3") has **no implementing class**.
3. **The documented resolver method does not exist.** `CommandDispatchService.java:15-16` says it resolves via `DeviceRegistry.getIntegrationForEntity()`, but that method is **not declared on `DeviceRegistry`** (`core/device-model/.../DeviceRegistry.java:29-88`) — the string appears only in that Javadoc. (The owning integration is on `Device.integrationId` (`Device.java:53`), but no resolver surfaces it.)
4. **Supervisor — interface only.** `IntegrationSupervisor` (`integration/integration-runtime/.../IntegrationSupervisor.java:76`) has **no implementation**; `integration-api`'s `module-info.java:11-14` says the impl "lives in integration-runtime" — but it isn't written. The only working `CommandHandler` is `StubCommandHandler` (test fixtures).

### D5. Other integrations (Matter, Z-Wave, MQTT, Thread) — NONE

Only three integration modules are registered (`integration-api`, `integration-runtime`, `integration-zigbee`); no `integration-matter/zwave/mqtt/thread` module, directory, factory, adapter, or descriptor exists. A repo-wide search for those protocols finds **only Javadoc/comment/test-data mentions** (e.g. `IntegrationAdapter.java:11`, `IntegrationId.java:13`, a `"zwave"` test literal in `CustomCapabilityTest.java:189`). Consistent with `IntegrationFactory.java:19-23` (DECIDE-04): "single MVP integration (Zigbee)."

---

## Section E: Testing Infrastructure Reality

All counts exclude `build/` (verified zero test sources there). Counting method: **anchored** = `grep -cE "^[[:space:]]*@Test\b"` (counts real method annotations, excludes Javadoc/comment refs). Raw `@Test` substring = 1403; **anchored = 1396** (the accurate executable `@Test` count). `@ParameterizedTest` (20) and `@ArchTest` (9) are separate annotations, not in the 1396.

### E1. Total counts & category breakdown

| Metric | Result |
|---|---|
| Files containing `@Test` | 163 |
| Anchored `@Test` methods | **1396** |
| `@ParameterizedTest` | 20 |
| `@ArchTest` | 9 |
| **Total executable test methods** | **1425** |

Anchored `@Test` by module group (sums to 1396): platform 85, core 1184, integration 45, config 13, api 25, observability 0, web-ui 0, lifecycle 18, app 0, testing 26 (test-support 14 + integration-tests 12), spike 0.

Category breakdown (by reliable structural signal — there is no `*UnitTest` naming convention, so unit/contract co-mingle in `src/test`):
- **Contract (abstract suite definitions): 144 `@Test`** — the 10 abstract `*ContractTest` classes (E2). Each runs once *per concrete subclass* at runtime, so runtime contract executions are far higher.
- **Integration / E2E: 14 `@Test`** across 10 `*IT.java` files (8 in `testing/integration-tests/.../it/` = 12 methods incl. `EndpointE2eIT`=5; plus `core/event-bus/.../ReplayTransitionIT`=1 and `core/state-store/.../StateProjectionVerticalIT`=1). No `*E2ETest`/`*IntegrationTest`-named files exist — E2E uses the `*IT` suffix.
- **Architecture: 9 `@ArchTest`** in `HomeSynapseArchRulesTest` (E4).
- **Unit (residual): ~1238 `@Test`** = 1396 − 144 − 14 (folds in 9 contract-subclass extras + 14 `EventCollectorTest` fixture meta-tests; +20 `@ParameterizedTest` are unit-style and not in this tally).

### E2. Abstract contract test suites — 10, not 3

The PM's 3 are confirmed exactly; **7 more exist.** Per-suite `@Test`:

| # | Suite (path under repo) | `@Test` | Concrete impls |
|---|---|---|---|
| 1 | `core/event-model/src/testFixtures/.../EventStoreContractTest.java` | **27** | `InMemoryEventStoreTest`, `SqliteEventStoreTest` |
| 2 | `core/event-bus/src/testFixtures/.../CheckpointStoreContractTest.java` | **9** | `InMemoryCheckpointStoreTest`, `SqliteCheckpointStoreTest` |
| 3 | `core/state-store/src/testFixtures/.../ViewCheckpointStoreContractTest.java` | **10** | InMem(+1), Sqlite(+3) |
| 4 | `core/event-bus/src/testFixtures/.../DeadLetterStoreContractTest.java` | 10 | `SqliteDeadLetterStoreContractTest` (concrete `final` despite name) |
| 5 | `core/event-bus/src/testFixtures/.../EventBusContractTest.java` | **47** | `InProcessEventBusTest`, `InMemoryEventBusTest` (10 `@Nested` classes) |
| 6 | `core/persistence/src/testFixtures/.../ReadExecutorContractTest.java` | 5 | InMemory, PlatformThread |
| 7 | `core/persistence/src/testFixtures/.../WriteCoordinatorContractTest.java` | 12 | InMemory, PlatformThread (4 `@Nested`) |
| 8 | `core/state-store/src/testFixtures/.../ProjectionAdvancerContractTest.java` | 11 | `InMemoryProjectionAdvancerTest` |
| 9 | `core/state-store/src/testFixtures/.../StateProjectionContractTest.java` | 9 | `InMemoryStateProjectionTest` (+5); `extends SubscriberContractTest` |
| 10 | `core/state-store/src/testFixtures/.../SubscriberContractTest.java` | 4 | (inherited via #9) |

Total abstract-suite `@Test` = 144. Note the dual-implementation pattern (in-memory + real/SQLite or platform-thread) for every core port, and contract inheritance (`StateProjectionContractTest extends SubscriberContractTest`).

### E3. `testing/test-support` fixture inventory

All 7 PM-expected types present (in `src/main/java/com/homesynapse/test/`), plus 3 AssertJ assertion classes + entry point. `test-support` distributes via `src/main` (normal dependency), unlike the contract suites (`src/testFixtures`).

- `TestClock` — controllable `Clock` (`AtomicReference<Instant>`); `at(...)`, `createDefault()` (fixed 2026-01-01Z), `advance(Duration)`, `setFixed`, `peek`.
- `SynchronousEventBus` — single-threaded inline `EventBus` for determinism; `registerHandler(...)`, `notifyEvent` runs handlers synchronously in registration order.
- `EventCollector` — thread-safe `EventEnvelope` accumulator (`CopyOnWriteArrayList`, LTD-11 compliant); `add`, `events`, `eventsOfType`, `awaitCount(int,Duration)`, `awaitAtLeast`.
- `TestSubscriber` — configurable pull subscriber; `withProcessingDelay`, `withFailOnNthEvent`, `registerWith(SynchronousEventBus)`; `BATCH_SIZE=100`.
- `GivenWhenThen` — event-sourced assertion DSL; `given(...).whenProcessedBy(...).thenAssert(...)`. Contains its OWN nested non-thread-safe `EventCollector` (deliberately distinct from the standalone one).
- `NoRealIoExtension` — JUnit 5 extension rejecting non-localhost I/O (skips when `@RealIo` present).
- `RealIo` — `@interface` exempting tests from the I/O guard + filesystem ArchUnit rule.
- AssertJ: `HomeSynapseAssertions` (entry: `assertThat(EventEnvelope|CausalContext|SubjectRef)`), `EventEnvelopeAssert` (~16 matchers incl. `hasCorrelationId`, `hasNonNullActorRef`, `hasGlobalPosition`), `CausalContextAssert`, `SubjectRefAssert`. Only test in the module: `EventCollectorTest` (14 `@Test`). Nothing the PM expected is missing.

### E4. ArchUnit rules — 9, not 7

`app/homesynapse-app/src/test/java/com/homesynapse/app/HomeSynapseArchRules.java` (lives in the app test source set because it depends on all modules; on classpath to dodge a JPMS/ArchUnit + `-Werror` catch-22). `grep -cE "static final ArchRule"` → **9**; `HomeSynapseArchRulesTest` registers all 9 as `@ArchTest`. Rules 8–9 are M3.6e.2 additions.

1. `NO_SYNCHRONIZED_METHODS` — LTD-11: no `synchronized` methods (use `ReentrantLock`).
2. `NO_DIRECT_TIME_ACCESS` — Clock injection; no `Instant.now()`/`System.currentTimeMillis()` etc. (except app/platform/test).
3. `NO_SERVICE_LOADER` — DECIDE-04: no `ServiceLoader`.
4. `NO_REVERSE_DEPENDENCIES` — core packages must not depend on integration/api/lifecycle/app.
5. `NO_DIRECT_FILESYSTEM_IN_CORE` — core must not touch `java.io.File`/`java.nio.file.Files` (use `PlatformPaths`).
6. `NO_INTERNAL_PACKAGE_ACCESS` — non-`internal` classes must not depend on `..internal..`.
7. `NO_JSON_TYPE_INFO_IN_EVENTS` — event package must not use `@JsonTypeInfo`.
8. `QUERY_SERVICE_READ_ONLY` (M3.6e.2) — `api.rest..` must not access `persistence..` (reads go via `StateQueryService`).
9. `REST_ENDPOINTS_NO_EVENT_PUBLISHING` (M3.6e.2) — `api.rest..` must not access `EventPublisher`.

### E5. CI pipeline

Single workflow `.github/workflows/ci.yml` (one job `check`). **Triggers:** push to `main`/`develop`, PRs to `main`. **Env:** `ubuntu-latest`, `timeout-minutes: 15`, `permissions: contents: read`, JDK = `actions/setup-java@v4` `distribution: corretto`, `java-version: 21`. **Runs:** checkout → setup JDK 21 → `gradle/actions/setup-gradle@v4` → **`./gradlew check --no-daemon`** (the sole gate — runs all unit/contract/integration/`@ArchTest` tests) → on failure, uploads `**/build/reports/tests/`. No separate lint/static-analysis step, and **no Pi runner** (hardware validation is manual on `hs-dev-1`, see F4).

---

## Section G: Forward-Looking Foundations

Verdict key: **IN CODE** (concrete production type/field) / **SPEC-ONLY** (only in `homesynapse-core-docs`) / **FUTURE WORK** (not found; search terms shown).

### G1. Multi-user identity (INV-MU-01) — PARTIALLY IN CODE

Typed identity primitives exist and are plumbed through event/persistence, but there is **no Person entity, no role/permission model, and REST auth is not person-linked.**
- In code: **`PersonId`** (`platform/platform-api/.../identity/PersonId.java:26`, typed ULID wrapper); **`SubjectType.PERSON`** + **`SubjectRef.person(PersonId)`** (`SubjectRef.java:111-114`); `EventEnvelope.actorRef` is **untyped `Ulid`** (not `PersonId`), nullable (`EventEnvelope.java:112`); `EventOrigin.USER_COMMAND`; PersonId registered for JSON serde (`PersistenceJacksonModule.java:79`).
- Absent (zero matches): no `Person`/`User` entity or registry (PersonId is referenced only by itself, `SubjectRef`, `EventEnvelope` Javadoc, and the Jackson module); no role/permission/RBAC (the only `Permission` type, `core/device-model/.../Permission.java`, is a device-attribute `READ/WRITE/NOTIFY` enum); no `Household/Role/Occupant/UserProfile/Preference/Tenant`. REST auth = `ApiKeyIdentity(keyId, displayName, createdAt)` (`api/rest-api/.../ApiKeyIdentity.java:36`) via `AuthMiddleware` — caller is a key, never a person. INV-MU-03/04 (preference arbitration, household roles) are SPEC-ONLY (`governance/Architecture_Invariants_v1.md:667-681`).

### G2. Energy first-class (INV-EI-01) — IN CODE at device/capability layer; energy EVENT types NOT in code

In code (`core/device-model/`): `EnergyMeter` capability (`EnergyMeter.java:34`, `energy_wh`/`direction`/`cumulative`, `reset_meter`), `EnergyDirection` enum (`IMPORT/EXPORT/BIDIRECTIONAL`), `PowerMeter` (`power_w`/`voltage_v`/`current_a`), `PowerMeasurement`, `EntityType.ENERGY_METER` (`EntityType.java:77`). **Gap:** none of the 22 core event types (`EventTypes.java:244-267`) is energy-specific; energy rides the generic numeric telemetry path (`TelemetrySample`, `TelemetrySummaryEvent`). INV-EI-01's "meter readings, tariff changes, grid signals, battery SoC" event types are SPEC-ONLY; no battery/inverter/EV/grid types in code.

### G3. Protocol-agnostic network telemetry (INV-MN-01) — PARTIALLY IN CODE

Generic per-device link quality exists as a capability: **`DeviceHealth`** (`core/device-model/.../DeviceHealth.java:30`) exposes `rssi_dbm` and `lqi` as generic attributes — protocol-neutral, flows through the normal pipeline. Richer mesh/route telemetry is **Zigbee-package-only**: `RouteHealth`, `RouteStatus`, `NeighborTableEntry.lqi`, `NetworkParameters` (all `com.homesynapse.integration.zigbee`). **No generic `NetworkHealth`/`NetworkTelemetry` domain type or event** (integration-api's `HealthState` is adapter-process health, not RF/link telemetry). The unified RF/mesh-health dashboard (INV-MN-02..04) is SPEC-ONLY.

### G4. Local AI capability (INV-AI-04) — ENTIRELY FUTURE WORK

No inference/ML/model-loading code and **no ML dependency in any `build.gradle.kts`** (searched onnx/tensorflow/pytorch/tflite/djl/tribuo/mxnet/llama/inference/neural/tensor/embedding — zero). The only source hits for `inference`/`embedding` are unrelated comments (`ListEntitiesEndpoint.java:64` "inference … (premature)"; `EventPayloadCodec.java:173` "for embedding in a [string]"). INV-AI-04 (`Architecture_Invariants_v1.md:595-599`, names LightGBM/TinyLSTM/ONNX/DJL/Hailo-10H) and INV-AI-05 ("data pipeline must be in place") are fully SPEC-ONLY — no behavioral-data pipeline type exists either.

### G5. Spatial / presence (INV-MU-02) — PARTIALLY IN CODE

In code: presence is a registered first-class event — `PresenceSignalEvent(signalType, signalSource, signalData)` and `PresenceChangedEvent(previousState, newState)` (`core/event-model/...`, in `EventTypes.java:260-261`); **`AreaId`** (`platform/platform-api/.../identity/AreaId.java:21`, ULID wrapper) is a real field on `Device.areaId` (`Device.java:54`) and `Entity.areaId` (`Entity.java:51`); `Occupancy` capability. **Gaps:** "Area" is **only a bare ULID** — no `Area`/`Room`/`Zone`/`Floor` type, no name/hierarchy/coordinates anywhere (zero matches for coordinate/geometry/latitude/floorplan); BLE/UWB/GPS appear only as **example strings** in `PresenceSignalEvent.java:11` Javadoc (`signalData` is opaque `String`); presence automation is stubbed — `PresenceTrigger`/`ZoneCondition` are empty Tier-2 records ("Requires Tier 2 presence infrastructure … zone definition model"). INV-MU-02 is largely SPEC-ONLY beyond this event scaffolding + area-id wiring.

| Q | Invariant | Verdict | Strongest in-code evidence | Largest gap |
|---|---|---|---|---|
| G1 | INV-MU-01 | Partial | `PersonId`, `SubjectType.PERSON`, `actorRef` | No Person entity; no roles; REST auth = API key |
| G2 | INV-EI-01 | In code (device layer) | `EnergyMeter`, `EntityType.ENERGY_METER` | No energy event types |
| G3 | INV-MN-01 | Partial | `DeviceHealth` (`rssi_dbm`,`lqi`) | Mesh telemetry zigbee-only; no generic type/event |
| G4 | INV-AI-04 | Future work | none | No ML code or dependency anywhere |
| G5 | INV-MU-02 | Partial | presence events; `AreaId` on Device/Entity | `Area` is a bare ULID; no coords/BLE/UWB; triggers stubbed |

---

## Section H: Open Questions and Unresolved Issues

**Scope note.** The "four open architecture questions" are **not** in the 2026-05-19 cross-tier audit (`nexsys-hivemind/context/audits/archive/2026-05-19_cross-tier-deployment-audit.md`, titled "Cross-Tier Deployment Versatility Audit"). They live in a follow-on gap-closure doc which states Nick "surfaced four unexamined architectural questions that the audit had missed" (`homesynapse-core-docs/research/2026-05-20_M3_Audit_Gap_Closure_v1.md:30`).

### H1 — The four open architecture questions (all answered in the 2026-05-20 gap-closure doc)

That doc's own header status is **"Draft (Artifact 1 …)"** (`:5`) with a §8 "STOP for Review" gate (`:353-362`) — so the answers are evidence-backed and carried into the M3.6 WU plan, but the doc was never re-stamped Final.

- **(a) globalPosition contiguity — RESOLVED: gap-tolerant by construction.** "No code in `core/event-bus`, `core/state-store`, or `core/event-model` depends on contiguous positions" (`:118-119`); cursor advance is `Math.max(cursor, envelope.globalPosition())` (`StateProjection.java:576`), gap detection `<=` (`TransitionCoordinator.java:91`). **Affects M3.6? NO** (`:122`). Audit D6-03 concurs: "monotonic, not contiguous" (`:180`).
- **(b) chain_hash backend semantics — RESOLVED: reserved schema, zero-bind.** "Every event row gets `chain_hash = 0x00…00`" (`:163`); `SqliteEventStore.java:353` binds `ZERO_HASH` unconditionally. **Affects M3.6? NO** (`:169`). The recommended (non-blocking) AMD-37 "Activation invariant: … single-writer or partition-local chain construction" annotation (`:173`) **was NOT added** — and **AMD-37's body is stale**: it still describes `ps.setNull(16, Types.BLOB)` "chain_hash deferred to crypto milestone" (`AMD-37_…md:14,46`), whereas shipped code binds `ZERO_HASH`. Substance settled; doc trail inconsistent.
- **(c) event type registration portability — RESOLVED and IMPLEMENTED.** "static list assembled at composition root … the only DECIDE-04-compliant option" (`:217-218`). **Affects M3.6? YES — minimally** (`:230`), the M3.6c sub-WU. **Verified in code:** `EventTypes.CORE_PRODUCTION_EVENT_CLASSES` (`EventTypes.java:244`), `IntegrationEvents.LIFECYCLE_EVENT_CLASSES` (`IntegrationEvents.java:50`), concatenated in `HomeSynapseCore.java:208-209`. The only one of the four that required and got a code change.
- **(d) home_id on EventEnvelope — RESOLVED: deferral decision.** "Defer to the multi-hub WU. Do not surface `homeId` on `EventEnvelope` in M3.6" (`:312`); `home_id` is written but `fromRow()` never reads it back (`:275-290`). **Affects M3.6? NO** (`:324`). The recommended AMD-34 annotation (`:320`) **was NOT added** to `AMD-34_…md`. Audit D6-05 flags the same as a future (not-MVP) multi-hub risk (`:182`).

> **Closing note:** the 2026-05-19 audit's actual headline finding was **DEFECT C-01 "`DeploymentProfile` defined but never wired"** (BLOCKING). **This is now RESOLVED (M3.6a):** `DatabaseExecutor` takes `DeploymentProfile profile` (`DatabaseExecutor.java:118,147`) and renders PRAGMAs from it (`connectionPragmas(profile):409`, `cacheSizeKiB():431`); the hardcoded pragma list is gone.

### H2 — OR-M3-17 (NO_OP_DERIVATION) / OR-M3-18 (NO_OP_ADVANCER): RESOLVED in M3.7

Both were M3.6d-b composition-root placeholders, MEDIUM-severity, gating M3.7 E2E tests; **both resolved in M3.7** (`nexsys-hivemind/context/handoff/pm-handoff.md:100-108`):
- OR-M3-17 → renamed to `MINIMAL_DERIVATION_RULE = context -> List.of()` (`HomeSynapseCore.java:144-145`, wired `:255`). Derives nothing because its consumer (automation engine) is later-milestone scope.
- OR-M3-18 → replaced by `MinimalProjectionAdvancer` (`lifecycle/.../MinimalProjectionAdvancer.java`, wired `HomeSynapseCore.java:257`), reads from `EventStore` via the bounded-window contract.

Residual (non-blocking, **M4.0** scope): both are deliberately *minimal*; the full replacement is `DispatchingProjectionAdvancer` (Research 8 REC-28, per-event-type dispatch) — `MinimalProjectionAdvancer` Javadoc `:45-51`.

### H3 — AMD-45 (Atomic Subscriber+View Checkpoint Coupling): DRAFT, implementable but with 2 self-flagged open decisions

`homesynapse-core-docs/design/amendments/AMD-45_…md`, **Status: DRAFT** (`:5`), "Date applied: —", "Slot as M4.0's first work unit" (`:12`). Substantially complete: problem statement, invariant alignment, the `CrashRecoveryReplayIT` regression spec, and file-impact list are detailed, and the core mechanism is clear — write both checkpoints in one transaction via the already-built-but-unwired `AtomicCheckpointWriter` ("fully implemented and tested … but is not wired into the production checkpoint path," `:54`; confirmed independently in B2). **But two design forks are explicitly left open for implementation planning:** (1) mechanism Option A (SubscriberInfo flag) vs Option B (CheckpointStore delegation) (`:64-69`); (2) cross-module boundary — interface-in-state-store vs expose-through-PersistenceFactory, since `AtomicCheckpointWriter` is package-private in `com.homesynapse.persistence` (`:130-135`). So: implementable from, but a PM must close both forks before coding.

### H4 — Amendments not in APPLIED status

20 amendment docs in `design/amendments/`; **15 APPLIED** (AMD-26,27,31,32,33,34,35,36,37,38,40,41,42,43 + one more). The **5 not APPLIED:**

| AMD | Title | Status |
|---|---|---|
| AMD-45 | Atomic Subscriber+View Checkpoint Coupling | **DRAFT** |
| AMD-44 | Floor Aggregate and EntityRole Enum | **RATIFIED (pending implementation)** |
| AMD-25 | Temporal Duration Trigger Modifier | **Approved — ready for integration** |
| AMD-39 | Journal Size Limit Revision | **WITHDRAWN** (D1 showed existing 6 MB limit sufficient) |
| AMD-M2Bridge | Tier-2 Schema Reservations | **(no Status field present — governance-hygiene gap)** |

AMD-44 and AMD-25 are accepted-but-unimplemented (pending code, not open debate); AMD-39 is closed-negative.

### H5 — Material technical debt in production source (`src/main`)

**106 debt-marker hits across 73 files**; **zero literal `TODO`/`FIXME`/`XXX`/`HACK`** — debt is expressed as Javadoc prose + `UnsupportedOperationException`. Most are benign. Material debt, grouped:
- **Automation engine — schema-only (largest body):** 8 Tier-2 "implementation deferred" stubs (`ActivateSceneAction`, `InvokeIntegrationAction`, `ParallelAction`, `PresenceTrigger`, `SunTrigger`, `TimeTrigger`, `WebhookTrigger`, `ZoneCondition`), plus `CommandDispatchService.java:23` ("VT in Phase 3") and `ConflictDetector.java:17` (priority suppression deferred). Several triggers defer validation to "YAML load (Phase 3)."
- **Backup/restore unimplemented:** `SqlitePersistenceLifecycle.java:392-394,406-408` — `createBackup()`/`restoreFromBackup()` throw "not yet implemented. Planned for post-M2." (audit D5-09, SIGNIFICANT).
- **Device-model confirmation primitive:** `WithinTolerance.java:24` — `evaluate()` throws "Implementation deferred to Phase 3" (tolerance-confirmation path non-functional).
- **Lifecycle wiring shims:** `HomeSynapseCore.java:269-270` health → SLF4J bridge "for now" (real HealthAggregator wiring is a future WU); `ThrowingStateQueryService` placeholder ("not yet wired — available after M3.6e"); `Main.java:11,20` still prints "not yet implemented."
- **Not material (excluded):** `EventBus.java:131-165` four `default` `UnsupportedOperationException` methods are AMD-42 interface-evolution shims overridden by `InProcessEventBus`; REST endpoint "recording stub" mentions describe the test strategy; `module-info` "M2 placeholder" comments are historical.
- **Related active open question:** `nexsys-hivemind/context/open-questions.md:21-27` — OQ-05-02 (`StateCheckpointSource` reconciliation-metadata threading), "Resolution: (open)", "Likely M4 scope"; a 5th `ReconciliationTest` method was deferred as it "would fail trivially against the current contract."

Cross-reference to A3: the supervisor's exponential-backoff retry loop is also dead code (`SubscriberSupervisor.java:84-87`) — material for anyone reasoning about delivery-retry semantics.

---

## Investigation Limitations

- **REST envelope→JSON serializer (B4, third bullet):** I report its *absence* from `api/rest-api/src/main` (no `ObjectMapper` construction, no `EventEnvelope` serializer). This is an absence-claim from targeted greps; if a REST mapper is wired at the composition root via a type I didn't search by name, I could have missed it — but no candidate file surfaced.
- **`notifyEvent` production wiring (B1, step 5):** the persist→notify hand-off is decoupled within the modules I read; the exact composition-root call site that invokes `EventBus.notifyEvent(...)` after each `publish` was not pinned to a line. The split itself is confirmed by Javadoc and the bus's `EventStore`-only dependency.
- **`INV-SE-04` text (D2):** the invariant ID is absent from the entire repo, so I could not quote its canonical wording; D2's verdict rests on the absence of enforcing code, not on the invariant text.
- **Test categorization (E1):** unit vs contract counts are structural approximations — there is no `*UnitTest` naming convention, so the ~1,238 "unit" figure is a residual, not a hand-classified count. The 1,396 `@Test` total and the 144 contract / 14 integration / 9 arch figures are exact.
- **Sub-agent-sourced sections (C, D, E, G, H):** gathered by parallel investigations and spot-verified by me against source on the highest-stakes claims (ZERO_HASH, `SecretStore` interface-only, PersonId serde, `AtomicCheckpointWriter` unwired, automation has no `src/test`, the 9th/10th contract suites). I did not independently re-open every file each sub-investigation cited; line numbers in those sections should be treated as high-confidence-but-spot-checkable.
- **`build/` artifacts:** intentionally excluded from all counts; I read no compiled output and ran no build, so any generated-source types are not represented (none expected for this codebase).

## Files Referenced

Repo-root-relative. Files I personally opened in full:

**homesynapse-core — production source:**
- `core/persistence/src/main/java/com/homesynapse/persistence/PlatformThreadWriteCoordinator.java`
- `core/persistence/src/main/java/com/homesynapse/persistence/WriteCoordinator.java`
- `core/persistence/src/main/java/com/homesynapse/persistence/WritePriority.java`
- `core/persistence/src/main/java/com/homesynapse/persistence/SqliteEventStore.java`
- `core/persistence/src/main/java/com/homesynapse/persistence/AtomicCheckpointWriter.java`
- `core/persistence/src/main/java/com/homesynapse/persistence/PersistenceJacksonModule.java`
- `core/persistence/src/main/java/com/homesynapse/persistence/EventPayloadCodec.java`
- `platform/platform-api/src/main/java/com/homesynapse/platform/identity/UlidFactory.java`
- `core/event-bus/src/main/java/com/homesynapse/event/bus/InProcessEventBus.java`
- `core/event-bus/src/main/java/com/homesynapse/event/bus/SubscriberRuntime.java`
- `core/event-bus/src/main/java/com/homesynapse/event/bus/ReplayWindowQueue.java`
- `core/event-bus/src/main/java/com/homesynapse/event/bus/SubscriberMode.java`
- `core/event-bus/src/main/java/com/homesynapse/event/bus/SubscriberSupervisor.java`
- `core/event-bus/src/main/java/com/homesynapse/event/bus/ReplayDriver.java`
- `core/event-bus/src/main/java/com/homesynapse/event/bus/TransitionCoordinator.java`
- `core/event-bus/src/main/java/com/homesynapse/event/bus/SubscriberDlq.java`
- `core/state-store/src/main/java/com/homesynapse/state/SelfProducedFilter.java`
- `core/event-model/src/main/java/com/homesynapse/event/CausalContext.java`
- `core/event-model/src/main/java/com/homesynapse/event/EventPublisher.java`
- `core/event-model/src/main/java/com/homesynapse/event/EventDraft.java`
- `config/configuration/src/main/java/com/homesynapse/config/SecretStore.java`
- `config/configuration/src/main/java/com/homesynapse/config/SecretEntry.java`
- `build-logic/src/main/kotlin/homesynapse.java-conventions.gradle.kts`
- `settings.gradle.kts`

**Key files cited by the sub-investigations (C/D/E/G/H), spot-verified:**
- `core/automation/...`: `TriggerDefinition`, `ConditionDefinition`, `ActionDefinition`, `Selector`, `RunId`, `AutomationDefinition`, `RunContext`, `CommandDispatchService`, `ConflictDetector`, and the 9 service interfaces; `MODULE_CONTEXT.md`
- `integration/integration-api/...`: `IntegrationContext`, `IntegrationAdapter`, `IntegrationFactory`; `src/testFixtures/.../StubIntegrationContext.java`
- `integration/integration-runtime/.../IntegrationSupervisor.java`; `integration/integration-zigbee/...` (38 types incl. `CoordinatorTransport`, `ZigbeeAdapter`, `TuyaDpCodec`)
- `core/device-model/...`: `EntityRegistry`, `DeviceRegistry`, `Device`, `Entity`, `Permission`, `EnergyMeter`, `EnergyDirection`, `PowerMeter`, `EntityType`, `DeviceHealth`, `Occupancy`, `WithinTolerance`
- `core/event-model/...`: `EventEnvelope`, `EventTypes`, `SubjectRef`, `SubjectType`, `EventOrigin`, `EventCategory`, `PresenceSignalEvent`, `PresenceChangedEvent`, `CommandDispatchedEvent`
- `core/state-store/.../StateProjection.java`; `core/persistence/.../DatabaseExecutor.java`, `SqlitePersistenceLifecycle.java`
- `platform/platform-api/.../identity/PersonId.java`, `AreaId.java`
- `api/rest-api/...`: `CommandRequest`, `ApiKeyIdentity`, `AuthMiddleware`, `EndpointHandler`, read endpoints
- `lifecycle/.../HomeSynapseCore.java`, `MinimalProjectionAdvancer.java`, `ThrowingStateQueryService.java`; `app/.../Main.java`, `HomeSynapseArchRules.java`, `HomeSynapseArchRulesTest.java`
- Contract suites under `*/src/testFixtures/...` (10), `testing/test-support/src/main/java/com/homesynapse/test/...`, `.github/workflows/ci.yml`
- `core/persistence/src/main/resources/db/migration/events/V001__initial_event_store_schema.sql`

**homesynapse-core-docs:**
- `research/2026-05-20_M3_Audit_Gap_Closure_v1.md`; `design/2026-05-20_M3.6_Composition_Root_Design.md`
- `design/amendments/AMD-45_…md`, `AMD-44_…md`, `AMD-37_…md`, `AMD-34_…md`, `AMD-25_…md`, `AMD-39_…md`, `AMD-M2Bridge_…md`
- `governance/Architecture_Invariants_v1.md`

**nexsys-hivemind:**
- `context/planning/phase-3-milestone-backlog.md`, `context/planning/master-release-plan.md`
- `context/status/PROJECT_SNAPSHOT.md`, `context/handoff/pm-handoff.md`, `context/handoff/coder-handoff.md`
- `context/instructions/Research_4_Automation_Engine_Brief.md`, `context/assessments/2026-05-22_Research_4_PM_Assessment.md`
- `context/audits/archive/2026-05-19_cross-tier-deployment-audit.md`, `context/open-questions.md`
- `coder/references/homesynapse-mental-model.md`

*End of report.*
