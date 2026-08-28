<!--
file: context/handoff/2026-08-27_R4_re-rep_operator-packet.md
purpose: R-4 — THE RE-REP ON THE SHIPPED ARTIFACT (Sun 2026-08-30, ~2–3 h incl. swap + restore; the ~45-min evidence core): R-3b's CI-built arm64 `.deb` (the loosening IN THE UNIT) installs on the held card, the R-3a drop-in comes OFF, and the shipped unit alone boots the real fleet and meets the four lift criteria. THE WEEK'S PRIZE: on this packet's audited record — and only then — the hub lifts the two D-1 DO-NOT-SAY sentences into the positive-scope register (H9; the lift is the HUB's Sunday-night write, never this packet's act). Authored AHEAD at v57 beat 3 (Thu); the three ⟨SLOTS⟩ fill at the R-3b landing (Sat evening).
audience: Nick (the operator) + the hub (the record intake → the fence lift).
status: DRAFT-PENDING-R-3b — the ⟨SLOTS⟩: the R-3b sha · its install-smoke run id + the ARM64 `version-grammar echo green: … sha256 …` line · the predicted version `0.1.0+git⟨R-3b commit date UTC⟩.g⟨sha⟩`. Everything else is final. FILL ALL THREE BEFORE RUNNING (each slot is marked in-line).
baseline at authoring: after R-3a (Sat), the held card carries `0.1.0+git20260823.231355.gdec35be` + the 10-serial-coordinator.conf drop-in + the CLONED bench custody (resumed, six devices) + Saturday's event rows; the bench card is back IN with its floor `[PASS]`. The coordinator NEVER leaves hub 3-2.4 Port 2 in this packet (both cards resume the SAME network custody — the ONE COORDINATOR, ONE BOOT invariant is held by the sequential card swap alone).
fences: delete NOTHING (every aside is `mv` to `~/r3-history/`) · the token pair untouched, values never pasted · NO `--allow-downgrades` (the new `+git` date orders ABOVE the installed one — apt asking for the flag = a FINDING, STOP) · the D-1 sentences are not said anywhere until the hub's lift · Pi clocks are ET — every ⏺ written ET or Z · the bench floor is back `[PASS]` before 03:00 CT.
predictions (H12, filed now): the install is an ordinary UPGRADE (no downgrade line) · post-install `dpkg` == image `VERSION` == ⟨PREDICTED-VERSION⟩ · with the drop-in OFF, `systemctl show` reads the loosening FROM THE UNIT (PrivateDevices=no · the two DeviceAllow class rules · SupplementaryGroups=dialout) · the restart resumes in seconds: `zigbee.network_resumed: channel=20 panId=0x774c`, ZERO `network_formed` · the four criteria: (1) resumed ✓ (2) ≥1 device Available, fresh `Last reported` (3) ROWS-B > ROWS-A, discriminator 0 (4) ≥1 bench-hero run with a rendered explanation · restore: `[PASS] boot-health — 6/6 positive · 0 forbidden`, PAN 0x774c, the by-id string byte-identical (F-S20).
-->

# R-4 — the re-rep on the shipped artifact (operator packet · Sun 2026-08-30)

**The shape (≈2–3 h):** §1 fetch + hash (desktop, 10 min — can run Saturday night) → §2 the swap to the held card (10 min) → §3 the new artifact on (10 min) → §4 THE DROP-IN COMES OFF (5 min) → §5 the measured boot (5 min) → §6 the ~45-min evidence core → §7 the restore (20 min). **STOP-gates in their own blocks. Every ⏺ is a paste-either-way.**

## §1 Fetch — R-3b's arm64 artifact (desktop; browser + Git Bash)

