<!--
file: context/audits/2026-06-19_Doc16_DOCS_Review_Return.md
purpose: DOCS second-opinion review of homesynapse-core-docs/design/16-superior-automation.md (DRAFT 32afb3f) against the design-doc template + review-and-quality.md §1. Produces a verdict + an explicit edit list. Review ONLY — edits are NOT folded here (review separate from fold; Nick folds → ratifies → Locks). Doc 16 Lock is the M7.2b prerequisite.
audience: Nick (ratify/fold), the Doc 16 fold session
state-type: review return
status: COMPLETE 2026-06-19 — verdict RATIFY-WITH-EDITS (3 edits, all NON-BLOCKING). No BLOCKING/REVISE findings.
reviewed: docs 32afb3f (working-tree intact-on-host; the VM showed a truncation artifact, quarantined). Source cross-checks at core beb4bc3.
-->

# Doc 16 (Superior Automation Layer) — DOCS Second-Opinion Review Return

**Independence caveat (stated up front):** this review was run by the same Cowork session that, in the M7-forward plan (Part B), judged Doc 16 "review-ready." It is therefore a **rigorous structured critique, not a fully-independent second opinion.** It was conducted adversarially (hunting for defects, not confirming the prior read) and it found three real edits — but for maximum pre-Lock rigor a fresh DOCS-Project conversation remains the stronger path. The edit list below is the substantive output either way.

## Verdict: **RATIFY-WITH-EDITS** (3 edits, all NON-BLOCKING; the Locked decisions hold regardless of how they resolve)

Doc 16 is fundamentally sound and Lock-ready after the edits. It is well-scoped (it explicitly splits federation, cross-cutting reliability, and honest-hybrid into separate docs — the M4-retrospective "epic-under-one-label" failure is avoided), adds **no sealed permit and no event type** (AMD-88..93 preserved — cross-checked against `beb4bc3`), and its §7.2 M7-Contract-Impact Interlock states the required verdict (M7.1 UNAFFECTED / M7.2 SHAPED / M7.3 UNAFFECTED) consistent with the landed M7.1 reality.

## Checklist results (review-and-quality.md §1)

- **Template compliance — PASS.** 17 numbered sections (§0–§16), all substantive; exceeds the 13 mandatory. Metadata header complete; dependencies cite specific sections (Doc 07 §3.4/§3.7/§3.11.2, Doc 01 §4.1, Doc 06 §3.2, Doc 15 §3, etc.); dependents populated (M7.2; the reliability/federation/hybrid docs; REST/WS/Observability/Web UI).
- **Invariant coverage — PASS.** §5.2 cites each relevant INV with a concrete mechanism + section, and §13 gives a verifying test per contract (C-SA-1..7): INV-TO-01/02/03/04, ES-06, RF-01/04/06, LF-01/02, PD-03/07, SE-02, CE-01/02/03, CS-03, PR-01/02/03, MU-01, plus AMD-88/90/91/92/93 invariants. §5.3 introduces 4 candidate invariants ([SA-INV-1..4]) flagged for canonical registration at Lock (see E3).
- **Locked-decision compliance — PASS.** LTD-01/04/08/09/11/15/17 cited and honored; no decision contradicts a Locked doc; the anti-requirements (no DSL, no engine retry, no destructive migration, never-lead-with-commodity-encryption, local-first) are each operationalized (SP1/SP3/§6.1/§12/§3.6) and restated in §16.
- **Precision — PASS.** Behavioral claims are test-backed; performance targets are quantitative with Pi-4 context (§10); config options have types/defaults/ranges (§9); failure modes give trigger/impact/recovery/events (§6).
- **Consistency — PASS with E1/E2.** Scope owns/does-not-own is unambiguous; the diagnostic events §3.3 reads (`automation_run_skipped`, `cascade_loop_detected`, `cascade_depth_exceeded`, `automation_condition_evaluated`, `config_error`) all exist in the landed AMD-92/AMD-93 inventory. Two consistency clarifications needed (E1, E2).
- **Decision quality — PASS.** §16 table: every decision has a principle/constraint-grounded rationale; alternatives are realistic (expressiveness-only rejected as too thin; templating-DSL rejected on the silent-failure corpus); tradeoffs explicit.
- **Open questions — PASS.** §15: 5 OQs, all NON-BLOCKING; Q2 (AX-7 versioning) + Q5 (D2/REC-162) flagged as escalations to Nick (M7.2/user-authoring gates, not Doc-16-Lock gates); "No BLOCKING question remains."

