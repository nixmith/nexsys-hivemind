<!--
file: context/instructions/2026-09-11_coder-lane_FIX-2b-i_bus-stall_pending-depth-and-thread-dump_coding-instruction.md
purpose: FIX-2b-i — the second instrument half of FIX-2 for OR-BUS-SILENT-DROP, cut on the first diagnostic-bearing runner red (core cc05a54; context/audits/2026-09-11_CI-cc05a54_red-read_first-diagnostic_v70-b8.md). Two discriminators, small: (A) every SubscriberSnapshot carries its pending-queue depth, so the diagnostic and the census say whether a position was offered and not consumed, or never offered; (B) on an await timeout the test writes a thread dump that includes virtual threads (jcmd Thread.dump_to_file on the test JVM; a platform-thread fallback) and prints the frames of the threads that matter, so the runner names the blocked frame. Plus the runner's own pinned-thread trace and the -D passthrough docketed at FIX-2a, both in the conventions' Test block. The fix (FIX-2b-ii) is authored on the first red that carries these.
audience: the Coder (a host-side Claude Code session on homesynapse-core at cc05a54; the Java slot) · the hub (audits the return)
state-type: coding instruction
status: ISSUE-READY (authored v70 beat 8, Fri 2026-09-11 ~21:2x CT; instrument 2026-09-12T02:10:48Z). Dispatches on Nick's word `FIX2B: go` (his paste is §12). The Java slot is free (FIX-2a landed at cc05a54; EXPLAIN-114a is held behind the gate).
baseline: core `cc05a54` (test(lifecycle): FIX-2a). Re-verify at issue: `git -C homesynapse-core log -1 --oneline` prints `cc05a54`; `git status --porcelain` is empty apart from paths under web-ui/dashboard/ (the HERO-1b lane).
evidence: the four mechanisms H1–H4 pre-registered in the audit's §2; the checkpoints of the three failures; `bus.soak_host: available_processors=2` on the runner.
-->

# FIX-2b-i — the stall gets a queue depth and a thread dump (event-bus + lifecycle tests + one build block)

## §0 The lane contract
- `date -u` first; CT = UTC−5 once. **Read-set:** this file · `context/audits/2026-09-11_CI-cc05a54_red-read_first-diagnostic_v70-b8.md` whole (6.7 KB) · `core/event-bus/src/main/java/com/homesynapse/event/bus/SubscriberSnapshot.java` whole · `InProcessEventBus.java` `:316–:388` (`notifyEvent`), `:525–:592` (`liveLoop`), `:593–:660` (`routeByMode`, `offerUnfiltered`), `:729–:748` (`buildSnapshot`) · `SubscriberRuntime.java` `:30–:50`, `:195–:245` (`pendingPositions`, `virtualThread`) · `core/event-bus/MODULE_CONTEXT.md` — the three `SubscriberSnapshot` mentions (`grep -n`) · the FIX-2a test files (`BusAwaitDiagnostic`, its test, `BusPositionCensusIT` `:100–:200` and `:370–:400`, `BusSoakIT` `:130–:180`, `:270–:290`, the hero IT `:600–:665`) · `api/rest-api/src/test/java/com/homesynapse/api/rest/DlqStatusEndpointTest.java` (six `new SubscriberSnapshot(` sites) · `build-logic/src/main/kotlin/homesynapse.java-conventions.gradle.kts` `:44–:80`.
- **Return path:** `context/audits/<CT filing date>_FIX-2b-i_return.md`. **Cap ≤12 KB is a CEILING, not a target;** the §0 card first (the verdict · the census counted from porcelain · P1–P4 adjudicated first · the measurement table · deviations by tag · the Deferred Build Gate line · `RETURNED <path> <bytes>` as the last line, printed to Nick).
- **The instrument limit:** `./gradlew :core:event-bus:test :api:rest-api:test :lifecycle:lifecycle:test --tests '*BusAwaitDiagnostic*' --tests '*BusPositionCensus*' --tests '*BusSoak*' --tests '*HeroLoop*' spotlessCheck --offline` is yours; `./gradlew check` is owed to CI on Nick's push. The desk will not reproduce the stall (FIX-2a measured 143 green loops); **the dump path is proven on the desk by a forced timeout** (§4-B's unit test), not by a real stall.
- **You commit nothing and stage nothing.** The census you leave is the Files table's, exactly. Pushback welcome (§9).

