<!--
file: context/instructions/2026-09-11_R-4c_measurement-only_zdo-surface-C-003_navigator-packet.md
purpose: THE R-4c NAVIGATOR PACKET — one hardware session on the held card (hs-fresh), Saturday 2026-09-12: install the newest green install-smoke .deb (core 1e26912's run; its Java is eabdbb1's: F-R4-1b's ZDO surface + HONESTY-1), then MEASURE — the boot tokens as counts; lastReported read once on the new bytes (LASTREPORTED-1b); the card's gradle answer (card-gradle:); one permit-join window in which the sleepy SNZB-02P is admitted through the ZDO IEEE_addr_req surface on silicon (C-003, the exit); the six-device census; the DeliveryAnomaly count in the journal; the restore. No Core write; nothing on the core tree changes.
audience: Nick at the desktop and the rig · the R-4c navigator (a fresh Cowork window; §N is its paste) · the hub (§H is what it banks)
state-type: navigator packet (operator blocks in walk order; each block: WHERE · the command · EXPECTED · the ⏺ line)
status: LIVE — Sat 2026-09-12 at the rig (R4C: Sun moves it). Authored v70 beat 3 (Fri 2026-09-11 ~18:1x CT; instrument 2026-09-11T23:08:46Z) by range from the R-4b packet (archive/2026-09/2026-09-04_R-4b_navigator-packet_held-card.md), the R-4b record's findings card (context/audits/2026-09-04_R-4b_re-rep_operator-record.md §9), the H8-a packet's form (B0 pins the IP; counts, never heads; self-timing blocks) and F-R4-1b's return (context/audits/2026-09-06_F-R4-1b_return.md). The record you build as you go: context/audits/2026-09-12_R-4c_measurement-only_operator-record.md (scaffolded). Do not start before §0 is answered at the desktop. The hub asks nothing while you are at the rig.
-->

# R-4c — measurement only: the ZDO surface on silicon, lastReported on the new bytes (Sat 2026-09-12)

**GOAL.** On the held card, running the .deb of core `1e26912`'s install-smoke run (Java = `eabdbb1`: F-R4-1b's second over-the-air surface, HONESTY-1's `lastReported`), measure four things and change nothing on the core tree: (1) the boot tokens as counts; (2) `lastReported` read once — a never-reported entity shows `null`, a reporting entity shows an instant; (3) the card's gradle answer, one line; (4) inside ONE permit-join window, the sleepy SNZB-02P (`0xF044D3FFFED2A201`), which the coordinator's table missed in R-4b (`lookup_eui64_failed … status=0x1`), is resolved by `IEEE_addr_req` on the air and adopted — **C-003, the exit**. The other sleepy devices (SNZB-01P button, SNZB-04P contact) are provoked in the same window; the census of the six adopt IEEEs is recorded either way. The `bus.delivery_anomaly` count for the whole service invocation is read once at the end (FIX-1a's detector on the wire, zero expected). Then the bench night is restored.

**The rig rules (one line each):** `network_formed` anywhere = POWER OFF + STOP · s31 and the nightly untouched · never `--allow-downgrades` · delete nothing (move aside) · the token value never enters the record (`token_len=NN` + `TOKLEN-OK` is the line) · NEVER long-press any Sonoff button (5 s = factory reset; a short press only) · one window, disarmed before B5 · B5 outranks everything after B3 · nothing else while at the rig.

**Provenance in one line:** R-4b left the S31 adopted by `source=rejoin` (C-002), the SNZB-02P missed at `nwk=0x15ac status=0x1`, the Hue absent from the air (F-R4b-G, CONTESTED), the config at `/var/lib/homesynapse/config/` (D-3), the token file at `/var/lib/homesynapse/config/initial_api_token` (H8-a B2), the window key at line 2 of `integrations/zigbee.yaml` with the idempotency guard (D-7), counts instead of heads (D-6), `<IP>` pinned at B0 (D-4). H8-a (Friday night) installed `f25291b`'s .deb on this same card; B0's glance reads that version as the incumbent (or `…gef02d13` if H8-a did not install).

