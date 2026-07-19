<!--
file: context/programs/matter-design/dispatches/2026-07-19_A2_transport-and-hardware_lane_prompt.md
purpose: Dispatch prompt for research lane A2 — Matter transports (WiFi/Ethernet vs Thread), commissioning flows, DUT shortlist with prices, and Matter-bench network isolation.
audience: a fresh write-isolated Cowork research lane (NOT the PM hub; do not load the PM skill).
state-type: session prompt (lane dispatch).
status: READY — authored 2026-07-19 by the Matter design-program hub (launch beat 1).
-->

# Lane A2 — Transport + Hardware (commissioning, border-router reality, the DUT shortlist Nick rules on)

You are a **write-isolated research lane** of the Matter/Integrations Design Program (charter: `nexsys-hivemind/context/handoff/2026-07-19_matter-design-program_hub_session_prompt.md`; ruled by Nick 2026-07-19). Your job: the transport question (WiFi/Ethernet-first vs Thread), commissioning-flow reality, a **priced DUT shortlist** (this becomes memo B3, Nick's purchase ruling), and lab-network isolation for a future Matter bench.

**WRITE ISOLATION (ABSOLUTE):** exactly ONE file: `nexsys-hivemind/context/programs/matter-design/returns/A2_transport-and-hardware_return.md`. No other writes anywhere. All repo reads read-only.

**EVIDENCE DISCIPLINE (two-layer hub audit):** tag every load-bearing claim `[VERIFIED-current: URL, fetched YYYY-MM-DD]` · `[community-reported: URL]` · `[inference — reasoning stated]` · `[banked: repo-path §]`. Prices carry retailer + date. Quotes are evidence; labels are claims. Honest gaps outrank confident guesses.

## Baseline (banked; ↻ = re-verify currency — the base was fetched 2026-07-10)

Roadmap return §3.3 banked: phone-free BLE→WiFi commissioning became practical June 2026 (matterjs-server Beta; HA 2026.6) with a named **BLE→Thread gap** ↻ · chip-tool on a Pi commissions retail devices against the public PAA store, no CSA membership needed · **OTBR-on-Pi is "workable-but-fragile"** (IPv6 RA/RIO routing = the recurring failure domain) ↻ · Thread 1.4 credential sharing mandatory-for-1.4-TBRs but rollout uneven ↻ · **RULED (banked, currency §1C C1-15): Thread arrives on a DEDICATED radio, never MG24 dual-stack — Multi-PAN is dead** · Matter 1.6 (2026-06-17) added NFC commissioning ↻ · IKEA's 21-product native-Matter line rolling out from Jan 2026 ↻.

**Baseline shift since the banked base:** (1) Nick's 2026-07-19 ruling — full design program NOW, code gated; your DUT table is a real purchase decision, not a thought experiment. (2) **The Gen4 Shelly plugs (2× S4PL-00116US) arrived 2026-07-18 and are RULED stimulus-only, radios permanently un-provisioned — they are NOT Matter DUTs and never will be**; Matter DUTs are NEW purchases Nick rules in at B3. (3) The live bench fleet is now 5 devices/5 entities on Zigbee ch20/panId 0x774c — a production-grade evidence asset the Matter bench must never perturb.

## Required reads (before searching)

1. The program charter — your fences.
2. Roadmap return §3.1/§3.3 — the banked base.
3. `context/planning/2026-06-21_device-acquisition-and-test-strategy_brief.md` — the acquisition principles (radios front-load; endpoints just-in-time) your DUT table must honor.
4. `context/assessments/2026-07-11_wave2-device-dossiers_research-return.md` — skim for the dossier format precedent (per-device identity/capability/price rows) your table should echo.
5. `context/process/2026-07-18_compounding-testing-doctrine.md` — what a DUT must be good FOR (fixture capture, ratchet scenarios, measured envelopes).

## The questions

1. **Transport shape of the actual 2026 Matter device market:** what share of retail native-Matter devices are Matter-over-WiFi/Ethernet vs Matter-over-Thread vs bridge-fronted — best available evidence (category counts from trackers, ecosystem catalogs, the IKEA line's split ↻). Conclusion to evidence: what does a WiFi/Ethernet-only V1-Matter controller honestly cover, and what does it visibly lack?
2. **Thread border-router reality, updated ↻:** OTBR-on-Pi current state (the IPv6 failure-domain record; any 2026 improvement), RCP radio candidates for a Pi-hosted OTBR (chipsets, boards/dongles, prices, firmware maturity), Thread 1.4 credential-sharing rollout state, and coexistence constraints of an OTBR radio with our EZSP coordinator (2.4 GHz channel planning vs the live ch20 network — physical-layer honesty, cite sources).
3. **Commissioning flows, enumerated:** QR/manual-pairing-code payload contents (what the controller parses), the BLE role (which device classes require BLE commissioning vs on-network/IP commissioning), the Pi-side BLE stack posture (BlueZ over D-Bus; GPL fence via IPC `[banked: roadmap §7.1]` — confirm current), NFC (1.6) practical availability, and multi-admin/joint-fabric basics (what "already commissioned to Apple/Google, add us second" requires of a controller). Rate each flow: works-headless-today / works-with-caveats / gap.
4. **THE DUT SHORTLIST (the B3 purchase table — the lane's center of gravity):** a priced table of first Matter DUTs, honoring: **native-Matter (not bridge-fronted) for the first wave** · Matter-over-WiFi/Ethernet first (no TBR dependency) · device classes that exercise distinct confirmation postures (a mains plug/switch [command+energy], a bulb [level/color], a mains sensor or contact/motion class if any exist native-WiFi, and ONE deliberate bridge-class device for the bridged-provenance work A4 defines) · retail-available in the US with price + retailer + date · vendor firmware/update reputation noted. For each: model, protocol/transport, device types exposed, price, why THIS unit earns bench time (what it lets us measure), and any known quirks (issue-tracker evidence). Include a phase-2 row set: one Thread DUT + the RCP radio for the OTBR phase — priced but explicitly phase-2. Give a total-budget line per phase. **Do not include the Gen4 Shellys in any DUT capacity.**
5. **Lab-network isolation for a Matter bench:** what Matter-over-WiFi actually needs from the LAN (mDNS/DNS-SD, IPv6 — link-local sufficiency vs routable, multicast behavior), options for isolating a Matter bench segment (separate SSID/VLAN/subnet; a dedicated AP on the bench) while the controller still reaches it, hazards (mDNS across VLANs, IPv6 RA leakage — the OTBR failure domain generalizes), and what the Zigbee bench's isolation posture teaches. Deliverable: 2–3 concrete isolation options with tradeoffs, no winner.
6. **Commissioning custody:** what fabric/operational credentials a Matter controller persists (fabric keys, NOCs, operational certs, the attestation trust store), where each stack from lane A1's option set stores them, their sensitivity class, and what backup/restore implies — framed as evidence for the design phase's custody section (the SD-5 seed-custody discipline is the house precedent `[banked: pm-handoff v33 beats 2/4]`; you map what EXISTS, not what we'll build).

## Known hazards

- Retail listings conflate bridge-fronted and native devices constantly — verify "native Matter" per unit from vendor docs/certification listings, not marketing pages.
- Thread marketing understates the TBR ops burden; the banked fragility record is load-bearing — update it, don't soften it without evidence.
- Prices drift: date every price; prefer two retailer citations for anything over ~$50.
- The live fleet (ch20/0x774c) is untouchable — any coexistence claim that implies touching it is a STOP-and-flag, not a proposal.

## NOT in scope

No purchases (Nick rules at B3). No stack recommendation (A1/A3/B1). No moat mapping (A4). No certification economics (A5). No code, no core writes, no gate interaction (J1 FROZEN; criteria §2 fences Matter out of mid-Aug).

## Return format

`§0` executive digest (≤1 page) → `§1–§6` matching the questions → **§4 renders the DUT table ready to lift into memo B3 verbatim** (rows + budget lines) → `§7` open questions BLOCKING / NON-BLOCKING for the design phase → `§8` honest gaps.

**Done-when:** the single return file exists at the exact path, every price dated and sourced, the DUT table lift-ready, the Gen4-Shelly fence restated in §4, isolation options concrete enough to cost.
