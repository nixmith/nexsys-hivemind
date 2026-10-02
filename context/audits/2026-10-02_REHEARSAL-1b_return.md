# REHEARSAL 1b — return
Thu 2026-10-01 18:25 CT → overnight break (Nick asleep after action 6's first silence) → Fri 06:02–06:58 CT at Nick's call. Core 40412f9. Pi times (UTC−4) → CT. Overflow (per-command store map, capture reads, full quotes, full bytes) in reh1b/REHEARSAL-1b_guide-notes.md.

## §0 pre-registrations
P1 HELD — KEY WRITTEN · WARN x5 WRITTEN · carrier now 1363 B; boot 200844 formed=0 resumed=1 relinked=9 permit=1 bad-key=0; projection devices=9 entities=9 position=201201; hero: 1.
P2 HELD, both halves — Thu 20:04:28 (210350): announce nwk=0x3627 → proposed SONOFF SNZB-06P24 profile=null COMPLETE source=announce; no interview_failed; no proposal_accepted. Fri 06:10:41 (070945, fresh association nwk=0xd923): announce → proposed → proposal_accepted source=config → endpoint_classified → device_adopted deviceId=01M3Y4YA6KMH7JDEF5YMMJ3YND entities=1 → reporting_configured, 0.56 s.
P3 HELD — endpoint=1 deviceType=0x107 inputClusters=[0x0, 0x3, 0x400, 0x406, 0xfc11, 0xfc57] entityType=BINARY_SENSOR capabilities=[occupancy, illuminance_measurement, identify]; API attributes illuminance_lux + occupied.
P4 REFUTED on posture, HELD on cadence — reporting_configured clusters=2 verified=1 degraded=1 (no line names the cluster); lux report ≈6 s after uncovering (age=24s at +30 s).
P5 HELD, LOG-SCALE arm — covered 0.0 (room dark, 06:29); uncovered + lights on 39.9 lux (ver 15→22). Direct-lux arm absent. Hue comparison NOT-REACHED.
P6 HELD on its claim, with anomalies — run 01M3Y71A4CJJ8ZSMFF9W74S329 bench-hero triggeredAt 06:47:16.7 CT COMPLETED; store > 851999: command_issued 5 · command_dispatched 5 · command_confirmation_timed_out 3 · command_result 2 · state_confirmed 0. Timeouts +5.79 s (turn_on), +5.78 s (set_brightness), third at +17.8/+15.8 s (cmd3/cmd4, both set_color_temperature); command_result 1 ms after cmd4's dispatch (no log line) and 17 ms after identify's; automation_completed 1 ms after identify's dispatch, three commands without a terminal (map: notes §A6).
P7 HELD — WINDOW KEY REMOVED · adopt_devices 10; carrier restored IDENTICAL a239bd60b40a · key-lines=0 · warn-lines=0; closed boot 075042 devices=10 entities=10 position=849602 (>201201); formed=0 resumed=1 relinked=10 permit=0; hero: 1; store-after 852331|852331 integrity ok; Bearer 0.
Read from the capture (notes §A): key_established VERIFY_KEY_SUCCESS at both joins · device_left ×3 Thu 20:18:25 CT after the "pairing step" fallback on a joined unit · USB-cycle gave no device_announce from this device · key_establishment_failed device=0xFFFF… WARN ≈4:57 after every permit_join_opened (transient key expiry) · every run logs command_result identify "DefaultResponse SUCCESS +90 ms, then no report, ever" 17–21 ms after dispatch (Hue reachable, or canned?) · Fri 03:30 nightly ran on the edited configs.

## §1 SAY lines (verbatim, decisive lines)
1: pairing step: device sitting in position on the counter, fully charged, accessible and in-reach of USB-C charger (as necessary). Have not pressed or done anything else.
2: ssh: connect to host hs-dev-1 port 22: Connection timed out
2 (re-run): clone: 40412f9 · pid 43101 · boot 043137 · pi-clock 23:56:15Z | key-lines=0 · adopt=9 · warn-lines=0 · carrier a239bd60b40a 1208 B | backups: 6b40ad3647c3 a239bd60b40a | store-before: 803342|803342 integrity ok | hero: 1 | entities-before: 9 rows; 8 AVAILABLE; 9 devices; unavailable: ['DHE40F']
3: KEY WRITTEN · WARN x5 WRITTEN · carrier now 1363 B | boot 200844 | projection_live: devices=9 entities=9 position=201201 | formed=0 resumed=1 relinked=9 permit=1 bad-key=0 | 20:09:04.149 Pi permit_join_opened: duration=254s | hero: 1
4: nothing in 240 s (twice; window closed 19:13:18). After restart (boot 210350, permit 21:04:09 Pi): 21:04:28.415 device_announce: device=0xA4C13814CE41FFFF nwk=0x3627 | .606 device_proposed: … manufacturer=SONOFF model=SNZB-06P24 profile=null status=COMPLETE source=announce
5: PROPOSED 0xA4C13814CE41FFFF | manufacturer= SONOFF | model= SNZB-06P24 | status= COMPLETE | ADOPT LIST WRITTEN: 9 + 1 | boot bench-2026-10-01-210942.log · formed=0 resumed=1 relinked=9 permit=1
6 (Thu): nothing in 240 s. 6 (Fri, cp + restart, boot 070945, permit 07:10:05.721 Pi): 07:10:41.193 device_announce nwk=0xd923 | .361 device_proposed … COMPLETE | .362 proposal_accepted source=config | .373 endpoint_classified (the line in §0 P3) | .409 device_adopted entities=1 | .748 reporting_configured clusters=2 verified=1 degraded=1
S0 (Fri, added): boot 043007 | key-lines=1 · adopt=10 · warn-lines=5 · carrier 9161dd3e5979 1363 B | sensor last_link_at 01:17:38Z then '-' | formed=0 resumed=1 relinked=9 permit=1 · position=201201 | hero: 1 | 9 rows; 8 AVAILABLE; 9 devices
7: entities now: 10 rows; 10 devices; new: 1 | NEW 01M3Y4YA6YSYQWVE9ET8FT4HWQ AVAILABLE stale False | state: illuminance_lux 0.0, occupied false, stateVersion 10, lastReported 06:11:51 CT
8: covered 06:29:21 ±5 s · lux=0.0 ver=13 age=104s | 8b: lux=0.0 ver=15 age=240s / age=267s · lights off, dawn
9: uncovered 06:44:03, lights on · lux=39.9 ver=22 age=24s
10: occupied=false (cleared 06:45:01) · max-before-walk: 851999
11: walked at 06:47:21 (6–7 s)
12: occupied=false (cleared 06:48:25) · 01M3Y71A4CJJ8ZSMFF9W74S329 bench-hero 11:47:16.745Z COMPLETED None · rows 852069–852139 (D12.txt)
13: WINDOW KEY REMOVED · adopt_devices 10 | carrier restored: IDENTICAL a239bd60b40a · key-lines=0 · warn-lines=0 | closed boot 075042 | projection_live: devices=10 entities=10 position=849602 | formed=0 resumed=1 relinked=10 permit=0 | hero: 1 | store-after: 852331|852331 integrity ok | Bearer in the capture: 0
14: files 16 · join lines 11 · PRESENCE 0xA4C13814CE41FFFF | SONOFF | SNZB-06P24

## §2 what else Nick said (verbatim, CT; all in notes §B)
18:54 "Login was successful after I clicked the link and logged into Tailscale" (Pi: up 12 days, tailscaled active, "Logged out."). 19:52 "It keeps blinking red, even when I would press/hold the button." 20:06 "the TR3 has an adapter plugged into it … I now have that USB-C plugged to the sensor." 20:26 "it kept blinking when plugged back in". 06:02 "I fell asleep … I want to continue". 06:12 "it blinked 5 times, then made a solid LED light, then went away." 06:35 "Lights are off but the natural light … is improving quickly". 06:53 "keep plugged in, do not remove power now."

## §3 guide's departures
- Action 1's SAY gave the rig state; the pairing step was read from Nick's manual pages (reh1b/manual/).
- 18:48–18:56 ssh timeout (Pi's Tailscale logged out): one LAN ssh (HostName override) read uptime/tailscaled/status; Nick re-authenticated; action 2 re-run unchanged. Recommend disabling key expiry for hs-dev-1.
- Action 4 run after the window closed; the packet's restart re-open used (boot 210350).
- Action 6 Thu: restart re-open added; the "hold 5 s" fallback caused the leave. Nick fell asleep before the retry; configs stayed edited through the Fri 03:30 nightly (the 21:00 hard stop could not run unattended).
- Fri continuation at Nick's call: S0 read added; Thu boot logs 200844/210350/210942 copied into ~/reh1b (else lost from the 4-newest copy); action 6 retry with restart.
- Action 8 one extra read; action 9 lights turned on before uncovering.
- Fri captures derived $D=fri1002; moved into thu1001/reh1b/ (empty fri1002/reh1b/ left). Notes + manual/ added at Nick's request.

## §4 files under _scratch/v90/thu1001/reh1b/ (bytes)
A2.txt 314 · A3.txt 1264 · B5.txt 616 · S0-friday-state.txt 4644 · B7.txt 582 · D12.txt 2321 · E13.txt 1290 · REHEARSAL-1b_guide-notes.md 8423
pi-capture/ (16): bench logs 200844 44670 · 210350 17362 · 210942 174420 · 043007 56810 · 070945 36455 · 075042 10216 · entities-before/joined/after.json 1600/1768/1768 · homesynapse.yaml.before 1208 · zigbee.yaml.before/after 571/659 · join-boot-log.path 55 · join-lines.txt 1882 · new-entity.txt 27 · presence.txt 50
manual/ (9): png 01–08 55347/35057/39383/29016/49890/139495/168059/89465 · SNZB-06P24_manual-notes.md 3651
RETURNED _scratch/v90/thu1001/REHEARSAL-1b_return.md 8168
