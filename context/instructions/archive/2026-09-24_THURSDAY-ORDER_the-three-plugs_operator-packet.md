<!--
file: context/instructions/2026-09-24_THURSDAY-ORDER_the-three-plugs_operator-packet.md
purpose: THE THURSDAY ORDER (the v76 b7 audit §0) cut as one-command cards through THE PRIOR-LEDGER GATE, at the bytes of the Pi as read 2026-09-23T12:08:46Z. Half 1 (T-A → T3: the Gen4s into Zigbee, the pre-read, the pairing window, the adoption, the capture) is cut here, whole; Half 2 (T4 → T8: the constants re-mint, the pull, boot-health, the scenario in tmux, the capture) is cut by the hub at the re-mint beat from T3's capture, because its values are read after the adoption, never predicted.
audience: Nick (at the rig; §1 then the cards in order) · the hub (the re-mint beat reads §3 and the capture)
state-type: operator packet (hardware session — exclusive; one card at a time)
status: EXECUTED — Half 1 run Fri 2026-09-25 (20:00–20:15 CT; 1 of 3 adopted) + T2b (both Gen4 adopted by "Start pairing"); Half 2 T4–T6 EXECUTED (bench `a45686f` · `df4a2d7`); T7–T8 SUPERSEDED by v81's METER-2 re-cut (v80 b4, 2026-09-26T03:40:57Z). Was: DISPATCH-READY v79 beat 3 (Wed 2026-09-23 ~07:2x CT; instrument 2026-09-23T12:21:57Z).
-->

# THE THURSDAY ORDER — the three plugs (Thu 2026-09-24)

