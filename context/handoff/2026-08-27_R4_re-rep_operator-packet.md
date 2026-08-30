<!--
file: context/handoff/2026-08-27_R4_re-rep_operator-packet.md
purpose: R-4 — THE RE-REP ON THE SHIPPED ARTIFACT (Mon 2026-08-31 evening, ~2.5–3.5 h incl. swap + fleet-arm + restore): R-3b's CI-built arm64 `.deb` (the loosening IN THE UNIT) installs on the held card, the R-3a drop-in comes OFF, and the shipped unit alone boots the real fleet and meets the four lift criteria. THE WEEK'S PRIZE: on this packet's audited record — and only then — the hub lifts the two D-1 DO-NOT-SAY sentences into the positive-scope register (H9; the lift is the HUB's Sunday-night write, never this packet's act). Authored AHEAD at v57 beat 3 (Thu); the three ⟨SLOTS⟩ fill at the R-3b landing (Sat evening).
audience: Nick (the operator) + the hub (the record intake → the fence lift).
status: DRAFT-PENDING-R-3b · ★-AMENDED v58 beat 7 (2026-08-30): the R-3a findings folded — the §9-B re-adoption rewrite · criteria (2)/(4) restated (rulings R-1/R-2) · the fleet-arm choreography · the optional power-loss leg · the grep/token/reset-failed/no-pager fixes; R-4 RUNS MON 2026-08-31 EVENING — the ⟨SLOTS⟩ — TWO OF THREE STAMPED (v58 b8; RE-STAMPED v58 b10 from NICK’S OWN re-commit 2026-08-30T15:14:00-05:00 = 20:14:00Z — the beat-9 correction executed): the R-3b sha = `7c57d7f` · the predicted version = `0.1.0+git20260830.201400.g7c57d7f` (both from the landed core commit, computed at the instrument). ALL THREE STAMPED (v58 b11, from the CI read): run id 33333075509 · the origin hash PINNED in §1 (`452a2f95…`) · the echo-line version = the prediction EXACT (.deb Version == image VERSION == 0.1.0+git20260830.201400.g7c57d7f — H12 on the third surface). THE PACKET IS COMPLETE; G1 CLOSED.
baseline at authoring (CONFORMED v58 b7 — R-3a ran SUN 08-30): the held card carries `0.1.0+git20260823.231355.gdec35be` + the 10-serial-coordinator.conf drop-in + the CLONED bench custody (resumed, six devices) + the R-3a day's event rows (incl. the RIG re-adoptions ×2, the §10 evidence and the power-loss survival — ROWS-A ≈ 53+); the bench card is back IN with its floor `[PASS]` (restored 15:06 ET). The coordinator NEVER leaves hub 3-2.4 Port 2 in this packet (both cards resume the SAME network custody — the ONE COORDINATOR, ONE BOOT invariant is held by the sequential card swap alone).
fences: delete NOTHING (every aside is `mv` to `~/r3-history/`) · the token pair untouched, values never pasted · NO `--allow-downgrades` (the new `+git` date orders ABOVE the installed one — apt asking for the flag = a FINDING, STOP) · the D-1 sentences are not said anywhere until the hub's lift · Pi clocks are ET — every ⏺ written ET or Z · the bench floor is back `[PASS]` before 03:00 CT (Tue 09-01).
predictions (H12, filed now): the install is an ordinary UPGRADE (no downgrade line) · post-install `dpkg` == image `VERSION` == 0.1.0+git20260830.201400.g7c57d7f · with the drop-in OFF, `systemctl show` reads the loosening FROM THE UNIT (PrivateDevices=no · the two DeviceAllow class rules · SupplementaryGroups=dialout) · the restart resumes in seconds: `zigbee.network_resumed: channel=20 panId=0x774c`, ZERO `network_formed` · the four criteria: (1) resumed ✓ (2) ≥1 device Available, freshness AT THE STORE (fresh `state_reported`/`availability_changed` rows — the list's Last-reported render is a known read-path gap, §10-G) (3) ROWS-B > ROWS-A, discriminator 0 (4) ≥1 bench-hero run with a rendered explanation, the automation RE-BOUND to the rig's re-adopted entities as an explicit step (ruling R-1 = (b)) · restore: `[PASS] boot-health — 6/6 positive · 0 forbidden`, PAN 0x774c, the by-id string byte-identical (F-S20).
-->

# R-4 — the re-rep on the shipped artifact (operator packet · Mon 2026-08-31, ★-amended v58 b7)

**The shape (≈2.5–3.5 h):** §1 fetch + hash (desktop, 10 min — can run Saturday night) → §2 the swap to the held card (10 min) → §3 the new artifact on (10 min) → §4 THE DROP-IN COMES OFF (5 min) → §5 the measured boot (5 min) → §6 the fleet-arm + the evidence core (~75 min) → §7 the restore (20 min). **STOP-gates in their own blocks. Every ⏺ is a paste-either-way.**

## §1 Fetch — R-3b's arm64 artifact (desktop; browser + Git Bash)

The run page: `https://github.com/nexsys-io/homesynapse-core/actions/runs/33333075509` (the install-smoke run on commit 7c57d7f). Open the **arm64** job → the "Version-grammar echo" step → **⏺ its `version-grammar echo green: … sha256 <64 hex>  homesynapse_0.1.0+git20260830.201400.g7c57d7f_arm64.deb` line whole** (the origin hash). Then Artifacts (bottom of the run's Summary page) → **`distribution-artifacts-arm64`** → `~/Downloads`.

```bash
# WHERE: Git Bash. Keep R-3a's artifact folder clean of the OLD .deb before unpacking the new one.
mkdir -p ~/r3-history && mv ~/r3-artifact/homesynapse_0.1.0+git20260823.231355.gdec35be_arm64.deb ~/r3-history/ 2>/dev/null; cd ~/r3-artifact && powershell.exe -NoProfile -Command "Expand-Archive -LiteralPath \"$(cygpath -w ~/Downloads/distribution-artifacts-arm64.zip)\" -DestinationPath \"$(cygpath -w ~/r3-artifact)\" -Force" && ls -la && sha256sum homesynapse_*_arm64.deb
# expect: ONE .deb named homesynapse_0.1.0+git20260830.201400.g7c57d7f_arm64.deb (≈61.8 MB); its hash EQUALS THE PINNED ORIGIN HASH `452a2f95a89c4021af53916dfd0b63ad27ca804db455af0c1c6552de1b216937` (the arm64 echo line's sha256, pinned at the CI read, v58 b11). ⏺ both. (Two .debs listed = the mv above missed — STOP, paste, sort the folder before anything ships to the card.)
```

```bash
# STOP-GATE R4-1: exactly one .deb · the hash equals the run-log line · the name carries 0.1.0+git20260830.201400.g7c57d7f (the `+git` date NEWER than 20260823.231355). Anything else → STOP, paste.
```

## §2 The swap (bench → held card; the radio stays in Port 2)

```bash
# WHERE: the bench card (ssh pi). FIRST (★): read the overnight nightly digest — `ls -t ~/hs-bench/bundles | head -3` + the digest glance; ⏺ one line (the bench never goes down un-read). THEN normal shutdown; then: power OFF → bench card OUT → held card IN (`hs-fresh — R-3/R-4 rig — +git dec35be · drop-in ON · bench custody CLONED`) → power ON → ~90 s. The coordinator STAYS plugged (the held card resumes the same cloned custody — never forms).
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
# expect: no stray .deb before the copy ("---" alone) · the SAME hash as §1 (hop 3 = the run log's) · Version 0.1.0+git20260830.201400.g7c57d7f · arm64. ⏺ all.
```

```bash
# WHERE: the held card. ★ SPLIT (v58 b7 — the R-3a §4-B lesson): the baseline + integrity gate FIRST, so a bad store can stop the install.
sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;' && sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'PRAGMA integrity_check;'
# expect: ROWS pre ⏺ · `ok`. Anything but `ok` → STOP, paste — NOTHING installs over a bad store.
```

```bash
# WHERE: the held card. The install (NO --allow-downgrades; apt asking to downgrade = STOP — the ordering scheme has failed, a finding).
sudo apt install -y ~/homesynapse_*_arm64.deb 2>&1 | tail -12 && dpkg-query -W -f '${Version}\n' homesynapse && cat /opt/homesynapse/VERSION && sleep 20 && systemctl is-active homesynapse.service && sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;' && sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'PRAGMA integrity_check;'
# expect: an UPGRADE tail (no "downgrad" token) · 0.1.0+git20260830.201400.g7c57d7f TWICE · active · ROWS-AFTER ≥ pre · `ok`. ⏺ all.
```

```bash
# STOP-GATE R4-2: version exact in both places · active · zero row loss · integrity ok. Any miss → `sudo systemctl status homesynapse.service --no-pager -l` ⏺, STOP, paste.
```

## §4 THE DROP-IN COMES OFF (the shipped unit stands alone from here)

```bash
# WHERE: the held card. The whole drop-in dir moves aside (delete nothing) → reload → prove the loosening now comes FROM THE UNIT.
sudo systemctl stop homesynapse.service && sudo mv /etc/systemd/system/homesynapse.service.d ~/r3-history/homesynapse.service.d-removed-$(date -u +%Y%m%d) && sudo systemctl daemon-reload && systemctl cat --no-pager homesynapse.service | grep -cE '/etc/systemd/system/homesynapse.service.d'; systemctl show --no-pager homesynapse.service -p PrivateDevices -p DeviceAllow -p SupplementaryGroups -p DevicePolicy
# expect: `0` (no drop-in section in `systemctl cat`) · PrivateDevices=no · DeviceAllow lists the char-ttyUSB/char-ttyACM class rules · SupplementaryGroups=dialout · DevicePolicy=closed — ALL FROM THE SHIPPED UNIT. ⏺ every line. (PrivateDevices=yes here = the unit on the card is NOT R-3b's → STOP, paste.)
```

## §5 The measured boot (the shipped unit, the real fleet)

```bash
# WHERE: the held card.
sudo systemctl reset-failed homesynapse.service 2>/dev/null; sudo systemctl start homesynapse.service; sleep 60; systemctl is-active homesynapse.service; sudo journalctl -u homesynapse.service -b --no-pager | grep -E "zigbee\.(port_identity_captured|network_resumed|network_formed|network_parameter_mismatch|transport_unbound|transport_failed|device_relinked|device_proposed|device_adopted|ingestion_unknown_sender|permit_join_opened|ncp_configured)|registry\.projection_live|health-probe|Configuration issue" | head -30
# expect: active · `port_identity_captured` (the F-S20 by-id string) → `network_resumed: channel=20 panId=0x774c` · ZERO network_formed · `[health-probe] ready (200) at http://127.0.0.1:7070/health` · re-adoption signals per §9-B (the arm proper happens at §6). ⏺ whole (incl. any `Configuration issue` lines VERBATIM — a commissioned capture; and `ingestion_unknown_sender` = the un-re-adopted fleet SPEAKING, §10-Q — expected, never a fault; `adopt_list_loaded` is DEBUG — absence is NOT failure). Re-run once at +60 s if quiet. `network_formed` → POWER OFF, STOP (same law as R-3a §9).
```

```bash
# STOP-GATE R4-3: active · resumed · zero formed · ready names /health. Then the window opens.
```

## §6 The fleet arm + the evidence core (a ≥45 min window AFTER the arm; the four lift criteria — H9's exact objects)

```bash
# WHERE: the held card. The window opens: ⏺ ROWS-W0 + the Z time.
sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'; date -u +%H:%M:%SZ
```

**THE FLEET ARM (★ v58 b7 — finding §9-B: a cloned-custody rig RE-ADOPTS; the 5+1 census was never reachable and is not the bar).** (i) Copy the yaml aside (`sudo cp /etc/homesynapse/config/homesynapse.yaml ~/r3-history/homesynapse.yaml.pre-R4` — delete nothing), then add `permit_join_duration` to its zigbee block → `sudo systemctl restart homesynapse.service`. (ii) Wake the motion sensor with a SHORT button press (>5 s is a network LEAVE — the R-3a lesson); expect the measured ~10 s chain `device_announce → device_proposed → proposal_accepted: source=config → device_adopted → reporting_configured`; other devices re-adopt as they speak (a `SECURED_REJOIN` needs no window). ⏺ each adoption line. (iii) **THE (b) RE-BIND (ruling R-1):** capture the rig's NEW entity ULIDs (`sudo journalctl -u homesynapse.service -b --no-pager | grep -E "device_adopted|entity_registered" | tail -8`), rewrite `bench-hero`'s `entity_ref`s in the yaml to the new trigger/action ULIDs AND remove `permit_join_duration` in the same edit → `sudo systemctl restart homesynapse.service` → verify the rule loads clean (zero config WARNs naming bench-hero). ⏺ the re-bind in prose (old→new ULIDs). Two attempts max; will-not-converge → STOP, paste — the criterion records MISS and the hub adjudicates. **Then the dashboard over the tunnel** (`ssh -L 7070:127.0.0.1:7070 -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local`): **⏺ in prose with times** — (C2) ≥1 device **Available** (freshness is evidenced AT THE STORE at window close — the list's `Last reported`/`Current` render is a known read-path gap, §10-G, and is NOT the instrument) · one real motion wave, then stand still · **(C4) bench-hero fires on the packaged path and the explain surface renders "why did it fire?"** for that run — the run exists because of the (iii) re-bind, and the lift sentence says so.

```bash
# WHERE: the held card, at ≥45 min after ROWS-W0. The window close: (C1)(C3) + the runs surface.
sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'; date -u +%H:%M:%SZ; sudo journalctl -u homesynapse.service -b --no-pager | grep -ciE "NoClassDefFoundError|jdk.jfr|BusMetrics"; sudo journalctl -u homesynapse.service -b --no-pager | grep -cE "zigbee\.network_resumed"; sudo journalctl -u homesynapse.service -b --no-pager | grep -cE "zigbee\.network_formed"; TOK=$(sudo homesynapse-token | grep -oE '[A-Za-z0-9+/=_-]{40,}' | tail -1); test ${#TOK} -eq 44 && echo TOKLEN-OK; curl -s -H "Authorization: Bearer $TOK" http://127.0.0.1:7070/api/v1/runs | head -c 1200; echo
# ★ the helper prints a LABELLED block, not a bare token (the R-3a lesson); TOKLEN-OK gates. The token value is never ⏺'d.
# ★ C2 store-freshness: open `sudo sqlite3 -readonly /var/lib/homesynapse/data/homesynapse-events.db`, run `.schema events` ONCE (⏺ the column names), then select the newest `state_reported` / `availability_changed` rows using the schema's own timestamp column — expect timestamps INSIDE the window. ⏺ the two newest lines. (Never invent column names; the schema read is the instrument.)
# expect: ROWS-W1 > ROWS-W0 · `0` throw-discriminator · resumed-count ≥1 · formed-count 0 · the runs JSON showing ≥1 bench-hero run. ⏺ all (the JSON carries no token).
```

```bash
# STOP-GATE R4-4 (the lift gate — read it, ⏺ each): C1 resumed ✓ · C2 ≥1 Available + store-freshness rows inside the window ✓ (the list render is not the instrument) · C3 rows delta + discriminator 0 ✓ · C4 one run + rendered explanation ✓ (the re-bound refs — the record says so). FOUR OF FOUR → the record supports the lift (the HUB writes it tonight). Any miss → paste-either-way; the hub adjudicates what the record supports; NOTHING is said publicly either way.
```


```bash
# OPTIONAL §6b — THE UNCONTROLLED-POWER-LOSS LEG (★ adopted v58 b6; runs ONLY after ALL FOUR R4-4 ⏺s are banked — the lift evidence is never at stake). Pull the held card's plug mid-idle → 10 s → power back → ~90 s.
systemctl is-active homesynapse.service; sudo journalctl -u homesynapse.service -b --no-pager | grep -E "zigbee\.(network_resumed|network_formed)" | tail -2; sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'; sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'PRAGMA integrity_check;'
# expect: active (auto-start) · resumed, ZERO formed · rows ≥ the window close · `ok`. ⏺ all. Any miss = a FINDING (paste); the lift already stands on §6.
```

## §7 The restore (the bench night)

```bash
# WHERE: the held card → the physical swap → the bench card.
sudo systemctl stop homesynapse.service && systemctl is-active homesynapse.service; sudo shutdown -h now
# inactive (a `transport_failed` with retransmits=0/crcRejects=0/timeouts=0 during THIS stop is the ORDERLY-CLOSE signature — §10-O — not port loss; ⏺ without alarm) → ACT LED stops → power OFF → held card OUT (re-label: `hs-fresh — R-4 DONE — 0.1.0+git20260830.201400.g7c57d7f · shipped unit · bench custody`) → bench card IN → power ON → ~90 s.
```

```bash
# WHERE: the bench card (ssh pi). F-S15: start it yourself, then the floor.
~/bench.sh status; ~/bench.sh start; sleep 45; ~/bench.sh status; ~/bench.sh scenario boot-health; grep -E "zigbee\.(port_identity_captured|network_resumed)" ~/hs-bench/current.log | tail -2
# expect: NOT running → start (RADIO UP 12–18 s) → running → `[PASS] boot-health — 6/6 positive · 0 forbidden` → `network_resumed: channel=20 panId=0x774c` + the byte-identical by-id string (F-S20). ⏺ all. A changed PAN = STOP, paste.
```

## §8 What the hub banks — and the lift (the hub's act, tonight)

One line each: the hash chain · the upgrade with NO flag · the drop-in OFF + the unit's own loosening at `systemctl show` · resumed/zero-formed · the four criteria MET/MISS · the restore `[PASS]`. **THE GUARD (v57 beat 8, adopted from the strategy review): the lift consumes R-4's ⏺s only THROUGH the audit — a record that passes WITH ANY ANOMALY (an unexpected token, a timing oddity, a partial criterion) HOLDS the lift one beat while the hub adjudicates. The claim is forever; a beat of delay is nothing.** On an audited, anomaly-free four-of-four the hub writes THE FENCE LIFT: the two D-1 sentences enter the positive-scope register as *"verified on real hardware at commit 7c57d7f: the packaged artifact runs the Zigbee integration and publishes events (six-device bench fleet RE-ADOPTED on the cloned-custody rig; the bench-hero automation re-bound to the rig’s entities as an explicit rehearsal step; 2026-08-31, the re-rep record at context/audits/…)"* — at the claim-fence register + the north-star honesty state. `distribution/README.md:117` does NOT lift (W2-3 owns it). The ⏺ record files at `context/audits/2026-08-31_R4_re-rep_operator-record.md`.