## §0 GUARD 1 — which artifact (DESKTOP; the browser; answer before §1)
GitHub → `nexsys-io/homesynapse-core` → Actions → the **install-smoke** workflow → the run whose commit is `1e26912` (`docs(dashboard): HERO-1 …`, 2026-09-11). **EXPECTED:** both jobs (amd64 · arm64) GREEN. ⏺ one line: `ARTIFACT: 1e26912 — run <URL> — amd64 <green|red> arm64 <green|red>`. **STOP:** any red or pending → the packet does not proceed to §1; paste the failing step's last 20 lines to the navigator. (The `ci` run on the same commit is RED at `lifecycle:test` — that is the FIX-2 class, read and filed at `context/audits/2026-09-11_CI-1e26912_red-read_HeroLoop-lifecycle_v70-b2.md`; it does not gate the .deb, which install-smoke builds and boots on its own.)

## §1 Fetch + hash (DESKTOP; browser + Git Bash)
Open the run → the **arm64** job → the step "Version-grammar echo" → ⏺ the whole `version-grammar echo green: … sha256 <64 hex>  homesynapse_0.1.0+git<…>.g1e26912_arm64.deb` line (the origin hash). Then Summary → Artifacts → `distribution-artifacts-arm64` → `~/Downloads`.
```bash
# WHERE: Git Bash. The zip nests at deb/build/. Old .debs move aside — delete nothing.
mkdir -p ~/r4c-artifact ~/r3-history && mv ~/r4c-artifact/*.deb ~/r3-history/ 2>/dev/null; cd ~/r4c-artifact && powershell.exe -NoProfile -Command "Expand-Archive -LiteralPath \"$(cygpath -w ~/Downloads/distribution-artifacts-arm64.zip)\" -DestinationPath \"$(cygpath -w ~/r4c-artifact)\" -Force" && find . -name '*_arm64.deb' | wc -l && find . -name '*_arm64.deb' -exec sha256sum {} \;
# EXPECTED: the count is 1 · the hash EQUALS the echo line's sha256 · the name carries g1e26912. ⏺ both lines. A count ≠ 1 or a mismatch → STOP, paste.
```
**STOP-GATE R4c-1:** one .deb · hash = the run log · `g1e26912` in the name.

## B0 — Preflight at the rig (the bench card OUT, the held card IN; the boot glance)
```bash
# WHERE: the BENCH card (ssh pi). The overnight digest first — the bench never goes down un-read. ⏺ the lines.
tail -2 ~/hs-bench/digests/nightly.log; ls -t ~/hs-bench/bundles | head -2; ~/bench.sh status
```
```bash
# WHERE: the BENCH card. The orderly halt. Then: power OFF at the wall → bench card OUT → held card IN (labelled hs-fresh) → power ON → wait ~90 s. Note the clock on the physical acts. The coordinator dongle STAYS in its port.
sudo shutdown -h now
```
```bash
# WHERE: Git Bash → the HELD card by NAME once (the first line MUST print hs-fresh); it prints the address you PIN for every hop after this — every <IP> below is that value.
ssh -i ~/.ssh/id_ed25519_pi -o StrictHostKeyChecking=accept-new nick@hs-fresh.local 'hostname; hostname -I; date -u +%H:%M:%SZ; dpkg-query -W -f "${Version}\n" homesynapse; cat /opt/homesynapse/VERSION; systemctl is-active homesynapse.service; INV=$(systemctl show -p InvocationID --value homesynapse.service); echo "INV=$INV"; sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -cE "zigbee\.network_formed"; sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -E "zigbee\.network_resumed" | tail -1; sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" "SELECT COUNT(*) FROM events;"; ls /var/lib/homesynapse/config/ /var/lib/homesynapse/config/integrations/; sudo grep -cE "^[[:space:]]*permit_join_duration:" /var/lib/homesynapse/config/integrations/zigbee.yaml'
# EXPECTED: hs-fresh · an IPv4 (PIN IT) · the Z clock · the incumbent version TWICE (H8-a's f25291b build, or …gef02d13) · active · formed count 0 · one network_resumed line with channel=20 panId=0x774c · a row count ⏺ = ROWS-A · homesynapse.yaml + integrations/zigbee.yaml listed · window-key count 0. ⏺ all. A changed PAN, a formed ≠ 0, or a window-key count ≠ 0 → STOP, paste.
```
**STOP-GATE R4c-0:** hs-fresh · the IP pinned · formed 0 · resumed on PAN 0x774c · ROWS-A read · no window key.

