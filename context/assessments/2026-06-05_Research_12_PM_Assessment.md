<!--
file: context/assessments/2026-06-05_Research_12_PM_Assessment.md
purpose: PM assessment of Research 12 (Zigbee adapter de-risk, M14). First research for the highest-risk milestone.
audience: Nick, PM
state-type: assessment
status: v1 — PM-reviewed 2026-06-05. Identifier discipline verified (no module-info proposals, EntityRole/matrix vocabulary correct, §7 LIGHT honored). Nick decision PENDING on the dual-coordinator spike scheduling.
-->

# Research 12 — PM Assessment

**Grade: A.** The strongest research return to date. Primary-source-dense (GitHub issues with numbers, verbatim maintainer quotes, vendor docs), positioned throughout, zero identifier fabrications (it proposed no module names — §7 LIGHT honored exactly; the Q10 table uses HomeSynapse vocabulary and **every row passes the 6×3 legality matrix** — PM-checked by inspection). The brief's framing held: Doc 08 stays Locked; output = nine amendment candidates (REC-120..128 + 129) for the M14 briefing, each with LOC + gate-severity.

## Headline findings the PM endorses
1. **Transport before devices.** The 80/20 inversion (transport/transaction layer + quirk data model >> ZCL correctness) should dictate M14's internal milestone ordering: REC-120 (per-device serialized transaction queue) and REC-121 (SED queue-until-awake) are the two CRITICAL items and land FIRST, before any device support. openHAB's `ZigBeeTransactionManager` (per-node queue, maxOutstanding=1, bounded retries) is the JVM-native pattern to steal.
2. **The openHAB anti-pattern is the existential one.** Compiled-Java-converter-per-device is the documented root cause of its small catalogue. REC-122's data-file DeviceProfile (declarative JSON; **named compiled parse-handlers referenced by string key** — LTD-17-safe, the deCONZ DDF `parse.fn` model) is the right architecture; deCONZ's DDF-bundle decoupling (versioned, hashed, signed, shippable out-of-band) is "the single most important idea to steal." PM concurs.
3. **Dual-coordinator has NO field precedent (§5.2).** None of the surveyed platforms aggregate two coordinators; openHAB is strictly 1:1. Doc 08's dual-coordinator requirement therefore has no reference design to copy — this is the highest-uncertainty M14 area and needs a **dedicated design spike well before M14** (recommend ~Aug, before the M14 briefing) rather than discovery during the milestone.
4. **Q10 delivered.** The §7.4 EntityRole classification table is adoption-ready for the adapter-author guide and discharges the deferred AMD-44 §6 HA-reclassification survey. The "config affordances are SWITCH-typed CONFIG entities" consequence of the matrix (PLUG is PRIMARY-only) is correctly derived and becomes adapter-author doctrine. HA's churn evidence (battery/LQI flips breaking dashboards) justifies classifying correctly at first proposal.

## REC dispositions (all target the M14 briefing; AMD integers assign-at-milestone)

| REC | Disposition | Severity | PM note |
|---|---|---|---|
| REC-120 transaction queue | **ACCEPT** | CRITICAL | First M14 WU. ReentrantLock + VT per LTD-11. |
| REC-121 SED queue-until-awake | **ACCEPT** | CRITICAL | Second M14 WU; covers interview/reporting/IAS flows; 7.68 s parent-hold documented. |
| REC-122 device-profile data files | **ACCEPT** | HIGH | §7.2 schema sketch is the seed; profile `role` field aligns with `ProposedEntity.entityRole` (B-S2). Profile signing/validation note (§5.6) folds in. |
| REC-123 firmware gate + backup | **ACCEPT** | HIGH | Actionable startup error + portable backup record. Firmware baselines re-verify at M14 start (§5.1). |
| REC-124 Tuya DP codec as data | **ACCEPT** | HIGH | seq tracking, time-sync, magic packet, McuVersionResponse battery fix — all evidence-cited. |
| REC-125 Xiaomi TLV | **ACCEPT** | MED-HIGH | Don't trust the ZCL datatype (CHARACTER_STRING lie). |
| REC-126 IAS auto-enroll | **ACCEPT** | HIGH | Enroll failure aborts interview — gate-visible. |
| REC-127 route-aware telemetry | **ACCEPT** | MEDIUM | Alert on delivery-failure rate + route churn, never raw LQI/RSSI thresholds; informs Doc 11/AMD-07 surface too. |
| REC-128 OTA reserve-only posture | **ACCEPT** | LOW now | Adopt the zigbee-OTA index shape as a dormant record; no flashing in MVP. |
| REC-129 channel + join security defaults | **ACCEPT** | MEDIUM | Channel 15/20/25 guidance; install-code + legacy-key fallback + R21 TC-link-key update. |

## Caveats verified/endorsed
§5.1 firmware drift (re-verify at M14); §5.2 dual-coordinator spike (escalated above); §5.4 Tuya TS0601 modelID reuse → manufacturerName-primary fingerprinting (already reflected in §7.2); §5.5 correctly distinguishes our locked matrix from observed HA fact; §5.6 profile signing if profiles ship out-of-band.

## Strategic impact
- **B-S2 (in flight): zero change** — and §7.4 independently validates the EntityRole matrix against field practice.
- **Workstream C (next): freeze proceeds unchanged.** All nine RECs are adapter-internal (M14); none require new integration-api contract surface. The restart-intensity findings corroborate the resolved NQ-5/NQ-6 calls (existing `HealthParameters` + per-descriptor override).
- **M14 planning:** RECs 120/121 fix the milestone's internal ordering (transport-first); REC-122's profile system is the largest single work item (~700–1000 LOC) and could begin as a hardware-free early WU if M-band slack appears.
- **NEW plan item:** dual-coordinator design spike (~Aug, pre-M14-briefing). Nick to confirm scheduling.
- **Adapter-author guide:** seed with §7.4 + the SWITCH-CONFIG doctrine at the C/M9 documentation pass.
