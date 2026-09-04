<!--
file: context/strategy/2026-09-04_R10-sitting_THE-WORDS_ruling-record.md
purpose: THE RULING RECORD of the R-10 sitting — Nick's words, VERBATIM, given Thu 2026-09-03 ~20:40 CT (instrument: banked at v62 beat 2, Fri 02:xxZ) in the Part-5 answer shape, plus his three H10 words (EXITCODE · FOP-DATES · ORPHANS) with his own reasoning and caveats, and his four-day plan. One-way doors get a real ruling with his words preserved verbatim in the spine (working-with-nick §3). §1 is his text; §2 is the hub's reading of what each word does and where it is spliced. Refutable by his one word (REVERT / EDIT), never by the hub.
audience: the hub (splices) · every charter that finalizes on these words · Nick (his record)
state-type: ruling record (verbatim)
status: FILED at v62 beat 2. The splice: strategy v1.2 (A-1..A-7 + the FOP-DATES rows) · the docket cards RULED · the September plan §0-ter · the OR register · the brand posture (TIER-2 GO).
-->

# The R-10 sitting — THE WORDS (verbatim record)

## §1 Nick's message (2026-09-03, ~20:40 CT) — verbatim

> **2 — The words:**
> ```
> STRATEGY: R-1 b · R-2 b · R-3 b · R-4 a · R-5 a
> DOCKET:   ADOPT-ALL-RECS
>           EDIT Row 2: (b), as a DATED design note first (the Doc 17/02 AMD charters with the P4 build); weeks 3–4, after R-4b and the CG batch land
>           EDIT Row 12: (a); the fallback fires on a criterion-0 miss at this weekend's R-4b, not on the 09-14 calendar date
> OPTIONAL: TIER-2 GO
> ```
> I say we make a prompt and I launch the FAILCHAN lane the moment PKG-SEC-2's CI is green (`ef02d13` all checks passed) — it's a focused Coder evening, and if it lands tonight the unit fix rides into Saturday's artifact as a free rider. Friday midday tomorrow: Erik's nudge as a reply on your Wednesday email if he's still silent (if you think this is smart or okay). Saturday is R-4b: install the CI-built artifact carrying F-R4-1 and PKG-SEC-2 on the held card, set `permit_join_duration` for the run (absent now means no window, and the rejoin hook only admits inside one), pre-validate the card's `zigbee.yaml` against the fragment, then the four-of-four with v62 navigating — criterion 0 first, and the fallback above if it misses; the evening is the audit, and if it goes four-of-four, C-002 mints and the docket's row 12 closes. Sunday is the dashboard's honesty: the CG-1/2/3 Core WU in the morning, commit and CI, then the FE fast-follow in the afternoon on the same tree once Core is in — sequential, because both write into `homesynapse-core`. Monday, Labor Day, is the real-wire day: the H8 exercise on the clone rig, which rules `sys_*` and turns FE-HONEST-1's register from "live-verification pending" to verified; with what's left, the Doc 12 correction note commit, the F-S8/FE-STATE-DIALECT charter, and the Row 2 design-lane dispatch. That's roughly twelve hours of your hands across the four days, and every one of them lands on hardware, on main, or on the register — which is the compounding the program was built around. I also had a shower thought we should probably dedicate a brainstorming / deep-reasoning session (or two) dedicated to what direction we are going to shift our ambitions as soon as we file, get approved, and are focused on building out the smart home system beyond just the MVP — both technically and strategically.
>
> **C** — Again, let me know if this is wise/smart on our part, or we should just be patient and focus on what's in front of us and in our control right now.
>
> **D** — Understood. Let's just ensure everything is properly written/designed so we can get the most informative results possible to guide us.
>
> **E** — It does not seem to be working; I cannot get the information here. At the top of the page, it reads: `EUR-Lex is temporarily not fully available. You can however access recent OJs. In addition, you can consult EU law here (https://op.europa.eu/en/web/eu-law-in-force).`
>
> **G — EXITCODE: a · FOP-DATES: a · ORPHANS: a**
>
> The reasoning, briefly, plus one caveat each.
> **EXITCODE (a).** This is a real find and it belongs in FAILCHAN — same class (a healthy or deterministic outcome reported through the wrong channel), same files, same lane. An unwired `ExitCode` enum plus a `RestartPreventExitStatus=10` that can never match means a bad config today restart-loops five times in 300 s and then dies looking like a crash; wiring the code makes the unit's own comment true. It also composes correctly with Row 6: `RestartPreventExitStatus` applies whatever `Restart=` policy the charter picks, so `Restart=always` plus a 10 on deterministic config failure is exactly the honest pair. The caveat to write into the charter: the `System.exit(code)` lives in `main` after `manager.start()` has thrown and teardown has run — never in a shutdown hook, where it deadlocks — and the exit call itself goes behind a thin seam so the FATAL-subsystem → code mapping is unit-tested while the process exit is not.
> **FOP-DATES (a).** A declined row is a decision too, and both dates are inside the next twelve days, so leaving them out of v1.2 would mean deciding by default. The EU row has a dependency worth naming now: the `EU: ship|defer` word on 11 September should be given on the W-C6 closure, which is still waiting on your one-minute Annex I paste — so E1 stops being low priority and becomes "before Friday the 11th." Activate is cheap to carry and costs nothing until the 15th.
> **ORPHANS (a).** Four questions the Pelton-week plan raised and the sixteen cards silently dropped — the JDK trajectory in particular touches LTD-01 and the sd_notify matrix, and the events endpoint touches the corpus's demo face, so they'll resurface whether or not they have cards. Better to carry them as rows for the R-5 charter than rediscover them in November. One sizing note for the hub: these are carry-forward questions, not load-bearing rulings, so ≤1 KB each is enough; the words come at the R-5 charter, not this weekend.
>
> Noted on H & I.

