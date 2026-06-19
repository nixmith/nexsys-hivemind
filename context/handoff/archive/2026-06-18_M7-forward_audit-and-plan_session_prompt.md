<!--
file: context/handoff/2026-06-18_M7-forward_audit-and-plan_session_prompt.md
purpose: Dispatch-ready brief for a FRESH Cowork session that (A) SECOND-CHECKS the just-landed M7.1 work and its WUCP Phase 2 closeout, then (B) produces the FULL M7-FORWARD PLAN — scoping and sequencing M7.2, M7.3 (and the M7→M8 boundary) with the three interlocks that changed this week baked in: Doc 16 (superiority design) gates the M7.2 action-model freeze, the composition-root wiring is deferred to app-bootstrap, and the D2/REC-162 retry question is live. Output: a verification verdict + a recorded M7-forward plan that drives the next coding and design sessions.
audience: PM/Architect (a FRESH Cowork conversation, nexsys-project-manager skill — Mode 3 Director for the plan, with a Mode-1 Architect read of Doc 16's M7-impact section), Nick (rules sequencing + any contract-shaping calls)
state-type: session prompt (verification + Phase-3 planning)
status: READY — authored 2026-06-18 after M7.1 landed GREEN. Run as a fresh Cowork conversation.
baseline: core `beb4bc3` (M7.1 committed+pushed; substantive HEAD now beb4bc3) / docs `f2e064d` (UNCHANGED — Doc 16 is an UNTRACKED DRAFT, not yet committed) / hivemind `0f3951f` (M7.1 WUCP Phase 2 + converge-era hygiene committed+pushed). M6 COMPLETE; M7.1 DONE (gate-verified GREEN, ./gradlew check 149 tasks); watermark AMD-93 (invariants 163/47); Doc 15 LOCKED; M7.2 = NEXT.
reads (in order):
  - context/process/cowork-environment-model.md (FIRST)
  - context/status/PROJECT_SNAPSHOT.md (the 2026-06-18 "latest" M7.1-GREEN masthead note + Current-WU)
  - context/handoff/pm-handoff.md (the 2026-06-18 M7.1 WUCP Phase 2 record — gate-fix, [REVIEW] adjudications, next-WU)
  - context/handoff/coder-handoff.md (the M7.1 entry + gate-fix round 1 + the refuse-to-close next-WU=M7.2 pointer) + context/lessons/coder-lessons.md (the FIX-07 / §authoring-vs-module-graph lesson)
  - context/decisions/2026-06-18_app-bootstrap-and-superiority-scope_decisions.md (Part B superiority scope ruling + the M7 interlock verdict + the M7.1 composition-root-wiring-deferral ADDENDUM)
  - context/planning/phase-3-milestone-backlog.md (the M7 row → M7.1 DONE / M7.2 NEXT; the AB-1..AB-4 + Doc 16 + split-doc rows)
  - context/planning/2026-06-12_M7-M8-charter-skeleton.md + context/planning/2026-06-12_M7-blueprint_merged-disposition.md (the M7/M8 piece decomposition + the M7.x obligations)
  - core/automation/MODULE_CONTEXT.md + core/event-model/MODULE_CONTEXT.md (the M7.1 reality — type inventory, the new permits/records, the gotchas)
  - homesynapse-core-docs/design/16-superior-automation.md (the Doc 16 DRAFT — read §4/the M7-contract-impact section closely; it gates M7.2's scope) + homesynapse-core-docs/design/07-automation-engine.md (the Locked baseline automation contract) + design/amendments/AMD-88..93
  - context/planning/2026-06-15_app-bootstrap_charter.md (AB-3 carries the deferred M7.1 wiring; the residual gates) ; references/coding-instruction-format.md + references/cross-subsystem-awareness.md (if the M7.2 instruction is dispatched)
-->

# Session Brief — M7.1 Second-Check + the M7-Forward Plan (M7.2 / M7.3 scope + sequencing)

PM/Architect session (**nexsys-project-manager** skill). Read `context/process/cowork-environment-model.md` FIRST, then run the freshness preflight against the pinned baseline above. **This session has two payloads; do them in order.** Part A is a focused verification (is M7.1 truly closed out and sound?); Part B is the main deliverable (the M7-forward plan). Nick rules sequencing and any contract-shaping call; you assemble, verify, plan, and record.

**Step 0:** preflight; reconcile HEADs. Expected state: the spine was reconciled at M7.1's WUCP Phase 2 (hivemind `0f3951f`), so this should be **PASS** — but verify, because the codebase advanced (`beb4bc3`) and a STALE result here would mean the M7.1 closeout under-recorded something. **Note explicitly: Doc 16 is an UNTRACKED DRAFT in the docs repo (not committed, not reviewed, not Locked).** Do NOT treat it as Locked ground.

---

## PART A — Second-check the M7.1 landing (verify before you plan forward)

M7.1 passed the full gate (`./gradlew check`, 149 tasks) and a WUCP Phase 2 closeout ran. **Confirm that closeout is sound and the governance is internally consistent before building the forward plan on top of it.** You cannot run Gradle (the gate already passed; do not re-litigate the build) — verify the *record*, the *deferrals*, and the *source-vs-claim* consistency:

1. **Closeout consistency.** Backlog M7.1 = DONE; snapshot + pm-handoff + MODULE_CONTEXT ×2 + coder-lessons all agree; the FIX-07 instruction correction is in place; watermark still AMD-93 (no new AMD landed — confirm). Flag any drift.
2. **The deferrals are correctly tracked (no silent debt).** Three things were deferred at M7.1 — verify each has a named home: (a) the composition-root wiring (the `automation_engine` subscriber + the config-loading/schema-registration + the lifecycle wiring test) → **app-bootstrap AB-3** (the decision-record addendum's inbound dependency); (b) the FIX-07 config-edge lesson (the `core→config` ban) is captured so M7.2/M7.3 cannot repeat it; (c) the schema fragment lives in the config-free `AutomationSchema` holder, not lost.
3. **The [REVIEW] adjudications hold.** Re-check the six adjudicated deviations (3 substrate gaps routed forward — slug-tombstone, first-class `Area` slug, `Availability` asleep-vs-dead granularity; 3 behavioral defaults recorded — multi-entity condition all-of/empty→false, EventTrigger event-type-only matching, device-subject `entityRef` flattening). Confirm none of the three behavioral defaults silently constrains M7.2's design in a way the plan must now account for (especially the condition semantics and the `entityRef` flattening, which M7.2's run/action model touches).
4. **Source round-trip spot-check (Check 11).** Spot-verify that the M7.1 types the forward plan will cite actually exist as named (e.g., `StandardTriggerEvaluator.evaluate` returns the matched-IDs decision; the AMD-92 slice rows that landed vs the rows M7.2 still owes). No fabricated forward dependencies.

**Part A done-when:** a short **M7.1 verification verdict** (PASS, or PASS-WITH-FINDINGS with each finding logged + owner). If a finding is material (a closeout gap, a silent contract constraint), fix it under WUCP discipline before Part B; if cosmetic, log and proceed.

---

## PART B — The M7-forward plan (the main deliverable)

Produce the **scope + sequencing plan for the rest of M7** (M7.2, M7.3, and the M7→M8 boundary), integrating the three interlocks that changed this week. This is a planning deliverable (a charter-grade plan), not a coding instruction — though it MAY end by dispatching the M7.2 instruction if (and only if) its entry-gate is clear (see done-when).

**The three interlocks the plan MUST bake in (these are the new constraints since the M7/M8 charter skeleton was written):**

- **I1 — Doc 16 gates the M7.2 action-model freeze.** The Part-B ruling (decision record): M7.2 builds *into* Doc 16; **do not freeze M7.2's action-model contract before Doc 16 Locks.** So Doc 16's review → Lock is a **hard prerequisite** for the action-model half of M7.2. Read Doc 16's §4 M7-contract-impact section: confirm it states M7.1-UNAFFECTED / M7.2-SHAPED / M7.3-UNAFFECTED, and that its "shaped" claims about the action model are consistent with the landed M7.1 reality. The plan must sequence Doc 16 review→Lock and partition M7.2 into "baseline, buildable now" vs "Doc-16-shaped, gated on Lock."
- **I2 — the composition-root wiring is deferred to app-bootstrap.** M7.1 built against injected/stubbed deps because the runtime assembles no `ConfigurationService`/registries. Determine whether **M7.2 can likewise build against injected deps** (run/action/dispatch logic + the event slice, gate-verified without a live composition root) — almost certainly yes, same pattern — and explicitly route M7.2's eventual wiring to app-bootstrap AB-3 too. State the boundary: what M7.2 builds-and-tests now vs what it hands to AB-3.
- **I3 — D2 / REC-162 (retry vs Expectation) is a live M7.2 action-model question.** The standing escalation: does the field's retry demand belong as a *guarded, expected-state-gated* bounded re-issue in the sealed action model, or is it already satisfied by `Expectation` + AMD-90 confirmation? **Do NOT flip the REC-162 anti-retry silently.** This is a Nick call, tied to Doc 16's expressiveness/action-model section. The plan must say WHEN it gets decided (before or at M7.2 scoping) and route it.

**Assemble the M7-forward plan answering each of these:**

1. **M7.2 scope decomposition.** From the M7/M8 charter skeleton + merged disposition: the baseline run/action/dispatch pieces (`ActionExecutor`, `RunManager`, `CommandDispatchService`, the AMD-91 `RunContext`→`RunCausalChain` swap, the AMD-92 event-slice rows 2/4–10/17/18). Mark each piece **baseline-buildable-now** vs **Doc-16-shaped (Lock-gated)**. Apply the P1 milestone-sizing smell-test — if M7.2 exceeds ~3 sub-pieces, split it into first-class sub-milestones with their own done-whens.
2. **M7.3 scope.** The pending-command ledger (`PendingCommandLedger`, command confirmation/timeout, the F5 slice; C4 placeholder records precede it). Confirm M7.3 is UNAFFECTED by Doc 16 (per the verdict) and state its dependency on M7.2.
3. **The Doc 16 review→Lock prerequisite.** Recommend the path: is Doc 16 review-ready (13 sections substantive, §4 present, anti-requirements held)? Fold the DOCS review into a dispatch, or dispatch it separately — but it must Lock before M7.2's action contract. Sequence it explicitly.
4. **M7.2-vs-app-bootstrap sequencing (one Coder; both are priority lanes).** App-bootstrap is the runnability unlock (gated on CC-1 run + R-γ return + AMD-94 ratify + its coding instruction) and it provides the composition-root wiring M7.1/M7.2 defer to it. M7.2 (or its baseline half) can build in parallel. Recommend the interleave: which lane takes the next Coder slot, and why. Respect the P6 non-Core floor if a non-Core lane is in the window.
5. **Route the M7.1 substrate gaps** (slug-tombstone → identity/device; `Area` slug → device-model AMD-44 Stage-2; `Availability` granularity → integration/device per R-δ AX-8) to their consuming WUs with a one-line owner each, so they are not forgotten.
6. **M7.2 entry-gate** (the table): what must be GREEN before the M7.2 coding instruction issues (Doc 16 Locked for the action-model half; D2/REC-162 ruled or explicitly scoped-out; the C3 cascade-doc-fix — already landed `03f16dc`; the construction-site sweep + carry-pins). Owners + open/closed.

**Part B done-when:** a recorded **M7-forward plan** (write it to `context/planning/` and reflect it in the backlog + W26) stating: M7.2 scope (baseline-now vs Lock-gated, sized per P1), M7.3 scope, the Doc 16 review→Lock prerequisite + its sequencing, the M7.2-vs-app-bootstrap interleave recommendation, the substrate-gap routing, and the M7.2 entry-gate. **EITHER** dispatch the M7.2 coding instruction (only if its entry-gate is fully GREEN — i.e., Doc 16 Locked + D2 ruled) **OR** state the precise, owner-tagged gate list that blocks the M7.2 issue. Escalate to Nick: the sequencing call, the D2/REC-162 decision, and anything implying a new invariant or an M7-contract reshape (those move through the formal AMD pipeline, never a silent reshape).

---

## Anti-requirements (bind both parts — non-negotiable)
No templating DSL (expressiveness comes another way) · **no engine retry unless Nick reopens REC-162 (D2) explicitly** · no destructive forced migration · never lead with commodity encryption · local-first is inviolate. **M7.2's action-model contract does not freeze before Doc 16 Locks.** Locked design docs (07, 15, and Doc 16 once Locked) move only via the formal re-open→review→ratify pipeline. The `core→config` module edge is banned — config wiring rides the composition root (app-bootstrap), never a `requires config` in a core module.

## Closeout (record where it belongs)
Record the M7-forward plan in `context/planning/`; update PROJECT_SNAPSHOT (masthead + Current-WU), the backlog (M7.2/M7.3 rows + any sub-milestone split), and the W26 lanes; run the WUCP drift check; hand over commit messages (bang-free / `git commit -F`). If the M7.2 instruction is dispatched, also run the §4b deferred-gate setup and the consumer/pin survey per `references/coding-instruction-format.md`. Escalate any new-invariant / M7-contract reshape — those are Nick's calls.
