<!--
file: context/instructions/2026-10-07_bench-card_PKG-FRESH-1_fresh-card-install_49455fc-deb_operator-session-prompt.md
purpose: PKG-FRESH-1 — the fresh-card install (D-v97-7 `FRESH-CARD: oct8-11`; the strategy pass S1 (a); gate (i)'s instrument five weeks early): a SECOND SD card with fresh Raspberry Pi OS Lite (64-bit) in the SAME Pi (hs-dev-1's board), the CI-built arm64 `.deb` of `main` `49455fc` installed with `apt`, timed against the release plan's row 34 (30 minutes), the first-run token read, `/health` 200 on loopback, the LAN opt-in as its own timed block, the dashboard at `/` recorded, then THE SWAP-BACK (the held card in, the dongle back, the Core relaunched, boot-health at the fleet of 10). Nick's two fences (D-v97-7) bind every block: (1) THE FLEET'S COORDINATOR NEVER MEETS THE FRESH CARD — the dongle is unplugged BEFORE the fresh card boots and replugged only AFTER the held card is back (a fresh install that reached the NCP could FORM on it; `network_formed` = POWER OFF + STOP); (2) HARDWARE IN SERIES — one hands act at a time, the swap-back is the restore, boot-health on the held card is read before the gap closes. Cut from DIST-CENSUS (`context/audits/2026-10-07_v99_DIST-CENSUS_rows-33-35_at-49455fc.md`: no blocker; the runtime bundled; the artifact CI-built; two frictions pre-registered). Nothing here is a fix; every red is a J8-class row with a month of slack.
audience: Nick (Part 0 on the desk — DONE Thu 10-08: debs=1, FLASHED hs-fresh-1; Parts A–E at the rig in ONE sitting, Sat 2026-10-10 morning, ≤ 2 h; pastes this file WHOLE into a FRESH Cowork conversation with ClaudeFolder connected at the sitting's start) · the guide session (one block at a time; never adjudicates) · the hub that intakes (two layers at the bytes; the §P order)
state-type: operator card (bench; the rig; one sitting + a desk hour)
status: EXECUTED — STOPPED at A3 (10:26 CT: the card in the Pi was hs-fresh, not a fresh flash); the fence-1 breach at D1's swap-back (10:46–10:55 CT; no form, nothing sent); the restore by the v104 rulings (R1–R4, R2 by name) → D2's cold-start failure (IR-148) → W1 + D2b PASS 6/6, the fleet's Core back 12:00:49 CT; INTAKEN v104 b1 (Sat 2026-10-10 ~12:1x CT; D-v104-6; `context/audits/2026-10-10_v104-b1_boot_restore_PKG-FRESH-1_intake_two-layer_audit.md`); the re-sit is PKG-FRESH-1b (a third card; hostnames only; the identity gate before the dongle). Was: RUNNING — LAUNCHED Sat 2026-10-10 08:46 CT (Nick; D-v103-21); PRE-A and the 0a STOP RULED before A1 (D-v103-28: known_hosts (a) with a `pi` guard; the stale `ef02d13` artifact renamed, `49455fc`'s re-downloaded); its one line goes to v104. Was: DISPATCH-READY — RE-STAMPED for Sat 2026-10-10 MORNING at v103 beat 3 (Sat 2026-10-10 ~08:33 CT; instrument 2026-10-10T13:33:23Z): Nick asked for it at 08:31 CT — the sitting pulled forward from Sunday (the Pi on `37f05a9` since BC9a; tonight's soak S0 not before ≈ 21:00, so the swap-back has the day to settle); the guide's day; the outputs and guide-notes names and D1's label `2026-10-10_`; the start gate 20:30 → 10:00 CT and Part E's close 22:00 → 12:00 CT; the evening words → the sitting; every command, EXPECTED and pre-registration otherwise unchanged; the dry-run re-run (`_scratch/v103/b3/fresh1_dry-run_v103.txt`). Was: DISPATCH-READY — RE-STAMPED for Sun 2026-10-11 ≈ 19:00 at v101 beat 1 (Fri 2026-10-09 ~09:0x CT; instrument 2026-10-09T14:06:35Z; D-v101-7): the guide's day, the outputs and guide-notes names `2026-10-11_`, the STATE slot (`BC9a/BC9:`), A1's core-clone EXPECTED (`37f05a9` OR `df2bc62`), D1's label; every command and both clock gates (20:30 · 22:00) untouched; the dry-run re-run COMPLETE (`_scratch/v101/fresh1/fresh1_dry-run_v101.txt`). Was: DISPATCH-READY — MOVED to Sun 2026-10-11 ≈ 19:00 (D-v100-12, v100 beat 3, Thu 2026-10-08 ~21:2x CT): not sat Thu 10-08 — Nick reached the card at 21:12 CT and its own 20:30 gate stops it; Part 0 DONE (debs=1; FLASHED hs-fresh-1); the body UNTOUCHED — v101 re-stamps the day words, the clock words, the outputs name `2026-10-11_` and the STATE slots by D-v99-5's script form and re-runs the dry-run. Was: DISPATCH-READY — cut v99 beat 2 (Wed 2026-10-07 ~20:0x CT; instrument 2026-10-08T01:00:36Z) from DIST-CENSUS at core `49455fc`; dated for Thu 2026-10-08 and RE-STAMPED by the hub (D-v99-5) if the evening moves inside `FRESH-CARD: oct8-11`; the dry-run on the desk `_scratch/v99/fresh1/fresh1_dry-run_v99.txt`; flips to EXECUTED at the hub's intake. Nick never edits this file.
-->

You are the PKG-FRESH-1 GUIDE for NexSys / HomeSynapse on Sat 2026-10-10 morning. You are NOT the hub and you never re-plan: you hold six parts (0, A, B, C, D, E — below, verbatim; A–D have numbered sub-blocks), you show Nick ONE block at a time, you read each block's EXPECTED line against what he pastes, and you say either "next" or "STOP — paste the block's output to the hub; nothing else is run". The rules: every rig block tees to `~/Desktop/Code/ClaudeFolder/_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_outputs.txt` (the file the hub reads); `pi` is the ssh alias of the HELD card (hs-dev-1); the FRESH card is reached as `nick@<IP>` with the key `~/.ssh/id_ed25519_pi` (you fill `<IP>` from Part A3's answer into every later block before you show it); nothing is deleted on either card; no `--allow-downgrades`; no token printed; `network_formed` in ANY output = POWER OFF the Pi and STOP; if a block's output does not match its EXPECTED line that is a STOP — you do not improvise a fix; the only act allowed before the hub answers is Part D (the restore) if the held card is out. **THE TWO FENCES:** the dongle (the Zigbee coordinator's USB stick) is OUT of the Pi from A2 until D1 — you ask Nick to confirm `dongle-out yes` before the fresh card powers on and `dongle-in yes` only after the held card is back; one hands act per block. A Pi timestamp is EDT = CT + 1; a `Z` is UTC = CT + 5 — write both, never convert in your head. The clock of the install is the fresh card's own `date -u` inside the blocks (T0 … T3); you compute T1 − T0 and T3 − T2 and write them.

Before Part A, ask Nick for ONE STATE line: `STATE: HIVE: LANDED <sha> · BC9a/BC9: <the Pi's sha from the newest card, or 'not run'> · the fresh card flashed: yes/no · the artifact on the desk: yes/no (Part 0) · the time is <HH:MM CT>`. If Part 0 is not done, STOP (Part 0 is desk work; the sitting starts at A1). If the time is past 10:00 CT, STOP before Part A — say back `PKG-FRESH-1: STOP (<HH:MM> CT)` (the hub re-plans by id; tonight's soak is not before ≈ 21:00 in any case). When Part E's line is said, write your guide notes file (`~/Desktop/Code/ClaudeFolder/_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_guide-notes.md` — the one line back · the record · per-block verdicts · the readings · observations · what this card did not verify · card discipline), tell Nick the one line to paste to the hub, and stop.

# PKG-FRESH-1 — fresh Raspberry Pi OS on a second card; `main@49455fc`'s arm64 `.deb` by `apt`; timed; the LAN opt-in; the swap-back

## Part 0 — the desk, before the sitting (DONE Thu 10-08: debs=1, FLASHED hs-fresh-1 — re-run only if the STATE line says the artifact or the card is missing; no rig; ≈ 25 min; two pastes and one GUI)
### 0a — the artifact of record (the browser, then one paste)
In the browser: `https://github.com/nexsys-io/homesynapse-core/actions/workflows/install-smoke.yml` → the newest run on `main` for `49455fc` (event push, Sun 10-04 ≈ 16:3x CT) → its conclusion (✅ or ❌ — write it) → the **arm64** job → the step "Version-grammar echo" → copy the whole `version-grammar echo green: … sha256 <64 hex>  homesynapse_0.1.0+git<…>.g49455fc_arm64.deb` line → the run's Summary → Artifacts → `distribution-artifacts-arm64` → it downloads to `~/Downloads`. **If the run's conclusion is ❌, or the artifact is gone (7-day retention — ≈ Sun 10-11 16:3x CT): STOP and tell the hub** (`workflow_dispatch` on `main` mints a fresh one; the hub says the word). Then, in Git Bash:
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_outputs.txt; mkdir -p "$(dirname "$OUT")" ~/fresh1-artifact; { echo "=== 0a $(date -u +%Y-%m-%dT%H:%M:%SZ)"; cd ~/fresh1-artifact && powershell.exe -NoProfile -Command "Expand-Archive -LiteralPath \"$(cygpath -w ~/Downloads/distribution-artifacts-arm64.zip)\" -DestinationPath \"$(cygpath -w ~/fresh1-artifact)\" -Force" && echo "debs=$(find . -name '*_arm64.deb' | wc -l)" && find . -name '*_arm64.deb' -exec sha256sum {} \; && find . -name '*_arm64.deb' -exec dpkg-deb --field {} Version Architecture Depends \; 2>/dev/null || echo "dpkg-deb absent on the desk — the Pi reads the fields at B1"; } 2>&1 | tee -a "$OUT"
# EXPECTED: debs=1 · the sha256 EQUALS the echo line's · the name carries g49455fc · (if dpkg-deb exists on the desk) Version 0.1.0+git….g49455fc · arm64 · Depends: adduser. debs ≠ 1 or a hash mismatch → STOP, paste.
```
### 0b — the fresh card (Raspberry Pi Imager; the GUI — one line back)
Raspberry Pi Imager on the desk → Device: the Pi's model → OS: **Raspberry Pi OS Lite (64-bit)** (Bookworm) → Storage: the SECOND SD card (NOT the held card — it is in the Pi) → OS customisation: hostname `hs-fresh-1`; username `nick` with a password you choose; **Services → Enable SSH → "Allow public-key authentication only"** → paste the ONE line printed by the block below; the LAN as the held Pi has it (Ethernet needs nothing; Wi-Fi: the same SSID). Write. Label the card **FRESH-1**. Say back `FLASHED: hs-fresh-1 · <Ethernet|Wi-Fi> · <HH:MM CT>`.
```bash
cat ~/.ssh/id_ed25519_pi.pub
# EXPECTED: one line beginning ssh-ed25519 — the key the held card already trusts (R-4c's `-i ~/.ssh/id_ed25519_pi`). No line → STOP (the key is elsewhere; the hub finds it).
```

## Part A — the swap (the rig; THE HANDS ACT in series; ≈ 10 min)
### A1 — the held card's state before the gap (reads; nothing changes)
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_outputs.txt; { echo "=== A1 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh pi 'hostname; echo "pi-clock $(date -u +%H:%M:%SZ)"; echo "core-clone: $(cd ~/homesynapse-core && git --no-optional-locks log -1 --oneline | cut -c1-40) ref=$(cd ~/homesynapse-core && git --no-optional-locks rev-parse --abbrev-ref HEAD) porcelain=$(cd ~/homesynapse-core && git --no-optional-locks status --porcelain | wc -l)"; ~/bench.sh status 2>&1 | tail -1; L=~/hs-bench/current.log; echo "boot-log: $(basename $(readlink -f $L)) bytes=$(wc -c < $L) formed=$(grep -c zigbee.network_formed $L) relinked=$(grep -c device_relinked $L)"; ~/bench.sh entities | python3 -c "import sys,json; d=json.load(sys.stdin); d=d[\"data\"] if isinstance(d,dict) and \"data\" in d else d; print(\"registry rows=%d unavailable=%s\" % (len(d), [r[\"entityId\"][-6:] for r in d if r.get(\"availability\")!=\"AVAILABLE\"]))"; lsusb 2>/dev/null | grep -i -c "silicon labs\|cp210\|zigbee\|sonoff\|10c4" '; } 2>&1 | tee -a "$OUT"
# EXPECTED: hs-dev-1 · core-clone: 37f05a9 … ref=HEAD (BC9a ran) OR df2bc62 … ref=HEAD (it did not — RECORD, not STOP) · porcelain=0 · running (pid <n>) · boot-log: bench-2026-10-0<d>-<Pi-stamp>.log formed=0 relinked=<9|10> · registry rows=10 unavailable=['DHE40F'] (±'FT4HWQ' — RECORD) · the last number ≥ 1 (the dongle is present NOW; WRITE IT — A2 removes it). STOP: formed ≠ 0 (POWER OFF) · rows ≠ 10.
```
### A2 — the clean shutdown, THE DONGLE OUT, the cards swapped (Nick's hands)
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_outputs.txt; { echo "=== A2 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh pi '~/bench.sh stop 2>&1 | tail -1; sync; echo "poweroff-sent $(date -u +%H:%M:%SZ)"; sudo systemctl poweroff' 2>&1 | tail -3; echo "desk-clock $(date -u +%H:%M:%SZ)"; } 2>&1 | tee -a "$OUT"
# EXPECTED: stopped · poweroff-sent <Z> · the ssh connection closes (a "Connection closed" line is lawful). Then, HANDS, in THIS order, one at a time: (1) wait until the Pi's green activity LED has been dark ≈ 20 s; (2) UNPLUG THE DONGLE (the Zigbee USB stick) and set it beside the keyboard — it does not go back until D1; (3) unplug the Pi's power; (4) the HELD card OUT — label it HELD if it is not; (5) the FRESH-1 card IN; (6) power ON; (7) wait 90 s. Say back ONE line: `SWAP: <HH:MM:SS CT> dongle-out yes`. The guide does not show A3 until it reads `dongle-out yes`.
```
### A3 — first contact with the fresh card (the IP; the OS; the clock)
```bash
ping -n 2 hs-fresh-1.local 2>&1 | tail -2
# EXPECTED: a reply from <IP> (write it). No reply → the router's client list (hostname hs-fresh-1) or `arp -a | grep -i "b8-27-eb\|dc-a6-32\|e4-5f-01\|d8-3a-dd\|2c-cf-67"` in Git Bash — one of these gives <IP>; still nothing after 3 minutes → STOP (the card did not boot or did not join the LAN — the Imager settings are the first suspect; nothing is lost: the held card goes back in at D1).
```
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_outputs.txt; { echo "=== A3 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh -o StrictHostKeyChecking=accept-new -i ~/.ssh/id_ed25519_pi nick@<IP> 'hostname; uname -m; . /etc/os-release; echo "$PRETTY_NAME"; echo "pi-clock $(date -u +%H:%M:%SZ)"; df -h / | tail -1; lsusb 2>/dev/null | grep -i -c "silicon labs\|cp210\|zigbee\|sonoff\|10c4"; dpkg -l homesynapse 2>/dev/null | tail -1 || echo "homesynapse: not installed"; systemctl is-active homesynapse.service 2>/dev/null || true'; } 2>&1 | tee -a "$OUT"
# EXPECTED: hs-fresh-1 · aarch64 · Debian GNU/Linux 12 (bookworm) · the Pi's clock within a minute of the desk's (NTP) · the root filesystem with ≥ 2 GB free · the dongle count 0 (FENCE 1 PROVED on the fresh card) · "not installed" · inactive. STOP: aarch64 missing (a 32-bit image was flashed) · the dongle count ≥ 1 (the dongle is in — POWER OFF, remove it, restart A2's hands list).
```

## Part B — THE INSTALL, timed against row 34's 30 minutes (the fresh card; ≈ 6 min)
### B1 — T0; the `.deb` to the fresh card; the hash and the fields
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_outputs.txt; { echo "=== B1 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; echo "T0=$(date -u +%H:%M:%SZ)"; cd ~/fresh1-artifact && scp -i ~/.ssh/id_ed25519_pi $(find . -name '*_arm64.deb') nick@<IP>: && ssh -i ~/.ssh/id_ed25519_pi nick@<IP> 'sha256sum ~/homesynapse_*_arm64.deb; dpkg-deb --field ~/homesynapse_*_arm64.deb Version Architecture Depends'; } 2>&1 | tee -a "$OUT"
# EXPECTED: T0=<Z> (WRITE IT — the install clock starts here) · the SAME sha256 as 0a · Version: 0.1.0+git<date>.<time>.g49455fc · Architecture: arm64 · Depends: adduser (the runtime is INSIDE the package — DIST-CENSUS §2). A hash mismatch → STOP.
```
### B2 — `apt install` (a FRESH install, no flag); the service; the bundled runtime; `/health` on loopback
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_outputs.txt; { echo "=== B2 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh -i ~/.ssh/id_ed25519_pi nick@<IP> 'bash -s' <<'EOF_B2'
echo "apt-start $(date -u +%H:%M:%SZ)"; sudo apt install -y ~/homesynapse_*_arm64.deb 2>&1 | tail -14; echo "apt-end $(date -u +%H:%M:%SZ) rc=${PIPESTATUS[0]}"
echo "dpkg-version=$(dpkg-query -W -f '${Version}' homesynapse) opt-version=$(cat /opt/homesynapse/VERSION 2>/dev/null)"
sleep 5; echo "unit=$(systemctl is-active homesynapse.service) enabled=$(systemctl is-enabled homesynapse.service 2>/dev/null)"
echo "runtime: $(/opt/homesynapse/runtime/bin/java -version 2>&1 | head -1) arch=$(file -b /opt/homesynapse/runtime/bin/java 2>/dev/null | cut -c1-40)"
echo "listen: $(sudo ss -ltnp 2>/dev/null | grep ':7070' | awk '{print $4}' | tr '\n' ' ')"
echo "health=$(curl -s -m 5 -o /dev/null -w '%{http_code}' http://127.0.0.1:7070/health) T1=$(date -u +%H:%M:%SZ)"
EOF_B2
} 2>&1 | tee -a "$OUT"
# EXPECTED: an install tail with `Setting up homesynapse (0.1.0+git….g49455fc)` and the postinst's `HomeSynapse Core is running.` (its alternative line `was installed but did not start cleanly` = RECORD and go on to B3 — the log tells why) · rc=0 · dpkg-version = opt-version = the g49455fc build · unit=active enabled=enabled · runtime: `openjdk version "21…"` arch=`ELF 64-bit … ARM aarch64` (the arch-truth proof on silicon) · listen: 127.0.0.1:7070 (LOOPBACK — the product as shipped; the LAN opt-in is Part C) · health=200 · T1=<Z>. **The guide writes `install→200 = T1 − T0` in seconds** (row 34's envelope is 1800 s; the number is the finding either way). STOP only on rc ≠ 0 with no unit at all (`unit=inactive`+`not-found`); everything else is RECORDED.
```
### B3 — the first-run token (never printed); the empty registry; the coordinator-absent posture in the log
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_outputs.txt; { echo "=== B3 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh -i ~/.ssh/id_ed25519_pi nick@<IP> 'bash -s' <<'EOF_B3'
TOK=$(sudo cat /var/lib/homesynapse/config/initial_api_token | tr -d '\r\n'); echo "token_len=${#TOK}"; [ "${#TOK}" -ge 40 ] && echo TOKLEN-OK
echo "token-verb: $(homesynapse-token 2>&1 | wc -c) bytes printed by the verb (the value stays on the Pi)"
curl -s -m 5 -o /tmp/ent.json -w "entities http=%{http_code} bytes=%{size_download}\n" -H "Authorization: Bearer $TOK" http://127.0.0.1:7070/api/v1/entities
python3 -c "import json; d=json.load(open('/tmp/ent.json')); d=d['data'] if isinstance(d,dict) and 'data' in d else d; print('registry rows=%d' % len(d))"
echo "formed-lines=$(sudo journalctl -u homesynapse.service -b --no-pager | grep -c 'zigbee.network_formed') port-identity=$(sudo journalctl -u homesynapse.service -b --no-pager | grep -c 'zigbee.port_identity_captured')"
echo "--- zigbee posture (first 6 lines naming the coordinator, the serial device or the integration's state):"; sudo journalctl -u homesynapse.service -b --no-pager | grep -i 'coordinator\|serial\|/dev/tty\|zigbee' | head -6 | cut -c1-220
echo "--- config issues: $(sudo journalctl -u homesynapse.service -b --no-pager | grep -c 'Configuration issue')"; echo "T-posture $(date -u +%H:%M:%SZ)"
EOF_B3
} 2>&1 | tee -a "$OUT"
# EXPECTED: token_len ≥ 40 and TOKLEN-OK · the verb prints a few dozen bytes (the token's path or value — the count only) · entities http=200 · registry rows=0 (a fresh store — the fence's proof at the API: nothing of ours is here) · formed-lines=0 (there is no NCP to form on) · port-identity=0 · the posture lines name the ABSENT coordinator or serial device in the integration's own words — WRITE THEM WHOLE (a product finding: what a household sees when the stick is not yet in) · config issues 0 (C-002's zero-warning boot holds on a fresh OS) — a number > 0 is RECORDED with the lines. STOP: http ≠ 200 with the unit active (the token or the API path moved — the hub reads).
```

## Part C — THE LAN OPT-IN, timed as its own act (the fresh card; ≈ 4 min; the second friction DIST-CENSUS §4 names)
### C1 — from the desk, BEFORE: the loopback bind seen from the LAN
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_outputs.txt; { echo "=== C1 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; curl -s -m 5 -o /dev/null -w "desk-health-before=%{http_code}\n" http://<IP>:7070/health || echo "desk-health-before=unreachable"; } 2>&1 | tee -a "$OUT"
# EXPECTED: desk-health-before=unreachable (or 000) — the product as shipped binds 127.0.0.1 (`common.sh:38`; AB-1); a household's browser cannot reach the dashboard until the opt-in. A 200 here = RECORD (the default moved) and skip C2.
```
### C2 — the opt-in (the env drop-in; one restart; T2 → T3)
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_outputs.txt; { echo "=== C2 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh -i ~/.ssh/id_ed25519_pi nick@<IP> 'bash -s' <<'EOF_C2'
echo "T2=$(date -u +%H:%M:%SZ)"; echo "env-before: $(sudo cat /etc/homesynapse/homesynapse.env 2>/dev/null | grep -v '^#' | grep -c .) uncommented lines"
echo 'HOMESYNAPSE_BIND_HOST=0.0.0.0' | sudo tee -a /etc/homesynapse/homesynapse.env >/dev/null; echo "env-after: $(sudo grep -c '^HOMESYNAPSE_BIND_HOST=0.0.0.0' /etc/homesynapse/homesynapse.env)"
sudo systemctl restart homesynapse.service; echo "unit=$(systemctl is-active homesynapse.service)"
echo "listen: $(sudo ss -ltnp 2>/dev/null | grep ':7070' | awk '{print $4}' | tr '\n' ' ')"; echo "health=$(curl -s -m 5 -o /dev/null -w '%{http_code}' http://127.0.0.1:7070/health) T3=$(date -u +%H:%M:%SZ)"
EOF_C2
} 2>&1 | tee -a "$OUT"
# EXPECTED: env-before 0 (the shipped conffile is comments only) · env-after 1 · unit=active (the restart waits for the 90 s probe) · listen: 0.0.0.0:7070 or *:7070 · health=200 · the guide writes `opt-in = T3 − T2` seconds. STOP: unit ≠ active after the restart (the opt-in broke the start — the hub reads the journal; D1 still runs).
```
### C3 — from the desk, AFTER: the dashboard (one paste + one line from the browser)
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_outputs.txt; { echo "=== C3 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; curl -s -m 5 -o /dev/null -w "desk-health-after=%{http_code}\n" http://<IP>:7070/health; curl -s -m 5 -o /dev/null -w "desk-root=%{http_code} type=%{content_type}\n" http://<IP>:7070/; } 2>&1 | tee -a "$OUT"
# EXPECTED: desk-health-after=200 · desk-root=<200|401|404> type=<text/html|application/json|…> — RECORDED, not judged. Then open http://<IP>:7070/ in the browser and say back ONE line: `DASHBOARD: renders | token-wall | 404 | blank · <HH:MM CT>`.
```

## Part D — THE SWAP-BACK = THE RESTORE (Nick's hands; the held card; the dongle back; the Core relaunched; ≈ 8 min)
### D1 — the fresh card off; the cards swapped back; THE DONGLE IN
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_outputs.txt; { echo "=== D1 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh -i ~/.ssh/id_ed25519_pi nick@<IP> 'sync; echo "poweroff-sent $(date -u +%H:%M:%SZ)"; sudo systemctl poweroff' 2>&1 | tail -2; echo "desk-clock $(date -u +%H:%M:%SZ)"; } 2>&1 | tee -a "$OUT"
# EXPECTED: poweroff-sent <Z>; the connection closes. HANDS, in THIS order: (1) the LED dark ≈ 20 s; (2) power OFF; (3) the FRESH-1 card OUT — label it `FRESH-1 · PKG-FRESH-1 2026-10-10 · g49455fc` and keep it (the artifact of the sitting); (4) the HELD card IN; (5) THE DONGLE BACK IN (the same USB port it came from); (6) power ON; (7) wait 120 s. Say back ONE line: `SWAP-BACK: <HH:MM:SS CT> dongle-in yes`. The guide does not show D2 until it reads `dongle-in yes`.
```
### D2 — the held card's boot; the Core relaunched; boot-health at the fleet of 10 (the gap closes here)
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_outputs.txt; { echo "=== D2 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh pi 'bash -s' <<'EOF_D2'
hostname; echo "pi-clock $(date -u +%H:%M:%SZ) uptime: $(uptime -p)"; echo "dongle=$(lsusb 2>/dev/null | grep -i -c 'silicon labs\|cp210\|zigbee\|sonoff\|10c4') by-id: $(ls /dev/serial/by-id/ 2>/dev/null | head -2 | tr '\n' ' ')"
echo "core-clone: $(git -C ~/homesynapse-core --no-optional-locks rev-parse --short HEAD) ref=$(git -C ~/homesynapse-core --no-optional-locks rev-parse --abbrev-ref HEAD)"; ~/bench.sh status 2>&1 | tail -1
~/bench.sh restart 2>&1 | tail -2; sleep 25; ~/bench.sh scenario boot-health 2>&1 | tail -3
L=~/hs-bench/current.log; echo "boot-log: $(readlink -f $L | xargs basename)"; echo "formed=$(grep -c 'zigbee.network_formed' $L) resumed=$(grep -c 'zigbee.network_resumed' $L) relinked=$(grep -c 'device_relinked' $L) config_issue=$(grep -c 'Configuration issue' $L)"
~/bench.sh entities | python3 -c "import sys,json; d=json.load(sys.stdin); d=d[\"data\"] if isinstance(d,dict) and \"data\" in d else d; print(\"registry rows=%d unavailable=%s\" % (len(d), [r[\"entityId\"][-6:] for r in d if r.get(\"availability\")!=\"AVAILABLE\"]))"
EOF_D2
} 2>&1 | tee -a "$OUT"
# EXPECTED: hs-dev-1 · uptime ≈ 2–3 min · dongle=1 with one by-id entry (the stick is back) · core-clone = A1's sha and ref · status: not running (a cold boot does not relaunch the bench's Core — the nightly does at 03:30; RECORD) · restart → launched · [PASS] boot-health — 6/6 positive · 0 forbidden · boot-log: bench-2026-10-0<d>-<Pi-stamp>.log (WRITE IT) · formed=0 resumed=1 · relinked ≥ 9 · config_issue=0 · registry rows=10 unavailable=['DHE40F'] (±'FT4HWQ' — the sensor needs its first frame; RECORD). STOP: formed ≠ 0 (POWER OFF — the standing law) · rows ≠ 10 · boot-health FAIL (the hub reads the log; the restore is DONE either way — the held card runs).
```

## Part E — the close (the desk; the capture home; the one line; ≈ 3 min; run it at 12:00 CT whatever block you are on — D1–D2 FIRST if the held card is out)
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_outputs.txt; D=~/Desktop/Code/ClaudeFolder/_scratch/v99/fresh1; { echo "=== E $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh pi 'L=~/hs-bench/current.log; echo "held: $(hostname) $(readlink -f $L | xargs basename) formed=$(grep -c zigbee.network_formed $L) rows=$(~/bench.sh entities | python3 -c "import sys,json; d=json.load(sys.stdin); d=d[\"data\"] if isinstance(d,dict) and \"data\" in d else d; print(len(d))")"'; echo "blocks: $(grep -c '^=== ' "$OUT") outputs: $OUT $(wc -c < "$OUT") B"; } 2>&1 | tee -a "$OUT"
# EXPECTED: held: hs-dev-1 <boot-log> formed=0 rows=10 · blocks ≥ 10 · the byte count (WRITE IT — it is the RETURNED slot).
```

## The one line back (paste it to the hub; every slot filled by the guide from the record)
`PKG-FRESH-1: g49455fc on hs-fresh-1 (bookworm aarch64) · install→200 <s>s (row 34: 1800) · rc=<0|n> unit=<active|…> runtime=<openjdk 21…|absent> · health 200 · entities 0 · posture <the coordinator-absent line, ≤ 12 words> · LAN before <unreachable|200> · opt-in <s>s → <200|fail> · dashboard <renders|token-wall|404|blank> · swap-back <PASS 6/6|FAIL> formed=0 rows=10 dongle-in · RETURNED _scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_outputs.txt <bytes>`

## The pre-registrations (the hub's; adjudicated at the intake IN THIS ORDER; the guide records, never rules)
1. **P1 — THE INSTALL COMPLETES** (gate (i)'s instrument): B2 `rc=0`, `unit=active`, `health=200`, with `install→200 = T1 − T0 ≤ 1800 s` (row 34). A red here is the first J8-class row — named by its block and its line, a month early.
2. **P2 — THE RUNTIME IS THE PACKAGE'S OWN** (DIST-CENSUS §2): `openjdk version "21…"` from `/opt/homesynapse/runtime/bin/java` on an `aarch64` ELF; no system Java installed or asked for (`Depends: adduser`).
3. **P3 — THE COORDINATOR-ABSENT POSTURE** (fence 1): `formed-lines=0`, `port-identity=0`, `registry rows=0`; the integration names the missing coordinator or serial device in its own words — the lines are a register row for the product's first-run wording (what a household reads before the stick is in).
4. **P4 — THE LOOPBACK FRICTION** (DIST-CENSUS §4 (2)–(3)): `desk-health-before=unreachable`, then after C2 `desk-health-after=200` with `opt-in = T3 − T2 ≤ 120 s`. Pre-registered as a FINDING either way: row 34's "dashboard live" has a hidden step today (the env drop-in + restart); the register row asks whether first-boot should print the LAN URL or offer the opt-in.
5. **P5 — THE DASHBOARD AT `/`**: `renders | token-wall | 404 | blank` — RECORDED with `desk-root=<code> type=<…>`; no arm is a red (the web-ui's packaging is FE-lane work; this is its first fresh-OS reading).
6. **P6 — THE RESTORE** (fence 2): D2 `formed=0`, `relinked ≥ 9`, `registry rows=10`, boot-health PASS 6/6, `dongle=1`; the gap (A2's `poweroff-sent` → D2's boot-log stamp) written in minutes; the fleet re-links to its own coordinator and nothing of the fresh card touched it (`rows=0` at B3 is the proof).
7. **P7 — THE ARTIFACT'S RETENTION** (DIST-CENSUS §3): 0a found the `49455fc` run and its artifact (or the hub re-minted one by `workflow_dispatch`); the sha256 identical on the run page, the desk and the card (B1) — C-002/C-003's four-surface form, one surface fewer.
THE RESTORE RUNS BEFORE THE GAP: no config is written on the HELD card; the only rig changes are the card swap and the dongle's absence between A2 and D1, both reversed in D1; the fresh card's own config (the env drop-in) stays on the fresh card, which is kept as the sitting's artifact. The dongle never meets the fresh card (A3's and D2's `lsusb` counts are the proof, 0 then 1).
