<!--
file: context/audits/2026-08-21_FE-lane_never-triggered-fixture_F-S3_return.md
purpose: FE-lane return for the 2026-08-21 brief (context/instructions/2026-08-21_FE-lane_never-triggered-fixture_and_F-S3_brief.md) — (1) the 2026-08-20 live never-triggered body filed as a provenance-grade fixture and tested as CROSS-DEPLOYMENT DIALECT STABILITY (not a third arm); (2) F-S3 answered at source — the run-detail "Updated" stamp's mechanism pinned at file:line, with ONE copy proposal for the hub to rule on; (3) the optional NEW-7 (a) rider EXECUTED — the already-shipped Activity teaching state re-keyed on the observed wire discriminator (path ∧ 404 ∧ application/json-not-problem+json), headers-only fixture, red-first both directions.
audience: the Core/PM mission-control hub (two-layer audit), Nick.
state-type: lane return. Files to context/audits/ per the brief (ONE file, uncommitted — the hub stages it).
status: DELIVERED 2026-08-21 (filing day, America/Chicago — written Fri 2026-08-21 ~20:50 CDT). Baseline homesynapse-core `7c9e4fa` (verified at checkout: 7c9e4fab4f3cfc52de41ad89a6a040f1baf85a9b, main, porcelain clean at start). All work under web-ui/dashboard/. ZERO core-Java changes (Core sources were READ to ground F-S3 and the 404 discriminator; none edited). Local verify gate GREEN (210/210; 63.2/100 KB gzip; contract-check 11 endpoints v1.1.2); frontend.yml on the push remains the CI gate of record. The one changed SURFACE (the Activity teaching card) concludes REPO-COMPLETE, LIVE-VERIFICATION PENDING THE DEPLOY (§8).
-->

# FE Lane Return — the 2026-08-20 never-triggered fixture · F-S3 at source · NEW-7 (a)

## §0 Preflight + baseline

```
FRONTEND FRESHNESS PREFLIGHT — 2026-08-22 01:25 UTC (2026-08-21 20:25 CDT)
Check 1 (snapshot ↔ lane state):     PASS  (snapshot chain v55 beat 2 names THIS brief dispatch-ready; core 7c9e4fa == checkout HEAD; dashboard tree untouched since c091f7c per the brief, confirmed — the three NEW-2/3 gotcha rows are in MODULE_CONTEXT)
Check 2 (contract v1.1 currency):    PASS  (contract.ts CONTRACT_VERSION v1.1.2-2026-07-26; lastEvaluation object-OR-null at contract.ts:361; contract-check green at the gate)
Check 3 (Doc-13 currency / stack):   PASS  (verified at code: Preact 10 + Vite + TS + CSS Modules; 100 KB gate enforced by scripts/check-bundle-size.mjs; no WS client — poll.tsx is the one loop)
Check 4 (module truth populated):    PASS  (MODULE_CONTEXT + FRONTEND_DOCTRINE populated; every cited file/switch exists in src/)
Check 5 (B-class mock vs real):      PASS  (B3 four reads live on the deployed Pi — the 2026-08-20 sitting record; B1 /events UNBUILT → router 404 — the same record, §6 row 5; B2 composed client-side)
Check 6 (brand-source / name-light): PASS  (G-2 two-acts-held per the snapshot's standing fences; name-light in force; no product name hardcoded by this lane — the one new copy string is name-free, test-pinned)
Check 7 (dual skill-mirror):         PASS  (7/7 files sha256-identical — nexsys-skills/orchestrators/nexsys-frontend on the device vs the session's synced skill)
Check 8 (source round-trip):         PASS  (both wire bodies re-derived byte-exact against the recorded sizes — §3; the ETag/304 mechanism traced to Core source + the Javalin 6.7.0 tag; the discriminator's premise traced to RestFilters.java:551 + EndpointResponses.java:40–:43 + HomeSynapseCore.java:904 — and the brief's media-type framing CORRECTED at source, §6)
Aggregate: PASS
```

