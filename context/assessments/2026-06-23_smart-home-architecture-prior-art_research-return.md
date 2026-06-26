# Prior-Art Architecture Study for HomeSynapse: Lessons from 15 Years of Smart-Home / IoT Platforms

## 1. Executive Summary

HomeSynapse's core architectural bets — local-first, event-sourced immutable log, deterministic no-autonomous-retry engine, and explainability-as-projection — are strongly validated by 15 years of prior art, but five specific decisions need correction or sharpening before MVP. The highest-leverage finding: **no existing mainstream platform can durably answer "why did this NOT fire?" — Home Assistant's traces are in-memory, default to only 5 per automation, are evicted, and are never created at all when a trigger fails to match.** This is HomeSynapse's single largest defensible differentiator, and the event-log-as-source-of-truth is exactly the substrate that makes it possible.

The 10 highest-confidence, highest-leverage lessons:

1. **The Recorder/history DB is Home Assistant's most documented scaling wall.** → HomeSynapse's "everything is a projection of the log" with retention/snapshot discipline is correct, but the log itself will hit the same wall without per-scope retention and projection pruning designed in now.
2. **SmartThings' Groovy→Edge forced migration broke users' setups and is the canonical anti-pattern.** → HomeSynapse's no-destructive-migration + immutable-log stance is validated; never deprecate a schema destructively.
3. **openHAB's rules-engine proliferation (DSL/JSR223/Blockly/JRuby) fragmented its community and docs.** → HomeSynapse's single component-based model (no templating DSL) is the right call; resist adding a second authoring paradigm.
4. **Event-sourcing's hardest pitfalls are schema versioning, projection-rebuild cost, and external side-effects on replay.** → HomeSynapse must version events additively (upcasting), keep command dispatch side-effects OUT of the replay path, and design snapshots now.
5. **Explainability prior art tops out at HA's ephemeral traces; nobody does non-firing or command-outcome honesty well.** → Lead with this; reserve nothing — build the "why-not" projection into MVP.
6. **Local-first is now a proven market value proposition (Hubitat, HA), not a niche.** → Validated; "local-first inviolate" is correct and increasingly demanded.
7. **Matter has under-delivered: version-mismatch fragmentation, multi-admin battery drain, slow platform adoption.** → Reserving Matter/Thread for post-MVP (Zigbee first) is the correct sequencing; don't bet the MVP on Matter.
8. **The Zigbee device-quirk long tail (Tuya/Xiaomi) is the dominant integration cost; Z2M/ZHA solved it with a community converter database.** → Don't build a bespoke quirk database from scratch; adapt the converter-database pattern and the ZNP/EZSP coordinator abstraction (which HomeSynapse already mirrors).
9. **AI-in-the-home is converging on a two-tier "deterministic-first, LLM-fallback" pattern (HA Assist) with planner/verifier/executor safety architecture from research.** → HomeSynapse's "AI proposes, the deterministic engine disposes" frame is exactly the emerging safety consensus.
10. **Regulation (EU CRA, UK PSTI, US Cyber Trust Mark) is making SBOM, secure-by-default, and vulnerability handling mandatory.** → HomeSynapse's security stance (auth-before-exposure, loopback-default, at-rest encryption) is ahead of the curve; reserve an SBOM/update seam now.

A cross-cutting caution: HomeSynapse's command-pipeline decision (Decision 1) should go **event-driven (executor emits `command_issued`, dispatch subscriber consumes, ordered via global log position)** because that is the only shape that scales additively to cross-process, multi-host, cloud, and AI consumption — which the system's own aspirations require.

## 2. Comparative Study

### 2.1 Home Assistant (deepest — closest comparable and main competitor)

**Core architecture.** HA's core is an in-memory **event bus** plus a **state machine** plus a **service (action) registry** (documented in HA core architecture docs and the `homeassistant/core.py` `StateMachine` class). Every entity produces `state_changed` events; the state machine holds exactly one immutable `State` object per entity and creates a new one on each change. The event loop is single-threaded asyncio — blocking it freezes the system. Entities → devices → areas/floors is the data model; integrations register via `config_flow` and receive the `hass` object.

**What worked.** The decoupled event-bus design is HA's enduring strength: integrations don't need to know about each other, automations subscribe to events, and the entity/area/floor model maps cleanly to natural-language addressing for voice. The `event` entity (added 2023.8) was a deliberate architecture-discussion outcome to stop "shoehorning every gizmo through a single pipe," improving automation authoring. Blueprints gave reusable parameterized automations. The integration ecosystem is the network-effect moat: HA supports **over 3,000 brands across roughly 2 million installations** — per the GitHub Blog (Dec 2025) quoting HA lead Franck Nijhof, who frames it as "We don't build Home Assistant, the community does."

