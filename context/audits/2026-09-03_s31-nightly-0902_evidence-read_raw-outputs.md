<!--
file: context/audits/2026-09-03_s31-nightly-0902_evidence-read_raw-outputs.md
purpose: Companion exhibit to 2026-09-03_s31-nightly-0902_evidence-read_return.md — the eight ssh command lines and their COMPLETE outputs, verbatim as pasted by Nick (Git Bash, `ssh pi`), 2026-09-03 ~06:30–06:50 CT. This is the primary paste record (chat-is-not-a-storage-tier); the return pins the load-bearing extracts.
state-type: raw evidence exhibit (point-in-time) · read-only session — nothing on the card was touched
-->

# Raw outputs — 09-02 s31 evidence read (8 commands)

## Command 1 — hostname / date / digest tail / bundles ls
```
$ ssh pi '/usr/bin/hostname; /usr/bin/date -u; /usr/bin/tail -n 3 /home/homesynapse/hs-bench/digests/nightly.log; /usr/bin/ls -la /home/homesynapse/hs-bench/bundles/ | /usr/bin/tail -n 6'
hs-dev-1
Thu  3 Sep 11:48:10 UTC 2026
2026-09-01 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.10s
2026-09-02 quiesced AUTO floor: 7/9 · FAIL command-confirm-s31 · bundle /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260902T083122Z · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)
2026-09-03 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.09s
drwxrwxr-x   2 homesynapse homesynapse  4096 Jul 18 14:19 usb-reenumeration-manual-20260718T181914Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Jul 18 14:24 usb-reenumeration-manual-20260718T182430Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Jul 18 14:34 usb-reenumeration-manual-20260718T183446Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Jul 18 17:23 usb-reenumeration-manual-20260718T212347Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Jul 25 13:28 usb-reenumeration-manual-20260725T172815Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Jul 29 19:55 usb-reenumeration-manual-20260729T235544Z
```
Note: plain `ls` sorts by name, so the tail showed only `usb-…` entries — corrected by command 2.

## Command 2 — s31 bundle census / newest-by-time / digest last 6
```
$ ssh pi '/usr/bin/ls -la /home/homesynapse/hs-bench/bundles/ | /usr/bin/grep command-confirm-s31; echo ===NEWEST-BY-TIME; /usr/bin/ls -lat /home/homesynapse/hs-bench/bundles/ | /usr/bin/head -n 8; echo ===DIGEST-6; /usr/bin/tail -n 6 /home/homesynapse/hs-bench/digests/nightly.log'
drwxrwxr-x   2 homesynapse homesynapse  4096 Jul 29 20:01 command-confirm-s31-20260730T000124Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Jul 29 21:37 command-confirm-s31-20260730T013743Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Jul 31 00:22 command-confirm-s31-20260731T042204Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug  1 04:30 command-confirm-s31-20260801T083055Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug  2 04:31 command-confirm-s31-20260802T083057Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug  3 04:31 command-confirm-s31-20260803T083057Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug  4 04:31 command-confirm-s31-20260804T083057Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug  5 04:31 command-confirm-s31-20260805T083057Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug  6 04:31 command-confirm-s31-20260806T083127Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug  6 20:12 command-confirm-s31-20260807T001211Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug  7 04:31 command-confirm-s31-20260807T083127Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug  8 04:31 command-confirm-s31-20260808T083127Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug  9 04:31 command-confirm-s31-20260809T083132Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 10 04:31 command-confirm-s31-20260810T083135Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 11 04:31 command-confirm-s31-20260811T083127Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 12 04:31 command-confirm-s31-20260812T083146Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 13 04:31 command-confirm-s31-20260813T083132Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 14 04:34 command-confirm-s31-20260814T083338Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 15 04:34 command-confirm-s31-20260815T083334Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 16 04:32 command-confirm-s31-20260816T083217Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 17 04:32 command-confirm-s31-20260817T083214Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 18 04:32 command-confirm-s31-20260818T083213Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 19 04:32 command-confirm-s31-20260819T083215Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 20 04:32 command-confirm-s31-20260820T083217Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 21 04:32 command-confirm-s31-20260821T083216Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 22 04:32 command-confirm-s31-20260822T083215Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 23 04:32 command-confirm-s31-20260823T083215Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 24 04:31 command-confirm-s31-20260824T083118Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 25 04:31 command-confirm-s31-20260825T083118Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 26 04:31 command-confirm-s31-20260826T083118Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 27 04:31 command-confirm-s31-20260827T083123Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 28 04:31 command-confirm-s31-20260828T083118Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 29 04:31 command-confirm-s31-20260829T083117Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 30 04:31 command-confirm-s31-20260830T083121Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Aug 31 04:31 command-confirm-s31-20260831T083120Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Sep  1 04:31 command-confirm-s31-20260901T083117Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Sep  2 04:31 command-confirm-s31-20260902T083122Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Sep  3 07:12 command-confirm-s31-20260903T111217Z
===NEWEST-BY-TIME
total 1412
drwxrwxr-x   8 homesynapse homesynapse 12288 Sep  3 07:12 ..
drwxrwxr-x   2 homesynapse homesynapse  4096 Sep  3 07:12 command-s31-settle-20260903T111218Z
drwxrwxr-x 346 homesynapse homesynapse 20480 Sep  3 07:12 .
drwxrwxr-x   2 homesynapse homesynapse  4096 Sep  3 07:12 command-confirm-s31-20260903T111217Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Sep  3 07:12 timeout-honesty-no-change-20260903T111216Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Sep  3 07:12 usb-reenumeration-20260903T111210Z
drwxrwxr-x   2 homesynapse homesynapse  4096 Sep  3 07:11 command-identify-honest-20260903T111155Z
===DIGEST-6
2026-08-29 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.50s
2026-08-30 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 3.29s
2026-08-31 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 3.52s
2026-09-01 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.10s
2026-09-02 quiesced AUTO floor: 7/9 · FAIL command-confirm-s31 · bundle /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260902T083122Z · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)
2026-09-03 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.09s
```

