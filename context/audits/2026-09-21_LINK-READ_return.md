<!--
file: context/audits/2026-09-21_LINK-READ_return.md
purpose: the Coder lane's return for LINK-READ (the instruction of the same date, its §15 AUDIT CORRECTION 1 and §16 AUDIT CORRECTION 2 included)
baseline: core 13d439f · filed Mon 2026-09-21 ~13:2x CT (date -u first: Mon Sep 21 17:20:16 UTC 2026; census stamp 18:17:57Z) · this file: 13,678 B
-->
# LINK-READ — return

## §0 The verdict card
**DELIVERED.** `./gradlew check` GREEN on the lane's tree at `13d439f` (exit 0); uncommitted, unstaged, ZERO commits. Two forks were raised BEFORE the code they govern and ruled by the hub through Nick (§15, §16).

**What landed.** (1) A per-IEEE `LongAdder` in `route()`'s resolved branch, no line per frame. (2) The last-hop reading rides `onFrame(device, Optional<LinkReading>)` → `recordFrame(device, now, link)` → `DeviceState.lastLink/lastLinkAt`; every transition prints the SIBLING line `zigbee.availability_link: device= available= reason= last_lqi= last_rssi_dbm= last_link_at= frames_since_summary=` from the adapter's sink; the frozen DP-8 line is byte-identical (`StandardAvailabilityTracker.java:393`, was `:313`). (3) `LINK_SUMMARY_PERIOD = 10 min` with the rule in its Javadoc; `zigbee.link_summary: device= frames= last_lqi= last_rssi_dbm= last_link_at=` once per period per device. No event type, schema, module-info, Gradle or config change.

**Tests, red first.** Predictions filed 18:07:13Z, the stage-A run (seams declared, behavior inert) started 18:07:17Z: zigbee `678 tests completed, 12 failed` — the 12 predicted, each with its predicted text; T7 red in its own run. The three the instruction names:
- **T1** `StandardAvailabilityTrackerTest.lastLink_survivesTheSilenceTimeout`: `Expecting Optional to contain: LinkReading[lqi=200, rssiDbm=-45] but was empty.`
- **T4** `ZclIngestionUnitTest.frameCounter_countsResolvedHaFramesPreDedup_andDrains`: `expected: 3L but was: 0L`
- **T6** `EzspIncomingMessageTest`: the sign half is GREEN at HEAD, as §16 says (`:79` widens with sign). Its red is a MUTATION (`& 0xFF` injected at `:79`, reverted): `[lastHopRssi is s8: 0xC4 is −60 dBm, never 196] expected: -60 but was: 196`. The domain half was red at stage A: `Expecting Optional to contain: LinkReading[lqi=255, rssiDbm=-60] but was empty.`
Green, forced fresh (`--rerun`, 18:16:18–18:16:51Z; XML mtimes inside the window): zigbee **679** (1 skipped: `MeteringRateMeasurementTest`, env-gated) · lifecycle **94** · app **30** (ArchUnit); 0 failures.

**Deviations.** The hub's AUDIT CORRECTION 1 and 2 (§3), five lane notes ([REVIEW] ×1, [INFO] ×4).

**Census** — core, `git --no-optional-locks status --porcelain`, 12 = 9 M + 3 `??` = §3's eleven rows (row 7 is two files):
```
 M integration/integration-zigbee/MODULE_CONTEXT.md
 M integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/AvailabilityTracker.java
 M integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/StandardAvailabilityTracker.java
 M integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/ZclIngestionUnit.java
 M integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/ZigbeeIntegrationAdapter.java
 M integration/integration-zigbee/src/test/java/com/homesynapse/integration/zigbee/FixtureReplayTest.java
 M integration/integration-zigbee/src/test/java/com/homesynapse/integration/zigbee/StandardAvailabilityTrackerTest.java
 M integration/integration-zigbee/src/test/java/com/homesynapse/integration/zigbee/ZclIngestionUnitTest.java
 M integration/integration-zigbee/src/test/java/com/homesynapse/integration/zigbee/ZigbeeAvailabilityWiringTest.java
?? integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/LinkReading.java
?? integration/integration-zigbee/src/test/java/com/homesynapse/integration/zigbee/EzspIncomingMessageTest.java
?? lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/LinkReadIT.java
```
Nothing staged. Hivemind: the lane adds ONE `??`, this file; the tree's other 6 M + 10 `??` are the hub's (five `context/research/*` arrived during the lane). All touched files LF (`tr -cd '\r' | wc -c` = 0 each).

