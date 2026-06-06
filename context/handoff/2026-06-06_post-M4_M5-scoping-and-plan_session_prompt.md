<!--
file: context/handoff/2026-06-06_post-M4_M5-scoping-and-plan_session_prompt.md
purpose: Priming prompt for a fresh Cowork conversation — a deep working-through of the code + docs that SYNTHESIZES the prior M4 deliberation into a confident, sequenced, decision-ready post-M4 plan with M5 defined. Output is decision-support: Nick brings it back to the deliberation conversation to decide.
audience: Nick (to paste into a new Cowork session)
state-type: instruction
status: READY
-->

# Cowork Session Prompt — Post-M4 Plan + M5 Scoping (deep synthesis → decision-ready plan)

You are the NexSys Project Manager / senior systems architect. **First action: invoke the `nexsys-project-manager` skill, run the session-start freshness preflight, and report the result before anything else.** (Expected PASS — the hivemind was reconciled to M4 COMPLETE on 2026-06-05/06. If STALE/CONFLICTED, stop and follow the skill's protocol.)

**This is a documents-only synthesis-and-planning session. No code, no coding instructions, no amendments.** The output is one decision-support planning document.

## What this is — and is NOT

The audits are **done**. Three deep deliberation artifacts already exist and you must build on them, not re-derive them:
- `context/audits/2026-06-05_M4-retrospective.md` — the M4 *process* retro (sizing, the instruction-scope-miss/consumer-pin pattern P2, the deferred-gate model, the partial-closeout finding, debt register, strategic/velocity, proposals P1–P6).
- `context/audits/2026-06-06_M3-M4_foundation-readiness-assessment.md` — the *artifact-level* forward gap analysis (the crypto design vacuum, AMD-65, INV-SE-04, the schema-irreversible seams, the doc-currency and contract-reconciliation gaps; §6 has a prioritized expand-now/JIT/accept list). **This was source-verified at HEAD on 2026-06-06 — trust its findings; do not re-audit them.**
- `context/assessments/2026-06-06_core-language-replatform-assessment.md` — the honest Java-vs-Rust decision-support (recommendation: stay Java + harden + pre-position a surgical Rust seam; the no-regret moves; the energy-interview decision-trigger).

**This session is the next step: turn that insight into a plan.** The objective is to give Nick deeper insight and clarity to **confidently decide what M5 is and how the post-M4 path sequences** — produced as **decision-support** (a clear recommendation + the genuine alternatives + the specific decisions Nick must make), because Nick will bring this output back to a separate deliberation conversation to decide. Do not unilaterally lock M5. Make the decision *easy and well-armed*, don't make it for him.

The governing question:

> **Given everything we now know, what should M5 actually be, what is the right sequenced path from M4 → M5 → M6 and beyond, and what internet/technical research is a prerequisite to planning or building each piece?**

## The central tension you must resolve (stated honestly, not pre-decided)

The earlier next-piece recommendation (`context/planning/2026-06-05_next-piece-recommendation.md`) proposed **M5 = Platform API + test-support** (small, dependency-free, force-multiplying), paired with the W3 website/docs lane, M6 next, AMD-65 in the M5 window. That logic predates the foundation-readiness assessment and the language study, which together complicate it. Weigh, honestly and independently (be willing to disagree with the earlier recommendation if the evidence now points elsewhere):

1. **Build-forward (the original M5):** Platform API + test-support. Small, unblocks nothing-blocks-it, and its test-support module is a force-multiplier for every later module.
2. **Reinforce-first (the foundation-readiness "expand now" work):** the crypto design owner-doc (an **M6 *entry gate*** — M6 is next and 7 docs lean on a design that doesn't exist), AMD-65 (M9+M14 critical path), the INV-SE-04 scoped-registry mechanism (M9), and the contract reconciliations (Doc 06 ↔ AMD-60 `CredentialRotator`; Doc 02 currency).
3. **Decide-the-irreversible-now (the schema lens):** `actorRef` identity semantics, the energy event-type family, and payload typing are **frozen into the immutable event log** — their cost curve is exponential, not linear, so they're cheaper now than after the log accrues. Critically, **these decisions are language-independent**: they survive a re-platform unchanged (the event log is the asset that carries over), so they are *regret-proof under both the stay-Java and the go-Rust futures* — the safest investments on the board.
4. **Protect the launch (non-Core):** website/docs, Web UI, and distribution are **at zero** and are the runway's stated #1 risk (M4 retro §8; release-runway roadmap §5). P6 of the retro said protect non-Core capacity with a non-preemptable floor.
5. **The language no-regret moves:** the GraalVM native-image spike and the Generational-ZGC-vs-G1 Pi measurement (both *double as* LTD-01 reversal-criteria data) and the energy Mom-Test interviews — all from the language assessment.

These are not necessarily mutually exclusive. A well-shaped M5 might combine a small Core build (Platform API + test-support) on the Coder lane with the design/decision/reconciliation work (crypto owner-doc, schema decisions, AMD-65, contract reconciliations) on the PM lane and the non-Core standup as the parallel lane — because much of the reinforcement work is *design/decision*, not code, and can run concurrently with a small Core milestone. Two specific syntheses to test, not assume:
- **M5 = test-support is the natural home for the verification-foundation gap** the foundation-readiness assessment did *not* cover: the harder modules (M7 automation, M9 supervisor, M14 Zigbee, energy) need fault-injection / property / time-series / hardware-in-the-loop testing the current contract-suite + Pi-profile approach doesn't provide. If M5 builds test-support, scope it for *those* needs, not just `TestClock`/`InMemoryEventStore`.
- **The GraalVM / GenZGC spikes are platform/build-foundation work** that naturally belongs in or beside M5 and simultaneously generates the language-decision data.

Your job is to resolve this into a concrete recommendation with the alternatives laid out — not to declare one winner without showing the work.

## Do a deep, genuine working-through (this is what makes the plan trustworthy)

Read the three prior artifacts above first (so you synthesize, not re-derive). Then **work through the code and documentation thoroughly** to build your own grounded understanding and to go *deeper than the audits did on the candidate-next surface specifically.* Prime context:

- **Current state & planning:** `context/status/PROJECT_SNAPSHOT.md`; `context/planning/phase-3-milestone-backlog.md` (the M5–M15 Future Major Groups + the M4-retrospective debt subsection); `context/planning/2026-05-31_release-runway-roadmap.md`; `context/planning/master-release-plan.md`; `context/planning/2026-06-05_next-piece-recommendation.md`; `context/planning/research-agenda.md`.
- **The candidate-M5 surface — read the actual code + docs deeply:** `platform/platform-api/` (source + `MODULE_CONTEXT.md`) and `testing/test-support/` + `testing/integration-tests/` (what exists, what's stubbed) — these are the literal M5 candidate. Plus `config/configuration/` + Doc 06 and the unpromoted crypto Draft (`homesynapse-core-docs/research/2026-03-22_Unified_Cryptographic_Architecture_for_HomeSynapse.md`) — the M6 dependency M5 must set up.
- **The schema-decision points:** `EventEnvelope` (`actorRef`), `EventTypes.java` (energy event family), the string-typed payload fields, and the persistence serde — to ground the irreversible-decision recommendations.
- **The forward modules:** the `MODULE_CONTEXT.md` files and design docs 01–14 §8 for the modules M5/M6 touch and that M5 must not paint into a corner.
- **The invariants flagged unmet:** `governance/Architecture_Invariants_v1.md` — INV-PD-07 (crypto-shred), INV-EI-01 (energy events), INV-SE-02/04 (auth/least-privilege), INV-AI-05 — to anchor which "expand now" items are MVP-mandated vs horizon.
- **The codebase reality check:** `context/relay/2026-05-28_codebase-investigation-for-rust-deliberation.md` (Sections C/D/E/G/H) for the as-built state, re-verifying anything load-bearing against HEAD `8ef9e9f`.

**Method:** trust the just-verified foundation-readiness findings (don't re-audit the whole tree); spend your depth on the *candidate-next surface* and the *sequencing/dependency logic*; be willing to disagree with the earlier next-piece recommendation; source-verify any new load-bearing claim (file:line); separate what you can plan now from what needs research first.

## Be research-aware (the "research on the side" requirement)

For every candidate work item, flag whether external/technical research is a **prerequisite**, a **parallel** input, or **not needed** — and what specifically. Likely research surfaces (assess, don't assume): crypto key-management / KEK-DEK / crypto-shredding patterns for the M6 owner-doc; OpenADR/IEEE-2030.5 specifics *if* the energy event family is prioritized; the GraalVM closed-world ↔ dynamic-integration-loading interaction; property/fault-injection testing patterns for the verification-foundation. You have the `deep-research` skill available — use it for *quick, decision-relevant scoping* where it changes the plan, but the **heavy research is commissioned separately** (the project's research→AMD→code pipeline); your job is to produce a *research-aware plan* and a crisp research agenda, not to do all the research now.

## Deliverable

Write `context/planning/2026-06-XX_post-M4-plan-and-M5-scoping.md` (today's date; house format). Structure it to make the follow-on deliberation efficient:

1. **Consolidated current picture** — a brief, single-place synthesis of where we stand (from the three prior artifacts + current state), with pointers, not re-derivation. The shared baseline for the decision.
2. **The candidate work universe** — every contender for "next," deduplicated across all sources, each tagged: schema-irreversible? language-independent/regret-proof? M6-blocker/entry-gate? cheap? on the Core critical path? research-needed? Core vs non-Core.
3. **Sequencing logic** — the dependency graph (M6 fans out to M7/M9/M10), the cost-curve (schema-irreversible first), the M6 entry-gate (crypto owner-doc), the Core-critical-path vs non-Core-parallel split, and where the language decision interacts. Apply the **contract-freeze-readiness gate** (a sibling to the consumer/pin survey: before M5 freezes any Platform-API contract, prove it round-trips / is enforceable / has an owner doc — the systemic fix for the AMD-65/INV-SE-04 "frozen as Javadoc" pattern).
4. **Recommended M5 — definition + concrete scope — with the genuine alternatives weighed.** State a clear recommendation (what M5 *is*, its lanes, its done-when), and lay out the 2–3 honest alternatives (e.g., pure-Platform-API-as-planned vs foundation-reinforcement-bundle vs the blended multi-lane M5) with tradeoffs, so the deliberation can choose. Note explicitly which "reserved slots" are *validated* vs *name-only* (AMD-65 proved a reservation can be a liability) so M5 doesn't build on a hollow one.
5. **Post-M5 sequence sketch** — M6 and the shape beyond, enough to confirm M5 sets up M6 (esp. the crypto entry-gate) and doesn't corner the harder modules.
6. **Research agenda** — per item: prerequisite / parallel / none, what specifically, and whether it's a quick-scope or a full research brief. Fold in the language assessment's no-regret research (GraalVM/GenZGC spikes; energy interviews).
7. **Open decisions for Nick** — the specific calls the deliberation must make: the M5 definition, the non-Core posture (P6), the language-deliberation interaction and timing (do the spikes/interviews ride M5?), the energy bet, and anything else the analysis surfaces. Frame each as a crisp choice with the recommended default.

Close with a one-paragraph honest read: is the post-M4 path clear enough to commit to, what is the single highest-leverage thing to do next, and what one piece of evidence (research or interview) would most change the plan.
