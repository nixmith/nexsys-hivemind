<!--
file: context/handoff/2026-08-26_R3a_rehearsal_operator-packet.md
purpose: R-3a — THE REHEARSAL on the held card, as ONE self-contained operator packet (the operator-packet class, arc-35): the E3-RED → Block I → E3-GREEN triple (the packaged-unit artifact-absent restart proof + the first CI-built `+git` artifact onto the card, hash-verified on every hop) → the custody CLONE (the bench fleet, one direction only) → the drop-in measurement → the packaged boot on real silicon with the real fleet → the ≥30-min evidence window → the restore. Authored WED 2026-08-26 (v57 beat 1) AHEAD of Friday's print-ready act: every fold ruled at v56 beat 5 is IN (F-S9 · F-S10 · F-S11 · F-S13 · F-S15 · F-S19 · E-P5 · F-S20 · F-S12) and the row-count expectation is corrected to the instrument's own assertion (zero LOSS, never "unchanged"). Base texts: `context/instructions/2026-08-21_R3_PKG-E2E-1_packaged-integration-run_coding-instruction_SKELETON.md` §3 (A-1…A-5, RULED CLONE) + `context/handoff/2026-08-22_R3-packet_new-blocks_CI-artifact-install_and_E3-restart-proof.md` (E3/Block I) — this packet SUPERSEDES both as the operator text; they stay as the design record.
audience: Nick (the operator; the held card `hs-fresh`, the bench card, the desktop) · the hub (the ⏺ intake → `context/audits/<filing-date>_R3a_rehearsal_operator-record.md`, hub-filed; chat is not a storage tier).
status: PRINT-READY (v57 beat 2, Thu 2026-08-27) — the `dec35be` install-smoke run is **32672999145** (banked at Nick's paste: the amd64 leg printed `hs_version=0.1.0+git20260823.231355.gdec35be` EXACTLY as predicted, `.deb Version` == image `VERSION`); the ARM64 leg's `version-grammar echo green: … sha256 …` line is the origin hash — read it on the run page at fetch time (§4 I-1) and ⏺ it; STOP-GATE I-0/I-1 compare against it. Run: Sat 2026-08-29, DAYLIGHT (4–6 h; the bench floor back `[PASS]` before 03:00 CT = 04:00 ET — the nightly's 04:30 ET oneshot must find the bench up).
baseline: held card `hs-fresh` = `7c9e4fa` (dpkg `Version: 7c9e4fa` = `/opt/homesynapse/VERSION`), store 14 rows at its last boot (2026-08-23), `initial_api_token` PRESENT 44 B `-rw-r--r--` (F-S9/F-S10), `data/zigbee/` PRESENT (written at the Aug-23 16:54 ET boot with NO radio — F-S11), UNPATCHED (95 OS packages pending — F-S12 HOLD-PATCH through R-4: the artifact is the only variable) · bench = `e845cd9` build, floor `8/9 PASS · 1 SKIP(hue-online)`, network ch20 PAN 0x774c, fleet 5 AVAILABLE + 1 UNAVAILABLE · the CI artifact = the `dec35be` arm64 `.deb` (R-9 + R-7b inside; predicted `hs_version=0.1.0+git20260823.231355.gdec35be` — H12, derived from `common.sh` `hs_version()` + `TZ=UTC git log -1 --format=%cd` on `dec35be`).
fences honoured: ONE COORDINATOR, ONE BOOT (§2 ruling (c)) — the dongle is UNPLUGGED from the bench shutdown until §6's STOP-gate passes, and re-plugged ONLY then (F-S11, explicit) · the R-7b fence at the instrument (§4's Version-shape STOP-gates: no `0.1.0+g<sha>` artifact reaches the card) · `--allow-downgrades` exactly ONCE per card (§4 I-3) · delete NOTHING (every aside is `mv`) · the token pair never cloned, its VALUES never pasted (paths only) · the D-1 DO-NOT-SAY pair is untouched by this packet (R-4 owns the lift; H9) · `distribution/README.md` untouched · nothing on the core checkout (R-3b is the next core touch) · the held card stays UNPATCHED (F-S12).
-->

# R-3a — the rehearsal (operator packet · Sat 2026-08-29, daylight)

**Goal.** The packaged path runs the real Zigbee fleet on real silicon for the first time — measured under a systemd drop-in whose text becomes R-3b's spec byte-for-byte (H13) — after the held card has (1) proven the E3 availability class on hardware, (2) moved onto the first CI-built `+git` artifact through the channel R-7/R-7b built, and (3) proven the class closed. **Done-when (all of):** E3-RED shows `token not yet available` + `TIMEOUT after 90s`; Block I's `dpkg-query` prints `0.1.0+git20260823.231355.gdec35be` with the hash chain equal on three hops and rows AFTER ≥ rows BEFORE; E3-GREEN shows `ready (200) … /health` with the artifact absent + the `200/401` pair; A-3's journal shows `zigbee.network_resumed: channel=20 panId=0x774c` (never `network_formed`); A-4 banks a ≥30-min window with ≥1 device Available, an integration-attributable row delta, zero throw signatures, one automation run with a rendered explanation; A-5 restores the bench to `[PASS] boot-health` with the coordinator at its byte-identical port identity. **Every ⏺ is a paste-either-way** — a miss is a finding, not a failure of the day.

**The shape of the day (est. 4–6 h; the clock bounds are per block).** §1 bench-side pre-flight (10 min, bench UP) → §2 THE SWAP + held-card pre-flight (15 min) → §3 E3-RED (≤3 min + restore) → §4 Block I (20 min) → §5 E3-GREEN (≤2 min) → §6 the CLONE + THE STOP-GATE (15 min, service STOPPED, radio still UNPLUGGED) → §7 the drop-in (2 min) → §8 the coordinator PLUG (2 min) → §9 A-3 the measured boot (5–30 min, the discriminator set) → §10 A-4 the evidence window (≥30 min) → §11 A-5 the restore (20 min; `~/bench.sh start` — F-S15). **STOP-gates get their own block; read each before the next block.** Timestamps: the Pi clocks are **ET** — write ET or Z on every ⏺, never bare CT (F-S21).

**Predictions FILED before the run (H12; scored at intake, misses owned):** (E3-RED) `restart rc=1` after ~90 s; ≥1 `token not yet available` line then `TIMEOUT after 90s`; unit `activating`/`failed`. (Block I) desktop hash == card hash == the run-log `sha256`; `Version: 0.1.0+git20260823.231355.gdec35be` and `Architecture: arm64`; apt prints a downgrade line; post-install `dpkg` == image `VERSION`; `ExecStartPost … --health-path /health`; rows AFTER ≥ BEFORE (each boot appends ≈4 lifecycle rows — Δ+4 at the Aug-23 Block 2); discriminator 0; `ready (200) … /health`. (E3-GREEN) `restart rc=0` in seconds; `NRestarts=0 Result=success`; `200` then `401`. (A-3) P-a `zigbee.port_identity_captured` then `zigbee.network_resumed: channel=20 panId=0x774c`; the fleet re-proposes and auto-adopts through the cloned `adopt_devices` list (P-e) — or waits for an ANNOUNCE (P-f); **P-d `zigbee.network_formed` = POWER OFF at once** (the priced worst case; the gate in §6 exists to make it impossible). (A-5) bench `[PASS] boot-health — 6/6 positive · 0 forbidden`, `zigbee.network_resumed: channel=20 panId=0x774c`, the by-id string byte-identical (F-S20).

---

## §1 Bench-side pre-flight (the bench card UP, the bench app RUNNING — the custody files are immutable post-formation; the device cache is a snapshot)

```bash
# WHERE: the bench card (ssh pi). PF-0 the clock gate + the identity + P-3 REFRESHED (F-S19: "these three AMONG the listing" — the dir has SEVEN entries; the values are the §OP-A post-state of Aug 23).
date; id -un; ls -la /home/homesynapse/hs-bench/config/
# expect: the ET clock ⏺ · `homesynapse` (the user that owns the 0400 custody — so the tar below can read it WITHOUT sudo; any other user → prefix `sudo` on the tar line) · AMONG the seven entries: `api_tokens` 300 B `-rw-------` Aug 23 13:12 · `initial_api_token` 44 B `-rw-------` Aug 23 13:12 · `api_tokens.rotated-2026-08-20` 132 B. A different listing → ⏺ and paste; NO act (the token store is never touched by this packet).
```

```bash
# WHERE: the bench card. The yaml path glance (P6) + the custody listing at tar time (the cache size is LIVE — this listing, not 4551, is what §6 compares against).
grep -nE "/home/|/mnt/|path" /home/homesynapse/hs-bench/config/homesynapse.yaml /home/homesynapse/hs-bench/config/integrations/zigbee.yaml; ls -la /home/homesynapse/hs-bench/data/zigbee/
# expect: NO grep hit (a hit = ⏺, STOP, paste — the cloned yaml would point the packaged service at a bench path) · the listing: `.root-key` 32 B 0400 · `scope_keys.json` 248 B · `secrets.enc` 568 B · `zigbee-network.json` 122 B · `zigbee-devices.json` (LIVE size — ⏺ it) · possibly `scope_nonce_counters.json` (⏺ if present — it is NOT in the tar list below; add it to the tar line if it exists) · the retired `.ch20-0x9b65.retired` file + `_pre-seed-backup-20260719/` stay behind. ⏺ the listing whole.
```

```bash
# WHERE: the bench card. The custody tar + the config tar + the udev rule, hashed. SECRET-BEARING (the bench's zigbee root key travels in the custody tar): they go to your Windows HOME (not a synced folder), and nowhere near a repo.
mkdir -p ~/artifacts && tar czf ~/artifacts/zigbee-custody-for-r3.tar.gz -C /home/homesynapse/hs-bench/data zigbee/.root-key zigbee/scope_keys.json zigbee/secrets.enc zigbee/zigbee-network.json zigbee/zigbee-devices.json && tar czf ~/artifacts/bench-config-for-r3.tar.gz -C /home/homesynapse/hs-bench/config homesynapse.yaml integrations/zigbee.yaml && chmod 600 ~/artifacts/zigbee-custody-for-r3.tar.gz ~/artifacts/bench-config-for-r3.tar.gz && tar tzf ~/artifacts/zigbee-custody-for-r3.tar.gz && sha256sum ~/artifacts/zigbee-custody-for-r3.tar.gz ~/artifacts/bench-config-for-r3.tar.gz /etc/udev/rules.d/99-zigbee-coordinator.rules
# expect: five `zigbee/…` member lines (add `zigbee/scope_nonce_counters.json` to the tar line FIRST if the listing above showed it) · three hashes — ⏺ all three (hop 1 of 3). The rule file is the bench's INSTALLED copy (LF-clean) — never the Windows checkout's.
```

```bash
# WHERE: your desktop, Git Bash. Hop 2 of 3. (~ = C:\Users\Nick — deliberately NOT Desktop.)
mkdir -p ~/r3-rehearsal && cd ~/r3-rehearsal && scp pi:artifacts/zigbee-custody-for-r3.tar.gz pi:artifacts/bench-config-for-r3.tar.gz pi:/etc/udev/rules.d/99-zigbee-coordinator.rules . && sha256sum zigbee-custody-for-r3.tar.gz bench-config-for-r3.tar.gz 99-zigbee-coordinator.rules
# expect: the SAME three hashes as the bench. ⏺. A mismatch → re-copy that file; do not continue on a mismatch.
```

```bash
# STOP-GATE §1: three hashes equal on two hops · no yaml path hit · the custody listing ⏺'d (with the live cache size and the nonce-counter presence noted). Also confirm ~/r3-artifact holds the CI .deb from §4 I-1 (fetch it NOW while the bench is up, if not already done — §4 I-1 needs only the desktop + the browser). Anything short → STOP, paste.
```

---

## §2 THE SWAP + the held-card pre-flight (the coordinator fence starts HERE — F-S11)

```bash
# WHERE: the bench card. Normal shutdown. Then the PHYSICAL sequence, in this order, no step skipped:
sudo shutdown -h now
# 1. wait for the ACT LED to stop → power OFF.
# 2. UNPLUG the coordinator (the SONOFF Dongle Plus MG24 on hub 3-2.4 Port 2). It stays out through §3–§7. ⏺ "unplugged HH:MM ET".
# 3. bench card OUT · held card IN (labeled `hs-fresh — R-3/R-4 rig — 7c9e4fa`) · power ON · wait ~90 s.
```

```bash
# WHERE: your desktop → the held card. PF-0 clock · E-P5 the throttle word (the Aug-23 D-2 absence, now measured) · the radio ABSENT (the fence, verified at the instrument) · the app up.
ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local 'date; hostname; sudo vcgencmd get_throttled; lsusb | grep -ci "10c4:ea60"; ls -l /dev/zigbee /dev/ttyUSB0 2>&1; systemctl is-active homesynapse.service'
# expect: the ET clock ⏺ · `hs-fresh` · `throttled=0x0` (anything else → ⏺ and paste; a non-zero word does NOT stop the day but every later timing carries it) · `0` (NO coordinator visible — the fence holds; a `1` here = STOP, unplug it, paste) · both `No such file` · `active`. ⏺ all six lines.
```

```bash
# WHERE: the held card (ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local). The rig glance — `sudo` on every config/data read (F-S13: the dirs are 0700 homesynapse). Read-only.
dpkg-query -W -f '${Version}\n' homesynapse; cat /opt/homesynapse/VERSION; sudo ls -la /var/lib/homesynapse/config/; sudo ls -la /var/lib/homesynapse/data/ /var/lib/homesynapse/data/zigbee/; sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'; sudo journalctl -u homesynapse.service -b --no-pager | grep -ciE "NoClassDefFoundError|jdk.jfr|BusMetrics"; sudo journalctl -u homesynapse.service -b --no-pager | grep -E "health-probe" | tail -2
# expect: `7c9e4fa` twice · AMONG the config listing: `api_tokens` 132 B `-rw-r--r--` · `home_id` 26 B · `initial_api_token` 44 B `-rw-r--r--` Aug 13 07:35 — the 644 modes are F-S10 (KNOWN; OR-TOKEN-MODE-644), NOT a stop · `data/zigbee/` PRESENT (F-S11 — the held card's OWN, written radio-less on Aug 23; ⏺ its listing: it is moved aside in §6) · rows ≥ 14 (this boot appends its own; ⏺ the number = ROWS-0, the E3-RED baseline) · `0` · `[health-probe] ready (200) at http://127.0.0.1:7070/api/v1/entities` (the 7c9e4fa probe reads the token — F-S14). ⏺ everything.
```

```bash
# STOP-GATE §2: `7c9e4fa` · active · the artifact PRESENT · radio ABSENT · discriminator 0 · ROWS-0 recorded. Anything else → STOP, paste.
```

---

## §3 Block E3-RED — the availability class, measured on the `7c9e4fa` artifact (≤3 min from the restart line; restored in-block)

**Goal:** prove on real hardware that the `7c9e4fa` unit's readiness DEPENDS on the pairing artifact. **F-S9:** the artifact is PRESENT on this card — the block CREATES the absence (`mv`, never `rm`) and restores it. **Done-when:** `token not yet available` lines during a restart with the artifact aside, then the artifact back and the unit `active`.

```bash
# WHERE: the held card. The RED arm: artifact aside → restart → watch the probe → (next block) stop → restore. Hard clock bound: 3 minutes from the restart line.
sudo mv /var/lib/homesynapse/config/initial_api_token /var/lib/homesynapse/config/initial_api_token.e3red && date -u +%H:%M:%SZ && sudo systemctl restart homesynapse.service; echo "restart rc=$?"; date -u +%H:%M:%SZ
# expect: ~90 s wall-clock (the probe burns its --timeout 90), then `restart rc=1` (ExecStartPost failed → the unit failed). ⏺ both timestamps (Z) + the rc.
systemctl is-active homesynapse.service; systemctl show -p NRestarts -p Result -p ExecMainStatus homesynapse.service
# expect: `activating` (auto-restart pending, RestartSec=10) or `failed`; Result=exit-code-class. ⏺ the three lines.
sudo journalctl -u homesynapse.service -b --no-pager --since "-4min" | grep -E "health-probe|Started|Failed|Scheduled restart|start-limit" | tail -20
# expect: ≥1 `[health-probe] token not yet available at /var/lib/homesynapse/config/initial_api_token`, then `[health-probe] TIMEOUT after 90s — service did not become ready`, then a `Failed to start` / `Scheduled restart job` pair. ⏺ the tail. (A `ready (200)` line here = the REFUTATION — the 7c9e4fa probe did not need the token: STOP after the restore block below, paste; the hub re-derives.)
```

```bash
# WHERE: the held card. RESTORE — run this block REGARDLESS of what the RED arm showed.
sudo systemctl stop homesynapse.service; sudo mv /var/lib/homesynapse/config/initial_api_token.e3red /var/lib/homesynapse/config/initial_api_token && sudo ls -la /var/lib/homesynapse/config/initial_api_token && sudo systemctl reset-failed homesynapse.service && sudo systemctl start homesynapse.service && sleep 15 && systemctl is-active homesynapse.service && sudo journalctl -u homesynapse.service -b --no-pager --since "-1min" | grep -E "health-probe" | tail -3
# expect: the artifact back, `-rw-r--r--` 44 B (mv preserves the F-S10 mode) · `active` · `[health-probe] ready (200) at http://127.0.0.1:7070/api/v1/entities`. ⏺ all three. (Not active after 60 s → `sudo systemctl status homesynapse.service --no-pager -l` ⏺, STOP, paste.)
```

```bash
# STOP-GATE E3-RED: the artifact is back AND the unit is `active` (the RED evidence itself is a paste-either-way). Not restored/not active → STOP, paste; do not install anything on a card in an unknown state.
```

---

## §4 Block I — the CI-built arm64 `.deb` (`dec35be`) as the install source (`--allow-downgrades` exactly ONCE on this card)

**Goal:** the held card runs the first CI-built artifact (R-9 + R-7b inside), installed through the channel R-7 built, hash-verified on every hop (CI log → desktop → card), the event store preserved (zero LOSS). **Done-when:** `dpkg-query` prints `0.1.0+git20260823.231355.gdec35be`, the unit is `active`, rows AFTER ≥ ROWS-BEFORE, the discriminator is 0, the probe's ready line names `/health`.

**I-1 Fetch (desktop, Git Bash + the browser; do this any day before Saturday — `gh` is not assumed on the desktop and is ABSENT on the Pi).** The run page: **`https://github.com/nexsys-io/homesynapse-core/actions/runs/32672999145`** (the install-smoke run on commit `dec35be`). **THE ORIGIN ANCHOR (banked v57 beat 5 from the run's own Artifacts box):** `distribution-artifacts-arm64`, 123 MB, digest **`sha256:1fe1c812f665cfcc2da3e9d49cb62676fa32e2f2be7d1317c6620dc5c67acbd1`** — the digest of the ZIP itself, printed by GitHub on the Summary page. The chain: the downloaded zip's sha256 must EQUAL that digest → the `.deb` unpacked from a digest-verified zip is origin-authentic → its sha256 (computed in the block below) becomes the pinned value hops 2–3 compare against. (Optional cross-check, not required: the arm64 JOB's "Version-grammar echo" step prints `version-grammar echo green: … sha256 …  homesynapse_…_arm64.deb` — if you do open it, its sha256 must equal the `.deb` hash the block computes. The amd64 leg's banked line, sha256 `f68e31d5…_amd64.deb`, is a DIFFERENT file and is never the comparison value.)

```bash
# WHERE: your desktop, Git Bash. Browser FIRST: the run page (above) → Artifacts → `distribution-artifacts-arm64` → the zip lands in ~/Downloads. (FILL-IN: nothing in this line — the zip name is the workflow's.)
sha256sum ~/Downloads/distribution-artifacts-arm64.zip && mkdir -p ~/r3-artifact && cd ~/r3-artifact && powershell.exe -NoProfile -Command "Expand-Archive -LiteralPath \"$(cygpath -w ~/Downloads/distribution-artifacts-arm64.zip)\" -DestinationPath \"$(cygpath -w ~/r3-artifact)\" -Force" && ls -la && sha256sum homesynapse_*_arm64.deb
# expect: the ZIP hash = 1fe1c812f665cfcc2da3e9d49cb62676fa32e2f2be7d1317c6620dc5c67acbd1 (the GitHub artifact digest — the ORIGIN; a mismatch = STOP, re-download; if it persists, fall back to the arm64 job's echo-line cross-check and paste both) · ONE .deb named homesynapse_0.1.0+git20260823.231355.gdec35be_arm64.deb (≈61.8 MB) + one .tar.gz (+ logs). ⏺ BOTH hashes — the .deb hash from a digest-verified zip is the PINNED ORIGIN VALUE for hops 2–3 (STOP-gates I-0/I-1 compare against it).
```

```bash
# STOP-GATE I-0 — THE R-7b FENCE at the instrument (Git Bash has no dpkg-deb; the card-side gate I-1 below is the one that binds): the ZIP hash equals the GitHub artifact digest (1fe1c812…) AND the .deb NAME carries `+git<8 digits>.<6 digits>.g<sha>`; a `homesynapse_0.1.0+g<sha>_` or bare-id name is PRE-R-7b and must NOT reach the card. The digest-verified .deb hash is hop 1 of 3. Anything else → STOP, paste.
```

**I-2 Copy + the card-side gate.**

```bash
# WHERE: your desktop → the held card (hop 2 of 3).
cd ~/r3-artifact && scp -i ~/.ssh/id_ed25519_pi homesynapse_*_arm64.deb nick@hs-fresh.local: && ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local 'sha256sum ~/homesynapse_*_arm64.deb; dpkg-deb --field ~/homesynapse_*_arm64.deb Version Architecture'
# expect: the SAME hash as the desktop AND the run log · `Version: 0.1.0+git20260823.231355.gdec35be` · `Architecture: arm64`. ⏺ all three lines.
```

```bash
# STOP-GATE I-1: hash equal on all three hops AND Version matches ^0\.1\.0\+git[0-9]{8}\.[0-9]{6}\.g[0-9a-f]{7,}$ (predicted EXACTLY 0.1.0+git20260823.231355.gdec35be) AND Architecture=arm64. A `-dirty` suffix = a dirty CI tree, impossible by construction → STOP. Any mismatch → STOP, paste, do not install.
```

**I-3 Install — `--allow-downgrades` exactly ONCE on this card** (the bare id `7c9e4fa` sorts ABOVE every `0.1.0+…` — F-S18 proved bare-id ordering live; after this install no later `+git` build ever needs the flag: the scheme is monotone by commit time).

```bash
# WHERE: the held card, as nick. Baseline (the same instrument as update-smoke: rows + integrity + home_id) → install → verify.
sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;' && sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'PRAGMA integrity_check;' && sudo cat /var/lib/homesynapse/config/home_id && echo && dpkg-query -W -f '${Version}\n' homesynapse
# ⏺ all four — ROWS-BEFORE (≥ ROWS-0: the E3-RED restarts appended their lifecycle rows) · `ok` · the home_id (26 chars; the held card's OWN identity — it never changes) · `7c9e4fa`
sudo apt install -y --allow-downgrades ~/homesynapse_*_arm64.deb 2>&1 | tail -15
# expect: a downgrade line (apt's "Downgrading homesynapse from 7c9e4fa to 0.1.0+git…" or dpkg's "downgrading" warning), postinst output, no error. ⏺ the tail.
dpkg-query -W -f '${Version}\n' homesynapse; cat /opt/homesynapse/VERSION; sleep 20; systemctl is-active homesynapse.service; systemctl cat homesynapse.service | grep -E '^ExecStartPost'
# expect: `0.1.0+git20260823.231355.gdec35be` TWICE (dpkg == the image stamp) · `active` · `ExecStartPost=/opt/homesynapse/libexec/health-probe.sh --wait --timeout 90 --health-path /health` (R-9's unit, pinned at dec35be `homesynapse.service:53`). ⏺ all four.
sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'; sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'PRAGMA integrity_check;'; sudo cat /var/lib/homesynapse/config/home_id; echo; sudo journalctl -u homesynapse.service -b --no-pager | grep -ciE "NoClassDefFoundError|jdk.jfr|BusMetrics"; sudo journalctl -u homesynapse.service -b --no-pager --since "-3min" | grep -E "health-probe" | tail -3
# expect: ROWS-AFTER ≥ ROWS-BEFORE (the install's boot appends ≈4; FEWER = event loss = STOP) · `ok` · the SAME home_id · `0` · `[health-probe] ready (200) at http://127.0.0.1:7070/health`. ⏺ all five.
```

```bash
# STOP-GATE I-2: the +git version in BOTH places · active · the ready line names /health · ROWS-AFTER ≥ ROWS-BEFORE · integrity ok · home_id unchanged · discriminator 0. Any miss → `sudo systemctl status homesynapse.service --no-pager -l` ⏺, STOP, paste. (A second `--allow-downgrades` is NEVER needed on this card from here on — a later install asking for it is a FINDING, not a flag to add.)
```

---

## §5 Block E3-GREEN — the same restart, artifact ABSENT, on the R-9 artifact (≤2 min; the H8 hardware close)

**Goal:** the packaged unit restarts to `active` with the pairing artifact ABSENT, because the probe reads `/health`. **F-S9:** the block CREATES the absence (`mv`), proves, restores. **Done-when:** `ready (200) at …/health` with the artifact aside, `active`, `200/401`, then the artifact back.

```bash
# WHERE: the held card, as nick. The GREEN arm — the same verbs as E3-RED, the opposite prediction.
sudo mv /var/lib/homesynapse/config/initial_api_token /var/lib/homesynapse/config/initial_api_token.e3green && date -u +%H:%M:%SZ && sudo systemctl restart homesynapse.service; echo "restart rc=$?"; date -u +%H:%M:%SZ
# expect: the restart returns in SECONDS (not 90), `restart rc=0`. ⏺ the timestamps (Z) + rc.
systemctl is-active homesynapse.service; systemctl show -p NRestarts -p Result homesynapse.service; sudo journalctl -u homesynapse.service -b --no-pager --since "-2min" | grep -E "health-probe|Started" | tail -5
# expect: `active` · `NRestarts=0` `Result=success` · `[health-probe] ready (200) at http://127.0.0.1:7070/health` + `Started homesynapse.service`. NO `token not yet available` line. ⏺ all. (`token not yet available` here = the unit on the card is NOT R-9's — STOP, paste: `systemctl cat homesynapse.service | grep ExecStartPost`.)
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:7070/health; curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:7070/api/v1/entities
# expect: `200` then `401` — the fence proof on hardware (unauthenticated /health open; the API still gated). ⏺ both. (curl is present on this card — verified Aug 23.)
sudo mv /var/lib/homesynapse/config/initial_api_token.e3green /var/lib/homesynapse/config/initial_api_token && sudo ls -la /var/lib/homesynapse/config/initial_api_token && systemctl is-active homesynapse.service
# expect: the artifact back, `-rw-r--r--` 44 B · `active` (a restore needs no restart — the store, not the file, is the key's home). ⏺.
```

```bash
# STOP-GATE E3-GREEN: active with the artifact absent · the ready line names /health · the 200/401 pair · the artifact restored. All four → the E3 class is CLOSED ON HARDWARE (OR-E3-PROBE closes at the hub's next beat). Any miss → STOP, paste; do not proceed to §6.
```

---

## §6 A-2 — THE CLONE (held-card side; the SERVICE STOPPED; the radio STILL UNPLUGGED) → THE STOP-GATE that replaces SD-5

**Why the gate exists:** `ZigbeeIntegrationAdapter.resumeOrForm()` FORMS A NEW NETWORK whenever `parameterStore.load()` is empty — an incomplete clone + a visible coordinator = the bench network re-formed (new PAN, new key, six devices orphaned, hours of re-pairing). `load()` present ⇒ resume-or-PIE, never form (`formation.resume()` throws on key-missing/NVRAM mismatch — it never re-forms silently). Clones travel ONE direction only: bench → held card, never back.

```bash
# WHERE: your desktop → the held card (hop 3 of 3 for the custody set).
cd ~/r3-rehearsal && scp -i ~/.ssh/id_ed25519_pi zigbee-custody-for-r3.tar.gz bench-config-for-r3.tar.gz 99-zigbee-coordinator.rules nick@hs-fresh.local: && ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local 'cd ~ && sha256sum zigbee-custody-for-r3.tar.gz bench-config-for-r3.tar.gz 99-zigbee-coordinator.rules'
# expect: the same three hashes as the bench AND the desktop. ⏺. A mismatch → re-copy; do not lay down a mismatched tarball.
```

```bash
# WHERE: the held card, as nick. Service STOPPED; the card's OWN radio-less custody moved ASIDE (F-S11 — delete nothing); the clone laid down; ownership + modes set.
sudo systemctl stop homesynapse.service && systemctl is-active homesynapse.service
# expect: `inactive`
sudo mv /var/lib/homesynapse/data/zigbee /var/lib/homesynapse/data/zigbee.held-pre-r3-2026-08-29 && sudo ls -la /var/lib/homesynapse/data/ /var/lib/homesynapse/data/zigbee.held-pre-r3-2026-08-29/
# expect: NO `zigbee/` under data/ any more; the aside dir listed (⏺ — the held card's own state before the clone, kept whole)
sudo tar xzf ~/zigbee-custody-for-r3.tar.gz -C /var/lib/homesynapse/data && sudo tar xzf ~/bench-config-for-r3.tar.gz -C /var/lib/homesynapse/config
sudo chown -R homesynapse:homesynapse /var/lib/homesynapse/data/zigbee /var/lib/homesynapse/config/homesynapse.yaml /var/lib/homesynapse/config/integrations && sudo chmod 0700 /var/lib/homesynapse/data/zigbee /var/lib/homesynapse/config/integrations && sudo chmod 0400 /var/lib/homesynapse/data/zigbee/.root-key && sudo chmod 0600 /var/lib/homesynapse/data/zigbee/scope_keys.json /var/lib/homesynapse/data/zigbee/secrets.enc /var/lib/homesynapse/data/zigbee/zigbee-network.json /var/lib/homesynapse/data/zigbee/zigbee-devices.json /var/lib/homesynapse/config/homesynapse.yaml /var/lib/homesynapse/config/integrations/zigbee.yaml
sudo cp ~/99-zigbee-coordinator.rules /etc/udev/rules.d/ && sudo udevadm control --reload && echo "udev reloaded"
# expect: no error · `udev reloaded`. (The /dev/zigbee symlink appears only when the dongle is plugged — §8. The token pair, home_id and schemas/ are the held card's OWN — untouched, by construction of the two tar lists.)
```

```bash
# STOP-GATE §6 (THE CLONE GATE — run it, ⏺ it, read it before §7): the clone must be COMPLETE, or the packaged adapter FORMS a new network the moment it sees the radio.
sudo python3 -m json.tool /var/lib/homesynapse/data/zigbee/zigbee-network.json && sudo ls -la /var/lib/homesynapse/data/zigbee/ && sudo sha256sum /var/lib/homesynapse/data/zigbee/secrets.enc /var/lib/homesynapse/data/zigbee/scope_keys.json && sudo grep -nE "serial_port|channel" /var/lib/homesynapse/config/integrations/zigbee.yaml
# expect: the JSON parses and names channel 20 + the bench's PAN (0x774c-class — read the field name as printed) · five files (six if the nonce counter travelled) with the BENCH-SIDE listing's byte sizes (32 / 248 / 568 / 122 / the LIVE cache size from §1), owned homesynapse, `.root-key` 0400 · the two hashes ⏺ · `serial_port: /dev/zigbee` + `channel: 20` (inert on resume). ANY missing/unparseable file = STOP. Do not plug the coordinator. Do not start the service.
```

---

## §7 A-1 — the drop-in (the candidate loosening — measured, never assumed)

```bash
# WHERE: the held card, as nick. The MEASUREMENT instrument; R-3b ships whatever text this measures (H13); it is removed before R-4.
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
# expect: the drop-in's five lines below the unit. ⏺ the tail. Rationale pinned: `char-ttyUSB`/`char-ttyACM` are the /proc/devices class names (majors 188/166) — class rules survive replug renumbering where a node path would not; `DevicePolicy=closed` keeps only the standard pseudo-devices; `SupplementaryGroups=dialout` matches the node's root:dialout 0660. Candidate ONLY — if §9 demands more, the MEASURED text wins.
```

---

## §8 The coordinator PLUG (the fence lifts HERE and only here — after the §6 gate)

```bash
# WHERE: physical, then the held card. Plug the SONOFF dongle back into hub 3-2.4 Port 2 (the same port — F-S20's byte-identical identity depends on it). ⏺ "plugged HH:MM ET". Then:
sleep 3; sudo udevadm trigger && sleep 2 && lsusb | grep -i "10c4:ea60"; ls -l /dev/zigbee /dev/ttyUSB0; ls -l /dev/serial/by-id/ | grep -i sonoff; id homesynapse
# expect: the CP210x/SONOFF line · `/dev/zigbee -> ttyUSB0` · the node `root dialout` 0660 (`crw-rw----`) · `usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0` · the homesynapse user's groups (⏺ — the drop-in's SupplementaryGroups adds dialout at exec, so `dialout` need NOT appear here). ⏺ all.
```

```bash
# STOP-GATE §8: /dev/zigbee resolves to a root:dialout 0660 node AND the by-id name is the SONOFF string above. Otherwise STOP, paste (a different by-id string = a different dongle or port; the symlink absent = the udev rule did not take — `sudo udevadm control --reload; sudo udevadm trigger` once more, then STOP if still absent).
```

---

## §9 A-3 — the measured boot (the discriminator set; predictions filed in the head)

```bash
# WHERE: the held card, as nick. Start, then read the journal for the discriminator tokens after ~60 s.
sudo systemctl start homesynapse.service; sleep 60; systemctl is-active homesynapse.service; sudo journalctl -u homesynapse.service -b --no-pager | grep -E "zigbee\.(port_identity_captured|transport_override|network_resumed|network_formed|network_parameter_mismatch|transport_unbound|transport_unsupported|transport_failed|device_cache_loaded|adopt_list_loaded|adoption_maps_rehydrated|device_relinked|device_proposed|proposal_accepted|device_adopted|device_announce)|registry\.projection_live|EPERM|Permission denied|SerialPort|ASH|NETWORK_UP" | head -40
# expect (P-a): `active` · `zigbee.port_identity_captured: stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false` then `zigbee.network_resumed: channel=20 panId=0x774c` = the loosening is SUFFICIENT. The fleet arm is a paste-either-way (tokens pinned at source, `integration-zigbee`): P-g `zigbee.device_cache_loaded` → `zigbee.adoption_maps_rehydrated: devices=6` → `zigbee.device_relinked` ×6 (the bench-identical boot path — the cloned cache carries the identities) · P-e `zigbee.device_proposed` → `zigbee.proposal_accepted` → `zigbee.device_adopted` (the registry is empty on this card; the cloned `adopt_list_loaded` auto-adopts) · P-f nothing until `zigbee.device_announce`. ⏺ the whole output either way. If NEITHER `network_resumed` nor any failure token has appeared yet, re-run the journal line once at +60 s (the bench lands the P-a pair within ~30 s of start; a packaged first boot under the drop-in may be slower) — then read the arms. (`zigbee.network_parameter_mismatch` = the custody/NVRAM PIE — the honest failure, never a re-form: STOP, paste.)
```

```bash
# STOP-GATE §9 — read the journal against the arms BEFORE anything else:
#   P-d  `zigbee.network_formed`  → POWER OFF THE PI AT ONCE (pull the plug; not shutdown). ⏺. STOP. The hub adjudicates (the §6 gate should make this impossible; if it fired, the bench's own custody still resumes ITS parameters on the bench card, and the recovery path is the hub's to write).
#   P-b  `zigbee.transport_unbound` → the class rule or the group did not take: ⏺ `ls -la /dev/ttyUSB0`, `id homesynapse`, `systemctl show -p DeviceAllow -p SupplementaryGroups homesynapse.service`, `sudo journalctl -u homesynapse.service -b --no-pager | grep -iE "zigbee|serial" | tail -20`. STOP, paste — the hub writes the next drop-in line (one hypothesis per line, re-measured, each ⏺'d).
#   P-c  `Permission denied` / `EPERM` with the node visible → the syscall filter or the group: the same four ⏺s. STOP, paste.
#   P-a  `network_resumed` → CONTINUE to §10.
```

---

## §10 A-4 — the evidence window (≥30 min; the R-4 dress rehearsal)

```bash
# WHERE: the held card. ROWS-W0 + the fleet re-adoption arm (P-e vs P-f) at +2 min.
sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'; date -u +%H:%M:%SZ; sudo journalctl -u homesynapse.service -b --no-pager | grep -oE "zigbee\.(device_relinked|device_proposed|proposal_accepted|device_adopted|device_announce)" | sort | uniq -c
# ⏺ ROWS-W0 + the time (Z) + the token counts. P-g: `device_relinked` ×6 (the cloned cache carried the identities) · P-e: `device_proposed`/`proposal_accepted`/`device_adopted` (entities appear as they are adopted) · P-f: nothing until `device_announce` — then a single power-cycle of the motion sensor is the probe. ⏺ which arm fired.
```

```bash
# WHERE: your desktop, a SECOND Git Bash: the tunnel; then the browser at http://127.0.0.1:7070/ — the token via `sudo homesynapse-token` ON THE CARD'S TERMINAL ONLY (never into this record).
ssh -L 7070:127.0.0.1:7070 -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local
# In the dashboard (⏺ each in prose, with the ET/Z time): the Devices list shows the fleet with honest availability (expect 5 Available + 1 Unavailable, each with a fresh `Last reported`) → walk the motion sensor (one wave, then STAND STILL — occupancy holds defeat scripted waves) → bench-hero fires on the packaged path → the explain surface renders "why did it fire?" for that run. If no device shows Available after 5 min: ⏺ the Devices list as shown; power-cycle the motion sensor ONCE (P-f); ⏺ again at +2 min.
```

```bash
# WHERE: the held card, at ≥30 min after ROWS-W0. The window close: the row delta, the throw discriminator, the transport health.
sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'; date -u +%H:%M:%SZ; sudo journalctl -u homesynapse.service -b --no-pager | grep -ciE "NoClassDefFoundError|jdk.jfr|BusMetrics"; sudo journalctl -u homesynapse.service -b --no-pager | grep -E "zigbee\.(transport_failed|network_resumed|network_formed)" | tail -5; curl -s -H "Authorization: Bearer $(sudo homesynapse-token)" http://127.0.0.1:7070/api/v1/runs | head -c 1200; echo
# expect: ROWS-W1 > ROWS-W0 (the delta is integration-attributable — no other publisher runs on this card) · `0` · exactly one `network_resumed`, ZERO `network_formed`, ZERO `transport_failed` · the runs surface (the same read `~/bench.sh runs` does on the bench; `sudo homesynapse-token` with no verb prints the pairing token INTO the substitution only — the output is the runs JSON, never the token) showing ≥1 run of bench-hero. ⏺ all five — the runs JSON as printed (it carries no token). (A `transport_failed … retransmits=0 crcRejects=0 timeouts=0` line = a physical port loss (F-S16's signature) — ⏺ and check the dongle seat.)
```

```bash
# STOP-GATE §10 — the R-4 lift criteria, rehearsed (H9; nothing lifts today): (1) `network_resumed` · (2) ≥1 device Available with a fresh Last reported · (3) ROWS-W1 > ROWS-W0 + discriminator 0 · (4) one automation run with a rendered explanation. Each is a paste-either-way; a miss on (2)/(4) does not stop §11.
```

---

## §11 A-5 — the restore (the bench back before 03:00 CT = 04:00 ET; `~/bench.sh start` is LAW — F-S15)

```bash
# WHERE: the held card. Normal shutdown. The drop-in STAYS on the held card until R-3b's artifact is installed there (then it is `mv`'d aside so R-4 measures the shipped unit alone). The coordinator STAYS PLUGGED (the bench card resumes on it).
sudo systemctl stop homesynapse.service && systemctl is-active homesynapse.service; sudo shutdown -h now
# expect: `inactive` · then the ACT LED stops → power OFF → held card OUT (re-label: `hs-fresh — R-3/R-4 rig — +git dec35be · drop-in ON · bench custody CLONED 2026-08-29`) → bench card IN → power ON → wait ~90 s.
```

```bash
# WHERE: the bench card (ssh pi). F-S15: the bench app has NO systemd unit — nothing starts it before the 04:30 ET nightly. START IT, then the floor.
~/bench.sh status; ~/bench.sh start; sleep 45; ~/bench.sh status; ls -l /dev/zigbee; lsusb | grep -i "10c4:ea60"
# expect: `[!!] NOT running` first (the F-S15 proof) · a start line (`RADIO UP after 12–18 s` — 18 s after a long unplug is F-S17's known first-enumeration, not a shifted baseline) · running · `/dev/zigbee -> ttyUSB0` · the SONOFF line. ⏺ all.
~/bench.sh scenario boot-health
# expect: `[PASS] boot-health — 6/6 positive · 0 forbidden` (radio up ≤ ~18 s; 6/6 relinked). ⏺ the verdict line + the `zigbee.network_resumed: channel=20 panId=0x774c` line from its boot log. A CHANGED PAN here = STOP, ⏺, the hub adjudicates (the bench must never re-form).
grep -E "zigbee\.(port_identity_captured|network_resumed)" ~/hs-bench/current.log | tail -2
# expect (F-S20): `stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false` byte-identical + `zigbee.network_resumed: channel=20 panId=0x774c`. ⏺ both. (`~/hs-bench/current.log` is `bench.sh`'s current boot log — `tools/bench.sh:9`; `~/bench.sh log` reads the same file.)
```

```bash
# STOP-GATE §11 (the day's exit): bench running · `[PASS] boot-health 6/6 · 0 forbidden` · PAN 0x774c · the by-id string identical · the held card OUT and re-labeled. The nightly at 04:30 ET then runs on its own; its digest line is the morning's ⏺.
```

---

## §12 What the hub banks (one line each, law 16 form) + the record

E3-RED: the Z timestamps + `token not yet available` + `TIMEOUT after 90s` + the failed/activating state (the class on hardware) · Block I: `0.1.0+git20260823.231355.gdec35be` (dpkg == image), the hash chain (CI log → desktop → card), ROWS-AFTER ≥ ROWS-BEFORE + integrity ok + home_id stable, `--allow-downgrades` used ONCE · E3-GREEN: `ready (200) … /health` with the artifact absent, `200/401`, restart in seconds — OR-E3-PROBE CLOSES · §6: the clone gate's listing + hashes · §9: which arm fired (P-a/b/c) + the measured drop-in text = R-3b's spec · §10: the four R-4 criteria rehearsed (each MET/MISS) · §11: `[PASS]`, the PAN, the by-id string. **R-4's lift language does not change today** (R-4 owns the lift; the D-1 pair stays DO-NOT-SAY until R-4's return is on disk + audited).

**⏺ RECORD — paste-either-way.** Paste the ⏺s in packet order under the section numbers, every timestamp ET or Z, every hash whole, no token VALUE anywhere (paths only). Deviations (a step skipped, a block re-run, a line re-typed) get their own list at the end. The hub files the record at `context/audits/2026-08-29_R3a_rehearsal_operator-record.md` (dated by the filing day) and authors R-3b from §9's measured text the same evening.
