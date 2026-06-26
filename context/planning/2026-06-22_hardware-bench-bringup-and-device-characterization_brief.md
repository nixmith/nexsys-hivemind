<!--
file: context/planning/2026-06-22_hardware-bench-bringup-and-device-characterization_brief.md
purpose: The pre-M9 execution layer for the (now-ordered) curated hardware — bring up both coordinator paths and characterize every device against ground truth via a reference stack AS THE HARDWARE ARRIVES (before M9), producing a DURABLE device-characterization corpus. The corpus becomes M9's acceptance ground-truth + the regression baseline + the empirical Doc 02/08 validation (fix model gaps now, while cheap) + the generalizable method for every future protocol (Matter/MQTT/Z-Wave, Doc 05). A parallel, write-isolated, Nick-driven bench thread at ZERO cost to the serial Core path.
audience: Nick (runs the bench — it is physical), the PM hub (reconciles Doc-gap escalations + sequences M9 against the corpus), the future M9 Zigbee lane, the Distribution pairing-wizard lane
state-type: planning / execution brief (extends the #0 acquisition brief)
status: AUTHORED 2026-06-22 (v4 hub). Ruled by Nick: Call-1 = Option 1 (full bench thread + durable corpus; Option 3/pull-M9-forward held as the mid-August contingency only).
anchors: context/planning/2026-06-21_device-acquisition-and-test-strategy_brief.md (the #0 acquisition brief this extends — §2a bring-up, the silicon-vs-software principle §6); context/decisions/2026-06-20_V1-launch-scope_decision-record.md (D-OPEN-1/2 hardware; the Oct 12–25 validation window; the mid-August go/no-go); homesynapse-core-docs/design/08-zigbee-adapter.md (two coordinator transport paths; §3.5 Cluster-to-Capability Mapping; interview/pairing flow); homesynapse-core-docs/design/02-device-model.md (the device model the corpus validates); INV-CE-04 (Protocol Agnosticism in the Device Model); homesynapse-core/integration/integration-zigbee (the M9 scaffold the fingerprints feed); homesynapse-core-docs/design/05-integration-runtime.md (the multi-protocol seam the method generalizes to)
-->

# Hardware Bench Bring-Up + Device-Characterization Brief (pre-M9)

**One sentence.** As the curated hardware lands (two waves), bring up both coordinator paths and characterize every device against ground truth **via a reference stack, now — before M9** — producing a **durable device-characterization corpus** that becomes M9's acceptance baseline, validates the device model (Doc 02/08) against real silicon while fixes are still cheap, and generalizes to every future protocol — all in a parallel, write-isolated, Nick-driven bench thread at **zero cost to the serial Core lane.**

## 0.5 — 2026-06-26 fan-out de-risk addendum (Session A + Session C validation; v6 hub)

Validated, actionable notes for the bench (from the converter-DB feasibility review + the Session C premises check):

1. **For the EZSP/MG24 path, lead with ZHA (bellows) over Zigbee2MQTT.** Z2M's EZSP/Ember support is the *younger/experimental* driver; ZHA's bellows is the more mature EZSP path. If Z2M's `exposes` data capture is wanted, capture identity/clusters on ZHA first, then cross-check.
2. **Record the EmberZNet/EZSP firmware version FIRST**, before pairing — the MG24 is newer silicon and the EZSP protocol-version-mismatch hard-failure class is real (INV-CE-04 fingerprint capture covers it; reinforce).
3. **Naming:** the Wave-1 stick is the **MG24 (EFR32MG24)** — not the older ZBDongle-E (EFR32MG21); Wave-2's ZNP stick is the **ZBDongle-P (CC2652P)**.
4. **Hue:** pairs direct (standard Zigbee); if it won't join, factory-reset (power-cycle sequence or Hue app/Touchlink) and pair close to the coordinator.
5. **High-leverage bonus — empirically validate the §1-D5 converter-DB direction here.** Session A's "adapt-the-data" recommendation rests on Z2M's `exposes` capability model mapping cleanly onto our ZCL-aligned model (assessed MED-HIGH, the one hedge). The bench can **confirm that mapping on real silicon this week** for two devices — capture the Hue A19's and the SNZB-03P's `exposes` and check each maps to a HomeSynapse capability with modest transform. A clean map raises D5's technical-fit confidence; a messy one re-weights toward the curated-subset fallback sooner. Record this verdict in the corpus entry per device.

## 0. What this is, and why now

The #0 acquisition brief got the hardware **ordered**; its §2a framed bring-up as something that happens "as M9 lands." This brief **moves characterization earlier** — to as-it-arrives, before M9 exists — per Nick's Call-1 ruling (Option 1). The reasoning: the hardware is the V1 record's **#1 risk-pole landing early**, but landing early only *helps* if the idle window (now → M9) is converted into risk reduction. **Idle sticks reduce nothing; sticks validated against ground truth do.** By the time the Core lane reaches M9, we want the detection fingerprints, confirmed firmware, and a device model validated against real silicon all waiting — so M9 builds fast against known-good reality instead of discovering surprises at the end, where surprises are most expensive.

This is a **parallel, write-isolated, Nick-driven bench thread.** It writes **no HomeSynapse integration code** — characterization is done with reference stacks (Zigbee2MQTT / ZHA). Its return is **the corpus** (+ any Doc-gap escalation). The serial Core path (M7.2b → M7.3 → causal-read-API → AB-4 → M9) is untouched.

## 1. The deliverable — the durable device-characterization corpus

Not throwaway bring-up notes. A **versioned reference corpus** in the hivemind:

```
project-knowledge/device-corpus/
  README.md                         (index + the entry schema + the Doc 02/08 validation procedure + the method)
  coordinators/
    sonoff-zbdongle-p_cc2652p_znp.md
    sonoff-dongle-plus-mg24_efr32mg24_ezsp.md
  devices/
    philips-hue-white-a19.md
    sonoff-snzb-03p-motion.md
    sonoff-snzb-04p-contact.md
    sonoff-snzb-01p-button.md
    sonoff-s31-lite-zb-plug.md
    sonoff-snzb-02p-temphumidity.md
```

**Each device entry captures** (the corpus schema — scaffolded in the README): device identity (manufacturer, model, the Zigbee **manufacturer code + model identifier** from the Basic cluster, firmware/dateCode); the coordinator path + stick it was characterized on; the reference stack + version; the **full interview** (endpoints → in/out ZCL clusters → attributes with types → reported commands); the **HomeSynapse device-model mapping** (Doc 02 capabilities/entities/attributes + Doc 08 §3.5 cluster→capability) with a **validation verdict (MATCH / GAP)**; the raw interview dump (linked); and the capture date + corpus schema version.

**Each coordinator entry captures:** USB VID/PID, chip, stack + firmware/EZSP version, and the **auto-detect signature** — the ground truth feeding M9's coordinator auto-detection (INV-CE-04) and the `integration-zigbee` scaffold.

**What the corpus is FOR (the four payoffs):**
1. **M9 acceptance ground-truth** — M9's interview/codec must *reproduce* these captured surfaces; the corpus is the acceptance spec, not a simulation.
2. **The regression baseline** — every future device we support is characterized the same way and diffed against this baseline.
3. **The cheap-fix moment for the device model** — if real silicon doesn't match Doc 02/08, that is a **now-fix** (a Doc amendment before M9 builds on a wrong abstraction), not an expensive M9-era discovery.
4. **The generalizable method** — the identical characterization onboards **Matter-over-Thread (on the MG24 border router), MQTT, Z-Wave** later (Doc 05; the silicon-vs-software principle). The corpus is durable integration-onboarding infrastructure, not a one-off.

## 2. The reference-stack approach (ground truth without M9)

Pair + interview the devices with **Zigbee2MQTT or ZHA (Home Assistant)** running on the Sonoff sticks — standard reference stacks, no HomeSynapse code. They expose the coordinator firmware version and the **full device interview** (clusters/attributes/endpoints/commands) — exactly the ground truth M9 must later reproduce. Notes: **no flashing is needed** for characterization (the sticks ship with coordinator firmware) — only update firmware if it is *below* the EZSP ≥ v13 / EmberZNet ≥ 7.4 target (the stack reports the version). Use the **USB extension cable** (already ordered) to distance the stick from host USB3 — a known 2.4 GHz interference mitigation.

## 3. Wave 1 — ✅ RECEIVED 2026-06-23: MG24/EZSP + Philips Hue White-and-Color (2-pack) + 2× SNZB-03P motion + USB extension — DO ALL OF THIS NOW

The **hero pair** (motion → light) is on the desk. The MEANTIME — before Wave 2 arrives and before any M9/M7.4 software exists — is the OPTIMAL window to front-load it. **The MG24/EZSP is a fully-capable Zigbee 3.0 coordinator — it runs the hero demo on its own; do NOT wait on the ZNP stick.** Front-load everything the EZSP path + the hero set can give: the coordinator fingerprint, the EZSP/EmberZNet version, the full device interviews, and **real captured event streams (motion reports, light state changes) saved as durable TEST FIXTURES** (these become M9's acceptance ground-truth AND M7.4's E2E-test inputs — a step from software-E2E toward hardware-in-the-loop). The Hue is **White-AND-Color** (richer than planned: On/Off + Level + Color-Temp + Color — characterize all of it). This builds the corpus AND hardens the repeatable **characterize → corpus → fixture → Doc-02/08-validate → integrate device-onboarding pipeline**, so Wave 2 and every future device/integration flow through it seamlessly (the durable payoff, not just two device entries).

1. **Coordinator bring-up (EZSP / MG24):** connect via the extension cable; capture the fingerprint (USB VID/PID, EFR32MG24, EZSP/EmberZNet version) → `coordinators/` entry; **confirm EZSP ≥ v13 / EmberZNet ≥ 7.4** (update firmware only if below).
2. **Characterize the hero devices** on the EZSP path via the reference stack: **Philips Hue White A19** (confirm it pairs **direct — no Hue bridge**; expect On/Off + Level Control) and **SNZB-03P motion** (expect Occupancy Sensing / IAS Zone). Capture full interviews → `devices/` entries.
3. **Validate vs Doc 02/08 §3.5:** does each device's real cluster/attribute surface map to the capabilities/entities the device model expects? Record **MATCH** or **GAP**. **Any GAP → flag as a now-fix** (escalate to the hub for a Doc 02/08 amendment before M9).
4. **Hero sanity (optional, high-value):** in the reference stack, manually confirm motion → light behaves as the demo needs (device sanity only — this is *not* a HomeSynapse automation).

## 4. Wave 2 — ORDERED (sonoff.tech), NOT yet received, no firm ETA: ZBDongle-P/ZNP + SNZB-02P/-01P/-04P + S31

1. **Coordinator bring-up (ZNP / ZBDongle-P):** fingerprint (CC2652P, Z-Stack/ZNP version) → `coordinators/` entry. (The bench originally pegged the ZNP stick as the demo's reference coordinator; since the **MG24/EZSP arrived first and runs the hero on its own, the meantime primary IS the MG24/EZSP**. The cross-path data the bench gathers informs which coordinator the demo ultimately ships on — both paths must work either way, INV-CE-04.)
2. **Characterize the rest of the curated set** on the ZNP path: SNZB-04P contact (IAS Zone), SNZB-01P button (Scenes/multistate), S31 Lite plug (On/Off + Metering), SNZB-02P temp/humidity (Measurement). Interviews → `devices/`; validate vs Doc 02/08; flag gaps.
3. **Both-paths-on-one-host:** with both sticks connected, confirm they coexist and each auto-detects its path independently — the two-path abstraction's real test, and the empirical input M9's auto-detect (INV-CE-04) needs.
4. **Re-characterize the hero pair on the ZNP path** (the demo's reference coordinator) — confirm cross-path consistency.

## 5. How this feeds the Core lane (the payoff at M9)

- M9's **coordinator runtime** (both paths) builds against the captured **fingerprints** (auto-detect, INV-CE-04) instead of guessing.
- M9's **interview/codec** is acceptance-tested against the **corpus** (real cluster/attribute surfaces) — known-good, not simulated.
- **Doc 02/08 gaps are fixed now** (cheap), not discovered at M9 (expensive) — the single most valuable output.
- The **Distribution pairing wizard** (post-M9) targets these exact, characterized archetypes.
- The method + corpus **generalize** to Matter/MQTT/Z-Wave later (Doc 05).

## 6. Guardrails (bind)

- **V1 stays Zigbee-only.** The MG24's Thread capability is latent insurance, not exercised here.
- **This is a bench/characterization thread, not M9.** No HomeSynapse integration code is written; the corpus is captured via reference stacks. M9 remains the Core milestone (sequenced after AB-4).
- **Write-isolation.** The bench returns the corpus (+ any Doc-gap escalation); the hub reconciles gaps into Doc 02/08 (governance) and sequences M9 against the corpus. Zero cost to the serial Core path.
- **AB-4-before-M9 holds** — and note the bench writes nothing to the HomeSynapse log (it uses reference stacks), so there is no trust-gate interaction here at all.

## 7. SPIKE-DC opportunity (queue after Wave 2)

Once both sticks are on one host (Wave 2), the **dual-coordinator design spike** (currently parked ~Aug, pre-M14) has its real-hardware target. Recommend **pulling it earlier as a cheap spike**: validate whether two coordinators on one host behave per Doc 08's two-layer architecture; findings may amend Doc 08. The hub queues SPIKE-DC post-Wave-2.

## 8. Escalation / next

The bench is **Nick-driven** (it is physical). The hub has, with this brief, **scaffolded the corpus** (`project-knowledge/device-corpus/README.md` — index + entry template + validation procedure) so the bench just fills entries in. The hub will: reconcile any Doc 02/08 gap the bench flags (a now-fix amendment), sequence M9 against the corpus, and queue SPIKE-DC after Wave 2. **No blocking dependency on the Core lane** — the bench runs in parallel; the corpus is its write-isolated return.