**Instrument limits:** §7 — chiefly: the rig carries ONE fixed pair; the counter sees the drain's frames only; `check` ran here with `--offline`, CI is the gate of record.

## §1 What changed (line numbers at the lane's tree)
1. `LinkReading.java` NEW (80 lines): public record; the compact constructor asserts `0..255` / `−128..127`, throws; `fromWire(int, int)` total, `:73`.
2. `ZclIngestionUnit.java` +132/−10: `onFrame(device, Optional<LinkReading>)` `:160`; `frameCounts` `:238`, `linkSuspectNamed` `:242`; `route()` package-private `:587` (D-1); the increment `:627`; `linkReadingOf` `:647` + `nameLinkSuspectOnce` `:659`; `framesSince` `:676`; `drainFrameCounts` `:693` (unsigned-IEEE `TreeMap`); `handleAnnounce(announce, message)` `:700` hands its reading `:711`, counts nothing.
3. `ZigbeeIntegrationAdapter.java` +104/−4: `NO_LINK_READING` `:185`; `lastLinkSummaryAt` `:264`, set in `initialize()` `:423`; `logLinkSummaryIfDue()` `:602`, called `:579` after `evaluateAvailabilityTimeouts()`; `linkFields` `:631`; `onFrame(device, link)` `:1315` → `recordFrame(device, now, link)` `:1327`; the sibling line `:1495`, first statement of `onTransition` `:1483`.
4. `AvailabilityTracker.java` +34/−2: `recordFrame(…, Optional<LinkReading>)` `:45`; `lastLink` `:58`; `lastLinkAt` `:68`.
5. `StandardAvailabilityTracker.java` +86/−6: `LINK_SUMMARY_PERIOD` `:79`; `DeviceState.lastLink/lastLinkAt` `:133–:134`; `recordFrame` `:184`; the getters `:193`, `:206`; `transition(…, LinkReading)` `:357` keeps the reading inside the lock `:366`, before the listener fires; the `:393` log statement untouched.
6. `StandardAvailabilityTrackerTest.java`: ELEVEN call sites migrated (`ANY_LINK` `:48`); T1 `:438`, T2 `:462`, T2-b `:481`, T3 `:505` — state only.
7. `FixtureReplayTest.java` `:111` (one line); `ZclIngestionUnitTest.java`: the listener records `linksSeen`; `incomingFrame(…, lqi, rssi, …)` `:1299`; T4 `:1146`, T5 `:1180`, T8 `:1208`, T9 `:1237`.
8. `EzspIncomingMessageTest.java` NEW (5 tests): literal bytes `:74`; the misdecode 196 refused `:96`; the wire corners `:115`; all 256 × 256 byte pairs through `parse` construct `:139`; truncation `:159`.
9. `LinkReadIT.java` NEW: T7 (§2).
10. `MODULE_CONTEXT.md` +30/−2: the `LinkReading` row, the `AvailabilityTracker` row, the LINK-READ section (tokens, gotchas).
11. `ZigbeeAvailabilityWiringTest.java` **+117/−0** (`git diff --numstat`; hunks `@@ -875,6 +875,106 @@` and `@@ -954,6 +1054,23 @@`; zero `-` lines): T1′ `:887`, T3′ `:915`, the pin `:946`, one `deliverReport` overload `:1063`. `:335` and `:870–:875` byte-unchanged and green.

