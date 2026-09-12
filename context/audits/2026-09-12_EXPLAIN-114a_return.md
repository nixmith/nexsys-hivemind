<!--
file: context/audits/2026-09-12_EXPLAIN-114a_return.md
purpose: Coder return for EXPLAIN-114a — the read-API v1.1.4 additive keys. §0 first; the hub audits; Nick commits.
status: DELIVERED — REPO-COMPLETE, hub audit pending
-->

# EXPLAIN-114a return — v1.1.4 additive keys (filed 2026-09-12 CT)

## §0 The card
- **Verdict: DELIVERED.** Baseline `72efb42` clean at boot. `date -u` 2026-09-12T21:35:54Z ⇒ CT = UTC−5 = 16:35 CDT, once; filed 2026-09-12 CT. Instrument: 24-core Windows 11 desk, warm daemon, `--offline`; not the runner.
- **Census (lock-free porcelain): 13 = 13 M + 0 A + 0 D.** `core/automation/`: `MODULE_CONTEXT.md` · `RunExplanation` · `NonFiringExplanation` · `AutomationSummary` · `StandardExplanationService` · `StandardExplanationServiceTest` · `NonFiringExplanationServiceTest`; `api/rest-api/`: `MODULE_CONTEXT.md` · `GetRunCausalChainEndpoint` · `GetNonFiringEndpoint` · `ListAutomationsEndpoint` · `RunEndpointsTest` · `AutomationEndpointsTest` (`.java`, `src/{main,test}`). Code diff +891/−104. Nothing staged or committed; `module-info` ×2, build files, `web-ui/**`, every payload, `ListRunsEndpoint`, the FIX-2b-ii lines untouched.
- **P1 — 12 table rows + 1 untabled = 13 M, declared:** row 7 `ListRunsEndpoint` OUT (DP-5: `automation_completed` carries no hash); row 6's carrier is the untabled `AutomationSummary.java` (5→6, `definitionKey` LAST) — rest-api holds no definition and `DefinitionHashes` is package-private.
- **P2 —** every new key red at HEAD by construction; `firingValue` red on a VALUE (T1 `expected: "active" but was: null`, run 2). **P3 —** green in one round: run 3 22:04Z on the exact allow-listed line, run 4 22:06Z fresh. **P4 —** moved cites, corrected: ArchRules `:265→:266`, `:305→:306`; `AutomationDisabledEvent :43–:49` (six components); `StateReportedEvent :30–:36` (five); the hash stamp `StandardRunManager:649 → :261/:457`, the publish `:690`.
- **DP-5:** `definitionKey` served where the hash is in hand — the non-firing read and the automations list via `DefinitionHashes.forDefinition(definition)`, the engine's identical function and input (`:261/:457 → RunContext.definitionHash → :690`; T12 pins non-firing key == chain key); the runs list left out. **DP-6:** the literal `"configuration"` — the definition has no reason field (`enabled = optBool(map, "enabled", true)`, `AutomationDefinitionLoader:134`).
- **F3:** a run's `automation_triggered` inherits `correlation_id` from the triggering envelope (`StandardRunManager:218`, the one `correlationId` behind every run class incl. failed-closed `:441`; `RunInitiator:96–:101` hands the bus envelope itself), so the triggering event IS in `readByCorrelation` for every run whose triggering envelope is still retained — the only class outside the chain is a retention-trimmed one; T3 encodes that shape.
- **Red-first:** HEAD 211 · 152 → compile-red 31 + 6 → stage A (seams declared, hooks inert) → behavior-red 14 + 7 → stage B → GREEN 228/228 · 156/156 (3 skip); times in §2. **Deviations:** `[REVIEW]` R1–R4 · `[INFO]` I1–I5 (§3).

## §1 What changed + the red-first table
**core/automation.** `RunExplanation` 8→9 (+`String definitionKey`; an 8-arg convenience ctor); `ActionView` 8→10 (+`Instant settledAt`, `confirmedAt`; no convenience — the 2 + 3 sites gain two args); `NonFiringExplanation` 10→13 (+`disabledAt`, `disabledReason`, `definitionKey`; a 10-arg convenience — the 8/9-arg ones resolve through it); `NonFiringVerdict` +`FIRED_CONFIRMED` LAST; `AutomationSummary` 5→6. `StandardExplanationService`: (a) `buildTrigger` locates the triggering envelope once; `firingValueOf` = `state_changed.newValue` via `AttributeValues.asString` · `state_reported.value` · else null; (b) `deriveOutcome` keeps the classifying ENVELOPES (`instantOf` = eventTime else ingestTime); `buildActions` keeps the `action_completed` envelope so a command-less SKIPPED/FAILED action settles at it; (c) `completedVerdict`'s clean branch → `FIRED_CONFIRMED`, sentence unchanged; (d) `latestDisabled` on the DISABLED branch only, `disabledReason` = its `reason` else `"configuration"`; (e) `definitionKey` threaded into all 8 constructions; the chain serves `definitionHash`, list rows `DefinitionHashes`.
**api/rest-api.** Chain: `settledAt`, `confirmedAt` after `settled` (map 10), `definitionKey` after `cascade` (map 9). Non-firing: `disabledAt`, `disabledReason`, `definitionKey` after `triggerRef` (map 13); `verdict` still `name()`. List: `definitionKey` after `lastRunId` (map 6).

