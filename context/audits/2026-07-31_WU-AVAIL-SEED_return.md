<!--
file: context/audits/2026-07-31_WU-AVAIL-SEED_return.md
purpose: Coder return for WU-AVAIL-SEED — availability seed + boot truth (core repo; the F2 [M] producer).
audience: Hub (two-layer audit), Nick
state-type: audit-record
status: FILED 2026-07-31 (Coder, host-CC desk session)
-->

# WU-AVAIL-SEED — Return (2026-07-31)

**Instruction:** `context/instructions/2026-07-31_WU-AVAIL-SEED_availability-seed-and-boot-truth_coding-instruction.md` · **Baseline:** core `4288a9d` (HEAD verified `4288a9d90c14b36ca987ab5b28b817c40c24ba67`, porcelain EMPTY at session start) · **DP-3 ruling:** **STOP** (carried on the dispatch line — "stop manufacturing the relink 'available'"; Branch STOP executed, T-5 active, G-4 not in play) · **Duplicate-dispatch check:** newest handoff entry = this WU's own DISPATCH READY (v42 beat 9); B3 DELIVERED is bench-repo — fresh dispatch, verify-not-redo satisfied.

---

## §1 — P0 re-verification transcript (G-5: ALL §6 pins, at source, pre-code)

| Pin | Verified at source | Status |
|---|---|---|
| `ZigbeeIntegrationAdapter:318` `Map.of()` construction | `availabilityTracker = new StandardAvailabilityTracker(clock, …` begins at **:318**; the empty map literal at **:321**; the M9.6 "EMPTY, deliberately" comment block at :306–:316 | ✅ exact |
| `ZigbeeAdoptionSlice:553` relink emission | `publishRoot(new EventDraft(… AVAILABILITY_CHANGED … SubjectRef.device …` at **:546–:555** with `new AvailabilityChangedEvent("unknown", "available"),` at **:553**; the relink log line `zigbee.device_relinked` at :556–:557 | ✅ exact |
| `StandardAvailabilityTracker` + `ZigbeeDeviceCache` carry `lastKnownAvailability`; the cache writes via `setAvailability`; `zigbee-devices.json` the carrier | tracker ctor :92–:113 (M-1 init — **and the aggravator locus: `state.lastSeen = now` at :103/:110, boot-time stamping**); cache map :75, `setAvailability` :188–:197, `availabilitySnapshot()` :216–:223 (production-unconsumed = the written-never-read half), file wiring :35/:280 | ✅ exact |
| `:735`-era `productionLoop → runCycleOnce → evaluateAvailabilityTimeouts`; `:1140–1165` `publishForEntities` + conflict WARN | `productionLoop()` :730 → `runCycleOnce()` :735/:464 → `evaluateAvailabilityTimeouts()` :470/:485; `publishForEntities` :1140–:1163, `SequenceConflictException` swallow + `zigbee.availability_publish_conflict` WARN :1157–:1161 | ✅ exact |
| `StateProjection:856` handler; `ListEntitiesEndpoint:160` read surface | `else if (envelope.payload() instanceof AvailabilityChangedEvent ac)` at **:856** (applies `parseAvailability(ac.newStatus())`, preserves `prior.stale()`); `summary.put("availability", …)` at **:160** + `summary.put("stale", state.stale())` at :161 — the F2 discriminator read | ✅ exact |

**G-5 verdict: PASS — zero drift from `4288a9d`.** Bonus source facts recorded pre-code: `parseAvailability` (StateProjection:1005–:1015) maps `"available"`→AVAILABLE defensively and unknown strings → UNKNOWN; `evaluateTimeouts` (:173) skipped `lastSeen == null` entries and non-AVAILABLE states — the two eligibility seams DP-1 had to widen; `adapter.close()` → `cache.flush()` (:398–:406) — the shutdown-persistence leg T-7 rides.

## §2 — Per-DP disposition (source citations)

