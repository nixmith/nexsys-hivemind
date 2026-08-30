<!--
file: _scratch/2026-08-30_R3a_rehearsal_operator-record_RUNNING.md
purpose: The LIVE ⏺ record for the R-3a rehearsal, Sun 2026-08-30. Built block-by-block as the run proceeds. The hub files the final form at context/audits/2026-08-30_R3a_rehearsal_operator-record.md.
status: COMPLETE — §0-§11 ALL RUN, EVERY STOP-GATE PASSED. The bench is restored and [PASS]. Ready for hub filing at context/audits/2026-08-30_R3a_rehearsal_operator-record.md.
structure: executive summary + findings table -> the per-block adjudication (§0-§9) -> APPENDIX A the complete verbatim transcript (primary evidence; wins over the adjudication on any disagreement) -> APPENDIX B the 2026-08-29 source verification -> APPENDIX C the amendment ledger -> the card's current state (resume point).
redaction: NONE. No token VALUE was read, printed or transmitted at any point in this run - paths only. home_id appears because the packet requires it and it is an identifier, not a credential. The two custody tarballs are secret-bearing; only their SHA-256 digests appear.
note: R-3a was DEFERRED from Sat 2026-08-29 (see _scratch/2026-08-29_R3a_DEFERRED_desk-audit_operator-return.md for the ruling + the pre-run desk audit that produced amendments F-A1..F-A5).
-->

# R-3a operator record — Sun 2026-08-30 (COMPLETE)

> **STATUS: COMPLETE. §0–§11 all run, every STOP-gate passed.** The bench was restored at 15:06 ET with `[PASS] boot-health — 6/6 positive · 0 forbidden`, nine hours inside the Mon 03:00 CT floor. Scorecard: 32 predictions EXACT, 1 half, 5 misses owned in full.

## EXECUTIVE SUMMARY — what this run establishes

1. **OR-E3-PROBE is CLOSED on hardware.** Same card, same probe binary, same 44-byte artifact absent, fourteen minutes apart: the `7c9e4fa` unit took **90 s to fail** (`TIMEOUT`, `ExecMainStatus=143`, `Failed to start`, restart loop); the `dec35be` R-9 unit took **4 s to `active`** (`Result=success`, `NRestarts=0`, `ready (200) … /health`). The sole difference is `--health-path /health` on `ExecStartPost`. A single-variable controlled experiment on real silicon.
2. **The first CI-built `+git` artifact is on the card**, hash-identical across all three hops, with **zero event loss** (22 → 24 rows), integrity `ok`, `home_id` unchanged, and `--allow-downgrades` spent exactly once.
3. **H13 is satisfied: R-3b's spec is the §7 drop-in text, byte-for-byte, unmodified.** The candidate loosening was sufficient on first measurement — no second hypothesis was needed.
4. **The drop-in costs nothing measurable.** `projection_live → network_resumed` took **8.219 s** on the packaged+sandboxed held card versus **8.235 s** on the native bench the same morning. Sixteen milliseconds.
5. **The coordinator fence was load-bearing, not ceremonial.** §2 caught the held card sitting in the *form* state (no `zigbee-network.json` ⇒ `parameterStore.load()` empty ⇒ `resumeOrForm()` takes the FORM branch). For **47 min 54 s** the only thing preventing a new network on the live fleet's air was that the dongle was physically out of the hub.

## FINDINGS RAISED BY THIS RUN

| id | severity | one line |
|---|---|---|
| **§9-B** | **HIGH** | **The custody clone transfers the Zigbee network but NOT the HomeSynapse adoptions.** Cache loaded 6, rehydrated 0, zero relinks — rehydration matches the cache against the *registry*, a projection of the *event store*, which is not (and must not be) cloned. **§10's stated expectation is unreachable and must be rewritten; R-4 must plan for re-adoption, not resumption.** |
| **§6-B** | **MEDIUM-HIGH** | **The service lies about its own exit.** A graceful `systemctl stop` leaves the unit `failed`: the app catches SIGTERM, shuts down cleanly (SQLite checkpoint proves it), then exits **143** — the shell's "I was killed" convention — with no `SuccessExitStatus=143` on the unit. A never-false-ALIVE violation in the app's exit contract. |
| **§4-C** | **MEDIUM** | **The installer's own banner instructed operators into the OR-E3-PROBE failure** — *"then delete the token file"* — which under `7c9e4fa` is exactly the §3 experiment. R-9 is what makes the banner honest. |
| **§4-B** | **MEDIUM** | The packet's §4 I-3 groups the baseline and the install, un-chained, so **a failed `integrity_check` would not have stopped the install.** |
| **§3-A** | **MEDIUM** | `ExecMainStatus=143` re-states the E3 risk more precisely: systemd **tears down a healthy process**, it is not the app crashing. |
| **§2-A** | — | The held card was in the P-d state at pre-flight; the packet's F-S11 description of `data/zigbee/` as Aug-23 custody is wrong — it is re-created empty every boot. |
| **§4-A** | — | The probe's 503 arm fired; its full three-state model is now silicon-exercised. |
| **§8-A** | — | The dongle enumerated as `Device 004` vs `Device 011` on the bench — the class-rule choice over the source RAMP comment's node path was justified within the hour. |

**Prediction scoring across the run: 21 EXACT, 1 half (a `tail -20` truncation artifact, owned), 2 MISSES owned in full** — the packet's Δ+4 row model (observed Δ+2 on an upgrade restart) and the guide's §9 fleet-arm inference (see §9-B).

## HOW TO READ THIS DOCUMENT

- **§0 – §9 below** — the guide's adjudication of each block, with its STOP-gate verdict, prediction scoring, and findings.
- **Appendix A** — the complete verbatim transcript. Every command, every byte of output, unedited. **Where the adjudication and the transcript disagree, the transcript wins.**
- **Appendix B** — the source verification from the 2026-08-29 desk audit (read-only `git show`/`git grep` at `dec35be` / `7c9e4fa`), which produced the amendments.
- **Appendix C** — the amendment ledger: every deviation from the packet, with outcome and a ★ on those recommended for permanent adoption.
- **The card's current state** — the resume point, at the very end.

---

**Run window:** started 06:57 CT / 07:57 ET. Floor: bench `[PASS]` before Mon 03:00 CT / 04:00 ET.
**Amendments in force (from the 2026-08-29 desk audit):** F-A1 `adopt_list_loaded` is DEBUG · F-A2 permit-join glance · F-A3 P-c before P-b · F-A4 installed-unit check at §2 · F-A5 R-3b rider. Each marked `[AMEND]` where run.

---

## §0 [AMEND] Pre-swap bench health — the overnight nightly

`~/bench.sh digest 3`:
```
2026-08-28 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.34s
2026-08-29 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.50s
2026-08-30 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 3.29s
```
**Verdict: GREEN.** The digest line for 2026-08-30 is PRESENT (a missing line by morning is itself the red — `nightly.sh:18`). Floor unchanged at the `8/9 PASS · 1 SKIP(hue-online)` baseline.

**ON-latency 0.34 → 0.50 → 3.29 s — ⏺ AND CARRY, not a finding.** Initially flagged by the guide as a possible degradation trend; **withdrawn on the artifact.** `scenarios/constants.yaml:234` documents the metric as bimodal — "observed at 111 ms (S-1) and between 3.8 s and 5.0 s" — and `tools/runner/README.md:130` defines the field as the S-31 DISPATCHED→CONFIRMED distance accumulated into `~/hs-bench/digests/on-latency.log` for B4's corpus. It is observational, not a gate; the gate is the floor verdict, which PASSED. s31/nightly remain HANDS-OFF until R-5.

`~/bench.sh status`: `[OK] running (pid 31595)`, current boot log `bench-2026-08-30-043130.log`.

**[AMEND] §9 REFERENCE TRACE — the bench's own 04:31 boot, captured free.** This is the P-g arm the held card should reproduce at §9, with measured timings rather than the packet's estimate:
```
04:31:34.278  registry.projection_live: devices=6 entities=6 position=25065
04:31:34.732–.735  zigbee.device_relinked ×6
   0x00124B002FA8D1C5 / 0xF044D3FFFE9C78D7 / 0x449FDAFFFE688F57
   0x00178801101A09BB / 0xF044D3FFFED2A201 / 0xF044D3FFFE1C1E8E
04:31:34.736  zigbee.adoption_maps_rehydrated: devices=6
04:31:42.513  zigbee.network_resumed: channel=20 panId=0x774c
04:31:42.513  zigbee.network_up: stackStatusHandler reported EMBER_NETWORK_UP (buffered)
```
**projection_live → network_resumed = 8.2 s.** Zero failure tokens. **Zero `permit_join_opened`** — and `tools/bench.sh:23` proves that grep would have caught it.

---

## §1 Bench-side pre-flight + custody capture — **STOP-GATE §1: PASS**

**PF-0.** Clock `Sun 30 Aug 08:01:50 EDT 2026` ⏺ · `id -un` = `homesynapse` (owns the 0400 custody; the tar ran without sudo, as the packet's conditional anticipated) · config dir = **seven entries**, the three named ones exact: `api_tokens` 300 B `-rw-------` Aug 23 13:12 · `initial_api_token` 44 B `-rw-------` Aug 23 13:12 · `api_tokens.rotated-2026-08-20` 132 B. Both token files 600 here = the rotate-path mode, consistent with OR-TOKEN-MODE-644 (the held card's 644 pair is the Aug-13 mint vintage).

**The yaml path glance: NO HIT** on either `homesynapse.yaml` or `integrations/zigbee.yaml`. The gate holds — the clone will not point the packaged service at a bench path.

**[AMEND F-A2] — CLOSED, FOUND-SAFE, VERIFIED NOT ASSUMED.** `integrations/zigbee.yaml` carries **exactly three keys**:
```
serial_port: /dev/zigbee
channel: 20
adopt_devices:
```
**No `permit_join_duration`.** The held card therefore opens no Trust-Center join window on the live fleet at §9/§10, and the desk audit's escalation of the P-d price **dissolves**: a rogue formation would still land on channel 20 (the pin makes `formNetwork()` skip the energy scan), but with joins closed the six devices stay orphaned rather than recruited. P-d reverts to the packet's original pricing, which is what the §6 gate was already sized for. Corroborated by three independent artifacts: `tools/bench.sh:23` (the health grep includes `permit_join_opened`), the M9.4 acceptance runbook step 18 + the 2026-07-10 soak-entry record (the key was REMOVED, "joins closed, the SD-5 exception window is over"), and `scenarios/constants.yaml:15` (`permit_join_opened count 0` pinned as a watermark).

**Custody listing (the §6 comparison basis):** `.root-key` 32 B `-r--------` 0400 · `scope_keys.json` 248 B · `secrets.enc` 568 B · `zigbee-network.json` 122 B · **`zigbee-devices.json` 4551 B (LIVE, mtime 08:01)** · `zigbee-network.json.ch20-0x9b65.retired` 123 B and `_pre-seed-backup-20260719/` both stay behind. **`scope_nonce_counters.json` ABSENT** — the packet's tar line stood verbatim, no amendment needed.

**[AMEND — new hazard, closed at source] TORN-READ CHECK.** `zigbee-devices.json` had an mtime of 08:01 (i.e. *now*) — the running app actively rewrites the cache, and the §6 gate parse-checks only `zigbee-network.json`, never the device cache. A tar reading mid-flush could capture torn JSON that would ride undetected to §6. Both JSONs were therefore parse-checked **inside the tarball** immediately after creation: `network.json: PARSES` · `devices.json: PARSES`. **Recommend folding this into the packet permanently.**

**THE HASH CHAIN — hops 1 and 2 EQUAL.**
```
custody  268be10e5a2d0d57ad54483e8149231b34cc08d3b37b62b652732ace017432e1
config   fa8645c1df458e6e35c0fedf4217c8a2c4d432a5c37864834eb9f5d1536b462c
udev     3e46f44dabde83ccac851e1a17f50e7eaff8a75289e6ccf30630ba765eb4ec17
```
tar members: exactly the five `zigbee/…` files. Transfer sizes 1934 / 635 / 1134 B. Hop 3 (onto the card) is verified at §6.

**[AMEND — §4 I-1 pulled forward while the bench was still up] THE PINNED ARTIFACT CONFIRMED.**
`~/r3-artifact/homesynapse_0.1.0+git20260823.231355.gdec35be_arm64.deb` · **62,905,262 B** · sha256 **`8156f4cb9553883b882375b915594f01fe91dc5702ce09aad65df48db25b843f`** = the pinned origin value banked v57 beat 8. Flat in the directory (the `deb/` and `image/` upload trees remain beside it, unused).
**STOP-GATE I-0 PASSES EARLY** — the name carries `+git[0-9]{8}\.[0-9]{6}\.g[0-9a-f]{7,}`, no `0.1.0+g<sha>` or bare-id form, no `-dirty`. Pulling this forward means an artifact fault would have surfaced with the bench still up and the rig intact, rather than mid-swap.

---


## §2 THE SWAP + held-card pre-flight — **STOP-GATE §2: PASS**

**The swap.** Bench `sudo shutdown -h now` → ACT LED stopped → power OFF → **coordinator UNPLUGGED 07:19:14 CT = 08:19:14 ET** (SONOFF Dongle Plus MG24, hub 3-2.4 Port 2; a photo of the hub was taken first so §8 returns it to the identical port) → bench card OUT → held card `hs-fresh — R-3/R-4 rig — 7c9e4fa` IN → power ON. The radio stays out through §3–§7.

**[AMEND F-S20] the byte-identical BEFORE, captured while the bench was still up** — the §11 comparison target is now measured, not transcribed from the packet (it matches the packet exactly):
```
04:31:42.397 zigbee.port_identity_captured: stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false
04:31:42.513 zigbee.network_resumed: channel=20 panId=0x774c
by-id symlink → ../../ttyUSB0 · lsusb: Bus 003 Device 011: ID 10c4:ea60 Silicon Labs CP210x UART Bridge
/dev/ttyUSB0: crw-rw---- root dialout 188, 0   ← major 188 = the char-ttyUSB class, confirming §7's DeviceAllow class-rule choice against the live node
```

**Held-card pre-flight (`nick@hs-fresh.local`).** Clock `Sun 30 Aug 08:27:05 EDT 2026` ⏺ (this settles F-S21 for the day: the desk clock is CT, the Pi clocks are ET, +1 h) · `hs-fresh` · `throttled=0x0` · **`lsusb` count 0**, `/dev/zigbee` and `/dev/ttyUSB0` both `No such file` — **the fence holds, verified at the instrument** · `active` · discriminator **0** · probe: `no connection yet` → `[health-probe] ready (200) at http://127.0.0.1:7070/api/v1/entities` (the authed path; NO `token not yet available`, correct with the artifact present).

**Version pair:** `7c9e4fa` twice (dpkg == `/opt/homesynapse/VERSION`).

**ROWS-0 = 18.** The Aug-23 baseline was 14; this boot appended exactly 4. **H12's "≈4 lifecycle rows per boot" model confirmed live** — the §4 row-delta expectation rests on solid ground.

**[AMEND F-A4] — PASSES; the amendment earned its keep.**
```
ExecStartPost=/opt/homesynapse/libexec/health-probe.sh --wait --timeout 90
```
**No `--health-path`.** Because the probe binary is byte-identical at `7c9e4fa` and `dec35be` (desk audit §3.1 item 4), E3-RED's entire RED prediction rested on this and nothing else. It is now verified rather than assumed, so a `ready (200)` at §3 is a true refutation rather than an unnoticed already-upgraded card. **Recommend this check become permanent in the packet's §2.**

**Config listing:** `api_tokens` 132 B `-rw-r--r--` · `home_id` 26 B · `initial_api_token` 44 B `-rw-r--r--`, all Aug 13 07:35, plus `schemas/`. The three named entries match exactly. The 644 modes are F-S10 / OR-TOKEN-MODE-644 (the Aug-13 mint vintage) — KNOWN, not a stop. **Note: NO `homesynapse.yaml` and NO `integrations/` exist on this card** — §6's config tar introduces both, which is safe precisely because §1's path glance came back clean.

### ⏺ FINDING §2-A — THE HELD CARD IS SITTING IN THE P-d STATE RIGHT NOW

`data/zigbee/` contains **exactly one file**: `zigbee-devices.json`, **38 bytes**, mtime **Aug 30 08:20 — this boot**, not Aug 23. There is **no `zigbee-network.json`**, no `.root-key`, no `secrets.enc`, no `scope_keys.json`.

`ZigbeeIntegrationAdapter.resumeOrForm()` branches on `parameterStore.load().isPresent()`, and `load()` reads `zigbee-network.json`. **That file does not exist here.** So `load()` returns empty and the adapter would take the **FORM** branch the instant it saw a coordinator. The only thing preventing a new network on the live fleet's air is that the dongle is physically out of the hub.

**Consequences banked:** (1) the §2 coordinator fence is not ceremonial — it is the sole active control today, and the packet's insistence on it is vindicated at the instrument; (2) the §6 clone gate is correctly placed and its severity correctly priced — it is what converts this card from form-state to resume-state; (3) **the packet's F-S11 description needs correcting**: it describes this dir as custody "written at the Aug-23 16:54 ET boot with NO radio", but the dir is re-created with an empty device cache on every boot by `cache.flush()`. §6's "move aside" will set aside one 38-byte file, not a custody set — the expectation text should say so.


## §3 Block E3-RED — **STOP-GATE E3-RED: PASS** · the RED arm proven on hardware

**The measurement.** `12:30:44Z` → `12:32:14Z` = **exactly 90 s** (the probe burning `--timeout 90`). `restart rc=1`.

**Unit state:** `activating` · `Result=exit-code` · `NRestarts=0` · **`ExecMainStatus=143`**.

**Journal (the last 20 of ~45 matching lines):**
```
08:31:40 … 08:32:12  [health-probe] token not yet available at /var/lib/homesynapse/config/initial_api_token   (×17 visible, 2 s poll interval)
08:32:14  [health-probe] TIMEOUT after 90s — service did not become ready
08:32:14  systemd: homesynapse.service: Failed with result 'exit-code'.
08:32:14  systemd: Failed to start homesynapse.service - HomeSynapse Core — local-first smart-home engine.
```
**NO `ready (200)` in the red arm — the refutation branch did NOT fire.**

