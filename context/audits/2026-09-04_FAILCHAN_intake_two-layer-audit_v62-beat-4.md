<!--
file: context/audits/2026-09-04_FAILCHAN_intake_two-layer-audit_v62-beat-4.md
purpose: THE HUB'S TWO-LAYER INTAKE AUDIT of the FAILCHAN Coder return (context/audits/2026-09-04_FAILCHAN_return.md, 12,532 B, delivered 2026-09-04 03:20Z). Layer 1: the return's claims read critically. Layer 2: the hub's own re-execution at the bytes on the uncommitted core tree (porcelain 19 atop ef02d13). Rulings on R1/R2; dispositions of O1–O6/I1–I6; what the hub could not re-execute, disclosed.
audience: the hub · Nick (the commit block rides the brief §A)
state-type: intake audit
status: FILED at v62 beat 4 (Fri 2026-09-04, instrument 12:2xZ = 07:2x CT). VERDICT: ACCEPT-WITH-RULINGS — R1 ACCEPT · R2 ACCEPT (+1 M; the hub's Files-table miss, owned). Census for Nick's hands: 19 = 14 M + 5 A. CI on his push = the gate of record.
-->

# FAILCHAN — intake audit (v62 beat 4)

## §0 Verdict
**ACCEPT-WITH-RULINGS.** Parts A/B/C delivered as chartered; ten tests with the red-first carve-outs as predicted; the two [REVIEW] items ruled ACCEPT; two of the instruction's own claims corrected by the lane at source (owned below). **Census 19 = 14 M + 5 A** (porcelain re-read by the hub: 14 ` M` + 5 `??`). Msg file: `../_scratch/2026-09-04_core_FAILCHAN_commit-msg.txt`. The deferred `./gradlew check` + the install-smoke matrix are CI on Nick's push — **guard 1 (the R-4b free rider) is decided at the Actions page, not here.**

## §1 Layer 2 — re-executed by the hub at the bytes
| Claim | Instrument | Result |
|---|---|---|
| The ONE new `System.exit` lives in `main`, behind the SIGTERM guard; the hook never exits | `grep -n` `Main.java`: `:83` (the pre-existing token-CLI exit) · `:136` flag · `:139` set FIRST in the hook · `:174` `manager.start()` wrapped · `:176` guard · `:182` `ExitCodes.forStartupFailure(manager.lastStartupFailure())` · `:186` the exit | ✓ CONFIRMED — Nick's caveat honored exactly |
| Nine `initializing` markers before the fatal-set inits; the throw type unchanged; the C12-04 line | `HomeSynapseCore.java` `:260/:262` fields · `:451` reset · `:465` report · `:467` `lifecycle.startup_failed: phase= subsystem= recommendation=` · `:475` `throw fatal;` · markers `:497/:545/:549/:578/:602/:665/:781/:795/:807` · `:893` accessor | ✓ CONFIRMED (persistence `:545` and event-bus `:549` are separate markers — 11 and 12 distinguishable) |
| The unit: the seven directives; the DANGER block untouched | `grep` `:21/:24/:58/:60/:70/:71/:72`; `git diff -U0` hunks at `:14`, `:59–60`, `:64–70` only | ✓ CONFIRMED |
| The CI twins identical; the lint wired after `systemd-analyze` | `diff -q` → IDENTICAL; the +5 lines in both | ✓ CONFIRMED |
| §10-O: the guard consults `stopSignal` BEFORE the watchdog at both arms | adapter `:822` (transport arm) · `:835` (timeout arm) · `:828/:838` the INFO token · `:857` `closeRequested()` | ✓ CONFIRMED |
| R1: the root document is `homesynapse.yaml` | `YamlLoader.java:86` `static final String ROOT_DOCUMENT_NAME = "homesynapse.yaml";` | ✓ CONFIRMED — the instruction (and Doc 12 §9) said `config.yaml` |
| R2: `ZclIngestionUnit.java` is comment-only | `git diff -U0`: 13 `+` lines, all `//`, zero `-` | ✓ CONFIRMED |
| I5: no test double implements the interface | `grep 'implements SystemLifecycleManager'`: `HomeSynapseCore.java:183` + `LifecycleWiringTest.java:132` — a `@DisplayName("HomeSynapseCore implements System…")` STRING | ✓ the lane is right; the hub's P2 claim was a display-name grep match |
| The five A files exist | `ls`: `ExitCodes.java` 2,655 · `ExitCodesTest.java` 3,752 · `unit-directives-test.sh` 3,372 · `StartupFailureReport.java` 2,194 · `HomeSynapseCoreStartupFailureTest.java` 13,377 | ✓ |
| Census 19 = 14 M + 5 A | `git status --porcelain | wc -l` = 19; Nick's paste 14 modified + 5 untracked | ✓ |
| Test counts app 27→30 · lifecycle 75→79 · zigbee 581→582; `-Werror` clean; the WSL `systemd-analyze`; the stub-`systemctl` fragment runs | — | **NOT re-executed** (no Gradle on the bridge; the lane's word; CI on the push is the gate) |

## §2 Rulings
- **R1 — ACCEPT.** The operator-facing recommendation names the real root document. **Consequence for the docs repo:** Doc 12 §9's `config.yaml` is docs-side drift → one row in the docs correction block (Nick's hands).
- **R2 — ACCEPT the 19th file.** The instruction's Part C row (ii) itself prescribed "a code comment naming the open cause + the R-3a §8 pointer"; the Files table failed to list a file for that arm — **the hub's authoring miss, owned.** The comment is the ruling row's own consequence, not scope creep. Census 19.
- **O3 (§10-M) — the ruling (ii) STANDS, on the lane's evidence:** the all-ones partner is the EmberZNet null EUI64; the status is `0x32 TC_REQUESTER_VERIFY_KEY_TIMEOUT` (the instruction's "0x9B" was the frame id — **the hub's error, owned**); no spec text at source confirms the designed expiry → WARN kept, cause OPEN. The OR-FAILCHAN §10-M line is corrected to `0x32`.
- **O1 (the residual window at stop) — RECORDED as OR-FAILCHAN instance 6 (LOW):** a `close()` landing between the `while` check and the next `pumpInbound` reaches `requireOpen()`/`requireConnected()` → an `IllegalStateException` no loop catch holds → `run()` throws at stop. Not evidenced on a card yet; rides Row 7's WU as a rider (classify the stop-time ISE at `run()`'s boundary); the lane recorded it in MODULE_CONTEXT.
- **O4 (docs drift the fix exposes) — into the docs correction block:** Doc 12 §8.4 `:663` (`System.exit(1)`) · Doc 12 §6.4/§6.6 + LTD-13 `:37/:58/:62` (`Restart=on-failure`) · Doc 12 §9 `config.yaml` (R1). Plus ONE core follow-on outside this census: `ExitCode.java`'s Javadoc "a clean shutdown returns 0" → "the JVM exits 143 after a caught SIGTERM (clean by the unit's `SuccessExitStatus`)" — rides Row 7's WU (same desk).
- **I1–I6 — ACCEPT as filed.** I1 (the `configuration` marker at the top of the Phase-1 block) is correct: the whole block is the configuration init, so a malformed bundled fragment also reads 10, deterministic, never looped. I2 (drive seam package-private) is the F-R4-1 precedent. I6 (the lint's verdict prefix) is cosmetic; CI's predicted line is `[unit-directives-test] PASSED ✓ (7 directives)`.

## §3 Layer 1 — the return read critically
Shape: §0 card first (5.3 KB — over the 3 KB target because the census carries 19 exact paths; accepted, the paths are the point) · the red-first table with the three carve-outs disclosed (T3/T6/T7 green-by-construction; T10 red-by-measurement with the fragment proven under a four-arm stub) · mutations (three lint mutants; the `stopSignal` guard = stage A; the `sigtermReceived` guard reviewed-not-tested, as the instruction's seam boundary said) · §2 the allow-list gate green in one round with XML mtimes · §3 six observations, each with a line cite · §4 the WUCP checklist complete. The lane's pushback was evidence-based at every point (I5, O3) — the instruction was wrong at both and the fix was right at both. Return size 12.5 KB vs the 12 KB target: inside the ceiling.

## §4 What lands where
- **Nick's hands (now):** the core commit of exactly the 19 from the msg file → push → CI (Build & Check + install-smoke both legs). Predicted CI lines: `[unit-directives-test] PASSED ✓ (7 directives)` · `unit directives verified` · 24 `[smoke] PASS` per leg including `clean stop grades success (Result=success ExecMainStatus=143)`.
- **The hivemind (this beat):** this audit (A) · the return (A, the lane's) · `coder-handoff.md` + `coder-lessons.md` (M, the lane's) · OR-FAILCHAN status (instances 5 fixed-pending-CI · 6 recorded; the 0x32 correction) · the brief §A → the commit block.
- **The card (R-4b today):** the first `systemctl stop` on the held card reads `inactive`/`success` = the mechanical confirmation of §6-B on hardware (iff the FAILCHAN artifact is the one installed — guard 1).
- **Next on the same desk:** Row 7 (`<N>` journald prefix) + the two riders (the stop-time ISE classification; the `ExitCode` Javadoc line).
