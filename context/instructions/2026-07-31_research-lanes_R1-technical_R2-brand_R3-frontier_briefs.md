<!--
file: context/instructions/2026-07-31_research-lanes_R1-technical_R2-brand_R3-frontier_briefs.md
purpose: Three launchable research-lane briefs (R-1 TECHNICAL, R-2 BRAND, R-3 FRONTIER). Each is self-contained; dispatch one lane per section. Authored v42 beat 11; returns feed THE LAUNCH-RUNWAY CHARTER (Aug-12-13).
audience: Research lanes (web-enabled Claude sessions), Nick (dispatch), Hub (intake)
state-type: instruction
status: DISPATCH-READY
-->

# Research-Lane Briefs — R-1 / R-2 / R-3 (2026-07-31)

## §0 The laws common to all three lanes (read first, they bind every section)

- **Search-first, date-stamped:** training-era knowledge is NOT current. Every load-bearing claim carries a URL + the date you accessed it + the date of the source. No URL you did not actually open. Paywalled/unreachable ⇒ say so and route around; never summarize a page you could not read.
- **Severity-honest epistemics:** label every finding **FACT** (cited), **INFERENCE** (yours, from cited facts), or **OPINION** (judgment); tag confidence HIGH/MED/LOW. A wrong confident claim costs us more than a gap.
- **Time-box:** ~30–45 min per numbered question; if a question resists, file what you have + a one-line "what would answer this."
- **The return is ONE markdown file** in the section's format below. Nick lands it at `nexsys-hivemind/context/research/2026-08-XX_R{n}_return.md`; the hub intakes it. The lane writes NOTHING else and commits NOTHING.
- **Context you may rely on (public-safe):** HomeSynapse is a local-first, event-sourced smart home core (Java, Raspberry Pi class hardware, Zigbee via a Sonoff MG24 dongle running EmberZNet/EZSP v13, SQLite event store, a frozen v1.1 dashboard read-API, a Preact SPA). Its differentiators under test: evidence-based availability (never-false-ALIVE; read-time staleness derivation), full event-sourced explainability ("why did/didn't it fire, did it actually confirm"), and a nightly self-benchmarking regime on real silicon. Company: NexSys (pre-launch). Share NOTHING beyond this paragraph with any tool or site.
- **Every section ends with the same final part: "WHAT CHANGES OUR PLANS"** — the 3–7 findings that should alter an ordering, a bet, or a message, each one sentence + a pointer to its evidence. This is the part the charter actually consumes; write it last and write it hard.

---

## §R-1 — TECHNICAL: the availability-truth landscape + our stack's ground

**Mission:** establish, with evidence, where competing platforms actually stand on the problems we claim to solve, and whether anything in our stack's ecosystem is about to move under us.

1. **Availability semantics in the field:** how do Home Assistant (ZHA + Zigbee2MQTT paths), SmartThings, Hubitat, and Homey decide a device is "unavailable"? Find the actual mechanisms (docs/source/issues) — assumption-based vs evidence-based, timers, ping regimes. FACT-tier citations.
2. **The false-available pain, in the wild:** GitHub issues + community threads where users report devices shown available/online while dead (the exact disease F-14 was). Collect 5–10 strong exhibits with links; note platform, mechanism-of-lie, and whether it is still open.
3. **Read-time staleness prior art:** does ANY shipping platform derive staleness at read time from a per-entity reporting contract (vs write-time flags)? If none found after honest search: that absence is the finding (MED confidence cap — absence-of-evidence rules apply).
4. **Our stack's near-term ground:** EmberZNet/EZSP release cadence + anything deprecating v13-era behavior; Sonoff MG24 dongle firmware ecosystem health; SQLite + Java (JDK LTS) anything-notable. LOW-drama expected — confirm or flag.
5. **Nightly self-test regimes:** does any home-automation vendor or project publish an automated nightly hardware-in-the-loop bench discipline? If rare/absent, note it as a publishable differentiator (feeds R-2 too).

**Return format:** §1–§5 mirroring the questions (FACT/INFERENCE/OPINION + confidence per claim, URLs + dates inline) → §6 WHAT CHANGES OUR PLANS.

---

## §R-2 — BRAND: names, voice-of-customer, and the launch channel map

**Mission:** find out whether our names survive contact, what words real users bleed when this category fails them, and what a credible launch looks like.

