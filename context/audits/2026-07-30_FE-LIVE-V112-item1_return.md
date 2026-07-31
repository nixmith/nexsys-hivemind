<!--
file: context/audits/2026-07-30_FE-LIVE-V112-item1_return.md
purpose: Lane return for FE-LIVE-V112 item 1 — the causal-chain render hardening (null-guards on the present-but-null tri-state seam + the load-bearing error boundary + the honest empty states). The last named G1 gate-day blocker, retired subject to CI-of-record + Nick's native run.
audience: the PM hub (intakes at v41); Nick (commits — the lane commits nothing).
state-type: lane return (single-charge, write-isolated to web-ui/dashboard/**)
status: FILED 2026-07-31 ~01:35 UTC (the 2026-07-30 dispatch; authored from the brief's returns-file law). Gate: npm run verify GREEN in-lane (verbatim §7); CI on the pushed commit is the gate of record and Nick's native host run outranks this sandbox.
baseline: core HEAD 1c800b5a3e10ee1dbf9c8884e12509491c283dc1 (worktree clean at session start, lock-free porcelain); source staged via `git archive HEAD web-ui/dashboard` (tar md5 6f985c7d3f0bc2179e05f6b3f243dd4c verified identical on both sides of the bridge).
-->

# LANE RETURN — FE-LIVE-V112 item 1: causal-chain render hardening — 2026-07-30/31

## 1. Summary

The chain view no longer crashes on live payloads. Every string mapping in the causal-chain render path is guarded against the **present-but-null tri-state seam** (absent / null / value); a **load-bearing error boundary** now contains any render throw and the polling loop **provably** survives it (test-proven, not assumed); and the view distinguishes, in the user's language, **request-failed** (retryable), **genuinely-empty** (explicit, calm), and **partial** (what resolved shown, what did not marked "not recorded" — never hidden, never invented). The mocks now carry the shape that actually broke. Red-first throughout; `npm run verify` green; 10 files, all under `web-ui/dashboard/**`.

Preflight summary: contract mirror pinned at v1.1.2-2026-07-26 ✓ · Locked stack + verify script unchanged ✓ · account-synced skill v1.8 per the brief (no local-mirror gate for this lane) ✓ · shapes re-derived from repo source at HEAD, not from copies ✓. No STALE/CONFLICTED finding blocked the charge.

## 2. The enumerated throwing sites (the corpus sweep) and their guards

Sweep basis: every value the live wire has served null (`resultOutcome` beside `settled: true`, `reason`, `trigger.type`, `automationName`, `firingValue` — the filed 2026-07-27 chain-glance evidence), plus every method/property access downstream of the chain payload in the render path.

| # | Site (pre-fix) | Failure | Guard |
|---|---|---|---|
| S1 | `format.ts:334 triggerVerbFromValue` — `firingValue.toLowerCase()`; reached from `causalSentence`, the FIRST expression of the render | **THE production crash** (`TypeError: … toLowerCase, e is null`; killed the view) | null/empty → plain verb `changed`, no parenthetical; absence disclosed in the trigger detail instead |
| S2 | `CausalChain.tsx:205 triggerPhrase` — a byte-duplicate `.toLowerCase()` on the same field (the trigger step line) | same crash class, second occurrence | duplicate REMOVED; the step line calls the single hardened `triggerVerbFromValue` |
| S3 | `format.ts labelFor` — `id.replace()` on a null/undefined `subjectRef.id` / `targetRef.id` | TypeError | null → honest `Something not on record` |
| S4 | `format.ts commandKind` — `command.toLowerCase()` (reached via `pendingHint`/`unconfirmableHint` on every action row) | TypeError | `(command ?? '')`; null classifies as `other` (no hint invented) |
| S5 | `commandVerb` / `actionPhrase` — null command interpolated | renders `ran null` / `Ran null on` (a lie, not a throw) | `acted` / `Ran an unrecorded command on` |
| S6 | `format.ts attrValueList` — `Object.entries(params)` on null | TypeError | `params ?? {}` |
| S7 | `format.ts runStatusMeta` — exhaustive switch returns `undefined` on a null/unrecognized status; `.tone`/`.label` then throws at the call site | TypeError | null → `Outcome not recorded` (tone unknown); unrecognized string → `Recorded as "<s>"` verbatim |
| S8 | `verdicts.ts actionVerdict` — a null outcome fell into the FAILED default | renders **Failed** for a value that records nothing (a lie) | new honest `not-recorded` mode: label "Not recorded", distinct dotted-line glyph, tone unknown, never provisional. Unrecognized NON-null strings keep the conservative SD-7 FAILED default (unchanged) |
| S9 | `CausalChain.tsx` — `chain.conditions.map` / `chain.actions.map` / `c.observedState.length` / `chain.outcome.*` / `chain.cascade.parentRunId` on a sparse payload | TypeError | `?? []` on all arrays; optional chaining on `trigger`/`cascade`/`outcome`; outcome-null → honest `Outcome not recorded.` terminal line |
| S10 | `terminalLine` — `durationMs / 1000` on null | renders `0.0s` — a plausible-looking number the record does not carry | duration omitted unless a finite number (`Done.` / `Finished, but nothing was changed.`) |
| S11 | trigger detail rendered a raw null `firingValue` | a SILENT BLANK in the detail row | `value not recorded`, in words |
| S12 | `c.expression` null in the condition line | renders `The rule "null" …` | `?? 'not recorded'` |

The honest-absence marker is centralized (`format.NOT_RECORDED`) and test-locked; no surface prints the string "null", and no placeholder can be mistaken for data.

## 3. Red-first evidence (house law)

The failing tests were written and run BEFORE any fix. Red run (verbatim summary):

```
 ❯ src/components/CausalChain.hardening.test.tsx (19 tests | 14 failed) 209ms
 ❯ src/lib/poll.survival.test.tsx (0 test)   [suite failed: ErrorBoundary does not exist yet]
 Test Files  2 failed (2)
      Tests  14 failed | 5 passed (19)
```

The headline failure reproduces the filed production crash exactly, at the predicted site:

```
FAIL  … > renders the full observed present-but-null chain without throwing
"TypeError: Cannot read properties of null (reading 'toLowerCase')"
 ❯ triggerVerbFromValue src/lib/format.ts:334:25
 ❯ causalSentence src/lib/format.ts:303:23
 ❯ CausalChain src/components/CausalChain.tsx:39:35
```

(The browser evidence's `e is null` phrasing is Firefox's rendering of the same TypeError; jsdom/V8 phrases it as above.) The survival suite was red on `Failed to resolve import "../components/ErrorBoundary"` — the boundary did not exist. After the fix: all 19 new tests green; full suite **140/140** green (121 pre-existing + 19 new); no pre-existing test changed.

## 4. Proof the polling loop survives a contained render throw

`src/lib/poll.survival.test.tsx` mounts the real `PollProvider` + a panel mimicking `RunChainView` (real `useApi`/`Resource`), whose data renderer **throws unconditionally** — strictly worse than the fixed chain render — inside the new `ErrorBoundary`. With fake timers:

- after the first contained throw, the spy counts for BOTH loops are recorded, then time advances again and the test asserts both counts **strictly increased**: `api.getProjection` (the global 1.5 s poll) AND the view's own refetch-on-cursor-advance (the loop that died in the field on 2026-07-27);
- a sibling surface outside the boundary stays rendered (the app does not go down with the view);
- the honest render-error card is on screen (`role="alert"`), and **Try again** resets the boundary and re-renders the children (proven with a throw-once component).

Wiring: `RunChainView` wraps the chain render in `<ErrorBoundary resetKey={runId} onRetry={state.reload}>`; navigating to a different run auto-resets a tripped boundary.

## 5. The three empty-state cases (what each renders)

1. **The request failed** — network/HTTP error on the chain read → the existing `Resource`/`ErrorState` card: the problem's own title + detail and a **Try again** button (the Activity-404 exemplar posture). Fixture `run_ln_missing` exercises it end-to-end (listed run, chain read 404s). Distinct from it, a **render** failure now gets its own card (`ErrorBoundary`): *"This view hit a problem displaying the record — the record itself arrived and is preserved; the display failed while drawing it. The rest of the dashboard keeps updating."* + Try again. The two failures are never conflated, and neither is a spinner or a blank.
2. **The chain is empty** — a real, successful, genuinely empty response (no conditions, no actions, `actionCount 0`) → an explicit step in the chain: *"This run finished without recording any steps — no conditions were checked and no commands were sent."* (`format.EMPTY_CHAIN_NOTE`, test-locked). Calm `unknown` tone — nothing failed, so no error register.
3. **The chain is partial** — present-but-null / era-sparse fields render what resolved and mark what did not: trigger value → *"value not recorded"*; trigger type → *"recorded before the current automations"* (existing); null name → the calm prior-instance note (existing); null action outcome → the *"Not recorded"* pill; missing duration → omitted, never `0.0s`. The era-skeleton (`actionCount > 0`, empty `actions[]`, `commandCount 0`) keeps its never-clean-success rendering — see §8 observation O5 on the item-(i) boundary.

Tests pin all three, including that the empty state never borrows the error register and that no null-carrying chain ever prints "null".

## 6. The new fixtures (the shape that actually broke, now fixture-covered)

New mock scenario **`live-nulls`** (“Live wire: present-but-null”), on-contract and validated by `contract.test.ts` + the new fixture tests:

- **`run_ln_nulls`** — every nullable key PRESENT-BUT-NULL beside populated siblings, exactly as captured: `automationName: null`, `trigger.type: null`, `trigger.firingValue: null`, `actions[].reason: null`, `actions[].resultOutcome: null` **beside** `settled: true`, `outcome.reason: null`.
- **`run_ln_empty`** — the genuinely empty chain (conditions `[]`, actions `[]`, `actionCount 0`, `commandCount 0`).
- **`run_ln_missing`** — listed in `runs[]` with NO chain fixture, so the mock transport serves the honest 404 problem+json (the retryable error-card case).

Additionally the hardening test builds the observed live shape in-file (independent of the scenario), and a **fixture-blindness sweep** renders every chain of EVERY scenario — so no future fixture can be structurally blind to a shape the render would crash on.

## 7. Gate output — verbatim (in-lane; CI on the pushed commit is the gate of record)

```
> @homesynapse/dashboard@0.1.0 verify
> npm run tokens:check && npm run lint && npm run typecheck && npm run test && npm run build && npm run check:bundle && npm run check:contract

> @homesynapse/dashboard@0.1.0 tokens:check
> node scripts/build-tokens.mjs --check
tokens:check — OK (tokens.css matches the token source).

> @homesynapse/dashboard@0.1.0 lint
> eslint .

> @homesynapse/dashboard@0.1.0 typecheck
> tsc --noEmit

> @homesynapse/dashboard@0.1.0 test
> vitest run
 Test Files  8 passed (8)
      Tests  140 passed (140)

> @homesynapse/dashboard@0.1.0 build
> vite build
vite v6.4.3 building for production...
✓ 60 modules transformed.
dist/index.html                                     1.69 kB │ gzip:  0.87 kB
dist/assets/inter-variable-subset-C98NWKZD.woff2   25.39 kB
dist/assets/style-BnqGyYkK.css                     28.13 kB │ gzip:  5.61 kB
dist/assets/index-B9CmxYDm.js                     101.88 kB │ gzip: 32.34 kB
✓ built in 856ms

> @homesynapse/dashboard@0.1.0 check:bundle
> node scripts/check-bundle-size.mjs
✓ Within budget (62.6 KB / 100 KB, 37.4 KB headroom).

> @homesynapse/dashboard@0.1.0 check:contract
> node scripts/contract-check.mjs
✓ Contract coverage complete: 11 endpoints, version v1.1.2-2026-07-26.
```

Exit code 0. Environment notes: Node v22.22.2 / npm 10.9.7 in the cloud container; **esbuild's native binary ran clean here — the §9 wasm workaround was not needed**; `package-lock.json` untouched (not regenerated); disk checked before `npm ci`. This green is not the gate of record — `frontend.yml` on the pushed commit is, and Nick's native host run outranks any sandbox result.

## 8. Deviations and observations (severity-honest)

- **[INFO] O1 — contract mirror nullability annotation (guard-only, per the §4 ruling).** `contract.ts CausalTrigger.firingValue` widened to `string | null` with an OBSERVED-LIVE-NULLABILITY comment — the exact `automationName`/`trigger.type` precedent already in the mirror. The freeze document is untouched; the v1.1 wire base is untouched; **a contract-clarification ask is hereby recorded for the hub** (same class as the 2026-07-19 automationName ask): the freeze text does not annotate `firingValue` nullable, the live wire serves it null in all eras. No other action taken on the field.
- **[INFO] O2 — validator addition.** `shapes.ts B3:causalChain` now checks `trigger.firingValue` as present-and-string-or-null (it was previously unvalidated). A live payload OMITTING it would now surface as a `[contract-drift]` console error in validate-mode — which is the correct cross-lane visibility, not a client patch.
- **[INFO] O3 — client-internal vocabulary.** `verdicts.ActionMode` gains `'not-recorded'` (label/glyph/tone only). No wire meaning, no contract surface; the five-modes-distinct law is untouched (all five keep their distinct label+glyph pairs; the new mode adds a sixth distinct pair for the null class).
- **[INFO] O4 — bundle delta.** Initial js 99.02 → 101.88 kB raw; gzip 32.34 KB, total initial 62.6/100 KB — green with 37.4 KB headroom.
- **[INFO] O5 — the era-skeleton boundary (item (i), not this lane).** A skeleton chain (`actionCount > 0`, `actions: []`, `commandCount: 0`) is wire-indistinguishable from a lawful silent-skip run, so it renders through the existing hedged silent-skip posture (never clean success). The dedicated *"no detail recorded for this run"* state is charter item (i), explicitly out of this lane's scope; the hub owns its dispatch. Nothing in this lane makes that later fix harder.
- **[INFO] O6 — the npm-audit rider.** `npm ci` reports the standing `1 high severity vulnerability`; no dependency was touched (the rider rides the next deps touch, per the charter).
- **[INFO] O7 — environment.** Source was staged into the work container from **git objects at HEAD** (`git archive HEAD web-ui/dashboard`, md5-verified across the bridge — no worktree-read hazard); outputs were written back host-side via the bridge and byte-size-verified against the host listing. `_scratch/dashboard_1c800b5.tar` (610 KB) remains in `ClaudeFolder/_scratch/` — scratch-area content, safe to delete; it is a sibling of the repos and cannot be staged by any repo commit.
- **Dialect observations:** none new — this lane did not touch `/state` or any wire parsing (item (h) untouched, per the STATE-DIALECT hold). `firingValue` is O1 above: guarded, recorded, not otherwise acted on.
- **[REVIEW]-class deviations:** none. Scope held to item 1; no favicon change, no deps change, no core/bench/docs/hivemind-spine writes, no new dependency, no contract-shape invention.

## 9. Accessibility + stranger test

The boundary card is `role="alert"` with plain-language title/body (test-locked copy constants); the null-class states carry label TEXT + distinct glyph + tone (never hue alone — the `not-recorded` mode has its own dotted-line glyph); the chain stays a semantic `<ol>`; axe-core structural rules pass on the hardened present-but-null chain (new test) and the whole existing a11y suite passes unchanged. All new copy is device-backward plain language, ≤ ~20 words a sentence, name-light (no product-name hardcoding anywhere in the new strings).

## 10. Porcelain census + the commit order (Nick commits; the lane commits nothing)

Exact lock-free census (`git --no-optional-locks status --porcelain -- web-ui/dashboard`, host repo, post-write — **exactly 10 entries, each mapped to a §2/§4/§6 deliverable**):

```
 M web-ui/dashboard/src/components/CausalChain.tsx        → S2, S5, S9–S12; the honest empty step; partial markers
 M web-ui/dashboard/src/lib/api/contract.ts               → O1 firingValue observed-nullability annotation
 M web-ui/dashboard/src/lib/api/mock/scenarios.ts         → §6 the live-nulls scenario (3 exhibits)
 M web-ui/dashboard/src/lib/api/shapes.ts                 → O2 firingValue validator line
 M web-ui/dashboard/src/lib/format.ts                     → S1, S3–S7; NOT_RECORDED + EMPTY_CHAIN_NOTE copy
 M web-ui/dashboard/src/lib/verdicts.ts                   → S8 the not-recorded verdict mode
 M web-ui/dashboard/src/views/RunChainView.tsx            → §4 boundary wiring (resetKey + reload retry)
?? web-ui/dashboard/src/components/CausalChain.hardening.test.tsx → §3/§5/§6 red-first render + fixture tests
?? web-ui/dashboard/src/components/ErrorBoundary.tsx      → §4/§5 the load-bearing boundary + honest card
?? web-ui/dashboard/src/lib/poll.survival.test.tsx        → §4 loop-survival proof
```

Ignore-coverage: `dist/`, `node_modules/`, coverage untracked and ignored (verified — the census above is the whole delta); lockfile unmodified; no secrets — no server run, no token minted, no token in any file or this return.

**The core commit — stages exactly 10 files** (from `homesynapse-core/`):

```
git add web-ui/dashboard/src/components/CausalChain.tsx web-ui/dashboard/src/components/CausalChain.hardening.test.tsx web-ui/dashboard/src/components/ErrorBoundary.tsx web-ui/dashboard/src/lib/poll.survival.test.tsx web-ui/dashboard/src/lib/format.ts web-ui/dashboard/src/lib/verdicts.ts web-ui/dashboard/src/lib/api/contract.ts web-ui/dashboard/src/lib/api/shapes.ts web-ui/dashboard/src/lib/api/mock/scenarios.ts web-ui/dashboard/src/views/RunChainView.tsx
```

Suggested message (plain; **no attribution trailers of any kind, per the standing directive** — no Co-Authored-By, no AI-attribution, no session links; contains no `!`, no inner `"`, no backticks, so `-m` is safe):

```
fix(dashboard): FE-LIVE-V112 item 1 - chain render hardened for the live present-but-null wire (null-guards, load-bearing error boundary, honest empty states, live-nulls fixtures; red-first, verify green)
```

**The hivemind commit — stages exactly 1 file** (from `nexsys-hivemind/`; this return, per the returns-file law):

```
git add context/audits/2026-07-30_FE-LIVE-V112-item1_return.md
```

After the core push: the `frontend.yml` glance on the landing commit is the gate of record; the fix reaches the Pi on any warm rebuild + restart.

## 11. Done-when, checked against §7 of the brief

- populated live-shaped payload renders without throwing — ✅ (test: full observed null-set chain + the every-scenario sweep)
- present-but-null renders honestly, no crash, no lie — ✅ (per-key tests; "null" never printed; nothing invented)
- error and empty each produce their own truthful state — ✅ (§5; fetch-failure ≠ render-failure ≠ empty, all distinct, two retryable, one calm)
- polling loop provably survives a render throw — ✅ (§4, strict-increase assertions on both loops)
- `npm run verify` green with output quoted — ✅ (§7, exit 0)

In-lane, item 1 is COMPLETE. It is **retired as the G1 blocker only when** `frontend.yml` is green on the pushed commit and Nick's native run agrees — those two are Nick's/CI's, not this lane's, and this return claims nothing beyond its sandbox green.

## 12. Next recommended WU (refuse-to-close)

**FE-LIVE-V112 items (f) + (g)** as the next FE lane (the uniform honest error/empty postures across the remaining surfaces + timestamp-with-date qualification), with the favicon rider folded in per the beat-9 REC; item (h) stays gated on the STATE-DIALECT ruling; item (i) (the era "no detail recorded" state) dispatches whenever the hub prefers — O5 notes it composes cleanly with this landing. Cross-lane asks for the hub: the O1 firingValue contract-clarification ask; nothing else.
