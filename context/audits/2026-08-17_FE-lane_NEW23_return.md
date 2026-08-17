<!--
file: context/audits/2026-08-17_FE-lane_NEW23_return.md
purpose: FE-lane return for the NEW-2/NEW-3 + NEW-6/NEW-7 dispatch (error-posture enforcement app-wide · contract-vs-wire nullability corpus-swept · device-detail copy honesty · Activity-nav proposal). First post-gate FE dispatch of the ratified semester program.
audience: the Core/PM mission-control hub (two-layer audit), Nick.
state-type: lane return (files to context/audits/ per the brief; ONE file, uncommitted — the hub stages it).
status: DELIVERED 2026-08-17. Baseline homesynapse-core d26777c (verified at checkout: d26777c601c5acd909d8b6bacd7cd71ccc8fd802, HEAD clean). All work under web-ui/dashboard/. ZERO core-Java changes. Local verify gate GREEN (181/181); frontend.yml on the push remains the CI gate of record. The touched surfaces conclude REPO-COMPLETE, LIVE-VERIFICATION PENDING THE DEPLOY (§8).
-->

# FE Lane Return — NEW-2 / NEW-3 + riders (error posture + nullability)

## §0 Preflight + baseline verification

```
FRONTEND FRESHNESS PREFLIGHT — 2026-08-17 ~20:05 UTC
Check 1 (snapshot ↔ lane state):     PASS  (the v53 beat-6 last-verified chain names THIS brief dispatch-ready; chain summary ↔ brief agree)
Check 2 (contract v1.1 currency):    PASS  (CONTRACT_VERSION v1.1.2-2026-07-26; contract-check green; freeze record re-read at source)
Check 3 (Doc-13 currency / stack):   PASS  (verified at code: Preact 10 + Vite + TS + CSS Modules; 100 KB gate enforced; no WS client anywhere)
Check 4 (module truth populated):    PASS  (MODULE_CONTEXT + FRONTEND_DOCTRINE populated, consistent with src/)
Check 5 (B-class mock vs real):      PASS  (B3 four reads live on the deployed Pi per the G1 instrument record; B1 unbuilt → honest 404; B2 composed A4+A5)
Check 6 (brand-source / name-light): PASS  (G-2 still two-acts-held per the v53 chain; name-light fully in force; no hardcoded name added)
Check 7 (dual skill-mirror):         PASS  (7/7 files sha256-identical, device source vs synced mirror)
Check 8 (source round-trip):         PASS  (every cited shape re-derived at source; see the baseline-identity note below)
Aggregate: PASS
```

**Baseline identity, stronger than required:** the checkout at `d26777c` builds to `dist/assets/index-B9CmxYDm.js` — the SAME hashed bundle name the rehearsal's console error names at the throw site (§4.5: `index-B9CmxYDm.js:1:99808`). The tree this lane starts from IS the deployed incident build, proven by the build system itself. Working tree porcelain at start: clean except a pre-existing untracked `_scratch/` (untouched).

## §1 Summary

NEW-2: `ErrorBoundary` is now mounted at the view-switch level in `app.tsx` — every one of the nine views renders inside it, with a full-route-identity `resetKey`; a render throw in ANY view degrades to the honest render-failure card while the nav, status footer, and poll loop stay alive. The eternal-spinner state is unreachable by construction, and 12 red-first tests prove containment per view plus retry-remount and navigate-away-reset. NEW-3: `contract.ts` now declares `lastEvaluation` object-OR-null (the wire truth, §4.5 of the rehearsal record), both `WhyNotView` dereferences are guarded to render honest absence, the validator checks the field it previously skipped, the mocks carry the real tri-state, and the corpus sweep (§4) enumerated every dereference of a contract-declared-non-nullable field — closing the whole closed-switch-over-a-wire-string crash class (7 formatting maps hardened with the honest `Recorded as "…"` register) with red-first fixtures. Riders: the DX-20 device-detail self-contradiction is dead at the class (one shared parse for prose + row; clock-only stamps date-qualify past 24 h — NEW-6), and the NEW-7 Activity-nav disposition is proposed in §6, hub rules.

