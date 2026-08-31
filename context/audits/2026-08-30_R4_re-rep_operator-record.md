<!--
file: context/audits/2026-08-30_R4_re-rep_operator-record.md
purpose: R-4 ⏺ RECORD OF ACCOUNT — the re-rep on the shipped artifact (packet: context/handoff/2026-08-27_R4_re-rep_operator-packet.md, ★-amended v58 b7). Filed by the R-4 NAVIGATOR session (boot: context/handoff/2026-08-30_R4_navigator_session-prompt.md). The hub audits and commits; the navigator committed NOTHING.
audience: the hub (audit → the fence-lift decision) · Nick (operator of record)
state-type: operator record — CLOSED; sections consolidated at close-out per §F
status: CLOSED-PENDING-HUB-AUDIT. Sitting ran Sun 2026-08-30 16:25 → 19:12 CT (21:25 → 00:12Z Mon). 35 operator paste-backs banked.
size note: this record is ~29 KB, ABOVE the packet §F ~12 KB target. The overrun is deliberate and is reported rather than hidden: the sitting produced four unforeseen packet deviations (D-d/D-e/D-f + O-2), a hub-ruled deviation attempt with a pre-filed prediction, three reproducible packet instrument defects, and two substantive findings (F-R4-1, F-R4-2) — plus the hub's three close-out additions. Reaching 12 KB would require deleting ⏺ evidence or findings the hub has asked for. The navigator has already cut the record from 51 KB by removing its own redundant prose and trimming log prefixes; a further cut should be a hub instruction naming what to drop.
form note: ⏺s are preserved as their DECISIVE SUBSTRINGS (journal prefixes `Aug 30 hh:mm:ss hs-fresh homesynapse[pid]:` and java class paths trimmed) for the size budget. No hash, version, ULID, count, timestamp or verdict has been altered. Section stamps are FILING times, not event times — event times are stated inline where they matter.
-->

# R-4 re-rep — operator ⏺ record (Sun 2026-08-30, the shipped artifact on the held card)

## §0 VERDICT SURFACE

**THREE OF FOUR. The record does not support the fence lift. C4 was never attemptable — for a baseline reason now precisely identified (F-R4-2), not an artifact regression.**

**The four R4-4 criteria**
- **C1 network resumed — ✓ MET.** `network_resumed: channel=20 panId=0x774c` on every one of FIVE service starts; `network_formed` = 0 on every one; close-count resumed 6 / formed 0.
- **C2 ≥1 device Available + store freshness in-window — ✓ MET.** Both live entities `AVAILABLE`, `stale:false`; `state_reported` at pos 75 (23:19:14Z) and pos 73 (23:18:14Z), inside 23:05:06Z–23:50:06Z.
- **C3 rows delta + discriminator 0 — ✓ MET.** ROWS-W0 70 → ROWS-W1 80; throw-discriminator `0`.
- **C4 one bench-hero run + rendered explanation, re-bound — ✗ MISS-BLOCKED.** `/api/v1/runs` = `{"data":[]}`; `bench-hero` `lastRunId: null`. The (b) re-bind (ruling R-1) was UNATTEMPTABLE, not failed. **Re-bind attempts used: 0 of 2.**

**Per-section**
| § | Verdict |
|---|---|
| §1 fetch + hash | **MET** · R4-1 CLOSED (after D-d) |
| §2 boot glance | **MET** (swap skipped D-a; digest deferred D-b — later satisfied) |
| §3 artifact on | **MET** · R4-2 CLOSED · O-1 raised + resolved |
| §4 drop-in off | **MET** — the crux; loosening proven in the shipped unit |
| §5 measured boot | **MET** · R4-3 CLOSED (after D-e) · C-1 captured |
| §6 arm + evidence | **PARTIAL** — C1/C2/C3 MET, C4 MISS-BLOCKED; D-f, D-g |
| §6b power-loss leg | **NOT RUN** — hub ruling (precondition fails on C4) |
| §7 restore | **MET** — floor `[PASS] 6/6 · 0 forbidden`; O-2 raised |

**⏺ census: 35 operator paste-backs banked.** Gates: G1 CLOSED · G2 banked · **G3 CONFIRMED @ 22:56Z** ("I read 6, and am ready to run the commands now") · R4-1/R4-2/R4-3 CLOSED · R4-4 three-of-four.

