<!--
file: _scratch/card-sitting-2026-08-23/2026-08-23_card-sitting_Blocks-1-3_operator-return.md
suggested destination: context/audits/2026-08-23_card-sitting_Blocks-1-3_operator-return.md
                       (NOT written into the repo — R-7b is live on the core checkout and the hivemind
                        census discipline belongs to the hub, not to this file)
purpose: OPERATOR RETURN for Blocks 1–3 of `context/handoff/2026-08-21_card-sitting_operator-packet.md`,
         run Sunday 2026-08-23 in daylight. Layer-1 operator evidence + per-line adjudication, assembled for
         hub adjudication. Every ⏺ in packet §5 order; every packet prediction scored; every deviation
         disclosed; fifteen findings, four of which change work already scheduled.
packet:  UNCHANGED — verified byte-identical to the issued copy at md5 bd42cb934547ba8c07ebff888709067c (27,639 B).
clocks:  Operator desktop = CDT. Both Pi cards = America/New_York (EDT). Pi time = CT + 1 h.
         Every Pi-side stamp below is ET and is marked as such. See F-S21 — one TZ-label ambiguity found in
         the hub's own §OP-A record, surfaced by this sitting's artifacts.
status:  COMPLETE. All ⏺ slots filled. No STOP-gate tripped; no step retuned on a card; nothing deleted.
-->

# The Sunday Card Sitting — Operator Return, Blocks 1–3

## §0 Verdict

**R-1/R-2's hardware half is PROVEN, and the rig is restored on both sides.**

On one card, with one byte-identical instrument (H13), the held card's known-bad artifact `0.1.0+gd26777c`
produced **7 throw-signature lines with 10 event rows**; the artifact rebuilt from core `7c9e4fa` produced
**0 throw-signature lines with 14 event rows in a fresh boot**, followed by `run-smoke.sh` returning **18/18
PASS across nine checks** and `INSTALL-SMOKE PASSED ✓` on real hardware. The bench then restored to
**`[PASS] boot-health — 6/6 positive · 0 forbidden`** with the coordinator returned to its exact hub port and
the fleet reporting **5 AVAILABLE + 1 UNAVAILABLE**, the expected census.

**P-1, P-2 and P-3 are all met.** No STOP-gate was tripped. No step was retuned on a card. Nothing was deleted.
No token value ever entered the evidence set.

Four secondary objects closed alongside: **the Block-0 proximity confounder is discharged** (F-S7), **P-1's
channel census is banked and coherent at the wall clock** (§3.1), **the layer-2 audit's stale-tree defect is
disproven at the instrument** (§3.3), and **the bare-id dpkg ordering is proven live** (F-S18).

Against that, four things the hub must act on: **E-P1's refutation invalidates a premise of R-3's E3-GREEN
block** (F-S9); **the packet's Block 3 would have failed as written** because the bench app is not running
after a restore boot (F-S15); **the first-run mint and the rotate path disagree on token file mode, and
run-smoke structurally cannot see it** (F-S10); and **P-3's config-listing prediction was stale before the
sitting began** — superseded by today's own §OP-A (F-S19), which in turn surfaced a timezone-label ambiguity
in the hub's record (F-S21).

Two of the addendum's own enrichment predictions went untested because those enrichments were withdrawn
mid-sitting to reduce operator load. Recorded as absences, not as passes.

---

## §1 Timeline

| CT (operator) | ET (Pi) | Act |
|---|---|---|
| 15:03:07 | — | PF-0 clock gate · PF-2 desktop artifact gate — both GO |
| 15:07:34 | — | PF-3 desktop rig · the disclosed Git-Bash slip (§5) |
| 15:08 | 16:08:00 | **PF-1** — bench floor, digest ×2, P-1 census, LAN, USB topology, recovery source |
| ~15:50 | 16:50:43 | Bench `shutdown -h now`; **coordinator OUT of Rosonway port 5** (D-3) — the WARN at F-S16 |
| ~15:54 | 16:54:10 | Held card boots; `homesynapse.service` active on `0.1.0+gd26777c` |
| ~15:55 | — | `hs-fresh.local` fails once, resolves on retry → `2600:1702:6e8a:aff0::47` (E-P2 met) |
| 15:56 | 16:56 | Artifacts pushed by `scp`; session in |
| ~15:57 | 16:54–16:59 | **BLOCK 1 — RED** |
| 16:03 | 17:03 | **BLOCK 2 part 1** — upgrade `0.1.0+gd26777c` → `7c9e4fa` |
| 16:06 | 17:06:05 / 17:06:24 | Reboot; service active 19 s after boot. **Discriminator = 0** |
| ~16:08–16:12 | — | `run-smoke.sh` — 18/18 PASS |
| ~16:12 | — | Re-install for the R-3 rig; L3 mask |
| 16:13 | — | Evidence files home |
| ~16:16 | — | Held card down and OUT (labeled) · **coordinator BACK into Rosonway port 5** · bench card IN |
| 16:18:53 | 17:18:53 | **`~/bench.sh start`** (D-4) — RADIO UP after 18 s; 6/6 relinked |
| 16:26:56 | 17:26:56 | **BLOCK 3** — `boot-health` (its own restart): RADIO UP after 13 s → **`[PASS] 6/6 · 0 forbidden`** |
| 16:27 | 17:27 | Rotation confirm + restore verification set |

Sitting opened 15:03 CT, ~11 h clear of the 03:00–04:15 CT guard. No block ran inside the guard.
Bench down-time across the swap: approximately 90 minutes.

---

## §2 Predictions scored

### The packet's own (§6)

| id | verdict | evidence |
|---|---|---|
| **P-0** (Block 0) | **CARRIED — GREEN** (adjudicated v55 b4) | Not re-run. Re-verified today at the bytes on **both** hops: desktop and bench copies at exact sizes and sha256 (§3.1). |
| **P-1** (Block 1, RED) | **MET on the primary arm** | rows **10** (≥ 1) **AND** matching-line count **7** (≥ 6), with `NoClassDefFoundError: jdk/jfr/Event` → `BusMetricsJfr.recordWriterQueueDepth:59` → `ClassNotFoundException: jdk.jfr.Event`. Both disjuncts satisfied simultaneously. **The both-clean refutation arm did not fire — F-23's upper bound stands.** |
| **P-2** (Block 2, GREEN) | **MET IN FULL** | `Version: 7c9e4fa` · `/opt/homesynapse/VERSION` = `7c9e4fa` · fresh-boot discriminator **0** · rows **14 > 10** · **18 `[smoke] PASS ` lines / nine checks**, including check 4's two positive lines · `INSTALL-SMOKE PASSED ✓` · re-install `HomeSynapse Core is running.` The conditional-store-reset sub-clause **did not apply** (`initial_api_token` present — F-S9). |
| **P-3** (Block 3) | **MET — with one prediction proven stale, not one result wrong** | `[PASS] boot-health — 6/6 positive · 0 forbidden` **verbatim**, bundle `boot-health-20260823T212709Z`. The config listing shows the rotation state **as of today's §OP-A**, not as of 08-20; the prediction was authored 08-21 and superseded by the hub's own act hours before this sitting. See **F-S19**. No act was taken; the packet's "⏺ and paste (no act)" instruction was followed exactly. |

