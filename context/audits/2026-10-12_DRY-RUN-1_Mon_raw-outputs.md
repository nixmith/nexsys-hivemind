<!--
file: context/audits/2026-10-12_DRY-RUN-1_Mon_raw-outputs.md
purpose: dry-run #1's Monday raw outputs (`_scratch/v107/dr1/`), concatenated verbatim with one header each — the evidence behind the v110 b2 intake. F1.txt's one cp1252 byte (0x97 at offset 1280, the WALK line's dash) is transcoded to U+2014 here and nowhere else.
state-type: evidence (verbatim; never edited)
-->
# DRY-RUN-1 (Mon) — raw outputs

## D0a.txt (765 B)
```
=== D0a 2026-10-13T00:30:49Z
LOG0=bench-2026-10-12-043246.log MARK0=494463 pi-clock 2026-10-13T00:30:49Z deployed=37f05a9 ref=HEAD bench=cddac94
timedatectl: Timezone=America/New_York NTPSynchronized=yes TimeUSec=Mon 2026-10-12 20:30:49 EDT 
formed=0 relinked=10 pings-so-far=765 dark-so-far=0 startup_failed=0
DB=/home/homesynapse/hs-bench/data/homesynapse-events.db
du: /home/homesynapse/hs-bench/data/homesynapse-events.db=940638208 /home/homesynapse/hs-bench/data/homesynapse-events.db-wal=4202432 /home/homesynapse/hs-bench/data/homesynapse-events.db-shm=32768  dir=944884021 free=101282185216 card= 117G 95G 16%
retention keys (the config, read-only): 
home_id: 
POS0=1875960 rows=1875960 avail-rows-total=481 presence-rows=0
=== D0a end 2026-10-13T00:30:49Z
```

## D0b.txt (504 B)
```
=== D0b 2026-10-13T00:40:02Z
DB=/home/homesynapse/hs-bench/data/homesynapse-events.db rows-now=1876566
method: the online backup API in ONE step (python3 sqlite3 backup, pages=-1; the guide amendment Nick approved) - the sqlite3 CLI .backup restarts on every concurrent write
backup: 28 s bytes=940978176 md5-pi=6dfd6e3c7441fb5a224b7ee666cc0d16 integrity-pi=ok copy-rows=1876566 free-after=100340580352
=== D0b end 2026-10-13T00:40:40Z
scp: 16 s bytes=940978176 md5-desk=6dfd6e3c7441fb5a224b7ee666cc0d16
```

## K4.txt (194 B)
```
=== K4 2026-10-13T00:42:32Z core=176adad copy-bytes=940978176 md5=6dfd6e3c7441fb5a224b7ee666cc0d16
presence-rows=0 rows=1876566 types=23
BUILD SUCCESSFUL in 17s
=== K4 end 2026-10-13T00:42:52Z
```

## F1.txt (1339 B)
```
=== F1 2026-10-13T00:47:37Z
columns: global_position event_id home_id event_type schema_version ingest_time event_time subject_ref subject_type subject_sequence priority origin actor_ref idempotency_key correlation_id causation_id event_category payload_size batch_id external_ref intent_kind logical_time node_id payload chain_hash payload_iv dek_ref
total=1876566 first=None last=None
type state_reported=1202395
type state_changed=631933
type automation_action_completed=14364
type automation_action_started=14364
type command_dispatched=3009
type command_issued=3009
type command_confirmation_timed_out=1714
type automation_completed=1596
type automation_triggered=1596
type command_result=1129
type availability_changed=481
type integration_started=346
type integration_stopped=317
type state_confirmed=185
type integration_restarted=28
type device_discovered=22
type integration_health_changed=18
type join_rejected=18
type device_adopted=10
type device_registered=10
type entity_registered=10
type permit_join_closed=6
type permit_join_opened=6
avail-rows=481
SCAN rows=1876566 payload-bytes=236209434 seconds=1.21 (the desk; the replay floor is read on the copy, never the live store)
WALK rows=1876566 seconds=1.07 (every row read in log order — A4's floor on the desk)
=== F1 end 2026-10-13T00:47:42Z
```

## D1-pre_sudo.txt (99 B)
```
=== D1-pre 2026-10-13T00:50:31Z user=homesynapse
sudo-n: OK (passwordless) - D1 can drop the cache
```