## B1 — Install + boot (the hash hop-to-hop; the integrity gate; the upgrade; the boot tokens as counts)
```bash
# WHERE: Git Bash on the desktop → the HELD card at <IP> (three times in this line). Move the old .deb aside on the card, copy the new one, verify the hash.
ssh -i ~/.ssh/id_ed25519_pi nick@<IP> 'mkdir -p ~/r3-history && mv ~/homesynapse_*_arm64.deb ~/r3-history/ 2>/dev/null; ls ~/homesynapse_*_arm64.deb 2>/dev/null | wc -l' && cd ~/r4c-artifact && scp -i ~/.ssh/id_ed25519_pi $(find . -name '*_arm64.deb') nick@<IP>: && ssh -i ~/.ssh/id_ed25519_pi nick@<IP> 'sha256sum ~/homesynapse_*_arm64.deb; dpkg-deb --field ~/homesynapse_*_arm64.deb Version Architecture'
# EXPECTED: 0 (no .deb left before the copy) · the SAME hash as §1 · Version = the g1e26912 build · arm64. ⏺ all.
```
```bash
# WHERE: the HELD card (ssh -i ~/.ssh/id_ed25519_pi nick@<IP>, then paste). THE INTEGRITY GATE — its own block, before the act.
sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;' && sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'PRAGMA integrity_check;'
# EXPECTED: ROWS-pre ⏺ (= ROWS-A) · ok. Anything but ok → STOP, paste.
```
```bash
# WHERE: the HELD card. THE INSTALL (an ordinary UPGRADE — no flag; apt asking to DOWNGRADE = STOP). The block stamps before and after.
date -u +%H:%M:%SZ; sudo apt install -y ~/homesynapse_*_arm64.deb 2>&1 | tail -8; date -u +%H:%M:%SZ; dpkg-query -W -f '${Version}\n' homesynapse; cat /opt/homesynapse/VERSION; sleep 25; systemctl is-active homesynapse.service; sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'; sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'PRAGMA integrity_check;'
# EXPECTED: an UPGRADE tail (no "downgrad") · the new Version TWICE (g1e26912) · active · ROWS ≥ pre · ok. ⏺ all.
```
```bash
# WHERE: the HELD card. THE BOOT TOKENS, invocation-scoped, as COUNTS.
INV=$(systemctl show -p InvocationID --value homesynapse.service); echo "INV=$INV"; J="sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager"; for t in "Configuration issue" "lifecycle.integration_schema_registered" "zigbee.network_resumed" "zigbee.network_formed" "zigbee.adopt_list_loaded" "zigbee.adoption_maps_rehydrated" "zigbee.availability_seeded" "bus.delivery_anomaly" "permit_join_opened"; do printf '%-42s %s\n' "$t" "$($J | grep -c "$t")"; done; $J | grep -E "zigbee\.(adopt_list_loaded|adoption_maps_rehydrated|availability_seeded|network_resumed)" | sed 's/^.*INFO *//' | head -4
# EXPECTED: Configuration issue 0 · schema_registered 1 · network_resumed 1 (channel=20 panId=0x774c) · network_formed 0 · adopt_list_loaded 1 · adoption_maps_rehydrated 1 (its devices= number ⏺ = the devices the store already knows) · availability_seeded 1 · bus.delivery_anomaly 0 · permit_join_opened 0. ⏺ all nine counts and the four lines.
```
**STOP-GATE R4c-2:** version exact in both places · active · zero row loss · integrity ok · formed 0 · anomaly 0 at boot.

