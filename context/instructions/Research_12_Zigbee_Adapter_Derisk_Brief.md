<!--
file: context/instructions/Research_12_Zigbee_Adapter_Derisk_Brief.md
purpose: Research 12 brief — M14 Zigbee adapter de-risk: field-evidence survey of real-world Zigbee implementation hazards from Zigbee2MQTT/ZHA/deCONZ/openHAB, plus the EntityRole classification survey (AMD-44 §6). Dispatch to the HomeSynapse **DOCS** Claude Project (it must read Doc 08, which lives in the homesynapse-core-docs repo only the DOCS Project holds; all code identifiers this brief needs are embedded verbatim below).
audience: External researcher (Claude Project), PM
state-type: instruction
status: READY TO DISPATCH — authored 2026-06-05, source-verified vs HEAD `e73e199`
-->

RESEARCH BRIEF: Research 12 — Zigbee Adapter De-Risk: Field Evidence from Production Smart Home Platforms

**AUTHORITATIVE STATE HEADER (per your custom instructions, this is the only source of "now"):** `homesynapse-core` HEAD `e73e199` · amendment watermark **AMD-53** · `projectionVersion` **5** · M4.B-S2 (EntityRole) in flight · Doc 08 status **Locked**.

You are the PM/architect for HomeSynapse Core, a local-first event-sourced smart home runtime in Java 21. Produce a research document with EXACTLY these sections (the mandatory format — self-contained here, do not look for it elsewhere): **§1 Executive Summary** (verdict-led: the 3–5 findings that most change M14's risk, each with a position); **§2 Platform Deep Dives** (one subsection per surveyed platform, primary-source-cited); **§3 Cross-Cutting Analysis** (patterns across platforms; where they agree, where they diverge and why); **§4 Amendment Recommendations** (numbered RECs — each with a position, evidence, effort-in-LOC, and a severity for the 72h validation gate); **§5 Caveats and Open Questions**; **§6 Appendix: Sources** (URLs); **§7 Code-Level Implications** (LIGHT — see constraints).

## Why this research exists

**M14 (Zigbee Integration, ~Sep–mid-Oct band) is the single highest-risk milestone on the release runway**: real hardware, ZCL plus two manufacturer codecs, dual-coordinator support, and a 72-hour validation gate, all landing in the thinnest-buffer window before the late-Nov launch. Doc 08 (Zigbee Adapter) is **Locked** — this research does NOT redesign it. The job is to harvest a decade of field evidence from the platforms that have already paid the tuition (Zigbee2MQTT, ZHA/zigpy, deCONZ, openHAB Zigbee binding, HA core), so M14's amendments and coding instructions inherit their scar tissue instead of re-earning it. Findings age slowly; we dispatch early (3+ months of lead time) deliberately.

A second deliverable rides along: the **EntityRole classification survey** deferred at AMD-44 §6 — Home Assistant's `EntityCategory` (diagnostic/config) assignment patterns across major Zigbee integrations, which calibrates HomeSynapse's adapter-author guide for the just-landed `EntityRole` enum (PRIMARY/DIAGNOSTIC/CONFIG, Decision 9 coordinator convention).

## What Doc 08 already locks (the frame you validate against, not reopen)

Doc 08 §-map for orientation: §3.2 two-layer coordinator architecture; §3.3 transport implementations; §3.4 device interview pipeline; §3.5 cluster-to-capability mapping; §3.6 device profile registry; §3.7 reporting configuration; §3.8 Tuya datapoint manufacturer codec; §3.9 Xiaomi/Aqara TLV manufacturer codec; §3.10 command dispatch; §3.11 network telemetry; §3.12 IAS zone enrollment; §3.13 network formation and security; §3.14 local device metadata cache; §3.15 route health monitoring (AMD-07). **Read the full document before answering: `design/08-zigbee-adapter.md` in the `homesynapse-core-docs` repo connected to this Project.** Where field evidence shows a §-level decision is dangerous in practice, say so plainly in §4 as an amendment candidate — evidence-based challenge is the point; silent redesign is not.

## SCOPE — Specific questions to answer (take positions on each)

**Q1 — Coordinator firmware and transport pitfalls (§3.2/§3.3).** For TI CC2652-class (Z-Stack) and Silicon Labs EFR32 (EmberZNet) coordinators: the documented failure modes — firmware-version lock-in, message-queue exhaustion under burst, watchdog resets, USB latency/serial framing issues (incl. on Raspberry Pi USB controllers), backup/restore (NVRAM) portability. What does Z2M's herdsman layer do that a new implementation always gets wrong first? Which firmware versions are the community-stable baselines in 2026?

**Q2 — Device interview/pairing failure modes (§3.4).** Sleepy battery devices failing mid-interview; devices that lie in their simple descriptors; interview retry/backoff strategies that actually work; pairing UX failures users hit most (the Z2M and ZHA issue trackers are the primary source). What fraction of interview logic is genuinely generic vs. quirk-driven?

**Q3 — Reporting configuration reality (§3.7).** Devices that accept configure-reporting then silently never report; devices that only report on poll; minimum-interval floors that brick battery life. How do Z2M converters and zigpy quirks encode per-device reporting overrides, and what's the maintenance cost curve?

**Q4 — Tuya datapoint protocol (§3.8).** The gotcha catalogue: undocumented datapoints, spec-violating checksum/sequencing behavior, devices that re-use datapoint IDs across product lines, time-sync demands, "magic packet" init sequences. How complete is Z2M's Tuya layer and what does its churn rate say about ongoing maintenance burden?

**Q5 — Xiaomi/Aqara TLV (§3.9).** Non-standard attribute 0xFF01/0xFF02 TLV blobs, heartbeat semantics, devices that drop off mesh without LeaveRequest, pairing-window quirks. Same maintenance-burden question.

**Q6 — Quirk/profile registry architecture (§3.6).** Compare the three models: Z2M external converters (JS, per-device files, community PRs), zigpy quirks (Python classes, signature matching), deCONZ DDF (declarative JSON). Which properties predict low review burden + high community contribution? What should HomeSynapse's device-profile schema steal, given profiles must be data files consumed by a compiled Java adapter (LTD-17 — in-process compiled integrations; no runtime scripting)?

**Q7 — IAS zone enrollment (§3.12) + network formation (§3.13).** Enrollment races and auto-enroll workarounds; channel selection vs. 2.4 GHz Wi-Fi interference guidance that holds up; install-code vs. well-known-key joining in 2026 (Zigbee 3.0 reality vs. legacy devices).

**Q8 — Mesh/route health (§3.11/§3.15).** What network-telemetry signals actually predict user-visible failures (LQI vs. RSSI vs. route churn)? What did AMD-07-style route health monitoring miss in peers — and what creates alert fatigue?

**Q9 — OTA firmware updates.** Doc 08 scope check: if OTA is out of MVP scope, what's the minimum forward-compatible posture (index formats, manufacturer image sources, the Z2M/ZHA OTA pain catalogue) so the door isn't designed shut?

**Q10 — EntityRole classification survey (AMD-44 §6 deliverable).** Across HA's top Zigbee-relevant integrations (ZHA, Z2M-via-MQTT, Hue, deCONZ): how is `EntityCategory` (diagnostic/config) actually assigned per entity kind — battery, voltage, LQI/RSSI, identify buttons, power-on-behavior, sensitivity/timeout settings, coordinator state? Catalogue reclassification churn (entities that flipped category across releases and why). Output: a concrete classification table HomeSynapse's adapter-author guide can adopt, calibrated to our matrix — `EntityRole` ∈ {PRIMARY, DIAGNOSTIC, CONFIG}; legality per `EntityType`: LIGHT {P,D}, SWITCH {P,D,C}, PLUG {P}, SENSOR {P,D}, BINARY_SENSOR {P,D}, ENERGY_METER {P,D}; coordinator-state default DIAGNOSTIC (Decision 9).

## PLATFORMS TO SURVEY
Zigbee2MQTT (zigbee-herdsman, zigbee-herdsman-converters — incl. issue tracker + converter churn), ZHA/zigpy (+ zigpy-quirks repo), deCONZ/Phoscon (DDF), Home Assistant core (ZHA integration + EntityCategory history), openHAB Zigbee binding (com.zsmartsystems.zigbee — the closest Java prior art: what did a JVM Zigbee stack get right/wrong?).

## VERIFIED IDENTIFIERS YOU MUST USE

The adapter compiles against `integration-api`. Verbatim `integration/integration-api/src/main/java/module-info.java` at `e73e199`:
```java
module com.homesynapse.integration {
    requires transitive com.homesynapse.platform;
    requires transitive com.homesynapse.event;
    requires transitive com.homesynapse.device;
    requires transitive com.homesynapse.state;
    requires transitive com.homesynapse.persistence;
    requires transitive com.homesynapse.config;
    requires transitive java.net.http;

    exports com.homesynapse.integration;
}
```
integration-api is 22 public types incl. `IntegrationAdapter` (initialize → run → close lifecycle), `IntegrationFactory`, `IntegrationContext`, `IntegrationDescriptor` (8 fields incl. `healthParameters`, `dependsOn`, `schemaVersion`), `HealthParameters` (incl. `maxRestarts`/`restartWindow` — restart intensity default 1/60s, per-descriptor override; a pre-M9 empirical spike on real Zigbee restart frequency is already logged), `HealthReporter`, `CommandHandler`, `CommandEnvelope`, sealed `IntegrationLifecycleEvent` (5 permits). Device adoption flows through device-model's `DiscoveryPipeline` (`propose(Set<HardwareIdentifier>, …, List<ProposedEntity>) → ProposedDevice`, then `adopt(...)`); `ProposedEntity` carries `(endpointIndex, proposedEntityType, proposedCapabilities, entityRole)` with `entityRole` defaulting PRIMARY and validated against `EntityType.allows(role)` at construction. Use these names exactly; for anything else, use the MODULE_CONTEXT.md inventories in project knowledge and never paraphrase module/type names.

## CONSTRAINTS
- Take positions. "X is worth investigating" is banned. Cite primary sources with URLs (GitHub issues/PRs, maintainer statements, official docs) — issue trackers outrank blog posts.
- Doc 08 is Locked: frame proposals as **amendment candidates for the M14 briefing** (§4), each with effort-in-LOC and a severity (how badly does ignoring this bite during the 72h validation gate?).
- REC numbering: start at **REC-120** (REC-106..119 reserved for Research 7 v2).
- AMD integers: do NOT assign — assign-at-milestone per the P2 renumbering decision.
- LTD-17 (in-process compiled integrations — no runtime scripting engine for quirks), LTD-04 (typed ULIDs), LTD-11 (ReentrantLock, virtual threads), no `ServiceLoader` (DECIDE-04), no new library without an explicit `gradle/libs.versions.toml` addition proposal with version pin.
- §7 is LIGHT for this research: concept-mapping tables onto the embedded identifiers + data-file schema sketches only. **No `module-info.java` proposals, no new module names.** If you believe a module change is needed, state it in §5 as an open question for the PM.
- Q10's output table must use HomeSynapse vocabulary (`EntityRole`, `EntityType`) — not HA's — with the legality matrix above respected in every row.

OUTPUT: a single complete markdown document in the mandatory format. Do not truncate.
