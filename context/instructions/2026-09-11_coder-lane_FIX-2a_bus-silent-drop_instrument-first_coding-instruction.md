<!--
file: context/instructions/2026-09-11_coder-lane_FIX-2a_bus-silent-drop_instrument-first_coding-instruction.md
purpose: FIX-2a — the INSTRUMENT half of FIX-2 for OR-BUS-SILENT-DROP (the CI-613 class: HeroLoopHardwareFreeIT times out awaiting the On frame; the event is in the store; no subscriber acts; the FIX-1a detector emits nothing). Three test-only deliverables in the lifecycle module: (A) the hero-loop IT's await gains a timeout diagnostic that names every subscriber's mode, checkpoint and DLQ depth beside the store head and the awaited position; (B) TR-1b's position-census IT computes the census of TR-1 §1 in-process after one hero loop and prints the frozen tokens; (C) a bus-soak IT runs K hero loops in one core and reports delivery latency p50/p99 and the anomaly count — the desk's reproduction of the class. No production code. The structural fix (FIX-2b: checkpoint-driven LIVE delivery; an AMD to Doc 01 §3.4) is authored on this lane's reading.
audience: the Coder (a host-side Claude Code session on homesynapse-core at 1e26912; the Java slot) · the hub (audits the return)
state-type: coding instruction
status: ISSUE-READY (authored v70 beat 4, Fri 2026-09-11 ~18:1x CT; instrument 2026-09-11T23:17:30Z). Dispatches on Nick's word `FIX2: go`; the Java slot is free (EXPLAIN-114a is held behind this lane). Nick's paste is §14.
baseline: core `1e26912` (docs(dashboard): HERO-1; the Java is `eabdbb1`'s). Re-verify at issue: `git -C homesynapse-core log -1 --oneline` prints `1e26912`.
evidence: context/audits/2026-09-11_CI-1e26912_red-read_HeroLoop-lifecycle_v70-b2.md (the read of run 34650129654) · context/research/2026-09-07_TR-1_position-census_bench-verb_design_return.md (the census definition, §1; the frozen tokens, §3) · context/audits/2026-09-07_TR-1_intake_two-layer-audit_v67-b5.md §3–§5 (TR1-B2 = DRIVER; TR-1b's shape).
-->

# FIX-2a — OR-BUS-SILENT-DROP, instrument first (lifecycle; test-only)

## §0 The lane contract (read first; the return's §0 mirrors it)
- **`date -u` first.** Every stamp in your return derives from it; CT is UTC−5, re-derived once.
- **Read-set (whole unless a range is named):** this file · `lifecycle/lifecycle/MODULE_CONTEXT.md` §Gotchas (`grep -n '^## Gotchas'` → read to the next `## `) · `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/HeroLoopHardwareFreeIT.java` whole (625 lines) · `core/event-bus/src/main/java/com/homesynapse/event/bus/InProcessEventBus.java` `:316–:345` (`notifyEvent`), `:467–:499` (`subscribers()`), `:525–:592` (`liveLoop`), `:650–:700` (`readLivePosition` and its anomaly kinds) · `core/event-bus/src/main/java/com/homesynapse/event/bus/SubscriberSnapshot.java` `:36–:43` · `core/event-bus/src/main/java/com/homesynapse/event/bus/SubscriptionFilter.java` (the `matches` body and the three factories, `:78–:110`) · `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java` `:555–:562` (the anomaly handler's log grammar), `:620–:640` (the state_projection registration, `atomicCheckpoint = true`), `:730–:740` (the automation_engine registration) · `integration/integration-zigbee/src/testFixtures/java/com/homesynapse/integration/zigbee/ZigbeeHardwareFreeRig.java` `:45–:60`, `:130–:170` (`reportOccupied`, `sentZclFrames`) · the census definition: `context/research/2026-09-07_TR-1_position-census_bench-verb_design_return.md` §1 and §3 (by range).
- **Return path:** `context/audits/<CT filing date>_FIX-2a_return.md`. **Cap: ≤12 KB is a CEILING, not a target; the §0 card is what the hub reads first; a shorter return with the same receipts is a better return.** Its §0 card: the verdict · the census line (`git --no-optional-locks status --porcelain` counted, M/A/D) · the predictions adjudicated FIRST (P1–P4 below, each HELD/SPLIT/FAILED with the artifact line it was read from) · the measurement table (§7) · the deviations by tag (`[REVIEW]` / `[INFO]`) · the Deferred Build Gate line · the `RETURNED <path> <bytes>` line as the LAST line of the file, and printed to Nick as the one line back.
- **The instrument limit:** `./gradlew :lifecycle:lifecycle:test --tests '*HeroLoop*' --tests '*BusPositionCensus*' --tests '*BusSoak*'` and `:lifecycle:lifecycle:compileTestJava` are yours; `./gradlew check` (the app's ArchUnit sweep) is NOT run on your desk — it is owed to CI on Nick's push and named as the Deferred Build Gate in your closeout. Every measurement in §7 names the artifact it is read from.
- **You commit nothing and stage nothing.** Leave the working tree with exactly the Files table's census; Nick's card lands it.
- **Pushback is welcome** (§11); evidence-based pushback that changes a row is `[REVIEW]`; a shape you chose inside the row's freedom is `[INFO]`.

## §1 What this implements
The `1e26912` red (run 34650129654) shows the class at its clearest: the `occupied=true` `state_reported` envelope is in the store (the IT read it back), then ten seconds of silence — no dispatch, no frame at the scripted NCP, no `bus.delivery_anomaly` line although other WARN lines are present. The FIX-1a detector covers `NOTIFY_NOT_VISIBLE`, `LIVE_READ_EMPTY/FAILED/EXHAUSTED` and the TRANSITION reads; the drop the hero loop sees is none of those. Before any structural change, the desk gets three instruments that turn the next red into a reading instead of a timeout:

**(A) The await diagnostic.** `HeroLoopHardwareFreeIT.awaitTrue` (`:607–:615`) throws `AssertionError("timed out awaiting " + what)` and nothing else. It gains a diagnostic: on timeout the message carries the store head, the awaited position when the caller can name one, and one line per subscriber from `core.eventBus().subscribers()` — `subscriberId · mode · checkpoint · dlqDepth · behind = head − checkpoint`. The same text is printed to stdout so the JUnit XML's `<system-out>` carries it beside the `<failure message>`.

**(B) The position census (TR-1b's IT).** After one hero loop, for every subscriber of the manifest (the six ids the composition root registers: `state_projection`, `automation_engine`, `command_dispatch_service`, `pending_command_ledger`, `integration_supervisor`, `registry_projection`) and every position in the store, the census of TR-1 §1: `MATCHED(S,P)` by the subscriber's filter; `DELIVERED(S,P)` := `checkpoint(S) ≥ P` and no DLQ row for `(S,P)`; `MISS` := matched and not delivered. The frozen tokens are printed exactly as TR-1 §3 froze them: `bus.position_census: subscriber=<id> matched=<m> delivered=<d> missed=<n> first_missed=<p|none>` per subscriber and `bus.position_census_total: runs=<k> subscribers=<K> missed=<n>`. The atomic-checkpoint subscriber (`state_projection`) is scored on the bus snapshot's checkpoint AND flagged `atomic=true` in its line; a miss on it alone is reported, not asserted (TR-1 §1 reason 3).

**(C) The soak.** One core, K hero loops (`K = 20` default; the system property `homesynapse.soak.loops` overrides): each loop is `reportOccupied(false)` → `reportOccupied(true)` → await the On frame at the scripted NCP (`sentFrame(0x0006, 0x01)` count grows by one) → await the confirm → `occupied` back to false. Per loop the delivery latency = the instant the On frame reached the NCP minus the instant `reportOccupied(true)` returned (the test's injected `Clock` is not the source here — wall time via `System.nanoTime()` is the lawful exception for a latency MEASUREMENT in a test, and is named so in the class javadoc). At the end: p50, p99, max in ms; the anomaly count (a logback `ListAppender` on the `com.homesynapse.lifecycle.HomeSynapseCore` logger counting messages that start with `bus.delivery_anomaly`); the census of (B) once over the whole run. A loop that times out runs the (A) diagnostic and the test FAILS with it — that failure IS the instrument working.

Nothing in `src/main` changes. Module-info is untouched (the lifecycle test source set already reads `SubscriberSnapshot` and `SubscriberMode` through `requires transitive com.homesynapse.event.bus`).

## §2 Files to create or modify (the table governs; M/A exact)
| Path | M/A | What |
|---|---|---|
| `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/BusAwaitDiagnostic.java` | A | package-private final class; `static String render(String what, long storeHead, OptionalLong awaited, List<SubscriberSnapshot> subscribers)`; pure; no I/O; the format in §4-A |
| `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/BusAwaitDiagnosticTest.java` | A | unit test of `render` on a hand-built snapshot list (red at HEAD: the class does not exist) |
| `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/HeroLoopHardwareFreeIT.java` | M | `awaitTrue` gains the diagnostic (§4-A); the hero-loop test names its awaited position for the On-frame await; no assertion changes |
| `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/BusPositionCensusIT.java` | A | (B): one hero loop, then the census; prints the frozen tokens; asserts `missed=0` for every non-atomic subscriber |
| `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/BusSoakIT.java` | A | (C): K loops; the latency table; the anomaly count; the census; the diagnostic on any timeout |
| `lifecycle/lifecycle/MODULE_CONTEXT.md` | M | a `## FIX-2a` entry under Phase 3 Notes: the three instruments, how to run them, what each line means |

Expected census: **6 = 2 M + 4 A.** A helper the three tests share (the manifest of subscriber ids and their filters; the census computation) lives in ONE new class only if it keeps the table at 6 — otherwise it lives in `BusPositionCensusIT` as package-private statics and `BusSoakIT` calls them. State the choice as `[INFO]`.

## §3 STOP-on-mismatch gates (read before writing; a mismatch = STOP and report)
| Where | Expected | Instrument |
|---|---|---|
| `HeroLoopHardwareFreeIT.java:607–:615` | `private static void awaitTrue(BooleanSupplier condition, String what)` — 500 polls, `sleepBriefly()`, `throw new AssertionError("timed out awaiting " + what)` | `sed -n '607,615p'` |
| `HeroLoopHardwareFreeIT.java:115` | the On-frame await: `awaitTrue(() -> sentFrame(0x0006, 0x01).isPresent(), "the On frame reaching the scripted NCP")` | `sed -n '113,116p'` |
| `HeroLoopHardwareFreeIT.java:495–:501` | `subscriberMode(String)` reads `core.eventBus().subscribers()` → `SubscriberSnapshot::mode` | `sed -n '495,501p'` |
| `SubscriberSnapshot.java:36–:43` | record fields, in order: `subscriberId, mode, checkpoint, dlqDepth, crashCount, oldestParkedAt` | `sed -n '36,43p'` |
| `InProcessEventBus.java:467` | `public List<SubscriberSnapshot> subscribers()` | `grep -n 'public List<SubscriberSnapshot> subscribers' ` |
| `InProcessEventBus.java:525–:592` | `liveLoop`: `pendingPositions().poll()` → `LockSupport.park()` on null; the checkpoint written only on `SUCCESS` and only when `!atomicCheckpoint()` | `sed -n '525,592p'` |
| `HomeSynapseCore.java:557–:560` | the anomaly handler logs `"bus.delivery_anomaly: kind={} subscriber={} position={} detail={} at={}"` at WARN on the `HomeSynapseCore` logger | `sed -n '555,562p'` |
| `HomeSynapseCore.java:189, :200` | `PROJECTION_SUBSCRIBER_ID = "state_projection"`, `AUTOMATION_SUBSCRIBER_ID = "automation_engine"` | `sed -n '189p;200p'` |
| `DeliveryAnomaly.java` | the `Kind` constants: `NOTIFY_NOT_VISIBLE LIVE_READ_EMPTY LIVE_READ_FAILED TRANSITION_READ_EMPTY LIVE_READ_EXHAUSTED TRANSITION_READ_EXHAUSTED` (six) | `grep -cE '^\s+[A-Z][A-Z_]+[,;]?\s*(//.*)?$'` → 6 |
| `ZigbeeHardwareFreeRig.java:137` | `public void reportOccupied(boolean occupied)` | `sed -n '137p'` |
| the lifecycle test home | 18 tracked files under `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/`; the suite count at HEAD from `./gradlew :lifecycle:lifecycle:test` = 79 | `git ls-files … \| wc -l`; the gradle line |
| `logback-classic` on the lifecycle test classpath | present (the ITs already log through it) — if absent, STOP: the anomaly counter needs `ch.qos.logback.core.read.ListAppender`, the pattern at `integration/integration-zigbee/src/test/java/com/homesynapse/integration/zigbee/ZclIngestionUnitTest.java` | `grep -n 'logback' lifecycle/lifecycle/build.gradle.kts` |

## §4 Technical specification
**A — the diagnostic.** `BusAwaitDiagnostic.render` returns exactly these lines, `\n`-joined, no trailing newline:
```
bus.await_timeout: what=<what> store_head=<H> awaited=<P|none>
bus.await_subscriber: subscriber=<id> mode=<MODE> checkpoint=<C> dlq=<D> behind=<H-C>
… one per snapshot, in the list's order
```
`awaitTrue(BooleanSupplier, String)` keeps its signature and gains a private sibling `awaitTrue(BooleanSupplier condition, String what, LongSupplier awaitedPosition)`; on timeout both build the text from `core.eventBus().subscribers()` and `events()` (the head = the max `globalPosition` in the store; `events()` exists at `:543`), print it with `System.out.println`, and throw `new AssertionError(text)` — the first line is the message the JUnit XML `<failure message>` carries. The On-frame await at `:115` passes the position of the newest `state_reported` envelope whose `attributeKey()` is `occupied` and whose reported value is `true` (the predicate `reportedValues` already applies at `:563–:572`). `render` is the only thing `BusAwaitDiagnosticTest` tests: three snapshots, one behind by 2, one atomic at 0, one LIVE at head → the exact six-line string.

**B — the census.** The manifest is built from what the composition root registers — the six ids in §1, each with its filter obtained the way the source exposes it (`RegistryProjectionSubscriber.subscriptionFilter()` at `:73` is package-private in `com.homesynapse.lifecycle` — the test is in that package; `CommandDispatchAssembly` `:95` and `PendingCommandLedgerAssembly` `:119` are `public static`; `IntegrationSupervisorAssembly` `:81` likewise; `state_projection` is `SubscriptionFilter.all()` at `HomeSynapseCore:634`; `automation_engine`'s filter is read at `HomeSynapseCore:735`). Ground every one with the `sed -n` line in your return; if a filter is not reachable from the test, replicate it from the registration site with the line cited and say so as `[INFO]`. Positions come from `events()`; the checkpoint and DLQ depth from `subscribers()`; a DLQ row per position is NOT visible through the snapshot (only the depth is) — so `DELIVERED` is computed as `checkpoint ≥ P` and the subscriber's `dlqDepth` is printed on its line; when `dlqDepth > 0` the line is flagged `dlq_unscored=true` and the miss count is reported, not asserted (state this limit in MODULE_CONTEXT; TR-1b's driver on the card reads the DLQ table directly). Assert: every non-atomic subscriber with `dlqDepth == 0` has `missed=0`. Print the tokens in §1's exact grammar; `runs=1`.

**C — the soak.** `BusSoakIT.soak_kHeroLoops_reportsLatencyAndAnomalies`: boot once (the IT's `bootAndAdopt` shape, copied — not shared across classes unless the Files table stays at 6); `awaitRuntimeSubscribersLive()`; then K loops as §1-C. Per loop: `t0 = System.nanoTime()` after `reportOccupied(true)` + `deliverAndCycle()` returns; await the NCP frame count = loop index + 1 (with the (A) diagnostic, the awaited position named); `t1` at the first poll that sees it; record `(t1 − t0)` ms. Between loops: await the confirm the way the hero test does (`:120–:160` — read it; do not invent an event type), then `reportOccupied(false)` + `deliverAndCycle()` and await its `state_reported`. After K loops print:
```
bus.soak: loops=<K> ok=<n> timed_out=<m> p50_ms=<x> p99_ms=<y> max_ms=<z> anomalies=<a>
```
then the census tokens of (B) with `runs=<K>`. The assertions: `timed_out == 0`; `anomalies == 0`; the census `missed=0` for every scored subscriber. A timeout fails the test WITH the diagnostic — do not swallow it, do not retry the loop.

**Clock.** The three tests inject `Clock` where the core takes one (as the hero IT does); `System.nanoTime()` appears ONLY in `BusSoakIT` for the latency measurement and is named in the class javadoc as the measured wall-clock quantity. See §8's paste block.

## §5 Locked decisions and invariants that apply
D11 (the bench is the test-and-truth engine; the desk's soak is the in-process instrument, the card's driver is TR-1b's) · TR1-B2 = DRIVER (the bench verb is a driver script, not a scenario; NOT this WU) · the FROZEN token grammar of TR-1 §3 (`bus.position_census*`; the soak line is NEW and named here first) · AMD-45 §2.2 (state_projection's atomic checkpoint lags delivery by design) · LTD-15 (SLF4J only through the existing logger; the test reads logback directly on the test classpath — a test concern, not a production dependency) · INV: no production behaviour changes in this WU (the instruction's whole premise; a `src/main` diff = STOP).

## §6 Red-first predictions (adjudicate FIRST in the return; name the artifact each is read from)
| # | Prediction | Direction / arm | Inverse arm (report it as first-class) | Read from |
|---|---|---|---|---|
| P1 | `BusAwaitDiagnosticTest` is RED at HEAD (compile: the class does not exist) and GREEN after A | compile-red → green | — (a preservation fixture cannot go red; this one is a new class) | the gradle compile log; then the XML |
| P2 | `BusSoakIT` at K=20 reproduces the class on the desk at least once in three runs: a loop times out, the diagnostic shows `automation_engine` with `checkpoint < awaited` and `dlq=0`, `anomalies=0` | at least 1 of 3 runs RED | 3 of 3 GREEN → the class does not reproduce in-process on this desk in 60 loops; the next instrument is the card's driver (TR-1b), not a fix; say so | `TEST-com.homesynapse.lifecycle.BusSoakIT.xml` `<failure message>` + `<system-out>` |
| P3 | On the green loops: p50 < 250 ms, p99 < 2,000 ms | bounds | p99 ≥ 2 s on a green run = a latency finding in its own right (report the distribution) | the `bus.soak:` line in the XML `<system-out>` |
| P4 | `BusPositionCensusIT` after one loop: `missed=0` for the five non-atomic subscribers; `state_projection` reported `atomic=true` with its own number | green at HEAD (a measurement, not a preservation claim — it can go red if the drop lands in that one loop) | a red here = the class reproduced in one loop; file the tokens and the diagnostic | the `bus.position_census*` lines in the XML |

## §7 The measurement table (fill in the return; every cell names its artifact)
| Row | Value | Artifact |
|---|---|---|
| suite count at HEAD / after | 79 / <n> | the gradle `tests completed` line |
| soak runs (K=20 ×3): ok / timed_out per run | | `BusSoakIT.xml` `<system-out>` |
| p50 / p99 / max (per run) | | the `bus.soak:` line |
| anomalies (per run) | | the `bus.soak:` line + `grep -c bus.delivery_anomaly` on the XML |
| census after one loop: per-subscriber lines | | `BusPositionCensusIT.xml` |
| the diagnostic text of any timeout, whole | | `<failure message>` + `<system-out>` |

## §8 What to watch out for
- **Tests must inject `Clock`.** Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` in this module's test code. Use `Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC)` injected via constructor/`@BeforeEach`. **Enforcement reach:** `NO_DIRECT_TIME_ACCESS` runs from `com.homesynapse.app`'s test classpath, so it mechanically catches PRODUCTION code in every non-whitelisted module (plus app's own tests) — it does **not** scan this module's test source set. Clock-injection here is a self-enforced project convention that PM review enforces. *(The ONE exception in this WU: `BusSoakIT`'s latency measurement uses `System.nanoTime()` for the measured quantity and says so in its javadoc; the hero IT's own polling loop already runs on wall time via `sleepBriefly()`.)*
- **The registry projection is type-filtered** (`HeroLoopHardwareFreeIT:503–:521` explains why a store-head await is unreachable for it): the census scores it by ITS filter, never against the head.
- **`state_projection` is atomic** (`HomeSynapseCore:636`): its bus checkpoint lags delivery by design; report, never assert.
- **Positions are not dense** (retention; `AUTOINCREMENT`): derive the position set from `events()`, never from a range.
- **The DLQ is visible only as a depth** through `SubscriberSnapshot`; the per-position rule of TR-1 §1 is the card driver's; say what you scored.
- **Do not change any assertion in the hero test** and do not add retries; the diagnostic is added to the failure path only.
- **The soak shares one core across K loops**: the rig's `sentZclFrames()` accumulates — count, do not `isPresent()`; the confirm path per loop is the hero test's (`:120–:160`), read before writing.
- **`ListAppender` attaches to the logback `Logger` behind `LoggerFactory.getLogger(HomeSynapseCore.class)`** — cast pattern as in `ZclIngestionUnitTest`; detach in `@AfterEach`.
- **Timeouts:** the hero test's 10 s (500 × 20 ms) stands for the soak's per-loop await; K=20 × ~1 s is the expected wall time — if the suite time grows past 60 s, say so in the return; do not lower K without a `[REVIEW]`.

## §9 Out of scope
The structural fix (checkpoint-driven LIVE delivery: read forward from the checkpoint on every wake, the notification as a hint, a bounded idle tick — FIX-2b, authored on this lane's §7) · any `src/main` change · the bench driver script in `nexsys-bench/tools/` (TR-1b's, gated on `card-gradle:`) · the per-position DLQ census (the card's) · EXPLAIN-114a (held behind this lane) · changing the FIX-1a detector's kinds.

## §10 Test requirements (summary)
Unit: `BusAwaitDiagnosticTest` (1 test, the exact string). Integration: `BusPositionCensusIT` (1 test), `BusSoakIT` (1 test). Existing: the hero suite stays 5/5 in the green case; the new expected count is `79 + 3 = 82` (the P2 red, when it lands, is reported as the run's observed count with its failure). Run each IT three times and report all three (P2 is a frequency claim).

## §11 Coder pushback welcome
If `subscribers()` or the filter accessors cannot give the census what §4-B needs without a production seam, STOP with the exact gap (`file:line`) and the smallest seam you would add — the hub rules; this WU stays test-only. If the class never reproduces (P2's inverse arm), that is a finding, not a failure of the WU: report the three distributions and stop.

## §12 WUCP Phase 1 closeout (in the return)
The census line · the predictions adjudicated · the measurement table · MODULE_CONTEXT's `## FIX-2a` entry (what each token means; how to run the soak with `-Dhomesynapse.soak.loops=N`) · the Deferred Build Gate line (`./gradlew check` owed to CI on Nick's push) · the `RETURNED` line last.

## §13 module-info (verbatim; NO change proposed)
`lifecycle/lifecycle/src/main/java/module-info.java` — `requires transitive com.homesynapse.event.bus;` and `requires transitive com.homesynapse.event;` are already present (the file is 90 lines; `grep -n 'requires transitive com.homesynapse.event' lifecycle/lifecycle/src/main/java/module-info.java` → two lines). The test source set sees `SubscriberSnapshot`, `SubscriberMode`, `SubscriptionFilter`, `EventEnvelope` through them today (`HeroLoopHardwareFreeIT` imports them). Zero module-info edits; a needed edit = STOP.

## §14 Nick's paste (a host-side Claude Code session in `homesynapse-core`, on `main` at `1e26912`, porcelain empty)
```
date -u first. You are the Coder for FIX-2a on homesynapse-core (the nexsys-coder skill governs). Read ../nexsys-hivemind/context/instructions/2026-09-11_coder-lane_FIX-2a_bus-silent-drop_instrument-first_coding-instruction.md WHOLE, then its §0 read-set by the ranges it names. Verify the baseline (git log -1 --oneline prints 1e26912; git --no-optional-locks status --porcelain is empty) and every §3 gate at the instrument before you write. Test-only: no file under src/main changes; module-info is untouched. Red-first: run BusAwaitDiagnosticTest at HEAD before writing the class. Run BusSoakIT three times at K=20 and report all three. Adjudicate P1–P4 first in the return. Commit nothing; stage nothing. Write the return to ../nexsys-hivemind/context/audits/<today CT>_FIX-2a_return.md (≤12 KB; §0 card first; the last line is `RETURNED <path> <bytes>`), and say that one line to Nick.
```
