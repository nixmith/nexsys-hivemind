<!--
file: context/planning/2026-06-19_M7-forward_plan.md
purpose: The recorded M7-forward plan — (A) the M7.1 second-check verdict, then (B) the scope + sequencing plan for the rest of M7 (M7.2 split, M7.3, the Doc 16 review->Lock prerequisite, the M7.2-vs-app-bootstrap interleave, substrate-gap routing, the M7.2 entry-gate), with the three 2026-06-18 interlocks baked in (Doc 16 gates the M7.2 action-model freeze; composition-root wiring deferred to app-bootstrap; D2/REC-162 live).
audience: Nick (rules sequencing + D2/REC-162), PM, the future M7.2/M7.3 + app-bootstrap coding-instruction sessions, the Doc 16 DOCS-review session
state-type: planning (verification verdict + Phase-3 forward plan)
status: RECORDED 2026-06-19. Part A verdict = PASS-WITH-FINDINGS (2 cosmetic currency findings reconciled in-session; 1 informational observation). Part B = recorded; M7.2 NOT dispatched (entry-gate not GREEN — Doc 16 not Locked, D2 not ruled); owner-tagged gate list stated; sequencing + D2 escalated to Nick.
baseline: core beb4bc3 (M7.1 committed+pushed, gate-verified GREEN 149 tasks) / docs 32afb3f (Doc 16 committed-as-DRAFT, NOT Locked) / hivemind ec9905e (M7-forward prompt + archive). M6 COMPLETE 4-of-4; M7.1 DONE; watermark AMD-93 (invariants 163/47, no new AMD landed); Doc 15 LOCKED; Doc 16 = review-candidate DRAFT.
preflight: PASS (currency-lag findings F1/F2 logged + reconciled in-session; Check 9 benign-STALE pending Nick mirror sync; zero CONFLICTED). HEADs reconciled below.
anchors: context/decisions/2026-06-18_app-bootstrap-and-superiority-scope_decisions.md (Part B scope ruling + M7 interlock verdict + the M7.1 wiring-deferral addendum); context/planning/2026-06-12_M7-M8-charter-skeleton.md + 2026-06-12_M7-blueprint_merged-disposition.md (M7.x decomposition + obligations); context/planning/2026-06-15_app-bootstrap_charter.md (AB-1..AB-4 + residual); homesynapse-core-docs/design/16-superior-automation.md (the DRAFT; §7.2 M7-impact interlock); weeks/2026-W26_jun22-jun28.md (lanes)
-->

# M7-Forward Plan — M7.1 Second-Check + M7.2/M7.3 Scope & Sequencing

PM/Architect session (nexsys-project-manager, Mode-3 Director with a Mode-1 read of Doc 16 §7.2). Two payloads, in order: Part A verifies the M7.1 landing; Part B is the forward plan. Nick rules the sequencing call and the D2/REC-162 disposition; the PM assembled, verified, planned, and recorded.

## Rulings (Nick, 2026-06-19) — both escalations decided

Nick ratified both PM recommendations, each with a refinement folded forward.

**R1 — Sequencing: app-bootstrap AB-3 takes the next Coder slot (RULED).** Runnability is the existential gap the core-review named (sound but not runnable — `main()` is a stub); the 2026-06-18 pivot prioritizes it over speed-running the engine. AB-3 is the load-bearing piece: the composition-root/lifecycle substrate that unblocks M7.1's deferred wiring (subscriber + config-loading + the lifecycle wiring test all ride AB-3) and gives M7.2 a runtime to dispatch into. Interleaving M7.2a first would add a second milestone of correct-but-inert engine code to the exact pile the core-review flagged — motion, not progress toward runnability.
- **Refinement (resolve up front in the AB-3 instruction):** AB-3 surfaced that the runtime assembles no production Entity/Device/Area registries (device-model breadth — AMD-44/Research-8). The AB-3 lifecycle skeleton (startlevel ladder, health loop, phase gating) is buildable without them, but the registry-dependent wiring needs them. **AB-3 scope must either fold minimal production registries or sequence that device-model slice just ahead — resolved in the instruction, never a silent block.**
- **Fallback (explicit):** M7.2a is the fallback ONLY if the AB-3 registry-prep genuinely stalls and the Coder slot would otherwise idle. Default priority is app-bootstrap. Doc 16 review→Lock runs in parallel either way.

