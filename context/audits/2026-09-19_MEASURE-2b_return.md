<!--
file: context/audits/2026-09-19_MEASURE-2b_return.md
purpose: the Coder's return for MEASURE-2b (the read path at run-scale; the shared fixture; row 0; the rig sweep)
status: filed Sat 2026-09-19 evening CT — `date -u` first: 23:14:02Z (18:14 CT); baseline core `d1c2cbc`, porcelain EMPTY at 23:14:09Z; ZERO commits by the lane
-->

# MEASURE-2b — return

## §0 Card
**DELIVERED, uncommitted. Census EXACT — 12 = 9 M + 3 A:** core 8 M + 2 A (rows 1–9 + `ZigbeeAdoptionSliceTest.java`, T1's home); hivemind 1 M + 1 A (rows 10–11) beside the hub's own dirty beat (5 M + 4 `??` at dispatch).
**Sort:** RED→GREEN T1, T2 (+ T1b, T2b) · GREEN at baseline, disclosed: T3 (predicted RED), T4, T5, T6 (24 of 25; T2 re-pins one) · MEASUREMENT: T7.
**Gate line, verbatim, ONE round — GREEN:** 23:38:10Z→:41Z `BUILD SUCCESSFUL in 30s · 112 actionable tasks: 8 executed, 104 up-to-date` (`_scratch/v77/…_gate.log`); three test tasks EXECUTED, XML mtimes 18:38:32–:40 CT: lifecycle 82 · zigbee 663 (1 skip) · app 30 · 0 red; T7's smoke 5.5 s. **It does not run T4** (`bus-soak` tag): T4 + T5 ran by the MODULE_CONTEXT's line, 23:37:43Z — `bus.soak: loops=20 ok=20 timed_out=0 … anomalies=0`, `missed=0`, Hero 5/5.
**Measurement** — median ms, warm (k=5) / cold (k=1); `_scratch/v77/2026-09-19_MEASURE-2b_readpath.txt` = the `<system-out>` of `…_readpath_junit.xml`:
| rows · runs | q1 explainRun | q2 nonFiring | q3 chain | q4 listRuns | q5 listAutom. | q6 state | restart ms |
|---|---|---|---|---|---|---|---|
| 10,013 · 10 | 1.769 / 2.933 | 0.356 / 0.438 | 0.111 / 0.134 | 0.151 / 0.169 | 0.153 / 0.289 | 0.112 / 0.316 | 161 |
| 100,013 · 100 | 10.633 / 17.832 | 0.852 / 1.204 | 0.084 / 0.187 | 0.526 / 0.596 | 0.504 / 0.680 | 0.144 / 0.239 | 545 |
| 242,999 · 242 (the 500k, CAPPED) | 42.267 / 47.918 | 1.055 / 3.191 | 0.084 / 0.171 | 0.915 / 1.191 | 0.948 / 1.437 | 0.123 / 0.236 | 924 |
| 500,013 · 500 (supplementary: a TRUE 500k) | 90.481 / 93.985 | 4.228 / 4.113 | 0.111 / 0.152 | 3.225 / 3.523 | 3.401 / 3.542 | 0.194 / 0.241 | 1611 |
**P1 MISSED** — 12, not 11: T1's home (row 7's own branch) has no row; and the table's column sums to 8 M + 3 A, not "9 M + 2 A". **P2 MET** 0 · 0 · 1 · 1. **P3 MISSED on T3** (§2). **P4 MET** 478.0 / 469.9 / 469.2 rows/s vs 24,031.1 — production's derived-write bucket (200/s), not fsync. **P5 (a) MISSED** — q1 grows with N: 1.769 → 10.633 → 42.267 → 90.481 ms at 10k / 100k / 243k / 500k (×51; the bound was 3×) — F-2. **(b) MET in direction** — q2 0.356 → 0.852 → 1.055 → 4.228 ms over 10 → 100 → 242 → 500 runs, the last step ×4.0 for ×2.1 the runs; runs ∝ N here, so flat-in-reports rests on q3. **P6 MET** — 512.8 B/row at 243k, 503.4 at 500k, the WAL's share in (the db file ~494; the 10k's 916.3 is the WAL). **P7 MET** — 924 ms at 243k, 1611 ms at 500k.
**Two read-path defects found, neither fixed (§4):** F-1 a restart makes `explainNonFiring` say `NEVER_TRIGGERED` of an automation that fired; F-2 q1 is O(N). **Deviations:** 9 [REVIEW] · 6 [INFO]. **Rig-blindness (§11):** 8 shared surfaces, 8 blind inside the rig, 1 without an independent instrument; the four helpers the charter named are NOT shared. **Deferred Build Gate:** `./gradlew check` owed to CI. **NEXT WU: LINK-READ.**

