<!--
file: _scratch/v106/b4/AVAIL-API-1_independent-review_v1.md
purpose: REVIEW-AA1 — the one-way-door review of the AVAIL-API-1 coding instruction (DRAFT v1), by an agent that has not seen the drafting; the nine questions of the brief graded; the findings on bytes at core 9cf0ed9; the edits as exact OLD → NEW pairs for the hub's script.
reviewer: REVIEW-AA1 (read-only on every repository; one write — this file)
status: FILED 2026-10-11 17:16Z (started 17:04:07Z by `date -u`; core `9cf0ed9` confirmed by `git --no-optional-locks log -1 --oneline`; docs `e2a5844`)
under review: _scratch/v106/b4/AVAIL-API-1_instruction_v1.md — 48,069 B, md5 f1f08c970c45dae39763d8577cb2aa58 (verified)
brief: _scratch/v106/b4/AVAIL-API-1_review-brief_v1.md — 5,535 B, md5 dd09a44d2dc2d44b63c6e5c000bf5c21 (verified)
-->
# AVAIL-API-1 — the independent one-way-door review (v1 of the instruction)

## §0 The verdict

**READY-WITH-EDITS.** Twenty edits (§3), all script-applicable; two findings are BLOCKING and both are closed by the edits — neither needs a redesign, each needs the instruction to stop pointing the lane at a door that does not exist (F-1) or at a door that must not be opened (F-2).

- **F-1 (BLOCKING, Q4):** the monotonic source's ruled home — a `default` accessor on the integration context, overridden by the composition root — cannot be written: `IntegrationContext` is a frozen 12-component RECORD (`IntegrationContext.java:103`; `ZigbeeIntegrationFactory.java:38`). The `Clock` already reaches the tracker by a seam the draft does not use: `Main.java:114` → the Zigbee factory → the adapter → `T/:261`. The `LongSupplier` rides it; `Main` is whitelisted; no `platform` type, no `integration-api` edit, no `module-info` edit.
- **F-2 (BLOCKING, Q5 · Q9):** the draft lets the lane add a table and a migration for the projection's durable view. `MigrationRunner.java:326`–`:329` fails the boot of any build behind the store's schema — a T-B migration makes T-B irreversible, which §1 promises it is not. The coupled form the draft asks the lane to find EXISTS and needs no table: `PersistenceFactory.atomicCheckpointSink()` (`:213`–`:217`) over `subscriber_checkpoints` + `view_checkpoints` under one key, read back by `ViewCheckpointStore.readLatestCheckpoint`. The edits name it, name the runtime write the bus leaves to an `atomicCheckpoint = true` subscriber, and forbid a migration.
- Eight NON-BLOCKING findings: the sweep and the deadline live in `A/` (`:161`, `:176`), not `T/`, and `state-store` cannot read them (F-3); E-3 (f) is a non-proof on a `ReentrantLock` (F-4); §4.4 should model the older build's 58-class registry and must not claim a boot proof it does not give (F-5); "`at`'s nanos" (F-6); the interview site exists and has an ordering the lane will trip on (F-7); the counters must key on PING_SUCCESS and on `:375` only (F-8); row 9 unfilled (F-9); BC10's T-A evidence line is printed by nothing (F-10).
- **The schema door (Q1) is as narrow as the amendment says:** the two records are R-A/R-B/R-C's payloads; the priority is the draft's `EventDraft.priority` written to the row (`SqliteEventStore.java:504`) — no second mechanism; an older registry decodes the rows as `DegradedEvent` (`EventPayloadCodec.java:40`–`:44`) and the state projection ignores a DEVICE subject (`StateProjection.java:1152`–`:1157`).
- **All 28 premise rows hold at `9cf0ed9`** (§4). The wire (Q7) is exactly FIELDS §3's PROPOSED rows + Q10's two − `probeLink`.

After the edits: DISPATCH-READY on Nick's word. What the review did NOT reach: §5.

## §1 The nine questions, graded

