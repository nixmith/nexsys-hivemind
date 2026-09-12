<!--
file: context/audits/2026-09-11_FIX-2a_return.md
purpose: Coder return for FIX-2a — OR-BUS-SILENT-DROP, instrument first (A the await diagnostic · B the position census · C the bus soak); test-only; §0 card first, P1–P4 first.
audience: the hub (audit) · Nick (commits)
state-type: lane return
status: DELIVERED 2026-09-11 CT — REPO-COMPLETE, LIVE-VERIFICATION PENDING (CI on the push = the gate of record AND the runner's first soak sample)
-->

# FIX-2a return — the three instruments (2026-09-11 CT)

## §0 The card

**Verdict: DONE (repo-complete, test-only); 1 [REVIEW] + 8 [INFO]; nothing STOP-grade. P2 came back on its INVERSE ARM: the class does not reproduce in-process on this desk.** Instruction: `context/instructions/2026-09-11_coder-lane_FIX-2a_bus-silent-drop_instrument-first_coding-instruction.md`. Baseline: core `main` HEAD `1e26912`, porcelain empty at launch; NOT a re-paste (no prior return at this path). Every §3 gate byte-exact at the instrument (18 tracked test files; 79 at HEAD from a fresh `--rerun`; logback at `build.gradle.kts:79`; the two `requires transitive` lines). Preflight: Checks 1–7 PASS (`diff -rq` skill vs `nexsys-hivemind/coder` empty); Check 12 STALE-by-hygiene (the 08-22 RS3 brief + the 09-06 H8a packet still live — the hub's, as HONESTY-1 recorded). Instrument: `date -u` 00:36Z launch · 00:42Z HEAD suite · 00:44Z reds · 00:45Z green A · 00:53–00:56Z the runs · 01:0xZ filing; CT = UTC−5 → **2026-09-11**.

**Census — CORE (`git --no-optional-locks status --porcelain`): EXACTLY 6 = 2 M + 4 A + 0 D; ZERO staged; ZERO commits by the lane; ZERO files under `src/main`; module-info untouched.** M `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/HeroLoopHardwareFreeIT.java` (65/3) · M `lifecycle/lifecycle/MODULE_CONTEXT.md` · A `…/BusAwaitDiagnostic.java` · A `…/BusAwaitDiagnosticTest.java` · A `…/BusPositionCensusIT.java` · A `…/BusSoakIT.java`. HIVEMIND (this lane's rows only; the other rows at porcelain are the hub's beats): 1 A (this file) + 2 M (`coder-handoff.md` prepended at line 17; `coder-lessons.md` appended, one lesson).

**P1–P4, adjudicated first (every cell names its artifact):**
| # | Verdict | Read from |
|---|---|---|
| P1 | **HELD** — compile-red at HEAD 00:44:23Z (`cannot find symbol: variable BusAwaitDiagnostic` ×2, `compileTestJava FAILED`); behaviour-red with the inert render 00:44:40Z (`expected: "bus.await_timeout: …" but was: ""`); GREEN 00:45:14Z (`tests="1" failures="0"`) | the gradle log · `TEST-…BusAwaitDiagnosticTest.xml` `<failure message>`, then the green XML |
| P2 | **FAILED — the inverse arm, first-class.** 3 of 3 solo runs GREEN, and 7 of 7 at K=20 (140 loops) + 1 at K=3: `timed_out=0`, `anomalies=0`, scored `missed=0` on EVERY run, unpinned (24 cores) AND pinned to 2 carriers (`bus.soak_host: available_processors=2 vt_parallelism=2`). The class does not reproduce in-process on this desk in 60 (143) loops; the next instrument is the card's driver (TR-1b), not a fix — §11 | `TEST-…BusSoakIT.xml` `<system-out>` (`bus.soak:` lines, the table below) + `grep -c bus.delivery_anomaly` = 0 on every XML |
| P3 | **HELD** — p50 24–26 ms (< 250), p99 28–96 ms (< 2,000) on every green run; the pinned sample the widest (96) | the `bus.soak:` line per run |
| P4 | **HELD (green arm)** — after one loop `missed=0` for the five non-atomic subscribers AND `state_projection … missed=0 … atomic=true` (checkpoint 24 = head 24); the atomic lag shows only in the soak (`unscored_missed` 0–1) | `TEST-…BusPositionCensusIT.xml` `<system-out>` (00:53:08Z) |

**§7 The measurement table:**
| Row | Value | Artifact |
|---|---|---|
| suite count at HEAD / after | 79 / 82 (0 failed both; the XML `<testcase>` count — Gradle prints no count on green) | the 00:42Z and 00:56Z XML sets, `grep -o '<testcase ' *.xml \| wc -l` |
| soak runs, K=20: ok / timed_out | run1 20/0 · run2 20/0 · run3 20/0 (solo, 00:53:46/51/57Z) — also run0 20/0 (the three-class run), the `-D` run 20/0, PINNED 20/0, the full-suite run 20/0 | `BusSoakIT.xml` `<system-out>` per run (green runs = the summary line, per the corpus convention; nothing filed) |
| p50 / p99 / max (ms) | run1 26/68/68 · run2 26/59/59 · run3 26/59/59 — run0 26/29/29 · `-D` 26/68/68 · PINNED 24/96/96 · full 26/28/28 (n=20 ⇒ nearest-rank p99 = max) | the `bus.soak:` line |
| anomalies | 0 on every run; `grep -c bus.delivery_anomaly` = 0 on every XML (all 20 suites) | `bus.soak:` + the grep |
| census after one loop | `state_projection 24/24/0 atomic=true` · `automation_engine 24/24/0` · `command_dispatch_service 1/1/0` · `pending_command_ledger 5/5/0` · `integration_supervisor 2/2/0` · `registry_projection 4/4/0`; `total: runs=1 subscribers=6 missed=0 unscored_missed=0` | `BusPositionCensusIT.xml` |
| the diagnostic text of any timeout | none — no await timed out in any run; the exact render is pinned by `BusAwaitDiagnosticTest` | — |

**Deviations by tag.**
- **[REVIEW] R1 — the `-D homesynapse.soak.loops=N` override (§4-C, §12) cannot reach the forked test JVM as written.** `homesynapse.java-conventions.gradle.kts`'s `Test` block declares no `systemProperty` passthrough, so a `-D` on the gradlew line stays on the Gradle JVM — MEASURED: `-Dhomesynapse.soak.loops=2` ran `loops=20`. Shipped: the property first as specified, then the env var `HOMESYNAPSE_SOAK_LOOPS` (MEASURED: `=3` → `loops=3`; MODULE_CONTEXT documents it). The passthrough if the hub wants the `-D` spelling: in the conventions' `tasks.withType<Test>` block, `providers.systemProperty("homesynapse.soak.loops").orNull?.let { systemProperty("homesynapse.soak.loops", it) }` — a build-script row outside the Files table; not added.
- **[INFO] I1** — `awaitTrue(BooleanSupplier, String)` keeps its parameter list but drops `static` (the diagnostic needs `core`); zero static callers.
- **[INFO] I2** — §4-A's "exact six-line string" vs its own format: one header + one line per snapshot = 4 lines for three snapshots; the format governs; the single test pins the 4-line string and the `none`/empty-list arm (count stays 1).
- **[INFO] I3** — the census line appends ` checkpoint=<C> dlq=<D>` (+ ` atomic=true` / ` dlq_unscored=true`) AFTER the five frozen keys; the total's `missed` counts scored subscribers only with ` unscored_missed=<u>` appended — every frozen substring intact.
- **[INFO] I4** — the census settles before it is scored (re-read ≤ the 10 s window until every scored subscriber shows `missed=0`): an in-flight delivery is not a miss; a drop never resolves inside the window — the class's own definition.
- **[INFO] I5** — the shared code (manifest · census · tokens · paged store reads · `timeoutDiagnostic` · the one-automation YAML) lives as package-private statics in `BusPositionCensusIT`; the boot/await instance code is copied — the table stays at 6.
- **[INFO] I6** — two readings beyond the letter: the diagnostic's gather-failure fallback (an instrument never becomes the failure channel) and the `bus.soak_host:` line (`available_processors`, `vt_parallelism`) so a pinned sample reads beside an unpinned one.
- **[INFO] I7** — the MODULE_CONTEXT entry is `### FIX-2a` under `## Phase 3 Notes` (a `##` would leave the section); `:lifecycle:lifecycle:spotlessCheck` added to the desk gate; 7 soak samples reported, not 3.
- **[INFO] I8** — the ITs' boot copies the hero shape minus another leg's pins (CT-window, schema-composed); the readiness helper carries all FIVE ids.

**Deferred Build Gate: YES** — `./gradlew check` NOT run on this desk; owed to CI on Nick's push of exactly the 6 atop `1e26912` (the gate of record; that run's `BusSoakIT.xml` is the RUNNER's first soak sample). **Completion register: REPO-COMPLETE, LIVE-VERIFICATION PENDING.**

## §1 What changed, per file
- **`HeroLoopHardwareFreeIT.java`** (65/3): `+OptionalLong`, `+LongSupplier`; the step-3 await passes `() -> newestReportedPosition("occupied", "true")`; `awaitTrue` → instance + the `LongSupplier` sibling; `timeoutDiagnostic` (head = max `globalPosition` of `events()`, snapshots from `subscribers()`; println + `AssertionError(text)`); `NO_AWAITED_POSITION = -1` ⇒ `none`. No assertion changed; no retry; `awaitEnvelope` untouched.
- **`BusAwaitDiagnostic.java`** (A): `static String render(String, long, OptionalLong, List<SubscriberSnapshot>)` — the §4-A lines, `\n`-joined, no trailing newline. **`BusAwaitDiagnosticTest.java`** (A): 1 test — three snapshots (behind by 2 with `dlq=1`, `REPLAY` at 0, `LIVE` at head) → the exact string; then `awaited=none` + empty list → the header alone.
- **`BusPositionCensusIT.java`** (A): 1 test + the statics — `ManifestEntry` / `SubscriberCensus` (`scored() = !atomic && dlqDepth == 0`) / `SettledCensus`; `manifest()` (each filter from its registration site, cited); `census`; `awaitSettledCensus`; `renderTokens`; `allEvents` (paged); `timeoutDiagnostic(core, …)`; the store reads; `heroMotionConfigYaml()`.
- **`BusSoakIT.java`** (A): 1 test — baseline `occupied=false`; per loop `reportOccupied(true)` + `deliverAndCycle()` → `t0` → frame count ≥ loop+1 → `t1` → the loop's `command_issued(turn_on)` → `reportOnOff(true)` → `state_confirmed` joined to it → `occupied=false` + its report; timeout ⇒ summary printed, the error rethrown; `configuredLoops()`: property → env → 20.
- **`MODULE_CONTEXT.md`**: the `### FIX-2a` entry (the instruments · the grammars · the DLQ-depth limit · how to run + K · the first readings).

## §2 Gates run + counts (Windows 11 · JDK 21.0.4 · Gradle 8.8 · `--offline --console plain`)
HEAD `:lifecycle:lifecycle:test --rerun` 00:42Z → `compileTestJava` + `test` EXECUTED, 79, 0 failed. The three classes `--rerun` 00:53:05Z → `compileTestJava` EXECUTED under `-Xlint:all -Werror`; hero 5/5 (1.9 s) · census 1/1 (1.3 s) · soak 1/1 (1.4 s). Solo soak runs 00:53:44–54:00Z; `-D`/env 00:55:45/50Z; pinned 00:55:54–56:11Z (`cmd.exe /c start "" /affinity 3 /B /WAIT`, `ORG_GRADLE_PROJECT_vtParallelism=2`, `--no-daemon`); the full suite `--rerun` 00:56:11–30Z → 82, 20 suites `failures="0"`; `:lifecycle:lifecycle:spotlessCheck` EXECUTED, green. Wall-clock grep over the five files: only `BusSoakIT`'s two `System.nanoTime()` sites. The soak takes 1.4–2.5 s at K=20. Every touched file LF (`w/lf`).

## §3 Observations
- **O1 (= R1)** — the `-D` passthrough; the desk override is the env var. Only the affinity pin was run, no busy-load loops — the FIX-1 "both load levels" sweep is a follow-up if the runner sample reds.
- **O2** — in-process the pipeline is fast: p50 ≈ one poll (26 ms) from the report entering the adapter to the On frame back at the NCP; the p99 outliers (59–96 ms) are single loops. `state_projection`'s checkpoint rests one position behind the head after a soak (`unscored_missed=1`) — AMD-45's cadence.
- **O3 `[FORESIGHT-NOTE]`** — `awaitEnvelope` (the hero IT's confirm awaits) still throws the bare message; routing it through `timeoutDiagnostic` is one line each — outside this row.
- **O4** — the runner's first soak sample is CI on the landing push: read `BusSoakIT.xml`'s `bus.soak_host:`/`bus.soak:` lines there; a red on it carries the (A) reading in its `<failure message>`.

## §4 WUCP Phase 1: Coder Closeout
- [x] MODULE_CONTEXT.md updated for: lifecycle/lifecycle
- [x] coder-handoff.md updated (the DELIVERED entry prepended, newest-first; Deferred Build Gate + the NEXT WU pointer)
- [x] Deferred build gate flag: YES (`./gradlew check` → CI on Nick's push = the gate of record)
- [x] coder-lessons.md appended: the `-D`-never-reaches-the-test-worker lesson (≤1,200 B)
- [x] Cross-agent note posted: Not needed (the channel is retired)
- [x] NEXT WU named: the hub's audit (rules R1) → Nick's commit (exactly the 6) + push → `ci` green = the gate AND the runner's soak sample → TR-1b's card driver / FIX-2b on these readings → EXPLAIN-114a
- Timestamp: 2026-09-12 01:0x UTC (Fri 2026-09-11 ~20:0x CT)

RETURNED context/audits/2026-09-11_FIX-2a_return.md 12175