## §0 The order on one screen
**Half 1 (this packet):** T-A the two Gen4s into Zigbee + tmux on the Pi → T0 the pre-read and the one backup → T1 the pairing window (G4-1 · TR3 · G4-2, one at a time) → T2 the adoption list from the plugs' own log lines, then one power-cycle per plug → T3 the window closed and the capture home.
**Half 2 (the hub cuts it on T3's capture):** T4 the constants re-mint (the bench card) → T5 the Pi's pull → T6 boot-health on the new counts + the drift cmp → T7 the scenario in tmux (CHAR-BEFORE IS THE CHAR) → T8 the capture home. **Friday:** the digest read → BENCH-CORE-3.
**At every card:** it names its prompt (every rig command runs from **Git Bash on the desktop**, through `ssh pi`; no open ssh session to paste into) · one device at a time, each act confirmed by its own log line before the next · the S31 is not touched · a `STOP` line means nothing was written and nothing restarted — say it back as printed.

## §1 Before T-A (the bench, physically)
- The S31 stays OFF and unloaded; nothing else from the box is powered.
- Stick a label on each Gen4: **G4-1**, **G4-2**. The TR3 is the Third Reality plug.
- The LAMP is the two 40 W appliance lamps lit together — 80 W (`metering-known-load.yaml:15–:16`); the P4460 (A), B1 and B2, the CHAR sheet and the rep sheet at hand for Half 2.
- Two variables every card uses (paste once per Git Bash window):
```
D=~/Desktop/Code/ClaudeFolder/_scratch/thu0924; S=~/Desktop/Code/ClaudeFolder/nexsys-hivemind/context/instructions/2026-09-24_THURSDAY-ORDER_scripts; mkdir -p $D
```

## §2 Half 1 — the cards

### T-A — the Gen4s into Zigbee; tmux on the Pi
1. **Each Gen4 (G4-1, then G4-2):** in the Shelly app or the plug's local web interface — put it on your Wi-Fi, update to the newest firmware it offers (at least 2.0.0: "Fix excessive power measurements reporting", DEVICE-SET note 4), write the version down, then **Settings → Switch to Zigbee** (Shelly: "Firmware switching can only be done via the local web interface: Settings → Switch to Matter/Zigbee"). It reboots in Zigbee mode; it cannot join our network until T1 opens the window.
2. **tmux on the Pi (Git Bash):**
```
ssh -t pi 'sudo apt-get install -y tmux && tmux -V'
```
(If the homesynapse login has no sudo, run the same command from your admin login on hs-dev-1.)
Say back: `T-A: G4-1 <fw> · G4-2 <fw> · Zigbee · tmux <version>`

### T0 — the pre-read and the one backup (Git Bash)
```
ssh pi 'bash -s' < $S/T0.sh > $D/T0.txt 2>&1; tail -4 $D/T0.txt
```
Read: `== tmux: /usr/bin/tmux` · `entities rows 6 devices 6` · `T0-END`, and in the file `BACKUP WRITTEN` (or `KEPT`), `adopt_devices: 6`, the carrier `a239bd60b40a · live-basis IDENTICAL`. **Stop** and say it back if the nightly line is anything but `8/9 PASS` or `7/9 · FAIL command-confirm-s31`.
Say back: `T0: T0-END`

### T1 — the pairing window, then the three named acts (Git Bash; one command: the window boot, then the watcher)
```
ssh pi 'bash -s' < $S/T1.sh > $D/T1.txt 2>&1; tail -3 $D/T1.txt; grep -q T1-END $D/T1.txt && ssh pi 'timeout 240 tail -n +1 -F ~/hs-bench/current.log | grep --line-buffered -E "permit_join_opened|device_proposed|interview_"'
```
The window opens at this boot and closes 254 s later. As soon as the watcher prints `zigbee.permit_join_opened: duration=254s`:
1. **G4-1** into a wall outlet near the Pi → **3 quick presses** of its button → wait for its line `zigbee.device_proposed: device=0x… manufacturer=… model=…`.
2. **TR3** into an outlet → **hold its On/Off button more than 10 s** until the LED flashes red → wait for its line.
3. **G4-2** → **3 quick presses** → its line.
If the window runs out first, run the card again (the key is kept; a new window opens) and pair only the missing plug.
Say back: `PAIRED: G4-1 · TR3 · G4-2`

### T2 — the adoption list from the plugs' own lines, then one power-cycle each (Git Bash; one command)
```
ssh pi 'bash -s' < $S/T2.sh > $D/T2.txt 2>&1; grep -E 'PROPOSED|NOTE|ADOPT|STOP|Error|T2-END' $D/T2.txt; grep -q T2-END $D/T2.txt && ssh pi 'timeout 240 tail -n +1 -F ~/hs-bench/current.log | grep --line-buffered -E "proposal_accepted|device_adopted|proposal_incomplete|interview_|metering_formatting_read|reporting_configured"'
```
Read: three `PROPOSED` lines (Shelly · Third Reality · Shelly) · `ADOPT LIST WRITTEN: 6 + 3` · `T2-END`. The window is open at this boot too. Then, one at a time:
1. **G4-1:** unplug, count 10, plug back → `zigbee.proposal_accepted: device=<its IEEE>` then `zigbee.device_adopted: … deviceId=… entities=…`. Nothing within 60 s → 3 quick presses.
2. **TR3:** the same (fallback: hold more than 10 s).
3. **G4-2:** the same.
Say back: `ADOPTED: 3`

### T3 — the window closed, the capture home (Git Bash; one command)
```
ssh pi 'bash -s' < $S/T3.sh > $D/T3.txt 2>&1; scp -rq pi:thu0924 $D/pi-capture; tail -5 $D/T3.txt; ls $D/pi-capture | wc -l
```
Read: `WINDOW KEY REMOVED · adopt_devices 9` · `adopted lines: 3 · devices=9 entities=<n> · proposals at the closed boot: 0` · `entities rows <n> devices 9` · `Bearer in the capture: 0` · `T3-END` · the file count.
Say back: `T3: devices 9 · entities <n> · proposals 0 · files <k>` — then the hub cuts Half 2.

## §3 Half 2 — the shape (the hub cuts the cards from T3's capture; every value read, none predicted)
- **T4 the constants re-mint** (`nexsys-bench/scenarios/constants.yaml`, the hub's splice, your bench card): `fleet.devices` · `fleet.entities` · `remembered-ulids` as `/api/v1/entities` lists them after the adoption; `metering.plug-entity` g4-1 · tr3 · g4-2 ← each plug's entity (labels.txt → `device_adopted`'s deviceId → the entity row); the `metering-plug` flag `available: true`; `provenance:` untouched (the b7 audit F-4).
- **T5** the Pi's pull (`git -C ~/nexsys-bench pull --ff-only`) and the banner.
- **T6** `~/bench.sh suite boot-health` → PASS on the new counts (its forbidden `device_proposed` absent); `cmp` carrier vs live-basis → IDENTICAL (§4 P-2).
- **T7** the scenario at an attended TTY: `ssh -t pi`, `tmux new -s metering`, `~/nexsys-bench/tools/bench.sh scenario metering-known-load` (`bench.sh:91` delegates `scenario` to the runner); a second tmux window with the `power_w` watcher for the plug under test (the command carries the three ULIDs); each LOAD STEP by the lamp out of the plug ≥ 15 s and back — the prompt's own alternative, no command path.
- **T8** the bundle and `~/thu0924` home → `context/audits/2026-09-24_THURSDAY-ORDER_capture/` (sha256; Bearer 0).
- **Fri 09-25:** the digest read (boot-health on the new counts; `[OK] drift check`) → BENCH-CORE-3 (core `d22a8a4`: LINK-READ + IR-40 onto the bench card; step 0b re-run).

## §4 What the carrier read changed in the order (THE PREMISE GATE; the Pi at 2026-09-23T12:08:46Z)
- **P-1** The adoption edits `~/hs-bench/config/integrations/zigbee.yaml`. The carrier holds `zigbee: !include integrations/zigbee.yaml` at line 2 and no `adopt_devices`; the b7 audit §0 placed the edit in the carrier.
- **P-2** No regeneration of the hero-less variant or the live-basis. The variant is the carrier with `automations: []` (89 B) and carries the same include, so the carrier's bytes (1,208 B, md5 `a239bd60b40a`, unchanged since 07-09) do not move and the drift guard's `cmp` stays IDENTICAL; the b7 step assumed the edit landed in the carrier. T6 verifies the `cmp` instead.
- **P-3** tmux is ABSENT on the Pi (`command -v tmux`) — the scenario's "RUN IT IN tmux" needs T-A's install.
- **P-4** The Gen4 firmware ("Update both first", DEVICE-SET note 4; the G4-3 row reads "at firmware 2.0.0") and Shelly's Zigbee switch are T-A.
- **P-5** The scenario's prompts name a dashboard toggle; the load step is the lamp out and back.
- **P-6** `~/bench.sh` is a symlink to `~/nexsys-bench/tools/bench.sh`; `restart` waits for `zigbee.network_up` and prints `permit_join_opened` among its health tokens (`bench.sh:40–:66`).
- **The adoption path, at source:** the list is read once at boot and consent is first-adoption-only (`ZigbeeIntegrationAdapter.java:1245–:1264`); every discovery of an unadopted device re-proposes (`ZigbeeAdoptionSlice.java:224–:279`); a listed proposal with a COMPLETE interview adopts (`ZigbeeIntegrationAdapter.java:1094–:1110`). So a plug's IEEE is taken from its own `zigbee.device_proposed` line at T1 and the power-cycle at T2 re-proposes it into the list.

## §5 THE PRIOR-LEDGER GATE — each ledger row and what this packet does about it
| Ledger row (`cut -c1-240`) | The hit | Here |
|---|---|---|
| H8-a D-1 · D-4 | blocks pasted at the wrong prompt | every card names its prompt; every rig command is a desktop `ssh pi` — no open session to paste into |
| H8-a D-2 · R-5B D-1 | `cut -c1-160` truncates the app's line | no cut below 240 anywhere; the capture keeps whole lines and whole boot logs |
| H8-a D-5 · R-5B D-7 | the sshd PATH | scripts run through `bash -s` with absolute paths; tmux checked with `command -v`, never assumed |
| R-5B D-2 | an act on the fenced device | the S31 is not touched; nothing outside the cards |
| R-5B D-3 | the choreography not run as written | one device at a time, three named acts, each confirmed by its own line before the next |
| R-5B D-5 | a row filtered by name strings | rows by deviceId (from `device_adopted`) and entityId, never by name |
| R-5B D-6 | evidence left on the card | T3 copies `~/thu0924` home: the three boot logs, the lines, the entities, the labels, `zigbee.yaml` after; Bearer 0 |