**One magnitude note on P-1, disclosed rather than smoothed.** The packet describes 12–24 matching lines as
"the EXPECTED shape". The observed count is **7** — above the ≥ 6 threshold the prediction actually gates on,
but at its floor. Two named candidate contributors, neither verified: (a) the ≈6-throw estimate was formed in
the R1R2 era with a coordinator attached, and (b) this boot ran under the SD-5 fence with no radio present, so
the zigbee path had fewer opportunities to throw. **The class is proven either way; the magnitude is not
load-bearing for R-1/R-2.** Recorded so a future run seeing 12–24 is not read as a regression, and one seeing
7 again is not read as a novelty.

### The addendum's (E-P1…E-P5, filed pre-run)

| id | prediction | verdict |
|---|---|---|
| **E-P1** | `initial_api_token` ABSENT ⇒ the conditional store reset fires | **REFUTED.** Present, 44 B, Aug 13 07:35, and unchanged through the whole sitting. See **F-S9** — this refutation is load-bearing. |
| **E-P2** | `hs-fresh.local` resolves in minutes, not 90 s | **MET.** First `ping` returned "could not find host"; the retry resolved. |
| **E-P3** | The held card inherits the bench's LAN IP `192.168.1.80` ⇒ the `known_hosts` collision is live | **NOT TESTED.** mDNS resolved to **IPv6** `2600:1702:6e8a:aff0::47` and every ssh/scp went over it. The IPv4 fallback was never used and the collision never arose. Neither confirmed nor refuted. |
| **E-P4** | The held card's clock is correct and reads ET | **MET on the bench, INFERRED on the held card.** Bench: 15:07:34 CDT ↔ 16:08:00 EDT, UTC 20:08:00, RTC in UTC. Held card: every stamp internally consistent as EDT (16:54:10, 17:06:05, 17:06:24), but no independent `date` line was taken there — the pre-probe that would have taken it was withdrawn (D-2). |
| **E-P5** | `vcgencmd get_throttled` = `0x0` | **NOT TESTED.** Same cause — D-2 withdrawn. No under-voltage or thermal-cap reading exists for this sitting. Nothing in the results suggests one was needed; recorded as an absence, not an all-clear. |

---

## §3 ⏺ The record, in packet §5 order

### §3.0 Block 0 — carried forward (built 2026-08-22 03:16–03:21 CT; GREEN at every prediction; v55 b4)

Not re-run. The artifact pair of record:

| | |
|---|---|
| `.deb` | `homesynapse_7c9e4fa_arm64.deb` · **61,788,352 B** · `ed82ae8fa989fd7bf01373bba95ff5eb7df2a72fca825bc6bc271d0d666f2324` |
| tarball | `dist-7c9e4fa.tar.gz` · **33,982 B** · `db57fa90285b0a859eaca76963d225e16ac01af2ff4fc1d914c39579a122204d` |

### §3.1 Pre-flight

**⏺ PF-0 — clock gate** *(the v55 b4 harvest: "a time guard written as prose is not a gate")*

```
Sun Aug 23 15:03:07 CDT 2026
```

**⏺ PF-2 — desktop artifact gate**

```
-rw-r--r-- 1 Nick 197121    33982 Aug 22 03:22 dist-7c9e4fa.tar.gz
-rw-r--r-- 1 Nick 197121 61788352 Aug 22 03:22 homesynapse_7c9e4fa_arm64.deb
ed82ae8fa989fd7bf01373bba95ff5eb7df2a72fca825bc6bc271d0d666f2324 *homesynapse_7c9e4fa_arm64.deb
db57fa90285b0a859eaca76963d225e16ac01af2ff4fc1d914c39579a122204d *dist-7c9e4fa.tar.gz
```

Both sizes and both hashes exact. The `*` prefix is MSYS binary-mode marking — cosmetic. → **F-S6.**

**⏺ PF-3 — desktop rig**

```
DROP = /c/Users/Nick/Desktop/Code/ClaudeFolder/_scratch/card-sitting-2026-08-23   (created)
-rw-r--r-- 1 Nick 197121 411 Apr  2 20:19 /c/Users/Nick/.ssh/id_ed25519_pi
script: ABSENT in Git Bash
```

**⏺ PF-1 — the pre-swap bench floor** (`ssh pi`, 2026-08-23 16:08 EDT / 15:08 CDT)

`~/bench.sh status` → **`[OK] running (pid 51927)`**, boot log `bench-2026-08-23-131519.log`:

```
13:15:23.163  registry.projection_live: devices=6 entities=6 position=25065
13:15:23.567  zigbee.device_relinked: device=0xF044D3FFFED2A201 deviceId=01KXW0156Z1GJ3WCV2G516AKWS
13:15:23.567  zigbee.device_relinked: device=0xF044D3FFFE1C1E8E deviceId=01KXW13WEGRCT5C0XSQT8WZBG9
13:15:23.568  zigbee.device_relinked: device=0x00124B002FA8D1C5 deviceId=01KXW1W1RR66GV98D9QDPB4VXY
13:15:23.568  zigbee.device_relinked: device=0xF044D3FFFE9C78D7 deviceId=01KX1PB9A5931A8G0F0X03QXT2
13:15:23.568  zigbee.device_relinked: device=0x449FDAFFFE688F57 deviceId=01KY12MQVQ204M1VP39F1ZDM33
13:15:23.569  zigbee.device_relinked: device=0x00178801101A09BB deviceId=01KX1PA4GRZHY2GD37B5CFVQHY
13:15:23.569  zigbee.adoption_maps_rehydrated: devices=6
13:15:31.271  zigbee.network_resumed: channel=20 panId=0x774c
13:15:31.272  zigbee.network_up: stackStatusHandler reported EMBER_NETWORK_UP (buffered)
--- failure tokens ---   (EMPTY)
```

Clock: `Sun 23 Aug 16:08:00 EDT 2026` · Universal `20:08:00 UTC` · RTC `20:08:00`.

**`~/bench.sh digest 2` — THE NIGHTLY FLOOR, owed to the hub since v56 beat 1:**

