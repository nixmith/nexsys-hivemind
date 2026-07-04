<!--
file: context/handoff/2026-06-25_Doc17_independent-DOCS-review_session_prompt.md
purpose: Dispatch-ready brief for a FRESH, CONTEXT-ISOLATED Cowork session that runs the INDEPENDENT DOCS-Project second-opinion review of the Doc 17 "AIoT + Cloud Readiness" beat (DRAFT) before Lock. Same discipline Doc 16 passed before Locking. Its distinct value is INDEPENDENCE ON SCOPE — it must rule the §0 scoping call (new Doc 17 vs Doc-16 extension) on the beat's own merits, assess the [AIOT-INV-1..3] candidates, and source-verify every cited invariant id. Produce a verdict + consolidated edit list. Review ONLY — do not fold.
audience: a FRESH Cowork conversation acting as an independent DOCS reviewer (nexsys-project-manager skill, Mode-1 review discipline), Nick (rule scope / ratify / fold / Lock)
state-type: session prompt (independent design-doc review)
status: READY — authored 2026-06-25. OFF the M7.4 critical path (the Doc 17 beat reserves seams and builds nothing; it gates no milestone), so it runs fully in parallel and delays nothing. Run as its OWN fresh conversation.
baseline: docs `e47f01e` (Doc 16 Locked; AMD-94; 169/49) + the Doc 17 DRAFT (lands with Nick's 2026-06-25 docs commit — confirm it is on disk at `design/17-aiot-and-cloud-readiness.md`) / core `5363347` (M7.3). Confirm at a light preflight.
reads (in order):
  - context/process/cowork-environment-model.md (FIRST — the truncated-tail mount artifact; host file tools authoritative)
  - context/status/PROJECT_SNAPSHOT.md (current state ONLY — for grounding, not for scope rationale)
  - homesynapse-core-docs/design/17-aiot-and-cloud-readiness.md (THE DOCUMENT UNDER REVIEW — read in full)
  - the LOCKED docs the beat composes over, to check it does not foreclose or contradict them: design/16-superior-automation.md (§3.2 component model, §3.3 explainability/audit, §3.5 federation seam, §3.6 hybrid cut-line, §5.3 INV-SA register), design/15-* (§3 chain_hash / crypto-shred), design/01-* (§4.1 CausalContext / immutable log), design/05-* (integration isolation), design/12-* (composition root / lifecycle), design/14-* (master architecture) + governance/Architecture_Invariants_v1.md (the §17 index + the cited ids — independently scan for invariants the beat should cite but doesn't)
  - references/review-and-quality.md §1 (the design-doc review checklist) + references/constraint-enforcement.md
-->

# Session Brief — Independent DOCS-Project Review of the Doc 17 "AIoT + Cloud Readiness" beat (rule the scope)

You are a **fresh, independent DOCS reviewer** for the Doc 17 "AIoT + Cloud Readiness" beat — a DRAFT reserved-architecture artifact submitted for the project's standard pre-Lock independent review (the discipline Doc 15 and Doc 16 passed before Locking). Read `context/process/cowork-environment-model.md` FIRST, then a light preflight (confirm the docs HEAD + that the Doc 17 DRAFT is on disk + core is `5363347`).

## The independence rule (the reason this session exists — read carefully)

The beat's scope was set by a now-first-class strategic direction (Nick elevated AIoT-readiness) and the v6 hub's §1 deliberation. **Your distinct job is to rule the scope on the beat's OWN merits — independently — not to ratify the hub's lean.** Therefore:

- **Form your own view on §0 (the scoping call) FIRST**, from the beat + the Locked dependency docs + the spine. The beat's §0 states the hub's lean (a **new Doc 17**, not a Doc-16 extension) with reasoning; treat that as a position to pressure-test, not a settled call.
- You **may** read the companion `context/decisions/2026-06-25_deeper-M7-automation-architecture_decision-record.md` for the ratified D1–D5 context (the concrete M7.4-gating rulings the beat references), but do **not** treat its framing as binding on your scope verdict. If anything there reads as scope-advocacy that anchors you, note it.

## Your charge — three parts Nick named, scope first

1. **Rule the §0 scoping call (the headline).** Is "AIoT + Cloud Readiness" rightly a **new design doc (Doc 17)**, or should it be a **Doc-16 extension** (e.g. Doc 16 §3.7/§3.8 + a Doc-14 master-architecture note)? Probe specifically: does the subject (the immutable log as the *universal* substrate; cloud replication outward; the AI-safety frame across device-intelligence/authoring/reasoning/dispatch) genuinely cut **across** persistence/event-model/integration/crypto/federation — beyond the automation layer Doc 16 owns — such that a new doc is the right cut? Or is it narrow enough that a new doc is over-structure (a doc that reserves seams but builds nothing)? State your independent verdict with reasoning. (The "epic-under-one-label" failure cuts both ways — under-splitting hides scope; over-splitting fragments it.)

2. **Assess the `[AIOT-INV-1..3]` candidates (§6).** The beat offers three PROPOSED invariant candidates (AI-is-never-an-autonomous-actuator; cloud-is-non-authoritative-and-non-required; every-AI-decision-is-explainable-and-auditable), each framed as a composition of existing parents. Rule each: **mint-at-Lock** (a first-class INV-… in a new subsystem category, the way INV-SA-01..04 minted at the Doc 16 Lock) **vs keep-as-design-principle** (the non-preclusion already rests on the cited parents). For any you'd mint, check it adds a constraint its parents do not already impose (the INV-SA-03/04 citing-composition test — not a droppable near-duplicate).

3. **Source-verify every cited invariant id** against `governance/Architecture_Invariants_v1.md` (the §17 index). The beat leans on **INV-LF-01/02, INV-RF-01, INV-ES-06, INV-SA-01..04, INV-PD-07** (and cites Doc 16 §3.3, AX-7, AMD-90-INV-01). Confirm each id **exists and says what the beat claims it says** — a standard review check (the Research-6 fabricated-id lesson). Flag any id that does not resolve or is mis-cited.

## Full design-doc review (per review-and-quality.md §1)

Judge the beat as a readiness/reservation doc (it reserves seams and builds nothing — that is a legitimate scope, like Doc 16 §3.5/§3.6): precision (every reserved seam has a concrete non-preclusion mechanism, not a hand-wave), consistency (terminology vs the Glossary; cross-refs cite real sections), the **genuinely-non-precluding** test for each seam (does any "reserved" seam smuggle in a design decision that should be its own doc — especially the **NEW cloud-replication seam** and the **SBOM/update seam**?), open-question discipline (BLOCKING/NON-BLOCKING — confirm none gates V1), and that the watermark-unchanged / not-self-ratified / no-invariant-minted posture is correct for a DRAFT.

## Anti-requirements to verify the beat holds

Local-first inviolate (cloud strictly additive, never a dependency; keys never leave the machine) · AI proposes / the deterministic engine disposes (no autonomous actuation; no engine retry — AMD-90-INV-01) · explanation is a pure projection of the log (no parallel trace store — INV-SA-03) · no destructive forced migration (federation/scope additive — INV-SA-02). Confirm each is operationalized in the reservation, not merely asserted.

## Done-when

An **independent review return** on disk (`context/audits/2026-06-DD_Doc17_independent_DOCS_Review_Return.md`) with: a **scope verdict** (new-doc vs Doc-16-extension — your independent reasoning), an **invariant-candidate verdict** (mint-at-Lock vs keep-as-principle, per candidate), the **invariant-id source-verification result** (each cited id: resolves / mis-cited / absent), a **document verdict** (RATIFY-TO-LOCK / RATIFY-WITH-EDITS / REVISE), and a **consolidated edit list**. **Do NOT fold edits into the beat** (review-separate-from-fold). Hand the return to Nick → he rules the scope + folds the consolidated edits → mints any `[AIOT-INV-*]` + (new-doc Lock → watermark stays AMD-94) → co-signs → **the beat Locks (as Doc 17 or as the Doc-16 extension Nick rules).** Hand over a bang-free, backtick-free commit message for the review return.
