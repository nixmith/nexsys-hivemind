<!--
file: context/instructions/2026-06-15_C3_cascade-governance-doc-fix_coding-instruction.md
purpose: C3 fix-first doc-only correction — retire the superseded AMD-04 cascade-governance model in RunContext.java Javadoc + core/automation/MODULE_CONTEXT.md, citing AMD-91 (RunCausalChain + cycle detection) and flagging the field-swap reshape as M7.2. DOC/JAVADOC ONLY — zero behavioral or interface change. Must precede the M7.2 instruction so the implementer does not build the depth-only model.
audience: Coder (nexsys-coder), Nick (issue gate), PM
phase: 3-Implementation (doc-currency correction)
status: ⛔ ISSUE-GATED — authored 2026-06-15. Issues when the W25 Lane-4 P6 floor lifts (Nick APPROVEs M5-C Increment 1 = entry-gate row 4). Independent of row 3 (interviews): C3 can land DURING interview week, ahead of M7.1.
baseline: homesynapse-core HEAD 1eddd9a; docs watermark AMD-93; AMD-91 RATIFIED 2026-06-12; AMD-04 SUPERSEDED-by-AMD-91. RE-VERIFY the STOP-gates at issue.
amd-refs: AMD-91 (F4 — RunCausalChain supersedes AMD-04, RATIFIED). The implementing field-swap is M7.2 (AMD-91 §8) — OUT of scope here.
-->

# Coding Task: C3 — Cascade-Governance Doc-Currency Fix (AMD-04 → AMD-91)

**Subsystem:** Automation Engine (`com.homesynapse.automation`) — documentation only
**Design Doc:** AMD-91 (RATIFIED 2026-06-12); supersedes AMD-04. Doc 07 §3.7.1 / §8.2.
**Phase:** 3-Implementation (doc-currency correction; no production behavior changes)
**Source:** converge synthesis `context/audits/2026-06-15_core-review_CONVERGE_synthesis.md` finding **C3 (=B-M2)**, ranked FIX-FIRST before M7.2.

---

## ⛔ Issue Gate (read first)

AUTHORED, not issued. Issues only when **entry-gate row 4** is GREEN — Nick APPROVEs `homesynapse-core-docs/website/pages/config-superiority.md`, lifting the W25 Lane-4 "no new Core coding instruction" P6 floor. **C3 does NOT depend on row 3 (energy/erasure interviews)** — it has no evidence dependency, so it can land during interview week, ahead of M7.1. It MUST land before the M7.2 instruction is drafted.

At issue: re-confirm the STOP-on-Mismatch Gates at the then-current HEAD.

## What This Fixes (and what it deliberately does NOT)

The cascade-governance documentation still describes the **superseded AMD-04** model: a bare `cascadeDepth: int` with `automation.max_cascade_depth` (default 8, range 1–32) and only the `cascade_depth_exceeded` diagnostic. **AMD-91 superseded AMD-04** (RATIFIED 2026-06-12): the lineage moves to a `RunCausalChain` (a list of `(RunId, AutomationId)` `ChainLink`s; `depth()` derived), and cycle detection becomes **chain-membership** (`containsAutomation`) emitting a **distinct** `cascade_loop_detected` diagnostic — deterministic, replacing the old windowed/evictable `(correlation_id, automation_id)` suppression set. A Coder building M7.2 cascade governance from the contract/MODULE_CONTEXT (not the charter) would build the depth-only model and **miss cycle detection** — that is the drift C3 closes.

**This WU is DOC/JAVADOC ONLY. It does NOT change the `RunContext` record.** The `cascadeDepth (int)` field stays exactly as-is — the breaking field-swap to `causalChain (RunCausalChain)` is **AMD-91 §2.2, scheduled for M7.2** (AMD-91 §8). C3 makes the *documentation* cite the correct (AMD-91) governing model and **forward-flag** the reshape as M7.2 work, so no one builds on the stale model in the meantime.

## Files to Read Before Starting

| File | Why |
|---|---|
| `homesynapse-core-docs/design/amendments/AMD-91_RunCausalChain_Supersedes_AMD-04.md` | The governing model: §2.1 (`RunCausalChain`), §2.3 (governance mechanics — depth UNCHANGED, cycle detection UPGRADED), §2.4 (the AMD-04 supersession ledger), §8 (implementing WU = M7.2) |
| `core/automation/src/main/java/com/homesynapse/automation/RunContext.java` | The Javadoc target (the `<h2>Cascade Governance</h2>` block) |
| `core/automation/MODULE_CONTEXT.md` | The two drift lines (cascade gotcha + the AMD-04 "Issue 10.1" resolution line) |
| `context/audits/2026-06-15_core-review_CONVERGE_synthesis.md` (C3 row) | The finding + disposition |