**What failed / was regretted.**
- **The Recorder/history database is the single most-documented pain point.** HA records every state change by default to SQLite (`home-assistant_v2.db`); users routinely report databases of 7 GB, 23 GB, even 53 GB, requiring manual `purge`/`repack`/`VACUUM`, `exclude` globs, and offloading to InfluxDB. A community architecture discussion (home-assistant/discussions #2899) explicitly states "HA not designed to store only what is needed from the beginning" and that the impact (SD-card wear, slow restarts, failed updates) isn't visible "until it's too late." Per-entity retention has been repeatedly requested and not delivered (core PR #121377 closed).
- **Integration-quality variance.** Because integrations are community-maintained with uneven adherence to quality tiers, reliability varies widely; a single bad integration spamming state changes is a common DB-bloat culprit.
- **State `state.state` is always a string** with magic `"unavailable"`/`"unknown"` values — a data-model compromise that pushes type-handling into every consumer.

**Explainability (the differentiator ceiling).** HA's **automation traces** are the closest prior art to HomeSynapse's explanation projection — and their limits define the opportunity. Per HA docs and confirmed primary sourcing: traces default to **5 stored per automation** (`stored_traces`, "If not specified the default value of 5 will be used"; "The last 5 traces are recorded for all automations"), are held **in memory** with a fragile `.storage/trace.saved_traces` backup that can be overwritten/wiped on a double restart (core issue #70310), and are **evicted** — producing the UI error **"Chosen trace is no longer available"** (frontend issue #10768; multiple community threads). Critically, **a trace is made only "when an automation is run"** — if the trigger never matches, **no trace exists at all** ("If there are no trace entries… the automation may not have triggered"). So HA can show "why did it take the wrong branch" but cannot durably answer "why did it NOT fire (trigger-never-matched vs condition-false)" or "did the device actually confirm?" — exactly the three questions HomeSynapse targets. HA's traces are also YAML-`id`-dependent and not a queryable historical projection. (Note: HA docs give the default of 5 and allow raising it via `stored_traces`, but document no hard maximum.)

**AI direction.** HA's "Assist" uses a **two-tier model**: the native rule-based Assist handles known intents first (fast, local, pattern-matched), and only unrecognized queries fall back to an LLM (local via Ollama or cloud), gated by a "Control Home Assistant" toggle and a "prefer local intents" setting. Only tool-calling models can control HA. HA added LLM-assisted automation authoring (a "Suggest" button) and `start_conversation` for proactive prompts. Local STT/TTS (Whisper/Piper/Speech-to-Phrase, Wyoming protocol) keeps voice on-device; per HA's "Voice Chapter 11" blog (Oct 22 2025), streaming gave a **10× TTS-latency improvement** — "Without streaming, both Home Assistant Cloud and Piper took more than five seconds to respond! With streaming enabled, both TTS services took about half a second to start talking back."

### 2.2 openHAB (Java/OSGi — same language family)

**Core architecture.** openHAB uses an **Item/Thing/Channel** abstraction (Things = devices, Channels = capabilities, Items = the abstract state) over an OSGi (Eclipse Equinox/Karaf) module system, with a binding model for integrations and an event bus. This is the closest structural analog to HomeSynapse's entities→devices→capabilities and JPMS modularity.

**What worked.** OSGi gives true runtime modularity (bundles install/start/stop/update at runtime, versioned dependencies via manifest headers) — conceptually similar to JPMS goals. The Thing/Channel separation cleanly models capabilities. Persistence services are pluggable.

**What failed / was regretted — the cautionary tales.**
- **Rules-engine proliferation.** openHAB accreted the Xtext-based **Rules DSL**, then **JSR223** scripting (Groovy, JS/Nashorn then GraalJS, Jython then GraalPython, JRuby), **Blockly** visual rules, and the "Next-Generation Rule Engine" with Modules/ModuleTypes. The result: fragmented documentation (docs issue #1855 admits "the rules documentation is in sore need of reworking," basics buried in DSL reference, "JSR223 page is too prominent and incomplete"), end-of-life engines (Nashorn JS, Jython 2.7), and users repeatedly asking "which language should I use?" JSR223 also "allows access to all packages… use at your own risk, since changes outside the official APIs occur frequently and are not considered breaking changes" — an API-stability nightmare.
- **OSGi complexity cost.** The flexibility comes with steep developer onboarding and operational fragility — major-version migrations (1.x→2.0, 2.5→3.0, →4.0, →5.0) repeatedly broke setups: loss of JS rule support 1.x→2.0, no built-in auth in 2.0 (needed reverse proxy), Java-version jumps (Java 17 for 4.0, Java 21 for 5.0) silently failing `apt` upgrades, and a migration guide whose "Breaking Changes" link was itself broken (distro issue #1339).

**Lesson for HomeSynapse.** One frozen, component-based authoring model is a feature, not a limitation. The "no templating DSL" anti-requirement is directly validated by openHAB's fragmentation. JPMS modularity should expose a *narrow, stable, versioned* API surface — the opposite of JSR223's "access everything."

### 2.3 SmartThings (the forced-migration disaster)

**Core architecture.** SmartThings began **cloud-first**: Groovy Device Type Handlers (DTHs) and SmartApps ran in Samsung's cloud, so device control depended on internet + cloud uptime. It later pivoted to **Edge drivers** (Lua, running locally on the hub) for local execution.

**What failed — the canonical anti-pattern.** The **Groovy→Edge migration was destructive and broke users' setups.** Per SmartThings' own Platform Transition FAQ: migration of Groovy DTHs to Lua Edge drivers ran Oct 2022–2023; "A small number of devices will lose some functionality"; devices without a supported Edge driver were "migrated to a generic 'Thing' placeholder"; deleting a device "will remove it from all the Routines, Scenes, or Services it is associated with"; "There is no published schedule for when particular devices will be migrated, nor will you receive a notification that the migration has occurred." SmartApps had to be re-installed. This forced thousands of users to re-pair devices and rebuild automations, and drove the documented "SmartThings refugee" migration to Hubitat.
- **Cloud-dependency outages.** SmartThings has a long incident history (one aggregator has tracked 117+ incidents; another 405+ outages since 2019), with documented events (e.g., Oct 20–21 2025 "Platform Degraded Performance") where Zigbee/Z-Wave devices and virtual switches stopped responding even though local radios were fine — because execution routed through the cloud.

**Lesson for HomeSynapse.** This is the empirical case for the **no-destructive-migration anti-requirement and immutable log**. SmartThings violated both: it changed the runtime substrate (Groovy→Lua), broke the data model (devices→placeholders), and silently severed automation references. HomeSynapse's "immutable log + no destructive schema migration + additive cloud" is the precise antidote.

### 2.4 Hubitat (local-first commercial validation)

**What worked.** Hubitat's entire value proposition is **100% local processing** — "automations run entirely on the hub; routines fire during internet outages." Independent testing reports ~50–87 ms local automation latency vs SmartThings' 2–5 s cloud round-trips. A Smart Home Explorer 2026 hub comparison citing PCMag reports that "PCMag's 24 hours of cloud-outage testing achieved 97.8% automation success rate," with Hubitat routines firing "within 50 ms latency" vs SmartThings cloud bridging "within 200 ms latency" (these figures are secondhand via the aggregator citing PCMag, so treat the precise percentage as indicative rather than independently verified). Hubitat captured the SmartThings-refugee market explicitly on local reliability + privacy + no subscription. Migration testimonials report ~99% Z-Wave/Zigbee device compatibility and one-weekend migrations.

**What complicates the thesis.** Hubitat's usability is a documented weakness — TechHive called the local-only goal "noble but ultimately impractical" for beginners, citing a "world of hackery" setup, 1–3 hour onboarding, and a non-intuitive web admin. Also, the moment you add cloud integrations (Alexa, Nest), "you pretty much undo the security blanket." Hubitat still uses Groovy apps/drivers — inheriting some of the same community-driver-quality variance.

**Lesson.** Local-first is validated as a market position, but **UX/setup is the make-or-break**. HomeSynapse's "it just works" bar and first-automation experience matter as much as the architecture.

### 2.5 Apple HomeKit + Matter/Thread (standardization & security model)

**Matter security/data model.** Matter's architecture is genuinely strong and worth learning from: a **fabric** is a security domain sharing a root CA and 64-bit Fabric ID; **commissioning** assigns a Node Operational Certificate; **device attestation** uses a per-device immutable **DAC** (Device Attestation Certificate) chaining to a PAI then a PAA root in the **Distributed Compliance Ledger**, with PASE (Password-Authenticated Session Establishment) from the QR/setup code. **Multi-admin** lets one device join multiple fabrics with a shared data model but separate operational credentials. This certificate-chain + attestation model is a reference for HomeSynapse's per-scope keys and trust model.

**What failed / adoption friction.** Matter has under-delivered on its interoperability promise. Documented problems (multiple 2025–2026 sources): **version-mismatch fragmentation** (a device on Matter 1.4 may "desync or become a ghost" when another controller is on 1.2/1.3; Google Home notoriously lags the spec); **multi-admin battery drain** (a sensor on three fabrics polled by each can drop from 3-year to 18-month battery life because it "never gets to go to sleep"); **slow feature rollout** (camera support only in Matter 1.5, Nov 2025; many firmware updates still not shipped); Thread border-router fragmentation; and The Verge's reviewer reporting "not one Matter-based device working reliably." Matter 1.6 (June 17 2026) added full NFC commissioning and **Joint Fabric** — which, per the CSA newsroom, "allows multiple user-authorized controllers to co-administer a single shared Matter network" via a central Datastore — but per TechTimes (June 19 2026) "platform adoption lags have been the most consistent criticism of the standard since its 2022 debut," and "Google Home is still implementing earlier Matter versions."

**Lesson.** Reserving Matter/Thread for post-MVP and shipping **Zigbee-first** is correct. The radio being Thread-capable is the right hedge. Adopt Matter's attestation/fabric concepts for the trust model; don't depend on Matter's interoperability maturing on your schedule.

### 2.6 Zigbee2MQTT / ZHA / deCONZ (the integration layer)

**Core pattern.** All three solve the Zigbee long tail with a **community device database + converter/quirk model**: Z2M uses `zigbee-herdsman-converters`; ZHA uses Python "quirks" (zha-device-handlers) that do "on-the-fly conversion of custom Zigbee configurations." Both abstract the coordinator radio across **ZNP (TI), EZSP (Silicon Labs), deCONZ, zigate, xbee** — exactly the ZNP/EZSP dual-path HomeSynapse already plans.

**What worked.** The converter database is the reason these tools support thousands of devices including the Tuya/Xiaomi long tail. Z2M's coordinator abstraction supports install-code/QR commissioning for zstack, ember, and deconz radios. Backup/restore (and thus coordinator migration) is "only implemented for the zstack and ember adapters" — notably the same two HomeSynapse chose.

**What's painful.** The manufacturer-quirk long tail is genuinely endless — Tuya devices use non-standard cluster `0xEF00` with per-datapoint typing; Xiaomi/Aqara devices deviate from spec; quirks rely on volunteers ("submitting a device support request does not guarantee that someone will develop a custom quirk"). EZSP protocol-version mismatches (e.g., "NCP EZSP protocol version… does not match Host version 13") cause hard startup failures.

**Lesson.** **Do not build a bespoke quirk database from scratch.** The converter-database pattern is the proven way to bound the long tail, and the ZNP/EZSP abstraction is validated. HomeSynapse should adapt (license-permitting) or interoperate with existing converter data rather than re-deriving thousands of device definitions — the database, not the coordinator code, is the moat and the cost.

### 2.7 Node-RED (visual/flow-based authoring)

**Core pattern.** Node-RED is flow-based: **nodes** (pre-built, unit-tested components) wired by **messages**, on a Node.js event-driven runtime, with 5,000+ community nodes. Each node is "a complete module that has been unit tested," so authors "focus on checking the operation at the join level."

**What worked / what teaches HomeSynapse.** The component-composition model (validated nodes + wiring) is precisely the non-DSL, composable authoring philosophy HomeSynapse's "component-based, not templating DSL" stance embraces — and a natural future AI-authoring target (generate a flow graph, not free-form code).

**Limits.** Academic work (ACM 2018) notes visual wiring "can reduce understandability and obscure error propagation paths," and complex flows "do not scale, at least from a developing process perspective" — and Node-RED lacks built-in flow testing/debugging. Function nodes (custom JS) reintroduce the very code-quality problems components avoid.

**Lesson.** Components-over-DSL is right; but invest in flow comprehensibility and testing from the start (HomeSynapse's causal chain + explainability projection directly addresses Node-RED's "obscured error propagation" weakness).

### 2.8 Event-Sourcing / CQRS (HomeSynapse IS event-sourced)

**Documented pitfalls (the load-bearing ones for HomeSynapse):**
- **Schema/event versioning.** The immutable-event rule means you can never edit old events; you must use **upcasting** (transform old→new at read time), **versioned event types** (`OrderPlaced_v2`), or weak/mapping schemas. "Forgetting to upcast during projection rebuild is a silent failure." Best practice: add an event `version` field from day one; prefer additive changes; "test rebuild with the full history including old events before deploying schema changes."
- **Projection rebuild cost.** Rebuild time grows non-linearly with log size; teams use out-of-place/blue-green rebuilds, snapshots, and pruning of inactive streams. Snapshots have their own versioning problems and are "often not worth implementing due to conceptual and operational costs" (Greg Young) — but without them every read replays all events.
- **External side-effects on replay — critical.** "Many of the advantages of Event Sourcing stem from the ability to replay events at will, but if these events cause update messages to be sent to external systems, then things will go wrong." The fix (Jérémie Chassaing): the `Apply` method that rebuilds state must be a **pure function with no external side-effects**; side-effects (device dispatch) happen only on *new* command handling, never on replay.
- **Command vs event dispatch.** DDD consensus (Microsoft/eShop, Oskar Dudycz): **domain events** can be in-process and synchronous within an aggregate; **integration events** (cross-process) should be asynchronous and only published *after* the transaction commits (outbox pattern). Event sourcing ≠ event-driven architecture — but they compose, and the event log is the natural integration substrate.
- **Eventual consistency / read-your-writes.** Projections lag the log; the fix is causal-consistency tokens / version-stamped reads ("return the event's version; the read waits until the projection caught up").
- **GDPR/right-to-be-forgotten** conflicts with immutability; the standard pattern is **crypto-shredding** (store PII encrypted, delete the key) — which HomeSynapse already plans.

### 2.9 Local-First Software movement (the federation/cloud seam)

**Patterns.** Ink & Switch's "local-first software" (the seven ideals; "the availability of another computer should never prevent you from working") plus **CRDTs** (Automerge — "never deletes anything… stores every change with efficient compression… can compute an exact diff between two points in history") and sync engines (ElectricSQL's "Electric Next" server-streaming model, PowerSync, Yjs, Loro). Automerge 3.0 (May 2025) cut memory **by over 10× (sometimes far more)** — per automerge.org, "pasting Moby Dick into an Automerge 2 document consumes 700Mb of memory, in Automerge 3 it only consumes 1.3Mb!" with load times dropping from 17 hours to 9 seconds. Conflict models range from **last-write-wins** (simple, drops data) to **CRDT auto-merge** to **manual/diff merge**.

**Lesson for HomeSynapse federation.** A single-home immutable causal log is essentially an **append-only event stream that replicates outward** — the cleanest fit is **event-log shipping / replication** (like ES replication) rather than full document CRDTs, because the log is already append-only and causally ordered. CRDTs become relevant only where **two sites concurrently mutate the same logical entity** (rare in a single home; real in multi-site/MDU). Automerge's "history + diff" model is the closest conceptual cousin to HomeSynapse's "explanation = projection of the log."

### 2.10 The AI-home frontier & LLM-as-controller safety

**Landscape.** HA Assist (two-tier, above), local LLMs (Ollama, the `home-llm` project with models fine-tuned for home control running on a Pi/CPU), and the broad industry LLM pivots. The dominant practical lesson from practitioners: **reasoning/"think" models are catastrophic for voice latency** (one builder reports qwen3:4b "think mode" reading its internal monologue aloud), so the deterministic-first/LLM-fallback split is not just safety — it's UX necessity.

**Safety architecture from research (directly validates HomeSynapse's frame).** The **Planner–Executor** pattern separates a (probabilistic) LLM planner from a (deterministic, least-privilege, often stateless) executor, with a **Verifier** / **safety gate** in between. Concrete research: VERIMAP (verification-aware planner generating deterministic verification functions), SafeGate (pre-execution safety gate + task safety contracts for LLM-controlled robots), "Blueprint First, Model Second" (deterministic workflow with a Double-Check safety-gate node), VeriPlan (formal model-checking as "deterministic boundaries for the inherently probabilistic nature of LLM systems," a "safety net"), and f-secure LLM systems (LLM planner + rule-based executor + security monitor, with a Structured Executable Planning Format).

**Lesson.** HomeSynapse's "AI proposes; the deterministic engine disposes; everything auditable" is **exactly the emerging research consensus**. The immutable log + explainability projection is the audit substrate these papers call for; the no-autonomous-retry deterministic engine is the verifier/executor.

### 2.11 Adjacent reliability/safety (KNX/BACnet, OT/SCADA)

Building-automation (KNX, BACnet) and OT/SCADA emphasize **deterministic, locally-executing control** with no dependence on cloud reasoning — reinforcing local-first + deterministic-engine choices. The "LLM-as-planner + deterministic-verifier/executor" pattern is the bridge from these safety-critical domains to AIoT.

## 3. Lessons → HomeSynapse Mapping

| Pattern / Anti-pattern (source) | HomeSynapse today | Recommendation | Confidence |
|---|---|---|---|
| Immutable event log as source of truth (ES literature) | Yes | KEEP | High |
| Recorder/history DB unbounded growth (HA) | Partial — log is SoT, retention TBD | ADJUST-FOR-MVP: per-scope retention + projection pruning + snapshots designed now | High |
| Destructive forced migration (SmartThings Groovy→Edge) | No (anti-req) | KEEP / AVOID the anti-pattern | High |
| Rules-engine proliferation (openHAB) | No — single component model | KEEP (resist second paradigm) | High |
| Pure-function replay, side-effects only on new commands (ES) | Partial/unclear | ADJUST-FOR-MVP: enforce no-side-effect replay | High |
| Additive event versioning + upcasting + version field (ES) | Partial (no destructive migration) | ADJUST-FOR-MVP: add explicit event `version` + upcasters + full-history rebuild tests | High |
| Explainability incl. non-firing + command-outcome (nobody does it) | Yes (flagship) | KEEP / build "why-not" projection in MVP | High |
| Two-tier deterministic-first, LLM-fallback (HA Assist) | Reserved | RESERVE-SEAM (AI as log producer/consumer) | High |
| Planner/Verifier/Executor safety gate (AI research) | Yes (engine = verifier/executor) | KEEP / RESERVE-SEAM for AI author | Medium-High |
| Device converter/quirk database (Z2M/ZHA) | Bespoke runtime planned | ADJUST: adapt/interop existing converter DB, don't rebuild | Medium-High |
| ZNP/EZSP coordinator abstraction + backup-restore (Z2M) | Yes (both paths) | KEEP | High |
| Matter fabric/DAC attestation trust model | Reserved | RESERVE-SEAM (adopt concepts for per-scope keys) | Medium |
| Matter as MVP dependency (adoption friction) | No (post-MVP) | KEEP / AVOID early dependency | High |
| Event-log shipping for federation (ES replication) | Reserved | RESERVE-SEAM (log replication, CRDT only for concurrent multi-site mutation) | Medium |
| Crypto-shred for GDPR/right-to-be-forgotten (ES) | Yes | KEEP | High |
| Local-first as value proposition (Hubitat/HA) | Yes | KEEP | High |
| UX/setup is make-or-break (Hubitat) | Unclear | ADJUST-FOR-MVP: invest in first-run/pairing/first-automation | Medium-High |
| SBOM + secure-by-default + update obligations (CRA/PSTI) | Partial | RESERVE-SEAM: SBOM + signed-update pipeline | High |
| Event-driven command dispatch for cross-process scaling (ES/DDD) | Decision open | ADJUST-FOR-MVP: go event-driven (see Decision 1) | Medium-High |

## 4. Decision Briefs

### Decision 1 — Command-pipeline shape: event-driven vs in-process
**Recommendation: EVENT-DRIVEN (executor emits `command_issued`; a dispatch subscriber consumes it, ordered via global log position; outcome events correlated back via the Pending Command Ledger). Confidence: Medium-High.**

*Evidence.* The DDD/ES consensus distinguishes in-process **domain events** (fine for synchronous, single-aggregate side-effects) from cross-process **integration events** (must be async, post-commit, via outbox). HomeSynapse's own aspirations — cross-process, multi-host, cloud federation, and AI as a first-class log consumer — are precisely the conditions under which the event-driven shape is mandated: "the event log is the natural integration substrate," and AI/cloud consumers subscribe to the same ordered stream rather than to in-process calls. The append-only log gives you the global ordering for free.

*Trade-offs.* Event-driven adds latency (a subscriber hop) and eventual-consistency UX (the "command issued but outcome not yet confirmed" window) — but HomeSynapse already embraces this with the dispatched→confirmed/unconfirmed/failed model and 1–2 s polling (no WebSocket in MVP). In-process dispatch is simpler and lower-latency for a single host but becomes a re-architecture the moment you cross a process boundary. Critically, **device dispatch must never run on log replay** — the side-effect belongs to new-command handling only (the pure-function replay rule).

*What would change it.* If MVP scope were permanently single-process single-host with no AI/cloud seam, in-process would be defensible. It isn't — so reserving the event-driven seam now avoids the SmartThings-class re-architecture later. Mitigate latency by keeping the dispatch subscriber in-process for MVP but communicating *only* via emitted events (logical event-driven, physical co-location), so the seam is real but the latency is minimal.

### Decision 2 — Local-first → cloud event-log federation
**Recommendation: Event-log shipping / append-only replication as the primary pattern; CRDTs only for the narrow case of concurrent multi-site mutation of the same logical entity. Confidence: Medium.**

*Evidence.* HomeSynapse's source of truth is already an append-only, causally-chained log — structurally identical to an event-sourcing replication stream. ES replication ships ordered events outward; the cloud/remote/other-site rebuilds projections from the replicated log. This preserves "local-first inviolate" (local function never depends on the replica) and "additive cloud" (the cloud is just another projection consumer). Automerge's history+diff model shows the conceptual fit, but full document-CRDTs are overkill for a log that is already conflict-free by construction within a single home.

*Conflict model a multi-site home actually needs.* Within one home, a single writer (the local runtime) means **no merge conflicts** — log shipping suffices. Across sites/MDU/hospitality, conflicts arise only if two sites can mutate the *same* logical entity concurrently (e.g., a shared identity or a shared policy). For that, use **scope as an additive envelope-level discriminator** (which HomeSynapse already reserves — no site-local-sequential identity) so events from different sites never collide on identity; reserve a CRDT or last-write-wins merge **only** for genuinely shared mutable state. Most "multi-site" is actually partitioned, not concurrent.

*What would change it.* If real-time collaborative editing of shared automations across sites becomes a requirement, escalate to a CRDT (Automerge/Yjs/Loro) for that specific shared document.

### Decision 3 — AIoT integration + safety architecture
**Recommendation: VALIDATED. Keep the deterministic + explainable + no-autonomous-retry engine + immutable causal log as the safety frame. AI enters at three seams (author, reasoner, device-intelligence) as a log producer/consumer, never as an autonomous actuator. Confidence: High.**

*Evidence.* This is the emerging research consensus (Planner–Executor, VERIMAP, SafeGate, Blueprint-First, VeriPlan, f-secure LLM). The pattern is universally: probabilistic planner → deterministic verifier/safety-gate → deterministic executor, with an audit trail. HomeSynapse's engine *is* the deterministic verifier/executor; the immutable log + explanation projection *is* the audit substrate; "no autonomous retry" *is* the least-privilege executor constraint. HA Assist's two-tier (deterministic-first, LLM-fallback) confirms the same shape works in production and is a UX necessity (reasoning models are too slow/unsafe to be the primary path).

*Right seam for AI.* (a) **Author**: NL→proposed component-flow, surfaced to the user for confirmation before it ever enters the engine (a pre-execution safety gate); the proposal and its provenance are themselves logged. (b) **Reasoner/suggester**: reads the log + explanation projection, proposes automations or flags anomalies — output is advisory events, not commands. (c) **Device-intelligence**: anomaly/prediction as projections over the log. In all three, **AI emits proposals as events; the deterministic engine disposes**.

*On-device vs cloud inference.* For a privacy-first brand, **default to on-device/edge inference** (Ollama-class small models, fine-tuned home models run on the local hub for control intents; the `home-llm` project proves Pi/CPU feasibility), with cloud inference as an **opt-in, clearly-scoped** fallback for heavy reasoning — mirroring HA's separate-pipeline approach ("keep your local and cloud assistants separate"). Never send person-linked/sensitive-scope data to cloud inference before the at-rest cipher and explicit consent are in place.

*NL-authoring safety/verification model.* Generate a *structured* artifact (component flow), not free-form code; validate it against the frozen action model and cascade governance (the deterministic verifier); require human confirmation for any actuation-bearing automation; log the proposal, the verification result, and the human decision. This is VeriPlan's "model-checker as safety net" applied to home automation.

### Decision 4 — Device-model & coordinator strategy
**Recommendation: Build the coordinator *runtime* (ZNP/EZSP abstraction) — which you're doing — but LEVERAGE an existing device-converter database for the quirk long tail; don't rebuild it. Stay Zigbee-first, Matter/Thread post-MVP. Confidence: Medium-High.**

*Evidence.* Z2M/ZHA prove the coordinator abstraction (ZNP/EZSP/deCONZ) is tractable and that backup/restore is mature exactly for zstack+ember (HomeSynapse's two paths). They also prove the **device-quirk long tail is effectively infinite and volunteer-driven** — Tuya's non-standard `0xEF00` cluster, Xiaomi deviations, no-guarantee quirk requests. Re-deriving thousands of device definitions is a multi-year cost with no differentiation payoff. The database, not the radio code, is where the effort and the risk concentrate.

*How to bound the quirk tail.* (a) Align to standard ZCL clusters first (HomeSynapse already does — this maximizes the devices that "just work" without quirks). (b) Adapt or interoperate with an existing converter database (license-permitting — zigbee-herdsman-converters is MIT; zha-device-handlers is Apache-2.0) rather than starting empty. (c) Treat quirks as data (declarative converter definitions), not code, so new devices don't require a release — exactly Z2M's and Tasmota's `.zb`-plugin lesson.

*Matter/Thread trajectory.* Matter's interoperability is years from the maturity its marketing implies (version-mismatch fragmentation, multi-admin battery drain, slow platform adoption through 1.5/1.6). The Thread-capable radio is the correct hedge; model the device layer so Matter clusters map onto the same entity→capability abstraction (Matter's data model is cluster-based like ZCL, so this is natural), but do not let Matter gate the MVP.

*What would change it.* If a converter-DB license proves incompatible with HomeSynapse's distribution model, fall back to a curated subset + a community-contribution pipeline (the ZHA model), accepting slower long-tail coverage.

### Decision 5 — Maintainability disciplines (doc-vs-source drift; testing)
**Recommendation: Adopt docs-as-code with generated reference + ADRs as the architecture record; make the live end-to-end demo the integration/E2E gate, backed by hardware-in-the-loop and given-when-then unit tests. Confidence: Medium-High.**

*Evidence.* openHAB's doc fragmentation (docs issue #1855; broken migration links in distro #1339) and HA's reliance on architecture discussions show that **docs drift unless generated from or co-located with source**. ES testing best practice is **given-when-then** (set up past events → issue command → assert on produced events) for business logic, plus separate integration tests for projections, idempotency, and schema-evolution/replay ("test rebuild with the full history including old events").

*Concrete disciplines.* (a) **ADRs** for every frozen decision (the action model, command-pipeline shape) committed alongside code, so "doc-vs-source drift" becomes a review-gate failure. (b) **Generated API reference** from the JPMS module exports (narrow, versioned surface — the anti-openHAB-JSR223). (c) **Test pyramid**: given-when-then unit tests on the engine; projection-rebuild tests over full synthetic histories (catch the "forgot to upcast" silent failure); **hardware-in-the-loop** for both coordinator paths (TI + Silabs) since EZSP/ZNP version mismatches are a documented hard-failure class; and the **live E2E demo as the honest progress unit** — automate it as a smoke test. (d) Event-schema registry with mandatory `version` field and upcaster coverage checks in CI.

## 5. Risk Register

| Documented failure/disaster (source) | HomeSynapse exposure | Guardrail (have / add) |
|---|---|---|
| Recorder DB unbounded growth, SD-card wear, failed updates (HA) | High — immutable log grows forever by design | HAVE: projection model. ADD: per-scope retention, log compaction/snapshots, projection pruning, growth monitoring from day one |
| Forced destructive migration breaking setups (SmartThings) | Low — explicitly anti-req | HAVE: immutable log + no destructive migration. Maintain rigor on every milestone |
| Cloud-dependency outage disabling local control (SmartThings) | Low — local-first inviolate | HAVE: local-first. Ensure cloud seam is strictly additive |
| Rules-engine fragmentation + doc rot (openHAB) | Medium — pressure to add DSL/visual later | HAVE: single component model. AVOID adding paradigms; ADRs |
| Side-effects on event replay (ES) | High if not enforced | ADD: pure-function replay invariant; dispatch only on new commands; CI test |
| Silent upcast failure on projection rebuild (ES) | High | ADD: event `version` field, upcaster coverage, full-history rebuild tests |
| Eviction of explanation/trace (HA in-memory traces) | Low — log is durable SoT | HAVE: explanation = durable projection of immutable log (the differentiator) |
| Device-quirk long tail unmanageable (Z2M/ZHA) | High if bespoke | ADD: leverage existing converter DB; quirks-as-data |
| EZSP/ZNP version-mismatch hard failures (Z2M) | Medium — dual coordinator paths | ADD: hardware-in-the-loop tests for both radios; clear version diagnostics |
| Matter version-mismatch / multi-admin battery drain | Low (post-MVP) | KEEP Matter out of MVP critical path |
| AI autonomous actuation / prompt-injection (AI research) | Medium (future) | HAVE: AI-proposes/engine-disposes + audit log. ADD: pre-execution safety gate, structured-artifact authoring |
| Regulatory non-compliance (CRA/PSTI/Cyber Trust Mark) | Medium — selling connected product into EU/UK | ADD: SBOM (CycloneDX/SPDX), signed-update pipeline, coordinated-vuln-disclosure policy, secure-by-default (already loopback/auth-first) |
| GDPR right-to-be-forgotten vs immutable log | Medium | HAVE: crypto-shred + per-scope keys |
| UX/setup too hard (Hubitat) | Medium | ADD: first-run/pairing/first-automation investment |

## 6. Trends & Future-Proofing (2-5 years)

**(i) AI/AIoT.** Converging on local-first LLMs for control intents + cloud for heavy reasoning, with deterministic-first fallback and planner/verifier/executor safety. HomeSynapse is well-positioned; **reserve the AI-as-log-producer/consumer seam now**; the safety frame is already correct. Pressure point: users will expect NL authoring soon — build the structured-artifact authoring seam early.

**(ii) Cybersecurity & regulation.** The **EU Cyber Resilience Act** is in force (Dec 10 2024). Per the European Commission, the **reporting obligations set out in Article 14 apply from 11 September 2026** (an "early warning within 24 hours" and "full notification within 72 hours" via ENISA's CRA Single Reporting Platform), and the **main provisions apply from 11 December 2027**; Article 69(3) extends reporting even to products placed on the market before that date. Fines run "up to €15 million or 2.5% of the undertaking's total worldwide annual turnover… whichever is higher" for Annex I / Article 13–14 breaches (lower tiers of €10M/2% and €5M/1% apply to other obligations). The CRA mandates SBOM, secure-by-default, coordinated vulnerability disclosure, and security updates for the support lifetime. **UK PSTI** (in force) bans default passwords and mandates vuln-disclosure; the **US Cyber Trust Mark** is a voluntary certification. HomeSynapse's local-first + auth-before-exposure + loopback-default + at-rest encryption is a genuine compliance and marketing advantage. **Reserve an SBOM + signed-update + vuln-disclosure seam now** — these become table-stakes within the MVP-to-post-MVP window. The local-first architecture itself reduces attack surface (no cloud account to breach).

**(iii) Interoperability.** Matter/Thread will keep maturing slowly; version fragmentation and platform-adoption lag persist into 2026. **Stay Zigbee-first; keep the Thread-capable radio; map Matter clusters onto the existing capability model when adoption justifies it.** Don't let any anti-requirement block a future Matter controller/bridge role.

**(iv) User demands.** Privacy backlash and cloud-outage fatigue (Amazon's 2025 local-processing changes; SmartThings outages) are driving demand toward exactly HomeSynapse's local-first, no-subscription, "it just works" position. Sustainability (SD-card wear from over-logging — the HA lesson) argues for disciplined retention. **No HomeSynapse anti-requirement is contradicted by near-term trends** — the one to watch is "no WebSocket in MVP / poll 1–2 s": as users expect snappier UI and as the system scales, a push/WebSocket layer will be pressured post-MVP (reserve, don't build).

## 7. Staged Roadmap of Architectural Moves

**NOW (validate/correct current architecture):**
1. Lock the **event-driven command-pipeline** decision (logical event-driven, physically co-located for MVP) — Decision 1.
2. Enforce the **pure-function replay** invariant (no device side-effects on replay) with a CI test.
3. Add an explicit **event `version` field + upcaster framework**, and a full-history projection-rebuild test.
4. Design **per-scope retention + snapshot/compaction** for the log before it grows (the HA lesson).
5. Write **ADRs** for all frozen decisions; stand up generated API reference from JPMS exports.

**MVP:**
6. Ship the **"why-not" explanation projection** (trigger-never-matched vs condition-false vs device-didn't-confirm) — the flagship differentiator, durable because it's a projection of the immutable log.
7. **Zigbee-first** with ZNP + EZSP auto-detect; **leverage an existing converter database** (quirks-as-data) rather than building one; hardware-in-the-loop tests for both radios.
8. Implement the **Pending Command Ledger** with dispatched→confirmed/unconfirmed/failed and honest degradation.
9. Invest in **first-run/pairing/first-automation UX** (the Hubitat lesson).
10. Stand up **SBOM (CycloneDX/SPDX) + signed-update pipeline + vuln-disclosure policy** (CRA/PSTI runway).

**POST-MVP:**
11. **Cloud federation via event-log shipping** (additive, local-first-inviolate); scope as additive envelope discriminator; CRDT only for concurrent shared-state.
12. **Enterprise audit projection** (default-off, hash-chain tamper-evident).
13. **AI authoring seam** (NL→structured component flow, pre-execution safety gate, human confirmation, fully logged).
14. **Matter/Thread** controller/bridge mapping onto the existing capability model.
15. Evaluate a **push/WebSocket layer** if polling latency becomes a UX ceiling.

**FAR-FUTURE:**
16. **AI reasoner/device-intelligence** as advisory log consumers (anomaly/prediction), engine-disposes safety frame intact.
17. Multi-site/MDU/hospitality federation at scale with the reserved identity-scoping seam.
18. On-device fine-tuned home models as the default control-intent path; cloud inference strictly opt-in.

## 8. Sources & Confidence

**FACT (documented, primary or strong secondary):**
- HA architecture: event bus + state machine + service registry (HA core docs, `homeassistant/core.py`). FACT.
- HA Recorder DB growth pain: multi-GB databases, manual purge/repack, no per-entity retention (HA community guides, discussion #2899, HA Recorder docs). FACT.
- HA traces: default 5 (`stored_traces`), in-memory, evictable ("Chosen trace is no longer available"), no trace when trigger never matches (HA docs /automation/yaml/ and /automation/troubleshooting/ at v2026.5.4; core issue #70310; frontend issue #10768). FACT. (No documented hard maximum for `stored_traces`.)
- HA scale: 3,000+ brands, ~2M installations (GitHub Blog Dec 2025, Franck Nijhof). FACT.
- HA Assist two-tier deterministic-first/LLM-fallback; local Whisper/Piper/Wyoming; 10× streaming-TTS latency improvement (HA blog Sep/Jun/Oct 2025). FACT.
- openHAB rules-engine multiplicity + doc-rework need + breaking migrations (openHAB docs, docs issue #1855, distro issue #1339). FACT.
- SmartThings Groovy→Edge migration specifics (SmartThings Platform Transition FAQ). FACT.
- SmartThings outage history (status aggregators; community Oct 2025 thread). FACT (aggregator counts are secondary).
- Hubitat local-first latency/outage claims — vendor + reviews; the "97.8% / 50 ms / 200 ms" PCMag figures are cited secondhand via a 2026 aggregator and should be treated as indicative. FACT for reviews; vendor/aggregator figures flagged.
- Matter fabric/DAC/attestation/commissioning (CSA Matter Handbook, Silicon Labs/Espressif docs). FACT.
- Matter adoption friction, multi-admin battery drain, 1.5/1.6 timing, Joint Fabric (XDA, matter-smarthome.de, CSA newsroom, TechTimes June 2026). FACT (journalistic + CSA primary for 1.6).
- Z2M/ZHA converter-database + ZNP/EZSP abstraction + backup-restore zstack/ember only (Z2M docs, ZHA docs). FACT.
- ES pitfalls: versioning/upcasting, rebuild cost, no-side-effects-on-replay, command/event dispatch (Microsoft Learn, AWS, event-driven.io, Chassaing, Greg Young summaries, ScienceDirect empirical study). FACT.
- Local-first/CRDT patterns; Automerge 3.0 >10× memory reduction (Ink & Switch, automerge.org, sync-engine landscape). FACT.
- LLM planner/verifier/executor safety (arXiv: VERIMAP, SafeGate, Blueprint-First, VeriPlan, f-secure). FACT (research, some preprints).
- CRA dates/fines, PSTI, Cyber Trust Mark (European Commission, Pillsbury, Mend, Thales). FACT.

**INFERENCE (my analysis, not documented as such):**
- That event-driven dispatch is the better fit for HomeSynapse's specific cross-process/AI aspirations (Decision 1). INFERENCE from ES/DDD principles applied to HomeSynapse's stated goals.
- That event-log shipping beats CRDTs for HomeSynapse federation (Decision 2). INFERENCE.
- That leveraging an existing converter DB beats bespoke (Decision 4). INFERENCE from Z2M/ZHA cost evidence + license facts.
- The specific seam placements for AI (Decision 3). INFERENCE aligned to research consensus.

**The 5 most important open questions this research could NOT resolve, and the primary source that would resolve each:**
1. **Does ANY shipping system durably answer "why did it NOT fire?"** Searches found none, but absence of evidence isn't proof. → A patent search + vendor architecture docs (Josh.ai, Control4, Crestron internal docs) would confirm/strengthen the differentiator claim.
2. **What is HomeSynapse's real event-log growth and projection-rebuild time on Pi-class hardware?** → In-house benchmark (sizes the retention/snapshot strategy; the HA Recorder lesson makes this urgent).
3. **Are the major Zigbee converter databases (zigbee-herdsman-converters MIT, zha-device-handlers Apache-2.0) license-compatible with HomeSynapse's free→paid→enterprise tiers?** → Legal review of the repos' LICENSE files against HomeSynapse's distribution model.
4. **What latency does logical-event-driven dispatch actually add vs in-process on Pi-class hardware?** → In-house prototype measurement (validates the Decision 1 latency-mitigation assumption).
5. **What is the precise CRA conformity class for a local-first smart-home hub (self-assessment vs notified body)?** → CRA Annex III + implementing acts + a notified-body consultation.