<!--
file: context/assessments/2026-07-03_device-profile-registry_research-dossier.md
purpose: The grounding-before-authoring research dossier the M9.3 coding instruction is authored FROM. M9.3 (interview → ingestion → profile registry) FREEZES the device-profile registry — the highest-consequence freeze in the current arc. Doc 18 §3.5 Locked the CONSTRAINTS; this dossier researches the registry DESIGN SPACE to the Doc-17/Doc-18 dossier bar: primary-source receipts, anti-fabrication tags, per-claim source tables, honest gaps. Research ONLY — designs nothing, authors no instruction, relitigates no ruled decision.
audience: the v16 hub (audits + folds; authors the M9.3 instruction FROM this); Nick (receives framed decision points).
state-type: assessment (research-lane return).
status: COMPLETE — authored 2026-07-03 by the device-profile-registry research lane (fresh Cowork, read-only).
baseline (light preflight, re-derived this lane): core `6ea6912` (M9.2 landed — transport substrate incl. `drainPendingCallbacks()`) · docs `78e0c5c` (Doc 18 DRAFT—REVIEW-FOLDED on disk; §3.5 constraint CONTENT read as-is; the LOCK commit + Nick's OQ-1/N-2 co-sign are PENDING, outside this lane) · hivemind newest = PROJECT_SNAPSHOT beat 63 · bench `5ceff3b` (frozen instrument). Porcelain at write time: 4 pre-existing `M` spine files = the hub's uncommitted beat-63 writes (NOT this lane's — see §Return contract).
internal grounding (truth-outranks-field): homesynapse-core-docs/design/18 §3.5 + §4 · design/08 §3.3–§3.9 · design/02 §3.8/§3.12 · the FROZEN Phase-2 `DeviceProfile.java`(9-comp)/`DeviceProfileRegistry.java` + integration-zigbee MODULE_CONTEXT · nexsys-bench corpus (Hue LCA017, SNZB-03P) + fixtures + the 2026-06-28 device-model/corpus return + the 2026-07-02 plugin-ecosystem-wars dossier (L-22/L-29/L-30 EXTENDED, not re-researched) · governance INV-CE-04/CE-05/INV-PR.
-->

# Device-Profile-Registry Research Dossier — grounding M9.3 before it freezes

## Executive summary

The field has already converged on the registry shape M9.3 needs, and our frozen Phase-2 scaffolds are **most of the way there** — with three concrete gaps this dossier names as AMD needs and one that is the single most consequential finding.

1. **Matching is layered with fingerprint-priority** (Doc 18 §3.5(d) is field-correct). Every serious stack matches an interviewed device by an ordered precedence — exact fingerprint (manufacturerName + modelID + endpoint/cluster signature) **before** a bare model string — with an explicit tie-break priority and a rebrand (white-label) mapping. Our frozen `DeviceProfileRegistry.findProfile(String manufacturerName, String modelIdentifier)` and `DeviceProfile.matches : Set<ManufacturerModelPair>` **cannot express a fingerprint**. Realizing §3.5(d) is an **AMD** (widen the match key to a sealed `MatchCriteria`).
2. **The confirmation moat is not in the frozen record.** The Phase-2 `DeviceProfile` is **9 components** and predates AMD-97 (ratified 2026-07-01). AMD-97's `confirmation[]` block — the schema realization of `confirmed | unconfirmed | failed` — is specified in Doc 08 §3.6 / Doc 02 §3.8 but **absent from the source**. M9.3 must grow the record 9→10 to carry it. This is realizing a *ratified* amendment, but it is a frozen-record arity change — the highest-consequence one-way door in M9.3. **(The brief's "10-component arity note" is a correction target: the source and MODULE_CONTEXT both say 9.)**
3. **Identify vs normalize is already structured correctly.** The frozen `manufacturerCodec` string selector + the sealed `ManufacturerCodec` hierarchy put the repair *code* outside the data path (INV-PROJ-01 / D5), exactly where the field puts it but with our determinism boundary enforced. No AMD — a boundary to state crisply.
4. **Honest degradation is the inviolable rule** and the field validates it: reporting config fails in named, survivable ways (`UNSUPPORTED_ATTRIBUTE` vs `UNREPORTABLE_ATTRIBUTE`, sleepy timeouts, Xiaomi self-schedule). The M9.3 degrade ladder rides AMD-97's `confirmability`/`degradeRule` and `WithinTolerance`; a device that cannot report per spec degrades its confirmability class honestly and **never renders a false `CONFIRMED`** (AMD-97-INV-01).
5. **Performance at scale is a solved pattern**: match-before-full-parse (deCONZ DESC index chunk) + lazy body loading (Z2M compile-time index, measured 54% heap cut on an established network). The registry must load an index at init and resolve full profiles only on interview — keeping registry init off the INV-PR boot budget at 5,000 profiles.
6. **The generic seam is per-protocol-family.** Matter self-describes at commissioning (no quirks corpus); Zigbee needs one. `DeviceProfile`'s Zigbee vocabulary must stay Zigbee-scoped so it never silently becomes the generic profile contract (INV-CE-04) — a future Matter source carries no quirks DB.

The scaling half (Nick's four hub vectors): the corpus **data channel updates out-of-band from code releases** (our user-override file is that seam, reserved by Doc 18 §3.5(d)); the **bench-fixture replay IS our contributed-profile acceptance gate** (the field proves-by-CI; we prove-by-replay-to-recorded-confirmability); the **sleepy-device interview queue is an original design choice** (no upstream precedent found — a differentiator, but validate the adversarial stall against Wave-2); and **identity pins on IEEE while the profile re-matches on every interview** (the OTA-fingerprint-drift case is real and documented — STYRBAR #3135).

Internal grounding outranks the field throughout: the bench corpus + AMD-96/97 are the acceptance spec; the survey is advisory.

## Method + tagging discipline

Env-model first, then a light preflight (baseline above), then internal grounding, then the external survey — deepening (not repeating) the 2026-06-28 corpus return and the 2026-07-02 plugin-ecosystem-wars dossier. Each claim below carries a per-question **source table**: `Claim | Source | Date | Tag`, where **VERIFIED** = a page was fetched and its quote supports the claim, **INFERRED** = reasoning from verified facts, **UNVERIFIED** = could not confirm from a fetched page. **✓✓** marks the load-bearing claims **re-fetched lane-direct** this lane (13 such claims across 5 primary pages the brief flagged as load-bearing; the brief requires ≥6). Prose target ≤ ~8K words; source tables are excluded from the count (the Doc-18 dossier envelope). Every recommendation traces to a Q-finding, checks against the frozen Phase-2 shapes + Doc 18 §3.5, and **names every AMD need** rather than assuming one.

---

## Q1 — Matching model: lightweight vs deep signature vs layered

**Finding — the field is unanimously LAYERED with fingerprint-priority.** Z2M's `findDefinition` is the clearest primary source: candidates are gathered by `modelID`, then *"First try to match based on fingerprint, return the first matching one"* runs before *"Match based on fingerprint failed, return first matching definition based on zigbeeModel."* A fingerprint is `modelID + manufacturerName + manufacturerID + per-endpoint {deviceID, profileID, inputClusters, outputClusters}`, carries an explicit `priority` for ties, and `whiteLabel` re-maps vendor/model via its own fingerprint. The Tuya guide states the collision driver in the project's own words: **"Since a lot of Tuya devices use the same modelID, but use different datapoints it's necessary to provide a fingerprint instead of a zigbeeModel"** (✓✓) — all Tuya 0xEF00 devices report `TS0601`, differentiated only by `manufacturerName` (e.g. `_TZE200_d0yu2xgi`). ZHA quirks match a `Signature` (`models_info` + per-endpoint profile/device-type/cluster lists) that must match *"EXACTLY or zigpy will not match them"*; the ambiguous-match failure is real — `MultipleQuirksMatchException` when a built-in and a custom quirk both match — and its built-in-vs-custom precedence was fixed so custom wins (zigpy 0.75.0 / HA 2025.2.0). deCONZ keys on `manufacturername + modelid` (constants like `$MF_IKEA` expand at load) and its documented failure is the **wrong-DDF selection** when the manufacturer name is not properly checked (#5788). Hubitat's fingerprint matching is *"mainly based on the inClusters,"* which the community reports produces *"false positives for completely different devices"* — the "too coarse" end of the spectrum.

**Internal cross-check (outranks the field).** The bench SNZB-03P is a live proof that model-string keying is necessary but not sufficient: the *same* "Sonoff motion" archetype maps to **different capabilities across hardware revisions** — the older SNZB-03 uses IAS Zone (`0x0500` → `motion`, no battery) while the SNZB-03P uses Occupancy (`0x0406` → `occupancy`, adds battery), and the corpus note is explicit that the registry "must key on `(manufacturerName, modelIdentifier)` — not on a blanket 'Sonoff motion → IAS/`motion`' assumption." Even then, the measured SNZB-03P fingerprint carried deltas (`0xFC57`, an enrolled IAS Zone) that a fingerprint match would see and a model-string match would miss. Both Wave-1 devices interviewed on the **generic** path (`quirk_applied: False`) — so fingerprint *disambiguation* is not exercised by Wave-1, only fingerprint *identity*.

**M9.3 recommendation.** Adopt the layered precedence explicitly, mapping onto Doc 18 §3.5(d). Precedence, highest→lowest: **(1)** exact fingerprint (manufacturerName + modelID + endpoint/cluster signature) → **(2)** manufacturerName + modelID exact → **(3)** modelID + manufacturerName-family wildcard (e.g. `TRADFRI*`) → **(4)** generic ZCL, no profile. Within a tier, an explicit `priority` int breaks ties (Z2M precedent). White-label/rebrand mapping is a first-class field (Z2M `whiteLabel`, L-30). **AMD need (named, HIGH consequence — one-way):** the frozen `findProfile(String, String)` + `matches : Set<ManufacturerModelPair>` cannot express tiers (2)–(1)'s fingerprint. Recommend an AMD that makes `matches` a **sealed `MatchCriteria`** — `ExactModel(mfr, model)` | `ModelWildcard(mfr, modelPrefix)` | `Fingerprint(mfr, model, endpoints[])` — with an explicit precedence order + `priority`, and either widens `findProfile` to accept the full `InterviewResult` (which already carries `endpoints`) or adds a fingerprint-aware overload. This is **additive** (the existing model-pair path becomes one sealed variant) and it is exactly what the corpus IR schema-v2 already anticipates (`identity.fingerprint[]`) — only the *emitted* runtime API lags. **Namespace keying (§3.5(b)):** `profileId` is a bare `String` today; reserve the convention now — bare = first-party, `publisher.profile` = third-party, immutable — so third-party sources later are additive rows, not a re-keying (Doc 18 seam 5). This is a naming discipline the M9.3 instruction states, not a schema change (a `String` holds a namespaced id).

| Claim | Source | Date | Tag |
|---|---|---|---|
| Z2M matches fingerprint before zigbeeModel | github.com/Koenkk/zigbee-herdsman-converters `src/index.ts` (findDefinition) | 2026-07-03 | VERIFIED |
| Tuya reuse modelID → "necessary to provide a fingerprint instead of a zigbeeModel" | zigbee2mqtt.io/advanced/support-new-devices/02_support_new_tuya_devices.html | 2026-07-03 | VERIFIED ✓✓ |
| whiteLabel rebrand format `tuya.whitelabel(VENDOR,MODEL,DESC,[MFR])` | zigbee2mqtt.io/advanced/support-new-devices/02_support_new_tuya_devices.html | 2026-07-03 | VERIFIED ✓✓ |
| TS0601 duplicate-fingerprint collision can be unresolvable | github.com/Koenkk/zigbee2mqtt/issues/19864 | 2026-07-03 | VERIFIED |
| ZHA signature must match device EXACTLY | github.com/zigpy/zha-device-handlers `dev/README.md` | 2026-07-03 | VERIFIED |
| `MultipleQuirksMatchException` / built-in-vs-custom precedence, fixed zigpy 0.75.0 | github.com/zigpy/zigpy/issues/1508 | 2026-07-03 | VERIFIED |
| deCONZ wrong-DDF when manufacturer name not checked | github.com/dresden-elektronik/deconz-rest-plugin/issues/5788 | 2026-07-03 | VERIFIED |
| deCONZ match keys manufacturername + modelid (`$`-constants) | dresden-elektronik.github.io/deconz-dev-doc/modules/ddf/ | 2026-07-03 | VERIFIED |
| Hubitat matches mainly on inClusters → false positives | community.hubitat.com/t/.../7773 | 2026-07-03 | INFERRED (community thread, not official docs) |
| SNZB-03/03P: same archetype → different capabilities per hw revision | nexsys-bench/corpus/devices/sonoff-snzb-03p-motion.md | 2026-07-01 | VERIFIED (internal) |

---

## Q2 — Identify vs normalize: does a profile REPAIR, or only SELECT?

**Finding — every model separates identity-match from a transform/repair layer, and the repair is where code lives.** ZHA is explicit: a quirk is *Signature* (identify) + *Replacement* (*"what will actually be used by Zigpy and ZHA to interact with the device"*) — it substitutes `CustomCluster` implementations and, in the README's worked Xiaomi example, *"take[s] the values that are reported on the AnalogInput cluster and publish[es] them to the ElectricalMeasurement cluster"* — literal normalization into a clean ZCL surface. Z2M splits the auto-generated ZCL capability map from the code you add when a device deviates: `fromZigbee`/`toZigbee` converters plus a `configure:` section (*"if the device does not conform... you will have to extend"*). deCONZ expresses per-item transformation declaratively — each item has `read`/`write`/`parse` with an `eval` expression (`Item.val = Attr.val * 254 / 100`), *"the most basic yet powerful approach... without having to implement any C++ code."* SmartThings Edge does the same at driver granularity: a `can_handle` identity gate over `zigbee_handlers`/`capability_handlers` overrides.

**Internal cross-check.** The 2026-06-28 corpus return already ruled the decisive point: *every* adaptive model reserves a code escape hatch, and **where that code lives is the whole game** — our event-sourcing invariants (INV-PROJ-01; the derivation rule is a pure function of `(priorState, envelope)`) force it OUT of the data path. The determinism boundary == the security boundary == the license boundary (data-in / our-code-out). deCONZ's `eval` is the pattern we must *not* borrow.

**M9.3 recommendation.** The profile does **both** — it identifies **and** carries declarative repair data — but the repair *logic* stays in named code. The frozen shape already embodies this correctly and needs **no AMD**: `manufacturerCodec` is a **string selector** (`"tuya_ef00"`, `"xiaomi_ff01"`, `"xiaomi_fcc0"`) that Phase-3 resolves to a sealed `ManufacturerCodec` (`TuyaDpCodec` / `XiaomiTlvCodec`); the declarative tail (`tuyaDatapoints` DPID→attributeKey tables, `initializationWrites` such as the Aqara `0xFCC0/0x0200` decoupled-mode write — our analog of Z2M's `configure`) is data; `clusterOverrides`/`reportingOverrides` are typed override records. **State the boundary crisply in the M9.3 instruction:** the `DeviceProfile` carries selectors + declarative repair data ONLY; any repair that needs *logic* goes to a `ClusterHandler` or a sealed `ManufacturerCodec`, never into the profile as an expression. Forbid any `eval`/script-in-data field (INV-PROJ-01). If a real device needs a repair that neither `clusterOverrides` nor an existing codec expresses, the answer is a **named codec addition**, not a profile schema escape hatch — and that decision routes to Nick (scope), not into data.

| Claim | Source | Date | Tag |
|---|---|---|---|
| ZHA quirk = Signature (identify) + Replacement (interact) | github.com/zigpy/zha-device-handlers `dev/README.md` | 2026-07-03 | VERIFIED |
| Replacement republishes AnalogInput → ElectricalMeasurement (normalize) | github.com/zigpy/zha-device-handlers `dev/README.md` | 2026-07-03 | VERIFIED |
| Z2M `configure:` + fromZigbee/toZigbee are the repair code | zigbee2mqtt.io/advanced/support-new-devices/01_support_new_devices.html | 2026-07-03 | VERIFIED |
| deCONZ item read/write/parse + `eval` transform | dresden-elektronik.github.io/deconz-dev-doc/modules/ddf/ | 2026-07-03 | VERIFIED |
| SmartThings SubDriver `can_handle` = identity gate over handlers | developer.smartthings.com/docs/edge-device-drivers/driver.html | 2026-07-03 | VERIFIED |
| Repair code belongs OUT of the data path (determinism == security == license) | nexsys-hivemind .../2026-06-28_device-model-and-corpus_research-return.md §3.4 | 2026-06-28 | VERIFIED (internal) |
| Frozen `manufacturerCodec` is a string selector; codec resolved Phase-3 | homesynapse-core integration-zigbee MODULE_CONTEXT.md | 2026-07-03 | VERIFIED (internal) |

---

## Q3 — Reporting-config robustness across firmware

**Finding — the ZCL failure surface is named, and every system degrades to polling/readback or the device's own schedule.** The distinction is `UNSUPPORTED_ATTRIBUTE` (attribute not implemented) vs `UNREPORTABLE_ATTRIBUTE` (present but not reportable); a real Z2M case shows `configReport` returning `UNREPORTABLE_ATTRIBUTE` on a Legrand meter while the device *"seem[s] to be working... with basic functionality"* (#7831). Our own stress case is verified: the SNZB-03P `motion_timeout` write *"timed out after 10000ms"* (#29933), attributed by the maintainer to *"sleeping to save battery."* Degrade strategies: SmartThings Edge uses **monitored attributes** that *"automatically issue a read if the attribute hasn't reported within the requested max reporting interval"* (polling fallback) and *removes* an attribute from monitoring on an unsupported/read-failure status; Z2M relaxes/disables reporting (large max interval) or accepts the device schedule (Xiaomi `SKIP_CONFIGURATION`); deCONZ polls sleepy devices. Critically, an OTA update *"re-configure[s] to ensure normal operation (this may overwrite custom reporting intervals with the default values)"* (✓✓) — reporting config is not durable across firmware.

**Internal cross-check.** Doc 08 §3.7 already ratifies the exclusion pattern (`interviewSkips: ["configure_reporting"]` for all Xiaomi/Aqara, which *"silently reject or disconnect"* on Configure Reporting) and the AMD-96 OccupancySensing row notes the SNZB-03P *"report[s] on their own firmware schedule regardless."* The bench Hue shows the timeout consequence: CT batches at ~10s min-interval → measured 6.7–8.4s confirm latency → `recommendedTimeoutMs: 15000`, a per-capability measured necessity. `WithinTolerance` (Doc 02 §3.8) confirms against the **settled** value, not transients (Hue CT re-derives ±1 mired, so `ExactMatch` false-fails).

**M9.3 recommendation.** Define the degrade ladder, tied to AMD-97's `confirmability`/`degradeRule` and `WithinTolerance`: **(1)** Configure Reporting succeeds → `VERIFIED_REPORTS` / `ON_CHANGE` → `CONFIRMABLE`. **(2)** `UNSUPPORTED_ATTRIBUTE` → the attribute is genuinely absent → the capability may be unrealizable → degrade honestly. **(3)** `UNREPORTABLE_ATTRIBUTE`, a Configure-Reporting rejection, or a sleepy timeout → fall to `READBACK_ONLY` or accept the device's own schedule (`interviewSkips: configure_reporting`) → `BEST_EFFORT` (expect honest `UNCONFIRMED` under load). **(4)** No authoritative attribute at all → `UNCONFIRMABLE` → render `UNCONFIRMED` immediately, **never** a false `CONFIRMED` (AMD-97-INV-01, inviolable). The `degradeRule` enum (`NO_REPORT_TIMEOUT_TO_UNCONFIRMED | NACK_TO_FAILED | IMMEDIATE_UNCONFIRMED | CONFIRM_FROM_CACHE_OR_READBACK`) already encodes each rung. **AMD need (the big one, named under Q-cross-ref → see Consolidated §A):** the ladder requires the `confirmation[]` block, which the frozen 9-component `DeviceProfile` does not carry. Also: after an OTA re-interview, reporting config must be **re-applied AND the confirmation class re-characterized** (the fingerprint changed → confirmability may have changed) — ties to Q10.

| Claim | Source | Date | Tag |
|---|---|---|---|
| `UNREPORTABLE_ATTRIBUTE` returned by real Configure Reporting; device still basic-works | github.com/Koenkk/zigbee-herdsman-converters/issues/7831 | 2026-07-03 | VERIFIED |
| SNZB-03P motion_timeout write "timed out after 10000ms"; "sleeping to save battery" | github.com/Koenkk/zigbee2mqtt/issues/29933 | 2026-07-03 | VERIFIED |
| SmartThings monitored attributes = read-if-not-reported (polling fallback); drop on unsupported | developer.smartthings.com/docs/edge-device-drivers/zigbee/device.html | 2026-07-03 | VERIFIED |
| OTA re-configure "may overwrite custom reporting intervals with the default values" | zigbee2mqtt.io/guide/usage/ota_updates.html | 2026-07-03 | VERIFIED ✓✓ |
| ZCL `UNSUPPORTED_ATTRIBUTE` vs `UNREPORTABLE_ATTRIBUTE` spec distinction | ZCL R8 spec (search-surfaced, not fetched as a page) | 2026-07-03 | INFERRED |
| Xiaomi excluded from Configure Reporting; report on own schedule | homesynapse-core-docs/design/08 §3.7 + bench SNZB-03P | 2026-07-01 | VERIFIED (internal) |
| Hue CT batches ~10s → measured 15000ms timeout; TOLERANCE confirms settled value | nexsys-bench/corpus/devices/philips-hue-white-a19.md | 2026-07-01 | VERIFIED (internal) |

---

## Q4 — Profile-format versioning

**Finding — forward-only-with-migration is the survivable path; coexistence beats big-bang.** ZHA's quirks `v1 → v2` rewrite was driven by developer-experience pain, not a technical break: the RFC opens *"Quirks in ZHA are currently a major pain point... exceedingly difficult for new users to create... without knowing intricate details of the ZCL,"* and v2's fluent `QuirkBuilder` *"remove[s] the need to specify a signature dictionary and a replacement dictionary"* and lets a quirk expose entities *"without having to modify ZHA component code in HA core."* Crucially, **v1 and v2 coexist** — v2 shipped as a non-breaking *"New feature"* in the same registry, not a replacement. Z2M took the harder road: `modernExtend` replaced legacy `extend`, and *"Remove legacy extend support"* was a flagged **BREAKING CHANGE** in herdsman-converters v19.0.0 (2024-03-11) — survivable only because the migration was mechanical and the population is a single merged corpus. deCONZ marks maturity with a DDF `status` (`Draft` default → `Bronze`/`Silver`/`Gold`; *"Any Draft DDFs are not considered further"*, *"Gold will automatically be put active upon start"*) and makes its bundles immutable so *"A bundle can't break another one, even if it's using the same external dependencies."*

**M9.3 recommendation.** Ride the AMD-54 `(major, minor)` schema-versioning discipline (DP-18-A: semver + declared compat range + forward-only non-destructive migration + a named deprecation floor). Concretely: the bundled `zigbee-profiles.json` carries a top-level `schemaVersion (major, minor)` the **loader** validates and migrates forward-only; format evolution is additive within a major (new optional fields), with a loader that reads N and N−1 across a major; adopt **coexistence over big-bang** (the ZHA v1/v2 precedent) so an in-place corpus survives a format change. **No per-record AMD** — the loader (not the `DeviceProfile` record) owns the schema version, so the frozen record stays lean. The corpus IR is already `schema-version 2` with a `provenance` block (`upstreamVersion`, `ingestDate`); that provenance/versioning is a corpus-side concern emitted into the artifact header, not the runtime record. DP-18-A alignment holds: the corpus survives format changes forward-only.

| Claim | Source | Date | Tag |
|---|---|---|---|
| ZHA v2 driven by DX pain ("major pain point") | github.com/zigpy/zigpy/discussions/1312 | 2026-07-03 | VERIFIED |
| v2 removes signature/replacement dicts; exposes entities without HA-core edits | community.home-assistant.io/t/.../666460 | 2026-07-03 | VERIFIED |
| v1 + v2 coexist (v2 added as non-breaking new feature) | github.com/home-assistant/core/pull/111176 | 2026-07-03 | VERIFIED |
| Z2M legacy `extend` removed = BREAKING in herdsman-converters v19.0.0 | github.com/Koenkk/zigbee-herdsman-converters/releases/tag/v19.0.0 | 2026-07-03 | VERIFIED |
| deCONZ DDF `status` maturity (Draft/Bronze/Silver/Gold); Draft not processed, Gold auto-active | github.com/dresden-elektronik/deconz-rest-plugin/wiki/DDF-cheat-sheet | 2026-07-03 | VERIFIED |
| deCONZ immutable bundle "can't break another one" | dresden-elektronik.github.io/deconz-rest-doc/endpoints/ddf/ | 2026-07-03 | VERIFIED |

---

## Q5 — Constrained-hardware performance

**Finding — match-before-full-parse + lazy body loading, measured.** deCONZ's `.ddb` bundle is a RIFF container whose **first chunk is `DESC`** — *"This is always the first chunk and allows fast indexing and matching without parsing the whole DDF. It's a JSON file"* (✓✓) — carrying `device_identifiers` *"generated from each combinaison of manufacturername and modelid."* The matcher reads only the descriptor to find the right DDF, and the REST API paginates because *"in future many thousands of bundles may exist."* Z2M's lazy-loading PR (#8471) changed startup from *"Load all definitions into memory on start"* to *"Load pre-built index (mapping zigbeeModel to array of [module, definition index])... built at compile time,"* importing a module only on match and then purging it — measured on an established network at total heap **192 MB → 105 MB (54%)** and cold-start CPU **1948 ms → 1242 ms**, with an RPi 3 user reporting *"~30% RSS decrease."* The index holds **3,781 model keys** (`ts0601` alone maps 271 definitions).

**Internal cross-check.** INV-PR is constitutional: startup-to-functional-dashboard **< 10 s** and steady-state memory **< 512 MB** on the Raspberry Pi 4 validation target; INV-PR-04 mandates the architecture accommodate 1,000 devices *"from day one."* The M9.3 registry init cannot blow the boot budget when the corpus is thousands of profiles.

**M9.3 recommendation.** Two-stage load: **(1)** at init, load a lightweight **index** keyed by `(manufacturerName, modelID)` → profile locator (the deCONZ DESC + Z2M compile-time-index precedent), NOT the full profile bodies; **(2)** resolve/parse a full `DeviceProfile` only on interview match, then cache it (`ZigbeeDeviceRecord.matchedProfileId`). For 5,000 profiles the index is a few thousand string keys (KB-scale); full bodies load lazily. Because fingerprint matching (Q1) is costlier than string keying, **gather candidates by model string first (cheap hash), then disambiguate by fingerprint only within the candidate set** — exactly Z2M's order. **No interface AMD** — the frozen `DeviceProfileRegistry` (`findProfile` / `allProfiles` / `registerProfile`) is agnostic to load strategy; an implementation can lazy-load and `allProfiles()` can stream rather than eagerly materialize. State the index-first shape in the M9.3 instruction (the Phase-3 note "bundled + user-override JSON loading" must adopt it). **Related obligation (Q3/Q5 crossover, from MODULE_CONTEXT M9.3 inheritance):** `drainPendingCallbacks()` parks callback frames in an **unbounded `ArrayDeque`** — M9.3's ingestion unit MUST establish the drain cadence + a bound-with-drop-policy (`WARN` + count) before any live NCP runs, or a chatty network is a slow memory leak against INV-PR-03.

| Claim | Source | Date | Tag |
|---|---|---|---|
| deCONZ DESC first chunk enables "matching without parsing the whole DDF" | github.com/deconz-community/ddf-tools .../bundler/README.md | 2026-07-03 | VERIFIED ✓✓ |
| DESC `device_identifiers` from manufacturername + modelid | github.com/deconz-community/ddf-tools .../bundler/README.md | 2026-07-03 | VERIFIED ✓✓ |
| deCONZ anticipates "many thousands of bundles" (paginated) | dresden-elektronik.github.io/deconz-rest-doc/endpoints/ddf/ | 2026-07-03 | VERIFIED |
| Z2M lazy pre-built compile-time index; import-on-match then purge | github.com/Koenkk/zigbee-herdsman-converters/pull/8471 | 2026-07-03 | VERIFIED |
| Z2M lazy-load measured: heap 192→105 MB (54%), CPU 1948→1242 ms | github.com/Koenkk/zigbee-herdsman-converters/pull/8471 | 2026-07-03 | VERIFIED (author-measured) |
| Z2M index = 3,781 model keys (ts0601 → 271 defs) | github.com/Koenkk/zigbee-herdsman-converters/pull/8471 | 2026-07-03 | VERIFIED |
| INV-PR constitutional: startup <10 s, memory <512 MB, Pi 4 target; 1,000-device architecture | homesynapse-core-docs/governance/Architecture_Invariants_v1.md §9 | 2026-07-01 | VERIFIED (internal) |
| `drainPendingCallbacks()` unbounded deque → M9.3 must bound-and-drain | homesynapse-core integration-zigbee MODULE_CONTEXT.md | 2026-07-03 | VERIFIED (internal) |

---

## Q6 — The Matter-shaped generic seam

**Finding — Matter self-describes at commissioning; no quirks corpus exists or is needed.** The Descriptor Cluster *"describes the Endpoint enumerating its: Server Clusters, Client Clusters, Device Types, Additional Endpoints,"* and *"The Commissioner or Controlling device such as a phone or hub can use the information found on the Descriptor Cluster to model the Device (light, switch, pump, thermostat)"* (✓✓). The `DeviceTypeList` attribute *"is a list of Device Types supported by the Endpoint... It must contain at least one Device Type,"* and Matter is **prescriptive**: *"Each Endpoint implementing a Device Type must implement the mandatory Clusters that define that Device Type."* This is the opposite philosophy from Zigbee's descriptive/adaptive quirks corpus (which exists precisely because manufacturers deviate). The 2026-06-28 return already ruled the posture: borrow Matter's conformance rigor **internally** (Doc 02 §3.10 is already Matter-style composition), do **not** adopt Matter as the corpus mechanism or an MVP dependency.

**M9.3 recommendation.** Concretize Doc 18 §3.5(d)'s "Zigbee-scoped-with-a-general-seam-note": the generic profile contract is **per-protocol-family PROFILE SOURCES** — Zigbee needs a corpus (matched by fingerprint); Matter needs none (self-describes). The frozen `DeviceProfile` is **already physically Zigbee-scoped** (it lives in `com.homesynapse.integration.zigbee`, not a shared/core package) and its vocabulary is ZCL-specific (`ManufacturerModelPair`, `clusterOverrides` keyed by ZCL cluster int, `tuyaDatapoints`, `manufacturerCodec`). The risk is only its *unqualified name* reading as the generic contract. **Recommendation (naming discipline, no AMD required):** the M9.3 instruction adds a javadoc/doc note that `DeviceProfile` is the **Zigbee** profile shape, and that any future cross-protocol "profile" concept is a separate seam (Doc 18 §4 row 5) that does **not** reuse this record — a future Matter integration carries its own near-empty profile source keyed on device-type conformance, never forced through the Zigbee-quirks shape (INV-CE-04 protocol agnosticism). M9.3 must **not** pre-genericize the record (YAGNI; pre-genericizing would itself risk the INV-CE-04 violation §3.5(d) warns against). *(Optional, Nick's call: rename to `ZigbeeDeviceProfile` for maximum clarity — but a frozen-record rename is itself an AMD; the javadoc-scoping note is the cheaper equivalent and is recommended over the rename.)*

| Claim | Source | Date | Tag |
|---|---|---|---|
| Matter Descriptor Cluster lets a controller "model the Device" (no per-device DB) | developers.home.google.com/matter/primer/device-data-model | 2026-07-03 | VERIFIED ✓✓ |
| `DeviceTypeList` "must contain at least one Device Type" (self-declared) | developers.home.google.com/matter/primer/device-data-model | 2026-07-03 | VERIFIED ✓✓ |
| Matter prescriptive: "must implement the mandatory Clusters" | developers.home.google.com/matter/primer/device-data-model | 2026-07-03 | VERIFIED ✓✓ |
| Borrow Matter rigor internally; do not adopt as corpus/MVP dependency | nexsys-hivemind .../2026-06-28_device-model-and-corpus_research-return.md §1.5 | 2026-06-28 | VERIFIED (internal) |
| Frozen `DeviceProfile` is package-scoped to integration-zigbee | homesynapse-core .../integration/zigbee/DeviceProfile.java | 2026-07-03 | VERIFIED (internal) |
| Canonical CSA Core self-description sentence is member-gated (not fetched) | CSA Matter Core spec (member-gated) | 2026-07-03 | UNVERIFIED (grounded on Google primer + CSA Device Library instead) |

---

## Q7 — Corpus update cadence + distribution (thousands-of-devices scaling)

**Finding — the DATA channel updates out-of-band from the CODE release, in every ecosystem.** Z2M ships herdsman-converters via release-please with near-per-merge npm publishing (manifest at `26.77.0`; roughly one release every ~2 days), and its "update without a release" path is **external converters** — a local file that *"work[s] identically to internal converters"* and that you *"just delete... once the new Zigbee2MQTT version is released,"* saveable at runtime via MQTT. ZHA rides Home Assistant's monthly train but offers **`custom_quirks_path`** to *"load custom quirks from a specific folder... without having to manually edit the Python package."* deCONZ is the most decoupled: DDF files **hot-reload** *"when a file changes,"* and a **DDF store** delivers updates *"which doesn't depend on a deCONZ release,"* with REST endpoints to reload a device's DDF and hot-swap bundles at runtime.

**Internal cross-check.** Doc 18 seam 6 (reserved, V1 builds none) already fixes the shape: a plugin/data artifact is a *"versioned, immutable release artifact + static manifest"* carrying `version` + a *"declared core-compatibility range the registry/loader enforces by serving only compatible versions"* — composing LTD-16/INV-CS-04's independent integration-API versioning and LTD-16's additive-only discipline. The corpus IR `provenance` block already pins `upstreamCommit`/`upstreamVersion`/`license`/`spdx`.

**M9.3 recommendation (V1-safe posture — what M9.3 must NOT preclude).** The frozen registry already ships the seam: `DeviceProfileRegistry.registerProfile` + the **user-override file** (`integrations.zigbee.profiles_path`, user > bundled precedence) IS the "update without a core release" channel and IS the first-class third-party **data channel** Doc 18 §3.5(d) reserves — **keep it.** Then, so a later out-of-band update channel is purely additive: **(a)** the corpus is a bundled **data resource**, never compiled into code (already the design); **(b)** the `zigbee-profiles.json` carries the `schemaVersion` header (Q4) so a future updatable artifact can declare compat; **(c)** the M9.3 instruction makes **no choice that couples the corpus to a core release** — no profile IDs hardcoded in code, no profile schema pinned to the core version. Do **not** build the versioned-artifact / compat-range distribution or a hot-reload/store now (Doc 18 seam 6, reserved) — just don't preclude it. **No AMD.**

| Claim | Source | Date | Tag |
|---|---|---|---|
| Z2M external converters = local add without a release; delete after release | zigbee2mqtt.io/advanced/more/external_converters.html | 2026-07-03 | VERIFIED |
| Z2M near-per-merge release cadence (manifest 26.77.0; release-please) | github.com/Koenkk/zigbee-herdsman-converters `.release-please-manifest.json` | 2026-07-03 | VERIFIED |
| ZHA `custom_quirks_path` loads local quirks without editing the package | github.com/home-assistant/core/pull/49143 | 2026-07-03 | VERIFIED |
| deCONZ DDF hot-reload on file change | dresden-elektronik.github.io/deconz-dev-doc/modules/ddf/ | 2026-07-03 | VERIFIED |
| deCONZ DDF store "doesn't depend on a deCONZ release"; REST reload/hot-swap | dresden-elektronik.github.io/deconz-rest-doc/endpoints/ddf/ + /devices/ | 2026-07-03 | VERIFIED |
| Doc 18 seam 6: versioned immutable artifact + declared compat range | homesynapse-core-docs/design/18 §4 row 6 | 2026-07-03 | VERIFIED (internal) |
| Frozen user-override file (`profiles_path`) = the reserved data channel | homesynapse-core-docs/design/08 §3.6 + DeviceProfileRegistry.java | 2026-07-03 | VERIFIED (internal) |

---

## Q8 — Contributed-profile proof discipline

**Finding — the scale gate is automated CI, not deep human review; and a submission carries a captured signature/fixture that must validate.** Z2M's herdsman-converters CI runs `build → check (Biome lint/format) → test (Vitest) → bench` on every PR, plus a required device picture and auto-generated docs — and human review is thin (a sampled device PR merged *"No reviews"*; ~200 PRs/month, L-22). ZHA quirks are pytest-gated with an `assert_signature_matches_quirk` fixture that *"check[s] that a particular device signature matches the corresponding quirk... without needing to go through the pairing process,"* with the signature required to match *"EXACTLY"* and ruff formatting CI-enforced. deCONZ validates DDFs against a JSON schema *"automated via GitHub actions for pull request,"* auto-generates a test bundle, and the bundle even carries a `VALI` validation-result chunk and `SIGN` signatures where *"A DDF bundle which is submitted for testing can be promoted to stable / official by simply adding another signature"* (✓✓). The common theme: a submission must **prove it matches and behaves**, verified automatically.

**Internal cross-check — this maps directly onto our own strongest pattern.** The bench fixtures README is explicit: *"a captured real device event stream is a seeded event log,"* replayed deterministically (the M7.4d `RunPipelineReplaySafetyTest` substrate) so *"each real-world interaction becomes a deterministic, hardware-free regression test."* The corpus two-path pipeline already routes upstream-ingest (Path U) and bench-capture (Path B) through **one human-review gate** (ACCEPT/CORRECT/DEFER/ESCALATE, bench overrides upstream) to **M9 acceptance**: *"the corpus entry is M9's interview/codec acceptance spec; M9 must render the recorded confirmability; the captured fixture replays as the moat regression test."*

**M9.3 recommendation.** **The bench-fixture replay IS our contributed-profile acceptance gate** — the natural, differentiated equivalent of herdsman-converters CI. A submitted profile must PROVE: **(1)** the captured device signature/fingerprint (manufacturerName, modelID, endpoint/cluster set) — validates the MATCH; **(2)** a captured event-stream fixture that replays to the **recorded `confirmability` verdict** — validates NORMALIZE + confirmation (our moat; nobody upstream gates on confirmation semantics); **(3)** IR JSON-schema validation (the deCONZ precedent); **(4)** provenance (source/license/upstreamCommit — the corpus IR block). **M9.3-era shape:** build the fixture-replay acceptance now, internal-only — wire the Wave-1 fixtures (Hue LCA017 confirming path; SNZB-03P read-only event stream) as the acceptance gate, each rendering its recorded confirmability. The community-submission portal + per-version automated scanning is a **later** seam (Doc 18 seam 7 marketplace floor; **not** V1). **No AMD** — this is CI/process over existing bench substrate.

| Claim | Source | Date | Tag |
|---|---|---|---|
| herdsman-converters CI = build/check/test/bench + device picture | github.com/Koenkk/zigbee-herdsman-converters `.github/workflows/ci.yml` + AGENTS.md | 2026-07-03 | VERIFIED |
| Human review thin (sampled PR "No reviews"; ~200 PRs/month) | github.com/Koenkk/zigbee-herdsman-converters/pull/12587 (L-22) | 2026-07-02 | VERIFIED (prior dossier) |
| ZHA `assert_signature_matches_quirk` proves match without pairing | github.com/zigpy/zha-device-handlers `dev/README.md` | 2026-07-03 | VERIFIED |
| deCONZ DDF JSON-schema validation via GitHub Actions + auto test bundle | dresden-elektronik.github.io/deconz-dev-doc/modules/ddf/ | 2026-07-03 | VERIFIED |
| deCONZ bundle promoted to stable "by simply adding another signature"; `VALI` chunk | github.com/deconz-community/ddf-tools .../bundler/README.md | 2026-07-03 | VERIFIED ✓✓ |
| Captured event stream = seeded log = hardware-free regression test | nexsys-bench/fixtures/README.md | 2026-07-01 | VERIFIED (internal) |
| Corpus entry = M9 acceptance spec; fixture replays to recorded confirmability | nexsys-bench/docs/2026-06-28_phase-2_corpus-model...md §4 | 2026-06-28 | VERIFIED (internal) |

---

## Q9 — Sleepy / battery-device interview

**Finding — every stack relies on a wake window, and none automates the resume.** Z2M's canonical instruction on interview failure: *"If it's a battery powered device... Try to keep the device awake by pressing the button of the device (if any) every 3 seconds"* (✓✓); a real interview stall (#13600) is fixed by pressing the button for 5 s during join plus relaxing the reporting interval. deCONZ's End-device Polling wiki documents deep sleepers (Xiaomi RTCGQ11LM *"Polls once per hour"*), that *"When button is pressed once, it polls once,"* and parent-loss recovery on repeated activation. The SNZB-03P reporting-write timeout (#29933) is attributed to the device *"sleeping to save battery."* **Honest gap:** across Z2M / ZHA / deCONZ / SmartThings I found the *manual* wake pattern everywhere but **no primary-source precedent for an automatic pending-interview-resume queue** — so Doc 08 §3.4's queue is an **original HomeSynapse design choice** (a differentiator).

**Internal cross-check.** Doc 08 §3.4 already ratifies the machine: a *"pending interview queue... When a sleepy device sends any frame (including the initial Device Announce), the adapter checks the queue and resumes the interview. Pending interviews expire after 24 hours,"* with a `PARTIAL` interview status carrying whatever metadata was gathered. The bench SNZB-03P validates the *cooperative* path — it is a sleepy end device (`rx_on_when_idle=false`) but *"joined + interviewed promptly on permit-join... no wake-press needed during interview."* The adversarial stall (a device that genuinely sleeps mid-interview) was **not** exercised by Wave-1.

**M9.3 recommendation.** Build the full state machine per Doc 08 §3.4 (ratified): pending-interview queue, resume-on-any-frame, 24-hour expiry with a structured log, and a `PARTIAL` profile the adoption pipeline (Doc 02 §3.12) decides on. The sleepy `reportingPosture: SLEEPY` maps to the AMD-97 `BEST_EFFORT` confirmability leg. **What M9.3 builds vs what waits for Wave-2:** build the queue/resume/partial/timeout policy **now** (ratified; the SNZB-03P woke and completed, so it does not block); mark the **adversarial** sleepy path — an interview that genuinely stalls, and a sleepy device whose confirmation is genuinely `BEST_EFFORT`/unconfigurable — as the **Wave-2 bench validation vehicle** (the sleepy sensor the brief names). Do not gate M9.3 on a stalling device that Wave-1 did not produce. **No AMD** — `InterviewResult.interviewStatus` (frozen, supports `PARTIAL`) and the frozen `AvailabilityTracker` (per-IEEE wake/availability) already carry the state; the queue is adapter-internal Phase-3 implementation.

| Claim | Source | Date | Tag |
|---|---|---|---|
| Z2M: keep battery device awake by pressing button every 3 s | zigbee2mqtt.io/guide/faq/ (Interview fails) | 2026-07-03 | VERIFIED ✓✓ |
| Real sleepy interview stall + button-wake fix | github.com/Koenkk/zigbee2mqtt/issues/13600 | 2026-07-03 | VERIFIED |
| deCONZ deep sleepers; button press = one poll; parent-loss recovery | github.com/dresden-elektronik/deconz-rest-plugin/wiki/End-device-Polling | 2026-07-03 | VERIFIED |
| No upstream precedent for an AUTOMATIC pending-interview-resume queue | (Z2M/ZHA/deCONZ/SmartThings surveyed — manual pattern only) | 2026-07-03 | UNVERIFIED-ABSENCE (our queue is original) |
| Doc 08 §3.4 pending-interview queue + resume-on-wake + 24h expiry + PARTIAL | homesynapse-core-docs/design/08 §3.4 | 2026-07-01 | VERIFIED (internal) |
| SNZB-03P sleepy but interviewed promptly (cooperative path only) | nexsys-bench/corpus/devices/sonoff-snzb-03p-motion.md | 2026-07-01 | VERIFIED (internal) |

---

## Q10 — Identity + rejoin stability

**Finding — identity pins on IEEE; the profile match re-runs on interview; OTA fingerprint-drift is real.** Maintainer-authoritative: *"Zigbee devices can change their network address (but never their ieee address)"* — the NWK short address changes on rejoin, the IEEE/EUI-64 is stable. An OTA update *"treats it similarly to pairing a new device... automatically re-interview to detect new capabilities and re-configure"* (✓✓), and software build IDs are *"optional device attributes... even same model can differ"* (✓✓). The strongest fingerprint-drift case is IKEA STYRBAR #3135: after a firmware update *"The device signature has changed and the current quirk... is not applied. It seems that there is now 0x0004 cluster included, and 0xFC57 is missing from the signature"* (`quirk_applied: false`) — fixed only by delete + re-pair, and the same breakage hit Z2M. Z2M's re-pair matrix confirms the boundary: changing the network key or pan ID **requires** re-pairing; **updating the coordinator firmware does not**.

**Internal cross-check — this is Doc 02's boundary, not the profile registry's.** Doc 02 §3.12: the `DeviceIdentifiers` registry maps `(namespace, value)` → `device_id`, matching is **integration-scoped** (a Zigbee IEEE only compared against Zigbee), and on a match *"the integration re-links to the existing device_id without user intervention... No new adoption event is produced."* Doc 08 §3.4 step 7 makes the IEEE the hardware identifier (namespace `zigbee`); step 6 re-runs the profile match on every interview. The frozen `ZigbeeDeviceRecord.matchedProfileId` (nullable) is the per-IEEE profile **cache**. DP-B ruled deterministic identity **permanent** (a pure function of the type string); §3.13 removal releases hardware identifiers, §3.15 orphaning preserves them.

**M9.3 recommendation — the pin-vs-rematch policy.** **Pin IDENTITY on IEEE** (Doc 02 §3.12, integration-scoped): rejoin / power-loss / NWK-address-change re-link to the existing `device_id` with **no re-adoption and no identity re-interview** — the profile registry **never keys device identity** (that is Doc 02's boundary; state this explicitly so M9.3 does not blur it). **Re-match the PROFILE on every interview** (Doc 08 §3.4 step 6) as a pure function of the *current* interviewed fingerprint: a rejoin with an unchanged fingerprint re-matches the same profile (stable); an OTA that changes the fingerprint (the STYRBAR class) triggers re-interview → the profile **may re-match to a different/no profile**, which is *correct* — the profile follows the device's current behavior while identity stays pinned on IEEE. Persist `matchedProfileId` as a **re-validated cache**, not identity; after an OTA re-interview, **re-match + re-apply reporting config + re-characterize `confirmation[]`** (the fingerprint changed, so confirmability may have changed — Q3 crossover). This is the DP-F re-pair story's M9.4 bench-rehearsal input. **No AMD for identity** (Doc 02 owns it); the frozen `matchedProfileId` slot and `IEEEAddress` bridge are sufficient — the M9.3 instruction states the cache-not-identity semantics and the OTA re-characterize step.

| Claim | Source | Date | Tag |
|---|---|---|---|
| IEEE never changes; NWK address changes on rejoin | github.com/Koenkk/zigbee2mqtt/discussions/15874 | 2026-07-03 | VERIFIED |
| OTA "treats it similarly to pairing a new device... automatically re-interview" | zigbee2mqtt.io/guide/usage/ota_updates.html | 2026-07-03 | VERIFIED ✓✓ |
| software_build_id/date_code optional; "even same model can differ" | zigbee2mqtt.io/guide/usage/ota_updates.html | 2026-07-03 | VERIFIED ✓✓ |
| OTA changed signature → quirk not applied; fix = delete + re-pair (STYRBAR) | github.com/zigpy/zha-device-handlers/issues/3135 | 2026-07-03 | VERIFIED |
| Coordinator-firmware update does NOT require re-pair; network-key change DOES | zigbee2mqtt.io/guide/faq/ | 2026-07-03 | VERIFIED ✓✓ |
| Identity is IEEE-keyed, integration-scoped; rejoin re-links, no re-adoption | homesynapse-core-docs/design/02 §3.12 | 2026-07-01 | VERIFIED (internal) |
| `matchedProfileId` (nullable) is the per-IEEE profile cache; DP-B permanent identity | integration-zigbee MODULE_CONTEXT + design/18 §7 DP-B | 2026-07-03 | VERIFIED (internal) |

---

## Consolidated M9.3 design-constraint recommendations

Each recommendation traces to a Q-finding, checks against the frozen Phase-2 shapes + Doc 18 §3.5, and names any AMD need. **§A–§C are AMD/one-way; §D–§K are build-time constraints inside the frozen shapes.**

**§A — Grow `DeviceProfile` 9→10 to carry AMD-97 `confirmation[]`. (AMD — realizes a ratified amendment; the highest-consequence one-way door.)** *Traces:* Q3, and the moat. *Check:* the frozen record is 9 components (`profileId … tuyaDatapoints, initializationWrites`) and predates AMD-97 (ratified 2026-07-01); AMD-97 specifies the 8-field `confirmation[]` block in Doc 08 §3.6 + Doc 02 §3.8 but it is **absent from source**. M9.3 must add `List<ConfirmationCharacterization> confirmation` (empty for read-only devices), grow the compact-constructor fan-out, and update MODULE_CONTEXT `(9)`→`(10)`. Because AMD-97 already authorizes the slot, this is *realizing* a ratified amendment — but it is a frozen-record arity change, so do it through the AMD-correction discipline (cite AMD-97; it is not a new mint). This is the load-bearing schema for `confirmed | unconfirmed | failed`; freezing `DeviceProfile` at M9.3 **without** it would force a re-amendment.

**§B — Widen the match key to a sealed `MatchCriteria` for fingerprint-priority. (AMD — one-way on the type.)** *Traces:* Q1; Doc 18 §3.5(d). *Check:* `findProfile(String, String)` + `matches : Set<ManufacturerModelPair>` cannot express a fingerprint (endpoints/clusters), which the field ranks **above** model strings and which §3.5(d) mandates. Recommend `matches : Set<MatchCriteria>` where `MatchCriteria` is a **sealed interface** — `ExactModel(mfr, model)` | `ModelWildcard(mfr, modelPrefix)` | `Fingerprint(mfr, model, endpoints[])` — with a documented precedence order + `priority` int and white-label mapping. The sealed-type decision is the one-way door: adopting it now makes `Fingerprint` an additive permit later; leaving `matches` a bare model-pair set makes fingerprints a harder retrofit. The corpus IR already carries `identity.fingerprint[]`, so the data model is ready; only the emitted API lags. Widen `findProfile` to accept the full `InterviewResult` (already carries `endpoints`) or add a fingerprint-aware overload.

**§C — Reserve the namespace convention in the registry key. (Convention now; no schema change.)** *Traces:* Q1; Doc 18 §3.5(a)/(b). *Check:* `profileId` is a bare `String`. Reserve: bare `profileId` = first-party; `publisher.profile` = third-party, immutable by convention; the registry must not collide across namespaces. State it in the M9.3 instruction so later third-party sources are additive rows, not a re-keying (§3.5(b) "key third-party profile sources by namespaced identity from day one"; seam 5).

**§D — Identify + declarative-repair-data in the profile; repair LOGIC in named codecs.** *Traces:* Q2; INV-PROJ-01. *Check:* the frozen `manufacturerCodec` selector + sealed `ManufacturerCodec` already put code outside the data path — correct, no AMD. Forbid any `eval`/script-in-data field; a repair needing logic is a **named codec addition** (Nick-scope), never a profile escape hatch.

**§E — Honest degrade ladder tied to `confirmability`/`degradeRule` + `WithinTolerance`.** *Traces:* Q3. *Check:* rides §A's `confirmation[]`. A device that cannot report per spec degrades its confirmability class honestly; `UNCONFIRMABLE` ⇒ immediate `UNCONFIRMED`, never a false `CONFIRMED` (AMD-97-INV-01, inviolable).

**§F — Index-first, match-before-parse load.** *Traces:* Q5; INV-PR. *Check:* the frozen `DeviceProfileRegistry` is load-strategy-agnostic — load a `(mfr, modelID)` index at init, resolve full bodies lazily on interview, cache in `matchedProfileId`; gather by model string then disambiguate by fingerprint within the candidate set. No AMD.

**§G — Bound-and-drain `pendingCallbacks` before live NCP.** *Traces:* Q5/Q3 crossover; MODULE_CONTEXT M9.3 inheritance; INV-PR-03. *Check:* the unbounded callback deque needs a drain cadence + bound-with-drop (`WARN` + count) in M9.3's ingestion unit.

**§H — Loader-owned `schemaVersion` header; forward-only additive evolution.** *Traces:* Q4; AMD-54 / DP-18-A. *Check:* `zigbee-profiles.json` carries `(major, minor)`; the loader validates/migrates; coexistence over big-bang. No per-record AMD.

**§I — Keep the corpus a bundled data resource + user-override channel; don't couple to a core release.** *Traces:* Q7; Doc 18 seam 6. *Check:* the frozen user-override file is the reserved data channel — keep it; don't hardcode profile IDs or pin the profile schema to the core version. Build no distribution machinery (reserved).

**§J — Fixture-replay is the acceptance gate.** *Traces:* Q8. *Check:* wire Wave-1 fixtures (Hue LCA017, SNZB-03P) as the M9.3 acceptance — each renders its recorded `confirmability`; a submitted profile proves match + fixture-replay + schema + provenance. Internal-only now; community portal is Doc 18 seam 7 (not V1).

**§K — Build the sleepy-interview queue now; keep `DeviceProfile` Zigbee-scoped.** *Traces:* Q9, Q6. *Check:* build the Doc 08 §3.4 queue/resume/partial/timeout machine (ratified; `InterviewResult.interviewStatus` + `AvailabilityTracker` suffice — no AMD); validate the adversarial sleepy `BEST_EFFORT` leg against Wave-2. Add a javadoc note scoping `DeviceProfile` to Zigbee so it never becomes the generic contract (INV-CE-04); do not pre-genericize.

---

## Decision points for Nick

Framed where the choice is genuinely his (one-way doors / scope). The hub authors the M9.3 instruction from these rulings.

**DP-1 — Realize AMD-97 `confirmation[]` into `DeviceProfile` at M9.3 (9→10)?** *Evidence:* the moat schema is ratified (AMD-97) but absent from the frozen record; M9.3 freezes `DeviceProfile`. *Options:* **(a)** add it at M9.3 *(recommended)* — it is the `confirmed | unconfirmed | failed` differentiator, ratified and bench-measured (Hue/SNZB values exist); **(b)** defer to M9.4 — risks freezing `DeviceProfile` without the moat, then re-amending a one-way record. *Recommendation:* **(a).** *Mark:* **one-way door** — the record arity freezes at M9.3.

**DP-2 — Adopt the sealed `MatchCriteria` type at M9.3, even though Wave-1 doesn't exercise fingerprint disambiguation?** *Evidence:* Doc 18 §3.5(d) mandates fingerprint-priority; both Wave-1 devices matched on the generic path (`quirk_applied: False`), so only fingerprint *identity*, not *disambiguation*, is exercised now; the first real collider is a Tuya `TS0601` (Wave-2+). *Options:* **(a)** introduce the sealed `MatchCriteria` now, populate `ExactModel`/`ModelWildcard`, **reserve** `Fingerprint` *(recommended)* — satisfies §3.5(d)'s precedence + non-preclusion, keeps `Fingerprint` an additive permit; **(b)** keep `matches` a bare model-pair set now, add fingerprints later — cheaper now, but a harder AMD when a collider arrives. *Recommendation:* **(a)** — the sealed-type choice is the real one-way door; the populated variants can grow additively. *Mark:* **one-way door** on the match-key type.

**DP-3 — M9.3 build line: Wave-1 ratified scope vs Wave-2-validated legs.** *Evidence:* Wave-1 (Hue, SNZB-03P) exercises the cooperative interview + generic match + measured confirmation; it does **not** exercise the adversarial sleepy stall, fingerprint disambiguation, a manufacturer codec (Tuya/Xiaomi), or OTA fingerprint-drift. *Options:* **(a)** M9.3 builds the ratified machine (interview queue, degrade ladder, index-first load, identity pin/rematch) and gates acceptance on Wave-1 fixtures, marking the codec/sleepy-BEST_EFFORT/OTA-rematch legs as Wave-2 bench-validated *(recommended)*; **(b)** expand M9.3 to build+prove the codec/adversarial legs now, without hardware to validate them. *Recommendation:* **(a)** — the bench is the acceptance oracle; don't freeze behavior no Wave-1 device can prove. *Mark:* **scope.**

*(Not surfaced as decisions — resolved by recommendation: §C namespace convention, §D codec boundary, §F–§K build constraints. The `ZigbeeDeviceProfile` rename (§K) is noted as an optional Nick call but the javadoc-scoping note is recommended as the cheaper equivalent.)*

---

## Honest gaps + corrections to this brief

**Corrections to the brief (source-verified):**
- **"10-component `DeviceProfile` arity note" → the source is 9.** The frozen `DeviceProfile.java` and MODULE_CONTEXT both say **9** components; AMD-97's `confirmation[]` would be the 10th but is **not yet in source** (§A). The brief likely counted the anticipated block; the correction matters because adding it is the load-bearing AMD.
- **`MultipleQuirksMatchException` #1508 lives in `github.com/zigpy/zigpy`, not `zha-device-handlers`.** Content matches the brief (built-in-vs-custom v2 precedence, fixed zigpy 0.75.0 / HA 2025.2.0).
- **deCONZ "#5788" verified as expected** (wrong-DDF when the manufacturer name is not checked), in `dresden-elektronik/deconz-rest-plugin`.

**Honest gaps (research limits):**
- **No upstream precedent for an automatic pending-interview-resume queue** (Q9). Every surveyed stack documents only the manual wake pattern; Doc 08 §3.4's queue is an original design choice — a differentiator, but its adversarial-stall behavior is unvalidated (Wave-1 devices woke cooperatively). Validate on Wave-2.
- **Matter's canonical self-description sentence is member-gated** (Q6). The CSA Core spec was not fetched; the conclusion rests on the official Google Matter primer (✓✓) + the CSA Device Library — strong, but not the single CSA Core sentence.
- **Hubitat "too coarse"** (Q1) is from a community feature-request thread, not official Hubitat docs (INFERRED).
- **ZCL `UNSUPPORTED_ATTRIBUTE` vs `UNREPORTABLE_ATTRIBUTE` spec wording** (Q3) is INFERRED; the *runtime* `UNREPORTABLE_ATTRIBUTE` status is VERIFIED (#7831), but the formal ZCL R8 spec sentence was not fetched as a page.
- **Z2M "~200 PRs/month"** (Q7) is an estimate; the *release* cadence (near-per-2-days, manifest 26.77.0) is VERIFIED, the exact per-month PR count is not.
- **`priority` field on Z2M fingerprints** (Q1) is read from source-code structure; treated as VERIFIED-from-code, not from narrative docs.

---

## Return contract (env-model §10 audit + refuse-to-close)

**Write-isolation audit (env-model §10).** This lane's entire write surface is **exactly 1 new file**:
`nexsys-hivemind/context/assessments/2026-07-03_device-profile-registry_research-dossier.md` (this file). Zero repo writes elsewhere; zero shared-file appends (the hub folds this return).

- **Inventory (lock-free porcelain at write time):** `nexsys-hivemind` showed **4 pre-existing `M` files** — `context/handoff/cross-agent-notes.md`, `context/handoff/pm-handoff.md`, `context/planning/phase-3-milestone-backlog.md`, `context/status/PROJECT_SNAPSHOT.md` — **NOT attributable to this lane.** These are the hub's uncommitted **beat-63** spine writes (the masthead stamps them beat-63; the snapshot's own "Next" line schedules their commit). This lane did not open, edit, or stage any of them. After this file is written, porcelain adds exactly **1 untracked** path (this dossier).
- **Expected count:** the prepared host-side command **stages exactly 1 file** (this dossier). If Nick's porcelain shows more than `1 untracked + the 4 known hub-M`, **STOP** — investigate before staging.
- **Ignore/secrets sweep:** N/A — one markdown assessment; no runtime state, build output, tokens, or keys produced or referenced. No server run, no token minted.
- **Commit-message hygiene:** message staged bang-free / backtick-free / inner-quote-free in `ClaudeFolder/_scratch/` for `git commit -F` (env-model §9). Suggested staged file: `_scratch/2026-07-03_hivemind_profile-registry-dossier_commit-msg.txt`; suggested host command (single path):
  `git -C <ClaudeFolder>/nexsys-hivemind add context/assessments/2026-07-03_device-profile-registry_research-dossier.md && git -C <ClaudeFolder>/nexsys-hivemind commit -F <ClaudeFolder>/_scratch/2026-07-03_hivemind_profile-registry-dossier_commit-msg.txt`
  *(the hub may instead fold this dossier into its own beat commit; if so, add the 1 path to that commit's explicit list and bump its stated count by 1.)*

**Refuse-to-close — what the M9.3 instruction still needs beyond this dossier (all outside this lane):**
1. **The Doc-18 LOCK confirmation.** Doc 18 is `DRAFT—REVIEW-FOLDED` on disk; §3.5's constraint *content* is what this dossier validated against (it will not change), but the **LOCK commit + Nick's co-sign of OQ-1 (deprecation floor N) and N-2 (EXT-INV-2 scoping)** are pending. M9.3 issues on Lock.
2. **The CC allow-list verification** (targeted `./gradlew :integration:integration-zigbee:*` allow-listed in the Claude Code session) — flagged repeatedly in the spine as a pre-M9.3 fix; outside this lane.
3. **Nick's rulings on DP-1 / DP-2 / DP-3** (the AMD-97 realization, the sealed `MatchCriteria` one-way door, the Wave-1/Wave-2 build line) — framed above, his to rule; the hub authors the instruction once they are ruled.

*End of dossier. Research only — designed nothing, authored no instruction, relitigated no ruled decision.*