**Findings and observations for the hub**
- **F-R4-1** — on this rig the shipped artifact never converts a live, powered, adopt-listed device into an adopted device. Two short presses in a correct 254 s window, plus a newly-powered Hue flicked twice in a second window: zero `device_announce` / `device_proposed` / `proposal_accepted` / `device_adopted` / `reporting_configured` / `device_interview` / `entity_registered`.
- **F-R4-2 (MAJOR — explains F-R4-1 and C4)** — the held card and bench card carry **divergent registries for the same physical fleet**, and bench-hero's refs belong to the BENCH card. The cloned custody carried the Zigbee network (PAN/channel/keys — resumed flawlessly six times) but **not the device/entity registry**. Detail in §7.
- **O-1 RESOLVED** — postinst printed the first-run pairing-token banner on an UPGRADE; the token pair was NOT rewritten. Fence intact.
- **O-2 OPEN** — the shipped unit lands in systemd state `failed` after a clean operator `systemctl stop` (packet expects `inactive`). Likely pre-existing: the packet's own §5 opens with `reset-failed`. Cause not recoverable tonight; persists on the held card.
- **C-1 OPEN** — `Configuration issue [WARNING] at 'integrations.zigbee': property 'zigbee' is not defined in the schema and the schema does not allow additional properties` on EVERY start. The shipped schema does not admit the config layout the working deployment uses; the service runs on a WARNING.
- **PACKET INSTRUMENT DEFECTS (three, all reproducible)** — (i) §1's unpack/scp globs assume a flat artifact; the zip nests at `deb/build/`. (ii) §5's `journalctl -b … | head -30` returns the PRE-§4 run on a long-uptime machine. (iii) §6's token gate cannot pass: extraction regex class `[A-Za-z0-9+/=_-]` contains `-` so `tail -1` selects the helper's 64-dash rule, and the real token is **43** characters (44-byte file = 43 + newline), not 44. **Recommended amendment: read the token from the file and gate `-ge 40`.**

**Asks of the hub**
1. Adjudicate three-of-four against the §8 guard (any anomaly holds the lift one beat). Anomalies present: O-2, C-1, and the three instrument defects.
2. Rule on F-R4-2 as a **baseline correction** — the packet's baseline says "the CLONED bench custody (resumed, six devices)"; correct as to custody, incorrect as to a six-device registry on the held card.
3. Decide whether a C4 re-run needs a registry-carrying clone, or a re-bind to the held card's own entities plus an adopted light.
4. Next-sitting reads: `systemctl show -p ExecMainStatus -p Result homesynapse.service` on the held card (O-2), and whether `adoption_maps_rehydrated` appears there at all.
5. §6b never ran and remains available.

## §1 Fetch + hash (desktop) — MET · R4-1 CLOSED
**§1a origin echo (CI run 33333075509, arm64) @ 22:13Z** ⏺
```
hs_version=0.1.0+git20260830.201400.g7c57d7f
version-grammar echo green: 0.1.0+git20260830.201400.g7c57d7f (scheme 0.1.0+git<YYYYMMDD.HHMMSS>.g<sha>; .deb Version=0.1.0+git20260830.201400.g7c57d7f; image VERSION=0.1.0+git20260830.201400.g7c57d7f; sha256 452a2f95a89c4021af53916dfd0b63ad27ca804db455af0c1c6552de1b216937 homesynapse_0.1.0+git20260830.201400.g7c57d7f_arm64.deb)
```
sha256 == the PINNED origin hash EXACT; version identical on all three echo surfaces.