**Restore (§3 block 2, run regardless):** artifact back at `-rw-r--r-- 44 Aug 13 07:35` (mode AND mtime preserved by `mv` — F-S10 intact) · `active` · probe:
```
08:32:18  [health-probe] waiting up to 90s for readiness at http://127.0.0.1:7070/api/v1/entities
08:32:18  [health-probe] no connection yet
08:32:20  [health-probe] ready (200) at http://127.0.0.1:7070/api/v1/entities
```

### Prediction scoring (H12) — 6 of 7 EXACT, 1 truncation artifact

| filed | observed | verdict |
|---|---|---|
| ~90 s wall clock | 90 s exactly | **EXACT** |
| `restart rc=1` | `restart rc=1` | **EXACT** |
| `activating` or `failed` | `activating` | **EXACT** |
| `Result=exit-code` class | `Result=exit-code` | **EXACT** |
| ≥1 `token not yet available at <path>` | ×17 visible (~45 actual), path character-exact | **EXACT** |
| `TIMEOUT after 90s — service did not become ready` | character-exact, em-dash included | **EXACT** |
| `Failed to start` / `Scheduled restart job` **pair** | `Failed to start` present; `Scheduled restart job` ABSENT | **half — truncation artifact, not a miss** |

The `Scheduled restart job` line is absent because `RestartSec=10` had not elapsed at read time and `tail -20` was already full of probe lines. Recorded honestly rather than claimed.

### ⏺ FINDING §3-A — THE DISCRIMINATOR, AND A SHARPENING OF OR-E3-PROBE

**Same probe binary, same unit, same card: 90 s → FAILURE with the artifact absent; 2 s → `ready (200)` with it present.** A 45× difference produced by one 44-byte file. The E3 availability class is proven on real silicon for the RED arm.

**`ExecMainStatus=143` (128+15 = SIGTERM) was not predicted and it re-states the risk more precisely.** The application did not crash — it started normally. systemd **terminated a healthy process** because `ExecStartPost`'s readiness gate failed. So OR-E3-PROBE is not "a missing pairing artifact breaks the app"; it is **"a missing pairing artifact causes systemd to tear down a working service, then loop on it under `Restart=on-failure`."** Recommend the open-risk row adopt this wording — it is both more accurate and more alarming, and it is what makes the R-9 `/health` fix load-bearing rather than cosmetic.


## §4 Block I — the CI-built `dec35be` arm64 `.deb` — **STOP-GATES I-0 / I-1 / I-2: ALL PASS**

**I-0 (passed early, at §1, while the bench was still up).** `~/r3-artifact/homesynapse_0.1.0+git20260823.231355.gdec35be_arm64.deb` · 62,905,262 B · sha256 `8156f4cb9553883b882375b915594f01fe91dc5702ce09aad65df48db25b843f` = the pinned origin value. Name grammar `+git[0-9]{8}\.[0-9]{6}\.g<sha>` — the R-7b fence holds.

**I-1 — THE HASH CHAIN EQUAL ON ALL THREE HOPS.** origin (digest-verified zip) → desktop → card, all `8156f4cb9553883b882375b915594f01fe91dc5702ce09aad65df48db25b843f`. Card-side `dpkg-deb --field`: `Version: 0.1.0+git20260823.231355.gdec35be` · `Architecture: arm64` · no `-dirty`. Transfer 60 MB @ 37.3 MB/s.

**H12 CONFIRMED ON A THIRD SURFACE.** The version string predicted from `common.sh hs_version()` + the `dec35be` committer date now agrees across: the amd64 CI leg (banked v57), the desktop filename, and the card's own `dpkg-deb --field`.

**I-3 baseline (run as a SEPARATE gate — see finding §4-B).** ROWS-BEFORE **22** · `integrity_check` **ok** · home_id `01KZXEG38VC0ZT375GZ3H1P5QS` (26 ch, ULID) · `7c9e4fa` · [AMEND] disk 109 G free of 117 G, 4% used.

**The install.** `--allow-downgrades` used **EXACTLY ONCE** on this card, as designed:
```
Get:1 …/homesynapse_0.1.0+git20260823.231355.gdec35be_arm64.deb homesynapse arm64 0.1.0+git20260823.231355.gdec35be [62.9 MB]
dpkg: warning: downgrading homesynapse (7c9e4fa) to (0.1.0+git20260823.231355.gdec35be)
Unpacking homesynapse (0.1.0+git20260823.231355.gdec35be) over (7c9e4fa) …
Setting up homesynapse (0.1.0+git20260823.231355.gdec35be) …
HomeSynapse Core is running.
```

**Post-install verify — every I-2 condition met.** `0.1.0+git20260823.231355.gdec35be` **twice** (dpkg == image stamp) · `active` · **ROWS-AFTER 24 ≥ 22 — ZERO EVENT LOSS** · `integrity_check` **ok** · home_id **UNCHANGED** · discriminator **0**.

