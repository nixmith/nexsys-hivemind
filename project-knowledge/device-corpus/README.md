<!--
file: project-knowledge/device-corpus/README.md
purpose: Index + schema + method for the durable device-characterization corpus. Each entry records a real device's (or coordinator's) ground-truth interview captured on a reference stack, and validates it against the HomeSynapse device model (Doc 02 / Doc 08 §3.5). The corpus is M9's acceptance ground-truth, the regression baseline for every future device, the empirical device-model validation (gaps are now-fixes), and the generalizable method for every future protocol (Matter/MQTT/Z-Wave, Doc 05).
audience: Nick (bench), the PM hub (Doc-gap reconciliation), the M9 Zigbee lane, the Distribution pairing-wizard lane
state-type: durable reference (corpus index)
status: SCAFFOLDED 2026-06-22 (v4 hub) — populate as hardware arrives (Wave 1 ~2026-06-23; Wave 2 ~2026-06-29/30).
brief: context/planning/2026-06-22_hardware-bench-bringup-and-device-characterization_brief.md
schema-version: 1
-->

# Device-Characterization Corpus

Ground-truth Zigbee device + coordinator characterizations, captured on a **reference stack** (Zigbee2MQTT or ZHA) **before M9 exists**, and validated against the HomeSynapse device model. This is durable infrastructure: M9's interview/codec must reproduce these surfaces; future devices are diffed against them; device-model gaps surface here while they are cheap to fix; and the same method onboards Matter/MQTT/Z-Wave later.

## Layout
- `coordinators/` — one entry per coordinator stick (the auto-detect fingerprint feeding M9 INV-CE-04).
- `devices/` — one entry per device archetype (the interview + the device-model validation).

## Index (fill as entries land)

> **Captured legend:** ☐ = none · **◐ = pre-populated from public reference + Doc-02/08-validated, live silicon capture pending** · ✓ = live-captured on the bench. The ◐ entries carry `[REF]` (documented) vs `[CONFIRM-ON-BENCH]` (live-only) field tags; their verdicts are final, only the raw interview values await capture. See `2026-06-23_wave1-benchup-report.md` §0.

| Archetype | Model | Path(s) | Captured | Doc 02/08 verdict |
|---|---|---|---|---|
| Dimmable light (hero target) | Philips Hue White A19 | EZSP (W1) / ZNP (W2) | ◐ W1 | MATCH + **GAP (full color)** — ESC-W1-HUE-01 |
| Motion (hero trigger) | Sonoff SNZB-03P | EZSP (W1) / ZNP (W2) | ◐ W1 | **MATCH** (`occupancy`, not `motion`) — ESC-W1-SNZB03P-01 |
| Contact | Sonoff SNZB-04P | ZNP (W2) | ☐ | ☐ |
| Button / scene | Sonoff SNZB-01P | ZNP (W2) | ☐ | ☐ |
| Smart plug (energy) | Sonoff S31 Lite ZB | ZNP (W2) | ☐ | ☐ |
| Temp / humidity | Sonoff SNZB-02P | ZNP (W2) | ☐ | ☐ |

| Coordinator | Radio / stack | Captured |
|---|---|---|
| Sonoff Dongle Plus MG24 | EFR32MG24 / EZSP | ◐ (EZSP v14 / EmberZNet 8.0.2 — ESC-W1-COORD-01) |
| Sonoff ZBDongle-P | CC2652P / Z-Stack (ZNP) | ☐ |

## Method (per device)
1. Pair + interview on a reference stack (Z2M or ZHA) on the relevant coordinator. Capture the **full** interview (endpoints, in/out clusters, attributes + types, commands) and the raw dump.
2. Fill a `devices/<model>.md` from the template below.
3. **Validate vs the device model:** map each real cluster/attribute to the Doc 02 capability/entity it should surface (Doc 08 §3.5 cluster→capability). Record **MATCH** or **GAP**.
4. **On any GAP:** stop and escalate to the hub — it is a candidate **now-fix** (a Doc 02/08 amendment *before* M9 builds on the abstraction), not an M9-era discovery. Note it in the entry's Validation section AND flag the hub.

## Device entry template
```
# <Manufacturer> <Model> — <archetype>

- Identity: manufacturer=<>, model=<>, manufacturerCode=<0x..>, modelIdentifier=<Basic cluster>, firmware/dateCode=<>
- Characterized on: path=<EZSP|ZNP>, coordinator=<stick>, refStack=<Z2M|ZHA> <version>, date=<>
- Pairs direct? <yes/no — e.g. Hue White expected direct, no bridge>

## Interview (ground truth)
- Endpoint <n>: in clusters [..], out clusters [..]
  - <cluster>: attributes [<name>:<type>, ..], commands [..]
- (raw dump: <link/path>)

## Device-model mapping (Doc 02 / Doc 08 §3.5)
| Real cluster/attribute | Expected capability/entity/attribute | Verdict |
|---|---|---|
| <On/Off> | <switchable / on_off> | MATCH / GAP |

## Validation verdict: <MATCH | GAP — detail + escalation ref>
## Notes / quirks:
```

## Coordinator entry template
```
# <Stick> — <radio> / <stack>

- USB: VID=<0x..> PID=<0x..>, serial path hint=<>
- Radio/chip: <e.g. EFR32MG24>; stack: <EZSP|ZNP>; firmware: <EZSP v.. / EmberZNet .. | Z-Stack ..>
- Firmware target met? EZSP >= v13 / EmberZNet >= 7.4: <yes/no — action if no>
- Auto-detect signature (feeds M9 INV-CE-04): <what distinguishes this path at startup>
- Characterized: refStack=<> version=<>, date=<>
## Notes (interference, range, both-on-one-host coexistence):
```
