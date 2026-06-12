<!--
file: context/handoff/2026-06-05_M3-M4_foundation-readiness-retrospection_session_prompt.md
purpose: Priming prompt for a fresh Cowork conversation — a forward-looking, artifact-level readiness retrospection of the M3→M4 system (docs + code), surfacing what's missing/thin for the harder modules ahead.
audience: Nick (to paste into a new Cowork session)
state-type: instruction
status: READY
-->

# Cowork Session Prompt — M3→M4 Foundation-Readiness Retrospection (forward-looking gap analysis)

You are the NexSys Project Manager / senior systems architect. **First action: invoke the `nexsys-project-manager` skill, run the session-start freshness preflight, and report the result before anything else.** (Expected PASS — the hivemind was reconciled to M4 COMPLETE on 2026-06-05. If STALE/CONFLICTED, stop and follow the skill's protocol.)

**This is a documents-only analysis session. No code, no coding instructions, no amendments.** The only output is one assessment document.

## What this is — and is NOT

This is **not** a process retrospective. The M4 *process* retro already exists at `nexsys-hivemind/context/audits/2026-06-05_M4-retrospective.md` — read it for context, but do not repeat it.

This **is** an **artifact-level, forward-looking readiness assessment** of the *system as designed and built across M3 → M4* (event distribution, state projection/derivation, persistence, the device + value model, the integration-api contract freeze, the composition root, and the foundational invariants/contracts). It answers one governing question:

> **When we build the harder modules that come next — M6 Configuration + secrets/crypto, M7/M8 Automation, M9 Integration Runtime, M10/M11 REST + WebSocket APIs, M12 Observability, M13 Lifecycle, M14 Zigbee, M15 validation — and the longer-horizon invariants (multi-user identity + RBAC, energy as a first-class event domain, on-device AI, network/mesh telemetry, multi-hub/cloud sync, tamper-evidence + crypto-shredding) — what will those modules NEED from the M3→M4 foundation that ISN'T THERE YET, is under-specified, is stubbed/placeholder/dead, or is too THIN for the complexity that's coming?**

The objective: deeper insight into the current state — the documentation or functionality we missed or should expand on (in writing and/or code) because it will matter a great deal for the more complex modules, now or later. The value of this session is the **forward lens**, not a recap of what we built (that's already in the snapshot).

## Scope

- **Code and docs together** — both `homesynapse-core` (HEAD `8ef9e9f`, M4 COMPLETE, watermark AMD-64, `projectionVersion` 5) and `homesynapse-core-docs` (design + governance).
- **Window:** M3 (event bus / state projection / composition root) through end of M4 (projection-derivation foundation, device-model breadth incl. Floor/Area/EntityRole, integration-api freeze AMD-54..64). M0–M2 are in scope only where they bear on the forward question.

## Prime your context precisely — read these first, in order

1. `nexsys-hivemind/context/strategic-context-map.md` — the routing map.
2. `nexsys-hivemind/context/status/PROJECT_SNAPSHOT.md` — current state + milestone history + the long Open-Items trail.
3. `nexsys-hivemind/context/relay/2026-05-28_codebase-investigation-for-rust-deliberation.md` — a verified, source-cited codebase investigation taken at the **start of M4**. **Sections G (Forward-Looking Foundations — IN CODE / SPEC-ONLY / FUTURE verdicts) and H (open questions + §H5 material debt) are your highest-value starting inventory.** ⚠️ It is the *pre-M4* baseline — M4 has since shipped Floor/Area/EntityRole, the typed-value pipeline, the now-wired AtomicCheckpointWriter, the DispatchingProjectionAdvancer, and the integration-api freeze — so **re-verify every relevant finding against HEAD `8ef9e9f`** before relying on it.
4. The 14 design docs `homesynapse-core-docs/design/01-…` … `14-…` — especially 01 (event), 02 (device/capability), 03 (state/projection), 04 (persistence), 05 (integration runtime), 06 (configuration), 07 (automation). Read the §8 Key Interfaces and the behavioral contracts.
5. The `MODULE_CONTEXT.md` files for every core module (`homesynapse-core/**/MODULE_CONTEXT.md`) — verified type inventories, cross-module contracts, **Gotchas**, and **Phase-3 notes**. This is where "thin contract" and "deferred" appear concretely.
6. `homesynapse-core-docs/governance/Architecture_Invariants_v1.md` — the 133 constitutional invariants. **Many are "Architecture only" / forward-looking (energy §12, multi-user §13, mesh §14, AI §11). The gap between an invariant's promise and the code that exists is the heart of this analysis.**
7. `nexsys-hivemind/context/planning/phase-3-milestone-backlog.md` — the M5–M15 "Future Major Groups" and their dependencies (what's coming, and what each needs from the foundation).
8. `nexsys-hivemind/context/open-questions.md` + the amendment register `homesynapse-core-docs/design/amendments/` (AMD-01..65). The amendment trail shows where the *original* design was thin enough to need patching — a leading indicator of where it's still thin.
9. The curated spine — `nexsys-hivemind/project-knowledge/HomeSynapse_Knowledge_Primer.md` + `HomeSynapse_Current_State.md` — for the compressed mental model.

## Method (non-negotiable)

- **Source-verify everything.** Read the actual code and docs; cite `file:line`. Distinguish **IN CODE** vs **SPEC-ONLY** vs **FUTURE/absent** (the investigation's verdict discipline). Do not trust any summary — including the pre-M4 investigation — without re-checking against HEAD.
- **Label every finding as one of three:** (a) **deliberate deferral** — tracked, fine (note and move on); (b) **genuine miss** — should exist, doesn't, nobody's tracking it; (c) **thin contract** — exists but is under-specified/under-built for the complexity the consuming module will demand. **(c) is the most valuable and the most easily overlooked.**
- **Forward-map every finding** to the specific future module(s) it threatens and *when* it bites (M6? M9? the energy/B2B horizon?).
- **Be genuinely critical.** Surface what's missing or thin, not what went well. The uncomfortable findings are the point.

## Deliverable

Write `nexsys-hivemind/context/audits/2026-06-XX_M3-M4_foundation-readiness-assessment.md` (today's date; house audit format — metadata header, numbered sections, tables where they aid scanning). Structure:

1. **What the M3→M4 foundation actually provides** — brief baseline; don't rehash the snapshot.
2. **Documentation gaps** — under-specified contracts, missing design depth, stale/inconsistent governance trail (e.g., the AMD-34/AMD-37 annotation misses + AMD-37 body stale vs shipped code; the Phase-2 traceability stubs for 10 docs; the permanent mixed event-naming convention; PLAN-M4 currency). Each mapped to the module that needs the missing detail.
3. **Functional gaps** — stubbed / deferred / placeholder / dead code a future module depends on (automation Tier-2 stubs, `WithinTolerance.evaluate()`, backup/restore, the dead supervisor retry loop, `CommandHandler` routing, the greenfield crypto/SecretStore, INV-SE-04 least-privilege unenforced, the `Main.java` shim).
4. **Thin-contract risks** — contracts that exist but won't carry the weight: is the event/payload model rich enough for energy event types and AIoT? Is the capability/AttributeValue system deep enough for M7 automation + M14 device breadth? Is the just-frozen integration-api actually sufficient for the M9 supervisor + the multi-protocol future, or did we freeze something too thin? Is identity-by-convention (`actorRef` as bare `Ulid`) enough before multi-user? Is `Area` deep enough now that `Floor` exists?
5. **Forward-looking foundation readiness** — a table over the long-horizon invariants (identity/RBAC, energy events, on-device AI pipeline, network/mesh telemetry, multi-hub, crypto/tamper-evidence) with IN-CODE / SPEC-ONLY / FUTURE verdicts at HEAD `8ef9e9f` and an "expand now vs later" call for each.
6. **Prioritized recommendations** — per finding: severity, the module it threatens, and **expand-now / expand-just-in-time / accept-and-track** — the bar for "expand now" being *foundational AND cheaper-now-than-later*. End with the handful of items that, left thin, will most hurt the harder modules.

Close with a one-paragraph honest verdict: is the M3→M4 foundation deep enough to carry what's coming, or are there specific places to reinforce before we build on top of them?
