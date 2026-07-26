<!--
file: context/instructions/2026-07-19_LEARN-PERSIST_persist-learned-zonetypes_coding-instruction.md
purpose: Coding instruction — LEARN-PERSIST: persist wire-learned IAS zoneTypes across restarts (ride the existing zigbee-devices.json additive-sidecar precedent) and rehydrate them at construction, so adopt-time classification reads the learned truth regardless of the cached-interview fast-propose race. The REQUIRED predecessor to the 04P adoption / D1 [M] 5/5.
audience: Coder (Claude Code lane, homesynapse-core).
state-type: coding instruction (issue-ready).
status: ISSUE-READY 2026-07-19 (v35 hub, beat 3). Dispatch on Nick's word.
provenance: the 2026-07-19 04P BENCH-STOP finding (context/handoff/2026-07-19_04p-adoption_BENCH-STOP_learn-persist-finding.md) — hub two-layer audited; every source claim below re-verified at core HEAD 554e18c by the hub same-day (pre-verification: context/pre-verifications/WU-LEARN-PERSIST.md, P1–P14).
-->

# Coding Task: LEARN-PERSIST — Persist Learned IAS ZoneTypes Across Restarts

**Subsystem:** integration-zigbee (single module; no other module is touched)
**Design Doc:** Doc 08 (Zigbee Adapter) — Locked; §3.14 local device metadata cache. Governing precedent: the §8.1 M-1 `lastKnownAvailability` additive sidecar inside `zigbee-devices.json` (frozen `ZigbeeDeviceRecord` untouched; the FILE carries the field).
**Phase:** 3-Implementation
**Task Brief Reference:** the 04P BENCH-STOP / LEARN-PERSIST finding, 2026-07-19 (hub-audited ACCEPT-WITH-ADJUDICATIONS)

## What This Implements

The 2026-07-19 bench session falsified the two-window adoption plan for cached-interview devices: on the 04P's re-join, `device_proposed … COMPLETE` fired **0.8 s** after the announce (cached interview) while `ias_zone_type_learned … CONTACT` landed **~9.2 s later** (the IAS enroll is TCLK-gated). The config-accept adopt fires AT the proposal, the `learnedZoneTypes` map is in-memory and wiped by the restart the accept-list edit forces, and `adopt()`'s classify is a learned-ONLY read with the MOTION fallback — so adopting would have durably classified the contact sensor as MOTION (no `device_removed` emitter exists; undo = full re-formation). W2-LEARN's learn itself is silicon-confirmed working; what's missing is durability. This WU persists every wire learn into the existing `zigbee-devices.json` cache (a new additive top-level section, exactly the `lastKnownAvailability` precedent) and seeds `ZclIngestionUnit`'s learned map from it at construction — structurally BEFORE the ingestion cycle can process any join — so a cached-interview fast propose reads the learned truth. The classifier, the adopt trigger, and the frozen record are untouched.

## Files to Read Before Starting

| File | Why |
|---|---|
| `integration/integration-zigbee/MODULE_CONTEXT.md` | Type inventory; the W2-LEARN section (shared learn core, LEARNED-ONLY accessor, F-8 handler invalidation, cycle-thread confinement); the M9.4-ADP adoption contract (initialize-time accept list; adopt-at-proposal); the §8.1 M-1 availability-sidecar precedent |
| `integration/integration-zigbee/src/main/java/module-info.java` | Verbatim JPMS truth (quoted below) — MUST NOT change in this WU |
| `.../zigbee/ZclIngestionUnit.java` | The learn core `:528-:551` (put `:542`, invalidate-on-change `:546`, INFO `:548`), the LEARNED-ONLY accessor `:584-:587`, `effectiveZoneType` `:594-:598`, the ctor (7 params), `learnedZoneTypes` at `:142` |
| `.../zigbee/ZigbeeDeviceCache.java` | The pattern to extend: Jackson tree model interior-only; 30 s `WRITE_DEBOUNCE`; `WRITE_FAILURE_BACKOFF_MILLIS` (F-14); writes snapshot under the `ReentrantLock`, I/O outside it; shutdown flush (`:292`); loads-if-exists ctor (`:77`); the `lastKnownAvailability` additive per-device carry |
| `.../zigbee/ZigbeeIntegrationAdapter.java` | Wiring: cache constructed `:279-:280` (`dataDirectory.resolve("zigbee-devices.json")`); ingestion constructed `:323` (AFTER the cache — the seed point); `learnedZoneTypeFor` `:1029-:1032` (the null-guarded zoneTypeSource); `adoptIfAccepted` `:815/:841` (DO NOT TOUCH); `readAdoptAcceptList` `:289` |
| `.../zigbee/ZigbeeAdoptionSlice.java` | `:348-:358` — the adopt-time classify ("reads in-memory learned state only — never blocking, never I/O"); untouched by this WU |
| `.../zigbee/EndpointClassifier.java` | `iasCapability` `:175-:177` CONTACT-else-MOTION; untouched |
| `.../zigbee/ZclIngestionUnitTest.java` + `ZigbeeWave2ContactAdoptionTest.java` | The existing test idioms (logback capture; the enroll-driven e2e twin with its `containsExactly` learn-INFO pin — the pin MUST keep holding) |
| `context/pre-verifications/WU-LEARN-PERSIST.md` | P1–P14 — every load-bearing signature verified same-day at `554e18c`; re-verify at your dispatch HEAD before writing |

