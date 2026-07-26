<!--
file: context/handoff/2026-07-22_rosonway-topology-move_I3b_operator-package.md
purpose: Operator package — the Rosonway dongle-behind-hub topology move + the I3b [S] hub-attached reenumeration leg. Authored from Nick's 2026-07-22 block plan (recorded verbatim in context/decisions/2026-07-22_nick-rulings-1-5_verbatim.md, ruling 3) per playbook sect-8.
audience: Nick (one bench evening); any Cowork session guiding him runs THIS file block-by-block.
status: READY. Preconditions: boot-health GREEN standing (of record 2026-07-22); NO deploy, config edit, or other physical change in flight; NOT the same evening as the CMD-API deploy session (A4/H4 fold there — variables stay separated).
semantics-correction (hub, 2026-07-22 — instrument-semantics class, playbook sect-8): Nick's draft Block 2 expected "ZERO proposes/relinks." CORRECTED: `device_relinked` x6 IS the lawful NORMAL-boot signature (registry rehydration relink — boot-health itself asserts device_relinked >= 2; zero relinks would FAIL the floor). The rejoin-indicating tokens to expect ZERO of are: `device_proposed`, `UNSECURED_JOIN`, `permit_join_opened`, device announces.
-->

# Operator Package — Rosonway Move + I3b (one evening, single-variable)

**Goal:** prove the coordinator behind the powered Rosonway hub changes NOTHING (boot-health green before AND after), then close **I3b [S]** with the hub-attached reenumeration leg.
**Done-when:** Block-3 `[PASS]` + Block-4 `[PASS] 3/3` pastes are in the hub's hands. ⏺ EVERY block, either way — a FAIL paste is a finding, not a failure.

## Block 0 — the floor, BEFORE (~5 min)
1. Confirm nothing else is in flight (no deploy, no config edit, no other cable change tonight).
2. Run: `~/bench.sh scenario boot-health` (the exact invocation of your 2026-07-22 [PASS] of record).
3. Expect: `[PASS] boot-health — 6/6 positive · 0 forbidden`. ⏺ paste.
   ⛔ Anything but [PASS] => STOP. The floor must be green before the variable changes.

## Block 1 — the move (app STOPPED first)
1. Stop the app cleanly (your practiced SIGTERM stop — same as every bench close). Wait for full shutdown.
2. Coordinator dongle OUT of the Pi's direct port. Keep its extension cable + antenna separation intact (never stacked on USB-3; ~1 m from any WiFi radiator — the AN1017 discipline).
3. Rosonway RSH-A107C on its OWN PSU (powered mode) -> into a Pi **USB-2** port.
4. Dongle (with its extension cable) -> into a Rosonway port.
5. ANTI-ACTIONS: no other cabling changes; no config edits; no battery pulls; the Gen4 plugs stay off-network as always.

## Block 2 — boot + identity glance
1. Start the app (practiced start). Watch the boot log.
2. Expect, in the practiced envelope (log tokens unless noted):
   - `/dev/zigbee` resolves (the udev symlink survives the new USB path). ⛔ If it does NOT resolve: STOP + ⏺ paste `ls -l /dev/zigbee*` + `dmesg | tail -30`. That is a udev-rule finding, not a retry.
   - RADIO UP in the practiced ~11-13 s window; `port_identity_captured` present.
   - `registry.projection_live devices=6 entities=6` (boot-once token) and `adoption_maps_rehydrated: devices=6` (boot-once).
   - `network_resumed channel=20 panId=0x774c`.
   - **`device_relinked` x6 — EXPECTED (lawful rehydration; the normal-boot signature).**
   - ZERO of: `device_proposed`, `UNSECURED_JOIN`, `permit_join_opened` (a pure transport-path change causes no rejoin).
   - Availability returns on the warm envelope (minutes-scale; ping-resolution — do not out-wait it here, Block 3's scenario is the verdict instrument).
3. ⏺ paste the boot block.

## Block 3 — the floor, AFTER
1. Run: `~/bench.sh scenario boot-health`.
2. Expect `[PASS] boot-health — 6/6 positive · 0 forbidden`. ⏺ paste = **the topology change is proven clean, single-variable.**
   ⛔ [FAIL] => STOP, ⏺ paste, no further physical changes; the hub adjudicates (the likely classes: udev path, power budget, USB-3 interference).

## Block 4 — I3b [S], the hub-attached reenumeration leg
1. Run: `~/bench.sh scenario usb-reenumeration-manual` (same invocation as the I3a rep). When the scenario directs the physical act: pull/replug the dongle **at the ROSONWAY port** (not the Pi).
2. Expect: instant detection; autonomous reopen in the 16-17 s envelope; `[PASS] usb-reenumeration-manual 3/3 · 0 forbidden`; outcomes QUOTED in the runner output.
3. ⏺ paste either way -> **I3b [S] closes on this paste.**

## Block 5 — close
1. The topology is now STANDING. The bench-constants `usb-power` flip records at the NEXT constants re-mint (rides B2 — do not edit constants tonight).
2. The AUTO usb scenario (scripted cut via a stimulus plug feeding the Rosonway) stays post-CMD-API as sequenced.
3. All pastes -> the hub next turn; they are corpus material (the ratchet rule).
