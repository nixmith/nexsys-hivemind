<!--
file: context/assessments/2026-06-26_converter-db-embed-pipeline-design.md
purpose: SESSION V2-B return — the concrete embed-pipeline design for leveraging the Z2M `zigbee-herdsman-converters` declarative data (`zigbeeModel`/`fingerprint` + `exposes`) as attributed, version-pinned input to HomeSynapse's ZCL-aligned device/capability model. Operationalizes §1 D5 (RATIFIED 2026-06-26: adapt-the-data declarative core + curated-subset/community fallback) so M9 builds device breadth against a KNOWN pipeline, not ad-hoc. Frames the LOW-risk legal spot-check into a counsel-ready list. Design + recommendation; NO production code. The hub folds the M9-gating verdict into M9 scoping and routes the counsel list to Nick.
audience: PM (v6 hub), Nick, the M9 Zigbee lane, the Distribution pairing-wizard lane, counsel (for §legal list).
state-type: assessment (dispatched-session return — write-isolated per the 2026-06-26 v2 fan-out brief; this session writes ONLY this file)
status: RETURNED 2026-06-26.
sources-discipline: design grounded in the project's own Locked design docs (Doc 02 §3.5–§3.12, Doc 08 §3.5–§3.9) + the ratified D5 record + Session A's file-level license reads (primary sources cited inline). FACT vs INFERENCE flagged throughout. Real-silicon confirmation of the two worked mappings rides Session C (bench). This is engineering due diligence, NOT a legal opinion and NOT a strategic ruling. Counsel must rule the §legal items.
-->

# Session V2-B — Converter-DB Embed-Pipeline Design

## One-paragraph recommendation — CONFIDENCE: HIGH on pipeline shape, MEDIUM-HIGH on transform-modesty, HIGH on provenance discipline

**Build the embed as an offline, human-gated, version-pinned "ingest → normalize → map → emit" pipeline whose emit target is the device-model artifact HomeSynapse already specifies — the Doc 08 §3.6 `DeviceProfile` registry (the bundled `zigbee-profiles.json`) plus the Doc 02 §3.6 capability rows — so the runtime loads an attributed dataset, never the upstream code and never a live dependency.** The pipeline cleaves exactly along the line D5 ratified: the **standard-ZCL majority** (lights, switches, plugs, contact/motion/temp/humidity/illuminance/power sensors — Doc 08 §3.6 categories C/D, ~60% of devices) ingests `zigbeeModel`/`fingerprint` (→ device identity) + `exposes` (→ Doc 02 §3.6 standard capabilities) as **pure data values** via a deterministic, rules-driven transform that requires no porting of upstream logic; the **code-shaped tail** (`fromZigbee`/`toZigbee`, Tuya `0xEF00`, Xiaomi/Aqara TLV — categories A/B, ~40%) is **not transcribed** — it is independently re-expressed as Doc 08 §3.8/§3.9 codecs + Doc 02 §3.9 `CustomCapability` rows, using upstream as a behavioral *reference/cross-check*, and is delivered through the **curated-subset + community path** rather than the bulk embed. Provenance discipline: **a consolidated `NOTICE`/attributions artifact (recommended over per-file headers)** built mechanically from the ingest manifest, carrying the **pinned upstream commit + version + license-at-ingest** for every consumed definition as the relicensing hedge; a periodic, diffed re-ingest keeps it current. The pipeline is license-clean (MIT data values, attribution-only) and serves D5 directly. **It does not gate the decision (already ratified); it gates M9 *scoping*, and the gates-vs-deferrable table below says exactly what must land first.** The one residual uncertainty is the same one D5 recorded — whether the `exposes`→capability map is genuinely "modest" on real silicon — and that rides Session C's bench validation of the two HERO devices this week.

---

## 1. The ingest/transform pipeline

### 1.1 Design thesis — the embed targets an artifact the architecture already has

The single most important design decision (record this): **HomeSynapse does not need new runtime machinery to consume the converter data.** Doc 08 §3.6 already specifies a `DeviceProfile` registry loaded at adapter init from a bundled JSON resource (`zigbee-profiles.json`), with per-`(manufacturerName, modelIdentifier)` overrides, a `DeviceCategory` (STANDARD_ZCL / MINOR_QUIRKS / MIXED_CUSTOM / FULLY_CUSTOM), cluster/reporting overrides, and a `manufacturerCodec` pointer. Doc 08 §3.5 already maps ZCL clusters → Doc 02 §3.6 capabilities, and explicitly states its converter-composition pattern "follows zigbee2mqtt's." (FACT — Doc 08 §3.5/§3.6.) So the embed pipeline's **emit target is that existing `DeviceProfile` registry + the Doc 02 capability rows it references** — the pipeline *populates a known artifact*, it does not invent a parallel one. This is what turns "M9 builds breadth ad-hoc" into "M9 builds breadth against a known pipeline." (INFERENCE — HIGH — that emitting into the already-specified profile registry is the lowest-friction, lowest-risk shape; it reuses Doc 08's loader, its category model, and its codec-pointer seam unchanged.)

