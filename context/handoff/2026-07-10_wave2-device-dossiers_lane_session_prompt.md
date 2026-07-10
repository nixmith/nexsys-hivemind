<!--
file: context/handoff/2026-07-10_wave2-device-dossiers_lane_session_prompt.md
purpose: Session prompt for the Wave-2 device-dossiers research lane (Track B lane (a) — MONDAY-BLOCKING, first-class per Nick's 2026-07-10 ruling). Four device dossiers to the corpus standard + the Shelly Gen2 stimulus-contract appendix.
audience: a fresh Cowork research lane (write-isolated; returns to the hub for two-layer audit).
state-type: lane dispatch prompt (one session; retires on return).
status: READY — launch in a FRESH Cowork conversation; attach this file; paste: "Read and follow all instructions contained within the wave2-device-dossiers lane session prompt file."
-->

# Lane Brief — Wave-2 Device Dossiers (+ the Shelly stimulus appendix)

## 0. Mission and authority

You are a RESEARCH LANE for HomeSynapse (a local-first, event-sourced smart-home platform on a Pi bench). Produce **four device dossiers + one appendix** that let the PM hub author device profiles and bench scenarios the day the soak exits (Monday 2026-07-13). You are WRITE-ISOLATED: your ONLY repo write is the single return file named in §3. You never touch code, config, the Pi, or any other hivemind file. Your return is audited by the hub (two-layer; labels-are-claims, quotes-are-evidence) before anything downstream consumes it.

## 1. Required reads (before any research)

1. `nexsys-hivemind/context/process/truth-hierarchy-and-pointer-not-copy-discipline.md` — your return states claims with sources, never copies of state.
2. The corpus standard by example: `nexsys-bench/docs/2026-07-06_m9.4-bench-acceptance-record.md` (how evidence is bound to claims) and ONE existing device profile in `homesynapse-core/integration/integration-zigbee/src/main/resources/` (or wherever `philips_hue_white_color_a19` / `sonoff_snzb_03p` profiles live — locate them; they define the profile shape: match criteria, endpoints/clusters, attributes, commands, confirmation characterization fields per AMD-97's confirmation[] model).
3. `nexsys-bench/scenarios/SCENARIO_FORMAT.md` + `nexsys-bench/docs/2026-07-10_bench-automation-charter.md` — the appendix's consumer (the B3 stimulus driver) and the API-first assertion rules.

## 2. The four dossiers (the devices are IN HAND, unboxed — SONOFF, Zigbee 3.0)

For EACH of: **S31 Lite zb** (smart plug, on/off, NO power monitoring — the Lite), **SNZB-02P** (temperature/humidity), **SNZB-04P** (door/window contact), **SNZB-01P** (wireless button):

1. **Identity as an interview will see it:** manufacturer/model strings (the Basic-cluster values zigbee2mqtt/ZHA record — quote them exactly; these become MatchCriteria), endpoint map, in/out clusters per endpoint, power source byte.
2. **Interview expectations:** what a Z3.0 interview should find; known quirks (sleepy timing for battery devices — check-in behavior, how long the awake window is after a button press; the SNZB-03P precedent: 2/3 reporting-verify with a 5 s exchange window).
3. **Reporting configuration expectations:** which attributes support configured reporting (min/max/reportable-change values z2m ships), which are report-on-change vs periodic, expected report cadences — this feeds availability-ALIVE anchoring AND confirmation windows.
4. **Confirmation characterization (the AMD-97 lens — the important one):** per capability: is a command CONFIRMABLE via authoritative report (the S31's on/off should report back — latency envelope from community data), UNCONFIRMABLE (button/contact/temp have no commands), and what the honest expectation shape is. For the sensors: what does each REPORT and on what stimulus (contact open/close both edges? button single/double/long — which cluster carries it: OnOff-cluster events? MultistateInput? SONOFF custom?). Quote the z2m converter/ZHA quirk source for every claim.
5. **Known firmware variance + failure modes:** community-reported issues (drop-offs, spammy reporting, IAS enroll quirks for the 04P if it uses IAS vs plain OnOff, battery reporting oddities).
6. **Bench-scenario seeds:** 2–3 AUTO/OPERATOR scenario sketches per device in the SCENARIO_FORMAT idiom (e.g., S31: command-confirm direct on_off — the leg the Hue could never give us; 02P: report-cadence → ALIVE anchoring; 04P: contact both-edges; 01P: press-class events → automation trigger).

**Evidence discipline:** zigbee2mqtt device pages + converter source, ZHA device handlers (quirks), SONOFF official docs — cite every claim with a URL; mark everything as SECONDARY evidence ("community-documented; silicon adjudicates on the bench"). NO invented cluster IDs, NO invented attribute names — if sources conflict or are silent, SAY SO in a flagged-uncertainty list per device. The bench will verify; your job is to make Monday's verification fast, not to guess.

## 3. The appendix: the Shelly Plus Plug US Gen2 stimulus contract

The bench ordered 2× Shelly Plus Plug US as OUT-OF-BAND actuators (WiFi, local API — they drive wall power for devices under test; they are NOT devices under test). Produce the exact driver spec `bench.sh` will implement (B3): the local RPC endpoints for on/off/toggle/status (`/rpc/Switch.Set`, `Switch.GetStatus`, `Shelly.GetStatus` — verify against the official Gen2+ API docs and quote them), auth model (default none on LAN? password option?), discovery + static-addressing REC for a bench (mDNS name vs static IP), response shapes (what JSON confirms the switch state — the driver's success token), latency/timeout expectations, retry semantics, and any cloud-disable/eco-mode settings the bench should set at provisioning. Deliverable shape: a "provision once" checklist + a curl one-liner per verb + the assertion field per verb.

## 4. Deliverable + return protocol

ONE file: `nexsys-hivemind/context/assessments/2026-07-11_wave2-device-dossiers_research-return.md` — frontmatter (purpose/status/date), §1–§4 per device, §5 the Shelly appendix, §6 the consolidated flagged-uncertainty list, §7 source index. Dense, quote-rich, pointer-not-copy. When done: state "RETURN READY for hub audit" + the file path + a 10-line summary in-conversation. Do NOT commit; the hub orders commits. If you cannot resolve something material after honest effort, flag it loudly rather than padding — an honest gap beats a confident fabrication (never-false-CONFIRMED applies to research too).
