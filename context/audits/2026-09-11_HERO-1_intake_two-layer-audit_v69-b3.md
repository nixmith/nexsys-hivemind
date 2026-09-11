<!--
file: context/audits/2026-09-11_HERO-1_intake_two-layer-audit_v69-b3.md
purpose: The hub's two-layer audit of the HERO-1 return (the first design of the explainability hero): the lane's claims read critically, then the hub's own re-execution at the bytes — sizes, md5s, the name grep, the banned-word grep, the line cites, and the mockups rendered headlessly and inspected.
audience: the hub (v69 and after) · Nick (the verdict, the landing card and the ruling batch are in the operator brief)
state-type: intake audit (FILED; not edited after this beat)
status: FILED v69 beat 3 (Fri 2026-09-11 ~16:3x CT; instrument 2026-09-11T21:20Z at the first check)
-->

# HERO-1 — intake audit (two layers)

**Verdict: ACCEPT.** The write-set is exactly the three files the charter named; nothing under `src/` changed; the four predictions hold on the hub's own re-execution; the design does what the charter asked and the spec is usable as the implementing lane's order of work. Two observations for the build lane and one terminology question for Nick (Q7) are recorded below; none blocks the landing.

## §1 Layer one — the claims, read critically
The return (`context/audits/2026-09-11_HERO-1_return.md`, 7,294 B) claims: three files written (57,427 / 80,605 / 881 B); P1–P4 met; 30 headline cells + 3 rows, 7 why-not rows, 4 empty states, 5 modes + 4 neighbours, 9 EXPLAIN rows, 140 keyed strings, 20/20 state pairs at or above 4.5:1; no name other than `{{NAME}}`; no scripts or external resources in the mockups; `npm run dev` not runnable from the Linux shell (FE-NULL-1 O3), so the design was made from source and fixtures; six questions, none blocking. The claims are specific and each names how it was measured. Nothing in the return asserts a live-wire verification, and its register is stated as DESIGN-COMPLETE, BUILD PENDING — correct for a lane that ran nothing.

## §2 Layer two — the hub's re-execution (device, at `eabdbb1`; container for the render)
| Rule | Check the hub ran | Result |
|---|---|---|
| R1 write-set | `git status --porcelain` on core: only `?? web-ui/dashboard/design/`; `wc -c` and `md5sum` on the three files | 57,427 · 80,605 · 881 B; md5 `307a07ba…` · `e29f21c3…` · `15cd3fae…` — identical to the return. PASS |
| R2 predictions | P4's cites re-read: `contract.ts:367` `export interface CausalChain {`, `:384` `cascade: { parentRunId: string \| null; depth: number };`, `:385` `}`; `:346` `reason`, `:353` `resultOutcome?`; `format.ts:519` `function commandVerb(`, `:532` `}` | all as the return states; the charter's cites were stale as it says. P1–P3 verified by the counts and greps below. PASS |
| R3 banned list | `grep -io` over SPEC §7 (lines 134–275) for simply · just · easily · please note · obviously · seamless · robust · leverage · delve · moreover · furthermore · crucial · vital · exciting · powerful · oops | zero hits. PASS |
| R4 name grep | `grep -rli` for the current and retired candidates, the product name and the company name over `design/hero-v1/` | 0 files; `{{NAME}}` appears 6 times. PASS |
| R5 delivery claims | `grep -rio 'deliver'` over the folder | 3 hits, all sentences stating that no delivery claim is made; "was asked to" is the sent-but-unconfirmed verb throughout. PASS |
| R6 the modes | `states.html` staged and rendered in headless Chromium (1400 px); section C and the reference card inspected as images | the five modes and the two neighbours are distinct by label and glyph in both themes: Confirmed (check) · Sent — not settled yet (dashed arrow, dashed pill) · Sent — no reply (clock) · Replaced (swap) · Accepted, never confirmed (check+dots) · Failed (x) · Expired at restart (arc). 0 `<script>`, 0 `http`, 94 `card` elements. PASS |
| R7 the questions | SPEC §12 read | six real decisions, each with options and a recommendation; none blocks. PASS |

## §3 Observations (for the build lane, not defects in the return)
- **O1 — the reference card mixes eras.** Section A's headline reads "…because Hallway Motion detected motion at 9:42 pm" (the verb the firing value will supply once EXPLAIN-1 lands) while its trigger step reads "the reading wasn't recorded" (today). The spec's own rule (`{triggerVerb}` null → "changed") would headline today's run as "…because Hallway Motion changed at 9:42 pm". The `hero-states` mock scenario (SPEC §11 B7) must keep each run in one era so the mock never shows a sentence the wire cannot back.
- **O2 — the trigger verb table is undefined.** "detected motion" for `occupancy.occupied = true` implies a per-capability verb map for `{triggerVerb}` when the value is present. B1 needs that table written before the sentence is coded; until then every trigger reads "changed", which is honest.
- **O3 — the spec is 57 KB.** Right for a design of record; the implementing lane reads §3, §7 and §11 and consults the rest by range.

## §4 Q7 — a terminology question the design surfaces
The copy says "the hub" for the running HomeSynapse instance (`explain.offline.title`, `explain.replaying.*`, `explain.mode.expiredRestart.*`, the "not in this hub's registry" arm). The dashboard already uses "the hub" in five user-facing strings at HEAD (`DevicesView.tsx:174–175`, `feedback.tsx:67`) and in code comments, but the Glossary has no entry for it (its one "hub" match, line 91, is incidental). DAS §9 asks that established terms be stable and defined. Options for Nick: (a) ratify "the hub" as the UI term for the running instance and add a Glossary §8 row (UI term "hub"; concept: the HomeSynapse Core instance serving this home; API token: none) through the amendment path — hub-applied, Nick commits; (b) replace it with a name-free phrasing ("this system") everywhere; (c) leave it undefined. Recommendation (a): it is short, device-like, rename-proof and already in use. Not blocking.

## §5 Disposition
Landing: Nick's card `git add -A web-ui/dashboard/design` (3 A) with the message file `_scratch/2026-09-11_core_HERO-1_commit-msg.txt`; `frontend.yml` runs on the push and is unaffected (nothing under `src/`). Rulings: `HERO1: Q1 a · Q2 a · Q3 a · Q4 a · Q5 a · Q6 a · Q7 a` are the hub's recommendations, one word per row or `HERO1: all recs`. Next lane on this surface: **HERO-1b** = SPEC §11 B1–B7 on the then-current mirror (B1 first, one small WU with its test), then B8 row by row as each EXPLAIN key lands; it runs in the web-ui slot beside the Java lane. MODULE_CONTEXT: unchanged by a design-only lane; the build lane updates it. Check 9: unaffected.
