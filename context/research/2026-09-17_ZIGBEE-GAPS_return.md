<!--
file: context/research/2026-09-17_ZIGBEE-GAPS_return.md
purpose: ZIGBEE-GAPS's return — HEAD's Zigbee coverage against the field's corpus at one tag (read / classify / adopt); gaps ranked per lane-day, an instrument each; the market column; P1–P5.
audience: the hub (intake; October charters draw from §2) · Nick (`GAPS: <top-N to charter>`)
state-type: research return (read-only; retail rows as fetched — they move)
status: RETURNED Thu 2026-09-17 CT (instrument 2026-09-17T12:13Z). Core read at `be4788a` = `3d40b5f` + DUR-1/HASH-1 (`git diff 3d40b5f be4788a -- integration/` empty). "z" = Koenkk/zigbee-herdsman-converters tag v26.110.0 (`fce9c18`, 2026-09-15): tag source parsed, same-version npm dist loaded. "zh" = zigbee-herdsman v10.9.3 (`467b284`), z's dependency.
-->

# ZIGBEE-GAPS — coverage against the field — 2026-09-17

## §0 The card
**HEAD vs z v26.110.0, 4,499 definitions; every capability must pass** (capability = a published, non-setting z expose, 29 classes; read = on a standard cluster HEAD handles; classify = the classifier yields it; adopt = no vendor interview step; §1): read **34.7 %** (1,563) · classify **33.4 %** (1,501) · adopt **79.7 %** (3,584) · all three **29.7 %** (1,338). Band 27.7–31.0: 27.7 if no temperature endpoint is 0x0302 (92 ride that arm; z shows 45 device types), 31.0 without `tamper`, 29.3 counting zh's Tuya interview tolerance.
- **P1 — clause 1 CONFIRMED, narrowly; clause 2 REFUTED.** Over 60 %: dimmable lights only (79.5); switch/plug 45.0, temp/humidity 48.2, contact 27.6, motion 22.1. Rig: 2 of 6 pass (S31, SNZB-02P); SNZB-04P fails on `tamper`, SNZB-03P on 0xFC11 dim/bright, SNZB-01P on `action`, LCA017 (extended-color) on xy/hs.
- **P2 — REFUTED.** Full color is the largest gap (blocks 15.0 %, alone 14.5); metering blocks 10.4 (alone 5.2), ranked 3rd. ENERGY-READ leads for the run, not coverage.
- **P3 — PARTLY.** Interview steps block most often (magic packet 15.9 %, lumi 4.1) but unlock +3.1 pp at rank 4 — the same devices need the codecs. "Any device" needs a quirk layer: ceiling 93.6 % with it, 72.9 without; size 565 EF00 definitions (1,368 fingerprints) + 180 lumi + 184 on 44 vendor clusters.
- **P4 — PARTLY.** Illuminance is a ½-day handler; pressure lacks a capability; cover/lock are reserved actuators (multi-day).
- **P5 — PARTLY.** Classify-by-clusters is ≈1 day and structural, but 7th (+2.5 pp); 3rd (+3.3) under the 27.7 bound — it removes the band.

**For a stranger:** of the open corpus's 4,499 Zigbee device definitions, HomeSynapse fully handles about 3 in 10 — nearly all white bulbs; no color bulbs (out of V1 scope by ruling), buttons, or metering plugs (ENERGY-READ is chartered). Twelve ranked rows (≈27.5 lane-days, mostly est.) reach 88.7 %; the last 6.4 % is vendor-specific.

