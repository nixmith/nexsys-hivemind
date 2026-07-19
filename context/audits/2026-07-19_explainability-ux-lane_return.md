<!--
file: context/audits/2026-07-19_explainability-ux-lane_return.md
purpose: Lane return — explainability-UX lane (the verdict surface), dispatched via the 2026-07-19 refreshed brief (M14 G1 [M] trigger). The ONE spine artifact this lane writes.
audience: the Core/PM hub (two-layer audit); Nick (commit + push).
state-type: lane return (write-isolated).
status: DELIVERED 2026-07-19. Gate: npm run verify GREEN in-session (cloud container); the gate of record remains Nick's push/CI.
baseline: core 554e18c (verified at launch via git rev-parse on-device; clean tree; = the brief's stated baseline; no shift observed in-session).
-->

# FRONTEND LANE RETURN — Explainability UX: the verdict surface — 2026-07-19

## 0. Preflight (run at session start, before any write)

```
FRONTEND FRESHNESS PREFLIGHT — 2026-07-19
Check 1 (snapshot ↔ lane state):     PASS  (v34/beat-2; core 554e18c deployed; MODULE_CONTEXT beat FE-1b consistent)
Check 2 (contract v1.1 currency):    PASS  (freeze doc status FROZEN v1.1.1 2026-07-02; client CONTRACT_VERSION matches)
Check 3 (Doc-13 currency / stack):   PASS  (Locked stack unchanged; WS-superseded holds; 100 KB budget stands)
Check 4 (module truth populated):    PASS
Check 5 (B-class mock vs real):      PASS  (re-derived from api/rest-api source: A1–A5 + the B3 hero four REAL —
                                            List/Get/GetEntityState/Projection/Dlq + ListRuns/GetRunCausalChain/
                                            GetNonFiring/ListAutomations endpoint classes exist; NO events/health
                                            endpoint class exists → B1 /events + B2 /health remain MOCKED)
Check 6 (brand-source / name-light): PASS  (W-11/R-1 unratified — rules at G-2; name-light in force)
Check 7 (dual skill-mirror):         STALE (EXPECTED: source v1.4 2026-07-18 vs loaded mirror v1.3 — the hub already
                                            recorded "Check 9 STALE pending Nick's mirror sync"; v1.4 §4a/§4c were
                                            read from the SOURCE at nexsys-skills/orchestrators/nexsys-frontend/)
Check 8 (source round-trip):         PASS  (every load-bearing fact re-verified at source; citations below)
Aggregate: STALE (Check-7 only, the expected class) → ground-truth + clean folds; proceeded.
```

Vocabulary re-verified at launch per the brief §2: `CommandResultEvent.java` javadoc carries exactly the ten values `acknowledged | rejected | timed_out | invalid | unsupported | handler_error | integration_unavailable | superseded | expired_on_restart | unconfirmed` (and notes the last four incl. `invalid` are DISPOSITIONS the ledger's terminal-match guard skips; adapters may publish additional protocol-specific strings — the UI carries an honest fallback for those).

## 1. Summary

The verdict surface now renders the moat's honest verdicts on the live vocabulary. A dedicated verdict-vocabulary layer (`src/lib/verdicts.ts`) maps all TEN `command_result.outcome` values to distinct, test-locked renderings in the charter's three classes (honest-can't-know / known-failed / deliberately-superseded, + protocol-ack and restart-accounting); the two ledger dispositions erased by `StandardExplanationService`'s flattening are RECOVERED client-side from their deterministic recorded-reason wire strings and rendered calm — an intent change, never a failure. Every §4 field-evidence class renders honestly: the silent-skip do-nothing run never reads as clean success; the prior-instance null-name run gets calm honest copy (never an invented name); availability renders as evidence-with-age (flag + last-heard-from), with UNKNOWN-after-restart calm; DP-B2's "ran fine" NEVER_TRIGGERED is disambiguated by the non-null run id exactly as core's javadoc intends; brightness percent renders only from the DERIVED `brightness_percent` key, never a client rescale. Three new mock scenarios exercise all of it against wire-faithful strings, and the full gate ran GREEN in-session.

## 2. Files (the §10 pre-commit change-set audit — EXACT counts)

**15 paths total. 14 under `homesynapse-core/web-ui/dashboard/` (12 M + 2 A) + this return file (1 A under `nexsys-hivemind/`). Nothing else. Every path maps to a deliverable below; no runtime state, build output, secrets, or caches are in the set (no server was run; no token was minted; `dist/`/`node_modules/` were produced only in the session container, never written to the device).**

Modified (12):
1.  `src/lib/format.ts` — `availabilityEvidence()` (evidence-with-age), `runName()`/`NULL_NAME_NOTE` (null-name class), `brightnessDisplay()` (derived-percent-only), `causalSentence()` do-nothing honesty + null tolerance.
2.  `src/lib/format.test.ts` — locks all of the above (stranger-test copy locks incl. "never rescaled", "nothing was changed", calm-UNKNOWN).
3.  `src/lib/api/contract.ts` — OBSERVED-LIVE-NULLABILITY annotations: `RunSummary.automationName: string | null`, `CausalChain.automationName: string | null`, `CausalTrigger.type: string | null` (each with a drift comment citing the field evidence + this return; see §5 GAP-2 — clarification ask, not a silent divergence).
4.  `src/lib/api/shapes.ts` — `strOrNull()` tolerance for exactly those three fields (absence and wrong types still FAIL).
5.  `src/lib/api/contract.test.ts` — pins the null tolerance to exactly-null (absence fails; non-string fails); validates the null-name fixture end-to-end.
6.  `src/lib/api/mock/scenarios.ts` — three new scenarios: `verdict-vocabulary` (all ten outcomes as they reach today's wire: flattened FAILED + the verbatim ledger disposition strings), `field-evidence` (silent-skip run · null-name run · rehydrated-AVAILABLE with ~2-day-old evidence · honest-UNKNOWN-since-restart · the DP-B2 composed case), `live-fleet` (one entity per deployed class, canonical keys, brightness level 209 + derived 82%).
7.  `src/lib/api/mock/mockData.ts` — name-light fix: the EXTERNAL event summary now templates `BRAND.productName` (was a hardcoded literal).
8.  `src/components/CausalChain.tsx` — disposition-honest action pills (recovered superseded/expired render calm with the recorded reason as provenance under "Recorded reason"); the do-nothing step + honest terminal line ("Finished …, but nothing was changed", warn tone, never clean success); null-name note; null `trigger.type` rendered as "recorded before the current automations", never a blank.
9.  `src/views/RunsView.tsx` — null-name rows render *An earlier automation* (em, with the explanatory title), never a blank cell.
10. `src/views/WhyNotView.tsx` — DP-B2 disambiguation: verdict `NEVER_TRIGGERED` + non-null `lastRelevantRunId` → "It did run" (ok tone) + a link "See that run — including whether anything actually changed →" (the honest bridge to the silent-skip truth on the run page).
11. `src/views/DevicesView.tsx` — availability evidence-with-age line (role="status") in the detail drawer; brightness from the derived key with the raw-level fold; level-honest fallback when no derived percent.
12. `MODULE_CONTEXT.md` — the 2026-07-19 beat + pointers.

Added (2):
13. `src/lib/verdicts.ts` — the vocabulary layer: `resultOutcomeMeta()` (ten distinct verdicts + honest fallback for adapter-specific strings), `classifyRecordedReason()` (deterministic-wire-truth-only recovery), `postureMeta()` (design-ready posture vocabulary — see GAP-3), `isDoNothingRun()`.
14. `src/lib/verdicts.test.ts` — locks: ten distinct labels (zero flattening), superseded never error/warn + "not a failure", honest-can't-know = calm amber, known-failed set = error, ack ≠ confirmation, no-guessing classifier (variable zigbee reasons stay unclassified), posture-is-not-a-verdict, silent-skip detection truth table.

Added, spine (1):
15. `nexsys-hivemind/context/audits/2026-07-19_explainability-ux-lane_return.md` — this file.

**Sweep-guard:** a fresh lock-free porcelain should show exactly these 15 paths (14 in core + 1 in hivemind). `src/styles/tokens.css` regenerated byte-identical during the build and is NOT in the set. Commit staging should be by explicit path list (never `-A`), core and hivemind as separate commits per standing practice.

## 3. Gate result

**GREEN in-session:** `npm ci && npm run verify` in the session's cloud container (Node 22.22.2 / npm 10.9.7) — tokens:check ✓ · lint ✓ · typecheck ✓ · test **86/86 (6 files)** ✓ (includes the axe-core a11y suite) · build ✓ · bundle **35.1 KB gzipped / 100 KB budget** ✓ · contract-check **11 endpoints, v1.1.1-2026-07-02** ✓. Per doctrine, the lane's local green is NOT the gate of record — Nick's push through `frontend.yml` CI is. (Env note: esbuild ran NATIVE cleanly in the cloud container — the §9 esbuild-SIGSEGV class did not manifest; no wasm override was needed and none is committed.)

## 4. Evidence (file:line, all re-verified at source this session)

- **The ten-value vocabulary:** `core/event-model/src/main/java/com/homesynapse/event/CommandResultEvent.java` javadoc `@param outcome` (the M9.4b §4.3 currency block, ~lines 22–27 of the record's doc) — read verbatim on-device.
- **The flattening (named target):** `core/automation/src/main/java/com/homesynapse/automation/StandardExplanationService.java:656` — `isFailure(String)` = anything ≠ `"acknowledged"`; applied at `:634`; FAILED minted at `:647` with `reason = firstNonBlank(failureReason, outcome)`; UNCONFIRMED only from the timeout event at `:651`. Consequence on the wire: `superseded`/`unconfirmed`/`timed_out`/`expired_on_restart` command_results all render `actions[].outcome: FAILED` (matches the §4c field reps).
- **The deterministic recovery strings:** `core/automation/src/main/java/com/homesynapse/automation/StandardPendingCommandLedger.java:912-916` (superseded: `"superseded by a newer command on the same attribute; superseding command event <id>"`) and `:922-924` (expired: `"command was in-flight at restart and is not idempotent"`). `classifyRecordedReason()` matches exactly these + bare outcome tokens — nothing else.
- **Zigbee honest-unconfirmed reasons are VARIABLE** (`integration/integration-zigbee/.../ZigbeeCommandHandler.java:181,206,216,219` publish sites; `disabledReason`/`unconfirmableReason`/`noSurfaceReason` at `:253,:270,:326` are profile-note-driven) — therefore NOT pattern-matched (no guessing); see D-4.
- **DP-B2 / completedVerdict:** `StandardExplanationService.java:275-311` — javadoc states the clean-success case reports `NEVER_TRIGGERED` with a NON-NULL `lastRelevantRunId` and "the UI tells them apart by the non-null run id" — implemented verbatim in WhyNotView.
- **The silent-skip composition:** same `completedVerdict` derives "clean" from `buildActions()` (empty actions[] ⇒ no unconfirmed ⇒ reads as ran-fine) — the do-nothing run's honest story therefore lives on the run page, which is where the UI sends the user.
- **Null-name class:** `StandardExplanationService.toSummary` (`automationName = registry.get(automationId).map(name).orElse(null)`) and `buildTrigger` (`type` from the registry definition, `orElse(null)`).
- **brightness_percent is LIVE:** `core/state-store/src/main/java/com/homesynapse/state/MaterializedStateQueryService.java:113` (`BRIGHTNESS_PERCENT_KEY`), `:240` (Doc 08 §3.5 derivation), `:78/:209` (M9.4b §2.3) — an additive data key INSIDE the A3 attributes map; frozen shape untouched.
- **camelCase wire keys:** per the hub's recorded M7.5a/b precedent (hand-built camelCase maps, shape-test-pinned) — the mirror and mocks stay camelCase; read at the endpoint, never assumed from Doc 09's Jackson snake_case row.
- **No wire path for posture:** grep of `EventTypes.java` for `downgrad` = zero hits; `confirmation_downgraded` exists only as the zigbee WARN/log vocabulary — see GAP-3.
- **B1/B2 still unbuilt:** `api/rest-api/src/main/java/com/homesynapse/api/rest/` contains no events/health endpoint class (find-verified on-device).

## 5. v1.1 contract gaps (verbatim, per the brief §5 — flag, don't improvise; each STOPPED, recorded, built-around)

- **GAP-1 (the load-bearing one):** *The ten-value `command_result.outcome` vocabulary does not flow through any FROZEN v1.1 shape. `causal-chain.actions[].outcome` is the frozen five-value set (`DISPATCHED|CONFIRMED|UNCONFIRMED|FAILED|SKIPPED`), and the raw outcome survives only inside the free-text `reason` (and only when `failureReason` was null, or via the two deterministic ledger strings).* STOPPED on: wire-level distinct rendering of the known-failed subtypes (rejected vs handler_error vs …) when `failureReason` is set, and of zigbee's variable-reason honest-unconfirmed class. **Ask:** additive optional `resultOutcome: string` on the causal-chain action (the raw `command_result.outcome` where one exists) — additive, backward-compatible; pairs with CORE-P1 below.
- **GAP-2:** *The freeze text does not annotate nullability on `RunSummary.automationName`, `CausalChain.automationName`, or `trigger.type`; the LIVE wire serves `null` for prior-instance runs.* The client now tolerates exactly-null (absence/wrong-type still fail) and renders the class honestly. **Ask:** ratify the nullability annotation as a v1.1.2 clarification (or rule the core-side durable-automation-identity fix instead) — the mirror's fold is flagged here precisely so it is a recorded adjudication, not a silent divergence.
- **GAP-3:** *Confirmation POSTURE (`VERIFIED_REPORTS`/`SLEEPY`/`best_effort`, the `confirmation_downgraded` class) has NO wire path — no EventTypes constant, no read endpoint.* The posture vocabulary + calm copy is design-ready in `verdicts.ts` (`postureMeta`, test-locked); NO mock invents a shape for it. **Ask:** rule where posture surfaces (candidate: additive per-entity confirmation block on A2/A3, from the AMD-99 durable registry provenance).
- **GAP-4:** *Silent-skip runs carry no per-target skip record (empty `actions[]`; no marker event).* Rendered honestly from the actionCount-vs-actions[] tell; the real fix is the already-minted SKIP-VIS core WU (skip token + chain rendering + the completedVerdict fix) — this lane endorses its shape and will consume it.
- **GAP-5 (minor, additive):** *A1 entity summaries carry no last-evidence timestamp*, so evidence-with-age renders in the A3-backed detail drawer but the LIST can only show the flag + stale. **Ask (low-friction additive):** optional `lastReported` on the A1 summary.

## 6. Core-side proposals (for the hub to fold into core WUs; exact file:line + needed behavior)

- **CORE-P1 (rides SKIP-VIS or CMD-API adjacency):** `StandardExplanationService.java:617-653` (`deriveOutcome`) + `:656` (`isFailure`) — stop collapsing dispositions into FAILED. Needed behavior: (a) carry the raw `command_result.outcome` on the action view (GAP-1's additive field); (b) `superseded` must not select the FAILED branch (an intent change is not a failure — Nick's beat-5 pin); (c) zigbee's honest-`unconfirmed` command_result should derive UNCONFIRMED (with its recorded reason), not FAILED — today only the timeout event reaches UNCONFIRMED (`:651`).
- **CORE-P2 (the SKIP-VIS completedVerdict fix, already named by the hub):** `StandardExplanationService.java:288-309` — a COMPLETED run with `actionCount>0 / commandCount=0 /` empty derived actions must not report the clean "last fired and confirmed" NEVER_TRIGGERED; needs the skip marker + an honest verdict/explanation (the javadoc's own post-V1 `FIRED_CONFIRMED` additive is the growth path).
- **CORE-P3:** durable automation identity across YAML reloads (kills the null-name class at the root) — already a candidate core row per skill v1.4 §4c; until then GAP-2's annotation stands.
- **CORE-P4:** posture read surface (GAP-3) from the AMD-99 durable provenance.

## 7. Decisions / defaults taken (explicit + revisable)

- **D-1:** `timed_out` classified honest-can't-know (calm amber, "No reply") — not known-failed: a send with no reply proves nothing about whether the device acted. The brief's §3 known-failed list omits `timed_out`; this default realizes that reading. Revisable on hub ruling.
- **D-2:** The live-fleet probe was NOT possible from this session (the device bridge's shell has no network; the Pi's loopback API is unreachable from the cloud container) — the `live-fleet` scenario's attribute keys are SOURCE-DERIVED (W2 handlers' canonical `temperature_c`/`humidity_pct`; `MaterializedStateQueryService`'s `brightness_percent`; the ≥6-entity post-04P class list from the v34 snapshot). **Re-verify payload shapes at the first live run** (`FE1_GO_LIVE.md` §0 style) — flagged, not assumed.
- **D-3:** The exactly-null tolerance (GAP-2) was folded ahead of formal ratification because (a) the brief makes rendering the null-name class an obligation, and (b) a validator that hard-fails the live wire on every prior-instance run would break the dev-runtime drift check on real data. Held to exactly-null; pinned by tests; adjudication requested.
- **D-4:** No pattern-matching of VARIABLE reason text (zigbee profile notes) — those actions keep the FAILED pill with the recorded reason shown verbatim. Honesty over cleverness; full fidelity arrives with GAP-1/CORE-P1.
- **D-5 (identify-class §1 pin, partial):** the immediate honest-UNCONFIRMED rendering for identify-class is fully realized where the wire is deterministic (the e5 scenario + bare-token reasons + the effect-class hint) and degrades to FAILED-pill+verbatim-reason where the wire is variable — the pin's complete realization requires CORE-P1. Never a silent DISABLED bypass is core-side guaranteed (`ZigbeeCommandHandler.java:206` publishes the honest verdict; consumed as-is).
- **D-6:** No escalation-triggering new direction was taken: no new brand element, no IA change, no new hero presentation (all rendering extends the existing pill/step/tone system); the scenario additions follow the established registry pattern.

## 8. Accessibility + stranger test

State is never color-alone: every new verdict renders via StatusPill (tone + SVG shape + text label); the superseded/expired calm classes use the neutral/unknown glyph shapes, distinct from error's ✕. The availability evidence line is a polite `role="status"` region. Chains remain semantic `<ol>`; disclosure stays two-level (`<details>` for "Recorded reason"). The axe suite ran green inside `npm test`. All new copy is Register C (no self-reference, no blame, no alarm), centralized in `format.ts`/`verdicts.ts`, and test-locked — including "That is a change of intent, not a failure", "nothing was changed", and the calm UNKNOWN-after-restart line. Name-light held: zero new hardcoded product-name strings, and one pre-existing hardcode in mock data was tokenized.

## 9. Cross-lane asks (FOR THE HUB)

1. Rule GAP-1 (additive `resultOutcome`) + CORE-P1 — the single highest-leverage fix for the moat's surface.
2. Ratify or supersede GAP-2's nullability annotation (v1.1.2 clarification vs CORE-P3).
3. Rule GAP-3 posture surfacing and GAP-5 (`lastReported` on A1) as additive candidates.
4. SKIP-VIS (already minted): this return adds the lane's consuming-side endorsement + CORE-P2 specifics.
5. The skill mirror sync (Check-7 STALE) remains pending on Nick — already on the hub's record.

## 10. Next WU (refuse-to-close)

**FE-VERDICT-2 — consume the ruled contract deltas:** when the hub rules GAP-1/GAP-2 (and SKIP-VIS lands), swap `classifyRecordedReason` recovery to the first-class `resultOutcome` field endpoint-by-endpoint, render the skip tokens in the chain, and retire D-4's limitation; plus an FE-4-style visual sweep of the three new scenarios in both themes (dark/light AA spot-check on the new calm tones). Zero bench dependency; dispatchable on the next contract ruling.
