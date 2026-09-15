<!--
file: context/research/2026-09-15_PLUG-DOSSIER_return.md
purpose: THE PLUG DOSSIER — the read-only micro-lane's return on `PLUG: two` (D-v74-4): US Zigbee metering plugs graded on Nick's two disqualifying criteria (ONE STANDARD_ZCL model with 0x0B04 AND 0x0702 as server clusters, multiplier/divisor present; a plug-in reference meter), the Shelly Plug US Gen4 units Nick owns graded FIRST. Result: the Gen4 units qualify — buy NO plugs, buy the reference meter only. Run by an in-conversation agent at v75 b4; audited two-layer by the hub (`context/audits/2026-09-15_v75-b4_CI-verdicts_freeze-v115_premise-gate_MEASURE-1_plug-dossier_audit.md` §4 — the disqualifying rows re-fetched at the Shelly feature matrix; the z2m converter cited at a tag). THE ADOPTION FENCE stands: no metering plug joins any card before ENERGY-READ is green. The divisor prediction (acPowerDivisor 10) is adjudicated at ENERGY-READ's first read.
audience: Nick (§0 — the one-paste shopping card is in the b4 operator packet, block 3) · the hub (ENERGY-READ's fixture — §1's divisor column) · the bench lane (`metering-known-load.yaml`'s operator blocks)
state-type: research return (read-only; no grading in chat; prices as of 2026-09-15 — they move)
status: FILED v75 beat 4 (2026-09-15); ACCEPT with the hub's re-executions. Supersedes nothing; the plan of record §7 DROPS the second plug purchase on this dossier.
-->

# Zigbee metering-plug dossier (US, standard ZCL only) — 2026-09-15

## §0 Recommendation

**Shelly Plug US Gen4 (S4PL-00116US) ×2 — the owner already has units; buy no plugs.** Buy only the reference meter: **P3 Kill A Watt EZ P4460** (±0.2 %, $43.87 Home Depot), fallback **Poniie PN2000** (Class 1.0, $28.99).

Disqualifying criteria MET, by citation:
- **Zigbee; 0x0B04 + 0x0702 as Input (server) on EP1; Router.** Shelly feature-matrix row "Shelly Plug US": "On/Off Plug-in Unit (0x010A)", "Zigbee Router", "On/Off (0x0006): Endpoint 1: Input", "Metering (0x0702): Endpoint 1: Input", "Electrical Measurement (0x0B04): Endpoint 1: Input". Manufacturer clusters 0xFC01/0xFC02 (EP239) and 0xFC21 are RPC/Wi-Fi/light-level, not metering — https://shelly-api-docs.shelly.cloud/gen2/Integrations/Zigbee/DeviceFeatures
- **Divisor attrs, no quirk.** z2m shelly.ts (tag v25.80.0, complete file): `zigbeeModel: "Plug US", model: "S4PL-00116US", extend: [m.onOff({powerOnBehavior: false}), m.electricityMeter(), ...shellyCustomClusters(), shellyWiFiSetup()]` — https://raw.githubusercontent.com/Koenkk/zigbee-herdsman-converters/v25.80.0/src/devices/shelly.ts . `m.electricityMeter()` defaults `cluster: 'both'` (haElectricalMeasurement + seMetering), runs `endpoint.read(cluster, [divisor, multiplier])` for `acPowerDivisor/acPowerMultiplier`, `acVoltageDivisor/Multiplier`, `acCurrentDivisor/Multiplier`, seMetering `divisor/multiplier`, then configures reporting for activePower/rmsVoltage/rmsCurrent/currentSummDelivered — https://raw.githubusercontent.com/Koenkk/zigbee-herdsman-converters/master/src/lib/modernExtend.ts
- Corroboration (same Gen4 firmware): ZHA signature Mini1PM Gen4: EP1 in_clusters 0x0000,0x0003,0x0004,0x0005,0x0006,0x0702,0x0b04; EP239 0xfc01,0xfc02; standard clusters work "without custom quirks" — https://github.com/zigpy/zha-device-handlers/issues/4125 . Hubitat `inClusters:"0000,0003,0004,0005,0006,0B04,0702"`; a divisor-reading driver is correct, the generic driver off ×10 — divisor attrs are real — https://community.hubitat.com/t/zigbee-with-gen4-shelly-work/152290
- **OnOff reporting.** `m.onOff` configures `genOnOff` attr `onOff` reporting (min/MAX/change 1) (modernExtend.ts). Gen4 honours reporting config on 0x0B04: missing updates fixed by lowering `Min rep change` to 1 W — https://github.com/Koenkk/zigbee2mqtt/issues/30381 . Physical-toggle OnOff report trace: UNVERIFIED (§4).
- **Rating/price.** 15 A, 1800 W, 120 V, NEMA 5-15 — https://kb.shelly.cloud/knowledge-base/shelly-plug-us-gen4 ; "Acts as ... Zigbee router", $24.99, In stock — https://us.shelly.com/products/shelly-plug-us-gen4-white ; Best Buy $24.99 but "Unavailable from this seller" — https://www.bestbuy.com/product/shelly-plug-us-gen4-smart-home-plug--wi-fi-bluetooth-zigbee--1800w--energy-monitoring-light-sensor-white/JV5QKYSQLK
- **Caveats.** z2m: update firmware via WiFi/BT first; "The latest firmware fixes known issues like negative power readings" — https://www.zigbee2mqtt.io/devices/S4PL-00116US.html . Default report thresholds >5 W (#30381). 5 pushes = Matter↔Zigbee, 3 = pair (KB).

## §1 Grading table

| model | Zigbee | 0x0B04 srv | 0x0702 srv | divisor attrs | quirk | OnOff rpt | rating | router | US avail/price | sources |
|---|---|---|---|---|---|---|---|---|---|---|
| **Shelly Plug US Gen4** | Y | Y EP1 | Y EP1 | read by `m.electricityMeter()` | No | configured; trace UNVERIFIED | 15 A/1800 W | Y | $24.99 in stock | §0 |
| Innr SP 244 (US) | Y | Y (2820) | Y (1794) | read; Innr staff: "'Multiplier' and 'Divisor' attributes 0x0600 to 0x0605 of cluster 0x0b04" | No | `m.onOff({configureReporting: true})` | UNVERIFIED (EU SP 240 16 A) | Y ("type":"Router") | UNVERIFIED | https://github.com/Koenkk/zigbee2mqtt/issues/20234 ; https://raw.githubusercontent.com/Koenkk/zigbee-herdsman-converters/master/src/devices/innr.ts ; https://community.hubitat.com/t/innr-sp244-zigbee-smart-plug/137011/26 |
| Third Reality 3RSP02028BZ | Y | Y | Y | reads them, then z2m OVERWRITES: `seMetering divisor 3600000`, `acVoltageDivisor 10`, `acCurrentDivisor 1000`, `acPowerDivisor 10` | partial (0xFF03 for LED/countdown; divisor override) | `reporting.onOff`; Hubitat: "Out of the box reporting is only ON_OFF_CLUSTER min 0 max 240" | 15 A (eBay title) | repeater (vendor) | $12.99 "Sold out" 3reality; eBay $18.99 OOS | https://raw.githubusercontent.com/Koenkk/zigbee-herdsman-converters/master/src/devices/third_reality.ts ; https://raw.githubusercontent.com/bradsjm/hubitat-public/main/ThirdReality/ThirdRealityPowerMonitorPlug.groovy ; https://www.thirdreality.com/products/smart-plug-gen2-power-metering ; https://www.ebay.com/itm/396742862132 |
| IKEA INSPELNING E2220 (US) | Y | Y | Y | `m.electricityMeter()`, but `acPowerDivisor` "needs to change dynamically with the amount of power" — adapter must track divisor reports | none for metering | `m.onOff()` | UNVERIFIED | UNVERIFIED | $11.99 at 2024 launch; now UNVERIFIED | https://raw.githubusercontent.com/Koenkk/zigbee-herdsman-converters/master/src/devices/ikea.ts ; https://homekitnews.com/2024/09/10/ikea-release-smart-plug-with-energy-monitoring/ |
| SmartThings Outlet 2018 GP-WOU019BBDWG | Y | Y (W) | Y (kWh) | `m.electricityMeter({current: false, voltage: false})` | No | `m.onOff()` | UNVERIFIED | UNVERIFIED | discontinued; UNVERIFIED | https://raw.githubusercontent.com/Koenkk/zigbee-herdsman-converters/master/src/devices/smartthings.ts |
| Tuya TS011F (metering) | Y | Y | Y | standard, but FW ≥1.0.5: "TuYa has disabled the automatic reporting of power, voltage and current ... need to be polled" | polling | UNVERIFIED | UNVERIFIED | UNVERIFIED | no NEMA variant identified | https://www.zigbee2mqtt.io/devices/TS011F_plug_1.html ; https://www.zigbee2mqtt.io/devices/TS011F_plug_3.html |

## §2 Disqualified

- Sonoff S31ZB — "Exposes: switch (state)" only — https://www.zigbee2mqtt.io/devices/S31ZB.html
- Sonoff S40ZBTPB — switch only — https://www.zigbee2mqtt.io/devices/S40ZBTPB.html
- Sonoff S26R2ZB — switch only — https://www.zigbee2mqtt.io/devices/S26R2ZB.html
- Third Reality 3RSP019BZ — `extend: [m.onOff(), ...0xff03 custom]`, no meter (third_reality.ts above)
- Sengled E1C-NB7 — `m.electricityMeter({cluster: "metering"})`: 0x0702 only, no 0x0B04 — https://raw.githubusercontent.com/Koenkk/zigbee-herdsman-converters/master/src/devices/sengled.ts
- Centralite/Iris 3210-L — 0x0B04 only, no seMetering; discontinued — https://raw.githubusercontent.com/Koenkk/zigbee-herdsman-converters/master/src/devices/iris.ts
- Hue smart plug 929003050601 — "switch (state), power_on_behavior, identify" — https://www.zigbee2mqtt.io/devices/929003050601.html
- Sylvania/Ledvance SMART+ 72922-A — "switch (state), power_on_behavior" — https://www.zigbee2mqtt.io/devices/72922-A.html
- IKEA TRETAKT E2204 — no `m.electricityMeter()` (ikea.ts above)
- Innr SP 234 — divisors hard-coded in converter (`current: {divisor: 1000}, voltage: {divisor: 1}, power: {divisor: 1}, energy: {divisor: 100}`) (innr.ts above)
- Aqara ZNCZ12LM (lumi.plug.maus01) — metering via `lumi.fromZigbee.lumi_power`/`lumi_specific` — https://raw.githubusercontent.com/Koenkk/zigbee-herdsman-converters/master/src/devices/lumi.ts
- Tuya TS0601 class — 0xEF00, excluded by rule.

## §3 Reference meter

| meter | accuracy | max | price/avail | link |
|---|---|---|---|---|
| P3 Kill A Watt EZ **P4460** | "Accurate to within 0.2%" | 15 A/1875 VA | $43.87 Home Depot (stock not shown); $34.99 p3 shop "Sold out"; Lowe's listed | https://shop.p3international.com/products/kill-a-watt-ez ; https://homedepot.com/p/P3-International-Kill-A-Watt-EZ-Meter-P4460/202196388 ; https://www.lowes.com/pd/Choose-Renewables-Kill-A-Watt-EZ/3191393 |
| P3 Kill A Watt **P4400** | "0.2% Accuracy" | 15 A/1875 VA | $32.99 p3 shop "Sold out"; Newegg OOS; Walmart $55.19 OOS | https://www.p3international.com/products/p4400.html ; https://shop.p3international.com/products/kill-a-watt |
| Poniie **PN2000** | "Accuracy standard Class 1.0" (±1 %); res 0.01 W/0.001 A/0.01 V | 16 A/1760 W@110 V | $28.99 poniie.com | https://poniie.com/products/6 ; https://poniie.com/download_manual/12 |

Pick P4460 (5× tighter) where stock shows; else PN2000.

## §4 Not verified

- Shelly: no fetched log of an unsolicited genOnOff report after a physical toggle; Shelly Zigbee docs list cluster IDs only, no attribute/reporting tables. Best Buy unavailable; only us.shelly.com confirmed in stock.
- Innr SP 244: US retailer, price, amp rating (Amazon robots-blocked; innr.com US page 404).
- IKEA E2220: current US price/stock, rating, router role; GitHub comment on dynamic divisor (#23961) not fetchable — cited via ikea.ts code comment only.
- Third Reality: 15 A from an eBay title only; Amazon stock not fetched.
- SmartThings 2018 outlet: rating/router/stock not fetched.
- Tuya TS011F: which manufacturerName strings are NEMA 5-15 — none found.
- z2m `shelly.ts`/`philips.ts`/`lumi.ts`/`tuya.ts` at master exceed the fetch limit; Shelly cited from tag v25.80.0 (file ends `];`).
