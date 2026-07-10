<!--
file: context/assessments/2026-07-10_bench-automation-and-test-suite_direction-brainstorm.md
purpose: The hub's structured brainstorm of Nick's 2026-07-10 direction charge — automating bench/test execution on the Pi as logging/catch/troubleshoot/fix confidence matures; building a smart-home test-suite library; and the runway that library creates for the platform's automation/AI/ML ambitions. Analysis layer; feeds a charter + rows on Nick's ruling, not standing state.
audience: Nick (ruling); the hub (charter authoring); future WU authoring.
state-type: assessment (point-in-time brainstorm; supersedable by the ruled charter).
status: CURRENT at authoring — written by the v27 hub at beat 1, soak day 1 (nothing here lands on the Pi mid-soak; the design work is deliberately desk-only).
-->

# Bench Automation & the Test-Suite Library — Direction Brainstorm

## 0. The charge (Nick, 2026-07-10, paraphrase-faithful)

Automate the way we test/run benches on the Pi as confidence grows in our ability to log, catch, troubleshoot, and fix. This matters for (a) building a healthy smart-home test-suite library, (b) more fine-tuned testing — which is predicated on correct functionality of the HomeSynapse platform we are continuously refining and studying, and (c) the automation/AI/ML capacities we want the ecosystem to accommodate. The dependency order in (b) is the load-bearing insight: **fine-tuned testing presupposes certified functionality — which is exactly what the acceptance arc + soak are producing right now.** This direction is the natural next consumer of the certification.

## 1. What already exists (the assets the library composes from)

1. **The oracle is built.** The moat's verdict stream (`command_result` / `state_confirmed` / `command_confirmation_timed_out`, never-false-CONFIRMED) is a machine-readable ground-truth channel. A test harness normally has to SOLVE the oracle problem; ours ships it as the product.
2. **Frozen log tokens** — every glance-point of the acceptance run (`projection_live`, `adoption_maps_rehydrated`, `device_relinked`, `key_established`, `reporting_configured`, the verdict tokens) is a stable, grep-exact assertion surface, deliberately frozen under test pins.
3. **`tools/bench.sh`** — the decisive-verdict pattern (launch → poll → HEALTHY/FAILED with evidence) is already the right *shape*; today it covers launch/stop/status/health/log/entities/runs/events.
4. **The runbook** — a human-executable scenario library in prose. Phases 0–6 + §51 legs are effectively test cases with preconditions, stimulus, expected tokens, and done-whens. They were executed by hand this week; most are mechanically checkable.
5. **The read-API + event log** — positions, ULIDs, causation chains; the acceptance run's §51 evidence was adjudicated from these. (The bench read raw SQLite this week; the API is the right assertion surface — see the supersession-decrypt ruling.)
6. **The hardware-free tier already runs in CI** — the seeded-corpus regression tests and the zigbee hardware-free rig. The library's Tier A exists; what is missing is the silicon tier's automation.
7. **journalctl as a first-class instrument** (acceptance-run lesson) — kernel-side truth for physical events (re-enumeration, port claims).

## 2. The core move: encode the runbook as a scenario library

A **scenario** is a declarative unit: `{preconditions, stimulus, expected-evidence (positive tokens/events with timeouts), forbidden-evidence (WARN/failure tokens), verdict}`. The runner executes stimulus, polls evidence through the read-API + log, and returns a decisive verdict with an evidence bundle. Anti-vacuous discipline carries over from the bench doctrine: **every scenario asserts at least one positive-evidence line** — absence-of-WARN alone is never a pass (the vacuous-VERIFY class, killed at design time).

Two tiers, explicitly labeled per scenario:

- **Tier AUTO** — runnable with zero human hands, schedulable nightly ("bench CI"). Stimulus = REST commands (turn_on/off, brightness, identify), restarts (`bench.sh restart`), and out-of-band actuators (§3). Examples ported straight from this week: boot-health (projection_live N/N + rehydration INFO + relink ×N, zero proposals), command-confirm (brightness → CONFIRMED ≤ corpus envelope), supersession probe (CT pending → superseding dispatch → superseded verdict ≤ Xms + exactly one CT confirm), timeout-honesty/no-change (command an already-set value → honest timeout, zero false CONFIRM), identify immediate-honest (UNCONFIRMED ≤ Yms with reason verbatim), restart-identity (NQ-6 shape: restart → same ULIDs API-to-API).
- **Tier OPERATOR** — needs human hands (pairing button holds, factory resets, physical placement/RF changes). Stays a runbook, but inherits the decisive-verdict pattern: `bench.sh scenario <name>` prints the one physical act, polls for its named signal, verdicts. The tired-operator lessons (§2A of the acceptance retrospective) become code.

## 3. Automation levers for the physical layer (what buys AUTO coverage)