## §1 What this implements
**(A) `pendingDepth` on the snapshot.** `SubscriberSnapshot` gains one component, `int pendingDepth`, after `dlqDepth`: the size of the runtime's `pendingPositions` queue at the instant of the snapshot (`runtime.pendingPositions().size()` in `buildSnapshot`). The diagnostic's subscriber line and the census line gain ` pending=<n>`. With it, the red reads: `pending ≥ 1` on a subscriber whose checkpoint sits below the head = offered and not consumed (the loop is blocked or parked past its wake — H1/H2/H3-parked); `pending=0` with `checkpoint < head` on a matching subscriber = never offered (H3-fan-out).

**(B) The thread dump at the timeout.** A test helper `BusThreadDump` (lifecycle test source) with `static String capture(Path dir)`: (1) runs `<java.home>/bin/jcmd <pid> Thread.dump_to_file -format=text <dir>/threads-<epochMillis>.txt` with a 10 s process timeout (`ProcessHandle.current().pid()`; `System.getProperty("java.home")`); (2) if the file appears, returns a filtered rendering: every thread whose name starts with `hs-sub-`, plus every thread — platform or virtual — whose top 12 frames contain `com.homesynapse`, each as `bus.thread: name=<n> state=<s>` followed by its frames (at most 12) as `bus.thread_frame: <frame>`; the count of threads in the dump and the count printed as the first line `bus.thread_dump: threads=<total> shown=<k> file=<path>`; (3) if jcmd is absent or fails, falls back to `Thread.getAllStackTraces()` (platform threads only) with the first line `bus.thread_dump: source=platform_only threads=<n> shown=<k>`, and the reason on a second line. The three timeout paths (the hero IT's `timeoutDiagnostic`, `BusPositionCensusIT`'s, and the one `BusSoakIT` uses) append the dump text after the subscriber lines, print the whole to stdout, and throw the `AssertionError` whose message is the FIRST line plus the subscriber lines only (the XML `<failure message>` stays readable; the dump lives in `<system-out>`). The file is written under the test's temp dir and its path printed; nothing is asserted about it.

