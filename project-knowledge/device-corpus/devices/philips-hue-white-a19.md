<!--
file: project-knowledge/device-corpus/devices/philips-hue-white-a19.md
purpose: Wave-1 device characterization — Philips Hue White-and-Color Ambiance A19 (the hero LIGHT, "motion → light on"). Captures the interview surface and validates it against the HomeSynapse device model (Doc 02 capability set + Doc 08 §3.5 cluster→capability). Surfaces the full-color GAP for hub reconciliation.
brief: context/planning/2026-06-22_hardware-bench-bringup-and-device-characterization_brief.md
validates-against: design/02-device-model-and-capability-system.md §3.5/§3.6/§3.10 ; design/08-zigbee-adapter.md §3.5/§3.10
schema-version: 1
status: PRE-POPULATED 2026-06-26 (desk research + Doc 02/08 validation). NOT yet a live-silicon capture — see PROVENANCE.
-->

# Philips (Signify) Hue White-and-Color Ambiance A19 — light (hero target)

> **PROVENANCE — read first.** Pre-populated from public reference data (Zigbee2MQTT / blakadder / Signify) **and validated against Doc 02/08**. **NOT** a live capture — the corpus "is the acceptance spec, **not a simulation**" (brief §1). Tags: **`[REF]`** = documented from a cited public source; **`[CONFIRM-ON-BENCH]`** = only establishable from the physical unit (exact model variant, firmware/dateCode, reported attribute values, raw interview dump). The physical interview is **Nick-driven**. The **Doc 02/08 validation verdict below is fully computed now** and does not depend on the live capture — only the raw interview values do.

- **Identity:** manufacturer=`Signify Netherlands B.V.` (Basic `ManufacturerName`), manufacturerCode=**`0x100B`** (4107 dec), modelIdentifier=**`LCA0xx`** `[CONFIRM-ON-BENCH]` — `LCA006` = 1100 lm A19; the **"Essential" White-and-Color** 2-pack ships a sibling model id in the same LCA family. *The verdict below is variant-independent — every Hue White-and-Color A19 is an Extended Color Light.* firmware/dateCode/SWBuildID (Basic `0x4000`)=`[CONFIRM-ON-BENCH]`. `[REF]`
- **Characterized on:** path=**EZSP**, coordinator=SONOFF Dongle Plus MG24, refStack=**ZHA (bellows) then Z2M** `[CONFIRM-ON-BENCH]` version, date=`[CONFIRM-ON-BENCH]`
- **Pairs direct?** **YES — direct to the coordinator, no Hue bridge** `[REF]`. If it won't join: factory-reset (power-cycle sequence, or Hue app / Touchlink) and pair close to the coordinator (brief §0.5 note 4). `[CONFIRM-ON-BENCH]`
- **ZCL device type:** **Extended Color Light `0x010D`** (OnOff + LevelControl + ColorControl-full) `[REF]`

## Interview (ground truth)
`[REF]` shape from the Zigbee2MQTT/blakadder reference; **exact attribute values + raw dump = `[CONFIRM-ON-BENCH]`.**

- **Endpoint 11** (Hue light endpoint), profile `0x0104` (HA), device type `0x010D`:
  - **in (server)** clusters: `genBasic 0x0000`, `genIdentify 0x0003`, `genGroups 0x0004`, `genScenes 0x0005`, `genOnOff 0x0006`, `genLevelCtrl 0x0008`, `lightingColorCtrl 0x0300`, `manuSpecificPhilips 0xFC03` (Hue effects/gradient, mfr 0x100B)
  - **out (client)** clusters: `genOta 0x0019`
  - `lightingColorCtrl 0x0300` attributes: `currentHue 0x0000`(Uint8), `currentSaturation 0x0001`(Uint8), `currentX 0x0003`(Uint16), `currentY 0x0004`(Uint16), `colorTemperatureMireds 0x0007`(Uint16), `colorMode 0x0008`(Enum8), `colorCapabilities 0x400A`(Bitmap16 — expect hue/sat + enhanced-hue + XY + color-temp bits set)
- **Endpoint 242**: Green Power (`0x0021`) — standard on Hue, no HomeSynapse capability (out of MVP scope) `[REF]`
- raw dump: `[CONFIRM-ON-BENCH]` — link the ZHA device signature + the Z2M `exposes` JSON here.

## Device-model mapping (Doc 02 §3.6 / Doc 08 §3.5)

