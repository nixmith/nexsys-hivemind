<!--
file: context/audits/2026-10-17_v112-b3_BC10_intake_two-layer_audit.md
purpose: v112 beat 3 — BENCH-CORE-10's intake, two layers: §P 0–10 adjudicated in order against the outputs file at the bytes (the guide's own record beside it), the hub's re-execution (both kept boot logs re-read by BP11's `boot_timing.py` on the desk copies; the five md5s; the boot-health stimulus at the source; DV-8 resolved from the cold log; IR-166's shape counted), the results the record banks (IR-148's "after"; the pre-warm question answered), and DV-1 — the hub's own miss.
audience: the hub · Nick · the bench lane (IR-220)
state-type: audit (a rig card's intake)
status: FILED — v112 beat 3 (Sat 2026-10-17 ~10:4x CT; instrument 2026-10-17T15:44:06Z)
-->

# BC10 — the intake (v112 b3)

## §0 Verdict
**INTAKEN ACCEPT — every §P PASS; `176adad` is up on hs-dev-1 by sha; the fix holds on the real store.** Nick ran the card Sat 2026-10-17 09:35–10:23 CT (the guide's return: every block once, in order, no STOP). The outputs file `_scratch/v111/bc10/2026-10-17_BENCH-CORE-10_outputs.txt` 5,387 B md5 `b49c72192171c505061e7a3181463efa` (verbatim in §5); the kept logs — the cold boot `bench-2026-10-17-111535.log` 16,161 B md5 `2d2242241273161f93da651700efb3fc` (Nick's extra copy) and the running boot `bench-2026-10-17-111625.log` 14,303 B md5 `3a70467da3892c47648e9d8cdec9c501`; the guide's return `…_guide-return.md` 12,087 B md5 `dbac263d64cd796ea55bac3279fa045f`; HERO-U3-W's capture `wire-2026-10-17-entities_raw.json` 5,639 B md5 `559ac60dc338068ad00313d57288115f`. **ONE material deviation, the hub's (DV-1):** C3's `bench.sh scenario boot-health` restarted the Core 43 s after the cold start — the scenario's stimulus is `bench: restart` — so boot-health's 7/7 is the warm boot's, and the card's "ONE cold start" held only until the scenario ran (IR-220).

## §1 Layer 1 — §P 0–10, in order
- **P0 THE PREMISE ✓** (A, 15:05:36Z): hs-dev-1 · NTP yes · core `37f05a9` porcelain 0 · bench `cddac94` porcelain 0 · the nightly's boot `bench-2026-10-17-043253.log` formed=0 relinked=10 startup_failed=0 · store 1,163,522,048 B, 2,317,635 events · free 100.1 GB · the unit not installed.
- **P1 BACKUP-1 ✓** (C1/C1b): the one-step API, 36 s, 1,163,702,272 B, integrity ok, 2,317,979 rows; md5 `90724ec4e9092ad2d900772a127ee274` on the Pi AND on the desk after an 18-s scp; STAMP `20261017T151006Z`. The restore point of record for every act until the next backup.
- **P2 THE BENCH ✓** (BP): `cddac94` → `7e03c81` fast-forward; 48 · 66 · 44 · 54 · 10 checks, 0 failures — the desk VM's counts exactly; `constants.yaml` `9b0af47b3376`; the pre-warm verb and `boot_timing.py` present.
- **P3 IR-148's "after" ✓ — decisively** (C3, the cold boot 111535): the page cache dropped 2,077,440 → 354,640 kB; `boot: launched=11:15:37.534 Loaded=+1.415 projection_live=+1.999 network_resumed=+13.867 network_up=+13.868 startup_failed=none` (Pi EDT; = 10:15:37 CT) → **`projection_live − Loaded` = 0.584 s against the bar of 20.4 s**; `registry.projection_rebuilt: rows=20 head=2318340 skipped=0 ms=512` (DV-2: hundreds of ms, not the tens the EXPECTED guessed; the bar is P3's). Dry-run #1's "before" on `37f05a9`, five days and ≈ 440 k events earlier: cold exit 99 at +49.6 s.
- **P4 ✓** issues=0 on the cold boot; boot-health `[PASS] 7/7 · 0 forbidden` — on the scenario's own warm restart (DV-1; DV-3: BP11's scenario has seven positives, the card said six).
- **P5 RECORDED:** 0 `zigbee.reporting_configured`/`reporting_cluster` lines in either boot (DV-4 — the posture lines are not printed on a resumed boot; IR-113/123's reading is "none at boot"); IR-166 13 lines on the cold boot.
- **P6 ✓** AVAIL-API-1: the entities rows carry the v1.1.7 keys (the first row is the Hue — UNAVAILABLE, `mains-floor`, `silenceLimitSeconds` 60, `missesToDark` 2, `recordIntervalSeconds` 3600); `probe_answered` = 2 store rows (B3's first).
- **P7 RECORDED:** F-6 0 lines · 0/0/0 (no automation has run on `176adad` yet; DV-7: the guide checked the SQL against the codec); F-7 0 keys (no `IllegalStateException` at the cold instance's close either — an orderly SIGTERM at 11:16:20.547).
- **P8 ✓** `key_establishment_failed` = 0.
- **P9 ✓** HERO-U3-W: 10 rows, 1 UNAVAILABLE, `meta` = viewPosition · timestamp · recoveryViewPosition — HERO-U4's input; STARTER-1 NOT-RUN.
- **P10 ✓** the CLOSE: `deployed=176adad bench=7e03c81`, the running boot 111625, pings 5, dark 0, store 1,164,107,776 B / 2,318,835 events, the backup in place. The prior-ledger gate's greps were run at the re-stamp — and missed DV-1's cause (§3).

## §2 Layer 2 — the hub's own re-execution (Sat 15:3xZ)
- Both kept logs re-read by `boot_timing.py` (BP11, `git archive 7e03c81`) on the desk copies: the cold line equals C3's byte for byte; the warm boot `launched=11:16:26.451 Loaded=+1.107 projection_live=+1.238 network_resumed=+9.730 startup_failed=none` (`projection_live − Loaded` 0.131 s; rebuilt `ms=103`). **Cold vs warm, one binary, one store, one minute apart: 0.584 vs 0.131 s · 512 vs 103 ms · network up +13.868 vs +9.730 s** — SCHEMA-1's snapshot instrument (IR-193) has its first post-fix pair at 2.32 M events.
- The five md5s re-taken on the desk (§0); the capture's equals Part E's line; the backup's two sides equal.
- DV-1's cause at the source: `scenarios/boot-health.yaml:48–49` at `7e03c81` — `stimulus: - bench: restart`. The cold log ends in an orderly SIGTERM (`HomeSynapseCore stopped … (SIGTERM)`, 11:16:20.547); the warm boot loaded the state checkpoint and replayed 3 events (the guide's read).
- DV-8 resolved: the cold log holds one `zigbee.probe_answered` (11:16:00.305, `0x00124B002FA8D1C5`, answered=1 missed=0) and the warm log one (11:17:00) — the store's two rows are one per instance.
- IR-166's shape counted on the cold log: 13 lines = 7 devices × 1 + 3 metered devices × 2 (`mains-floor` + `mains-metered`) — the EXPECTED form exactly.
- The capture parsed: 10 rows of 19 keys (8 base + the 11 recovery keys); classes passive 5 · mains-floor 2 · mains-metered 3; the one UNAVAILABLE row is the Hue (seeded dark: reason and last-seen null) — IR-162's reading at this boot.
- **Not re-executed:** the live API after 15:21Z; the backup's restore (a read of the copy, not a drill — RESTORE-1's); the gradle build (43 s — DV-6: the clone's cache held); CI on `176adad` (Nick's banked line).

## §3 What the record banks, and the hub's miss
- **IR-148 CLOSED on the rig:** the post-fix cold boot needs 0.584 s from `Loaded` to a live registry on the real store; **IR-189's question is answered — no pre-warm after the fix** (D-v110-20's "measure whether a cold boot still needs it"); `37f05a9`'s ≈ Oct 22 overrun is moot (the Pi no longer runs it). IR-179 CLOSED on the Pi (Part B put `ceb08c5` under the Pi's bench).
- **SOAK-NIGHT-3's BOOT0 is `bench-2026-10-17-111625.log`** (the running boot, 10:16:26 CT); its first restart is the nightly ≈ 03:30 CT; its mornings read the digest and `~/hs-bench/state/wear.tsv` (IR-213, IR-216).
- **DV-1 is the hub's miss, twice over.** The scenario's restart sits in five ledgers since 2026-07-26 (the guide cites `audits/2026-07-26_deploy-evening_return.md:180` and four more); the re-stamp's prior-ledger gate grepped five strings and not the verbs' side effects; and the dry-run's stub `scenario` printed PASS without restarting — the stub was less than the verb it stood for. The evidence survived because C3 read the cold boot before the scenario ran. → IR-220; pm-lessons 2026-10-17. Sunday's card is the first to carry it.
- DV-5 (the `tail` cuts: Part A's `status | tail -1` shows the failure-tokens header) joins IR-220's stub-fidelity half: the stub's `status` printed a running line the real verb prints above its last line.

## §4 Next
HERO-U4 (DISPATCH-READY on this capture) · Sunday's card: the rollback rehearsal (`e11ae20`; the margin) + BC9b, boot-health's restart named · SOAK-NIGHT-3's morning read.

## §5 The outputs file, verbatim (5,387 B, md5 `b49c72192171c505061e7a3181463efa`)
```
=== A 2026-10-17T15:05:36Z
hs-dev-1
pi-clock 15:05:36Z
NTPSynchronized=yes
core-clone: 37f05a9 feat(integration-zigbee,lifecycl ref=HEAD porcelain=0
bench-clone: cddac94 feat(runner,verify72h): AVAIL-LI porcelain=0
--- failure tokens ---
boot-log: bench-2026-10-17-043253.log bytes=179032 formed=0 relinked=10 startup_failed=0
store: 1163522048 B rows=2317635 max=2317635 free=100113063936 cached-kB=1871744
unit: not-found
not-enabled
=== BP 2026-10-17T15:08:47Z
hs-dev-1
before: cddac94 feat(runner,verify72h): AVAIL-LINE-1 — the digest'
porcelain=0
Updating cddac94..7e03c81
Fast-forward
after: 7e03c81 feat(tools,bench.sh,runner): BENCH-HYGIENE-1 — the
constants-md5: 9b0af47b3376
selftest: 48 check(s), 0 failure(s)
verify72h selftest: 66 check(s), 0 failure(s)
bench.sh selftest: 44 check(s), 0 failure(s)
selftest: 54 check(s), 0 failure(s)
breakdown selftest: 10 check(s), 0 failure(s)
pre-warm-verb=1 boot-timing=1
=== C1 2026-10-17T15:10:07Z
hs-dev-1
method: the online backup API in ONE step (python3 sqlite3 backup, pages=-1) — never the sqlite3 CLI .backup (IR-188)
backup: 36 s bytes=1163702272 md5-pi=90724ec4e9092ad2d900772a127ee274 integrity-pi=ok copy-rows=2317979 STAMP=20261017T151006Z BACKUP=/home/homesynapse/hs-backup/20261017T151006Z free-after=98919829504
=== C1b 2026-10-17T15:11:34Z
scp: 18 s bytes=1163702272 md5-desk=90724ec4e9092ad2d900772a127ee274
=== C2 2026-10-17T15:12:50Z
hs-dev-1
HEAD is now at 176adad feat(event-model,automation,persistence): J3 T-B — the skip is counted: automation_completed carries skipped_unavailable as its eighth, additive component; a command action that issued nothing completes skipped; the count rides the executor's locals through the run manager
clone: 176adad feat(event-model,automation,persistence): J3 T-B — the skip is counted: automati ref=HEAD sha=176adad parent=e11ae20 origin-main=176adad
BUILD pid=28461 log=~/hs-bench/build-20261017T151250Z.log
=== C2-poll 2026-10-17T15:13:56Z
/home/homesynapse/hs-bench/build-20261017T151250Z.log
> Task :app:homesynapse-app:installDist

BUILD SUCCESSFUL in 43s
60 actionable tasks: 31 executed, 29 up-to-date
-rwxr-xr-x 1 homesynapse homesynapse 11008 11:13:34 /home/homesynapse/homesynapse-core/app/homesynapse-app/build/install/homesynapse-app/bin/homesynapse-app
=== C3 2026-10-17T15:15:29Z
hs-dev-1
pi-clock 15:15:27Z
  [OK] stopped
cached-before-kB=2077440
cache dropped: cached-kB=354640
11:15:51.401 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
11:15:51.402 [integration-zigbee-0] INFO  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.network_up: stackStatusHandler reported EMBER_NETWORK_UP (buffered)
--- failure tokens ---
boot-log: bench-2026-10-17-111535.log
boot: launched=11:15:37.534 Loaded=+1.415 projection_live=+1.999 network_resumed=+13.867 network_up=+13.868 startup_failed=none
formed=0 resumed=1 relinked=10 startup_failed=0 issues=0 cache_loaded=device_cache_loaded: 10 rebuilt=registry.projection_rebuilt: rows=20 head=2318340 skipped=0 ms=512
contract_declared_lines=13
    [ok] api /api/v1/entities {"rows": 10, "ulids": ["01KX1PA4HSJ581GASYB7DHE40F", "01KX1PB9AAB4VB3E10BD477TV3", "01KXW0157SP56CCSGJCNDCSQNG", "01KXW13WF0D6TYGN13WXHTG87K", "01KXW1W1SBJZERC9MBAMV2DWKE", "01KY12MQW954E4XYNKH0Y5H8VX", "01M3DPGF6Y4YXNXDHBW38ZEX2G", "01M3DM74SGEY7RXVDYSM4PK2XA", "01M3DPKN9WD9B88Q4SVDMSBJVS", "01M3Y4YA6YSYQWVE9ET8FT4HWQ"]} — all asserts satisfied (within 90s)
[PASS] boot-health — 7/7 positive · 0 forbidden
  [--] bundle: /home/homesynapse/hs-bench/bundles/boot-health-20261017T151636Z
deployed=176adad ref=HEAD
=== D 2026-10-17T15:18:40Z
AVAIL-API-1 (1): {"data":[{"entityId":"01KX1PA4HSJ581GASYB7DHE40F","availability":"UNAVAILABLE","stale":false,"deviceId":"01KX1PA4GRZHY2GD37B5CFVQHY","lastReported":"2026-07-19T00:49:15.787079Z","availabilityReason":null,"lastSeenAt":null,"link":null,"probeAnsweredAt":null,"probeWindowStart":null,"probesAnswered":null,"probesMissed":null,"availabilityClass":"mains-floor","reportIntervalSeconds":null,"silenceLimitSeconds":60,"missesToDark":2,"recordIntervalSeconds":3600,"recordDueBy":"2026-10-17T16:18:18.322873Z","recordOverdueSince":null},{"entityId":"01KX1PB9AAB4VB3E10BD477TV3","availability":"AVAILABLE","sta
AVAIL-API-1 (2): probe_answered rows since boot = 2 (the first store rows of B3)
J3 T-A (F-7): ingestion_handler_failed keys = 
J3 T-B (F-6): action_skipped lines = 0 · skipped-actions/eighth-component/of-which-1+ = 0/0/0
IR-115 premise: key_establishment_failed = 0 (0 on a closed boot)
IR-166: availability_contract_declared: device=0xF044D3FFFE9C78D7 class=passive;availability_contract_declared: device=0x4CE175B4C0700000 class=mains-floor;availability_contract_declared: device=0x00178801101A09BB class=mains-floor;availability_contract_declared: device=0xF044D3FFFED2A201 class=passive;
=== E 2026-10-17T15:21:14Z
capture: bytes=5639 md5=559ac60dc338068ad00313d57288115f
rows=10 unavailable=1 meta=recoveryViewPosition,timestamp,viewPosition
=== CLOSE 2026-10-17T15:22:12Z
deployed=176adad bench=7e03c81 boot-log=bench-2026-10-17-111625.log 14303 B pings=5 dark=0 store=1164107776 rows=2318835 backup=/home/homesynapse/hs-backup/20261017T151006Z
kept bench-2026-10-17-111625.log 14303 B
outputs: /c/Users/Nick/Desktop/Code/ClaudeFolder/_scratch/v111/bc10/2026-10-17_BENCH-CORE-10_outputs.txt 5275 B
```
