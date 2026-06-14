<!--
file: context/handoff/2026-06-15_core-review_CONVERGE_M7-forward_session_prompt.md
purpose: The converge session for the two-part homesynapse-core review. Synthesize the Session A + Session B audits into ONE ranked, de-duplicated, actionable backlog + the M7-forward readiness plan. This is the session that proceeds forward — confident, focused, with M7 insight. Synthesis, NOT concatenation.
audience: PM (Cowork, fresh conversation), Nick
state-type: session prompt
status: READY (dispatch AFTER Sessions A and B have produced their audits)
-->

# Converge Session — Synthesis & the M7-Forward Plan

**You are the PM (`nexsys-project-manager` hat).** Sessions A and B each reviewed half of `homesynapse-core` and produced an audit. **Your job is synthesis: turn two diverged reviews into one short, ranked, actionable picture and a confident, focused M7-forward direction.** This is the session that lets the next real work begin without re-deriving anything.

**Synthesis is NOT concatenation.** You are not merging two documents end-to-end. You are de-duplicating, clustering, re-ranking, reconciling disagreements, and distilling to the findings and decisions that actually drive what we do next. If A + B together surfaced 60 findings, your backlog is the prioritized subset that matters — the rest stays as referenced detail in the source audits.

## Step 0

Invoke `nexsys-project-manager`; run the freshness preflight (baseline: M6 COMPLETE, core `1eddd9a`). Same environment realities as the framework — **host Read tools only; no sandbox `git`; Cowork cannot run Gradle** (so the HYPOTHESIS findings you inherit stay hypotheses until a Claude Code verification is dispatched — you decide which are worth it). Read:
- `context/handoff/2026-06-14_core-review_FRAMEWORK.md` (the shared stance, severity/disposition scale, the **Signal discipline** section — it governs your output too).
- **The two audits** (your inputs): `context/audits/2026-06-14_core-review_A_data-crypto-spine.md` and `context/audits/2026-06-14_core-review_B_runtime-automation-M7.md`.
- The M7 planning set (`2026-06-11_M7-blueprint_research-architecture.md`, `2026-06-12_M7-M8-charter-skeleton.md`, `2026-06-12_M7-blueprint_merged-disposition.md`, Doc 07) and the standing research set (`2026-06-13_side-research-candidates_CORE-DOCS.md`, `research-agenda.md`).

If A or B is missing or incomplete, note it and synthesize what exists (flag the coverage gap); do not block.

## Synthesis tasks

1. **One ranked, de-duplicated backlog.** Merge A's + B's BLOCKING/HIGH/MEDIUM findings. Collapse duplicates and shared root causes into single cross-cutting items (list the sites). Re-rank globally by severity × M7-impact × effort. Drop or roll up anything that doesn't survive the framework's materiality bar. Each surviving item: `ID | severity | type | site(s) | issue | recommendation | disposition | [VERIFIED]/[HYPOTHESIS]`.
2. **Reconcile cross-session seams.** The high-value findings live where A meets B: a contract A flags in the event/device/state spine that B's `automation` consumes; an end-to-end concern (e.g., the crypto write-path in A vs. the composition-root wiring in B). Surface these explicitly — they are the ones neither session could see alone. Resolve any A/B disagreement by re-checking source.
3. **The M7-forward readiness package** (the headline deliverable). From B's M7-readiness call + A's spine contracts that automation depends on, state plainly: what is **ready** for M7.1; what is **fix-first** (the findings that must close before M7 builds on them); what is **research-first** (the avenues that should return before committing a design); and the **recommended M7 entry sequence**. The standing M7 entry-gate (rows 3 energy/erasure interviews + 4 M5-C approve) still governs *issue* — fold that in. The goal: the next session can open M7 confident and focused.
4. **Consolidate research → one routed doc.** Merge A's + B's "research avenues surfaced" sections; de-duplicate against the standing R-α…R-ε set (mark each reinforced / refined / superseded / net-new); prioritize and route (DOCS design-research vs CORE empirical spike). Note which warrant their own dispatched session (Nick runs those separately).
5. **The Claude-Code-verification shortlist.** From the inherited HYPOTHESIS findings, pick the few where empirical confirmation actually changes a decision. For each: the exact `:module:test`/grep/command, the why, and what a pass vs. fail would mean. This is the deliberate "exactly what/why" list Nick dispatches to Claude Code — not a speculative dump.

## Output discipline

Apply the framework's **Signal discipline** to your own output. The synthesis doc leads with an executive summary that stands alone (the health verdict, the top findings, the M7-forward call). The backlog is ranked and dispositioned. Keep it the shortest thing that is complete — an input Nick acts on, not a merged transcript.

## Deliverables

1. `context/audits/2026-06-15_core-review_CONVERGE_synthesis.md` — the unified health verdict; the ranked, de-duplicated, dispositioned **backlog**; the cross-session seam findings; the **M7-forward readiness package**; the **Claude-Code-verification shortlist**.
2. `context/planning/2026-06-15_M7-plus_research-avenues.md` — the consolidated, prioritized, routed research set.
3. A completion report to Nick: the health verdict in 2–3 sentences, the M7-forward recommendation, anything BLOCKING, and the immediate next action(s) — including, if warranted, an offer to author the next session prompt (the first M7.1-prep coding instruction, or the top fix-first instruction, or a research dispatch). **Commit messages handed over** (`!`-free).

## Done-when

The synthesis doc + the consolidated research doc are on disk; the M7-forward readiness package names what's ready / fix-first / research-first + the entry sequence; the Claude-Code-verification shortlist is written (or explicitly "none warranted"); any BLOCKING item is escalated; the immediate next action is recommended; commit messages handed over. The session succeeds if Nick can read the exec summary and know exactly how to proceed on M7.
