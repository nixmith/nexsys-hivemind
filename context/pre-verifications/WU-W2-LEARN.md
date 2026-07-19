<!--
file: context/pre-verifications/WU-W2-LEARN.md
purpose: Pre-verification for W2-LEARN — every load-bearing source-state assumption behind the enroll-zoneType-learn instruction, with observed signatures. The Coder reads this BEFORE executing; any mismatch with live source is a STOP.
audience: Coder (host-side CC lane); PM hub (audit).
status: VERIFIED 2026-07-19 (v34 hub, beat 1) — all signatures observed at core HEAD `9d40ce8` (worktree clean; hivemind spine at `3cc423b`) via §12 host-truth object reads the same day.
-->

# Pre-Verification — WU W2-LEARN (IAS ZoneEnrollRequest zoneType learn + the S31-ROUTE closure)

All line numbers are at core `9d40ce8`. Re-verify HEAD at dispatch; if HEAD moved, STOP and report.

| # | Assumption | Observed signature (2026-07-19) |
|---|---|---|
| P1 | `learnZoneType` has exactly ONE caller | `ZclIngestionUnit.java:376` — inside the general-command attribute arm (`REPORT_ATTRIBUTES`/`READ_ATTRIBUTES_RESPONSE`, IAS cluster only, :373–:377); declaration `:490`. `git grep learnZoneType` returns only these two + javadoc. |
| P2 | The ZoneEnrollRequest arm never reads the request payload | `:399–:405` — arm condition = `clusterSpecific && clusterId == IasZoneHandler.CLUSTER_ID && commandId == COMMAND_ZONE_ENROLL_REQUEST` (NO length guard, unlike the ZoneStatusChangeNotification arm `:389–:391`); body = `respondZoneEnroll(device, message); return;`. `respondZoneEnroll` (`:463–:480`) reads only `sourceEndpoint()`/`sender()` — the zoneType bytes are dropped on the floor. |
| P3 | `route()` gates ZCL dispatch on the FRAME's APS profileId, silently | `:291–:301` — ZDO arm first (`ZDO_PROFILE_ID`, device-announce only), then `if (message.profileId() != EzspCoordinatorProtocol.HA_PROFILE_ID) { return; }` — bare return, NO diagnostic. The gate field is `EzspIncomingMessage.profileId()` (per-frame), never the cached simple-descriptor. |
| P4 | The learned-state store + accessor | `learnedZoneTypes` = plain `HashMap<Long, ZoneType>` `:141` (cycle-thread confined — no locking); `learnedZoneType(IEEEAddress)` accessor `:551–:553`, LEARNED-ONLY (never the resolver fallback — the M9.7-W2 gotcha); `effectiveZoneType` `:561–:564` = learned-else-resolver. |
| P5 | IasZoneHandler constants | `CLUSTER_ID = 0x0500` (:26) · `ATTRIBUTE_ZONE_TYPE = 0x0001` (:28) · `COMMAND_ZONE_ENROLL_REQUEST = 0x01` (:33) · `COMMAND_ZONE_ENROLL_RESPONSE = 0x00` (:35) · `ENROLL_RESPONSE_SUCCESS = 0x00` (:37) · `ENROLL_ZONE_ID = 0x00` (:39). |
| P6 | ZoneType zclIds | MOTION `0x000D` · CONTACT `0x0015` · SMOKE `0x0028` · WATER_LEAK `0x002A` · VIBRATION `0x002D` (`ZoneType.java:23–:35`); `zclId()` accessor `:50`. |
| P7 | Existing learn semantics (must be byte-preserved by the extraction) | `learnZoneType(IEEEAddress, Map<Integer,Object>)` `:490–:519`: value must be `Long`; zclId→ZoneType scan over `values()`; unknown ⇒ `ias_zone_type_unknown` DEBUG + no store; store via `put`; `learned != previous(effective)` ⇒ `invalidateHandlers` (F-8) + `zigbee.ias_zone_type_learned: device={} zoneType={} (was {})` INFO; same-as-effective ⇒ silent store, no invalidate, no INFO. |
| P8 | The wire fixture already exists in the test corpus | `ZclIngestionUnitTest.zoneEnrollRequestAnswered` `:314–:335` builds the enroll request: fc `0x19`, tsn, cmd `0x01`, payload `zoneType 0x0015 LE + manufacturerCode 0x0000 LE`. **After this WU that fixture LEARNS CONTACT** — sweep it (and siblings) for asserts the new behavior drifts; today it pins only the response bytes. |
| P9 | Test census (mechanism-sweep at execution, never name-grep) | `ZclIngestionUnitTest`: 25 `@Test` at 9d40ce8. Sweep by MECHANISM: every test constructing cmd-`0x01`/`COMMAND_ZONE_ENROLL_REQUEST` frames; every caller of `learnedZoneType`/`invalidateHandlers`; every test asserting route() drop behavior for non-HA frames; every log-capture pin on `ias_zone_type_learned` / `ias_zone_enrolled`. |
| P10 | End-to-end choreography pins | `ZigbeeWave2ContactAdoptionTest` drives today's learn via a ZoneType ATTRIBUTE REPORT in the scripted drain (`:118` comment) and pins `containsExactly` ONE `ias_zone_type_learned` line (`:125–:128`). The new enroll-driven twin is a SEPARATE method — the existing pin must stay green untouched. |
| P11 | JPMS | `module-info.java` — verbatim embedded in the instruction; ZERO change this WU. |
| P12 | Silicon record (the joins night, pm-handoff v33 beat 4) | THREE enrollments (03P re-enroll + 04P ×2 arcs) produced ZERO `ias_zone_type_learned` — no wire source elicits the ZoneType attribute on real silicon; the enroll REQUEST is where zoneType arrives (ZCL8 §8.2.2.3). The 04P is joined/enrolled/proposed/HELD on the door pending exactly this learn. S31: cached descriptor profileId `0xC05E` (C-05 closed) yet reports INGEST (`on:true`, stateVersion 7) ⇒ with P3, its frames carry 0x0104 — the S31-ROUTE closure basis. |
| P13 | Protocol constants (Coder re-verifies at read) | `EzspCoordinatorProtocol.HA_PROFILE_ID` / `ZDO_PROFILE_ID` referenced at `:292`/`:299` — expected `0x0104`/`0x0000`; verify at source before writing the DEBUG diagnostic. |
| P14 | Suite baseline (VOLATILE — the stale-452 lesson) | M9.7-W2's close recorded **518/0/0 forced-fresh AT `9d40ce8`**. Stated as at-commit; G-WL-5 re-derives forced-fresh at the dispatch HEAD BEFORE any edit — never carry the count. |