## Command 3 — 09-02 bundle: ls / MANIFEST / verdict / resolved / scenario stat
```
$ ssh pi 'B=/home/homesynapse/hs-bench/bundles/command-confirm-s31-20260902T083122Z; /usr/bin/ls -la "$B"; echo ===MANIFEST; /usr/bin/cat "$B/MANIFEST.txt"; echo ===VERDICT; /usr/bin/cat "$B/verdict.txt"; echo ===RESOLVED; /usr/bin/cat "$B/resolved.json"; echo ===SCENARIO-STAT; /usr/bin/stat -c "%y %n" "$B/scenario.yaml"'
total 60
drwxrwxr-x   2 homesynapse homesynapse  4096 Sep  2 04:31 .
drwxrwxr-x 346 homesynapse homesynapse 20480 Sep  3 07:12 ..
-rw-rw-r--   1 homesynapse homesynapse  1421 Sep  2 04:31 api-captures.json
-rw-rw-r--   1 homesynapse homesynapse   835 Sep  2 04:31 MANIFEST.txt
-rw-rw-r--   1 homesynapse homesynapse   791 Sep  2 04:31 post-window-state.json
-rw-rw-r--   1 homesynapse homesynapse  1268 Sep  2 04:31 quiesce-evidence.txt
-rw-rw-r--   1 homesynapse homesynapse  3238 Sep  2 04:31 resolved.json
-rw-rw-r--   1 homesynapse homesynapse  8127 Jul 31 00:17 scenario.yaml
-rw-rw-r--   1 homesynapse homesynapse  1176 Sep  2 04:31 verdict.txt
===MANIFEST
bundle: command-confirm-s31-20260902T083122Z
written: 2026-09-02T08:31:22+00:00

scenario.yaml — the scenario file as run
resolved.json — constants + let bindings + run-window markers + extracted values (e.g. the boot position — the aged-replay stake, recorded per DP-8 row 1)
app-log-slice.log ABSENT — window read + bundle-time marker-offset re-read both returned zero lines — the app wrote nothing in the run window
journal-slice.txt DROPPED (B3.1 A-6): two nights of noise-only exhibits (night-1 D-6; night-2 tailscaled x2) — app-log-slice + api-captures are the targeted evidence
api-captures.json — 2 captured API exchange(s)
post-window-state.json — the A-9 one-shot GET of the command target's /state at terminal-read FAIL (the late-report-vs-no-edge discriminator)
verdict.txt — the one-page verdict summary
===VERDICT
scenario: command-confirm-s31
verdict:  FAIL
reason:   terminal phase mismatch: expected CONFIRMED, read CONFIRMATION_TIMED_OUT — {"data":{"commandId":"01M1GKWV46MNZKS51J79K7M4ZY","correlationId":"01M1GKWV46MNZKS51J79K7M4ZY","entityId":"01KXW1W1SBJZERC9MBAMV2DWKE","capability":"on_off","command":"turn_on","lifecycle":{"ACCEPTED":{"at":"2026-09-02T08:31:16.102305Z","eventId":"01M1GKWV46MNZKS51J79K7M4ZY","details":null},"DISPATC
started:  2026-09-02T08:31:16+00:00
duration: 6.1s
log:      /home/homesynapse/hs-bench/bench-2026-09-02-043028.log
markers:  [{"at": "2026-09-02T08:31:16+00:00", "note": "api POST /api/v1/entities/01KXW1W1SBJZERC9MBAMV2DWKE/commands", "log_offset": 11442}]

evidence lines:
  [X] api /api/v1/commands/01M1GKWV46MNZKS51J79K7M4ZY {"phase_terminal": "CONFIRMED"} — terminal phase mismatch: expected CONFIRMED, read CONFIRMATION_TIMED_OUT — {"data":{"commandId":"01M1GKWV46MNZKS51J79K7M4ZY","correlationId":"01M1GKWV46MNZKS51J79K7M4ZY","entityId":"01KXW1W1SBJZERC9MBAMV2DWKE","capability":"on_off","command":"turn_on","lifecycle":{"ACCEPTED":{"at":"2026-09-02T08:31:16.102305Z","eventId":"01M1GKWV46MNZKS51J79K7M4ZY","details":null},"DISPATC
===RESOLVED
(full 3238-byte resolved.json reproduced in the paste; load-bearing values pinned here)
  command.s31-entity: "01KXW1W1SBJZERC9MBAMV2DWKE" · command.s31-ieee: "0x00124B002FA8D1C5"
  let.command_id: "01M1GKWV46MNZKS51J79K7M4ZY"
  network: channel 20, panId 0x774c · serial-port-alias: /dev/zigbee · api.base: http://127.0.0.1:7070
  auto-suite (order): boot-health · command-confirm · command-timeout-absent · command-supersession · command-identify-honest · usb-reenumeration · timeout-honesty-no-change · command-confirm-s31 · command-s31-settle
  command-lifecycle.phases: ACCEPTED, DISPATCHED, ACKNOWLEDGED, CONFIRMED, CONFIRMATION_TIMED_OUT (terminal-field data.terminal, phase-field data.currentPhase)
  capabilities: command-api available (CMD-API 5b4797e, deployed c09c61c 2026-07-27); hue-online unavailable (HUE-RESET pending); usb-power available (uhubctl 2.6.0-1, hub 3-2.4 port 2); plug unavailable
  markers: [{"at": "2026-09-02T08:31:16+00:00", "note": "api POST /api/v1/entities/01KXW1W1SBJZERC9MBAMV2DWKE/commands", "log_offset": 11442}] · extracted: {}
===SCENARIO-STAT
2026-07-31 00:17:34.581236456 -0400 /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260902T083122Z/scenario.yaml
```

