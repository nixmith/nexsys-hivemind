<!--
file: context/assessments/2026-06-27_smart-home-ecosystem-currency_research-return.md
purpose: Cited, web-backed CURRENCY refresh (mid-2026) on the three smart-home / ecosystem clusters that steer live HomeSynapse decisions — returns a DELTA + decision-impact assessment for the v8 product hub to reconcile. Scoped to decision-relevance, not survey. Complements (does not re-derive) the established baselines.
audience: the v8 product hub (reconciles this return + folds deltas into AMD-96 / Doc 17 / the V1-scope record / the mid-Aug go/no-go); Nick (relays).
state-type: assessment (research return; write-isolated). Off the M7.4 critical path.
status: RETURNED 2026-06-27 by a fresh write-isolated research session (deep-research vehicle). Read-only on the spine; writes ONLY this file. Mints nothing; edits no design doc; touches no Core code; runs no git. The hub reconciles.
sources-discipline: ANTI-FABRICATION ENFORCED (the SafeGate-citation lesson). Every load-bearing claim is tagged [VERIFIED] (primary source retrieved + linked, with date), [UNVERIFIED] (could not confirm on a primary source — NOT laundered into fact), or [INFERENCE] (own synthesis from verified inputs). The prior-session fabricated "SafeGate 2604.05427" citation was sought and NOT reused. Source table at the end; only links actually opened are cited as VERIFIED.
-->

# Smart-Home / Ecosystem Currency — Research Return (decision-relevant, web-backed)

This refreshes the **current (mid-2026) state** of three clusters that steer live HomeSynapse decisions, and returns a **decision delta** per cluster keyed to the artifact it touches (AMD-96, Doc 17, the V1-scope record, D5, the mid-Aug go/no-go). The HomeSynapse model's knowledge was ~a year stale on these; everything below is from live web search against primary sources. The established baselines were digested first, so this is the **DELTA + currency**, not a re-derivation.

**One-paragraph bottom line.** Two of the three clusters hold and are *reinforced* by mid-2026 ground truth (Matter deferral; converter-DB licensing; the planner→verifier→executor frame; the patent novelty). The **one cluster that moved is the explainability moat** — Home Assistant began *actively closing* the "why didn't it fire?" half on 2026-06-22 (merged to `dev`, not yet shipped), which makes the **mid-Aug positioning the most time-sensitive item in this return**. Two smaller but concrete currency deltas: the EmberZNet/EZSP line has advanced well past the bench's v14 (sizing AMD-96 + the M9 ASH item), and single-chip Zigbee+Thread multiprotocol on the MG24 is now deprecated upstream (narrowing how the Thread seam should be reserved).

---

## 0. Decisions for the hub — ranked by impact