## D1.txt (2815 B)
```
=== D1 2026-10-13T00:51:32Z pi-clock
  [OK] stopped
1274 login -- homesynapse
12117 sshd-session: homesynapse [priv]
page cache dropped: used=550M free=3265M cache=326M
--- health tokens (current boot: /home/homesynapse/hs-bench/bench-2026-10-12-205143.log) ---
--- failure tokens ---
20:52:32.568 [main] ERROR c.h.lifecycle.HomeSynapseCore -- lifecycle.startup_failed: phase=CORE_DOMAIN subsystem=state-store recommendation="inspect the log and the JFR recording; report with the phase and subsystem named" — tearing down initialized subsystems
HomeSynapse Core exiting: code=99 (UNEXPECTED_ERROR) — inspect the log and the JFR recording; report with the phase and subsystem named
COLD LOG=bench-2026-10-12-205143.log
COLD: startup_failed at +91 s (the EXPECTED exit 99 arm)
20:51:47.130 [main] INFO  c.h.persistence.SqliteStateStore -- Loaded 10 entities from checkpoint for view state_projection at position 1877389; projectionVersion=5
20:52:32.568 [main] ERROR c.h.lifecycle.HomeSynapseCore -- lifecycle.startup_failed: phase=CORE_DOMAIN subsystem=state-store recommendation="inspect the log and the JFR recording; report with the phase and subsystem named" — tearing down initialized subsystems
java.lang.IllegalStateException: registry projection did not reach LIVE within ~30s during startup
20:52:32.636 [main] INFO  c.h.lifecycle.HomeSynapseCore -- HomeSynapseCore stopped: db=/home/homesynapse/hs-bench/data/homesynapse-events.db (startup failure: registry projection did not reach LIVE within ~30s during startup)
HomeSynapse Core exiting: code=99 (UNEXPECTED_ERROR) — inspect the log and the JFR recording; report with the phase and subsystem named
COLD status:   [!!] NOT running
W1: relaunch (warm)
--- health tokens (current boot: /home/homesynapse/hs-bench/bench-2026-10-12-205319.log) ---
--- failure tokens ---
20:54:02.530 [main] ERROR c.h.lifecycle.HomeSynapseCore -- lifecycle.startup_failed: phase=CORE_DOMAIN subsystem=state-store recommendation="inspect the log and the JFR recording; report with the phase and subsystem named" — tearing down initialized subsystems
HomeSynapse Core exiting: code=99 (UNEXPECTED_ERROR) — inspect the log and the JFR recording; report with the phase and subsystem named
LOG1=bench-2026-10-12-205319.log MARK1=4068 pi-clock 2026-10-13T00:55:10Z
20:53:21.737 [main] INFO  c.h.persistence.SqliteStateStore -- Loaded 10 entities from checkpoint for view state_projection at position 1877389; projectionVersion=5
20:54:02.530 [main] ERROR c.h.lifecycle.HomeSynapseCore -- lifecycle.startup_failed: phase=CORE_DOMAIN subsystem=state-store recommendation="inspect the log and the JFR recording; report with the phase and subsystem named" — tearing down initialized subsystems
POS1=1877395
W1 status:   [!!] NOT running
=== D1 end 2026-10-13T00:55:11Z
```

## D1-W2.txt (1666 B)
```
=== D1-W2 2026-10-13T01:02:31Z pi-clock (W1-CONTINGENCY yes: the read-only pre-warm, then W1 again - one start)
pre-warm 01:02:31Z /home/homesynapse/hs-bench/data/homesynapse-events.db=941400064 /home/homesynapse/hs-bench/data/homesynapse-events.db-wal=0 
Mem:            4049         537        2662          36         943        3511
pre-warm done 01:03:02Z
Mem:            4049         553        2294          36        1296        3495
W1 again: relaunch (warm)
21:03:25.834 [integration-supervisor-start] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.adoption_maps_rehydrated: devices=10
21:03:33.596 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
21:03:33.596 [integration-zigbee-0] INFO  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.network_up: stackStatusHandler reported EMBER_NETWORK_UP (buffered)
--- failure tokens ---
LOG1b=bench-2026-10-12-210302.log MARK1b=11406 pi-clock 2026-10-13T01:03:53Z
21:03:04.337 [main] INFO  c.h.persistence.SqliteStateStore -- Loaded 10 entities from checkpoint for view state_projection at position 1877389; projectionVersion=5
21:03:24.758 [hs-sub-registry_projection] INFO  c.h.l.RegistryProjectionSubscriber -- registry.projection_live: devices=10 entities=10 position=849602
21:03:33.596 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
21:03:33.596 [integration-zigbee-0] INFO  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.network_up: stackStatusHandler reported EMBER_NETWORK_UP (buffered)
POS1b=1877415
W2 status:   [OK] running (pid 12899)
=== D1-W2 end 2026-10-13T01:03:53Z
```

## K4 XML (the IT's evidence; 3790 B)
```
tests="1" skipped="0" failures="0" errors="0"
registry-cold.k4: source=C:\Users\Nick\hs-bench\backups\homesynapse-events-2026-10-12.db bytes=940978176 wal_bytes=0
```
