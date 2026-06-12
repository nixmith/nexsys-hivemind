<!--
file: context/assessments/2026-06-12_Research_14A_PM_Assessment.md
purpose: PM assessment of Research 14-A (Automation Authoring & Operating UX — Failure Modes, REC-141..155) — 6-step A–F, source-verified against Doc 07 actual text (researcher connector-blind, declared). FOLDED SECOND (after R14-B) per the serialized order.
audience: PM, Nick
state-type: assessment
status: COMPLETE 2026-06-12 — grade A−; 13 ACCEPT (5 narrowed, 2 re-bucketed to ALREADY-COVERED, 1 split) + 1 POST-MVP + 1 REJECT; zero discards; the ledger-gap dossier is M5-C-ready
anchors: context/instructions/Research_14A_Automation_UX_Failure_Modes_Brief.md; context/assessments/2026-06-12_Research_14B_PM_Assessment.md (folded first); context/assessments/2026-06-12_W0_Research_4_Currency_Delta.md
-->

# Research 14-A — PM Assessment (community/UX register; folded SECOND)

**Return:** "Research 14-A: Automation Authoring & Operating UX — Failure Modes" (2026-06-12). **RECs:** 141–155 (15 — full range, none exceeded). **Venue note:** same connector-blind condition as R14-B, declared in §5; the researcher worked from embeds and flagged exactly the right escalation ("request those fields from the connector — I did not reconstruct them"). **PM verification read Doc 07 §4.2 (run-trace model), §4.3, §5 C1/C2, and the §3.6/§3.7/§3.8 trace-event passages (:270, :313, :326, :379) before ruling.**

## Step 0 — Quote-back gate: **HONORED**
(a) module-info content-identical (one collapsed blank line — whitespace nit, noted, not a violation) (b) inventory line verbatim (c) all five decided-ground rows verbatim. Admitted past §0.

## Steps A–C — Format / Summary / Cross-cutting: **PASS, STRONG**
All sections present; §7 LIGHT; all six buckets populated, no double-bucket; sources graded by reliability in §5 (aggregator sites flagged — good hygiene). The §3.3 **ledger-gap dossier is the deliverable of the cycle**: maintainer-statement evidence (frenck 2022: retry/verification "out of scope for HA… a level UP"), installed-workaround Mom-Test signals (AppDaemon verify-resend, `amitfin/retry` with `expected_state`, watchdog automations), and the protocol-ack red-herring analysis — category-of-one claim, INV-CE-01 calibration grade. §3.4 honesty produced a real REJECT (templating DSL).

## Step D — REC dispositions (PM rulings; source-verified)

**Verification headline: the Locked design is ahead of the return's gap framing in three places** — the connector-blind embeds didn't carry §4.2's field table or the §3.6/§3.8 trace-event specifications. (1) **All four "why didn't it fire?" details are ALREADY SPECIFIED:** `matched_triggers` + `resolved_targets` in the §4.2 trace record; per-condition `automation_condition_evaluated` DIAGNOSTIC ("condition type, evaluated state values, boolean result", :379); drop/cancel observability via `automation_run_skipped`/`automation_run_cancelled` DIAGNOSTIC events (:270). (2) **Traces are log events assembled by `correlation_id` (§4.2) — there is NO ring buffer to fix**; the HA-class eviction problem is structurally absent. The genuine residual is the **7-day DIAGNOSTIC retention window** (:326) interacting with failed-run forensics. (3) **`MaxExceededSeverity` already defaults INFO** (frozen Javadoc) — "never default SILENT" is already satisfied. None of this voids the RECs — it converts "wire it" claims into test-pin obligations and narrows the genuinely-new content.

