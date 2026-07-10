<!--
file: context/assessments/2026-07-11_wave2-device-dossiers_research-return.md
purpose: Wave-2 device-dossiers research return (Track B lane (a), MONDAY-BLOCKING) — four dossiers (S31 Lite zb · SNZB-02P · SNZB-04P · SNZB-01P) to the corpus standard + the Shelly Plus Plug US Gen2 stimulus-contract appendix, so the hub can author device profiles (zigbee-profiles.json entries incl. AMD-97 confirmation[]) and bench scenarios the day the soak exits (2026-07-13).
audience: the PM hub (two-layer audit → profile/scenario authoring); Nick; the B1/B3 runner WUs (the Shelly appendix's consumer).
state-type: assessment (dispatched research-lane return — WRITE-ISOLATED per the 2026-07-10 lane brief; this session writes ONLY this file; no spine, no code, no Pi).
status: RETURNED 2026-07-10 (filename per the dispatch §3). NOT yet hub-audited.
brief: context/handoff/2026-07-10_wave2-device-dossiers_lane_session_prompt.md
anchors: nexsys-hivemind/project-knowledge/device-corpus/ (README schema + the two Wave-1 entries — the corpus standard) · homesynapse-core/integration/integration-zigbee/src/main/resources/zigbee-profiles.json (the SHIPPED profile shape: matches[] + AMD-97 confirmation[]) · nexsys-bench/scenarios/SCENARIO_FORMAT.md (RATIFIED B0) · nexsys-bench/docs/2026-07-10_bench-automation-charter.md (stimulus independence; API-first) · nexsys-bench/docs/2026-07-06_m9.4-bench-acceptance-record.md (evidence-binding standard; the SNZB-03P silicon fingerprint) · homesynapse-core-docs/design/02-device-model-and-capability-system.md §3.6/§3.10 (Locked) · design/08-zigbee-adapter.md §3.5/§3.7/§3.10/§3.12 (Locked).
sources-discipline: EVERYTHING here about Wave-2 hardware is SECONDARY evidence — community-documented; silicon adjudicates on the bench. Every external claim carries a URL (inline + §7). [REF] = documented from a cited public source · [CONFIRM-ON-BENCH] = only establishable from the physical unit · FACT vs INFERENCE flagged where the line is load-bearing. No invented cluster IDs or attribute names: where sources are silent or conflict, the gap is flagged in §6, not papered over (never-false-CONFIRMED applies to research too).
-->

# Wave-2 Device Dossiers — S31 Lite zb · SNZB-02P · SNZB-04P · SNZB-01P (+ the Shelly Gen2 stimulus contract)

## 0. Method, calibration, and cross-cutting findings

### 0.1 What this return feeds (the Monday consumers)

Three artifacts the hub authors the day the soak exits, all of which pull directly from the per-device sections below: (1) **corpus entries** (`project-knowledge/device-corpus/devices/*.md`, schema-version 1 — the README template); (2) **device profiles** in `homesynapse-core/integration/integration-zigbee/src/main/resources/zigbee-profiles.json` — `matches[]` (exact_model + fingerprint) and the AMD-97 `confirmation[]` block per actuating capability, in exactly the shipped shape (`profileId`/`matches`/`category`/`confirmation`; the Hue + SNZB-03P entries are the reference instances); (3) **bench scenarios** in the SCENARIO_FORMAT v0 idiom (`nexsys-bench/scenarios/SCENARIO_FORMAT.md`, RATIFIED 2026-07-10) — §N.6 of each dossier (§4.7 for the button) sketches the seeds. The Shelly appendix (§5) is a different consumer: it is the driver spec for the `plug:` stimulus verb the charter §4 hardware unlocks (`bench.sh`, B1+; nightly B3).

### 0.2 Evidence discipline and the Wave-1 calibration (read before trusting any endpoint map)

Everything below about Wave-2 hardware is **SECONDARY evidence — community-documented; silicon adjudicates on the bench.** Tags follow the corpus convention: `[REF]` = cited public source; `[CONFIRM-ON-BENCH]` = only the physical unit can establish it.

The calibration precedent is the SNZB-03P. Its pre-populated corpus entry (desk research, 2026-06-26) predicted EP1 in-clusters `{0x0000, 0x0001, 0x0003, 0x0406}` / out `{0x0019}`. The **bench-captured** fingerprint shipped in `zigbee-profiles.json` is in `{0x0000, 0x0001, 0x0003, 0x0020, 0x0406, 0x0500, 0xFC57}` / out `{0x0003, 0x0019}` — real silicon carried **PollControl `0x0020`, IAS Zone `0x0500`, and the SONOFF custom cluster `0xFC57`** that the desk pass missed, and the live device both reports occupancy AND enrolls/fires IAS (`ias_zone_enrolled endpoint=1 zoneId=0`; the acceptance run then measured the consequence — "IAS ×2 twins ABSORBED: one run per motion," bench acceptance record). Two rules fall out, applied to every dossier below:

1. **Converter docs list what the reference stack USES, not everything the device EXPOSES.** Endpoint maps below distinguish the *z2m-consumed surface* from *full-signature evidence* (ZHA quirk signatures / interview dumps), and each §N.2 names the residual-cluster classes to expect on silicon (PollControl, OTA, `0xFC57`-class custom clusters).
2. **Dual-path signaling is a live class, not a 03P one-off.** Where a device plausibly emits the same physical event on two channels (§3 contact: IAS + bound-OnOff "local linkage"; §4 button: OnOff client commands), the dossier says so explicitly — twin absorption is a bench assertion, not a surprise.

### 0.3 The platform-side anchors these dossiers bind against (pointer, not copy — re-derive at consumption)

- **Doc 08 §3.7 default reporting posture** (the values M9's `ReportingConfigurator` attempts unless the profile overrides): OnOff `0/3600/discrete` · TemperatureMeasurement `10/3600/10 (0.1 °C)` · RelativeHumidity `10/3600/100 (1 %)` · PowerConfiguration `3600/62000/0`. §N.3 of each dossier compares the z2m-shipped values against these rows and flags deltas the profile should carry.
- **AMD-97 `confirmation[]`** as shipped (per actuating capability): `capability · confirmationMode · authoritativeAttribute · reportsAuthoritative (VERIFIED_REPORTS|READBACK_ONLY|NONE) · reportingPosture (ON_CHANGE|PERIODIC|SLEEPY|NONE) · confirmability (CONFIRMABLE|BEST_EFFORT|UNCONFIRMABLE) · recommendedTimeoutMs · degradeRule[] · notes`. Sensors with **no actuating capabilities carry an empty `confirmation: []`** — the SNZB-03P entry is the precedent (empty-array ≠ UNCONFIRMABLE; UNCONFIRMABLE is for commands that exist but cannot confirm, e.g. Hue `identify`/`effect`).
- **M9.4-RPT semantics** (silicon-proven): bind → Configure Reporting → read-back verify; posture facts `VERIFIED / UNSUPPORTED / UNREPORTABLE / TIMEOUT / ack-lies`; only VERIFIED postures keep a capability report-confirmable; reporting outcomes never gate adoption. **TIMEOUT is an expected sleepy-device posture class** — the SNZB-03P runs 2/3-verified with the 5 s exchange window and that is honest BEST_EFFORT degradation, not a defect. All three battery devices below inherit this expectation.
- **Path note.** The Monday program joins Wave-2 onto the soaked EZSP/MG24 bench network (PROJECT_SNAPSHOT v27 beat 3: soak exit → close-out → deploy → silicon legs → B1 → Wave-2 joins, runbook step 26). The corpus README's index still shows the June-era "ZNP (W2)" column — per the 2026-07-10 rulings the ZBDongle-P is now the adversarial-scenario tool + the Z-Stack half of pre-M14, not Wave-2's capture path. Identity/match criteria below are stack-independent; a later ZNP cross-capture only enriches the corpus. (Hub reconciles the README column; write isolation keeps this return's hands off it.)

### 0.4 Cross-cutting findings (the headlines; detail in the sections)

1. **THE BUTTON GAP (escalation candidate, the ESC-W1-HUE-01 class).** Doc 02 §3.10's MVP entity-type table is `light · switch · plug · sensor · binary_sensor · energy_meter` — **no `button` entity type** — and §3.6 has no press-event capability in the MVP set *or* the post-MVP reserved list. Yet Doc 08 §3.10's classification table maps "On/Off Light Switch (0x0103) → `button`" (an entity type Doc 02 does not define), and the SNZB-01P's entire function is stateless press events (§4). Monday's profile authoring hits this immediately. Detail + options: §4.5.
2. **The S31 Lite zb is the corpus's first DIRECT `on_off` confirm leg.** The acceptance run's one open non-blocking §51 item is exactly "a DIRECT on_off confirm (the bulb was never off when turn_on arrived)" — the S31 closes it with a mains-powered, always-listening relay (§1.4, §1.6). It is also the first mains **router** added since the Hue (mesh-topology effect worth recording at join time).
3. **Twin-signal watch items:** §3 (04P: IAS zone status + advertised device-to-device "local linkage") and §4 (01P: press events as OnOff *client commands*) both carry dual-path or command-shaped signaling questions that decide what the ingestion pipeline must absorb. Each dossier's confirmation section (§1.4/§2.4/§3.4/§4.5) states the honest expectation shape; §6 carries the residual unknowns.
4. **Sleepy-interview discipline generalizes:** 02P/04P/01P are battery sleepy end devices — interview and Configure-Reporting ride the post-announce awake window; expect honest degraded postures (TIMEOUT class) on some legs, per the 0.3 RPT anchor.

---

## 1. SONOFF S31 Lite zb — smart plug (on/off, NO power monitoring)

### 1.1 Identity as an interview will see it

- **Basic-cluster identity → MatchCriteria:** manufacturerName=**`SONOFF`**, modelIdentifier=**`S31 Lite zb`** (with the space — the z2m match key is `zigbeeModel: ["S31 Lite zb"]`; z2m's *catalog* name "S31ZB" is a z2m-side alias, NOT the on-wire string). Corroborated by a REAL machine interview capture: `"manufacturer": "SONOFF", "model": "S31 Lite zb"` in the zigpy/zha test corpus — https://raw.githubusercontent.com/zigpy/zha/dev/tests/data/devices/sonoff-s31-lite-zb.json — and the SmartThings DTH fingerprint `manufacturer: "SONOFF", model: "S31 Lite zb"`. Profile key = **`("SONOFF", "S31 Lite zb")`** `[REF]` — note this is the ONE Wave-2 device whose manufacturer string is `SONOFF`, not `eWeLink`. Verify at interview `[CONFIRM-ON-BENCH]`.
- **Mains ROUTER** (node descriptor: `logical_type: 1`, power source "Mains" — zha capture). First router added to the bench since the Hue — record mesh/topology effects at join. `[REF]`
- **NO power monitoring** (the Lite): z2m exposes `switch (state)` only — https://www.zigbee2mqtt.io/devices/S31ZB.html — and the capture shows no ElectricalMeasurement/Metering clusters. **Corpus-README reconcile pointer:** the index row labels this archetype "Smart plug (energy)" — the Lite has NO energy surface; the hub corrects the row at corpus-entry time (write isolation keeps this return's hands off it). `[REF]`
- **No ZHA quirk** (`quirk_applied: false`, plain `zigpy.device.Device`) — clean standard-ZCL surface. `[REF]`
- manufacturerCode, firmware/dateCode `[CONFIRM-ON-BENCH]`.

### 1.2 Interview expectations — including the ZLL-profile flag (the S31's headline)

Real capture (zha test corpus, machine-recorded): **EP1, profile `0xC05E` (ZLL, 49246), device type `0x0010` (ON_OFF_PLUGIN_UNIT)** — in: `genBasic 0x0000`, `genIdentify 0x0003`, `genGroups 0x0004`, `genScenes 0x0005`, `genOnOff 0x0006` · out: `0x0000` (Basic client — odd but captured). **No OTA cluster, no manufacturer-specific clusters.** `[REF]`

- **CONFLICT (both quoted, report-both):** the SmartThings DTH fingerprint hand-writes `profileId: "0104"` for the same cluster set. The machine capture (0xC05E) is the stronger evidence and is independently corroborated by behavior: the S31 Lite zb joins Philips Hue v1 bridges as a "light" (HA carries a model-string special case — `self.is_s31litezb = light.modelid == "S31 Lite zb"`, `homeassistant/components/hue/v1/light.py:363`; changelog "Fix Hue SONOFF S31 Lite zb plug", core-2022.6) — ZLL-profile behavior. Firmware variance across units is possible. **The profile field is `[CONFIRM-ON-BENCH]` before any fingerprint ships.**
- **PRE-MONDAY CODE-READ FLAG (hub):** every shipped fingerprint so far carries `"profileId": "0x0104"`, and the Hue's non-HA endpoint (Green Power, EP242) is *ignored* by the pipeline. If the interview or entity pipeline gates on profile `0x0104` anywhere, the S31's ONLY application endpoint could be skipped → adopted-but-entityless. Not asserted about the code (unread from this lane) — named as the FIRST thing to verify at source before authoring this profile. The classification fallback is also in play: device type `0x0010` is absent from Doc 08 §3.10's table, so classification falls to the cluster rule "OnOff server without LevelControl ⇒ `switch`" — fine, but note Doc 02 also has a `plug` entity type; whether the profile should pin `plug` is a hub taste call (AMD-44 legality: `plug` is PRIMARY-only).
- Interview is otherwise the easy one of the wave: mains router, always listening, no sleepy discipline, five standard clusters.

### 1.3 Reporting-configuration expectations

- **z2m ships (INFERENCE from defaults; the S31ZB `extend:` line itself was not retrievable §6.1-b):** modern `onOff()` with `configureReporting: true` ⇒ `genOnOff/onOff` reporting **min `0` / max `65000` / change `1`** (verbatim: `setupAttributes(… "genOnOff", [{attribute: "onOff", min: "MIN", max: "MAX", change: 1}])` + `TIME_LOOKUP {MAX: 65000, … MIN: 0}`, `src/lib/modernExtend.ts` — https://raw.githubusercontent.com/Koenkk/zigbee-herdsman-converters/master/src/lib/modernExtend.ts). `[REF]`+flag
- **Platform comparison:** Doc 08 §3.7 `OnOff onOff 0/3600/discrete` — same min/on-change posture, tighter max (a keepalive report at least hourly vs z2m's ~18 h). No profile override needed; the tighter max is availability-friendly for a router.
- **powerOnBehavior:** z2m's `onOff()` defaults `powerOnBehavior = true` yet the S31ZB page exposes NO `power_on_behavior` — INFERENCE: the definition disables it, i.e. **StartUpOnOff attr support is doubtful**; treat power-on state as uncharacterized `[CONFIRM-ON-BENCH]` (matters for the Shelly-driven wall-power scenarios: after a power cycle, does the relay restore ON, OFF, or last?). §6.1-c.
- **Report-on-local-toggle** (physical button → report): NOT FOUND in sources; expected from on-change reporting; `[CONFIRM-ON-BENCH]` (§1.6 seed 3).

### 1.4 Confirmation characterization (the AMD-97 lens) — the wave's ONE confirmable device

The S31 closes the acceptance run's open non-blocking §51 item — "a DIRECT on_off confirm (the bulb was never off when turn_on arrived)" (bench acceptance record) — with a mains relay that is always listening. Draft `confirmation[]` (values pending bench; shape = the shipped Hue on_off entry):

```json
{
  "capability": "on_off",
  "confirmationMode": "EXACT_MATCH",
  "authoritativeAttribute": "OnOff/0x0000",
  "reportsAuthoritative": "VERIFIED_REPORTS",
  "reportingPosture": "ON_CHANGE",
  "confirmability": "CONFIRMABLE",
  "recommendedTimeoutMs": 5000,
  "degradeRule": ["NO_REPORT_TIMEOUT_TO_UNCONFIRMED", "NACK_TO_FAILED", "CONFIRM_FROM_CACHE_OR_READBACK"],
  "notes": "latency envelope [CONFIRM-ON-BENCH] — no community measurement found; expect ≤ the Hue's measured 293–701 ms (mains relay, no fade transients); no-change commands ⇒ honest timeout class; duplicate-transaction reports community-documented (z2m #3904)"
}
```

- **Honest expectation shape:** `turn_on`/`turn_off`/`toggle` → relay actuates → on-change `onOff` report → `state_confirmed` (EXACT_MATCH, discrete — no tolerance band, no transients: the cleanest confirm leg the platform will have). No-change commands produce no report ⇒ the honest-timeout class, now provable on a DISCRETE capability (the Hue proved it on brightness/level).
- **Duplicate-report watch:** "S31ZB … multiple messages generated per event" — https://github.com/Koenkk/zigbee2mqtt/issues/3904 (body unfetched §6.1-d; z2m's library carries `skipDuplicateTransaction` machinery consistent with the class). If our unit double-reports, the assertion class is twin-absorption (exactly one `state_changed` per edge), and the ledger must not double-verdict — same absorption the IAS twins proved, different mechanism. `[REF]`-title+flag
- Groups/Scenes clusters present but out of MVP scope (Doc 08 §3.10 future) — expect `tolerate-unknown` silence, not warnings.

### 1.5 Known firmware variance + failure modes (titles search-verified; bodies unfetched — §6.1-d)

- **Configure-reporting failures on a z2m release:** "Unable to Configure/Reconfigure Sonoff Plugs (S31ZB) in 1.35" — https://github.com/Koenkk/zigbee2mqtt/issues/20618. If OUR configure hits non-SUCCESS postures on a mains router, that is signal (the sleepy excuse doesn't apply here).
- **Duplicate messages per event:** #3904 (above) — the §1.4 watch.
- **Router-quality concerns (Hubitat community):** "Zigbee Routing with Sonoff S31 Lite appears to be bad" — https://community.hubitat.com/t/zigbee-routing-with-sonoff-s31-lite-appears-to-be-bad/91985; "Sonoff S31 Lite (Zigbee) very chatty - is this a problem?" — https://community.hubitat.com/t/sonoff-s31-lite-zigbee-very-chatty-is-this-a-problem/101320. Watch: once it joins, OTHER devices may route through it — if the 03P/Hue behavior shifts post-join, check the topology before blaming firmware (the corpus records the mesh effect).
- **Pairing complaints:** https://community.hubitat.com/t/sonoff-s31-lite-zigbee-smart-plug-us-not-pairing/88569; "Stopped working suddenly" #19510 (linkage to this model unconfirmed).
- **The Hue-bridge/ZLL quirk** (§1.2) is itself the documented firmware-personality headline.

### 1.6 Bench-scenario seeds (SCENARIO_FORMAT v0 idiom)

1. **`s31-command-confirm-direct-onoff`** (AUTO; the brief's named leg — "the leg the Hue could never give us") — precondition: adopted, relay OFF. Stimulus: `api: {method: POST, path: /api/v1/…turn_on}`. Positive: `state_confirmed` for on_off `within:` the corpus envelope (measured at first bench session); API state `on=true`; then the mirror leg OFF. Forbidden: `command_confirmation_timed_out` for these commands, `reporting_ack_lies`. Closes the §51 open item on the record.
2. **`s31-no-change-honesty-onoff`** (AUTO) — turn_on on an already-ON relay ⇒ the honest `command_confirmation_timed_out` (or the no-change explanation once EXPLAIN-PUSH lands), **zero** `state_confirmed`, state unchanged. The never-false-CONFIRMED regression on a DISCRETE EXACT_MATCH capability — composes with the B1 seed `timeout-honesty-no-change` (which runs on the Hue's TOLERANCE legs).
3. **`s31-local-toggle-device-initiated`** (OPERATOR) — "Press the plug's physical button ONCE, HANDS OFF." Positive: exactly one `state_changed` transition (PHYSICAL-origin class, Doc 08 §7) with **zero** command dispatch and zero verdicts (nothing was pending); duplicate raw reports recorded if seen (#3904 characterization). Also the free probe for §1.3's report-on-local-toggle `[CONFIRM-ON-BENCH]`.

---

## 2. SONOFF SNZB-02P — temperature/humidity sensor

### 2.1 Identity as an interview will see it

- **Basic-cluster identity → MatchCriteria:** manufacturerName=**`eWeLink`**, modelIdentifier=**`SNZB-02P`** — REAL machine capture: `"manufacturer": "eWeLink", "model": "SNZB-02P"` (zigpy/zha test corpus — https://raw.githubusercontent.com/zigpy/zha/dev/tests/data/devices/ewelink-snzb-02p-0x00002100.json). z2m matches `zigbeeModel: ["SNZB-02P"]`, catalogs vendor "SONOFF" (branding vs on-wire manufacturer differ — the exact class z2m tracked as "[Wrong device]: Sonoff SNZB-02P vs eWeLink", https://github.com/Koenkk/zigbee2mqtt/issues/20734, body unfetched). Profile key = **`("eWeLink", "SNZB-02P")`** `[REF]`; whether ANY units report `SONOFF` instead is unknown (§6.2-c) `[CONFIRM-ON-BENCH]`.
- **Sleepy battery end device:** node descriptor `logical_type: 2`, `mac_capability_flags: 128` (RxOnWhenIdle=0 — INFERENCE from the standard capability-bit decode); battery **1× CR2477**; OTA supported — z2m page https://www.zigbee2mqtt.io/devices/SNZB-02P.html. `[REF]`
- **Firmware provenance of the capture:** file version `0x2100` (8448) — the zha corpus keys captures per-firmware, a hint that behavior varies by firmware; record OUR unit's version at interview `[CONFIRM-ON-BENCH]`. `[REF]`
- No quirk applied in the capture (plain `zigpy.device.Device`); a ZHA quirk has since merged (offset support — §2.5). manufacturerCode/dateCode `[CONFIRM-ON-BENCH]`.

### 2.2 Interview expectations

Real capture (machine-recorded): **EP1, profile `0x0104`, device type `0x0302` (TEMPERATURE_SENSOR)** — in: `genBasic 0x0000`, `genPowerCfg 0x0001`, `genIdentify 0x0003`, **`genPollCtrl 0x0020`**, **`msTemperatureMeasurement 0x0402`**, **`msRelativeHumidity 0x0405`**, **`0xFC11`**, **`0xFC57`** · out: `genOta 0x0019`. `[REF]`

- Device type `0x0302` hits Doc 08 §3.10's exact row "Temperature Sensor (0x0302) → `sensor`"; the cluster set hits §3.5's TemperatureMeasurement + RelativeHumidity + PowerConfiguration rows cleanly. Expected mapping: `sensor` entity with `temperature_measurement` + `humidity_measurement` + `battery` — **the cleanest Doc-02/08 MATCH candidate of the wave** (the corpus entry computes the verdict; nothing visible blocks it). Minor pointer for the corpus entry: Doc 08 §3.5's capability column writes `temperature`/`humidity` shorthand where Doc 02 §3.6 defines `temperature_measurement`/`humidity_measurement` — same contract, naming drift only.
- **The 03P calibration confirmed:** PollControl + BOTH `0xFC11` and `0xFC57` on real silicon — the residual-cluster classes §0.2 predicts. Expect `tolerate-unknown` handling; the custom clusters carry SONOFF's calibration-offset attributes (§2.5).
- **Sleepy interview discipline:** interview + Configure-Reporting ride the post-announce awake window; keep-awake guidance for this unit was NOT retrievable (§6.2-d) — the P-family norm (wake presses during long exchanges) applies; pairing hold `[CONFIRM-ON-BENCH]`.

### 2.3 Reporting-configuration expectations (the ALIVE-anchor device)

- **z2m ships (modernExtend defaults, verbatim; application to the 02P is INFERENCE — its `extend:` list was not retrievable §6.2-b):** temperature `min 10 s / max 3600 s / change 100` (= **1.00 °C** in ZCL 0.01 units); humidity `min 10 s / max 3600 s / change 100` (= **1.00 %**); battery `min 3600 s / max 65000 s / change 10` (= **5 %** in 0.5-unit steps) — https://raw.githubusercontent.com/Koenkk/zigbee-herdsman-converters/master/src/lib/modernExtend.ts. `[REF]`+flag
- **Platform comparison (the one real delta of the wave):** Doc 08 §3.7 defaults — temperature `10/3600/10` (**0.1 °C**), humidity `10/3600/100` (1 %), battery `3600/62000/0`. **Our temperature reportable-change is 10× more sensitive than z2m's default** (0.1 °C vs 1.0 °C): more reports, better bench fidelity, more battery drain. Hub call at profile time: keep 0.1 °C for the bench era (fidelity feeds corpus v2 latency/cadence data) and revisit for field defaults — or match z2m's 1.0 °C. Flag, not a defect. Battery change `0` (ours) vs `10` (z2m): ours reports every max-interval regardless — availability-friendly.
- **SONOFF's official cadence (gap-fill fetched, product page):** "If there is a change in value, the shortest reporting interval is 5 seconds. If no change occurs within an hour, the device will report at least once every 60 minutes." Accuracy "±0.2°C / ±0.4°F" and "±2% RH"; range −10~60 °C / 5–95 %RH non-condensing; CR2477 "up to 4 years of battery life under typical use conditions" — https://sonoff.tech/en-us/products/sonoff-zigbee-temperature-and-humidity-sensor-snzb-02p `[REF]`. The firmware-native shape (≈5 s min / 60 min max) is CONSISTENT with the z2m-configured 10/3600 posture — but the page states **no change THRESHOLD** (the ±X °C trigger), so whether firmware honors a configured 0.1 °C reportable-change remains `[CONFIRM-ON-BENCH]` (the §2.6-3 stimulus scenario measures it; `help.sonoff.tech` is robots-disallowed to this session's fetcher — §6.2-a).
- **Expected stimulus:** temp/humidity reports on change-threshold or max-interval; battery on cadence. This device is the wave's **availability-ALIVE anchor**: a healthy 02P should emit SOMETHING at least hourly (max-interval 3600), which is exactly the signal the `battery_timeout_hours`/ALIVE wiring consumes.

### 2.4 Confirmation characterization (the AMD-97 lens)

**No actuating capabilities ⇒ `confirmation: []`** (z2m exposes are read-only measurements; the capture shows no actuating server cluster; the only inbound interactions are Identify/OTA/PollControl service traffic). Honest expectation shape: measurement reports on the §2.3 cadences, nothing issuable, nothing confirmable — the entity's truth is anchored entirely by report freshness, which is why the ALIVE-anchor scenarios below are this device's real bench job. Calibration/precision knobs on the z2m page are **coordinator-side options, not device commands** (the device-side offset attributes live on the custom cluster — §2.5; V1: tolerate-unknown, unsurfaced).

Draft profile stub: `exact_model ("eWeLink","SNZB-02P")` + fingerprint from the zha capture (EP1 `0x0104`/`0x0302`, in `["0x0000","0x0001","0x0003","0x0020","0x0402","0x0405","0xFC11","0xFC57"]`, out `["0x0019"]`), `category STANDARD_ZCL`, `confirmation: []` — re-derive the fingerprint from OUR interview before shipping (the LCA006→LCA017 lesson).

### 2.5 Known firmware variance + failure modes (titles search-verified; bodies unfetched — §6.2-e)

- **Availability flapping with a 6 h period:** "ZHA SNZB-02P unavailable for 6 hours every 6 hours" — https://community.home-assistant.io/t/zha-snzb-02p-unavailable-for-6-hours-every-6-hours/686475; also "Sonoff SNZB-02P temperature sensors often unavailable" — https://community.home-assistant.io/t/sonoff-snzb-02p-temperature-sensors-often-unavailable/881140. The 6 h signature smells like check-in/poll-control interval interaction — directly relevant to our `battery_timeout_hours` default (25 h clears it, but the pattern is worth recognizing on sight).
- **Configure-Reporting friction on this sleepy device:** "Error editing reporting values for SonOff SNZB-02P" — https://github.com/Koenkk/zigbee2mqtt/issues/27919. Expect the honest TIMEOUT posture class if exchanges miss the awake window (the 03P 2/3 precedent); wake presses during the drive are the operator mitigation.
- **Calibration drift/precision complaints:** "SNZB-02P temperature and humidity calibration error" — https://github.com/koenkk/zigbee2mqtt/issues/28493; the ZHA quirk PR adding device-side offsets: "Add temperature and humidity offset to Sonoff SNZB-02P" — https://github.com/zigpy/zha-device-handlers/pull/4263 (offset attrs live on the SONOFF custom cluster; attribute IDs unverified — §6.2-f). V1 posture: record raw values; no offset writes.
- **Ecosystem support gaps (context only):** deCONZ pairing issue #7903, Domoticz not-supported thread, HA core #149502, OTA-tab absence #22889 (URLs in §7).
- **Battery-stuck/sudden-death: NOT FOUND for the 02P specifically** — the known reports are SNZB-02/-02D (different models); do not transfer the claim. Honest unknown.

### 2.6 Bench-scenario seeds (SCENARIO_FORMAT v0 idiom)

1. **`snzb02p-report-cadence-alive-anchor`** (AUTO, long-horizon; the brief's named leg) — precondition: adopted, reporting driven. Positive: ≥1 `state_reported` for temperature or humidity `within: 3700s` (max-interval + slack) AND ≥1 battery report within its window; availability never UNAVAILABLE across the run (the ALIVE-anchor assertion — `requires:` the availability wiring; author now, gate on the WU). Forbidden: `device_proposed`.
2. **`snzb02p-reporting-verify-posture`** (OPERATOR at join; the honest-degrade leg) — during the adoption drive, operator keeps the device awake (wake presses). Positive: `zigbee.reporting_configured: … clusters=N verified=V degraded=D` with the counts RECORDED (not asserted maximal — the 2/3-class sleepy posture is honest, not a failure). Forbidden: `reporting_ack_lies`.
3. **`snzb02p-temp-delta-stimulus`** (OPERATOR) — "Hold the sensor in your hand for 60 s, then HANDS OFF." Positive: a temperature `state_reported` with rising value within the configured min-interval + slack; records whether the configured reportable-change (0.1 °C vs 1.0 °C — §2.3) actually governs the firmware's emission. The cheap change-threshold characterization, no thermal rig needed.

---

## 3. SONOFF SNZB-04P — door/window contact sensor

### 3.1 Identity as an interview will see it

- **Basic-cluster identity → MatchCriteria:** manufacturerName=**`eWeLink`**, modelIdentifier=**`SNZB-04P`** — the ZHA quirk keys on exactly this pair: `QuirkBuilder("eWeLink", "SNZB-04P")` (`zhaquirks/sonoff/snzb04p.py` — https://raw.githubusercontent.com/zigpy/zha-device-handlers/dev/zhaquirks/sonoff/snzb04p.py); z2m matches `zigbeeModel: ["SNZB-04P"]` / `model: "SNZB-04P"` (`src/devices/sonoff.ts` via grep.app index of Koenkk/zigbee-herdsman-converters). Cross-ecosystem corroboration: SmartThings fingerprints `{ mfr = "eWeLink", model = "SNZB-04P" }`. Profile key = **`("eWeLink", "SNZB-04P")`** `[REF]` — same manufacturer string as the bench-captured SNZB-03P, so HIGH confidence, but the exact-model match still verifies at interview `[CONFIRM-ON-BENCH]`.
- **ZCL device type:** `0x0402` (1026, **IAS Zone**) — from the quirk's embedded SimpleDescriptor (§3.2). This hits Doc 08 §3.10's exact classification row "IAS Zone (0x0402) → per zone type: `binary_sensor` or `sensor`". `[REF]`
- **Vendor page identity:** z2m device page: Vendor "SONOFF", Model "SNZB-04P", "Contact sensor"; exposes `contact, battery_low, tamper, battery, voltage`; OTA supported — https://www.zigbee2mqtt.io/devices/SNZB-04P.html `[REF]`
- **Power:** battery sleepy end device (PollControl-bearing battery sensor — §3.2). **Battery TYPE unverified** (SONOFF product page unfetched this session — §6.3-d; do not assume CR2032). manufacturerCode + firmware/dateCode `[CONFIRM-ON-BENCH]`.
- **Disambiguation trap:** a successor **`SNZB-04PR2`** ("SenseGuard DW Gen2") exists as a distinct modelIdentifier (`zigbeeModel: ["SNZB-04PR2"]` in sonoff.ts). Exact-model matching keeps them separate; do not fold their evidence together. `[REF]`

### 3.2 Interview expectations

The strongest pre-silicon signature available for any Wave-2 device — the ZHA quirk carries a verbatim SimpleDescriptor capture (https://raw.githubusercontent.com/zigpy/zha-device-handlers/dev/zhaquirks/sonoff/snzb04p.py):

```
<SimpleDescriptor endpoint=1 profile=260 device_type=1026
 input_clusters=[0, 1, 3, 32, 1280, 64529, 64567]
 output_clusters=[3, 6, 25]>
```

Decoded (standard ZCL hex; decode is INFERENCE on the quoted dump): **EP1**, profile `0x0104`, device type `0x0402` — **in:** `genBasic 0x0000`, `genPowerCfg 0x0001`, `genIdentify 0x0003`, **`genPollCtrl 0x0020`**, **`ssIasZone 0x0500`**, **`0xFC11`** (SONOFF custom, 64529), **`0xFC57`** (64567) · **out:** `genIdentify 0x0003`, **`genOnOff 0x0006` (client!)**, `genOta 0x0019`. `[REF]`

**Second, independent machine capture corroborates byte-for-byte** (parent lane's gap-fill pass): the zigpy/zha test-corpus dump at firmware `0x2200` records the identical map (EP1, profile 260, device type IAS_ZONE 1026, in `[0x0000, 0x0001, 0x0003, 0x0020, 0x0500, 0xfc11, 0xfc57]`, out `[0x0003, 0x0006, 0x0019]`), quirk applied `zhaquirks.sonoff.snzb04p:(eWeLink / SNZB-04P)`, **cached IAS `zoneType = 21`** (the ZCL Contact-Switch class — the §3.2 expectation now evidence-backed), battery cache 3.0 V / 100 % — https://raw.githubusercontent.com/zigpy/zha/dev/tests/data/devices/ewelink-snzb-04p-0x00002200.json `[REF]`. Raw dump on OUR silicon `[CONFIRM-ON-BENCH]`.

- **The 03P-calibration cross-check passes:** PollControl + 0xFC57 — the two clusters desk research MISSED on the 03P — are already in this signature, and 0xFC11 appears here (04P) where the 03P silicon showed 0xFC57 only. Expect the family pattern; expect no surprise if silicon adds/varies a residual cluster.
- **Sleepy interview:** battery + PollControl ⇒ interview and Configure-Reporting ride the post-announce awake window (Doc 08 §3.4; the 03P precedent). Pairing/wake procedure specifics unfetched (§6.3-d) — the P-family norm is a ~5 s button hold `[CONFIRM-ON-BENCH]`.
- **IAS enrollment:** Doc 08 §3.12 (CIE write ATTEMPTED, never a gate) applies; the platform's enroll path is already silicon-proven on the 03P (`ias_zone_enrolled endpoint=1 zoneId=0`, bench acceptance record). Whether the 04P *requires* enrollment before reporting zone status is **unestablished either way** in fetched sources (§6.3-c); z2m's modern `iasZoneAlarm()` extend is characterized (reader-model, not verbatim) as NOT enrolling — meaning z2m field reports may reflect an unenrolled posture. Zone type: the zha capture caches **`zoneType = 21`** (ZCL Contact Switch) for a real unit (§3.2) — Doc 08 §3.5's zone-type→capability selection lands on **`contact`**; our interview re-reads attr `0x0001` `[CONFIRM-ON-BENCH]`.

### 3.3 Reporting-configuration expectations

- **z2m's exact configure block for the 04P was NOT retrieved** (the sonoff.ts definition sits at ~lines 6513–6533, beyond the fetch window this session — §6.3-a). What IS sourced verbatim (gap-fill fetch of `src/lib/ewelink.ts`): the eWeLink battery helper the P-family uses — `// 3600/7200 prevents disconnect` → `battery({voltage: true, voltageReporting: true, percentageReportingConfig: {min: 3600, max: 7200, change: 2}, voltageReportingConfig: {min: 3600, max: 7200, change: 100}})` — https://raw.githubusercontent.com/Koenkk/zigbee-herdsman-converters/master/src/lib/ewelink.ts. **Battery % reporting min `3600 s` / max `7200 s` / change `2` (= 1 %), plus voltage reporting** — deliberately tighter than the stock `m.battery()` default (`{min: "1_HOUR", max: "MAX"(65000), change: 10}`, `src/lib/modernExtend.ts`) so sleepy eWeLink devices are never silent past ~2 h. That the 04P block uses `ewelinkBattery` remains INFERENCE — but the 04P page exposes **voltage**, which the stock default omits (`voltage = false`), so the eWeLink-tuned shape is the strongly indicated one. `[REF]`+flag
- **Platform comparison:** Doc 08 §3.7 default `PowerConfiguration batteryPercentageRemaining 3600/62000/0` is compatible with either z2m posture; if silicon shows the 7200-max eWeLink tuning matters for availability, that is a **profile `reporting_overrides` candidate**, not a code change. IAS `zoneStatus` is event-driven (ZoneStatusChangeNotification), not Configure-Reporting-driven — expect the reporting drive to cover PowerCfg (+ possibly nothing else standard), and a 1/N-verified posture to be NORMAL here, not degradation.
- **Tamper reporting (ZHA precedent):** the quirk configures the custom `0xFC11` attr `tamper` (`0x2000`, Bool) with `ReportingConfig(min_interval=0, max_interval=900, reportable_change=1)` — evidence the custom attribute is report-capable. `[REF]` V1 relevance: none (custom cluster ⇒ tolerate-unknown), recorded for the corpus.
- **Expected report stimulus:** contact edge → IAS `ZoneStatusChangeNotification` (both edges — z2m models `contact` as a two-state boolean: "Indicates whether the device is opened or closed", raw doc — INFERENCE that both edges notify; no explicit both-edges quote exists §6.3-b); battery on the configured cadence; tamper on case-open (custom path).

### 3.4 Confirmation characterization (the AMD-97 lens)

**No actuating capabilities ⇒ `confirmation: []`** (the SNZB-03P shipped-profile precedent: empty array = nothing issuable, distinct from UNCONFIRMABLE-with-commands). The honest expectation shape:

- **What it reports and on what stimulus:** `contact.open` (bool) on each physical edge via IAS zone status; `battery` on the configured cadence; `tamper` via custom `0xFC11` (V1: unsurfaced, tolerate-unknown expected — the `characterization_unmatched … skipped (tolerate-unknown)` class from the Hue `effect` precedent).
- **THE TWIN-PATH WATCH (the 03P class, different mechanism):** the signature carries **`genOnOff` as a CLIENT (output) cluster** — a pure reporter needs no OnOff client — and the ZHA quirk explicitly suppresses the phantom entity it would otherwise create (`.prevent_default_entity_creation(endpoint_id=1, cluster_id=OnOff.cluster_id)`, quirk source). INFERENCE (flagged, unproven by traffic capture §6.3-b): the 04P can SEND on/off commands to bound targets — SONOFF's advertised device-to-device linkage — so one physical edge could emit **IAS notification + OnOff command twins** if anything binds that cluster. **REC for the hub's profile: do NOT bind the 04P's OnOff client cluster to the coordinator in V1** — don't invite a second signal path the ingestion would need to absorb; characterize it deliberately on the bench instead (§3.6 seed 3). Which command per edge (on? off? toggle?), and whether anything emits with no binding: `[CONFIRM-ON-BENCH]`.
- **Draft profile stub** (hub authors; values pending bench):

```json
{
  "profileId": "sonoff_snzb_04p",
  "matches": [
    {"type": "exact_model", "manufacturer": "eWeLink", "model": "SNZB-04P"},
    {"type": "fingerprint", "manufacturer": "eWeLink", "model": "SNZB-04P",
     "endpoints": [{"profileId": "0x0104", "deviceType": "0x0402",
       "inClusters": ["0x0000","0x0001","0x0003","0x0020","0x0500","0xFC11","0xFC57"],
       "outClusters": ["0x0003","0x0006","0x0019"]}]}
  ],
  "category": "STANDARD_ZCL",
  "confirmation": []
}
```
(fingerprint = the quirk capture; re-derive from OUR interview before shipping — the Hue LCA006→LCA017 lesson.)

### 3.5 Known firmware variance + failure modes (community; titles search-verified, bodies mostly unfetched — §6.3-e)

- **Tamper latching:** "Sonoff SNZB-04P: Can't reset tamper" — https://github.com/Koenkk/zigbee2mqtt/issues/25069. Watch: a stuck-true custom-cluster bool; V1-invisible but corpus-relevant.
- **Availability drop-offs across BOTH generations:** "[BUG] Sonoff SNZB-04P and SNZB-04 (DS01) becoming unavailable" — https://github.com/zigpy/zha-device-handlers/issues/4222; predecessor pattern quantified: "Sonoff SNZB-04 devices leave network 256 minutes after last activity" — https://github.com/Koenkk/zigbee2mqtt/issues/15027. Feeds the availability-ALIVE work: battery_timeout must comfortably exceed the real check-in/report cadence.
- **Pairing/interview failures:** "Fail to pair SNZB-04P." — https://github.com/Koenkk/zigbee2mqtt/issues/25968; "SNZB-04P interview failed" — https://github.com/koenkk/zigbee2mqtt/issues/28524. Sleepy-interview class; the wake discipline matters.
- **Basic-cluster misreports:** "Sonoff SNZB-04P doesn't report any power source" — https://github.com/Koenkk/zigbee2mqtt/issues/24025 (family trait — same class as the 01P's powerSource issues §4.6): **do not key any platform logic on Basic `powerSource`**; the profile knows the device is battery.
- HA-community availability threads (unfetched bodies): "Sonoff SNZB-04P strangeness" · "SNZB-04P problem" · "Sonoff door sensor goes unavailable" (URLs in §7).

### 3.6 Bench-scenario seeds (SCENARIO_FORMAT v0 idiom)

1. **`contact-both-edges`** (OPERATOR; the brief's named leg) — precondition: adopted, reporting driven. Operator line: "Open the contact ONCE, wait 5 s, close it ONCE, then HANDS OFF." Positive: `state_reported`/API state `contact.open=true` then `=false`, in order, each `within: 10s` of its edge; forbidden: `device_proposed`, any second transition per edge (`exactly:` semantics scoped to the run window — the twin-absorption assertion). Bundle always.
2. **`contact-battery-alive-anchor`** (AUTO, long-horizon) — positive: ≥1 battery report within the configured max-interval window AND availability never UNAVAILABLE across it (blocked on availability-ALIVE landing; author now, `requires:` the wiring).
3. **`contact-onoff-linkage-characterization`** (OPERATOR, bench-only, one-time) — deliberately bind the 04P's OnOff client cluster to the coordinator, actuate both edges, record whether on/off/toggle commands arrive and which per edge; then UNBIND. Output feeds the corpus + the twin-absorption posture; not a regression scenario.

---

## 4. SONOFF SNZB-01P — wireless button

### 4.1 Identity as an interview will see it

- **Basic-cluster identity → MatchCriteria:** manufacturerName=**`eWeLink`**, modelIdentifier=**`SNZB-01P`** — ZHA: `QuirkBuilder("eWeLink", "WB01") … .also_applies_to("eWeLink", "SNZB-01P")` (`zhaquirks/sonoff/button.py` — https://raw.githubusercontent.com/zigpy/zha-device-handlers/dev/zhaquirks/sonoff/button.py); z2m: `zigbeeModel: ["SNZB-01P"], model: "SNZB-01P", vendor: "SONOFF", description: "Wireless button"` (sonoff.ts ~6410–6414 via grep.app); SmartThings: `{ mfr = "eWeLink", model = "SNZB-01P" }`. Profile key = **`("eWeLink", "SNZB-01P")`** `[REF]`; verify at interview `[CONFIRM-ON-BENCH]`.
- **Predecessor trap:** the old SNZB-01 reports modelIdentifier **`WB01`** (the quirk's primary key) — different string, same behavior family. Exact-model matching separates them cleanly. `[REF]`
- **Battery:** **1× CR2477**; OTA supported — z2m device page https://www.zigbee2mqtt.io/devices/SNZB-01P.html `[REF]`
- **Sleepy end device (documented):** "sleeps to preserve energy when it's not actively used"; "Press its button to keep it awake and allow interactions" — z2m raw doc https://raw.githubusercontent.com/Koenkk/zigbee2mqtt.io/master/docs/devices/SNZB-01P.md `[REF]`
- ZCL device type: **NOT FOUND pre-silicon** (§4.2) `[CONFIRM-ON-BENCH]`.

### 4.2 Interview expectations (closed by the parent lane's gap-fill pass — two machine captures)

Real captures (zigpy/zha test corpus, machine-recorded, **byte-identical endpoint maps across firmwares `0x2000` and `0x2200`**): **EP1, profile `0x0104` (260), device type `0x0000` (ON_OFF_SWITCH)** — in: `genBasic 0x0000`, `genPowerCfg 0x0001`, `genIdentify 0x0003`, **`genPollCtrl 0x0020`**, **`0xFC57`** · out: `genIdentify 0x0003`, **`genOnOff 0x0006` (client — the §4.3 event carrier)**, `genOta 0x0019`. Quirk applied: `zhaquirks.sonoff.button:(eWeLink / WB01)` — the shared-quirk identity of §4.1 confirmed in the field. Battery cache: 3.1 V / 100 %. — https://raw.githubusercontent.com/zigpy/zha/dev/tests/data/devices/ewelink-snzb-01p-0x00002200.json (and `…-0x00002000.json`) `[REF]`

- **Precision detail:** the 01P carries `0xFC57` but **NOT `0xFC11`** — unlike its 02P/04P siblings. Expect one custom cluster, not two.
- **Classification consequence (feeds §4.5):** device type `0x0000` (ON_OFF_SWITCH — the ZCL "controls-others" type) is absent from Doc 08 §3.10's table, and the device has **no OnOff SERVER**, so the cluster fallback ("OnOff server without LevelControl ⇒ switch") never fires either — classification lands on the battery-only remainder. The interview will succeed; the ENTITY story is the §4.5 gap.
- Sleepy-interview discipline applies (wake presses during interview); pairing = "Press and hold the reset button for 5s" (z2m raw doc, quoted). Raw dump on OUR unit `[CONFIRM-ON-BENCH]`. `[REF]`

### 4.3 The signal path (the brief's critical question — answered cross-stack)

**Press events are OnOff cluster COMMANDS from the device — not MultistateInput, not a custom cluster** (MultistateInput association: NOT FOUND in any searched source):

- **ZHA** (verbatim, quirk source): `device_automation_triggers({(SHORT_PRESS, BUTTON): {COMMAND: COMMAND_TOGGLE}, (DOUBLE_PRESS, BUTTON): {COMMAND: COMMAND_ON}, (LONG_PRESS, BUTTON): {COMMAND: COMMAND_OFF}})` — https://raw.githubusercontent.com/zigpy/zha-device-handlers/dev/zhaquirks/sonoff/button.py `[REF]`
- **z2m (verbatim, the modern-extend the P-family uses — `src/lib/ewelink.ts`, gap-fill fetched):** the converter consumes `cluster: "genOnOff", type: ["commandOn", "commandOff", "commandToggle"]` and maps with the exact lookup `const lookup: KeyValueAny = {commandToggle: "single", commandOn: "double", commandOff: "long"};` — exposing `presets.action(["single", "double", "long"])` — https://raw.githubusercontent.com/Koenkk/zigbee-herdsman-converters/master/src/lib/ewelink.ts (the legacy `fz.ewelink_action` at `src/converters/fromZigbee.ts:1983` is the same shape). The 01P page exposes Action enum `single | double | long` — https://www.zigbee2mqtt.io/devices/SNZB-01P.html `[REF]`
- **Mapping (now FACT by verbatim code, cross-stack consistent with ZHA's trigger table):** single-press → `toggle` · double-press → `on` · long-press → `off`. Bench still verifies all three on OUR unit (one press class per capture) `[CONFIRM-ON-BENCH]`.
- **The binding is load-bearing and z2m creates it (verbatim):** `ewelinkAction`'s configure is `setupConfigureForBinding("genOnOff", "output")` — z2m explicitly **binds the genOnOff OUTPUT cluster to the coordinator** at configure time. Without that binding the presses have no unicast destination. `[REF]`

**Pipeline consequence (flag for the hub):** commands-from-device are a **different ingestion class** than anything Wave-1 exercised (attribute reports + IAS notifications). Two platform questions decide the 01P's viability, both pre-authorable now: (a) does `ZclIngestionUnit` parse incoming genOnOff cluster commands addressed to the coordinator, and (b) can the reporting/binding drive create a **client(output)-cluster binding** (the z2m precedent above — our drive binds clusters for reporting; a command-delivery bind is the same ZDO Bind_req aimed at an output cluster). Neither is a device fact — both are code reads the hub runs before authoring the profile. `[REF]`-grounded flag.

**Binding-behavior CONFLICT (both quoted, unresolved — §6.4-c):** z2m doc: "This button can **not** directly control individual devices or groups (v2.2.0)" (binds accepted, "clicks perform no action") — versus zhaquirks issue title "[BUG] After Power Outage SNZB-01P Binds to Nearest Aqara Smart Plug As a Toggle Device" (https://github.com/zigpy/zha-device-handlers/issues/4574), which implies it CAN drive a bound target on some firmware. Likely firmware-dependent; the bench's seed-3 characterization adjudicates for OUR unit.

### 4.4 Reporting-configuration expectations

The only report-bearing standard cluster is `genPowerCfg` (no measurement clusters; presses are commands, not reports — §4.3). z2m's eWeLink-tuned battery shape (verbatim, `src/lib/ewelink.ts`, §3.3): **battery % min `3600 s` / max `7200 s` / change `2` (= 1 %) + voltage min `3600`/max `7200`/change `100` (mV)** — and the 01P page exposes voltage, indicating the tuned helper over the stock default. `[REF]`+flag (per-device extend list unretrieved — §6.4-b). Platform comparison: Doc 08 §3.7 battery `3600/62000/0` — if availability wants the ≤2 h heartbeat the eWeLink tuning exists for, that is a profile `reporting_overrides` candidate (`"0x0001": {min_interval: 3600, max_interval: 7200}`), not a code change. Expected stimulus: battery on cadence; a press mints NO report. PollControl check-in cadence unknown (§6.4-e) `[CONFIRM-ON-BENCH]`.

### 4.5 Confirmation characterization (the AMD-97 lens)

**No actuating capabilities ⇒ `confirmation: []`.** The honest expectation shape is EVENT-emission, not state: a press produces one OnOff command frame (class per §4.3), battery reports on cadence, and **nothing about a press is confirmable, repeatable-on-query, or state-anchored — there is no attribute to read back; a missed press is silently gone.** That shape is exactly what makes the button the platform's first pure-event device — and it exposes a device-model gap:

**THE BUTTON GAP (escalation candidate ESC-W2-SNZB01P-01 — hub numbers/owns; the ESC-W1-HUE-01 class)**

1. **Doc 02 §3.10's MVP entity-type table has no `button`** (`light · switch · plug · sensor · binary_sensor · energy_meter`; post-MVP reserved list likewise lacks button/scene) and **Doc 02 §3.6 has no press/action capability** in the MVP or post-MVP sets. A press is not representable as canonical state.
2. **Doc 08 §3.10 already references a `button` entity type** — rows "On/Off Light Switch (0x0103) | OnOff (client) | `button`" and "Dimmer Switch (0x0104) | LevelControl (client) | `button`" — an entity type Doc 02 does not define. Cross-doc inconsistency to reconcile whichever way the ruling goes. (Doc 08 §7 also anticipates the event class: "Origin model: PHYSICAL for button presses".)
3. **Trigger-path consequence:** Doc 07's Tier-1 trigger table includes an `event` trigger type ("A specific event type is received…"), but the engine's Tier-1 subscription filter is `state_changed` + `availability_changed` only (Doc 07 §3.2). A press that mints no state change cannot fire an automation through the current subscription without either (a) minting press-as-state (semantic kludge: a `binary_state` pulse or counter — misrepresents an event as state, pollutes the state view, and double/long don't fit) or (b) an AMD-class ruling that defines a press-event representation + widens the trigger surface.
4. **REC (hub's call, before profile authoring):** route as an AMD candidate in the AMD-97/AMD-99 pattern — rule the representation FIRST (button entity type + event-shaped capability, or an explicit V1-scope-out), then author the profile. **Honest V1 fallback if scoped out:** adopt the 01P as a battery-only device (`sensor`/battery + the press events visible in logs but not in the device model), recorded as deliberate scoping — never a silent half-map.

Draft profile stub (fingerprint now authorable from the §4.2 machine captures; re-derive from OUR interview before shipping):

```json
{
  "profileId": "sonoff_snzb_01p",
  "matches": [
    {"type": "exact_model", "manufacturer": "eWeLink", "model": "SNZB-01P"},
    {"type": "fingerprint", "manufacturer": "eWeLink", "model": "SNZB-01P",
     "endpoints": [{"profileId": "0x0104", "deviceType": "0x0000",
       "inClusters": ["0x0000","0x0001","0x0003","0x0020","0xFC57"],
       "outClusters": ["0x0003","0x0006","0x0019"]}]}
  ],
  "category": "STANDARD_ZCL",
  "confirmation": []
}
```
Entity shape pending the ESC ruling.

### 4.6 Known firmware variance + failure modes (titles search-verified; bodies unfetched — §6.4-d)

- **Spontaneous/ineffective binding:** #4574 (power-outage auto-bind, above); "SNZB-01P bind not effective" — https://github.com/Koenkk/zigbee2mqtt/issues/23304; eWeLink forum "SNZB-01P problem with smart switches (M2M, 4CH PRO)". The binding surface is the flakiest part of this device's story — another reason V1 should not depend on it beyond the coordinator binding (if ruling (b) needs one).
- **Basic powerSource misreport (multi-confirmation):** "power source is 'Unknown' … '?' sign instead of a 100 percent charge%" — https://github.com/Koenkk/zigbee2mqtt/issues/22032; also #24007. Same family rule as the 04P: don't trust Basic `powerSource`.
- **Ecosystem action-plumbing breakage (not device firmware, but bench-relevant noise):** "SNZB-01P lost the action entity after 2.0 upgrade" #26047 · "action not showing on Home Assistant" #29963 · ZHA "action/button press not recognized" https://github.com/home-assistant/core/issues/104548 · Hubitat/openHAB single-press-only threads. Read: the EVENT-shaped signal is fragile in every downstream stack — which is precisely the §4.5 representation problem, observed in the wild.
- **Wrong-quirk class (ZHA):** "[BUG] SNZB-01P (eWelink) using wrong quirk?" — https://github.com/zigpy/zha-device-handlers/issues/4394 (shared WB01 quirk + also_applies_to is the mechanism; our exact-model profile keying avoids the class).
- **OTA metadata noise:** z2m reporting phantom updates/wrong versions — https://github.com/Koenkk/zigbee2mqtt/issues/20863.

### 4.7 Bench-scenario seeds (SCENARIO_FORMAT v0 idiom)

1. **`button-press-classes`** (OPERATOR; blocked on the ESC ruling for its assertion surface) — three runs: "ONE single press / ONE double press / ONE ~5 s long press, then HANDS OFF." Positive per run: exactly one press event of the expected class within 10 s (token or API surface per the ruling); forbidden: any second event in-window (`exactly:` + run-window), `device_proposed`.
2. **`button-press-to-automation`** (OPERATOR; the brief's "press-class → automation trigger" — DOUBLE-blocked: ESC ruling + trigger-path (a/b) reads) — a bench automation bound to the press representation fires exactly one Run per press; forbidden: double-runs (the IAS-twin-absorption assertion, event-flavored).
3. **`button-battery-alive-anchor`** (AUTO, long-horizon) — same shape as §3.6-2: battery report within window + availability honesty for a device that is asleep ~100% of the time (the sharpest test of battery_timeout_hours semantics on the bench).

---

## 5. Appendix — the Shelly Plus Plug US (Gen2) stimulus contract for `bench.sh`

### 5.0 Role and rails

2× **Shelly Plus Plug US** (ordered 2026-07-10 with the Rosonway hub; PROJECT_SNAPSHOT v27 beat 3) are **OUT-OF-BAND actuators** — they drive wall power for devices under test (first target: the Hue) and are NOT devices under test. The charter's stimulus-independence rule is the design constraint: *"stimulus never rides the system under test"* (charter §4) — these plugs ride the bench LAN over WiFi and local HTTP RPC, never the Zigbee network, never HomeSynapse. The consumer is the `plug:` stimulus verb of SCENARIO_FORMAT (`- plug: {target: hue-wall, act: off, settle: 5s}`), implemented by `bench.sh` at B1+ and ridden nightly at B3. Everything below is quoted from the official Gen2+ docs (URLs inline) unless tagged INFERENCE; §6.5 carries the residual unknowns.

**One RF-coexistence advisory (INFERENCE, band arithmetic — bench-verify):** the plugs are 2.4 GHz-only WiFi (802.11 b/g/n; official KB) and the bench Zigbee network currently sits on ch20 (≈2450 MHz; acceptance record). WiFi ch11 (2451–2473 MHz) overlaps Zigbee ch20–24; WiFi ch1 (2401–2423 MHz) clears it. Pin the bench SSID to a WiFi channel clear of the live Zigbee channel — the stimulus channel must not degrade the system it stimulates.

### 5.1 The device (identity, and what the driver may assert)

- Model **`SNPL-00116US`**; "Power supply voltage AC: 120 V ±10 %, 60 Hz"; "Max switching current AC: 15 A"; ESP32; 2.4 GHz WiFi; BT 4.2 — official KB: https://kb.shelly.cloud/knowledge-base/shelly-plus-plug-us `[REF]`
- **It meters** ("Power and energy meters: Yes" — KB; the 0.14 device page: "has a built-in power meter to instantaneously measure the power and energy consumed by the channel," https://shelly-api-docs.shelly.cloud/gen2/0.14/Devices/ShellyPlugUS/). Though the plug is not under test, `apower` is a free **positive-evidence channel**: "the Hue socket is actually drawing power" is assertable as `apower > threshold`, which upgrades absent-device scenarios from "we turned the plug off" to "the lamp was provably unpowered/powered." `[REF]` + INFERENCE
- Identity check at provision + per-suite-run: `Shelly.GetDeviceInfo` returns `id`, `mac`, `model`, `gen`, `fw_id`, `ver`, `app`, `auth_en` (documented example shows the key set — https://shelly-api-docs.shelly.cloud/gen2/ComponentsAndServices/Shelly/). Gate the driver on `model=="SNPL-00116US"` && `gen==2`. **The `app`/`id` strings for this model ("PlusPlugUS"/"shellyplusplugus-<mac>") are UNVERIFIED** — no fetched source shows a real dump; capture them at provisioning (§6.5-b). `[REF]`/`[CONFIRM-ON-BENCH]`
- Generation note: there is **no "Plug US Gen3"** in the official docs tree; the US plug's successor is Gen4 (`ShellyPlugUSG4`, adds Matter/Zigbee — https://shelly-api-docs.shelly.cloud/gen2/Devices/Gen4/ShellyPlugUSG4/). If a shipped unit reports `gen:4`, the RPC contract below still holds (Gen2+ RPC is generation-generic) but record the actual `gen`/`model`/`fw_id` in the bench log — and note a Gen4 unit carries a Zigbee radio that must stay OFF (stimulus independence). `[REF]`

### 5.2 The RPC contract (quoted shapes)

- **Invocation forms** (https://shelly-api-docs.shelly.cloud/gen2/General/RPCChannels/): GET — "Clients submit a GET request to an endpoint which includes the method name: `/rpc/<method name>` and supply the parameters to the method in a query string" (e.g. `/rpc/Switch.Set?id=0&on=true`); POST — "Clients POST to `/rpc` on the Shelly, supplying the entire JSON RPC call frame as payload" (body `{"id":0,"method":"Switch.Set","params":{"id":0,"on":true}}`). HTTP channel has **no keep-alive** ("does not support connection keepalive") and the device caps **6 simultaneous non-persistent RPC channels** — one fresh connection per command, one command at a time. `[REF]`
- **`Switch.Set`** (https://shelly-api-docs.shelly.cloud/gen2/ComponentsAndServices/Switch/): params `id` (required), `on` (boolean, required), `toggle_after` (optional seconds). Response: **`{"was_on": <bool>}`** — "True if the switch was on before the method was executed." Note `was_on` reports the PRIOR state: it is an accept token, **not** the settled-state assertion (that is GetStatus `output`). `[REF]`
- **`Switch.Toggle`** (same page): params `id`; response `{"was_on": <bool>}`. `[REF]`
- **`Switch.GetStatus`** (same page): `output` — "`true` if the output channel is currently on, `false` otherwise" (THE assertion field); `apower` — "Last measured instantaneous active power (in Watts)"; `voltage`, `current`, `aenergy.total` (Wh), `temperature.tC`, `source` ("Source of the last command, for example: `init`, `WS_in`, `http`"), `errors[]` — "May contain `overtemp`, `overpower`, `overvoltage`, `undervoltage`." `[REF]`
- **Health + identity**: `Sys.GetStatus` → `uptime`, `restart_required`, `available_updates` (https://shelly-api-docs.shelly.cloud/gen2/ComponentsAndServices/Sys/) — log `uptime` with every poll so an unexpected watchdog reboot is visible in the evidence bundle; `Shelly.GetDeviceInfo` per §5.1. `[REF]`
- **Error shape** (https://shelly-api-docs.shelly.cloud/gen2/General/RPCProtocol/): a response carries `result` XOR `error`, error = `{"code": <int>, "message": <string>}` (documented example `{"code": -105, "message": "Bad id=12"}`). Auth failures are HTTP **401** with the challenge in `WWW-Authenticate` (https://shelly-api-docs.shelly.cloud/gen2/General/Authentication/). **The common error codes (gap-fill fetched — https://shelly-api-docs.shelly.cloud/gen2/General/CommonErrors/):** `-103` INVALID_ARGUMENT ("parameters sent in the request do not match the ones specified by the method") · `-104` DEADLINE_EXCEEDED (timeouts, "usually … fetching external resources") · `-105` NOT_FOUND ("instance specified in the request is not found") · `-108` RESOURCE_EXHAUSTED · **`-109` FAILED_PRECONDITION ("precondition for a requested action is not satisfied" — examples include OVERPOWER conditions: the code a bench driver treats as "the plug refused for a physical-safety reason")** · `-114` UNAVAILABLE. Driver rule: HTTP ≠ 200 ⇒ transport/auth failure; HTTP 200 ⇒ check for `error.code` before trusting `result`; `-109` on `Switch.Set` ⇒ FAIL the stimulus step with the code as evidence (never retry into an overpower condition). `[REF]`
- **Auth model**: "Communication through HTTP and Websocket channels is secured by a digest authentication mechanism using the SHA256 hmac algorithm as defined in RFC7616"; single user, "username … must be set to admin"; realm = device id; "Protection through digest authentication over HTTP is enforced **when enabled**" (Authentication + RPCChannels pages). **Default-open on LAN is INFERENCE** (the `auth_en` flag + `Shelly.SetAuth` with "`null` to disable authentication" imply factory = disabled) — verify `auth_en:false` out of the box. Bench REC: leave auth disabled on the isolated bench LAN (simplest driver); if ever enabled, `curl --digest -u admin:<pw>` works (RFC 7616 SHA-256). `[REF]`/INFERENCE

### 5.3 Provision-once checklist (per plug; each step = one RPC + its verify read)

Out of the box the plug raises AP **`ShellyPlusPlugUS-XXXXXXXXXXXX`**, setup IP **`192.168.33.1`** (official user guide: https://kb.shelly.cloud/knowledge-base/shelly-plus-plug-us-user-and-safety-guide). Join the AP, then:

1. **Capture identity (fills §6.5-b):** `GET http://192.168.33.1/rpc/Shelly.GetDeviceInfo` → record `id`, `mac`, `model`, `gen`, `app`, `fw_id`, `auth_en` verbatim into the bench notes. Expect `model:"SNPL-00116US"`, `auth_en:false`.
2. **Join the bench WiFi:** `WiFi.SetConfig` `{"config":{"sta":{"ssid":"<bench>","pass":"<pw>","enable":true}}}` (params quoted: `sta.pass` "Must be provided if you provide ssid" — https://shelly-api-docs.shelly.cloud/gen2/ComponentsAndServices/WiFi/). Verify: device reachable at its LAN address, `WiFi.GetStatus`.
3. **Pin addressing:** DHCP reservation (official REC: "Add a DHCP reservation (MAC -> fixed IP) after a device joins the network" — https://kb.shelly.cloud/knowledge-base/network-design-guide-for-shelly-gen2-devices) **or** static: `WiFi.SetConfig` `{"config":{"sta":{"ipv4mode":"static","ip":"…","netmask":"…","gw":"…"}}}` (fields quoted on the WiFi page). The two plug IPs land in `scenarios/constants.yaml`; **mDNS is discovery-only, never resolved at stimulus time** (§5.6).
4. **Disable the AP:** `WiFi.SetConfig` `{"config":{"ap":{"enable":false}}}`. Verify: `WiFi.GetConfig` → `ap.enable:false`.
5. **Disable cloud (the local-only rail):** `Cloud.SetConfig` `{"config":{"enable":false}}` → response carries `restart_required` (documented example `{"restart_required": false}` — https://shelly-api-docs.shelly.cloud/gen2/ComponentsAndServices/Cloud/); reboot via `Shelly.Reboot` if true. Verify: `Cloud.GetStatus` → not connected.
6. **Disable Bluetooth:** `BLE.SetConfig` `{"config":{"enable":false}}` on 1.x firmware (documented `restart_required: true` example — https://shelly-api-docs.shelly.cloud/gen2/ComponentsAndServices/BLE/); NOTE the BLE schema is firmware-dependent (top-level `enable` "Removed since version 2.0.0") — `BLE.GetConfig` first, key off what is present.
7. **Eco mode OFF (load-bearing for a stimulus driver):** `Sys.SetConfig` `{"config":{"device":{"eco_mode":false}}}`. The vendor's own definition: eco mode "Decreases power consumption when set to true, **at the cost of reduced execution speed and increased network latency**" (https://shelly-api-docs.shelly.cloud/gen2/ComponentsAndServices/Sys/) — exactly the wrong trade for an actuator that exists to stimulate with tight timing. Factory default value unverified — read `Sys.GetConfig` and force false regardless (§6.5-c).
8. **Relay policy:** `Switch.SetConfig` `{"config":{"initial_state":"on","auto_on":false,"auto_off":false}}` — `initial_state` allowed values quoted: "`off`, `on`, `restore_last`, `match_input`" (Switch page). REC `"on"` for a bench actuator: wall power present ⇒ DUT powered, so a plug reboot can never silently strand the DUT off (a stranded-off Hue mid-suite would masquerade as the absent-device class). `auto_on/auto_off:false` — no surprise flips. Optionally set `power_limit`/`current_limit` at the bench-fuse level. Verify: `Switch.GetConfig`.
9. **LED ring:** `PLUGS_UI.SetConfig` `{"config":{"leds":{"mode":"switch"}}}` — LED mirrors relay state = free visual ground truth at the rack. `leds.mode` values "power", "switch", "off" are quoted from the **Plus Plug S** device page (https://shelly-api-docs.shelly.cloud/gen2/Devices/Gen2/ShellyPlusPlugS/); PLUGS_UI presence on the US model is expected but unconfirmed in the current docs tree (§6.5-d) — `PLUGS_UI.GetConfig` on hardware adjudicates; absence is cosmetic-only.
10. **Firmware: check, optionally update, then PIN:** `Shelly.CheckForUpdate` → `stable.version`; update only at provisioning (never mid-suite); record `fw_id` in the bench notes. The bench then treats firmware as frozen instrument state (the MG24 precedent).
11. **Self-measure the latency envelope (fills the honest gap in §5.5):** 20× `curl -w '%{time_total}'` around `Switch.Set` on/off + `Switch.GetStatus`, record min/median/max in the bench notes — this return found NO published local-RPC latency numbers, so the bench mints its own reference points at commissioning.

### 5.4 The driver verbs (curl one-liner + the assertion field per verb)

`$IP` from `scenarios/constants.yaml`; `id=0` is the only switch instance. All verbs: HTTP 200 + no `error` key = accepted; the **assert** column is the field the scenario evidence binds to.

| Verb | curl one-liner | Accept token (response) | Assert (settled state) |
|---|---|---|---|
| `on` | `curl -s "http://$IP/rpc/Switch.Set?id=0&on=true"` | `{"was_on":…}` present, no `error` | follow-up `Switch.GetStatus` → `"output":true` |
| `off` | `curl -s "http://$IP/rpc/Switch.Set?id=0&on=false"` | `{"was_on":…}` present, no `error` | `Switch.GetStatus` → `"output":false` |
| `toggle` | `curl -s "http://$IP/rpc/Switch.Toggle?id=0"` | `{"was_on":…}` (prior state, logged) | `Switch.GetStatus` → `"output" == !was_on` |
| `status` | `curl -s "http://$IP/rpc/Switch.GetStatus?id=0"` | JSON with `"output"` | `output` (+ optional `apower` threshold for is-the-DUT-actually-drawing assertions; `errors[]` MUST be absent/empty) |
| `health` | `curl -s "http://$IP/rpc/Sys.GetStatus"` | JSON with `"uptime"` | `uptime` monotone vs last poll (reset ⇒ plug rebooted mid-run — flag the run); `restart_required:false` |
| `ident` | `curl -s "http://$IP/rpc/Shelly.GetDeviceInfo"` | JSON with `"model"` | `model=="SNPL-00116US"` (per-suite-run preflight) |

**Driver semantics (INFERENCE, from the quoted contract):** `Switch.Set` with explicit `on=` is **idempotent** — safe to retry; `Switch.Toggle` is **not** — never auto-retry a toggle (a retried toggle double-flips; prefer Set in scenarios, reserve Toggle for interactive use). The settle contract: after the accept token, poll `Switch.GetStatus` until `output` matches (expect near-immediate; see §5.5), THEN start the scenario's `settle:` clock — the scenario's `settle: 5s` means "5 s of confirmed wall-power state," not "5 s after we sent an HTTP request."

### 5.5 Latency / timeout / retry expectations

**Honest gap:** neither the official docs nor located community threads yield a numeric local-RPC latency figure (the one promising openHAB thread could not be fetched — proxy 429; §6.5-e). What IS sourced: eco mode explicitly increases latency (vendor text, §5.3-7), the HTTP channel is connectionless per request, and cloud round-trips are out of the picture once disabled. REC (INFERENCE): plan for tens-of-ms-class responses on an idle 2.4 GHz LAN but **budget timeouts in seconds** — driver defaults `--connect-timeout 2 --max-time 5`, ONE retry on transport failure for idempotent verbs only, then FAIL the stimulus step with the curl exit code + any partial body as evidence (a failed stimulus is a SKIPPED/FAILED scenario precondition, never silently absorbed — SCENARIO_FORMAT `requires` honesty). After any wall-power event on the plug's own supply, poll `health` until `uptime` is sane rather than assuming a fixed boot delay (no boot-time figure exists in the docs; §6.5-e). Step 11 of §5.3 replaces this REC with measured bench numbers at commissioning.

### 5.6 Discovery + addressing REC

mDNS: Gen2+ devices advertise `_shelly._tcp` (and `_http._tcp`) with "gen=2" in the TXT record (https://shelly-api-docs.shelly.cloud/gen2/General/mDNS/); hostname pattern `<deviceid>.local` (KB discovery guide example: `Shelly2PMG4-7C2C67640B38.local.` — https://kb.shelly.cloud/knowledge-base/kbsa-discovering-shelly-devices-via-mdns). **REC: use mDNS once at provisioning to find the fresh device, then never again** — fixed IPs (DHCP reservation per the official network-design guide, or `ipv4mode:"static"`) in `scenarios/constants.yaml` are the stimulus-time contract. Rationale: the nightly B3 suite must not take a dependency on multicast name resolution for its actuator channel (mDNS "never crosses a VLAN boundary on its own" — same guide — and a name-resolution flake would read as a stimulus failure).

### 5.7 Constraints and failure modes the driver must respect

1. **6-channel cap:** "The number of simultaneous non-persistent RPC channels … is limited to 6" (RPCChannels page). A serial one-curl-at-a-time driver never hits it; a parallel poller + a human's browser tab + HA could. Keep the driver serial per plug. `[REF]`
2. **Watchdog-reboot class (community, titles only):** Gen2/Gen3 watchdog crash/reboot reports exist on FW 1.7.5 (e.g. "BUG REPORT: Watchdog Crash / Reboot on Gen2/Gen3 (FW 1.7.5) caused by L2 Peer-to-Peer Traffic in UniFi Networks" — https://community.shelly.cloud/topic/14085-…). Mitigation is already in the verb table: `uptime` logged every poll makes a mid-run reboot visible; firmware pinned at provisioning. `[REF]` (titles; bodies unfetched)
3. **Unknown-method behavior:** older firmware answers unimplemented methods with an RPC error ("No handler for X" class — observed as "`No handler for Shelly.GetComponents`," https://github.com/home-assistant/core/issues/123440). The driver sticks to the small stable set above. `[REF]`
4. **Do not copy Gen1 recipes:** `/relay/0?turn=on` URLs in older blog posts are Gen1; this device speaks `/rpc`. (The infamous 18 s-delay HA issue was Gen1 CoIoT multicast, not Gen2 — https://github.com/home-assistant/core/issues/75952.) `[REF]`
5. **Upgrade path noted, not used:** the Webhook component ("This service allows Shelly devices to send HTTP requests triggered by events," events `switch.on`/`switch.off` — https://shelly-api-docs.shelly.cloud/gen2/ComponentsAndServices/Webhook/) can later push state changes to a bench listener; polling remains the B1 baseline. `[REF]`

---

## 6. Consolidated flagged-uncertainty list

Everything below is a KNOWN GAP, stated so Monday's verification is fast. Nothing in §1–§5 papers over any of these. (Items the lane CLOSED during its gap-fill pass are marked ✔-closed and kept for the audit trail.)

### 6.1 S31 Lite zb
- **(a) Profile-ID CONFLICT — the wave's sharpest identity unknown:** `0xC05E` (ZLL; zigpy/zha machine capture, behavior-corroborated by the Hue-bridge quirk) vs `"0104"` (SmartThings hand-written fingerprint). Bench adjudicates; the fingerprint match entry is BLOCKED on it; §1.2 carries the pre-Monday code-read (does anything gate on profile 0x0104?).
- **(b)** z2m `S31ZB` definition-block internals unretrieved (sonoff.ts ~5742, beyond fetch window) — onOff reporting `0/65000/1` and powerOnBehavior-disabled are library defaults + INFERENCE, not device-block quotes.
- **(c)** Power-on relay behavior (StartUpOnOff support) uncharacterized — load-bearing for Shelly-driven wall-power scenarios; `[CONFIRM-ON-BENCH]` at first power-cycle.
- **(d)** Issue/thread bodies unread (titles only): z2m #20618 configure-failures, #3904 duplicate-messages, #19510 (model linkage unconfirmed), Hubitat routing/chatty/pairing threads — severity + confirmation counts unknown.
- **(e)** Command→report latency: no community measurement found; the bench mints the envelope (the `recommendedTimeoutMs: 5000` seed is the Hue's, not measured).
- **(f)** The agent-reported claim that SONOFF definitions "frequently set `skipDuplicateTransaction: true`" was a reader-model summary, not a quoted line — only the library machinery's existence is verified.

### 6.2 SNZB-02P
- **(a)** `help.sonoff.tech` is **robots-disallowed** to this session's fetcher (not a rate-limit — permanent for this environment); the product-page cadence quote (§2.3) stands, but the official change-THRESHOLD is unstated anywhere fetched. ✔-partially-closed (cadence yes, threshold no).
- **(b)** 02P `extend:` list is INFERENCE — stock `m.temperature()/m.humidity()/m.battery()` defaults assumed (10/3600/100 ×2; battery 3600/65000/10). Supporting signal: the 02P page exposes battery % WITHOUT voltage, matching stock `battery()` defaults (the eWeLink-tuned helper exposes voltage — contrast 01P/04P).
- **(c)** Manufacturer-string variance: whether ANY 02P units report `SONOFF` instead of `eWeLink` — unknown; z2m #20734 ("Sonoff SNZB-02P vs eWeLink") body unread.
- **(d)** Keep-awake procedure and Configure-Reporting timeout behavior on this sleepy device: only issue-title evidence (#27919); the 6-hour ZHA unavailability signature (community threads) is unread at body level.
- **(e)** ZHA offset-quirk attribute IDs on `0xFC11` unverified (PR #4263 diff unfetched); `0xFC57` function unknown on every fetched source.
- **(f)** Battery stuck-at-100 %/sudden-death: NO 02P-specific reports found (the known ones are SNZB-02/-02D — different models). Absence of found evidence, not evidence of absence.

### 6.3 SNZB-04P
- **(a)** z2m 04P definition-block internals unretrieved (sonoff.ts ~6513–6533) — the exact IAS/tamper/battery wiring is inferred from exposes + the shared helpers; `ewelinkBattery` usage is indicated (voltage exposed) but not block-quoted.
- **(b)** The OnOff-command linkage: which command per edge (on/off/toggle), whether anything emits with NO binding, and both-edges IAS reporting — all `[CONFIRM-ON-BENCH]` (cluster-map + quirk-suppression evidence only; no traffic capture found; "both edges" rests on the two-state exposure semantics).
- **(c)** IAS CIE enrollment requirement: no evidence either way; "z2m's `iasZoneAlarm()` does not enroll" is a reader-model characterization of modernExtend.ts, not verbatim code. Our platform attempts CIE per Doc 08 §3.12 regardless (never a gate).
- **(d)** Battery TYPE unverified (product page unfetched; capture shows 3.0 V — coin-cell class); pairing hold duration assumed P-family norm; official battery-report cadence unfetched.
- **(e)** Issue bodies unread: tamper-can't-reset #25069, dual-generation dropouts zhaquirks #4222, pairing/interview failures #25968/#28524, powerSource misreport #24025.
- **(f)** The snzb04p.py quirk's import lines may be reader-model paraphrase (the SimpleDescriptor comment + builder chain are corroborated by grep.app AND by the ✔ second machine capture; imports are not load-bearing).

### 6.4 SNZB-01P
- **(a) ✔-closed:** the endpoint map — two zigpy/zha machine captures (fw `0x2000` + `0x2200`, byte-identical) landed during the gap-fill pass; the fingerprint is authorable (§4.2/§4.5).
- **(b) ✔-mostly-closed:** `ewelinkAction`/`ewelinkBattery` bodies now verbatim (mapping lookup + binding + 3600/7200/2 values); the residual inference is only that the 01P block composes exactly these helpers (voltage-expose signal supports it).
- **(c) CONFLICT unresolved:** z2m "can **not** directly control individual devices or groups (v2.2.0) … clicks perform no action" vs zhaquirks #4574 (power-outage → binds to nearest plug and toggles it). Likely firmware-dependent; issue bodies unread; §3.6-3-style bench characterization adjudicates for OUR unit.
- **(d)** Awake-window duration after a press: NOT FOUND in any source; PollControl check-in cadence unknown. Feeds the sleepy-availability scenario design.
- **(e)** Whether presses unicast only-when-bound vs broadcast when unbound: unverified (ties to (c); decides if the coordinator binding is strictly required for event delivery).
- **(f)** Issue bodies unread (the §4.6 list — bind-ineffective, powerSource-unknown, action-entity losses, ZHA/Hubitat/openHAB gaps).
- **(g) THE PLATFORM GAP (not a research uncertainty — the blocking ruling):** ESC-W2-SNZB01P-01, §4.5 — no `button` entity type / no press capability / trigger-subscription mismatch; Doc 02 §3.10 + §3.6 vs Doc 08 §3.10 cross-doc inconsistency. Hub routes pre-profile.

### 6.5 Shelly Plus Plug US (Gen2)
- **(a) ✔-closed:** the CommonErrors catalogue (−103/−104/−105/−108/−109/−114) fetched and folded into §5.2.
- **(b)** `app`/`id` strings for `SNPL-00116US` unverified (no real GetDeviceInfo dump found; updates.shelly.cloud unfetched) — captured at provisioning step 1.
- **(c)** `eco_mode` factory default unverified (widely reported on-by-default; unconfirmed) — step 7 reads and forces false regardless.
- **(d)** PLUGS_UI on the US model: config quoted from the Plug S device page; the current docs tree has NO Plus Plug US page (404; only the 0.14 legacy page + KB) — `PLUGS_UI.GetConfig` on hardware adjudicates; cosmetic-only if absent.
- **(e)** NO local-RPC latency / relay-actuation / boot-time / WiFi-reconnect numbers exist in any fetched source — checklist step 11 self-measures at commissioning; timeouts budgeted in seconds until then.
- **(f)** Default-open auth is INFERENCE (via `auth_en` + `SetAuth` null-to-disable); verify `auth_en:false` at step 1.
- **(g)** Minor: the GET example rendered two ways across extractions (`?id=0&on=true` vs `?id=0,on=true`) — the `&` form matches the page's own "query string" prose; eyeball once. HTTP status codes for non-auth RPC errors undocumented (only 200/401 evidenced) — treat per §5.2 driver rule. `Shelly.GetDeviceInfo` example shows `src` omitted from HTTP-POST frames despite RPCProtocol marking it required — tolerate-and-verify.
- **(h)** Generation drift at purchase: no "Plug US Gen3" exists; a fulfilled order could ship Gen4 (`gen:4`, Matter/Zigbee onboard — keep its Zigbee OFF per stimulus independence). Same RPC contract.

### 6.6 Session-level method note (for the audit)
Three parallel research subagents tripped the shared WebFetch proxy's rate limiter (~40 min of HTTP 429 mid-session). Response: agents were ordered to finalize with evidence-in-hand + explicit NOT-FETCHED queues rather than wait or guess; the parent lane then closed the highest-value gaps serially once the limiter cooled (01P endpoint captures ×2, 04P second capture + zoneType, `ewelink.ts` verbatim, SONOFF 02P official cadence, Shelly CommonErrors). All WebFetch quotes pass through an extraction model; where a claim is load-bearing and single-extraction, it is tagged (e.g. §6.3-c, §6.3-f). No gap was filled by invention; every remaining unknown is enumerated above with its chase URL in §7.

---

## 7. Source index

### 7.1 Repo-local anchors (pointer, not copy — re-derive at consumption)
- `homesynapse-core/integration/integration-zigbee/src/main/resources/zigbee-profiles.json` (the shipped profile + `confirmation[]` shape; the SNZB-03P silicon fingerprint) · `…/schema/zigbee-config-schema.json` (`reporting_overrides`, availability timeouts)
- `homesynapse-core-docs/design/02-device-model-and-capability-system.md` §3.6 (capability tables) / §3.10 (entity types; AMD-44 roles) · `design/08-zigbee-adapter.md` §3.5 (cluster→capability) / §3.7 (default reporting) / §3.10 (device-type classification) / §3.12 (IAS) · `design/07-automation-engine.md` §3.2/§3.4 (subscription filter; trigger types)
- `nexsys-bench/docs/2026-07-06_m9.4-bench-acceptance-record.md` (measured envelopes; IAS twins; no-change class; the open on_off leg) · `docs/2026-07-10_bench-automation-charter.md` · `scenarios/SCENARIO_FORMAT.md`
- `nexsys-hivemind/project-knowledge/device-corpus/` (README + the two Wave-1 entries) · `context/instructions/2026-06-28_AMD-CAND-1_…` (AMD-97 dispatch) · `context/instructions/2026-07-07_M9.4-RPT_…` (posture semantics) · `context/status/PROJECT_SNAPSHOT.md` (v27 beat 3 — the weekend program)

### 7.2 Machine captures + reference-stack source (fetched; the evidence backbone)
1. https://raw.githubusercontent.com/zigpy/zha/dev/tests/data/devices/sonoff-s31-lite-zb.json — S31 full interview capture (identity, 0xC05E, clusters, router)
2. https://raw.githubusercontent.com/zigpy/zha/dev/tests/data/devices/ewelink-snzb-02p-0x00002100.json — 02P capture (identity, clusters, sleepy flags, fw 0x2100)
3. https://raw.githubusercontent.com/zigpy/zha/dev/tests/data/devices/ewelink-snzb-01p-0x00002200.json (+ `…-0x00002000.json`) — 01P captures ×2 (identity, clusters, WB01 quirk)
4. https://raw.githubusercontent.com/zigpy/zha/dev/tests/data/devices/ewelink-snzb-04p-0x00002200.json — 04P capture (clusters, zoneType=21, snzb04p quirk)
5. https://raw.githubusercontent.com/zigpy/zha-device-handlers/dev/zhaquirks/sonoff/snzb04p.py — 04P quirk (SimpleDescriptor comment; 0xFC11 tamper 0x2000; OnOff entity suppression; tamper ReportingConfig 0/900/1)
6. https://raw.githubusercontent.com/zigpy/zha-device-handlers/dev/zhaquirks/sonoff/button.py — WB01/SNZB-01P quirk (device_automation_triggers: toggle/on/off)
7. https://raw.githubusercontent.com/Koenkk/zigbee-herdsman-converters/master/src/lib/modernExtend.ts — TIME_LOOKUP; onOff/temperature/humidity/battery default reporting configs
8. https://raw.githubusercontent.com/Koenkk/zigbee-herdsman-converters/master/src/lib/ewelink.ts — `ewelinkAction` (lookup + `setupConfigureForBinding("genOnOff","output")`) + `ewelinkBattery` (3600/7200/2 + voltage)
9. https://raw.githubusercontent.com/SmartThingsCommunity/SmartThingsPublic/master/devicetypes/smartthings/zigbee-switch.src/zigbee-switch.groovy — S31 DTH fingerprint (the 0104 side of the §6.1-a conflict; S26R2ZB/S40LITE FC57 contrast)
10. grep.app index queries (code-search evidence for sonoff.ts identity lines, fromZigbee.ts:1983, usage sites, zha test-file discovery): https://grep.app/api/search?q=S31ZB · …q=S31%20Lite%20zb · …q=SNZB-02P · …q=%22SNZB-01P%22&filter[repo][0]=Koenkk/zigbee-herdsman-converters · …q=SNZB-04P&filter[repo][0]=Koenkk/zigbee-herdsman-converters · …q=SNZB-01P&filter[repo][0]=zigpy/zha · …q=%22SNZB-04P%22&filter[repo][0]=zigpy/zha · …q=ewelink_action · …q=ewelinkBattery
11. https://raw.githubusercontent.com/Koenkk/zigbee2mqtt.io/master/docs/devices/SNZB-04P.md · …/SNZB-01P.md — z2m raw device docs (exposes semantics; sleepy notes; pairing hold; the v2.2.0 no-direct-control note)

### 7.3 Device pages + official vendor (fetched)
12. https://www.zigbee2mqtt.io/devices/S31ZB.html · https://www.zigbee2mqtt.io/devices/SNZB-02P.html · https://www.zigbee2mqtt.io/devices/SNZB-04P.html · https://www.zigbee2mqtt.io/devices/SNZB-01P.html
13. https://sonoff.tech/en-us/products/sonoff-zigbee-temperature-and-humidity-sensor-snzb-02p — official 02P cadence/accuracy/battery quotes

### 7.4 Shelly official (fetched; §5's contract base)
14. https://shelly-api-docs.shelly.cloud/gen2/General/RPCProtocol/ · …/General/RPCChannels/ · …/General/Authentication/ · …/General/mDNS/ · **…/General/CommonErrors/** · …/ComponentsAndServices/Switch/ · …/Shelly/ · …/WiFi/ · …/Sys/ · …/Cloud/ · …/BLE/ · …/Webhook/ · …/Devices/Gen2/ShellyPlusPlugS/ (PLUGS_UI) · …/Devices/Gen4/ShellyPlugUSG4/ · …/gen2/0.14/Devices/ShellyPlugUS/ · …/gen2/changelog/
15. https://kb.shelly.cloud/knowledge-base/shelly-plus-plug-us (SNPL-00116US; ratings) · …/shelly-plus-plug-us-user-and-safety-guide (AP SSID; 192.168.33.1) · …/kbsa-discovering-shelly-devices-via-mdns · …/network-design-guide-for-shelly-gen2-devices

### 7.5 Community failure-mode index (titles search-verified; bodies = the §6 chase queue)
- S31: z2m #20618 · #3904 · #5533 · #19510 · Hubitat t/91985, t/101320, t/88569, t/36044 · HA `hue/v1/light.py:363` + core-2022.6 changelog (via grep.app)
- 02P: z2m #21213 · #20734 · #22889 · #27919 · #28493 · HA core #149502 · deCONZ #7881, #7903 · HA community t/686475, t/881140 · zhaquirks PR #4263
- 04P: z2m #25069 · #25968 · #28524 · #24025 · #15027 · #16005 · #30744 · #29018 · zhaquirks #4222, #3308 · deCONZ #7857 · HA community t/823255, t/746386, t/1012690
- 01P: z2m #23304 · #23468 · #22032 · #24007 · #26047 · #29963 · #26921 · #20863 · #25630 · #25751 · discussion #24198 · zhaquirks #4574, #4394, #2686 · HA core #104548 · Hubitat t/128804 · openHAB t/148858 · eWeLink forum t/105732
- Shelly: HA core #75952 (Gen1 CoIoT contrast) · #123440 ("No handler for") · shelly community t/14085, t/14756 (watchdog titles) · t/10775, t/11388 (cloud-API 429s)
(Full URLs for every item above appear inline at first use in §1–§5.)

### 7.6 Located, NOT fetched (the chase queue — §6's per-item URLs, deduplicated)
- Code/blocks: https://github.com/Koenkk/zigbee-herdsman-converters/blob/master/src/devices/sonoff.ts (the four definition blocks: ~5742 S31ZB · ~6410 01P · ~6466 02P · ~6513 04P) · https://github.com/zigpy/zha-device-handlers/pull/4263 (+.diff) · https://raw.githubusercontent.com/dresden-elektronik/deconz-rest-plugin/master/devices/sonoff/snzb-01p_switch_wireless.json
- Interview cross-checks: deCONZ #2601 (S31) · #7881 (02P) · #7857 (04P) · zhaquirks #2686 (01P) · #3308 (04P)
- Official manuals: help.sonoff.tech/docs/snzb-02p|snzb-04p|snzb-01p (**robots-disallowed to this fetcher**) · sonoff.tech product pages for S31 Lite zb / 04P / 01P · support.sonoff.tech usermanual pages · itead.cc product pages
- Misc: zigbee.blakadder.com Sonoff pages · cnx-software 01P/02P + 04P reviews · blog.richardfennell.net 02P write-up · updates.shelly.cloud/update/PlusPlugUS · https://community.openhab.org/t/shelly-switch-responses-a-bit-slow/149674 · every §7.5 issue body
