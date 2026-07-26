<!--
file: context/audits/2026-07-26_FE-VERDICT-2_lane_return.md
purpose: Lane return — FE-VERDICT-2 (the honest-verdict rendering lane), dispatched via the 2026-07-26 v38 lane session prompt (v38 charge 4). The ONE spine artifact this lane writes.
audience: the PM hub (two-layer audit); Nick (commit + push — the return orders NO commit).
state-type: lane return (write-isolated: web-ui/dashboard/ + this file ONLY).
status: DELIVERED 2026-07-26. Gate: npm run verify GREEN in-session (cloud container); the gate of record remains Nick's push/CI.
baseline: core `da11f46` stated by the dispatch (SKIP-VIS ON MAIN, audit ACCEPT, NOT yet deployed to the Pi); the dashboard tree consumed = the device working tree at staging time (the dependabot-bumped lockfile in place; see §4 for the md5-verified lockfile identity). No core Java, bench, or other hivemind file read-modified — write-isolation held.
-->

# FRONTEND LANE RETURN — FE-VERDICT-2: the honest-verdict rendering (v1.1.2 consumption · five-modes-distinct · G2) — 2026-07-26

## 0. Preflight (run at session start, before any write)

```
FRONTEND FRESHNESS PREFLIGHT — 2026-07-26
Check 1 (snapshot ↔ lane state):     PASS  (v38 beat 5: SKIP-VIS ON MAIN da11f46, audit ACCEPT, NOT deployed —
                                            "landed-not-deployed" per the FE brief baseline update; MODULE_CONTEXT
                                            2026-07-19 beat consistent)
Check 2 (contract version):          STALE (EXPECTED — this lane's charge: freeze doc stamps v1.1.2 [amended
                                            2026-07-26, hub-owned], client mirror was v1.1.1 → folded this
                                            session under the STALE protocol's clean-fold allowance)
Check 3 (Doc-13 currency / stack):   PASS  (Locked stack unchanged; WS-superseded holds; 100 KB budget stands)
Check 4 (module truth populated):    PASS
Check 5 (B-class mock vs real):      PASS  (A1–A5 + the B3 hero four REAL on the deployed surface; B1/B2 mocked;
                                            the THREE v1.1.2 additive keys are LANDED-ON-MAIN but NOT DEPLOYED →
                                            MOCK-ONLY for this lane, per the dispatch's law-(c) framing)
Check 6 (brand-source / name-light): PASS  (Architecture C RATIFIED; R-1 HELD until G-2 — name-light fully in
                                            force; red retired to the error register; §3a ALL-USERS/CVD mandate
                                            binding on all color work)
Check 7 (dual skill-mirror):         PASS  (all 7 files size-identical source↔mirror: 32680/7680/10001/7778/
                                            7301/11063/9683 — the v1.5 mirror sync has run)
Check 8 (source round-trip):         PASS  (the five-modes signature table, the wire-key casing, the DP-4 GO
                                            state, and every token hex re-read at source this session; citations §5)
Aggregate: STALE (Check-2 only, the expected class — the fold IS the WU) → proceeded under the clean-fold rule.
```

**DP-4 gate state consumed: GO.** Ground truth, three independent sources read this session: the freeze doc's v1.1.2 amendment notes ("landed 2026-07-26 (SKIP-VIS, DP-4 GO)"), the Coder's 2026-07-26 cross-agent note item 2 ("DP-4 executed GO — `settled` shipped: ActionView 8th component + wire key"), and PROJECT_SNAPSHOT v38 beat 4 ("DP-4 GO — ActionView 6→8; the Q1b `settled` formula verbatim"). Consequence: the mirror/mocks carry `settled`; consumption keys on the FIELD where present with the client-side derivation (identical formula) as the pre-v1.1.2 fallback — so the §5 sequencing rule's "note which branch you shipped" answer is: **the GO branch, field-first, with the derivation retained as graceful degrade** (it is a no-op difference by construction, since the formula is the same).

## 1. Summary

