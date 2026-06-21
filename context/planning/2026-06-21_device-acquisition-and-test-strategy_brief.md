<!--
file: context/planning/2026-06-21_device-acquisition-and-test-strategy_brief.md
purpose: The #0 schedule-critical deliverable — the device-acquisition + test/validation strategy for V1 (the real-Zigbee hero demo + the 72h stability run), plus the Matter/MQTT/Thread future-proofing research Nick asked for. Assembles options + a recommendation; the hardware spend + the multi-integration purchase are Nick's calls (escalation at the end).
audience: Nick (approves the spend + the future-proofing call), PM hub (sequences M9 + the validation window against it), the future M9 Zigbee lane, the Distribution lane (first-run/device-pairing wizard)
state-type: planning / decision-support (research brief + escalation)
status: AUTHORED 2026-06-21 (v3 hub). Zigbee spec hub-verified vs Locked Doc 08 §3.2–3.5 + the integration-zigbee scaffold (carried from the V1 record D-OPEN-1/2); current prices/availability + the Thread/Matter angle web-verified 2026-06-21. NOT ordered — awaiting Nick's spend approval.
anchors: context/decisions/2026-06-20_V1-launch-scope_decision-record.md (D-OPEN-1/2/3 RESOLVED; the Nov-25 backward schedule; the Oct 12–25 validation window); homesynapse-core-docs/design/08-zigbee-adapter.md (the two coordinator transport paths; the ZCL cluster table §3.5); homesynapse-core-docs/design/05-integration-runtime.md (multi-protocol — the seam Matter/MQTT would later use); homesynapse-core-docs/design/16-superior-automation.md (the explainability hero view the demo exercises)
-->

# #0 — Device Acquisition + Test Strategy (V1 hero demo + 72h validation)

**One sentence:** buy two coordinators (one per transport path) + a six-archetype curated Zigbee device set this week (~$140–175 all-in), because real-Zigbee + the 72-hour stability run is the longest non-compressible pole on the Nov-25 schedule — every day of procurement lag is a day off the Oct 12–25 validation window, and that window cannot move.

> **✅ RESOLVED 2026-06-21 (Nick) — APPROVED + ORDERING THIS WEEK.** **Q1 = the recommended ~$140–175 bundle** (buy the full bench once; the ~$20–55 delta is noise vs the schedule risk of under-buying and discovering a missing coordinator/device mid-validation, which eats another procurement lead-time cycle). **Q2 = MG24-as-border-router now, Matter/MQTT endpoints deferred** (the MG24 is the V1 EZSP coordinator being bought anyway; choosing it over the MG21 lands Thread/Matter-capable silicon on the bench for ~$10 of silicon choice — endpoints + border-router host software get added when the Matter integration lands post-MVP, never re-buying radio). **MQTT needs no hardware decision** — a software broker (Mosquitto) + a simulatable publisher, stood up when the integration lands. **Strategic principle (Nick) for the "onboard integrations fast near MVP" goal:** the **radio** protocols (Zigbee now, Thread/Matter later) are the ONLY integrations gated by physical silicon + a procurement lead-time pole — front-load those; everything **IP-based** (MQTT, most cloud/LAN integrations) is software spun up on demand, so it is schedule-flexible and can be onboarded fast and late. Sequence integration milestones accordingly. See §6.

**Why this is #0, above all code.** Code can be written in parallel and compressed; hardware cannot. The validation window (Oct 12–25) needs *physical devices on a desk talking to a real coordinator*, and the 72h run is 72 wall-clock hours you cannot shrink, plus fix-and-rerun cycles. If the parts are not in hand well before October, the schedule slips on a dependency that costs $150 and a week of shipping to remove now. **The recommendation: approve the order this week.**

---

## 1. The finalized Zigbee order (ready to buy)

### 1a. Coordinators — one per transport path (de-risks M9's adapter + validates the two-path abstraction)

Locked Doc 08 §3.2–3.3 defines two coordinator transport paths, auto-detected at startup (INV-CE-04 — no manual config selection). Buying one stick per path is cheap insurance: it gives the M9 adapter a real validation target on **both** paths instead of one, so a path-specific bug surfaces in development, not at launch.

