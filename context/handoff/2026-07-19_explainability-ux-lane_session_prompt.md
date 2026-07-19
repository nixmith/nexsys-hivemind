<!--
file: context/handoff/2026-07-19_explainability-ux-lane_session_prompt.md
purpose: Dispatch brief for the explainability-UX lane (fresh Cowork conversation; nexsys-frontend skill v1.4) — REFRESHED 2026-07-19 by the v34 hub, superseding the 2026-07-06 brief (archive at the next hygiene pass). The lane renders the moat's HONEST VERDICTS — the hero questions on live vocabulary. Dispatching this brief IS the G1 [M] M14-trigger condition; the lane then runs fully parallel.
audience: The explainability-UX lane (Cowork); Nick (launch + return relay).
state-type: session prompt (lane; write-isolated).
status: READY — launch on Nick's word. Zero bench dependency.
write-isolation: `homesynapse-core/web-ui/dashboard/**` + ONE return file (`nexsys-hivemind/context/audits/2026-07-19_explainability-ux-lane_return.md`). NOTHING else — no spine writes, no core-Java writes, no skill edits, no commits (Nick commits; the hub audits first).
baseline: core `554e18c` (W2-LEARN; deployed at the Pi) — state it in your return; if HEAD differs at your launch, run the baseline-shift protocol (record, don't absorb).
-->

# Lane Brief — Explainability UX (the verdict surface) — 2026-07-19 refresh

You are a **frontend lane** (nexsys-frontend skill **v1.4** — read its §4a vocabulary, §4c field-evidence, and the FROZEN-v1.1 grounding rule first; v1.4 is CURRENT as of 2026-07-18, but source still outranks — re-verify the vocabulary at `CommandResultEvent.java` before rendering). You consume the **live** verdict vocabulary — real events, never invented screens. The hub never implements; you never write outside your isolation set.

## 1. The charter (Nick's scope ruling, verbatim — this IS the boundary)

> *"honest-can't-know vs known-failed vs deliberately-superseded are its entire vocabulary."* (Nick, v18 beat-5.)

The hero questions: **why did it fire? / why didn't it? / did it actually confirm?** The differentiator is that these render HONESTLY — `StandardExplanationService`'s UNCONFIRMED/FAILED flattening erases exactly what this surface sells (§3). Related pin (v18 beat-5, verbatim — identify-class commands): *"an immediate rendered `UNCONFIRMED` verdict with recorded reason, not the silent DISABLED bypass; never-tracked and honestly-verdicted are different promises."*

## 2. THE LIVE VOCABULARY (skill v1.4 §4a carries the TEN-value `command_result.outcome` set — re-verify at `core/event-model/.../CommandResultEvent.java:22-27` at launch)

`acknowledged` | `rejected` | `timed_out` | `invalid` | `unsupported` | `handler_error` | `integration_unavailable` | `superseded` | `expired_on_restart` | `unconfirmed`. `state_confirmed` = six components (`StateConfirmedEvent.java:26-33` — the causal join naming BOTH the command and the proving report). `command_confirmation_timed_out` = honest can't-know at deadline. Brightness: 0–254 canonical; render percent from the DERIVED `brightness_percent`, never client-side rescale.

## 3. The NAMED TARGET (unchanged — render what the service erases; do not modify it)

`StandardExplanationService` collapses distinct verdicts into `ACTED_BUT_UNCONFIRMED`/FAILED-class renderings. The lane's surface keeps the distinctions: deliberately-superseded (calm, never a failure) vs honest-can't-know (`unconfirmed`, timeout) vs known-failed (`rejected`, `handler_error`, `unsupported`, `invalid`, `integration_unavailable`). Core-side fix proposals go in your RETURN (exact file:line + needed behavior); the hub folds them into a core WU.

## 4. THE FIELD-EVIDENCE SET (every item silicon-proven on the certified deployed build — your fixture/rendering obligations, all pointered in skill v1.4 §4c)

1. **The flattening has field reps** (the soak close-out + the 2026-07-18 bench `[PASS]` evidence line: `outcomes ['UNCONFIRMED','UNCONFIRMED','FAILED','UNCONFIRMED','DISPATCHED']` — the FAILED is a superseded flattening in the wild).
2. **THE SILENT-SKIP RUN CLASS:** a COMPLETED run with `actionCount>0 / commandCount=0 / empty actions[]` = lawful Doc 07 §3.9 per-target skips of UNAVAILABLE targets — currently invisible end-to-end. Until the SKIP-VIS core WU lands, **render do-nothing runs honestly, never as clean success** (the actionCount-vs-actions[] disagreement is the tell).
3. **Prior-instance runs render `automationName`/`trigger.type` null** (instance ULIDs re-mint per YAML load) — render the null-name class honestly.
4. **Availability is silicon-proven BOTH directions with measured envelopes:** honest UNKNOWN at boot · UNAVAILABLE on evidence at ping-resolution (minutes-scale BY DESIGN) · returns 0.7 s warm / ~50 min dead-air cold-start. Render staleness as evidence-with-age, never a binary lie.
5. **NEW — the posture-downgrade class (the joins night, 2026-07-19):** the live S31 carries `confirmation_downgraded … posture=VERIFIED_REPORTS/SLEEPY outcome=best_effort` — a device whose confirmation posture honestly degraded (configure-verify timeout) and is upgradeable later. best_effort is a POSTURE, not a failure — it needs its own calm rendering distinct from any verdict.
6. **NEW — the rehydrated-availability exhibit:** the Hue is physically off-network yet reads API `AVAILABLE` from rehydrated history (the AVAIL-RECONCILE class) — exactly why the surface renders last-evidence-age, never the flag alone.
7. **The live fleet is your real-data source:** re-derive at launch via the read-API (expected ≥6 devices/entities post-04P: light · occupancy · switch · temp/hum/battery · contact · battery-only). Mocks conform to OBSERVED payload shapes — probe first.

## 5. The FROZEN v1.1 read-API rule (unchanged: flag, don't improvise)

The contract is FROZEN at v1.1. If any verdict data you need does NOT flow through the v1.1 shape: **STOP on that element, record the exact gap in your return (a contract conversation with the hub), and build the rest.** Never invent fields, endpoints, or event shapes. Note: the LIVE endpoints hand-build **camelCase** wire keys (per-endpoint reality — read at the endpoint, never assume from the module row).

## 6. Deliverables + done-when

1. **The verdict-surface UX** in `web-ui/dashboard/` (Preact + TS per the skill): the three hero questions answerable per entity/automation-run; all ten outcomes distinctly renderable (zero flattening); superseded calm; unconfirmed honest; identify per the §1 pin; the §4 items 2/3/5/6 rendered honestly; availability as evidence-with-age; brightness percent-from-derived; WCAG + design tokens; token-parameterized brand strings (R-1 pending — never hardcode).
2. **The return file** (the ONE spine artifact): what shipped, evidence with file:line, the §10 pre-commit change-set audit (exact path count), v1.1 contract gaps verbatim, core-side proposals.
3. Frontend build green (`frontend.yml` is the lane's CI surface; the lane's local green is NOT the gate of record — Nick's push is).

## 7. Disciplines (pointers, not copies)

Env-model first (`context/process/cowork-environment-model.md` — §2 mount-lag/phantoms · §4 lock-free porcelain ONLY · §9 the esbuild-SIGSEGV class: /tmp-copy-proven-≡-mount with esbuild-wasm on the BUILD COPY only · §10 exact counts · §12 if remote). Quotes are evidence; labels are claims. Your return gets a two-layer hub audit — write it so every claim is checkable.
