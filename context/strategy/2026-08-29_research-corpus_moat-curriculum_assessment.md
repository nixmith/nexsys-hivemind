<!--
file: context/strategy/2026-08-29_research-corpus_moat-curriculum_assessment.md
purpose: Strategic review of Nick's study corpus (C:\Users\Nick\Documents\Books\CS\Research Papers — 28 items, 4 tiers + root, inventoried at the bridge 2026-08-29) against the moat: the four-item landing zone (RS-3 §6.6 — durable confirmation record · general why-not · cross-device policy kernel + attributed record · sensing consent), the Substrate Thesis, and the W-C6/W-C7 standards horizon. Names what stands, what is missing, the additions, and the reading order by phase. Long-term instrument: the corpus is the syllabus a competitor would have to traverse.
audience: Nick (the reader) · the hub (September-plan rows; register/claim ancestry) · future research lanes
state-type: strategy assessment (decision input; no design authority)
status: FILED (v58 beat 4, 2026-08-29). Maintenance: additions enter by harvest line or Nick's word; the crosswalk (§4) is the living part.
-->

# The research corpus — moat curriculum assessment (v1)

## §0 What the corpus is FOR (four jobs, in moat order)

1. **Design authority** — every enforcement invariant we ship should have a named theoretical ancestor (what a monitor CAN enforce; what a shield may overwrite; who may say what). The corpus is where those ancestors live.
2. **Register armor** — a claim phrased in the field's canonical vocabulary (safety property, edit automaton, tamper-evident log, actual cause) is materially harder to refute or lawyer around than one phrased in product words. The reading converts directly into claim-sentence quality.
3. **Standards credibility (the W-C7 horizon)** — whoever holds the home instance of "the declaration object" will be talking to SCITT/MHS/ETSI-class rooms; speaking Schneider and transparency-logs natively is the entry fee.
4. **The conditions-to-copy syllabus** — a competitor copying the surface must still traverse this literature to copy the substance. The corpus, kept current, IS a written record of the depth gap.

## §1 What stands (the four tiers map cleanly — keep the structure)

- **Tier 1 (Starter) = the enforceability canon.** Alpern–Schneider (safety/liveness) → Schneider 2000 (EM-enforceable = safety properties) → Ligatti/Bauer/Walker (edit automata — suppression/insertion, the formal shape of "the harness rewrites the proposal") → Basin 2013 (enforceability revisited with clocks). This IS the theory of the deterministic floor. Nothing to add at this tier but one capstone: **Falcone/Fernandez/Mounier, "What can you verify and enforce at runtime?" (STTT 2012)** — the survey that joins the four.
- **Tier 2 (Architecture) = the Simplex lineage.** Sha 1998/2001 → Neural/Distributed/Black-Box Simplex. Harness-enforces/model-proposes has a 25-year control-theory pedigree; Black-Box Simplex is the nearest ancestor to our posture. Complete as a spine.
- **Tier 3 (Enforcement over learned components) = shielding.** TACAS 2015 → AAAI 2018 → CACM 2025 + PLC runtime enforcement. Current and sufficient.
- **Tier 4 (Substrate) = capabilities + verified kernels + time.** Dennis–Van Horn, Miller ocap, CHERI ×2, seL4, Lamport, Lee–Seshia CPS, FORGE. Right shelf; two adds below (§2.4).
- **Root = the working library.** Anderson, Baier–Katoen, Huth–Ryan, Vardi–Wolper, Nipkow–Klein, Kleppmann, Lee–Seshia embedded. Sound.

## §2 The gaps — mapped to the landing zone (each add: one line of why)

**2.1 Confirmation truth & silent failure (the deepest claimed row; currently ZERO coverage):**
- Saltzer, Reed & Clark, *End-to-End Arguments in System Design* (TOCS 1984) — the canonical argument for why "did it actually happen" can only be answered end-to-end; underwrites the confirmation leg.
- Sampath et al., *Diagnosability of Discrete-Event Systems* (IEEE TAC 1995) — the formal frame for detecting failures (and non-events) from observable event streams; the general why-not's theory.
- Chandra & Toueg, *Unreliable Failure Detectors* (JACM 1996) + FLP 1985 — what is knowable about a silent device; the availability-truth row's foundations.

