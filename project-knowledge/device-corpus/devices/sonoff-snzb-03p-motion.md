<!--
file: project-knowledge/device-corpus/devices/sonoff-snzb-03p-motion.md
purpose: Wave-1 device characterization — SONOFF SNZB-03P motion sensor (the hero TRIGGER, "motion → light on"). Captures the interview surface and validates it against the HomeSynapse device model (Doc 02 + Doc 08 §3.5). Records the empirical Occupancy-cluster (not IAS-Zone) finding and its capability-binding consequence.
brief: context/planning/2026-06-22_hardware-bench-bringup-and-device-characterization_brief.md
validates-against: design/02-device-model-and-capability-system.md §3.6/§3.10 ; design/08-zigbee-adapter.md §3.5/§3.10/§3.12
schema-version: 1
status: PRE-POPULATED 2026-06-26 (desk research + Doc 02/08 validation). NOT yet a live-silicon capture — see PROVENANCE.
-->

# SONOFF (eWeLink) SNZB-03P — binary_sensor / motion (hero trigger)

> **PROVENANCE — read first.** Pre-populated from public reference data (Zigbee2MQTT, CNX-Software) **and validated against Doc 02/08**. **NOT** a live capture — the corpus "is the acceptance spec, **not a simulation**" (brief §1). Tags: **`[REF]`** = documented from a cited public source; **`[CONFIRM-ON-BENCH]`** = only establishable from the physical unit (manufacturerCode, firmware/dateCode, reported attribute values, the **captured motion event stream**, raw dump). The physical interview + the **event-stream fixture capture** are **Nick-driven**. The **Doc 02/08 verdict is fully computed now**.

- **Identity:** manufacturerName=**`eWeLink`** (Basic cluster), modelIdentifier=**`SNZB-03P`**, manufacturerCode=`0x____` `[CONFIRM-ON-BENCH]` (Node Descriptor), firmware/dateCode (Basic `0x4000`/`DateCode`)=`[CONFIRM-ON-BENCH]`. The `(manufacturerName, modelIdentifier)` profile key (Doc 08 §3.6) = **`("eWeLink", "SNZB-03P")`** `[REF]`
- **Characterized on:** path=**EZSP**, coordinator=SONOFF Dongle Plus MG24, refStack=**ZHA (bellows) then Z2M** `[CONFIRM-ON-BENCH]` version, date=`[CONFIRM-ON-BENCH]`
- **Pairs direct?** **YES — pairs to any Zigbee 3.0 coordinator; the "SONOFF bridge required" listing is marketing** (brief context) `[REF]`. Battery end-device → **sleepy interview** (Doc 08 §3.4): may need a button-press/wake to complete. `[CONFIRM-ON-BENCH]`
- **ZCL device type:** **Occupancy Sensor `0x0107`** `[REF]`
- **Power:** battery (CR2450) end device `[REF]`

## Interview (ground truth)
`[REF]` shape; **exact attribute values + raw dump + the event-stream fixture = `[CONFIRM-ON-BENCH]`.**

- **Endpoint 1**, profile `0x0104` (HA), device type `0x0107`:
  - **in (server)** clusters: `genBasic 0x0000`, `genPowerCfg 0x0001`, `genIdentify 0x0003`, **`msOccupancySensing 0x0406`**
  - **out (client)** clusters: `genOta 0x0019` `[CONFIRM-ON-BENCH]`
  - `msOccupancySensing 0x0406` attributes: `occupancy 0x0000` (Bitmap8, **bit 0 = occupied**); **manufacturer-specific** extras: `motion_timeout` (occupied→unoccupied delay) and `no_occupancy_since` — **non-standard Sonoff attributes on the occupancy cluster** `[REF]`
  - `genPowerCfg 0x0001` attributes: `batteryVoltage 0x0020` (Uint8, 100 mV), `batteryPercentageRemaining 0x0021` (Uint8, 0.5 %)
- raw dump: `[CONFIRM-ON-BENCH]`
- **Event-stream fixture (hero TEST FIXTURE — capture this):** trigger motion, record the sequence of `msOccupancySensing.occupancy` attribute reports (occupied=true → … → occupied=false after `motion_timeout`) with timestamps. **This becomes M9 acceptance ground-truth AND M7.4 E2E input** (brief §3). `[CONFIRM-ON-BENCH]`

## Device-model mapping (Doc 02 §3.6 / Doc 08 §3.5)