**Baseline identity:** `7c9e4fa` at checkout; porcelain clean (the `_scratch/` working dir sits outside the repo). The brief's evidence base was read whole and in order (§0 items 1–4) before any edit. Test-site census at baseline, re-derived by the brief's grep: **144 `it(`/`test(` sites across 12 files** (matches the brief's authoring count exactly); vitest-executed: **181/181** (the `it.each` tables account for the difference).

## §1 Summary

**Charge 1 — filed as stability, not as an arm.** `src/lib/api/fixtures/wire-2026-08-20-never-triggered.ts` carries the 2026-08-20 non-firing 200 body VERBATIM (envelope included, key order as captured) under the 2026-08-16 fixture's exact provenance-header form, with `not captured` written for every value the record does not carry. A sibling drift detector, `fixtures.stability.test.ts`, proves the two real captures have IDENTICAL key sets (recursive, envelope included), IDENTICAL null-ness per key, and differ in VALUE at EXACTLY `{data.automationId, meta.viewPosition, meta.timestamp}` — and proves its own teeth by mutated copies that fail the named arm. Two strengtheners, labeled: a byte-completeness pin (both fixtures serialize compactly to exactly their recorded sizes, 395 B and 396 B — the +1 is the sixth digit of `viewPosition`) and a key-ORDER pin (stricter than the brief; separately named so the hub can drop it). The view's own suite gains the render test: the 08-20 body renders text-identical to the 08-16 body once the freshness stamp is masked.

**Charge 2 — F-S3 answered at source (§5).** The run-detail view is NOT fetch-once and NOT interval-driven: it is viewPosition-driven exactly like every other view (`poll.tsx:147–:149`). The stamp ages because the causal-chain endpoint is the ONLY read surface with a STRONG, content-constant ETag (`"<runId>"`, `GetRunCausalChainEndpoint.java:100–:102`), so every refetch after the first is answered `304` by Javalin's ETag short-circuit, and the client's 304 path returns its OWN cached result — `meta.timestamp` included (`client.ts:124–:126` at baseline). The stamp then re-renders the FIRST response's generation time against a fresh `Date.now()` at each cursor advance. List views carry weak position-keyed ETags that change with the cursor → `200` → fresh `meta.timestamp` → the stamp resets. ONE proposal: **relabel to `As of <time> · live`** (rationale in §5). Nothing changed in this lane — the hub rules.

**Charge 3 — the NEW-7 (a) rider, executed (census permitting — it did).** A finding first: the teaching state already SHIPPED in `EventsView.tsx` (i18n `events.notServedYet.*`) but keyed on problem slug `not-found` — an inference the live wire refuted. It is now keyed on the OBSERVED discriminator, client-side: `client.ts` mints a typed `endpoint-not-in-this-release` problem when (path `/api/v1/events` ∧ status 404 ∧ media type `application/json`) — decided from the headers BEFORE any body read; the body was not captured and is never consulted. A problem+json 404 on the same path now renders the generic honest card + Try again, as every OTHER 404 does. Headers-only fixture filed and labeled `HEADERS-ON-RECORD, BODY NOT CAPTURED`; 13 tests; the two surface flips captured RED at baseline. A source finding rides it (§6): Core's endpoint-level problems go out as `application/json` (`EndpointResponses.problem()` → `ctx.json`), not `application/problem+json` — so the discriminator's premise is carried by the PATH (unrouted in this release), not by the media type alone; flagged for the hub as a Core-side content-type observation, not patched.

## §2 Changed-file census (exact; all under `web-ui/dashboard/`; 7 files = 3 M + 4 A)

Modified (3):

| # | File | Charge | What changed |
|---|---|---|---|
| 1 | `src/views/WhyNotView.nullability.test.tsx` | 1 (c) | `renderDetail` gains an optional `meta` parameter; NEW describe (2 tests): the 08-20 body renders the honest never-triggered surface, and renders text-identical to the 08-16 body with the `Updated … ago` stamp masked |
| 2 | `src/lib/api/client.ts` | 3 | `ApiProblem.isUnservedEndpoint`; `UNSERVED_ENDPOINT_SLUG`; `FROZEN_UNBUILT_PATHS` (only the observed `/api/v1/events`); `mediaType()`; `isUnservedEndpoint404()`; `unservedEndpointProblem()`; the non-2xx branch consults the discriminator before `toProblem()`. Header comment extended by one clause |
| 3 | `src/views/EventsView.tsx` | 3 | The teaching-state condition: `slug === 'not-found'` → `isUnservedEndpoint`; the comment rewritten to say why (the refuted inference; problem+json not-found now = generic card) |

New (4):

| # | File | Charge | What it is |
|---|---|---|---|
| 4 | `src/lib/api/fixtures/wire-2026-08-20-never-triggered.ts` | 1 (a) | THE REAL 2026-08-20 WIRE BODY, verbatim, envelope included — provenance block in §3 |
| 5 | `src/lib/api/fixtures/fixtures.stability.test.ts` | 1 (b) | The cross-deployment drift detector (14 tests: 7 stability + 7 teeth) |
| 6 | `src/lib/api/fixtures/wire-2026-08-20-events-404-headers.ts` | 3 | `HEADERS-ON-RECORD, BODY NOT CAPTURED` — the request shape + `{ status: 404, headers: { content-type: application/json, content-length: 159 }, body: null }` |
| 7 | `src/views/EventsView.unserved404.test.tsx` | 3 | 13 tests: the discriminator as a pure function (6) · through the client, incl. body-independence (4) · the surface: teaching vs generic (3) |

Against the brief's expectation: Charge 1 = 1 A fixture + **1 A test + 1 M test** (one file more than "1 M/A" — the detector lives beside the fixture class it guards, as a `.ts` with no DOM, and will accept future captures; the render test belongs in the view's suite beside the 08-16 render test it mirrors — declared, §7 dev-1). Charge 2 = zero, as required. Charge 3 = 2 M + 2 A = **4** (vs "+2–3" — the fixture and the test are separate files by the fixture-class law; declared, §7 dev-2). Not touched, deliberately: `MODULE_CONTEXT.md` (hub-owned fold; suggested rows in §7), `feedback.tsx` / `format.ts` / `poll.tsx` / `RunChainView.tsx` (F-S3's mechanism and copy — untouched per the brief; DX-22's open question stands), `i18n.ts` (the shipped teaching copy kept verbatim — §7 dev-4), `mock/*` (the mock transport never emits the router 404, so the mock fleet needs no new exhibit — the headers-only fixture is the exhibit).

