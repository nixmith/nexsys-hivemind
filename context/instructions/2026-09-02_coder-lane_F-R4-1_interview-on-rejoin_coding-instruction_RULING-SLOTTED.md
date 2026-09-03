<!--
file: context/instructions/2026-09-02_coder-lane_F-R4-1_interview-on-rejoin_coding-instruction_RULING-SLOTTED.md
purpose: F-R4-1 — THE SILENT-REJOINER ADOPTION GAP: the coding instruction for the first Coder WU of wk 2, authored AHEAD at v61 beat 5 (Wed 2026-09-02 ~20:06 CT, instrument 01:06Z) against R-10 Row 10 (`context/planning/2026-09-02_R10-docket_ruling-cards_v61-b3.md`). RULING-SLOTTED: §0 carries the design ruling as the sitting's word fills it; everything below is authored to the rec (a). Grounded at SOURCE this session (integration-zigbee at core HEAD `f519f42`: `ZclIngestionUnit.java` :104–:118 (the listener) · :275–:312 (`handleTrustCenterJoin` — THE M9.4-TCJ PIN) · :386–:397 (the unknown-sender skip) · `ZigbeeIntegrationAdapter.java` :471–:478 (`isPermitJoinActive`) · :753–:769 (`openPermitJoinWindow`) · :1115–:1121 (`onDeviceAnnounce` → `cache.recordAnnounce` + `interviewQueue.schedule`) · `EzspCoordinatorProtocol.java` :218–:236 + :1042–:1105 (`TrustCenterJoin`, `accepted()`) · `PendingInterviewQueue.schedule(IEEEAddress,int)` :81 · `ZigbeeAdoptionSlice` (`relink` :515; `device_proposed` :253; `device_adopted` :416–:434); module-info verbatim below) and at the EVIDENCE (R-3a return :1256–:1344 — the mains fleet SILENT after the outage; only the battery sensor produced a `SECURED_REJOIN` 0x0024 · R-4 record :149 — inside the 254 s window the Hue-class device spoke ONLY as `ingestion_unknown_sender nwk=0xf87d`, no announce, no join callback).
audience: the Coder lane (host-side, compile-loop; `nexsys-coder`) · Nick (the commit + push — CORE IS NICK'S HANDS) · the hub (the two-layer audit at the return)
state-type: coding instruction (Phase 3 — tests first)
status: AUTHORED AHEAD — RULING-SLOTTED. Dispatches when §0's slot reads RULED. Return: `context/audits/<CT-filing-date>_F-R4-1_return.md` (≤12 KB; §0 first; the porcelain census; the deferred-gate line; instrument limits disclosed).
-->

# Coding Task: F-R4-1 — interview-on-rejoin (the silent-rejoiner adoption gap)

**Subsystem:** integration-zigbee (`com.homesynapse.integration.zigbee`) · **Design Doc:** Doc 08 (Device Model, LOCKED) + Doc 18 seams as constraints; the adoption doctrine per R-10 Row 10 · **Phase:** 3-Implementation (tests first) · **Task Brief Reference:** R-10 additions item 1 (F-R4-1) + R-4 record F-R4-1 + Row 10.

## §0 THE RULING SLOT
**Row 10 word:** ⟨RULED: (a) | EDIT: … | HOLD⟩. Authored to **(a)**: *relink ≠ adopt; a KNOWN-network-but-UNADOPTED device that speaks DURING an open permit-join window is interviewed by the SAME path as an announce-class device and adopted by the same path (`device_proposed` → `device_adopted`); outside a window it is logged ONCE per invocation and ignored for adoption. Failed/denied joins stay observability-only (the never-synthesize rule holds).* **The M9.4-TCJ §A.2 PIN IS AMENDED BY THIS RULING** for exactly the accepted-rejoin-during-window case; every other sentence of the pin stands.

## What This Implements
The shipped pipeline (`f519f42`) starts adoption ONLY at ZDP Device_annce (`IngestionListener.onDeviceAnnounce` → `cache.recordAnnounce` + `interviewQueue.schedule`). A mains router that holds the network key rejoins on its own authority — usually BEFORE the service is listening — sends no announce the service sees, and thereafter every frame it sends lands as `zigbee.ingestion_unknown_sender … frame skipped` (`ZclIngestionUnit` :386–:397): it reports forever and never proposes. This WU adds the second admission path — **interview-on-rejoin** — with two hooks feeding the ONE existing interview path: (H-ii, primary — the evidenced case) an unknown-sender frame while `isPermitJoinActive()` → resolve the sender's IEEE → schedule the interview; (H-i, secondary — cheap, same path) an ACCEPTED 0x0024 (`SECURED_REJOIN`/`UNSECURED_REJOIN`, not denied) for a device NOT in the adoption maps while the window is open → schedule the interview. It makes R-4b's C4 (the fleet re-adopted on the shipped artifact) REACHABLE, which is C-002's road.

## Files to Read Before Starting
| File | Why |
|---|---|
| `integration/integration-zigbee/MODULE_CONTEXT.md` — §M9.4-TCJ (:431–:452) · §M9.4-ADP (:471–:490) · §M9.4-PJ (:414–:430) · §M9.6-RO (:593–:614) · §WU-AVAIL-SEED (:713–:736) · Gotchas (:197–:214) | the pin you are amending; the adoption path's contracts; the permit-join semantics; reopen identity capture; availability seeding — DO NOT feed availability from a join callback |
| `integration/integration-zigbee/src/main/java/module-info.java` | verbatim below — no new `requires` |
| `integration/integration-api/MODULE_CONTEXT.md` + its `module-info.java` | the adapter contract; `IntegrationContext` (clock, config) |
| `core/device-model/MODULE_CONTEXT.md` · `core/event-model/MODULE_CONTEXT.md` (the event-versioning / additive-field rule) | `device_proposed` / `device_adopted` are event-log facts — read the versioning rule BEFORE touching any event payload |
| `ZclIngestionUnit.java` :104–:130 · :240–:330 · :360–:410 | the listener, `handleTrustCenterJoin`, the unknown-sender skip |
| `ZigbeeIntegrationAdapter.java` :200–:220 · :460–:480 · :740–:770 · :1110–:1125 · :1020–:1035 | `permitJoinDeadline`/`isPermitJoinActive`, `openPermitJoinWindow`, `onDeviceAnnounce`, the relink call site |
| `EzspCoordinatorProtocol.java` :150–:240 · :1040–:1110 · the frame-send path used by `permitJoin` | `TrustCenterJoin`; the EZSP request/response idiom you extend for the lookup |
| `PendingInterviewQueue.java` · `ZigbeeDeviceCache.java` (`recordAnnounce`) · `ZigbeeAdoptionSlice.java` :96–:110 · :240–:270 · :410–:440 · :505–:560 | the interview queue; the cache; the proposal → adopted path; `relink` (what NOT to do here) |
| the existing TCJ test(s) locking the pin (find: `grep -rl "never schedules an interview\|tc_join\|TrustCenterJoin" integration/integration-zigbee/src/test`) | the lock you re-pin WITH DISCLOSURE — the FE-HONEST-1 precedent: a lock may be re-pinned only when it encodes the chartered defect |

**module-info.java (verbatim, `integration/integration-zigbee/src/main/java/module-info.java`):**
```java
module com.homesynapse.integration.zigbee {
    requires transitive com.homesynapse.integration;
    requires com.fazecast.jSerialComm;
    requires org.slf4j;
    requires com.fasterxml.jackson.databind;
    exports com.homesynapse.integration.zigbee;
}
```
No JPMS change. No catalog change. (LTD-17 · Doc 15 zero-new-deps.)

## Files to Create or Modify
| Action | File | Description |
|---|---|---|
| MODIFY | `…/zigbee/ZclIngestionUnit.java` | H-ii: on unknown-sender + window open → `listener.onRejoinCandidate(nwk)`; H-i: in `handleTrustCenterJoin`, accepted + unknown + window open → `listener.onRejoinCandidate(eui64, nwk)`; the pin's Javadoc amended to cite this WU + Row 10 |
| MODIFY | `…/zigbee/ZclIngestionUnit.java` (`IngestionListener`) | + `onRejoinCandidate(IEEEAddress ieeeOrNull, int networkAddress)` (or two overloads) — Javadoc states the doctrine |
| MODIFY | `…/zigbee/ZigbeeIntegrationAdapter.java` | implements the new listener method: resolve IEEE if absent (see spec), then `cache.recordAnnounce(ieee, nwk)` + `interviewQueue.schedule(ieee, nwk)` — the announce path, reused, not duplicated; the once-per-invocation `zigbee.rejoin_ignored_window_closed` log |
| MODIFY | `…/zigbee/CoordinatorProtocol.java` + `EzspCoordinatorProtocol.java` (+ the mock/fake protocol in test-support) | + `Optional<IEEEAddress> lookupIeee(int networkAddress)` — EZSP `lookupEui64ByNodeId` (frame id 0x0061 PER BELLOWS — VERIFY the id and the layout against the bellows source the module already cites BEFORE encoding; request u16 nodeId; response u8 status + EUI64) — **THE ONE NEW SILICON SURFACE** (see Watch-outs) |
| CREATE | tests (below) | red-first |
| MODIFY | the TCJ pin test | re-pinned WITH DISCLOSURE in the return |
| MODIFY | `integration/integration-zigbee/MODULE_CONTEXT.md` | a `## F-R4-1 Implementation` block: deltas · gotchas · the amended pin |

## Technical Specification (the contracts; the Coder owns the shape within them)
1. **Doctrine (Row 10 (a)):** relink ≠ adopt. Adoption starts ONLY via the interview → proposal → adopted path. This WU adds admission TRIGGERS, never a bypass: `handleTrustCenterJoin` and the unknown-sender branch still NEVER create a device, NEVER feed availability, NEVER publish an event.
2. **Window gate:** both hooks fire ONLY while `isPermitJoinActive()` is true (the adapter's never-false-ALIVE deadline, :471–:478). Outside the window: H-ii logs `zigbee.rejoin_ignored_window_closed: nwk=0x… cluster=0x…` ONCE per (invocation, nwk) — a bounded set, cleared on `openPermitJoinWindow()` — then the existing `ingestion_unknown_sender` WARN continues as today (no behavior change outside the window beyond the one INFO).
3. **IEEE resolution (H-ii):** order: (1) the device cache's NWK→IEEE view if it has one (`ZigbeeDeviceCache`); (2) `protocol.lookupIeee(nwk)` — EZSP `lookupEui64ByNodeId`; (3) on miss → log `zigbee.rejoin_candidate_unresolved: nwk=0x…` once per (invocation, nwk); NO ZDO IEEE_addr_req in this WU (a second over-the-air surface is a second WU if (2) misses on silicon at R-4b).
4. **The interview path is REUSED:** `cache.recordAnnounce(ieee, nwk)` + `interviewQueue.schedule(ieee, nwk)` exactly as `onDeviceAnnounce` does (:1119–:1121). The proposal's provenance rides the LOG LINE (`zigbee.device_proposed: … source=rejoin|announce`) and the `InterviewAttempt` record if it has a reason slot — **NOT the event payload** unless `core/event-model/MODULE_CONTEXT.md`'s additive-field rule makes it a zero-cost additive key; if it does, propose it in the return as a follow-on, do not ship it here (the frozen event-log contract check).
5. **Dedup/idempotence:** a device already in the adoption maps never re-enters via these hooks (the resolver hit is the gate); a candidate already queued is not re-queued (`PendingInterviewQueue` semantics — read before asserting).
6. **Logging (LTD-15 structured):** every new line is `zigbee.<snake_case>: k=v …`, Register C voice. New lines: `rejoin_candidate` (INFO: ieee, nwk, source=tc_join|unknown_sender) · `rejoin_ignored_window_closed` (INFO) · `rejoin_candidate_unresolved` (WARN).

## Event Types Produced or Consumed
Produces (unchanged types, via the existing path): `device_proposed` → `device_adopted`. This WU adds NO event type and NO payload field. Consumes: none new.

## Locked Decisions / Invariants That Must Hold
Doc 08 adoption doctrine (adoption is explicit and evidenced) · LTD-15 structured logging · LTD-17 (integration-zigbee depends only on integration-api) · Doc 15 zero-new-deps · the never-synthesize rule (failed/denied joins → observability only) · the never-false-ALIVE rule (`isPermitJoinActive` is the only window truth; availability is NEVER fed from a join callback — WU-AVAIL-SEED) · SK-INV-02 Clock injection (the once-per-invocation sets use no wall clock; if a timestamp is needed, `context.clock()`). **INV/LTD sweep owed in the return:** list every INV/LTD the touched files cite in their Javadoc and state MET/UNAFFECTED per item.

## Test Requirements (RED FIRST — predictions filed in the return)
Unit (hardware-free, the M9.4a hero-loop harness + the fake protocol): (T1) unknown-sender frame + window OPEN + lookup hit → `recordAnnounce` + `schedule` called once with the resolved IEEE — RED at HEAD (the frame is skipped today) · (T2) unknown-sender + window CLOSED → no schedule; `rejoin_ignored_window_closed` logged once per nwk per invocation; second frame logs nothing new — RED · (T3) unknown-sender + window OPEN + lookup MISS → no schedule; `rejoin_candidate_unresolved` once — RED · (T4) accepted 0x0024 SECURED_REJOIN for an UNKNOWN device + window OPEN → schedule once — RED · (T5) accepted 0x0024 for a KNOWN (adopted) device → NO schedule (today's relink path untouched) — GREEN-by-construction, disclosed · (T6) DENIED 0x0024 → observability only, never a schedule — GREEN-by-construction (the pin's surviving half), disclosed · (T7) window reopen clears the once-per-invocation sets — RED · (T8) `lookupIeee` frame encode/decode against the bellows-derived fixture (0x0061; status 0x00 + 8-byte EUI64; status ≠ 0 → empty) — RED. The TCJ pin lock: re-pin to "never schedules WITHOUT an open window / for a known device / on a denied join" — disclose the re-pin verbatim in the return.

## Code Quality Standards
Java 21 idioms as the module uses them; package-private by default; no public type added; every new log line has a test asserting its key set; `./gradlew :integration:integration-zigbee:compileJava :integration:integration-zigbee:test` GREEN in-session (targeted; `-Werror`-sensitive); the full `./gradlew check` is the DEFERRED GATE (Nick's sandbox-external environment) — name it in the return's Deferred Build Gate section with the commit it must run against.

## What to Watch Out For
- **THE ONE NEW SILICON SURFACE:** `lookupEui64ByNodeId` (0x0061) is authored from the bellows-derived spec and a fixture — NOT silicon-verified until R-4b's first ⏺ (the lookup returning the Hue-class device's EUI64 for its live nwk). The return says so verbatim; R-4b's packet makes it criterion 0. If silicon disagrees, the WU is NOT wrong — the hop was unmeasured by design and the fix rides R-4b's harvest.
- **Do not route through `relink`** (:515): relink is the KNOWN-device path (registry rebuild + maps). A rejoin candidate is by definition NOT in the registry.
- **`journalctl -b` scoping / once-per-invocation:** "invocation" = this adapter instance's lifetime, not the machine boot.
- **The unknown-sender branch is hot** (every frame from every unknown device): the window check is the FIRST test, the set lookup second, the protocol lookup LAST and only once per nwk per invocation.
- **The SK-INV-02 arch rule** (`NO_DIRECT_TIME_ACCESS`) runs only from `com.homesynapse.app`'s test classpath: non-app TEST code is a self-enforced convention — inject `Clock` in tests too.
- **MODULE_CONTEXT.md is part of the census** (the F-R4-1 block); the pin's Javadoc amendment cites Row 10.

## Coder Pushback Welcome
If the bellows frame layout for 0x0061 is not derivable with confidence from what the module already cites, STOP and return the question with the two candidates — do not guess a wire layout. If `PendingInterviewQueue` cannot be reused without change for a non-announce trigger, say why (evidence: the line), and propose the smallest change.

## Out of Scope
The ZDO IEEE_addr_req path · any event payload field · the custody/registry redesign (F-R4-2 is a docs row) · R-4b's packet · the FAILCHAN sweep · anything in `ZigbeeAdoptionSlice.relink`.

## Work Unit Completion (WUCP Phase 1 — the return's shape)
§0: verdict-first (what landed; the porcelain census EXACT — expected ≈ 6–8 M + N test files A; ZERO commits by the lane); the red-first table (T1–T8 predicted vs observed); the re-pin disclosed verbatim; the Deferred Build Gate line (`./gradlew check` on ⟨sha⟩); INV/LTD sweep; instrument limits; CT filing date. **THE MSG FILE (hub-authored at the audit, for Nick's hands):** `../_scratch/<date>_core_F-R4-1_commit-msg.txt` — "core: F-R4-1 — interview-on-rejoin … Stages exactly N = … (M …; A …)" — Nick reviews the diff, commits `-F`, pushes; CI verdict banks as one spine line (law 16). **THE CENSUS CARD** rides the audit beat.