**R2 — D2/REC-162: keep the anti-retry default; rule at M7.2b (RULED).** Retry-vs-re-issue is an action-model question, and the action model is designed at M7.2b (Doc-16-gated). Deciding now means ruling on the action model's semantics before it is in front of us — premature; Doc 16 already keeps no-engine-retry and defers it. REC-162-as-default forecloses nothing (safe, reversible); M7.2b is the natural decision point with the full sealed model in hand.
- **Refinement (cheap, at M7.2 scoping — NOT a REC-162 flip):** confirm that the *verification* half of the field demand — "did the device actually reach the commanded state?" — is **already satisfied by the `Expectation` model + AMD-90 confirmation** (R-δ judged it likely is). A fact-check against what is built. If verification is covered, the only open M7.2b question is the narrow one: whether a guarded, expected-state-gated, idempotent re-issue earns its place in the sealed model.

Both rulings keep the irreversible calls at the moment of maximum context — the same discipline as the A4 version-tag and the Doc 16 split.

---

## Step 0 — Preflight + HEAD reconciliation

**HEADs (host-verified; VM `git status` quarantined — see below):**

| Repo | Baseline (prompt) | Actual HEAD | Delta |
|---|---|---|---|
| core | `beb4bc3` | `beb4bc3` | MATCH — M7.1 committed, "gate-verified GREEN, ./gradlew check 149 tasks" |
| docs | `f2e064d` | `32afb3f` | +1 — **Doc 16 committed-as-DRAFT** ("Review-candidate"). Benign currency lag (Nick-flagged); NOT a conflict; **Doc 16 is NOT Locked.** |
| hivemind | `0f3951f` | `ec9905e` | +1 — the M7-forward session prompt + consumed-prompt archive. Benign. |

**Working-tree "modifications" = the truncated-tail mount-lag artifact, NOT real changes.** All three repos showed files cut at EOF ("No newline at end of file", two files mis-reported as `Bin`, ~pure-deletion diffs). Confirmed against the host file tools: e.g. `StandardTriggerEvaluator.java` is intact on the host (closes cleanly, trailing newline at line 627) while the VM diff showed it truncated. Per cowork-environment-model §2/§5: the host file tools are authoritative; the VM git view is suspect; nothing was "fixed" or committed from it. **The working trees are clean on the host.**

