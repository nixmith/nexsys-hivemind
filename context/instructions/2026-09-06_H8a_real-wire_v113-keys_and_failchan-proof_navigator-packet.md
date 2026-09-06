<!--
file: context/instructions/2026-09-06_H8a_real-wire_v113-keys_and_failchan-proof_navigator-packet.md
purpose: THE H8-a NAVIGATOR PACKET — the v1.1.3 read-API keys read on the REAL WIRE of the held card (hs-fresh) running the CI-built artifact that carries CG-123 (f25291b's Java = 093d5b4's Java), the FAILCHAN §6-B/EXITCODE stop-proof on hardware, the v1.1.3 wire CAPTURE that becomes FE-113b's fixture, plus two read-only bonus reads (OR-JOURNALD-PRIO's priority count; docket Row 16's sys_* count). Authored by the v66 hub at Block 1 (Sun 2026-09-06 ~10:5x CT; instrument 2026-09-06T15:5xZ) on the R-4b packet + record + audit (every R-4b deviation D-1…D-13 folded in as the packet's own text), the CG-123 audit §3/§6, and the read-API source at 093d5b4 (the wire keys verified at ListEntitiesEndpoint.java:191–204 · ListAutomationsEndpoint.java:112–125 · GetNonFiringEndpoint.java:118–129 · EndpointResponses.subjectRefMap; the ref rule at StandardExplanationService.java:493–546). Playbook §8 contract: every block self-contained; the WHERE label is the block's first EXECUTABLE line (hostname); one act per line; the EXPECTED line and the STOP condition on every block; counts never heads; a gate never shares a block with its act; ⏺ = paste either way.
audience: Nick (the operator) · the H8-a navigator (a fresh Cowork window; §N is its dispatch line) · the hub (audits the record at intake)
state-type: operator packet (navigator pattern)
status: LIVE — TODAY (Sun 09-06, the rig ~15:00 CT; fallback Tue evening). Do not start before §0's guard is answered at the desktop. The record you build as you go: paste each ⏺ into the NAVIGATOR window; it files them into context/audits/2026-09-06_H8a_real-wire_operator-record.md (scaffolded). The hub asks nothing while you are at the rig.
-->

# H8-a — the four keys on the real wire, the clean-stop proof, the capture (held card, Sunday 09-06)

**GOAL.** On the held card, running the CI-built artifact of `f25291b` (CG-123's Java bytes — identical Java to `093d5b4`; the lock-only bump touched no Java and, by `install-smoke.yml`'s path filter, built no artifact): **(K) the four v1.1.3 keys are on the wire** — `deviceId` + `lastReported` on every `/api/v1/entities` row · `components[].ref` on every `/api/v1/automations` component · `triggerRef` on `/api/v1/automations/{id}/non-firing` — with the literal `"type":"entity"` where non-null and ISO-8601 where non-null; **(S) a clean operator stop GRADES clean** — `Result=success · ExecMainStatus=143 · ActiveState=inactive` (FAILCHAN §6-B; R-4b §9 read `exit-code · failed` on `ef02d13`, BEFORE the fix); **(C) the three bodies are CAPTURED to disk** — FE-113b's fixture is a measurement, never a mock; **(J)** the journald priority count; **(R)** the `sys_*` count. **DONE-WHEN:** every ⏺ in B0–B6 banked; the bench card back and its floor `[PASS]` (B6). **Registers this packet moves at intake:** FE-113 → VERIFIED (law #22) on (K) · OR-FAILCHAN → CLOSES on (S) · FE-113b's capture EXISTS on (C).

**TIME AT THE RIG: ≤60 min** (B0 8 · B1 10 · B2 10 · B3 5 · B4 2 · B5 1 · B6 12 ≈ 48). §0 + §1 are DESKTOP work — do them before you walk to the rig.

**ANTI-ACTIONS (the whole session).** Never re-run `main` CI · never `--allow-downgrades` · never delete a file on either card (move aside) · never touch the bench card's s31/nightly (the bench goes OUT and comes BACK; nothing on it is edited) · never paste a token value (`token_len=NN` is the ⏺; `TOKLEN-OK`) · **`network_formed` ANYWHERE = POWER OFF + STOP** · no permit-join window today (`permit_join_duration` stays ABSENT — this session adopts nothing) · one physical act per line, note the clock on each.