**DP-1 — THE SEED: BUILT.** `initialize()` replaces `Map.of()` with a seed built from `cache.all()` × `availabilitySnapshot()` × the new `lastEvidenceSnapshot()` — every cached device enters tracking. `StandardAvailabilityTracker` grows minimally per the instruction's sanction, package-private, zero new public types: nested `record Seed(Boolean available, Instant lastEvidenceAt)` (both components nullable — null availability seeds UNKNOWN; null recency = unknown), ctor seeds SILENTLY with `lastSeen` = the **persisted** instant (the `state.lastSeen = now` boot-stamp is gone — the aggravator's locus), `evaluateTimeouts()` eligibility widened from "AVAILABLE with non-null lastSeen" to "everything except UNAVAILABLE" with null-lastSeen = infinite silence (an UNKNOWN entry can only be a seed — live transitions never leave one behind, verified at `transition()`: every path exits AVAILABLE/UNAVAILABLE). Seeded-UNAVAILABLE devices are never pinged/re-verdicted (recovery stays evidence-driven — pre-WU semantics preserved, test-pinned). The seeded-vs-evidenced distinction the instruction anticipated: `DeviceState.evidenced` + package-private `isEvidencedAvailable()` — consumed by the one liveness-asserting consumer (`seedFreshAdoption`), closing the last manufacture path (a sidecar-seeded available can no longer produce the adoption-time per-entity "online"; production adoption is announce-preceded so evidenced flows are unaffected — unit- and adapter-pinned).

**DP-2 — BOOT TRUTH, floor: BUILT (T-7 green at the composition root).** The verdict rides the untouched normal path: tracker verdict → `EntityAvailabilityPublisher.publishForEntities` (entity grain, per relinked entity — `entitiesFor` is populated by the DP-6 rehydration relink at initialize) → the real bus → `StateProjection:856` → `StateQueryService.materialized` — the same instance `HomeSynapseCore` wires into the REST endpoints (HomeSynapseCore:578 construction, :928/:935 endpoint wiring). No projection/read-path **production** code was touched. **Stretch: G-3 — floor only + OBS-1 (§6).** **Rejected mechanisms honored:** no per-boot event floods (seeding publishes nothing — T-3 pinned), no arch exemptions, no rule edits.

**DP-3 — Branch STOP: EXECUTED.** The `publishRoot(… "unknown", "available" …)` statement at ZigbeeAdoptionSlice:546–:555 is deleted; the relink log line stays byte-identical and is now the relink's sole observable (RestartHonestyIT's re-link barrier awaits it — see §6 D-2). The now-unused `AvailabilityChangedEvent` import removed (spotless law). T-5 pinned at three levels: slice-unit (both relink tests → zero events), adapter (rehydration + re-announce relinks → zero events of ANY grain + the log line ×2), composition (ZigbeeConfigAcceptedAdoptionTest: device-grain count pinned to ZERO, the entity-grain adoption seed pinned to survive).

**DP-4 — THE RESTART CLOCK: BUILT.** Additive per-device `lastEvidenceAt` (ISO-8601 UTC) in `zigbee-devices.json`, file-sidecar level exactly like `lastKnownAvailability` (the frozen `ZigbeeDeviceRecord` untouched). Sources of evidence: every `onFrame` (the SAME `clock.instant()` fed to the tracker — persisted and in-memory clocks can never disagree) + every answered ping. **Write-rate floor, stated:** value updates are in-memory puts under the existing lock; FILE writes ride the pre-existing mechanisms unchanged — per-transition dirty via `setAvailability`, the 30 s-debounced `maybeFlush()` each cycle (note: `recordFrame` already dirtied the cache per frame at baseline — this WU adds ZERO write-rate; the effective cadence is ≤1 write/30 s under traffic, comfortably above the 5–15 min floor), and the shutdown `flush()` in `close()` (source-verified :398–:406). Per-frame FILE writes do not occur (the debounce is the mechanism). **Compat:** absent field = old-format, loads silently, seeds unknown-recency (T-4 at cache + adapter levels); malformed VALUE = per-device skip + ONE WARN, never a load failure (§6 D-5). **Pinned reasoning honored:** persisted time is a lower bound; unknown recency = infinitely stale (false-ALIVE-avoidance wins the tie — the first post-deploy boot pings mains devices immediately, alive ones answer with no false verdict, and battery devices take a one-time honest verdict that self-heals; priced in MODULE_CONTEXT).