The corollary: the embed is **data into Doc 08's profile/capability slots**, not a port of upstream behavior. The standard majority maps as *values*; the code tail is re-expressed as Doc 08 codecs (§3.8/§3.9) the architecture already owns. The pipeline never emits HomeSynapse production code — it emits the bundled dataset the production code loads. (This is the line that keeps the TS→Java derivative-work question LOW-risk; see §5.)

### 1.2 The five transform stages (text stage diagram)

```
  UPSTREAM (Koenkk/zigbee-herdsman-converters, MIT, pinned @ <commit>/v<semver>)
        │
        │  zigbeeModel / fingerprint (identity)  +  exposes (capability decl)
        │  meta / configure (reporting hints)    +  fromZigbee / toZigbee (CODE — not ingested as data)
        ▼
 ┌──────────────────────────────────────────────────────────────────────────┐
 │ STAGE 1 — FETCH (pinned)                                                  │
 │   Pull the converter source at a PINNED commit + semver. Record commit,   │
 │   version, license text, and SPDX id into the ingest MANIFEST. No live    │
 │   network at runtime — this is an offline, build-time / tooling step.     │
 │   [provenance capture begins HERE — §2]                                   │
 └──────────────────────────────────────────────────────────────────────────┘
        ▼
 ┌──────────────────────────────────────────────────────────────────────────┐
 │ STAGE 2 — PARSE definitions                                              │
 │   Read each definition module. Extract the DECLARATIVE fields only:       │
 │   zigbeeModel[], fingerprint[] (manufacturerName/modelID/endpoint sig),   │
 │   exposes[] (type, name, unit, value_min/max/step, access bits, values),  │
 │   reporting hints. CLASSIFY each def: STANDARD-MAJORITY vs CODE-TAIL       │
 │   (presence of a non-trivial fromZigbee/toZigbee, modelID==TS0601, or a   │
 │   Xiaomi/Aqara manufacturer marks it CODE-TAIL → routed away from bulk).   │
 │   fromZigbee/toZigbee bodies are NOT parsed-as-data; at most their        │
 │   PRESENCE + a reference link are recorded for the curated path.          │
 └──────────────────────────────────────────────────────────────────────────┘
        ▼
 ┌──────────────────────────────────────────────────────────────────────────┐
 │ STAGE 3 — NORMALIZE to an Intermediate Representation (IR)               │
 │   A HomeSynapse-owned, stable IR (JSON) — the de-coupling layer between    │
 │   the upstream schema and our model. One IR record per device def:        │
 │     { identity:{manufacturerName, modelIdentifier, fingerprint…},          │
 │       category: STANDARD_ZCL|MINOR_QUIRKS|MIXED_CUSTOM|FULLY_CUSTOM,       │
 │       entities:[ { endpoint, exposes:[ <normalized exposes> ] } ],         │
 │       provenance:{ upstreamCommit, version, license, sourcePath } }        │
 │   Normalization fixes units to canonical SI (Doc 02 §3.7), maps Z2M        │
 │   access bits → Doc 02 permissions, ranges → min/max/step.                │
 │   The IR is the thing we DIFF on re-ingest (§2) and the thing the human    │
 │   reviews (§1.4). It outlives any single upstream schema version.          │
 └──────────────────────────────────────────────────────────────────────────┘
        ▼
 ┌──────────────────────────────────────────────────────────────────────────┐
 │ STAGE 4 — MAP IR → HomeSynapse rows (the rules engine — §1.3)            │
 │   exposes → Doc 02 §3.6 capability rows + Doc 02 §3.10 entity-type        │
 │   classification. STANDARD-MAJORITY maps deterministically by rule.       │
 │   Unmapped/novel exposes (CODE-TAIL) → flagged for the curated path +     │
 │   (where adopted) a Doc 02 §3.9 namespaced CustomCapability stub.         │
 │   Emit candidate DeviceProfile rows (Doc 08 §3.6 schema) + capability     │
 │   rows. Every row carries its provenance pointer.                          │
 └──────────────────────────────────────────────────────────────────────────┘
        ▼
 ╔══════════════════════════════════════════════════════════════════════════╗
 ║ ███ HUMAN-REVIEW GATE ███  (sits BETWEEN Stage 4 and Stage 5)            ║
 ║   No mapping reaches the shipped artifact un-reviewed. The reviewer sees   ║
 ║   the IR + the proposed rows + the auto-classification, and either        ║
 ║   ACCEPTS (standard map is clean), CORRECTS (edit the rule/override), or  ║
 ║   DEFERS to the curated/community path (code-tail / ambiguous).           ║
 ║   For the worked HERO devices this gate is also where the BENCH ground-   ║
 ║   truth (Session C) is reconciled against the upstream-derived mapping.   ║
 ║   Reviewer sign-off is recorded in the manifest (who/when/commit).        ║
 ╚══════════════════════════════════════════════════════════════════════════╝
        ▼
 ┌──────────────────────────────────────────────────────────────────────────┐
 │ STAGE 5 — EMIT the embedded, attributed artifact                        │
 │   Write the reviewed rows into the bundled DeviceProfile dataset          │
 │   (zigbee-profiles.json shape, Doc 08 §3.6) + the consolidated NOTICE/    │
 │   attributions artifact (§2). This is what ships; the runtime LOADS it    │
 │   via Doc 08's existing init path. No upstream code is bundled. No live    │
 │   fetch at runtime.                                                        │
 └──────────────────────────────────────────────────────────────────────────┘
        ▼
   RUNTIME (HomeSynapse Zigbee adapter, Doc 08): loads the dataset like any
   bundled profile; the code-tail codecs (Tuya/Xiaomi, §3.8/§3.9) are
   HomeSynapse-authored and load alongside, pointed-to by manufacturerCodec.
```

