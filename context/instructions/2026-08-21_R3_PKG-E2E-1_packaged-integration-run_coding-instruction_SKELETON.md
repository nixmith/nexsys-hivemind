<!--
file: context/instructions/2026-08-21_R3_PKG-E2E-1_packaged-integration-run_coding-instruction_SKELETON.md
purpose: R-3 / PKG-E2E-1 — THE FIRST END-TO-END INTEGRATION RUN ON THE PACKAGED PATH, EVER (S-10 Tier 1; minted distinct at v51 beat 6: "jlink fix + PrivateDevices loosening + the rehearsal rig"). The jlink half landed at core 7c9e4fa (R-1/R-2, CI-proven; the hardware legs ride the 2026-08-22 card sitting). THIS WU = the rehearsal rig (R-3a, operator, measured-first per H7) + the PrivateDevices loosening landed byte-identical to the measurement (R-3b, coder lane) + the rebuild/re-install that hands R-4 a shipped artifact to re-rep on. R-4 (the ~45-min re-rep on the SHIPPED unit) is the act that lifts the two D-1 DO-NOT-SAY items — nothing in THIS WU lifts any claim (H9: a fence lifts only on the lifting WU's return on disk + audited).
audience: the hub (finalization after the Saturday ⏺ intake); then Nick (R-3a operator blocks) + the R-3b Coder lane (host-side Claude Code per D12; zero Java expected).
status: SKELETON (v55 beat 1; AMENDED beat 3 — **R-3 RULED CLONE** (Nick, 2026-08-21) and the enrichment listing banked: A-2 is now AUTHORED against the real custody set + yaml facts; the remaining [⏺-GROUNDED-AT-INTAKE] slots are the Saturday ⏺s only). NOT DISPATCHABLE until the hub's finalization stamp replaces this line (one pass after the 2026-08-22 sitting).
baseline: core 7c9e4fa (the unit at distribution/systemd/homesynapse.service is the R-3b edit target; verify at launch); the held card `hs-fresh` carrying `7c9e4fa` (the bare-id version string — `hs_version` wraps only a–f-leading ids) after Saturday Block 2 [⏺-GROUNDED-AT-INTAKE: the installed version + whether the conditional store reset ran].
return: nexsys-hivemind/context/audits/<filing-date>_R3_PKG-E2E-1_return.md (R-3b, lane-filed, filing-day dated) + nexsys-hivemind/context/audits/<filing-date>_R3a_rehearsal_operator-record.md (hub-filed from Nick's ⏺ pastes — chat is not a storage tier).
-->

# R-3 / PKG-E2E-1 — The Packaged-Path Integration Run (rehearsal rig → unit loosening → the R-4 hand-off)

## §0 Context and objective (why this is weekend 2's anchor)

**What is true today (banked):** the packaged artifact boots, goes RUNNING, serves health/auth/dashboard, and — as of `7c9e4fa` — links `jdk.jfr` so the bus's metrics path no longer kills every publish (R-1's check 4 proves the write path on a clean runner; the card sitting proves it on hardware). **What is NOT yet true on the packaged path:** an integration has never run on it. Two known blockers were named by the H3 Stage-2 return §9.4 and are independent of F-23: (1) `homesynapse.service` sets `PrivateDevices=yes`, so the service cannot see a serial coordinator at all (the unit's own RAMP comment names the loosening); (2) the service user `homesynapse` is not in `dialout`, the group that owns `/dev/ttyUSB*` nodes on Debian. A third class has never been measured: the REST of the hardening block (`ProtectSystem=strict`, `SystemCallFilter=@system-service` with `SystemCallErrorNumber=EPERM`, `PrivateTmp=yes`, `RestrictAddressFamilies=`) has never hosted jSerialComm + the EZSP/ASH stack (F-24's class: "the hardened unit has never executed outside the runner"). **R-3 exists to MEASURE all three on real hardware, then land the loosening as a shipped unit that is byte-identical to the measured drop-in (H13), then hand R-4 a rebuilt artifact to re-rep on.**

**The fence language this WU serves but does not touch (D-1, verbatim until R-4's return is on disk + audited):** "the packaged artifact runs integrations" · "the packaged artifact publishes events" — DO-NOT-SAY on every surface. `distribution/README.md:117` stays fenced until W2-3: **README.md is UNTOUCHED by R-3** (documentation rows land under `distribution/docs/`).

**Sequencing (measured, then green — H7):** R-3a the rehearsal on the held card under a systemd DROP-IN (an operator act; nothing in the repo changes) → the measured drop-in text is the SPEC for R-3b → R-3b lands the unit edit + the docs row (coder lane; CI install-smoke on the push is the gate of record — it cannot see a coordinator, so it certifies only that the loosened unit still boots/serves on the runner) → rebuild the `.deb` on the bench card → re-install on the held card with the drop-in REMOVED (the shipped unit is what R-4 measures) → **R-4**.

## §1 Files to read (R-3b lane, before writing anything; the hub read them at authoring — pins below)

`distribution/systemd/homesynapse.service` WHOLE (the edit target; the RAMP comment block at the `PrivateDevices=yes` line is the seam) · `distribution/deb/build-deb.sh` (the unit is copied verbatim into the package — `cp -p "${DIST}/systemd/homesynapse.service" …/lib/systemd/system/`) · `distribution/deb/debian/postinst` (enable + start on configure; the unit is not edited there) · `distribution/smoke/run-smoke.sh` (checks 1–9; no integration probe — the R-10 purpose-gap question stays open) · `distribution/docs/boot-contract-map.md` (the packaged path-model: `HOMESYNAPSE_HOME=/var/lib/homesynapse`, config at `config/`, data at `data/`) · `integration/integration-zigbee/MODULE_CONTEXT.md` §§5.1/5.5 (PRODUCTION run mode: `resolvePort()` → the `integrations.zigbee.serial_port` key else the VID:PID locator `10c4:ea60`; custody at `<dataDirectory>/zigbee-network.json` + the INDEPENDENT SecretStore `.root-key`/`scope_keys.json`/`secrets.enc`; `zigbee-devices.json` the device cache) · `app/homesynapse-app/src/main/java/com/homesynapse/app/Main.java` (`zigbeeDataDir = baseDir.resolve("data").resolve("zigbee")` — the adapter data directory is `$HOMESYNAPSE_HOME/data/zigbee/`, pinned at source) · `integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/ZigbeeIntegrationAdapter.java` `resolvePort()` (:596–:613 at 7c9e4fa) + `resumeOrForm()` (:690–:700) · the H3 Stage-2 return §9.4 · `nexsys-bench/iac/99-zigbee-coordinator.rules` (the bench's stable `/dev/zigbee` handle + autosuspend-off for the SONOFF `10c4:ea60` serial `0ae2dd7cecf8ef11b80168135c2a50c9`). **No Java module is touched → no `module-info.java` embeds apply; zero `.java` edits (if one seems needed, STOP and flag).**

## §2 THE RIG-SHAPE RULING (Nick, one word — the hub authors the R-3a blocks for the ruled shape)

The decisive source fact: **`ZigbeeIntegrationAdapter.resumeOrForm()` FORMS A NEW NETWORK whenever `parameterStore.load()` is empty** — i.e., whenever `<dataDirectory>/zigbee-network.json` is absent or unparseable. A fresh packaged data dir + the bench coordinator = the bench network RE-FORMED (new PAN, new key; the six joined devices orphaned; hours of re-pairing). That rules out "plug the bench dongle into the held card and see" — the H3-era SD-5 fence ("the coordinator never attaches to the held card") is replaced for R-3 not by trust but by a custody STOP-gate. Two lawful shapes:

- **CLONE (RECOMMENDED) — the bench-fleet migration rehearsal.** Copy the bench's self-contained zigbee custody directory (`/home/homesynapse/hs-bench/data/zigbee/` — `zigbee-network.json` + `.root-key` + `scope_keys.json` + `secrets.enc` + `zigbee-devices.json` [+ `scope_nonce_counters.json` if present]) onto the held card at `/var/lib/homesynapse/data/zigbee/` (owner `homesynapse:homesynapse`, dir 0700, files 0600), and the bench's `config/homesynapse.yaml` + `config/integrations/*.yaml` onto `/var/lib/homesynapse/config/` (NEVER the token store, NEVER the config-dir `.root-key`/`scope_keys.json`/`secrets.enc` — the held card owns its own). Then move the bench coordinator to the held-card boot (it is the same Pi — the dongle never leaves the USB3 port; the CARD changes) and the packaged service RESUMES the bench network with full device knowledge: the six real devices report into the packaged path; the bench-hero automation runs on it; the explain surface renders on the packaged dashboard. **Why recommended:** zero new hardware; it rehearses the literal Nov-25 move (bench → product) and yields R-4 evidence on the real fleet. **Risk named:** the bench is DOWN for the rehearsal window (daylight only; the coordinator is back + the bench floor `[PASS]` before 03:00 CT); the custody snapshot may diverge afterwards (device-cache + TCLK-seed writes on the held card — accepted; the bench keeps its own copy; the network identity is stable because `formation.resume()` NEVER re-forms — a params/NVRAM mismatch throws PIE "never re-form silently"); `!secret`/`!env` tags in the bench yaml would fail to resolve on the held card (a boot CONFIGURATION_FAILURE, exit 10, no restart — the §4 P-rows read the yaml for tags before the copy). **The STOP-gate that replaces SD-5:** the packaged service never starts with the coordinator visible until `zigbee-network.json` is PRESENT, PARSES, and names the bench's channel/PAN (`ch20`, PAN `0x774c` per the 2026-08-20 boot glance — re-read at ⏺), and `secrets.enc` is present with the bench's byte size — because `load()` present ⇒ resume-or-PIE, never form.
- **SPARE — a second coordinator + a fresh network + a spare device.** A second EZSP dongle (the identical SONOFF Dongle-E family for transport-dialect parity — v13 EZSP pinned to owned silicon) in a second USB port; the packaged service FORMS a fresh network under a generated seed (lawful since M9.6-SEED's silicon leg passed); `integrations.zigbee.channel` pinned away from the bench's ch20 (e.g. 25); one spare device joins through `permit_join_duration` → `device_proposed` → adoption via `adopt_devices` (the Tier-1 config surface, M9.4-ADP) → reports → events. **Why not first:** needs hardware that may not be on hand, a spare un-joined device, and an adoption round-trip; the evidence is a one-device network, not the fleet. **Why still valuable:** zero bench downtime; it is the true first-install household path; it can run on a weekday evening. If a spare dongle + device are at hand, SPARE can ALSO run as a second rehearsal after CLONE.

**RULED — CLONE (Nick, 2026-08-21 evening).** Nick's articulation, banked as law for this WU: (a) the `resumeOrForm()` read settles it — "plug and see" is a destructive act in disguise; (b) the javadoc's mismatch posture ("never adopt a wrong network, never silently re-form over corrupt custody — propagates PERMANENT") means a PARTIAL clone fails honestly rather than damaging anything — so the custody listing guarantees COMPLETENESS of the clone, it does not inform the ruling; (c) **THE INVARIANT, stated here so the single-Pi card swap stops enforcing it by accident: ONE COORDINATOR, ONE BOOT — the bench card and the held card never run concurrently against the same custody, and clones travel ONE direction only (bench → held card), never back.** SPARE remains the right shape for R-5-era destructive testing — a different weekend, a different WU.

**The enrichment read (2026-08-21, pasted; the CLONE ground):** `~/hs-bench/config/`: `homesynapse.yaml` (1208 B, Jul 9) · `integrations/zigbee.yaml` (299 B, Jul 21) · `home_id` · `api_tokens` + `initial_api_token` (the 08-20 22:06 rotation) · `schemas/` (dir) — NEVER cloned: the token pair, `home_id`, `schemas/`. `~/hs-bench/data/zigbee/`: `.root-key` (32 B, **0400**, Jul 18 21:09) · `scope_keys.json` (248 B) · `secrets.enc` (568 B) · `zigbee-network.json` (122 B, Jul 18 21:09 — the E3 re-formation under the generated seed) · `zigbee-devices.json` (4551 B, Aug 21 21:00 — live cache) · NOT cloned: `zigbee-network.json.ch20-0x9b65.retired` (the retired PAN) and `_pre-seed-backup-20260719/`. The yaml facts: `integrations/zigbee.yaml` carries `serial_port: /dev/zigbee` (:1), `channel: 20` (:2), `adopt_devices:` (:3, a list follows); NO `!secret`/`!env` tag in either file (the grep matched none) — P6's CONFIGURATION_FAILURE hazard is CLEAR. `home_id` stays the held card's own (AMD-34: stamped on every event; the held card's install identity is its own).

## §3 R-3a — the rehearsal (operator; the held card; [⏺-GROUNDED-AT-INTAKE] slots marked)

**Precondition (from Saturday):** the held card runs `7c9e4fa` (Block 2's re-install), `dpkg -s homesynapse` = `install ok installed` [⏺-GROUNDED-AT-INTAKE: confirm; also whether `initial_api_token` exists on the held card — the dashboard pairing below reads it via `sudo homesynapse-token`]. The drop-in below is the MEASUREMENT instrument; it is removed before R-4.

**A-1 The drop-in (the candidate loosening — measured, never assumed):**
```
# WHERE: the held card, as nick.
sudo mkdir -p /etc/systemd/system/homesynapse.service.d
sudo tee /etc/systemd/system/homesynapse.service.d/10-serial-coordinator.conf >/dev/null <<'EOF'
[Service]
PrivateDevices=no
DevicePolicy=closed
DeviceAllow=char-ttyUSB rw
DeviceAllow=char-ttyACM rw
SupplementaryGroups=dialout
EOF
sudo systemctl daemon-reload && systemctl cat homesynapse.service | tail -12
```
⏺ the `systemctl cat` tail (the drop-in must appear below the unit). Rationale pinned: `char-ttyUSB`/`char-ttyACM` are the `/proc/devices` class names (majors 188/166) — class rules survive replug renumbering where a node path would not; `DevicePolicy=closed` keeps the standard pseudo-devices (`/dev/null`, `urandom`, …) and nothing else; `SupplementaryGroups=dialout` matches the node's `root:dialout 0660` ownership. Candidate ONLY — if the measurement demands more (e.g. `SystemCallFilter=@system-service ioctl`-class additions, or `ProtectSystem` relaxations for jSerialComm's native-library extraction under `PrivateTmp`), the MEASURED text wins and is what R-3b ships.

**A-2 Custody + config (CLONE — authored beat 3 from the enrichment read; the version slots are the Saturday ⏺s):**

```bash
# WHERE: the bench card (`ssh pi`), the bench app RUNNING (the custody files are immutable post-formation; the device cache is a snapshot). Delete nothing.
grep -nE "/home/|/mnt/|path" /home/homesynapse/hs-bench/config/homesynapse.yaml /home/homesynapse/hs-bench/config/integrations/zigbee.yaml
# expect: no absolute bench paths (a hit = ⏺, STOP, paste — the cloned yaml would point the packaged service at a bench path)
mkdir -p ~/artifacts && tar czf ~/artifacts/zigbee-custody-for-r3.tar.gz -C /home/homesynapse/hs-bench/data zigbee/.root-key zigbee/scope_keys.json zigbee/secrets.enc zigbee/zigbee-network.json zigbee/zigbee-devices.json && tar czf ~/artifacts/bench-config-for-r3.tar.gz -C /home/homesynapse/hs-bench/config homesynapse.yaml integrations/zigbee.yaml && sha256sum ~/artifacts/zigbee-custody-for-r3.tar.gz ~/artifacts/bench-config-for-r3.tar.gz /etc/udev/rules.d/99-zigbee-coordinator.rules
# ⏺ the three hashes; the rule file is the bench's INSTALLED copy (LF-clean) — never the Windows checkout's
```

```bash
# WHERE: your desktop. Three files down, three files up; re-hash on each hop.
mkdir -p ~/Desktop/r3-rehearsal && cd ~/Desktop/r3-rehearsal && scp pi:artifacts/zigbee-custody-for-r3.tar.gz pi:artifacts/bench-config-for-r3.tar.gz pi:/etc/udev/rules.d/99-zigbee-coordinator.rules . && sha256sum zigbee-custody-for-r3.tar.gz bench-config-for-r3.tar.gz 99-zigbee-coordinator.rules
```

Normal shutdown of the bench (`ssh pi 'sudo shutdown -h now'`), bench card OUT, held card IN, boot; then:

```bash
# WHERE: your desktop → the held card.
cd ~/Desktop/r3-rehearsal && scp -i ~/.ssh/id_ed25519_pi zigbee-custody-for-r3.tar.gz bench-config-for-r3.tar.gz 99-zigbee-coordinator.rules nick@hs-fresh.local: && ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local
```

```bash
# WHERE: the held card, as nick. Lay the custody down with the SERVICE STOPPED (the adapter reads custody at start).
cd ~ && sha256sum zigbee-custody-for-r3.tar.gz bench-config-for-r3.tar.gz 99-zigbee-coordinator.rules
# expect: the same three hashes as the bench and the desktop
sudo systemctl stop homesynapse.service && systemctl is-active homesynapse.service
# expect: inactive
sudo ls -la /var/lib/homesynapse/data/zigbee/ /var/lib/homesynapse/config/ 2>&1
# ⏺ — the held card's own state BEFORE the clone (a prior data/zigbee/ here means the packaged adapter already ran on this card — ⏺ and paste before continuing)
sudo tar xzf ~/zigbee-custody-for-r3.tar.gz -C /var/lib/homesynapse/data && sudo tar xzf ~/bench-config-for-r3.tar.gz -C /var/lib/homesynapse/config
sudo chown -R homesynapse:homesynapse /var/lib/homesynapse/data/zigbee /var/lib/homesynapse/config/homesynapse.yaml /var/lib/homesynapse/config/integrations && sudo chmod 0700 /var/lib/homesynapse/data/zigbee /var/lib/homesynapse/config/integrations && sudo chmod 0400 /var/lib/homesynapse/data/zigbee/.root-key && sudo chmod 0600 /var/lib/homesynapse/data/zigbee/scope_keys.json /var/lib/homesynapse/data/zigbee/secrets.enc /var/lib/homesynapse/data/zigbee/zigbee-network.json /var/lib/homesynapse/data/zigbee/zigbee-devices.json /var/lib/homesynapse/config/homesynapse.yaml /var/lib/homesynapse/config/integrations/zigbee.yaml
sudo cp 99-zigbee-coordinator.rules /etc/udev/rules.d/ && sudo udevadm control --reload && sudo udevadm trigger && sleep 2 && ls -la /dev/zigbee /dev/ttyUSB0
# expect: /dev/zigbee -> ttyUSB0 and the node root:dialout 0660 (the dongle has been in this Pi's USB3 port since H3)
```

**THE STOP-GATE (replaces SD-5 for this WU) — run it, ⏺ it, and read it before the next block:**

```bash
# WHERE: the held card. The clone must be COMPLETE, or the packaged adapter FORMS a new network on the bench dongle.
sudo python3 -m json.tool /var/lib/homesynapse/data/zigbee/zigbee-network.json && sudo ls -la /var/lib/homesynapse/data/zigbee/ && sudo sha256sum /var/lib/homesynapse/data/zigbee/secrets.enc /var/lib/homesynapse/data/zigbee/scope_keys.json
# expect: JSON parses, channel 20 and the bench's PAN (0x774c-class — read the field name as printed); five files with the bench's byte sizes (32 / 248 / 568 / 122 / 4551), owned homesynapse, .root-key 0400; the two hashes (compare to the bench's: run the same sha256sum on the bench beforehand if you want the pair — the tarball hash already covers it)
```
**Any missing/unparseable file = STOP. Do not proceed to A-1/A-3 with an incomplete clone.**

**A-3 The measured boot (after A-1's drop-in AND A-2's STOP-gate):** `sudo systemctl start homesynapse.service` → `journalctl -u homesynapse.service -b --no-pager | grep -E "zigbee\.(port_identity_captured|transport_override|network_resumed|network_formed|transport_unbound|transport_unsupported)|EPERM|Permission denied|SerialPort|ASH|NETWORK_UP"` ⏺. **Predictions (filed pre-run, the discriminator set):** (P-a) `zigbee.port_identity_captured` then `zigbee.network_resumed: channel=20 panId=0x774c` [⏺-GROUNDED-AT-INTAKE: the PAN from the clone's JSON] = the loosening is sufficient; (P-b) `zigbee.transport_unbound` = the device class rule or the group did not take (inspect `ls -la /dev/ttyUSB0`, `id homesynapse`, `systemctl show -p DeviceAllow homesynapse.service`); (P-c) `Permission denied`/`EPERM` on open or ioctl with the node visible = the syscall filter or the group — one drop-in line per hypothesis, re-measured, each ⏺'d; (P-e) the fleet RE-ADOPTS on the packaged path: the held card's events DB carries no bench history, so the device REGISTRY starts empty even though the zigbee device cache knows the six devices — prediction: the cached devices are re-proposed on their first frame and auto-adopted through the cloned `adopt_devices` list (`zigbee.proposal_accepted`-class INFO lines; entities appear on the dashboard) — the alternate arm (P-f): devices stay unregistered until they ANNOUNCE, in which case a single power-cycle of the motion sensor is the probe (⏺ which arm fired; both are findings for the R-4 lift language); (P-d) **`zigbee.network_formed` = the STOP-gate failed — POWER OFF the Pi at once, ⏺, the hub adjudicates (the bench network has been re-formed; recovery = the bench's own custody still resumes ITS parameters — `formation.resume()` will PIE on NVRAM mismatch — so the recovery path is a NEW formation on the bench + re-pair; this is the priced worst case and the reason the gate exists).**

**A-4 The evidence window (the R-4 dress rehearsal; ≥30 min):** the dashboard over the tunnel (`ssh -L 7070:127.0.0.1:7070 -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local`; token via `sudo homesynapse-token` on the card — read it on the card's terminal only) → the Devices list shows the fleet (availability honest) → a motion wave → bench-hero fires on the packaged path → the explain surface renders → `sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'` before/after (⏺ both; the delta is integration-attributable) → `journalctl … | grep -ciE "NoClassDefFoundError|jdk.jfr|BusMetrics"` = 0 (the same instrument, third rig).

**A-5 Restore:** coordinator stays in the port; `sudo shutdown -h now` → bench card IN → boot → `~/bench.sh scenario boot-health` `[PASS]` ⏺ (the bench resumes its own custody; if the glance shows a changed PAN — STOP, ⏺, the hub adjudicates). The drop-in stays on the held card until R-3b's artifact is installed there; then it is removed (`sudo rm` is lawful for a file this WU created — or `mv` aside) so R-4 measures the shipped unit alone.

## §4 Pre-verification rows (the hub fills `context/pre-verifications/WU-R3.md` at finalization; the rows below are the charge)

| # | Assumption | Pinned at authoring (7c9e4fa) | Verified at ⏺/launch |
|---|---|---|---|
| P1 | The unit's hardening block + the RAMP seam | `distribution/systemd/homesynapse.service`: `PrivateDevices=yes` directly under the 5-line RAMP comment; `SystemCallFilter=@system-service` + `SystemCallErrorNumber=EPERM`; `PrivateTmp=yes`; `ProtectSystem=strict`; no `DeviceAllow`, no `SupplementaryGroups` | R-3b lane: line numbers at checkout |
| P2 | The adapter data dir on the packaged path | `Main.java`: `baseDir.resolve("data").resolve("zigbee")` ⇒ `/var/lib/homesynapse/data/zigbee/`; bench ⇒ `/home/homesynapse/hs-bench/data/zigbee/` | the §2 enrichment `ls` |
| P3 | Custody file set | `PersistentNetworkParameterStore`: `zigbee-network.json` + independent SecretStore (`.root-key`, `scope_keys.json`, `secrets.enc`); `ZigbeeIntegrationAdapter:282` `zigbee-devices.json`; `StandardScopeKeyManager` may write `scope_nonce_counters.json` beside `.root-key` | the `ls -la` of both dirs |
| P4 | The form-vs-resume decision | `resumeOrForm()` :690–:700: `:691 if (parameterStore.load().isPresent())` ⇒ `protocol.resumeStored()` (:692, INFO `zigbee.network_resumed` :693) else `formNetwork()` (:696, INFO `zigbee.network_formed` :697); `resumeStored()` ⇒ `formation.resume()` which throws PIE on key-missing or NVRAM mismatch (never re-forms) | unchanged at checkout (R-3b lane re-reads) |
| P5 | Port resolution | `resolvePort()` :596: configured `serial_port` wins (synthesized if unenumerated), else the VID:PID locator `10c4:ea60` | BANKED 2026-08-21: the bench yaml's `serial_port: /dev/zigbee` (`integrations/zigbee.yaml:1`) — hence the udev rule on the held card (A-2); `channel: 20` (:2) is the form-path pin, inert on resume |
| P6 | Config layout | `YamlLoader`: root `homesynapse.yaml` + `integrations/` include dir under `$HOMESYNAPSE_HOME/config`; `!secret`/`!env`/`!include` tags exist | BANKED 2026-08-21: NO `!secret`/`!env` in either bench file (grep matched none); the absolute-path glance rides A-2's first line |
| P7 | The packaged unit is the repo unit | `build-deb.sh` copies `distribution/systemd/homesynapse.service` verbatim into the staging tree; `postinst` enables + starts; no unit edit at install | the R-3b rebuild's `.deb` carries the new unit (`dpkg-deb -c` glance) |
| P8 | The held card's state | [⏺-GROUNDED-AT-INTAKE: version `7c9e4fa` expected, token-file presence, row-count baseline, journal discriminator 0, whether `data/zigbee/` already exists on the held card] | Saturday ⏺s + the A-2 pre-clone listing |
| P9 | The coordinator identity | SONOFF `10c4:ea60` serial `0ae2dd7cecf8ef11b80168135c2a50c9` (the udev rule); direct to the Pi USB3 port since H3 | `lsusb` on the held card |

## §5 R-3b — the repo delta (coder lane; authored at finalization from the MEASURED drop-in)

| File | Kind | Content |
|---|---|---|
| `distribution/systemd/homesynapse.service` | M | the RAMP comment block replaced by the measured loosening — the drop-in's `[Service]` lines VERBATIM (H13), each with a one-line rationale comment; the comment records the rehearsal date + the held-card measurement as its source |
| `distribution/docs/boot-contract-map.md` | M | one row: the serial-device posture (class-based `DeviceAllow`, `dialout`, what stays hardened) |
| `integration/integration-zigbee/MODULE_CONTEXT.md` | M (hub-owned fold, post-return) | one gotcha row: the packaged-path custody location + the resume-or-form consequence for migrations |

**Stages exactly 2 M in the lane's census** (the MC fold is the hub's, the F-14-row precedent). Zero Java. README.md untouched. CI twins untouched (install-smoke cannot see a coordinator; the gate certifies boot/serve under the loosened unit on the runner). `bash -n` N/A; `systemd-analyze verify distribution/systemd/homesynapse.service` on the host if available (flag if absent). Red-first accounting (#18): no fixture can red at HEAD for a unit-file change — the rehearsal's own (P-b)/(P-c) arms ARE the red leg, disclosed.

## §6 What R-4 measures (the fence-lift criteria, written now so the lift language is precise — H9)

On the SHIPPED artifact (R-3b's rebuilt `.deb`, drop-in removed), one ~45-min re-rep on the held card: (1) `zigbee.network_resumed` (CLONE) or `zigbee.network_formed` (SPARE) in the journal; (2) ≥1 device `Available` on the packaged dashboard with a fresh `Last reported`; (3) an integration-attributable event-row delta + zero throw signatures; (4) one automation run with a rendered explanation. Then — and only then — the lift, into the positive-scope register: *"verified on real hardware at commit <R-3b SHA>: the packaged artifact runs the Zigbee integration and publishes events (six-device bench fleet, <date>, the re-rep record at context/audits/…)"*. The `README.md:117` "deterministic and self-checksumming" line is NOT lifted by R-4 (W2-3 owns it).

## §7 Finalization checklist (the hub's one pass after the Saturday intake)

[x] §2 ruled CLONE (2026-08-21) · [x] the enrichment read pasted + banked (§2) · [ ] every [⏺-GROUNDED-AT-INTAKE] slot filled from the sitting ⏺s · [ ] `WU-R3.md` written (P1–P9 with observed values) · [x] the A-2 tar/scp/install block written zero-placeholder in the packet idiom (beat 3) · [ ] R-3a dispatched as an operator packet (`context/handoff/<date>_R3a_rehearsal_operator-packet.md`) · [ ] after the R-3a ⏺s: §5 authored from the measured drop-in; the R-3b instruction stamped ISSUE-READY and dispatched to the coder lane · [ ] this SKELETON line replaced by the finalization stamp.
