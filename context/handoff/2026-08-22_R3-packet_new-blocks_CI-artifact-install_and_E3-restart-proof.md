<!--
file: context/handoff/2026-08-22_R3-packet_new-blocks_CI-artifact-install_and_E3-restart-proof.md
purpose: the TWO NEW BLOCKS the R-3/PKG-E2E-1 packet gains at its finalization (v55 beat 6 ruling (6); the R-7 audit §4; the R-6/R-8 audit H-1). Authored AHEAD of the Saturday ⏺s so the finalization pass is a fold, not an authoring act: **Block E3 — the packaged-unit artifact-absent restart proof** (RED on the held card's `7c9e4fa` artifact, GREEN on the first CI-built artifact carrying R-9 — the H7 measured-then-green pair; R-9's hardware close; the INTERIM OPERATOR LAW retires on its GREEN + §OP-H) and **Block I — the CI-built arm64 `.deb` as the install source** (post-R-7b; `--allow-downgrades` exactly ONCE per `7c9e4fa` card; hashed on every hop; the R-7b FENCE as a STOP-gate). Both blocks are self-contained (the operator-packet class, arc-35) and slot into the R-3a packet BEFORE A-1 (E3-RED → I → E3-GREEN → A-1…).
audience: the hub (the fold at finalization) · Nick (the operator, on the held card `hs-fresh`).
status: AUTHORED-AHEAD (v56 beat 1). Three [⏺-GROUNDED] slots remain — the post-Block-2 held-card state (today's ⏺s), the R-7b/R-9 landing SHAs, and the install-smoke run id that built the artifact — filled at finalization. NOT an operator dispatch until folded.
fences honoured: R-7b BEFORE R-3b installs any CI artifact (the Version-shape STOP-gate in Block I enforces it at the instrument) · the INTERIM OPERATOR LAW holds on the held card until Block E3-GREEN passes (the RED arm is the ONE sanctioned breach, bounded to ≤ 3 min and restored in the same block) · delete NOTHING (the artifact is `mv`'d aside and back) · the D-1 DO-NOT-SAY pair is untouched by either block.
-->

# R-3 packet — the two new blocks (Block E3 · Block I)

**Where they slot.** R-3a opens with **E3-RED** (on the card's current `7c9e4fa` artifact — the instrument proves it can SEE the class) → **Block I** (the CI artifact installs; the card moves onto the `+git` scheme, `--allow-downgrades` once) → **E3-GREEN** (the same restart with the artifact absent now succeeds on `/health`) → the existing A-1/A-2/STOP/A-3/A-4/A-5. Every ⏺ line is a paste-either-way.

**Instrument semantics (derived from the artifact, H12).** `homesynapse.service` is `Type=exec` · `ExecStartPost=/opt/homesynapse/libexec/health-probe.sh --wait --timeout 90` · `Restart=on-failure` · `RestartSec=10` · `StartLimitIntervalSec=300` / `StartLimitBurst=5`. On the `7c9e4fa` artifact the probe targets `/api/v1/entities` (auth-gated) and reads `/var/lib/homesynapse/config/initial_api_token` ONCE per attempt (`health-probe.sh :85–:93`); with the file absent it logs `[health-probe] token not yet available at /var/lib/homesynapse/config/initial_api_token` every 2 s, then `[health-probe] TIMEOUT after 90s — service did not become ready` and exits 1 → the unit FAILS although the app is up → `Restart=` retries → start-limited after 5. On the R-9 artifact the probe targets `/health` (no token: `NEEDS_AUTH=0`) and logs `[health-probe] ready (200) at http://127.0.0.1:7070/health`. Journal identifier: `homesynapse`.

---

## Block E3-RED — the class, measured on the `7c9e4fa` artifact (≤ 3 min; ONE sanctioned breach of the interim law, restored in-block)

**Goal:** prove on real hardware that the packaged unit's readiness DEPENDS on the pairing artifact (the availability class the R-6/R-8 audit named). **Done-when:** the journal shows `token not yet available` lines during a restart with the artifact moved aside, then the artifact is back and the unit is `active`.

```bash
# WHERE: the held card, as nick (ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local). Precondition glance — the card's CURRENT state.
dpkg-query -W -f '${Version}\n' homesynapse; systemctl is-active homesynapse.service; sudo ls -la /var/lib/homesynapse/config/initial_api_token; sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'
# expect: 7c9e4fa · active · -rw------- homesynapse homesynapse (the artifact PRESENT) · a row count (⏺ it — the baseline for Block I's preservation glance)
# [⏺-GROUNDED: today's Block-2/3 ⏺s fix the expected version + artifact presence; if the artifact is ABSENT here, skip E3-RED — the class cannot be measured without a baseline — and paste]
```

```bash
# STOP-GATE E3-RED-0 (read before the next block): the unit is `active` AND the artifact is PRESENT. Anything else → STOP, paste, do not continue.
```

```bash
# WHERE: the held card. The RED arm: artifact aside (mv, never rm) → restart → watch the probe → stop → restore. Hard clock bound: 3 minutes from the restart line.
sudo mv /var/lib/homesynapse/config/initial_api_token /var/lib/homesynapse/config/initial_api_token.e3red && date -u +%H:%M:%S && sudo systemctl restart homesynapse.service; echo "restart rc=$?"; date -u +%H:%M:%S
# expect: ~90 s wall-clock (the probe burns its --timeout 90), then `restart rc=1` (ExecStartPost failed → the unit failed). ⏺ both timestamps + the rc.
systemctl is-active homesynapse.service; systemctl show -p NRestarts -p Result -p ExecMainStatus homesynapse.service
# expect: `activating` (auto-restart pending, RestartSec=10) or `failed`; Result=exit-code-class; ⏺ the three lines
sudo journalctl -u homesynapse.service -b --no-pager --since "-4min" | grep -E "health-probe|Started|Failed|Scheduled restart|start-limit" | tail -20
# expect: ≥1 `[health-probe] token not yet available at /var/lib/homesynapse/config/initial_api_token`, then `[health-probe] TIMEOUT after 90s — service did not become ready`, then a `Failed to start` / `Scheduled restart job` pair. ⏺ the tail. (A `ready (200)` line here = the REFUTATION: the 7c9e4fa probe does not need the token — STOP, paste; the hub re-derives.)
```

```bash
# WHERE: the held card. RESTORE — the interim law is back in force after this line.
sudo systemctl stop homesynapse.service; sudo mv /var/lib/homesynapse/config/initial_api_token.e3red /var/lib/homesynapse/config/initial_api_token && sudo ls -la /var/lib/homesynapse/config/initial_api_token && sudo systemctl reset-failed homesynapse.service && sudo systemctl start homesynapse.service && sleep 15 && systemctl is-active homesynapse.service && sudo journalctl -u homesynapse.service -b --no-pager --since "-1min" | grep -E "health-probe" | tail -3
# expect: the artifact back, -rw------- · active · `[health-probe] ready (200) at http://127.0.0.1:7070/api/v1/entities`. ⏺ all three. (Not active after 60 s → `sudo systemctl status homesynapse.service --no-pager -l` ⏺, STOP, paste.)
```

---

## Block I — the CI-built arm64 `.deb` as the install source (post-R-7b; `--allow-downgrades` ONCE)

**Goal:** the held card runs the first CI-built artifact (R-9 + R-7b inside), installed through the artifact channel R-7 built, hash-verified on every hop, the event store preserved. **Done-when:** `dpkg-query` prints a `0.1.0+git<YYYYMMDD.HHMMSS>.g<sha>` version, the unit is `active`, the row count is unchanged, the journal discriminator is 0.

**I-1 Fetch (desktop, Git Bash + the browser; `gh` is not assumed on the desktop — it is ABSENT on the Pi).** [⏺-GROUNDED at finalization: the install-smoke run id of the commit that carries BOTH R-9 and R-7b — the hub names it and its echo-step line `hs_version=0.1.0+git….g<sha>`; the run page URL is `https://github.com/nexsys-io/homesynapse-core/actions/runs/<run-id>`.]

```bash
# WHERE: your desktop, Git Bash. Browser first: the run page → Artifacts → `distribution-artifacts-arm64` → the zip lands in ~/Downloads.
mkdir -p ~/Desktop/r3-artifact && cd ~/Desktop/r3-artifact && powershell.exe -NoProfile -Command "Expand-Archive -LiteralPath \"$(cygpath -w ~/Downloads/distribution-artifacts-arm64.zip)\" -DestinationPath \"$(cygpath -w ~/Desktop/r3-artifact)\" -Force" && ls -la && sha256sum homesynapse_*_arm64.deb
# expect: ONE .deb named homesynapse_0.1.0+git<YYYYMMDD.HHMMSS>.g<sha>_arm64.deb (≈ 61.8 MB) + one .tar.gz; ⏺ the .deb hash — it must EQUAL the `sha256` line the echo step printed on the run page (R-7b adds it; if the step shows no hash, R-7b's artifact is not what you downloaded — STOP).
# (gh path, if `gh` is installed: gh run download <run-id> --repo nexsys-io/homesynapse-core -n distribution-artifacts-arm64 -D ~/Desktop/r3-artifact — then the same sha256sum.)
```

```bash
# STOP-GATE I-0 — THE R-7b FENCE, at the instrument. Run on the desktop. The Version field must carry the `+git<date>.g<sha>` scheme; a `0.1.0+g<sha>` (no `git`) artifact is PRE-R-7b and must NOT reach the card.
dpkg-deb --field ~/Desktop/r3-artifact/homesynapse_*_arm64.deb Version Architecture 2>/dev/null || echo "no dpkg-deb on this desktop — run the same line on the card after scp, BEFORE apt"
# expect: Version: 0.1.0+git<8 digits>.<6 digits>.g<sha>  ·  Architecture: arm64.  Anything else → STOP, paste. (Git Bash has no dpkg-deb: the card gate below is the one that binds.)
```

**I-2 Copy + the card-side gate.**

```bash
# WHERE: your desktop → the held card.
cd ~/Desktop/r3-artifact && scp -i ~/.ssh/id_ed25519_pi homesynapse_*_arm64.deb nick@hs-fresh.local: && ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local 'sha256sum ~/homesynapse_*_arm64.deb; dpkg-deb --field ~/homesynapse_*_arm64.deb Version Architecture'
# expect: the SAME hash as the desktop · Version 0.1.0+git<date>.g<sha> · Architecture arm64. ⏺ all three lines.
```

```bash
# STOP-GATE I-1: hash equal on both hops AND Version matches ^0\.1\.0\+git[0-9]{8}\.[0-9]{6}\.g[0-9a-f]{7,}(-dirty)?$ AND Architecture=arm64. A `-dirty` suffix = a dirty CI tree, impossible by construction → STOP, paste. Any mismatch → STOP, paste, do not install.
```

**I-3 Install — `--allow-downgrades` exactly ONCE on this card (its `7c9e4fa` bare id sorts ABOVE every `0.1.0+…`; after this install no later `+git` build ever needs the flag — the scheme is monotone by commit time).**

```bash
# WHERE: the held card, as nick. Baseline, install, verify. The interim law holds throughout (no token verbs).
sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;' && dpkg-query -W -f '${Version}\n' homesynapse
# ⏺ both — the PRE row count (must equal E3-RED's baseline) and the PRE version (7c9e4fa)
sudo apt install -y --allow-downgrades ~/homesynapse_*_arm64.deb 2>&1 | tail -15
# expect: a `Downgrading homesynapse from 7c9e4fa to 0.1.0+git…` (or dpkg's "downgrading" warning) line, postinst output, no error. ⏺ the tail.
dpkg-query -W -f '${Version}\n' homesynapse; cat /opt/homesynapse/VERSION; systemctl is-active homesynapse.service; systemctl cat homesynapse.service | grep -E '^ExecStartPost'
# expect: the +git version (twice — dpkg and the image stamp, EQUAL) · active · `ExecStartPost=/opt/homesynapse/libexec/health-probe.sh --wait --timeout 90 --health-path /health` (R-9's unit). ⏺ all four.
sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'; sudo journalctl -u homesynapse.service -b --no-pager | grep -ciE "NoClassDefFoundError|jdk.jfr|BusMetrics"; sudo journalctl -u homesynapse.service -b --no-pager --since "-3min" | grep -E "health-probe" | tail -3
# expect: the row count UNCHANGED (the upgrade preserves the store — the same instrument as update-smoke's assertion, third rig) · 0 · `[health-probe] ready (200) at http://127.0.0.1:7070/health`. ⏺ all three.
```

```bash
# STOP-GATE I-2: Version is the +git scheme in BOTH places · active · the probe's ready line names /health · rows unchanged · discriminator 0. Any miss → `sudo systemctl status homesynapse.service --no-pager -l` ⏺, STOP, paste. (A second `--allow-downgrades` is NEVER needed on this card from here on — if a later install asks for it, that is a finding, not a flag to add.)
```

---

## Block E3-GREEN — the same restart, artifact absent, on the R-9 artifact (≤ 2 min; the H8 hardware close)

**Goal:** the packaged unit restarts to `active` with the pairing artifact ABSENT, because the probe reads `/health`. **Done-when:** `ready (200) at …/health` in the journal with the artifact moved aside, `active`, then the artifact restored (A-4's pairing reads it).

```bash
# WHERE: the held card, as nick. The GREEN arm — the same verbs as E3-RED, the opposite prediction.
sudo mv /var/lib/homesynapse/config/initial_api_token /var/lib/homesynapse/config/initial_api_token.e3green && date -u +%H:%M:%S && sudo systemctl restart homesynapse.service; echo "restart rc=$?"; date -u +%H:%M:%S
# expect: the restart returns in SECONDS (not 90), `restart rc=0`. ⏺ the timestamps + rc.
systemctl is-active homesynapse.service; systemctl show -p NRestarts -p Result homesynapse.service; sudo journalctl -u homesynapse.service -b --no-pager --since "-2min" | grep -E "health-probe|Started" | tail -5
# expect: active · NRestarts=0 Result=success · `[health-probe] ready (200) at http://127.0.0.1:7070/health` + `Started homesynapse.service`. NO `token not yet available` line. ⏺ all. (`token not yet available` here = the unit on the card is NOT R-9's — STOP, paste: check `systemctl cat` for `--health-path /health`.)
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:7070/health;   # curl: installed by today's Block 2
 curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:7070/api/v1/entities
# expect: 200 then 401 — the fence proof on hardware (unauthenticated /health open; the API still gated). ⏺ both.
sudo mv /var/lib/homesynapse/config/initial_api_token.e3green /var/lib/homesynapse/config/initial_api_token && sudo ls -la /var/lib/homesynapse/config/initial_api_token && systemctl is-active homesynapse.service
# expect: the artifact back, -rw------- · active (a restore needs no restart — the store, not the file, is the key's home). ⏺.
```

```bash
# STOP-GATE E3-GREEN: active with the artifact absent · ready-line names /health · 200/401 pair · artifact restored. All four → the E3 class is CLOSED ON HARDWARE; the INTERIM OPERATOR LAW retires at the hub's next beat (with §OP-H already banked). Any miss → STOP, paste; do not proceed to A-1.
```

**What the hub banks from these three blocks (one line each, law 16 form):** E3-RED: the timestamps + `token not yet available` + `TIMEOUT after 90s` + the failed/activating state (the class on hardware) · Block I: the `+git` version (dpkg == image), the hash chain (CI-log → desktop → card), rows unchanged, `--allow-downgrades` used ONCE · E3-GREEN: `ready (200) … /health` with the artifact absent, `200/401`, restart in seconds. The R-4 lift language does not change (R-4 owns the lift); these blocks close R-9 (H8) and retire the interim law and the `--allow-downgrades` line forever on this card.
