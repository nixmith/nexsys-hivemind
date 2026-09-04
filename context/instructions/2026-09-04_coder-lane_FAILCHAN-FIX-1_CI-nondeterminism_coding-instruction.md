<!--
file: context/instructions/2026-09-04_coder-lane_FAILCHAN-FIX-1_CI-nondeterminism_coding-instruction.md
purpose: THE FAILCHAN-FIX-1 CODING INSTRUCTION — `main` is RED on two runs of identical Java bytes, two classes, two modules (CI #225 on 7af2d6c: HeroLoopHardwareFreeIT:324 · dc3328b's run: ReplayTransitionIT:212; PR #5's run on the same bytes: GREEN). RULED instrument-first at v62 beat 8; RE-CUT at v63 beat 1 on the hub's source reads (the grounding audit context/audits/2026-09-04_v63-b1_boot-grounding_executive-model-and-intake.md §3–§6): the charter is THE CLASS (silent, unlogged delivery drops on the bus's LIVE/TRANSITION paths; CI that hides every verdict after the first red), not the instance. ONE lane, TWO commits: FIX-1a THE INSTRUMENTS (lands first; every later red self-describing) → the loops → FIX-1b THE MECHANISM (on the evidence, never on theory).
audience: the Coder lane (host-side Claude Code, homesynapse-core) · Nick (dispatch + the two commits) · the hub (audit)
state-type: coding instruction
status: ISSUE-READY — dispatch-as-word (`FIX1: class` is the hub's recommendation and the default if the dispatch line is pasted as written; `FIX1: instance` narrows §B to HeroLoop only). baseline: core `dc3328b` CLEAN (re-verify at issue: `git -C homesynapse-core log -1 --format=%h` must print dc3328b; if not, STOP and report). Java bytes identical to 7af2d6c's. Return path + cap: §0. One lane on the core tree until FIX-1b's green clears the gate.
-->

# Coding Task: FAILCHAN-FIX-1 — the delivery-drop class made visible, then fixed on its measurement (`main` green for a reason)

**Subsystem:** core/event-bus (the LIVE + TRANSITION delivery paths) · lifecycle (the composition root's emitter route) · `.github/workflows/ci.yml` + `build-logic` (the gate's own instruments) · integration-runtime (read-only: the `route_join_miss` fingerprint)
**Design Doc:** Doc 04 (Event Bus) — AMD-42 §3.4.2/§3.4.3 (REPLAY→TRANSITION→LIVE; `onCaughtUp` single-shot) · AMD-43 §3.6.2 (the SEVEN canonical bus metrics — LOCKED; this WU adds NONE) · Doc 11 (metrics governance, by pointer) · LTD-09/LTD-11 (injected clocks; no `synchronized`) · LTD-15/DECIDE-01 (one logging facade — SLF4J; the bus module stays SLF4J-free by its own design note, `QueueSaturationHealthCheck.java:36–:43`)
**Phase:** 3-Implementation (Part A carries instruments; Part B the fix)
**Task Brief Reference:** OR-FAILCHAN (pm-handoff §Open Risks) beat-8 line → FAILCHAN-FIX-1 RULED instrument-first (v62 b8/b9) → re-cut at v63 b1 (the grounding audit §6, option (a) THE CLASS)

## §0 The lane contract (read first)
- **`date -u` FIRST** — every stamp in your return derives from it. State your instrument limit (host clock; WSL if used) and re-derive CT as UTC−5 once at the top.
- **Return path:** `nexsys-hivemind/context/audits/2026-09-05_FIX-1_return.md` — ONE file (the path is fixed whatever CT date you file at). **Shape:** §0 card FIRST (≤3 KB: the TWO censuses `FIX-1a: N = a M + b A` and `FIX-1b: …` with exact paths · the branch verdict per class from §A.5's table · the red-first table ≤2.5 KB · deviations by tag) · §1 THE MEASUREMENT TABLE (§A.5, filled) · §2 what changed per file · §3 the gates run + counts · §4 pushback/observations · §5 the WUCP Phase-1 checklist. **Cap:** ≤12 KB target, hard ceiling ~17 KB. **The loop corpus** goes beside it, NOT in it: `nexsys-hivemind/context/audits/2026-09-05_FIX-1_loops/` — `SUMMARY.md` (one line per run: `class · tree · run-NN · GREEN|RED · wall-clock · the anomaly tokens seen`) + the per-method XML **of RED runs only** + their class stdout; passing runs contribute their summary line only. Cap the folder at ~400 KB.
- **Baseline:** `dc3328b`. Line numbers below are from that HEAD (re-derived by the hub at the instrument on 2026-09-04 22:5xZ); a cited line shifted by a few → `[INFO]` and proceed; a cited construct ABSENT → STOP and report.
- **Build discipline:** you MAY run targeted Gradle on your desk (`./gradlew :core:event-bus:compileJava :core:event-bus:test :lifecycle:lifecycle:compileJava :lifecycle:lifecycle:test spotlessCheck --offline`) — GREEN in one round is the target; the full `./gradlew check` is Nick's push → CI = the gate of record. The loops (§A.3/§A.4) are YOUR instrument and run on your desk.
- **Two commits, one lane, you commit neither.** Stage nothing. The hub audits the return; Nick commits FIX-1a from its msg file, pushes, and its `main` run is SAMPLE #4; the loops run meanwhile; FIX-1b lands as the second commit. **The gate clears only on FIX-1b's push run GREEN** (plus §B.4's veto-only samples). Never a `main` re-run as clearance.
- **Tests first** (red-first): every new test is written and RUN RED at HEAD (or declared green-by-construction, disclosed) before the production edit; the return's red-first table shows the two runs.
- **THE INSTRUMENT LAW:** no line of Part B is written before Part A's table (§A.5) is filled from real runs. A fix on theory is a `[BLOCKING]` deviation against this instruction.

## What This Implements
`main` has failed on two different integration tests across three CI runs of byte-identical Java (the audit §3). At source, the bus's LIVE delivery loop and the TRANSITION drain contain **four silent, unlogged drop points** where a position whose read returns empty or throws is skipped forever (`InProcessEventBus.java:250 :480 :487`; `TransitionCoordinator.java:100`), and CI's `check` stops at the first failing module (no `--continue`) while uploading only HTML reports on failure — so no red run has ever carried its own mechanism. This WU (a) makes every drop **visible** through a typed emitter routed to the log (FIX-1a), makes CI **report everything** with per-test-case XML and full assertion messages (FIX-1a), (b) **measures** both failing classes under runner-shaped scheduling on the current tree and on the pre-FAILCHAN tree (the loops), and (c) **fixes the mechanism the measurement names** — a drop becomes a bounded retry then an honest SUSPEND, never a skip (FIX-1b, branch-tabled). It never raises a bound, never retries a test, never quarantines.

## Files to Read Before Starting (minimum read set — MANDATORY; the grounding audit §4 is the map)
1. `nexsys-hivemind/context/audits/2026-09-04_v63-b1_boot-grounding_executive-model-and-intake.md` §2–§4 (the filed CI log; the three-run table; the source premises S1–S6, line-cited).
2. `core/event-bus/src/main/java/com/homesynapse/event/bus/InProcessEventBus.java` — WHOLE (591 lines): `notifyEvent` `:235–:310` (the `:250` empty-page return; the `:302` `vt != null` guard), `subscribeRuntime` + the VT start (`:341–:365`, `setVirtualThread` at `:365`), `liveLoop` `:460–:520` (`:471` park; `:480` empty page; `:487–:488` the transient-read skip; `:508` the checkpoint write).
3. `core/event-bus/src/main/java/com/homesynapse/event/bus/TransitionCoordinator.java` — WHOLE (173 lines): `drainAndPromote` `:83–:150` (`:100` empty page; `:107` the honest SUSPEND on exception; `:134` the CAS).
4. `core/event-bus/src/main/java/com/homesynapse/event/bus/{SubscriberRuntime,ReplayDriver,ReplayWindowQueue,HealthSignal,HealthLevel,QueueSaturationHealthCheck,BusMetrics}.java` — `SubscriberRuntime` whole; the others' class javadoc + public surface (the `HealthSignal` emitter pattern is the shape DP-1 copies; `BusMetrics`' seven names are LOCKED).
5. `core/event-bus/src/test/java/com/homesynapse/event/bus/ReplayTransitionIT.java` — WHOLE (237 lines; `:112 :167 :168` the three waits; `:200–:214` `awaitCheckpoint`).
6. `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/HeroLoopHardwareFreeIT.java` — WHOLE (625 lines; `:318–:333` the red method; `:481–:493` the LIVE barrier; `:592–:615` the awaits).
7. `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java` — the bus construction `:545–:560` (`BusMetrics.jfr()` at `:550`, `new InProcessEventBus(` at `:551`) and the emitter `:628–:640`; the subscriber registrations `:590–:840`.
8. `integration/integration-runtime/src/main/java/com/homesynapse/integration/runtime/CommandRoutingSubscriber.java` `:92 :152–:198` (read-only: the join cache and the `route_join_miss` WARN — the fingerprint you will look for in red HeroLoop runs).
9. `.github/workflows/ci.yml` (40 lines) · `build-logic/src/main/kotlin/homesynapse.java-conventions.gradle.kts` `:40–:51` (the `Test` task block).
10. `core/event-bus/MODULE_CONTEXT.md` (header + Gotchas) · `lifecycle/lifecycle/MODULE_CONTEXT.md` (header + the composition-root section) — the persistent memory you update.
11. `nexsys-hivemind/context/audits/2026-09-04_CI-225_HeroLoopHardwareFreeIT_stdout-census.txt` — **if present** (Nick files it separately). If absent, say so in §0 and proceed; §A.5 rebuilds per-method truth on the FIX-1a tree.

## STOP-on-Mismatch Gates (read, then confirm before any edit)
| File | Expected state at `dc3328b` | What to check |
|---|---|---|
| `InProcessEventBus.java` | `:250` `if (page.events().isEmpty()) { return; }` inside `notifyEvent`; `:480` the same test inside `liveLoop` followed by `continue`; `:487–:488` `catch (Exception e)` with the comment "Transient read failure — skip this position; retain mode." | the three constructs exist; the class has NO SLF4J import |
| `TransitionCoordinator.java` | `:100` empty page → `continue`; `:107` `catch (Exception e)` → `transitionTo(SUSPENDED)` + `setMode(SUSPENDED)` + `return false` | both arms as stated |
| `core/event-bus/src/main/java/module-info.java` | exactly `requires transitive com.homesynapse.event;` · `requires jdk.jfr;` · `exports com.homesynapse.event.bus;` (embedded verbatim below) | **byte-unchanged by this WU** |
| `HeroLoopHardwareFreeIT.java` | 5 `@Test` methods (`:90 :165 :224 :269 :318`); `awaitTrue` = 500 × 20 ms (`:607–:619`) | counts; the bound is NOT edited by this WU |
| `ReplayTransitionIT.java` | 1 `@Test`; waits `15_000L` (`:112`), `60_000L` (`:160`), `30_000L` (`:167`), `5_000L` (`:168`) | the bounds are NOT edited by this WU |
| `ci.yml` | `run: ./gradlew check --no-daemon` (`:32`); upload `if: failure()` of `**/build/reports/tests/` (`:34–:40`); no `workflow_dispatch` | as stated |
| `homesynapse.java-conventions.gradle.kts` | `tasks.withType<Test>().configureEach { useJUnitPlatform(); jvmArgs("-XX:+EnableDynamicAgentLoading") }` (`:48–:51`) | as stated |
| `HomeSynapseCore.java` | `Consumer<HealthSignal> healthSignalHandler` at `:628`; `new InProcessEventBus(` at `:551` | the route lands beside `:628`; the ctor call at `:551` gains the emitter |

## Files to Create or Modify (the Files table governs — addition #2)

**FIX-1a — THE INSTRUMENTS (commit 1; census 9 = 7 M + 2 A):**
| # | File | M/A | Delta |
|---|---|---|---|
| 1 | `.github/workflows/ci.yml` | M | `on:` gains `workflow_dispatch:` (no inputs) · `run: ./gradlew check --no-daemon --continue` · the upload step becomes `if: always()`, `name: test-reports-${{ github.run_number }}`, `path:` a two-line list `**/build/reports/tests/` + `**/build/test-results/`; `retention-days: 14` |
| 2 | `build-logic/src/main/kotlin/homesynapse.java-conventions.gradle.kts` | M | inside `tasks.withType<Test>().configureEach { … }`: `reports.junitXml.outputPerTestCase = true` · `testLogging { events("failed"); exceptionFormat = org.gradle.api.tasks.testing.logging.TestExceptionFormat.FULL; showStandardStreams = false }` · the property-gated VT knob: `project.findProperty("vtParallelism")?.toString()?.toIntOrNull()?.let { n -> jvmArgs("-Djdk.virtualThreadScheduler.parallelism=$n", "-Djdk.virtualThreadScheduler.maxPoolSize=$n") }` (a desk-only knob; CI never sets it) |
| 3 | `core/event-bus/src/main/java/com/homesynapse/event/bus/DeliveryAnomaly.java` | A | `public record DeliveryAnomaly(String subscriberId, long globalPosition, Kind kind, String detail, Instant timestamp)` with nested `public enum Kind { NOTIFY_NOT_VISIBLE, LIVE_READ_EMPTY, LIVE_READ_FAILED, TRANSITION_READ_EMPTY, LIVE_READ_EXHAUSTED }` — `Objects.requireNonNull` on the three references in the compact ctor; components are `java.base` only (no JPMS edge; the P2 direction check is trivially satisfied). `LIVE_READ_EXHAUSTED` is reserved for FIX-1b (DP-2) and is not emitted by FIX-1a — say so in the javadoc. |
| 4 | `core/event-bus/src/main/java/com/homesynapse/event/bus/InProcessEventBus.java` | M | a new `public` constructor overload adding a trailing `Consumer<DeliveryAnomaly> anomalyEmitter` (non-null; the three existing constructors delegate with `a -> { }` — ZERO change at the four existing call-site files); emit at the four points: `:250` `NOTIFY_NOT_VISIBLE` (subscriberId `"*"`, detail `"notifyEvent: no envelope at position"`), `:480` `LIVE_READ_EMPTY`, `:487` `LIVE_READ_FAILED` (detail = `e.getClass().getSimpleName() + ": " + e.getMessage()`); timestamp from the injected `clock`. Behavior otherwise UNCHANGED in FIX-1a (the `return`/`continue` stay). |
| 5 | `core/event-bus/src/main/java/com/homesynapse/event/bus/TransitionCoordinator.java` | M | receives the same emitter (package-private ctor param; `InProcessEventBus` passes it); emit `TRANSITION_READ_EMPTY` at `:100` before the `continue`. |
| 6 | `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java` | M | beside `healthSignalHandler` (`:628`): `Consumer<DeliveryAnomaly> anomalyHandler = a -> LOG.warn("bus.delivery_anomaly: kind={} subscriber={} position={} detail={} at={}", a.kind(), a.subscriberId(), a.globalPosition(), a.detail(), a.timestamp());` — passed into the bus ctor at `:551` (declare it BEFORE `:551`; move the lambda up, not the ctor down). ONE token, ONE line; the bus stays SLF4J-free. |
| 7 | `core/event-bus/src/test/java/com/homesynapse/event/bus/DeliveryAnomalyEmissionTest.java` | A | red-first (§Tests T1–T3): a stub `EventStore` whose `readFrom(pos-1,1)` returns an EMPTY page for one chosen position and THROWS for another; assert the emitter receives `LIVE_READ_EMPTY` / `LIVE_READ_FAILED` with the subscriberId + position, and that `notifyEvent` on a position the store cannot see emits `NOTIFY_NOT_VISIBLE`. Injected `Clock.fixed`. |
| 8 | `core/event-bus/MODULE_CONTEXT.md` | M | header 33 → 34 types (+ `DeliveryAnomaly` with nested `Kind`); a Gotcha: "the LIVE loop never pages forward from the checkpoint — a position not offered is a position not delivered; every drop now emits a `DeliveryAnomaly`"; the emitter's contract (never throws; called on the subscriber's VT). |
| 9 | `lifecycle/lifecycle/MODULE_CONTEXT.md` | M | the composition-root section: the `bus.delivery_anomaly` WARN route beside the health-signal route. |

**FIX-1b — THE MECHANISM (commit 2; census by branch, §Part B — declared in the return's §0 after §A.5 is filled):** the bus files above (M) + the red-first tests per branch (A) + MODULE_CONTEXT deltas; HeroLoop/ReplayTransitionIT are NOT edited unless a branch names them (then only to add a stamp, never a bound).

## Technical Specification

### Part A — THE INSTRUMENTS, then THE LOOPS (nothing in Part B before §A.5 is filled)

**A.1 FIX-1a as specified in the Files table; DP-1 settled:** the drop signal rides a typed emitter (`Consumer<DeliveryAnomaly>`) exactly as `HealthSignal` rides `Consumer<HealthSignal>` — the bus module's own design note (`QueueSaturationHealthCheck.java:41–:43`) forbids a new `requires org.slf4j`, and AMD-43's seven metric names are locked, so neither a log line in the bus nor an eighth JFR event is lawful here. The composition root owns the transport (one SLF4J WARN). Contract: the emitter is called on the delivering thread, must not throw (wrap the call in a `try/catch (RuntimeException)` that swallows — an instrument must never become a failure channel), and is invoked BEFORE the existing `return`/`continue`.

**A.2 CI as specified (`ci.yml` + the conventions):** `--continue` so a red run reports every failing task (the `dc3328b` run hid lifecycle's verdict entirely); XML per test case + full exception format so the console and the artifact carry the assertion MESSAGE (today's console shows only `java.lang.AssertionError at ReplayTransitionIT.java:212` — the phase is invisible); `workflow_dispatch` so Nick can take VETO-ONLY samples of a landed sha (§B.4); the `vtParallelism` knob so a desk can reproduce the runner's virtual-thread scheduler (2 carriers) without changing CI.

**A.3 I-3 — the loops on the FIX-1a tree (both classes ×20, runner-shaped).** Run in WSL (or any Linux shell with `taskset`); if your desk has neither, state the instrument limit and use the `-PvtParallelism=2` knob alone. The recipe (adapt paths; keep the stamps):
```bash
date -u; cd ~/Desktop/Code/ClaudeFolder/homesynapse-core   # or the WSL mount of it
OUT=$HOME/fix1-loops; mkdir -p $OUT
for i in 1 2; do taskset -c 0,1 sh -c 'while :; do :; done' & done; LOAD=$!   # two busy loops on the same two cores
run_class () {  # $1 module:task  $2 test filter  $3 label  $4 tree-label
  for n in $(seq -w 1 20); do
    s=$(date -u +%H:%M:%S.%N); taskset -c 0,1 ./gradlew $1 --tests "$2" --rerun-tasks --no-daemon -PvtParallelism=2 -q >/tmp/run.log 2>&1; rc=$?
    e=$(date -u +%H:%M:%S.%N); d="$OUT/$3/$4/run-$n"; mkdir -p "$d"
    tok=$(grep -hoE 'bus\.delivery_anomaly: kind=[A-Z_]+|integration\.route_join_miss' $(dirname ${1//:/\/})/build/test-results/test/*.xml 2>/dev/null | sort | uniq -c | tr '\n' ';')
    echo "$3 · $4 · run-$n · $([ $rc -eq 0 ] && echo GREEN || echo RED) · $s→$e · $tok" | tee -a $OUT/SUMMARY.md
    [ $rc -ne 0 ] && cp $(dirname ${1//:/\/})/build/test-results/test/*.xml "$d"/ && cp /tmp/run.log "$d"/gradle.log
  done; }
run_class :lifecycle:lifecycle:test 'com.homesynapse.lifecycle.HeroLoopHardwareFreeIT' HeroLoop fix1a
run_class :core:event-bus:test 'com.homesynapse.event.bus.ReplayTransitionIT' ReplayIT fix1a
kill %1 %2 2>/dev/null; date -u
```
(The `$(dirname ${1//:/\/})` path trick resolves `:lifecycle:lifecycle:test` → `lifecycle/lifecycle`; verify it prints the module's `build/test-results/test/` before trusting it — a `[INFO]` if you replace it with literal paths.) Per-run stamps are the instrument's clock; the red runs' XML carries the per-method stdout (`outputPerTestCase`), so the `route_join_miss` WARN and every `bus.delivery_anomaly` token are attributable to the method that produced them.

**A.4 I-4 re-cut — HeroLoop ×20 on the pre-FAILCHAN tree.** `git worktree add ../hs-ef02d13 ef02d13` → the same `run_class` for HeroLoop with tree-label `ef02d13` (no tokens exist there; the loop answers only "does it reproduce" — the FAILCHAN lifecycle hunks isolated). **ReplayTransitionIT on `ef02d13` is skipped by construction**: `core/event-bus` is byte-identical between `ef02d13` and `dc3328b` (say so in the table). Remove the worktree after (`git worktree remove ../hs-ef02d13`).

**A.5 THE MEASUREMENT TABLE (the return's §1) — and the hub's predictions, filed before your runs (H12).** Fill every cell; where a prediction misses, say so — a mismatch is adjudicated first, never explained away.
| Instrument | The hub predicts | Measured |
|---|---|---|
| HeroLoop ×20 · fix1a tree · `taskset 0,1` + load + `vtParallelism=2` | ≥1 RED in 20 (the CI sample is 1-of-2 on this class; the desk is faster, so ≤10 %/run is the honest band; 0/20 is possible → branch (c) for this class) | |
| …the RED run's tokens | `integration.route_join_miss` ×1 in the red method's stdout AND ≥1 `bus.delivery_anomaly` with `subscriber=integration_supervisor` naming the `command_issued` position — `LIVE_READ_FAILED` or `LIVE_READ_EMPTY` (S4); `NOTIFY_NOT_VISIBLE` possible | |
| ReplayIT ×20 · fix1a tree · same pressure | ≥1 RED in 20; the message names PHASE 2 (`did not reach 1500 within 30000 ms`); NO `bus.delivery_anomaly` (the in-memory store is lock-protected — the stall is the park/unpark or drain handshake); the checkpoint's resting value in the message's neighbourhood is the diagnostic (1499 ⇒ the last unpark lost at `:302`; < 1499 ⇒ a drain gap) | |
| HeroLoop ×20 · `ef02d13` | reproduces at a similar rate → branch (a) for HeroLoop (FAILCHAN's lifecycle hunks are not the cause) | |
| The CPU-shape sensitivity (run HeroLoop ×10 WITHOUT `taskset`/knob, load only) | the rate collapses toward 0 — the mechanism is carrier-count (2 VT carriers; SQLite's native reads pin a carrier), not raw CPU speed | |
| I-1 (Nick, in the brief; copy his line here) | at least one of CI #169/#183/#206 failed on `ReplayTransitionIT` or `HeroLoopHardwareFreeIT` | |
| The `dc3328b` `test-reports` artifact (Nick, in the brief; copy his line) | `ReplayTransitionIT.html` says `did not reach 1500 within 30000 ms` (phase 2) | |

### Part B — THE MECHANISM, by branch (FIX-1b; one row per class; a class may take a different branch from the other)
| Branch | The evidence that selects it | The fix (the mechanism, never the bound) |
|---|---|---|
| **(a) pre-existing determinism defect** — reproduces on `ef02d13` too, and/or the tokens name a drop | HeroLoop: a `bus.delivery_anomaly` on `integration_supervisor` at the `command_issued` position in the red run · ReplayIT: the stamp/message locates the stall | **DP-2 (settled):** a drop is never a skip. `liveLoop` on `LIVE_READ_EMPTY`/`LIVE_READ_FAILED` **re-queues the same position at the head** and parks `LockSupport.parkNanos` with a bounded backoff (1 → 2 → 4 → 8 → 16 ms, 5 attempts — a sleep is not a clock read; LTD-09 holds); on exhaustion it emits `LIVE_READ_EXHAUSTED` and **SUSPENDs the subscriber** (`transitionTo(SUSPENDED)` + `subscriber().setMode(SUSPENDED)`) — the `drainAndPromote:107` precedent; honest failure beats silent loss. `notifyEvent` on an empty page **offers the position unfiltered to every active LIVE subscriber and enqueues it for REPLAY/TRANSITION ones** (the LIVE loop filters at `:492` after its own read); passive subscribers cannot be filtered without the envelope → emit `NOTIFY_NOT_VISIBLE` for them and document the limitation. `drainAndPromote:100` follows the same retry-then-SUSPEND. **For ReplayIT's stall:** if the last position sits in `pendingPositions` un-parked (the `:302` `vt == null` window), fix the handshake (the VT reference published before the CAS to LIVE, or a re-check of the queue after `park()` returns) — on the stamp evidence only. |
| **(b) FAILCHAN's lifecycle hunks** — HeroLoop reproduces on the fix1a tree but NOT on `ef02d13` (0/20 vs ≥2/20) | the `ef02d13` row | Fix the hunk the stamps implicate (`HomeSynapseCore` +71 / `SystemLifecycleManager` +25 — the start/stop path), keeping FAILCHAN's intent (the report beside the throw; the exit in `main`, never the hook). The §10-O adapter hunk is EXCLUDED by source (driven mode never runs `productionLoop()`). |
| **(c) irreproducible on the desk** — 0/20 on every row | the table | FIX-1b = the DP-2 retry-then-SUSPEND anyway (a drop point with no retry is a defect whether or not this desk can trigger it — the RED run of #225 already proved a delivery was lost) + no other change; the landed sha then takes §B.4's samples, and the next red carries its mechanism by construction. Say plainly in §0 that the desk did not reproduce. |

**B.4 The gate, sharpened (a hub ruling; Nick's word `SAMPLES: veto-only | none` in the brief, default veto-only):** FIX-1b's push run GREEN is the clearance. Then Nick fires `workflow_dispatch` on `main` at the landed sha **3×**; **a sample can VETO a clearance (any red → the gate re-opens and the red's XML is the next instrument), it can never GRANT one** — this is the "never re-run `main` CI" law's mechanism kept whole: no run other than the push run ever clears the gate.

### Configuration Parameters — none in production. The `vtParallelism` Gradle property is desk-only (documented in the conventions file's comment; CI never sets it).
### Event Types Produced or Consumed — none added. `DeliveryAnomaly` is an in-process signal, not an event; it never enters the store (INV: the bus does not publish about itself).
### Error Handling — the emitter never throws (swallow + continue); DP-2's terminal state is SUSPENDED, reached only after the bounded retry; every path that today returns/continues silently emits first.

## Locked Decisions That Apply
AMD-42 §3.4.2 (the mode FSM; SUSPENDED is a legal terminal; `onCaughtUp` single-shot — DP-2 must not re-fire it) · AMD-43 §3.6.2 (SEVEN metrics — add none) · AMD-45 §2.2 (atomic-checkpoint subscribers skip the per-delivery write — DP-2's re-queue must not write a checkpoint for a position it has not delivered) · LTD-09 / `NO_DIRECT_TIME_ACCESS` (timestamps from the injected `clock`; `parkNanos` is not a clock read) · LTD-11 (no `synchronized`; the existing `ReentrantReadWriteLock`/queue lock discipline) · LTD-15 / DECIDE-01 (SLF4J only in the composition root; the bus stays facade-free) · DEC-M3-14 (the bus holds no persistence types — the stub store in T1–T3 is a test type).

## Invariants That Must Hold
INV-BUS-02 (the publisher never blocks on subscriber state — `notifyEvent`'s new offer path must stay non-blocking) · the LIVE loop delivers each matching position at most once (DP-2's head re-queue must not duplicate a delivered position — assert in T5) · a subscriber's checkpoint never advances past an undelivered matching position (T6) · `HeroLoopHardwareFreeIT` and `ReplayTransitionIT` bounds byte-unchanged.

## P2 Consumer/Pin (Fan-Out) Survey (done at authoring; re-run the greps)
- `new InProcessEventBus(` — 4 files (`HomeSynapseCore.java:551` + 3 test files): untouched by the overload (delegating ctors). Re-grep; list the three test files in §2.
- `getDeclaredMethods().length` / shape tests in event-bus: `EventBusTest.java` pins the `EventBus` INTERFACE shape — the interface is untouched (the emitter is a ctor concern). Re-grep `hasSize(`/`isEqualTo(` over `core/event-bus/src/test` for a constructor-count or type-count pin; the MODULE_CONTEXT header count 33 → 34 is the only pin the hub found.
- `TransitionCoordinator(` construction sites — inside `InProcessEventBus` only (re-grep; a test constructing it directly gets the emitter).
- **ARCH-RULE-REACH:** Rules 1 (no `synchronized`), 2 (time), 4 (dependency direction — the bus gains no requires), 6 (package isolation — `DeliveryAnomaly` lives in `com.homesynapse.event.bus`), 5 (no filesystem in core — none). Zero collisions; state it.
- **JPMS / contract direction:** `DeliveryAnomaly`'s components are `String`, `long`, its own nested enum, `Instant` — `java.base` only. `module-info.java` byte-unchanged (embedded verbatim below; the P2 direction check is satisfied by construction).
- The `test-reports` artifact name changes (`test-reports-<run_number>`) — nothing consumes it programmatically (re-grep `.github/` for `download-artifact`).

**`core/event-bus/src/main/java/module-info.java` — VERBATIM at `dc3328b`; PROPOSED DIFF: none (byte-unchanged):**
```java
module com.homesynapse.event.bus {
    requires transitive com.homesynapse.event;

    // M3.3 (AMD-43): JFR-native bus metrics commit jdk.jfr.Event subclasses.
    // jdk.jfr is a JDK platform module but is NOT in java.base — JPMS requires
    // an explicit `requires` directive even though it ships with the JDK.
    requires jdk.jfr;

    exports com.homesynapse.event.bus;
}
```
**`lifecycle/lifecycle/src/main/java/module-info.java` — byte-unchanged** (it already `requires transitive com.homesynapse.event.bus` and `requires org.slf4j`; `DeliveryAnomaly` is consumed inside the composition root only — no exported-surface exposure, no transitive promotion). **`integration/integration-runtime`** — read-only in this WU.

## Test Requirements (tests first; red at HEAD unless marked)
| # | Test (class · method) | Red at HEAD? | Asserts |
|---|---|---|---|
| T1 | `DeliveryAnomalyEmissionTest.liveReadEmpty_emits` | RED (no emitter exists) | a LIVE subscriber whose store returns an empty page for position P receives `LIVE_READ_EMPTY(subscriberId, P)`; FIX-1a behaviour: the position is then skipped (assert the checkpoint does NOT advance to P) |
| T2 | `…liveReadFailed_emits` | RED | the store throws `RuntimeException("boom")` at P → `LIVE_READ_FAILED` with detail `RuntimeException: boom` |
| T3 | `…notifyNotVisible_emits` | RED | `notifyEvent(P)` when `readFrom(P-1,1)` is empty → `NOTIFY_NOT_VISIBLE("*", P)` |
| T4 | `…emitterNeverThrows` | RED | an emitter that throws does not propagate out of `notifyEvent`/the loop |
| **FIX-1b (branch a / c):** | | | |
| T5 | `…liveReadRetried_thenDelivered` | RED | the store returns empty for P on the first 2 reads, the envelope on the 3rd → delivered exactly once; checkpoint = P; no `LIVE_READ_EXHAUSTED` |
| T6 | `…liveReadExhausted_suspendsHonestly` | RED | empty for all 5 attempts → `LIVE_READ_EXHAUSTED`; mode SUSPENDED; checkpoint unchanged (never past P) |
| T7 | `…notifyNotVisible_stillOffersToLive` | RED | `notifyEvent(P)` with an invisible page offers P to the LIVE subscriber; when the store later shows P, it is delivered |
| T8 | `ReplayTransitionIT` unchanged — run ×20 under the §A.3 recipe on the FIX-1b tree | (a measurement, not a red-first row) | 20/20 GREEN, and the return states the pre-fix rate beside it |
| T9 | `HeroLoopHardwareFreeIT` unchanged — ×20 likewise | (measurement) | 20/20 GREEN; the pre-fix rate beside it |
| T10 | branch (b) only: the lifecycle test the stamps implicate | RED | per the evidence |
Existing suites: `:core:event-bus:test` 221 completed / 30 skipped at `dc3328b` (the filed CI log) → +4 (FIX-1a) / +3 (FIX-1b); `:lifecycle:lifecycle:test` 79 at #225 → unchanged. State the counts in §3.

## MODULE_CONTEXT.md Update
`core/event-bus/MODULE_CONTEXT.md`: header 33 → 34; `DeliveryAnomaly` (public record + nested `Kind`) in the Complete Type Inventory; Gotchas: (i) the LIVE loop never pages forward — offer-or-lose (FIX-1a), then retry-then-SUSPEND (FIX-1b); (ii) the emitter contract; (iii) the `vtParallelism` desk knob and why carrier count matters (SQLite native reads pin carriers). `lifecycle/lifecycle/MODULE_CONTEXT.md`: the `bus.delivery_anomaly` route.

## What to Watch Out For
- **Tests must inject `Clock`.** Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` in this module's test code. Use `Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC)` injected via constructor/`@BeforeEach`. **Enforcement reach:** `NO_DIRECT_TIME_ACCESS` runs from `com.homesynapse.app`'s test classpath, so it mechanically catches PRODUCTION code in every non-whitelisted module (plus app's own tests) — it does **not** scan this module's test source set. Clock-injection here is a self-enforced project convention that PM review, not `./gradlew check`, enforces.
- **A grep hit is a string, not a symbol** — verify every cited line at its declaration before you edit it; the hub's pins were read at `dc3328b` on 2026-09-04 but the lane owns the re-derivation.
- **The bus is SLF4J-free by design** (`QueueSaturationHealthCheck.java:41–:43`). If you find yourself importing `org.slf4j` in `core/event-bus`, stop — the composition root owns the transport.
- **`--continue` changes the shape of a red run, not its verdict**: the job still fails; the log now lists every failing task. Do not "fix" a failing module by removing it from `check`.
- **The loops are the WU's evidence, not its ceremony.** If a loop reproduces on run 3, keep going to 20 — the RATE is the datum the post-fix loop is compared against.
- **Never**: raise `awaitTrue`'s 500×20 ms, `awaitCheckpoint`'s bounds, add `@RepeatedTest`/retry plugins, or tag either IT out of `check`. Each is a bound-fix; the instruction forbids them by name.
- **Virtual threads + SQLite:** a VT inside a JDBC native call pins its carrier; with 2 carriers (the runner) two pinned VTs starve every other subscriber. This is a HYPOTHESIS the CPU-shape row of §A.5 tests — it is not a premise to code against.
- **`workflow_dispatch` is inert until the file with it is on the default branch** — FIX-1a's landing on `main` is what enables §B.4's samples; do not expect it to work from a branch.

## Coder Pushback Welcome
The DP-1 emitter shape (a typed record + `Consumer`) vs. a narrower alternative that keeps the bus facade-free; DP-2's retry parameters (5 attempts, 1→16 ms) if the measurement argues for others; whether `notifyEvent`'s unfiltered offer (DP-2) is acceptable for high-fan-out passive subscribers (say what it costs); any place the hub's line pins have drifted; the loop recipe's path trick. The FAILCHAN lane out-verified the hub twice — your source reads outrank this instruction's prose where they disagree, and you say so in §4.

## Out of Scope
An eighth JFR metric (AMD-43 amendment path) · any change to the seven canonical names · the hardware proof of FAILCHAN §6-B/EXITCODE (the next card session, on FIX-1b's artifact) · OR-JOURNALD-PRIO · CG-1/2/3 · the `HeroLoopHardwareFreeIT` §A2 census file (Nick's act) · `main` branch protection (Row 34) · a PR workflow.

## Success Criterion (binary)
DONE when: (1) FIX-1a's census is exactly the Files table (9 = 7 M + 2 A) or the deviation is declared in §0; T1–T4 ran RED at HEAD and GREEN after; `spotlessCheck` clean; `:core:event-bus:test` + `:lifecycle:lifecycle:test` GREEN on your desk with counts; (2) §A.5's table is filled from ≥60 real runs (HeroLoop fix1a ×20 · ReplayIT fix1a ×20 · HeroLoop ef02d13 ×20; + the CPU-shape row ×10) with the loop corpus at `nexsys-hivemind/context/audits/2026-09-05_FIX-1_loops/`; (3) FIX-1b's branch per class is declared FROM the table and its census + red-first tests (T5–T7, T10 as applicable) are in the return; T8/T9 20/20 with the pre-fix rate beside them; (4) both MODULE_CONTEXTs updated; (5) the WUCP Phase-1 checklist; (6) the return at `nexsys-hivemind/context/audits/2026-09-05_FIX-1_return.md`, §0 first, within cap. **The gate of record is CI on Nick's FIX-1b push (Build & Check, with `--continue` now reporting every task); §B.4's three dispatch samples may veto it, never grant it.**

## Work Unit Completion (WUCP Phase 1)
After your desk gates pass, execute WUCP Phase 1 from `nexsys-hivemind/context/protocols/work-unit-completion-protocol.md`: update the two MODULE_CONTEXT.md files; append the `coder-handoff.md` entry (Deferred Build Gate: YES — the full `./gradlew check` is CI on Nick's pushes, two of them; NEXT WU pointer: the hub's audit → the two msg files → Nick's FIX-1a commit + push (sample #4) → the loops' corpus → FIX-1b commit + push = the gate → §B.4 samples → CG-1/2/3 dispatches on the green); a `coder-lessons.md` note only if you learned one; the checklist in the return.

---
### DISPATCH LINE (Nick pastes into a host-side Claude Code session in `~/Desktop/Code/ClaudeFolder/homesynapse-core`)
```
date -u first. Boot as the nexsys-coder skill. Baseline: this tree must be at dc3328b and clean — verify with `git log -1 --format=%h` and `git status --porcelain` (STOP and report if not). Execute nexsys-hivemind/context/instructions/2026-09-04_coder-lane_FAILCHAN-FIX-1_CI-nondeterminism_coding-instruction.md exactly: read its §0 contract, the grounding audit §2–§4 it points at, and the minimum read set first. FIX1: class. Part A before Part B — the instruments (FIX-1a, census 9 = 7 M + 2 A, tests T1–T4 red at HEAD) and then the loops (§A.3/§A.4, ≥60 runs, the corpus to nexsys-hivemind/context/audits/2026-09-05_FIX-1_loops/); fill the §A.5 table BEFORE writing a line of FIX-1b; declare FIX-1b's branch per class from the table. Return ONE file at nexsys-hivemind/context/audits/2026-09-05_FIX-1_return.md, §0 card first, ≤12 KB target. Stage nothing; commit nothing; the hub audits and Nick commits FIX-1a first, then FIX-1b.
```