**DP-5 — OBSERVABILITY: BUILT.** (a) `zigbee.availability_seeded: devices=N from_sidecar=K unknown=U` — INFO, once per boot, unconditional (N = cached devices entered, K = with persisted availability, U = N−K); exact-line test-pinned (`devices=2 from_sidecar=1 unknown=1` on the two-device fixture). (b) `zigbee.availability_ping: device=<ieee> outcome=<ok|timeout|error> rttMs=<n>` — DEBUG per ping; rtt from the injected clock (NO_DIRECT_TIME_ACCESS-clean); `ok` and `timeout` test-pinned; `error` = the unresolvable-candidate arm (no record / F-6 sentinel address). (c) `zigbee.availability_changed` verified firing identically on seed-originated verdicts — test-pinned verbatim in T-1 (`… available=false` as the ONLY line). (d) `availability_publish_conflict` byte-untouched (in-context verified). Tokens documented in MODULE_CONTEXT per WUCP.

## §3 — The test record

**Red-first, staged (one module holds both behavioral and compile-red legs, so the evidence was split):**

**Stage A1 (behavioral reds at `4288a9d` — existing APIs only): 12 zigbee failures + 1 lifecycle failure, every one for its designed reason (XML-quoted):**
- **T-1** `seededStaleMains_deadDevice_offlineAtFirstCycle`: `[persisted staleness makes the seeded device a candidate at the first cycle — the seed entered it into tracking] expected: 1L but was: 0L` — **the mandated red: `Map.of()` ⇒ never tracked, never pinged.**
- **T-2** `seededStaleBattery_timesOutAtFirstCycle`: `[the battery timeout fires from the persisted clock — a boot-time seed would wait another 25 h …] Expected size: 1 but was: 0` — **the mandated red: no verdict without the seed.**
- **T-5** `relinkPaths_publishZeroAvailability_logLinePreserved`: `[NO availability event of ANY grain rides either relink path…] expected: 0L but was: 3L` — the full boot-burst disease visible at baseline (rehydration device-grain + announce relink + first-frame edge).
- **T-4** `oldFormatSidecar_unknownRecency_mainsPingedAtFirstCycle`: `expected: 1L but was: 0L`.
- **T-6** `seededAvailable_promptEvidence_publishesNothing`: `expected: 0L but was: 2L` (the pre-seed first-frame edge + the rehydration burst).
- **DP-5(a)** `bootSeedLine_countsDevices`: expected `zigbee.availability_seeded: devices=2 from_sidecar=1 unknown=1`, actual `[]`.
- **DP-5(b)** `seededStaleMains_pingAnswered_staysQuietRefreshesClock`: `expected: 1L but was: 0L`.
- **Evidence guard** `seededUnevidencedDevice_adoption_neverManufacturesOnline`: `[the frame confirms the seeded-available state silently] expected: 0L but was: 1L`.
- **T-2 boundary** `seededFreshBattery_firstCycleQuiet`: `expected: 0L but was: 1L` — red at baseline via the rehydration burst (disclosure D-6: red for the L1 reason, not its own boundary reason; its boundary tooth is regression).
- **T-5 slice pins**: `ieeeMatchRelinksNotReadopts` (isEmpty vs 1), `relinkNeverMutatesTheRegistry` (isEmpty vs 2), `relinkOfAdoptedListedDevice_neverCallsAdopt` (total 1 vs 2 / device-grain 0 vs 1).
- **T-7** `AvailabilityBootTruthIT`: `timed out awaiting the DP-2 floor: served UNAVAILABLE within one window of boot` — behavioral red at the composition root (untracked ⇒ no ping ⇒ served AVAILABLE forever = F-14 reproduced under test).
- Zigbee stage-A1 run: **544 tests, EXACTLY 12 failed**; lifecycle: **60 tests, EXACTLY 1 failed** (RestartHonestyIT GREEN with the swapped barrier — baseline-compatible by design, disclosed D-2).

**Stage A2 (compile-red at `4288a9d` — the new seams, disclosed):** `compileTestJava` FAILED on the designed missing symbols — `class Seed` (×3 sites) + `method isEvidencedAvailable(IEEEAddress)` (×4 sites) quoted from the compiler; the cache legs' `recordEvidence`/`lastEvidenceAt`/`lastEvidenceSnapshot` sit behind the same wall.