## B2 — Two reads on the new bytes: `lastReported` (LASTREPORTED-1b) and the card's gradle (`card-gradle:`)
```bash
# WHERE: the HELD card. The entities read, saved to a file; the token never printed. python3 renders one line per entity.
mkdir -p ~/r4c; TOK=$(sudo cat /var/lib/homesynapse/config/initial_api_token | tr -d '\r\n'); echo "token_len=${#TOK}"; [ "${#TOK}" -ge 40 ] && echo TOKLEN-OK; curl -s -o ~/r4c/entities-1.json -w "entities http=%{http_code} bytes=%{size_download}\n" -H "Authorization: Bearer $TOK" http://127.0.0.1:7070/api/v1/entities; python3 - <<'PY'
import json; d=json.load(open('/home/nick/r4c/entities-1.json')); rows=d['data'] if isinstance(d,dict) and 'data' in d else d
print('rows=%d  lastReported key on every row: %s  null: %d  instant: %d' % (len(rows), all('lastReported' in r for r in rows), sum(r.get('lastReported') is None for r in rows), sum(r.get('lastReported') is not None for r in rows)))
for r in rows: print('   %s %s stale=%s deviceId=%s lastReported=%s' % (r.get('entityId'), r.get('availability'), r.get('stale'), r.get('deviceId'), r.get('lastReported')))
PY
# EXPECTED: TOKLEN-OK · http=200 · the key on every row · at least one row with lastReported=None that has NEVER reported (the Hue's entity from R-4, absent from the air) and none showing an instant near this boot's clock without a report behind it · the S31's row an ISO-8601 Z instant. ⏺ the summary line and every row. (This is LASTREPORTED-1b's read: null at adoption is honest; an instant only after a report. A never-reported entity showing THIS boot's time = a FINDING, paste.)
```
```bash
# WHERE: the HELD card. The gradle answer, one line, bounded (a Pi has no toolchain unless one was put there).
which gradle java 2>/dev/null; for d in ~/homesynapse-core /opt/homesynapse; do if [ -x "$d/gradlew" ]; then (cd "$d" && timeout 180 ./gradlew --version 2>/dev/null | grep -m1 -i gradle) && exit 0; fi; done; echo "card-gradle: absent"
# EXPECTED: either a "Gradle N.N" line (⏺ `card-gradle: <that line>`) or `card-gradle: absent` (⏺ it). Either answer is the answer; TR-1b's driver shape follows it.
```

