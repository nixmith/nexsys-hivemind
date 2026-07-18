<!--
file: context/handoff/2026-07-18_joins-night_operator-go-package.md
purpose: The hub's paste-block package for THE JOINS NIGHT — SEED fresh formation (E2 [M] discharge) → Wave-1 rejoin → the four Wave-2 joins → config-gated adoption ×4 → the D1 [M] 5-classes + B2 [M] identity-stability reads. One formation, one night (the one-formation economy). Authored by the v33 hub 2026-07-18; consumed by Nick at the bench (relay to the wave2 operator lane's return file, or paste results into the hub session — either is fine; the wave2 return file is the durable home).
audience: Nick (hands at the bench); the wave2-setup operator lane (its §4 fills from this run); the hub (adjudication).
state-type: operator go-package.
status: ⛔ GATED — DO NOT START until ALL THREE: (1) M9.7-W2 landed on core, CI GREEN on the pushed commit; (2) deployed to the Pi and RE-VERIFIED AT THE PI (Block 0 — deploy-state is re-derived at the instrument, never assumed); (3) the hub's explicit GO word after the M9.7-W2 audit. The instrument's resolution note (the doctrine §3): interviews/joins resolve in seconds; availability resolves at ping-scale minutes — no leg here waits on availability except where stated.
-->

# THE JOINS NIGHT — operator go-package (⛔ gated; run blocks IN ORDER)

**GOAL:** one fresh formation under the generated seed (E2), Wave-1 back on it with identities unchanged (B2), all four Wave-2 devices joined and CORRECTLY adopted (D1 5/5 + D2), every claim evidenced by pasted log/API blocks.
**DONE-WHEN:** Blocks 0–9 each hit their done-when; the ⏺ pastes land (either way — a surprising paste is worth more than a clean one).
**STOP RULE:** any join instability, identity anomaly, unexpected token, or a count that misses its expectation ⇒ ⏺ paste + STOP. Never improvise; the hub adjudicates.

**HONEST STATES — do not panic on:** `availability: UNKNOWN` on fresh joins until first evidence · `key_establishment_failed: TC_REJECTED_APP_KEY_REQUEST` WARNs (the known policy-denial watch class) · sleepy `reporting_configured` with degraded>0 / TIMEOUT-class postures (the 03P 2/3 precedent) · the 04P reporting-verifying only 1/N (IAS is event-driven — NORMAL) · ash CRC noise ×1-class · `zigbee.device_join_failed` for a retrying sleepy device that then succeeds.

**ANTI-ACTIONS (all night):** ZBDongle-P stays STOWED, never powered · the Shelly Gen4 plugs stay OFF-NETWORK and unprovisioned (their Matter/Zigbee radios never join anything, ever) · NO Rosonway/topology moves tonight (that is its own post-joins single-variable step with a boot-health re-run first) · the Hue lamp stays on DIRECT wall power tonight (the S31-inline placement is a post-night act — a plug hiccup must not be able to mask Hue legs) · NO long-press on an already-joined device (long-press = leave/re-pair — only used where a block says so) · no config edits beyond the two named keys · no events-DB or zigbee-devices.json touches.

---

## Block 0 — deploy re-verify AT the Pi (the minted rule)
GOAL: prove the instrument runs M9.7-W2. DONE-WHEN: both reads match the landed commit.
```
git -C ~/homesynapse-core log --oneline -1        # must show the M9.7-W2 commit sha
# after the app is (re)started later, the boot log's Jetty build-SHA banner must agree;
# any mismatch = STOP (the stale-instrument class).
```
⏺ paste the sha line.

## Block 0.5 — the B2 BASELINE (before ANYTHING else changes)
GOAL: bank the pre-night identity truth. DONE-WHEN: the full entity list is saved.
```
curl -s http://<pi>:<port>/api/v1/entities > ~/joins-night-baseline-entities.json && cat ~/joins-night-baseline-entities.json
```
⏺ paste it in full (Wave-1 ULIDs live here — the after-read compares against THIS).

## Block 1 — config preflight (app may be running or stopped; read-only)
GOAL: the two keys are right BEFORE the formation boot. DONE-WHEN: the zigbee section reads as expected.
Print your config's `integrations.zigbee` section. EXPECT: `serial_port: /dev/zigbee` (unchanged) · `permit_join_duration: 254` (ADD it if absent — the joins windows ride it; one window opens per boot) · `adopt_devices:` carrying ONLY the two Wave-1 entries (unchanged tonight until Block 6) · channel key as it stands (do not change it; whatever it reads, the formation logs will tell us the truth).
⏺ paste the section (mask nothing — no secrets live in it).