## Command 4 — api-captures.json + post-window-state.json (full dumps)
```
$ ssh pi 'B=/home/homesynapse/hs-bench/bundles/command-confirm-s31-20260902T083122Z; echo ===API-CAPTURES; /usr/bin/python3 -m json.tool "$B/api-captures.json"; echo ===POST-WINDOW-STATE; /usr/bin/python3 -m json.tool "$B/post-window-state.json"'
===API-CAPTURES
[
  { "when": "2026-09-02T08:31:16+00:00",
    "what": "stimulus POST /api/v1/entities/01KXW1W1SBJZERC9MBAMV2DWKE/commands",
    "status": 202,
    "body": "{\"data\":{\"commandId\":\"01M1GKWV46MNZKS51J79K7M4ZY\",\"correlationId\":\"01M1GKWV46MNZKS51J79K7M4ZY\",\"entityId\":\"01KXW1W1SBJZERC9MBAMV2DWKE\",\"status\":\"accepted\",\"acceptedAt\":\"2026-09-02T08:31:16.102305101Z\",\"viewPosition\":137900},\"meta\":{\"viewPosition\":137899,\"timestamp\":\"2026-09-02T08:31:16.105098059Z\"}}" },
  { "when": "2026-09-02T08:31:22+00:00",
    "what": "assert GET /api/v1/commands/01M1GKWV46MNZKS51J79K7M4ZY",
    "status": 200,
    "body": "{\"data\":{\"commandId\":\"01M1GKWV46MNZKS51J79K7M4ZY\",\"correlationId\":\"01M1GKWV46MNZKS51J79K7M4ZY\",\"entityId\":\"01KXW1W1SBJZERC9MBAMV2DWKE\",\"capability\":\"on_off\",\"command\":\"turn_on\",\"lifecycle\":{\"ACCEPTED\":{\"at\":\"2026-09-02T08:31:16.102305Z\",\"eventId\":\"01M1GKWV46MNZKS51J79K7M4ZY\",\"details\":null},\"DISPATCHED\":{\"at\":\"2026-09-02T08:31:16.104643Z\",\"eventId\":\"01M1GKWV483Q7PRFRCH604YNY5\",\"details\":{\"integration_id\":\"6V1CMGY2HKF4H1FGZ4H7F257FS\"}},\"CONFIRMATION_TIMED_OUT\":{\"at\":\"2026-09-02T08:31:21.601076Z\",\"eventId\":\"01M1GKX0G07CBNAAY9Q5T14Q10\",\"details\":null}},\"currentPhase\":\"CONFIRMATION_TIMED_OUT\",\"terminal\":true},\"meta\":{\"viewPosition\":137902,\"timestamp\":\"2026-09-02T08:31:22.137864394Z\"}}" }
]
===POST-WINDOW-STATE
{ "when": "2026-09-02T08:31:22+00:00",
  "what": "post-window state read (A-9: the late-report-vs-no-edge discriminator)",
  "path": "/api/v1/entities/01KXW1W1SBJZERC9MBAMV2DWKE/state",
  "status": 200,
  "body": { "data": {
      "entityId": {"value": {"msb": 116944185699571677, "lsb": -8780177225415200146}},
      "attributes": {"on": {"value": false}},
      "availability": "AVAILABLE",
      "stateVersion": 12646,
      "lastChanged": 1788251477.275482,
      "lastUpdated": 1788337881.601076,
      "lastReported": 1788337735.86976,
      "staleAfter": null, "stale": false },
    "meta": {"viewPosition": 137902, "timestamp": "2026-09-02T08:31:22.142128951Z"} } }
```
Epoch→Z (arithmetic, base 2026-09-02T00:00:00Z = 1788307200): lastReported 1788337735.86976 → +30535.87 s = 08:28:55.870Z (09-02). lastUpdated 1788337881.601076 → +30681.60 s = 08:31:21.601Z (= the CONFIRMATION_TIMED_OUT stamp). lastChanged 1788251477.275482 → 2026-09-01 base 1788220800 +30677.28 s = 09-01 08:31:17.275Z.

