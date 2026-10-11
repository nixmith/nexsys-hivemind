<!--
file: context/instructions/2026-10-10_coder-lane_REGISTRY-COLD-1_IR-148_registry-rebuild-from-type-index_LOCAL_desk-coding-instruction.md
purpose: THE CODING INSTRUCTION for REGISTRY-COLD-1 — Nick's `COLD-BOOT: a` (Sat 2026-10-10 14:39 CT, D-v104-18) in the shape he named: the registry projection stops walking the whole log at every boot (IR-148: 1,654,229 rows; unfinished at 44.8 s and 38.3 s cold on the Pi; exit 99). Unit 1: note H; rebuild the registries from their four event types only, up to H, through the type index; checkpoint H; subscribe as today — with the type read pinned to its index (IR-40's form), a comparison test and a rows-read guard. Unit 2, its own commit: a progress-based registry gate.
audience: the REGISTRY-COLD-1 Coder lane (Claude Code on Nick's desk) · the hub (the intake) · the reviewer (the one-way-door review, FILED before dispatch)
state-type: coding instruction (LOCAL form; self-gated)
status: DISPATCH-READY — DRAFT v4, re-filed v105 beat 4 (Sat 2026-10-10 ~18:2x CT): v3 + the same reviewer's six addendum edits (A1–A6 — the DLQ premise as the bytes have it: `PersistenceFactory.deadLetterWriter()` exists, no `src/main` caller hands it to the bus; the `L/` prefix; `skipped` sourced from a package-private accessor; K-2's bad-row pass conditions worded), applied by script; the addendum filed at `context/audits/2026-10-10_v105-b4_REGISTRY-COLD-1_independent-review_v3-addendum.md`. Was: DISPATCH-READY — DRAFT v3, re-filed v105 beat 4 (Sat 2026-10-10 ~18:2x CT): v2 (the review's 17 edits) + the hub's four parity edits on Nick's F1 ruling (18:13 CT — (a), the bus's own path, with three parity conditions: the durable trace named at the bytes, `skipped=` on the INFO line; `RuntimeException` only, an `Error` fails at the first; K-2 tested with four and five bad rows), re-read by the same reviewer. Was: DISPATCH-READY — DRAFT v2, filed v105 beat 3 (Sat 2026-10-10 ~18:0x CT): the one-way-door review (`REVIEW-RC1`, READY-WITH-EDITS, 1 BLOCKING + 10 NON-BLOCKING, 17 edits; filed verbatim at `context/audits/2026-10-10_v105-b3_REGISTRY-COLD-1_independent-review.md`) applied by script, every edit once; F1's exception rule is the bus's own (E1–E3, E15) unless Nick's word `RC1-F1: tighten` names the alternative. Dispatches on Nick's paste of §14 (the Java domain is free; AVAIL-API-1 waits on this unit's landing, AMD-103 §4). Was: DRAFT v1 — cut v104 beat 4 (Sat 2026-10-10 ~15:xx CT) from the premises grepped at `409547c` (§0b).
baseline: homesynapse-core `409547c` (`main`; porcelain 0; HERO-U2b + r1; CI green)
-->

# REGISTRY-COLD-1 — the registry rebuilds from its four types up to H, and its checkpoint starts at H · the type read pinned to its index · a progress-based registry gate (LOCAL; self-gated)

## §0 The coder-session prompt (read this whole section before any command; every line binds)
- You are in `~/Desktop/Code/ClaudeFolder/homesynapse-core` on `main` at `409547c`. Run `date -u` FIRST; every stamp you write derives from it (CT = UTC − 5; a Pi log line is EDT = UTC − 4 — name the clock beside every time you quote). `git --no-optional-locks status --porcelain` must be EMPTY before your first act, and your first act is `git switch -c registry-cold-1/ir-148` — every write lives on that branch; never `main`, never `git push`, never merge. **You STAGE, never COMMIT** (THE LANE STOPS AT A LOCK, D-v95-28). If `.git/index.lock` exists before any git act, STOP and write `BLOCKED: index.lock`.
- **TWO TREES, IN ORDER** (Nick: *"A progress-based timeout, as a separate commit"*). Unit 1 (§4.1–§4.3) is written, staged and `./gradlew check` green → `git write-tree` = **T1**, written into the return at once. THEN unit 2 (§4.4) is written, staged and `check` green → `git write-tree` = **T2** (T2 ⊇ T1). A unit-2 byte inside T1 is [BLOCKING]. Nick's landing card commits T1, then T2; the hub cuts it at the intake.
- **SELF-GATED (no plan round-trip).** Before any write to a source file: read §2's set by the ranges given; re-run EVERY row of §0b and paste each count or line into your return's §0; a row that holds as written is your GO for that row; a row that FAILS at `409547c` STOPS the lane at that row — write the return with §0 filled to the failing row and `BLOCKED` on its card, and stop. The forks are settled by this instruction (§4); where it says "the lane reads", the bytes you read decide and the return names them.
- **THE DOOR THIS OPENS IS NICK'S, AND NARROW.** `COLD-BOOT: a` rules the shape (verbatim in §1). REG-INV-1 (AMD-99: *"at boot the registries are reconstructed by replaying those events"*) holds: the same four types, in log order, through the same single apply path — only the READ changes (the type index up to H, instead of the bus's whole-log page walk with the filter applied in process). The bus does not change: `core/event-bus/` is ABSENT from `git --no-optional-locks diff --cached --stat` at T1 and T2. The REPLAY → LIVE hand-off (AMD-42 · AMD-101 · BUS-ORDER-1) is the bus's, untouched; the bus simply starts from H.
- Tests first (§7): the red is OBSERVED — a compile failure on a missing method or constant IS the red; say so in the return — then green. Write ONLY §3's rows (the Files table governs where prose and table differ).
- `./gradlew check` green at T1 and at T2 (`-Xlint:all -Werror` is on). The gate lines are the verbatim task paths of `settings.gradle.kts`: `:core:persistence:test` · `:lifecycle:lifecycle:test` · `:app:homesynapse-app:test` (the ArchUnit rules and `RegistryApplyCensusTest` live there).
- **THE RETURN:** `../nexsys-hivemind/context/audits/<CT-date>_REGISTRY-COLD-1_return.md` — §0 the card (DELIVERED/BLOCKED; `check`'s closing lines at T1 and at T2; the XML test counts for the three modules; `diff --cached --stat` at T1 and at T2; the red texts; §0b's rows re-run with their counts) · §1 what changed (per file, line spans) · §2 the tests (names; the observed red; green) · §3 deviations at honest severity ([INFO]/[REVIEW]/[BLOCKING]) · §4 the survey as re-run (§6) · §5 findings for the register · §6 the MODULE_CONTEXT rows as written (§8) · §7 the numbers: K-1's `registry.projection_rebuilt` line and K-2's two row counts · the last two lines `tree1: <T1>` and `tree: <T2>`.
- The hub stages nothing of yours; the landing is Nick's card after the intake (IR-101's gated form); CI on his push is the gate of record. **The sha that lands is deployed at BC10 (Fri Oct 17, D-v104-18) only after K-4, the real-store comparison, has PASSED on BACKUP-1's copy** (dry-run #1's Part 0 makes the copy) — never on the Pi's live store.

