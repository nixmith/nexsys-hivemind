<!--
file: context/audits/2026-06-26_AMD-95-and-doc-currency_review_return.md
purpose: The Cowork source-verifying review return for (Tier 1) AMD-95 to ratify-readiness and (Tier 2) a doc-vs-source documentation-currency sweep against the frozen Java at core HEAD 5363347. Review ONLY — proposals for Nick to fold via review->ratify. Nothing was edited; no amendment was self-ratified.
audience: Nick (co-sign AMD-95 / rule Tier-2 remedy scheduling), PM (v6 hub), the DOCS lane (the Doc 07 / AMD-90 folds), the Core lane (M7.4 authors against the reconciled design)
state-type: review return (documentation currency + amendment review)
status: COMPLETE — authored 2026-06-26 in Cowork (nexsys-project-manager skill, Mode-1 review discipline, file + bash source access)
baseline: docs e47f01e (+ uncommitted Doc 17 DRAFT + AMD-95 PROPOSED, confirmed on disk untracked) / core 5363347 (M7.3 — the frozen source verified against) / hivemind 373a0f8 (living spine, ahead of the brief's stated 837e743; out of scope)
method: every signature/count/enum below was re-derived from git OBJECTS at core 5363347 (git show / git grep, never a worktree read — the truncated-tail hazard); docs read via host file tools (authoritative); git run --no-optional-locks (index.lock hazard).
-->

# Review Return — AMD-95 + Documentation-Currency Sweep (Cowork, source-verifying)

**Bottom line.** AMD-95's substance is correct and **fully source-verified** at core `5363347` — all eight frozen-signature/count claims hold exactly, the AMD-90 §2.1 supersede-in-part is the right disposition, and the zero-impact claim (no event mint, counts stay 71/41/53, no module-info, no source delta) is exact. **Verdict: RATIFY-WITH-EDITS** — the *rulings* need no change; the *consolidated edit list* AMD-95 hands to ratification is incomplete and should be extended so the same currency pass leaves §3.11 fully current rather than half-current. Separately, the Tier-2 sweep found the M7.4-authoring-critical documentation surface to be in strong shape (Docs 01/02/03/05/12/06/15 current or correctly forward-shaped; invariants register **169/49 reconciles exactly**); the genuine drift clusters in the command pipeline (the section AMD-95 already targets) plus one ratified-but-unbuilt amendment item (AMD-90 §2.2/§2.3 action permits) that AMD-95 §6 correctly flags and my sweep confirms fires.

---

## 0. Scope operated under (Nick confirms / may recut)

Per the dispatch brief §0, I swept the **`homesynapse-core-docs` documentation surface**: the design docs (`design/00`..`design/17` incl. the Doc 17 DRAFT), the **amendments** (`design/amendments/AMD-*`) as currency-cross-check targets (NOT free-edit targets), and `governance/`. Amendments were treated as point-in-time governance records: where one has drifted from shipped source (the AMD-90 cases below), I **propose a remedy** (currency note / new currency amendment) — I did **not** silently edit any ratified amendment. **Out of scope** (untouched): the hivemind spine (`PROJECT_SNAPSHOT`, `pm-handoff`, backlog, decision records). If you want a different cut (e.g. include the hivemind `references/`), that is your call — say so and I re-run.

**Review-only discipline held:** no design doc, amendment, or invariant was edited or minted. Everything below is a proposal for you to fold via review->ratify. AMD-95 is not self-ratified.

## Preflight (light, per brief)

| Item | State | Note |
|---|---|---|
| core HEAD | `5363347` (M7.3, clean tree) | The frozen source verified against — matches the brief baseline exactly. |
| docs HEAD | `e47f01e` (Doc 16 Locked; watermark AMD-94) | Untracked on disk: `design/17-aiot-and-cloud-readiness.md` (DRAFT) + `design/amendments/AMD-95_*.md` (PROPOSED) — exactly as the brief predicted. |
| hivemind HEAD | `373a0f8` (+ 4 modified spine files) | Ahead of the brief's stated `837e743`; both are 2026-06-26 v6-hub commits. Hivemind is the living spine and **out of scope** — not a blocker, not CONFLICTED. |
| Source-of-truth rule | Honored | Every count/signature re-derived from git objects at `5363347`; no stated number copied forward. |

---

# TIER 1 — AMD-95 to ratify-readiness

## 1.1 Source-verification of every frozen-signature claim (@ core 5363347)

All claims **VERIFIED EXACT**. Evidence is the git-object read at the frozen commit (file:line / verbatim signature).

| # | AMD-95 claim (section) | Source reality @ 5363347 | Result |
|---|---|---|---|
| 1 | `CommandIssuedEvent` = 5-component record `(Ulid targetEntityRef, String commandType, String parameters, int confirmationTimeoutMs, CommandIdempotency idempotencyClass)`; carries **no** expectation (§1.2) | `event-model/.../CommandIssuedEvent.java:30-35` — the five components verbatim; no `Expectation`/`AttributeValue` component | VERIFIED |
| 2 | `CommandAction` = frozen 4-field `(Selector target, String commandName, Map<String,Object> parameters, UnavailablePolicy onUnavailable)`; **no** `confirmation` 5th component (§1.3 / §2.C) | `automation/.../CommandAction.java:34-38` — exactly four components; no `confirmation` | VERIFIED |
| 3 | Confirmation signal is the capability's `ConfirmationPolicy.mode()` / device-model `ConfirmationMode` enum incl. `DISABLED` (§1.3 / §2.C) | `device/.../ConfirmationMode.java:22-37` = `{EXACT_MATCH, TOLERANCE, ENUM_MATCH, ANY_CHANGE, DISABLED}`; `device/.../ConfirmationPolicy.java:29-30` = `record ConfirmationPolicy(ConfirmationMode mode, ...)`; ledger consumes it at `StandardPendingCommandLedger.java:294` `if (instance.confirmation().mode() == ConfirmationMode.DISABLED) return;` (the OPTIMISTIC bypass) | VERIFIED |
| 4 | `CommandDispatchService.dispatch(EventId, EntityId, String, Map)` is in-process; **nothing publishes `command_issued`** in main (§1.1) | `automation/.../CommandDispatchService.java:43-44` = `void dispatch(EventId commandEventId, EntityId targetRef, String commandName, Map<String,Object> parameters)`; `StandardActionExecutor.java:184` calls `dispatchService.dispatch(...)` in-process; **zero** `new CommandIssuedEvent(` in any main source; `"command_issued"` appears only as the `EventTypes.COMMAND_ISSUED` constant + Javadoc — never published | VERIFIED |
| 5 | Expectation resolved from the capability's `CommandDefinition.expectedOutcomes()` via `EntityRegistry`; `ExpectationFactory` is interface-only, no impl (§1.2 / §2.B) | `device/.../CommandDefinition.java:31-36` = record with `List<ExpectedOutcome> expectedOutcomes`; ledger resolves at `StandardPendingCommandLedger.java:555` `entityRegistry.findEntity(target)` and `:572-583` `chooseOutcome(...)` reads `definition.expectedOutcomes()`; `device/.../ExpectationFactory.java:25` is an `interface`, and **zero** `implements ExpectationFactory` exists in main | VERIFIED |
| 6 | `StateReportedEvent.value` is a `String` (§1.4 / §2.D) | `event-model/.../StateReportedEvent.java:32` = `String value` (its own Javadoc flags "Phase 3 introduces typed AttributeValue" — the documented forward path) | VERIFIED |
| 7 | The automation-resident `ConfirmationPolicy{OPTIMISTIC, REQUIRED, BEST_EFFORT}` enum **does not exist** (§1.3 / §2.C) | No `enum ConfirmationPolicy` anywhere in the tree (the device-model `ConfirmationPolicy` is a *record*); `OPTIMISTIC`/`BEST_EFFORT` survive only as Javadoc references in `StandardPendingCommandLedger.java` | VERIFIED |
| 8 | Zero event mint; counts stay **71/41/53**; module-info unchanged (§3) | **71** `EventTypes` string constants; **41** core `@EventType` records (`EventTypeAnnotationTest` asserts `EXPECTED_EVENT_RECORDS.hasSize(41)` + "exactly 41 core event records carry @EventType"); **53** = 41 core + 12 integration registered = 53 `EventCategoryMapping.TABLE` rows (`EventTypeRegistryTest` asserts 41 core / 53 all). The amendment is doc-only — no source delta | VERIFIED |

**One precision nit (optional clarity edit, not a substance error).** AMD-95 §1.1 reads as if `StandardActionExecutor` "emit[s] `command_dispatched`/`command_result`." The actual emitter is the in-process collaborator it invokes, **`StandardCommandDispatchService`** (`command_dispatched` DIAGNOSTIC on success at `:135`; `command_result` on failure at `:143`); the executor itself publishes only its own `automation_action_started/completed` diagnostics. Doc 07 §3.11.1 already attributes these correctly to the dispatch service. Tightening the §1.1 sentence to "the executor calls `dispatch(...)` in-process; the dispatch service emits `command_dispatched`/`command_result`" removes the ambiguity. Harmless either way.

## 1.2 Ruling on the AMD-90 §2.1 supersede-in-part

**The disposition is CORRECT.** Withdrawing, for the V1 engine, (a) the `CommandAction.confirmation` 5th component (the never-added 4->5 field change) and (b) the automation-resident `ConfirmationPolicy{OPTIMISTIC, REQUIRED, BEST_EFFORT}` enum (which does not exist in source), in favor of **capability-sourced** confirmation via `ConfirmationMode` (`DISABLED` == optimistic/no-track), matches the as-built engine exactly (claims 2, 3, 7 above). The M7.2b action-model freeze (`1b0b6c9`) froze `CommandAction` at four fields; the confirmation signal genuinely lives on the capability.

- **AMD-90-INV-01 (no engine retry) is correctly left untouched** and is still honored in source — no autonomous re-issue exists on any path (the M7.2b/M7.3 "one dispatch" pins). AMD-90-INV-02 (bounded iteration) is likewise not disturbed.
- **AMD-90's `RepeatAction` / `InvokeAutomationAction` items are correctly out-of-scope here (flag-only, §6).** My Tier-2 sweep **confirms the flag fires**: the shipped `ActionDefinition` permits **8** types, not AMD-90's 9, and `ActivateSceneAction` was never renamed (Tier-2 finding D-07-A). That is a *separate* action-model currency gap, rightly fenced out of this command-pipeline amendment.

## 1.3 Zero-impact confirmation

CONFIRMED on all three axes: **no event-type mint** (counts 71/41/53 re-derived exact, three independent ways — §1.1 claim 8), **no module-info change** (the amendment is doc-only; the M7.3 closeout already established both `:core:automation` and `:core:event-model` module-infos unchanged at `5363347`), and **no source change from the amendment itself** (M7.4 is the code work unit; AMD-95 reconciles prose to the frozen source).

## 1.4 Verdict and consolidated edit list

### VERDICT: **RATIFY-WITH-EDITS**

Ratify the substance as-is. The "edits" are **edit-list additions** — none reverse an AMD-95 ruling; they extend the ratification fold so §3.11 (and its two cross-referencing sites) is left fully current. The source-verification surfaced three stale items living *inside the very sections AMD-95 edits* that its §3 edit list omits, plus the §1.1 precision nit.

**Edits AMD-95 already specifies (apply at ratification — all confirmed correct against source):**

1. **Doc 07 §3.11.1** — affirm the event-driven shape; add the co-located-for-MVP sentence; add the current-vs-target currency note (as-of M7.3 the executor dispatches in-process and emits no `command_issued`; M7.4a wires the event-driven/co-located shape). Correct the `ExpectationFactory` step to capability-sourced `CommandDefinition.expectedOutcomes()`.
2. **Doc 07 §3.11.2** — correct "expected outcome from the event payload" -> capability-resolved (`EntityRegistry.findEntity` -> `CommandDefinition.expectedOutcomes()`); add the confirmation-from-capability sentence (`ConfirmationMode.DISABLED` bypass); add the `String`->`AttributeValue` coercion note (total; uncoercible -> `DegradedAttributeValue`).
3. **Doc 07 §16** — add the confirmation-policy-on-capability decision row (no such row exists today; it becomes D16).
4. **AMD-90** — a §11 "Superseded-in-part by AMD-95" note on §2.1 (withdraw the `CommandAction.confirmation` 5th component + the `ConfirmationPolicy{OPTIMISTIC,REQUIRED,BEST_EFFORT}` enum for the V1 engine; confirmation is capability-sourced). INV-01/02, the timeout design, and the RepeatAction/InvokeAutomation items untouched.
5. **Nav-index row + watermark AMD-94 -> AMD-95; spine flip** (snapshot watermark; backlog M7.4 row references AMD-95).

**Edits to ADD to the list (genuine drift in the same sections; folding them now avoids a second pass):**

6. **Doc 07 §3.11.1 step 2** — `DeviceRegistry.getIntegrationForEntity(entityRef)` is stale: **no such method exists in source.** The real resolution is the two-hop `EntityRegistry.findEntity -> Entity.deviceId() -> DeviceRegistry.findDevice -> integration` (the shipped `StandardCommandDispatchService.java:41` Javadoc explicitly names `getIntegrationForEntity` as the thing it is *not*). Correct step 2 to the two-hop path. *(Genuine drift — HIGH, because M7.4a authors directly against §3.11.1.)*
7. **Doc 07 §3.11.1 step 5 + §7 (line ~777)** — `CommandHandler.handleCommand(entityRef, commandName, parameters)` is stale: source is `void handle(CommandEnvelope command) throws Exception` (`integration-api/.../CommandHandler.java:61`); the three args are now `CommandEnvelope` fields. `handleCommand` exists nowhere. Correct both sites to `CommandHandler.handle(CommandEnvelope)`. *(Genuine drift — HIGH. Doc 05 §3.8 itself is already correct; only the Doc 07 citation drifted.)*
8. **Doc 07 §4.3 (PendingCommand record)** — the field comment `Expectation expectation, // from ExpectationFactory` carries the *same* stale claim §3.11.2 step 1 corrects, but §4.3 is omitted from AMD-95's edit list. Change the comment to capability-sourced (`from CommandDefinition.expectedOutcomes()`). *(Genuine drift — MED; cheap to fold in the same pass.)*
9. **(Optional) AMD-95 §1.1** — tighten the `command_dispatched`/`command_result` emitter attribution to `StandardCommandDispatchService` (the §1.1 precision nit above).

---

# TIER 2 — Documentation-currency drift register (prioritized HIGH -> LOW)

**Method calibration.** Source is M7.3 (`5363347`); some doc prose legitimately describes the M7.4+ end-state. I distinguish **genuine drift** (doc describes a thing the code built *differently*) from **not-yet-built forward shape** (doc describes the intended end-state not yet reached) from **cosmetic** (sanctioned naming shorthand). The recurring "the docs describe a thing the code never built" failure mode is largely **absent** from the M7.4-critical surface — the docs are notably current. Genuine drift concentrates in the command pipeline (Tier-1 territory) plus one ratified-but-unbuilt amendment.

| ID | Doc claim (file §section) | Source reality (file:line / signature / count) | Classification | Proposed remedy | Priority |
|---|---|---|---|---|---|
| D-07-A | AMD-90 §2.2/§2.3 + Doc 07 line-13 banner: action permits expand to **9** (`+RepeatAction`; `ActivateSceneAction`->`InvokeAutomationAction`) | `ActionDefinition.java:37-39` permits exactly **8** (`CommandAction, DelayAction, WaitForAction, ConditionBranchAction, EmitEventAction, ActivateSceneAction, InvokeIntegrationAction, ParallelAction`); `ActivateSceneAction.java` still present; no `RepeatAction`/`InvokeAutomationAction` files exist | genuine drift (ratified-but-unbuilt) | A separate **action-model currency pass**: decide build (a M7.x slot) vs defer (a currency note marking AMD-90 §2.2/§2.3 forward/unbuilt). The AMD-95 §6 flag, now confirmed. | **HIGH** (it is a ratified amendment the code never built — the exact class this sweep exists to catch; not on the M7.4 critical path, so schedulable) |
| D-07-B | Doc 07 §3.11.1 step 2 / step 5 / §7: `DeviceRegistry.getIntegrationForEntity(...)` and `CommandHandler.handleCommand(entityRef, commandName, parameters)` | No `getIntegrationForEntity` in source (two-hop `EntityRegistry.findEntity`->`Entity.deviceId()`->`DeviceRegistry.findDevice`); `CommandHandler.java:61` = `handle(CommandEnvelope)` | genuine drift | **Fold into the AMD-95 ratification pass** (Tier-1 edits 6 + 7) | **HIGH** (M7.4a authors against §3.11.1) |
| D-12 | Doc 12 §3.5/§7: startup "Recover the `PendingCommandLedger`" (Step 3.4/3.5) + shutdown flush | Not wired in `HomeSynapseCore` at `5363347` — the Step-3.5 registration was **reverted at the M7.3 gate-fix** because a runtime subscriber with no paired `stop()` teardown leaks its SQLite read connection (`core/automation/MODULE_CONTEXT.md`). Live registration + teardown deferred to M7.4. | not-yet-built forward shape | Currency/foresight note in Doc 12: the ledger subscriber's `stop()`-teardown pairing is the explicit M7.4 wiring precondition. Cleanest folded **with M7.4's own doc update**, not a standalone amendment. | MED |
| D-06 | Doc 07 §9 (config): `automation.command_pipeline.default_confirmation_timeout_ms: 30000` (range 5000-120000); AMD-90 says the key "EXISTS at baseline" | In source the value exists only as a Java constant `DEFAULT_CONFIRMATION_TIMEOUT_MS = 30_000L` (`PendingCommandLedgerAssembly.java:46`) — **no wired config-schema key, no range enforcement** (the pipeline is unwired at M7.3). Default value matches. | not-yet-built forward shape | Currency note: the schema key + range land with the live command-pipeline wiring (M7.4). Value is correct today. | LOW-MED |
| D-15 | Doc 15 §3.4/§4.1/§6 (AMD-94): every encrypted row carries a 1-byte envelope version/algorithm discriminator; "rotate-DEK-on-restore" restore contract | Not built at `5363347`: `V005__at_rest_payload_encryption_columns.sql` adds only `payload_iv` + `dek_ref` (no `envelope_version` column); `EncryptedPayload.java` is 3-field `(ciphertext, iv, keyVersion)` — no version byte; no rotate-on-restore path. AMD-94 itself states it "changes no shipped code... corpus empty until the first encrypted write at AB-4." Crypto-at-rest is INERT in M7.3 (`payloadCipher=null`). | not-yet-built forward shape (correctly anticipated) | **No-op** — design contract for an unbuilt feature; reserved-in-design, lands at AB-4. | LOW |
| D-12b | Doc 12 §8.4: `SystemLifecycleManager` interface pseudocode shows bare `void start()` / `void shutdown(String)` | Source declares `void start() throws Exception` / `void shutdown(String) throws Exception`; otherwise all 5 methods match and `HomeSynapseCore` implements them | cosmetic | Optional currency note (pseudocode omits the `throws`) | LOW |
| D-COSM | Sanctioned naming shorthand across docs: `ULID`/`EntityRef` (concept) vs `Ulid`/`EntityId` (typed); `StateQuery` (Doc 07 §7 prose) vs `StateQueryService` (source); wire-name `command_type` vs record component `commandType` | The typed/concept and wire/Java conventions are documented project-wide | cosmetic / acceptable | No-op | LOW |

**Verified CLEAN against source at 5363347 (no remedy needed):**

- **Doc 02 (device model)** — `CommandDefinition` (6-comp incl. `List<ExpectedOutcome> expectedOutcomes`, `Duration defaultTimeout`), `ExpectedOutcome`, `ConfirmationMode` (5 constants), `ConfirmationPolicy` (record, `.mode()`), `EntityRegistry.findEntity`, `Entity` (12-comp incl. `entityRole`, matching the folded AMD-44 banner), `EntityType` legal-role matrix, `Capability` accessors. Current.
- **Doc 01 (event model)** — the AMD-92 automation family is exactly **19** `[automation]`-category types in source, names matching; `CommandIssuedEvent`(5)/`StateReportedEvent.value`(String)/`StateConfirmedEvent`(6)/`CommandConfirmationTimedOutEvent`(commandEventId,resultEventId) match; the AMD-52 `state_changed` v1->v2 deliberately-not-upcasted seam matches `EventPayloadCodec.java:174-180`. Current. (Counts 71/41/53 re-derived — Tier-1 claim 8.)
- **Doc 03 (state store)** — `StateQueryService` (`getState`/`getStates`/`getSnapshot`/`getViewPosition`/`isReady`) and `StateSnapshot` match component-for-component. Current.
- **Doc 05 (integration runtime)** — `CommandHandler.handle(CommandEnvelope)`, `IntegrationAdapter`, `IntegrationDescriptor`, `IntegrationContext`, `IntegrationFactory` all present as documented. Current. (Doc 05 §3.8 is correct; only Doc 07's *citation* of it drifted — D-07-B.)
- **Governance invariants register** — masthead **169/49 reconciles exactly**: §17 Invariant Index = **169** identifier rows; §0.3 category-prefix table = **49** categories (regeneration trail 152/41 -> 163/47 -> 165/48 -> 169/49). Every spot-checked id resolves (`INV-ES-04/06`, `INV-TO-01/02`, `INV-SA-01..04`, `AMD-90-INV-01`, `AMD-92-INV-01`).

---

## Sequencing recommendation

**Fold AMD-95 before M7.4a authoring — it is the gate.** Ratify it with the **extended edit list** (the §3.11.1/§3.11.2/§16 + AMD-90-note edits AMD-95 already specifies, **plus** edits 6-8: the §3.11.1 `getIntegrationForEntity` two-hop correction, the §3.11.1/§7 `handle(CommandEnvelope)` signature correction, and the §4.3 `// from ExpectationFactory` comment — and optionally the §1.1 emitter-attribution tightening). M7.4a wires the command-pipeline spine directly against §3.11 and §7, so these are precisely the sentences it will read; fixing them in one pass is the whole point of authoring-against-reality. **Schedule, but do not block M7.4a on, the AMD-90 §2.2/§2.3 action-permit currency pass (D-07-A)** — a ratified-but-unbuilt amendment is the highest-signal Tier-2 finding, but `RepeatAction`/`InvokeAutomationAction` are off the M7.4 critical path, so it can be a fast-follow currency amendment (mark forward/unbuilt) or a scheduled build slot; the imperative is only that AMD-90 stop reading as "built" when it is not. **Let the two forward-shape notes (D-12 ledger-wiring foresight, D-06 config-schema key) ride M7.4's own doc-fold** rather than spending a standalone amendment now — they describe exactly what M7.4 makes real; log them on pm-handoff so M7.4's WUCP Phase 2 closes them. **No action** on D-15 (correctly forward; lands at AB-4) or the cosmetic shorthands.

---

## Done-when / what Nick does next

1. **Co-sign AMD-95** (the PM does not self-ratify). On co-sign, apply the Tier-1 §1.4 edit list (items 1-5 as specified + 6-8 added + optional 9), advance the watermark AMD-94 -> AMD-95, add the nav-index row, and flip the spine (snapshot watermark; backlog M7.4 row references AMD-95).
2. **Rule the Tier-2 remedy scheduling** per the recommendation above — chiefly: build-vs-defer for AMD-90 §2.2/§2.3 (D-07-A), and confirm D-12/D-06 ride M7.4's fold.
3. Nothing here is folded. This return is the proposal set; the DOCS edits happen under your co-sign via review->ratify.

*Source-verified against homesynapse-core HEAD 5363347 (M7.3). Docs read at e47f01e + the untracked AMD-95 PROPOSED / Doc 17 DRAFT. No file outside this return was created or modified.*