```
2026-08-22 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.29s
2026-08-23 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.28s
```

→ **F-S7 — the Block-0 proximity confounder is discharged.**

**P-1 — the 02P channel census** (`bench.sh state 01KXW0157SP56CCSGJCNDCSQNG`):

```json
{"data":{"entityId":{"value":{"msb":116944059229647180,"lsb":-4150609780050960720}},
 "attributes":{"humidity_pct":{"value":56.0},"battery_pct":{"value":100},"temperature_c":{"value":23.0}},
 "availability":"AVAILABLE","stateVersion":78574,
 "lastChanged":1787515645.073185000,"lastUpdated":1787515655.083874000,"lastReported":1787515655.083874000,
 "staleAfter":null,"stale":false},
 "meta":{"viewPosition":112516,"timestamp":"2026-08-23T20:08:00.922131673Z"}}
```

**The beat-4 prediction holds on both limbs, and the read is coherent at the wall clock.** Values nest as
`data.attributes.<key>.value`. Instants are epoch-second numbers and resolve correctly: `lastChanged`
20:07:25.073 UTC · `lastUpdated` = `lastReported` 20:07:35.084 UTC · `meta.timestamp` 20:08:00.922 UTC — the
read is 25.8 s after the last update, and `lastChanged` trails `lastUpdated` by exactly 10 s (a report that did
not move the value). Consistent with the `date` line taken in the same second. → **F-S8** for two rendering
asymmetries.

**LAN / USB topology / recovery source:**

```
eth0             UP             192.168.1.80/24
Bus 003 Device 022: ID 10c4:ea60 Silicon Labs CP210x UART Bridge
lrwxrwxrwx 1 root root 7 Aug 23 04:32 /dev/zigbee -> ttyUSB0
Current status for hub 3-2.4 [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
  Port 1: 0100 power
  Port 2: 0103 power enable connect [10c4:ea60 SONOFF SONOFF Dongle Plus MG24 0ae2dd7cecf8ef11b80168135c2a50c9]
  Port 3: 0100 power
  Port 4: 0100 power
-rw-rw-r-- 1 homesynapse homesynapse    33982 Aug 22 04:20 /home/homesynapse/dist-7c9e4fa.tar.gz
-rw-r--r-- 1 homesynapse homesynapse 61788352 Aug 22 04:19 /home/homesynapse/homesynapse_7c9e4fa_arm64.deb
```

Port 2 byte-identical to the 2026-07-28 B2 record. Bench artifact mtimes place the Block-0 build at
Sat 04:19–04:20 EDT = 03:19–03:20 CDT — inside the recorded build window. → **F-S6.**

### §3.2 ⏺ Block 1 — RED on the held card (boot of 16:54:10 EDT)

```
$ dpkg -s homesynapse | grep -E "^(Status|Version):"
Status: install ok installed
Version: 0.1.0+gd26777c

$ systemctl status homesynapse.service --no-pager | head -12
     Loaded: loaded (/usr/lib/systemd/system/homesynapse.service; enabled; preset: enabled)
     Active: active (running) since Sun 2026-08-23 16:54:10 EDT; 5min ago
       Docs: file:/opt/homesynapse/VERSION
    Process: 895 ExecStartPost=/opt/homesynapse/libexec/health-probe.sh --wait --timeout 90 (code=exited, status=0/SUCCESS)
   Main PID: 890 (java)   Tasks: 39 (limit: 4810)   CPU: 5.639s

$ sudo ls -la /var/lib/homesynapse/data/ /var/lib/homesynapse/config/
/var/lib/homesynapse/config/:        drwx------  (mode 700)
-rw-r--r-- 1 homesynapse homesynapse  132 Aug 13 07:35 api_tokens
-rw-r--r-- 1 homesynapse homesynapse   26 Aug 13 07:35 home_id
-rw-r--r-- 1 homesynapse homesynapse   44 Aug 13 07:35 initial_api_token
drwxr-xr-x 2 homesynapse homesynapse 4096 Aug 13 07:35 schemas
/var/lib/homesynapse/data/:
-rw-r--r-- 1 homesynapse homesynapse 102400 Aug 13 07:52 homesynapse-events.db
-rw-r--r-- 1 homesynapse homesynapse  32768 Aug 23 16:54 homesynapse-events.db-shm
-rw-r--r-- 1 homesynapse homesynapse 123632 Aug 23 16:54 homesynapse-events.db-wal
drwxr-xr-x 2 homesynapse homesynapse   4096 Aug 23 16:54 zigbee

$ command -v sqlite3 || (apt-get update && apt-get install -y sqlite3)
→ sqlite3 3.46.1-7+deb13u1 INSTALLED (additive, lawful; "95 not upgraded" left untouched)
→ apt Err:8/Err:9 on trixie-updates Packages.diff/Index ("Need 4751 compressed bytes, but limit is 4424"):
  pdiff fallback; apt fetched the full index; exit 0. Cosmetic. Also cosmetic: "Repository … changed its
  'Version' value from '13.5' to '13.6'".

$ sudo sqlite3 "file:…/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'
10

$ … | grep -ciE "NoClassDefFoundError|jdk.jfr|BusMetrics"
7

$ … | grep -iE "…" | head -5
Aug 23 16:54:09 hs-fresh homesynapse[890]: java.util.concurrent.ExecutionException: java.lang.NoClassDefFoundError: jdk/jfr/Event
Aug 23 16:54:09 hs-fresh homesynapse[890]: Caused by: java.lang.NoClassDefFoundError: jdk/jfr/Event
Aug 23 16:54:09 hs-fresh homesynapse[890]:         at com.homesynapse.event.bus.BusMetricsJfr.recordWriterQueueDepth(BusMetricsJfr.java:59)
Aug 23 16:54:09 hs-fresh homesynapse[890]: Caused by: java.lang.ClassNotFoundException: jdk.jfr.Event
Aug 23 16:54:09 hs-fresh homesynapse[890]: Exception in thread "integration-zigbee-0" java.lang.NoClassDefFoundError: jdk/jfr/Event

$ … > ~/block1-red-journal.txt; wc -l
92 /home/nick/block1-red-journal.txt
```

**STOP-GATE 1: GO.** Both P-1 disjuncts satisfied. `initial_api_token` **present** → F-S9; token file modes
**644** → F-S10; `data/zigbee/` written **this boot** → F-S11.

### §3.3 ⏺ Block 2 — the fixed artifact + GREEN

**Part 1 — the upgrade (same boot):**