## Command 5 — quiesce-evidence + 09-02 settle bundle verdict
```
$ ssh pi 'B=/home/homesynapse/hs-bench/bundles/command-confirm-s31-20260902T083122Z; echo ===QUIESCE; /usr/bin/cat "$B/quiesce-evidence.txt"; echo ===SETTLE-0902; /usr/bin/ls -d /home/homesynapse/hs-bench/bundles/command-s31-settle-20260902T*; /usr/bin/cat /home/homesynapse/hs-bench/bundles/command-s31-settle-20260902T*/verdict.txt'
===QUIESCE
=== 2026-09-02 post-quiesce automations read (expect '"bench-hero"' ABSENT) — 2026-09-02T04:30:21-04:00 — GET http://127.0.0.1:7070/api/v1/automations — HTTP 200 ===
{"data":[],"pagination":{"nextCursor":null,"hasMore":false,"limit":50},"meta":{"viewPosition":137882,"timestamp":"2026-09-02T08:30:21.025033707Z"}}
=== 2026-09-02 post-restore automations read (expect '"bench-hero"' PRESENT) — 2026-09-02T04:31:43-04:00 — GET http://127.0.0.1:7070/api/v1/automations — HTTP 200 ===
{"data":[{"automationId":"01M1GKXD599YX5DVQDDZ44E9AY","name":"bench-hero","enabled":true,"components":[{"type":"StateChangeTrigger","summary":"state change trigger"},{"type":"CommandAction","summary":"command action"},{"type":"DelayAction","summary":"delay action"},{"type":"CommandAction","summary":"command action"},{"type":"DelayAction","summary":"delay action"},{"type":"CommandAction","summary":"command action"},{"type":"DelayAction","summary":"delay action"},{"type":"CommandAction","summary":"command action"},{"type":"DelayAction","summary":"delay action"},{"type":"CommandAction","summary":"command action"}],"lastRunId":null}],"pagination":{"nextCursor":null,"hasMore":false,"limit":50},"meta":{"viewPosition":137908,"timestamp":"2026-09-02T08:31:43.547070419Z"}}
===SETTLE-0902
/home/homesynapse/hs-bench/bundles/command-s31-settle-20260902T083123Z
scenario: command-s31-settle
verdict:  PASS
reason:   1/1 positive · 0 forbidden
started:  2026-09-02T08:31:22+00:00
duration: 1.1s
log:      /home/homesynapse/hs-bench/bench-2026-09-02-043028.log
markers:  [{"at": "2026-09-02T08:31:22+00:00", "note": "api POST /api/v1/entities/01KXW1W1SBJZERC9MBAMV2DWKE/commands", "log_offset": 11442}]

evidence lines:
  [ok] api /api/v1/commands/01M1GKX12RHSGW7PXSVWBSY7EP {"field_equals": {"field": "data.terminal", "value": true}} — all asserts satisfied (within 25s)
```