## B3 — THE WINDOW: the ZDO surface on silicon (C-003), the sleepy devices provoked, the census
**What this measures.** With the door closed, an unknown sender is noted once and ignored (`rejoin_ignored_window_closed`). Opening the window clears that note and the once-per-nwk lookup set; the next frame from an unknown sender runs the coordinator lookup (`0x0061`): a table HIT adopts as R-4b did; a MISS (`lookup_eui64_failed … status=0x1`, the sleepy class) now sends `IEEE_addr_req` (`0x0001`) on the air and, on `ieee_addr_rsp`, admits the device on the response pair → `rejoin_candidate` → `device_adopted … source=rejoin`. No answer in 10 s → `ieee_addr_req_unanswered` / `rejoin_candidate_unresolved … reason=zdo_miss` (a finding, not a stop).
```bash
# WHERE: the HELD card. Step 0a — the config write, guarded (D-7): the key lands at line 2; the read-back is the guard against a double paste.
sudo cp /var/lib/homesynapse/config/integrations/zigbee.yaml /root/r4c-history-zigbee.yaml.pre-window 2>/dev/null || sudo sh -c 'mkdir -p /root/r4c-history && cp /var/lib/homesynapse/config/integrations/zigbee.yaml /root/r4c-history/zigbee.yaml.pre-window'; sudo grep -qE '^[[:space:]]*permit_join_duration:' /var/lib/homesynapse/config/integrations/zigbee.yaml && echo "GUARD: already present — NOT adding" || sudo sed -i '1a permit_join_duration: 254' /var/lib/homesynapse/config/integrations/zigbee.yaml; sudo cat -n /var/lib/homesynapse/config/integrations/zigbee.yaml | head -12; sudo grep -cE '^[[:space:]]*permit_join_duration:' /var/lib/homesynapse/config/integrations/zigbee.yaml
# EXPECTED: line 1 serial_port · line 2 permit_join_duration: 254 · channel: 20 on line 3 · the six adopt IEEEs · the count 1. ⏺ the head and the count. A count of 2 → STOP, paste (a duplicate key; the navigator hands the one-line fix).
```
```bash
# WHERE: the HELD card. Step 0b — ARM: restart; the window opens at boot; the countdown is the block's, not yours. Have the three Sonoffs within reach BEFORE you paste: the SNZB-02P (temp/humidity), the SNZB-01P (button), the SNZB-04P (contact + magnet).
sudo systemctl restart homesynapse.service; sleep 25; INV=$(systemctl show -p InvocationID --value homesynapse.service); echo "INV=$INV"; sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -E "permit_join_opened|network_formed|network_resumed" | sed 's/^.*INFO *//'; T0=$(date -u +%s); echo "WINDOW OPEN at $(date -u +%H:%M:%SZ) — 254 s. PROVOKE NOW, in this order, ~40 s apart: (1) hold the SNZB-02P in a closed warm hand (a temperature change makes it report; never press its button longer than a tap) · (2) SHORT-press the SNZB-01P once · (3) separate the SNZB-04P from its magnet, wait 5 s, rejoin them · (4) wave at the SNZB-03P · (5) press the S31's button once ON and once OFF."; for i in $(seq 1 24); do sleep 10; printf '%3ds  lookups=%s  zdo_req=%s  zdo_rsp=%s  adopted=%s  unresolved=%s  ignored_closed=%s\n' $(( $(date -u +%s) - T0 )) "$(sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -c 'lookup_eui64')" "$(sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -c 'zigbee.ieee_addr_req')" "$(sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -c 'zigbee.ieee_addr_rsp')" "$(sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -c 'device_adopted')" "$(sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -c 'rejoin_candidate_unresolved')" "$(sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -c 'rejoin_ignored_window_closed')"; done; echo "WINDOW CLOSED at $(date -u +%H:%M:%SZ)"
# EXPECTED: permit_join_opened: duration=254s ×1 · network_resumed ×1, formed 0 · then 24 count lines over 240 s. The exit: zdo_req ≥1 · zdo_rsp ≥1 · adopted ≥1 within the window. ⏺ the opened line and the LAST count line whole (the intermediate lines may be summarised as "monotone").
```
```bash
# WHERE: the HELD card, after the countdown. THE HARVEST — the chain, verbatim, invocation-scoped; then the census of the six adopt IEEEs against the adopted set.
INV=$(systemctl show -p InvocationID --value homesynapse.service); sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -E "zigbee\.(lookup_eui64|ieee_addr_req|ieee_addr_rsp|rejoin_candidate|rejoin_ignored|device_proposed|device_adopted|proposal_incomplete)" | sed 's/^.*\(INFO\|WARN\|DEBUG\) *//' | head -40; echo "--- census"; for d in 0x00178801101A09BB 0xF044D3FFFE9C78D7 0x00124B002FA8D1C5 0xF044D3FFFED2A201 0xF044D3FFFE1C1E8E 0x449FDAFFFE688F57; do printf '%s  adopted_this_invocation=%s  in_adopt_list=%s\n' "$d" "$(sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -c "device_adopted: device=$d")" "$(sudo grep -ci "$d" /var/lib/homesynapse/config/integrations/zigbee.yaml)"; done
# EXPECTED (C-003): ONE chain for the SNZB-02P: lookup_eui64_failed status=0x1 → ieee_addr_req nwk=0x… → ieee_addr_rsp nwk=0x… device=0xF044D3FFFED2A201 → rejoin_candidate … source=… → device_adopted: device=0xF044D3FFFED2A201 … source=rejoin. The SNZB-01P and SNZB-04P: the same shape if they were unknown senders, or nothing (already known from the store: adoption_maps_rehydrated) — either is recorded. The Hue: expected absent (F-R4b-G). The census line for 0xF044D3FFFED2A201 reads adopted_this_invocation=1. ⏺ the chain whole and the six census lines. The six IEEEs are the R-4b record's `zigbee.yaml as found` (§3, lines 4–9); if any census line prints in_adopt_list=0, the navigator reads the IEEE from the yaml (T1) and re-runs the census — the file, not this packet, is the truth.
```
**STOP-GATE R4c-3 (the exit):** `ieee_addr_rsp … device=0xF044D3FFFED2A201` ×1 and `device_adopted: device=0xF044D3FFFED2A201` ×1 in this invocation. A MISS (`ieee_addr_req_unanswered` or `reason=zdo_miss`) is NOT a stop: ⏺ it whole with the nwk, re-provoke the SNZB-02P once more inside the same window if seconds remain, and record the outcome; the hub rules on the evidence. `network_formed` at any point = POWER OFF + STOP.