## §1 The corpus counts
| measure (z v26.110.0) | count |
|---|---|
| definitions · vendor files · vendor strings · white labels (not counted) | 4,499 · 393 · 460 · 1,226 |
| vendors | Philips 601 (13.4 %) · Tuya 442 (9.8) · Aqara 171 (3.8) · Innr 119 · IKEA 100 · Gledopto 93; top 10 = 40.7 % |
| capabilities (definitions exposing) | on/off 2,731 (60.7 %) · brightness 1,704 (37.9) · battery 1,140 (25.3) · CT 1,121 (24.9) · xy/hs 677 (15.0) · action 650 (14.4) · electrical 469 (10.4) · temperature 453 (10.1) · humidity 286 (6.4) · thermostat 249 (5.5) · occupancy 203 · illuminance 196 · tamper 190 · cover 165 · contact 131 · leak 78 · presence 74 · air 60 · smoke 52 · lock 50 · gas/CO 48 · pressure 41 · soil 37 |
| clusters read (non-`ignore_*` converters) | 0x0006 2,796 (62.1 %) · 0x0008 1,914 (42.5) · 0x0300 1,229 (27.3) · 0x0001 962 (21.4) · 0xEF00 745 (16.6) · 0x0500 423 (9.4) · 0x0402 375 · 0x0702 315 · 0x0B04 260 · 0x0405 227 · 0x0201 159 · 0x0102 126 · 0x0400 122 · 0x0406 69; 56 standard + 147 vendor clusters |
| device types | a fingerprint `deviceID` on 45 definitions (1.0 %) — not a measure |
| quirks | capability off standard clusters 849 (18.9 %); quirk-bound (that, or an adopt step) 1,138 (25.3); magic packet 716 (15.9); zh Tuya pattern 725 (16.1); zh lumi pattern 186 (4.1); DP maps 482 defs / 5,693 rows; manufacturer-code configure writes 152 (3.4); battery from voltage 186, undivided 45 |
| extends (tag source) | `m.light` 1,287 · `m.onOff` 462 · `m.battery` 426 · `m.electricityMeter` 206 · `m.temperature` 197 · `m.iasZoneAlarm` 153 · `m.illuminance` 112 · `tuyaBase` 636 · `fz.battery` 455 |

**Rule.** Each dist definition → `prepareDefinition` (z `src/index.ts:420`); exposes evaluated on `{isDummyDevice: true}` as z does (`:449`). A capability = a STATE feature, not `config`, not `diagnostic` unless `action`/`battery`, in the 29 classes; standard-sourced iff a non-`ignore_*` converter reads its ZCL cluster (IAS: any frame type), else Tuya/lumi/vendor. **Read:** all standard-sourced with a HEAD handler, battery neither voltage-derived nor undivided. **Classify:** the `EndpointClassifier` arms, simulated per expose endpoint, yield every capability. **Adopt:** no magic packet, no zh lumi quirk, no Green Power (C-002/C-003 cover both roles). Nothing beyond battery = not covered (103).

| category (capability set) | n (share %) | read | classify | adopt | all |
|---|---|---|---|---|---|
| color light | 677 (15.0) | 0 | 0 | 99 | **0** |
| on/off switch·plug | 653 (14.5) | 64 | 60 | 61 | **45** |
| dimmable light | 550 (12.2) | 82 | 82 | 94 | **80** |
| white-ambiance light | 469 (10.4) | 99 | 99 | 95 | **95** |
| remote/button | 358 (8.0) | 0 | 0 | 81 | **0** |
| metered on/off | 297 (6.6) | 0 | 0 | 66 | **0** |
| thermostat | 249 (5.5) | 0 | 0 | 64 | **0** |
| temp/humidity | 191 (4.2) | 51 | 58 | 78 | **48** |
| cover | 165 (3.7) | 0 | 0 | 62 | **0** |
| motion | 163 (3.6) | 25 | 27 | 84 | **22** |
| contact | 127 (2.8) | 31 | 31 | 91 | **28** |
| tail (alarms, leak, presence, meters, locks, …) | 600 (13.3) | ≤46 | 0 | 12–100 | **0** |

