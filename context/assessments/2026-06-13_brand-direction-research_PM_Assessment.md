<!--
file: context/assessments/2026-06-13_brand-direction-research_PM_Assessment.md
purpose: PM assessment of the two independent brand-direction returns answering Prompt 2 (validate & sharpen the W-3/W-3a thesis via a six-site teardown). Separates gold from noise, reconciles the cross-session divergences, closes C6 with values, folds C11 grammar, and proposes new rulings + a deduplicated OQ bundle for Nick's veto. Embeds the verified competitive-receipts corpus (C2).
audience: Nick, PM, design-exploration session, future nexsys-brand skill
state-type: assessment
status: DELIVERED 2026-06-13 — proposes C6 closure + new rulings for Nick's veto; C11 folds AFTER the sample veto round
-->

# PM Assessment — Brand-Direction Research (Prompt 2)

**Session:** 2026-06-13 (parallel brand lane; no Core work touched; no PROJECT_SNAPSHOT/pm-handoff edits — fold at converge). Aligns to W-1..W-11/W-3a and C1..C11 by number.

**Inputs assessed:**
- **Return 2A** — `website/design-system/research/2026-06-12_brand-direction_teardown-and-validation.md` (ST-/AV-/TS-/BD- namespacing, computed WCAG, tied to existing doc sections). The tighter, more governance-native of the two.
- **Return 2B** — inline `2026-06-13_brand-direction_research-return.md` (REC-style STEAL/AVOID/TEST; its own palette hexes; the useful button-fill token).

Both ran the six-layer teardown over the corpus Nick defined in the draft rulings (UniFi → Framework → Stripe → Apple → Oracle Redwood → anti-models), with strong convergence.

---

## Verdict

This was a *validate-and-refine* prompt and both returns validate the thesis: **W-3/W-3a survives unchanged** — infrastructure-grade software, consumer-grade calm, four references assigned jobs not looks. Almost nothing here is new *direction*. The value is concentrated in three places: (1) **one genuinely new answered question** — the warmth-vs-trust bet; (2) **the computed C6 fix** — a hard correctness blocker, now solvable with values; (3) **execution detail** that folds into C11 and the OQ rulings. Treat the rest as confirmation of decisions already ruled. **Prefer Return 2A as the canonical fold source; 2B corroborates and adds the button-fill token.**

## Gold (preserve / fold)

1. **Warmth-vs-trust verdict — the riskiest bet, now answered.** Oracle-style warmth does **not** dilute prosumer trust *provided it is confined to texture/illustration and never enters the claim layer, the type, or the UI.* **Confidence: HIGH** on the confinement rule (both sessions); MEDIUM-HIGH that it's net-additive. Framework is the existence proof — warm voice + pixel-art mascots coexisting with a footnoted battery-test methodology on the homepage, for a near-twin audience. This resolves standing tension #1 and converts W-9/W-10 from a bet into a controlled rule. → propose ratifying.

2. **C6 fix — computed and blocking, now closable.** Both sessions independently compute `#3FA6C9` ≈ **2.4:1** on Mineral Ash `#ECEFF3` — fails AA text (needs 4.5:1) *and* the 3:1 non-text/UI threshold. The fix is a two-tier accent (brand hue ≠ text hue). Reconciled token set (PM synthesis — 2A's link/warning values + 2B's fill value):

   | Role | Value (light mode) | Contrast | Notes |
   |---|---|---|---|
   | Brand hue (logo, ≥24px graphics, dark-mode link) | `#3FA6C9` | 2.4:1 light / 6.87:1 dark | decorative on light; **never** text or small UI on light |
   | Link / focus text (light) | `#176B85` | 5.23:1 ✓ | derived darker sibling, same hue family; headroom alt `#1F6379` = 5.84:1 |
   | Button fill, white text (light) | `#0E6E8C` | white-on-fill ≈ 4.9:1 ✓ | 2B's addition — the *fill*, not the text |
   | Warning text (light) | `#7E6315` | 4.94:1 ✓ | always icon-paired; demote `#C7A14A` amber to illustration-only |

   Links are **mode-specific** (derived-dark on light; brand-hue `#3FA6C9` on dark, where it passes at 6.87:1). This **closes C6** and unblocks PG-0. One dependency: re-verify against the final neutral if the warm-neutral option (OQ below) is adopted.

3. **The Framework footnoted-claim pattern = house evidence style** (both nominate it as the flagship steal). Every load-bearing number carries an inline, dated, reproducible methodology note — you already do this in the config dossier's encryption-µs note; make it system-wide. This is the literal mechanism that lets warmth and rigor coexist (the answer to bet #1) and the operational form of "evidence over assertion."

