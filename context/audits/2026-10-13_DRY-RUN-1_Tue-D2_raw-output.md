<!--
file: context/audits/2026-10-13_DRY-RUN-1_Tue-D2_raw-output.md
purpose: dry-run #1's D2 raw output (`_scratch/v107/dr1/D2.txt`, 3,532 B, md5 ea986e69301ac8e03db6cf351ed89d60; Nick's tee of his own shell, Tue 2026-10-13 19:42:27 CT), verbatim — the evidence behind the v111 b1 intake. No guide notes exist for D2 (the deviation ruled in the audit §3).
state-type: evidence (verbatim; never edited)
-->
# DRY-RUN-1 (Tue) — D2 raw output

## D2.txt (3532 B)
```
=== D2 2026-10-14T00:42:27Z
LOG1=bench-2026-10-12-210302.log from MARK1=11406 · LOG2=bench-2026-10-13-043250.log (the nightly's boot — whole) · window-bytes=696443 pi-clock 2026-10-14T00:42:27Z deployed=37f05a9
timedatectl: NTPSynchronized=yes TimeUSec=Tue 2026-10-13 20:42:27 EDT 
formed=0 resumed=1 relinked=10 launched=1 startup_failed=0 ash-LOG1=33 ash-LOG2=80
nightly boot: 04:32:52.749 [main] INFO  c.h.persistence.SqliteStateStore -- Loaded 10 entities from checkpoint for view state_projection at position 1907319; projectionVersion=5 04:33:22.654 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c 
G4-1 dark=0 up=0 pings=0 outcomes=[] seen-during-probe-true=0
G4-2 dark=0 up=0 pings=0 outcomes=[] seen-during-probe-true=0
TR3 dark=0 up=0 pings=0 outcomes=[] seen-during-probe-true=0
S31 dark=0 up=0 pings=1136 outcomes=[ 1135 outcome=ok  1 outcome=timeout ] seen-during-probe-true=1135
HUE dark=0 up=0 pings=0 outcomes=[] seen-during-probe-true=0
FLAPS(fleet-of-five, available=false lines, the Hue excluded)=0 CEILING=4
17:37:03.324 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.availability_ping: device=0x00124B002FA8D1C5 nwk=0xF87D ep=1 outcome=timeout rttMs=5019 seen_during_probe=false
store since POS1=1877415: state_reported=63050 state_changed=31241 automation_action_completed=504 automation_action_started=504 automation_completed=56 automation_triggered=56 command_dispatched=7 command_issued=7 command_confirmation_timed_out=3 integration_started=3 integration_stopped=3 command_result=2 state_confirmed=2 
POS2=1972853 rows-24h=95438
du: /home/homesynapse/hs-bench/data/homesynapse-events.db=989450240 /home/homesynapse/hs-bench/data/homesynapse-events.db-wal=4202432 /home/homesynapse/hs-bench/data/homesynapse-events.db-shm=32768  dir=993696053 free=100291231744 card= 117G 94G 17%
registry rows=10 unavailable=['DHE40F']
SENSOR availability=AVAILABLE reason=frame_received lastSeenAt=2026-10-08T22:10:38.556395459Z link={'lqi': 240, 'rssiDbm': -40, 'at': '2026-10-08T22:10:38.556395459Z'}
HUE availability=UNAVAILABLE reason=None lastSeenAt=None link=None
sensor frames per 10-min window: 0 5 5 6 5 2 1 3 3 0 1 0 0 0 1 5 6 0 2 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0 1 0 1 0 6 0 0 0 1 0 1 0 0 0 1 0 1 0 0 3 1 0 8 6 6 8 16 8 1 2 2 2 3 4 2 4 4 5 6 12 19 28 31 12 3 5 2 1 2 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 0 1 0 13 6 1 0 0 0 0 2 3 4 4 2 1 2 6 2 1 0 2 6 1 6 6 
automation runs in the window: 56
nightly digest (last 2 lines): 
2026-10-12 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · fleet: 10/10 · re-seen 10 · avail: 9/10 · bench-hero RESTORED ✓ · ON-latency 0.28s
2026-10-13 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · fleet: 10/10 · re-seen 10 · avail: 9/10 · bench-hero RESTORED ✓ · ON-latency 0.31s
IR-56 read (D-v85-12's row, from LOG1 after D1's launched at line 51): 21:03:25.886 [integration-supervisor-start] INFO  c.h.i.r.StandardIntegrationSupervisor --
IR-56 G4-1 links: 
IR-56 G4-1 first-summary: 21:13:25.888 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.link_summary: device=0xAC
IR-56 G4-2 links: 
IR-56 G4-2 first-summary: 21:13:25.888 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.link_summary: device=0xAC
IR-56 TR3 links: 
IR-56 TR3 first-summary: 21:13:25.888 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.link_summary: device=0x4C
=== D2 end 2026-10-14T00:42:27Z
```