## Block 2 — custody reset for the SEED formation (app STOPPED)
GOAL: force a FRESH formation under a generated seed (the SD-5/E2 discharge). DONE-WHEN: the three custody files are moved aside; `zigbee-devices.json` is UNTOUCHED.
```
# stop the app your practiced way first (clean SIGTERM), then:
ls -la <data-dir>/zigbee/
# EXPECT to see: zigbee-network.json, secrets.enc, .root-key, zigbee-devices.json
# If the names differ from these four: STOP + paste the listing.
mkdir <data-dir>/zigbee/_pre-seed-backup-20260719
mv <data-dir>/zigbee/zigbee-network.json <data-dir>/zigbee/secrets.enc <data-dir>/zigbee/.root-key <data-dir>/zigbee/_pre-seed-backup-20260719/
ls -la <data-dir>/zigbee/
```
Rationale: params+custody gone ⇒ the boot FORMS fresh and MINTS a new seed; `zigbee-devices.json` preserved ⇒ interview cache + rehydration intact. The backup makes tonight reversible.
⏺ paste both listings.

## Block 3 — boot #1: THE SEED FORMATION
GOAL: fresh network under the generated seed. DONE-WHEN: all five glance-points appear.
Start the app the practiced way. In the log EXPECT, in rough order:
1. `zigbee.tc_link_key_posture: posture=generated_seed context=formation`  ← **THE E2 LINE**
2. a formation/channel line (record channel + panId verbatim — the constants re-mint consumes them)
3. `zigbee.adoption_maps_rehydrated: devices=2`  ← Wave-1 rehydration (count EXACTLY 2)
4. `production_session_started: port=/dev/zigbee`
5. `zigbee.permit_join_opened: duration=254s`
Also EXPECT ABSENT: any hex that could be key material (never logged), any `zigbee.network_key_missing`.
⏺ paste the boot block (first ~40 lines).

## Block 4 — Wave-1 rejoin (+ the S31 gate-crash caveat) — window #1
GOAL: Hue + SNZB-03P on the new network as the SAME identities. DONE-WHEN: two `device_relinked` lines, ZERO `device_proposed` for Wave-1.
1. Re-pair the Hue with the practiced reset (the original bench-up procedure). EXPECT: `zigbee.device_announce: device=0x…` → interview lines → **`zigbee.device_relinked: device=… deviceId=…`** (the registered-device arm — NOT proposed) → `reporting_configured` → availability.
2. Long-press the 03P into pairing. EXPECT the same shape: announce → **relinked** (+ `ias_zone_enrolled` re-appearing is normal).
3. **The S31 may gate-crash this window** (it is powered + factory-fresh and chases the FIRST open permit-join). That is LAWFUL: expect `zigbee.device_join` → `zigbee.device_announce: device=0x…` → interview → **`zigbee.device_proposed: … manufacturer=SONOFF model=S31 Lite zb … COMPLETE`** — and NOTHING adopts (not listed). **⏺ RECORD ITS `device=0x…` EUI-64 — that string is its Block-6 accept-list entry.**
Per-device ⏺: the announce→relink/propose block, pasted.
COUNTS at end of Block 4: `device_relinked` ×2 · `device_proposed` ×0-or-1 (the S31 if it crashed in) · adopted ×0.

## Block 5 — the Wave-2 joins — same window if time remains; else restart for window #2 (each boot re-opens 254 s; a restart between joins is lawful and cheap)
GOAL: all four Wave-2 devices JOINED + interviewed COMPLETE + PROPOSED (adoption comes in Block 7). DONE-WHEN: four `device_proposed … COMPLETE` lines + four EUIs recorded.
Order: **S31 (if not already in) → 02P → 04P → 01P.** One device at a time; wait for its `device_proposed` before the next.
- **S31:** plug in / it joins on its own in an open window. EXPECT propose with `manufacturer=SONOFF model=S31 Lite zb`.
- **02P:** long-press to pair; short wake-presses every ~5 s while interview lines run. EXPECT `manufacturer=eWeLink model=SNZB-02P` COMPLETE. ⏺ record its EUI — bind to printed serial `25471900074240`.
- **04P:** long-press to pair; wake-presses through the interview. EXPECT `model=SNZB-04P` COMPLETE. ⏺ record EUI — bind to serial `25303900144196`. **THEN the CONTACT-LEARN GUARD: bring the magnet to the reed and pull it away ONCE.** EXPECT `zigbee.ias_zone_type_learned: device=… zoneType=CONTACT` (enroll may already have printed it at join — either timing is fine). **If CONTACT has NOT appeared by the end of Block 5: STOP + paste — do NOT proceed to Block 6.** (Adoption is a one-way door; the 04P must classify contact, and the learned zoneType is what makes it.)
- **01P:** long-press to pair; wake-presses. EXPECT `model=SNZB-01P` COMPLETE. ⏺ record EUI. Then press it once — whether a press prints ANYTHING is a characterization read (unbound presses may be silent — an honest finding either way, not a failure).
PARTIAL interviews: a sleepy interview may land PARTIAL — wake-press and power-cycle the device to re-announce/re-interview; paste if it stays PARTIAL after two tries.
⏺ the four propose blocks + the EUI table (device → EUI → serial where printed).

