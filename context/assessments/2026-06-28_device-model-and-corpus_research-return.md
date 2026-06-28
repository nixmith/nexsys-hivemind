<!--
file: context/assessments/2026-06-28_device-model-and-corpus_research-return.md
purpose: STREAM B return — how HomeSynapse should represent, store, code-for, and maintain its device/component compatibility model + characterization corpus, objectively benchmarked against the five prevailing models (HA components/ · Z2M converters/exposes · zigpy zha-device-handlers quirks · deCONZ DDF · Matter device-types/clusters), returning the concrete corpus schema + onboarding-pipeline that REALIZES the ratified D5 and feeds Doc 02/08 governance + M9 + the nexsys-bench Phase-2 model. Realizes R5 (the three sharpenings) of the 2026-06-28 bench-test-and-truth-engine decision record.
audience: PM (v11 hub — reconciles into Doc 02/08 governance + the nexsys-bench Phase-2 model), Nick, the M9 Zigbee lane, the Stream A bench lane, the Distribution pairing-wizard lane.
state-type: assessment (dispatched research-session return — WRITE-ISOLATED per the 2026-06-28 dispatch; this session writes ONLY this file; no spine, no production code).
status: RETURNED 2026-06-28. RECONCILED into the spine by the v11 hub 2026-06-28 (beat-30): AMD-CAND-1 routed to governance review→ratify; AMD-CAND-2/3 surfaced to Nick; the confirmation block wired into the bench runbook; the IR + pipeline seeded into the nexsys-bench Phase-2 model.
anchors: context/handoff/2026-06-28_device-model-and-corpus_research_session_dispatch.md (the dispatch) · context/decisions/2026-06-25_deeper-M7-automation-architecture_decision-record.md §D5 (RATIFIED — adapt-the-data + curated-subset fallback; this REALIZES it) · context/decisions/2026-06-28_bench-test-and-truth-engine_decision-record.md R5 (the three sharpenings) · homesynapse-core-docs/design/02-device-model-and-capability-system.md (Locked) · design/08-zigbee-adapter.md §3.5/§3.6 (Locked) · INV-CE-04 / INV-PROJ-01 / AMD-50-INV-03 / AMD-90-INV-01 / AMD-87-INV-01.
sources-discipline: every load-bearing EXTERNAL claim is read from a primary source (project docs, official upstream docs, or file-level license/SPDX), cited inline + in §9. FACT vs INFERENCE flagged. Honest UNVERIFIED flags where a claim could not be primary-verified this session. No fabricated citations. Builds on (does not duplicate) Session A (license feasibility) + Session V2-B (embed pipeline); the new contributions are the full 5-way survey + scorecard, the confirmation-first corpus layer, and the unified onboarding pipeline.
-->

# Stream B — The Device-Representation Model That Realizes D5

## One-paragraph recommendation — CONFIDENCE: HIGH on the model shape + survey; MEDIUM-HIGH on transform-modesty (rides Stream A bench); HIGH on the confirmation-first contribution

**Adopt a HomeSynapse-owned, declarative, version-pinned JSON corpus that borrows the best idea from each prevailing model and rejects the one idea each gets wrong for an event-sourced, local-first system — emitting into the artifacts the architecture already specifies (Doc 08 §3.6 `DeviceProfile` registry + Doc 02 §3.6 capability rows), never a parallel one.** Concretely, take Zigbee2MQTT's **`exposes` capability-declaration shape** as the capability layer (this is D5's "adapt-the-data" source, and it maps onto our ZCL-aligned model with modest transform — Session A/V2-B); take deCONZ DDF's **generic-items inheritance** as the scale-without-rot discipline (a device entry points at shared defaults and records only its deltas — the "pointer-not-copy / truth-hierarchy" rule); take Matter's **mandatory/optional conformance** framing for entity-type composition (Doc 02 §3.10 already "follows Matter's device type composition model"); and **reject the code-in-the-data-path escape hatch** that HA (`supported_features` + arbitrary Python), zigpy (replacement-cluster Python), and even the most data-driven model — deCONZ DDF (`eval` JavaScript via QJSEngine) — all reserve, because our replay-determinism invariants (INV-PROJ-01, AMD-50-INV-03: the derivation rule is a pure function of `(priorState, envelope)` — no I/O, no clock, no `eval`) forbid arbitrary code on the event-replay path. The code-shaped long tail (Tuya `0xEF00`, Xiaomi TLV) is therefore routed to **named, audited, HomeSynapse-authored codecs** (Doc 08 §3.8/§3.9), pointed-to by the profile's `manufacturerCodec` field — re-expressed, never transcribed (the D5 cleavage; the license-clean line, Session A/V2-B). The single most important *new* contribution of this return is **first-classing confirmation (sharpening #2): the corpus must record, per real device, whether a true `CONFIRMED` is even achievable and when it must honestly fall to `UNCONFIRMED`** — a fact the capability-level `ConfirmationMode` default cannot know (it depends on whether the device reports its authoritative attribute back, its reporting posture, and whether it accepts Configure Reporting). That confirmation-characterization block is the corpus slot the Stream A bench fills, and it is what turns the `confirmed | unconfirmed | failed` differentiator from a design claim into a per-device, regression-protected fact. **No structural Doc-02/08 amendment is required to stand up the corpus; the confirmation-characterization block is the one substantive amendment candidate, alongside the two carried-forward Wave-1 GAPs (ESC-W1-HUE-01 full-color + the color-temp canonical-unit drift).**

---

## 0. Scope, method, and what this builds on

This return realizes **R5** (the three sharpenings) of the bench-test-and-truth-engine decision record and answers the dispatch's precise question: *how should HomeSynapse represent, store, code-for, and maintain its device/component compatibility model + characterization corpus, objectively better for our architecture than the prevailing approaches, and what is the concrete corpus schema + onboarding pipeline?* It is framed throughout as **"the corpus model that realizes D5,"** never as a greenfield that could contradict a locked decision; where the research found tension with a Locked doc it is surfaced in §8 as an escalation, not silently diverged (per the dispatch).

**Write-isolation.** This session writes **only this file** to `context/assessments/`. It proposes no spine edit and emits no production code, no `zigbee-profiles.json`, and no corpus entries. The hub reconciles this into Doc 02/08 governance + the nexsys-bench Phase-2 model.

**What is already settled (this return does not re-litigate):**
- **D5 is RATIFIED** — adapt-the-data declarative core + curated-subset/community fallback; reject runtime-interop + rebuild (decision record §D5).
- **The license question is settled and re-verified below (§7).** Session A established it at the file level; this session re-confirmed the load-bearing SPDX facts against primary sources.
- **The upstream-ingest embed pipeline shape is designed** (Session V2-B): a five-stage offline `fetch→parse→normalize-to-IR→map→emit` pipeline with a human-review gate, emitting into Doc 08 §3.6. This return **extends** it (adds the bench-capture interview path, the confirmation layer, and the M9-acceptance tail) rather than restating it.

