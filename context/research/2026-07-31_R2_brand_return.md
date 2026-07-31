<!--
file: context/research/2026-07-31_R2_brand_return.md
purpose: R-2 BRAND lane return per the 2026-07-31 research-lane briefs (§0 + §R-2). Names / voice-of-customer / positioning / explainability-in-marketing / launch-channel map. Feeds THE LAUNCH-RUNWAY CHARTER (Aug-12-13).
audience: Nick (dispatch), Hub (intake)
state-type: research return (lane deliverable)
status: DELIVERED 2026-07-31 (due Aug-10; early)
lane-discipline: this lane wrote ONE file and committed nothing.
-->

# R-2 BRAND — Lane Return

**Executed:** 2026-07-31. **All URLs below were opened on 2026-07-31** unless a different access date is stated. Source dates are given separately from access dates throughout.

---

## §0-COMPLIANCE — read this before you trust anything below

Three method facts bound every claim in this document. They are stated once, here, and not repeated.

**(a) Reddit was 100% unreachable.** Every retrieval path in this environment returned `HTTP 403 PROXY_REJECTED` for both `www.reddit.com` and `old.reddit.com`, across four independent research passes, on both page fetches and domain-scoped search. **r/homeassistant, r/homeautomation, r/smartthings, r/hubitat and r/selfhosted are entirely unrepresented in this return.** The brief named those subreddits as primary sources for §2 and §5; that instruction could not be executed. What survives is Discourse forums (community.home-assistant.io, community.hubitat.com, community.smartthings.com), GitHub, and Hacker News. **Consequence (INFERENCE, HIGH):** the phrase bank in §2 is skewed toward the more measured register of forum posters — high-competence self-hosters — and away from the rawer mass-market language that lives on Reddit. Every emotional-intensity read in §2 should be treated as a *floor*, not a ceiling. **What would answer this:** one lane-session with Reddit fetch permitted, or a manual paste of ~10 thread bodies.

**(b) Verbatim quotes are verbatim-as-extracted.** Direct `curl` is blocked (403 on CONNECT), so pages came through a fetch tool that passes text through an extraction model under explicit "transcribe exactly, preserve typos" instruction. Mitigation: surviving misspellings and broken grammar across the corpus (`stucked`, `unreachble`, `kitch`, `silently go unresponse`) are strong evidence of genuine transcription rather than rewriting. Where retrieval used a **raw JSON endpoint** — Discourse `.json`, HN Algolia `hn.algolia.com/api/v1/items/<id>` — the text is unrendered and the quote is exact; those are marked **[RAW]**. **Rule for use: any quote from this bank that is going to appear on a public surface must be spot-checked against the rendered page first.** Two attributions are flagged inline as uncertain.

**(c) HN item HTML pages returned wrong metrics twice** (two Show HN posts showed implausible ages and scores). Every HN number in §5 is Algolia-API-confirmed. Treat single HN HTML reads in other lanes with suspicion.

---

## §1 — THE COLLISION TABLE

### 1.0 The premise problem — state this before the table (FACT, HIGH)

The brief asks for a knockout scan on **"HomeSynapse" and "NexSys."** Per the hivemind's own record those are **legacy names, superseded eight days before this brief was written**:

- **ASIMTOTE** is the locked company name (2026-06-13, re-confirmed 2026-07-11).
- **TAMORO** is the leading product/ecosystem candidate; **Architecture C was RATIFIED by Nick on 2026-07-23** (TAMORO forward on every consumer surface, ASIMTOTE the real-but-quiet parent), and **Q2 ruled the engine register as "TAMORO Core."**
- A **paid Pelton comprehensive search + written analysis** ($1,200, SIGNED+PAID) lands **~Aug-5**, and **R-1 (the name) resolves at G-2 on those results.**
- The record already contains the verdict this lane was asked to reach: the two-brand NexSys/HomeSynapse split is logged as *"a standing cost"* that W-7 half-collapsed, and it is cited in the 2026-07-22 decision package as the direct argument against re-creating a two-public-brand surface.

*Source: `context/strategy/brand-program/2026-07-22_brand-architecture_decision-package.md` §0/§6; `context/strategy/brand-program/2026-07-23_domain-handle-claims-refresh.md`.*

**Two consequences for how this section was executed:**

1. **This lane deliberately does NOT duplicate the TAMORO/ASIMTOTE clearance.** A knockout pass by a non-lawyer five days before a paid comprehensive search returns would add no information and could anchor the G-2 read on amateur findings. Counsel's instrument is the instrument. **Nothing in this section is a trademark-risk conclusion or clearance.**
2. **The legacy scan was still run, because the legacy names still carry live exposure.** The repository is `homesynapse-core`, the hivemind is `nexsys-hivemind`, and Java namespaces are explicitly **deferred** (decision package Deliverable 4 row 6). If those strings survive into public repo URLs, package coordinates, or Docker image names at launch, they ship — regardless of what the consumer mark says. **The scan below prices that residual exposure.**

### 1.1 The table

Severity key: **CRITICAL** = would block or embarrass a public launch · **HIGH** = material confusion or a credible objector · **MED** = friction, findable, survivable · **LOW** = noise.