## §0 GUARD 1 — which artifact (DESKTOP; the browser; answer before §1)
The `.deb` is built ONLY by the `install-smoke` workflow (`.github/workflows/install-smoke.yml:155–160` uploads `distribution-artifacts-<arch>`; `ci.yml` uploads test reports only). `install-smoke` runs on `main` pushes that touch `distribution/** app/** lifecycle/** api/** gradle/** build-logic/**` — CG-123 (`f25291b`) touched `api/**` + `lifecycle/**` → it RAN; the lock bump (`093d5b4`) touched only `web-ui/dashboard/package-lock.json` → it did NOT. **Therefore the artifact of record is `f25291b`'s install-smoke run**, and its Java is byte-for-byte `093d5b4`'s.
Open GitHub → Actions → the **install-smoke** workflow → the run whose commit is `f25291b` ("feat(read-api): CG-1/2/3 …"). **EXPECTED:** both jobs (amd64 · arm64) GREEN. ⏺ one line: `ARTIFACT: f25291b — run <URL> — amd64 <green|red> arm64 <green|red>`. **STOP:** any red or pending on that run → paste the failing step's last 20 lines to the navigator; the session does not proceed to §1 (a red install-smoke on the artifact you are about to install is the one thing a desk cannot argue with). Also EXPECTED on the same page: the newest `CI` (Build & Check) run on `main` is `093d5b4`'s and GREEN — ⏺ `CI-main: 093d5b4 <green|red>` (a read, not a gate for this packet).

## §1 Fetch + hash (DESKTOP; browser + Git Bash)
Open the chosen run → the **arm64** job → the step "Version-grammar echo (hs_version is tag-shaped; the .deb carries it)" → ⏺ the whole `version-grammar echo green: … sha256 <64 hex>  homesynapse_0.1.0+git<…>_arm64.deb` line (the ORIGIN hash). Then the run's Summary → Artifacts → `distribution-artifacts-arm64` → it lands in `~/Downloads` (if a `(1)` suffix appears, an older zip of the same name is there — the hash gate below is the backstop; use the newest).
```bash
# WHERE: Git Bash on the desktop (the first line prints the host so the ⏺ is self-locating). The zip NESTS at deb/build/. Old .debs move aside — delete nothing.
hostname; date -u +%H:%M:%SZ; mkdir -p ~/h8a-artifact ~/r3-history && mv ~/h8a-artifact/*.deb ~/r3-history/ 2>/dev/null; cd ~/h8a-artifact && powershell.exe -NoProfile -Command "Expand-Archive -LiteralPath \"$(cygpath -w ~/Downloads/distribution-artifacts-arm64.zip)\" -DestinationPath \"$(cygpath -w ~/h8a-artifact)\" -Force" && find . -name '*_arm64.deb' | wc -l && find . -name '*_arm64.deb' -exec sha256sum {} \;
# EXPECTED: the count line reads 1 · the hash EQUALS the echo line's sha256 · the name reads homesynapse_0.1.0+git20260906.114248.gf25291b_arm64.deb (f25291b's committer date 2026-09-06T11:42:48Z — the grammar is the committer date UTC + g<sha>). ⏺ all. STOP: two .debs, a hash mismatch, or a name without gf25291b → paste; do not walk to the rig.
```
**STOP-GATE H8a-1:** one .deb · hash = the run log · `gf25291b` in the name.

