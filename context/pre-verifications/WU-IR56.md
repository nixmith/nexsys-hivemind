<!--
file: context/pre-verifications/WU-IR56.md
purpose: The pre-verification for IR-56 (a cached, listed, un-adopted device that resumes silently is never re-proposed — the Gen4's silent resume after a restart): the source signatures at core `e96dce8` (law #27) and THE PREMISE ROW the instruction waits on — P4's sample 3 (REHEARSAL 1's kill −9, Mon 2026-09-28 09:00 CT) decides the shape (THE WEEKS AHEAD §2 row 3). Samples 1 and 2 (BC3, BC4: an orderly restart) both read all three plugs AVAILABLE — IR-56's class 0 of 2. Written v83 beat 2 (Sun 2026-09-27 ~16:3x CT) so that Monday's instruction is one row's edit, not an authoring.
audience: the hub (Monday's cut) · the Coder lane · the independent reviewer (adoption admission is a one-way door — D-v82-10)
state-type: pre-verification (the premise row OPEN)
status: FILED — v83 beat 2; the shape row fills at REHEARSAL 1's intake (Monday)
-->

# WU-IR56 — the signatures at `e96dce8`, and the premise row

## §0 The premise row (fills Monday)
| Sample | The restart | The Gen4 class 90 s after `launched` | Read at |
|---|---|---|---|
| 1 | BC3 (Sun 2026-09-27 08:18 CT; `installDist`, an orderly stop/start) | all three AVAILABLE | the BC3 return |
| 2 | BC4 (Sun 2026-09-27 14:44 CT; orderly) | all three AVAILABLE | the b4 audit §1 |
| 3 | REHEARSAL 1 (Mon 2026-09-28 09:00 CT; `kill -9`) | **PENDING** — P4's pre-registration: a Gen4 UNAVAILABLE or `age` > 60 s; the inverse arm (all three fresh) is the refutation | the rehearsal's return, action 7 |
**The shape rule (THE WEEKS AHEAD §2 row 3):** sample 3 UNAVAILABLE → shape (a), the boot-time re-proposal (§2); sample 3 fresh with samples 1–2 → the premise (v80 b2, the T2/T3 boots of 09-25) has not recurred in three restarts of two kinds → IR-56 is RE-SCOPED to shape (b), the operator re-interview verb, and DATED after the run unless rehearsal 2 (wk 10-05, a restart under load) shows it. Neither shape is authored before the row fills (THE PREMISE GATE).

## §1 The signatures (run at `homesynapse-core` HEAD `e96dce8`; `Z` as in WU-PJ2)
| # | The assumption | The instrument | Found |
|---|---|---|---|
| 1 | the announce path: cache + interview schedule | `sed -n '1305,1312p' $Z` | `onDeviceAnnounce(ZdoCodec.DeviceAnnounce)` :1309 → `cache.recordAnnounce(ieee, nwk)` :1310; `interviewQueue.schedule(ieee, nwk)` :1311 |
| 2 | the rejoin path admits by EXACTLY the announce path's two calls, with a provenance on the LOG LINE only | `sed -n '1434,1440p' $Z` | the F-R4-1 §1/§4/§5 comment: "relink ≠ adopt — a device already in the adoption maps never re-enters … EXACTLY the announce path's two calls … the rejoin provenance on the queue entry — it renders on the proposal's LOG LINE, never in an event payload" |
| 3 | both join paths are gated by the window | `sed -n '1339p;1422p' $Z` | `if (!isPermitJoinActive())` at both — a re-proposal at boot would ALSO be gated unless it bypasses the window by design (a design question for shape (a): a cached device in `adopt_devices` is already accepted — the interview needs no window; the lane pins where `interviewQueue.schedule` meets the window gate) |
| 4 | adoption is decided after the interview | `sed -n '1093,1096p' $Z` | `adoptIfAccepted(InterviewResult, ZigbeeAdoptionSlice.DiscoveryOutcome, DeviceProfile)` :1093; `LINKED → driveReporting(...)` :1095–:1096 |
| 5 | the cache seeds AVAILABILITY only at boot | `sed -n '388,396p' $Z` | `zigbee.availability_seeded: devices={} from_sidecar={} unknown={}` :392 (DP-5(a)); the ingestion unit is built after it with `CacheDeviceResolver` :395–:396 — no interview is scheduled from the cache |
| 6 | the accepted list | `grep -n 'adopt_devices' integration/integration-zigbee/src/main/resources/schema/zigbee-config-schema.json $Z \| head -4` | the schema key :32; the adapter reads it at adoption (the lane pins the line) |
| 7 | the module's boundary | as WU-PJ2 row 10 | no new `requires`; shape (a) touches `integration-zigbee` only (the frozen event contract untouched — the provenance renders on the log line, as the rejoin path already does) |
| 8 | the rig-side instrument | THE WEEKS AHEAD §4; the rehearsal packet action 7 | the T2b card (Fri 09-25) re-joined the Gen4s inside one window; P4's read is the three plugs' `availability`/`age` at 90 s |
