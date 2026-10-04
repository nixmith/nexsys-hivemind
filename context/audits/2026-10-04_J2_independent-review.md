<!--
file: context/audits/2026-10-04_J2_independent-review.md
purpose: THE ONE-WAY-DOOR REVIEW of J2's instruction (the skill §3 law 16; coding-instruction-format #33) — written by an agent that had not seen the authoring, from the draft (28,613 B), the pre-verification WU-J2 and 37 source files staged byte-exact from homesynapse-core `df2bc62` (every MANIFEST.md5 row re-checked). Verdict DISPATCH WITH EDITS: 24 edits (8 BLOCKING) + 17 compensating cuts, net −15 B (28,598 B before stamps; every anchor verified to match once and the result re-applied). The review text below is VERBATIM as returned.
audience: the v97 hub · the J2 lane · the v98 boot
state-type: review (verbatim; never edited)
status: FILED — RETURNED v97 beat 3 (Sun 2026-10-04 ~11:1x CT; instrument 2026-10-04T16:13:00Z); the 24 edits and 17 cuts APPLIED to the instruction before the dispatch line (the hub's three further byte trims are listed in the b3 audit §2). The review text below is verbatim as returned.
-->

# ONE-WAY-DOOR REVIEW — J2 (the scoped recovery window + the boot re-proposal; IR-114/115/123) at `df2bc62`

## §0 Verdict
**DISPATCH WITH EDITS** — the door's hinges hold at the bytes (the `String` scope equals `IEEEAddress.toString()`'s form; the tolerant decode is J1's staged precedent; the sealed/manifest pins are where named; the root is one method), but §4.2 models the close as ONE method where the adapter has THREE closers (the elapsed and superseding paths never enter `closeWindow(cause)`), §4.1 keeps an open order under which the new NCP close would undo its own enablement, §4.4 names a site where `interviewQueue` is still null, and two existing "no event but permit_join_opened" pins plus every FakeNcp's unanswered 0x006B would turn the lane's first run into hangs and unexplained reds. §3 #1–#8 fix these without a design reversal.

## §1 The premise rows
A = ZigbeeIntegrationAdapter · E = EzspCoordinatorProtocol · I = ZclIngestionUnit · S = ZigbeeAdoptionSlice · Q = PendingInterviewQueue · DC = ZigbeeDeviceCache · PJT/TCJ/IOR/KET = the Zigbee PermitJoin/TrustCenterJoin/InterviewOnRejoin/KeyEstablishment tests · PWA = PairingWindowEventTypeAnnotationTest.
| # | Claim | Lines seen | Verdict |
|---|---|---|---|
| 15 | `IEEEAddress` zigbee-only; scope a `String`; canonical form = `toString()` | zigbee module-info :10–:16; integration-api :16–:26 (no zigbee); `toString()` :83–:86 → `toHexString()` :53–:55 = `"0x" + String.format("%016X", value)`; `fromHexString` :68–:74 takes `0x`/`0X`/bare | HOLDS — `joiner.toString()` and a canonicalized request compare equal |
| 16 | The root builds the request | HomeSynapseCore :1298–:1299 (the method; :1300 is its body), :1307, :1312; the port cast :1124; PairingWindowPort :40–:41, view :53–:60 | HOLDS (`:1300` → `:1298`, #21) |
| 17 | One helper, version 1 | A:1107–:1119 (`new EventDraft(eventType, 1, …)`); calls :1010, :1056, :1065, :1082; `AVAILABILITY_CHANGED_SCHEMA_VERSION = 2` A:193 → :1789 | HOLDS |
| 18 | Permits 2; manifest 12; the pins | PairingWindowEvent :26; IntegrationEvents :55–:68; PWA :89–:90, :91–:94, :101–:103; EventTypesTest :46 (75 constants counted) | HOLDS + a trap: PWA :35–:37 / :63–:64 pin the `permit_join_` prefix (#10) |
| 19 | Three listener test impls | ZclIngestionUnitTest :66 is a FIELD, :125 an impl; FixtureReplayTest :105; main `AdapterIngestionListener` A:1524–:1675; I:135–:200 has no `default` | HOLDS / miscount: two (#18–19) |
| 20 | The frozen pins | IOR :304, :522, :671; KET :141, :157, :193; PJT :157, :191, :378, :396, :441; bench.sh :132 | HOLDS — but PJT :405–:419, TCJ :296–:297, IOR :678–:679 go red BY DESIGN (§2 d) |
| 21 | `data` is a hand-built map | PermitJoinEndpoint :217–:224; PermitJoinEndpointTest :68–:69 pins six keys | HOLDS |
| 22 | The grader's pin | grader.py :141–:144, :185 (no `join_rejected`); bench.sh :124 reads the six keys BY NAME | HOLDS |
| pv-1 | The wildcard is one line | E:1047; no `setPolicy` method — the form is `execute(FRAME_SET_POLICY, encodePolicy(…), …)` + `requireSuccess` :1036–:1044, :1059 | HOLDS |
| pv-5 | 0x0010 → DENY | gsdk not staged | UNCHECKABLE (the bit values match ezsp-enum.h as I know it) |
| pv-6 | The DENY has a handler | I:473–:502 (WARN :500–:501); E :262, :1110, :1115 | HOLDS |
| pv-8 | The close never touches the NCP | `grep -c -i 'clearTransient\|0x006B' E` → 0; A:1049–:1097 send nothing — THREE closers: `closeWindowIfElapsed` :1049–:1060, `closePrior` :1063–:1069, `closeWindow(cause)` :1079–:1087 (:1092 shutdown, :1219 reopen); :1071 calls the last "the two unconditional closers' shared body" | HOLDS; the instruction's model of it FAILS (#1) |
| pv-9 | The open's two frames | A:998–:999, THEN the prior's CAS + `closePrior` :1003–:1006 | HOLDS — the prior closes AFTER the new frames (#3) |
| pv-10 | No scope today | request :24; window :27–:34; event :29–:38 (every reference component `requireNonNull`ed :41–:46); endpoint :31, :138–:163 | HOLDS |
| pv-11 | Admission gates | A:1639–:1649; `admitRejoinCandidate` :1661–:1674 (`adoption.deviceIdFor` :1663); the H-ii path lands there too :1634 | HOLDS |
| pv-12 | J2a's site | A:385, :392 (body :1397–); `readAdoptAcceptList()` ×2; S:305–:309 renders `source={}` | HOLDS — `interviewQueue` is built at A:401, AFTER :392 (#4) |
| pv-13 | No window gate on announce | A:1527–:1530 | HOLDS |

## §2 The one-way door
**(a) Schema.** `PermitJoinOpened` :29–:38 is a plain record; the tolerant decode is J1's precedent IN the staged codec test — :349–:357 (a v1 row with missing keys → the record with nulls), :409–:417 (the version column is informational), :396–:406 (unknown keys ignored). A `String scope` kept out of the compact constructor's `requireNonNull`s rides the same path; its wire key is `scope`. Unsettled: the codec test's registry `AllEventClasses.ALL_EVENTS` (:51) is not staged — a hand list must gain `JoinRejected.class` (#22).
**(b) New event.** `permits` :26 → three; manifest :55–:68 → 13; PWA :90, :101–:103 as written. TRAP: PWA :35–:37 `EXPECTED_RECORDS` feeds :57–:65, whose :63–:64 asserts `startsWith("permit_join_")` — `JoinRejected` added there goes red for its NAME; keep the list at two and assert its annotation apart (#10). `permit_join_rejected` would satisfy the rule, but the name is D-v94-24's. `IntegrationEventTypeAnnotationTest.EXPECTED_SUBTYPES` (IntegrationEvents :33; not staged) pins the ten lifecycle subtypes — unaffected unless it counts the manifest.
**(c) Admission + J2a.** `admitRejoinCandidate` A:1661 is the one site for both hooks (:1634, :1649); the DEBUG form :1664–:1666 fits `reason=outside_scope`. `Q.schedule(IEEEAddress, int, Source)` EXISTS (Q:126; the 2-arg :111 delegates); `Source` :53–:72 with the vocabulary comment :68 — row 5 exact. The IEEE → NWK lookup EXISTS: `cache.device(ieee)` DC:401 → `networkAddress()` — row 33 is a named [INFO] (#11); an invalidated record carries `NETWORK_ADDRESS_UNKNOWN = 0xFFFF` (:503, :510–:514) and must be skipped or J2a interviews the broadcast address (#4). THE SITE: `interviewQueue` is built at A:401; "after `rehydrateAdoptionMaps()` (:392)" is an NPE at boot (#4, #5).
**(d) NCP close.** (1) THREE closers (pv-8): "`closeWindow(cause)`: (1) NCP (2) record" misses the elapsed (:1049) and superseding (:1063) paths and, read literally, sends three frames on EVERY `close()` with no window (`open == null` :1081) — twelve windowless `adapter.close()` in ZigbeeAvailabilityWiringTest alone (#1). (2) Today the new enablement (:998–:999) precedes the prior's close (:1003–:1006); a three-act close inside `closePrior` would import the new key, then CLEAR it, write 0x0002 and `permitJoin(0)` — every superseding open kills its own window. §4.1's "order kept" contradicts §4.2's fence: the prior block moves ahead of :998 and nulls `permitJoinDeadline` (today overwritten only at :1007) (#3). (3) `closeWindowIfElapsed` runs on the RUN thread (:637), the open on the executor; the protocol `lock` (E:1441) serializes frames, not sequences — an elapsed close that wins the CAS can land its frames AFTER the new enablement; one adapter lock around `closeOnNcp()` and the enablement, with a `currentWindow` re-check inside, closes it (#9). (4) `execute` is 3-arg (E:1455) and returns the frame unchecked; `requireSuccess` :1545 would throw on an empty payload. Status-less frames already exist — `ping()` :1417 (`FRAME_NOP`, `NO_PARAMETERS` :429), `coordinatorEui64` :1843 — so the hub's reading holds; the draft's `execute(…, new byte[0])` does not compile (#1). 0x006B's empty response matches bellows' `(0x006B, (), ())`; unprovable from the staged set. (5) `permitJoin(0)` is in range (E:1003). (6) P5 contradicts P3: after `permitJoin(0)` the MAC refuses association — no 0x0024 carries `DENY_JOIN` (#13–14).
**(e) Composition root.** Every `PairingWindowPort.open` site staged: HomeSynapseCore :1124 (method ref), :1298; PermitJoinEndpoint :167; PermitJoinEndpointTest `RecordingPort.open` :340–:348, `Call` :308, `new PairingWindowView(` :347 (§6's 1 / 1 ✓). Rows 13–15, 30 cover them; row 30 did not SAY the test port changes (#23). A bad scope's `IllegalArgumentException` → :1308–:1309 → the endpoint's :204–:205 `INVALID_PARAMETERS`.
**Byte order.** E reads EUI64 little-endian at :1093–:1096, :1185–:1187, :1224–:1227, :1654–:1656, :1850–:1853 — right — and already ENCODES one: `lookupNetworkAddress` :1586–:1590, `eui64[i] = (byte) (value >> (8 * i))`, silicon-exercised by every interview; mirror THAT (#12). `0x00124B0012345678` → `78 56 34 12 00 4B 12 00`.
**The pins vs T3/T4.** Every adapter test's `FakeNcp` answers `List.of()` (nothing) to an unknown frame — PJT :581–:602, IOR :929–:948, TCJ :499–:519, KET :546–:576 — 0x006B included; on the suite's `TestClock` (:97) the command loop (E:1474–:1504) never advances → a hang or a real-time wait. Every test that CLOSES a window needs a 0x006B arm answering `new byte[0]` (PJT :594's form): PJT T2 :168, T4a :362, T4b :385, T4c :430, DP-B5 :321 (via `resumeHandler` :556), IOR T7 :712 (#8, #7); TCJ and KET never close — unaffected. PJT T4b :405–:408 (`hasSize(2)`, `joins.get(1)[5] == 60`) and :409–:419 (`enablementFrameIds` collects every SET_POLICY/IMPORT_TRANSIENT_KEY/PERMIT_JOINING) go red under the new close — a designed rewrite (#8); the event pins :191, :378, :396, :441 stay. The listener: two abstract methods on I:135–:200 break ZclIngestionUnitTest :125 and FixtureReplayTest :105 (compile reds; :66 is a field). ZclIngestionUnitTest :353 and KET `assertPin` :470 stay green — the UNIT publishes nothing; the ADAPTER's `join_rejected` is what turns TCJ §A-4 :296–:297 and IOR T6 :678–:679 (`nonWindowEvents()` — "no event of any type but permit_join_opened") red BY DESIGN (#6, #7).
**Files table.** Every §1/§4 write site has a row; row 33 is not needed (#11); row 18's "two impls" is one (#18). §6's `new PairingWindow(` 1 / 2: PJT :141 is one test hit, the other lies outside the staged set — §6's "a §3 row or a named [INFO]" covers it.
**Tests.** T1–T4: PJT `bootProduction` :481, `framesWithId` :626, `enablementFrameIds` :650, `TestClock.advance` ✓. T5: TCJ §A-4 :276–:298 IS the fixture ✓. T6: ZclIngestionUnitTest `trustCenterJoinFrame` :1298 + `processCycle` ✓. T7: IOR `rejoinHandler` + `riders` + `deliverAndCycle` ✓ (a scoped twin of `request()` :830). T10: ZigbeeAvailabilityWiringTest `bootProduction(ncp, adoptDevices)` :1353–:1371 twice over one `tempDir` (the first boot's `close()` :330 flushes the sidecar) ✓. T11: KET's handler lacks the enablement arms — a scoped open there hangs the same way (#16). T15: PermitJoinEndpointTest :93–:130's forms ✓; :68–:69 stays green unscoped. T8, T12, T13, T16: their tests are not staged.
**The cap.** Draft 28,613 B (+~27 B stamps). Edits +1,183; cuts −1,198; net −15 → 28,598 B — applied to a copy from this file's own CUR/NEW strings; every anchor matched once.

## §3 EDITS
Apply all 24 edits AND all 17 cuts (the cuts are the byte compensation). `CUR:` is the exact text to replace — a unique substring of the draft; `CUR: ‹a› ⋯ ‹b›` is the span from the unique string a through the unique string b, inclusive (both verified unique; the span equals the intended text). `NEW:` replaces it byte-for-byte; `(delete line)` removes the whole line with its newline. Deltas in bytes.

1. **[BLOCKING] §4.2 ¶1** (+208 B)
   CUR: ‹`closeWindow(cause)`: (1) `protocol.closeJoinWin› ⋯ ‹e. `closeWindowOnShutdown`'s try already fences.›
   NEW: THREE closers (`A:1071`): `closeWindowIfElapsed` :1049 (run thread), `closePrior` :1063 (superseding), `closeWindow(cause)` :1079 (reopen :1219, shutdown :1092) — each CAS WINNER (:1054, :1004, :1081) calls a private `closeOnNcp()` before its publish; `open == null` sends NOTHING. `closeOnNcp()` = `protocol.closeJoinWindow()` in a try: `execute(FRAME_CLEAR_TRANSIENT_LINK_KEYS, NO_PARAMETERS, DEFAULT_COMMAND_TIMEOUT_MILLIS)` (3-arg `E:1455`, no `requireSuccess` — `ping()` `E:1417`) → policy 0x0002 → `permitJoin(0)`; a `RuntimeException` → WARN `zigbee.permit_join_ncp_close_failed: cause={}: {}`; the record still closes.
2. **[BLOCKING] §7 T3** (-5 B)
   CUR: T3 `closeWindow(elapsed)` → 0x006B,
   NEW: T3 the elapsed close → 0x006B,
3. **[BLOCKING] §4.1** (+107 B)
   CUR: A protocol failure at the open propagates as today (`A:995–1012`'s order kept).
   NEW: A protocol failure at the open propagates as today; :1003–:1006 MOVES ahead of :998 (§4.2's fence) and nulls `permitJoinDeadline` — a failed open then leaves no window on either side.
4. **[BLOCKING] §4.4** (+145 B)
   CUR: ‹Once per `initialize()`, after `rehydrateAdoptio› ⋯ ‹ched`; adopted → DEBUG `reason=already_adopted`;›
   NEW: Once per `initialize()`, right after `interviewQueue = new PendingInterviewQueue(clock)` (`A:401`; at :392 the queue is null): `proposeListedCachedDevices()` — per listed IEEE: no cache entry → DEBUG `zigbee.boot_listed_skipped: device={} reason=not_cached`; nwk 0xFFFF (cache :503) → `reason=address_unknown`; adopted (`adoption.deviceIdFor`, :1663) → DEBUG `reason=already_adopted`;
5. **[BLOCKING] §2** (+0 B)
   CUR: `Z/ZigbeeIntegrationAdapter.java` :190–200, :260–270, :356–400,
   NEW: `Z/ZigbeeIntegrationAdapter.java` :190–200, :260–270, :356–401,
6. **[BLOCKING] §3 row 17** (+88 B)
   CUR: | M | T5 |
   NEW: | M | T5; §A-4's `nonWindowEvents()` pin :296–:297 goes RED BY DESIGN → ONE `join_rejected` |
7. **[BLOCKING] §3 row 20** (+100 B)
   CUR: | M | T7; the pins at :304, :522, :671 UNCHANGED |
   NEW: | M | T7; the pins at :304, :522, :671 UNCHANGED; T6's :678–:679 RED BY DESIGN (ONE `join_rejected`); `defaultResponses` :947 gains the 0x006B arm |
8. **[BLOCKING] §3 row 16** (+272 B)
   CUR: | M | T1–T4 |
   NEW: | M | T1–T4; `defaultResponses` :593–:601 gains the 0x006B arm (`new byte[0]`, the :594 form; unanswered frames never return on the TestClock; `resumeHandler` :556 rides it); T4b :405–:419 REWRITTEN (three 0x0022; `SET_POLICY, PERMIT_JOINING` between the enablements); :396 stays |
9. **[REVIEW] §4.2 fence** (+146 B)
   CUR: ‹A superseding open (`A:1004–1006`) runs `closeWi› ⋯ ‹— never between a policy write and a key import.›
   NEW: A superseding open runs `closePrior` (:1063) to completion BEFORE the new enablement — never between a policy write and a key import; `closeWindowIfElapsed` (run thread) is a second NCP writer: `closeOnNcp()` and the enablement share one lock, and the close re-checks `currentWindow.get() == null` inside it.
10. **[REVIEW] §3 row 26** (+108 B)
   CUR: the ten lifecycle permits UNCHANGED |
   NEW: the ten lifecycle permits UNCHANGED; `EXPECTED_RECORDS` :35–:37 stays two (:64 pins the `permit_join_` prefix); `JoinRejected` asserted apart |
11. **[REVIEW] §3 row 33** (+10 B)
   CUR: | 33 | `Z/ZigbeeDeviceCache.java` | M only if no IEEE → NWK lookup exists (`grep -n 'public ' …`); else a named [INFO] | the lookup J2a needs |
   NEW: | 33 | `Z/ZigbeeDeviceCache.java` | — | NOT modified: `cache.device(ieee)` (:401) → `ZigbeeDeviceRecord.networkAddress()` IS the lookup; a named [INFO] |
12. **[REVIEW] §4.1 bytes** (+53 B)
   CUR: ‹with the partner's 8 bytes in the EZSP wire orde› ⋯ ‹red; T8 pins the bytes for `0x00124B0012345678`.›
   NEW: with the partner's 8 bytes little-endian — mirror the ENCODE at `E:1586–1590` (`eui64[i] = (byte) (value >> (8 * i))`, the inverse of `KeyEstablishment.parse` :1224–1227); T8 pins `78 56 34 12 00 4B 12 00` for `0x00124B0012345678`.
13. **[REVIEW] §4.2 tail** (-86 B)
   CUR: ‹Between windows the standing TC policy is now 0x› ⋯ ‹ce_join_failed … decision=DENY_JOIN` — §13's P5.›
   NEW: Between windows the standing TC policy is 0x0002 where 0x0003 lingered — §13's P5.
14. **[REVIEW] §13 P5** (+20 B)
   CUR: ‹plus **P5** — a join attempt between windows rea› ⋯ ‹ED_KEY` for that attempt REFUTES §4.2's reading.›
   NEW: plus **P5** — a join attempt between windows reads NO 0x0024 (P3's MAC refusal); a 0x0024 that does arrive (a router still permitting) reads `decision=DENY_JOIN`; `USE_PRECONFIGURED_KEY` there REFUTES §4.2's reading.
15. **[REVIEW] §6** (+110 B)
   CUR: `IngestionListener` 12 / 3 ·
   NEW: `IngestionListener` 12 / 3 · `PairingWindowPort` impls 1 / 1 · `openPairingWindow(` in `*Test.java` (each closer needs the 0x006B arm) ·
16. **[REVIEW] §3 row 24** (+115 B)
   CUR: | M | T11; the pins at :141, :157, :193 UNCHANGED |
   NEW: | M | T11; the pins at :141, :157, :193 UNCHANGED; its handler :546–:576 lacks the enablement arms T11's scoped open needs (copy ZigbeePermitJoinTest :586–:592) |
17. **[REVIEW] §7 Clock ¶** (-255 B)
   CUR: ‹**Tests must inject `Clock`.** Do NOT use `Clock› ⋯ ‹that PM review, not `./gradlew check`, enforces.›
   NEW: **Tests inject the module's `TestClock`** (`TestClock.createDefault()` + `advance`, ZigbeePermitJoinTest :97/:173 — `Clock.fixed` cannot elapse a window); never `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, `System.currentTimeMillis()`. `NO_DIRECT_TIME_ACCESS` (app's ArchUnit) scans production code only — this convention is PM-reviewed, not `check`-enforced.
18. **[INFO] §3 row 18** (+9 B)
   CUR: T6; its two listener impls (:66, :125) gain the two methods |
   NEW: T6; its listener impl (:125; :66 is the field) gains the two methods |
19. **[INFO] §0b row 19** (+8 B)
   CUR: ‹the listener has three test impls; the protocol › ⋯ ‹va:105`, `ZclIngestionUnitTest.java:66`, `:125`;›
   NEW: the listener has two test impls; the protocol interface none | §6's `git grep` lines | the counts of §6; the listener impls at `FixtureReplayTest.java:105`, `ZclIngestionUnitTest.java:125` (main: `A:1524`);
20. **[INFO] §5** (+1 B)
   CUR: `com.homesynapse.lifecycle` (`lifecycle/lifecycle/…`, 30 lines;
   NEW: `com.homesynapse.lifecycle` (`lifecycle/lifecycle/…`, 102 lines;
21. **[INFO] §0b row 16** (+0 B)
   CUR: `:1307` in `openPairingWindow(…)` `:1300`
   NEW: `:1307` in `openPairingWindow(…)` `:1298`
22. **[INFO] §3 row 28** (+15 B)
   CUR: T14 (the `availability_changed` v1→v2 case is the form) |
   NEW: T14 (:349–:357 is the form; `AllEventClasses` :51 must carry the type) |
23. **[INFO] §3 row 30** (+46 B)
   CUR: | M | T15 |
   NEW: | M | T15; `RecordingPort` :308/:340/:347 gains `scope` |
24. **[INFO] §1** (-32 B)
   CUR: ‹Every close — elapsed · superseded · shutdown — › ⋯ ‹closes (the key's 300-s expiry is the backstop).›
   NEW: Every close — elapsed · superseded · reopened · shutdown — runs the NCP's three-act close (0x006B → policy 0x0002 → `permitJoin(0)`) before the record's `permit_join_closed`; a failed NCP close is a WARN; the record still closes.

**Compensating cuts** — redundant or superseded text; none load-bearing after the edits:
- **C1 §9 bullet 4 (duplicates §3 row 3)** (-77 B)
   CUR: - `publishWindowEvent`'s version: opened 2, closed 1, rejected 1 (D-v82-10).
   NEW: (delete line)
- **C2 §9 bullet 5 (duplicates §0b row 15)** (-136 B)
   CUR: - `scope` is a `String` in `integration-api`, `rest-api`, `lifecycle`; an `IEEEAddress` only inside `integration-zigbee` (§0b row 15).
   NEW: (delete line)
- **C3 §10 two settled clauses** (-246 B)
   CUR: ‹If `execute(0x006B, …)` cannot be sent without a› ⋯ ‹ more than ~20 lines, propose the smallest; **if›
   NEW: **If
- **C4 §4.2 0x006B sentence** (-75 B)
   CUR: ‹0x006B's response carries NO status byte in EZSP› ⋯ ‹eSuccess` — the frame's arrival is the success).›
   NEW: 0x006B's response has NO status byte (bellows `(0x006B, (), ())`; arrival is success).
- **C5 §12 §1 list** (-43 B)
   CUR: (the byte order; 0x006B's response shape; the cache lookup; the listener impls; the J2a/J2b split)
   NEW: (the byte order; the listener impls; the J2a/J2b split)
- **C6 §9 bullet 1** (-73 B)
   CUR: ‹- The EUI64's BYTE ORDER on the wire is this uni› ⋯ ‹–1230`); pin it in T8; say which order you read.›
   NEW: - The EUI64's BYTE ORDER is this unit's trap — the wildcard hid it; mirror `E:1586–1590`, pin it in T8.
- **C7 §2 bullet 1** (-68 B)
   CUR: ‹- The pre-verification whole (19.5 KB): §1 your › ⋯ ‹ions; §4 the rig pre-registrations; §5 the door.›
   NEW: - The pre-verification whole (19.5 KB; §1 your premise rows · §3 the forks · §4 the rig pre-registrations).
- **C8 §0b row 15 Found** (-77 B)
   CUR: `com.homesynapse.integration` requires platform · event · device · state · persistence · config · java.net.http — never zigbee.
   NEW: `com.homesynapse.integration` never requires zigbee (§5).
- **C9 §0b row 22 Found** (-11 B)
   CUR: — `join_rejected` is NOT in it; a bench row follows the landing (OUT of this lane; a named [INFO])
   NEW: (:141) — `join_rejected` is NOT in it; a bench row follows the landing (a named [INFO])
- **C10 §0 bullet 2 tail** (-25 B)
   CUR: A premise row that no longer holds at `df2bc62` STOPS the plan at that row and says which.
   NEW: A premise row that fails at `df2bc62` STOPS the plan at that row.
- **C11 §4.3** (-14 B)
   CUR: `onKeyEstablishment(partner, status)` → §1's INFO when `partner` is the open or last-closed scoped window's IEEE, or all-zeros; else nothing.
   NEW: `onKeyEstablishment(partner, status)` → §1's INFO when `partner` is the open or last-closed scoped window's IEEE, or all-zeros.
- **C12 masthead purpose** (-108 B)
   CUR: A ONE-WAY DOOR (an event schema v2, a new store event, an admission rule, NCP close behavior, the composition root's port): the review ran
   NEW: A ONE-WAY DOOR: the review ran
- **C13 §11** (-58 B)
   CUR: · any bench file (the grader's whitelist is a bench row after the landing) ·
   NEW: · any bench file ·
- **C14 §0 THE RETURN** (-51 B)
   CUR: (3 KB + 1 KB × 33 rows, rounded up to the KiB); the §0 card is read first; a shorter return
   NEW: (3 KB + 1 KB × 33 rows); a shorter return
- **C15 §2 E ranges** (-32 B)
   CUR: :1079–1150 (`TrustCenterJoin`), :1217–1230 (`KeyEstablishment.parse` — the EUI64's wire order) ·
   NEW: :1079–1150, :1217–1230, :1455–1465, :1545–1552, :1582–1592 ·
- **C16 §0b row 20 Found tail** (-61 B)
   CUR: ; `bench.sh:132` watches the open line. New lines are ADDED beside them — text, order, count stay |
   NEW: ; `bench.sh:132` watches the open line |
- **C17 §6 sweep** (-43 B)
   CUR: the plan names what the boot did before for a listed, cached, unadopted device (nothing; IR-114) and what it does now (one `schedule`).
   NEW: before, a listed, cached, unadopted device got nothing at boot (IR-114); now one `schedule`.

## §4 Not checked
Not staged: `EventPayloadCodec`, `PersistenceObjectMapper`, `AllEventClasses`, `TestEventSamples`, `EventTypeRegistry`, `IntegrationEventTypeAnnotationTest`, `EzspProtocolTest`, `PendingInterviewQueueTest`, the `reporting_configured` test, the integration-api request/window tests, any lifecycle test of `openPairingWindow`, `RestFilters`, `IntegrationSupervisor`, `EzspAshTransport`/`FakeNcp`/`FakeSerialByteChannel`/`TestClock` (whether an unanswered command HANGS or times out on the TestClock is inferred from E:1474–:1504, not observed), the ArchUnit rules, the five `MODULE_CONTEXT.md`, gecko_sdk (pv-4/pv-5 and 0x006B's response shape rest on the pre-verification's reads and bellows' table as I recall it). Not judged: `join_rejected` vs the `permit_join_` prefix (a naming decision above this review); the IR-115 INFO-beside-WARN shape; the J2a/J2b split (§10).
