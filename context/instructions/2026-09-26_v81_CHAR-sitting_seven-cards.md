<!--
file: context/instructions/2026-09-26_v81_CHAR-sitting_seven-cards.md
purpose: THE CHAR SITTING of Sat 2026-09-26 as SEVEN CARDS in THE SIMPLER WAY's shape (D-v80-17; D-v81-7): each card at most five acts and exactly one say-back line; one card on screen at a time; every card cut FROM the scenario's prompts (metering-known-load.yaml at the METER-2 sha) and the rig as Nick stated it (one Kill A Watt = A; one 1-ft cord; B1 the SURAIELEC and B2 the MECHEER on the desk; one 40 W clamp lamp; G4-1 · TR3 · G4-2 in wall sockets, OFF, movable; the S31 unplugged, hands off). A surprise is a STOP-and-close: say the line with the surprise as one clause; the next card is cut at the desk. Two windows: Git Bash A = the card window (the scenario runs in it, inside tmux on the Pi); Git Bash B = the meter-reader (`ssh pi '~/bench.sh state <ULID> | head -c 240'; echo`). The CHAR sheet is paper: every number typed is first written there.
audience: Nick (one card at a time; he never remembers — every card is self-locating) · the hub (hands each card on the prior card's line; intakes the bundle at card 7)
state-type: operator cards (the sitting of record)
status: PARTIAL — card 1 EXECUTED (all three plugs AVAILABLE; card 1b not needed); card 2 SKIPPED at the rig (CHAR-BEFORE confirmed without the passes); card 3 EXECUTED with departures (the b3 audit §2); cards 4–7 SUPERSEDED by the action script `context/instructions/2026-09-26_v81_CHAR-sitting-2_action-script_operator-session-prompt.md` (v81 beat 3, Sat 2026-09-26 ~15:4x CT; instrument 2026-09-26T20:44:20Z). Was: DISPATCH-READY — cut v81 beat 2 (Sat 2026-09-26 ~09:2x CT; instrument 2026-09-26T14:2xZ). Cards 1..7 handed in order; card 1b only if card 1 reads a plug UNAVAILABLE. EXECUTED when card 7's line is said.
-->

# The CHAR sitting — seven cards

Every card's shell variables (set inside the card; nothing to remember): `S=~/Desktop/Code/ClaudeFolder/nexsys-hivemind/context/instructions/2026-09-24_THURSDAY-ORDER_scripts` · `D=~/Desktop/Code/ClaudeFolder/_scratch/v81/sat0926`. The ULIDs: G4-1 `01M3DPGF6Y4YXNXDHBW38ZEX2G` · TR3 `01M3DM74SGEY7RXVDYSM4PK2XA` · G4-2 `01M3DPKN9WD9B88Q4SVDMSBJVS`.

## Card 1 — the desk: the stray session, the Pi's pull, the availability read (Git Bash A; one paste)
1. Paste whole:
```
mkdir -p ~/Desktop/Code/ClaudeFolder/_scratch/v81/sat0926; ssh pi 'bash -s' <<'EOF_C1' 2>&1 | tee ~/Desktop/Code/ClaudeFolder/_scratch/v81/sat0926/card1.txt
T=$(tmux kill-session -t metering 2>/dev/null && echo killed || echo none)
cd ~/nexsys-bench && git pull --ff-only -q 2>&1 | tail -1; P=$(git log -1 --format=%h)
L=""; for pair in G4-1:01M3DPGF6Y4YXNXDHBW38ZEX2G TR3:01M3DM74SGEY7RXVDYSM4PK2XA G4-2:01M3DPKN9WD9B88Q4SVDMSBJVS; do n=${pair%%:*}; u=${pair##*:}; L="$L · $n $(~/bench.sh state "$u" | python3 -c 'import sys,json; d=json.load(sys.stdin)["data"]; a=d["attributes"]; print("%s on=%s W=%s" % (d["availability"], a["on"]["value"], a["power_w"]["value"]))' 2>&1 | tail -1)"; done
echo "CARD1: tmux $T · pi $P$L"
EOF_C1
```
2. Read the last line. **Say back that line exactly** (`CARD1: tmux <killed|none> · pi <sha> · G4-1 <AVAILABLE|UNAVAILABLE> on=<..> W=<..> · TR3 … · G4-2 …`). `pi <sha>` must equal the METER-2 sha you landed; if not, say so as a clause and stop.

## Card 1b — only if card 1 read a plug UNAVAILABLE: the re-join (the plug's own "Start pairing" inside a window)
1. Open the window and the watcher (Git Bash A; paste whole; it runs up to 4 minutes):
```
S=~/Desktop/Code/ClaudeFolder/nexsys-hivemind/context/instructions/2026-09-24_THURSDAY-ORDER_scripts; D=~/Desktop/Code/ClaudeFolder/_scratch/v81/sat0926; ssh pi 'bash -s' < $S/T1b.sh > $D/T1b.txt 2>&1; tail -3 $D/T1b.txt; grep -q T1b-END $D/T1b.txt && ssh pi 'timeout 240 tail -n +1 -F ~/hs-bench/current.log | grep --line-buffered -E "permit_join_opened|device_join|device_announce|device_relinked|device_proposed|proposal_accepted|device_adopted|interview_"'
```
2. When the watcher prints `permit_join_opened`, open the UNAVAILABLE plug's web page (its Wi-Fi IP, in the browser), find the Zigbee control and press **Start pairing** (the act of Friday's T2b; nothing else on the page).
3. Wait for the watcher to print the plug's join / announce lines (or 240 s to pass).
4. Read the plug again (Git Bash B): `ssh pi '~/bench.sh state <the UNAVAILABLE plug's ULID> | head -c 240'; echo`.
5. **Say back one line:** `CARD1B: <plug> <AVAILABLE|UNAVAILABLE> · window <opened|T1b-STOP> · watcher <the join lines' names, or none>`. The window closes at card 7 (T3.sh).