## B0 — Preflight at the rig (the bench card OUT, the held card IN; the boot glance)
```bash
# WHERE: Git Bash → the BENCH card (its alias `pi`; the first line prints its hostname). Read-only: the overnight digest — the bench never goes down un-read. ⏺ the whole output (it banks your owed `nightly 09-05` / `nightly 09-06` lines).
ssh pi 'hostname; date -u +%H:%M:%SZ; tail -3 ~/hs-bench/digests/nightly.log; ls -t ~/hs-bench/bundles | head -3'
# EXPECTED: hostname hs-dev-1 · the last nightly digest lines (09-05 and/or 09-06) · the newest bundle names. STOP: nothing — this is a read; a missing digest is a ⏺, not a stop.
```
```bash
# WHERE: the BENCH card. The orderly halt. Then: power OFF at the wall → bench card OUT → held card IN (the one labelled hs-fresh — R-4b DONE — ef02d13) → power ON → wait ~90 s. Note the clock on the physical acts. The coordinator dongle STAYS in its port.
ssh pi 'hostname; sudo shutdown -h now'
# EXPECTED: hs-dev-1, then the connection drops (the halt). STOP: the hostname is not hs-dev-1 → do not halt; paste.
```
```bash
# WHERE: Git Bash → the HELD card, by NAME once (the first line MUST print hs-fresh — the O-2 lesson), and it prints the address you will PIN for every hop after this (R-4b D-4: mDNS failed mid-chain; 192.168.1.80 was the measured address).
ssh -i ~/.ssh/id_ed25519_pi -o StrictHostKeyChecking=accept-new nick@hs-fresh.local 'hostname; hostname -I; date -u +%H:%M:%SZ; date "+%Z %z"; command -v python3 curl | wc -l; dpkg-query -W homesynapse; cat /opt/homesynapse/VERSION; systemctl is-active homesynapse.service; INV=$(systemctl show -p InvocationID --value homesynapse.service); echo "INV=$INV"; sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -c "zigbee.network_formed"; sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -c "zigbee.network_resumed"; sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -E "zigbee.network_resumed" | tail -1 | cut -c1-160; sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" "SELECT COUNT(*) FROM events;"; sudo grep -c permit_join_duration /var/lib/homesynapse/config/integrations/zigbee.yaml'
# EXPECTED: hs-fresh · an IPv4 (PIN IT — the FIRST address printed; every block below says <IP>: replace with this value) · the Z clock · the card's TZ · 2 (python3 and curl both present; a 1 = python3 absent → the navigator applies B2's grep fallback, T1) · homesynapse 0.1.0+git20260903.124041.gef02d13 (R-4b's artifact, the incumbent) twice · active · INV=<hex> · network_formed COUNT 0 · network_resumed COUNT 1 · the resumed line reads channel=20 panId=0x774c · a row count ⏺ = ROWS-A (R-4b closed at 212+) · permit_join_duration COUNT 0 (no window today). If hs-fresh.local does not RESOLVE at all (D-4's class), re-run this block with nick@192.168.1.80 (R-4b's measured address) — the hostname line still guards. STOP: hostname ≠ hs-fresh · network_formed ≠ 0 (= POWER OFF + STOP) · a changed PAN · permit_join_duration ≠ 0 (paste; the navigator rules).
```
**STOP-GATE H8a-0:** hs-fresh · the IP pinned · formed 0 · resumed 1 on PAN 0x774c · ROWS-A read · no window.