## §2 The tests
Stage-A reds beyond §0: T2, T2-b, T5, T8, T9, T6 corners, T1′ (`Expected size: 2 but was: 0`), T3′, the pin (`Expecting actual: [] to contain exactly …`). T3 was predicted GREEN at stage A (absence is what an inert seam answers) and was. **T7** `LinkReadIT.summaryCountsFrames_andTheSilenceCarriesTheLastReading` (~1.3 s): three SNZB + two Hue frames → no zigbee line at INFO+ per frame; +10 min → exactly `frames=3` / `frames=2`; +25 h → `zigbee.availability_link: device=0x00124B0012345678 available=false reason=SILENCE_TIMEOUT last_lqi=176 last_rssi_dbm=-56 last_link_at=2026-01-01T00:00:00Z frames_since_summary=0`, the frozen line beside it, the next period's rows `frames=0`. Stage-A red: `[exactly one line per device…] Expecting actual: [] …`. No rig change was needed (`ZigbeeHardwareFreeRig.java:701–:702` carries 176 / −56).
Gates: `check` #1 18:12:14–18:12:51Z exit 0 (13 executed); +T6e, then `check` 18:15:52–18:15:58Z exit 0; then the forced-fresh run of §0. Evidence: `_scratch/v78/2026-09-21_LINK-READ_*` (predictions, red/green/mutation/check logs).