| # | Test (S service · N non-firing · R/A endpoints) | Run 1 | Run 2 stage A | Run 3/4 |
|---|---|---|---|---|
| T1/T1b | state_changed value · numeric dialect `"72"` (S) | set failed | RED value vs null | GREEN |
| T2 | state_reported value (S) | set failed | RED `"21.5"` vs null | GREEN |
| T3/T3b | outside the correlation · non-state payload (S) | set failed | g-b-c (inert seam yields null; teeth in stage B) | GREEN |
| T4/T5/T6 | CONFIRMED · classifying result · timeout + ingest fallback (S) | c-red | RED `+3s`/`+5s`/`+9s` vs null | GREEN |
| T7/T7b | DISPATCHED nulls · SKIPPED settles at completion (S) | c-red | g-b-c / RED `+2s` vs null | GREEN |
| T8 | chain `definitionKey` (S) | c-red | RED `"hash"` vs null | GREEN |
| T9 | BOTH flipped: `nonFiring_cleanConfirmedRun_perDpB2Default` · `completedWithConfirmedCommands_cleanPathUnchanged` (N) | c-red | RED `FIRED_CONFIRMED` vs `NEVER_TRIGGERED` ×2 | GREEN |
| T9b | the enum grows LAST (N) | c-red | g-b-c (stage A's declaration) | GREEN |
| T10/T11/T11b | latest `automation_disabled` · configuration · nulls off DISABLED (N) | c-red | RED `+11s` / `"configuration"` vs null / g-b-c | GREEN |
| T12/T16s | non-firing key == chain key · list rows (N) | c-red | RED sha vs null ×2 | GREEN |
| T13 + `causalChain_v11ShapeTest` (M) | order, ISO or null (R) | c-red ctor ×3 | RED keys absent | GREEN |
| T14/T15 + `nonFiring_v11ShapeTest` (M) | disabled keys · `FIRED_CONFIRMED` by name (A) | c-red ctor | RED keys absent | GREEN |
| T16 + `automations_v11ShapeTest` (M) | row key LAST (A) | c-red ctor | RED keys absent | GREEN |

automation 211 → 228 (+11 S, +6 N); rest-api 152 → 156 (+1 R, +3 A). c-red = compile-red; g-b-c = green-by-construction, disclosed.

## §2 Gates, freshness, sweeps
- **Runs (UTC):** 0 21:50 tests `--rerun` ×2 → 211/211 · 152/152 (3 skip). 1 21:58 `compileTestJava` ×2 → FAILED 31 + 6. 2 22:00 tests ×2 + lifecycle `compileJava` → 228 run/14 fail · 156 run/7 fail. **3 22:04 `./gradlew :core:automation:test --rerun :api:rest-api:test --rerun :lifecycle:lifecycle:compileJava spotlessCheck --offline` → BUILD SUCCESSFUL: 228/228 · 156/156 (3 skip); `spotlessJavaCheck` ×2 executed; `compileJava` ×2 fresh, zero `warning:` lines under `-Werror`.** 4 22:06 the same with `--rerun` on the three compile/test tasks → BUILD SUCCESSFUL, 4 executed; XML 22:06:01Z/:03Z.
- **Deferred Build Gate: YES** — `./gradlew check` (ArchUnit in `:app`) owed to CI on Nick's push.
- **Preflight:** `CODER FRESHNESS PREFLIGHT — 2026-09-12 21:5x UTC — PASS (all 7 + Check 12)`. Check 1 note: `coder-handoff.md`'s newest entry is R-7b (08-23) — the hub writes the handoff (instruction §0); the instruction + v71 b4 are the plan of record. Check 6 `diff -rq` empty. Check 12 clean.
- **ARCH-RULE-REACH:** Rule 8 `:266` · Rule 9 `:306` (the endpoints read a record) · `NO_DIRECT_TIME_ACCESS :98` — no clock read added (every new instant is an envelope's); diff-only sweep for `Instant.now`/`systemUTC`/`currentTimeMillis`/`nanoTime`/`synchronized`/`System.out`/`Thread.sleep`/`TODO`: none. One READ added (`readByType(AUTOMATION_DISABLED)`), no write — both `projection_writesNothing` tests green (INV-SA-03).
- **INV/LTD at source:** INV-SA-03 (`Architecture_Invariants:1086`, Doc 16 `:264`) · INV-ES-06 `:206` · INV-TO-03 `:494` · LTD-04 `Locked_Decisions:147` · LTD-08 `:287` · Doc 01 `:400` (DP-G) — all ✓; **LTD-09 `:324` is YAML configuration**, not the clock law → R4.
- **P2 re-run (`git grep -c`):** `ActionView(` 2 + 3 ✓ · `NonFiringExplanation(` 8 + 8 · `AutomationSummary(` 1 + 4 · `RunExplanation(` 1 + 2 · accessor/static-factory collisions: none. Glossary ×5 resolve; the new key names are the contract's / SPEC §6's. JPMS: `module-info` ×2 unchanged; `AttributeValue` never reaches the exported API.
- **`WhyNotView.tsx` at HEAD (read-only):** an unknown verdict falls out of the closed `switch` (`:107–:138`) to `:141–:146` — the `not-recorded` glyph and `Recorded as "{verdict}" — a verdict this dashboard can't explain yet.` (`i18n.ts:145`), body/link null; `frontend.yml` does not run on this commit.

## §3 Pushback / observations
- **R1 `[REVIEW]` — DP-3's named source has no string rendering.** `GetEntityStateEndpoint:114` puts the `EntityState` record on the wire (Jackson: an OBJECT; rest-api main never names `AttributeValue`); `MaterializedStateQueryService:254` reads `rawValue()` only as a Number. The ONE string dialect already on the explain wire is `AttributeValues.asString` (`:31`, `String.valueOf(rawValue())`): it IS `observedState[].value` (`StandardRunConditionGate:150`) and the ledger's `state_confirmed.expectedValue` (`StandardPendingCommandLedger:997`). Used it — no new helper, no record `toString()` (T1b pins `"72"`).
- **R2 `[REVIEW]` — the DISABLED walk reaches less than T10 reads.** An auto-disable never touches the registry (`StandardRunManager.disabled`, add-only, `:163`/`:539`; no `automation_enabled` event exists) while `explainNonFiring` derives `DISABLED` from the registry's `enabled` — a configuration fact. So an auto-disabled automation whose YAML still says enabled reports from its last terminal run (FAILED ⇒ `ACTED_BUT_UNCONFIRMED`), never `DISABLED`; the walk fires only for a configuration-disabled automation that ALSO carries an earlier marker (then `disabledReason = "repeated_failure"`). Implemented as ordered; T10 seeds that shape. The honest fix (`DISABLED` when `latestDisabled != null` too, plus a re-enable rule the log lacks) changes a verdict — a 114b/c row.
- **R3 `[REVIEW]` — `settledAt` null for a superseded DISPATCHED although `settled == true`.** Implemented as written, T7 pins it; the superseded result's instant IS on the log — `settledAt != null ⇔ settled` is a one-line flip in `deriveOutcome`'s last branch. The hub's call.
- **R4 `[REVIEW]` — cite:** §5's "LTD-09 / `NO_DIRECT_TIME_ACCESS`" — LTD-09 is YAML (`:324`); the clock law is `HomeSynapseArchRules:98`. No code impact.
- **`[INFO]`** I1 the `FIRED_CONFIRMED` sentence is the existing one verbatim. I2 T1b/T3b/T7b/T9b/T11b added beyond T1–T16, one fact each. I3 T9 flipped TWO existing assertions (both named in the table). I4 the walk: one `SCAN_BATCH`-paged forward pass over the `automation_disabled` type index, last match wins, keyed on the payload's `automationId`, unbounded by the window; O(retained auto-disables). I5 a `forDuration` run's triggering event is the `trigger_duration_expired` envelope (`AutomationEngineSubscriber:70`) — in the correlation, not a state event ⇒ `firingValue` null by K1; its `startingEventId` names the state event — a 114b candidate.
- **Next WU:** 114b — `parentRunId` (note `RunInitiator:101`: every run starts at `RunCausalChain.root()`), condition text, the by-id read (K2); the hub authors it from this return.

## §4 WUCP Phase 1: Coder Closeout
- [x] MODULE_CONTEXT.md updated for: core/automation (banner + Gotcha), api/rest-api (§EXPLAIN-114a beside §CG-123)
- [ ] coder-handoff.md — not by this lane (instruction §0: the hub files the entry)
- [x] Deferred build gate flag: YES
- [x] coder-lessons.md appended: No new pattern
- [x] Cross-agent note posted: Not needed (channel retired)
- Timestamp: 2026-09-12 22:20 UTC

RETURNED nexsys-hivemind/context/audits/2026-09-12_EXPLAIN-114a_return.md 11999
