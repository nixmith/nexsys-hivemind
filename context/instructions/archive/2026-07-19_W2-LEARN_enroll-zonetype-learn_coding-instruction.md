<!--
file: context/instructions/2026-07-19_W2-LEARN_enroll-zonetype-learn_coding-instruction.md
purpose: Coding instruction for W2-LEARN — feed the ZoneEnrollRequest's zoneType payload into the existing F-7a learn (the D1 closer: the 04P adopts as contact once this lands + deploys), fold the S31-ROUTE verify-first CLOSURE, and add the route() non-HA DEBUG diagnostic. Micro-WU, full bar.
audience: Coder (host-side Claude Code lane, in homesynapse-core); PM hub (two-layer audit).
status: ISSUE-READY
baseline: core `9d40ce8` (re-verify at issue: `git log --oneline -1` must show 9d40ce8 and the worktree CLEAN; if HEAD moved, STOP and report).
pre-verification: nexsys-hivemind/context/pre-verifications/WU-W2-LEARN.md (READ FIRST — P1–P14, all same-day signatures; the silicon record P12 is why this WU exists).
scope: v34 orchestrator prompt charge 1 (the v33 beat-4 adjudication (1): W2-LEARN is the required micro-WU and the D1 closer; S31-ROUTE was demoted to verify-first INSIDE this WU — the hub ran the verify at desk 2026-07-19 and the closure is settled below as DP-WL-5).
-->

# Coding Task: W2-LEARN — ZoneEnrollRequest zoneType Learn (F-7a completion) + the S31-ROUTE Closure

**Subsystem:** Zigbee integration adapter (`integration/integration-zigbee`)
**Design Doc:** Doc 08 §3.12 (IAS tolerate-not-require), §3.10 (classification — consumes the learn via the M9.7-W2 seam); the M9.7-W2 record (MODULE_CONTEXT §M9.7-W2, esp. DP-6 and the Gotchas)
**Phase:** 3-Implementation (tests FIRST — red-first staged, the M9.6-RO idiom)

## What This Implements

The joins night proved the gap on silicon (P12): **three enrollments, zero `ias_zone_type_learned`** — no real device volunteers the IAS ZoneType ATTRIBUTE, so the M9.7-W2 learn machinery (which is live and correct) never receives wire truth. But every enrolling device DOES announce its zoneType — in the **ZoneEnrollRequest payload** (ZCL8 §8.2.2.3: zoneType uint16 LE + manufacturerCode uint16 LE), which today's enroll arm answers without reading (P2). The 04P sits joined/enrolled/proposed/HELD on the door waiting for exactly this learn.

Three parts, one compile-and-commit unit, all inside `ZclIngestionUnit` + tests + MODULE_CONTEXT:

- **§1 (REQUIRED — the D1 closer):** parse zoneType from the enroll-request payload and feed the EXISTING learn core. Learn semantics byte-preserved (P7); the attribute-report path unchanged.
- **§2 (the S31-ROUTE closure, DP-WL-5):** the MODULE_CONTEXT "S31 bench watch" resolves to a recorded CLOSURE — no routing change.
- **§3 (the observability rider):** the `route()` non-HA silent skip gains ONE DEBUG diagnostic (the never-theorize-twice-about-a-silence rule; it is the standing instrument if any device ever emits non-HA frames).

ZERO event mints (73/43/55 hold) · ZERO module-info/build/schema/config diffs · ZERO public surface (everything touched is package-private) · the `ias_zone_type_learned` INFO token format is FROZEN-SHAPE — untouched.

## Files to Read Before Starting

| File | Why |
|---|---|
| `nexsys-hivemind/context/pre-verifications/WU-W2-LEARN.md` | P1–P14 — the verified source-state basis |
| `integration/integration-zigbee/MODULE_CONTEXT.md` | §M9.7-W2 (the seam this feeds) + Gotchas (`learnedZoneType` ≠ `effectiveZoneType`; the choreography rationale) |
| `.../zigbee/ZclIngestionUnit.java` IN FULL | The only production file touched: `route()` :291–:313 · `handleZcl` :329–:413 · `respondZoneEnroll` :457–:480 · `learnZoneType` :483–:519 · accessor :539–:553 · `effectiveZoneType` :558–:564 |
| `.../zigbee/IasZoneHandler.java` (constants) + `.../zigbee/ZoneType.java` | P5/P6 — ids and zclIds |
| `.../zigbee/EzspCoordinatorProtocol.java` (profile-id constants) | P13 — verify HA/ZDO values before writing the §3 diagnostic |
| `test/.../ZclIngestionUnitTest.java` | The F-7a legs :312–:390 (the enroll fixture :315 is your red-first tooth) + the M9.7-W2 accessor legs :530+ |
| `test/.../ZigbeeWave2ContactAdoptionTest.java` | The end-to-end choreography + its `containsExactly` learn pin (:125) — your enroll-driven twin must not disturb it |

