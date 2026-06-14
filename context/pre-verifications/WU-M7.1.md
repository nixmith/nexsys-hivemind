<!--
file: context/pre-verifications/WU-M7.1.md
purpose: Pre-verification artifact for the M7.1 (trigger/condition path) coding instruction. Each source-state assumption the instruction depends on, with its observed signature (or absent→must-create) and a verification timestamp. The Coder reads this FIRST and re-confirms at issue (pre-empts the source-vs-brief mismatch class, M3.6d). Authored at the converge; the instruction it backs is ISSUE-GATED on entry-gate rows 3+4.
audience: Coder (read first), PM, Nick
state-type: pre-verification
status: AUTHORED 2026-06-15 (converge) — RE-VERIFY AT ISSUE (baseline may advance)
baseline: homesynapse-core M6.3-landed tree (framework baseline 1eddd9a; substantive HEAD per PROJECT_SNAPSHOT). Host Read/Grep only — Cowork cannot run Gradle; sandbox git quarantined.
-->

# Pre-Verification — WU-M7.1 (trigger/condition path)

Every source-state assumption the M7.1 instruction rests on, verified against actual `.java` source this session (host Read/Grep). **The headline finding de-risks the block: the AMD-88/AMD-89 breaking-constructor changes have ZERO existing construction sites — the sweep set is empty.** Re-run each check at issue; if any has diverged, STOP and report before coding.

## A. The construction-site sweep set is EMPTY (the load-bearing finding)

**Assumption (from AMD-88 §2.5 / AMD-89 §2.2):** the `triggerId` additions (5 trigger permits) and `includedRoles` additions (3 selector permits) are BREAKING canonical-constructor changes requiring a construction-site sweep of "Phase-2 tests and fixtures."

**Observed (2026-06-15):**
- `grep -E "new (StateChangeTrigger|StateTrigger|EventTrigger|AvailabilityTrigger|NumericThresholdTrigger|AreaSelector|LabelSelector|TypeSelector)\("` across the entire `homesynapse-core` tree → **0 matches.**
- Broad reference grep for those permit names → **9 files, all `core/automation/src/main/java/...` type definitions** (the permit records + `Selector`/`TriggerDefinition` roots + `SelectorResolver`). No test, no fixture, no `app`/IT reference.
- Consistent with the review finding that `core/automation` is **Phase-2 interface-only: 53 types + package-info, 0 tests, 0 implementation.**

**Implication:** the breaking ctor changes have **zero blast radius at baseline.** The M7.1 evaluator + the M7.1 tests will be the **first** constructors of these permits, written against the post-AMD shapes from the start. The "construction-site sweep" required by the AMD-88 §9 and AMD-89 §9 ratification checklists resolves, at this baseline, to **"there are no existing sites; the P2 survey records the empty set and the new M7.1 tests construct the post-AMD shapes."** This refines the Session-B characterization ("M7.1's first construction step + a construction-site sweep") — there is nothing to retrofit. **Re-verify at issue:** if any automation test/fixture has landed between now and issue, the sweep set is no longer empty — re-run the grep.

## B. Source-state assumptions table