```
$ cd ~ && sha256sum homesynapse_7c9e4fa_arm64.deb dist-7c9e4fa.tar.gz
ed82ae8fa989fd7bf01373bba95ff5eb7df2a72fca825bc6bc271d0d666f2324  homesynapse_7c9e4fa_arm64.deb
db57fa90285b0a859eaca76963d225e16ac01af2ff4fc1d914c39579a122204d  dist-7c9e4fa.tar.gz
   → byte-exact on the THIRD hop (bench → desktop → held card)

$ tar xzf … && ls -la distribution/deb/build/ distribution/smoke/ distribution/common.sh
-rwxrwxr-x 1 nick nick     5569 Aug 21 17:57 distribution/common.sh
-rwxrwxr-x 1 nick nick     4524 Aug 21 17:57 distribution/smoke/health-probe.sh
-rwxrwxr-x 1 nick nick    11600 Aug 21 17:57 distribution/smoke/run-smoke.sh
-rw-r--r-- 1 nick nick 61788352 Aug 23 16:56 distribution/deb/build/homesynapse_7c9e4fa_arm64.deb
   → run-smoke.sh at 11,600 B = the byte-size of the copy the v55 layer-2 audit read. The tree is the frozen 7c9e4fa tree.

$ command -v curl || (…)     → curl already present; nothing installed

$ sudo apt install -y ./distribution/deb/build/homesynapse_7c9e4fa_arm64.deb
Summary: Upgrading: 1, Installing: 0, Removing: 0, Not Upgrading: 95
Space needed: 16.4 MB / 116 GB available
Unpacking homesynapse (7c9e4fa) over (0.1.0+gd26777c) ...
Setting up homesynapse (7c9e4fa) ...
HomeSynapse Core is running.
 First-run pairing token: /var/lib/homesynapse/config/initial_api_token     ← PATH only, never the value
Notice: Download is performed unsandboxed as root … (13: Permission denied)  ← the named cosmetic warning, exit 0

$ dpkg -s homesynapse | grep -E "^Version:"     → Version: 7c9e4fa
$ cat /opt/homesynapse/VERSION                  → 7c9e4fa
```

Two audit objects close here:

- **The bare-id dpkg ordering is proven on hardware.** `7c9e4fa` was accepted as an **upgrade** over
  `0.1.0+gd26777c` with no `--allow-downgrades`. The layer-2 correction to `common.sh` :62–:65 (the `[0-9]*`
  arm prints the id bare) is confirmed end-to-end. → **F-S18.**
- **The stale-tree hazard is disproven at the instrument.** `/opt/homesynapse/VERSION` = `7c9e4fa`, so the
  runtime inside the package is the tree `build-image.sh` rebuilt at Block 0, not a repackaged `d26777c`
  image. The audit's root-cause defect (a) closes on hardware.

**The conditional store-reset block was NOT run** — `initial_api_token` was present. D-5 is moot.

**Part 2 — fresh boot and the discriminator:**

```
$ uptime -s                                                   → 2026-08-23 17:06:05
$ systemctl status homesynapse.service --no-pager | head -5
     Active: active (running) since Sun 2026-08-23 17:06:24 EDT; 14s ago    ← 19 s boot → active
$ … | grep -ciE "NoClassDefFoundError|jdk.jfr|BusMetrics"     → 0     ← THE DISCRIMINATOR
$ … | grep -iE "…" | head -5                                  → (empty)
$ sudo sqlite3 "file:…?mode=ro" 'SELECT COUNT(*) FROM events;' → 14    ← > Block 1's 10 (Δ +4 this boot)
```

**STOP-GATE 2: GO.** The R-1/R-2 hardware pair, one card, one byte-identical instrument:

| | RED — `0.1.0+gd26777c` | GREEN — `7c9e4fa` |
|---|---|---|
| throw-signature lines | **7** | **0** |
| event rows | 10 | **14** |
| boot | 16:54:10 EDT | 17:06:24 EDT |

**run-smoke — 18/18 PASS · `INSTALL-SMOKE PASSED ✓`:**

```
[smoke] mode=systemd
[smoke] deb=/home/nick/distribution/deb/build/homesynapse_7c9e4fa_arm64.deb
[smoke] PASS  package installed
[smoke] PASS  unit is active
[smoke] PASS  unit is enabled (starts on boot)
[health-probe] waiting up to 90s for readiness at http://127.0.0.1:7070/api/v1/entities
[health-probe] ready (200) at http://127.0.0.1:7070/api/v1/entities
[smoke] PASS  loopback health probe green (HTTP 200 RUNNING)
[smoke] PASS  event write path persisted 14 event row(s) this boot (/var/lib/homesynapse/data/homesynapse-events.db)
[smoke] PASS  zero uncaught-throw signatures across 1 log source(s) (grep -icE 'NoClassDefFoundError|jdk.jfr|BusMetrics' = 0)
[smoke] PASS  first-run pairing token minted at /var/lib/homesynapse/config/initial_api_token
[smoke] PASS  token owned by homesynapse
[smoke] PASS  config dir mode 700 (no world access)
[smoke] PASS  unauthenticated request rejected (401) — auth enforced
[smoke] PASS  headerless GET / redirects to the dashboard (302)
[smoke] PASS  headerless GET /dashboard/ serves the shell (200)
[smoke] PASS  service stopped
[smoke] PASS  service inactive after stop
[smoke] PASS  package removed
[smoke] PASS  unit file gone
[smoke] PASS  image dir gone
[smoke] PASS  data dir preserved on remove (event store safe)
────────────────────────────────────────────────────────
[smoke] INSTALL-SMOKE PASSED ✓  (gate #4: install path proven)
```

Eighteen `[smoke] PASS ` lines, nine checks, the census matching the packet's predicted set. **Check 4's two
positive lines are the sitting's centre of gravity:** `persisted 14 event row(s) this boot` — equal to the
independent `sqlite3` read taken minutes earlier — and `zero uncaught-throw signatures … = 0`. **This is the
first green of the packaged write-path assert on real hardware**; CI had proven it only on a clean runner.

The probe path (`/api/v1/entities`, not `/health`) is an independent witness of artifact vintage → **F-S14.**

**R-3 rig restored on the card:**

