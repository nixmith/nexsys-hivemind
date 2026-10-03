<!--
file: context/instructions/2026-10-03_coder-lane_J1_LINK-READ-2_IR-121_dark-device-named_LOCAL_desk-coding-instruction.md
purpose: THE CODING INSTRUCTION for J1 = LINK-READ-2 (IR-45) + IR-121 — "a dark device is NAMED at the read surface, with its reason, its last-seen instant and its last link reading; a mains device inside 90 s; a reporting class inside twice its own contract" — in the LOCAL form on Nick's desk (D-v92-28 e; THE HORIZON §2 J1; `DESK: j1-first`). THE PLAN-RETURN FORM (W9): the lane reads, re-runs the premises, writes a PLAN and WAITS for `GO` before its first write. A ONE-WAY DOOR (the event schema 1 → 2; the checkpoint's record): the independent review is filed beside this file and its edits are applied here before the dispatch line was handed.
audience: the J1 Coder lane (Claude Code on Nick's desk) · the hub (the intake) · the reviewer
state-type: coding instruction (LOCAL form; plan-first)
status: DISPATCH-READY — cut v95 beat 2 (Sat 2026-10-03 ~12:4x CT; instrument 2026-10-03T17:41:46Z); baseline `5b0e20c` (re-verified at the paste); the pre-verification `context/pre-verifications/WU-J1_LINK-READ-2_IR-121.md` (twelve rows); the review `context/audits/2026-10-03_J1_independent-review.md`. Flips to EXECUTING at the paste, EXECUTED at the intake.
baseline: homesynapse-core `5b0e20c` (`main`; porcelain 0)
-->

# J1 — LINK-READ-2 + IR-121: a dark device named at the read surface (LOCAL desk form; plan first)

## §0 The coder-session prompt (read this whole section before any command; every line binds)
- You are in `~/Desktop/Code/ClaudeFolder/homesynapse-core` on `main` at `5b0e20c`. Run `date -u` FIRST; every stamp you write derives from it (CT = UTC − 5; a Pi log line is EDT = UTC − 4 — name the clock beside every time you quote). `git --no-optional-locks status --porcelain` must be EMPTY before your first act and your first act is `git switch -c j1/link-read-2-ir-121` — every write of this lane lives on that branch; you never touch `main`, never `git push`, never merge; `git add`/`git commit` on the branch only, with NO attribution trailer of any kind (grep your message for `Co-Authored\|Claude-Session` before each commit; a hit is a defect). No token, no secret, nothing from the Pi: you do not ssh anywhere.
- **PLAN FIRST (W9).** Before any write to a source file: read §2's set by the ranges given; re-run EVERY row of `../nexsys-hivemind/context/pre-verifications/WU-J1_LINK-READ-2_IR-121.md` §1 (twelve instruments) and §0b below, paste each count or line into your plan; settle the three forks (§4) from the BYTES the plan cites; then write `../nexsys-hivemind/context/audits/<CT-date>_J1_plan.md` (≤ 8,192 B) in the shape of §12 and STOP, printing its last line `PLAN-RETURNED <path> <bytes>`. You write code only after the word `GO` (or `GO with: …`, whose edits you apply first). A premise row that no longer holds at `5b0e20c` STOPS the plan at that row and says which.
- Tests first (§7): the red is OBSERVED — a compile failure on a type, field or method that does not yet exist IS the red; say so in the return — then green. Write ONLY §3's rows (the Files table governs where prose and table differ).
- `./gradlew check` green at the end (`-Xlint:all -Werror` is on). The gate lines are the verbatim task paths of `settings.gradle.kts`: `:integration:integration-zigbee:test` · `:core:event-model:test` · `:core:state-store:test` · `:core:persistence:test` · `:core:device-model:test` · `:api:rest-api:test` · `:lifecycle:lifecycle:test` · `:app:homesynapse-app:test` (the ArchUnit rules live there). A re-run of an up-to-date test task carries `--rerun`. Scripts over ~15 lines are written with the Write tool and run by path — no long heredocs.
- Read `MODULE_CONTEXT.md` by `grep -n` only, never whole (integration-zigbee's is 241 KB, persistence's 198 KB, rest-api's 123 KB, state-store's 100 KB).
- THE RETURN: `../nexsys-hivemind/context/audits/<CT-date>_J1_return.md` — §0 the card (DELIVERED/BLOCKED; `check`'s closing lines; the XML counts per module; `git --no-optional-locks diff --stat 5b0e20c..HEAD`; the red texts; the twelve pre-verification rows re-run with their counts) · §1 what changed (per file, line spans) · §2 the tests (names; the observed red; green) · §3 deviations at honest severity ([INFO]/[REVIEW]/[BLOCKING]) · §4 the survey as re-run (§6) · §5 findings for the register · §6 the coder-handoff entry text · §7 instrument limits. **≤ 26,624 B is a CEILING, not a target** (3 KB + 1 KB per Files-table row, 23 rows, rounded up to the KiB); the §0 card is what the hub reads first; a shorter return with the same receipts is a better return. The last line of the FILE: `RETURNED <path> <bytes> <the branch head sha>`.
- The hub stages nothing of yours; the landing is Nick's card after the intake (a squash onto `main` under the gated form, IR-101; CI on his push is the gate of record).

### §0b The premise table (the rows beyond the pre-verification's twelve; grepped at `5b0e20c`; re-run each)
| # | The claim | The instrument | Found |
|---|---|---|---|
| 13 | The projection constructs `EntityState` at more than one site — every site must carry the three new fields through | `grep -n 'new EntityState(' core/state-store/src/main/java/com/homesynapse/state/*.java \| wc -l; grep -rn 'new EntityState(' --include=*.java core api lifecycle app \| grep -v '/test/' \| wc -l` | the hub read SEVEN in the projection (:896, :920, :933, :945, :956, :1055, :1090 — :945 sets from the event; :1090 nulls = the [INFO] case; the others carry the prior's three) + `CheckpointSerializer.java:255` + `MaterializedStateQueryService` (not read by the hub — row 23); the lane pastes both counts; every production site is a Files-table row or a named [INFO] deviation |
| 14 | `StandardTriggerEvaluator` reads the event's status strings only | `sed -n '555,575p' core/automation/src/main/java/com/homesynapse/automation/StandardTriggerEvaluator.java` | `instanceof AvailabilityChangedEvent ace` :559/:568, reading `newStatus()` only (:563, :572); the type-check at :581–:582; a v2 field read there is OUT of J1 |
| 15 | The event-model shape test pins the record's component count | `grep -n 'getDeclaredMethods\|RecordComponents\|components' core/event-model/src/test/java/com/homesynapse/event/AvailabilityChangedEventTest.java` | the lane pastes the hits; a pinned count is a §3 row (the test moves with the record) |
| 16 | The endpoint tests pin the row's KEY SET (`containsExactly` / `containsOnlyKeys`) | `grep -n 'containsExactly\|containsOnlyKeys\|hasSize' api/rest-api/src/test/java/com/homesynapse/api/rest/ListEntitiesEndpointTest.java api/rest-api/src/test/java/com/homesynapse/api/rest/GetEntityEndpointTest.java api/rest-api/src/test/java/com/homesynapse/api/rest/GetEntityStateEndpointTest.java 2>/dev/null` | every hit on a key set is a §3 test row (#31: a frozen token is a pin) |
| 17 | The checkpoint serializer's test round-trips a null `staleAfter` (the additive precedent the three new fields follow) | `grep -n 'staleAfter' core/persistence/src/test/java/com/homesynapse/persistence/CheckpointSerializerTest.java \| head -5` | the lane pastes the hits and adds the three-field case beside them |
| 18 | The adoption maps give the tracker a device → entities → capabilities path (for the per-device expected interval) | `grep -n 'entitiesFor(' integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/ZigbeeAdoptionSlice.java integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/ZigbeeIntegrationAdapter.java \| head -6; grep -n 'capabilities()' core/device-model/src/main/java/com/homesynapse/device/Entity.java` | `adoption.entitiesFor(device)` (the publish site uses it, A:1708); the lane names the registry call that yields each entity's `CapabilityInstance`s and the type that exposes `expectedReportInterval()` (the instance → `Capability` mapping, or `RegistryStalenessResolver`'s own lookup reused) |
| 19 | The 070945 adoption log's per-cluster lines after `reporting_configured` for `0xA4C13814CE41FFFF` (fork 2) | `grep -rn 'A4C13814CE41FFFF' ../_scratch/v92 ../_scratch/v90 --include=*.log \| grep -i 'reporting' \| head -8` (if no log is under `_scratch/`, say "not reachable from the desk" and take fork 2's NOTHING arm) | the lane pastes the lines; the plan's fork-2 choice cites them |

## §1 What this implements
Two gaps in one unit, both on the read surface a household and the bench read (`/api/v1/entities`, `bench.sh entities`/`state`, IR-118's `avail:` line):
1. **IR-121 — the aging.** Today a mains device is probed after **10 min** of silence (`T:53`) and every non-mains device waits **25 h** (`T:55`) whatever its own reporting contract says. After J1: a mains device is probed after `MAINS_PING_SILENCE` = **60 s** (derivation §4.1) — named dark in ≤ 60 + 5 + 0.05 s ≤ **90 s** (D-v94-25's acceptance); a non-mains device whose entities declare an expected report interval (IR-61's chain, row 10) is named dark at the **smallest declared interval** (already 2 × the contract's max by PowerMeter's derivation), else at 25 h as today. The sensor class's declaration is fork 2 (§4.2).
2. **LINK-READ-2 — the reason and the reading on the surface.** `availability_changed` goes to schema version **2**: `(previousStatus, newStatus, reason, lastSeenAt, lqi, rssiDbm, linkAt)` — the last three nullable, `reason`/`lastSeenAt` nullable for v1 rows. The projection carries them onto `EntityState` (three nullable fields); the three read endpoints render `availabilityReason`, `lastSeenAt` and `link` (`{"lqi": n, "rssiDbm": n, "at": "…Z"}` or `null`) — camelCase like every key of the v1.1 surface. A dark device's row then says WHEN it was last heard and HOW its link read at that frame — the dark-device line THE HORIZON §0 asks for. The 10-min `link_summary` stays a log line (no new event type; J1b in §11).

## §2 Files to read before starting (the minimum read set; by range)
- `../nexsys-hivemind/context/pre-verifications/WU-J1_LINK-READ-2_IR-121.md` whole (12,391 B) — the twelve rows ARE your map.
- `T` (`StandardAvailabilityTracker.java`): :26–:50 (the javadoc's laws) · :52–:80 (the constants) · :98–:135 (Seed, State, DeviceState) · :137–:180 (the constructor and the seed) · :184–:215 (`recordFrame`, `lastLink`, `lastLinkAt`) · :219–:250 (`recordCommandResult`, `isAvailable`, `lastReason`) · :294–:345 (`evaluateTimeouts`, `isMainsPowered`) · :350–:380 (`transition`). `AvailabilityTracker.java` whole (the interface). `AvailabilityReason.java` whole.
- `A` (`ZigbeeIntegrationAdapter.java`): :160–:185 (the constants) · :395–:415 (the tracker's construction and the seed) · :598–:618 (`runCycleOnce`) · :676–:710 (`evaluateAvailabilityTimeouts`) · :723–:760 (`pingBasic`) · :1690–:1730 (the transition listener → the publish site).
- `E/AvailabilityChangedEvent.java` whole (≈ 40 lines) · `E/EventTypes.java` :110–:120 · `E/EventEnvelope.java` :36–:42, :100–:150 (schemaVersion) · `E/DomainEvent.java` :25–:35.
- `P/EventPayloadCodec.java` :55–:65, :130–:200 · `P/PersistenceObjectMapper.java` :40–:50, :100–:112 · `P/CheckpointSerializer.java` :40–:80, :230–:300.
- `S/EntityState.java` whole · `S/StateProjection.java` :930–:960, :1100–:1115, and every `new EntityState(` site (row 13) · `S/RegistryStalenessResolver.java` :20–:110 · `S/Availability.java` whole.
- `M/Capability.java` :90–:105 · `M/PowerMeter.java` :40–:66 (THE DERIVATION's wording) · `M/Occupancy.java`, `M/IlluminanceMeasurement.java` whole.
- `R/ListEntitiesEndpoint.java` :30–:60, :180–:205 · `R/GetEntityEndpoint.java` :25–:60 · `R/GetEntityStateEndpoint.java` :25–:60 and their tests (row 16).
- `Z/ReportingConfigurator.java` :40–:90 (the §3.7 default table).
- MODULE_CONTEXT.md by grep: `grep -n -i 'availability\|FROZEN' integration/integration-zigbee/MODULE_CONTEXT.md core/state-store/MODULE_CONTEXT.md api/rest-api/MODULE_CONTEXT.md | head -60`; `grep -n -i 'upcast\|schema_version\|FROZEN' core/event-model/MODULE_CONTEXT.md core/persistence/MODULE_CONTEXT.md | head -40`. Every `FROZEN` hit on a token you touch is a fork for the plan, never your choice (#31).
- `../nexsys-hivemind/context/planning/improvement-register.md` by grep: `grep -n '^| IR-45 \|^| IR-61 \|^| IR-118 \|^| IR-121 ' …` — the four rows.

## §3 Files to create or modify (the Files table governs; A = added, M = modified)
| # | Path | A/M | What |
|---|---|---|---|
| 1 | `Z/StandardAvailabilityTracker.java` | M | `MAINS_PING_SILENCE` → 60 s with its derivation comment (§4.1); a constructor parameter `expectedSilenceLookup: Function<IEEEAddress, Optional<Duration>>` (the per-device declared interval; empty → 25 h); `evaluateTimeouts()`'s non-mains arm uses it; the transition listener's call carries `(device, instant, available, reason, lastSeen, lastLink, lastLinkAt)` — `LinkReading` is two ints and its instant is kept apart (T:133–:134); all four snapshotted into locals INSIDE the lock before :390 and passed at :395, never re-read through `lastLink()`/`lastLinkAt()` after the unlock; the LAST reading and last-seen instant at the moment of the transition, never the transition's own evidence reading (null on a timeout); a package-private `Optional<Instant> lastSeen(IEEEAddress)` on T, shaped as :206, under the lock |
| 2 | `Z/AvailabilityTracker.java` | M | the listener's signature if it lives here (the lane names where `TransitionListener` is declared — T:86 or the interface) |
| 3 | `Z/ZigbeeIntegrationAdapter.java` | M | the tracker's construction passes the lookup (row 18's path: device → entities → capabilities → the smallest `expectedReportInterval()`); the publish site (A:1710) emits schema version **2** with `reason` = `AvailabilityReason.name().toLowerCase()`, `lastSeenAt`, `lqi`, `rssiDbm`, `linkAt` from the listener's arguments (`onTransition` :1650 — `lastReason` :1661 and `linkFields` :1660 exist; `lastSeen` is the new accessor of row 1). `publishForEntities` (A:1704) has a SECOND caller, `seedFreshAdoption` (:1696–:1702), with no listener arguments: it passes `reason = lastReason(device)`, the reading = `lastLink`/`lastLinkAt(device)`, `lastSeenAt = lastSeen(device)`. T:393's log line is byte-frozen (A:1652–:1653) — untouched |
| 4 | `Z/StandardAvailabilityTrackerTest.java` | M | T1–T3 (§7) |
| 5 | `Z/ZigbeeIntegrationAdapterTest.java` (or the test that covers the publish site — the lane names it) | M | T4 |
| 6 | `E/AvailabilityChangedEvent.java` | M | the v2 record: `String previousStatus, String newStatus, String reason, Instant lastSeenAt, Integer lqi, Integer rssiDbm, Instant linkAt`; the compact constructor validates the first two as today and ACCEPTS null for the five additions (a v1 row decodes to this shape); Javadoc: the version history (1: two statuses; 2: + the five, 2026-10-xx J1) and the invariant "lqi/rssiDbm/linkAt are all null or all set"; NO secondary constructor (`PersistenceObjectMapper.java:61–:63` — conflicting creators); the canonical 7-arg constructor is the only creator; the five additions boxed/reference-typed (`Integer`, `Instant`, `String`), never primitives |
| 7 | `E/AvailabilityChangedEventTest.java` | M | T5 (and row 15's pin moved with the record) |
| 8 | `P/EventPayloadCodecTest.java` (the existing codec test — the lane names it) | M | T6: the two-direction decode (a v1 JSON → the record with nulls; a v2 JSON → whole; `schemaVersion` 2 on the envelope is NOT a decode gate) |
| 9 | `S/EntityLink.java` | A | `record EntityLink(int lqi, int rssiDbm, Instant at)` — the read model's link value (state-store owns the read model; the zigbee `LinkReading` type does not cross the module boundary) |
| 10 | `S/EntityState.java` | M | three nullable fields after `stale`: `String availabilityReason, Instant lastSeenAt, EntityLink link`; Javadoc as `staleAfter`'s |
| 11 | `S/StateProjection.java` | M | the `AvailabilityChangedEvent` arm maps reason/lastSeenAt/link (null-safe: a v1 event leaves them null; the prior's values are NOT carried when the event carries nulls — the event is the truth at its instant); every other `new EntityState(` site carries the prior's three values through |
| 12 | `S/InMemoryStateProjectionTest.java` (the projection test at `core/state-store/src/test/…`; the lane confirms it covers the availability arm, else names the one that does) | M | T7 |
| 13 | `P/CheckpointSerializer.java` | M | the three fields on `SerializableEntityState` (:277–:287, camelCase, by `staleAfter`'s path :285 ← :242 / → :263; read by name through the `TypeReference` :200 — no key count, no order, no per-entity version), with an internal `SerializableEntityLink(int lqi, int rssiDbm, Instant at)` beside :277, written `null` under `Include.ALWAYS`; `projectionVersion` (:295) is the CODE's version (:137) — NOT bumped (a replay from zero yields the same nulls); a checkpoint WITHOUT the keys (pre-J1) loads with nulls — pinned (T8) |
| 14 | `P/CheckpointSerializerTest.java` | M | T8 |
| 15 | `R/ListEntitiesEndpoint.java` · `R/GetEntityEndpoint.java` · `R/GetEntityStateEndpoint.java` | M | `availabilityReason` (string or null) · `lastSeenAt` (ISO-8601 Z or null) · `link` (`{"lqi": n, "rssiDbm": n, "at": "…Z"}` or null) AFTER the existing keys (the additive path; the frozen keys' order unchanged). `ListEntitiesEndpoint.summarise` (:189) appends the three EXPLICITLY, the instants via `toString()` as `lastReported` is (:201–:203); `GetEntityEndpoint` (:125) and `GetEntityStateEndpoint` (:114) put the `EntityState` RECORD itself in `data` through Javalin's Jackson — the new components render by their component names with NO handler code (state-store has no Jackson, module-info :140–:150, so no `@JsonProperty`; snake_case keys are unachievable there — hence camelCase everywhere); their only edit is the Javadoc shape (:37; :44–:46) |
| 16 | the three endpoint tests (row 16) | M | T9 |
| 17 | `M/Occupancy.java` · `M/IlluminanceMeasurement.java` | M | ⛔ FORK 2 (§4.2): `expectedReportInterval()` = 7200 s with THE DERIVATION comment in PowerMeter's words (2 × the §3.7 max 3600 s, `ReportingConfigurator.java:81/:86`), for the class(es) the plan's log read supports; a class the read does not support is NOT touched; if `Occupancy` declares, the sentence at `Capability.java:89–:91` ("binary sensors … declare nothing") is revised in the same commit |
| 18 | `M/…Test.java` for row 17 | M | T10 |
| 19 | `MODULE_CONTEXT.md` ×5 (integration-zigbee · event-model · state-store · persistence · rest-api) | M | rows only (§8) |
| 20 | `../nexsys-hivemind/context/audits/<CT-date>_J1_plan.md` | A | the plan (§12) — written FIRST |
| 21 | `../nexsys-hivemind/context/audits/<CT-date>_J1_return.md` | A | the return (§0) |
| 22 | `P/TestEventSamples.java` (the codec test's samples; `availabilityChanged()` at codec test :141) | M | the sample built with the 7-component record |
| 23 | `MaterializedStateQueryService.java` (the state query the Get endpoints read through, `GetEntityStateEndpoint.java:44–:46`; the lane names its module) | M | its `new EntityState(` site(s) carry the three fields through (row 13) — or a named [INFO] if it constructs none |

No `module-info.java` changes are expected (no new package, no new `requires`; `EntityLink` lives in the already-exported `com.homesynapse.state`). The lane confirms by the surface-export check (#14): every public type in an exported package whose API names another module's type is covered by an existing `requires transitive`. The embeds (§5) are the pin.

## §4 Technical specification
### §4.1 The mains probe interval (fork 1 — rec (a))
`static final Duration MAINS_PING_SILENCE = Duration.ofSeconds(60);` beside `LINK_SUMMARY_PERIOD` with the derivation written: D-v94-25's acceptance (a mains device named dark in ≤ 90 s); the probe is ONE ZCL Basic read per silent mains device per interval — on the ten-device run fleet ≤ 10 reads/min, each ≤ `AVAILABILITY_PING_TIMEOUT_MILLIS` = 5 s; the worst-case naming time for ONE device = 60 s silence + 5 s deadline + one 50-ms cycle = 65.05 s (< 90 s); fleet-wide the pings are SEQUENTIAL on the run thread (A:693–:708), so N simultaneously silent mains devices name the last one at 60 + 5·N + 0.05 s — 85.05 s at the run fleet's five (the two G4s, the S31, the Hue, the TR3); the acceptance holds for N ≤ 5 and the plan says so; the radio cost is measured at R6 and this constant moves only on that measurement. (Z2M probes at 10 min; ours is a product number, D-v94-25.) A yaml key is fork 1 (b) — write it in the plan if you want it; the hub's rec is (a).
### §4.2 The per-device silence limit (the non-mains arm)
`expectedSilenceLookup.apply(device)` → the SMALLEST `Capability.expectedReportInterval()` declared across the device's entities' capabilities — SOURCE 2 of `RegistryStalenessResolver`'s chain ONLY (:133–:143: the smallest declared interval over the entity's `CapabilityInstance` ids against the `StandardCapabilities` catalog), taken as the minimum across `adoption.entitiesFor(device)`; NEVER the per-entity override (:127) nor the global default (:146) — `staleness_overrides` and `default_staleness_threshold` do not bear on availability. Reuse by constructing a resolver with `Map.of()` and `Optional.empty()`, or mirror :133–:143 in the adapter — the plan says which. Empty → `BATTERY_OFFLINE_SILENCE` (25 h, unchanged). The mains arm is unchanged in shape (ping candidates). A device's limit is read at each evaluation (a capability declared later takes effect without a restart). **Fork 2 — the sensor class (⛔ row 17):** read row 19's lines. If the device accepted the 3600-s max on 0x0400 (Illuminance VERIFIED) → declare `IlluminanceMeasurement` 7200 s and `Occupancy` 7200 s; if Illuminance DEGRADED and Occupancy VERIFIED with its 3600-s max accepted → `Occupancy` 7200 s only; if neither line can be read from the desk → declare NOTHING (the 25-h window stands for the class) and write the finding for R6 in §5 of the return. The derivation comment names the log line it rests on.
### §4.3 The event v2
`EventDraft(EventTypes.AVAILABILITY_CHANGED, 2, …, new AvailabilityChangedEvent(previous, next, reason, lastSeenAt, lqi, rssiDbm, linkAt), null, null)` at A:1710 — `reason` the tracker's `AvailabilityReason` token lower-cased (`silence_timeout`, `ping_timeout`, `frame_received`, `ping_success`, `first_contact`, …); `lastSeenAt` the tracker's `lastSeen` for the device at the transition (null when unknown); the reading = the listener's `lastLink` + `lastLinkAt` (null when none). On the wire (the persistence mapper, SNAKE_CASE :106): `previous_status`, `new_status`, `reason`, `last_seen_at`, `lqi`, `rssi_dbm`, `link_at`; `NON_NULL` on write (:107) means a v2 event with five nulls writes the v1 byte-shape. The upcast IS the tolerant decode (row 7): no transformer; a v1 row reads as the v2 record with nulls; a v2 row read by a pre-J1 core ignores the extras (`FAIL_ON_UNKNOWN_PROPERTIES` disabled). Both directions are pinned by T6. The `schemaVersion` on the envelope is informational for this type (the codec gates only `state_changed` v1) — say so in the MODULE_CONTEXT row.
### §4.4 The read model and the surface
`EntityState` + `availabilityReason` (String, nullable) · `lastSeenAt` (Instant, nullable) · `link` (`EntityLink`, nullable). The projection's availability arm sets all three from the event (nulls stay nulls). The checkpoint JSON gains `"availabilityReason": "…" | null`, `"lastSeenAt": "…Z" | null`, `"link": {"lqi": n, "rssiDbm": n, "at": "…Z"} | null`. The three endpoints carry `availabilityReason`, `lastSeenAt`, `link` after the existing keys (the list endpoint by explicit puts; the two Get endpoints by the record's own serialization — row 15); `meta` untouched; the `X-View-Position` header untouched; the FROZEN v1.1 keys keep their names, order and types.
### §4.5 Error handling
No new exception. A null in any of the five v2 fields is a VALUE, never an error. A `SequenceConflictException` at the publish site keeps the relink-precedent idiom (A:1719–:1724). The lookup's registry exception at evaluation time is caught and logged once per device per cycle at WARN (`zigbee.availability_limit_lookup_failed`) and the device takes the 25-h arm for that cycle — never a stuck cycle.

## §5 Locked decisions, invariants, the module boundaries (verbatim embeds at `5b0e20c`)
- Doc 08 §9 (the availability regime: never-false-ALIVE; mains probed, non-mains passive) — J1 changes the NUMBERS and the per-class source of the non-mains limit, never the direction of failure (a false-UNAVAILABLE that self-heals on the next report remains the lawful failure direction; a false-AVAILABLE never is).
- Doc 01 §3.10 (schema versioning; upcasting at read) — J1's v2 is additive-nullable; the codec's posture (row 7) is the upcast.
- Doc 03 §3.8 / AMD-11 (`staleAfter` derived at read; THE DERIVATION RULE, D-v82-25) — every number in this file is derived beside its use (§4.1, §4.2).
- The FROZEN v1.1 read-API (the frontend consumes it): additive keys only; no key renamed, retyped or reordered (the v1.1.3 `deviceId` precedent, row 9).
- LTD-11 (locks: `ReentrantLock` only) · LTD-04 (ULIDs on the wire) · NO_DIRECT_TIME_ACCESS (the injected `Clock`; §9's block).
- REG-INV-1: the registry is read, never mutated, by the lookup.
- The module-info embeds (verbatim; NO proposed diff — zero-change pinned, #14 checked by the lane):

`integration/integration-zigbee/src/main/java/module-info.java`
```java
/**
 * Zigbee integration adapter module for HomeSynapse Core.
 *
 * <p>Provides the ZCL data model, coordinator abstraction, device profile system,
 * and adapter interfaces for the Zigbee protocol integration. Depends exclusively
 * on integration-api per LTD-17; all upstream core types (event-model, device-model,
 * state-store, persistence, configuration, platform-api) are available transitively
 * through integration-api's own transitive chain.
 */
module com.homesynapse.integration.zigbee {
    requires transitive com.homesynapse.integration;
    requires com.fazecast.jSerialComm; // explicit JPMS module (ships module-info.class); interior-only per D-M92-1
    requires org.slf4j; // plain (implementation-only): Doc 08 §3.3 mandates structured log entries (LTD-15)
    requires com.fasterxml.jackson.databind; // plain (implementation-only): the M9.3 JSON profile loader + device cache; no Jackson type on any exported signature (the D-M92-1 pattern)

    exports com.homesynapse.integration.zigbee;
}
```
`core/event-model/src/main/java/module-info.java`
```java
/**
 * Event model — types, envelope, publisher, store, and bus interfaces.
 */
module com.homesynapse.event {
    requires transitive com.homesynapse.value;
    requires transitive com.homesynapse.platform;

    exports com.homesynapse.event;
}
```
`core/state-store/src/main/java/module-info.java`
```java
/*
 * HomeSynapse Core
 * Copyright (c) 2026 NexSys. All rights reserved.
 */

/**
 * State Store — materialized entity state view, query service, and checkpoint contracts.
 */
module com.homesynapse.state {
    requires transitive com.homesynapse.platform;
    requires transitive com.homesynapse.value;
    requires transitive com.homesynapse.device;
    requires transitive com.homesynapse.event;
    requires transitive com.homesynapse.event.bus;

    requires org.slf4j;

    exports com.homesynapse.state;
}
```
`core/persistence/src/main/java/module-info.java`
```java
/*
 * HomeSynapse Core
 * Copyright (c) 2026 NexSys. All rights reserved.
 */

/**
 * Persistence Layer — telemetry ring store, backup/restore, retention,
 * and storage maintenance contracts (Doc 04).
 *
 * <p>This module defines the public API interfaces consumed by other
 * HomeSynapse subsystems. The implementation (SQLite JDBC operations,
 * WAL management, retention scheduler) lives in this module's Phase 3
 * implementation classes.</p>
 *
 * <p>The Persistence Layer implements two checkpoint contracts from two
 * different subsystems:</p>
 * <ul>
 *   <li>{@link com.homesynapse.state.ViewCheckpointStore} from the
 *       state-store module — durable storage behind the State Store's
 *       view-checkpoint mechanism (M2 scope placeholder).</li>
 *   <li>{@link com.homesynapse.event.bus.CheckpointStore} from the
 *       event-bus module — durable storage for every event-bus
 *       subscriber's {@code last_delivered_position} against the
 *       {@code subscriber_checkpoints} table (M2.6).</li>
 * </ul>
 */
module com.homesynapse.persistence {
    requires transitive com.homesynapse.platform;

    // M3.6d-b: PersistenceFactory.eventPublisher()/eventStore() return
    // com.homesynapse.event types, .stateStore()/.stateCheckpointSource() return
    // com.homesynapse.state types, .checkpointStore()/.subscriberReadConnectionFactory()/
    // .deadLetterWriter() return com.homesynapse.event.bus types — all three modules
    // appear on the persistence module's public API, so promote to `requires transitive`
    // (LD#10) so PersistenceFactory consumers automatically resolve those types.
    requires transitive com.homesynapse.state;
    requires transitive com.homesynapse.event;
    // M2.6: SqliteCheckpointStore implements
    // com.homesynapse.event.bus.CheckpointStore — the subscriber checkpoint
    // contract owned by the event-bus module (distinct from
    // com.homesynapse.state.ViewCheckpointStore which covers view state).
    requires transitive com.homesynapse.event.bus;

    // M4.0b-4a: CheckpointSerializer (package-private) names com.homesynapse.value
    // .AttributeValue/.StringValue internally — declared non-transitive at its use
    // site (value is not re-exported on persistence's public API). The AttributeValue
    // hierarchy relocated from com.homesynapse.device to the new com.homesynapse.value
    // leaf (AttributeValue Module Relocation Design Note, 2026-05-31).
    requires com.homesynapse.value;

    // M5-A Part 2 (AMD-87): the package-private ExpectationSerializer/Deserializer name
    // com.homesynapse.device.Expectation + its four permits (ExactMatch/AnyChange/
    // EnumTransition/WithinTolerance) internally so a command-bearing CapabilityAdded
    // round-trips — declared non-transitive at its use site (device is not re-exported on
    // persistence's public API). Acyclic: com.homesynapse.device requires value/event/
    // platform only, NOT persistence. Persistence already read device transitively via
    // `requires transitive state -> transitive device`; this makes that read direct.
    requires com.homesynapse.device;

    requires java.sql;
    requires org.slf4j;

    // M2.4: Jackson serialization infrastructure for DomainEvent payload
    // encode/decode in the SQLite event store BLOB column (DECIDE-M2-04).
    // jackson-databind transitively requires jackson-core and jackson-annotations.
    requires com.fasterxml.jackson.core;
    requires com.fasterxml.jackson.databind;
    requires com.fasterxml.jackson.datatype.jsr310;
    requires com.fasterxml.jackson.module.blackbird;

    exports com.homesynapse.persistence;
}
```
`core/device-model/src/main/java/module-info.java`
```java
/*
 * HomeSynapse Core
 * Copyright (c) 2026 NexSys. All rights reserved.
 */

/**
 * Device model — Device, Entity, Capability, registries, and discovery.
 */
module com.homesynapse.device {
    requires transitive com.homesynapse.value;
    // M9.5-DUR (AMD-99): PROMOTED to transitive — RegistryProjection and
    // RegistryEventMapper name DeviceRegisteredEvent/EntityRegisteredEvent/
    // DeviceRemovedEvent on PUBLIC methods of an EXPORTED package, so a plain
    // requires trips -Xlint:exports (-Werror). Paired with the api(...) scope
    // build.gradle.kts already carries (the M9.1/M9.4b lockstep rule).
    requires transitive com.homesynapse.event;
    requires transitive com.homesynapse.platform;

    exports com.homesynapse.device;
}
```
`api/rest-api/src/main/java/module-info.java`
```java
/*
 * HomeSynapse Core
 * Copyright (c) 2026 NexSys. All rights reserved.
 */

/**
 * REST API module — public-facing HTTP interface types for HomeSynapse.
 *
 * <p>Defines request/response records, service interfaces, pagination contracts,
 * authentication types, RFC 9457 error model, and ETag/caching contracts that
 * endpoint handlers (Phase 3) and the WebSocket API module (Block N) compile
 * against. M3.6e.1 adds the first production HTTP plumbing — the
 * {@link com.homesynapse.api.rest.RestFilters#installReadinessGate
 * RestFilters.installReadinessGate} method that registers a readiness
 * gate on {@code /api/*} traffic until the State Projection reaches
 * {@code SubscriberMode.LIVE}.</p>
 */
module com.homesynapse.api.rest {
    // M3.6e.1: ReadinessFilter consumes ReadinessSource (state-store) and
    // observes SubscriberMode (event-bus) via that source. The Javalin
    // Handler interface lives in io.javalin. SLF4J is used for DEBUG-level
    // rejection logs.
    requires transitive com.homesynapse.state;
    requires com.homesynapse.event.bus;

    // M7.5a: the run-query endpoints consume ExplanationService + RunExplanation/
    // RunSummary INTERNALLY (package-private handlers + the Object-erased
    // installRunQueryEndpoints gateway param), so this edge stays PLAIN
    // (non-transitive) — automation is not on rest-api's exported API.
    // build.gradle.kts already has implementation(project(":core:automation")).
    requires com.homesynapse.automation;

    // M7.5a: the causal-chain handler parses the raw command-parameter JSON string
    // (command_issued.parameters) into the wire `params` object. rest-api is the JSON
    // boundary (LTD-08) and already has implementation(libs.jackson.databind); used
    // only inside a package-private handler, so PLAIN requires.
    requires com.fasterxml.jackson.databind;

    requires io.javalin;
    requires org.slf4j;

    exports com.homesynapse.api.rest;
}
```

## §6 The P2 consumer/pin survey (the hub's counts at `5b0e20c`; the lane re-runs each before writing and pastes the counts)
- `grep -rn 'AvailabilityChangedEvent' --include=*.java . | grep -v '/test/' | wc -l` — the hub read 5 USE sites (event-model's record; the adapter's publish; the projection's arm; the trigger evaluator ×2); the LINE count is ≥ 10 (imports, :1106, :581–:582) — paste the lines, not the number. Also `grep -rn 'new AvailabilityChangedEvent(' --include=*.java . | grep '/test/' | wc -l` — every test constructor moves to seven arguments (row 22 among them). The evaluator reads statuses only (row 14) — untouched.
- `grep -rn 'new EntityState(' --include=*.java . | grep -v '/test/' | wc -l` — row 13; every site is a row or a named deviation.
- `grep -rn 'EntityState(' --include=*.java . | grep '/test/' | wc -l` — the test constructors that must gain three arguments (or a test helper that builds them — the lane says which; a helper is the better return).
- `grep -rn '"availability"' --include=*.java api/ web-ui/ 2>/dev/null | wc -l` — the frontend's client types live under `web-ui/dashboard/`; J1 touches NONE of them (unknown keys are ignored by the client's parser — the lane greps `web-ui/dashboard/src` for a strict-keys parse of the entity row and names the hit if any as a [REVIEW] deviation for the FE lane; J1 does not edit `web-ui/`).
- `grep -rn 'FROZEN' integration/integration-zigbee/MODULE_CONTEXT.md core/state-store/MODULE_CONTEXT.md core/event-model/MODULE_CONTEXT.md core/persistence/MODULE_CONTEXT.md api/rest-api/MODULE_CONTEXT.md | grep -i 'availab\|EntityState\|checkpoint\|entities' | head` — the hub's run: 4 hits, all on `zigbee.availability_changed: device={} available={}` (integration-zigbee MODULE_CONTEXT :632, :860 — FROZEN DP-8, OUT OF BOUNDS for every later unit = T:393, untouched by J1); a hit on a token J1 changes is a fork in the plan.
- `grep -rn 'containsExactly' --include=*Test.java core/state-store core/persistence api/rest-api integration/integration-zigbee | grep -i 'availab\|entityId\|stale' | wc -l` — the pinned shapes (#31).
- ARCH-RULE-REACH (#16): the publish site and the projection are existing wirings — no new publisher, no new handler; `:app:homesynapse-app:test` is the proof.
- THE MISS-SCRIPT SWEEP (#28): no resolver appended; the lookup is a constructor argument of an existing type.

## §7 Test requirements (red first; each named in the return with its red text)
- **T1** (`T`, the suite's `TestClock` — the test's :7/:58/:137 advance it; `Clock.fixed` cannot): a mains device silent 61 s is a ping candidate; silent 59 s is not. The red is the NEW 61-s assertion — no existing assertion names 600 s or `MAINS_PING_SILENCE` (:162/:179/:193/:217 advance 11 min and stay green); the :386 one-minute seed sits ON the new 60-s boundary (:314 is a strict `>`) — move it to 30 s and say so.
- **T2** (`T`): a non-mains device whose lookup returns 7200 s transitions `UNAVAILABLE/SILENCE_TIMEOUT` at 7201 s and not at 7199 s; a device whose lookup is empty keeps the 25-h limit (preservation); UNAVAILABLE devices are never re-verdicted (preservation).
- **T3** (`T`): the listener receives, on a `SILENCE_TIMEOUT` transition, the device's LAST reading and last-seen instant (recorded by an earlier `recordFrame`), not null.
- **T4** (the adapter's publish test): the `EventDraft` carries `schemaVersion == 2` and a payload whose `reason`, `lastSeenAt`, `lqi`, `rssiDbm`, `linkAt` equal the listener's arguments; `priority` CRITICAL on offline (preservation).
- **T5** (event-model): the record accepts nulls in the five additions and still rejects a blank status; the all-or-none invariant on the reading triple is enforced in the compact constructor (an `IllegalArgumentException` on a partial triple).
- **T6** (persistence): `decode("availability_changed", 1, '{"previous_status":"online","new_status":"offline"}')` → the record with five nulls — THE PERSISTENCE MAPPER IS SNAKE_CASE (`PersistenceObjectMapper.java:106`; `EventPayloadCodecTest.java:346–:361` pins it): the v2 wire keys are `previous_status`, `new_status`, `reason`, `last_seen_at`, `lqi`, `rssi_dbm`, `link_at`; pin the written form with `contains("\"rssi_dbm\"")` as :346–:361 does; a camelCase literal decodes to a DegradedEvent, never the record. `decode(…, 2, <a full v2 JSON>)` → whole; a v2 JSON with an UNKNOWN extra key still decodes (the posture pinned); `TestEventSamples.availabilityChanged()` (codec test :141) updated with the record (row 22).
- **T7** (state-store): the projection carries the three fields from a v2 event; a v1 event (nulls) sets them null; the entity's `stateVersion` increments as today.
- **T8** (persistence): the checkpoint round-trips the three fields; the pre-J1 checkpoint case is BUILT by serializing with the new code, parsing to an `ObjectNode` and removing the three keys per entity — never a hand-written literal (the composition root's naming strategy is not read by this unit; the test mapper :70–:76 has none) — and loads with nulls.
- **T9** (rest-api): each of the three endpoints renders `availabilityReason`, `lastSeenAt`, `link` (and `link: null` when absent) after the frozen keys — presence and names pinned on all three, the ISO-8601 form on the list endpoint only (the Get endpoints' instants render by Javalin's mapper); the frozen keys' order and names unchanged — `ListEntitiesEndpointTest.java:203–:204` is the ONE key-set pin, updated not deleted.
- **T10** (device-model, ⛔ fork 2): `expectedReportInterval()` on the declared class(es) returns 7200 s; the undeclared classes stay empty (preservation).
- **IT (optional, lifecycle `LinkReadIT`'s home):** if the fake coordinator can advance a `Clock`, one arm: a mains device silent → `availability_changed` v2 with `reason=ping_timeout` within the simulated 65 s. Say in the plan whether it is feasible; it is not a gate.
The census prediction: the Files table has 23 rows — 3 A, 20 M (computed from the table; the plan re-computes after fork 2).

## §8 MODULE_CONTEXT.md — rows only
integration-zigbee: the two constants with their derivations; the lookup and its 25-h fallback; the v2 publish. event-model: `availability_changed` v2's components and the all-or-none triple; the version history. state-store: `EntityState`'s three nullable fields and `EntityLink`; the projection's null rule. persistence: the checkpoint keys (`availabilityReason`, `lastSeenAt`, `link{lqi, rssiDbm, at}` — camelCase, the serializer's own naming); the event's SEVEN snake_case wire keys (`previous_status`, `new_status`, `reason`, `last_seen_at`, `lqi`, `rssi_dbm`, `link_at`); the decode posture for this type ("schemaVersion is informational for `availability_changed`; the codec gates only `state_changed` v1"). rest-api: the three additive keys (camelCase; the two Get endpoints serialize the record) and the frozen-keys rule.

## §9 What to watch out for
- **The direction of failure.** A shorter mains probe makes a flaky device flap AVAILABLE/UNAVAILABLE every ~65 s if its Basic read times out under load — the lawful failure direction, but it emits a CRITICAL event per flap. Count it in the plan (the fleet's mains devices: the two G4s, the S31, the Hue, the TR3 — five) and name the instrument that would show it (the `zigbee.availability_link` lines per hour on the soak night). Do NOT add hysteresis in J1; write the number in §5 of the return if the soak shows it.
- **The reading at a timeout.** The transition's own evidence carries no reading (T:350); the event must carry the tracker's LAST reading, read inside the lock before the state changes.
- **Every `new EntityState(` site** (row 13): the record's arity changes; a site left behind is a compile error (good — the red) but a site that passes `null, null, null` where the prior's values belong is a silent regression (bad — T7's "carried through" case).
- **The key-set pins** in the endpoint tests (row 16) and the record-component pin (row 15) are the frozen tokens of this unit: update, never delete.
- **`FAIL_ON_UNKNOWN_PROPERTIES` is disabled on the persistence mapper (row 7) — do not enable it, do not add a `@JsonIgnoreProperties`:** the rollback path depends on it.
- **The lookup and the lock:** never a registry call under `ReentrantLock` (LTD-11's deadlock surface). The shape: under the lock snapshot `(device, state, lastSeen)` per entry (:299–:321), release, apply BOTH lookups outside (`powerSourceLookup` runs under the lock today at :312 — move it too), compare, then `transition()` as :325–:328 already does outside the lock.
- **Tests must inject `Clock`.** Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` in this module's test code. Use `Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC)` injected via constructor/`@BeforeEach`. **Enforcement reach:** `NO_DIRECT_TIME_ACCESS` runs from `com.homesynapse.app`'s test classpath, so it mechanically catches PRODUCTION code in every non-whitelisted module (plus app's own tests) — it does **not** scan this module's test source set. Clock-injection here is a self-enforced project convention that PM review, not `./gradlew check`, enforces. This module's suites already inject a `TestClock` (the tracker test :7/:58/:137) — use it where the test must advance time.
- **Frozen tokens and moving Javadoc:** T:393's log line is byte-frozen (A:1652–:1653) — untouched; the "10 min" wording at `AvailabilityTracker.java:13–:15`, `AvailabilityReason.java:39`, T:22–:27/:52/:281–:283 and the test name at :156 move with the constant.
- The Pi's clock in any log you quote is EDT; the API's `meta.timestamp` is UTC; your stamps are from `date -u`.

## §10 Coder pushback welcome
The `EntityLink` record vs three flat fields on `EntityState`; the lookup's shape (a `Function` vs a per-cycle map); whether the projection should keep the prior's reading when a v2 event carries a null triple (the hub says NO — the event is the truth at its instant; argue with a case); the IT's feasibility; the mains probe at 60 s vs 30 s (argue with the radio-cost arithmetic). Evidence-based pushback in the plan is the cheapest edit this unit will ever get.

## §11 Out of scope
A `link_observed` event per device per period and a live `link` on an AVAILABLE device (J1b — a register row); hysteresis or a flap counter; a yaml key for the probe (fork 1 b, unless the plan argues it); any `web-ui/` edit (the FE lane reads the three keys when it wants them); the bench's `avail:` digest line (IR-118, a bench unit); the docs repo's contract note (DOCS-2, a docs row); any change to the mains ping's mechanics (one Basic read, 5 s); the `permit_join` window or any admission path (J2); the Hue (IR-112).

## §12 The plan's shape (`<CT-date>_J1_plan.md`, ≤ 8,192 B; written FIRST; the lane STOPS after it)
§0 the premise rows 1–19 re-run — one line each: the instrument's output or "holds" with the line; any row that fails and why · §1 the three forks settled, each with the BYTES that settled it (fork 2 quotes row 19's lines) · §2 the Files table as you will write it (A/M; the row count; the census) · §3 the tests you will write first, each with its predicted red text · §4 risks and pushback (§10) · §5 the return cap re-computed (3 KB + 1 KB × rows). Last line: `PLAN-RETURNED <path> <bytes>`. Then wait for `GO`.

## §13 Success criterion (binary)
`./gradlew check` green on the branch with every §7 test green after an observed red; a v1 and a v2 `availability_changed` row decode to the same class; `GET /api/v1/entities` renders `availabilityReason`, `lastSeenAt`, `link`; the pre-J1 checkpoint loads; the return on disk at its path under its cap with the twelve rows re-run. On the rig (after the landing, the soak night): a mains device unplugged reads `UNAVAILABLE` with `availabilityReason=ping_timeout` and a `lastSeenAt` inside 90 s — pre-registered (D-v94-25), adjudicated by the hub.

## §14 Work unit completion (WUCP Phase 1)
The return (§0); the coder-handoff entry (§6 of the return); the deviations ledger; the MODULE_CONTEXT rows (§8); the branch at its head sha, un-pushed, named in the return's last line.

## §15 The dispatch (Nick pastes the line below into Claude Code in `~/Desktop/Code/ClaudeFolder/homesynapse-core`)
```
You are the J1 Coder lane (LINK-READ-2 + IR-121) on my desk. Read ../nexsys-hivemind/context/instructions/2026-10-03_coder-lane_J1_LINK-READ-2_IR-121_dark-device-named_LOCAL_desk-coding-instruction.md WHOLE, then its §2 set by range. Execute §0 exactly: date -u first; porcelain empty; the branch; the premise rows re-run; the PLAN written to its path and STOP at PLAN-RETURNED. No code before my GO.
```
