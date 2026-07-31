<!--
file: context/research/2026-07-31_R3_frontier_return.md
purpose: R-3 FRONTIER lane return. Executes §R-3 of 2026-07-31_research-lanes_R1-technical_R2-brand_R3-frontier_briefs.md. Feeds THE LAUNCH-RUNWAY CHARTER (Aug-12-13).
audience: Hub (intake), Nick, charter authors
state-type: research-return
status: DELIVERED
lane: R-3 FRONTIER
executed: 2026-07-31
all-URLs-accessed: 2026-07-31
note: rename to the landing date if the hub intakes it in August (brief template: 2026-08-XX_R3_frontier_return.md)
-->

# R-3 FRONTIER — return

**Mission (from brief):** map the frontier tech adjacent to our thesis well enough to make deliberate bets in the charter — every verdict RIDE NOW / WATCH / IGNORE-DELIBERATELY, with reasons.

**Epistemic key:** **FACT** = directly cited from a page actually opened · **INFERENCE** = my reasoning from cited facts · **OPINION** = judgment. Confidence HIGH / MED / LOW. Every URL below was fetched and read on **2026-07-31** unless a fetch failure is disclosed in-line. Pages that could not be read are named and **not** summarised.

**Verification note:** this lane was executed as five parallel sub-investigations, then eight of the most load-bearing citations were independently re-fetched and confirmed by the lane author. Confirmed: HA MCP Server install share and payload · HA Connect ZBT-2 multiprotocol stance · Matter 1.6 release date and contents · CRA Article 14 dates · Samsung Research ambient-context-sensor description · matterjs-server #494 · HA core #127759 · ioXt Lead Administrator. **One correction applied:** the "ambient context sensor" does **not** appear in CSA's own Matter 1.6 announcement — that finding rests solely on Samsung Research's write-up and is downgraded accordingly (§4b).

**Three structural caveats that bound this whole return:**

1. **No Matter/Thread specification PDF was read.** CSA and Thread Group gate all spec downloads behind request forms. Every protocol-mechanism claim in §2 comes from Matter SDK source, Silicon Labs vendor docs, or controller source read directly — never from normative spec text. Where that matters it is flagged.
2. **GitHub's REST API is blocked in this environment.** Per-file source claims (fetched via `raw.githubusercontent.com`) are solid; repo-level metrics (stars, commit dates) came from HTML fetches and were inconsistent for one repo — flagged LOW there rather than picking a number.
3. **Reddit was not reachable** (proxy rejected domain-restricted queries). Community-sentiment findings rest on HA/Silabs forums, GitHub, and dated review sites instead. Subreddit volume figures are absent by design, not by omission.

---

## §1 — LLM-agentic home control, mid-2026

### 1a. What actually shipped

- **FACT / HIGH — Home Assistant has a real, plugin-architected LLM tool-calling layer.** The Assist API has been refactored out of `helpers/llm.py` into a dedicated `llm` integration exposing an `LLMToolsPlatformProtocol`, so any integration contributes tools + prompt fragments via a `<domain>/llm.py` platform file. Verified platform files exist for `homeassistant`, `intent`, `todo`, `calendar`, `script`. Source read raw: `https://raw.githubusercontent.com/home-assistant/core/dev/homeassistant/helpers/llm.py`; docs `https://developers.home-assistant.io/docs/core/llm/`.

- **FACT / HIGH — HA's Assist API gives the model a *static* entity snapshot plus one live-lookup tool, `GetLiveContext`.** Read verbatim from `https://raw.githubusercontent.com/home-assistant/core/dev/homeassistant/components/homeassistant/llm.py`. The `DYNAMIC_CONTEXT_PROMPT` instructs the model: *"If the user asks about the CURRENT state, value, or mode … 1. Recognize this requires live data. 2. You MUST call `GetLiveContext`."* The static block is labelled *"Static Context: An overview of the areas and the devices in this smart home"*; the tool output *"Live Context: …"*.
  **This is the industry's most explicit acknowledgement that snapshot state goes stale — and its mitigation is a prompt string, not metadata.**

- **FACT / HIGH — HA ships MCP in both directions, since release 2025.2 (2025-02-05).** MCP **Server**: `https://www.home-assistant.io/integrations/mcp_server/` — verbatim, *"introduced in Home Assistant 2025.2, and it's used by 3.1% of the active installations"*, Silver quality, IoT class Local Push. MCP **Client**: `https://www.home-assistant.io/integrations/mcp/` — *"used by 209 active installations"*, Silver, Local Polling. Release post: `https://www.home-assistant.io/blog/2025/02/05/release-20252/`. *(Both figures independently re-verified by the lane author.)*

- **FACT / HIGH — HA's MCP Server now speaks Streamable HTTP, not just legacy SSE.** `components/mcp_server/http.py` docstring: *"Model Context Protocol transport protocol for Streamable HTTP and SSE"*; endpoints `/api/mcp`, `/api/mcp/<API ID>`, `/mcp_server/sse`. Corroborated by `https://github.com/orgs/home-assistant/discussions/1383` (opened 2025-10-15; user confirms 2026-04-28, *"I found HTTP streamable indeed does work now"*). **Asymmetry worth noting:** the *client* integration docs still describe SSE-only.

- **FACT / MED — Google completed the Assistant→Gemini transition for Home.** Google I/O 2026: Gemini 3.1, "Ask Home / Home Brief / Gemini camera intelligence", Gemini Built-In reference designs extended from cameras to speakers, 16 countries / 10 languages outside the US (`https://www.techinsights.com/blog/google-io-2026-gemini-home-takes-center-stage`, pub 2026-06-19). Assistant retirement corroborated at `https://the-gadgeteer.com/2026/06/23/gemini-for-home-replaces-google-assistant/` (pub 2026-06-23).

- **FACT / HIGH — Google's "context" for Home is a 15-minute *conversational* window, not state provenance.** `https://9to5google.com/2026/07/23/nest-cam-july-2026-update/` (pub 2026-07-23): context memory expanded to 15 minutes "across the entire Gemini for Home experience," example being "turn on the kitchen lights" → minutes later "dim it to 50%". **INFERENCE / MED:** this is pronoun/referent memory — a different axis from freshness of device state entirely.

- **FACT / MED — Alexa+ is broadly available and agentic.** Alexa+ on all Echo devices, free with Prime / $19.99 mo otherwise, agentic tasks (OpenTable, GrubHub, Ring summaries) — `https://www.tomsguide.com/ai/alexa-release-date-cost-devices-and-all-the-new-ai-features`. **Caveat: that page's stated last-update is 2025-10-10**, so its "mid-2026" framing is weakly dated. Amazon's own Alexa+ smart-home developer docs are live and dated 2026-07-23 (`https://developer.amazon.com/docs/alexaplus/smarthome/troubleshooting-guide.html`).

- **FACT / MED — Samsung rebuilt Bixby as an LLM agent reaching SmartThings.** `https://news.samsung.com/us/interview-bixby-starting-point-every-samsung-device-meet-jisun-park-head-language-ai` (pub 2026-04-07). Jisun Park: Bixby now has *"an LLM at its core"*, can *"interpret intent more flexibly and generate its own execution plans"*, achieved by converting *"individual functions into callable agents"*; claims it *"deeply understands device status and capabilities."* **No MCP mention.**

- **FACT / MED — Apple has not shipped LLM Siri; Gemini-powered Siri slipped to iOS 27 (~Sept 2026).** `https://www.t3.com/tech/ai/gemini-powered-siri-still-on-track-for-2026-release-apple-tells-major-outlet` (pub 2026-02-16). **INFERENCE / MED:** Apple is effectively absent from LLM home control through mid-2026.

- **FACT / MED — Josh.ai (the luxury/custom-install incumbent) shipped "AI X OS", no MCP.** `https://josh.ai/stories/joshai-keynote-2026-home-in-harmony-showcases-a-new-era-of-adaptive-home-control` (pub 2026-03-19). Natural-language scene creation; CEO Alex Capecelatro: *"Systems can now be configured on the fly using natural language, even by the homeowner themselves."*

- **UNVERIFIED — credible newcomers.** Homey (Athom) is the most-cited candidate but the primary article returned **HTTP 520** and was not read. *What would answer this: Athom's own 2026 release notes.* No venture-backed startup positioned specifically on trustworthy/provenance-carrying home context was found.

### 1b. Failure stories — the documented record