```
$ id homesynapse                            → uid=102(homesynapse) gid=105(homesynapse) groups=105(homesynapse)
$ systemctl is-enabled homesynapse.service  → not-found          ← NOT masked; no unmask needed
$ ls -la /var/lib/homesynapse/config/       → Permission denied  ← F-S13, PACKET DEFECT

$ sudo apt install -y ./distribution/deb/build/homesynapse_7c9e4fa_arm64.deb
Summary: Upgrading: 0, Installing: 1, Removing: 0, Not Upgrading: 95
Space needed: 91.7 MB / 116 GB available
Selecting previously unselected package homesynapse.
Unpacking homesynapse (7c9e4fa) ...   Setting up homesynapse (7c9e4fa) ...
HomeSynapse Core is running.
$ dpkg -s homesynapse | grep -E "^(Status|Version):"
Status: install ok installed
Version: 7c9e4fa

$ sudo ls -la /var/lib/homesynapse/config/        ← re-taken with sudo after F-S13
drwx------ 3 homesynapse homesynapse 4096 Aug 13 07:35 .
-rw-r--r-- 1 homesynapse homesynapse  132 Aug 13 07:35 api_tokens
-rw-r--r-- 1 homesynapse homesynapse   26 Aug 13 07:35 home_id
-rw-r--r-- 1 homesynapse homesynapse   44 Aug 13 07:35 initial_api_token
drwxr-xr-x 2 homesynapse homesynapse 4096 Aug 13 07:35 schemas
```

**The remove → install path CI never exercises worked clean.** The config listing is **byte-identical to Block
1's** — same sizes, same mtimes, same modes. Three consequences: the remove preserved the data dir; the
re-install minted no new token (mtimes unmoved); **the sitting left this card's token state completely
unchanged.**

**The L3 mask:**

```
before → block1-red-journal.txt:0 · block2-run-smoke.txt:0
after  → block1-red-journal.txt:0 · block2-run-smoke.txt:0
```

Zero on both files both times. Nothing failed, so no `dump_logs` diagnostics ran, and the mint predates this
boot. **No token value ever entered the evidence set** — L3 is satisfied by construction, not only by masking.

**Evidence home:** `block1-red-journal.txt` 15,223 B · `block2-run-smoke.txt` 1,507 B.

### §3.4 ⏺ Block 3 — restore

**Physical restore, in the H3 order:** held card down → LED settled → power off → **held card OUT and labeled
`hs-fresh — R-3/R-4 rig — 7c9e4fa`** → **coordinator re-plugged into Rosonway physical port 5** (only after the
held card was out) → bench card IN → power on.

**`~/bench.sh status` — before the start:**

```
  [!!] NOT running
--- health tokens (current boot: /home/homesynapse/hs-bench/bench-2026-08-23-131519.log)   ← the SUPERSEDED log
… (the 13:15 tokens, unchanged) …
--- failure tokens ---
16:50:43.220 [integration-zigbee-0] WARN  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.transport_failed:
  serial read error: port dead or closed; lastFrame=DATA(frm=2, ack=6, reTx=false)
  retransmits=0 crcRejects=0 timeouts=0 — the watchdog owns recovery
```

→ **F-S15** (the app was not running: D-4 proven necessary) and **F-S16** (the WARN is caused and expected-class).

**`~/bench.sh start` (D-4):**

```
  [OK] launched pid 2117 -> /home/homesynapse/hs-bench/bench-2026-08-23-171853.log
  [OK] RADIO UP after 18s
17:19:01.767  registry.projection_live: devices=6 entities=6 position=25065
17:19:02.366–17:19:02.368  zigbee.device_relinked ×6  (all six device ids, re-pairing, no new adoption)
17:19:02.368  zigbee.adoption_maps_rehydrated: devices=6
17:19:10.262  zigbee.network_resumed: channel=20 panId=0x774c
17:19:10.262  zigbee.network_up: stackStatusHandler reported EMBER_NETWORK_UP (buffered)
--- failure tokens ---   (EMPTY)
```

**`position=25065` is identical to the pre-swap read** — the bench event log did not advance across the
~90-minute swap, confirming the bench was genuinely quiescent throughout.

**⏺ `~/bench.sh scenario boot-health` — `runner B3.1-2026-08-02-postwindow @ 16e672d`:**

```
  [--] stimulus bench: restart
  [OK] stopped
  [OK] launched pid 2336 -> /home/homesynapse/hs-bench/bench-2026-08-23-172656.log
  [--] waiting for a decisive radio state (up to 90 s)...
  [OK] RADIO UP after 13s
17:27:00.429  registry.projection_live: devices=6 entities=6 position=25065
17:27:00.844–17:27:00.846  zigbee.device_relinked ×6
17:27:00.847  zigbee.adoption_maps_rehydrated: devices=6
17:27:08.720  zigbee.network_resumed: channel=20 panId=0x774c
17:27:08.721  zigbee.network_up: stackStatusHandler reported EMBER_NETWORK_UP (buffered)
--- failure tokens ---
    [ok] log 'registry.projection_live: devices=6 entities=6' min=25065 — position=25065 (within 90s)
    [ok] log 'zigbee.adoption_maps_rehydrated: devices=6' (within 90s)
    [ok] log 'zigbee.device_relinked' x2(at-least) (within 90s)
    [ok] log 'zigbee.network_resumed: channel=20 panId=0x774c' (within 90s)
    [ok] log 'zigbee.port_identity_captured:' same-line ['pinnedOnly=false'] — 17:27:08.605
         stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0
         vendorId=10c4 productId=ea60 pinnedOnly=false (within 90s)
    [ok] api /api/v1/entities {"rows": 6, "ulids": ["01KX1PA4HSJ581GASYB7DHE40F","01KX1PB9AAB4VB3E10BD477TV3",
         "01KXW0157SP56CCSGJCNDCSQNG","01KXW13WF0D6TYGN13WXHTG87K","01KXW1W1SBJZERC9MBAMV2DWKE",
         "01KY12MQW954E4XYNKH0Y5H8VX"]} — all asserts satisfied (within 90s)
[PASS] boot-health — 6/6 positive · 0 forbidden
  [--] bundle: /home/homesynapse/hs-bench/bundles/boot-health-20260823T212709Z
```

**P-3's boot-health limb is met verbatim.** Two things this run establishes beyond the pass itself:

- **`RADIO UP after 13s`** — back on the 12–13 s precedent (Rosonway ×3 at 12 s; §OP-H today at 13 s). The
  18 s at the cold start was the first enumeration after a physical re-plug, not a shifted baseline.
  → **F-S17 opens and closes inside this sitting.**
- **`zigbee.port_identity_captured … stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0`** is **byte-identical to the string in the 2026-07-25
  Rosonway report**, pre- and post-move. The coordinator is not merely working; it is the same identity on the
  same path. → **F-S20.**

**⏺ `ls -la /home/homesynapse/hs-bench/config/` — the rotation CONFIRM (read-only; no act taken):**