| Path | Coordinator | Radio / stack | Why | Price (2026-06-21) | Source |
|---|---|---|---|---|---|
| **Path 1 — ZNP (reference)** | **Sonoff ZBDongle-P** | TI **CC2652P**, Z-Stack/**ZNP** | The reference path; most-deployed, best-documented; the demo runs on this alone | **~$29.90** | ITEAD official (itead.cc) / Amazon |
| **Path 2 — EZSP** | **Sonoff Dongle Plus MG24** (USB) — *upgraded from the v2 spec's ZBDongle-E* | Silabs **EFR32MG24**, **EZSP** (EmberZNet 7.4+ / EZSP v13+) | Validates the EZSP adapter; **and the MG24 doubles as a Thread Border Router** (see §3 — this is the future-proofing answer) | **~$30–35** | sonoff.tech / Amazon |

**Change from the carried v2 spec (deliberate, web-verified):** the v2 record named the **ZBDongle-E (EFR32MG21)** for Path 2. I recommend the **EFR32MG24** part instead (Sonoff Dongle Plus MG24, the official successor to the ZBDongle-E, or the SMLIGHT SLZB-06MG24 if you prefer a PoE/Ethernet coordinator, ~$30–40). Same EZSP path, same EmberZNet ≥7.4 target — but the MG24 (a) has measurably better range/reliability than the MG21 in 2026 home-lab testing, and (b) runs OpenThread/MultiPAN firmware, so it can later serve Matter-over-Thread **on the same stick**. The MG21 cannot do this as well. For one or two dollars more, Path 2 also becomes the Thread future-proofing — so I fold the two questions into one purchase.

Coordinator subtotal: **~$60–70.**

### 1b. Curated device set — the six archetypes (ZCL-standard, off IKEA)

All six map to standard ZCL clusters the device model already expresses (Doc 08 §3.5 cluster table + Doc 02 §3.6 — hub-verified, no gaps). Models are off IKEA TRÅDFRI (wound down 2026 → procurement risk) onto Sonoff + Philips, which pair direct to the coordinator with **no vendor bridge**.

| Archetype | Model | Role in the demo | ZCL surface | Price (2026-06-21) |
|---|---|---|---|---|
| **Dimmable light** | **Philips Hue White A19** (single bulb, no Hue bridge) | The hero **target** (motion → light on) | On/Off + Level Control | ~$15 |
| **Motion** | **Sonoff SNZB-03P** | The hero **trigger** | Occupancy Sensing (IAS Zone) | ~$13–15 |
| **Contact** | **Sonoff SNZB-04P** | Second trigger archetype | IAS Zone | ~$15.90 |
| **Button / scene** | **Sonoff SNZB-01P** | Manual trigger archetype | Scenes / multistate | ~$12 |
| **Smart plug (energy)** | **Sonoff S31 Lite ZB** | Switchable load + energy metering archetype | On/Off (+ Metering) | ~$15–20 |
| **Temp / humidity** | **Sonoff SNZB-02P** | Numeric-attribute archetype (condition tests) | Temperature/Humidity Measurement | ~$16.90 |

Device subtotal: **~$87–95** (one of each). Buy **two motion sensors + two bulbs** (the hero pair — cheap redundancy against a DOA unit blocking the demo build): **~$115–125.**

### 1c. Bottom line

| Bundle | Contents | Total |
|---|---|---|
| **Minimum (demo-sufficient)** | ZBDongle-P + one of each device | **~$120** |
| **Recommended (two paths + hero redundancy)** | Both coordinators + one of each + a spare motion + spare bulb | **~$140–175** |

Lead time: in-stock at Amazon/ITEAD/sonoff.tech; allow ~1 week shipping + a buffer for a DOA swap. **Ordering this week lands everything with ~14 weeks of slack before the Oct 12–25 window — exactly the margin the schedule needs.**

---

## 2. The test / validation protocol

Maps to the V1 record's **Oct 12–25 validation window** (the 72h stability run + fix-and-rerun buffer) and the **by-~Oct-11** "full thin-slice system running + stable enough to validate" gate.

### 2a. Bring-up (as M9 lands, well before October)
1. **Coordinator detection** — plug each stick; confirm the auto-detect picks the right path (ZNP vs EZSP) per INV-CE-04, on each stick independently. This is the two-path abstraction's real test.
2. **Pair each archetype** — interview + pairing + control for all six (Doc 08 interview/pairing flow). Confirm each maps to the expected ZCL clusters and surfaces the expected entities/capabilities in the device model. Log any codec quirk (Tuya/Xiaomi quirks are deliberately OUT of first validation — these six are clean ZCL).
3. **Hero automation** — author **motion (SNZB-03P) → light on (Hue White)**; fire it physically; then open the dashboard hero view and click **"why did this fire?"** — confirm the `RunCausalChain` renders the trigger → condition → action chain correctly end-to-end. *This is the product.* Also build one "why **didn't** it fire?" case (condition not met) to exercise the negative path.

### 2b. The 72h stability run (Oct 12–25 — the non-compressible pole)
- **Setup:** the curated set on the reference coordinator (ZBDongle-P), the hero automation + 2–3 supporting automations live, dashboard polling at 1–2s (no WebSocket in V1).
- **Run:** 72 wall-clock hours continuous. **Acceptance (from the V1 record IN-list):** 72h-stable on the curated set; **zero event loss across a `kill -9`** (event-sourced replay intact); **the event trace explains any state change** (the differentiator's honesty claim, validated against real device traffic).
- **Instrument:** periodic motion events (real PIR + a scripted nudge cadence), a contact open/close loop, temp/humidity drift; capture run outcomes (deterministic terminal state + recorded reason — the run-coupled-reliability surface).
- **Fix-and-rerun buffer:** the back half of the window absorbs one or two fix-and-rerun cycles. A 72h run that fails at hour 60 costs ~3 days to re-validate — which is the whole reason this window is two weeks, not one, and why the hardware must be in hand and exercised *before* October so the October run is a confirmation, not a first attempt.

### 2c. The mid-August go/no-go feeds off this
The V1 record's **mid-August checkpoint** asks: is the engine done, is the explainability view rendering against **real `RunCausalChain` data**, and is hardware validating? "Hardware validating" by mid-August means: **parts in hand, paired, hero automation firing on a real coordinator** — i.e., §2a complete by ~mid-August. That is only possible if the order is placed now. **The hardware timeline is the spine of the go/no-go.**

---

## 3. Future-proofing research — Matter / Thread / MQTT (research-to-inform; V1 stays Zigbee-only)

Nick asked whether to future-proof the test bench for other integrations. **Scope discipline first: Zigbee is the V1 commitment. Matter/MQTT are NOT in V1 scope and this section does not propose pulling them in.** Doc 05 (Integration Runtime) is multi-protocol by design, so the question is narrow: *does a small future-aware purchase now de-risk a later integration milestone without touching V1?*

### 3a. Thread / Matter — **already covered by the Path-2 coordinator choice (near-zero marginal cost)**
The single highest-leverage finding: the **EFR32MG24** coordinator I recommend for the EZSP path (§1a) **is also a Thread Border Router.** With OpenThread (or MultiPAN) firmware it forms a Thread network and connects **Matter-over-Thread** devices — on the *same ~$30 stick* already in the V1 order. So choosing the MG24 over the older MG21:
- costs ~$0–5 extra now,
- validates the V1 EZSP Zigbee path (its V1 job), **and**
- gives a future Matter milestone a working border router with zero new coordinator hardware.

**To actually exercise Matter later** (not now), the only additional purchase would be **1–2 Matter-over-Thread devices** (~$20–40 each — e.g., a Matter contact sensor or plug). My recommendation: **buy the MG24 now** (it earns its place on V1 grounds alone); **defer the Matter device(s)** until a Matter milestone is actually scheduled — buying a Matter sensor today that sits in a drawer until 2027 is the kind of scope-creep spend the V1 record exists to prevent. The border-router capability is the asset worth securing now; the Matter endpoint is a just-in-time buy.

### 3b. MQTT — **a software path; defer the hardware, it's nearly free later**
MQTT in this space is mostly software: an MQTT broker (Mosquitto) is free, and "MQTT devices" are typically WiFi devices speaking native MQTT (Shelly, Tasmota/ESPHome-flashed ESP boards). None of this needs to be bought now to de-risk a later MQTT milestone:
- The broker is a `apt install` when the milestone arrives.
- A representative MQTT device is a single **Shelly Plus** (~$15–20) or a spare ESP32 — also a just-in-time buy.
- Nothing about an MQTT milestone is gated on owning the hardware early (unlike Zigbee, where the radio + the 72h run are the pole).

**Recommendation: no MQTT purchase now.** Note it as a ~$20 just-in-time buy when/if an MQTT milestone is scheduled.

### 3c. Scope guardrail (binds)
V1 ships **Zigbee-only** (D-OPEN-2/3). The MG24's Thread capability is *latent insurance*, not a V1 feature — V1 does not pair a Thread device, does not run a Thread network, does not surface Matter. The V1 OUT-list does not creep IN on the strength of a capable coordinator. Matter/MQTT acquisition beyond the MG24 is **research-to-inform, ruled by Nick, scheduled to its own milestone.**

---

## 4. Escalation to Nick — the spend + the multi-integration call (options + recommendation)

**(A) The hardware spend (blocking the longest pole — decide this week).**
- **Option 1 (RECOMMENDED): the ~$140–175 recommended bundle** — both coordinators (ZBDongle-P + MG24) + the six archetypes + a spare motion sensor + spare bulb. Validates both transport paths, gives hero-pair redundancy, and folds in the Thread future-proofing. Best risk-adjusted spend; it is $150 to remove a schedule-critical dependency.
- **Option 2: the ~$120 minimum** — ZBDongle-P + one of each device. Demo-sufficient, single transport path, no redundancy. Saves ~$40 at the cost of leaving the EZSP adapter unvalidated until later and risking a DOA unit blocking the demo build.
- **Option 3: defer.** Not recommended — every week of delay comes straight off the Oct 12–25 validation buffer; this is the one decision in the plan where waiting is the expensive choice.

**(B) The Matter/Thread/MQTT future-proofing call.**
- **Option 1 (RECOMMENDED): MG24-as-border-router now, Matter/MQTT endpoints deferred.** Take the Thread future-proofing for ~$0 via the coordinator choice; buy no Matter/MQTT devices until those milestones are scheduled. Maximum future-readiness, minimum scope-creep spend.
- **Option 2: add 1–2 Matter-over-Thread devices now** (+~$40–60) to have a Matter target on the bench from day one. Only worth it if a Matter milestone is likely inside the next ~6 months; otherwise it is drawer-spend.
- **Option 3: Zigbee-only, no Thread-capable coordinator** — revert Path 2 to the MG21 ZBDongle-E. Saves nothing meaningful and forfeits the free Thread option. Not recommended.

**PM recommendation: A1 + B1.** Order the recommended bundle this week; take Thread future-proofing for free in the coordinator choice; defer all Matter/MQTT endpoint purchases to their own (Nick-ruled, post-V1) milestones. **Blocking:** the spend is Nick's — no code lane is blocked by it, but the Oct validation window is, so the clock is the reason to decide now.

---

## 5. Downstream consequences once Nick approves (hub will sequence)
- **M9 Zigbee lane** gets a concrete hardware target (both paths) — the adapter is built and bring-up-tested against real sticks, not simulated.
- **Distribution lane** — the first-run/device-pairing wizard (post-M9 ramp) targets this exact curated set; the pairing UX is designed around these six archetypes.
- **The validation window (Oct 12–25)** is now anchored to a real procurement date; the hub tracks "parts in hand → paired → hero firing" as the mid-August go/no-go's hardware evidence.
- **AB-4 before M9 holds** (trust gate) — nothing person-linked writes before the at-rest cipher is live; raw Zigbee device-state maps to non-sensitive scopes, so basic M9 telemetry does not trip the fail-closed boundary on event one (V1 record sequencing rationale).

## 6. The silicon-vs-software integration-sequencing principle (Nick, 2026-06-21 — durable planning rule)
A rule for the post-MVP "onboard integrations fast" goal, surfaced by the future-proofing analysis: **only the radio protocols carry a hardware procurement pole.**
- **Radio (Zigbee, Thread/Matter, Z-Wave, …):** needs physical silicon (a coordinator/radio) with a non-compressible lead time + on-device validation. **Front-load the silicon** — buy the radio early, even if the integration milestone is later (this brief does exactly that: the MG24 lands Thread-capable silicon now, the Matter milestone uses it later). The radio is the schedule-critical, plan-around-it dependency.
- **IP-based (MQTT, Shelly/Tasmota, cloud APIs, most LAN integrations):** software you stand up on demand — a broker is `apt install`, a device is a ~$15 just-in-time buy or a simulator. **No procurement pole; schedule-flexible.** These can be onboarded fast and late, slotted wherever the lane has bandwidth.
- **Sequencing consequence:** order integration milestones so the silicon-gated ones (Thread/Matter, any new radio) trigger their hardware buy at the *start* of their lead-time window, while IP-based ones are treated as drop-in-when-ready. The only thing that ever needs to be "bought ahead" is a radio. This is why the V1 hardware order is #0 and the future MQTT/cloud integrations are not.