## §3 Deviations
**AUDIT CORRECTION 1 (the hub's; §15, "Mon 2026-09-21 ~12:3x CT; instrument 2026-09-21T17:33:25Z").** Said: extend `zigbee.availability_changed`. The tree: DP-8 froze it (`MODULE_CONTEXT.md:625`, `:731`); `ZigbeeAvailabilityWiringTest.java:335`, `:870–:875` pin it with `containsExactly`, outside §3's table. Did: the sibling line in the adapter's sink; row 11 added; T1′/T3′/the pin there; tracker tests assert state.
**AUDIT CORRECTION 2 (the hub's; §16, "~12:5x CT; instrument 2026-09-21T17:56:14Z").** Said: `rssiDbm ≤ 0`, thrown, built in `route()`. The tree: a correct s8 is −128..127 and `productionLoop()` (`ZigbeeIntegrationAdapter.java` `:857–:899` at HEAD) has no `RuntimeException` arm. Did: the wire domain in the type, `fromWire`, the `Optional` seam, the once-per-device `zigbee.link_reading_suspect` WARN, T8, T9. **The `Optional` pair was used, not the overload pair:** `java-patterns.md` holds no rule against `Optional` parameters (its two "optional" hits, `:559`, `:575`, are about default methods).
**D-1 [INFO]** `route()` private → package-private: `parse` cannot produce an out-of-domain pair, so T8 hands it a constructed message.
**D-2 [REVIEW]** "one line per device" is implemented as every CACHED device plus any counted one, unsigned-IEEE order, `frames=0` rows included, the first period from `initialize()`. A silent period is a count, not an absence; a seeded silent device prints `-`. The hub may prefer spoken-only.
**D-3 [INFO]** `EzspIncomingMessage.java` (not a row) was mutated twice for T6's red and reverted; `git diff --quiet` exit 0; absent from the census.
**D-4 [INFO]** Beyond §7's list: T2-b (an empty reading is liveness, keeps the prior) and T6e (256 × 256; added after green — mutation red: `[wire bytes lqi=0x00 rssi=0x80] … but was empty`).
**D-5 [INFO]** §10's question: the counter is PRE-dedup — `:627` precedes `isDuplicate` `:739`; the ×2 twin counts twice (T4 pins it), the rule DP-3 gives liveness. `LinkReading` must be public: it rides a public signature of the exported package under `-Xlint:all -Werror`.

## §4 The P2 survey as found
- `recordFrame` sites in `StandardAvailabilityTrackerTest`: **eleven**, not eight — §6 misses `:228`, `:350`, `:410`.
- The interface is `ZclIngestionUnit.IngestionListener`, not `Listener`; `:548` was a method reference, now a lambda.
- The frozen token (AC1) — a pin §6 did not cover. Nothing else failed to compile; no other module names either interface.

## §5 Findings for the register
- (a) **IR-46 candidate — the ingestion loop's failure posture:** no `RuntimeException` arm in `ZclIngestionUnit` or `productionLoop()`; a throw in any handler ends `run()` and drops the cycle's drained frames. Instrument: a handler that throws inside a test rig; assert the next frame is still processed.
- (b) **The T6 pin:** `EzspIncomingMessage.java:79` is a sign-extending widen; `& 0xFF` there is the defect T6 exists to catch (mutation-proven twice).
- (c) **Exchange-consumed responses are neither counted nor read** (`awaitIncomingLocked`, `EzspCoordinatorProtocol.java:1785–:1817`): ping replies, interview reads, reporting configures. Instrument: `zigbee.availability_ping outcome=ok` lines against `frames=` in one sitting.
- (d) `frames_since_summary` on a real 25 h silence is 0 by construction; it informs inside the first period and on a ping-timeout edge.
- (e) The summary scales with the CACHE (N devices → N lines per period); the knob is §11's later unit.

## §6 The coder-handoff entry (for the hub's splice)
> **LINK-READ — the per-device frame counter; the last link reading on every transition; the sampling rule (CORE, integration-zigbee + one lifecycle IT; 12 = 9 M + 3 A, UNCOMMITTED) — DELIVERED (Mon 2026-09-21 ~13:2x CT).** `check` green on the desk; CI on the landing sha is the gate of record. The delta: `LinkReading` (wire domain + total `fromWire`) · `onFrame`/`recordFrame` carry `Optional<LinkReading>` · the counter in `route()` · `zigbee.link_summary` and `zigbee.availability_link` on the adapter · `zigbee.link_reading_suspect` once per device · `zigbee.availability_changed` FROZEN, untouched. AC1 + AC2 the hub's; D-2 awaits a ruling. NEXT WU: IR-40 + IR-44 (D-v78-1); LINK-READ-2 = IR-45. LINK-READ deploys to the bench card only after THE THURSDAY ORDER.

## §7 Instrument limits
- The rig carries ONE pair (176 / −56) on every frame: T7 proves the plumbing through the real core; variation is T5, T9, T1′. No raw 0x0045 frame is filed in the corpus — T6 is the spec layout at the measured range (`fixtures/2026-07-01_snzb-03p_…json:31–:32`).
- `reason=out_of_wire_domain` is unreachable through `parse` at HEAD (T6e); T8 reaches it by construction only.
- `drainFrameCounts()` is exact on the cycle thread only (`LongAdder.sumThenReset`).
- The frame path allocates the record, its `Optional` (AC2's seam) and the boxed IEEE key the module's maps already pay; no allocation instrument was run.
- `check` ran on Windows / JDK 21 with `--offline`; the `bus-soak` tag is excluded from the gate as always; `:testing:integration-tests:test` SKIPPED by its own gate (`enabled = hasProperty("piProfile")`, its `build.gradle.kts:22`).
- The cap: 3 KB + 11 rows × 1 KB = 14 KB — this file sits at the arithmetic.

**WUCP Phase 1:** [x] tests first, red for the right reason, then green; the gate as written, `-Werror` clean, freshness from executed-state lines and XML mtimes · [x] MODULE_CONTEXT (row 10; tokens documented) · [x] census exact, nothing committed or staged · [x] deviations by honest severity · [x] this return at the named path; coder-handoff is the hub's splice (§6), lessons ride §5; NEXT WU named.