**What is new in this return:** (1) the full **five-way comparative survey** with primary sources (Session A deeply assessed only Z2M + ZHA; deCONZ DDF, Matter, and HA's representation model were not surveyed at this depth); (2) the **objective scorecard** against our constraints; (3) the **confirmation-characterization layer** (sharpening #2 — genuinely new); (4) the **unified onboarding pipeline** that merges the upstream-ingest and bench-capture paths and carries through to M9 acceptance (sharpening #3).

---

## 1. The comparative survey (five models, primary-sourced)

The five models split cleanly into two philosophies, and naming the split is the most load-bearing finding of the survey:

- **Descriptive / adaptive** (HA, Z2M, zigpy, deCONZ): the model *wraps whatever the device actually does*, including out-of-spec behavior. This is where the real-world device long tail is actually solved.
- **Prescriptive / normative** (Matter): the model defines what a conformant device *must* do; the device conforms to the model. Elegant, but it does not help with the non-conforming long tail — it assumes it away.

HomeSynapse is ZCL-aligned and Zigbee-first and must onboard real, frequently-non-conforming devices today, so its corpus must be **descriptive/adaptive in mechanism** while borrowing Matter's **prescriptive rigor** for the *internal* type system (the sealed capability set + entity-type composition). That is precisely the posture Doc 02 already takes (Matter-style composition internally; ZCL-derived adaptation at the boundary).

### 1.1 Home Assistant — the `components/` integration model (code-per-integration)

**Representation.** Each integration is a Python package under `homeassistant/components/<domain>`; device/feature support *is code*. Entities subclass platform base classes (`light`, `switch`, `sensor`, …) and advertise capabilities through a **`supported_features` integer bitmask defined at the root `Entity` class**, plus per-domain `EntityDescription` dataclasses. There is **no central, declarative device database** — support for a device is the existence and correctness of integration code. (FACT — HA developer docs, Entity model.)

**The load-bearing weakness for us (and Doc 02 already calls it out by name).** `supported_features` is **allowed to change at runtime** (HA's own docs: an entity "is allowed to change `device_class`, `supported_features` or any property included in a domain's `capability_attributes`"). Doc 02 §3.4 explicitly rejects this: "If capabilities change silently with runtime state (as Home Assistant's `supported_features` bitmask permits), controllers cannot reliably generate UIs, voice assistants discover incorrect capabilities, and automations that depend on capability presence break unpredictably." HA also does not let *custom* integrations define their own features — features are fixed at the entity-integration (domain) level (HA architecture discussions #1320). (FACT.)

**Verdict.** Maximum flexibility (arbitrary Python can model anything), at the cost of: capabilities are not data (not diffable, not version-controllable as a dataset), they are runtime-mutable (the anti-pattern Doc 02 §3.4 was written against), and there is no degrade-honest story for an unknown device beyond "no integration ⇒ unsupported." License: **Apache-2.0** (§7).

### 1.2 Zigbee2MQTT — `zigbee-herdsman-converters` + the `exposes` model (D5's adapt-the-data source)

**Representation.** Each device definition (a TS module under `src/devices/*`) carries: `zigbeeModel`/`fingerprint` (identity match keys — pure data); `exposes` (a structured capability declaration); `meta`/`configure`/`ota` (reporting/binding hints — mostly declarative); and `fromZigbee`/`toZigbee` (converter **functions** — JS/TS code). (FACT — Session A §3; Z2M "support new devices" docs.)

**The `exposes` model (primary-sourced in full).** Two kinds: **generic** types — `binary` (`value_on`/`value_off`/optional `value_toggle`), `numeric` (`value_min`/`value_max`/`value_step`/`unit`/`presets`), `enum` (`values[]`), `text`, `composite` (combines generics in a `features[]` array), `list` (`item_type` + `length_min`/`length_max`); and **specific** types — `light` (features `state`/`brightness`/`color_temp`/`color_xy`/`color_hs`/…), `switch`, `fan`, `cover`, `lock`, `climate`. Every generic expose carries an **`access` 3-bit bitmask** — **bit 1** = present in published state; **bit 2** = settable via `/set`; **bit 3** = retrievable via `/get` — and an optional **`category`** of `config` | `diagnostic` | (unset ⇒ regular). (FACT — Z2M `exposes` docs, read 2026-06-28; doc "Last Updated 5/16/26".)

**Two findings that directly feed our design:**
1. **`access` and `category` map onto contracts HomeSynapse already has.** `access` bits → Doc 02 §3.7 `permissions` (READ/WRITE/NOTIFY); `category` config/diagnostic/regular → Doc 02 §3.10 AMD-44 `EntityRole` CONFIG/DIAGNOSTIC/PRIMARY. The transform is near-mechanical. (INFERENCE — HIGH.)
2. **`access` is also a confirmation signal — and nobody downstream uses it that way.** Z2M's own examples: a sleeping Xiaomi WSDCGQ01LM sensor has `access: 1` (state-only, *cannot* be `/get`-queried); a Hue `effect` is `access: 2` (set-only, never reflected in state). These are exactly the devices for which an actuation can **never be actively confirmed** — a fact our corpus must capture (§4). (FACT that the access values are as stated; INFERENCE — HIGH — that they are a confirmability signal.)

**Verdict.** The `exposes` model is the single best portable capability declaration in the field, and it is license-clean as data (MIT — §7). The code tail (`fromZigbee`/`toZigbee`) is the part D5 correctly routes to re-expression, not embedding.

### 1.3 zigpy / `zha-device-handlers` — "quirks" (code-as-patches per device)

**Representation.** A quirk is, in the project's own words, a **"translator"** that "bridge[s] the functionality gap created when manufacturers deviate from the ZCL specification … parsing custom messages to and from Zigbee devices." A quirk comprises a **Signature** (the device fingerprint: `models_info` + `endpoints` with `profile_id`/`device_type`/`input_clusters`/`output_clusters`), a **replacement** (substitute clusters that normalize the deviating behavior into a clean ZCL surface), and device-automation triggers. **v1** quirks are `CustomDevice` Python classes; **v2** quirks use a fluent `QuirkBuilder` (`.replaces()`, `.sensor()`, `.add_to_registry()`), with a `TuyaQuirkBuilder` subclass for Tuya. (FACT — `zha-device-handlers` README, read 2026-06-28.)

**Verdict.** The replacement-cluster idea is elegant — it presents a normalized ZCL surface upward, which is conceptually close to what our adapter's cluster→capability layer wants. But a quirk is **code per device** (Python), so: not data, not diffable-as-data, must execute a Python runtime, and scale = code volume. It is the strongest *cross-check reference* for a device's true behavior (Session A's recommendation to use it as a second source stands), but the wrong storage model for an event-sourced core. License: **Apache-2.0** (+ express patent grant — a defensive plus; §7).

### 1.4 deCONZ DDF — JSON device descriptors (the most "data, not code" model)

**Representation.** A Device Description File is JSON: a `schema` reference (JSON-schema-validated), `manufacturername`/`modelid` match keys (with `$`-prefixed constants resolved at load), a `subdevices[]` array (each with `type`, `restapi`, `uuid`, and an `items[]` list), and a `bindings[]` array (reporting config). Crucially, each **item references a `ResourceItem` suffix and is *merged with* `generic/items/<name>.json` defaults** — a true **inheritance model** where a device records only its deltas over shared generic items, and "every key can be overwritten in the DDF file if device-specific customizations are needed." Files are organized one directory per vendor, one file per product, and **hot-reload** on change. (FACT — deCONZ DDF dev-doc, read 2026-06-28.)

**The decisive finding — even the most data-driven model reserves a code escape hatch.** Each item's `read`/`write`/`parse` carries an `"fn"` function-pointer (default `"zcl"`) **plus an `"eval"` JavaScript expression** evaluated via `QJSEngine` (e.g., `"Item.val = Attr.val * 254 / 100"`). For the hard cases it falls through to **named C++ functions** (`"fn": "xiaomi:special"`) and **external JavaScript files** (the documented Xiaomi vibration-sensor DDF parses `config/battery` and `state/orientation` via external JS). The dev-doc is explicit: `eval` is "the most basic yet powerful approach to support reading writing and parsing of arbitrary Zigbee messages without having to implement any C++ code." (FACT.) **This is the empirical proof of D5's thesis:** the field's most aggressive "data, not code" model *still* embeds executable expressions for the long tail, because pure declarative data cannot express arbitrary deviation. The question is never "data or code" — it is "*where* does the code live." (INFERENCE — HIGH.)

**Maturity nuance (honest flag).** The dev-doc page is labeled "draft / Work in Progress," but DDF is in production use in current deCONZ (a DDF editor, bundle format `.ddf`/DDB, and the community `ddf-tools` bundler all exist — search-surfaced, not deeply verified this session). **UNVERIFIED:** the exact current production maturity/coverage of DDF vs deCONZ's legacy C++ device code. Treat DDF as a *shipping, maturing* format, not a draft. (UNVERIFIED — flagged.)

**Verdict.** The inheritance model (generic-items merge) and JSON-schema validation are exactly the scale-and-diff disciplines we want and should borrow. The `eval`-in-data escape hatch is exactly what we must **not** borrow (§3.4). License: **BSD-3-Clause** (permissive; §7).

### 1.5 Matter — the standardized device-type / cluster spec (a type system)

**Representation.** Matter's **Device Library** (a CSA specification document, separate from the core spec — 22-27351, v1.0 2022 → v1.2 2023 → later revisions) defines each **device type** as a `device type ID` + a revision number + a set of **mandatory and optional clusters** with **conformance** rules; "each endpoint supporting a device type SHALL include clusters based on the conformance defined." A **cluster** is "a collection of data that group[s] the attributes, events, and commands of a specific functionality … the lowest independent functional element," explicitly "thought of as an interface, service, or object class." (FACT — CSA Matter Device Library spec + Google/Silicon Labs Matter primers, read 2026-06-28.)

**Verdict.** This is a **type system / standard, not a populated device database**. Its great strength is rigor: the mandatory/optional-cluster conformance model is exactly the entity-type composition Doc 02 §3.10 already adopts ("following Matter's device type composition model"), and Matter's cluster data model is ZCL-derived, so Matter device types will map onto our entity→capability abstraction naturally when adoption justifies a Matter controller/bridge role (the §16.6 reserved seam; prior-art return §2.8). Its weakness for *today*: it is prescriptive, so it offers nothing for the non-conforming Tuya/Xiaomi long tail — and the prior-art return already found Matter's real-world interoperability lags its marketing (version fragmentation, multi-admin issues). **Borrow the conformance/type-system rigor internally; do not adopt Matter as the corpus mechanism or an MVP dependency.** License of the reference SDK (connectedhomeip): **Apache-2.0** (§7).

### 1.6 The cross-cutting conclusion

Three facts fall out of the survey and bind the recommendation:
1. **The `exposes` capability declaration (Z2M) is the right capability layer** — portable, structured, license-clean as data, and already the architecture's chosen reference (Doc 08 §3.5 "follows zigbee2mqtt's converter-composition pattern"). 
2. **The generic-items inheritance (deCONZ) is the right scale/rot discipline** — point-at-defaults, record-only-deltas is the pointer-not-copy/truth-hierarchy rule the dispatch demands for thousands of entries.
3. **Every adaptive model reserves a code escape hatch for the long tail, and where that code lives is the whole game.** HA/zigpy put it inline (Python); deCONZ puts it inline (`eval`/C++ fn). **Our event-sourcing invariants force it *out* of the data path into named, audited codecs** — which is the one place our architecture is objectively *stricter* than all four, and the reason a straight copy of any of them would violate INV-PROJ-01.

---

## 2. The objective scorecard

Scored **for HomeSynapse's specific architecture** (local-first, event-sourced, ZCL-aligned, must-degrade-honestly, scale-without-rot). Scale: ●●● strong · ●●○ adequate · ●○○ weak — *for our constraints*, not in the absolute (HA's code model is "weak" here precisely because our constraints penalize runtime-mutable code-as-capability; it is a strength in HA's own context).

| Dimension (our constraint) | HA `components/` | Z2M converters+`exposes` | zigpy quirks | deCONZ DDF | Matter device-types | **Recommended corpus** |
|---|---|---|---|---|---|---|
| **Data-vs-code balance** (declarative pref.) | ●○○ all code | ●●○ data core + code tail | ●○○ all code | ●●● data + eval tail | ●●● pure spec | **●●● data core; code tail named-out** |
| **Version-control / diff story** | ●○○ diff = code review | ●●○ TS modules diff ok | ●○○ code diff | ●●● JSON diffs clean | ●●○ spec versions | **●●● JSON corpus diffs clean** |
| **Degrade-honestly (unknown device)** | ●○○ unsupported=silent | ●●○ generic fallback | ●○○ no-match=no quirk | ●●○ generic items | ●○○ non-conformant=undefined | **●●● generic ZCL + honest UNKNOWN (INV-SA-03)** |
| **ZCL alignment** | ●●○ via integration | ●●● ZCL-native | ●●● ZCL-native | ●●● ZCL-native | ●●○ ZCL-derived | **●●● ZCL-native (Doc 08 §3.5)** |
| **Multi-protocol generalization** | ●●● any protocol | ●○○ Zigbee-bound | ●○○ Zigbee-bound | ●○○ Zigbee-bound | ●●○ Matter/Thread | **●●● protocol-agnostic schema (INV-CE-04)** |
| **Scale / rot resistance (1000s)** | ●○○ code volume | ●●○ big repo, churns | ●○○ code volume | ●●● inheritance | ●●● finite type set | **●●● inheritance + pointer-not-copy** |
| **Event-sourced fit (replay-deterministic)** | ●○○ side-effectful | ●●○ data ok / fn no | ●○○ runs code | ●○○ `eval` breaks determinism | ●●○ data ok | **●●● no eval-in-path (INV-PROJ-01)** |
| **Confirmation-semantics support** | ●○○ none | ●●○ `access` signal, unused | ●○○ none | ●○○ none | ●●○ command/attr typed | **●●● first-class confirmation block (§4)** |
| **Licensing (for embed/redistribute)** | ●●● Apache-2.0 | ●●● MIT (data) | ●●● Apache-2.0 | ●●● BSD-3 | ●●● Apache-2.0 | **●●● MIT-derived + NOTICE** |

**Reading the scorecard honestly.** No surveyed model dominates; each leads on something. deCONZ DDF and Matter tie our recommendation on pure data-ness and rigor respectively; HA leads on raw flexibility and protocol-generality-via-code; Z2M leads on real-world coverage. The recommended corpus wins **only on the specific conjunction our architecture requires** — declarative data **and** replay-determinism (no eval) **and** confirmation-first **and** degrade-honest **and** license-clean — which no single existing model delivers because none was built against an event-sourced, confirmation-as-differentiator core. That conjunction, not any single column, is the objective case for building our own corpus that *borrows* rather than *adopts*.

---

## 3. The recommended corpus model (realizing D5)

### 3.1 Design thesis — borrow three ideas, reject one, emit into the artifacts we already have

The corpus is a **HomeSynapse-owned, declarative, attributed, version-pinned JSON dataset** whose authoritative form is a stable **Intermediate Representation (IR)** (the Session V2-B de-coupling layer) and whose *emitted* runtime artifacts are the ones Doc 08/02 already specify. Restating the V2-B design thesis because it is load-bearing and unchanged: **HomeSynapse needs no new runtime machinery to consume device data.** Doc 08 §3.6 already specifies a `DeviceProfile` registry loaded from a bundled `zigbee-profiles.json` (keyed by `(manufacturerName, modelIdentifier)`, carrying a `DeviceCategory`, cluster/reporting overrides, and a `manufacturerCodec` pointer); Doc 08 §3.5 already maps ZCL clusters → Doc 02 §3.6 capabilities. **The corpus populates those slots; it does not invent a parallel model.** (FACT — Doc 08 §3.5/§3.6; the V2-B emit target, unchanged.)

The model is built from four decisions:

1. **Capability layer = Z2M `exposes` shape, transformed to Doc 02 §3.6 capability rows as DATA values.** The §1.3(a) rule table (V2-B) stands: `exposes` type/unit/range/`access` → capability/attribute/permission/`EntityRole`. No upstream function body is ported. (Realizes D5's "adapt-the-data.")
2. **Storage discipline = deCONZ generic-items inheritance (pointer-not-copy / truth-hierarchy).** A corpus entry does **not** copy the full capability/cluster definition; it references shared **generic capability + cluster templates** and records only device-specific deltas (overrides, quirks, the confirmation block). This is how the corpus scales to thousands of entries without rotting: a ZCL-standard light is ~10 lines of deltas over the generic `light` template, not a self-contained copy that drifts when the template changes. (Borrows deCONZ; satisfies the dispatch's "pointer-not-copy discipline.")
3. **Entity-type composition = Matter-style mandatory/optional conformance** — already in Doc 02 §3.10 (required/optional capability sets per entity type, with an "unexpected capability" validation warning). The corpus entry's entity-type classification is validated against this composition at map-time; an out-of-set capability surfaces a warning rather than a silent accept (degrade-honest classification).
4. **Code tail = named, audited HomeSynapse codecs, never embedded code.** The `fromZigbee`/`toZigbee`/Tuya-`0xEF00`/Xiaomi-TLV logic is re-expressed as Doc 08 §3.8/§3.9 codecs, pointed-to by `manufacturerCodec`. The corpus carries only the **declarative shell** of the tail (the DPID→attributeKey / tag→attributeKey *tables* are data; the decode/encode *logic* is HomeSynapse code). (Realizes D5's "curated-subset fallback"; §3.4 explains why this is forced, not merely preferred.)

### 3.2 The corpus entry schema (concrete)

The schema below is the **IR record** — the durable, diffable, provenance-bearing source of truth from which `zigbee-profiles.json` + Doc 02 capability rows are emitted. It is a superset of today's `device-corpus/README.md` template (schema-version 1) and of the Doc 08 §3.6 `DeviceProfile` record, adding the **inheritance pointers**, the **provenance block**, and the **confirmation block (§4)**. Illustrative; the hub ratifies field names.

```jsonc
{
  "schemaVersion": 2,                         // corpus IR schema (bump from README v1)
  "identity": {
    "manufacturerName": "eWeLink",            // Basic cluster — the §3.6 match key
    "modelIdentifier": "SNZB-03P",
    "manufacturerCode": "0x____",             // Node Descriptor; [CONFIRM-ON-BENCH]
    "fingerprint": [ { "profileId": "0x0104", "deviceType": "0x0107",
                       "endpoints": [ { "id": 1, "in": ["0x0000","0x0001","0x0003","0x0406"],
                                        "out": ["0x0019"] } ] } ],
    "extends": "generic/profile/occupancy-binary-sensor"   // INHERITANCE pointer (deCONZ idea)
  },
  "category": "STANDARD_ZCL",                 // Doc 08 §3.6: STANDARD_ZCL|MINOR_QUIRKS|MIXED_CUSTOM|FULLY_CUSTOM
  "manufacturerCodec": null,                  // null for the standard majority; "tuya_ef00"/"xiaomi_ff01" for the tail
  "entities": [
    {
      "endpointIndex": 1,
      "entityType": "binary_sensor",          // Doc 02 §3.10 (validated vs required/optional composition)
      "capabilities": [
        { "ref": "generic/cap/occupancy",     // points at the generic capability template
          "role": "PRIMARY",                  // Doc 02 §3.10 AMD-44 EntityRole (from exposes.category)
          "deltas": {} },                     // record-only-deltas
        { "ref": "generic/cap/battery", "role": "DIAGNOSTIC",
          "deltas": { "raw": "PowerConfiguration/0x0021 ÷2" } },
        { "ref": "generic/cap/device_health", "role": "DIAGNOSTIC", "deltas": {} }
      ]
    }
  ],
  "confirmation": [ /* §4 — per actuating capability; this device is read-only so empty */ ],
  "reportingOverrides": { "0x0001": { "minInterval": 3600, "maxInterval": 62000 } },
  "interviewNotes": { "sleepy": true, "iasEnrollment": false,
                      "note": "occupancy via 0x0406 OR IAS 0x0500 per firmware — bench selects" },
  "validation": { "verdict": "MATCH", "escalation": "ESC-W1-SNZB03P-01",
                  "docRefs": ["Doc02 §3.6","Doc08 §3.5/§3.12"] },
  "provenance": {
    "source": "UPSTREAM_Z2M",                 // UPSTREAM_Z2M | BENCH_CAPTURE | COMMUNITY | DATASHEET
    "upstreamCommit": "<sha>", "upstreamVersion": "v26.73.0",
    "license": "MIT", "spdx": "MIT", "sourcePath": "src/devices/sonoff.ts",
    "ingestDate": "2026-06-28", "reviewedBy": null,
    "fieldTags": { "fingerprint": "[REF]", "confirmation": "[CONFIRM-ON-BENCH]" }
  }
}
```

The **generic templates** (`generic/cap/*`, `generic/profile/*`) hold the shared capability/cluster definitions once; entries point at them and override deltas. This is the deCONZ `generic/items/<name>.json` merge model, applied to *our* capability vocabulary. (INFERENCE — HIGH — that this is the lowest-rot form for thousands of entries.)

### 3.3 Why this is objectively better, *for our architecture*, than each surveyed model

- **vs HA `components/`:** capabilities are *data* (diffable, version-controlled, statically queryable) and *immutable per device-revision*, eliminating the runtime-mutable-`supported_features` failure Doc 02 §3.4 was written against. (We give up arbitrary-Python flexibility — acceptable, because the code tail is still expressible as named codecs.)
- **vs Z2M:** we keep `exposes`' declarative win but drop the TS-module-as-distribution-unit (we ship one attributed dataset, not thousands of code modules) and we keep the converter *logic* out of the replay path (named codecs, not `fromZigbee` functions loaded at runtime).
- **vs zigpy quirks:** we keep the replacement-cluster *concept* (a normalized ZCL surface upward = our cluster→capability layer) but as data + named codecs, not Python-per-device.
- **vs deCONZ DDF:** we adopt its inheritance + JSON-schema-validation disciplines wholesale, and **reject its `eval`-in-data** (§3.4) — the single most important divergence.
- **vs Matter:** we adopt its conformance/type-system rigor internally (already in Doc 02 §3.10) without taking on a prescriptive model that cannot represent the non-conforming long tail.

### 3.4 The event-sourcing divergence from deCONZ (the one place we are stricter than the entire field)

deCONZ proves that the most data-driven model still needs executable expressions (`eval`/named-fn) for the long tail (§1.4). HomeSynapse **cannot** put that code in the data path, and this is a hard architectural constraint, not a preference:

- **INV-PROJ-01 / AMD-50-INV-03:** the derivation rule is a **pure function of `(priorState, envelope)`** — no clock, no registry, no I/O, no randomness. An `eval` expression in a corpus entry, executed during state projection, would inject non-deterministic, non-replayable, unsanitizable code into exactly the path these invariants protect. A captured event log must replay bit-identically forever (the R1 replay-as-regression moat); `eval`-in-data forecloses that. (FACT — invariants; INFERENCE — HIGH — that eval-in-data violates them.)
- **The resolution is the D5 cleavage, expressed as a determinism boundary:** declarative data (capability rows, DPID/tag tables, reporting config) rides the corpus and is consumed by pure functions; transform *logic* is **named HomeSynapse code** (Doc 08 §3.8/§3.9 codecs) that is reviewed, tested, version-controlled, and itself replay-pure. The corpus points at a codec by name (`manufacturerCodec: "tuya_ef00"`); it never carries the codec's body.
- **Consequence — this is also the trust-brand + security win.** An embedded `eval` from a community contribution is an arbitrary-code-execution surface on a local-first hub; a named-codec pointer is not. The determinism boundary and the security boundary are the same line. (INFERENCE — HIGH.)

This is the dispatch's "must produce/consume our event-log cleanly" made concrete: the corpus is **inert declarative data**; all behavior lives in replay-pure code; the two never mix in the data path.

---

## 4. First-classing confirmation (sharpening #2) — the genuinely new contribution

### 4.1 The gap: capability-level `ConfirmationMode` cannot know device-level confirmability

HomeSynapse's confirmation semantics are real and well-specified, but they live at the **capability** level. Doc 02 §3.6 assigns each capability a default `ConfirmationMode` (`on_off`→`EXACT_MATCH`, `brightness`→`TOLERANCE ±2`, `color_temperature`→`TOLERANCE ±50K`); Doc 02 §3.8 defines the `Expectation` sealed interface (`ExactMatch`/`WithinTolerance`/`EnumTransition`/`AnyChange`) that returns `CONFIRMED`/`NOT_YET`/`FAILED`; AMD-90-INV-01 makes confirmation per-action, never Run-blocking, no engine retry; AMD-95 sources confirmation from the capability (`DISABLED` ≡ optimistic); AMD-87-INV-01 makes every `Expectation` round-trip the codec losslessly. Doc 02 §3.8 allows **adapters to override the tolerance band**. (FACT — Doc 02 §3.6/§3.8; AMD-90/95/87.)

**What none of that can express:** whether a *specific real device* can actually render a true `CONFIRMED`. The capability default assumes the authoritative attribute comes back. Three device-level facts decide whether it does — and they are exactly the facts the survey surfaced and the bench measures:

1. **Does the device report/return the authoritative attribute at all?** The Z2M `access` bitmask is the tell (§1.2): `access:1` (state-only, no `/get`) cannot be *actively* confirmed by read-after-write; `access:2` (set-only, e.g. a Hue `effect`) can **never** be confirmed — there is no attribute to compare. (FACT — Z2M `exposes` examples.)
2. **Reporting posture:** on-change reporting → promptly confirmable; **periodic-only** firmware reporting (Xiaomi environmental sensors, ~30–60 min — Doc 08 §3.7 reporting exclusions) → a command would time out before a report arrives → must honestly become `UNCONFIRMED`, not `FAILED`; **sleepy** end-devices (SNZB-03P — corpus entry) → delayed confirmation, longer honest timeout.
3. **Configure-Reporting acceptance:** Xiaomi/Aqara *reject* Configure Reporting (Doc 08 §3.7 `interviewSkips`), so the bounded report cadence we'd rely on for a confirmation deadline does not hold — the timeout must be tuned per device, or the verdict honestly degraded.

Without a device-level record of these, the engine either fabricates a `CONFIRMED` it cannot back (the silent-wrong-abstraction INV-SA-03 forbids) or pessimistically marks everything `UNCONFIRMED` (destroying the differentiator). **The corpus is where this fact must live.** This is the dispatch's requirement that a device entry "answer 'does this device let us render a true CONFIRMED, and when does it honestly become UNCONFIRMED?'"

### 4.2 The confirmation-characterization block (schema)

One block **per actuating capability** on the entity, carried in the corpus entry (and emitted into a new Doc 08 §3.6 `DeviceProfile` confirmation-override slot — §6 amendment #1):

```jsonc
"confirmation": [
  {
    "capability": "on_off",
    "confirmationMode": "EXACT_MATCH",        // inherited from Doc 02 §3.6 default; overridable per device
    "authoritativeAttribute": "on",           // the attribute whose report/readback confirms
    "reportsAuthoritative": "VERIFIED_REPORTS",// VERIFIED_REPORTS | READBACK_ONLY | NONE
    "reportingPosture": "ON_CHANGE",          // ON_CHANGE | PERIODIC | SLEEPY | NONE
    "confirmability": "CONFIRMABLE",          // CONFIRMABLE | BEST_EFFORT | UNCONFIRMABLE  ← the honest verdict
    "recommendedTimeoutMs": 5000,             // feeds Doc 02 §3.8 default_timeout, per-device-tuned
    "degradeRule": "no authoritative report within timeout ⇒ UNCONFIRMED (never FAILED unless explicit NACK)",
    "provenance": "[CONFIRM-ON-BENCH]"        // [REF] from datasheet/upstream vs bench-measured
  }
]
```

`confirmability` is the load-bearing field — it is the corpus's honest answer to "can this device back a CONFIRMED?":
- **CONFIRMABLE** — device reliably reports/returns the authoritative attribute; a true `CONFIRMED` is achievable.
- **BEST_EFFORT** — confirmation possible but unreliable/slow (sleepy, periodic-only, no Configure-Reporting); the engine should expect honest `UNCONFIRMED` under load and tune the timeout up.
- **UNCONFIRMABLE** — no authoritative attribute is reported/readable (`access:2` set-only commands); the engine must render `UNCONFIRMED` immediately and **never** a false `CONFIRMED`. This maps to `ConfirmationMode.DISABLED` (≡ optimistic, AMD-95) **with the honest reason recorded**, not a silent optimism.

### 4.3 How it renders `confirmed | unconfirmed | failed` honestly — worked cases

- **Hue White A19, `on_off`/`brightness`:** mains-powered router, reports OnOff/LevelControl on change → `reportsAuthoritative: VERIFIED_REPORTS`, `reportingPosture: ON_CHANGE`, `confirmability: CONFIRMABLE`. The hero `CONFIRMED` is genuinely achievable — and the bench measures it (the moat's headline capture target). (INFERENCE — HIGH; bench-confirmed PENDING Stream A.)
- **A write-only `effect`/`identify` (Hue `effect`, `access:2`):** no attribute returns → `confirmability: UNCONFIRMABLE`; the engine renders `UNCONFIRMED` honestly and immediately. Without this block, a naive `EXACT_MATCH` would wait the full timeout then mislabel — the block makes the honesty immediate and explained.
- **Xiaomi periodic environmental sensor (actuating config write):** `reportingPosture: PERIODIC`, `reportsAuthoritative: READBACK_ONLY` (and may reject reporting config) → `confirmability: BEST_EFFORT`, longer `recommendedTimeoutMs`, `degradeRule` → honest `UNCONFIRMED` when the periodic window hasn't elapsed. (FACT that Xiaomi rejects Configure Reporting — Doc 08 §3.7; INFERENCE on the confirmation consequence.)
- **SNZB-03P (read-only sensor):** no actuating capability → empty confirmation block; the device's value is its event stream, not a command confirmation. (Its *fixture* is still a moat asset — §5.)

### 4.4 The bench is the confirmation oracle — this ties Stream A to Stream B

The confirmation block's `[CONFIRM-ON-BENCH]` fields are exactly what the bench (Stream A) measures: the bench-test-and-truth-engine record names the moat capture target as "does a real Hue report the expected state back (→ a genuine `CONFIRMED`)? Does a non-confirming device yield an honest `UNCONFIRMED` rather than a false positive?" **That measurement is the value of `confirmability` and `reportsAuthoritative`.** So the corpus's confirmation block is the *schema slot the Stream A captures fill*, and the captured event-stream fixture (R1) is the *regression test that asserts the recorded verdict replays*. The corpus first-classes confirmation; the bench populates and proves it. (FACT — bench-test-and-truth-engine record §1/R5; INFERENCE — HIGH — that the block is the natural reconciliation slot.)

---

## 5. The onboarding pipeline (sharpening #3) — interview → corpus → device-model → M9 acceptance

### 5.1 Two interview sources, one IR, one acceptance contract

The durable thing the bench harness seeds is a pipeline with **two entry paths that converge on the same IR** (§3.2) and carry through to M9 acceptance:

- **Path U (upstream-ingest)** — the Session V2-B `fetch→parse→normalize→map` stages, machine-deriving an IR record from the pinned Z2M `zigbee-herdsman-converters` data. Cheap breadth; provenance `UPSTREAM_Z2M`.
- **Path B (bench-capture)** — the Stream A harness captures a real-silicon interview (endpoints, clusters, attributes, the full message stream + the event-stream fixture) and normalizes it into the *same* IR. Ground truth; provenance `BENCH_CAPTURE`; fills the `[CONFIRM-ON-BENCH]` fields — most importantly the confirmation block (§4).

The two paths are not redundant — they reconcile: Path U proposes the expectation, Path B confirms or corrects it on real silicon. The human-review gate (below) is where they meet.

### 5.2 The pipeline (stage diagram)

```
  PATH U: Z2M upstream (MIT, pinned @commit/semver)        PATH B: real device on the bench (Stream A)
        │  zigbeeModel/fingerprint + exposes + hints              │  interview + full message stream + fixture
        ▼                                                          ▼
  [U1 FETCH(pinned) → U2 PARSE → U3 NORMALIZE]            [B1 CAPTURE RAW ("reconstructable truth, never
        │  (V2-B stages; provenance begins)                │   notes" — R1) → B2 NORMALIZE]
        └──────────────────────────────┬───────────────────┘
                                        ▼
              ┌───────────────────────────────────────────────────────────┐
              │  IR RECORD (§3.2)  — one stable, diffable, attributed form  │
              │  identity · category · entities(caps,role,deltas) ·         │
              │  CONFIRMATION BLOCK (§4) · reporting · provenance · verdict  │
              └───────────────────────────────────────────────────────────┘
                                        ▼
              ┌───────────────────────────────────────────────────────────┐
              │  MAP → HomeSynapse rows (rules engine, V2-B §1.3)           │
              │  exposes→Doc02 §3.6 caps · entity-type→Doc02 §3.10 ·        │
              │  cluster→Doc08 §3.5 · confirmation→Doc08 §3.6 (new slot) ·  │
              │  code-tail→manufacturerCodec pointer (§3.4)                 │
              └───────────────────────────────────────────────────────────┘
                                        ▼
        ╔═══════════════════════════════════════════════════════════════════╗
        ║  ███ HUMAN-REVIEW GATE ███   (the U↔B reconciliation point)        ║
        ║   ACCEPT (clean standard map) · CORRECT (edit rule/override) ·      ║
        ║   DEFER (code-tail → curated/community) · ESCALATE (MATCH/GAP vs    ║
        ║   Doc 02/08 — a GAP is a NOW-FIX before M9 builds on it).           ║
        ║   Bench ground-truth (Path B) overrides upstream (Path U) on        ║
        ║   conflict. Sign-off (who/when/commit) recorded in the manifest.    ║
        ╚═══════════════════════════════════════════════════════════════════╝
                                        ▼
              ┌───────────────────────────────────────────────────────────┐
              │  EMIT (reviewed):  zigbee-profiles.json (Doc 08 §3.6) +      │
              │  Doc 02 capability rows + consolidated NOTICE (§7) +         │
              │  the corpus entry (devices/<model>.md ↔ IR) committed        │
              └───────────────────────────────────────────────────────────┘
                                        ▼
              ┌───────────────────────────────────────────────────────────┐
              │  M9 ACCEPTANCE (§5.4):  the corpus entry IS the spec;        │
              │  M9's interview/codec must reproduce the recorded surface;   │
              │  the captured fixture replays as a CI regression test        │
              │  asserting the recorded confirmed/unconfirmed verdict.       │
              └───────────────────────────────────────────────────────────┘
```

### 5.3 How the bench fixtures + the M9 adapter relate (shared DNA; the corpus is the contract)

The bench-test-and-truth-engine record locks two consequences this pipeline operationalizes: (a) **the harness's Zigbee→event-log transform shares DNA with the M9 adapter's interview/codec** — so Path B's `B1/B2` (capture→normalize) is a *head-start on M9*, not just a feeder; and (b) a captured stream is a seeded event log (R1), so the fixture is a replay regression test. The corpus is the **shared contract** between the three: the bench fills `[CONFIRM-ON-BENCH]` + captures the fixture; M9 consumes the corpus entry as its acceptance spec and reuses the harness's transform as its codec; the fixture replays (M7.4d `RunPipelineReplaySafetyTest` substrate) to assert M9 didn't regress. One IR, three consumers. (FACT — bench record §1 consequences (a)/(b), R1/R2/R4; INFERENCE — HIGH — that the corpus entry is the shared contract.)

### 5.4 M9 acceptance — the corpus entry as the acceptance spec

The corpus README already states the corpus "is the acceptance spec, not a simulation" and defines the MATCH/GAP-→now-fix method; this return makes the M9 hand-off explicit:
1. **Acceptance spec.** For each Tier-0/Tier-1 device, M9's interview must reproduce the corpus entry's recorded interview surface (endpoints/clusters/attributes), and M9's cluster→capability mapping must produce the recorded capability rows. A divergence is an M9 defect *or* a corpus correction — resolved at the gate.
2. **Confirmation acceptance (new).** M9 must render the corpus's recorded `confirmability` verdict: a `CONFIRMABLE` device's hero command yields `CONFIRMED` on the captured fixture; an `UNCONFIRMABLE`/`BEST_EFFORT` device yields honest `UNCONFIRMED`. This is the moat, asserted as a test.
3. **Replay regression.** The captured event-stream fixture (e.g., the SNZB-03P motion sequence) seeds a deterministic replay test — real-world behavior becomes a hardware-free CI gate (the reserved hardware-grounded-E2E seam; capture toward it, do not build it yet — bench record §1(b)).

**Sequencing (unchanged from the streams plan):** Stream B (this model) + Stream A raw captures → the durable corpus + transform → M9 acceptance + Doc 02/08 amendments. The pipeline *design* is deliverable now; the *first populated entries* ride Stream A's first-light captures.

---

## 6. Doc-02/08 amendment candidates

Surfaced as candidates for the hub to reconcile — **not** self-ratified here (write-isolation). One substantive, two carried-forward-and-confirmed, two housekeeping.

**AMD-CAND-1 (substantive) — first-class device-level confirmation characterization.** Doc 02 §3.8 currently lets adapters override *tolerance* only; it has no slot for *whether a device can confirm at all*. **Proposal:** add a confirmation-characterization block (§4.2) to the Doc 08 §3.6 `DeviceProfile` record (`confirmability` / `reportsAuthoritative` / `reportingPosture` / `recommendedTimeoutMs` / `degradeRule`), and amend Doc 02 §3.8 to acknowledge per-device *confirmability* override (not just tolerance), with the engine consuming `confirmability` to choose between a real `CONFIRMED` attempt and an honest immediate `UNCONFIRMED`. This is the schema realization of the `confirmed|unconfirmed|failed` moat and is consistent with AMD-90-INV-01 (per-action, never Run-blocking, no retry) and AMD-95 (`DISABLED`≡optimistic — now with a *recorded honest reason*). **Impact:** Doc 08 §3.6 record + Doc 02 §3.8 prose; no invariant conflict found. Severity: **substantive, pre-M9** (M9 builds confirmation on this).

**AMD-CAND-2 (carried forward, confirmed real) — ESC-W1-HUE-01 full-color GAP + internal inconsistency.** Doc 08 §3.5 has a `ColorControl(CT)→color_temperature` row only — **no** `currentHue`/`currentSaturation`→`color_hs` or `currentX`/`currentY`→`color_xy` handler. Doc 02 §3.6 marks `color_hs`/`color_xy` post-MVP, yet Doc 02 §3.10 lists them as `light` *optional* capabilities — so Doc 02 both invites and cannot realize color. This return confirms the existing corpus finding; disposition (scope-to-white/CT **(A)** vs pull-color-forward **(B)**) is the hub's + Nick's. Severity: **decision pending; not pipeline-blocking** (hero path is white/CT).

**AMD-CAND-3 (carried forward, confirmed real) — color-temp canonical-unit drift.** Doc 08 §3.5 stores `color_temp_mireds` and converts "K = 1e6/mireds **at query time**"; Doc 02 §3.6/§3.7 declares the canonical attribute `color_temp_kelvin` and the moat rule "convert to canonical units **at ingestion**." Mireds-stored-convert-at-query contradicts Kelvin-canonical-at-ingestion — the exact unit-representation drift Doc 02 §3.7 exists to prevent. Pick one canonical representation. Fold into the ESC-W1-HUE-01 disposition. Severity: **minor, but a real §3.7 contradiction.**

**AMD-CAND-4 (housekeeping) — corpus IR schema-version + provenance/inheritance governance.** Formalize the corpus IR (schema-version 2; the inheritance pointers; the `[REF]`/`[CONFIRM-ON-BENCH]` provenance tags already in the README) as the **single contribution unit** shared by machine-ingest, bench-capture, and community submission, and clarify the **truth hierarchy**: the IR corpus is the source of truth; `zigbee-profiles.json` + Doc 02 rows are *derived/emitted* artifacts (pointer-not-copy). Severity: **housekeeping; do before scale.**

**AMD-CAND-5 (cosmetic, carried from V2-B) — brief/spine pointer fix.** Several briefs point at "Doc 02 §3.5" for the ZCL cluster→capability table; that table lives in **Doc 08 §3.5** (Doc 02 §3.5 is "Capability Definition Structure"; the capability vocabulary is Doc 02 §3.6/§3.7). This dispatch already cites Doc 08 §3.5 correctly. Severity: **cosmetic.**

**No structural amendment is required to stand up the corpus as designed** — it targets artifacts both Locked docs already specify (Doc 08 §3.6 `DeviceProfile` + codec seams; Doc 02 §3.6/§3.7/§3.9 capability + custom-capability model; §3.10 composition). AMD-CAND-1 is the one substantive add, and it *extends* a reserved seam rather than contradicting a locked decision.

---

## 7. Licensing + maintenance notes (re-verified; pin-version-and-record-license per D5's hedge)

**License facts re-verified against primary sources this session (2026-06-28)** — confirming and extending Session A:

| Artifact | Role here | License (SPDX) | Primary source | Consume? |
|---|---|---|---|---|
| `zigbee-herdsman-converters` | The `exposes`/identity data — D5's adapt-the-data core | **MIT** | repo `package.json` `"license":"MIT"` | **YES — data values + attribution** |
| `zigbee-herdsman` | The Node ZNP/EZSP library (behavioral reference) | **MIT** | repo `LICENSE` | reference only |
| `zha-device-handlers` (`zha-quirks`) | Quirks — cross-check reference (§1.3) | **Apache-2.0** (+ patent grant) | repo `pyproject.toml` | reference; embed only w/ NOTICE |
| **Zigbee2MQTT (application)** | The MQTT bridge app | **GPL-3.0** | project site | **NO — never vendor/link** |
| `deconz-rest-plugin` (incl. DDF data) | DDF — potential second-source cross-check | **BSD-3-Clause** | repo README/LICENSE | reference; permissive if ever embedded |
| Home Assistant `core` | HA model — survey reference only | **Apache-2.0** | repo `LICENSE.md` | reference only |
| Matter SDK (`connectedhomeip`) | Matter — survey/seam reference only | **Apache-2.0** | repo | reference only |

**The load-bearing distinction holds (re-confirmed):** the GPL-3.0 artifact is the Z2M *application* — a different package from the MIT converter **data** + MIT library we consume. Consuming MIT data values + independently re-expressing the code tail (using upstream as behavioral reference, transcribing no function body) is permitted under MIT/Apache-2.0 with attribution; the boundary is the §3.4 determinism line, which doubles as the derivative-work line (data in / our code out). (FACT on SPDX; the four counsel spot-check items remain as Session V2-B §5 framed them — they gate the embed *form*, not the direction.)

**Maintenance discipline (adopt — Session V2-B §2, unchanged):**
- **Pin + record at ingest.** Every IR record's `provenance` carries the upstream `commit + semver + SPDX + sourcePath + ingestDate` (§3.2). The consolidated, **mechanically-generated `NOTICE`** is built from the ingest manifest (exhaustive by construction; regenerated each re-ingest) — the recommended form over per-file headers for a bundled dataset.
- **Relicensing hedge.** A pinned MIT commit is unaffected by any future upstream relicense (forward-only). On re-ingest, a **license change at the new commit is an escalation, not an auto-adopt** — stay on the last permissive-pinned commit and route to counsel + hub.
- **Re-ingest cadence.** Tie to a release train (per HomeSynapse minor / on-demand when a target device's upstream def changes), diffing the new IR against the shipped IR; new/changed rows re-enter the human-review gate.
- **Bench-captured + community entries carry no upstream license** (provenance `BENCH_CAPTURE`/`COMMUNITY`) — they are first-party/contributed; the community path uses the same IR contribution unit + review gate (§5.1, V2-B §3.2).

---

## 8. Escalations to the hub

*(Recorded, not actioned — write-isolated to this file. The hub assembles any amendment.)*

1. **AMD-CAND-1 (confirmation characterization) needs a hub decision before M9 builds confirmation.** It is the schema realization of the differentiator; M9's acceptance tests (§5.4) depend on it. **Action:** ratify the `DeviceProfile` confirmation slot + the Doc 02 §3.8 per-device confirmability note. Severity: **substantive, pre-M9.**
2. **ESC-W1-HUE-01 (full color) + the color-temp canonical-unit drift (AMD-CAND-2/3) remain open** and are real Doc 02/08 inconsistencies, not bench artifacts. **Action:** Nick/hub pick scope-to-white-CT vs pull-color-forward, and pick one canonical color-temp representation. Not pipeline-blocking.
3. **The one recorded D5 re-open trigger is still open and rides Stream A:** whether the `exposes`→capability map is "modest" on real silicon (Hue A19 + SNZB-03P). A clean map confirms the declarative-core weighting; a messy one re-weights toward the curated-subset fallback sooner. **Status:** corpus `devices/` holds two **pre-populated, Doc-02/08-validated** entries (◐) whose verdicts are final but whose raw interview + confirmation fields are `[CONFIRM-ON-BENCH]`. PENDING Stream A first-light.
4. **SNZB-03P OccupancySensing-vs-IAS selection** (V2-B escalation 2) remains a bench-pending fact, not a model gap (Doc 08 §3.5 covers both rows). The corpus `interviewNotes` proposes both candidates; the review gate selects on ground-truth.
5. **No structural Doc-02/08 gap blocks the corpus or the pipeline.** The model targets artifacts both Locked docs already specify; AMD-CAND-1 extends a reserved seam. (Confirms V2-B escalation 3.)

---

## 9. Sources

**Primary — project-internal (Locked / ratified):**
- Dispatch — `context/handoff/2026-06-28_device-model-and-corpus_research_session_dispatch.md`.
- D5 (RATIFIED 2026-06-26) — `context/decisions/2026-06-25_deeper-M7-automation-architecture_decision-record.md` §D5 + riders.
- R5 + reframe (RATIFIED 2026-06-28) — `context/decisions/2026-06-28_bench-test-and-truth-engine_decision-record.md` §1 (consequences a/b), R1–R5.
- Doc 02 (Locked) — `homesynapse-core-docs/design/02-device-model-and-capability-system.md` §3.4 (three-level separation; the `supported_features` critique), §3.5 (capability def structure), §3.6 (standard capability set + per-capability `ConfirmationMode`), §3.7 (attribute type system / `QuantityValue` (value,unit) moat / canonical-at-ingestion), §3.8 (command model + `Expectation` `ExactMatch`/`WithinTolerance`/`EnumTransition`/`AnyChange` → `CONFIRMED`/`NOT_YET`/`FAILED`; tolerance override), §3.9 (Custom capabilities), §3.10 (entity-type composition + AMD-44 `EntityRole`), §3.12 (discovery/adoption).
- Doc 08 (Locked) — `homesynapse-core-docs/design/08-zigbee-adapter.md` §3.5 (ZCL cluster→capability table — "follows zigbee2mqtt's converter-composition pattern"), §3.6 (`DeviceProfile` registry + A/B/C/D category split + bundled `zigbee-profiles.json` + `manufacturerCodec`), §3.7 (reporting config + Xiaomi `interviewSkips`), §3.8 (Tuya `0xEF00` DP codec), §3.9 (Xiaomi/Aqara TLV codec).
- Invariants — `project-knowledge/Invariants_Quick_Reference.md`: INV-CE-04 (protocol agnosticism), INV-PROJ-01 + AMD-50-INV-03 (pure-function replay determinism), INV-ES-01/02 (immutable/derivable log), AMD-90-INV-01 (per-action confirmation), AMD-87-INV-01 (Expectation codec round-trip); INV-SA-03 (never-silent / explanation-is-projection — Doc 16, via decision records).
- Prior assessments built on — `context/assessments/2026-06-23_zigbee-converter-db-license-feasibility_assessment.md` (Session A — license FACTs, technical fit, re-open triggers); `context/assessments/2026-06-26_converter-db-embed-pipeline-design.md` (Session V2-B — the ingest pipeline, provenance discipline, counsel list, M9-gating table); `context/assessments/2026-06-23_smart-home-architecture-prior-art_research-return.md` §2.5/§2.6/§2.8 (Matter trajectory; the converter-DB pattern); `project-knowledge/device-corpus/README.md` + `devices/philips-hue-white-a19.md` + `devices/sonoff-snzb-03p-motion.md` (the corpus schema v1, method, and the two ◐ entries).

**Primary — external (read this session, 2026-06-28, unless flagged):**
- Zigbee2MQTT `exposes` model (generic binary/numeric/enum/text/composite/list + specific light/switch/fan/cover/lock/climate; the `access` 3-bit bitmask; `category` config/diagnostic) — https://www.zigbee2mqtt.io/guide/usage/exposes.html (fetched in full).
- Zigbee2MQTT "support new devices" (converter authoring; `fromZigbee`/`toZigbee`) — https://www.zigbee2mqtt.io/advanced/support-new-devices/01_support_new_devices.html ; external converters — https://www.zigbee2mqtt.io/advanced/more/external_converters.html.
- `zigbee-herdsman-converters` license (MIT) — https://github.com/Koenkk/zigbee-herdsman-converters/blob/master/package.json ; `zigbee-herdsman` (MIT) — https://github.com/Koenkk/zigbee-herdsman.
- Zigbee2MQTT application (GPL-3.0; distinct from the data) — https://www.zigbee2mqtt.io/.
- `zha-device-handlers` quirk model (Signature/replacement "translator"; v1 `CustomDevice` vs v2 `QuirkBuilder`/`TuyaQuirkBuilder`; Apache-2.0) — https://github.com/zigpy/zha-device-handlers ; `zha-quirks` — https://pypi.org/project/zha-quirks/.
- deCONZ DDF format (JSON descriptors; `subdevices`/`items`; generic-items inheritance merge; `read`/`write`/`parse` with `fn` + `eval` JavaScript via QJSEngine + named C++ fns + external JS) — https://dresden-elektronik.github.io/deconz-dev-doc/modules/ddf/ ; DDF REST docs — https://dresden-elektronik.github.io/deconz-rest-doc/endpoints/ddf/.
- `deconz-rest-plugin` license (BSD-3-Clause) — https://github.com/dresden-elektronik/deconz-rest-plugin.
- Home Assistant entity model + `supported_features` (root-`Entity` bitmask; runtime-mutable; custom integrations cannot define features) — https://developers.home-assistant.io/docs/core/entity/ ; HA architecture discussion #1320 — https://github.com/home-assistant/architecture/discussions/1320 ; HA core license (Apache-2.0) — https://github.com/home-assistant/core/blob/dev/LICENSE.md.
- Matter Device Library (device type ID + revision + mandatory/optional clusters w/ conformance; cluster = attrs/commands/events, "interface/object class") — CSA Matter Device Library Spec v1.2 https://csa-iot.org/wp-content/uploads/2023/10/Matter-1.2-Device-Library-Specification.pdf ; Matter data-model primer — https://developers.home.google.com/matter/primer/device-data-model ; connectedhomeip (Apache-2.0) `matter-devices.xml` — https://github.com/project-chip/connectedhomeip/blob/master/src/app/zap-templates/zcl/data-model/chip/matter-devices.xml.

**UNVERIFIED / honest flags:**
- The current production maturity/coverage of deCONZ DDF vs its legacy C++ device code is **UNVERIFIED** (the dev-doc page is labeled draft; DDF tooling/bundles indicate production use, but exact coverage was not primary-verified). Treated as "shipping, maturing."
- The "~60% standard / ~40% custom" device-category split is an **internal figure** (Doc 08 §3.6 "from competitive research" / V2-B), not independently re-verified this session; used only directionally.
- The `exposes`→capability mapping being "modest" on real silicon is **INFERENCE (MED-HIGH)** — the recorded D5 re-open trigger; PENDING Stream A bench validation.
- Confirmation-block consequences for specific devices (Hue CONFIRMABLE, Xiaomi BEST_EFFORT, write-only UNCONFIRMABLE) are **INFERENCE** from the `access`/reporting FACTs; the device-specific verdicts are `[CONFIRM-ON-BENCH]`.
