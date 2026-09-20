<!-- file: context/audits/2026-09-19_R-5B_operator-record.md · purpose: the R-5 Part B operator record — every ⏺ verbatim, one section per block, the verdict surface first · audience: the hub (intake) · state-type: operator record · status: CLOSED — hub-audited v77 beat 6 (Sun 2026-09-20 ~10:1x CT); §10. Was: CLOSED-PENDING-HUB-AUDIT (navigator close-out 2026-09-19T19:00:15Z; Sunday's R5B-2: line is appended by the hub) · created by the H8-a/R-5B navigator 2026-09-19T17:43:51Z from the packet's §R skeleton; H8-a's record (context/audits/2026-09-06_H8a_real-wire_operator-record.md) carries §0→B5 of the same sitting -->
# R-5 Part B — operator record (Sat 2026-09-19; artifact 0.1.0+git20260914.115803.g6bd8508; held card hs-fresh; bench card hs-dev-1)

## §0 VERDICT SURFACE (written last, read first): the gates R5B-0..R5B-5 as counts · P-B1..P-B6 with the evidence line each will be graded on · O-2's two readings · the S31 count · the frame table (with the bound) · the deviations ledger (D-n) · ASKS OF THE HUB

# THE RESTORE MET · SIX GATES MET AS MEASUREMENTS · ZERO STOPS · THE FIRST `fleet:` DATUM · P-B2/P-B3/P-B6 NOT TESTED (the protocol was not run at the rig — D-3) · bench-hero LIVE ×4, CONFIRMED ×4
**Written 2026-09-19T19:00:00Z by the navigator. R-5B ran 17:43Z → 18:59Z after H8-a's 28 min (one sitting; H8-a's record carries §0→B5). Held card `hs-fresh` @ 192.168.1.80 on `0.1.0+git20260914.115803.g6bd8508` (H8-a's install); bench card `hs-dev-1` back at 18:48Z, floor `[PASS] boot-health — 6/6 positive · 0 forbidden`, PAN 0x774c, formed 0 on every read of the night.**

## THE GATES
| gate | verdict | on what |
|---|---|---|
| R5B-0 handover | **MET 8/8** | g6bd8508 ×2 · active · formed 0 · resumed 1 on 0x774c · no window key · TOKLEN-OK · ROWS-0 438 · rows 4 |
| R5B-1 the exit | **MET as a measurement** | opened line 13:48:17.641 local, 254 s · every counter 0 for 24 ticks · ARM 2 unconfirmed, ARM 1 NEVER PERFORMED (D-3) |
| R5B-2 harvest | **MET** | chain = 2 lines (tc_joins_enabled · permit_join_opened), no ZDO · census 0/1 ×6 · `NULL-ARM: not testable — no adoption this window` |
| R5B-3 | **MET** | frame table with its bound · `S31-CLUSTERS: no reading retained` · door closed 0 · 0 · active · 1 · rows 619 ≥ 438 |
| R5B-4 restore | **MET 5/5** | `[PASS] boot-health 6/6` · PAN unchanged · formed 0 · **re-seen 6 · adopted 0** · registry rows 6 byte-stable |
| R5B-5 close | **MET** | the digest line verbatim with `fleet: 6/6 · re-seen 0` · formed 0 |

## P-B1..P-B6 — the evidence line each is graded on (the hub adjudicates)
- **P-B1 line 1:** `2026-09-19 quiesced AUTO floor: 7/9 · FAIL usb-reenumeration · bundle /home/homesynapse/hs-bench/bundles/usb-reenumeration-20260919T185603Z · 1 SKIP(hue-online) · fleet: 6/6 · re-seen 0 · bench-hero RESTORED ✓ · ON-latency 0.08s` — the fleet clause MET; the floor's FAIL is an **environment fault** (`FileNotFoundError: 'uhubctl'` — the scenario came with the fa01cad pull; §7), not Core; `command-confirm-s31` PASSED. Line 2 = Sunday's 03:30 CT timer run (`R5B-2:`), which hits the same fault unless uhubctl is installed (ask 1).
- **P-B2: NOT TESTED.** 0 lookups · 0 ZDO · 0 candidates · 0 tc_join · 0 adoption · unknown_sender 0 across 254 s. The operator: "pressed and switched everything … No batteries were ever pulled." Neither confirmed nor refuted; the 01P either was not pressed or emitted nothing this coordinator saw.
- **P-B3: NOT TESTED** — no adoption; the poll (79 samples, D-4) instead recorded every device's instants sample-by-sample (§3).
- **P-B4: MET as pre-registered** — `relinked=6 adopted=0 announced=0`; registry rows=6, ids byte-identical to the boot-health assert.
- **P-B5: MEASURED under a hand-driven window (D-3), bound stated** — state_reported: SNZB-02P 23 · S31 4 · SNZB-03P 3 · SNZB-04P 0 (the untouched control); ZDO frames 0; `bus.delivery_anomaly` 0 at ~7 rows/min. Lower bound per frame class: attribute-report ≥ 23/4/3/0 (≥ 46/–/6/0 with the SNZB 2× twin multiplier). **Unplanned:** bench-hero fired 2× in-window and 4× tonight — trigger → 10.00 s delay → command → **confirmed in 77–228 ms, 4/4** (§4); the journal carries NONE of it at INFO (store-only).
- **P-B6: NOT ANSWERED** — no reporting_configured/device_proposed line for the S31 in 2 retained boots; relinked from the maps. F-R4b-C CARRIED without a second reading; `PLUG: two` stands as it was.

**O-2, two readings on 6bd8508:** H8-a B3 (17:35:02Z) and R-5B B4 (18:34:28Z), both `Result=success · ExecMainStatus=143 · ActiveState=inactive · SubState=dead · NRestarts=0` — with R-4c's on a458a64: three readings, two artifacts. **F-1 on BOTH stops** (H8-a's finding, repeated to the pattern): no `transport_closed_orderly`; `transport_failed: port dead or closed` 3 ms into the hook → watchdog `port_reopened` +1.7 s → JVM exit 60 ms later. **S31 count:** none retained. **S31-LABEL:** 15A 1800W — Input 120V @ 60Hz (H8-a B0-3).

**Deviations: 7 (D-1..D-7, §9) — 3 instrument (T1), 3 read-only probes (T2), 2 operator (D-2 the S31 fence; D-3 the protocol). STOPs: none (§8). ⏺ census: see the last line of §9.**

## ASKS OF THE HUB
1. **`uhubctl` on the bench card before Sunday 03:30 CT** — a rig change; the navigator did not install it. Without it P-B1's line 2 repeats `7/9 · FAIL usb-reenumeration`.
2. **Rule D-2 (the S31 switched by hand, the vacuum still plugged into it) and D-3 (the provocation protocol not executed)** — and whether the window is re-run in a next sitting with a ONE-device, three-acts, say-it-back choreography (the packet lesson in §9).
3. **F-1 ×2** — the FAILCHAN §10-O ordering defect (adapter read-loop stop vs. port close): a docket row.
4. **The journal is silent on automations at INFO** — explainability's journal trace is absent; the store is the only record (§4 B3-1b).
5. **The bench card's Core prints `deviceId=None`** (pre-CG-123) — its upgrade plan, now that the fence is lifted.
6. The record is ~45 KB: every ⏺ verbatim as the packet asked; no harvest.

## §1 B0 — the handover (paste-back verbatim)

