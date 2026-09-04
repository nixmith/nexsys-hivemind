<!--
file: context/audits/2026-09-04_FAILCHAN_return.md
purpose: THE FAILCHAN CODER RETURN — R-10 Row 6 (a) + EXITCODE (a): 143-is-clean + Restart=always (A), the ExitCode contract wired behind the exit seam (B), the orderly-path emission sweep (C). One lane on homesynapse-core at ef02d13. §0 card first.
audience: the hub (audit) · Nick (commit)
state-type: lane return
status: DELIVERED 2026-09-03 ~22:20 CT (2026-09-04 03:20Z); hub audit pending; nothing staged, nothing committed.
-->

# FAILCHAN — Coder return (boot-honesty sweep)

## §0 The card

**Clock:** `date -u` 2026-09-04 02:39:00Z → CT (UTC−5) 2026-09-03 21:39 (the operator day; filed under the instruction's 09-04 name). Instrument: the desk host clock, no Pi. **Baseline** `ef02d13`, porcelain empty. **ZERO commits/staged.**

**Census 19 = 14 M + 5 A** (the instruction's 18 **+1 M**, R2). M `.github/workflows/install-smoke.yml` · `app/homesynapse-app/MODULE_CONTEXT.md` · `app/homesynapse-app/src/main/java/com/homesynapse/app/Main.java` · `distribution/ci/install-smoke.yml` · `distribution/docs/boot-contract-map.md` · `distribution/smoke/run-smoke.sh` · `distribution/systemd/homesynapse.service` · `integration/integration-zigbee/MODULE_CONTEXT.md` · `integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/ZclIngestionUnit.java` (+1) · `…/zigbee/ZigbeeIntegrationAdapter.java` · `integration/integration-zigbee/src/test/java/com/homesynapse/integration/zigbee/ZigbeeProductionTransportTest.java` (the adapter scenario class) · `lifecycle/lifecycle/MODULE_CONTEXT.md` · `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java` · `…/lifecycle/SystemLifecycleManager.java`. A `app/homesynapse-app/src/main/java/com/homesynapse/app/ExitCodes.java` · `app/homesynapse-app/src/test/java/com/homesynapse/app/ExitCodesTest.java` · `distribution/smoke/unit-directives-test.sh` · `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/StartupFailureReport.java` · `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/HomeSynapseCoreStartupFailureTest.java`. Both `module-info.java` byte-unchanged; no Gradle/catalog/event/schema diffs.

**Verdict: A DONE · B DONE · C DONE** (§10-O FIXED at both catches · §10-M KEEP-WITH-REASON (ii) · §10-I ROUTED, untouched).

| # | HEAD ef02d13 | Stage A (seams inert) | Stage B |
|---|---|---|---|
| T1 | compile-red (`ExitCodes`/`StartupFailureReport` absent) | RED `expected CONFIGURATION_FAILURE but was UNEXPECTED_ERROR` | GREEN |
| T2 | compile-red | RED `expected PERSISTENCE_FAILURE …` | GREEN |
| T3 | compile-red | green-by-construction (inert map = 99), disclosed | GREEN |
| T4 | compile-red (`lastStartupFailure` absent) | RED `Optional to contain …FOUNDATION, configuration…` | GREEN; throw type pinned `ConfigurationLoadException` (HEAD-true) |
| T5 | compile-red | RED `…DATA_INFRASTRUCTURE, persistence…` | GREEN |
| T6 | compile-red | green-by-construction, disclosed | GREEN |
| T7 | compile-red | green-by-construction (INV-RF-01), disclosed | GREEN |
| T8 | compile-red (`productionLoop()` private — the drive seam IS stage A) | RED `Expected size: 1 but was: 0` (no orderly INFO) | GREEN |
| T9 | RED `FAILED ✗ (2 of 7)`: `SuccessExitStatus=143`, `Restart=always` missing | — | `PASSED ✓ (7 directives)` |
| T10 | red-by-measurement (O-2 `exit-code/failed/143`); fragment under a stub `systemctl` 4 arms correct | — | CI shows the green |

Mutations: `Restart=on-failure` restored → T9 FAILS 1 · a duplicate `SuccessExitStatus=143` → FAILS 1 (present 2×) · commented out → FAILS 1 · HEAD's unit → FAILS 2 · the `stopSignal` guard absent = the stage-A run → T8 FAILS · the `sigtermReceived` guard: reviewed, not tested (the seam's boundary).

**Deviations.** **[REVIEW] R1** the configuration recommendation says `homesynapse.yaml`, not the instruction's `config.yaml` — the root document IS `homesynapse.yaml` (`YamlLoader.ROOT_DOCUMENT_NAME` :86; Doc 12 §9's name is docs-side); operator-facing text corrected at source; revert = one literal in `recommendationFor` + the T4 pin. **[REVIEW] R2** +1 M `ZclIngestionUnit.java`: the §10-M (ii) code comment the ruling row prescribes ("a code comment naming the open cause + the R-3a §8 pointer"), which the Files table omitted for either arm; comment-only; drop it and the census is exactly 18 (the ruling survives in MODULE_CONTEXT + §3). **[INFO] I1** the `"configuration"` marker sits at the top of the Phase-1 block (beside the `configStart` bookend), not right before `load()` — the whole block is the configuration init, so a malformed bundled fragment (schema-admission T9b) also reads `configuration` → 10, deterministic, never looped. **I2** `productionLoop()` private → package-private (drive seam) for T8. **I3** a private `closeRequested()` shared by both arms. **I4** the 13-no-producer note lives in `ExitCodes`' Javadoc + the app MODULE_CONTEXT, not `ExitCode.java` (outside the table). **I5** the instruction's "`LifecycleWiringTest` test double" does not exist — nothing but `HomeSynapseCore` implements the interface (grep); the `default` ships anyway (java-patterns §12). **I6** the lint's verdict carries the sibling's prefix: `[unit-directives-test] PASSED ✓ (7 directives)`.