The run page: `https://github.com/nexsys-io/homesynapse-core/actions/runs/⟨R-3b-RUN-ID — FILL IN⟩` (the install-smoke run on commit ⟨R-3B-SHA — FILL IN⟩). Open the **arm64** job → the "Version-grammar echo" step → **⏺ its `version-grammar echo green: … sha256 <64 hex>  homesynapse_⟨PREDICTED-VERSION⟩_arm64.deb` line whole** (the origin hash). Then Artifacts (bottom of the run's Summary page) → **`distribution-artifacts-arm64`** → `~/Downloads`.

```bash
# WHERE: Git Bash. Keep R-3a's artifact folder clean of the OLD .deb before unpacking the new one.
mkdir -p ~/r3-history && mv ~/r3-artifact/homesynapse_0.1.0+git20260823.231355.gdec35be_arm64.deb ~/r3-history/ 2>/dev/null; cd ~/r3-artifact && powershell.exe -NoProfile -Command "Expand-Archive -LiteralPath \"$(cygpath -w ~/Downloads/distribution-artifacts-arm64.zip)\" -DestinationPath \"$(cygpath -w ~/r3-artifact)\" -Force" && ls -la && sha256sum homesynapse_*_arm64.deb
# expect: ONE .deb named homesynapse_⟨PREDICTED-VERSION⟩_arm64.deb (≈61.8 MB); its hash EQUALS the arm64 echo line's sha256. ⏺ both. (Two .debs listed = the mv above missed — STOP, paste, sort the folder before anything ships to the card.)
```

```bash
# STOP-GATE R4-1: exactly one .deb · the hash equals the run-log line · the name carries ⟨PREDICTED-VERSION⟩ (the `+git` date NEWER than 20260823.231355). Anything else → STOP, paste.
```

## §2 The swap (bench → held card; the radio stays in Port 2)

```bash
# WHERE: the bench card (ssh pi). Normal shutdown; then: power OFF → bench card OUT → held card IN (`hs-fresh — R-3/R-4 rig — +git dec35be · drop-in ON · bench custody CLONED`) → power ON → ~90 s. The coordinator STAYS plugged (the held card resumes the same cloned custody — never forms).
sudo shutdown -h now
```

```bash
# WHERE: the held card (ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local). The boot glance — Saturday's state resumed.
date; dpkg-query -W -f '${Version}\n' homesynapse; systemctl is-active homesynapse.service; sudo journalctl -u homesynapse.service -b --no-pager | grep -E "zigbee\.(network_resumed|network_formed|port_identity_captured)" | tail -3; sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'
# expect: the ET clock ⏺ · `0.1.0+git20260823.231355.gdec35be` · active · `network_resumed: channel=20 panId=0x774c` (ZERO network_formed) · a row count (⏺ = ROWS-A). Anything else → STOP, paste.
```

## §3 The new artifact on (an ordinary upgrade — NO flag)

```bash
# WHERE: desktop → the held card. The old .deb in the card's home moves aside first (delete nothing), so the glob is unique.
ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local 'mkdir -p ~/r3-history && mv ~/homesynapse_0.1.0+git20260823.231355.gdec35be_arm64.deb ~/r3-history/ 2>/dev/null; ls ~/homesynapse_*_arm64.deb 2>/dev/null; echo "---"' && cd ~/r3-artifact && scp -i ~/.ssh/id_ed25519_pi homesynapse_*_arm64.deb nick@hs-fresh.local: && ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local 'sha256sum ~/homesynapse_*_arm64.deb; dpkg-deb --field ~/homesynapse_*_arm64.deb Version Architecture'
# expect: no stray .deb before the copy ("---" alone) · the SAME hash as §1 (hop 3 = the run log's) · Version ⟨PREDICTED-VERSION⟩ · arm64. ⏺ all.
```

```bash
# WHERE: the held card. Baseline → install (NO --allow-downgrades) → verify. apt asking to downgrade = STOP (the ordering scheme has failed — a finding).
sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;' && sudo apt install -y ~/homesynapse_*_arm64.deb 2>&1 | tail -12 && dpkg-query -W -f '${Version}\n' homesynapse && cat /opt/homesynapse/VERSION && sleep 20 && systemctl is-active homesynapse.service && sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;' && sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'PRAGMA integrity_check;'
# expect: ROWS pre ⏺ · an UPGRADE tail (no "downgrad" token) · ⟨PREDICTED-VERSION⟩ TWICE · active · ROWS-AFTER ≥ pre · `ok`. ⏺ all.
```

```bash
# STOP-GATE R4-2: version exact in both places · active · zero row loss · integrity ok. Any miss → `sudo systemctl status homesynapse.service --no-pager -l` ⏺, STOP, paste.
```

## §4 THE DROP-IN COMES OFF (the shipped unit stands alone from here)

```bash
# WHERE: the held card. The whole drop-in dir moves aside (delete nothing) → reload → prove the loosening now comes FROM THE UNIT.
sudo systemctl stop homesynapse.service && sudo mv /etc/systemd/system/homesynapse.service.d ~/r3-history/homesynapse.service.d-removed-$(date -u +%Y%m%d) && sudo systemctl daemon-reload && systemctl cat homesynapse.service | grep -cE '/etc/systemd/system/homesynapse.service.d'; systemctl show homesynapse.service -p PrivateDevices -p DeviceAllow -p SupplementaryGroups -p DevicePolicy
# expect: `0` (no drop-in section in `systemctl cat`) · PrivateDevices=no · DeviceAllow lists the char-ttyUSB/char-ttyACM class rules · SupplementaryGroups=dialout · DevicePolicy=closed — ALL FROM THE SHIPPED UNIT. ⏺ every line. (PrivateDevices=yes here = the unit on the card is NOT R-3b's → STOP, paste.)
```

## §5 The measured boot (the shipped unit, the real fleet)

```bash
# WHERE: the held card.
sudo systemctl start homesynapse.service; sleep 60; systemctl is-active homesynapse.service; sudo journalctl -u homesynapse.service -b --no-pager | grep -E "zigbee\.(port_identity_captured|network_resumed|network_formed|network_parameter_mismatch|transport_unbound|transport_failed|device_relinked|device_proposed|device_adopted)|registry\.projection_live|health-probe" | head -30
# expect: active · `port_identity_captured` (the F-S20 by-id string) → `network_resumed: channel=20 panId=0x774c` · ZERO network_formed · `[health-probe] ready (200) at http://127.0.0.1:7070/health` · the fleet arm (relink/adopt per Saturday's precedent). ⏺ whole. Re-run once at +60 s if quiet. `network_formed` → POWER OFF, STOP (same law as R-3a §9).
```

```bash
# STOP-GATE R4-3: active · resumed · zero formed · ready names /health. Then the window opens.
```

## §6 The evidence core (≥45 min; the four lift criteria — H9's exact objects)

```bash
# WHERE: the held card. The window opens: ⏺ ROWS-W0 + the Z time.
sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'; date -u +%H:%M:%SZ
```

Dashboard over the tunnel (`ssh -L 7070:127.0.0.1:7070 -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local`; token via `sudo homesynapse-token` on the card's terminal only): **⏺ in prose with times** — (C2) the Devices list: ≥1 device **Available** with a fresh `Last reported` (expect the 5+1 census) · one real motion wave, then stand still · **(C4) bench-hero fires on the packaged path and the explain surface renders "why did it fire?"** for that run.

```bash
# WHERE: the held card, at ≥45 min after ROWS-W0. The window close: (C1)(C3) + the runs surface.
sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'; date -u +%H:%M:%SZ; sudo journalctl -u homesynapse.service -b --no-pager | grep -ciE "NoClassDefFoundError|jdk.jfr|BusMetrics"; sudo journalctl -u homesynapse.service -b --no-pager | grep -cE "zigbee\.network_resumed"; sudo journalctl -u homesynapse.service -b --no-pager | grep -cE "zigbee\.network_formed"; curl -s -H "Authorization: Bearer $(sudo homesynapse-token)" http://127.0.0.1:7070/api/v1/runs | head -c 1200; echo
# expect: ROWS-W1 > ROWS-W0 · `0` throw-discriminator · resumed-count ≥1 · formed-count 0 · the runs JSON showing ≥1 bench-hero run. ⏺ all (the JSON carries no token).
```

```bash
# STOP-GATE R4-4 (the lift gate — read it, ⏺ each): C1 resumed ✓ · C2 ≥1 Available + fresh Last reported ✓ · C3 rows delta + discriminator 0 ✓ · C4 one run + rendered explanation ✓. FOUR OF FOUR → the record supports the lift (the HUB writes it tonight). Any miss → paste-either-way; the hub adjudicates what the record supports; NOTHING is said publicly either way.
```

## §7 The restore (the bench night)

```bash
# WHERE: the held card → the physical swap → the bench card.
sudo systemctl stop homesynapse.service && systemctl is-active homesynapse.service; sudo shutdown -h now
# inactive → ACT LED stops → power OFF → held card OUT (re-label: `hs-fresh — R-4 DONE — ⟨PREDICTED-VERSION⟩ · shipped unit · bench custody`) → bench card IN → power ON → ~90 s.
```

```bash
# WHERE: the bench card (ssh pi). F-S15: start it yourself, then the floor.
~/bench.sh status; ~/bench.sh start; sleep 45; ~/bench.sh status; ~/bench.sh scenario boot-health; grep -E "zigbee\.(port_identity_captured|network_resumed)" ~/hs-bench/current.log | tail -2
# expect: NOT running → start (RADIO UP 12–18 s) → running → `[PASS] boot-health — 6/6 positive · 0 forbidden` → `network_resumed: channel=20 panId=0x774c` + the byte-identical by-id string (F-S20). ⏺ all. A changed PAN = STOP, paste.
```

## §8 What the hub banks — and the lift (the hub's act, tonight)

One line each: the hash chain · the upgrade with NO flag · the drop-in OFF + the unit's own loosening at `systemctl show` · resumed/zero-formed · the four criteria MET/MISS · the restore `[PASS]`. On an audited four-of-four the hub writes THE FENCE LIFT: the two D-1 sentences enter the positive-scope register as *"verified on real hardware at commit ⟨R-3B-SHA⟩: the packaged artifact runs the Zigbee integration and publishes events (six-device bench fleet, 2026-08-30, the re-rep record at context/audits/…)"* — at the claim-fence register + the north-star honesty state. `distribution/README.md:117` does NOT lift (W2-3 owns it). The ⏺ record files at `context/audits/2026-08-30_R4_re-rep_operator-record.md`.
