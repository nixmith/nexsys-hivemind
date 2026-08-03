<!--
file: context/audits/2026-08-03_B3_night3_command-confirm-s31_clean-park-FAIL_evidence-read.md
purpose: The night-3 (Aug-3 04:30 fire) command-confirm-s31 FAIL under the CLEAN PARK — the escalation evidence read of record. The pre-stated night-3 prediction is REFUTED; the thread escalates under the two-fails law. Per-hypothesis predictions for the discriminating reads are FILED HERE BEFORE those reads run (arc-discipline 28). Bundle: command-confirm-s31-20260803T083057Z.
audience: Hub (v45), Nick, the fix-ruling beat
state-type: evidence read (point-in-time)
status: FILED 2026-08-03 (v45 hub, beat 2) — predictions pre-stated; the Pi reads (BLOCK R) had NOT run at filing
provenance: Nick's 17:50 CDT gate paste (pgrep · digest ×3 · systemctl show · journalctl tail-40) is the primary record; pinned extracts below. The scenario/unit grounding was read at host (bench 41a7a3c git objects) BEFORE predictions were stated.
-->

# B3 Night-3 Evidence Read — command-confirm-s31 FAIL UNDER THE CLEAN PARK (2026-08-03)

## 1. The gate intake, pinned

- **Digest (three nights):** Aug-1 `8/9 PASS · 1 SKIP(hue-online) · RESTORED ✓ · ON-latency 3.65s` · Aug-2 `7/9 · FAIL command-confirm-s31 · … · ON-latency n/a(FAIL)` · **Aug-3 `7/9 · FAIL command-confirm-s31 · bundle /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260803T083057Z · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)`.**
- **The survival gate PASSED:** pgrep shows PID 73230 `com.homesynapse.app.Main` alive — the wrapper's own restored boot (`[OK] launched pid 73230`, 04:31:43) — and systemd's own line confirms the mechanism again: `Unit process 73230 (java) remains running after unit stopped`. `KillMode=process` · `Type=oneshot` held. `Result=exit-code` / `ExecMainStatus=1` = **EXPECTED-HONEST** (the wrapper's documented exit contract: exit 1 = suite FAIL).
- **The suite tail was healthy:** command-identify-honest PASS · usb-reenumeration 2/2 PASS (`uhubctl -l 3-2.4 -p 2 -a cycle -d 10`) · timeout-honesty-no-change 2/2 PASS · **command-s31-settle PASS (bundle `command-s31-settle-20260803T083136Z`) — the relay was RE-PARKED at suite end, 04:31:36.** Restore ASSERTED (bench-hero PRESENT); restored boot clean (relink ×6 · projection 6/6 @25065 · network_resumed ch20 · RADIO UP 12 s).
- **Hands-off is now corroborated at the instrument, not just testimony:** the ssh login banner at the gate read — `Last login: Sun Aug 2 07:44:48 2026` — proves no interactive session between the Aug-2 morning reads and this 17:50 gate. Physical acts remain outside shell history; Nick attests none.

## 2. The pre-stated prediction is REFUTED — the escalation branch fires

The night-2 evidence read pre-stated: *"the Aug-3 04:30 fire reads s31 PASS; digest 8/9 PASS · 1 SKIP(hue-online) with an ON-latency line."* **It read 7/9 · FAIL.** The park-history mechanism (the attended Saturday broke the park) is therefore **insufficient as the sole mechanism** — night-3's park was set by the Aug-2 suite's own settle leg and stood undisturbed (§1 hands-off). Per the pre-stated branch and arc-discipline 28: **the thread is ESCALATED — instrument-first; the reads below run BEFORE any third ruling; no retune of any scenario, window, or suite order.**

## 3. Grounding read at source (host git objects @ bench `41a7a3c`, BEFORE predictions)

- **The settle leg asserts SOME terminal, disposition-agnostic** (`command-s31-settle.yaml`: `field_equals data.terminal == true`, within 25 s). Its header's dichotomy — CONFIRMED (real off-edge) or TIMED_OUT (already-OFF no-change), *"EITHER terminal leaves the relay OFF"* — carries an **unpriced third case: TIMED_OUT because the turn_off never physically executed (relay stays ON).** Under best_effort posture with unverified reporting, a settle PASS does NOT prove the relay is OFF. **Which terminal each settle actually hit is therefore decisive evidence** (reads R-4a/R-4b).
- **The confirm leg has TWO positives** (`command-confirm-s31.yaml`): the lifecycle read (`phase_terminal` CONFIRMED-class, within 20 s, fail-fast on mismatch — the observed FAIL path) AND **a state read (`data.attributes.on.value == true`, within 20 s). If the engine captured that second read, the bundle already holds a ~5–20 s post-command relay-state observation — an in-bundle edge-vs-no-edge discriminator** (read R-1 checks for it).
- **The build boundary sits exactly between the last unattended PASS and both FAILs:** night-1 (Aug-1 04:30) ran the PRE-deploy core; the convergent deploy (`60d3ab5` + FE) landed 10:06 EDT Aug-1; nights 2 and 3 ran on `60d3ab5`. WU-AVAIL-SEED touched the zigbee adapter (boot seed · first-boot mains pings · the ping arm made real via `PingOutcome` · evidence marks). **No clean unattended S31 CONFIRMED exists on `60d3ab5` in the record** (the Aug-1 17:40 rejoin-race TIMED_OUTs were deliberately raced and honest). Correlation, not yet causation — named so the reads can kill or confirm it.
- The unit file (in-repo, A-8): `ExecStart=/usr/bin/bash %h/nexsys-bench/tools/nightly.sh` — bash-prefixed by design, so pull-time exec-bit loss cannot break the fire; repo modes 100755 on both scripts.

## 4. Hypotheses, with per-hypothesis predictions — STATED BEFORE THE READS

- **H-1 LATE REPORT (margin/latency excursion; the F-12 margin class — 3.65 s was already 68% of the 5.37 s window).** The turn_on executed; the relay clicked ON at ~04:30:52; the confirming report arrived after the window.
  PREDICTS: (a) the quiesced-boot log shows an S31 on-report ~04:30:57–04:31:50; (b) the in-bundle state read (if captured) reads `on.value=true`; (c) the Aug-3 settle then hit a REAL off-edge ⇒ likely CONFIRMED; (d) R-5 now reads `on=false` with lastChanged ≈ 08:31:4x Z (the settle's off-edge).
- **H-2a STANDING SETTLE-IMPOTENCE (commands not executing; relay ON continuously since the Saturday).**
  PREDICTS: (a) **R-5 NOW reads `on=true`** — the single sharpest observation; (b) both settles read TIMED_OUT; (c) no on-report anywhere in the quiesced-boot log (no edges at all); (d) day-log shows no off/on transitions. R-5 `on=false` effectively kills this branch.
- **H-2b BOOT-WINDOW COMMAND LOSS (relay was OFF — the park held; the turn_on was dispatched but never acted).**
  PREDICTS: (a) NO S31 on-report in the quiesced-boot log at any offset; (b) the in-bundle state read (if captured) reads `on.value=false`; (c) the Aug-3 settle = no-change TIMED_OUT; (d) R-5 now `on=false`; (e) the Aug-2 settle read matters: CONFIRMED there (a real off-edge after night-2's ON-relay) would prove commands DO execute at 04:31 — narrowing loss to the turn_on minute specifically.
- **H-3 BUILD-CORRELATED REPORT-PATH CHANGE (the AVAIL-SEED ping arm / boot ping wave).** Two testable forms: **H-3a boot-contention** — the first-boot mains-ping wave + route discovery around 04:30:4x–5x adds seconds to the S31's report path ⇒ the report lands late (a cause of H-1). **H-3b report-clock interaction** — the ping arm now exercises the S31 all day (~10-min mains cadence), and if ping replies reset or substitute for the device's native report clock, the park's "~22 h idle clock" premise no longer exists on the new build.
  PREDICTS: (a) the day-log shows a periodic S31 ping/reply cadence (absent on the old build); (b) the quiesced-boot log shows a ping/reply to the S31 in the seconds before the turn_on; (c) the on-report (if any) lands at a min-interval-shaped offset; (d) night-1-PASS-pre-deploy stands as the only unattended PASS. H-3 predicts **night-4 FAILS again** (structural, not transient).
- **H-4 (minor) USB-CYCLE AFTERMATH** — the nightly `uhubctl` 10 s dongle outage (runs AFTER the s31 leg each night) leaves standing network state that degrades the NEXT night's first commands. Weak (the restored boot re-resumes cleanly and runs all day); listed for completeness.

## 5. The discriminator map (BLOCK R, read-only; issued in-chat this beat)

R-5 the CURRENT S31 state read (`bench.sh state`) → kills or confirms H-2a instantly · R-1 the FAIL bundle full body (esp. whether the second-positive state read was captured, and at what value) → edge-vs-no-edge (H-1/H-3 vs H-2b) · R-4a/R-4b the two settle bundles' terminal dispositions → the park's physical truth both nights + command-execution proof at 04:31 · R-2 the quiesced-boot log S31 slice → late-report timing + the pre-command ping (H-3a/b) · R-3 the day-log S31 slice → the ping cadence + any transitions across the quiet day (H-2a/H-3b). **Level-1 verdict (edge vs no edge) should close on today's pastes; level-2 (why) may need night-4's A-9 read.**

## 6. Night-4 (Aug-4 04:30), pre-stated — with the refreshed instrument (BLOCK P arms A-9 + tiered app-log capture tonight; zero scenario changes — the s31 YAMLs are byte-identical at `41a7a3c`)

- Under H-3 (structural): **FAIL again**, and the bundle now carries `post-window-state.json` — `on.value=true` pins LATE-REPORT/edge-occurred; `on.value=false` pins NO-EDGE — plus the tiered app-log slice with the report lines. Decisive either way.
- Under H-1-as-transient: **PASS** (8/9 · 1 SKIP · ON-latency present), and the thread closes as a margin excursion with the margin finding re-opened for the C4 estimator.
- Under H-2a: the R-5 read today already ruled; the night-4 form follows whichever branch survived.

## 7. Standing orders and the ruling boundary

- **HANDS OFF the S31** — today, tonight, until the level-1 ruling. The park (re-set 04:31:36) is part of the instrument.
- **BLOCK P is instrument hardening, not a retune:** the pull to `41a7a3c` changes NO scenario the experiment runs (s31 YAMLs byte-untouched; digest grammar selftest-pinned byte-exact). The never-retune law stands.
- **Any FIX — scenario precondition, suite order, window, or core change — is a SEPARATE ruling** taken only after the mechanism is pinned, with Nick's word where it touches the freeze runway or core code. Nothing in this read authorizes one.
- The Hue remains physically dark (hue-online SKIP ×3 is honest); re-powering it is an H3-visit line item for the 9/9 ceiling — Nick's call, noted once.
