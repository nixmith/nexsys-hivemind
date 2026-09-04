<!--
file: context/handoff/2026-09-04_R-4b_navigator-packet_held-card.md
purpose: THE R-4b NAVIGATOR PACKET — the four-of-four re-representation on the held card (hs-fresh) with the CI-built artifact carrying F-R4-1 + PKG-SEC-2 (+ FAILCHAN if guard 1 selects it). Row 12 RULED (a) with Nick's EDIT: the announce-class fallback (b) fires on a criterion-0 MISS today, not on 09-14. Authored by the v62 hub at beat 5 (Fri 2026-09-04 ~08:xx CT) on the R-4 packet + record + audit, the F-R4-1 audit/return, the FAILCHAN audit, and the zigbee fragment at HEAD. Every criterion pre-checked reachable against the rig census (the R-4 record). Playbook §8 contract: every block self-contained; WHERE-labelled; one act per line; expected tokens named; ⏺ = paste either way.
audience: Nick (the operator) · the hub (navigates live between blocks; audits the record)
state-type: operator packet (navigator pattern)
status: LIVE — TODAY (Fri 09-04). Do not start before §0's guard is answered. The record you build as you go: paste each ⏺ into chat; the hub files them as context/audits/2026-09-04_R-4b_re-rep_operator-record.md.
-->

# R-4b — the four-of-four on the shipped artifact (held card, Friday 09-04)

**GOAL.** On the held card, running the CI-built artifact, (C1) the network RESUMES (zero formed), (C2) ≥1 entity AVAILABLE with store-freshness rows inside a ≥45-min window, (C3) the event store grows with a zero throw-discriminator, and **(C4) ONE `bench-hero` run with a rendered explanation, re-bound to the held card's OWN entities including a device ADOPTED TODAY through the rejoin path** — the F-R4-1 hop's first real-silicon ⏺ is **criterion 0**. Four-of-four → **C-002 mints** (the hub writes it tonight). **DONE-WHEN:** every ⏺ in §5–§8 banked; the bench card back and its floor `[PASS]` (§9).

**ANTI-ACTIONS (the whole day).** Never re-run `main` CI · never `--allow-downgrades` · never delete a file on the card (move aside) · never press a battery sensor's button >5 s (a network LEAVE) · never power-cycle the Hue 6× (the factory dance — not today) · never touch the bench card's s31/nightly · never paste a token value (the helper prints a labelled block; ⏺ `TOKLEN-OK` only) · one physical act per line, note the clock on each.

