<!--
file: context/instructions/2026-10-03_REHEARSAL-2_sensor-join_restart-under-loads_IR-56-power-cycle_operator-session-prompt.md
purpose: REHEARSAL 2's packet (THE WEEKS AHEAD §10 Sat 10-03 → SUNDAY 10-04, D-v95-25; the v94 dispatch's ONE DELIVERABLE) — a 4-h envelope opening 17:30 CT with ≈ 70 min of actions: the SNZB-06P24's join under IR-114's form (the window FIRST, then the USB re-seat as this class's own gesture — IR-117; never a button hold), a core restart under DECLARED loads with the three plugs, the S31 and the sensor read across it, IR-56's plug POWER-CYCLE sample on G4-1 (sample 6; samples 1–5 clean on app restarts — the BC6b audit), and the close. One instrument per card, ≤ 3 parts (D-v92-28 a); every tool argument through its validator on the desk at the cut (`pj_valid`'s regex; the ULIDs against `scenarios/constants.yaml`); every watch on a byte mark (THE BYTE-MARK WATCH, v93 b5); every loop RUN on the corpus with the sleeps removed (`_scratch/v94/b2/reh2_dry-run.txt`). The Hue is UNTOUCHED (the spike's return is not intaken). No config edit tonight: the restore is a CHECK, not an edit. The 21:00 CT STOP assumes NO present operator.
audience: the REHEARSAL 2 GUIDE (a fresh Cowork conversation; the paragraph below is its whole brief) · Nick (one action per message) · the v96 hub (the intake)
state-type: operator packet (one sitting; self-contained — THE WHOLE-PASTE LAW)
status: EXECUTED — the sitting ran Sun 2026-10-04 17:10 → 18:37 CT (cards 0–4; no STOP; `formed=0`); the return `_scratch/v97/sun1004/reh2/REHEARSAL-2_guide-return.md` 8178 B, filed verbatim at `context/audits/2026-10-04_REHEARSAL-2_return.md`; INTAKEN ACCEPT v98 beat 1 (D-v98-3; the audit `context/audits/2026-10-04_v98-b1_boot-and-REHEARSAL-2-intake_audit.md`; instrument 2026-10-05T00:43:04Z). Was: DISPATCH-READY — re-stamped v97 beat 4 (Sun 2026-10-04 ~15:5x CT; instrument 2026-10-04T20:58:22Z): the sitting opens 17:30 CT SUN 2026-10-04 (D-v95-25); the date-bound lines re-derived (the b4 audit lists each: the day, the sensor's dark span ≈ 54 h, P8's nightly = Monday 03:30, the output directory, the intaking hub v98); the Pi's core `5b0e20c` UNCHANGED (BC8 is Monday); a fresh dry-run on the corpus `_scratch/v97/reh2/reh2_dry-run.txt`; flips to EXECUTED at v98's intake. Was: DISPATCH-READY — cut v94 beat 2 (Sat 2026-10-03 ~07:5x CT; instrument 2026-10-03T12:54:05Z); the sitting opens 17:30 CT Sat 2026-10-03; flips to EXECUTED at v96's intake.
-->

# REHEARSAL 2 — the sensor's join · a restart under declared loads · IR-56's power-cycle (Sun 2026-10-04, 17:30 → ≤ 21:00 CT; re-stamped v97 b4)

**The guide's brief (paste this file WHOLE into a fresh Cowork conversation with `ClaudeFolder` connected; nothing else).** You are the REHEARSAL 2 GUIDE for NexSys / HomeSynapse. You are NOT the hub and you never re-plan. You show Nick EXACTLY ONE action per message — its DO line (one command to paste, or one physical thing), its RIG line (what the rig is after it), its SAY line (what he pastes or types back) — and wait for his line. One meaning per word; the exact command inline; the expected screen named. If his line does not match the action's EXPECT, you read the EXPECT's arms: an arm the card NAMES is recorded and the sitting CONTINUES; a state the card does not name is a STOP — "STOP — write what the screen shows; I close the sitting" — then card 4 (the close) and the return. `network_formed` anywhere ≠ 0 = POWER OFF + STOP (the standing law). A slot in angle brackets (`<MARK1>`, `<MAXW1>`, `<MARK3>`, `<BOOT2>`) is filled by YOU from the record of the sitting — Nick never retypes a number or an id. The clocks: Nick says CT; the Pi's log is EDT (= CT + 1 h); `date -u` lines are UTC (= CT + 5 h); you write every time with its clock named. **The envelope:** the sitting starts by 17:30 CT; the actions take ≈ 70 min; if the clock passes **21:00 CT** at any action, STOP there and run card 4 — card 4 needs no decision and no operator after it. **Two hardware acts tonight, in series, ≥ 60 min apart:** 1b (the sensor's USB re-seat) and 3b (G4-1's plug power-cycle). Nothing touches the Hue, the S31's relay, the nightly or any config file. **The return:** `_scratch/v97/sun1004/reh2/REHEARSAL-2_guide-return.md` ≤ 8 KB — §0 P1–P8 HELD / REFUTED / NOT-REACHED with the line that decided each; §1 every SAY verbatim with its CT; §2 Nick's other words with CT; §3 your departures from this file (none expected); §4 the files and bytes under `_scratch/v97/sun1004/reh2/`; the last line `RETURNED <path> <bytes>` — Nick pastes that one line to the hub.

**The pre-registrations (adjudicated by the hub at v98, Sunday night, never by the guide):**
- **P1** (card 0): the clone reads `5b0e20c`; the config carries `key-lines=0 · adopt=10 · warn-lines=0`; the entities read 10 rows with the SNZB-06P24 reading `avail=? stale=False lastReported=2026-10-02T16:19:36Z` (≈ 54 h dark since Fri 11:19 CT; THE HUB'S PRE-REGISTRATION OF RECORD is D-v95-13 on `5b0e20c`: `UNAVAILABLE` — the 25-h SILENCE_TIMEOUT arm, D-v95-10 — and `stale=false`; `AVAILABLE` here REFUTES that arm for this device and is J1's first finding on the fleet; either reading is RECORDED, neither is a STOP) and the Hue `UNAVAILABLE` (IR-112).
- **P2** (card 1): with the window open FIRST, the USB re-seat brings the sensor's chain inside 120 s after the mark: `child_join`/`device_announce` → `device_relinked` (re-pairing, no new adoption — the same device id `01M3Y4YA6KMH7JDEF5YMMJ3YND`) → `reporting_reapply` → `reporting_configured`; `proposed-new=0 adopted-new=0`; `keyfail-new` 0 or 1 (IR-115's third sample — recorded). Arm (ii), NAMED: no sensor line inside 120 s → `JOIN: none`, the sensor left as it is, the sitting continues (the hub rules Sunday; no second gesture, no button).
- **P3** (card 2, before): the loads read as DECLARED — G4-1 and G4-2 `W=0.0` (no load); the TR3 ≈ 2–3 W with the phone OFF its charger, higher and variable with the phone ON (the STATE line's `PHONE:` names which); the S31 `AVAILABLE` (no load; its relay untouched).
- **P4** (card 2, the restart): the new boot reaches `integration.launched`; `projection_live: devices=10 entities=10`; `formed=0 · resumed=1 · relinked=10 · permit=0` (a relink is a cache rehydration — IR-118; the Hue and, if unjoined, the sensor relink without a frame).
- **P5** (card 2, after): at +90 s the three plugs read `AVAILABLE stale=False` with `W` within ±0.5 W of P3's reading for the steady loads (IR-56's samples 1–5 shape); the sensor, if it joined in card 1, reads `AVAILABLE` with `lastReported` newer than card 1's; the S31's +30 s and +120 s reads are RECORDED beside the plugs', never asserted (IR-52's placements; no command is issued — the fence); at +600 s one `zigbee.link_summary` line per plug with `frames>0` (IR-96's column).
- **P6** (card 3): G4-1's power-cycle brings, inside 90 s after the mark, a `device_announce` or `child_join`/`SECURED_REJOIN` and a `device_relinked` for `0xACEBE6FFFEF733DC`, and at +120 s the API reads `AVAILABLE` with `lastReported` newer than 3a's. Arm (ii), NAMED — THE SILENT RESUME: no log line for G4-1 inside 90 s and the API still `AVAILABLE` on 3a's `lastReported` → IR-56's shape on a plug (the Java unit is queued after J2); recorded, the sitting continues.
- **P7** (card 4): nothing to restore — `key-lines=0 · warn-lines=0`, the carrier's md5 unchanged from card 0; `permit_join_closed` ≥ 1 in the first boot; both boot logs copied home.
- **P8** (Monday 03:30's nightly — the first after the sitting — read by the hub): `8/9 PASS · 1 SKIP(hue-online) · fleet: 10/10 · re-seen 10 · 6/6 · 0 forbidden` — `re-seen 10` because BOTH nightly reads now know ten ids (`nightly_digest.py:151–172`: the intersection of two registry reads), whether or not the sensor joined tonight — the digest cannot tell; a dark sensor under `10/10 · re-seen 10` is IR-118's second exhibit.

---

## Card 0 — THE STATE (the desk; read-only; one paste; ≈ 3 min)
**0.** DO (paste whole):
```
D=~/Desktop/Code/ClaudeFolder/_scratch/v97/sun1004/reh2; mkdir -p "$D"; ssh pi 'bash -s' <<'EOF_0' 2>&1 | tee "$D/C0.txt"
mkdir -p ~/reh2; L=$(readlink -f ~/hs-bench/current.log); Z=~/hs-bench/config/integrations/zigbee.yaml; C=~/hs-bench/config/homesynapse.yaml
echo "clone: $(cd ~/homesynapse-core && git --no-optional-locks log -1 --format=%h) | pid $(pgrep -f "[c]om.homesynapse.app.Main" | head -1) | boot $(basename $L) bytes=$(wc -c < $L) | pi-clock $(date -u +%H:%M:%SZ)"
echo "key-lines=$(grep -c permit_join_duration $Z) | adopt=$(grep -c '^\s*-\s*"\?0x' $Z) | warn-lines=$(grep -c on_unavailable $C) | carrier $(md5sum < $C | cut -c1-12) $(wc -c < $C) B"
echo "formed=$(grep -c zigbee.network_formed $L) opened=$(grep -c permit_join_opened $L) closed=$(grep -c permit_join_closed $L) relinked=$(grep -c device_relinked $L) keyfail=$(grep -c key_establishment_failed $L)"
for pair in SENSOR:01M3Y4YA6YSYQWVE9ET8FT4HWQ G4-1:01M3DPGF6Y4YXNXDHBW38ZEX2G TR3:01M3DM74SGEY7RXVDYSM4PK2XA G4-2:01M3DPKN9WD9B88Q4SVDMSBJVS S31:01KXW1W1SBJZERC9MBAMV2DWKE; do n=${pair%%:*}; u=${pair##*:}; echo "$n $(~/bench.sh state "$u" | python3 -c 'import sys,json,datetime; d=json.load(sys.stdin)["data"]; a=d.get("attributes",{}); w=a.get("power_w",{}).get("value"); lr=d.get("lastReported"); print("avail=%s stale=%s W=%s lastReported=%s" % (d.get("availability"), d.get("stale"), w, datetime.datetime.utcfromtimestamp(lr).strftime("%Y-%m-%dT%H:%M:%SZ") if lr else None))' 2>&1 | tail -1)"; done
echo "entities: $(curl -s -H "Authorization: Bearer $(~/bench.sh api_token)" http://127.0.0.1:7070/api/v1/entities | python3 -c 'import sys,json; rows=json.load(sys.stdin)["data"]; print("%d rows; %d AVAILABLE; unavailable: %s" % (len(rows), sum(1 for r in rows if r.get("availability")=="AVAILABLE"), [r.get("entityId","")[-6:] for r in rows if r.get("availability")!="AVAILABLE"]))' 2>&1 | tail -1)"
EOF_0
```
RIG: unchanged. · SAY: paste the output (nine lines), then TWO words of your own: `LED: slow-red-flash | solid | off` (the sensor, by eye) and `PHONE: on | off` (is the phone on the TR3's charger?). EXPECT (P1): `clone: 5b0e20c` (anything else = STOP — the fence); `key-lines=0 · adopt=10 · warn-lines=0 · carrier <md5> <n> B` (the guide WRITES the md5 — card 4 compares); `formed=0`; `SENSOR avail=AVAILABLE|UNAVAILABLE stale=False W=None lastReported=2026-10-02T16:19:36Z` (either `avail` is RECORDED — D-v95-13 expects UNAVAILABLE on `5b0e20c` at ≈ 54 h; a newer lastReported = the sensor is ALREADY joined → card 1 is SKIPPED and recorded, the sitting goes to card 2); G4-1/G4-2 `W=0.0`; TR3 `W=` ≈ 2–3 (phone off) or higher (phone on); S31 `avail=AVAILABLE`; `entities: 10 rows; 9 AVAILABLE; unavailable: ['DHE40F']` (the Hue). The guide writes the TR3's W and `PHONE:` on paper — P3's declared load.

## Card 1 — THE SENSOR'S JOIN under IR-114's form (the rig; instrument: the boot log on a byte mark; ≈ 12 min)
**1a.** DO (the mark, then the window — paste whole; the window is 254 s, so 1b follows AT ONCE):
```
ssh pi 'bash -s' <<'EOF_1A' 2>&1 | tee -a ~/Desktop/Code/ClaudeFolder/_scratch/v97/sun1004/reh2/C1.txt
L=~/hs-bench/current.log; DB=$(find ~/hs-bench -name "homesynapse-events.db" | head -1); echo "MARK1=$(wc -c < $L) MAXW1=$(sqlite3 "file:$DB?mode=ro" "SELECT MAX(global_position) FROM events;") pi-clock $(date -u +%H:%M:%SZ)"
~/bench.sh permit-join 254 "REH2 SNZB06P24 join" > /tmp/pj.out 2>&1; echo "permit-join exit=$?"; tail -2 /tmp/pj.out | cut -c1-200
sleep 3; grep -E "zigbee.permit_join_(opened|key_ignored|event_conflict)" $L | tail -1 | cut -c1-200
EOF_1A
```
RIG: a 254-s window is open. · SAY: paste the output (four lines). EXPECT: `MARK1=<bytes> MAXW1=<n>` (the guide WRITES BOTH — they fill 1c); `permit-join exit=0`; the last line carries `permit_join_opened` with `254`. The usage line or `exit=` ≠ 0 = STOP (paste it; no act). Then AT ONCE 1b.

**1b.** DO (Nick's hands; nothing typed): **unplug the sensor's USB-C from its charger, count five, plug it back in.** Watch the LED. · RIG: the sensor re-powering inside the open window. · SAY: ONE line — `REPLUG: <HH:MM:SS CT> · LED <slow-red-flash | solid-then-off | nothing | other>`. EXPECT: `slow-red-flash` (pairing — IR-117's return-in-pairing-mode, the gesture working) then solid/off as it joins. **Never press or hold the button — a 5-s hold is a factory reset (IR-114).** Then AT ONCE 1c.

**1c.** DO (the watch on the mark — 120 s, then the reads at +300 s from the window; paste whole, `<MARK1>` and `<MAXW1>` filled by the guide):
```
M=<MARK1>; W=<MAXW1>; ssh pi "bash -s $M $W" <<'EOF_1C' 2>&1 | tee -a ~/Desktop/Code/ClaudeFolder/_scratch/v97/sun1004/reh2/C1.txt
M=$1; W=$2; L=~/hs-bench/current.log; DB=$(find ~/hs-bench -name "homesynapse-events.db" | head -1); SEL='child_join|device_join|device_announce|device_relinked|device_proposed|device_adopted'
for i in $(seq 1 24); do tail -c +$((M+1)) $L | grep '0xA4C13814CE41FFFF' | grep -Eq "$SEL" && break; sleep 5; done; sleep 15
echo "--- +$(( i * 5 + 15 ))s ($(date -u +%H:%M:%SZ)) since MARK1=$M"; tail -c +$((M+1)) $L | grep '0xA4C13814CE41FFFF' | grep -E "$SEL|device_left|reporting_(reapply|configured)|key_establish" | cut -c1-220
echo "new-sensor-lines=$(tail -c +$((M+1)) $L | grep '0xA4C13814CE41FFFF' | grep -Ec "$SEL|reporting_") formed=$(grep -c zigbee.network_formed $L) proposed-new=$(tail -c +$((M+1)) $L | grep -c device_proposed) adopted-new=$(tail -c +$((M+1)) $L | grep -c device_adopted) keyfail-new=$(tail -c +$((M+1)) $L | grep -c key_establishment_failed)"
echo "waiting to +300 s from the window ..."; sleep 150
echo "closed=$(tail -c +$((M+1)) $L | grep -c permit_join_closed) keyfail-new=$(tail -c +$((M+1)) $L | grep -c key_establishment_failed)"; tail -c +$((M+1)) $L | grep key_establishment_failed | tail -1 | cut -c1-200
echo "sensor-state: $(~/bench.sh state 01M3Y4YA6YSYQWVE9ET8FT4HWQ | python3 -c "import sys,json,datetime; d=json.load(sys.stdin)[\"data\"]; a=d.get(\"attributes\",{}); lr=d.get(\"lastReported\"); print(\"avail=%s stale=%s lux=%s occupied=%s lastReported=%s\" % (d.get(\"availability\"), d.get(\"stale\"), a.get(\"illuminance_lux\",{}).get(\"value\"), a.get(\"occupied\",{}).get(\"value\"), datetime.datetime.utcfromtimestamp(lr).strftime(\"%Y-%m-%dT%H:%M:%SZ\") if lr else None))" 2>&1 | tail -1)"
echo "store since MAXW1: $(sqlite3 "file:$DB?mode=ro" "SELECT event_type || '=' || count(*) FROM events WHERE global_position > $W GROUP BY event_type;" | tr '\n' ' ')"
EOF_1C
```
RIG: the window closes by itself at 254 s. · SAY: paste the output whole. EXPECT (P2): the `---` line at ≤ +135 s with the sensor's chain (`child_join`/`device_announce` → `device_relinked … re-pairing, no new adoption` → `reporting_reapply` → `reporting_configured`); `new-sensor-lines ≥ 3 · formed=0 · proposed-new=0 · adopted-new=0`; `closed=1`; `sensor-state: avail=AVAILABLE … lastReported=<tonight, UTC>`; the store line with `device.relinked` or `reporting.*` rows. **Arm (ii), named:** `--- +135s` with NO sensor line and `new-sensor-lines=0` → say `JOIN: none`, leave the sensor as it is, go to card 2. `formed` ≠ 0 anywhere = POWER OFF + STOP. `keyfail-new` 0 or 1 is RECORDED (IR-115's third sample), never a STOP.

## Card 2 — THE RESTART UNDER DECLARED LOADS (the desk; instrument: `bench.sh state` across a restart; ≈ 15 min; starts only after card 1's `closed=1`)
**2a.** DO (the reads before — paste whole):
```
ssh pi 'bash -s' <<'EOF_2A' 2>&1 | tee ~/Desktop/Code/ClaudeFolder/_scratch/v97/sun1004/reh2/C2.txt
echo "BOOT1=$(basename $(readlink -f ~/hs-bench/current.log)) pi-clock $(date -u +%H:%M:%SZ)"
for pair in G4-1:01M3DPGF6Y4YXNXDHBW38ZEX2G TR3:01M3DM74SGEY7RXVDYSM4PK2XA G4-2:01M3DPKN9WD9B88Q4SVDMSBJVS S31:01KXW1W1SBJZERC9MBAMV2DWKE SENSOR:01M3Y4YA6YSYQWVE9ET8FT4HWQ; do n=${pair%%:*}; u=${pair##*:}; echo "before $n $(~/bench.sh state "$u" | python3 -c 'import sys,json,datetime; d=json.load(sys.stdin)["data"]; a=d.get("attributes",{}); lr=d.get("lastReported"); print("avail=%s stale=%s on=%s W=%s lastReported=%s" % (d.get("availability"), d.get("stale"), a.get("on",{}).get("value"), a.get("power_w",{}).get("value"), datetime.datetime.utcfromtimestamp(lr).strftime("%Y-%m-%dT%H:%M:%SZ") if lr else None))' 2>&1 | tail -1)"; done
EOF_2A
```
RIG: unchanged; the loads as card 0 declared (`PHONE:` as said — if the phone's state changed since card 0, Nick says `PHONE: <on|off>` again here). · SAY: paste the six lines. EXPECT (P3): `BOOT1=bench-2026-10-0…log`; G4-1/G4-2 `W=0.0`; TR3 `W=` ≈ 2–3 (phone off) or higher (phone on); every row `avail=AVAILABLE stale=False`.

**2b.** DO (the restart — paste whole; ≈ 2 min):
```
ssh pi 'bash -s' <<'EOF_2B' 2>&1 | tee -a ~/Desktop/Code/ClaudeFolder/_scratch/v97/sun1004/reh2/C2.txt
~/bench.sh restart 2>&1 | tail -3; sleep 30; L=$(readlink -f ~/hs-bench/current.log); echo "BOOT2=$(basename $L) pi-clock $(date -u +%H:%M:%SZ)"
for i in $(seq 1 18); do grep -q "integration.launched" $L && break; sleep 5; done; echo "launched at +$(( i * 5 ))s: $(grep -c integration.launched $L)"
sleep 20; grep -h "projection_live" $L | tail -1 | cut -c1-200
echo "formed=$(grep -c zigbee.network_formed $L) resumed=$(grep -c zigbee.network_resumed $L) relinked=$(grep -c device_relinked $L) permit=$(grep -c permit_join_opened $L) keyfail=$(grep -c key_establishment_failed $L) sensor-relinked=$(grep -c 'device_relinked.*0xA4C13814CE41FFFF' $L)"
EOF_2B
```
RIG: the core restarted on the same clone; every plug stays powered. · SAY: paste the output whole. EXPECT (P4): `BOOT2=<a new name>` (the guide WRITES it — card 3 and card 4 use it); `launched at +≤60s: 1`; `projection_live: devices=10 entities=10 position=<P>`; `formed=0 resumed=1 relinked=10 permit=0 keyfail=0 sensor-relinked=1`. `formed` ≠ 0 = POWER OFF + STOP. `relinked` < 10 is RECORDED (which device is missing is Sunday's read), not a STOP.

**2c.** DO (the reads after — ONE paste; it prints as it goes over ≈ 10.5 min; do not interrupt):
```
ssh pi 'bash -s' <<'EOF_2C' 2>&1 | tee -a ~/Desktop/Code/ClaudeFolder/_scratch/v97/sun1004/reh2/C2.txt
L=$(readlink -f ~/hs-bench/current.log); T0=$(date +%s); rd() { ~/bench.sh state "$1" | python3 -c 'import sys,json,datetime; d=json.load(sys.stdin)["data"]; a=d.get("attributes",{}); lr=d.get("lastReported"); print("avail=%s stale=%s on=%s W=%s lastReported=%s" % (d.get("availability"), d.get("stale"), a.get("on",{}).get("value"), a.get("power_w",{}).get("value"), datetime.datetime.utcfromtimestamp(lr).strftime("%Y-%m-%dT%H:%M:%SZ") if lr else None))' 2>&1 | tail -1; }
echo "S31 @+$(( $(date +%s) - T0 ))s $(rd 01KXW1W1SBJZERC9MBAMV2DWKE)"; sleep 60
for pair in G4-1:01M3DPGF6Y4YXNXDHBW38ZEX2G TR3:01M3DM74SGEY7RXVDYSM4PK2XA G4-2:01M3DPKN9WD9B88Q4SVDMSBJVS SENSOR:01M3Y4YA6YSYQWVE9ET8FT4HWQ; do echo "after $pair @+$(( $(date +%s) - T0 ))s $(rd ${pair##*:})"; done; sleep 30
echo "S31 @+$(( $(date +%s) - T0 ))s $(rd 01KXW1W1SBJZERC9MBAMV2DWKE)"
echo "waiting for the ten-minute link summary ..."; sleep 480
for ieee in 0xACEBE6FFFEF733DC 0x4CE175B4C0700000 0xACEBE6FFFEF25A2C 0xA4C13814CE41FFFF; do echo "link $(grep "zigbee.link_summary: device=$ieee" $L | tail -1 | grep -oE 'device=.*' | cut -c1-120)"; done
echo "summaries=$(grep -c zigbee.link_summary $L) pi-clock $(date -u +%H:%M:%SZ)"
EOF_2C
```
RIG: unchanged. · SAY: paste the output whole. EXPECT (P5): `S31 @+0s avail=AVAILABLE` and `S31 @+≈95s avail=AVAILABLE` (RECORDED, never asserted); `after G4-1/G4-2 … W=0.0`, `after TR3 … W=` within ±0.5 W of 2a's for the steady load (the phone, if on, is declared variable — no tolerance); `after SENSOR … lastReported=` newer than 2a's if card 1 joined it (else 2a's value — recorded); four `link device=… frames=<n>` lines with `frames>0` for the three plugs (the sensor's `frames=0 … last_link_at=-` if unjoined — recorded); `summaries ≥ 4`.

## Card 3 — IR-56's POWER-CYCLE SAMPLE on G4-1 (the rig; instrument: the boot log on a byte mark + `bench.sh state`; ≈ 6 min; ≥ 60 min after 1b)
**3a.** DO (the mark and the read before — paste whole):
```
ssh pi 'bash -s' <<'EOF_3A' 2>&1 | tee ~/Desktop/Code/ClaudeFolder/_scratch/v97/sun1004/reh2/C3.txt
L=~/hs-bench/current.log; echo "MARK3=$(wc -c < $L) boot=$(basename $(readlink -f $L)) pi-clock $(date -u +%H:%M:%SZ)"
echo "G4-1 before $(~/bench.sh state 01M3DPGF6Y4YXNXDHBW38ZEX2G | python3 -c 'import sys,json,datetime; d=json.load(sys.stdin)["data"]; a=d.get("attributes",{}); lr=d.get("lastReported"); print("avail=%s stale=%s on=%s W=%s lastReported=%s" % (d.get("availability"), d.get("stale"), a.get("on",{}).get("value"), a.get("power_w",{}).get("value"), datetime.datetime.utcfromtimestamp(lr).strftime("%Y-%m-%dT%H:%M:%SZ") if lr else None))' 2>&1 | tail -1)"
EOF_3A
```
RIG: unchanged. · SAY: paste the two lines. EXPECT: `MARK3=<bytes> boot=<BOOT2>` (the guide WRITES MARK3); `G4-1 before avail=AVAILABLE … W=0.0 lastReported=<t>` (the guide WRITES `<t>`). Then AT ONCE 3b.

**3b.** DO (Nick's hands; nothing typed): **unplug G4-1 from the wall outlet, count five, plug it back in.** G4-1 is the Shelly with NO load; nothing is plugged into it. · RIG: G4-1 re-powering; every other device untouched. · SAY: ONE line — `CYCLE: <HH:MM:SS CT>`. Then AT ONCE 3c.

**3c.** DO (the watch on the mark — 90 s, then the read at +120 s; `<MARK3>` filled by the guide):
```
M=<MARK3>; ssh pi "bash -s $M" <<'EOF_3C' 2>&1 | tee -a ~/Desktop/Code/ClaudeFolder/_scratch/v97/sun1004/reh2/C3.txt
M=$1; L=~/hs-bench/current.log; SEL='child_join|device_join|device_announce|SECURED_REJOIN|device_relinked|device_proposed'
for i in $(seq 1 18); do tail -c +$((M+1)) $L | grep '0xACEBE6FFFEF733DC' | grep -Eq "$SEL" && break; sleep 5; done
echo "--- +$(( i * 5 ))s ($(date -u +%H:%M:%SZ)) since MARK3=$M"; tail -c +$((M+1)) $L | grep '0xACEBE6FFFEF733DC' | cut -c1-220
echo "g41-new-lines=$(tail -c +$((M+1)) $L | grep -c '0xACEBE6FFFEF733DC') formed=$(grep -c zigbee.network_formed $L) proposed-new=$(tail -c +$((M+1)) $L | grep -c device_proposed)"
sleep $(( 120 - i * 5 > 0 ? 120 - i * 5 : 1 ))
echo "G4-1 @+120s $(~/bench.sh state 01M3DPGF6Y4YXNXDHBW38ZEX2G | python3 -c 'import sys,json,datetime; d=json.load(sys.stdin)["data"]; a=d.get("attributes",{}); lr=d.get("lastReported"); print("avail=%s stale=%s on=%s W=%s lastReported=%s" % (d.get("availability"), d.get("stale"), a.get("on",{}).get("value"), a.get("power_w",{}).get("value"), datetime.datetime.utcfromtimestamp(lr).strftime("%Y-%m-%dT%H:%M:%SZ") if lr else None))' 2>&1 | tail -1)"
EOF_3C
```
RIG: unchanged. · SAY: paste the output whole. EXPECT (P6): the `---` line at ≤ +90 s with a `device_announce` or `child_join`/`SECURED_REJOIN` and a `device_relinked` for `0xACEBE6FFFEF733DC`; `g41-new-lines ≥ 1 · formed=0 · proposed-new=0`; `G4-1 @+120s avail=AVAILABLE … lastReported=` newer than 3a's. **Arm (ii), named — THE SILENT RESUME:** `--- +90s` with NO line, `g41-new-lines=0`, and `@+120s … lastReported=` EQUAL to 3a's → IR-56's shape on a plug; say `IR56: silent`, continue to card 4. `proposed-new` ≠ 0 is RECORDED (a re-proposal would be the row's own fix appearing — it is not expected), not a STOP. `formed` ≠ 0 = POWER OFF + STOP.

## Card 4 — THE CLOSE (the desk; the restore-check, the logs home, the return; ≈ 5 min; run it at 21:00 CT whatever card is current)
**4a.** DO (paste whole):
```
D=~/Desktop/Code/ClaudeFolder/_scratch/v97/sun1004/reh2; ssh pi 'bash -s' <<'EOF_4A' 2>&1 | tee "$D/C4.txt"
Z=~/hs-bench/config/integrations/zigbee.yaml; C=~/hs-bench/config/homesynapse.yaml; L=$(readlink -f ~/hs-bench/current.log)
echo "restore-check: key-lines=$(grep -c permit_join_duration $Z) | warn-lines=$(grep -c on_unavailable $C) | carrier $(md5sum < $C | cut -c1-12) $(wc -c < $C) B | formed=$(grep -c zigbee.network_formed $L) | pi-clock $(date -u +%H:%M:%SZ)"
ls -t ~/hs-bench/bench-*.log | head -2 | while read f; do cp -p "$f" ~/reh2/; echo "kept $(basename $f) $(wc -c < $f) B"; done
EOF_4A
scp -q pi:reh2/bench-*.log "$D/" && ls -la "$D" | tail -n +2 | awk '{print $5, $9}'
```
RIG: as it stands — nothing is powered off; the window closed itself; no file was edited. · SAY: paste the output. EXPECT (P7): `restore-check: key-lines=0 · warn-lines=0 · carrier <md5 EQUAL to card 0's> <n> B · formed=0`; two `kept bench-…log` lines (BOOT1 and BOOT2); the local listing with `C0.txt … C4.txt` and the two logs. A carrier md5 that DIFFERS from card 0's is written in the return as the first line of §3 — nothing is edited back tonight (no edit was made; a difference is a finding).

**4b.** DO (the guide): write the return at `_scratch/v97/sun1004/reh2/REHEARSAL-2_guide-return.md` in the form above (≤ 8 KB) and tell Nick its last line. · SAY (Nick, to the hub): `RETURNED <path> <bytes>` — the whole report-back. The hub (v98) intakes at the bytes; nothing else is asked tonight.

---
**The hub's line to the guide, for the record:** this packet reuses SENSOR-REJOIN-1's Part 2 form (`_scratch/v93/sensor/hub-amendment_part2.md`, the byte-mark watch), BENCH-CORE-3's plug read (`context/instructions/2026-09-26_bench-card_BENCH-CORE-3_…:63`) and the 1b packet's card shape; every reused string is listed with its prior-ledger grep in `context/audits/2026-10-03_v94-b2_REHEARSAL-2-packet-cut_dry-run_prior-ledger-gate_audit.md`. The deviations carried: the pairing gesture is the USB re-seat, never the button (IR-114; the 1b manual); the window opens BEFORE the act (the guide's note :55 — the class's pairing cycle is ≈ 180 s); every watch reads only the bytes after its mark (the guide's note :42); a restart re-points `current.log` to a NEW file, so card 3's mark is taken on BOOT2 and card 2's counts read BOOT2 whole; a STOP clause names a state the record does not know, never a token the record's history carries (the BC7 slips); the logs are copied home before the 4-newest window evicts them (1b d6).