**(C) The conventions' Test block, two lines** (⛔ gated on Nick's word: `FIX2B: go` lands them; `FIX2B: go no-build` skips this row): `jvmArgs("-Djdk.tracePinnedThreads=short")` (JDK 21 prints a line with the frames whenever a virtual thread blocks while pinned — the H1 witness, on the runner, into the XML's stdout) and `systemProperty("homesynapse.soak.loops", providers.systemProperty("homesynapse.soak.loops").getOrElse("20"))` (the FIX-2a R1 passthrough; `BusSoakIT` keeps its env-var fallback). Ground the exact Kotlin DSL form against the file's existing `jvmArgs(...)` calls before you write it.

Nothing else in `src/main` changes. `InProcessEventBus` changes only in `buildSnapshot`.

## §2 Files (the table governs; M/A exact)
| Path | M/A | What |
|---|---|---|
| `core/event-bus/src/main/java/com/homesynapse/event/bus/SubscriberSnapshot.java` | M | `int pendingDepth` after `dlqDepth`; the javadoc names it (offered, not yet consumed) |
| `core/event-bus/src/main/java/com/homesynapse/event/bus/InProcessEventBus.java` | M | `buildSnapshot` passes `runtime.pendingPositions().size()` |
| `core/event-bus/MODULE_CONTEXT.md` | M | the snapshot's shape (7 components) where it is described |
| `api/rest-api/src/test/java/com/homesynapse/api/rest/DlqStatusEndpointTest.java` | M | the six constructor sites gain `0` for `pendingDepth` (compile-red at HEAD after A) |
| `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/BusAwaitDiagnostic.java` | M | ` pending=<n>` on the subscriber line; `render` unchanged otherwise |
| `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/BusAwaitDiagnosticTest.java` | M | the three constructor sites gain a depth; the pinned string gains ` pending=` |
| `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/BusThreadDump.java` | A | (B): `capture`, the filter, the fallback |
| `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/BusThreadDumpTest.java` | A | one test: `capture` on the live test JVM returns a text whose first line starts `bus.thread_dump:` and which contains the current test thread's own frame (`BusThreadDumpTest`); red at HEAD (the class does not exist) |
| `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/HeroLoopHardwareFreeIT.java` | M | `timeoutDiagnostic` appends the dump to stdout; the thrown message = the subscriber lines only |
| `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/BusPositionCensusIT.java` | M | the same in its `timeoutDiagnostic`; the census line gains ` pending=<n>` |
| `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/BusSoakIT.java` | M | no change if it calls the census IT's diagnostic; else the same edit (state which as `[INFO]`) |
| `lifecycle/lifecycle/MODULE_CONTEXT.md` | M | the FIX-2a entry gains the FIX-2b-i lines (pending=, the dump, how to read a red) |
| `build-logic/src/main/kotlin/homesynapse.java-conventions.gradle.kts` | M ⛔ | (C) the two lines in `tasks.withType<Test>().configureEach` |

Expected census: **13 = 11 M + 2 A** with (C); **12 = 10 M + 2 A** without it. Say which in the return's first line.

## §3 STOP-on-mismatch gates
| Where | Expected | Instrument |
|---|---|---|
| `SubscriberSnapshot.java:36–:43` | six components in the order `subscriberId, mode, checkpoint, dlqDepth, crashCount, oldestParkedAt` | `sed -n '36,43p'` |
| `InProcessEventBus.java:729–:738` | `buildSnapshot` constructs the record with those six | `sed -n '729,738p'` |
| `SubscriberRuntime.java:38, :201` | `LinkedBlockingQueue<Long> pendingPositions` and its package-private accessor | `sed -n '38p;201p'` |
| `new SubscriberSnapshot(` sites | exactly 10: rest-api test 6 · InProcessEventBus 1 · BusAwaitDiagnosticTest 3 | `git grep -c 'new SubscriberSnapshot(' -- '*.java'` |
| `homesynapse.java-conventions.gradle.kts:47–:63` | `tasks.withType<Test>().configureEach { useJUnitPlatform(); jvmArgs("-XX:+EnableDynamicAgentLoading"); … findProperty("vtParallelism") … }` | `sed -n '47,63p'` |
| the suite counts at HEAD | lifecycle 82 (FIX-2a's number); event-bus and rest-api as the fresh `--rerun` prints | the gradle XML sets |
| `jcmd` on the desk | `<java.home>/bin/jcmd(.exe)` exists | `ls "$JAVA_HOME/bin" \| grep jcmd` |

## §4 Technical specification
**A.** The record component is additive; every constructor site passes the depth (production: the queue size; tests: `0` or the value the test pins). The `SubscriberSnapshot` javadoc gains one sentence: "pendingDepth — positions offered to this subscriber's LIVE queue and not yet consumed at the snapshot instant; 0 in REPLAY/TRANSITION (those modes queue elsewhere)". `render` prints ` pending=` right after ` dlq=`. The census line prints ` pending=<n>` after ` dlq=<n>`.

**B.** `BusThreadDump.capture(Path dir)`: never throws — every failure path returns a text that begins `bus.thread_dump:` and says why. The jcmd invocation: `new ProcessBuilder(jcmd, pid, "Thread.dump_to_file", "-format=text", file).redirectErrorStream(true)`, `waitFor(10, SECONDS)`, destroy on timeout. The filter reads the text dump line by line (a thread block begins with `#<id> "<name>"`), keeps the blocks named `hs-sub-*` and the blocks whose first 12 frames mention `com.homesynapse`, and renders each as one `bus.thread:` line + `bus.thread_frame:` lines (≤12). The unit test forces nothing on the bus: it calls `capture` from the test thread and asserts the shape (first line prefix; its own class name present in some frame; the file exists when `source=platform_only` is absent). **The timeout paths:** `text = render(...) + "\n" + BusThreadDump.capture(tempDir)`; `System.out.println(text)`; `throw new AssertionError(renderOnly)`.

**C.** In the conventions' Test block, after the existing `jvmArgs("-XX:+EnableDynamicAgentLoading")`: `jvmArgs("-Djdk.tracePinnedThreads=short")` and the property passthrough. Then `BusSoakIT` reads the property first (it already does); verify with one run `-Dhomesynapse.soak.loops=3` → `loops=3` (the FIX-2a R1 measurement inverted).

## §5 Red-first predictions (adjudicate first; each names its artifact)
| # | Prediction | Inverse arm | Read from |
|---|---|---|---|
| P1 | After A, `DlqStatusEndpointTest` and `BusAwaitDiagnosticTest` are compile-RED (six + three sites) until their sites gain the depth; then GREEN; the pinned render string fails on text until ` pending=` is added | — | the gradle compile log; the XML |
| P2 | `BusThreadDumpTest` is compile-red at HEAD, then GREEN with `source=platform_only` ABSENT on the desk (jcmd present) | jcmd absent on the desk → the fallback line; report it, the runner may differ | the XML `<system-out>` |
| P3 | The soak and census stay GREEN on the desk (no stall to dump); the desk never exercises the timeout path beyond the unit test | a desk stall → the dump is the reading; file it whole | the XML |
| P4 | With C, `-Dhomesynapse.soak.loops=3` runs `loops=3` | still 20 → the DSL form is wrong; STOP with the file's line | the `bus.soak:` line |

## §6 The measurement table (fill in the return)
suite counts at HEAD / after (event-bus · rest-api · lifecycle) · the `BusThreadDumpTest` first line on the desk · the `-D` passthrough measurement · the soak line (one run) · the census line with `pending=` (one loop).

## §7 Locked decisions and invariants
No behaviour change on the bus (the snapshot gains a read-only field) · the FROZEN census token prefix unchanged (`pending=` is a trailing key, as FIX-2a's audit ruled) · the test-clock rule below · LTD-15 (no new production logging) · the diagnostic must never mask the timeout (every path throws).

## §8 What to watch out for
- **Tests must inject `Clock`.** Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` in this module's test code. Use `Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC)` injected via constructor/`@BeforeEach`. **Enforcement reach:** `NO_DIRECT_TIME_ACCESS` runs from `com.homesynapse.app`'s test classpath, so it mechanically catches PRODUCTION code in every non-whitelisted module (plus app's own tests) — it does **not** scan this module's test source set. Clock-injection here is a self-enforced project convention that PM review enforces. *(Exception in this WU: the dump file's `<epochMillis>` name in `BusThreadDump` may use `System.currentTimeMillis()` — a file name, not a measured quantity; say so in its javadoc.)*
- `pendingPositions()` is package-private in `com.homesynapse.event.bus`; `buildSnapshot` is in that package — no visibility change.
- The record's canonical constructor changes: every site is in the gate; a missed site is a compile error, not a runtime surprise.
- The dump can be large on the runner (hundreds of threads): the filter keeps it to the threads that matter; the full file stays on the runner's disk (not in the artifact unless the workflow uploads `build/test-results/**` only — it does; note it).
- `jcmd` needs the same JDK as the test JVM: use `java.home`, never `PATH`.
- Do not change the await timeout (500 × 20 ms); do not add retries.

## §9 Coder pushback welcome
If `jcmd` cannot attach on the desk (a Windows attach-listener quirk), say so and ship the fallback with the runner as the place it is proven; do not spend more than one probe on it. If the rest-api test's six sites carry a builder or fixture, use it and say so.

## §10 Out of scope
The fix itself (FIX-2b-ii) · any change to `liveLoop`, `notifyEvent` or the read executor · EXPLAIN-114a · the bench driver.

## §11 module-info (verbatim; NO change)
`core/event-bus/src/main/java/module-info.java` exports `com.homesynapse.event.bus` already; a record component is not a module change. `lifecycle`'s test source set already sees the bus types. Zero module-info edits; a needed edit = STOP.

## §12 Nick's paste (a host-side Claude Code session in `homesynapse-core`, on `main` at `cc05a54`)
```
date -u first. You are the Coder for FIX-2b-i on homesynapse-core (the nexsys-coder skill governs). Read ../nexsys-hivemind/context/instructions/2026-09-11_coder-lane_FIX-2b-i_bus-stall_pending-depth-and-thread-dump_coding-instruction.md WHOLE, then its §0 read-set by the ranges it names, then ../nexsys-hivemind/context/audits/2026-09-11_CI-cc05a54_red-read_first-diagnostic_v70-b8.md whole. Verify the baseline (git log -1 --oneline prints cc05a54; git status --porcelain is empty apart from web-ui/dashboard/ — the HERO-1b lane; never touch it) and every §3 gate before you write. Row C (the two build-logic lines) is IN unless this paste says no-build. Red-first as §5 states. Run the named gradle tasks with --offline; commit nothing; stage nothing. Write the return to ../nexsys-hivemind/context/audits/<today CT>_FIX-2b-i_return.md (≤12 KB; §0 card first; P1–P4 adjudicated first; the last line `RETURNED <path> <bytes>`) and say that one line to Nick.
```
