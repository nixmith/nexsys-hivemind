# Competitive Research — Automation Explainability UX

*How Home Assistant, Hubitat, SmartThings, openHAB, and Node-RED let users understand **why an automation did or didn't fire** — and where they fail. For: the HomeSynapse explainability hero-view design, the M7.2b retry-vs-confirmation decision (D2/REC-162), and the user interviews. Authored 2026-06-21.*

---

## TL;DR — the thesis

Every major platform fails at explainability in the **same five structural ways**, and HomeSynapse's architecture (immutable event log + per-run `RunCausalChain` + explanation-as-a-projection, Doc 16 / INV-SA-03) is positioned to solve exactly those failures. Two unmet needs dominate and **no platform answers either well**:

1. **"Why DIDN'T it fire?"** — every platform can sometimes show you what *did* happen; none cleanly distinguishes *condition-was-false* vs *trigger-never-matched* vs *device-didn't-act*. This is the canonical user complaint and it is wide open.
2. **"Did the device actually DO it?"** — every platform's trace records that the command was **sent** (the service call ran), not that the device **acted**. Optimistic state literally lies ("says on, but it's off"). The HA core team calls this "really bad UX" in their own words and hasn't solved it.

**Design the hero view around those two questions, in plain language, backed by the log + causal chain.** That is the differentiator, and the research says it is genuinely unoccupied territory.

---

## 1. The competitive landscape (what each platform actually offers)

**Home Assistant — the best-in-class trace, gated by structural limits.** Every automation run produces an interactive **trace**: a step graph of trigger→conditions→actions, with per-condition pass/fail showing actual-vs-wanted state, changed variables, and the config-at-runtime. Causality across entities is attributed via a **context** object (`context.id`/`parent_id` chaining) that powers the Logbook's "turned on, triggered by automation X." *But:* only the **last 5 traces** are kept (YAML-configurable, not via UI); a YAML automation produces **no trace without an `id`**; and **no trace exists at all if the trigger never fired** — so "didn't fire" is diagnosed by *absence*. (Sources: HA troubleshooting doc; Context doc.)

**Hubitat — local, transparent, but raw.** Explainability is a text **Logs** page (Live + Past) plus, per device, an **Events** page with a "Produced By" column that names the app that sent a command — the one clean "which automation commanded this device" signal in the field. Rule Machine offers opt-in Trigger/Event/Action logging (Action logging even logs *skipped* actions). *But:* logging is opt-in and ephemeral, there is **no visual step-trace and no unified cross-device timeline**, and reconstructing "what happened at 3pm" means reading each device's Events page by hand. Notably, Hubitat is the **only** platform with built-in closed-loop **Command Retry** (see §3).

**SmartThings — cloud, opaque, shallow.** End users get an in-app **History** feed; that's essentially it. Samsung **killed the Groovy IDE** (the power-user logging tool) in 2023 and replaced it with an Advanced Web App that **shipped without hub event logging**. Automations are split across surfaces — the AWA "Rules" tab only lists Routines; API-created Rules are invisible without a third-party token tool — producing **"ghost routines"** that run but can't be found, edited, or deleted. The real "why" lives in **server-side hub logs only Samsung staff can read**.

**openHAB — text logs only, hand-instrumented.** No visual trace; the documented debugging method is to **manually add `logInfo` lines and `grep` the log**. Even experienced programmers report feeling "completely blind," and experts disagree in-thread about whether `log:set` even works on rules — evidence of how opaque the model is.

**Node-RED — visual-flow-as-causality (the one bright spot).** Its defining advantage is stated as a design contract: *"if you can see the wires, you understand the flow."* The success path is literally drawn on the canvas; node **status dots** give at-a-glance state; the Debug sidebar inspects live messages. *But:* `catch`/`complete`/`status` are **invisible scope-based listeners** ("you can't trace errors visually"), Debug nodes are manual and capped at 100 messages, and large flows degrade into **"spaghetti."** The lesson for us: **visual causality is more legible than text logs at the core, but it must make the error/non-firing paths first-class and stay bounded** — exactly where Node-RED breaks.

---

## 2. The five universal failure modes (the design targets)

These recur across **all** platforms. Each is a HomeSynapse opportunity.

**FM-1 — Attribution gaps (silent blanks).** When the cause is outside the system or context isn't propagated, the platform shows a state change with **no "why."** HA examples: changes made outside HA, **context-less Sun/Time triggers** (effects show `parent_id: None`), **hub-mediated** changes (a Hue group switching its own bulbs happens "outside HA"), and **attribute-only** changes (brightness/color drift isn't logged at all). The honest answer ("the system doesn't know") is **indistinguishable in the UI from "nothing caused it."**
→ *HomeSynapse answer:* every state change is an event in the log with a causal chain or an explicit `external`/`unknown` origin — **never a silent blank.** This is INV-SA-03 (explanation is a pure projection of the log) made visible.