⏺ B0 THE HANDOVER — filed 2026-09-19T17:45:00Z — MET · **STOP-GATE R5B-0 MET 8/8**: hs-fresh · 17:44:31Z · EDT -0400 · g6bd8508 on both surfaces · active · INV=a3c45da2… (H8-a B3-3's invocation, unchanged) · formed 0 · resumed 1 on channel=20 panId=0x774c (13:41:04 local) · **ROWS-0 = 438** (H8-a's ROWS-A 404, B3-3's 421) · window key 0 (door closed) · the 01P `0xF044D3FFFE1C1E8E` in the adopt list ×1 · TOKLEN-OK · entities 200/759 b · rows=4, every lastReported an instant (the S31's now 17:43:15.978Z and the SNZB-02P's 17:41:44.901Z — both LIVE since B3-3's restart; the two UNAVAILABLE rows still carry their 09-13 instants).
```text
hs-fresh
17:44:31Z
EDT -0400
homesynapse     0.1.0+git20260914.115803.g6bd8508
0.1.0+git20260914.115803.g6bd8508
active
INV=a3c45da2f9b34bcaaaa0feddae2adad6
0
1
Sep 19 13:41:04 hs-fresh homesynapse[1817]: 13:41:04.972 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
438
0
1
TOKLEN-OK
entities http=200 bytes=759
rows=4
   01M19RHWXYZYJMM26SX0E41HXN deviceId=01M19RHWWZXKD4MWM66KAW8MSR lastReported='2026-09-13T14:45:07.132090Z'
   01M19XN7NNQQ8S3JJF09T6YKKY deviceId=01M19XN7MXFBA3P5BT4VDY0BM6 lastReported='2026-09-13T14:44:31.278087Z'
   01M1PRQN03X8H4MNEZQ62F76F1 deviceId=01M1PRQMZHFV4SAWT1E96B9BQ2 lastReported='2026-09-19T17:43:15.978054Z'
   01M2DKJWVSJCHB6TTAJSW3D880 deviceId=01M2DKJWVDDHRF8ZX9HQ5B94KX lastReported='2026-09-19T17:41:44.901862Z'
```

## §2 B1 — the arm (1a · 1b · 1c, verbatim; the opened line; OPEN_UNIX; the first adopted=1 and tc_join=1 ticks)

