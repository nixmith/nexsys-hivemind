<!--
file: context/handoff/2026-07-06_explainability-ux-lane_session_prompt.md
purpose: Dispatch brief for the explainability-UX lane (fresh Cowork conversation; nexsys-frontend skill v1.2). The lane renders the moat's HONEST VERDICTS — the hero questions on live vocabulary. Chartered 2026-07-06 by the v21 hub (pm-handoff v21 beat-1); every load-bearing fact below was SOURCE-VERIFIED same day at core `959f925`.
audience: The explainability-UX lane (Cowork); Nick (launch + return relay).
state-type: session prompt (lane; write-isolated).
status: READY — launch on Nick's word. Zero bench dependency; fully parallel with the bench/soak.
write-isolation: `homesynapse-core/web-ui/dashboard/**` + ONE return file (`nexsys-hivemind/context/audits/2026-07-06_explainability-ux-lane_return.md`). NOTHING else — no spine writes, no core-Java writes, no skill edits, no commits (Nick commits; the hub audits first).
-->

# Lane Brief — Explainability UX (the verdict surface)

You are a **frontend lane** (nexsys-frontend skill v1.2 — read its §4a and the FROZEN-v1.1 grounding rule first). You consume the **live** verdict vocabulary M9.4a/b landed — real events, never invented screens. The hub never implements; you never write outside your isolation set.

## 1. The charter (Nick's scope ruling, verbatim — this IS the boundary)

> *"honest-can't-know vs known-failed vs deliberately-superseded are its entire vocabulary."* (Nick, v18 beat-5 — the explanation-vocabulary scope ruling.)

The hero questions the surface must answer: **why did it fire? / why didn't it? / did it actually confirm?** The product differentiator is that these render HONESTLY — `StandardExplanationService`'s UNCONFIRMED/FAILED flattening erases exactly what this surface sells (see §3).

Related pin (Nick, v18 beat-5, verbatim — governs how identify-class commands render): *"an immediate rendered `UNCONFIRMED` verdict with recorded reason, not the silent DISABLED bypass; never-tracked and honestly-verdicted are different promises."*

## 2. THE LIVE VOCABULARY (source-verified 2026-07-06 at core `959f925` — quote-exact, with file:line)

**`command_result.outcome` — TEN values** (`core/event-model/.../CommandResultEvent.java:22-27`, the M9.4b §4.3 currency):
`acknowledged` | `rejected` | `timed_out` | `invalid` | `unsupported` | `handler_error` | `integration_unavailable` | `superseded` | `expired_on_restart` | `unconfirmed`.
The javadoc's own sentence, verbatim: *"The last four (including `invalid`) are DISPOSITIONS — terminal reports the pending command ledger's `onCommandResult` guard skips, never terminal-matches; integration adapters may publish additional protocol-specific strings."*

⚠ **Skill-staleness flag (source outranks):** the nexsys-frontend skill §4a lists a FIVE-value vocabulary — it was accurate when folded (v19, pre-M9.4b) and is now a stale SUBSET. Build against the ten above. Do NOT edit the skill (the fix rides the hub's next skills pass); note the discrepancy in your return.

**`state_confirmed` — six components** (`StateConfirmedEvent.java:26-33`): `commandEventId, reportEventId, attributeKey, expectedValue, actualValue, matchType` — the causal join (the verdict names BOTH the command and the authoritative report that proved it).

**`command_confirmation_timed_out`** (`EventTypes.java:65`) — honest can't-know at deadline; distinct from every failure.

**Brightness:** the state domain is **0–254 canonical** (Doc 08 §3.5); **`brightness_percent` is DERIVED AT QUERY** (`MaterializedStateQueryService:78/:113/:209`). Render percent from `brightness_percent`; NEVER client-side-rescale the 0–254 state.

## 3. The NAMED TARGET (render what the service erases — do not modify it)

`StandardExplanationService` (core/automation, `:56` mapping note; `:251-265`) collapses distinct verdicts into `ACTED_BUT_UNCONFIRMED` / FAILED-class renderings. **The lane's job is the SURFACE that keeps the distinctions:** deliberately-superseded (verdict-free expiry — the system doing the right thing, not a failure) vs honest-can't-know (`unconfirmed`, `command_confirmation_timed_out`) vs known-failed (`rejected`, `handler_error`, `unsupported`, `invalid`, `integration_unavailable`). Core Java is NOT in your tree: if the right fix is service-side, write the proposal (with the exact file:line and the behavior you need) in your RETURN — the hub folds it into a core WU.

## 4. The FROZEN v1.1 read-API rule (flag, don't improvise)

The dashboard read-API contract is FROZEN at v1.1. `brightness_percent` is a SHAPE-COMPATIBLE new data key inside the existing attributes map — consume it as such. If any verdict data you need does NOT flow through the v1.1 shape: **STOP on that element, record the exact gap in your return (a contract conversation with the hub), and build the rest.** Never invent fields, endpoints, or event shapes. Mocks must conform to OBSERVED payload shapes (probe first, then parse what you saw).

## 5. Deliverables

1. **The verdict-surface UX** in `web-ui/dashboard/` (Preact + TS per the skill): the three hero questions answerable per entity/automation-run, with the §2 vocabulary rendered distinctly; microcopy honoring the honesty brand ("says less, truthfully" — e.g., superseded is calm, not alarming; unconfirmed is honest, never dressed as success OR failure).
2. **The return file** (the ONE spine artifact): what shipped, screens/evidence, every claim with file:line, the §10 pre-commit change-set audit (exact path count for Nick's staging glance), any v1.1 contract gaps (flagged verbatim), any core-side proposals, and the skill-§4a discrepancy note.

## 6. Done-when

The three hero questions render from real/fixture verdict streams with: all ten outcomes distinctly renderable (zero flattening); superseded = deliberately-superseded (never a failure); `unconfirmed`/timeout = honest-can't-know (never success, never generic failure); identify renders the immediate honest UNCONFIRMED per the §1 pin; brightness as percent-from-`brightness_percent`; WCAG + design tokens per the skill; **zero v1.1 improvisations** (gaps flagged, not filled); the frontend build green (`frontend.yml` is the lane's CI surface — and the lane's local green is NOT the gate of record; Nick's push is).

## 7. Disciplines (pointers, not copies)

Env-model first (`context/process/cowork-environment-model.md` — esp. §2 mount-lag/phantoms, §4 lock-free porcelain ONLY, §9 the esbuild-SIGSEGV sandbox class: if a build must run in-lane, use the /tmp-copy-proven-≡-mount pattern with esbuild-wasm on the BUILD COPY only; §10 exact counts). Baseline: core `959f925` — state it in your return; if HEAD differs at your launch, run the baseline-shift protocol (record, don't absorb). Quotes are evidence; labels are claims. Your return gets a two-layer hub audit — write it so every claim is checkable.
