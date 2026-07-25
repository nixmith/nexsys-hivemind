<!--
file: context/handoff/2026-07-25_rosonway-topology-move_I3b_bench-session-report.md
purpose: Full session report for the Rosonway dongle-behind-hub topology move + the I3b [S] hub-attached reenumeration leg, run 2026-07-25 against the operator package `context/handoff/2026-07-22_rosonway-topology-move_I3b_operator-package.md` (Nick's ruling 3). Layer-1 operator + desk evidence assembled for INDEPENDENT (layer-2) hub adjudication: the result, the measurements, ONE REPRODUCIBLE READ-SURFACE DEFECT with a live false-FAIL path into the B1 instrument, four operator-package corrections applied in-session, and a re-derivation checklist.
audience: the PM mission-control hub (paste adjudication); Nick (operator).
state-type: session report / audit INPUT. An in-session read is layer-1 evidence, NOT a gate. Everything below is refutation-welcome in both directions.
status: COMPLETE run · GREEN at the instrument · single-variable discipline held end-to-end · ONE NEW CANDIDATE DEFECT (RUNS-TRIGGEREDAT) reproduced on TWO runs of DIFFERING duration, each exact to the microsecond, with independent external corroboration. §7 R7 CLOSED in-session — no captures owed.
observed-at: Pi hs-dev-1, deploy `355a711` UNCHANGED (no pull, no build, no deploy tonight — the deploy evening stays separate per v37 charge 2). Pi local clock = UTC−4; operator local = UTC−5. All times below are UTC unless marked "Pi-local".
pointer-not-copy: no project-wide state lives here. HEADs, watermark, counts, milestone status → the spine.
banked-by: the v37 hub, beat 2 (2026-07-25) — Nick's paste intaken verbatim; the hub's two-layer adjudication is recorded at pm-handoff v37 beat 2 (ACCEPT; RUNS-TRIGGEREDAT confirmed at source; I3b [S] CLOSED).
-->

# Rosonway Topology Move + I3b [S] — Bench Session Report (2026-07-25)

## §0 — How to read this, and the one-line verdict

**Verdict.** The coordinator now runs **behind the powered Rosonway RSH-A107C**, three USB hops from the Pi root, and the platform cannot tell the difference: boot-health `[PASS] 6/6 · 0 forbidden` **before** the move and **after** it, three boots at an identical 12 s RADIO-UP, and **I3b [S] CLOSED** on `[PASS] usb-reenumeration-manual — 3/3 positive · 0 forbidden`. The topology is **STANDING**.

**The night's real yield is not the [S] row.** It is a reproducible defect on the frozen v1.1 read surface — `/api/v1/runs[].triggeredAt` is understated by exactly the run's own duration — which opens a **~34-second dead zone immediately after every reopen** in which a genuine post-reopen run is silently discarded by the `new_run_after` assert. It was found by a pre-flight baseline, reproduced twice, and corroborated against an external device timestamp. **Without the mitigation improvised in-session, this rep would have FAILED and the failure would have been attributed to the Rosonway.** See §4.

**This report is layer-1 evidence, not a gate.** Treat every CLAIM as a hub-refutable hypothesis and every QUOTE (log line, API payload, `File.java:Lxxx`) as the primary evidence to adjudicate it against. §7 is a re-derivation checklist so nothing here needs to be taken on faith.

---

## §1 — The result, against the package's own DONE-WHEN

The package's done-when: *"Block-3 `[PASS]` + Block-4 `[PASS] 3/3` pastes are in the hub's hands."*

| Criterion | Verdict | Evidence (primary) |
|---|---|---|
| Block 0 — floor BEFORE | **PASS** | `[PASS] boot-health — 6/6 positive · 0 forbidden` · bundle `boot-health-20260725T110015Z` |
| Block 1 — the move, app STOPPED | **DONE** | clean SIGTERM stop 12:40:41; dongle `1-2` → `3-2.4.2`; Rosonway on own 12 V PSU into a Pi USB-2 socket |
| Block 2 — boot + identity glance | **PASS** | `RADIO UP after 12s`; relinked ×6; zero rejoin tokens; byte-identical `stableId` |
| **Block 3 — floor AFTER** | **PASS** | `[PASS] boot-health — 6/6 positive · 0 forbidden` · bundle `boot-health-20260725T162200Z` |
| **Block 4 — I3b [S]** | **PASS** | `[PASS] usb-reenumeration-manual — 3/3 positive · 0 forbidden` · bundle `usb-reenumeration-manual-20260725T172815Z` |
| Block 5 — close | **DONE** | app running (pid 34635); no constants edit; no deploy |

**Single-variable discipline held.** Exactly one thing changed between the two green floors: the coordinator's USB path. No config edit, no deploy, no `git pull`, no reboot, no other cabling change, no device button presses, no constants edit.

---

## §2 — The standing topology

```
Pi 5 · black USB-2 socket (Bus 003 Port 002)
 └── VIA Labs VL822   2109:2822  4 ports  480M   ← Rosonway stage 1 (upstream)
      └── port 4 ──── Realtek RTS5411  0bda:5411  4 ports  480M   ← stage 2 (cascaded)
           └── port 2 ──── SONOFF Dongle Plus MG24  10c4:ea60  cp210x  12M   ← THE COORDINATOR
```

`DEVPATH=/devices/platform/axi/1000120000.pcie/1f00300000.usb/xhci-hcd.1/usb3/3-2/3-2.4/3-2.4.2/3-2.4.2:1.0/ttyUSB0/tty/ttyUSB0`

- **7-port hub = 4 + 4 cascaded, one port consumed by the cascade.** Physical port 5 (a standard USB-A 3.0 port) resolves to the Realtek stage, logical `3-2.4.2`.
- **USB-2 uplink confirmed by construction, not by trusting the socket colour.** A USB 3.2 hub in a USB-3 socket enumerates on *both* the HS and SS buses. It appears **once, at 480M, on Bus 003 only**; Buses 002 and 004 (5000M) are empty. The SuperSpeed link never trained, so the hub and its uplink emit no 2.4 GHz SuperSpeed noise — the AN1017 discipline satisfied by the socket choice rather than asserted.
- **The Pi 5 socket map, derived from the instrument** (Bus 001 has 2 HS ports and Bus 002 has 1 SS port; likewise 003/004): Blue-A = `1-1`+`2-1` · Black-A = `1-2` · Blue-B = `3-1`+`4-1` · Black-B = `3-2`. The dongle was on Black-A pre-move, so the direct-attached baseline was *already* USB-2 — one fewer confound.
- `dmesg` records a first uplink attempt in a blue socket at kernel `784643` (four enumerations: `1-1`, `1-1.4`, `2-1`, `2-1.4`), a disconnect at `784749`, and the corrected USB-2 plug at `784753` (two enumerations, both 480M). **The double-enumeration test caught it in real time.**
- **Runtime PM preserved:** `power/control` reads `6 auto · 1 on`. The single `on` is the dongle, re-pinned by `iac/99-zigbee-coordinator.rules:12` firing on the re-enumeration `add` event. A parent hub cannot runtime-suspend while a child is held `on`, so the dongle's forced state protects the whole chain.

---

## §3 — Measurements

### 3.1 Boot envelope — no cost from the topology

| Boot | Log | Topology | RADIO UP |
|---|---|---|---|
| Block 0 `boot-health` | `bench-2026-07-25-070003.log` | direct on Pi (`1-2`) | **12 s** |
| Block 2 manual `start` | `bench-2026-07-25-121622.log` | behind hub (`3-2.4.2`) | **12 s** |
| Block 3 `boot-health` | `bench-2026-07-25-122148.log` | behind hub (`3-2.4.2`) | **12 s** |

Three boots, two topologies, **zero delta**. Adding two cascaded transaction translators to a full-speed (12 M) serial device's path cost nothing measurable. Both post-move boots carried **zero** `transport_failed` / `port_unhealthy` / `reopen_no_target` / `ASH_ERROR` at idle.

### 3.2 Autonomous reopen — TWO independent reps behind the hub

The operator accidentally pulled and re-seated the dongle **before** pressing ENTER, producing a complete, fully-resolved recovery cycle *outside* the evidence window. It is banked here as a free second rep; it never touched the verdict.

| | Rep 1 (pre-window, accidental) | Rep 2 (**the I3b rep**) |
|---|---|---|
| `zigbee.transport_failed` | 13:24:25.682 Pi-local | 13:24:59.732 Pi-local |
| `lastFrame` | `DATA(frm=5, ack=4)` | `DATA(frm=0, ack=1)` |
| `zigbee.port_unhealthy: cause=read-error` | 13:24:25.682 | 13:24:59.733 |
| `reopen_no_target` ×4 (Δ from failure) | +0.004 / +1.008 / +3.012 / +7.018 s | +0.002 / +1.005 / +3.009 / +7.016 s |
| `zigbee.reopened: port=/dev/ttyUSB0` | 13:24:42.433 | 13:25:16.477 |
| `port_reopened: recovery succeeded after` | **4 failed attempts** | **4 failed attempts** |
| **Detection → reopen** | **16.751 s** | **16.745 s** |

**Δ between reps = 6 ms. Backoff ladders identical to within 4 ms.** Against I3a's direct-attached ~17 s of record, the hub-attached envelope is indistinguishable.

The differing `lastFrame` counters corroborate two genuinely separate port deaths: `frm=5, ack=4` is mid-session; `frm=0, ack=1` is the start of a *fresh* ASH session, i.e. after rep 1's recovery reset the counter.

**Operator testimony (recorded per playbook §4a), and it agrees with the instrument:** *"Yes I accidentally pulled the dongle then reseat it once before I pressed enter to actually start the evidence window."* · ENTER #1 marker `17:24:50` vs launch `17:24:15` = 35 s, matching his *"no longer than like 30 seconds."* Rep 1's recovery completed 8 s **before** ENTER, so the window opened on a healthy port.

### 3.3 Identity and continuity across the move

- `zigbee.port_identity_captured: stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false` — **byte-identical pre- and post-move**, re-derived independently by the running adapter on the new path. The udev rule keys on VID/PID/serial (`99-zigbee-coordinator.rules:11`), so the by-id name carries no topology-derived component; `-if00-port0` is the serial-port index within the USB interface, not a physical port.
- `registry.projection_live: devices=6 entities=6 position=25065` on every boot (meets `min=25065`).
- `adoption_maps_rehydrated: devices=6` · `learned_zonetypes_rehydrated: count=1` (the persisted CONTACT learn survived) · `network_resumed: channel=20 panId=0x774c`.
- **`device_relinked` ×6 on every boot** — the lawful rehydration signature, exactly as the package's semantics-correction states.
- **ZERO** `device_proposed` / `UNSECURED_JOIN` / `permit_join_opened` / `device_announce` on every post-move boot (grep exit 1 against a verified-non-empty log). **The fleet never noticed the move.**
- All six remembered ULIDs matched on the `/api/v1/entities` assert, both floors.

---

## §4 — 🔴 FINDING **RUNS-TRIGGEREDAT** — `triggeredAt` is understated by exactly `durationMs`

**This is the section to layer-2 hardest.** It is a defect on the FROZEN v1.1 read surface with a live false-FAIL path into the B1 instrument, and it survived I3a undetected.

### 4.1 The observation

Pre-flight baseline run `01KYD3D4VN6B5M7PBT41FA1F3D` (automation `bench-hero`, `automationId 01KYD1AFM4CC6X3Z6X55F249NN`):

| Source | Value |
|---|---|
| `/api/v1/runs/{id}/causal-chain` → `trigger.matchedAt` | `2026-07-25T16:58:15.782896Z` |
| `/api/v1/runs` → `triggeredAt` | `2026-07-25T16:57:41.578896Z` |
| **Difference** | **34.204000 s** |
| `outcome.durationMs` | **34204 ms** |
| Exact to the microsecond? | **Yes** |

`triggeredAt` = `matchedAt` − `durationMs`. Not approximately — on every digit.

### 4.2 External corroboration — `matchedAt` is the true instant, `triggeredAt` is the wrong one

The trigger's `subjectRef` is the SNZB-03P occupancy entity `01KX1PB9AAB4VB3E10BD477TV3`. Its own state record, read independently:

- `lastChanged` = `lastReported` = **`1784998695.782896` = 2026-07-25T16:58:15.782896Z** — **identical to `matchedAt` to the microsecond.**
- The same entity read 6 min later: `lastChanged` = `1784998760.189004` = `16:59:20.189Z`, `occupied: false` — a clean 64.4 s occupancy hold from a single wave.
- **Nothing changed state at 16:57:41.** The alternative reading — that the run genuinely started at `triggeredAt` and `matchedAt` was mis-stamped — requires a state change that provably did not occur.

### 4.3 Independent reproduction on the I3b run itself — and the decisive form of the evidence

The qualifying run for Block 4's positive #3, `01KYD5305W1ZXNMPK01AGNDZTX`, read directly:

| Run | `trigger.matchedAt` | runs-list `triggeredAt` | Difference | `outcome.durationMs` | Exact? |
|---|---|---|---|---|---|
| pre-flight `01KYD3D4VN6B5M7PBT41FA1F3D` | `16:58:15.782896Z` | `16:57:41.578896Z` | **34.204000 s** | **34204 ms** | ✅ |
| **I3b `01KYD5305W1ZXNMPK01AGNDZTX`** | `17:27:40.471693Z` | `17:27:06.421693Z` | **34.050000 s** | **34050 ms** | ✅ |

**The two runs have DIFFERENT durations — 34.204 s and 34.050 s — and the offset tracks each one exactly.** This is the decisive form: it refutes "a fixed constant offset" and establishes that the discrepancy **equals the run's own `durationMs`**, run-dependent, to the microsecond, on both observations.

Operational corroboration on the I3b run: ENTER #2 marker (bundle `resolved.json`) = `17:27:34Z`; `matchedAt` = `17:27:40.472Z` = **6.47 s later** — the operator's 3 m walk to the sensor, following the timer's GO at `17:27:29`.

*Prediction check, recorded for honesty:* this report's pre-capture prediction was `matchedAt ≈ 17:27:40.626Z`, derived by applying the pre-flight run's 34.204 s. The measured value is `17:27:40.472Z` — a **0.154 s** residual, which is exactly the difference between the two runs' durations (`34.204 − 34.050`). The prediction was off by precisely the amount it assumed a constant where the mechanism is run-dependent — which is itself confirmation of the mechanism.

### 4.4 The consequence — a dead zone in `new_run_after`

`tools/runner/engine.py` `eval_new_run_after()` reads the **runs-list `triggeredAt`** and applies the anti-false-PASS arm:

```python
triggered = parse_iso_utc(run.get("triggeredAt"))
if triggered < m_observed:
    ignored.append("%s: triggeredAt %s predates M_observed %s" % ...)
    continue
```

With `triggeredAt` understated by the run's duration, **every `new_run_after` scenario carries a dead zone of width `durationMs` immediately after `M_observed`.** A genuine post-reopen run triggered inside it reports a `triggeredAt` that predates `M_observed` and is silently discarded.

**The dead zone is not a fixed window — it is as wide as whatever the qualifying run's own duration turns out to be** (§4.3: 34.204 s and 34.050 s on two consecutive runs of the same automation). Any mitigation must therefore be bounded by the *worst-case* chain duration for the triggering automation, not by an observed sample. A longer chain — more actions, stacked confirmation timeouts, a cascade — widens the dead zone proportionally, and nothing on the read surface advertises it.

**Tonight's numbers:**

| | |
|---|---|
| `M_observed` (engine's own UTC observation of `zigbee.reopened`) | `17:25:16.641913Z` |
| Engine poll lag (log line → `M_observed`) | 0.165 s |
| **Dead zone** | **`17:25:16.642` → `17:25:50.846` — 34.204 s wide** |
| Actual reported `triggeredAt` | `17:27:06.422Z` |
| **Margin above `M_observed`** | **109.78 s** |

**Counterfactual, had the operator pressed ENTER promptly at the Act-2 prompt** (as the package and the scenario's own act text imply): wave ≈ `17:25:30` → reported `triggeredAt` ≈ `17:24:56.4` → **predates `M_observed` by ~20 s → run IGNORED → positive #3 times out at 90 s → `[FAIL]`**, with the failure landing on the reopened transport and, by construction, on the Rosonway.

**Mitigation used, and it was load-bearing:** a deliberate **90 s wait at the Act-2 prompt** before pressing ENTER. The prompt has no timeout and the `within: 90s` clock starts at ENTER, so the wait is free. It is not in the package or the scenario.

### 4.5 Why I3a never saw it

The scenario's Act-2 note instructs: *"If the SNZB saw you during the re-seat it may hold occupied for ~59 s — let it clear BEFORE pressing ENTER."* On a bench where the sensor watches the rack, that instruction **incidentally** pushes the wave past the ~34 s bias. Tonight's geometry — the SNZB-03P sited in a corner, pointed away, blind to the rack — removed that accidental protection: the hold never latched, so the operator had no reason to wait.

**The bug was always there. I3a's bench layout hid it.** It follows that the protection every prior rep enjoyed was coincidental, and any future rep on a different physical layout re-exposes it.

### 4.6 What the hub owes this

1. **Source read** of the run-record write path and `ListRunsEndpoint.java:127` (`triggeredAt = Instant.toString()`, per the scenario header's own citation). Determine whether `triggeredAt` is stamped from a completion-relative computation, or whether it is a different concept from `trigger.matchedAt` that is merely mis-named on the wire. **This report deliberately does not diagnose the cause** — the bench measured the arithmetic; naming the defect is a source-read job.
2. **Contract question.** If `triggeredAt` is wrong, the fix is a v1.1.x change to a FROZEN surface and rides the four-constraint law (additive-only · wire-casing at the endpoint · emitter-leads · version discipline). If it is *correct-but-differently-defined*, then **`new_run_after` binds the wrong field** and the engine should bind `matchedAt` — a B1/B2 instrument change, not a contract change. **These are opposite fixes; the source read decides which.**
3. **Sweep.** `new_confirmed_run` (the B2 STRONG variant) uses the same runs snapshot but does **not** currently apply a `triggeredAt` bound — confirm it is unaffected before B2's port lands, and re-check at the CMD-API flip.
4. **Package rule.** Until resolved, every operator package containing a `new_run_after` leg must specify a wait ≥ the automation's chain duration after the anchor, and must not rely on the occupancy-hold instruction to supply it implicitly.

---

## §5 — Secondary observations

**5.1 — never-false-CONFIRMED, demonstrated on silicon.** The pre-flight run's causal chain, all five commands targeting the Hue LCA017 `01KX1PA4HSJ581GASYB7DHE40F` (physically off-network pending HUE-RESET):

```
turn_on              → UNCONFIRMED  "confirmation timed out"
set_brightness 50    → UNCONFIRMED  "confirmation timed out"
set_color_temp 4550  → FAILED       "superseded by a newer command on the same attribute;
                                     superseding command event 01KYD3DJR13QPHVCXTSC5TDCA6"
set_color_temp 4525  → UNCONFIRMED  "confirmation timed out"
identify 5s          → FAILED       "DefaultResponse SUCCESS +90 ms, then no report, ever"
```

Five commands into a lamp that is not there, and **not one returned `CONFIRMED`.** `"DefaultResponse SUCCESS +90 ms, then no report, ever"` is the system explicitly refusing to treat an ACK as proof. The I3b run's own chain: `['UNCONFIRMED','UNCONFIRMED','FAILED','UNCONFIRMED','DISPATCHED']` — five real dispatches through the reopened transport, mirroring I3a's evidence shape.

**5.2 — the §3.9 SKIP gate did NOT fire, and that is worth SKIP-VIS's attention.** The expectation going in was `SKIPPED` outcomes for an off-network target. Instead the Hue entity reads `AVAILABLE` (log-rehydrated), the skip gate never engages, and commands dispatch into the void and time out honestly. Honest — but it means "availability" and "reachability" have diverged on the read surface in a way a dashboard consumer would have to reason about.

**5.3 — availability is NOT an RX proof, confirmed by measurement.** The SNZB-03P read `"availability":"AVAILABLE","stale":false` while its `lastReported` was **4 h 35 m old**, with `"staleAfter": null`. Any bench or UI claim that reads AVAILABLE as evidence of live radio contact is unsound. The only live-traffic evidence tonight is Block 4's positive #3.

**5.4 — `actionCount: 9` but `actions[]` lists 5**, with `commandCount: 5`. The four non-command actions (the scripted delays) are counted but not surfaced in the causal chain. Possibly by design; worth one question given the explainability hero is *"why did it fire?"*

**5.5 — `pending_positive_tokens()` cosmetic defect (engine).** The Act-2 operator block printed `DONE-WHEN: zigbee.transport_failed OR zigbee.port_unhealthy then api:/api/v1/runs` — re-listing a condition satisfied ~17 s earlier. Cause: for a `log_any:` line the function builds `tok = " OR ".join(...)` and for an `api:` line `tok = "api:" + path`, then tests `tok not in self.satisfied_at_index` — but that map is only ever keyed by **individual log tokens**. So **`log_any:` and `api:` lines can never be filtered out of the DONE-WHEN display.** Verdict-neutral, but it misleads a tired operator into believing a met condition is still outstanding — precisely the class §8 exists to prevent.

**5.6 — the scenario's goal string is topology-hardcoded.** `usb-reenumeration-manual.yaml` prints `GOAL: … on a physical re-seat (direct-attached topology)` — now inaccurate, since this same file just closed the **hub-attached** leg. Recommend parameterising or neutralising the string now that one file serves both legs.

**5.9 — an action outcome MUTATED after the run read `COMPLETED`.** The engine's successful poll (bundle stamp `20260725T172815Z`, ≈0.5 s after the run's completion at `matchedAt + durationMs` = `17:28:14.52`) quoted `['UNCONFIRMED','UNCONFIRMED','FAILED','UNCONFIRMED','DISPATCHED']`. The same chain re-read at `17:57:12` reads `[…,'FAILED']` for that fifth action — `identify`, reason `"DefaultResponse SUCCESS +90 ms, then no report, ever"`, a determination that by construction requires a confirmation window to expire. So **`outcome.status: COMPLETED` can be published while an action's outcome is still non-terminal, and that outcome later changes.** Honest in the sense that the system refuses to assert `FAILED` before it knows — but a consumer reading the chain at COMPLETED gets a different answer than the settled truth. Direct relevance to the explainability hero *"did it actually confirm?"* and to FE-VERDICT-2, which must decide whether to render a provisional outcome, and to SKIP-VIS's emitter half. Verdict-neutral for `new_run_after` (the assert is deliberately outcome-agnostic), but it means the assert can be satisfied by a *provisional* outcome.

**5.7 — `uhubctl` is NOT installed on the Pi.** `which uhubctl` → absent. The AUTO usb scenario (`usb:` driver, `drivers.py:usb_act`) needs it; `sudo apt-get install uhubctl` belongs in the B2 session's prep, not tonight.

**5.8 — candidate `usb.*` constants for the B2 re-mint.** Physical port 5 = logical `3-2.4.2`, i.e. hub location `3-2.4`, port `2`. **CANDIDATE ONLY — not minted.** `constants.yaml` requires these be read from `uhubctl`'s own output, which was not possible tonight. No constants file was edited.

---

## §6 — Corrections applied to the operator package in-session

The package was run block-by-block by a guiding session which grounded every expectation against `scenarios/*.yaml`, `tools/bench.sh`, `tools/runner/engine.py` and `iac/99-zigbee-coordinator.rules` before dispatch. Five corrections were required. All are of the class playbook §8 already names: *a glance-point asserting something the instrument cannot deliver.*

| # | Correction | Grounding |
|---|---|---|
| **C-1** | **OPERATOR-tier scenarios require an interactive TTY.** With no TTY the engine prints *"no tty — window opens now"* and does **not** wait — the 30 s window opens before the operator's hands are ready. `ssh pi '<cmd>'` is fatal here; a plain interactive `ssh pi` session is required. | `engine.py print_operator_block()` — `if sys.stdin.isatty(): input()` else the no-tty note |
| **C-2** | **Block 4 has TWO operator acts, not one.** The package named only the pull/re-seat. Act 2 is the SNZB-03P wave, gated `after: zigbee.reopened`. An operator who walks away after the re-seat FAILs positive #3. | `usb-reenumeration-manual.yaml stimulus[1]` |
| **C-3** | **`boot-health` restarts the app itself** (`stimulus: bench: restart`). The package implies the operator manages app state around Blocks 0 and 3; they must not. | `boot-health.yaml` |
| **C-4** | **The reopen target is the by-id `stableId`, not `/dev/zigbee`.** A gate on the alias alone is insufficient — the alias could resolve while the captured stable identity changed, passing boot-health and then dying in Block 4 on `reopen_no_target`. A byte-check on the exact `stableId` string was added to the Block-2 gate. | `port_identity_captured … stableId=/dev/serial/by-id/…` |
| **C-5** | **The `new_run_after` dead zone** — §4. Requires an explicit wait ≥ chain duration at the Act-2 prompt. **Not in the package and not in the scenario.** | §4 |

Two further operator-ergonomics items were added and both proved load-bearing:

- **A pre-flight trigger-chain baseline** (wave → confirm `occupied:true` → confirm a new run with an executed chain) run *before* the rep, with predictions stated in advance. **This is what surfaced §4.** Recommend it become standard for any `new_run_after` leg — it separates "the wave/automation is broken" from "the transport is broken" *before* the variable is introduced, at a cost of ~3 minutes.
- **A disambiguation table for the "no `/dev/zigbee`" branch**: `cp210x` absent from `lsusb` = an unpowered hub port (operator-fixable, not a finding) vs `cp210x` present but no symlink = the genuine udev finding (STOP). The package collapsed both into "STOP + paste."

---

## §7 — Re-derivation checklist for layer-2 (verify, don't re-run)

1. **R1** — Re-read the run-record write path + `ListRunsEndpoint.java:127`. Confirm or refute: `runs[].triggeredAt` is not the trigger instant. **The load-bearing claim of §4.**
2. **R2** — Re-derive the arithmetic from the quoted payloads: `matchedAt 16:58:15.782896` − `triggeredAt 16:57:41.578896` = `34.204000 s` = `durationMs 34204`. Confirm exactness.
3. **R3** — Confirm the external corroborator: SNZB-03P `lastChanged` = `1784998695.782896` = `16:58:15.782896Z`, identical to `matchedAt`. This is what makes `matchedAt` the true instant.
4. **R4** — Re-read `engine.py eval_new_run_after()` and confirm the `triggered < m_observed` arm discards on the runs-list field, and that `new_confirmed_run` applies no equivalent bound.
5. **R5** — Confirm the Block-4 forbidden scoping was correct: four `reopen_no_target` lines at `13:24:59.734`–`13:25:06.748` all precede `zigbee.reopened` at `13:25:16.477`, so the `after:`-scoped forbidden was inactive. **Verdict soundness depends on this.**
6. **R6** — Confirm rep 1 (`13:24:25.682` → `13:24:42.433`) lies **outside** the evidence window: marker 1 `at 17:24:50Z`, `log_offset 11672`. Rep 1 must not have contributed to the verdict.
7. **R7 — CLOSED in-session (2026-07-25 17:57:12Z).** The I3b run's own causal chain was read directly and confirms the mechanism on a run whose duration **differs** from the pre-flight run's:
   ```bash
   curl -s -H "Authorization: Bearer $(cat ~/hs-bench/config/initial_api_token)" \
     "http://127.0.0.1:7070/api/v1/runs/01KYD5305W1ZXNMPK01AGNDZTX/causal-chain" | python3 -m json.tool
   ```
   Measured: `matchedAt 17:27:40.471693Z` · `durationMs 34050` · runs-list `triggeredAt 17:27:06.421693Z` · difference **34.050000 s = durationMs, exact**. Nothing is owed. Layer-2 re-derives from the quoted payloads (§4.3), not by re-running.
8. **R8** — Confirm CI/deploy state untouched: the Pi still runs `355a711`; no pull, build, or deploy occurred.

### Open questions, ranked

- **Q1 (contract).** Is `triggeredAt` a defect, or a correctly-computed different concept that `new_run_after` binds wrongly? **Opposite fixes.** Blocks any decision on §4. *(Note for the source read: the offset equals `durationMs` on two runs of differing duration, so any explanation must be duration-derived — a fixed-offset or clock-skew hypothesis is already refuted by the data.)*
- **Q1b (explainability).** §5.9 — `COMPLETED` published alongside a non-terminal action outcome that later flips. Is the causal chain intended to be re-readable/mutable after terminal status, and what should FE-VERDICT-2 render in that window?
- **Q2 (instrument reach).** Does the dead zone affect other scenarios, and does it interact with the CMD-API flip / B2's `new_confirmed_run`?
- **Q3 (packaging).** Should the pre-flight trigger-chain baseline become a standing clause for `new_run_after` legs? It cost 3 minutes and saved the rep.
- **Q4 (observability).** `actionCount 9` vs `actions[]` = 5 (§5.4) — intended, or an explainability gap?
- **Q5 (engine).** `pending_positive_tokens()` (§5.5) — one-line fix, verdict-neutral, operator-facing.
- **Q6 (bench state).** `uhubctl` install + the real `usb.hub-location`/`usb.port` mint — sequence into B2, candidates in §5.8.

---

## §8 — Assessment

**The topology move is a non-event, and that is the strongest possible result.** Three boots at an identical 12 s, two reopen reps 6 ms apart, a byte-identical stable identity, zero rejoin tokens, zero idle transport errors, and both floors green. The single-variable framing held: exactly one thing changed, and the platform could not detect it. **I3b [S] closes, and the M14 RO condition is now proven in both topologies.**

**The engineering signal is §4, not the [S] row.** A frozen read surface reports a timestamp that is wrong by a run-dependent amount, the project's own regression instrument binds that field, and the resulting false-FAIL window is invisible on any bench where the occupancy sensor happens to watch the rack. It was found only because a pre-flight baseline was run *before* the variable was introduced — instrument-first, predictions stated in advance, exactly as playbook §1 and §4c prescribe. Had the rep been run straight from the package, tonight's output would have been a `[FAIL]` paste blaming a USB hub for a JSON field.

**The accidental pull is the report's second-best datum.** An operator error, honestly reported, converted into an independent second rep that matched the deliberate one to six milliseconds. That is the §4a rule paying off: operator actions are data, and a testimony that agrees with the instrument turns a wobble into a confirmation.

**The package's own defect class recurred.** Five corrections were needed, and every one was a glance-point asserting something the instrument could not deliver — the same class as D-1/D-2 from the 04P run. The class is now large enough to be worth a standing authoring checklist rather than a per-package catch: *does every asserted token exist, on the surface named, at the moment asserted, through the interface the operator will actually use?* C-1 (TTY) and C-5 (the dead zone) are both "at the moment asserted, through the interface actually used" failures, and neither is visible from reading the scenario YAML alone.

**Bottom line for adjudication.** Result: GREEN. I3b [S]: CLOSED. Topology: STANDING. Safety: intact — no identity regression, no rejoin, no forbidden hit anywhere in the session. **No captures owed** (R7 closed in-session). Layer-2 asks, in order: rule **Q1** (defect vs mis-bound field — the two runs of differing duration already refute any fixed-offset or clock-skew explanation, so the source read is narrowly scoped), rule **Q1b** (§5.9, the mutable post-COMPLETED outcome — it lands on FE-VERDICT-2 and SKIP-VIS), and decide whether §6's pre-flight baseline becomes standing law for `new_run_after` legs.

*— End of report. Refutation welcome in both directions; the quoted log lines, API payloads, and bundle markers are the evidence.*

---

## Appendix A — Artifacts

**Bundles (on the Pi, `~/hs-bench/bundles/`):**

```
usb-reenumeration-manual-20260725T172815Z   ← I3b [S] — the closing paste
boot-health-20260725T162200Z                ← Block 3, the floor AFTER
boot-health-20260725T110015Z                ← Block 0, the floor BEFORE
```

Each contains `MANIFEST.txt · scenario.yaml · resolved.json · app-log-slice.log · journal-slice.txt · api-captures.json · verdict.txt`.

**Boot logs:** `bench-2026-07-25-070003.log` (Block 0) · `bench-2026-07-25-121622.log` (Block 2) · `bench-2026-07-25-122148.log` (Block 3 + the Block-4 run window; **the standing boot**).

**Run IDs:** pre-flight baseline `01KYD3D4VN6B5M7PBT41FA1F3D` · **I3b qualifying run `01KYD5305W1ZXNMPK01AGNDZTX`** · automation `bench-hero` `01KYD1AFM4CC6X3Z6X55F249NN`.

**Entities referenced:** SNZB-03P occupancy `01KX1PB9AAB4VB3E10BD477TV3` · Hue LCA017 `01KX1PA4HSJ581GASYB7DHE40F`.

## Appendix B — Master timeline (UTC; Pi-local = UTC−4)

```
10:59:35  pre-move instrument capture — /dev/zigbee -> ttyUSB0, dongle at 1-2 (Black-A)
10:59:45  BLOCK 0  [PASS] boot-health 6/6 · 0 forbidden   RADIO UP 12s   pos=25065
12:40:41  BLOCK 1  bench.sh stop -> [OK] stopped
12:40:46  ......... zigbee.transport_failed — DEATH RATTLE, T+5.8s, inside JVM shutdown (not a defect)
13:23:09  ......... Rosonway verified on a true USB-2 socket (single 480M enumeration, Bus 003)
                    dmesg shows an earlier blue-socket attempt (4 enumerations) corrected 3.7 s later
16:05     ......... dongle -> Rosonway physical port 5  (= 3-2.4.2)
16:10:57  BLOCK 2  GATE: stableId byte-identical — reopen target survived
16:11:15  ......... 6 auto · 1 on ; dongle 3 hops out, 12M ; dmesg clean
16:16:22  ......... bench.sh start -> RADIO UP 12s ; relinked x6 ; zero rejoin ; 0 transport/ASH
16:16:54  ......... 6/6 entities AVAILABLE stale=false  (informational — NOT an RX proof, §5.3)
16:21:41  BLOCK 3  [PASS] boot-health 6/6 · 0 forbidden   RADIO UP 12s
                   >>> THE TOPOLOGY CHANGE IS PROVEN CLEAN, SINGLE-VARIABLE <<<
16:57:59  PREFLIGHT baseline runs read (qualifying run not yet materialised)
16:58:15.783        wave -> occupied:true ; matchedAt identical to the microsecond
17:00:24  ......... new run visible; triggeredAt 34.204 s EARLY  >>> FINDING RUNS-TRIGGEREDAT <<<
17:04:22  ......... causal chain: bench-hero, SNZB-03P trigger, 5 outcomes, durationMs=34204
17:24:15  BLOCK 4  scenario launched
17:24:25.682 ...... REP 1 (accidental, pre-window)  -> reopened 17:24:42.433   = 16.751 s
17:24:50  ......... ENTER #1  (marker, log_offset 11672)
17:24:59.732 ...... REP 2 (the I3b rep)             -> reopened 17:25:16.477   = 16.745 s
17:25:16.642 ...... M_observed ; DEAD ZONE 17:25:16.642 -> ~17:25:50.7 (width = the run's own durationMs)
17:25:59  ......... 90 s wait started (the §4.4 mitigation)
17:27:29  ......... GO
17:27:34  ......... ENTER #2 (marker, log_offset 14343)
17:27:40.472 ...... wave — matchedAt MEASURED (+6.47 s after ENTER #2, +143.83 s over M_observed)
                    reported triggeredAt 17:27:06.422 = matchedAt - durationMs(34050) ; +109.78 s over M_observed
17:28:14.52 ....... run COMPLETED (matchedAt + 34.050 s)
17:28:15  ......... [PASS] usb-reenumeration-manual — 3/3 positive · 0 forbidden
                   >>> I3b [S] CLOSED <<<   (engine quoted identify as DISPATCHED here — see §5.9)
17:36:16  BLOCK 5  3 bundles banked ; app running pid 34635 ; uhubctl absent ; no constants edit
17:57:12  R7 ..... I3b causal chain re-read: offset = durationMs 34050, EXACT (2nd direct rep)
                    identify now reads FAILED — the outcome mutated post-COMPLETED (§5.9)
```
