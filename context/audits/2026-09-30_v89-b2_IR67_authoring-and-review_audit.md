<!--
file: context/audits/2026-09-30_v89-b2_IR67_authoring-and-review_audit.md
purpose: v89 beat 2 — IR-67's coding instruction authored on WU-IR67 and fourteen further premises grepped at `8deef4b` (the premise gate, law #32), the independent review (E1–E12) and the hub's second layer on it, the cloud first message, the acts handed.
audience: the v89 hub · the v90 boot (by §0) · the IR-67 intake (the counts of record)
state-type: audit (one beat)
status: FILED — Wed 2026-09-30 ~20:2x CT (instrument 2026-10-01T01:28:00Z)
-->

# v89 beat 2 — IR-67 AUTHORING and REVIEW audit

## §0 Verdict
**THE INSTRUCTION DISPATCH-READY; THE REVIEW FILED AND APPLIED; THE FIRST MESSAGE HANDED.** The authoring read core at `8deef4b` in the hub's container clone (`/home/claude/core`, the D-v88-6 route) — 14 premises beyond WU-IR67's 18, each with its instrument in §0b; the survey's twelve greps run (§6). The FRESH reviewer (an in-conversation agent; 87 tool calls; the clone untouched) returned RE-CUT with 12 findings; the hub re-verified seven at the instrument (§2) and applied all twelve. Five modules touched (device-model the fifth — the projection's home); no module-info, no build file. ONE act handed: the b2 card; then the first message.

## §1 The authoring's premise greps (the fourteen beyond WU-IR67 §1; each in the instruction's §0b with its command and its found line)
Row 19 the holder's descriptor (:1171) and `buildContext` (:1088) · 20 the publisher :119, the clock :123, the registry :1093 · 21 the zigbee descriptor `Set.of()` :137 and its comment; `ZigbeeAdapterFactory` an interface (:41) with stale Javadoc · 22 `CapabilityAdded`'s `DeviceId` (:42–:47) vs `findEntity` :49 and `Entity.deviceId()` :62 · 23 `StandardCapabilities.all()` :68 and the classifier's private instance form · 24 `RegistryProjection` :57 and REG-INV-1 :410 · 25 the apply census :45–:46 / :49–:52 · 26 the slice's write-ahead form :414/:424, the maps :124–:130, `installOverrides` :587 · 27 `initialize()`'s order :342 · :372 · :420 (:441) · :476 · :498 · 28 the configurator's `inputClusters()` loop :235, `onRejoin` :412, the 0x0400/0x0402 rows :86/:84 · 29 thirteen five-null contexts in twelve zigbee tests · 30 `SequenceConflictException` in event-model; the catch :1058–:1063 · 31 the subscriber's filter and switch; the checkpoint reset :622–:628 · 32 the two test fixtures. Each was read with `sed -n`/`grep -n` in the clone; the instruction carries the command.

## §2 The review (RE-CUT; `context/audits/2026-09-30_IR67_independent-review.md`) and the hub's second layer
- E1 [BLOCKING] no logback on runtime's test classpath — RE-VERIFIED (`integration/integration-runtime/build.gradle.kts` :6–:8: test-support, two testFixtures, nothing else) → T1's WARN leg dropped (no throw asserted instead); no build edit; the token the hub's grep at intake.
- E2 T8's capture level — applied (INFO; attached after the first boot).
- E3 T9's zone-type seam — applied (the cache file seeded: `recordInterview` :150, `recordLearnedZoneType` :300, `flush()` :470; the registries seeded for the relink join :545–:556).
- E4 the unbound arm unreachable as written — RE-VERIFIED (`relink` :545–:556 builds `entitiesByIeee` FROM the registry) → the three arms re-pinned; `unbound` a counter, DEBUG once per device.
- E5 the IAS fallback-then-learned case — applied as THE IAS-SWAP ARM (`relearned`; one WARN per launch; nothing published).
- E6 the per-pass INFO/WARN repeats and the restart path — RE-VERIFIED (`logClassified` :155/:168; `profile_unresolved` :596; `initialize()` on the restart path :743–:744) → `classifySilently` (row 5b); `profile_unresolved` disclosed; "per launch".
- E7 the read API renders no capabilities — RE-VERIFIED (two `capabilities()` hits: `GetCommandStatusEndpoint` :230, `IssueCommandEndpoint` :315) → the observable re-cut; IR-108.
- E8 the null `deviceId` NPE — RE-VERIFIED (`CapabilityAdded.java` :51 `requireNonNull(deviceId)`; `Entity.java` :41/:100 "null for helper entities") → the guard + T1's leg.
- E9 three counts and WU row 6 — RE-VERIFIED (`ZigbeeAdapterFactory.java` :41 `public interface … extends IntegrationFactory`; `subscriptionFilter()` 7 in lifecycle tests) → corrected; row 21 carries the instrument of record; IR-109 (a).
- E10 eight line misses — RE-VERIFIED (the census :45–:46/:49–:52; `context(...)` :1226; `adapterMessages` :1137; M-1 :252–:277) → corrected.
- E11 [INFO] the design holds (the boot gate `awaitRegistryProjectionLive()` :669 precedes Phase 6; `publishRoot` takes no cause and declares the checked exception :127; the entity subject matches `entity_registered` :421) — noted in §9.8.
- E12 [INFO] the ownership check unenforced — IR-109 (b); named in §10 pushback.
Not re-executed by the hub: the reviewer's reads of `BootOrderingGateIT`, `ZclIngestionUnit.java` :920, `ZigbeeDeviceCache` :26/:150/:300/:470 (cited as the reviewer found them; the lane re-runs each — §2 of the instruction names the files).

## §3 The first message
`context/instructions/2026-09-30_coder-lane_IR67_CLOUD-DISPATCH_first-message.md` — BH-3's as the FORM; the exit clauses 1–5; THE GRANT FIRST; the settings words re-cut (the effort "the highest the build offers"; `ultracode` named, unobservable); the hivemind cloned beside for the instruction, the pre-verification and the review; the toolchain check (`java -version` 21; the wrapper) before the work.

## §4 Layer 2
Re-executed: the clone's HEAD `8deef4b`; the fourteen premise greps; the twelve survey greps; the seven review findings named above; the instruction's own asserts (one row 5b, T7b present, the review named in the masthead, no trailer strings); the three files' bytes on the device = the container's. Not re-executed: the reviewer's remaining reads (named above); any build (none possible here; the lane's `./gradlew check` is the gate).

## §5 The acts handed
1. The b2 card (`_scratch/v89/card_b2.txt`; 11 paths; gated) → `HIVE: LANDED <sha>`.
2. IR-67's launch: the first message pasted WHOLE into a FRESH cloud session on `nexsys-io/homesynapse-core` (the grant PUSH, the settings) → `IR67: LAUNCHED <HH:MM CT> · CREDITS: $<n>`.
3. The lines still owed, one each: `TIME:` · `HOURS:` · `PR1: closed` · `BENCH-PULL-5:` · `BASELINE:` · `NIGHTLY:`.