## §0 GUARD 1 — which artifact (answer before §1)
Read the Actions page for your FAILCHAN push (§A of the brief). **BOTH `Build & Check` and `install-smoke` (amd64 + arm64) GREEN → the FAILCHAN artifact rides (its install-smoke run's `distribution-artifacts-arm64`); the §5 stop-proof applies.** Anything else (pending, or any red) → **`ef02d13`'s artifact** (the PKG-SEC-2 push's install-smoke run) — F-R4-1 + PKG-SEC-2 are what R-4b needs; FAILCHAN's proof waits for the next card session. ⏺ one line: `ARTIFACT: <FAILCHAN <sha> | ef02d13> — run <URL>`.

## §1 Fetch + hash (desktop; browser + Git Bash)
Open the chosen install-smoke run → the **arm64** job → the "Version-grammar echo" step → ⏺ the whole `version-grammar echo green: … sha256 <64 hex>  homesynapse_0.1.0+git<…>_arm64.deb` line (the origin hash). Then the run's Summary → Artifacts → `distribution-artifacts-arm64` → `~/Downloads`.
```bash
# WHERE: Git Bash. The zip NESTS at deb/build/ (the R-4 record's instrument defect (i), fixed here). Old .debs move aside — delete nothing.
mkdir -p ~/r4b-artifact ~/r3-history && mv ~/r4b-artifact/*.deb ~/r3-history/ 2>/dev/null; cd ~/r4b-artifact && powershell.exe -NoProfile -Command "Expand-Archive -LiteralPath \"$(cygpath -w ~/Downloads/distribution-artifacts-arm64.zip)\" -DestinationPath \"$(cygpath -w ~/r4b-artifact)\" -Force" && find . -name '*_arm64.deb' -exec sha256sum {} \;
# expect: EXACTLY ONE .deb (under ./deb/build/ or ./); its hash EQUALS the echo line's sha256; its name carries the chosen sha. ⏺ the line. Two .debs or a hash mismatch → STOP, paste.
```
**STOP-GATE R4b-1:** one .deb · hash = the run log · the sha in the name = §0's choice.

## §2 The swap (bench card → held card; the coordinator STAYS in its port)
```bash
# WHERE: the bench card (ssh pi). FIRST: the overnight digest — the bench never goes down un-read. ⏺ the two lines.
tail -2 ~/hs-bench/digests/nightly.log; ls -t ~/hs-bench/bundles | head -2
```
```bash
# WHERE: the bench card. Then power OFF at the wall → bench card OUT → held card IN (the card labelled hs-fresh) → power ON → wait ~90 s. Note the clock.
sudo shutdown -h now
```
```bash
# WHERE: desktop → the held card. The FIRST line must print hs-fresh (the O-2 lesson). The boot glance.
ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local 'hostname; date -u +%H:%M:%SZ; dpkg-query -W -f "${Version}\n" homesynapse; systemctl is-active homesynapse.service; sudo journalctl -u homesynapse.service --no-pager -n 400 | grep -E "zigbee\.(network_resumed|network_formed)" | tail -2; sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" "SELECT COUNT(*) FROM events;"'
# expect: hs-fresh · the Z clock ⏺ · 0.1.0+git20260830.201400.g7c57d7f (R-4's artifact) · active · network_resumed: channel=20 panId=0x774c (ZERO formed) · a row count ⏺ = ROWS-A. Anything else → STOP, paste.
```

## §3 Step 0b — the config pre-read (BEFORE the install; the held card)
```bash
# WHERE: the held card. Copy aside (delete nothing) and show the zigbee block as found.
sudo mkdir -p /root/r4b-history && sudo cp /etc/homesynapse/config/integrations/zigbee.yaml /root/r4b-history/zigbee.yaml.pre-R4b && sudo cat /etc/homesynapse/config/integrations/zigbee.yaml
# expect (the R-4 record's shape): serial_port: /dev/zigbee · channel: 20 · adopt_devices: SIX IEEEs (0x00178801101A09BB Hue · 0xF044D3FFFE9C78D7 SNZB-03P · 0x00124B002FA8D1C5 S31 · 0xF044D3FFFED2A201 SNZB-02P · 0xF044D3FFFE1C1E8E SNZB-01P · 0x449FDAFFFE688F57 SNZB-04P) · NO permit_join_duration line. ⏺ the file. Every key present is a fragment key (serial_port · channel · adopt_devices) → the new artifact must boot with ZERO "Configuration issue" lines (§5). A key you see that is NOT one of {serial_port, baud_rate, adapter_type, channel, permit_join_duration, adopt_devices, watchdog_interval_seconds, availability, topology_scan_interval_hours, reporting_overrides, profiles_path, telemetry_threshold_seconds, route_health, ezsp_config} → ⏺ it; expect one WARN for it at §5 (a finding, not a stop).
```

## §4 The install (an ordinary upgrade — NO flag)
```bash
# WHERE: desktop → the held card. Move the old .deb aside on the card, copy the new one, verify the hash hop-to-hop.
ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local 'mkdir -p ~/r3-history && mv ~/homesynapse_*_arm64.deb ~/r3-history/ 2>/dev/null; ls ~/homesynapse_*_arm64.deb 2>/dev/null; echo "---"' && cd ~/r4b-artifact && scp -i ~/.ssh/id_ed25519_pi $(find . -name '*_arm64.deb') nick@hs-fresh.local: && ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local 'sha256sum ~/homesynapse_*_arm64.deb; dpkg-deb --field ~/homesynapse_*_arm64.deb Version Architecture'
# expect: "---" alone before the copy · the SAME hash as §1 · Version = the chosen artifact's · arm64. ⏺ all.
```
```bash
# WHERE: the held card. The integrity gate FIRST (a bad store stops the install).
sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;' && sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'PRAGMA integrity_check;'
# expect: ROWS-pre ⏺ · ok. Anything but ok → STOP, paste.
```
```bash
# WHERE: the held card. The install; apt asking to DOWNGRADE = STOP (the ordering scheme failed — a finding).
sudo apt install -y ~/homesynapse_*_arm64.deb 2>&1 | tail -8 && dpkg-query -W -f '${Version}\n' homesynapse && cat /opt/homesynapse/VERSION && sleep 25 && systemctl is-active homesynapse.service && sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;' && sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'PRAGMA integrity_check;'
# expect: an UPGRADE tail (no "downgrad") · the new Version TWICE · active · ROWS ≥ pre · ok. ⏺ all.
```
**STOP-GATE R4b-2:** version exact in both places · active · zero row loss · integrity ok. A miss → `sudo systemctl status homesynapse.service --no-pager -l` ⏺, STOP.

## §5 The measured boot (PKG-SEC-2's proof; FAILCHAN's proof if it rides)
```bash
# WHERE: the held card. Scope to THIS service invocation (the R-4 record's instrument defect (ii), fixed): the invocation id, then the greps.
INV=$(systemctl show -p InvocationID --value homesynapse.service); echo "INV=$INV"; sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -cE "Configuration issue"; sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -E "lifecycle\.integration_schema_registered|zigbee\.(network_resumed|network_formed|port_identity_captured)" | head -4
# expect: Configuration issue count 0 (PKG-SEC-2: R-4's C-1 is GONE) · exactly ONE lifecycle.integration_schema_registered: type=zigbee stage=pre-load · network_resumed: channel=20 panId=0x774c · ZERO network_formed. ⏺ all. (A WARN for a key you flagged at §3 is expected and ⏺'d.)
```
```bash
# WHERE: the held card. ONLY IF §0 chose the FAILCHAN artifact — the §6-B proof on hardware: ONE clean stop, read the grade, start again. (ef02d13's artifact: SKIP this block; ⏺ "stop-proof: skipped (ef02d13)".)
sudo systemctl stop homesynapse.service; sleep 2; systemctl show -p Result -p ActiveState -p ExecMainStatus homesynapse.service; sudo systemctl start homesynapse.service; sleep 25; systemctl is-active homesynapse.service
# expect: Result=success · ActiveState=inactive · ExecMainStatus=143 → active. ⏺ all. (Result=exit-code/ActiveState=failed = the lie is still there — a FINDING; paste; the day continues.)
```
**STOP-GATE R4b-3:** zero Configuration issue · the schema line once · resumed, zero formed (· the stop grades success if FAILCHAN rides).

## §6 THE ARM — criterion 0 (the window timed to the plug's cadence; ONE window, three provocations)
**Why the timing:** the S31 Lite zb plug (`nwk=0xf87d`) reports on a fixed **5-minute cadence at :54 s** (R-4 record: 17:18:54 · 17:23:54 · 19:18:54 · 19:33:54 → minutes ≡ 3 mod 5). The window is at most 254 s. **Open it at a minute ≡ 0 mod 5, between :20 s and :40 s** (e.g. xx:20:30 → closes xx:24:44 — the :23:54 report lands inside). Provoke traffic inside the window anyway (below) so criterion 0 does not depend on the cadence.
```bash
# WHERE: the held card. Step 0a — SET the key (254 = spec max; the R-4 record accepted it unclamped). Delete nothing.
sudo sed -i '1a permit_join_duration: 254' /etc/homesynapse/config/integrations/zigbee.yaml && sudo cat /etc/homesynapse/config/integrations/zigbee.yaml | head -4
# expect: permit_join_duration: 254 as line 2. ⏺.
```
```bash
# WHERE: the held card. Watch the clock; at a minute ≡ 0 mod 5 and :20–:40 s, restart. ⏺ the Z time + the two lines.
date -u +%H:%M:%SZ; sudo systemctl restart homesynapse.service; sleep 20; INV=$(systemctl show -p InvocationID --value homesynapse.service); sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -E "zigbee\.(network_resumed|permit_join_opened|permit_join_clamped)" | tail -3
# expect: network_resumed ch20 PAN 0x774c · permit_join_opened: duration=254s (NO clamped line). WINDOW-OPEN = that line's time; WINDOW-CLOSE = +254 s. ⏺.
```
**The three provocations (inside the window; note the clock on each; one act per line):**
1. **t+15 s — press the S31 plug's button ONCE** (a short press toggles it; a plug reports its On/Off state immediately). Expected within seconds: `zigbee.rejoin_candidate: device=0x00124B002FA8D1C5 nwk=0xf87d source=unknown_sender` — **THIS IS CRITERION 0** (the 0x0061 lookup's first real-silicon ⏺) → the interview walk → `zigbee.device_proposed … source=rejoin` → `zigbee.proposal_accepted … source=config` → `zigbee.device_adopted` → `reporting_configured` → `entity_registered`.
2. **t+60 s — wave a hand in front of the SNZB-03P** (motion; do NOT press its button). Expected: an occupancy report → `rejoin_candidate: device=0xF044D3FFFE9C78D7 …` → the same chain (a battery end device may stay silent — not a stop).
3. **t+100 s — flick the Hue ONCE at the wall** (off ~10 s, on). Expected: `rejoin_candidate: device=0x00178801101A09BB …` → the chain (a router rejoin may instead arrive as an accepted 0x0024 rejoin — the H-i path — same chain, no lookup line).
```bash
# WHERE: the held card, at WINDOW-CLOSE + 30 s. The harvest — ⏺ WHOLE.
INV=$(systemctl show -p InvocationID --value homesynapse.service); sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -E "zigbee\.(rejoin_candidate|rejoin_candidate_unresolved|lookup_eui64_failed|rejoin_ignored_window_closed|device_proposed|proposal_accepted|proposal_rejected|device_adopted|reporting_configured|interview)|entity_registered|registry\.projection_live|ingestion_unknown_sender" | head -60
```
**READ THE HARVEST (the hub reads it with you; three branches, each keyed to a token):**
- `rejoin_candidate` ×≥1 AND `device_adopted` ×≥1 → **criterion 0 MET, adoption(s) MET** → §7.
- `rejoin_candidate` ×≥1 but NO `device_adopted` → the lookup WORKED and the pipeline stalled later: ⏺ every `device_proposed`/`proposal_rejected`/`interview` line; the hub adjudicates in ≤10 min (a second window is lawful — restart again at the next ≡ 0 mod 5 minute).
- `lookup_eui64_failed: nwk=0x… status=0x…` + `rejoin_candidate_unresolved … reason=lookup_miss` and NO candidate → **CRITERION 0 MISSED — the status byte is the day's finding (⏺ it whole); THE FALLBACK (b) FIRES NOW (Row 12, your EDIT):** §6-F.

### §6-F THE ANNOUNCE-CLASS FALLBACK (only on a criterion-0 miss)
The announce path is the one the shipped pipeline has ALWAYS had (M9.4). **Factory-reset the S31 plug** so it LEAVES and RE-JOINS as an announce: hold its button ~5 s until the LED blinks fast (pairing mode) — inside a fresh window (restart again at a ≡ 0 mod 5 minute). Expected: `zigbee.device_announce: … 0x00124B002FA8D1C5` → `device_proposed … source=announce` → `proposal_accepted: source=config` → `device_adopted` → `entity_registered`. ⏺ the harvest block again. The plug is then the held card's adopted actuator; C4 re-scopes to it (§7, path B). (The Hue is NOT factory-reset today — the 6× dance is unreliable; the plug is enough for an honest C4.)

## §7 C4 — the re-bind (the held card's OWN entities) and the run
```bash
# WHERE: the held card. Who is registered now? The labelled token block, then the two reads. ⏺ both JSONs (no token appears in them).
TOK=$(sudo homesynapse-token | grep -oE '[A-Za-z0-9+/=_-]{40,}' | tail -1); test ${#TOK} -ge 40 && echo TOKLEN-OK; curl -s -H "Authorization: Bearer $TOK" http://127.0.0.1:7070/api/v1/entities | head -c 1500; echo; curl -s -H "Authorization: Bearer $TOK" http://127.0.0.1:7070/api/v1/automations | head -c 1200; echo
# expect: TOKLEN-OK · entities: the two pre-existing (01M19RHWXYZYJMM26SX0E41HXN · 01M19XN7NNQQ8S3JJF09T6YKKY) PLUS the newly registered ones (one per adopted device; a Hue bulb may register more than one) · automations: bench-hero present, lastRunId null.
```
```bash
# WHERE: the held card. Map the new entity ids to devices: the newest entity_registered lines carry the device. ⏺.
INV=$(systemctl show -p InvocationID --value homesynapse.service); sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -E "entity_registered|device_adopted" | tail -8
```
**Choose the path (the hub confirms in ≤5 min):** **Path A (the original bench-hero):** the SNZB-03P is adopted (its entity id = MOTION) AND the Hue is adopted (its light entity id = LIGHT) → trigger MOTION `occupied → true`, five actions on LIGHT (as the yaml has them). **Path B (re-scoped):** the plug is adopted (entity id = PLUG) → trigger PLUG `on → true`; actions: `turn_on` LIGHT (if adopted) else replace the five actions with ONE `turn_off` PLUG after `PT10S` — a run whose action the plug CONFIRMS by its own state report.
```bash
# WHERE: the held card. The re-bind: copy aside, then edit ONLY the entity_ref values (sudo nano — one id per line; save). Then DISARM (remove the window key) and restart.
sudo cp /etc/homesynapse/config/homesynapse.yaml /root/r4b-history/homesynapse.yaml.pre-rebind && sudo nano /etc/homesynapse/config/homesynapse.yaml
sudo sed -i '/^permit_join_duration:/d' /etc/homesynapse/config/integrations/zigbee.yaml && sudo systemctl restart homesynapse.service && sleep 25 && INV=$(systemctl show -p InvocationID --value homesynapse.service) && sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -cE "permit_join_opened|Configuration issue"
# expect: 0 (no window, no config issue after the edit; a non-zero = paste — the yaml edit is wrong, fix before the trigger). ⏺.
```
```bash
# WHERE: the held card. ⏺ ROWS-W0 + the Z time — THE ≥45-MIN WINDOW OPENS HERE (C2/C3 count from this line).
sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'; date -u +%H:%M:%SZ
```
**THE TRIGGER (one act; note the clock):** Path A — walk in front of the SNZB-03P. Path B — press the plug's button ONCE (on). Expected within ~10 s: the run.
```bash
# WHERE: the held card, ~60 s after the trigger. The run + the explanation. ⏺ both whole (the JSON carries no token).
TOK=$(sudo homesynapse-token | grep -oE '[A-Za-z0-9+/=_-]{40,}' | tail -1); test ${#TOK} -ge 40 && echo TOKLEN-OK; curl -s -H "Authorization: Bearer $TOK" http://127.0.0.1:7070/api/v1/runs | head -c 1500; echo; curl -s -H "Authorization: Bearer $TOK" http://127.0.0.1:7070/api/v1/automations | head -c 800; echo
# expect: runs data ≥1 with bench-hero's id; automations: bench-hero lastRunId NOT null. C4's "rendered explanation": open an ssh tunnel (desktop: ssh -i ~/.ssh/id_ed25519_pi -L 7070:127.0.0.1:7070 nick@hs-fresh.local) → browser http://127.0.0.1:7070/dashboard/ (if the dashboard asks for a bearer token, paste the labelled block's token into the BROWSER only — never into chat) → the run in the explain hero → ⏺ a screenshot + the verdict word it renders (CONFIRMED / ACTED_BUT_UNCONFIRMED). Either verdict is evidence; the hub words C-002 on what rendered. If the dashboard cannot be reached, the run detail JSON (`/api/v1/runs/<id>`, ⏺ whole) is the rendered explanation of record for today and H8 carries the visual.
```

## §8 The evidence window (C1 · C2 · C3) — at ≥45 min after ROWS-W0
```bash
# WHERE: the held card. ⏺ WHOLE.
sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'; date -u +%H:%M:%SZ; INV=$(systemctl show -p InvocationID --value homesynapse.service); sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -ciE "NoClassDefFoundError|jdk.jfr|BusMetrics"; sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -cE "zigbee\.network_resumed"; sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -cE "zigbee\.network_formed"
# expect: ROWS-W1 > ROWS-W0 · throw-discriminator 0 · resumed ≥1 · formed 0.
```
```bash
# WHERE: the held card. C2 store-freshness — the schema read is the instrument (never invent column names): ⏺ the .schema line, then the two newest rows.
sudo sqlite3 -readonly /var/lib/homesynapse/data/homesynapse-events.db '.schema events'
```
Then, using the schema's own timestamp column: `sudo sqlite3 -readonly … "SELECT <pos-col>, <type-col>, <time-col> FROM events WHERE <type-col> IN ('state_reported','availability_changed') ORDER BY <pos-col> DESC LIMIT 2;"` — expect both timestamps INSIDE the window. ⏺.
**STOP-GATE R4b-4 (the lift gate — ⏺ each):** C1 resumed ✓ · C2 ≥1 AVAILABLE + freshness in-window ✓ · C3 rows delta + discriminator 0 ✓ · C4 one run + a rendered explanation on the held card's own entities incl. a device adopted TODAY ✓. **FOUR OF FOUR → C-002 mints tonight (the hub's act).** A miss → paste either way; the hub adjudicates what the record supports; nothing is said publicly either way.