**Green (final tree), forced-fresh ×2 with executed-state proof (the `--rerun`-binding lesson applied — per-task `--rerun`, task lines verified executing, result-file mtimes fresh):**
- `:integration:integration-zigbee:test` — **557/0/0** (544 + 13 stage-A2 legs) ×2 fresh JVMs.
- `:lifecycle:lifecycle:test` — **60/0/0** (59 + the new IT) ×2 fresh JVMs; T-7 GREEN: served AVAILABLE inside the pre-convergence window (the boundary half), served UNAVAILABLE after one 11-min window + one cycle.
- `spotlessApply` (both touched modules): **zero reformats** (diffstat byte-identical across the apply).
- **`./gradlew check` — FULL GATE GREEN: 156 actionable tasks, 87 executed** (the one granted full check, against the final tree; every arch rule green — zero module-info/build-file/dependency changes to threaten them).

**Fixture-paired boundaries (every PASS with its false-verdict twin):** T-1 ↔ fresh-recency-mains-not-a-candidate (unit U8) + ping-answered-stays-quiet (W8b); T-2 ↔ 1 h-fresh battery quiet (W3) + the 24 h→26 h window-exact unit pair (U10); T-3 ↔ the all-shapes silent-seed unit leg + `initializeAlone_noTrackerActivity` (now exercising a NON-empty seed); T-4 ↔ the cache old-format load + malformed-value skip pair; T-5 ↔ the preserved log line asserted alongside every zero-event pin; T-6 ↔ seeded-UNKNOWN-first-evidence-edges (U6 — the edge still fires where it must); T-7 ↔ the in-test pre-convergence AVAILABLE assert (the accepted brief-false-ALIVE, proving the verdict came from the timeout machinery, not a boot reset); the evidence guard ↔ `evidencedAvailable_distinguishesSeededFromLive` (frame and ping-reply both clear the mark).

## §4 — The exact porcelain census (13 entries: 12 M + 1 ??)

```
 M integration/integration-zigbee/MODULE_CONTEXT.md
 M integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/StandardAvailabilityTracker.java
 M integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/ZigbeeAdoptionSlice.java
 M integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/ZigbeeDeviceCache.java
 M integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/ZigbeeIntegrationAdapter.java
 M integration/integration-zigbee/src/test/java/com/homesynapse/integration/zigbee/StandardAvailabilityTrackerTest.java
 M integration/integration-zigbee/src/test/java/com/homesynapse/integration/zigbee/ZigbeeAdoptionSliceTest.java
 M integration/integration-zigbee/src/test/java/com/homesynapse/integration/zigbee/ZigbeeAvailabilityWiringTest.java
 M integration/integration-zigbee/src/test/java/com/homesynapse/integration/zigbee/ZigbeeConfigAcceptedAdoptionTest.java
 M integration/integration-zigbee/src/test/java/com/homesynapse/integration/zigbee/ZigbeeDeviceCacheTest.java
 M integration/integration-zigbee/src/testFixtures/java/com/homesynapse/integration/zigbee/ZigbeeHardwareFreeRig.java
 M lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/RestartHonestyIT.java
?? lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/AvailabilityBootTruthIT.java
```

**Sweep-guard:** safe IFF a fresh lock-free porcelain shows exactly these 13. The two lifecycle entries are the §7-clause touches, named per instruction: the NEW `AvailabilityBootTruthIT` is T-7's DP-2-floor leg (test-only, rides the existing composition-root machinery — cited in §7 below), and `RestartHonestyIT` is the unavoidable DP-3 consequence (its `:111` await pinned the now-removed relink emission as a sync barrier; reworked to await the preserved `zigbee.device_relinked` log line — see §6 D-2). Zero production files outside integration-zigbee. Zero bench changes; hivemind touched only by the two WUCP-mandated writes (this return + the coder-handoff DELIVERED entry).

## §5 — STOP-gate status ×5

