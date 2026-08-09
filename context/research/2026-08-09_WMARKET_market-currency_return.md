<!--
file: context/research/2026-08-09_WMARKET_market-currency_return.md
purpose: W-MARKET lane return — the market-currency refresh of the class-(iii) claim surface for S-10 THE CHARTER (Aug-12–13) and THE READ (Aug-16). Executed per context/instructions/2026-08-08_research-lane_WMARKET-market-currency_brief.md (v50 beat 1). Five charges: Matter/Thread delta · Home Assistant trajectory · local-first field · model-in-the-loop vs the enforce-vs-propose line · SHORT-clock delta (SCITT / 802.11bf).
audience: the hub (adjudicates at intake); the charter SKELETON (Aug-11 EOD) — filed 2026-08-09, ahead of the 2026-08-11 09:00 CT due, so this consumes as a NAMED input.
state-type: research return (write-isolated)
status: RETURNED 2026-08-09 by the W-MARKET lane (fresh Cowork session; web-backed). Method: five parallel primary-source research passes (one per charge) + a parent adversarial-verification pass that independently re-fetched every falsifier-class and headline primary source before it entered this file as [VERIFIED]. Read-only on every repo; this file is the lane's ONLY repo write. No outreach, no accounts, no posting. The hub adjudicates.
laws-held: D5 language law (the layered form at every enforcement restatement: the deterministic floor is MISSING from the field, not SUPERIOR; L2/L3 without L1 are unsound; L1 without L2 is insufficient) · anti-fabrication ([VERIFIED] = primary source retrieved this lane, URL + access date; [REPORTED] = named secondary; [INFERRED] = own reasoning, so labeled; UNVERIFIED reported loudly, never rounded up) · unbiased-instrument (falsifier-relevant evidence headlines §0; evidence AGAINST our positioning outranks evidence for it) · gate sovereignty (decision input, never a work order; freeze 2026-08-14 EOD; THE READ Aug-16) · R-1 name-agnostic (the product is "the product"; internal docs cited by their own titles only) · comparative statements about named competitors are research notes only — counsel-gated, publish nowhere · moat-watch entries logged as CANDIDATES only (the hub adopts; this lane only watches) · A-14 sizing (15 h/wk weekend-anchored floor) binds every proposal herein.
baseline-at-launch (re-derived 2026-08-09 at the device, per brief §0.8): core d26777c · hivemind 1613205 (at-or-after 5729cdf — the newest spine) · bench 16e672d.
hazards-discharged: L-E division of labor held (this lane owns adoption/commercial/ecosystem currency; physics-positioning analysis is L-E's — the one physics-adjacent surface here, 802.11bf silicon, is reported as clock-delta only per Charge 5's own mandate). LD platform-horizon overlap held (plugin/cloud radar deltas noted as deltas, never re-surveyed). C-2 Tier-0 fence held (its claims are not restated here; the contradiction check is explicit in §6.4 — none found).
-->

# W-MARKET — Market-Currency Research Return (filed 2026-08-09)

## §0 Executive summary (falsifier-relevant findings first)

**F-1 — §9 condition 1 (enforcement reads as overhead): evidence ACCUMULATING, direction adverse, not yet conclusive.** The clearest new datapoint: **Amazon shipped the "Smart Home AI Toolkit" (developer preview, July 2026) — natural-language authoring of agentic device capabilities — and the entire agentic developer surface carries zero safety, confirmation, guardrail, permission, or audit language** ([VERIFIED] at developer.amazon.com this lane, §4.2). The strongest longitudinal datapoint: the Aug-2025 calendar-promptware attack that actuated a Gemini-driven home (lights, shutters, a boiler) produced mitigations and *wider rollout*, not recall, regulation, or market consequence (§4.3). Homey handed ChatGPT full device/Flow control with no published restrictions; Tuya ships a cross digital/physical agent whose only gate is install-time skill vetting. The honest counterweight, stated at full strength: platforms ARE shipping *subtraction-based* floors — Gemini for Home categorically blocks lock/garage/security actuation ([VERIFIED], §4.4), Google added post-attack confirmations, Apple's announced App Intents pattern declares "when they're safe to run" — so the field's behavior is "carve out the scariest categories and ship," which is neither an enforcement layer nor pure indifference. Condition 1 is NOT met; it is measurably closer than at the Jul-28 return.

**F-2 — §9 condition 2 (a major platform ships an unbypassable enforcement layer): NOT TRIGGERED — and the window is now visibly narrowing on a date.** No platform ships a deterministic enforcement floor between model output and home actuator (§4.1 table: the only L1-class mechanisms in the wild are *visibility subtraction* — HA's entity-exposure lists, Google's security-category exclusion — no invariants, no rate limits, no reversibility classes, no audit). But two artifacts moved the clock: **Google now ships a true deterministic pre-tool deny gate ("Agent Hooks": a pre-tool hook returning `{"decision":"deny"}` makes the runtime immediately cancel the tool call) in its Gemini agent runtime** — enterprise/developer-side, not connected to Home, but the L1 socket now exists at a major vendor and could be flipped toward Home APIs ([VERIFIED], §4.5). And **Apple's rebuilt Siri plus the home hub is scheduled for ~September 2026** with an OS-mediated, schema-typed action model — the single biggest dated arm-2 event risk on the calendar ([VERIFIED]/[REPORTED], §4.5). Recommendation-shaped input, not a work order: the charter should treat Sept-2026 as a named re-adjudication tripwire on the F-1/T6 watch.

**F-3 — §9 condition 6 (adjacent FOSS race): NOT falsifier-class, but BOTH halves moved and one baseline sentence is now partially CONTRADICTED.** Home Assistant's "not-triggered traces" are **no longer "in no stable release": stable 2026.7.0 and 2026.8.0 contain live `report_not_triggered` emitters** — verified at raw tag source this lane — but for exactly five *evaluation-error* reasons (missing threshold entity, non-numeric value, unsupported unit…); a plain "value didn't cross the threshold" still produces no trace, buckets stay capped (default 5) and FIFO-evicted, and the feature shipped unannounced (§2.1). The audit/accountability/multi-tenancy story remains dormant at HA (the Minimal-Security-Audit-Log proposal still has zero maintainer replies; RBAC is "a no for now" — Frenck, via collaborator; §2.2). Meanwhile **openHAB 5.2 (2026-07-05) became the first FOSS home platform with an item-level AI permission model** (No-Access/Read-Only/Read-Write, explicitly marketed for shielding locks and garage doors from LLMs) plus an MCP server with token- and tool-level ACLs — authorization, not accountability, so not condition-6 — but the adjacent-FOSS lane is demonstrably capable of moving first (§2.3).

**F-4 — the SCITT actuation-evidence territory is being staked NOW.** **draft-wilder-scitt-physical-site-engage-receipt-00 (Wilder Robotics, 2026-07-29): tamper-evident SCITT receipts for "autonomous or human-directed physical engagement at a specific real-world site," TEE-attested, three-party no-unilateral-forgery trust model** ([VERIFIED], §5.1). This is the closest external filing yet to the RR-W1 SCITT-actuation-profile territory the Jul-28 return told us to hold cheaply. With draft-hawkins-scitt-attested-agent-payment-00 (Aug-05) and an energy-standards body (NAESB) meeting on SCITT (Aug-06), the individual-draft corpus around agent/physical-world evidence is accelerating while the WG itself shows no movement. The Jul-28 return's "decide by ~IETF 127" now reads generous; the decision input here is that the positioning clock aged from "months" toward "now."

**Bottom line for the charter.** The enforce-vs-propose technical thesis and the C-2 Tier-0 positions survive this refresh intact — no finding contradicts them (§6.4), and the evidence lane (availability-truth, confirmation-truth, tamper-evident records) remains empty across every competitor surveyed, verified-by-absence (§3.6). What must re-price in class (iii): (1) the fragmentation row — controller spec-lag is compressing (leaders now 0–1 versions behind; Google is the sole deep laggard); (2) the explainability row — "nobody durably records why-it-didn't-fire" is now wrong in its absolute form for the error-class subset at HA; (3) the enforcement row — "no enforcement anywhere" must become the precise form: *no policy kernel anywhere; subtraction-fragments only.* Three clocks aged: SCITT-actuation (F-4), the HA (A)-half (F-3), Apple-September (F-2).

---

## §1 Charge 1 — Matter/Thread adoption state (delta vs the 2026-06-27 baseline)

Baseline: `context/assessments/2026-06-27_smart-home-ecosystem-currency_research-return.md` §1B/§1C + source rows C1-10..C1-16. Lens: Substrate Thesis §2.6 (ratification as starting gun) and §2.7 (commoditization pushes value up the stack — predict the landing zone).

### 1.1 Spec and certification state