**Where the human-review gate sits (explicit):** between Stage 4 (machine-proposed rows) and Stage 5 (emit). The machine does the deterministic bulk; the human ratifies the standard map, corrects the rules, and routes the tail. This keeps the bulk cheap while making *what ships* a reviewed artifact — and it is the natural reconciliation point for Session C's bench ground-truth on the HERO devices. (INFERENCE — HIGH — a gate before emit, not after, is the discipline that prevents an upstream schema drift from silently shipping a wrong mapping.)

### 1.3 The mapping rules — standard-ZCL majority vs the code-shaped tail

**The split is the design.** D5 ratified exactly this cleavage; the pipeline enforces it mechanically at Stage 2 classification.

**(a) Standard-ZCL majority — `exposes` → Doc 02 §3.6 capability rows, as DATA values (no logic ported).** The `exposes` model is a structured capability declaration; the mapping is a finite rule table from `exposes` shapes to HomeSynapse capabilities. (FACT that `exposes` is structured — Session A §3; FACT that the destination capabilities exist — Doc 02 §3.6.) The core rules (INFERENCE — MEDIUM-HIGH that these are modest for standard devices; Session C confirms on silicon):

| Z2M `exposes` shape | → HomeSynapse capability (Doc 02 §3.6) | → attribute / mapping notes |
|---|---|---|
| `switch`/`binary` w/ `state` ON/OFF, access RW | `on_off` | `on` (BOOLEAN); confirmation EXACT_MATCH. ZCL OnOff 0x0006 per Doc 08 §3.5 |
| `light` feature `brightness` (0–254, RW) | `brightness` | `brightness` (INT 0–100 %); Doc 08 §3.5 keeps raw 0–254, % at query time; TOLERANCE ±2 |
| `light` feature `color_temp` (mireds, RW) | `color_temperature` | `color_temp_kelvin` (INT, K); mireds→K = 1e6/mireds at query (Doc 08 §3.5); TOLERANCE ±50K |
| `light` feature `color_xy`/`color_hs` | *(Doc 02 §3.6 post-MVP `color_xy`/`color_hs` — reserved)* | schema-accommodated; map when capability lands; else curated |
| `numeric` `temperature` °C, RO | `temperature_measurement` | `temperature_c` (FLOAT/QuantityValue °C); ZCL 0x0402 ÷100 (Doc 08 §3.5) |
| `numeric` `humidity` %, RO | `humidity_measurement` | `humidity_pct`; ZCL 0x0405 ÷100 |
| `numeric` `illuminance` lux, RO | `illuminance_measurement` | `illuminance_lux`; ZCL 0x0400 |
| `numeric` `power` W, RO | `power_measurement`/`power_meter` | `power_w`; ZCL 0x0B04 × mult/div (Doc 08 §3.5) |
| `numeric` `energy` kWh, RO | `energy_meter` | `energy_wh`; ZCL 0x0702 × mult/div |
| `binary` `occupancy` | `occupancy` | `occupied` (BOOLEAN); ZCL OccupancySensing 0x0406 / IAS Zone 0x0500 |
| `binary` `contact` | `contact` | `open` (BOOLEAN); IAS Zone zone-type 0x0015 |
| `binary` water/smoke/vibration | `binary_state` (+ post-MVP `water_leak`/`smoke`) | IAS Zone zone-type → capability (Doc 08 §3.5/§3.12) |
| `numeric` `battery` %, RO | `battery` | `battery_pct` (INT 0–100); ZCL PowerConfiguration 0x0001 ÷2 |
| `numeric` `linkquality`/RSSI | `device_health` | `lqi`/`rssi_dbm`; synthetic signal-quality (Doc 08 §3.11) |
| `enum` (RW/RO) w/ `values[]` | nearest standard cap, else `CustomCapability` (Doc 02 §3.9) | ENUM (validated `valid_values`); EnumTransition confirmation |

