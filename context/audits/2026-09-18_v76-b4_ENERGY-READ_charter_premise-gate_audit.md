<!--
file: context/audits/2026-09-18_v76-b4_ENERGY-READ_charter_premise-gate_audit.md
purpose: THE v76 BEAT-4 AUDIT — ENERGY-READ chartered through THE PREMISE GATE: every `file:line`, "exists" and mechanism claim in the instruction's premise table grepped at core `3af6213` this beat (the commands and their hit counts below); the design's four load-bearing choices and their refutable-by; the sized decision's arithmetic checked; Nick's eight additions ruled (the plan §16); THE MEASUREMENT RECORD minted; the words banked; `7605dfc` verified.
audience: the hub (the record) · Nick (§0)
state-type: charter audit + gate record
status: FILED v76 beat 4 (Fri 2026-09-18 ~1x:xx CT)
-->

# v76 beat 4 — ENERGY-READ through the gate

## §0 Card
- **`HIVE: LANDED 7605dfc`** verified: 10 at diff-tree (7 M + 3 A); porcelain 0; push 0. The other four HEADs unmoved.
- **Words:** `PILOT: after` (D-v76-9 RULED — a hardware ruling) · `EXPORT: letters` (given → a Nick act in the advisory session → `LETTERS: RETURNED <path> <bytes>`) · `PROTECT:` still owed — the word is `PROTECT: done` once the six clicks are made (§5).
- **ENERGY-READ DISPATCH-READY** — the window's deliverable half met: `context/instructions/2026-09-18_coder-lane_ENERGY-READ_metering-by-clusters_divisors-at-adoption_scaled-reporting_coding-instruction.md` (42,144 B; 23 Files-table rows; the return cap 26 KB by arithmetic; the gate line's task paths read from `settings.gradle.kts`). Nick's paste is §14.
- **The four load-bearing design choices:** (i) the formatting is READ at adoption on the reporting drive, not at the interview — an unadopted device is never asked, THE ADOPTION FENCE keeps its meaning, and the interview's frozen types are untouched (refutable-by: a Coder reason to read earlier); (ii) a handler with no formatting is NOT constructed — a metering report with unknown scale is silence plus one debug, never a guessed divisor (Nick's "the divisor VALUE read at the first read, no prediction"); (iii) the reportable change is configured in engineering units scaled by the read divisor — 1 W / 5–600 s and 5 Wh / 5–3600 s — with the predicted frames/h per divisor stated in the instruction's §1 table (fold 1); (iv) the raw value rides beside every scaled value (`rawProtocolValue`/`rawProtocolUnit`) — the provenance law applied at the source.
- **The sized decision, checked:** 0x0702 at 80 W — 5 raw at divisor 1e6 = 5 mWh accrues in 0.225 s (5e-3 Wh ÷ 80 W = 6.25e-5 h = 0.225 s) → the 5-s floor → 720/h; at 1,000 → 5 Wh every 225 s → 16/h; at 3.6e6 → 5 Ws in 0.0625 s → 720/h. After: 5 Wh at any divisor → 16/h. 0x0B04: 10 raw at divisor 100 = 0.1 W under a 0.32 W noise band → 720/h; after: 1 W → edges. Three plugs × 72 h: BEFORE 155,520–311,040; AFTER ≈ 3,456 + edges. The arithmetic in the instruction matches Nick's brief §4 and the b2 audit.
- **The eight additions:** ruled in the plan §16 — the watts go/no-go dated Sun 2026-10-11 20:00 CT; VERIFY-72H's two dated gates and its frozen invariant list (IR-30's case flagged); IR-31's `derived` provenance; the run's log retained and indexed under the bench corpus; the buyer outreach from Fri 09-25 behind the register-checked script; THE SPOKEN CARD's embargo side; VERDICT-VOCAB-1's two policy lines. None costs the window.
- **THE MEASUREMENT RECORD minted:** `context/planning/measurement-record.md` — rows M2-1..3 (MEASURE-2), G4-1..3 (the Gen4's formatting and type at the first adoption), CHAR-1..3, REP-1; a value is written once from an instrument, never edited.
- **The ONE act:** the packet — block 1 the ENERGY-READ dispatch paste; block 2 the b4 hivemind card.

## §1 The premise table at `3af6213` — the greps as run (this beat, from the device VM)
| Claim | Command | Result |
|---|---|---|
| `DEVICE_TYPE_SMART_PLUG = 0x0051` at `:41`; the SMART_PLUG arm `:99–:101`; the default → fallback `:102–:103`; `binarySensor` `:150–:165`; `iasCapability` `:175–:178`; `fallback` `:180–:186` | `sed -n '41p;91,104p;150,165p;175,178p;180,186p' EndpointClassifier.java` | as cited (the b2 audit §6 read the same lines) |
| no metering cluster consulted by the classifier | `grep -c '0x0B04\|0x0702\|0x0b04' EndpointClassifier.java` | 0 |
| eight handlers, no metering | `sed -n '30,60p' ClusterHandlers.java`; `grep -c 'ElectricalMeasurement\|Metering' ClusterHandlers.java` | eight `Map.of` entries; 0 |
| `forDevice` has one production caller | `grep -rn 'forDevice(' zigbee/*.java` | the declaration + `ZclIngestionUnit.java:731` |
| the classifier has one production call site | `grep -rn 'EndpointClassifier\.' zigbee/*.java` | `ZigbeeAdoptionSlice.java:377–:378` |
| `IasZoneHandler` emits `active` for the three zone types | `grep -n 'case ' IasZoneHandler.java` | `:75 MOTION → "detected"`, `:76 CONTACT → "open"`, `:77 WATER_LEAK, SMOKE, VIBRATION → "active"` |
| `ZoneType` has five values | `grep -n '^\s*[A-Z_]\+(' ZoneType.java` | `:23–:35` MOTION, CONTACT, WATER_LEAK, SMOKE, VIBRATION |
| the capabilities exist with the keys | `grep -n 'public static' StandardCapabilities.java`; `sed -n '312,331p;332,349p;451,500p'` | `powerMeasurement` :312, `binaryState` :332 (`active`), `energyMeter` :451 (`energy_wh`, `reset_meter`, EXACT_MATCH), `powerMeter` :481 (`power_w`, `voltage_v`, `current_a`) |
| `ReportingOps` has no attribute read | `grep -c 'readAttributes' ReportingOps.java`; `grep -n 'boolean \|Optional<' ReportingOps.java` | 0; `bind` :54, `readReportingConfiguration` :83, `writeCieAddress` :94 |
| `readBasic` is a synchronous unicast + await | `sed -n '1990,2010p' EzspCoordinatorProtocol.java` | `encodeReadAttributes` → `sendUnicastLocked` → `awaitIncomingLocked` |
| the codec decodes uint24/uint48/int16/enum8, not int24 | `grep -n 'case 0x2' ZclCodec.java` | `:199` 0x22, `:201` 0x25, `:203` 0x29, `:204` 0x2B; no 0x2A |
| DEFAULTS' two raw rows; the skip; the per-cluster configure | `grep -n 'DEFAULTS\|0x0B04\|0x0702\|SKIP_CONFIGURE' ReportingConfigurator.java`; `sed -n '95,170p'` | `:57`, `:63–:72` (`:71`, `:72`), `:102–:104`, `:110–:113`, `:125–:126`, `:131–:136` |
| the adoption drive and its order | `sed -n '960,1030p' ZigbeeIntegrationAdapter.java`; `grep -n 'private void adoptIfAccepted\|private void driveReporting\|adoption.adopt(interview\|reporting.configureDevice(ieee'` | `:979`, `:995`, `:1009`, `:1015` |
| the onAdopted listener invalidates handlers | `sed -n '380,420p' ZigbeeIntegrationAdapter.java` | `:406–:409` |
| the cache's learned-zone pattern | `grep -n 'learnedZoneType\|recordLearned\|void ' ZigbeeDeviceCache.java` | `:84`, `:291–:296`, `:308–:311`, `:364`, `:392` |
| the ingestion's dispatch, the unhandled branch, the unadopted guard, `invalidateHandlers`, `handlersFor` | `sed -n '520,560p;586,600p' ZclIngestionUnit.java`; `grep -n 'void invalidateHandlers\|handlersFor(\|ZclIngestionUnit('` | `:521–:545`, `:540`, `:586–:593`; `:724`, `:729`; the constructors `:209`, `:244` |
| the interview reads no metering attribute | `sed -n '52,60p' InterviewStateMachine.java`; `grep -n readBasic` | `Step` :52–:57; `:160–:167` |
| the test harness | `grep -n '@Test\|FakeNcp' ZigbeeReportingDriveTest.java`; `grep -n 'public ' ZigbeeHardwareFreeRig.java` | `FakeNcp` :162; the rig's `announce` :121, `report*` :137–:156, `silence` :169, `deliverAndCycle` :178, `adopt` :189, `sentZclFrames` :194 |
| one `ReportingOps` implementation + one fake; no shape test; no ArchUnit rule names zigbee; the app test task exists | `grep -rln 'implements ReportingOps\|new ReportingOps()' src`; `grep -rl 'getDeclaredMethods().length' src/test`; `grep -c zigbee HomeSynapseArchRules.java`; `grep -n homesynapse-app settings.gradle.kts` | `EzspReportingOps.java`, `ReportingConfiguratorTest.java`; 0; 0; `:63 include("app:homesynapse-app")` |
| the record's signature and divisor rows | `grep -n '0x010A\|divisor' PLUG-DOSSIER_return.md`; `sed -n '39,47p' DEVICE-SET_return.md` | row 16 (the feature matrix), row 18 (ZHA), row 29 (the TR3's z2m override); notes 1–4 |
The external constants (the ZCL attribute ids) are embedded with their source and marked for the Coder's independent re-derivation (format law #4); they are not grepped in the tree because the tree does not carry them yet.

## §2 Against the record
Doc 08 §3.5 (the smart plug → `switch`) stands: the meters ride beside `on_off`, the entity type unchanged. Doc 02's 16 capabilities: none added. LTD-17: no new `requires`. The read-API freeze: untouched — the attribute keys are the device model's and the state read is generic; the mirror's labels are FE-116's. THE ADOPTION FENCE: the lane runs on the desk; the first plug adoption is Thu 09-24's CHAR session only if the landing is green (D-v76-1).

## §3 What the hub could not re-execute (disclosed)
The ZCL attribute ids against the specification document itself (embedded from the record's corroborations and the hub's reading of the standard; the Coder re-derives before pinning); the Gen4's live signature at firmware 2.0.0 (G4-3, the first adoption); whether the rig's factory can be pointed at a SQLite temp store for M2-2 (the Coder discloses the store used).

## §4 The beat order re-cut
b5 charters the bench lane (`metering-known-load.yaml` with CHAR and the two chains; `field_within`; the `link-quality.yaml` skeleton); Saturday silent; b6 Sunday's intakes; b7 VERDICT-VOCAB-1 + rehearsal 1's packet; the window closes ≤ b8 with the rest in v77's §HELD.

## §5 `PROTECT` — the act as the record reads it
For `homesynapse-core` and `homesynapse-core-docs` on GitHub: Settings → Branches (or Rules) → a rule on `main` → block force pushes · block deletions → save — three clicks per repo, six in all (v69 b1: "handed in chat"; `PROTECT: core + docs`, `PROTECT: no-force`). The word when done: `PROTECT: done`.