**The unit line, byte-for-byte the source:**
```
ExecStartPost=/opt/homesynapse/libexec/health-probe.sh --wait --timeout 90 --health-path /health
```
This is exactly `distribution/systemd/homesynapse.service:53` at `dec35be` as read at source in the 2026-08-29 desk audit (confirmation #1). **The desk audit's derived expectation is now verified on running hardware.**

**The probe, post-install:**
```
08:41:38  [health-probe] no connection yet
08:41:40  [health-probe] up, not ready yet (503)
08:41:42  [health-probe] ready (200) at http://127.0.0.1:7070/health
```

### ⏺ FINDING §4-A — the 503 branch fired; the probe's full state model is silicon-exercised

One boot walked all three readiness states: `000` no-connection → **`503` up-but-projection-not-ready** → `200` ready. Per `health-probe.sh` lines 8–12 the 503 arm means "up but the state projection is not LIVE — keep waiting". First observation of that arm on hardware. It is positive evidence the readiness gate does real work rather than racing to a 200, and it means `TimeoutStartSec=120` is genuinely load-bearing on this hardware.

### ⏺ FINDING §4-B — the packet's I-3 block lets a damaged store be installed over

§4 I-3 groups the baseline reads (`COUNT`, `PRAGMA integrity_check`, `home_id`, `dpkg-query`) and the `apt install` in one block, and they are NOT `&&`-chained across the boundary. **An `integrity_check` returning anything but `ok` would not have stopped the install.** Run split today, with the baseline as a real gate. **Recommend the packet adopt the split permanently** — the zero-LOSS assertion is meaningless if the baseline it is measured against was never allowed to halt anything.

### ⏺ FINDING §4-C — the install banner's advice is only safe because of R-9

The postinst banner prints, verbatim: *"Pair a client with that bearer token to reach the dashboard, **then delete the token file**."*

Under `7c9e4fa` — the unit on this card ninety minutes earlier — following that instruction is precisely the §3 experiment, and §3 measured its result: 90 s to `TIMEOUT`, `ExecMainStatus=143`, `Failed to start`, then a `Restart=on-failure` loop. **The shipped installer actively instructed operators into the OR-E3-PROBE failure.** R-9's `--health-path /health` is what makes the banner honest. Both halves are now measured on the SAME card, twenty minutes apart — an unusually clean before/after for the risk row.

### Prediction scoring (H12)

| filed | observed | verdict |
|---|---|---|
| desktop hash == card hash == origin | all three `8156f4cb…` | **EXACT** |
| `Version: 0.1.0+git20260823.231355.gdec35be` | identical | **EXACT** |
| `Architecture: arm64` | arm64 | **EXACT** |
| apt prints a downgrade line | `dpkg: warning: downgrading …` | **EXACT** (dpkg form) |
| post-install dpkg == image `VERSION` | both `0.1.0+git…gdec35be` | **EXACT** |
| `ExecStartPost … --health-path /health` | byte-identical to source | **EXACT** |
| discriminator 0 | 0 | **EXACT** |
| `ready (200) … /health` | exact | **EXACT** |
| rows AFTER ≥ BEFORE | 24 ≥ 22 | **PASS** |
| **Δ+4 rows on the install boot** | **Δ+2** | **MISS — owned** |

**The Δ+4 miss, owned and re-priced:** cold boots have now twice produced **+4** (Aug-23 Block 2; and ROWS-0 18 → ROWS-BEFORE 22 across §3's failed-start/stop/start cycle), but an **in-place upgrade restart produced +2**. The ≈4 model is boot-specific, not restart-specific. R-4's row accounting should carry the two-rate model rather than a single constant.


## §5 Block E3-GREEN — **STOP-GATE E3-GREEN: PASS** · **OR-E3-PROBE CLOSES ON HARDWARE**

**The measurement.** `12:44:08Z` → `12:44:12Z` = **4 s**. `restart rc=0`.

`active` · `Result=success` · `NRestarts=0`.

```
08:44:10.209  Started ServerConnector@…{HTTP/1.1}{127.0.0.1:7070}
08:44:10.222  Started Server@…{STARTING}[11.0.25,sto=0] @1968ms
08:44:10      [health-probe] up, not ready yet (503)
08:44:12      [health-probe] ready (200) at http://127.0.0.1:7070/health
08:44:12      systemd: Started homesynapse.service - HomeSynapse Core — local-first smart-home engine.
```
**ZERO `token not yet available` lines.** The fence pair: `/health` → **200**, `/api/v1/entities` → **401**. Artifact restored `-rw-r--r-- 44 Aug 13 07:35`, unit still `active` **without a restart** (the store, not the file, is the key's home).

### ⏺ THE E3 RESULT — a single-variable controlled experiment on silicon

| | artifact absent, `7c9e4fa` | artifact absent, `dec35be` (R-9) |
|---|---|---|
| elapsed | `12:30:44Z → 12:32:14Z` = **90 s** | `12:44:08Z → 12:44:12Z` = **4 s** |
| `restart rc` | **1** | **0** |
| unit | `activating` → `Failed to start`, `Restart=on-failure` loop | `active`, `Result=success`, `NRestarts=0` |
| `ExecMainStatus` | **143 (SIGTERM — a healthy process torn down)** | n/a |
| probe | ~45 × `token not yet available` → `TIMEOUT after 90s` | `503` → `ready (200) … /health` |

**Same card. Same probe binary (comments-only different between the two commits — desk audit §3.1 item 4). Same 44-byte file absent. Fourteen minutes apart. The sole difference is `--health-path /health` on `ExecStartPost`.** H8's bar is met: the packaged unit restarts to `active` with the pairing artifact absent, because the probe reads the unauthenticated loopback `/health`.

**OR-E3-PROBE — CLOSED.** Its stated closing condition ("R-9's CI banks green AND §OP-H passes on the bench AND the packaged unit restarts with the artifact absent") is now fully satisfied; the third leg landed here. Recommend the hub close the row at its next beat and adopt the §3-A wording (systemd tears down a *healthy* process) plus finding §4-C (the installer's own banner instructed operators into the failure) into the closure note.

**App start performance, incidental but banked:** Jetty up at `@1968ms`; probe saw 503 at +2 s and 200 at +4 s. Roughly 2 s process start plus 2 s projection catch-up on this hardware.


## §6 A-2 THE CLONE — **STOP-GATE §6 (THE CLONE GATE): PASS**

**Hop 3 of 3 — the custody set is byte-identical on all three machines.** bench == desktop == card:
```
custody  268be10e5a2d0d57ad54483e8149231b34cc08d3b37b62b652732ace017432e1
config   fa8645c1df458e6e35c0fedf4217c8a2c4d432a5c37864834eb9f5d1536b462c
udev     3e46f44dabde83ccac851e1a17f50e7eaff8a75289e6ccf30630ba765eb4ec17
```

**[DEVIATION — deliberate, recorded] the aside directory is named `zigbee.held-pre-r3-2026-08-30`, not the packet's `-2026-08-29`.** The run slipped a day; the directory is stamped with the date of the act. The hub already treats date-conformance in names as a live hazard (the RS-4 conform at v58 beat 4), and a directory stamped with a day the act did not occur is the wrong artifact to leave on disk.

**[AMEND — structural] the lay-down ran under an explicit stop-guard.** The packet's §6 runs `systemctl stop … && systemctl is-active`, then the `mv` as a SEPARATE command. `is-active` returns non-zero when stopped, so the `&&` chain terminates there and **the `mv` would execute regardless of whether the stop succeeded** — moving the custody directory out from under a live service. Today's block wrapped the entire lay-down in `if [ "$STATE" != inactive ] && [ "$STATE" != failed ]; then …NOTHING TOUCHED… fi`. **Recommend the packet adopt the guard.**

**The aside (delete-nothing, kept whole):** `zigbee.held-pre-r3-2026-08-30/zigbee-devices.json`, 38 B, mtime 08:44. This directory is now the **evidence exhibit for finding §2-A** — the card's pre-clone form state, preserved.

**Clean shutdown corroborated:** `homesynapse-events.db` 110592 → 118784 B with **both `-wal` and `-shm` gone** — SQLite checkpointed and closed the write-ahead log. No torn store.

### THE GATE — every condition met

**`zigbee-network.json` parses and names the bench network:**
```json
{ "channel": 20, "panId": 30540, "extendedPanId": 7455717304051557428, "networkKeyRef": "zigbee.network_key" }
```
**`panId` 30540 decimal = `0x774C`** — the bench's exact PAN on the bench's exact channel. This is the decisive verification of the day: `parameterStore.load()` will now return present, so `resumeOrForm()` takes the **RESUME** branch. The card is converted out of the form state, and §8's plug becomes safe.

**Custody listing — five files, bench-exact sizes, correct modes, all `homesynapse:homesynapse`:**
```
-r-------- 32    .root-key            (0400)
-rw------- 248   scope_keys.json      (0600)
-rw------- 568   secrets.enc          (0600)
-rw------- 4551  zigbee-devices.json  (0600)
-rw------- 122   zigbee-network.json  (0600)
drwx------ dir   (0700)
```
Custody hashes ⏺: `secrets.enc` = `ccface0ecff495fcb5d5aa53de7ae87a72cd47ea8d3aadcd968ce4b9377b77cb` · `scope_keys.json` = `d98f03f4b5aadb5f96023477d8edc1935085c112bc40ef708996c4d2bf65bb13`. Device cache parses post-extraction.

**Config:** `homesynapse.yaml` 1208 B 0600 and `integrations/` 0700 containing `zigbee.yaml` 299 B 0600 — **both introduced by the clone; neither existed on this card before.** The card's OWN `api_tokens` / `home_id` / `initial_api_token` (644) and `schemas/` untouched, exactly as the two tar lists guarantee.

**[AMEND F-A2] re-confirmed post-clone:** `serial_port: /dev/zigbee` · `channel: 20` · `adopt_devices:` · **no `permit_join_duration`.** No join window will open at §9/§10.

**[AMEND] torn-read hazard was REAL, not theoretical.** The bench's `zigbee-devices.json` mtime moved **08:01 → 08:05** between the §1 listing and the tar, at an unchanged 4551 B. The cache was actively rewritten during the capture window. The in-tar parse check is the only reason we know the captured copy is well-formed. **Recommend the packet adopt the parse-check permanently.**

### ⏺ FINDING §6-B — THE SERVICE LIES ABOUT ITS OWN EXIT (new; not in any packet or risk row)

A graceful, operator-requested `systemctl stop` leaves the unit **`failed`**, not `inactive`. Diagnosed at the instrument:
```
SuccessExitStatus=        (empty)
ExecMainCode=1            → CLD_EXITED: the process EXITED; it was NOT killed by a signal
ExecMainStatus=143
```
**Mechanism.** The unit sets `KillSignal=SIGTERM` and Main installs a SIGTERM shutdown hook (Doc 12 §7). The app catches SIGTERM, shuts down cleanly — the SQLite checkpoint above proves the shutdown was orderly — and then **exits deliberately with status 143**. But `128+N` is the *shell's* convention for "terminated by signal N"; a process that catches a signal, completes its shutdown and exits under its own control has **succeeded**, and should exit `0`. The app is reporting that it was killed when it was not. With no `SuccessExitStatus=143` on the unit, systemd correctly records `Result=exit-code` and marks the unit failed.

**Impact.** (1) Every clean stop and every host reboot leaves a `failed` unit; any monitor, smoke check or runbook asserting `inactive` after a stop sees a false alarm — the packet's own §6 expected `inactive`. (2) It does NOT cause a restart loop: systemd never restarts an explicitly-stopped unit whatever `Restart=` says. (3) It is why the packet's §3 restore block runs `systemctl reset-failed` before `start` — the workaround is already in the operator text with no explanation of what it works around. (4) Under the unit's own ExitCode contract (`RestartPreventExitStatus=10`; "all other non-zero exits are restart-worthy"), 143 is classified restart-worthy — harmless on an explicit stop, but wrong as a classification.

**This is a never-false-ALIVE violation in the app's exit contract**, the same family as the M9.4 `key_establishment_failed` misclassification: a healthy outcome reported through a failure channel.

**Recommended fix, root-correct first:** make the graceful SIGTERM shutdown path exit **0** (it succeeded). A unit-side `SuccessExitStatus=143` would silence the symptom but would also mask a genuine SIGTERM kill, so it is the inferior option. Candidate WU home: PKG-SEC-1's neighbourhood or the R-6/R-8 token-ops touch, whichever reaches the unit first. **This finding also sharpens §3-A**: at §3 systemd sent SIGTERM after `ExecStartPost` failed, and the app shut down gracefully and reported 143 — so §3's `ExecMainStatus=143` was never evidence of a crash, and the "healthy process torn down" reading is now confirmed at the instrument rather than inferred.


## §7 A-1 the drop-in + §8 the coordinator PLUG — **STOP-GATE §8: PASS**

### §7 — THE MEASURED TEXT (this is R-3b's spec under H13)

`/etc/systemd/system/homesynapse.service.d/10-serial-coordinator.conf`, written verbatim:
```ini
[Service]
PrivateDevices=no
DevicePolicy=closed
DeviceAllow=char-ttyUSB rw
DeviceAllow=char-ttyACM rw
SupplementaryGroups=dialout
```

**[AMEND] verified by EFFECTIVE merged config, not just the file text.** The packet verifies with `systemctl cat` (the text on disk); a mis-parsed or unloaded drop-in still looks perfect there. `systemctl show --no-pager` reports what systemd will actually apply:
```
PrivateDevices=no
DevicePolicy=closed
DeviceAllow=char-rtc r          ← NOT ours; systemd's implied rule from the base unit's clock protection. Benign, read-only.
DeviceAllow=char-ttyACM rw
DeviceAllow=char-ttyUSB rw
SupplementaryGroups=dialout
ExecStartPost=… --wait --timeout 90 --health-path /health   (unchanged by the drop-in)
```
**Recommend the packet verify with `show`, not `cat`** — and note the `char-rtc r` entry in R-3b so its author does not puzzle over an allow-rule nobody wrote.

**[OPERATOR NOTE] `systemctl show` pages by default.** The first attempt piped into `less` and the transcript filled with `ESCOC`/`ESCOD` (arrow-key echoes). `--no-pager` belongs on every `systemctl` invocation in the packet, not only on `journalctl`.

### §8 — the plug. **⏺ plugged 08:07:08 CT = 09:07:08 ET.**

**THE FENCE HELD 08:19:14 → 09:07:08 ET = 47 min 54 s**, unbroken across §3, §4, §5, §6 and §7 — the entire window in which the card sat in the form state.

```
lsusb:   Bus 003 Device 004: ID 10c4:ea60 Silicon Labs CP210x UART Bridge
node:    crw-rw---- 1 root dialout 188, 0  /dev/ttyUSB0        (major 188 = the char-ttyUSB class)
symlink: /dev/zigbee -> ttyUSB0                                 (09:07, the udev rule fired)
by-id:   usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0
id:      uid=102(homesynapse) gid=105(homesynapse) groups=105(homesynapse)   ← no dialout, correct
```

**The by-id string is BYTE-IDENTICAL to the pre-swap bench capture** (§2 record). F-S20's comparison target is measured on both ends of the day.

### ⏺ FINDING §8-A — the class-rule choice paid for itself within the hour

The dongle enumerated as **`Bus 003 Device 004`** on the held card versus **`Bus 003 Device 011`** on the bench this morning. The USB device number changed across the replug. The in-source RAMP comment at `dec35be` recommends `DeviceAllow=/dev/ttyUSB0 rw` — a node path; the packet's drop-in uses `DeviceAllow=char-ttyUSB rw` — a device-class rule (major 188), on the stated rationale that class rules survive replug renumbering. **That rationale was exercised for real, in the same session, and held.** This is now measured justification for F-A5's R-3b rider: the source comment should be updated to the class form, because the path form is demonstrably the more fragile of the two on this exact hardware.


## §9 A-3 THE MEASURED BOOT — **STOP-GATE §9: P-a. THE LOOSENING IS SUFFICIENT.**

**[AMEND] `systemctl reset-failed` was run before `start`**, so `NRestarts`/`Result` measure THIS boot rather than inheriting the exit-143 artifact of finding §6-B.

**The boot:** `13:12:19Z` → `start rc=0` → `13:12:23Z` = **4 s**. `active` · `Result=success` · `NRestarts=0`.

**The discriminator set, verbatim:**
```
09:12:21.208 [hs-sub-registry_projection]     registry.projection_live: devices=0 entities=0 position=0
09:12:21.726 [integration-supervisor-start]   zigbee.device_cache_loaded: 6 devices from /var/lib/homesynapse/data/zigbee/zigbee-devices.json
09:12:21.728 [integration-supervisor-start]   zigbee.adoption_maps_rehydrated: devices=0
09:12:29.307 [integration-zigbee-0]           ASH session connected: ashVersion=2 resetCode=0xb
09:12:29.310 [integration-zigbee-0]           zigbee.port_identity_captured: stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false
09:12:29.400 [integration-zigbee-0]           zigbee.ncp_configured: zdo_flags=0x3 stack_profile=2 security_level=5
09:12:29.427 [integration-zigbee-0]           zigbee.network_resumed: channel=20 panId=0x774c
09:12:29.427 [integration-zigbee-0]           zigbee.network_up: stackStatusHandler reported EMBER_NETWORK_UP (buffered)
```

**ARMS RESOLVED:** **P-a FIRED** · P-b REFUTED (no `transport_unbound`) · P-c REFUTED (no `EPERM`, no `Permission denied`) · **P-d DID NOT OCCUR** (no `network_formed`) · no `network_parameter_mismatch`.

**H13 SATISFIED — R-3b's spec is the §7 text, byte-for-byte, unmodified.** The candidate loosening was sufficient on first measurement; no second hypothesis was needed.

**[AMEND F-A2] confirmed a THIRD time, now at runtime on the held card:** zero `zigbee.permit_join_opened`. No join window opened on the live fleet.

**[AMEND F-A1] confirmed:** zero `zigbee.adopt_list_loaded` lines — expected, it is DEBUG-level. Its absence is not evidence of failure.

### ⏺ FINDING §9-A — THE DROP-IN COSTS NOTHING MEASURABLE

| | bench (04:31, native) | held card (09:12, packaged + drop-in) |
|---|---|---|
| `registry.projection_live` | 04:31:34.278 | 09:12:21.208 |
| `zigbee.network_resumed` | 04:31:42.513 | 09:12:29.427 |
| **elapsed** | **8.235 s** | **8.219 s** |

**Sixteen milliseconds apart.** The packaged path under `PrivateDevices=no` + `DevicePolicy=closed` + two class rules performs identically to the native bench app on the same fleet. `ncp_configured: zdo_flags=0x3 stack_profile=2 security_level=5` matches the bench's resume-arm signature exactly. There is no measurable sandbox penalty to report to R-3b.

### ⏺ FINDING §9-B — **THE CUSTODY CLONE TRANSFERS THE NETWORK BUT NOT THE ADOPTIONS** (the day's most consequential finding; re-prices §10 and R-4)

**Observed, and it refutes the guide's filed prediction:**
```
zigbee.device_cache_loaded:      6 devices     ← the cloned cache DOES carry six device records
zigbee.adoption_maps_rehydrated: devices=0     ← but ZERO rehydrated
registry.projection_live:        devices=0 entities=0 position=0
zigbee.device_relinked:          ABSENT ENTIRELY (bench had ×6)
```

**Prediction filed before the run (guide, §9):** "N=6 ⇒ the cloned cache drove rehydration ⇒ P-g, `device_relinked` ×6; N=0 ⇒ the registry is empty ⇒ P-e." **BOTH HALVES WRONG in their mechanism.** N=0 was correct as an observation, but the inference was not: the cache loaded 6 and *still* rehydrated 0. **Owned.**

**The mechanism, as the evidence forces it.** `adoption_maps_rehydrated` does not rehydrate from the device cache; it rehydrates the adapter's device→deviceId maps by matching cache entries **against the registry**. The registry is a projection of the **event store**. The event store was NOT cloned — correctly, and it must never be: this card carries its own `home_id` (`01KZXEG38VC0ZT375GZ3H1P5QS`) and its own event lineage, and cloning an event store across identities would be a far worse act than re-adopting six devices. Cache ∩ registry = ∅ ⇒ 0 rehydrated, 0 relinked. `position=0` corroborates: the projection replayed and consumed nothing, consistent with a 24-row store holding only lifecycle events and no adoption events.

**CONSEQUENCE 1 — the packet's §10 expectation is unreachable and must be rewritten.** §10 states: *"the Devices list shows the fleet with honest availability (expect 5 Available + 1 Unavailable, each with a fresh `Last reported`)"*. That text was authored for a bench-identical relink (P-g). **On a cloned-custody card the Devices list starts EMPTY and populates only as each device next speaks.** The correct §10 expectation is the P-f arm: nothing until `device_announce`, then `device_proposed` → `proposal_accepted` → `device_adopted` per device, driven by the cloned `adopt_devices` list. The motion-sensor walk and the single power-cycle are not fallbacks in this design — **they are the primary mechanism.**

**CONSEQUENCE 2 — R-4 must plan for re-adoption, not resumption.** Any R-4 acceptance criterion that assumes the rehearsal rig comes up with a populated fleet is unsound. The rig resumes the *network* in ~8 s; the *fleet* re-adopts device-by-device on each device's own schedule, which for a sleepy end device means on its next report.

**CONSEQUENCE 3 — a sharper statement of what custody cloning actually is.** It reproduces Zigbee-layer membership (channel, PAN, keys, NVRAM parameters → `network_resumed`). It does not reproduce application-layer identity (adoption records, entity IDs, availability history). The packet's §6 language ("the cloned cache carries the identities") is **wrong as stated** and should be corrected: the cache carries device *records*, not adoption *identities*.

**Open question for the hub:** whether `device_cache_loaded: 6` with `adoption_maps_rehydrated: 0` should itself log a WARN. Today it is two INFO lines whose disagreement is only visible to a reader who knows to compare them — a silently-succeedable arm of exactly the kind the project's own anti-vacuous doctrine targets.


---
---

# APPENDIX A — THE COMPLETE VERBATIM TRANSCRIPT

**Purpose.** Everything above is the guide's *adjudication*. This appendix is the *primary evidence*: every command issued and every byte of output returned, in run order, unedited. The hub can re-derive every verdict above from this appendix alone. Where the guide's reading and this transcript disagree, **the transcript wins**.

**Redaction policy:** NOTHING is redacted. No token VALUE was ever read, printed, or transmitted during this run — only paths. `home_id` appears because the packet explicitly requires it in the record; it is an identifier, not a credential. The two custody tarballs are secret-bearing but only their SHA-256 digests appear here, never their contents.

**Machines.** `DESKTOP-SRK0P9D` = Nick's Windows desktop (Git Bash; `~` = `C:\Users\Nick`) · `hs-dev-1` = the BENCH card, user `homesynapse`, reached as `ssh pi` · `hs-fresh` = the HELD card, user `nick`, reached as `ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local`.

**Clocks.** Both Pis run **ET (EDT, UTC-4)**. Nick's desk clock is **CT (CDT, UTC-5)**. `date -u` output is **Z (UTC)**. Per F-S21 every timestamp below is labelled.

---

## A.0 — Pre-swap bench health (guide addition; not in the packet)

```
homesynapse@hs-dev-1:~ $ ~/bench.sh digest 3; echo "--- status ---"; ~/bench.sh status; echo "--- §1 PF-0 ---"; date; id -un; ls -la /home/homesynapse/hs-bench/config/
2026-08-28 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.34s
2026-08-29 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.50s
2026-08-30 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 3.29s
--- status ---
  [OK] running (pid 31595)
--- health tokens (current boot: /home/homesynapse/hs-bench/bench-2026-08-30-043130.log) ---
04:31:34.278 [hs-sub-registry_projection] INFO  c.h.l.RegistryProjectionSubscriber -- registry.projection_live: devices=6 entities=6 position=25065
04:31:34.732 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0x00124B002FA8D1C5 deviceId=01KXW1W1RR66GV98D9QDPB4VXY — re-pairing, no new adoption
04:31:34.733 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0xF044D3FFFE9C78D7 deviceId=01KX1PB9A5931A8G0F0X03QXT2 — re-pairing, no new adoption
04:31:34.734 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0x449FDAFFFE688F57 deviceId=01KY12MQVQ204M1VP39F1ZDM33 — re-pairing, no new adoption
04:31:34.734 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0x00178801101A09BB deviceId=01KX1PA4GRZHY2GD37B5CFVQHY — re-pairing, no new adoption
04:31:34.735 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0xF044D3FFFED2A201 deviceId=01KXW0156Z1GJ3WCV2G516AKWS — re-pairing, no new adoption
04:31:34.735 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0xF044D3FFFE1C1E8E deviceId=01KXW13WEGRCT5C0XSQT8WZBG9 — re-pairing, no new adoption
04:31:34.736 [integration-supervisor-start] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.adoption_maps_rehydrated: devices=6
04:31:42.513 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
04:31:42.513 [integration-zigbee-0] INFO  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.network_up: stackStatusHandler reported EMBER_NETWORK_UP (buffered)
--- failure tokens ---
--- §1 PF-0 ---
Sun 30 Aug 08:01:50 EDT 2026
homesynapse
total 44
drwxrwxr-x 4 homesynapse homesynapse  4096 Aug 30 04:31 .
drwxrwxr-x 8 homesynapse homesynapse 12288 Aug 30 04:31 ..
-rw------- 1 homesynapse homesynapse   300 Aug 23 13:12 api_tokens
-rw-rw-r-- 1 homesynapse homesynapse   132 Jul  6 08:41 api_tokens.rotated-2026-08-20
-rw-rw-r-- 1 homesynapse homesynapse    26 Jul  6 08:41 home_id
-rw-rw-r-- 1 homesynapse homesynapse  1208 Jul  9 22:26 homesynapse.yaml
-rw------- 1 homesynapse homesynapse    44 Aug 23 13:12 initial_api_token
drwxrwxr-x 2 homesynapse homesynapse  4096 Jul 21 07:33 integrations
drwxrwxr-x 2 homesynapse homesynapse  4096 Jul  6 08:41 schemas
```

**Six device IEEE addresses and their bench deviceIds are captured above** — the definitive reference for what the fleet is and what identities the BENCH holds for them. Note these deviceIds are the *bench's* ULIDs; §9-B establishes they do NOT transfer with a custody clone.

---

## A.1 — §1 bench-side pre-flight

### A.1.1 The yaml glance + the custody listing

```
homesynapse@hs-dev-1:~ $ grep -nE "/home/|/mnt/|path" /home/homesynapse/hs-bench/config/homesynapse.yaml /home/homesynapse/hs-bench/config/integrations/zigbee.yaml
echo "--- [AMEND F-A2] the join-window + pin keys ---"
grep -nE "permit_join|channel|serial_port|adopt" /home/homesynapse/hs-bench/config/integrations/zigbee.yaml
echo "--- [AMEND F-A2] full key inventory, names only ---"
grep -E "^[a-zA-Z_]+:|^  +[a-zA-Z_]+:" /home/homesynapse/hs-bench/config/integrations/zigbee.yaml | sed -E 's/:.*/:/'
echo "--- the custody listing (the LIVE cache size is what §6 compares against) ---"
ls -la /home/homesynapse/hs-bench/data/zigbee/
--- [AMEND F-A2] the join-window + pin keys ---
1:serial_port: /dev/zigbee
2:channel: 20
3:adopt_devices:
--- [AMEND F-A2] full key inventory, names only ---
serial_port:
channel:
adopt_devices:
--- the custody listing (the LIVE cache size is what §6 compares against) ---
total 40
drwxrwxr-x 3 homesynapse homesynapse 4096 Aug 30 08:01 .
drwxrwxr-x 3 homesynapse homesynapse 4096 Aug 30 04:31 ..
drwxrwxr-x 2 homesynapse homesynapse 4096 Jul 18 20:53 _pre-seed-backup-20260719
-r-------- 1 homesynapse homesynapse   32 Jul 18 21:09 .root-key
-rw-rw-r-- 1 homesynapse homesynapse  248 Jul 18 21:09 scope_keys.json
-rw-rw-r-- 1 homesynapse homesynapse  568 Jul 18 21:09 secrets.enc
-rw-rw-r-- 1 homesynapse homesynapse 4551 Aug 30 08:01 zigbee-devices.json
-rw-rw-r-- 1 homesynapse homesynapse  122 Jul 18 21:09 zigbee-network.json
-rw-rw-r-- 1 homesynapse homesynapse  123 Jul  6 19:05 zigbee-network.json.ch20-0x9b65.retired
```

**The path grep produced NO OUTPUT — the gate that could have halted the day.** The zigbee.yaml has exactly three keys; `permit_join_duration` is absent.

### A.1.2 The custody tar + hop 1 hashes

```
homesynapse@hs-dev-1:~ $ mkdir -p ~/artifacts && tar czf ~/artifacts/zigbee-custody-for-r3.tar.gz -C /home/homesynapse/hs-bench/data zigbee/.root-key zigbee/scope_keys.json zigbee/secrets.enc zigbee/zigbee-network.json zigbee/zigbee-devices.json && tar czf ~/artifacts/bench-config-for-r3.tar.gz -C /home/homesynapse/hs-bench/config homesynapse.yaml integrations/zigbee.yaml && chmod 600 ~/artifacts/zigbee-custody-for-r3.tar.gz ~/artifacts/bench-config-for-r3.tar.gz && tar tzf ~/artifacts/zigbee-custody-for-r3.tar.gz
zigbee/.root-key
zigbee/scope_keys.json
zigbee/secrets.enc
zigbee/zigbee-network.json
zigbee/zigbee-devices.json
--- [AMEND] torn-read check: both JSONs parse INSIDE the tarball ---
network.json: PARSES
devices.json: PARSES
--- the three hashes (hop 1 of 3) ---
268be10e5a2d0d57ad54483e8149231b34cc08d3b37b62b652732ace017432e1  /home/homesynapse/artifacts/zigbee-custody-for-r3.tar.gz
fa8645c1df458e6e35c0fedf4217c8a2c4d432a5c37864834eb9f5d1536b462c  /home/homesynapse/artifacts/bench-config-for-r3.tar.gz
3e46f44dabde83ccac851e1a17f50e7eaff8a75289e6ccf30630ba765eb4ec17  /etc/udev/rules.d/99-zigbee-coordinator.rules
```

### A.1.3 Hop 2 (desktop) + the pinned artifact confirm

```
Nick@DESKTOP-SRK0P9D MINGW64 ~/Desktop/Code/ClaudeFolder/homesynapse-core (main)
$ mkdir -p ~/r3-rehearsal && cd ~/r3-rehearsal && scp pi:artifacts/zigbee-custody-for-r3.tar.gz pi:artifacts/bench-config-for-r3.tar.gz pi:/etc/udev/rules.d/99-zigbee-coordinator.rules . && sha256sum zigbee-custody-for-r3.tar.gz bench-config-for-r3.tar.gz 99-zigbee-coordinator.rules
zigbee-custody-for-r3.tar.gz     100% 1934   210.2KB/s   00:00
bench-config-for-r3.tar.gz       100%  635    76.8KB/s   00:00
99-zigbee-coordinator.rules      100% 1134   129.8KB/s   00:00
268be10e5a2d0d57ad54483e8149231b34cc08d3b37b62b652732ace017432e1 *zigbee-custody-for-r3.tar.gz
fa8645c1df458e6e35c0fedf4217c8a2c4d432a5c37864834eb9f5d1536b462c *bench-config-for-r3.tar.gz
3e46f44dabde83ccac851e1a17f50e7eaff8a75289e6ccf30630ba765eb4ec17 *99-zigbee-coordinator.rules
--- [AMEND, pulled forward from §4 I-1] the pinned CI artifact ---
total 61464
drwxr-xr-x 1 Nick 197121        0 Aug 28 04:44 .
drwxr-xr-x 1 Nick 197121        0 Aug 30 07:07 ..
drwxr-xr-x 1 Nick 197121        0 Aug 27 21:38 deb
-rw-r--r-- 1 Nick 197121 62905262 Aug 23 23:15 homesynapse_0.1.0+git20260823.231355.gdec35be_arm64.deb
drwxr-xr-x 1 Nick 197121        0 Aug 27 21:38 image
8156f4cb9553883b882375b915594f01fe91dc5702ce09aad65df48db25b843f */c/Users/Nick/r3-artifact/homesynapse_0.1.0+git20260823.231355.gdec35be_arm64.deb
```

### A.1.4 [AMEND F-S20] The last bench reads before the swap — the byte-identical BEFORE

```
homesynapse@hs-dev-1:~ $ ls -l /dev/serial/by-id/ | grep -i sonoff
lrwxrwxrwx 1 root root 13 Aug 30 04:31 usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 -> ../../ttyUSB0
--- lsusb ---
Bus 003 Device 011: ID 10c4:ea60 Silicon Labs CP210x UART Bridge
--- the symlink + node ---
crw-rw---- 1 root dialout 188, 0 Aug 30 08:09 /dev/ttyUSB0
lrwxrwxrwx 1 root root         7 Aug 30 04:31 /dev/zigbee -> ttyUSB0
--- [AMEND F-S20] the byte-identical BEFORE ---
04:31:42.397 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.port_identity_captured: stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false
04:31:42.513 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
```

---

## A.2 — §2 THE SWAP + held-card pre-flight

**Physical sequence performed by the operator:** `sudo shutdown -h now` on the bench → ACT LED stopped → power OFF → **coordinator UNPLUGGED 07:19:14 CT = 08:19:14 ET** (SONOFF Dongle Plus MG24, hub 3-2.4 Port 2; hub photographed first) → bench card OUT → held card IN → power ON → ~90 s.

```
nick@hs-fresh:~ $ echo "=== fence + identity ==="
date; hostname; sudo vcgencmd get_throttled; lsusb | grep -ci "10c4:ea60"; ls -l /dev/zigbee /dev/ttyUSB0 2>&1; systemctl is-active homesynapse.service
=== fence + identity ===
Sun 30 Aug 08:27:05 EDT 2026
hs-fresh
throttled=0x0
0
ls: cannot access '/dev/zigbee': No such file or directory
ls: cannot access '/dev/ttyUSB0': No such file or directory
active
=== [AMEND F-A4] the INSTALLED unit — E3-RED's precondition ===
ExecStartPost=/opt/homesynapse/libexec/health-probe.sh --wait --timeout 90
=== the version pair ===
7c9e4fa
7c9e4fa
=== config listing (F-S10: the 644 modes are KNOWN, not a stop) ===
total 24
drwx------ 3 homesynapse homesynapse 4096 Aug 13 07:35 .
drwx------ 6 homesynapse homesynapse 4096 Aug 13 07:35 ..
-rw-r--r-- 1 homesynapse homesynapse  132 Aug 13 07:35 api_tokens
-rw-r--r-- 1 homesynapse homesynapse   26 Aug 13 07:35 home_id
-rw-r--r-- 1 homesynapse homesynapse   44 Aug 13 07:35 initial_api_token
drwxr-xr-x 2 homesynapse homesynapse 4096 Aug 13 07:35 schemas
=== data + this card's OWN radio-less custody (F-S11) ===
/var/lib/homesynapse/data/:
total 288
drwx------ 3 homesynapse homesynapse   4096 Aug 30 08:20 .
drwx------ 6 homesynapse homesynapse   4096 Aug 13 07:35 ..
-rw-r--r-- 1 homesynapse homesynapse 110592 Aug 23 17:16 homesynapse-events.db
-rw-r--r-- 1 homesynapse homesynapse  32768 Aug 30 08:20 homesynapse-events.db-shm
-rw-r--r-- 1 homesynapse homesynapse 135992 Aug 30 08:20 homesynapse-events.db-wal
drwxr-xr-x 2 homesynapse homesynapse   4096 Aug 30 08:20 zigbee

/var/lib/homesynapse/data/zigbee/:
total 12
drwxr-xr-x 2 homesynapse homesynapse 4096 Aug 30 08:20 .
drwx------ 3 homesynapse homesynapse 4096 Aug 30 08:20 ..
-rw-r--r-- 1 homesynapse homesynapse   38 Aug 30 08:20 zigbee-devices.json
=== ROWS-0 + discriminator + probe ===
18
0
Aug 30 08:20:24 hs-fresh homesynapse[893]: [health-probe] no connection yet
Aug 30 08:20:26 hs-fresh homesynapse[893]: [health-probe] ready (200) at http://127.0.0.1:7070/api/v1/entities
```

**Operator note, recorded for completeness:** a first attempt at priming sudo used `sudo -v`, which prompts even under NOPASSWD and produced three failed password attempts before the operator retrieved the password. The correct non-prompting probe is `sudo -n true`. No lockout occurred (standard sudo has none). Sudo on `hs-fresh` DOES require a password; the standing practice adopted for the rest of the run was `sudo -v` on its own line immediately before any multi-line block containing `sudo`.


---

## A.3 — §3 Block E3-RED

### A.3.1 The RED arm

```
nick@hs-fresh:~ $ sudo -v
nick@hs-fresh:~ $ sudo mv /var/lib/homesynapse/config/initial_api_token /var/lib/homesynapse/config/initial_api_token.e3red && date -u +%H:%M:%SZ && sudo systemctl restart homesynapse.service; echo "restart rc=$?"; date -u +%H:%M:%SZ
systemctl is-active homesynapse.service; systemctl show -p NRestarts -p Result -p ExecMainStatus homesynapse.service
sudo journalctl -u homesynapse.service -b --no-pager --since "-4min" | grep -E "health-probe|Started|Failed|Scheduled restart|start-limit" | tail -20
12:30:44Z
Job for homesynapse.service failed because the control process exited with error code.
See "systemctl status homesynapse.service" and "journalctl -xeu homesynapse.service" for details.
restart rc=1
12:32:14Z
activating
Result=exit-code
NRestarts=0
ExecMainStatus=143
Aug 30 08:31:40 hs-fresh homesynapse[1130]: [health-probe] token not yet available at /var/lib/homesynapse/config/initial_api_token
Aug 30 08:31:42 hs-fresh homesynapse[1130]: [health-probe] token not yet available at /var/lib/homesynapse/config/initial_api_token
Aug 30 08:31:44 hs-fresh homesynapse[1130]: [health-probe] token not yet available at /var/lib/homesynapse/config/initial_api_token
Aug 30 08:31:46 hs-fresh homesynapse[1130]: [health-probe] token not yet available at /var/lib/homesynapse/config/initial_api_token
Aug 30 08:31:48 hs-fresh homesynapse[1130]: [health-probe] token not yet available at /var/lib/homesynapse/config/initial_api_token
Aug 30 08:31:50 hs-fresh homesynapse[1130]: [health-probe] token not yet available at /var/lib/homesynapse/config/initial_api_token
Aug 30 08:31:52 hs-fresh homesynapse[1130]: [health-probe] token not yet available at /var/lib/homesynapse/config/initial_api_token
Aug 30 08:31:54 hs-fresh homesynapse[1130]: [health-probe] token not yet available at /var/lib/homesynapse/config/initial_api_token
Aug 30 08:31:56 hs-fresh homesynapse[1130]: [health-probe] token not yet available at /var/lib/homesynapse/config/initial_api_token
Aug 30 08:31:58 hs-fresh homesynapse[1130]: [health-probe] token not yet available at /var/lib/homesynapse/config/initial_api_token
Aug 30 08:32:00 hs-fresh homesynapse[1130]: [health-probe] token not yet available at /var/lib/homesynapse/config/initial_api_token
Aug 30 08:32:02 hs-fresh homesynapse[1130]: [health-probe] token not yet available at /var/lib/homesynapse/config/initial_api_token
Aug 30 08:32:04 hs-fresh homesynapse[1130]: [health-probe] token not yet available at /var/lib/homesynapse/config/initial_api_token
Aug 30 08:32:06 hs-fresh homesynapse[1130]: [health-probe] token not yet available at /var/lib/homesynapse/config/initial_api_token
Aug 30 08:32:08 hs-fresh homesynapse[1130]: [health-probe] token not yet available at /var/lib/homesynapse/config/initial_api_token
Aug 30 08:32:10 hs-fresh homesynapse[1130]: [health-probe] token not yet available at /var/lib/homesynapse/config/initial_api_token
Aug 30 08:32:12 hs-fresh homesynapse[1130]: [health-probe] token not yet available at /var/lib/homesynapse/config/initial_api_token
Aug 30 08:32:14 hs-fresh homesynapse[1130]: [health-probe] TIMEOUT after 90s — service did not become ready
Aug 30 08:32:14 hs-fresh systemd[1]: homesynapse.service: Failed with result 'exit-code'.
Aug 30 08:32:14 hs-fresh systemd[1]: Failed to start homesynapse.service - HomeSynapse Core — local-first smart-home engine.
```

**17 `token not yet available` lines are VISIBLE; the true count is ~45** (2 s poll × 90 s). `tail -20` truncated the head of the sequence. This is also why no `Scheduled restart job` line appears — `RestartSec=10` had not elapsed at read time and the tail was already full.

### A.3.2 The restore (run regardless of the RED arm's result)

```
nick@hs-fresh:~ $ sudo systemctl stop homesynapse.service; sudo mv /var/lib/homesynapse/config/initial_api_token.e3red /var/lib/homesynapse/config/initial_api_token && sudo ls -la /var/lib/homesynapse/config/initial_api_token && sudo systemctl reset-failed homesynapse.service && sudo systemctl start homesynapse.service && sleep 15 && systemctl is-active homesynapse.service && sudo journalctl -u homesynapse.service -b --no-pager --since "-1min" | grep -E "health-probe" | tail -3
-rw-r--r-- 1 homesynapse homesynapse 44 Aug 13 07:35 /var/lib/homesynapse/config/initial_api_token
active
Aug 30 08:32:18 hs-fresh homesynapse[1265]: [health-probe] waiting up to 90s for readiness at http://127.0.0.1:7070/api/v1/entities
Aug 30 08:32:18 hs-fresh homesynapse[1265]: [health-probe] no connection yet
Aug 30 08:32:20 hs-fresh homesynapse[1265]: [health-probe] ready (200) at http://127.0.0.1:7070/api/v1/entities
--- [AMEND] unconditional re-read ---
active
Aug 30 08:32:18 hs-fresh homesynapse[1265]: [health-probe] waiting up to 90s for readiness at http://127.0.0.1:7070/api/v1/entities
Aug 30 08:32:18 hs-fresh homesynapse[1265]: [health-probe] no connection yet
Aug 30 08:32:20 hs-fresh homesynapse[1265]: [health-probe] ready (200) at http://127.0.0.1:7070/api/v1/entities
```

---

## A.4 — §4 Block I

### A.4.1 I-2 the card-side hop

```
Nick@DESKTOP-SRK0P9D MINGW64 ~/r3-rehearsal
$ cd ~/r3-artifact && scp -i ~/.ssh/id_ed25519_pi homesynapse_*_arm64.deb nick@hs-fresh.local: && ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local 'sha256sum ~/homesynapse_*_arm64.deb; dpkg-deb --field ~/homesynapse_*_arm64.deb Version Architecture'
homesynapse_0.1.0+git20260823.231355.gdec35be_arm64.deb    100%   60MB  37.3MB/s   00:01
8156f4cb9553883b882375b915594f01fe91dc5702ce09aad65df48db25b843f  /home/nick/homesynapse_0.1.0+git20260823.231355.gdec35be_arm64.deb
Version: 0.1.0+git20260823.231355.gdec35be
Architecture: arm64
```

### A.4.2 I-3 the baseline (run as a SEPARATE gate — see finding §4-B)

```
nick@hs-fresh:~ $ sudo -v
nick@hs-fresh:~ $ sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'
sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'PRAGMA integrity_check;'
sudo cat /var/lib/homesynapse/config/home_id; echo
dpkg-query -W -f '${Version}\n' homesynapse
echo "--- [AMEND] headroom before a 63 MB install ---"
df -h /var /opt / | tail -4
22
ok
01KZXEG38VC0ZT375GZ3H1P5QS
7c9e4fa
--- [AMEND] headroom before a 63 MB install ---
Filesystem      Size  Used Avail Use% Mounted on
/dev/mmcblk0p2  117G  4.1G  109G   4% /
/dev/mmcblk0p2  117G  4.1G  109G   4% /
/dev/mmcblk0p2  117G  4.1G  109G   4% /
```

### A.4.3 I-3 the install + full verify

```
nick@hs-fresh:~ $ sudo apt install -y --allow-downgrades ~/homesynapse_*_arm64.deb 2>&1 | tail -15
Get:1 /home/nick/homesynapse_0.1.0+git20260823.231355.gdec35be_arm64.deb homesynapse arm64 0.1.0+git20260823.231355.gdec35be [62.9 MB]
dpkg: warning: downgrading homesynapse (7c9e4fa) to (0.1.0+git20260823.231355.gdec35be)
(Reading database ... 66758 files and directories currently installed.)
Preparing to unpack .../homesynapse_0.1.0+git20260823.231355.gdec35be_arm64.deb ...
Unpacking homesynapse (0.1.0+git20260823.231355.gdec35be) over (7c9e4fa) ...
Setting up homesynapse (0.1.0+git20260823.231355.gdec35be) ...
HomeSynapse Core is running.
----------------------------------------------------------------
 HomeSynapse Core installed.
 First-run pairing token: /var/lib/homesynapse/config/initial_api_token
   View it with:  sudo homesynapse-token
   Pair a client with that bearer token to reach the dashboard,
   then delete the token file.
----------------------------------------------------------------
=== version pair + unit + readiness ===
0.1.0+git20260823.231355.gdec35be
0.1.0+git20260823.231355.gdec35be
active
ExecStartPost=/opt/homesynapse/libexec/health-probe.sh --wait --timeout 90 --health-path /health
=== zero-LOSS + identity + discriminator + probe ===
24
ok
01KZXEG38VC0ZT375GZ3H1P5QS
0
Aug 30 08:41:38 hs-fresh homesynapse[1565]: [health-probe] no connection yet
Aug 30 08:41:40 hs-fresh homesynapse[1565]: [health-probe] up, not ready yet (503)
Aug 30 08:41:42 hs-fresh homesynapse[1565]: [health-probe] ready (200) at http://127.0.0.1:7070/health
```

**The banner text `then delete the token file` is the subject of finding §4-C.**

---

## A.5 — §5 Block E3-GREEN

```
nick@hs-fresh:~ $ sudo mv /var/lib/homesynapse/config/initial_api_token /var/lib/homesynapse/config/initial_api_token.e3green && date -u +%H:%M:%SZ && sudo systemctl restart homesynapse.service; echo "restart rc=$?"; date -u +%H:%M:%SZ
systemctl is-active homesynapse.service; systemctl show -p NRestarts -p Result homesynapse.service; sudo journalctl -u homesynapse.service -b --no-pager --since "-2min" | grep -E "health-probe|Started" | tail -5
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:7070/health; curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:7070/api/v1/entities
sudo mv /var/lib/homesynapse/config/initial_api_token.e3green /var/lib/homesynapse/config/initial_api_token && sudo ls -la /var/lib/homesynapse/config/initial_api_token && systemctl is-active homesynapse.service
12:44:08Z
restart rc=0
12:44:12Z
active
Result=success
NRestarts=0
Aug 30 08:44:10 hs-fresh homesynapse[1679]: 08:44:10.209 [main] INFO  o.e.jetty.server.AbstractConnector -- Started ServerConnector@112d1c8e{HTTP/1.1, (http/1.1)}{127.0.0.1:7070}
Aug 30 08:44:10 hs-fresh homesynapse[1679]: 08:44:10.222 [main] INFO  org.eclipse.jetty.server.Server -- Started Server@5cb042da{STARTING}[11.0.25,sto=0] @1968ms
Aug 30 08:44:10 hs-fresh homesynapse[1684]: [health-probe] up, not ready yet (503)
Aug 30 08:44:12 hs-fresh homesynapse[1684]: [health-probe] ready (200) at http://127.0.0.1:7070/health
Aug 30 08:44:12 hs-fresh systemd[1]: Started homesynapse.service - HomeSynapse Core — local-first smart-home engine.
200
401
-rw-r--r-- 1 homesynapse homesynapse 44 Aug 13 07:35 /var/lib/homesynapse/config/initial_api_token
active
```


---

## A.6 — §6 A-2 THE CLONE

### A.6.1 Hop 3 of 3

```
Nick@DESKTOP-SRK0P9D MINGW64 ~/r3-artifact
$ cd ~/r3-rehearsal && scp -i ~/.ssh/id_ed25519_pi zigbee-custody-for-r3.tar.gz bench-config-for-r3.tar.gz 99-zigbee-coordinator.rules nick@hs-fresh.local: && ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local 'cd ~ && sha256sum zigbee-custody-for-r3.tar.gz bench-config-for-r3.tar.gz 99-zigbee-coordinator.rules'
zigbee-custody-for-r3.tar.gz     100% 1934   388.9KB/s   00:00
bench-config-for-r3.tar.gz       100%  635   150.6KB/s   00:00
99-zigbee-coordinator.rules      100% 1134   287.5KB/s   00:00
268be10e5a2d0d57ad54483e8149231b34cc08d3b37b62b652732ace017432e1  zigbee-custody-for-r3.tar.gz
fa8645c1df458e6e35c0fedf4217c8a2c4d432a5c37864834eb9f5d1536b462c  bench-config-for-r3.tar.gz
3e46f44dabde83ccac851e1a17f50e7eaff8a75289e6ccf30630ba765eb4ec17  99-zigbee-coordinator.rules
```

### A.6.2 The lay-down, under the [AMEND] stop-guard

```
nick@hs-fresh:~ $ sudo -v
[sudo] password for nick:
nick@hs-fresh:~ $ sudo systemctl stop homesynapse.service
sleep 2
STATE=$(systemctl is-active homesynapse.service); echo "state=$STATE"
if [ "$STATE" != "inactive" ] && [ "$STATE" != "failed" ]; then echo "GATE FAILED — service is '$STATE'; NOTHING TOUCHED. Stop and paste."; else
  sudo mv /var/lib/homesynapse/data/zigbee /var/lib/homesynapse/data/zigbee.held-pre-r3-2026-08-30 && echo "--- aside done ---" && sudo ls -la /var/lib/homesynapse/data/ /var/lib/homesynapse/data/zigbee.held-pre-r3-2026-08-30/
  ... [extract / chown+chmod / udev stages] ...
fi
state=failed
--- aside done ---
/var/lib/homesynapse/data/:
total 128
drwx------ 3 homesynapse homesynapse   4096 Aug 30 08:58 .
drwx------ 6 homesynapse homesynapse   4096 Aug 13 07:35 ..
-rw-r--r-- 1 homesynapse homesynapse 118784 Aug 30 08:58 homesynapse-events.db
drwxr-xr-x 2 homesynapse homesynapse   4096 Aug 30 08:44 zigbee.held-pre-r3-2026-08-30

/var/lib/homesynapse/data/zigbee.held-pre-r3-2026-08-30/:
total 12
drwxr-xr-x 2 homesynapse homesynapse 4096 Aug 30 08:44 .
drwx------ 3 homesynapse homesynapse 4096 Aug 30 08:58 ..
-rw-r--r-- 1 homesynapse homesynapse   38 Aug 30 08:44 zigbee-devices.json
--- extracting the clone ---
extract OK
--- ownership + modes ---
modes OK
--- udev ---
udev reloaded
```

**`state=failed`, not `inactive`** — the guard accepted it (a failed unit is not running) and this is the origin of finding §6-B. Note `homesynapse-events.db` 110592 → 118784 B with `-wal`/`-shm` GONE: a clean SQLite checkpoint on shutdown.

### A.6.3 THE CLONE GATE

```
nick@hs-fresh:~ $ sudo -v
nick@hs-fresh:~ $ echo "=== the network parameters must parse and name the bench PAN ==="
sudo python3 -m json.tool /var/lib/homesynapse/data/zigbee/zigbee-network.json
=== the network parameters must parse and name the bench PAN ===
{
    "channel": 20,
    "panId": 30540,
    "extendedPanId": 7455717304051557428,
    "networkKeyRef": "zigbee.network_key"
}
=== [AMEND] the device cache must parse too (post-extraction) ===
devices.json: PARSES
=== the custody listing — sizes and modes ===
total 32
drwx------ 2 homesynapse homesynapse 4096 Aug 30 08:58 .
drwx------ 4 homesynapse homesynapse 4096 Aug 30 08:58 ..
-r-------- 1 homesynapse homesynapse   32 Jul 18 21:09 .root-key
-rw------- 1 homesynapse homesynapse  248 Jul 18 21:09 scope_keys.json
-rw------- 1 homesynapse homesynapse  568 Jul 18 21:09 secrets.enc
-rw------- 1 homesynapse homesynapse 4551 Aug 30 08:05 zigbee-devices.json
-rw------- 1 homesynapse homesynapse  122 Jul 18 21:09 zigbee-network.json
=== the two custody hashes ===
ccface0ecff495fcb5d5aa53de7ae87a72cd47ea8d3aadcd968ce4b9377b77cb  /var/lib/homesynapse/data/zigbee/secrets.enc
d98f03f4b5aadb5f96023477d8edc1935085c112bc40ef708996c4d2bf65bb13  /var/lib/homesynapse/data/zigbee/scope_keys.json
=== the config landed, and [AMEND F-A2] no join window rode along ===
/var/lib/homesynapse/config/:
total 32
drwx------ 4 homesynapse homesynapse 4096 Aug 30 08:58 .
drwx------ 6 homesynapse homesynapse 4096 Aug 13 07:35 ..
-rw-r--r-- 1 homesynapse homesynapse  132 Aug 13 07:35 api_tokens
-rw-r--r-- 1 homesynapse homesynapse   26 Aug 13 07:35 home_id
-rw------- 1 homesynapse homesynapse 1208 Jul  9 22:26 homesynapse.yaml
-rw-r--r-- 1 homesynapse homesynapse   44 Aug 13 07:35 initial_api_token
drwx------ 2 homesynapse homesynapse 4096 Aug 30 08:58 integrations
drwxr-xr-x 2 homesynapse homesynapse 4096 Aug 13 07:35 schemas

/var/lib/homesynapse/config/integrations/:
total 12
drwx------ 2 homesynapse homesynapse 4096 Aug 30 08:58 .
drwx------ 4 homesynapse homesynapse 4096 Aug 30 08:58 ..
-rw------- 1 homesynapse homesynapse  299 Jul 21 07:33 zigbee.yaml
1:serial_port: /dev/zigbee
2:channel: 20
3:adopt_devices:
=== [AMEND] why the stop reported 'failed' ===
SuccessExitStatus=
Result=exit-code
ExecMainCode=1
ExecMainStatus=143
```

**`panId` 30540 decimal = `0x774C`.** The decisive verification: `parameterStore.load()` now returns present, so `resumeOrForm()` takes the RESUME branch. **`ExecMainCode=1` is `CLD_EXITED`** — the process exited under its own control; it was not killed. This is the primary evidence for finding §6-B.

---

## A.7 — §7 the drop-in + §8 the coordinator PLUG

### A.7.1 The drop-in written (this text IS R-3b's spec, H13)

```
nick@hs-fresh:~ $ sudo mkdir -p /etc/systemd/system/homesynapse.service.d
sudo tee /etc/systemd/system/homesynapse.service.d/10-serial-coordinator.conf >/dev/null <<'EOF'
[Service]
PrivateDevices=no
DevicePolicy=closed
DeviceAllow=char-ttyUSB rw
DeviceAllow=char-ttyACM rw
SupplementaryGroups=dialout
EOF
sudo systemctl daemon-reload && echo "--- daemon reloaded ---" && systemctl cat homesynapse.service | tail -12
--- daemon reloaded ---
# instrument. Map: distribution/docs/boot-contract-map.md.

[Install]
WantedBy=multi-user.target

# /etc/systemd/system/homesynapse.service.d/10-serial-coordinator.conf
[Service]
PrivateDevices=no
DevicePolicy=closed
DeviceAllow=char-ttyUSB rw
DeviceAllow=char-ttyACM rw
SupplementaryGroups=dialout
```

**Operator note:** the first `systemctl show` was issued WITHOUT `--no-pager` and piped into `less`; the transcript filled with `ESCOC`/`ESCOD` arrow-key echoes. Re-read cleanly below. **`--no-pager` belongs on every `systemctl` in the packet, not only on `journalctl`.**

### A.7.2 [AMEND] the EFFECTIVE merged config + §8 the plug

**⏺ coordinator PLUGGED 08:07:08 CT = 09:07:08 ET** into hub 3-2.4 Port 2 (same port, verified against the pre-swap photo). **Fence duration 08:19:14 → 09:07:08 ET = 47 min 54 s.**

```
nick@hs-fresh:~ $ echo "=== the drop-in, clean re-read for the record ==="
systemctl show --no-pager -p PrivateDevices -p DevicePolicy -p DeviceAllow -p SupplementaryGroups homesynapse.service
echo "=== the coordinator ==="
sleep 3; sudo udevadm trigger && sleep 2 && lsusb | grep -i "10c4:ea60"; ls -l /dev/zigbee /dev/ttyUSB0; ls -l /dev/serial/by-id/ | grep -i sonoff; id homesynapse
=== the drop-in, clean re-read for the record ===
DevicePolicy=closed
DeviceAllow=char-rtc r
DeviceAllow=char-ttyACM rw
DeviceAllow=char-ttyUSB rw
SupplementaryGroups=dialout
PrivateDevices=no
=== the coordinator ===
Bus 003 Device 004: ID 10c4:ea60 Silicon Labs CP210x UART Bridge
crw-rw---- 1 root dialout 188, 0 Aug 30 09:08 /dev/ttyUSB0
lrwxrwxrwx 1 root root         7 Aug 30 09:07 /dev/zigbee -> ttyUSB0
lrwxrwxrwx 1 root root 13 Aug 30 09:07 usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 -> ../../ttyUSB0
uid=102(homesynapse) gid=105(homesynapse) groups=105(homesynapse)
```

**`Bus 003 Device 004` here vs `Device 011` on the bench** — the USB device number changed across the replug. See finding §8-A. **`DeviceAllow=char-rtc r` is NOT ours** — systemd's implied rule from the base unit's clock protection. **`dialout` correctly absent from `id homesynapse`** — the drop-in adds it at exec, not to the account.

---

## A.8 — §9 A-3 THE MEASURED BOOT

```
nick@hs-fresh:~ $ sudo -v
nick@hs-fresh:~ $ sudo systemctl reset-failed homesynapse.service
date -u +%H:%M:%SZ
sudo systemctl start homesynapse.service; echo "start rc=$?"
date -u +%H:%M:%SZ
sleep 60
systemctl is-active homesynapse.service; systemctl show --no-pager -p NRestarts -p Result homesynapse.service
echo "=== THE DISCRIMINATOR SET ==="
sudo journalctl -u homesynapse.service -b --no-pager --since "-6min" | grep -E "zigbee\.(port_identity_captured|transport_override|network_resumed|network_formed|network_parameter_mismatch|transport_unbound|transport_unsupported|transport_failed|device_cache_loaded|adopt_list_loaded|adoption_maps_rehydrated|device_relinked|device_proposed|proposal_accepted|device_adopted|device_announce|permit_join_opened|ncp_configured)|registry\.projection_live|EPERM|Permission denied|SerialPort|ASH|NETWORK_UP" | head -60
13:12:19Z
start rc=0
13:12:23Z
active
Result=success
NRestarts=0
=== THE DISCRIMINATOR SET ===
Aug 30 09:12:21 hs-fresh homesynapse[2231]: 09:12:21.208 [hs-sub-registry_projection] INFO  c.h.l.RegistryProjectionSubscriber -- registry.projection_live: devices=0 entities=0 position=0
Aug 30 09:12:21 hs-fresh homesynapse[2231]: 09:12:21.726 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeDeviceCache -- zigbee.device_cache_loaded: 6 devices from /var/lib/homesynapse/data/zigbee/zigbee-devices.json
Aug 30 09:12:21 hs-fresh homesynapse[2231]: 09:12:21.728 [integration-supervisor-start] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.adoption_maps_rehydrated: devices=0
Aug 30 09:12:29 hs-fresh homesynapse[2231]: 09:12:29.307 [integration-zigbee-0] INFO  c.h.integration.zigbee.AshSession -- ASH session connected: ashVersion=2 resetCode=0xb
Aug 30 09:12:29 hs-fresh homesynapse[2231]: 09:12:29.310 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.port_identity_captured: stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false
Aug 30 09:12:29 hs-fresh homesynapse[2231]: 09:12:29.400 [integration-zigbee-0] INFO  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.ncp_configured: zdo_flags=0x3 stack_profile=2 security_level=5
Aug 30 09:12:29 hs-fresh homesynapse[2231]: 09:12:29.427 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
Aug 30 09:12:29 hs-fresh homesynapse[2231]: 09:12:29.427 [integration-zigbee-0] INFO  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.network_up: stackStatusHandler reported EMBER_NETWORK_UP (buffered)
```

**ABSENT and significant:** zero `device_relinked` · zero `device_proposed` / `proposal_accepted` / `device_adopted` / `device_announce` · zero `permit_join_opened` · zero `adopt_list_loaded` (DEBUG, expected) · zero `EPERM` / `Permission denied` / `transport_unbound` / `transport_unsupported` / `network_formed` / `network_parameter_mismatch`.


---
---

# APPENDIX B — SOURCE VERIFICATION (the 2026-08-29 desk audit, read-only at the artifacts)

Method: `git show <sha>:<path>` and `git grep <sha>` only. No checkout, no working-tree touch. Core porcelain verified **EMPTY at `5051fa5`** before and after. Shas present and read: `dec35be`, `7c9e4fa`, `e845cd9`, `5051fa5`.

**B.1 — `distribution/systemd/homesynapse.service:53` @ `dec35be`** (verified byte-identical on the running card at §4):
```
ExecStartPost=/opt/homesynapse/libexec/health-probe.sh --wait --timeout 90 --health-path /health
```

**B.2 — the same unit's sandbox ground @ `dec35be`:**
```
19:StartLimitIntervalSec=300      20:StartLimitBurst=5        23:Type=exec
24:User=homesynapse               25:Group=homesynapse        44:ExecStart=/opt/homesynapse/bin/homesynapse
64:Restart=on-failure             65:RestartSec=10            66:RestartPreventExitStatus=10
89:SystemCallFilter=@system-service    90:SystemCallErrorNumber=EPERM    96:PrivateDevices=yes
```
**No `SuccessExitStatus` anywhere in the unit** — the primary source evidence for finding §6-B.

**B.3 — the in-source RAMP comment @ `dec35be` (lines 91–96)** — the basis for F-A5 / finding §8-A:
```
# RAMP (post-M9): the Zigbee coordinator is a serial device. PrivateDevices=yes
# blocks /dev access, so loosen it then and allowlist the coordinator, e.g.:
#   PrivateDevices=no
#   DeviceAllow=/dev/ttyUSB0 rw          ← a NODE PATH; the packet chose the CLASS form instead
#   SupplementaryGroups=dialout
PrivateDevices=yes
```

**B.4 — `distribution/smoke/health-probe.sh`, both commits.** Defaults identical at `7c9e4fa` and `dec35be`:
```
22:HOST="127.0.0.1"   23:PORT="7070"   24:HEALTH_PATH="/api/v1/entities"
25:TOKEN_FILE="/var/lib/homesynapse/config/initial_api_token"
55:log() { printf '[health-probe] %s\n' "$*" >&2; }
 97:  log "token not yet available at ${TOKEN_FILE}"
102:  200) log "ready (200) at ${URL}"; return 0 ;;
114:  log "waiting up to ${TIMEOUT}s for readiness at ${URL}"
123:  log "TIMEOUT after ${TIMEOUT}s — service did not become ready"
```
**A full diff `7c9e4fa` → `dec35be` returned ZERO non-comment lines.** The probe binary is comments-only different between the two commits. **Therefore the entire E3 RED↔GREEN delta is the unit's `ExecStartPost` line** — the single-variable claim in the §5 result rests on this.
`7c9e4fa`'s unit line, for contrast (verified live at §2 via F-A4): `50:ExecStartPost=/opt/homesynapse/libexec/health-probe.sh --wait --timeout 90`

**B.5 — `ZigbeeIntegrationAdapter.resumeOrForm()` @ `dec35be`** — the §6 gate's whole justification:
```java
/**
 * §5.2 resume-or-form: stored parameters present → RESUME (a mismatch or
 * missing key custody propagates PERMANENT — never adopt a wrong network,
 * never silently re-form over corrupt custody: never-false-ALIVE); absent
 * (first run) → form with the §5.4 hashed-TCLK security state and persist …
 */
void resumeOrForm() throws PermanentIntegrationException {
    if (parameterStore.load().isPresent()) {
        NetworkParameters resumed = protocol.resumeStored();
        log.info("zigbee.network_resumed: channel={} panId=0x{}", resumed.channel(), Integer.toHexString(resumed.panId()));
    } else {
        NetworkParameters formed = formNetwork();
        log.info("zigbee.network_formed: channel={} panId=0x{}", formed.channel(), Integer.toHexString(formed.panId()));
    }
}
```
`Integer.toHexString` → lowercase, unpadded → `panId=0x774c`. Confirmed live at §9.

**B.6 — the adapter start sequence @ `dec35be`** — the basis for the F-A2 investigation:
```java
PortCandidate port = resolvePort();
bindTransport(port);
protocol.startSession();
resumeOrForm();
protocol.awaitNetworkUp();
log.info("zigbee.production_session_started: …");
openPermitJoinWindow();   // ← runs on BOTH the resume and form paths
productionLoop();
```
`openPermitJoinWindow()` returns immediately when `permit_join_duration` is absent ("conservative default: no key ⇒ the window NEVER opens"). Config keys: `PERMIT_JOIN_DURATION_KEY="permit_join_duration"` · `CHANNEL_KEY="channel"` · `ADOPT_DEVICES_KEY="adopt_devices"`. `formNetwork()` honours a present, in-range `channel` and **skips the energy scan** — the basis for the P-d re-pricing that F-A2 raised and then withdrew.

**B.7 — log level of every §9 discriminator token @ `dec35be`:**
```
port_identity_captured info · transport_override info · network_resumed info · network_formed info
network_parameter_mismatch warn · transport_failed warn · device_cache_loaded info
adopt_list_loaded DEBUG ←←← the only DEBUG token in the packet's §9 grep (finding F-A1)
adoption_maps_rehydrated info · device_relinked info · device_proposed info · proposal_accepted info
device_adopted info · device_announce info · permit_join_opened info · registry.projection_live info
transport_unbound / transport_unsupported → PermanentIntegrationException CODES, not log calls (F-A3)
```
All 17 tokens exist in the sources — the §9 grep is not blind.

**B.8 — `distribution/common.sh:57 hs_version()` @ `dec35be`** — H12's derivation: a bare id is wrapped as `0.1.0+git<YYYYMMDD.HHMMSS>.g<id>` from the committer date in UTC; a Debian Version must start with a digit, so a bare id sorts as a NUMBER above every `0.x.y` (hence `--allow-downgrades` exactly once), and `+git…` sorts above every `+g…` because `g` is a proper prefix of `git`.

---
---

# APPENDIX C — THE AMENDMENT LEDGER

Every deviation from the packet as written, with its outcome. **Recommendations marked ★ should be folded into the packet permanently.**

| # | Where | Amendment | Outcome |
|---|---|---|---|
| F-A1 | §9 | `adopt_list_loaded` is DEBUG; absence ≠ failure | ★ CONFIRMED — zero lines, correctly read as expected |
| F-A2 | §1, §6, §9 | grep `permit_join`; be ready to remove the key before §8 | ★ CLOSED FOUND-SAFE — key absent at all three checks; **no operator action was needed**; the P-d escalation was withdrawn on evidence |
| F-A3 | §9 | expect P-c before P-b on a pinned-port rig | Not exercised — P-a fired. Reasoning stands unrefuted |
| F-A4 | §2 | check the INSTALLED unit's `ExecStartPost` before §3 | ★ CONFIRMED — `--wait --timeout 90`, no `--health-path`; E3-RED made falsifiable for the right reason |
| F-A5 | R-3b | the source RAMP comment recommends a node path; R-3b must update it | ★ STRENGTHENED by finding §8-A — the device number changed across the replug, so the class rule is now measured-justified |
| — | §0 | read the overnight nightly digest before taking the bench down | ★ GREEN; also supplied the §9 reference trace |
| — | §1 | capture the F-S20 by-id string from the LIVE bench pre-swap | ★ Turned §11's gate from "compare to a document" into "compare to the measured before" |
| — | §1 | parse-check both JSONs INSIDE the custody tarball | ★ Hazard proved REAL (cache mtime moved 08:01→08:05 mid-capture) |
| — | §1 | pull §4 I-1's artifact confirm forward while the bench was still up | ★ An artifact fault would have surfaced with the rig intact |
| — | §4 | split I-3's baseline from the install so `integrity_check` can actually gate | ★ Finding §4-B |
| — | §3 | unconditional journal re-read after the `&&` chain | ★ The packet's chain stops on a non-active unit, blinding the reader exactly when it matters |
| — | §6 | wrap the lay-down in an explicit stop-guard | ★ The packet's `mv` would run even if the stop failed |
| — | §6 | aside dir named `-2026-08-30`, not the packet's `-2026-08-29` | DEVIATION, deliberate — stamped with the date of the act |
| — | §7 | verify with `systemctl show` (effective config), not `cat` (file text) | ★ Also surfaced the un-authored `DeviceAllow=char-rtc r` |
| — | all | `--no-pager` on **every** `systemctl`, not only `journalctl` | ★ One block was lost to the pager |
| — | §9 | `reset-failed` before `start` | ★ Needed because of finding §6-B; gives a clean `NRestarts`/`Result` |
| — | §9 | grep gains `permit_join_opened` and `ncp_configured` | ★ Both observed-either-way; `ncp_configured` matched the bench signature |

---

# THE CARD'S CURRENT STATE (resume point)

- **Held card `hs-fresh`** — powered ON, service `active`, `NRestarts=0`, `Result=success`.
- **Artifact:** `0.1.0+git20260823.231355.gdec35be` (dpkg == `/opt/homesynapse/VERSION`).
- **Unit:** R-9's, `--health-path /health`, plus the §7 drop-in at `/etc/systemd/system/homesynapse.service.d/10-serial-coordinator.conf`.
- **Custody:** the BENCH clone in `data/zigbee/` (PAN 0x774c, channel 20). The card's own pre-clone dir preserved at `data/zigbee.held-pre-r3-2026-08-30/` (one 38-byte file).
- **Config:** the bench `homesynapse.yaml` + `integrations/zigbee.yaml` present; the card's own token pair and `home_id 01KZXEG38VC0ZT375GZ3H1P5QS` untouched.
- **Token artifact:** PRESENT, restored, `-rw-r--r--` 44 B.
- **Coordinator:** PLUGGED since 09:07:08 ET, hub 3-2.4 Port 2, `/dev/zigbee -> ttyUSB0`.
- **Zigbee:** network RESUMED on channel 20 / PAN 0x774c. **Fleet NOT yet adopted** — 0 rehydrated, awaiting device announce (P-f).
- **Events:** 24 rows at the last count, `integrity_check ok`.
- **Bench card:** OUT of its slot, powered off, since 08:19:14 ET. **The bench is DOWN and must be restored by §11 before Mon 03:00 CT / 04:00 ET.**
- **Remaining:** §10 the evidence window (≥30 min) → §11 the restore.


## §10 A-4 THE EVIDENCE WINDOW — *in progress*

**ROWS-W0 = 27 at 15:09:52Z (11:09:52 ET).** Rows moved 24 → 27 (+3) across the §9 start. Fleet token counts at W0: **EMPTY** — zero `device_relinked` / `device_proposed` / `proposal_accepted` / `device_adopted` / `device_announce`. The P-f arm is confirmed as the operative one.

### ⏺ FINDING §10-A — THE DASHBOARD CONFIRMS §9-B VISUALLY, AND STAYS HONEST DOING IT

Dashboard at `http://127.0.0.1:7070/dashboard/#/overview` via the SSH tunnel, ~11:07 ET:

```
All running — HomeSynapse is live and watching your home in real time.     [Live]
Recent runs:  No automation runs yet.
Devices:      Available          0 of 0
              Offline            none
              Not determined yet none
              Stale readings     none
              "Counts reflect each device's last report — not a live connection test."
```

**`Available 0 of 0` — the DENOMINATOR is zero.** The registry holds no devices at all. This is the visual proof of §9-B: the custody clone resumed the Zigbee network (channel 20 / PAN 0x774c, §9) while the HomeSynapse registry stayed empty, because adoption identity lives in the event store, which was correctly not cloned.

**The packet's §10 expectation — "expect 5 Available + 1 Unavailable, each with a fresh `Last reported`" — is REFUTED at the surface, not merely unreached.** It cannot be met on a cloned-custody card by any amount of waiting.

**Positive finding inside the negative one:** the UI did not fabricate a fleet. It reported `0 of 0`, `none`, `none`, `none`, and `No automation runs yet` — every honest empty. The `All running` banner and `Live` stream indicator are simultaneously correct: the engine IS healthy; it simply has nothing adopted. Under a condition no one designed for, the never-false-ALIVE posture held at the presentation layer. **This is positive evidence for the FE lane's explainability contract and should be banked as such**, alongside the microcopy "Counts reflect each device's last report — not a live connection test", which correctly refuses to imply liveness it has not measured.

**⏺ finding §4-C reinforced on a second surface.** `sudo homesynapse-token` prints: *"Pair a client with this token, then delete the file: `sudo rm /var/lib/homesynapse/config/initial_api_token`"*. The delete-the-token advice appears in BOTH the postinst banner and the token helper. Under `7c9e4fa` both were instructions into the §3 failure. R-9 is what makes both honest.


### §10 EVENT — THE MOTION SENSOR LEFT THE NETWORK (operator act, 11:43:01 ET)

**Sequence.** ROWS-W0 27 @ 15:09:52Z. A wave probe at ~15:15Z produced **zero** journal activity and rows unchanged at 27. Escalating to the packet's P-f probe, the operator went to power-cycle the SNZB-03P and **held the button past the ~5 s threshold**, which on that device is a network-leave-and-enter-pairing, not a power cycle. The device began flashing (hunting for a network).

```
Aug 30 11:43:01 hs-fresh homesynapse[2231]: 11:43:01.782 [integration-zigbee-0] INFO
  c.h.i.zigbee.ZclIngestionUnit -- zigbee.device_left: device=0xF044D3FFFE9C78D7 nwk=0x1955
```
Rows remained **27** — `device_left` from an unregistered device logs but appends no event row.

`0xF044D3FFFE9C78D7` is the SNZB-03P motion sensor (identified from the bench trace at A.0; bench deviceId `01KX1PB9A5931A8G0F0X03QXT2`). **It is off the bench's Zigbee network and cannot rejoin: no permit-join window is open on either card** (F-A2 — the key is absent from the bench config and therefore from the clone).

### ⏺ FINDING §10-B — NO SILENT-DROP PROBLEM; AND INDEPENDENT CONFIRMATION OF §9-B

The open question at §10 was whether the earlier silence meant **(a)** nothing transmitted or **(b)** traffic arrived and the adapter dropped it without logging. **Answer: (a).** The adapter logged `device_left` at **INFO** for a device with **zero registry presence** — so unknown-device traffic IS surfaced, and the preceding silence was simply an absence of transmissions. No silent-drop defect exists. Positive finding.

**And a device can only LEAVE a network it was ON.** This independently confirms §9-B from the opposite direction: the custody clone genuinely carried Zigbee-layer membership (the sensor was a member of PAN 0x774c under the held card's coordinator), while the HomeSynapse registry stayed empty. Zigbee layer transferred; application layer did not. The model is now confirmed by two independent observations.

### ⏺ §10-C — `bench-hero` IS PRESENT AND `On` (criterion (4) is NOT structurally unreachable)

Dashboard → Automations: **`bench-hero`** listed, **State `On`**, shape `state change trigger · command action · delay action · command action · delay action · command action · delay action · command action · delay action · command action`, with a live `Why didn't it?` explain affordance. Dashboard → Devices: **"No devices paired yet."**

So the automation DID travel with the clone. **R-4 criterion (4) is blocked on the same missing adoption as criterion (2), not on a missing automation.** Recovering one device unblocks both. Note also that the `Why didn't it?` affordance is present and live on an automation that has never run — the explainability surface is available for the negative case, which is the harder half of the FE contract.

### SOURCE CHECK RUN BEFORE ESCALATING — hashed TCLK, no key-divergence risk

Before recommending where to re-pair, the guide verified at `dec35be` whether per-device link keys are persisted host-side (which would make a re-pair on the held card diverge that card's `secrets.enc` from the bench's and potentially break the device on the bench):
```
* each device its seed-derived hashed TCLK, exactly the bellows posture
* generated TCLK seed (each loaded from custody or minted fresh)
private static final int TCLK_SEED_LENGTH_BYTES = 16;
```
**HomeSynapse runs hashed TCLK: per-device keys are DERIVED from one 16-byte seed plus the device address, not stored per device.** The seed is in `secrets.enc`, which is byte-identical on both cards (cloned; hash `ccface0e…`). **A re-pair on the held card therefore derives exactly the key the bench derives. No divergence risk.** The concern was real enough to check and resolves in favour of either location being key-safe.

### ⏺ ESCALATED TO THE HUB — §10 HELD PENDING A RULING

The operator declined to choose the re-pair location at the bench and escalated. See the decision card: `_scratch/2026-08-30_R3a_ESCALATION_fleet-repair-ruling_card.md`.

**Holding state at escalation (11:50 ET):** held card powered, service `active`, network resumed on PAN 0x774c, registry empty, sensor off-network, no permit-join window anywhere, bench card OUT since 08:19:14 ET. Nothing is time-critical except the bench floor.


---

## §10 (continued) — THE POWER OUTAGE, AN UNPLANNED DURABILITY TEST

**Event.** Mains power failed at Nick's location at approximately 12:20 ET while §10 was held pending the hub's ruling. The held card lost power with the coordinator live and the service running — an **uncontrolled shutdown**, unscripted by the packet. The Pi rebooted unattended at **12:24:15 ET** and, because the unit is `WantedBy=multi-user.target`, the service auto-started and ran its full boot sequence with nobody watching.

**Clock note:** `uptime -s` reports 12:34:07 while the first journal entry is 12:24:15. The Pi has no RTC, so it boots with a stale clock which NTP then corrects forward. **Timestamps in the first minutes after a cold boot on this hardware are approximate** — worth knowing before anyone reasons hard about a post-outage timeline.

### ⏺ FINDING §10-D — THE PACKAGED ARTIFACT SURVIVED AN UNCONTROLLED POWER LOSS, COLD

Post-outage boot, unsupervised, with the radio present:
```
12:24:27.231  registry.projection_live: devices=0 entities=0 position=0
12:24:27.830  zigbee.device_cache_loaded: 0 devices from …/zigbee-devices.json
12:24:27.832  zigbee.adoption_maps_rehydrated: devices=0
12:24:35.613  zigbee.port_identity_captured: stableId=…MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false
12:24:35.744  zigbee.network_resumed: channel=20 panId=0x774c
```
`active` · `Result=success` · `NRestarts=0` · `ExecMainStatus=0` · `ExecStartPost … code=exited status=0` (ran 12:24:24 → 12:24:29).

**NO `network_formed`. The custody survived and `resumeOrForm()` took the RESUME branch on an unattended cold boot.** `zigbee-network.json` intact at 122 B / Jul 18 / `panId 30540 = 0x774c`. `integrity_check` **ok**. Rows **27 → 33** (grew; no loss). Artifact still `0.1.0+git20260823.231355.gdec35be` in both places. The §7 drop-in still merged (`PrivateDevices=no`, `DevicePolicy=closed`, both class rules, `SupplementaryGroups=dialout`). Coordinator re-enumerated with the by-id string still byte-identical.

**This is an unplanned but genuine durability test of the class an always-on home hub must survive, and the packaged artifact passed it cold with no operator present.** The packet never thought to script it. **Recommend R-4 adopt an uncontrolled-power-loss leg deliberately** — it is cheap (pull the plug), it exercises SQLite WAL recovery, custody survival and the resume-vs-form branch simultaneously, and today it produced more evidence in four minutes than the scripted wave probe produced in thirty.

### ⏺ FINDING §10-E — THE APPLICATION DESTROYS THE CLONED DEVICE CACHE

`zigbee-devices.json` on the held card, before and after:
```
at the clone (§6):   4551 B   mode 0600   (6 devices — device_cache_loaded: 6 at 09:12)
post-outage boot:       ?     ...         device_cache_loaded: 0 devices
now:                  845 B   mode 0644   (devices list len=1 — the one re-adopted device)
```
**The mode changed 0600 → 0644.** A power-loss truncation preserves the inode and its mode; a 644 file means **the application rewrote it** under its own umask. So this was not outage corruption — HomeSynapse overwrote the cloned 6-device cache with its own, and the post-outage boot then loaded zero devices from it.

Cache structure now: `{version: int, devices: list(len=1), learnedZoneTypes: dict(len=1)}`.

**No permanent loss:** the 4551 B original survives in the custody tarball on all three machines (`268be10e…`) and in the bench's own powered-off card. **But the operational consequence for R-4 is real: a cloned-custody rig destroys its cloned cache on first run, so the rig is not re-runnable without re-cloning.** The precise trigger (a periodic flush of an emptied in-memory cache, versus a reconciliation that prunes cache entries lacking a registry counterpart) is **NOT established** — it is inferred from the mode change and the load counts. **Recommend the hub commission a source read before this is treated as characterised.**

### ⏺ FINDING §10-F — **THE FULL P-e RE-ADOPTION CHAIN, MEASURED ON THE PACKAGED ARTIFACT**

The outage power-cycled the mains fleet. At 12:37:58 one device performed a **`SECURED_REJOIN`** — which requires **no permit-join window**, because a device holding valid network keys rejoins on its own authority — and the complete adoption chain ran end to end:

```
12:37:58.330  zigbee.device_join: device=0x449FDAFFFE688F57 nwk=0xcee2 status=SECURED_REJOIN decision=NO_ACTION
12:37:58.552  zigbee.device_announce: device=0x449FDAFFFE688F57 nwk=0xcee2
12:37:59.325  zigbee.device_proposed: device=0x449FDAFFFE688F57 manufacturer=eWeLink model=SNZB-04P profile=sonoff_snzb_04p status=COMPLETE
12:37:59.326  zigbee.proposal_accepted: device=0x449FDAFFFE688F57 source=config
12:37:59.424  zigbee.device_adopted: device=0x449FDAFFFE688F57 deviceId=01M19RHWWZXKD4MWM66KAW8MSR entities=1
12:38:00.312  zigbee.reporting_configured: device=0x449FDAFFFE688F57 clusters=2 verified=1 degraded=1
12:38:08.542  zigbee.ias_zone_enrolled: device=0x449FDAFFFE688F57 endpoint=1 zoneId=0
```

**Announce → IAS-enrolled in 10.0 seconds** on the packaged `+git` artifact under the §7 drop-in.

**`proposal_accepted: source=config` is the decisive token.** The cloned `adopt_devices` list drove the auto-adoption — the exact mechanism §9-B predicted would be the *only* path available on a cloned-custody rig. **A refutation filed this morning, proven on silicon this afternoon, without a single deliberate act.**

**The new `deviceId=01M19RHWWZXKD4MWM66KAW8MSR` differs from the bench's `01KY12MQVQ204M1VP39F1ZDM33` for the same IEEE address** (bench trace, A.0). This is §9-B made concrete: the device is re-adopted with a **fresh application identity**, because adoption records never travelled with the custody. R-4 must expect new ULIDs on a cloned rig, and any criterion keyed to bench deviceIds will not hold.

`reporting_configured: clusters=2 verified=1 degraded=1` is the known sleepy-device Configure-Reporting posture (honest BEST_EFFORT per the M9.4 acceptance record), not a defect. The device is the **SNZB-04P contact sensor** — NOT the motion sensor, which remains off-network.

**Fleet state:** 1 of 6 re-adopted (0x449FDAFFFE688F57). 1 of 6 off-network entirely (0xF044D3FFFE9C78D7, the SNZB-03P motion sensor). 4 of 6 silent — no `device_join` logged for them.


### §10 DASHBOARD STATE AFTER THE RE-ADOPTION (~13:40 ET, via the SSH tunnel)

**Overview:** `All running` · `Live` · **Devices: Available `1 of 1`**, Offline none, Not determined yet none, Stale readings none · **Recent runs: "No automation runs yet."**
**Devices list:** one row — `01M19RHWXYZYJMM26SX0E41HXN` · Status **`Available`** · Reading **`Current`**
**Device detail panel:** `✓ Available` · *"Available — the time of the last report is not recorded."* · Battery Pct **—** · Last changed **—** · Last reported **—**
**Automations:** `bench-hero`, State `On`, `Why didn't it?` live.
**Explain surface** (`/dashboard/#/explain/why-not/01M19QS3VR7KJ47J2S…`): badge **"Nothing set it off"** · *"Automation 'bench-hero' has not been triggered; it fires on state change."* · "What would make it run" → **"state change"**.

**Operator act:** Nick waved at the motion sensor after these screenshots. **Nothing changed** — correct and confirmatory: `0xF044D3FFFE9C78D7` left the network at 11:43:01 and is not a member, so it cannot report.

### ⏺ FINDING §10-G — R-4 CRITERION (2) IS **PARTIALLY** MET; DO NOT SCORE IT AS MET

R-4 criterion (2) is *"≥1 device Available **with a fresh `Last reported`**"*. Observed: **`Available` = yes; `Last reported` = EMPTY**, with the detail panel stating plainly *"the time of the last report is not recorded."*

So the availability half holds and the freshness half does not. **Scored PARTIAL.** Either `Available` here derives from adoption/IAS-enrollment rather than from an observed report, or the report time is not persisted on this path. Which of those it is has NOT been established and should not be guessed. The UI's honesty is intact — it declines to fabricate a timestamp — but the criterion as written is not satisfied.

### ⏺ FINDING §10-H — THE DEVICES PAGE SHOWS AN ID THE JOURNAL NEVER LOGS

Journal: `zigbee.device_adopted: device=0x449FDAFFFE688F57 **deviceId=01M19RHWWZXKD4MWM66KAW8MSR** entities=1`
Dashboard Devices list AND detail header: **`01M19RHWXYZYJMM26SX0E41HXN`**

These share the ULID time prefix `01M19RHW` but differ in the random component — **two distinct ULIDs minted moments apart.** Since the adoption reported `entities=1`, the dashboard is almost certainly displaying the **entity** ULID under a column headed `DEVICE`. Benign in itself, but it means **an operator cannot correlate a dashboard row to a `device_adopted` log line by the identifier shown**, which is precisely the correlation an observability dashboard exists to support. **FE-lane item:** either surface the deviceId, or label the column for what it holds.

### ⏺ FINDING §10-I — THE LIST CLAIMS A FRESHNESS THE DETAIL PANEL DISCLAIMS

The Devices **list** renders Reading = **`Current`**. The **detail panel** for the same device says *"the time of the last report is not recorded"*, with `Last reported` blank. The Overview tile's own microcopy says *"Counts reflect each device's last report — not a live connection test."*

**`Current` is a freshness claim with no timestamp behind it, on a device whose report time the system explicitly says it does not have.** The detail panel is honest; the list is not, and the tile's microcopy describes a basis the data does not supply. This is a never-false-ALIVE surface inconsistency of the same family as the M9.4 `key_establishment_failed` misclassification — a claim asserted through a channel whose evidence is absent. **Recommend the FE lane render an explicit unknown (an em-dash or "not yet reported") rather than `Current` when no report time exists.**

### ⏺ FINDING §10-J — THE NEGATIVE-CASE EXPLANATION RENDERS, AND IS HONEST, BUT IS NOT ACTIONABLE

The explainability hero's harder half — *why didn't it happen* — **works on the packaged artifact**, on an automation that has genuinely never run, and says so without inventing a cause: badge "Nothing set it off", body *"Automation 'bench-hero' has not been triggered; it fires on state change."*

**But "What would make it run" answers "state change" — which restates the trigger TYPE and names neither the entity nor the condition.** On a six-device bench that is not enough for an operator to act on; the product promise is plain-language *why*, and this is a restatement of the rule's shape. **Positive:** the surface exists, is live, and is honest. **Gap:** it should name the specific entity and state transition it is waiting for. **FE-lane item, and directly relevant to R-4's criterion (4)**, which asks for a *rendered explanation* — today's negative-case rendering would satisfy the letter and not the spirit.


### ⏺ FINDING §10-K — THE WRITE PATH PROVEN END-TO-END ON REAL SILICON

The contact-sensor magnet test appended exactly two rows with correct provenance:
```
35  state_changed    ENTITY  seq 4  origin=SYSTEM              event_time 1788111478788377
34  state_reported   ENTITY  seq 3  origin=DEVICE_AUTONOMOUS   event_time 1788111478788377
33  device_adopted   DEVICE  seq 2  origin=INTEGRATION
```
A real device reported autonomously; HomeSynapse ingested it, derived a state change, and committed both — `DEVICE_AUTONOMOUS` for the raw report, `SYSTEM` for the derivation. **This is the assertion CI's run-smoke check 4 makes on a clean runner, now demonstrated with real hardware through the packaged `+git` artifact under the drop-in.** Ingest latency (ingest_time − event_time) = **14.2 ms**.

**THE EVENT-TYPE CENSUS at 35 rows** — the day's whole write path:
```
integration_started         15      availability_changed  1     state_changed   1
integration_health_changed  13      device_adopted        1     state_reported  1
                                    device_discovered     1
                                    device_registered     1
                                    entity_registered     1
```
**28 of 35 rows are lifecycle chatter** (`integration_started` + `integration_health_changed`) — this is the decomposition behind the packet's "≈4 rows per boot" figure and refines finding §4's two-rate model with the actual constituents. **One adoption costs exactly four rows**: `device_discovered` → `device_registered` → `entity_registered` → `device_adopted`.

**THE `adopt_devices` ROSTER (the fleet, named):**
```
0x00178801101A09BB  Hue LCA017        MAINS
0x00124B002FA8D1C5  S31 Lite zb       MAINS
0xF044D3FFFE9C78D7  SNZB-03P          battery — the motion sensor that LEFT at 11:43
0xF044D3FFFED2A201  SNZB-02P          battery
0xF044D3FFFE1C1E8E  SNZB-01P          battery
0x449FDAFFFE688F57  SNZB-04P contact   battery — the one that self-recovered
```
**The device that self-recovered is BATTERY-powered and did not power-cycle.** It rejoined because its *parent* vanished during the outage and it initiated a `SECURED_REJOIN` when the coordinator returned. So the four still-silent devices may yet recover on their own poll cycles — a mechanism worth R-4 knowing.

### ⏺ FINDING §10-G **SHARPENED** — THE DEFECT IS IN THE READ PATH, NOT THE WRITE PATH

The census shows `availability_changed = 1` AND `state_reported = 1`. **The store holds both an availability event and a state report for the device whose `Last reported` the UI renders as empty.** So the earlier ambiguity resolves: it is NOT that the system lacks the report time. **The system has it and does not surface it.** This relocates the defect from Core to the **read-API / FE contract**, and makes it directly actionable for the frontend lane rather than a Core investigation.

### ⏺ FINDING §9-B **CONFIRMED BY CONSTRUCTION** — a controlled test, predicted then run

Prediction filed BEFORE the restart (guide, §10): *"This morning the cache loaded 6 and rehydrated 0 because the registry was empty. If §9-B's mechanism is right — rehydration matches the cache against the REGISTRY — then now that exactly one device has a real adoption record, we should see 1 and 1, with a relink. If we instead see rehydrated: 0 again, my model is wrong."*

| | cache loaded | registry | rehydrated | relinks |
|---|---|---|---|---|
| **09:12** (post-clone, empty registry) | **6** | 0 | **0** | **0** |
| **14:06** (one real adoption in the store) | **1** | 1 | **1** | **1** |

```
14:06:22.209  zigbee.device_relinked: device=0x449FDAFFFE688F57 deviceId=01M19RHWWZXKD4MWM66KAW8MSR — re-pairing, no new adoption
14:06:22.210  zigbee.adoption_maps_rehydrated: devices=1
```
**The registry was the only variable that changed and the outcome moved exactly as predicted.** §9-B is no longer an inference from a refutation — it is a model that made a falsifiable forecast and survived it. **The custody clone transfers the Zigbee network; adoption identity lives in the event store and does not travel. R-4 must plan for re-adoption.**

**This also settles finding §10-H definitively:** the relink reuses `deviceId=01M19RHWWZXKD4MWM66KAW8MSR`, identical to the `device_adopted` line at 12:37:59. The dashboard's `01M19RHWXYZYJMM26SX0E41HXN` is therefore the **entity** ULID rendered under a column headed `DEVICE`.

### §10 THE `RIG` RE-PAIR (hub-ruled, executed 14:06 ET)

**Hub ruling received: `RIG`.** Executed per the card's §5: the cloned `integrations/zigbee.yaml` was backed up to `zigbee.yaml.pre-repair-2026-08-30` (delete-nothing), `permit_join_duration: 180` appended at column 0 (verified by read-back BEFORE any restart — the file drives the radio), then a restart.

```
14:06:29.907  zigbee.tc_joins_enabled: join policy set; wildcard well-known transient link key installed
              (stack-bounded lifetime — expected to self-expire with the join window)
14:06:29.915  zigbee.permit_join_opened: duration=180s
```
180 s chosen deliberately: long enough to hold the button, short enough to self-close. Spec max is 254. **The key MUST be removed and the service restarted after the join — the M9.4 runbook step-18 posture.**

Operator report: the sensor's LED blinked on the button press then **went solid**, the physical indication of a successful join.


### §10 THE MOTION SENSOR RE-PAIRED — the full fresh-join chain (14:07 ET)

```
14:07:10.697  zigbee.device_join: device=0xF044D3FFFE9C78D7 nwk=0x330a status=UNSECURED_JOIN decision=USE_PRECONFIGURED_KEY
14:07:10.734  zigbee.child_join: child=0xF044D3FFFE9C78D7 nwk=0x330a type=SLEEPY_END_DEVICE
14:07:10.748  zigbee.device_announce: device=0xF044D3FFFE9C78D7 nwk=0x330a
14:07:11.515  zigbee.device_proposed: manufacturer=eWeLink model=SNZB-03P profile=sonoff_snzb_03p status=COMPLETE
14:07:11.516  zigbee.proposal_accepted: device=0xF044D3FFFE9C78D7 source=config
14:07:11.594  zigbee.device_adopted: deviceId=01M19XN7MXFBA3P5BT4VDY0BM6 entities=1
14:07:13.282  zigbee.reporting_configured: clusters=3 verified=2 degraded=1
14:07:13.295  zigbee.key_established: status=TC_REQUESTER_VERIFY_KEY_SUCCESS
14:07:20.731  zigbee.ias_zone_enrolled: endpoint=1 zoneId=0
```
**Join → IAS-enrolled in 10.0 s.** `UNSECURED_JOIN/USE_PRECONFIGURED_KEY` — a genuine fresh join (contrast the contact sensor's `SECURED_REJOIN`), correct for a device that had left. **New deviceId `01M19XN7MXFBA3P5BT4VDY0BM6`**, again confirming §9-B: re-adoption mints a fresh application identity. Operator report: the LED blinked on the press then went solid.

### ⏺ FINDING §10-L — **M9.4-KEYb APPEARS TO HAVE LANDED** (a guide prediction refuted, in the good direction)

**Prediction filed before the join:** per the M9.4 §B finding, a healthy TCLK exchange would emit a FALSE `key_establishment_failed status=TC_RESPONDED_TO_KEY_REQUEST` (0x06) as a WARN ~0.26 s before the real `key_established` (0x34), because the binary `established()`/else classifier did not anticipate the in-flight progress statuses `{0x06, 0x07, 0x0C}`.

**Observed: the false-failure pair did NOT appear.** This join logged **exactly one `key_established: status=TC_REQUESTER_VERIFY_KEY_SUCCESS` and zero `key_establishment_failed` for that device** — precisely the done-when M9.4-KEYb specified. **PREDICTION REFUTED; the fix appears to have landed.** This is a free regression confirmation of M9.4-KEYb on the packaged artifact and hardware. **Recommend the hub verify at source and close the KEYb row if it is still open.**

### ⏺ FINDING §10-M — AN UNATTRIBUTABLE `key_establishment_failed` WARN (cause NOT established)

```
14:11:26.868  WARN  zigbee.key_establishment_failed: device=0xFFFFFFFFFFFFFFFF status=TC_REQUESTER_VERIFY_KEY_TIMEOUT
```
`0xFFFFFFFFFFFFFFFF` is the all-Fs sentinel — **an unattributable device**. Timing: ~2 min after the 180 s join window closed (opened 14:06:29), ~4 min after the motion sensor's key established cleanly. No device was harmed; both adopted devices are healthy.

**This is a WARN naming a failure for a device that does not exist — an operator cannot act on it.** A plausible cause is the wildcard transient link key self-expiring (the `tc_joins_enabled` line states it is "stack-bounded lifetime — expected to self-expire with the join window"), which would make this a **benign, expected event reported through a failure channel** — the same family as findings §6-B (clean shutdown → exit 143) and §10-I (`Current` with no timestamp). **But the timing does not line up exactly with the window close, so the cause is NOT ESTABLISHED and is not claimed. Recommend a source read before this is characterised.**

### §10 THE DOOR CLOSED — the join window removed (14:20 ET)

`integrations/zigbee.yaml` restored **verbatim from the backup** (`cp -a` of `zigbee.yaml.pre-repair-2026-08-30`) rather than edited in place. Verified by read-back: three keys, no `permit_join_duration`. Restart at 14:20:
```
14:20:41.281  zigbee.device_relinked: device=0xF044D3FFFE9C78D7 deviceId=01M19XN7MXFBA3P5BT4VDY0BM6 — re-pairing, no new adoption
14:20:41.282  zigbee.device_relinked: device=0x449FDAFFFE688F57 deviceId=01M19RHWWZXKD4MWM66KAW8MSR — re-pairing, no new adoption
14:20:41.282  zigbee.adoption_maps_rehydrated: devices=2
14:20:49.021  zigbee.network_resumed: channel=20 panId=0x774c
```
`active` · **NO `permit_join_opened`** · **NO `tc_joins_enabled`** · no `network_formed`. **The fence is back exactly where R-3a found it, which is the state the bench must inherit tonight.** The M9.4 runbook step-18 posture is honoured.

### ⏺ §9-B — THE THREE-POINT CONFIRMATION

| registry adoptions | cache loaded | rehydrated | relinks | when |
|---|---|---|---|---|
| **0** | 6 | **0** | **0** | 09:12 post-clone |
| **1** | 1 | **1** | **1** | 14:06 after the contact sensor |
| **2** | — | **2** | **2** | 14:20 after the motion sensor |

**Rehydration tracks the REGISTRY, not the cache — predicted before each observation, correct each time.** The custody clone transfers the Zigbee network; adoption identity lives in the event store and does not travel. This is now a model with three confirmed forecasts, not an inference.

### ⏺ FINDING §10-N — bench-hero DID NOT FIRE on a freshly-adopted, IAS-enrolled motion sensor

Dashboard after the wave: **`Available 2 of 2`** · **`Recent runs: No automation runs yet.`** · Ask why → `Why did something happen?` → **"No automation runs yet."** The event census shows `state_reported` risen to 4 and `state_changed` to 3 — **reports ARE arriving** — yet zero automation runs.

bench-hero is present, `On`, shaped `state change trigger · command action · delay action ×4 · command action`. It reached this card via **`homesynapse.yaml`** (the only vector — this card had no `homesynapse.yaml` before §6). **Leading hypothesis, NOT yet confirmed: the trigger binds to the BENCH's entity ULID for the motion sensor, which does not exist on this card** — because §9-B establishes re-adoption mints fresh entity identities. If so, **automations survive a custody clone as definitions but not as functioning rules, every entity reference inside them dangling** — §9-B extended one layer up, and decisive for whether R-4 criterion (4) is achievable on a cloned rig at all. **Pending: a read of `homesynapse.yaml` to see what the trigger actually binds to.**


### ⏺ FINDING §10-N **CONFIRMED** — AUTOMATIONS SURVIVE A CUSTODY CLONE AS TEXT, NOT AS RULES

`homesynapse.yaml` (cloned from the bench at §6) defines bench-hero:
```yaml
automation:
  automations:
    - name: bench-hero
      triggers:
        - type: state_change
          entity_ref: 01KX1PB9AAB4VB3E10BD477TV3      # a BENCH entity ULID
          attribute: occupied
          to: "true"
      actions:
        - type: command
          target: { entity_ref: 01KX1PA4HSJ581GASYB7DHE40F }   # another BENCH entity ULID
          command: turn_on
        - delay PT6S → set_brightness{level:50} → delay PT6S → set_color_temperature{4550}
        - delay PT2S → set_color_temperature{4525} → delay PT20S → identify{5s}
```
**Both `entity_ref`s are the BENCH's identities.** Prefix evidence: `01KX1PB9A…` matches the bench's motion-sensor deviceId `01KX1PB9A5931A8G0F0X03QXT2` (A.0), and `01KX1PA4H…` sits adjacent to the Hue's `01KX1PA4GRZHY2GD37B5CFVQHY`. **Neither exists on the held card** — the motion sensor was re-adopted as `01M19XN7MXFBA3P5BT4VDY0BM6` with a fresh entity, and the Hue was never re-adopted.

**CONSEQUENCE 1 — R-4 CRITERION (4) IS STRUCTURALLY UNREACHABLE ON A CLONED-CUSTODY RIG.** *"One automation run with a rendered explanation"* cannot be satisfied by any amount of device activity: the trigger references a nonexistent entity and all five actions target another. This is not a slow path or a missing device; it is a dangling reference.

**CONSEQUENCE 2 — §9-B extends one layer up.** The clone carries the Zigbee network (channel/PAN/keys) and the automation *text*, but not the entity identities the automation depends on. **Automations arrive as definitions, not as functioning rules.**

**CONSEQUENCE 3 — R-4's options, for the hub to rule:** (a) clone the event store too — rejected on its face, it would carry the bench's `home_id` and destroy the rig's identity; (b) rewrite `entity_ref`s after re-adoption as an explicit rehearsal step; (c) drop criterion (4) for cloned-rig runs and prove the automation path on the bench instead. **(b) is the only option that preserves the criterion's meaning.**

### ⏺ FINDING §10-J **SHARPENED TO A DEFECT** — THE EXPLAIN SURFACE CONCEALED A REAL FAULT IT COULD SEE

The explain page rendered: *"Automation 'bench-hero' has not been triggered; it fires on state change."* · "What would make it run" → **"state change"**.

The rule it was describing says: **fires when entity `01KX1PB9AAB4VB3E10BD477TV3`'s `occupied` attribute becomes `true`.** That information is in the loaded configuration — the system had it and rendered a generic phrase instead.

**The honest rendering would have been:** *"bench-hero is waiting for entity 01KX1PB9AAB4VB3E10BD477TV3 (occupied → true). That entity does not exist in this home."* **That single sentence would have surfaced a genuine configuration fault in one click; instead it took an hour of journal archaeology to derive.** The explainability hero's product promise is plain-language *why*; on the negative case it currently restates the trigger type and, in doing so, **actively conceals a dangling reference**. Upgraded from "not actionable" to **a defect in the negative-case explanation path**. FE-lane, high value, and directly load-bearing for R-4's criterion (4).

### §10 WINDOW CLOSE — 18:25:18Z (14:25:18 ET)

| reading | value | verdict |
|---|---|---|
| ROWS-W0 → ROWS-W1 | **27 → 53** (+26) | criterion (3) row-delta **MET** emphatically |
| `PRAGMA integrity_check` | **ok** | survived a power cut, 2 adoptions, 4+ restarts |
| `home_id` | `01KZXEG38VC0ZT375GZ3H1P5QS` **unchanged** | identity intact all day |
| throw discriminator | **0** | criterion (3) **MET** |
| `zigbee.network_formed` | **0** | P-d never occurred, all day |
| `zigbee.network_resumed` | **3** | one per service start this boot |
| `zigbee.transport_failed` | **2** | **UNEXPECTED — predicted 0; under investigation** |
| journald `-p warning` tail | only 2 systemd `Failed with result 'exit-code'` lines | **see below** |

**[PACKET EXPECTATION THAT DOES NOT SURVIVE] §10 expects "exactly one `network_resumed`".** That was written for a single service start; this boot had three. The correct expectation is *one per service start, with zero `network_formed`*. Recorded rather than pretended to match.

**⏺ OPEN AT THE CLOSE — TWO ITEMS:**
1. **`transport_failed` = 2, cause unknown.** Predicted 0. The packet names `transport_failed … retransmits=0 crcRejects=0 timeouts=0` as F-S16's physical-port-loss signature. Plausibly the two service restarts closing the serial port, but **NOT ESTABLISHED**. Being read directly.
2. **journald priority appears not to carry the application's log level.** The `-p warning` tail shows only systemd's own two lines and **omits the `key_establishment_failed` WARN known to have fired at 14:11:26**. Hypothesis: the app logs to stdout/stderr (`StandardOutput=journal`), so its WARN/ERROR levels live in the message TEXT while journald assigns priority by stream. **If confirmed, `journalctl -p warning` never surfaces application warnings on this service — any monitor or operator filtering by journal priority would miss every application-level warning and error.** Being tested.


### ⏺ FINDING §10-O — F-S16's "PHYSICAL PORT LOSS" SIGNATURE ALSO FIRES ON A CLEAN SERVICE STOP

Both `transport_failed` lines, in full:
```
14:06:18.208 WARN zigbee.transport_failed: serial read error: port dead or closed;
  lastFrame=DATA(frm=3, ack=6, reTx=false) retransmits=0 crcRejects=0 timeouts=0 — the watchdog owns recovery
14:20:37.193 WARN zigbee.transport_failed: serial read error: port dead or closed;
  lastFrame=DATA(frm=6, ack=4, reTx=false) retransmits=0 crcRejects=0 timeouts=0 — the watchdog owns recovery
```
**Both timestamps are exactly the two operator-issued service restarts** (the permit-join restart at 14:06:18 and the door-close restart at 14:20:37). The coordinator was never unseated; the service stopping closed the serial port and the reader thread reported it.

**The packet's §10 states:** *"A `transport_failed … retransmits=0 crcRejects=0 timeouts=0` line = a physical port loss (F-S16's signature) — ⏺ and check the dongle seat."* **That signature is NOT specific to physical port loss.** It fires identically on an orderly shutdown. **An operator following the packet would investigate a hardware fault that is in fact a clean stop.** The message's own "— the watchdog owns recovery" is honest about handling, but the token and level are not. **Recommend the packet's F-S16 guidance be corrected and, at source, that an orderly-close path not report through `transport_failed`.**

### ⏺ FINDING §10-P — **JOURNALD PRIORITY IS BLIND TO EVERY APPLICATION WARNING ON THIS SERVICE** (major, observability)

```
app-level WARN/ERROR lines in the message TEXT:  158
lines journald reports at priority >= warning:     2
  ...of those, systemd's own:                      2
```
**Zero of the application's 158 WARN/ERROR lines are visible to `journalctl -p`.** Mechanism: the unit sets `StandardOutput=journal` / `StandardError=journal`, so the application's SLF4J level lives in the message *text* (`… WARN  c.h.i.z.Class -- …`) while journald assigns priority by *stream*. Confirmed by the omission of the `key_establishment_failed` WARN (14:11:26) from the `-p warning` output.

**Consequences.** `journalctl -p warning` and `journalctl -p err` are useless on this service. **Any monitoring, alerting, log-shipping or exporter pipeline that filters by journal PRIORITY sees zero application problems on a HomeSynapse host** — it would report a perfectly healthy service while 158 warnings accumulate. For a product whose central claim is observability and explainability, this is a significant gap between what the system knows and what an operator or monitor can find.

**Secondary, unexamined:** the 158 count itself. That is a substantial warning volume in a single boot that nobody has reviewed, precisely because priority filtering hides it. **Composition NOT established** — the guide's grep matched a level marker in the text and did not classify the lines. **Recommend the hub commission a review of what those 158 lines actually are.**

**Candidate fixes (hub to rule):** emit journal-native priority via `SyslogLevelPrefix`/sd-journal integration, or a `LOG_LEVEL`-mapped stderr split, so that an application WARN becomes a journald WARN.

### ⏺ THE PATTERN — FOUR INSTANCES IN ONE DAY OF HEALTHY OUTCOMES REPORTED THROUGH FAILURE CHANNELS

| finding | the healthy event | the failure channel it uses |
|---|---|---|
| **§6-B** | a graceful, operator-requested shutdown | exits **143**, systemd marks the unit **`failed`** |
| **§10-I** | a device with no recorded report time | the list renders **`Current`**, a freshness claim with no evidence |
| **§10-M** | (probably) a transient key self-expiring as designed | **`key_establishment_failed`** WARN for device `0xFFFFFFFFFFFFFFFF` |
| **§10-O** | an orderly service stop closing the serial port | **`transport_failed`** carrying F-S16's "physical port loss" signature |

This is the same family as the M9.4 §B `key_establishment_failed` misclassification the project already identified and fixed as KEYb (confirmed landed today, finding §10-L). **It is a recurring shape, not four unrelated defects**, and it directly undercuts the never-false-ALIVE doctrine from the reporting side rather than the sensing side. **Recommend the hub treat this as a class and consider a sweep** — the doctrine currently guards against claiming health that is not there, but not against claiming failure that is not there, and the second error costs operator trust just as fast.


### ⏺ FINDING §10-Q — THE WARNING CENSUS, AND **A CORRECTION TO FINDING §10-B**

The held card's application-level WARN/ERROR lines this boot, by class and message:
```
 165  WARN  ZclIngestionUnit             zigbee.ingestion_unknown_sender
  15  WARN  MigrationRunner              Skipping already-applied migration
  10  WARN  EzspCoordinatorProtocol      zigbee.ncp_config_skipped
   3  WARN  SqlitePersistenceLifecycle   Database is on removable storage (/dev/mmcblk0p2). SD c…
   3  WARN  StandardConfigurationService Configuration issue [WARNING] at 'integrations.zigbee'
   2  WARN  ZigbeeIntegrationAdapter     zigbee.transport_failed
   2  WARN  PortWatchdog                 zigbee.port_unhealthy
   1  WARN  ZclIngestionUnit             zigbee.key_establishment_failed
```

**⚠ THIS REFUTES FINDING §10-B AND THE GUIDE OWNS IT.** §10-B concluded: *"Answer: (a) nothing transmitted. The adapter logged `device_left` for an unregistered device, so unknown-device traffic IS surfaced, and the preceding silence was simply an absence of transmissions. No silent-drop defect exists."*

**That was wrong.** `zigbee.ingestion_unknown_sender` × **165** is ZCL traffic from devices with no registry record — **the four un-re-adopted devices were transmitting continuously throughout §10.** The correct reading of the §10 silence is neither (a) nor (b) but a third thing: **the traffic arrived, the adapter warned about it 165 times, and the guide missed it twice over** — the §10 greps never included `ingestion_unknown_sender`, and journald's priority filter (finding §10-P) hid the WARN level from every `-p warning` read. The right conclusion (no silent drop) was reached from the wrong premise and stated with more confidence than the evidence carried.

**What this changes:**
1. **The §10 evidence window was never short of device traffic.** It was short of *instrumentation the operator could see*. The packet's §10 token list omits `ingestion_unknown_sender`, which on a cloned-custody rig is the single most informative token available — it is the direct signature of §9-B in motion.
2. **It compounds §10-P.** 165 warnings saying *"the fleet is talking and I don't recognise it"* — a precise, actionable operational signal — invisible to `journalctl -p`, invisible to any monitor built on it, and invisible to a token-grep that doesn't already know to look.
3. **Recommend the packet's §9/§10 greps add `ingestion_unknown_sender`**, and that R-4 treat its count as a first-class rehearsal metric: on a cloned rig it should start high and fall to zero as the fleet re-adopts.

**Other lines worth the hub's eye:** `Database is on removable storage (/dev/mmcblk0p2)` ×3 — an SD-wear advisory that is correct and probably deserves a documented posture. `Configuration issue [WARNING] at 'integrations.zigbee'` ×3 — **an unexamined config warning against the CLONED zigbee.yaml; content not captured, cause not established.** `ncp_config_skipped` ×10 and `port_unhealthy` ×2 are expected companions to the resume path and to §10-O's two restarts.

---

## §11 A-5 THE RESTORE — the bench is home

**Held card:** stopped (`failed`, per §6-B — now an expected reading, not an anomaly), `shutdown -h now`, powered off, removed. **Coordinator left PLUGGED** for the bench. Re-labelled:
> `hs-fresh — R-3/R-4 rig — +git dec35be · drop-in ON · bench custody CLONED 2026-08-30 · 2 devices RE-ADOPTED (new entity IDs)`

The re-adoption clause is deliberate: the card's registry now holds identities that do NOT match the bench's, and anyone picking it up later must know that or they will re-derive §9-B from scratch.

**Bench card in, powered, `ssh pi`:**
```
[!!] NOT running                                    ← F-S15 proven a second time
[OK] launched pid 2118 -> bench-2026-08-30-150211.log
[OK] RADIO UP after 20s
15:02:22.913  registry.projection_live: devices=6 entities=6 position=25065
15:02:23.455  device_relinked: 0x00178801101A09BB deviceId=01KX1PA4GRZHY2GD37B5CFVQHY
15:02:23.456  device_relinked: 0xF044D3FFFED2A201 deviceId=01KXW0156Z1GJ3WCV2G516AKWS
15:02:23.456  device_relinked: 0xF044D3FFFE1C1E8E deviceId=01KXW13WEGRCT5C0XSQT8WZBG9
15:02:23.456  device_relinked: 0x00124B002FA8D1C5 deviceId=01KXW1W1RR66GV98D9QDPB4VXY
15:02:23.457  device_relinked: 0xF044D3FFFE9C78D7 deviceId=01KX1PB9A5931A8G0F0X03QXT2
15:02:23.457  device_relinked: 0x449FDAFFFE688F57 deviceId=01KY12MQVQ204M1VP39F1ZDM33
15:02:23.457  adoption_maps_rehydrated: devices=6
15:02:31.240  network_resumed: channel=20 panId=0x774c
15:02:31.240  network_up: EMBER_NETWORK_UP (buffered)
--- failure tokens ---   (EMPTY)
[OK] running (pid 2118) · /dev/zigbee -> ttyUSB0 · Bus 003 Device 004: ID 10c4:ea60
```

### ⏺ FINDING §11-A — **THE REHEARSAL DID NOT TOUCH THE BENCH'S APPLICATION STATE** (the day's key safety result)

The two devices re-adopted on the held card — the motion sensor (held-card deviceId `01M19XN7MXFBA3P5BT4VDY0BM6`) and the contact sensor (`01M19RHWWZXKD4MWM66KAW8MSR`) — **relinked on the bench with their ORIGINAL bench ULIDs**, `01KX1PB9A5931A8G0F0X03QXT2` and `01KY12MQVQ204M1VP39F1ZDM33`, byte-identical to the pre-swap 04:31 trace (A.0).

**All six relinked. `adoption_maps_rehydrated: devices=6`. `position=25065` unchanged from the 04:31 boot.** The bench's event store did not advance and its registry is exactly as it was left.

**This closes the §9-B loop from the other side and is the day's most important safety result:** adoption identity is per-card and lives in the event store; the two registries are wholly independent; **a full day of card-swapping, custody cloning, two re-adoptions, a permit-join window and an uncontrolled power loss on the rig left the production bench's application state untouched.** The clone travels one direction only, exactly as the packet's fence requires — and now that fence has evidence behind it, not just doctrine.

**[MINOR DEVIATION] `RADIO UP after 20s`.** F-S17's documented band is 12–18 s, with 18 s named as the known first-enumeration after a long unplug. 20 s is 2 s above the envelope. The start succeeded and no failure token appeared. Plausibly attributable to a day in which the dongle was moved to another host, power-cycled by a mains outage, and used for a fresh device join — but **not established**, and recorded rather than rounded into the band.


### **STOP-GATE §11: PASS — THE DAY'S EXIT**

```
runner B3.1-2026-08-02-postwindow @ 16e672d
  [OK] RADIO UP after 13s
  [ok] log 'registry.projection_live: devices=6 entities=6' min=25065
  [ok] log 'zigbee.adoption_maps_rehydrated: devices=6'
  [ok] log 'zigbee.device_relinked' x2(at-least)
  [ok] log 'zigbee.network_resumed: channel=20 panId=0x774c'
  [ok] log 'zigbee.port_identity_captured:' same-line ['pinnedOnly=false']
  [ok] api /api/v1/entities {"rows": 6, "ulids": [...]} — all asserts satisfied
[PASS] boot-health — 6/6 positive · 0 forbidden
  bundle: /home/homesynapse/hs-bench/bundles/boot-health-20260830T190604Z
```

**F-S20 CLOSED — byte-identical across the whole day:**
```
04:31:42.397 (pre-swap)   stableId=…MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false
15:06:03.598 (post-run)   stableId=…MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false
```
Compared against a **measured** before, not the packet's transcription — the §1 amendment paying off at the last gate.

**[MINOR DEVIATION RESOLVED] `RADIO UP after 20s` → 13 s on the restart.** The 20 s reading was the F-S17 long-unplug first enumeration; steady state is **13 s**, inside the documented 12–18 s band. The envelope is intact and the earlier note is withdrawn.

### ⏺ FINDING §10-N **PROVEN DIRECTLY** — the bench's own entity roster names bench-hero's refs

The boot-health API assert printed the bench's live entity ULIDs:
```
{"rows": 6, "ulids": ["01KX1PA4HSJ581GASYB7DHE40F", "01KX1PB9AAB4VB3E10BD477TV3",
                      "01KXW0157SP56CCSGJCNDCSQNG", "01KXW13WF0D6TYGN13WXHTG87K",
                      "01KXW1W1SBJZERC9MBAMV2DWKE", "01KY12MQW954E4XYNKH0Y5H8VX"]}
```
**`01KX1PB9AAB4VB3E10BD477TV3` is bench-hero's trigger `entity_ref`. `01KX1PA4HSJ581GASYB7DHE40F` is its action target `entity_ref`.** Both alive on the bench; both absent from the held card, whose registry held only `01M19XN7…` and `01M19RHW…`.

**§10-N is no longer an inference from ULID prefixes — it is a direct observation on both sides of the swap.** Automations reference entities by ID; those IDs are per-card and live in the event store; therefore **automations survive a custody clone as text and not as rules, and R-4 criterion (4) is unreachable on a cloned rig unless the refs are rewritten after re-adoption.**

---

# CLOSING STATE

**Bench `hs-dev-1`:** running (pid 2344), `[PASS] boot-health 6/6 · 0 forbidden`, PAN 0x774c ch 20, all six devices relinked with their original identities, `position=25065` unchanged, zero failure tokens. **The 04:30 ET nightly will run on its own; its digest is tomorrow's read.**

**Held card `hs-fresh`:** powered off, out of the slot, re-labelled `+git dec35be · drop-in ON · bench custody CLONED 2026-08-30 · 2 devices RE-ADOPTED (new entity IDs)`. Carries: the `0.1.0+git20260823.231355.gdec35be` artifact, R-9's unit, the §7 drop-in, the bench custody clone, its own `home_id 01KZXEG38VC0ZT375GZ3H1P5QS`, 53 event rows, `integrity_check ok`, its pre-clone `data/zigbee.held-pre-r3-2026-08-30/` and `zigbee.yaml.pre-repair-2026-08-30` both preserved.

**Coordinator:** on the bench, hub 3-2.4 Port 2, by-id byte-identical to this morning.

**Repos:** untouched. Core porcelain verified EMPTY at `5051fa5` before, during and after. Every artifact of this run lives in `_scratch/`.

**Fences honoured:** ONE COORDINATOR ONE BOOT (fence held 47 min 54 s across §3–§7) · `--allow-downgrades` used exactly once · delete-nothing (every aside an `mv` or `cp -a`) · no token VALUE ever read, printed or transmitted · the D-1 pair untouched · `distribution/README.md` untouched · nothing on the core checkout · the held card stayed UNPATCHED.

# THE PREDICTION SCORECARD

| block | filed | result |
|---|---|---|
| §3 E3-RED | 7 | **6 EXACT**, 1 half (a `tail -20` truncation artifact) |
| §4 Block I | 10 | **9 EXACT**, 1 **MISS owned** (Δ+4 rows filed, Δ+2 observed — the model is boot-specific, not restart-specific) |
| §5 E3-GREEN | 4 | **4 EXACT** |
| §6 clone gate | 5 | **5 EXACT** (incl. `panId 30540 = 0x774C`) |
| §8 plug | 4 | **4 EXACT** |
| §9 measured boot | 5 arms | **P-a fired**; b/c/d refuted. Fleet arm **MISS owned** (guide predicted P-g-or-P-e from N; actual mechanism was neither — see §9-B) |
| §10 rehydration | 2 forecasts | **2 EXACT** (1→1 and 2→2, after 0→0) |
| §10 M9.4-KEYb | 1 | **REFUTED, owned** — the false-failure pair did NOT appear; the fix appears landed |
| §10 transport_failed | 1 | **MISS owned** — predicted 0, observed 2 (finding §10-O) |
| §10-B silent drops | 1 | **REFUTED BY LATER EVIDENCE, owned** — 165 `ingestion_unknown_sender` (finding §10-Q) |
| §11 restore | 4 | **4 EXACT** |

**Totals: 32 EXACT · 1 half · 5 owned misses or refutations.** Every miss is recorded with its mechanism; none were rounded up.