| Real cluster / attribute | Expected capability / attribute | Verdict |
|---|---|---|
| `msOccupancySensing 0x0406` · `occupancy` (bit 0) | **`occupancy` · `occupied` (bool)** — Doc 08 §3.5 OccupancySensing row; Doc 02 §3.6 | **MATCH** |
| `genPowerCfg 0x0001` · `batteryPercentageRemaining` | `battery` · `battery_pct` (raw/2) — Doc 08 §3.5 PowerConfiguration row; Doc 02 §3.6 | **MATCH** |
| device type `0x0107` (Occupancy Sensor) | entity_type `binary_sensor` — Doc 08 §3.10; Doc 02 §3.10 | **MATCH** |
| `msOccupancySensing` · `motion_timeout` / `no_occupancy_since` | *(non-standard — needs a device profile, Doc 08 §3.6; no MVP capability)* | N/A (profile, not blocking) |

## Validation verdict: **MATCH** — clean against the device model. Two consequential characterization notes ↓ (advisory escalation **ESC-W1-SNZB03P-01**).

The SNZB-03P maps cleanly: `occupancy` + `battery` on a `binary_sensor`. **The hero trigger is unblocked.** But two empirical facts must propagate to M9 and the hero automation — they are *not* model gaps, they are **binding/assumption corrections**:

1. **The hero trigger is `occupancy`, NOT `motion`.** The brief and the corpus index label this device the **"Motion (hero trigger)"** and the bench expected "Occupancy Sensing **or** IAS Zone." It resolves empirically to **OccupancySensing `0x0406`**, which Doc 08 §3.5 maps to the **`occupancy`** capability (`occupied`), **not** the **`motion`** capability (`detected`). Both capabilities exist in Doc 02 §3.6, so there is no gap — **but the hero automation must trigger on `occupancy.occupied`, and any "motion sensor" archetype assumption keyed on `motion`/`detected` is wrong for this device.** Confirm the hero rule and the pairing-wizard archetype bind to `occupancy`.

2. **No IAS Zone enrollment on the hero path.** Because the P variant uses the Occupancy cluster, **Doc 08 §3.12 IAS Zone enrollment (write `IAS_CIE_Address`, `ZoneEnrollRequest`/`Response`, `ZoneStatusChangeNotification`) is NOT exercised by the hero motion sensor.** The trigger flows as plain `occupancy` attribute reports. **M9 must not gate the hero on IAS enrollment**, and the IAS path remains unexercised by Wave-1 (it returns with the Wave-2 SNZB-04P contact sensor — confirm IAS enrollment there).

3. **Regression-baseline note — same archetype, different cluster across revisions.** The **older SNZB-03** (non-P) uses **IAS Zone `0x0500`** (→ `motion`) and reports **no battery**; the **SNZB-03P** uses **Occupancy `0x0406`** (→ `occupancy`) and **adds** `genPowerCfg` battery. The "Sonoff motion" archetype therefore maps to **different capabilities depending on hardware revision.** M9's device-profile registry (Doc 08 §3.6) and the automation templates must key on `(manufacturerName, modelIdentifier)` — not on a blanket "Sonoff motion → IAS/`motion`" assumption. This is precisely the regression-baseline value of the corpus (brief §1 payoff 2).

## Notes / quirks
- Battery **sleepy end device** — interview may stall until the device wakes (Doc 08 §3.4 sleepy-device queue). Press the pairing button to wake during interview. `[CONFIRM-ON-BENCH]`
- `motion_timeout` is firmware-configurable but writes to `msOccupancySensing` have shown timeout errors in the field (z2m #29933) — note if the M9 profile wants to set it.
- Coarse runtime observations to record for the log-retention thinking (brief §6 DO step 6): pairing time, and motion-report cadence/volume during a 5-min walk-test (occupancy reports + battery cadence). `[CONFIRM-ON-BENCH]`

## Sources (public reference — `[REF]` fields)
- SNZB-03P uses occupancy property / `msOccupancySensing` (motion_timeout written to that cluster), reports battery % + voltage, pairs without bridge: https://www.zigbee2mqtt.io/devices/SNZB-03P.html ; https://github.com/Koenkk/zigbee2mqtt/issues/29933
- SNZB-03P overview (P-variant upgrade over SNZB-03): https://www.cnx-software.com/2024/01/30/review-sonoff-snzb-03p-zigbee-motion-sensor-ewelink-home-assistant/
- Older SNZB-03 uses IAS Zone (`ssIasZone`) + genPowerCfg, contrast: https://www.zigbee2mqtt.io/devices/SNZB-03.html
