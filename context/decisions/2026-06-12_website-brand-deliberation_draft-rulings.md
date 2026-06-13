<!--
file: context/decisions/2026-06-12_website-brand-deliberation_draft-rulings.md
purpose: Draft rulings W-1..W-7 from the 2026-06-12 brand/website deliberation session (Nick, via structured Q&A) + brand reference-class thesis + the site-teardown research protocol. Pending formal ratification; future website/brand sessions load this BEFORE proposing direction.
audience: Nick, PM, future brand/web sessions
state-type: decision record
status: DRAFT RULINGS — answered directly by Nick 2026-06-12; treat as binding-unless-Nick-reverses; fold/ratify at converge
-->

# Website & Brand Deliberation — Draft Rulings (2026-06-12)

Method: structured clarifying questions (AskUserQuestion), Nick answering from intent; PM translated to design language. These sit BELOW the ruled D-1..D-7 register rules and ABOVE the Feb design-system drafts in authority.

## Rulings

**W-1 — Launch audience: prosumers & HA refugees.** The homepage and first content wave optimize for people already running Home Assistant/Hubitat or comfortable with a Pi. They read receipts — the dossier pages are the conversion engine. Mainstream copy waits on the install story (W-4). Note D-4 still binds: even prosumer-facing pages lead reliability; privacy-first framing reserved for prosumer/EU contexts per the segment rule.

**W-2 — Publish model: build hidden, publish early-but-gated, then grow a following.** Site is developed privately; goes public only when the publish gate (W-5) passes; after that, primary CTA is follow-the-build (email list + GitHub) until the product ships. Anti-perfectionism guard: the gate is the *complete* definition of "solid" — when PG rows pass, it ships, no new criteria invented at the threshold.