⏺ B1-1a THE WINDOW KEY, GUARDED — filed 2026-09-19T17:46:07Z — MET (line 1 serial_port · line 2 `permit_join_duration: 254` · channel: 20 on line 3 · the six adopt IEEEs · count 1; the pre-window copy at /root/r5b-history/zigbee.yaml.pre-window). The file is the truth for every IEEE below — the six match B2's census list.
```text
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

⏺ B1-1b THE POLL — filed 2026-09-19T17:47:23Z — MET (TOKLEN-OK · POLL pid=2023 · 10 lines after 6 s = two samples · first sample 17:46:40.580Z rows=4, four entity lines with lastReported RAW — all instants; the S31's advanced to 17:45:13.608Z since B0). The poll's 400 s run from 17:46:40Z.
```text
TOKLEN-OK
[1] 2023
POLL pid=2023
10 /home/nick/r5b/poll.log
17:46:40.580Z rows=4
17:46:40.580Z 01M19RHWXYZYJMM26SX0E41HXN deviceId=01M19RHWWZXKD4MWM66KAW8MSR lastReported='2026-09-13T14:45:07.132090Z'
17:46:40.580Z 01M19XN7NNQQ8S3JJF09T6YKKY deviceId=01M19XN7MXFBA3P5BT4VDY0BM6 lastReported='2026-09-13T14:44:31.278087Z'
17:46:40.580Z 01M1PRQN03X8H4MNEZQ62F76F1 deviceId=01M1PRQMZHFV4SAWT1E96B9BQ2 lastReported='2026-09-19T17:45:13.608209Z'
17:46:40.580Z 01M2DKJWVSJCHB6TTAJSW3D880 deviceId=01M2DKJWVDDHRF8ZX9HQ5B94KX lastReported='2026-09-19T17:41:44.901862Z'
```

⏺ B1-1c ARM — THE WINDOW — filed 2026-09-19T17:54:16Z — **the window opened as designed and the air was SILENT for all 24 ticks.** Opened line ×1 (`permit_join_opened: duration=254s` at 13:48:17.641 local, 30 ms after `network_resumed` channel=20 panId=0x774c) · formed 0 · OPEN_UNIX=1789840097.641299 · WINDOW OPEN 17:48:17Z · every counter ZERO on every tick, 29 s → 263 s: lookups=0 zdo_req=0 zdo_rsp=0 candidates=0 tc_join=0 device_join=0 adopted=0 unresolved=0 unknown_sender=0 · CLOSED 17:52:40Z. NEITHER of P-B2's pre-registered branches: no resolution after ARM 2 (R-4c's short press produced `lookup_eui64_failed → ieee_addr_req → ieee_addr_rsp` in 515 ms), no `tc_join`/`device_join` after ARM 1 — the coordinator logged no frame from the 01P at all. The operator's action notes (`ARM2 @s · ARM1 @s · null @s`) were NOT in the paste-back; asked for before B2 (filed beneath when they land). Also filed beneath: the operator's report of an out-of-packet act on the S31 BEFORE this window (D-2).
```text
INV=f268eb6fb79a43b0858a470a038aeeff
2026-09-19T13:48:17.611602-04:00 hs-fresh homesynapse[2112]: 13:48:17.611 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
2026-09-19T13:48:17.641299-04:00 hs-fresh homesynapse[2112]: 13:48:17.641 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.permit_join_opened: duration=254s
OPEN_UNIX=1789840097.641299
WINDOW OPEN at 17:48:17Z — 254 s. PROVOKE NOW in the order above.
 29s  lookups=0  zdo_req=0  zdo_rsp=0  candidates=0  tc_join=0  device_join=0  adopted=0  unresolved=0  unknown_sender=0
 39s  lookups=0  zdo_req=0  zdo_rsp=0  candidates=0  tc_join=0  device_join=0  adopted=0  unresolved=0  unknown_sender=0
 50s  lookups=0  zdo_req=0  zdo_rsp=0  candidates=0  tc_join=0  device_join=0  adopted=0  unresolved=0  unknown_sender=0
 60s … 253s  (all 24 ticks identical: every counter 0 — the operator's paste holds all 24 lines verbatim; ticks at 60,70,80,90,100,110,121,131,141,151,161,171,182,192,202,212,222,232,242,253 s)
263s  lookups=0  zdo_req=0  zdo_rsp=0  candidates=0  tc_join=0  device_join=0  adopted=0  unresolved=0  unknown_sender=0
WINDOW CLOSED at 17:52:40Z
```

⏺ B1-1c OPERATOR'S ACTION NOTES (asked twice; landed 2026-09-19T18:10:22Z) — verbatim: (1) "Yes, I pressed and switched everything — I wasn't sure what I was supposed to be provoking or doing. I just started going around to all devices and pressing them on or messing with them." (2) "No batteries were ever pulled." (3) "I do not know." (4) "I did not press any buttons to reset or pair any devices, or anything like that." READING FOR THE HUB: the pre-registered protocol was not executed — ARM 1 (the battery pull, the rejoin arm) never ran; ARM 2 (one short press of the 01P at ~+30 s) is unconfirmed inside a general "pressed everything"; the null-arm press is unknown. The window's silence on every counter therefore separates into: the 01P was never pressed, OR it was pressed and emitted nothing this coordinator saw. The journal alone cannot tell them apart; `ingestion_unknown_sender=0` says no frame from an unknown NWK address arrived at all. **P-B2 is NOT TESTED tonight** (neither confirmed nor refuted). The known devices' reports do not register on the tick counters — B2-2's diff and the poll's 80 samples are the record of what DID speak in the window. Filed as D-3.

## §3 B2 — the harvest (the chain with instants · the gaps · the census · the null arm)

⏺ B2-1 THE HARVEST — filed 2026-09-19T17:57:24Z — the chain holds TWO lines and nothing else: `tc_joins_enabled` (13:48:17.634 — the wildcard well-known transient link key installed, stack-bounded lifetime) and `permit_join_opened: duration=254s` (13:48:17.641). No lookup, no ZDO request or response, no candidate, no join, no announce, no proposal, no adoption, no interview token in the whole invocation. Gaps: one anchor line. Census: all six `adopted_this_invocation=0 · in_adopt_list=1`. The poll (pid 2023) reported `Done` — its 80 samples are complete in ~/r5b/poll.log. **The operator's action notes for ARM 2 / ARM 1 / the null arm are still not in hand — asked a second time; nothing further is handed until they land.**
```text
[1]+  Done                    nohup bash -c 'for i in $(seq 1 80); … done' > ~/r5b/poll.nohup 2>&1
2026-09-19T13:48:17.634107-04:00 INFO zigbee.tc_joins_enabled: join policy set; wildcard well-known transient link key installed (stack-bounded lifetime — expected to self-expire with the join window)
2026-09-19T13:48:17.641299-04:00 INFO zigbee.permit_join_opened: duration=254s
--- gaps (s)
1789840097.641299  +0.000 s since previous  permit_join_opened
--- census
0x00178801101A09BB  adopted_this_invocation=0  in_adopt_list=1
0xF044D3FFFE9C78D7  adopted_this_invocation=0  in_adopt_list=1
0x00124B002FA8D1C5  adopted_this_invocation=0  in_adopt_list=1
0xF044D3FFFED2A201  adopted_this_invocation=0  in_adopt_list=1
0xF044D3FFFE1C1E8E  adopted_this_invocation=0  in_adopt_list=1
0x449FDAFFFE688F57  adopted_this_invocation=0  in_adopt_list=1
```

⏺ B2-2 THE NULL ARM + THE SECOND READ — filed 2026-09-19T18:18:59Z — **`NULL-ARM: not testable — no adoption this window`** (ADOPTED empty · NEWID empty · 79 samples, every one rows=4 · entities-1 200/757 b · rows before=4 after=4 new=0). **P-B3 NOT TESTED.** The diff is the record of what DID speak: the SNZB-04P (front door, `01M19RHWXYZ…`) UNCHANGED at its 09-13 instant — the one device the operator did not disturb; the SNZB-03P (`01M19XN7NNQ…`) came back from its 09-13 instant to **17:53:05.985Z** (its first report in six days — 34 s AFTER the window closed at 17:52:31); the S31 17:43:15 → 18:08:15.986Z (the 5-min periodic at :15.98 s); the SNZB-02P 17:41:44 → 18:10:49.171Z. (The `grep "deviceId=$NEWID"` lines with NEWID empty match every poll line — the three printed are the first sample, not evidence; R-4c D-10's instrument had no adoption to read.) OPERATOR'S ANSWERS, verbatim, to the two questions asked with this block: (a) "I switched it, yes, just to see what happened (it turned off again after a few second, just like earlier with the vacuum that's stayed plugged into it)." (b) "The only device that was not powered on/off or provoked/disturbed was the 04P for my front door. I even turned on the lamp with the smart bulb, and warmed up then cooled down the temperature/humidity device." Filed under D-3. Two readings from (a)/(b) for the hub: the S31 switched itself OFF a few seconds after being switched ON, twice tonight (17:45 and in-window) — the shape of bench-hero (StateChangeTrigger on the S31 → DelayAction → CommandAction on the S31) firing; and the Hue LCA017 was powered on inside an OPEN window and the coordinator logged nothing (no announce, no lookup, unknown_sender=0) — R-4c's "fourth failure to reproduce" is now a fifth.
```text
ADOPTED: 
NEWID=
412
17:46:40.580Z 01M19RHWXYZYJMM26SX0E41HXN deviceId=01M19RHWWZXKD4MWM66KAW8MSR lastReported='2026-09-13T14:45:07.132090Z'
17:46:40.580Z 01M19XN7NNQQ8S3JJF09T6YKKY deviceId=01M19XN7MXFBA3P5BT4VDY0BM6 lastReported='2026-09-13T14:44:31.278087Z'
17:46:40.580Z 01M1PRQN03X8H4MNEZQ62F76F1 deviceId=01M1PRQMZHFV4SAWT1E96B9BQ2 lastReported='2026-09-19T17:45:13.608209Z'
--- first instant
17:46:40.580Z 01M19RHWXYZYJMM26SX0E41HXN deviceId=01M19RHWWZXKD4MWM66KAW8MSR lastReported='2026-09-13T14:45:07.132090Z'
17:46:40.580Z 01M19XN7NNQQ8S3JJF09T6YKKY deviceId=01M19XN7MXFBA3P5BT4VDY0BM6 lastReported='2026-09-13T14:44:31.278087Z'
--- the samples around adoption
     79 1:17:46:40.580Z rows=4
entities http=200 bytes=757
rows before=4 after=4 new=0
   01M19RHWXYZYJMM26SX0E41HXN deviceId=01M19RHWWZXKD4MWM66KAW8MSR lastReported '2026-09-13T14:45:07.132090Z' -> '2026-09-13T14:45:07.132090Z'
   01M19XN7NNQQ8S3JJF09T6YKKY deviceId=01M19XN7MXFBA3P5BT4VDY0BM6 lastReported '2026-09-13T14:44:31.278087Z' -> '2026-09-19T17:53:05.985593Z'
   01M1PRQN03X8H4MNEZQ62F76F1 deviceId=01M1PRQMZHFV4SAWT1E96B9BQ2 lastReported '2026-09-19T17:43:15.978054Z' -> '2026-09-19T18:08:15.986660Z'
   01M2DKJWVSJCHB6TTAJSW3D880 deviceId=01M2DKJWVDDHRF8ZX9HQ5B94KX lastReported '2026-09-19T17:41:44.901862Z' -> '2026-09-19T18:10:49.171676Z'
```

⏺ B2-2b THE POLL, SAMPLE BY SAMPLE (D-4, T2) — filed 2026-09-19T18:21:00Z — 79 samples, 17 non-sample lines (the restart gap). What reported INSIDE the window [17:48:17.6 → 17:52:31.6]: **SNZB-04P (01M19RHWXYZ…): nothing — one instant, the 09-13 one, all 79 samples** (the undisturbed control). **SNZB-03P (01M19XN7NNQ…): came back from six days of silence at 17:50:14.586Z — INSIDE the window** (then 17:51:16, 17:52:04, 17:53:05) — CORRECTION to B2-2's note above, which read only the diff's last instant and called it post-window. **S31 (01M1PRQN03X…): two ON/OFF pairs in-window — 17:50:22.532 → 17:50:32.676 (Δ 10.14 s) and 17:51:47.790 → 17:51:57.919 (Δ 10.13 s)** — the operator's "turned off again after a few seconds" is a 10.1 s interval, identical twice: the shape of bench-hero's DelayAction then CommandAction (the T2 read after B3-1 will name it). **SNZB-02P (01M2DKJWVSJ…): ~30 reports in-window at a ~5 s floor** (17:50:44 → 17:52:55 nearly every sample; earlier bursts 17:46:42–17:47:02 and 17:48:43–17:49:08) — the operator warming and cooling it. P-B5's per-device counts must be read against this: the window was driven by hand, not quiet.
```text
samples=79 non-sample lines=17 (the restart gap + errors)
01M19RHWXYZYJMM26SX0E41HXN
   first seen 17:46:40.580Z  lastReported='2026-09-13T14:45:07.132090Z'
01M19XN7NNQQ8S3JJF09T6YKKY
   first seen 17:46:40.580Z  lastReported='2026-09-13T14:44:31.278087Z'
   first seen 17:50:17.362Z  lastReported='2026-09-19T17:50:14.585899Z'
   first seen 17:51:17.799Z  lastReported='2026-09-19T17:51:16.118046Z'
   first seen 17:52:08.158Z  lastReported='2026-09-19T17:52:04.152683Z'
   first seen 17:53:08.629Z  lastReported='2026-09-19T17:53:05.985593Z'
01M1PRQN03X8H4MNEZQ62F76F1
   first seen 17:46:40.580Z  lastReported='2026-09-19T17:45:13.608209Z'
   first seen 17:50:27.428Z  lastReported='2026-09-19T17:50:22.531724Z'
   first seen 17:50:37.493Z  lastReported='2026-09-19T17:50:32.676414Z'
   first seen 17:51:48.011Z  lastReported='2026-09-19T17:51:47.789871Z'
   first seen 17:51:58.079Z  lastReported='2026-09-19T17:51:57.919359Z'
   first seen 17:53:18.708Z  lastReported='2026-09-19T17:53:15.982756Z'
01M2DKJWVSJCHB6TTAJSW3D880
   first seen 17:46:40.580Z  lastReported='2026-09-19T17:41:44.901862Z'
   first seen 17:46:45.617Z  lastReported='2026-09-19T17:46:42.449419Z'
   first seen 17:46:55.685Z  lastReported='2026-09-19T17:46:52.460728Z'
   first seen 17:47:05.768Z  lastReported='2026-09-19T17:47:02.471550Z'
   first seen 17:48:46.642Z  lastReported='2026-09-19T17:48:43.469146Z'
   first seen 17:48:56.722Z  lastReported='2026-09-19T17:48:53.468932Z'
   first seen 17:49:11.831Z  lastReported='2026-09-19T17:49:08.668901Z'
   first seen 17:50:47.561Z  lastReported='2026-09-19T17:50:44.464813Z'
   … 21 further distinct instants at ~5 s spacing, 17:50:49.508 → 17:52:30.344 (the operator's paste holds every line) …
   first seen 17:52:53.511Z  lastReported='2026-09-19T17:52:50.515968Z'
   first seen 17:52:58.549Z  lastReported='2026-09-19T17:52:55.553108Z'
   first seen 17:53:08.629Z  lastReported='2026-09-19T17:53:05.636161Z'
```

## §4 B3 — the frame table · the S31 re-read · the disarm

⏺ B3-1 THE FRAME-COUNT BLOCK — filed 2026-09-19T18:22:32Z — MET as a measurement (the bound stated in the block: a LOWER BOUND on frames; HEAD emits no per-frame token). Window [1789840097641299, 1789840351641299] µs. By event_type: state_reported 30 · state_changed 30 · automation_action_started 4 · automation_action_completed 4 · state_confirmed 2 · command_issued 2 · command_dispatched 2 · automation_triggered 2 · automation_completed 2 · availability_changed 1. By subject (state_reported): **SNZB-02P 23 · S31 4 · SNZB-03P 3 · SNZB-04P 0** — exactly the poll's in-window instants per device (B2-2b). Tokens: ingestion_unknown_sender=0 (the 01P never spoke) · publish_conflict 0 · ias_zone_enrolled 0 · reporting_configured 0 (no re-announce this invocation) · **bus.delivery_anomaly=0** across 30 reports + 2 automation runs in 254 s (a bound on OR-BUS-SILENT-DROP at ~7 rows/min, not a closure). **THE UNPLANNED RESULT: bench-hero FIRED TWICE inside the window** — `automation_triggered 2 → 4 actions (delay + command) → command_issued/dispatched 2 → state_confirmed 2 → automation_completed 2` — the two S31 ON→OFF pairs at 10.1 s (B2-2b) are the DelayAction then the CommandAction, and `state_confirmed=2` says the plug's own report confirmed both commands. The S31's cut-offs tonight are the hero loop, not the plug's protection. The 03P's `availability_changed 1` is its UNAVAILABLE→AVAILABLE at 17:50:14. P-B5 as pre-registered ("S31 0 with nothing switched", quiet SNZBs) is confounded by D-3; the per-device lower bound per frame class stands as: attribute-report ≥ 23/4/3/0 (≥ 46/–/6/0 with the SNZB 2× twin multiplier, M9.3), ZDO frames 0 (no ZDO token this invocation), default-response/ack uncounted at HEAD.
```text
window_us=[1789840097641299,1789840351641299]
state_reported|30
state_changed|30
automation_action_started|4
automation_action_completed|4
state_confirmed|2
command_issued|2
command_dispatched|2
automation_triggered|2
automation_completed|2
availability_changed|1
--- by subject (state_reported)
   01M2DKJWVSJCHB6TTAJSW3D880 ENTITY count=23
   01M1PRQN03X8H4MNEZQ62F76F1 ENTITY count=4
   01M19XN7NNQQ8S3JJF09T6YKKY ENTITY count=3
--- journal tokens this invocation
ingestion_unknown_sender=0
ingestion_publish_conflict=0
ias_zone_enrolled=0
reporting_configured=0
bus.delivery_anomaly=0
--- entityId -> deviceId (from entities-1.json)
   01M19RHWXYZYJMM26SX0E41HXN -> 01M19RHWWZXKD4MWM66KAW8MSR
   01M19XN7NNQQ8S3JJF09T6YKKY -> 01M19XN7MXFBA3P5BT4VDY0BM6
   01M1PRQN03X8H4MNEZQ62F76F1 -> 01M1PRQMZHFV4SAWT1E96B9BQ2
   01M2DKJWVSJCHB6TTAJSW3D880 -> 01M2DKJWVDDHRF8ZX9HQ5B94KX
```

⏺ B3-1b D-2/D-3 T2 READ (journal) — filed 2026-09-19T18:24:13Z — **EMPTY in both invocations**: no `automation_triggered` / `command_issued` / `state_confirmed` / `automation_completed` / `delay` token reaches the journal at INFO in f268eb6f… or a3c45da2…. The automation engine's firings live in the STORE only (B3-1's rows); the journal is silent about them. A datum in its own right for the hub (explainability's "why did it fire" has no journal trace at HEAD). One last read-only store query for the chain's instants follows (the third and final probe on this item).
```text
hs-fresh
--- this invocation f268eb6fb79a43b0858a470a038aeeff
--- previous invocation a3c45da2f9b34bcaaaa0feddae2adad6
```

⏺ B3-1c D-2/D-3 T2 READ (store) — filed 2026-09-19T18:25:24Z — **bench-hero fired FOUR times tonight, 4/4 confirmed**: 17:42:36.875 (the operator's first S31 ON, between H8-a's B4 and B5), 17:45:03.366 (the vacuum event), 17:50:22.577 and 17:51:47.798 (in-window). Every chain: `automation_triggered → action_started (delay) → +10.00 s action_completed → action_started (command) → command_issued → command_dispatched → automation_completed → state_confirmed` — the DelayAction 10.007 / 10.003 / 10.006 / 10.002 s; command_dispatched → state_confirmed **154 / 228 / 77 / 112 ms** (the plug's own report confirming the OFF). The automation subject is per-load (01A0BAC1C7… in a3c45da2, 01A0BAC861… in f268eb6f — R-4b §7-ii on the store's side); the command subject 01A06D8BD4… is constant (the S31 entity). The 03P's `availability_changed` at 17:50:14.584 sits 8 s before the first in-window trigger. This is the hero loop's whole explainability triad, live, four times, on the held card: why it fired (the S31's state change), what it did (delay 10 s, command OFF), did it confirm (yes, ≤228 ms). The S31's "cut-offs" are closed as bench-hero; nothing about the plug's protection was exercised.
```text
hs-fresh
17:42:36.875|automation_triggered|01A0BAC1C74DD1E9892DEAD03C008536
17:42:36.891|automation_action_started|01A0BAC1C74DD1E9892DEAD03C008536
17:42:46.898|automation_action_completed|01A0BAC1C74DD1E9892DEAD03C008536
17:42:46.902|automation_action_started|01A0BAC1C74DD1E9892DEAD03C008536
17:42:46.911|command_issued|01A06D8BD403EA224A55DFB984F399E1
17:42:46.913|automation_action_completed|01A0BAC1C74DD1E9892DEAD03C008536
17:42:46.918|command_dispatched|01A06D8BD403EA224A55DFB984F399E1
17:42:46.920|automation_completed|01A0BAC1C74DD1E9892DEAD03C008536
17:42:47.072|state_confirmed|01A06D8BD403EA224A55DFB984F399E1
17:45:03.366|automation_triggered|01A0BAC1C74DD1E9892DEAD03C008536
17:45:13.376|command_issued|01A06D8BD403EA224A55DFB984F399E1
17:45:13.383|command_dispatched|01A06D8BD403EA224A55DFB984F399E1
17:45:13.611|state_confirmed|01A06D8BD403EA224A55DFB984F399E1
17:50:14.584|availability_changed|01A053DA9EB5BDD191CA4F02746F4E7E
17:50:22.577|automation_triggered|01A0BAC8617D20DB8980445AFD234552
17:50:32.602|command_issued|01A06D8BD403EA224A55DFB984F399E1
17:50:32.605|command_dispatched|01A06D8BD403EA224A55DFB984F399E1
17:50:32.682|state_confirmed|01A06D8BD403EA224A55DFB984F399E1
17:51:47.798|automation_triggered|01A0BAC8617D20DB8980445AFD234552
17:51:57.807|command_issued|01A06D8BD403EA224A55DFB984F399E1
17:51:57.810|command_dispatched|01A06D8BD403EA224A55DFB984F399E1
17:51:57.922|state_confirmed|01A06D8BD403EA224A55DFB984F399E1
(the 17:45 / 17:50 / 17:51 chains' action_started/completed/automation_completed rows are in the operator's paste; the first chain is shown whole above)
```

⏺ B3-2 THE S31's INTERVIEW RE-READ — filed 2026-09-19T18:28:24Z — **`S31-CLUSTERS: no reading retained`** (a ⏺, never a stop; the S31 was not provoked to re-announce). boots retained = 2 (09-13's and tonight's); no `reporting_configured` / `reporting_reapply` / `device_proposed` line for 0x00124B002FA8D1C5 in either — the plug has not been interviewed on this card within journald's retention; F-R4b-C's `clusters=1 verified=0 degraded=1` (09-04, ef02d13) remains the only reading and lives in the R-4b record alone. This invocation: `device_relinked: device=0x00124B002FA8D1C5 deviceId=01M1PRQMZHFV4SAWT1E96B9BQ2` at 13:48:09.884 (rehydrated from the adoption maps, no interview). **P-B6 NOT ANSWERED tonight; F-R4b-C CARRIED without a second reading; `PLUG: two` stands as it was.** The block's S31-row filter (`'S31' | 'on_off' | 'switch'`) matched nothing — the entities JSON carries none of those tokens (D-5, T1, instrument; no measurement lost: the S31's row is `01M1PRQN03X8H4MNEZQ62F76F1 → deviceId 01M1PRQMZHFV4SAWT1E96B9BQ2`, joined by the relinked line's deviceId, and its full row is in entities-1.json).
```text
2
--- this invocation
Sep 19 13:48:09 hs-fresh homesynapse[2112]: 13:48:09.884 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0x00124B002FA8D1C5 deviceId=01M1PRQMZHFV4SAWT1E96B9BQ2 —
--- the S31's entity rows
```

⏺ B3-3 DISARM — filed 2026-09-19T18:30:11Z — MET 5/5 · **STOP-GATE R5B-3 MET** (the frame table ⏺'d with its bound · the S31 count ⏺'d as `no reading retained` · the door closed): key count 0 · opened/config-issue/formed 0 · active · resumed 1 · **ROWS-W = 619** ≥ ROWS-0 438 (zero row loss across two restarts; +181 rows tonight — the hand-driven window, four hero firings, the 02P's burst). The key is out; the pre-window copy stays at /root/r5b-history/zigbee.yaml.pre-window.
```text
0
0
active
1
619
```

⏺ B3-4 THE R-5B EVIDENCE HOME (D-6) — filed 2026-09-19T18:33:42Z — MET: five files at `context/audits/2026-09-19_R-5B_capture/` · Bearer 0 ×5 · NAVIGATOR CROSS-CHECK on the filed copies (same minute): hashes identical, Bearer 0 ×5, poll.log = 79 `rows=4` samples + 17 non-sample lines (one python JSONDecodeError traceback from the restart's dead API — the sample lost), poll.nohup = `nohup: ignoring input`, window-open.unix = `1789840097.641299`. No token value anywhere in the five.
```text
DESKTOP-SRK0P9D
entities-0.json 100%  759 · entities-1.json 100%  757 · poll.log 100%  40KB · poll.nohup 100%  22 · window-open.unix 100%  18
-rw-r--r-- 1 Nick 197121   759 Sep 19 13:32 entities-0.json
-rw-r--r-- 1 Nick 197121   757 Sep 19 13:32 entities-1.json
-rw-r--r-- 1 Nick 197121 40536 Sep 19 13:32 poll.log
-rw-r--r-- 1 Nick 197121    22 Sep 19 13:32 poll.nohup
-rw-r--r-- 1 Nick 197121    18 Sep 19 13:32 window-open.unix
393ac5d4f57a443d8d7c11ef51b37b05b661dcf431b88e6fa3934580cf0debc6  entities-0.json
068df1294df4f87e9325bfd3a85494f66f5ca2cf9b47ea0dc350988ba7cb62ee  entities-1.json
60bf88ecfb686d939394463a81ae387e3a55112e0e72eb4efe8d44edc4db14bb  poll.log
0ea7cf1d885ad4976e0150df9dce6ffc37f00cf7db07e24b2b2e886ad0493c46  poll.nohup
444c88dcc89c33bde81f64d5d3707028425ec2cb7de42dc8faf4c7728cd66d98  window-open.unix
Bearer: entities-0.json:0 · entities-1.json:0 · poll.log:0 · poll.nohup:0 · window-open.unix:0
```

## §5 B4 — the stop · THE GRADE (O-2's second reading) · the halt · the swap clock · S31-LABEL if read here

⏺ B4-1 THE ACT (one clean operator stop) — filed 2026-09-19T18:34:51Z — MET (18:34:28Z → 18:34:33Z; the stop returned in ≈2 s, as at H8-a's B3-1).
```text
hs-fresh
18:34:28Z
18:34:33Z
```

⏺ B4-2 THE READ — O-2's SECOND READING ON 6bd8508 — filed 2026-09-19T18:36:21Z — **MET: `Result=success · ActiveState=inactive · ExecMainStatus=143 · SubState=dead · NRestarts=0`.** Two clean grades on one artifact tonight (H8-a B3-2 at 17:35, this at 18:34) beside R-4c's one on a458a64 — three readings, two artifacts: the shape §H names for closing O-2. One T2 read follows before the halt: does H8-a's F-1 (no orderly transport close; watchdog reopen during the stop) repeat on this second stop?
```text
hs-fresh
Result=success
NRestarts=0
ExecMainStatus=143
ActiveState=inactive
SubState=dead
```

⏺ B4-2b F-1's SECOND OBSERVATION (T2 read) — filed 2026-09-19T18:37:47Z — **H8-a's F-1 REPEATS EXACTLY: 2 of 2 clean stops on 6bd8508.** `Stopping` 14:34:28.292 → `transport_failed: port dead or closed` 14:34:28.295 (3 ms after "Stopping Javalin", the link clean: `frm=4 ack=1 reTx=false retransmits=0 crcRejects=0 timeouts=0`) → `port_unhealthy: reopen scheduling started` → `port_reopened: recovery succeeded after 0 failed attempts` 14:34:30.005 (+1.71 s) → `HomeSynapseCore stopped (SIGTERM)` 14:34:30.065 (+60 ms) → `Deactivated successfully`. No `transport_closed_orderly`. The shutdown hook closes the serial port before the adapter's read loop is stopped, every time; the watchdog re-negotiates the NCP and the JVM exits on top of it; systemd grades it `success` because the exit code is 143. A deterministic ordering defect on FAILCHAN §10-O's path — for the hub, with H8-a B3-2/B3-2b.
```text
hs-fresh
2026-09-19T14:34:28.292006-04:00 hs-fresh systemd[1]: Stopping homesynapse.service - HomeSynapse Core — local-first smart-home engine...
2026-09-19T14:34:28.293839-04:00 INFO Stopping Javalin ...
2026-09-19T14:34:28.295220-04:00 WARN zigbee.transport_failed: serial read error: port dead or closed; lastFrame=DATA(frm=4, ack=1, reTx=false) retransmits=0 crcRejects=0 timeouts=0 — the watchdog o
2026-09-19T14:34:28.295304-04:00 WARN zigbee.port_unhealthy: cause=read-error; reopen scheduling started
2026-09-19T14:34:30.005503-04:00 INFO zigbee.port_reopened: recovery succeeded after 0 failed attempts
2026-09-19T14:34:30.065231-04:00 INFO HomeSynapseCore stopped: db=/var/lib/homesynapse/data/homesynapse-events.db (SIGTERM)
2026-09-19T14:34:30.071622-04:00 hs-fresh systemd[1]: homesynapse.service: Deactivated successfully.
```

⏺ B4-3 THE HALT — filed 2026-09-19T18:45:13Z — MET (hs-fresh · 18:41:46Z · "Connection to 192.168.1.80 closed by remote host"). The swap's clock notes (OFF · OUT · re-label · IN · dongle · ON) were not in the paste-back — asked for with B5; filed beneath when they land. The held card's session on 6bd8508 tonight: B0 17:17Z power-on → 18:41:46Z halt, five invocations (e7b2dea6 · d17e76a2 · a3c45da2 · f268eb6f · the disarm's), rows 404 → 619, zero loss, formed 0 throughout.
```text
hs-fresh
18:41:46Z
nick@hs-fresh:~ $ Connection to 192.168.1.80 closed by remote host.
Connection to 192.168.1.80 closed.
```

⏺ B4-3b THE SWAP CLOCK (operator's notes, landed 2026-09-19T18:52:47Z) — `OFF 13:45 · OUT 13:45 · re-labelled (hs-fresh — H8-a + R-5B DONE — 6bd8508) · IN 13:45 · dongle in place · ON 13:46` (CT; = 18:45/18:46Z). S31-LABEL was read at H8-a's B0-3 — not re-read here.

## §6 B5 — the restore and the split

⏺ B5 THE RESTORE + THE SPLIT — filed 2026-09-19T18:52:47Z — **MET · STOP-GATE R5B-4 MET 5/5: the bench card back · `[PASS] boot-health — 6/6 positive · 0 forbidden` · PAN 0x774c unchanged · formed=0 · the split read.** hs-dev-1 at 18:48:10Z (≈2 min after power-on) · `[!!] NOT running` → `bench.sh start` → RADIO UP after 25 s → running (pid 2173) → the boot-health scenario's own restart (pid 2350, RADIO UP after 13 s) → six asserts `[ok]` → bundle `boot-health-20260919T184941Z`. **P-B4: `relinked=6 adopted=0` — re-seen 6 · adopted 0, as pre-registered**; `announced=0 reporting_configured=0` (no device spoke at the boot; the S31 did not re-announce — no second-card reading of P-B6). Registry rows=6, the six bench-minted ids byte-identical to the boot-health assert's list (R-4c card §13 holds). Dongle stableId `usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0`, vendorId=10c4 productId=ea60, pinnedOnly=false — the same silicon R-4c read. NOTE for the hub: the bench card's `/api/v1/entities` prints `deviceId=None` on all six rows — the bench card's Core predates CG-123's v1.1.3 keys (the fence kept it un-upgraded; runner `B3.1-2026-08-02-postwindow @ 16e672d`); the held card's wire had deviceId on every row. Three health-token dumps in the paste are the same ten lines (relinked ×6 · adoption_maps_rehydrated devices=6 · network_resumed · network_up) for the 04:32 boot, the 14:48 start and the 14:49 scenario restart — the 14:49 set is shown whole.
```text
hs-dev-1
18:48:10Z
  [!!] NOT running
  [OK] launched pid 2173 -> /home/homesynapse/hs-bench/bench-2026-09-19-144810.log
  [OK] RADIO UP after 25s
  [OK] running (pid 2173)
runner B3.1-2026-08-02-postwindow @ 16e672d
  [--] stimulus bench: restart
  [OK] stopped
  [OK] launched pid 2350 -> /home/homesynapse/hs-bench/bench-2026-09-19-144928.log
  [OK] RADIO UP after 13s
14:49:32.714 registry.projection_live: devices=6 entities=6 position=25065
14:49:33.136 zigbee.device_relinked: device=0x00124B002FA8D1C5 deviceId=01KXW1W1RR66GV98D9QDPB4VXY — re-pairing, no new adoption
14:49:33.137 zigbee.device_relinked: device=0xF044D3FFFE1C1E8E deviceId=01KXW13WEGRCT5C0XSQT8WZBG9 — re-pairing, no new adoption
14:49:33.137 zigbee.device_relinked: device=0xF044D3FFFED2A201 deviceId=01KXW0156Z1GJ3WCV2G516AKWS — re-pairing, no new adoption
14:49:33.138 zigbee.device_relinked: device=0x00178801101A09BB deviceId=01KX1PA4GRZHY2GD37B5CFVQHY — re-pairing, no new adoption
14:49:33.139 zigbee.device_relinked: device=0x449FDAFFFE688F57 deviceId=01KY12MQVQ204M1VP39F1ZDM33 — re-pairing, no new adoption
14:49:33.139 zigbee.device_relinked: device=0xF044D3FFFE9C78D7 deviceId=01KX1PB9A5931A8G0F0X03QXT2 — re-pairing, no new adoption
14:49:33.140 zigbee.adoption_maps_rehydrated: devices=6
14:49:40.863 zigbee.port_identity_captured: stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false
14:49:40.978 zigbee.network_resumed: channel=20 panId=0x774c
    [ok] log 'registry.projection_live: devices=6 entities=6' min=25065 (within 90s)
    [ok] log 'zigbee.adoption_maps_rehydrated: devices=6' (within 90s)
    [ok] log 'zigbee.device_relinked' x2(at-least) (within 90s)
    [ok] log 'zigbee.network_resumed: channel=20 panId=0x774c' (within 90s)
    [ok] log 'zigbee.port_identity_captured:' same-line ['pinnedOnly=false'] (within 90s)
    [ok] api /api/v1/entities {"rows": 6, "ulids": ["01KX1PA4HSJ581GASYB7DHE40F", "01KX1PB9AAB4VB3E10BD477TV3", "01KXW0157SP56CCSGJCNDCSQNG", "01KXW13WF0D6TYGN13WXHTG87K", "01KXW1W1SBJZERC9MBAMV2DWKE", "01KY12MQW954E4XYNKH0Y5H8VX"]} — all asserts satisfied (within 90s)
[PASS] boot-health — 6/6 positive · 0 forbidden
  [--] bundle: /home/homesynapse/hs-bench/bundles/boot-health-20260919T184941Z
formed=0
relinked=6 adopted=0 announced=0 reporting_configured=0
registry rows=6
   01KX1PA4HSJ581GASYB7DHE40F deviceId=None
   01KX1PB9AAB4VB3E10BD477TV3 deviceId=None
   01KXW0157SP56CCSGJCNDCSQNG deviceId=None
   01KXW13WF0D6TYGN13WXHTG87K deviceId=None
   01KXW1W1SBJZERC9MBAMV2DWKE deviceId=None
   01KY12MQW954E4XYNKH0Y5H8VX deviceId=None
```

## §7 B6 — the tree · THE RUN · the digest line verbatim · the bundle names · formed

⏺ B6-1 THE BENCH TREE — filed 2026-09-19T18:54:43Z — MET (the packet's own fast-forward branch): hs-dev-1 · the card's tree was at **16e672d** (B3.3, 2026-08-04 — four commits behind) · porcelain=0 · `git pull --ff-only` fast-forwarded to **fa01cad** (BENCH-METER-1b), which CONTAINS f3631cb (navigator check on the desktop clone: `merge-base --is-ancestor f3631cb fa01cad` = yes; the path 16e672d → 4539f13 → 1201368 → f3631cb → 764e537 → fa01cad) · `selftest: 43 check(s), 0 failure(s)` (the packet's EXPECTED said 30 at f3631cb; 43 is the count at fa01cad — the two BENCH-METER commits added checks) · the timer: NEXT `Sun 2026-09-20 04:30:00 EDT` (= 03:30 CT) — LAST fired `Sat 2026-09-19 04:30:53 EDT`. The first `fleet:` datum in the digest is now possible on the bench card.
```text
hs-dev-1
16e672d bench: B3.3 - the s31 suite-position amendment (the 2026-08-04 ruling; hub-audited
porcelain=0
 create mode 100644 tools/harness/test_harness.py
 create mode 100644 tools/runner/test_engine.py
fa01cad bench: BENCH-METER-1b — the record's two subtractions with the side in the name,
selftest: 43 check(s), 0 failure(s)
NEXT                        LEFT LAST                        PASSED UNIT                       ACTIVATES
Sun 2026-09-20 04:30:00 EDT  13h Sat 2026-09-19 04:30:53 EDT      - nexsys-bench-nightly.timer nexsys-bench-nightly.service
```

⏺ B6-2 THE RUN — filed 2026-09-19T18:57:19Z — **STOP-GATE R5B-5 MET (the digest line ⏺'d verbatim WITH `fleet:` · formed 0 on the bench card — the LAST token of the sitting).** RUN pid=2538 at 18:55:09Z; the digest line landed at 18:56:39Z (lines 50 → 51; the suite ran in ~90 s). **THE FIRST `fleet:` DATUM EVER PRINTED: `fleet: 6/6 · re-seen 0`** — P-B1's fleet clause met on line 1. The floor: **`7/9 · FAIL usb-reenumeration`** (bundle `usb-reenumeration-20260919T185603Z`) · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.08 s — NOT the 9/9 or the SKIP-honest 8/9 the prediction named, and NOT the 09-12/09-18 `command-confirm-s31` shape either (command-confirm-s31 and command-s31-settle both bundled at 18:56:10/11 and did not fail tonight): a third scenario, usb-reenumeration, failed 60 s after the run began. The bundle path is filed; one T2 read of the runner's .out follows to characterize it; the hub adjudicates P-B1 on this line + Sunday's. Date label note: the digest now carries TWO `2026-09-19` lines (the 08:32Z timer run: 8/9 PASS · ON-latency 1.92 s, banked at H8-a B0-1; and this manual run).
```text
hs-dev-1
18:55:09Z
digest lines before=50
RUN pid=2538
18:56:39Z
digest lines after=51
2026-09-19 quiesced AUTO floor: 7/9 · FAIL usb-reenumeration · bundle /home/homesynapse/hs-bench/bundles/usb-reenumeration-20260919T185603Z · 1 SKIP(hue-online) · fleet: 6/6 · re-seen 0 · bench-hero RESTORED ✓ · ON-latency 0.08s
usb-reenumeration-20260919T185603Z
command-s31-settle-20260919T185611Z
command-confirm-s31-20260919T185610Z
formed=0
```

⏺ B6-2b THE FAIL, CHARACTERIZED (T2 read) — filed 2026-09-19T18:59:17Z — **`[FAIL] usb-reenumeration — environment fault: FileNotFoundError: [Errno 2] No such file or directory: 'uhubctl'`** — the scenario needs the `uhubctl` binary, which is not on the bench card; the scenario (or its uhubctl dependency) arrived with tonight's fast-forward to fa01cad (the 08:32Z timer run on 16e672d did not fail it). Not a Core failure: every other leg PASSED — `ran 8/9 — 1 SKIPPED: [hue-online]`; `[PASS] command-confirm-s31 — 2/2` · `[PASS] command-s31-settle — 1/1` · `[PASS] timeout-honesty-no-change — 2/2`. The runner: `fleet: 6/6 · re-seen 0 (registry read: nightly-logs/2026-09-19-registry-read.json)` · `nightly 2026-09-19 closing: exit path normal, exit code 1`. Bundle files: api-captures.json · MANIFEST.txt · quiesce-evidence.txt · resolved.json · scenario.yaml · verdict.txt. Sunday's 03:30 CT timer run will hit the same fault unless `uhubctl` is installed on the card — installing a package on the bench card is a rig change beyond the packet (T3): NOT done by the navigator; an ask of the hub.
```text
hs-dev-1
api-captures.json  MANIFEST.txt  quiesce-evidence.txt  resolved.json  scenario.yaml  verdict.txt
62:[2026-09-19 14:56:11] [FAIL] usb-reenumeration — environment fault: FileNotFoundError: [Errno 2] No such file or directory: 'uhubctl'
63:[2026-09-19 14:56:11]   [--] bundle: /home/homesynapse/hs-bench/bundles/usb-reenumeration-20260919T185603Z
67-[2026-09-19 14:56:11] [PASS] timeout-honesty-no-change — 2/2 positive · 0 forbidden
71-[2026-09-19 14:56:11] [PASS] command-confirm-s31 — 2/2 positive · 0 forbidden
75-[2026-09-19 14:56:11] [PASS] command-s31-settle — 1/1 positive · 0 forbidden
77-[2026-09-19 14:56:11] ran 8/9 — 1 SKIPPED: [hue-online]
98-[2026-09-19 14:56:32] [--] fleet: 6/6 · re-seen 0 (registry read: /home/homesynapse/hs-bench/nightly-logs/2026-09-19-registry-read.json)
100-[2026-09-19 14:56:32] [--] nightly 2026-09-19 closing: exit path normal, exit code 1
```

## §8 STOPs (none expected; each one whole if reached)

None reached. No T3 condition arose at any block: network_formed 0 on every read (held card ×5 invocations, bench card ×3 boots); integrity ok ×2; no downgrade; every http 200; the one design-class question (uhubctl on the bench card) was NOT acted on — filed as an ask.

## §9 Deviations ledger (D-n · tier · block · Z time · what · fix) + THE FINDINGS CARD FOR THE HUB

- **D-1 · T1 (instrument) · B0 · 2026-09-19T17:43:59Z** — inherited from H8-a's D-2 (same sitting, same card): `cut -c1-160` on the `zigbee.network_resumed` line truncates at `panI` (journald prefix + the app's stamp/thread/class ≈135 columns). B0 handed with `cut -c1-240`; nothing else in the block changed. B1c's `cut -c1-200` on the opened/resumed grep is left as written (short-iso-precise adds ~10 columns; the `permit_join_opened: duration=254s` token sits before column 200 — checked against B1-4's line length) — if it clips, the re-read is one T2 line.

- **D-2 · OP (an act outside the packet, on the FENCED device) · between H8-a B5 and R-5B B1c · 2026-09-19T17:54:16Z** — the operator reports, in his words: "while you were processing my command line results a few prompts ago, I turned on the S31, and then the vacuum plugged into it. About a second or two into the vacuum being turned on, the S31 power shut off." The fence (R-4c D-8, restated in this packet's inheritance line) says the S31 is never pressed, unplugged or cycled. The S31's `lastReported` moved 17:28:15 → 17:43:15.978 (B0's read, 17:44:31Z) → 17:45:13.608 (the poll's first sample, 17:46:40Z) — two reports 118 s apart, off the 5-min periodic cadence: consistent with an ON and an OFF in that interval. Candidate causes, none adjudicated here: bench-hero (StateChangeTrigger on the S31 → DelayAction → CommandAction on the S31; `verdict=NEVER_TRIGGERED` at 17:30) firing on the state change and commanding the plug; the S31's own overcurrent cut-out under the vacuum's inrush; the load itself. One T2 read is ordered after B3's frame table (the a3c45da2 invocation's journal for automation/command tokens 17:43–17:47 and the store rows for the S31 subject in that interval). Bears on P-B5 only if the act fell inside the window — it did not (the window opened 17:48:17Z). ASK: the hub rules on the fence breach and on what the vacuum load means for the harness (S31-LABEL: 15A/1800W).

- **D-3 · OP (the provocation protocol not executed as written) · B1c · 2026-09-19T18:10:22Z** — the operator's own words are under §2. Effects: ARM 1 not run (no battery pull); ARM 2 unconfirmed; the null-arm press unknown; other devices on the rig pressed/switched inside the window (which ones, asked before B3 — bears on P-B5's per-device table, whose "S31 0 with nothing switched" assumption may not hold). No software state changed by the operator; the packet's blocks continue (the disarm and the restore are mandatory). Navigator's own lesson, filed for the packet: the choreography must be ONE device, THREE named acts, each tied to a tick number, said back by the operator BEFORE the block is pasted — the packet's "have the SNZB-01P in hand" line was not enough at the rig.

  - D-3 addendum, 2026-09-19T18:18:59Z — the operator's answers to the two follow-up questions are under §3 (B2-2): the S31 WAS switched inside the window (and cut itself off after a few seconds, as at 17:45); every device but the SNZB-04P was disturbed (the 03P motion, the 02P temp/humidity warmed and cooled, the Hue lamp powered on). The vacuum has stayed plugged into the S31. D-4 (T2): one read-only summary of the poll ordered — per entity, each distinct lastReported with the first sample instant it appeared — so the window's reports are read sample-by-sample rather than from the before/after diff alone.

- **D-5 · T1 (instrument, no re-run) · B3-2 · 2026-09-19T18:28:24Z** — the S31 entity-row filter tests for `S31`/`on_off`/`switch` in the row's JSON; the v1.1.x entities body carries none of those strings, so the filter prints nothing on every card. Fix for the packet: select the row by deviceId (the `device_relinked` line's `deviceId=`) or by entityId. Not re-run — the row is already in entities-1.json (copied home before B4, D-6).
- **D-6 · T1 (instrument — evidence capture the packet omitted) · before B4 · 2026-09-19T18:28:24Z** — the packet leaves ~/r5b/ (entities-0.json · entities-1.json · poll.log · window-open.unix · poll.nohup) on the held card, which is then halted and swapped out. One scp from the desktop into `context/audits/2026-09-19_R-5B_capture/` is added before B4's halt (read-only on the rig; the desktop-prompt discipline of H8-a D-4 applied), with sha256 and a Bearer count of 0 on every file.

- **D-7 · T2 (one read-only probe) · B6-2 · 2026-09-19T18:59:23Z** — the runner .out grep and the bundle listing, to characterize the usb-reenumeration FAIL (an environment fault: uhubctl absent). Nothing on the rig changed; uhubctl NOT installed (T3 — the hub rules).


### THE FINDINGS CARD FOR THE HUB (navigator, 2026-09-19T19:00:15Z; ⏺ census: 23 paste-backs banked under §1–§7)
**What the wire showed that the desk did not predict.** (1) The window opened as designed and the air stayed silent for 254 s — but the desk's real miss was the *choreography*: three timed acts on one device, handed as prose, did not survive contact with the rig; the operator "pressed and switched everything". The untouched SNZB-04P is the only clean control and it behaved exactly (one instant, 79 samples). (2) bench-hero fired four times on the held card — 10.00 s delay, command, confirmation in 77–228 ms, 4/4 — and the journal holds none of it: the store is the only trace. (3) The bench card's tree was four commits behind; the pull brought usb-reenumeration's uhubctl dependency and the floor's first FAIL of a new kind. (4) The Hue powered on inside an open window: the coordinator saw nothing — a fifth non-reproduction. (5) The SNZB-03P came back from six days of silence inside the window, unprovoked by any packet act. **The stop-proof.** Two clean grades on 6bd8508 (success · 143 · inactive · dead · NRestarts=0); F-1 on both — the orderly transport close never runs; the watchdog re-opens the NCP under a dying JVM. **Three things to change in the packet.** (a) B1c's provocations become a checklist the operator says back BEFORE the paste (device · act · tick), one device only, with a STOP if any other device is touched. (b) B3's frame block copies ~/r5b home itself (D-6) and selects the S31 row by deviceId (D-5); B0's cut is 240 (D-1). (c) B6-1 pins the bench tree to a commit the hub has run the suite on, and lists the scenarios' binary dependencies (uhubctl) as a preflight read — a pull to HEAD at the rig changed what the floor measures.
## §10 The hub's close (v77 beat 6, Sun 2026-09-20 ~10:1x CT; instrument 2026-09-20T15:15:24Z)
**`R5B-2:` (Sunday 03:30 CT, read 12:33Z):** `2026-09-20 quiesced AUTO floor: 7/9 · FAIL command-confirm-s31 · bundle /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260920T083121Z · 1 SKIP(hue-online) · fleet: 6/6 · re-seen 6 · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)`. **P-B1 MET** on both lines (the fleet clause `6/6`; line 2 on the timer). The b2 audit's pre-registration CONFIRMED: `usb-reenumeration` passed on the timer with nothing installed — the manual FAIL was the sshd `PATH`; ask 1 refused, correctly. The 7/9 is the OR-NIGHTLY-0902-S31 class, the first night with the vacuum on the S31 (D-2/D-3) — the vacuum comes off today; Monday's line is the instrument. **CLOSED (hub-audited):** R5B-0..R5B-5 as recorded; the fleet floor row (`6/6 · re-seen 6 · adopted 0`; registry rows 6 byte-stable, re-read on the new Core at BENCH-CORE-1); P-B5's bounds banked; P-B2/P-B3/P-B6 NOT TESTED → `REARM: reh1` (D-v77-2); F-R4b-C carried; `C003:` unruled; the S31 fact row (the cut-out under the vacuum's inrush; `S31-LABEL: 15A 1800W — Input 120V @ 60Hz`); bench-hero 4/4 confirmed in 77–228 ms (a wire datum, not an outward claim); IR-34; D-1..D-7 → rehearsal 1's packet (the ONE-device, three-acts, say-it-back form). The audits: `2026-09-19_v77-b2_…` (the read) and `2026-09-20_v77-b6_…` (the close).

RETURNED context/audits/2026-09-19_R-5B_operator-record.md 50494
