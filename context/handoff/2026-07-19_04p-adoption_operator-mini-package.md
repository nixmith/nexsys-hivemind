<!--
file: context/handoff/2026-07-19_04p-adoption_operator-mini-package.md
purpose: The hub's paste-block package for the W2-LEARN silicon leg — the 04P long-press re-pair → the enroll-payload CONTACT learn ON THE WIRE → accept-list → adopt as BINARY_SENSOR/contact → D1 [M] 5/5 → the BENCH-CONST value capture. Two windows, one device, ~15 minutes at the bench.
audience: Nick (hands at the bench); the hub (adjudication on the pastes).
state-type: operator mini-package.
status: ⛔ GATED — DO NOT START until ALL THREE: (1) W2-LEARN landed on core, CI GREEN on the pushed SHA; (2) deployed to the Pi and RE-VERIFIED AT the instrument (Block 0); (3) the hub's GO on the Block-0 paste. Instrument resolution note: joins/enrolls resolve in seconds; no leg here waits on availability.
-->

# The 04P Adoption — operator mini-package (⛔ gated; blocks IN ORDER)

**GOAL:** the 04P adopts as BINARY_SENSOR/`contact` — **D1 [M] 5/5**. **DONE-WHEN:** every ⏺ lands.
**STOP RULE:** any unexpected token, count, or ordering ⇒ ⏺ paste + STOP. Never improvise; the hub adjudicates.
**HONEST STATES (don't panic on):** sleepy retry WARNs · `availability: UNKNOWN` on the fresh join until first evidence · a PARTIAL interview that completes after wake-presses.
**ANTI-ACTIONS:** ZBDongle-P stays STOWED · the Gen4 Shellys stay off-network · no topology moves · **no long-press on any OTHER joined device** · config edits ONLY the two named keys · no events-DB or zigbee-devices.json touches.

**KNOWN-HAZARD (eyes open, the hub's honesty line):** the learned-zoneType map is IN-MEMORY — adoption must consume a learn from its OWN session. Every piece of silicon evidence (3/3 enrollments arrived before any propose on the joins night) plus the end-to-end test pin the enroll-before-adopt ordering, and window #1 verifies the learn fires on the wire BEFORE the 04P is ever accept-listed. But adoption is a ONE-WAY DOOR: **if `device_adopted` ever prints BEFORE `ias_zone_type_learned … CONTACT` within the same session (Block 4): STOP + paste immediately and do NOT re-pair again** — the hub adjudicates before anything else happens.

## Block 0 — deploy re-verify AT the Pi (the minted rule)
After the practiced deploy (pull → build → restart is NOT yet run — just the pull/build; the restart rides Block 2):
```
git -C ~/homesynapse-core log --oneline -1     # must show the W2-LEARN commit sha
```
⏺ paste the sha line. **The hub's GO fires on this paste.**

## Block 1 — config: the window key ON, the list untouched (app STOPPED)
Add `permit_join_duration: 254` back (the joins-night close-down removed it). `adopt_devices` UNTOUCHED this block.
⏺ paste the current `adopt_devices:` list. EXPECT **5 entries** (2 Wave-1 + 02P/01P/S31; the 04P absent). If it shows the 04P already present: **STOP + paste** — the choreography changes and the hub re-rules first.

## Block 2 — boot + window #1: THE WIRE LEARN (the W2-LEARN proof)
Start the app. EXPECT at boot: the log's build/boot banner agrees with Block 0's sha (mismatch = STOP, the stale-instrument class) · `zigbee.adoption_maps_rehydrated: devices=5` · `zigbee.permit_join_opened: duration=254s`.
Long-press the 04P into pairing; short wake-presses every ~5 s through the interview. EXPECT, in order:
1. `zigbee.device_announce: device=0x…` — ⏺ **RECORD THE EUI** (the log's own `0x`+16-hex rendering = the Block-3 accept-list entry)
2. interview lines → `zigbee.ias_zone_enrolled: …`
3. **`zigbee.ias_zone_type_learned: device=… zoneType=CONTACT` ← THE LINE THIS WU EXISTS FOR**
4. `zigbee.device_proposed: … COMPLETE` (unlisted ⇒ nothing adopts — correct)
If CONTACT has NOT printed by the proposal: ⏺ paste the whole arc + **STOP**.
⏺ the announce→propose block.

## Block 3 — accept-list (app STOPPED)
Append the Block-2 EUI to `adopt_devices` EXACTLY as announced. ⏺ paste the edited list (**6 entries**).

## Block 4 — boot + window #2: THE ADOPTION
Start the app (the window re-opens — lawful). **Long-press the 04P AGAIN** (a fresh join ⇒ a fresh enroll ⇒ the learn re-fires in THIS session); wake-presses through the interview. EXPECT, in order:
`device_announce` (same EUI) → interview → `ias_zone_enrolled` → **`ias_zone_type_learned … CONTACT`** → `device_proposed … COMPLETE` → `zigbee.proposal_accepted: … source=config` → **`zigbee.device_adopted: … entities=1`**.
**Ordering watch:** the learned line BEFORE the adopted line (the KNOWN-HAZARD stop rule governs).
⏺ the full arc.

## Block 5 — THE READS (D1 5/5 + the magnet proof)
1. `curl -s http://<pi>:<port>/api/v1/entities` — ⏺ FULL paste. EXPECT **6 devices / 6 entities**; the 04P entity = BINARY_SENSOR carrying **`contact`** (never motion); every pre-existing ULID byte-identical vs the joins-night read (identity stability).
2. One magnet edge at the reed: the contact state flips in a re-read. ⏺ before/after values.
3. Hygiene glances: `grep -c "ias_zone_type_learned" <log>` (⏺ the count) · `grep "ingestion_profile_skipped" <log> | head -3` (⏺ — DEBUG-level diagnostics only; empty at default log level is EXPECTED and healthy).

## Block 6 — close-down + THE BENCH-CONST CAPTURE
1. Stop the app; **REMOVE `permit_join_duration`**; start. EXPECT: NO `permit_join_opened`. ⏺ the boot's first ~15 lines.
2. ⏺ **CAPTURE for the re-mint** (read at the instrument, never assumed — the volatile-baselines law): the boot's `registry.projection_live: devices=… entities=… position=…` line verbatim · the resume line's channel/panId · Block 5's entity count.
3. `~/bench.sh scenario boot-health` — EXPECT **still `[FAIL]`** (the constants pin devices=2; LAWFUL until the re-mint, which the hub authors from step 2's captured values). ⏺ either way.

**Hub-side afterwards (not yours tonight):** the BENCH-CONST re-mint authored from the Block-6 capture (6/6-era values, the `${C.fleet.devices}` fold) → ordered → boot-health GREEN → WUCP P2 (backlog D1-flip + the LEARN-PERSIST candidate row) → CMD-API authoring.