## §1 What changed, per file

- **unit** — +1 header line naming FAILCHAN; `SuccessExitStatus=143` + its comment under `KillSignal=SIGTERM`; `:61–:66` → the ruled block verbatim (`Restart=always` · `RestartSec=10` · `RestartPreventExitStatus=10`); DANGER block byte-unchanged (diff-proven).
- **`unit-directives-test.sh`** (A) — seven active directives each exactly once (`grep -c -x -F`: a commented DANGER shape never counts; a duplicate is a miss); path arg for mutants; `bash -n`/`sh -n`/`dash -n` clean.
- **both `install-smoke.yml`** — `bash distribution/smoke/unit-directives-test.sh` after the `if grep … fi` block, before `echo "unit directives verified"`; IDENTICAL (sha256 `5e7544419154418b8…` ×2).
- **`run-smoke.sh` §8** — `Result`/`ActiveState`/`ExecMainStatus` via `systemctl show --value`; `ok "clean stop grades success (Result=… ExecMainStatus=…)"` iff `success` ∧ `inactive`, else `bad "clean stop graded R/S (ExecMainStatus=E) — the §6-B lie"` + `dump_logs`; ok-sites 23 → 24; the no-systemd arm untouched.
- **`boot-contract-map.md`** — the two sections state the wired contract, the three lines, the lint, 143-is-clean with the measured before/after, the hook-never-exits rule (and corrects "default KillSignal").
- **`StartupFailureReport`** (A, public record) — `(LifecyclePhase, String subsystem, String recommendation)`, `requireNonNull` ×3.
- **`SystemLifecycleManager`** — `default Optional<StartupFailureReport> lastStartupFailure()` → empty.
- **`HomeSynapseCore`** — `volatile String initializing = "unknown"` set before each fatal-set init (configuration · persistence · event-bus · device-model · state-store · automation · observability · rest-api · integration); `start()` resets the report; its catch builds the report BEFORE teardown and emits `lifecycle.startup_failed: phase={} subsystem={} recommendation="{}" — tearing down initialized subsystems` (throwable last); `throw fatal;` byte-unchanged; `@Override lastStartupFailure()`; `recommendationFor`.
- **`ExitCodes`** (A) — empty → 99; `configuration` 10 · `persistence` 11 · `event-bus` 12 · else 99; NPE on a null Optional.
- **`Main`** — `AtomicBoolean sigtermReceived` set FIRST in the hook's `try`; ONLY `manager.start()` wrapped: SIGTERM seen ⇒ `return` (the hook owns the 143); else map → one stderr line → `System.exit(code)`.
- **`ZigbeeIntegrationAdapter`** — both catches: `closeRequested()` ⇒ INFO `zigbee.transport_closed_orderly: {}` + `break`, else the arm unchanged; `productionLoop()` package-private.
- **`ZclIngestionUnit`** — the §10-M comment at the WARN arm (R2).
- **`ZigbeeProductionTransportTest`** — T8 + test-local `CloseInsideReadChannel` (a delegating `SerialByteChannel` whose armed next read runs `adapter::close` then returns −1: the cross-thread race in order on one thread); a second `ListAppender` on the `PortWatchdog` logger.
- **tests** (A) — `ExitCodesTest` T1–T3; `HomeSynapseCoreStartupFailureTest` T4–T7 (fixed clock, logback capture, a `ThrowingFactory`).
- **MODULE_CONTEXT ×3** — app (+`ExitCodes`, total 6 files, the FAILCHAN paragraph, the prescribed gotcha); lifecycle (H1 9 public, the FAILCHAN blockquote, the record row, the interface 6 methods, gotcha #11 the marker discipline, the token); zigbee (the FAILCHAN section: deltas, gotchas incl. the residual window, the §10-M row, tokens).

## §2 Gates + counts

- Allow-list: `./gradlew :app:homesynapse-app:compileJava :app:homesynapse-app:test :lifecycle:lifecycle:compileJava :lifecycle:lifecycle:test :integration:integration-zigbee:compileJava :integration:integration-zigbee:test spotlessCheck --offline` → **BUILD SUCCESSFUL in 23s**, zero `warning:` (`-Werror` clean), the three `test` tasks EXECUTED; XML mtimes 03:06:44Z / 03:06:59Z / 03:07:01Z. **app 27 → 30 · lifecycle 75 → 79 · zigbee 581 → 582**; 0 failures/errors/skips.
- Staged: HEAD compileTestJava ×3 RED (the symbols above) → stage A `3/2 failed` · `4/2 failed` · `10/1 failed` → stage B green.
- Shell: T9 7/7 + three mutants + HEAD 2/7; `bash -n` over all 10 `distribution/**/*.sh`; `sh -n` (msys), `dash -n` + a dash run (WSL); `systemd-analyze --man=no verify` (WSL systemd 255, /tmp copy — the 9p caveat): 0 `Unknown key name`, no parse lines, the 2 expected "not executable"; twins IDENTICAL; PyYAML: 14 steps, verify < lint < echo, both; the check-8 fragment (extracted bytes) under a stub: `exit-code/failed/143` FAIL+dump · `success/inactive/143` PASS · `success/activating` FAIL · `failed/inactive/137` FAIL.
- Hygiene: CR=0 + trailing LF ×19; no `synchronized`, no wall clock, no new dependency; porcelain = 14 M + 5 `??`.
- **DEFERRED BUILD GATE: YES** — `./gradlew check` NOT run; owed against Nick's commit of exactly the 19 atop `ef02d13`; **CI on the push (Build & Check + install-smoke BOTH legs) = the gate of record.** Predictions: Static lint `PASSED ✓ (7 directives)` + `unit directives verified`; run-smoke **24** `[smoke] PASS` per leg incl. `clean stop grades success (Result=success ExecMainStatus=143)`.

## §3 Pushback / observations

1. **O1 residual window (recorded, not changed):** a `close()` between the `while` check and the next `pumpInbound` hits `requireOpen()`/`requireConnected()` → an `IllegalStateException` no loop catch holds → `run()` throws at stop time; outside the two evidenced catches the instruction classified. In MODULE_CONTEXT.
2. **O2** the timeout arm is covered by the shared predicate, not a scenario (a command timeout inside the cycle needs a due interview/ping).
3. **O3 §10-M = (ii):** R-3a §8 `14:11:26 device=0xFFFFFFFFFFFFFFFF status=TC_REQUESTER_VERIFY_KEY_TIMEOUT` + its own "(probably) … as designed"; the acceptance record 07:39:03; all-ones = EmberZNet null EUI64; 0x32 = the TC Verify-Key timeout. No spec text at source confirms the designed expiry ⇒ WARN kept, cause OPEN. (The instruction's "status 0x9B" is the frame id.)
4. **O4 docs drift for the hub's correction block:** Doc 12 §8.4 :663 (`System.exit(1)`), §6.4/§6.6 + LTD-13 :37/:58/:62 (`Restart=on-failure`), and `ExitCode.java`'s "a clean shutdown returns 0" Javadoc (outside the census).
5. **O5** `system.subsystem_failed` still not emitted (observation, as instructed); the pre-start `Main` paths still exit 1.
6. **O6** fan-out re-run: `ExitCode` consumers = `ExitCodes` + `Main`; ONE lifecycle test pins `start()`'s throw type (`HomeSynapseCoreSchemaAdmissionTest` T9b, IAE) — unchanged, green; `nexsys-bench` greps `transport_failed` in soak logs/fixtures/docs only (token kept); `distribution/deb` parses no directive; cited lines off by ≤2 (report-and-proceed).

## §4 WUCP Phase 1: Coder Closeout

- [x] MODULE_CONTEXT.md updated for: app (homesynapse-app), lifecycle, integration-zigbee
- [x] coder-handoff.md updated (the FAILCHAN DELIVERED entry prepended; Deferred Build Gate flagged; NEXT WU pointer)
- [x] Deferred build gate flag: YES
- [x] coder-lessons.md appended: the inject-the-race-into-the-blocking-seam pattern (T8)
- [x] Cross-agent note posted: Not needed (channel retired; this return + the handoff carry it)
- Timestamp: 2026-09-04 03:20 UTC
