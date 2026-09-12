<!--
file: context/instructions/2026-09-12_coder-lane_FIX-2b-ii-B_notify-order_census-truth_coding-instruction.md
purpose: FIX-2b-ii (ii)-B — the census's second face, settled at source by REV-1: notify order is not append order, the checkpoint upsert is not monotonic, so an out-of-order delivery [P+1, P] regresses the persisted checkpoint and TR-1's census reads a delivered head as a miss (samples #11/#12's exact tuple), while the harmful reorder (P skipped by the guard) is invisible to that census. Part B-i (this instruction, ISSUE-READY): make the census read the bus's in-memory max-delivered position, keep the persisted checkpoint monotonic, and print the head's event type on every timeout — the next sample then separates artefact from drop. Part B-ii (⛔ H10 to Nick, §7): the delivery-discipline fix.
audience: the Coder lane (host-side Claude Code in homesynapse-core) · Nick (§7 is the ruling; §8 is the paste) · the hub
state-type: coding instruction
status: RULED at v71 beat 3 (Sat 2026-09-12 ~16:0x CT) — B-ii ruled (b) by Nick (`context/planning/2026-09-12_v71_BUSFIX-b_ruling-of-record.md`); B-i FOLDED into BUS-ORDER-1 (its parts are (b)'s own; not dispatched separately); §8 is retired. Was: ISSUE-READY, part B-i (authored v71 beat 2, Sat 2026-09-12 ~14:1x CT; instrument 2026-09-12T19:08:23Z). ⛔ GATED on the (i) landing: dispatches only on a CLEAN tree at `CORE: LANDED <sha>` and Nick's word `FIX2BIIB: go`. Part B-ii is ⛔ GATED on Nick's ruling (§7). Small: ≤ 6 M + 1 A, ≤ 1 desk-hour.
baseline: the (i) landing sha (the lane STOPs if `git log -1 --oneline` is still `ff1a6e1` or the tree is not clean).
-->

# FIX-2b-ii (ii)-B — notify order, the checkpoint's monotonicity, the census's truth

## §0 The lane contract
- **Baseline** the (i) landing sha on `main`, tree clean. Java slot; no other lane on the Java path-domain (D4). `date -u` first for every stamp.
- **Return** `../nexsys-hivemind/context/audits/2026-09-12_FIX-2b-ii-B_return.md`, §0 card first, ≤ 12 KB (a ceiling, not a target), last line `RETURNED <path> <bytes>`. The instrument beside every claim.
- **Hands.** The lane writes the working tree and the return; never `git add`, `git commit` or `git push`.
- **Shape.** Tests first. Zero change to delivery semantics in B-i (what is offered, skipped or delivered stays as it is); B-i changes what is RECORDED and what the census READS.

## §1 What this implements (the mechanism, at source — REV-1 F2–F4, `context/audits/2026-09-12_REV-1_second-read_return.md`)
1. `NotifyingEventPublisher.publish` (`lifecycle:44–:47`) appends, then calls `bus.notifyEvent(P)` on the publisher's own thread, with no lock across the pair; two publishers' notifies therefore reach a subscriber in either order.
2. `liveLoop` (`InProcessEventBus:557–:566`) writes `writeCheckpoint(subscriberId, envelope.globalPosition())` after every SUCCESS, in delivery order; `SqliteCheckpointStore.UPSERT_SQL` (`:91–:95`) is `INSERT OR REPLACE`, so delivering `[P+1, P]` leaves the persisted checkpoint at `P` — a regression, both delivered.
3. `BusPositionCensusIT` (`:284–:290`) scores `delivered` as `position <= snapshot.checkpoint()`. After (2) it reports `missed=1 first_missed=P+1` for a subscriber that delivered everything — the tuple of samples #11 and #12 (`automation_engine matched=24 delivered=23 missed=1 first_missed=24 checkpoint=23`). The opposite case — `P+1` delivered before `P`'s notify arrives, so `notifyEvent`'s guard (`:371–:373`) skips `P` for good — scores as `delivered` and is invisible; since (i) it emits `NOTIFY_SKIPPED_LIVE`.
4. Neither sample's XML names the event type at the head (183, 24); the timeout text prints positions only (REV-1 F1).

B-i makes three things true: the persisted checkpoint never regresses; the census reads the bus's in-memory max-delivered position and prints the persisted one beside it; every timeout prints the head's event type and the three positions under it.

## §2 Files (exact) — part B-i: ≤ 6 M + 1 A
| # | M/A | Path | Change |
|---|---|---|---|
| 1 | M | `core/event-bus/src/main/java/com/homesynapse/event/bus/SubscriberRuntime.java` | `private final AtomicLong maxDelivered = new AtomicLong(-1L)`; `boolean recordDelivered(long position)` — CAS-max; returns `true` when it advanced. |
| 2 | M | `core/event-bus/src/main/java/com/homesynapse/event/bus/InProcessEventBus.java` | `liveLoop` (`:557–:566`): `if (runtime.recordDelivered(pos) && !atomicCheckpoint) writeCheckpoint(...)` — the write happens only when the max advanced (the checkpoint becomes monotonic; a lower late delivery is recorded in memory, not persisted). **`public long lastDelivered(String subscriberId)`** on the concrete class only (the `abandon()` precedent — not on the `EventBus` interface): the runtime's `maxDelivered`, or `-1` for an unknown id. |
| 3 | M | `core/event-bus/src/main/java/com/homesynapse/event/bus/TransitionCoordinator.java` | the FIX-1b per-delivery checkpoint write (its SUCCESS path) goes through the same `recordDelivered` rule. |
| 4 | A | `core/event-bus/src/test/java/com/homesynapse/event/bus/NotifyOrderTest.java` | **T1 (red at baseline):** a LIVE subscriber with `InMemoryCheckpointStore`; offer `[P+1, P]` (both `notifyEvent` calls before the loop consumes — park the loop or offer under the test's own ordering as `DeliveryAnomalyEmissionTest` does); await both deliveries; assert the persisted checkpoint is `P+1` (baseline: `P`) and `lastDelivered` is `P+1`. **T2 (green-by-construction, disclosed — documents the surviving hazard):** deliver `P+1` (checkpoint `P+1`), THEN `notifyEvent(P)`: assert one `NOTIFY_SKIPPED_LIVE` anomaly and that `P` was not delivered — the B-ii row this test is the red for. |
| 5 | M | `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/BusPositionCensusIT.java` | `delivered := position <= lastDelivered(subscriberId)` (the concrete bus reached the way `subscribers()` is reached today — STOP gate 3); the token line keeps TR-1 §3's five keys and its readings, and gains ` delivered_max=<D>` beside ` checkpoint=<C>`. `timeoutDiagnostic` gains, after the FIX-2b-i reading and before `automation.handoff_census`, `bus.head: position=<H> type=<eventType>` and three `bus.tail: position=<H-k> type=<…>` lines (k = 1..3; read from the store the way `events()` reads it). |
| 6 | M | `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/BusSoakIT.java` | only if its timeout call sites need the new arguments (the FIX-2b-ii (i) shape: one shared static). |
| 7 | M | `core/event-bus/MODULE_CONTEXT.md` | `SubscriberRuntime` + the accessor; the monotonic rule; the T2 hazard stays open until B-ii. |

`module-info.java`: zero change in both modules (no new edge; `AtomicLong` is `java.base`). The lane confirms with `git diff --stat -- '*module-info.java'` = empty.

## §3 STOP gates
1. Tree not clean, or HEAD still `ff1a6e1` (the (i) landing has not happened) → STOP.
2. `git grep -n 'writeCheckpoint(' -- core/event-bus/src/main` finds a third production write site beyond `liveLoop` and `TransitionCoordinator` → STOP, name it (the rule must cover every site or none).
3. The census IT cannot reach the concrete `InProcessEventBus` (grep how `subscribers()` is obtained: `HomeSynapseCore` accessor vs the `EventBus` interface) → STOP with the two options: a `HomeSynapseCore` accessor for the concrete type, or `SubscriberSnapshot` 7 → 8 fields (`lastDelivered`) — the latter touches an exported record; the hub rules.
4. `SubscriberRuntime` is constructed in a testFixtures stub (`MinimalEventBusStub`?) whose shape a contract test pins → include it in the Files table as `[INFO]`.

## §4 Predictions (adjudicate first)
- P1 (red-first): T1 fails at baseline with the persisted checkpoint = `P` (`INSERT OR REPLACE`, delivery order `[P+1, P]`). Not green-by-construction.
- P2: `./gradlew :core:event-bus:test :lifecycle:lifecycle:test --rerun` green; `-Werror` clean; the tagged pair green with `bus.position_census … delivered_max=` printed; `check` green on the push.
- P3 (the next `bus-soak` red's shape): the census line for `automation_engine` shows `missed=0 … checkpoint=<H-1> delivered_max=<H>` → the #11/#12 shape WAS the reorder artefact (closed by B-i); `missed=1` with `delivered_max < H` → a real miss, and `bus.head:` names the event.
- P4: `bus.head:`/`bus.tail:` print on every timeout; the soak's 20/20 green prints none.

## §5 What to watch out for
- The paste-block of record: **Tests must inject `Clock`.** Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` in this module's test code. Use `Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC)` injected via constructor/`@BeforeEach`. **Enforcement reach:** `NO_DIRECT_TIME_ACCESS` runs from `com.homesynapse.app`'s test classpath, so it mechanically catches PRODUCTION code in every non-whitelisted module (plus app's own tests) — it does **not** scan this module's test source set. Clock-injection here is a self-enforced project convention that PM review, not `./gradlew check`, enforces.
- The atomic-checkpoint subscriber (`state_projection`, AMD-45 §2.2) keeps its own write path; `recordDelivered` is still called for it (the census reads the max), the bus-side write stays skipped.
- `maxDelivered` is per runtime activation; a SUSPENDED → REPLAY re-bootstrap creates no regression (REPLAY starts at the persisted checkpoint, which is now ≤ the max by construction).
- LTD-11: no `synchronized`; the CAS loop is the pattern (`AtomicLong.accumulateAndGet(pos, Math::max)` and compare).
- Nothing in B-i changes what a subscriber receives. The reorder's real drop (T2) stays until B-ii; say so in the return.

## §6 Out of scope
The guard's behavior; the offer path; `SqliteCheckpointStore`'s SQL; anything in `core/automation`; part (i)'s tokens; `web-ui/`.

## §7 Part B-ii — the delivery-discipline fix (⛔ H10 to Nick; not the lane's until ruled)
```
ESCALATION TO NICK
Task: FIX-2b-ii (ii)-B-ii — close the notify-reorder drop path (REV-1 F3/F4; kind NOTIFY_SKIPPED_LIVE)
Question: which discipline closes it?
Options:
 (a) LIVE offers unconditionally (the guard kept for passive/TRANSITION) + the monotonic checkpoint (B-i). Cost: ≤ ½ desk-day. Risk: a position drained during TRANSITION and notified after the flip to LIVE is delivered TWICE; for command_issued that is a double actuation unless the loop dedups — a recent-positions set per runtime, more state on the hot path. Buys: the drop closed cheaply.
 (b) Store-driven, in-order delivery: the pending queue becomes a wake-up; on wake the LIVE loop pages the store from maxDelivered+1 to the head (the REPLAY discipline, already the code's own model) and delivers in position order through the existing filter and supervisor. Cost: 1–2 desk-days incl. a design note (liveLoop, TransitionCoordinator's hand-off, the FIX-1b retry folds into the page read). Risk: a redesign of the LIVE path a week before EXPLAIN-114a; needs its own soak samples. Buys: no order dependence, no guard, no duplicate, TR-1's census exact by construction — the class removed, not patched.
 (c) B-i only for now; decide (a)/(b) on the first sample that shows delivered_max ≠ checkpoint or a NOTIFY_SKIPPED_LIVE line. Cost: nothing. Risk: the drop path stays open in the household meanwhile.
PM recommendation: (b), chartered as its own WU after B-i lands and before EXPLAIN-114a's dispatch — the drop is proven at source (F3), it needs only two concurrent publishers (the run VT and the integration always are), and it is OR-BUS-SILENT-DROP's named mechanism; (a) trades one silent drop for a double actuation.
Refutable-by: T2 never firing across the next ten bus-soak samples AND REPRO-1 at K=200 under two carriers — then (c) is the cheaper truth and (b) waits for the R-5 floor.
Blocking: no — B-i, EXPLAIN-114a's authoring, HERO-1c and R-4c proceed; only B-ii's dispatch waits on the word.
```
Words: `BUSFIX: a` · `BUSFIX: b` · `BUSFIX: c`.

## §8 Nick's paste (a host-side Claude Code session in `homesynapse-core` on `main`, AFTER the (i) landing, tree clean)
```
Invoke the nexsys-coder skill. Execute ../nexsys-hivemind/context/instructions/2026-09-12_coder-lane_FIX-2b-ii-B_notify-order_census-truth_coding-instruction.md — PART B-i ONLY (§2 rows 1–7; §7 is a ruling, not yours). date -u first. STOP if the tree is not clean or HEAD is still ff1a6e1. Tests first (§2 row 4 T1 red at baseline, then green; T2 green-by-construction, disclosed). Never run git add, git commit or git push. Return: ../nexsys-hivemind/context/audits/2026-09-12_FIX-2b-ii-B_return.md — §0 card first (P1–P2, the census from git status --porcelain, the module-info diff-stat = empty), ≤ 12 KB, last line RETURNED <path> <bytes>.
```