**FM-2 — Ephemeral traces (the run you need is gone).** HA's 5-trace cap silently evicts the misbehaving run — the canonical GitHub issue: "light comes on at 3am → I look at the traces → it just shows the last 5 minutes where nothing happened." Hubitat logs are opt-in and size-capped; SmartThings History is shallow.
→ *HomeSynapse answer:* the **immutable event log means the explanation is always reconstructable** — the trace is never evicted because it's a projection of durable events, not a capped ring buffer. **Structural advantage; lead with it.**

**FM-3 — Unreadable to non-experts.** HA's trace labels nested conditions by **index path** (`conditions/0/conditions/1/conditions/0/entity_id/0`) instead of the human condition; a professional developer called the trace "mostly useless… doesn't even fit the screen… you can't click what you can't see." openHAB needs hand-instrumentation; Hubitat needs cross-referencing. The community even normalizes it ("powerful tools require understanding") — which is itself the UX smell.
→ *HomeSynapse answer:* the hero view must read in **plain language** to a stranger: *"The hallway light turned on because the 'evening lights' automation fired, because the hallway motion sensor detected motion at 9:42pm."* Not index paths. **This is the mom-test bar.**

**FM-4 — Two tools, two causality models.** HA users bounce between the **trace** (an automation's *internal* logic) and the **Logbook** (cross-entity causality) because **no single view answers "why is this light on right now."**
→ *HomeSynapse answer:* **one** causal-chain view that runs *from the device state backward* through the run to the trigger — unifying the two models the others split.

**FM-5 — The "didn't fire" blind spot (the biggest gap).** No platform cleanly distinguishes the three reasons an automation didn't act: **(a)** a condition was false, **(b)** the trigger never matched, **(c)** it "fired" but the device didn't move. HA gives a partial trace for (a), *no* trace for (b), and a **misleading SUCCESS** trace for (c).
→ *HomeSynapse answer:* the **"why didn't it fire?"** view (Doc 16's `NonFiringExplanation`) is the hero's other half and the single most differentiated thing in this report. **Build it as a first-class peer to "why did it fire?", not an afterthought.**

---

## 3. Command reliability — the decisive M7.2b input (retry vs. confirmation, D2/REC-162)

This is the deepest trust hole **and** the input to the M7.2b action-model decision. The research is unusually decisive.

**The "says on, but it's off" problem is real, cross-platform, and the trace hides it.** HA's automation trace records that the command was **sent as a service call**, not that the device acted — the official doc's own debugging advice is to *bypass the trace* and watch the physical device. Optimistic / `assumed_state` integrations flip the UI on command **without confirmation**; when later polling reveals the truth, the correction logs **with no context, masquerading as an external change** (FM-1 again). Mechanical causes: Zigbee **message loss under concurrency** (a group-of-4 turn-on where the 4th throws `DeliveryError`), devices that **act but never report** state, and devices **going offline mid-automation** (which on SmartThings *silently skips the whole automation*).

**The three regimes, with field evidence:**

| Regime | What it does | Evidence | Failure |
|---|---|---|---|
| **Optimistic / fire-and-forget** | Flip UI state on send, no feedback | HA MQTT default when no `state_topic`; `assumed_state` | **Lies** when the command is lost; false voice confirmations |
| **Confirmed / closed-loop** | Trust only real device state | HA "source-based" mode; **Z-Wave Supervision CC** (device reports understood+executed, incl. "working"→"success") | Slower; **"flip-flop"** when feedback lags |
| **Retry** | Re-send on no-confirm | **Hubitat Command Retry** (≤5×, escalating backoff, idempotent classes only); HA users hand-roll `wait_for_trigger`+`repeat…until` | **Double-actuation** on momentary actuators |

**The load-bearing architectural finding: retry *requires* confirmation to be safe, and only for idempotent targets.** You can only safely retry when a feedback channel tells you the command didn't take — and Hubitat **explicitly warns** that retry is dangerous for garage doors/gates/valves (re-sending a toggle reverses the outcome), which is why their retry is **gated to switches/dimmers/locks/shades/thermostats** and **off by default**.

**Where the HA core team landed (architecture discussion #740):** keep **actual state authoritative** (don't overwrite it with an assumption), represent the in-flight command as a **separate, time-boxed "expected/pending" state**, surface it in the UI as **"working,"** and on timeout show an **error**. Their own words: *"the user has no visual indication that we're waiting for the device to process the command… imo this is really bad UX."* It's an acknowledged, unsolved gap at the top of the biggest platform.

**→ M7.2b recommendation (frames the deliberation; Nick rules):**
- **Keep the no-engine-retry default (REC-162 holds for V1).** Engine-default retry is the wrong default — it's unsafe without confirmation and on actuators, and the field evidence backs "don't auto-retry."
- **The differentiator is *visibility*, not retry.** Make the **command outcome first-class and visible**: `dispatched → confirmed | unconfirmed(timeout) | failed(reason)`. This is precisely the run-coupled-reliability terminal contract (Doc 16 §3.4: deterministic terminal + recorded reason) + the `PendingCommandLedger` (M7.3, command→`state_confirmed`). **No platform shows this; users desperately want it.** It's a near-free differentiator because the architecture already produces the data.
- **Defer retry to a post-MVP opt-in**, gated to idempotent device classes (adopt Hubitat's exact supported list) and **explicitly excluded for momentary actuators**. Do not pull it into V1.
- **Net for the demo:** "watch it fire, click 'why', and *see whether the light actually confirmed*" is a stronger hero than any competitor's trace, and it requires no retry engine — just making the confirmed/unconfirmed distinction legible.

---

## 4. Implications for the HomeSynapse hero view (actionable design principles)

1. **Two co-equal questions.** "Why **did** this fire?" *and* "Why **didn't** it?" as peer entry points. The second is the differentiator (FM-5).
2. **Plain-language causal chain, device-backward.** Start from the thing the user noticed ("the light is on") and walk back: state ← action ← run ← trigger ← event. Plain sentences, not index paths (FM-3, FM-4).
3. **Never a silent blank.** Every change is attributed or explicitly labeled `external`/`unknown`. Distinguish "we don't know" from "nothing caused it" (FM-1).
4. **Show command outcome, not just intent.** `confirmed | unconfirmed | failed(reason)` on every action — the trust win no one delivers (§3).
5. **Always reconstructable.** Lead on "the explanation is never evicted" — it's a projection of the durable log (FM-2, INV-SA-03).
6. **Borrow Node-RED's visual legibility, bounded.** A small visual chain per run reads better than text; keep it per-run (bounded), and make error/non-firing paths first-class (where Node-RED fails).
7. **Mom-test the language.** A stranger should read the explanation aloud and be right. That's the acceptance bar for the hero view.

---

## 5. Secondary findings

**Onboarding / pairing (feeds the Distribution first-run wizard).** Every canonical first-run device pain reduces to **hidden state the user can't see**: devices arrive **already bonded** (need exclusion/reset *before* inclusion), must be paired **within inches of the coordinator** then relocated, have **ambiguous pairing-mode ordering**, and fail with **opaque "interview failed / not found in inclusion mode" errors and no logs**. HA's own roadmap admits onboarding "can be drastically hindered by a few sub-optimal early decisions" and that only **46% of partners / 27% of children** interact with even a working HA install. → A guided wizard that (a) offers reset/exclusion first, (b) says "pair near the hub, then move it," (c) handles start-order, and (d) **surfaces interview progress + actionable errors** directly beats the field.

**Local-first positioning (validates the trust brand).** "Local control and privacy first" is HA's literal tagline — a *differentiator, not a feature*. The pitch that lands: **"your automations keep running with no internet, and no vendor can switch off the hub you own."** It has a built-in horror story — the **Wink** hub (sold with "no monthly fees") that gave owners **one week to pay $5/mo or be bricked** — and a live contrast in SmartThings cloud outages. **The honest counter-risk** is HA's own reputation for **breaking changes** (monthly cadence; a 2026.6 removal made affected automations **fail silently — still shown "enabled," never firing**). HomeSynapse can beat HA precisely on **long-term reliability / "your automations don't break on update"** — which ties straight into the Doc 16 reliability-as-a-product-property thesis.

---

## 6. Interview ammunition (pains to probe in the mom-test)

- "Has a light/device ever done something at the wrong time and you couldn't figure out **why**?" (FM-1/FM-5 — the "3am light" complaint is canonical.)
- "Has an automation **just stopped working** and you couldn't tell if it was broken or just not triggering?" (FM-5.)
- "Has your app ever said a device was **on when it was actually off**?" (§3 — near-universal.)
- "When you add a new device, how does **pairing** usually go?" (§5 — expect frustration stories.)
- "Does it matter to you whether your home **keeps working without internet**?" (§5 — local-first lever.)

---

## 7. Method, confidence, and sources

**Method:** five parallel search angles (HA; Hubitat+SmartThings; openHAB+Node-RED; command reliability; onboarding/local-first), official docs + community forums + GitHub, cross-checked for contradiction (none material). **Confidence: high** on the mechanism claims (official docs) and the recurring pain patterns (multiple independent community threads + GitHub issues). **Attributed-opinion** items: Node-RED's "see the wires" framing (a forum feature-pitch — mechanics accurate, slogan is one author's); HA's 46%/27% household stat (HA's own survey). **Caveat:** Reddit was unreachable (US-only search); equivalent first-person evidence was sourced from the official HA/Hubitat/SmartThings/openHAB Discourse forums and GitHub, which are higher-authority and quotable.

**Primary sources (priority):**
- HA automation trace/troubleshooting: https://www.home-assistant.io/docs/automation/troubleshooting/
- HA Context (parent_id chaining): https://data.home-assistant.io/docs/context/
- HA optimistic-vs-confirmed-vs-pending state debate (richest single source on the §3 tension): https://github.com/home-assistant/architecture/discussions/740
- HA `assumed_state` semantics: https://www.home-assistant.io/docs/configuration/state_object/
- HA "no built-in retry" + Z-Wave ACK-vs-apply + user closed-loop pattern: https://community.home-assistant.io/t/does-ha-know-if-a-zwave-command-wasnt-received-by-a-device/427283
- HA confirm-and-retry pattern (`wait_for_trigger`+`repeat…until`): https://community.home-assistant.io/t/confirm-zigbee-switch-automation-and-retry-every-x-min-on-fail/763641
- HA Zigbee group message-loss (`DeliveryError`): https://community.home-assistant.io/t/turning-lights-on-off-in-a-group-or-scene-doesnt-work-reliably/450913
- HA 5-trace eviction bug: https://github.com/home-assistant/core/issues/117133
- HA trace readability complaints: https://community.home-assistant.io/t/why-are-automation-traces-so-hard-to-read-or-even-not-readable/767431
- HA "what turned on my light / no context": https://community.home-assistant.io/t/wth-can-i-not-find-out-what-automation-or-action-just-turned-on-my-light/814755
- Hubitat Command Retry (the only built-in closed-loop retry; + actuator-safety warning): https://docs2.hubitat.com/en/user-interface/settings/command-retry
- Hubitat Logs + device Events ("Produced By"): https://docs2.hubitat.com/en/how-to/troubleshoot-apps-or-devices · https://docs2.hubitat.com/en/user-interface/devices/device-events
- Hubitat "current states wrong" (says on/is off): https://community.hubitat.com/t/hubitat-current-states-wrong/113032
- SmartThings AWA launched without hub logging: https://community.smartthings.com/t/new-advanced-user-app-for-smartthings-web/265581
- SmartThings "ghost routine" (runs but can't be found): https://community.smartthings.com/t/routine-runs-but-i-can-t-find-see-it-jan-2024/276429
- SmartThings outage — state wrong, history frozen, status page "operational": https://community.smartthings.com/t/devices-stopped-responding-26-march-2024/280222
- openHAB logging (text-only): https://www.openhab.org/docs/administration/logging.html
- openHAB "Why does this rule not fire?" / "completely blind": https://community.openhab.org/t/why-does-this-rule-not-fire/137336 · https://community.openhab.org/t/solved-ultimate-guide-to-debugging-rules/50921
- Node-RED "see the wires" + invisible error paths: https://discourse.nodered.org/t/explicit-error-complete-status-ports-making-node-reds-data-flow-honest/100935
- Node-RED Debug sidebar / handling errors: https://nodered.org/docs/user-guide/editor/sidebar/debug · https://nodered.org/docs/user-guide/handling-errors
- Z-Wave Supervision CC (protocol-native command-applied confirmation): https://docs.silabs.com/z-wave/latest/zwave-api/supervision
- HA onboarding roadmap + household-adoption stat: https://github.com/home-assistant/roadmap/issues/25 · https://www.home-assistant.io/blog/2025/05/09/roadmap-2025h1/
- Zigbee pairing proximity/interview-fail: https://github.com/Koenkk/zigbee2mqtt/issues/7762 · https://www.zigbee2mqtt.io/guide/faq/
- Z-Wave inclusion opaque failure: https://community.home-assistant.io/t/cant-add-a-z-wave-device-we-have-not-found-any-device-in-inclusion-mode/550331
- Local-first positioning + Wink shutdown precedent: https://github.com/home-assistant/core · https://9to5mac.com/2020/05/13/wink/
- HA breaking-change silent failure (2026.6): https://www.home-assistant.io/changelogs/core-2026.6/
