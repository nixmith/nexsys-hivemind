<!--
file: _scratch/v104/b4/REGISTRY-COLD-1_independent-review_v1.md
purpose: independent one-way-door review of the draft coding instruction REGISTRY-COLD-1 v1 -- every claim tested against the code at the bytes; verdict, graded questions, findings, exact edits
draft reviewed: _scratch/v104/b4/REGISTRY-COLD-1_instruction_v1.md -- 34,472 B, md5 0ebebee24c9af9f001d96e4b526c8125 (asserted before reading)
sources: homesynapse-core HEAD 409547c (porcelain 0); homesynapse-core-docs HEAD 5e8eb8b; _scratch/v104/b2/nick_1439_words_verbatim.txt; _scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_hs-dev-1_startup-failure.txt
reviewer: REVIEW-RC1, independent (did not see the drafting); read-only everywhere except this file
started: 2026-10-10 22:22 UTC
-->

# REGISTRY-COLD-1 (instruction v1) -- independent one-way-door review

## §0 Verdict

**READY-WITH-EDITS** — **1 BLOCKING · 10 NON-BLOCKING** findings; **17 edits** in §3 (E1–E15, with E7 and E15 split in two), every one mechanical (OLD occurs once; checked by script; applied in memory, the result is 39,921 bytes). Dispatchable once E1–E3 and E15 (the blocking set) are folded; the rest make the text exact. The shape Nick ruled holds at the bytes: H from `latestPosition()` under one write connection and AUTOINCREMENT, the four-way merge reproduces the bus's type-only filter in position order, REG-INV-1 and the census are untouched because the rebuild enters at `onEvent`, nothing in the bus assumes a 0 checkpoint, a rollback to `409547c` overwrites H with 0 at its next boot. The nine questions: Q1 HOLDS · Q2 HOLDS · Q3 HOLDS · Q4 IMPRECISE · Q5 HOLDS · Q6 IMPRECISE · Q7 WRONG (one place) · Q8 IMPRECISE · Q9 HOLDS. All 23 §0b rows re-ran as written.

- **F1 BLOCKING** — §4.2 rules "Exceptions propagate" while saying the arms "all behave as under the bus". The bus's supervisor PARKS a `RuntimeException` from `onEvent` and continues, SUSPENDing at the fifth in 10 min (`SubscriberSupervisor.java:52`, `:55`, `:97–:135`). The thrower exists (`RegistryProjection.java:83–:84`, an enum name unknown to this build — a store a newer build wrote): today that store boots degraded; under the draft it exits 99. K-2's "old way" does not model PARKED either. E1–E3, E15 mirror the supervisor (WARN, skip, count, throw at five); the alternative — the tightening — is Nick's to rule and E1 says what then changes.
- **F2 NON-BLOCKING** — the happens-before edge (`Thread.ofVirtual()…start`, `InProcessEventBus.java:426–:428`) and the write's durability (`PlatformThreadWriteCoordinator.java:69–:90`, `future.get()`) are unnamed (E4, E5).
- **F3 NON-BLOCKING** — `forTypes` is a type-only filter (`SubscriptionFilter.java:93`); the throw-on-`false` is right for that reason, which the text should carry (E6).
- **F4 NON-BLOCKING** — two javadocs that become false (`RegistryProjectionSubscriber.java:31–:33`, `:47`) are not in the edit list; the comment block is `:612`–`:620` (E7a, E7b).
- **F5 NON-BLOCKING** — the outer bound has numbers: `homesynapse.service:54` `--timeout 90`, `:61` `TimeoutStartSec=120`; a moving-but-slow replay under the unit fails without a `startup_failed` line (E8).
- **F6 NON-BLOCKING** — `registryProjectionMode()` has one reader (`:1502`); "stays for its other readers" is wrong (E9).
- **F7 NON-BLOCKING** — P-1's ≥ 100k-row fixture through `append` is CI cost without planner evidence (IR-40's probe: row count did not move the choice, `…PlanTest.java:146–:150`); the unbound case is missing (E10).
- **F8 NON-BLOCKING** — K-4 must say the source is a closed file and the copy lands in a `@TempDir` (E11).
- **F9 NON-BLOCKING** — §13's BC10 row names no evidence for the cold start (E12).
- **F10 NON-BLOCKING** — the overflow re-application is idempotent per apply but not across the tombstone's cascade (`RegistryProjection.java:190–:192`); pre-existing, unreachable after T1; §11 should name it (E13).
- **F11 NON-BLOCKING** — the ArchUnit reach claim overstates: `LT/` tests are not scanned (`HomeSynapseArchRules.java:362–:366`) (E14).

## §1 The nine questions