## §1 R1 — the two `bootAndAdopt` bodies, diffed first (`BusSoakIT:309` vs `HeroLoopHardwareFreeIT:383`)
They differ in the config (now the `configYaml` parameter), Hero's assertion that the composed schema contains `zigbee`, and Hero's two 15000 ms CT-override assertions. **The fixture took Hero's form:** the three assertions moved VERBATIM (Hero −3 `assertThat`, fixture +3 — they now run for BusSoak and T7 too); the timeout is Hero's, its head from `latestPosition()`; the barrier await keeps BusSoak's named position. **A THIRD copy exists** — `BusPositionCensusIT.java:137/:658`, byte-identical to BusSoak's (§6's grep, "these six lines", returns ten). Outside the Files table → untouched: `IR-41 | BusPositionCensusIT | the third boot copy | one row onto the fixture`.

## §2 Red-first (RED-1 23:24:53Z: 44 run / 4 red → GREEN-1 23:25:59Z; XML banked `_scratch/v77/…RED1_*.xml`)
| Test | Predicted | Observed at `d1c2cbc` |
|---|---|---|
| T1 `adoptLogsEndpointClassifiedWithDevice` (+ T1b) | RED | RED — `Expecting actual: [] to contain exactly ["zigbee.endpoint_classified: device=0x…"]` |
| T2 `meteringOnlyEndpoint_energyMeterWithEnergyMeterOnly` (+ T2b) | RED | RED — `expected: ENERGY_METER but was: SENSOR` |
| T3 `electricalOnlyEndpoint_sensorWithPowerMeterOnly` | RED | **GREEN** — `.orElse(SENSOR)` already answers it; pinned since ENERGY-READ |
T2 is a RE-PIN in the open: ENERGY-READ's `meteringOnlyEndpoint_sensorWithEnergyMeterOnly` asserted SENSOR for T2's exact signature; renamed, its assertion replaced.

## §3 The measurement (23:39:03Z→23:53:45Z, the charter's command verbatim; XML: 1 test · 0 failures · 879.962 s)
```
MEASURE2B knob=10000,100000,500000 sha=d1c2cbc clock_step_ms=1000 k=5 profile=testing seed_cap_min=10
MEASURE2B rows=10013 runs=10 seed_events_per_s=478.0 db_bytes=4952064 wal_bytes=4190072 shm_bytes=32768 bytes_per_row=916.3 q1_ms=1.286/1.769/4.936 q2_ms=0.324/0.356/2.381 q3_ms=0.093/0.111/0.204 q4_ms=0.135/0.151/0.283 q5_ms=0.135/0.153/0.796 q6_ms=0.107/0.112/0.599 restart_ms=161 q1_cold_ms=2.933 q2_cold_ms=0.438 q3_cold_ms=0.134 q4_cold_ms=0.169 q5_cold_ms=0.289 q6_cold_ms=0.316 target=10000 reports=4938 seed_wall_s=20.663 clock_end=2026-01-01T00:01:00Z entities=3 q2_verdict=FIRED_CONFIRMED/NEVER_TRIGGERED hero_id_stable=false capped=false
MEASURE2B rows=100013 runs=100 seed_events_per_s=469.9 db_bytes=49360896 wal_bytes=4276592 shm_bytes=32768 bytes_per_row=536.6 q1_ms=10.405/10.633/17.374 q2_ms=0.765/0.852/1.623 q3_ms=0.075/0.084/0.112 q4_ms=0.483/0.526/0.564 q5_ms=0.474/0.504/0.684 q6_ms=0.102/0.144/0.225 restart_ms=545 q1_cold_ms=17.832 q2_cold_ms=1.204 q3_cold_ms=0.187 q4_cold_ms=0.596 q5_cold_ms=0.680 q6_cold_ms=0.239 target=100000 reports=49398 seed_wall_s=210.264 clock_end=2026-01-01T00:10:00Z entities=3 q2_verdict=FIRED_CONFIRMED/NEVER_TRIGGERED hero_id_stable=false capped=false
MEASURE2B rows=242999 runs=242 seed_events_per_s=469.2 db_bytes=120246272 wal_bytes=4334272 shm_bytes=32768 bytes_per_row=512.8 q1_ms=39.406/42.267/47.503 q2_ms=1.025/1.055/2.336 q3_ms=0.080/0.084/0.115 q4_ms=0.853/0.915/1.344 q5_ms=0.867/0.948/1.087 q6_ms=0.113/0.123/0.224 restart_ms=924 q1_cold_ms=47.918 q2_cold_ms=3.191 q3_cold_ms=0.171 q4_cold_ms=1.191 q5_cold_ms=1.437 q6_cold_ms=0.236 target=500000 reports=120039 seed_wall_s=511.673 clock_end=2026-01-01T00:24:17Z entities=3 q2_verdict=FIRED_CONFIRMED/NEVER_TRIGGERED hero_id_stable=false capped=true
```
**The cap:** 500k did not complete in 10 minutes → `rows=242999 capped=true` (§9's rule; F-3). **Supplementary, never the record** (same tree; banked): `…_readpath_true-500k.txt`, `SEED_CAP_MIN=45` — `rows=500013 runs=500 capped=false`, 1053.460 s of seeding at 468.9 rows/s: the card's fourth row. `…_readpath_frozen-clock.txt`, `CLOCK_STEP_MS=0` — q1 = 36.770 ms at 10k and 640.932 ms at 100k (stepped: 1.769 / 10.633), every other read unchanged: the literal seed would have filed the rig, ×21–×60. **The clock at the end of seeding** (`clock_end=`): 00:01:00Z / 00:10:00Z / 00:24:17Z from `TestClock`'s 00:00:00Z — 1 s per pumped batch; nothing else moves it.

## §4 Findings (R8 — numbers, no fix)
**F-1 — a restart orphans the run history from its automation.** `HomeSynapseCore.java:677` wires `InMemoryAutomationIdentityStore`: each boot mints a NEW `AutomationId` per slug (AMD-93 §2.3's file store is pending). Every line reads `q2_verdict=FIRED_CONFIRMED/NEVER_TRIGGERED hero_id_stable=false`: after one restart the non-firing hero says "has not been triggered" of an automation with 10–500 confirmed runs in the log. One restart inside the 72-hour run files a false verdict: `IR-39 | automation identity | re-minted per boot | a restart IT asserting the id by slug`.
**F-2 — `explainRun` is O(N): its hint read is a rowid walk.** `EXPLAIN QUERY PLAN` of `SqliteEventStore.java:221–:226` through the shipped driver (sqlite-jdbc 3.51.3.0; scratch JDBC on a copy of the 100k store) → `SEARCH events USING INTEGER PRIMARY KEY (rowid>?)`, 203 window rows in 18.6 ms; python's SQLite 3.45.3 on the same file picks `idx_events_event_time` + a temp b-tree, 0.47 ms. So `StandardExplanationService.java:1113`'s "a hit costs O(events in one minute)" is false as shipped: the cost is the rows BEFORE the window. `IR-40 | readByTimeRange | the plan | q1 across N + the plan read through the shipped driver`.
**F-3 — the seed measures production's pacing (no defect).** A report lands as two rows, the second a derived write behind `DerivedWriteRateLimit` (AMD-43 §3.6.4: 200/s); the dedup (an unchanged payload on a consecutive TSN inside 10 s) forces the alternation.

## §5 Deviations by tag
**[REVIEW]** R-a the seed ADVANCES the clock (1 s per pumped batch; a knob, `0` = frozen): §9 asked only what it read; frozen, q1 measures the rig (§3). · R-b the Gen4 adopts by CONFIG (`integrations.zigbee.adopt_devices`; `withGen4AcceptListed`): `rig.adopt` never runs the formatting reads (only `ZigbeeIntegrationAdapter.adoptIfAccepted` :1012 does) and without them 0x0B04 emits nothing; R2's verify step caught it. FORESIGHT: a REST adopt path that calls the slice adopts meters silent. · R-c T1 lives in `ZigbeeAdoptionSliceTest.java` (row 7's own branch: `sliceLogCapture` :66) — the 12th file. · R-d P3/T3, the T2 re-pin (§2). · R-e the gate line cannot run T4 (conventions :57–:61). · R-f the third boot copy (§1). · R-g the classifier's R6 line is KEPT at INFO (it alone carries `deviceType=`/`inputClusters=`, Thursday's G4-3 instrument): two same-token INFO lines per classified endpoint; the alternative is one six-field slice line, the classifier's at DEBUG. · R-h §13 names a `coder-handoff.md` entry, §0/§3 say "nothing else": the table governed; its text is in §12. · R-i the 500k cap (§3).
**[INFO]** the fixture's timed methods take the caller's `LongSupplier` (§9's "nowhere else" vs a fixture that returns nanos) and a `Duration` step; added `settle()` `walBytes()` `shmBytes()`, two ENV knobs. · one pulse per 1,000 ROWS (a report is two rows); `pulseMotion()` is a whole CONFIRMED loop. · q6 omits the endpoint's `viewPositionSupplier` long. · BusSoak's BOOT-phase timeout loses head/tail + the census line; `BusPositionCensusIT:725`'s javadoc pointer is stale. · q2's `0L` = since the beginning, the widest walk. · profile TESTING (cache 2 MB, mmap 32 MB, one read thread; HOME 16/256/two): the desk's numbers, not the Pi's; cold = new connections, OS cache + JIT warm.

## §11 The rig-blindness sweep (the rig, `FakeNcp`; no code)
**The premise, corrected.** `wireType` :637 · `wireValue` :656 · `attributeRecord` :681 · `report` :617 are the rig's OWN private statics; production decodes with `ZclCodec.parseAttributeReports` :92 / `parseReadAttributesResponse` :123 — two implementations, so a production defect SHOWS: not blind. (The uint48 blindness was `ZigbeeReportingDriveTest`'s store mirroring HEAD's `int` shift; pinned at :563/:617 now.) Their limit is fidelity.
**Shared: 8 surfaces (production side: AshSession :130/:352/:420/:421, the protocol, the codecs, the handlers), all symmetric-blind INSIDE the rig; 7 carry an independent instrument, 1 none.**
| Shared | Rig site | Independent instrument |
|---|---|---|
| `AshCodec.parse` / `.emit` (2) | FakeNcp :91/:99/:112/:124 | `AshCodecTest` vectors; bench |
| `AshFrameAccumulator.accept` | FakeNcp :90 | `AshSessionTest` :134/:370/:387 |
| EZSP frame + profile ids | rig :172/:331/:340/:350/:714 · FakeNcp :165–:177 | literals in 6 tests; bench |
| `ZdoCodec.CLUSTER_*` | rig :173/:535–:548 | `ZdoCodecTest`; bench |
| `ZclCodec` read ids | rig :428/:432 | `"b04:0"` send-order strings; bench |
| metering attribute ids | rig :499–:524 | literal lists: `ElectricalMeasurementHandlerTest:205`, `MeteringHandlerTest:204` |
| **`EzspReportingOps.*`** — Bind 0x0021/0x8021, response ids 0x07/0x09, statuses 0x86/0x8C, direction | rig :376–:383/:439–:481 | **NONE hardware-free**: the drive test's NCP (:889–:1010) and assertions use the same constants; only request ids are literal |
**Register rows** (next free after IR-35; the hub renumbers): `IR-36 | EzspReportingOps wire constants | every hardware-free instrument replies from the constants under test | one literal-bytes test` · `IR-37 | the rig's encoders | unpinned, author-shaped | captured frames as fixtures` · `IR-38 | the ITs' frozen TestClock | a time window is the whole log or none | the fixture's clock step (§3)`.

## §12 Closeout (WUCP Phase 1)
- [x] tests first, red for the stated reason, then green; the gate verbatim, one round, `-Werror` clean; freshness proven; census exact; nothing staged
- [x] both `MODULE_CONTEXT.md` by exact-once insert (zigbee `(1b)`; lifecycle `### MEASURE-2b` + gotcha 13); the record: M2-2b filled, M2b-1..6 new (`status:` left to the hub)
- [x] INV/LTD read at source, no discrepancy: LTD-17 · INV-SUB-ISO-02 / AMD-26/27 · AMD-44 · LTD-11 · `NO_DIRECT_TIME_ACCESS` (one `System.nanoTime()`, `MeasureReadPathIT.stopwatchNanos`)
- [x] **the `coder-handoff.md` entry, for the hub to file (R-h):** `MEASURE-2b DELIVERED 2026-09-19, uncommitted 12 = 9 M + 3 A on d1c2cbc — RealCoreFixture exists (the boot shape of three ITs); medians ms at 10k/100k/500k: q1 1.8/10.6/90.5 (O(N)) · q2 0.4/0.9/4.2 · q3 0.1 · q4 0.2/0.5/3.2 · q5 0.2/0.5/3.4 · q6 0.1–0.2 · restart 161/545/1611; F-1, F-2 open; Deferred Build Gate: check owed to CI; NEXT: LINK-READ.`
- Lesson (file outside the write-set): read a planner claim with `EXPLAIN QUERY PLAN` through the SHIPPED driver.
RETURNED nexsys-hivemind/context/audits/2026-09-19_MEASURE-2b_return.md 13995
