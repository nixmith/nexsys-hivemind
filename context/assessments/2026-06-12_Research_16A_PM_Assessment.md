<!--
file: context/assessments/2026-06-12_Research_16A_PM_Assessment.md
purpose: PM assessment of the Research 16-A return (Logging & Observability UX: Market and Human Factors, REC-186–200) — quote-back verification, source verification, external spot-checks, fabrication scan, grade.
audience: PM, Nick
state-type: assessment record
status: COMPLETE — folded SECOND per the R16 fold order (16-B's engineering constraints first; this return's human evidence prioritizes)
last-verified: 2026-06-12 (assessment session)
-->

# Research 16-A — PM Assessment (UX/market register; folded SECOND)

Return: `context/instructions/Research_16A_Logging_Observability_UX_Market_Human_Factors_RETURN.md` (292 lines, 47,869 B; md5-archived to docs `research/returns/2026-06-12_Research_16A_Logging_Observability_UX_Market_Human_Factors.md`). Assessed against: the A-brief embeds → ground (scripts at `01841ba`; Doc 07 §11.2; DAS Register C; INV-TO-04 in `Architecture_Invariants_v1.md` §482–484; `config_error` in Doc 06) + live web spot-checks (2026-06-12).

## Step 0 — Quote-back gate: **HONORED (verbatim vs the A-brief, zero adulteration)**

All three §0 blocks byte-match the A-brief's embeds: (a) §0.2(i)/(ii)/(iii) including the A-brief's own prose variants ("is set to the empty string", "no ANSI noise", the shorter pi4 idiom tail) — correctly reproduced from ITS brief, not the sibling's; (b) all 14 §0.3 names in order with levels; (c) the Register-C paragraph. The underlying embeds were ground-verified this session (scripts at `01841ba` git objects; Doc 07 §11.2; DAS §1.1). No cascade contamination (grep-verified).

## Steps A–C — Format / Summary / Cross-cutting: **PASS, STRONG**