## §2 The gap list — greedy by coverage unlocked per lane-day (blocks = share carrying the gap; +pp at its rank → cumulative)
| # | gap | blocks → +pp | HEAD lines that change | INSTRUMENT | device | dependency | lane-days |
|---|---|---|---|---|---|---|---|
| 1 | full color (xy/hs) | 15.0 % → +14.5 (44.2) | `ColorControlHandler.java:22–23,:44–50` (xy/hs ignored); `EndpointClassifier.java:124–126` (CT attached on any 0x0300 — wrong on xy-only); `StandardCapabilities.java:68–86` | fixture replay: currentX/Y + colorMode ⇒ `color_xy`; a bench `set_color_xy`, tolerance verdict | Hue LCA017 (rig; `color_capabilities=31`, Doc 02:285) | AMD-96 (V1 white/CT; Doc 02:283 reserves `color_hs`/`color_xy`) — a word | 2.5 est. |
| 2 | IAS completion: zone types + status bits | 7.5 → +3.7 (47.9) | `EndpointClassifier.java:175–178` (IR-15); `ZoneType.java:23–35` (five; CO/generic/SOS ignored at `ZclIngestionUnit.java:677–683` ⇒ MOTION ⇒ `detected`); `IasZoneHandler.java:30–31,:67–71` (bit 0 only) | IR-15's enrol replay + 0x002B; a zoneStatus frame with bit 2 ⇒ `tamper` | SNZB-04P (rig; z `sonoff.ts:9540` exposes tamper); TR WL2 (fenced) | IR-15 (the fence) | 1 (IR-15 ½ + ½ est.) |
| 3 | metering (ENERGY-READ) | 10.4 → +5.3 (53.2) | `ClusterHandlers.java:37–52`; `EndpointClassifier.java:41,:99–101` (IR-24); `ReportingConfigurator.java:71–72` (IR-25) | `metering-known-load.yaml` + the dossier fixture (divisors 1/10/100) | Gen4 ×2 (owned), TR Gen3, PN2000/P4460 | IR-17/24/25; THE ADOPTION FENCE | 2 (IR-17) |
| 4 | Tuya magic packet (adopt) | 15.7 → +3.1 (56.3) | `InterviewStateMachine.java:160–169` (4 Basic attributes, no vendor step) vs z `lib/tuya.ts:1325`, zh `device.ts:990–1009` | unit test: a `_TZ*` interview sends the extended Basic read; a TS011F-class join then reports | none (DEVICE-SET refused Tuya) | AM-10; a purchase | 1 est. + a sitting |
| 5 | buttons (`action`) | 14.4 → +6.9 (63.1) | `ZclIngestionUnit.java:577–579` (other cluster-specific commands dropped); `EndpointClassifier.java:194–197` | fixture replay of SNZB-01P on/off/toggle ⇒ a press record; a press block | SNZB-01P (rig) | BTN-AMD (post-gate) | 2.5 est. |
| 6 | battery quirks | 4.4 → +1.8 (65.0) | `PowerConfigurationHandler.java:25,:41–53` (0x0021 only, always ÷2) | fixture replay: a 0x0020-only and a 0–100 unit ⇒ correct `battery_pct` | none | a profile flag | 1 est. |
| 7 | classify by clusters | 3.9 (9.4 at the bound) → +2.5 (67.5) | `EndpointClassifier.java:91–104`, `:150–165` (0x0107 drops 0x0402/0x0400), `:180–203` (no temperature arm; battery dropped on switch arms) | unit tests on recorded signatures: SML003 EP2 ⇒ temperature; Gen4 0x010A ⇒ meters; SNZB-02P unchanged | SML003 (EXTENDED), Gen4 | IR-24 (fold); IR-20 measures types | 1 (IR-24) |
| 8 | illuminance | 4.4 → +1.4 (68.9) | `ClusterHandlers.java:37–52`; capability exists (`StandardCapabilities.java:294`); no arm, no reporting row | fixture replay of 0x0400 (log scale) ⇒ `illuminance_lux`; a lux block | SNZB-06P24, SML003 | IR-18 | ½ (IR-18) |
| 9 | Tuya DP codec | 12.6 → +8.2 (77.1) | `TuyaDpCodec.java:27` (marker, no implementation); EF00 falls to `ZclIngestionUnit.java:577–579` | fixture replay per DP map; one TS0601 on the rig | none | AM-10; DP-D (Doc 08 §3.8); §4 | 4 (AM-10) + map rows |
| 10 | covers | 3.7 → +3.1 (80.2) | no 0x0102 handler; `cover` reserved (Doc 02:283) | fixture replay of currentPositionLiftPercentage; a move with a position verdict | none | an AMD + an AMD-97 block | 3 est. |
| 11 | lumi codec + interview tolerance | 4.0 → +3.8 (84.0) | `XiaomiTlvCodec.java:31` (marker); `InterviewStateMachine.java:101–106` (a node-descriptor miss fails; zh `device.ts:917–922` tolerates `lumi.*`) | fixture replay of 0xFF01/0xFCC0 TLV; one Aqara end device | none | AM-10 | 4 (AM-10) |
| 12 | thermostats | 5.5 → +4.7 (88.7) | no 0x0201 handler; `thermostat_control`/`hvac_mode` reserved (Doc 02:283) | fixture replay; a device | none (§3) | an AMD | 5 est. |

