<!--
file: context/instructions/2026-10-04_coder-lane_J2_scoped-recovery-window_IR-114_LOCAL_desk-coding-instruction.md
purpose: THE CODING INSTRUCTION for J2 = J2a (IR-114: a cached, unadopted, LISTED device re-proposed at boot) + J2b (the DEVICE-SCOPED recovery window: the transient key's partner = the named IEEE; TC policy 0x0013; an explicit NCP close; `join_rejected`) + IR-115's reclassification + IR-123's rider — LOCAL form, plan-first (W9), on Nick's desk (THE HORIZON §2 J2; `WIZARD: b′`, D-v94-24). A ONE-WAY DOOR: the review ran before the dispatch line (`context/audits/2026-10-04_J2_independent-review.md`).
audience: the J2 Coder lane (Claude Code on Nick's desk) · the hub (the intake) · the reviewer
state-type: coding instruction (LOCAL form; plan-first)
status: DISPATCH-READY — cut v97 beat 3 (Sun 2026-10-04 ~11:1x CT; instrument 2026-10-04T16:13:00Z); baseline `df2bc62` (re-verified at the paste); the pre-verification `context/pre-verifications/WU-J2_scoped-recovery-window_IR-114.md` (fourteen rows, re-run v97 b2, D-v97-5); the review applied.
baseline: homesynapse-core `df2bc62` (`main`; porcelain 0)
-->

# J2 — the scoped recovery window + the boot re-proposal (LOCAL; plan-first)

## §0 The coder-session prompt (read this whole section before any command; every line binds)
- You are in `~/Desktop/Code/ClaudeFolder/homesynapse-core` on `main` at `df2bc62`. Run `date -u` FIRST; every stamp you write derives from it (CT = UTC − 5; a Pi log line is EDT = UTC − 4 — name the clock beside every time you quote). `git --no-optional-locks status --porcelain` must be EMPTY before your first act and your first act is `git switch -c j2/scoped-recovery-window-ir-114` — every write lives on that branch; never `main`, never `git push`, never merge. **You STAGE, never COMMIT** (THE LANE STOPS AT A LOCK, D-v95-28): `git add` your files; the return's last line names `git write-tree`'s sha; the commit is Nick's card after the intake. No attribution text anywhere (grep your return for `Co-Authored\|Claude-Session`; a hit is a defect). No token, no secret.
- **PLAN FIRST (W9).** Before any write to a source file: read §2's set by the ranges given; re-run EVERY row of `../nexsys-hivemind/context/pre-verifications/WU-J2_scoped-recovery-window_IR-114.md` §1 (fourteen instruments) and §0b below, paste each count or line into your plan; settle the forks (§4) from the BYTES the plan cites; then write `../nexsys-hivemind/context/audits/<CT-date>_J2_plan.md` (≤ 8,192 B) in the shape of §12 and STOP, printing its last line `PLAN-RETURNED <path> <bytes>`. You write code only after the word `GO` (or `GO with: …`, whose edits you apply first). A premise row that fails at `df2bc62` STOPS the plan at that row.
- Tests first (§7): the red is OBSERVED — a compile failure on a type, field or method that does not yet exist IS the red; say so in the return — then green. Write ONLY §3's rows (the Files table governs where prose and table differ).
- `./gradlew check` green at the end (`-Xlint:all -Werror` is on). The gate lines are the verbatim task paths of `settings.gradle.kts`: `:integration:integration-zigbee:test` · `:integration:integration-api:test` · `:core:event-model:test` · `:core:persistence:test` · `:api:rest-api:test` · `:lifecycle:lifecycle:test` · `:app:homesynapse-app:test` (the ArchUnit rules live there). `--rerun` on an up-to-date task. Scripts over ~15 lines are written with the Write tool and run by path. `MODULE_CONTEXT.md` by `grep -n` only, never whole (zigbee's is 244 KB).
- THE RETURN: `../nexsys-hivemind/context/audits/<CT-date>_J2_return.md` — §0 the card (DELIVERED/BLOCKED; `check`'s closing lines; the XML counts per module; `git --no-optional-locks diff --cached --stat`; the red texts; rows 1–22 re-run with their counts) · §1 what changed (per file, line spans) · §2 the tests (names; the observed red; green) · §3 deviations at honest severity ([INFO]/[REVIEW]/[BLOCKING]) · §4 the survey as re-run (§6) · §5 findings for the register · §6 the coder-handoff entry · §7 instrument limits. **≤ 36,864 B is a CEILING, not a target** (3 KB + 1 KB × 33 rows); a shorter return with the same receipts is better. The last line of the FILE: `RETURNED <path> <bytes> <the staged tree sha>`.
- The hub stages nothing of yours; the landing is Nick's card after the intake (a squash onto `main` under the gated form, IR-101; CI on his push is the gate of record).

### §0b The premise table (beyond the pre-verification's fourteen; grepped by the hub at `df2bc62`; re-run each; the path letters are §2's)
| # | The claim | The instrument | Found |
|---|---|---|---|
| 15 | **`IEEEAddress` lives in `integration-zigbee`, not `integration-api`** — the request, the window and the events (`com.homesynapse.integration`) cannot name it; the scope crosses as a STRING | `git ls-files \| grep IEEEAddress.java`; `grep -n requires integration/integration-api/src/main/java/module-info.java` | the one file is `integration/integration-zigbee/…/IEEEAddress.java`; `com.homesynapse.integration` never requires zigbee (§5). The pre-verification's `Optional<IEEEAddress> scope` (forks 1, 6) is CORRECTED: `String scope`, nullable, canonical `0x` + 16 upper-case hex (`IEEEAddress.toString()`, `:84–`); `fromHexString` (`:68`) parses it in the adapter |
| 16 | The port that builds the request is the COMPOSITION ROOT's | `grep -n 'new PairingWindowRequest(' L/HomeSynapseCore.java` | `:1307` in `openPairingWindow(…)` `:1298` → `supervisor.openPairingWindow(id, request)` → `new PairingWindowView(…)`; the port `api/rest-api/…/PairingWindowPort.java:40`; the view `:53` |
| 17 | The window events are published at schema version 1 by one helper | `sed -n '1107,1119p' Z/ZigbeeIntegrationAdapter.java` | `publishWindowEvent(String, DomainEvent)` → `new EventDraft(eventType, 1, …)`; five call sites; J1's v2 form: `AVAILABILITY_CHANGED_SCHEMA_VERSION = 2` `A:193`, passed at `A:1789` |
| 18 | The sealed hierarchy and the codec manifest pin their counts | `sed -n '25,26p' IA/PairingWindowEvent.java`; `grep -n 'LIFECYCLE_EVENT_CLASSES =\|PermitJoinClosed.class' IA/IntegrationEvents.java`; `grep -n 'hasSize\|containsExactly'` on `PairingWindowEventTypeAnnotationTest.java` and `EventTypesTest.java` | `permits PermitJoinOpened, PermitJoinClosed` (:26); the manifest `:55–68`; the test pins 2 permits (:90), 10 lifecycle permits (:93), the manifest 12 + `subList(10, 12)` (:101–103); `EventTypesTest.java:46` `hasSize(75)` |
| 19 | The constructors have few callers; the listener has two test impls; the protocol interface none | §6's `git grep` lines | the counts of §6; the listener impls at `FixtureReplayTest.java:105`, `ZclIngestionUnitTest.java:125` (main: `A:1524`); every hit is a §3 row or a named [INFO] |
| 20 | Frozen log pins J2 must not move | `grep -n containsExactly` on `ZigbeeInterviewOnRejoinTest`, `ZigbeeKeyEstablishmentTest`, `ZigbeePermitJoinTest`; `grep -n permit_join_opened ../nexsys-bench/tools/bench.sh` | `device_join` (:304, :522), `device_join_failed` (:671), `key_establishment_failed` (:141, :157, :193), `permit_join_opened: duration=120s …` (:157), the event sequences (:191, :378, :396, :441); `bench.sh:132` watches the open line |
| 21 | The endpoint's `data` is a hand-built map, keys as written | `sed -n '217,226p' R/PermitJoinEndpoint.java`; `grep -n durationSeconds` on `PermitJoinEndpointTest.java` | `data.put("durationSeconds", …)` (:220) — map keys pass through (THE WIRE'S CASE: read the test's literal first); `ApiResponse.java:14`'s SNAKE_CASE is for POJO properties, not these |
| 22 | The bench's run grader whitelists `EventTypes` at a pin | `sed -n '139,146p' ../nexsys-bench/tools/verify72h/grader.py` | "every EventTypes constant at e96dce8" (:141) — `join_rejected` is NOT in it; a bench row follows the landing (a named [INFO]) |

## §1 What this implements
**J2b.** A window may be SCOPED to one device: `POST …/permit-join` with an optional `"scope": "0x<16 hex>"` opens a window whose transient key names that IEEE as its partner (the import's first 8 bytes instead of `0xFF × 8`) under TC policy **0x0013** (`ALLOW_JOINS | ALLOW_UNSECURED_REJOINS | JOINS_USE_INSTALL_CODE_KEY`), so the trust center DENIES a joiner without a transient-key entry; the DENY (today's WARN at `I:500–502`) also becomes the STORE EVENT `join_rejected` (the joiner, the window's scope). The un-scoped open is UNCHANGED (0x0003 + the wildcard key). Every close — elapsed · superseded · reopened · shutdown — runs the NCP's three-act close (0x006B → policy 0x0002 → `permitJoin(0)`) before the record's `permit_join_closed`; a failed NCP close is a WARN; the record still closes.

**Compensating cuts** — redundant or superseded text; none load-bearing after the edits: The accepted-rejoin admission (`A:1661`) checks the scope. `permit_join_opened` → schema **2** (+ nullable `scope`); a v1 row decodes to the same class.
**J2a.** After `rehydrateAdoptionMaps()` (`A:392`), every IEEE in `adoptAcceptList` that the announce cache knows and the adoption maps do not is scheduled on the interview queue with `Source.BOOT_LISTED`; the interview proposes (`S:305` stays the one site).
**IR-115.** Beside the WARN at `I:570` (unchanged) the adapter logs `zigbee.transient_key_expired: partner={} scope={}` when the partner is the scoped window's IEEE or all-zeros. **IR-123.** One INFO per `ReportingPostureFact` beside `A:1330`: `zigbee.reporting_cluster: device={} endpoint={} cluster=0x{} attribute=0x{} posture={} authoritative={}`.

## §2 Files to read before starting (the minimum read set; by range)
Z = `integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/`; IA = `integration/integration-api/src/main/java/com/homesynapse/integration/`; R = `api/rest-api/src/main/java/com/homesynapse/api/rest/`; L = `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/`; EM = `core/event-model/src/main/java/com/homesynapse/event/`.
- The pre-verification whole (19.5 KB; §1 your premise rows · §3 the forks · §4 the rig pre-registrations).
- `Z/EzspCoordinatorProtocol.java` :100–110, :185–240, :1002–1012, :1035–1066, :1079–1150, :1217–1230, :1455–1465, :1545–1552, :1582–1592 · `Z/CoordinatorProtocol.java` :29–80.
- `Z/ZigbeeIntegrationAdapter.java` :190–200, :260–270, :356–401, :600–612, :993–1017, :1049–1098, :1107–1119, :1326–1334, :1397–1402, :1470–1474, :1527–1532, :1634–1676, :1760–1795 (J1's v2 publish — the form).
- `Z/ZclIngestionUnit.java` :135–200, :473–503, :534–571 · `Z/PendingInterviewQueue.java` :30–75 · `Z/ZigbeeDeviceCache.java` by `grep -n 'public '` · `Z/ReportingPostureFact.java` :27–36 · `Z/ConfirmationOverrideInstaller.java` :195–210 · `Z/IEEEAddress.java` :31, :60–90.
- `IA/PairingWindowRequest.java`, `IA/PairingWindow.java`, `IA/PermitJoinOpened.java`, `IA/PairingWindowEvent.java` whole · `IA/PermitJoinClosed.java` :20–60 (the causes) · `IA/IntegrationEvents.java` :50–70 · `EM/EventTypes.java` :300–315 + the tail.
- `R/PairingWindowPort.java` whole · `R/PermitJoinEndpoint.java` :28–40, :130–230 · `L/HomeSynapseCore.java` :1295–1325 · the five `module-info.java` (§5) · the five `MODULE_CONTEXT.md` by `grep -n -i 'permit_join\|PairingWindow\|FROZEN\|IngestionListener'` · the tests of §3 rows 16–31, each by `grep -n 'containsExactly\|hasSize\|@Test'` first.

## §3 Files to create or modify (the Files table governs; A = added, M = modified)
| # | Path | A/M | What |
|---|---|---|---|
| 1 | `Z/CoordinatorProtocol.java` | M | `void enableScopedKeyJoins(IEEEAddress partner)`; `void closeJoinWindow()`; Javadoc naming the frames and policy bytes; no `default` bodies |
| 2 | `Z/EzspCoordinatorProtocol.java` | M | constants with DERIVATION comments — `DECISION_ALLOW_SCOPED_KEY_JOINS = 0x0013` (0x0001 \| 0x0002 \| 0x0010; `ezsp-enum.h:420–439`, v4.4.3), `DECISION_ALLOW_REJOINS_ONLY = 0x0002`, `FRAME_CLEAR_TRANSIENT_LINK_KEYS = 0x006B` (`:755–757`); the two methods (§4.1, §4.2) |
| 3 | `Z/ZigbeeIntegrationAdapter.java` | M | §4.1–§4.4; IR-123's loop after `:1332`; `PERMIT_JOIN_OPENED_SCHEMA_VERSION = 2` beside `:193`; `publishWindowEvent(String, int schemaVersion, DomainEvent)` — five call sites: opened 2, closed 1, rejected 1 |
| 4 | `Z/ZclIngestionUnit.java` | M | `IngestionListener` + `void onJoinDenied(IEEEAddress joiner, String status, String decision)`, `void onKeyEstablishment(IEEEAddress partner, int status)`; the calls after the WARNs at `:500–502` and `:570` (texts UNCHANGED) |
| 5 | `Z/PendingInterviewQueue.java` | M | `Source.BOOT_LISTED("boot_listed")` + Javadoc; the vocabulary comment |
| 6 | `IA/PairingWindowRequest.java` | M | `+ String scope` (nullable); `SCOPE_PATTERN = "^0[xX][0-9a-fA-F]{16}$"`; a non-matching non-null scope → `IllegalArgumentException`; CANONICALIZED to `0x` + upper-case; Javadoc |
| 7 | `IA/PairingWindow.java` | M | `+ String scope` (nullable), mirrored |
| 8 | `IA/PermitJoinOpened.java` | M | `+ String scope` (nullable; not required by the compact constructor); Javadoc version history (1: seven fields, PJ-2; 2: + `scope`, J2) |
| 9 | `IA/JoinRejected.java` | A | `@EventType(EventTypes.JOIN_REJECTED) public record JoinRejected(IntegrationId integrationId, String integrationType, String joiner, String scope, String status, Instant at) implements PairingWindowEvent` — `scope` nullable, the rest non-null; Javadoc: "a device that is not yours tried to join" (D-v94-24) |
| 10 | `IA/PairingWindowEvent.java` | M | `permits PermitJoinOpened, PermitJoinClosed, JoinRejected` |
| 11 | `IA/IntegrationEvents.java` | M | `LIFECYCLE_EVENT_CLASSES` + `JoinRejected.class` APPENDED (13) |
| 12 | `EM/EventTypes.java` | M | `JOIN_REJECTED = "join_rejected"` after the PJ-2 block in the file's convention (76) |
| 13 | `R/PairingWindowPort.java` | M | `open(IntegrationId, int, String reason, String actor, String scope)`; `PairingWindowView` + `String scope` (nullable) |
| 14 | `R/PermitJoinEndpoint.java` | M | the optional `"scope"` body key — absent/`null` → unscoped; present → textual, matching the pattern, else `INVALID_PARAMETERS` "scope must be 0x followed by 16 hex digits"; `respondOpened` puts `"scope"` ONLY when non-null; the Javadoc body line |
| 15 | `L/HomeSynapseCore.java` | M | `openPairingWindow(id, duration, reason, actor, scope)` → `new PairingWindowRequest(duration, reason, actor, scope)`; the view's `scope` |
| 16 | `Z/…/ZigbeePermitJoinTest.java` | M | T1–T4; `defaultResponses` :593–:601 gains the 0x006B arm (`new byte[0]`, the :594 form; unanswered frames never return on the TestClock; `resumeHandler` :556 rides it); T4b :405–:419 REWRITTEN (three 0x0022; `SET_POLICY, PERMIT_JOINING` between the enablements); :396 stays |
| 17 | `Z/…/ZigbeeTrustCenterJoinTest.java` | M | T5; §A-4's `nonWindowEvents()` pin :296–:297 goes RED BY DESIGN → ONE `join_rejected` |
| 18 | `Z/…/ZclIngestionUnitTest.java` | M | T6; its listener impl (:125; :66 is the field) gains the two methods |
| 19 | `Z/…/FixtureReplayTest.java` | M | its listener impl (:105) gains the two methods (no-op) |
| 20 | `Z/…/ZigbeeInterviewOnRejoinTest.java` | M | T7; the pins at :304, :522, :671 UNCHANGED; T6's :678–:679 RED BY DESIGN (ONE `join_rejected`); `defaultResponses` :947 gains the 0x006B arm |
| 21 | `Z/…/EzspProtocolTest.java` | M | T8 |
| 22 | `Z/…/PendingInterviewQueueTest.java` | M | T9 |
| 23 | `Z/…/ZigbeeBootListedProposalTest.java` | A | T10 (J2a), on `ZigbeeAvailabilityWiringTest`'s `initialize()` form |
| 24 | `Z/…/ZigbeeKeyEstablishmentTest.java` | M | T11; the pins at :141, :157, :193 UNCHANGED; its handler :546–:576 lacks the enablement arms T11's scoped open needs (copy ZigbeePermitJoinTest :586–:592) |
| 25 | the test covering `A:1326–1334` (`git grep -l reporting_configured -- '*Test.java'`; the lane names it) | M | T12 |
| 26 | `integration/integration-api/src/test/…/PairingWindowEventTypeAnnotationTest.java` | M | the permits → three (:90); the manifest `hasSize(13)` + `subList(10, 13)` (:101–103); the ten lifecycle permits UNCHANGED; `EXPECTED_RECORDS` :35–:37 stays two (:64 pins the `permit_join_` prefix); `JoinRejected` asserted apart |
| 27 | the request's test in integration-api (`git grep -l 'new PairingWindowRequest(' -- '*Test.java'`) | M | T13 |
| 28 | `core/persistence/src/test/…/EventPayloadCodecTest.java` | M | T14 (:349–:357 is the form; `AllEventClasses` :51 must carry the type) |
| 29 | `core/event-model/src/test/…/EventTypesTest.java` | M | `hasSize(76)` |
| 30 | `api/rest-api/src/test/…/PermitJoinEndpointTest.java` | M | T15; `RecordingPort` :308/:340/:347 gains `scope` |
| 31 | the lifecycle test driving `openPairingWindow` (`git grep -l openPairingWindow -- 'lifecycle/**/*Test.java'`; none → a named [INFO]) | M | T16 |
| 32 | the five `MODULE_CONTEXT.md` (zigbee · integration-api · event-model · rest-api · lifecycle) | M | rows only (§8) |
| 33 | `Z/ZigbeeDeviceCache.java` | — | NOT modified: `cache.device(ieee)` (:401) → `ZigbeeDeviceRecord.networkAddress()` IS the lookup; a named [INFO] |

## §4 Technical specification
### §4.1 The scoped open (fork 1 → `String scope`; fork 2 → 0x0013)
Scoped = `request.scope() != null` → `IEEEAddress.fromHexString(scope)` → `protocol.enableScopedKeyJoins(ieee)`: `setPolicy(TRUST_CENTER, 0x0013)` → `setPolicy(TC_KEY_REQUEST, 0x51)` (as today) → `FRAME_IMPORT_TRANSIENT_KEY` with the partner's 8 bytes little-endian — mirror the ENCODE at `E:1586–1590` (`eui64[i] = (byte) (value >> (8 * i))`, the inverse of `KeyEstablishment.parse` :1224–1227); T8 pins `78 56 34 12 00 4B 12 00` for `0x00124B0012345678`. Un-scoped: today's `enablePreconfiguredKeyJoins()` byte for byte. The `PairingWindow` carries the scope. A protocol failure at the open propagates as today; :1003–:1006 MOVES ahead of :998 (§4.2's fence) and nulls `permitJoinDeadline` — a failed open then leaves no window on either side.
### §4.2 The close (fork 3 → every cause, with the fence)
THREE closers (`A:1071`): `closeWindowIfElapsed` :1049 (run thread), `closePrior` :1063 (superseding), `closeWindow(cause)` :1079 (reopen :1219, shutdown :1092) — each CAS WINNER (:1054, :1004, :1081) calls a private `closeOnNcp()` before its publish; `open == null` sends NOTHING. `closeOnNcp()` = `protocol.closeJoinWindow()` in a try: `execute(FRAME_CLEAR_TRANSIENT_LINK_KEYS, NO_PARAMETERS, DEFAULT_COMMAND_TIMEOUT_MILLIS)` (3-arg `E:1455`, no `requireSuccess` — `ping()` `E:1417`) → policy 0x0002 → `permitJoin(0)`; a `RuntimeException` → WARN `zigbee.permit_join_ncp_close_failed: cause={}: {}`; the record still closes. A superseding open runs `closePrior` (:1063) to completion BEFORE the new enablement — never between a policy write and a key import; `closeWindowIfElapsed` (run thread) is a second NCP writer: `closeOnNcp()` and the enablement share one lock, and the close re-checks `currentWindow.get() == null` inside it. 0x006B's response has NO status byte (bellows `(0x006B, (), ())`; arrival is success). Between windows the standing TC policy is 0x0002 where 0x0003 lingered — §13's P5.
### §4.3 The admission, the events, IR-115
`admitRejoinCandidate` (`A:1661`): a scoped window and `device ≠ scope` → `log.debug("zigbee.rejoin_candidate_ignored: device={} reason=outside_scope scope={}", …)` and return; else as today. `onJoinDenied(joiner, status, decision)` → `publishWindowEvent(EventTypes.JOIN_REJECTED, 1, new JoinRejected(context.integrationId(), context.integrationType(), joiner.toString(), scopeOrNull, status, clock.instant()))` — the ADAPTER publishes (the unit stays event-free, `I:534`). `onKeyEstablishment(partner, status)` → §1's INFO when `partner` is the open or last-closed scoped window's IEEE, or all-zeros.
### §4.4 J2a (fork 4 → boot only)
Once per `initialize()`, right after `interviewQueue = new PendingInterviewQueue(clock)` (`A:401`; at :392 the queue is null): `proposeListedCachedDevices()` — per listed IEEE: no cache entry → DEBUG `zigbee.boot_listed_skipped: device={} reason=not_cached`; nwk 0xFFFF (cache :503) → `reason=address_unknown`; adopted (`adoption.deviceIdFor`, :1663) → DEBUG `reason=already_adopted`; else `interviewQueue.schedule(ieee, nwk, Source.BOOT_LISTED)` + `log.info("zigbee.boot_listed_candidate: device={} nwk=0x{}", …)`. A sleepy device rides the queue's ladder and parks; nothing is adopted without a completed interview. No epoch trigger.

## §5 The module boundaries (verbatim at `df2bc62`; NO proposed change to any — the scope is a `String`; the new record is inside `com.homesynapse.integration`)
```java
module com.homesynapse.integration.zigbee {
    requires transitive com.homesynapse.integration;
    requires com.fazecast.jSerialComm; // explicit JPMS module (ships module-info.class); interior-only per D-M92-1
    requires org.slf4j; // plain (implementation-only): Doc 08 §3.3 mandates structured log entries (LTD-15)
    requires com.fasterxml.jackson.databind; // plain (implementation-only): the M9.3 JSON profile loader + device cache; no Jackson type on any exported signature (the D-M92-1 pattern)
    exports com.homesynapse.integration.zigbee;
}
```
```java
module com.homesynapse.integration {
    requires transitive com.homesynapse.platform;
    requires transitive com.homesynapse.event;
    requires transitive com.homesynapse.device;
    requires transitive com.homesynapse.state;
    requires transitive com.homesynapse.persistence;
    requires transitive com.homesynapse.config;
    requires transitive java.net.http;
    exports com.homesynapse.integration;
}
```
`com.homesynapse.event` (`core/event-model/src/main/java/module-info.java`, 9 lines: requires transitive value · platform; exports event), `com.homesynapse.api.rest` (`api/rest-api/…`, 43 lines) and `com.homesynapse.lifecycle` (`lifecycle/lifecycle/…`, 102 lines; it already `requires com.homesynapse.api.rest` and `requires transitive com.homesynapse.integration`) are read whole by the lane and left UNCHANGED. The two embeds above omit their comment blocks; the lane diffs each against its file and STOPS on any difference. Locked decisions that bind: D-M92-1 (no Jackson type on an exported signature — `scope` is a `String`); REG-INV-1 (no registry write outside `RegistryProjection` — J2a writes none); LTD-15 (structured log lines); IR-101 (the landing is gated); THE LANE STOPS AT A LOCK.

## §6 The P2 consumer/pin survey (the hub's counts at `df2bc62`; the lane re-runs each before writing and pastes the counts)
`git grep -n -F '<s>' -- '*.java'` (main / test): `new PairingWindowRequest(` 1 / 8 · `new PairingWindow(` 1 / 2 · `new PermitJoinOpened(` 1 / 2 · `new PairingWindowView(` 1 / 1 · `implements CoordinatorProtocol` 1 / 0 · `publishWindowEvent(` 5 / 0 · `LIFECYCLE_EVENT_CLASSES` 7 / 7 · `enablePreconfiguredKeyJoins` 5 / 0 · `IngestionListener` 12 / 3 · `PairingWindowPort` impls 1 / 1 · `openPairingWindow(` in `*Test.java` (each closer needs the 0x006B arm) · `grep -c FROZEN integration/integration-zigbee/MODULE_CONTEXT.md` 10 (none names a J2 surface — confirm with `… | grep -i 'permit\|join\|transient'` = 0) · the pins of §0b row 20. **The miss-script sweep (#28):** before, a listed, cached, unadopted device got nothing at boot (IR-114); now one `schedule`.

## §7 Test requirements (red first; each named in the return with its red text)
T1 scoped open → `setPolicy(TC, 0x0013)` + the import's first 8 bytes = the partner (wire order) · T2 un-scoped open → today's bytes exactly (0x0003; `0xFF × 8`) · T3 the elapsed close → 0x006B, policy 0x0002, `permitJoin(0)`, then `permit_join_closed`; the pinned sequences hold · T4 a superseding open → the close's three frames complete before the new policy write · T5 a `DENY_JOIN` → `onJoinDenied` → ONE `join_rejected` with `joiner` and `scope` · T6 the unit calls both listener methods; the WARN texts unchanged · T7 a candidate outside a scoped window → not scheduled, `reason=outside_scope`; inside → as today · T8 row 2's frames, byte-exact · T9 `Source.BOOT_LISTED.token() == "boot_listed"` · T10 `initialize()` with a listed, cached, unadopted IEEE → one `schedule(…, BOOT_LISTED)`; adopted → none; unlisted → none · T11 a key-establishment status for the scoped partner → the INFO; a foreign partner → none; the three WARN pins green · T12 one `reporting_cluster` line per fact · T13 the request's scope validation and canonical form · T14 the codec v1 decode and the new type's round-trip · T15 the endpoint: valid scope (canonical on the wire), invalid (the problem text), absent (no `scope` key) · T16 the port's pass-through.
**Tests inject the module's `TestClock`** (`TestClock.createDefault()` + `advance`, ZigbeePermitJoinTest :97/:173 — `Clock.fixed` cannot elapse a window); never `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, `System.currentTimeMillis()`. `NO_DIRECT_TIME_ACCESS` (app's ArchUnit) scans production code only — this convention is PM-reviewed, not `check`-enforced.

## §8 MODULE_CONTEXT.md — rows only
zigbee: the scoped window (the policy table 0x0003 / 0x0013 / 0x0002 with the gsdk cites; the partner bytes; the three-act close and its fence; the two listener methods and their events/lines; J2a; IR-123) · integration-api: the three records + `scope`; `JoinRejected`; permits 3; the manifest 13 · event-model: `EventTypes` 75 → 76 · rest-api: the body's optional `scope`; the view's `scope` · lifecycle: the port's `scope`. One dated row each, the WU id.

## §9 What to watch out for
- The EUI64's BYTE ORDER is this unit's trap — the wildcard hid it; mirror `E:1586–1590`, pin it in T8.
- A record component added breaks EVERY canonical-constructor caller (§6) — each a §3 row or a named deviation; never a second constructor.
- §0b row 20's pins are frozen tokens (#31): add beside them, never edit.

## §10 Coder pushback welcome
**If J2a and J2b can land as TWO staged trees in sequence (J2a first), say so in the plan's §4 with the file split — the hub prefers it (D-v97-5).**

## §11 Out of scope
A `closed_by_operator` cause and a close endpoint · the dashboard · any bench file · the nightly · `MODULE_CONTEXT.md` prose beyond §8 · the Hue · IR-122 · any registry, device or entity write · the Pi.

## §12 The plan's shape (`<CT-date>_J2_plan.md`, ≤ 8,192 B; written FIRST; the lane STOPS after it)
§0 the premise rows 1–22 re-run — one line each: the output or "holds" with the line; a failing row and why · §1 the forks settled (the byte order; the listener impls; the J2a/J2b split), each with the BYTES · §2 the Files table as you will write it (A/M; the count; the census) · §3 the tests first, each with its predicted red · §4 risks and pushback (§10) · §5 the return cap re-computed. Last line: `PLAN-RETURNED <path> <bytes>`. Then wait for `GO`.

## §13 Success criterion (binary)
`./gradlew check` green on the branch, every §7 test green after an observed red; a v1 and a v2 `permit_join_opened` row decode to the same class; `join_rejected` round-trips; the endpoint's three cases; the staged tree named in the return's last line. On the rig (after the landing; R6's first card or REHEARSAL 3 — not the soak night, which runs J1's core): the pre-verification §4's P1–P4 verbatim, plus **P5** — a join attempt between windows reads NO 0x0024 (P3's MAC refusal); a 0x0024 that does arrive (a router still permitting) reads `decision=DENY_JOIN`; `USE_PRECONFIGURED_KEY` there REFUTES §4.2's reading.

## §14 Work unit completion (WUCP Phase 1)
The return (§0); the coder-handoff entry; the deviations ledger; the MODULE_CONTEXT rows (§8); the tree STAGED, un-committed, un-pushed, its `git write-tree` sha in the return's last line.

## §15 The dispatch (Nick pastes the line below into Claude Code in `~/Desktop/Code/ClaudeFolder/homesynapse-core`)
```
You are the J2 Coder lane (the scoped recovery window + the boot re-proposal; IR-114/115/123) on my desk. Read ../nexsys-hivemind/context/instructions/2026-10-04_coder-lane_J2_scoped-recovery-window_IR-114_LOCAL_desk-coding-instruction.md WHOLE, then its §2 set by range. Execute §0 exactly: date -u first; porcelain empty; the branch; the premise rows re-run; the PLAN written to its path and STOP at PLAN-RETURNED. No code before my GO. You stage, never commit.
```
