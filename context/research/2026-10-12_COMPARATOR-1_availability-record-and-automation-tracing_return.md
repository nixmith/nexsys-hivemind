<!--
file: context/research/2026-10-12_COMPARATOR-1_availability-record-and-automation-tracing_return.md
purpose: §1 pre-registrations adjudicated at pinned revisions; automation tracing; safe wording (the hub updates the register).
status: RETURNED 2026-10-12 CT (date -u at start 19:39:02Z = 14:39 CT)
-->
# COMPARATOR-1 — availability record and automation tracing

## §0 Verdicts
| # | Claim (pre-read) | Verdict | Revision |
|---|---|---|---|
| 1 | Z2M 10-min silence timer, then genBasic read ×2, 3 s apart; retained on change; passive 1,500 min unpinged; off by default | CONFIRMED + qualifiers (§1) | Z2M@344b6e03, Z2MD@fffda0aa, ZH@78424d4f |
| 2 | ZHA 7,200 s / 21,600 s; 30-45 s loop; one Basic `manufacturer` read per cycle; unavailable after 2 missed | CONFIRMED + qualifiers (§1) | ZHA@2d2e88eb |
| 3a | Z2M: no probe history (memory; failed pings at warning) | CONFIRMED; warning lines reach the default file log | Z2M@344b6e03 |
| 3b | ZHA: no probe history (memory) | CONFIRMED for the library; its HA host stores each transition | ZHA@2d2e88eb, HA@adb4367f |
| 3c | SmartThings: a state + `lastUpdatedDate` | CONFIRMED | ST, STS@e43dda5e |
| 3d | deCONZ (pre-read NOT FOUND) | CONFIRMED at source: latest `reachable` + `lastseen`; no reachability history | DZ@a4c17adf, DZD@12daa453 |
| 3e | Hubitat (pre-read NOT FOUND) | NOT FOUND: no probe-outcome record in the docs read | HUB |
| 4 | "no structured, queryable per-probe history in the sources checked" | CONFIRMED; add the transition qualifier (S1) | all above |
| T1 | HA traces: 5 per automation; `.storage/trace.saved_traces` | CONFIRMED; written at HA stop | HA@adb4367f |
| T2 | HA: fired-but-condition-false is traced | CONFIRMED (`failed_conditions`) | HA@adb4367f |
| T3 | HA: a trigger that did not fire is not traced | REFUTED in part: "Did not trigger" traces since 2026.7.0 | HA@adb4367f, tags 2026.6.0/7.0 |

## §1 Availability axis
**Zigbee2MQTT.** Off by default (settings.ts:37), or per device (utils.ts:264-268). Active: timer = 10 min + 1 s + jitter ≤ 30 s, reset by any message (availability.ts:94-122, 287-293); then a genBasic `zclVersion` read (ZH device.ts:1436-1442), 2 tries 3 s apart if last published online, else 1 (:156-176); failure publishes `offline`, retained, on change (:262-276). Backoff (default on): next ping ×1.5, ×3, ×6… (:183-194). Passive: offline after 1,500 min + 1 s silent, never pinged (:123-127). Record: timers, state, backoff in in-memory Maps (:26-35); one `lastSeen` per device in database.db (ZH device.ts:685); the retained topic; a `warning` line per failed try (:169) in the default file log (settings.ts:94-97; 3 × 10 MB per run, 10 runs kept: logger.ts:99-103, 225-241); success at debug (:166).

**ZHA.** 7,200 s mains / 21,600 s battery (const.py:78-79; helpers.py:343-348). Loop interval drawn once in 30-45 s (helpers.py:505-558; decorators.py:58-73), after startup (gateway.py:383-391). Past it: one uncached Basic `manufacturer` read per cycle; a reply resets the count; after 2 missed, unavailable next cycle (device.py:106, 819-867); LUMI and endpoint-less devices go unavailable unread (:838-861). Record: state, miss count in memory; probe steps at debug (:845-857); one `last_seen` per device in zigpy SQLite (ZP appdb.py:340-351). **In Home Assistant** it is stored: entity state `unavailable` (HA entity.py:1105-1108) and `zha_event` `device_offline` (ZHA device.py:893-902; HA zha/helpers.py:459-483), recorded 10 days by default (recorder/__init__.py:109, core.py:285-319), read by REST `/api/history/period` (history/__init__.py:57): transitions, not probes.