Tail (13–18, each ≤ +1.0 pp): soil (1), air quality (1.5; AM-4), pressure (1; a new capability), fan (1.5), lock (3), siren (1.5) → **ceiling 93.6 %**. Unrankable (6.4 %, overlapping): 184 vendor-cluster, 39 battery-only, 64 capability-less, 13 Green Power definitions.

## §3 The market column (Best Buy best-selling sort, fetched 2026-09-17 CT)
| category | device (page) | z row | ZCL? | rank effect |
|---|---|---|---|---|
| color light | Hue A19 75W White and Color Ambiance, SKU 6472191, model 563254, "Best Selling", 592 reviews [b1] | `philips.ts:1598` family (12 color A19/E26, all standard) | standard | #1 holds |
| switch/plug | Hue Smart Plug, SKU 6367452, 552349, "Best Selling" [b2] | `philips.ts:3255` LOM002 | standard; covered | — |
| dimmable | Hue A19 Starter Kit – White, SKU 6472230, "Best Selling" [b3] | `philips.ts:165` family (17, covered) | standard | — |
| white ambiance | unranked (color rows fill the pages) | `philips.ts:325` family (16, covered) | standard | — |
| remote | Hue Dimmer Switch, SKU 6454394, 562777, first, 495 reviews [b4] | `philips.ts:2953` RWL022 | standard commands | #5 holds |
| metered on/off | Shelly Plug US Gen4, SKU 11673596 — first but Sponsored [b5]; 9th unlabelled [b6] | `shelly.ts:2883` | standard | #3 holds |
| thermostat | none — the rows are Wi-Fi (Nest 6427015, Amazon 6483323, ecobee) [b7] | — | — | #12 down |
| temp/humidity | Shelly BLU H&T ZB, SKU 12657322, unreviewed, 5th [b6] | `shelly.ts:3112` (modelID "BLU H&T ZB") | standard; covered | — |
| cover | none — no row names Zigbee [b8] | — | — | #10 down |
| motion | Hue Motion Sensor, SKU 13006990, 570977, "Best selling", Zigbee + daylight sensor [b9] | `philips.ts:3162` SML003 family | standard | #7–8 up |

The only quirk-bound device on any page: the Aqara T1 door sensor (SKU 6568829, first under "zigbee sensor" [b10]; `lumi.ts:4138`). The rows are Hue and Shelly, standard ZCL: color, buttons, metering, motion up; thermostats, covers, Tuya down.

## §4 Refused, in writing
- **Matter/Thread** as a second radio (plan §7). Shelly Gen4 rows count only as Zigbee.
- **Tuya EF00 as a class.** It blocks 12.6 % (565 definitions, 1,368 fingerprints); refusing it caps the ceiling at 81.2 % (93.6 with it; 76.8 without the magic packet too). The plan names no coverage target, so it stays refused: the number is 12.4 pp.
- **Green Power** (13; `InterviewStateMachine.java:121–126`; Doc 08 §14; map R-6): no instrument.
- **The vendor-cluster tail** (184; 44 clusters) and **functions outside the vocabulary** (IR blasters, SET-only sirens, scales, routers: 103): no single instrument.
- **Locks in October**: an irreversible actuator with no device.
- **Install codes, Touchlink**: unmarked in z (Doc 08:958, :1030).