## B1 — Install + boot (self-timing; the boot tokens; the unit directives)
```bash
# WHERE: Git Bash on the desktop → the HELD card at <IP>. Move the old .deb aside on the card, copy the new one, verify the hash hop-to-hop. (Replace EVERY <IP> — three in this line — with B0's pinned address.)
ssh -i ~/.ssh/id_ed25519_pi -o StrictHostKeyChecking=accept-new nick@<IP> 'hostname; mkdir -p ~/r3-history && mv ~/homesynapse_*_arm64.deb ~/r3-history/ 2>/dev/null; ls ~/homesynapse_*_arm64.deb 2>/dev/null | wc -l' && cd ~/h8a-artifact && scp -i ~/.ssh/id_ed25519_pi $(find . -name '*_arm64.deb') nick@<IP>: && ssh -i ~/.ssh/id_ed25519_pi nick@<IP> 'hostname; ls ~/homesynapse_*_arm64.deb | wc -l; sha256sum ~/homesynapse_*_arm64.deb; dpkg-deb --field ~/homesynapse_*_arm64.deb Version Architecture'
# EXPECTED: hs-fresh · 0 (nothing left before the copy) · hs-fresh · 1 · the SAME hash as §1 · Version: 0.1.0+git20260906.114248.gf25291b · Architecture: arm64. ⏺ all. STOP: a hash mismatch or a count ≠ 1 → paste (a partial copy is exactly the failure D-4 removed; do not install).
```
```bash
# WHERE: the HELD card (ssh -i ~/.ssh/id_ed25519_pi nick@<IP>, then paste). THE INTEGRITY GATE — its own block, before the act (a bad store stops the install).
hostname; date -u +%H:%M:%SZ; sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;' && sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'PRAGMA integrity_check;' && sudo cat -n /var/lib/homesynapse/config/homesynapse.yaml | wc -l && sudo ls -l /var/lib/homesynapse/config/homesynapse.yaml /var/lib/homesynapse/config/initial_api_token
# EXPECTED: ROWS-pre ⏺ (≥ ROWS-A) · ok · 17 (bench-hero as R-4b re-bound it: 1 state_change trigger + 1 delay + 1 command, both refs on the S31 entity 01M1PRQN03X8H4MNEZQ62F76F1) · the two files listed (426 b homesynapse.yaml; the token file present). STOP: anything but ok → paste; no install.
```
```bash
# WHERE: the HELD card. THE INSTALL (an ordinary UPGRADE — no flag; apt asking to DOWNGRADE = STOP). Self-timing: the block stamps before and after; the unit's ExecStartPost health probe holds the start until /health answers.
hostname; date -u +%H:%M:%SZ; sudo apt install -y ~/homesynapse_*_arm64.deb 2>&1 | tail -8; date -u +%H:%M:%SZ; dpkg-query -W homesynapse; cat /opt/homesynapse/VERSION; sleep 25; date -u +%H:%M:%SZ; systemctl is-active homesynapse.service; systemctl show -p ActiveState -p SubState -p ExecMainStatus -p SuccessExitStatus -p Restart homesynapse.service
# EXPECTED: an UPGRADE tail (no "downgrad") · homesynapse 0.1.0+git20260906.114248.gf25291b · the same string from /opt/homesynapse/VERSION · active · ActiveState=active SubState=running ExecMainStatus=0 · SuccessExitStatus=143 · Restart=always (the FAILCHAN unit directives, carried by this .deb — homesynapse.service:60/:70). ⏺ all with the three stamps. STOP: "downgrad" anywhere · not active after the sleep → `sudo systemctl status homesynapse.service --no-pager -l` ⏺, STOP.
```
```bash
# WHERE: the HELD card. THE BOOT TOKENS, invocation-scoped, as COUNTS (D-6: an assertion of absence or uniqueness is a count, never a head).
hostname; INV=$(systemctl show -p InvocationID --value homesynapse.service); echo "INV=$INV"; J="sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager"; echo "config_issue=$($J | grep -c 'Configuration issue')"; echo "schema_registered=$($J | grep -c 'lifecycle.integration_schema_registered')"; echo "network_formed=$($J | grep -c 'zigbee.network_formed')"; echo "network_resumed=$($J | grep -c 'zigbee.network_resumed')"; $J | grep -E "zigbee.network_resumed|lifecycle.integration_schema_registered" | cut -c1-160; sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'; sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'PRAGMA integrity_check;'
# EXPECTED: config_issue=0 (PKG-SEC-2 holds on the new artifact) · schema_registered=1 (stage=pre-load) · network_formed=0 · network_resumed=1 (channel=20 panId=0x774c) · ROWS ≥ ROWS-pre · ok. ⏺ all. STOP: network_formed ≠ 0 = POWER OFF + STOP · integrity not ok · config_issue > 0 (paste the lines; the navigator rules T2).
```
**STOP-GATE H8a-2:** version exact in both places · active · formed 0 · resumed 1 · zero row loss · integrity ok · `SuccessExitStatus=143` + `Restart=always` on the unit.