**D-d — THE HASH-CHAIN REMEDIATION, IN ORDER** (hub close-out item (c)):
1. **Stale zip found.** §1's block reported `sha256sum: 'homesynapse_*_arm64.deb': No such file or directory`; read-only inspection showed the ONLY .deb present was the OLD `homesynapse_0.1.0+git20260823.231355.gdec35be_arm64.deb`, sha `8156f4cb9553883b882375b915594f01fe91dc5702ce09aad65df48db25b843f` (≠ pinned), and `~/Downloads/distribution-artifacts-arm64.zip` dated **2026-08-27 21:29** — the R-3a-era archive. The R-3b artifact had never been fetched; Expand-Archive re-unpacked the stale zip. Second cause: the artifact nests at `deb/build/`, so the block's top-level globs (and its opening `mv`) could not match.
2. **mv-sorted (DELETE NOTHING).** Stale zip → `~/r3-history/distribution-artifacts-arm64-R3a-20260827.zip`; stale .deb → `~/r3-history/`. Verified: `ls: cannot access '/c/Users/Nick/Downloads/distribution-artifacts-arm64*.zip': No such file or directory` and `find ~/r3-artifact -name '*.deb'` EMPTY.
3. **Correct artifact fetched and verified against the pinned hash.** ⏺
```
-rw-r--r-- 1 Nick 197121 62854240 Aug 30  2026 homesynapse_0.1.0+git20260830.201400.g7c57d7f_arm64.deb
452a2f95a89c4021af53916dfd0b63ad27ca804db455af0c1c6552de1b216937 *homesynapse_0.1.0+git20260830.201400.g7c57d7f_arm64.deb
```
Exactly ONE .deb at the shipping glob's surface; `+git` date 20260830 orders ABOVE 20260823. Size 62,854,240 B (the packet's "≈61.8 MB" is an authoring approximation; the hash is the instrument).

