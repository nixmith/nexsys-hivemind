<!--
file: context/assessments/2026-06-23_zigbee-converter-db-license-feasibility_assessment.md
purpose: SESSION A return — Zigbee converter-database license + feasibility review. Determines whether HomeSynapse should adapt/interop an existing Zigbee device-converter database rather than rebuild the device-quirk long tail, and how. The hub folds the recommendation-with-confidence into Decision 4/§1 D5 (converter-DB direction), which is HELD PENDING this return.
audience: PM (v6 hub), Nick. Feeds §1 D5 + M9/device strategy.
state-type: assessment (dispatched-session return — write-isolated per the 2026-06-23 fan-out brief)
status: RETURNED. Authored 2026-06-26 (dispatched Session A executed 3 days after the 2026-06-23 brief; the brief filename is honored so the hub fold-contract holds — see the companion reconciliation memo 2026-06-26_v6-fanout-validation-and-dispatch-reconciliation_PM-memo.md for why the brief partially went stale post the 2026-06-25 §1 ratification, and why Session A specifically remains fully live).
sources-discipline: every license claim is read from the project's own LICENSE / package metadata (primary source), cited inline. FACT vs INFERENCE flagged. Items needing a lawyer's confirmation are called out explicitly. This is engineering due diligence, NOT a legal opinion.
-->

# Session A — Zigbee Converter-Database License + Feasibility Review

## One-paragraph recommendation (the hub folds this into §1 D5) — CONFIDENCE: HIGH on license, MEDIUM-HIGH on technical fit