**Current `module-info.java` (verbatim — zero changes in this WU):**
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

| Action | File Path | Description |
|---|---|---|
| MODIFY | `integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/ZigbeeDeviceCache.java` | The additive `learnedZoneTypes` top-level JSON section + `recordLearnedZoneType(...)` + `learnedZoneTypeIds()` snapshot |
| MODIFY | `.../zigbee/ZclIngestionUnit.java` | Ctor-seed of the learned map (silent; tolerance-scanned) + the write-through learn sink |
| MODIFY | `.../zigbee/ZigbeeIntegrationAdapter.java` | Wire seed + sink at ingestion construction; emit `zigbee.learned_zonetypes_rehydrated: count={}` |
| MODIFY | `.../zigbee/ZclIngestionUnitTest.java` | + seed/tolerance/sink legs (tests-first, red-first where red is honest) |
| MODIFY | `.../zigbee/ZigbeeDeviceCacheTest.java` (or the module's existing cache test) | + round-trip / absent-section / corrupt-tolerance legs |
| MODIFY | `.../zigbee/ZigbeeWave2ContactAdoptionTest.java` | + the RESTART-SIMULATION leg (the race, hardware-free); the two existing methods + the `containsExactly` pin stay byte-untouched |
| MODIFY | `integration/integration-zigbee/MODULE_CONTEXT.md` | The LEARN-PERSIST section + the cached-interview-race gotcha (at completion) |

## Technical Specification

### Settled Decision Points (DP-LP-1..8)

- **DP-LP-1 — Ride `zigbee-devices.json`, not a new file.** A new **top-level** JSON section `learnedZoneTypes`: an object keyed by the IEEE hex string (the cache's existing key form), value = the learned **ZCL zone-type id** (integer; `ZoneType.zclId()`). Top-level (NOT a per-record field) so a learn for a device with no record node still persists, and the frozen `ZigbeeDeviceRecord` shape is provably untouched. The existing loader must tolerate the section's ABSENCE (old files load clean) and unknown content (skip + WARN ⇒ empty — fail-safe = current behavior). Custody note: the file is already preserved by bench custody resets; the interview-cache-clear coupling is self-healing (a cleared cache forces a fresh slow interview, where enroll-before-propose holds).
- **DP-LP-2 — Persist the wire id, not the enum name.** Values are `zclId` longs; rehydration maps them through the SAME candidate-scan tolerance the learn core uses (unknown id ⇒ skip + DEBUG, never a crash, never a learn). One tolerance code path, rename-proof.
- **DP-LP-3 — Write-through on EVERY successful learn, both feeders, both cases.** In the shared learn core (`learnZoneType(IEEEAddress, long)`), after the map `put` succeeds, invoke the sink — for the change case AND the same-as-effective silent case (a first wire learn that matches the resolver default is still a learned fact and MUST persist). The sink is a ctor-injected functional param (suggested: `ObjLongConsumer<IEEEAddress>`-shaped or a small package-private interface; Coder's call) wired to `cache::recordLearnedZoneType`. `recordLearnedZoneType` mutates state under the cache lock and marks dirty ONLY — no I/O on the cycle thread; the existing per-cycle `maybeFlush()` + debounce + F-14 backoff + shutdown flush carry the I/O exactly as they do for availability.
- **DP-LP-4 — Seed at construction, silently.** `ZclIngestionUnit`'s ctor gains a seed input (suggested: `Map<Long, Long>` ieee→zclId; Coder's call on exact shape) applied through the tolerance scan into `learnedZoneTypes` — a plain seed loop, **NOT** the INFO-firing learn path: NO `ias_zone_type_learned` line at seed time (it is not a wire learn; the e2e twin's `containsExactly` pin and the operator's log glances depend on that INFO meaning exactly one thing), no handler invalidation needed (no handlers exist pre-cycle). The adapter seeds from `cache.learnedZoneTypeIds()` at the existing construction site (`:323` area) — the cache (`:279`) already precedes it, so **rehydrate-before-joins holds by construction**, not by ordering discipline.
- **DP-LP-5 — LEARNED-ONLY is preserved.** Only previously-PERSISTED LEARNS seed the map; the resolver default is never written to the cache and never seeded. The classifier's unlearned arm (MOTION fallback) stays reachable for genuinely-unlearned devices — the existing `learnedZoneType()` accessor and `effectiveZoneType()` precedence are byte-untouched.
- **DP-LP-6 — The one new observable: `zigbee.learned_zonetypes_rehydrated: count={}`** (INFO, adapter-side, after seeding; count = entries APPLIED post-tolerance). The anti-vacuous boot glance-point: an operator confirms persistence worked before opening any window. Token name frozen as written.
- **DP-LP-7 — No re-learn INFO noise across sessions.** After rehydration, a live wire re-learn of the same type takes the same-as-effective silent path (existing behavior) — verify, don't change.
- **DP-LP-8 — Nothing else moves.** ZERO: event mints (73/43/55 hold) · `module-info.java` · build files · config schema (the section is DATA in an existing data file, not config) · public surface (everything stays package-private) · new locking on the cycle thread (the cache's existing `ReentrantLock` discipline is the only lock touched; LTD-11) · `EndpointClassifier` · `ZigbeeAdoptionSlice` · `adoptIfAccepted`/propose timing · frozen tokens (`ias_zone_type_learned` / `ias_zone_enrolled` / `ias_zone_type_unknown` byte-untouched as emitted strings).

### Error Handling

| Condition | Behavior | Recovery |
|---|---|---|
| `learnedZoneTypes` section absent in an existing file | Empty map; no log | Normal first-run/upgrade path |
| Section present but malformed (non-object, non-numeric value, bad IEEE key) | Skip the bad entry (or section) + one WARN; continue with what parses | Fail-safe = unlearned ⇒ existing MOTION-default behavior |
| Unknown zclId in a persisted entry | Skip + DEBUG (the existing `ias_zone_type_unknown` tolerance class; do not reuse that exact token for the seed path — it is a wire-path token; a DEBUG is enough) | Device stays unlearned |
| Cache write fails | Existing F-14 backoff (unchanged) | Existing behavior |

### Tests First (write RED where red is honest, then implement)

1. **Cache round-trip:** `recordLearnedZoneType` → flush → NEW `ZigbeeDeviceCache` instance on the same path → `learnedZoneTypeIds()` returns the entry. Plus: absent-section tolerance (an existing-format file loads clean, empty ids) and malformed-section tolerance (WARN + empty, no throw).
2. **Silent seed:** a unit constructed with a seed entry answers `learnedZoneType()` present WITHOUT any frame processed, and the log capture pins the ABSENCE of any `ias_zone_type_learned` line at construction (the DP-LP-4 pin). Unknown-id seed entry ⇒ absent + no crash.
3. **THE RACE LEG (the regression tooth, hardware-free)** — in `ZigbeeWave2ContactAdoptionTest`: session A learns CONTACT via the production enroll path (existing machinery) and the cache captures it; a SIMULATED RESTART (new cache instance from the same file → new unit/slice seeded from it) then classifies/adopts the 04P-class device **with ZERO enroll or attribute frames processed in session B** → `BINARY_SENSOR/contact`, never motion. This leg is RED at HEAD (the seed doesn't exist) — it is the instruction's falsification of the bench race, in a unit-scale harness.
4. **Write-through both cases:** a wire learn that CHANGES the effective type reaches the cache; a wire learn EQUAL to the effective type (silent path) ALSO reaches the cache (the DP-LP-3 same-case pin).
5. **Rehydrate INFO:** `zigbee.learned_zonetypes_rehydrated: count=N` fires with the applied count (and count excludes tolerance-skipped entries).
6. **Existing pins hold:** the e2e twin's two existing methods byte-untouched and green; the `containsExactly` learn-INFO pin still passes (proof the seed path emits nothing).

**Named mutants (all realizable against control flow — verify each kills):** (M1) delete the seed loop ⇒ test 3 fails (empty map at adopt). (M2) delete the sink invocation ⇒ test 4 fails (cache never written). (M3) route seeding through the INFO-firing learn path ⇒ test 2's absence pin fails.

### STOP Gates

- **G-LP-1:** Before writing: confirm at source that the existing loader tolerates an unknown top-level section (or add tolerance INSIDE this WU's diff); if tolerance would require touching the frozen `ZigbeeDeviceRecord` or its serialization ⇒ STOP, report.
- **G-LP-2:** If preserving LEARNED-ONLY (DP-LP-5) proves impossible without classifier changes ⇒ STOP, report (the classifier is out of scope).
- **G-LP-3:** If any public-surface, module-info, or build-file change appears needed ⇒ STOP, report.
- **G-LP-4:** Baseline re-derive FORCED-FRESH at your dispatch HEAD before any edit (`./gradlew :integration:integration-zigbee:test --rerun-tasks`; expected 526/0/0 AS-AT `554e18c` — re-derive, never carry; any drift ⇒ STOP, report).
- **G-LP-5:** If the e2e twin's existing `containsExactly` pin cannot survive your diff ⇒ STOP, report (the pin is a frozen instrument).

## What to Watch Out For

- **Tests must inject `Clock`.** Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` anywhere in test code. Enforcement reach (corrected 2026-06-13 per the M6.2 Coder finding): the ArchUnit rule `NO_DIRECT_TIME_ACCESS` runs only from `com.homesynapse.app`'s test classpath — production code in any module IS caught, but a non-app module's test code is a self-enforced convention. Use `Clock.fixed(...)` injected via constructors (the module's existing idiom; `ZigbeeDeviceCache` already takes a `Clock`).
- The learn core runs on the ingestion cycle thread; `recordLearnedZoneType` must be state-mutation-only under the cache lock (no I/O) — the I/O rides `maybeFlush()`/shutdown exactly like availability (F-14 stays intact).
- The seed map applies at construction — before `processCycle()` can run — so no invalidation or synchronization gymnastics are needed; do not add any (LTD-11: no new locking).
- Jackson stays interior-only (no Jackson type on any signature — the D-M92-1 pattern; all touched types are package-private anyway).
- `spotlessApply` before handoff; the full `./gradlew check` runs in-session per this WU's CC-lane grant (the W2-LEARN precedent).
- **Welcome pushback:** if you find a cleaner seam (e.g., a different seed-shape or sink-shape) that preserves every DP above, take it and record the deviation [INFO]; if any DP itself looks wrong at source, STOP and report — do not silently implement around it.

## Build Discipline (this WU's CC-lane grant)

```
./gradlew :integration:integration-zigbee:test --rerun-tasks     # baseline re-derive (G-LP-4), then stage-A red, then stage-B green
./gradlew :app:homesynapse-app:test :lifecycle:lifecycle:test --rerun-tasks   # defensive
./gradlew check                                                  # full, in-session
./gradlew :integration:integration-zigbee:spotlessApply
```
Mutation verification in-session for M1–M3 with `cmp`-proven byte-identical restores (the W2-LEARN idiom). CI on the pushed commit remains the gate of record; the hub's two-layer audit precedes ANY commit order (Success Criterion 5).

## Success Criteria

1. All new legs green; 526-baseline + new count forced-fresh green; app/lifecycle defensive green; full `check` green; zero frozen-token diffs; zero public-surface/module-info/build/config diffs.
2. Mutants M1–M3 each demonstrably killed; restores cmp-verified.
3. The race leg (test 3) is the standing hardware-free regression of the 2026-07-19 bench finding.
4. MODULE_CONTEXT gains the LEARN-PERSIST section + the cached-interview gotcha ("a cached interview proposes in <1 s, before the TCLK-gated IAS enroll; enroll-before-propose holds only for FRESH interviews").
5. Hub two-layer audit → commit → CI → deploy → the re-authored 04P operator package (persist-verified two-window): window #1 learn fires AND `learned_zonetypes_rehydrated`-verified persisted BEFORE the 04P is ever listed → accept-list + restart → window #2 re-pair → fast propose → adopt reads CONTACT → `device_adopted entities=1` BINARY_SENSOR/contact → **D1 [M] 5/5** → BENCH-CONST 6/6 → boot-health GREEN.
