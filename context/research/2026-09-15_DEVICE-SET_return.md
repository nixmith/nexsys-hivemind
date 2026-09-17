<!--
file: context/research/2026-09-15_DEVICE-SET_return.md
purpose: DEVICE-SET's return — the benchmark fleet to order now, each unit with its row and instrument; P1–P5 adjudicated; two tiers priced.
audience: Nick (§0, `DEVICES: core|extended|<edits>`) · the hub (intake; ENERGY-READ's fixture — the §1 notes) · the bench lane (§2)
state-type: research return (read-only; prices as fetched — they move)
status: RETURNED Tue 2026-09-15 CT (instrument 2026-09-16T02:19Z). "z" = zigbee-herdsman-converters v26.110.0 (tag 2026-09-15, via its npm tarball). Links fetched 2026-09-15 CT.
-->

# DEVICE-SET — the benchmark fleet — 2026-09-15

## §0 The card
**Recommend `DEVICES: core` — $104.78 list, pre-tax.** CORE: Third Reality Smart Plug Gen3 ×1 $14.99 · Poniie PN2000 (reference A; stock §4) $28.99 · P3 P4460 (cross-check B; Walmart) $42.43 · Southwire clamp light $9.63 · GE 40 W appliance lamp ×2 $8.74. EXTENDED +$73.89: SONOFF SNZB-06P24 $24.90 + Hue motion sensor SML003 $48.99 — in stock, fenced until IR-18; waiting costs one order, so not now. Edits: `-B` → $62.35 · `+TR3` → +$14.99 (a unit spread on model B).
- **P1 CONFIRMED** — two Gen4 units already give model A's spread; four corrections in §1's notes.
- **P2 CONFIRMED, off the list** — the Gen3 (divisors read from the device; maker ±1 %); every listed one is REFUSED.
- **P3 REFUTED** — the P4460 manual: power 0.5 % typ / 2 % max (0.2 % is its voltage row); the maker is sold out, Home Depot and Lowe's show no stock. None found under $100 states Class ≤ 0.5, so A = PN2000 (Class 1.0, 0.01 W), B = P4460.
- **P4 SPLIT** — CORE over by $4.78 (B is the overrun); EXTENDED $73.89 < $180.
- **P5 PARTLY** — the load is $14.00 with one lamp (cheapest, by $0.99), $18.37 with the spare; the 60–100 W lamp it names is not sold new.

**Method.** One sitting, one tungsten load (40 W, PF≈1, 0.33 A — inside B's 0.2–15 A typical band), plugs G4-1 · TR3 · G4-2, three reps each; per rep, at one instant, the platform's `power_w`, A and B, chained wall→A→B→plug→lamp so no meter switches. The block anchors on the platform's frame and rings; the human reads. A and B must agree within 1.5 % (A's class + B's typical) or the rep is `reference-disputed`; a ratio off by > 50 % is `divisor-error` (the platform's verdict). Else `within` iff |ratio − 1| ≤ 1.0 % (A's class) + the plug's quantization (0.5·mult/div W ÷ load) + 1.6·ΔV/V (P ∝ V^1.6) + the maker's stated accuracy (TR3 1 %; Shelly states none, so its error is the datum). At 40 W, ΔV 0.3 V: ≈ 2.7 % (divisor-1 Gen4), ≈ 2.5 % (divisor-10 Gen3).

## §1 The grading table (prices 2026-09-15 CT)
| model | vendor | radio/role | clusters (server) | divisor shape | rating | maker accuracy / resolution | US price + stock | row | instrument | tier |
|---|---|---|---|---|---|---|---|---|---|---|
| Plug US Gen4 S4PL-00116US (own ×2) | Shelly | router [sdf] | EP1 dev 0x010A: 0006 0702 0B04 FC21 [sdf][z5182] | z `m.electricityMeter()`, read at join; 1 or 100 (note 3) | 15 A/1800 W [sus] | none stated [sus] | $24.99 "In stock" [sus] | ENERGY-READ; the run's watts | reps; the run | CORE (owned) |
| Smart Plug Gen3 3RSP02064Z | Third Reality | router ("Zigbee Repeater") [tr3] | z: onOff, meter, FF03; dev UNVERIFIED | z `m.electricityMeter()`, read at join; power "delayed for almost 1 minutes" [z2m3] | "15A" [tr3] | "±1% detection accuracy" [tr3]; a user: "not impressed with the precision" [ha3] | $14.99 available [tr3] | ENERGY-READ, vendor 2 | reps | **CORE** |
| PN2000 | Poniie | none (by eye) | — | — | 16 A/1760 W [pn] | "Class 1.0"; 0.01 W, 0.001 A, 0.01 V [pn] | $28.99, no stock line [pn] | reference A | each rep | **CORE** |
| Kill A Watt EZ P4460 | P3 | none | — | — | 15 A/1875 VA [p3m] | W 0.5 % typ, 2 % max; V 0.2 %; typ at 0.2–15 A; W resolution unstated [p3m] | $42.43, arrives Sep 22 [wmt]; HD $44.32, no stock line [hdk]; maker "Sold out" [p3s] | cross-check B | XCHK | **CORE** |
| clamp light 64810801 + lamp 40A15/RVL/APP/HD ×2 | Southwire; GE | none | — | — | 150 W porcelain, "UL listed" [clamp]; 40 W [lamp] | — | $9.63 [clamp]; $4.37 each [lamp] | known load; the run's load | each rep | **CORE** |
| SNZB-06P24 | SONOFF | 24 GHz mmWave; router [s24] | z `m.illuminance` + `m.occupancy` (`reporting:false`) + FC11; dev UNVERIFIED | — | — | — | $24.90 available [s24] | IR-18; mmWave presence | interview line; a lux block | **EXTENDED** |
| Hue motion SML003 | Signify | battery end device [z1417] | EP2 dev 0x0107: 0001 0400 0402 0406 [z1417] | — | 2×AAA [hue] | — | $48.99 "In stock" [hue] | IR-18, vendor 2 | same | **EXTENDED** |
| Gen2 3RSP02028BZ · Gen1 3RSP019BZ | Third Reality | mains | Gen2 0B04 0702; Gen1 onOff only (z) | Gen2: z pins divisors (power 10, current 1000, energy 3.6×10⁶) | — | — | — | — | — | REFUSED: quirk · no meter |
| SP 244 | Innr | router; devId 266 = 0x010A [z20234] | 0006 0008 0702 0B04 E001 [z20234] | z: SP 240 white label, "Needs FW 1.9.27/1.9.28+" | — | — | no US price + stock page (§4) | — | — | REFUSED: no listing |
| INSPELNING E2220 | IKEA | mains | 0B04 0702 | z: acPowerDivisor "needs to change dynamically" | — | — | US page opens "Products - IKEA" [ikea] | — | — | REFUSED: moving divisor; no listing |
| S40ZBTPB · SmartThings 2018 outlet | SONOFF · SmartThings | mains | S40: switch only (dossier) | 2018: z "voltage and current values are always 0" | — | — | — | — | — | REFUSED |
| R3 3RPL01084Z | Third Reality | 60 GHz; USB-C; repeater [r3] | EP1: 0006 0008 0300 0400 0406 042E [r3h] | — | — | — | $49.99 available [r3] | IR-18; presence | — | REFUSED: dominated |
| WL2 3RWS0218Z | Third Reality | battery | z: IAS water_leak | — | — | — | $17.99 available [wl2] | IR-15's check | — | REFUSED now: the fence |
| HOBO UX120-018 | Onset | none (logger) | — | — | 15 A/1800 W [hobo] | power "0.5% up to 14 Amp"; 10 mW [hobo] | $335.00 [hobo] | A-vs-B tie-break | — | REFUSED: price — buy at the first `reference-disputed` rep |

**Notes for ENERGY-READ's fixture** (refutable at first join).
1. **Device type.** The Gen4 is 0x010A "On/Off Plug-in Unit" [sdf][z5182]; the plug arm is 0x0051 only (`EndpointClassifier.java:41/:99`), so a Gen4 falls to `fallback` (`:102`) → SWITCH (`:186`), and an SP 244 (with 0x0008) → LIGHT (`:183`). Attach meters by cluster, not by "the 0x0051 arm" (IR-17); IR-20(a)'s line should print the type.
2. **Raw thresholds.** `ReportingConfigurator.java:71–72` hold raw changes (0B04: 10; 0702: 5). Divisor 1 ⇒ 10 W: any swing under 10 W (a dimmed bulb) behind a Gen4 waits for the 3600 s max; seMetering divisor 10⁶ ⇒ 5 mWh: a frame every 5 s at 40 W. z reads the divisor first, then `change = property.change * (divisor / multiplier)` (power 5 W) [z].
3. **The divisor P-row.** No Gen4 read shows 10: a 1PM Gen4 reads 0x0605 = 100 [hub] and 1 [z30381] (seMetering 10⁶ in both); [hub]'s "off by a factor of 10" reads as a generic driver on a divisor-100 unit. Predict Plug US ∈ {1, 100}. TR3: unknown (Gen2's pinned 10 the only prior); z's unforced meter asserts both are numbers at configure, so they exist. The fixture replays 1, 10, 100 regardless.
4. **Firmware.** Shelly 2.0.0 (2026-07-13): "Fix excessive power measurements reporting"; "PlugUS Gen4: Add Zigbee illuminance cluster" [scl] — but [sdf] shows only "Shelly Light Level (0xFC21)" for Plug US: IR-18 needs its own unit unless the interview shows 0x0400. Update both first.

## §2 The known load and the sitting's operator blocks
No 60–100 W general-service incandescent is sold new: "incandescent and halogen GSLs are not able to meet the 45 lm/W requirement" [fr]; the exempt appliance lamp tops out at "40 watts" [cfr]. So: a 40 W appliance lamp (and a spare) in a UL porcelain clamp light on a non-combustible surface, burned in for an hour. Tungsten is not a fixed resistor — P ∝ V^1.6 [rr] — so a ±5 % line swing moves it 36.8–43.2 W (−7.9/+8.1 %, not V²'s ±10 %); its label is a sanity check, the simultaneous reading the reference.
```
chain  wall → A (PN2000) → B (P4460) → PLUG → LAMP; nothing above B switches
T1     once: B's outlet empty, 30 s → enter A_W = BSELF
T2     per PLUG: into B, turn_on CONFIRMED, LAMP out, 30 s → A_W = TARE; A_V twice 10 s apart (ΔV); the platform's power_w = OFFSET (expect 0.0)
REP    per PLUG (G4-1 · TR3 · G4-2): LAMP in, then ×3: api turn_off → 15 s → turn_on; anchor = the first power_w frame stamped ≥ 5 s after the on-edge (never `date`)
READ   bell + "READ NOW" → enter A_W, A_V, B_W within 10 s of the anchor, else VOID; no frame in 60 s ⇒ VOID, the delay recorded
XCHK   |B_W − (A_W − BSELF)| > 1.5 % of (A_W − BSELF) ⇒ reference-disputed
DIV    r = (power_w − OFFSET) / (A_W − TARE); |r − 1| > 0.5 ⇒ divisor-error
BAND   within iff |r − 1| ≤ 1.0 % + (0.5·mult/div W) / (A_W − TARE) + 1.6·ΔV/A_V + maker accuracy (TR3 1 %, Shelly 0); else outside
```

## §3 Refused, and why
The table's tier column carries its rows' reasons; the rest:
- **A second protocol** (one radio until the run): IKEA GRILLPLATS/TOFSMYGGA (z: "(Matter)"), Wi-Fi meter plugs, and the Gen4's own Wi-Fi readout as a third reading (after the run).
- **Quirks, not read paths:** TR Dual Plug ZP1 (two metered endpoints, forced energy divisor — z), Sinopé SP2600ZB (forced energy divisor — z), Tuya TS011F/TS0601 (the rule).
- **Watts on 0x0702 only** (instantaneousDemand, which `ReportingConfigurator.java:72` never configures): GE 45853GE, Jasco 43095, Sengled E1C-NB7 (z: seMetering only).
- **No listing, or dominated:** IKEA VALLHORN (its US page opens "Products - IKEA" [vall]); SNZB-06P (lux only dim/bright on FC11 — z); TR R2 (IAS, no 0x0400 — z); Aqara FP300 (lumi — z); Inovelli VZM32-SN (z: a "Dimmer", in-wall).
- **R3:** twice the SNZB-06P24's price, and its light clusters send the fallback to LIGHT unless its type is 0x0107. **WL2:** fenced until IR-15 is green — the row's instrument today is the synthetic enrol replay, and a two-day order beats rehearsal 2. **The owned S31** stays P-1's harness; in the run a Gen4 upstream reads its watts.

## §4 Unverified (each with the link that failed)
- Plug US: an OnOff report on a physical press (no log; a 2PM Gen4 reported local switching only after a re-pair [ha2pm]); its divisors (github.com/user-attachments/files/30103497/…Shelly.Plug.US….json → 401). Rehearsal 2 measures both.
- TR3 device type, clusters, divisors: github.com/Koenkk/zigbee2mqtt/issues?q=3RSP02064Z → robots-blocked; github.com/user-attachments/files/26161789/…3RSP02064Z….json → 401.
- PN2000 stock: amazon.com/dp/B0777H8MS8 → robots-blocked; [pn] has no cart; newegg.com/p/pl?d=poniie+pn2000 → 0 items.
- P4460: watt resolution (absent from [p3m]); Home Depot stock ([hdk]: no line); lowes.com/pd/Choose-Renewables-Kill-A-Watt-EZ/3191393 → "Get Pricing & Availability" only.
- Innr SP 244 in the US: amazon.com/dp/B07SQGG8Z7 → robots-blocked; innr.com/en-us/ → 404. IKEA E2220: github.com/Koenkk/zigbee2mqtt/issues/23961#issuecomment-2366733453 → did not load.
- SNZB-06P24: device type, clusters (no signature found); whether 0406/0400 take a reporting config (z: `reporting:false`). HD stock for the clamp light and lamps.

## §5 The next device classes and the row each waits on
| class | unit | waits on |
|---|---|---|
| illuminance 0x0400 (two vendors) · mmWave presence 0x0406 | SNZB-06P24 + Hue SML003 (0x0107 arm: occupancy + battery only) | IR-18 in ENERGY-READ — adoption is one-way: adopt once, with lux |
| water / smoke / vibration IAS | TR WL2 | IR-15 |
| multi-endpoint · moving-divisor · 0x0702-only metering | TR ZP1 · IKEA-class · GE-class | WUs after the run |
| community plugins | nothing new — the same bench | the plugin SDK |

[z]: https://github.com/Koenkk/zigbee-herdsman-converters/tree/v26.110.0/src
[sdf]: https://shelly-api-docs.shelly.cloud/gen2/Integrations/Zigbee/DeviceFeatures
[z5182]: https://github.com/zigpy/zha-device-handlers/issues/5182
[sus]: https://us.shelly.com/products/shelly-plug-us-gen4-white
[scl]: https://shelly-api-docs.shelly.cloud/gen2/changelog/
[hub]: https://community.hubitat.com/t/152290
[z30381]: https://github.com/Koenkk/zigbee2mqtt/issues/30381
[ha2pm]: https://community.home-assistant.io/t/888242?page=4
[tr3]: https://www.thirdreality.com/products/smart-plug-gen3.js
[z2m3]: https://www.zigbee2mqtt.io/devices/3RSP02064Z.html
[ha3]: https://community.home-assistant.io/t/1002785
[z20234]: https://github.com/Koenkk/zigbee2mqtt/issues/20234
[ikea]: https://www.ikea.com/us/en/p/inspelning-plug-smart-energy-monitor-90569846/
[vall]: https://www.ikea.com/us/en/p/vallhorn-wireless-motion-sensor-smart-white-40504348/
[p3m]: https://www.p3international.com/manuals/p4460_manual.pdf
[p3s]: https://shop.p3international.com/products/kill-a-watt-ez
[wmt]: https://www.walmart.com/ip/14282371
[hdk]: https://www.homedepot.com/p/202196388
[pn]: https://poniie.com/products/6
[clamp]: https://www.homedepot.com/p/303047495
[lamp]: https://www.homedepot.com/p/100393381
[fr]: https://www.federalregister.gov/d/2024-07831
[cfr]: https://www.ecfr.gov/current/title-10/section-430.2
[rr]: https://en.wikipedia.org/wiki/Lamp_rerating
[s24]: https://sonoff.tech/en-us/products/sonoff-senseguard-presence-core-24ghz-zigbee-human-presence-sensor-snzb-06p24.js
[hue]: https://www.philips-hue.com/en-us/products/all-products/product-page.hue_motion-sensor_indoor
[z1417]: https://github.com/zigpy/zha-device-handlers/issues/1417
[r3]: https://www.thirdreality.com/products/smart-presence-sensor-r3.js
[r3h]: https://community.hubitat.com/t/162206
[wl2]: https://www.thirdreality.com/products/smart-water-leak-sensor-wl2.js
[hobo]: https://www.onsetcomp.com/products/data-loggers/ux120-018

RETURNED nexsys-hivemind/context/research/2026-09-15_DEVICE-SET_return.md 13995