```
drwxrwxr-x 4 homesynapse homesynapse  4096 Aug 23 13:12 .
-rw------- 1 homesynapse homesynapse   300 Aug 23 13:12 api_tokens
-rw-rw-r-- 1 homesynapse homesynapse   132 Jul  6 08:41 api_tokens.rotated-2026-08-20
-rw-rw-r-- 1 homesynapse homesynapse    26 Jul  6 08:41 home_id
-rw-rw-r-- 1 homesynapse homesynapse  1208 Jul  9 22:26 homesynapse.yaml
-rw------- 1 homesynapse homesynapse    44 Aug 23 13:12 initial_api_token
drwxrwxr-x 2 homesynapse homesynapse  4096 Jul 21 07:33 integrations
drwxrwxr-x 2 homesynapse homesynapse  4096 Jul  6 08:41 schemas
```

**This differs from P-3's literal, and the prediction is what is stale — not the rig.** P-3 was authored
2026-08-21 and describes the 08-20 22:06 rotation state (`api_tokens` 132 B @ Aug 20 22:06, `initial_api_token`
44 B @ Aug 20 22:06). **Today's §OP-A superseded it hours before this sitting**, and the observed listing is
the §OP-A post-state exactly as the hub itself recorded it: *"`api_tokens` (300 B) + `initial_api_token`
(44 B) both `-rw------- homesynapse` with fresh mtimes."* Observed: **300 B / 44 B, both `-rw-------`, both
stamped Aug 23 13:12 (Pi/ET)**. `api_tokens.rotated-2026-08-20` sits beside them at 132 B / Jul 6 08:41 — the
original store, moved aside, untouched. → **F-S19**, and the TZ-label question it raises → **F-S21.**

**The rotation state is CONFIRMED. No second rotation was performed. The 08-20 exposed token remains dead.**

**⏺ Restore verification, like-for-like against PF-1:**

```
$ ~/bench.sh entities
{"data":[{"entityId":"01KX1PA4HSJ581GASYB7DHE40F","availability":"UNAVAILABLE","stale":false},
         {"entityId":"01KX1PB9AAB4VB3E10BD477TV3","availability":"AVAILABLE","stale":false},
         {"entityId":"01KXW0157SP56CCSGJCNDCSQNG","availability":"AVAILABLE","stale":false},
         {"entityId":"01KXW13WF0D6TYGN13WXHTG87K","availability":"AVAILABLE","stale":false},
         {"entityId":"01KXW1W1SBJZERC9MBAMV2DWKE","availability":"AVAILABLE","stale":false},
         {"entityId":"01KY12MQW954E4XYNKH0Y5H8VX","availability":"AVAILABLE","stale":false}],
 "meta":{"viewPosition":112578,"timestamp":"2026-08-23T21:27:19.686138143Z"}}

$ lsusb | grep -i 10c4   → Bus 003 Device 004: ID 10c4:ea60 Silicon Labs CP210x UART Bridge
$ ls -l /dev/zigbee      → lrwxrwxrwx 1 root root 7 Aug 23 17:18 /dev/zigbee -> ttyUSB0
$ uhubctl
Current status for hub 3-2.4 [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
  Port 1: 0100 power
  Port 2: 0103 power enable connect [10c4:ea60 SONOFF SONOFF Dongle Plus MG24 0ae2dd7cecf8ef11b80168135c2a50c9]
  Port 3: 0100 power
  Port 4: 0100 power
```

**Six entities: 5 AVAILABLE + 1 UNAVAILABLE** — exactly the H3 restore criterion (the UNAVAILABLE one,
`01KX1PA4HSJ581GASYB7DHE40F`, is the dead-and-kept Hue; *fewer than 5 AVAILABLE would mean the coordinator did
not return*). `viewPosition` 112516 → 112578 across the sitting.
**Hub `3-2.4` Port 2 is byte-identical to the PF-1 read and to the 2026-07-28 B2 record.** The USB device
number moved 022 → 004 (re-enumeration, expected) and the `/dev/zigbee` symlink is re-stamped 17:18 by the
udev rule firing on the re-plug. **The `usb-power` scenario's path addressing (`uhubctl -l 3-2.4 -p 2`) is
intact.**

**BLOCK 3 CLOSED. THE SITTING IS CLOSED.**

---

## §4 Findings

**Ranked by what they change:**
**F-S9** (changes an R-3 premise) · **F-S15** (changes every card-swap restore block) · **F-S10** (adds an R-6
row CI cannot see) · **F-S19 / F-S21** (a stale prediction and the TZ-label question under it) · **F-S7**
(closes a wait-state) · **F-S11** (ratifies a fence) · **F-S13** (packet craft) · then the notes.

