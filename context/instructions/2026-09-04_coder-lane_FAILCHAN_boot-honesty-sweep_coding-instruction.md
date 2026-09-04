<!--
file: context/instructions/2026-09-04_coder-lane_FAILCHAN_boot-honesty-sweep_coding-instruction.md
purpose: THE FAILCHAN CODING INSTRUCTION — R-10 Row 6 RULED (a) + EXITCODE RULED (a) (Nick, 2026-09-03 ~20:40 CT; the record: context/strategy/2026-09-04_R10-sitting_THE-WORDS_ruling-record.md). One Coder lane on homesynapse-core: (A) the unit stops lying about a clean stop — `SuccessExitStatus=143` + the `Restart=` ruling + a unit-directive lint + the run-smoke stop assert; (B) the `ExitCode` contract is WIRED — `Main` exits with the documented code on a fatal startup failure (Nick's caveat as a constraint: `System.exit` in `main` after teardown, never in a shutdown hook; the mapping unit-tested behind a seam, the exit not); (C) the orderly-path emission sweep as a classification table with one ruling per instance (§10-O FIXED · §10-M classified at source · §10-I ROUTED). Zero hardware. Authored by the v62 hub at beat 3 on source read at HEAD ef02d13.
audience: the Coder lane (host-side Claude Code, homesynapse-core) · Nick (dispatch + commit) · the hub (audit)
state-type: coding instruction
status: ISSUE-READY — dispatch-as-word (Row 6 (a) + EXITCODE (a) are ruled). baseline: core `ef02d13` CLEAN (re-verify at issue: `git -C homesynapse-core log -1 --format=%h` must print ef02d13; if not, STOP and report). Return path + cap: §0. One lane on the core tree until the return is audited.
-->

# Coding Task: FAILCHAN — the boot-honesty sweep (the unit's exit contract made true; healthy outcomes stop reporting through failure channels)

**Subsystem:** distribution (systemd unit + smoke) · app (composition root) · lifecycle (startup-failure report) · integration-zigbee (one orderly-path emission)
**Design Doc:** Doc 12 — Startup, Lifecycle & Shutdown (Locked Phase 2): §3.9 shutdown, §6.3 the fatal set, **C12-04** (fatal failures produce a diagnostic exit: non-zero code + a structured log entry naming subsystem, phase, exception, recommendation), C12-06 (SIGTERM → exit ≤ 30 s); LTD-13 (systemd deployment). Doc 08 §5.1 (the production cycle) for Part C.
**Phase:** 3-Implementation
**Task Brief Reference:** R-10 Row 6 (a) — the OR-FAILCHAN sweep charter (the docket cards, Row 6; O-2 measured 2026-09-03 03:10Z on `hs-fresh`: `Result=exit-code · ExecMainCode=1 · ExecMainStatus=143 · ActiveState=failed` after ONE clean stop) + EXITCODE (a) — the v62 beat-1 grounding audit §1.1 (`context/audits/2026-09-03_v62-b1_boot-grounding_docs-and-strategy_validation.md`).

## §0 The lane contract (read first)
- **`date -u` FIRST** — every stamp in your return derives from it (the lane clock law). State your instrument limit (host clock; no Pi) and re-derive CT as UTC−5 once at the top.
- **Return path:** `nexsys-hivemind/context/audits/2026-09-04_FAILCHAN_return.md` — ONE file. **Shape:** §0 card FIRST (≤3 KB: the census `N = a M + b A` with exact paths · the verdict per part A/B/C · the red-first table ≤2.5 KB · deviations by tag) · then §1 what changed per file · §2 the gates run + counts · §3 pushback/observations · §4 the WUCP Phase-1 checklist. **Cap:** ≤12 KB target, hard ceiling ~17 KB (a cap is a per-section budget, not a ceiling to trim toward).
- **Baseline:** `ef02d13`. Line numbers below are from that HEAD; if a cited line has shifted by a few lines, report-and-proceed (`[INFO]`); if a cited construct is ABSENT, STOP and report.
- **Build discipline:** you MAY run targeted Gradle on your desk (`./gradlew :app:homesynapse-app:compileJava :app:homesynapse-app:test :lifecycle:lifecycle:compileJava :lifecycle:lifecycle:test :integration:integration-zigbee:compileJava :integration:integration-zigbee:test spotlessCheck --offline`) — GREEN in one round is the target; the full `./gradlew check` and the install-smoke matrix are Nick's push → CI = the gate of record. `bash -n` every touched shell file; `systemd-analyze --man=no verify` on the unit if your desk has systemd (WSL has it).
- **You do NOT commit.** Stage nothing. The hub audits the return, writes the msg file; Nick commits exactly the census.
- **Tests first** (red-first): every new test is written and RUN RED at HEAD (or declared green-by-construction, disclosed) before the production edit; the return's red-first table shows the two runs.

## What This Implements
Two boot-honesty defects measured on the shipped artifact, plus the class they belong to. (A) The JVM catches SIGTERM, runs the shutdown hook, and exits **143** by contract; the unit has no `SuccessExitStatus=`, so systemd grades every clean `systemctl stop` as `failed` (measured twice: R-3a §6-B; O-2 on `hs-fresh`). (B) `ExitCode` (10/11/12/13/99) is defined and DOCUMENTED as the unit's restart contract (`RestartPreventExitStatus=10`, `boot-contract-map.md` §"Exit codes → restart policy") but referenced by nothing: `Main.main` is `throws Exception`, `manager.start()` is unwrapped, `HomeSynapseCore.start()` re-throws the fatal after teardown → the JVM exits **1** → a deterministic bad config restart-loops every 10 s until `StartLimitBurst=5/300 s` — the loop the unit's own comment says it prevents. C12-04 is half-built (the log line exists, the code does not). (C) The same shape recurs in the adapter: an ORDERLY serial close is reported as `zigbee.transport_failed` and fed to the port watchdog. Never-false-ALIVE guards against claiming health that is not there; this WU guards against claiming FAILURE that is not there.

## Files to Read Before Starting (minimum read set — MANDATORY)
| File | Why |
|---|---|
| `app/homesynapse-app/MODULE_CONTEXT.md` (head + Gotchas) | the apex module; `ExitCode`'s documented purpose (Doc 12 §6 ↔ ExitCode values) |
| `app/homesynapse-app/src/main/java/module-info.java` | verbatim below — NO change expected (assert) |
| `app/homesynapse-app/src/main/java/com/homesynapse/app/Main.java` (whole, 267 lines) | the composition root; the hook at :121–:130; `manager.start()` at :148; the latch park at :154–:161 |
| `app/homesynapse-app/src/main/java/com/homesynapse/app/ExitCode.java` (whole) | the contract you are wiring; `code()` at :50 |
| `app/homesynapse-app/src/test/java/com/homesynapse/app/MainSchemaFragmentsTest.java` | the app test-tree pattern (PKG-SEC-2) |
| `app/homesynapse-app/src/test/java/com/homesynapse/app/HomeSynapseArchRules.java` | the 11 rules; none forbids `System.exit`; Rule 2 whitelists `com.homesynapse.app` for time |
| `lifecycle/lifecycle/MODULE_CONTEXT.md` (head + the PKG-SEC-2/R-9 gotchas + Gotchas) | the composition-root contracts; `schemaLock`; the `abandon()` semantics |
| `lifecycle/lifecycle/src/main/java/module-info.java` | verbatim below — NO change expected (assert) |
| `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java` — regions: `start()` :424–:450 · `bootstrap()` :452–:820 (the `setPhase` markers at :454/:464/:499/:533/:740/:753/:757/:818 and the `recordSubsystem` calls at :496/:529/:530/:560/:609/:735/:741/:809) · `shutdown()` :829–:840 · `doTeardown` (:1175–:1250) · `abandon()` :1116–:1170 · `recordSubsystem` :1564 | the failure catch you are enriching; the phase/subsystem markers you are reading |
| `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/SystemLifecycleManager.java` (whole) | the interface gaining one default method |
| `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/LifecyclePhase.java` | the enum you will carry in the report |
| `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/HomeSynapseCoreSchemaAdmissionTest.java` + `LifecycleWiringTest.java` | the temp-dir core-construction pattern; the one test-side `implements SystemLifecycleManager` (a default method must not break it) |
| `platform/platform-systemd/src/main/java/module-info.java` | verbatim below — read-only context (the unit's readiness story); NO change |
| `distribution/systemd/homesynapse.service` (whole, 133 lines) | Part A; :18–:20 the start limit · :55–:59 the stop budget · :61–:66 the restart block · :111–:130 the DANGER note (do not touch) |
| `distribution/smoke/run-smoke.sh` (whole, 213 lines) | Part A: the `ok`/`bad` helpers :26–:28; §8 STOP at :186–:193 |
| `distribution/smoke/version-grammar-test.sh` | the fixture-paired lint pattern to match for the new unit-directive lint |
| `.github/workflows/install-smoke.yml` :67–:86 AND `distribution/ci/install-smoke.yml` :67–:86 | the static-lint step (TWO COPIES — edit both identically; `diff -q` them in the return) |
| `distribution/docs/boot-contract-map.md` §"Exit codes → restart policy" (:100–:108) + §"Shutdown" | the operator-facing contract map you update |
| `integration/integration-zigbee/MODULE_CONTEXT.md` (head + §F-R4-1 + Gotchas) | Part C context; the log-token inventory discipline |
| `integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/ZigbeeIntegrationAdapter.java` — `stopSignal` :184 · `close()` :439–:447 · `productionLoop()` :801–:827 (the `transport_failed` arm :814–:817) · `attemptReopen()` :841–:874 | Part C |
| the adapter's existing scenario tests (find: `grep -rln 'productionLoop\|TransportFailureException' integration/integration-zigbee/src/test`) + the fake transport in `src/testFixtures` | the harness for the §10-O test |
| `nexsys-hivemind/context/lessons/coder-lessons.md` (newest 5) | the lane's own standing lessons |

**Verbatim `module-info.java` (baseline ef02d13) — assert byte-unchanged at handoff:**

`app/homesynapse-app/src/main/java/module-info.java`:
```java
module com.homesynapse.app {
    requires com.homesynapse.lifecycle;
    requires com.homesynapse.observability;
    requires com.homesynapse.event;
    requires com.homesynapse.device;
    requires com.homesynapse.state;
    requires com.homesynapse.persistence;
    requires com.homesynapse.event.bus;
    requires com.homesynapse.automation;
    requires com.homesynapse.integration;
    requires com.homesynapse.integration.runtime;
    requires com.homesynapse.integration.zigbee;
    requires com.homesynapse.config;
    requires com.homesynapse.api.rest;
    requires com.homesynapse.api.ws;
    requires com.homesynapse.platform;
}
```
`lifecycle/lifecycle/src/main/java/module-info.java` (directives only; the comments stand):
```java
module com.homesynapse.lifecycle {
    requires transitive com.homesynapse.observability;
    requires transitive com.homesynapse.event;
    requires transitive com.homesynapse.platform;
    requires transitive com.homesynapse.persistence;
    requires transitive com.homesynapse.event.bus;
    requires transitive com.homesynapse.state;
    requires transitive com.homesynapse.integration;
    requires com.homesynapse.integration.runtime;
    requires com.homesynapse.api.rest;
    requires com.homesynapse.config;
    requires transitive com.homesynapse.device;
    requires com.homesynapse.automation;
    requires com.homesynapse.platform.systemd;
    requires io.javalin;
    requires org.eclipse.jetty.util;
    requires org.slf4j;
    exports com.homesynapse.lifecycle;
}
```
`platform/platform-systemd/src/main/java/module-info.java`: `module com.homesynapse.platform.systemd { requires transitive com.homesynapse.platform; requires org.slf4j; exports com.homesynapse.platform.systemd; }` — read-only.

**Surface-export check (addition #14), done at authoring:** the ONE new public type, `StartupFailureReport(LifecyclePhase phase, String subsystem, String recommendation)`, lives in the already-exported `com.homesynapse.lifecycle` and names only in-module + `java.base` types → **zero module-info changes**, zero Gradle changes. If you find yourself adding a `requires`, STOP — the design is wrong.

## Files to Create or Modify (the Files table governs — addition #2)
| Action | File Path | Description |
|---|---|---|
| MODIFY | `distribution/systemd/homesynapse.service` | Part A: `SuccessExitStatus=143` · `Restart=on-failure` → `Restart=always` · the :61–:66 comment rewritten to the ruled contract · the header (:2–:13) gains one line naming FAILCHAN; the DANGER block :111–:130 byte-unchanged |
| CREATE | `distribution/smoke/unit-directives-test.sh` | Part A: the fixture-paired unit-directive lint (the seven required lines, each exactly once) |
| MODIFY | `.github/workflows/install-smoke.yml` | Part A: the static-lint step runs the new lint after `systemd-analyze verify` |
| MODIFY | `distribution/ci/install-smoke.yml` | Part A: byte-identical to the above (the two-copy rule; `diff -q` in the return) |
| MODIFY | `distribution/smoke/run-smoke.sh` | Part A: §8 STOP asserts `Result=success` + `ActiveState=inactive` after `systemctl stop` (the O-2 measurement inverted into a gate) |
| MODIFY | `distribution/docs/boot-contract-map.md` | Part A+B: the "Exit codes → restart policy" and "Shutdown" sections state the ruled contract |
| CREATE | `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/StartupFailureReport.java` | Part B: public record `(LifecyclePhase phase, String subsystem, String recommendation)` |
| MODIFY | `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/SystemLifecycleManager.java` | Part B: `default Optional<StartupFailureReport> lastStartupFailure() { return Optional.empty(); }` |
| MODIFY | `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java` | Part B: the `initializing` marker set before each fatal-set subsystem init; the `start()` catch records the report + emits the C12-04 line; `lastStartupFailure()` override |
| CREATE | `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/HomeSynapseCoreStartupFailureTest.java` | Part B tests (T4–T7) |
| CREATE | `app/homesynapse-app/src/main/java/com/homesynapse/app/ExitCodes.java` | Part B: package-private final class; `static ExitCode forStartupFailure(Optional<StartupFailureReport>)` — the pure mapping |
| MODIFY | `app/homesynapse-app/src/main/java/com/homesynapse/app/Main.java` | Part B: the `sigtermReceived` flag on the hook; `manager.start()` wrapped; the exit path |
| CREATE | `app/homesynapse-app/src/test/java/com/homesynapse/app/ExitCodesTest.java` | Part B tests (T1–T3) |
| MODIFY | `integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/ZigbeeIntegrationAdapter.java` | Part C §10-O: the orderly-close arm |
| MODIFY | the adapter scenario test class you identify (name it in the return) | Part C test (T8) |
| MODIFY | `app/homesynapse-app/MODULE_CONTEXT.md` · `lifecycle/lifecycle/MODULE_CONTEXT.md` · `integration/integration-zigbee/MODULE_CONTEXT.md` | WUCP Phase 1: the new contract + gotchas (spec in §MODULE_CONTEXT below) |
| MODIFY (hivemind) | `nexsys-hivemind/context/handoff/coder-handoff.md` · `nexsys-hivemind/context/lessons/coder-lessons.md` (if a lesson) | WUCP Phase 1 |

Expected census: **core 18 = 13 M + 5 A** (M: the unit · both `install-smoke.yml` · `run-smoke.sh` · `boot-contract-map.md` · `SystemLifecycleManager` · `HomeSynapseCore` · `Main` · the adapter · the adapter test · 3 MODULE_CONTEXT; A: the lint · `StartupFailureReport` · `HomeSynapseCoreStartupFailureTest` · `ExitCodes` · `ExitCodesTest`). If you touch a different/extra file, say so in §0 — the census is a claim about the diff that exists.

## Technical Specification

### Part A — the unit stops lying (Row 6 (a), ruled)

**A.1 `SuccessExitStatus=143`.** The JVM's SIGTERM path (hook runs → `exit(128+15)`) is the contract; the unit declares it. Add under `KillSignal=SIGTERM` (:57) the line `SuccessExitStatus=143` with a one-line comment: `# The JVM exits 143 after a caught SIGTERM (hooks run first) — a clean stop, by contract; SIGKILL (137) still grades as failure.`

**A.2 THE `Restart=` RULING — `Restart=always` (the hub's reconciliation of the OR-FAILCHAN §6 note with Row 6's rec; Nick's word 09-03 confirms the pair).** The §6 note preferred an app-side exit 0 because a unit-side 143 "would mask a genuine kill." Weighed at source: (i) systemd's DEFAULT already treats death-by-SIGTERM as clean for every non-JVM service — the JVM merely converts the signal to an exit code; declaring 143 restores the default semantics, it does not weaken them; (ii) SIGKILL/OOM (137) and every `ExitCode` (10/11/12/13/99) still grade as failure; (iii) an app-side exit 0 needs a signal HANDLER (`sun.misc.Signal`, `jdk.unsupported`) because `System.exit` from inside a shutdown hook deadlocks — a JPMS/jlink cost and an internal-API dependency for no honesty gain. **The relaunch half:** with 143 = success, a stray external SIGTERM (not from systemd) would no longer trigger `on-failure` and the service would stay silently down — so the unit takes `Restart=always`: it relaunches after ANY exit the operator did not order (`systemctl stop` never triggers a restart, by systemd's own rule), `RestartPreventExitStatus=10` still refuses to loop on a deterministic config failure, and `StartLimitBurst=5/300 s` bounds everything else. Rewrite :61–:66 as:
```
# Restart policy keyed to the ExitCode contract (FAILCHAN, 2026-09-04; wired in Main):
# a clean stop is exit 143 (SuccessExitStatus above) and is never restarted because
# systemd never restarts a unit it stopped itself; every other exit relaunches
# (Restart=always — a stray SIGTERM or a crash must not leave the house dark) EXCEPT
# CONFIGURATION_FAILURE (10), which is deterministic — a bad config fails identically on
# every restart, so it is surfaced, not looped. StartLimitBurst bounds the rest.
Restart=always
RestartSec=10
RestartPreventExitStatus=10
```
Do not touch the DANGER block (:111–:130): its `Restart=on-watchdog` line is a commented record of the eventual notify-shape unit and is out of scope.

**A.3 The unit-directive lint (`distribution/smoke/unit-directives-test.sh`, CREATE).** Fixture-paired like `version-grammar-test.sh`: takes the unit path (default `distribution/systemd/homesynapse.service`), asserts each of these lines is present EXACTLY ONCE as an active (uncommented) directive — `Type=exec` · `KillSignal=SIGTERM` · `SuccessExitStatus=143` · `Restart=always` · `RestartPreventExitStatus=10` · `StartLimitBurst=5` · `ExecStartPost=/opt/homesynapse/libexec/health-probe.sh --wait --timeout 90 --health-path /health`; prints `PASSED ✓ (7 directives)` or lists the misses and exits 1; `bash -n`-clean and dash-clean (`sh -n`). Wire it into BOTH `install-smoke.yml` copies immediately after the `systemd-analyze` block, before `echo "unit directives verified"`: `bash distribution/smoke/unit-directives-test.sh`. **Red-first:** at HEAD it FAILS on two lines (no `SuccessExitStatus`; `Restart=on-failure`) — show the run.

**A.4 The run-smoke stop assert (`run-smoke.sh` §8).** After `systemctl stop "${HS_UNIT}"` and the 2 s sleep, add: read `RES=$(systemctl show -p Result --value "${HS_UNIT}")`, `ST=$(systemctl show -p ActiveState --value "${HS_UNIT}")`, `EX=$(systemctl show -p ExecMainStatus --value "${HS_UNIT}")`; `ok "clean stop grades success (Result=${RES} ExecMainStatus=${EX})"` iff `RES = success` AND `ST = inactive`, else `bad "clean stop graded ${RES}/${ST} (ExecMainStatus=${EX}) — the §6-B lie"`. The no-systemd arm is unchanged. **This is the mechanical confirmation of §6-B on the install-smoke runner (Nick's push) and on the card (R-4b's first `systemctl stop`).** Red-first: on any systemd host it reads `exit-code/failed/143` at HEAD (the O-2 measurement) — if your desk cannot run the installed unit, declare the row *red-by-measurement (O-2)* and let CI show the green.

**A.5 `boot-contract-map.md`.** "Exit codes → restart policy": state the wired contract (Part B) and the three lines; "Shutdown": the 143-is-clean sentence + the hook-never-exits rule (B.4).

### Part B — the `ExitCode` contract, wired (EXITCODE (a), ruled; Nick's caveat is a constraint)

**B.1 `StartupFailureReport` (lifecycle, public record).** `record StartupFailureReport(LifecyclePhase phase, String subsystem, String recommendation)`; compact ctor `requireNonNull` all three; `subsystem` is one of the `recordSubsystem` names (`configuration` · `persistence` · `event-bus` · `device-model` · `state-store` · `automation` · `rest-api` · `observability` · `integration`) or `"unknown"`; `recommendation` is the C12-04 hint (see B.3). Javadoc: the C12-04 contract; produced only by `start()`'s fatal path.

**B.2 `SystemLifecycleManager.lastStartupFailure()`** — `default Optional<StartupFailureReport> lastStartupFailure() { return Optional.empty(); }` with Javadoc: present iff the most recent `start()` threw from `bootstrap()`; empty before start, after a successful start, and for the pre-bootstrap `IllegalStateException("already started")`. A `default` so `LifecycleWiringTest`'s test double and any fixture need no edit (verify: grep every `implements SystemLifecycleManager`).

**B.3 `HomeSynapseCore`.** (i) A private field `private volatile String initializing = "unknown";` set IMMEDIATELY before each fatal-set subsystem's init inside `bootstrap()`, using the exact `recordSubsystem` names: `"configuration"` before `configurationService.load()` (:495 region) · `"persistence"` before the persistence factory build (Phase 2) · `"event-bus"` before the bus build (Phase 2 — the two are recorded together at :529–:530, so the marker is what tells them apart) · `"device-model"` · `"state-store"` · `"automation"` (Phase 3, at their respective inits) · `"rest-api"` before `bringUpHttpSurface()` (Phase 5) · `"observability"` (Phase 4) · `"integration"` (Phase 6). (ii) In `start()`'s catch (:441): BEFORE the teardown call, build `lastStartupFailure = Optional.of(new StartupFailureReport(phase, initializing, recommendationFor(initializing)))` (a private static switch: configuration → `"check the configuration file (config.yaml + integrations/) — a schema or syntax error is deterministic; the unit does not restart on it"` · persistence → `"verify the event store file and disk; run the integrity check; restore from the pre-upgrade snapshot if corrupt"` · event-bus → `"report: the in-process bus failed to initialize — a defect, not an operator condition"` · default → `"inspect the log and the JFR recording; report with the phase and subsystem named"`), and REPLACE the :442 line with the C12-04 structured line: `LOG.error("lifecycle.startup_failed: phase={} subsystem={} recommendation=\"{}\" — tearing down initialized subsystems", phase, initializing, recommendation, fatal);` (the throwable last → stack trace). (iii) The re-throw at :448 stays EXACTLY as is (`throw fatal;`) — every existing test that pins `start()`'s thrown type keeps passing (one test file asserts on it today; verify by grep and list it in the return). (iv) `@Override public Optional<StartupFailureReport> lastStartupFailure()` returns the field. Reset the field to `Optional.empty()` at the top of `start()` (a second `start()` is illegal anyway, but the reset keeps the contract literal).

**B.4 `Main` — the exit path (the constraint).** (i) The hook gains a flag: `AtomicBoolean sigtermReceived = new AtomicBoolean()` set `true` as the FIRST statement inside the hook's `try`, before `manager.shutdown("SIGTERM")`. (ii) Wrap ONLY `manager.start()` (:148):
```java
try {
    manager.start();
} catch (Exception fatal) {
    if (sigtermReceived.get()) {
        // Doc 12 §6.5: SIGTERM arrived mid-bootstrap; the hook owns the exit (143 — clean
        // by the unit's SuccessExitStatus). A System.exit here would block forever:
        // Runtime.exit during a running shutdown sequence never returns.
        return;
    }
    ExitCode code = ExitCodes.forStartupFailure(manager.lastStartupFailure());
    System.err.println("HomeSynapse Core exiting: code=" + code.code() + " (" + code
            + ") — " + manager.lastStartupFailure().map(StartupFailureReport::recommendation)
            .orElse("see the log"));
    System.exit(code.code());
}
```
`main` stays `throws Exception` (the pre-start `Files.createDirectories`/`resolveHomeId` paths are unchanged and out of scope). **NEVER call `System.exit` from the shutdown hook or from any thread after the hook has started** (the deadlock Nick named). The exit call stays in `main`, after `start()` threw and the lifecycle's own teardown ran inside `start()` — nothing else to tear down.

**B.5 `ExitCodes` (app, package-private final class, private ctor).** `static ExitCode forStartupFailure(Optional<StartupFailureReport> report)`: empty → `UNEXPECTED_ERROR`; else by `subsystem()`: `configuration` → `CONFIGURATION_FAILURE` · `persistence` → `PERSISTENCE_FAILURE` · `event-bus` → `EVENT_BUS_FAILURE` · anything else → `UNEXPECTED_ERROR`. `SUBSYSTEM_INIT_TIMEOUT (13)` has NO producer at HEAD (Phase 6's bounded integration start is non-fatal by design, INV-RF-01) — leave it in the enum, document the absence in its Javadoc (`// no producer at ef02d13; reserved`), do not invent one. The mapping is a pure function: unit-tested; the process exit is not (the seam).

### Part C — the orderly-path emission sweep (one ruling row per instance)
| Instance | Mechanism at source | Ruling | Act in this WU |
|---|---|---|---|
| **§6-B** the unit `failed` after a clean stop | JVM exit 143; no `SuccessExitStatus` | **FIX** (Part A) | A.1–A.4 |
| **EXITCODE-UNWIRED** (instance 5) | `ExitCode` unreferenced; exit 1; `RestartPreventExitStatus=10` unreachable | **FIX** (Part B) | B.1–B.5 |
| **§10-O** `zigbee.transport_failed` on an orderly close | `close()` (:439) counts `stopSignal` down and closes the transport while `productionLoop()` is inside `protocol.pumpInbound(...)`; the read throws `TransportFailureException`; the catch at :814 WARNs `transport_failed` and calls `watchdog.onReadError()` BEFORE the loop condition sees `stopSignal == 0` | **FIX — classify at the catch:** if `stopSignal.getCount() == 0` → `log.info("zigbee.transport_closed_orderly: {}", failure.getMessage())` and `break` (do NOT feed the watchdog); else the existing arm unchanged. The same guard on the `EzspCommandTimeoutException` arm (a timeout racing a close is also orderly). | C.1 + T8 |
| **§10-M** `key_establishment_failed` for `0xFFFFFFFFFFFFFFFF` | a faithful relay of an NCP status (source-read v58 b6: status 0x9B); the all-ones partner is the "no specific partner" sentinel; CAUSE OPEN (the R-3a card §8) | **CLASSIFY AT SOURCE, then ONE of:** (i) if UG100/the EZSP status table you cite confirms the all-ones partner + that status = the transient link key expiring/being cleared as designed → RECLASSIFY: emit `zigbee.transient_key_cleared: status=0x9B partner=none` at INFO and keep the WARN for any non-sentinel partner; (ii) if you cannot confirm it at the spec → KEEP-WITH-REASON: a code comment naming the open cause + the R-3a §8 pointer, no behavior change, and say so in §3 of the return. Never guess the cause. | C.2 (bounded: ≤30 min; the ruling row is the deliverable either way) |
| **§10-I** `Current` renders with no recorded report time | read-path (FE/REST) | **ROUTED** — the FE honesty row §10-J (`Current` never renders without evidence), wk 3 | none (name it in MODULE_CONTEXT? no — it is not this module's) |

**C.1** The `transport_failed` arm (:814–:817) and the timeout arm (:818–:821) each gain the orderly-close guard first. Log token inventory delta: NEW INFO `zigbee.transport_closed_orderly` (message); no token removed. Update the MODULE_CONTEXT token inventory.

### Configuration Parameters — none. Event Types — none produced or consumed (`system.subsystem_failed` per Doc 12 §4.4 is NOT emitted today and is not added here — out of scope; note it as an observation).

### Error Handling
| Condition | Behavior | Exit / channel |
|---|---|---|
| fatal in Phase 1 (config load/validation) | teardown; C12-04 line; re-throw; `Main` exits | **10**; unit does NOT restart (`RestartPreventExitStatus=10`) |
| fatal in Phase 2, persistence | same | **11**; restarts (`always`, 10 s) |
| fatal in Phase 2, event bus | same | **12**; restarts |
| any other fatal-set subsystem (device-model · state-store · automation · rest-api) or pre-bootstrap ISE | same (report present or empty) | **99**; restarts |
| SIGTERM during bootstrap (Doc 12 §6.5) | hook runs `shutdown("SIGTERM")`; `start()` throws or returns; `main` sees `sigtermReceived` and RETURNS | **143** = clean (no `System.exit` call) |
| clean `systemctl stop` while RUNNING | hook → teardown → JVM exit | **143** = clean; `ActiveState=inactive`, `Result=success` |
| SIGKILL / OOM | no hook | **137** = failure; restarts |

## Locked Decisions That Apply
- **LTD-13 (systemd deployment):** `Type=exec`, the hardening block and the readiness probe are untouched; only the four restart/exit lines change. **LTD-01 (no preview/internal APIs):** no `sun.misc.Signal`, no `jdk.unsupported` — the app-side-exit-0 design is REJECTED for this reason too. **LTD-11:** any new state you add is `volatile`/`Atomic*`; no `synchronized`. **LTD-19:** `start()` stays on the platform main thread; the exit happens on that thread.

## Invariants That Must Hold
- **C12-04** (Doc 12 §5): non-zero exit + the structured line with subsystem, phase, exception, recommendation — T4–T7 + T1–T3 together prove it end-to-end except the literal `System.exit`, which the seam leaves untested by design (state this in the return).
- **C12-06:** the shutdown grace is unchanged (no new work on the hook).
- **INV-RF-01** (integration isolation): Phase 6 stays non-fatal; the marker `"integration"` maps to 99 only if a Phase-6 exception ever escapes — it does not today; T7 pins that a failing factory does not produce a report.
- **AMD-97-INV-01's spirit** (never a false verdict): the unit and the adapter stop reporting failure that is not there — A.4 and T8 are the pins.

## P2 Consumer/Pin (Fan-Out) Survey (done at authoring; re-run the greps)
- `ExitCode`: referenced ONLY by itself + `app/.../MODULE_CONTEXT.md` at HEAD (hub-verified) → new consumers: `ExitCodes`, `Main`. No enum values added or removed → no count pins.
- `SystemLifecycleManager`: implementors = `HomeSynapseCore` + `LifecycleWiringTest`'s double (grep `implements SystemLifecycleManager`); no `getDeclaredMethods` shape test in `lifecycle/lifecycle/src/test` (hub-verified: zero files) → a `default` method is additive-safe.
- `start()`'s thrown type: ONE lifecycle test file asserts on it (`grep -rln 'assertThatThrownBy\|assertThrows' lifecycle/lifecycle/src/test | xargs grep -l 'start()'`) — unchanged by design (re-throw stays `throw fatal;`); list the file in the return.
- The unit file: consumed by `run-smoke.sh` (installed path), `health-probe.sh` (no directive reads), `systemd-analyze verify` in CI, `boot-contract-map.md` (prose) — all in the Files table. `distribution/deb/` packaging copies the unit — no directive parsing (verify with `grep -rn 'Restart\|SuccessExit' distribution/deb`).
- Log tokens: `zigbee.transport_failed` is grepped by any bench scenario? Run `grep -rn 'transport_failed' ../nexsys-bench` (read-only) and report; the token is NOT removed, only guarded, so no scenario breaks.
- **ARCH-RULE-REACH (addition #16):** `HomeSynapseArchRules` Rules 1–11 — none reaches `System.exit`/`Runtime`; Rule 2 (`NO_DIRECT_TIME_ACCESS`) whitelists `com.homesynapse.app` and scans lifecycle PRODUCTION code — you add no clock reads. **Zero collisions.**

## Test Requirements (tests first; red at HEAD unless marked)
| # | Class · method | Scenario | Assertion | HEAD |
|---|---|---|---|---|
| T1 | `ExitCodesTest.configurationMapsToTen` | report(FOUNDATION, "configuration", …) | `CONFIGURATION_FAILURE` (10) | compile-red (class absent) |
| T2 | `ExitCodesTest.persistenceAndBusMapToElevenTwelve` | "persistence" → 11 · "event-bus" → 12 | exact codes | red |
| T3 | `ExitCodesTest.unknownAndEmptyMapToNinetyNine` | "automation" · "rest-api" · `Optional.empty()` | `UNEXPECTED_ERROR` (99) | red |
| T4 | `HomeSynapseCoreStartupFailureTest.malformedConfigReportsConfiguration` | a temp config dir with syntactically invalid `config.yaml` (the schema-admission test's construction pattern) → `start()` throws | throw type UNCHANGED from HEAD's behavior; `lastStartupFailure()` = (FOUNDATION, "configuration", the config recommendation); the log line `lifecycle.startup_failed: phase=FOUNDATION subsystem=configuration` present (a list appender or the test-support log capture) | red (`lastStartupFailure` absent) |
| T5 | `…persistenceFailureReportsPersistence` | a failure that surfaces INSIDE the persistence init, AFTER `setPhase(DATA_INFRASTRUCTURE)` — e.g. `dbPath` is an existing DIRECTORY, or a pre-existing file of non-SQLite bytes ("file is not a database" at open/migrate). Verify at HEAD where the throw occurs; a fixture that fails in Phase 0 (`createDirectories` on a bad parent) reads `unknown`/99 and is the WRONG fixture — pick another | (DATA_INFRASTRUCTURE, "persistence", …) | red |
| T6 | `…noReportBeforeStartOrAfterSuccess` | fresh core → empty; a started core (the wiring test's happy path) → empty | `Optional.empty()` both | red |
| T7 | `…integrationFactoryFailureIsNotFatal` | a factory whose `create()` throws → `start()` completes RUNNING | `lastStartupFailure()` empty; phase RUNNING | **green-by-construction (INV-RF-01 preserved) — disclosed** |
| T8 | the adapter scenario test — `orderlyCloseDoesNotReportTransportFailure` | drive the production loop with the fake transport; call `close()` so the next `pumpInbound` throws `TransportFailureException` | no `zigbee.transport_failed` line; `watchdog` NOT signalled (`isHealthy()` stays true / the read-error counter unchanged — pick the observable the fake exposes); `zigbee.transport_closed_orderly` present; the loop exits | red |
| T9 | `unit-directives-test.sh` at HEAD | the lint | FAILS listing `SuccessExitStatus=143` and `Restart=always` missing | red (shell) |
| T10 | `run-smoke.sh` §8 | on a systemd host | `Result=success` + `inactive` | red-by-measurement (O-2) if your desk cannot run it; CI shows green |

**Red-first prediction (addition #18):** T1–T6, T8, T9 red at HEAD for the right reasons; T7 green-by-construction, disclosed; T10 red-by-measurement. Mutation checks to run and report: restore `Restart=on-failure` → T9 fails 1; remove the `sigtermReceived` guard → no test can see it (state this: the guard is reviewed, not tested — the seam's boundary); remove the `stopSignal` guard in C.1 → T8 fails.

**Test-clock reminder (lifecycle is NOT whitelisted):**
> **Tests must inject `Clock`.** Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` in this module's test code. Use `Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC)` injected via constructor/`@BeforeEach`. **Enforcement reach:** `NO_DIRECT_TIME_ACCESS` runs from `com.homesynapse.app`'s test classpath, so it mechanically catches PRODUCTION code in every non-whitelisted module (plus app's own tests) — it does **not** scan this module's test source set. Clock-injection here is a self-enforced project convention that PM review, not `./gradlew check`, enforces.

The app tests (T1–T3) are whitelisted; the zigbee test (T8) uses the adapter's existing `TestClock`/fixed-clock fixture pattern.

## MODULE_CONTEXT.md Update
- `app/homesynapse-app/MODULE_CONTEXT.md`: header type count +1 (`ExitCodes`, package-private); a FAILCHAN gotcha: *"`ExitCode` is WIRED as of FAILCHAN: `Main` maps `SystemLifecycleManager.lastStartupFailure()` → `ExitCodes.forStartupFailure` → `System.exit` — in `main`, after `start()` threw, NEVER from the hook (Runtime.exit during a running shutdown blocks forever); on a SIGTERM mid-bootstrap `main` returns and the JVM's 143 is the clean exit. 13 (`SUBSYSTEM_INIT_TIMEOUT`) has no producer."*
- `lifecycle/lifecycle/MODULE_CONTEXT.md`: +1 public type (`StartupFailureReport`); the `initializing` marker discipline (*"set the marker before every fatal-set init; `recordSubsystem` names are the vocabulary"*); the C12-04 line's token `lifecycle.startup_failed`; `lastStartupFailure()` on the interface (default empty).
- `integration/integration-zigbee/MODULE_CONTEXT.md`: the token inventory +`zigbee.transport_closed_orderly` (INFO); the gotcha *"an orderly `close()` races the pump: the catch must consult `stopSignal` before feeding the watchdog (FAILCHAN §10-O)"*; the §10-M ruling row as recorded.

## What to Watch Out For
- **The hook/exit deadlock (Nick's caveat — the one thing that must not ship wrong):** `Runtime.exit` invoked while shutdown hooks are running blocks the caller forever; `Runtime.halt` skips hooks (data loss). The ONLY `System.exit` you add is in `main`, on the fatal path, guarded by `sigtermReceived`. Write the guard first, then the exit.
- **`initializing` must be set BEFORE the init call, not after** — the marker names what is being attempted; `recordSubsystem` (after success) is the other bookend. Phase 2 records persistence and event-bus together (:529–:530) — the marker is the only thing that distinguishes 11 from 12.
- **Do not wrap the fatal.** Wrapping changes the exception type one existing test pins and would fan out into the schema-admission tests; the report-beside-the-throw shape is deliberate.
- **`Restart=always` + `RestartPreventExitStatus=10`:** `RestartPreventExitStatus` applies to every `Restart=` policy; verify with `systemd-analyze verify` (both copies of the CI step must stay identical — `diff -q` them in the return).
- **`SuccessExitStatus` vs the `-dirty`/ExecStartPost story:** the probe (`ExecStartPost`) exits 3 on a 401/403 — that is a START failure and stays a failure; `SuccessExitStatus=143` speaks only to the main process's exit. Do not add 3.
- **Part C's fake transport:** confirm the fake can throw `TransportFailureException` from `pumpInbound` on demand AFTER `close()`; if the harness cannot express the race, say so in §3 and pin the guard with a narrower unit test on the classification helper (extract `isOrderlyClose()`), disclosed as a scope deviation `[REVIEW]`.
- **Two copies of the CI workflow** (`.github/workflows/install-smoke.yml` and `distribution/ci/install-smoke.yml`): the dialect-sweep obligation (addition #21) — edit both, `diff -q`, report.
- **Register C voice** in every new log/stderr line: no "we", no apology, no exclamation.
- **Spotless** runs on Java only; shell files are `bash -n`/`sh -n`-clean by hand.

## Coder Pushback Welcome
If the fake transport cannot express the orderly-close race, if a cleaner seam than the `initializing` marker exists that keeps the throw type intact, or if `Restart=always` collides with a unit behavior you can show at `systemd-analyze`/`man systemd.service` — raise it with evidence (`[REVIEW]`), implement the closest lawful shape, and proceed. Naked "I disagree" is not pushback; a cited line is.

## Out of Scope
Row 7 (the `<N>` journald prefix — its own small WU, next on this desk after this return is audited) · `system.subsystem_failed` event emission (Doc 12 §4.4 — not built today; an observation only) · the DANGER/notify block · the `sd_notify` transport (Row 5 HOLD) · §10-I (FE row §10-J, wk 3) · any new `ExitCode` value · the `Files.createDirectories`/`resolveHomeId` pre-start failure paths in `Main` (they exit 1 today and stay so; note it) · `README.md` currency (a separate docs-hygiene row) · anything on hardware.

## Success Criterion (binary)
DONE when: (1) the census is exactly the Files table (or the deviation is declared in §0); (2) T1–T6, T8, T9 ran RED at HEAD and GREEN after; T7 declared green-by-construction; T10 measured or declared red-by-measurement; (3) `:app:homesynapse-app:test` · `:lifecycle:lifecycle:test` · `:integration:integration-zigbee:test` GREEN on your desk with the counts stated (app 27 → 27+3; lifecycle 75 → 75+4; zigbee 581 → 582) and `spotlessCheck` clean; (4) both `install-smoke.yml` copies byte-identical; `bash -n` clean on every touched `.sh`; `systemd-analyze --man=no verify` prints no `Unknown key name`; (5) the three MODULE_CONTEXTs updated per spec; (6) the WUCP Phase-1 checklist in the return; (7) the return at `nexsys-hivemind/context/audits/2026-09-04_FAILCHAN_return.md`, §0 first, within cap. **The gate of record is CI on Nick's push (Build & Check + install-smoke both legs); the mechanical proof of §6-B is A.4's green on the runner and, on the card, R-4b's first `systemctl stop` → `inactive`/`success`.**

## Work Unit Completion (WUCP Phase 1)
After your desk gates pass, execute WUCP Phase 1 from `nexsys-hivemind/context/protocols/work-unit-completion-protocol.md`: update the three MODULE_CONTEXT.md files; append the `coder-handoff.md` entry (Deferred Build Gate: YES — the full `./gradlew check` + the install-smoke matrix are CI on Nick's push; NEXT WU pointer: the hub's audit → the msg file → Nick's commit + push → CI → R-4b's first stop reads `inactive`/`success` (the free rider, iff CI is green by Sat 08:00 CT) → Row 7 `<N>`-prefix); a `coder-lessons.md` note only if you learned one; the checklist in the return.

---
### DISPATCH LINE (Nick pastes into a host-side Claude Code session in `~/Desktop/Code/ClaudeFolder/homesynapse-core`)
```
date -u first. Boot as the nexsys-coder skill. Baseline: this tree must be at ef02d13 and clean — verify with `git log -1 --format=%h` and `git status --porcelain` (STOP and report if not). Execute nexsys-hivemind/context/instructions/2026-09-04_coder-lane_FAILCHAN_boot-honesty-sweep_coding-instruction.md exactly: read its §0 contract and the minimum read set first; tests first, red at HEAD; Parts A, B, C; the census is 18 = 13 M + 5 A unless you declare a deviation in §0. Return ONE file at nexsys-hivemind/context/audits/2026-09-04_FAILCHAN_return.md, §0 card first, ≤12 KB target. Stage nothing; commit nothing; the hub audits and Nick commits.
```