## B4 — The reads after the window: `lastReported` again, the anomaly count, the disarm
```bash
# WHERE: the HELD card. The second entities read (the devices that reported in the window now carry instants; a row that was null and did not report stays null).
TOK=$(sudo cat /var/lib/homesynapse/config/initial_api_token | tr -d '\r\n'); [ "${#TOK}" -ge 40 ] && echo TOKLEN-OK; curl -s -o ~/r4c/entities-2.json -w "entities http=%{http_code} bytes=%{size_download}\n" -H "Authorization: Bearer $TOK" http://127.0.0.1:7070/api/v1/entities; python3 - <<'PY'
import json
def load(p):
    d=json.load(open(p)); return d['data'] if isinstance(d,dict) and 'data' in d else d
a={r['entityId']:r for r in load('/home/nick/r4c/entities-1.json')}; b={r['entityId']:r for r in load('/home/nick/r4c/entities-2.json')}
print('rows before=%d after=%d new=%d' % (len(a), len(b), len(set(b)-set(a))))
for k,r in b.items(): print('   %s %s deviceId=%s lastReported %s -> %s' % (k, r.get('availability'), r.get('deviceId'), (a.get(k) or {}).get('lastReported'), r.get('lastReported')))
PY
# EXPECTED: new ≥1 (the SNZB-02P's entity or entities, registered this window) · every entity that reported in the window moved null→instant or instant→later instant · nothing moved instant→null. ⏺ the summary and the rows.
```
```bash
# WHERE: the HELD card. The anomaly count for the whole invocation, and the row growth.
INV=$(systemctl show -p InvocationID --value homesynapse.service); sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -c "bus.delivery_anomaly"; sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep "bus.delivery_anomaly" | sed 's/^.*WARN *//' | head -5; sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'; date -u +%H:%M:%SZ
# EXPECTED: 0 (FIX-1a's detector saw nothing on the wire during the window; any non-zero line is ⏺'d whole — it is FIX-2 evidence, not a stop) · ROWS-W1 > ROWS-A. ⏺ all.
```
```bash
# WHERE: the HELD card. DISARM — the key out, restart, prove the door is closed. This runs before B5 no matter what B3 produced.
sudo sed -i '/^[[:space:]]*permit_join_duration:/d' /var/lib/homesynapse/config/integrations/zigbee.yaml && sudo grep -cE '^[[:space:]]*permit_join_duration:' /var/lib/homesynapse/config/integrations/zigbee.yaml; sudo systemctl restart homesynapse.service && sleep 25 && INV=$(systemctl show -p InvocationID --value homesynapse.service) && sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -cE "permit_join_opened|Configuration issue|network_formed"; systemctl is-active homesynapse.service; sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -c "zigbee.network_resumed"
# EXPECTED: 0 (key gone) · 0 (no window, no config issue, no formed) · active · 1 (resumed). ⏺ all. A non-zero on the second count → paste; the navigator reads which token it was.
```

## B5 — The restore (the bench night) — outranks everything after B3
```bash
# WHERE: the HELD card. The clean stop, graded (with this artifact the stop reads Result=success · inactive · 143, the H8-a proof; ⏺ whatever it reads). Then power OFF → held card OUT (re-label: hs-fresh — R-4c DONE — g1e26912) → bench card IN → power ON → ~90 s.
sudo systemctl stop homesynapse.service; sleep 2; systemctl show -p Result -p ActiveState -p ExecMainStatus homesynapse.service; sudo shutdown -h now
```
```bash
# WHERE: the BENCH card (ssh pi). Start the floor, then the boot-health scenario.
~/bench.sh status; ~/bench.sh start; sleep 45; ~/bench.sh status; ~/bench.sh scenario boot-health; grep -E "zigbee\.(port_identity_captured|network_resumed)" ~/hs-bench/current.log | tail -2
# EXPECTED: NOT running → start → running → [PASS] boot-health — 6/6 positive · 0 forbidden → network_resumed: channel=20 panId=0x774c. ⏺ all. A changed PAN = STOP, paste.
```
**STOP-GATE R4c-4:** the floor is back to [PASS]; the PAN unchanged.

