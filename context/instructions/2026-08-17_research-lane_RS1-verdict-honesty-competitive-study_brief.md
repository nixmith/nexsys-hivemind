<!--
file: context/instructions/2026-08-17_research-lane_RS1-verdict-honesty-competitive-study_brief.md
purpose: RS-1 — THE COMPETITIVE VERDICT-HONESTY STUDY: convert the moat from our assertion into a MEASURED MARKET FACT. For each major smart-home platform, establish at citation grade what the platform records and what the user is shown when a commanded device does not confirm — and whether any surface in the field distinguishes sent / acknowledged / confirmed the way our verdict layer does.
audience: a FRESH Cowork research-lane session (NOT the hub; read-only on every repo; ONE return write).
state-type: research-lane brief / dispatch (adopted RS-1, v53 beat 5; the research slate of record).
dispatch-line: "Read nexsys-hivemind/context/instructions/2026-08-17_research-lane_RS1-verdict-honesty-competitive-study_brief.md and execute it."
due: Thu 2026-08-20 EOD (graceful degrade Fri EOD; a partial return with honest coverage notes beats silence).
return: `context/audits/2026-08-20_RS1_verdict-honesty-competitive-study_return.md` (ONE file, uncommitted; the hub stages it). Returns file to context/audits/.
laws: DESK-ONLY — no purchases, no hardware, no vendor contact, no account signups beyond free doc access · NAME-LIGHT — never disclose ZENDOMO/any candidate or the company posture; the lane writes product-agnostic ("a local-first home-automation platform") · every load-bearing claim CITED (URL + retrieval date; file:line where source is open) · anecdote-grade sources (forums/issues) LABELED as such, never load-bearing alone · re-fetch-at-consumption (I-8) noted in the frontmatter · findings-never-marketing: the return's language stays inside the D5 layered form (the deterministic floor is MISSING from the field, never "we are superior") · refutation welcome in both directions.
-->

# RS-1 — The Competitive Verdict-Honesty Study (the moat, measured against the field)

## §0 Read first

1. This brief, whole.
2. Strategy pointers (ONE-LINE grounding each; carriers stay the strategy files): the technical north star at `context/strategy/2026-07-27_homesynapse-technical-overview_north-star.md` (the harness enforces; the model only proposes) · the Substrate Thesis at `context/strategy/Substrate_Thesis_v0.md` §5/§9 (the evidence discipline this study serves) · the moat note at `context/strategy/2026-07-30_instruction-vs-evidence_moat-note.md`.
3. The method precedent: the W-MARKET return's falsifier-class primary reads (e.g., HA `trigger.py` at a raw tag — five error-class reason codes, plain non-match SILENT). That is the evidence grade this study runs at.
4. Our own baseline, so comparisons are honest: the verdict vocabulary (CONFIRMED · CONFIRMATION_TIMED_OUT · ACKNOWLEDGED/superseded · honest-UNCONFIRMED classes) and the ~1,728-verdict corpus are OURS to know, NEVER to state in the return as a comparison claim — the return measures THEM; the hub writes any us-vs-them language later, claim-fenced.

## §1 The platforms (in priority order; depth follows priority)

1. **Home Assistant** (open source — file:line citations expected; automations, `homeassistant.components.*` command paths, action results, trace surfaces).
2. **SmartThings** (docs + developer docs; Routines' behavior on unresponsive devices; health API semantics).
3. **Amazon Alexa Routines** (+ Ring where distinct).
4. **Apple Home / HomeKit** (+ Matter controller behavior where documented).
5. **Homey** · 6. **Hubitat** (community-documented internals acceptable, labeled). 7. Optional: Google Home.

## §2 The five questions (answered PER PLATFORM, each answer cited)

1. **The silence case:** a commanded device does not respond/confirm. What does the platform RECORD, and what does the USER SEE — immediately, and in any history/trace surface?
2. **The vocabulary case:** does ANY surface distinguish *sent* vs *acknowledged* vs *confirmed-by-device-report*? Or does "ran successfully" mean only "the command was dispatched"?
3. **The dead-target case:** an automation targets an offline/absent device. Silent skip? Error? Retry? Does the run report success?
4. **The false-confirm case (the C1 mirror):** can the platform claim an action happened without device evidence? Name the exact mechanism (optimistic state updates, assumed state, fire-and-forget) with the citation.
5. **The self-report case (the DX-12 mirror):** what does each platform's health/status surface claim about its OWN liveness, and is any of it evidence-based vs asserted?

## §3 Output shape (the return)

(1) The comparison map — one section per platform, the five questions answered with citations, each claim tagged SOURCE-GRADE (code/official-doc) or ANECDOTE-GRADE; (2) the falsifier headlines — anything that would DISPROVE our differentiation thesis goes FIRST, not buried (if a platform does distinguish confirmed-by-report, we need to know more than we need to be right); (3) the gap table — for each of the five questions, which platforms have NO honest answer (the market's missing floor, stated neutrally); (4) an appendix of exact quotes/snippets for the hub's later claim-fencing work; (5) coverage honesty — what could not be established from desk sources, listed, never guessed; (6) route-back: "Intakes at the hub for two-layer audit (falsifier-class primaries re-fetched at intake, the W-MARKET precedent)."

## §4 Fences

No instrumentation of live competitor systems (priced separately, later, if ever) · no contact with any vendor/community as ourselves · nothing in this return is external-ready copy — the hub + the D5 language law own any restatement · if the evidence contradicts our thesis anywhere, the return says so plainly (the falsifier-first rule is the point of the study).