| Q | Grade | The short answer (the bytes in §2) |
|---|---|---|
| 1 The schema door | **PASS with F-5** | The two records are R-A/R-B/R-C's payloads field for field; DEVICE-subject (`SubjectRef.device`, `SubjectRef.java:67`); `device_health`; the priorities R-A's. "Elevated at production" IS how `EventDraft` works at `9cf0ed9`: `EventDraft.priority` (`EventDraft.java:71`) is the value written to the row (`SqliteEventStore.java:504`) and read back (`:854`) — no second flag exists or is needed. The rollback test proves the DECODE (`EventPayloadCodec.java:38`–`:44`: an unknown type → `DegradedEvent`) and the state projection's silence; it does not prove a BOOT of `409547c` — §4.4's last sentence over-claims (F-5). |
| 2 The lock and the window | **PASS with F-4, F-6, F-8** | §4.2 keeps R-B's rule and matches `transition()`'s form (`T/:575` lock, `:613` unlock, `:618` sink). `windowStart = at − (monotonic now − window start)` is right at the opening record (start = construction) and after a wall step (`at − windowStart` is the monotonic length by construction — R-B's own words). A flicker is never a record: the decision is taken only on a PING_SUCCESS and only by (i)/(ii). The counters cannot double-count if the answer is counted on the PING_SUCCESS reason only (a frame also enters `transition()` with `available = true`, `:361` vs the ingestion seam) and the miss at `:375` only (the dark transition at `:379` re-enters `transition()`); the draft does not say either — F-8. E-3 (f) is a non-proof on a `ReentrantLock` — F-4. |
| 3 The contract | **PASS with F-7** | §4.3's arms are the tracker's: `isMainsPowered` (`:550`, 0x01/0x02), `mainsSilenceLimitFor` (`:515`–`:518`, max + `MAINS_PING_SILENCE` `:95`), `silenceLimitFor` (`:504`–`:507`, declared else `BATTERY_OFFLINE_SILENCE` `:117`); the lookups `A/:872` and `:897`; the per-cycle catch `:530`–`:536`. The four moments are R-C's. "Change" is detected by comparing the derived tuple with the last declared one in `DeviceState` at each evaluation — no publish storm (one row per change). The interview hook EXISTS: `adoptIfAccepted` `A/:1493`, COMPLETE-gated at `:1502`; the draft leaves it to the lane; F-7 names it and the `driveReporting` `:1523` ordering. |
| 4 The monotonic source | **FAIL as drafted — F-1 (BLOCKING)** | `System.nanoTime` is banned outside `com.homesynapse.{app,platform,test}..` (`HomeSynapseArchRules.java:101`–`:108`; 0 production calls). But §3's home is unwritable: `IntegrationContext` is a RECORD (`IntegrationContext.java:103`) frozen at 12 components (`ZigbeeIntegrationFactory.java:38`); a record has no `default` accessor; a new component reaches `integration-runtime` (`StandardIntegrationSupervisor.java:1098`) and 16 test/fixture constructors. No existing monotonic source exists in `platform` or `integration-api` (only the ULID's monotonicity). The seam that already exists is the `Clock`'s: `Main.java:114` → `ZigbeeIntegrationFactory(…, Clock)` `:84`/`:94` → `new ZigbeeIntegrationAdapter(` `:167`/`:170` → the tracker `:261`. `Main` is whitelisted. No `platform` type, no `integration-api` edit, no `module-info` edit. |
| 5 Path (b) and the coupled view | **FAIL as drafted — F-2 (BLOCKING)** | §4.5 reproduces REGISTRY-COLD-1's four steps (`HomeSynapseCore.java:632`–`:643`; `rebuildFromIndex` `RegistryProjectionSubscriber.java:138`, the per-type cursors `:144`–`:147`, the peek-merge `:150`–`:160`, the page walk `:250`). The "durable and coupled" view HAS an API at `9cf0ed9` the draft does not name: `PersistenceFactory.atomicCheckpointSink()` (`:213`–`:217`) → `AtomicCheckpointSink.writeAtomicCheckpoint(key, position, viewData)` (one transaction over `subscriber_checkpoints` + `view_checkpoints`, key = subscriber id = view name) and `ViewCheckpointStore.readLatestCheckpoint(viewName)` (`:73`). No table and no migration is needed — and a migration would make T-B irreversible (`MigrationRunner.java:326`–`:329`). The merge: `global_position` is unique and AUTOINCREMENT (one writer), the cursors peek-and-take the minimum, cut at H — no loss, no double (the registry's proof carries). Entity → device: `EntityRegistry` is `com.homesynapse.device` (`EntityRegistry.java:32`), which `state-store` already requires transitively (`module-info` `:12`) — no new edge; `ListEntitiesEndpoint:200`–`:203` is the read to mirror. |
| 6 R-G at read | **PASS with F-3** | §4.6's arithmetic is R-G's (asked: record + limit + misses × 5 × N + sweep; passive: limit + sweep), the 5 s and the serial-N reading are `T/:83`–`:85`'s. N is the projection's count over its view, never a page's — stated. The null rules are AMD-103 §3's tri-state law (not LIVE → null; no contract → the bound not computed). The sweep is NOT a constant in `T/`: it is the 50-ms run cycle `A/:161` and the deadline `A/:176`, both package-private in a module `state-store` cannot require — F-3. |
| 7 The wire | **PASS** | The eleven keys = FIELDS §3's PROPOSED rows (`FIELDS.md:27`–`:35`: `probeAnsweredAt`, `probeWindowStart`, `probesAnswered`, `probesMissed`, `availabilityClass`, `reportIntervalSeconds`, `silenceLimitSeconds`, `missesToDark`, `recordIntervalSeconds`) + Q10's `recordDueBy`, `recordOverdueSince` (`HERO-U2c_intake-audit.md:28`) − `probeLink` (`:30`, off by Q12). Additive under `:260` of the freeze doc (verified: "Additive, backward-compatible fields are low-friction"). `meta.recoveryViewPosition` follows `viewPositionSupplier` (`DlqStatusEndpoint.java:102`). V-6's golden test pins the existing order; `EntityStateJson.java:60`–`:68` and `ListEntitiesEndpoint.java:193`–`:195` are the keys it must not move. |
| 8 Premises and scope | **PASS with F-9** | §0b re-run: rows 1–28 all hold (§4). Not named and should be: the interview site (F-7); the sweep/deadline lines (F-3); the `Main`/factory seam (F-1); an `app/homesynapse-app` MODULE_CONTEXT row (F-1); row 9's lock count (F-9). R-E's un-tabled pins are delegated to a grep in row 4 — acceptable. The T-A/T-B split is clean: T-A's `check` needs no T-B byte (the types, the tracker, the adapter, the factory/`Main` seam, the rollback IT are closed under T-A); T-B is revertible alone ONLY with F-2 applied. |
| 9 The door | **PASS with F-2, F-5, F-10** | T-A's rows under a rollback: decoded as `DegradedEvent` by any older registry (`EventPayloadCodec.java:40`–`:44`), ignored by the state projection (`StateProjection.java:1152`–`:1157`), walked harmlessly by the older registry rebuild — reversible. T-B under a rollback: two orphan rows keyed `recovery-card-projection` in `subscriber_checkpoints`/`view_checkpoints`, read by no older build — reversible; a MIGRATION would not be (F-2). BC10's evidence lines: T-B's replay line is printed by §4.5 (2)'s log; T-A's "first two rows in the store" is a store READ, printed by nothing in the draft — F-10 adds the two INFO lines. |