The five honest failure modes now render DISTINCT, never collapsed — each with its own label + glyph + tone, at AA in both themes, with color reinforcing and never carrying the distinction alone. `verdicts.actionVerdict()` classifies every causal-chain action from the ruled v1.1.2 `(outcome, resultOutcome, reason)` signature: dispatched-and-timed-out ("Sent — no reply", clock glyph, calm amber) · superseded-same-attribute ("Replaced", swap glyph, neutral — an intent change, never a failure, in both its primary and timed-out variants) · acked-then-silent-forever ("Accepted, never confirmed", ack-then-dots glyph, calm amber, the recorded zigbee reason shown VERBATIM) · held-DISPATCHED ("Sent — not settled yet", arrow glyph, dashed PROVISIONAL pill — the §5.9 register, with the provisionality carried in the label text itself, never styling alone) · settled-FAILED (✕ glyph, error register, with the ten-value sub-label where the disposition is known). D-4 is retired: the first-class `resultOutcome` wins wherever present; `classifyRecordedReason` recovery survives only for pre-v1.1.2 payloads, including the variable zigbee reasons it could never classify — those now render honestly via the field. The silent-skip marker is consumed (`noCommandsIssued` → "Ran, but sent nothing" on the why-not surface; a do-nothing run never reads as clean success anywhere). G2's availability tile renders the honest states with the "not a live connection test" disclosure, honest UNKNOWN-at-boot as its own row, and evidence-with-age one click away. Four light/dark token values were corrected mode-paired after this session's contrast computation reproduced the brand program's light-mode failure class inside the dashboard's own palette. The full gate ran GREEN twice, the second time on a pristine `npm ci` from the dependabot-bumped lockfile — the deps watch closes on §4's evidence.

## 2. Files (the §10 pre-commit change-set audit — EXACT counts)