### §0b The premise table (grepped by the hub at `409547c`; re-run each; `L/` = `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/`, `LT/` = its `src/test/…` twin, `P/` = `core/persistence/src/main/java/com/homesynapse/persistence/`, `PT/` = its test twin, `PR/` = `core/persistence/src/main/resources/db/migration/events/`, `B/` = `core/event-bus/src/main/java/com/homesynapse/event/bus/`, `AT/` = `app/homesynapse-app/src/test/java/com/homesynapse/app/`)
| # | The claim | The instrument | Found at `409547c` |
|---|---|---|---|
| 1 | The baseline | `git --no-optional-locks rev-parse --short HEAD` · `git --no-optional-locks status --porcelain \| wc -l` | `409547c` · `0` |
| 2 | ONE checkpoint reset to 0 in production code: the registry's | `git --no-optional-locks grep -n -E 'writeCheckpoint\([^)]*, 0L\)' -- '*/src/main/*.java'` | 1: `L/HomeSynapseCore.java:623` (`.writeCheckpoint(RegistryProjectionSubscriber.SUBSCRIBER_ID, 0L);`) |
| 3 | Step 3.1 subscribes the registry after the reset | `grep -n -A2 'eventBus.subscribeRuntime($' L/HomeSynapseCore.java \| head -3` | `:624`–`:626`: `new SubscriberInfo(RegistryProjectionSubscriber.SUBSCRIBER_ID, RegistryProjectionSubscriber.subscriptionFilter(), false)` |
| 4 | The two ~30-s gates and the registry gate's callers | `grep -n 'maxPolls = 1_500' L/HomeSynapseCore.java` · `grep -n 'awaitRegistryProjectionLive();' L/HomeSynapseCore.java` | `:1463` (state), `:1500` (registry) · `:669` (Step 3.2, before the state projection subscribes — IR-61b), `:702` |
| 5 | The registry gate's throw — the Pi's stack trace line | `grep -n 'registry projection did not reach LIVE' L/HomeSynapseCore.java` | `:1514` (the `throw` at `:1513`; the capture: `HomeSynapseCore.java:1513`) |
| 6 | The four types; `onEvent` has no mode guard; four apply sites | `sed -n '75,81p' L/RegistryProjectionSubscriber.java` · `grep -c 'projection\.apply' L/RegistryProjectionSubscriber.java` | `SubscriptionFilter.forTypes(DEVICE_REGISTERED, ENTITY_REGISTERED, DEVICE_REMOVED, CAPABILITY_ADDED)` · `4` (`:87`, `:89`, `:90`, `:97`); `onEvent` `:84`–`:117` switches on the payload and sets `lastAppliedPosition` `:116` |
| 7 | The index exists and no migration drops it | `grep -n 'idx_events_type' PR/*.sql` | 1: `V001__initial_event_store_schema.sql:58` `ON events(event_type, global_position)` (V003 drops only `idx_events_subject`) |
| 8 | Positions: one writer, AUTOINCREMENT | `sed -n '29p' PR/V001__initial_event_store_schema.sql` | `global_position   INTEGER PRIMARY KEY AUTOINCREMENT,` |
| 9 | The type read carries NO hint; the only hint is the time range's | `grep -n -A2 'SELECT_BY_TYPE_SQL =' P/SqliteEventStore.java` · `grep -n 'INDEXED BY' P/SqliteEventStore.java` | `:212`–`:214` `… WHERE event_type = ? AND global_position > ? ORDER BY global_position ASC LIMIT ?` · `:221` (javadoc), `:237` (`idx_events_event_time`) |
| 10 | The type hasMore probe, unhinted | `grep -n 'WHERE event_type = ? AND global_position > ? LIMIT 1' P/SqliteEventStore.java` | `:772` |
| 11 | H's read | `grep -n 'COALESCE(MAX(global_position), 0)' P/SqliteEventStore.java` | `:244`; `latestPosition()` `:725` |
| 12 | No ANALYZE anywhere in production (the planner runs on its heuristics) | `git --no-optional-locks grep -n -i -w 'ANALYZE' -- '*/src/main/*' \| wc -l` | `0` |
| 13 | IR-40's plan test — the form to mirror | `grep -n -E 'INDEX_PLAN =\|ROWID_WALK_PLAN =' PT/SqliteEventStoreTimeRangePlanTest.java` | `:79` `"USING INDEX " + INDEX_NAME` · `:80` `"USING INTEGER PRIMARY KEY"` |
| 14 | The bus reads the checkpoint at registration, on its own thread | `sed -n '111p' B/ReplayDriver.java` | `long currentPosition = checkpointStore.readCheckpoint(subscriberId);` |
| 15 | AMD-38's replay checkpoint cadence | `grep -n -E 'CHECKPOINT_EVENT_THRESHOLD =\|CHECKPOINT_MAX_INTERVAL_SECONDS =' B/ReplayDriver.java` | `:67` `200` · `:70` `2L` |
| 16 | `onCaughtUp` fires once, empty replay included | `sed -n '156p' B/TransitionCoordinator.java`; the javadoc `:41` | `runtime.subscriber().onCaughtUp();` · "exactly once" |
| 17 | The bus's position read is the stored checkpoint | `sed -n '388,391p' B/InProcessEventBus.java` | `subscriberPosition(String)` returns `checkpointStore.readCheckpoint(subscriberId)` |
| 18 | The snapshot the gate reads | `sed -n '50,58p' B/SubscriberSnapshot.java` | `(subscriberId, mode, checkpoint, dlqDepth, pendingDepth, crashCount, oldestParkedAt)` |
| 19 | The filter's own predicate | `grep -n 'public boolean matches(EventEnvelope' B/SubscriptionFilter.java` | `:129` |
| 20 | The clock rule reaches `System.nanoTime` | `grep -n '"nanoTime"' AT/HomeSynapseArchRules.java` | `:108` |
| 21 | The apply census | `sed -n '49,54p' AT/RegistryApplyCensusTest.java` | `SANCTIONED_APPLY_CALLERS = Set.of("…zigbee.ZigbeeAdoptionSlice", "…zigbee.ZigbeeIntegrationAdapter", "com.homesynapse.lifecycle.RegistryProjectionSubscriber")` |
| 22 | The pins this unit must keep green | `grep -c 'registry.projection_live' LT/BootOrderingGateIT.java` · `grep -n 'devices=1 entities=2' LT/ProcessRestartIdentityIT.java` | `4` · `:168` |
| 23 | The lifecycle module already reads the store's API | `grep -n -E 'requires transitive com\.homesynapse\.(event\|persistence\|event\.bus);' lifecycle/lifecycle/src/main/java/module-info.java` | `:22` · `:34` · `:35` |

## §1 What this implements
**Nick's ruling, verbatim (14:39 CT; filed `nexsys-hivemind/context/planning/2026-10-10_v104_decision-record.md`, D-v104-18):** *"There's a shape that leaves the bus untouched: 1. Note the log's current last position, H. 2. Rebuild the registry from its 4 event types only, up to H, using the database's existing index. That takes milliseconds, and the events go through the registry's normal single apply path. 3. Set the registry's checkpoint to H instead of 0. 4. Subscribe it to the bus as today. The bus only replays what arrived after H. That's the same mechanism the code uses now, with a different starting value."* Alongside it: *"A progress-based timeout, as a separate commit: fail only if the replay stops moving, not after a fixed 30 s."* · *"A comparison test: the registry rebuilt the new way must equal the registry rebuilt by the full replay, on a copy of the real 1.65 M-event store."* · *"A CI guard on rows read, not time, so it's deterministic."* (His fourth, the cleared-cache test on the Pi, is the bench packets', §11.)

**The defect (IR-148, D-v104-10):** the Pi's cold launches at 11:43 and 11:45 CT (12:43 and 12:45 EDT in the Pi's lines) logged `Persistence layer started` and then, 44.8 s and 38.3 s later, `lifecycle.startup_failed: phase=CORE_DOMAIN subsystem=state-store` with `java.lang.IllegalStateException: registry projection did not reach LIVE within ~30s during startup at …HomeSynapseCore.awaitRegistryProjectionLive(HomeSynapseCore.java:1513)` — exit 99 (`nexsys-hivemind/context/audits/2026-10-10_v104-b1_boot_restore_PKG-FRESH-1_intake_two-layer_audit.md` §4). The store: 1,654,229 rows, 828,829,696 B, on the SD card. Warm (after the file was read once), the same boot passed. The registry's checkpoint is reset to 0 at every boot (§0b row 2), so the bus pages the WHOLE log (`readFrom`, 500 rows a page) and keeps four types in process: the boot's cost grows with the log, not with the registry.

**After this unit:** the boot's registry cost is the four types' rows (read through `idx_events_type`), plus the bus's replay of the rows after H (the few that arrive during the boot). The read is pinned to the index so a planner choice cannot turn it back into a log walk (§4.1). If the bus's replay ever stalls, the gate says so; while it moves, the gate waits (§4.4, T2).

## §2 Files to read before starting (the minimum read set; by range)
- `L/HomeSynapseCore.java` `:596`–`:632` (Step 3.1), `:655`–`:705` (Steps 3.2–3.3; the two gate calls), `:1455`–`:1530` (both gates; `registryProjectionMode()`).
- `L/RegistryProjectionSubscriber.java` whole (126 lines).
- `P/SqliteEventStore.java` `:186`–`:245` (the SQL constants; IR-40's javadoc `:216`–`:233`), `:590`–`:684` (`readFrom`, `readByType`), `:720`–`:800` (`latestPosition`; the hasMore probes).
- `PT/SqliteEventStoreTimeRangePlanTest.java` whole — the form P-1..P-3 mirror.
- `B/ReplayDriver.java` `:100`–`:230`; `B/InProcessEventBus.java` `:380`–`:430` (`subscribeRuntime`; the virtual thread's start `:426`), `:455`–`:490`, `:630`–`:660` (`deliverStep`), `:765`–`:773` (`buildSnapshot`: the snapshot's `checkpoint` is the persisted one); `B/SubscriberSupervisor.java` `:48`–`:145` (the PARKED arm §4.2 mirrors) — all READ ONLY.
- `core/event-model/src/main/java/com/homesynapse/event/EventStore.java` `:100`–`:130`; `EventPage.java`.
- `AT/HomeSynapseArchRules.java` `:84`–`:110`, `:398`–`:425`; `AT/RegistryApplyCensusTest.java` whole.
- The pins: `LT/BootOrderingGateIT.java` (T3), `LT/ProcessRestartIdentityIT.java` `:150`–`:175`, `LT/RestartHonestyIT.java` `:244`–`:292`, `LT/RegistryProjectionSubscriberTest.java`, `LT/RealCoreFixture.java` (how a core boots on a store that already holds rows).
- `lifecycle/lifecycle/MODULE_CONTEXT.md` and `core/persistence/MODULE_CONTEXT.md`: `grep -n -i 'registry_projection\|RESETS TO 0\|IR-40\|readByType'` — the rows §8 edits.

## §3 Files to create or modify (the Files table governs; A = added, M = modified)
| Path | A/M | Tree | What |
|---|---|---|---|
| `P/SqliteEventStore.java` | M | T1 | `INDEXED BY idx_events_type` on `SELECT_BY_TYPE_SQL` and on the type hasMore probe (`:770`–`:772`), both package-private constants; the javadoc names IR-148 beside IR-40 (§4.1) |
| `PT/SqliteEventStoreTypeReadPlanTest.java` | A | T1 | P-1..P-3 |
| `L/RegistryProjectionSubscriber.java` | M | T1 | `rebuildFromIndex(EventStore, long)` and the one type list shared with `subscriptionFilter()` (§4.2) |
| `L/HomeSynapseCore.java` | M | T1, T2 | Step 3.1 (§4.3) in T1; the registry gate (§4.4) in T2 |
| `LT/RegistryProjectionSubscriberTest.java` | M | T1 | R-1..R-5 |
| `LT/RegistryColdBootIT.java` | A | T1 | K-1..K-3 |
| `LT/RegistryRealStoreComparisonIT.java` | A | T1 | K-4 (opt-in; skipped without its property) |
| `L/RegistryGate.java` | A | T2 | the gate's polling logic, package-private, with an injected sleeper (§4.4) |
| `LT/RegistryGateTest.java` | A | T2 | G-1..G-3 |
| `lifecycle/lifecycle/MODULE_CONTEXT.md` · `core/persistence/MODULE_CONTEXT.md` | M · M | T1 | the rows of §8 |
The census at T1: 9 paths — 3 A (`SqliteEventStoreTypeReadPlanTest`, `RegistryColdBootIT`, `RegistryRealStoreComparisonIT`) + 6 M. At T2: 11 paths — T1's 9 + 2 A (`RegistryGate`, `RegistryGateTest`); `HomeSynapseCore.java` changes again inside its own path. A path outside this table is [BLOCKING].

## §4 Technical specification
### §4.1 The type read pinned to its index (T1) — `P/SqliteEventStore.java`
- `SELECT_BY_TYPE_SQL` (`:212`–`:214`) becomes package-private and carries the hint in the time range's form (`:235`–`:241`): `SELECT_COLS + " INDEXED BY idx_events_type" + " WHERE event_type = ? AND global_position > ? " + "ORDER BY global_position ASC LIMIT ?"`.
- The type branch of the hasMore probe (`:770`–`:772`, used by `hasMoreForTypeAfterPosition` `:768`) becomes a package-private constant with the same hint: `SELECT 1 FROM events INDEXED BY idx_events_type WHERE event_type = ? AND global_position > ? LIMIT 1`.
- The javadoc gains one paragraph beside IR-40's: *"`INDEXED BY idx_events_type` (REGISTRY-COLD-1, IR-148): the registry's boot rebuild reads its four types through these statements. A rowid walk — the plan IR-40 caught the shipped planner choosing for the sibling time-range read — would turn the rebuild back into a whole-log walk while returning the same few hundred rows, which no count of returned rows can see. The hint makes the plan the index range whatever the bound page size or the table's size, and a dropped or renamed index fails loudly (`no such index`)."*
- Nothing else in the class changes: `readByType`'s signature, page shape and `hasMore` rule stand; `StandardExplanationService:1063` reads through the same pinned statement.

### §4.2 `RegistryProjectionSubscriber.rebuildFromIndex(EventStore store, long head)` (T1) — `L/`
- Package-private instance method; returns `long`, the envelopes passed to `onEvent` (the throw arm's rows included — they were passed). A package-private `long skipped()` accessor returns the throw arm's count (a plain field written on `main` during the rebuild, read on `main` before `subscribeRuntime` — §4.3's edge covers it; 0 when nothing threw).
- **One type list.** A private static list of the four types (`DEVICE_REGISTERED`, `ENTITY_REGISTERED`, `DEVICE_REMOVED`, `CAPABILITY_ADDED`) that `subscriptionFilter()` ALSO builds from, so the filter and the rebuild cannot drift.
- **Per type, a cursor:** `store.readByType(type, after, REBUILD_PAGE)`, `REBUILD_PAGE = 500` (the bus's `MAX_REPLAY_PAGE` value, `B/ReplayDriver.java:64`, cited in a comment, not imported — the bus's constant is package-private to the bus), `after` from 0. An envelope with `globalPosition() > head` ends that cursor (the read has no upper bound); `hasMore == false` ends it too.
- **A four-way MERGE by `globalPosition()`, ascending**, holding at most one page per type: per-type order is not log order, and the apply order matters (the `capability.added` orphan arm, AMD-99's implementation note; a remove-then-re-register sequence). Positions are unique, so a tie between two cursors is impossible: assert it (`IllegalStateException` naming both types and the position).
- **Each envelope** passes `subscriptionFilter().matches(envelope)` (`B/SubscriptionFilter.java:129`, the bus's own predicate; for `forTypes` it is a type-only test — DIAGNOSTIC floor, no subject restriction, `:91`–`:94` — so a `false` IS a type the read should not have returned) — a typed read that returns another type throws `IllegalStateException` naming the type asked and the type returned — and then goes to **`onEvent(envelope)`**, the SAME method the bus calls (no mode guard, §0b row 6): the `DegradedEvent` and unexpected-payload WARN arms, the orphan WARN and `lastAppliedPosition` all behave as under the bus.
- **The class javadoc** (`:29`–`:33`: "the composition root resets this subscriber's checkpoint to 0 BEFORE registration, so every boot replays the full registration history") is re-cut to the four steps; `SUBSCRIBER_ID`'s javadoc (`:47`, "the checkpoint key the boot reset targets") becomes "the checkpoint key Step 3.1 writes H to".
- **Never `projection.apply*` from the new method**, and no lambda, anonymous or inner class calls `apply*` — `RegistryApplyCensusTest` names CLASSES (a `$1` would break it). A plain loop is simplest.
- **A `RuntimeException` from `onEvent` is handled as the bus's supervisor handles it** (`B/SubscriberSupervisor.java:97`–`:135`: the row is parked, the crash counted, delivery continues; SUSPENDED at the fifth crash — `CIRCUIT_BREAKER_THRESHOLD = 5`, `:52`). The rebuild catches it per envelope, logs ONE WARN `registry.projection_rebuild_apply_failed: type={} position={} cause={}`, counts it and continues; at the fifth — `REBUILD_CRASH_THRESHOLD = 5`, a named constant of the lifecycle module retyped from `B/SubscriberSupervisor.java:52` (the bus's is private; K-2's five-row case is the drift detector) — it throws `IllegalStateException` naming the count and the position, and the boot fails inside Step 3.1 (`initializing = "device-model"`) at once, with the rebuild's own message. **The one visible difference, accepted (Nick, 18:13 CT):** today the fifth crash surfaces ≈ 30 s later as `registry projection did not reach LIVE` (`L/HomeSynapseCore.java:1514`); anything that matched that text for a crash storm will not see the rebuild's exception. **The durable trace:** today's parked row is not durable either — `subscribeRuntime` wires `PersistentDlqWriter.noop()` (`B/InProcessEventBus.java:401`–`:402`; the production writer exists — `PersistenceFactory.deadLetterWriter()` `:252`, `SqliteDeadLetterStore::park` — but no `src/main` caller passes it to the bus: its only callers are `PersistenceFactoryTest:67`, `:93`) and `SubscriberDlq.park` writes no log line, so a parked registration row leaves only the in-memory `dlqDepth`; the rebuild's WARN is one line more than today's silence, and the count rides the INFO line as `skipped=` (§4.1; K-1). **What it catches:** `RuntimeException` only, as the supervisor's first arm (`:102`); an `Error` (`:136`) or a checked exception (`:142`) SUSPENDs the subscriber at the first today and is NOT caught here — it propagates and the boot fails at the first. Nothing else is caught: a `readByType` that throws propagates. The reason: a registration row whose apply throws (`RegistryProjection.java:83`–`:84`: an enum name unknown to this build — the shape of a store a newer build wrote) boots the Core today with the row parked; propagating would make that store unbootable on this code, a tightening Nick did not rule. If Nick rules the tightening, this bullet reverts to "Exceptions propagate", R-5 inverts, and §13 names the change for the register.

### §4.3 Step 3.1 (T1) — `L/HomeSynapseCore.java` `:603`–`:629`, in this ORDER
```java
this.registryProjection = new RegistryProjection(deviceRegistry, entityRegistry);
RegistryProjectionSubscriber registrySubscriber =
        new RegistryProjectionSubscriber(registryProjection, deviceRegistry, entityRegistry);
EventStore store = persistenceFactory.eventStore();
long head = store.latestPosition();                                         // (1) H
Instant rebuildStart = clock.instant();
long rows = registrySubscriber.rebuildFromIndex(store, head);               // (2)
long skipped = registrySubscriber.skipped();                                 // (2b) the throw arm's count, 0 normally
persistenceFactory.checkpointStore()
        .writeCheckpoint(RegistryProjectionSubscriber.SUBSCRIBER_ID, head); // (3) H, not 0
LOG.info("registry.projection_rebuilt: rows={} head={} skipped={} ms={}", rows, head, skipped,
        Duration.between(rebuildStart, clock.instant()).toMillis());
eventBus.subscribeRuntime(
        new SubscriberInfo(RegistryProjectionSubscriber.SUBSCRIBER_ID,
                RegistryProjectionSubscriber.subscriptionFilter(), false),
        registrySubscriber);                                                // (4) as today
```
- The SAME subscriber instance rebuilds and subscribes, so its `lastAppliedPosition` carries into `registry.projection_live`'s `position=` with today's meaning.
- H is read BEFORE the rebuild. The checkpoint is written AFTER the rebuild returns and BEFORE `subscribeRuntime`: the bus reads it on its own thread after the call (§0b row 14). A rebuild that throws never reaches the write. **The happens-before edge** into the bus's thread is the virtual thread's start inside `subscribeRuntime` (`B/InProcessEventBus.java:426`–`:428`, `Thread.ofVirtual()…start(...)`): everything `main` wrote before the call — the registries' contents and `lastAppliedPosition` (also `volatile`, `L/RegistryProjectionSubscriber.java:57`) — is visible to `hs-sub-registry_projection`. **The write is durable at its return:** `SqliteCheckpointStore.writeCheckpoint` (`:167`) blocks on the write coordinator's future (`P/PlatformThreadWriteCoordinator.java:69`–`:90`, `return future.get()`), and the bus's read (`B/ReplayDriver.java:111`) runs a new read transaction on a read connection, which under WAL sees the committed row.
- **Why no row is lost or doubled:** one writer and AUTOINCREMENT (§0b row 8), so no row ≤ H commits after H is read. The rebuild applies (0, H]; the bus delivers every row > H, whether appended before or after `subscribeRuntime`. Both halves go through `onEvent`.
- The comment block `:612`–`:620` is re-cut: the four steps; "IR-148: the reset to 0 made every boot walk the whole log"; REG-INV-1 kept.
- Time is the injected `clock` (the arch rule reaches `System.nanoTime`, §0b row 20). On the Pi `ms=` is wall-clock milliseconds; under a fixed test clock it prints 0, so K-1 asserts `rows=` and `head=`, never `ms=`.
- `registry.projection_live` does not change: four pins in `BootOrderingGateIT`, `ProcessRestartIdentityIT:168`, and the bench's fixtures parse it.

### §4.4 Unit 2 (T2) — the progress-based registry gate
- `L/RegistryGate.java`, a package-private final class, holds the loop with an injected sleeper, e.g. `static void awaitLive(Supplier<Optional<SubscriberSnapshot>> snapshot, int stallPolls, LongConsumer sleeper)` (the lane picks the exact shape). It polls every 20 ms; it returns on `mode == LIVE`; **progress** = the snapshot's `checkpoint` or `mode` differs from the previous poll's; it **fails** after `stallPolls` consecutive polls with no progress. `stallPolls = 1_500` (~30 s at 20 ms — today's number, now counted from the last movement).
- A moving replay shows progress: the driver writes the checkpoint every 200 matching events or every 2 s during REPLAY (AMD-38, §0b row 15).
- No clock read: it counts polls. Production passes `Thread.sleep`; tests pass a recorder and never sleep.
- The failure is an `IllegalStateException`, as today: `"registry projection made no progress for ~30s during startup (mode=<m>, checkpoint=<n>)"`.
- `awaitRegistryProjectionLive()` (`:1499`) delegates to it, passing a supplier built on `eventBus.subscribers()` filtered to `RegistryProjectionSubscriber.SUBSCRIBER_ID` (the lookup `registryProjectionMode()` makes today, `:1517`–`:1526`). `registryProjectionMode()` has ONE reader at `409547c` (`:1502`): it is re-cut as that snapshot lookup or removed, never left dead.
- `awaitProjectionLive()` (`:1462`, the state projection's) is NOT changed. Its checkpoint is the coupled atomic one (AMD-45 §2.2), written at the projection's own cadence; whether the same gate fits it is a [REVIEW] row in the return's §3.
- No absolute ceiling (Nick: *"fail only if the replay stops moving"*): a ceiling is a §10 question, not this unit's. The outer bound is the packaged unit's: `distribution/systemd/homesynapse.service:54` `health-probe.sh --wait --timeout 90` (ExecStartPost; `/health` is 200 only once the state projection is LIVE, which waits on this gate) and `:61` `TimeoutStartSec=120`. Under the unit a registry replay that keeps moving past ~90 s ends as a start failure of the unit (the probe's exit 3) with no `lifecycle.startup_failed` line; the bench Core, which runs under no unit, waits as long as the replay moves. The return's §5 names this for the register.

## §5 The module boundaries (at `409547c`; NO proposed change)
- `lifecycle/lifecycle/src/main/java/module-info.java` already `requires transitive com.homesynapse.event` (`:22`, `EventStore`'s module), `com.homesynapse.persistence` (`:34`) and `com.homesynapse.event.bus` (`:35`) — unchanged.
- `core/persistence`'s module-info — unchanged (the change is a SQL string and a test).
- A module-info edit anywhere is [BLOCKING]: stop and report.

## §6 The consumer/pin survey (the hub's counts at `409547c`; the lane re-runs each before writing and pastes the post-unit counts into its return's §4)
- `git --no-optional-locks grep -n 'SUBSCRIBER_ID, 0L' -- '*/src/main/*.java'` → 1 (`HomeSynapseCore.java:623`) → **0**.
- `git --no-optional-locks grep -n 'INDEXED BY' -- '*/src/main/*.java'` → 2 lines (`SqliteEventStore.java:221`, `:237`) → the lane names the post-unit lines.
- `git --no-optional-locks grep -n 'readByType(' -- '*/src/main/*.java'` → 3 (`EventStore.java:113`, `SqliteEventStore.java:662`, `StandardExplanationService.java:1063`) → **4**.
- `git --no-optional-locks grep -n 'registry.projection_rebuilt'` → 0 → 1 in main + K-1's.
- `git --no-optional-locks grep -n 'registry.projection_live'` and `'awaitRegistryProjectionCaughtUp'` → listed, unchanged.
- The bench's readers of these lines live in `nexsys-bench`: the hub's, not this lane's.

## §7 Test requirements (red first; each named in the return with its red text)
**Persistence (`SqliteEventStoreTypeReadPlanTest`, the time-range plan test's fixture and migrations list):**
- **P-1:** `EXPLAIN QUERY PLAN` of `SELECT_BY_TYPE_SQL`, bound with LIMIT 1, 500 and 10,000 and unbound (the form's `UNBOUND`), on an empty table AND on a table of ≥ 100,000 rows where the queried type is ≤ 1 % (the rows may go in by direct SQL on the write connection, not `append` — the plan is what is under test, and IR-40's probe recorded that the row count, 0 or 100k, and the absence of `sqlite_stat1` did not move the planner, `PT/SqliteEventStoreTimeRangePlanTest.java:146`–`:150`; if the fixture costs more than ~5 s in CI, say so under §10 and keep the 100k table for the once-only unhinted run below) → every plan names `idx_events_type` (`USING INDEX` or `USING COVERING INDEX`) and never `USING INTEGER PRIMARY KEY` or `SCAN events`.
- **P-2:** the same for the hasMore constant.
- **P-3:** on a schema WITHOUT `idx_events_type`, both statements fail with `no such index`.
- The red: P-1 and P-2 reference the new package-private constants (the compile failure IS the red). ALSO run, once, the UNHINTED text at each bound on the 100,000-row table and quote its plans in the return's §2 — the fact IR-148's register row needs.

**Lifecycle (`RegistryProjectionSubscriberTest`):**
- **R-1 ORDER:** a log whose per-type order is not its global order — `device_registered` D (p1) · `entity_registered` E (p2) · `device_removed` D (p3) · `device_registered` D again (p5) · `capability.added` on E (p6), with non-registry rows between → the rebuilt registries EQUAL those built by `onEvent` over the same envelopes in position order.
- **R-2 THE CUT:** registry rows above `head` are not applied; `lastAppliedPosition` ≤ head.
- **R-3 THE ROWS-READ GUARD** (deterministic; Nick's CI guard): a counting `EventStore` decorator over a store of 10,000 non-registry rows and 40 registry rows → zero `readFrom` calls, `readByType` called only with the four types, 40 envelopes returned. It counts rows, never time.
- **R-4:** a registry-type row that fails decode arrives as a `DegradedEvent`, takes the WARN arm (`registry.projection_degraded_event`), and the rebuild does not throw.
- **R-5 THE THROW ARM:** a registry-type row whose `onEvent` throws a `RuntimeException` (a registry stub whose `createDevice` throws for one id) → ONE `registry.projection_rebuild_apply_failed` WARN, that row skipped, every other row applied, the rebuild returns; five such rows → `IllegalStateException` (§4.2).

**Lifecycle (`RegistryColdBootIT`, a real core booted on a store that already holds rows, the way `RealCoreFixture` does):**
- **K-1:** N registry rows among M ≥ 50 × N others → ONE `registry.projection_rebuilt: rows=N head=H skipped=0` line and ONE `registry.projection_live` line with the right counts; the registry subscriber's `SubscriberSnapshot.checkpoint` ≥ H once LIVE (read through `eventBus().subscribers()`).
- **K-2 THE COMPARISON** (synthetic, in CI): the same store rebuilt the OLD way (every envelope of `readFrom(0, 500)` pages that `subscriptionFilter().matches`, fed in order to a fresh subscriber's `onEvent`, a `RuntimeException` from `onEvent` skipping that row as the supervisor's PARKED does, and SUSPENDING — the model stops and reports SUSPENDED — at the fifth, as `:128` does) and the NEW way (`rebuildFromIndex`) → the device and entity registries EQUAL, record for record. **With bad rows (parity tested, not asserted — Nick, 18:13 CT):** the same store with FOUR registry-type rows whose apply throws (a registry stub throwing for four ids) → both ways yield the same registries minus those rows and the INFO line reads `skipped=4`; with FIVE → both ways FAIL (the old way's model reports SUSPENDED, the new way throws `IllegalStateException`); the sub-case asserts both outcomes and is green when both occur — the test that keeps the retyped threshold from drifting from the bus's. The return's §7 names both row counts and the two bad-row outcomes.
- **K-3:** a restart on the same store keeps identity (`ProcessRestartIdentityIT`'s shape): the same deviceIds and entityIds, and the same `devices=… entities=…` as before the stop.

**Lifecycle (`RegistryRealStoreComparisonIT`) — K-4, THE REAL-STORE COMPARISON, OPT-IN:**
- It runs only with `-Dhomesynapse.registryCold.store=<path>`; JUnit `Assumptions` skip it otherwise, so CI and this sitting run it SKIPPED.
- It copies the given file, with any `-wal` beside it, to a JUnit `@TempDir` (deleted after the run; the copy is ~830 MB, so the desk needs the space) and opens the COPY: opening runs migrations and PRAGMAs, and a backup is never written. The source must be a file no running Core has open — a file-level copy of an open WAL database is not a consistent snapshot. BACKUP-1's copy is such a file; the Pi's live store is not (§0).
- It builds both registries as K-2 does, asserts equality, and prints rows and ms for both ways.
- Its real run is on BACKUP-1's copy, after dry-run #1's Part 0 — BC10's precondition (§0).

**Lifecycle (`RegistryGateTest`) — unit 2, T2 only, no real sleep:**
- **G-1:** a snapshot frozen in REPLAY → throws after exactly `stallPolls` polls; the message names mode and checkpoint.
- **G-2:** a checkpoint that moves once every 1,000 polls for 5,000 polls, then LIVE → returns (today's gate would have thrown at 1,500).
- **G-3:** LIVE on the first poll → returns with zero sleeps.

**The test clock** — paste-block, verbatim: **Tests must inject `Clock`.** Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` in this module's test code. Use `Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC)` injected via constructor/`@BeforeEach`. **Enforcement reach:** `NO_DIRECT_TIME_ACCESS` runs from `com.homesynapse.app`'s ArchUnit suite over every module's production classes and the app module's own test tree only (`AT/HomeSynapseArchRules.java:362`–`:366`); `LT/` test code is not scanned, so for this module's tests the rule is a convention the return attests, not an enforcement.

## §8 MODULE_CONTEXT.md — rows only
- **`lifecycle/lifecycle/MODULE_CONTEXT.md`:** a new row at the top in the J-row form — REGISTRY-COLD-1 (the date; the branch; T1 · T2): *"IR-148 — Step 3.1 rebuilds the registries from the four registry types through `idx_events_type` up to H = `latestPosition()`, through `onEvent` in log order (REG-INV-1 kept), writes the registry subscriber's checkpoint as H (was 0), then subscribes; the bus replays only the rows after H. One INFO line `registry.projection_rebuilt: rows= head= ms=`. T2: the registry gate fails after ~30 s WITHOUT PROGRESS (`RegistryGate`)."* Any row or sentence saying the checkpoint resets to 0 is ANNOTATED "(REGISTRY-COLD-1: now H)", never deleted.
- **`core/persistence/MODULE_CONTEXT.md`:** a row under IR-40's: *"`SELECT_BY_TYPE_SQL` and the type hasMore probe carry `INDEXED BY idx_events_type` (REGISTRY-COLD-1, IR-148: the registry's boot rebuild reads through them); `SqliteEventStoreTypeReadPlanTest` pins the plan."*

## §9 What to watch out for
- **The threshold is retyped, and the old text is gone for a crash storm.** `CIRCUIT_BREAKER_THRESHOLD` is private to the bus (`B/SubscriberSupervisor.java:52`); `REBUILD_CRASH_THRESHOLD = 5` is the lifecycle module's own constant with a comment citing that line, and K-2's five-row case fails if either moves. A reader that matched `registry projection did not reach LIVE` for five bad rows now sees the rebuild's `IllegalStateException` in Step 3.1 instead (§4.2).
- **The SQL itself.**
  - `SELECT_COLS` (`:192`–`:199`) must end at `FROM events`, so the hint goes between it and `WHERE`. Read it before writing.
  - `readByType`'s `hasMore` (`:677`–`:679`) is computed only when a page is full. Read it before trusting it to end a cursor.
- **The merge.** It is a merge, never a concatenation: per-type order is not log order (R-1). The cut at H is the caller's, because the read has none.
- **The checkpoint.**
  - The store is the bus's own (`persistenceFactory.checkpointStore()`, the one `ReplayDriver` reads), never a new store.
  - `subscribeRuntime` returns before the replay runs, so the write must be durable at its return. Read `SqliteCheckpointStore.writeCheckpoint` (`:167`) to confirm it is synchronous.
- **Lines and tests that stay as they are.**
  - `registry.projection_live`'s `position=` stays `lastAppliedPosition` (≤ H at boot). Do not "fix" it to H.
  - The tests' `awaitRegistryProjectionCaughtUp` (RestartHonestyIT `:264`–`:274`; ZigbeeReplaySafetyIT; BusPositionCensusIT) waits for checkpoint ≥ the last registration fact. H satisfies it for facts from before the boot, and adoptions after the boot still move it through the bus.
  - A test that passed only because it watched a whole-log replay is a [REVIEW] finding, never a silent rewrite.
  - `BusPositionCensusIT`'s manifest (`:270`) pins the registry's id, filter and `false` — unchanged.
- **Out of scope, but name them in the return's §5.**
  - The startup-failure line names `subsystem=state-store` for the registry's gate, because the gate is called inside Step 3.2 since IR-61b (`:669`).
  - The Pi's cold boot spent ~8 s between `Persistence layer started` (12:45:08.086 EDT) and the start of the gate's ~30-s window (the throw at 12:45:46.384 EDT). Quote the `recordSubsystem` timings K-1's boot shows, and claim nothing about the Pi.
- **Windows desk:** no CRLF into sources; `-Xlint:all -Werror`; no `@SuppressWarnings`.

## §10 Coder pushback welcome
- On the hint, if P-1's unhinted plans already use the index at every bound: the hint stays, for the loud failure, but say so.
- On the gate's progress signal, if `SubscriberSnapshot.checkpoint` does not move during REPLAY as AMD-38 says: name the signal that does.
- On an absolute ceiling for the gate: the hub's default is none, per Nick's words; the packaged unit's start timeout is the outer bound.
- On where the merge lives.
- On K-1's store size, if a boot on 50 × N rows is slow in CI: name the time, and never weaken K-2 or R-3.
- On any §0b row that reads differently at `409547c`.

## §11 Out of scope
- **The bus** (`core/event-bus/`), the state projection and `awaitProjectionLive()`. The bus's overflow recovery (`B/ReplayDriver.java:131`–`:138`) re-applies the rows after the last written checkpoint (≥ H after this unit) through `onEvent`; each apply is idempotent (`RegistryProjection.java:92`–`:96`, `:118`–`:122`, `:154`–`:157`, `:190`–`:192`), and `applyDeviceRemoved`'s early return on an absent device (`:190`–`:192`) skips the entity cascade on a re-applied suffix — pre-existing at `409547c`, unreachable for this subscriber after T1 (its REPLAY spans (H, tail]; the window holds 10,000, `B/EventBusConfig.java:86`). Named here; not changed.
- **AMD-103's recovery-card projection and AVAIL-API-1.** They REUSE this mechanism later (AMD-103 R-F, path (b)); nothing here anticipates them.
- **The Pi's cleared-cache cold start** (`sync; echo 3 | sudo tee /proc/sys/vm/drop_caches`). That belongs to the bench packets: dry-run #1 records it on `37f05a9` as an expected exit 99, and BC10 records it on this unit's sha as a PASS.
- **The rest:** the startup-failure label · store growth and retention (D-v104-20 R4) · the packaged unit's start timeout · the restart-after-power-cut decision (D-v104-20 R1).

## §12 Success criterion (binary)
- `./gradlew check` green at T1 and at T2.
- P-1..P-3, R-1..R-5 and K-1..K-3 named with their red, and P-1's unhinted plans quoted.
- K-4 present and SKIPPED without its property.
- G-1..G-3 in T2 only.
- `core/event-bus/` absent from both diffs; no module-info change.
- The survey (§6) at its post-unit counts, and the MODULE_CONTEXT rows written.
- `tree1:` and `tree:` are the last two lines.

## §13 Work unit completion (WUCP Phase 1)
- The return as §0 names it, with the branch left staged (never committed).
- The register rows named in §5, each with the status it should take at the intake (the hub writes the rows; you name the facts):
  - IR-148: FIXED on landing; deploy-verified at BC10 by one real cold start on the Pi (caches dropped, §11): the evidence is the `registry.projection_rebuilt: rows= head= skipped=0 ms=` line, a `registry.projection_live: devices= entities=` line whose counts equal the preceding warm boot's, and `/health` 200 inside the packaged probe's 90 s.
  - The startup-failure label.
  - P-1's unhinted plans.

## §14 The dispatch (Nick pastes the line below into Claude Code in `~/Desktop/Code/ClaudeFolder/homesynapse-core` — on his word, the one-way-door review's verdict and its edits applied at v105 beat 3)
```
Read ../nexsys-hivemind/context/instructions/2026-10-10_coder-lane_REGISTRY-COLD-1_IR-148_registry-rebuild-from-type-index_LOCAL_desk-coding-instruction.md in full. Execute §0 exactly: date -u first; porcelain empty; the branch; §0b every row re-run and pasted; tests first; ./gradlew check green at T1 and at T2; the return at the path §0 names; stage, never commit, never push; the last two lines tree1: <T1> and tree: <T2>.
```
