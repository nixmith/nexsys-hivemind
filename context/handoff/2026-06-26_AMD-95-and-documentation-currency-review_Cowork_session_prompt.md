<!--
file: context/handoff/2026-06-26_AMD-95-and-documentation-currency-review_Cowork_session_prompt.md
purpose: Dispatch-ready brief for a FRESH Cowork conversation that runs (1) the review-to-ratify-readiness of AMD-95 (the §8.C command-pipeline currency amendment) AND (2) a broader DOC-VS-SOURCE CURRENCY SWEEP across the documentation surface — catching latent drift (the way the Doc 07 §3.11 / AMD-90 drift was caught) BEFORE the next milestone authors against stale prose. Runs in COWORK (not the DOCS Project) so it has direct repo + frozen-source access to source-verify every doc claim. Review ONLY — propose, do not fold.
audience: a FRESH Cowork conversation acting as a documentation reviewer (nexsys-project-manager skill, Mode-1 review discipline, with file + bash source access), Nick (rule scope / co-sign / fold / ratify)
state-type: session prompt (documentation currency + amendment review)
status: READY — authored 2026-06-26 by the v6 hub. Off the M7.4 critical path; runs in parallel. The AMD-95 half gates the §8.C ratification (which precedes M7.4a authoring), so prioritize Tier 1.
why Cowork, not the DOCS Project: this review must SOURCE-VERIFY doc claims against the frozen Java at HEAD `5363347` (signatures, event sets, counts, type names) — that needs repo + bash access the DOCS Project conversation does not have. Use the file tools as authoritative (env-model), git `--no-optional-locks` for read-only state.
baseline: docs `e47f01e` (+ the uncommitted Doc 17 DRAFT + AMD-95 PROPOSED, if Nick has not yet committed them — confirm on disk) / core `5363347` (M7.3 — the frozen source to verify against) / hivemind `837e743`. Confirm at a light preflight.
reads (in order):
  - context/process/cowork-environment-model.md (FIRST — path duality; truncated-tail mount artifact; host file tools authoritative; git index.lock hazard → use --no-optional-locks)
  - project-manager/references/freshness-preflight.md (run a light preflight) + references/review-and-quality.md §1 (design-doc review checklist) + references/constraint-enforcement.md
  - homesynapse-core-docs/design/amendments/AMD-95_Command-Pipeline_Currency_Event-Driven-Co-Located.md (THE ANCHOR — Tier 1)
  - the §1 decision record context/decisions/2026-06-25_deeper-M7-automation-architecture_decision-record.md (D1 the event-driven shape AMD-95 affirms; D2/D3 the constraints)
  - the docs-repo documentation surface (Tier 2 — design/00–17, design/amendments/AMD-*, governance/) + the frozen Java under homesynapse-core (the source of truth)
-->

# Session Brief — AMD-95 review + a documentation-currency sweep (Cowork, source-verifying)

You are a **fresh Cowork documentation reviewer** (nexsys-project-manager skill, Mode-1 review discipline) with **direct repo + frozen-source access**. Your two jobs: (Tier 1) take **AMD-95** to ratify-readiness, and (Tier 2) run a **doc-vs-source currency sweep** across the documentation surface so the recurring "the docs describe a thing the code never built" failure (the M7.3 [REVIEW]s; the §3.11/AMD-90 drift AMD-95 fixes) is caught **systematically**, before the next milestone authors against stale prose. Read `context/process/cowork-environment-model.md` FIRST, then a light freshness preflight.

## 0. The scope call (stated explicitly — Nick confirms; the "all documentation, including or not including amendments" question)

**Scope = the `homesynapse-core-docs` documentation surface:** the design docs (`design/00`…`design/17`, incl. the Doc 17 DRAFT), the **amendments** (`design/amendments/AMD-*`), and the governance docs (`governance/` — invariants register, Locked decisions, Glossary/DAS, the MVP doc). **Amendments are IN scope — as currency-cross-check targets, NOT free-edit targets.** A ratified AMD is a point-in-time governance record; you do **not** rewrite its ratified substance. Where an amendment has drifted from the shipped source (exactly the AMD-90 §2.1 case AMD-95 handles), you **propose the remedy** — a "superseded-in-part / currency" note, or a new currency amendment (the AMD-95 pattern) — for Nick to fold via review→ratify. **Never silently edit a ratified amendment.**

**OUT of scope:** the hivemind spine (`PROJECT_SNAPSHOT`, `pm-handoff`, the backlog, decision records) — those are the hub's living, continuously-reconciled state, not the Locked architecture this sweep audits. (You may note a glaring hivemind-reference-doc currency miss as a low-priority aside, but do not sweep it.) **If Nick wants a different cut** (e.g. include the hivemind `references/`), that is his call at the top of your return.

## Tier 1 — AMD-95 to ratify-readiness (the anchor; gates §8.C → M7.4a)

