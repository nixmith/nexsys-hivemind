<!--
file: context/strategy/2026-09-05_post-MVP-horizon_strategy-card-INPUT.md
purpose: THE BEYOND INPUT — docket Row 26 (STRAT-BEYOND-MVP), fired by Nick's word `BEYOND: at-C-002` (09-04). The post-MVP (P4+) horizon as a strategy-card INPUT: the candidate rows the hub actually believes in, each with its dependency graph, the measurement that would mint its claim, the fence it needs, and what NOT to build and why. Launch-dated rows stay SLOTS pending Erik's opinion. The D5 language law throughout (the deterministic floor is MISSING from the field, not superior to it). An INPUT to a sitting, never a ruling — nothing here adopts until Nick's words.
audience: Nick (the sitting) · the hub (carries the questions) · the v65+ hubs
state-type: strategy INPUT (hub-authored; the sitting's words are recorded elsewhere — the ruling-record pattern of context/strategy/2026-09-04_R10-sitting_THE-WORDS_ruling-record.md)
status: INPUT, v64 beat 3 (Sat 2026-09-05, 14:06 CT = 19:06Z). Read-set: strategy v1.2 whole · the north star (Problem 2 → the open questions) · the Substrate Thesis §1 + §3.1 · the claim register · the docket rows 17–34 · the FIX-1 grounding (the four silent drop points; the corpus 0/38 on the desk). Nothing below is a public sentence; every candidate claim is written in the register's grammar so that, IF minted, it is already fenced.
-->

# THE BEYOND INPUT — the post-MVP horizon, as rows a sitting can rule on

## §0 How to read this
This is not a plan and not a ruling. It is the hub's best argument for what the company builds AFTER the Nov-25 runway is reached with a product, a name, a surface and a fleet story that are all evidence-backed (v1.2 §2, P3's exit) — written as ROWS, because that is the only form Nick can rule on in one word each, and because a row carries its own refutable-by. Each row states: **the claim it would mint** (in the register's D5 grammar — a sentence with a scope fence and a falsifier, never an adjective) · **what it stands on** (the dependency graph — which earlier rows and which P0–P3 gates) · **the measurement that would mint it** (an instrument, a place it runs, a number) · **the fence it needs before anything public** · **what it deliberately does NOT build**. The rows are ordered by what COMPOUNDS — what makes every later row cheaper or more credible — not by what is most exciting. §5 lists the questions the sitting must answer; none is answered here. §6 names the one horizon-3 word already on Nick's desk that this document depends on.

**The frame in three sentences (nothing new; all banked):** the Thesis's bet is that anything built *underneath* the model — enforcing, attributing and bounding what it proposes — is made MORE valuable by every model improvement (Substrate Thesis §1). The north star's one line is *the harness enforces; the model only proposes*: the strongest guarantee is that the worst outcome of a bad inference is a REJECTED ACTION, never an unsafe physical state. And the D5 law: the deterministic floor is MISSING from the field (the embodied-safety literature converges on models judging plans before execution, trends away from runtime enforcement, benchmarks in simulation), not superior to it — L1 without L2 is insufficient; L2/L3 without L1 is unsound. P4 is where the company builds the missing floor as a product surface. Everything below is that, and only that.

## §1 What P0–P3 will have proven by the runway — the ground every row stands on
By Nov-25 (gates, not dates): **C-001** the packaged artifact installs/boots/runs the real integration (LIVE, narrow) · **C-002** one rejoiner adopted + one automation the device CONFIRMED on the shipped build (LIVE, standing) · **C-003** the six-device fleet re-adopted on the shipped artifact (the slot behind F-R4-1b + R-4c) · the explain surface honest (§10-G/§10-J; CG-1/2/3 + the FE fast-follow; "did it actually confirm" from the log) · the bus's silent drops made visible and retried (FAILCHAN-FIX-1; OR-BUS-SILENT-DROP closing on the passive instrument) · the nightly floor 8/9 with the settle redesign (R-5; the s31 fence lifted by its own proof) · Tier 2 + the curated fleet v1 · the corpus PUBLIC with its verdicts (B-6, post-R-10) · the LICENSE flip with the rename in-tree · the presence dataset begun in Nick's home + 3–5 others (four metrics, four-qualifier sentences) · the privacy posture a ratified surface before any beta intake (E-4). **What will NOT exist yet, and the rows below must not assume:** any agent proposer in the loop · any principal model beyond the API token store's scopes · any risk-class metadata on the device model · any measured statement about the bus under scheduling pressure · a hash-chain the log can PROVE (see Q1 — the north star says "hash-chained"; the hub has not verified it at source and orders that read before any accountability row is worded).

## §2 The candidate rows (the ones the hub believes in), in compounding order

### B-1 — THE DELIVERY GUARANTEE (the bus's first measured sentence)
**The claim it would mint (D5 form):** *"On commit X, on the bench card under scheduling pressure of shape S for N nights, every event published to the log was delivered to every LIVE subscriber whose filter matched it, in log order, at least once, with zero silent losses — every drop point emitted a `DeliveryAnomaly`, every retry either delivered or SUSPENDED the subscriber honestly (`LIVE_READ_EXHAUSTED`), and no checkpoint ever advanced past an undelivered matching position."* Scope fence: at-least-once + ordered per subscriber — NOT exactly-once (the checkpoint model already implies idempotent consumers: a crash between delivery and the checkpoint write redelivers on restart — a design fact to state, not a new property), NOT under a shape the card was never measured on, NOT a distributed claim. Refutable-by: one `LIVE_READ_EXHAUSTED` or one position-census miss in the measured window.
**What it stands on:** FIX-1b landed (DP-2 retry-then-SUSPEND; the four emission sites; the `bus.delivery_anomaly` WARN) · the passive instrument (rule R2: the token absent across 20 ordinary `main` runs) · **R-5** (the nightly is HANDS OFF until then — this row cannot touch the card's nightly before the settle redesign lifts the fence by its own proof) · the census instrument: a position census over the log + the checkpoint store (every published position × every matching subscriber → delivered? — derivable from the event store and the checkpoint store — the in-memory one in the ITs, the persistent one on the card; a bench verb, not a Core change).
**The measurement that would mint it:** the bench's nightly gains ONE row — `bus-delivery-under-pressure` — which runs the two ITs (HeroLoop · ReplayIT) ×K on the Pi itself under a load shape the card can produce (the Pi IS the slow, pre-empted machine the desk could not imitate at v64 beat 2 — 0 RED in 38 on a 24-core box pinned to two cores), tails the tokens, and runs the position census. N nights × K runs, zero anomalies of kind EXHAUSTED, census exact → the sentence. The loops become a permanent instrument, not a one-weekend spike.
**The fence it needs:** `FENCE-BUS: add` on the register NOW — no claim of delivery completeness until this row's measurement exists (the word is on Nick's desk; §6). Nothing public about the bus before the sentence.
**What it does NOT build:** exactly-once semantics · a persistent DLQ overflow (M3.5b's deferral stands until a measurement demands it) · a distributed or multi-process bus · any change to AMD-43's seven locked metrics (the anomaly stays a typed signal routed to one WARN).
**Why first:** every later row is an ENFORCEMENT layer on this bus. A policy kernel on a bus that can silently drop a `command_issued` is not categorical; it is probabilistic with extra steps. B-1 is the floor's floor.

### B-2 — THE POLICY KERNEL AT THE ACTUATION BOUNDARY (L1 as a product surface)
**The claim it would mint:** *"On commit X, every actuation on the bench card passed through one deterministic kernel at the single-writer chokepoint; for the enumerated policy classes {capability, device-invariant, rate, reversibility-class} the kernel REJECTED every violating proposal with an attributed `command_rejected` event carrying the rule id, and admitted every conforming one — N/N on the adversarial bench row, zero bypasses, zero model in the loop."* Scope fence: the enumerated classes only; "rejected action, never unsafe state" for THOSE classes; nothing about semantic appropriateness (L2). Refutable-by: one admitted violation, or one actuation path that does not traverse the kernel (a second writer).
**What it stands on:** B-1 (a kernel on a lossy bus is not a kernel) · the four-phase command lifecycle (exists: `accepted → dispatched → acknowledged → confirmed`; the kernel sits before `accepted`) · the single-writer total order (exists — the chokepoint the north star names) · **a principal model** — who is proposing? The seed exists: `OpaqueTokenStore`'s scoped tokens (`scopes`, `siteId`, `fullAccess`) already distinguish callers at the REST boundary; a principal is a token identity extended with a capability grammar ("may read these sensors, may actuate these entities, within these bounds") · **risk-class metadata on the device model** — does NOT exist; a Doc 02 amendment (an `irreversibility`/`riskClass` component on the capability or entity model — the formal AMD path, Phase-2 work) · **a rate primitive** — the command pipeline has supersession; a per-principal/per-entity rate window is new.
**The measurement that would mint it:** an adversarial bench row: a scripted proposer with a scoped principal issues a matrix of proposals (in-capability · out-of-capability · invariant-violating · rate-exceeding · irreversible-without-confirmation); the card's log must show the exact rejected/admitted partition the matrix predicts, each rejection attributed. Shadow-mode (B-3) is the natural first proposer.
**The fence it needs:** no "safe"/"secure"/"guardrail" adjective anywhere; the register sentence names the classes. No public mention of "AI safety" positioning before the kernel has one bench row green — the field's crowded lane is L2, and a claim there would be read as a claim we cannot cash.
**What it does NOT build:** L2 semantic judgment (a model judging whether a plan is "appropriate" — the field's default; not our layer) · L3 · any policy expressed in natural language · a policy DSL richer than the four classes · arbitration between principals (the open research question; a row of its own AFTER two principals exist).
**Why second:** it is the north star's core claim made measurable, and its cost is mostly Phase-2 design (the AMD for risk classes; the principal grammar) that the sitting can charter without a line of P4 code.

### B-3 — SHADOW MODE + THE PROPOSAL EVENT (agents propose; nothing actuates)
**The claim it would mint:** *"On commit X, a principal in shadow mode proposed N actions against the live event stream of the held card over D days; zero of them actuated (a census of `command_issued` by principal = 0); every proposal, its adjudication and its counterfactual outcome are in the log as causally-linked events."* Refutable-by: one `command_issued` attributed to a shadow principal.
**What it stands on:** B-2's event vocabulary (`action_proposed` → `proposal_adjudicated` → `command_issued` | `command_rejected`) — the proposal is an EVENT, so shadow mode is a policy ("adjudicate, never issue") not a code path · a proposer seam whose FIRST implementation is a rules-compiled proposer (the existing automation engine wearing a principal identity) and whose second is a LOCAL model — never a cloud one (zero cloud dependence is a register sentence) · the token store's identity for the principal.
**The measurement:** D days on the held card; the proposal corpus vs what the deterministic automations actually did; the zero-actuation census.
**The fence:** no agent actuates before B-2's bench row is green; the shadow corpus is not public until the privacy posture (E-4) covers proposal events (they describe the household's state as richly as the state events do).
**What it does NOT build:** any actuation from a model · a cloud LLM · an "assistant" front-end.
**Why:** it is the trust-building onboarding path AND the continuous zero-risk evaluation harness — the thing the benchmark literature does not have — and it costs nothing physical.

### B-4 — COUNTERFACTUAL REPLAY (the evaluation harness against recorded reality)
**The claim:** *"A recorded day from the held card replayed twice through the same agent-under-test produced byte-identical proposal streams (determinism), and a different agent-under-test's stream against the same day is a comparable, attributable record."* Refutable-by: a byte difference between two replays of one agent.
**Stands on:** replay determinism (exists: COLD→REPLAY→TRANSITION→LIVE — and B-1's guarantee that REPLAY delivers everything) · B-3's proposal events · the log as dataset · injected clocks throughout (LTD-09 — the reason this is even possible).
**Measurement:** the bench's replay verb over a captured day; two runs; `cmp` on the proposal streams.
**Fence:** no recorded day leaves a home before E-4's anonymization surface is ratified and applied; the first corpus is Nick's own home only.
**Does NOT build:** a simulator (the field has those); a synthetic benchmark.

### B-5 — THE PRESENCE-QUALITY CORPUS (P3's dataset, generalized)
**The claim (per home, per device, per metric — four-qualifier sentences only):** *"In home H, device D, over W weeks: latency-to-detect p50/p95 = …, latency-to-clear = …, false-clear-while-stationary = …/day, false-hold-after-vacancy = …/day — measured by the bench's presence verbs against ground truth G."* Refutable-by: the ground-truth method's own error bar.
**Stands on:** Tier 2 + the fleet (P3) · the presence sensors admitted as profiles with verdicts (B-6's gate) · E-4 · the FOP §1 benchmark design · the Matter 1.6 ambient-sensing clusters watch row (being in the room, v1.2 §4).
**Measurement:** the four metrics in Nick's home + 3–5 others; the ground-truth instrument named per home.
**Fence:** never "presence detection works"; never a cross-home average before N homes ≥ the number the register's statistician-of-one can defend (a question for the sitting, Q6).
**Does NOT build:** a proprietary presence algorithm (the corpus is the asset; algorithms are commodity and will be commoditized further by models — the Thesis) · a cloud aggregation.

### B-6 — THE VERDICT CORPUS AS THE COMMUNITY WEDGE, OPENED (P3's B-6 → contributions)
**The claim:** *"Device profile P, contributed externally, was admitted through the bench's profile-admission gate on commit X and published with its verdict (`confirmed|unconfirmed`, never rounded up)."* One, measured; then a count.
**Stands on:** the LICENSE flip landed with the rename (one launch moment; S-1: no wedge date spoken before the flip date is scheduled) · the curated fleet v1 · the profile-admission gate as a bench verb · the explain surface as the demo (R-10's condition) · E-4.
**Measurement:** the first external profile through the gate; the verdict published; the contributor's PR merged under the flip's license.
**Fence:** no un-benched profile ever labelled "supported"; no marketplace language; no SDK before the corpus has users (A-2 — code enters only at the rung that fences it).
**Does NOT build:** a plugin marketplace · a code SDK (its own docket row when there are users to serve) · a forum before the demo can be the demo.

### B-7 — THE ACCOUNTABILITY RECORD (integrity, stated only as far as it is proven)
**The claim (CONDITIONAL on Q1):** *"On commit X, the card's event log carries a hash chain an independent verifier recomputed end-to-end and matched; every actuation is attributable to a principal and a causal chain by graph traversal."* Refutable-by: one recomputation mismatch, or one actuation without a principal.
**Stands on:** **Q1 — is the log hash-chained today?** The north star says "immutable, causally-linked, hash-chained"; the hub has NOT verified it at source and will not word this row until it has (the unmeasured-hop gate, law #19). If it is not, the chain is a Doc 04 amendment before any row · B-2's principals · B-3's proposal events.
**Measurement:** an independent recomputation tool (not the product) over a card's log.
**Fence:** the EU AI Act Art. 12 shadow is a WATCH row, never a claim — the statute mandates logging and is silent on integrity; we say "integrity demonstrable", never "compliant". A-1b (the conformity path from 2027-01-20) is a company-horizon fact, not a product sentence.
**Does NOT build:** a compliance product; a certification story.

### B-8 — GRACEFUL DEGRADATION (the D5 layered form as a runtime property)
**The claim:** *"With the proposer killed / stalled / returning garbage for D hours on the held card, every deterministic automation continued to fire and confirm as before (the C-002 sentence unchanged) and the four household goals were unaffected."* Refutable-by: one deterministic automation whose behavior changed while the proposer was down.
**Stands on:** B-3 (a proposer to kill) · the deterministic floor as it exists today · the bench's power-harness primitive (P-1 — a self-confirming mains switch is exactly the instrument that kills a proposer host honestly).
**Measurement:** a bench row: kill the proposer; run the hero loop; compare.
**Fence / Does NOT build:** none new; this is the floor proving it is a floor.

### The launch-dated SLOTS (pending Erik's written opinion; the hard stop 09-18; the 10-31 rename-slip fallback)
S-1 the public name on every P4 surface · S-2 the community front's opening date (after the flip date is scheduled) · S-3 the first external mention of the agent layer (after B-2's bench row is green AND the name is cleared). Each stays a slot; the rows above are written token-parameterized so none waits on the name to be BUILT.

## §3 The dependency graph (what waits on what)
```
FIX-1b (landed, green) ─→ OR-BUS-SILENT-DROP closes (passive, 20 runs) ─┐
R-5 (the nightly fence lifts by its own proof) ────────────────────────────┴→ B-1 DELIVERY GUARANTEE (the bench row) ─→ B-2 POLICY KERNEL ─→ B-3 SHADOW MODE ─→ B-4 COUNTERFACTUAL REPLAY
                                                                                              (needs: Doc 02 AMD risk classes · principal grammar)   └→ B-8 GRACEFUL DEGRADATION (needs P-1)
Tier 2 + the fleet (P3) ─→ B-6 CORPUS OPENED (needs the LICENSE flip + E-4) ─→ B-5 PRESENCE CORPUS (needs E-4 + the ground-truth instrument)
Q1 (hash chain at source?) ─→ [Doc 04 AMD if absent] ─→ B-7 ACCOUNTABILITY (needs B-2 principals + B-3 events)
Erik's opinion ─→ S-1 · S-2 · S-3 (slots)
```
**The critical chain is B-1 → B-2 → B-3.** Everything the north star promises about agents stands on a bus that never silently drops and a kernel that cannot be routed around; both are measurable on hardware the company already owns, and both are Phase-2-heavy (design + AMDs) — the kind of work a one-founder company can do at a 15 h/wk floor while the fleet grows.

## §4 What NOT to build, and why (each is a fence, not advice)
- **Not L2.** A model that judges plans before execution is the field's crowded, model-dependent lane; it is obsoleted by the next model (the Thesis's corollary) and it is not MISSING. Our layer is underneath it.
- **Not a cloud dependency of any kind** — zero cloud dependence is a register sentence; a cloud LLM proposer would falsify it.
- **Not a simulator or a synthetic benchmark** — the field has those; the thing it lacks is recorded reality (B-4).
- **Not a proprietary presence algorithm** — the corpus compounds; the algorithm commoditizes.
- **Not a marketplace, an SDK, or a community front before their gates** (A-2 · S-1 · R-10 · E-4) — a front opened before its gate produces un-backed words or un-audited work.
- **Not a second product front before Tier 2 lands** (v1.2 §5).
- **Not a policy language.** Four classes, enumerated, measured. A DSL is a product the company would have to support before the floor is proven.
- **Not any adjective.** "Safe", "secure", "compliant", "guardrail" — the register's grammar is sentences with falsifiers; the brand IS the honesty made legible (v1.2 §0).
- **Not arbitration between principals yet** — a real research question (the north star's list); it needs two principals to exist first.

## §5 The questions for the sitting (listed; none answered here)
- **Q1** Is the event log hash-chained today, at source (Doc 04 / the persistence layer)? If not, is the Doc 04 amendment a P4 opener or a P2/P3 rider? (The hub orders the source read before any B-7 wording.)
- **Q2** The first proposer: the rules-compiled proposer (the existing engine wearing a principal) or a local model from day one?
- **Q3** The principal model's seed: extend `OpaqueTokenStore`'s scopes into a capability grammar, or a new identity type in the device/event model (a Doc 02/04 AMD)?
- **Q4** Which reversibility classes first — locks, valves, heating (categorical consequences) — and does "irreversible ⇒ human confirmation" live in the device model or the kernel's policy table?
- **Q5** The bench card as the permanent delivery-pressure instrument (B-1): what nightly budget (minutes, runs) is acceptable beside the 9-row floor after R-5?
- **Q6** The presence corpus: how many homes before any cross-home sentence, and is E-4's anonymization surface a prerequisite even for Nick's own home's data entering the corpus?
- **Q7** The P4 opener — ONE row: the hub's lean is **B-1** (it is already half-instrumented by FIX-1; it costs no Nick-hours beyond a bench-row charter after R-5; and it is the ground every other row stands on), with B-2's AMDs chartered as Phase-2 work in parallel. Refutable by: the fleet's needs (B-6) proving more urgent for the runway story than the agent layer's floor.
- **Q8** Which of these rows, if any, needs counsel's or Erik's eye BEFORE its charter (B-7's regulatory shadow; S-3's first public mention)?

## §6 What this document costs, at three horizons
**H1 (the next commit):** nothing — no row here touches the core tree before FIX-1b's green, CG, FE and H8; the only near-term act is a WORD: `FENCE-BUS: add` (already on Nick's desk; it protects C-002 from being read as a delivery-completeness claim while B-1 is unmeasured). **H2 (September):** nothing on the calendar moves; B-1's bench-row charter waits for R-5's proof; B-2's AMDs are Phase-2 documents the hub can draft in idle beats without a lane. **H3 (the runway):** this is the runway's content — the missing floor as a product surface, measured on hardware we own, minted one sentence at a time. If the sitting adopts nothing, the company still has P0–P3; if it adopts B-1 → B-2, the north star's central claim becomes a bench row instead of an essay.