The transform reads **values** (type, unit, range, access) out of `exposes` and writes them into Doc 02 schema rows. It ports **no upstream function body.** (This is the load-bearing fact for §5's TS→Java question: the standard majority is *data consumption*, not derivative code.)

**(b) The code-shaped tail — re-expressed, never transcribed.** `fromZigbee`/`toZigbee` are converter FUNCTIONS (Session A §3 — FACT); Tuya `0xEF00` tunnels a proprietary datapoint protocol (modelID `TS0601`); Xiaomi/Aqara pack sensor+battery data in a custom TLV on Basic 0xFF01 / 0xFCC0 0x00F7. (FACT — Doc 08 §3.8/§3.9.) HomeSynapse **already owns** the destination machinery: Doc 08 §3.8 specifies a Tuya DP codec (`tuyaDatapoints` DPID→attribute map + converters) and §3.9 a Xiaomi TLV codec (`xiaomiTags` map). So the tail is handled by:
1. **Ingesting only the declarative shell** (identity + which DPIDs/tags exist + their HomeSynapse target attribute) into the Doc 08 profile's `tuyaDatapoints`/`xiaomiTags` slots — that is *data* (a DPID→attributeKey table), and it maps cleanly.
2. **Re-expressing the decode/encode logic** as HomeSynapse-authored converters (the §3.8/§3.9 codecs) and, where a datapoint has no standard capability, a Doc 02 §3.9 namespaced `CustomCapability` (e.g., `zigbee_tuya.datapoint_102`, the exact pattern Doc 02 §3.9 cites). Upstream is the **behavioral reference/cross-check** (alongside ZHA as a second source per Session A §3), never the source text.
3. **Delivery via the curated-subset + community path (§3)**, not the bulk embed — because this is incremental engineering, not a data drop.

This is precisely D5's "code, not pure data" tail. The DPID/tag *tables* ride the embed as data; the *codecs* are HomeSynapse code. (INFERENCE — MEDIUM — the table-vs-logic split is clean for the documented Tuya/Xiaomi cases Doc 08 already enumerates; novel datapoints are curated case-by-case.)

### 1.4 Worked mapping #1 — Philips Hue White A19 (HERO: `light`)

*(Wave-1 HERO. Pairs direct, no Hue bridge — reconciliation memo assertion 6. Standard-ZCL, Doc 08 §3.6 category D. Real-silicon interview rides Session C — corpus `devices/` is empty today; this is the upstream-derived expectation the bench confirms.)*

- **Identity (Stage 2/3):** `manufacturerName: "Signify Netherlands B.V."` (historically "Philips"), `modelIdentifier` per Basic 0x0005; `fingerprint`/`zigbeeModel` → device identity → Doc 02 device record + hardware identifier `zigbee_ieee`. The White A19 is on-off + dimmable (white-ambiance variants add color_temp); a plain White A19 is `light` with `on_off` + `brightness`.
- **`exposes` → capability rows (Stage 4):**

| upstream `exposes` | → capability | → attribute | confirmation |
|---|---|---|---|
| `light` feature `state` (RW) | `on_off` | `on` BOOLEAN | EXACT_MATCH |
| `light` feature `brightness` 0–254 (RW) | `brightness` | `brightness` INT 0–100 % (raw 0–254 kept; % at query) | TOLERANCE ±2 |
| *(white-ambiance only)* `color_temp` mireds (RW) | `color_temperature` | `color_temp_kelvin` INT K | TOLERANCE ±50K |
| `linkquality` | `device_health` | `lqi` / `rssi_dbm` | n/a |

- **Entity type (Doc 02 §3.10):** `light` (required `on_off`; optional `brightness`, `color_temperature`). ZCL device type Dimmable Light 0x0101 (or Color-Temp Light 0x010C) → `light` per Doc 08 §3.5. Single endpoint → single entity, `endpoint_index 1`.
- **DeviceProfile (Doc 08 §3.6):** category STANDARD_ZCL, no `manufacturerCodec`, generic cluster handlers — **no profile override needed for the plain White A19** (Doc 08 §3.6 lists Philips Hue under category D explicitly). The embed contributes the identity match + capability confirmation, not a quirk.
- **Verdict:** clean standard map; zero code-tail. **FACT** the destination capabilities/clusters exist (Doc 02 §3.6, Doc 08 §3.5). **INFERENCE — HIGH** the map is modest. **Bench-confirmed: PENDING Session C.**

### 1.5 Worked mapping #2 — SONOFF SNZB-03P (HERO: `binary` occupancy + battery)

*(Wave-1 HERO motion trigger. Pairs to any Zigbee 3.0 coordinator — "SONOFF bridge required" is marketing, reconciliation memo assertion 5. Standard-ZCL, category D. Real-silicon interview rides Session C.)*

- **Identity (Stage 2/3):** `manufacturerName: "SONOFF"` (eWeLink), `modelIdentifier: "SNZB-03P"`; `fingerprint` → device identity. Battery end device (sleepy → Doc 08 §3.4 sleepy-interview path).
- **`exposes` → capability rows (Stage 4):**

| upstream `exposes` | → capability | → attribute | confirmation |
|---|---|---|---|
| `binary` `occupancy` (RO) | `occupancy` | `occupied` BOOLEAN | n/a (read-only sensor) |
| `numeric` `battery` % (RO) | `battery` | `battery_pct` INT 0–100 (+`battery_low`) | n/a |
| `linkquality` | `device_health` | `lqi` / `rssi_dbm` | n/a |

- **Entity type (Doc 02 §3.10):** `binary_sensor` (required ≥1 binary capability — `occupancy`; optional `battery`, `device_health`). The `battery` surface is a candidate DIAGNOSTIC `EntityRole` per Doc 02 §3.10 AMD-44 Stage-2 (battery/voltage are diagnostic); occupancy is PRIMARY. (INFERENCE — role assignment is a Stage-4 rule + review-gate call.)
- **Protocol nuance the bench confirms (Doc 08 §3.5/§3.12):** the SNZB-03P reports occupancy via OccupancySensing 0x0406 **or** IAS Zone 0x0500 (zone type 0x000D motion) depending on firmware. If IAS Zone, the adapter's IAS enrollment handshake (Doc 08 §3.12) applies and `zoneStatus` bit 0 → `occupied`. Battery via standard PowerConfiguration 0x0001 (raw/2) — *not* the Xiaomi voltage-TLV path. **Which of OccupancySensing-vs-IAS the device actually uses is exactly the kind of fact the bench (Session C) pins**; the embed proposes both candidate mappings and the review gate selects on ground-truth.
- **DeviceProfile (Doc 08 §3.6):** category STANDARD_ZCL, no manufacturer codec. SONOFF SNZB is named under Doc 08 §3.6 category D.
- **Verdict:** clean standard map; the only open question is OccupancySensing-vs-IAS routing, which is a **Doc 08 §3.5 mapping selection** (the table already covers both), resolved at the review gate with bench data — *candidate* Doc 08 currency note, not a model gap. **FACT** capabilities/clusters exist. **INFERENCE — HIGH** modest. **Bench-confirmed: PENDING Session C.**

---

## 2. Provenance / attribution + version-pinning discipline

### 2.1 Recommendation: a CONSOLIDATED `NOTICE`/attributions artifact, built mechanically from the ingest manifest (NOT per-file headers)

**Recommend the consolidated artifact.** Reasoning (the trade-off, decided):

- **Per-file provenance** (a license header transcribed into every emitted profile row) is the wrong shape here because (a) the embed is *data*, not source files — the natural distribution unit is one bundled dataset, not thousands of files; (b) MIT/Apache notices "aggregate to a single retained-attributions artifact" cleanly (Session A §5.3 flagged this as the routine form); (c) per-file headers would bloat the runtime artifact and drift the moment a row is re-mapped, creating a maintenance liability with no legal upside.
- **Consolidated `NOTICE`** satisfies both licenses' actual obligations: MIT requires the copyright line + permission notice "in all copies or substantial portions" — a single bundled NOTICE shipped with the dataset *is* that reproduction (FACT — Session A §1); Apache-2.0 (if any ZHA cross-reference is ever embedded) requires **propagating upstream NOTICE content** + retaining attribution — again a consolidated NOTICE is the canonical vehicle (FACT — Session A §1). 
- **The mechanically-built bit is the discipline.** The consolidated NOTICE is **generated from the Stage-1/3 ingest manifest**, not hand-curated — so it is exhaustive by construction and re-generated on every re-ingest. It carries, per consumed definition: upstream repo + **pinned commit + semver**, license SPDX id + license text reference, source path, and ingest date. (INFERENCE — HIGH — a generated NOTICE is the only form that stays correct across constant upstream churn; a hand-maintained one rots.)

**Counsel still blesses the form** (§5 item 3) — but the engineering recommendation is unambiguous: consolidated, generated, manifest-backed.

### 2.2 Pinned-version + re-ingest pipeline (the relicensing hedge)

D5 records the explicit hedge: "pin the consumed version + record its license at ingest." (FACT — D5 riders.) Concretely:

- **Pin at Stage 1.** Every ingest is against a specific upstream **commit SHA + semver** (Session A read v26.73.0 @ 2026-06-26 — FACT, primary source; upstream climbs constantly). The pin + the license text *as read at that commit* go into the manifest. If upstream ever relicenses away from MIT (no evidence; the GPL-3.0 is the *app*, not this DB — Session A §1, D5), **the embedded dataset is unaffected because it was consumed under the pinned MIT commit** — relicensing is forward-only; it does not retroactively un-license code already obtained under MIT. The pin is the proof of the terms under which we took it.
- **Periodic re-ingest, diffed against the IR (Stage 3).** Re-run the pipeline on a cadence (recommend tied to a release train, not a clock — e.g., once per HomeSynapse minor, or on demand when a target device's upstream def changes). The re-ingest **diffs the new IR against the shipped IR**: new devices → candidate adds; changed `exposes` → candidate row updates (re-gated by a human); a license change at the new commit → **escalation, not auto-adopt** (stay on the last MIT-pinned commit and escalate to counsel + the hub). 
- **The manifest is the single source of provenance truth** — it drives the NOTICE (§2.1), records the human-review sign-off (§1.2 gate), and is the artifact a re-ingest diffs against. (INFERENCE — HIGH — one manifest, mechanically consumed three ways, is the discipline that makes provenance not-a-chore.)

---

## 3. Curated-subset fallback + community path

D5 ratified "curated, prioritized subset + community-contribution path" for the non-declarative tail. The pipeline serves it as follows.

### 3.1 The top-N priority list — V1 demo + UX devices first

The embed runs **breadth-first within priority tiers**, not uniformly across upstream's thousands of defs. The priority order (grounded in the bench corpus README's HERO targets + the Wave-1/Wave-2 device list):

1. **Tier 0 — the V1-demo HERO path (must work):** Philips Hue White A19 (`light`), SONOFF SNZB-03P (`occupancy`+`battery`). These are the worked mappings above; bench-validated (Session C). *These gate the demo, hence M9 (see §5).*
2. **Tier 1 — the Wave-1/Wave-2 bench archetypes (the corpus README list):** SNZB-04P (contact), SNZB-01P (button/scene), S31 Lite ZB / S31-ZB (smart plug + energy), SNZB-02P (temp/humidity). All standard-ZCL or minor-quirks → bulk-embeddable; each is a corpus regression baseline.
3. **Tier 2 — the standard-ZCL long tail (categories C/D, ~60%):** generic Zigbee 3.0 lights/switches/plugs/sensors. Bulk embed via the rules engine; review-gated in batches.
4. **Tier 3 — the code-tail (categories A/B, ~40%): Tuya `0xEF00` (`TS0601`), Xiaomi/Aqara.** *Curated, not bulk.* Prioritized by demand; each requires the §1.3(b) re-expression (DPID/tag table embed + HomeSynapse codec). This is where the community path carries the weight.

### 3.2 The community-contribution path

The long-tail code-tail is unbounded; a new project's community flywheel is unproven (Session A §4 cons). The pipeline makes contribution *structured* rather than ad-hoc:

- **The IR + DeviceProfile schema (Doc 08 §3.6) is the contribution unit.** A contributor characterizes a device on a reference stack (the corpus README method — interview, map clusters→Doc 08 §3.5, record MATCH/GAP), then submits an IR/profile row + (for code-tail) a codec mapping. This is the *same artifact the embed pipeline emits*, so contributions and machine-ingest converge on one format.
- **The Doc 02 §3.9 `CustomCapability` namespace is the contribution sandbox.** Novel datapoints land as `EXPERIMENTAL` namespaced custom capabilities (Doc 02 §3.9 governance: stability levels, no shadowing standard IDs, UI-labeled non-standard). Proven ones graduate to standard capabilities ("paved path," Doc 02 §3.9). 
- **The human-review gate (§1.2) is the contribution merge gate** — community submissions enter at the same Stage-4→5 gate as machine output, so quality control is uniform. (INFERENCE — MEDIUM — the flywheel's *velocity* is unproven; the *mechanism* is sound because it reuses the embed's own artifacts.)

---

## 4. (folded into §3 above — curated/community is one section)

---

## 5. Counsel-ready legal list (LOW-risk spot-check — phrased for yes/no-with-context answers)

*Engineering assessed all four LOW-risk (Session A §5; D5 records them as gating the embed *form*, not the decision). Each is phrased as a specific question a lawyer can answer yes/no with context. These gate the embed MECHANICS; the direction is ratified.*

1. **Apache-2.0 NOTICE-propagation at enterprise-sublicensing scale.** *If* HomeSynapse ever embeds any Apache-2.0 material (e.g., a ZHA `zha-quirks` cross-reference) into the bundled dataset and sublicenses HomeSynapse across a free→paid→enterprise tier model: **Is a single consolidated, generated `NOTICE` artifact that reproduces the upstream NOTICE content + retains attribution sufficient to satisfy Apache-2.0 §4(d) at every tier, with no per-tier or per-sublicensee additional obligation?** (Yes/No + any condition on the NOTICE's placement/visibility.)

2. **Apache-2.0 patent-grant + retaliation clause vs the enterprise sublicensing model.** **Does HomeSynapse's enterprise-tier sublicensing structure interact with Apache-2.0 §3's patent grant or its patent-retaliation termination in any way that creates exposure or that we must surface to enterprise sublicensees?** (Yes/No + context. Engineering view: the express grant is *defensive/favorable*; confirm nothing in our tiering forfeits it.)

3. **TS→Java derivative-work boundary — consuming data VALUES vs porting LOGIC.** Our pipeline (a) reads declarative `exposes`/identity **values** out of the MIT converter DB into our own schema, and (b) **independently re-expresses** the `fromZigbee`/`toZigbee`/Tuya/Xiaomi *logic* as our own code using upstream only as a behavioral reference. **For (a) data-value consumption and (b) clean-reference re-expression: is a single consolidated attribution NOTICE (carrying the pinned commit/version/license per consumed definition) the correct and sufficient attribution form under MIT, and does (b) avoid creating a derivative work of the upstream source as long as no upstream function bodies are transcribed?** (Yes/No + where the derivative-work line sits.)

4. **Trademark / CSA "Zigbee" word-mark + vendor names — nominative use.** The dataset embeds vendor names ("Philips/Signify," "SONOFF," "Tuya," "Aqara") to identify which physical device a definition matches, and product materials may reference "Zigbee." **Is descriptive/nominative use of (a) embedded vendor names within the matching dataset and (b) the CSA-controlled "Zigbee" word mark in product/marketing copy defensible without a trademark license, provided we imply no endorsement and make no certification claim?** (Yes/No + the specific "do/don't" line for marketing copy — engineering view: a branding-copy concern, not a data-embed one.)

**None blocks M9 *direction* (D5 ratified). Items 1–3 gate the embed form before the dataset ships at scale; item 4 gates marketing copy.**

---

## 6. M9-gating verdict — what must land BEFORE M9 scoping vs AFTER

*Framing: D5 is ratified, so M9 *scoping* is unblocked in principle. The question this table answers is what must be TRUE for M9 scoping to be sound (not built — sound), vs what M9 can defer to execution.*

| Item | Gates M9 scoping (must land BEFORE) | Deferrable (AFTER M9 scoping / during execution) | FACT/INFERENCE |
|---|---|---|---|
| **Pipeline shape agreed** (this design: ingest→IR→map→gate→emit into Doc 08 §3.6 profiles) | ✅ — M9 scopes against THIS pipeline, not ad-hoc | | INFERENCE (HIGH) — it's the "known pipeline" D5 asked for |
| **The standard-majority `exposes`→capability rule table (§1.3a)** | ✅ — the rule table bounds M9's "how many devices, how fast" estimate | per-row corrections | FACT rows exist (Doc 02 §3.6/Doc 08 §3.5); INFERENCE the table is complete-enough |
| **HERO bench validation (Hue A19 + SNZB-03P) — Session C** | ✅ — confirms the map is "modest" (the one D5 re-open trigger). A messy map re-weights M9 toward curated sooner | broader corpus (Tier 1+) bench | FACT corpus is EMPTY today; INFERENCE map is modest → **PENDING Session C** |
| **Provenance/version discipline decided** (consolidated NOTICE, manifest-backed, pinned commit) | ✅ — M9 can't ship breadth without the attribution+pin discipline in place | the re-ingest *cadence* tuning | INFERENCE (HIGH) |
| **Legal items 1–3 (counsel)** | **Soft-gate** — should be commissioned before M9, but per D5 they gate the embed *form/ship*, not scoping. M9 can *scope* in parallel with counsel; it cannot *ship the embedded dataset at scale* until 1–3 return | item 4 (marketing) | FACT D5 says "gate embed mechanics, not the decision" |
| **Tuya `0xEF00` / Xiaomi codec re-expression (§1.3b)** | | ✅ DEFERRABLE — curated/community path, incremental; NOT a scoping gate (it's the ~40% tail, explicitly post-bulk) | FACT it's "code, not data" (D5) |
| **Community-contribution mechanism** (IR/profile as contribution unit) | | ✅ DEFERRABLE — design now (done, §3.2), stand up during/after M9 | INFERENCE |
| **Re-ingest pipeline running** | | ✅ DEFERRABLE — first pinned ingest gates scoping; the *periodic* re-ingest is post-M9 maintenance | INFERENCE |

**Net verdict:** M9 scoping is sound once (i) this pipeline shape + the standard-majority rule table are accepted, (ii) the provenance/pin discipline is adopted, and (iii) Session C confirms the two HERO mappings are modest. Counsel items 1–3 should be commissioned in parallel and must return before the embedded dataset ships at scale, but they do not block scoping. Everything in the code-tail / community / re-ingest column is deferrable to M9 execution and beyond.

---

## ESCALATIONS TO THE HUB

*(Recorded, not edited — this session is write-isolated to this one file. The hub assembles any amendment.)*

1. **Brief cross-reference imprecision (NOT a doc gap — a pointer correction for the hub's records).** The dispatch brief (and D5) point at "Doc 02 §3.5 ZCL cluster→capability mapping" as the embed target. **The actual ZCL-cluster→capability mapping table lives in Doc 08 §3.5**, not Doc 02 §3.5. Doc 02 §3.5 is the "Capability Definition Structure"; the capability *vocabulary* the embed targets is **Doc 02 §3.6** (Standard Capability Set) + **§3.7** (attribute type system). This design uses the correct sections. No doc is wrong; the brief's section pointer is. Flagging so the hub's spine references resolve cleanly. **Severity: cosmetic.**

2. **Candidate Doc 08 §3.5 currency note (NOT a model gap — bench will confirm).** The SNZB-03P occupancy surface may arrive on **either** OccupancySensing (0x0406) **or** IAS Zone (0x0500, zone type 0x000D) depending on firmware. Doc 08 §3.5's table **already covers both** rows, so the model is *not* missing anything — but the *selection rule* (which to use when a device exposes one vs the other, and whether IAS enrollment per §3.12 is always required for SNZB-03P) is a real-silicon fact the corpus is empty on today. **If Session C finds the device does something the §3.5 table can't express, THAT is a now-fix escalation per the corpus README method.** As of this design it is a *candidate* currency note, not a confirmed gap. **Severity: deferred-to-bench; no amendment proposed yet.**

3. **No Doc 02 / Doc 08 *gaps* found that block the pipeline.** The embed targets artifacts both Locked docs already specify (Doc 08 §3.6 `DeviceProfile` registry + codec seams; Doc 02 §3.6/§3.7/§3.9 capability+custom-capability model). The architecture explicitly anticipated the Z2M pattern (Doc 08 §3.5). **No structural amendment is required to stand up the pipeline as designed.** (If Session C surfaces a HERO-device mapping the model can't express, that flips item 2 to a now-fix — but that is a bench finding, not a design finding.)

---

## 7. Sources

**Primary (project-internal, Locked / ratified):**
- D5 (RATIFIED 2026-06-26) — `context/decisions/2026-06-25_deeper-M7-automation-architecture_decision-record.md` §D5 + riders.
- Session A (the basis) — `context/assessments/2026-06-23_zigbee-converter-db-license-feasibility_assessment.md` (license FACTs §1; technical fit §3; legal spot-check §5; re-open triggers §6).
- Reconciliation memo — `context/assessments/2026-06-26_v6-fanout-validation-and-dispatch-reconciliation_PM-memo.md` (HERO-device pairing assertions 5/6; D5 ratification).
- Doc 02 (Locked) — `homesynapse-core-docs/design/02-device-model-and-capability-system.md` §3.5 (capability def structure), §3.6 (standard capability set — embed destination vocabulary), §3.7 (attribute type system / QuantityValue (value,unit) contract), §3.9 (CustomCapability extensibility — the code-tail home), §3.10 (entity-type compositions + AMD-44 Stage-2 EntityRole), §3.12 (discovery/adoption), §8.1 (registry interfaces).
- Doc 08 (Locked) — `homesynapse-core-docs/design/08-zigbee-adapter.md` §3.5 (ZCL cluster→capability mapping table — the real mapping target; states it follows the Z2M converter-composition pattern), §3.6 (DeviceProfile registry + A/B/C/D category split + 60/40 standard-vs-custom number + bundled `zigbee-profiles.json` emit target), §3.8 (Tuya 0xEF00 DP codec + `tuyaDatapoints`), §3.9 (Xiaomi/Aqara TLV codec + `xiaomiTags`), §4.3 (profile JSON schema).
- Corpus ground-truth — `nexsys-hivemind/project-knowledge/device-corpus/README.md` (HERO targets; characterization method; MATCH/GAP→now-fix escalation rule) + the directory itself: **EMPTY of device entries today** (only README) — Session C bench has not landed (FACT, verified 2026-06-26).

**Primary (external, via Session A's file-level reads — re-verification by live fetch was attempted this session but the web tool timed out twice at 180s; relying on Session A's 2026-06-26 primary-source reads, which are same-day):**
- `zigbee-herdsman-converters` LICENSE (MIT) + package.json (`"license":"MIT"`, **v26.73.0**, read 2026-06-26) — https://github.com/Koenkk/zigbee-herdsman-converters (LICENSE, package.json).
- `zigbee-herdsman` LICENSE (MIT) — https://github.com/Koenkk/zigbee-herdsman/blob/master/LICENSE.
- Zigbee2MQTT *application* is GPL-3.0 (distinct package — NOT consumed) — https://www.zigbee2mqtt.io/.
- Z2M `exposes` model (the capability-declaration shape ingested at Stage 2) — https://www.zigbee2mqtt.io/guide/usage/exposes.html (documented in Session A §3; live fetch timed out this session).
