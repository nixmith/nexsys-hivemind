<!--
file: context/instructions/2026-08-08_research-lane_WMARKET-market-currency_brief.md
purpose: W-MARKET — the market-currency research lane (Nick's menu word "both, sequenced", 2026-08-08, v50 beat 1). Fresh Cowork session, read-only, web-backed currency research. Return is a NAMED input to the charter SKELETON (Aug-11 EOD) and S-10 THE CHARTER (Aug-12–13); if late past the skeleton window it degrades gracefully to a READ input (Aug-16) — the hub adjudicates the consumer at intake.
audience: the W-MARKET lane (a fresh Cowork session; no role skill required — this brief is self-contained)
status: DISPATCH-READY. Dispatch line: "Read nexsys-hivemind/context/instructions/2026-08-08_research-lane_WMARKET-market-currency_brief.md and execute it."
due: return ON DISK by 2026-08-11 09:00 America/Chicago (the skeleton consumes it Tue EOD). GRACEFUL-DEGRADE: if you cannot make 09:00, FILE ANYWAY by 2026-08-13 EOD — the return then feeds THE READ (Aug-16) instead of the skeleton; a late return is still a return (a lane is verified at its file on disk).
-->

# W-MARKET — Market-Currency Research Lane Brief

## Section 0 — Posture and laws (read first; these bind every sentence you write)

1. **READ-ONLY.** You commit NOTHING, edit NOTHING, in any repo. Your ONLY write is your return file: `nexsys-hivemind/context/research/2026-08-XX_WMARKET_market-currency_return.md` (XX = completion day). A lane is verified at its RETURN ON DISK, never at word — if the file does not exist at that path, the lane did not run. No outreach, no accounts, no posting, anywhere.
2. **The D5 language law.** Any restatement of the enforcement position uses ONLY the layered form: the deterministic floor is MISSING from the field, not SUPERIOR; L2/L3 without L1 are unsound; L1 without L2 is insufficient. Never "deterministic beats model." The enforce-vs-propose line means: the harness enforces; the model only proposes (the north star's technical thesis).
3. **Anti-fabrication discipline (the ecosystem-currency return's own standard):** every load-bearing claim is tagged [VERIFIED] (primary source retrieved this lane, URL + access date), [REPORTED] (secondary source, named), or [INFERRED] (your reasoning, so labeled). No untagged market claims. A claim you could not verify is reported as UNVERIFIED, loudly — never silently dropped, never rounded up.
4. **Unbiased-instrument posture (Nick's standing directive, 2026-08-08):** you are a currency instrument, not an advocate. Evidence AGAINST our positioning outranks evidence for it in reporting priority: any observed evidence FOR a Substrate-Thesis §9 falsification condition is a HEADLINE finding (top of the executive summary), never a footnote.
5. **Gate sovereignty.** Nothing you produce moves pre-freeze code (freeze 2026-08-14 EOD; THE READ Aug-16). Your return is decision input, not a work order.
6. **Comparative statements about named competitors are research notes only** — they inherit the counsel gate and publish nowhere. R-1 rename-readiness: keep the return name-agnostic beyond citing our internal docs' own titles; never couple analysis to the current brand string.
7. **The moat-watch quiet question rides every charge** (`context/strategy/2026-08-06_company-scale-moat-watch_standing-directive.md`): does this generalize beyond the smart home; is there a company-scale lever as the surrounding technology shifts? Log candidate watch entries explicitly as CANDIDATES for the hub — never self-adopted.
8. **Baseline at dispatch (re-derive at your launch; trust the newest spine):** core `d26777c` · hivemind at-or-after `5729cdf` · bench `16e672d`. Web research is the lane's core method — cite everything.
9. **A-14 sizing binds any proposal you make:** operator attended-hours floor is 15 h/wk (weekend-anchored, semester constraint from Aug-17). Detail: `context/research/2026-08-02_A14_attended-hours_charter-input.md`.

## Section 1 — Mission

Refresh the market-facing claim surface that S-10 THE CHARTER (Aug-12–13) and THE READ (Aug-16) will price. The charter assigns every input a disposition class — (i) PRODUCT SURFACE / (ii) PROCESS MOAT (deliberately under-disclosed) / (iii) MARKET CLAIMS (priced, DO-NOT-SAY-fenced) — and your return must let it price class (iii) on CURRENT data instead of a Jun-27 baseline.

**Deliverable: ONE return file** with (a) an executive summary ≤ 1 page at top (falsifier-relevant findings FIRST per Section 0.4); (b) the body as the five charges below; (c) EVERY charge closed with claim rows in this exact one-word-adjudicable form:

> **ROW:** the charter-relevant claim · PRIOR (what our corpus says, doc + section cited) · FINDING (web-backed, dated, tagged) · **VERDICT: CURRENT / MOVED / CONTRADICTED / NEW** · CONSEQUENCE ≤ 1 line (which charter/READ item it touches).

**Charge 1 — Matter/Thread adoption state.** Delta against `context/assessments/2026-06-27_smart-home-ecosystem-currency_research-return.md`: spec releases and certification state, actual shipped-device adoption vs announcements, fragmentation/controller-interop reality, hub-class certification trends. The Substrate-Thesis §2.6/§2.7 lens applies: where is the standard in its absorb-the-connectivity-layer arc, and where is value provably relocating (orchestration · arbitration · reliability · accountability)?

**Charge 2 — Home Assistant trajectory + commercial ecosystem.** Release cadence and governance state, Works-With program traction, Nabu Casa / Open Home Foundation commercial moves, credible market-share/install-base signals. The §9.6 race-condition watch is explicit: any evidence that HA (or an adjacent FOSS project with network effects) is adding a credible audit/accountability/multi-tenancy story is a falsifier-class HEADLINE finding.

**Charge 3 — Local-first competitor field.** Hubitat, Homey, openHAB, and any new entrants since Jun-27: funding, positioning, discontinuations, local-first marketing claims vs cloud-dependency reality. Counter-positioning is tested PER-COMPETITOR (§2.3), never globally — for each: what structurally prevents them from copying an honest-evidence position, if anything?

**Charge 4 — Model-in-the-loop home products vs the enforce-vs-propose line.** Every shipped or credibly-announced LLM/agent-in-the-home product you can find (platform assistants' home integrations, HA's LLM features, startups). For EACH: which safety layer does its story actually occupy (L0–L3 per the Substrate Thesis §3.1), and does ANY ship a deterministic enforcement floor between model output and actuator? BOTH §9 falsifier arms are live here: high-consequence deployments shipping with NO enforcement layer and no incident-driven consequence (condition 1), or a major platform shipping an unbypassable enforcement layer (condition 2). Report what IS, not what flatters.

**Charge 5 — SHORT-clock delta check ONLY.** Prior art: `context/assessments/2026-07-28_agent-substrate-research_return.md` verified the Substrate Thesis §5 ledger + §10 clocks at primary source (that lane ran Jul-31). Your charge is the DELTA since: SCITT draft/WG status changes; 802.11bf silicon shipments + application-layer/privacy-semantics claims. Do not re-verify what that return already verified — cite it and report movement.

**Known hazards:** L-E (the physics deep-research lane) runs in parallel and its §4 includes a competitive/market scan — division of labor: L-E owns physics-positioning analysis; YOU own adoption/commercial/ecosystem currency. Where you overlap, cite the division and stay in your lane. The LD platform-horizon return (`context/research/2026-08-02_LD_platform-horizon_return.md`) covered the plugin/cloud-platform radar Aug-1 — delta only, do not re-survey. The C-2 Tier-0 claims position (`context/strategy/brand-program/2026-08-06_C2-tier0_sleepy-battery-and-confirmation-position_draft.md`) is ACCEPTED — your findings may CONTRADICT it (report loudly if so) but your language must never casually restate claims it fences.

## Section 2 — Named sources (read in this order)

1. `nexsys-hivemind/context/assessments/2026-06-27_smart-home-ecosystem-currency_research-return.md` — the baseline you delta against.
2. `nexsys-hivemind/context/strategy/Substrate_Thesis_v0.md` — §2 (the pattern library: your analytical lenses), §9 (falsification conditions: your headline test), §10 (the clocks), §11 (precedence: where it conflicts with source or governance, THOSE win).
3. `nexsys-hivemind/context/assessments/2026-07-28_agent-substrate-research_return.md` — Charge-5 prior art.
4. `nexsys-hivemind/context/research/2026-08-02_LD_platform-horizon_return.md` — the plugin/cloud radar; delta only.
5. `nexsys-hivemind/context/strategy/2026-07-27_homesynapse-technical-overview_north-star.md` — the enforce-vs-propose line's home (note its frontmatter honesty-state discipline).
6. `nexsys-hivemind/context/strategy/2026-08-06_company-scale-moat-watch_standing-directive.md` — W-1/W-2/W-3; your candidates extend it.
7. `nexsys-hivemind/context/research/2026-08-02_A14_attended-hours_charter-input.md` — the sizing floor.

**Return integrity:** end with a self-audit section — sources actually read (any you could not access flagged loudly) · every UNVERIFIED claim listed in one place · the three weakest claims in your own return · what a hostile reviewer would attack first.