**Preflight aggregate: PASS** (currency-lag findings F1/F2 logged for in-session reconciliation; Check 9 benign-STALE pending Nick's mirror sync; **zero CONFLICTED** — every SHA resolves). Checks 1/3 carry the F2 currency-lag (snapshot Recent-Session-Log table + footer behind the masthead); Check 11 = the source round-trip below; Check 9 = expected post-agent-pass STALE. The user-flagged docs delta (`32afb3f`, Doc 16 committed-as-draft) is the only baseline-line delta and is benign.

---

## PART A — M7.1 verification verdict

**VERDICT: PASS-WITH-FINDINGS.** M7.1 is truly closed out and sound. The build is not re-litigated (the gate passed, 149 tasks, attested in the `beb4bc3` commit message and the PM WUCP Phase 2 record). All material checks PASS; two cosmetic currency findings (F1, F2) are reconciled in-session; one informational observation (O1) is carried into the plan. No material closeout gap and no silent contract constraint.

### A1 — Closeout consistency — PASS (with F1, F2)
Backlog M7.1 = DONE (`beb4bc3`, GREEN 149); PROJECT_SNAPSHOT masthead + Current-WU = M7.1 LANDED GREEN / M7.2 NEXT; pm-handoff = the detailed WUCP Phase 2 record (gate-fix round 1, the [REVIEW] adjudications, next-WU); MODULE_CONTEXT ×2 (automation + event-model) updated; coder-lessons carries three 2026-06-19 entries incl. the FIX-07 superseding lesson. **Watermark AMD-93 confirmed** — AMD-94 is NOT on disk (only AMD-90..93 exist as files); AMD-94 is reserved/pending for app-bootstrap's Doc 15 §6 amendment, not an M7.1 artifact. No new AMD landed.

- **Finding F1 (cosmetic — currency lag in a Coder-owned hot-path file).** The coder-handoff masthead (committed in the PM closeout `0f3951f`) still frames the M7.1 gate as "BUILD GATE DEFERRED / gate RE-DEFERRED / Open Risk until GREEN / NOT gate-verified" — the Coder's hand-back posture (the Coder cannot run Gradle), never flipped to the landed GREEN. The authoritative records unanimously contradict it: the `beb4bc3` commit message says "gate-verified GREEN, ./gradlew check 149 tasks", and pm-handoff/snapshot/backlog all record RESOLVED/DONE. **Effect: cosmetic** (the gate IS green); but it could mislead a future Coder. **Owner: PM. Fix: a one-line reconciliation note on the coder-handoff DEFERRED section (applied this session, single-anchor, host-side).**
- **Finding F2 (cosmetic — secondary-record lag in the snapshot).** The PROJECT_SNAPSHOT Recent-Session-Log table top row is 2026-06-14 (Track-4); the 2026-06-18 converge, the app-bootstrap-decisions, and the M7.1-landing sessions live in the masthead notes but were not appended as session-log rows; the "Last updated" footer reads 2026-06-12. The masthead + Current-WU are current. **Owner: PM. Fix: append the session-log rows + correct the footer (this session's closeout).**

These two are exactly the "M7.1 closeout under-recorded something" class the brief's Step 0 warned about — both are currency-lag in secondary/Coder records, not conflicts, and the primary records (masthead, Current-WU, backlog, pm-handoff, MODULE_CONTEXTs, coder-lessons, the commit itself) are current and mutually consistent.

### A2 — Deferrals correctly tracked (no silent debt) — PASS
- **(a) Composition-root wiring** (the `automation_engine` subscriber `new` + config-loading/schema-registration + the lifecycle wiring test) → **app-bootstrap AB-3.** Home named in the decision-record addendum (inbound dependency: AB-3 must assemble `ConfigurationService` + production Entity/Device/Area registries, wire the subscriber into `start()` subscribe-after-state-store-catch-up, carry the M7.1 lifecycle wiring test) and the AB-3 backlog row.
- **(b) The FIX-07 config-edge lesson** (the `core->config` ban) → coder-lessons 2026-06-19: the superseding lesson "the §authoring exported-API check is necessary but NOT sufficient; `assertAllowedModuleDependencies` bans a forbidden LAYER edge at ANY scope" — explicitly captured so M7.2/M7.3 cannot repeat it, with the architecturally-correct home for composition-root glue stated (lifecycle/app, not core:automation).
- **(c) The schema fragment** lives in the config-free `AutomationSchema` holder — source-confirmed: `AutomationSchema` exists (SCHEMA_SECTION + SCHEMA_JSON), `AutomationConfigBridge` is deleted, and `core/automation/module-info.java` has NO `requires com.homesynapse.config` (it keeps the legal `requires com.homesynapse.event.bus` core->core edge).

All three deferrals have a named home. No silent debt.

### A3 — The six [REVIEW] adjudications hold — PASS
Three substrate gaps routed forward (slug-tombstone → future identity/device WU; first-class `Area` slug → device-model AMD-44 Stage-2; `Availability` asleep-vs-dead granularity → integration/device per R-δ AX-8) — re-routed in Part B item 5. Three behavioral defaults recorded: (i) multi-entity condition = all-of / empty→false; (ii) `EventTrigger` event-type-only matching (payload-field matching deferred); (iii) device-subject duration `entityRef` flattening.

**None silently constrains M7.2** — all three are tracked as explicit M7.2 carry-items (pm-handoff + coder-handoff): (i) fold a Doc 07 §3.8 clarification when the condition path is next touched at M7.2; (ii) `EventTrigger.payloadFilters` matching lands at M7.2; (iii) the `entityRef` flattening cleanup lands at M7.2. The plan accounts for them as M7.2a carry-items (Part B item 1) so they are not forgotten. The two the brief flags specifically — the condition semantics and the `entityRef` flattening, which M7.2's run/action model touches — are tracked, not silent.

### A4 — Source round-trip spot-check (Check 11) — PASS (no fabrication)
Verified against source at `beb4bc3` (subagent + direct git-diff confirmation):
- `StandardTriggerEvaluator.evaluate(EventEnvelope)` returns `List<AutomationId>` — the matched-IDs decision, not void. ✓
- The four service impls exist as named: `StandardAutomationRegistry`, `StandardTriggerEvaluator`, `StandardConditionEvaluator`, `StandardSelectorResolver`. ✓
- AMD-88 `TriggerDefinition` = 12 permits (+`CalendarTrigger`/`ReachabilityTrigger`/`ManualTrigger`, `WebhookTrigger` promoted); AMD-89 `Selector` = 7 permits (+`SemanticTagSelector`). ✓
- **The AMD-92 slice that landed = rows 1/3/11–16/19:** `AutomationTriggeredEvent` reshaped to the flattened shape (Ulid/EventId/List<String>/Map/String/int — no automation domain type) + 8 new event records; **+7 `EventTypes` constants (55→62)**; `CORE_PRODUCTION_EVENT_CLASSES` 24→32; `EventCategoryMapping.TABLE` 36→44 — **all source-accurate.** The "+7 EventTypes vs +8 records" is the documented gap (row-1 reshape adds 0 constants against the existing `AUTOMATION_TRIGGERED`; row-19 maps a new record to an existing constant). _Note: an interim verification flagged "+8 constants" — re-checked directly against `git diff 03f16dc..beb4bc3`: exactly 7 new constant names; the "+8" was a miscount. The governance records are correct._
- **The rows M7.2 still owes = 2/4–10/17/18** (the run-lifecycle/dispatch slice). Confirmed M7.2 production code does NOT yet exist: `ActionExecutor`/`RunManager`/`CommandDispatchService`/`PendingCommandLedger` are interface-only (no impl), `RunCausalChain` is ABSENT, and `RunContext` still carries `int cascadeDepth` (the AMD-91 swap is M7.2 work). No fabricated forward dependency.

### Observation O1 (informational — carried into the plan)
Doc 16 §4/§8.2 label `RunCausalChain` "Existing (AMD-91)" and its explainability surface (§3.3) reads it. In source `RunCausalChain` is not yet a Java type — M7.2 builds it via the AMD-91 `RunContext`→`RunCausalChain` swap. This is **consistent** for a Phase-1 design doc (it references the ratified AMD-91 contract; the explainability/component surface builds with/after M7.2, never into M7.1) and does NOT undercut the M7.1-UNAFFECTED verdict. The plan owns it: **M7.2 builds `RunCausalChain`; Doc 16's explainability/audit surfaces sequence after that lands.**

---

## PART B — The M7-forward plan

### The three interlocks, baked in

- **I1 — Doc 16 gates the M7.2 action-model freeze.** Doc 16 §7.2 (the mandatory M7-Contract-Impact Interlock) states **M7.1 UNAFFECTED · M7.2 SHAPED (builds into the doc; do not freeze its action contract first) · M7.3 UNAFFECTED**, adds **no sealed permit and no event type** (AMD-88..93 untouched), and confirms M7.2 is *forward-shaped* because it is unbuilt. Verified consistent with the landed M7.1 reality (the trigger/condition path, the AMD-92 inventory, and the AMD-88/89 permits are all unchanged by Doc 16). Doc 16 is review-ready but **NOT Locked** — so the action-model half of M7.2 is gated on Doc 16 Lock.
- **I2 — composition-root wiring deferred to app-bootstrap.** M7.1 built GREEN against injected/stubbed deps because the runtime assembles no `ConfigurationService`/registries. **M7.2 builds the same way** (run/action/dispatch logic + the event slice, gate-verified without a live composition root — same pattern, same DP-non-preclusion seam discipline). Boundary: M7.2 builds-and-tests against injected deps; its eventual wiring (subscriber-into-`start()`, `ConfigurationService`/registry assembly) rides **app-bootstrap AB-3**, alongside M7.1's deferred wiring.
- **I3 — D2/REC-162 (retry vs Expectation) is a live M7.2 action-model question.** Doc 16 §3.4/§14/§15-Q5 keeps **no-engine-retry (REC-162 / AMD-90-INV-01)** as the current contract and **explicitly does not pre-empt** the decision. The standing question: does the field's retry demand belong as a *guarded, expected-state-gated, idempotent bounded re-issue* in the sealed action model, or is it already satisfied by `Expectation` + AMD-90 confirmation (with remediation parked at M8.2 as ledger-signal-driven, above the transport)? **This is a Nick call, tied to Doc 16's action-model section; it must be ruled at/before the M7.2 action-model freeze (M7.2b) — never flipped silently.** Routed in Part B item 6 + Escalations.

### B-1 — M7.2 scope decomposition (baseline-now vs Doc-16-shaped; P1-sized)

From the charter skeleton + merged disposition, M7.2 = `RunManager` (§3.7 FSM; C2 dedup; C3 ordering; concurrency §3.6; cascade governance §3.7.1) + `ActionExecutor` (§3.9 sequential, virtual threads, `UnavailablePolicy`) + `CommandDispatchService` (§3.11.1, `CommandValidator`, DIAGNOSTIC events) + the AMD-91 `RunContext`→`RunCausalChain` swap + the AMD-92 event slice rows 2/4–10/17/18 + run-trace data (§4.2). **That is ~5 sub-pieces → it exceeds the P1 smell-test (~3) → SPLIT into first-class sub-milestones.**

**M7.2a — Run lifecycle + causal chain + command dispatch — BASELINE-BUILDABLE-NOW (Doc-16-independent).**
Scope: `RunManager` FSM (states, C2 dedup, C3 ordering, concurrency §3.6, cascade governance §3.7.1); the **AMD-91 `RunContext`→`RunCausalChain` swap** (F4 — ratified; same-automation cycle detection + distinct diagnostic); `ActionExecutor` execution mechanics over the ratified sealed `ActionDefinition` permits (sequential, VT, `UnavailablePolicy`, §3.9, with the Doc 07 §6.2 failure behavior); `CommandDispatchService` + `CommandValidator` (§3.11.1); the **AMD-92 run-lifecycle/dispatch event slice (rows 2/4–10/17/18)** with full manifest fan-out + the consumer/pin survey; run-trace data (§4.2). **Build against injected/stubbed deps (I2); wiring → AB-3.** `RunManager.initiateRun(...)` is built with the Doc-16 computed-parameter-resolution as a **design-not-precluded wireable seam** (the M7.1 / M6.3-DP pattern) so M7.2b wires it with zero rework.
Carry-items (the A3 behavioral defaults): fold the Doc 07 §3.8 multi-entity-condition clarification; `EventTrigger.payloadFilters` matching; device-subject `entityRef` flattening cleanup.
Done-when: run-lifecycle FSM + dedup + ordering contract tests GREEN; cascade-depth governor test-pinned (default 8, range 1–32); REPLAY re-derive-never-re-execute kill-tests GREEN; W4/W5/W7 crash-window pins; `RunCausalChain` cycle-detection tests; C8 stamping test (`actorRef = AutomationId`); manifest fan-out + survey for the run-lifecycle/dispatch slice. **No Doc 16 dependency, no D2 dependency.**

**M7.2b — Action-model contract freeze — Doc-16-SHAPED (Lock-gated).**
Scope: the three beats Doc 16 §7.2 shapes into M7.2's run model — (a) the **computed-parameter-resolution semantics** wired into the M7.2a `initiateRun` seam (Doc 16 §3.2); (b) the **run-coupled reliability terminal-state contract** (Doc 16 §3.4: deterministic terminal + recorded reason on action-failure / unavailable-target / fail-closed-read, reusing AMD-92 `failureReason`/`abortReason` + AMD-90 no-retry, no autonomous re-dispatch); (c) the **D2/REC-162 disposition** (the action model's stance on guarded bounded re-issue). **Gated on Doc 16 Locked + D2/REC-162 ruled.**
Done-when: Doc 16 C-SA-5 degradation tests (inject action-failure/unavailable-target/fail-closed-read → terminal `RunStatus` + populated reason + emitted event; assert **no re-dispatch**); computed-value resolution-at-run-init determinism + replay tests; the D2 disposition test-pinned per Nick's ruling.

This partition isolates the contract *freeze* to M7.2b, so the bulk of M7.2 (M7.2a) can proceed without waiting on Doc 16 — directly honoring "do not freeze M7.2's action-model contract before Doc 16 Locks."

### B-2 — M7.3 scope (UNAFFECTED by Doc 16; depends on M7.2a)

`PendingCommandLedger` — §3.11.2 FSM (`PendingStatus` 5 states), `Expectation` correlation → `state_confirmed`, deadline/timeout semantics, `CommandIdempotency` + EXPIRED-on-restart, **coalescing DISABLED** (correctness pin), projection handlers as separate registrations on the existing `DispatchingProjectionAdvancer` (DQ-3, decided); the ledger event slice rides the manifest fan-out + survey. Done-when: ledger FSM + timeout + idempotency contract tests GREEN; W1/W8 restart/EXPIRED kill-tests GREEN; transport-ack ≠ CONFIRMED test.
**Doc 16 confirms M7.3 UNAFFECTED** (§7.2: mints no event type, changes no ledger state machine; D2/REC-162 touches M7.3 only if folded into the ledger — it is not). **Dependency: M7.2a** (specifically `CommandDispatchService` — the ledger tracks commands the dispatch path issues). Sized at ~1–2 pieces; P1 passes. NOT Lock-gated.

### B-3 — The Doc 16 review→Lock prerequisite + its sequencing

**Doc 16 is review-ready.** Sixteen substantive sections (§0–§16 of DESIGN_DOC_TEMPLATE), the mandatory M7-contract-impact section present (§7.2) and consistent with the landed M7.1 reality, all five anti-requirements explicitly held (no DSL — SP1/§3.2; no engine retry — SP3/§3.4/AMD-90-INV-01; no destructive forced migration — §6.1/AMD-93; never lead with commodity encryption — §12; local-first inviolate — §3.6/INV-LF-02), and §15 carries five open questions all marked **NON-BLOCKING** (Q2 AX-7 versioning + Q5 D2/REC-162 flagged as escalations, neither a Doc-16-Lock gate).

**Recommendation: dispatch the Doc 16 DOCS second-opinion review as its own fresh DOCS session** (review separated from authoring, per discipline) — NOT folded into a Coder dispatch. Sequence: **Doc 16 DOCS review → fold edits → Nick ratifies → Lock.** This runs in **parallel** with the Coder lane (it does not consume a Coder slot). **The Lock is the hard prerequisite for M7.2b** (the action-model freeze) and is the Phase-1 deliverable of the superiority lane.

### B-4 — M7.2-vs-app-bootstrap sequencing (one Coder; RULED 2026-06-19)

**RULED (Nick, 2026-06-19) — see Rulings R1: app-bootstrap AB-3 takes the next Coder slot.** Caveat to carry into the AB-3 instruction: **AB-3 scope must resolve the device-model registry dependency up front** (fold minimal Entity/Device/Area production registries, or sequence that device-model slice just ahead — never a silent block). **M7.2a is the explicit fallback** only if AB-3 registry-prep stalls and the Coder slot would otherwise idle.

**Recommendation (ratified): app-bootstrap AB-3 takes the next Coder slot.** Recommended Coder order: **AB-3 → AB-1 + AB-2 + AB-4 (the Seam-1 go-live) → M7.2a → [by now Doc 16 Locked + D2 ruled] → M7.2b → M7.3**, with the Doc 16 DOCS review running in parallel throughout.

Why app-bootstrap first:
1. **Existential runnability.** `main()` is a one-line stub — the crypto is inert and the HTTP surface unexposed. Until app-bootstrap lands, **nothing runs** — not M7.1, not M7.2. This is the highest-leverage lane.
2. **AB-3 is the substrate both M7 pieces defer into.** M7.1's deferred composition-root wiring AND M7.2's eventual wiring both land in AB-3 (I2). Building AB-3 first unblocks actually running the automation engine.
3. **All app-bootstrap decision gates are RULED** (A1 loopback-default · A2 token issuance · A3 fail-closed + degrade-seam · A4 rotate-DEK + reserve-tag). Residual is mechanical only (CC-1 confirm-gate · R-γ version-policy · AMD-94 ratify); AB-3 (lifecycle substrate) carries no decision gate and issues first.
4. **M7.2b is hard-blocked anyway** on Doc 16 Lock + D2 — so the engine cannot fully proceed regardless, while the Doc 16 review→Lock matures in parallel.

**P6 non-Core floor:** the Doc 16 DOCS review (a non-Core/design lane) is non-preemptable and must not be starved by the Coder lane; no website/distribution lane is competing for the Coder slot this window, so P6 is not otherwise binding. **Option for Nick** (the sequencing is his call): because M7.2a is baseline-buildable-now with no decision gate, it could interleave between AB-3 and the AB-1+2+4 Seam-1 event if he wants engine progress sooner — but I recommend completing the runnability unlock (Seam-1) before turning the Coder to M7.2a.

### B-5 — Route the M7.1 substrate gaps (one-line owner each)

- **slug-tombstone** (`SlugSelector` current-only; `automation_slug_redirect` event minted but dormant) → **future identity/device-model WU** (slug-history/tombstone substrate). _Owner: device-model/identity._
- **first-class `Area` slug** (`Area` keys on name; no slug) → **device-model AMD-44 Stage-2.** _Owner: device-model._
- **`Availability` asleep-vs-dead granularity** (`ReachabilityTrigger` false-alarm risk) → **integration/device-model per R-δ AX-8** (also the deferred E2 reachability vector). _Owner: integration-runtime/device-model._

Recorded so they are not forgotten; each is a forward consuming-WU input, none blocks M7.2.

### B-6 — M7.2 entry-gate

| # | Gate | Owner | Status |
|---|---|---|---|
| 1 | **Doc 16 Locked** (gates the **M7.2b action-model freeze** only) | DOCS review → Nick ratify | **OPEN** — Doc 16 is committed-as-DRAFT (`32afb3f`); review→Lock pending (B-3) |
| 2 | **D2/REC-162 disposition** (gates M7.2b) | **Nick** (at M7.2b, post-Doc-16-Lock) | **RULED 2026-06-19** — keep **REC-162 anti-retry** as default; the action-model disposition is decided **at M7.2b** (not now). M7.2-scoping fact-check (not a flip): confirm the *verification* half is already satisfied by `Expectation` + AMD-90. So row 2 is no longer an OPEN decision gate — it is a deferred-to-M7.2b ruling. |
| 3 | M7.1 WUCP Phase 2 complete | PM | **CLOSED** — verified in Part A |
| 4 | No unresolved deferred build gates | PM/Nick | **CLOSED** — M7.1 gate RESOLVED GREEN (`beb4bc3`, 149 tasks) |
| 5 | C3 cascade-governance doc-fix | — | **CLOSED** — landed `03f16dc` |
| 6 | Construction-site sweep + carry-pins (type-residency/FLATTEN; manifest fan-out + consumer/pin survey incl. publish-count pins; AMD-52 codec; C8 stamping; §4c Clock) | PM | **per-instruction** — built into the M7.2a/M7.2b instruction at issue |
| 7 | M7.1 behavioral-default carry-items folded (Doc 07 §3.8 condition clarification; `EventTrigger.payloadFilters`; `entityRef` flattening) | PM | **tracked** — fold into the M7.2a instruction |
| 8 | M7.2 builds against injected deps (I2); wiring → AB-3 | PM/Coder | **confirmed** — not a build-gate; the wiring is AB-3's deliverable |

**Decision: M7.2 is NOT dispatched this session.** The brief's dispatch condition ("Doc 16 Locked + D2 ruled") is not met — gates 1 and 2 are OPEN. **M7.2a** (baseline) is unblocked on contracts and is issuable subject only to the Coder-slot sequencing call (B-4 recommends app-bootstrap first); **M7.2b** is hard-blocked on gates 1+2. Per the done-when, the owner-tagged gate list above is the output; no instruction is dispatched.

---

## Escalations to Nick (do not decide unilaterally)

1. **The sequencing call (B-4) — ✅ RULED 2026-06-19: app-bootstrap AB-3 next Coder slot** (then AB-1+2+4 Seam-1; Doc 16 review→Lock in parallel; then M7.2a → M7.2b → M7.3). Carry into the AB-3 instruction: resolve the device-model registry dependency up front (fold minimal Entity/Device/Area registries or sequence the device-model slice just ahead). M7.2a = explicit fallback only if AB-3 prep stalls. See Rulings R1.
2. **D2/REC-162 disposition + timing (I3) — ✅ RULED 2026-06-19: keep REC-162 anti-retry as the default; decide the action-model disposition AT M7.2b** (post-Doc-16-Lock; remediation stays ledger-signal-driven at M8.2, above the transport). At M7.2 scoping, do the cheap fact-check (not a flip): confirm the *verification* half ("did the device reach the commanded state?") is already satisfied by `Expectation` + AMD-90 (R-δ judged it likely is). Any reopen of REC-162 enters via a **formal AMD** that re-sequences M7.2b — never silent. See Rulings R2.
3. **Contract-reshape watch (none triggered).** This plan triggers no AMD/supersession; Doc 16 reshapes nothing and M7.2 is forward-shaped. **If** the Doc 16 DOCS review or M7.2b authoring surfaces a genuine contract change (e.g., Doc 16 §15-Q1: a computed-condition that needs a *new* `ConditionDefinition` permit — an AMD-89-class change that would re-sequence M7.1), it moves through the formal AMD pipeline with explicit re-sequencing — never silent.
4. **Carry (charter-adjacent).** (a) **AX-7 component versioning/deprecation policy** (Doc 16 §15-Q2) — must be set before M7.2 ships user-authored components. (b) **AB-3 lifecycle API-shape call** — does `main()` construct `HomeSynapseCore` directly, or does `SystemLifecycleManager` wrap it? Pin at AB-3 instruction authoring.
5. **Flag (input to app-bootstrap sizing).** AB-3's composition-root wiring may pull in **device-model breadth** — the production Entity/Device/Area **registry impls may not exist yet** (AMD-44 Floor/EntityRole, Research-8 REC-23–30), distinct from `ConfigurationService` (exists, needs only wiring). A real input to app-bootstrap's true size/sequencing; not a blocker for the M7.2a core build.

## Anti-requirements (bind the whole plan)
No templating DSL · **no engine retry unless Nick reopens REC-162 (D2) explicitly** · no destructive forced migration · never lead with commodity encryption · local-first inviolate. **M7.2's action-model contract does not freeze before Doc 16 Locks** (isolated to M7.2b). Locked design docs (07, 15, and Doc 16 once Locked) move only via the formal re-open→review→ratify pipeline. The `core→config` module edge is banned — config wiring rides the composition root (app-bootstrap), never a `requires config` in a core module.