No Matter 1.7; no new spec release since 1.6 (2026-06-17); CSA newsroom between Jun-17 and Aug-09 carries testimonials and reposts only ([VERIFIED] csa-iot.org/newsroom/, accessed 2026-08-09). "Unify 2026" post-event signal: CSA is explicitly expanding scope toward **commercial building automation and industrial IoT**, Product Security 1.1 now certifies whole systems ("mobile applications, gateways, Cloud services, and remote management infrastructure"), board expanded with ADT and Telink ([VERIFIED] embeddedcomputing.com, 2026-07-22, accessed 2026-08-09). One under-reported nuance: **the Matter 1.6 certification program was not finalized at release** — Silicon Labs' own 2.9.0-1.6 release notes (2026-06-25): "the Connectivity Standards Alliance (CSA) certification is not finalized for Matter 1.6 branch" ([VERIFIED] docs.silabs.com, accessed 2026-08-09). Whether it opened during Jul–Aug: UNVERIFIED.

### 1.2 Controller spec-lag — the baseline's "2–4 versions behind" is decaying

- Amazon: "Matter-enabled Echo devices now support the Matter 1.5 protocol" — March 2026 entry on Amazon's own what's-new page ([VERIFIED] developer.amazon.com/docs/alexaplus/smarthome/whats-new.html, re-fetched by the parent pass 2026-08-09). One behind, not 2–4.
- Samsung SmartThings: Matter 1.5 in production; **Matter 1.6 in hub-firmware beta since 2026-07-23**, GA reportedly late-Oct — ~4 months after spec ship ([REPORTED] Matter Alpha 2026-07-29; caveat: Samsung's own release notes do not mention it — vendor-unconfirmed).
- Home Assistant: **full Matter 1.6.0 in beta 26 days after spec release** — matter.js "0.17.5 (2026-07-13)… Upgraded to Matter specification version 1.6.0" ([VERIFIED] raw matter.js CHANGELOG, accessed 2026-08-09). The Jun-27 baseline's "rebuilt matter.js server" row has materialized its consequence: spec-version currency is becoming nearly free for any orchestrator built on it.
- Google: the stagnant outlier — Google Home developer Matter release notes last touched 2026-02-25; device types still Matter-1.2-vintage ([VERIFIED] developers.home.google.com/matter/release-notes, accessed 2026-08-09). Google's window energy went to Gemini for Home instead (§4).
- Joint Fabric (1.6's headline multi-admin feature): **no controller ships it** ([REPORTED] FixoryHQ 2026-06-24: "no major consumer ecosystem has confirmed full end-user Joint Fabric support"; corroborated by matter.js keeping provisional clusters feature-gated [VERIFIED]).

### 1.3 Fragmentation reality — pain current, remediation entering betas

Freshest in-window consumer-reality audit ([VERIFIED] apple.gadgethacks.com, pub. 2026-07-14 / updated 2026-08-03, accessed 2026-08-09): "The Matter badge now carries roughly the same weight as a 'works with…' platform sticker rather than a universal guarantee"; Apple Home "provides no logs, no debug tools, and no meaningful error messages when Thread pairing fails." Concurrently, real interop fixes are shipping to beta channels: SmartThings 62.x "expanded Thread unification" (joining other Thread networks without re-pairing), tvOS 27 Thread-1.4 credential sharing ([REPORTED] Matter Alpha). Per-vendor works-with programs are still growing, not dissolving — two new "Works with Home Assistant" partners in-window ([VERIFIED] home-assistant.io/blog index) — direct evidence the connectivity layer is not yet absorbed. **Counts discipline:** the baseline's "750+ certified" was matter-smarthome.de's own database; Unify coverage says "over 1,200 devices"; the CSA product search paginates to 1,130 pages with no total ([VERIFIED observation]). Three incompatible denominators — do not chart any of them as growth.

### 1.4 Thread

Thread 1.4 cert-floor holds; rollout progressing (tvOS 27, SmartThings 62.x, new TBR entrants — Ubiquiti's first Matter certification Jul-02 at 1.4 with TBR hardware "this quarter" [REPORTED]). NEW: the next Thread spec is signaled as **"Thread Direct"** (removing border-router dependency for initial setup), likely branded Thread 2.0, no timeline ([REPORTED] tuttotech.net 2026-06-23, citing a Verge interview with Thread Group's Anne Olivo). Thread Group's own press page shows nothing newer than 2022 — stale page vs. real silence UNVERIFIED. Single-chip Zigbee+Thread stays dead; the successor pattern is switchable-at-onboarding dual-stack (Aqara Power Plug H2, Jul-23 [VERIFIED via Matter Alpha]) — the baseline's "reserve Thread as a dedicated radio later" narrowing is reinforced.

### 1.5 Where value is relocating (§2.6/§2.7 lens)

The in-window release behavior of every major player is up-stack: Amazon's Smart Home AI Toolkit makes device-capability definition an AI-agent interaction ([VERIFIED]); HA's two in-window releases compete on orchestration and approachability, with no Matter/Thread/Zigbee headline content ([VERIFIED] release posts); SmartThings' 62.x firmware "focuses on reliability rather than new device controls," including automatic state reconciliation after offline periods ([REPORTED]) — a big-four vendor competing on state-consistency, exactly the landing zone the thesis predicts; the Open Home Foundation launched a community device database ("Wikipedia of smart home devices," public preview 2026-07-23 [VERIFIED]) — accountability-shaped infrastructure. Counter-reading, honestly: hub *hardware* remains an active battleground (Homey certifying, Ubiquiti entering, Aqara shipping) — the absorption arc is mid-flight, not complete; and if matter.js makes spec currency free for everyone, integration breadth commoditizes for us too — the defensible layer must genuinely be arbitration/reliability/accountability, never "we integrate more" [INFERRED].

### 1.6 Charge-1 claim rows

> **ROW C1-1:** "No Matter 1.7 announced; CSA runs Unify instead" · PRIOR: Jun-27 return §1B (C1-11) · FINDING: no 1.7 through Aug-09; Unify scope-expansion toward commercial/industrial ([VERIFIED] CSA newsroom; embeddedcomputing 07-22) · **VERDICT: CURRENT** · CONSEQUENCE: V1 Matter-deferral stays unpressured; CSA's commercial-buildings turn feeds the class-(iii) buildings narrative.

> **ROW C1-2:** "Platforms are 2–4 spec versions behind" · PRIOR: Jun-27 return §1B (C1-12) · FINDING: Amazon 1.5 ([VERIFIED] own docs, Mar-2026), SmartThings 1.5-prod/1.6-beta ([REPORTED] 07-29), HA full 1.6 beta in 26 days ([VERIFIED] matter.js changelog), Google alone at ~1.2-vintage ([VERIFIED]) · **VERDICT: MOVED** · CONSEQUENCE: re-price any fragmentation-flavored class-(iii) claim — the lag figure is stale; the durable form is "adoption uneven; Google lags; feature-exposure trails protocol support."

> **ROW C1-3:** "Matter interop is fragmented/painful in lived practice" · PRIOR: Jun-27 return §1B (C1-12) · FINDING: "Matter badge ≈ works-with sticker," no-logs-no-debug at Apple Home ([VERIFIED] 07-14/08-03); works-with programs still growing ([VERIFIED]) · **VERDICT: CURRENT** · CONSEQUENCE: the reliability/explainability wedge holds on current data.

> **ROW C1-4:** "Joint Fabric spec'd but unshipped" · PRIOR: Jun-27 return §1B (Matter 1.6 content) · FINDING: still no shipping controller ([REPORTED] + [VERIFIED] feature-gating) · **VERDICT: CURRENT** · CONSEQUENCE: multi-admin arbitration remains an open field — the arbitration leg of the up-stack claim is unclaimed at the platforms.

> **ROW C1-5:** "Thread 1.4 sole BR cert floor; credential sharing mandated" · PRIOR: Jun-27 return §1C (C1-14) · FINDING: holds; rollout progressing in betas; Ubiquiti enters at 1.4 · **VERDICT: CURRENT→MOVED (rollout)** · CONSEQUENCE: none for V1; seam posture unchanged.

> **ROW C1-6:** "Single-chip Zigbee+Thread multiprotocol dead; reserve Thread as dedicated radio" · PRIOR: Jun-27 return §1C (C1-15) · FINDING: switchable-not-concurrent is now the shipping industry pattern (Aqara H2, 07-23) · **VERDICT: CURRENT (pattern confirmed)** · CONSEQUENCE: the narrowed Thread-seam reservation stands verbatim.

> **ROW C1-7:** "750+ certified products / 38% HA-instance Matter share" · PRIOR: Jun-27 return §1B (C1-13) · FINDING: three incompatible count denominators (750/1,200/1,130-pages); no fresh HA-share measurement · **VERDICT: MOVED/AMBIGUOUS (counts), CURRENT-UNVERIFIED (share)** · CONSEQUENCE: strike absolute device-counts from any class-(iii) surface; they are unpriceable on present evidence.

> **ROW C1-8:** "Value relocates to orchestration · arbitration · reliability · accountability as the standard absorbs connectivity" · PRIOR: Substrate Thesis §2.7 [LIKELY] · FINDING: in-window release behavior of Amazon/HA/SmartThings/OHF is uniformly up-stack ([VERIFIED]/[REPORTED], §1.5); hub hardware still contested (counter-reading) · **VERDICT: MOVED (reinforced)** · CONSEQUENCE: §2.7's landing-zone prediction gains its strongest dated evidence cluster yet; cite this row when the charter prices the up-stack claim.

> **ROW C1-9 (NEW):** Thread Direct / "Thread 2.0" signaled, no timeline · PRIOR: none · FINDING: [REPORTED] 06-23 · **VERDICT: NEW** · CONSEQUENCE: watch-only; does not touch the narrowed seam.

---

## §2 Charge 2 — Home Assistant trajectory + commercial ecosystem

Baseline: Jun-27 return Cluster 2 + C2-1..C2-5; Jul-28 return §3.3. The §9.6 falsifier watch is explicit here.

### 2.1 The (A) half of the explainability moat — the baseline sentence is now partially CONTRADICTED

Verified at raw stable-tag source this lane (parent pass re-fetched raw.githubusercontent.com/home-assistant/core/2026.8.0/homeassistant/helpers/trigger.py, accessed 2026-08-09):

- Stable 2026.7.0 and 2026.8.0 contain a live `report_not_triggered` → `did_not_trigger(NotTriggeredInfo(...))` pipeline in the shared entity-trigger framework, wired into automations (`did_not_trigger=self._handle_not_triggered` in components/automation) [VERIFIED].
- **Exactly five reason codes exist**: `threshold_entity_not_found`, `threshold_unit_not_supported`, `threshold_value_not_numeric`, `entity_unit_not_supported`, `entity_value_not_numeric` — all *evaluation-error* classes [VERIFIED]. **A plain numeric non-match returns False and reports nothing** [VERIFIED at source]. The general "why didn't it match" case remains unshipped and, per discussion #3912 (no activity since 2026-06-24 [VERIFIED]), undesigned.
- Not-triggered traces persist across restarts but live in a **capped bucket exactly like run traces** (`LimitedSizeDict(size_limit=stored_traces)`, default 5, FIFO) [VERIFIED at source]. The structural distinction the Jun-27 return drew — capped/bucketed bolt-on vs. never-evicted pure projection — is intact and now demonstrable at their source.
- The feature shipped **unannounced**: neither the 2026.7 nor 2026.8 release post mentions it [VERIFIED both posts]. The UI PR (#52708) merged 2026-06-22 and presumptively shipped with 2026.7 [VERIFIED merge; shipping INFERRED].
- Negative movement on the adjacent surface: frontend #51742 (per-automation health/error summary in the picker) is **closed without merge** ([VERIFIED page-state, parent-pass re-fetch; close date not visible]).

### 2.2 The §9.6 audit/accountability/multi-tenancy test — negative again, with sharpened evidence

- "Minimal Security Audit Log" (architecture #1346, opened 2026-02-24, login-events-only): **still zero replies, zero maintainer engagement** [VERIFIED, accessed 2026-08-09].
- RBAC: maintainer position sharpened on the record — collaborator karwosts (2025-11-17): "In the livestream this month Frenck seems to have said pretty clearly that RBAC is not going to happen"; Frenck quoted: "It's a no for now." In-window community pressure: a commercial multi-tenant hosting use case posted 2026-07-11, no maintainer response [VERIFIED org discussion #22]. Third-party demand is being met by a core-patching HACS hack whose own README warns it may break on any update [VERIFIED github.com/SamAthanas/user-rbac].
- Architecture #740 (expected-state / confirmation semantics): last comment still 2025-05-29 [VERIFIED]. **No durable confirmed/unconfirmed/failed projection anywhere in HA — the (B) half of the moat is untouched.**
- Recorder DB remains mutable; no tamper-evidence work found anywhere in HA or the OHF public roadmap repo (which lists no security/permissions/audit items) [VERIFIED README; project-board items not fetched — gap].
- Lexical near-miss, logged for precision: 2026.8 shipped Z-Wave lock user-code management with "an audit log of every change" — **device-scoped credential history, not a system audit log** [VERIFIED release post]. First appearance of the phrase "audit log" in an HA release post; watch the phrase, not just the feature.

### 2.3 The adjacent-FOSS mover this window is openHAB, and it moved on authorization, not accountability

openHAB 5.2 (released 2026-07-05, parent-pass verified at openhab.org): item-level `voiceSystem` metadata with three access levels — "No Access, Read-Only, or Read-Write" — explicitly marketed: "incredibly simple to shield security-sensitive devices — like smart locks, garage doors, and alarm systems — from being accessed by the LLM"; plus an MCP server gated by user tokens where "different tools can be enabled or disabled, allowing for granular control over access to sensitive areas" [VERIFIED, accessed 2026-08-09]. No audit log, no RBAC, no multi-tenancy in the release [VERIFIED]. Classification under D5's layered form: this is a real, if coarse, deterministic floor for AI access (capability subtraction per item) — the FOSS field's first; it is not an accountability story, so §9.6 stays untriggered. openHAB's persistence remains architecturally lossy-by-design (rrd4j decimation; §3.3) — provenance without durability.

### 2.4 Cadence, governance, commercial

Releases on cadence (2026.7 Jul-01; 2026.8 Aug-05; 2026.8.1 Aug-07) [VERIFIED]. OHF window items: device database public preview (07-23), Plausible analytics adoption (07-29), and the **EC/DMA ruling (07-16) ordering Alphabet to open eleven Android features — "always-on wake word detection, ambient sensor access, and screen automation" — to competing assistants "on equal terms,"** with OHF's Android developer having "consulted directly with the European Commission" [VERIFIED home-assistant.io/blog/2026/07/31]. An OHF **AI Policy** (2026-07-20) governs *contributions*, not product: "Autonomous agents are not allowed to contribute" [VERIFIED developers.home-assistant.io]. Nabu Casa: no commercial news in-window (latest news item 2026-03-31) [VERIFIED nabucasa.com/news]. Works-with-HA added IoTorero (07-09) and FireAvert (07-28) [VERIFIED index]. Install-base signal: **664,467 active (opt-in) installations**, with HA's own caveat "we estimate that less than a fourth of all Home Assistant users opt in" ([VERIFIED] analytics.home-assistant.io, parent-pass re-fetch 2026-08-09). No credible third-party market-share estimate exists — searched, absent, stated loudly.

### 2.5 HA AI/LLM state

2026.8 adds model plumbing only (LiteLLM proxy, llama.cpp conversation agents, OpenAI integration to current models) [VERIFIED release post]. Entity-exposure allowlists remain HA's only AI enforcement — unchanged; no policy layer appeared [VERIFIED-absence across release posts + dev blog]. Philosophy row unchanged ("AI as a powerful tool…"), now reinforced at the governance layer by the contribution-scoped AI policy.

### 2.6 Charge-2 claim rows

> **ROW C2-1:** "HA's not-triggered traces are merged plumbing, in no stable release; no built-in trigger emits them" · PRIOR: Jun-27 return C2-1/C2-2 · FINDING: five evaluation-error emitters live in stable 2026.7.0/2026.8.0 ([VERIFIED] raw tag source, parent-pass re-fetch); plain non-match still unreported; unannounced · **VERDICT: CONTRADICTED (in its absolute form); the narrow claim "no general why-not" is CURRENT** · CONSEQUENCE: the differentiator copy must drop "unshipped in any stable release" NOW — the honest form is "error-class only, capped, no general case, no confirmation leg" (feeds C-2's parent position and the mid-Aug read).

> **ROW C2-2:** "Watch the 2026.7 line for per-trigger did_not_trigger emitters going stable" · PRIOR: Jun-27 return §0.1 watch-item · FINDING: fired, in the narrow sense · **VERDICT: MOVED (watch resolved)** · CONSEQUENCE: open the successor watch — non-error reason emitters, result-typed buckets (#3912 dormant), and any release-post announcement (the moment they *market* it, the DIY (A)-half closes loudly).

> **ROW C2-3:** "No durable confirmed/unconfirmed/failed projection anywhere; #740 dormant" · PRIOR: Jun-27 return C2-5 · FINDING: #740 last comment still 2025-05-29 ([VERIFIED]) · **VERDICT: CURRENT** · CONSEQUENCE: the (B) half — the confirmation leg — remains the durable class-(iii) differentiator; price it as the lead claim.

> **ROW C2-4:** "HA audit/RBAC/multi-tenancy dormant; §9.6 untriggered" · PRIOR: Jul-28 return §3.3 · FINDING: #1346 still zero maintainer replies; RBAC "a no for now"; in-window commercial multi-tenant ask unanswered; core-patching community hack carries the demand ([VERIFIED] ×3) · **VERDICT: CURRENT (sharpened)** · CONSEQUENCE: falsifier #6 stays DORMANT-not-dead; quarterly T6 watch cadence suffices (fits the A-14 floor).

> **ROW C2-5:** "HA traces capped (default 5), a bolt-on — not a never-evicted projection" · PRIOR: Jun-27 return Cluster 2 · FINDING: not-triggered bucket equally capped, FIFO ([VERIFIED at source]) · **VERDICT: CURRENT (now demonstrable at their source)** · CONSEQUENCE: "never-evicted as a structural property" survives as claim #2 in the class-(iii) ordering.

> **ROW C2-6 (NEW):** openHAB 5.2 ships item-level AI permissions + MCP tool ACLs (first FOSS AI-authorization floor) · PRIOR: none (Jul-28 return §3.3 ranked openHAB farthest) · FINDING: [VERIFIED] 2026-07-05 release · **VERDICT: NEW** · CONSEQUENCE: re-rank the FOSS race board (openHAB moved from farthest to first-on-authorization); the D5-layered read: a partial L1 fragment exists in FOSS — the accountability layer above it is still nobody's.

> **ROW C2-7:** "HA install base / commercial posture" · PRIOR: Jun-27/Jul-28 ecosystem rows · FINDING: 664,467 opt-in installs ([VERIFIED]); EC/DMA Android opening ([VERIFIED]); Nabu Casa quiet; two new works-with partners · **VERDICT: MOVED (additive)** · CONSEQUENCE: the DMA ruling is a distribution lever for FOSS assistants — feeds the READ's ecosystem-trajectory picture, not V1 scope.

> **ROW C2-8 (NEW):** HA ships "audit log" *phrase* (Z-Wave lock user-codes, device-scoped) · PRIOR: none · FINDING: [VERIFIED] 2026.8 post · **VERDICT: NEW (lexical near-miss)** · CONSEQUENCE: watch the language surface — if HA's copy starts using accountability vocabulary, the naming window for our class-(iii) claims shortens even while the architecture gap holds.

---

## §3 Charge 3 — The local-first competitor field

Baseline: Jun-27 return C2-9 ("Hubitat/SmartThings/openHAB/Homey: no durable why-not, no confirmation projection; troubleshooting remains ephemeral logs"); Jul-28 return §3.2/§3.3. Counter-positioning tested per-competitor per §2.3 — never globally. Comparative notes below are research notes only: counsel-gated, publish nowhere.

### 3.1 Hubitat

State: private, small (revenue ~$4.5M [REPORTED, snippet-grade — Kona Equity, unfetched]); no C-9; flagship remains C-8 Pro. Healthy release cadence: 2.4.4 (03-16, Matter 1.5 + BTHome), 2.5.0 (04-23), **2.5.1 (07-29, in-window): "Added model context protocol (local AI) integration with a companion AI Connector Integration app"** [VERIFIED community release thread, accessed 2026-08-09]. Evidence architecture confirmed ephemeral at the primary docs: "The hub has a size-based limit on past logs, around 1 MB… oldest logs being removed first" [VERIFIED docs2.hubitat.com]; staff: "The 'Event' history is pruned to 1000 entries per attribute per device as part of nightly maintenance" [VERIFIED community, staff post]; the 2.5.0 chart store is explicitly a 31-day/1000-value ring buffer [VERIFIED]. Repair culture is soft-reset + database restore [VERIFIED community thread 07-18] — a mutable-state platform to its bones. **Structural-copy test: PARTIAL barrier.** Cheap-eMMC hub economics + prune-by-design storage + mutable DB make a durable ordered evidence ledger a re-architecture, not a feature flag [INFERRED from verified retention design]. Honest counterpoint: nothing prevents incremental imitation (raised caps, an export projection), and they ship platform features fast (MCP within months of the wave).

### 3.2 Homey (Athom / LG 80%)

LG operates it as a parallel brand (no Homey mention in LG's CES-2026 AI-home messaging [VERIFIED lg.com]); distribution expanding (webOS TV app ~May-2026 [VERIFIED]). Hardware: Pro (2026) shipped Dec-2025; **June-2026 price hike (€399→€449) attributed by Athom to RAM/eMMC cost pass-through from Raspberry Pi** [VERIFIED homey.app news] — confirming Pi-CM-based hardware under margin pressure. In-window: **Matter 1.5 certified (~Jul-26)** across Pro/mini/Self-Hosted with built-in TBR and a reverse-bridge to all five majors [VERIFIED homey.app]. AI: the **ChatGPT app (Jun-2026) — "control devices, start Flows and Advanced Flows… rename devices… create and update Flows," account-linked, no published restrictions or confirmations** [VERIFIED homey.app]. Cloud reality: account, App Store, remote, push, ChatGPT and cloud-device apps all ride Athom cloud even on the "local" tiers [VERIFIED self-hosted product page]. Zero explainability/evidence features shipped in 2026. **Structural-copy test: WEAK-to-MODERATE — honestly the weakest barrier in the field.** No hardware/architecture blocker; the barrier is the "it just works" consumer brand (surfacing honest-UNKNOWN/unconfirmed/failed contradicts the polish that sells it) plus LG pointing its energy at AI-control/appliance synergy [INFERRED from verified release direction]. If honest-evidence proves market-valuable, Homey is the competitor most able to imitate its *surface* — likely as UX gloss without append-only substance.

### 3.3 openHAB

5.1 (2025-12-22) shipped **event source tracking** — command provenance in events/logs ("received command ON (source: …climate.rb:56)") [VERIFIED openhab.org blog] — the field's closest approach to "why-did." 5.2 (2026-07-05): the AI permission model + MCP server (§2.3), Chat UI, biggest-ever charting; 141 contributors / 3,082 commits [VERIFIED]. But: RBAC (openhab-core #3305) open since Jan-2023, status "Todo," no branches/PRs [VERIFIED github]; default persistence is rrd4j — "does not grow in size… The older the data is, the fewer values are available… cannot provide precise answers to all queries" [VERIFIED addon docs] — **lossy by design, the architectural opposite of an evidence ledger**; and 5.1 *deprecated* default persistence to stop databases filling. **Structural-copy test: MODERATE.** No canonical total order, no durable event log to chain; volunteer bandwidth demonstrably flows to visible UI/AI features over unglamorous evidence infrastructure (the RBAC precedent) — but zero economic moat against one motivated contributor shipping an "audit persistence" add-on, and source-tracking shows the community drifting toward provenance [INFERRED from verified record].

### 3.4 New entrants and retreats

- **One Raven** (launched 2026-07-07, $5M seed led by Fifth Wall; homebuilder channel; founders incl. Lucas Haldeman): "every device runs locally and keeps homeowner data on the home network"; "What happens inside the home should stay inside the home" [VERIFIED prnewswire]. Crowds the *local-first/privacy* lane through a channel we do not occupy (production homebuilders); **no audit/confirmation/availability-truth claims found** — the evidence lane stays ours on present data. Remote-access architecture unspecified; no teardown exists yet — UNVERIFIED local-vs-cloud reality.
- Local-first as *marketing* is commoditizing: Homey "operates locally… privacy-first" [VERIFIED], Aqara "Local control keeps your data inside your home network" while admitting notification automations "still require a cloud connection" [VERIFIED eu.aqara.com]. [INFERRED] Local-first alone no longer differentiates; the honest-evidence layer is where the field is empty.
- Retreats: no in-window shutdowns; the Wemo cloud shutdown (2026-01-31 — "Remote access? Gone… App updates? Finished," with HomeKit-configured units surviving precisely because HomeKit routes commands "through Apple's local network protocols" rather than the vendor cloud [VERIFIED techbuzz.ai]) remains the freshest brick-out exhibit; the running catalog (Insteon, Revolv, Wink, POP, Neato, Nest Secure) [VERIFIED howtogeek 04-22]. No local-first product found failing commercially — searched, absent.
- The field-wide wave: **all three competitors shipped LLM/MCP control planes in Jun–Jul 2026** (Hubitat MCP 2.5.1; openHAB MCP/Chat 5.2; Homey ChatGPT) — all control-plane, none evidence-plane [VERIFIED ×3]. (Plugin/cloud-radar implications belong to the LD return's board — noted as a delta, not re-surveyed.)

### 3.5 SmartThings (cross-reference only)

Not a local-first competitor and covered per-charge elsewhere (§1.2, §1.5, §4); the Jun-27 C2-9 row's SmartThings leg was not re-tested this lane — carried as NOT-REASSESSED.

### 3.6 The honesty/evidence lane across the field

**No competitor found marketing availability-truth, confirmation-truth, tamper-evident logs, or any honest-evidence concept** — searched explicitly ("tamper-evident"/"audit log" hub marketing, command-confirmation evidence, explainability positioning); only enterprise/SIEM and academic material surfaced [VERIFIED-by-absence; absence is inherently non-conclusive and is listed in the self-audit]. Nearest real features: openHAB source tracking (provenance, not confirmation), Hubitat "Matter logs for troubleshooting" (ephemeral), Homey Insights (consumer charts).

### 3.7 Charge-3 claim rows

> **ROW C3-1:** "Hubitat: no durable why-not, no confirmation projection, ephemeral logs" · PRIOR: Jun-27 return C2-9 · FINDING: retention design verified at primary docs (1MB rolling logs; 1000-events/attribute nightly prune; 31-day ring buffer); 2026 releases add MCP/AI, nothing evidence-grade ([VERIFIED]) · **VERDICT: CURRENT (strengthened at source)** · CONSEQUENCE: the per-competitor counter-position holds; barrier class = economics + installed flash + mutable DB (partial, not absolute).

> **ROW C3-2:** "openHAB: same" · PRIOR: Jun-27 return C2-9 · FINDING: 5.1 source tracking = partial why-did provenance ([VERIFIED]); rrd4j decimation and RBAC-at-Todo verified; no why-not, no confirmation record · **VERDICT: MOVED (provenance only; core claim stands)** · CONSEQUENCE: tighten class-(iii) wording from "nobody records causes" to "nobody keeps a durable, queryable record — provenance exists at openHAB, durability nowhere."

> **ROW C3-3:** "Homey: same" · PRIOR: Jun-27 return C2-9 · FINDING: 2026 = ChatGPT control, Matter 1.5 cert, TV apps, price hike; zero evidence features ([VERIFIED]) · **VERDICT: CURRENT** · CONSEQUENCE: weakest structural barrier in the field — if the honest-evidence position ships publicly, expect Homey-style surface imitation first; keep the append-only/tamper-evident substance in the claim language (D5-compliant, mechanism-first).

> **ROW C3-4 (NEW):** Field-wide LLM/MCP control-plane wave, Jun–Jul 2026, zero evidence-plane movement · PRIOR: none · FINDING: [VERIFIED ×3] · **VERDICT: NEW** · CONSEQUENCE: the field is wiring models to actuators faster than it is wiring evidence to anything — the exact asymmetry the north star names; feeds F-1.

> **ROW C3-5 (NEW):** One Raven stakes "local-first, out of the cloud" in the homebuilder channel ($5M, Fifth Wall) · PRIOR: none · FINDING: [VERIFIED] 07-07 · **VERDICT: NEW** · CONSEQUENCE: local-first-as-positioning is now contested; the class-(iii) surface should lead with evidence-truth, not locality (locality is the floor, not the claim).

> **ROW C3-6:** "Local-first demand is real and large" · PRIOR: Substrate Thesis §5 [PROVEN — held as NOTE by Jul-28 return §7.1] · FINDING: demand-side exhibits accumulate (Wemo brick-out, One Raven funding, Homey Self-Hosted SKU, Aqara privacy marketing) while the *wording* commoditizes ([VERIFIED] ×4) · **VERDICT: CURRENT (+caveat)** · CONSEQUENCE: unchanged ledger row; the caveat prices the claim, not the demand.

---

## §4 Charge 4 — Model-in-the-loop home products vs the enforce-vs-propose line

Baseline: Jul-28 return §3.1/§3.2 (platform scan) + §8.4 F-1 watch (recognition rule: enforcement/signature rooted OUTSIDE the agent stack; an actor signing/checking its own report never counts). Language law held throughout: the deterministic floor is MISSING from the field, not SUPERIOR; L2/L3 without L1 are unsound; L1 without L2 is insufficient.

### 4.1 The one-table state of the field (L0–L3 per Substrate Thesis §3.1)

| Product (Aug-09 2026 state) | What ships | Layer occupied | Deterministic floor between model and actuator? |
|---|---|---|---|
| Gemini for Home (US early access effectively open) | NL control + automation creation | L2/L3 + two L1 *fragments* | Partial-by-omission: security categories excluded ([VERIFIED] §4.4); "Help me create" save-gate for automations; everything else model→actuator ungated |
| Alexa+ (GA all-US since 02-04) + Smart Home AI Toolkit (Jul-26 dev preview) | Agentic device actions; NL capability authoring | L2/L3 | **N** — zero enforcement language across the agentic developer surface ([VERIFIED] §4.2) |
| Apple Siri-AI + home hub (announced; hub ~Sept-2026) | Dev beta only | Announced = strongest L1 candidate (OS-mediated typed App Intents; schemas declare "when they're safe to run") | Not shipped; verdict deferred to ~Sept-2026 ([VERIFIED] WWDC session; [REPORTED] hub timing) |
| Samsung Bixby "new brain" / AI Home | Rolling to appliances (~Mar-2026) | L2/L3 | **N** — no safety/permission/audit language found (again) [REPORTED + VERIFIED-absence] |
| LG ThinQ ON | GenAI hub, proactive autonomous actions | L2/L3 | **N** — "no explicit safety disclaimers, permission requests, or confirmation protocols" in launch material ([VERIFIED] PR) |
| Home Assistant | Entity-exposure allowlists + model plumbing | L1 fragment (coarse) + L2 | Partial: a real categorical floor, but visibility-subtraction only — no invariants, rates, reversibility classes, audit |
| Homey × ChatGPT | Full device/Flow control from ChatGPT | L2/L3 (+ OpenAI Apps-SDK confirmation *hints*) | **N/hint-partial**: confirmations keyed to developer-declared annotations ([VERIFIED] OpenAI docs: separate write tools so "ChatGPT can respect confirmation flows") — untrusted metadata, not a floor |
| Tuya TuyaClaw (03-24) | Cross digital/physical agent, 3,200+ skills | Install-time supply-chain gate + L2 | **N** — pre-install code vetting is not runtime actuation enforcement ([VERIFIED] launch coverage) |
| Josh.ai AI X OS (06-18) | AI-embedded whole-home OS | L2/L3 | **N** — no safety language in launch material ([VERIFIED]) |
| 1X NEO (production started 04-30; ships by EOY-2026) | Humanoid in homes; teleop in loop | L0 (soft body) + human teleop | **N** on the AI path — the "floor" is a human teleoperator: a labor arrangement, not an architecture ([VERIFIED] Forbes) |
| Figure 03 (announced 10-2025; home timeline unpublished) | — | L0 (foam, BMS) | **N** — no software behavioral-constraint layer described ([VERIFIED] figure.ai) |
| Matter 1.6 (substrate) | Thermostat "defer" heuristic; Aliro credentials | L0/L1 fragments | **N for agents** — no agent access-control concept in the spec ([VERIFIED] CSA announcement) |
| MCP spec rev 2026-07-28 (substrate) | Stateless core, header routing | Enforcement-*friendly* plumbing | **N** — "no mentions of signed tool results, receipts, attestation" ([VERIFIED] MCP blog) — F-1 recognition rule unmet |
| Gemini API Agent Hooks (substrate) | Pre-tool deny gate, runtime-enforced | **L1** | **Y within its runtime** — opt-in, developer-configured, enterprise, not Home ([VERIFIED] §4.5) |

**The Charge-4 sentence, D5-form:** nobody ships a deterministic enforcement floor between model output and home actuator; the only L1-class mechanisms in deployment are visibility subtraction (entity allowlists, category exclusions) — real categorical fragments, with no invariants, no rate limits, no reversibility classes, and no audit beneath the L2/L3 stories the platforms are actually shipping.

### 4.2 Falsifier arm 1 — the Amazon exhibit

Amazon's agentic what's-new page, parent-pass verified 2026-08-09: July 2026 — "Use the new Smart Home AI Toolkit (developer preview) to build custom smart home capabilities by chatting with the Alexa+ smart home agent or uploading a specification." The page contains **no mention of safety, confirmation, guardrails, PIN, restricted device categories, permissions, or audit** — answered as a direct yes/no against the fetched page [VERIFIED]. The WWA security-certification doc remains classic device hygiene (TLS, signed firmware) with nothing agentic [VERIFIED]. Alexa+ is GA to all US customers (02-04), free for Prime, with agentic smart-home among the headline uses [VERIFIED geekwire]. This is the cleanest condition-1-direction exhibit a platform has produced: agent reach expanding into device-capability *authoring* with no enforcement story attached.

### 4.3 Falsifier arm 1 — the incident-consequence record

The Tel Aviv University "Invitation Is All You Need" promptware attack (Black Hat, ~Aug-2025) hijacked a Gemini-driven home via a poisoned calendar invite and actuated "smart devices such as lights, shutters, and even a boiler," fired by an innocuous user word [VERIFIED techradar]. Consequence observed: Google "accelerated the rollout of new protections… added scrutiny for calendar events and extra confirmations for sensitive actions" — then expanded Gemini for Home toward open US access. **No recall, no regulatory action, no rollback found anywhere** [VERIFIED-absence, searched]. No real-world harm incident with market or regulatory consequence found for any LLM home agent, 2025–2026 [VERIFIED-absence]. One year on, a demonstrated actuation compromise was absorbed as a patch note. Stated per the unbiased-instrument law: **this is evidence FOR falsification condition 1** — the market is currently pricing enforcement near zero. The counterweights: (a) the mitigation WAS a consequence, just an internal one — the attack produced new confirmations, i.e., incident-driven L2-hardening; (b) the arm's full text requires *high-consequence* deployments — the platforms' category exclusions (§4.4) show they do not yet trust agents with the high-consequence classes at all, which is itself an admission that an enforcement floor is missing rather than unnecessary [INFERRED — this reading is the honest both-ways cut].

### 4.4 The exclusion-list datapoint (what platforms actually gate today)

Google (Community Specialist, parent-pass verified): "Gemini doesn't support security-related actions, such as unlocking a door or garage door… it blocks actions that could compromise home security" — with the suggested workaround being *reverting to classic Assistant*, which still supports PIN-gated security actions [VERIFIED googlenestcommunity]. Read precisely: a categorical, platform-rooted exclusion (an L1 fragment by subtraction), currently treated by users as a regression to be fixed — and no formal support-doc statement of the policy was found (UNVERIFIED as formal policy; the community-specialist statement is the best available primary). Google's "Help me create" automation flow has a real platform-enforced save-gate (the automation does not exist until the human saves it) [VERIFIED support doc] — a genuine L1 gate for automation *creation*, not live actuation.

### 4.5 Falsifier arm 2 — the near-misses that move the clock

1. **Gemini API "Agent Hooks"** ([VERIFIED] ai.google.dev, parent-pass re-fetch 2026-08-09): "If your pre-tool hook returns {"decision": "deny", …}, the runtime immediately cancels the tool call," with the model seeing the rejection reason and adapting. Deterministic, runtime-rooted, categorical — a true L1 deny gate shipped by a major vendor — currently opt-in, developer-configured, in the enterprise agent runtime, with no Home connection [VERIFIED: no smart-home mention in the doc]. The architectural read: the socket where a floor could go now exists at Google; flipping it toward Home APIs would be a condition-2 event. CANDIDATE (moat-watch, §7).
2. **Apple, ~Sept-2026**: rebuilt Siri announced at WWDC26 (dev testing now, user beta "later this year"); App Schemas declare "the actions your app supports, the parameters they require, and when they're safe to run," with confirmation-required classes [VERIFIED developer.apple.com session]; the home hub is reported finished and gated on Siri, targeted September 2026 [REPORTED macrumors]. OS-mediated typed intents with schema-level safety metadata is the strongest platform-enforced pattern announced by anyone — unshipped, scope-unconfirmed. **The single biggest dated arm-2 event risk.**
3. **OpenAI Apps SDK**: write-tool confirmation flows keyed to developer-declared annotations — the meta-platform gate over every home integration routed through ChatGPT (Homey today), resting on untrusted hints [VERIFIED].
4. **Protocol level**: MCP's 2026-07-28 revision ships no signed results/receipts ([VERIFIED] — F-1 recognition rule unmet); its stateless/header-routing turn is enforcement-*friendly* plumbing (gateways can police calls cheaply) [INFERRED]. A2A task-result signing: not found either way [INFERRED-absence].

### 4.6 Academic/startup claim-jumpers since Jul-31

**DreamGuard** (arXiv 2608.05695, submitted 2026-08-06): "proactive guardrail for LLM agents built around a risk-aware world model" [VERIFIED arxiv] — the newest guardrail is itself a world model, i.e., L2 research crowding into the judge layer while the floor stays unbuilt: the Jul-28 return's narrowed gap statement survives another month unclaimed. No new HearthNet-class home-actuation-lease work found for Aug-2026; no home-agent-safety startup surfaced (Product Hunt/YC sweeps; absence non-exhaustive). The home-actuation policy-kernel position remains unoccupied [VERIFIED-by-absence + INFERRED].

### 4.7 Charge-4 claim rows

> **ROW C4-1:** "No major platform ships an enforcement/confirmation layer for agentic home actuation" · PRIOR: Jul-28 return §3.2 · FINDING: holds at every shipping platform, now with sharper texture — subtraction fragments exist (Gemini security-category exclusion [VERIFIED]; HA allowlists), no policy kernel anywhere · **VERDICT: CURRENT (restate precisely: no kernel; fragments only)** · CONSEQUENCE: class-(iii) enforcement claims must use the fragments-aware form or a reviewer refutes them with the exclusion lists.

> **ROW C4-2:** "Alexa+ agentic surface carries no safety language" · PRIOR: Jul-28 return §3.2 · FINDING: strengthened — Smart Home AI Toolkit (Jul-2026) expands agentic reach into capability authoring, still zero safety/confirmation/audit language ([VERIFIED] parent-pass) · **VERDICT: CURRENT (strengthened; arm-1-grade)** · CONSEQUENCE: F-1 evidence; also the cleanest per-competitor counter-positioning exhibit for the accountability wedge (counsel-gated).

> **ROW C4-3:** "Apple: strongest environment-side enforcement pattern; nothing agentic shipped for home" · PRIOR: Jul-28 return §3.2 · FINDING: Siri-AI announced with schema-typed safety metadata; hub ~Sept-2026 ([VERIFIED]/[REPORTED]) · **VERDICT: CURRENT — with a dated tripwire attached** · CONSEQUENCE: name Sept-2026 in the charter's F-1/T6 watch as a re-adjudication trigger (arm-2 event risk).

> **ROW C4-4:** "Both §9 falsifier arms live; neither met" · PRIOR: Substrate Thesis §9.1/§9.2 · FINDING: arm 1 accumulating (Toolkit; promptware-without-consequence; Homey/Tuya), arm 2 near-misses (Agent Hooks; Apple pattern) — neither condition satisfied ([VERIFIED] corpus above) · **VERDICT: MOVED (both arms closer, neither triggered)** · CONSEQUENCE: the thesis stands, on notice — the charter should price class-(iii) claims to survive EITHER arm firing within 12 months.

> **ROW C4-5:** "The guardrail literature is model-judge-heavy; the floor unbuilt" · PRIOR: Jul-28 return §1.1 L9 (narrowed form) · FINDING: DreamGuard (08-06) is a world-model guardrail — L2 research continues crowding the judge layer ([VERIFIED]) · **VERDICT: CURRENT** · CONSEQUENCE: the narrowed gap sentence (actuation-boundary, unbypassable, deployed, attributed) survives; keep RoboGuard/HearthNet differentiation mandatory in any external use.

> **ROW C4-6 (NEW):** A major vendor ships a true deterministic pre-tool deny gate (Gemini Agent Hooks) — enterprise, not home · PRIOR: none · FINDING: [VERIFIED] 2026-08-09 · **VERDICT: NEW** · CONSEQUENCE: condition-2's plausible route is now visible (Google flips Hooks toward Home APIs); watch the Google Home developer surface for hook/policy vocabulary.

> **ROW C4-7 (NEW):** Home robots enter the actuation field with no software behavioral floor (1X NEO production, teleop-as-floor; Figure 03 physical-only safety story) · PRIOR: none · FINDING: [VERIFIED ×2] · **VERDICT: NEW** · CONSEQUENCE: the enforce-vs-propose framing generalizes beyond fixed-device homes — feeds the moat watch (§7), not V1.

> **ROW C4-8:** "MCP/A2A ship no externally-rooted result signing (F-1 recognition rule unmet)" · PRIOR: Jul-28 return §8.4(3) · FINDING: MCP 2026-07-28 major revision — no signatures/receipts ([VERIFIED]); A2A unchanged ([INFERRED-absence]) · **VERDICT: CURRENT** · CONSEQUENCE: the F-1 watch stands at quarterly cadence; the leading indicators (cMCP, Microsoft VCR) were not re-checked this lane — carried, not laundered.


---

## §5 Charge 5 — SHORT-clock delta ONLY (SCITT · 802.11bf)

Prior art of record: `context/assessments/2026-07-28_agent-substrate-research_return.md` §2.4 + §8.2, verified at primary source 2026-07-31. Nothing there is re-verified here; this section reports movement in the 2026-07-31 → 2026-08-09 window only. Absence-of-movement rows state what was checked.

### 5.1 SCITT

| Item | Jul-31 state | Aug-09 state | Delta |
|---|---|---|---|
| Architecture | RFC 9943 (Proposed Standard) | unchanged | NO MOVEMENT ([VERIFIED] datatracker WG documents page, 2026-08-09) |
| SCRAPI | RFC Ed Queue | still "RFC Ed Queue - In Progress" (draft -11) | NO MOVEMENT ([VERIFIED] same) |
| CCF receipts profile | Publication Requested | unchanged, with IESG | NO MOVEMENT ([VERIFIED] same) |
| Recharter | debated, unposted | charter-01 still the approved charter; no recharter text | NO MOVEMENT ([VERIFIED] WG about page) |
| Adoption calls | planned pre-IETF-127 | none issued through Aug-09 ([VERIFIED] mailarchive search "adoption") | NO MOVEMENT |
| IETF 127 planning | Nov-2026 | no session request/agenda visible yet | NO MOVEMENT (recheck ~Sept) |
| **Individual-draft corpus** | ~12 drafts incl. agent execution / IoT | **EXPANDED, direction: agent actuation + payments + physical-world receipts** | **MOVED** — see below |

The movement, dated: **draft-wilder-scitt-physical-site-engage-receipt-00** (Rob Wilder, Wilder Robotics, 2026-07-29; parent-pass verified at datatracker 2026-08-09): "A SCITT Profile for Physical-Site Engagement Receipts" — tamper-evident signed records of "an autonomous or human-directed physical engagement at a specific real-world site governed by a defined operating envelope"; five-artifact payload vocabulary (Site · Operator/Actor · Engagement Window and Envelope · TEE Attestation Evidence · …); the profile "explicitly does NOT claim that the engagement was safe, correct, or wise"; trust model requires that "no single party can unilaterally forge or repudiate a receipt" [VERIFIED]. Plus: **draft-hawkins-scitt-attested-agent-payment-00** (2026-08-05/06 — hardware-attested agent payment authorization registered on a transparency service) [VERIFIED datatracker]; draft-kamimura-scitt-refusal-events-03 rev (08-02) and draft-hillier-scitt-arp-02 rev (08-08) [VERIFIED listing-level only — contents not fetched]; a list message (Lawrence Reilly, 08-07) pitching three AI-agent behavior/safeguards-record drafts to the WG, explicitly not-yet-adoption-proposals [VERIFIED mailarchive]; and **NAESB — the North American Energy Standards Board — held a meeting on SCITT, flagged to the WG list 08-06** [VERIFIED mailarchive].

**What this means for the RR-W1 decision (input, not work order):** the Jul-28 return's §8.2 verdict was "the adjacent territory is being staked this quarter" with minimal position-holding acts (subscribe [S]; watch the repo [S]; respond to adoption calls / short individual draft [M]) and a decide-by of ~IETF 127. The Wilder draft is a robotics company filing *physical-engagement receipts* — the nearest-yet neighbor to an actuation-events profile, differentiated today by its site/industrial framing, TEE-attestation dependency, and explicit no-safety-claim scope (our substrate's differentiable content — totally-ordered household actuation evidence with confirmation semantics — is not what it claims) [INFERRED from verified abstract]. The clock read this lane files: **the "months, not years" window from the Jul-28 return is now "this quarter, not this year."** All named acts still fit the A-14 floor (S/M-class, weekend-compatible). The hub adjudicates; gate sovereignty absolute.

### 5.2 IEEE 802.11bf

| Item | Jul-31 state | Aug-09 state | Delta |
|---|---|---|---|
| Infineon AIROC ACW741x | sampling (Jan-2026) | still "upcoming" on Infineon's own promo page; explicit 11bf/CSI commitment language present; no production date | NO MOVEMENT ([VERIFIED] infineon.com/promo/acw741x, 2026-08-09) |
| Qualcomm | marketing-level only | **re-tested at primary source**: Dragonwing NPro A7 Product Brief (Rev C) contains zero occurrences of 802.11bf / Wi-Fi sensing / CSI | NO MOVEMENT — prior claim re-confirmed harder ([VERIFIED] docs.qualcomm.com PDF); NOTE: one secondary (pascalpiron.substack, 06-11) claims 2026 Dragonwing briefs list sensing — conflicts; other briefs unchecked (UNVERIFIED conflict, flagged) |
| Broadcom / MediaTek / NXP / Espressif | none | no 11bf-specific announcements in-window | NO MOVEMENT ([REPORTED] searches) |
| Consumer products citing 11bf | none | none found | NO MOVEMENT |
| Privacy semantics / consent frameworks | unclaimed | still unclaimed — no standards, regulatory, or vendor movement in-window | NO MOVEMENT ([INFERRED from absence across 4 searches]) |

Context surfaced that the Jul-31 pass may not have logged (pre-window; strengthens the "privacy layer unclaimed" read, left for L-E where it turns physics-positional): the Letter Ballot 272 record — a proposed secure-transmission mechanism for sensing failed because "the definition of sensing privacy is not clear and the group did not align on the characterization of privacy problem," and the published standard "includes no privacy protection for non-participating individuals, no consent framework, no opt-out" ([VERIFIED] pascalpiron.substack.com, pub. 2026-06-11); KIT researchers demonstrated 99.5%-accuracy person identification from unencrypted beamforming feedback and urged IEEE toward stronger safeguards ([VERIFIED] gizmodo 2026-05-25 — BFI, not 11bf-proper; the distinction matters and is preserved).

### 5.3 Charge-5 claim rows

> **ROW C5-1:** "SCITT WG state: SCRAPI in Ed Queue; CCF profile with IESG; recharter debated; adoption calls planned" · PRIOR: Jul-28 return §2.4/§8.2 · FINDING: all four unchanged through Aug-09 ([VERIFIED] datatracker + mailarchive) · **VERDICT: CURRENT** · CONSEQUENCE: none — the WG clock did not move; the *territory* clock did (next row).

> **ROW C5-2:** "The SCITT-adjacent territory (agent/physical-world evidence) is being staked this quarter" · PRIOR: Jul-28 return §8.2 · FINDING: physical-site engagement receipts (07-29, robotics company), attested agent payments (08-05), behavior-records pitch (08-07), NAESB engagement (08-06) ([VERIFIED ×4]) · **VERDICT: MOVED (accelerating)** · CONSEQUENCE: the RR-W1 hold-the-position decision should not assume the window survives to IETF 127 untouched; re-adjudicate at the charter, not in November.

> **ROW C5-3:** "802.11bf silicon: sampling, not shipping; Qualcomm marketing-level only" · PRIOR: Jul-28 return §2.4 · FINDING: Infineon still pre-production; Qualcomm absence re-confirmed at the product brief ([VERIFIED ×2]) · **VERDICT: CURRENT (re-confirmed at primary)** · CONSEQUENCE: the sensing clock stays real-but-not-gating; RR-W2 parking stands.

> **ROW C5-4:** "Wi-Fi-sensing privacy semantics unclaimed" · PRIOR: Substrate Thesis §7 Q9; Jul-28 return §8.2 · FINDING: no movement in-window; LB272/KIT context sharpens how *documented* the vacuum now is ([VERIFIED context]) · **VERDICT: CURRENT (better-evidenced)** · CONSEQUENCE: unchanged posture; the vacuum is now citable rather than merely observed.

> **ROW C5-5 (NEW):** An energy-sector standards body (NAESB) is engaging SCITT · PRIOR: none · FINDING: [VERIFIED] mailarchive 08-06 · **VERDICT: NEW** · CONSEQUENCE: early evidence SCITT rails may become sector-regulatory infrastructure beyond software supply chains — moat-watch candidate (§7), and a demand-side signal for the accountability thesis generally.

---

## §6 Cross-cutting adjudication surface (what the charter prices)

### 6.1 The three class-(iii) re-prices this return forces

1. **Fragmentation claims**: retire "platforms are 2–4 spec versions behind" (C1-2). Durable form: adoption is uneven, feature-exposure trails protocol support, Google lags deepest; interop pain is current but remediation is entering betas (C1-3, C1-5).
2. **Explainability claims**: retire every absolute of the form "no platform durably records why an automation didn't fire" (C2-1). Durable, priceable forms, in strength order: (i) the confirmation leg — no durable confirmed/unconfirmed/failed projection anywhere (C2-3, untouched since Jun-27); (ii) never-evicted-as-structural-property vs. capped bolt-on buckets (C2-5, now demonstrable at HA's own source); (iii) the unified tri-state in one durable artifact (HA has no path to the confirmation leg).
3. **Enforcement claims**: the D5-layered form now needs the fragments clause — the field ships L2/L3 stories plus *visibility-subtraction fragments* (category exclusions, entity allowlists, one enterprise deny-gate outside the home); the deterministic floor — invariants, rate limits, reversibility classes, attribution — remains missing from every shipping home product (C4-1..C4-6). Any external sentence omitting the fragments is refutable in one citation; any sentence framing the floor as superior violates the language law.

### 6.2 The dated tripwires this return proposes for the standing watches (all S-class, within the A-14 floor)

- **~Sept-2026 · Apple**: Siri-AI user beta + home hub — arm-2 re-adjudication trigger (C4-3).
- **HA release posts, monthly skim**: the moment not-triggered traces are *announced/marketed*, the DIY (A)-half closes loudly; also watch #3912 (result-typed buckets) and any successor to #51742 (C2-2).
- **SCITT list, existing subscription cadence**: adoption calls in the 126→127 window; any move of the Wilder/Hawkins class toward WG adoption (C5-2).
- **Google Home developer surface**: hook/policy vocabulary appearing = the Agent-Hooks-to-Home flip beginning (C4-6).

### 6.3 Moat-watch — logged as CANDIDATES only (the hub adopts; this lane watches)

- **CANDIDATE W-C1 (from C5-2):** SCITT physical-world receipts generalizing beyond the home — a robotics company just filed the pattern; attested agent payments and an energy-standards body are converging on the same rails. The company-scale lever: whoever holds a credible actuation-evidence profile holds it for every physical-AI domain at once. Source rows: §5.1.
- **CANDIDATE W-C2 (from C4-6):** the deny-gate socket at a hyperscaler (Gemini Agent Hooks) — if enforcement sockets become platform table-stakes, the differentiable layer moves to what the gate *consults* (policy, reversibility classes, evidence) — which compounds with, rather than competes against, model progress. Source: §4.5.
- **CANDIDATE W-C3 (from §1.1):** CSA's turn toward commercial buildings/industrial + whole-system security certification (Product Security 1.1) — accountability-as-certification forming a market adjacent to ours; a certification regime is a future carrier for enforcement/evidence requirements. Source: embeddedcomputing 07-22 [VERIFIED].
- **CANDIDATE W-C4 (from C2-7):** the EC/DMA Android ruling — regulation prying open OS chokepoints for third-party assistants; the template (regulated access to platform primitives "on equal terms") is a company-scale lever wherever a platform gate blocks the accountability layer. Source: HA blog 07-31 [VERIFIED].
- **CANDIDATE W-C5 (from C3-4/C4-7):** the field wires models to actuators (hubs, appliances, humanoids) faster than it wires evidence to anything — the asymmetry is domain-general; every new actuation surface without a floor is future demand for one. Sources: §3.4, §4.1.

### 6.4 The C-2 Tier-0 contradiction check (owed loudly, per the brief's hazards)

**No finding contradicts the ACCEPTED C-2 Tier-0 positions.** Specifically: (a) no surveyed platform or competitor ships availability-truth for battery/sleepy devices or markets anything adjacent to it (§3.6, verified-by-absence); (b) no durable confirmation projection appeared anywhere (C2-3; #740 dormant); (c) openHAB's source tracking is command *provenance*, not confirmation truth — it does not touch the confirmed-means-device-report reading; (d) nothing surfaced that would force retraction of any Tier-0 sayable sentence. The fenced claims themselves are not restated here, and no delivery-proof-adjacent claim is made anywhere in this return.

### 6.5 Division-of-labor notes

802.11bf appears here strictly as a clock-delta (Charge 5's mandate); its physics-positioning meaning is L-E's to analyze — where L-E's §4 competitive scan overlaps rows C1-8/C4-7, this return owns the adoption/commercial reading and defers the physics reading. The competitor MCP wave (C3-4) and Espressif's ESP RainMaker Neo (an AWS-powered open-source device-cloud, 08-05 [REPORTED — Matter Alpha index, headline-level]) touch the LD platform-horizon board — reported here as deltas for the LD trigger set (T-3′/T-6 class), not re-surveyed.

---

## §7 Self-audit (return integrity, per brief §2)

### 7.1 Sources actually read

**Corpus (all read in the brief's order, in full):** the Jun-27 ecosystem-currency baseline · Substrate_Thesis_v0.md (§2/§9/§10/§11 as lenses; §11 precedence held) · the Jul-28 agent-substrate return (in full, incl. §8) · the LD platform-horizon return (§0 method + §1–§5 structure at header depth — read for coverage boundaries per its delta-only hazard; not re-derived) · the north star · the moat-watch standing directive (W-1/W-2/W-3) · the A-14 attended-hours input · C-2 Tier-0 (ACCEPTED draft). **Access note:** the Jun-27 baseline is hardlinked on disk; the device bridge refused the original path and it was read via a byte-identical copy staged to `_scratch/wmarket_stage/` (32,742 bytes; content unaffected; the copy is disclosed here as the lane's only filesystem side-effect beyond this return).
**Web:** ~90 URLs fetched across five research passes; every URL is cited inline at point of use with access date 2026-08-09. Parent verification pass independently re-fetched the eight highest-stakes primaries: HA raw tag source (trigger.py @2026.8.0), the Wilder SCITT draft, openHAB 5.2 blog, Amazon what's-new, Gemini Agent Hooks doc, the Google security-exclusion thread, analytics.home-assistant.io, HA frontend #51742.

### 7.2 Every UNVERIFIED claim in one place

1. Matter certified-product totals — three incompatible denominators; no official count (C1-7).
2. connectedhomeip official 1.6 SDK tag — GitHub releases fetch returned incoherent dates; unresolved.
3. Thread Group formal activity since Jun-27 — press page shows nothing post-2022; stale-page vs. silence undecidable.
4. SmartThings Matter-1.6 hub beta — single specialist outlet (Matter Alpha); Samsung's own notes silent; vendor-unconfirmed.
5. Whether the Matter 1.6 certification program opened after Silabs' Jun-25 "not finalized" note.
6. HA frontend #51742 close *date* (closed-without-merge state verified twice; date not visible; GitHub API 403'd).
7. HA AI-Tasks adoption numbers (analytics data endpoints 403/JS-rendered).
8. Hubitat ownership/revenue/headcount ($4.5M is snippet-grade); Alexa/Google ongoing cloud-relay [INFERRED]; absence of any confirmation-record behavior [INFERRED, not re-verified].
9. One Raven's actual local-vs-cloud architecture (launch coverage only; no teardown exists).
10. Samsung Bixby "new brain" rollout — secondary sources only (primary robots-blocked).
11. Google's security-category exclusion as *formal policy* — best primary is a Community-Specialist statement; no support-doc found.
12. A2A task-result signing absence — inferred from absence, not shown either way.
13. Qualcomm sensing conflict — one secondary claims 2026 Dragonwing briefs list sensing; the one brief checked directly contains none; other briefs unchecked.
14. SCITT mailarchive coverage gap — pagination limited exhaustive enumeration of 07-31→08-05 messages (the targeted adoption-call search covered the full window).
15. Joint-Fabric non-shipping — rests on secondary statements + feature-gating evidence; no vendor/CSA timeline statement either way.
16. HA "38% Matter share" delta and any third-party market-share estimate — no fresh data exists.
17. Frontend #52708 shipping *in* 2026.7 — merge verified; inclusion in the release cut is [INFERRED] from dates.

### 7.3 The three weakest claims in this return

1. **The F-1 (arm-1) direction call.** It rests substantially on absence evidence — no safety language in docs, no consequence found — and absence is the weakest evidence class this return uses. A platform could hold unpublished enforcement internals; "no consequence" could be one lawsuit away from wrong. The claim is framed as direction-not-conclusion for exactly this reason.
2. **"The evidence lane is empty across the field" (C3, §3.6).** Verified-by-absence across named searches; a competitor could be marketing evidence-truth in a channel (installer/CEDIA, non-English markets) the sweep did not reach.
3. **The controller spec-lag compression row (C1-2).** The SmartThings leg is single-outlet and vendor-unconfirmed; the Amazon leg conflicts with practitioner reports in a way this return resolves by trusting the primary doc ("protocol support ≠ feature exposure") — that resolution is itself [INFERRED].

### 7.4 What a hostile reviewer attacks first

The verified-by-absence pattern (§3.6, §4.2, §4.3): three of the four headline findings lean on "we looked and it is not there." The defenses built in: every absence names what was searched and where; the two falsifier arms are stated as direction-with-counterweights, never as fired; and the single most damaging *positive* claim against our own copy (HA's emitters in stable — the one place this return contradicts our own baseline) was verified at raw tag source rather than taken from any secondary. Second attack: subagent single-fetch provenance — most body-level [VERIFIED] tags ride one fetch by one research pass; the mitigation is the parent re-fetch of everything falsifier-class or headline-grade, disclosed in §7.1. Third attack: Matter Alpha concentration risk in Charge 1 (four load-bearing rows cite it); mitigated where possible with primary corroboration (matter.js changelog, Amazon docs, Silabs notes), flagged where not (UNVERIFIED #4).

---

*Return complete. Filed 2026-08-09 at `context/research/2026-08-09_WMARKET_market-currency_return.md` — the lane's only write. The hub adjudicates the consumer at intake (ahead of the Aug-11 09:00 skeleton window, this consumes as a NAMED input to the charter SKELETON and S-10). Nothing here moves pre-freeze code; nothing here publishes; comparative rows inherit the counsel gate; the moat-watch rows are CANDIDATES for the hub, not adoptions.*