| Platform | What went wrong | Link | Date | Open? |
|---|---|---|---|---|
| Gemini for Home | **Model denied a camera existed** while checking garage-door status — *"there's no camera in place to check the garage door status, even when there is."* Also: Home Hub lost alarm and light control; *"when they ask Gemini to do a very specific thing, it does whatever it wants."* | [androidheadlines](https://www.androidheadlines.com/2026/01/gemini-update-for-google-home-doesnt-seem-to-be-all-that-smooth.html) | 2026-01-09 | Yes |
| Gemini for Home | Same cluster, independent coverage. User quote in headline: *"Gemini can't possibly be this stupid."* | [TechRadar](https://www.techradar.com/home/smart-home/should-you-upgrade-to-gemini-for-home-tread-carefully-some-users-are-still-reporting-major-bugs-and-problems) | 2026-01-09 | Yes |
| Gemini for Home | Thermostat request surfaced a **Spotify connection error**; refuses lights on Nest Hub that phone version controls. Reviewer: responses *"absolutely wrong."* | [TechRadar](https://www.techradar.com/home/smart-home/think-twice-about-upgrading-to-gemini-for-home-its-getting-some-tasks-absolutely-wrong-and-is-full-of-bugs) | 2025-12-17 | Yes |
| HA + Gemini 2.5 Flash | **Agent does not read state before acting.** "Turn off the bathroom light" → *"does not check the current state"*, confirms success even when already off. | [core#149325](https://github.com/home-assistant/core/issues/149325) | HA 2025.7.3 | **Open** |
| HA + Ollama | **LLM actuated an entity not exposed to Assist** — a YAML custom sentence bypassed the exposure allowlist. | [core#133460](https://github.com/home-assistant/core/issues/133460) | HA 2024.11.3 | Closed |
| HA Assist | LLM stuck in follow-up mode, stops re-consulting the local agent after a mis-heard query; needs manual RESET. | [core#162768](https://github.com/home-assistant/core/issues/162768) | opened 2026-02-11 | Closed |
| HA MCP **client** | Regression — cannot connect to SSE MCP gateway; `BrokenResourceError` / "Session terminated". Worked 2026.1.0, broken 2026.2.1 → 2026.4.2. | [core#162601](https://github.com/home-assistant/core/issues/162601) | — | **Open** (PR #162655) |
| Alexa+ | Missed a motorized curtain for weeks; **retrieved wrong home/destination addresses** during an agentic Uber booking despite confirming correctly elsewhere. Verdict: *"the Alexa app is still hot garbage."* | [Consumer Reports](https://www.consumerreports.org/electronics/digital-assistants/amazon-alexa-plus-ai-assistant-review-a1667486499/) | 2025-12-19 | Ongoing |
| Academic | **SmartBench** — LLMs on anomalous device states. Best context-independent F1 **79.3%** (Gemini-3); context-dependent F1 **67.6%**; anomaly-location score **0.300 / 0.221**. *"most LLMs are only able to provide reasonable explanations for less than 70% of the anomalies"*; concludes current LLM home assistants *"remain unreliable for residential anomaly detection."* | [arxiv 2603.06636](https://arxiv.org/html/2603.06636) | **date MED** — arXiv ID implies Mar 2026; abs page did not render a submission line | N/A |

**INFERENCE / MED — the exhibit that matters most is the garage-door one.** It is not a control failure. It is a model **asserting a false negative about the world** — denying a sensor exists — rather than saying "I can't confirm." That is precisely the failure class an evidence-based availability model prevents, and it is the single best public demo of our thesis that we did not have to construct ourselves.

### 1c. MCP and smart homes — the deep answer

**Short answer: MCP-for-home is real, live, and already at meaningful scale on Home Assistant — but essentially nobody conveys freshness, staleness, or confidence. The information exists upstream and is destroyed at the agent boundary.**

**FACT / HIGH — the crux, proven from source.** HA's `async_get_exposed_entities()` (`components/homeassistant/llm.py`, read raw) hands the LLM, per entity, exactly: `names`, `domain`, `state`, `areas`, and `attributes` filtered to a 14-item allowlist (`temperature`, `brightness`, `humidity`, `device_class`, `media_title`, …). There is **no `last_changed`, no `last_updated`, no `last_reported`, no availability field, no confidence, no reporting-contract metadata.** HA's own REST API *does* carry `last_changed`/`last_updated` — so this is an **active discard, not an upstream gap**. The only residual signal is HA's literal state string (`unavailable`/`unknown`), which conflates "device is off" with "I haven't heard from this device in three days" for any integration that keeps serving last-known values.

**FACT / HIGH — the MCP Resource is a thin wrapper over the same payload.** `components/mcp_server/server.py` defines `SNAPSHOT_RESOURCE_URI = "homeassistant://assist/context-snapshot"`, described as *"A snapshot of the current Assist context, matching the existing GetLiveContext tool output"*; `handle_read_resource` literally invokes `GetLiveContext` with empty args. Same payload, same missing metadata. *(Independently re-verified against the public integration page, which confirms the resource returns "a plain-text snapshot".)*

**Verified MCP servers** — each repo page and/or raw README opened:

| Name | Wraps | Repo / docs | Activity signal | Conveys freshness/staleness? |
|---|---|---|---|---|
| **HA MCP Server** (built-in) | HA Assist API | [docs](https://www.home-assistant.io/integrations/mcp_server/) | **3.1% of all HA installs**; Silver; 2025.2; Streamable HTTP + SSE | **No.** Verified in source |
| **HA MCP Client** (built-in) | External MCP → HA agents | [docs](https://www.home-assistant.io/integrations/mcp/) | **209 installs**; Silver; SSE-only per docs; **currently broken** (core#162601) | N/A (consumer) |
| **voska/hass-mcp** | HA REST | [repo](https://github.com/voska/hass-mcp) | listed on mcpservers.org; 15 tools | **Partial, off by default.** `DEFAULT_LEAN_FIELDS = ["entity_id","state","area","attr.friendly_name"]` — no timestamps. `DEFAULT_STANDARD_FIELDS` includes `last_updated`; the MCP *resource* is hardcoded `lean=True`. Raw pass-through, no derivation |
| **homeassistant-ai/ha-mcp** | HA (87–92 tools) | [repo](https://github.com/homeassistant-ai/ha-mcp) | **Metrics LOW** — three fetches returned 3.9k / 2.6k / 78 stars. Clearly the most active third-party server; exact numbers unreliable. README references HA 2026.6 | **No.** Grepped README for `last_changed\|last_updated\|stale\|freshness\|provenance\|confidence` — zero hits about device state |
| **robbrad/homeassistant-mcp** | HA | [repo](https://github.com/robbrad/homeassistant-mcp) | tool-search / progressive disclosure | **No** |
| **tevonsb/homeassistant-mcp** | HA | [repo](https://github.com/tevonsb/homeassistant-mcp) | widely mirrored | **No** |
| **ichbinder/MCP2ZigBee2MQTT** | Zigbee2MQTT / MQTT | [repo](https://github.com/ichbinder/MCP2ZigBee2MQTT) | 10★, 4 forks, 6 commits | **Closest to a yes — but misplaced.** Exposes `last_seen` only inside `get_recent_devices` (inventory). `get_device_state` — the tool an agent actually calls before acting — returns state with **no age** |
| **veonua/smartthings-mcp** | SmartThings API | [repo](https://github.com/veonua/smartthings-mcp) | ~5★, 29 commits | **No** |
| **abeardmore/hubitat-mcp** | Hubitat Maker API | [repo](https://github.com/abeardmore/hubitat-mcp) | ~4★, 3 commits | **No** |
| **homey-mcp/homey-mcp** | Homey Pro | [repo](https://github.com/homey-mcp/homey-mcp) | devices/zones/flows/insights | **No** |
| Domoticz / UniFi Protect / Homey-Wan-Kenobi / Rhombus / GMA2 MCP | various | listed at [Glama](https://glama.ai/mcp/servers/categories/home-automation-and-iot) | 29 / 62 / 60 / 31 / 100★ | **Not individually verified — directory listing only** |

**FACT / MED — directory scale.** Glama's Home Automation & IoT category lists **28 MCP servers**. PulseMCP advertises "Top 24 Home Assistant MCP Servers" — **search-snippet only; PulseMCP was ROBOTS_DISALLOWED and not read.**

**Absence findings (MED, per §0 rules):**
- **No MCP server speaks Matter or Thread natively.** Every "Matter" hit was standard coverage or a hub wrapper that happens to reach Matter devices. Fabric-level state — commissioning status, subscription health, report intervals — is exposed to agents by nobody found.
- **No commercial/vendor MCP offering for home automation.** Samsung describes "callable agents" without saying MCP; Josh.ai's 2026 keynote page has no MCP. Crestron/Control4/Savant searches returned only buyer guides. *What would answer this: vendor developer-portal changelogs rather than press coverage.*

**FACT / HIGH — the protocol itself does not help us.** The MCP spec revision dated **2026-07-28** (`https://blog.modelcontextprotocol.io/posts/2026-07-28/` — three days before this lane ran) adds `ttlMs` and `cacheScope` cache hints on **list results** and moves change notifications to a `subscriptions/listen` stream. Those are *transport/catalog* caching semantics — how long a client may cache a **tool list** — **not** data-freshness semantics for returned values. A community proposal asking for exactly that (`https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/2964`, opened 2026-06-22) requests a `verification` object with `producer`, `produced_at`, `input_hash`, `output_hash`, arguing *"the client receives content and has no standard, structured way to answer 'what produced this, when, and can I check it later?'"* and that *"Integrity metadata lets a consumer tell a fresh result from a stale or substituted one."* **Status: no visible maintainer response, discussion locked and unresolved.**

**FACT / MED — one precedent worth knowing.** Amazon's Smart Home skill API has carried `timeOfSample` and `uncertaintyInMilliseconds` in state reports for years (`https://developer.amazon.com/en-US/docs/alexa/smarthome/state-reporting-for-a-smart-home-skill.html`), with best-practice text: *"Update `timeOfSample` for the changed property only. For other properties, report the `timeOfSample` that reflects the last time the property changed."* The page gives no definition of `uncertaintyInMilliseconds` and says nothing about staleness thresholds. **UNVERIFIED whether any of it reaches the Alexa+ LLM.**

**INFERENCE / HIGH.** Across every implementation inspected the pattern is identical: *hand the model the platform's last-known value as if it were ground truth.* HA is the only one that even names the problem, and its fix is a prompt string (`"You MUST call GetLiveContext"`) that re-reads the same un-timestamped snapshot. **Re-reading a stale cache faster does not make it fresh.**

### 1d. Verdict on the lane — open or crowded?

**OPINION / HIGH confidence in the reasoning, MED in the market call: the *plumbing* lane is crowded and closing; the *truthfulness/provenance* lane is genuinely open — but open because it is unproven, not because nobody thought of it.**

**Crowded:** 28+ home-automation MCP servers on one directory; ≥10 wrapping HA specifically; HA's first-party server at 3.1% of installs (**INFERENCE / MED: ≈19,000 installs**, from 3.1% × the 625,530 active installations reported at `https://analytics.home-assistant.io/`). "Expose my hub's entities and services to an LLM over MCP" is a commodity rebuildable in a weekend.

**Open:** zero of the verified servers *derive* staleness — best case is raw `last_updated` pass-through, disabled by default for token economy. The protocol has no slot for it and the one proposal asking is unanswered and locked. No vendor is selling epistemics — Samsung, Josh.ai, Google, Amazon and Apple all describe *capability*, none describe *how they know*. And the documented failures are epistemic failures, not capability failures.

**OPINION / MED — the strategic read.** The defensible asset is not the MCP server; that is table stakes to ship early and cheaply for directory presence. It is **read-time staleness derivation from a per-entity reporting contract**, because that requires an event-sourced substrate none of these wrappers have. Every server in the table is a stateless proxy over a hub's current-value store; none of them *can* express *"last confirmed 4 h ago, contract says 15 min, therefore UNKNOWN not OFF"* however much they wanted to.

**The countervailing risk, stated plainly: HA could add `last_changed` to `async_get_exposed_entities()` in a single PR and claim ~80% of the *perceived* value.** The raw timestamp is one line away. Our moat is **contract + derivation + explanation**, not the timestamp — position accordingly and expect the timestamp itself to be commoditised within a release or two.

**Two asymmetries to carry into the charter:** (1) **3.1% vs 209 installs** — users overwhelmingly want to control the home *from* an external agent, not give the home's agent more tools. Build for the **inbound** direction. (2) HA's inbound server supports Streamable HTTP while the outbound client is SSE-only-per-docs and **currently broken** — the inbound path is where both the maintained code and the users are.

**Highest-value unread document:** OpenHomeFoundation roadmap issue #16, titled **"Voice is more transparent"**, referenced from `https://github.com/OHF-Voice/linux-voice-assistant/discussions/281` (posted 2026-03-31). Not opened. That title is adjacent enough to our thesis that someone should read it before the charter locks.

---

## §2 — Matter/Thread trajectory

### 2a. Spec state

**Matter — from CSA's own newsroom (all FACT / HIGH unless noted):**

| Version | Date | Added |
|---|---|---|
| **1.4** | 2024-11-07 | Home Router & Access Point; Enhanced Multi-Admin; **ICD Long Idle Time (LIT) + Check-In Protocol**; energy device types; radar & vision occupancy sensing |
| **1.4.1** | announced 2025-05-07 | Enhanced Setup Flow; multi-device setup QR; NFC onboarding info |
| **1.4.2** | 2025-08-11 | Wi-Fi-only commissioning (no BLE); Vendor ID Verification; Access Restriction Lists; CRLs; certifiable Scenes; **"Quieter Reporting"**; Endpoint Unique IDs |
| **1.5** | 2025-11-20 | Cameras (WebRTC); unified Closures; soil sensors; energy tariffs; EV bidirectional charging; TCP transport / large messages |
| **1.5.1** | 2026-03-31 | Camera multi-stream, HEIC, HLS/DASH, PTZ fixes |
| **1.6** | **2026-06-17** | Full NFC commissioning; **Joint Fabric** (multiple controllers co-administering one network, counting as *one* fabric); Thermostat Suggestions; **Device Capability and Limits communication**; Security Sensor Event History; partitioned CRLs |

Sources: [1.4](https://csa-iot.org/newsroom/matter-1-4-enables-more-capable-smart-homes/) · [1.4.1](https://csa-iot.org/newsroom/a-smarter-start-matter-1-4-1-makes-setup-easier/) · [1.4.2](https://csa-iot.org/newsroom/matter-1-4-2-enhancing-security-and-scalability-for-smart-homes/) · [1.5](https://csa-iot.org/newsroom/matter-1-5-introduces-cameras-closures-and-enhanced-energy-management-capabilities/) · [1.5.1](https://csa-iot.org/newsroom/matter-1-5-1-enhancing-camera-performance-and-expanding-device-flexibility/) · [1.6](https://csa-iot.org/newsroom/matter-1-6-enables-more-intuitive-setup-multi-ecosystem-experiences-and-context-driven-control/) *(1.6 date and contents independently re-verified by the lane author.)* Product Security 1.1 shipped the same day as 1.6 ([9to5Mac, 2026-06-17](https://9to5mac.com/2026/06/17/matter-1-6-and-product-security-1-1-officially-announced-heres-whats-new/)).

- **FACT / HIGH — Matter 1.6 is the latest *released* spec as of 2026-07-31.** Nothing above it on CSA's download page.
- **INFERENCE / MED — 1.6.1 is in development, not released.** The SDK's generated `docs/ids_and_codes/spec_clusters.md` (read raw) already carries a `1.6.1` column: `|1.0|1.1|1.2|1.3|1.4|1.4.1|1.4.2|1.5|1.5.1|1.6|1.6.1|`. No CSA announcement, no download entry.
- **FACT / HIGH — ICD Management cluster is `0x0046` (70), PICS `ICDM`, certifiable since Matter 1.2** and in every release since (same generated file).

**Thread:**
- **FACT / HIGH — Thread 1.4 released 2024-09-04** ([Thread Group](https://threadgroup.org/Newsroom/Blog/thread-14-paves-the-path-for-smart-devices-to-work-together-regardless-of-their-ecosystem-or-manufacturer)): "when adding an updated device or Thread Border Router, it will join the existing Thread network versus creating a new one." Adds Thread-over-Infrastructure.
- **FACT / MED — current published spec is Thread 1.4.1** ([threadgroup.org/ThreadSpec](https://threadgroup.org/ThreadSpec)) — the page is titled 1.4.1 but carries **no date**, and no dated 1.4.1 announcement was found. Spec behind a request form; not read.
- **FACT / MED (secondhand) — Thread 1.4 became the sole Border Router certification on 2026-01-01** ([Bitdefender, 2025-09-03](https://www.bitdefender.com/en-us/blog/hotforsecurity/thread-1-4-slow-rollout)). Same piece: "Adding a new Border Router creates yet another network instead of joining the existing one."

### 2b. Liveness & ICD semantics — the mechanism

**One-sentence answer: Matter has no "online" attribute. Liveness is entirely a property of the subscription transaction, and it is a single derived boolean — "did a report arrive within MaxInterval + round-trip allowance?"**

**(i) Subscriptions are the heartbeat — FACT / HIGH.** From Matter SDK `src/app/ReadClient.cpp` on `master` (read raw), `ComputeLivenessCheckTimerTimeout`:

```
*aTimeout = System::Clock::Seconds16(mMaxInterval) + roundTripTimeout;
```

In-source comment: *"To calculate the duration we're willing to wait for a report to come to us, we take into account the maximum interval of the subscription AND the time it takes for the report to make it to us in the worst case."* Expiry fires `OnLivenessTimeoutCallback` → logs `Subscription Liveness timeout with SubscriptionID = ...` → resubscribe. Overridable via `OverrideLivenessTimeout()`.

**INFERENCE / HIGH — and this is the finding that matters most in §2.** Because the client declares death purely on "no report within MaxInterval + RTT," the publisher must emit *something* every MaxInterval even when nothing changed. **MaxInterval is therefore a negotiated, protocol-level, per-node freshness contract.** The controller knows, machine-readably, the maximum age of its own knowledge. **This is our reporting-contract concept, already standardised, already present, and surfaced by nobody.**

**FACT / HIGH — negotiation is client-proposes / server-decides.** Client sends `MinIntervalFloor` and `MaxIntervalCeiling`; server returns the actual `MaxInterval`. For ICDs the server may raise it far above the request: `MinIntervalRequested ≤ MaxInterval ≤ MAX(IdleModeInterval, MaxIntervalRequested)` ([Silicon Labs Matter ICD guide](https://docs.silabs.com/matter/latest/matter-overview-guides/matter-icd)). **A controller cannot force a battery device to prove liveness more often than the device wants to.**

**(ii) SIT vs LIT — FACT / HIGH** (same Silabs source):
- **SIT (Short Idle Time):** polling intervals "small enough to guarantee that a message sent from a client will be able to reach the ICD without any synchronization." Locks etc. Effectively always addressable.
- **LIT (Long Idle Time):** requires "synchronization between the client and the ICD for communication to succeed." Deep-sleeping sensors.

| Attribute | Range | Meaning |
|---|---|---|
| `IdleModeInterval` | **1 – 64800 s (18 h)** | max time in idle mode |
| `ActiveModeInterval` | min 300 ms | min time active |
| `ActiveModeThreshold` | min 300 ms | stay-awake window after activity |

Recommended: SIT = 600 s idle / 10 s active / 1 s threshold; LIT = 3600 s idle / 0 s active / 5000 ms threshold. *(Silabs naming; the spec renamed these `IdleModeDuration` / `ActiveModeDuration` / `ActiveModeThreshold`.)*

**INFERENCE / HIGH — the crux stated plainly:** for a LIT ICD with `IdleModeInterval = 64800`, **"asleep" and "dead" are indistinguishable at the transport layer for up to 18 hours**, and no probe resolves it — probing is exactly what LIT exists to prevent.

**(iii) Check-In Protocol — FACT / HIGH.** The only push-side liveness primitive: "a fail-safe mechanism which allows an ICD to notify a registered client that it is available for communication when all subscriptions between the client and ICD are lost." Sessionless, authenticated by a shared secret established at client registration via the ICD Management cluster.
**FACT / MED — as of late 2025 no major ecosystem had shipped LIT/check-in.** [Matter Alpha, 2025-12-04](https://www.matteralpha.com/news/google-and-apple-are-ready-to-optimize-your-battery-powered-sensors): "Apple and Google have wrapped up development of this feature internally, though it has not yet been released"; "no major ecosystems support this feature… certain Matter controllers even frequently pull data from devices without distinguishing if they are battery-powered." *(Trade press, ~8 months stale.)*

**(iv) No node-level "online" attribute — INFERENCE / MED-HIGH.** Matter's only `Reachable` attribute lives on **Bridged** Device Basic Information (`0x0039`), not Basic Information (`0x0028`). Behavioural evidence from HA's Matter entity base class (`components/matter/entity.py` on `dev`, read raw):

```python
self._attr_available = (
    self._endpoint.node.available and self._get_bridged_reachable()
)
```

and `_get_bridged_reachable()` ends:

```python
reachable = self.get_matter_attribute_value(
    clusters.BridgedDeviceBasicInformation.Attributes.Reachable
)
if reachable is None:
    return True
return bool(reachable)
```

**Note the fail-open default: absent `Reachable` ⇒ `True`.** And when present, `Reachable` is *a bridge's assertion about a third-party device behind it* — second-hand testimony whose own staleness policy is unknowable to the controller.
**UNVERIFIED — confirming no reachability attribute exists on cluster 0x0028.** *What would answer this: the Basic Information attribute table in the Matter 1.6 Application Cluster Specification PDF (behind CSA's download form).*

**(v) What a real controller actually does — FACT / HIGH.** `python-matter-server/matter_server/server/device_controller.py` (1757 lines, read raw), verbatim constants:

```python
NODE_SUBSCRIPTION_FLOOR_DEFAULT = 1
NODE_SUBSCRIPTION_FLOOR_ICD = 0
NODE_SUBSCRIPTION_CEILING_WIFI = 60
NODE_SUBSCRIPTION_CEILING_THREAD = 60
NODE_SUBSCRIPTION_CEILING_BATTERY_POWERED = 600
NODE_RESUBSCRIBE_ATTEMPTS_UNAVAILABLE = 2
NODE_RESUBSCRIBE_TIMEOUT_OFFLINE = 30 * 60
NODE_PING_TIMEOUT = 10
NODE_PING_TIMEOUT_BATTERY_POWERED = 60
NODE_MDNS_SUBSCRIPTION_RETRY_TIMEOUT = 30 * 60
```

Ceiling selection keys off `ThreadNetworkDiagnostics.routingRole`: no cluster ⇒ Wi-Fi (60 s); `kSleepyEndDevice` ⇒ **600 s**; else Thread router (60 s). ICD detection sets floor 0 with the comment *"for ICD devices, the interval floor must be 0 according to the spec, to prevent additional battery drainage. See Matter core spec, chapter 8.5.2.2."*

State machine, in order:
- **Fail-closed on boot (good):** `# always mark node as unavailable at startup until subscriptions are ready` → `node.available = False`.
- `node.available = True` **immediately** on subscription establishment.
- `resubscription_attempted()` only calls `_node_unavailable()` at `resubscription_attempt >= 2`, comment: *"We debounce it a bit so we only mark the node unavailable after some resubscription attempts."* **This is a deliberate, coded-in false-ALIVE window.**
- After 30 min of failed resubscribes the subscription is torn down.
- **A second, independent liveness channel exists:** mDNS. `_node_last_seen_on_mdns[node_id] = time.time()`, used to trigger setup/resubscribe (*"we only treat UPDATE state changes as ADD if the node is marked as unavailable"*).
- `ping_node` exists but is a **manual diagnostic**, not part of the availability loop — and partly trusts the very bit it is meant to test.

**Answering "evidence vs assumption" directly — INFERENCE / HIGH.** Matter's subscription *is* evidence-based at the protocol layer: a report is proof the device answered within a known bound. Three things degrade it to assumption before it reaches an app:
1. It is **collapsed to a boolean with no exposed timestamp** (`node.available: bool`, `_attr_available: bool`). Nothing carries "last heard from at T."
2. It is **deliberately debounced** (2 attempts) and **negotiated coarse** (600 s sleepy; up to 64800 s LIT).
3. **Command paths are assumption-based.** Invoke/Write yield transport status; nothing obliges the controller to wait for a report confirming physical effect, and there is no `Reachable` to consult. Truth returns only on the next subscription report.

There is **no per-attribute freshness anywhere in the chain**. Attribute values persist at last-known values for as long as `available` is `True`.

### 2c. Adoption honesty — exhibits

| Source | Date | Claim | Link |
|---|---|---|---|
| matter-smarthome.de — "The Matter Standard in 2026" | 2026-01-03 (mod. 01-12) | "over 750 products". Ecosystems lag: "many ecosystems are still at the Matter 1.2 or 1.3 stage." IKEA's Bilresa remote "does not work in the Google ecosystem"; Klippbok "fails to integrate with Amazon." Thread battery life behind Zigbee ("three years" vs "more likely to be two"). "Hardly any vendors and only a few platforms communicate publicly about how far they are with implementation." | [link](https://matter-smarthome.de/en/development/the-matter-standard-in-2026-a-status-review/) |
| Tom's Guide | 2026-02-06 | IKEA's new Matter-over-Thread line "failing to connect up to 50% of the time." Verge: of six devices "only one connected properly after seven attempts." Reddit user: "Of the 59 remotes I bought, 29 have paired." | [link](https://www.tomsguide.com/home/smart-home/ikeas-new-matter-smart-home-devices-are-struggling-to-stay-connected-but-a-firmware-fix-is-in-the-works) |
| **core#127759** — "Matter devices connected over Thread regularly become unavailable" | opened Oct 2024, **still open** | Devices **pingable and controllable via vendor app while HA shows unavailable**. Maintainer: "The problem appears to be related to when RF links are not strong enough. In theory, this should be alleviated by TREL, but this seems not to work (correctly) in practice." And: **"Using multiple Border routers is simply broken atm. Using just one and it will be stable."** Devices fail CASE despite being network-reachable. Maintainers indicate this is **not HA-specific**. | [link](https://github.com/home-assistant/core/issues/127759) *(re-verified)* |
| Apple Developer Forums #783080 | May 2025 | LIT ICD switch: "when the device is rebooted the subscription doesn't appear to resume successfully and the buttons no longer work." `Failed to establish CASE for subscription-resumption with error '32'`. "After about 10-15 minutes the Apple TV initiates a new case session…" | [link](https://developer.apple.com/forums/thread/783080) |
| **matterjs-server#494 — "Matter.js does not communicate 'unavailable' state to HA"** | opened **2026-04-06**, now **closed** (PR #515) | **The purest false-ALIVE exhibit.** Device loses power; matter.js correctly marks it offline; **HA keeps showing it available.** Reporter: "HA Core is not getting a message that it 'understands' to mark a device as 'Unavailable' when a device is declared as offline in matter.js." Matter.js never sent the availability-changed event HA expects; the Python server had explicitly sent "Marked node as unavailable." | [link](https://github.com/matter-js/matterjs-server/issues/494) *(re-verified)* |
| HA addons#4355 | opened 2026-01-29, closed | 100-device install: "about an hour later about 50 devices give or take are constantly offline," churning. Pre-existing pattern: "after an HAOS or Matter Server reboot, I would experience a slew of offline Matter devices exactly 6 hours later." | [link](https://github.com/home-assistant/addons/issues/4355) |
| HA Community | 2026-01-21 | "every six hours, on the dot… a big chunk of my Matter Server nodes go offline and then slowly come back online after 30-60 minutes." 4 border routers. | [link](https://community.home-assistant.io/t/matter-over-thread-devices-go-offline-every-6-hours-on-the-dot-or/977351) |
| XDA | 2026-07-24 | HA replaced its C++/CHIP Python Matter server with pure-TypeScript matter.js — "no native CHIP dependency at all." Motivation was maintenance, not correctness. | [link](https://www.xda-developers.com/home-assistant-quietly-rewrote-its-matter-server-from-python-to-typescript-heres-what-changed/) |
| HA official blog — "The Matter upgrade you've been waiting for" | 2026-06-23 | First-party framing: "greater stability… fewer bugs, and faster start-up and recovery"; "devices now come back online much faster." **Note the implicit admission — recovery is the thing being fixed.** New network visualisation exposes role (leader / router / **sleepy** / end device) and link quality. | [link](https://www.home-assistant.io/blog/2026/06/23/the-matter-upgrade-youve-been-waiting-for/) |
| How-To Geek / Yahoo | 2025-10-13 | "Matter is creating more headaches than solutions." **Its specific claim that Apple is "only on version 1.2" and Google "still on 1.0" is flagged LOW and uncorroborated — do not repeat it.** | [link](https://tech.yahoo.com/home/articles/matter-promised-smart-home-unity-143016750.html) |

**OPINION / MED-HIGH — adoption read.** Spec cadence is genuinely fast and healthy (six releases in 20 months), but ecosystem implementation lags the spec by roughly 2–4 minor versions, and the *reliability* complaints in 2026 are the same as in 2024 — Thread mesh / border-router pathology and availability churn — not feature gaps. **The 2026 failure mode has moved from "won't pair" to "pairs, then lies about being there,"** which is worse for a system automations depend on.

### 2d. Does Matter solve availability-truth?

> **VERDICT — OPINION / HIGH: No. Matter *bounds* the lie but does not eliminate it, and every layer above the subscription re-introduces it.**

**What Matter genuinely gives (do not discount this):** the negotiated `MaxInterval` is a **per-node, protocol-enforced, machine-readable staleness bound**. A controller can know "my knowledge of node N is at most 60 s / 600 s old" from the transport, without heuristics. That is materially better than cloud-polled or fire-and-forget local protocols, and it is the correct raw material.

**What Matter does not give:** any obligation anywhere to *carry that bound upward*. No node-level `Online`/`LastSeen` attribute (only bridge-hearsay `Reachable` on 0x0039), no per-attribute freshness, and no exposed distinction between "device confirmed the command took effect" and "we sent a command."

**Where the lie enters — walk the chain:**

| Hop | Truth available here | How the lie is introduced |
|---|---|---|
| Device (LIT ICD) | Device knows it's alive | Nothing observable. Asleep ≡ dead for up to `IdleModeInterval` (**max 64800 s = 18 h**). Only Check-In distinguishes them — and major ecosystems hadn't shipped it as of Dec 2025 |
| Radio / Thread mesh | RF link state | Path-specific, not device-specific. #127759: device IP-pingable and app-controllable yet **Matter-dead** because CASE won't form. A healed path can hide that it ever broke |
| Border router | Route existence | Multi-BR "pingpong" and BR restarts (6-hourly cycles) desynchronise reachability from device health. First place where "I can reach it" ≠ "it is there" |
| Controller / SDK | `MaxInterval + roundTripTimeout` — a real bounded evidence window | **Lie #1 — the blind window:** between last report and timeout, alive is *assumed*. 60 s Wi-Fi/router, **600 s sleepy**, more for LIT. **Lie #2 — the debounce:** `NODE_RESUBSCRIBE_ATTEMPTS_UNAVAILABLE = 2`, extending it further, by design |
| Integration state machine | Knows *when* the last report arrived | **Lie #3 — the boolean collapse:** timestamp discarded. **Lie #4 — the translation gap:** matterjs#494, truth existed and was lost between processes |
| UI | Nothing independent | **Lie #5 — stale values render as current:** a 9-minute-old reading and a 1-second-old reading are visually identical. **Lie #6 — fail-open bridging:** `if reachable is None: return True` |
| Command path | Transport status only | **Lie #7 — assumed effect:** no confirm-by-report requirement; the next report may be `MaxInterval` away |

**INFERENCE / MED — two spec-level trends *widen* the window rather than narrow it:**
1. **"Quieter Reporting" (1.4.2, 2025-08-11)** — CSA describes it as defining "when and how often devices should report attribute changes" to reduce network utilisation. Fewer reports ⇒ coarser liveness resolution. **The spec is optimising bandwidth/battery against freshness, and freshness is losing.**
2. **LIT ICD (1.4, 2024-11-07)** — the entire point is to make devices unreachable for long stretches; the compensating control (Check-In) is what ecosystems hadn't shipped.

**Bet-relevant conclusions:**
- **OPINION / HIGH — Matter is a good *source* of evidence and a bad *carrier* of it.** The negotiated `MaxInterval` **is** a per-entity reporting contract, already there, per node, machine-readable. Harvesting it (plus `IdleModeDuration`/`ActiveModeDuration` from cluster `0x0046`) as the contract value, alongside a last-report timestamp, is available today from any CHIP/matter.js-based stack.
- **FACT / HIGH — do not treat controller `available` as ground truth.** It is a lagging, debounced, fail-open boolean; both HA implementations have shipped bugs where it was wrong in the shows-alive-while-dead direction, and the debounce is *intentional*.
- **INFERENCE / HIGH — "never falsely report ALIVE" is not achievable from Matter alone for LIT devices.** The honest statement is *"last confirmed alive at T; contract permits silence until T + IdleModeDuration."* Matter can supply both numbers. **That sentence is our product, expressed in their vocabulary.**
- **FACT / MED-HIGH — mDNS operational-node advertisements are a genuine second, independent liveness channel**, already consumed by python-matter-server. Treat as corroborating evidence, not primary.

---

## §3 — The MG24 dual-protocol angle

### 3a. Silicon capability

- **FACT / HIGH.** Silicon Labs documents the EFR32MG24 as a multiprotocol 2.4 GHz SoC. Product-page protocol table, verbatim: `Matter`, `OpenThread`, `Zigbee`, `Bluetooth Low Energy (Bluetooth 6.0)`, `Bluetooth mesh`, `Proprietary 2.4 GHz`, `Multiprotocol`. Radio: up to 19.5 dBm TX; −105.4 dBm sensitivity @ 250 kbps OQPSK DSSS. Secure Vault, TrustZone, secure boot. — [silabs.com/wireless/zigbee/efr32mg24-series-2-socs](https://www.silabs.com/wireless/zigbee/efr32mg24-series-2-socs)
- **FACT / HIGH.** Datasheet Rev 1.2 (© 2024) lists the same protocol set plus "Multiprotocol"; up to 1536 kB flash / 256 kB RAM. — [datasheet PDF](https://www.silabs.com/documents/public/data-sheets/efr32mg24-datasheet.pdf)
- **FACT / MED (precision caveat).** The datasheet uses only the bare word "Multiprotocol" — **not** "concurrent multiprotocol" or "dynamic multiprotocol". Those are defined a level up in the Multiprotocol SDK docs, which distinguish **Concurrent Multiprotocol** (simultaneous) from **Dynamic Multiprotocol** (time-sliced). — [docs.silabs.com/multiprotocol/1.2.0](https://docs.silabs.com/multiprotocol/1.2.0/multiprotocol-overview/)
- **FACT / HIGH.** Silabs' Linux multiprotocol architecture doc enumerates four supported configurations: **Multi-PAN 802.15.4 RCP**, **Multiprotocol RCP**, **Zigbee NCP + OpenThread RCP**, **Zigbee NCP + BLE NCP**. Host side = **CPCd** + **zigbeed** + OTBR + BlueZ. Stated caveat: configs 3–4 have "a larger application footprint, it is recommended to choose parts with sufficient RAM (>64kB)". — [system-architecture](https://docs.silabs.com/multiprotocol/latest/multiprotocol-solution-linux/system-architecture)

**Bottom line: the silicon is unambiguously capable. Nothing in hardware blocks Zigbee+Thread. The constraint is entirely software.**

### 3b. Firmware reality — the crux, and the brief's premise needs correcting

**The widely-repeated claim "Silicon Labs deprecated multi-PAN" is, as stated, WRONG.** What got deprecated was (i) a Silabs Docker *delivery container*, and (ii) the *Home Assistant add-on*. The feature itself still ships and is still supported by the silicon vendor. **The host ecosystem killed it, not Silicon Labs.**

**FACT / HIGH — Silicon Labs has NOT deprecated multi-PAN or zigbeed.** EmberZNet SDK 8.1 GA release notes (Rev 3, **2025-08-06**) list exactly one relevant deprecation, and it is the container: *"The 'Multiprotocol Container' which is currently available on DockerHub…will be deprecated in an upcoming release."* No multiprotocol / multi-PAN / zigbeed / RCP / CPC entry under Removed Items. In the same release zigbeed **gained** platform support (Tizen-13.1, Android 12), RCP reached **GA on OpenWRT**, and multi-PAN received active bug fixes. — [release notes PDF](https://www.silabs.com/documents/public/release-notes/emberznet-release-notes-8.1.3.0.pdf)

**FACT / HIGH — current Simplicity SDK Zigbee release notes v2025.12.3, released 2026-05-04** (under three months old) still ship zigbeed; multi-PAN and multiprotocol referenced as live features. Only deprecation listed is the unrelated Zigbee Classic Key Storage component. — [sisdk release notes](https://docs.silabs.com/sisdk-release-notes/2025.12.3/sisdk-zigbee-release-notes/sisdk-zigbee-sdk-release-notes)

**FACT / HIGH — current Silabs docs across three doc-sets (Zigbee v9.1.1, OpenThread latest, Multiprotocol v1.2.0) still present multi-PAN RCP as active and supported**, with no deprecation, EOL or "not recommended" language. The single deprecation string is container-scoped. — [zigbee](https://docs.silabs.com/zigbee/latest/multiprotocol-solution-linux/) · [openthread](https://docs.silabs.com/openthread/latest/multiprotocol-solution-linux/) · [overview](https://docs.silabs.com/zigbee/latest/zigbee-multiprotocol-overview/)

**FACT / MED — Silabs' own performance claim:** multi-PAN RCP throughput "comparable to that of a single-protocol SoC device." Only the Introduction section was read (HTML); the results chapters and their caveats were not. — [link](https://docs.silabs.com/zigbee/latest/multi-pan-rcp-performance-for-openthread-and-zigbee/01-introduction)

**Who actually deprecated it — all three major host stacks. FACT / HIGH, dated:**

- **Home Assistant.** Dec 2022 SkyConnect ships experimental multiprotocol. **2024-01-25**, HA blog *The State of Matter*: *"While Silicon Labs' multiprotocol works, it comes with technical limitations. These limitations mean users will not have the best experience compared to using dedicated Zigbee and Thread radios"* and *"We do not recommend using this firmware."* HA developer *puddly*: *"Multiprotocol was frozen last year and will be formally deprecated in an upcoming release. It has not been possible to set up multiprotocol automatically for many many months."* **July 2025** — formal deprecation PR: *"Formally deprecate the addon… you should find an alternative way to run both Zigbee and Thread if you use both with the same adapter."* Add-on renamed **"Silicon Labs Multiprotocol [deprecated]"**. **Verified live today:** manifest still exists at v2.4.5, `stage: deprecated`. A migration repair flashing users back to single-protocol reports ~**4,400 active installs** still on it. — [blog](https://www.home-assistant.io/blog/2024/01/25/matter-livestream-blog/) · [core#142466](https://github.com/home-assistant/core/issues/142466) · [addons#3833](https://github.com/home-assistant/addons/pull/3833) · [config.yaml](https://raw.githubusercontent.com/home-assistant/addons/master/silabs-multiprotocol/config.yaml) · [core#168431](https://github.com/home-assistant/core/pull/168431)
- **ZHA / zigpy** (in-thread 2025-11-08): *"We do not support any Multiprotocol solutions anymore"* and *"avoid any Multiprotocol solutions and just get a second adapter. One for Zigbee, one for Thread."* — [discussion](https://github.com/darkxst/silabs-firmware-builder/discussions/41)
- **Zigbee2MQTT:** *"Multiprotocol firmware is not supported. The recommended alternative to establish multiple networks is to use one adapter per protocol."* Z2M supports EmberZNet 7.4.x–8.2.x (EZSP v13+) and lists the SONOFF Dongle-PMG24 as supported. — [emberznet guide](https://www.zigbee2mqtt.io/guide/adapters/emberznet.html)

**FACT / HIGH — the closest precedent to our exact hardware class: HA Connect ZBT-2 (MG24), announced 2025-11-19, $49 / €45.** *(Independently re-verified by the lane author.)* HA states: **"Connect ZBT-2 cannot do both Zigbee and Thread simultaneously."** And: **"Though it is theoretically possible with the hardware within Connect ZBT-2, in our experience, this functionality doesn't work well, and we don't plan to implement it."** They tested it on ZBT-1 and "found its operation to be inconsistent, often causing device stability issues," concluding **"multiprotocol is not suitable for operation in the home."** Switching is a firmware flash with a hard warning: *"This guide installs firmware that supports only Thread! You will no longer be able to control your Zigbee devices with this adapter after installing the Thread firmware."* — [blog](https://www.home-assistant.io/blog/2025/11/19/home-assistant-connect-zbt-2/) · [docs](https://www.home-assistant.io/connect/zbt-2/) · [Nabu Casa KB](https://support.nabucasa.com/hc/en-us/articles/31347057208989-Switching-from-Zigbee-to-Thread-support-on-Home-Assistant-Connect-ZBT-2)

**FACT / MED — the dissenting voice is SONOFF itself.** Blog *"Multiprotocol is Not Dead"* (mod. 2025-06-06) claims re-engineered MultiPAN with "Silicon Labs' official support," **v4.6.0** tested with "100 Zigbee devices [and] 50 Thread devices… continuously for 5 weeks without any crashes or instability," 100% success. **MED because:** vendor self-report, no third-party replication found, and the stress test was on the **MG21** ZBDongle-E, not MG24. — [link](https://dongle.sonoff.tech/guide/zbdongle-e/multiprotocol_is_not_dead/)

**FACT / HIGH — and this is the practical killer.** SONOFF's own how-to (2025-07-11) for MultiPAN on Dongle-PMG24 requires installing **the deprecated HA Silicon Labs Multiprotocol add-on from a *custom* repository**, and states **"Only Zigbee2MQTT (Z2M) is supported"** — ZHA does not work because "MultiPAN firmware is built on EZSP v16" while ZHA requires EZSP v14. Flashing also **changes the dongle's IEEE address**, breaking existing networks and forcing re-pairing. OpenThread support described as "experimental." — [link](https://sonoff.tech/blogs/news/how-to-use-multipan-in-home-assistant-with-sonoff-dongle)

**INFERENCE / HIGH.** Multi-PAN is *technically alive at the silicon vendor and dead at every host stack that matters*. Note the version fork: MultiPAN firmware sits on **EZSP v16**, a different rail from our **EZSP v13** single-protocol NCP line. Adopting it means leaving the mainstream EmberZNet NCP path, depending on a deprecated add-on served from a custom repo, and being locked out of ZHA. **That is a maintenance liability, not an option.**

### 3c. What MG24 dongles actually run today

| Firmware | Protocol | Source / repo | Notes |
|---|---|---|---|
| **EmberZNet NCP (EZSP)** | Zigbee only | SONOFF Dongle Flasher; [darkxst/silabs-firmware-builder](https://github.com/darkxst/silabs-firmware-builder); [NabuCasa/silabs-firmware-builder](https://github.com/NabuCasa/silabs-firmware-builder/releases/tag/v2026.02.23) | **The default and only mainstream path.** Dongle Plus MG24 ships 7.4.5, upgradeable to 8.0.2 [GA]. Z2M supports 7.4.x–8.2.x. Fully supported by ZHA + Z2M |
| **Zigbee Router** | Zigbee only | SONOFF matrix; darkxst | Range extender, not coordinator |
| **OpenThread RCP** | Thread only | NabuCasa builder (Thread targets: ZBT-2, Yellow); darkxst | Marked **experimental**. Requires OTBR on host. **Replaces** Zigbee |
| **MultiPAN RCP v4.6.0** | Zigbee + Thread concurrent | SONOFF Dongle Flasher (Dongle-PMG24 ✅); darkxst builds it | **EZSP v16.** darkxst: *"the RCP MultiPAN in multiprotocol mode is no longer recommended because running multi-protocol with multiple active networks on a single radio adapter has proven to not be stable."* Needs deprecated HA add-on from custom repo. **Z2M only — ZHA incompatible. Changes IEEE address** |

Verified: darkxst latest release 20250627 (2025-06-27), supports Sonoff Dongle Plus MG24, SMLIGHT SLZB-07Mg24, Seeed Xiao MG24, Sparkfun MGM240P · NabuCasa v2026.02.23 (released 2026-02-24), Zigbee for ZBT-1/ZBT-2/Yellow, Thread for ZBT-2/Yellow, **no multi-PAN images offered** · [SONOFF supported-firmware matrix](https://dongle.sonoff.tech/guide/dongle-pmg24/supported_firmware/) (Zigbee NCP ✅, Zigbee Router ✅, OpenThread RCP ✅, MultiPAN RCP ✅) · [itead firmware repo](https://github.com/itead/Sonoff_Zigbee_Dongle_Firmware) latest v7.4.4 (2025-01-14) — **partially verified**, per-file MG24 listings did not render.

**FACT / HIGH — switching protocols is a flash operation, not concurrency.** Every mainstream vendor treats it that way.

### 3d. Option value

**(i) Can one MG24 dongle serve a Thread/Matter future without hardware replacement?**

**INFERENCE / HIGH — yes for a *migration*, no for *coexistence*.** The silicon supports Thread and OpenThread RCP firmware for MG24 sticks is published and buildable, so there is no forced hardware replacement to *reach* Thread. Realistic cost:
- **A re-flash that is destructive to Zigbee.** The Zigbee network must be migrated to another controller first or lost, along with entity customisations.
- **On SONOFF specifically, flashing changes the IEEE address**, so devices need re-pairing — materially worse than a clean coordinator backup/restore.
- **Concurrency is available on paper, not in practice** (EZSP v16, ZHA-incompatible, Z2M-only, deprecated add-on from a custom repo, called unstable by the firmware builder himself).

**INFERENCE / MED — the reliability risk is ecosystem-attested, not vendor-attested.** Silabs claims comparable throughput and has issued no deprecation. Negative evidence is all downstream: HA's Jan-2024 "technical limitations," a community advisory to "not advise connecting more than 30 devices if using RCP Multi-PAN mode" (2024-02-15, against firmware 4.3/4.4), and darkxst's note that each 4.x release "breaks ABI." SONOFF's v4.6.0 claims are newer and unreplicated.

**INFERENCE / HIGH — the strategic read: a single MG24 is a *sequential* dual-protocol asset, not a *simultaneous* one.** Its option value is the option to **switch**, not to do both. Nobody credible is building toward one-radio concurrency — Nabu Casa shipped an MG24 product in Nov 2025 and said explicitly "we don't plan to implement it."

**(ii) Second-dongle pricing, verified 2026-07-31:**

| Product | Chip | Price | Source |
|---|---|---|---|
| SONOFF Dongle Plus MG24 | EFR32MG24 | **$35.90** | [sonoff.tech](https://sonoff.tech/en-us/products/sonoff-zigbee-thread-usb-dongle-dongle-plus-mg24) |
| SONOFF Dongle Plus MG24 | EFR32MG24 | **$35.49**, 36 in stock | [cloudfree.shop](https://cloudfree.shop/product/sonoff-dongle-plus-mg24/) |
| SONOFF Dongle Plus MG24 | EFR32MG24 | **$32.90** direct / $35.90 Amazon | [CNX Software, 2026-01-18](https://www.cnx-software.com/2026/01/18/getting-started-with-sonoff-dongle-plus-mg24-zigbee-adapter-using-home-assistant/) |
| SONOFF Dongle Max (Dongle-M) | MG24 + ESP32D0WDR2, PoE/Wi-Fi/USB-C | **$42.90** (sale) | [sonoff.tech](https://sonoff.tech/en-us/products/sonoff-dongle-max-zigbee-thread-poe-dongle-dongle-m) |
| HA Connect ZBT-2 | MG24 + ESP32-S3 | **$49 / €45** MSRP; **$48.95** (399 in stock) | [HA](https://www.home-assistant.io/connect/zbt-2/) · [cloudfree.shop](https://cloudfree.shop/product/home-assistant-connect-zbt-2/) |

**INFERENCE / HIGH.** A second dedicated radio costs **~$33–49** — the option every host stack explicitly recommends. Against maintaining a deprecated, ZHA-incompatible, custom-repo MultiPAN integration, **a ~$35 second stick is not a close call.**

**FACT / HIGH — naming correction for the brief.** There is no "SONOFF ZBDongle-M." SONOFF's MG24 products are the **Dongle Plus MG24 (Dongle-PMG24)** (USB) and the **Dongle Max (Dongle-M)** (MG24 + ESP32D0WDR2, PoE/Ethernet/Wi-Fi/USB-C, web-console firmware switching). The ZBDongle-E is MG21, as the brief correctly noted.

**UNVERIFIED — Silabs' *forward* intent for multi-PAN beyond current docs.** No Silabs forum roadmap post or PCN was reachable. *What would answer this: a Silicon Labs product-change notice, an official forum roadmap post, or a Simplicity SDK deprecation-schedule page naming multi-PAN.*

---

## §4 — Presence/occupancy edge sensing

### 4a. mmWave landscape

**Module tier — Hi-Link family. The recommended part changed; LD2410 is the volume part but no longer the default choice for new designs.**

| Part | Price (cited, 2026-07-31) | Maturity | Notes |
|---|---|---|---|
| **LD2410 / B / C** (24 GHz) | **$3.20** [hlktech](https://www.hlktech.net/index.php?id=988); **€4.35** LD2410C [OpenELAB](https://openelab.io/collections/sensors-presence-sensor) | Very mature, huge base | 5 m, ±60°. Reviewers call it cost-effective but "quite fiddly to adjust… a lot of gate settings" |
| **LD2412** (24 GHz, ±75°, 9 m) | **€4.35–4.95** OpenELAB | Maturing, now shipping in products | **The de-facto LD2410 successor for presence.** Wider FOV and range. Radar inside CeilSense and Apollo R PRO-1 |
| **LD2450** (3-target X/Y/speed) | **€6.90** [OpenELAB](https://openelab.io/products/hlk-ld2450-human-movement-trajectory-tracking-radar-module) | Mature; the zone-tracking workhorse | Behind every "draw zones on a map" product. "Tends to lose targets when multiple targets are at the same time" |
| **LD2410S** (ultra-low-power, µA class) | **€4.35–4.36** OpenELAB | Shipping in battery products | **The part that unlocked battery mmWave.** Inside the Tuya ZG-204ZM |
| **LD2451** | €4.35–9.79 | N/A for home | **NOT a home-presence part** — vehicle/blind-spot radar, 5 vehicles @ 100 m, ±20°. Anyone shortlisting it for occupancy has misread the datasheet |
| **LD6002** (60 GHz respiration/heartbeat) | **UNVERIFIED** — not in OpenELAB's presence catalog | Niche / vitals | *What would answer this: an opened distributor listing with a numeric price* |
| **LD1125H** | not opened | Legacy | Community has moved off it: users "abandoned the LD1125H for the LD2450, reporting the ceiling fan problem was unresolvable" |

**INFERENCE / HIGH — current recommended picks: LD2412 for binary presence, LD2450 for zone/coordinate tracking, LD2410S when battery is a hard requirement.** LD2410B/C remains the cheapest known-good part.

**Product tier — the ones that matter for a Zigbee-first hub are bolded:**

| Product | Protocol | Price (cited, 2026-07-31) | Notes |
|---|---|---|---|
| Aqara FP2 | **Wi-Fi only**, mains | **$82.99** [us.aqara.com](https://us.aqara.com/products/presence-sensor-fp2) | 60 GHz, 40 m², 30 zones, 5 people, fall detection. **No Zigbee path.** Street price well below MSRP |
| **Aqara FP1E** | **Zigbee 3.0**, mains | price UNVERIFIED | 6 m, **AI interference-source identification (fans/AC)**, adaptive sensitivity, spatial learning, OTA. [Z2M page](https://www.zigbee2mqtt.io/devices/FP1E.html) |
| **Aqara FP1 (RTCZCGQ11LM)** | **Zigbee 3.0**, mains | not opened | 4×7 grid, up to 10 regions, enter/leave/approach/away. **Does not function on Zigbee channels 21–24** ([Z2M](https://www.zigbee2mqtt.io/devices/RTCZCGQ11LM.html)) |
| **Aqara FP300** | **Zigbee 3.0 OR Thread/Matter**, **2×CR2450 battery** | **$49.99** ([SmartHomeScene teardown, 2026-01-30](https://smarthomescene.com/reviews/aqara-fp300-presence-multi-sensor-teardown-and-review/)); £49 (sold out) | 60 GHz + PIR, EFR32MG24 SoC, "up to 3 years" claim. **Shipping but rough** — see pain exhibits |
| Aqara FP400 | Thread/Zigbee dual (vendor); Bluetooth/Thread (third-party listing — **conflict unresolved**) | announced, no price | CES 2026: posture (standing/sitting/lying), fall detection, real-time headcount, dwell analytics ([Aqara, 2026-01-06](https://www.aqara.com/en/news/aqara-showcases-latest-innovations-in-spatial-intelligence-at-ces-2026/)) |
| Everything Presence Lite | Wi-Fi + BLE, ESPHome | **£28.00** [product page](https://shop.everythingsmart.io/products/everything-presence-lite) | LD2450, 3 targets, X/Y coords, 4 zones, doubles as HA BLE proxy |
| Everything Presence Pro | Wi-Fi + BLE + **PoE** | **£67.00** [product page](https://shop.everythingsmart.io/products/everything-presence-pro) | **Dual radar** (DFRobot SEN0609 25 m + LD2450 6 m) + PIR + alarm/tamper I/O. Only mainstream unit with PoE + panel I/O |
| Apollo MSR-2 / MTR-1 / R PRO-1 | Wi-Fi/ESPHome (R PRO-1 adds PoE) | **$37.99–69.99** [apolloautomation](https://apolloautomation.com/collections/sensors) | LD2410B / LD2450 / dual LD2450+LD2412 |
| SwitchBot mmWave Presence | **BLE 5.0**; Matter only via SwitchBot hub; 2×AAA | **$29.99** [us.switch-bot.com](https://us.switch-bot.com/products/switchbot-mmwave-presence-sensor) | 60 GHz Possumic RS6130 + PIR, "up to 2 years", one-click AI interference filtering |
| **Third Reality R3** | **Zigbee 3.0**, USB-C | **$49.99**, sold out [thirdreality](https://www.thirdreality.com/products/smart-presence-sensor-r3) | 60 GHz, Lux + TVOC, **acts as a Zigbee router** |
| **Third Reality R2** | **Zigbee 3.0**, **3×AA** | **$39.99** ([PRWeb, 2026-05-29](https://www.prweb.com/releases/thirdreality-launches-smart-presence-sensor-r2-bringing-flexible-battery-powered-presence-detection-to-everyday-smart-homes-302785258.html)) | 24 GHz, AI environmental learning. **Newest Zigbee battery mmWave part found** |
| **Tuya ZY-M100 / TS0601** | **Zigbee**, mains | ~$15–25 (no live listing opened) | Presence, distance, illuminance, sensitivity 0–9, range 0–9.5 m, fading 0.5–1500 s ([Z2M](https://www.zigbee2mqtt.io/devices/ZY-M100-S_2.html)) |
| **Tuya ZG-204ZM** | **Zigbee, 2×AAA** | ~$15 AliExpress (via [SmartHomeScene](https://smarthomescene.com/reviews/zigbee-battery-powered-presence-sensor-zg-204zm-review/)) | LD2410S + PIR. **Hardware lottery** — Z2M warns "Multiple hardware versions exist with identical appearance"; `_TZE200_kb5noeto` sticks on presence; reviewer: "roughly 50% of units" |
| **Sonoff SNZB-06P** | **Zigbee 3.0**, USB-C, also a router | ~$15 | **Not mmWave** — 5.8 GHz radar. Firmware warning: "1.0.3 can be misbehaving… upgrade to 1.0.5" ([Z2M](https://www.zigbee2mqtt.io/devices/SNZB-06P.html)) |
| Meross MS605 | **Thread/Matter**, CR123A | not opened | 24 GHz, IP67, zones, "3-year" battery |
| CeilSense | Wi-Fi/**PoE**, ESPHome | not opened | LD2412 + ESP32 in a **recessed ceiling housing**. 2026 EU newcomer, thin evidence base |

**MATURITY & PAIN — the dated exhibits**

1. **FACT / HIGH — stuck presence is environmental, not brand-specific. This is the single most load-bearing exhibit in §4.** HA thread **2026-07-30** (the day before this lane ran): four sensors from three vendors — Aqara FP2 (Wi-Fi), 2× Sonoff (Zigbee), CeilSense (ESPHome) — all get "stuck presence" in the same kitchen ~once a month, and all work flawlessly elsewhere. Hypothesis: fridge compressor cycles + extractor fan + metal appliances slowly corrupt the radar's static background model. **Workaround = press "Dynamic background calibration" or reboot.** — [link](https://community.home-assistant.io/t/every-mmwave-presence-sensor-gets-stuck-presence-in-my-kitchen-once-a-month-fp2-2x-sonoff-ceilsense-same-devices-work-flawlessly-in-other-rooms/1019274)
2. **FACT / HIGH — ceiling fans remain unsolved at module level.** LD1125H's segmented sensitivity can't reject a fan when fan and human share a range gate; responders concluded no practical fix. — [HA community, 2024-05-21](https://community.home-assistant.io/t/ld1125h-mmwave-sensor-dealing-with-ceiling-fans/731476)
3. **FACT / HIGH — battery mmWave ships but tunes badly.** Aqara FP300 thread, Dec 2025: works "80% correctly, but in the last 20% I have no presence detection"; "stand direct in front of the sensor and it doesn't recognize any presence"; "detection range always resets to 65535 (or zero), no matter how many times I wake the device and set it higher"; battery status often "Unknown." — [link](https://community.home-assistant.io/t/aqara-fp300-presence-sensor/894596?page=3)
4. **FACT / HIGH — Z2M FP300 has a live tracking bug.** Z2M discussion #31203 (2026-03-09): target distance stays 0, presence only fires at ~10 cm despite a 6 m config; pressing "Track target distance" restores real readings for 20–30 min then freezes — "Z2M does not persist the tracking mode after a timeout." — [link](https://github.com/Koenkk/zigbee2mqtt/discussions/31203)
5. **FACT / HIGH — reviewer verdict on FP300:** "false negative dropouts" vs SwitchBot; config changes "often didn't apply reliably"; a commenter called setup "a nightmare"; "you have to be willing to tinker with it to get good results." — [SmartHomeScene, 2026-01-30](https://smarthomescene.com/reviews/aqara-fp300-presence-multi-sensor-teardown-and-review/)
6. **FACT / HIGH — Tuya Zigbee devices flood the mesh.** SmartHomeScene's explicit *avoid* list (upd. 2026-02-19) names Moes/Linptech ZSS-LP-HP02, Tuya TZ-GS-200, SZR07U ("network flooding — unfixable in Tuya devices"), `_TZE204_ztqnh5cg` ("spammy illuminance readings ~2-second payloads"), and LY-TAD-K616S ("advertised as radar but actually dual-PIR"). — [link](https://smarthomescene.com/blog/best-and-worst-presence-sensors-for-home-assistant/)
7. **FACT / MED — DIY/ESPHome flashing remains a support burden.** Everything Presence Lite issue #410: install fails with "reboot it or press the boot button while clicking install," post-update Wi-Fi hangs at "connecting," one bootloop with repeated "invalid header." *(No dates surfaced in the fetch.)*

**FACT / HIGH — the headline change since 2024: battery mmWave is now real and shipping.** Four independent battery products verified: Aqara FP300 (2×CR2450, Zigbee-or-Thread), SwitchBot (2×AAA, BLE), Third Reality R2 (3×AA, Zigbee, 2026-05-29), Tuya ZG-204ZM (2×AAA, ~6 mo). **INFERENCE / HIGH:** all achieve it by pairing a low-duty-cycle radar (LD2410S-class or 60 GHz Possumic RS6130) with a **PIR gate** — PIR wakes the radar. The cost is exactly the failure users report (FP300 "Both (PIR+mmWave)" mode dropping to "Not detected" while someone stands in front of it). **You do not get FP2-class zone tracking on batteries.**

### 4b. BLE & UWB

**BLE room-level presence:**
- **FACT / HIGH — Bermuda** is larger by stars but slower-moving: 1.8k★, 56 forks, 87 open issues, 464 commits, 50 releases; **latest release v0.8.5, 2025-08-05**. **INFERENCE / MED:** a ~12-month gap since last tag, with 87 open issues, reads as maintenance-mode-at-best for a project many people depend on. Its README frames trilateration mapping as "eventually" — today it is **area-level, not coordinate-level**. — [repo](https://github.com/agittins/bermuda)
- **FACT / HIGH — ESPresense** is smaller by stars but shipping faster: 1.4k★, 180 forks, 1,077 commits, **204 releases**, v4.0.6 on **2026-02-28**. Two models: `mqtt_room` = room-level, **1 node per room**; ESPresense-Companion = "precise X,Y coordinates" requiring **5–8+ nodes per floor**. — [repo](https://github.com/ESPresense/ESPresense) · [espresense.com](https://espresense.com/)
- **FACT / HIGH — MAC randomization is solved, but only via IRK extraction.** ESPresense advertises "IRK-based enrollment of Apple devices to passively locate them uniquely, even with private random addresses." HA's `Private BLE Device` integration is the Bermuda-side equivalent.
- **FACT / MED — one practitioner's real-world result:** Bermuda "recognizes which room I'm in under 10 seconds," "very reliable with my iPhone," but an Apple Watch Ultra 3 "would often jump wildly far distances" from power saving. Hardware: multiple Seeed Xiao ESP32-C6 at ~$5 each **plus an external antenna strongly recommended**; ~17 setup steps; "Solid global settings and scanner RSSI configuration is KEY"; IRK extraction "a bit cumbersome." — [derekseaman.com, 2025-12-13/23](https://www.derekseaman.com/2025/12/home-assistant-track-whos-in-each-room-with-esphome-bermuda-ble.html)

**INFERENCE / HIGH — BLE room presence in 2026 is identity-first, not occupancy-first.** It tells you *which known person* is in a room; it cannot see a guest, a child without a phone, or a person asleep with their phone elsewhere. **It is complementary to mmWave, not competitive.** High labour cost, low BOM (~$5/room).

**UWB:**
- **FACT / HIGH — no consumer UWB room-presence product has shipped from a major ecosystem.** As of 2026-07-15, the next Apple TV 4K is expected to get the N1 chip (Wi-Fi 7 / BT 6 / Thread) with **no UWB mentioned**, and a rumoured ~$350 Apple smart home hub does presence detection via **a built-in camera with facial recognition**, not UWB. *(All rumour, explicitly labelled as such by the source.)* — [MacRumors](https://www.macrumors.com/2026/07/15/apple-smart-home-lineup-rumors/)
- **FACT / HIGH — FiRa still describes use cases, not products.** Its smart-home page lists 8 conceptual use cases with **no shipping products, no dates, no spec references**. — [firaconsortium.org](https://www.firaconsortium.org/discover/use-cases/smart-home-consumer)
- **FACT / MED — the market is phones and cars.** ~450 M UWB chips shipped in 2024, +21% YoY, **~60% into smartphones**; radar-style presence framed as future tense: "in the longer term we can see increased attention to UWB **radar** which would allow presence and health detection of people without requiring them to carry any electronics." — [pozyx.io](https://www.pozyx.io/newsroom/the-state-of-uwb) *(March 2025 — ~16 months old)*
- **FACT / MED — one CES 2026 entrant:** Eforthink "Eforlink UWB Identity Presence Sensor." No shipping date, no price, no post-CES coverage found. — [PRNewswire, 2025-12-29](https://www.prnewswire.com/news-releases/from-factory-floors-to-smart-homes-eforthink-debuts-next-gen-uwb-solutions-at-ces-2026-302650057.html)

**OPINION / HIGH — UWB home presence is still promise, not product, in mid-2026**, and it shares BLE's fundamental limitation (it tracks *tags/phones*, not *people*) until UWB-radar matures.

**Matter standardisation of presence — read this one carefully, it carries a caveat:**
- **FACT / HIGH — CSA's own Matter 1.5 and 1.6 announcements omit occupancy/presence entirely.** *(1.6 independently re-verified: the CSA release does not mention ambient sensing, presence, or occupancy anywhere.)*
- **FACT / MED — but Samsung Research reports a new provisional "ambient context sensor" device type in Matter 1.6.** *(Re-verified directly.)* Verbatim: *"The latest iteration of Matter, release 1.6, introduces a new ambient sensing feature, available on a provisional status. Nonetheless, it is expected to become a fully certifiable version in the near future."* Four categories: **human activity detection** ("falling, sleeping, walking, package delivery and pickup, etc. — total 10 items"), **object identification** ("person (adult or child), pet, car, package, etc. — total 12 items"), **sound identification** ("glass breaking, clapping, faucet running, coughing, etc. — total 21 items"), and predicted activity notification. Concurrent reporting from up to 10 sensing sources in a single event. **Confidence capped at MED: this rests on a single vendor-research page with no visible publication date, and CSA's own announcement does not corroborate it.** — [research.samsung.com](https://research.samsung.com/blog/CSA-Matter-1-6-Release-Ambient-Sensing-More-Intuitive-Setup-Multi-Ecosystem-Experiences-and-Context-Driven-Control)
- **INFERENCE / MED (downgraded from HIGH on the corroboration gap) — if it holds, this is the standardisation story that matters:** Matter is moving from binary occupancy toward **semantic presence** (who / what / doing-what). Provisional means no certified products yet and 12–18 months of vendor differentiation. **A hub that models presence as a boolean today will be modelling the wrong shape by 2027.** *What would close the gap: the Matter 1.6 Device Type Library entry for the ambient context sensor, or a second independent source.*

### 4c. The Zigbee-reachable subset — what a Zigbee-first hub could own today

**Confirmed Zigbee, with a Z2M device page opened (all 2026-07-31):**

| Device | Power | Radar | Exposes | Risk |
|---|---|---|---|---|
| **Aqara FP1E** | mains | 60 GHz | presence, movement, distance, sensitivity L/M/H, 6 m, AI interference-source ID, adaptive sensitivity, spatial learning, **OTA**, device temp | **Lowest-risk Zigbee pick.** Native OTA, no vendor bridge |
| **Aqara FP1** | mains | 60 GHz | presence, presence_event (enter/leave/approach/away, directional), monitoring mode, **4×7 grid → up to 10 regions**, region events | **Does not work on Zigbee channels 21–24** — a hard coordinator channel-planning constraint |
| **Aqara FP300** | 2×CR2450 | 60 GHz + PIR | presence, motion, temp, humidity, illuminance, battery, sensitivity, AI interference detection, **24 distance zones to 6 m**, OTA | Thread→Zigbee conversion needs a **10× reset-button press**, not the standard hold. Live target-distance bug |
| **Linptech ES1ZZ(TY)** | mains | 24 GHz | occupancy, illuminance + calibration offset, target distance, motion distance (→600 cm), keep-time, motion + static sensitivity, fading time, LED | Its Moes-badged twin is on the network-flooding avoid list |
| **Tuya ZY-M100 / TS0601** | mains | 24 GHz | presence, distance, illuminance, sensitivity 0–9, range 0–9.5 m, delay, fading 0.5–1500 s | Manufacturer-ID fragmentation (`_TZE200_*`/`_TZE204_*`); several siblings on the avoid list |
| **Tuya ZG-204ZM** | 2×AAA | LD2410S + PIR | presence, motion state (none/large/small/static), battery, illuminance, fading, distance/sensitivity, mode | Identical-looking hardware revs; one variant sticks on "presence detected"; ~50% failure rate per review |
| **Sonoff SNZB-06P** | mains, **also a router** | 5.8 GHz | occupancy, timeout 15–65535 s, sensitivity L/M/H, illumination dim/bright | Illumination updates only on occupancy. Require FW ≥1.0.5 |

**Zigbee per vendor but no Z2M page opened — verify before committing:** Third Reality R3 and R2 (both claim ZHA + Z2M), Aqara FP400 (not shipping; protocol claim contested).

**Not reachable over Zigbee — needs a second radio:** Aqara FP2, all Everything Presence models, all Apollo models, CeilSense, SwitchBot, Meross, Shelly Presence Gen4, LinknLink, and all ESPresense/Bermuda infrastructure.

**INFERENCE / HIGH — the load-bearing gap.** Every Zigbee mmWave device above tops out at **occupancy + single target distance + sensitivity/timeout knobs**. Aqara FP1's 4×7 region grid is the ceiling for Zigbee zoning. **No Zigbee device found exposes LD2450-class multi-target X/Y coordinates or user-drawn zones** — that lives exclusively on Wi-Fi/ESPHome. **If zone-level presence is a product requirement, a Zigbee-only radio strategy cannot deliver it today.**

**INFERENCE / HIGH — second design constraint, and it is a v1 architecture input.** Chatty Tuya-class radar is a documented mesh-health hazard, and the two best Zigbee options each carry a coordinator-level constraint (FP1 refuses channels 21–24; FP300 needs a non-standard 10-press factory reset to leave Thread). **A Zigbee-first hub should plan per-device reporting-rate throttling and a channel-selection guard as first-class features, not afterthoughts.**

### 4d. Traction signals

- **FACT / HIGH — GitHub (2026-07-31):** Bermuda 1.8k★ / last release 2025-08-05 · ESPresense 1.4k★ / 204 releases / v4.0.6 2026-02-28 · everything-presence-lite 293★ / 111 forks / v1.5.0 2026-06-02.
- **INFERENCE / MED — this is enthusiast-scale, not mass-market.** HA reports **625,530 active installations** ([analytics.home-assistant.io](https://analytics.home-assistant.io/)), so Bermuda's 1.8k stars ≈ 0.3% of installs. **Presence is a loud niche, not a large one** — though stars undercount installs by a wide and unknown margin.
- **UNVERIFIED — per-integration install counts.** The HA analytics integrations table did not render to the fetcher. *What would answer this: the JSON behind analytics.home-assistant.io, or a browser-rendered read.*
- **FACT / HIGH — Zigbee ecosystem scale:** Zigbee2MQTT supports **5,521 devices from 583 vendors** ([supported-devices](https://www.zigbee2mqtt.io/supported-devices/)).
- **FACT / HIGH — vendor investment is accelerating.** In the 8 months before this report: Third Reality launched **two** new presence SKUs (R3, then R2 on 2026-05-29); Aqara announced FP400 + FP310 at CES 2026; Everything Smart shipped EP Pro firmware v1.5.0 (2026-06-02); Apollo shipped the PoE R PRO-1; CeilSense entered as a new EU vendor (first HA mention 2026-04-16).
- **INFERENCE / MED — a "best presence sensor 2026" content industry exists**, including vendors publishing their own roundups (LinknLink published two) — a reliable tell that the category has enough search volume to be worth farming. Real consumer demand, heavy commercial noise.

### 4e. Candidate Wave-3 device classes — ranked

1. **Mains-powered Zigbee mmWave, single-target, tuning-forward — INFERENCE / HIGH.** The only class where a Zigbee-first hub competes on equal footing today; supply is real (FP1E, FP1, ES1ZZ, ZY-M100, Third Reality R3); and **the differentiator is software, not hardware**. Exhibit 1 shows every vendor's radar drifts into stuck-presence in hostile rooms and the fix is a manual recalibration button. **A hub that auto-detects a stale background model — presence asserted continuously beyond a learned per-room ceiling with zero illuminance/PIR corroboration — and issues the vendor recalibration command would fix, in software, the #1 cross-vendor complaint.** Highest value per unit of effort, and it is *the same epistemic move as our availability thesis applied to a sensor's own self-report*.
2. **Sensor fusion over heterogeneous presence sources — OPINION / HIGH.** No single class works: mmWave sees anonymous bodies but hallucinates; BLE identifies people but only phone-carriers; PIR is fast but blind to stillness. All three are already in most enthusiast homes. A hub whose native model is *"room occupancy = fused confidence with per-source attribution"* rather than *"binary from one entity"* is defensible, radio-agnostic, and aligned with where Matter appears to be heading.
3. **Battery Zigbee mmWave — INFERENCE / HIGH.** Newly real, placement-unconstrained, Zigbee-native. But quality is unproven-to-poor across all three options. **Support it, do not depend on it**; budget explicit handling for hardware-revision fragmentation and non-reporting battery levels.
4. **Zone/coordinate presence — INFERENCE / HIGH on the gap, OPINION / MED on the response.** Genuinely valuable, genuinely unavailable over Zigbee. Options: (a) accept a Wi-Fi/ESPHome escape hatch, (b) build a first-party Zigbee device around LD2450, (c) declare out of scope for v1. **Option (b) is where a hardware-capable company could differentiate — nobody ships a good Zigbee multi-target zone sensor, and the module is €6.90.**
5. **Thread/Matter presence as a hedge — INFERENCE / MED.** Roadmap item, not v1.
6. **BLE identity presence — OPINION / MED.** Worth **consuming** (ingest Bermuda/ESPresense MQTT as a fusion input) rather than **building**.
7. **UWB — OPINION / HIGH: do not target this cycle.** Revisit in 18–24 months.

---

## §5 — Regulatory tailwinds

*Primary sources marked (P); law-firm/vendor/press summaries (S) used only as corroboration. **Disclosed fetch failures:** direct access to EUR-Lex was blocked (403 on CONNECT) and both HTML renderings truncated at recital 42 — **Articles 13, 14, 71 and Annexes I/III were never read on EUR-Lex itself**; those texts come from mirrors, cross-checked against the Commission's own summary. `fcc.gov/CyberTrustMark` returned 403 to every attempt; routed to `docs.fcc.gov` PDFs instead. One law-firm source was paywalled (HTTP 402).*

### 5a. EU Cyber Resilience Act

**FACT / HIGH — citation.** Regulation (EU) 2024/2847 of 23 October 2024 on horizontal cybersecurity requirements for products with digital elements (Cyber Resilience Act). Title read directly on [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847). A corrigendum dated 2024-12-05 exists (surfaced in search, not opened).

| Obligation | Date | Confidence |
|---|---|---|
| Entry into force | **10 December 2024** | FACT / HIGH — [Commission CRA summary](https://digital-strategy.ec.europa.eu/en/policies/cra-summary) (P) |
| Chapter IV — notified bodies may be designated | **11 June 2026** *(passed)* | FACT / HIGH — Commission summary (P) |
| **Article 14 reporting — actively exploited vulnerabilities + severe incidents** | **11 September 2026** *(6 weeks from today)* | FACT / HIGH — [Commission CRA reporting](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting) (P) *(re-verified verbatim: "As of 11 September 2026, manufacturers are required to report actively exploited vulnerabilities and severe incidents impacting the security of products with digital elements.")* |
| **Main body — essential requirements, conformity assessment, CE marking, support period** | **11 December 2027** | FACT / HIGH — Commission summary (P) |

**FACT / HIGH — reporting mechanics** *(re-verified verbatim)*: **early warning within 24 hours** of becoming aware → **full notification within 72 hours** → **final report no later than 14 days after a corrective measure is available** (**within a month** for severe incidents). Reports go to the CSIRT of the manufacturer's main establishment and simultaneously to ENISA, via one submission to the CRA **Single Reporting Platform (SRP)**.

**FACT / HIGH — the SRP is not live yet.** ENISA's own page (updated July 2026) says the platform URL will be published "in due course," with user and security testing still underway ahead of the 11 September go-live ([ENISA](https://www.enisa.europa.eu/topics/product-security-and-certification/single-reporting-platform-srp), P). **INFERENCE / MED-HIGH: the obligation date is statutory and does not move because the tool is late — detection and triage capability must exist independently of the platform.**

**FACT / MED-HIGH — Annex I Part I (product properties)**, read via mirror ([streamlex](https://streamlex.eu/annexes/cra-en-annex-i/), S), consistent with the Commission summary (P). Requires: ship "without known exploitable vulnerabilities"; **secure-by-default configuration** (deviation only by agreement with a *business* user — not consumers); **automatic security updates enabled by default with a clear opt-out**; access control/authentication; **encryption at rest and in transit**; **data minimisation** ("only data … adequate, relevant and limited to what is necessary"); **availability of essential functions also after an incident**; **security-relevant logging and monitoring of internal activity**; secure permanent deletion of all data and settings.

**FACT / MED-HIGH — Annex I Part II (vulnerability handling).** A **software bill of materials in a commonly used, machine-readable format** covering at least top-level dependencies; remediation "without delay"; regular security testing; public disclosure of fixed vulnerabilities with severity; an enforced **coordinated vulnerability disclosure policy**; a published contact address; secure update distribution; updates disseminated **free of charge** with advisory messages.

**FACT / MED — support period.** Article 13(8) via mirror: *"the support period shall be **at least five years**,"* except where expected use is demonstrably shorter. Article 13(9): each security update must **remain available for at least 10 years** after issue, or the remainder of the support period, whichever is longer. **MED not HIGH because this is mirror-only text** — the Commission summary confirms a support-period obligation and end-of-support disclosure but the numeral was not seen on a primary page.

**FACT / HIGH — classification tiers and conformity routes** (Commission summary, P; category detail from [cyberresilienceact.eu](https://www.cyberresilienceact.eu/classification.html), S):
- **Default** (the large majority) → **self-assessment** (internal control)
- **Annex III Important Class I** → self-assessment **only if harmonised standards / an EU certification scheme are applied in full**; otherwise a **notified body**
- **Annex III Important Class II** → **third-party assessment mandatory**
- **Annex IV Critical** → may require European cybersecurity certification
- All in-scope products: CE marking, technical documentation, EU declaration of conformity, cybersecurity risk assessment

**FACT / HIGH — where smart home lands.** Annex III **Class I** explicitly includes *smart home general purpose virtual assistants*; *smart home products with security functionalities, including smart door locks, security cameras, baby monitoring and alarm systems*; *routers, modems and switches*; **and *operating systems***; and microcontrollers with security-related functionalities. Class II covers hypervisors/container runtimes, firewalls/IDS/IPS. Annex IV Critical is narrow.

**INFERENCE / MED — the hub question, which is commercially decisive.** A general smart-home hub is **not named** in Annex III. Its tier turns on **core functionality**: a hub that merely aggregates sensors and automations is plausibly **Default (self-assessment)**; a hub that is the control point for door locks, cameras or alarms is at material risk of being read as a "smart home product with security functionalities" → **Class I**. Two further traps: **shipping a general-purpose operating system is itself Class I**, and voice control could pull toward "virtual assistant." **This is the single highest-leverage classification decision on the runway.** It should be settled against Implementing Regulation (EU) **2025/2392**, which published the technical descriptions of Annex III/IV categories and entered into force **21 December 2025** (S, [Snellman](https://digitalcompliance.snellman.com/technical-descriptions-for-important-and-critical-products-are-published/)). **UNVERIFIED — the implementing regulation itself was not opened.** *What would answer this: the operative Articles/Annex of IR (EU) 2025/2392 on EUR-Lex, specifically the functional definitions of "smart home product with security functionalities" and of "operating system."*

**FACT / HIGH — no CRA harmonised standard is yet cited in the Official Journal.** As of **2026-06-04**, none had been published, so **the Article 27 presumption of conformity is available for no product category** ([craevidence tracker](https://craevidence.com/cra-compliance/harmonised-standards-status), S). Deadlines: framework + vulnerability-handling standards (EN 40000-1-2, -1-3) due **2026-08-30**; product-specific (EN 304 6xx, EN 50770, EN 5076x) due **2026-10-30**; generic security requirements (EN 40000-1-4) due **2027-10-30**. CEN/CENELEC/ETSI accepted the standardisation request on **2025-04-03** ([CEN-CENELEC](https://www.cencenelec.eu/news-events/news/2025/newsletter/ots-62-cra/), P). **INFERENCE / MED-HIGH: the binding constraint is not delivery but OJ citation, whose timetable the Commission has not confirmed — so a Class I product today has no practical self-assessment route, only a notified body.**

**The open-source question — FACT / HIGH, from the Commission's own page** ([digital-strategy.ec.europa.eu/en/policies/cra-open-source](https://digital-strategy.ec.europa.eu/en/policies/cra-open-source), P):
- The CRA bites only on FOSS **made available on the market in the course of a commercial activity**. Verbatim: *"the provision of products with digital elements qualifying as free and open-source software that are not monetised by their manufacturers should not be considered to be a commercial activity."*
- *"the CRA does not apply to developers who contribute … source code to free and open-source software that are not under their responsibility."* Contributing upstream is not a trigger.
- **Open-source software steward** = a legal entity providing *"systematic support on a sustained basis for the development of specific products with digital elements, qualifying as free and open-source software and intended for commercial activities."* Stewards get a lighter regime (Article 24) and — critically — *"open-source software stewards are not subject to administrative fines for infringements of the CRA."*
- **FACT / MED — a real benefit for open-core:** manufacturers of *important* products qualifying as FOSS may use **self-assessment provided the technical documentation is made publicly available**. *(Article number is inferred and unverified; the substance is on the Commission's page.)*

**INFERENCE / HIGH — the trap, stated plainly because it is widely misunderstood.** The steward regime is **not** an escape hatch. A steward *supports* FOSS it does **not** place on the market. **A vendor that sells a supported edition, hardware, or a paid tier is a manufacturer of that product** — full obligation set (technical documentation, conformity assessment, CE marking, ≥5-year support, Article 14 reporting) and full exposure to administrative fines. Publishing source code changes none of that. What **does** help materially is the FOSS self-assessment carve-out: if the hub lands in **Class I** and no harmonised standard is cited, being genuinely open source **with public technical documentation may be the only route that avoids a notified body.** That converts an ideological choice into quantifiable cost avoidance.

**2025–2026 developments:**
- **FACT / HIGH — Commission guidance published 2026-07-27, four days before this lane ran.** Communication **C(2026) 5252** plus annexed guidance, covering scope — **explicitly including remote data processing solutions and free and open-source software** — substantial modification, how support periods are to be understood, reporting obligations and risk assessment. **67 practical examples**, use cases, flowcharts, with stated "particular attention" to microenterprises and SMEs. — [library](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation) · [news](https://digital-strategy.ec.europa.eu/en/news/commission-publishes-new-guidance-support-businesses-implementation-cyber-resilience-act) (both P). **This is the single most useful document for the classification and scope questions above and should be read in full before the charter locks a market-entry plan.**
- **FACT / MED-HIGH — EU cyber package of 2026-01-20**: a "Cybersecurity Act 2", a NIS2 amendment, complementing the **Digital Omnibus** simplification package (S, [Clifford Chance, Feb 2026](https://www.cliffordchance.com/briefings/2026/02/eu-cyber-reforms-proposed--including-overhauled-cybersecurity-ac.html)).
- **UNVERIFIED — does the Digital Omnibus delay or amend the CRA?** **No evidence found** that CRA application dates have moved; the Commission was still publishing guidance on 2026-07-27 to support "timely implementation," which cuts against a delay. The one targeted source was paywalled (402). *What would answer this: the Digital Omnibus proposal on EUR-Lex, checked for any amending article touching Regulation (EU) 2024/2847 Articles 14 or 71.* **Plan on the dates holding.**

### 5b. US Cyber Trust Mark

**FACT / HIGH — the program is NOT operationally live and has never accepted a product submission.** That is the honest headline and the evidence is unambiguous.

- **2023-07-18** announced; **2025-01-07** "launched" at the White House as a *"voluntary cybersecurity labeling program for wireless interconnected smart products,"* claiming *"The program is open for business in 2025: companies will soon be able to submit their products for testing"* ([archived release](https://bidenwhitehouse.archives.gov/briefing-room/statements-releases/2025/01/07/white-house-launches-u-s-cyber-trust-mark-providing-american-consumers-an-easy-label-to-see-if-connected-devices-are-cybersecure/), P).
- **June 2025** — FCC Chairman opened a national-security review of **UL Solutions**, the Lead Administrator, over a joint venture with a Chinese state-owned company and test labs in China (S, [Cybersecurity Dive, 2025-09-02](https://www.cybersecuritydive.com/news/fcc-cyber-trust-mark-ul-investigation-delay/758507/)).
- **Sept 2025** — still not accepting submissions; UL's June 2025 testing standards still awaiting comment and FCC approval; label design unfinished. Expert: *"We're not really near to people applying for these marks. There's a ways to go."*
- **2025-12-19** — **UL Solutions withdrew** as Lead Administrator.
- **2026-01-06** — FCC Public Notice **DA 26-18** opened a new Lead Administrator filing window (7–28 January 2026), confirming UL's withdrawal and that the Bureau had **conditionally approved 11 CLAs** ([PDF](https://docs.fcc.gov/public/attachments/DA-26-18A1.pdf), P).
- **April 2026** — FCC named the **ioXt Alliance** Lead Administrator. *(Date: ioXt's own release says 13 April; Cybersecurity Dive reports "Monday, April 14, 2026." **Sources differ by one day — use "mid-April 2026" in any external copy.**)* Remit: operational integrity, a **public device registry**, CLA coordination, implementation guidance. — [ioXt](https://ioxt.com/news-events-blog/fcc-names-ioxt-alliance-lead-administrator-for-us-cyber-trust-mark-program) · [Cybersecurity Dive](https://www.cybersecuritydive.com/news/fcc-cyber-trust-mark-new-lead-administrator/817437/) *(re-verified: "UL withdrew in December, after the Trump administration began investigating the company over its ties to China.")* · [Nextgov](https://www.nextgov.com/cybersecurity/2026/04/fcc-selects-ioxt-alliance-lead-cyber-labeling-program/412800/)
- **Neither the FCC nor ioXt has stated any date for accepting applications or for labels reaching shelves.**

**INFERENCE / MED-HIGH — honest assessment.** Roughly **three years** from announcement to today with **zero certified products**, one Lead Administrator resignation under a national-security cloud, a four-month administrator vacuum, and no published launch date four months after the replacement was named. The FCC's revealed preference — a fresh filing window rather than cancellation — signals the program survives, but the *velocity* signal is poor. **Do not build a launch plan, a marketing claim, or a retail conversation around the Cyber Trust Mark being available in 2026.** Treat it as an option to exercise later, not a milestone.

**FACT / HIGH — technical demands: NIST IR 8425**, *Profile of the IoT Core Baseline for Consumer IoT Products*, Sept 2022 ([PDF](https://nvlpubs.nist.gov/nistpubs/ir/2022/NIST.IR.8425.pdf), P). Six product capabilities: **Asset Identification**; **Product Configuration** (restorable to secure default); **Data Protection** (at rest and in transit); **Interface Access Control**; **Software Update** (all components, secure and configurable, authorized actors only); **Cybersecurity State Awareness** ("supports detection of cybersecurity incidents affecting or affected by IoT product components and the data they store and transmit"). Four non-technical: Documentation, Information and Query Reception, Information Dissemination, Product Education and Awareness.

**FACT / HIGH — voluntary, and commercial pull is currently nil.** Best Buy, Amazon and Consumer Reports gave supportive statements in Jan 2025, but the release contains **no purchase commitments, no quantities, and no federal procurement mandate** — specifically searched for and not found. **INFERENCE / MED-HIGH: with no products labelled and no mandate, retailer pressure is a 2027+ hypothesis, not a 2026 fact.**

**UNVERIFIED — identities of the 11 CLAs and the accredited CyberLABs.** Blocked by repeated 403s from `fcc.gov`.

### 5c. Other regimes

- **UK PSTI — FACT / HIGH.** In force **2024-04-29** ([techUK](https://www.techuk.org/resource/psti-regulations-come-into-force.html), S). Three duties: no universal default passwords; published vulnerability disclosure policy; **published minimum security-update support period**. Note it mandates *transparency* about the period, not a minimum length — materially lighter than the CRA's ≥5 years.
- **Australia — FACT / HIGH.** Mandatory security standards for consumer smart devices under the **Cyber Security Act 2024**, commencing **2026-03-04** ([Home Affairs](https://www.homeaffairs.gov.au/about-us/our-portfolios/cyber-security/security-standards-for-smart-devices), P). Same three requirements as UK PSTI plus a published support period **including an end date** and a supplier statement of compliance. **INFERENCE / HIGH: UK PSTI artifacts substantially transfer.**
- **Singapore — FACT / HIGH.** Cybersecurity Labelling Scheme, voluntary **except Wi-Fi routers** (CLS Level 1 mandatory).
- **Japan — FACT / HIGH.** JC-STAR, voluntary, multi-level. Singapore and Japan signed **mutual recognition** on **2026-03-18**, effective **2026-06-01** ([CSA Singapore](https://www.csa.gov.sg/news-events/press-releases/singapore-signs-memorandum-of-cooperation-with-japan-on-mutual-recognition-of-internet-of-things-cybersecurity-schemes/), P). **INFERENCE / MED-HIGH: mutual recognition is the direction of travel — one well-built evidence pack is increasingly reusable, lowering the marginal cost of each additional market.**

### 5d. Moat or tax?

**The case that local-first / no-cloud / event-sourced is genuinely ADVANTAGED:**

1. **INFERENCE / HIGH — it shrinks compliance *scope*, not just attack surface.** The CRA reaches **remote data processing solutions** — manufacturer-designed cloud components whose absence would break a product function. That the Commission's 2026-07-27 guidance devotes explicit treatment to this boundary confirms it is live and contested. A product with no manufacturer cloud has **no such component to document, risk-assess, secure, or report incidents about**. A cloud-dependent competitor must extend technical documentation, SBOM discipline and Article 14 incident detection across a server estate and its sub-processors. **A structurally smaller compliance object, not merely a smaller codebase.**
2. **INFERENCE / HIGH — several Annex I Part I requirements are satisfied architecturally.** Data minimisation is trivially met when data never leaves the home. *"Protect the availability of essential and basic functions, also after an incident"* is met by construction when no cloud outage can disable the product — **genuinely hard for cloud-dependent smart-home vendors**. Secure permanent deletion is a local operation. Encryption-in-transit surface is far smaller.
3. **INFERENCE / HIGH — event sourcing maps near one-to-one onto two named obligations.** Annex I Part I requires the product to *"provide security related information by recording and monitoring relevant internal activity."* NIST IR 8425 requires **Cybersecurity State Awareness**. An immutable, append-only event log **is** that capability, already built for product reasons. Competitors bolt on audit logging as a compliance cost; here it is a pre-existing asset.
4. **INFERENCE / MED-HIGH — and this is the sharpest point — event sourcing directly serves the Article 14 24-hour clock.** The trigger is not "a vulnerability exists" but "a vulnerability is **actively exploited**." Determining that within 24 hours requires evidence of what actually executed on devices. A vendor without a reliable per-device audit trail must **over-report** (regulatory noise, reputational cost, 72-hour and 14-day follow-ups on non-events) or **under-report** (breach). An event-sourced core answers *"was this exploited, on which devices, when"* as a **query**. That is a real operational edge on a genuinely hard duty, arriving **2026-09-11**.
5. **INFERENCE / MED-HIGH — the open-source self-assessment carve-out is worth real money.** If the hub is Class I and no harmonised standard is cited (true as of 2026-06-04), the default route is a notified body. The FOSS-with-public-documentation route may be the difference between a notified-body engagement and internal control.

**The case that it is just the same TAX, possibly worse:**

1. **FACT / HIGH — obligations attach to the product; architecture buys no relief from the paperwork.** Technical documentation, risk assessment, conformity assessment, EU DoC, CE marking, machine-readable SBOM, CVD policy, published contact address, public disclosure of fixed vulnerabilities, ≥5-year support, 10-year update availability, 24/72-hour reporting — every one applies identically to a device with no cloud. **There is no SME exemption from the substantive requirements**; the Commission offers proportionality and 67 worked examples, not relief.
2. **INFERENCE / HIGH — the support period is the most dangerous obligation for a tiny vendor, and local-first makes one part *harder*.** Five years minimum of free security updates, each retained ten years, across a Pi-class Linux base and a large open-source dependency tree = five years of CVE triage over a big SBOM regardless of revenue. And note the asymmetry: **Annex I Part I requires automatic security updates enabled by default**, so a no-cloud product still needs an update distribution channel funded and operated for 5–10 years — while *forgoing* the cloud vendor's ability to hot-patch server-side and fix a whole class of bugs without touching devices. **Local-first pushes every fix through a device-update path to hardware in homes, some offline, some behind NAT.** For a pre-launch company this is an open-ended liability incurred at first sale.
3. **INFERENCE / MED-HIGH — classification risk is asymmetric and expensive.** Class I with no usable self-assessment route means a notified-body assessment: a fixed cost a large vendor amortises over millions of units and a small vendor over thousands.
4. **INFERENCE / HIGH — the open-source carve-out is narrower than commonly believed** (see the steward trap above). **Any plan that assumes "we're open source, so the CRA is light" is wrong and should be corrected now.**
5. **INFERENCE / MED — fixed compliance cost is regressive.** The same absolute spend is a rounding error for Google, Amazon or Samsung and a material fraction of a pre-launch company's runway. **A moat the incumbents cross more easily than you is not your moat.**

> **VERDICT — INFERENCE / MED-HIGH: it is a TAX first and a MOAT second — but the architecture converts an unusually large share of the tax into product, and that is the real prize.**

The CRA is a mandatory, non-waivable cost of EU market access paid in full whatever the architecture, and the ≥5-year support obligation is the line item most likely to hurt. **Anyone modelling this as a free tailwind is wrong.** However, the moat is real at the *bottom* of the market — exactly where cheap imports and hobby-project competitors live. Non-monetised open-source projects sit outside the CRA entirely; the moment they commercialise they inherit the manufacturer obligation set, and most will not. Cheap non-EU imports need an EU importer or authorised representative bearing liability. That floor-raising is the regulation's stated purpose and it does clear out the low end.

**The asymmetry that decides it: compliance cost is fixed per release for a vendor who builds the artifacts into the pipeline, and variable per release for a vendor who treats them as a documentation exercise.** SBOM generated in CI, CVD policy published from day one, event-sourced audit trail already load-bearing for the product, support period set deliberately at launch rather than retrofitted — these drive marginal compliance cost per release toward zero while competitors pay each time. **Correct posture: treat the CRA as a product specification you were going to build anyway, not as a legal workstream** — then market the evidence (published SBOM, ≥5-year support commitment, local-only data, verifiable audit trail) as differentiation while cloud-dependent competitors are still enumerating their server estate.

**UNVERIFIED and first thing to resolve — the transitional treatment of products placed on the market *before* 11 December 2027, and whether a substantial modification resets it.** *What would answer this: CRA Article 69 (transitional provisions) on EUR-Lex, plus the "substantial modification" section of the Commission's 2026-07-27 guidance C(2026) 5252.* **This materially affects whether shipping into the EU before December 2027 is advantageous or a trap.**

*Not legal advice. Classification, conformity-assessment route and support-period decisions should be confirmed with qualified counsel before being relied on commercially.*

---

## §6 — THE BETS TABLE

| # | Topic | Verdict | One-line reason | What would change the verdict |
|---|---|---|---|---|
| 1 | **Inbound MCP server** (external agents read/control the home) | **RIDE NOW** | HA's first-party server is at 3.1% of installs vs 209 for the outbound client — the demand is inbound, and being absent from the directories costs us presence for a week of work (§1a, §1d) | Evidence that a provenance-carrying MCP server needs protocol extensions we can't ship unilaterally |
| 2 | **"The home's truthful, provenance-carrying context layer for AI agents"** as positioning | **RIDE NOW** | Zero of 10+ verified home MCP servers derive staleness; the MCP spec has no slot for it and the one proposal is locked and unanswered; the documented agent failures are epistemic, not capability (§1c) | HA adding contract-aware freshness (not just `last_changed`) to the Assist payload, or an accepted MCP provenance spec |
| 3 | **Raw `last_changed` as the differentiator** | **IGNORE-DELIBERATELY** | HA can add it in a single PR and claim ~80% of the perceived value; our moat is **contract + derivation + explanation**, not the timestamp (§1d) | — (this is a warning, not an opportunity) |
| 4 | **Outbound LLM agent inside the product** (HA MCP-client equivalent) | **IGNORE-DELIBERATELY** for v1 | 209 installs, SSE-only, and currently broken upstream; the asymmetry vs 3.1% is ~90:1 (§1a, §1d) | Inbound saturating, or a clear customer pull for in-product agency |
| 5 | **Implementing Matter/Thread in v1** | **WATCH** | Matter's *reliability* complaints in 2026 are the same as 2024 — pairs, then lies about being there — and the ecosystem lags the spec 2–4 minor versions (§2c) | A Zigbee device-class gap we can only close with Thread, or a customer segment that is Matter-native |
| 6 | **Harvesting Matter's `MaxInterval` / ICD `IdleModeDuration` as the reporting contract** | **RIDE NOW (as message + design validation)** | Matter already ships a per-node, protocol-enforced, machine-readable staleness bound and nobody surfaces it — it validates our model's *shape* and gives us standards-anchored vocabulary (§2b, §2d) | Discovering an ecosystem that already surfaces it end-to-end |
| 7 | **One-radio Zigbee+Thread concurrency (multi-PAN)** on our MG24 | **IGNORE-DELIBERATELY** | Alive at Silicon Labs, dead at every host stack: EZSP v16 fork, ZHA-incompatible, deprecated add-on from a custom repo, changes the IEEE address. Nabu Casa shipped MG24 hardware and said "we don't plan to implement it" (§3b) | A ZHA/zigpy reversal **and** an independent long-run replication of SONOFF's v4.6.0 claims on MG24 |
| 8 | **MG24 as a Thread migration option** (sequential, not simultaneous) | **WATCH** | The silicon and firmware exist, so no forced hardware replacement to *reach* Thread — but the flash is destructive to Zigbee and re-pairs every device (§3d) | Matter/Thread device classes we need that Zigbee cannot serve |
| 9 | **Second dedicated dongle if we ever need Thread** | **RIDE NOW (as the plan of record)** | ~$33–49, and it is what ZHA, Z2M and HA all explicitly recommend (§3d) | — |
| 10 | **Mains Zigbee mmWave as Wave-3 device class + auto-recalibration** | **RIDE NOW** | Only class where a Zigbee-first hub competes on equal footing; and stuck-presence from stale radar background models is the #1 cross-vendor complaint and is **fixable in software by the hub** (§4a, §4e) | Evidence that vendors are fixing background-model drift in firmware themselves |
| 11 | **Per-device reporting-rate throttling + Zigbee channel-selection guard** | **RIDE NOW** | Tuya-class radar floods the mesh (documented, unfixable device-side) and Aqara FP1 refuses channels 21–24 — both are v1 architecture inputs, not polish (§4c) | — |
| 12 | **Battery Zigbee mmWave** | **WATCH** | Newly real (Third Reality R2, FP300, ZG-204ZM) but quality is unproven-to-poor: config resets, ~50% stick rates, hardware-revision lottery (§4a, §4e) | A battery Zigbee part with clean Z2M support and a reviewer verdict that isn't "be willing to tinker" |
| 13 | **Zone/coordinate presence over Zigbee** | **WATCH** (gap, possibly a build) | Genuinely valuable, genuinely unavailable — **no Zigbee device exposes LD2450-class multi-target X/Y**; the module is €6.90 (§4c, §4e) | A decision to do first-party hardware, or a Zigbee zone sensor shipping from someone credible |
| 14 | **Presence as a boolean** | **IGNORE-DELIBERATELY** (i.e. don't lock the model) | Matter 1.6 reportedly adds a provisional *ambient context sensor* — semantic presence (who/what/doing-what), 10 activities + 12 objects + 21 sounds (§4b) | Corroboration that the device type is real; or its removal before certifiability |
| 15 | **BLE identity presence (ESPresense/Bermuda)** | **WATCH** — consume, don't build | Identity-first not occupancy-first; high labour, ~$5/room BOM; Bermuda's last tagged release was 2025-08-05 (§4b, §4e) | Bermuda resuming releases, or a customer pull for per-person room presence |
| 16 | **UWB** | **IGNORE-DELIBERATELY** | Nothing consumer has shipped; Apple's own 2026 presence bet is a camera; FiRa still publishes use cases, not products; UWB-radar is explicitly long-term (§4b) | A shipping, reviewed consumer UWB room-presence product |
| 17 | **EU CRA compliance artifacts in CI from day one** | **RIDE NOW** | Article 14's 24-hour clock starts **2026-09-11**; marginal compliance cost per release goes to ~zero if built into the pipeline and stays variable if retrofitted (§5a, §5d) | Confirmed evidence the Digital Omnibus moves CRA dates (none found) |
| 18 | **Cyber Trust Mark in launch messaging** | **IGNORE-DELIBERATELY** | Three years, zero certified products, administrator resigned under a national-security review, no application date four months after the replacement was named (§5b) | FCC/ioXt announcing an application-opening date |
| 19 | **Open-source public technical documentation as the Class I conformity route** | **WATCH** (decision blocked on classification) | May be the *only* affordable route if the hub is Class I, since no harmonised standard is cited in the OJ — but the steward regime is **not** an escape hatch for a monetising vendor (§5a, §5d) | Reading IR (EU) 2025/2392 and C(2026) 5252 to settle whether our hub is Default or Class I |

---

## §7 — WHAT CHANGES OUR PLANS

1. **Our core claim is demonstrable in one file, not merely assertable — but the cheap half of it is one upstream PR away.** HA's `async_get_exposed_entities()` hands the LLM `names / domain / state / areas / 14 filtered attributes` and **actively discards** `last_changed` / `last_updated`, which its own REST API carries; every third-party MCP server does the same or worse. **Ship an inbound MCP server early and cheaply for presence, but position the moat on contract + read-time derivation + explanation, never on the timestamp.** → §1c, §1d
2. **Matter already ships our reporting-contract concept and nobody surfaces it — which validates the shape and hands us the vocabulary.** The negotiated subscription `MaxInterval` (and ICD `IdleModeDuration`, up to **64800 s**) is a per-node, protocol-enforced, machine-readable staleness bound that every controller collapses into a debounced, fail-open boolean. **"Last confirmed alive at T; contract permits silence until T + D" is our product stated in the standard's own terms — use it in the message, and treat controller `available` as untrustworthy in the design.** → §2b, §2d
3. **Delete every multiprotocol line item from the runway; budget $35 instead.** One-radio Zigbee+Thread is alive at Silicon Labs and dead at all three host stacks (EZSP v16 fork, ZHA-incompatible, deprecated add-on from a custom repo, changes the IEEE address); Nabu Casa shipped MG24 hardware in Nov 2025 saying *"we don't plan to implement it."* **Our MG24 is a sequential dual-protocol asset — the option to switch, not to do both.** → §3b, §3d
4. **CRA Article 14's 24-hour actively-exploited reporting clock starts 2026-09-11 — six weeks out — and event sourcing is the operational answer to it.** Determining exploitation within 24 hours requires evidence of what actually executed; without it a vendor must over-report or under-report. **This is a launch-timing and market-entry input now, not a 2027 problem — and the transitional treatment of products placed on the market before Dec 2027 is the single unresolved question most likely to change the plan.** → §5a, §5d
5. **Strike the US Cyber Trust Mark from every launch message and plan.** Three years from announcement, zero certified products, the Lead Administrator resigned in Dec 2025 under a national-security review, and four months after ioXt replaced it there is still no application date. **It is an option to exercise later, not a milestone to schedule around.** → §5b
6. **Do not lock presence as a boolean.** Matter 1.6 reportedly introduces a provisional **ambient context sensor** covering 10 human activities, 12 object identifications and 21 sound identifications, with concurrent reporting from up to 10 sources — semantic presence, not occupancy. *(MED confidence: single vendor-research source, not corroborated by CSA's own announcement — corroborate before betting hard.)* **A hub modelling presence as a bit today is modelling the wrong shape by 2027.** → §4b
7. **The #1 cross-vendor presence complaint is a software problem a hub can own — and it is our thesis applied one layer down.** Four sensors from three vendors, all radios, all get stuck presence in the same hostile room roughly monthly; the fix is a manual "dynamic background calibration" press. **A hub that detects a stale radar background model — presence asserted past a learned per-room ceiling with zero corroborating illuminance/PIR evidence — and issues the recalibration command fixes in software what no vendor fixes in firmware. That is evidence-based availability applied to a sensor's own self-report, and it is a demo.** → §4a, §4e

---

## Appendix — honest limits of this return

**Read but explicitly downgraded:** the Matter 1.6 "ambient context sensor" (§4b) rests on one vendor-research page that CSA's own release does not corroborate — MED, corroborate before acting. The How-To Geek claim that Apple is "only on Matter 1.2" and Google "still on 1.0" (§2c) is flagged LOW and should not be repeated. CRA Article 13(8)'s "at least five years" is mirror-only text (§5a).

**Could not be read (not summarised, not cited as content):** all Matter Core / Application Cluster specification PDFs (CSA download form) · Thread 1.4.1 specification (Thread Group request form) · Implementing Regulation (EU) 2025/2392 · EUR-Lex Articles 13/14/71 and Annexes I/III verbatim (proxy 403; HTML truncated at recital 42) · `fcc.gov/CyberTrustMark` (403) · PulseMCP (robots) · Amazon retail listings (robots) · Matter Alpha's Homey-AI and Matter-1.6 articles (HTTP 520) · one law-firm Digital Omnibus briefing (HTTP 402) · Reddit at any scale (proxy rejected domain-restricted queries).

**Highest-value next reads, in order:** (1) Commission guidance **C(2026) 5252** of 2026-07-27, in full — settles our CRA classification and the transitional question, which is the biggest single unknown in this return. (2) **OpenHomeFoundation roadmap issue #16, "Voice is more transparent"** — the only signal found that HA may be moving onto our lane. (3) The **Matter 1.6 Device Type Library** entry for the ambient context sensor — corroborates or kills finding #6. (4) **Google Home's `OnlineState` schema reference** (`developers.home.google.com/automations/schema/reference/entity/sht_device/online_state`) — cheap, and shows how one major ecosystem models device online state.
