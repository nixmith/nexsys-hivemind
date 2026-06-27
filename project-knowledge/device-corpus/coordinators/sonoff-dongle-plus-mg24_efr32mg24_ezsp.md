<!--
file: project-knowledge/device-corpus/coordinators/sonoff-dongle-plus-mg24_efr32mg24_ezsp.md
purpose: Wave-1 coordinator characterization — SONOFF Dongle Plus MG24 (EFR32MG24 / EZSP). The auto-detect fingerprint feeds M9 coordinator auto-detection (INV-CE-04) and the integration-zigbee scaffold; the EZSP/EmberZNet version is recorded per the brief's protocol-version-mismatch hard-failure class.
brief: context/planning/2026-06-22_hardware-bench-bringup-and-device-characterization_brief.md
validates-against: homesynapse-core-docs/design/08-zigbee-adapter.md §3.2/§3.3 (two-layer coordinator + transport selection); INV-CE-04 (coordinator auto-detection)
schema-version: 1
status: PRE-POPULATED 2026-06-26 (desk research + Doc-08 validation). NOT yet a live-silicon capture — see PROVENANCE.
-->

# SONOFF Dongle Plus MG24 — EFR32MG24 / EZSP

> **PROVENANCE — read first.** This entry is **pre-populated from public reference data** (Sonoff/ITead, the Home Assistant community, the Zigbee2MQTT project) **and validated against Doc 08**. It is **NOT** a capture from the physical stick on the bench. The corpus "is the acceptance spec, **not a simulation**" (brief §1), so every field is tagged:
> - **`[REF]`** — documented from a cited public source; expected to match, but must be confirmed.
> - **`[CONFIRM-ON-BENCH]`** — can only be established from the live stick (exact firmware revision, USB enumeration on *this* host, the EZSP version negotiated at init). Nick fills these from the reference-stack bring-up.
>
> An agent cannot plug in a USB dongle or read live silicon; the physical bring-up is **Nick-driven** (brief audience line). What is front-loaded here is the entire knowledge layer — the expected fingerprint, the firmware-target verdict, and the auto-detect signature — so the bench step is a fast **confirm/correct**, not a from-scratch fill.

## Identity & fingerprint

| Field | Value | Provenance |
|---|---|---|
| Product | SONOFF Zigbee 3.0 USB Dongle **Plus MG24** (model `Dongle-PMG24`) | `[REF]` |
| Radio / SoC | Silicon Labs **EFR32MG24** (1536 KB flash, 256 KB RAM), 2.4 GHz, Zigbee 3.0 + Thread-capable | `[REF]` |
| USB-serial bridge | **CP2102(N)** (Silicon Labs USB-to-UART) | `[REF]` |
| **USB VID:PID** | **`0x10C4` : `0xEA60`** (Silicon Labs CP210x class) | `[REF]` → `[CONFIRM-ON-BENCH]` via `lsusb` / `dmesg` / `/dev/serial/by-id` |
| Serial path hint | `/dev/serial/by-id/usb-Silicon_Labs_CP2102N_USB_to_UART_Bridge_Controller-*` (or `/dev/ttyUSB*`) | `[REF]` → `[CONFIRM-ON-BENCH]` (the `by-id` serial suffix is unit-specific) |
| Stack | **EZSP** (EmberZNet NCP) — ships EZSP by default | `[REF]` |
| **Firmware (default ship)** | **EmberZNet `8.0.2 [GA]`** → **EZSP protocol v14** | `[REF]` → `[CONFIRM-ON-BENCH]` (the stack reports the exact revision at init; firmware batches vary) |

## Firmware-target verdict (Doc 08 §3.3)

Doc 08 §3.3 sets the transport target at **EZSP ≥ v13 / EmberZNet ≥ 7.4** (WARN `zigbee.ezsp_legacy_version` below v13; `PermanentIntegrationException` below v8).