## Command 6 — system journal, 08:25–08:40Z, tailscale/magicsock filtered
```
$ ssh pi '/usr/bin/journalctl --no-pager -S "2026-09-02 08:25:00 UTC" -U "2026-09-02 08:40:00 UTC" | /usr/bin/grep -i -v "tailscale\|magicsock" | /usr/bin/head -n 120'
-- No entries --
```

## Command 7 — settle api-captures (full) + bench-log grep
```
$ ssh pi '/usr/bin/python3 -m json.tool /home/homesynapse/hs-bench/bundles/command-s31-settle-20260902T083123Z/api-captures.json'
[
  { "when": "2026-09-02T08:31:22+00:00",
    "what": "stimulus POST /api/v1/entities/01KXW1W1SBJZERC9MBAMV2DWKE/commands",
    "status": 202,
    "body": "{\"data\":{\"commandId\":\"01M1GKX12RHSGW7PXSVWBSY7EP\",\"correlationId\":\"01M1GKX12RHSGW7PXSVWBSY7EP\",\"entityId\":\"01KXW1W1SBJZERC9MBAMV2DWKE\",\"status\":\"accepted\",\"acceptedAt\":\"2026-09-02T08:31:22.201111812Z\",\"viewPosition\":137903},\"meta\":{\"viewPosition\":137902,\"timestamp\":\"2026-09-02T08:31:22.203600569Z\"}}" },
  { "when": "2026-09-02T08:31:23+00:00",
    "what": "assert GET /api/v1/commands/01M1GKX12RHSGW7PXSVWBSY7EP",
    "status": 200,
    "body": "{\"data\":{\"commandId\":\"01M1GKX12RHSGW7PXSVWBSY7EP\",\"correlationId\":\"01M1GKX12RHSGW7PXSVWBSY7EP\",\"entityId\":\"01KXW1W1SBJZERC9MBAMV2DWKE\",\"capability\":\"on_off\",\"command\":\"turn_off\",\"lifecycle\":{\"ACCEPTED\":{\"at\":\"2026-09-02T08:31:22.201111Z\",\"eventId\":\"01M1GKX12RHSGW7PXSVWBSY7EP\",\"details\":null},\"DISPATCHED\":{\"at\":\"2026-09-02T08:31:22.204493Z\",\"eventId\":\"01M1GKX12W6TQA5FTXFZDWAYDR\",\"details\":{\"integration_id\":\"6V1CMGY2HKF4H1FGZ4H7F257FS\"}},\"CONFIRMED\":{\"at\":\"2026-09-02T08:31:22.689506Z\",\"eventId\":\"01M1GKX1J1ZKTS7XVTWV70H1HY\",\"details\":{\"match_type\":\"exact\"}}},\"currentPhase\":\"CONFIRMED\",\"terminal\":true},\"meta\":{\"viewPosition\":137906,\"timestamp\":\"2026-09-02T08:31:23.215901105Z\"}}" }
]

$ ssh pi '/usr/bin/grep -n -i "s31\|command-confirm\|CONFIRM\|DISPATCH\|ACCEPTED\|timed_out\|FAIL\|restore\|hero" /home/homesynapse/hs-bench/bench-2026-09-02-043028.log | /usr/bin/head -n 120'
55:04:30:53.909 [integration-cmd-zigbee-0] INFO  c.h.i.zigbee.ZigbeeCommandHandler -- zigbee.command_result: outcome=unconfirmed entity=01KXW1W1SBJZERC9MBAMV2DWKE command=identify correlation=01M1GKW5C25Y6D8C0R6ZHT9K4E reason=no confirmation surface exists for 'identify'; the command was issued and is not tracked
56:04:31:04.969 [integration-zigbee-0] WARN  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.transport_failed: serial read error: port dead or closed; lastFrame=DATA(frm=4, ack=0, reTx=false) retransmits=0 crcRejects=0 timeouts=0 — the watchdog owns recovery
59:04:31:04.973 [integration-zigbee-0] WARN  c.h.integration.zigbee.PortWatchdog -- zigbee.port_reopen_failed: attempt 1 failed; next attempt in 1000 ms
61:04:31:07.881 [integration-zigbee-0] WARN  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.reopen_failed: unexpected NCP reset (RSTACK) while connected: resetCode=0x0B; lastFrame=DATA(frm=0, ack=0, reTx=false) retransmits=0 crcRejects=0 timeouts=0
62:04:31:07.885 [integration-zigbee-0] WARN  c.h.integration.zigbee.PortWatchdog -- zigbee.port_reopen_failed: attempt 2 failed; next attempt in 2000 ms
69:04:31:09.691 [integration-zigbee-0] INFO  c.h.integration.zigbee.PortWatchdog -- zigbee.port_reopened: recovery succeeded after 2 failed attempts
73:04:31:23.296 [integration-zigbee-0] WARN  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.transport_failed: serial read error: port dead or closed; lastFrame=DATA(frm=3, ack=6, reTx=false) retransmits=0 crcRejects=0 timeouts=0 — the watchdog owns recovery
83:04:31:25.002 [integration-zigbee-0] INFO  c.h.integration.zigbee.PortWatchdog -- zigbee.port_reopened: recovery succeeded after 0 failed attempts
```