| Name | Arena | Finding | Severity | Link |
|---|---|---|---|---|
| **HomeSynapse** | Domain (.com) | **`homesynapse.com` is REGISTERED and LIVE** — Cloudflare NS (`raphaela`/`elmo.ns.cloudflare.com`); serves a **"coming soon" countdown page carrying a "HomeSynapse logo"** and the line *"Big things always start small, and good things come to those who wait."* Someone is actively preparing to launch under this exact name. | **CRITICAL** | [homesynapse.com](https://homesynapse.com) · DNS via [dns.google/resolve](https://dns.google/resolve?name=homesynapse.com&type=NS) |
| **HomeSynapse** | GitHub | **`github.com/homesynapse` EXISTS** — user account, ID 257191284, zero public repos. GitHub user and org names share one namespace, so an org of this name **cannot be created**. | **HIGH** | [github.com/homesynapse](https://github.com/homesynapse) |
| **HomeSynapse** | Category-adjacent naming (the launch audience) | **"Synapse" already means something specific to our exact launch community.** Matrix's homeserver is named **Synapse** — *"an open source Matrix homeserver implementation, written and maintained by Element."* In r/selfhosted / HN vocabulary, "Synapse" + "home" collides head-on with **"Synapse homeserver."** | **CRITICAL** | [element-hq/synapse](https://github.com/element-hq/synapse) (4.3k stars) |
| **HomeSynapse** | Smart-home vendors | `Synapse Smart Homes` (installer); `synapse-system.com` — *"Android Based Home Automation and Security System"* (India); `Digital-Alchemy-TS/synapse` — *"Typescript utilities for creating and managing virtual entities within Home Assistant"* (3 stars, **our exact stack**). | **HIGH** | [synapsesmarthomes.com](https://www.synapsesmarthomes.com/) · [synapse-system.com](http://www.synapse-system.com/home-automation-system.html) · [Digital-Alchemy-TS/synapse](https://github.com/Digital-Alchemy-TS/synapse) |
| **HomeSynapse** | Corporate / hardware | **Synapse Product Development** (`synapse.com`) — established hardware/product engineering firm publishing smart-home thought-leadership (*"Why Your Smart Home Isn't Truly Smart…Yet"*). Deep pockets, adjacent field. | **HIGH** | [synapse.com](https://www.synapse.com/the-edge/why-your-smart-home-isnt-truly-smart-yet/) |
| **HomeSynapse** | App stores | Multiple live "Synapse" apps incl. `Synapse` (id6756261199), `Synapse Apps, LLC`, `Synapse Product Development`, `Synapse ITS`. Field is crowded; no exact "HomeSynapse" app found. | MED | [apps.apple.com](https://apps.apple.com/au/app/synapse/id6756261199) |
| **HomeSynapse** | USPTO (knockout, via web) | **No `HOMESYNAPSE` record surfaced.** Caveat: the Justia search interface returned a pagination error rather than a clean zero-result page — **treat as weak evidence, not a clean absence.** | LOW *(conf. LOW)* | [trademarks.justia.com](https://trademarks.justia.com/) |
| **NexSys** | USPTO — **Class 009** | **`NEXSYS`, Reg. 3952639, LIVE (registered + renewed)** — owner **EH Europe GmbH** (EnerSys entity), goods *"Batteries and battery chargers,"* **International Class 009**. Filed 2010-06-16. | **CRITICAL** | [Justia 3952639](https://trademarks.justia.com/850/64/nexsys-85064419.html) |
| **NexSys** | USPTO — **Class 009** | **`NEXSYS`, Reg. 4650236, LIVE (Section 8 & 15 accepted 2020-03-13)** — owner **Lakewood Instruments LLC**, goods *"Programmable electronic controllers for controlling water treatment equipment, fluid processes, and chemical feed systems,"* **Class 009**. Filed 2013-10-01, registered 2014-12-02. **A live Class-009 registration for programmable controllers is functionally adjacent to a smart-home controller.** | **CRITICAL** | [Justia 4650236](https://trademarks.justia.com/860/79/nexsys-86079334.html) |
| **NexSys** | USPTO — Class 040 | `NEXSYS`, Reg. 2860745, LIVE (renewed 2014-07-15) — owner **Taiwan Semiconductor Manufacturing Co.**, Class 040 (semiconductor custom manufacture). Different class; matters only as evidence the mark is contested by large actors. | MED | [Justia 2860745](https://trademarks.justia.com/763/32/nexsys-76332983.html) |
| **NexSys** | Live product, in-market | **`NexSys®`** — EnerSys battery product line, marked with **®** across the site, spanning NexSys iON / NexSys TPPL / NexSys blocs, with global catalogues (Americas, EMEA, Japan) and a dedicated storefront. | **CRITICAL** | [enersys.com/…/nexsys](https://www.enersys.com/en/products/batteries/nexsys/) · [nexsysstore.com](https://nexsysstore.com/) |
| **NexSys** | Corporate (well-resourced) | **Nexsys Technologies LLC** — a **Rocket Companies** subsidiary in mortgage/title software (Clear HOI etc.), with sustained PR since 2019. A large, well-counseled corporate on the same string. | **HIGH** | [rocketcompanies.com press](https://www.rocketcompanies.com/press-release/nexsys-technologies-releases-clear-hoi-a-groundbreaking-homeowners-insurance-verification-tool-to-all-mortgage-lenders/) |
| **NexSys** | Other live companies | `NEXSYS-ONE` (software, nexsysone.com) · `Nexsys` LatAm IT distributor (nexsysla.com) · `nexsys.co.uk` (smart-factory software) · `nexsys.global` · `nexsys.consulting` · `Nexsys Motorsport LLC` · `NeXsys Group Inc.` | **HIGH** | [nexsysone.com](https://www.nexsysone.com/) · [nexsysla.com](https://www.nexsysla.com/us/about-us/) · [nexsys.co.uk](https://www.nexsys.co.uk/smart-factory-software-syspro/) |
| **NexSys** | Domain (.com) | `nexsys.com` — REGISTERED, **Afternic NS** (`ns3`/`ns4.afternic.com`) = brokered/for-sale portfolio. Not obtainable cheaply. | **HIGH** | DNS via [dns.google/resolve](https://dns.google/resolve?name=nexsys.com&type=NS) |
| **NexSys** | GitHub | `github.com/nexsys` — **TAKEN**, active third party (4 repos, ML/data-science). | MED | [github.com/nexsys](https://github.com/nexsys) |
| *EU / EUIPO* | Both names | **NOT REACHED.** EUIPO eSearch was not retrievable in this environment. Recorded as a gap, not a clean read. | — | — |

### 1.2 §1 verdict

**NEXSYS FAILS A KNOCKOUT PASS OUTRIGHT (FACT, HIGH).** Two **live, renewed, Class-009** US registrations — the exact class a smart-home controller and its software would file in — one of them for *programmable electronic controllers*, plus a globally-marketed `NexSys®` product line, plus a Rocket Companies subsidiary, plus five-plus live companies and a brokered .com. This is not a close call and does not need counsel to reach.

**HOMESYNAPSE FAILS FOR A DIFFERENT AND MORE INTERESTING REASON (INFERENCE, HIGH).** The trademark picture is unresolved (no record surfaced, but on a weak search). The *practical* picture is decisive: **the .com is held by a third party actively counting down to a launch under a HomeSynapse logo**, the GitHub namespace is gone, and — the sharpest point — **"Synapse" is already claimed vocabulary inside the precise community §5 identifies as our launch channel.** Every self-hoster who reads "HomeSynapse" on HN parses it against Matrix Synapse first.

**What this means, stated plainly (OPINION, HIGH):** the R-2 name question returns a result that **confirms a decision already taken rather than reopening it.** Moving off NexSys/HomeSynapse was correct, and this scan independently prices what staying would have cost. The live question — TAMORO — is counsel's, and its instrument lands ~Aug-5.

**The residual exposure that is NOT yet handled (INFERENCE, HIGH → see §6.1).** The consumer mark moved; the *artifact strings* did not. `homesynapse-core` as a public repo name would inherit the Matrix-Synapse confusion **and** point at a third party's live countdown site, in front of the one audience most likely to notice.

### 1.3 One-minute checks this lane could not close

- **Is `homesynapse.com` yours?** NS are Cloudflare; the known owned families (asimtote.\*, tamoro.co/.tech) sit on **GoDaddy** infrastructure. That mismatch reads third-party (INFERENCE, MED). A registrar-dashboard glance settles it. *Same discipline as the open `tamorro.com` question in the 07-23 refresh.*
- **Is `github.com/homesynapse` yours?** Zero repos, ID 257191284 (high = recently created). If not yours, the namespace is fenced.

---

## §2 — THE PHRASE BANK

**35 verbatim quotes, four clusters.** Read §0-COMPLIANCE (a) and (b) first: Reddit is absent, and quotes marked **[RAW]** came through unrendered JSON endpoints (highest fidelity). Platform is noted where the poster stated it.

### Cluster A — AVAILABILITY LIES

> "It sometimes happens that devices silently go down without any chance to tell Home Assistant about that."

ToHi · HA, battery Zigbee/Z-Wave sensors · [community.home-assistant.io/t/658030](https://community.home-assistant.io/t/detecting-unresponsive-devices/658030) · posted 2023-12-19 · *sleepy devices send no keep-alive, so death is invisible by construction*

> "It seems, after restarting Home Assistant, entities of dead devices get a refreshed 'last_changed' and/or 'last_updated'."

ToHi · HA · [same thread](https://community.home-assistant.io/t/detecting-unresponsive-devices/658030) · posted 2024-01-07 · ***"last seen" that means nothing** — a restart makes every physically dead device look freshly alive. The purest instance of the disease in the corpus.*

> "The device doesn't go unavailable, it simply doesn't update status anymore. binary_sensor stucked at on/off, illumination sensor stucked at a certain value."

*(author not captured — quote text HIGH conf., attribution LOW)* · HA · [same thread](https://community.home-assistant.io/t/detecting-unresponsive-devices/658030) · thread spans 2023-12→2025-03 · *stale value presented as current, stated exactly*

> "I noticed that it often silently go unresponse. The behavior is all the binary_sensors and sensor don't change their states."

cofw2005 · HA, Aqara presence via HomeKit *(platform MED)* · [same thread](https://community.home-assistant.io/t/detecting-unresponsive-devices/658030) · posted 2025-03-08

> "This is either found when using the device or even worse, go back in the sensor history to see that "the living room temperature has been fixed for the last 144 hours.""

MDSDM · HA · [community.home-assistant.io/t/537848](https://community.home-assistant.io/t/request-notification-on-dead-devices/537848) · posted 2024-01-24 · *six days of a dashboard reporting a number as current; discovery is retrospective and accidental*

> "Some of them report 30% battery but work for months. Sometimes they show 40% forever but are dead."

ToHi · HA, Z-Wave + Zigbee · [community.home-assistant.io/t/658030](https://community.home-assistant.io/t/detecting-unresponsive-devices/658030) · posted 2024-04-03

> "I don't think I have a single device where the reported battery level is actually useful. :)"

brooksben11 · HA · [community.home-assistant.io/t/771130](https://community.home-assistant.io/t/getting-notified-when-a-sensor-is-dead-is-there-a-way/771130) · posted 2024-09-15 · *total distrust of a first-class UI field, stated casually as consensus — learned helplessness phrased as a joke*

> "the sensors keep reporting a battery level above 80 or even 90% and then they die."

fridolin · HA · [same thread](https://community.home-assistant.io/t/getting-notified-when-a-sensor-is-dead-is-there-a-way/771130) · posted 2024-09-15

> "The status in Hubitat is never accurate, and changes randomly."

SmplTeddyBear · Hubitat, Zigbee · [community.hubitat.com/t/87780](https://community.hubitat.com/t/having-issues-with-hubitat-showing-correct-device-status/87780) · posted 2022-01-20

> "I can toggle the light off, the switch will update correct to show off, but then if I open the Dashboard hours later the switch on the Dashboard indicates its on when the bulbs are not."

SmplTeddyBear · Hubitat dashboard · [same thread](https://community.hubitat.com/t/having-issues-with-hubitat-showing-correct-device-status/87780) · posted 2022-01-20 · *state is correct at the moment of action, then silently decays into fiction*

> "For example, a light will be off but the dashboard and the device detail will show that it is on."

kenny_a_davis · Hubitat · [community.hubitat.com/t/130909](https://community.hubitat.com/t/devices-not-always-showing-correct-status-in-hubitat/130909) · posted 2024-01-01 · *summary and detail views agree with each other and disagree with the house*

> "If I go to the device details page for the light, its current state will show as on until I hit refresh."

kenny_a_davis · Hubitat · [same thread](https://community.hubitat.com/t/devices-not-always-showing-correct-status-in-hubitat/130909) · posted 2024-01-01 · *"current state" is a cache with no expiry*

> "my z-wave kitch light keeps showing "off" but it is clearly on"

v6turbo · Hubitat, Z-Wave · [community.hubitat.com/t/108636](https://community.hubitat.com/t/light-shows-off-but-light-is-on/108636) · posted 2022-12-28

> "Can the device receive and act on events but not update its status properly with hubitat, thus hubitat is out of sync with actual device state and all rules that depend on that state will fail?"

bill · Hubitat · [community.hubitat.com/t/45063](https://community.hubitat.com/t/hubitat-out-of-sync-with-device-state/45063) · posted 2020-07-14 · **the bridge quote — a user deriving the contagion himself: a lying state layer silently poisons every automation above it**

> "That all goes out the window if hubitat can't even maintain legitimate state though."

bill · Hubitat · [same thread](https://community.hubitat.com/t/hubitat-out-of-sync-with-device-state/45063) · posted 2020-07-14 · *state integrity framed as the precondition for the category having any value*

> "The status of all my zigbee devices alternates between unavailable and the respective entity status."

blade-of-fire · HA + Zigbee2MQTT · [community.home-assistant.io/t/706495](https://community.home-assistant.io/t/zigbee2mqtt-devices-alternating-between-unavailable-and-correct-state/706495) · posted 2024-03-20 · *availability flapping — the signal gets so noisy that "unavailable" stops carrying information and users learn to ignore it*

### Cluster B — SILENT AUTOMATION FAILURE

> "I have 2 automations that just quit working."
> "I'm not even sure when or how they just one day quit working."

cowboysdude · HA · [community.home-assistant.io/t/392661](https://community.home-assistant.io/t/automations-just-quit-working/392661) · posted 2022-02-14 · *no failure event, no timestamp — the user cannot establish even **when** it broke*

> "I've been stumped for a month and would like to get these working again....having to go in and do this all manually everyday is wearing me out LOL"

cowboysdude · HA · [same thread](https://community.home-assistant.io/t/automations-just-quit-working/392661) · posted 2022-02-14 · *a month of manual labour plus the load of not knowing; "wearing me out" is the emotional core*

> "One (or a few) automations execute their actions just partially or not at all."

stefre · HA · [community.home-assistant.io/t/614539](https://community.home-assistant.io/t/add-error-exception-handling-to-automations/614539) · posted 2023-09-15 · *half-executed automation stated as the canonical failure mode*

> "Once(!) noticed: crawl through log files, find the automation, analyse root cause"

stefre · HA · [same thread](https://community.home-assistant.io/t/add-error-exception-handling-to-automations/614539) · posted 2023-09-15 · **the emphatic "(!)" carries the whole complaint — noticing is the hard part; debugging only starts after a lucky discovery**

> "I had an automation fail overnight as a Zigbee device failed to respond. The device did switch off as requested but the automation failed to continue"

RalphG · HA + Zigbee · [same thread](https://community.home-assistant.io/t/add-error-exception-handling-to-automations/614539) · posted 2024-07-23 · *partial success is worse than failure — the action happened, the sequence aborted, nothing raised an alarm overnight*

> "I cannot find a good way to make my automation reliable or tell me when it fails"

michaelmarconi · HA architecture discussion · [github.com/home-assistant/architecture/discussions/845](https://github.com/home-assistant/architecture/discussions/845) · posted 2023-11-16 · **the two asks stated as one. Users will accept failure; they will not accept *unannounced* failure.**

> "So I understand there isn't something generic that checks automations? I think it would be a good use-case of having something generic for failed automation."

liorfranko · HA · [community.home-assistant.io/t/729235](https://community.home-assistant.io/t/get-notify-when-an-automation-failed-to-run/729235) · posted 2024-05-15 · *user discovers there is no system-level watchdog and is surprised by the absence*

> "I have a Sunset automation that turns on light on Sunset, when one of the lights is unreachble. I have automations for Alarms, when I replaced my wife's phone, the notification failed to be sent."

liorfranko · HA · [same thread](https://community.home-assistant.io/t/get-notify-when-an-automation-failed-to-run/729235) · posted 2024-05-15 · ***the alerting channel itself failed silently*** *— a stale notify target meant the alarm never reached anyone*

> "Had the below automation working for literally a year with NO problems."
> "The only thing I can think of is one of the updates borked something, but I have no idea what."

axsdenied · HA + ZHA · [community.home-assistant.io/t/600935](https://community.home-assistant.io/t/automation-working-for-a-year-stops/600935) · posted 2023-08-09 · *root cause was an unavailable entity on a disabled trigger — **an availability lie causing a silent automation failure***

> "I have a situation where checking the config doesn't return any error, yet reloading automations or all YAML or even restarting HA doesn't load the automation at all - no trace of it in home-assistant.log or in the automations or the states pages."

dannutu · HA · [community.home-assistant.io/t/253665](https://community.home-assistant.io/t/how-do-i-troubleshoot-an-automation-not-firing/253665) · posted 2024-02-29 · **"no trace of it"** *— config validates, logs are clean, and the absence is invisible*

> "If I turn off a HA light group, HA reports all lights in the group as off, but random (zigbee) lights in the group remain on."

alpacalypse · HA + Zigbee · [community.home-assistant.io/t/235158](https://community.home-assistant.io/t/zha-light-state-bounces-and-often-not-reflected-accurately/235158) · posted 2022-12-21 · **the strongest single quote for commanded-vs-confirmed: the system reports the *intended* state, not the *observed* state**

> "I turn off (or on) a group of lights and in real life the lights are turned on or off correctly, but in HA the state for the individual lights sometimes hang in the old state."

Veldkornet · HA + ZHA · [same thread](https://community.home-assistant.io/t/zha-light-state-bounces-and-often-not-reflected-accurately/235158) · posted 2020-10-31 · *note **"in real life"** as the explicit reality/model split*

> "They are still available as entities and switching them on on the dashboard does not switch the device on, only the switch in the UI."

JKoehorst2 *(attribution MED; quote HIGH)* · HA + ZHA · [github.com/home-assistant/core/issues/95288](https://github.com/home-assistant/core/issues/95288) · posted 2023-07 · ***"only the switch in the UI"*** *— the toggle animates, the entity stays available, the device is dead*

> "Click the switch in the HA interface to turn on a light, the light turns on almost immediately but the report that the light turned on takes a few seconds to arrive and you see the UI flipflopping causing confusion."

marcelveldt · HA core architecture discussion · [github.com/home-assistant/architecture/discussions/740](https://github.com/home-assistant/architecture/discussions/740) · posted 2022-02-24 · **a core HA developer naming the optimistic-state problem: the UI asserts a change before confirmation, so users cannot distinguish in-flight from failed**

> "This has worked for years but not now."

Edesignsplans · SmartThings · [community.smartthings.com/t/306282](https://community.smartthings.com/t/my-routine-has-stop-working/306282) · posted 2025-10-31

### Cluster C — DEBUGGING OPACITY

> "My what the heck moment was that sometime ago my light turned itself on and to this day I do not know what triggered it. So I'd like to improve logbook and add information about what actually triggered the change."

LordBoos · HA · [community.home-assistant.io/t/219488](https://community.home-assistant.io/t/what-the-heck-turned-my-light-on/219488) · posted 2020-08-18 · **[RAW]**

> "I've looked in the logs on the sonoff devices, in HA, in the logbook but I can't find what's causing these to turn on. I thought my HA install had perhaps been compromised, but i've looked through my firewall logs too and can't find anything to support that.
> This is driving me crazy!"

velkrosmaak · HA + Sonoff/ESPurna/MQTT · [community.home-assistant.io/t/658987](https://community.home-assistant.io/t/lights-mysteriously-turn-themselves-on-no-detail-in-logbook/658987) · posted 2023-12-21 · **[RAW]** · ***opacity escalates to a security scare*** *— absent causal data, the user's next hypothesis is "I've been hacked"*

> "The log book and device information tells me the light has been switched on but not by what or why - I don't know how to troubleshoot if the logs are only telling me when the entity was turned on. Could it be possible to have device XXX has been turned on by YYY"

AndyMack · HA · [community.home-assistant.io/t/814755](https://community.home-assistant.io/t/wth-can-i-not-find-out-what-automation-or-action-just-turned-on-my-light/814755) · posted 2024-12-22 · **[RAW]** · *names the exact gap — **"when" is logged, "by what or why" is not** — then writes the desired output format himself*

> "When trying to understand why an automation did not work as expected the traces are the place to go. Nevertheless i find it unnecesary complicated to read them. When there are multiple conditions it uses the term conditions/0, conditions/1 etc. instead of showing the condition itself."

StefanHabel · HA · [community.home-assistant.io/t/812645](https://community.home-assistant.io/t/why-are-the-traces-of-an-automation-so-complicated-to-read/812645) · posted 2024-12-17 · **[RAW]** · *machine node-paths instead of the human-authored condition text*

> "I think traces only shows last 3 triggers. Whenever I've tried to find issue it seems the incident I'm looking for is no longer available or gets overridden while I'm testing"

Tmjpugh · HA · [same thread](https://community.home-assistant.io/t/why-are-the-traces-of-an-automation-so-complicated-to-read/812645) · posted 2024-12-18 · **[RAW]** · **the evidence destroys itself under investigation — the act of testing evicts the trace of the event being investigated. Highest-value mechanism in this cluster.**

> "I currently don't have a trace showing the problem because the automation runs too often, and it pushes the failed runs out of the history."

Steve Dinn · HA 2025.10.3 · [community.home-assistant.io/t/942957](https://community.home-assistant.io/t/automation-triggered-but-not-running/942957) · posted 2025-10-22 · **[RAW]** · *independent restatement of trace eviction, 10 months after Tmjpugh*

> "The automation is getting triggered, and it's producing traces, but no steps are executed, not even the first one... I'm not even sure that this isn't happening with other automations, because there are no errors being logged."

Steve Dinn · HA + Folder Watcher · [same thread](https://community.home-assistant.io/t/automation-triggered-but-not-running/942957) · posted 2025-10-22 · **[RAW]** · **note the second sentence — opacity generalizes into distrust of the whole system, not just this automation**

> "That's interesting. I would have expected an error saying as much. Something like "25 instances of this automation are already queued. The queue is full.""

Steve Dinn · HA · [same thread](https://community.home-assistant.io/t/automation-triggered-but-not-running/942957) · posted 2025-10-23 · **[RAW]** · **the user writes the error message the system should have produced — the single most directly usable copy artifact in this bank**

> "the trace just showing a red line to nowhere wasn't as helpful as it could be. I had to look at the trace timeline section and it said why it stopped in there. And it is strange that nothing was reported in the logs. the docs say that a warning will be raised but I didn't see anything at all about any automation in the logs in that timeframe."

finity · HA + LG ThinQ · [community.home-assistant.io/t/1015631](https://community.home-assistant.io/t/why7-did-this-automation-not-actually-execute/1015631) · posted **2026-06-30** · **[RAW]** · ***the most recent artifact in this bank — one month old.** The explanation exists but is in a different tab, and the documented warning never reached the log.*

> "Does anyone else find that automation traces sometimes don't work, giving a 'Chosen trace is no longer available' error message?"

jarrah · HA · [community.home-assistant.io/t/361630](https://community.home-assistant.io/t/automation-and-script-debugging/361630) · posted 2021-11-29 · **[RAW]** · *the logbook's own "show trace" link lands on an expired trace; answered in-thread: "Only 5 traces are stored"*

> "Rule actually works/worked but there is nothing in the log... However "past logs" did not have any records related to the above rule. Rule was triggered at least by first trigger event but rule did not log anything. Why?"

Vitaliy Kh · **Hubitat** C-7, Rule Machine · [community.hubitat.com/t/91708](https://community.hubitat.com/t/no-logs-for-rule/91708) · posted 2022-04-01 · **[RAW]** · *cross-platform confirmation: same opacity on Hubitat*

> "Eventually it just got real laggy and stopped responding to input or device state changes promptly. I had no idea why that would have been, and had no desire to wade through Docker manure to figure out how to debug it, so my setup just kind of fell by the wayside."

mindslight · HN, on HA OS Release 8 · [news.ycombinator.com/item?id=31553657](https://news.ycombinator.com/item?id=31553657) · posted 2022-05-29 · **[RAW]** · **the terminal outcome: the user does not file a bug, they quit. Churn evidence.**

### Cluster D — CLOUD DISTRUST

> "There's no way I'm ever permanently installing some for-profit company's opaque, remotely updatable system into my home's walls. Even if they don't turn evil like Chamberlain did, it would be crazy to leave the basic functionality of my house's lights, door locks, HVAC, sensors, etc at the mercy of some vendor bug, broadband outage or regional S3 'mis-configuration'."

mrandish · Tasmota/ESPHome + HA, 75 in-wall dimmers · [news.ycombinator.com/item?id=46156195](https://news.ycombinator.com/item?id=46156195) · posted 2025-12-05 · **[RAW]** · *the fully-articulated local-first ideology; same comment demands layered fallbacks so the lights "always fucking work"*

> "Ten or so years ago, when Google was still mostly a darling, I never thought they would ever try to pull anything like that. Yet here we are, and my dropcam is just going to brick itself in April."
> "Similarly, at least one device I bought didn't require an account when I first got it, but then all of a sudden there was a new app update and you didn't think twice about it, but now this requires a cloud connection. It sneaks up on you"

kevstev · Google/Nest, Sonos · [news.ycombinator.com/item?id=39359636](https://news.ycombinator.com/item?id=39359636) · posted 2024-02-13 · **[RAW]** · *four grievances in one comment; **"It sneaks up on you"** is the retroactive-requirement idiom*

> "The issue is that you have a washing machine that you bought with a feature that you can watch the inside of the machine while it's running over wifi from anywhere in the world. Then the company "kills" their cloud features... and you no longer can watch your 4k stream of the washer working. Not even locally, not remotely, nothing. It's a feature you paid for, and 2 or 3 years down the line it's gone."

eddythompson80 · on the Belkin Wemo sunset · [news.ycombinator.com/item?id=44536750](https://news.ycombinator.com/item?id=44536750) · posted 2025-07-11 · **[RAW]**

> "The fact that the refund is only partial seems pretty unreasonable to me. If they are reneging on their side of the deal then they should return the money that they took."

apparent · Belkin Wemo · [news.ycombinator.com/item?id=44526196](https://news.ycombinator.com/item?id=44526196) (thread) · posted 2025-07-11 · **[RAW]** · *the sunset framed as **breach of contract**, not obsolescence.* Context: Belkin announced 2025-07-10 that support for nearly all Wemo devices ends 2026-01-31.

> "I still believe that calling an integration "local" and then it stops working when the internet is down is misleading. And the GUI is even worse - it shows a cloud icon next to the integration with the caption "depends on cloud". A lot of people (me included) will take that to mean that the others will work without cloud/internet access"

Magnavox · HA + Nuki lock · [community.home-assistant.io/t/493917](https://community.home-assistant.io/t/indicate-more-clearly-if-an-device-will-work-without-the-cloud-internet/493917) · posted 2022-11-28 · **[RAW]** · **a labelling-trust failure: the badge describes how the hub talks to the device, not whether the device survives an outage**

> "If you block the Nuki bridge from the internet it works fine for a couple of hours but if you restart home assistant after a given time period and it tries to re-authenticate with the bridge the bridge rejects any authentication until cloud access is restored. Meaning you would be unable to unlock the door which could lead to serious problems."

Magnavox · HA + Nuki · [same thread](https://community.home-assistant.io/t/indicate-more-clearly-if-an-device-will-work-without-the-cloud-internet/493917) · posted 2022-11-25 · **[RAW]** · *cloud dependency hidden in the **auth** path, not the control path; fails only after restart + elapsed time — exactly when you can't diagnose it*

> "You can have local execution on SmartThings, but the rules for that execution are in the cloud."

Ken Fraleigh · SmartThings · [community.hubitat.com/t/33692](https://community.hubitat.com/t/smartthings-has-an-outage-defect-by-taking-a-shot-at-hubitat/33692) · posted 2020-02-06 · **[RAW]**

> "Hehe, thats the stupid part. If Internet is down, it works locally. If internet is up, and ST cloud is down, it does not work.. Go figure... Hahaha"

RogerThat · SmartThings · [same thread](https://community.hubitat.com/t/smartthings-has-an-outage-defect-by-taking-a-shot-at-hubitat/33692) · posted 2020-02-06 · **[RAW]** · *the failover covers the wrong failure mode*

> "I opened a ticket with ST Support and the answer I got was "We aren't seeing any issues.""

Keo · SmartThings · [community.hubitat.com/t/896](https://community.hubitat.com/t/smartthings-platform-outage-again/896) · posted 2018-03-25 · **[RAW]** · **the hinge between opacity and distrust: with no independent observability, the user cannot contest the vendor's account of reality**

> "I woke up to find all my zwave devices along with the hub deleted. After much posting on the ST forum only to find Other users in the same boat as i.... it's time for me to go... This is unacceptable."

RC51 Tofuman · SmartThings, ~8 years tenure · [community.hubitat.com/t/116533](https://community.hubitat.com/t/leaving-smartthings/116533) · posted 2023-04-06 · **[RAW]** · *server-side data loss wipes a cloud-held device registry; long-tenure loyalist churns*

> "nothing like having the project done, go away to a confernece and have the wife call and say lights wont turn on. Come home and the hub is reset."

Ronv42 · SmartThings · [same thread](https://community.hubitat.com/t/leaving-smartthings/116533) · posted 2023-04-06 · **[RAW]** · *household-credibility damage; discovered by a family member while the owner is away*

> "Just a little over 4 years ago I bought a C-5 hub after one of the many cloud outages on SmartThings. I haven't had to be concerned with the cloud breaking my setup since!"

Ken Fraleigh · SmartThings → Hubitat · [same thread](https://community.hubitat.com/t/leaving-smartthings/116533) · posted 2023-04-06 · **[RAW]** · **direct switching-trigger evidence: an outage named as the purchase cause**

> "But yeah, the average life of a company is what 1 year? Don't get any product you want for more than 5 years from a company younger than 5 years if you need that company to exist for it to work."

lesuorac · Zigbee + HA · [news.ycombinator.com/item?id=46388371](https://news.ycombinator.com/item?id=46388371) · posted 2025-12-26 · **[RAW]** · **users now run explicit vendor-survival actuarial math before purchase. Directly relevant to a pre-launch company's launch messaging.**

> "I have accumulated so much smart-stuff fatigue, I can't stand anything branded as "smart"."

culebron21 · on IKEA's Matter launch · [news.ycombinator.com/item?id=45836140](https://news.ycombinator.com/item?id=45836140) · posted 2025-11-06 · **[RAW]** · *brand-level rejection of the category word itself*

### The recurring idioms — the part that matters more than any single quote

Ranked by cross-user, cross-platform recurrence. *(FACT that each phrase appears in the cited sources; prevalence ranking is INFERENCE, MED-HIGH.)*

1. **"silently."** The category's own native word for the disease, reached for unprompted: *"devices silently go down," "it often silently go unresponse."* **(HIGH)**
2. **The `says X / is Y` inversion.** The dominant *grammatical shape* of the complaint, identical across every platform: *"shows off but it is clearly on"* · *"a light will be off but the dashboard… will show that it is on"* · *"HA reports all lights as off, but random lights remain on"* · *"in real life the lights are turned on… but in HA the state… hang in the old state."* **This construction is the single most reusable copy asset in this return.** **(HIGH)**
3. **Frozen-value vocabulary:** *"stucked at"* · *"hang in the old state"* · *"fixed for the last 144 hours"* · *"show 40% forever."* Note that users volunteer **specific hour-counts** — the duration is part of the injury. **(HIGH)**
4. **"I'm not even sure when or how" / "to this day I do not know" / "no trace of it" / "no errors being logged."** The no-evidence idiom. **The complaint is not that it broke — it is that there is no record that it broke.** **(HIGH)**
5. **"It says WHEN, not WHY."** Phrased almost identically by different users four years apart (AndyMack 2024, FutureTense 2020). **(HIGH)**
6. **"The trace is already gone."** Five independent statements, three platforms, five years (jarrah 2021 · Vitaliy Kh 2022 · Tmjpugh 2024 · alander 2024 · Steve Dinn 2025). Retention is a *recognised, unaddressed* wound. **(HIGH)**
7. **Users write the missing error message themselves.** Three independent users draft the string the system should have shown, in quotes: *"25 instances of this automation are already queued. The queue is full."* · *"device XXX has been turned on by YYY."* **This is the product being specified in the customer's own words — treat it as copy, not as a feature request.** **(HIGH)**
8. **"just quit working" / "worked for literally a year with NO problems" / "This has worked for years but not now."** The *I-changed-nothing* frame; near-universal opener in Cluster B. **(HIGH)**
9. **"brick" / "bricked"** — the universal verb, used reflexively: *"my dropcam is just going to brick itself."* The device is framed as the agent of its own death. **(HIGH)**
10. **"a feature you paid for… and it's gone"** → *"reneging on their side of the deal," "return the money that they took."* Sunset framed as **theft**. **(HIGH)**
11. **"'Local' is misleading."** The badge-vs-reality gap, stated by users on HA, SmartThings and Hubitat. **(HIGH)**
12. **Outage → purchase.** Cloud failures named directly as the trigger for buying a competing local hub. **(HIGH)**
13. **The spouse as escalation vector.** *"have the wife call and say lights wont turn on."* Reliability failures are **socially** costly, not merely technically annoying. **(MED)**
14. **Platform dialects for the same wound:** HA `unavailable` · Hubitat `offline` / `out of sync` · SmartThings `not responding` · Homey `unreachable`. **INFERENCE (MED): copy should use plain English — "dead," and "is it actually alive" — because those cross all four dialects** (see the HA thread literally titled *Request: Notification on "dead" devices*).

**The single most important structural observation (INFERENCE, HIGH):** Clusters A and B **are not separable in the source material.** The Hubitat `bill` quote and the `axsdenied` thread both show an availability lie *causing* a silent automation failure, and Keo's *"We aren't seeing any issues"* shows opacity converting a reliability problem into a trust problem. **Users experience this as one disease with three symptoms, not three problems.** Marketing that splits them into three feature bullets will describe something users do not recognise; marketing that names the causal chain will.

---

## §3 — CATEGORY POSITIONING AUDIT

Every homepage below was opened 2026-07-31.

**Home Assistant** — [home-assistant.io](https://www.home-assistant.io/). *"Awaken your home"* / *"Open source home automation that puts local control and privacy first. Powered by a worldwide community of tinkerers and DIY enthusiasts."* Leads with: 1000+ brands · powerful automations · versatile dashboards · Assist voice · *"All your smart home data stays local."* **Axis:** local control + privacy, then breadth. **Audience:** self-selected — *"tinkerers and DIY enthusiasts."* **FACT (HIGH): the word "reliable" does not appear in the returned homepage copy, and traces/debugging are not among the five features it leads with.**

**Open Home Foundation** (governs HA, ESPHome, Music Assistant) — [openhomefoundation.org](https://www.openhomefoundation.org/): *"fights for the fundamental principles of privacy, choice, and sustainability for smart homes."* Corroborated by the 2021-12-23 manifesto ([source](https://www.home-assistant.io/blog/2021/12/23/the-open-home/)).

> **INFERENCE (HIGH) — the most important structural finding in this section.** The category's ideological centre is a **three-legged stool — privacy, choice, sustainability — with no leg for reliability, correctness, or truthfulness of what the system reports.** This is not one company's copy oversight; it is the stated value system of the foundation governing the category leader.

**Nabu Casa** — [nabucasa.com](https://www.nabucasa.com/). *"Get the best extras for Home Assistant while supporting its development."* · *"Not even Nabu Casa can see your smart home data."* · *"Keep your smart home running without a hitch"* — **scoped to backups, not runtime behaviour.** **Axis:** privacy-preserving convenience; monetization framed as patronage.

**Homey** — [homey.app](https://homey.app/en-us/). *"Control, automate and monitor your entire smart home in one app"* / *"the world's most easy to use, privacy-first smart home platform."* **Axis: ease of use, first and loudest**; privacy is a compound modifier, not an argument. Note "monitor" in the headline verb list — but it means dashboards, not verification. **Homey Pro** ([page](https://homey.app/en-us/homey-pro/)): *"runs entirely on-premise, ensuring minimal latency and maximum reliability"* · *"Always up — even when your internet is down."*

**Hubitat** — [hubitat.com](https://hubitat.com/). *"Home Automation, the Way It Is Meant To Be."* Bullets: *"CloudFree: Your automations execute on your hub, not in the cloud"* · *"Local Processing: Experience private and reliable home automation with local processing"* · Privacy. Closing line: ***"A smart home is more than controlling lights with an app. It's about devices that do what they should do."*** **Axis:** local processing as master claim; privacy/speed/reliability all derived from it.

> **OPINION (HIGH).** *"Devices that do what they should do"* is the closest any incumbent comes to gesturing at correctness — and it is a **closing throwaway about the devices**, not about the hub's own truthfulness. It promises the devices behave. It promises nothing about the system telling you whether they did.

**SmartThings** — smartthings.com now **302-redirects** to [samsung.com/us/smartthings](https://www.samsung.com/us/smartthings). Hero: *"Your home saves energy."* Sections: "Experience AI Living," "Home Insight," "Home Routine," "Manage energy usage with AI." **Axis:** ecosystem breadth + ease + energy + AI, funnelling to Samsung hardware. **FACT (MED — heavy-JS page, extraction may be partial):** among the target words *reliable / reliability / trust / secure*, the only hit was **"seamless."**

**openHAB** — [openhab.org](https://www.openhab.org/). *"empowering the smart home"* / *"vendor and technology agnostic."* Sections: Integrate Everything (400+ technologies) · *"No Cloud Required… but Cloud-Friendly."* **Axis:** vendor neutrality above all. No reliability claim.

**HomeSeer** — [homeseer.com](https://homeseer.com/). Rotating headline: *"Smart Home Living Made Affordable / Convenient / Efficient / **Reliable**."* Plus *"Locally Managed: Your automations run faster and more reliably with no cloud needed"* and "25 years of trusted, local expertise." **This is the cleanest specimen of reliability-as-decoration in the category — the word is one interchangeable item in a CSS text rotator, cycling with "Affordable."**

**Newcomer — One Raven (the significant one).** **FACT (HIGH).** Launched **2026-07-07** — three weeks before this return — with a **$5M seed led by Fifth Wall**. Release headline: ***"One Raven Launches to Take the Smart Home out of the Cloud"***; subhead promises *"no pairing, no subscriptions, and no external data collection."* Founder (Sarah Roudybush): *"The first generation of the smart home asked homeowners to send their data to the cloud and pay monthly fees for features they already owned. We don't think any of that is necessary."* Rallying line: *"Your home is yours. Your data should be too."* Sold B2B2C through homebuilders. [PR Newswire](https://www.prnewswire.com/news-releases/one-raven-launches-to-take-the-smart-home-out-of-the-cloud-302819562.html) · [HousingWire](https://www.housingwire.com/articles/local-first-smart-home-platform-homebuilders/). **FACT (MED — absence): no claims about state accuracy, verification, responsiveness, or explainability anywhere in the launch materials.** *(Gap: oneraven.com itself is a client-rendered SPA and could not be read; homepage copy may differ from the PR.)*

**Newcomer — SwitchBot AI Hub.** ~$259.99, covered [2026-01-22](https://homekitnews.com/2026/01/22/switchbot-launches-its-ai-centric-matter-home-hub/): on-device VLM, *"local automation and device management even in the absence of cloud connectivity."* **Axis:** local AI + privacy. No explainability claim.

### Where reliability/truth actually stands — the verdict

**Three tiers, and the distinction is commercially load-bearing.**

**Tier 1 — Uptime-reliability: CLAIMED, but only as a derivative of local processing, never as a headline. (FACT, HIGH)** Hubitat, Homey Pro and HomeSeer all use the word; in **every** case reliability is the *effect* and local processing is the *cause*, and the claim reduces to *"it keeps working when your internet is down, and it responds faster."* **INFERENCE (HIGH): this is an *availability* claim, not a *correctness* claim — and it is structurally unownable, because it belongs to the entire local-first camp collectively. It is also unfalsifiable as marketed: no vendor publishes a mechanism, a metric, or a guarantee behind the word.**

**Tier 2 — Reliability as pure adjective: HomeSeer.** Textbook claimed-but-unproven.

**Tier 3 — Truth-reliability ("what the system tells you is actually true"): UNCLAIMED. Completely. (FACT, MED — absence-of-evidence, capped per §0.)** Across **ten properties opened 2026-07-31** — home-assistant.io, nabucasa.com, homey.app (home + Pro + Advanced Flow), hubitat.com (home + products), samsung.com/us/smartthings, openhab.org, homeseer.com, One Raven's launch materials, openhomefoundation.org — **not one** claims that reported device state is verified rather than assumed; that a command was confirmed to have taken effect; that the system will tell you when it *doesn't know*; or that stale data is surfaced rather than silently rendered as an "off" icon. *Searched to establish this: the ten properties above plus targeted queries on "did it actually," "confirm the command," "device state truth," "dependable automations." All returned SEO listicles and market-research reports — zero vendor positioning.*

> **The sharpest single exhibit in this return (FACT, HIGH).** Home Assistant release 2026.7 ([blog, source date 2026-07-01](https://www.home-assistant.io/blog/2026/07/01/release-20267/)) states verbatim:
>
> **"With these new triggers, you don't need to care about `unknown` or `unavailable` states."**
>
> **INFERENCE (HIGH): the category leader's 2026 strategy for state uncertainty is to *hide it* so users need not think about it — the precise inverse of owning truthfulness.** Read alongside HA lead Franck's stated 2026 direction, *"We really want to lower the floor without lowering the ceiling"* ([State of the Open Home 2026](https://www.openhomefoundation.org/blog/building-whats-next-state-of-the-open-home-2026/), source date 2026-04-10), the incumbent is committed to **simplification**, which structurally opens the flank on **verifiability**.

**OPINION (HIGH).** The privacy/local-control axis is saturated past the point of differentiating: Home Assistant, Homey, Hubitat, openHAB, HomeSeer, One Raven and SwitchBot all now say a version of it — and **One Raven raised $5M in July 2026 on a pitch that is, in message terms, indistinguishable from Hubitat's 2018 pitch.** Truth-reliability is the only major axis in this category with **no incumbent occupant and no incumbent claim to dislodge.**

---

## §4 — EXPLAINABILITY PRIOR ART IN MARKETING

**Headline answer: the language exists inside this category — but only in engineering documentation and a five-year-old release note. It has never been elevated to marketing. One category over, it is a successful headline claim.**

**Exhibit 1 — HA traces: the exact words, in 2021, then abandoned to the archive. (FACT, HIGH)** The [2021-04-07 release blog](https://www.home-assistant.io/blog/2021/04/07/release-20214/) opens, verbatim:

> **"Wait, why didn't that light turn on? Why isn't the thermostat adjusted? Why is this automation not working?"**

and: *"If an automation didn't run as it should, this will allow you to debug and understand why it ran the way it did."* Extended to scripts [2021-07-07](https://www.home-assistant.io/blog/2021/07/07/release-20217/): *"why didn't that script work? Or why did it behave as it did?"*

**But it stayed in the release note. (FACT, HIGH)** The homepage leads with five features and traces are not among them. The [troubleshooting docs](https://www.home-assistant.io/docs/automation/troubleshooting/) are purely procedural ("Go to Settings," "Select Traces") with zero persuasive framing. And retention is capped: **"The last 5 traces are recorded for all automations."**

> **INFERENCE (HIGH): a 5-run buffer is a debugging aid for a developer reproducing a fault on demand. It cannot answer "why did the lights do that last Tuesday" — which is the actual homeowner question. This is a *tool*, not a *system of record*.** §2 idiom #6 shows five independent users hitting exactly this wall over five years.

**Exhibit 2 — HA 2026.7 "Activity logbook": the closest current move, one month old. (FACT, HIGH)** [Release blog, 2026-07-01](https://www.home-assistant.io/blog/2026/07/01/release-20267/), verbatim: ***"It shows the cause.** When something was set in motion by a person, you see their avatar. An automation shows what triggered it… **The 'why' sits right next to the 'what'."*** **INFERENCE (HIGH):** real causal attribution presented as a user benefit — but scoped to *what triggered a change that did happen*, published in a monthly release post rather than on any marketing surface, and doing nothing for the two harder questions: **why it did NOT fire**, and **whether the command actually took effect.**

**Exhibit 3 — Homey: absent. (FACT, HIGH / MED on absence)** [Advanced Flow page](https://homey.app/en-us/features/advanced-flow/): *"Advanced Flow. Simple yet powerful."* No mention of debugging, testing, execution feedback, or understanding why a flow ran or failed. Searches surfaced **only community forum threads** — "Advanced flows debugging," "How to debug flow(s)?", "Advanced Flow Working in Test State But Failing Once Saved" — i.e. visible unmet demand with no product claim. *(Gap: Homey's changelog renders via JS and could not be read; a 2025–2026 Homey debugging feature cannot be fully ruled out. This is the largest genuine hole in the absence claim.)*

**Exhibit 4 — Hubitat: documented, and explicitly disclaimed for troubleshooting. (FACT, HIGH)** [App Status docs](https://docs2.hubitat.com/en/user-interface/apps/app-status): *"detailed, read-only information about the internal data values of an app"* — and — *"This page is generally most useful for app developers or advanced users and **typically not useful for general troubleshooting**."* Nothing on hubitat.com. A community thread titled *"Hubitat Needs Better Logging for Easier Troubleshooting"* exists.

**Exhibit 5 — SmartThings, openHAB, Domoticz, One Raven, SwitchBot: absent. (FACT, MED — absence)** None of the retrieved copy contains explainability, causal-attribution or command-verification claims. **The best-funded 2026 entrant, three weeks old, makes no claim about knowing what the system is doing.**

**Exhibit 6 — the adjacent proof that this SELLS: n8n. (FACT, HIGH)** [n8n.io](https://n8n.io/) headline: ***"AI agents and workflows you can see and control."*** Lead: *"Every step of your agents' reasoning, traceable on the canvas."* Supporting: *"Inspect every decision"* · *"See the inputs and outputs right next to the settings of every step"* · *"Avoid endless debugging clicks with the logs view."* **INFERENCE (HIGH): n8n has made observability-of-automation-logic its *primary headline positioning* — not a feature bullet — in a category structurally analogous to home automation (event-triggered, multi-step, integration-dependent workflows). "You can see why it did what it did" is a proven top-line commercial claim.**

**Exhibit 7 — Honeycomb, on making the claim falsifiable. (FACT, HIGH)** [honeycomb.io](https://www.honeycomb.io/): *"Perform root cause analysis in under three minutes with BubbleUp."* Root-cause explanation marketed with a **named mechanism** and a **time bound** — precisely what the smart-home "reliable" adjectives lack.

**Correction to the brief's hypothesis (MED-HIGH).** Industrial SCADA is a **weak** analogy. [Inductive Automation's Ignition](https://inductiveautomation.com/ignition/) leads with *"The Unlimited Platform for Enterprise Integration"* — licensing/scale economics, not explainability. **The useful adjacent vocabulary lives in workflow automation and observability, not industrial control.**

### §4 verdict

**INFERENCE (MED, per absence rules): no smart-home platform — incumbent or 2025–2026 newcomer — markets the ability to know why an automation fired, why it didn't, or whether a command took effect.** The absence is broad, current, and holds through the newest and best-funded entrant.

**OPINION (MED-HIGH) — and this is the risk worth naming: the competitive threat is not that someone owns this position. It is that Home Assistant already ships most of the technology and wrote the perfect problem statement in 2021, and could claim the position in a single release cycle.** The defensible version is therefore **not "we have traces"** — HA has traces. It is the three things HA structurally does not do, all three of which §2 shows users bleeding over:

1. **Retention beyond five runs** (idiom #6 — five users, three platforms, five years)
2. **Negative explanation** — why it did **not** fire (Cluster B; HA 2026.7 explicitly does not address it)
3. **Command confirmation** — did the device actually do it (the `alpacalypse` and `marcelveldt` quotes; HA's own core developer names optimistic state as an open problem)

---

## §5 — THE LAUNCH CHANNEL MAP

### 5.1 Hacker News — the primary channel, with a counter-intuitive shape

**Show HN rules (FACT, HIGH — [showhn.html](https://news.ycombinator.com/showhn.html)):** must be *"something you've made that other people can play with"*; blog posts and sign-up pages are **not eligible**; new features/upgrades *"generally aren't substantive enough"*; must be *"something you've worked on personally and which you're around to discuss"*; make it *"easy for users to try your thing out, ideally without barriers such as signups or emails."*

**Category Show HN performance band, 2023–2026 (FACT, HIGH — all Algolia-confirmed):**

| Post | Points | Comments | Date |
|---|---|---|---|
| Micasa – track your house from the terminal | **657** | 218 | 2026-02-19 |
| Willow – Open-source privacy-focused voice assistant hardware | **581** | 138 | 2023-05-15 |
| Pila – Plug-in Home Battery for the 99.7% | **301** | 480 | 2025-03-11 |
| ESPectre – Motion detection via Wi-Fi spectre analysis | **215** | 50 | 2025-11-17 |
| Lightwhale – home server OS | **194** | 91 | 2026-04-24 |
| CheapSecurity – Self-Hosted CCTV for Linux SBCs | **138** | 37–47 | 2026-07-26 |
| Secluso – Open-source private home security camera | **137** | 27 | 2026-05-29 |
| Tommy – ESP32 through-wall motion sensors *(commercial)* | **110** | 80 | 2025-10-23 |

**The counter-intuitive part (FACT, HIGH).** The biggest numbers in this category are **not launches** — they are cloud-betrayal stories:

- Bose opens API for EoL SoundTouch speakers — **2532 / 396** (2026-01-08)
- HA blocked from Garage Door opener API (MyQ) — **1181 / 640** (2023-11-08)
- The era of open voice assistants (HA Voice PE) — **931 / 278** (2024-12-20)
- Frigate: Open-source NVR with real-time AI — **625 / 140** (2023-11-18)
- Immich – self-hosted photo management — **565 / 205** (2025-09-08)
- VW blocks Home Assistant — **392 / 190** (2026-05-29)

> **INFERENCE (HIGH): HN's attention engine in this category is *cloud betrayal and platform erosion*, not novelty.** A vendor killing an integration reliably outscores any Show HN by 2–8×. The practical Show HN ceiling here is ~200–660; the 900–2500 band belongs to grievance stories. **This is the same emotional vein §2 Cluster D documents — the channel and the phrase bank agree.**

**INFERENCE (MED): HN is an amplifier, not an origin.** ESPectre had *"almost 2,000 stars in two weeks"* **before** its Show HN (author's own submission text). Frigate's 602-point 2025 moment was a **stranger reposting the homepage** with no maintainer participation.

### 5.2 YouTube — two distinct audiences, not one

All subscriber figures are **Social Blade's**, accessed 2026-07-31 (rounded; not YouTube-native).

**Smart-home reviewer tier (device-centric):** **The Hook Up** (@thehookup) — **577K** subs, 78.2M views, 286 videos, since 2018 — deep technical testing/teardowns · **Everything Smart Home** — **246K** subs, 29.0M views · **digiblur DIY** — **74.3K** subs, 12.8M views, 462 videos, active (2 videos in the last 14 days) — de-clouding/flashing (Tasmota/ESPHome).

**Homelab / self-host tier (infrastructure-centric):** **Jeff Geerling** — **1.08M** subs, 206M views (~628K views in 14 days) — largest single lever found · **Hardware Haven** — **462K** subs, +3K subs and ~796K views in 14 days — fastest-growing · **Techno Tim** — **333K** subs · **DB Tech** — **108K** subs, 709 videos — highest cadence, most launch-shaped format (per-app install/review).

**The community's own canonical roster (FACT, HIGH)** — [frenck/awesome-home-assistant](https://github.com/frenck/awesome-home-assistant), explicitly *"sorted by subscribers"*: Home Assistant (official) → The Hook Up → Everything Smart Home → Home Automation Guy → Smart Home Junkie → digiblurDIY → Intermit.Tech → BeardedTinker → JuanMTech → mostlychris → KPeyanski → This Smart House → SlackerLabs → Michael Leen → Technithusiast → Frenck. Non-English: simon42, haus:automation (DE) · AyLabs (FR) · DinamoTech (IT) · Tecnoyfoto (ES) · Descomplicando Tech (PT-BR).

**INFERENCE (MED): the two tiers barely overlap in format, and a local-first home product needs both.**

### 5.3 The channels that are NOT what you'd assume

**Product Hunt is a vanity checkbox here. (FACT, HIGH → INFERENCE, HIGH.)** [Home Assistant on PH](https://www.producthunt.com/products/home-assistant) has **232 followers and 3 reviews total.** Its flagship [Voice PE launch](https://www.producthunt.com/products/home-assistant/launches/home-assistant-voice) got **197 upvotes and 4 comments** (#5 of the day, 2024-12-22) — versus **931 points and 278 comments on HN three days earlier.** ≈4.7× the points and **70× the discussion** in HN's favour.

**The Self-Hosted podcast (Jupiter Broadcasting) HAS ENDED. (FACT, HIGH)** [Episode 150, "The Last One," 2025-05-30](https://selfhosted.show/150). **Anyone planning from pre-2025 knowledge will pitch a dead show.**

**selfh.st is the most launch-shaped dedicated channel that could be verified. (FACT, HIGH)** [selfh.st](https://selfh.st/) — weekly Friday newsletter + aggregator, self-reported *"Join 30,000+ readers,"* latest issues 2026-07-31 / 07-24 / 07-17.

**Home Assistant Podcast — very active. (FACT, HIGH)** [hasspodcast.io](https://hasspodcast.io/) — Phil Hawthorne + Rohan Karamandi, **291+ episodes**, most recent 3 days before access; guest-interview format (45–70 min) plus monthly release breakdowns.

**HA community forum — a compounding channel, not a spike channel. (FACT, HIGH)** [Share your Projects!](https://community.home-assistant.io/c/projects/9) — verified long-tail: Local Tuya 356 replies / **75,358 views** · "Claude Code for Home Assistant" 95 / **41,804** · Lovelace Windrose Card 350 / **41,479**. New posts sit at 8–270 views. **Threads accumulate tens of thousands of views over months.** It also feeds HN: a forum thread *"My Journey to a reliable locally hosted voice assistant"* hit HN at **425 / 140** (2026-03-16).

**Lemmy — real but secondary. (FACT, HIGH)** [lemmy.world/c/selfhosted](https://lemmy.world/c/selfhosted) — **60.3K subscribers**, 763 users/day, recent post scores 74–262. **Its self-promo rule is published and FLOSS-permissive** (promotion requires 30+ day accounts with active participation, with FLOSS exceptions) — notable precisely because Reddit's equivalent rules could not be read.

**Subreddits — RULES NOT VERIFIED (see §0-COMPLIANCE (a)).** Zero verified self-promotion rules for r/homeassistant, r/homeautomation, r/selfhosted, r/homelab, r/smarthome. SEO blog summaries of those rules were deliberately **not** laundered as citations. Reddit→HN spillover is nonetheless evidenced: r/selfhosted *"Large US company came after me for releasing a free open-source alternative"* → HN **120 / 20** (2026-02-22); r/homeassistant LoRa-over-grid-down post → HN **99 / 10** (2026-02-19).

### 5.4 Three worked examples

**A — Home Assistant Voice Preview Edition** (big-org hardware). $59 open-hardware voice assistant, announced **2024-12-19** on [the HA blog](https://www.home-assistant.io/blog/2024/12/19/voice-preview-edition-the-era-of-open-voice/), **sold immediately — not a preorder.** Channel order: own blog → HN (Dec 20, **submitted by a community member, `_Microft`, not the company**) → PH (Dec 22). **Reception: HN [931 points / 278 comments](https://news.ycombinator.com/item?id=42467194); PH 197 upvotes / 4 comments, #5 of day.** Founder `balloob` engaged in the HN thread. **INFERENCE (HIGH) — what worked:** in stock at announcement; a hard cheap memorable price; the post is an *ideological* claim (*"the era of open voice"*) not a spec sheet; and the company **did not submit it themselves** — which removes the self-promo smell while the founder still shows up to answer.

**B — ESPectre** (solo-dev OSS, HA-native). Wi-Fi CSI motion detection on a bare ESP32, GPLv3. Repo first → Show HN **2025-11-17** at **[215 points / 50 comments](https://news.ycombinator.com/item?id=45953977)**, author engaged throughout. Author's in-thread claim: *"almost 2,000 stars in two weeks."* [Repo today](https://github.com/francescopace/espectre): **7.3k stars, 576 forks**, latest release v2.7.0 (2026-03-17). **Direct comparator:** the commercial equivalent **Tommy** got **110 / 80** one month earlier — **the GPL project got ~2× the points on the same idea.** **INFERENCE (HIGH) — what worked:** anti-hype technical claims up front (*"does NOT use Machine Learning, it relies purely on Math"*); a cheap already-owned substrate so trying it costs ~$5 (satisfying the Show HN "easy to try" rule); **"Home Assistant integration" named in the description — that phrase is the category's distribution keyword**; and stars *before* HN, so the thread met a live project, not a launch page.

**C — Pila Energy** (indie hardware, closed, paid — **the cautionary one**). 1.6 kWh plug-in home battery, Show HN **2025-03-11** at **[301 points / 480 comments](https://news.ycombinator.com/item?id=43333661)**. **Comments exceed points by 1.6× — the signature of a contested thread, not an enthusiastic one.** Three team members engaged. Pricing ($999 preorder / $1,299 regular) disclosed **only in comments**; the thread contained **astroturfing allegations and criticism of misleading marketing claims.** Shipping announced [2026-06-17](https://www.pilaenergy.com/blogs/updates/pila-is-shipping) — **~15 months after the Show HN**, with no unit numbers disclosed. **INFERENCE (MED-HIGH):** the *"for the 99.7% of us without Powerwalls"* framing is the strongest constituency line in the dataset and probably earned the 301 points — but closed hardware + a landing-page URL + preorder pricing put the thread into adversarial mode. **480 comments of the audience litigating your product is not distribution.**

### 5.5 Format intelligence

1. **Title patterns that carried.** *Mechanism-forward* beat product-forward on the same idea (ESPectre 215 vs Tommy 110). *Constituency-forward* — *"for the 99.7% of us without Powerwalls"* — names who the incumbent excludes. *Concrete verb + artifact* — *"track your house from the terminal"* — is the highest scorer in the set (657). **The adjective stack does load-bearing work in the title itself: open-source / self-hosted / local-first / private / no cloud.**
2. **Founder-in-comments is near-universal among winners (FACT, HIGH).** Verified in Willow, ESPectre, Pila, Micasa, Secluso. The two exceptions (CheapSecurity 138, the Frigate repost 602) succeeded on submission quality alone.
3. **Repo-as-URL beats landing-page-as-URL (INFERENCE, MED-HIGH).** Every high scorer submitted a GitHub URL. The two landing-page submissions produced the most hostile thread (Pila) and the lowest score (Tommy).
4. **Open source is a scoring multiplier here, not a neutral choice (INFERENCE, HIGH).** Same idea, same month, same substrate: GPLv3 215 vs commercial 110.
5. **Pricing transparency defuses; preorders detonate (INFERENCE, MED).** $59-in-stock-stated-upfront → 931 points, celebratory. $999-preorder-disclosed-in-comments → 480 comments including astroturf accusations. **The clearest paired contrast in the dataset.**
6. **"No cloud, no account, no subscription" appears verbatim in the top home-category Show HN** (Micasa, 657 points). **Treat it as the category's canonical value-proposition sentence.**
7. **Ship the artifact before the announcement (INFERENCE, HIGH).** ESPectre had 2,000 stars pre-HN; HA Voice PE was purchasable the same hour; Micasa had a runnable demo mode. Pila had a preorder and a 15-month wait.
8. **The recurring sequence (INFERENCE, MED):** artifact/repo → HN (ideally submitted by a community member) → Reddit/Lemmy spillover → selfh.st weekly → YouTube reviewer pickup weeks later (the long-tail driver) → HA forum thread that accrues views for years. **Product Hunt sits outside this chain and contributes almost nothing.**

---

## §6 — WHAT CHANGES OUR PLANS

Seven findings. Each is one sentence plus its evidence pointer.

**6.1 — The name moved but the artifact strings did not, and the legacy ones are worse than "stale" — they are actively occupied.**
`homesynapse.com` is a third party's live countdown page under a HomeSynapse logo, `github.com/homesynapse` is taken, `github.com/nexsys` is taken, and "Synapse" already means the Matrix homeserver to the exact HN/self-hosted audience §5 identifies as our launch channel — so **the deferred Java-namespace/repo-naming decision (decision package Deliverable 4 row 6) is no longer deferrable past G-2**, because `homesynapse-core` as a public repo URL ships the collision on launch day in front of the one audience certain to notice. → *§1 table rows 1–3; §5.1.*

**6.2 — NexSys is dead on a Class-009 knockout, which retires the fallback branch and confirms the ruled architecture at zero cost.**
Two live renewed **Class 009** US registrations — EnerSys/EH Europe Reg. 3952639 (batteries) and Lakewood Instruments Reg. 4650236 (*programmable electronic controllers*) — plus a globally marketed `NexSys®` line and a Rocket Companies subsidiary mean **no branch of the G-2 map should ever route back to NexSys**, and Architecture C's collapse to one consumer mark is independently vindicated. → *§1.1 rows 8–15; §1.2.*

**6.3 — The positioning lane we are aiming at is not merely unclaimed; the category leader has publicly committed to the opposite, and that is a stronger position than "unclaimed."**
Home Assistant 2026.7 states verbatim *"you don't need to care about `unknown` or `unavailable` states"* while the Open Home Foundation's stated values are **privacy, choice, sustainability — with no leg for truth** — so an evidence-based-availability claim does not compete with an existing claim, it **contradicts the leader's stated design philosophy**, which is both more defensible and more newsworthy. → *§3 Tier-3 verdict; [HA 2026.7](https://www.home-assistant.io/blog/2026/07/01/release-20267/); [openhomefoundation.org](https://www.openhomefoundation.org/).*

**6.4 — Do NOT position on privacy or local-first; that axis is saturated to worthlessness, as a $5M seed round three weeks ago just demonstrated.**
One Raven launched 2026-07-07 on *"Take the Smart Home out of the Cloud" / "no subscriptions, no external data collection"* — a message indistinguishable from Hubitat's 2018 pitch — while every incumbent says a version of it, so **every sentence of launch copy spent on privacy/local is a sentence spent on the one thing that cannot differentiate us.** → *§3 One Raven block; §3 OPINION (HIGH).*

**6.5 — The three defensible claims are precisely the three HA structurally cannot make, and the phrase bank supplies the exact words for each.**
HA already owns traces and wrote the perfect problem statement in 2021 (*"Wait, why didn't that light turn on?"*) but caps retention at **five runs**, offers **no negative explanation**, and has its own core developer naming **optimistic state** as an open problem — so the ownable trio is **retention · why-it-did-NOT-fire · did-the-command-actually-confirm**, and the copy should use the users' own construction: **"says X / is Y"** (*"shows off but it is clearly on"*). → *§4 verdict; §2 idioms #2, #6, #7; §2 quotes `alpacalypse`, `marcelveldt`.*

**6.6 — Launch on HN with a repo URL and a grievance frame, not a landing page and a product frame — and let someone else submit it.**
The category's 900–2500-point band belongs to cloud-betrayal stories (Bose 2532, MyQ 1181) not launches; open source scored 2× closed on the identical idea (ESPectre 215 vs Tommy 110); the two landing-page submissions produced the most hostile thread and the lowest score; and the highest-scoring launch in the set was **submitted by a community member while the founder answered in comments** — so the launch shape is: **artifact shipped and runnable first → community-submitted Show HN with a mechanism-forward title → selfh.st → YouTube reviewers weeks later**, with **Product Hunt dropped entirely** (197 upvotes / 4 comments vs 931 / 278 on the same product). → *§5.1, §5.3, §5.4 A–C, §5.5 items 2–8.*

**6.7 — Two research obligations this lane could not discharge, both of which should be fixed before the charter locks messaging.**
**Reddit was 100% blocked across four independent passes**, so the four subreddits the brief named contributed nothing to the phrase bank and **no subreddit self-promotion rule is verified** — meaning both the emotional register of §2 and the feasibility of the Reddit leg of §5 rest on unverified ground; separately, **every quote in §2 passed through an extraction model** and must be spot-checked against the rendered page before appearing on any public surface. → *§0-COMPLIANCE (a) and (b).*

---

## Appendix — what this lane could not reach

| Gap | Why | What would close it |
|---|---|---|
| **All of Reddit** (r/homeassistant, r/homeautomation, r/smartthings, r/hubitat, r/selfhosted) | `HTTP 403 PROXY_REJECTED` on every path, all four passes | A session with Reddit fetch permitted, or manual paste of ~10 thread bodies |
| **Subreddit self-promotion rules** | Same block; SEO summaries deliberately not laundered as citations | Same as above — load-bearing before any Reddit launch leg |
| **EUIPO / EU trademark** for both legacy names | eSearch not retrievable | Counsel's lane, or a manual EUIPO check |
| **`oneraven.com` homepage copy** | Client-rendered SPA; only PR copy obtained | Browser-rendered fetch |
| **Homey changelogs 2025–2026** | JS-rendered ("Loading…") | Browser-rendered fetch — **this is the biggest hole in the §4 absence claim** |
| **YouTube view counts / reviewer→launch attribution** | YouTube returns no metrics to this fetcher; RSS robots-disallowed | Subscriber counts are Social Blade's; no video-level data anywhere in §5 |
| **Lobsters** | robots.txt disallows `/search` and `/t/homeautomation` | Manual check |
| **Control4 / Savant (custom-install tier)** | Time-box | **Recommended highest-value follow-up** — plausibly the one segment already selling "the system tells you the truth" to integrators |
| **MacRumors / Universal Devices (Insteon 2022 shutdown) reaction threads** | No raw-text endpoint; ~14 candidate quotes discarded rather than risk paraphrase | Browser fetch — likely the richest untapped cloud-distrust corpus |
| **`homesynapse.com` and `github.com/homesynapse` ownership** | Cannot be determined externally | A one-minute registrar/GitHub dashboard glance by Nick |

---

*Lane discipline observed: one file written, nothing committed, no public surface touched, no candidate mark used publicly. Nothing in §1 is legal advice or clearance.*