## Block 6 — the accept-list edit (app STOPPED)
GOAL: authorize adoption of exactly the four. DONE-WHEN: `adopt_devices` carries 2 old + 4 new entries.
Stop the app. Append the FOUR recorded EUIs to `adopt_devices` — each EXACTLY as the announce printed it (`0x` + 16 hex — the log's own rendering). Wave-1 entries stay untouched.
⏺ paste the edited `adopt_devices:` list (6 entries).

## Block 7 — boot #2: ADOPTION ×4
GOAL: four correct adoptions. DONE-WHEN: four `device_adopted` lines with the RIGHT entity shapes.
Start the app. EXPECT at boot: `zigbee.adoption_maps_rehydrated: devices=2` (STILL 2 — Wave-2 not yet adopted), `permit_join_opened` (lawful), the posture line now reading `context=restore` with `posture=generated_seed` (the AS-FORMED restore proof — a free E2 bonus read).
Then wake each Wave-2 device to re-announce, one at a time, IN ORDER — power-cycle only (S31: unplug/replug · sensors: battery out/in; **NO long-press — that is a leave**):
Per device EXPECT: `device_announce` → re-interview → `device_proposed … COMPLETE` → **`zigbee.proposal_accepted: device=… source=config`** → **`zigbee.device_adopted: device=… deviceId=… entities=1`** → `zigbee.reporting_configured: device=… clusters=N verified=V degraded=D` (record the counts; sleepy degradation honest) → availability edges.
For the 04P specifically: `ias_zone_type_learned … CONTACT` must be in the log BEFORE its adopted line (re-provoke with one magnet edge pre-reinsert if needed).
COUNTS at end: `proposal_accepted` ×4 · `device_adopted` ×4 (each `entities=1`) · `half_registration_detected` ×0 (its appearance = STOP + paste).
⏺ per-device adoption blocks.

## Block 8 — THE READS (D1 · D2 · B2 · live evidence)
GOAL: the gate evidence. DONE-WHEN: all four reads pasted.
1. **D1/D2 —** `curl -s http://<pi>:<port>/api/v1/entities` ⏺ FULL paste. EXPECT 6 devices' entities; classes: light (Hue) · binary_sensor/occupancy (03P) · **switch (S31)** · **sensor: temperature+humidity+battery (02P)** · **binary_sensor: contact (04P)** · **sensor: battery (01P)**. Availability UNKNOWN on fresh joins is honest.
2. **B2 —** compare Wave-1 entity ULIDs in that read against Block 0.5's baseline: **byte-identical ids**. ⏺ state match/mismatch explicitly.
3. **Live evidence, one per class:** 04P: magnet edge → the contact state flips in a re-read (⏺ before/after values) · 02P: hold it in your hand 60 s → a temperature `state_reported`/value change (may take ~10 s min-interval + report cadence) · S31: press its physical button once → exactly ONE state change, zero commands (the PHYSICAL-origin read) · 01P: one press → whatever the log shows (characterization ⏺).
4. **SEED/I2 glance:** `grep -i "tc_link_key_posture" <log>` (⏺) and confirm no key/seed hex anywhere you pasted.

## Block 9 — close-down hygiene
GOAL: the bench returns to its standing posture. DONE-WHEN: all three done.
1. Stop the app; REMOVE `permit_join_duration` from the config (windows must not re-open on every future boot); start the app; EXPECT: NO `permit_join_opened` line. ⏺ the boot's first ~15 lines.
2. `~/bench.sh scenario boot-health` → EXPECT `[PASS]`. ⏺ either way.
3. Leave everything powered where it sits (placements — S31-inline-with-Hue, 04P door mount — are POST-NIGHT acts the hub sequences separately).

**Hub-side afterwards (not yours tonight):** constants re-mint (`${C.fleet.devices}` 2→6 + the new network constants from Block 3) · corpus entries from the pasted evidence · the wave2 return §4 fill · the M14-condition flip (SEED ✓) on the spine.