1. **Out-of-band smart plug** (WiFi, local-API class — Tasmota/Shelly; NOT Zigbee, NOT through HomeSynapse): wall-power control for the Hue. Automates the absent-device timeout class, the rejoin race, and L1-style relink-on-re-announce. **Design rule: stimulus never rides the system under test** — the actuator channel must be independent of the radio/platform being measured, or the test contaminates its own evidence.
2. **Software USB power interruption** (uhubctl class; the Pi's built-in hub is ganged — acceptable on a bench where the dongle is the only USB device): automates the dongle-pull/re-enumeration scenario — which is EXACTLY the M9.6-RO field scenario and its post-fix regression proof. The worst manual test of the arc becomes a nightly scenario.
3. **What stays human, honestly:** pairing holds (SNZB button), BT factory resets, RF-environment changes, motion (organic or operator; a servo waving at the IAS sensor is possible but not Wave-1-worthy). The library's coverage claim is always tier-labeled — no silent pretense that AUTO covers the join arc.

## 4. Phased shape (sizing; sequencing vs the ruled stack)

- **B0 — Charter + scenario-format spec** (desk-only, soak-window-safe; hub work product → Nick ratifies). Where the format lives: REC the bench repo (`nexsys-bench/scenarios/` + a spec doc) — the bench is the test-and-truth engine; promote to a core design doc only when/if the runner grows into the `hsctl` product surface (that boundary crossing is a named STOP).
- **B1 — Runner v0** (post-soak; Pi-side): `bench.sh` grows `scenario <name>` + `suite <list>` + `bundle` (evidence tarball: app-log slice + journalctl slice + event positions + verdicts per run). 3 seed scenarios: boot-health, command-confirm, timeout-honesty/no-change.
- **B2 — The §51 port**: the acceptance legs become scenarios (supersession, identify-honest, IAS-twin absorption where motion is available, restart-identity). The acceptance runbook's next execution is mostly `suite acceptance-core` + a short OPERATOR appendix.
- **B3 — Bench CI**: nightly suite on the Pi + the flight-recorder bundle on failure; a morning one-line digest (the soak-watch pattern, generalized). Hardware spend: the plug (+ optionally a controllable hub) rides this.
- **B4 — The data pipeline**: every scenario run appends labeled tuples `{scenario, stimulus, context, expected, observed, verdict, latency, positions}` to a runs-corpus (corpus v2 — the hand-built per-device latency envelopes become continuously regenerated). Drift becomes visible as data, not anecdote.
- **B5 — Learning studies** (offline, advisory-only): consume B4. Explicitly downstream of certification — the "predicated on correct functionality" clause, honored structurally.

Stack placement REC: **B0 runs NOW** (soak window, zero Pi touches). B1–B3 slot into the post-soak arc alongside the explainability push (§3 of the priority stack — they consume the same read-API and reinforce each other: the dashboard renders the same evidence the scenarios assert) and field-hardening (B-tier scenarios are the regression proofs for M9.6-RO/hs-radio/frame-counters). B4–B5 follow.

## 5. The AI/ML runway (why this is the on-ramp, and its governance rails)

The library's byproduct is the thing AI/ML needs most and smart-home stacks almost never have: **honestly-labeled behavioral data.** Because verdicts are never-false-CONFIRMED, the tuples are trustworthy training/eval labels by construction — no human annotation pass, no plausible-but-wrong labels. Concrete capacities, in ascending ambition, all inside AIOT-INV-1 (AI is never an autonomous actuator) and the SA-layer posture:

1. **Drift/anomaly detection (advisory):** per-device latency envelopes and failure-signature baselines from B4; a device whose confirm-latency distribution shifts is an early-failure signal surfaced as an observation, not an action.
2. **Learned tuning PROPOSALS:** per-device-per-firmware confirmation timeouts (the DP-a tuning we set by hand today) proposed from measured distributions — ratified through config by the human, never self-applied. The proposal artifact is reviewable evidence, same register as everything else.
3. **Failure-signature classification:** the 0x11-class diagnosis this arc did by hand (status-byte sequence → root-cause family) is a learnable mapping over the event/log corpus — an explainability assist ("this looks like the TCLK-rejection class") with citations to the matching historical evidence.
4. **Further out:** automation suggestion/ranking over observed routines — gated by the SA layer's existing consent design; out of scope until the library and dashboard are real.

The honest framing for the ruling: **B0–B3 are engineering with immediate certification leverage; B4 is cheap once B1 exists; B5 is optionality we are deliberately buying, not committing to.**

## 6. Open questions for Nick (one-turn-rulable at charter time)

Q1 — Charter B0 now (soak-window desk work)? [REC: yes]
Q2 — Home for the spec: bench repo (REC) vs core design doc now?
Q3 — Hardware spend approval class for B3 (a local-API smart plug; optionally uhubctl-capable hub) — order with Wave-2 or separately?
Q4 — Nightly-cadence appetite once B3 exists (every night vs pre-milestone)?
Q5 — Assertion surface: confirm API-first (scenarios read the app's own surfaces; raw SQLite only as a debug fallback) — aligns with the supersession-decrypt ruling REC.

## 7. Anti-goals and risks (named now so they never get improvised later)

- **Nothing lands on the Pi mid-soak.** B0 is paper; the soak's sanctity outranks this direction's momentum.
- **The library never substitutes for the operator release runbook** — AUTO-tier green is a regression floor, not a certification. Physical-tier evidence remains the release gate where it is the honest gate.
- **Stimulus independence** (§3 rule) — no self-testing through the product's own actuation channel.
- **Scenario flake discipline:** a flaky scenario is a defect (of the scenario or the platform) and gets the same instrument-first/discriminator treatment as any bench ambiguity — never a retry-until-green loop (the CI deflake precedent, `ReplayTransitionIT`, applies).
- **Token-freeze coupling:** scenarios bind to frozen tokens; the freeze discipline now carries a second consumer (the library) — token changes get a scenario-sweep obligation in the WU format, same as the grep-vocabulary rule.