| id | class | statement and disposition |
|---|---|---|
| **F-S9** | **CORRECTION — R-3 premise** | **`initial_api_token` is PRESENT on the held card** (44 B, Aug 13 07:35), and remained so through the whole sitting. E-P1 refuted. The R-3 residue is written as *"the PACKAGED unit restarts to `active` with `initial_api_token` **absent**, on the held card"* — **that condition does not pre-exist.** R-3's E3-GREEN block must create it itself (an `mv` aside, delete-nothing) rather than inherit it. The packet's conditional store-reset correctly did not fire; D-5 is moot. |
| **F-S15** | **PACKET GAP — proven, not theoretical** | After the restore boot, `~/bench.sh status` returned **`[!!] NOT running`.** The packet's §4 goes straight to `~/bench.sh scenario boot-health`; run as written it would have driven the scenario against a dead app and produced a red with no bearing on anything. The bench app has no systemd unit — it is a `nohup` child of the oneshot nightly — so nothing would have started it before 04:30. **`~/bench.sh start` must be written into every card-swap restore block.** (Known since the H3 context pack trap 4; never propagated into a packet. Now observed.) |
| **F-S10** | **PACKAGING — for the R-6 batch; both halves observed in one sitting** | **The first-run mint and the rotate path disagree on token file mode.** Held card, after the packaged first-run mint: `api_tokens` and `initial_api_token` are **`-rw-r--r--` (644)**. Bench, after the R-6/R-8 `rotate` path: both **`-rw-------` (600)** — observed directly at §3.4, hours after the held-card read. Same two filenames, two write paths, two modes. **run-smoke structurally cannot catch it** — check 7 asserts the *directory* is 700 (it is) and check 6 asserts ownership (correct), so CI stays green over a 644 token file. Only the 700 directory prevents exposure today. |
| **F-S19** | **STALE PREDICTION — no act taken** | **P-3's config-listing expectation was superseded before the sitting began.** It was authored 2026-08-21 against the 08-20 22:06 rotation; today's §OP-A rewrote the store. The observed listing (300 B / 44 B, both 600, Aug 23 13:12 ET, with `api_tokens.rotated-2026-08-20` 132 B / Jul 6 beside them) **matches the hub's own §OP-A record exactly**. The packet's instruction on a mismatch — "⏺ and paste (no act)" — was followed to the letter. Two dispositions: (a) refresh P-3 in any successor packet; (b) note that P-3's phrasing "expect the three lines" reads as a claim about the whole directory, which has **seven** entries — it should say "these three among the listing", or a future operator will report a false mismatch. |
| **F-S21** | **TZ-LABEL AMBIGUITY — in the hub's own record** | The §OP-A/§OP-H sitting is recorded as *"(Nick, 13:11–13:16 CT…)"*. The artifacts it produced are stamped **Aug 23 13:12 on a Pi whose clock is EDT** (`timedatectl`: `Local time: Sun 2026-08-23 16:08:00 EDT`), and the corroborating bench boot log is `bench-2026-08-23-131519.log` (13:15:19 ET). **13:11–13:16 matches the ET clock, not CT.** Either the record's "CT" should read "ET", or the store was written an hour before the recorded window. **This is precisely the class R-B's TZ-HOLD ruling and the Z-stamp convention exist to prevent**, and it is now sitting inside a record that other work cites. Recommend the hub reconcile the label at source. |
| **F-S7** | **WAIT-STATE CLOSED** | **The Block-0 proximity confounder is discharged at the instrument.** The hub named Aug-22's nightly as confounded (Block 0 ended ~11 min before the ~03:32 CT fire; ≈100 MB of SD writes, page-cache churn) and ruled it not adjudicable without that caveat. **There was no flake.** Confounded and clean nights are identical in shape — `8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓` both — with ON-latency `0.29s` → `0.28s`, a 10 ms delta inside noise. The confounder cost nothing measurable. Closes on a negative result. |
| **F-S11** | **RATIFIES THE SD-5 FENCE** | The held card's zigbee integration is **live**: `/var/lib/homesynapse/data/zigbee/` was written at this boot (16:54) and `integration-zigbee-0` appears in the throw set. That is the independent custody store the R-3 `resumeOrForm()` finding concerns — it forms a new network whenever the parameter store is empty. **With the coordinator attached it would have had a radio to form on.** The fence (unplugged for the whole held-card leg) was load-bearing, not ceremonial. **Recommend it be written explicitly into the R-3 and R-4 packets**, which currently inherit it only by convention. |
| **F-S13** | **PACKET DEFECT** | Packet §3's rig-glance reads `ls -la /var/lib/homesynapse/config/` **without `sudo`**, while Block 1's equivalent line has it. The dir is `drwx------ homesynapse`, so **the line cannot succeed as written for user `nick`** — it returned `Permission denied`. This is the class the Rosonway report names: *a glance-point asserting something the instrument cannot deliver.* Re-taken with `sudo` in-session; the expectation was then met in full. |
| **F-S18** | **F-V1 premise exercised live** | `7c9e4fa` was accepted by `apt` as an **upgrade** over `0.1.0+gd26777c` with no `--allow-downgrades`, on hardware. Confirms the layer-2 correction to `common.sh` :62–:65 end-to-end and prices F-V1: the fix is needed for *future* a–f-leading ids, not for this pair. |
| **F-S20** | **RESTORE PROVEN AT IDENTITY, not just at function** | `zigbee.port_identity_captured: stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false` is **byte-identical to the string recorded pre- and post-move in the 2026-07-25 Rosonway report**, and `uhubctl` shows the dongle back on hub `3-2.4` **Port 2**. The unplug/re-plug cycle left the by-id name, the udev symlink and the path addressing all intact — so the `usb-power` scenario (`uhubctl -l 3-2.4 -p 2`) is unaffected. This is the check that would have caught a wrong-port re-plug, and it is clean. |
| **F-S17** | NOTE — **opened and closed in-sitting** | `~/bench.sh start` after the re-plug reported **RADIO UP after 18 s**, against a 12 s precedent measured three times in the Rosonway report and 13 s at today's §OP-H. The very next start — `boot-health`'s own restart, eight minutes later — reported **13 s**. The 18 s was the first enumeration after a physical re-plug with the dongle unpowered ~90 min, **not a shifted baseline.** No action needed; recorded so the pattern is recognised next time a card is swapped. |
| **F-S16** | NOTE — caused, expected-class | The single failure token in the **superseded** boot log — `zigbee.transport_failed: serial read error: port dead or closed … retransmits=0 crcRejects=0 timeouts=0` at **16:50:43 EDT** — coincides with the coordinator unplug / bench shutdown. Zero retransmits, zero CRC rejects, zero timeouts is the signature of an instantaneous physical port loss, not degradation, and `the watchdog owns recovery` is the designed handling. **The new boot's failure tokens are empty.** Recorded so this is never later read as a spontaneous transport flake. |
| **F-S14** | NOTE — positive | The held card's health probe reports readiness at `…:7070/api/v1/entities`, not `/health` — correct, since `/health` arrives with R-9, which postdates `7c9e4fa`. An independent witness that the card ran the intended vintage. |
| **F-S8** | NOTE — read surface, R-10 docket | One `/state` response renders instants **two ways**: `data.*` as epoch-second numbers, `meta.timestamp` as an ISO-8601 string. Separately, `entityId` returns as a 128-bit `{msb,lsb}` pair though the request addressed it by ULID — a caller cannot round-trip the identifier from the body. Neither is a defect against a stated contract; filed as consumer-facing asymmetries. |
| **F-S6** | NOTE — record hygiene | The `7c9e4fa` pair was staged **Sat 2026-08-22 ~03:20 CT**, not Thursday. Desktop mtimes `Aug 22 03:22` CDT; bench mtimes `Aug 22 04:19–04:20` EDT — both inside the recorded Block-0 window. The queue and the pm-handoff standing-ask both say "Thursday". Provenance is closed at the bytes on both hops; suggest correcting the prose. |
| **F-S12** | NOTE — rig hygiene | The held card is **95 packages behind** on OS updates (Aug 13 image state). Untouched today, correctly. Flagged only so R-3/R-4 decide **deliberately** whether the rig is patched before those runs rather than drifting into it. |

---

## §5 Deviations and disclosed acts