## §2 Findings (numbered; honest severity; each on bytes at `9cf0ed9`)

**F-1 [BLOCKING] — the monotonic source's home is unwritable as ruled; the seam that exists is the `Clock`'s.** §3's T-A row and §5, §8, §9 (1) put a `MonotonicSource` in `platform/platform-api` and "a `default MonotonicSource monotonicSource()` on the integration context that the composition root overrides". `IntegrationContext` is `public record IntegrationContext(` (`integration/integration-api/src/main/java/com/homesynapse/integration/IntegrationContext.java:103`) with twelve components (`:104`–`:115`) and a ten-argument convenience constructor (`:155`–`:168`); `ZigbeeIntegrationFactory.java:36`–`:39` calls it "the frozen 12-component context carries no clock" and names the M9.3 R4 seam as the way the clock reaches the adapter. A record cannot carry an overridable `default`; a thirteenth component changes `new IntegrationContext(` at `StandardIntegrationSupervisor.java:1098` (`integration-runtime`, a module §3 does not name) plus `StubIntegrationContext` (testFixtures) and 15 test sites. The existing seam: `Main.java:114`–`:116` (`new ZigbeeIntegrationFactory(…, zigbeeDataDir, clock)`), the factory's constructors `:84`, `:94`, its `new ZigbeeIntegrationAdapter(` at `:167`/`:170`, the adapter's constructors `:355`/`:374`/`:386` (`Clock clock`), the tracker's construction `:470`. `Main` is in `com.homesynapse.app`, whitelisted by the rule (`HomeSynapseArchRules.java:101`); it passes `System::nanoTime` as the `LongSupplier`. No `platform` type, no `integration-api` edit, no `module-info` edit, no `exports` line (`platform`'s `module-info` exports only `com.homesynapse.platform` and `.identity`, `:2`–`:3` — the draft's new package `com.homesynapse.platform.time` would have needed one, contradicting §5's "no change"). Edits 1–5.

**F-2 [BLOCKING] — T-B's view store: the draft permits a migration that would make T-B irreversible; the coupled API already exists and needs no table.** §3's T-B `P/` row allows "a table + the coupled write … with the migration file if one is needed (`PR/V0xx__recovery_card_view.sql`)" and §9 (8) repeats it. `MigrationRunner.java:324`–`:329`: `if (maxTracked > maxParsed) throw new MigrationException("Database schema version %d is ahead of application …")` — a store carrying V006 cannot boot T-A's build or `409547c`'s; §1's "T-B can be reverted alone" would be false. The API: `PersistenceFactory.atomicCheckpointSink()` (`core/persistence/src/main/java/com/homesynapse/persistence/PersistenceFactory.java:213`–`:217`) returns `(key, position, viewData) -> writer.writeAtomicCheckpoint(key, position, key, viewData)`; `AtomicCheckpointSink.writeAtomicCheckpoint` (`core/state-store/src/main/java/com/homesynapse/state/AtomicCheckpointSink.java:50`–`:67`: "writes both the subscriber position and the view snapshot in one SQLite transaction … The `checkpointKey` is used as both the subscriber id (`subscriber_checkpoints`) and the view name (`view_checkpoints`)"); `ViewCheckpointStore.readLatestCheckpoint(viewName)` (`ViewCheckpointStore.java:73`). With `SubscriberInfo.atomicCheckpoint = true` (the four-argument form at `HomeSynapseCore.java:676`–`:680`) the bus writes no subscriber checkpoint of its own (`InProcessEventBus.java:651`; `ReplayDriver.java:170`, `:209`) — the projection must write the coupled checkpoint itself at runtime; the draft names no runtime policy. Edits 6–10 rule the API, the runtime write (after every applied row; the volume is R-B's), the boot-time restore that skips the catch-up (V-7), and forbid a migration.