## B2 — THE FOUR KEYS on the wire (the capture; the asserts; the copy to the desktop)
```bash
# WHERE: the HELD card. The token is READ FROM ITS FILE and never echoed (R-4b D-9); only its length prints. The three GETs save their bodies to ~/h8a/ and print only the http code and the byte count. The automation id is resolved BY NAME from the saved list (the id is per-load — R-4b §7-ii).
hostname; date -u +%H:%M:%SZ; mkdir -p ~/h8a; TOK=$(sudo cat /var/lib/homesynapse/config/initial_api_token | tr -d '\r\n'); echo "token_len=${#TOK}"; [ "${#TOK}" -ge 40 ] && echo TOKLEN-OK; curl -s -o ~/h8a/entities.json -w "entities http=%{http_code} bytes=%{size_download}\n" -H "Authorization: Bearer $TOK" http://127.0.0.1:7070/api/v1/entities; curl -s -o ~/h8a/automations.json -w "automations http=%{http_code} bytes=%{size_download}\n" -H "Authorization: Bearer $TOK" http://127.0.0.1:7070/api/v1/automations; AID=$(python3 -c 'import json;print([a["automationId"] for a in json.load(open("/home/nick/h8a/automations.json"))["data"] if a["name"]=="bench-hero"][0])' 2>/dev/null || grep -o '"automationId":"[A-Z0-9]*"' ~/h8a/automations.json | head -1 | cut -d'"' -f4); echo "bench-hero id=$AID"; curl -s -o ~/h8a/nonfiring.json -w "nonfiring http=%{http_code} bytes=%{size_download}\n" -H "Authorization: Bearer $TOK" "http://127.0.0.1:7070/api/v1/automations/$AID/non-firing"; unset TOK; ls -l ~/h8a/
# EXPECTED: token_len=43 · TOKLEN-OK · three http=200 lines with non-zero bytes · bench-hero id=01M… · three files listed. ⏺ all (the token value never appears — if it does anywhere, do not paste that line). STOP: any http ≠ 200 → `curl -s -w "\nhttp=%{http_code}\n" http://127.0.0.1:7070/health` ⏺ (no token needed), then paste; the navigator rules T2 (≤3 read-only probes).
```
```bash
# WHERE: the HELD card. THE ASSERTS — read-only, on the SAVED bodies (python3 is on Raspberry Pi OS; the hub re-executes the same asserts on the filed copies at intake — the gate of record is the hub's audit, this line is your EXPECTED).
hostname; python3 - <<'PY'
import json, re
E=json.load(open('/home/nick/h8a/entities.json')); A=json.load(open('/home/nick/h8a/automations.json')); N=json.load(open('/home/nick/h8a/nonfiring.json'))
iso=re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{1,9})?Z$')
rows=E['data']; print('entities rows=%d viewPosition=%s' % (len(rows), E['meta'].get('viewPosition')))
print('K1 deviceId key on every row:', all('deviceId' in r for r in rows), '| non-null:', sum(r.get('deviceId') is not None for r in rows), '| every non-null is a 26-char ULID:', all(isinstance(r['deviceId'],str) and len(r['deviceId'])==26 for r in rows if r.get('deviceId') is not None))
print('K2 lastReported key on every row:', all('lastReported' in r for r in rows), '| non-null:', sum(r.get('lastReported') is not None for r in rows), '| every non-null is ISO-8601 Z:', all(isinstance(r['lastReported'],str) and bool(iso.match(r['lastReported'])) for r in rows if r.get('lastReported') is not None))
for r in rows: print('   ', r['entityId'], r['availability'], 'stale=%s' % r['stale'], 'deviceId=%s' % r.get('deviceId'), 'lastReported=%s' % r.get('lastReported'))
auts=A['data']; comps=[c for a in auts for c in a['components']]
print('automations=%d components=%d types=%s' % (len(auts), len(comps), [c.get('type') for c in comps]))
print('K3 ref key on every component:', all('ref' in c for c in comps), '| non-null:', sum(c.get('ref') is not None for c in comps), '| every non-null ref is exactly {type:"entity", id:<26>}:', all(set(c['ref'])=={'type','id'} and c['ref']['type']=='entity' and isinstance(c['ref']['id'],str) and len(c['ref']['id'])==26 for c in comps if c.get('ref') is not None))
d=N['data']; print('nonfiring: automation=%s verdict=%s enabled=%s' % (d.get('automationName'), d.get('verdict'), d.get('enabled')))
print('K4 triggerRef key present:', 'triggerRef' in d, '| value:', json.dumps(d.get('triggerRef')), '| matches the list\'s trigger ref:', d.get('triggerRef') == next((c['ref'] for c in comps if c.get('type','').endswith('Trigger')), 'NO-TRIGGER'))
print('R16 sys_* refs on the wire:', sum(1 for c in comps if c.get('ref') and str(c['ref'].get('id','')).startswith('sys_')))
PY
# EXPECTED (pre-registered from source + the R-4b record): entities rows=3 · K1 True | non-null 3 | True · K2 True | non-null ≥1 (the projection replays the log at boot, so historical instants are lawful values — the key reports the projection, not the live radio; the S31 reports every 5 min at :54 s) | True · automations=1 components=3 types=['StateChangeTrigger','DelayAction','CommandAction'] · K3 True | non-null 2 (the trigger and the command, both on 01M1PRQN03X8H4MNEZQ62F76F1; DelayAction → null by the ref rule) | True · nonfiring: automation=bench-hero verdict=<a verdict word> · K4 True | {"type": "entity", "id": "01M1PRQN03X8H4MNEZQ62F76F1"} | True · R16 0 (SunTrigger → null by the ref rule; no sys_* ref can appear on this wire). ⏺ the whole output. A False anywhere is a FINDING, not a stop — ⏺ it whole and continue (the packet's job is to MEASURE).
```
```bash
# WHERE: Git Bash on the desktop. THE CAPTURE COMES HOME — the three bodies into the hivemind tree (the hub stages them at intake; FE-113b's fixture is this measurement). Replace <IP>.
hostname; D=~/Desktop/Code/ClaudeFolder/nexsys-hivemind/context/audits/2026-09-06_H8a_v113-wire-capture; mkdir -p "$D" && scp -i ~/.ssh/id_ed25519_pi 'nick@<IP>:h8a/*.json' "$D"/ && ls -l "$D" && sha256sum "$D"/*.json && grep -c 'Bearer' "$D"/*.json
# EXPECTED: three files (entities.json · automations.json · nonfiring.json) with the same byte counts B2 printed · three hashes ⏺ · grep -c Bearer reads 0 on all three (no token in any body). STOP: a Bearer count ≠ 0 → do not commit anything; paste to the navigator (the hub redacts at intake).
```
**STOP-GATE H8a-3 (a measurement, not a bar):** three bodies on the desktop, hashed, token-free.

## B3 — THE §6-B / EXITCODE STOP-PROOF (the gate reads first; then the act; then the read)
```bash
# WHERE: the HELD card. THE ACT: one clean operator stop. Nothing else in this block.
hostname; date -u +%H:%M:%SZ; sudo systemctl stop homesynapse.service; sleep 3; date -u +%H:%M:%SZ
# EXPECTED: two stamps a few seconds apart (the SIGTERM hook's 30 s internal grace is the ceiling; TimeoutStopSec=90). ⏺ both stamps. STOP: the stop hangs past 90 s → paste `systemctl status homesynapse.service --no-pager -l`.
```
```bash
# WHERE: the HELD card. THE READ — the grade of the stop (the same four properties run-smoke.sh:195–201 asserts in CI; one instrument, two rigs).
hostname; systemctl show -p Result -p ExecMainStatus -p ActiveState -p SubState -p NRestarts homesynapse.service; sudo journalctl -u homesynapse.service -n 25 -o short-iso --no-pager | cut -c1-200
# EXPECTED: Result=success · ExecMainStatus=143 · ActiveState=inactive · SubState=dead · NRestarts=<n> (⏺ the number; 0 expected — a nonzero means Restart=always fired at some earlier start: a finding, not a stop) · the tail carries "Deactivated successfully" and ZERO "Failed with result" · ZERO "abandoned (ungraceful shutdown)" · a zigbee.transport_closed_orderly line (FAILCHAN §10-O's orderly path). ⏺ all. R-4b §9 on ef02d13 read Result=exit-code · ActiveState=failed here — that reading today is a FINDING (the .deb did not carry the unit, or the hook path regressed); ⏺ it whole, then continue to the start.
```
```bash
# WHERE: the HELD card. THE START, and the boot tokens again as counts.
hostname; date -u +%H:%M:%SZ; sudo systemctl start homesynapse.service; sleep 25; date -u +%H:%M:%SZ; systemctl is-active homesynapse.service; INV=$(systemctl show -p InvocationID --value homesynapse.service); echo "INV=$INV"; J="sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager"; echo "config_issue=$($J | grep -c 'Configuration issue')"; echo "network_formed=$($J | grep -c 'zigbee.network_formed')"; echo "network_resumed=$($J | grep -c 'zigbee.network_resumed')"; sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'
# EXPECTED: active · a NEW INV (differs from B1's) · config_issue=0 · network_formed=0 · network_resumed=1 · ROWS ≥ B1's. ⏺ all. STOP: network_formed ≠ 0 = POWER OFF + STOP.
```
**STOP-GATE H8a-4:** `Result=success · ExecMainStatus=143 · inactive` on the stop · a clean resume after.

## B4 — (bonus, read-only) OR-JOURNALD-PRIO: the priority count
```bash
# WHERE: the HELD card. Every application line lands at journald's default priority (the mechanism verified at source, v58 b6); this is its number on a card.
hostname; sudo journalctl -u homesynapse.service -n 200 -o json --no-pager | grep -o '"PRIORITY":"[0-9]"' | sort | uniq -c; echo "warning-or-worse in the last 200 = $(sudo journalctl -u homesynapse.service -n 200 -o json --no-pager | grep -c '"PRIORITY":"[0-4]"')"; echo "app WARN lines in the same 200 = $(sudo journalctl -u homesynapse.service -n 200 --no-pager | grep -c ' WARN ')"
# EXPECTED: (nearly) every line "PRIORITY":"6" · the warning-or-worse count small and systemd's own (the stop/start lines) · the app-WARN count is the datum (its token may differ from ' WARN ' — if it reads 0 while the json count shows only 6s, ⏺ five app lines so the hub reads the level token) — the pair (app WARN lines vs journald ≤4) is Row 7's number. ⏺ all. STOP: none (a read).
```

## B5 — (read-only) docket Row 16: the `sys_*` count on the wire
```bash
# WHERE: the HELD card. The count the ruling asked for, from the SAVED automations body (already printed as R16 in B2; this is the one-line form for the record).
hostname; python3 -c 'import json;A=json.load(open("/home/nick/h8a/automations.json"));c=[x for a in A["data"] for x in a["components"]];print("components=%d refs_nonnull=%d sys_refs=%d" % (len(c), sum(1 for x in c if x.get("ref")), sum(1 for x in c if x.get("ref") and str(x["ref"].get("id","")).startswith("sys_"))))'
# EXPECTED: components=3 refs_nonnull=2 sys_refs=0. ⏺ the line. STOP: none (a read).
```

## B6 — The restore (the bench night) — outranks everything after B3
```bash
# WHERE: the HELD card. The clean stop (today it reads inactive/success — B3 proved it), then the halt. Then: power OFF → held card OUT (re-label: hs-fresh — H8-a DONE — f25291b) → bench card IN → power ON → ~90 s. Note the clock.
hostname; date -u +%H:%M:%SZ; sudo systemctl stop homesynapse.service; sleep 3; systemctl show -p Result -p ActiveState -p ExecMainStatus homesynapse.service; sudo shutdown -h now
# EXPECTED: Result=success · ActiveState=inactive · ExecMainStatus=143 (the second reading of the day — ⏺ it; two readings on one artifact is the proof's shape) · the halt drops the connection.
```
```bash
# WHERE: Git Bash → the BENCH card (`pi`). Start the floor yourself, then the boot-health scenario.
ssh pi 'hostname; date -u +%H:%M:%SZ; ~/bench.sh status; ~/bench.sh start; sleep 45; ~/bench.sh status; ~/bench.sh scenario boot-health; grep -E "zigbee\.(port_identity_captured|network_resumed)" ~/hs-bench/current.log | tail -2; grep -c "zigbee.network_formed" ~/hs-bench/current.log'
# EXPECTED: hs-dev-1 · NOT running → start → running → [PASS] boot-health — 6/6 positive · 0 forbidden → network_resumed: channel=20 panId=0x774c · network_formed COUNT 0. ⏺ all. STOP: a changed PAN or formed ≠ 0 → POWER OFF, paste.
```
**STOP-GATE H8a-5:** the bench card back, the floor `[PASS]`, the PAN unchanged. Then tell the navigator `B6 done` — it closes the record and gives you the one line for the hub.

## §N The navigator (a FRESH Cowork window with `ClaudeFolder` connected; paste ~14:50 CT; keep it open beside the terminal)
```
date -u first. You are the H8-a NAVIGATOR for NexSys/HomeSynapse — the senior engineer sitting next to Nick for ONE hardware session (≤60 min at the rig). Read nexsys-hivemind/context/instructions/2026-09-06_H8a_real-wire_v113-keys_and_failchan-proof_navigator-packet.md WHOLE, then nexsys-hivemind/context/audits/2026-09-06_H8a_real-wire_operator-record.md (the scaffold you fill), then nexsys-hivemind/context/audits/2026-09-04_R-4b_intake_two-layer-audit_v62-beat-7.md §0 only (what the last session on this rig proved). The walk: feed the packet's blocks ONE AT A TIME (§0 → §1 → B0 → B1 → B2 → B3 → B4 → B5 → B6), each pasted VERBATIM as one fenced block with its WHERE line; say in one line what the block is FOR; wait for the paste-back — never proceed on silence or a summary; compare it to the EXPECTED line; MATCH → append the ⏺ verbatim under the record's matching section with a `date -u` stamp via device_bash (append-only; assert the heading exists first; never rewrite an earlier ⏺) and hand the next block; MISMATCH → your license is the R-4b navigator's three tiers: T1 fix an INSTRUMENT defect yourself (a path, a glob, a shifted count — never what a block measures or asserts) and file it in the record's §9 the same minute; T2 order ≤3 READ-ONLY probes (journalctl scoped by invocation, systemctl show, sqlite3 ?mode=ro, curl GET on the loopback /health, ls/cat of config) and file the reads; T3 STOP for anything that would change the rig beyond the packet's own blocks — network_formed ANYWHERE (= POWER OFF + STOP), an integrity check not ok, apt asking to downgrade, any http≠200 you cannot characterize in three probes, a design question — and say "STOP at <block> — return to the hub session and paste the record's <block>". Hard fences: delete nothing (move aside) · no --allow-downgrades · no permit-join window today · the token VALUE never enters the record (token_len=NN + TOKLEN-OK is the ⏺; a raw token pasted is filed as [token redacted]) · the bench card's s31/nightly untouched · no public sentence about any claim · B6 outranks everything after B3 — the bench floor is back [PASS] tonight. Close-out (exactly once, after B6 or a STOP): date -u; rewrite the record's §0 into a one-screen verdict surface (per-block MET/MISS/DEVIATION · K1–K4 each ✓/✗ with the assert line quoted · the stop grade quoted · the capture's three hashes · the ⏺ census as a count · the deviations · asks of the hub); write §9 THE FINDINGS CARD (≤1.5 KB): what the wire showed that the desk did not predict, the stop-proof, the three things you would change in the packet; set the frontmatter status to CLOSED-PENDING-HUB-AUDIT (or STOPPED-AT-<block>); keep the record ≤ ~24 KB (the ⏺s are short today — no harvests); commit NOTHING. Your last message to Nick: "Record filed — paste to the hub: `H8-a: RETURNED <path> <bytes>`". You report to the hub through that line, not to me.
```

## §H What the hub banks at intake
The record (every ⏺, in order) → the two-layer audit (the hub re-runs B2's asserts on the FILED capture; re-derives the artifact's identity from the Actions page line and the hash) → **FE-113 → VERIFIED** (law #22: the four keys read on the wire, the literal `entity`, ISO-8601) → **OR-FAILCHAN → CLOSED** on the two stop readings (`success · 143 · inactive`) → the capture staged as **FE-113b's inputs** (its instruction: the three files → a recorded fixture + its stability test; a fixture is captured, never generated) → OR-JOURNALD-PRIO's number → Row 16's count → the nightly lines banked from B0 → the docket rows the findings card opens.
