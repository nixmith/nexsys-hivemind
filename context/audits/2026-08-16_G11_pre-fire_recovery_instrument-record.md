<!--
file: context/audits/2026-08-16_G11_pre-fire_recovery_instrument-record.md
purpose: THE G-11 SANCTIONED RIG RECOVERY — instrument record + hub adjudication. Executed by Nick ~01:08 CT Sun 2026-08-16 (DX-A FIRE-NOW), before the 03:30 CT nightly. Files the verbatim terminal record that resolved DX-13's refutation path: boot-time transport acquisition PROVEN at the fd instrument; the gap narrows to HOTPLUG-ONLY. Chat is not a storage tier (law 34) — this file is the record.
audience: the hub; Nick; THE READ (the D-2 evidence line banks from §3).
state-type: instrument record / evidence bank. Layer-1 evidence + the hub's adjudication; refutation welcome in both directions.
filed: 2026-08-16 ~01:45 CT, the v53 hub (beat 1). Staged in the beat-1 order.
authority: G-11 pre-ruled SANCTIONED RIG RECOVERY (v52 beat 7 / PROJECT_SNAPSHOT): "bench.sh restart + one boot-health = SANCTIONED RIG RECOVERY (not a freeze exception — the freeze froze code and evidence claims, not peripheral recovery)." The timing variation (fire BEFORE the 03:30 nightly rather than after a 3/9) = DX-A, ruled FIRE-NOW by Nick with hub concurrence on the record; grounds: the measured 8.5-hour non-acquisition (the complete record §0) — a system that did not hotplug-acquire in 8.5 h will not in the next 2.5.
L3: no token material appears anywhere in this file.
-->

# G-11 — Pre-Fire Sanctioned Rig Recovery (instrument record)

**Operator:** Nick, all acts on the Pi terminal. **Hub:** adjudication only. **Freeze:** the act is inside G-11's sanction; nothing else was touched (operator word; hivemind porcelain carries only this order's expected files; core porcelain unchanged).

## §1 The verbatim record (operator terminal, transcribed)

### ⏺ 1a — pre-restart fd check (DX-13's pre-state, re-proven)

```
homesynapse@hs-dev-1:~ $ for p in $(pgrep java); do echo "== pid $p =="; ls -l /proc/$p/fd 2>/dev/null | grep -i ttyUSB || echo "  (no ttyUSB fd)"; done
== pid 9767 ==
  (no ttyUSB fd)
```

### ⏺ 1b — the recovery + boot-health (key tokens; full output in the operator transcript, bundle on the Pi)

```
homesynapse@hs-dev-1:~ $ /home/homesynapse/bench.sh restart
/home/homesynapse/bench.sh scenario boot-health
  [OK] stopped
  [OK] launched pid 14600 -> /home/homesynapse/hs-bench/bench-2026-08-16-020814.log
  [--] waiting for a decisive radio state (up to 90 s)...
  [OK] RADIO UP after 12s
02:08:18.307 [hs-sub-registry_projection] INFO  c.h.l.RegistryProjectionSubscriber -- registry.projection_live: devices=6 entities=6 position=25065
02:08:18.711..713 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: x6 — re-pairing, no new adoption
02:08:18.713 [integration-supervisor-start] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.adoption_maps_rehydrated: devices=6
02:08:26.470 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
02:08:26.471 [integration-zigbee-0] INFO  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.network_up: stackStatusHandler reported EMBER_NETWORK_UP (buffered)
runner B3.1-2026-08-02-postwindow @ 16e672d
  [--] stimulus bench: restart
  [OK] stopped
  [OK] launched pid 14718 -> /home/homesynapse/hs-bench/bench-2026-08-16-020833.log
  [OK] RADIO UP after 12s
  (health tokens repeat on the second boot: projection_live 6/6 @ 02:08:37.606 · relinked x6 · maps_rehydrated 6 · network_resumed ch20 panId=0x774c @ 02:08:45.800 · EMBER_NETWORK_UP)
    [ok] log 'registry.projection_live: devices=6 entities=6' min=25065 (within 90s)
    [ok] log 'zigbee.adoption_maps_rehydrated: devices=6' (within 90s)
    [ok] log 'zigbee.device_relinked' x2(at-least) (within 90s)
    [ok] log 'zigbee.network_resumed: channel=20 panId=0x774c' (within 90s)
    [ok] log 'zigbee.port_identity_captured:' same-line ['pinnedOnly=false'] — stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 (within 90s)
    [ok] api /api/v1/entities {"rows": 6, "ulids": ["01KX1PA4HSJ581GASYB7DHE40F", "01KX1PB9AAB4VB3E10BD477TV3", "01KXW0157SP56CCSGJCNDCSQNG", "01KXW13WF0D6TYGN13WXHTG87K", "01KXW1W1SBJZERC9MBAMV2DWKE", "01KY12MQW954E4XYNKH0Y5H8VX"]} — all asserts satisfied (within 90s)
[PASS] boot-health — 6/6 positive · 0 forbidden
  [--] bundle: /home/homesynapse/hs-bench/bundles/boot-health-20260816T060845Z
```

