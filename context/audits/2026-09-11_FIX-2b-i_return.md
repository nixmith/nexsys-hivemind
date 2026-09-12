<!--
file: context/audits/2026-09-11_FIX-2b-i_return.md
purpose: Coder return for FIX-2b-i — the stall gets a queue depth (A) and a thread dump (B) + the conventions' two lines (C); §0 card first, P1–P4 first.
audience: the hub (audit) · Nick (commits)
state-type: lane return
status: DELIVERED 2026-09-11 CT — REPO-COMPLETE, LIVE-VERIFICATION PENDING (CI on the push = the gate of record; the dump on a real stall is the runner's to show)
-->

# FIX-2b-i return — pending depth · thread dump · the two build lines (2026-09-11 CT)

## §0 The card

**Verdict: DONE (repo-complete) WITH row C IN — 13 = 11 M + 2 A; 1 [REVIEW] + 7 [INFO]; nothing STOP-grade. P1–P4 all HELD; P2 on its main arm (jcmd attaches on this desk).** Instruction: `context/instructions/2026-09-11_coder-lane_FIX-2b-i_bus-stall_pending-depth-and-thread-dump_coding-instruction.md`; the audit `2026-09-11_CI-cc05a54_red-read_first-diagnostic_v70-b8.md` read whole. Baseline: core `main` HEAD `cc05a54`; porcelain at launch = the HERO-1b lane's 17 rows under `web-ui/dashboard/` only (untouched). Every §3 gate byte-exact at the instrument (six components in order · `buildSnapshot` six · `SubscriberRuntime:38/:201` · 10 sites = 6+1+3 · the Test block · `jcmd.exe` beside the toolchain JDK 21.0.4; CI's Corretto 21 ships one too). Instrument: `date -u` 02:27Z launch · 02:38Z HEAD suite · 02:48–02:51Z the reds and greens · 02:53–02:55Z the measurements · 02:58Z filing; CT = UTC−5 → **2026-09-11**.