## STOP-on-Mismatch Gates

Confirm BEFORE editing. If any has diverged, STOP and report (e.g., if the M7.2 field-swap already landed, this doc-fix is moot — report it).

| File | Expected state at issue | If diverged |
|---|---|---|
| `RunContext.java` | record with **`int cascadeDepth` at field position 7** (the AMD-91 swap has NOT happened); the `<h2>Cascade Governance</h2>` Javadoc cites `automation.max_cascade_depth` (default 8, range 1–32) + `cascade_depth_exceeded` only — no AMD-91 / `RunCausalChain` / cycle-detection mention | If the field is already `causalChain`, M7.2 ran first — STOP, this WU is moot |
| `core/automation/MODULE_CONTEXT.md` | the cascade gotcha line ("RunContext.cascadeDepth is 0 … Maximum governed by `automation.max_cascade_depth` … default 8, range 1–32") and the Constraints "Issue 10.1 (cascade loops) → AMD-04: cascade depth max 8, duplicate suppression, natural termination" line both still cite **AMD-04** with no AMD-91 supersession note | If AMD-91 already cited there, confirm whether C3 was partially applied; reconcile, don't duplicate |

## Files to Modify

| Action | Path | Change |
|---|---|---|
| MODIFY (Javadoc only) | `core/automation/src/main/java/com/homesynapse/automation/RunContext.java` | The `<h2>Cascade Governance</h2>` block + the `@param cascadeDepth` line |
| MODIFY | `core/automation/MODULE_CONTEXT.md` | The cascade gotcha line + the Constraints "Issue 10.1 → AMD-04" line (+ the Amendments-in-force / currency section if the file has one) |

No other files. No `.java` outside `RunContext.java`'s Javadoc. No `module-info`, no `build.gradle.kts`, no test, no `projectionVersion`.

## The Edits (authoritative content; exact wording is the Coder's call within these constraints)

### 1. `RunContext.java` — the `<h2>Cascade Governance</h2>` Javadoc block

Keep the field and its current behavior described accurately for the **present** record shape (`cascadeDepth` int, root 0, child `parent.cascadeDepth + 1`, `automation.max_cascade_depth` default 8 range 1–32, `cascade_depth_exceeded` DIAGNOSTIC) — all of that is still true of the code as it stands. **Add** a forward-governance note that:

- the **governing cascade model is AMD-91** (`RunCausalChain`), which **supersedes AMD-04**;
- AMD-91 keeps depth-limiting semantics **unchanged** (same config key, same default/range, same `cascade_depth_exceeded`) but **upgrades cycle detection** to deterministic **chain-membership** with a **distinct `cascade_loop_detected`** diagnostic (replacing the windowed `(correlation_id, automation_id)` suppression set);
- the **field reshape itself — `cascadeDepth (int)` → `causalChain (RunCausalChain)` — is M7.2 work** (AMD-91 §2.2/§8) and is intentionally **not yet applied** to this record.

**CRITICAL — do NOT use `{@link}` for `RunCausalChain`.** That type does not exist until M7.2; a `{@link com.homesynapse.automation.RunCausalChain}` would fail `-Xdoclint`/`javadoc` (and break the build gate). Reference it as **`{@code RunCausalChain}`** or plain prose only. Likewise reference `cascade_loop_detected` as `{@code cascade_loop_detected}` (an event name, not a Java element).

Update the `@param cascadeDepth` line to note it is the AMD-04-era field retained until the AMD-91/M7.2 reshape (one clause; keep it a valid `@param`).

### 2. `core/automation/MODULE_CONTEXT.md`

- **Cascade gotcha line** (the "RunContext.cascadeDepth is 0 for user/device-initiated Runs … Maximum governed by `automation.max_cascade_depth` …"): append an AMD-91 supersession note — chain-membership cycle detection + `cascade_loop_detected`, deterministic (no window/eviction); field-swap to `causalChain: RunCausalChain` is M7.2.
- **Constraints "Issue 10.1 (cascade loops) → AMD-04 …" line:** mark **AMD-04 SUPERSEDED by AMD-91**; cycle suppression is now chain-membership (deterministic), depth-limiting unchanged. Keep the historical AMD-04 reference legible (it explains the lineage) but make AMD-91 the governing citation.
- If the file carries an "Amendments in force" / currency list, add **AMD-91 (RunCausalChain, supersedes AMD-04; field-swap M7.2)**.