**F-3 [NON-BLOCKING] — the sweep "constant in `T/`" is not in `T/` and is not reachable from `state-store`.** §4.6 and §9 (10) send the lane to `T/` for the sweep period. The sweep is the run cycle `ZigbeeIntegrationAdapter.PRODUCTION_CYCLE_MILLIS = 50` (`A/:161`), applied at `runCycleOnce()` `:669`–`:680` (`evaluateAvailabilityTimeouts()` `:676`); the deadline is `AVAILABILITY_PING_TIMEOUT_MILLIS = 5_000` (`A/:176`); the tracker's Javadoc `:83`–`:85` quotes both as "60 + 2·5·N + 0.05 s". Both are package-private statics in `integration-zigbee`; `core/state-store`'s `module-info` (`:10`–`:18`) requires `platform`, `value`, `device`, `event`, `event.bus` — never an integration, and must not. `StaleRecordBound` carries its own cited copies. Edits 11–12.

**F-4 [NON-BLOCKING] — E-3 (f) is a non-proof.** The tracker's lock is `private final ReentrantLock lock = new ReentrantLock();` (`T/:230`). A listener that "calls back into the tracker (a read)" on the same thread re-enters whether or not the lock is held; the test would pass against a listener called under the lock. The proof needs a second thread with a bound. Edit 13.

**F-5 [NON-BLOCKING] — §4.4's registry and its claim.** The production registry is `new EventTypeRegistry(eventClasses)` (`SqlitePersistenceLifecycle.java:312`) over the FULL list (58: `AllEventClasses.ALL_EVENTS`, as `EventPayloadCodecTest.java:54` builds it), not the 43-class manifest; the Degraded result is the same, but the test should model the older build's registry, not its manifest. Both constructors are package-private (`EventTypeRegistry.java:73`, `EventPayloadCodec.java:94`) — reachable from a test in `com.homesynapse.persistence`, where the draft puts `ProbeRecordRollbackIT`. And "This is the proof that `409547c`'s build boots" over-claims: the test exercises the codec and one all-types subscriber; the registry subscriber's walk, the explanation service and the DLQ are not in it; the boot proof is BC10's rehearsal (D-v105-23). Edits 14–15.

**F-6 [NON-BLOCKING] — "the window restarted at `at`'s nanos".** `at` is a wall `Instant` (`clock.instant()`'s or the reply's `timestamp`); the window's start is the supplier's reading taken inside the lock. A lane reading this literally would derive nanos from the wall clock and lose the monotonic property R-B buys. Edit 16.