4. **Competitive-receipts corpus — VERIFIED (this session, web-checked, dated/sourced).** Every dated claim in both returns checks out. This is dossier-ready under C2:

   | Receipt | Verified fact | Date | Source |
   |---|---|---|---|
   | SmartThings Groovy | Legacy Groovy DTHs/SmartApps + IDE removal began **Sept 30, 2022**; community Groovy SmartApps (incl. webCoRE) stopped functioning **Dec 31, 2022** | 2022 | SmartThings Community "The End of Groovy"; webCoRE forum |
   | Amazon Echo local processing | "Do Not Send Voice Recordings" removed; all voice shipped to cloud. Affected Echo Dot 4th Gen, Show 10, Show 15 | **Mar 28, 2025** | The Register; TechHQ; Malwarebytes |
   | Amazon FTC penalty | $25M civil penalty (Alexa/COPPA, kids' recordings kept indefinitely) + $5.8M (Ring) ≈ $30.8M | May 2023 | FTC press release; DOJ OPA; Variety |
   | Insteon | Cloud turned off **without notice**; hubs inoperable (no local fallback); status page still showed "online" days later | ~Apr 15, 2022 | The Register; TinkerTry; iClarified |
   | Wink | Surprise $4.99/mo or hardware disabled; cutoff May 13 (extended ~1 wk, then indefinite); non-payers lose app/voice/API | May 2020 | Consumer Reports; 9to5Mac; MacRumors |
   | Home Assistant (ally, not target) | 1M → **2M+** active installs in 2024; **21,000+** unique GitHub contributors | 2024 | HA "State of the Open Home 2025" |

   **Through-line:** every competitor weakness is a *cloud-or-memory dependency they can't make provable*; Asimtote's play is provable-by-architecture *absence* of those failure classes. Frame as a **structural dated timeline, never anxiety** — "don't get burned again" stays banned (C2 / V&T §7.4); the durable counter is the architecture claim "core never requires an account" (C5).

5. **HA-as-ally positioning** (both sessions). Position complementary to Home Assistant — its 2M-install base *is* the launch audience (W-1) — never against it. Receipts target cloud-dependent incumbents (SmartThings/Echo/Insteon/Wink), not HA/Hubitat/Homey. Reinforces W-3a #3 (no identity-by-negation) and C1.

6. **Ruled-consistent execution specifics, ready to fold:**
   - **Stripe three-column dossier geometry** (nav tree │ claim-prose │ the receipt locked in the right rail) — the literal structural answer to "show the receipts."
   - **Docs/dossiers as a primary-nav peer** (Stripe + Framework) — promote the four dossiers to first-class nav, not a footer.
   - **UniFi software-as-hero** — the hero proof is a *real event-log / "ask why" screenshot* shown calmly, not abstract illustration (closest business analog).
   - **UniFi cloud-account creep as the cautionary twin** — weaponize as ammunition for the "No cloud account. Really." flagship (REC-171, C1).
   - **AVOID-4 thin-weight reconciliation** (genuinely useful): Stripe uses weight 300; Apple HIG warns against thin weights for legibility. Resolution: reserve 300 for large display (≥~32px); 400+ for body and anything <20px. Folds into the typography weight-discipline rule.

7. **Governance starter (Oracle "O"-tag → symbol usage law).** Both draft a pre-committed law for the future symbol (never standalone, never a novelty, fixed placement, no-reflow of the wordmark, monochrome-survivable, single-accent). Ties W-3a #2 and W-6. → stand up as its own file `brand-governance.md` (the seed of the future `nexsys-brand` skill, per the design-system README skill-ification rule).

## Noise (discount)

- **The specific pre-veto warm-palette hexes are suggestions, not decisions.** W-3a is explicit: the 3–5 sample-composition veto round decides the look. The two sessions even propose *different* clay/ochre/sage hexes — proof they're provisional. **Fold the grammar, not the swatches** (see C11 below).
- **The motif recommendation (hybrid topo + mesh/synapse) is validation of an already-ruled pick** (W-8 is Nick's call "up to blend"). Don't fold it as new; the real next step is the sample round.
- **Return 2B carries more restatement/padding;** 2A is tighter and tied to existing doc section numbers — use 2A as canonical.
- **Correctly deferred (LATER, not launch):** live event-log injection into docs (Stripe test-keys analog) and the license-free interactive tool (UniFi Design Center analog). Both sessions flag these as maturation-phase — agree.
- **The "(characteristic)" vs first-hand-measured caveat** (2A is honest that some UniFi/Apple type/color values are characteristic, not pixel-measured) is fine; a live-browser audit can harden them later if ever needed. Not a launch dependency.

## Divergences resolved

- **C6 exact values:** reconciled above (2A's link/warning tokens + 2B's button-fill token). Adopt as the canonical set; it ties to visual-design-reference §3 / typography-reference §7.2.
- **Warm vs cool neutral background:** 2B pushes a warm-tinted neutral (Redwood model) replacing cool `#ECEFF3`; 2A keeps canon but notes the option. **PM: do not pre-decide** — this is a look-decision W-3a routes through the sample veto round. Test warm-neutral vs cool-neutral as a sample variable; re-verify C6 against whichever wins.
- **Launch hero saturation:** both lean reduced-for-launch given a maximally skeptical audience. **PM: agree (reduced for v1, expand later)** — but it's Nick's veto in the sample round.

## Fold actions (proposed — Nick ratifies at converge)

- **C6 → CLOSE** with the reconciled two-tier token set above. Amends visual-design-reference §3 / typography-reference §7.2. Unblocks PG-0. *Owner: PM draft → Nick ratify the token.*
- **C11 → fold the warmth GRAMMAR (not swatches), AFTER the sample veto round** (as C11 already specifies). The grammar to fold: warm-tinted-neutral *option to test*; contour-dominant / node-sparse motif; hard firewall (warm → never UI/text/action); saturation-budget-by-page (full only on homepage hero + About/Vision); the "if a user notices the background, it is too strong" control preserved.
- **C2 → reinforce the dossier-register amendment** with the verified receipts table above (dated/sourced). Anxiety framing stays banned; structural timeline only.
- **C1 →** the "No cloud account. Really." (REC-171) flagship is now well-supported by the UniFi-cloud-creep + Insteon/Wink/Amazon corpus; the identity-adjective-vs-factual-claim distinction holds.
- **New rulings proposed (Nick assigns numbers at ratification):**
  - **Warmth-confinement verdict** — warmth lives only in texture/illustration on W-10 brand-moment pages; never claim/type/UI. (Could fold into W-9 rather than stand alone.)
  - **Footnoted-claim house style** — every load-bearing number carries a dated, reproducible methodology note (Framework pattern). Ties C2, W-4 tense-truth.
  - **HA-as-ally positioning** — complementary to HA; receipts target cloud-dependent incumbents only. Reinforces W-3a #3, C1.
  - **Docs/dossiers as primary-nav peer** + Stripe three-column dossier geometry; ≥1 ownership artifact + dated method footnote per dossier.
- **Governance law → stand up `brand-governance.md`** (own file; seed of `nexsys-brand` skill) with launch (wordmark-only) clauses + pre-committed symbol clauses. Ties W-3a #2, W-6.

## Open questions for Nick (deduplicated across both sessions; PM rec each)

1. **C6 token:** ratify `#176B85` light link (5.23:1) or `#1F6379` (5.84, more headroom)? *PM: `#176B85`; accept mode-specific links. [unblocks PG-0]*
2. **Warm vs cool neutral background:** *PM: decide in the sample round; re-verify C6 against the winner.*
3. **Launch hero saturation:** full vs reduced. *PM: reduced for v1, expand later.*
4. **Warm-tone count:** 6 (tightest) vs 9. *PM: 6 — maturation-safe.*
5. **Semantic warning:** demote `#C7A14A` to illustration-only and add a text-grade warning token (`#7E6315`, icon-paired)? *PM: yes.*
6. **Docs-in-nav at launch** even if thin pre-1.0? *PM: yes, peer-level.*
7. **Governance-law file location:** own `brand-governance.md` vs a section in visual-design-reference? *PM: own file — it's the brand-skill seed.*
8. **Wordmark case/weight** (contingent on the name): *PM: lowercase/sentence-case, Inter 500–600, slight negative tracking — set intent now, confirm against `asimtote` letterforms.*
9. **Stat-band honesty (W-4):** confirm the homepage uses architecture receipts (acceptance tests/invariants), never faked scale numbers (no Stripe "$1.9T" move). *PM: confirm.*
10. **Following mechanism (W-2):** email + GitHub vs a Framework-style public roadmap/changelog. *PM: email + GitHub primary; test changelog later.*
11. **Docs framework (C4 still open):** does the three-column dossier geometry constrain the framework choice? *PM: decide C4 before the PG-1 build to avoid rework.*

## Launch-vs-later split (both sessions agree — reaffirmed)

**Launch-necessary (gates W-2 publish / W-5 PG rows):** PG-0 design-system v0 *including the C6 two-tier accent* (the one hard correctness blocker — do first); PG-1 four dossiers reviewer-grade in three-column geometry with ≥1 ownership artifact + dated footnote each; PG-2 wordmark + its launch usage law; homepage leads reliability (D-4/C7); follow-the-build CTA (email + GitHub); one consumer domain (W-7); tense-truth (Zigbee MVP adapter, Matter fenced, no plug-and-play — W-4/C3); the verified receipts layer (C2).

**Later (maturation):** full warm-motif system at production fidelity (after the sample round); the symbol + activation of its governance law; interactive trust tools; live event-log injection; warm-palette expansion (each swatch contrast-checked); serif reading-mode.

## Handoff

Parallel lane; no governance-spine files touched. Register this assessment at converge. **C6 can close now** (it's name-independent and unblocks PG-0); **C11 folds after** the W-8/9/10 sample veto round, exactly as C11 specifies. Verified receipts table is ready to drop into the dossier-register (C2) amendment. The brand system is otherwise name-independent — only the wordmark render, domains, and code namespace wait on the W-11 clearance.