## Command 8 — 08-02 verdict + usb-reenumeration-0902 verdict + bench-log lines 41–100
```
$ ssh pi 'echo ===0802-VERDICT; /usr/bin/cat /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260802T083057Z/verdict.txt; echo ===USB-REENUM-0902; /usr/bin/cat /home/homesynapse/hs-bench/bundles/usb-reenumeration-20260902T*/verdict.txt'
===0802-VERDICT
scenario: command-confirm-s31
verdict:  FAIL
reason:   terminal phase mismatch: expected CONFIRMED, read CONFIRMATION_TIMED_OUT — {"data":{"commandId":"01KZ0SHTCKAMR9TCGEDK54R39N","correlationId":"01KZ0SHTCKAMR9TCGEDK54R39N","entityId":"01KXW1W1SBJZERC9MBAMV2DWKE","capability":"on_off","command":"turn_on","lifecycle":{"ACCEPTED":{"at":"2026-08-02T08:30:51.795524Z","eventId":"01KZ0SHTCKAMR9TCGEDK54R39N","details":null},"DISPATC
started:  2026-08-02T08:30:51+00:00
duration: 6.1s
log:      /home/homesynapse/hs-bench/bench-2026-08-02-043039.log
markers:  [{"at": "2026-08-02T08:30:51+00:00", "note": "api POST /api/v1/entities/01KXW1W1SBJZERC9MBAMV2DWKE/commands", "log_offset": 8923}]

evidence lines:
  [X] api /api/v1/commands/01KZ0SHTCKAMR9TCGEDK54R39N {"phase_terminal": "CONFIRMED"} — terminal phase mismatch: expected CONFIRMED, read CONFIRMATION_TIMED_OUT — (embedded lifecycle JSON truncates at "DISPATC", as in the 09-02 verdict.txt)
===USB-REENUM-0902
scenario: usb-reenumeration
verdict:  PASS
reason:   2/2 positive · 0 forbidden
started:  2026-09-02T08:30:54+00:00
duration: 15.1s
log:      /home/homesynapse/hs-bench/bench-2026-09-02-043028.log
markers:  [{"at": "2026-09-02T08:30:54+00:00", "note": "usb cycle", "log_offset": 9237}]

evidence lines:
  [ok] log-any ['zigbee.transport_failed', 'zigbee.port_unhealthy'] — 04:31:04.969 [integration-zigbee-0] WARN  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.transport_failed: serial read error: port dead or closed; lastFrame=DATA(frm=4, ack=0, reTx=false) retransmits=0 crcRejects=0 timeouts=0 — the watchdog owns recovery (within 30s)
  [ok] log 'zigbee.reopened' — 04:31:09.691 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.reopened: port=/dev/ttyUSB0 (within 120s)

$ ssh pi '/usr/bin/head -n 100 /home/homesynapse/hs-bench/bench-2026-09-02-043028.log | /usr/bin/tail -n 60'
04:30:32.930 [main] INFO  io.javalin.Javalin -- You are running Javalin 6.7.0 (released June 22, 2025. Your Javalin version is 436 days old. Consider checking for a newer version.).
04:30:32.930 [main] INFO  c.h.lifecycle.HomeSynapseCore -- HTTP surface exposed on 127.0.0.1:7070 behind bearer-token auth (AB-1, C1 closed); loopback-default bindHost=127.0.0.1
04:30:32.974 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeDeviceCache -- zigbee.device_cache_loaded: 6 devices from /home/homesynapse/hs-bench/data/zigbee/zigbee-devices.json
04:30:32.980 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0xF044D3FFFED2A201 deviceId=01KXW0156Z1GJ3WCV2G516AKWS — re-pairing, no new adoption
04:30:32.981 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0x00178801101A09BB deviceId=01KX1PA4GRZHY2GD37B5CFVQHY — re-pairing, no new adoption
04:30:32.982 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0x449FDAFFFE688F57 deviceId=01KY12MQVQ204M1VP39F1ZDM33 — re-pairing, no new adoption
04:30:32.982 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0xF044D3FFFE9C78D7 deviceId=01KX1PB9A5931A8G0F0X03QXT2 — re-pairing, no new adoption
04:30:32.983 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0x00124B002FA8D1C5 deviceId=01KXW1W1RR66GV98D9QDPB4VXY — re-pairing, no new adoption
04:30:32.983 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0xF044D3FFFE1C1E8E deviceId=01KXW13WEGRCT5C0XSQT8WZBG9 — re-pairing, no new adoption
04:30:32.984 [integration-supervisor-start] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.adoption_maps_rehydrated: devices=6
04:30:32.994 [integration-supervisor-start] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.availability_seeded: devices=6 from_sidecar=6 unknown=0
04:30:32.998 [integration-supervisor-start] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.learned_zonetypes_rehydrated: count=2
04:30:33.002 [integration-supervisor-start] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.initialized: integration_id=6V1CMGY2HKF4H1FGZ4H7F257FS data_dir=/home/homesynapse/hs-bench/data/zigbee mode=production
04:30:33.003 [integration-supervisor-start] INFO  c.h.i.r.StandardIntegrationSupervisor -- integration.launched: integration_id=6V1CMGY2HKF4H1FGZ4H7F257FS integration_type=zigbee io_type=SERIAL
04:30:33.125 [main] INFO  c.h.lifecycle.HomeSynapseCore -- HomeSynapseCore RUNNING: db=/home/homesynapse/hs-bench/data/homesynapse-events.db, configDir=/home/homesynapse/hs-bench/config, homeId=01KWVQ4XMC5803M3ZQYR87VMHW, automations=0; HTTP exposed behind bearer-token auth on 127.0.0.1:7070 (AB-1), cipher inert=false
HomeSynapse Core is RUNNING (phase=RUNNING); HTTP surface exposed behind bearer-token auth, loopback-bound (AB-1). Send SIGTERM to stop.
04:30:39.019 [integration-zigbee-0] INFO  c.h.i.zigbee.TransportProbe -- zigbee.transport_detected: kind=EZSP port=/dev/zigbee
04:30:40.609 [integration-zigbee-0] INFO  c.h.integration.zigbee.AshSession -- ASH session connected: ashVersion=2 resetCode=0xb
04:30:40.612 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.port_identity_captured: stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false
04:30:40.620 [integration-zigbee-0] INFO  c.h.i.zigbee.EzspCoordinatorProtocol -- EZSP session negotiated: protocolVersion=13 stackType=2 stackVersion=0x7450
04:30:40.677 [integration-zigbee-0] WARN  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.ncp_config_skipped: id=0x1 status=0x37
04:30:40.683 [integration-zigbee-0] WARN  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.ncp_config_skipped: id=0x6 status=0x35
04:30:40.701 [integration-zigbee-0] INFO  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.ncp_configured: zdo_flags=0x3 stack_profile=2 security_level=5
04:30:40.728 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
04:30:40.728 [integration-zigbee-0] INFO  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.network_up: stackStatusHandler reported EMBER_NETWORK_UP (buffered)
04:30:40.728 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.production_session_started: port=/dev/zigbee protocolVersion=13
04:30:53.909 [integration-cmd-zigbee-0] INFO  c.h.i.zigbee.ZigbeeCommandHandler -- zigbee.command_result: outcome=unconfirmed entity=01KXW1W1SBJZERC9MBAMV2DWKE command=identify correlation=01M1GKW5C25Y6D8C0R6ZHT9K4E reason=no confirmation surface exists for 'identify'; the command was issued and is not tracked
04:31:04.969 [integration-zigbee-0] WARN  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.transport_failed: serial read error: port dead or closed; lastFrame=DATA(frm=4, ack=0, reTx=false) retransmits=0 crcRejects=0 timeouts=0 — the watchdog owns recovery
04:31:04.969 [integration-zigbee-0] WARN  c.h.integration.zigbee.PortWatchdog -- zigbee.port_unhealthy: cause=read-error; reopen scheduling started
04:31:04.973 [integration-zigbee-0] WARN  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.reopen_no_target: the coordinator port did not re-enumerate; retrying on the watchdog backoff
04:31:04.973 [integration-zigbee-0] WARN  c.h.integration.zigbee.PortWatchdog -- zigbee.port_reopen_failed: attempt 1 failed; next attempt in 1000 ms
04:31:06.401 [integration-zigbee-0] INFO  c.h.integration.zigbee.AshSession -- ASH session connected: ashVersion=2 resetCode=0x2
04:31:07.881 [integration-zigbee-0] WARN  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.reopen_failed: unexpected NCP reset (RSTACK) while connected: resetCode=0x0B; lastFrame=DATA(frm=0, ack=0, reTx=false) retransmits=0 crcRejects=0 timeouts=0
04:31:07.885 [integration-zigbee-0] WARN  c.h.integration.zigbee.PortWatchdog -- zigbee.port_reopen_failed: attempt 2 failed; next attempt in 2000 ms
04:31:09.580 [integration-zigbee-0] INFO  c.h.integration.zigbee.AshSession -- ASH session connected: ashVersion=2 resetCode=0xb
04:31:09.586 [integration-zigbee-0] INFO  c.h.i.zigbee.EzspCoordinatorProtocol -- EZSP session negotiated: protocolVersion=13 stackType=2 stackVersion=0x7450
04:31:09.642 [integration-zigbee-0] WARN  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.ncp_config_skipped: id=0x1 status=0x37
04:31:09.648 [integration-zigbee-0] WARN  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.ncp_config_skipped: id=0x6 status=0x35
04:31:09.666 [integration-zigbee-0] INFO  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.ncp_configured: zdo_flags=0x3 stack_profile=2 security_level=5
04:31:09.691 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.reopened: port=/dev/ttyUSB0
04:31:09.691 [integration-zigbee-0] INFO  c.h.integration.zigbee.PortWatchdog -- zigbee.port_reopened: recovery succeeded after 2 failed attempts
04:31:23.291 [hs-shutdown] INFO  io.javalin.Javalin -- Stopping Javalin ...
04:31:23.292 [hs-shutdown] INFO  org.eclipse.jetty.server.Server -- Stopped Server@6c1832aa{STOPPING}[11.0.25,sto=0]
04:31:23.295 [hs-shutdown] INFO  o.e.jetty.server.AbstractConnector -- Stopped ServerConnector@12b5454f{HTTP/1.1, (http/1.1)}{127.0.0.1:7070}
04:31:23.296 [integration-zigbee-0] WARN  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.transport_failed: serial read error: port dead or closed; lastFrame=DATA(frm=3, ack=6, reTx=false) retransmits=0 crcRejects=0 timeouts=0 — the watchdog owns recovery
04:31:23.297 [integration-zigbee-0] WARN  c.h.integration.zigbee.PortWatchdog -- zigbee.port_unhealthy: cause=read-error; reopen scheduling started
04:31:23.301 [hs-shutdown] INFO  o.e.j.server.handler.ContextHandler -- Stopped o.e.j.s.ServletContextHandler@31ff6309{/,null,STOPPED}
04:31:23.307 [hs-shutdown] INFO  io.javalin.Javalin -- Javalin has stopped
04:31:24.892 [integration-zigbee-0] INFO  c.h.integration.zigbee.AshSession -- ASH session connected: ashVersion=2 resetCode=0xb
04:31:24.897 [integration-zigbee-0] INFO  c.h.i.zigbee.EzspCoordinatorProtocol -- EZSP session negotiated: protocolVersion=13 stackType=2 stackVersion=0x7450
04:31:24.953 [integration-zigbee-0] WARN  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.ncp_config_skipped: id=0x1 status=0x37
04:31:24.960 [integration-zigbee-0] WARN  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.ncp_config_skipped: id=0x6 status=0x35
04:31:24.978 [integration-zigbee-0] INFO  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.ncp_configured: zdo_flags=0x3 stack_profile=2 security_level=5
04:31:25.002 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.reopened: port=/dev/ttyUSB0
04:31:25.002 [integration-zigbee-0] INFO  c.h.integration.zigbee.PortWatchdog -- zigbee.port_reopened: recovery succeeded after 0 failed attempts
04:31:25.081 [hs-shutdown] INFO  c.h.p.SqlitePersistenceLifecycle -- WAL checkpoint completed: database=/home/homesynapse/hs-bench/data/homesynapse-events.db
04:31:25.082 [hs-shutdown] INFO  c.h.persistence.DatabaseExecutor -- Shutting down DatabaseExecutor
04:31:25.082 [hs-shutdown] INFO  c.h.persistence.DatabaseExecutor -- DatabaseExecutor shutdown complete
04:31:25.082 [hs-shutdown] INFO  c.h.p.SqlitePersistenceLifecycle -- Persistence layer stopped: database=/home/homesynapse/hs-bench/data/homesynapse-events.db
04:31:25.083 [hs-shutdown] INFO  c.h.lifecycle.HomeSynapseCore -- HomeSynapseCore stopped: db=/home/homesynapse/hs-bench/data/homesynapse-events.db (SIGTERM)
```

Transcription notes: (a) api-captures/post-window JSON above is reformatted (indent/line-wrap) from `python3 -m json.tool` output for readability — values byte-identical to the paste; (b) command 3's ===RESOLVED section is condensed to its load-bearing values (the paste carried the full 3238-byte file; nothing extracted here differs from it); (c) command 8's 08-02 second "evidence lines" duplicate of the truncated JSON is elided as marked; (d) MINGW64 prompt lines trimmed. All timestamps, ids, phases, verdicts, and log lines are verbatim.
