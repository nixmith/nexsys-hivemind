<!--
file: context/strategy/Six_Battlefields_MVP_Strategy.md
purpose: Quick-reference extract of the Six Battlefields MVP competitive-strategy frame.
audience: PM, Nick
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# Six Battlefields — MVP Competitive Strategy Quick Reference

**Source:** HomeSynapse_Core_v1_Project_MVP.md §2.1–2.2
**Purpose:** Standalone decision tool for scope evaluation, feature prioritization, and competitive positioning
**Status:** Extracted reference — authoritative content lives in the MVP doc
**Use this when:** Evaluating whether a feature belongs in Tier 1 vs. Tier 2, assessing scope changes, or explaining why HomeSynapse exists

---

## The Strategic Frame

HomeSynapse does not win by matching 3,000 integrations. It wins by demonstrating superiority on six battlefields where every competitor fails. These battlefields are not a feature list — they are the selection criteria for what the MVP proves and the decision framework for what gets built, deferred, or rejected.

Every feature proposal must trace to at least one battlefield. If it doesn't serve any of these six, it doesn't belong in the MVP.

---

## The Six Battlefields

### 1. Reliability Under Load

**The claim:** A 60-device home with layered automations running for months without intervention, without memory leaks, without degradation.

**Who fails here:** Home Assistant struggles (Python GIL contention, recorder bloat, event loop blocking at scale). Google/Amazon hide the problem behind cloud servers — when cloud degrades, so does the home.

**What proves it:** 50+ Zigbee devices, stable for 72+ hours on Raspberry Pi 4. No memory growth. No performance degradation. Kill -9 recovery with zero event loss.

**Architecture that enables it:** Event sourcing (append-only, no in-place mutation), Java 21 virtual threads (no GIL), SQLite WAL mode (concurrent reads, sequential writes), checkpoint-based recovery.

### 2. Local-First Superiority

**The claim:** Unplug the internet cable. Everything still works — locks, lights, automations, the UI, event recording.

**Who fails here:** Google Home and Alexa fail completely. Home Assistant mostly works but has cloud-dependent integrations that degrade unpredictably. HomeKit works locally but has no observability.

**What proves it:** Internet outage simulated — zero degradation in any capability. The killer demo: internet unplugged, locks still work, automations still trigger, UI still loads, events still record.

**Architecture that enables it:** All core functionality runs on local hardware. No cloud dependency in the critical path. Event bus, state store, persistence, automation engine — all local.

*(D-4/REC-180 messaging rule — ACCEPTED 2026-06-12, folded here 2026-07-03: **privacy is a SEGMENT lead, not THE lead.** Mass-market messaging leads with reliability/works-together (battlefields 1 and 6); local-first is the architecture story, and privacy is its segment-scoped expression — it converts prosumer/EU audiences (where regulation has dated teeth), not the mass market. A messaging rule, not a scope change. Source: the R15 strategy-refresh drafts, `context/planning/2026-06-13_strategy-refresh-drafts_R15.md`.)*

### 3. Explainability

**The claim:** A non-developer user can answer "why did the porch light turn on at 3am?" by looking at the event trace in the UI.

**Who fails here:** Every platform. Home Assistant requires log diving. Cloud platforms don't expose causality at all. No major platform provides causal chain visualization.

**What proves it:** Event trace for any device state change — full causal chain visible in the UI. correlation_id and causation_id threading through trigger → condition → action → state change.

**Architecture that enables it:** Three-level state lifecycle (state_reported → state_changed → state_confirmed), correlation/causation IDs in every event envelope, INV-TO-01 through INV-TO-03.

### 4. Crash Isolation

**The claim:** Kill the Zigbee adapter mid-operation. Z-Wave locks keep working. Automations that don't depend on Zigbee keep firing. The crashed adapter restarts. No events are lost. No state is corrupted.

**Who fails here:** Home Assistant has no formal isolation model — one bad integration can block the event loop and freeze the entire system. Cloud platforms hide crashes but lose state.

**What proves it:** Integration crash simulated — isolated, automatic recovery, no data loss. Other integrations continue operating throughout.

**Architecture that enables it:** OTP-style fault isolation in Integration Runtime (Doc 05), one-for-one restart strategy, write-ahead event persistence (events durable before delivery), per-integration fault domains.

### 5. Energy Intelligence

**The claim:** Real-time whole-home energy monitoring with historical data that loads instantly, even six months of data. Automations that respond to power usage.

**Who fails here:** No platform does this well at the local level. Home Assistant's recorder degrades with historical data volume. Cloud platforms silo energy data.

**What proves it:** Energy dashboard with six months of historical data — loads instantly. Automations triggered by power thresholds. The feature that justifies platform adoption to the skeptical household member — it saves money.

**Architecture that enables it:** Dedicated telemetry ring store (Doc 04), energy devices as first-class citizens with typed capabilities (Doc 02), aggregation engine producing domain events from raw telemetry.

### 6. Zero-Maintenance Stability

**The claim:** The system runs on a Raspberry Pi in a closet and does not require babysitting. Updates are safe, rollbacks work, and device replacement does not break automations.

**Who fails here:** Home Assistant requires ongoing maintenance (database purging, integration updates that break things, YAML migrations). Cloud platforms require internet. Hubitat is stable but opaque.

**What proves it:** System update simulated — clean rollback on failure. Device replacement (swap a lock) — automations remain intact, event history preserved. Months of unattended operation.

**Architecture that enables it:** Three-layer identity model (ULID binding keys survive device replacement), checkpoint-based recovery, storage pressure management (progressive retention, never catastrophic failure).

---

## The Proof Scenario (Tier 2 Acceptance Test)

This is the competitive demonstration — the eight-step acceptance test that proves all six battlefields simultaneously:

1. A 60-device home across multiple protocols (Zigbee, Z-Wave, energy monitoring)
2. Six layered automations operating simultaneously
3. Internet outage simulated — zero degradation in any capability
4. Integration crash simulated — isolated, automatic recovery, no data loss
5. System update simulated — clean rollback on failure
6. Device replacement (swap a lock) — automations remain intact, event history preserved
7. Energy dashboard with six months of historical data — loads instantly
8. Event trace for any device state change — full causal chain visible in the UI

---

## Decision Framework: Using Battlefields for Scope Evaluation

When evaluating a feature proposal, scope change, or prioritization question:

**Step 1 — Battlefield trace.** Which battlefield(s) does this feature prove? If none, it doesn't belong in the MVP. Record it as a future consideration.

**Step 2 — Competitive differentiation.** Does this feature demonstrate something no competitor can match? Features that match competitors without exceeding them are lower priority than features that create clear separation.

**Step 3 — Tier alignment.** Does this feature belong in Tier 1 (foundation proof on Zigbee), Tier 2 (full competitive proof across protocols), or Tier 3 (market credibility with Matter/Thread)? Don't pull Tier 2 work into Tier 1.

**Step 4 — Architecture impact.** Does building this now create rework when Tier 2/3 features arrive? The critical constraint: every Tier 1 design decision must accommodate Tiers 2 and 3 without architectural rework. Design for the full scope, implement for the current tier.