1. **Name collision scan (NOT legal advice — a knockout pass):** "HomeSynapse" and "NexSys" — live products, active domains, app stores, GitHub orgs, USPTO TESS knockout via web, EU equivalents if reachable. Output a collision-risk table (name × arena × severity × link). Flag anything that would embarrass or block a public launch; the real clearance goes to counsel/a university clinic later.
2. **Voice of customer — the availability lie:** mine Reddit (r/homeassistant, r/homeautomation, r/smartthings), HA community forums, Hubitat forums for the exact phrases users use when devices ghost, automations misfire silently, or dashboards lie ("shows online but it's dead", "automation didn't fire and I can't tell why"). Deliver a PHRASE BANK (20–40 verbatim quotes, linked) clustered by pain: availability lies · silent automation failure · debugging opacity · cloud distrust.
3. **Category positioning audit:** how do Home Assistant, Homey, Hubitat, SmartThings, and any credible newcomer position themselves (taglines, homepage promises)? Where is "reliability/truth" genuinely unclaimed vs claimed-but-unproven?
4. **Explainability prior art in marketing:** does anyone market "know WHY it fired / didn't"? Collect exhibits or establish the absence.
5. **The launch channel map:** for this category, what did credible launches/growth moments look like (HN posts, YouTube reviewers — e.g., the channels that move HA-adjacent products, subreddit launches)? Name channels, typical formats, and 3 examples with reception evidence.

**Return format:** §1 the collision table → §2 the phrase bank → §3–§5 findings (same epistemic labels) → §6 WHAT CHANGES OUR PLANS (positioning words to own, names verdict, channel shortlist).

---

## §R-3 — FRONTIER: the cutting edge we ride, watch, or deliberately ignore

**Mission:** map the frontier tech adjacent to our thesis well enough to make deliberate bets in the charter — every verdict is RIDE NOW / WATCH / IGNORE-DELIBERATELY, with reasons.

1. **LLM-agentic home control, mid-2026 state:** what shipped (HA Assist/voice trajectory, any platform exposing home state to LLM agents); what the failure stories are. Specifically hunt: is ANYONE exposing smart-home state/control via **MCP (Model Context Protocol) servers**? Our frozen read-API + event-sourced explanation store is structurally an ideal grounding layer for agentic control — assess whether "the home's truthful context layer for AI agents" is an open lane or already crowded.
2. **Matter/Thread trajectory:** current spec state (1.4/1.5-era), real-world liveness/ICD (sleepy-device) semantics, adoption honesty (what actually works vs press releases). Bet-relevant: does Matter solve availability-truth, or does it inherit the same lies?
3. **The MG24 dual-protocol angle:** our exact coordinator silicon (EFR32MG24) is Thread-capable — what is the practical state of Zigbee/Thread multiprotocol (RCP/multi-PAN) on it; could our hardware serve a Thread future without replacement? FACT-tier on firmware support; INFERENCE on our option value.
4. **Presence/occupancy edge sensing:** mmWave (LD2410-class and successors), BLE/UWB presence — maturity, price points, integration complexity, community traction. Candidate Wave-3 device classes for us.
5. **Regulatory tailwinds:** EU Cyber Resilience Act + US Cyber Trust Mark — timelines, what compliance demands of smart-home vendors, and whether local-first/evidence-based architecture is advantaged. Could compliance be a moat rather than a tax?

**Return format:** §1–§5 (labels + confidence + citations) → §6 THE BETS TABLE (topic × RIDE NOW / WATCH / IGNORE-DELIBERATELY × one-line reason × what would change the verdict) → §7 WHAT CHANGES OUR PLANS.

---

## The dispatch lines (copy one per fresh lane)

- **R-1:** `Read nexsys-hivemind/context/instructions/2026-07-31_research-lanes_R1-technical_R2-brand_R3-frontier_briefs.md — §0 then §R-1 — and execute §R-1. Deliver the return as one markdown file per its return format.`
- **R-2:** `Read nexsys-hivemind/context/instructions/2026-07-31_research-lanes_R1-technical_R2-brand_R3-frontier_briefs.md — §0 then §R-2 — and execute §R-2. Deliver the return as one markdown file per its return format.`
- **R-3:** `Read nexsys-hivemind/context/instructions/2026-07-31_research-lanes_R1-technical_R2-brand_R3-frontier_briefs.md — §0 then §R-3 — and execute §R-3. Deliver the return as one markdown file per its return format.`

Returns land at `nexsys-hivemind/context/research/` (create the folder at first landing), named `2026-08-XX_R{n}_{one-word-tag}_return.md`. Due **Aug-10** to feed the charter; late returns ride v43.