| Real cluster / attribute | Expected capability / attribute | Verdict |
|---|---|---|
| `genOnOff 0x0006` · `onOff` | `on_off` · `on` (bool) — Doc 08 §3.5 row; Doc 02 §3.6 | **MATCH** |
| `genLevelCtrl 0x0008` · `currentLevel` (0–254) | `brightness` · `brightness` (0–100 %) — Doc 08 §3.5; Doc 02 §3.6 | **MATCH** |
| `lightingColorCtrl 0x0300` · `colorTemperatureMireds` | `color_temperature` — Doc 08 §3.5 (ColorControl CT row) | **MATCH** (units nuance ↓) |
| `lightingColorCtrl 0x0300` · `currentHue` / `currentSaturation` | `color_hs` | **GAP** ↓ |
| `lightingColorCtrl 0x0300` · `currentX` / `currentY` | `color_xy` | **GAP** ↓ |
| `genGroups 0x0004` / `genScenes 0x0005` | *(no capability — Zigbee groups/scenes out of MVP, Doc 08 §3.10 future)* | N/A (intentional) |
| `manuSpecificPhilips 0xFC03` | *(Hue effects/gradient — non-standard; needs a device profile, Doc 08 §3.6)* | N/A (post-MVP) |

## Validation verdict: **MATCH (MVP-relevant surface) + GAP (full color)** → escalation **ESC-W1-HUE-01**

The hero light's MVP-relevant surface — **`on_off` + `brightness` + `color_temperature`** — maps cleanly and is sufficient for the hero demo (motion → light **on**, and white/CT control). **The hero path is unblocked.**

But the hero hardware is **richer than the MVP device model can represent** (brief §3: "White-AND-Color … characterize all of it"):

1. **Full color is unmapped in Doc 08 §3.5.** The cluster→capability table has a `ColorControl (CT) → color_temperature` row only. There is **no row** translating `currentHue`/`currentSaturation` → `color_hs` or `currentX`/`currentY` → `color_xy`. So the adapter, as specified, cannot surface the Hue's color.
2. **The target capabilities are not in the MVP set.** Doc 02 **§3.6** lists **`color_hs`, `color_xy` as "Post-MVP capabilities (reserved)"** — not part of the MVP sealed capability set.
3. **Doc 02 is internally inconsistent.** Doc 02 **§3.10** lists `color_hs`/`color_xy` among the `light` entity's **optional capabilities** (so a Hue presenting them would *not* trip the §3.10 "unexpected capability" warning) — yet **§3.6** marks them post-MVP/unimplemented and Doc 08 provides no handler. The model both invites and cannot realize color.

This is the **cheap-fix moment** the brief targets (§1 payoff 3): decide **now**, before M9 builds on the abstraction. It is an **escalation, not a bench edit** (write-isolation, brief §6). Disposition is the hub's + Nick's:
- **(A) Scope V1 Hue to White/CT** — accept the GAP as deliberate MVP scoping; document that color is post-MVP; reconcile §3.10 to *not* advertise `color_hs`/`color_xy` as MVP `light` options (fix the internal inconsistency). *Lower effort; matches "V1 stays Zigbee-only / lean."*
- **(B) Pull color forward** — promote `color_hs`/`color_xy` into the MVP sealed set (Doc 02 §3.6) **and** add a `ColorControl(full) → color_hs`/`color_xy` handler row to Doc 08 §3.5 (incl. `colorMode 0x0008` to choose hue/sat vs xy, and `colorCapabilities 0x400A` gating). *Higher effort; delivers full color on the hero device.*

**Secondary nuance (record, not blocking) — color-temp canonical unit.** Doc 08 §3.5 stores `color_temp_mireds` (IntValue) and computes "K = 1,000,000 / mireds **at query time**." Doc 02 §3.6 declares the canonical attribute as **`color_temp_kelvin` (int, K)**, and Doc 02 §3.7's moat rule is "convert to **canonical** units **at ingestion**." Mireds-stored-convert-at-query contradicts Kelvin-canonical-at-ingestion. Minor, but it is exactly the kind of unit-representation drift Doc 02 §3.7 exists to prevent. Fold into the ESC-W1-HUE-01 disposition (pick one canonical representation for color temperature). The hero demo is unaffected.

## Notes / quirks
- Hue bulbs are **mains-powered routers** — they extend the mesh (useful for the SNZB-03P's route once both are paired).
- Hue uses **endpoint 11** for the light (not EP 1) — the interview pipeline (Doc 08 §3.4 step 5 "first application endpoint") must read Basic from the active endpoint, not assume EP 1. `[CONFIRM-ON-BENCH]` that the interview keys on EP 11 correctly.
- `manuSpecificPhilips 0xFC03` and Green Power EP 242 are present but out of MVP scope — note their presence so M9's generic handler ignores them gracefully (no interview failure).

## Sources (public reference — `[REF]` fields)
- Hue White-and-Color A19 / LCA006, Signify mfr 4107 (0x100B), EP11 clusters genOnOff/genLevelCtrl/lightingColorCtrl, direct binding: https://zigbee.blakadder.com/Philips_LCA006.html ; https://github.com/Koenkk/zigbee2mqtt/issues/9860 ; https://www.zigbee2mqtt.io/guide/usage/binding.html
- Hue Essential White-and-Color A19 product line: https://www.philips-hue.com/en-us/p/hue-white-and-color-ambiance-essential-a19-e26-smart-bulb-800-lm-88w/046677592530