## §9 The restore (the bench night)
```bash
# WHERE: the held card. The clean stop — with the FAILCHAN artifact this reads inactive/success; with ef02d13's it reads failed/143 (the known lie; ⏺ without alarm). Then power OFF → held card OUT (re-label: hs-fresh — R-4b DONE — <artifact sha> · shipped unit) → bench card IN → power ON → ~90 s.
sudo systemctl stop homesynapse.service; sleep 2; systemctl show -p Result -p ActiveState -p ExecMainStatus homesynapse.service; sudo shutdown -h now
```
```bash
# WHERE: the bench card (ssh pi). Start the floor yourself, then the boot-health scenario.
~/bench.sh status; ~/bench.sh start; sleep 45; ~/bench.sh status; ~/bench.sh scenario boot-health; grep -E "zigbee\.(port_identity_captured|network_resumed)" ~/hs-bench/current.log | tail -2
# expect: NOT running → start → running → [PASS] boot-health — 6/6 positive · 0 forbidden → network_resumed: channel=20 panId=0x774c. ⏺ all. A changed PAN = STOP, paste.
```

## §10 What the hub banks tonight
The operator record (every ⏺, in order, with your clock notes) → the two-layer audit → **C-002's sentence**, worded on exactly what rendered (Path A or B; CONFIRMED or ACTED_BUT_UNCONFIRMED; the artifact sha; the window; the criterion-0 line quoted) → the register row → the docket Row 12 closed → the FAILCHAN stop-proof banked (if it rode) → the F-R4-1 silicon surface ADJUDICATED either way (a `lookup_eui64_failed status=0x..` is as valuable a datum as a candidate line — it is the one thing no desk could measure).