## §2 Boot glance (held card) — MET @ 22:21Z
Physical swap SKIPPED (**D-a**, card already in); bench digest DEFERRED (**D-b**, satisfied at §7). ⏺
```
Sun 30 Aug 18:21:20 EDT 2026
0.1.0+git20260823.231355.gdec35be
active
17:15:58.482 zigbee.port_identity_captured: stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false
17:15:58.603 zigbee.network_resumed: channel=20 panId=0x774c
57
```
Clock is ET ✓ · pre-upgrade baseline version ✓ · active ✓ · resumed, ZERO formed ✓ · **ROWS-A OF RECORD = 57 @ 22:21:20Z** (supersedes the scaffold's provisional 56). **F-S20 REFERENCE STRING pinned** = the by-id string above. Card boot of record 17:15:58 ET.

## §3 The new artifact on — MET · R4-2 CLOSED
**§3a** benign non-execution: the desktop block was entered at the card's prompt; the card ssh'd to itself → `Permission denied (publickey)`; the `&&` chain aborted at hop 1 — no mv, no scp, no install. Sole state change: a self-entry appended to the card's own `known_hosts`.
**§3b ship to card @ 22:25Z** ⏺
```
---
homesynapse_0.1.0+git20260830.201400.g7c57d7f_arm64.deb  100%   60MB  46.3MB/s   00:01
452a2f95a89c4021af53916dfd0b63ad27ca804db455af0c1c6552de1b216937  /home/nick/homesynapse_0.1.0+git20260830.201400.g7c57d7f_arm64.deb
Version: 0.1.0+git20260830.201400.g7c57d7f
Architecture: arm64
```
**HASH CHAIN COMPLETE — 3 hops byte-identical: CI echo line → desktop disk → card home.**
**§3c baseline + integrity gate @ 22:32Z** ⏺ `57` / `ok` — ROWS-PRE == ROWS-A, no drift; install cleared.
**§3d the install @ 22:32Z (event), filed 22:44Z** ⏺
```
Preparing to unpack .../homesynapse_0.1.0+git20260830.201400.g7c57d7f_arm64.deb ...
Unpacking homesynapse (0.1.0+git20260830.201400.g7c57d7f) over (0.1.0+git20260823.231355.gdec35be) ...
Setting up homesynapse (0.1.0+git20260830.201400.g7c57d7f) ...
HomeSynapse Core is running.
 First-run pairing token: /var/lib/homesynapse/config/initial_api_token
0.1.0+git20260830.201400.g7c57d7f
0.1.0+git20260830.201400.g7c57d7f
active
60
ok
```
R4-2, condition by condition: **ordinary UPGRADE — "over", the token "downgrad" appears NOWHERE, apt never requested `--allow-downgrades`; the `+git<date>` ordering scheme is VERIFIED on the instrument** ✓ · version identical on `dpkg-query` AND `/opt/homesynapse/VERSION` — with the .deb field and the CI echo, **four surfaces** ✓ · active ✓ · ROWS 57 → 60, **zero row loss** ✓ · integrity `ok` ✓.
**O-1 RAISED AND RESOLVED @ 22:46Z.** The postinst printed the first-run pairing-token banner on an UPGRADE of a card already carrying an in-use token pair. ⏺ `/var/lib/homesynapse/config/initial_api_token  size=44  mtime=2026-08-13 07:35:41.051004828 -0400`; **install time `2026-08-30T22:41:32Z`, whose SOURCE is `stat -c %Y /var/lib/dpkg/info/homesynapse.list`** — i.e. when dpkg wrote the package file list (hub close-out item (a)). It reads earlier than §3d's `22:44Z` header only because section stamps are FILING times; the install completed 22:41:32Z and was filed ~2.5 min later. **Token file predates the install by 17 days ⇒ the upgrade did NOT rewrite the token pair; the banner is message text only. Fence UNBROKEN.** No token value was read, printed or filed at any point in the sitting.

## §4 The drop-in comes off — MET @ 22:48Z (THE CRUX)
Drop-in dir `mv`'d (not deleted) to `~/r3-history/homesynapse.service.d-removed-20260830`. ⏺
```
0
DevicePolicy=closed
DeviceAllow=char-rtc r
DeviceAllow=char-ttyACM rw
DeviceAllow=char-ttyUSB rw
SupplementaryGroups=dialout
PrivateDevices=no
```
`systemctl cat` drop-in sections = `0` ✓ · `PrivateDevices=no` (not `yes` — the unit IS R-3b's) ✓ · both predicted class rules present ✓ · `dialout` ✓ · `DevicePolicy=closed` ✓. **From here the shipped unit stands alone; every later observation is of the packaged artifact unaided.** Neutral: a third entry `char-rtc r` is also listed; the packet's expect says DeviceAllow *lists* the two class rules, not "exactly two".

## §5 The measured boot — MET @ 22:53Z · R4-3 CLOSED
**D-e (instrument):** the packet's `journalctl -u … -b | head -30` scopes to the MACHINE boot (17:15:48) and returned 30 lines of the PRE-§4 run (PID 844). Re-scoped to the service invocation. The stale window is not probative of the shipped unit but corroborates §10-Q: **19 `ingestion_unknown_sender` lines from 3 distinct un-adopted senders** — `0x15ac` (0x402 temp / 0x405 humidity), `0xf87d` (0x6 on/off), `0xa5da` (0x1 power config).
**§5b the real measured boot** ⏺
```
invocation=43f652fae02d44d5810632e65c5a2897  MainPID=1798  (pre-§4 PID was 844)
active
18:48:52.355 WARN Configuration issue [WARNING] at 'integrations.zigbee': /integrations: property 'zigbee' is not defined in the schema and the schema does not allow additional properties
18:48:53.226 registry.projection_live: devices=2 entities=2 position=40
18:48:53.634 zigbee.device_relinked: device=0x449FDAFFFE688F57 deviceId=01M19RHWWZXKD4MWM66KAW8MSR — re-pairing, no new adoption
18:48:53.635 zigbee.device_relinked: device=0xF044D3FFFE9C78D7 deviceId=01M19XN7MXFBA3P5BT4VDY0BM6 — re-pairing, no new adoption
18:48:55 [health-probe] ready (200) at http://127.0.0.1:7070/health
18:49:01.344 zigbee.port_identity_captured: stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false
18:49:01.434 zigbee.ncp_configured: zdo_flags=0x3 stack_profile=2 security_level=5
18:49:01.460 zigbee.network_resumed: channel=20 panId=0x774c
--- network_formed count, this invocation: 0
```
MainPID 1798 ≠ 844 ✓ · by-id **byte-identical to the §2 F-S20 reference** ✓ · resumed, same PAN ✓ · **formed = 0, explicit** ✓ · ready (200) ✓. Timings: start 18:48:51 → ready 18:48:55 (4 s) → resumed 18:49:01.460 (**10.6 s**).
**THE SUBSTANTIVE R-4 FACT: with the R-3a drop-in removed, the CI-built shipped artifact ALONE opened the SONOFF coordinator, configured the NCP, and resumed the existing Zigbee network (ch 20, PAN 0x774c) with zero network formation.**
**C-1 CONFIRMED ON THE SHIPPED UNIT** (line above, 18:48:52) and on every subsequent start.

## §6 The fleet arm + the evidence core
**WINDOW: ROWS-W0 = `70` @ `23:05:06Z`; close floor 23:50:06Z.**
**D-f — THE REAL CONFIG PATH** (hub close-out item (b)). The packet's `/etc/homesynapse/config/homesynapse.yaml` DOES NOT EXIST on this card (`cp: cannot stat`). The unit is the authority: `WorkingDirectory=/var/lib/homesynapse` · `Environment=HOMESYNAPSE_HOME=/var/lib/homesynapse` · `ExecStart=/opt/homesynapse/bin/homesynapse`. **The real config root is `/var/lib/homesynapse/config/`, holding `homesynapse.yaml` (1208 b) and `integrations/zigbee.yaml` (299 b).** All §6 edits were made to **`/var/lib/homesynapse/config/integrations/zigbee.yaml`** and to that file ONLY — `homesynapse.yaml` was **never edited** (the re-bind never happened), so `bench-hero` stands exactly as found. **Pre-R4 copies confirmed present @ 19:09 ET: `~/r3-history/homesynapse.yaml.pre-R4` (1208 b) and `~/r3-history/zigbee.yaml.pre-R4` (299 b)** (verified before any edit; the held card is now powered down, so this is the standing confirmation).
**Config as found** — `homesynapse.yaml`: `integrations: zigbee: !include integrations/zigbee.yaml`; `automation.automations:` one rule `bench-hero`, trigger `state_change entity_ref: 01KX1PB9AAB4VB3E10BD477TV3 attribute: occupied to: "true"`, five actions ALL targeting `entity_ref: 01KX1PA4HSJ581GASYB7DHE40F` (turn_on → PT6S → set_brightness 50 → PT6S → set_color_temperature 4550 → PT2S → set_color_temperature 4525 → PT20S → identify 5 s). `integrations/zigbee.yaml`: `serial_port: /dev/zigbee` · `channel: 20` · `adopt_devices` SIX IEEEs — `0x00178801101A09BB` Hue LCA017 · `0xF044D3FFFE9C78D7` SNZB-03P · `0x00124B002FA8D1C5` S31 Lite zb · `0xF044D3FFFED2A201` SNZB-02P · `0xF044D3FFFE1C1E8E` SNZB-01P · `0x449FDAFFFE688F57` SNZB-04P contact.
**Key definition — NAVIGATOR SOURCE LOOKUP, DISCLOSED for audit** (outside read-set §B; `/opt/homesynapse` yielded no text because jar entries are compressed). From `zigbee-config-schema.json` + `ZigbeeIntegrationAdapter.openPermitJoinWindow()`: `permit_join_duration`, integer SECONDS, `minimum 1, maximum 254, default 120`; out-of-range clamps with `permit_join_clamped`; **an ABSENT key returns early — the window NEVER opens**; the window opens on boot/restart only and a watchdog reopen never renews it; success emits `permit_join_opened: duration={}s`. Operator chose **254** (spec max) over the default for margin, since a lapsed window is only reopenable by another restart.
**§6-i THE ARM — MET.** `permit_join_duration: 254` written at `integrations/zigbee.yaml` line 3 → restart. ⏺ `invocation=4a3ee346d2de4616aa45c21eddad0587 MainPID=2043` · `active` · `19:17:28.969 zigbee.network_resumed: channel=20 panId=0x774c` · `19:17:28.999 zigbee.permit_join_opened: duration=254s`. Value accepted EXACTLY, **no `permit_join_clamped`** ✓; zero formed ✓. Window OPEN 23:17:28.999Z → CLOSE 23:21:43Z.
**§6-ii THE WAKE — [MISS].** TWO short presses on the SNZB-03P inside the full 254 s window. ⏺ the only in-window Zigbee traffic: `19:18:54.604 zigbee.ingestion_unknown_sender: nwk=0xf87d cluster=0x6; frame skipped`. **ZERO announce / proposed / proposal_accepted / adopted / reporting_configured / interview.** The two known devices arrive only by boot-time `device_relinked`.
**§6-iii D-g (hub-ruled) — EXECUTED, BOUNDS HONOURED, FAILED.** Prediction pre-filed BEFORE the act (§9). Executed: key verified still present → restart (`invocation=44a1db37b49a44979d6a828a6427c1d7 MainPID=2196`) → `network_resumed` ch20 PAN 0x774c, **zero formed** → `19:31:55.057 permit_join_opened: duration=254s` (window 23:31:55Z → 23:36:09Z) → Hue powered at the wall for the first time this sitting → flick 1 (off ~10 s/on) → flick 2. ⏺ after both flicks: `registry.projection_live: devices=2 entities=2 position=40` — unmoved; zero adoption chain of any kind.
*Correction, appended not rewritten:* the earlier attribution of `0xf87d cluster=0x6` to the Hue is **WITHDRAWN** — the lamp was off at the wall until 23:31Z, so the bulb was unpowered; `0xf87d` reports on a steady 5-minute :54s cadence (17:18:54, 17:23:54, 17:28:54, 19:18:54, 19:33:54), i.e. a mains device, most consistent with the S31 Lite zb plug.
**§6-iv DISARM — MET.** Key removed; file back to its original 9 lines, content-equivalent to `zigbee.yaml.pre-R4`. ⏺ `invocation=488c36798cf647c6ae75e1de8f63eff0 MainPID=2327` · `permit_join_opened` count **`0`** (absent key ⇒ no window — source semantics confirmed on the instrument) · `19:37:54.299 zigbee.network_resumed: channel=20 panId=0x774c` · `network_formed` count **`0`**.
**FIVE-START TALLY:** starts at 17:15:58, 18:48:51, 19:17:19, 19:31:46, 19:37:48 ET — `network_resumed` on every one, `network_formed` **0** on every one. The ONE COORDINATOR / ONE BOOT invariant held throughout.
**§6-v WINDOW CLOSE @ 23:50:50Z** (45m44s after ROWS-W0). ⏺ `80` · `23:50:50Z` · discriminator `0` · resumed-count `6` · formed-count `0` · then HTTP 403 `"the supplied bearer token is invalid, expired, or revoked"` (correlation_id `b10ff307-ef79-4fb3-a140-e03e521a0c33`), `TOKLEN-OK` absent. **C3 = MET** (70→80, discriminator 0). **C1 = MET, re-confirmed.**
events schema ⏺ (read ONCE, the C2 instrument): 27 columns; the timestamp columns are `ingest_time` and nullable `event_time` (both INTEGER, MICROSECONDS), indexed via `idx_events_ingest_time` and `idx_events_event_time(COALESCE(event_time, ingest_time))`. Full schema recoverable from the store.
**TOKEN GATE — PACKET DEFECT, NOT A TOKEN FAULT.** Re-read from the file: ⏺ `token_len=43`, **`http=200`**. The token is **43 characters**; the file is 44 BYTES (43 + trailing newline), matching O-1's `size=44`. The packet's `test ${#TOK} -eq 44` therefore CANNOT pass on a valid token, and the 403 came from the helper-block regex selecting the 64-char dashed rule (class `[A-Za-z0-9+/=_-]` contains `-`, `tail -1` takes the rule). No token value was ever printed, pasted or filed.
**§6-vi C2 — MET @ 23:55Z.** `ingest_time` is MICROSECONDS (`MAX=1788133066589853` = 2026-08-30T23:37:46Z). ⏺ store freshness:
```
pos 75  state_reported  ingest_utc 2026-08-30 23:19:14  event_utc 23:19:14  subj12 01A053DA9EB5  ENTITY
pos 73  state_reported  ingest_utc 2026-08-30 23:18:14  event_utc 23:18:14  subj12 01A053DA9EB5  ENTITY
(paired state_changed at pos 76 / 74, same entity, same timestamps; older state_reported at pos 67/65/63/61 = 22:45:36 / 22:44:36 / 22:43:00 / 22:42:01, pre-window)
```
census: `integration_started` 23 (last_pos 80) · `integration_stopped` 8 (79) · `state_changed` 11 (76) · `state_reported` 15 (75) · `device_adopted` 2 (42) · `availability_changed` 2 (41) · `entity_registered` 2 (40) · `device_registered` 2 (39) · `device_discovered` 2 (38) · `integration_health_changed` 13 (26).
⏺ `/api/v1/entities` (200): `{"data":[{"entityId":"01M19RHWXYZYJMM26SX0E41HXN","availability":"AVAILABLE","stale":false},{"entityId":"01M19XN7NNQQ8S3JJF09T6YKKY","availability":"AVAILABLE","stale":false}],"meta":{"viewPosition":80}}`
C2: **≥1 Available — TWO entities, both AVAILABLE, both `stale:false`** ✓ · **freshness IN-WINDOW — `state_reported` pos 75 (23:19:14Z) and 73 (23:18:14Z) inside 23:05:06Z–23:50:06Z**, positions 71–80 being the in-window rows ✓. (`availability_changed` last at pos 41 pre-window — availability is a held state, not a per-window event.) `subject_ref` is a 16-byte BLOB; the reporting entity is recorded by hex prefix `01A053DA9EB5` and was not resolved to a ULID from the store alone.
⏺ `/api/v1/runs` (200): `{"data":[],"pagination":{"nextCursor":null,"hasMore":false,"limit":50},"meta":{"viewPosition":80}}` — **ZERO runs**; `viewPosition` 80 == ROWS-W1 exactly (read API and store agree).
⏺ `/api/v1/automations` (200): `{"automationId":"01M1AGJHC9JMDJ4YX1AQQDY37R","name":"bench-hero","enabled":true,"components":[StateChangeTrigger, CommandAction, DelayAction, CommandAction, DelayAction, CommandAction, DelayAction, CommandAction, DelayAction, CommandAction],"lastRunId":null}`
**C4 = MISS-BLOCKED, confirmed on the read API not inferred.** `bench-hero` LOADS CLEAN on the shipped unit — present, `enabled:true`, 10 components parsing exactly as the yaml declares (1 trigger + 5 commands + 4 delays) — but `lastRunId: null`, never fired. The live entities `01M19RHWXYZ…` / `01M19XN7NNQ…` match NEITHER configured ref. The trigger could have been re-bound to the live motion entity; **the action target could not — no light entity exists in the registry at all**, and all five CommandActions target one. **Re-bind attempts used: 0 of 2.**
**§6 CLOSES: C1 MET · C2 MET · C3 MET · C4 MISS-BLOCKED. §6b NOT RUN (hub ruling).**

## §7 The restore (bench night) — MET
**§7a held-card stop — [MISS vs expect].** ⏺ `systemctl is-active` → **`failed`** (packet expects `inactive`), then `shutdown -h now` → `Connection to hs-fresh.local closed by remote host.` → **O-2** (see §0). Physical swap executed; held card relabelled `hs-fresh — R-4 DONE — 0.1.0+git20260830.201400.g7c57d7f · shipped unit · bench custody`; **the coordinator never left Port 2 at any point in the sitting.**
**§7b bench digest (D-b) — SATISFIED, and the bench went down ORDERLY, doubly evidenced.** Bundles newest-first: `boot-health-20260830T190604Z` · `command-s31-settle-20260830T083122Z` · `command-confirm-s31-20260830T083121Z`; newest holds `api-captures.json`, `app-log-slice.log`, `MANIFEST.txt`, `resolved.json`, `scenario.yaml`, `verdict.txt`, all 15:06 ET (matches the baseline's "restored 15:06 ET"). ⏺ instrument: `17:14:07.745 WARN zigbee.transport_failed: serial read error: port dead or closed; lastFrame=DATA(frm=5, ack=4, reTx=false) retransmits=0 crcRejects=0 timeouts=0 — the watchdog owns recovery` — **zeros across retransmits/crcRejects/timeouts = the §10-O ORDERLY-CLOSE signature.** ⏺ operator action, from the bench card's own shell history: `1809  sudo shutdown -h now`. Port closed 17:14:07 ET; held card booted 17:15:58 ET — a 1m51s swap gap. **D-b CLOSED, no residual uncertainty.**
**§7c THE FLOOR — MET @ 00:07Z. `[PASS] boot-health — 6/6 positive · 0 forbidden`.** ⏺
```
[ok] log 'registry.projection_live: devices=6 entities=6' min=25065 — 20:07:07.281 position=25065
[ok] log 'zigbee.adoption_maps_rehydrated: devices=6' — 20:07:07.680
[ok] log 'zigbee.device_relinked' x2(at-least) — 20:07:07.677 device=0x449FDAFFFE688F57 deviceId=01KY12MQVQ204M1VP39F1ZDM33
[ok] log 'zigbee.network_resumed: channel=20 panId=0x774c' — 20:07:15.420
[ok] log 'zigbee.port_identity_captured:' — 20:07:15.305 stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false
[ok] api /api/v1/entities {"rows": 6, "ulids": ["01KX1PA4HSJ581GASYB7DHE40F", "01KX1PB9AAB4VB3E10BD477TV3", "01KXW0157SP56CCSGJCNDCSQNG", "01KXW13WF0D6TYGN13WXHTG87K", "01KXW1W1SBJZERC9MBAMV2DWKE", "01KY12MQW954E4XYNKH0Y5H8VX"]}
[PASS] boot-health — 6/6 positive · 0 forbidden
  [--] bundle: /home/homesynapse/hs-bench/bundles/boot-health-20260831T000716Z
```
Floor `[PASS]` ✓ · **PAN `0x774c` UNCHANGED** ✓ · **F-S20 by-id string BYTE-IDENTICAL to §2** ✓ · RADIO UP after 13 s (expect 12–18 s) ✓ · runner `B3.1-2026-08-02-postwindow @ 16e672d`.
**§7d bench night — CONFIRMED @ 00:11:20Z.** ⏺ `[OK] running (pid 2347)` · `registry.projection_live: devices=6 entities=6 position=25065`. The bench floor is `[PASS]` and running, ~7 h ahead of the 03:00 CT Tue deadline.

**FINDING F-R4-2 (MAJOR — the mechanism behind F-R4-1 and C4), from the §7 floor output:**
- The bench card's `/api/v1/entities` returns 6 ULIDs **including `01KX1PB9AAB4VB3E10BD477TV3` and `01KX1PA4HSJ581GASYB7DHE40F` — exactly the trigger and action refs written in the held card's bench-hero rule.** Those refs are live and valid **on the bench card**.
- The held card returned only `01M19RHWXYZYJMM26SX0E41HXN` and `01M19XN7NNQQ8S3JJF09T6YKKY` — neither is a bench-hero ref.
- Device ULIDs diverge for the SAME IEEE: `0xF044D3FFFE9C78D7` → bench `01KX1PB9A5931A8G0F0X03QXT2` vs held `01M19XN7MXFBA3P5BT4VDY0BM6`; `0x449FDAFFFE688F57` → bench `01KY12MQVQ204M1VP39F1ZDM33` vs held `01M19RHWWZXKD4MWM66KAW8MSR`.
- Store depth diverges: bench `position=25065`, `adoption_maps_rehydrated: devices=6`, all six relink every boot; held `position=40`, `devices=2 entities=2`, ROWS 57→80 across the whole sitting.
**Consequence: the cloned custody carried the ZIGBEE NETWORK (PAN 0x774c, channel 20, keys — the held card resumed it flawlessly five times) but NOT the DEVICE/ENTITY REGISTRY. bench-hero on the held card was bound to refs that never existed in that card's registry — which is why C4 was unattemptable, and why no join window or power-cycle could have rescued it.** The packet's baseline "the CLONED bench custody (resumed, six devices)" is correct as to custody and incorrect as to a six-device registry on the held card. Scope caveat: the held card's greps did not include `adoption_maps_rehydrated`, so its presence there is UNESTABLISHED and not claimed.

## §9 Deviations ledger
- **D-a** §2 physical swap pre-executed before the sitting opened (dispatch).
- **D-b** §2 bench-digest ⏺ deferred to §7 — **SATISFIED and CLOSED** (orderly shutdown, doubly evidenced).
- **D-c** ROWS-A filled from the full §2 boot glance — **57 @ 22:21:20Z** of record.
- **D-d** §1 artifact nests at `deb/build/` AND the R-3b zip was never fetched (stale 2026-08-27 zip re-unpacked). Remediated by mv-sort, nothing deleted; R4-1 closed on the pinned hash. Full sequence in §1.
- **D-e** §5 `journalctl -b … | head -30` returned the PRE-§4 run; re-scoped to `_SYSTEMD_INVOCATION_ID`; R4-3 closed on the corrected window.
- **D-f** the packet's `/etc/homesynapse/config/homesynapse.yaml` does not exist; real root `/var/lib/homesynapse/config/`, zigbee a separate `!include`. Backups honoured at the real path.
- **D-g OPERATOR DEVIATION (hub-ruled), PRE-FILED @ 23:26Z BEFORE THE ACT.** *(The hub's ruling text labels this "D-d"; relabelled D-g here to avoid collision. Hub wording verbatim:)*
  > "D-d OPERATOR DEVIATION (hub-ruled): Hue power-cycle to force rejoin — not a packet step. Prediction, filed first: reopened permit-join window (254s) + Hue switch off ~10s/on → rejoin/announce → device_proposed → proposal_accepted: source=config → device_adopted → reporting_configured. Bounds: ONE window, ≤2 flicks, expiry = attempt over."
  Executed exactly to those bounds; **the prediction did not occur** (§6-iii). Outcome banked as F-R4-1.
- **Navigator disclosure:** to avoid inventing a config key, the navigator read `homesynapse-core` SOURCE for the `permit_join_duration` definition — outside read-set §B, disclosed for audit. No other project state was re-derived.

## §10 Hub verdict surface (fills at audit)
- pending