1. **AMEND the explainability positioning before mid-Aug (Cluster 2 → differentiator + mid-Aug positioning + go/no-go).** Home Assistant merged the framework for **durable, separately-bucketed "not-triggered traces"** to `dev` on 2026-06-22 (core #174116 + frontend #52708). The *"why didn't it fire?"* half of the moat is no longer safely describable as "unshipped everywhere." **Re-weight the positioning onto the two halves that still hold** — (a) the durable **`confirmed | unconfirmed | failed` device-confirmation** projection (unaddressed on *every* platform surveyed, open + closed + AI), and (b) **never-evicted-ness as a structural property** (HA's version is still capped/bucketed, not a pure projection). Also **correct a baseline factual error** (HA traces are persisted to disk, not "in-memory/evicted on restart") so no inaccurate claim ships. Time-sensitive; watch the HA 2026.7-line.

2. **AMEND AMD-96 currency + elevate the M9 ASH item (Cluster 1 → AMD-96, M9, hero-bench).** The bench's "EmberZNet 8.0.2 = EZSP v14" is real and is still what **shipping MG24 dongles carry from factory**, but the Silicon Labs SDK line has advanced to **8.2 (EZSP v17, Jun 2025)** and **9.0 (EZSP v18, Mar 2026)**. AMD-96's direction is right; widen its band to a **v14→v18 / EmberZNet 8.0.2→9.0 range** rather than pinning v14. Separately, the **`ASH_ERROR_TIMEOUT` finding is not a one-off** — it is a recognized cluster on factory-8.0.2 MG24 units whose accepted remedy is **reflashing newer NCP firmware**. Promote the M9 "v14/ASH" line to a first-class M9 **and** hero-bench reliability item (the hero demo runs on this exact silicon).

3. **NARROW the reserved Thread/multiprotocol seam (Cluster 1 → reserved multiprotocol seam, wave-1 dongle choice).** Running Zigbee + Thread concurrently on a *single* EFR32MG24 (RCP Multi-PAN) has been **deprecated by Home Assistant (Jul 2025, "multiprotocol is dead") and de-recommended by Silicon Labs** (advises dedicated radios). The Thread seam stays reserved and non-precluding, but reserve it as **"add a dedicated Thread radio later," not "flip the MG24 into dual-stack."** The MG24 remains an excellent *single-protocol* Zigbee coordinator (production guaranteed to ≥2032).

4. **Scope the Q1 patent follow-up + correct a baseline misattribution (Cluster 3 → Doc 17 §7 Q1, claim language).** The Doc 17 novelty — *static type-check of the AI-authored **form** against a sealed permit schema, rejected at load* — surfaced **no blocking patent** in a directional scan (moderate confidence). Before any "only/unique/safest" superlative ships, run the **focused follow-up** the scan flags as under-covered: Samsung/SmartThings 2024–26 filings, `WO2025024326A2`, Apple `US20250077786A1`, and non-US (CN/EP/KR) counterparts. **Correction for the record:** the `US10367652B2 / US9230560B2 / US9614690B2` family is assigned to **Nant Holdings IP LLC, not Nest/Google** — the baseline misattributed it. Counsel-gated superlatives stay gated.

5. **CONFIRM the AIoT safety frame + Doc 17 consensus claim (Cluster 3 → Doc 17).** Planner→verifier/safety-gate→deterministic-executor is *more* firmly the 2026 consensus; all five baseline arXiv papers verified, and the 2026 frontier ("externalized runtime governance" for embodied agents, e.g. arXiv 2604.07833) is HomeSynapse's frame by another name. Optional: cite the new entrants as external validation. No change required; the defensible claim language ("AI is structurally a proposer, statically verified, durably auditable") holds.

6. **CONFIRM D5 / converter-DB — no change (Cluster 1 → D5).** All three datasets remain permissively licensed at current versions (converters **MIT** v26.73.0; herdsman **MIT** v10.5.0; zha-device-handlers **Apache-2.0**); the GPL-3.0 Z2M *app* is confirmed a separate package. No relicensing, CLA, fork, or acquisition. Governance moved toward stability (zigpy → Open Home Foundation). None of D5's recorded re-open triggers fired. Keep the "pin the consumed version + record its license at ingest" hedge.

---

## Cluster 1 — Zigbee / Thread / Matter trajectory + converter-DB health

### 1A. EmberZNet / EZSP currency → **AMEND AMD-96; elevate the M9 ASH item**

**Current state (cited).** The bench's `EmberZNet 8.0.2 = EZSP v14` is accurate for that SDK and is still the **factory firmware on shipping SONOFF Dongle-PMG24 (EFR32MG24) units** (probed as `8.0.2.0 build 397`, EZSP v14, into early 2026) [VERIFIED — z2m #30891 / #31281, 2026]. But Silicon Labs has shipped three lines past it:

| EmberZNet | Simplicity SDK | Date | EZSP | Status |
|---|---|---|---|---|
| 8.0.2 | 2024.6.2 | 2024-09-18 | 0x0E = **v14** | [VERIFIED] |
| 8.1 | 2024.12.1 | 2024-12-16 | 0x10 = **v16** | [VERIFIED] |
| 8.2 | 2025.6.0 | 2025-06-16 | 0x11 = **v17** | [VERIFIED] |
| 9.0 (Zigbee 9.0) | 2025.12.x | 2026-03-25 | 0x12 = **v18** | [VERIFIED] (`latest`) |

EZSP is explicitly **version-negotiated** via the `version` command (ID `0x0000`) and is **not guaranteed backward-compatible** across bumps; `zigbee-herdsman`'s `ember` driver targets **EZSP 13+** and version-gates the NCP it will accept [VERIFIED — Silicon Labs EZSP reference + herdsman PR #918]. EZSP **v15 / 0x0F appears to have been skipped** (the 14→16 jump); no public GA assigns it [UNVERIFIED — absence of a primary statement].

**The `ASH_ERROR_TIMEOUT` finding is a cluster, not a one-off.** z2m **#30891** (opened 2026-02-01, SONOFF Dongle-PMG24, factory 8.0.2/v14, `adapter=ember`) reports repeated `ASH_ERROR_TIMEOUTS` and intermittent `HOST_FATAL_ERROR` on start; it is **Closed** with **no linked Z2M PR** — the reporter points to a *firmware-level* fix (`darkxst/silabs-firmware-builder#243`) [VERIFIED; the **closing reason/date is [UNVERIFIED]** — GitHub's static HTML didn't render the timeline]. It sits among a family of MG24 + factory-8.0.2 reports (#31281 *closed as duplicate of #28743*, #32309, #31754, #30933, #23761) [VERIFIED for #31281; title-level for the rest]. These are **ASH/serial-transport + NCP-runtime** failures (below EZSP), **not** version-negotiation rejections; the community remedy is **reflashing a newer/patched NCP firmware**, not a host-side change [INFERENCE from the issue corpus; no Silicon Labs erratum found — UNVERIFIED as a formal advisory].

**What it changes for HomeSynapse.**
- **AMD-96 (currency amendment): AMEND.** The "acknowledge EZSP v14 / EmberZNet 8.x; name the MG24 dongle" direction is correct, but **express the band as a range (v14→v18 / EmberZNet 8.0.2→9.0)**, noting v14 is the *floor that ships on dongles today* while the SDK current is 9.0/v18 (2026-03-25). Doc 08's `v13/7.4` text is now ~5 EZSP versions stale.
- **M9 (test scope): ELEVATE.** Keep the v14 version-negotiation/ASH test item, but reframe it around the **factory-8.0.2 MG24 ASH-stability cluster** with the **reflash remedy** as an explicit acceptance path. Because the **hero demo runs on this exact silicon**, this is a V1 *reliability* item, not just a currency check: decide whether V1 (a) recommends a specific dongle/firmware, (b) ships/points to a reflashed NCP image, or (c) documents the reflash + an ASH-timeout watch. (Non-precluding either way; this is a hardening call.)

### 1B. Matter trajectory → **CONFIRM the V1 deferral (reinforced)**

**Current state (cited).** **Matter 1.6 shipped 2026-06-17** and is, in CSA's own words, a *focused feature release* that **adds no new device categories** — NFC-based commissioning, **Joint Fabric** (multi-controller co-admin of one network), Thermostat Suggestions, and core/security plumbing [VERIFIED — CSA newsroom, 2026-06-17]. **No Matter 1.7 is announced**; CSA instead kicked off **"Unify 2026,"** an open requirements-gathering process for "what comes next" [VERIFIED — CSA, 2026-06-17]. The mid-2026 practitioner/tracker consensus remains **"fragmented and painful,"** with platforms **2–4 spec versions behind**, multi-admin/Thread-border-router conflicts, feature-stripping, and the grouped-light "popcorn effect" [VERIFIED — terrywhite.com 2026-05-27; matter-smarthome.de 2026-01-03]. The honest counter-signal: Matter is **growing** — **38% of Home Assistant instances**, **750+ certified products**, a rebuilt open-source `matter.js` server, and Thread 1.4 now the BR-cert floor [VERIFIED — HA blog 2026-06-23].

**What it changes for HomeSynapse.**
- **V1-scope record (Matter deferral): CONFIRM.** Every live signal supports "Zigbee-first, defer Matter to post-V1." The spec is in a consolidation phase (nothing you'd *miss* by waiting), the lived interop is still poor, and there's no imminent target to build against. The growth signal argues for **keeping the seam reserved** (which V1 already does) — not for pulling Matter into V1. No re-open.

### 1C. Thread / multiprotocol seam → **NARROW how it's reserved**

**Current state (cited).** **Thread 1.4 is the sole Border-Router certification since 2026-01-01** and mandates **credential sharing** (joining an existing mesh instead of spawning a parallel one), though platform rollout is uneven [VERIFIED — Bitdefender 2025-09-03; Espressif 2026-01-06]. **Decision-critical:** concurrent **Zigbee + Thread on a single EFR32MG24** (RCP Multi-PAN) is effectively dead — **Home Assistant deprecated the Silicon Labs Multiprotocol add-on (Jul 2025) and declared multiprotocol "dead,"** and **Silicon Labs itself flags RCP Multi-PAN as "no longer recommended,"** advising **separate dedicated radios** [VERIFIED — SmartHomeScene 2025-10-04 upd. 2026-02; Silicon Labs multi-PAN docs]. The MG24 itself remains a strong *single-protocol* coordinator (production guaranteed to ≥ April 2032) [VERIFIED — Silicon Labs].

**What it changes for HomeSynapse.**
- **Reserved multiprotocol seam: NARROW (non-precluding).** Reserve the Thread option as **"add a dedicated Thread radio later,"** not **"flip the Zigbee MG24 into a dual-stack coordinator."** The latter architecture is now contraindicated by both the reference platform and the silicon vendor. This refines the wave-1 device-model posture without changing V1 scope.

### 1D. Converter-DB health + licensing → **CONFIRM D5 — no change**

**Current state (cited).** As of 2026-06-27, against the raw `LICENSE`/manifest files:

| Project | License | Version | Source |
|---|---|---|---|
| `zigbee-herdsman-converters` | **MIT** | v26.73.0 (npm ~2026-06-25) | [VERIFIED] raw LICENSE + package.json + npm |
| `zigbee-herdsman` | **MIT** | v10.5.0 | [VERIFIED] raw LICENSE |
| `zha-device-handlers` (`zha-quirks`) | **Apache-2.0** | 1.2.0 (PyPI 2026-04-29) | [VERIFIED] license via `pyproject.toml`; **exact latest version [UNVERIFIED]** (a snippet claimed a 2026-06-24 release) |
| Zigbee2MQTT (the **app**) | **GPL-3.0** | v2.12.0 | [VERIFIED] — a **separate package** that *depends on* the MIT packages |

No relicensing, CLA, copyleft migration, acquisition, or notable maintainer fork surfaced for any of the three [VERIFIED-negative — targeted searches]. Governance moved toward **stability**: `zigpy` (which stewards `zha-device-handlers`) transferred to the **Open Home Foundation**, and ZHA was extracted into a standalone `zha` library — both make the quirks data *more* reusable, not less [VERIFIED — OHF / HA "State of the Open Home" 2025-04-16]. Project health is excellent (SLSA-attested npm publishing; high release cadence) [VERIFIED].

**What it changes for HomeSynapse.**
- **D5 ("adapt-the-data for the declarative core + curated/community fallback"): CONFIRM.** None of D5's recorded re-open triggers fired (no upstream relicensing; no governance threat; the GPL boundary is intact and confirmed separate). Keep the recorded hedge — **pin the consumed version + record its license at ingest time**. The remaining open question is the empirical `exposes`→capability mapping fit (bench Session C), which is unchanged by this currency pass.

---

## Cluster 2 — Durable "why-did / why-didn't / did-it-confirm" explainability moat

### Current state (cited) → **AMEND the positioning (the one cluster that moved)**

**The moat is intact today, but the "why didn't it fire?" half now has a dated, maintainer-led closure trajectory at Home Assistant.** On **2026-06-22**, HA merged to `dev`:
- **core PR #174116** — a `did_not_trigger` callback plus **`TraceBuckets`**, so **persisted "not-triggered traces" cannot be evicted by real runs** (carried through store/restore/save) [VERIFIED]. **Critical caveat:** the commit that actually *emitted* these for entity state-changes was **reverted before merge** (commit `634c7c5`) — so **framework + bucketing + serialization landed, but no built-in trigger emits not-triggered traces yet**; it is plumbing awaiting per-trigger adoption, **in no stable release** [VERIFIED].
- **frontend PR #52708** — the UI for the above [VERIFIED]; and **#51742** (open) — a roadmap-backed per-automation health-status surface [VERIFIED]. A collaborator describes the intended next step as **result-typed buckets (conditions-not-met / aborted / errored)** — i.e., approaching the trigger-never-matched vs condition-false distinction [VERIFIED — HA discussion #3912, 2026-06-24].

**Baseline correction (honesty item).** The baseline's "HA traces are in-memory, evicted on restart" is **partially wrong**: HA **persists traces to disk** (`trace.saved_traces`) [VERIFIED — core #70310]. The load-bearing limits are (a) the **cap** (default 5) and (b) **no trace is created when a trigger never matches**. Any positioning copy must use the *correct* limits, not the in-memory framing, or it repeats the SafeGate error in our own voice.

**The "did the device confirm it acted?" half is unaddressed everywhere.** No platform — open, closed, or AI — surfaces a first-class, durable `confirmed | unconfirmed | failed(reason)` per-action projection [VERIFIED across the survey]. The nearest artifacts are **Hubitat Command Retry** (a *behavior*, not a record) and HA architecture **discussion #740**, which is unanswered since May 2025 and proposes a **transient** expected-state (cleared in seconds) — the *opposite* of a durable projection [VERIFIED].

**The rest of the field holds (one line each):**
- **Hubitat / SmartThings / openHAB / Homey:** no durable "why-not," no confirmation projection; troubleshooting remains ephemeral logs (or staff-only server logs for SmartThings) [VERIFIED].
- **Google Home / Gemini:** durable why-not **confirmed absent** — Google's own docs make the *absence* of an Activity-feed entry the diagnostic method; the feed is ~10-day, state-changes-only [VERIFIED — strongest single piece of evidence].
- **Alexa / Alexa+** and **Apple Home (WWDC 2026):** confirmed absent; AI work is automation *authoring* + transient chat, not durable projection [VERIFIED; some Alexa+ review-site diagnostic claims UNVERIFIED]. Counterfactual "why-not" for smart homes is still an **open research area** (arXiv 2510.03078 bills itself as the *first* such method) [VERIFIED].

**What it changes for HomeSynapse.**
- **Differentiator + mid-Aug positioning: AMEND (time-sensitive).** Stop leading with "nobody can durably tell you *why it didn't fire*" as an absolute — HA is building exactly that half. **Lead instead with the parts that still hold:** (1) the **durable confirmation outcome** (`confirmed/unconfirmed/failed`), unshipped *everywhere*; (2) **never-evicted-as-a-structural-property** (pure projection of the immutable log — HA's version is still capped/bucketed and bolt-on); (3) the **unified tri-state in one durable artifact** (trigger-never-matched + condition-false + device-didn't-confirm) — HA is approaching the first two but has *no* path to the device-confirm leg. Keep the honest-claim discipline ("to our knowledge…," not "the only system").
- **Go/no-go: WATCH-ITEM.** Add a tracked watch on the HA **2026.7-line** for per-trigger `did_not_trigger` emitters graduating from `dev` to stable, and on `TraceBuckets` extending to result-typed buckets. If those ship, the (A) half of the moat closes for the DIY segment; the (B) half remains the durable differentiator.

---

## Cluster 3 — AIoT / LLM-in-home-automation safety frame + patent landscape

### 3A. Planner → verifier/safety-gate → deterministic-executor → **CONFIRM (reinforced)**

**Current state (cited).** The pattern is *more* firmly the 2026 consensus. **OWASP shipped the "Top 10 for Agentic Applications 2026" (2025-12-09)** introducing **"Least-Agency,"** and a **"State of Agentic AI Security & Governance 2.01" (2026-06-01)** [VERIFIED]; Microsoft is operationalizing the list (2026-03-30) [VERIFIED]. **All five baseline arXiv papers resolve and match** their descriptions — VeriMAP (`2510.17109`), Blueprint-First (`2508.02721`), VeriPlan (`2502.17898`), the f-secure IFC design (`2409.19091`), and the plan-then-execute security guide (`2509.08646`) [VERIFIED]; the fabricated **SafeGate `2604.05427` was sought and not reused** [VERIFIED-negative]. The 2026 frontier is **externalized runtime governance** — a dedicated layer between plan and action (policy-check → capability admission → execution monitor → rollback → human override) — most directly **"Harnessing Embodied Agents: Runtime Governance for Policy-Constrained Execution"** (`2604.07833`, Apr 2026), plus `2603.16586`, `2603.06636` (SmartBench), and `2601.04680` (IoTGPT) [VERIFIED]. No credible source advocates moving *away* toward unconstrained autonomous actuation. HA's own **deterministic-first / LLM-fallback** model persists ("Assist handles commands first; only what it can't understand goes to AI"), with **JSON-schema-constrained AI Tasks** and an AI-suggests/human-saves authoring flow [VERIFIED — HA blog 2025-09-11; current 2026.6.3]. (A dedicated **NIST** document naming this exact pattern was **not** found — [UNVERIFIED].)

**What it changes for HomeSynapse.**
- **Doc 17 (consensus claim): CONFIRM.** The frame is the field's consensus, expressed in HomeSynapse's existing architecture. Optionally cite `2604.07833` and the OWASP Agentic work as external validation. No change required.

### 3B. The Doc 17 moat + Q1 patent landscape → **CONFIRM moat; SCOPE the patent follow-up**

**Current state (cited).** A directional, non-legal prior-art scan found **no blocking patent** reading on the Doc 17 novelty — *an AI emits components that expand into a **sealed permit schema**, statically type-checked and **rejected at load** if malformed, verifying the authored **form** (resolves / type-checks / composes), not just plan behavior* [INFERENCE from the scan; **moderate confidence**]. Every adjacent system verifies *plan behavior* (model-checking, constraint-checking, guided decoding) or does *generic* schema/XML validation; the nearest published idea is **research, not a patent** ("Compiled AI: Deterministic Code Generation / Safety Sandwich," `2604.05150` — but it validates at *generation* time against templates/grammar, not the *authored artifact* at *load*) [UNVERIFIED as to patent status — research only]. **Command-confirmation as a mechanic is well-trodden prior art** (Google IoT notification/command family `US11538477 / US11948574 / US12100398`) — do **not** claim novelty there [UNVERIFIED — snippet-level, consistent with baseline]. Durable "why-not"/counterfactual explanation appears **unclaimed** [VERIFIED-directional].

**Baseline correction (for the record).** The "Smart home automation systems and methods" family **`US10367652B2 / US9230560B2 / US9614690B2` is assigned to Nant Holdings IP LLC — NOT Nest/Google** (it covers NL conversational device control) [VERIFIED — assignee read on the patent record]. `US20160259308A1 / US10114351B2` (sensor-driven policy suggestion) **is** Google LLC [VERIFIED].

**What it changes for HomeSynapse.**
- **Doc 17 §7 Q1 (patent search): SCOPE the follow-up.** The novelty appears unclaimed, but the scan is US-biased and snippet-limited. Before any "only/unique/safest" superlative ships, run the focused follow-up on the **under-covered surfaces**: **Samsung/SmartThings 2024–26 filings** (incl. "Routine Creation Assistant"), **`WO2025024326A2`** ("Generative AI for digital workflows" — broad genus), **Apple `US20250077786A1`**, and **non-US (CN/EP/KR) counterparts** — plus account for the **18-month publication lag** (a quiet pending application can't be ruled out). Owner: Nick + counsel; non-V1-gating.
- **Claim language: CONFIRM the gating.** Defensible (architecturally true): **"AI is structurally a proposer, statically verified, durably auditable."** Stay gated until Q1 closes: **"safest AIoT," "can never misfire," "formally verified"** (we do static type-checking against a sealed schema, *not* model-checking).

---

## Non-decision-relevant findings (flagged, one line each)

- Thread 1.4 **credential sharing** is real and demoed cross-ecosystem (SmartThings↔M5Stack), but doesn't change V1 (Thread is post-V1) [VERIFIED — Espressif 2026-01-06].
- **Automerge / CRDT** local-first tooling continues to mature; irrelevant to these three decisions [not re-verified this pass].
- **EU Cyber Resilience Act** reporting obligations begin 2026-09-11 (main provisions 2027-12-11) — a compliance-timeline item, not one of these three clusters [VERIFIED elsewhere; flagged for the right owner].
- HA shipped a **Thread mesh visualizer** and `matter.js`-based Matter Server 9.0 — ecosystem color, no HomeSynapse decision impact [VERIFIED — HA 2026-06-23].
- EZSP **v15/0x0F** appears skipped between 8.0.2 and 8.1 — curiosity, no decision impact [UNVERIFIED].

---

## Source table (claim → source → date → status)

| # | Claim | Source (URL) | Date | Status |
|---|---|---|---|---|
| C1-1 | EmberZNet 8.0.2 = EZSP v14 (0x0E) | silabs.com/documents/public/release-notes/emberznet-release-notes-8.0.2.0.pdf | 2024-09-18 | VERIFIED |
| C1-2 | EmberZNet 8.1 = EZSP v16 (0x10) | silabs.com/documents/public/release-notes/emberznet-release-notes-8.1.1.0.pdf | 2024-12-16 | VERIFIED |
| C1-3 | EmberZNet 8.2 = EZSP v17 (0x11) | docs.silabs.com/sisdk-release-notes/2025.6.0/sisdk-zigbee-release-notes/ | 2025-06-16 | VERIFIED |
| C1-4 | EmberZNet/Zigbee 9.0 = EZSP v18 (0x12), current `latest` | docs.silabs.com/sisdk-release-notes/latest/sisdk-zigbee-release-notes/ | 2026-03-25 | VERIFIED |
| C1-5 | EZSP is version-negotiated (`version` 0x0000), not back-compat-guaranteed | docs.silabs.com/zigbee/8.2.3/sisdk-ezsp-reference-guide/02-emberznet-serial-protocol | obs. 2026-06-27 | VERIFIED |
| C1-6 | herdsman `ember` driver targets EZSP 13+ | github.com/Koenkk/zigbee-herdsman/pull/918 | obs. 2026-06-27 | VERIFIED (title) |
| C1-7 | z2m #30891: MG24 factory 8.0.2/v14, ASH_ERROR_TIMEOUTS, Closed, no linked PR | github.com/Koenkk/zigbee2mqtt/issues/30891 | opened 2026-02-01 | VERIFIED (state); reason UNVERIFIED |
| C1-8 | MG24 ASH-timeout cluster (#31281 dup of #28743, #32309, #31754, #30933, #23761) | github.com/Koenkk/zigbee2mqtt/issues/31281 | obs. 2026-06-27 | VERIFIED (#31281); others title-level |
| C1-9 | EZSP v15/0x0F skipped | (no primary statement found) | — | UNVERIFIED |
| C1-10 | Matter 1.6 = focused release, no new device types; NFC commissioning + Joint Fabric | csa-iot.org/newsroom/matter-1-6-enables-more-intuitive-setup-multi-ecosystem-experiences-and-context-driven-control/ | 2026-06-17 | VERIFIED |
| C1-11 | CSA "Unify 2026" kicked off; no Matter 1.7 announced | csa-iot.org/newsroom/connectivity-standards-alliance-kicks-off-unify/ | 2026-06-17 | VERIFIED |
| C1-12 | Mid-2026 Matter still fragmented; platforms 2–4 versions behind | terrywhite.com/why-matter-still-sucks-in-2026/ ; matter-smarthome.de/en/development/the-matter-standard-in-2026-a-status-review/ | 2026-05-27 ; 2026-01-03 | VERIFIED |
| C1-13 | Matter growing: 38% of HA instances; 750+ certified; matter.js server | home-assistant.io/blog/2026/06/23/the-matter-upgrade-youve-been-waiting-for/ | 2026-06-23 | VERIFIED |
| C1-14 | Thread 1.4 sole BR cert since 2026-01-01; credential sharing mandated | bitdefender.com/en-us/blog/hotforsecurity/thread-1-4-slow-rollout ; developer.espressif.com/blog/2026/01/thread-credential-sharing/ | 2025-09-03 ; 2026-01-06 | VERIFIED |
| C1-15 | Single-chip Zigbee+Thread (MG24 Multi-PAN) deprecated by HA + de-recommended by Silicon Labs | smarthomescene.com/reviews/sonoff-dongle-plus-mg24-zigbee-thread-coordinator-review/ + docs.silabs.com multi-PAN | 2025-10-04 (upd 2026-02) | VERIFIED |
| C1-16 | EFR32MG24 production guaranteed to ≥ April 2032 | silabs.com/wireless/zigbee/efr32mg24-series-2-socs | obs. 2026-06-27 | VERIFIED |
| C1-17 | zigbee-herdsman-converters = MIT, v26.73.0 | raw.githubusercontent.com/Koenkk/zigbee-herdsman-converters/master/LICENSE + npm | ~2026-06-25 | VERIFIED |
| C1-18 | zigbee-herdsman = MIT, v10.5.0 | raw.githubusercontent.com/Koenkk/zigbee-herdsman/master/LICENSE | obs. 2026-06-27 | VERIFIED |
| C1-19 | zha-device-handlers = Apache-2.0 | raw.githubusercontent.com/zigpy/zha-device-handlers/dev/pyproject.toml | obs. 2026-06-27 | VERIFIED; exact version UNVERIFIED |
| C1-20 | Zigbee2MQTT app = GPL-3.0 v2.12.0, separate package depending on the MIT pkgs | raw.githubusercontent.com/Koenkk/zigbee2mqtt/master/package.json | obs. 2026-06-27 | VERIFIED |
| C1-21 | zigpy → Open Home Foundation (de-risking governance) | openhomefoundation.org ; home-assistant.io "State of the Open Home" | 2025-04-16 | VERIFIED |
| C2-1 | HA merged framework for durable not-triggered traces (TraceBuckets); emitter reverted | github.com/home-assistant/core/pull/174116 | merged 2026-06-22 | VERIFIED |
| C2-2 | HA frontend "not triggered traces" UI merged; health-status surface open | github.com/home-assistant/frontend/pull/52708 ; /pull/51742 | 2026-06-22 | VERIFIED |
| C2-3 | Intended next step: result-typed buckets (conditions-not-met/aborted/errored) | github.com/orgs/home-assistant/discussions/3912 | 2026-06-24 | VERIFIED |
| C2-4 | HA traces are persisted to disk (baseline "in-memory/evicted" is wrong); real limits = cap(5) + no-trace-on-never-match | github.com/home-assistant/core/issues/70310 ; home-assistant.io/docs/automation/troubleshooting/ | obs. 2026-06-27 | VERIFIED |
| C2-5 | No durable `confirmed/unconfirmed/failed` projection anywhere; #740 proposes transient state, unanswered since 2025-05 | github.com/home-assistant/architecture/discussions/740 | last 2025-05-29 | VERIFIED |
| C2-6 | Google: absence of Activity-feed entry IS the diagnostic; ~10-day, state-changes-only | support.google.com/googlenest/answer/15765771 | obs. 2026-06-27 | VERIFIED |
| C2-7 | Apple Home WWDC 2026 = cameras + Shortcuts AI authoring, no why-not | applehomeauthority.com/apple-home-gets-its-biggest-update-in-years-at-wwdc-2026/ | 2026-06-09 | VERIFIED (secondary) |
| C2-8 | Counterfactual "why-not" for smart homes = open research (billed "first") | arxiv.org/abs/2510.03078 | 2025 | VERIFIED |
| C2-9 | Hubitat/SmartThings/openHAB/Homey: no durable why-not / confirmation projection | docs2.hubitat.com ; support.smartthings.com/hc/.../360051931952 ; openhab.org/docs/configuration/rules-dsl.html ; community.homey.app | obs. 2026-06-27 | VERIFIED |
| C2-10 | Alexa/Alexa+: durable why-not absent in official materials | aboutamazon.com/news/devices/new-alexa-generative-artificial-intelligence | 2025-02-26 | VERIFIED; review-site diagnostics UNVERIFIED |
| C3-1 | OWASP Top 10 for Agentic Applications 2026 ("Least-Agency") | genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | 2025-12-09 | VERIFIED |
| C3-2 | OWASP State of Agentic AI Security & Governance 2.01 | genai.owasp.org/resource/state-of-agentic-ai-security-and-governance/ | 2026-06-01 | VERIFIED |
| C3-3 | Five baseline papers resolve + match (VeriMAP/Blueprint/VeriPlan/f-secure/plan-then-execute) | arxiv.org/abs/2510.17109 ; /2508.02721 ; /2502.17898 ; /2409.19091 ; /2509.08646 | 2025 | VERIFIED |
| C3-4 | 2026 frontier = externalized runtime governance for embodied agents | arxiv.org/abs/2604.07833 ; /2603.16586 ; /2603.06636 ; /2601.04680 | 2026 | VERIFIED |
| C3-5 | "SafeGate 2604.05427" sought + not reused | (no resolvable page) | — | UNVERIFIED (correctly excluded) |
| C3-6 | HA deterministic-first/LLM-fallback; JSON-schema AI Tasks; AI-suggests/human-saves | home-assistant.io/blog/2025/09/11/ai-in-home-assistant/ | 2025-09-11 | VERIFIED |
| C3-7 | No blocking patent on static type-check of authored FORM vs sealed schema at load | (Google Patents directional scan) | obs. 2026-06-27 | INFERENCE (moderate) |
| C3-8 | Nearest published idea is research, not a patent ("Compiled AI / Safety Sandwich") | arxiv.org/abs/2604.05150 | 2026 | UNVERIFIED as patent (research only) |
| C3-9 | US10367652B2 / US9230560B2 / US9614690B2 = Nant Holdings IP LLC (not Nest/Google) | patents.google.com (assignee field) | obs. 2026-06-27 | VERIFIED |
| C3-10 | US20160259308A1 / US10114351B2 = Google LLC (sensor policy suggestion) | patents.google.com | obs. 2026-06-27 | VERIFIED |
| C3-11 | Command-confirmation mechanic = prior art (Google IoT notification/command family) | patents.google.com (US11538477/US11948574/US12100398) | obs. 2026-06-27 | UNVERIFIED (snippet) |
| C3-12 | Follow-up surfaces under-covered: Samsung/SmartThings, WO2025024326A2, Apple US20250077786A1, non-US | (scan coverage gaps) | — | INFERENCE |
| C3-13 | No dedicated NIST doc naming the pattern found | (not found this pass) | — | UNVERIFIED |

---

*Return complete. The hub reconciles: fold the Cluster-2 positioning amendment into the differentiator + mid-Aug go/no-go (time-sensitive); fold the EZSP-band + ASH-cluster + Thread-seam-narrowing into AMD-96 / M9 / the wave-1 device-model; fold the patent-follow-up scope + the Nant-Holdings correction into Doc 17 §7 Q1; confirm D5 and the Doc 17 consensus claim unchanged. Keep HomeSynapse steered by current ground truth, not year-stale priors.*