- **Numerically: PASS.** The shipped EmberZNet 8.0.2 negotiates **EZSP v14**, which satisfies "≥ v13." No firmware flash is required for characterization (brief §2 — only flash if *below* target).
- **But this is above the doc's described ceiling → ESCALATION (doc currency).** Doc 08 §3.3 describes its supported generation as "**EZSP version 13 … corresponding to EmberZNet 7.4+** on EFR32MG21/MG24 hardware" and names only **MG21** dongles (ZBDongle-E, HA Connect ZBT-1/ZBT-2) as recommended targets. It does **not** mention **EZSP v14 / EmberZNet 8.x** nor the **MG24 dongle**. The real Wave-1 silicon sits one EZSP generation **above** the band the doc was written and reasoned against. See escalation **ESC-W1-COORD-01** (bench report).
  - *Why it matters (the brief's hard-failure class):* EZSP version negotiation (Doc 08 §3.3, command `0x0000`) and ASH framing must be exercised against **v14** specifically. A documented community failure exists on this exact dongle: **`ASH_ERROR_TIMEOUT` loops** (Zigbee2MQTT issue #30891) — i.e., the ASH transport layer (Doc 08 §3.2/§3.3: stop-and-wait window=1, adaptive 0.4–3.2 s ACK timeout, 5-timeout→FAILED) is the empirical stress point on MG24/v14. Flag for the M9 ASH/EZSP lane as a watch-item.

## Auto-detect signature — feeds M9 INV-CE-04 (Doc 08 §3.3 transport selection)

The ground-truth that distinguishes this path at startup (what M9's auto-detect must key on):

1. **USB descriptor:** CP2102N at `0x10C4:0xEA60` (shared with the MG21 ZBDongle-E — USB VID:PID alone does **not** disambiguate MG21 vs MG24; both present as CP210x). `[REF]`
2. **Probe sequence (Doc 08 §3.3):** ZNP `SYS_PING` SREQ → **no SRSP** (silence/garbage); then EZSP **ASH `RST`** → **`RSTACK`** received ⇒ **transport = EZSP**. `[REF]` → `[CONFIRM-ON-BENCH]` (capture the actual probe bytes).
3. **EZSP version handshake:** response to version command `0x0000` reports **protocol v14 / stack type EmberZNet / stack version 8.0.2**. This is the authoritative path+generation discriminator. `[CONFIRM-ON-BENCH]`

> **INV-CE-04 note:** because the MG24 (EZSP) and the Wave-2 ZBDongle-P (ZNP, CC2652P) share neither stack nor the ZNP `SYS_PING` response, the §3.3 probe order cleanly separates them. The MG21-vs-MG24 ambiguity is *within* the EZSP path and is resolved by the **stack version (8.0.2)**, not the USB ID — record this for the auto-detect lane.

## Characterized on
- Reference stack: `[CONFIRM-ON-BENCH]` — **lead with ZHA (bellows)**, the more mature EZSP path, then cross-check Zigbee2MQTT `exposes` (per brief §0.5 note 1). Record stack + version.
- Host: Raspberry Pi (brief). Use the **USB extension cable** to distance the stick from USB3 (2.4 GHz interference mitigation, brief §2). `[CONFIRM-ON-BENCH]`
- Date characterized: `[CONFIRM-ON-BENCH]`

## Notes (interference, range, coexistence)
- **Reference-stack version gate (EZSP v14):** EZSP **v14** support is *recent* in both reference stacks — zigbee-herdsman `0.51+` / Zigbee2MQTT `1.39+` (`ember` driver), and a current `bellows`/ZHA build (bellows tracked v14 in zigpy/bellows #632). **Use an up-to-date ZHA or Z2M build or the MG24 may fail to initialize** — itself a live demonstration of the EZSP-version-mismatch hard-failure class the brief flags. `[REF]`
- **ASH stability watch:** `ASH_ERROR_TIMEOUT` reports on this dongle (z2m #30891). If seen on the bench, record the firmware revision + host USB topology — it directly informs the M9 ASH layer's timeout/retry tuning.
- **USB3 interference:** extension cable mandatory; note RSSI/LQI on the hero devices with/without it if convenient (feeds §3.11 telemetry expectations).
- **Thread:** latent (Matter-over-Thread border-router capable). **Not exercised — V1 is Zigbee-only** (brief §6 guardrail).
- **Coexistence (Wave-2):** when the ZBDongle-P arrives, confirm both sticks enumerate independently on one host (SPIKE-DC, brief §7).

## Sources (public reference — `[REF]` fields)
- SONOFF Dongle Plus MG24 product + spec: https://sonoff.tech/en-us/products/sonoff-zigbee-thread-usb-dongle-dongle-plus-mg24 ; https://www.cnx-software.com/2025/09/02/sonoff-dongle-plus-mg24-a-zigbee-thread-usb-dongle-based-on-silabs-efr32mg24-soc/
- Default firmware EmberZNet 8.0.2 [GA] / EZSP: https://github.com/Koenkk/zigbee2mqtt/discussions/28697 ; https://community.home-assistant.io/t/itead-s-new-sonoff-dongle-plus-mg24-based-on-silicon-labs-efr32mg24-radio-microcontroller-soc-has-now-been-launched/926690
- ASH_ERROR_TIMEOUT on Dongle-PMG24: https://github.com/Koenkk/zigbee2mqtt/issues/30891
- EZSP v14 ↔ EmberZNet 8.0; EZSP v13 ↔ EmberZNet 7.4.x; ref-stack v8 support: https://github.com/Koenkk/zigbee-herdsman/issues/1093 ; https://github.com/zigpy/bellows/issues/632 ; https://www.zigbee2mqtt.io/guide/adapters/emberznet.html