Every §0b row (1–23) was re-run at `409547c` and holds as written (porcelain `0`; the 23 instruments printed the 23 "Found" cells byte for byte — row 6's four apply lines `:87 :89 :90 :97`, row 7's V003 `DROP INDEX IF EXISTS idx_events_subject` `:47`, row 22's `4` and `:168`). Nick's words in §1 match `nick_1439_words_verbatim.txt` (the list flattened; nothing dropped). IR-148's two intervals are right: 12:43:09.158 → 12:43:53.987 EDT = 44.8 s; 12:45:08.086 → 12:45:46.384 = 38.3 s (`startup-failure.txt:60–:63`, `:30–:33`).

| Q | result | instrument | what it printed (line-cited) |
|---|---|---|---|
| Q1 — the boundary: lose or double a row | **HOLDS** | `SqliteEventStore.java:244` `LATEST_POSITION_SQL`, `:725–:735` `latestPosition()`; `DatabaseExecutor.java:23–:48` (one write connection, N read connections, `journal_mode = WAL` `:446`); `V001…sql:29` AUTOINCREMENT; `ReplayDriver.java:111`, `:131–:138`, `:145`, `:170–:172`; `RegistryProjection.java:86–:200` | `latestPosition()` is one `SELECT COALESCE(MAX(global_position), 0)` on a read connection: under WAL it sees every committed row. SQLite serializes write transactions (one at a time, WAL included) and the executor owns ONE write connection (`:23–:30`, `:337` "single-writer contract"), so an in-flight append commits after H with positions > H (AUTOINCREMENT never reuses, `V001…sql:29`). The rebuild's cursors stop at the earliest envelope `> head` (§4.2); the bus starts at `readCheckpoint` = H (`ReplayDriver.java:111`) and pages `readFrom(H, 500)` (`:145`) — every row > H is delivered, whether appended before or after `subscribeRuntime`. No row is in both halves and none in neither. **Overflow recovery** (`:131–:138`) re-reads the persisted checkpoint (H, or a later cadence write) and re-pages from it, so rows (checkpoint, X] are re-applied through `onEvent`. Each apply is idempotent: upsert-by-equality (`RegistryProjection.java:92–:96`, `:118–:122`), present → `true` (`:154–:157`), absent device → return (`:190–:192`). The one non-idempotent shape is a re-applied `entity_registered` for a device whose tombstone was already applied: the tombstone's re-apply returns early on the absent device (`:190–:192`) and skips the cascade, leaving the entity. Pre-existing at `409547c` (today's overflow restart from a cadence checkpoint has the same shape); unreachable for this subscriber after T1 — its REPLAY spans (H, tail] and the window holds 10,000 (`EventBusConfig.java:86`). Named, not changed (F10). |
| Q2 — the order | **HOLDS** (one clause to make exact) | `ReplayDriver.java:145`, `:180–:200`; `SubscriptionFilter.java:91–:94` (`forTypes`), `:129–:143` (`matches`); `SqliteEventStore.java:808–:870` (`fromRow`; the envelope's `eventType` is the row's string `:821`, the payload `codec.decode` `:854`) | The bus delivers, in `global_position` order, every paged row for which `filter.matches(envelope)` (`:184`). For `forTypes` the filter is TYPE-ONLY: `minimumPriority = DIAGNOSTIC` ("accepts all priorities") and `subjectTypeFilter = null` (`:93`), so `matches` reduces to `eventTypes.contains(envelope.eventType())` (`:132`). A four-way merge by `globalPosition()` over the four typed reads yields exactly that sequence: positions are unique (PK), gaps (a retention hole) change nothing, and a `DegradedEvent` row keeps its `event_type` column (`:821`) so the typed read returns it and both paths hit the same WARN arm (`RegistryProjectionSubscriber.java:103–:110`). Because the filter is type-only, "a typed read that returns another type throws" is exactly right today; the text should say WHY a `false` is a type mismatch (F3). |
| Q3 — REG-INV-1, the census, the arch rules | **HOLDS** | `AMD-99…md:57` (REG-INV-1); `RegistryApplyCensusTest.java:49–:54`, `:100–:116` (`getMethodCallsFromSelf` on `apply*` targets); `HomeSynapseArchRules.java:98–:111` (clock), `:143–:160` (direction), `:191–:204` (filesystem), `:218–:223` (internal), `:410–:425` (mutators); `HomeSynapseArchRulesTest.java:24`; `module-info.java:22,:34,:35` | REG-INV-1 reads "at boot the registries are reconstructed by replaying those events … through a single projection-apply function" — the rebuild replays the four types' envelopes through `onEvent` → the same four `projection.apply*` sites; only the read changes. The census counts CLASSES whose bytecode calls `apply*` on `RegistryProjection` (`:109–:111`): `HomeSynapseCore` calls `onEvent`, not `apply*`, so the set stays the three (`:49–:54`). A lambda compiles to a synthetic method of the SAME class; only an anonymous/inner class would mint a `$1` — the draft's caution is safe. Mutators: only `RegistryProjection` calls them (`:410–:425`) — unchanged. Direction (`:143–:160`): lifecycle → persistence/event is the allowed way. Clock (`:98–:111`): `Thread.sleep` is not in the rule; `nanoTime` is (`:108`). Modules: `lifecycle` already `requires transitive` `event`, `persistence`, `event.bus` — `EventStore`, `SubscriberSnapshot` resolve. |
| Q4 — the bus hand-off | **IMPRECISE** (nothing assumes 0; the happens-before edge is unnamed) | `ReplayDriver.java:111–:114`, `:121–:122`; `SubscriberRuntime.java:41`, `:49`, `:239` (`cursor` CAS-max); `TransitionCoordinator.java:115–:173`, `:189–:191`; `InProcessEventBus.java:396–:430` (`subscribeRuntime`), `:630–:660` (`deliverStep`), `:766–:773` (`buildSnapshot`); `SubscriberSupervisor.java:97–:145`; `SqliteCheckpointStore.java:148–:185`; `PlatformThreadWriteCoordinator.java:69–:90` | **Checkpoint:** the driver reads it once (`:111`), seeds `lastReplayedPosition` and `advanceCursor` (`:112–:114`, a CAS-max from 0 — any H is fine). The tail write is `currentPosition > 0L` (`:170`): H > 0 writes, H = 0 (empty store) writes nothing — today's behaviour. BUS-ORDER-1's cursor starts at the checkpoint (`:114`) and the drain pages `readFrom(cursor, …)` (`TransitionCoordinator.java:189–:191`). The DLQ and the supervisor are built fresh per registration (`InProcessEventBus.java:401–:404`) and read no checkpoint. `onCaughtUp` fires once after the LIVE CAS (`:152–:156`). Nothing compares the checkpoint to 0. **Thread:** `onEvent` runs on `main` during the rebuild and on `hs-sub-registry_projection` after. The happens-before edge is `Thread.ofVirtual()…start(...)` inside `subscribeRuntime` (`InProcessEventBus.java:426–:428`): all of `main`'s writes before the call — the registries' contents, `lastAppliedPosition` (also `volatile`, `RegistryProjectionSubscriber.java:57`) — are visible to the new thread. The checkpoint is committed at `writeCheckpoint`'s return (`submit` blocks on `future.get()`, `PlatformThreadWriteCoordinator.java:69–:90`), and the bus's read runs a new read transaction on a read connection (`SqliteCheckpointStore.java:151–:163`), which under WAL sees it. The draft states the order (§4.3) but names neither edge (F2). |
| Q5 — the SQL hint | **HOLDS** (the fixture's size is cost without evidence) | `V001…sql:58` `idx_events_type ON events(event_type, global_position)`; `SqliteEventStore.java:212–:214`, `:235–:241`, `:662–:684`, `:768–:779`; `git grep readByType(` (3 lines in `src/main`); `SqliteEventStoreTimeRangePlanTest.java:144–:171`, `:236–:251`, `:258–:280` | The index's key is `(event_type, global_position)`: an equality on the leading column and a range on the second is the index's own order, so `ORDER BY global_position` costs no sort, and `INDEXED BY` cannot make the statement unplannable. The page read selects every column (`USING INDEX`); the probe selects `1` (`USING COVERING INDEX`) — the draft allows both. Callers: `StandardExplanationService.java:1063` (the one `src/main` caller) and the REST fakes/tests, which do not read the constant. A dropped index fails at prepare with `no such index` — the hasMore probe runs only on a full page (`:677–:679`), so P-3 must prepare the probe's constant directly, as the form's T3 does for its statement. **The bounds:** IR-40's own probe recorded that the row count (0 or 100k) and the absence of `sqlite_stat1` did NOT move the choice; the bound `LIMIT` did (`…PlanTest.java:146–:150`). So the bounds that matter are the LIMIT values and the unbound case, which P-1 has (1, 500, 10,000; add unbound, the form's `UNBOUND`); the ≥ 100,000-row table through `append` is CI cost for no planner evidence (F7). |
| Q6 — the gate (T2) | **IMPRECISE** (sound signal; the outer bound unnamed) | `ReplayDriver.java:126–:127`, `:180–:200`, `:203–:214`, `:220–:225`; `InProcessEventBus.java:650–:653`, `:769`; `HomeSynapseCore.java:1455–:1526`; `distribution/systemd/homesynapse.service:54`, `:61` | The snapshot's `checkpoint` IS the persisted one (`buildSnapshot` → `readCheckpoint`, `:769`). For `atomicCheckpoint = false` the driver writes it when `eventsSinceCheckpoint ≥ 200` MATCHING events or `≥ 2 s` since the last write (`:220–:225`), checked after each page (`:203`), and the value written is `currentPosition` — advanced past EVERY paged row (`:195`), matching or not. So during REPLAY the checkpoint moves at least every ~2 s + one page read while pages keep coming; the mode flips (COLD→REPLAY→TRANSITION→LIVE) count as progress too. A healthy replay shows no progress for ~30 s only if ONE `readFrom(…, 500)` page takes 30 s — a PK-range page, not a log walk. After T1 the registry's REPLAY spans (H, tail]. Sound. Today's gate already polls `eventBus.subscribers()` every 20 ms (`:1502`, `:1521`), so the per-poll `readCheckpoint` is not new load. **The ceiling:** the packaged unit's `health-probe.sh --wait --timeout 90` (`:54`) and `TimeoutStartSec=120` (`:61`) are the outer bound, and Nick's words name 90 s; under the unit a replay that keeps moving past ~90 s ends as a unit start failure with no `lifecycle.startup_failed` line. The draft names neither number (F5). |
| Q7 — the tests | **WRONG** in one place (K-2's "old way" and §4.2's exception rule are not the bus's path); the rest hold | `SubscriberSupervisor.java:52`, `:55`, `:97–:135`; `RegistryProjection.java:83–:84`; `ReplayDriver.java:180–:196`; `RealCoreFixture.java:469–:489`; `BootOrderingGateIT.java:52`, `:102–:108` | **P:** R-3 counts calls and envelopes RETURNED (zero `readFrom`; `readByType` on four types; 40 back) — the API-path guard; P-1 pins the PLAN, which is the only instrument that sees rows SCANNED (a rowid walk returns the same 40). Together they are the rows-read guard; neither alone is. **K-2's old way** is the driver's loop shape (`readFrom(0, 500)` pages, `filter.matches`, in order — `:145`, `:184`) EXCEPT the delivery: the bus calls `supervisor.deliver` (`:186–:187`), which catches a `RuntimeException` from `onEvent`, parks the row in the DLQ, counts a crash and CONTINUES; it SUSPENDs only at the fifth crash in a rolling 10 min (`SubscriberSupervisor.java:52`, `:55`, `:128–:135`). K-2 as written calls `onEvent` bare, and §4.2 says the rebuild's exceptions PROPAGATE and fail the boot. So on a store with one registry row whose apply throws — `RegistryProjection.java:83–:84`: "an enum name unknown to this build (fail loudly — the bus's DLQ path handles it)", the shape of a store written by a newer build — today's Core boots with the row parked; after this unit it exits 99. The draft's §4.2 says the arms "all behave as under the bus"; this one does not (F1). **K-4:** the copy discipline is right for a closed file; it must say the source is one no running Core has open (a file copy of an open WAL database is not a snapshot) and that the copy lands in a `@TempDir` (~830 MB) (F8). **K-1:** `BootOrderingGateIT` counts lines by the prefix `registry.projection_live: ` (`:52`, `:102`), so the new `registry.projection_rebuilt:` line cannot break T3. **G:** consistent with §4.4. |
| Q8 — the premises and the scope | **IMPRECISE** (all 23 rows hold; three pins unnamed; the split is clean) | the 23 instruments; `RegistryProjectionSubscriber.java:29–:33`, `:46–:47`; `HomeSynapseCore.java:612–:620`, `:1502`, `:1517`; `lifecycle/lifecycle/MODULE_CONTEXT.md:21`; `git grep registry.projection_live`; `HomeSynapseArchRules.java:362–:366` | Unnamed: (i) the class javadoc `RegistryProjectionSubscriber.java:31–:33` ("the composition root resets this subscriber's checkpoint to 0 BEFORE registration, so every boot replays the full registration history") and `:47` ("the checkpoint key the boot reset targets") become false; the file is M in §3 but §4.2 does not name them (F4). (ii) The comment block is `:612`–`:620`, not `:612`–`:619` (`:620` closes the sentence). (iii) `registryProjectionMode()` has ONE reader (`:1502`); "stays for its other readers" is wrong (F6). (iv) The test-clock paste-block's reach claim: the suite scans production classes and the app module's own test tree only (`:362–:366`; `@AnalyzeClasses(packages = "com.homesynapse")`), so for `LT/` it is a convention (F11). Consumers of `registry.projection_live` in this repo: `BootOrderingGateIT` (4), `ProcessRestartIdentityIT:136–:137`, `:163`, `:168`, `build.gradle.kts:79` (the logback capture), the MODULE_CONTEXT rows `:3`, `:21` — all listed or covered by §8; `lifecycle/lifecycle/MODULE_CONTEXT.md:21` carries the "resets the subscriber checkpoint to 0 BEFORE `subscribeRuntime`" sentence §8 annotates. The §6 counts re-ran as stated (1 · 2 lines · 3 · 0). **T1/T2:** clean — T2 adds `RegistryGate`, its test and the delegation in `awaitRegistryProjectionLive()` only; nothing in T1 depends on T2. |
| Q9 — the door | **HOLDS** (one gate row to make specific) | `HomeSynapseCore.java:622–:623`; the migrations (none added); §13 | **Rollback to `409547c`:** the old code writes `0L` at Step 3.1 before subscribing (`:622–:623`), so a persisted H is overwritten at the next old boot — the checkpoint carries no debt. No migration, no schema, no index change: the hint is a string in the new code only. The one new one-way shape is F1's: with "propagate", a store that a newer build wrote (a new enum name in a registration payload) stops booting on this code where `409547c` boots degraded — the mirror edit (E1) removes it. **BC10's precondition:** K-4 on BACKUP-1's copy proves equality on the real rows as of the backup; the cold start (caches dropped) proves the timing on the real card. That is the right pair; the second half needs its evidence named — the `registry.projection_rebuilt` line and `devices= entities=` equal to the preceding warm boot's, `/health` 200 inside the probe's 90 s (F9). |

## §2 Findings

### F1 — BLOCKING — §4.2 / §7 K-2: "Exceptions propagate" is not the bus's path, and the draft says it is
`SubscriberSupervisor.java:97–:135`: `subscriber.onEvent(envelope)` inside `try`; `catch (RuntimeException e)` → `dlq.park(deadLetter)` (`:122`), `recordCrash(now)` (`:125`), SUSPENDED only when `crashCount() >= CIRCUIT_BREAKER_THRESHOLD` (`:128`; `= 5` at `:52`, rolling `Duration.ofMinutes(10)` at `:55`), else `return DeliveryResult.PARKED` (`:135`). `ReplayDriver.java:186–:187` delivers through it and continues on PARKED. The draft's §4.2 says the WARN arms, the orphan WARN and `lastAppliedPosition` "all behave as under the bus", then rules "Exceptions propagate: the boot fails inside Step 3.1". `RegistryProjection.java:83–:84` names the real thrower: `IllegalArgumentException if the payload carries an enum name unknown to this build (fail loudly — the bus's DLQ path handles it)`. A store written by a newer build and booted by this one (a rollback) is that case: `409547c` boots with the row parked; the draft's rule exits 99. K-2's "old way" (bare `onEvent`) does not model PARKED either, so the comparison would throw rather than compare. The choice is unmade and unnamed; it changes the boot's failure surface and the rollback story. Edits E1–E3, E15 mirror the supervisor (WARN, skip, count, throw at five). If Nick rules the tightening instead, E1's last sentence says what then changes.

### F2 — NON-BLOCKING — §4.3: the happens-before edge and the checkpoint's durability are asserted, not named
`InProcessEventBus.java:426–:428`: `Thread vt = Thread.ofVirtual().name("hs-sub-" + …).start(() -> subscriberLoop(subscriberRuntime));` — the edge from `main`'s rebuild to the bus's thread. `RegistryProjectionSubscriber.java:57`: `private volatile long lastAppliedPosition;`. `PlatformThreadWriteCoordinator.java:69–:90`: `submit` returns `future.get()` — the checkpoint row is committed when `writeCheckpoint` returns. `ReplayDriver.java:111` reads it on a read connection in a new read transaction. §4.3 says only "the bus reads it on its own thread after the call". Edits E4, E5 (the read set gains the lines).

### F3 — NON-BLOCKING — §4.2: the filter clause is right for a reason the text does not give
`SubscriptionFilter.java:91–:94`: `forTypes` → `new SubscriptionFilter(Set.of(eventTypes), EventPriority.DIAGNOSTIC, null)`; `:129–:143`: the priority test cannot fail at the DIAGNOSTIC floor and the subject test is skipped on `null`. A `false` from this filter IS a type mismatch, so throwing is exact today; a later tightening of the filter would turn the throw into a boot failure the bus would not have. Edit E6 states the premise.

### F4 — NON-BLOCKING — §4.2 / §4.3: two texts that become false are not in the edit list; one range is off by one
`RegistryProjectionSubscriber.java:31–:33`: `the composition root resets this subscriber's checkpoint to 0 BEFORE registration, so every boot replays the full registration history — the Phase-3 boot rebuild.`; `:47`: `/** The stable subscriber id — the checkpoint key the boot reset targets. */`. `HomeSynapseCore.java:612–:620` is the comment block (`:620` = `// start-of-log per the CheckpointStore contract).`); §4.3 says `:612`–`:619`. Edit E7.

### F5 — NON-BLOCKING — §4.4 / §10: the outer bound exists and has numbers; the draft names neither
`distribution/systemd/homesynapse.service:54`: `ExecStartPost=/opt/homesynapse/libexec/health-probe.sh --wait --timeout 90 --health-path /health`; `:61`: `TimeoutStartSec=120`. Nick's words: "The packaged service waits up to 90 s for `/health`". Under the unit, a registry replay that keeps moving past ~90 s is a unit start failure (the probe's exit 3) with no `lifecycle.startup_failed` line — a different failure signature from exit 99. Edit E8.

### F6 — NON-BLOCKING — §4.4: `registryProjectionMode()` has one reader
`HomeSynapseCore.java:1502`: `if (registryProjectionMode() == SubscriberMode.LIVE) {` is the only call (`grep -n 'registryProjectionMode()'` → `:1502`, `:1517`). After the delegation it is dead unless it becomes the snapshot supplier. Edit E9.

### F7 — NON-BLOCKING — §7 P-1: the ≥ 100,000-row fixture is cost without planner evidence
`SqliteEventStoreTimeRangePlanTest.java:146–:150`: "the table's row count (0 or 100k) and the absence of `sqlite_stat1` did not move the choice (the IR-40 probe)". A stat-less planner does not read the table; the bound `LIMIT` and the unbound case are the variables (the form's `BOUND_MAX_COUNTS` `:152` and `UNBOUND` `:168`). 100,000 `append`s through the write coordinator in a permanent unit test cost CI seconds for no evidence the hint does not already give. The unhinted 100k run the draft asks for ONCE (the register's fact) stays. Edit E10 (unbound added; direct-SQL rows allowed; the cost named as pushback).

### F8 — NON-BLOCKING — §7 K-4: the copy's precondition is unstated
A file-level copy of a WAL database another process has open is not a consistent snapshot (the `-wal` may be mid-frame). BACKUP-1's copy is a closed file; the Pi's live store is excluded by §0 but K-4's own text does not say so; the copy is ~830 MB (`startup-failure.txt`: 828,829,696 B) and should land in a `@TempDir`. Edit E11.

### F9 — NON-BLOCKING — §13: BC10's "one real cold start" names no evidence
§13: "deploy-verified at BC10 by one real cold start on the Pi." The lines that prove it exist after T1: `registry.projection_rebuilt: rows= head= ms=` and `registry.projection_live: devices= entities=` (`RegistryProjectionSubscriber.java:121`), compared with the preceding warm boot's counts, and `/health` 200 inside the probe's 90 s. Edit E12.

### F10 — NON-BLOCKING — §11: the overflow re-application is idempotent per apply, not across the tombstone's cascade
`ReplayDriver.java:131–:138` restarts from `readCheckpoint`; `RegistryProjection.java:190–:192`: `if (deviceRegistry.findDevice(deviceId).isEmpty()) { return; }` skips the entity cascade when the device is already gone, so a re-applied `entity_registered` (device D) followed by the re-applied tombstone of D leaves the entity. Pre-existing at `409547c`; unreachable for this subscriber after T1 ((H, tail] under a 10,000-slot window, `EventBusConfig.java:86`). Out of scope; §11 should say so in one sentence so the intake does not re-derive it. Edit E13.

### F11 — NON-BLOCKING — §7 (the paste-block): the ArchUnit reach claim overstates
`HomeSynapseArchRules.java:362–:366`: "Reach: production classes of every module plus this app module's own test tree (the only test code on this classpath). Non-app TEST code is not scanned". `HomeSynapseArchRulesTest.java:24`: `@AnalyzeClasses(packages = "com.homesynapse")`. The lifecycle tests the lane writes are not scanned; the rule is a convention there. Edit E14.

## §3 The edits, verbatim

Each edit replaces the draft's OLD text, which occurs exactly once in `REGISTRY-COLD-1_instruction_v1.md` (md5 `0ebebee24c9af9f001d96e4b526c8125`; each OLD asserted by `str.count == 1`), with the NEW text. No two OLD texts overlap, so E1–E15 apply in any order. Fences are `~~~~`; the text between them is byte-exact.

**E1** (F1 — §4.2 — the exception rule, the bus's own)

Old:
~~~~
- Exceptions propagate: the boot fails inside Step 3.1 (`initializing = "device-model"`); nothing is swallowed.
~~~~
New:
~~~~
- **A `RuntimeException` from `onEvent` is handled as the bus's supervisor handles it** (`B/SubscriberSupervisor.java:97`–`:135`: the row is parked, the crash counted, delivery continues; SUSPENDED at the fifth crash — `CIRCUIT_BREAKER_THRESHOLD = 5`, `:52`). The rebuild catches it per envelope, logs ONE WARN `registry.projection_rebuild_apply_failed: type={} position={} cause={}`, counts it and continues; at the fifth it throws `IllegalStateException` naming the count and the position — the boot fails inside Step 3.1 (`initializing = "device-model"`). Nothing else is caught: a `readByType` that throws propagates. The reason: a registration row whose apply throws (`RegistryProjection.java:83`–`:84`: an enum name unknown to this build — the shape of a store a newer build wrote) boots the Core today with the row parked; propagating would make that store unbootable on this code, a tightening Nick did not rule. If Nick rules the tightening, this bullet reverts to "Exceptions propagate", R-5 inverts, and §13 names the change for the register.
~~~~

**E2** (F1 — §7 K-2 — the old way models PARKED)

Old:
~~~~
fed in order to a fresh subscriber's `onEvent`)
~~~~
New:
~~~~
fed in order to a fresh subscriber's `onEvent`, a `RuntimeException` from `onEvent` skipping that row as the supervisor's PARKED does)
~~~~

**E3** (F1 — §7 — R-5, the throw arm)

Old:
~~~~
- **R-4:** a registry-type row that fails decode arrives as a `DegradedEvent`, takes the WARN arm (`registry.projection_degraded_event`), and the rebuild does not throw.
~~~~
New:
~~~~
- **R-4:** a registry-type row that fails decode arrives as a `DegradedEvent`, takes the WARN arm (`registry.projection_degraded_event`), and the rebuild does not throw.
- **R-5 THE THROW ARM:** a registry-type row whose `onEvent` throws a `RuntimeException` (a registry stub whose `createDevice` throws for one id) → ONE `registry.projection_rebuild_apply_failed` WARN, that row skipped, every other row applied, the rebuild returns; five such rows → `IllegalStateException` (§4.2).
~~~~

**E4** (F2 — §4.3 — the happens-before edge and the durable write)

Old:
~~~~
- H is read BEFORE the rebuild. The checkpoint is written AFTER the rebuild returns and BEFORE `subscribeRuntime`: the bus reads it on its own thread after the call (§0b row 14). A rebuild that throws never reaches the write.
~~~~
New:
~~~~
- H is read BEFORE the rebuild. The checkpoint is written AFTER the rebuild returns and BEFORE `subscribeRuntime`: the bus reads it on its own thread after the call (§0b row 14). A rebuild that throws never reaches the write. **The happens-before edge** into the bus's thread is the virtual thread's start inside `subscribeRuntime` (`B/InProcessEventBus.java:426`–`:428`, `Thread.ofVirtual()…start(...)`): everything `main` wrote before the call — the registries' contents and `lastAppliedPosition` (also `volatile`, `L/RegistryProjectionSubscriber.java:57`) — is visible to `hs-sub-registry_projection`. **The write is durable at its return:** `SqliteCheckpointStore.writeCheckpoint` (`:167`) blocks on the write coordinator's future (`P/PlatformThreadWriteCoordinator.java:69`–`:90`, `return future.get()`), and the bus's read (`B/ReplayDriver.java:111`) runs a new read transaction on a read connection, which under WAL sees the committed row.
~~~~

**E5** (F2 — §2 — the read set gains the hand-off's lines)

Old:
~~~~
- `B/ReplayDriver.java` `:100`–`:230` and `B/InProcessEventBus.java` `:380`–`:400`, `:460`–`:470` — READ ONLY.
~~~~
New:
~~~~
- `B/ReplayDriver.java` `:100`–`:230`; `B/InProcessEventBus.java` `:380`–`:430` (`subscribeRuntime`; the virtual thread's start `:426`), `:455`–`:490`, `:630`–`:660` (`deliverStep`), `:765`–`:773` (`buildSnapshot`: the snapshot's `checkpoint` is the persisted one); `B/SubscriberSupervisor.java` `:48`–`:145` (the PARKED arm §4.2 mirrors) — all READ ONLY.
~~~~

**E6** (F3 — §4.2 — why a `false` is a type mismatch)

Old:
~~~~
- **Each envelope** passes `subscriptionFilter().matches(envelope)` (`B/SubscriptionFilter.java:129`, the bus's own predicate) — a typed read that returns another type throws — and then goes to
~~~~
New:
~~~~
- **Each envelope** passes `subscriptionFilter().matches(envelope)` (`B/SubscriptionFilter.java:129`, the bus's own predicate; for `forTypes` it is a type-only test — DIAGNOSTIC floor, no subject restriction, `:91`–`:94` — so a `false` IS a type the read should not have returned) — a typed read that returns another type throws `IllegalStateException` naming the type asked and the type returned — and then goes to
~~~~

**E7a** (F4 — §4.2 — the javadocs that become false)

Old:
~~~~
- **Never `projection.apply*` from the new method**
~~~~
New:
~~~~
- **The class javadoc** (`:29`–`:33`: "the composition root resets this subscriber's checkpoint to 0 BEFORE registration, so every boot replays the full registration history") is re-cut to the four steps; `SUBSCRIBER_ID`'s javadoc (`:47`, "the checkpoint key the boot reset targets") becomes "the checkpoint key Step 3.1 writes H to".
- **Never `projection.apply*` from the new method**
~~~~

**E7b** (F4 — §4.3 — the comment block's range)

Old:
~~~~
- The comment block `:612`–`:619` is re-cut
~~~~
New:
~~~~
- The comment block `:612`–`:620` is re-cut
~~~~

**E8** (F5 — §4.4 — the outer bound, with its numbers)

Old:
~~~~
- No absolute ceiling (Nick: *"fail only if the replay stops moving"*): a ceiling is a §10 question, not this unit's.
~~~~
New:
~~~~
- No absolute ceiling (Nick: *"fail only if the replay stops moving"*): a ceiling is a §10 question, not this unit's. The outer bound is the packaged unit's: `distribution/systemd/homesynapse.service:54` `health-probe.sh --wait --timeout 90` (ExecStartPost; `/health` is 200 only once the state projection is LIVE, which waits on this gate) and `:61` `TimeoutStartSec=120`. Under the unit a registry replay that keeps moving past ~90 s ends as a start failure of the unit (the probe's exit 3) with no `lifecycle.startup_failed` line; the bench Core, which runs under no unit, waits as long as the replay moves. The return's §5 names this for the register.
~~~~

**E9** (F6 — §4.4 — `registryProjectionMode()` has one reader)

Old:
~~~~
- `awaitRegistryProjectionLive()` (`:1499`) delegates to it; `registryProjectionMode()` stays for its other readers (grep them).
~~~~
New:
~~~~
- `awaitRegistryProjectionLive()` (`:1499`) delegates to it, passing a supplier built on `eventBus.subscribers()` filtered to `RegistryProjectionSubscriber.SUBSCRIBER_ID` (the lookup `registryProjectionMode()` makes today, `:1517`–`:1526`). `registryProjectionMode()` has ONE reader at `409547c` (`:1502`): it is re-cut as that snapshot lookup or removed, never left dead.
~~~~

**E10** (F7 — §7 P-1 — the unbound case; the fixture's cost)

Old:
~~~~
- **P-1:** `EXPLAIN QUERY PLAN` of `SELECT_BY_TYPE_SQL`, bound with LIMIT 1, 500 and 10,000, on an empty table AND on a table of ≥ 100,000 rows where the queried type is ≤ 1 % → every plan names
~~~~
New:
~~~~
- **P-1:** `EXPLAIN QUERY PLAN` of `SELECT_BY_TYPE_SQL`, bound with LIMIT 1, 500 and 10,000 and unbound (the form's `UNBOUND`), on an empty table AND on a table of ≥ 100,000 rows where the queried type is ≤ 1 % (the rows may go in by direct SQL on the write connection, not `append` — the plan is what is under test, and IR-40's probe recorded that the row count, 0 or 100k, and the absence of `sqlite_stat1` did not move the planner, `PT/SqliteEventStoreTimeRangePlanTest.java:146`–`:150`; if the fixture costs more than ~5 s in CI, say so under §10 and keep the 100k table for the once-only unhinted run below) → every plan names
~~~~

**E11** (F8 — §7 K-4 — the copy's precondition)

Old:
~~~~
- It copies the given file, with any `-wal` beside it, to a temp directory and opens the COPY: opening runs migrations and PRAGMAs, and a backup is never written.
~~~~
New:
~~~~
- It copies the given file, with any `-wal` beside it, to a JUnit `@TempDir` (deleted after the run; the copy is ~830 MB, so the desk needs the space) and opens the COPY: opening runs migrations and PRAGMAs, and a backup is never written. The source must be a file no running Core has open — a file-level copy of an open WAL database is not a consistent snapshot. BACKUP-1's copy is such a file; the Pi's live store is not (§0).
~~~~

**E12** (F9 — §13 — BC10's evidence)

Old:
~~~~
  - IR-148: FIXED on landing; deploy-verified at BC10 by one real cold start on the Pi.
~~~~
New:
~~~~
  - IR-148: FIXED on landing; deploy-verified at BC10 by one real cold start on the Pi (caches dropped, §11): the evidence is the `registry.projection_rebuilt: rows= head= ms=` line, a `registry.projection_live: devices= entities=` line whose counts equal the preceding warm boot's, and `/health` 200 inside the packaged probe's 90 s.
~~~~

**E13** (F10 — §11 — the overflow re-application, named)

Old:
~~~~
- **The bus** (`core/event-bus/`), the state projection and `awaitProjectionLive()`.
~~~~
New:
~~~~
- **The bus** (`core/event-bus/`), the state projection and `awaitProjectionLive()`. The bus's overflow recovery (`B/ReplayDriver.java:131`–`:138`) re-applies the rows after the last written checkpoint (≥ H after this unit) through `onEvent`; each apply is idempotent (`RegistryProjection.java:92`–`:96`, `:118`–`:122`, `:154`–`:157`, `:190`–`:192`), and `applyDeviceRemoved`'s early return on an absent device (`:190`–`:192`) skips the entity cascade on a re-applied suffix — pre-existing at `409547c`, unreachable for this subscriber after T1 (its REPLAY spans (H, tail]; the window holds 10,000, `B/EventBusConfig.java:86`). Named here; not changed.
~~~~

**E14** (F11 — §7 — the ArchUnit reach, as the rule states it)

Old:
~~~~
**Enforcement reach:** `NO_DIRECT_TIME_ACCESS` runs from `com.homesynapse.app`'s ArchUnit suite over every module on the classpath.
~~~~
New:
~~~~
**Enforcement reach:** `NO_DIRECT_TIME_ACCESS` runs from `com.homesynapse.app`'s ArchUnit suite over every module's production classes and the app module's own test tree only (`AT/HomeSynapseArchRules.java:362`–`:366`); `LT/` test code is not scanned, so for this module's tests the rule is a convention the return attests, not an enforcement.
~~~~

**E15a** (F1 — §12 — the test list)

Old:
~~~~
- P-1..P-3, R-1..R-4 and K-1..K-3 named with their red, and P-1's unhinted plans quoted.
~~~~
New:
~~~~
- P-1..P-3, R-1..R-5 and K-1..K-3 named with their red, and P-1's unhinted plans quoted.
~~~~

**E15b** (F1 — §3 — the Files table's row)

Old:
~~~~
| `LT/RegistryProjectionSubscriberTest.java` | M | T1 | R-1..R-4 |
~~~~
New:
~~~~
| `LT/RegistryProjectionSubscriberTest.java` | M | T1 | R-1..R-5 |
~~~~

**Check.** Applying all 17 OLD→NEW pairs in memory to the draft (nothing written): every OLD found once before its replacement and zero times after; the result is 39,921 bytes. The pairs touch §2, §3, §4.2, §4.3, §4.4, §7, §11, §12, §13; §0, §0b, §1, §5, §6, §8, §9, §10, §14 are untouched.

## §4 What you could not verify

Named, not guessed.

1. **The shipped planner's unhinted plan for `SELECT_BY_TYPE_SQL` at each bound.** Not run here (no build, no sqlite-jdbc on this desk). The index's shape (equality on the leading column, range on the second) makes the index range the natural plan; IR-40's rowid walk arose on a RANGE-only predicate. The draft already asks the lane to run and quote the unhinted plans (§7); §10's bullet on the hint covers the likely outcome.
2. **The per-type row counts on `hs-dev-1`'s store and the rebuild's real duration.** On the Pi; K-4 and BC10 produce them. The instrument, read-only: `SELECT event_type, COUNT(*) FROM events WHERE event_type IN ('device_registered','entity_registered','device_removed','capability.added') GROUP BY event_type;`.
3. **Whether anything appends to the log between `Persistence layer started` and Step 3.1 in the shipped boot.** `HomeSynapseCore.java` itself has no `.publish(` call (grep: none); subsystems started in Phase 2 were not traced for publishes. It affects only how many rows the bus replays after H and K-1's `head=` assertion (assert `head` ≥ the seeded head rather than equal, if a Phase-2 publish exists).
4. **SQLite's bound-`LIMIT` re-planning.** The form's comment (`SqliteEventStoreTimeRangePlanTest.java:145–:147`) says the planner "reads a bound `LIMIT ?` on re-prepare and treats it as a fixed limit"; that behaviour of sqlite-jdbc 3.51.3 was not independently verified. P-1 inherits the form's method either way.
5. **The DLQ writer in `subscribeRuntime` is `PersistentDlqWriter.noop()` (`InProcessEventBus.java:401–:402`)** — so a PARKED registration row today leaves no durable record. Read, not traced further; it bears on F1's framing (today's degraded boot is silent except for `dlqDepth`) and is out of this unit's scope.
6. **The bench's readers of `registry.projection_live`** live in `nexsys-bench`, which is not on this desk (§6's last bullet); not checked.
7. **AMD-38's text** was read for the 200 / 2 s values (`AMD-38…md:48`, `:53–:54`), not for its WAL argument; AMD-42 for the "exactly once" `onCaughtUp` (`:21`, `:37–:43`); AMD-45 and AMD-101 were not re-read beyond the code comments that cite them (`ReplayDriver.java:159–:169`, `:113`).
