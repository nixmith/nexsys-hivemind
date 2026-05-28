# HomeSynapse Core — Cross-Tier Deployment Versatility Audit

**Audit date:** 2026-05-19
**Auditor:** Independent architecture auditor (read-only, no code changes)
**Codebase HEAD:** `5ae7912` — *"M3.4a: integration test module scaffold + harness + BurstLoadIT + HeapBudgetIT"*
**Audit-spec target commit:** `aaa07d8` — NOT FOUND in `git log`. Audit performed against the actual HEAD `5ae7912f96efb5ca96c06dc14baf30c5af2a5025`, which is consistent with the M3.4a deliverable described in the brief.

---

## STOP-on-Mismatch Gates

| Gate | Check | Result |
|---|---|---|
| G1 | `DeploymentProfile.java` has exactly STUDIO, HOME, PERFORMANCE | **PASS** — file at `core/persistence/src/main/java/com/homesynapse/persistence/DeploymentProfile.java`, lines 42/52/62. |
| G2 | `DatabaseExecutor.java` applies PRAGMAs in `start()` | **PASS** — `applyConnectionPragmas(writeConnection)` called at line 180; `setCreationTimePragmas(writeConnection)` at line 172 (new DB only). |
| G3 | `InProcessEventBus.java` has both constructors | **PASS** — convenience ctor at line 87, production ctor (with `BusMetrics` + `IntSupplier`) at line 107. |
| G4 | `ReplayDriver.java` has `MAX_REPLAY_PAGE`, `CHECKPOINT_EVENT_THRESHOLD`, `CHECKPOINT_MAX_INTERVAL_SECONDS` | **PASS** — lines 62, 65, 68. |
| G5 | `DerivedWriteRateLimit.java` is `public` (Bus-Fix Piece A promotion) | **PASS** — `public final class DerivedWriteRateLimit implements AutoCloseable` at line 47. |
| G6 | `testing/integration-tests/` has `BurstLoadIT` and `HeapBudgetIT` | **PASS** — both present under `testing/integration-tests/src/test/java/com/homesynapse/it/`. |

All six gates pass. The audit proceeds.

---

## CRITICAL UPSTREAM DRIFT (Audit Spec vs. Code)

The audit brief stated the SQLite PRAGMAs in `DatabaseExecutor.start()` as `cache_size=-128000`, `mmap_size=1073741824`, etc. Verification confirms the values, but it also surfaces a **previously unreported architectural defect** that dwarfs most of the findings below:

> **DEFECT C-01 — `DeploymentProfile` is defined but never wired.**
> `DeploymentProfile` (3 enum values STUDIO/HOME/PERFORMANCE with hand-tuned `cacheSizeKiB` and `mmapSizeBytes` values) is referenced in exactly **four files** (`grep DeploymentProfile`): the enum itself, `PersistenceConfig`, `MaintenanceSubscriber`, and the module's `MODULE_CONTEXT.md`.
>
> `DatabaseExecutor.CONNECTION_PRAGMAS` (lines 68–76) is a **hardcoded `List.of(...)`** containing `cache_size = -128000` (128 MiB) and `mmap_size = 1073741824` (1 GiB) — the values that match no profile exactly (PERFORMANCE has `mmap_size = 1 GB` but `cache = 64 MiB`, not 128 MiB; HOME's mmap is only 256 MiB).
>
> Neither `DeploymentProfile` nor `PersistenceConfig` is passed to `DatabaseExecutor` at construction (constructor signature `DatabaseExecutor(int readThreadCount, Clock clock)` at line 105). `SqlitePersistenceLifecycle` (line 120) likewise has no `PersistenceConfig` parameter.
>
> **Consequence:** every deployment — STUDIO/HOME/PERFORMANCE alike — gets a 128 MiB SQLite page cache and a 1 GiB mmap. On a 4 GB Pi 4 with `-Xmx1536m`, the JVM heap (1.5 GiB) + SQLite cache (128 MiB) + SQLite mmap (1 GiB) + OS overhead approaches the physical RAM ceiling; under load this is a swap-thrash hazard, and on a swap-less device (the M3.4a integration test JVM is `-Xmx256m`) it is hard to even start the process if the mmap reservation is attempted at the wrong moment.
>
> This finding is the single biggest cross-tier blocker in the codebase, larger in blast radius than any of the per-dimension findings below. It is BLOCKING for the Constrained tier in its base specification (Architecture Invariants §0.5 rule: every invariant must hold at Constrained at its base specification — INV-PR-01 "constrained hardware" is not satisfied today).

---

## Dimension 1 — Hardware-Specific Constants and Assumptions

### Findings table

| # | File | Constant / Value | Tier Impact | Severity | Recommended Action |
|---|---|---|---|---|---|
| D1-01 | `core/persistence/.../DatabaseExecutor.java:68-76` | Hardcoded `CONNECTION_PRAGMAS` list including `cache_size = -128000`, `mmap_size = 1073741824`, `busy_timeout = 5000` | **Constrained: BLOCKING** (128 MiB cache + 1 GiB mmap on 4 GB Pi). Standard/Enhanced: OK. Companion: N/A. Enterprise/NAS: `busy_timeout=5s` too low — Portability Architecture v1 §5.2 calls for 10–15 s on NAS. | **BLOCKING** | Add `DeploymentProfile` (and a future `PlatformInfo`) to `DatabaseExecutor` constructor; render `cache_size`, `mmap_size`, `busy_timeout` from the profile; gate the M3.6 lifecycle composition root on this. Estimated 2 files, ~4 hours including tests. |
| D1-02 | `core/persistence/.../DatabaseExecutor.java:344` | `PRAGMA page_size = 4096` (creation-time) | All tiers OK. SD card (Constrained) preferred page = 4096; cloud / Enhanced may benefit from 8192 or 16384 to reduce index height. | MINOR | Move to `DeploymentProfile` for symmetry; non-blocking. |
| D1-03 | `core/persistence/.../DatabaseExecutor.java:345` | `PRAGMA auto_vacuum = INCREMENTAL` | All tiers OK; vacuum chunk size driven by `MaintenanceSubscriber`. | INFO | None. |
| D1-04 | `core/persistence/.../DeploymentProfile.java:42,52,62` | `STUDIO(2_000, 67_108_864, 6_144_000)`, `HOME(16_000, 268_435_456, 6_144_000)`, `PERFORMANCE(65_536, 1_073_741_824, 6_144_000)` | 3 profiles for 6 deployment tiers. No Companion/Enterprise. Companion is N/A (no SQLite). Enterprise needs distinct PostgreSQL path. | SIGNIFICANT | Add 4th profile `ENTERPRISE` *or* gate on a `StorageEngine` enum (SQLITE vs POSTGRES). Wire from YAML config (Portability Architecture v1 §5.2). |
| D1-05 | `core/persistence/.../DatabaseExecutor.java:74` | `busy_timeout = 5000` (5 s) | Constrained/Standard/Enhanced: OK on local NVMe. NAS-backed Enterprise: insufficient (research recommends 10–15 s). Docker Desktop macOS/Windows: VirtioFS + WAL-shm needs `locking_mode=EXCLUSIVE` (Portability Architecture v1 §2.1, LTD-03 column). | SIGNIFICANT | Make `busy_timeout` profile-driven; add `locking_mode` PRAGMA for Docker-Desktop builds via a `DockerStorageMode` flag. |
| D1-06 | `core/event-bus/.../ReplayDriver.java:62,65,68` | `MAX_REPLAY_PAGE=500`, `CHECKPOINT_EVENT_THRESHOLD=200`, `CHECKPOINT_MAX_INTERVAL_SECONDS=2` | AMD-38 cadence — empirically validated by D1 WAL Pathology Spike for Constrained tier. Enhanced/Enterprise with 100k+ event/sec ingest may want a larger page (e.g., 5000) and a shorter checkpoint interval. | MINOR | Promote to `CheckpointPolicy` already declared in `core/state-store` (sealed interface, FixedCheckpointPolicy / AdaptiveCheckpointPolicy). Adapter exists in design but `ReplayDriver` constants are still inline. |
| D1-07 | `core/event-bus/.../ReplayWindowQueue.java:44` | `MAX_CAPACITY = 10_000` | Constrained: ~80 KB heap — fine. Enhanced/Enterprise: a 100k-event ingest burst would overflow → REPLAY restart loop. | SIGNIFICANT | Make profile-tuneable (`MAX_CAPACITY` → constructor arg, default 10_000); already factored as `ReplayWindowQueue` but enforcement is package-private. |
| D1-08 | `core/event-bus/.../SubscriberDlq.java:30` | `CAPACITY = 1024` | Per subscriber. 20 subscribers × 1024 entries ≈ 20K entries; bounded. Persistent overflow handled by `PersistentDlqWriter` seam (M3.5b). Acceptable across tiers. | INFO | None. |
| D1-09 | `core/event-bus/.../DerivedWriteRateLimit.java:50,53,56` | `DEFAULT_CAPACITY=200`, `REFILL_TOKENS_PER_TICK=10`, `REFILL_TICK_MILLIS=50` → 200 tokens/sec | StateProjection-only per AMD-43 §3.6.4. Constrained: appropriate. Enterprise with 10K entities and high derived-publish density: 200/s may starve. | MINOR | Already constructor-parameterizable (`new DerivedWriteRateLimit(capacity, clock, metrics, subscriberId)`). Wire from YAML in M3.6. |
| D1-10 | `core/event-bus/.../InProcessEventBus.java:55` | `PUBLISHER_BLOCKED_DEPTH_THRESHOLD = 5000` | Threshold defines "depth at which publisher-blocked counter increments". Per AMD-43. Pi 4: 5000-deep writer queue is already pathological; ENH/Enterprise might tolerate 50K+. | MINOR | Make profile-driven; defaults are fine. |
| D1-11 | `core/event-bus/.../QueueSaturationHealthCheck.java:90` | Constructor takes `warnDepth, criticalDepth, saturationTicks`; PLAN-M3 defaults WARN=5000 / CRITICAL=10000 / 5 ticks | Already DI'd at composition root. AcCEPTABLE across tiers via configuration. | INFO | None. |
| D1-12 | `core/event-bus/.../SubscriberSupervisor.java:40-55` | `MIN_BACKOFF_MS=3000`, `MAX_BACKOFF_MS=30000`, `JITTER_FACTOR=0.2`, `MAX_RETRIES=5`, `CIRCUIT_BREAKER_THRESHOLD=5`, `CRASH_WINDOW=10min` | All tiers OK (failure semantics, not capacity). Note: retry loop is currently dead code; first failure → immediate park. | INFO | None until retry-loop WU lands. |
| D1-13 | `core/persistence/.../PlatformThreadReadExecutor.java:67` (size from ctor); `SqlitePersistenceLifecycle.java:120` (`readThreadCount` arg) | Default 2 read threads (AMD-27, Pi 4 tuning). | Pi 4: correct. 64-core x86 server: 2 readers leaves 62 cores idle. Companion: N/A. | SIGNIFICANT | Default profile-driven (e.g., min(4, max(2, cores/4))); already parameterizable. Cap upper bound by SQLite WAL reader budget (~8 productive readers per LTD-03). |
| D1-14 | `core/persistence/.../PlatformThreadWriteCoordinator.java:51` | `SHUTDOWN_JOIN_TIMEOUT_MS = 5_000L` | All tiers OK. | INFO | None. |
| D1-15 | `core/persistence/.../PlatformThreadReadExecutor.java:49` | `SHUTDOWN_AWAIT_TIMEOUT_MS = 5_000L` | All tiers OK. | INFO | None. |
| D1-16 | `core/persistence/.../PlatformThreadWriteCoordinator.java:62-65` | Thread name `hs-write-0`; read pool uses `ReadThreadFactory` → `hs-read-N`. | Multi-instance: names collide if multiple HS processes run on the same host (Docker, K8s). JFR analytics gets confused. | MINOR | Prefix with PID or HomeId hash: `hs-<homeIdShort>-write-0`. |
| D1-17 | `core/state-store/.../SelfProducedFilter.java:68` | `DEFAULT_TTL = Duration.ofSeconds(60)` | At 200 publishes/s × 60s × ~80 bytes/entry ≈ 1 MB per projection. Constrained-OK. | INFO | None. |
| D1-18 | `core/state-store/.../StateProjection` | `CHECKPOINT_SIZE_WARN_BYTES = 10 * 1024 * 1024` (10 MB) | Advisory, non-blocking. Confirms ENTERPRISE-scale (10K entities) will exceed 10 MB checkpoints — design intent matches. | INFO | None. |
| D1-19 | `core/persistence/.../SqlitePersistenceLifecycle.java:382-395` | `detectStorageType()` greps `FileStore.name()` for `mmcblk` | Linux-only; silent no-op on Docker, macOS, Windows, NAS, network mounts. SD card on a non-Linux host is undetected. | SIGNIFICANT | Add Windows / macOS detection paths or pass `StorageType` via `PersistenceConfig`. Document in `Portability_Architecture_v1.md` §7.3 (already a `AdaptivePragmaConfig` placeholder). |
| D1-20 | `core/persistence/.../JacksonWarmup` | Cold-start cost from walking every registered event type and pre-populating `SerializerCache` + `DeserializerCache` | Pi 4: warmup cost 50–200 ms per LTD-19; tolerable. Enterprise with hundreds of energy event types: warmup may exceed 1 s. | INFO | None — measurable, not blocking. |
| D1-21 | `core/persistence/.../MigrationRunner` (referenced) | `;`-delimited SQL splitter; classpath-relative migration files; SHA-256 checksums | Case-sensitive filesystem assumption; classpath layout fixed. Docker layered images: OK. Windows containers: case-folding mismatch risk. | MINOR | Switch to `Files.lines(...).collect()` with explicit charset and `Locale.ROOT` checks. |
| D1-22 | `core/persistence/.../PersistenceConfig.java` | `HOME_DEFAULT = PersistenceConfig(DeploymentProfile.HOME, RetentionPolicy.SOURCE_DEFAULT)` | Type exists, but as documented in C-01, **it is not consumed**. Constructor accepts profile but lifecycle does not. | **BLOCKING** | See C-01. |

### Summary

The most consequential Dimension 1 finding is the C-01 drift: a profile system exists in `core/persistence` (`DeploymentProfile`, `PersistenceConfig`) but is bypassed in the only code path that applies PRAGMAs. The Constrained tier today runs **PERFORMANCE-ish** PRAGMAs. This invalidates the Architecture Invariants §0.5 constitutional rule for cross-tier deployment. Everything else in this dimension is parameterization detail.

---

## Dimension 2 — Interface Pluggability for Alternate Backends

### Per-interface verdict

| # | Interface | File | Verdict | Justification |
|---|---|---|---|---|
| D2-01 | `EventStore` | `core/event-model/src/main/java/com/homesynapse/event/EventStore.java` | **NEARLY PLUGGABLE** | 6 read methods, all use `long` positions. The contract for `latestPosition()` is "highest `globalPosition`" — does not require contiguous. Doc 04 / LTD-05 explicitly says "Subscribers must tolerate gaps in the global_position sequence." PostgreSQL `BIGSERIAL` (gaps on rollback) satisfies the contract. The Javadoc class-level mentions "schema upcasting" — purely a behavior obligation, not implementation. |
| D2-02 | `EventPublisher` (not opened in audit, but referenced) | `core/event-model` | **PLUGGABLE** | Two methods (`publish`, `publishRoot`), returns `EventEnvelope`. Single-writer is a property of the SQLite impl; the interface contract does not name it. |
| D2-03 | `CheckpointStore` (subscriber) | `core/event-bus/.../CheckpointStore.java` | **PLUGGABLE** | 2 methods, `long` position. "Atomic" qualifier on `writeCheckpoint` — PostgreSQL `INSERT ON CONFLICT DO UPDATE` satisfies. Returns 0 sentinel for unknown subscriber — language-neutral. |
| D2-04 | `ViewCheckpointStore` | `core/state-store/.../ViewCheckpointStore.java` | **PLUGGABLE** | 2 methods, opaque `byte[]` payload, `Optional<CheckpointRecord>` return. PostgreSQL `bytea` satisfies. |
| D2-05 | `PersistenceLifecycle` | `core/persistence/.../PersistenceLifecycle.java` | **NEARLY PLUGGABLE** | 4 methods. Javadoc embedded text says "Configures WAL mode and checkpoint thresholds" and "Opens SQLite database connections with required PRAGMA configuration (WAL mode, synchronous NORMAL, cache sizes per LTD-03)" — this is documentation drift that leaks implementation. The interface signatures (start/stop/createBackup/restoreFromBackup) are PostgreSQL-friendly: a `PostgresPersistenceLifecycle` could open a connection pool instead of a SQLite WAL. `BackupResult.eventsGlobalPosition()` is positional but compatible. `BackupOptions.preUpgrade()` is generic. |
| D2-06 | `WriteCoordinator` | `core/persistence/.../WriteCoordinator.java` | **COUPLED** | Declared `package-private interface WriteCoordinator`. The Javadoc says "In production, this wraps a single platform thread executor (AMD-26/AMD-27) — all sqlite-jdbc JNI calls route through this interface because JNI pins carrier threads on ALL Java versions." This is correct for SQLite but the type is unreachable from outside `com.homesynapse.persistence`. A PostgreSQL backend that uses JDBC connection pooling (no JNI) does NOT need a single-writer serializer — yet the entire persistence module is structured around `WriteCoordinator.submit(...)`. **To swap backends, you must reimplement inside the persistence module.** |
| D2-07 | `ReadExecutor` | `core/persistence/.../ReadExecutor.java` | **COUPLED** | Same reason as D2-06: package-private. Same constraint. |
| D2-08 | `AtomicCheckpointWriter` | `core/persistence/.../AtomicCheckpointWriter.java` | **COUPLED** | Package-private final class (not an interface). The 2-way / 3-way atomic write contract is implemented as a single SQLite transaction holding three INSERT-OR-REPLACE statements; PostgreSQL can satisfy the same contract using `BEGIN ... COMMIT`. **The contract is achievable** but the type is not an interface — there is no seam. Refactor required. |
| D2-09 | `WritePriority` | (package-private enum) | **COUPLED** | 5-value enum (`EVENT_PUBLISH(1)`, `STATE_PROJECTION(2)`, `WAL_CHECKPOINT(3)`, `RETENTION(4)`, `BACKUP(5)`). `WAL_CHECKPOINT` is a SQLite-specific operation. PostgreSQL has no WAL_CHECKPOINT in the same sense (its checkpointer is autonomous). For a PostgreSQL backend, `WAL_CHECKPOINT` is dead. |
| D2-10 | `DatabaseExecutor` | `core/persistence/.../DatabaseExecutor.java` | **COUPLED** (intentionally) | Final, package-private. Owns one SQLite file. Cannot serve as a base for non-file storage. |

### Implications

The two cleanly-pluggable layers are: **(a) the top-level service interfaces** (`EventStore`, `EventPublisher`, `CheckpointStore`, `ViewCheckpointStore`, `PersistenceLifecycle`) — these can be reimplemented in a *sibling* module (e.g., `core/persistence-postgres`); and **(b) the EventEnvelope / EventDraft data types** — fully transport-agnostic.

The *internal* layer (`WriteCoordinator`, `ReadExecutor`, `AtomicCheckpointWriter`, `DatabaseExecutor`) is **structurally locked to SQLite + JNI**. This is correct for the MVP — it isolates the JNI-carrier-pinning mitigation behind a tight module boundary — but it means cloud / PostgreSQL deployments cannot reuse the supervisor / priority queue / connection lifecycle; they must build their own. For Enterprise this is acceptable; for Enhanced (Docker, K8s with SQLite) it is the right choice; the *risk* is only if the SQLite-internal abstractions are mistaken for portable seams.

### Findings table

| # | Finding | Severity | Recommended Action |
|---|---|---|---|
| D2-11 | `PersistenceLifecycle` Javadoc mentions "WAL mode" and "PRAGMA configuration (per LTD-03)" inside the public interface text (lines 29-35, 49-51). | MINOR | Strip implementation references from the interface Javadoc; keep them in `SqlitePersistenceLifecycle` instead. |
| D2-12 | `WritePriority.WAL_CHECKPOINT` (rank 3) is SQLite-specific. A non-SQLite backend has no notion of WAL checkpoint at the priority level. | MINOR | Acceptable today (no Postgres backend). If `WritePriority` ever leaks to public API, generalise to `MAINTENANCE`. |
| D2-13 | `BackupResult.eventsGlobalPosition()` field name presumes the SQLite global position scheme. A cloud event store using partition offsets returns N/A. | MINOR | Document the field as "store-specific position marker (may be 0 for stores without a global position)". |
| D2-14 | `AtomicCheckpointWriter.writeAtomicCheckpointWithDlqPark` carries `DeadLetter` (event-bus type) into the persistence layer. The atomicity contract assumes a single backing transaction. | MINOR | Add a `TransactionalCheckpointWriter` interface in `core/persistence`, with the SQLite impl as the only producer for now. Sets up the seam for PostgreSQL. |

---

## Dimension 3 — Threading Model Under Different Hardware

### Topology

- **Subscribers:** one virtual thread per subscriber (`Thread.ofVirtual().name("hs-sub-<id>").start(...)`, `InProcessEventBus.java:279`).
- **SQLite writer:** one daemon platform thread `hs-write-0` servicing a `PriorityBlockingQueue` (`PlatformThreadWriteCoordinator.java:60`).
- **SQLite readers:** N daemon platform threads `hs-read-0..N-1`, default N=2 (`PlatformThreadReadExecutor.java:67`, `SqlitePersistenceLifecycle` ctor parameter `readThreadCount`).
- **Per-subscriber dedicated read executor:** in production (`SubscriberReadConnectionFactory.create()` returns `SubscriberReadExecutor`). In M3.4a's `IntegrationTestHarness`, the factory is replaced with a synchronous-on-VT recording stub.
- **Refill scheduler for `DerivedWriteRateLimit`:** "production wiring will use a shared `ScheduledExecutorService`" — **not wired yet** (no `refill()` caller other than tests). This is a M3.6 lifecycle gap, not a portability gap.

### Per-tier analysis

| # | Tier | Worry | Severity | Recommendation |
|---|---|---|---|---|
| D3-01 | Constrained (Pi 4, 4 carriers) | 4 carriers must service: 1 writer thread (always parked on queue.take), 2 read threads (parked on queue.poll), 20+ subscriber VTs (parked on LockSupport or queue.poll). The platform threads are not carriers — they are dedicated. The 4 carriers serve only the virtual-thread pool. As long as no VT does `synchronized` or JNI, carrier exhaustion is impossible by design. Verified: Jackson cache pre-warmed (LTD-19), all locks are `ReentrantLock` (LTD-11), all SQLite calls via platform-thread executors (AMD-26). | INFO | None — design is sound. |
| D3-02 | x86 server (64 cores, 64 carriers) | Default `readThreadCount=2` (`SqlitePersistenceLifecycle` ctor default), `hs-write-0` is single by design. Only 3 platform DB threads on a 64-core box → all serialized contention on these 3 threads, 61 idle cores. WAL allows up to 8+ concurrent readers; tuned configurations would set N=4 or 8. | SIGNIFICANT | Default `readThreadCount` from `DeploymentProfile`: STUDIO=2, HOME=2, PERFORMANCE=4, ENTERPRISE=8. Hard cap at 8 per LTD-03 reader-budget guidance. |
| D3-03 | x86 server priority ordering | `PriorityBlockingQueue<WorkItem>` ordered by `WritePriority.rank()`+`AtomicLong` FIFO tiebreaker. With higher publish throughput on the server, lower-priority work (RETENTION, BACKUP) could starve indefinitely. The current code does not implement priority aging. | MINOR | Document as accepted — design intent per AMD-32 (priority-by-rank wins). Aging would be a separate AMD. |
| D3-04 | Docker container with CPU limits (e.g., 2 CPUs) | `Runtime.availableProcessors()` and `ForkJoinPool.commonPool()` parallelism are auto-detected by HotSpot from cgroup `cpu.cfs_quota_us` (Java 10+). Virtual thread carrier pool uses `Runtime.availableProcessors()` by default. **No explicit `-XX:ActiveProcessorCount` in production** (only in `testing/integration-tests/build.gradle.kts:28` for Pi 4 simulation). Should work automatically. | INFO | None — implicit behavior is correct. |
| D3-05 | Multiple HS instances on one host | Thread names `hs-write-0`, `hs-read-N` collide across processes. JFR/JMC analysis cannot disambiguate. | MINOR | Prefix with PID or HomeId fragment: `hs-${pid}-write-0`. |
| D3-06 | GraalVM Native Image (future) | **(a) Jackson:** uses reflection extensively for the typed-ULID serde and `EventPayloadCodec`. Requires `reflect-config.json`. `JacksonWarmup` pre-populates Jackson's caches but does NOT publish reflection config to native-image. **(b) `jdk.jfr`:** supported in native-image since GraalVM 21+ but with limitations (no `RecordingStream` host-streaming until 24+). The bus's `BusMetricsJfr` uses `jdk.jfr.Event` subclasses — must be registered. **(c) `Thread.ofVirtual()`:** supported in native-image 22+. (Java 21 native-image lacked it.) **(d) sqlite-jdbc native lib:** must be set as a native library in the image. | SIGNIFICANT | Native-image is not on the M3 roadmap; document as out-of-scope, add `reflect-config.json` skeleton for future work in `core/persistence/src/main/resources/META-INF/native-image/`. |
| D3-07 | Android (Companion tier) | No ART support for `Thread.ofVirtual()`, no JFR, no `jdk.jfr` module. Per Portability Architecture v1 §3.5 the Companion **does not run Core** — Companion is a REST/WS client. So this dimension is moot for Companion. | INFO | None. |
| D3-08 | Refill scheduler not wired | `DerivedWriteRateLimit.refill()` is supposed to be called every 50 ms from a shared `ScheduledExecutorService` — no such scheduler exists in production code. Today, `DerivedWriteRateLimit` never refills outside tests. | SIGNIFICANT (M3.6 gap, not tier-specific) | Owned by M3.6 lifecycle composition root WU. Not a cross-tier concern per se, but a deployment-readiness one. |

---

## Dimension 4 — Memory Model Across the Spectrum

### Per-component sizing

| # | Component | At Constrained (50 entities, 4 GB / 256 MB heap) | At Enterprise (10,000 entities, 32+ GB / 12 GB heap) | Severity |
|---|---|---|---|---|
| D4-01 | `SqliteStateStore` ConcurrentHashMap | 50 × ~500 B = ~25 KB | 10,000 × ~2 KB (with attributes) = ~20 MB | INFO |
| D4-02 | `SelfProducedFilter` HashMap (per projection) | 200 pubs/s × 60s × ~80 B = ~1 MB max | Same per-projection — single projection so bounded by the publish rate not entity count | INFO |
| D4-03 | `ReplayWindowQueue` (per subscriber) | 10,000 × 16 B = ~160 KB | Same (bounded by `MAX_CAPACITY`) — but overflow→REPLAY restart loops if Enhanced/Enterprise ingest spikes exceed 10K | SIGNIFICANT (see D1-07) |
| D4-04 | `SubscriberDlq` ring (per subscriber, ~ 1024 entries × ~200 B) | 200 KB × 20 = 4 MB | 200 KB × 100 (Enterprise multi-integration) = 20 MB | INFO |
| D4-05 | Jackson `ObjectMapper` cache | post-warmup ~5–10 MB for 27 event types | grows with type count: ENTERPRISE may add 50+ energy event types → ~15–25 MB | INFO |
| D4-06 | SQLite WAL mmap (`PRAGMA mmap_size`) | **Hardcoded 1 GiB today (D1-01).** On 4 GB Pi this is most of RAM — swap-thrash hazard. | 1 GiB OK | **BLOCKING** (subsumed by C-01) |
| D4-07 | SQLite page cache (`PRAGMA cache_size`) | **Hardcoded 128 MiB today (D1-01).** On 4 GB Pi 4 with `-Xmx1536m`, JVM (1.5 GiB) + cache (128 MiB) + mmap (1 GiB) ≈ 2.65 GiB before any working set. Tight. | 128 MiB OK | **BLOCKING** (subsumed by C-01) |
| D4-08 | `StateProjection` checkpoint blob | At 50 entities, ~few KB. | At 10K entities × ~100 B = ~1.5 MB, ENTERPRISE may approach `CHECKPOINT_SIZE_WARN_BYTES = 10 MB`. Advisory WARN only. | MINOR |
| D4-09 | `ReplayWindowQueue` overflow loop | Constrained: rare (60 events/min nominal). | Enterprise: at 1000 events/s ingest during projection cold-start, 10K queue fills in 10 s. REPLAY restart loop ensues until cursor catches up. | SIGNIFICANT |

### Verdict

If C-01 is fixed (DeploymentProfile is wired), **memory budgets are well-bounded** at every tier. The most worrisome dynamic is D4-09: a long REPLAY restart loop on a heavily-loaded Enhanced/Enterprise system. The `ReplayDriver` does recover (it restarts from the persisted checkpoint), but a sustained loop would not produce LIVE delivery. Mitigation: lift `MAX_CAPACITY` per profile.

---

## Dimension 5 — Operational Resilience Across Environments

| # | Concern | Finding | Severity | Recommended Action |
|---|---|---|---|---|
| D5-01 | SD card 200 ms fsync spikes (Pi4D1 SpikeIT scenario) | `synchronous = NORMAL` + WAL means fsync only on `wal_checkpoint`, not per transaction. WAL checkpointing is scheduled (`MaintenanceSubscriber`, 6-hour default). A 200 ms spike during checkpoint blocks the writer thread; reads on the read pool are unaffected. **Acceptable.** | INFO | None — design is robust. |
| D5-02 | SD card endurance (A1 card: 500 IOPS sustained) | Event store writes are batched per WAL page. At 100 events/sec sustained, ~1 IOP/sec WAL flush + checkpoint every 6 hr. Within budget. However, **LTD-02 explicitly states "SD card storage is not supported for production"**, and `SqlitePersistenceLifecycle.detectStorageType()` emits a WARN but does not refuse. | INFO | Keep WARN-only per INV-CE-02. Audit confirms no surprise. |
| D5-03 | Power loss during WAL checkpoint | `journal_mode=WAL` + `synchronous=NORMAL` guarantees recovery to the last fsync — data loss limited to the most recent WAL frames. Crash-recovery is exercised in tests. **OK for all tiers.** | INFO | None. |
| D5-04 | Docker volume mounts (bind, NFS, distributed FS) | SQLite WAL uses `*-shm` shared-memory file plus `*-wal`. Bind mounts on `overlay2` / `virtiofs` (Docker Desktop macOS/Windows) do **not** support SQLite WAL-shm correctly — must use `locking_mode=EXCLUSIVE` (LTD-03 column in Portability Architecture v1 §2.1). Current code never sets it. NFS without proper locking is unsafe. | SIGNIFICANT | Add a `lockingMode` field to `DeploymentProfile`; Docker-Desktop image bakes `EXCLUSIVE`. Document in README per LTD-03 reversal-criteria pattern. |
| D5-05 | Clock skew on ingested external events | All code uses injected `Clock` (NO_DIRECT_TIME_ACCESS ArchUnit rule). `event_time` from external sources may be skewed but does not affect `globalPosition` ordering (which uses `ingest_time`). | INFO | None. |
| D5-06 | Timezone / locale | Spot check on `SqlitePersistenceLifecycle` — found `Locale` import at line 17, used in `detectStorageType` (`String.toLowerCase(Locale.ROOT)` pattern is standard but unverified). All timestamps stored as microsecond `long` (`TimeConversion`). Locale-free. | INFO | None. |
| D5-07 | File descriptor limits | 1 write conn + N read conns (default 2) + per-subscriber dedicated read connections (M3.6 plan). At 20 subscribers + 3 default = ~23 FDs. Linux default `ulimit -n 1024` — ample headroom. Docker default ~65536 — even more. | INFO | None. |
| D5-08 | Linux-only SD detection (D1-19) | macOS/Windows/Docker Desktop: no SD detection. | SIGNIFICANT | See D1-19. |
| D5-09 | Backup / restore not implemented | `SqlitePersistenceLifecycle.createBackup()` throws `UnsupportedOperationException` (M3.5b state). | SIGNIFICANT (deployment readiness) | Post-M3 scope per the lifecycle module. Document. |

---

## Dimension 6 — API Contract Portability

| # | Concern | Finding | Severity | Recommended Action |
|---|---|---|---|---|
| D6-01 | REST/WS API independent of backend | REST API and WS API modules not yet read (they are in `api/` per repo layout but out of M3.4a scope). Doc 09 / Doc 10 in `homesynapse-core-docs/`. Per Portability Architecture v1 §6.2 the cloud sync subscriber pattern uses exactly the existing `EventBus` + `EventStore` interfaces — no core changes. **API contracts are designed to be backend-independent.** | INFO | None. |
| D6-02 | EventEnvelope / EventDraft transport-agnostic | `EventEnvelope` has 14 fields, all primitives or ULID. Jackson serialization is the only path today. `EventTypeRegistry` uses logical type strings (e.g., `"state_changed"`) — language-neutral. Cloud-scalability analysis §1.3 confirms this is replication-friendly. | INFO | None. |
| D6-03 | `globalPosition` contract | `EventStore.latestPosition()` and `EventStore.readFrom(afterPosition, maxCount)` use `long`. LTD-05 explicitly says "Subscribers must tolerate gaps in the `global_position` sequence (caused by rolled-back transactions)." PostgreSQL `BIGSERIAL` (gaps on rollback) satisfies. **Contract is monotonic, not contiguous.** | INFO | None — already correct. |
| D6-04 | WebSocket push relay memory bound | WS relay not yet implemented (designed in Doc 10). For a Companion app receiving real-time state, the relay is a `Subscriber` registered with the local bus — bounded by `pendingPositions` queue per subscriber (unbounded in the current Java `ConcurrentLinkedQueue` implementation, but rate-limited upstream by the WAL write rate). | MINOR | When WS relay lands (post-M3.6), bound the per-client outbound queue to prevent slow clients from inflating heap. |
| D6-05 | No `HubId` / `InstanceId` on `EventEnvelope` | Per cloud-scalability analysis §2.1: SQLite has `home_id BLOB(16) NOT NULL` column (AMD-34) but the **`EventEnvelope` Java record does not expose `homeId` as a top-level field**. A cloud aggregator receiving events from multiple hubs cannot identify the originating hub from the envelope alone. **MEDIUM risk** when multi-hub sync ships, not for MVP. | SIGNIFICANT (future) | Per the cloud-scalability analysis recommendation: add nullable `originHub: HomeId` field to `EventEnvelope` in a V005 migration when multi-hub ships. The `chain_hash` column was added proactively for this reason; `origin_hub` is the same pattern. |
| D6-06 | Companion does not run Core | Confirmed — Portability Architecture v1 §3. Companion is a REST/WS client. The persistence, event-bus, state-store modules are not loaded. The shared modules (`event-types`, `device-types`, `serialization`, `api-client`) form the Companion footprint. | INFO | None — architecturally clean. |
| D6-07 | API versioning | LTD-16: URL-versioned REST, semver. Companion app reads against `/v1/...`. Compatible with any backend. | INFO | None. |

---

## Findings rollup by severity

| Severity | Count | Files affected |
|---|---|---|
| BLOCKING | 1 (C-01, subsumes D1-01, D1-22, D4-06, D4-07) | `DatabaseExecutor.java`, `DeploymentProfile.java`, `PersistenceConfig.java`, `SqlitePersistenceLifecycle.java` |
| SIGNIFICANT | 9 (D1-04, D1-05, D1-07, D1-13, D1-19, D3-02, D3-06, D3-08, D4-09, D5-04, D5-08, D5-09, D6-05) | 7 files in `core/persistence`, `core/event-bus`, `core/state-store` |
| MINOR | 11 | scattered |
| INFO | 18 | n/a |

---

## Summary Verdict

**NEARLY READY** — significant findings that require targeted work.

The architecture is structurally sound: the cross-tier scaffolding (DeploymentProfile, ProfileConfig, RetentionPolicy, abstract EventStore/CheckpointStore/ViewCheckpointStore, NoRealIoExtension, ArchUnit module-boundary rules) exists and is correctly designed. The cloud-scalability research and Portability Architecture v1 demonstrate that the team has reasoned carefully about multi-tier deployment.

But **one BLOCKING defect (C-01)** prevents Constrained-tier deployment from satisfying its base specification today: `DatabaseExecutor` ignores `DeploymentProfile` and applies a 128 MiB cache + 1 GiB mmap on every deployment, including a 4 GB Pi 4. The Architecture Invariants §0.5 constitutional rule — "every invariant must hold at the Constrained tier at its base specification" — is currently violated for INV-PR-01 (constrained hardware) and INV-PR-03 (bounded resources).

The other significant findings are localized: tier-specific defaults that need to be parameterized (read-thread count, `MAX_CAPACITY` of replay window, `busy_timeout`, `locking_mode` for Docker Desktop), and a deployment-readiness gap (no refill scheduler wired for `DerivedWriteRateLimit`; backup unimplemented).

**Quantification:** Closing C-01 plus the 9 SIGNIFICANT findings is approximately **8–12 files, 16–24 engineering hours**, plus contract-test additions for each profile. All blocking changes are confined to `core/persistence` and `core/event-bus`. No public API changes are required. No design-doc amendments are required (the design is correct; the wiring is incomplete).

---

## Top 5 Highest-Impact Changes

1. **Wire `DeploymentProfile` into `DatabaseExecutor`** — *resolves C-01, the only BLOCKING finding*.
   - **File:** `core/persistence/src/main/java/com/homesynapse/persistence/DatabaseExecutor.java`
   - **Change:** Accept `DeploymentProfile` (or `PersistenceConfig`) in the constructor. Replace the hardcoded `CONNECTION_PRAGMAS` `List.of(...)` (lines 68–76) with a method that consults `profile.cacheSizeKiB()`, `profile.mmapSizeBytes()`, `profile.journalSizeLimitBytes()`. Add `lockingMode` and `busyTimeout` to `DeploymentProfile` for D5-04 (Docker Desktop) and D1-05 (NAS).
   - **Companion file:** `core/persistence/src/main/java/com/homesynapse/persistence/SqlitePersistenceLifecycle.java` — accept `PersistenceConfig` in ctor; pass to `DatabaseExecutor`. M3.6 lifecycle composition root reads from YAML.
   - **Unlocks:** Constrained-tier compliance with INV-PR-01 and INV-PR-03. Standard / Enhanced / Enterprise deployments now have tier-appropriate PRAGMAs. Docker-Desktop deployments become safe.

2. **Default `readThreadCount` from `DeploymentProfile`** — *unblocks Enhanced + Enterprise throughput on x86 servers*.
   - **File:** `core/persistence/src/main/java/com/homesynapse/persistence/SqlitePersistenceLifecycle.java` (lines 120–136)
   - **Change:** Replace the constructor parameter default of 2 with a `profile`-derived value (STUDIO=2, HOME=2, PERFORMANCE=4, future ENTERPRISE=8). Hard-cap at 8 per LTD-03 reader-budget guidance.
   - **Unlocks:** D3-02 (64-core server no longer leaves 61 cores idle). Throughput on Enhanced tier scales linearly with reader pool until WAL contention saturates.

3. **Promote `ReplayWindowQueue.MAX_CAPACITY` to a profile-driven constructor parameter** — *closes D4-09 / D1-07 for high-throughput tiers*.
   - **File:** `core/event-bus/src/main/java/com/homesynapse/event/bus/ReplayWindowQueue.java` (line 44)
   - **Change:** Accept `maxCapacity` in constructor; default to 10_000 for Constrained, scale to 100_000 for Enterprise. Pass through from `InProcessEventBus.subscribeRuntime`.
   - **Unlocks:** Enhanced/Enterprise tiers can absorb large ingest bursts during catch-up REPLAY without entering an overflow-restart loop.

4. **Wire `DerivedWriteRateLimit.refill()` scheduler in the lifecycle composition root** — *closes D3-08; not strictly cross-tier but is a deployment-readiness blocker per AMD-43*.
   - **File:** Will be in the future M3.6 lifecycle module (currently in design). Add a `ScheduledExecutorService` shared with `QueueSaturationHealthCheck.tick()`. Both have a 50–1000 ms cadence and can share a single 1-thread scheduler.
   - **Unlocks:** Production backpressure semantics. Without it, the rate limiter never refills outside tests, and StateProjection's derived-publish rate is unbounded.

5. **Generalize storage-type detection beyond Linux `mmcblk`** — *closes D1-19 / D5-08 for Docker, macOS, Windows, NAS*.
   - **File:** `core/persistence/src/main/java/com/homesynapse/persistence/SqlitePersistenceLifecycle.java` (lines 382–395)
   - **Change:** Either (a) extend `detectStorageType` with platform-specific probes (Windows volume APIs, macOS `diskutil`, Docker `mountinfo` walk), or (b) accept `StorageType` as a `PersistenceConfig` field driven from YAML and skip detection entirely. The Portability Architecture v1 §7.3 `AdaptivePragmaConfig` placeholder envisions option (b).
   - **Unlocks:** Operators on every host platform get a clear warning when storage is unsuitable. Combined with #1, lets Docker Desktop deployments select `lockingMode=EXCLUSIVE` automatically when bind-mounted volumes are detected.

---

## What this audit did NOT cover

Per the brief's "What This Audit Is NOT" clause:

- No code review, style, or Javadoc feedback.
- No M3 design-decision review (AMD-26/27/38/41/42/43 are LOCKED and respected).
- No feature-addition list.
- No performance benchmarks.

The audit is intentionally narrow: **can the existing code, without modification, run correctly across the full deployment spectrum?** The answer is *almost*. One BLOCKING wiring defect (C-01) and nine localized SIGNIFICANT parameterization findings stand between the current code and that goal. None of them require architectural change.
