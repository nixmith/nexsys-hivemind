<!--
file: context/instructions/2026-09-06_coder-lane_F-R4-1b_zdo-ieee-addr-req_second-surface_coding-instruction.md
purpose: The F-R4-1b coding instruction — the SECOND over-the-air identity surface for the interview-on-rejoin admission path: when the coordinator's own table misses (`lookupEui64ByNodeId` 0x0061 → status ≠ 0 — R-4b's measured miss arm, `zigbee.lookup_eui64_failed: nwk=0x15ac status=0x1`, the router-parented sleepy SNZB-02P), the adapter asks the DEVICE itself with a ZDP IEEE_addr_req (cluster 0x0001) over the existing locked ZDO exchange, once per nwk per window epoch, and admits on the response through the SAME announce path. F-R4-1 named exactly this as its own trigger condition ("a second over-the-air surface is a second WU if 0x0061 misses on silicon"); R-4b measured the miss; the program §1.1 chartered this as the next core lane after FE-113 (the road to C-003 via R-4c). Authored AHEAD by the v66 hub at Block 2 (Sun 2026-09-06, instrument ≈16:1xZ) on source at 093d5b4 (the integration-zigbee tree is byte-identical to f25291b's; nothing since FAILCHAN touched it).
audience: the Coder lane (host-side Claude Code in homesynapse-core) · the hub (audit) · Nick (dispatches; commits)
state-type: coding instruction
status: ⛔ GATED on FE-113 LANDING (one lane on the core tree — FE-113 is it until Nick's commit + push and frontend.yml GREEN). ISSUE-READY otherwise. Baseline: `main` HEAD after FE-113 lands (the dispatch line carries the sha; FE-113 touches only web-ui/dashboard/, so every cite below holds byte-exact — a shifted cite is `[INFO]`, never a STOP). The desk pins the FRAME SHAPE; the acceptance instrument is the WIRE at R-4c (⟨R4C: Sat 09-12 | Sun 09-13⟩ — Nick's word, rec Sat 09-12); the completion register is REPO-COMPLETE until R-4c reads the surface on the sleepy device.
-->

# Coding Task: F-R4-1b — the ZDO `IEEE_addr_req` second surface for interview-on-rejoin (the router-parented sleepy device)

**Subsystem:** Zigbee integration (`integration/integration-zigbee`) — ONE module; nothing outside it.
**Design Doc:** Doc 08 Integration Runtime (LOCKED) §3.4 (the ZDO interview steps — the exchange idiom this WU reuses) · Doc 08 §3.3 structured logging (LTD-15) · R-10 docket Row 10 RULED (a) "relink ≠ adopt" (F-R4-1's ruling; this WU adds a resolver, not a path).
**Phase:** 3-Implementation
**Task Brief Reference:** the program `context/planning/2026-09-06_v65-b6_post-landing_program_and_four-charters.md` §1.1 (F-R4-1b; R-4c = C-003's slot) · the R-4b record `context/audits/2026-09-04_R-4b_re-rep_operator-record.md` §0 "THE MISS" + §7-A (the measured arm) · F-R4-1's gotcha "NO ZDO IEEE_addr_req in this WU — a second over-the-air surface is a second WU if 0x0061 misses on silicon" (`integration/integration-zigbee/MODULE_CONTEXT.md` §F-R4-1 Gotchas).

## §0 The lane contract (read first)
- **`date -u` FIRST**; state your instrument limit; re-derive CT as UTC−5 once.
- **Return path:** `nexsys-hivemind/context/audits/<CT-filing-date>_F-R4-1b_return.md` — ONE file. §0 card FIRST (≤3 KB: the census `N = a M + b A` with exact paths · the red-first table ≤2 KB · deviations by tag · the ZDP constants you re-derived and from where) · §1 what changed per file · §2 the gates run + counts (`:integration:integration-zigbee:test` with the suite count before/after, `:integration:integration-zigbee:compileJava`, `spotlessCheck`) · §3 pushback/observations · §4 the WUCP Phase-1 checklist. **Cap ≤12 KB.**
- **Baseline:** `main` HEAD with FE-113 landed (verify `git status --porcelain` empty and `git log -1 --format=%h` = the sha in the dispatch line; STOP if not). Every cite below is from `093d5b4`, whose integration-zigbee tree FE-113 does not touch.
- **Build discipline:** targeted Gradle on your desk is allowed (`./gradlew :integration:integration-zigbee:test :integration:integration-zigbee:compileJava spotlessCheck --offline`) — GREEN in one round is the target; the full `./gradlew check` is CI on Nick's push = the gate of record. **One commit; you commit nothing; stage nothing.**
- **Tests first** (red-first): every new test RUNS RED at HEAD before the production edit, except the rows this instruction marks green-by-construction (law #18).
- **No words to give.** No fallbacks are offered; a deviation is filed in §0 with its cause.

## What This Implements
F-R4-1 (landed `ef02d13` and after) admits a silently-rejoined device into the ONE existing interview path from two triggers; its H-ii arm (an unknown-sender HA frame inside an open permit-join window) resolves the sender's IEEE through (1) the cache's NWK→IEEE view and (2) the coordinator's own table (`lookupEui64ByNodeId`, EZSP 0x0061), and on a miss WARNs `zigbee.rejoin_candidate_unresolved … reason=lookup_miss` and stops. R-4b measured both arms on silicon: the hop HIT the mains router (adopted in 315 ms) and MISSED the router-parented sleepy SNZB-02P (`lookup_eui64_failed nwk=0x15ac status=0x1`) — 0x0061 resolves the coordinator's OWN table entries, so every device parented by a router is invisible to it. This WU adds the third resolver, in order after the second: **a ZDP `IEEE_addr_req` (cluster 0x0001) unicast to the sender's nwk, awaited as the tsn-matched `IEEE_addr_rsp` (0x8001) over the existing locked ZDO exchange (`zdoUnicastExchange` — the interview's Node_Desc/Active_EP/Simple_Desc idiom), bounded by the interview's own step timeout, once per nwk per window epoch.** A response admits the device through EXACTLY the announce path's two calls (`recordAnnounce` + `schedule(…, REJOIN)`); a miss (a non-success status, an NCP rejection, or silence past the deadline) is the same unresolved candidate as today with its reason named. Nothing else moves: H-i untouched, `admitRejoinCandidate` untouched, the event payloads untouched, the window semantics untouched, the once-per-epoch sets untouched (one set bounds BOTH surfaces — the coordinator is asked at most once and the air at most once per nwk per epoch).

## Files to Read Before Starting (minimum read set — MANDATORY)
1. `integration/integration-zigbee/MODULE_CONTEXT.md` — §F-R4-1 (Behavior Deltas + Gotchas, whole: the resolution order, the once-per-epoch sets, the log grammar, the rig note) · §M9.4-RPT (the `zdoUnicastExchange` seam) · §Gotchas (the module-wide list).
2. `integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/ZigbeeIntegrationAdapter.java` — fields `:185–:233` (`protocol` is the CONCRETE `EzspCoordinatorProtocol`, `:190`; the two epoch sets `:226`/`:233`) · `openPermitJoinWindow` region around `:790` (where the sets clear) · `AdapterIngestionListener.onRejoinCandidate(int, int)` `:1205–:1251` (THE ARM) · `admitRejoinCandidate` `:1277–:1291`.
3. `…/EzspCoordinatorProtocol.java` — `FRAME_SEND_UNICAST` `:112` · `FRAME_LOOKUP_EUI64_BY_NODE_ID` `:137` · `ZDO_PROFILE_ID` `:140` · `INDIRECT_TRANSMISSION_TIMEOUT_VALUE` `:311–:312` · `lookupIeee` `:1611–:1661` (the WARN grammar you mirror) · `sendUnicastLocked` `:1669` · `awaitIncomingLocked` `:1708–:1740` (every non-matching callback is preserved for the drain) · `zdoUnicastExchange` `:1784–:1821` (THE SEAM you call; package-private; takes the lock itself) · the `InterviewBinding` `zdoExchange` + its `zigbee.interview_step_timeout` WARN `:1950–:1965`.
4. `…/ZdoCodec.java` whole (188 lines: the cluster constants `:26–:34`, `encodeAddressRequest` `:59`, `parseDeviceAnnounce` `:166` — the byte-layout idiom you extend).
5. `…/InterviewStateMachine.java` `:43` (`STEP_TIMEOUT_MILLIS = 10_000`, package-private — the bound this WU reuses).
6. `src/test/java/…/ZigbeeInterviewOnRejoinTest.java` — the harness whole (`setUp` `:140`, `rejoinHandler` `:664`, `handleUnicast` + `zdoReply` (the ZDO scripting idiom: a scripted reply is delivered as `incomingMessage(ZDO_PROFILE_ID, cluster | 0x8000, 0, SNZB_NWK, reply)`; a `null` reply = silence, and `FakeSerialByteChannel` ADVANCES the `TestClock` on an empty read, so a timeout is deterministic), T1 `:168–:230`, T3 `:298–:325` (the test you re-pin).
7. `src/test/java/…/ZdoCodecTest.java` (10 tests; the byte-vector style).
8. `src/testFixtures/java/…/FakeNcp.java` header comment (the null-return = silence contract) · `FakeSerialByteChannel.java` `:19`/`:94` (the clock advance).
9. `context/lessons/coder-lessons.md` — the F-R4-1 entry (2026-09-02) and the FAILCHAN entry (2026-09-04).

## STOP-on-Mismatch Gates (read, then confirm before any edit)
| File | Expected state | What to check |
|---|---|---|
| `ZigbeeIntegrationAdapter.java` | `private EzspCoordinatorProtocol protocol;` at `:190`; `onRejoinCandidate(int networkAddress, int clusterId)` at `:1205` with the comment "never a ZDO IEEE_addr_req (a second over-the-air surface is a second WU)" at `:1219–:1220` and the `reason=lookup_miss` WARN at `:1242–:1245` | the arm is exactly F-R4-1's; the comment you will rewrite is present |
| `EzspCoordinatorProtocol.java` | `Optional<byte[]> zdoUnicastExchange(int, int, int, IntFunction<byte[]>, long)` package-private at `:1801`; `ZDO_PROFILE_ID = 0x0000` at `:140`; `lookupIeee` logs `zigbee.lookup_eui64_failed: nwk=0x{} status=0x{}` at `:1642` | the seam exists with this signature; the WARN grammar |
| `ZdoCodec.java` | `final class ZdoCodec` package-private, constants `0x0002/0x0004/0x0005/0x8002/0x8004/0x8005/0x0013` only — NO `0x0001`/`0x8001` anywhere in the file | the surface is absent at HEAD (your codec tests go red by construction) |
| `InterviewStateMachine.java` | `static final long STEP_TIMEOUT_MILLIS = 10_000;` at `:43` | the bound |
| `ZigbeeInterviewOnRejoinTest.java` | T3 asserts `reason=lookup_miss` and `lookupRequests … containsExactly(UNKNOWN_NWK)`; `zdoReply` has NO `0x0001` case | the re-pin target |
| `module-info.java` | exactly the 4 `requires` + 1 `exports` quoted below | zero change expected |
| the suite | `grep -rc '@Test' src/test/java` sums to **582** | the count you report before/after |

## Files to Create or Modify (the Files table governs — addition #2)
| Action | File | Description |
|---|---|---|
| MODIFY | `integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/ZdoCodec.java` | +2 constants (`CLUSTER_IEEE_ADDR_REQ = 0x0001`, `CLUSTER_IEEE_ADDR_RSP = 0x8001`) · +1 package-private NESTED record `IeeeAddressResponse(int status, IEEEAddress ieeeAddress, int networkAddress)` · `encodeIeeeAddressRequest(int tsn, int networkAddress)` · `parseIeeeAddressResponse(byte[] message)` |
| MODIFY | `…/EzspCoordinatorProtocol.java` | +1 package-private method `Optional<IEEEAddress> requestIeeeAddress(int networkAddress, long timeoutMillis)` over `zdoUnicastExchange`; +2 log tokens |
| MODIFY | `…/ZigbeeIntegrationAdapter.java` | the H-ii arm gains the third resolver after the 0x0061 miss; +1 constant; the stale comment rewritten; +1 INFO token; the miss WARN's reason vocabulary |
| MODIFY | `integration/integration-zigbee/MODULE_CONTEXT.md` | a `## F-R4-1b Implementation` section (deltas · gotchas · tokens) + the in-place pointer on F-R4-1's "NO ZDO IEEE_addr_req in this WU" gotcha |
| MODIFY | `…/src/test/java/…/ZdoCodecTest.java` | +3 tests (C1–C3) |
| MODIFY | `…/src/test/java/…/ZigbeeInterviewOnRejoinTest.java` | T3 re-pinned (the double miss) · +3 tests (T3b the air HIT · T3c the air is SILENT · T3d the air is never asked when the table hits — an assertion added to T1 counts as T3d if you prefer; say which) · the harness: `zdoReply` gains the `0x0001` case with a scriptable status, the ZDO unicast REQUEST bytes captured per cluster |
**Census: 6 M + 0 A. ZERO change to `module-info.java`, `build.gradle.kts`, `libs.versions.toml`, any schema, any event type or payload, `CoordinatorProtocol` (the frozen interface), `InterviewOps`, `ZclIngestionUnit`, `PendingInterviewQueue`, `ZigbeeAdoptionSlice`, the testFixtures rig (`ZigbeeHardwareFreeRig` never opens a window — unchanged).**

## Technical Specification

### Settled Decisions (NOT open questions)
- **DP-1 (where the surface lives):** a package-private method on `EzspCoordinatorProtocol` — the adapter already holds the concrete type (`:190`), and `zdoUnicastExchange` is already the package-private seam the reporting binding and the interview use. **The frozen `CoordinatorProtocol` interface is NOT touched** (F-R4-1's `lookupIeee` exception is not repeated: that hop was a coordinator-table read every implementation must offer; this one is a ZDP exchange, EZSP-hosted by construction). `InterviewOps` is NOT touched either (it is the interview's contract; a resolver is not an interview step).
- **DP-2 (the resolution order, final):** (1) the cache's NWK→IEEE view → (2) the coordinator's table, 0x0061 → **(3) the air, `IEEE_addr_req` — ONLY after a clean (2) MISS (`Optional.empty()` from `lookupIeee`)**. An exception from (2) (`EzspCommandException | EzspFormatException | IllegalStateException`) stays an unresolved candidate as today and does NOT fall through to (3) — a rejected or malformed coordinator exchange is not evidence that the air will answer, and the WARN already names it. `EzspCommandTimeoutException` / `TransportFailureException` from EITHER surface PROPAGATE to the production loop's watchdog arms (coordinator trouble is never device evidence — the F-R4-1 posture, unchanged).
- **DP-3 (once per nwk per epoch, both surfaces):** the existing `rejoinLookupAttempted` set gates the PAIR — no second set. The coordinator is asked at most once and the air at most once per nwk per window epoch; both clear on `openPermitJoinWindow()` exactly as today; `attemptReopen()` leaves them alone.
- **DP-4 (the bound):** `static final long IEEE_ADDR_REQ_TIMEOUT_MILLIS = InterviewStateMachine.STEP_TIMEOUT_MILLIS;` on the adapter (10 s) — the interview steps that follow an admission run under the same bound, so a device that cannot answer inside it could not be interviewed anyway; a router parent buffers for its own indirect timeout (the coordinator's is `INDIRECT_TRANSMISSION_TIMEOUT_VALUE = 7680` ms, `:312`), and a sleepy end device that has just transmitted polls its parent — the wire at R-4c decides; the number is NOT re-tuned on this desk.
- **DP-5 (the request shape — ZDP, embedded per law #4; re-derive independently before pinning):** Zigbee Specification 05-3474-21 §2.4.3.1.2 `IEEE_addr_req` (cluster **0x0001**): `NWKAddrOfInterest` u16 LE · `RequestType` u8 (**0x00 = Single Device Response**; 0x01 = Extended) · `StartIndex` u8 (**0x00**). On the wire the ZDP transaction sequence number precedes the body (the codec's `[tsn]…` convention, `encodeAddressRequest`). Encoded: **`[tsn][nwk lo][nwk hi][0x00][0x00]` — 5 bytes.** Sent as a unicast to `networkAddress` (the device answers for its own address — the zigpy/Z2M idiom for an unknown sender), profile 0, endpoints 0/0, exactly as `zdoUnicastExchange` does.
- **DP-6 (the response shape):** §2.4.4.1.2 `IEEE_addr_rsp` (cluster **0x8001**): `Status` u8 (**0x00 SUCCESS · 0x80 INV_REQUESTTYPE · 0x81 DEVICE_NOT_FOUND**) · `IEEEAddrRemoteDev` u64 LE (8) · `NWKAddrRemoteDev` u16 LE; with RequestType 0x01 the optional `NumAssocDev` · `StartIndex` · list follow — this WU sends 0x00 and IGNORES any trailing bytes. Parsed from `[tsn][status][ieee LE 8][nwk LE 2]` = **12 bytes minimum**; shorter → `Optional.empty()` (the `parseDeviceAnnounce` truncation idiom); status ≠ 0 → present WITH the status (the caller logs it — the codec never logs). The parser does NOT require `NWKAddrRemoteDev` to equal the request's nwk (a device answering after a re-address is still an answer; the adapter's `recordAnnounce` takes the RESPONSE's nwk).
- **DP-7 (the log grammar — grep-stable, keys in this order):** protocol: INFO `zigbee.ieee_addr_req: nwk=0x{}` (the attempt) · INFO `zigbee.ieee_addr_rsp: nwk=0x{} device={}` (a SUCCESS status) · WARN `zigbee.ieee_addr_rsp_failed: nwk=0x{} status=0x{}` (a non-success status; the R-4c instrument, mirroring `lookup_eui64_failed`) · WARN `zigbee.ieee_addr_req_unanswered: nwk=0x{} timeout_ms={}` (an NCP rejection or the deadline). Adapter: the existing WARN `zigbee.rejoin_candidate_unresolved: nwk=0x{} cluster=0x{} reason={}` with **`reason=zdo_miss`** when the air was tried and missed (status, rejection or silence — the protocol's line says which); `reason=lookup_miss` is RETIRED from this arm (it can no longer occur — the air is always tried after a clean table miss); the exception arm's `reason=<message>` is unchanged. `zigbee.rejoin_candidate: device={} nwk=0x{} source=unknown_sender` is byte-unchanged on an admission from the air (the surface reads from the two protocol lines that precede it — the R-4c glance grammar: `lookup_eui64_failed status=0x1` → `ieee_addr_req` → `ieee_addr_rsp` → `rejoin_candidate` → the interview → `device_proposed … source=rejoin` → `device_adopted`).
- **DP-8 (the admission):** the response's IEEE and the RESPONSE's nwk go to `admitRejoinCandidate(ieee, nwk, "unknown_sender")` — byte-unchanged; the already-adopted DEBUG arm and the queue's put-replace semantics apply as today.

### JPMS — the current `module-info.java` of the target module, verbatim (`integration/integration-zigbee/src/main/java/module-info.java` at `093d5b4`; comments elided, directives exact). Expected diff: **NONE.**
```java
module com.homesynapse.integration.zigbee {
    requires transitive com.homesynapse.integration;
    requires com.fazecast.jSerialComm;
    requires org.slf4j;
    requires com.fasterxml.jackson.databind;

    exports com.homesynapse.integration.zigbee;
}
```
Walked against this instruction's own mandates (law #9/#14): logging → `org.slf4j` already present; no new type on any EXPORTED signature (`ZdoCodec` is package-private; the nested record is package-private; `requestIeeeAddress` is package-private on a public class — not an exported surface; `IEEEAddress` is this module's own public type); no Jackson; no new module edge. Zero change.

### The adapter arm after this WU (the shape; the Coder writes the code)
```
resolved = cache.deviceForNetworkAddress(nwk)                       // (1) unchanged
if (resolved.isEmpty()) {
    if (!rejoinLookupAttempted.add(nwk)) return;                     // once per nwk per epoch — the PAIR
    try { resolved = protocol.lookupIeee(nwk); }                      // (2) unchanged
    catch (EzspCommandException | EzspFormatException | IllegalStateException f) { WARN unresolved reason=<message>; return; }
    if (resolved.isEmpty()) {                                         // (3) NEW — the air
        try { resolved = protocol.requestIeeeAddress(nwk, IEEE_ADDR_REQ_TIMEOUT_MILLIS); }
        catch (EzspCommandException | EzspFormatException | IllegalStateException f) { WARN unresolved reason=<message>; return; }
        if (resolved.isEmpty()) { WARN unresolved reason=zdo_miss; return; }
    }
}
admitRejoinCandidate(resolved.get(), nwk, "unknown_sender");
```
`requestIeeeAddress` (protocol, package-private): range-check the nwk (IAE outside 0x0000–0xFFFF, the `lookupIeee` precedent) → INFO `ieee_addr_req` → `zdoUnicastExchange(nwk, CLUSTER_IEEE_ADDR_REQ, CLUSTER_IEEE_ADDR_RSP, tsn -> ZdoCodec.encodeIeeeAddressRequest(tsn, nwk), timeoutMillis)` → empty ⇒ WARN `ieee_addr_req_unanswered` + `Optional.empty()` → `parseIeeeAddressResponse` empty (truncated) ⇒ `EzspFormatException` naming `IEEE_addr_rsp` (the `lookupNetworkAddress`/`lookupEui64ByNodeId` precedent: a malformed answer is a dialect defect, not a miss) → status ≠ 0 ⇒ WARN `ieee_addr_rsp_failed` + empty → else INFO `ieee_addr_rsp` + the IEEE. **The response's nwk:** return it beside the IEEE if you need it for DP-6's last sentence — the simplest lawful shape is `Optional<ZdoCodec.IeeeAddressResponse>` from the protocol and the adapter reading both fields; choose one shape, say which in §0.

### Event Types Produced or Consumed — none added; none changed (the `device_discovered`/`device_adopted` payloads are the frozen event-log contract; F-R4-1's provenance rides the log line only, unchanged).
### Configuration Parameters — none (no new key; `permit_join_duration` semantics untouched).
### Error Handling — the two propagating exception classes (`EzspCommandTimeoutException`, `TransportFailureException`) are NOT caught in the arm (they reach the watchdog); everything else on the new surface is an unresolved candidate with its reason on the WARN; the codec never throws on a short buffer (empty), the protocol converts a short SUCCESS body to `EzspFormatException`.

## Locked Decisions That Apply
LTD-15 structured log entries (every new line has its key set asserted by a test) · LTD-17 the module depends only on integration-api (unchanged) · INV-CE-04 coordinator-neutral ADAPTER logic (honored: the resolver is a protocol method; the adapter's arm names no EZSP frame id) · R-10 Row 10 (a) relink ≠ adopt (the admission is unchanged; a device in the adoption maps never re-enters).

## Invariants That Must Hold
The frozen event-log contract (no payload change) · the once-per-epoch bound (T3/T3c assert ONE coordinator request and ONE air request per nwk per epoch) · the announce path is the only admission path (the two calls, byte-identical) · the production loop's watchdog arms still see coordinator trouble (the two propagating classes are not caught) · `Clock`-injected tests only (below).

## P2 Consumer/Pin (Fan-Out) Survey (done at authoring; re-run the greps)
- **`ZdoCodec` consumers:** `EzspCoordinatorProtocol` (the interview binding, the reporting binding) and `ZclIngestionUnit` (`parseDeviceAnnounce`) — none is changed; two constants and two static methods are ADDED. No shape test pins `ZdoCodec`'s method count (`ZdoCodecTest` has no `getDeclaredMethods`).
- **`reason=lookup_miss` consumers:** `ZigbeeInterviewOnRejoinTest` T3 `:316–:317` (re-pinned to `zdo_miss`); `ZigbeeIntegrationAdapter.java` `:1244` (the arm itself); `MODULE_CONTEXT.md:744` (§F-R4-1's policy paragraph — the pointer notes the retirement). `git grep -n 'lookup_miss'` at `093d5b4` = exactly those THREE files (verified at authoring); the F-R4-1 instruction/return/audit under the hivemind are history and keep their text. Re-run the grep and list the result in §0.
- **`rejoin_candidate_unresolved` key set:** unchanged (nwk · cluster · reason) — the tests asserting its key set stay green.
- **Exhaustive switches / count pins over any set this WU grows:** none (no enum, no sealed hierarchy, no registry touched). The nested record is a NEW type in a package-private class → **MODULE_CONTEXT type delta: +1 package-private NESTED record (no new type file)** — the F-R4-1 `PendingInterviewQueue.Source` precedent; the header type count is unchanged.
- **`CoordinatorProtocol` implementors:** untouched (DP-1). **`InterviewOps` implementors:** untouched.
- **ARCH-RULE-REACH (law #16):** `HomeSynapseArchRules.java` names `com.homesynapse.integration..` only in Rule 4's dependency-direction whitelist (`:133–:160`: core never depends on integration) — this WU adds no edge in any direction; **zero collisions**. `NO_DIRECT_TIME_ACCESS` reaches this module's PRODUCTION code: the new protocol method reads time only through the injected `clock` inside `zdoUnicastExchange` (unchanged) — add no `Instant.now()`.
- **The rig (`ZigbeeHardwareFreeRig`, testFixtures):** never opens a window → the arm never reaches (3); no script needed; unchanged (the F-R4-1 gotcha stands).

## Test Requirements (tests first; red at HEAD unless marked)
**`ZdoCodecTest` (+3):**
| Test | Scenario | Assertion |
|---|---|---|
| C1 `encodeIeeeAddressRequest_isTsnNwkLeSingleZeroIndex` | tsn 0x2A, nwk 0x15AC | exactly `[0x2A, 0xAC, 0x15, 0x00, 0x00]` |
| C2 `parseIeeeAddressResponse_successCarriesIeeeAndNwk` | `[tsn][0x00][8 bytes LE of 0xF044D3FFFED2A201][0xAC][0x15]` | status 0, `IEEEAddress(0xF044D3FFFED2A201L)`, nwk 0x15AC; trailing bytes (an extended list) ignored |
| C3 `parseIeeeAddressResponse_truncatedIsEmpty_statusIsCarried` | an 11-byte body → empty; a 12-byte body with status 0x81 → present with status 0x81 | the codec never decides — the caller does |
**`ZigbeeInterviewOnRejoinTest` (T3 re-pinned; +3):**
| Test | Scenario | Assertion |
|---|---|---|
| T3 (re-pin) `unknownSenderInsideWindow_tableAndAirMiss_warnsOnceAndSchedulesNothing` | window OPEN; 0x0061 answers status 0x01; the air answers `IEEE_addr_rsp` status 0x81 | ONE 0x0061 request; ONE ZDO unicast with cluster 0x0001 whose body is `[tsn][0x99][0x99][0x00][0x00]` (the request bytes captured from `handleUnicast`); WARN `rejoin_candidate_unresolved: nwk=0x9999 cluster=0x406 reason=zdo_miss` exactly once; protocol WARNs `lookup_eui64_failed: nwk=0x9999 status=0x1` and `ieee_addr_rsp_failed: nwk=0x9999 status=0x81` once each; no `rejoin_candidate:`; nothing scheduled; nothing published; a SECOND frame from the same nwk asks NEITHER surface again |
| T3b `unknownSenderInsideWindow_tableMiss_airHit_adoptsThroughTheAnnouncePath` | 0x0061 status 0x01; the air answers status 0x00 with the SNZB EUI64 + nwk | INFO `ieee_addr_req: nwk=0x9999` · INFO `ieee_addr_rsp: nwk=0x9999 device=0x…` · `rejoin_candidate: device=… nwk=0x9999 source=unknown_sender` (the T1 line, byte-identical) · the interview runs and `device_proposed … source=rejoin` (the T1 tail) · exactly ONE 0x0061 and ONE 0x0001 request |
| T3c `unknownSenderInsideWindow_tableMiss_airSilent_timesOutOnceAndSchedulesNothing` | 0x0061 status 0x01; `zdoReply` returns null for 0x0001 (silence — the fake channel advances the clock) | the clock advanced by ≥ `STEP_TIMEOUT_MILLIS` across the exchange; WARN `ieee_addr_req_unanswered: nwk=0x9999 timeout_ms=10000`; `reason=zdo_miss` once; nothing scheduled; a second frame asks nothing |
| T3d (an assertion added to T1, or its own test — say which) | the table HITS | ZERO 0x0001 unicasts — the air is never asked when the table answers |
**Red-first prediction (law #18):** C1–C3 red at HEAD by construction (the methods do not exist — a compile failure of the test class counts as red; say so). T3 (re-pinned) red at HEAD (HEAD logs `lookup_miss` and sends no ZDO unicast). T3b, T3c red at HEAD (no air request is ever sent). T3d **green-by-construction** at HEAD (HEAD never sends 0x0001 either) — disclosed; it earns its place by pinning the ORDER after the change. Every existing test stays green; the ONE pre-existing assertion that changes is T3's (`lookup_miss` → `zdo_miss`).
**Tests must inject `Clock`.** Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` in this module's test code. Use `Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC)` injected via constructor/`@BeforeEach` (this harness already uses `TestClock.createDefault()` — keep it). **Enforcement reach:** `NO_DIRECT_TIME_ACCESS` runs from `com.homesynapse.app`'s test classpath, so it mechanically catches PRODUCTION code in every non-whitelisted module (plus app's own tests) — it does **not** scan this module's test source set. Clock-injection here is a self-enforced project convention that PM review, not `./gradlew check`, enforces.

## MODULE_CONTEXT.md Update
Append `## F-R4-1b Implementation — the ZDO IEEE_addr_req second surface (2026-09-xx)` in the module's established shape: the deltas per type (codec · protocol · adapter), the gotchas (below), the token inventory (NEW ×4 protocol lines; CHANGED: `rejoin_candidate_unresolved`'s reason vocabulary — `zdo_miss` replaces `lookup_miss` on the miss arm), the suite count before/after, "Type delta: +1 package-private NESTED record". Amend F-R4-1's gotcha "NO ZDO IEEE_addr_req in this WU …" IN PLACE with a bracketed pointer ("[SUPERSEDED at F-R4-1b — see below]"), never by deletion. Header type count unchanged.

## What to Watch Out For
- **The hot path is still hot:** (3) runs on the run thread inside the ingestion drain and BLOCKS for up to 10 s per unknown nwk per epoch, only inside an open window — the interview already does the same for up to 60 s; do not move it off-thread (the lock discipline and the drain's ordering depend on it).
- **`zdoUnicastExchange` returns empty for BOTH an NCP rejection and the deadline** — one WARN token (`ieee_addr_req_unanswered`) covers both; do not invent a second.
- **The tsn matcher only checks byte 0** — a stray `IEEE_addr_rsp` from another device with the same tsn would match; the response's `NWKAddrRemoteDev` is the guard against admitting the wrong identity: if it differs from the request's nwk, still admit on the RESPONSE's pair (DP-6) but log the pair on the INFO line (both nwk values render only if they differ — or always; choose, say which).
- **Do not touch `reason=lookup_miss` anywhere except T3 and the arm** — the F-R4-1 instruction/return/audit under the hivemind are history and keep their text.
- **The record-component/static-factory collision check** (the M7.2a-2 gate-fix STOP-check): the nested record `IeeeAddressResponse(int status, IEEEAddress ieeeAddress, int networkAddress)` auto-defines `status()`, `ieeeAddress()`, `networkAddress()` — declare no static factory or helper with those names.
- **`spotlessCheck`** runs on the whole repo — the FE-113 landing left no Java change, so a red here is yours.
- **The fake NCP's built-in model** answers unscripted `setConfigurationValue`/`getConfigurationValue`/`getEui64` — nothing else; an unscripted `sendUnicast` is answered by `handleUnicast` in THIS test's handler only; keep the new case inside `zdoReply`'s switch so the delivery idiom (`incomingMessage(ZDO_PROFILE_ID, cluster | 0x8000, 0, SNZB_NWK, reply)`) is reused, not re-invented.
- **Sleepy-device physics is NOT modelled on the desk:** T3b's synchronous reply is the shape pin, not a timing claim. The return's §3 says so in one line.

## Coder Pushback Welcome
If `zdoUnicastExchange`'s contract (empty for rejection AND timeout) makes DP-7's `timeout_ms=` key dishonest for the rejection case, say so and propose the split (`reason=ncp_rejected|deadline`) with the seam change it needs — do not silently widen the seam. If the response-nwk ruling (DP-6) conflicts with `recordAnnounce`'s contract at source, STOP-note it in §0 with the line.

## Out of Scope
The `NWK_addr_req` inverse · the extended (RequestType 0x01) associated-device list · a re-index of the adopted-but-cache-unindexed corner (F-R4-1's OBS; still a separate proposal) · any change to the interview steps, the window semantics, the announce path, availability, events, the rig, the dashboard.

## Success Criterion (binary)
DONE when: (1) the census is exactly 6 M + 0 A or the deviation is declared in §0 with its cause; (2) C1–C3, T3, T3b, T3c ran RED at HEAD (T3d green-by-construction, disclosed) and GREEN after; every pre-existing test green; `spotlessCheck` clean; `:integration:integration-zigbee:test` GREEN with the suite count 582 → **588** (or the deviation named); (3) `module-info.java` byte-unchanged; (4) MODULE_CONTEXT updated (the section + the in-place pointer); (5) the WUCP Phase-1 checklist; (6) the return within cap. **The gate of record is CI on Nick's push. Completion register: REPO-COMPLETE, LIVE-VERIFICATION PENDING — the surface is "verified" only when R-4c (⟨R4C⟩) reads `ieee_addr_rsp: nwk=0x15ac device=0xF044D3FFFED2A201` (or the SNZB-02P's current nwk) followed by `rejoin_candidate … source=unknown_sender` and `device_adopted` on the held card; a `ieee_addr_req_unanswered` on the sleepy device is ALSO a first-class datum (the parent-buffer window vs the poll cadence) and re-opens DP-4, not the WU.**

## Work Unit Completion (WUCP Phase 1)
After your desk gates pass: update `MODULE_CONTEXT.md`; append the `coder-handoff.md` entry (Deferred Build Gate: YES — the full `./gradlew check` is CI on Nick's push; NEXT WU pointer: the hub's audit → the msg file → Nick's commit + push → CI green = the gate → **R-4c on the held card (the C-003 slot: the six-device fleet re-adopted — routers by rejoin, the SNZB-02P by this surface)** → P-1's charter); a `coder-lessons.md` note only if you learned one; the checklist in the return.

### DISPATCH LINE (Nick pastes into a host-side Claude Code session in `~/Desktop/Code/ClaudeFolder/homesynapse-core` — ONLY after FE-113 has LANDED (his commit + push; `frontend.yml` GREEN); the hub fills the sha)
```
date -u first. Boot as the nexsys-coder skill. Baseline: this tree must be at <FE-113's landed sha> and clean — verify with `git log -1 --format=%h` and `git status --porcelain` (STOP and report if not). Execute nexsys-hivemind/context/instructions/2026-09-06_coder-lane_F-R4-1b_zdo-ieee-addr-req_second-surface_coding-instruction.md exactly: read its §0 contract and the minimum read set first; confirm every STOP gate; re-derive the ZDP constants (DP-5/DP-6) independently before pinning them. Tests first (C1–C3, T3, T3b, T3c red at HEAD; T3d disclosed green-by-construction), then the production edits, 6 M + 0 A, module-info byte-unchanged. Return ONE file at nexsys-hivemind/context/audits/<today's CT date>_F-R4-1b_return.md, §0 card first, ≤12 KB. Stage nothing; commit nothing; the hub audits and Nick commits.
```