**SmartThings.** Opt-in (`healthCheck`). ONLINE / UNHEALTHY ("inactive longer than its designated health check interval") / OFFLINE ("a device with UNHEALTHY status cannot be contacted by the platform"); `checkInterval` an integer 0-604800, unit not stated. Record: `GET /devices/{deviceId}/health` → `state` + `lastUpdatedDate`, "the timestamp of the last known state change"; no health-history endpoint in the API reference; SDK enum ONLINE/OFFLINE/UNKNOWN (devices.ts:807-811).

**deCONZ.** DDF devices: `reachable` false after over 16 consecutive failed APS confirms while idle, i.e. its own traffic failing (device.cpp:75, 924-938); no silence timer found. Legacy lights follow the deCONZ core's node FailureState/zombie flag (de_web_plugin.cpp:3366-3378). Record: `reachable`, `lastseen` over REST (DZD lights/index.md:153-160) and websocket (de_web_plugin.cpp:2504, 3300); latest value per item (ON CONFLICT REPLACE, database.cpp:742-749, 788-793); the one time-series table, `zcl_values` (ZCL attribute data), is off by default (de_web_plugin.cpp:664).

**Hubitat.** Zigbee, C-8/C-8 Pro: "Ping inactive devices every 3 hours" (Last Message over 3 h old), "enabled by default", framed as helping devices "stay on" (zigbee-details). Record: per-device Last Message, messages since boot; Last Activity (devices); `HealthCheck` = `checkInterval` + `ping()`, driver-defined (capability-list).

