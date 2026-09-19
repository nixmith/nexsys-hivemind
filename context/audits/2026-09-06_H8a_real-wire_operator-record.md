<!--
file: context/audits/2026-09-06_H8a_real-wire_operator-record.md
purpose: THE H8-a OPERATOR RECORD — every ⏺ of the Sun 2026-09-06 rig session on the held card (hs-fresh) running f25291b's CI-built artifact (= 093d5b4's Java): the four v1.1.3 keys on the real wire (K1–K4), the FAILCHAN §6-B/EXITCODE stop-proof (two readings), the v1.1.3 wire CAPTURE (FE-113b's fixture), the journald priority count (OR-JOURNALD-PRIO), the sys_* count (docket Row 16), the bench restore. Scaffolded by the v66 hub at Block 1; FILLED by the H8-a navigator as ⏺s land (append-only under the headings; the hub writes §10 at intake).
audience: the navigator (fills §0–§9) · the hub (audits two-layer; writes §10) · Nick (reads §0)
state-type: operator record (evidence; verbatim paste-backs with Z stamps)
status: CLOSED-PENDING-HUB-AUDIT (navigator close-out 2026-09-19T19:01:40Z; B6 carried by R-5B — context/audits/2026-09-19_R-5B_operator-record.md, one sitting, two records; the artifact of record re-pinned to 6bd8508 per the packet's v75 b1 status — the purpose line's f25291b/093d5b4 is the scaffold's original pin, left as written). Was: SCAFFOLD — OPEN. Packet: context/instructions/2026-09-06_H8a_real-wire_v113-keys_and_failchan-proof_navigator-packet.md. Capture dir: context/audits/2026-09-06_H8a_v113-wire-capture/ (three JSON bodies, token-free).
-->

# H8-a — operator record (held card, Sun 2026-09-06)

## §0 VERDICT SURFACE (rewritten by the navigator at close-out, 2026-09-19T19:01:12Z — one screen)

# ★ FOUR OF FOUR STOP-GATES MET (H8a-1 · H8a-0 · H8a-2 · H8a-3 · H8a-4) · ZERO STOPS · K1–K4 ✓ ON THE REAL WIRE · THE STOP-PROOF CLEAN, TWICE · ONE FINDING ON THE WIRE (F-1) ★
**Sat 2026-09-19: navigator up 16:41Z · §0/§1 at the desk 17:06–17:14Z · at the rig 17:14:51Z (B0-1) → 17:43:22Z (B5) = 28 min of ≤60.** Held card `hs-fresh` @ `192.168.1.80` (EDT -0400). **B6 not run by this packet** — R-5B followed in the same sitting on Nick's word; its B4–B5 carried the grade, the halt and the restore (`context/audits/2026-09-19_R-5B_operator-record.md`, RETURNED 50,494 b — ONE SITTING, TWO RECORDS: INTAKE BOTH).

**ARTIFACT:** `homesynapse_0.1.0+git20260914.115803.g6bd8508_arm64.deb` · sha256 **`2fba0325c8ebfbffd2e86ecf2c9d10416009f00c729881b2a7cddc1955e09bd8`** · install-smoke **run #56** `https://github.com/nexsys-io/homesynapse-core/actions/runs/34840877827` · commit `6bd8508` · **amd64 green · arm64 green** · CI main unchanged. Four-surface custody, no human hash comparison: PUBLISHED digest `11f3a79e…8a75` ≡ zip ≡ desktop .deb ≡ card .deb. The incumbent before tonight: `ga458a64` on both surfaces (R-4c's). Install 17:28:24Z → 17:28:39Z (15 s), ordinary upgrade; rows 404 → 411 → 421 across install and restart, integrity `ok` ×2. **Navigator dispatched 16:41Z · record closed 2026-09-19T19:01:12Z · STOPs: 0.**

### THE FOUR KEYS (K) — 4 of 4 (B2-2, re-asserted by the navigator on the filed copies: identical)
| key | read | where | verdict | the assert line, quoted |
|---|---|---|---|---|
| K1 `deviceId` | `/api/v1/entities` rows | every row; ULID or null | **✓** | `K1 deviceId key on every row: True \| non-null: 4 \| every non-null is a 26-char ULID: True` |
| K2 `lastReported` | `/api/v1/entities` rows | every row; ISO-8601 Z or null | **✓** | `K2 lastReported key on every row: True \| non-null: 4 \| every non-null is ISO-8601 Z: True` |
| K3 `components[].ref` | `/api/v1/automations` | every component; `{type:"entity", id}` or null | **✓** | `K3 ref key on every component: True \| non-null: 2 \| every non-null ref is exactly {type:"entity", id:<26>}: True` |
| K4 `triggerRef` | `/api/v1/automations/{id}/non-firing` | present; `{type:"entity", id}` or null | **✓** | `K4 triggerRef key present: True \| value: {"type": "entity", "id": "01M1PRQN03X8H4MNEZQ62F76F1"} \| matches the list's trigger ref: True` |
The literal `"type":"entity"` (lowercase) on every non-null ref: **✓** (3 occurrences in the filed bodies). ISO-8601 on every non-null `lastReported`: **✓** (4 of 4 non-null). rows=4 (R-4c's adoption persisted); `R16 sys_* refs on the wire: 0`.

### THE STOP-PROOF (S) — FAILCHAN §6-B / EXITCODE
| reading | Result | ExecMainStatus | ActiveState | SubState | NRestarts | verdict |
|---|---|---|---|---|---|---|
| B3 (the proof, 17:35:02Z) | success | 143 | inactive | dead | 0 | **✓** |
| B6 slot = R-5B B4 (18:34:28Z) | success | 143 | inactive | dead | 0 | **✓** |
R-4b §9 on `ef02d13` read `Result=exit-code · ActiveState=failed · ExecMainStatus=143` (before the fix). Today: **two clean grades on `6bd8508`, beside R-4c's one on `a458a64` — three readings, two artifacts; `SuccessExitStatus=143 · Restart=always` read on the unit (B1-3).** **F-1, both stops:** no `zigbee.transport_closed_orderly` in the invocation (count 0); `transport_failed: port dead or closed` 3–6 ms into the hook on a clean link → watchdog `port_reopened` +1.6 s → JVM exit ≤60 ms later. The grade is clean because the exit code is; §10-O's orderly path never runs.

### THE CAPTURE (C) — FE-113b's inputs, `context/audits/2026-09-06_H8a_v113-wire-capture/`
| file | bytes | sha256 | Bearer count |
|---|---|---|---|
| `entities.json` | 759 | `29e04def1dd6cb3c317a665829284d61bb9700dd543dd80145193344ec005afe` | 0 |
| `automations.json` | 629 | `6fc36639059337f5303ad478cc597405c2388f81f7b713178098f193d3ff22c4` | 0 |
| `nonfiring.json` | 581 | `01bf6f29112eebb836a7031457bdea677ff21ab43085d0c549422c1a22efa46b` | 0 |

### THE READS (J · R)
OR-JOURNALD-PRIO (B4): `200 "PRIORITY":"6"` · warning-or-worse 0 · app WARN 26 — **Row 7's pair: 26 vs 0.** Row 16 (B5): `components=3 refs_nonnull=2 sys_refs=0`. `S31-LABEL: 15A 1800W — Input 120V @ 60Hz` (model line not transcribed). `fleet:` at B0: no line (the bench tree was 16e672d) — R-5B's B6 pulled to fa01cad and printed the first: `fleet: 6/6 · re-seen 0`. Nightly 09-12→09-19 banked (B0-1): `command-confirm-s31` FAILED 09-12 and 09-18, passed the other six nights and tonight's manual run.

### PER-BLOCK
| block | verdict | note |
|---|---|---|
| §0 guard 1 | **MET** | run #56 green ×2, digest = PUBLISHED |
| §1 fetch + hash | **MET (2nd attempt)** | attempt 1 caught the stale 09-13 zip (a458a64) — the gate did its job | STOP-GATE H8a-1 |
| B0 preflight | **MET 6/6** | PAN re-read after D-2 (cut width) | STOP-GATE H8a-0 |
| B1 install + boot | **MET 6/6** | 15 s upgrade; the unit directives on the card | STOP-GATE H8a-2 |
| B2 the four keys | **MET · K1–K4 ✓** | copy home on attempt 2 (D-4) | STOP-GATE H8a-3 |
| B3 the stop-proof | **MET (S) · F-1** | grade clean; the transport path is not the designed one | STOP-GATE H8a-4 |
| B4 journald priority | **MET** | 26 vs 0 |
| B5 sys_* count | **MET** | 0 |
| B6 the restore | **NOT RUN HERE — carried by R-5B B4–B5** | grade ✓ · `[PASS] boot-health 6/6` · PAN 0x774c · formed 0 | STOP-GATE H8a-5 met via R-5B |
**⏺ census: 25 paste-backs banked (incl. the B6 completion). Deviations: 5 (D-1..D-5, §9) — 2 instrument (T1), 1 navigator error, 2 operator slips (no rig effect beyond empty dirs). STOPs: 0.**

### ASKS OF THE HUB
1. **FE-113 → VERIFIED** on K1–K4 · **OR-FAILCHAN → CLOSED** on the two `success · 143 · inactive` readings · **FE-113b's fixture EXISTS** (three files, hashed, token-free) · **O-2 → CLOSED** on three readings / two artifacts — per §H.
2. **F-1 → a docket row:** FAILCHAN §10-O's orderly transport close never runs on 6bd8508 (2/2 stops); the adapter's read loop is not stopped before the hook closes the port; the watchdog re-negotiates the NCP under a dying JVM. A design finding, not a grade defect.
3. **The operator slips' residue** — empty `~/r3-history` + `~/h8a-artifact` in /home/homesynapse on hs-dev-1 (D-1); an empty `Desktop/Code/…/2026-09-06_H8a_v113-wire-capture` tree + a `192.168.1.80` known_hosts entry in /home/nick on hs-fresh (D-4): move aside or leave — nothing was deleted.
4. **Row 7:** bank 26 vs 0. **Row 16:** 0.
5. The record is ~40 KB, over the ~24 KB target: the 25-line B3-2 tail and the eight-night B0 digest were the packet's own ⏺s ("⏺ all"); nothing was harvested. The packet's `cut -c1-160` (D-2) should be 240 in B0-4 and B1-4.

## §0-G Guard 1 — the artifact (⏺ `ARTIFACT:` line · `CI-main:` line)

⏺ §0 GUARD 1 — filed 2026-09-19T17:06:29Z — MET (amd64 green · arm64 green · digest = PUBLISHED 11f3a79e… in full; no `CI-main:` line pasted → main still 6bd8508's, the banked line stands)
```text
ARTIFACT: 6bd8508 — run 34840877827 — amd64 green — arm64 green — arm64 digest <SHA256 digest of uploaded artifact zip is 11f3a79e6370b6e8e8155a7b3deaaced3eaf6fde3bdfa7a482137579d2aa8a75>
```

## §1 Fetch + hash (⏺ the origin echo line · the unpack + hash output)

⏺ §1 ATTEMPT 1 — filed 2026-09-19T17:10:54Z — MISS at THE GATE (the newest arm64 zip by mtime is R-4c's 09-13 download: sha256 883c5f8d… ≠ PUBLISHED 11f3a79e…; the expanded .deb is the incumbent ga458a64 = R-4c card §7's 1f46c5c8…). The block's own remediation applies: tonight's zip was never downloaded → download again, re-run. Not a T3. The desktop ~/h8a-artifact now holds a458a64's tree; the re-run moves it aside to ~/r3-history (delete nothing).
```text
DESKTOP-SRK0P9D
17:09:00Z
-rw-r--r-- 1 Nick 197121 129014717 2026-09-13T08:49:03 '/c/Users/Nick/Downloads/distribution-artifacts-arm64(1).zip'
883c5f8d808622429c937d92e9f711da7b371973ed9d2c2e3996f5441bd6e468 */c/Users/Nick/Downloads/distribution-artifacts-arm64(1).zip
PUBLISHED 11f3a79e6370b6e8e8155a7b3deaaced3eaf6fde3bdfa7a482137579d2aa8a75
1
-rw-r--r-- 1 Nick 197121 62896270 2026-09-13T11:40:04 ./deb/build/homesynapse_0.1.0+git20260913.113754.ga458a64_arm64.deb
1f46c5c864fe03c261a2c0a15752ac0b4b91c732646fec90e2f572f9aef7eed1 *./deb/build/homesynapse_0.1.0+git20260913.113754.ga458a64_arm64.deb
```

⏺ §1 ATTEMPT 2 — filed 2026-09-19T17:14:21Z — MET · STOP-GATE H8a-1 MET (zip mtime today 12:13:25 local · zip sha256 = PUBLISHED 11f3a79e…8a75 in full · one .deb · name carries g6bd8508 · ORIGIN HASH OF RECORD `2fba0325c8ebfbffd2e86ecf2c9d10416009f00c729881b2a7cddc1955e09bd8`, 62,889,838 bytes). The version-grammar echo step was not read (auth-gated; skipped, not a stop — R-4c D-1).
```text
DESKTOP-SRK0P9D
17:13:39Z
-rw-r--r-- 1 Nick 197121 129009105 2026-09-19T12:13:25 '/c/Users/Nick/Downloads/distribution-artifacts-arm64(2).zip'
11f3a79e6370b6e8e8155a7b3deaaced3eaf6fde3bdfa7a482137579d2aa8a75 */c/Users/Nick/Downloads/distribution-artifacts-arm64(2).zip
PUBLISHED 11f3a79e6370b6e8e8155a7b3deaaced3eaf6fde3bdfa7a482137579d2aa8a75
1
-rw-r--r-- 1 Nick 197121 62889838 2026-09-14T11:59:42 ./deb/build/homesynapse_0.1.0+git20260914.115803.g6bd8508_arm64.deb
2fba0325c8ebfbffd2e86ecf2c9d10416009f00c729881b2a7cddc1955e09bd8 *./deb/build/homesynapse_0.1.0+git20260914.115803.g6bd8508_arm64.deb
```

## B0 Preflight at the rig (⏺ the bench digest · the halt · the held card's boot glance; the pinned IP)

⏺ B0-1 THE BENCH DIGEST — filed 2026-09-19T17:15:21Z — MET (hs-dev-1 · eight nightly lines 09-12→09-19 · NO `fleet:` line → the bench tree on the card does not print R-5 Part A's datum (f3631cb not on the card, or not in the digest) — a ⏺, not a stop · newest bundles all 2026-09-19T08:32Z). Note for the hub: `command-confirm-s31` FAILED on 09-12 and again on 09-18 (7/9 each), 8/9 PASS every other night; ON-latency 0.12–3.57 s when it passes. Read only — s31/nightly untouched.
```text
hs-dev-1
17:14:51Z
2026-09-12 quiesced AUTO floor: 7/9 · FAIL command-confirm-s31 · bundle /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260912T083148Z · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)
2026-09-13 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 3.57s
2026-09-14 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.54s
2026-09-15 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.14s
2026-09-16 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.33s
2026-09-17 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.12s
2026-09-18 quiesced AUTO floor: 7/9 · FAIL command-confirm-s31 · bundle /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260918T083214Z · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)
2026-09-19 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 1.92s
command-s31-settle-20260919T083210Z
command-confirm-s31-20260919T083209Z
timeout-honesty-no-change-20260919T083207Z
```

⏺ B0-2 THE HALT + THE SWAP — filed 2026-09-19T17:23:47Z — MET (hs-dev-1 printed, then the ssh returned on the halt — no further line). Physical acts, operator's clock (CT): OFF 12:16 · bench card OUT 12:16 · held card IN 12:16 · dongle confirmed in the same port, not reseated · ON 12:17 (= 17:17Z).
```text
hs-dev-1
```
⏺ B0-3 S31-LABEL — filed 2026-09-19T17:23:47Z — MET (rated current and rated power read from the unit's own label; read only, nothing pressed or unplugged). The model line was not transcribed — the operator pasted the three label rows below; the packet's one-line form, filled from them:
```text
S31-LABEL: 15A 1800W — <model line not transcribed> — Input 120V @ 60Hz (Output 120V @ 60Hz)
```
Label rows as pasted: `Input: 120V @ 60Hz` · `Output: 120V @ 60Hz` · `Max Load: 15A/1800W`.

⏺ B0-4 THE HELD CARD'S BOOT GLANCE — filed 2026-09-19T17:25:04Z — MET 10/11 on the paste (hs-fresh · IP PINNED **192.168.1.80** · EDT -0400 · python3+curl 2 · incumbent `0.1.0+git20260913.113754.ga458a64` on both surfaces = R-4c's artifact, H8-a never installed before tonight · active · INV=e7b2dea6… · formed 0 · resumed 1 · ROWS-A **404** · permit_join_duration 0). The ELEVENTH — the PAN — is CLIPPED by the block's own `cut -c1-160`: the line ends `channel=20 panI`. Instrument defect (D-2, T1): re-read with a wider cut before the gate is called.
```text
hs-fresh
192.168.1.80 2600:1702:6e8a:aff0::47 2600:1702:6e8a:aff0:ebde:ae1b:776c:c32c
17:24:26Z
EDT -0400
2
homesynapse     0.1.0+git20260913.113754.ga458a64
0.1.0+git20260913.113754.ga458a64
active
INV=e7b2dea6519542e69cfea25822391d63
0
1
Sep 19 13:17:39 hs-fresh homesynapse[924]: 13:17:39.981 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panI
404
0
```

⏺ B0-4b THE PAN RE-READ (D-2, T1) — filed 2026-09-19T17:25:31Z — MET · **STOP-GATE H8a-0 MET 6/6**: hs-fresh · IP pinned 192.168.1.80 · formed 0 · resumed 1 on PAN 0x774c (channel 20) · ROWS-A 404 · no window.
```text
hs-fresh
Sep 19 13:17:39 hs-fresh homesynapse[924]: 13:17:39.981 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
```

## B1 Install + boot (⏺ the copy + hash · the integrity gate · the install with three stamps · the boot tokens as counts)

⏺ B1-1 THE COPY + HASH HOP-TO-HOP — filed 2026-09-19T17:26:16Z — MET (hs-fresh · 0 before the copy · hs-fresh · 1 · card hash = §1 ORIGIN `2fba0325…09bd8` · Version 0.1.0+git20260914.115803.g6bd8508 · arm64). Custody chain now four surfaces: PUBLISHED digest 11f3a79e… ≡ zip ≡ desktop .deb 2fba0325… ≡ card .deb.
```text
hs-fresh
0
homesynapse_0.1.0+git20260914.115803.g6bd8508_arm64.deb   100%   60MB  61.7MB/s   00:00
hs-fresh
1
2fba0325c8ebfbffd2e86ecf2c9d10416009f00c729881b2a7cddc1955e09bd8  /home/nick/homesynapse_0.1.0+git20260914.115803.g6bd8508_arm64.deb
Version: 0.1.0+git20260914.115803.g6bd8508
Architecture: arm64
```

⏺ B1-2 THE INTEGRITY GATE — filed 2026-09-19T17:27:31Z — MET (ROWS-pre **408** ≥ ROWS-A 404 · integrity `ok` · homesynapse.yaml 17 lines / 426 b · token file present, 44 b). CLOCK NOTE: the card stamped `17:26:43Z`, but this block was handed after B1-1 was filed at 17:31Z (navigator clock, which agreed with the bench card and the desktop to the minute at B0-1/§1, and with this card at B0-4 = 17:24:26Z). The held card's clock reads ~6 min behind real time here — one T2 read (timedatectl) ordered before the install; filed below.
```text
hs-fresh
17:26:43Z
408
ok
17
-rw------- 1 homesynapse homesynapse 426 Sep  4 14:56 /var/lib/homesynapse/config/homesynapse.yaml
-rw-r--r-- 1 homesynapse homesynapse  44 Aug 13 07:35 /var/lib/homesynapse/config/initial_api_token
```

⏺ B1-2 CORRECTION — filed 2026-09-19T17:27:53Z — the CLOCK NOTE in the ⏺ above is the NAVIGATOR'S error, not the card's: the record's own stamps read B1-1 filed 17:26:16Z → the card's 17:26:43Z is consistent to the second. The navigator had quoted rounded stamps from memory in its messages (17:28Z, 17:31Z) instead of reading them from the record. The held card's clock is sound; NO timedatectl probe is ordered; the ⏺ above stands as filed (append-only) with this correction beneath it. Filed as D-3 in §9.

⏺ B1-3 THE INSTALL — filed 2026-09-19T17:29:42Z — MET (ordinary UPGRADE, no "downgrad" · 17:28:24Z → 17:28:39Z = **15 s** · `0.1.0+git20260914.115803.g6bd8508` on both surfaces · active at 17:29:04Z · ActiveState=active SubState=running ExecMainStatus=0 · **SuccessExitStatus=143 · Restart=always** — the FAILCHAN unit directives are on the card). Note: `tail -8` shows only the postinst banner; the apt "Unpacking … over (…ga458a64)" line fell above the tail — the two version reads carry the upgrade.
```text
hs-fresh
17:28:24Z
HomeSynapse Core is running.
----------------------------------------------------------------
 HomeSynapse Core installed.
 First-run pairing token: /var/lib/homesynapse/config/initial_api_token
   View it with:  sudo homesynapse-token
   Pair a client with that bearer token to reach the dashboard,
   then delete the token file.
----------------------------------------------------------------
17:28:39Z
homesynapse     0.1.0+git20260914.115803.g6bd8508
0.1.0+git20260914.115803.g6bd8508
17:29:04Z
active
Restart=always
SuccessExitStatus=143
ExecMainStatus=0
ActiveState=active
SubState=running
```

⏺ B1-4 THE BOOT TOKENS — filed 2026-09-19T17:30:22Z — MET 6/6 · **STOP-GATE H8a-2 MET**: version exact ×2 · active · config_issue 0 · schema_registered 1 (stage=pre-load, 13:28:35 local) · formed 0 · resumed 1 on channel 20 panId 0x774c (13:28:44 local, 9.2 s after the schema line) · ROWS 408 → **411**, zero loss · integrity ok · SuccessExitStatus=143 + Restart=always on the unit (B1-3). New INV=d17e76a2… (B0's was e7b2dea6…).
```text
hs-fresh
INV=d17e76a2e92748c388039e44a3d36eaa
config_issue=0
schema_registered=1
network_formed=0
network_resumed=1
Sep 19 13:28:35 hs-fresh homesynapse[1520]: 13:28:35.150 [main] INFO  c.h.lifecycle.HomeSynapseCore -- lifecycle.integration_schema_registered: type=zigbee stage=pre-load
Sep 19 13:28:44 hs-fresh homesynapse[1520]: 13:28:44.363 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
411
ok
```

## B2 The four keys (⏺ the three GETs · the asserts output whole · the capture on the desktop with hashes)

⏺ B2-1 THE THREE GETs — filed 2026-09-19T17:31:13Z — MET (token_len=43 · TOKLEN-OK · entities 200/759 b · automations 200/629 b · nonfiring 200/581 b · bench-hero id=01M2XBCYM6K6ZW0W6WYBA84KNB, resolved by name · three files in ~/h8a/). No token value in the paste.
```text
hs-fresh
17:30:54Z
token_len=43
TOKLEN-OK
entities http=200 bytes=759
automations http=200 bytes=629
bench-hero id=01M2XBCYM6K6ZW0W6WYBA84KNB
nonfiring http=200 bytes=581
total 12
-rw-rw-r-- 1 nick nick 629 Sep 19 13:30 automations.json
-rw-rw-r-- 1 nick nick 759 Sep 19 13:30 entities.json
-rw-rw-r-- 1 nick nick 581 Sep 19 13:30 nonfiring.json
```

⏺ B2-2 THE ASSERTS — filed 2026-09-19T17:32:19Z — **MET · K1 ✓ K2 ✓ K3 ✓ K4 ✓ — no False anywhere.** rows=4 (R-4c's adoption persisted; viewPosition=411 = the row count) · K1 True|4|True · K2 True|**4**|True (the desk pre-registered ≥1: every row carries an instant — the null arm is not on this wire, R-4c D-9's class again) · automations=1 components=3, the three types as pre-registered · K3 True|2|True · nonfiring bench-hero verdict=NEVER_TRIGGERED enabled=True · K4 True | {"type": "entity", "id": "01M1PRQN03X8H4MNEZQ62F76F1"} | True · R16 0. Wire notes: the two UNAVAILABLE rows carry 2026-09-13 instants that survived six days powered off + a version upgrade un-refreshed (LASTREPORTED-1b's instant arm, a third time); the S31 (17:28:15.976Z) and the SNZB-02P (17:25:21.811Z) instants both PRE-DATE this invocation's resume (17:28:44Z) — the projection replayed them at boot, exactly as the packet said the key reports the projection, not the live radio.
```text
hs-fresh
entities rows=4 viewPosition=411
K1 deviceId key on every row: True | non-null: 4 | every non-null is a 26-char ULID: True
K2 lastReported key on every row: True | non-null: 4 | every non-null is ISO-8601 Z: True
    01M19RHWXYZYJMM26SX0E41HXN UNAVAILABLE stale=False deviceId=01M19RHWWZXKD4MWM66KAW8MSR lastReported=2026-09-13T14:45:07.132090Z
    01M19XN7NNQQ8S3JJF09T6YKKY UNAVAILABLE stale=False deviceId=01M19XN7MXFBA3P5BT4VDY0BM6 lastReported=2026-09-13T14:44:31.278087Z
    01M1PRQN03X8H4MNEZQ62F76F1 AVAILABLE stale=False deviceId=01M1PRQMZHFV4SAWT1E96B9BQ2 lastReported=2026-09-19T17:28:15.976273Z
    01M2DKJWVSJCHB6TTAJSW3D880 AVAILABLE stale=False deviceId=01M2DKJWVDDHRF8ZX9HQ5B94KX lastReported=2026-09-19T17:25:21.811743Z
automations=1 components=3 types=['StateChangeTrigger', 'DelayAction', 'CommandAction']
K3 ref key on every component: True | non-null: 2 | every non-null ref is exactly {type:"entity", id:<26>}: True
nonfiring: automation=bench-hero verdict=NEVER_TRIGGERED enabled=True
K4 triggerRef key present: True | value: {"type": "entity", "id": "01M1PRQN03X8H4MNEZQ62F76F1"} | matches the list's trigger ref: True
R16 sys_* refs on the wire: 0
```

⏺ B2-3 ATTEMPT 1 — filed 2026-09-19T17:33:23Z — MISFIRE (operator slip D-4): the desktop block was pasted at the `nick@hs-fresh` prompt. On the HELD card: an empty dir tree `~/Desktop/Code/ClaudeFolder/nexsys-hivemind/context/audits/2026-09-06_H8a_v113-wire-capture` created under /home/nick; the card's own `192.168.1.80` host key added to /home/nick/.ssh/known_hosts (operator answered `yes`); the scp to itself failed `Permission denied (publickey)` — nothing copied, nothing deleted, ~/h8a untouched. Left in place. Re-run on the desktop follows.
```text
hs-fresh
Warning: Identity file /home/nick/.ssh/id_ed25519_pi not accessible: No such file or directory.
The authenticity of host '192.168.1.80 (192.168.1.80)' can't be established.
ED25519 key fingerprint is SHA256:rzZUoqAKvw5gQ0rjGheaKMY0VxaDCoNTPRfM56UrCJQ.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:1: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? y
Please type 'yes', 'no' or the fingerprint: yes
Warning: Permanently added '192.168.1.80' (ED25519) to the list of known hosts.
nick@192.168.1.80: Permission denied (publickey).
scp: Connection closed
```

⏺ B2-3 ATTEMPT 2 THE CAPTURE HOME — filed 2026-09-19T17:34:29Z — MET · **STOP-GATE H8a-3 MET**: three bodies on the desktop at `context/audits/2026-09-06_H8a_v113-wire-capture/`, byte counts = B2-1's (759/629/581), Bearer 0 ×3. NAVIGATOR CROSS-CHECK on the filed copies (read-only, same minute): hashes re-read identical · Bearer 0 ×3 · rows 4 · K1 K2 K3 K4 all True · the literal lowercase `"type":"entity"` appears 3× (2 in automations.json + 1 in nonfiring.json).
```text
DESKTOP-SRK0P9D
automations.json   100%  629    81.9KB/s   00:00
entities.json      100%  759   110.1KB/s   00:00
nonfiring.json     100%  581    74.5KB/s   00:00
total 9
-rw-r--r-- 1 Nick 197121 629 Sep 19 12:33 automations.json
-rw-r--r-- 1 Nick 197121 759 Sep 19 12:33 entities.json
-rw-r--r-- 1 Nick 197121 581 Sep 19 12:33 nonfiring.json
6fc36639059337f5303ad478cc597405c2388f81f7b713178098f193d3ff22c4 */c/Users/Nick/Desktop/Code/ClaudeFolder/nexsys-hivemind/context/audits/2026-09-06_H8a_v113-wire-capture/automations.json
29e04def1dd6cb3c317a665829284d61bb9700dd543dd80145193344ec005afe */c/Users/Nick/Desktop/Code/ClaudeFolder/nexsys-hivemind/context/audits/2026-09-06_H8a_v113-wire-capture/entities.json
01bf6f29112eebb836a7031457bdea677ff21ab43085d0c549422c1a22efa46b */c/Users/Nick/Desktop/Code/ClaudeFolder/nexsys-hivemind/context/audits/2026-09-06_H8a_v113-wire-capture/nonfiring.json
/c/Users/Nick/Desktop/Code/ClaudeFolder/nexsys-hivemind/context/audits/2026-09-06_H8a_v113-wire-capture/automations.json:0
/c/Users/Nick/Desktop/Code/ClaudeFolder/nexsys-hivemind/context/audits/2026-09-06_H8a_v113-wire-capture/entities.json:0
/c/Users/Nick/Desktop/Code/ClaudeFolder/nexsys-hivemind/context/audits/2026-09-06_H8a_v113-wire-capture/nonfiring.json:0
```

## B3 The stop-proof (⏺ the stop stamps · the grade + the journal tail · the start + the counts)

⏺ B3-1 THE ACT (one clean operator stop) — filed 2026-09-19T17:35:41Z — MET (17:35:02Z → 17:35:07Z: the stop returned in ≈2 s, well inside the 30 s hook grace and TimeoutStopSec=90).
```text
hs-fresh
17:35:02Z
17:35:07Z
```

⏺ B3-2 THE READ — THE GRADE OF THE STOP — filed 2026-09-19T17:37:25Z — **(S) MET on the four properties: `Result=success · ExecMainStatus=143 · ActiveState=inactive · SubState=dead` · NRestarts=0** · "Deactivated successfully" present · ZERO "Failed with result" · ZERO "abandoned (ungraceful shutdown)". **FINDING F-1 (the tail's fifth expectation MISSED): NO `zigbee.transport_closed_orderly` line anywhere in the stop window (13:35:02.977 → 13:35:04.737, fully inside the 25-line tail).** Instead, during the shutdown: `WARN zigbee.transport_failed: serial read error: port dead or closed` (13:35:02.983, 6 ms after Javalin stopped) → `WARN zigbee.port_unhealthy: cause=read-error; reopen scheduling started` → the PortWatchdog **REOPENED the port while the process was shutting down**: ASH connected (resetCode=0xb), EZSP negotiated v13, two `ncp_config_skipped` WARNs (0x1/0x37, 0x6/0x35), `ncp_configured`, `zigbee.reopened: port=/dev/ttyUSB0`, `port_reopened: recovery succeeded after 0 failed attempts` (13:35:04.689) — then persistence stopped and `HomeSynapseCore stopped … (SIG…` 48 ms later. The desk (FAILCHAN §10-O) predicted the orderly path; the wire shows the shutdown hook and the port watchdog racing, the watchdog winning a full NCP re-negotiation ~50 ms before exit. The grade is clean because the exit code is; the transport path is not the one designed. One T2 read ordered (counts across the whole invocation + the uncut lines), filed below.
```text
hs-fresh
Result=success
NRestarts=0
ExecMainStatus=143
ActiveState=inactive
SubState=dead
2026-09-19T13:28:44-04:00 hs-fresh homesynapse[1520]: 13:28:44.363 [integration-zigbee-0] INFO  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.network_up: stackStatusHandler reported EMBER_NETWORK_UP
2026-09-19T13:28:44-04:00 hs-fresh homesynapse[1520]: 13:28:44.363 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.production_session_started: port=/dev/zigbee protocolVersion=
2026-09-19T13:35:02-04:00 hs-fresh systemd[1]: Stopping homesynapse.service - HomeSynapse Core — local-first smart-home engine...
2026-09-19T13:35:02-04:00 hs-fresh homesynapse[1520]: 13:35:02.977 [hs-shutdown] INFO  io.javalin.Javalin -- Stopping Javalin ...
2026-09-19T13:35:02-04:00 hs-fresh homesynapse[1520]: 13:35:02.977 [hs-shutdown] INFO  org.eclipse.jetty.server.Server -- Stopped Server@78226c36{STOPPING}[11.0.25,sto=0]
2026-09-19T13:35:02-04:00 hs-fresh homesynapse[1520]: 13:35:02.979 [hs-shutdown] INFO  o.e.jetty.server.AbstractConnector -- Stopped ServerConnector@1cec219f{HTTP/1.1, (http/1.1)}{127.0.0.1:7070}
2026-09-19T13:35:02-04:00 hs-fresh homesynapse[1520]: 13:35:02.981 [hs-shutdown] INFO  o.e.j.server.handler.ContextHandler -- Stopped o.e.j.s.ServletContextHandler@5b852b49{/,null,STOPPED}
2026-09-19T13:35:02-04:00 hs-fresh homesynapse[1520]: 13:35:02.983 [hs-shutdown] INFO  io.javalin.Javalin -- Javalin has stopped
2026-09-19T13:35:02-04:00 hs-fresh homesynapse[1520]: 13:35:02.983 [integration-zigbee-0] WARN  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.transport_failed: serial read error: port dead or closed; las
2026-09-19T13:35:02-04:00 hs-fresh homesynapse[1520]: 13:35:02.984 [integration-zigbee-0] WARN  c.h.integration.zigbee.PortWatchdog -- zigbee.port_unhealthy: cause=read-error; reopen scheduling starte
2026-09-19T13:35:04-04:00 hs-fresh homesynapse[1520]: 13:35:04.578 [integration-zigbee-0] INFO  c.h.integration.zigbee.AshSession -- ASH session connected: ashVersion=2 resetCode=0xb
2026-09-19T13:35:04-04:00 hs-fresh homesynapse[1520]: 13:35:04.584 [integration-zigbee-0] INFO  c.h.i.zigbee.EzspCoordinatorProtocol -- EZSP session negotiated: protocolVersion=13 stackType=2 stackVer
2026-09-19T13:35:04-04:00 hs-fresh homesynapse[1520]: 13:35:04.640 [integration-zigbee-0] WARN  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.ncp_config_skipped: id=0x1 status=0x37
2026-09-19T13:35:04-04:00 hs-fresh homesynapse[1520]: 13:35:04.646 [integration-zigbee-0] WARN  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.ncp_config_skipped: id=0x6 status=0x35
2026-09-19T13:35:04-04:00 hs-fresh homesynapse[1520]: 13:35:04.664 [integration-zigbee-0] INFO  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.ncp_configured: zdo_flags=0x3 stack_profile=2 security_le
2026-09-19T13:35:04-04:00 hs-fresh homesynapse[1520]: 13:35:04.689 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.reopened: port=/dev/ttyUSB0
2026-09-19T13:35:04-04:00 hs-fresh homesynapse[1520]: 13:35:04.689 [integration-zigbee-0] INFO  c.h.integration.zigbee.PortWatchdog -- zigbee.port_reopened: recovery succeeded after 0 failed attempts
2026-09-19T13:35:04-04:00 hs-fresh homesynapse[1520]: 13:35:04.736 [hs-shutdown] INFO  c.h.p.SqlitePersistenceLifecycle -- WAL checkpoint completed: database=/var/lib/homesynapse/data/homesynapse-even
2026-09-19T13:35:04-04:00 hs-fresh homesynapse[1520]: 13:35:04.736 [hs-shutdown] INFO  c.h.persistence.DatabaseExecutor -- Shutting down DatabaseExecutor
2026-09-19T13:35:04-04:00 hs-fresh homesynapse[1520]: 13:35:04.737 [hs-shutdown] INFO  c.h.persistence.DatabaseExecutor -- DatabaseExecutor shutdown complete
2026-09-19T13:35:04-04:00 hs-fresh homesynapse[1520]: 13:35:04.737 [hs-shutdown] INFO  c.h.p.SqlitePersistenceLifecycle -- Persistence layer stopped: database=/var/lib/homesynapse/data/homesynapse-eve
2026-09-19T13:35:04-04:00 hs-fresh homesynapse[1520]: 13:35:04.737 [hs-shutdown] INFO  c.h.lifecycle.HomeSynapseCore -- HomeSynapseCore stopped: db=/var/lib/homesynapse/data/homesynapse-events.db (SIG
2026-09-19T13:35:04-04:00 hs-fresh systemd[1]: homesynapse.service: Deactivated successfully.
2026-09-19T13:35:04-04:00 hs-fresh systemd[1]: Stopped homesynapse.service - HomeSynapse Core — local-first smart-home engine.
2026-09-19T13:35:04-04:00 hs-fresh systemd[1]: homesynapse.service: Consumed 11.015s CPU time.
```

⏺ B3-2b F-1 T2 READ (whole invocation d17e76a2…) — filed 2026-09-19T17:39:56Z — **closed_orderly=0 · transport_failed=1 · port_reopened=1** — the orderly-close token was NEVER emitted in this invocation; the one transport failure and the one reopen are both inside the stop window (none at boot or during the 6-min run). The uncut failure line says why: the serial read loop saw the port "dead or closed" with a clean link (`lastFrame=DATA(frm=2, ack=2, reTx=false) retransmits=0 crcRejects=0 timeouts=0`) and handed recovery to the watchdog — i.e. the shutdown hook closed the port underneath a read loop that had not been told to stop; the watchdog then re-opened and re-negotiated the NCP ~1.6 s later, and the JVM exited on SIGTERM 48 ms after that. Characterized in three counts + two lines; no further probe. For the hub: a design finding on the FAILCHAN §10-O path (stop ordering: adapter-stop before port-close, or the watchdog must observe the shutdown flag), not a grade defect — systemd's grade is `success`.
```text
hs-fresh
closed_orderly=0
transport_failed=1
port_reopened=1
Sep 19 13:35:02 hs-fresh homesynapse[1520]: 13:35:02.983 [integration-zigbee-0] WARN  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.transport_failed: serial read error: port dead or closed; lastFrame=DATA(frm=2, ack=2, reTx=false) retransmits=0 crcRejects=0 timeouts=0 — the watchdog owns recovery
Sep 19 13:35:04 hs-fresh homesynapse[1520]: 13:35:04.737 [hs-shutdown] INFO  c.h.lifecycle.HomeSynapseCore -- HomeSynapseCore stopped: db=/var/lib/homesynapse/data/homesynapse-events.db (SIGTERM)
```

⏺ B3-3 THE START — filed 2026-09-19T17:41:48Z — MET 6/6 · **STOP-GATE H8a-4 MET** (`success · 143 · inactive` on the stop; a clean resume after): start 17:40:54Z, held ~5 s by ExecStartPost (returned 17:41:24Z incl. the 25 s sleep) · active · NEW INV=a3c45da2… (B1's d17e76a2…, B0's e7b2dea6… — three invocations tonight) · config_issue=0 · **formed 0 · resumed 1** · ROWS 411 → **421**, zero loss. The NCP session the watchdog re-negotiated during F-1's stop did not disturb the resume.
```text
hs-fresh
17:40:54Z
17:41:24Z
active
INV=a3c45da2f9b34bcaaaa0feddae2adad6
config_issue=0
network_formed=0
network_resumed=1
421
```

## B4 OR-JOURNALD-PRIO (⏺ the priority count)

⏺ B4 OR-JOURNALD-PRIO — filed 2026-09-19T17:42:38Z — MET, the datum banked: **200 of 200 lines at PRIORITY 6 · journald warning-or-worse = 0 · app-level ` WARN ` lines in the same 200 = 26.** Row 7's pair is **26 vs 0**: every one of the application's own WARNs (among them F-1's `transport_failed`, `port_unhealthy`, two `ncp_config_skipped`) is invisible to a priority-based filter — `journalctl -p warning` on this card returns nothing while the app logged 26 warnings.
```text
hs-fresh
    200 "PRIORITY":"6"
warning-or-worse in the last 200 = 0
app WARN lines in the same 200 = 26
```

## B5 Row 16 (⏺ the sys_* line)

⏺ B5 ROW 16 — filed 2026-09-19T17:43:22Z — MET: `components=3 refs_nonnull=2 sys_refs=0` (agrees with B2's R16 0). H8-a's B0–B5 complete at the rig, 17:14:51Z → 17:43Z ≈ 28 min of the ≤60. B6 is R-5B's (Nick's word, v74 close): the navigator opens R-5B's packet now; the held card stays in, running on 6bd8508, INV a3c45da2….
```text
hs-fresh
components=3 refs_nonnull=2 sys_refs=0
```

## B6 The restore (⏺ the halt's grade · the bench floor)

⏺ B6 — NOT RUN BY THIS PACKET (Nick's word, v74 close; the packet's own B6 heading): at B5's close (2026-09-19T17:43:51Z) the navigator opened R-5B's packet; the restore is R-5B's B4–B5 and O-2's second reading of the day is R-5B's B4 grade. Both are filed in `context/audits/2026-09-19_R-5B_operator-record.md` §5/§6; this section is completed at the sitting's close with those readings copied beside their pointers.

⏺ B6 — COMPLETED AT THE SITTING'S CLOSE (2026-09-19T19:01:40Z) — the readings R-5B's record carries in H8-a's B6 slot, copied beside their pointers (R-5B §5/§6):
```text
R-5B B4-1 the stop:   hs-fresh · 18:34:28Z → 18:34:33Z
R-5B B4-2 the grade:  Result=success · NRestarts=0 · ExecMainStatus=143 · ActiveState=inactive · SubState=dead   (O-2's second reading on 6bd8508)
R-5B B4-3 the halt:   hs-fresh · 18:41:46Z · connection closed by remote host · OFF 13:45 · OUT 13:45 · re-labelled hs-fresh — H8-a + R-5B DONE — 6bd8508 · IN 13:45 · dongle in place · ON 13:46 (CT)
R-5B B5 the floor:    hs-dev-1 · 18:48:10Z · [PASS] boot-health — 6/6 positive · 0 forbidden · zigbee.network_resumed: channel=20 panId=0x774c · formed=0 · relinked=6 adopted=0 · registry rows=6
```
STOP-GATE H8a-5 (the bench card back · the floor [PASS] · the PAN unchanged): MET via R-5B. F-1 was read a second time on R-5B's stop (R-5B B4-2b): identical shape.

## §9 Deviations ledger + THE FINDINGS CARD FOR THE HUB
- Deviations (tier · block · what · why · Z):
- THE FINDINGS CARD (≤1.5 KB, at close-out): what the wire showed that the desk did not predict · the stop-proof · the three things you would change in the packet:

- **D-1 · OP (operator slip, no tier — no instrument change, no rig change beyond two empty dirs) · §1 · 2026-09-19T17:10:54Z** — the §1 block was pasted into an open `ssh pi` session (hs-dev-1, user homesynapse) before the desktop. Effect on the BENCH card, from the output: `mkdir -p ~/r3-history` and `mkdir -p ~/h8a-artifact` created (empty) in /home/homesynapse; the `&&` chain died at `powershell.exe: command not found`; no file moved, nothing deleted, s31/nightly untouched, the bench still up. Left in place (delete nothing). One T2 read ordered to confirm the two dirs are empty (filed below). ASK: the hub rules whether the two dirs move aside or stay. Output lines verbatim (the echoed command is §1's block, omitted):
```text
homesynapse@hs-dev-1:~ $ hostname; date -u +%H:%M:%SZ; Z=$(ls -t ~/Downloads/distribution-artifacts-arm64*.zip | head -1); … [§1 block verbatim]
hs-dev-1
17:08:44Z
ls: cannot access '/home/homesynapse/Downloads/distribution-artifacts-arm64*.zip': No such file or directory
ls: cannot access '': No such file or directory
sha256sum: '': No such file or directory
PUBLISHED 11f3a79e6370b6e8e8155a7b3deaaced3eaf6fde3bdfa7a482137579d2aa8a75
-bash: cygpath: command not found
-bash: cygpath: command not found
-bash: powershell.exe: command not found
homesynapse@hs-dev-1:~/h8a-artifact $ exit
```

  - D-1 T2 read, filed 2026-09-19T17:14:21Z — both dirs empty on hs-dev-1 (created 13:08 card-local = 17:08Z); nothing else on the bench changed.
```text
hs-dev-1
/home/homesynapse/h8a-artifact:
total 8
drwxrwxr-x  2 homesynapse homesynapse 4096 Sep 19 13:08 .
drwx------ 28 homesynapse homesynapse 4096 Sep 19 13:08 ..

/home/homesynapse/r3-history:
total 8
drwxrwxr-x  2 homesynapse homesynapse 4096 Sep 19 13:08 .
drwx------ 28 homesynapse homesynapse 4096 Sep 19 13:08 ..
```

- **D-2 · T1 (instrument) · B0-4 · 2026-09-19T17:25:04Z** — `cut -c1-160` on the `zigbee.network_resumed` line truncates at `panI`: journald's prefix (`Sep 19 13:17:39 hs-fresh homesynapse[924]: `) + the app's own stamp/thread/class (`13:17:39.981 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- `) consume ~135 of the 160 columns. The PAN never prints. Fix: one read-only re-read of the same line at `cut -c1-240` (below); the same widening applied forward to B1-4's `cut -c1-160` when handed. Nothing measured changes.

- **D-3 · NAV (navigator error, no rig effect) · B1-2 · 2026-09-19T17:27:53Z** — the navigator's B1-2 ⏺ carries a false "card clock ~6 min behind" note, derived from stamps the navigator quoted from memory in chat rather than from the record; the record's stamps show the card consistent to the second. Corrected by an appended line under B1-2 (never a rewrite). Rule adopted for the rest of the sitting: every stamp quoted in chat is read back from the filer's output. No probe was run, nothing on the rig changed.

  - D-2 applied forward, 2026-09-19T17:29:42Z: B1-4 handed with `cut -c1-160` → `cut -c1-240` on its resumed/schema_registered grep; nothing else in the block changed.

- **D-4 · OP (operator slip; two inert side-effects on the held card) · B2-3 · 2026-09-19T17:33:23Z** — the desktop capture block ran at the card's prompt. Effects on hs-fresh, from the output: empty dir tree `/home/nick/Desktop/Code/ClaudeFolder/nexsys-hivemind/context/audits/2026-09-06_H8a_v113-wire-capture` created; `192.168.1.80` (the card itself) appended to `/home/nick/.ssh/known_hosts`. No copy, no delete; ~/h8a intact. Left in place (delete nothing). Navigator's own change from here: WHERE lines in chat now also name the exact PROMPT the block must be pasted at, and the window is one — `exit` off the card before any desktop block. ASK: the hub rules whether the empty tree on the card moves aside or stays.

- **D-5 · T2 (one read-only probe, three counts + grep, on the B1 invocation) · B3-2 · 2026-09-19T17:39:56Z** — ordered to characterize F-1 (no `transport_closed_orderly`; `transport_failed` + watchdog reopen during the stop). Result filed under B3 as ⏺ B3-2b. Nothing on the rig changed.


### THE FINDINGS CARD FOR THE HUB (navigator, 2026-09-19T19:01:40Z)
**What the wire showed that the desk did not predict.** (1) **F-1** — the stop's transport path: the desk (FAILCHAN §10-O) predicted `transport_closed_orderly`; the wire, on 2 of 2 stops, shows the shutdown hook closing the serial port under a read loop that was never told to stop (`serial read error: port dead or closed` on a clean link, `retransmits=0 crcRejects=0 timeouts=0`), the PortWatchdog re-opening and fully re-negotiating the NCP (ASH → EZSP v13 → ncp_configured, +1.6 s), and the JVM exiting 48–60 ms later. systemd grades it `success` because 143 is 143. The next start resumed cleanly each time, so nothing broke — but the orderly path is dead code on the wire. (2) **Every entities row carried an instant** (the desk said ≥1): the projection replays the log at boot, so two rows still showed 09-13 instants six days and one upgrade later, and the live rows' instants pre-dated the invocation's own resume by minutes. (3) **Row 7 is 26 vs 0**: journald sees none of the application's WARNs. (4) **§1's gate caught a stale artifact on the first try** (the 09-13 zip, hash 883c5f8d… = a458a64), exactly R-4c's D-2 class — the anonymous-origin gate is worth its two minutes. **The stop-proof.** Clean, twice, on one artifact: `success · 143 · inactive · dead · NRestarts=0` at 17:35:02Z and 18:34:28Z; with R-4c's on a458a64, O-2 has three readings on two artifacts; the unit carries `SuccessExitStatus=143 · Restart=always`. **Three things to change in the packet.** (a) `cut -c1-160` → 240 on every journal grep that must show `panId=` (B0-4, B1-4): the app's prefix eats ~135 columns. (b) Every WHERE line names the PROMPT the block is pasted at (`nick@hs-fresh:~ $` vs `Nick@DESKTOP-SRK0P9D MINGW64`) and the walk uses ONE window with an explicit `exit` before any desktop block — two of tonight's five deviations were desktop blocks run on a card. (c) B3-2's EXPECTED should carry the orderly-close token as a COUNT across the invocation (`closed_orderly=`, `transport_failed=`, `port_reopened=`) rather than a hope in the tail — tonight's T2 probe is the block as it should read.

## §10 Hub verdict surface (the hub writes this at intake)