Keep edits surgical and consistent with the file's existing voice. Do not restructure sections.

## Invariants / Discipline That Apply

- **No behavioral change.** The record's fields, constructor, and validation are byte-identical after this WU. Diff must show only Javadoc/comment/MODULE_CONTEXT lines.
- **AMD-91-INV-01 (the reason this matters):** cascade-cycle suppression is a deterministic function of the Run's causal chain + config alone — *no windowed/evictable/restart-sensitive state*. The doc must not keep describing the old windowed suppression set as the governing mechanism.
- **§4c Clock note:** N/A — no test or production logic touched. (Stated so the Coder confirms it considered it.)

## What to Watch Out For

- **`{@link RunCausalChain}` will break the build** — the type is M7.2-future. Use `{@code …}`/prose. This is the single most likely defect in this WU.
- **Do not "helpfully" start the field swap.** The temptation is to change `int cascadeDepth` → `RunCausalChain causalChain`. That is M7.2 (AMD-91 §2.2/§8) and OUT of scope; doing it here would require `RunCausalChain` + governor changes + a `RunContext` construction-site sweep and would break the doc-only success criterion. STOP and report if you think the swap belongs here.
- **Keep the present-tense description accurate.** The record today *does* carry `cascadeDepth: int`; describe it truthfully as the current shape, with AMD-91 as the governing/forward model and the swap flagged M7.2 — not as if the swap already happened.
- **`cascade_rate_exceeded` was NOT adopted** (AMD-91 §2.4 ledger / §6) — do not introduce it.

## Build Discipline

You produce the file edits; you do NOT run `./gradlew`. Nick runs the gate after review. Flag the deferred gate in `coder-handoff.md` + the WUCP Phase 1 checklist. The gate that matters here is **`-Xdoclint`/`javadoc` + spotless on `:core:automation`** (the Javadoc edit recompiles); if your sandbox can run it, `./gradlew :core:automation:compileJava :core:automation:spotlessCheck` catches a bad `{@link}` in seconds. Full `check` stays the deferred gate.

## Success Criterion (binary)

DONE when: (1) `RunContext.java`'s Cascade Governance Javadoc cites AMD-91 (supersedes AMD-04), keeps depth-limiting described as unchanged, names chain-membership cycle detection + `{@code cascade_loop_detected}`, and flags the field-swap as M7.2 — **with no `{@link}` to the not-yet-existing `RunCausalChain`**; (2) the record's fields/constructor/validation are unchanged (diff is Javadoc/comment only); (3) `MODULE_CONTEXT.md`'s two cascade lines cite AMD-91 supersession; (4) build gate GREEN (deferred to Nick); (5) WUCP Phase 1 checklist complete with next-WU pointer.

## Out of Scope (do NOT do)

- The `RunContext` field swap `cascadeDepth → causalChain` and the `RunCausalChain`/`ChainLink` record (AMD-91 §2.2/§2.1) — **M7.2**.
- Any `RunManager`/governor logic, `CascadeDepthGovernorTest`/`CycleDetectionTest` (AMD-91 §5) — **M7.2**.
- Doc 07 §3.7.1 / Doc 01 §4.5 prose edits in the docs repo — already applied at AMD-91 ratification (§9 checklist); not this WU.

## WUCP Phase 1

After the edit: update `coder-handoff.md` (Deferred Build Gate flag = `-Xdoclint`/spotless on `:core:automation`; next-WU pointer); append to `coder-lessons.md` only if the `{@link}`-to-future-type trap bites; append the WUCP Phase 1 checklist to the Completion Report. The MODULE_CONTEXT.md update IS part of this WU's deliverable (not a separate step).

---

### PM note (for Nick, not the Coder)
C3 is small enough that you may alternatively apply it as a **direct host edit** rather than dispatching the Coder — the same `-Xdoclint`/spotless build-gate caveat applies (the `{@link RunCausalChain}` trap is the one thing to avoid). Either way it must land before the M7.2 instruction is drafted. Recommended sequence once you APPROVE M5-C: **C3 lands first** (it's the cheapest row-4-unblocked item and clears the M7.2 fix-first), then M7.1 issues once row 3 also closes.