**21 paths total. 20 under `homesynapse-core/web-ui/dashboard/` (20 M + 0 A) + this return file (1 A under `nexsys-hivemind/`). Nothing else.** No runtime state, build output, secrets, or caches in the set (`dist/` + `node_modules/` were produced only in the session's cloud container and never written to the device; the screenshot PNGs live only in the launch conversation, not on disk — §6). `package.json`/`package-lock.json` are NOT in the set (md5-verified untouched — §4).

Modified (20):
1.  `src/lib/api/contract.ts` — CONTRACT_VERSION → `v1.1.2-2026-07-26`; `CausalAction` + optional `resultOutcome`/`settled` (v1.1.2 additive; optional ONLY because the deployed surface predates the landing — absence = lawful pre-v1.1.2 payload); `NonFiringExplanation` + optional `noCommandsIssued?: true | null`; the DP-3 VALUE-correction + interim-caveat annotations on `triggeredAt`/`lastEvaluation.at`.
2.  `src/lib/api/shapes.ts` — presence-validated additive keys on B3:causalChain actions (`resultOutcome` string|null; `settled` boolean) and B3:nonFiring (`noCommandsIssued` must be `true` or `null` when present — **false on the wire FAILS**, the never-false idiom pinned); absence lawful.
3.  `src/lib/api/contract.test.ts` — version pin → v1.1.2; +8 tests: additive-key acceptance/rejection, pre-v1.1.2 absence lawful, never-false pin, the five-modes scenario's row-exact wire signatures + pairwise distinctness + `triggeredAt ≡ matchedAt`, the pre-v1.1.2 scenario carries NO v1.1.2 keys, the field-evidence DP-2 truth.
4.  `src/lib/verdicts.ts` — THE FIVE-MODES LAYER: `actionVerdict()` (mode classification, first-class-field-first with recovery fallback), `isActionSettled()` (the core-identical Q1b derivation; field wins), `MODE_GLYPHS` (a distinct SVG shape per mode), `ActionVerdict`/`ActionMode` types. Prior exports unchanged.
5.  `src/lib/verdicts.test.ts` — +17 tests in three new describes: the five modes pairwise distinct on mode AND label AND glyph, per-mode row-exact locks (superseded never error/warn and settled; held provisional with "not settled" in the label text; SD-7 conservative unknown-string), the settled derivation ≡ the core formula + field-wins, D-4-retirement locks (field beats reason; recovery only pre-v1.1.2; no-guessing unchanged).
6.  `src/components/StatusPill.tsx` — optional `glyph` path override (per-verdict distinct shapes) + `provisional` variant; default per-tone glyphs unchanged.
7.  `src/components/StatusPill.module.css` — the `.provisional` dashed-outline style (calm; reinforces the label text, never the sole signal).
8.  `src/components/CausalChain.tsx` — actions render via `actionVerdict()` (five modes distinct; provisional pills; per-mode calm help); "Recorded outcome" disclosure shows the raw `resultOutcome` (with a recovered-provenance note on pre-v1.1.2 payloads); terminal line carries "— N outcome(s) have not settled yet" while any action is provisional (§5.9).
9.  `src/lib/format.ts` — `availabilityMeta` gains the honesty `help` strings (AVAILABLE = concluded-from-reports, never a live-contact claim; UNAVAILABLE = evidence + recheck cadence; UNKNOWN relabeled "Not determined yet", normal-not-fault).
10. `src/lib/format.test.ts` — +3 G2 honesty copy locks (never "online"/live-contact on AVAILABLE; evidence+cadence on UNAVAILABLE; honest-normal UNKNOWN).
11. `src/views/WhyNotView.tsx` — `noCommandsIssued === true` → the "Ran, but sent nothing" verdict pill + "See the run that sent no commands →" link; the DP-B2 ran-fine disambiguation retained for pre-v1.1.2 payloads.
12. `src/views/OverviewView.tsx` — G2: the availability tile renders Available / Offline / **Not determined yet** (honest UNKNOWN as its own row, previously silently absorbed) / Stale + the "Counts reflect each device's last report — not a live connection test" line; "Online" retired from the tile (it was a live-contact claim); run rows use `runName()` (the null-name class no longer renders a blank).
13. `src/views/DevicesView.tsx` — availability pills (list + drawer) carry the honesty `help` as their title.
14. `src/lib/api/mock/mockData.ts` — default fixtures extended to the ruled v1.1.2 shape (`resultOutcome`/`settled` on all four chains; `noCommandsIssued: null` on all three non-firing), each block headed MOCK-pending-the-SKIP-VIS-deploy.
15. `src/lib/api/mock/scenarios.ts` — `makeAction`/`makeNonFiring` gain ruled-shape defaults (explicit-undefined strips keys for pre-v1.1.2 payloads); NEW `five-modes` scenario (the ruled wire: one chain, the five signature rows + a confirmed baseline, one provisional action, `triggeredAt ≡ matchedAt` exactly); `verdict-vocabulary` retained as the labeled PRE-v1.1.2 wire exhibit (the recovery path stays exercised until the deploy); `field-evidence` non-firing updated to the landed DP-2 truth (ACTED_BUT_UNCONFIRMED + `noCommandsIssued: true` + the frozen "issued no device commands" sentence — the composed-lie exhibit retired); e5 scenario's identify/superseded actions carry their ruled `resultOutcome`, and the live-flip CT action's `settled` flips with it.
16. `src/a11y.test.tsx` — +1 axe test: the five-modes chain (distinct glyphs + a provisional pill) has no violations.
17. `src/styles/tokens/tokens.dtcg.json` — the four mode-paired AA corrections (§7): light `ok500` #1a8f4c→**#157a40**, light `warn500` #9a6700→**#7f5500**, light `info500` {accent.500}→**{accent.600}**, dark `textMuted` {neutral.500}→**#7e8998**; each with the computed before/after ratios in its $description.
18. `src/styles/tokens.css` — REGENERATED from the source via `npm run tokens` (never hand-edited; `tokens:check` green).
19. `scripts/contract-check.mjs` — EXPECTED_VERSION → `v1.1.2-2026-07-26` + the amendment note.
20. `MODULE_CONTEXT.md` — the 2026-07-26 beat + the Design-Doc-Reference contract line updated to the v1.1.2 stamp.

Added, spine (1):
21. `nexsys-hivemind/context/audits/2026-07-26_FE-VERDICT-2_lane_return.md` — this file.

**Sweep-guard:** a fresh lock-free porcelain should show exactly these 21 paths (20 in core + 1 in hivemind). `package.json` and `package-lock.json` must NOT appear (md5-identical to the staged originals — §4; a temporary `playwright` install for screenshots used `--no-save` and node_modules was restored with a final pristine `npm ci` before the closing gate run). Commit staging by explicit path list (never `-A`), core and hivemind as separate commits per standing practice.

## 3. Gate result

**GREEN in-session, run twice** — the second (closing) run on a pristine `npm ci` tree: `npm run verify` (Node 22.22.2 / npm 10.9.7, cloud container) — tokens:check ✓ · lint ✓ · typecheck ✓ · test **116/116 (6 files)** ✓ (includes the axe a11y suite + the new five-modes axe case) · build ✓ · bundle **61.6 KB / 100 KB** (38.4 KB headroom) ✓ · contract-check **11 endpoints, v1.1.2-2026-07-26** ✓. Per doctrine, the lane's local green is NOT the gate of record — Nick's push through `frontend.yml` CI is. (Env note: esbuild ran native cleanly; no wasm override needed or committed.)

## 4. THE DEPS-WATCH EVIDENCE (the standing watch item closes here)

**`npm ci` against the dependabot-bumped lockfile: CLEAN — 330 packages added, 331 audited, zero errors; the BASELINE (unmodified) tree then built and tested GREEN on that lockfile: 86/86 tests, build ✓, bundle 59.9 KB / 100 KB ✓.** Method: the staged pristine dashboard tree (byte-identical to the device working tree) was copied untouched, `npm ci` + `npm run build` + `check-bundle-size` + `npm run test` run on it — proving the dependabot merges themselves break nothing, independent of this lane's changes. This lane's tree then re-ran `npm ci` (pristine) + the full verify: 116/116. Lockfile identity: `package-lock.json` md5 `d6f5965d80cffe4cef1e95140f96b072` and `package.json` md5 `82f77a14bb577ecc4171f853ec5515be`, identical before/after the session — neither file modified. Bundle delta attribution: baseline 59.9 KB → this lane 61.6 KB (+1.7 KB gzipped for the five-modes layer + tests + copy). (Note for the hub's ledger: the 2026-07-19 return quoted "35.1 KB" — that figure matches the JS+CSS subtotal; the check script's own total, which includes the ~24.8 KB self-hosted font, was already ~60 KB then. No accounting change occurred; both trees measured here with the same script.)

## 5. Evidence (re-verified at source this session)

- **The five-modes signature table consumed row-exact:** `context/instructions/2026-07-26_SKIP-VIS_explanation-honesty_coding-instruction.md` DP-1 (the table + "One test (`explainRun_fiveFailureModesDistinct`) … pairwise distinct AND each equals its row") — mirrored in the `five-modes` scenario + pinned client-side (contract.test.ts).
- **DP-4 GO + the Q1b formula verbatim:** the instruction's DP-4 (`settled = !(outcome == DISPATCHED && (resultOutcome == null || "acknowledged".equals(resultOutcome)))`) — `isActionSettled()` implements it verbatim (verdicts.test locks bare/acked-provisional, superseded-settled, field-wins).
- **Wire casing read at the target endpoints (law (b)):** the instruction's wire deltas — `resultOutcome`/`settled` appended after `reason` in the actions map; `noCommandsIssued` after `lastEvaluation` — camelCase like every sibling key; mocks append in the same order.
- **The DP-2 frozen sentence:** the instruction's behavioral contract, explanation exactly `"Automation '<name>' fired, but issued no device commands — …"` — carried verbatim in the field-evidence mock; the "fired and confirmed" absence is test-pinned.
- **never-false `noCommandsIssued`:** the instruction ("nullable Boolean … `true`/`null`") + the Coder's cross-agent note item 3 ("JSON null otherwise, never false") — validator FAILS a false.
- **§5.1/§5.3/§5.9 exhibits:** `context/handoff/2026-07-25_rosonway-topology-move_I3b_bench-session-report.md` — the five-command exhibit (the `five-modes` scenario mirrors its commands incl. the verbatim `"DefaultResponse SUCCESS +90 ms, then no report, ever"`), `staleAfter: null` + 4h35m-old `lastReported` behind AVAILABLE (the tile's honesty line), the post-COMPLETED outcome mutation (the provisional register).
- **The interim triggeredAt caveat honored:** skill §4d + the freeze doc's v1.1.2 VALUE note — this client only DISPLAYS `triggeredAt`; no ordering/age logic was added anywhere; the mirror annotation warns future consumers; the corrected `≡ matchedAt` semantics are carried by the mock and pinned.
- **Brand/WCAG sources:** `context/assessments/2026-07-22_brand-program_lane_return.md` §3 + Addendum 1 (the light-mode failure finding; "the WCAG finding routes … as FE-VERDICT-2 input"), `context/strategy/brand-program/2026-07-22_identity-system_exploration.md` §3/§3a (the mode-paired discipline + the ALL-USERS/CVD mandate) — applied to the dashboard's own token layer (§7; D-1 below).

## 6. Per-mode visual evidence, BOTH themes

Durable, reproducible refs (the mock is deterministic — these render identically for the auditor): with `npm run dev`, authenticate with any token, then
- **the five modes:** `/dashboard/?scenario=five-modes#/explain/run/run_fm_all` — all five pills + the confirmed baseline + the provisional dashed pill + the "— one outcome has not settled yet" terminal line;
- **the silent-skip marker:** `/dashboard/?scenario=field-evidence#/explain/why-not/auto_fe` — "Ran, but sent nothing" + the frozen sentence + the run link;
- **G2, the availability tile:** `/dashboard/?scenario=field-evidence#/overview` — Available 6 of 8 / Offline 1 / Not determined yet 1 / Stale 2 + the not-a-live-test line;
- **the pre-v1.1.2 degrade path:** `/dashboard/?scenario=verdict-vocabulary#/explain/run/run_vv_superseded` — recovery still renders the flattened wire calmly.
Theme switch: the in-app toggle (or `localStorage hs-theme`). Eight full-page screenshots (the four surfaces × dark/light, captured this session via headless Chromium at 1180×900@2x) were delivered into the launch conversation for Nick/the hub — they are deliberately NOT written into either repo (write-isolation; the census stays 21). The axe structural suite covers the five-modes chain in `npm test`; keyboard reachability on every new/changed surface rides native elements only (links, `<details>/<summary>` disclosures, the existing toggle) — no new custom interactive widget was introduced.

## 7. The AA numbers (computed this session, WCAG 2.x relative-luminance; pill text is 11–12 px ⇒ the 4.5:1 normal-text bar applies)

**The finding:** the dashboard's own light theme reproduced the brand program's failure class — before this lane, light `ok500`/`warn500`/`info500` on their pill fills read **3.65:1 / 4.33:1 / 4.23:1** (all below AA at pill size), and dark `textMuted` read **3.84:1** on the dark surface. Corrected mode-paired (same hue identity; the info correction stays on the existing accent ramp — no new hue minted):

| Pair (pill text on pill fill, + key surfaces) | LIGHT before → after | DARK (unchanged) |
|---|---|---|
| ok500 on okBg | 3.65:1 → **4.76:1 PASS** (#157a40; 5.40:1 on white) | 7.96:1 PASS |
| warn500 on warnBg (the honest amber) | 4.33:1 → **5.84:1 PASS** (#7f5500; 6.56:1 on white) | 7.92:1 PASS |
| error500 on errorBg | **4.64:1 PASS** (unchanged) | 6.97:1 PASS |
| info500 on infoBg (the provisional/in-flight tone) | 4.23:1 → **6.04:1 PASS** (accent.600) | 7.47:1 PASS |
| unknown500 on unknownBg | **5.17:1 PASS** (unchanged) | 7.24:1 PASS |
| neutral (textSecondary on surfaceSunk) | **5.89:1 PASS** (unchanged) | 5.62:1 PASS |
| provisional pill text on surface (dashed variant, transparent fill) | **6.79:1 PASS** (info on white) | 8.04:1 PASS |
| textMuted on surface (the tile note, evidence lines) | **4.55:1 PASS** (unchanged) | 3.84:1 → **4.92:1 PASS** (#7e8998; 5.37:1 on bg) |

The CausalChain step markers reuse the same tone-on-toneBg pairs (13 px semibold) — covered by the rows above. **§3a CVD check (luminance-separation leg):** the corrected LIGHT state triad separates (ok 0.145 / warn 0.110 / error 0.144 — ok-vs-error rides hue+shape as always; every pair also differs by label + glyph). **Observation for the token-authoring session (not fixed here — brand-level):** the DARK ok/warn pair carries near-zero luminance separation (0.4955 vs 0.4895) — under red-green CVD those two hues converge with little luminance help; the structural guarantee (distinct label + glyph, always present) holds, but per the §3a mandate the dark ramp deserves a luminance-separated retune when the post-G-2 token-authoring session runs. Flagged, not improvised.

## 8. Law-(c) FLAGS (every mock-consuming surface; the discipline: mocked to the RULED shape, nothing invented beyond it)

- **FLAG-1 — `resultOutcome`/`settled` are MOCK-ONLY until the deploy.** Consuming surfaces: `CausalChain.tsx` (via `actionVerdict`), the `five-modes` scenario, the default `mockData` chains, the e5 scenario's ruled-key actions. The LIVE deployed surface serves pre-v1.1.2 payloads until the SKIP-VIS deploy completes; on those, consumption degrades to exactly the pre-existing behavior (recovery + derivation). Swap-to-live = zero code: the keys arrive and the field-first paths engage endpoint-by-endpoint.
- **FLAG-2 — `noCommandsIssued` is MOCK-ONLY until the deploy.** Consuming surfaces: `WhyNotView.tsx`, the `field-evidence` scenario. Pre-v1.1.2 payloads keep the DP-B2 ran-fine disambiguation with its honest run-page caveat.
- **FLAG-3 — the DP-3 VALUE corrections are represented in mocks only** (`triggeredAt ≡ matchedAt` in the `five-modes` scenario, pinned). On the live pre-deploy wire `triggeredAt` remains understated by `durationMs` — this client displays it and builds nothing on it (the standing interim rule, which the deploy retires).
- **FLAG-4 — G2's live half could NOT run from this session** (the recorded D-2 environment class, 2026-07-19: the cloud container has no route to the Pi's loopback API; unchanged). The tile + drawer were verified against the scenario engine including the rehydrated-AVAILABLE-with-days-old-evidence and honest-UNKNOWN exhibits. The live demo is a two-minute browser action once Nick has the dashboard open against the Pi (any build ≥ the current deployed one — availability needs NO SKIP-VIS delta): Overview → the Devices tile shows the three honest rows + the not-a-live-test line; Devices → any entity → the evidence-with-age line. Requested as the hub's re-status evidence for the G2 ledger row, or fold it into the deploy evening's post-deploy glance.
- **NO unruled shape was built.** The posture surface (GAP-3) and the A1 `lastReported` (GAP-5) remain unbuilt awaiting rulings; nothing in this change-set invents beyond the three ruled keys.

## 9. Decisions / defaults taken (explicit + revisable)

- **D-1 (token corrections stay inside the dashboard's own ramps; the brand-exploration palette NOT imported).** The dispatch pointed at the brand deliverables' corrected mode-paired values; those §3 values are marked EXPLORATION for the post-G-2 token-authoring session and belong to the docs-side brand palette (#3FA6C9-family), which the dashboard has never used. Importing them now would be new brand direction under a HELD R-1 (§5 escalation class + the OUT fence). What this lane took from the brand deliverables is the DISCIPLINE (mode-paired, same-hue, computed AA) and applied it to the dashboard's shipped token layer, where this session's computation found the same failure class. Every corrected value keeps its hue identity; `info500` resolves to an existing primitive (`accent.600`). Revisable in one token edit each if the hub rules otherwise.
- **D-2 (the GO branch, field-first with the core-identical derivation retained).** See §0. The "or"-variants of the table (superseded+timeout ⇒ UNCONFIRMED with timeout text) render as the superseded mode — the intent-change register outranks the timeout register when both apply, matching CORE-P1(b)'s "an intent change is not a failure".
- **D-3 (the pre-v1.1.2 exhibit retained).** `verdict-vocabulary` now labeled "(pre-v1.1.2 wire)" and stripped of the new keys — it keeps the graceful-degrade path exercised and demonstrable until the deploy; retire it (or re-point it at an adapter-strings exhibit) once the fleet serves v1.1.2 everywhere.
- **D-4 (availability label honesty over brevity):** the UNKNOWN pill label is now "Not determined yet" (was "Unknown"); "Online" is retired from the Overview tile in favor of "Available" + the disclosure line. Copy test-locked; revisable on hub ruling.
- **D-5 (mode-5 sub-labels ride the ten-value layer unchanged):** within settled-FAILED, the known-failed dispositions keep their distinct sub-labels, and `timed_out` keeps the prior lane's D-1 calm-amber "No reply" default (hub never overruled it; SD-7's stated residue named only `expired_on_restart`/`invalid`, both honored as-shipped). One hub line re-classes any of these — derivation-only.
- **D-6 (no escalation-triggering new direction taken):** no new brand element, no IA change, no new hero PRESENTATION (the five-mode rendering extends the existing pill/step/tone system with per-verdict glyphs — the same shape-carries-state mechanism StatusPill always used); the provisional dashed variant is a state treatment inside the established component, not a new brand moment. If the hub reads the glyph set as presentation-precedent instead, it is revisable without wire or copy changes.

## 10. Accessibility + stranger test

State never rides color alone: each of the five modes = distinct label text + distinct SVG glyph + tone; the provisional state additionally says "not settled yet" IN the label (the dashed outline only reinforces). All new copy is Register C — calm, no blame, no alarm, no self-reference — centralized in `verdicts.ts`/`format.ts` and test-locked (including "That is a change of intent, not a failure", "an acceptance is not proof", "reported honestly instead of guessed", "not a live connection test", and the §5.9 "this can still settle, and the record updates itself when it does"). Chains remain semantic `<ol>`; disclosures remain native `<details>`; the axe suite (now including the five-modes chain) ran green inside `npm test`; contrast verified numerically in §7 for both themes. Name-light held: zero new hardcoded product-name strings (grep-verified over the change-set).

## 11. Cross-lane notes (FOR THE HUB)

1. **G2 re-status:** the tile + honest states are delivered and evidenced (§6/§8 FLAG-4); the two-minute live glance is the remaining leg — recommend folding it into the deploy evening's post-deploy checks.
2. **The deps watch closes** on §4's evidence (baseline green + lane green on the bumped lockfile; lockfiles untouched).
3. **The dark ok/warn CVD-luminance observation** (§7) routes to the post-G-2 token-authoring session's checklist — brand-level, not improvised here.
4. **Swap-to-live tracking:** when the SKIP-VIS deploy completes, FLAGS 1–3 retire with ZERO frontend code changes (field-first paths engage on arrival); the only optional follow-ups are D-3's exhibit retirement and deleting the pre-v1.1.2 absence-tolerance from the validators once the fleet is uniformly v1.1.2 (a deliberate tightening — one-line each in `shapes.ts`).
5. Standing asks unchanged from the 2026-07-19 return: GAP-3 (posture surface) and GAP-5 (A1 `lastReported` — it would let the DEVICE LIST show evidence-age, not just the drawer; it is now also the cheapest upgrade to G2's tile) remain open candidates.

## 12. Next WU (refuse-to-close)

**FE-LIVE-V112 — the post-deploy live verification pass:** once the SKIP-VIS deploy lands on the Pi, run the dashboard live against it and (a) verify the three additive keys arrive with the mocked shapes byte-for-shape (the FE1_GO_LIVE §0 style), (b) confirm a real superseded/unconfirmed chain renders its mode from the FIELD (watch the "Recorded outcome" disclosure lose its recovery note), (c) capture the G2 live glance for the ledger, (d) retire D-3's exhibit + tighten the validators (§11.4), and (e) fold GAP-5 if ruled. Zero bench dependency; dispatchable the morning after the deploy evening. (If the hub prefers, halves (a)–(c) are small enough to ride the deploy evening itself as a five-minute browser block.)