| # | Assumed element | Observed signature (2026-06-15) | M7.1 action |
|---|---|---|---|
| B1 | `core/automation/src/main/java/module-info.java` | `requires transitive` platform/event/device/state; `requires com.homesynapse.value`; `exports com.homesynapse.automation`. **No `requires config`, no `requires event.bus`** (FIX-07 removed config pre-Phase-3). Verbatim in the instruction §"Technical Spec". | **MODIFY** — re-add `requires com.homesynapse.config` + `requires com.homesynapse.event.bus` (FIX-07 reversal) when the registry/loader + the 3 subscribers import those types. Gradle `api`/`implementation` lockstep per the §authoring check. |
| B2 | `TriggerDefinition` sealed root | 9 permits: 5 Tier-1 non-empty (`StateChangeTrigger` 5 fields, `StateTrigger` 4, `EventTrigger` 2, `AvailabilityTrigger` 3, `NumericThresholdTrigger` 5) + 4 Tier-2 empty (`TimeTrigger`/`SunTrigger`/`PresenceTrigger`/`WebhookTrigger`). | **MODIFY** per AMD-88 → 12 permits: +`CalendarTrigger`/`ReachabilityTrigger`/`ManualTrigger` (new, +3 switch cases); `WebhookTrigger` promote (fields, 0 cases); `PresenceTrigger` stays empty (M8.1); `triggerId` String on all 5 existing Tier-1 permits + the 3 new + Webhook. |
| B3 | `Selector` sealed root | 6 permits: `DirectRefSelector`/`SlugSelector`/`AreaSelector`/`LabelSelector`/`TypeSelector`/`CompoundSelector`. | **MODIFY** per AMD-89 → 7 permits: +`SemanticTagSelector` (new, +1 case); `includedRoles` `Set<EntityRole>` on `AreaSelector`/`LabelSelector`/`TypeSelector`. New enum `MatchMode { EXACT, NAMESPACE_PREFIX }`. |
| B4 | New automation-resident enums | `CalendarEventTransition`, `MatchMode` — **absent** (grep clean). | **CREATE** both (UPPER_SNAKE values, no wire-format methods — they never enter payloads, AMD-92 residency). |
| B5 | Service interfaces (M7.1 targets) | `AutomationRegistry`, `TriggerEvaluator`, `ConditionEvaluator`, `SelectorResolver` — **interface-only, 0 implementations** (verified: automation has 0 impl). Signatures per MODULE_CONTEXT §8.1. | **CREATE** production impls. (`ActionExecutor`/`RunManager`/`CommandDispatchService`/`PendingCommandLedger`/`ConflictDetector` are M7.2/M7.3 — out of scope.) |
| B6 | `RunContext` record | 8 fields incl. `cascadeDepth (int)` at position 7. | **DO NOT TOUCH** — the `cascadeDepth → causalChain: RunCausalChain` swap is AMD-91, implementing WU **M7.2** (AMD-91 §8). M7.1 does not construct `RunContext`. |
| B7 | Event records (event-model) | `AutomationTriggeredEvent(String triggerType, String triggerDetail)` + `AutomationCompletedEvent(String status, String failureReason, long durationMs)` — minimal M1-era shapes. | **RESHAPE `AutomationTriggeredEvent` only** per AMD-92 row 1 (run-initiation slice). `AutomationCompletedEvent` reshape is AMD-92 row 2 = **M7.2** — do not touch. |
| B8 | M7.1 event slice (AMD-92 §2.3/§8) | Rows 1, 3, 11–16, 19 = reshape `automation_triggered` (1) + mint `automation_invoked` (3), `automation_slug_redirect` (11), `trigger_duration_started/cancelled/expired/state_validated/limit_exceeded` (12–16), `automation_capability_mismatch` record (19, constant exists). | **CREATE** 8 records + 7 constants (row 19 reuses the existing constant); reshape row 1's record. Exact counts fixed by the P2 survey at issue. |
| B9 | Manifest/pin baseline (AMD-92 baseline) | `EventTypes` 55 constants; `CORE_PRODUCTION_EVENT_CLASSES`/`EXPECTED_EVENT_RECORDS` 24; `EventCategoryMapping.TABLE` 36 rows; `EventTypeAnnotationTest` count pin; `EventTypeRegistry`/`JacksonWarmup`. | **MODIFY** — the M7.1 slice fan-out (subset of the block's 55→71 / 24→41 / 36→53). The P2 survey fixes exact M7.1-slice numbers at issue. |
| B10 | C1-interim pin (AMD-92 §10 A.9) | **Zero production publish sites** for `automation_triggered`/`automation_completed` (re-verified this session: only the record defs, the `EventTypes` roster, tests, docs). | **PRESERVE** — M7.1 must NOT introduce a production `automation_triggered` publish site (no completing side exists until M7.2). The reshape + registration land; the production publish is gated to M7.2. The `trigger_duration_*` / `slug_redirect` / `capability_mismatch` diagnostics have no pairing constraint and may publish. |
| B11 | `HomeSynapseCore.start()` | 16-step bootstrap; `module-info` does NOT `requires com.homesynapse.automation`; no automation steps; step-1 event-manifest aggregation is `Stream`-aggregated (no count pins). | **MODIFY** (composition root) — add the automation registry + the 3 subscribers (`automation_engine`, `command_dispatch_service`, `pending_command_ledger`), fold the automation event manifest into step-1 aggregation (AMD-92-INV-02 forcing point), order automation subscribe AFTER state-store catch-up. **This is the converge's flagged latent-defect surface — pin with a lifecycle wiring test.** |
| B12 | AMD-93 schema substrate | `automations.yaml` `(major,minor)` `schema_version` + forward-only idempotent migration; dangling-reference load validation (§6.1); rides the AMD-67 config substrate (M6.1/6.2/6.4 shipped). | Definition loading via the config pipeline honors the AMD-93 schema posture + §6.1 validation (empty `includedRoles` = per-definition load FAILURE, AMD-89 §4 / E89-1). |

## C. Re-verify-at-issue checklist (the Coder runs these before coding)

1. Re-run the §A sweep grep — confirm the construction-site set is still empty (or enumerate any new sites).
2. Read the verbatim `module-info.java` (B1) — confirm it still lacks `requires config`/`event.bus`.
3. Read `TriggerDefinition` (B2) + `Selector` (B3) permits clauses — confirm 9 / 6 at issue.
4. Read `AutomationTriggeredEvent`/`AutomationCompletedEvent` (B7) — confirm minimal shapes (the reshape is regret-proof only while zero producers exist; if a production publish landed, STOP — schema-versioning, not reshape).
5. Read the AMD-88/89/92/93 §9 ratification checklists — confirm the "M7.1 P2 survey enumerates the sweep set" rows are still open (this WU closes them).
6. Read `HomeSynapseCore.start()` (B11) — confirm 16 steps, no automation wiring.

*Pre-empts the source-vs-brief mismatch class (M3.6d). The instruction's STOP-on-Mismatch Gates re-state B1/B2/B3/B7/B11 as in-line gates.*