**W-3 — Brand reference class: Stripe × Apple × Oracle (Redwood era, ~2019–2025), counterweighted by Framework.** Nick's stated taste; Tailscale acknowledged as sharing Stripe's virtues; Framework preferred over Tailscale. Thesis sentence: *documents like Stripe, feels like Apple, carries Oracle-era institutional weight — with Framework's ownership ethos as the counterweight so prosumers read "built for me, forever," not "enterprise, not for you."* The Feb north star ("infrastructure-grade software presented with consumer-grade calm") survives unchanged; this defines its reference class. Anti-models: Home Assistant visual/community clutter; hype SaaS. Note: the Feb palette's dark anchors (#0B0F14 Obsidian Graphite) already support the Redwood-gravitas hero direction.

**W-4 — Install story: UNDECIDED (open D-grade decision).** Nick will push for plug-and-play as hard as pre-release constraints allow, assuming Core is MVP-ready. Until ruled, mainstream "plug-and-play" claims are embargoed (tense-truth gate); prosumer install copy may describe what exists. PM owes an options memo (image-flash vs manual vs appliance) with effort estimates when Nick calls for it.

**W-5 — Publish gate (defines W-2's "solid"):**
- PG-1: all four flagship dossier pages at reviewer-grade (no stubs).
- PG-2: brand mark exists — satisfied by the W-6 wordmark, so this gate is cheap.
- PG-0 (PM-recommended addition, pending Nick): design-system v0 implemented — typography + color tokens per the (reconciled) specs, so the gate is content-bound, not theme-bound. Rationale: finished dossiers on a default theme would recreate exactly the "unfinished site" risk W-2 exists to prevent; the specs are implementation-ready, so this is days not weeks.

**W-6 — Visual identity: wordmark-only at launch.** "HomeSynapse" typeset to spec (Inter, weight discipline, monochrome survivability per visual-design-reference §6.3). No symbol until post-launch; a future mark must not require reflowing the wordmark. Small task: produce the wordmark spec (weight, tracking, clearspace, light/dark variants) during design-system reconciliation.

**W-7 — Naming surface: homesynapse.com only at launch.** NexSys appears in footer/legal as "a NexSys product." nexsys.io deferred until an investor/B2B surface is needed. CLOSES website/README.md open item #3.

## W-3a — Oracle clarification + warmth-layer rulings (same session, second round)

Nick clarified W-3's Oracle component with Redwood-era brand material (mission hero, illustrated organic textures, logo-system governance, the maturation arc). What he's pointing at, made precise:

1. **Warmth through illustrated texture**, not photography/gradients — organic line-work (topographic swirls, grain patterns) layered over the palette.
2. **Brand-system governance** — Oracle's "O"-tag usage law (never standalone, placement rules, "never treat as graphic novelty") is the model for how we govern any future HomeSynapse symbol. When a symbol eventually joins the W-6 wordmark, it ships WITH a usage-governance section, day one.
3. **The maturation arc** — the brand must grow organically from free/local-first product into cloud/paid/B2B surfaces (Connect, Cloud Pro, distant B2B) without rebrand. Design implication: no asset may encode "hobbyist" or identity-by-negation ("anti-cloud"); maturity lives in type discipline, texture system, and governance. Reinforces C5 (Connect-proof copy).

**W-8 — Background/illustration motif: topographic/organic + mesh/constellation (Nick's pick, up to blend).** The two ruled families may be explored separately and as a hybrid (organic contour lines carrying occasional node-connections — which lands near "synapse lines" territory while keeping the warmth of topo). PM note, recorded not ruled: pure topo is borrowed visual language (means nothing specific about HomeSynapse); differentiation must come from execution and/or the mesh blend. The Feb strict rule stays as the control: *if a user notices the background, it is too strong.* Amends website-design-vision §8.1's allowed-styles list at reconciliation.

**W-9 — Warm illustration palette: APPROVED.** A small curated set of muted warm tones (clay/ochre/sage-teal class) for illustrations and textures ONLY — never UI, never text, never actions. HomeSynapse Blue keeps its interaction monopoly; the one-accent-per-screen rule is untouched. Amends visual-design-reference §5/§7 at reconciliation; new swatches need C6-style contrast checks for any text-adjacent use.

**W-10 — Brand moments: APPROVED, rare.** Saturated full-bleed fields with illustration allowed ONLY on homepage hero and About/Vision (the pages already mapped for expression in design-vision §11). Docs, downloads, account surfaces stay calm-neutral permanently. Amends the visual-design-reference "no bright saturated colors for large surfaces" rule with this scoped exception.

**Serif display: NO CHANGE.** The screenshot that suggested it was shared for its line-work only (Nick clarification). Typography v2 all-sans spec stands; serif remains opt-in body reading mode.

**Next concrete step for W-8/W-9/W-10:** a design-exploration session producing 3–5 sample texture/hero compositions (motif blends × warm palette over the existing neutrals) for Nick's veto BEFORE any of this is folded into the specs. Rulings define the lane; samples decide the look.

## Site-Teardown Research Protocol (for upcoming research sessions)

Purpose: turn "study other websites" into foldable returns, not vibes. Run as R-series-style sessions (Cowork or the DOCS Project), one return per site or pair, PM-assessed like any research return.

**Corpus (priority order):**
1. **Ubiquiti/UniFi** — closest business analog: prosumer infrastructure, premium consumer presentation. (PM addition to Nick's list.)
2. **Framework** — ownership/transparency counterweight; community-forward without clutter.
3. **Stripe** — docs craft, typography-in-practice, restrained accent discipline.
4. **Apple (product pages)** — landing-page economy of words, confidence pacing.
5. **Oracle 2019–2025 (Redwood)** — via Wayback Machine snapshots; gravitas, dark-surface discipline, what to AVOID (enterprise coldness markers). EXPANDED per W-3a: also study the Redwood brand *system* itself (illustration/texture language, the "O"-tag governance model, warm illustration palette mechanics, brand.oracle.com / Redwood design-system docs where public) — it is now a primary input to W-8/W-9/W-10 execution, not just homepage calibration.
6. **Anti-models/competitive:** Home Assistant, Hubitat, Homey, SmartThings, Aqara — both as design anti-models and as a claims audit (what they promise, where they're vulnerable → feeds dossier pages).

**Per-site method (the output contract):**
1. Capture: screenshots (landing, one deep doc page, one product/trust page), Wayback dates for Oracle.
2. Decompose into the six layers matching our doc structure: message hierarchy (what leads, what's buried) → IA/page map → typography/color/layout measurements (actual px/ratios, not impressions) → motion inventory → trust-signal inventory (receipts, proof, social, docs prominence) → CTA architecture.
3. Score against OUR rules: which of our register rules / design-system rules does this site obey or violate, and does the violation work?
4. Extract: STEAL (adopt), AVOID (anti-pattern, with why), TEST (try, uncertain) — each as numbered RECs.
5. Land the return at `homesynapse-core-docs/website/design-system/research/` dated, REC-numbered; PM assessment follows the standard pattern.

**Sequencing note:** UniFi + Framework first (closest analogs, highest information density for W-1's audience), Stripe/Apple second (craft calibration), Oracle via Wayback third, anti-model sweep last (it doubles as competitive-claims audit for the dossiers).

## W-11 — RENAME DIRECTIVE (Nick, 2026-06-12 — PENDING, name not final) ⚠️ affects everything

**Nick's ruling:** HomeSynapse AND NexSys will be renamed away within ~1 month. Reason: trademark conflict density makes a C&D "when, not if" for both names. New company-name candidates: **"Asimtote" / "Asymtot"** (coined near-spellings of "asymptote"; intent: Google/googol-style coined math word; brand story = perpetual approach to perfection, which Nick defends correctly — against infinity, perpetual approach is the win condition, and for any finite bar the curve eventually clears it).

**PM collision check (2026-06-12, surface-level web search — NOT legal clearance):**
- "Asimtote" — occupied by a Cambridge University open-source network-config Python tool (GitLab); "ASIMPTOTE" is an active thermal-power-conversion software company (LinkedIn). Variants are real foreign spellings of asymptote (≈Swedish "asymtot", Indonesian/Turkish "asimtot") — global feel, but slightly weakens fanciful-mark status in those jurisdictions.
- "Asymtot" — no exact-match entity found (nearest: Asymm, Asymbl — distinct). Cleaner of the two candidates on collisions.
- Neither is virgin; neither looks fatal. **Full clearance REQUIRED before the refactor:** attorney + USPTO/EUIPO (classes 9/35/42 at minimum), .com + handles + GitHub org, radio test (hear→spell), "did you mean" suppression check, international meaning check.

**Strategic upside (PM):** coined = *fanciful* mark — the strongest trademark category — which structurally strengthens D-2 (trademark as commercial control point). The rename is a legal upgrade, not just a dodge.

**Open question flagged to Nick:** company name is chosen-ish; product name is not. PM recommendation: collapse to ONE brand (company = product, the actual Google model; the NexSys/HomeSynapse two-brand split was a standing cost and W-7 already half-collapsed it). Rule deliberately.

**Lane impact:**
- BLOCKED on the name: W-6 wordmark task, domain purchase, any public surface, email domain, final flagship-page headers.
- NOT blocked: W-8/W-9/W-10 texture+palette sample round, site teardowns, design-system reconciliation (C1–C11), flagship copy drafting in name-light form (write around the name; single token-swap at rename).
- CODE NAMESPACE: `com.homesynapse.*` across all modules + JPMS names + Gradle + docs corpus + hivemind references. Cost grows with every new module/doc. Schedule as a dedicated rename milestone (single commit, full `./gradlew check` green, MODULE_CONTEXT sweep) once clearance passes. The known-name watermark ("HomeSynapse"/"NexSys") in strategy docs, governance docs, and skills gets a coordinated find-replace pass per the terminology-stability rule (documentation-style-guide §12.3: single coordinated change).

## Standing tensions to carry into reconciliation

1. Oracle gravitas vs W-1 audience warmth — Framework counterweight is the explicit control; check every hero/landing draft against "would an HA refugee feel invited?"
2. W-4 embargo vs Feb design-vision §10.1 mainstream framing — design vision reconciliation (C7) should also annotate the install-story dependency.
3. Publish-gate discipline vs C5 (Connect-proof flagship copy) — PG-1 review must include the C5 check.