**Charge-2 framing, stated so no one misreads the act:** the v1.1 wire contract is FROZEN and the SERVER is its reality. Correcting `contract.ts:350` to declare what the wire actually sends (`lastEvaluation: {…} | null`, observed 2026-08-16, 200 OK, byte-complete body on record) is a CLIENT-TYPE correction toward the frozen truth, not a contract change. Nothing server-side moves; zero core-Java files touched. A freeze-text clarification ask rides §7.

## §2 Changed-file census (exact; all under `web-ui/dashboard/`)

Modified (11):

| # | File | What changed |
|---|---|---|
| 1 | `src/app.tsx` | NEW-2: `ErrorBoundary` mounted around `renderView(route)` inside `AppShell`; `routeKey()` (name + sorted params) as `resetKey`; placement rationale in the comment + §5 |
| 2 | `src/lib/api/contract.ts` | NEW-3: `NonFiringExplanation.lastEvaluation` → `{…} | null` with the observed-live-nullability annotation (the automationName precedent) |
| 3 | `src/lib/api/shapes.ts` | `B3:nonFiring` validator now checks `lastEvaluation` (object-or-null; insides string-or-null) — the field it previously SKIPPED, the omission that let the mock conceal the divergence |
| 4 | `src/views/WhyNotView.tsx` | Both dereferences guarded (`nf.lastEvaluation?.at`); null → the row simply doesn't render; `Last checked` stamp date-qualified (NEW-6) |
| 5 | `src/lib/format.ts` | `parseInstant()` (the ONE parse; never coerces a non-string instant — the seconds-as-ms guard); `clockTimeWithDate()`; `availabilityEvidence` three honest branches (readable age · unreadable stamp · no report); honest open-vocabulary fallbacks on `verdictMeta`, `originMeta`, `outcomeMeta`, `availabilityMeta`, `healthMeta`; `causalSentence` date-qualified |
| 6 | `src/views/HealthView.tsx` | `projectionMeta` honest fallback for an off-vocabulary mode (the health surface must not crash when things are odd) |
| 7 | `src/views/DevicesView.tsx` | `Last reported` → `clockTimeWithDate` (same parse as the prose — DX-20 dead at the class) |
| 8 | `src/views/EventsView.tsx` | Feed timestamps → `clockTimeWithDate` (the feed can span days) |
| 9 | `src/components/CausalChain.tsx` | Trigger-step stamp → `clockTimeWithDate` (a run can be days old) |
| 10 | `src/lib/api/mock/mockData.ts` | `auto_evening_hallway.lastEvaluation` → `null` (the observed live shape — the mock fleet carries the real tri-state) |
| 11 | `src/lib/api/mock/scenarios.ts` | `makeNonFiring`: non-CONDITION_NOT_MET arms now serve `lastEvaluation: null` (live shape), CONDITION_NOT_MET keeps the object arm |

New (5):

| # | File | What it is |
|---|---|---|
| 12 | `src/lib/api/fixtures/wire-2026-08-16-nonfiring.ts` | THE REAL WIRE BODY, verbatim, envelope included — provenance in §5 |
| 13 | `src/app.errorPosture.test.tsx` | NEW-2 red-first suite: 12 tests (10 per-view/per-mode containment + retry-remount + navigate-away-reset) |
| 14 | `src/views/WhyNotView.nullability.test.tsx` | NEW-3 red-first suite: 7 tests over the real fixture + the tri-state arms + the unknown-verdict register |
| 15 | `src/lib/format.wire-nullability.test.ts` | 20 tests: seconds-as-ms guard, date qualification, DX-20 copy, the closed-switch class |
| 16 | `src/views/HealthView.wire-hardening.test.tsx` | 2 tests: off-vocabulary projection mode renders honestly; LIVE preservation pin |

