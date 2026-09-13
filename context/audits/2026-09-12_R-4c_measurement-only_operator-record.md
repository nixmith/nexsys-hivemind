<!--
file: context/audits/2026-09-12_R-4c_measurement-only_operator-record.md
purpose: THE R-4c OPERATOR RECORD — every operator paste-back (⏺) from the R-4c session on the held card hs-fresh, appended in walk order by the navigator with a `date -u` stamp each, plus a per-block verdict against the packet's EXPECTED. §0 is rewritten ONCE at close-out into the verdict surface; §9 carries the compact deviations ledger and the findings card; §10 is the hub's at intake.
audience: the hub (reads §0 then §9 at intake; re-derives from the ⏺s in §1–§7) · the navigator (writes) · Nick (§0)
state-type: operator record (append-only during the session; §0 rewritten once at close)

  ⚠ DATE OF RECORD — READ BEFORE CITING ANY TIMESTAMP. The FILENAME and the packet both say 2026-09-12 (the
  slot the packet was authored for). THE SESSION ACTUALLY RAN SUNDAY 2026-09-13, on Nick's `R4C: Sun`. The
  filename is deliberately NOT renamed — the packet, the operator brief and the v72 b5 dispatch all point at
  this path. Every Z stamp inside is genuinely 2026-09-13. Do not date this evidence 09-12.

  ⚠ TWO FILES, ONE RETURN. This record holds the ⏺s and the verdicts. Its companion holds the instrument
  analysis, the long-form deviations ledger, and the pre-flight source audit:
      context/audits/2026-09-13_R-4c_preflight_source-audit.md
  The split was made at 13:5xZ to keep THIS file inside the packet's `≤ ~30 KB` close-out cap. NOTHING was
  summarised away — the companion carries the original text verbatim. The hub should intake BOTH.

  ⚠ SESSION SHAPE (so the hub does not infer one). The packet's §N nominates "a FRESH Cowork window" as the
  navigator. Nick directed that THIS window be that navigator, so one session carried the desktop phase
  (§0, §1) AND the rig walk — rather than the packet's two-window split. The desktop phase was therefore
  NAVIGATOR-READ, not operator-read: Nick made `nexsys-io/homesynapse-core` PUBLIC mid-session (~13:4xZ) so
  the navigator could read the install-smoke run directly. That is why §0's ⏺ carries no operator paste-back.

  ⚠ WHAT THE ARTIFACT IS, AND HOW IT WAS PROVEN (do not re-derive from the packet's §1 design — it was not used).
  Artifact of record: homesynapse_0.1.0+git20260913.113754.ga458a64_arm64.deb, sha256
  1f46c5c864fe03c261a2c0a15752ac0b4b91c732646fec90e2f572f9aef7eed1, from install-smoke run #53
  (https://github.com/nexsys-io/homesynapse-core/actions/runs/34754940902), commit a458a64, both jobs GREEN.
  Bound to CI by a FOUR-SURFACE custody chain (§3 B1 block 1), NOT by the packet's `version-grammar echo`
  line — that line is auth-gated and was never read (D-1, D-3). The echo line's absence is a deliberate,
  documented substitution, not a gap in the evidence.

status: **CLOSED-PENDING-HUB-AUDIT** — closed 2026-09-13T15:07:27Z. ALL FIVE STOP-GATES MET (R4c-1, R4c-0, R4c-2, **R4c-3 = C-003**, R4c-4). ZERO STOPS.
  Session ran Sunday 2026-09-13 13:57:28Z -> 15:03Z (66 min of a <=90 min budget). 20 operator paste-backs; 11 deviations, all T1.
  Headlines: **C-003 EARNED** (F-R4-1b -> LIVE-VERIFIED; F-R4b-F retired) · **O-2 CLOSED** (R-4b ask #8 answered) ·
  **F-R4c-A: resolution is not adoption** (a bound on C-003) · LASTREPORTED-1b **HALF-VERIFIED** (instant arm proven,
  null arm NOT tested - D-9/D-10, do not bank in full) · card-gradle: absent · anomaly 0 at 6.8x idle load ·
  the Hue absent from the air on a 4th attempt · H8A: not run.
  Packet: context/instructions/2026-09-11_R-4c_measurement-only_zdo-surface-C-003_navigator-packet.md.
  Companion (INTAKE WITH THIS FILE): context/audits/2026-09-13_R-4c_preflight_source-audit.md.
-->

# R-4c operator record — the session ran **Sunday 2026-09-13** (filename says 09-12; see the date note above) · held card `hs-fresh` @ `192.168.1.80` · MEASUREMENT ONLY

## §0 VERDICT SURFACE

# ★ FIVE OF FIVE STOP-GATES MET · ZERO STOPS · C-003 EARNED · O-2 CLOSED ★
**Session ran Sunday 2026-09-13, `13:57:28Z` → `15:03Z` — 66 min of a ≤90 min budget.** Held card `hs-fresh` @ `192.168.1.80` (TZ `EDT -0400`). **MEASUREMENT-ONLY honoured: no Core write, nothing on the core tree changed, one config key added and removed, nothing deleted, one permit-join window, the bench floor restored.**

**ARTIFACT:** `homesynapse_0.1.0+git20260913.113754.ga458a64_arm64.deb` · sha256 `1f46c5c864fe03c261a2c0a15752ac0b4b91c732646fec90e2f572f9aef7eed1` · install-smoke **run #53** `https://github.com/nexsys-io/homesynapse-core/actions/runs/34754940902` · commit `a458a64` · **amd64 green · arm64 green**. Bound to CI by a **four-surface custody chain with no human hash comparison** (GitHub's published digest `883c5f8d…` ≡ downloaded zip ≡ desktop .deb ≡ card .deb). The packet's `version-grammar echo` line is auth-gated and **was never read** — a documented substitution (D-1, D-3), not a gap.

## THE GATES
| gate | verdict | on what |
|---|---|---|
| **§0 GUARD 1** | **MET** | run #53, both jobs green — read at source by the navigator, no operator act |
| **STOP-GATE R4c-1** | **MET (2nd attempt)** | 1st attempt caught a **nine-day-old artifact** (`gef02d13`) whose every assertion passed — D-2 |
| **STOP-GATE R4c-0** | **MET 6/6** | `hs-fresh` · IP pinned · **formed 0** · resumed PAN `0x774c` · ROWS-A 219 · no window key |
| **STOP-GATE R4c-2** | **MET 6/6** | version exact ×2 · active · zero row loss · integrity `ok` · **formed 0** · anomaly 0 at boot |
| **★ STOP-GATE R4c-3 (THE EXIT)** | **★ MET** | `ieee_addr_rsp … device=0xF044D3FFFED2A201` ×1 **and** `device_adopted … ×1` |
| **STOP-GATE R4c-4** | **MET** | `[PASS] boot-health — 6/6 positive · 0 forbidden` · PAN unchanged |

## ★ C-003 — EARNED. THE CHAIN, QUOTED.
```
10:42:34.729979  WARN  zigbee.lookup_eui64_failed: nwk=0x15ac status=0x1
10:42:34.730308  INFO  zigbee.ieee_addr_req: nwk=0x15ac                                    (+0.329 ms)
10:42:35.246104  INFO  zigbee.ieee_addr_rsp: nwk=0x15ac device=0xF044D3FFFED2A201          (+515.796 ms ON THE AIR)
10:42:35.246648  INFO  zigbee.rejoin_candidate: device=0xF044D3FFFED2A201 source=unknown_sender
10:43:47.681301  INFO  zigbee.rejoin_candidate: device=0xF044D3FFFED2A201 source=tc_join   (+72.43 s)
10:43:48.719158  INFO  zigbee.device_proposed: … model=SNZB-02P status=COMPLETE source=rejoin
10:43:48.783944  INFO  zigbee.device_adopted: device=0xF044D3FFFED2A201 deviceId=01M2DKJWVDDHRF8ZX9HQ5B94KX entities=1
```
**Same device, same `nwk=0x15ac`, same `status=0x1` as R-4b's miss, nine days apart, one variable changed — F-R4-1b's second surface.** Adopted **+122.06 s** into a 254 s window (132 s margin). **F-R4b-F retired** (the gap is no longer "mains routers only"). **F-R4-1b → LIVE-VERIFIED.**

## LASTREPORTED-1b — THE TWO ARMS, IN ONE TABLE. **HALF-VERIFIED. DO NOT BANK IN FULL.**
| arm | verdict | evidence |
|---|---|---|
| **instant** | **★ PROVEN, under a stronger test than designed** | an instant from `2026-09-04T19:42:00Z` survived **nine days, a power-cycle and a VERSION UPGRADE** un-refreshed beside `UNAVAILABLE`; a second survived the upgrade+restart; **SNZB-04P driven live `UNAVAILABLE`→`AVAILABLE` and `2026-09-04T19:42:00Z`→`14:45:07.132Z` in-window (+200.4 s)**; nothing anywhere moved instant→null |
| **null** | **NOT TESTED — twice, for two different reasons** | **D-9:** the packet's named witness ("the Hue's entity") **does not exist** — R-4b §0 `PATH TAKEN: B (no light entity existed)`, and the Hue is not even relinked. **D-10:** read-2's `None` is a **KeyError default** for a row absent from read 1 — it prints for ANY new row regardless of the API. A loose grade files "PROVEN" from it. |
| *corroboration* | *substance without the observation* | new entity registered `14:43:48.783Z`, first instant `14:50:28.702Z` — a **399.9 s gap**. Neither adoption-time nor boot-time: **adoption fabricated nothing.** |

## THE OTHER MEASUREMENTS
- **⏺ `card-gradle: absent`** — no Gradle, no `gradlew`, no `java` on PATH. **The held card is run-only; TR-1b must assume cross-build-and-ship.**
- **`bus.delivery_anomaly` = 0** at boot **and 0 across the FULL invocation** — window, two ZDO air exchanges, an adoption, an entity registration, a completed interview, four reporting devices, at **4.21 rows/min ≈ 6.8× the 0.621 idle baseline**. **A bound on OR-BUS-SILENT-DROP, not a closure.** Weight the full-invocation zero above the boot zero.
- **CENSUS OF SIX:** `0xF044D3FFFED2A201` **adopted=1**; all five others **0**; all six `in_adopt_list=1`. Entity rows **3 → 4**.
- **ROWS:** 219 → 228 → 230 → **380**, `integrity_check ok` at both taking points. **Zero row loss across the session.**
- **THE HUE:** powered on ~1 min **inside the open window**; the coordinator saw **nothing** (`lookups=2`, both accounted for). **Fourth failure to reproduce, and the first with the door open and a second resolution surface live. Recorded, not judged.**
- **`H8A: not run`** — settled on the wire (incumbent `gef02d13` on both surfaces), corroborated by `devices=3` unchanged since R-4b and by an unfilled H8-a scaffold.

## ★ THE TWO UNPLANNED RESULTS
1. **F-R4c-A — RESOLUTION IS NOT ADOPTION.** The **SNZB-01P** was resolved over the air (**265.036 ms**) and admitted as a candidate, then produced **no further line and no error**. The device that adopted emitted a second candidate line `source=tc_join`; this one never did. **Hypothesis (untested here): adoption additionally requires a real Trust Center join.** **Bounds what C-003 proves — R-5 and the rehearsals must not assume resolution ⇒ onboarding.**
2. **★ O-2 CLOSED.** A clean operator stop on `a458a64` grades **`Result=success · ActiveState=inactive · ExecMainStatus=143`**, against `Result=exit-code · ActiveState=failed` on R-4 (`g7c57d7f`) and R-4b (`gef02d13`). **R-4b's ask #8 answered.** The exit code is unchanged and correct (143 = SIGTERM); systemd's **grade** flipped. **This evidence exists only because D-11 split the packet's block** — as shipped, the shutdown would have raced the read.

## PER-BLOCK
| block | verdict |
|---|---|
| §0 guard 1 | **MET** (navigator-read) |
| §1 fetch + hash | **MET** — attempt 1 FAILED on the name (D-2), attempt 2 passed on a stronger chain (D-3) |
| B0 preflight | **MET 6/6** (after D-5, D-6) |
| B1 install + boot tokens | **MET** — 9/9 counts once F-1 applied; install 15 s, ordinary upgrade |
| B2 lastReported (1) + card-gradle | **MET on the mechanism**; packet EXPECTED unmet on a card that cannot satisfy it (D-9) |
| **B3 the window · the ZDO chain · the census** | **★ MET — C-003** |
| B4 read 2 · anomaly · disarm | **MET** (null arm not tested — D-10); **the door is proven shut** |
| B5 the restore | **MET** — O-2 closed; `[PASS] boot-health 6/6`; PAN unchanged; dongle stableId byte-identical to R-4b |

**⏺ census: 20 operator paste-backs banked + §0 navigator-read. DEVIATIONS: 11 (D-1…D-11), ALL T1, each filed the same minute. STOPS: NONE — no T3 was reached at any point.** **Seven deviations were INHERITED from R-4b's own ledger; two (D-5, D-11) are among the five instrument defects R-4b's ask #5 asked the hub to correct.**

**THE FINDINGS CARD AND THE TEN ASKS ARE IN §9. The instrument analysis (F-1…F-13, the long-form ledger, B0/B1 long-form readings) is in the companion: `context/audits/2026-09-13_R-4c_preflight_source-audit.md`. BOTH FILES ARE ONE RETURN — INTAKE BOTH.**

## §1 The artifact (§0 guard + §1 fetch + hash)


**⏺ filed 2026-09-13T13:42:55Z**

### §0 GUARD 1 — which artifact (desktop; read from the public run page by the navigator)

```
ARTIFACT: a458a64 — run https://github.com/nexsys-io/homesynapse-core/actions/runs/34754940902 — amd64 green arm64 green
```

**Read at source, not inferred** (`nexsys-io/homesynapse-core` was made public by Nick at ~13:4xZ so the navigator could read the run directly):
- workflow **install-smoke**, run **#53**, `install-smoke.yml` on: push · branch `main` · pushed by `nixmith`
- commit **`a458a64`** = `a458a64563c0d1b96eb6a2e4cdad948cd6e2c37e` — `feat(event-bus): BUS-ORDER-1 — read-forward LIVE delivery: the cursor delivers, the checkpoint floors, the notification wakes (AMD-101 §2)`
- run **Status: Success** · total duration **3m 23s** · **2 jobs completed**, both with the green success mark
- job `103717624036` — "Build image + .deb, install-smoke on a clean **amd64** machine" — **succeeded in 3m 20s** → GREEN
- job `103717624125` — "Build image + .deb, install-smoke on a clean **arm64** machine" — **succeeded in 3m 5s** → GREEN
- both jobs carry a green `Arch-truth assert (.deb Architecture == amd64|arm64)` step and a green `Version-grammar echo` step
- artifacts produced: `distribution-artifacts-amd64` 124 MB `sha256:9be1d076d436a9f6347fddf2f7a5343f54290d081f313b766c7a49bd5e0f5e97` · `distribution-artifacts-arm64` 123 MB `sha256:883c5f8d808622429c937d92e9f711da7b371973ed9d2c2e3996f5441bd6e468` *(these are GitHub's artifact-archive digests, NOT the .deb's own sha256 — the .deb hash is §1's echo line)*

**STOP-GATE §0: PASSED** — no red, no pending; the packet proceeds to §1.
**Navigator note (instrument, not a measurement):** the per-step LOG BODY is not readable anonymously — GitHub answers `Not Found` (text/plain) on every step-log route to a signed-out session, while the run/job pages and their pass/fail marks render fine. The job *colors* above are therefore read at source; the §1 echo LINE must come from a signed-in read. Filed as D-1 in §9.


**⏺ filed 2026-09-13T13:46:08Z**

### §1 attempt 1 — STOP-GATE R4c-1 **FAILED on the NAME** (operator paste-back, verbatim)

```
Nick@DESKTOP-SRK0P9D MINGW64 ~/Desktop/Code/ClaudeFolder/nexsys-hivemind (main)
$ mkdir -p ~/r4c-artifact ~/r3-history && mv ~/r4c-artifact/*.deb ~/r3-history/ 2>/dev/null; cd ~/r4c-artifact && powershell.exe -NoProfile -Command "Expand-Archive -LiteralPath \"$(cygpath -w ~/Downloads/distribution-artifacts-arm64.zip)\" -DestinationPath \"$(cygpath -w ~/r4c-artifact)\" -Force" && find . -name '*_arm64.deb' | wc -l && find . -name '*_arm64.deb' -exec sha256sum {} \;
1
48a33b0dc614a7f74fd0e0a279480e3c2f1f8e1e952f3195f0ffdbad1c626003 *./deb/build/homesynapse_0.1.0+git20260903.124041.gef02d13_arm64.deb
```

**Verdict: MISMATCH · the gate held.** Count = 1 ✓, hash well-formed ✓ — and **the artifact is the wrong one**:
- expected name carries `ga458a64`; **read name carries `gef02d13`** — the 2026-09-03 build.
- read sha256 `48a33b0dc614a7f74fd0e0a279480e3c2f1f8e1e952f3195f0ffdbad1c626003` is **byte-identical to the artifact hash recorded in the R-4b record §0** (`Artifact ef02d13 = 0.1.0+git20260903.124041.gef02d13 · sha256 48a33b0d…`). This is provably the **R-4b session's artifact**, still sitting at `~/Downloads/distribution-artifacts-arm64.zip` nine days later.

**No STOP escalation is owed: the gate did its job and no rig act followed.** The install never ran; the card was never touched; nothing on the core tree changed. §1 is re-attempted under D-2's fix below.


**⏺ filed 2026-09-13T13:50:58Z**

### §1 attempt 2 — **STOP-GATE R4c-1 PASSED** (operator paste-back, verbatim)

```
Nick@DESKTOP-SRK0P9D MINGW64 ~/r4c-artifact
$ mkdir -p ~/r3-history; [ -d ~/r4c-artifact ] && mv ~/r4c-artifact ~/r3-history/r4c-artifact-stale-$(date -u +%Y%m%dT%H%M%SZ); mkdir -p ~/r4c-artifact
echo "--- candidates in ~/Downloads (newest LAST) ---"; ls -lrt --time-style=+%Y-%m-%dT%H:%M:%SZ ~/Downloads/distribution-artifacts-arm64*.zip 2>/dev/null
Z=$(ls -1t ~/Downloads/distribution-artifacts-arm64*.zip 2>/dev/null | head -1); echo "CHOSEN: $Z"; ls -l --time-style=+%Y-%m-%dT%H:%M:%SZ "$Z"; echo "--- zip sha256 (compare to GitHub's artifact digest) ---"; sha256sum "$Z"
cd ~/r4c-artifact && powershell.exe -NoProfile -Command "Expand-Archive -LiteralPath \"$(cygpath -w "$Z")\" -DestinationPath \"$(cygpath -w ~/r4c-artifact)\" -Force" && find . -name '*_arm64.deb' | wc -l && find . -name '*_arm64.deb' -exec sha256sum {} \;
--- candidates in ~/Downloads (newest LAST) ---
-rw-r--r-- 1 Nick 197121 128981400 2026-09-04T11:26:30Z  /c/Users/Nick/Downloads/distribution-artifacts-arm64.zip
-rw-r--r-- 1 Nick 197121 129014717 2026-09-13T08:49:03Z '/c/Users/Nick/Downloads/distribution-artifacts-arm64(1).zip'
CHOSEN: /c/Users/Nick/Downloads/distribution-artifacts-arm64(1).zip
-rw-r--r-- 1 Nick 197121 129014717 2026-09-13T08:49:03Z '/c/Users/Nick/Downloads/distribution-artifacts-arm64(1).zip'
--- zip sha256 (compare to GitHub's artifact digest) ---
883c5f8d808622429c937d92e9f711da7b371973ed9d2c2e3996f5441bd6e468 */c/Users/Nick/Downloads/distribution-artifacts-arm64(1).zip
1
1f46c5c864fe03c261a2c0a15752ac0b4b91c732646fec90e2f572f9aef7eed1 *./deb/build/homesynapse_0.1.0+git20260913.113754.ga458a64_arm64.deb
```

**THE ARTIFACT OF RECORD FOR R-4c:**
- **`homesynapse_0.1.0+git20260913.113754.ga458a64_arm64.deb`**
- **sha256 `1f46c5c864fe03c261a2c0a15752ac0b4b91c732646fec90e2f572f9aef7eed1`**
- from `distribution-artifacts-arm64(1).zip`, 129,014,717 B, mtime `2026-09-13T08:49:03Z`, **zip sha256 `883c5f8d…`**
- built by install-smoke run **#53** = `https://github.com/nexsys-io/homesynapse-core/actions/runs/34754940902`, commit `a458a64`

**Gate conditions:** one .deb ✓ (count = 1) · `ga458a64` in the name ✓ · hash = the run log — **satisfied by a STRONGER chain than the packet specifies, see D-3.** The stale `gef02d13` tree is preserved, not deleted, at `~/r3-history/r4c-artifact-stale-<Z>/`.

## §2 B0 — preflight at the rig


**⏺ filed 2026-09-13T13:53:51Z**

### B0 block 1 of 3 — the overnight digest (BENCH card `hs-dev-1`) — operator paste-back, verbatim

```
homesynapse@hs-dev-1:~ $ uptime
 09:52:41 up 8 days, 17:22,  3 users,  load average: 0.00, 0.00, 0.00
homesynapse@hs-dev-1:~ $ tail -2 ~/hs-bench/digests/nightly.log; ls -t ~/hs-bench/bundles | head -2; ~/bench.sh status
2026-09-12 quiesced AUTO floor: 7/9 · FAIL command-confirm-s31 · bundle /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260912T083148Z · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)
2026-09-13 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 3.57s
command-s31-settle-20260913T083147Z
command-confirm-s31-20260913T083146Z
  [OK] running (pid 40852)
--- health tokens (current boot: /home/homesynapse/hs-bench/bench-2026-09-13-043155.log) ---
04:31:59.522 [hs-sub-registry_projection] INFO  c.h.l.RegistryProjectionSubscriber -- registry.projection_live: devices=6 entities=6 position=25065
04:31:59.941 … zigbee.device_relinked: device=0xF044D3FFFE9C78D7 deviceId=01KX1PB9A5931A8G0F0X03QXT2 — re-pairing, no new adoption
04:31:59.942 … zigbee.device_relinked: device=0x449FDAFFFE688F57 deviceId=01KY12MQVQ204M1VP39F1ZDM33 — re-pairing, no new adoption
04:31:59.943 … zigbee.device_relinked: device=0x00178801101A09BB deviceId=01KX1PA4GRZHY2GD37B5CFVQHY — re-pairing, no new adoption
04:31:59.943 … zigbee.device_relinked: device=0xF044D3FFFED2A201 deviceId=01KXW0156Z1GJ3WCV2G516AKWS — re-pairing, no new adoption
04:31:59.944 … zigbee.device_relinked: device=0xF044D3FFFE1C1E8E deviceId=01KXW13WEGRCT5C0XSQT8WZBG9 — re-pairing, no new adoption
04:31:59.944 … zigbee.device_relinked: device=0x00124B002FA8D1C5 deviceId=01KXW1W1RR66GV98D9QDPB4VXY — re-pairing, no new adoption
04:31:59.944 … zigbee.adoption_maps_rehydrated: devices=6
04:32:07.795 … zigbee.network_resumed: channel=20 panId=0x774c
04:32:07.796 … zigbee.network_up: stackStatusHandler reported EMBER_NETWORK_UP (buffered)
--- failure tokens ---   (EMPTY)
```

**Verdict: MET — the bench is read, healthy, and its baseline is pinned.**
- **THE B5 BASELINE OF RECORD: `8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 3.57s` (2026-09-13).** This is what the restore must return to.
- running (pid 40852) · uptime **8 d 17:22** (the card has been up since ~2026-09-04, i.e. since the R-4b restore — the rig genuinely has not moved) · **failure-token section EMPTY** ✓
- `network_resumed: channel=20 panId=0x774c` — **PAN and channel unchanged since R-4b** ✓
- `1 SKIP(hue-online)` persists — consistent with F-R4b-G (the Hue adopted in the registry, absent from the air). Recorded, not judged.


**⏺ filed 2026-09-13T14:01:27Z**

### B0 blocks 2 & 3 — the halt, the swap, the boot glance (operator paste-back, verbatim)

```
homesynapse@hs-dev-1:~ $ sudo shutdown -h now
homesynapse@hs-dev-1:~ $ Read from remote host hs-dev-1: Connection reset by peer
Connection to hs-dev-1 closed.
client_loop: send disconnect: Connection reset by peer
```
The halt. Card swapped (bench OUT · held `hs-fresh` IN · coordinator dongle undisturbed) and powered on.

**Run 1 — the packet's block VERBATIM (the D-5 defect, reproduced):**
```
hs-fresh
192.168.1.80 2600:1702:6e8a:aff0::47 2600:1702:6e8a:aff0:ebde:ae1b:776c:c32c
13:58:21Z
                                     <-- BLANK: dpkg-query -W -f "${Version}\n" printed a bare newline
0.1.0+git20260903.124041.gef02d13
active
INV=5ad66e5b175f4d62a8fa2c3a6d3ed3f8
0
Sep 13 09:57:28 hs-fresh homesynapse[926]: 09:57:28.140 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
219
ls: cannot access '/var/lib/homesynapse/config/': Permission denied
ls: cannot access '/var/lib/homesynapse/config/integrations/': Permission denied
0
```

**Run 2 — with D-5's fix (`dpkg-query -W homesynapse`):**
```
hs-fresh
192.168.1.80 2600:1702:6e8a:aff0::47 2600:1702:6e8a:aff0:ebde:ae1b:776c:c32c
13:58:30Z
homesynapse     0.1.0+git20260903.124041.gef02d13
0.1.0+git20260903.124041.gef02d13
active
INV=5ad66e5b175f4d62a8fa2c3a6d3ed3f8
0
Sep 13 09:57:28 hs-fresh homesynapse[926]: 09:57:28.140 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
219
ls: cannot access '/var/lib/homesynapse/config/': Permission denied
ls: cannot access '/var/lib/homesynapse/config/integrations/': Permission denied
0
```

**PINNED FOR THE SESSION: `<IP>` = `192.168.1.80`** (the same address R-4b pinned on 2026-09-04 — DHCP has not reassigned).
**PINNED: `INV` at B0 = `5ad66e5b175f4d62a8fa2c3a6d3ed3f8`.**
**PINNED: `ROWS-A = 219`.** (R-4b closed at ROWS-W1 = 212 on 09-04; +7 in nine days.)

| EXPECTED | read | verdict |
|---|---|---|
| `hs-fresh` first line | `hs-fresh` | ✓ correct card |
| an IPv4, pinned | `192.168.1.80` | ✓ |
| the Z clock | `13:58:30Z` | ✓ |
| the incumbent version TWICE | `0.1.0+git20260903.124041.gef02d13` ×2 (run 2) | ✓ **see B0-c-2** |
| `active` | `active` | ✓ |
| `network_formed` count **0** | `0` | ✓ **the hard fence is clear** |
| one `network_resumed`, `channel=20 panId=0x774c` | exactly that, `09:57:28.140` | ✓ **PAN unchanged since R-4b** |
| a row count ⏺ ROWS-A | `219` | ✓ |
| `homesynapse.yaml` + `integrations/zigbee.yaml` listed | **`Permission denied` ×2** | **✗ INSTRUMENT — D-6** |
| window-key count **0** | `0` | ✓ (this read WAS sudo'd, so the 0 is a real absence) |

**STOP-GATE R4c-0: five of six MET; the sixth is an instrument failure, not a rig fact** — closed by D-6's read-only re-read below. No STOP condition was met: PAN unchanged, formed 0, window key absent.


**⏺ filed 2026-09-13T14:03:58Z**

### B0 — D-6's read-only re-read: the gate closes (operator paste-back, verbatim)

```
--- TZ calibration (R-4b D-2; dropped by this packet) ---
EDT -0400
14:02:32Z
--- config tree, sudo (the packet ls was not) ---
/var/lib/homesynapse/config/:
-rw-r--r-- 1 homesynapse homesynapse  132 Aug 13 07:35 api_tokens
-rw-r--r-- 1 homesynapse homesynapse   26 Aug 13 07:35 home_id
-rw------- 1 homesynapse homesynapse  426 Sep  4 14:56 homesynapse.yaml
-rw-r--r-- 1 homesynapse homesynapse   44 Aug 13 07:35 initial_api_token
drwx------ 2 homesynapse homesynapse 4096 Sep  4 15:04 integrations
drwxr-xr-x 2 homesynapse homesynapse 4096 Aug 13 07:35 schemas

/var/lib/homesynapse/config/integrations/:
-rw------- 1 homesynapse homesynapse  299 Sep  4 15:04 zigbee.yaml
-rw------- 1 homesynapse homesynapse  299 Jul 21 07:33 zigbee.yaml.pre-repair-2026-08-30
--- zigbee.yaml as found, numbered ---
     1  serial_port: /dev/zigbee
     2  channel: 20
     3  adopt_devices:
     4    - "0x00178801101A09BB"    # Hue LCA017
     5    - "0xF044D3FFFE9C78D7"    # SNZB-03P
     6    - "0x00124B002FA8D1C5"    # S31 Lite zb
     7    - "0xF044D3FFFED2A201"    # SNZB-02P
     8    - "0xF044D3FFFE1C1E8E"    # SNZB-01P
     9    - "0x449FDAFFFE688F57"    # SNZB-04P contact
```

**★ STOP-GATE R4c-0 — SIX OF SIX MET. CLOSED.** `hs-fresh` ✓ · IP pinned `192.168.1.80` ✓ · formed 0 ✓ · resumed on PAN `0x774c` ✓ · ROWS-A `219` ✓ · **no window key** ✓ (confirmed by eye, not only by count — `permit_join_duration` appears nowhere in the file).


Six of six, same order, uppercase `0x`+16 — matching `IEEEAddress.toString()`'s `%016X` rendering (pre-flight). **The census will read true.**


**Other reads banked for later blocks:** `initial_api_token` is **44 B** on disk ⇒ 43 chars after `tr -d '\r\n'`, matching R-4b's measured `token_len=43` and clearing B2's `-ge 40` gate. `homesynapse.yaml` is 426 B dated Sep 4 14:56 — R-4b's Path-B re-bind, untouched since; **R-4c is measurement-only and does not read or write it.**


**⏺ filed 2026-09-13T14:04:52Z**

**B0 CLOSES — STOP-GATE R4c-0 SIX OF SIX MET.** The derived readings behind this section are in `context/audits/2026-09-13_R-4c_preflight_source-audit.md` § *B0 — long-form readings* (B0-a-1…B0-c-7). In brief:

- **PINNED:** `<IP>` `192.168.1.80` (unchanged since R-4b) · `ROWS-A` **219** · B0 `INV` `5ad66e5b175f4d62a8fa2c3a6d3ed3f8` · **TZ `EDT -0400`** (journal is card-local; +4 h for Z — the B0 resume was `13:57:28Z`).
- **`H8A: not run`, settled on the wire** — the incumbent reads `0.1.0+git20260903.124041.gef02d13` on both surfaces, the packet's own disambiguator for "H8-a did not install"; corroborated by its record being an unfilled 4,533 B scaffold.
- **D-5 proven, not argued** — the packet's block and the corrected block, 9 s apart, same invocation: bare blank vs `homesynapse	0.1.0+git…`. R-4b's D-2 on its third sighting.
- **The card's six adopt IEEEs are the packet's six, in the packet's order** — census validated against `zigbee.yaml` before the window; the packet's T1 truth-clause discharged in advance.
- **B3 step 0a's line arithmetic verified against the actual file** — the key will land on line 2, `channel: 20` slides to line 3, exactly as EXPECTED.
- **The bench baseline B5 must restore to:** `8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 3.57s` (2026-09-13). One-night regression on 09-12 (`7/9 · FAIL command-confirm-s31`), self-recovered — docketed, no R-4c act.

## §3 B1 — install + boot tokens


**⏺ filed 2026-09-13T14:10:32Z**

### B1 block 1 of 4 — copy to the card + the hash's third and fourth surfaces (operator paste-back, verbatim)

```
$ ssh -i ~/.ssh/id_ed25519_pi nick@192.168.1.80 'mkdir -p ~/r3-history && mv ~/homesynapse_*_arm64.deb ~/r3-history/ 2>/dev/null; ls ~/homesynapse_*_arm64.deb 2>/dev/null | wc -l' && cd ~/r4c-artifact && scp -i ~/.ssh/id_ed25519_pi $(find . -name '*_arm64.deb') nick@192.168.1.80: && ssh -i ~/.ssh/id_ed25519_pi nick@192.168.1.80 'sha256sum ~/homesynapse_*_arm64.deb; dpkg-deb --field ~/homesynapse_*_arm64.deb Version Architecture'
0
homesynapse_0.1.0+git20260913.113754.ga458a64_arm64.deb   100%   60MB  68.8MB/s   00:00
1f46c5c864fe03c261a2c0a15752ac0b4b91c732646fec90e2f572f9aef7eed1  /home/nick/homesynapse_0.1.0+git20260913.113754.ga458a64_arm64.deb
Version: 0.1.0+git20260913.113754.ga458a64
Architecture: arm64
```

**Verdict: MET, four of four.** `0` — the card held no .deb before the copy, so no glob can match two files ✓ · sha256 **identical to the desktop read** ✓ · `Version: 0.1.0+git20260913.113754.ga458a64` ✓ · `Architecture: arm64` ✓. The .deb is 60 MB on the card.

**★ THE ARTIFACT'S CUSTODY CHAIN IS NOW UNBROKEN AND FULLY MEASURED — four surfaces, no human hash comparison anywhere in it.** This is the evidence the hub should re-derive from, and it is stronger than the packet's own §1 design asked for:

| # | surface | value | read where |
|---|---|---|---|
| 1 | GitHub's published digest for run #53's `distribution-artifacts-arm64` | `sha256:883c5f8d808622429c937d92e9f711da7b371973ed9d2c2e3996f5441bd6e468` | the run summary page, **anonymously** (navigator) |
| 2 | the downloaded `.zip` on the desktop | `883c5f8d808622429c937d92e9f711da7b371973ed9d2c2e3996f5441bd6e468` | Git Bash `sha256sum` — **exact match to 1** |
| 3 | the `.deb` expanded from that zip, on the desktop | `1f46c5c864fe03c261a2c0a15752ac0b4b91c732646fec90e2f572f9aef7eed1` | Git Bash `sha256sum` |
| 4 | the `.deb` after `scp` to the held card | `1f46c5c864fe03c261a2c0a15752ac0b4b91c732646fec90e2f572f9aef7eed1` | on-card `sha256sum` — **exact match to 3** |

1≡2 binds the archive to CI's own upload; 3≡4 binds the transport. **Therefore the bytes about to be installed are provably the bytes install-smoke run #53 built from commit `a458a64`** — established without opening an auth-gated job log and without any operator comparing 64 hex characters by eye. The `version-grammar echo` line the packet nominates as the origin was never needed (D-1, D-3).


**⏺ filed 2026-09-13T14:16:11Z**

### B1 block 2 of 4 — THE INTEGRITY GATE, in its own block before the act (operator paste-back, verbatim)

```
nick@hs-fresh:~ $ sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;' && sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'PRAGMA integrity_check;'
228
ok
```

**Verdict: MET on the gate's intent · MISMATCH against the packet's literal EXPECTED — the packet is wrong, the card is not. See D-7.**
- `PRAGMA integrity_check` = **`ok`** ✓ — the gate's actual condition, and the one STOP-GATE R4c-2 names ("zero row loss · integrity ok").
- **`ROWS-pre = 228`**, against `ROWS-A = 219` read at B0. **Zero rows lost; nine gained.** STOP-GATE R4c-2's "zero row loss" is MET.


**⏺ filed 2026-09-13T14:18:32Z**

### B1 block 3 of 4 — THE INSTALL (operator paste-back, verbatim)

```
nick@hs-fresh:~ $ date -u +%H:%M:%SZ; sudo apt install -y ~/homesynapse_*_arm64.deb 2>&1 | tail -8; date -u +%H:%M:%SZ; dpkg-query -W -f '${Version}\n' homesynapse; cat /opt/homesynapse/VERSION; sleep 25; systemctl is-active homesynapse.service; sudo sqlite3 … 'SELECT COUNT(*) FROM events;'; sudo sqlite3 … 'PRAGMA integrity_check;'
14:17:05Z
HomeSynapse Core is running.
----------------------------------------------------------------
 HomeSynapse Core installed.
 First-run pairing token: /var/lib/homesynapse/config/initial_api_token
   View it with:  sudo homesynapse-token
   Pair a client with that bearer token to reach the dashboard,
   then delete the token file.
----------------------------------------------------------------
14:17:20Z
0.1.0+git20260913.113754.ga458a64
0.1.0+git20260913.113754.ga458a64
active
230
ok
```

**Verdict: MET, six of six.**
- **the install occupied `14:17:05Z` → `14:17:20Z` — 15 s**, bracketed by the block's own stamps
- **no `downgrad` token anywhere in the tail** ✓ — an ordinary upgrade, exactly as `dpkg --compare-versions` predicted pre-flight (F-5); `--allow-downgrades` was never reached for
- **`0.1.0+git20260913.113754.ga458a64` on BOTH independent surfaces** (`dpkg-query` and `/opt/homesynapse/VERSION`) ✓ — the card is now running the artifact whose four-surface custody chain closed at block 1
- `active` ✓ · ROWS **230 ≥ 228 ≥ 219**, zero loss ✓ · `integrity_check` **`ok`** ✓

**STOP-GATE R4c-2 — four of six conditions CLOSED here** (version exact in both places · active · zero row loss · integrity ok). The remaining two — `network_formed 0` and `bus.delivery_anomaly 0` at boot — are read in block 4.



**⏺ filed 2026-09-13T14:20:57Z**

### B1 block 4 of 4 — the boot tokens as COUNTS on the new bytes (operator paste-back, verbatim)

```
INV=9aa8fc3dd8614cb1b868c70223d03e7d
Configuration issue                        0
lifecycle.integration_schema_registered    1
zigbee.network_resumed                     1
zigbee.network_formed                      0
zigbee.adopt_list_loaded                   0
zigbee.adoption_maps_rehydrated            1
zigbee.availability_seeded                 1
bus.delivery_anomaly                       0
permit_join_opened                         0
c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.adoption_maps_rehydrated: devices=3
c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.availability_seeded: devices=3 from_sidecar=3 unknown=0
c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
```

**Verdict: MET — nine of nine counts correct once F-1's correction is applied; the three-line tail is also correct.**

| token | packet EXPECTED | read | verdict |
|---|---|---|---|
| `Configuration issue` | 0 | **0** | ✓ **PKG-SEC-2 holds on a fourth artifact; R-4's C-1 stays retired** |
| `lifecycle.integration_schema_registered` | 1 | **1** | ✓ matches F-10 (exactly one registered integration) |
| `zigbee.network_resumed` | 1 | **1** | ✓ `channel=20 panId=0x774c` |
| `zigbee.network_formed` | 0 | **0** | ✓ **THE HARD FENCE IS CLEAR** |
| `zigbee.adopt_list_loaded` | 1 | **0** | ✓ **correct — F-1: the line is `log.debug`, root is INFO. The packet's `1` is wrong.** |
| `zigbee.adoption_maps_rehydrated` | 1 | **1** | ✓ **`devices=3`** |
| `zigbee.availability_seeded` | 1 | **1** | ✓ `devices=3 from_sidecar=3 unknown=0` |
| `bus.delivery_anomaly` | 0 | **0** | ✓ FIX-1a's detector silent at boot |
| `permit_join_opened` | 0 | **0** | ✓ no window key present |
| the four-line display | 4 lines | **3 lines** | ✓ **correct — same cause as F-1** |

**★ STOP-GATE R4c-2 — CLOSED, SIX OF SIX.** version exact in both places ✓ · active ✓ · zero row loss ✓ · integrity ok ✓ · **formed 0** ✓ · **anomaly 0 at boot** ✓. New invocation `9aa8fc3dd8614cb1b868c70223d03e7d`.

**★ THE HELD CARD KNOWS THREE DEVICES — this is B3's arithmetic, and it is why C-003 is the exit.** `adoption_maps_rehydrated: devices=3` and `availability_seeded: devices=3 from_sidecar=3 unknown=0`, against **six** IEEEs in `adopt_devices` and **six** on the bench card. The held card carried 2 before R-4b and 3 after it (R-4b adopted the S31 `0x00124B002FA8D1C5` by `source=rejoin`) — **it is still 3, unchanged in nine days**, independently corroborating `H8A: not run`. **The SNZB-02P `0xF044D3FFFED2A201` is NOT among the three** — it is R-4b's measured miss (`lookup_eui64_failed nwk=0x15ac status=0x1`, the router-parented sleepy class). **B3's exit is therefore exactly: take the held card from 3 known devices to 4, over the ZDO `IEEE_addr_req` surface, inside one window.** F-R4-2 (the divergent held/bench registries, 3 vs 6) is re-measured here and unchanged.

## §4 B2 — lastReported (read 1) + card-gradle


**⏺ filed 2026-09-13T14:29:03Z**

### B2 block 1 of 2 — LASTREPORTED-1b, READ 1 on the new bytes (operator paste-back, verbatim)

```
token_len=43
TOKLEN-OK
entities http=200 bytes=589
rows=3  lastReported key on every row: True  null: 0  instant: 3
   01M19RHWXYZYJMM26SX0E41HXN UNAVAILABLE stale=False deviceId=01M19RHWWZXKD4MWM66KAW8MSR lastReported=2026-09-04T19:42:00.386341Z
   01M19XN7NNQQ8S3JJF09T6YKKY AVAILABLE   stale=False deviceId=01M19XN7MXFBA3P5BT4VDY0BM6 lastReported=2026-09-13T14:05:47.232350Z
   01M1PRQN03X8H4MNEZQ62F76F1 AVAILABLE   stale=False deviceId=01M1PRQMZHFV4SAWT1E96B9BQ2 lastReported=2026-09-13T14:24:01.789492Z
```

**Verdict: the mechanism MET — and the packet's EXPECTED is UNMET IN ITS LETTER on a card that cannot satisfy it. Both facts must reach the hub; neither alone is true. See D-9.**

**MET:** `token_len=43` + `TOKLEN-OK` (no token value entered the record) · `http=200`, 589 B · **the `lastReported` key is present on EVERY row** ✓ · the S31's row (`01M1PRQN03X8H4MNEZQ62F76F1`, identified as the S31 in R-4b §0 C4) carries an ISO-8601 Z instant ✓ · **no row shows an instant near this boot's clock without a report behind it** ✓ — the invariant the packet names as the FINDING condition did **not** fire.

**UNMET:** the packet expects "at least one row with `lastReported=None` that has NEVER reported (the Hue's entity from R-4)". **`null: 0` — no such row exists.** All three entities on this card have reported at some point, so **the null arm of LASTREPORTED-1b cannot be exercised here.**

**★ THE THREE INSTANTS ARE A STRONGER PROOF THAN THE NULL ROW WOULD HAVE BEEN.** Correlated against this session's own timeline — pre-install boot `13:57:28Z` (INV `5ad66e5b`) · install `14:17:05→14:17:20Z` · post-install boot INV `9aa8fc3d`:

| row | availability | lastReported | what it proves |
|---|---|---|---|
| `01M19RHWXYZ…` | **UNAVAILABLE** | **2026-09-04T19:42:00Z** — during R-4b | **nine days, one card power-cycle, and a VERSION UPGRADE later, the instant is still the one the device actually last spoke at.** It was not refreshed to boot, to adoption, or to now. |
| `01M19XN7NNQ…` | AVAILABLE | `14:05:47Z` — **11.5 min BEFORE this boot** | a value persisted across the upgrade **and the service restart** — not re-stamped by either |
| `01M1PRQN03X…` (the S31) | AVAILABLE | `14:24:01Z` — **after** this boot | a genuine live report on the new bytes |

A `null` row would have proven only *"we did not invent an instant for something that never reported."* Row 1 proves the harder thing: **an upgrade and a restart do not rewrite a real instant, even a nine-day-stale one, and `UNAVAILABLE` + a true stale instant is exactly the "never claims a freshness it cannot show" contract.** HONESTY-1's mechanism is demonstrated on silicon, on the new bytes, under a stronger test than the packet designed.

**⚠ WHAT THE HUB MUST NOT BANK: "LASTREPORTED-1b VERIFIED" IN FULL.** The invariant has two arms. The **instant arm is proven** (above). The **null arm — "null at adoption, before any report" — remains UNTESTED ON SILICON**, because this card holds no never-reported entity. **The one chance to test it in this session is B3→B4:** if the SNZB-02P adopts in the window, B4's read 2 will show a *new* row. **If that new row is `null`, the null arm is proven; if it already carries an instant, the null arm stays untested and must be recorded as such.** This is now the second thing B3 is worth beyond C-003 — flagged before the window rather than discovered after it.


**⏺ filed 2026-09-13T14:32:40Z**

### B2 block 2 of 2 — the gradle answer + the IEEE→deviceId probe (operator paste-back, verbatim)

```
card-gradle: absent
--- the card's known devices: IEEE -> deviceId ---
zigbee.device_relinked: device=0x00124B002FA8D1C5 deviceId=01M1PRQMZHFV4SAWT1E96B9BQ2 — re-pairing, no new adoption
zigbee.device_relinked: device=0xF044D3FFFE9C78D7 deviceId=01M19XN7MXFBA3P5BT4VDY0BM6 — re-pairing, no new adoption
zigbee.device_relinked: device=0x449FDAFFFE688F57 deviceId=01M19RHWWZXKD4MWM66KAW8MSR — re-pairing, no new adoption
```

**⏺ `card-gradle: absent`** — the owed line, answered. No Gradle and no `gradlew` on the held card; `which gradle java` printed nothing, so neither is on PATH. **TR-1b's driver shape follows this: the card cannot build, only run.** (Block run inside a subshell per F-6 — the packet's bare `exit 0` would have closed the ssh session on its success path. `absent` was the outcome, so the hazard did not fire, but the wrapper is what made that safe to find out.)

**★ THE HELD CARD'S REGISTRY, FULLY RESOLVED — three known, three unknown, and TWO of the five provocations are unknown senders.** Joining this probe to B2 read 1 by `deviceId`:

| IEEE | device | deviceId | entity | availability | lastReported (read 1) | known to the card? |
|---|---|---|---|---|---|---|
| `0x00124B002FA8D1C5` | **S31 Lite zb** | `01M1PRQMZHFV…` | `01M1PRQN03X…` | AVAILABLE | `14:24:01Z` (live) | **KNOWN** |
| `0xF044D3FFFE9C78D7` | **SNZB-03P** motion | `01M19XN7MXF…` | `01M19XN7NNQ…` | AVAILABLE | `14:05:47Z` | **KNOWN** |
| `0x449FDAFFFE688F57` | **SNZB-04P** contact | `01M19RHWWZX…` | `01M19RHWXYZ…` | **UNAVAILABLE** | **`2026-09-04T19:42Z`** (9 days) | **KNOWN** |
| **`0xF044D3FFFED2A201`** | **SNZB-02P** temp/hum | — | — | — | — | **UNKNOWN — C-003's target** |
| **`0xF044D3FFFE1C1E8E`** | **SNZB-01P** button | — | — | — | — | **UNKNOWN — a second witness** |
| `0x00178801101A09BB` | Hue LCA017 | — | — | — | — | **UNKNOWN (and absent from the air, F-R4b-G)** |

**This confirms the R-4b identification of `01M1PRQN03X…` as the S31, and resolves the two entities R-4b left unnamed.** It also settles D-9 completely: **the three entities are the S31, the SNZB-03P and the SNZB-04P — there is no Hue entity, so the packet's named null witness could not have existed.** The Hue's device is not even relinked; it is absent from the held card's registry entirely.

**★ B3 IS NOW WORTH MORE THAN THE PACKET PLANNED — three distinct measurements, not one.** The packet hedges: *"The SNZB-01P and SNZB-04P: the same shape if they were unknown senders, or nothing (already known)."* That is now **decided, before the window**:
1. **C-003's designated exit** — the SNZB-02P `0xF044D3FFFED2A201`, unknown, the R-4b miss.
2. **A SECOND, INDEPENDENT C-003 WITNESS** — the SNZB-01P `0xF044D3FFFE1C1E8E` is **also unknown to this card** and is also a battery-powered sleepy device. If both resolve over `IEEE_addr_req`, C-003 is minted on **two devices of the sleepy class in one window** rather than one. If one resolves and one does not, that is a **device-class boundary finding** of the same kind R-4b produced for the mains-router/sleepy split — a better outcome than a bare single hit.
3. **THE BEST AVAILABLE `lastReported` TRANSITION TEST** — the SNZB-04P is KNOWN, **UNAVAILABLE**, and carries a **nine-day-stale** instant. Provocation 3 should drive it `UNAVAILABLE → AVAILABLE` and `2026-09-04T19:42Z → 2026-09-13T14:xxZ` **in one step**. That is a direct, live exercise of HONESTY-1's update path on an entity whose staleness was measured minutes earlier — and it is the strongest `lastReported` movement available on this card given D-9.

**Provocation priority, re-derived from measurement (the packet's ORDER is already correct — only the weighting changes):** #1 and #2 are load-bearing for C-003 · #3 is load-bearing for LASTREPORTED-1b · **#4 (SNZB-03P) and #5 (S31) are corroborating only** — both are already KNOWN and already reporting live, so they can be dropped without loss if the window runs short or if the S31's load must not be cycled (D-8).

## §5 B3 — the window: the ZDO chain, the census


**⏺ filed 2026-09-13T14:34:37Z**

### B3 step 0a — the window key, guarded (operator paste-back, verbatim)

```
     1  serial_port: /dev/zigbee
     2  permit_join_duration: 254
     3  channel: 20
     4  adopt_devices:
     5    - "0x00178801101A09BB"    # Hue LCA017
     6    - "0xF044D3FFFE9C78D7"    # SNZB-03P
     7    - "0x00124B002FA8D1C5"    # S31 Lite zb
     8    - "0xF044D3FFFED2A201"    # SNZB-02P
     9    - "0xF044D3FFFE1C1E8E"    # SNZB-01P
    10    - "0x449FDAFFFE688F57"    # SNZB-04P contact
1
```

**Verdict: MET, exactly as B0-c-6 predicted from the pre-window read.** Line 1 `serial_port` ✓ · **line 2 `permit_join_duration: 254`** ✓ · line 3 `channel: 20` ✓ · the six IEEEs on lines 5–10 ✓ · **count `1`** ✓ — no duplicate key, so the idempotency guard (R-4b's D-7, correctly carried into this packet) had nothing to catch and the `sed` inserted cleanly. The pre-window copy is preserved at `/root/` per the block's own fallback; nothing was deleted.

`254` is exactly the schema ceiling (`permit_join_duration`: integer, min 1, **max 254**, no default) — so **no clamp and no `zigbee.permit_join_clamped` WARN is expected** at the arm. **The door is NOT yet open: the key only takes effect on the restart in step 0b.**


**⏺ filed 2026-09-13T14:49:01Z**

### B3 step 0b — THE WINDOW: the arm and the 24-tick countdown (operator paste-back, verbatim)

```
INV=83e5cb845ff7466d90c8366c1245867e
2026-09-13T10:41:46.697497-04:00 hs-fresh homesynapse[1803]: … zigbee.network_resumed: channel=20 panId=0x774c
2026-09-13T10:41:46.727636-04:00 hs-fresh homesynapse[1803]: … zigbee.permit_join_opened: duration=254s
T0 countdown-zero = 14:42:06Z  (the TRUE open is the permit_join_opened line above)
 10s  lookups=0  zdo_req=0  zdo_rsp=0  adopted=0  unresolved=0  ignored_closed=0
 20s  lookups=0  zdo_req=0  zdo_rsp=0  adopted=0  unresolved=0  ignored_closed=0
 30s  lookups=1  zdo_req=1  zdo_rsp=1  adopted=0  unresolved=0  ignored_closed=0
 40s … 60s   (monotone, unchanged: lookups=1 zdo_req=1 zdo_rsp=1 adopted=0 unresolved=0 ignored_closed=0)
 70s  lookups=2  zdo_req=2  zdo_rsp=2  adopted=0  unresolved=0  ignored_closed=0
 80s … 100s  (monotone, unchanged: lookups=2 zdo_req=2 zdo_rsp=2 adopted=0 unresolved=0 ignored_closed=0)
111s  lookups=2  zdo_req=2  zdo_rsp=2  adopted=1  unresolved=0  ignored_closed=0
121s … 242s  (monotone, unchanged: lookups=2 zdo_req=2 zdo_rsp=2 adopted=1 unresolved=0 ignored_closed=0)
LOOP END at 14:46:08Z
```
*(full 24 tick lines in the operator's paste; the three transition ticks — 30s, 70s, 111s — and the terminal tick are quoted whole above, the rest are monotone as the packet permits.)*

**Operator's note, recorded verbatim:** *"Every device was touched — most buttons and switches were activated and/or pressed multiple times. I opened my front door twice for 04P. I even turned on my Hue bulb lamp for a minute or so, then turned that off."* **Provocation coverage was therefore total: all five packet provocations plus a Hue mains power cycle.**

**Verdict: the window ran clean. `permit_join_opened: duration=254s` ×1 · `network_resumed` ×1 · `network_formed` 0 — the hard fence held. 2 lookups → 2 `ieee_addr_req` → 2 `ieee_addr_rsp` → 1 `device_adopted` → 0 unresolved → 0 ignored_closed.**

**★ THE ZDO SURFACE FIRED TWICE ON SILICON AND FAILED ZERO TIMES.** `unresolved=0` across the whole window is decisive on F-3's ambiguity: a `zigbee.ieee_addr_rsp_failed` returns empty from `requestIeeeAddress` and the adapter follows it with `rejoin_candidate_unresolved … reason=zdo_miss`. **Zero unresolved ⇒ neither of the two `zdo_rsp` counts was a failure** — both were genuine `ieee_addr_rsp` successes. **Two unknown sleepy devices were resolved OVER THE AIR**, which is exactly the surface R-4b's miss (`lookup_eui64_failed nwk=0x15ac status=0x1`) called for and F-R4-1b built. *(Which devices, and which one adopted, is settled by the harvest census — NOT inferred here.)*

**★ F-12 CONFIRMED AND MEASURED — the countdown's zero is 19.27 s late.**

| | |
|---|---|
| window OPEN (true, from `permit_join_opened`) | **`14:41:46.727Z`** |
| `T0` countdown-zero | `14:42:06Z` |
| **offset `T0 − open`** | **`19.272 s`** (F-12 predicted 13–17 s) |
| true door CLOSE = open + 254 s | **`14:46:00.727Z`** |
| **that close in the PRINTED column** | **`234.7 s` — not `254 s`** |
| LOOP END `14:46:08Z` | **7.3 s AFTER the door shut** |

The packet's own banner would have recorded the window as opening at `14:42:06Z`. **The fix is what makes the line above a measurement instead of an estimate**, and it is what lets this record state that the final tick reported on a closed door.

**★ EVERY EVENT LANDED WELL INSIDE THE WINDOW** (bounds from the tick interval, absolute):
- first lookup + ZDO exchange: between **`14:42:26Z` and `14:42:36Z`** — ~40–50 s after open
- second lookup + ZDO exchange: between **`14:43:06Z` and `14:43:16Z`** — ~80–90 s after open
- the adoption: between **`14:43:46Z` and `14:43:57Z`** — ~120–130 s after open, **2 min 4 s before the close**

**★ `ignored_closed = 0` THROUGHOUT, INCLUDING THE POST-CLOSE TICKS.** No unknown sender transmitted after `14:46:00.727Z` — consistent with provocations having stopped by ~190 s. It also means the door's closure is **not** independently witnessed this session (nothing tried it); the disarm proof at B4 is what establishes it.

**⚠ THE OPEN QUESTION THE COUNTDOWN CANNOT ANSWER: two devices resolved, ONE adopted.** `zdo_rsp=2` but `adopted=1`, with `unresolved=0` — so the second resolved device did **not** fail, and did **not** adopt, within this invocation. Candidate explanations (to be decided by the harvest, not guessed): a `device_proposed` whose interview had not completed (`proposal_incomplete`), or a resolution for a device whose admission path took a branch that emits no `device_adopted`. **This is a genuine finding either way and is the second thing the harvest must settle, after the census.**


**⏺ filed 2026-09-13T14:51:10Z**

### B3 harvest — THE CHAIN AND THE CENSUS (operator paste-back, verbatim) · ★ STOP-GATE R4c-3 PASSED ★

```
--- chain lines total: 11  (display capped at 60)          [no truncation: 11 of 11 shown]
2026-09-13T10:42:34.729979-04:00 … WARN  EzspCoordinatorProtocol -- zigbee.lookup_eui64_failed: nwk=0x15ac status=0x1
2026-09-13T10:42:34.730308-04:00 … INFO  EzspCoordinatorProtocol -- zigbee.ieee_addr_req: nwk=0x15ac
2026-09-13T10:42:35.246104-04:00 … INFO  EzspCoordinatorProtocol -- zigbee.ieee_addr_rsp: nwk=0x15ac device=0xF044D3FFFED2A201
2026-09-13T10:42:35.246648-04:00 … INFO  ZigbeeIntegrationAdapter -- zigbee.rejoin_candidate: device=0xF044D3FFFED2A201 nwk=0x15ac source=unknown_sender
2026-09-13T10:43:08.576384-04:00 … WARN  EzspCoordinatorProtocol -- zigbee.lookup_eui64_failed: nwk=0xa5da status=0x1
2026-09-13T10:43:08.576816-04:00 … INFO  EzspCoordinatorProtocol -- zigbee.ieee_addr_req: nwk=0xa5da
2026-09-13T10:43:08.841852-04:00 … INFO  EzspCoordinatorProtocol -- zigbee.ieee_addr_rsp: nwk=0xa5da device=0xF044D3FFFE1C1E8E
2026-09-13T10:43:08.842014-04:00 … INFO  ZigbeeIntegrationAdapter -- zigbee.rejoin_candidate: device=0xF044D3FFFE1C1E8E nwk=0xa5da source=unknown_sender
2026-09-13T10:43:47.681301-04:00 … INFO  ZigbeeIntegrationAdapter -- zigbee.rejoin_candidate: device=0xF044D3FFFED2A201 nwk=0x15ac source=tc_join
2026-09-13T10:43:48.719158-04:00 … INFO  ZigbeeAdoptionSlice -- zigbee.device_proposed: device=0xF044D3FFFED2A201 manufacturer=eWeLink model=SNZB-02P profile=sonoff_snzb_02p status=COMPLETE source=rejoin
2026-09-13T10:43:48.783944-04:00 … INFO  ZigbeeAdoptionSlice -- zigbee.device_adopted: device=0xF044D3FFFED2A201 deviceId=01M2DKJWVDDHRF8ZX9HQ5B94KX entities=1
--- census
0x00178801101A09BB  adopted_this_invocation=0  in_adopt_list=1
0xF044D3FFFE9C78D7  adopted_this_invocation=0  in_adopt_list=1
0x00124B002FA8D1C5  adopted_this_invocation=0  in_adopt_list=1
0xF044D3FFFED2A201  adopted_this_invocation=1  in_adopt_list=1
0xF044D3FFFE1C1E8E  adopted_this_invocation=0  in_adopt_list=1
0x449FDAFFFE688F57  adopted_this_invocation=0  in_adopt_list=1
```

# ★★★ STOP-GATE R4c-3 — MET. C-003 IS EARNED ON SILICON. ★★★
**`ieee_addr_rsp … device=0xF044D3FFFED2A201` ×1** ✓ · **`device_adopted: device=0xF044D3FFFED2A201` ×1** ✓ · census `adopted_this_invocation=1` for that IEEE and **0 for every other** ✓ · all six `in_adopt_list=1` ✓ · **`network_formed` 0 throughout** ✓ · 11 of 11 chain lines displayed, **no truncation** ✓.

**★ THE CONTROLLED COMPARISON — same device, same network address, same status byte, nine days apart, one variable changed.**

| | R-4b (2026-09-04) | **R-4c (2026-09-13)** |
|---|---|---|
| the miss | `lookup_eui64_failed: nwk=**0x15ac** status=**0x1**` | `lookup_eui64_failed: nwk=**0x15ac** status=**0x1**` — **byte-identical** |
| what followed | `rejoin_candidate_unresolved … reason=lookup_miss` — **dead end** | `ieee_addr_req: nwk=0x15ac` **329 µs later** |
| the air | *(no second surface existed)* | `ieee_addr_rsp: nwk=0x15ac device=0xF044D3FFFED2A201` — **the device answers for itself** |
| outcome | the sleepy device stayed unknown | **`device_adopted … deviceId=01M2DKJWVDDHRF8ZX9HQ5B94KX entities=1`** |

The only difference between the two runs is **F-R4-1b's second over-the-air surface.** R-4b's F-R4b-F recorded the ZDO follow-on as *"now EVIDENCED"*; **it is now implemented, measured and proven on MG24 silicon.** The R-4b boundary finding — *"F-R4-1 as shipped closes the silent-rejoiner gap for mains routers only"* — **is retired: the gap is now closed for the router-parented sleepy class as well.**

**★ THE MEASURED LATENCIES (the numbers the timestamp fix, F-13, exists to make writable):**

| leg | SNZB-02P (`0x15ac`) | SNZB-01P (`0xa5da`) |
|---|---|---|
| `lookup_eui64_failed` → `ieee_addr_req` | **0.329 ms** | **0.432 ms** |
| **`ieee_addr_req` → `ieee_addr_rsp` — THE AIR** | **515.796 ms** | **265.036 ms** |
| `ieee_addr_rsp` → `rejoin_candidate` | 0.544 ms | 0.162 ms |
| **miss → admitted candidate (total)** | **516.669 ms** | **265.630 ms** |
| `rejoin_candidate(unknown_sender)` → `rejoin_candidate(tc_join)` | **72.43 s** | — *(never occurred)* |
| `tc_join` → `device_proposed` | 1037.857 ms | — |
| `device_proposed` → `device_adopted` | **64.786 ms** | — |
| **window-open → adopted** | **122.06 s** (door closed at 254 s — **132 s of margin**) | — |

**Two independent measurements of the new over-the-air surface: 516 ms and 265 ms, against a 10 s deadline — the surface is roughly 20–40× inside its own timeout.** For scale, R-4b's coordinator-table path (`0x0061`, a local read) carried the mains S31 from candidate to adopted in 315 ms; the air adds a few hundred milliseconds, not seconds.

# ★ THE DAY'S SECOND FINDING — F-R4c-A: RESOLUTION IS NOT ADOPTION
**The SNZB-01P `0xF044D3FFFE1C1E8E` was resolved over the air and then stopped.** Its chain is complete and clean through `rejoin_candidate … source=unknown_sender` at `10:43:08.842` — and produces **no further line of any kind**: no `tc_join`, no `device_proposed`, no `device_adopted`, and critically **no `rejoin_candidate_unresolved`, no `proposal_incomplete`, no `ieee_addr_rsp_failed`.** It is not an error path. It is a path that simply ends.

**The discriminator is in chain A and is explicit in the log:** the SNZB-02P emitted a **second** `rejoin_candidate` line carrying **`source=tc_join`** 72.43 s after its first, and adoption followed **1.1 s** later. The SNZB-01P never produced one.

**Leading explanation — recorded as a HYPOTHESIS, not a conclusion, because this session did not test it:** the ZDO surface's job is to *identify* an unknown sender so it can be admitted as a **candidate**; **adoption additionally requires the device to complete a real Trust Center join**, which is what makes the interview possible. Warming the SNZB-02P in a closed hand woke it and drove a genuine rejoin (`tc_join`); a short press on the SNZB-01P transmitted a frame that was resolved, but never triggered a rejoin, so no interview ever ran.
**If that reading is right, it bounds exactly what C-003 proves: the resolution surface works and is fast — resolution ALONE is not sufficient for adoption.** Anything designed on top of this (R-5, the 72-hour rehearsals, the fleet-onboarding story) must not assume that resolving an unknown sender will onboard it.
**What would settle it, cheaply, next session:** provoke the SNZB-01P in a way that forces a rejoin rather than a report (battery pull-and-reinsert inside an open window) and look for `source=tc_join`. **A one-line prediction to test: the same device, provoked to rejoin, will adopt over the same ZDO path.**

# ★ F-R4b-G RE-CONFIRMED ON A FOURTH ATTEMPT — the Hue is absent from the air
The operator powered the Hue lamp on for ~1 minute inside the open window and then off. **The coordinator saw nothing**: `lookups=2` for the whole window, and both are accounted for (`0x15ac`, `0xa5da`). No third nwk, no third lookup, no `rejoin_ignored_window_closed`. **This is the fourth failure to reproduce playbook §6's "Hue LCA017: wall power-cycle ⇒ re-announce" — and the first under an OPEN permit-join window on an instrumented coordinator with the ZDO surface live.** Recorded, not judged, per the packet: **the Hue is adopted in the bench registry and absent from the air.** The demotion R-4b asked for (VERIFIED → CONTESTED) now has a fourth data point, and this attempt removes the last plausible excuse — the door was open and a second resolution surface was listening.

## §6 B4 — lastReported (read 2), the anomaly count, the disarm


**⏺ filed 2026-09-13T14:53:21Z**

### B4 block 1 — LASTREPORTED-1b, READ 2 after the window (operator paste-back, verbatim)

```
TOKLEN-OK
entities http=200 bytes=755
rows before=3 after=4 new=1
   01M19RHWXYZYJMM26SX0E41HXN AVAILABLE deviceId=01M19RHWWZXKD4MWM66KAW8MSR lastReported 2026-09-04T19:42:00.386341Z -> 2026-09-13T14:45:07.132090Z
   01M19XN7NNQQ8S3JJF09T6YKKY AVAILABLE deviceId=01M19XN7MXFBA3P5BT4VDY0BM6 lastReported 2026-09-13T14:05:47.232350Z -> 2026-09-13T14:44:31.278087Z
   01M1PRQN03X8H4MNEZQ62F76F1 AVAILABLE deviceId=01M1PRQMZHFV4SAWT1E96B9BQ2 lastReported 2026-09-13T14:24:01.789492Z -> 2026-09-13T14:49:01.793336Z
   01M2DKJWVSJCHB6TTAJSW3D880 AVAILABLE deviceId=01M2DKJWVDDHRF8ZX9HQ5B94KX lastReported None -> 2026-09-13T14:50:28.702945Z
```

**Verdict: MET on every condition the packet names.** `new=1` (≥1) ✓ · every entity that reported in the window moved forward ✓ · **nothing moved instant → null** ✓ · `http=200`, token length only ✓ · **`rows before=3 after=4` — the registry went 3 → 4, which is C-003's exit restated as arithmetic.**

| entity | device | before → after | timing vs the window (`14:41:46.727Z`–`14:46:00.727Z`) |
|---|---|---|---|
| `01M19RHWXYZ…` | **SNZB-04P** | **`UNAVAILABLE` → `AVAILABLE`** · `2026-09-04T19:42:00Z` → `14:45:07.132Z` | **IN-WINDOW, +200.4 s** |
| `01M19XN7NNQ…` | SNZB-03P | `14:05:47Z` → `14:44:31.278Z` | **IN-WINDOW, +164.6 s** |
| `01M1PRQN03X…` | S31 | `14:24:01Z` → `14:49:01.793Z` | post-close +181.1 s (its own cadence) |
| **`01M2DKJWVSJ…`** | **SNZB-02P (NEW)** | — → `14:50:28.702Z` | post-close +268.0 s |

**★ THE PREDICTED TRANSITION LANDED — the strongest live exercise of HONESTY-1's update path available on this card.** The SNZB-04P was identified at B2 as KNOWN, `UNAVAILABLE`, carrying a **nine-day-stale** instant. Provocation 3 drove it, **in a single step, `UNAVAILABLE` → `AVAILABLE` and `2026-09-04T19:42:00Z` → `2026-09-13T14:45:07Z`**, with the new instant falling **inside the permit-join window at +200.4 s**. Predicted from the registry probe **before** the window, measured after it.

# ⚠ ★ CRITICAL CORRECTION — THE `None` IS A SCRIPT ARTIFACT, NOT AN OBSERVED NULL. THE NULL ARM REMAINS UNTESTED.
The new row prints `lastReported None -> 2026-09-13T14:50:28.702945Z`. **That `None` is NOT a value read from the API.** It is the diff script evaluating `(a.get(k) or {}).get('lastReported')` against **read 1**, which was taken at `14:29Z` — **before the adoption at `14:43:48.783Z`.** The entity did not exist in read 1, so the lookup returns `None` **regardless of what the API ever held.** The packet's own B4 block produces this for *every* new row by construction.

**The null arm of LASTREPORTED-1b is therefore STILL NOT TESTED ON SILICON.** The observable window was `14:43:48.783Z` (registration) → `14:50:28.702Z` (first report) = **399.9 s / 6.7 minutes**, and read 2 was taken roughly **two seconds after** that report landed. The one chance this session had was missed by seconds. **The hub must NOT bank "LASTREPORTED-1b VERIFIED" in full; D-9's gap stands, now for a second, different reason.**

**★ WHAT IS NEVERTHELESS STRONGLY CORROBORATED — the substance of the null arm, without the literal observation.**
| | |
|---|---|
| entity registered (adoption, `entities=1`) | `14:43:48.783Z` |
| first instant the entity carries | `14:50:28.702Z` |
| **gap** | **399.919 s (6.7 min)** |
**The instant is neither the adoption time nor this boot's time — it is 400 seconds after registration.** The failure mode HONESTY-1 exists to prevent is `lastReported` being stamped at adoption; had that occurred, this row would read `14:43:48`. It does not. **Adoption fabricated no instant; a real report set the value.** This is the *substance* of "null at adoption, an instant only after a report" — established by the 400 s gap rather than by reading a null. **Recorded as corroboration, explicitly NOT as a pass of the null arm.**

**★ D-10 (filed) — the packet's read-2 diff CANNOT test the null arm, by construction, and silently manufactures a false positive for it.** A new row's "before" value is always `None`, because the row is absent from read 1. A navigator grading loosely would file "null → instant, LASTREPORTED-1b null arm PROVEN" — **from a KeyError default.** **Rec to the hub: to test the null arm, the read must happen BETWEEN registration and first report** — e.g. a short polling loop on `/api/v1/entities` started at the moment of the arm, or a re-read triggered on the `device_adopted` line, capturing the new row's `lastReported` directly rather than by diff. A 6.7-minute observable window existed today and was entirely adequate; only the instrument was missing.


**⏺ filed 2026-09-13T14:55:45Z**

### B4 block 2 — the anomaly count for the whole invocation + row growth (operator paste-back, verbatim)

```
nick@hs-fresh:~ $ INV=$(…); sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -c "bus.delivery_anomaly"; … | grep "bus.delivery_anomaly" | sed 's/^.*WARN *//' | head -5; sudo sqlite3 … 'SELECT COUNT(*) FROM events;'; date -u +%H:%M:%SZ
0
380
14:53:24Z
```

**Verdict: MET.** `bus.delivery_anomaly` **0** across the whole invocation, **no lines** ✓ · **ROWS-W1 = 380 @ `14:53:24Z` > ROWS-A 219** ✓ (+161).

**★ THIS IS THE LOAD-BEARING ANOMALY READ, AND IT SHOULD BE WEIGHTED ABOVE B1's.** B1's zero was measured across a quiet boot — the weakest available exercise of the delivery path. **This zero spans invocation `83e5cb845ff7466d90c8366c1245867e` in full: the 254 s permit-join window, TWO over-the-air ZDO exchanges, one adoption, one entity registration, a completed device interview (`status=COMPLETE`), and four devices reporting.** And the store quantifies that load:

| interval | rows | rate |
|---|---|---|
| pre-install baseline (B1 blk 2) | 219 → 228 | **0.621 rows/min** *(R-4b independently: 0.643)* |
| post-install through the window (this read) | 230 @ ~`14:17:45Z` → **380** @ `14:53:24Z` | **4.21 rows/min** |
| | | **≈ 6.8× the quiet baseline** |

**Zero silent delivery drops on BUS-ORDER-1's own bytes while the bus carried ~6.8× its idle load.** `a458a64` *is* BUS-ORDER-1 (read-forward LIVE delivery: the cursor delivers, the checkpoint floors, the notification wakes), and FIX-1a's detector is the instrument. **Bank this as a BOUND on OR-BUS-SILENT-DROP measured on the wire under real traffic — not as a closure.** The closure counter (twenty green pushes, kind E 0) is a separate instrument and is unaffected by this reading.

**Zero row loss across the entire session, on four independent reads:** 219 (B0) → 228 (B1 gate) → 230 (post-install) → 380 (post-window), with `PRAGMA integrity_check` = `ok` at both points it was taken.


**⏺ filed 2026-09-13T14:57:20Z**

### B4 block 3 — THE DISARM (operator paste-back, verbatim)

```
nick@hs-fresh:~ $ sudo sed -i '/^[[:space:]]*permit_join_duration:/d' … && sudo grep -cE '^[[:space:]]*permit_join_duration:' …; sudo systemctl restart homesynapse.service && sleep 25 && INV=$(…) && sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -cE "permit_join_opened|Configuration issue|network_formed"; systemctl is-active homesynapse.service; sudo journalctl … | grep -c "zigbee.network_resumed"
0
0
active
1
```

**Verdict: MET, four of four. THE DOOR IS PROVEN SHUT.** window key removed (`0`) ✓ · **the combined count `0`** — no `permit_join_opened`, no `Configuration issue`, no `network_formed` in the post-disarm invocation ✓ · `active` ✓ · `network_resumed` `1` ✓.

**★ THE WINDOW WAS OPENED EXACTLY ONCE AND IS NOW CLOSED BY CONFIGURATION, NOT BY TIMEOUT.** The packet's fence — *"ONE window, disarmed at B4 before B5 whatever B3 produced"* — is discharged. Because `permit_join_duration` carries **no schema default** and an absent key opens nothing (`openPermitJoinWindow()` returns immediately, F-4), the card cannot re-open a join window on any future boot. The pre-window copy of `zigbee.yaml` remains preserved under `/root/`; nothing was deleted.

**★ THE CONFIG EDIT INTRODUCED NO SCHEMA COMPLAINT — and this is the one moment in the session that could have produced one.** `Configuration issue` counted **0** at B1 (pre-edit) and **0** again here (post-edit, post-delete), so PKG-SEC-2's pre-Phase-1 schema composition accepted the key's insertion *and* its removal cleanly. **The packet's decision to re-count that token in the disarm block is correct instrument design and should be kept** — it is the only place the write-then-remove cycle is checked against the schema on live bytes.

## §7 B5 — the restore


**⏺ filed 2026-09-13T14:58:40Z**

### B5 block 1 — the clean stop, GRADED (operator paste-back, verbatim) · ★ O-2 CLOSED ★

```
nick@hs-fresh:~ $ sudo systemctl stop homesynapse.service; sleep 2; systemctl show -p Result -p ActiveState -p ExecMainStatus homesynapse.service
Result=success
ExecMainStatus=143
ActiveState=inactive
```

**Verdict: MET — and it answers an R-4b ask that has been open across three artifacts.**

# ★★ O-2 IS CLOSED ON THE WIRE — R-4b's ASK #8, ANSWERED ★★

| artifact | a clean operator stop grades | |
|---|---|---|
| `g7c57d7f` (R-4) | `Result=exit-code · ActiveState=failed · ExecMainStatus=143` | O-2 open |
| `gef02d13` (R-4b) | `Result=exit-code · ActiveState=failed · ExecMainStatus=143` | O-2 open, **confirmed across two** |
| **`a458a64` (R-4c, today)** | **`Result=success · ActiveState=inactive · ExecMainStatus=143`** | **★ O-2 CLOSED** |

R-4b's ask #8 reads: *"O-2 remains OPEN and is now confirmed across two artifacts … a clean operator stop grades `Result=exit-code · ActiveState=failed · ExecMainStatus=143`. The FAILCHAN stop-proof is still owed."* **It is owed no longer.**

**Read the numbers precisely — what changed is the GRADE, not the exit code.** `ExecMainStatus=143` is identical across all three and is **correct**: 143 = 128+15 = SIGTERM, the right exit for a service stopped by the operator. What changed is systemd's *verdict* on that exit — `Result` flipped `exit-code` → `success` and `ActiveState` flipped `failed` → `inactive`. **The unit now knows 143 is a clean stop.** That is precisely the FAILCHAN boundary the artifact's own `Main` javadoc describes (*"a SIGTERM that lands mid-bootstrap makes `main` return and the JVM's 143 is the clean exit"*), demonstrated on live silicon rather than in CI — which matters, because R-4b recorded the FAILCHAN stop-proof's CI as RED on `HeroLoopHardwareFreeIT`.

**★ THIS EVIDENCE EXISTS ONLY BECAUSE D-11 SPLIT THE BLOCK.** The packet ships the grade read and `sudo shutdown -h now` in a single paste. Had it run as written and the shutdown raced the read — the exact failure R-4b's D-13 documented — the ssh session carrying this output would have dropped and **O-2 would have remained open by default rather than by evidence**, with no second chance in this session. **R-4b's D-13 earned its keep nine days after it was written, on a packet that had inherited the defect it warned about.** This is the strongest single argument in the record for the pre-LIVE ledger grep asked for in §9.


**⏺ filed 2026-09-13T15:01:16Z**

### B5 block 2 — the halt and the physical restore (operator paste-back, verbatim)

```
nick@hs-fresh:~ $ sudo shutdown -h now
nick@hs-fresh:~ $ Read from remote host 192.168.1.80: Connection reset by peer
Connection to 192.168.1.80 closed.
client_loop: send disconnect: Connection reset by peer
```

**Verdict: MET.** The `Connection reset by peer` IS the halt — the card went down under `shutdown -h now` after a **graded clean stop** (`Result=success`), not under a yank. Operator confirms: **held card OUT, bench card IN, power ON.** The coordinator dongle was not removed at any point in the session.

**Session physical acts, for the record:** bench card OUT / held card IN at ~`13:5xZ` (B0) → held card OUT / bench card IN at ~`14:59Z` (B5). One swap each way, one dongle, never unseated.


**⏺ filed 2026-09-13T15:06:30Z**

### B5 block 3 — THE BENCH FLOOR (operator paste-back, key lines verbatim) · ★ STOP-GATE R4c-4 MET ★

```
  [!!] NOT running
  [OK] launched pid 2167 -> /home/homesynapse/hs-bench/bench-2026-09-13-110127.log
  [--] waiting for a decisive radio state (up to 90 s)...
  [OK] RADIO UP after 23s
  [OK] running (pid 2167)
11:01:41.638 … registry.projection_live: devices=6 entities=6 position=25065
11:01:49.977 … zigbee.network_resumed: channel=20 panId=0x774c
--- failure tokens ---   (EMPTY on every read)

runner B3.1-2026-08-02-postwindow @ 16e672d
  [--] stimulus bench: restart → [OK] stopped → [OK] launched pid 2345 → [OK] RADIO UP after 13s
    [ok] log 'registry.projection_live: devices=6 entities=6' min=25065 — 11:02:47.511 … position=25065 (within 90s)
    [ok] log 'zigbee.adoption_maps_rehydrated: devices=6' — 11:02:47.920 (within 90s)
    [ok] log 'zigbee.device_relinked' x2(at-least) — 11:02:47.918 … 0x00178801101A09BB (within 90s)
    [ok] log 'zigbee.network_resumed: channel=20 panId=0x774c' — 11:02:55.763 (within 90s)
    [ok] log 'zigbee.port_identity_captured:' same-line ['pinnedOnly=false'] — 11:02:55.648 … stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false (within 90s)
    [ok] api /api/v1/entities {"rows": 6, "ulids": ["01KX1PA4HSJ581GASYB7DHE40F", "01KX1PB9AAB4VB3E10BD477TV3", "01KXW0157SP56CCSGJCNDCSQNG", "01KXW13WF0D6TYGN13WXHTG87K", "01KXW1W1SBJZERC9MBAMV2DWKE", "01KY12MQW954E4XYNKH0Y5H8VX"]} — all asserts satisfied (within 90s)
[PASS] boot-health — 6/6 positive · 0 forbidden
  [--] bundle: /home/homesynapse/hs-bench/bundles/boot-health-20260913T150256Z
11:02:55.648 … zigbee.port_identity_captured: stableId=…usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false
11:02:55.763 … zigbee.network_resumed: channel=20 panId=0x774c
```

# ★ STOP-GATE R4c-4 — MET. THE BENCH FLOOR IS GREEN AND THE NIGHTLY WILL FIRE ON AN UNDISTURBED RIG. ★
`NOT running` → started (pid 2167) → **RADIO UP after 23 s** → `running` ✓ · **`[PASS] boot-health — 6/6 positive · 0 forbidden`** ✓ · **`network_resumed: channel=20 panId=0x774c` — PAN UNCHANGED** ✓ · failure-token section **EMPTY on every read** ✓ · bundle `boot-health-20260913T150256Z`. **The one STOP condition remaining in the session did not occur.**

**★ THE DONGLE FENCE HELD, AND IS PROVEN BYTE-FOR-BYTE ACROSS TWO SESSIONS.** `stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_**0ae2dd7cecf8ef11b80168135c2a50c9**-if00-port0` is **identical to the value R-4b recorded on 2026-09-04**, on both cards. Two sessions, four card swaps, one physical radio, never unseated. **The held card's and the bench card's identical channel-20 / PAN-`0x774c` resumes are therefore the same network, not a coincidence of configuration** — which is what licenses comparing today's held-card measurements against the bench's fleet at all.

**★ THE BENCH REGISTRY IS BYTE-STABLE ACROSS NINE DAYS AND THREE READS.** `registry.projection_live: devices=6 entities=6 **position=25065**` — the same position integer at R-4b (2026-09-04), at this session's B0 (`04:31:59` EDT), and at the restore (`11:02:47` EDT). The six entity ULIDs returned by the scenario's own API assert are **identical to the list in R-4b's §9-RESTORE**. Nine days, nine nightlies, one held-card session: the bench projection has not advanced a position.

**★ F-R4-2 MADE PRECISE — one physical device, two registries, two different ULIDs.** The bench card relinks `0xF044D3FFFED2A201` as deviceId **`01KXW0156Z1GJ3WCV2G516AKWS`**. The held card adopted that **same physical SNZB-02P** today and minted its own deviceId **`01M2DKJWVDDHRF8ZX9HQ5B94KX`**. **The divergent-registry finding is no longer a count mismatch — it is a concrete identity collision: the same silicon carries two different ULIDs depending on which card is in the slot.** The divergence also narrowed today: **bench 6 devices / 6 entities vs held 4 / 4** (was 6-vs-3 at R-4b). Any future design that assumes a device ULID is stable across cards is wrong, and this is the evidence.

## §8 STOPs (none expected; each one whole if reached)

## §9 Deviations ledger (D-n · tier · block · Z time · what · fix) + THE FINDINGS CARD FOR THE HUB


**⏺ filed 2026-09-13T14:02:32Z**

**Ledger format:** one line each; **the full reasoning, evidence and recommendations for every entry live in `context/audits/2026-09-13_R-4c_preflight_source-audit.md`** (§ *Deviations ledger — long form*), split out to keep this record inside the packet's `≤ ~30 KB` close-out cap. Nothing was summarised away.

| # | tier | block | Z | what | fix |
|---|---|---|---|---|---|
| **D-1** | T1 instrument | §0/§1 | 13:4x | §0/§1 assume a signed-in browser; GitHub's step logs are auth-gated (`Not Found` to a signed-out session) while run pages, job verdicts and artifact digests are not | §0 read anonymously by the navigator; §1's echo line left to the operator. **Rec: §0 can be lifted off the operator entirely.** |
| **D-2** | T1 instrument | §1 fetch | 13:5x | **the fetch block has no freshness guard and fails SILENTLY** — a stale same-named zip in `~/Downloads` passes `count = 1` and a valid 64-hex hash. Fired for real: `gef02d13`, R-4b's artifact, nine days old | newest-by-mtime selection, clean expand dir, **identity printed before the hash**; stale tree moved aside not deleted. **Rec: packet-class defect across R-3/R-4/R-4b/R-4c/H8-a.** |
| **D-3** | T1 substitution ★ | §1 | 13:5x | the packet binds the .deb to CI via an auth-gated log line and a 64-hex human diff — the weakest link in the chain meant to prevent D-2 | **THE ANONYMOUS ORIGIN GATE:** GitHub's published artifact digest `883c5f8d…` matched the downloaded zip exactly. Binds the whole archive, no credentials, catches a stale download *before* expansion. **Rec: adopt as the standing §1 gate.** |
| **D-4** | T1 housekeeping | §9 | 13:5x | the pre-flight source audit (11 KB) would have consumed the record's cap before B0 | relocated verbatim to the companion audit file; this ledger points to it |
| **D-5** | T1 instrument | B0 blk 3 | 13:5x | **R-4b's D-2, inherited unfixed**: `dpkg-query -W -f "${Version}\n"` inside a single-quoted ssh arg → the remote shell eats `${Version}` → bare newline | `dpkg-query -W homesynapse`. **PROVEN at 13:58:21Z vs 13:58:30Z** — both blocks run 9 s apart, blank vs correct, all else identical. **Navigator error also recorded:** handed the known-broken block verbatim first, corrected a minute later. |
| **D-6** | T1 instrument | B0 blk 3 | 14:0x | the config-tree `ls` is **not `sudo`'d** while every other read of that root-only tree in the same block is → `Permission denied` ×2; the EXPECTED line was unsatisfiable as written. Packet also **dropped R-4b's `date "+%Z %z"` TZ calibration**, which R-4b added because every timestamp correlation depends on it | read-only re-read with `sudo ls -la`, explicit `date "+%Z %z"`, and the card's `zigbee.yaml` read **before** the window so B3's census is validated against the file (the packet's own T1 clause, applied in advance) |
| **D-7** | T1 grading | B1 blk 2 | 14:1x | **the integrity gate's EXPECTED asserts `ROWS-pre = ROWS-A`, but the service is RUNNING and the fleet is reporting — equality is the UNHEALTHY outcome.** Read `228` vs `219`: +9 rows over ~14.5 min = **0.621 rows/min**, against R-4b's independently measured **0.643 rows/min** on the same fleet nine days earlier | graded against **STOP-GATE R4c-2's own words — "zero row loss · integrity ok"** — which is what the gate exists to test and is MET. The packet contradicts itself: this block says `=` while B1 block 3 says `ROWS ≥ pre` for the very same counter, twenty lines apart. **Rec: the gate's EXPECTED should read `ROWS-pre ≥ ROWS-A`; as written it would have the operator STOP on a healthy card, and a flat count between B0 and B1 is the reading that should actually raise an eyebrow.** |
| **D-8** | T1 operator-safety | B3 blk 0b | 14:2x | **the packet orders "press the S31's button once ON and once OFF" with NO load check.** R-4b restored the rig with Nick's laptop charger plugged into that S31 (relay off), so the provocation cycles mains power to whatever is plugged in — and R-4b's own P-1 finding states the rule in as many words: *"never harness a load that must not lose power"*, with R-4b's navigator asking the operator before the first press. This packet inherited the act and dropped the check | the navigator asked before B3 was handed over: unplug anything that must not lose power, or skip provocation 5 — **the S31 is already one of the card's three known devices and is NOT load-bearing for C-003**, so skipping it costs nothing this session. **Rec: any packet instructing a relay cycle must name the load check in the block, not leave it to the navigator's memory of a prior record; P-1's `maxCyclesPerWindow` / load-limit clauses should land as packet grammar, not only as harness code.** |
| **D-9** | T1 grading ★ | B2 blk 1 | 14:2x | **the packet's B2 names a specific expected witness — "the Hue's entity from R-4, absent from the air" — that DOES NOT EXIST on this card.** R-4b §0 C4 records *"PATH TAKEN: B (no light entity existed; the Hue never answered)"*: the held card has no light entity, and an adopted device with no registered entity is not a row in `/api/v1/entities`. Read: `rows=3 · null: 0`. Strict grading would file "LASTREPORTED-1b MISS" | graded as **instant arm PROVEN / null arm NOT TESTED** (see §4). The expectation was inherited from R-4 and never re-derived against R-4b's own finding about this machine's entity set — same root cause as D-1/D-2/D-5/D-6, but where those cost minutes, **this one would have cost a wrong scientific conclusion banked by the hub.** **Rec: a named expected witness must be re-derived against the latest record of that machine's state; a witness that has ceased to exist turns a working mechanism into a recorded failure.** |
| **D-10** | T1 grading ★★ | B4 blk 1 | 14:5x | **the packet's read-2 diff CANNOT test LASTREPORTED-1b's null arm and manufactures a false positive for it.** A NEW row's "before" value is `(a.get(k) or {}).get('lastReported')` against read 1, where the row does not exist — so it prints `None` **by construction, whatever the API held**. Today's new SNZB-02P entity printed `None -> 14:50:28.702Z` and a loose grade would file "null arm PROVEN" **from a KeyError default** | graded **NOT TESTED**, with the substance corroborated separately: registration `14:43:48.783Z` → first instant `14:50:28.702Z` = **399.9 s gap**, so the instant is neither adoption-time nor boot-time and adoption fabricated nothing. **Rec: the null arm requires a read BETWEEN registration and first report — a short poll on /api/v1/entities from the arm, or a re-read triggered on `device_adopted`. A 6.7-minute observable window existed today; only the instrument was missing.** |
| **D-11** | T1 instrument | B5 blk 1 | 14:5x | **R-4b's D-13, inherited unfixed — the SEVENTH inherited defect.** B5 puts the stop-GRADE read and `sudo shutdown -h now` in ONE block. R-4b hit this, split it, and wrote the reason into its record: *"if the shutdown races the read, ssh drops and the O-2 evidence is lost for the session… a gate that shares a block with the act it gates WILL be overrun."* The grade is **O-2 evidence**: R-4b measured a clean operator stop as `Result=exit-code · ActiveState=failed · ExecMainStatus=143` across TWO artifacts; this packet predicts `Result=success · inactive · 143` on `a458a64`. A raced read loses the only test of whether FAILCHAN fixed it | **split into two blocks** — the grade alone, then the shutdown. Nothing measured changed. **Rec: this is the second of R-4b's five named instrument defects to be inherited verbatim (D-5 was the first). The pre-LIVE ledger grep (§9) would have caught both.** |

### ★ THE ROOT CAUSE BEHIND D-1, D-2, D-5 AND D-6 — one line, and it is the packet-authoring lesson
**Four of six deviations are the same failure: this packet was cut from the R-4b record but never re-derived against that record's own deviations ledger.** R-4b's findings card §5(a) says it in those words — *"re-derive paths against the prior record's own deviations"* — and R-4b's ask #5 asked the hub to correct five named instrument defects. D-5 is one of those five, inherited verbatim and reproduced on the wire today. D-6 is its sibling (same config tree, permission instead of path) plus the deliberate loss of the calibration R-4b added in the same fix.
**The mechanical remedy is cheap and checkable: before a packet goes LIVE, grep the prior record's deviations ledger for every command string the new packet reuses.** Four of today's six deviations would not exist. Recommend the hub make it a pre-LIVE gate on packet authorship, not a lesson.



**⏺ filed 2026-09-13T14:54:57Z**

---

# ★ THE FINDINGS CARD FOR THE HUB — R-4c, Sunday 2026-09-13
*(Written against §H's own intake list, item by item, so the hub banks conclusions rather than deriving them. Every claim below is anchored to a ⏺ in §1–§7 of this record; the instrument analysis behind them is in the companion audit.)*

## 1 · C-003 — **MINT IT.** The ZDO surface is proven on silicon, on the exact device that defeated R-4b.
`lookup_eui64_failed: nwk=0x15ac status=0x1` → `ieee_addr_req: nwk=0x15ac` (**+0.329 ms**) → `ieee_addr_rsp: nwk=0x15ac device=0xF044D3FFFED2A201` (**+515.796 ms, on the air**) → `rejoin_candidate … source=unknown_sender` → *(72.43 s)* → `rejoin_candidate … source=tc_join` → `device_proposed … model=SNZB-02P status=COMPLETE source=rejoin` → **`device_adopted: device=0xF044D3FFFED2A201 deviceId=01M2DKJWVDDHRF8ZX9HQ5B94KX entities=1`**, at **+122.06 s** into a 254 s window. Census: that IEEE `adopted_this_invocation=1`, **every other device 0**. `network_formed` **0** throughout.
**The controlled comparison is the point: same device, same `nwk=0x15ac`, same `status=0x1` as R-4b's miss, nine days apart, one variable changed — F-R4-1b's second surface.** R-4b's **F-R4b-F is retired**: the silent-rejoiner gap is no longer "mains routers only". **F-R4-1b → LIVE-VERIFIED**, and the fence on B-2/B-3 design lifts on this mint.

## 2 · ★ F-R4c-A — **RESOLUTION IS NOT ADOPTION.** A bound the hub must apply before designing on top of C-003.
The **SNZB-01P `0xF044D3FFFE1C1E8E`** was resolved over the air in the same window — `lookup_eui64_failed: nwk=0xa5da status=0x1` → `ieee_addr_req` → `ieee_addr_rsp … device=0xF044D3FFFE1C1E8E` (**265.036 ms**) → `rejoin_candidate … source=unknown_sender` — **and then produced no further line of any kind.** No `tc_join`, no proposal, no adoption, **and no error**: zero `rejoin_candidate_unresolved`, zero `proposal_incomplete`, zero `ieee_addr_rsp_failed` across the whole invocation. It is not a failure path; it is a path that ends.
**The discriminator is explicit in the log:** the device that adopted emitted a **second** candidate line carrying **`source=tc_join`**, and adopted 1.10 s later. The device that did not adopt never emitted one.
**Hypothesis, recorded as such because this session did not test it:** ZDO resolution *identifies* an unknown sender and admits it as a **candidate**; **adoption additionally requires the device to complete a real Trust Center join**, which is what makes the interview possible. Warming the SNZB-02P drove a genuine rejoin; a short press on the SNZB-01P sent a frame that was resolved but never triggered one.
**One-line experiment to settle it next session: provoke the SNZB-01P to REJOIN (battery pull-and-reinsert inside an open window) rather than to report, and look for `source=tc_join`. Prediction: it then adopts over the same ZDO path.**

## 3 · LASTREPORTED-1b — **BANK THE INSTANT ARM. DO NOT BANK THE NULL ARM.**
- **INSTANT ARM — PROVEN, and under a stronger test than the packet designed.** An entity that last spoke `2026-09-04T19:42:00Z` still carried **that** instant after nine days, a card power-cycle **and a version upgrade**, sitting beside `UNAVAILABLE` — not refreshed to boot, adoption, or now. A second entity's instant survived the upgrade and restart unchanged. Then the **SNZB-04P** was driven live, in one step, **`UNAVAILABLE` → `AVAILABLE`** and **`2026-09-04T19:42:00Z` → `14:45:07.132Z`** (in-window, +200.4 s). Nothing anywhere moved instant → null.
- **NULL ARM — NOT TESTED. Twice over, for two different reasons.** (a) **D-9:** the packet's named witness — *"the Hue's entity from R-4"* — **does not exist**; R-4b §0 records `PATH TAKEN: B (no light entity existed)`, and today's `device_relinked` lines confirm the Hue is not even in the held card's registry. (b) **D-10:** the read-2 diff prints `None` for any NEW row **by construction** (the row is absent from read 1), so today's `None -> 14:50:28.702Z` on the new SNZB-02P entity is a **KeyError default, not an observed null.** A loose grade would have filed "null arm PROVEN" from it.
- **What IS corroborated without the literal observation:** the new entity was registered at `14:43:48.783Z` and its first instant is `14:50:28.702Z` — a **399.9 s gap**. The instant is neither adoption-time nor boot-time, so **adoption fabricated nothing.** That is the null arm's *substance*, established by the gap. **Record it as corroboration, not as a pass.**

## 4 · `card-gradle: absent` — the owed line, answered. **The held card is run-only.**
No Gradle, no `gradlew` under `~/homesynapse-core` or `/opt/homesynapse`, and `which gradle java` silent (the service runs a jlink'd image, so no `java` on the operator PATH). **TR-1b's driver must assume cross-build-and-ship, not on-card build** — any driver step wanting a Gradle verb runs on the desk or in CI and delivers an artifact, exactly as this session's .deb path did.

## 5 · ★ F-R4b-G — **the Hue is absent from the air on a FOURTH attempt, and this one removes the last excuse.**
The operator powered the Hue lamp on for ~1 minute **inside the open permit-join window** and off again. The coordinator saw **nothing**: `lookups=2` for the whole window, both accounted for (`0x15ac`, `0xa5da`); no third nwk, no third lookup, no `rejoin_ignored_window_closed`. **This is the first attempt made with the door OPEN and a second resolution surface live** — conditions strictly better than R-4b's three. Recorded, not judged, per the packet. **R-4b's ask #4 (playbook §6 "wall power-cycle ⇒ re-announce": VERIFIED → CONTESTED) should now be settled.**

## 6 · THE FLEET SENTENCE — the census of six, and the registry moved 3 → 4
Held card, this invocation: **`0xF044D3FFFED2A201` adopted (1); all five others 0; all six `in_adopt_list=1`.** Entity rows **3 → 4**. Known before: S31 `0x00124B002FA8D1C5`, SNZB-03P `0xF044D3FFFE9C78D7`, SNZB-04P `0x449FDAFFFE688F57`. Still unknown after: **SNZB-01P `0xF044D3FFFE1C1E8E` (resolved, not adopted — §2 above)** and **Hue `0x00178801101A09BB` (absent from the air)**. **F-R4-2 (divergent held/bench registries) re-measured: bench 6, held now 4.** The bench registry is byte-stable across nine days — all six `device_relinked` IEEE→deviceId pairs and `position=25065` identical to R-4b's 09-04 read.

## 7 · THE ARTIFACT AND ITS CUSTODY — re-derivable without an auth-gated log
`homesynapse_0.1.0+git20260913.113754.ga458a64_arm64.deb` · sha256 **`1f46c5c864fe03c261a2c0a15752ac0b4b91c732646fec90e2f572f9aef7eed1`** · install-smoke **run #53** `https://github.com/nexsys-io/homesynapse-core/actions/runs/34754940902` · commit `a458a64` · amd64 **green** arm64 **green**. **Four-surface chain, no human hash comparison:** GitHub's published artifact digest `883c5f8d…` ≡ downloaded zip ≡ (expansion) desktop .deb `1f46c5c8…` ≡ card .deb. Install `14:17:05Z→14:17:20Z`, ordinary upgrade, version exact on both surfaces, integrity `ok`, **zero row loss** across the whole session (ROWS-A 219 → 228 → 230 → …).

## 8 · `H8A: not run` — settled on the wire, from two directions
The incumbent read `0.1.0+git20260903.124041.gef02d13` on **both** surfaces at B0 — the packet's own disambiguator for "H8-a did not install". Corroborated independently by `adoption_maps_rehydrated: devices=3` (unchanged since R-4b's close) and by `context/audits/2026-09-06_H8a_real-wire_operator-record.md` being a 4,533-byte scaffold with no ⏺ under any heading. **The held card carried R-4b's artifact untouched from 2026-09-04 until this session.**

## 9 · ★ THE PACKET-AUTHORING FINDING — ELEVEN deviations, and SIX share ONE root cause
**D-2, D-5, D-6, D-8, D-9 and D-11 — six of eleven — all trace to the same failure: this packet was cut from the R-4b record but never re-derived against that record's own deviations ledger.** R-4b's findings card §5(a) states the remedy in those words — *"re-derive paths against the prior record's own deviations"* — and R-4b's ask #5 asked the hub to correct five named instrument defects. **TWO of those five — D-5 (R-4b's D-2, the nested-quote `dpkg-query`) and D-11 (R-4b's D-13, the stop-grade sharing a block with the shutdown) — were inherited VERBATIM. D-5 reproduced on the wire today at 13:58:21Z; D-11 would have cost the O-2 result entirely (§11). D-6 is R-4b's D-3 sibling plus the deliberate loss of the `date "+%Z %z"` calibration R-4b added in the same fix; D-8 drops R-4b's own P-1 load-check; D-9 inherits a witness from R-4 that R-4b had already recorded as non-existent; D-2 is the whole packet family's missing freshness guard.**
Severity is not uniform, and that is the important part: **D-1/D-5/D-6/D-7 cost minutes. D-2 nearly installed a nine-day-old artifact — every assertion in its block passed on the wrong bytes. D-9 and D-10 would each have banked a WRONG SCIENTIFIC CONCLUSION** (a working mechanism filed as a failure; a KeyError default filed as a proof).
**THE ASK — make it a pre-LIVE gate on packet authorship, not another lesson: before a packet goes LIVE, grep the prior record's deviations ledger for every command string and every named witness the new packet reuses.** Six of today's eleven would not exist.

## 10 · THE THREE THINGS THE NAVIGATOR WOULD CHANGE IN THIS PACKET
1. **Never strip a journal timestamp in a block whose output is evidence for a mint** (F-12, F-13). The packet's `sed 's/^.*INFO *//'` discards the window-open instant *and* the C-003 chain instants — together exactly the two quantities needed to say *"the device was admitted N seconds into the window and the air exchange took M milliseconds."* Both were restored additively today; without that, §1 and §2 of this card are unwriteable.
2. **Anchor a self-timing window block to `permit_join_opened`, not to `date` at loop start** (F-12). Measured offset today: **19.272 s** — the door closed at a *printed* elapsed of **234.7 s, not 254 s**, and the packet's own banner would have recorded the window as opening 19 s late. This is the unfinished half of R-4b's D-8.
3. **Assert what the block can actually observe.** Three EXPECTED lines were wrong on healthy bytes: `adopt_list_loaded 1` (it is `log.debug` under an INFO root — reads 0, F-1); `ROWS-pre = ROWS-A` (the service is running and ingesting — the same counter is asserted `≥` twenty lines later, D-7); and a null-arm test that cannot observe a null (D-10). **Add a pre-flight token-and-level read against the artifact's own source as a standing packet step** — it cost nothing at the desk today, ran while the operator was still at it, and pre-empted two rig mismatches on a healthy card (F-1 and F-9/D-5 both landed exactly as predicted).

## 11 · ★ O-2 IS CLOSED — an unplanned third headline, and R-4b's ask #8 answered
A clean operator stop on `a458a64` grades **`Result=success · ActiveState=inactive · ExecMainStatus=143`**. R-4 (`g7c57d7f`) and R-4b (`gef02d13`) both graded **`Result=exit-code · ActiveState=failed · ExecMainStatus=143`** — R-4b filed it as ask #8, *"confirmed across two artifacts … the FAILCHAN stop-proof is still owed."*
**What changed is the GRADE, not the exit code.** `143` (=128+15, SIGTERM) is identical and correct on all three; systemd's verdict on it flipped. **The unit now knows 143 is a clean stop** — the FAILCHAN boundary demonstrated on live silicon, which matters because R-4b recorded that proof's CI as RED on `HeroLoopHardwareFreeIT`.
**This evidence exists only because D-11 split the packet's block.** As shipped, the grade read and `sudo shutdown -h now` are one paste; a raced shutdown drops the ssh session carrying the output and **O-2 stays open by default rather than by evidence.** R-4b's D-13 warned about exactly this and was inherited unfixed. **ASK: close O-2 on this reading, and treat it as the strongest argument for the pre-LIVE ledger grep in §9.**

## 12 · ★ F-R4-2 MADE PRECISE — one physical device, two registries, TWO DIFFERENT ULIDs
The bench card relinks `0xF044D3FFFED2A201` as deviceId **`01KXW0156Z1GJ3WCV2G516AKWS`**. The held card adopted **that same physical SNZB-02P** today and minted **`01M2DKJWVDDHRF8ZX9HQ5B94KX`**. **F-R4-2 is no longer a count mismatch — it is a concrete identity collision: the same silicon carries different ULIDs depending on which card is in the slot.** The divergence narrowed today from 6-vs-3 to **bench 6/6 vs held 4/4**. **Any design that assumes a device ULID is stable across cards is wrong, and this is the evidence.** Relevant to R-5, to any fleet-merge story, and to anything that persists a deviceId outside the card that minted it.

## 13 · THE RIG IS PROVABLY UNDISTURBED — the comparison licence
- **Dongle `stableId` byte-identical to R-4b's**: `usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0`. Two sessions, four card swaps, one physical radio, never unseated. **This is what licenses comparing held-card measurements against the bench fleet at all.**
- **Bench registry byte-stable across nine days and three reads**: `devices=6 entities=6 position=25065` at R-4b, at today's B0, and at the restore; the six entity ULIDs identical to R-4b's §9 list.
- **PAN `0x774c` / channel 20 unchanged** on every one of the five service starts across both cards; **`network_formed` counted 0 on every one.**
- **Bench floor restored**: `[PASS] boot-health — 6/6 positive · 0 forbidden`, bundle `boot-health-20260913T150256Z`, failure tokens empty. **The nightly fires tonight on an undisturbed rig.**

## 14 · ASKS OF THE HUB
1. **Mint C-003** on the chain in §1. Word it on: artifact `a458a64`; `nwk=0x15ac`; the `516 ms` air exchange; `device_adopted … deviceId=01M2DKJWVDDHRF8ZX9HQ5B94KX entities=1` at +122.06 s. **Flip F-R4-1b → LIVE-VERIFIED and lift the B-2/B-3 design fence.**
2. **Rule on F-R4c-A (§2)** and charter the one-line rejoin experiment. **Do not let R-5 or the rehearsals assume resolution ⇒ onboarding.**
3. **Bank LASTREPORTED-1b as HALF-VERIFIED** — instant arm proven, null arm not tested. **Charter the null-arm instrument** (a poll between registration and first report; a 6.7-minute window existed today).
4. **Settle R-4b's ask #4** on the Hue with this fourth, door-open data point.
5. **Adopt the anonymous origin gate (D-3)** as the standing §1 for every artifact packet: GitHub's published artifact digest, read signed-out, hashed against the downloaded zip. It binds the whole archive, needs no credentials, and catches a stale download *before* expansion — where D-2's failure went undetected through `count = 1` and a valid 64-hex hash.
6. **Adopt the pre-LIVE ledger grep (§9)** as a gate on packet authorship.
7. **`card-gradle: absent` → TR-1b's charter** (§4).
8. **The anomaly count → OR-BUS-SILENT-DROP's row**, weighted: the boot zero is weak, the full-invocation zero (window, two ZDO exchanges, an adoption, an entity registration, four state reports) is the load-bearing one.
9. **Docket the 2026-09-12 bench regression** — `7/9 · FAIL command-confirm-s31 · ON-latency n/a(FAIL)`, self-recovered to `8/9 PASS` on 09-13, bundle preserved at `…/bundles/command-confirm-s31-20260912T083148Z`. On the S31 confirm path, i.e. the same path R-4b's C4 rode to `CONFIRMED`. A single self-recovering FAIL is the shape that gets forgotten.
10. **RECORD SIZE — a ruling is requested, as R-4b asked and did not receive.** The packet caps this record at `≤ ~30 KB` on the premise that "the ⏺s are counts and short chains today". The ⏺s *are* short; **the cap was consumed by ten deviations and thirteen pre-flight findings the packet did not budget for.** Navigability was solved instead of length: the instrument analysis was split into `context/audits/2026-09-13_R-4c_preflight_source-audit.md` at the moment it was written (D-4), and this record keeps every ⏺ verbatim plus a per-block verdict, with §0 and this card as the two screens the hub needs. **Both files are one return and must be intaken together.**

## §10 Hub verdict surface (the hub writes this at intake)

**Written by the v72 hub at intake, Sun 2026-09-13 ~10:3x CT (instrument 2026-09-13T15:34:09Z); the two-layer audit is `context/audits/2026-09-13_v72-b6_R-4c_intake_two-layer-audit.md`.**

| # | claim | ruling | the attack run |
|---|---|---|---|
| 1 | C-003 — the sleepy SNZB-02P adopted | **MINTED, BOUNDED** — adopted on the held card, +122.06 s into a 254 s window (`permit_join_opened` 14:41:46.727Z → `device_adopted` 14:43:48.783Z); the fleet's six all `in_adopt_list=1`. The ZDO surface's causal necessity for this adoption is UNTESTED: at source both `unknown_sender` and `tc_join` reach the same `admitRejoinCandidate` (the same `recordAnnounce` + `interviewQueue.schedule`), the proposal followed the `tc_join` by 1.04 s and did not follow the ZDO resolution in 72 s | §5.1 + the adapter read |
| 2 | F-R4-1b LIVE-VERIFIED; F-R4b-F retired | **MINTED as a resolver** (two on-air resolutions, 515.8 ms and 265.0 ms, against a 10 s deadline); F-R4b-F's "mains routers only" retired for RESOLUTION; adoption of a sleepy device still needs the device awake (claim 3) | §4.2 |
| 3 | F-R4c-A — resolution is not adoption | **MINTED as a finding; the explanation PROVISIONAL** — the 01P resolved and never proposed; source says the two admission paths are identical, so the difference is downstream (the interview completed only after the `tc_join`); the provocation control is contaminated (the operator's note) | §5.2 + the adapter read |
| 4 | O-2 closed | **PROVISIONALLY CLOSED** — one clean stop of one artifact against two failures on two artifacts; closes on the next rig restore grading `Result=success` again | §5.3 |
| 5 | LASTREPORTED-1b instant arm | **MINTED** — the 2026-09-04 instant survived nine days, a power-cycle and the upgrade un-refreshed; the SNZB-04P moved in-window | §4.5 |
| 6 | LASTREPORTED-1b null arm | **NOT BANKED** — read 2 ran after 14:50:28Z (its "after" value for the new row is that instant), so the 399.9 s null window was never sampled; the `None` is the diff script's default (D-10) | §4.6, checked hard |
| 7 | `bus.delivery_anomaly` 0 at "6.8× idle" | **BOUNDED, weakly** — 4.21 rows/min is three orders under the soak's rate; recorded in OR-BUS-SILENT-DROP as a rig-load zero, not counted as a sample | §5.4 |
| 8 | the Hue absent, fourth attempt | **RECORDED, NOT JUDGED** — the power event is operator-reported and uninstrumented; P-1's canonical live-leg target | §5.5 |
| 9 | F-R4-2 — one device, two registries, two ULIDs | **MINTED as an observation** (`01KXW0156Z…` bench vs `01M2DKJWVD…` held); the audit for persisted ids outside the minting card is a pre-R-5 task | §4.9 |
| 10 | six of eleven deviations, one root cause | **BOUNDED at four** — D-5 and D-11 verbatim inheritances; D-9 (a witness R-4b's own §0 says did not exist) and D-8 (R-4b's restore note) tied to the un-re-derived record; D-2 family-wide; D-6 an authoring miss of the same family, not an inheritance | §5.6 |

**§6 — the pre-LIVE gate: ADOPTED.** Minted in pm-lessons this beat (THE PRIOR-LEDGER GATE) and folded into `coding-instruction-format.md` at W-SKILLS-9: before any packet goes LIVE, grep the prior record's deviations ledger and its findings card's asks for every command string and every named witness the new packet reuses; each hit is fixed in the packet or carried as a named deviation. Why ask #5 produced no correction: the R-4c packet was authored (v70 beat 3) by range from R-4b's record — its blocks, not its ledger and asks; a return's asks had no home the next author was required to read. The gate gives them one. **Record size:** the cap is a ceiling on the record, not on the evidence — a companion file is the right split (D-4 stands as the form).

**Not banked, and why:** the null arm (no observation); O-2 (one reading); the causal role of the ZDO surface in the adoption (no counterfactual); the Hue's power event (uninstrumented); the "6.8×" as a bound on the soak class.