**2.2 The attributed durable record (the register's own theory; the SCITT/W-C7 room):**
- Crosby & Wallach, *Efficient Data Structures for Tamper-Evident Logging* (USENIX Sec 2009) — the log that can prove itself.
- Laurie, *Certificate Transparency* (ACM Queue 2014) + RFC 6962 — the transparency-log pattern a verdict corpus would speak when asked.
- Schneier & Kelsey, *Secure Audit Logs* (TISSEC 1999) — the pre-history; short.

**2.3 Causality & why-not (the explain surface's spine):**
- Halpern & Pearl, *Causes and Explanations: A Structural-Model Approach* (2005) — "why did it fire" as actual causality, formally.
- Cheney, Chiticariu & Tan, *Provenance in Databases: Why, How, and Where* (2009) + Chapman & Jagadish, *Why Not?* (SIGMOD 2009) — the why-not-provenance literature: the only field that has formalized answering "why didn't it."
- Miller, *Explanation in AI: Insights from the Social Sciences* (AIJ 2019) — how humans actually consume explanations; the hero surface's human half.

**2.4 The policy kernel over time (invariants · rates · reversibility · attribution):**
- Lampson, Abadi, Burrows & Wobber, *Authentication in Distributed Systems: Theory and Practice* (1992) — the "says" calculus; attribution's canon (Tier-4 add).
- Park & Sandhu, *The UCON_ABC Usage Control Model* (TISSEC 2004) — continuous authorization with obligations/conditions: the nearest formal model to rate-limits and standing invariants (Tier-4 add).
- Garcia-Molina & Salem, *Sagas* (SIGMOD 1987) — compensation as the formal shape of reversibility classes.
- Alur & Dill, *A Theory of Timed Automata* (TCS 1994) + Maler & Nickovic, *Monitoring Temporal Properties of Continuous Signals* (2004, STL) — timed/metric monitoring: rates and windows, and the bridge from logic to physical signals.
- Zanzibar (USENIX ATC 2019) — relationship-based authorization at scale; the practical composition pattern.

**2.5 Composition (the cross-device thesis's academic ancestry):**
- Calder, Kolberg, Magill & Reiff-Marganiec, *Feature Interaction: A Critical Review and Considered Forecast* (2003) — home automations ARE features interacting on shared devices; the composition-point argument has a 30-year telecom pedigree. High priority.

**2.6 Systems safety & the conformity object (the W-C6 era):**
- Leveson, *Engineering a Safer World* (STAMP/STPA, 2011) — the hazard-analysis language the machinery-file world speaks from 2027-01-20.
- Leveson & Turner, *The Therac-25 Accidents* (IEEE Computer 1993) — THE deterministic-interlock case study; register-adjacent rhetoric with fifty years of weight.
- Rushby, *Runtime Certification* (RV 2008) — the bridge between runtime verification and certification; exactly W-C6's seam.

**2.7 Sensing & consent (the RS-4 wedge):**
- Nissenbaum, *Privacy as Contextual Integrity* (2004; book 2010) — the consent-semantics framework; RS-4 §2.4's ten declarations map onto CI's parameters nearly one-to-one. Read BEFORE any wedge sentence is drafted.
- Ma, Zhou & Wang, *WiFi Sensing with CSI: A Survey* (ACM CSUR 2019) — the standard technical survey under the RS-4 envelope.
- Kyllo v. United States (2001), the opinion — short, quotable, already load-bearing in RS-4 §2.5.

**2.8 The founder shelf (one business classic, deliberately):**
- Shapiro & Varian, *Information Rules* (1999) — standards wars, lock-in, network effects: the W-C7/MHS/SCITT game in its economics form. (Local-first: Kleppmann et al., *Local-First Software*, Onward! 2019 — the brand's academic cousin; short, worth owning.)

## §3 Reading order (phase-tied; ~1 deep read/week is the honest cadence at A-14)

- **P0→R-10 (now→mid-Sep):** Saltzer end-to-end · Sampath diagnosability · Nissenbaum CI (feeds the R-10 rows and every explain/wedge sentence). Already-held tier 1 re-reads ride along.
- **P1/P2 (the surface + register era):** Halpern–Pearl · why-not provenance pair · Crosby–Wallach + CT · Therac-25 · Miller XAI · Local-First.
- **P3 (fleet/procurement):** Leveson STAMP · Rushby · UCON · Sagas · feature interaction · Lampson 1992 · Information Rules.
- **Standing:** Anderson and DDIA as reference; Baier–Katoen as needed per invariant.

## §4 Two structural moves (cheap now, compounding later)

1. **Three new tier folders** mirroring the missing pillars: `5 — Evidence & Provenance` (2.2+2.3) · `6 — Composition & Safety Systems` (2.5+2.6) · `7 — Sensing & Consent` (2.7). The tier structure then reads as the moat map itself.
2. **The claims-to-canon crosswalk** (a living file, one line per register claim naming its theory ancestors — e.g., claim #1's chain: Schneider 2000 → Simplex → event-sourced record). Start it at the register mint; every future claim adds its line. This is register armor made explicit — and someday, the seed of a technical whitepaper no competitor can write quickly.

## §5 The standing rule

The corpus grows by NAMED gaps (a harvest line, a lane finding, a Nick word) — never by accumulation. Anything that serves none of the four jobs in §0 is cut. The inventory + this map re-verify at each phase seam.