- **G-1 (schema/new event type):** NOT TRIPPED — zero mints; the entity-grain `availability_changed` publish path is pre-existing (M9.6).
- **G-2 (floor needs an event flood):** NOT TRIPPED — the floor rides seed + ping + the normal per-entity verdict publish; seeding itself publishes nothing (T-3 pinned).
- **G-3 (stretch needs an arch breach):** **TRIPPED AS DESIGNED → floor only + OBS-1** (the stretch memo in §7); no rule edits, no breaking schema.
- **G-4 (DP-3 ruling absent):** NOT TRIPPED — the ruling (STOP) rode the dispatch line; Branch STOP executed.
- **G-5 (pin drift):** NOT TRIPPED — §1: all pins exact at `4288a9d`.

## §6 — Deviations (severity-honest: ZERO [REVIEW] — eight [INFO] + three OBS)

- **[INFO] D-1 — two lifecycle test-tree entries in the census** (RestartHonestyIT M + AvailabilityBootTruthIT ??): sanctioned by the instruction's own §7 clause ("nothing outside integration-zigbee unless the DP-2 floor demands a projection/read-path touch WITHIN arch law — name it"); both are TEST-ONLY. Named and reasoned in §4.
- **[INFO] D-2 — RestartHonestyIT's re-link barrier reworked, green at BOTH ends:** its `:111` `awaitTrue(countEventsOfType(AVAILABILITY_CHANGED) >= 1)` used the L1 emission as a sync barrier (and was near-vacuous — the boot-1 adoption seed already satisfied ≥1 before the restart). Replaced with a logback capture awaiting `zigbee.device_relinked` ≥2 (one DP-6 rehydration relink + one announce-driven LINKED relink — deterministic arithmetic for its one-device fixture; the slice logger addressed by name, the class being package-private). Baseline-compatible by design (the log line predates this WU), so this edit has no red of its own; the WU's T-5 teeth live in the three inverted pins and the adapter leg.
- **[INFO] D-3 — the superseded test deleted:** `restartWithPersistedSidecar_firstFrameStillEdges` pinned the pre-seed contract (the MODULE_CONTEXT trap gotcha named it as the tripwire for exactly this WU's change); formally replaced by the T-6 quiet-boot leg; the gotcha rewritten with a SUPERSEDED marker (in-census MODULE_CONTEXT edit).
- **[INFO] D-4 — the evidence guard is spec-plus within DP-1's sanction:** `isEvidencedAvailable` + the `seedFreshAdoption` gate swap close the one remaining evidence-free-"online" manufacture path (a sidecar-seeded available reaching the M9.6 adoption-time view seed). Behavior-preserving for every evidenced flow (pre-seed, evidenced ≡ available); unit- and adapter-pinned.
- **[INFO] D-5 — malformed `lastEvidenceAt` VALUES degrade per-device with ONE WARN** (`zigbee.evidence_recency_malformed`, the learnedZoneTypes posture) rather than riding the whole-cache corrupt discard: the compat mandate covered only absence; a value-level parse failure inside the additive field should not cost the whole warm cache. Test-pinned (sibling survives, count-1 WARN).
- **[INFO] D-6 — the T-2 boundary leg (`seededFreshBattery_firstCycleQuiet`) was red at baseline for the L1 reason** (the rehydration relink burst tripping its any-grain zero-count), not its own boundary reason; post-fix its tooth is the over-fire regression. Disclosed rather than re-staged.
- **[INFO] D-7 — the ping outcome realized as a private 3-value enum** (`ok|timeout|error` — the DP-5(b) vocabulary): `error` = the unresolvable-candidate arm (`pingBasic`'s no-record/sentinel-address early return), `timeout` = wire silence; both record `responded=false` exactly as before (the M9.6 honest-unreachable semantics preserved; the NCP-deaf `EzspCommandTimeoutException` still propagates to the watchdog, never device evidence).
- **[INFO] D-8 — the rig (testFixtures) gained `silence(long)`** — the dead-device simulation T-7 needs (the rig's scripted NCP otherwise answers every Basic read); SRSP acceptance preserved (the radio is healthy, the device is dead); in-module, public-to-tests-by-design like the rest of the rig surface.
- **OBS-1 (the DP-2 stretch memo — for the hub):** see §7.
- **OBS-2 (the registry-loss corner):** a seeded-available-unevidenced device adopted WITHOUT an announce (registry lost, sidecar survived, direct adopt) gets no adoption seed and its frames confirm silently — its fresh entities sit honest-UNKNOWN until an offline/online cycle or the normal announce-driven re-adopt (which converges). Production adoption is always announce-preceded (= evidence), so the corner is test-only; pinned by the evidence-guard leg and documented in MODULE_CONTEXT.
- **OBS-3 (`previousStatus` on seed-originated verdicts):** reads `"unknown"` (the listener's process-local memory — M9.6 mechanics deliberately untouched) while the served view held the replayed prior state. Cosmetic event-record nuance; `newStatus` is what the projection applies; test-pinned so it is deliberate, not drift. If the hub ever wants previousStatus to mirror the seeded prior, that is a one-line listener-init decision — not taken unilaterally here.

## §7 — The DP-2 mechanism memo

**Built (the floor):** seed-driven convergence over the UNTOUCHED normal path. The seeded tracker holds the sidecar truth; the served view holds the log's replayed truth; the two mirror each other by construction because both were written by the same transition path (`EntityAvailabilityPublisher.onTransition` = publish + `setAvailability`, atomically the same events). Convergence for a dead device: mains — the seed makes it evaluable from cycle 1, persisted staleness (or unknown recency) makes it a ping candidate, the ping fails, PING_TIMEOUT publishes per relinked entity (rehydration populated `entitiesFor` at initialize), the projection applies at `StateProjection:856`, and `StateQueryService.materialized`/`ListEntitiesEndpoint` serve UNAVAILABLE — within one 10-min window of boot (T-7 proves it end-to-end at the composition root on the real `HomeSynapseCore`, reusing: the RestartHonestyIT boot/restart harness shape, `ZigbeeHardwareFreeRig` + `restartIntegration`, and the production `stateQueryService()` — the same materialized instance HomeSynapseCore wires into the REST endpoints at :928/:935; the HTTP hop above it is serialization only, covered by rest-api's own endpoint tests). Battery — the persisted clock makes the 25 h verdict fireable across restarts (T-2).

**Rejected (per instruction):** per-boot per-device event floods (G-2 — seeding publishes nothing; the boot stays event-quiet unless an honest verdict is due); any read-path mechanism needing an arch exemption (G-3).

**The stretch (OBS-1 — design sketch, not built):** the read surface's `stale` field derives at READ time in `MaterializedStateQueryService.recomputeStale` (:221–:236: `staleAfter != null && clock.instant().isAfter(staleAfter)`), from `EntityState.staleAfter` — a per-entity reporting-cadence contract fed only through the projection (EntityState.java:54–:59; the availability-apply branch at StateProjection:857–:866 deliberately preserves `prior.stale()`). "Seeded-not-yet-evidenced" is adapter-private knowledge that lawfully cannot reach that derivation: seeding publishes nothing (T-3), so no event carries it; a new event type is G-1; a rest→integration read is the G-3 breach. Honest realizations would be (a) a new additive read-side field derived from a first-class "boot epoch" concept (needs a ruling + likely an event), or (b) an integration-owned staleness hint riding a future health surface. Both are hub-scope; the floor stands alone without them.

## §8 — Next-WU pointer (refuse-to-close)

**The hub's two-layer audit precedes ANY commit** (this return + the coder-handoff DELIVERED entry are the audit inputs; ZERO [REVIEW] — eight [INFO] + three OBS ride it). The lane commits NOTHING; staging at the hub's order = exactly the §4 census (13 paths). CI on the pushed commit remains the gate of record. **Post-deploy:** the attended F2 rep proves BOTH directions on the FIXED build before Aug-10 — and gives the mains ping arm its first live exercise (L3 was never broken, only unexercised; DP-5(b) now makes every ping grep-visible for that rep) — pairing with the B3 §10 rejoin-race rep per the instruction. Per the dispatch entry: nothing else dispatches from this lane while AVAIL-SEED is in flight; the FE redeploy (charge 4) stays hub/operator-owned in parallel; the small-fix stack (STATE-DIALECT core P2 + FE-LIVE-V112 (f)/(g)) queues behind this audit.