## §3 The fixture provenance block, as filed (Charge 1 (a))

```
REAL-PAYLOAD FIXTURE (H8 tier 1 — the live-wire verification rule).
CAPTURE PROVENANCE — this is a REAL wire body, not an authored mock:
  Captured : 2026-08-20 ≈23:59:59 GMT (≈18:59:59 CT — "seconds before the 19:00 CT wave-trigger";
             the instant is the body's own meta.timestamp, the only clock the record carries),
             midweek FE-deploy sitting, DevTools → Network → Response tab, pasted as text
             (bodies carry no token — L3).
  Request  : GET /api/v1/automations/01M0GPZFVANYA5TZMZSXRCV063/non-firing
             (host not captured — the browser reached the Pi's :7070 through an SSH tunnel;
             the record carries the path only)
  Response : 200 OK · 396 B · timing not captured · ETag not captured ·
             X-HomeSynapse-View-Position not captured
             (396 B is the record's size for the 200 class on this path — §2 row 2; re-derived:
             this object serializes compactly to exactly 396 bytes, as the 2026-08-16 fixture
             does to its recorded 395. The header values for THIS response were not transcribed;
             the body's own meta.viewPosition is 104220.)
  Record   : nexsys-hivemind/context/audits/2026-08-20_midweek-FE-deploy_sitting-record.md
             §6 (closure addendum — row 2 CLOSED-FULL, "the null arm CONFIRMED at the wire")
  Build    : the deployed bundle at capture was index-C95CAnmp.js — core c091f7c, the NEW-2/3
             build (sitting record §1 Block 2). The dashboard tree at this checkout's baseline
             (7c9e4fa) is unchanged since c091f7c.
WHY IT EXISTS — STABILITY, not a new arm: [the brief's §1 adjudication, carried verbatim in
             sense: second real capture of the SAME null arm from a DIFFERENT deployment; its
             value is cross-deployment dialect stability — the class of silent drift F-S2
             proves possible on /state, caught on the surface where it has NOT happened.]
VERBATIM — do not "clean up" this object.
```

`WIRE_20260820_NEVER_TRIGGERED_BENCH_HERO: Envelope<NonFiringExplanation>` — body exactly as the record's §6 (`automationId` `01M0GPZFVANYA5TZMZSXRCV063` · `automationName` `bench-hero` · `enabled` true · `verdict` `NEVER_TRIGGERED` · `lastRelevantRunId` null · the explanation sentence · `triggerSummary` `state change` · `lastEvaluation` null · `noCommandsIssued` null · `meta` `{ viewPosition: 104220, timestamp: "2026-08-20T23:59:59.684724880Z" }`).

