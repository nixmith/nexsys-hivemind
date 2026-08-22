<!--
file: context/handoff/2026-08-21_card-sitting_operator-packet.md
purpose: THE SATURDAY CARD-SITTING PACKET (Sat 2026-08-22) — the R-1/R-2 hardware-evidence legs (RED on the held card → GREEN on the rebuilt artifact → restore) + THE TOKEN ROTATION BLOCK. This packet SUPERSEDES the R1R2 instruction's §OP Block 2 (OVERTAKEN at the hub, v55 beat 1 — the adjudication is §0 below); §OP Blocks 1 and 3 are carried here VERBATIM in substance with the ⏺ slots widened. Self-contained per the playbook §8 contract + arc-35 (a fresh session needs nothing but this file).
audience: Nick (operator, the ONLY hardware act of the weekend); the hub (the ⏺ intake — adjudicate-first against the predictions filed in §6; never improvise past a mismatch).
status: ISSUE-READY (v55 beat 1; AMENDED beat 3 — R-0 GO received: Block 0 runs TONIGHT (Fri) on the bench card, finished before ~02:30 CT; Blocks 1–3 Saturday in daylight. THE TOKEN ROTATION BLOCK IS RETIRED — it already ran 2026-08-20 22:06 Pi-time (the enrichment listing: `api_tokens.rotated-2026-08-20` beside a fresh `api_tokens` + `initial_api_token`); Block 3 now only CONFIRMS it at the listing). NEVER inside 03:00–04:15 CT (the nightly guard); a card swap spanning 03:30 CT fires the missed nightly on restore.
predictions: filed BEFORE the run, in §6 — derived from the ARTIFACTS at core 7c9e4fa (build-image.sh §2/§2b · run-smoke.sh checks 1–9 · debian/postinst · common.sh · the 9f99368 CI log's 16-module union), never from intent (H12).
audit: layer-2 adversarial review at the scripts (v55 beat 1, independent agent, hub-adjudicated): TWO root-cause defects found in the first draft and corrected here BEFORE any hardware act — (1) `build-deb.sh` SKIPS `build-image.sh` when a prior image tree exists (:36–:39), so the bench's stale `distribution/image/build/` would have repackaged the OLD runtime under the new version → Block 0 now moves the old tree aside and runs `build-image.sh` explicitly, with a STOP if no `[build-image]` lines print; (2) `hs_version` wraps a commit id as `0.1.0+g<id>` ONLY when it starts with a–f (`common.sh` :62–:65 — the `[0-9]*` arm prints it bare) → the version of record is `7c9e4fa`, not `0.1.0+g7c9e4fa`; every expected string below says so. Plus the L3 masking step (the initial mint WARN-logs the raw token into the journal — `OpaqueTokenStore.java` :214–:216).
instrument law: the probe pattern `NoClassDefFoundError|jdk.jfr|BusMetrics` is BYTE-IDENTICAL in Block 1, Block 2's discriminator, and run-smoke check 4 (H13 — one instrument, two rigs).
-->

# The Saturday Card Sitting — Operator Packet (R-1/R-2 evidence legs + the token rotation)

**Goal.** Three ⏺ pairs on real hardware: (1) **RED** — the held card's known-bad artifact (`0.1.0+gd26777c`) fails the write-path probe the way F-23 predicts; (2) **GREEN** — the artifact rebuilt from core `7c9e4fa` passes run-smoke checks 1–9 on the same card in a FRESH boot, write-path check 4 printing positive evidence; (3) **RESTORE** — the bench card back, `[PASS]` floor, and the token-rotation state CONFIRMED at the listing (the rotation itself already ran on 08-20 — the exposed token is DEAD; no second rotation). **Done-when:** every ⏺ slot in §6 is filled, pasted to the hub as TEXT (crop/mask any screenshot that shows an `Authorization` header — L3), and the hub has adjudicated the set.

**Cards and hosts (from the H3 record):** the BENCH card = `hs-dev-1`, user `homesynapse`, reached as `ssh pi` (your alias), carries the full toolchain + `~/homesynapse-core` (you pulled it to `7c9e4fa` on Fri 08-21 — that pull is Block 0's first act, already done). The HELD card = the H3 Stage-2 clean image, hostname `hs-fresh`, user `nick`, reached as `ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local` (the F-18 remedy; Ethernet — wlan0 is DOWN on it). **The held card has NO JDK, NO Gradle, NO repo checkout** — it is a clean Raspberry Pi OS Lite with the `.deb` installed. Everything it needs arrives by `scp` from your desktop. The coordinator NEVER attaches to the held card (SD-5). The bench card comes OUT only after a normal shutdown.

## §0 Why this packet supersedes §OP Block 2 (the hub's adjudication, filed before any hardware act)

The R1R2 instruction's §OP Block 2 reads *"same card … `cd ~/homesynapse-core && git pull` … `distribution/deb/build-deb.sh` … `sudo distribution/smoke/run-smoke.sh`"*. Two premises fail at the artifacts (and two more were found by the layer-2 audit — the frontmatter names them):

1. **The held card cannot build.** `build-image.sh` §0 dies without `JAVA_HOME` → a JDK 21 with `jlink`/`jdeps`, then runs `./gradlew --no-daemon :app:homesynapse-app:installDist` inside the repo. The held card is the clean image (H3 Stage-2: the artifact was *transferred* and `apt install`ed; no toolchain, no checkout). **The build runs on the BENCH card; the `.deb` + the `distribution/` tree travel to the held card by `scp`.**
2. **A same-boot GREEN would be a FALSE RED.** run-smoke check 4 probe 2 greps `journalctl -u homesynapse.service -b` — *this boot's* journal. On the held card, Block 1's RED lines (the old artifact's ≈6 throw signatures, emitted at THIS boot's service start) stay in the journal; the upgrade (prerm stop + `postinst` start) keeps the service inside the SAME boot. Probe 2 would count the OLD artifact's lines against the NEW artifact → check 4 FAILS on a fixed build. **The GREEN leg therefore runs in a FRESH boot: upgrade → `sudo reboot` → the discriminator grep (expect 0) → run-smoke.** (The journal on Pi OS Lite is volatile — the old boot's journal is lost at reboot — so Block 1 ALSO dumps the RED journal to a file first. Delete nothing.)

Also derived from the artifacts, so you are not surprised: run-smoke **check 1 installs** the `.deb` itself (an apt no-op when the same version is already installed), **check 8 stops** the service, **check 9 REMOVES the package** (data dir preserved — the event store and `config/api_tokens` survive). The card therefore ends run-smoke with NO package installed; Block 2's last act re-installs it so the held card stays R-3/R-4's rig with the fixed artifact running. `hs_version` resolves from `git describe` ONLY when `build-deb.sh` is invoked from the repo ROOT (cwd-relative `VERSION` lookup; the tracked `distribution/VERSION` = `0.1.0-skeleton` would win if you ran it from inside `distribution/` — verified at the git object) — hence the `cd ~/homesynapse-core` first, every time. **And the version string is `7c9e4fa` bare:** `common.sh`'s `case` wraps only a–f-leading ids as `0.1.0+g…` (the `0.1.0+gd26777c` precedent began with `d`); dpkg orders `7c9e4fa` ABOVE `0.1.0+gd26777c`, so Block 2 is a lawful upgrade — a finding for R-6's packaging batch (a future a–f-leading id would sort BELOW and apt would refuse it as a downgrade).

## §1 Block 0 — BUILD on the bench card (`ssh pi`; ~5–10 min; may run TONIGHT, Fri, any time outside 03:00–04:15 CT)

*Risk named (accepted at the hub):* Gradle `installDist` is the SAME output tree `bench.sh` runs the app from (`~/homesynapse-core/app/homesynapse-app/build/install/homesynapse-app/`). Zero Java/TS changed since the Thursday deploy built it (`c091f7c→7c9e4fa` = 4 scripts/YAML) ⇒ Gradle is UP-TO-DATE and rewrites nothing; the midweek deploy is the precedent for building with the app running. `build-deb.sh` does `rm -rf distribution/deb/build` — the old `.deb` there (if any) is COPIED aside first (delete-nothing).

```bash
# WHERE: the bench card, as homesynapse — `ssh pi`. One line at a time; ⏺ every output. Start early enough to finish before ~02:30 CT.
df -h / | tail -1
# expect: several GB free (two image trees + a .deb + a tarball land on this card tonight); under ~2 GB free = STOP, ⏺, paste
cd ~/homesynapse-core && git log --oneline -1 | cut -c1-60 && git --no-optional-locks status --porcelain | head -5
# expect: 7c9e4fa …  and an EMPTY porcelain (if lines appear, ⏺ them and continue — the filename may gain "-dirty"; nothing else changes)
ls -la ~/homesynapse-core/distribution/deb/build/ ~/homesynapse-core/distribution/image/build/ 2>/dev/null || echo "no prior build dirs"
# expect: listings or "no prior build dirs" — ⏺ either; the next two lines preserve whatever exists (delete nothing)
mkdir -p ~/artifacts && cp -p ~/homesynapse-core/distribution/deb/build/homesynapse_*_arm64.deb ~/artifacts/ 2>/dev/null; ls -la ~/artifacts/
[ -d ~/homesynapse-core/distribution/image/build ] && mv ~/homesynapse-core/distribution/image/build ~/artifacts/image-build.pre-7c9e4fa; ls -la ~/artifacts/
# WHY: build-deb.sh only runs build-image.sh when distribution/image/build/opt/homesynapse is ABSENT (build-deb.sh :36–:39) — a stale tree from the d26777c build would be repackaged under the new version with the OLD runtime inside. Moving it aside forces the real rebuild; nothing is deleted.
export JAVA_HOME="${JAVA_HOME:-$(dirname "$(dirname "$(readlink -f "$(command -v java)")")")}" && echo "JAVA_HOME=${JAVA_HOME}" && "${JAVA_HOME}/bin/jlink" --version
# expect: a path ending in a JDK dir and a jlink version line starting 21. (anything else = STOP, ⏺, paste)
```

**STOP-GATE 0 — do not continue unless the jlink version line printed.**

```bash
# WHERE: the bench card, same session. The build, in two explicit steps: the image (Gradle UP-TO-DATE expected, jdeps over all 55 jars, jlink, the 2b assert), then the .deb.
cd ~/homesynapse-core && distribution/image/build-image.sh 2>&1 | tee ~/block0-build-deb.log
cd ~/homesynapse-core && distribution/deb/build-deb.sh 2>&1 | tee -a ~/block0-build-deb.log
```

**⏺ RECORD from the build log (grep them out after both steps finish):**

```bash
grep -E "\[build-image\] (version=|bundled |jlink --add-modules|floor-presence assert|jlinked runtime)|\[build-deb\] building|ERROR" ~/block0-build-deb.log
```

Expected SIX lines (derived from the scripts + the `9f99368` CI log — §6 P-0): `[build-image] version=7c9e4fa arch=arm64 jdk=21` · `[build-image] bundled 55 jars` · `[build-image] jlink --add-modules java.base,java.desktop,java.instrument,java.logging,java.management,java.naming,java.net.http,java.security.jgss,java.sql,java.xml,jdk.crypto.cryptoki,jdk.crypto.ec,jdk.jfr,jdk.management,jdk.unsupported,jdk.zipfs` (**16 modules, `jdk.jfr` present, NO `Warning` token**) · `[build-image] jlinked runtime → <size>` · `[build-image] floor-presence assert green: all 16 requested modules present in the runtime` · `[build-deb] building /home/homesynapse/homesynapse-core/distribution/deb/build/homesynapse_7c9e4fa_arm64.deb (Installed-Size=<n> KB)`. **If the grep prints NO `[build-image]` lines at all, STOP — the image was not rebuilt (the stale-tree class); paste.** Any `ERROR` line = ⏺ verbatim, STOP, paste — the hub adjudicates (a Pi-side build red is a FINDING; never retune). A `-dirty` suffix on the version (a dirty bench checkout) also appears in the dpkg `Version:` later — ⏺ it; it changes nothing else.

```bash
# WHERE: the bench card. Fix the artifact's name + hash and package the distribution tree (LF-clean, made on Linux — never from the Windows checkout).
cp -p ~/homesynapse-core/distribution/deb/build/homesynapse_*_arm64.deb ~/homesynapse_7c9e4fa_arm64.deb && ls -la ~/homesynapse_7c9e4fa_arm64.deb
cd ~/homesynapse-core && git archive --format=tar.gz -o ~/dist-7c9e4fa.tar.gz HEAD distribution && ls -la ~/dist-7c9e4fa.tar.gz
sha256sum ~/homesynapse_7c9e4fa_arm64.deb ~/dist-7c9e4fa.tar.gz
# ⏺ both hashes — they are re-checked on every hop
```

```bash
# WHERE: your desktop, Git Bash. Pull both files down; re-hash.
mkdir -p ~/Desktop/card-sitting-2026-08-22 && cd ~/Desktop/card-sitting-2026-08-22
scp pi:homesynapse_7c9e4fa_arm64.deb pi:dist-7c9e4fa.tar.gz .
sha256sum homesynapse_7c9e4fa_arm64.deb dist-7c9e4fa.tar.gz
# expect: the SAME two hashes as on the bench card (a mismatch = STOP, re-copy)
```

Block 0 is complete when both files sit on the desktop with matching hashes. The bench keeps running throughout — no restart.

## §2 Block 1 — RED on the held card (change NOTHING before the probes)

Normal shutdown of the bench Pi (`ssh pi 'sudo shutdown -h now'`, wait for the LEDs), bench card OUT, held card IN, power on, wait ~90 s, then:

```bash
# WHERE: your desktop. Push the artifact + tree to the held card FIRST (network check), then probe.
cd ~/Desktop/card-sitting-2026-08-22 && scp -i ~/.ssh/id_ed25519_pi homesynapse_7c9e4fa_arm64.deb dist-7c9e4fa.tar.gz nick@hs-fresh.local:
ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local
```

```bash
# WHERE: the held card, as nick. The RED probes — the artifact INSTALLED here is still 0.1.0+gd26777c; touch nothing else first.
dpkg -s homesynapse | grep -E "^(Status|Version):"
# expect: Status: install ok installed · Version: 0.1.0+gd26777c   (a different version = STOP — the rig is not what the record says)
systemctl status homesynapse.service --no-pager | head -12
sudo ls -la /var/lib/homesynapse/data/ /var/lib/homesynapse/config/
# expect: homesynapse-events.db under data/ ; api_tokens AND initial_api_token under config/ — ⏺ EXACTLY what is there: run-smoke checks 3 and 5 read initial_api_token, and Block 2 has a one-line remedy if it is absent (the H3 banner told the operator to delete it after pairing)
command -v sqlite3 >/dev/null || (sudo apt-get update && sudo apt-get install -y sqlite3)
sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'
sudo journalctl -u homesynapse.service -b --no-pager | grep -ciE "NoClassDefFoundError|jdk.jfr|BusMetrics"
sudo journalctl -u homesynapse.service -b --no-pager | grep -iE "NoClassDefFoundError|jdk.jfr|BusMetrics" | head -5
sudo journalctl -u homesynapse.service -b --no-pager > ~/block1-red-journal.txt; wc -l ~/block1-red-journal.txt
```

**⏺ RECORD every line.** The prediction (§6 P-1, filed 2026-08-20/21): rows PRESENT (count ≥ 1 — persist precedes notify) **AND** a throw-signature LINE count ≥ 6 — `grep -c` counts lines, and each of the ≈6 throws contributes at least two matching lines (`NoClassDefFoundError: jdk/jfr/Event` + `Caused by: … ClassNotFoundException: jdk.jfr.Event`) plus any `BusMetrics` stack frames, so a count like 12–24 is the EXPECTED shape, not a deviation — with `NoClassDefFoundError: jdk/jfr/Event` lines in the head. **Either red proves the class. BOTH clean (rows ≥ 1 AND count 0) = F-23's upper bound REFUTED at the instrument → STOP at this block, ⏺, paste — the hub adjudicates before ANY further act (a finding, not a failure).** A zero/absent row count with hits is the disjunction's other arm — also RED, continue.

**STOP-GATE 1 — continue to Block 2 only if Block 1 showed at least one red arm.**

## §3 Block 2 — the fixed artifact + GREEN on the held card (fresh boot)

```bash
# WHERE: the held card, as nick. Verify the hops, lay the tree out the way run-smoke expects it, upgrade.
cd ~ && sha256sum homesynapse_7c9e4fa_arm64.deb dist-7c9e4fa.tar.gz
# expect: the SAME two hashes as the desktop and the bench card
tar xzf dist-7c9e4fa.tar.gz && mkdir -p distribution/deb/build && mv homesynapse_7c9e4fa_arm64.deb distribution/deb/build/ && ls -la distribution/deb/build/ distribution/smoke/ distribution/common.sh
# expect: the .deb under distribution/deb/build/ ; run-smoke.sh + health-probe.sh under distribution/smoke/ ; common.sh present
command -v curl >/dev/null || (sudo apt-get update && sudo apt-get install -y curl)
# (run-smoke checks 6–7 call curl directly; additive, lawful, ⏺ if it installed anything)
sudo apt install -y ./distribution/deb/build/homesynapse_7c9e4fa_arm64.deb
# expect: "Unpacking homesynapse (7c9e4fa) over (0.1.0+gd26777c)" … "HomeSynapse Core is running." … the pairing-token PATH banner (never the value)
dpkg -s homesynapse | grep -E "^Version:"
# expect: Version: 7c9e4fa
cat /opt/homesynapse/VERSION
# expect: 7c9e4fa  (stamped INTO the image by build-image.sh — the cheap proof the runtime inside is the new one, not a repackaged old tree)
```

**ONLY IF Block 1's `config/` listing showed NO `initial_api_token`** (otherwise skip this block entirely): checks 3 and 5 read that file, so give the fresh boot an empty store to mint into — the same store-reset rotation Block 3 performs on the bench card (the old hashes are preserved aside; delete nothing):

```bash
# WHERE: the held card — run ONLY when initial_api_token was ABSENT in Block 1.
sudo mv /var/lib/homesynapse/config/api_tokens /var/lib/homesynapse/config/api_tokens.rotated-2026-08-22 && sudo ls -la /var/lib/homesynapse/config/
# ⏺ the listing; the fresh boot below mints a new api_tokens + initial_api_token
```

```bash
# WHERE: the held card. The fresh boot — the GREEN leg's clean journal.
sudo reboot
```

Wait ~90 s, then `ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local` again.

```bash
# WHERE: the held card, FRESH boot. The hardware discriminator — the same instrument as Block 1, now against the fixed artifact in a clean journal.
uptime -s && systemctl status homesynapse.service --no-pager | head -5
# expect: a boot time a minute or two ago; Active: active (running) — if it reads "activating (start-post)" the ExecStartPost health probe (≤90 s) is still running: wait 30 s and re-run this line; do not STOP on it
sudo journalctl -u homesynapse.service -b --no-pager | grep -ciE "NoClassDefFoundError|jdk.jfr|BusMetrics"
# expect: 0   (the GREEN discriminator; ≥1 = STOP, ⏺ the next line's output, paste — never retune on the card)
sudo journalctl -u homesynapse.service -b --no-pager | grep -iE "NoClassDefFoundError|jdk.jfr|BusMetrics" | head -5
sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'
# expect: a count STRICTLY GREATER than Block 1's count (this boot's lifecycle publishes persisted — the position-delta §OP chose not to automate; you can read it by eye)
```

**STOP-GATE 2 — continue to run-smoke only if the discriminator printed 0.**

```bash
# WHERE: the held card, same fresh boot. The gate of record's own script, on hardware — installs (no-op), probes, stops, REMOVES (data preserved).
cd ~ && sudo ./distribution/smoke/run-smoke.sh 2>&1 | tee ~/block2-run-smoke.txt
```

**⏺ RECORD the whole output.** Expected (derived from run-smoke.sh at `7c9e4fa` — §6 P-2; every PASS line carries the `[smoke] ` prefix and two spaces after PASS; there are EIGHTEEN of them for nine checks): `[smoke] mode=systemd` · `[smoke] deb=/home/nick/distribution/deb/build/homesynapse_7c9e4fa_arm64.deb` · `[smoke] PASS  package installed` · `[smoke] PASS  unit is active` · `[smoke] PASS  unit is enabled (starts on boot)` · `[smoke] PASS  loopback health probe green (HTTP 200 RUNNING)` · **check 4's two positive lines:** `[smoke] PASS  event write path persisted N event row(s) this boot (/var/lib/homesynapse/data/homesynapse-events.db)` with N ≥ 1, and `[smoke] PASS  zero uncaught-throw signatures across 1 log source(s) (grep -icE 'NoClassDefFoundError|jdk.jfr|BusMetrics' = 0)` · `[smoke] PASS  first-run pairing token minted at /var/lib/homesynapse/config/initial_api_token` · `[smoke] PASS  token owned by homesynapse` · `[smoke] PASS  config dir mode 700 (no world access)` · `[smoke] PASS  unauthenticated request rejected (401) — auth enforced` · `[smoke] PASS  headerless GET / redirects to the dashboard (302)` · `[smoke] PASS  headerless GET /dashboard/ serves the shell (200)` · `[smoke] PASS  service stopped` · `[smoke] PASS  service inactive after stop` · `[smoke] PASS  package removed` · `[smoke] PASS  unit file gone` · `[smoke] PASS  image dir gone` · `[smoke] PASS  data dir preserved on remove (event store safe)` · `[smoke] INSTALL-SMOKE PASSED ✓  (gate #4: install path proven)`. Any `FAIL` = ⏺ verbatim (the diagnostics dump follows it), STOP, paste — the hub adjudicates. An output that simply ENDS without the `INSTALL-SMOKE` verdict line is ALSO a fail presentation (the script inherits `set -e` from `common.sh` and can abort on a failing assignment) — ⏺ and paste it as such.

```bash
# WHERE: the held card. Leave the rig READY for R-3 (the fixed artifact installed and running) and keep the evidence files.
id homesynapse; systemctl is-enabled homesynapse.service; ls -la /var/lib/homesynapse/config/
# expect: the user still exists; "disabled" or "not-found" (NOT "masked" — if masked: sudo systemctl unmask homesynapse.service, ⏺ it); api_tokens still present (the remove preserved the data dir)
sudo apt install -y ./distribution/deb/build/homesynapse_7c9e4fa_arm64.deb
# expect: "HomeSynapse Core is running."   (the store is non-empty → no new token mint; nothing about this card's token changes)
dpkg -s homesynapse | grep -E "^(Status|Version):"
# expect: Status: install ok installed · Version: 7c9e4fa
# THE L3 MASK — the first-run mint WARN-logs the raw pairing token into the journal (OpaqueTokenStore.java :214–:216); if the store reset ran, or any check dumped diagnostics, the two evidence files may carry it. Mask before anything leaves the card:
grep -c 'Token: ' ~/block1-red-journal.txt ~/block2-run-smoke.txt; sed -i 's/Token: .*/Token: [MASKED]/' ~/block1-red-journal.txt ~/block2-run-smoke.txt; grep -c 'Token: ' ~/block1-red-journal.txt ~/block2-run-smoke.txt
# ⏺ both counts (before/after); the files are evidence — the mask edits ONLY the token value lines
exit
```

```bash
# WHERE: your desktop. Bring the two evidence files home (they are the hub's intake, alongside your ⏺ pastes).
cd ~/Desktop/card-sitting-2026-08-22 && scp -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local:block1-red-journal.txt nick@hs-fresh.local:block2-run-smoke.txt . && ls -la
```

## §4 Block 3 — restore + THE TOKEN ROTATION BLOCK

Normal shutdown of the held card — from the desktop: `ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local 'sudo shutdown -h now'` (the FIFTH host-bearing line; the same IP substitution applies if `.local` fails) — wait for the LEDs → held card OUT — **labeled, kept: it is R-3/R-4's rig, now carrying the fixed artifact** → bench card IN → power on → wait ~90 s.

```bash
# WHERE: the bench card — `ssh pi`. The floor first.
~/bench.sh scenario boot-health
# ⏺ the [PASS] line (expect: [PASS] boot-health — 6/6 positive · 0 forbidden) and the bundle name
```

**THE TOKEN ROTATION — ALREADY RUN; CONFIRM ONLY (retired at v55 beat 3).** The 2026-08-21 enrichment listing proved the sitting-record §6 block executed on **2026-08-20 22:06 (Pi clock)**: `api_tokens.rotated-2026-08-20` (132 B, the original Jul-6 store moved aside) sits beside a FRESH `api_tokens` (132 B, 22:06) and a FRESH `initial_api_token` (44 B, 22:06) — one token in the live store, minted on the empty store; the hash of the token exposed in the 08-20 screenshots is no longer in the live store, so that token is DEAD. Do NOT rotate again (it would invalidate the re-paired browser for nothing). One glance closes the wait-state:

```bash
# WHERE: the bench card, as homesynapse. Read-only.
ls -la /home/homesynapse/hs-bench/config/
# expect: api_tokens (Aug 20 22:06) · api_tokens.rotated-2026-08-20 (Jul 6) · initial_api_token (Aug 20 22:06) — ⏺ the three lines; if any differs from this, ⏺ and paste (no act)
```

**Anti-actions (whole sitting):** never `rm` anything (mv/cp only) · never attach the coordinator to the held card · never run any block inside 03:00–04:15 CT · never paste a token value or an unmasked `Authorization` header · never retune a failing step on the card — ⏺ and stop · never run `build-deb.sh` from inside `distribution/` (the version string would be wrong) · never run `build-deb.sh` with a stale `distribution/image/build/` in place (it would skip the rebuild) · never edit the held card's files beyond what the blocks write (the L3 mask edits only token-value lines in the two evidence files this packet created).

## §5 ⏺ intake slots (paste as text, in this order)

- **⏺ Block 0:** the two `ls -la` listings + the `~/artifacts/` listing · the grep'd SIX build-log lines · the two sha256 lines (bench) · the two sha256 lines (desktop).
- **⏺ Block 1:** `dpkg -s` Status/Version · the `systemctl status` head · the two `ls -la` listings · the row count · the grep -ciE count · the grep head -5 · the `wc -l` of the journal dump.
- **⏺ Block 2:** the held-card sha256 pair · the `apt install` upgrade lines (Unpacking … over …; "is running.") · `dpkg -s` Version · `cat /opt/homesynapse/VERSION` · post-reboot: `uptime -s` + status head · the discriminator count (0) · the grep head (empty) · the row count (> Block 1's) · the COMPLETE run-smoke output (masked) · `id`/`is-enabled`/`ls` before the re-install · the re-install "is running." line + `dpkg -s` · the two mask counts.
- **⏺ Block 3:** the boot-health `[PASS]` line + bundle · the one `ls -la config/` listing (three expected lines).

## §6 Predictions of record (filed pre-run; the hub adjudicates EVERY deviation before any further act)

- **P-0 (Block 0):** the image REBUILDS (the `[build-image]` block prints — its absence is the stale-tree STOP) on arm64 with the 16-module `--add-modules` line above (the union is architecture-independent — jdeps analyses class references; the FLOOR is literal), `floor-presence assert green: all 16`, jar count 55 (the CI count; ⏺ the observed number — a different count is a NOTE, not a red), version `7c9e4fa` (bare — the a–f-only wrapper; `-dirty` appended only if the checkout is dirty).
- **P-1 (Block 1, RED):** rows ≥ 1 AND a matching-LINE count ≥ 6 (≈6 throws × ≥2 lines each; `NoClassDefFoundError: jdk/jfr/Event` / `ClassNotFoundException: jdk.jfr.Event`). Alternate arm: rows 0/absent with hits. BOTH-CLEAN = the refutation STOP.
- **P-2 (Block 2, GREEN):** upgrade clean (`Version: 7c9e4fa`; `/opt/homesynapse/VERSION` = `7c9e4fa`) · fresh-boot discriminator = 0 · row count > Block 1's · run-smoke 18/18 PASS lines (nine checks) with check 4's two positive lines · `INSTALL-SMOKE PASSED` · the re-install "is running.". (If the conditional store reset ran: the fresh boot shows a NEW `api_tokens` + `initial_api_token` on the held card beside `api_tokens.rotated-2026-08-22`; checks 3/5 pass on the minted file.)
- **P-3 (Block 3):** `[PASS] boot-health — 6/6 positive · 0 forbidden`; the config listing unchanged from the 08-21 enrichment read (the 08-20 22:06 store + artifact, the rotated store aside).
- **Named hazards:** the `_apt` "Download is performed unsandboxed" WARNING on a home-dir `.deb` is cosmetic (exit 0) · tunnel-refusal bursts during restarts are EXPECTED-CLASS · a `-dirty` suffix rides the version string into the filename AND the dpkg `Version:`/`Unpacking` lines (the packet's fixed filename absorbs the file; ⏺ the rest) · if `hs-fresh.local` does not resolve, `ssh pi` will not reach the held card either — read the IP from your router/`arp -a` and substitute it for `hs-fresh.local` in the FIVE ssh/scp lines (the ONLY substitution this packet ever asks for); because the same Pi hardware may hold the bench's DHCP lease, an IP-keyed `known_hosts` entry can collide with the held card's different host key — add `-o UserKnownHostsFile=~/.ssh/known_hosts_hsfresh` to those lines rather than editing `known_hosts` · the R-3 rig re-install after check 9 is a path CI never exercises (remove → install); the `id`/`is-enabled` glance prices it.