**Census — CORE (`git --no-optional-locks status --porcelain`, the HERO-1b rows excluded): EXACTLY 13 = 11 M + 2 A + 0 D; ZERO staged; ZERO commits by the lane; `src/main` touched at TWO files (the record + `buildSnapshot`); module-info untouched; every file LF.** M `SubscriberSnapshot.java` (+15/−0) · M `InProcessEventBus.java` (+1/−0, `buildSnapshot` only) · M `core/event-bus/MODULE_CONTEXT.md` (2/2) · M `DlqStatusEndpointTest.java` (6/6) · M `BusAwaitDiagnostic.java` (8/2) · M `BusAwaitDiagnosticTest.java` (17/10) · M `HeroLoopHardwareFreeIT.java` (15/5) · M `BusPositionCensusIT.java` (29/15) · M `BusSoakIT.java` (6/3) · M `lifecycle/lifecycle/MODULE_CONTEXT.md` (6/1) · M `homesynapse.java-conventions.gradle.kts` (+15/−0) · A `BusThreadDump.java` (283 lines) · A `BusThreadDumpTest.java` (116). HIVEMIND: 1 A (this file) + 2 M (`coder-handoff.md` prepended at line 17; `coder-lessons.md` +1 lesson, now 25,075 B — the hub's rotation is due).

**P1–P4, adjudicated first:**
| # | Verdict | Read from |
|---|---|---|
| P1 | **HELD, staged** — the tests first (02:48:46Z): `BusAwaitDiagnosticTest` compile-red ×3 (`constructor SubscriberSnapshot … cannot be applied`) + `BusThreadDumpTest` ×3 (`cannot find symbol`); the record + `buildSnapshot` in (02:50:07Z): `:core:event-bus:compileJava` clean under `-Werror`, `DlqStatusEndpointTest` compile-red at EXACTLY `:55 :57 :121 :124 :126 :145`; the six sites `0` → rest-api GREEN 152/0 (02:50:47Z), the frozen A5 envelope untouched (`containsOnlyKeys` holds); the three sites → `BusAwaitDiagnosticTest` behaviour-red on the text (`expected … dlq=1 pending=2 behind=2`) → ` pending=` in `render` → GREEN (02:51:19Z) | the R1–R4 gradle logs · the XML `<failure message>`s · the green XML |
| P2 | **HELD, main arm** — compile-red at HEAD (above) → the inert seam → behaviour-red (`Expecting actual: "" to start with: "bus.thread_dump: "`) → GREEN with `source=platform_only` ABSENT: `bus.thread_dump: threads=22 shown=1 file=C:\…\junit-…\threads-1789181707645.txt`, the calling thread rendered (`Test worker` at `ProcessImpl.waitFor` under `BusThreadDump.capture` ← `BusThreadDumpTest.capture_…`). The fallback is proven on the desk by the test's forced arm (`bus.thread_dump: source=platform_only threads=<n> shown=<k>` + `bus.thread_dump_fallback: reason=forced_by_test`) | `TEST-…BusThreadDumpTest.xml` `<system-out>` |
| P3 | **HELD** — no await timed out in any run (soak 20/20 · 3/3 · 3/3 · 20/20 · 20/20; the census settled every time; hero 5/5): the timeout paths were never entered on this desk — the dump on a real stall is the runner's to show | the XML sets |
| P4 | **HELD, both ways** — `-Dhomesynapse.soak.loops=3` → `bus.soak: loops=3 ok=3` (02:53:37Z; the build-logic recompiled); the env var ALONE (`HOMESYNAPSE_SOAK_LOOPS=3`, no `-D`) → `loops=3` (02:54:04Z); neither → `loops=20` (02:54:43Z — the daemon retained no `-D`, so the 3 before it was the env var's) | `BusSoakIT.xml` `bus.soak:` per run |

**§6 The measurement table:**
| Row | Value | Artifact |
|---|---|---|
| suite counts at HEAD / after | event-bus 230/230 · rest-api 152/152 · lifecycle 82 → **83** (the full suite `--rerun`, 21 suites; +`BusThreadDumpTest`); the named classes 8 → 9; 0 failures; `spotlessCheck` green on every module | the 02:38Z / 02:55Z XML sets (`<testcase` counts) |
| `BusThreadDumpTest` first line, desk | `bus.thread_dump: threads=22 shown=1 file=…\junit-15365882913127254701\threads-1789181707645.txt` | the XML |
| the `-D` passthrough | `-D…=3` → `loops=3` · env `=3` alone → `loops=3` · neither → `loops=20` | `bus.soak:` ×3 |
| the soak line (default run) | `bus.soak_host: available_processors=24 vt_parallelism=default` · `bus.soak: loops=20 ok=20 timed_out=0 p50_ms=26 p99_ms=27 max_ms=27 anomalies=0` · `…_total: runs=20 subscribers=6 missed=0 unscored_missed=1`; `<== monitors:` 0 (nothing pinned) · `bus.delivery_anomaly` 0 across every XML | R7's `BusSoakIT.xml` + the greps |
| the census line with `pending=` (one loop) | `bus.position_census: subscriber=automation_engine matched=24 delivered=24 missed=0 first_missed=none checkpoint=24 dlq=0 pending=0` — `pending=0` on all six (`state_projection … dlq=0 pending=0 atomic=true`) | R7's `BusPositionCensusIT.xml` |

**Deviations by tag.**
- **[REVIEW] R1 — row C's passthrough form.** The instruction's literal `systemProperty("homesynapse.soak.loops", providers.systemProperty(…).getOrElse("20"))` sets the property on EVERY run, and `BusSoakIT.configuredLoops()` reads the property FIRST (`:213–:217`) — the env-var fallback the same sentence keeps would be dead code. Shipped the conditional form `providers.systemProperty("homesynapse.soak.loops").orNull?.let { systemProperty("homesynapse.soak.loops", it) }` — the exact line the FIX-2a return §0 R1 named and the FIX-2a intake audit §3 docketed; the default stays in ONE place (the test's 20). All three arms MEASURED (P4). The flip to the literal is one line, plus the MODULE_CONTEXT K sentence.
- **[INFO] I1** — `-format=plain`, not `text`: JDK 21's `Thread.dump_to_file` option domain is `plain|json` (`jcmd <pid> help Thread.dump_to_file`, probed 02:32Z); `text` only works because anything not `json` falls through to plain.
- **[INFO] I2** — the name prefix is `hs-`, a superset of the specified `hs-sub-`: that set (`hs-sub-<id>` VTs + `hs-sub-read-<id>`, `SqliteSubscriberReadExecutor:140`) is included whole; it adds persistence's `hs-read-<n>` (`PlatformThreadReadExecutor:160`) and `hs-write-0` (`PlatformThreadWriteCoordinator:62`), whose IDLE frames are JDK-only and invisible under the top-12 marker rule — H2's reading needs the idle executor visible too. Flip = one literal.
- **[INFO] I3** — `bus.thread:` carries two trailing keys after `state=`: ` virtual=<true|false>` (the dump's own marker; H1 is about VTs) and ` tid=<id>`. JDK 21's plain dump carries NO thread state: `state` is the live `Thread.State` of a platform thread read beside the dump; a VT reads `unknown` (its frames say parked/blocked/running). The fallback's second line is `bus.thread_dump_fallback: reason=<why>`.
- **[INFO] I4** — the shared static is now `timeoutDiagnostic(core, dumpDir, what, awaited)`; each IT holds its `@TempDir` in a `tempDir` field set first in `bootAndAdopt`; `BusSoakIT`'s three call sites pass it (the table's "no change" arm did not apply). The dump is captured on the gather-failure arm too.
- **[INFO] I5** — `BusThreadDumpTest` is ONE test with three arms (the live JVM · the render pinned byte-exact on a synthetic JDK 21 dump: 5 threads, 3 shown, the 12-frame cap, a marker past the cap excluded · the forced fallback); count stays 1; `renderPlainDump`/`platformOnly` are package-private seams for it.
- **[INFO] I6** — the lifecycle MODULE_CONTEXT's FIX-2a "K" sentence ("this build's Test tasks forward no -D") is rewritten in place — false after C; the `SubscriberSnapshot` javadoc's "0 in REPLAY/TRANSITION" carries one caveat: `resume()` (`InProcessEventBus:447–:452`) clears the DLQ but not `pendingPositions`.
- **[INFO] I7** — the wall-clock sweep over the new/changed Java finds only the named `System.currentTimeMillis()` file-name site (`BusThreadDump:98`, javadoc'd) and `BusSoakIT`'s pre-existing four `nanoTime` sites; no `synchronized`, no new production logging (LTD-15), no module-info edit.

**Deferred Build Gate: YES** — `./gradlew check` NOT run on this desk; owed to CI on Nick's push of exactly the 13 atop `cc05a54` (the gate of record; the runner's first sample WITH the depth and the dump). **Completion register: REPO-COMPLETE, LIVE-VERIFICATION PENDING.**

## §1 What changed (detail: the MODULE_CONTEXTs, the handoff entry)
`SubscriberSnapshot` +`int pendingDepth` after `dlqDepth`; `buildSnapshot` passes `runtime.pendingPositions().size()`. `render` and `renderTokens` print ` pending=` right after ` dlq=`. `BusThreadDump.capture(dir)`: `<java.home>/bin/jcmd(.exe) <pid> Thread.dump_to_file -format=plain <dir>/threads-<ms>.txt` (10 s `waitFor`, `destroyForcibly`; exit≠0 or no file = the reason) → the filtered rendering; else `platformOnly(reason)` over `Thread.getAllStackTraces()`; never throws. The three ITs' `timeoutDiagnostic` print `reading + "\n" + capture(tempDir)` and throw `AssertionError(reading)`. Row C: `jvmArgs("-Djdk.tracePinnedThreads=short")` + the conditional passthrough, both commented.

## §2 Gates run (JDK 21.0.4 · Gradle 8.8 · `--offline`; every test task `--rerun`)
R0 HEAD 02:38Z: event-bus 230 · rest-api 152 · the four classes 8, all green. R1 02:48Z compile-red ×6. R2 02:50Z rest-api compile-red ×6 + lifecycle ×3. R3 02:50Z rest-api 152/0 + two behaviour-reds. R4 02:51Z 2/2 green. R5/R6 02:53/02:54Z the P4 soaks. R7 02:54Z the allow-listed line + `--tests '*BusThreadDump*'` + `spotlessCheck`: 230 · 152 · 9 · spotless green everywhere. R8 02:55Z the full lifecycle suite 83/0.

## §3 Observations
- **O1 `[FORESIGHT-NOTE]`** — the dump FILE is deleted with the JUnit `@TempDir`; the `<system-out>` rendering IS the record. `dir = Path.of("build", "test-results", "test", "thread-dumps")` (the test JVM's cwd is the project dir) would put the WHOLE dump — every thread, carriers included — into the `test-reports-<run>` artifact; one line, the hub's call.
- **O2** — jcmd attaches to the Gradle test worker on Windows (same user). `jdk.tracePinnedThreads` printed nothing here; on the runner grep `<== monitors:`. Caveat: JDK 21 prints that trace FROM the pinned thread — if a CI run ever hangs at a pin, drop that flag first.
- **O3** — `awaitEnvelope` (the hero IT's confirm awaits) still throws the bare message — FIX-2a's docketed O3; not in this Files table.

## §4 WUCP Phase 1: Coder Closeout
- [x] MODULE_CONTEXT.md updated for: core/event-bus, lifecycle/lifecycle
- [x] coder-handoff.md updated (the DELIVERED entry prepended, newest-first; Deferred Build Gate + the NEXT WU pointer)
- [x] Deferred build gate flag: YES (`./gradlew check` → CI on Nick's push = the gate of record)
- [x] coder-lessons.md appended: the "a build-script default shadows the code's fallback chain" lesson (1,156 B)
- [x] Cross-agent note posted: Not needed (the channel is retired)
- [x] NEXT WU named: the hub's audit (rules R1) → Nick's commit (exactly the 13) + push → `ci` green = the gate AND the runner's first depth+dump sample → FIX-2b-ii on the first red that carries `pending=` and `bus.thread:` lines → EXPLAIN-114a
- Timestamp: 2026-09-12 02:58 UTC (Fri 2026-09-11 ~21:58 CT)

RETURNED context/audits/2026-09-11_FIX-2b-i_return.md 12215