**Three honesty notes on the header, so nothing reads rounder than it is.** (1) The ETag / View-Position HEADER values for this specific response are not on record: the record's §2 row 2 carries positions 104218 → 104221 → 104223 for OTHER 200s in the series and "ETags advancing" — none equals this body's 104220, so the header line says `not captured` rather than inferring `W/"104220"` (which the endpoint's code, `GetNonFiringEndpoint.java:106`, WOULD have produced — a true-by-construction value is still not a captured one). (2) "396 B" is the record's size for the 200 class on this path, corroborated arithmetically (§4), not a per-response readout. (3) The capture instant is the body's `meta.timestamp` — the record's own anchor ("seconds before the 19:00 CT wave-trigger") — and is written as ≈.

**The refutation the brief invited, answered:** the two bodies do NOT differ in any key the brief did not enumerate. Re-derived independently of the brief (walked both objects): the value-diff set is exactly `{data.automationId, meta.timestamp, meta.viewPosition}`; key sets, null-ness, and key ORDER are identical. No finding to file first.

## §4 Test census + the red proofs

**Census:** `it(`/`test(` sites **144 → 173 (+29) across 12 → 14 files**; vitest-executed **181 → 210 (+29)**, all green. Per suite: `fixtures.stability.test.ts` 14 · `WhyNotView.nullability.test.tsx` 7 → 9 · `EventsView.unserved404.test.tsx` 13.

**Disclosure (#18, as the brief requires):** Charge 1's (b) stability assertions and (c) render test are GREEN-BY-CONSTRUCTION on a stable wire — seven detector assertions and two render tests, disclosed by name below. The detector's teeth are therefore proven two ways: (i) seven in-suite teeth tests, each mutating a copy and asserting the NAMED arm throws; (ii) a captured run with the REAL fixture mutated on disk.

**(ii) The mutated-real-fixture red run (the brief's own mutation — `extra: 1` added inside `data` of the 08-20 fixture file, run, then the file byte-restored and diff-verified):**

```
× IDENTICAL key sets — recursive, envelope included
  AssertionError: expected [ 'data.extra' ] to deeply equal []
× the differing VALUES are EXACTLY {data.automationId, meta.viewPosition, meta.timestamp} — nothing more, nothing less
  AssertionError: expected [Function] to not throw an error but 'Error: key set differs: data.extra' was thrown
× IDENTICAL key ORDER per object (…)
  AssertionError: expected [ 'data' ] to deeply equal []
× byte-complete against the recorded sizes: 395 B (2026-08-16) and 396 B (2026-08-20) (…)
  AssertionError: expected 406 to be 396
(+5 teeth tests red for the same root cause — their expected NAMED reason was pre-empted by "key set differs: data.extra")
Tests  9 failed | 5 passed (14)
```

The detector's false-verdict boundary, fixture-paired (arc-discipline 10) — the in-suite teeth, each green on the real pair and proving its arm by mutation: an EXTRA key → `key set differs: data.extra` · a MISSING key (`noCommandsIssued` dropped) → `key set differs: data.noCommandsIssued` · null → value (`noCommandsIssued: true`; key set unchanged, so ONLY the null-ness arm fires) → `null-ness differs: data.noCommandsIssued` · `lastEvaluation` null → object → null-ness differs AND its two new keys surface · a one-character VALUE change outside the lawful set (`'state change '`) → `value differs outside the lawful set: data.triggerSummary` · a re-ORDERED object (`automationId` moved last) → fails ONLY the order pin (the other three arms pass — the pins are independent) · a "cleaned-up" fixture changes the byte count.

**Byte-completeness corroboration (labeled strengthener, Check 8):** `JSON.stringify` of the 08-16 fixture object (compact, key order as captured) is exactly **395 bytes** — the rehearsal record's `395 B`; the 08-20 object is exactly **396 bytes** — the sitting record's `396 B`. Both bodies therefore mirror the wire byte-for-byte in key set, key order, and values (Jackson-compact, `LinkedHashMap` order at `GetNonFiringEndpoint.java:93–:99`), and the pin is itself a drift detector. (The same arithmetic on the uncaptured 404 body, for the record and NOT as evidence: Javalin's default 404 document for this route is 133 B compact, 158 B pretty-printed at 4 spaces, 159 B with a trailing newline — consistent with the recorded 159 B, not proven; the body stays uncaptured and the discriminator never keys on it.)

**Charge 3 red-first (captured against a pristine `7c9e4fa` copy with a baseline-only harness — the discriminator's own exports did not exist at baseline, so those 10 tests could not run there; disclosed, not rounded up):**

```
× [EXPECT RED AT BASELINE] the observed router 404 renders the teaching card
  AssertionError: expected 'ActivityRecent things that happened i…' to contain 'Your hub doesn’t share the activity f…'
  (baseline rendered the GENERIC card "Endpoint GET /api/v1/events not found" + Try again — the 2026-08-16/08-20 live posture, in-fixture)
× [EXPECT RED AT BASELINE] a problem+json not-found renders the GENERIC card, not teaching
  AssertionError: expected 'ActivityRecent things that happened i…' not to contain 'Your hub doesn’t share the activity f…'
  (baseline rendered the TEACHING copy for a Core-authored not-found — the refuted inference)
Tests  2 failed (2)
```

Both flip green after the change (the surface tests in `EventsView.unserved404.test.tsx`). Green-at-baseline by construction and disclosed: the 08-20 render tests (2) and the 7 stability assertions; the 6 pure-function discriminator tests and the 4 client-level tests are new-code tests with no baseline counterpart.

## §5 F-S3 answered at source (Charge 2) — the mechanism, at file:line

**What the stamp renders.** `Page` (`layout.tsx:28`) renders `<Freshness meta={meta}/>` from the view's `state.meta` (`RunChainView.tsx:17`; every list view likewise); `Freshness` (`feedback.tsx:79–:86`) renders `Updated {timeAgo(meta.timestamp)}` with a `title` of `Projection cursor <meta.viewPosition>`; `timeAgo` (`format.ts:73–:86`; the `min ago` branch at `:80–:81`) computes against `Date.now()` AT RENDER. `meta.timestamp` is the server's **response generation time** — `ResponseMeta.java:30` ("the response generation time"), emitted as `clock.instant()` at `GetRunCausalChainEndpoint.java:92` / `ListRunsEndpoint.java:107` / `GetNonFiringEndpoint.java:95`. There is NO timer anywhere: the stamp's text changes only when the view re-renders.

**When the view re-renders, and what `meta` it re-renders with.** `useApi` (`poll.tsx:129–:152`) runs `load()` on mount and whenever `viewPosition` changes (`:147–:149`) — and ONLY then; `load()` always calls `setS({ status: 'ok', data, meta })` (`:138`), a fresh object, so every settled fetch re-renders the view (and the stamp) against a new `Date.now()`. So far every view is identical. The divergence is what `load()` RECEIVES:

- `client.get` (`client.ts` at baseline) keeps a per-path `etagCache` (`:103`), sends `If-None-Match` with the cached ETag (`:111`), and **on a `304` returns the CACHED `ApiResult` — `meta.timestamp` and all** (`:124–:126`); on a `200` it stores the new result + ETag (`:161–:167`).
- The server's ETag policy is endpoint-specific (Core source, `api/rest-api/.../`): the causal chain carries a **STRONG ETag keyed on the immutable `runId`** — `"<runId>"`, constant for the life of the run (`GetRunCausalChainEndpoint.java:100–:102`, with its own comment: "The causal chain of a terminal run is immutable (INV-ES-01), so a strong ETag keyed on the immutable runId is appropriate"). Every other read surface that sets an ETag keys it WEAKLY on the projection position — `W/"<viewPosition>"` — runs list `ListRunsEndpoint.java:118`, non-firing `GetNonFiringEndpoint.java:106`, automations `ListAutomationsEndpoint.java:100`, DLQ `:174`, projection `ProjectionStatusEndpoint.java:172`; the entities list sets NONE (`ListEntitiesEndpoint` — no `ETag` header; no 304 path at all).
- The 304 itself is Javalin's, not Core's: the rest-api module has no `If-None-Match` handling; Javalin 6.7.0's `ETagGenerator.tryWriteEtagAndClose` (source read at the `javalin-parent-6.7.0` tag, lines 18–20) answers `304` whenever the handler-set `ETag` equals the request's `If-None-Match`, regardless of the autogenerate setting. The sitting record's "+1 lawful 304" on the non-firing path is the empirical confirmation that this path is live on the deployed hub.

**Therefore (i):** the run-detail view is **viewPosition-driven** — it refetches on every cursor advance exactly like the lists. But its ETag never changes, so every refetch after the first is a `304`, the client hands `load()` its own cached result, and the stamp re-renders the FIRST response's `meta.timestamp` against a later `Date.now()`: "just now" on load, then "1 min ago", "3 min ago" in STEPS at each cursor advance, never returning to "just now" while the run is immutable. The lists' weak ETag differs from the cached one on every cursor advance (the cursor is what changed) → `200` → fresh `meta.timestamp` → the stamp resets. F-S3's two observations are one mechanism seen from its two ends. The hub's fetch-once hypothesis was wrong in mechanism and right in effect — the detail IS served once; the client merely keeps asking and is told "unchanged".

**Residual, honestly carried:** the list readings "35 sec ago" / "24 sec ago" themselves are not fully explained by source: a 200 re-renders the stamp against the NEW `meta.timestamp`, which should read "just now" unless (a) the screenshot caught a re-render between a cursor advance and its refetch settling (milliseconds — unlikely twice), (b) an interaction re-render (row activation, the device drawer) drew a stale-but-honest age, or (c) the Pi's clock runs ahead of the laptop's by tens of seconds (`clock.instant()` vs the browser's `Date.now()`). The live plan (§8) discriminates (c) in one glance.

**(ii) Is the label honest, under the copy laws, for THIS mechanism?** Literally: yes — "Updated 3 min ago" states when the hub generated the representation on screen, and for an immutable run that representation IS the current truth (the hub has confirmed "unchanged" at every cursor advance since). Connotatively: no — beside a `● Live` footer, "Updated 3 min ago" reads to a stranger as "this page stopped refreshing", the frozen-stamp incident's own signature (the 2026-07-27 class), on the one surface where a stale-looking stamp is the CORRECT behavior. The operator read it that way at the sitting; that is the stranger test failing on the connotation while passing on the letter. Two smaller dishonesties ride the same path: the relative form is only true at the instant it renders (no timer — "35 sec ago" stays on screen for minutes if nothing re-renders), and the tooltip's "Projection cursor 104220" is the FIRST load's cursor on the 304 path — the client discards the fresh `X-HomeSynapse-View-Position` the 304 carries (`client.ts:124` returns before `:165` reads headers; the header is set before the body write at `GetRunCausalChainEndpoint.java:99`, so it rides the 304 by construction — not on record, stated as construction). Verdict: a copy nit and a tooltip nit — not a defect; the hub's F-S3 adjudication stands.

**(iii) THE ONE PROPOSAL — relabel: `As of <time> · live`** (the brief's own mapping for the position-driven case), where `<time>` = `clockTimeWithDate(meta.timestamp)` (date-qualified per NEW-6) and the trailing word is the poll PHASE label the footer already owns (`live` / `Catching up` / `Reconnecting` / `Offline`) rather than a constant. **Rationale, one line:** the stamp is an absolute server instant re-rendered without a timer, so an absolute "As of 7:00 PM" is true until the next render while a relative "Updated 3 min ago" is true only at the instant it renders and reads as staleness on the one surface whose ETag never changes; "· live" moves the liveness claim to where the poll phase actually knows it. Riders for the same touch, if ruled (not second proposals): fold the mechanism into the `title`/`aria-description` ("The hub generated this at <time>; the dashboard re-checks on every change") and have the 304 path refresh the tooltip's cursor from the response header. **Nothing changed in this lane** — DX-22's open question and the named post-gate discriminator stand; the hub rules.

## §6 The NEW-7 (a) rider — what was built, and the discriminator's grounding (Charge 3)

**The finding that shaped it:** `EventsView.tsx:27–:35` at baseline already rendered the calm teaching copy (`events.notServedYet.title/hint` — "Your hub doesn't share the activity feed yet." / "Everything else on this dashboard is live. The feed arrives with a <product> update — nothing is wrong."), keyed on `slug === 'not-found'`. The live 404 never carried that slug (the rehearsal and the sitting both rendered the generic card), so the shipped teaching state was unreachable on the real wire, and a Core-authored problem+json `not-found` on that path — which would mean the endpoint EXISTS — would have rendered "not served yet": wrong in both directions. The rider re-keys it.

**The discriminator, grounded at source — with a correction to the brief's framing, flagged.** The brief keys the teaching state on "`application/json`-not-problem+json". At source that is HALF the story: Core's problems reach the wire by two paths — the exception path serializes as `application/problem+json` (`RestFilters.java:551`, the one `ctx.contentType(...)` for problems), but the ENDPOINT-level path `EndpointResponses.problem()` writes the problem body via `ctx.json()` (`EndpointResponses.java:40–:43`), i.e. `application/json` with a problem-shaped body carrying the ratified type URI (the B3 reads' NOT_FOUND / INVALID_PARAMETERS go this way). So on a ROUTED path the media type alone cannot separate "not in this release" from "not found". What carries the premise is the PATH: `/api/v1/events` has no route in this release, so no handler exists to author a 404 there, and a 404 on it can only be the router's (Javalin's default document and its default `application/json`; no custom 404 handler exists — the `Javalin.create` block at `HomeSynapseCore.java:904` registers none, and no `app.error(...)` appears in any main source). The media type still earns its place — it excludes the exception-path problem+json shape and non-JSON 404s (`text/html`). Hence the path set is the load-bearing term, is consumer-maintained, and MUST SHRINK the moment an endpoint ships (the mock→real swap and that edit are one change — written into `client.ts` as a law). Implemented as `isUnservedEndpoint404(path, status, contentType)` in `client.ts` (`:110` post-change): `status === 404 ∧ FROZEN_UNBUILT_PATHS.has(path) ∧ mediaType(contentType) === 'application/json'`, where `mediaType` strips parameters and lower-cases (a `; charset=utf-8` would not change the verdict) and the path set contains ONLY the observed `/api/v1/events` (B2 `/api/v1/health` was not observed and is composed client-side — not guessed in). The client mints `{ type: 'endpoint-not-in-this-release', title: 'This part of the dashboard is not in this release yet', status: 404, detail: 'The hub does not serve /api/v1/events yet. Nothing is wrong — it arrives with a later update.' }` (name-light, calm; the fallback if any other surface ever renders it generically) and `ApiProblem.isUnservedEndpoint` reads the slug. `EventsView` keys the ALREADY-SHIPPED teaching card on that predicate; every other 404 — problem+json on the same path, `text/html`, a different path — keeps the honest generic card + Try again (the ruling's posture: the design working). The teaching card self-heals: `useApi` keeps refetching on every cursor advance, so the first `200` after a hub update renders the feed with no retry button needed.

**Tests (13):** the pure function fires for the recorded headers on the recorded path; tolerates media-type parameters; does NOT fire for `application/problem+json`, for a missing/`text/plain`/`text/html` content type, for any status but 404, or off the exact path (`/api/v1/events/abc`, `/api/v1/events/`, `/api/v1/runs`, `/api/v1/health`, `/internal/projection`). Through `createClient` with a fake transport: the headers-only fixture → `isUnservedEndpoint` true, status 404, the client slug, none of auth/offline/replaying; the verdict is IDENTICAL for body `null`, a Javalin-like JSON document, an unknown JSON shape, the bare title as text, `''`, and even a problem-SHAPED body under `application/json` (never body-keyed — on an unrouted path nothing could have authored it; pinned so the path-set law above is visible in the suite); a problem+json `not-found` on the same path → slug `not-found`, `isUnservedEndpoint` false; the minted copy is calm and contains no product name. Surface: the observed 404 → the teaching card (no `role="alert"`, no Try again, no spinner); a problem+json not-found → the generic card (`role="alert"`, "Not found", Try again, no teaching copy); a `text/html` 404 → the generic card (no teaching by status alone).

**H8 accounting: REPO-COMPLETE, LIVE-VERIFICATION PENDING THE DEPLOY** — the row rides §8.

## §7 Deviations declared (none silent) + cross-lane asks

1. **Charge 1 census +1 file** (§2): the detector is a sibling `fixtures.stability.test.ts` (pure data, beside the fixture class it guards, open to future captures); the render test extends the view's own suite beside the 08-16 render test it mirrors. Brief said "your call, justified" — this is the call.
2. **Charge 3 census 4 files** vs the brief's +2–3: the headers-only fixture and the suite are separate files by the fixture-class law (one fixture per file, provenance header each).
3. **A behavior change on a never-live-exercised branch:** `EventsView`'s `slug === 'not-found'` teaching arm is REPLACED by the discriminator, so a Core-authored problem+json `not-found` on `/api/v1/events` now renders the generic card. Red-first captured in both directions (§4). The mock transport cannot reach this branch (it always serves `/api/v1/events`), so no mock behavior changes.
4. **Teaching copy kept verbatim** (`events.notServedYet.*`, already in the FE skill's register and stranger-tested at FE-1) rather than the brief's paraphrase "The activity feed endpoint is not part of this release yet"; the brief's phrase is carried by the client-minted fallback title ("…is not in this release yet"). If the hub wants the literal wording on the card, it is a one-line i18n change.
5. **Two pins stricter than the brief's detector definition** — key ORDER and byte size — are separately named tests so the hub can drop either without touching the brief-mandated arms. Their purpose is the fixture-class law (byte-mirroring), not the contract (key order is not contractual).
6. **`timeAgo` / `Freshness` / `poll.tsx` / `RunChainView.tsx` UNTOUCHED** — F-S3 is answered and proposed, not changed (the brief's law).
7. **Gate environment:** the device VM cannot run the checkout's `node_modules` (installed on Windows — the rollup native binary is the win32 one; `vitest` fails to load in the Linux VM), so baseline re-derivation, the red captures, and the final gate ran in the lane's cloud workspace: the dashboard tree tarred from the device (105 entries, `node_modules`/`dist` excluded), `npm ci` from the repo's own `package-lock.json` at `7c9e4fa`, Node 22.22.2, `npm run verify` GREEN end-to-end (tokens-check OK · lint 0/0 · typecheck clean · 210/210 · build · **63.2/100 KB gzip, 36.8 KB headroom** (+0.2 KB vs the NEW-2/3 return's 63.0 — the client additions) · contract-check 11 endpoints v1.1.2). `prebuild` regenerated `tokens.css` byte-identical (checked). **`frontend.yml` on the push remains the CI gate of record** — commands for the record: `cd web-ui/dashboard && npm ci && npm run verify` on the committed tree.
8. **Env-model observation (the index.lock class):** an early plain `git status` on the device mount tried to refresh the index and could not unlink its `.git/index.lock` (the mount forbids unlink), leaving a stale 0-byte lock that would have blocked Nick's next git write. It was MOVED (rename is permitted) to `ClaudeFolder/_scratch/_to_delete/git-index.lock.stale-20260822`; a sibling `index.lock.rev1` from Aug 4 sits there already — the same class. Every later git read used `--no-optional-locks`. **Nick: `_scratch/_to_delete/`, `_scratch/dashboard-7c9e4fa.tgz`, and `_scratch/FRONTEND_DOCTRINE.copy.md` are this lane's scratch — safe to delete.** Hardlinked files (`FRONTEND_DOCTRINE.md`, `DevPanel.tsx`) were read via copies, unmodified (the NEW-2/3 return's dev-9 class).
9. **An external source was read to ground a claim:** Javalin's `ETagGenerator.kt` at the `javalin-parent-6.7.0` tag (GitHub; Maven Central's sources jar is not reachable from the workspace). It is cited as the mechanism's carrier, not copied; the deployed hub's "+1 lawful 304" is the on-record confirmation.
10. **One Edit-tool artifact caught and corrected in-session:** two `' '` join separators in the detector were written as NUL bytes by the authoring tool; detected by grep before any run, replaced, and the file re-verified NUL-free. Disclosed because the fixture-class law is byte-exactness.

Cross-lane asks (FOR THE HUB):

1. **Rule on the F-S3 proposal** (§5 (iii)): relabel `As of <time> · live` — or keep, or the tooltip-only form. The mechanism answer stands regardless.
2. **MODULE_CONTEXT fold rows** (hub-owned, the F-14-row precedent): (i) the non-firing wire has TWO provenance-grade captures across two deployments, and `fixtures.stability.test.ts` is the drift detector — a third capture extends the detector, never the arm count; (ii) the run-detail "Updated" stamp ages BY CONSTRUCTION and only there: the causal chain is the one read with a strong content-constant ETag → `304` → the client's cached `meta` (client.ts 304 path) → the stamp re-renders the first response's generation time; list views' weak position-keyed ETags reset it; (iii) the Activity teaching state is keyed on the wire discriminator (path ∧ 404 ∧ `application/json`-not-problem+json), the `not-found`-slug arm retired; every other 404 is the generic honest card.
3. **Documentation observation for the freeze record (no shape change):** the contract is silent on ETag keying; the live server keys the causal chain STRONG on `runId` and everything else WEAK on `viewPosition` (entities: none). Worth one line in §C so the next consumer does not rediscover F-S3.
4. **Core-side observation, flagged, not an ask:** `ListEntitiesEndpoint` sets no `ETag` (every other read does) — consistent with the observed ticking, no FE impact; the hub may want it on the R-10/consistency docket.
5. **Core-side CONTENT-TYPE observation (flagged, never an FE patch — the contract-consumer law):** `EndpointResponses.problem()` (`EndpointResponses.java:40–:43`) writes endpoint-level problems with `ctx.json()` → `Content-Type: application/json`, while `contract.ts:58` (and Doc 09 §3.8) say non-2xx bodies are `application/problem+json`; only the exception path (`RestFilters.java:551`) conforms. FE impact today: none — `toProblem()` keys on the BODY's `type` slug, never the content type, and the NEW-7 discriminator's premise is carried by the path. A one-line core fix (`ctx.contentType("application/problem+json")` before the `json()` in `problem()`) would make the media type a clean discriminator for every future unbuilt path; routed as an observation for the hub's adjudication, not this lane's act.

## §8 The live re-exercise plan (H8 tier 2 — Nick's next warm deploy, the midweek-deploy packet idiom)

DevTools Network + Console open throughout; L3: crop or mask the `Authorization` line before pasting any header screenshot (F-S1's law).

1. **Never-triggered, before any trigger:** `#/explain/why-not/<current bench-hero ULID>` (re-derive the ULID — it re-mints on re-provision; the 08-20 one was `01M0GPZF…`). Expected: "Nothing set it off" · the explanation sentence · "What would make it run: state change" · NO "Last checked" row · no spinner · no console TypeError. Network: the `…/non-firing` 200 body with `lastEvaluation: null` — paste it as text: a THIRD capture extends the stability detector (`fixtures.stability.test.ts`) with one import, and its byte count should be 395/396 ± the id/position digits. Falsifier: ANY key present in one capture and not another — that is the STATE-DIALECT class reaching this surface, and it files first.
2. **The run-detail stamp, mechanism now KNOWN — what it should read, by source:** open any COMPLETED run (`#/explain/run/<runId>`) and stay 3 min. Expected: "Updated just now" on load; at each subsequent cursor advance the stamp STEPS ("1 min ago" → "3 min ago") and never returns to "just now"; Network shows ONE `200` for the chain, then a `304` for every refetch with request `If-None-Match: "<runId>"` and the `304` carrying a FRESH `X-HomeSynapse-View-Position`. Falsifiers: a `200` on a refetch of the same run (the ETag changed — the chain was regenerated, or Javalin's short-circuit did not fire), or the stamp resetting to "just now". **The list-view residual (§5) in one glance:** on `#/explain/runs`, read the stamp IMMEDIATELY after a `200` lands — "just now" means the clocks agree; "N sec ago" right after a 200 is the Pi↔laptop clock offset, N seconds.
3. **Activity nav (the Charge-3 surface):** `#/events`. Expected: the calm teaching card "Your hub doesn't share the activity feed yet." + hint, no Try again, no alert; Network: the `404` with `Content-Type: application/json`. Falsifier: the generic "Endpoint GET /api/v1/events not found" card + Try again (the discriminator did not fire — read the content type first: `application/problem+json` means the GENERIC card is the CORRECT rendering and the premise, not the code, moved; `text/html` means the router's 404 changed shape). The other falsifier runs the other way: a `200`, or a 404 with a problem-shaped `application/json` body on this path, means Core now ROUTES `/api/v1/events` — the B1 swap is due and `/api/v1/events` leaves `FROZEN_UNBUILT_PATHS` in the same change (the teaching card would be a lie from that moment). While here, optionally save the 404 body as text (still NOT needed by the code; it would become its own fixture, never a key).
4. **Cross-surface:** the header stamp keeps ticking on every LIST surface visited after 1–3 — the poll loop survived everything (the 2026-07-27 signature absent).

**This lane's scope was repo-only — no deploy was performed or attempted. The Activity teaching card concludes REPO-COMPLETE, LIVE-VERIFICATION PENDING THE DEPLOY, in those words.** The WhyNot surface's CODE is unchanged by this lane (fixture + tests only); its VERIFIED-LIVE status from the 2026-08-20 record stands, and row 1 above re-exercises the stability claim rather than the surface.

## §9 Accessibility + stranger test

No new visual state was introduced: the Activity teaching card is the SHIPPED `EmptyState` (title + hint, calm register, no alarm role — nothing is wrong, so no `role="alert"`); the generic card keeps `role="alert"` + a real retry. The one new copy string (the client-minted fallback title/detail) reads aloud to a stranger as intended — "This part of the dashboard is not in this release yet. The hub does not serve /api/v1/events yet. Nothing is wrong — it arrives with a later update." — name-light (test-pinned: no product name), no positioning claim, no jargon beyond the path a fallback card legitimately names. No token, theme, contrast pair, or component changed; the a11y suite ran green in the gate.

## §10 Decisions / defaults taken (explicit + revisable)

1. **Detector placement:** sibling file beside the fixtures; the render test in the view's suite (§7 dev-1).
2. **Discriminator placement:** the client's non-2xx branch (the transport boundary is where status + content-type + path coexist), minting a typed client-side problem with a bare slug — the `network-unreachable` / `internal-error` precedent — consumed by a predicate, so views never parse headers.
3. **Path set = observed paths only** (`/api/v1/events`); adding B2 would be a guess. Exact-match, not prefix.
4. **Media-type parse** strips parameters and lower-cases; a bare `application/json` is the only affirmative.
5. **The shipped teaching copy kept**; the minted fallback copy authored in the same register.
6. **Filing-day date = 2026-08-21** (America/Chicago, 20:50 CDT at filing; the machine's UTC date is already 08-22).

## §11 Next recommended work unit (refuse-to-close)

**FE-STATE-DIALECT (FE-LIVE-V112 item (h))** — unchanged from the NEW-2/3 return and now carrying its first live operator observation (F-S2): consume the `/state` dialect at the `parseInstant` seam with fixture-locked detection, retiring the honest degradation on the device drawer. The stability detector filed here is the pattern to reuse there: two real captures of `/state`, one per deployment, and a detector that names the dialect axes (epoch-second instants · `{"value":…}` nesting · `{msb,lsb}` ids) explicitly. If the hub rules the F-S3 relabel, it is a half-day rider on whichever FE touch comes first.

## §12 Route-back

Intakes at the hub for two-layer audit; the deploy + live re-exercise ride the next Pi trip.