**Verbatim `module-info.java` (ZERO change this WU):**

```java
module com.homesynapse.integration.zigbee {
    requires transitive com.homesynapse.integration;
    requires com.fazecast.jSerialComm; // explicit JPMS module (ships module-info.class); interior-only per D-M92-1
    requires org.slf4j; // plain (implementation-only): Doc 08 §3.3 mandates structured log entries (LTD-15)
    requires com.fasterxml.jackson.databind; // plain (implementation-only): the M9.3 JSON profile loader + device cache; no Jackson type on any exported signature (the D-M92-1 pattern)

    exports com.homesynapse.integration.zigbee;
}
```

## Files to Create or Modify

| Action | File | Description |
|---|---|---|
| MODIFY | `main/.../zigbee/ZclIngestionUnit.java` | §1 enroll-arm parse + learn-core extraction · §3 the route() DEBUG line |
| MODIFY | `test/.../zigbee/ZclIngestionUnitTest.java` | The new legs (§Test Requirements) + P8/P9 drift adaptations |
| MODIFY | `test/.../zigbee/ZigbeeWave2ContactAdoptionTest.java` | The enroll-driven end-to-end twin (the silicon choreography pinned) |
| MODIFY | `integration/integration-zigbee/MODULE_CONTEXT.md` | W2-LEARN section + the S31-ROUTE watch → CLOSURE rewrite (DP-WL-5 text basis) |

The Files table governs; flag prose/table conflicts as `[INFO]`.

## STOP-on-Mismatch Gates

| Gate | Expected state at dispatch HEAD |
|---|---|
| G-WL-1 | `learnZoneType` has exactly ONE caller (:376); the enroll arm (:399–:405) calls `respondZoneEnroll(device, message)` and returns without reading payload bytes |
| G-WL-2 | `route()`'s non-HA arm (:299–:301) is a bare `return;` — no diagnostic |
| G-WL-3 | `learnedZoneType(IEEEAddress)` exists, learned-only (:551–:553) |
| G-WL-4 | `ZoneType.CONTACT.zclId() == 0x0015` · `COMMAND_ZONE_ENROLL_REQUEST == 0x01` · `ATTRIBUTE_ZONE_TYPE == 0x0001` |
| G-WL-5 | Module suite forced-fresh GREEN at the dispatch HEAD BEFORE any edit — re-derive the count (last recorded 518/0/0 AT `9d40ce8`; stated as at-commit per P14, never carried) |

Any mismatch ⇒ STOP and report.

## Settled Decisions (NOT open questions — implement as stated)