## §2 Automation-tracing axis
| Product | Fires-why recorded? | Didn't-fire-why recorded? | Confirmed? | Where | Retention | Read how | Source + revision |
|---|---|---|---|---|---|---|---|
| Home Assistant | Yes: trace = trigger + variables, each condition result, each action's params/error, outcome; plus an `automation_triggered` event with the trigger | Partly: condition false → `failed_conditions` trace with the path; since 2026.7.0, "Did not trigger" traces from new-style numeric entity triggers (5 reason codes: unit/value/threshold invalid); a change evaluated and not matched, or a legacy trigger: no trace | No: call params + raised error; resulting state in the recorder, linked by context id | memory → `.storage/trace.saved_traces` at stop; recorder SQLite | 5 runs + 5 not-triggered per automation (`stored_traces`); no time bound found; recorder 10 d | WebSocket `trace/list`/`get`/`contexts` (admin); UI | HA trace/*, automation/entity.py, entity_trigger.py, script.py:1083-1093; HAD testing.markdown:132-136 |
| Zigbee2MQTT | No engine among the 17 lib/extension files; docs: "a bridge" beside "automation software" | n/a | n/a | n/a | n/a | n/a | Z2M lib/extension/; Z2MD 14_securing.md:18 |
| SmartThings | `POST /rules/execute/{ruleId}` returns `executionId`, `result`, per-action results to the caller; none of the 6 Rules endpoints lists past runs | NOT FOUND | Per-command Success/Failure/Offline in that response; `GET /history/devices` = attribute events | cloud / hub (local) | NOT FOUND | REST | ST API ref; STS rules.ts:308-415, history.ts:96-128 |
| Hubitat Rule 5.1 | Opt-in logs: Events, Triggers, Actions (skipped too) | Opt-in: "Display current values" logs each condition T/F; a false required expression blocks the trigger | Device Events lists the command and its app; a command "is not a guarantee that the device responded" | hub logs; device event history | Past Logs ~1 MB, oldest dropped; device events 11 entries / 31 days default (2.3.1) | UI; Maker API `/devices/[id]/events` | HUB rule-5-1, logs, device-events, release-231, maker-api |
| deCONZ | `lasttriggered` + `timestriggered` per rule (counts when each action's internal call returns 200) | NOT FOUND | No: failed action → debug line, count unchanged | SQLite `rules` table | latest value + count | REST `GET /rules` | DZ rest_rules.cpp:1429-1443, database.cpp:495; DZD rules/index.md:350-376 |
| openHAB | No stored run record: `RuleStatusInfoEvent` RUNNING→IDLE on the bus, its logger ERROR by default | DEBUG "The condition '{}' of rule '{}' is unsatisfied." (default INFO) | events.log item command/state lines; the core command action posts no source | events.log, openhab.log; persistence = item states | 16 MB, 7 archives, rolled at start | log files | OHC RuleEngineImpl.java, ItemCommandActionHandler.java:82; OHX log4j2.xml:20-27, 47, 62; OHD persistence.md:11 |

## §3 Safe wording
‹hub› = the hub cites our code; this lane did not read it.
- **S1.** In the sources checked, Zigbee2MQTT and ZHA hold each device's probe state in memory and one last-seen timestamp per device on disk, and neither stores probe outcomes as structured, queryable records (Zigbee2MQTT writes a warning text line per failed probe; ZHA logs probe steps at debug); where Home Assistant hosts ZHA, its recorder keeps each change to `unavailable` for 10 days by default; the record `{{NAME}}` writes is ‹hub›. Sources: Z2M availability.ts:26-35, 169; ZH device.ts:685; ZHA device.py:819-867; ZP appdb.py:340-351; HA recorder/__init__.py:109.
- **S2.** In the sources checked, SmartThings, deCONZ and Hubitat expose a device's connectivity as a current value or timestamp (SmartThings `state` + `lastUpdatedDate`; deCONZ `reachable` + `lastseen`; Hubitat Last Message / Last Activity), and no endpoint or table holding availability-probe history was found; the record `{{NAME}}` writes is ‹hub›. Sources: ST health page, API ref; DZ database.cpp:742-749; HUB zigbee-details, devices.
- **S3.** In the sources checked, Home Assistant keeps a stored, queryable record of why an automation ran: per automation, the 5 most recent run traces by default (trigger, each condition's result, each action's call parameters or error), in memory, written to `.storage/trace.saved_traces` when Home Assistant stops, read over admin WebSocket commands; the record `{{NAME}}` writes is ‹hub›. Sources: HA trace/const.py:17, __init__.py:57-71, websocket_api.py:49-109; HAD testing.markdown:132-134.
- **S4.** In the sources checked, a non-firing is recorded in bounded cases: Home Assistant traces a run stopped by a failed condition and, from release 2026.7.0, keeps a separate set of 5 "Did not trigger" traces for new-style numeric entity triggers that could not evaluate a change (five reason codes), while a change it evaluates and does not match leaves no trace; Hubitat Rule Machine ("Display current values") and openHAB (DEBUG) write condition evaluations to text logs; the record `{{NAME}}` writes is ‹hub›. Sources: HA automation/entity.py:534-540, 771-813, entity_trigger.py:372, 590-620; HAD testing.markdown:134; HUB rule-5-1; OHC RuleEngineImpl.java:1357-1376.
- **S5.** In the sources checked, Home Assistant and Hubitat record an automation's command as dispatched, not the device's confirmation: Home Assistant's trace keeps the call parameters and any raised error, the resulting state sitting in the recorder linked by context id, and Hubitat's device Events page says a command "is not a guarantee that the device responded"; the record `{{NAME}}` writes differs in kind, not degree: ‹hub: an event-sourced log every projection reads; the non-firing as its own event; confirmation from the device's own report›. Sources: HA script.py:1083-1093, logbook/websocket_api.py:454-459; HAD testing.markdown:182, troubleshooting.markdown:204-212; HUB device-events.

## §4 Not found, by product
- **HA:** a REST read for traces (trace/ registers WebSocket commands).
- **SmartThings:** default check interval; retention of device history; whether `healthStatus` changes reach `/history/devices`; a stored rule/Routine run history.
- **deCONZ:** the core library's node-failure rule (not in deconz-rest-plugin); Phoscon UI NOT READ.
- **Hubitat:** a logs API; whether a failed 3-h ping changes device state; the event-history default after 2.3.1 (later notes NOT READ).
- **openHAB:** REST rule status; JS/Blockly engine logging (NOT READ).

## §5 Sources (read 2026-10-12 19:39-20:20Z; github.com/<repo>/blob/<sha>/<path>)
- **Z2M** Koenkk/zigbee2mqtt @344b6e03b436 (2026-10-02): lib/extension/availability.ts (whole); lib/util/settings.ts:36-40, 91-102; logger.ts:90-106, 225-241; utils.ts:249-269; lib/extension/ listing.
- **Z2MD** Koenkk/zigbee2mqtt.io @fffda0aa5a46 (2026-10-11) (= zigbee2mqtt.io/guide/configuration/device-availability.html): docs/guide/configuration/device-availability.md (whole); docs/guide/installation/14_securing.md:18.
- **ZH** Koenkk/zigbee-herdsman @78424d4f7021: src/controller/model/device.ts:668-694, 1436-1442.
- **ZHA** zigpy/zha @2d2e88eb408a (2026-10-12): zha/application/{const.py:78-79, helpers.py:343-348, 505-558, gateway.py:383-391}; zha/decorators.py:58-90; zha/zigbee/device.py:100-106, 430-446, 819-902.
- **ZP** zigpy/zigpy @2fdc4ab97afc: zigpy/appdb.py:340-351.
- **HA** home-assistant/core @adb4367fb465 (2026-10-12), homeassistant/components/{trace/*.py (whole), automation/trace.py, automation/entity.py:458-600, 750-841, recorder/__init__.py:109, recorder/core.py:285-320, history/__init__.py:57, logbook/websocket_api.py:454-506, zha/entity.py:121-123, zha/helpers.py:455-483}; homeassistant/helpers/{trigger/__init__.py:585-740, trigger/models.py:53-71, trigger/entity_trigger.py:180-210, 300-380, 580-710, script.py:1050-1100, entity.py:1100-1110}. Tags: 2026.6.0 @836740c247b3 (trace/models.py lacks `not_triggered`); 2026.7.0 @f474e1d59a97 (automation/__init__.py:901-973 has it); 2026.10.1 @abe1fdd7cd6b (has it).
- **HAD** home-assistant/home-assistant.io @7c990c884748: source/_docs/automation/testing.markdown:130-200; troubleshooting.markdown:120-132, 186-215.
- **ST** developer.smartthings.com/docs/ (no page date; read 2026-10-12 ~20:00Z): devices/health (whole); api/public (Rules endpoints; device health); automations/rules; devices/capabilities/capabilities-reference (healthCheck).
- **STS** SmartThingsCommunity/smartthings-core-sdk @e43dda5ebc79: src/endpoint/devices.ts:544-549, 805-817, 1168-1180; rules.ts:286-415; history.ts:1-140.
- **HUB** docs2.hubitat.com/en/ (page updated-at; whole pages; UI = user-interface): UI/settings/zigbee-details (2024-05-23); developer/driver/capability-list (2026-09-29); UI/devices (2026-09-20); UI/devices/device-detail, UI/devices/device-events, UI/advanced-features/logs (2026-09-28); apps/rule-machine/rule-5-1, apps/maker-api (2026-09-28); UI/apps/app-events (2025-08-01); release-notes/release-231 (2022-07-03).
- **DZ** dresden-elektronik/deconz-rest-plugin @a4c17adfa04a (2026-09-10): device.cpp:70-75, 876-938; de_web_plugin.cpp:664, 2495-2504, 3355-3385; database.cpp:478-800, 1340-1380; rest_rules.cpp:1313-1443.
- **DZD** dresden-elektronik/deconz-rest-doc @12daa4539c4d (2024-10-16): docs/endpoints/rules/index.md:340-385; docs/endpoints/lights/index.md:40-160.
- **OHC** openhab/openhab-core @7c3a2c5bcd44: bundles/org.openhab.core.automation/…/internal/RuleEngineImpl.java:587-590, 1120-1160, 1357-1380, …/module/handler/ItemCommandActionHandler.java:82; bundles/org.openhab.core/…/items/events/ItemCommandEvent.java:65-72.
- **OHX** openhab/openhab-distro @eb03f5770644 (2026-10-08): distributions/openhab/src/main/resources/userdata/etc/log4j2.xml:9-71.
- **OHD** openhab/openhab-docs @7ad33529a5df (2026-08-27): src/configuration/persistence.md:6-16; src/administration/logging.md:185.
RETURNED nexsys-hivemind/context/research/2026-10-12_COMPARATOR-1_availability-record-and-automation-tracing_return.md 14992