(§1 of his message — the hivemind push `5ce1f72..d66eeed` — and §F — the docs repo clean at `a53f474`, nothing staged — were operator reports, banked at v62 beat 2.)

## §2 The hub's reading — what each word does, and where it lives now

| Word | Effect | Spliced at |
|---|---|---|
| **R-1 (b)** | THE MEASURED CORPUS is the community wedge (RS-5's convergence + the FOP presence benchmark as one object); the explain surface its demo face; the code SDK a rung | strategy v1.2 §1 asset 1 (A-1) |
| **R-2 (b)** | The Apache-2.0 flip lands in the SAME window as the rename in-tree (one launch moment); 10-01 quarterly = gate check; fallback: rename slips past 10-31 → flip on the un-renamed tree | v1.2 §4 (A-4) |
| **R-3 (b)** | v1.2 absorbs the FOP's load-bearing rows (benchmark · NSF · standards/channel watch) and NAMES what it declines (§9 · §5.5 · Tracks A–B) | v1.2 §4 (A-4 + the declines paragraph) |
| **R-4 (a) · R-5 (a)** | The household and company goals, register-shaped, verbatim | v1.2 §0 (A-5) |
| **ADOPT-ALL-RECS** | Rows 1–16 ruled at their recs: 1 (a) · 2 (b, EDITED) · 3 (b) · 4 (a) · 5 (b) HOLD · 6★ (a) · 7 (a) · 8 (b) · 9 (a) · 10★ (a, by dispatch) · 11 (a) · 12 (a, EDITED) · 13★ (a′, by dispatch) · 14★ (a) · 15 (a) · 16 pre-lean (a), ruled at H8 | the docket cards file (RULED header) · the OR register (6 → FAILCHAN chartered; 7 → JOURNALD chartered; 5 → M13 HOLD, T-0 not spoken) |
| **EDIT Row 2** | (b) as a DATED design note first — the Doc 17/02 AMD charters with the P4 build; the design-note lane runs weeks 3–4, after R-4b and the CG batch land | the docket (Row 2 status) · the September plan §0-ter (wk 3–4 row) |
| **EDIT Row 12** | (a); the announce-class fallback (b) fires on a criterion-0 MISS at Saturday's R-4b — not on the 09-14 date | the docket (Row 12 status) · the R-4b navigator packet (the fallback branch is IN the packet) |
| **TIER-2 GO** | Name-dependent PRIVATE work may start under VERDOMO as the working assumption, name-TOKENIZED (`{{NAME}}`); the wordmark is the last layer; public use stays FENCED to the opinion | the posture ruling (status line) · B-1 identity may charter as a lane when hours exist (it slides whole, never shrinks) |
| **EXITCODE (a)** | Wire `ExitCode` — rides the FAILCHAN charter as instance 5; his caveat is a charter constraint: `System.exit(code)` in `main` after `start()` threw and teardown ran (never in a shutdown hook); the exit call behind a thin seam so the FATAL-subsystem → code mapping is unit-tested and the process exit is not; composes with Row 6: `Restart=always` + 10 on deterministic config failure = the honest pair | the FAILCHAN coding instruction (§ EXITCODE row) · OR-FAILCHAN |
| **FOP-DATES (a)** | v1.2 §4 gains the EU-posture row (`EU: ship|defer`, 09-11 — on W-C6's closure, so E1 is now "before Fri 09-11") and the Activate row (opens 09-15) | v1.2 §4 · E1 re-prioritized (the hub reads Annex I at source) |
| **ORPHANS (a)** | The Pelton-week plan's four orphan rows (Doc 09 §15 Q1 · the JDK trajectory · the IR emit question · the events endpoint) enter the docket addendum as carry-forward rows ≤1 KB each; their words come at the R-5 charter | the docket addendum (rows 22–25; beat 3/4) |
| **The four-day plan** | Thu: FAILCHAN lane (after PKG-SEC-2 green — it is) · Fri midday: Erik's nudge as a reply-in-thread · Sat: R-4b (step 0a/0b; criterion 0 first; the EDIT-12 fallback; the evening audit; C-002 on four-of-four) · Sun: CG-1/2/3 Core WU AM → FE fast-follow PM, sequential on the core tree · Mon (Labor Day): H8 real-wire (rules `sys_*`; FE-HONEST-1 → VERIFIED), then the Doc 12 note commit · the F-S8/FE-STATE-DIALECT charter · the Row 2 design-lane dispatch, with what's left | the September plan §0-ter (the plan of record for 09-03..07, with the hub's guards) |
| **The post-MVP deep-reasoning session(s)** | Chartered as a strategy-lane row (STRAT-BEYOND-MVP), gated to run at the filing go-ahead / C-002 — not this weekend | the docket addendum (row 26); the v62 brief §G |