### ⏺ 1c — post-restart fd check (the discriminator)

```
homesynapse@hs-dev-1:~ $ for p in $(pgrep java); do echo "== pid $p =="; ls -l /proc/$p/fd 2>/dev/null | grep -i ttyUSB || echo "  (no ttyUSB fd)"; done
== pid 14718 ==
lrwx------ 1 homesynapse homesynapse 64 Aug 16 02:18 85 -> /dev/ttyUSB0
```

## §2 Adjudication (hub)

1. **boot-health [PASS] 6/6 positive · 0 forbidden** — bundle `boot-health-20260816T060845Z` (06:08:45 UTC = **01:08:45 CT**).
2. **The fd discriminator: post-restart pid 14718 HOLDS fd 85 → `/dev/ttyUSB0`; pre-restart pid 9767 held none.** BOOT-TIME ACQUISITION IS PROVEN at the same instrument that proved the absence (arc-discipline 20 — instrument-first, same instrument both directions). **DX-13 NARROWS TO HOTPLUG-ONLY** — its own named refutation path, executed. NEW-1's scope statement inherits this precision.
3. Port identity captured at the by-id stableId (`pinnedOnly=false`) · network resumed ch 20 / panId 0x774c · RADIO UP after 12 s · 6 devices relinked "re-pairing, no new adoption" (identity durability re-proven live) · registries projection live devices=6 entities=6 · the entities API answered the six known entity ULIDs exact.
4. **Two restarts occurred by construction:** Nick's manual `bench.sh restart` (pid 14600), then the boot-health scenario's own restart stimulus (pid 14718 — the running instance). Both boots came up healthy; the assert set evaluated on the second.
5. **Device vs entity ULIDs — not a discrepancy:** the relink lines carry DEVICE ids (e.g. `01KX1PA4GR…`), the API assert carries ENTITY ids (`01KX1PA4HS…`) — same-millisecond mint pairs, distinct types (decoded: both `01KX1PA4..` → 2026-07-08 15:22:05 CT).
6. **PI-TZ (new datum):** the Pi's displayed local clock runs ONE HOUR AHEAD of CT — the log lines read 02:08 for acts bundle-stamped 06:08Z (= 01:08 CT). Z-stamps are the unambiguous record; the nightly's observed fire time (~08:32Z, 15-night stable) is unmoved by this. Mechanism (TZ config vs skew) undetermined — `timedatectl` at the next Pi trip; routed to the **R-8 batch**. The bench-evening return's F-11 internal-consistency finding stands; this is an offset-vs-CT nuance, not a contradiction.
7. Freeze accounting: the act is inside G-11's sanction — no code, config, constants, YAML, retune, or repo operation.

## §3 The banked D-2 evidence line (§15.2, accepted)

**The first radio-present positive on hop-verified cabling since Aug-13: the full boot floor GREEN (6/6, 0 forbidden) at 01:08 CT on the verified topology** (`3-2.4.2`, by-id stableId, `pinnedOnly=false`, fd held). This line banks in its own right and survives an unreadable digest.

## §4 The standing prediction (Branch 1 LIVE — filed before the fire)

Predict **7–8/9** at the ~03:32 CT fire (hue-online SKIP constant; an honest s31 TIMED_OUT stays inside the chronic-flake band and does not break the reading). A radio-leg collapse on THIS verified rig = a **REAL platform alarm** → an evidence read before the READ; never a retune, never a second restart (arc-discipline 28). **THE READ PROCEEDS in every branch.**

*End. Layer-1 evidence + hub adjudication. No token material. Refutation welcome in both directions.*