Not touched, deliberately: `MODULE_CONTEXT.md` (hub-owned fold per the core-side convention — suggestion in §7), `ErrorBoundary.tsx` (its documented law needed enforcement, not editing), `feedback.tsx`/`timeAgo` string behavior (DX-22's `Updated X ago` mechanism untouched per the brief — `timeAgo` gained only a non-string type guard whose output for numbers is byte-identical to the old coercion result, `'—'`).

## §3 Test census + red-first evidence

Baseline: 140 tests / 8 files, all green at `d26777c` (re-derived in-session before any edit). Final: **181 tests / 12 files, all green** — 41 new tests. Red-first capture: the four new suites were run against a pristine baseline copy of the tree BEFORE the fixes (two capture rounds; round 2 re-ran `format.wire-nullability` after 4 late-added switch-fallback tests). **28 of 41 red at baseline, 13 green-at-baseline disclosed by name below.**

| Suite | Tests | Red at baseline | Green-at-baseline (disclosed) |
|---|---|---|---|
| `app.errorPosture.test.tsx` | 12 | 11 | 1 — the RunChainView case: its pre-existing inner boundary contains it (the preservation fixture for the reference pattern; kept deliberately) |
| `WhyNotView.nullability.test.tsx` | 7 | 3 | 4 — "validator accepts null" was VACUOUSLY green (the validator skipped the field entirely at baseline — that omission is itself part of the finding; it now exercises the object-or-null arm); 3 object-arm preservation pins |
| `format.wire-nullability.test.ts` | 20 | 13 | 7 — preservation pins (ISO clockTime; timeAgo string behavior; readable-age evidence; the four frozen verdicts/origins; runStatusMeta's pre-existing fallback; unreadable-vs-no-report distinctness, which the old copy passed by accident) |
| `HealthView.wire-hardening.test.tsx` | 2 | 1 | 1 — LIVE-mode preservation pin |

**The baseline failure signatures are the incident, reproduced:**

- Error-posture, every unprotected view: the assertion output shows the exact live pathology — the shell header updates (`Updated just now`) over a body stuck at `Loading…` or a silent blank, no honest card, the raw TypeError uncaught. E.g. OverviewView at baseline: `Recent runs…Loading…Devices…Loading…` — the eternal spinner, in-fixture.
- `clockTime` at baseline: `expected '7:35 AM' to be '—'` — the fed epoch-seconds instant (1755321600.123) read as milliseconds lands in Jan 1970 and formats as a plausible morning time. The rehearsal's arithmetically-proven "9:52 AM" misread class, reproduced exactly.
- `availabilityEvidence` at baseline: produced `"Offline — last heard from —. …"` — DX-20's self-contradiction sentence, verbatim.

Harness disclosure: after the round-1 capture, the "Try again" test's tail was adjusted (raw `.click()` → act-wrapped `fireEvent.click` + a second timer flush) so the retry path settles under fake timers. Its baseline red stood on the EARLIER assertion (`RENDER_ERROR_TITLE` absent), unaffected by the tail change.

## §4 The corpus-sweep enumeration table (charge 2c — arc-discipline 25)

Method: walked `contract.ts` type by type against (a) the wire bodies on record (§4.5 of the rehearsal record; the 2026-07-27 WCAP/chain-glance returns, whose shapes the existing `CausalChain.hardening` suite already fixture-carries), (b) the v1.1.2 annotations in `contract.ts` itself, and (c) every FE dereference in `src/`. Verdict vocabulary: **FIXED** (this lane changed code + fixture) · **PRIOR-HARDENED** (already guarded + fixture-covered before this lane; verified, left alone) · **UNVERIFIED-AT-WIRE** (wire truth unknowable from the FE side today — LISTED, not guessed; the NEW-2 app-level boundary is the class-level containment if one of these ever nulls). Scope rule applied: type changes ONLY where wire-evidenced; honest-register fallbacks for every enum-keyed switch (the closed-switch crash class — in-repo precedent `runStatusMeta`); no speculative `??` guards on unevidenced fields (they would teach the type system to lie in the other direction).

| Field | Declared | Wire truth | FE dereference site(s) | Verdict → action |
|---|---|---|---|---|
| `NonFiringExplanation.lastEvaluation` | non-null object | **NULL, PROVEN** (§4.5 body, 200 OK) | `WhyNotView.tsx` `.at` + `.conditionsResult` | **FIXED**: type `\|null` · both guards · validator arm · mocks carry null · real-wire fixture + 7 tests |
| `NonFiringExplanation.verdict` | 4-value enum | enum on the one capture; vocabulary evolvable | `verdictMeta()` closed switch (no default → `.tone` of undefined crash) | **FIXED**: honest fallback `Recorded as "…"` + tests |
| `NonFiringExplanation.automationName` | `string` | populated on capture; the runs-surface registry-miss class COULD null it | JSX text render (no crash path) | **UNVERIFIED-AT-WIRE** — listed; renders blank-not-crash; boundary contains |
| `NonFiringExplanation.explanation`, `.triggerSummary` | `string` | populated on capture | JSX text render (no crash path) | **UNVERIFIED-AT-WIRE** — listed |
| `NonFiringExplanation.noCommandsIssued` | optional `true\|null` | per v1.1.2 | `=== true` (null-safe) | **PRIOR-HARDENED** |
| `RunSummary.automationName` | `string\|null` | null observed (prior-instance) | `runName()` fallback + `NULL_NAME_NOTE` | **PRIOR-HARDENED** |
| `RunSummary.triggeredAt` / `.status` / `.terminalReason` | str / enum / str-null | conformant on record | `timeAgo` (null-tolerant) / `runStatusMeta` (has fallback) / `?? undefined` | **PRIOR-HARDENED** |
| `CausalChain.automationName`, `trigger.type`, `trigger.firingValue` | annotated null | null observed (2026-07-27) | `CausalChain.tsx` guards + validators `strOrNull` | **PRIOR-HARDENED** (FE-LIVE-V112/FE-VERDICT-2; fixture suite carries present-but-null rows for every optional key) |
| `CausalChain.trigger.matchedAt` | `string` | ISO observed | `clockTimeWithDate` (was `clockTime`) — unparseable → `'—'`, never 1970 | **FIXED** (date-qualified; the parse guard rides `parseInstant`) |
| `CausalChain.conditions[]`/`actions[]`/`outcome`/`cascade` | non-null | sparse payloads observed (era boundary) | `?? []` / `outcome?` / `cascade?.` throughout `CausalChain.tsx` | **PRIOR-HARDENED** |
| `CausalAction.outcome` | 5-value enum | open in practice (adapter strings ride `resultOutcome`; the verdict layer consumes both) | `outcomeMeta()` closed switch | **FIXED**: honest fallback + test (`actionVerdict` is the primary consumer and was prior-hardened) |
| `CausalAction.resultOutcome`/`settled` | optional, str-null / bool | per v1.1.2, null-beside-siblings observed | `verdicts.ts` field-first + recovery | **PRIOR-HARDENED** |
| `EntityState.lastChanged/lastUpdated/lastReported` | `string\|null` | **/state serves fractional epoch-SECOND NUMBERS today** (STATE-DIALECT, measured 2026-07-27; the DX-20 exhibit is its rendering) | `timeAgo`/`clockTime`/`availabilityEvidence` in `DevicesView` | **FIXED at the misread class**: `parseInstant` never coerces a non-string → honest `'—'`/"not recorded", one parse for prose + row, date-qualified when readable. Full dialect CONSUMPTION stays charter item (h) — NOT this lane (see §7) |
| `EntityState.attributes` | non-null `Record` | present on record (dialect-nested values render `'—'` via `attrValue`'s null branch) | `Object.entries`, `brightnessDisplay` | **UNVERIFIED-AT-WIRE** for whole-map null — listed; boundary contains |
| `EntitySummary.availability` (+ `EntityState.availability`) | 3-value enum | enum on record | `availabilityMeta()`, `availabilityEvidence()` closed switches | **FIXED**: honest fallbacks + tests (the trust surface must never render `undefined`) |
| `EntitySummary.stale`, `.entityId`, `.name?` | bool / str / opt | conformant, C8 handled | filters, `displayName` | **PRIOR-HARDENED** |
| `ProjectionStatus.mode` | 3-value enum | enum on record | `HealthView.projectionMeta` closed switch (crash); `OverviewView` binary check (no crash); `poll.tsx` (try/caught → honest `error` phase) | **FIXED** (HealthView fallback + tests); Overview's binary banner renders "Catching up" for an off-vocabulary mode — accepted residue, noted |
| `ProjectionStatus.lagEvents/viewPosition/projectionVersion` | numbers | conformant | numeric renders (no crash on null) | **UNVERIFIED-AT-WIRE** for null — listed |
| `DlqStatus.parkedSubscribers` | non-null array | conformant on record (A5 live) | `.length`, `.map` in HealthView | **UNVERIFIED-AT-WIRE** for null — listed; boundary contains |
| `DlqStatus.subscribers?` | optional | per v1.1.1 | `d.subscribers?.find` | **PRIOR-HARDENED** |
| `AutomationSummary.components` | non-null array | populated on record (live automations list rendered at the rehearsal) | `.map` in 3 views | **UNVERIFIED-AT-WIRE** for null — listed; boundary contains |
| `AutomationSummary.lastRunId` | `string\|null` | null observed (DX-4) | ternaries | **PRIOR-HARDENED** |
| `EventSummary.*` (B1) | per contract | **UNVERIFIABLE — endpoint unbuilt live (404)** | EventsView renders; `originMeta()` closed switch | **FIXED** the switch (honest fallback + test); all other B1 fields listed UNVERIFIED until the endpoint exists |
| `IntegrationHealth` (B2) | 4-value enum | B2 not served (composed A4+A5) | `healthMeta()` closed switch (currently no live consumer) | **FIXED** (fallback + test — class consistency) |
| `ResponseMeta` | non-null | conformant on every capture | `Freshness` (`!meta` guarded), poll (`try`-caught) | **PRIOR-HARDENED** |

The class-level summary the hub should audit against: after this lane, (1) **no view renders outside an ErrorBoundary**, (2) **no enum-keyed formatting map can return `undefined`**, (3) **no displayed instant is ever coerced from a non-string**, and (4) the one wire-PROVEN nullability divergence is corrected in type, guard, validator, mock, and fixture. "Fixed the two open files" this is not.

## §5 Fixture provenance (H8 tier 1 — real payloads, labeled)

- `src/lib/api/fixtures/wire-2026-08-16-nonfiring.ts` — **REAL, VERBATIM**: the §4.5 rehearsal capture (GET `/api/v1/automations/01M028WEHCN64AFM2K0ZBSD5Z3/non-firing`, 200 OK, 395 B, 17 ms, ETag W/"91229", 2026-08-16 05:22:35 GMT), envelope included, key order preserved; full provenance header in the file. Consumed by the WhyNotView suite AND validated against the contract mirror in the same suite — a hand-convenient mock satisfies neither.
- The causal-chain present-but-null shapes in `CausalChain.hardening.test.tsx` were already built "exactly as observed (WCAP-2 + the chain glance)" — the pre-existing tier-1 coverage for the chain surface; verified standing, not duplicated.
- The mock fleet (`mockData`, `scenarios.makeNonFiring`) now carries the real tri-state for `lastEvaluation` (object-with-values · whole-object-null), so a fixture-green build can no longer hide the null the way it did before the rehearsal (H8's origin exhibit, closed at its origin).

## §6 The NEW-7 proposal (Activity nav → unbuilt endpoint) — hub rules

**A finding first (same H8 class as charge 2, discovered in this sweep):** EventsView already SHIPS a calm teaching state for exactly this situation ("Your hub doesn't share the activity feed yet… nothing is wrong", `events.notServedYet.*`, EventsView:27–35) — but it keys on problem slug `not-found`, and the rehearsal's live 404 rendered the generic honest ErrorState instead (title `Endpoint GET /api/v1/events not found`). Inference (stated as inference): the live unrouted-path 404 body does not carry the ratified problem+json `not-found` type, so the mock-only path is the teaching state and the live path is the raw card. The rendered text is on record; the 404 BODY is not — and per H8 this lane did not guess it.

Options: **(a)** keep-as-is — the honest 404 + retry is the design working (§6.5 of the rehearsal record calls it the counter-exhibit) · **(b)** feature-flag the nav item until B1 ships · **(c)** label the nav item "coming" honestly · **(d, REC)** keep the nav item as-is NOW, capture the live 404 body in one DevTools sitting on the next Pi visit (it rides the §8 plan below), and if it is recognizable, key the ALREADY-SHIPPED teaching state on the observed body — client-side detection only, no contract change, no guessing. Recommendation: **(d)**, degrading to (a) until the capture exists. Not implemented — the hub rules; no nav surface was removed unilaterally.

## §7 Deviations declared + cross-lane asks

Deviations (none silent):

1. **Green-at-baseline tests: 13**, disclosed by name in §3 (preservation pins + the RunChainView contained case + the vacuously-green validator-accepts-null).
2. **The "Try again" test-harness adjustment** post-red-capture (§3, disclosed; the red stood on the earlier assertion).
3. **Same-class scope additions beyond the brief's letter (arc-25, all red-first):** the closed-switch honest fallbacks were applied to ALL seven enum-keyed maps (brief names the WhyNot surface; the class doesn't stop there), and NEW-6's date-qualification was applied to every clock-only stamp (Devices, Events, WhyNot, CausalChain/causalSentence), not just the device card.
4. **UNVERIFIED-AT-WIRE fields were NOT speculatively guarded** — listed in §4 instead; the app-wide boundary is their containment. A `??` on an unevidenced field would manufacture a false nullability the same way the mock manufactured a false non-nullability.
5. **`timeAgo` non-string guard**: output for runtime numbers is byte-identical to the baseline coercion result (`'—'`); the `Updated X ago` mechanism (DX-22) is untouched — string-path behavior is pinned by a preservation test.
6. **Mock behavior change declared**: scenario `makeNonFiring` non-CONDITION_NOT_MET arms now serve `lastEvaluation: null` (the live shape) — scenario walkthroughs of those automations no longer show a "Last checked" row, which is the honest rendering.
7. **`MODULE_CONTEXT.md` not edited** — core-side convention treats MODULE_CONTEXT folds as hub-owned. Suggested fold rows for the hub: (i) ErrorBoundary is mounted app-wide at the view switch (`app.tsx`), inner per-view boundaries optional on top; (ii) `lastEvaluation` is object-or-null per the observed wire; (iii) `parseInstant`/`clockTimeWithDate` are the only lawful instant renderers (never coerce non-strings).
8. **Gate environment**: baseline re-derivation, red-first captures, and the final gate ran in the lane session's reconstructed workspace (`npm ci` from the repo's own `package-lock.json` at `d26777c`, Node 22). Local `npm run verify` GREEN end-to-end (tokens-check · lint 0/0 · typecheck · 181/181 tests · build · 63.0/100 KB gzip, 37.0 KB headroom · contract-check 11 endpoints v1.1.2). **`frontend.yml` on the push remains the CI gate of record** — commands for the record: `cd web-ui/dashboard && npm ci && npm run verify` on the committed tree.
9. **Env-model observation for the record**: several repo files are filesystem-hardlinked on the host (`ci/frontend.yml`, `scripts/build-tokens.mjs`, `src/components/{ThemeToggle,DevPanel}.tsx`, `src/lib/theme.ts`, `src/styles/fonts.css`, `FRONTEND_DOCTRINE.md`, `src/styles/fonts/README.md`); the device bridge refuses to read through link aliases, so they were read via copies. A `_scratch/hardlink-copies/` working dir was created on the host for this — safe to delete. None of those files were modified by this lane.

Cross-lane asks (FOR THE HUB):

1. **Freeze-record clarification ask (documentation, not a shape change):** annotate non-firing `lastEvaluation` as object-OR-null in the freeze record's §B3 block, citing §4.5 — the same treatment `automationName`/`firingValue` nullability received. The client mirror already records it.
2. **The NEW-7 capture ask** (§6): one DevTools save of the live `GET /api/v1/events` 404 body on the next Pi sitting.
3. **STATE-DIALECT status restate (no new ask):** `/state` instants remain epoch-second numbers on the live wire; after this lane the FE renders honest absence instead of 1970 misreads, and the drawer stays honestly degraded until charter item (h) + the core half land.

## §8 The live re-exercise plan (H8 tier 2 — for Nick, against the Pi, after the next warm rebuild/deploy)

Scripted browser pass; each row is surface · expected · what would falsify. DevTools console open throughout; any raw uncaught `TypeError` anywhere falsifies NEW-2 (a contained failure logs `[render-error] contained by ErrorBoundary:` and shows the card instead).

1. `#/explain/why-not/<current bench-hero ULID>` (re-derive the ULID — it re-mints nightly, DX-19). Expected: the "Nothing set it off" pill, the explanation sentence, "What would make it run", NO "Last checked" row, no spinner past load. Falsified by: an indefinite `Loading…`, or `can't access property "at"` in the console — the Act-2 incident signature.
2. Same page, Network tab: the non-firing response still carries `"lastEvaluation": null` (or an object — either must render; both arms are fixture-pinned).
3. `#/devices` → open the offline Hue's card. Expected: the prose and the "Last reported" row AGREE — either "last heard from X ago" + a date-qualified stamp, or "the time of the last report is not recorded" + `—`. Falsified by: "last heard from —" in prose, a bare clock time on a >24 h-old report, or any 1970-plausible morning time.
4. Any run detail >24 h old (`#/explain/run/…`). Expected: the trigger line reads "… at H:MM on <Mon D>." Falsified by: a bare clock time on an old run.
5. `#/events`. Expected: unchanged posture — the calm, honest 404 card with retry (until the hub rules on §6). While here: save the 404 response body (the §7 ask #2).
6. Cross-surface: the header "Updated …" stamp keeps ticking on every surface visited after steps 1–5 — the poll loop survived everything above. Falsified by: a frozen stamp (the 2026-07-27 signature).

**Per H7, the touched surfaces are REPO-COMPLETE, LIVE-VERIFICATION PENDING THE DEPLOY — they are not "verified" until measured live, and this return does not round that up.** This lane's scope was repo-only; no deploy was performed or attempted.

## §9 Accessibility + stranger test

All new copy is centralized in `format.ts`/component constants and test-locked; every new state is carried by label text + tone (never hue alone); the render-failure card is `role="alert"` with a real retry; the axe suite ran green in the gate in both token themes. Stranger reads, checked aloud: "This view hit a problem displaying the record — the record itself arrived and is preserved" · "Recorded as \"…\"" · "the time of the last report is not recorded" · "9:40 AM on Aug 16" — no jargon, no index paths, calm register throughout; the honest-can't-know tone is amber/unknown, never success, never alarm. No positioning or competitive claim was added; no product name was hardcoded (BRAND token untouched).

## §10 Decisions / defaults taken (explicit + revisable)

1. **Boundary placement:** inside `AppShell`, around the whole `renderView` switch (not inside AppShell's own markup) — the nav/status chrome stays outside the blast radius so a crashed view is always escapable. `resetKey` = route name + sorted params, so any navigation (including id-to-id within a view) resets a tripped boundary.
2. **App-level retry = remount-and-refetch** (boundary reset remounts children; `useApi` refetches on mount) — no `onRetry` plumbing at the switch level. Per-view inner boundaries remain lawful for tighter semantics; RunChainView's (reload-without-remount) is retained as the floor-not-cap precedent.
3. **The honest register for off-vocabulary values** standardizes on the existing `runStatusMeta` pattern: `Recorded as "<value>"`, tone `unknown`; null/absent → `<Thing> not recorded`.
4. **Date-qualification format:** `H:MM AM on Mon D` (+ year when cross-year); same-day stamps stay clock-only (the mom-test word budget).

## §11 Next recommended work unit (refuse-to-close)

**FE-STATE-DIALECT (FE-LIVE-V112 item (h)) — the device-detail drawer's contract-shape consumption**: consume AMD-52 `{"t","v"}` + ISO-8601 + string ULIDs with fixture-locked dialect detection, retiring the honest degradation this lane hardened (the `'—'` attribute rows and not-recorded stamps on the live drawer). It is the largest remaining visible-quality gap on a demo surface, it is charter-named, and this lane's `parseInstant` seam is exactly where the dialect boundary will live. Alternative if the hub prefers demo-narrative order: AUTO-IDENT (the named post-gate fix for rotation nulls). DX-12/DX-21 remain core-side.

## §12 Route-back

Intakes at the hub for two-layer audit; the deploy + live re-exercise ride the next Pi trip.