AMD-95 reconciles Doc 07 §3.11 / AMD-90 to (a) the §1-ratified **event-driven/co-located** dispatch shape (D1) and (b) the frozen source the M7.3 [REVIEW]s mapped. Verify it:

1. **Source-verify every frozen-signature claim at HEAD `5363347`** (use bash/grep against `homesynapse-core`): `CommandIssuedEvent` is the 5-component record `(Ulid targetEntityRef, String commandType, String parameters, int confirmationTimeoutMs, CommandIdempotency idempotencyClass)` and carries no expectation; `CommandAction` is the 4-field record `(Selector, String commandName, Map, UnavailablePolicy)` with **no** `confirmation` component; the confirmation signal is the **capability's** `ConfirmationPolicy.mode()` / device-model `ConfirmationMode` enum incl. `DISABLED`; `CommandDispatchService.dispatch(EventId, EntityId, String, Map)` is in-process and nothing publishes `command_issued` in main; the expectation is derived from the capability's `CommandDefinition.expectedOutcomes()`. Confirm each — flag any mismatch.
2. **Rule the AMD-90 §2.1 supersede-in-part** — is "withdraw the `CommandAction.confirmation` 5th component + the automation-resident `ConfirmationPolicy{OPTIMISTIC,REQUIRED,BEST_EFFORT}` enum for the V1 engine; confirmation is capability-sourced" the right disposition, and is AMD-90-INV-01 (no-retry) correctly left untouched? Confirm AMD-90's `RepeatAction`/`InvokeAutomationAction` items are correctly out-of-scope (flag-only).
3. **Confirm zero impact:** no event-type mint (counts stay 71/41/53), no module-info change, no source change from the amendment itself.
4. **Verdict:** RATIFY / RATIFY-WITH-EDITS / REVISE, with a consolidated edit list + the precise Doc 07 §3.11.1/§3.11.2/§16 + AMD-90-note edits to apply at ratification.

## Tier 2 — the documentation-currency sweep (the broaden; prevent the next §3.11)

The principle (v6 §4 governance discipline): **doc-to-doc consistency is necessary but not sufficient — a fabrication can be perfectly consistent without being true.** Source is the only ground truth. Sweep the documentation against the frozen Java at `5363347`, **prioritized by what M7.4 and the near-term milestones will author against** (don't boil the ocean):

- **HIGH (M7.4 + read-API author against these):** Doc 07 (the rest of §3 beyond §3.11 — run/action/dispatch/selector contracts vs the shipped `StandardRunManager`/`StandardActionExecutor`/`CommandDispatchService`); Doc 02 (device model / capability / `CommandDefinition`/`ExpectedOutcome`/`ConfirmationMode` / `EntityRegistry`); Doc 01 (event model — the AMD-92 event set vs the source roster; **re-derive counts 71/41/53 from source, never propagate**); Doc 03 (state store / `StateQuery`); Doc 05 (integration runtime).
- **MEDIUM:** Doc 12 (lifecycle / composition root vs `HomeSynapseCore`), Doc 06 (config), Doc 15 (crypto — AMD-94 envelope tag), the governance invariants register (every cited `INV-…` resolves; the 169/49 total re-derives from the §17 table).
- **For each finding, record a drift-register row:** the doc claim (file+section) · the source reality (file+line/signature) · classification (genuine drift / cosmetic / acceptable-forward-shape) · proposed remedy (currency note / new currency amendment / no-op) · priority. **Distinguish "the code hasn't built it yet" (a not-yet-wired forward note, like §3.11.1's shape until M7.4) from "the doc describes a thing the code built differently" (a genuine drift, like the ExpectationFactory/ConfirmationPolicy-placement).**

## Disciplines (bind)

Source is truth — re-derive every count/signature from `homesynapse-core` at `5363347`, never copy-forward a stated number (the v5 catch). Host file tools authoritative; VM git suspect (truncated-tail; `--no-optional-locks`). **Review-separate-from-fold** — you PROPOSE; you do **not** edit the design docs, the amendments, or mint invariants. **Never self-ratify.** No-engine-retry / no-templating-DSL / local-first-inviolate are anti-requirements the docs must still honor.

## Done-when

A **documentation-currency review return** on disk (`context/audits/2026-06-DD_AMD-95-and-doc-currency_review_return.md`) with: (Tier 1) the **AMD-95 verdict** + consolidated edit list + the source-verification result per signature; (Tier 2) a **prioritized drift register** (doc-claim vs source-reality vs proposed-remedy, HIGH→LOW); and a one-paragraph recommendation on sequencing the remedies (which currency notes/amendments to fold before M7.4a vs which can wait). **Do NOT fold anything.** Hand the return to Nick → he co-signs AMD-95 (→ Doc 07/AMD-90 edits + watermark 94→95) and rules which Tier-2 remedies to schedule. Hand over a bang-free, backtick-free commit message for the return.
