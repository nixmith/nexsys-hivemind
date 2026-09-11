<!--
file: context/instructions/2026-09-10_design-lane_HERO-1_explainability-hero_design-charter.md
purpose: The charter for HERO-1, the first design of the explainability hero (why did it fire · why didn't it · did it actually confirm), run as a frontend lane in design mode. It produces a design specification and static mockups under web-ui/dashboard/design/hero-v1/ and touches no source. The build that implements the spec is a later lane (FE-114 after EXPLAIN v1.1.4 lands, or HERO-1b if the spec is ready first).
audience: the HERO-1 lane (a fresh Cowork conversation booted as the nexsys-frontend skill) · the hub (audits the return) · Nick (rules on the spec in one batch)
state-type: lane charter
status: DISPATCH-READY (v69 beat 2, Thu 2026-09-10 evening CT). Nick's word `DESIGN: start` (Thu 2026-09-10) is the ruling the frontend skill §5 requires for the first design of the hero. Baseline: homesynapse-core HEAD `eabdbb1`.
-->

# HERO-1 — the explainability hero, designed from its empty states outward

## §0 The lane contract (read first; every line binds)
- `date -u` first. State your instrument limit (what you can and cannot run from your shell). CT = UTC−5, derived once.
- **The one deliverable:** `nexsys-hivemind/context/audits/<your CT date>_HERO-1_return.md`, one file, §0 card first (≤3 KB: the census of files written with exact paths, the four predictions adjudicated, the defaults you took, the questions for Nick), then §1–§4 as §3 below names them. Cap ≤10 KB. Your last line, in the file and printed: `RETURNED <path> <bytes>`.
- **Write-set.** You create `homesynapse-core/web-ui/dashboard/design/hero-v1/` and write only inside it. You do not edit anything under `web-ui/dashboard/src/`, and nothing outside `web-ui/dashboard/`. `git status --porcelain -- web-ui/dashboard` must be empty when you start; other paths may be dirty later (a Java lane, EXPLAIN v1.1.4, may be editing `core/**` on the same tree — that is lawful; never touch them). Never run `git add`, `git stash`, `git checkout` or `git commit`. Nick commits with a `git add -A web-ui/dashboard/design` card after the hub's audit.
- **This is design, not build.** No dependency installs, no changes to `package.json`, Vite, the token build or the CI gate. You may run `npm run dev` to look at the current dashboard against the mock; you may render your mockups as an artifact so Nick can see them; the files of record are the ones in the repo.
- **The honesty law binds every sentence you write:** a value the wire did not carry is never shown as if it had; a null renders as an honest sentence, never as a blank, "null", an invented name or an invented verb. `DISPATCHED` is not delivered; an acknowledgement is not confirmation; `UNCONFIRMED` is calm and honest, not an alarm and not a success.
- **Name-light.** The product name is in a trademark search and may not be used publicly. Every mockup and every line of the spec uses the literal token `{{NAME}}` where the product name would appear. No candidate name (of any kind) appears in any file you write. The frontend skill's `brand-and-design-system.md` §6.1 names an older candidate; it is superseded by the spine — the token is the rule.
- **The honest-claim discipline:** no "only", "unique", "first", "patented", and no competitor comparison anywhere in the copy or the spec's rationale.
- **Predictions, pre-registered; adjudicate them first in your §0 card:** P1 — the copy table in the spec covers every cell of RunStatus × ActionOutcome for the causal-chain headline and every NonFiringVerdict for "why didn't it", with no cell left to inference. P2 — `grep -ril` over `design/hero-v1/` for any product-name string other than `{{NAME}}` returns nothing. P3 — `git status --porcelain -- web-ui/dashboard/src` is empty at your close. P4 — you find at least one line cite in this charter that has moved or is wrong at `eabdbb1`, and you file it with the corrected line.

## §1 The read-set, in order (nothing older)
1. `nexsys-hivemind/context/research/2026-09-06_HERO-0_null-census_v1.1.3_return.md` — whole (10 KB). Its §1 table is the meaning of every null the read-API serves and the honest sentence per key; its §2 is the four empty states; its §3 (EXPLAIN-1..10) is what the hero cannot say until Core carries a key. Your design starts here.
2. `nexsys-hivemind/context/audits/2026-09-10_FE-NULL-1_return.md` — the O1 paragraph (§3): the headline sentence ignores the run's outcome, so a skipped run reads as if the light turned on. The L1 headline per outcome is your first row.
3. The frontend skill's `references/explainability-and-accessibility.md` §1–§4 (the two durable halves; the seven principles; the AMD-97 confirmation semantics; accessibility; the honest-claim discipline) and `web-ui/dashboard/FRONTEND_DOCTRINE.md` whole (lean).
4. `web-ui/dashboard/MODULE_CONTEXT.md` §Gotchas (the tri-state idiom: absent ≠ null ≠ value; the era boundary; epoch seconds) and the FE-113 / FE-NULL-1 beat notes at its top.
5. The types, at `eabdbb1`: `src/lib/api/contract.ts` — `RunStatus` :140, `ActionOutcome` :150, `NonFiringVerdict` :153–:157, `CausalChain` :358–:373 (with `cascade` :372), the `resultOutcome` comment :353–:355 (the open ten-value vocabulary underneath the five outcomes). `src/lib/format.ts` — `causalSentence` :472 and `commandVerb` :519–:530 (the "acted" fallback). The three views: `src/views/ExplainHubView.tsx`, `src/views/WhyNotView.tsx` (`:91` the inference DP-B2 flagged), `src/components/CausalChain.tsx`; their CSS modules for the current token usage.
6. `homesynapse-core-docs/design/16-superior-automation.md` — the hero substrate (`RunCausalChain`, INV-SA-01..04) by range; `design/08-zigbee-adapter.md` §3.6 (AMD-97: per-capability confirm timing, idempotent no-report, `UNCONFIRMABLE`) by range; `design/13-web-ui-observability-mvp.md` — the explain views' sections by range.
7. `homesynapse-core-docs/governance/DAS_Consolidated_Reference_v1.md` §1.1 (Register C for UI copy), §2.2 (banned patterns), §2.3 (the specificity principle).

## §2 The ground the design stands on (source-cited by the hub at `eabdbb1`; re-read, never trust)
- The hero is three questions, led by two durable halves: the honest command outcome (`Confirmed | Sent, not confirmed | Failed`) and the fact that explanations are never evicted (a projection of the immutable log). "Why didn't it fire?" is a co-equal half.
- The vocabularies the hero renders today: `RunStatus` = COMPLETED · FAILED · SKIPPED · CANCELLED · INTERRUPTED; `ActionOutcome` = DISPATCHED · CONFIRMED · UNCONFIRMED · FAILED · SKIPPED; `NonFiringVerdict` = CONDITION_NOT_MET · NEVER_TRIGGERED · ACTED_BUT_UNCONFIRMED · DISABLED. Under `ActionOutcome`, `resultOutcome` is an open string vocabulary from `command_result.outcome`; any value the design does not name renders in the honest-can't-know register.
- The five modes the standing rendering law keeps distinct: dispatched-and-timed-out · superseded-same-attribute · acked-then-silent-forever · held-DISPATCHED · settled-FAILED-on-window-close. Label and shape carry the distinction; colour reinforces it; AA in both themes.
- The four empty states HERO-0 wrote (its §2), with their working copy: not-fired ("It hasn't run yet."), no detail recorded ("This run is on record, but its steps aren't."), reading not recorded ("{entity} set it off at {time} — the reading wasn't recorded."), confirmation unknown ("Sent — the device never confirmed." / "Sent — waiting for the device to confirm."). Start from these; improve the words if the mom test says so, and say why.
- The keys Core does not yet carry (HERO-0 §3, EXPLAIN-1..9; EXPLAIN-10 is resolved core-side by HONESTY-1 `94ae99d`, which seeds `lastReported` null until the first `state_reported`): the firing value; the triggering `subject_ref`; the parent run id; the condition text; a stable definition key across reloads; `FIRED_CONFIRMED` as a verdict; per-permit trigger refs; `disabledAt` with its origin; `confirmedAt`/`settledAt` per action. EXPLAIN v1.1.4 is being authored beside you to add them. Your design shows each surface twice: what it says today (an honest "not recorded" sentence, never a mock value) and what it says once the key lands.
- The headline today: `causalSentence` (`format.ts:472`) composes "{target} {verb} because {trigger} at {time}" and `commandVerb` (`:519`) turns `turn_on` into "turned on" regardless of the run's status; a SKIPPED run therefore headlines as if the device acted. The interim one-line fix is a build task, not yours; the grammar per outcome is yours.

## §3 Files to create (all under `homesynapse-core/web-ui/dashboard/design/hero-v1/`)
1. **`SPEC.md` — the hero design specification, v1.** Register A, plain sentences, the Glossary's terms (Automation, Run, Trigger, Condition, Action, Event, Entity, Device). Sections, in this order:
   - §1 What the hero is for, in one paragraph, and the stranger who must understand it.
   - §2 The information architecture: the entry points for the three questions, the two disclosure levels (a plain sentence; a bounded linear step chain; the technical fact one expand away), and what never appears (index paths, internal identifiers, a free graph).
   - §3 **The L1 headline grammar** — a table with one row per (RunStatus, leading ActionOutcome) cell and one per NonFiringVerdict: the sentence template, its slots, the honest variant when a slot is null, the key name for the copy (dot-path style, e.g. `explain.headline.skipped`), and the shape/label/colour role. Every SKIPPED, FAILED, CANCELLED and INTERRUPTED run has a sentence that does not claim the device acted.
   - §4 The four empty states, as full copy (title, body, any action offered), and where each appears.
   - §5 The confirmation states: the five modes rendered distinct, the per-capability pending window (no global timeout; no failure anxiety inside a capability's honest window), the idempotent no-report case, `UNCONFIRMABLE` rendering honest `UNCONFIRMED` at once, superseded expectations expiring.
   - §6 The EXPLAIN placeholders: for each of EXPLAIN-1..9, the surface, today's sentence, the sentence once the key lands, and the key it waits for.
   - §7 Copy table: every string the hero shows, with its key, its register (C), its reading level check, and the slot types. Copy is centralised and test-locked in the build; you write the table, not the code.
   - §8 Accessibility: AA contrast in both themes for every state colour; shape + label on every state; focus order through the chain; `prefers-reduced-motion`; screen-reader text for each state marker.
   - §9 Tokens: which existing tokens each state uses (from `src/styles/` and the generated token source); any token you need that does not exist, named and justified, as a request — not a change.
   - §10 The acceptance script: six sentences (two per question) a stranger reads aloud, and what "right" means for each.
   - §11 Build rows for the implementing lane, in order, each one small (the first is the `commandVerb`/headline-per-outcome change with its test).
   - §12 Open questions for Nick, each with two or three options, your recommendation and whether it blocks the build.
2. **`states.html` — static mockups**, one self-contained file (inline CSS, no scripts required, no external resources): the hero card in every headline state of §3 and every empty state of §4, in dark and in light, using the existing token values by name in a comment beside each colour. `{{NAME}}` where the name would appear. Nothing here is wired to the app.
3. **`README.md`** — five lines: what this folder is, what it is not (not shipped, not bundled), who rules on it, the spec's version and date.

Return sections after the §0 card: §1 what was designed and the defaults taken (one line each); §2 the copy table's coverage counts (cells filled ÷ cells possible, per table); §3 the questions for Nick (mirroring SPEC §12); §4 the next recommended lane (refuse to close).

## §4 What to watch out for
- The mock data populates fields the wire serves null (`firingValue` in every mock chain; `command` on the SKIPPED action). Design from the wire's truth in HERO-0 §1, not from the mock.
- A run's headline must follow the run's status and the leading action's outcome, not the command's verb.
- `lastReported` on the entity list may still be a first-seen stamp on deployments before `94ae99d`; the spec says "No report time on record." for null and does not claim currency.
- Old runs serve skeleton chains forever (the era boundary): "no detail recorded" is permanent for them and must read as a fact, not an error.
- Colour never carries a state alone; the error register (red) is reserved for known failure; `UNCONFIRMED` is amber and calm.
- Sentences ≤ about 20 words; no index paths; no identifiers a stranger cannot read; a device or automation whose name is missing is described honestly ("a device the run didn't name"), never invented.
- Your shell may be Linux against a Windows tree; `npm run dev` may need the platform packages (FE-NULL-1's O3). If it does not run, design from source and the fixtures and say so in §0 — it is not a gate for this lane.

## §5 Out of scope
Any change under `src/`; any contract or wire change (a request goes in SPEC §12 and the return, as a cross-lane ask); the wordmark, the brand mark or any name; the marketing site; the non-hero views (entities, devices, events lists) except where the hero links into them; competitor comparison.

## §6 Success criterion (binary)
`design/hero-v1/SPEC.md`, `states.html` and `README.md` exist; every cell of the §3 headline table and every NonFiringVerdict has a sentence and a key; every EXPLAIN-1..9 row has a today-sentence and a landed-sentence; `grep -ril` for any name other than `{{NAME}}` under the folder is empty; `git status --porcelain -- web-ui/dashboard/src` is empty; the return is on disk with its `RETURNED` line.

## §7 Escalation
Decide inside the system freely and record each default in your §0 card. Put anything that changes direction — a new hero presentation beyond the two disclosure levels, a new colour role, a token that does not exist, a copy choice that reads as a positioning claim — into SPEC §12 as one batch for Nick, with options and your recommendation. Do not stop the lane to ask; Nick rules on the batch after the hub's audit, with one line per row (`HERO1: <row> <word>`).

## §8 The hub's audit rules (pre-filed)
R1 the write-set is exactly the three files under `design/hero-v1/` (census at porcelain) · R2 P1–P4 adjudicated with evidence, not asserted · R3 every sentence in the copy table passes the DAS §2.2 banned list and reads at or below the stated level · R4 no name string other than `{{NAME}}` (the hub greps) · R5 no claim that DISPATCHED means delivered and no optimistic rendering of `UNCONFIRMED` anywhere in the mockups · R6 the five modes are visually distinct by shape and label in both themes (the hub opens `states.html`) · R7 the return's questions are real decisions with options, not deferrals.

## §9 The dispatch line (Nick pastes into a FRESH Cowork conversation with `ClaudeFolder` connected)
```
date -u first. You are the HERO-1 design lane for NexSys/HomeSynapse — boot as the nexsys-frontend skill in design mode. Baseline: homesynapse-core HEAD must be eabdbb1 and `git status --porcelain -- web-ui/dashboard` must be empty (other paths may be dirty — a Java lane may be running; never touch them; stop and report only if web-ui/dashboard is dirty). Execute nexsys-hivemind/context/instructions/2026-09-10_design-lane_HERO-1_explainability-hero_design-charter.md exactly: read its §0 contract and §1 read-set first; adjudicate P1–P4 in your §0 card. Create web-ui/dashboard/design/hero-v1/ with SPEC.md, states.html and README.md as §3 specifies; write nothing under src/ and nothing outside web-ui/dashboard/; no git add/stash/checkout/commit; no installs; use the literal token {{NAME}} wherever the product name would appear and no candidate name anywhere. Write nexsys-hivemind/context/audits/<today's CT date>_HERO-1_return.md (≤10 KB, §0 card first) and end it, in the file and printed, with: RETURNED <path> <bytes>.
```