All sections present; §1 takes positions and flags both demanded items (highest-impact: log-diving = INV-TO-04's named failure mode, mass-documented; strongest B3 item: the maintainer-run "Month of WTH" porch-light evidence). HA is deepest per the brief. Mom-Test discipline genuinely applied — every platform deep-dive carries a "what users DID" section (installed recorder filters, kept browser tabs open, push-notification breadcrumbs, camera-footage reconstruction, third-party log apps). §3.2 per-audience matrix delivers the cycle's integrating verdict with a real position: two surfaces (live stream, trace view) genuinely need dual-channel; the rest are one-surface-layered. §3.4's honest negative is the standout of the cycle: **"The over-engineering risk is data-without-register, not machinery-nobody-needs"** — i.e., the plain-language rendering register that B3 depends on is thinner in the Locked record than the data machinery. This goes to the top of the merged disposition's read-out.

## Step D — REC dispositions (PM rulings — see the merged disposition for final routing)

- **REC-186 — ACCEPT, SCRIPT-STANDARD, MERGED** as the umbrella over 16-B's REC-201/202/203 (same artifact; A supplies the human-factors *why*, B the section-level *what*). A merge, not a conflict — exactly as intake read it.
- **REC-187 — ACCEPT, SCRIPT-STANDARD, MERGED** with 16-B's REC-205 (`NO_COLOR`) + the never-color-only rule. A's WCAG SC 1.4.1 normative citation is the rationale line the draft cites; the shipped bracket-tags already carry semantics color-free (verified at `01841ba`).
- **REC-188 — ACCEPT, M12-INPUT.** The log-dive corpus as INV-TO-04's named target; INV-TO-04 embed verified VERBATIM against `Architecture_Invariants_v1.md`. The HA `grep | wc -l` → 9553 evidence item is cited to its primary issue.
- **REC-189 — ACCEPT, M12-INPUT.** Noise-budget/level-discipline test; complements (does not collide with) B's REC-212 level table — 189 is the *test obligation*, 212 the *convention*.
- **REC-190 — ACCEPT, M12-INPUT,** and **absorbs REC-196's voice clause** (below). What+why+fix grammar for `config_error` message content, impersonal Register-C voice (Rust's structure, never Elm's first-person "I"). `config_error` ground verified in Doc 06 (per-ERROR diagnostic event, applied default, dashboard notification, `yamlLine` via SnakeYAML marks) — the return's "schema untouched, content register only" framing is correct and fence-respecting.
- **REC-191/192 — ACCEPT, M10-M13-INPUT (parked).** Plain-language causality rendering rule; friendly-name vs stable-ID vocabulary split. Both correctly parked, not drafted; REC-192 honestly labeled an input ("the embeds don't say" what user surfaces default to — correct: they don't).
- **REC-193/194 — ACCEPT, M5-C-COPY.** The no-eviction attestation and the B3 dossier. Evidence verified live this session: WTH thread 219488 exact (title, campaign, URL); HA `stored_traces` default 5 exact at the cited official doc; Hubitat ~1 MB Past Logs purge exact at the cited official doc. The dossier is flagship-grade as claimed. One register nit (non-docking): the dossier's website sentence is claimed to "satisfy Register C" — website copy actually lands in Register B (Calm Neighbor); the DAS bans are satisfied either way, and the sentence survives both registers. M5-C session applies final register.
- **REC-195 — ACCEPT-WITH-MODIFICATION, M5-C-COPY (single bucket).** The recommendation text smuggles a second-bucket clause ("verify in SCRIPT-STANDARD") — the verification is naturally absorbed by REC-201/206 in the draft (the paste-survival property is a stated design principle there); the REC itself stays M5-C only, per the no-two-buckets rule.
- **REC-196 — ACCEPT-WITH-RE-ROUTE: DOC-11-CURRENCY → M12-INPUT, folded into REC-190.** The Elm-first-person-vs-Register-C clarification is real and worth keeping, but Doc 11's Locked text contains no Elm reference to annotate — the place a future contributor would meet "adopt Elm-grade errors" is the M12 evidence base/instruction, so the one-sentence voice rule lands there (inside REC-190's register guidance). Keeps the voice rule in exactly one artifact. → Disagreement register.
- **REC-197 — ACCEPT, M12-INPUT.** Negative-trace ("why didn't it fire?") corpus filed under Doc 11 §15 OQ1 as evidence only; resolution correctly left out of scope. The HA-official admission (non-triggered automations produce no trace) is the strongest item.
- **REC-198/199/200 — ACCEPT, REJECT register.** Emoji-as-semantics (multi-source, incl. the pro-emoji concession that text tags must remain); silently-lossy/opt-in-only primary log surfaces (the SmartThings 1-in-4-drop → deletion arc; Dec-31-2022 sunset consistent with the platform-transition record); euphemistic "friendly" error copy (a guardrail restatement of existing DAS bans — honestly labeled as such, not minted as new ground).

## Step E — Error inventory / fabrication check: **CLEAN**

Connector-blind DECLARED with the exact verbatim-from-embeds inventory enumerated (§5) — every HomeSynapse identifier used (script idiom, 14 event names, `config_error`/`ConfigIssue`/`yamlLine`, INV-TO-04, projectionVersion 5, Doc 07/11/13 refs, AMD-92, §15 OQ1) traces to an A-brief embed; INV-TO-04 and `config_error` embeds independently ground-verified this session. Zero fabrications. External spot-checks PASS: WTH 219488 ✓, `stored_traces` default 5 ✓, Hubitat ~1 MB ✓ (all three at the return's cited URLs); SmartThings Groovy sunset dates consistent with the known record; rustc-dev-guide "The word 'illegal' is illegal" and WCAG 1.4.1 quotes match the primary texts. Source-reliability triage (gold/silver/bronze with bronze quarantined to corroboration) is exemplary, and the INCOMPLETE-EVIDENCE declaration is honest and specific (18-call search budget; the unobtained cargo/tailscale changelog quote; the partially-incomplete "vendor dashboards nobody reads" item — none load-bearing, as claimed). The claude-code emoji-issue citation was not individually verified (one corroborant among several in a REJECT row; nothing rests on it).

## Step F — Grade and process notes

**Grade: A−.** Quote-backs perfect, zero fabrications, 100% pass on every load-bearing external spot-check, exemplary honesty machinery (the data-without-register negative, the bronze quarantine, the specific INCOMPLETE-EVIDENCE), and the two flagship deliverables (§3.2 matrix, §3.3 dossier) are exactly what the cycle needed. Docked for three small routing/category slips, all PM-adjudicable: REC-195's bucket-bleed clause, REC-196's wrong vehicle (Doc 11 currency for a DAS/M12 voice rule), and the Register B/C category slip on the dossier sentence. FUTURE-bucket emptiness is reasoned and accepted.

**Disagreement register (16-A):** (1) REC-196 re-route (above) — resolved PM-side. (2) REC-195 single-bucket enforcement — resolved PM-side. (3) The dossier sentence's register label — corrected in passing; final wording is the M5-C session's call. No item requires re-research or return amendment.