## §5 Unverified
- Device types: 92 covered definitions ride the 0x0302 assumption (the 27.7 bound); IR-20's interview line would measure it.
- SKU→z rows are matched by description (z carries none of 563254/552349/570977/562777); the sort mixes in sponsored rows.
- amazon.com/Best-Sellers-Smart-Plugs/zgbs/hi/21224163011, walmart.com/search?q=zigbee and target.com/s?searchTerm=zigbee are robots-blocked; homedepot.com's Hue listing 404s. The Tuya/Aqara volume channel is unmeasured.
- Coverage is per definition, not per unit sold.
- ZLL-profile (0xC05E) frames drop at `ZclIngestionUnit.java:444–455`; which devices send them is unmeasured.
- The factory-new join is silicon-verified only in `EzspCoordinatorProtocol.java:181–185`; C-002/C-003 are rejoins.
- zh `device.ts:935` keys a quirk on "SNZB-01" (unanchored: matches SNZB-01P); its bearing on F-R4c-A is unread.
- Scripts not persisted (one file); §1's rule re-derives the counts; "est." = this lane's lane-days.

## §6 What this changes in the plan of record
- **Add (IR candidates):** IAS completion (zone types beyond five, status bits) folded into IR-15's WU · IR-24 widened to classify-by-clusters · battery quirks · the magic packet as a profile-keyed interview step · an executor for `InitializationWrite` — parsed (`ZigbeeProfileLoader.java:237`), run by nothing in main, so Doc 08 §3.6's Aqara example cannot run (152 z definitions pass a manufacturer code in `configure`).
- **Two words for Nick:** the two largest unlocks are fenced by scope, not code — color (AMD-96, +14.5 pp) and buttons (BTN-AMD, +6.9).
- **Correct:** Doc 08:260 and AM-10 put quirk-bound devices at "~40 %"; z says 25.3 % of definitions (18.9 % with a capability off standard clusters).
- **Drop:** P2 as a coverage argument · thermostats and covers from October (no US Zigbee listing) · LINK-READ as a coverage lever (link quality is not a corpus capability; it stays a depth row).

[b1]: https://www.bestbuy.com/site/searchpage.jsp?st=philips+hue+white+a19&sp=-bestsellingsort
[b2]: https://www.bestbuy.com/site/searchpage.jsp?st=philips+hue+smart+plug&sp=-bestsellingsort
[b3]: https://www.bestbuy.com/site/searchpage.jsp?st=hue+white+ambiance&sp=-bestsellingsort
[b4]: https://www.bestbuy.com/site/searchpage.jsp?st=philips+hue+switch&sp=-bestsellingsort
[b5]: https://www.bestbuy.com/site/searchpage.jsp?st=zigbee+smart+plug&sp=-bestsellingsort
[b6]: https://www.bestbuy.com/site/searchpage.jsp?st=zigbee&sp=-bestsellingsort
[b7]: https://www.bestbuy.com/site/searchpage.jsp?st=zigbee+thermostat&sp=-bestsellingsort
[b8]: https://www.bestbuy.com/site/searchpage.jsp?st=zigbee+smart+blinds&sp=-bestsellingsort
[b9]: https://www.bestbuy.com/site/searchpage.jsp?st=philips+hue+motion+sensor&sp=-bestsellingsort
[b10]: https://www.bestbuy.com/site/searchpage.jsp?st=zigbee+sensor&sp=-bestsellingsort
[z]: https://github.com/Koenkk/zigbee-herdsman-converters/tree/v26.110.0/src
[zh]: https://github.com/Koenkk/zigbee-herdsman/blob/v10.9.3/src/controller/model/device.ts

RETURNED nexsys-hivemind/context/research/2026-09-17_ZIGBEE-GAPS_return.md 15972