**Leverage the existing converter database — the license does not block it, and rebuilding is the wrong cost.** The two candidate databases are **permissively licensed** (verified against their actual LICENSE/metadata, not secondary claims): Zigbee2MQTT's `zigbee-herdsman-converters` is **MIT**, the `zigbee-herdsman` library it sits on is **MIT**, and ZHA's `zha-device-handlers` (PyPI `zha-quirks`) is **Apache-2.0**. None is copyleft; all three are compatible with shipping **one closed-or-open commercial runtime across free → paid → enterprise** with only an **attribution/NOTICE** obligation — no source-disclosure, no per-device code release. The only copyleft artifact in this ecosystem is the **Zigbee2MQTT *application*** (GPL-3.0), which HomeSynapse must **not** vendor or link — but that is the app, not the converter data, and we don't need it. Recommended direction: **adapt-the-data (embed a transformed, attributed dataset)** for the declarative core — device identity + the `exposes` capability model + standard ZCL cluster/attribute mappings, which map cleanly onto HomeSynapse's ZCL-aligned capability model — paired with a **curated, prioritized subset + community-contribution path** for the non-declarative long tail (the `fromZigbee`/`toZigbee` transform logic, Tuya's `0xEF00` datapoints, Xiaomi deviations) that is code, not pure data. **Reject runtime-interop** (shipping Node + Z2M as a co-process) for local-first / Pi-class / trust-brand reasons. The one thing that changes the call is a lawyer's read on the Apache-2.0 NOTICE/patent mechanics at enterprise-sublicensing scale and on TS→Java derivative-work boundaries (both assessed LOW risk below). **Net: D5 can move from HELD to a ratified "adapt-the-data + curated-subset fallback" once Nick accepts the attribution obligation and commissions the legal spot-check.**

---

## 1. License confirmation — read from primary sources (FACT)

| Artifact | What it is | License | Source read | Verdict |
|---|---|---|---|---|
| `zigbee-herdsman-converters` | The Z2M device-definition database (the "quirks-as-data" target) | **MIT** | `LICENSE` (© 2018 Koen Kanters) **and** `package.json` `"license": "MIT"` (v26.73.0, read 2026-06-26) | Permissive ✓ |
| `zigbee-herdsman` | The Node Zigbee library (ZNP/EZSP abstraction) under the converters | **MIT** | `LICENSE` (© 2019 Jack Wu, Simen Li, Hedy Wang, Koen Kanters) | Permissive ✓ |
| `zha-device-handlers` (PyPI `zha-quirks`) | ZHA/zigpy quirks — Python device handlers | **Apache-2.0** | `pyproject.toml` `license = { text = "Apache-2.0" }` (branch `dev`, read 2026-06-26) | Permissive ✓ (+ explicit patent grant) |
| **Zigbee2MQTT (the application)** | The end-user MQTT bridge app | **GPL-3.0** | project docs / repo | **COPYLEFT — do NOT vendor or link. Not needed.** |

**The load-bearing distinction (record this):** the brief, the prior-art study, and the §1 D5 lean all say "`zigbee-herdsman-converters` MIT." **That is correct** — verified at the file level. The thing that is GPL-3.0 is the **Z2M application**, a *different package* from the converter database and the herdsman library. HomeSynapse's plan consumes the **MIT converter data + the MIT library's abstractions**, never the GPL app. This is the single most important license fact in the whole question, and it lands in our favor.

**Attribution / notice obligations (FACT):**
- **MIT** (both herdsman packages): you must reproduce the copyright line + the MIT permission notice in "all copies or substantial portions." For an embedded dataset this means shipping a retained-notices/attributions file. Trivial, standard.
- **Apache-2.0** (ZHA quirks, if used): retain copyright/patent/trademark/attribution notices; **propagate any `NOTICE` file** content; state significant changes; includes an **express patent grant** (a *plus* for us — defensive) and a patent-retaliation termination clause. Slightly heavier than MIT but routine.
- **No copyleft, no source-disclosure, no "must keep separable"** obligation attaches to either permissive license. (FACT.)

---

## 2. Commercial compatibility across free → paid → enterprise (FACT + flagged INFERENCE)

**The one-runtime, three-tier model is compatible.** (FACT, modulo the lawyer spot-check in §5.) Permissive licenses (MIT, Apache-2.0) place no restriction on commercial use, on closed distribution, on charging money, or on tiering. We may **embed**, **transform**, **redistribute**, and **sublicense** the converter data inside a proprietary or open HomeSynapse runtime at every tier, provided the attribution/NOTICE travels with it. There is **no obligation to keep the data separable** and **no obligation to release HomeSynapse source**.

- **Copyleft exposure:** NONE, *as long as we never pull in the GPL-3.0 Z2M application code or its GPL-only modules.* (FACT.) The discipline that enforces this: depend only on the `zigbee-herdsman-converters` data + (optionally) reference the MIT `zigbee-herdsman` behavior; never copy from the `Koenkk/zigbee2mqtt` app repo.
- **Mixing MIT + Apache-2.0 in one embedded dataset:** compatible (both permissive; Apache-2.0 is one-way-compatible into Apache/closed). The only mechanical care is **NOTICE propagation** for the Apache-2.0 portion. (FACT; INFERENCE that the mechanics are routine.)
- **Trademark:** neither license grants trademark rights. Device-vendor names embedded in the data ("Philips Hue," "Aqara," "Tuya," "SONOFF") are **nominative/descriptive use** (identifying which physical device a definition matches), which is generally defensible — but "do not imply endorsement" is the rule, and **the "Zigbee" word mark + logo are controlled by the Connectivity Standards Alliance** (certification-gated). Marketing copy, not the data embed, is where this bites. (INFERENCE — confirm with counsel; LOW risk for the data, real for branding claims.)
- **Patent posture:** Apache-2.0's express grant is favorable; MIT is silent on patents (neither grants nor withholds). (FACT.)

---

## 3. Technical fit — can the definitions be consumed as DATA and mapped onto our ZCL-aligned capability model? (FACT + INFERENCE)

**Yes for the declarative core; partially for the long tail.** The two databases differ in how "data-like" they are, and this drives the recommendation.

**`zigbee-herdsman-converters` (the better "quirks-as-data" target).** Each definition (a TS module under `src/devices/*`) carries:
- `zigbeeModel` / `fingerprint` — the device-identity match keys (manufacturer/model/endpoint signature). **Pure data → maps directly to HomeSynapse's device-identity/interview layer.** (FACT.)
- `exposes` — a structured capability declaration (e.g., `light({features:[state, brightness, color_temp, color]})`, `numeric`, `binary`, `enum`, with units/ranges/access flags). **This is, in effect, a capability model**, and it is the highest-value artifact: it maps onto HomeSynapse's ZCL-aligned entity → capability model with modest transformation. (FACT that `exposes` exists and is structured; INFERENCE — MEDIUM-HIGH — that the mapping is modest for standard devices.)
- `meta`, `configure`, `ota` — reporting/binding config + OTA hints. Mostly declarative; some imperative. (FACT.)
- `fromZigbee` / `toZigbee` — **converter FUNCTIONS (JS/TS logic)**, not data: they parse incoming ZCL/raw frames into exposed values and serialize commands outward. **This is the part that is code, not data**, and it is where the device-quirk long tail actually lives (Tuya `0xEF00` datapoint decoders, Xiaomi's non-standard attribute packing). (FACT.)

**`zha-device-handlers` (more code-shaped).** Quirks are Python classes that declare a device `signature` (clusters/endpoints) and substitute **replacement clusters** that normalize the deviating behavior. Excellent as a *cross-check reference* for the same device's quirks, but less directly "data" than Z2M's `exposes`. (FACT.) Useful as a second source to disambiguate a device when the two databases disagree.

**Adaptation effort (INFERENCE, hedged):**
- **Low effort, high coverage:** ingest `zigbeeModel`/`fingerprint` + `exposes` for the standard-ZCL majority (lights, switches, plugs, contact/motion/temp sensors). A declarative transformer turns these into HomeSynapse device-model + capability rows. The Wave-1 devices (Hue A19 RGBW, SNZB-03P) are squarely in this majority — **the bench (Session C) can empirically confirm the `exposes`→capability mapping on real silicon for two devices this week.**
- **The real cost is the transform logic**, not the identity/capability data: the `fromZigbee`/`toZigbee` functions for non-standard devices (Tuya `0xEF00` especially) are logic that must be **re-expressed** in HomeSynapse's model, not merely copied. A declarative subset (standard cluster read/report/command) covers most devices; the Tuya/Xiaomi tail is incremental work.
- **Maintenance/freshness:** the upstream DB updates constantly (v26.73.0 and climbing). An embed needs a periodic re-ingest pipeline + a pinned-version + attribution-provenance discipline. (INFERENCE — this is a real ongoing cost, but far smaller than re-deriving thousands of defs.)

---

## 4. The four options, scored

| Option | What it means | Pros | Cons | Verdict |
|---|---|---|---|---|
| **A. Adapt-the-data (embed/transform)** | Ingest `zigbeeModel`+`exposes`+cluster maps, transform into HomeSynapse's model, embed an attributed dataset; re-express transform logic for the declarative subset | Local-first clean (no extra runtime); fast device coverage; the `exposes` capability model is most of the win; license-clean with attribution | Must build an ingest/transform + provenance pipeline; the `fromZigbee`/`toZigbee` long tail isn't free | **RECOMMENDED for the declarative core** |
| **B. Interop-at-runtime** | Ship Node + Z2M/herdsman as a co-process; call it live | Maximum device coverage "for free"; always current | Heavy runtime on Pi-class; process boundary + IPC; **GPL-3.0 entanglement risk if you reach into the Z2M app**; against the local-first/lean trust-brand posture; explainability/causal-log seam muddied by an opaque external actor | **REJECT** |
| **C. Curated subset + community contribution** | Hand-curate the top-N devices; crowd the long tail | Smallest initial surface; high quality on supported devices; the UX/first-run devices are covered first | Slow to breadth; community flywheel is unproven for a new project; re-derives what already exists upstream | **ADOPT AS THE FALLBACK / for the non-declarative tail** |
| **D. Rebuild from scratch** | Re-derive the device-quirk long tail ourselves | Total control | Multi-year cost, **no differentiation payoff** — the DB is the cost and the moat, and it already exists permissively | **REJECT (the null option the brief set up)** |

**Recommended synthesis: A for the declarative core + C for the long tail.** Embed the transformed, attributed identity+capability data (A) so device breadth comes cheap and license-clean; treat the `fromZigbee`/`toZigbee` non-standard transforms as a prioritized, curated, community-extensible subset (C). Reject B (runtime) and D (rebuild).

---

## 5. What needs a lawyer (call out explicitly — engineering flagged these; counsel must rule)

1. **Apache-2.0 NOTICE + patent-grant mechanics at enterprise-sublicensing scale** — does our enterprise tier's sublicensing model interact with the patent-retaliation clause or the NOTICE-propagation duty? (Assessed LOW risk; confirm.)
2. **TS→Java derivative-work boundary** — porting/transcribing `exposes`/converter logic vs. consuming the data values. Both are permitted under MIT/Apache-2.0 with attribution; counsel should bless the attribution form for a transformed dataset. (LOW risk.)
3. **Attribution mechanics for a bundled dataset of thousands of contributors** — MIT/Apache notices aggregate to a single retained-attributions artifact; confirm the form (per-file provenance vs. a consolidated NOTICE). (LOW risk, routine.)
4. **Trademark / "Zigbee" word mark + the CSA certification posture** — affects marketing/branding language more than the data embed; confirm nominative-use posture for vendor names. (Branding risk, not data risk.)

None of these blocks moving D5 to a ratified direction; they gate the *final embed mechanics*, not the decision.

---

## 6. What would change the call
- A lawyer flags the Apache-2.0 terms as incompatible with a specific enterprise model → drop ZHA from the embed, keep MIT-only Z2M data (still sufficient for the declarative core). 
- The bench (Session C) finds the `exposes`→capability mapping is *not* modest on the Hue/SNZB-03P → re-weight toward option C (curated) sooner; raise the technical-fit risk from MEDIUM-HIGH.
- Upstream relicensing of `zigbee-herdsman-converters` away from MIT (no evidence of this; the GPL-3.0 is the app, historically and currently) → re-open. Pin the consumed version + record its license at ingest time as a hedge.

## 7. Sources
- `zigbee-herdsman-converters` LICENSE (MIT) — https://github.com/Koenkk/zigbee-herdsman-converters/blob/master/LICENSE
- `zigbee-herdsman-converters` package.json (`"license": "MIT"`, v26.73.0) — https://github.com/Koenkk/zigbee-herdsman-converters/blob/master/package.json
- `zigbee-herdsman` LICENSE (MIT) — https://github.com/Koenkk/zigbee-herdsman/blob/master/LICENSE
- `zha-device-handlers` pyproject.toml (`license = "Apache-2.0"`, pkg `zha-quirks`) — https://github.com/zigpy/zha-device-handlers/blob/dev/pyproject.toml
- Zigbee2MQTT is GPL-3.0 (the application, distinct from the converter DB) — https://www.zigbee2mqtt.io/
- Zigbee2MQTT "support new devices" (the `exposes` / converter authoring model) — https://www.zigbee2mqtt.io/advanced/support-new-devices/01_support_new_devices.html