## Card 2 — the rig: the scenario starts; CHAR-BEFORE (two passes on the cord)
1. Git Bash A — attach tmux and start the scenario (two lines; the second inside tmux):
```
ssh -t pi 'tmux new -s metering'
```
```
~/nexsys-bench/tools/bench.sh scenario metering-known-load
```
2. The first prompt is CHAR-BEFORE. Pass 1: chain wall → A → cord → B1 → LAMP. Lamp OUT of B1 for 30 s; write A and B1 (the tares) on the sheet. Lamp IN; two minutes; three simultaneous A / B1 readings, written as pairs.
3. Pass 2: B2 in B1's place (wall → A → cord → B2 → LAMP); the tares; lamp in; two minutes; three A / B2 pairs.
4. Re-chain wall → A → cord → LAMP (no meter, no plug). Press ENTER in tmux.
5. **Say back one line:** `CARD2: B1 <tare A/B1> <pair1> <pair2> <pair3> · B2 <tare A/B2> <pair1> <pair2> <pair3>` (each pair as `A/B`, e.g. `40.1/42.5`). The next prompt on screen is G4-1's TARE — do nothing until card 3.

## Card 3 — G4-1 (the prompts G4-1 TARE → OFFSET → volts ×2 → REP ×3; ≤ 15 min)
1. TARE: with wall → A → cord → LAMP (no plug), after 30 s read A → W1 (sheet). Move G4-1 from its wall socket into the cord's end, the lamp into G4-1 (wall → A → cord → G4-1 → LAMP). Git Bash B: `ssh pi '~/bench.sh state 01M3DPGF6Y4YXNXDHBW38ZEX2G | head -c 240'; echo` — if `"on":{"value":false}`, press G4-1's button and read again until `true`. Wait 30 s, read A → W2. Type `W2 − W1` (0 if negative; note the pair), ENTER.
2. OFFSET: lamp OUT of G4-1 (relay on). Git Bash B: the same state read until `power_w` settles; type its value (expect 0.0), ENTER. Lamp back IN.
3. Volts: type A's volts, ENTER; 10 s later type A's volts again, ENTER.
4. REP ×3 — the same act three times: lamp OUT of G4-1 for 15 s, back IN; Git Bash B: the state read until `power_w` shows the lit value, then 5 s more; read A's watts, type, ENTER; the platform's read prints WITHIN / OUTSIDE / VOID within 10 s — write it on the sheet, keep going whatever it prints.
5. **Say back one line:** `CARD3: G4-1 tare <W2−W1> · offset <w> · V <v1>/<v2> · rep <A1>:<verdict> <A2>:<verdict> <A3>:<verdict>`. Leave G4-1 in the cord; the next prompt on screen is TR3's TARE.

