<!--
file: context/instructions/2026-09-25_THURSDAY-ORDER_T2b_shelly-recovery_operator-card.md
purpose: THE THURSDAY ORDER's recovery card (T2b): the two Shelly Plug US Gen4 (G4-1 · G4-2) joined at T1 but were NOT adopted at T2 — a power-cycled Gen4 in Zigbee mode resumed its membership silently (no `device_join`, no `device_announce`, no re-proposal at the T2 or T3 boots; the record's premise "the power-cycle at T2 re-proposes it" held for the TR3 only). This card re-opens the window (`T1b.sh`, guarded for the nine-entry list, self-tested on the after-T3 file), measures the silent resume once more per plug, then forces a fresh join from the plug's own side, then closes the window and brings the capture home (T3.sh, unchanged). Half 2 (T4 → T8) is cut from T3b's capture.
audience: Nick (at the rig; one card at a time) · the hub (the intake at T3b's capture)
state-type: operator card (hardware session — exclusive)
status: EXECUTED — Fri 2026-09-25 (both Gen4 adopted inside one window at 21:50 Pi-local; T3b 9/9, Bearer 0) (v80 b4, 2026-09-26T03:40:57Z). Was: DISPATCH-READY v80 beat 2 (Fri 2026-09-25 ~20:4x CT).
-->

# T2b — the Shelly recovery (run tonight, or Saturday morning before anything else at the rig)

## §0 What Friday's capture shows (the hub's read at the bytes)
At the T1 boot both Shellys joined (`device_join … UNSECURED_JOIN`, `device_announce`, `device_proposed … status=COMPLETE`, `key_established`) and the TR3 too. T2 listed all three (`ADOPT LIST WRITTEN: 6 + 3`) and restarted the app. At that boot the TR3 joined afresh when you cycled it (21:10:23) and was adopted (deviceId `01M3DM74RKEQ9H05PAATBMW2MW`, one entity, power divisor 10). **Neither Shelly produced a single line at the T2 or T3 boot** — not a join, not an announce, not a proposal — so the adoption path (which admits a device only from its announce or rejoin, `ZigbeeIntegrationAdapter.java:1309` → `adoptIfAccepted` :1093) never saw them, although the device cache holds them (`device_cache_loaded: 9 devices`). One late `key_establishment_failed … TC_REQUESTER_VERIFY_KEY_TIMEOUT` at 21:11:42 is a join attempt 43 s after the window closed — most likely G4-2's presses. The fleet stands at 7 devices / 7 entities; the list at 9; the window closed.

## §1 Before the card
- The three plugs stay where they are, powered. The S31 untouched. B1, B2, the P4460 and the lamps stay in the box for this card.
- Git Bash on the desktop; in a NEW window paste the two variables again:
```
D=~/Desktop/Code/ClaudeFolder/_scratch/thu0924; S=~/Desktop/Code/ClaudeFolder/nexsys-hivemind/context/instructions/2026-09-24_THURSDAY-ORDER_scripts; mkdir -p $D
```
- Have G4-1's and G4-2's web pages reachable (their Wi-Fi IPs from T-A — the AP is off in Zigbee mode, the Wi-Fi IP still answers).

## §2 The window re-opened, with a wider watcher (one command)
```
ssh pi 'bash -s' < $S/T1b.sh > $D/T1b.txt 2>&1; tail -3 $D/T1b.txt; grep -q T1b-END $D/T1b.txt && ssh pi 'timeout 240 tail -n +1 -F ~/hs-bench/current.log | grep --line-buffered -E "permit_join_opened|device_join|device_announce|device_proposed|proposal_accepted|proposal_incomplete|device_adopted|interview_|key_establish|metering_formatting_read|reporting_configured"'
```
Read: `WINDOW KEY WRITTEN` (or `ALREADY PRESENT (kept)`) · `T1b-END` · then the watcher's `zigbee.permit_join_opened: duration=254s`. A `T1b-STOP` line means nothing was written and nothing restarted — say it back and wait.

## §3 G4-1, then G4-2 — two steps each (the TR3 is adopted: do not touch it)
**Step A — the measurement (60 s).** Unplug the plug, count ten, plug it back in. Watch the log for 60 s. Expected from Friday: nothing at all (the Gen4 resumes silently). If a `device_announce` or `device_join` line DOES come, wait for `proposal_accepted … source=config` and `device_adopted … entities=1` — that plug is done; go to the other.
**Step B — the reset from the plug's own side.** Open the plug's web page (its Wi-Fi IP, in the browser). Find the Zigbee control — under Settings, or on the Components page as a Zigbee component — and use the one that leaves or resets the Zigbee network (its label may read Reset, Leave network, or Factory reset Zigbee; say which it was). The plug then searches and joins our open window; the lines, in order: `device_join … status=UNSECURED_JOIN` → `device_announce` → `device_proposed … status=COMPLETE` → `proposal_accepted … source=config` → `device_adopted … deviceId=… entities=1` → `metering_formatting_read` (two lines) → `reporting_configured`. If the page offers no Zigbee control at all: 3 quick presses of the button; if still nothing in 60 s, hold the button 10 s. Say which act produced the join line.
Then the same two steps for G4-2.
If the watcher's 240 s runs out before both are adopted, run §2's command again (the key is kept; a new window opens at that boot) and continue with the plug not yet adopted. Two windows at most; then stop and say where it stands.
**Say back:** `T2b: G4-1 <silent|announced> · reset-by <web:<label>|3-press|hold|none> · adopted <yes|no> · G4-2 <the same> · windows <1|2>`

## §4 T3 again — the window closed, the capture home (one command; T3.sh unchanged)
```
ssh pi 'bash -s' < $S/T3.sh > $D/T3b.txt 2>&1; scp -rq pi:thu0924 $D/pi-capture-2; tail -5 $D/T3b.txt; ls $D/pi-capture-2 | wc -l
```
Read: `WINDOW KEY REMOVED · adopt_devices 9` · `adopted lines: 2 · devices=9 entities=9 · proposals at the closed boot: 0` · `entities rows 9 devices 9` · `Bearer in the capture: 0` · `T3-END` · the file count. (If only one Shelly adopted: `adopted lines: 1 · devices=8 entities=8`; say it as printed.)
**Say back:** `T3b: devices <n> · entities <n> · proposals 0 · files <k>` — then the hub cuts Half 2 (T4 → T8) from `$D/pi-capture-2`.

## §5 If it does not recover
Two windows and a Shelly still silent and un-adopted → stop there. Half 2 runs on the plugs that are adopted (the hub re-cuts T7's scenario for the fleet as it is), and the Gen4's silent resume becomes a register row with an instrument (IR-56): the adoption path gains a boot-time re-proposal of cached, listed, un-adopted devices, or an operator re-interview verb — a Java unit, not a rig act.