| id | status | detail |
|---|---|---|
| D-1 | **WITHDRAWN — never executed** | Pi-side `script(1)` console capture. Proposed after Git Bash was found to lack `script`; withdrawn mid-sitting to reduce operator load. **No console logs exist.** The two packet-created evidence files are the verbatim record; every short line in §3 is transcribed from the operator's terminal output. |
| D-2 | **WITHDRAWN — never executed** | The read-only rig pre-probe (`date`/`uptime`/`ip`/`df`/`free`/`vcgencmd get_throttled`) on the held card. Consequence: **E-P4 is inferred rather than measured on that card, and E-P5 is untested** — no under-voltage or thermal reading exists for this sitting. |
| **D-3** | **EXECUTED** | **Zigbee coordinator physically unplugged** from Rosonway physical port 5 for the entire held-card leg; re-plugged **into the same port** only after the held card was physically out. Not in the packet; carried from the SD-5 rail and the H3 restore order. Justified after the fact by **F-S11**; restore proven at identity by **F-S20**. |
| **D-4** | **EXECUTED** | **`~/bench.sh start`** after the restore boot. Not in the packet. Justified after the fact by **F-S15** — the app was measurably not running. |
| D-5 | **MOOT** | The conditional store-reset would have been named `api_tokens.rotated-2026-08-23` rather than the packet's `-2026-08-22`. The conditional never fired (F-S9). |
| — | **ADDED, read-only** | `sudo ls -la /var/lib/homesynapse/config/` re-taken after F-S13, to recover the glance the packet's line could not deliver. |
| — | **ADDED, read-only** | The PF-1 pre-swap block (bench clock, LAN, USB topology, recovery-source listing) and the §3.4 restore-verification set (`entities`, `lsusb`, `/dev/zigbee`, `uhubctl`). All reads. They produced F-S6, F-S16, F-S20 and the like-for-like restore proof. |
| — | **SLIP, zero effect** | The PF-1 command block was first pasted into the Git Bash window rather than the `ssh pi` session. Every line failed `command not found` / `No such file or directory`; nothing executed, nothing written, nothing on any card touched. Same class as the v55 b4 disclosed slip. The block was then run correctly on the bench. |

**Anti-actions held throughout:** nothing was `rm`'d · no failing step was retuned on a card · no token value or
`Authorization` header was pasted · no block ran inside 03:00–04:15 CT · the coordinator was never attached
while the held card ran · no second token rotation was performed · `homesynapse-core` on the Windows host was
not touched while R-7b is live.

---

## §6 What this closes, and what it hands forward

**Closed by this sitting**

1. **R-1/R-2's hardware half.** RED → GREEN on one card, one instrument, plus 18/18 run-smoke on hardware.
2. **Block 3's restore floor.** `[PASS] boot-health — 6/6 positive · 0 forbidden`, fleet 5 + 1, coordinator
   proven back at identity and at port.
3. **The token-rotation wait-state.** Confirmed at the listing; no second rotation; the 08-20 exposed token
   stays dead.
4. **The Aug-22 nightly confounder** (F-S7) — a named wait-state, discharged on a negative result.
5. **The nightly digest wait-state** — both lines banked (owed since v56 beat 1).
6. **P-1, the 02P channel census** — banked, both limbs confirmed, coherent at the wall clock.
7. **The layer-2 audit's stale-tree defect (a)** — disproven at the instrument on hardware.
8. **The bare-id dpkg ordering question** (F-S18) — proven live.
9. **The remove → install path CI never exercises** — exercised, clean.

**Handed forward**

- **F-S9 changes an R-3 premise.** The E3-GREEN block must create the `initial_api_token`-absent condition.
- **F-S15 changes every future card-swap restore block.** `~/bench.sh start` is mandatory, not optional.
- **F-S11 recommends the SD-5 coordinator fence be written explicitly into the R-3/R-4 packets.**
- **F-S10 adds a row to the R-6 packaging batch**, with the note that CI cannot detect it.
- **F-S19 refreshes P-3** and fixes a prediction phrasing that invites a false mismatch.
- **F-S21 asks the hub to reconcile a TZ label** in the §OP-A record other work cites.
- **F-S13** is packet craft — a glance-point that cannot succeed as written.
- **E-P3 and E-P5 are untested** and remain open questions, not silent passes.

**Rig state left behind**

- **Held card** (`hs-fresh`, labeled `R-3/R-4 rig — 7c9e4fa`): package `7c9e4fa` installed and running; event
  store at **14 rows**; `config/` byte-identical to how the sitting found it; `initial_api_token` present;
  95 OS packages pending; the `distribution/` tree and the `.deb` left in `/home/nick`; **out of the Pi,
  labeled, kept.**
- **Bench card** (`hs-dev-1`): in the Pi, app running as **pid 2336**, log `bench-2026-08-23-172656.log`,
  coordinator on Rosonway port 5 / hub `3-2.4` Port 2, fleet 6 devices / 6 entities / 5 AVAILABLE + 1
  UNAVAILABLE, `position=25065` unadvanced across the swap, rotation state confirmed unchanged.

---

## §7 Recommended hub acts, ranked

1. **Fold F-S9 into the R-3 skeleton before it is finalized** — the E3-GREEN block's precondition does not exist and must be created.
2. **Write `~/bench.sh start` and the SD-5 coordinator fence into the R-3/R-4 packets** (F-S15, F-S11). Both were needed today and neither was written down.
3. **Add F-S10 to the R-6 packaging batch** — the mint/rotate mode disagreement, with the note that no CI check can see it.
4. **Reconcile the §OP-A timezone label at source** (F-S21) before more work cites that window.
5. **Refresh P-3's config expectation and its "three lines" phrasing** in any successor packet (F-S19).
6. **Retire the Aug-22 nightly confounder** from the open-risks set (F-S7).
7. **Correct the "Thursday" provenance line** in the queue and the pm-handoff standing-ask (F-S6).
8. **Fix the packet's un-`sudo`'d glance line** in the next revision (F-S13).
9. Route **F-S8** to the R-10 / frozen-v1.1 docket, and **F-S12** to the R-3/R-4 rig-prep decision.

---

## §8 The evidence set

| artefact | bytes / id | where |
|---|---|---|
| `block1-red-journal.txt` | 15,223 | desktop `~/Desktop/card-sitting-2026-08-22/` and `_scratch/card-sitting-2026-08-23/` |
| `block2-run-smoke.txt` | 1,507 | same two locations |
| `homesynapse_7c9e4fa_arm64.deb` | 61,788,352 | desktop staging · bench home · held card `~/distribution/deb/build/` |
| `dist-7c9e4fa.tar.gz` | 33,982 | desktop staging · bench home · held card `~` |
| boot-health bundle | `boot-health-20260823T212709Z` | bench `/home/homesynapse/hs-bench/bundles/` |
| bench app logs | `bench-2026-08-23-171853.log` (start) · `bench-2026-08-23-172656.log` (scenario) | bench `/home/homesynapse/hs-bench/` |

Both evidence files were masked on the card before leaving it (`Token: ` count 0 before and after, on both).
No console transcript exists — D-1 was withdrawn; §3 is transcribed from the operator's terminal output.
