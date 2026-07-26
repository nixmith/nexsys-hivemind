<!--
file: context/handoff/2026-07-10_integration-roadmap_lane_session_prompt.md
purpose: Session prompt for the integration-roadmap research lane (Track B lane (b) — decision-shaped per Nick's 2026-07-10 ruling: an EXECUTIVE SEQUENCING RECOMMENDATION with trade-offs, not a survey).
audience: a fresh Cowork research lane (write-isolated; returns to the hub for two-layer audit; the REC goes to Nick for the sequencing ruling).
state-type: lane dispatch prompt (one session; retires on return).
status: READY — launch in a FRESH Cowork conversation; attach this file; paste: "Read and follow all instructions contained within the integration-roadmap lane session prompt file."
-->

# Lane Brief — The Integration Roadmap (what follows Zigbee, decision-shaped)

## 0. Mission and authority

You are a RESEARCH LANE for HomeSynapse. The platform's first integration (Zigbee, EZSP-native, built from the radio up) is silicon-certified and soaking. The question Nick needs answered: **which integration(s) come next, in what order, and why — an executive sequencing recommendation with trade-offs stated, not a survey.** Lead with the REC; the survey is its supporting evidence. You are WRITE-ISOLATED: your ONLY repo write is the return file in §4. The hub audits your return; Nick rules on the REC.

## 1. Required reads (the thesis you are sequencing FOR)

1. `nexsys-hivemind/context/strategic-context-map.md` (§2 catalog) — then the strategy docs it points at, minimum: `Six_Battlefields_MVP_Strategy.md` + `Revenue_Model_and_Licensing_Strategy.md` (context/strategy/).
2. `homesynapse-core-docs/design/08-*.md` §3 (the integration architecture — adapter/supervisor model, the confirmation model) and `17-*.md` (AIoT + cloud readiness posture) and `18-*.md` (extension/plugin architecture — third-party integrations arrive HOW?). Skim for the seams, not cover-to-cover.
3. `nexsys-hivemind/context/strategy/2026-07-10_acceptance-arc-positioning-notes.md` — the honesty thesis as proven claims (never-false-CONFIRMED; identity-in-the-log; local-first).
4. `nexsys-hivemind/context/assessments/2026-06-23_smart-home-architecture-prior-art_research-return.md` + `2026-07-02_plugin-ecosystem-wars_research-dossier.md` — prior art already banked; do not re-research what they hold, cite them.

## 2. The candidates + the analysis frame

Candidates: **Matter (+ Thread)** · **Z-Wave** · **local-WiFi devices** (Shelly Gen2 RPC / ESPHome native API / Tasmota — with the Shelly Plus Plug US IN HAND as the concrete case study: 2 units arriving as bench actuators that double as the pilot integration target) · **MQTT bridge** (as an integration class, incl. zigbee2mqtt-bridge implications) · and name any candidate we're wrong to omit.

Per candidate, analyze against THESE axes (decision-shaped, evidence-cited):

1. **Fit to the honesty thesis:** can the protocol carry AUTHORITATIVE state evidence for never-false-CONFIRMED (attribute reports/acks with real device provenance)? Where does Matter's data model + interaction model land on this — does it strengthen or dilute the confirmation moat? Same for Shelly RPC notifications, ESPHome state streams, MQTT retained-message semantics (the honesty trap: retained state ≠ fresh evidence).
2. **Local-first fit:** cloud dependencies, commissioning constraints (Matter's fabric/commissioning flow on a Pi without a phone ecosystem?), Thread border-router hardware reality in 2026.
3. **Market coverage 2026:** what fraction of the devices our users actually own does each unlock; momentum direction (research CURRENT state — certified-device counts, ecosystem announcements; your knowledge may be stale, verify with searches).
4. **Implementation cost on OUR architecture:** map to Doc 08's adapter/supervisor/confirmation seams (a new integration = an IntegrationAdapter + profiles + confirmation characterizations); protocol stack build-vs-embed options (Matter SDK realities for Java/JNI vs a bridge process; Z-Wave serial API; Shelly = plain HTTP/WebSocket — likely the cheapest real adapter); JPMS/module implications; certification/licensing burdens (CSA membership tiers + cost, Z-Wave Alliance, anything GPL-viral in candidate stacks — flag for the LICENSE brief).
5. **Strategic timing vs the mid-Aug go/no-go and the trust brand:** which choice makes the strongest demo + earliest real-home viability; which can be Wave-3 without strategic cost.

## 3. The deliverable shape (REC first)

§0 = THE RECOMMENDATION: a sequenced roadmap (e.g., "M14 = X; M15-era = Y; defer Z") with the three strongest reasons and the two strongest counter-arguments stated honestly, each with its mitigation or its acceptance. §1 = the trade-off matrix (candidates × axes, terse). §2+ = per-candidate evidence (cited). §N = the Shelly pilot case study CONCRETE: what a minimal Shelly Gen2 adapter needs from our seams (transport, discovery, state ingestion → state_reported, command dispatch → confirmation via NotifyStatus — map it to the actual Doc 08 vocabulary), sized in WU-count terms. Final section: open questions only Nick can rule + what the LICENSE-flip brief should inherit from your findings.

## 4. Return protocol

ONE file: `nexsys-hivemind/context/assessments/2026-07-11_integration-roadmap_research-return.md`. Cite every load-bearing claim (URL or repo-doc pointer); mark confidence per claim (VERIFIED-current / community-reported / inference). State "RETURN READY for hub audit" + a 10-line summary in-conversation when done. Do NOT commit; the hub orders commits. An honest "this is genuinely contested, here's the fork" beats a manufactured certainty.