## §N The navigator (a FRESH Cowork window with `ClaudeFolder` connected; paste when you sit down at the desktop; keep it open beside the terminal)
```
date -u first. You are the R-4c NAVIGATOR for NexSys/HomeSynapse — the senior engineer sitting next to Nick for ONE hardware session (≤90 min at the rig). Read nexsys-hivemind/context/instructions/2026-09-11_R-4c_measurement-only_zdo-surface-C-003_navigator-packet.md WHOLE, then nexsys-hivemind/context/audits/2026-09-12_R-4c_measurement-only_operator-record.md (the scaffold you fill), then nexsys-hivemind/context/audits/2026-09-04_R-4b_re-rep_operator-record.md §0 and §9 only (what the last full session on this rig proved, and its findings card — the packet was cut from it). The walk: feed the packet's blocks ONE AT A TIME (§0 → §1 → B0 → B1 → B2 → B3 → B4 → B5), each pasted VERBATIM as one fenced block with its WHERE line (replace every <IP> with B0's pinned address before you hand a block); say in one line what the block is FOR; wait for the paste-back — never proceed on silence or a summary; compare it to the EXPECTED line; MATCH → append the ⏺ verbatim under the record's matching section with a `date -u` stamp via device_bash (append-only; assert the heading exists first; never rewrite an earlier ⏺) and hand the next block; MISMATCH → your license is three tiers: T1 fix an INSTRUMENT defect yourself (a path, a glob, a shifted count, an IEEE read from the yaml — never what a block measures or asserts) and file it in the record's §9 the same minute; T2 order ≤3 READ-ONLY probes (journalctl scoped by invocation, systemctl show, sqlite3 ?mode=ro, curl GET on the loopback, ls/cat of config) and file the reads; T3 STOP for anything that would change the rig beyond the packet's own blocks — network_formed ANYWHERE (= POWER OFF + STOP), an integrity check not ok, apt asking to downgrade, a second window, any http≠200 you cannot characterise in three probes, a design question — and say "STOP at <block> — return to the hub session and paste the record's <block>". Hard fences: delete nothing (move aside) · no --allow-downgrades · ONE window, disarmed at B4 before B5 whatever B3 produced · no long-press on any Sonoff · the token VALUE never enters the record (token_len=NN + TOKLEN-OK is the ⏺; a raw token pasted is filed as [token redacted]) · the bench card's s31/nightly untouched · no Core write, no config change beyond the window key · no public sentence about any claim · B5 outranks everything after B3 — the bench floor is back to [PASS] today. Close-out (exactly once, after B5 or a STOP): date -u; rewrite the record's §0 into a one-screen verdict surface (per-block MET/MISS/DEVIATION · C-003 ✓/✗ with the chain quoted · LASTREPORTED-1b's two reads in one table · the card-gradle line · the anomaly count · the census of six · the Hue's absence recorded, not judged); list the three things you would change in the packet; set the frontmatter status to CLOSED-PENDING-HUB-AUDIT (or STOPPED-AT-<block>); keep the record ≤ ~30 KB (the ⏺s are counts and short chains today); commit NOTHING. Your last message to Nick: "Record filed — paste to the hub: `R4C: RETURNED <path> <bytes>`". You report to the hub through that line, not to me.
```

## §H What the hub banks at intake
The record (every ⏺, in order) → the two-layer audit (the hub re-runs the census and the chain greps against Nick's filed paste-backs; re-derives the artifact's identity from the Actions line and the hash) → **C-003 minted or refused on the chain** (the ZDO surface on silicon: `ieee_addr_rsp` for `0xF044D3FFFED2A201` and its `device_adopted … source=rejoin`; the fence on B-2/B-3 design lifts on the mint) → **LASTREPORTED-1b banked** (null at adoption, an instant only after a report — the two tables) → **`card-gradle:`** into TR-1b's charter → **the anomaly count** into OR-BUS-SILENT-DROP's row (a zero on the wire is a bound on the class, not its closure) → the census of six into the fleet sentence → the findings card's rows into the docket → **F-R4-1b → LIVE-VERIFIED** on the mint.