## Edits (fold before Lock)

**E1 — `RunCausalChain` "Existing (AMD-91)" is ratified-but-not-yet-implemented; clarify to avoid a built-vs-ratified misread. [NON-BLOCKING]**
- Where: §4 data-model table (`RunCausalChain | ... | Existing (AMD-91)`) and §8.2 ("Existing types reused unchanged: ... RunCausalChain ...").
- Finding: at `beb4bc3`, `RunCausalChain` is **not yet a Java type** — `RunContext` still carries `int cascadeDepth`; the AMD-91 `RunContext`→`RunCausalChain` swap is **M7.2 (M7.2a) work** (source-verified). "Existing (AMD-91)" is defensible as a *ratified-contract* reference, but a reader can misread it as *built*. Because the explainability/audit surfaces (§3.3) **read** `RunCausalChain`, those surfaces inherently sequence **after** M7.2 builds it.
- Edit: in §4 and §8.2, change "Existing (AMD-91)" → "Ratified (AMD-91); implemented at M7.2a (the `RunContext`→`RunCausalChain` swap). The explainability/audit surfaces that read it build with/after M7.2." (No design change; a one-line currency clarification that also tightens the §7.2 dependency story.)

**E2 — the audit projection's tamper-evidence is inert until `chain_hash` is live; state the dependency so the enterprise-audit claim is honest pre-chain. [NON-BLOCKING]**
- Where: §3.3 ("the same assembly rendered as an append-only, **tamper-evident** audit record by binding each explanation to the Doc 15 `chain_hash`") and §12 ("Tamper-evident audit (Doc 15)").
- Finding: per app-bootstrap A3 / Track-3 F4 (and Doc 16's own §6.3), `chain_hash` is **32-byte ZERO for every event today** and the chain-validity / startup-verify machinery is **gated on chain activation** (post-MVP, ships with crypto-shred). So the audit projection's core value — tamper-evidence — is **inert until chain activation**. §3.3 introduces it without that caveat, slightly over-stating the pre-chain enterprise-audit claim.
- Edit: in §3.3 (and a clause in §12), add a sentence cross-referencing §6.3 / A3-F4: the audit tamper-evidence binding is **gated on `chain_hash` + mandatory startup-verification being live** (all-zero today); until then the audit projection assembles the record but its tamper-evidence is not yet in force. (Consistency with the A3/F4 chain-liveness reality; `audit.enabled` already defaults off per SP6, so no behavior change — this is honesty about the claim.)

**E3 — register the candidate invariants at Lock (ratification mechanics, not a doc defect). [process note]**
- §5.3's `[SA-INV-1..4]` are provisional statements + mechanisms; per INV-GA-02 the canonical `INV-XX-NN` / `AMD-NN-INV` identifiers are assigned **at ratification**. Confirm the fold session mints them in the invariant index (Architecture_Invariants §17 + the traceability matrix) in the same commit as the Lock, and bumps the watermark per the amendment pipeline. (This is the §15-escalation to Nick; flagged so it is not lost at Lock.)

## Cross-checks performed
- §7.2 verdict vs landed source (`beb4bc3`): no sealed permit added to `TriggerDefinition`(12)/`Selector`(7); no event type added to the AMD-92 inventory (`CORE_PRODUCTION_EVENT_CLASSES`=32); the `ConditionEvaluator.evaluate(ConditionDefinition, StateSnapshot)` contract the doc says it leaves unchanged is the one M7.1 implemented. Consistent — M7.1 ride-along verdict holds.
- Anti-requirement "no engine retry": §3.4/SP3/§16 hold it; D2/REC-162 is explicitly **deferred** to the M7.2b action-model decision (§14, §15-Q5), not pre-empted — consistent with the 2026-06-19 R2 ruling (keep REC-162 anti-retry; decide at M7.2b).
- No BLOCKING/REVISE trigger (review-and-quality §5): the doc does not misunderstand the subsystem, violate an unpatchable invariant, introduce a dependency-direction violation, or silently change a Locked contract.

## Next (Nick)
Fold E1 + E2 (one-line clarifications) + apply E3's registration at Lock → ratify → Lock Doc 16. Lock clears the M7.2b entry-gate (the action-model freeze). This review is **not** folded here (review-separate-from-fold discipline); it is the input to the fold step.