- **DP-WL-1 (parse shape):** inside the enroll arm — arm CONDITION unchanged — guard `zcl.length >= header.payloadOffset() + 2`; `zoneType` = LE uint16 at `payloadOffset` (the ZoneStatusChangeNotification arm's parse idiom, :392–:397); `manufacturerCode` ignored. Short/absent payload ⇒ learn NOTHING, still respond (§3.12 tolerate: a malformed request never blocks enrollment).
- **DP-WL-2 (learn core shared, semantics byte-preserved):** extract the zclId→store→invalidate core (e.g. a private `learnZoneType(IEEEAddress device, long zclId)`); the attribute path (:490) delegates to it after its existing `Long`-extraction. Unknown zclId ⇒ the existing `ias_zone_type_unknown` DEBUG ignore. Changed-vs-effective ⇒ F-8 `invalidateHandlers` + the existing `ias_zone_type_learned` INFO — **format untouched** (LTD-15: no new INFO/WARN tokens, no format change). Same-as-effective ⇒ silent store, no invalidate (P7 — pin it).
- **DP-WL-3 (learn BEFORE respond):** in the enroll arm the learn precedes `respondZoneEnroll` (the F-7a learn-before-dispatch principle at :374); the learn must not depend on the send outcome — pin with a test (learn recorded even when `frameSender.send` is rejected).
- **DP-WL-4 (the §3 diagnostic):** the non-HA arm gains ONE `log.debug` line, e.g. `zigbee.ingestion_profile_skipped: nwk=0x{} profile=0x{} cluster=0x{}; non-HA frame skipped` — DEBUG-level diagnostic (the M9.7-W2 R1 ratified precedent: DEBUG-level lines need no format-freeze). NEVER above DEBUG — Green-Power frames (0xA1E0) route here lawfully. Behavior (the drop) unchanged.
- **DP-WL-5 (S31-ROUTE CLOSED — record, don't code):** hub verify-first finding of record (2026-07-19, at source): `route()` gates on **the FRAME's APS `profileId()`** (:299), never the cached simple-descriptor; the night's silicon shows the S31's reports INGESTING (`on:true`, stateVersion 7) while its cached descriptor reads `0xC05E` (C-05 closed) ⇒ its frames carry 0x0104 (ZLL-descriptor devices emit HA-profile frames — the interop posture). **Routing widening DECLINED** — it would relax a correct gate for zero observed need; the §3 DEBUG line is the standing instrument if a non-HA emitter ever appears. Rewrite the MODULE_CONTEXT "S31 bench watch" bullet as this closure.
- **DP-WL-6 (no confirmation/posture code):** the S31's `confirmation_downgraded … best_effort` upgrade path is OPERATIONAL (the sanctioned `applyPostureRouting` re-emit on a future re-drive) — zero code here; carry the note in MODULE_CONTEXT.

## Error Handling

| Condition | Behavior |
|---|---|
| Enroll payload shorter than 2 bytes | Respond (unchanged), learn nothing |
| Unknown zoneType zclId in the payload | Respond; `ias_zone_type_unknown` DEBUG (existing); no store |
| Non-HA-profile frame at route() | Dropped exactly as today + the ONE DEBUG line |

## P2 Consumer/Pin (Fan-Out) Survey — sweep by MECHANISM at execution (the P9 lesson: never name-grep alone)

- Every test constructing a cmd-`0x01`/`COMMAND_ZONE_ENROLL_REQUEST` frame: **`zoneEnrollRequestAnswered` (:314) now LEARNS CONTACT as a side effect** (its fixture carries zoneType 0x0015 — P8). Verify its assertions still hold; if any sibling pins learn-absence or handler-table state post-enroll, adapt DELIBERATELY and record as `[INFO]`.
- Every caller of `learnedZoneType` / `invalidateHandlers` / `effectiveZoneType` (main + test).
- Every log-capture pin on `ias_zone_type_learned` / `ias_zone_enrolled` — esp. `ZigbeeWave2ContactAdoptionTest`'s `containsExactly` (:125): your new twin is a SEPARATE method; the existing pin stays green untouched.
- Every test asserting route() drops (non-HA frames) — the new DEBUG line must not break silent-drop assertions (log-level pins).
- Constructor arity: NONE widens this WU (the §4 seam already exists) — verify, don't assume.
- module-info: ZERO change (embedded above).

## Locked Decisions That Apply

- **Doc 08 §3.12 (tolerate-not-require):** enrollment is GRANTED unconditionally — the learn is a side observation, never a gate on the response.
- **LTD-15:** structured logging; the ONE new DEBUG diagnostic follows the R1 ratified DEBUG precedent; `ias_zone_type_learned` format untouched.
- **LTD-11:** ReentrantLock only if any locking is added — **add NONE**: `learnedZoneTypes` is cycle-thread confined (:141) and the enroll arm already runs on the same cycle thread as the attribute arm.
- **INV-SE-03:** nothing sensitive logs (zoneType/profileId are not sensitive).
- **REG-INV-1 / mint pins:** zero registry or event-model interaction; 73/43/55 hold untouched.

## Invariants That Must Hold

- **AMD-97-INV-01 / never-false-CONFIRMED:** untouched (no confirmation code).
- **DP-6 (M9.7-W2, of record):** classification stays learned-first CONTACT-else-motion; this WU changes the learn's SOURCE, never its consumers.
- **F-8:** a learn that changes the effective type still invalidates the handler table — through the shared core, proven by test.

## Test Requirements (write FIRST; red-first staged honest — state which reds are expected and why)

**`ZclIngestionUnitTest` new legs (§1/§3):**

| Test | Assertion | Red-first? |
|---|---|---|
| enrollRequestLearnsZoneType | The :315-shaped fixture (zoneType 0x0015 LE) ⇒ `learnedZoneType(device)` == CONTACT AND the response still sent | **RED at HEAD — this is the silicon gap made a regression tooth** |
| enrollLearnRebuildsHandlers | Enroll-driven CONTACT on a device whose effective type was MOTION ⇒ handler table invalidated (the :356 observation idiom) + the `ias_zone_type_learned … (was MOTION)` INFO | RED |
| enrollLearnPrecedesSendOutcome | `frameSender` rejects ⇒ the learn is STILL recorded (DP-WL-3 pinned) | RED |
| enrollUnknownZoneTypeIgnored | zclId `0x7777` ⇒ no store, `ias_zone_type_unknown` DEBUG, response still sent | RED (learn half) |
| enrollShortPayloadLearnsNothing | Payload < 2 bytes ⇒ no store, response still sent | may be GREEN at HEAD (nothing learns today) — state it; its false-verdict bound is the mutant below |
| enrollSameTypeTwiceInvalidatesOnce | Second enroll with the same type ⇒ no second invalidate, no second INFO (P7 same-as-effective semantics) | RED (first-learn half) |
| nonHaProfileFrameSkippedWithDiagnostic | A 0xC05E frame ⇒ no dispatch (unchanged) + the ONE DEBUG line; an HA frame produces no such line | RED (diagnostic half) |

**Fixture-paired false-verdict bounds (the standing rule):** each leg names the mutant that flips it — delete the payload parse ⇒ leg 1 fails; drop the length guard ⇒ leg 5's mutant fixture (a 1-byte payload) throws/fails; remove the shared core's invalidate ⇒ leg 2 fails; reorder respond-before-learn with a rejecting sender ⇒ leg 3 fails.

**`ZigbeeWave2ContactAdoptionTest` — the enroll-driven twin (new method):** the same scripted join walk but the CONTACT truth arrives ONLY via a ZoneEnrollRequest in the drain (NO ZoneType attribute report anywhere) ⇒ `ias_zone_type_learned … CONTACT` observed BEFORE the adopt step ⇒ the adopted entity carries `contact`. This pins the ACTUAL silicon choreography (long-press re-pair → enroll → learn → accept-list → adopt) that the joins night will re-run. The existing two methods stay byte-untouched.

**Suite:** full module forced-fresh GREEN; `./gradlew check` GREEN; count pins 73/43/55 undisturbed; state the realized row count as +N against the base you re-derived at G-WL-5.

## What to Watch Out For

- **Threading: add NO locking.** The learned map is cycle-thread confined; the enroll arm is already on that thread. If you believe otherwise, STOP and push back with evidence — do not add a lock speculatively.
- **`learnedZoneType` stays LEARNED-ONLY** (the M9.7-W2 gotcha) — do not fold in the resolver default anywhere.
- **Do not touch** `effectiveZoneType`, the adapter's `zoneTypeFor` MOTION stub, the classifier, the §4 seam, `ReportingConfigurator`, or the dedup scope (F-4 is report-channel-only; enroll frames are cluster-specific and never deduped — keep it that way).
- **The `ias_zone_type_learned` INFO format is pinned by the end-to-end test** — the shared-core extraction must reproduce it byte-for-byte including the `(was {})` clause fed by `effectiveZoneType`.
- **Tests must inject `Clock`.** Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` in this module's test code — `Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC)` injected per the module convention (the ArchUnit rule's test reach covers app only — self-enforced here).
- **Shift-left:** run `./gradlew :integration:integration-zigbee:compileJava` early (~20 s; `-Werror` surfaces the cheap classes).
- Record-component/static-factory STOP-check on anything new (no new records are expected).

## Coder Pushback Welcome

If the enroll arm's threading discipline, the shared-core shape, or any pin here contradicts what you read at source, raise it with evidence before writing — the M9.5-DUR arity pushback is the model. P13 (the profile-id constant values) is deliberately marked verify-at-read.

## Out of Scope (tempting; do NOT)

- Widening `route()` beyond the DEBUG line (DP-WL-5 declined it) · any classifier/capability change · fingerprints (the S31's stays withheld) · the S31 posture re-emit or any confirmation code (DP-WL-6) · accept-list/config edits (operator acts) · BTN-AMD anything · bench constants/scenarios (BENCH-CONST is hub-side, post-adoption) · `device_removed`/re-classification.

## Success Criterion — the milestone is DONE when

1. All Files-table rows realized; every DP implemented as stated.
2. All new/modified tests green; full module forced-fresh green; `./gradlew check` GREEN; 73/43/55 undisturbed.
3. Zero diffs: module-info, build files, config schema, event model, public surface (grep-verified in the completion report).
4. MODULE_CONTEXT updated: the W2-LEARN section (enroll-sourced learn; the DP-WL-3 ordering; the diagnostic) + the S31-ROUTE watch rewritten as the DP-WL-5 closure + the DP-WL-6 note.
5. WUCP Phase 1 checklist complete; completion report → the hub two-layer audit. **No commit until the hub's order.**
6. **UNIT-GREEN ≠ WU-DONE:** the silicon leg = deploy re-verified AT the Pi → ONE permit window + the 04P long-press re-pair → `zigbee.ias_zone_type_learned … zoneType=CONTACT` on the wire → accept-list → adopt as BINARY_SENSOR/contact → **D1 [M] 5/5**. The hub authors the operator mini-package at the deploy word; BENCH-CONST rides after adoption.

## Build Discipline

Host-side Claude Code lane: targeted `:integration:integration-zigbee:test` loop while iterating; full `./gradlew check` before handoff; CI on the pushed commit is the gate of record (push only on the hub's commit order, via Nick).