**F-7 [NON-BLOCKING] — the interview hook is left to the lane; it exists and has an ordering.** `interviewDevice` (`A/:1455`, `interviewQueue.complete(ieee)` `:1464`) → `adoptIfAccepted(InterviewResult …)` (`:1493`; `if (interview.interviewStatus() != InterviewStatus.COMPLETE)` `:1502`) → `driveReporting` (`:1523`). The cache record carries the PowerSource at adoption (`:456` comment; the tracker's lookup `:470`–`:472` reads `ZigbeeDeviceRecord::powerSource`), but the reporting contract is configured by `driveReporting` AFTER adoption, so a declaration at adoption reads `mains-floor` for a device that becomes `mains-metered` one evaluation later; R-C's on-change arm covers it. The instruction should say so, or the lane will see two rows and file a deviation. Edit 17.

**F-8 [NON-BLOCKING] — the counters' keying.** `recordCommandResult`'s success path calls `transition(device, timestamp, true, PING_SUCCESS, null)` (`T/:361`–`:362`); the ingestion seam calls the same `transition()` with `available = true` for a frame. R-B's `answeredSinceLastRecord` counts "the probes asked of this device"; the draft says "the success path (`:358`–`:362`)" but not that the count keys on the reason. The miss: `misses = ++state.probeMisses` at `:375` under the lock, then `transition(…, false, PING_TIMEOUT, null)` at `:379`–`:380` when `misses >= PROBE_MISSES_TO_DARK` — a `missedSinceRecord` incremented inside `transition()` on PING_TIMEOUT would count the second miss twice. Edit 18.

**F-9 [NON-BLOCKING] — §0b row 9 is unfilled.** "the count you read": `grep -c 'lock.lock()' T/` = 9 at `9cf0ed9`. Edit 19.

**F-10 [NON-BLOCKING] — BC10's T-A evidence line is printed by nothing.** §0 names "the first `probe_answered` and `availability_contract_declared` rows in the store" — a store read (a `sqlite3` line on the card), fine; but the Pi log carries nothing for either, where `availability_changed` has `zigbee.availability_changed: device={} available={}` (`T/:617`). Two INFO lines in the adapter's listener methods make the card's line a `grep`, not a query. Edit 20.

**F-11 [INFO] — what holds without edit.** The T-A/T-B split (no T-B byte in T-A; `RegistryApplyCensusTest`'s set `:50`–`:53` untouched); the gate lines (`:app:homesynapse-app:test` is already listed, so `Main`'s edit is gated); `EventStore.readByType` is `com.homesynapse.event`'s (`core/event-model/…/EventStore.java:113`) — the projection in `S/` reads it with no new edge; `SubjectRef.device(DeviceId)` (`:67`) and `adoption.deviceIdFor(ieee)` (`ZigbeeAdoptionSlice.java:558`; used at `A/:1570`, `:1674`) are the IEEE → `DeviceId` read §4.2 asks the lane to name; the freeze's `:260` is the additive rule; `ListEntitiesEndpoint.java:200`–`:203` is the entity → device read the projection mirrors.

## §3 The edits (each OLD occurs EXACTLY ONCE in `AVAIL-API-1_instruction_v1.md` at md5 `f1f08c970c45dae39763d8577cb2aa58`; non-overlapping; apply in any order)

### Edit 1 (F-1)
OLD:
~~~~
| T-A | the monotonic source's home — **`platform/platform-api`** `com.homesynapse.platform.time.MonotonicSource` (A; `long nanos()`; the production implementation over `System.nanoTime()` in the whitelisted `platform` package) and the integration context's additive accessor (`integration/integration-api` — the lane reads the context interface and adds a `default MonotonicSource monotonicSource()` that the composition root overrides) | A/M | **THE FORK, RULED BY THE HUB (§9 (1)):** `System.nanoTime` is banned outside `com.homesynapse.{app,platform,test}..` (§0b row 18), so the supplier is built in `platform` and injected; the tracker takes a `LongSupplier` and never names the source. If the integration context already carries a monotonic source the lane did not find, use it and say so under §10 |
~~~~
NEW:
~~~~
| T-A | (the monotonic source — no new module, no new type, no `module-info` edit) | — | **THE FORK, RULED (REVIEW-AA1 F-1):** `IntegrationContext` is a RECORD (`IntegrationContext.java:103`), frozen at 12 components (`ZigbeeIntegrationFactory.java:38`: "the frozen 12-component context carries no clock") — it cannot carry a `default` accessor, and a new component would reach `integration-runtime` (`StandardIntegrationSupervisor.java:1098`) and 16 test/fixture constructions in modules this table does not name. The source rides the `Clock`'s own seam instead (the `A/` row above: `Main` → the factory → the adapter → the tracker). The tracker takes a `LongSupplier` and never names the source. `System.nanoTime` stays banned outside `com.homesynapse.{app,platform,test}..` (§0b row 18): the only call is `Main`'s, in `com.homesynapse.app`. No `platform` type is added |
~~~~

### Edit 2 (F-1)
OLD:
~~~~
| T-A | `A/` (`ZigbeeIntegrationAdapter.java`) | M | the two listener methods publish DEVICE-subject drafts (§4.2, §4.3); the tracker's construction (`:470`) passes the monotonic source; the (re-)interview hook calls the tracker's `declareContract(device)` |
~~~~
NEW:
~~~~
| T-A | `A/` (`ZigbeeIntegrationAdapter.java`) · `…/zigbee/ZigbeeIntegrationFactory.java` · `app/homesynapse-app/src/main/java/com/homesynapse/app/Main.java` | M | the two listener methods publish DEVICE-subject drafts (§4.2, §4.3); the adapter's primary constructor (`:355`) gains `LongSupplier monotonicNanos` beside `Clock clock`, and its test-facing overloads (`:374`, `:386`) default it from the injected clock (`() -> TimeUnit.MILLISECONDS.toNanos(clock.millis())`) so the 18 test constructions in 13 files stand; the factory (`:84`, `:94`) carries it to `:167`/`:170`; `Main.java:114` passes `System::nanoTime` beside `clock` (the `app` package is whitelisted, `HomeSynapseArchRules.java:101`); the tracker's construction (`:470`) passes it on; the (re-)interview hook calls the tracker's `declareContract(device)` |
~~~~

### Edit 3 (F-1)
OLD:
~~~~
The platform module and `integration-api` gain the additive monotonic source (§3; the lane embeds both `module-info.java` files verbatim in the return §1 with the lines it added, if any — an `exports` line for a new package is the only edit allowed).
~~~~
NEW:
~~~~
No module gains anything: the monotonic source rides the `Clock`'s seam (`Main.java:114` → `ZigbeeIntegrationFactory` → the adapter → the tracker; §3), so NO `module-info.java` changes in either tree — the lane quotes the three above unchanged in the return §1; a `module-info` diff in either tree is [BLOCKING].
~~~~

### Edit 4 (F-1)
OLD:
~~~~
`platform` / `integration-api`: the monotonic source.
~~~~
NEW:
~~~~
`app/homesynapse-app`: `Main` hands `System::nanoTime` to the Zigbee factory beside the `Clock` (one row).
~~~~

### Edit 5 (F-1)
OLD:
~~~~
Build the source in `platform` and inject it; the ArchUnit suite
~~~~
NEW:
~~~~
Inject it from `Main` (`com.homesynapse.app`, whitelisted at `HomeSynapseArchRules.java:101`) through the factory's `Clock` seam (§3); the ArchUnit suite
~~~~

### Edit 6 (F-2)
OLD:
~~~~
| T-B | `P/` the view store for the projection's durable view (the lane reads how the state projection's checkpoint is coupled — §0b row 22 — and mirrors THAT form: a table + the coupled write, or the coupled checkpoint store's own API; §4.5 (3)) | A/M | named by the lane in the return §1 with the migration file if one is needed (`PR/V0xx__recovery_card_view.sql`, the next free number; never a change to an existing migration) |
~~~~
NEW:
~~~~
| T-B | `P/` | — | **NO CHANGE and NO MIGRATION** (REVIEW-AA1 F-2): the coupled form already exists for any view — `persistenceFactory.atomicCheckpointSink()` (`PersistenceFactory.java:213`–`:217`) writes the subscriber checkpoint and the opaque view bytes in ONE SQLite transaction under one key (`AtomicCheckpointSink.writeAtomicCheckpoint(key, position, viewData)`; the key is both the subscriber id in `subscriber_checkpoints` and the view name in `view_checkpoints`), and `persistenceFactory.viewCheckpointStore().readLatestCheckpoint(key)` (`ViewCheckpointStore.java:73`) reads it back; the projection serializes its per-device view as JSON bytes (Jackson, as the state projection's checkpoint). A new migration would make T-B IRREVERSIBLE: `MigrationRunner.java:326`–`:329` fails the boot of any build whose latest known version is behind the store's — T-A's build could not boot on a T-B store. A file under `db/migration/` in T-B's diff is [BLOCKING] |
~~~~

### Edit 7 (F-2)
OLD:
~~~~
(3) the checkpoint written as H — **durable and coupled by default (R-F):** the view persisted at H with its checkpoint in the coupled form the state projection uses (`:661`–`:666`; AMD-45 §2.2), so the catch-up runs ONCE and a restart resumes from the checkpoint
~~~~
NEW:
~~~~
(3) the checkpoint written as H — **durable and coupled by default (R-F):** `atomicCheckpointSink.writeAtomicCheckpoint(SUBSCRIBER_ID, H, viewBytes)` — one transaction over the subscriber checkpoint and the view bytes under one key (`PersistenceFactory.java:213`–`:217`; AMD-45 §2.2); the subscriber registers with `atomicCheckpoint = true` (`SubscriberInfo`'s four-argument form, the state projection's at `L/:676`–`:680`), under which the bus writes NO subscriber checkpoint of its own (`InProcessEventBus.java:651`; `ReplayDriver.java:170`, `:209`) — so at runtime the projection writes the same coupled checkpoint after EVERY applied row (the volume is R-B's: ≤ 24 records per asked device per day, plus the contracts and `availability_changed`); at boot it first reads `viewCheckpointStore().readLatestCheckpoint(SUBSCRIBER_ID)` and, when a checkpoint exists, restores the view from its bytes and SKIPS steps (1)–(3) (V-7), so the catch-up runs ONCE and a restart resumes from the checkpoint
~~~~

### Edit 8 (F-2)
OLD:
~~~~
If the coupled form needs a migration, it is a NEW file at the next free number.
~~~~
NEW:
~~~~
NO migration: the coupled form is `atomicCheckpointSink()` over the existing `subscriber_checkpoints` + `view_checkpoints` rows (§3, §4.5 (3)); a migration would make T-B irreversible (`MigrationRunner.java:326`–`:329`: a store ahead of the build fails the boot).
~~~~

### Edit 9 (F-2)
OLD:
~~~~
a coupled-checkpoint API that does not exist in the form §4.5 (3) assumes;
~~~~
NEW:
~~~~
a coupled-checkpoint API that does not behave as §4.5 (3) names it (`atomicCheckpointSink()` / `readLatestCheckpoint`);
~~~~

### Edit 10 (F-2)
OLD:
~~~~
(the projection's checkpoint and view are its own subscriber id; the keys vanish with the code).
~~~~
NEW:
~~~~
(the projection's checkpoint and view are two rows under its own subscriber id in the existing `subscriber_checkpoints` and `view_checkpoints` tables — no table, no migration — which an older build never reads; the keys vanish with the code).
~~~~

### Edit 11 (F-3)
OLD:
~~~~
`sweep` = the tracker's sweep period as a constant the lane reads from `T/` (the sweep interval it finds; cited in the return).
~~~~
NEW:
~~~~
`sweep` = one run cycle, `ZigbeeIntegrationAdapter.PRODUCTION_CYCLE_MILLIS = 50` (`A/:161`; the 0.05 s of `T/:83`–`:85`), and the probe deadline = `AVAILABILITY_PING_TIMEOUT_MILLIS = 5_000` (`A/:176`) — both package-private in `integration-zigbee`, which `state-store` must not require: `StaleRecordBound` carries them as its OWN constants `SWEEP = Duration.ofMillis(50)` and `PROBE_DEADLINE = Duration.ofSeconds(5)`, each with its citation in Javadoc (a duplicated value, never a module edge; the return cites both lines).
~~~~

### Edit 12 (F-3)
OLD:
~~~~
10. **The sweep constant for R-G:** read it from `T/`; cite the line; do not invent 60 s.
~~~~
NEW:
~~~~
10. **The sweep and the deadline for R-G:** they live in `A/`, not `T/` (`PRODUCTION_CYCLE_MILLIS` `:161` = 50 ms; `AVAILABILITY_PING_TIMEOUT_MILLIS` `:176` = 5 s); `StaleRecordBound` carries its own copies with the citations (§4.6); do not invent 60 s and do not add a module edge to read them.
~~~~

### Edit 13 (F-4)
OLD:
~~~~
(f) **the listener is called after the unlock**: a listener that calls back into the tracker (a read) completes without deadlock;
~~~~
NEW:
~~~~
(f) **the listener is called after the unlock**: the lock is a `ReentrantLock` (`T/:230`), so a same-thread callback re-enters and proves nothing — the test's listener, inside `onProbeRecord`, submits a tracker read to a SECOND thread and awaits it with a 2-s bound; it completes only because the lock was released (a listener called under the lock times out: that is the red);
~~~~

### Edit 14 (F-5)
OLD:
~~~~
decode them with a codec whose registry is the manifest MINUS the two classes (the older build's registry, built in the test from `CORE_PRODUCTION_EVENT_CLASSES` filtered by name);
~~~~
NEW:
~~~~
decode them with a codec whose registry is the older build's FULL registry MINUS the two classes (built in the test as `new EventTypeRegistry(…)` over `AllEventClasses.ALL_EVENTS` filtered by name — 58 classes, the list production hands the registry at `SqlitePersistenceLifecycle.java:312`; both constructors are package-private and reachable from the `persistence` test package: `EventTypeRegistry.java:73`, `EventPayloadCodec.java:94`);
~~~~

### Edit 15 (F-5)
OLD:
~~~~
This is the proof that `409547c`'s build boots on a log carrying the two types.
~~~~
NEW:
~~~~
This is the proof, at the codec and the all-types subscriber, that `409547c`'s build DECODES a log carrying the two types and its state projection is unmoved; the BOOT itself is proved by BC10's rehearsal of the older build on the throwaway repo (D-v105-23), which the card names as T-A's rollback evidence — the return says which of the two this test is.
~~~~

### Edit 16 (F-6)
OLD:
~~~~
the counters reset and the window restarted at `at`'s nanos,
~~~~
NEW:
~~~~
the counters reset and the window restarted at the monotonic reading taken inside the lock for this decision (`at` is wall time; the window's start nanos are the supplier's),
~~~~

### Edit 17 (F-7)
OLD:
~~~~
at every (re-)interview of a device (the adapter's hook — the lane names the interview completion site in `A/` and calls `tracker.declareContract(device)` from it);
~~~~
NEW:
~~~~
at every (re-)interview of a device (the hub's reading of the site: `adoptIfAccepted` `A/:1493`, after its `InterviewStatus.COMPLETE` gate at `:1502`, once the cache record carries the PowerSource and the endpoints — the lane confirms it and calls `tracker.declareContract(device)` there; `driveReporting` `:1523` configures the reporting contract AFTER adoption, so the row declared at adoption may read `mains-floor` and R-C's on-change arm re-declares `mains-metered` at the next evaluation — two rows, each true when written; the return names both);
~~~~

### Edit 18 (F-8)
OLD:
~~~~
on a probe outcome — the success path (`:358`–`:362`) and the timeout path that increments `probeMisses` — the counters move INSIDE the lock;
~~~~
NEW:
~~~~
on a probe outcome — the success path (`:358`–`:362`, which enters `transition()` with `AvailabilityReason.PING_SUCCESS`: count the answer ONLY on that reason, never on a frame's positive transition) and the timeout path that increments `probeMisses` (`:371`–`:377`: count the miss THERE and nowhere else, so the dark transition at `:379` never counts it twice) — the counters move INSIDE the lock;
~~~~

### Edit 19 (F-9)
OLD:
~~~~
`private final Clock clock;` · `StandardAvailabilityTracker(Clock clock, ToIntFunction<IEEEAddress> powerSourceLookup, …` · the count you read |
~~~~
NEW:
~~~~
`private final Clock clock;` · `StandardAvailabilityTracker(Clock clock, ToIntFunction<IEEEAddress> powerSourceLookup, …` · `9` (the `ReentrantLock` at `:230`) |
~~~~

### Edit 20 (F-10)
OLD:
~~~~
`priority` = NORMAL if `missed > 0`, else DIAGNOSTIC.
~~~~
NEW:
~~~~
`priority` = NORMAL if `missed > 0`, else DIAGNOSTIC. Each of the two listener methods logs ONE INFO line before its publish, in `T/:617`'s form — `zigbee.probe_answered: device={} answered={} missed={}` and `zigbee.availability_contract_declared: device={} class={}` — the Pi-log evidence line BC10's card quotes beside the store read.
~~~~

## §4 The premise table re-run at `9cf0ed9` (every row; the instrument as written unless noted)

| # | Result | Note |
|---|---|---|
| 1 | HOLDS | `9cf0ed9` · porcelain `0` |
| 2 | HOLDS | `76` · `EventTypesTest.java:46` |
| 3 | HOLDS | `58` |
| 4 | HOLDS | `:367` · `:171`, `:179` · `JacksonWarmupTest:43` (58), `:112` (43) |
| 5 | HOLDS | the record and its compact constructor (`:69`–`:74` not re-read line by line; the form is as stated) |
| 6 | HOLDS | `:56` entity · `:67` device · `SubjectType :27`, `:34` |
| 7 | HOLDS | `NORMAL(1)` `:61` · `DIAGNOSTIC(2)` `:73`; the Javadoc `:25`–`:28` ("may elevate a specific event instance from DIAGNOSTIC to NORMAL") |
| 8 | HOLDS | `:9`, `:23`, `:35`, `:38` |
| 9 | HOLDS | `:225` `private final Clock clock;` · `:261`–`:262` the constructor · `grep -c 'lock.lock()'` = **9** (the draft left it blank — F-9) |
| 10 | HOLDS | `:95` 60 s · `:110` 2 · `:117` 25 h |
| 11 | HOLDS | `silenceLimitFor` `:504`–`:507` · `mainsSilenceLimitFor` `:515`–`:518` · `isMainsPowered` `:550` |
| 12 | HOLDS | `:216` `LinkReading lastLink;` `:217` `Instant lastLinkAt;` `:222` `int probeMisses;` |
| 13 | HOLDS | `:575` lock … `:578`–`:580` `state.lastLink = link;` … `:613` unlock · `:615`–`:620` the sink |
| 14 | HOLDS | `:360`–`:362` |
| 15 | HOLDS | `T/:175` · `A/:2002` |
| 16 | HOLDS | `A/:470` · `:2085`–`:2096` ENTITY-subject per entity |
| 17 | HOLDS | `:872` `expectedSilenceFor` · `:897` `mainsContractFor` |
| 18 | HOLDS | `:108` · 0 production calls |
| 19 | HOLDS | `:1152`–`:1157` · `:588`–`:590` |
| 20 | HOLDS | `:230`, `:236` · `:685` · `:748` |
| 21 | HOLDS | `:635` · `:638` |
| 22 | HOLDS | `:666` · `:679` · `:685` |
| 23 | HOLDS | `:66`–`:68` · `:195` |
| 24 | HOLDS | `:102` |
| 25 | HOLDS | `:23` · `:18` |
| 26 | HOLDS | the first match on `:5` is `v1.1.5` (the grep yields 14 tokens; the draft's reading is the first) · `contract.ts:14` `'v1.1.6-2026-10-09'` |
| 27 | HOLDS | `:25`–`:28` the pre-AMD-102 sentence |
| 28 | HOLDS | `:50`–`:53` three sanctioned callers · `NO_DIRECT_TIME_ACCESS` `:98` (checked `:436`) |

No row fails. Row 9 is the only row the draft left for the lane to fill.

## §5 What I could not verify in the bound
- `AvailabilityChangedEvent.java:69`–`:74` (the compact constructor's triple rule) and `EventCategoryMapping.java:103`–`:104` — cited from the amendment and the draft, not re-read.
- `StateProjection.java:971`–`:984` (the catch-all arm's bump) — `:969`–`:971` read; the arm's end not read.
- `SqliteCheckpointStore.java:160`–`:190`, `ReplayDriver.java:111`/`:145`/`:184` (the post-subscribe delivery) — not re-read; REGISTRY-COLD-1's return is the evidence of record for step (4).
- The REGISTRY-COLD-1 instruction §4.2 and return §1 — the four steps were verified against the CODE at `HomeSynapseCore.java:632`–`:643` and `RegistryProjectionSubscriber.java:138`–`:262`, not against those two files.
- `SPEC.md` §12 Q9–Q12 — the rulings were read from the intake audit §3 (`:27`–`:31`), not from SPEC.
- Whether `JacksonWarmup.warmup` over a filtered registry needs anything beyond the registry (the rollback IT's construction) — `JacksonWarmup.java:107` takes `(mapper, registry)`; not exercised.
- Whether the ArchUnit import includes test classes (bears on the adapter's test overload defaulting from the clock — it does not call `nanoTime`, so it holds either way).
- The `IntegrationContextTest`/`StubIntegrationContext` sites were counted (17 files), not read.
- Q3's "publish storm" was judged from the draft's own design (a last-declared tuple in `DeviceState`), not from code — there is no code yet.