## Card 4 — TR3 (the same shape; the TR3 settles slower — up to a minute)
1. TARE: G4-1 back to its wall socket; wall → A → cord → LAMP; 30 s; A → W1. Move TR3 into the cord's end, the lamp into TR3. Git Bash B: `ssh pi '~/bench.sh state 01M3DM74SGEY7RXVDYSM4PK2XA | head -c 240'; echo` — relay ON (its button if `false`). 30 s; A → W2. Type `W2 − W1`, ENTER.
2. OFFSET: lamp OUT; the state read until `power_w` settles (up to a minute); type it, ENTER; lamp IN.
3. Volts ×2 (10 s apart), ENTER each.
4. REP ×3: lamp OUT 15 s, IN; the state read until the lit value (up to a minute), +5 s; read A, type, ENTER.
5. **Say back one line:** `CARD4: TR3 tare <..> · offset <..> · V <..>/<..> · rep <A1>:<v> <A2>:<v> <A3>:<v>`.

## Card 5 — G4-2 (the same shape)
1. TARE: TR3 back to its wall socket; wall → A → cord → LAMP; 30 s; A → W1. Move G4-2 into the cord's end, the lamp into G4-2. Git Bash B: `ssh pi '~/bench.sh state 01M3DPKN9WD9B88Q4SVDMSBJVS | head -c 240'; echo` — relay ON. 30 s; A → W2. Type `W2 − W1`, ENTER.
2. OFFSET: lamp OUT; the state read until `power_w` settles; type it, ENTER; lamp IN.
3. Volts ×2, ENTER each.
4. REP ×3: lamp OUT 15 s, IN; the state read until the lit value, +5 s; read A, type, ENTER.
5. **Say back one line:** `CARD5: G4-2 tare <..> · offset <..> · V <..>/<..> · rep <A1>:<v> <A2>:<v> <A3>:<v>`. The next prompt on screen is CHAR-AFTER.

## Card 6 — CHAR-AFTER; the verdict
1. G4-2 back to its wall socket. Pass 1: wall → A → cord → B1 → LAMP; lamp OUT 30 s (the tares A, B1 on the sheet); lamp IN; two minutes; three A / B1 pairs.
2. Pass 2: B2 in B1's place; the tares; two minutes; three A / B2 pairs.
3. Type the number of pairs the sheet holds from both halves (twelve if every reading was taken), ENTER. The scenario prints its verdict line and the bundle path.
4. Detach tmux: **Ctrl-b, then d** (never close the window before the verdict prints).
5. **Say back one line:** `CARD6: <the verdict line as printed> · bundle <stamp> · after B1 <tare> <p1> <p2> <p3> · B2 <tare> <p1> <p2> <p3>`.

## Card 7 — the desk: the bundle home, the window key, the S31 (Git Bash A)
1. The bundle home (paste whole):
```
D=~/Desktop/Code/ClaudeFolder/_scratch/v81/sat0926; ssh pi 'B=$(ls -d ~/hs-bench/bundles/metering-known-load-* | tail -1); echo "$B"; grep -rc Bearer "$B" | awk -F: "{s+=\$2} END {print \"Bearer in the bundle:\", s+0}"; tail -3 "$B/verdict.txt"'; scp -rq "pi:$(ssh pi 'ls -d ~/hs-bench/bundles/metering-known-load-* | tail -1')" $D/bundle-CHAR; ls $D/bundle-CHAR | wc -l
```
2. The window key — if card 1b ran: `S=~/Desktop/Code/ClaudeFolder/nexsys-hivemind/context/instructions/2026-09-24_THURSDAY-ORDER_scripts; D=~/Desktop/Code/ClaudeFolder/_scratch/v81/sat0926; ssh pi 'bash -s' < $S/T3.sh > $D/T3c.txt 2>&1; tail -3 $D/T3c.txt` (read `T3-END`). If card 1b did NOT run: `ssh pi 'grep -c permit_join_duration ~/hs-bench/config/integrations/zigbee.yaml'` (read `0`).
3. The S31 — only on your word `S31: back-in-at-close`: the S31 into its wall socket, not pressed, nothing plugged into it.
4. The lamp unplugged; the plugs left in their wall sockets; the meters on the desk.
5. **Say back one line:** `CARD7: files <k> · Bearer 0 · key <0|T3-END> · S31 <in|out>`. The hub intakes the bundle at the bytes and banks the datum.