| REC | Researcher bucket | PM ruling | PM modification |
|---|---|---|---|
| 141 four trace details | M7-OBLIGATION | **ACCEPT (narrowed to test-pinning)** | All four details are Locked design content (§4.2 + :270 + :379); the obligation is the M7.x instruction TEST-pinning each (trace assembly per C1, incl. the drop-reason DIAGNOSTICs) — no new design content |
| 142 ledger = differentiator | ALREADY-COVERED | **ACCEPT** | §3.3 dossier routed to M5-C (the cycle's flagship superiority material, INV-CE-01 grade) |
| 143 timeout defaults + status surfacing | M7-OBLIGATION | **ACCEPT (merged)** | Merges with R14-B REC-161 + Research-4 REC-33 into ONE AMD item: `ConfirmationPolicy` + default `confirmation_timeout_ms` (+ Pi-4 calibration spike). Status surfacing is largely §4.2's `commands` assembly — test-pin it |
| 144 ConfirmationPolicy default | M7-OBLIGATION | **ACCEPT (merged)** | Same AMD item as 143/161/33; the frenck double-actuation quote is the rationale text for the opt-in default |
| 145 failed-run trace retention | M7-OBLIGATION | **ACCEPT (re-framed + narrowed)** | No ring buffer exists (§4.2 — structural attestation for M5-C); residual = the 7-day DIAGNOSTIC window (:326) vs failed-run forensics — M7 instruction note + test (failed-run trace assembles fully in-window); retention-exception design, if evidence demands it, = FUTURE |
| 146 actorRef provenance | ALREADY-COVERED | **ACCEPT** | Hubitat evidence ("what turned on my light?" = top complaint) handed to Nick as C8 ratification support (entry-gate row 2) |
| 147 drop observability + defaults | M7-OBLIGATION | **RE-BUCKET → ALREADY-COVERED (test-pin carried)** | `automation_run_skipped`/`automation_run_cancelled` DIAGNOSTICs are specified (:270); default INFO is frozen; carry = instruction test-pins both events + an explicit never-default-SILENT attestation line |
| 148 edge/level affordance + validation | M7-OBLIGATION | **ACCEPT (narrowed + split lanes)** | M7 = schema descriptions + a load-time WARNING-class misuse heuristic (within §3.3/§6.1 validation); authoring affordances/UI = POST-MVP lane (noted, not bucketed — single bucket holds) |
| 149 validation surfacing | ALREADY-COVERED | **ACCEPT** | §6.1 + AMD-71 fail-closed; instruction nicety: user-legible error text |
| 150 definition schema versioning posture | M7-OBLIGATION | **ACCEPT (lightened)** | Doc 07 §4.1 already registers `automations.yaml` as a Doc 06 §7 secondary config doc (:584) → the AMD block states the `(major,minor)` posture + forward-only guarantee explicitly; mostly attestation + one schema_version statement |
| 151 forced-migration anti-requirement | ALREADY-COVERED | **ACCEPT** | AMD-67 + §3.3; recorded as anti-requirement with the Groovy/RM evidence |
| 152 confirmation-driven remediation | M8-OBLIGATION | **ACCEPT** | Maps 1:1 to charter row M8.2; the `amitfin/retry` `expected_state` pattern is the evidence the row needed |
| 153 reference integrity | FUTURE-AMD | **SPLIT** | **153a (M7-OBLIGATION):** dangling-reference load-time validation within §6.1 — co-anchored with the queued REC-136 FUTURE-AMD family (Research 13; reference-integrity lives at composition-root/automation), which M7 partially discharges for automation-internal refs. **153b (FUTURE-AMD):** stable entity-reference indirection — the contract delta, parked un-drafted |
| 154 authoring UX (blank-page/spaghetti) | POST-MVP | **ACCEPT** | M10/M11/Doc 13 lane |
| 155 no templating DSL | REJECT | **ACCEPT** | The strongest anti-requirement of the cycle: HA's largest authoring failure class is the thing the sealed-permit design forecloses — also M5-C material (a structural-absence claim, the INV-CE-01 shape) |

**Summary: 15 RECs → 9 obligations (141/143+144 merged/145/148/150/153a M7 · 152 M8) + 5 ALREADY-COVERED (142/146/147/149/151) + 1 FUTURE-AMD (153b) + 1 POST-MVP (154) + 1 REJECT (155). Zero discards; zero guardrail violations.** (147 re-bucketed; 153 split; counts overlap by the split.)

## Step E — Error inventory / fabrication check
Zero fabricated HomeSynapse identifiers. Quote-back whitespace nit (module-info blank line) — noted only. Two substantive gap-overclaims (REC-141 "must wire", REC-147 "needs a drop DIAGNOSTIC") — both artifacts of the connector-blind condition, both framed conditionally by the researcher, both corrected at PM verification without disposition damage. Evidence hygiene is exemplary: sources dated, aggregator-grade material flagged and quarantined, the HA 2026.6 release-blog claim primary-verified by the researcher itself.

## Step F — Grade and process notes

**Grade: A−.** The ledger-gap dossier and the Mom-Test discipline (installed hacks > requests) are the best evidence work of the research program to date; the debuggability matrix directly populates the charter. Docked: the three Locked-text corrections above (root cause: connector-blind run; same as R14-B) and the REC-153 single-bucket forcing that would have dropped the M7 validation half without PM splitting.

**Process notes:** (1) Second consecutive connector-blind return — **escalation to Nick:** if the DOCS-Project connector remains unreachable for research runs, future briefs must embed the §4.2-class contract tables at quote granularity (cost: bigger briefs), or the venue needs fixing. (2) The §0 quote-back + embed discipline again held the fabrication rate at zero across both blind runs — the pattern is validated. (3) REC-141's four details + REC-147's two DIAGNOSTIC events enter the M7 event-vocabulary inventory: `automation_triggered` (with `matched_triggers`/`resolved_targets`/`definition_hash`), `automation_condition_evaluated`, `automation_action_started/completed`, `automation_completed`, `automation_run_skipped`, `automation_run_cancelled` are all Doc-07-specified — the REC-39 manifest fan-out must count them (W0 §2.5 obligation 2).

**Feeds:** M5-C (the §3.3 dossier + the REC-145 no-ring-buffer attestation + the REC-155 structural-absence claim — three website-grade items); the M7 AMD block (143+144+161+33 merged item; 150 posture statement; 153a validation; 158-adjacent diagnostics); M7.x instruction tests (141/145/147 pins); M8.2 (152); C8 ratification support (146); FUTURE-AMD queue (153b joins REC-136 family); anti-requirements (151, 155, + R14-B's 162).
