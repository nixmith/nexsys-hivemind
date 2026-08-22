<!--
file: context/audits/2026-08-22_FE-SWAP-CENSUS_return.md
purpose: FE-SWAP-CENSUS return — the brand-token reach census, run read-only BEFORE the word, per `context/instructions/2026-08-22_FE-lane_SWAP-CENSUS_brand-token-reach_brief.md`. Every working-name hit in the FE lane's corpus enumerated at file:line, classified IN / OUT / REACHED with its reason, the reach map for every human-visible surface, the H+2–6 flip WU pre-authored as a Files table, and a ≤10-min OPERATOR dry-run block for Nick.
audience: the hub (intake + the flip-WU authoring at H+0–2) + Nick (§5, optional).
lane: FE (`/nexsys-frontend`), read-only.
census commit of record: homesynapse-core `89a912e`; porcelain EMPTY at open AND at close.
fences honored: no edits under `web-ui/`; no branch, no stash, no commit, no build in the lane; no candidate name anywhere ({{NAME}} / ZZ-PLACEHOLDER only); the working name stays on every surface; the D-1 DO-NOT-SAY items quoted ONLY to mark them OUT.
filed: 2026-08-22.
-->

# FE-SWAP-CENSUS — the brand-token reach census (read-only; before the word)

## §0 The one paragraph

**N = 71 working-name hits across 33 files** (union of the runbook instrument and the shape-level sweep; `package-lock.json` excluded and counted separately). **K = 7 IN across 3 files · M = 64 OUT across 31 files · R = 14 REACHED sites across 6 files.** The REACHED sites are invisible to every grep in the runbook — they are `${BRAND.productName}` compositions, which is the architecture working as designed (FE-3 / D-FE-9 / W-11). **The misses the token cannot reach today are exactly five lines in two files:** `index.html:9` (`<title>`) and `index.html:30` (`<noscript>`) — static by doctrine, painted before the bundle parses — plus `README.md:1`, `:3`, `:414`, a markdown file with no JS at all. **There is no manifest, no PWA, no favicon, no `og:`/`apple-` meta, no 404/offline page, and no footer legal line in this repo — those hit classes do not exist to miss.** Zero split/spaced/hyphenated/lowercased variants exist anywhere. **The flip WU stages exactly 4** (3 edits + 1 new test) in FE territory; `npm run verify` and `frontend.yml` both predict GREEN. **Two findings outrank the count.** (1) **The runbook §2's "red-first where a test exists (the brand-token test flips first)" has NO TARGET** — the only token-touching test imports `BRAND` and is therefore flip-invariant; the flip is currently ungated by any assertion (§4b). (2) **The flip WU as the runbook scopes it crosses the FE lane's write territory** — `README.md` is repo-root, and the FE lane writes only under `web-ui/dashboard/` (§4d). Both need a hub word at H+0–2, before the WU is authored. Sections: §1 the census · §2 the classification · §3 the reach map · §4 the flip WU · §5 the dry-run block · §6 harvest.

---

## §1 The census

### (a) The runbook's instruments, verbatim

```
git -C homesynapse-core grep -li "homesynapse" -- "web-ui/dashboard/src" "web-ui/dashboard/index.html" "README.md"
```
→ **25 files.** Then the line-level form (`grep -n -i`, same pathspec) → **54 lines.**

The runbook §2 expects ≈ 21; the hub's pre-run at `89a912e` counted 25. **The census re-confirms 25 files / 54 lines at `89a912e`** — the hub's number, not the runbook's. Split: `README.md` 25 · `index.html` 2 · 23 `src/` files 27.

### (b) The sweep the instrument cannot see

Each row is a grep actually run and recorded. **The instrument's pathspec is the first miss**: it covers `src/` and `index.html` but not the rest of the module.

| Sweep | Instrument | Result |
|---|---|---|
| The instrument's pathspec gap | `git grep -li "homesynapse" -- "web-ui/dashboard" ":!…/package-lock.json"` | **32 files** — 8 files the runbook grep never sees: `FRONTEND_DOCTRINE.md` · `MODULE_CONTEXT.md` · `README.md` (module) · `build.gradle.kts` · `package.json` · `scripts/build-tokens.mjs` · `scripts/contract-check.mjs` · `vite.config.ts` (**17 lines**) |
| Composition (`${BRAND.productName}`) | `git grep -n "BRAND" -- "web-ui/dashboard" ":!…/package-lock.json"` | **14 render/consume sites, 6 files** — all invisible to (a) |
| `document.title` / `<title>` | `git grep -n -iE "document\.title\|<title>\|useTitle\|setTitle"` | `main.tsx:13` (token-fed) · `index.html:9` (static) |
| Manifest / PWA / `short_name` / `start_url` / `apple-mobile-web-app-title` / `og:` / favicon | `git grep -n -iE "manifest\|og:title\|og:site_name\|apple-mobile-web-app\|short_name\|start_url\|favicon"` | **ZERO hits.** Corroborated by `git ls-files … \| grep -iE "manifest\|favicon\|icon\|\.svg\|\.png\|\.ico\|404\|offline\|robots\|webmanifest"` → **no tracked asset**, and `index.html` carries exactly four `<meta>`s (charset, viewport, color-scheme, theme-color) and **zero `<link>`s**. No SVG app-icon exists, so no SVG text to census. |
| `aria-label` / `alt` / `title=` | `git grep -n -iE "aria-label\|[^a-z]alt=\|title="` | 10 a11y sites audited (`AppShell:34` · `CausalChain:58` · `DevPanel:41,44,52,68,91` · `Drawer:43,49` · `ThemeToggle:56`) — **none carries the product name** |
| Footer / legal / copyright | `git grep -n -iE "footer\|copyright\|©\|legal\|all rights" -- src` | CSS class names + `AppShell.tsx:57–64` only (ThemeToggle, phase pill, Disconnect) — **no legal line, no name** |
| `package.json` name | `grep -n '"name"'` | `:2 "name": "@homesynapse/dashboard"` (+ `package-lock.json:2,:8`, excluded from N) |
| Tests asserting the name | `git grep -n -iE "BRAND\|productName\|homesynapse" -- "**/*.test.ts" "**/*.test.tsx"` | 3 files, 5 lines — **all analyzed at §4b** |
| Split / spaced / hyphenated / lowercased | `git grep -n -i` × 8: `home synapse` · `home-synapse` · `home_synapse` · `Home Synapse` · `HOME SYNAPSE` · `homeSynapse` · `hsynapse` · `synapse` (last filtered `-v homesynapse`) | **ZERO hits on every pattern.** "synapse" never appears except inside the closed compound. |
| D-1 fence text in the FE tree | `git grep -n -iE "runs integrations\|publishes events\|packaged artifact" -- "web-ui/dashboard"` | **ZERO.** The two DO-NOT-SAY items — *"the packaged artifact runs integrations"* / *"the packaged artifact publishes events"* — do not live in the FE corpus. The FE flip cannot touch them by construction. |

**Union of (a) + (b): N = 71 lines / 33 files** (54 + 17 = 71 ✓; 25 + 8 = 33 ✓).

---

## §2 The classification

### IN — renders the product name to a human; renames at the flip (**K = 7 lines / 3 files**)

| file:line | matched text | reason (≤ 12 words) |
|---|---|---|
| `web-ui/dashboard/src/lib/i18n.ts:18` | `productName: 'HomeSynapse',` | **The token.** Single source; all 14 REACHED sites follow it |
| `web-ui/dashboard/src/lib/i18n.ts:5` | `is unratified, so the value stays "HomeSynapse"` | Same-file comment states the value; flip makes it false |
| `web-ui/dashboard/index.html:9` | `<title>HomeSynapse</title>` | **Token cannot reach:** painted pre-JS, before the bundle parses |
| `web-ui/dashboard/index.html:30` | `<noscript>HomeSynapse dashboard requires JavaScript.` | **Token cannot reach:** the no-JS path never runs `main.tsx` |
| `README.md:1` | `# HomeSynapse Core` | Public README product reference; runbook §1 IN row |
| `README.md:3` | `The on-device runtime for HomeSynapse — a local-first…` | Public README product reference; runbook §1 IN row |
| `README.md:414` | `The consumer-facing product name is also under trademark review` | The rename note itself; stale tense the moment R-1 fires |

**The token-unreachable class, enumerated as the brief charges (5 lines / 2 files):** `index.html:9`, `index.html:30`, `README.md:1`, `README.md:3`, `README.md:414`. These five are the entire H+36–48 "ZERO working-name hits on IN-scope surfaces" surface. Nothing else in the FE corpus can miss.

### REACHED — already flows from `BRAND.productName`; no edit (**R = 14 sites / 6 files**)

| file:line | site | what renders |
|---|---|---|
| `src/lib/i18n.ts:25` | `'auth.tokenHelp'` | `…pairing token from your ${BRAND.productName} device.` |
| `src/lib/i18n.ts:26` | `'boot.startingBody'` | `${BRAND.productName} is catching up to live…` |
| `src/lib/i18n.ts:27` | `'devices.lede'` | `Everything ${BRAND.productName} can see in your home.` |
| `src/lib/i18n.ts:28` | `'health.live'` | `${BRAND.productName} is up to date and processing events…` |
| `src/lib/i18n.ts:29` | `'overview.live'` | `${BRAND.productName} is live and watching your home…` |
| `src/lib/i18n.ts:30` | `'overview.catchingUp'` | `${BRAND.productName} is catching up after a restart…` |
| `src/lib/i18n.ts:31` | `'hero.permanence'` | `…rebuilt from ${BRAND.productName}’s permanent activity log…` |
| `src/lib/i18n.ts:32` | `'origin.external.phrase'` | `outside ${BRAND.productName}` |
| `src/lib/i18n.ts:35` | `'events.notServedYet.hint'` | `…arrives with a ${BRAND.productName} update — nothing is wrong.` |
| `src/main.tsx:13` | `document.title = BRAND.productName;` | The live tab title |
| `src/components/AppShell.tsx:36` | `<span class={styles.dot} /> {BRAND.productName}` | The sidebar wordmark slot |
| `src/components/AuthGate.tsx:23` | `<div class={styles.brand}>{BRAND.productName}</div>` | The pairing-screen wordmark |
| `src/lib/api/mock/mockData.ts:466` | `` summary: `Kitchen Light changed outside ${BRAND.productName}` `` | Mock fixture copy (mock-builds only) |
| `src/lib/format.test.ts:46` | `` .toBe(`outside ${BRAND.productName}`) `` | Token-relative assertion — **flip-invariant, see §4b** |

### OUT — a technical identifier or a record that NEVER renames (**M = 64 lines / 31 files**)

| Class | file:line | matched text | reason (≤ 12 words) |
|---|---|---|---|
| Wire identifier | `src/lib/api/contract.ts:59`, `:76` · `contract.test.ts:56`, `:63` · `scripts/contract-check.mjs:15` | `https://homesynapse.local/problems/` | Pinned to Core `ProblemType.java:160`; renaming breaks the wire |
| Wire header | `fixtures/wire-2026-08-16-nonfiring.ts:7` · `fixtures/wire-2026-08-20-never-triggered.ts:13` | `X-HomeSynapse-View-Position` | Verbatim historical capture under byte-size pins; editing reddens the detector |
| npm identifier | `package.json:2` (+ `package-lock.json:2`, `:8`) | `"@homesynapse/dashboard"` | Runbook §1 OUT: package name is not the brand |
| npm metadata | `package.json:6` | `"HomeSynapse Core — V1 Observability Dashboard…"` | `private: true`; never published, never rendered anywhere |
| Gradle / JPMS | `build.gradle.kts:6`, `:29` | `homesynapse.java-conventions`, `app/homesynapse-app` | Plugin id and module path; runbook §1 OUT identifiers |
| Negative test literal | `src/views/EventsView.unserved404.test.tsx:153` | `.not.toContain('HomeSynapse')` | **OUT by class, but goes false-green on flip — §4b** |
| Source-header banners (19 files, 20 lines) | `client.ts:2` · `contract.ts:2` · `endpoints.ts:2` · `api/index.ts:2` · `mockData.ts:2` · `mockState.ts:2` · `mockTransport.ts:2` · `scenarios.ts:2` · `realTransport.ts:2` · `shapes.ts:2` · `auth.ts:2` · `format.ts:2` · `poll.tsx:2` · `router.ts:2` · `verdicts.ts:2` · `global.css:2` · `tokens.css:2` · `tokens.dtcg.json:2` · `build-tokens.mjs:3`, `:125` · `vite.config.ts:4` | `HomeSynapse — <subject>` | Internal source comment; no user surface; **census-ruled, see below** |
| Module docs | `FRONTEND_DOCTRINE.md:2,3,5,9,29` · `MODULE_CONTEXT.md:13,20,59` · `web-ui/dashboard/README.md:1` | prose | Repo record; runbook §1: history is never rewritten |
| Root README identifiers (22 lines) | `README.md:46,55,56,59,60,62,78,192,206,207,208,211,213,220,225,258,259,260,266,341,403` | `HOMESYNAPSE_HOME`, `/var/lib/homesynapse`, `homesynapse.yaml`, `homesynapse-events.db`, `homesynapse.service`, `com.homesynapse.app.Main`, `HomeSynapseConfig`, `homesynapse-core-docs` | Env vars, paths, service unit, JPMS, class, repo slug — all OUT |
| Legal header sample | `README.md:371` | `* HomeSynapse Core` (inside a copyright block) | Runbook §1 OUT: LICENSE/legal headers are their own act |

> **Census ruling the hub must ratify (it sets what "ZERO" means at H+36–48).** The 19-file **source-header banner class** is classified **OUT**: a `/* HomeSynapse — Typed API client. */` banner is neither a human-visible surface (so not IN) nor a technical identifier (so not literally the brief's OUT wording). It is the *internal working name*, which the runbook's own OUT rationale covers ("the internal working name is not the brand"). Flipping 20 comment lines buys zero user value and inflates the flip diff tenfold. **Consequence if the hub overturns:** the flip WU grows from 4 files to 23, and `tokens.css:2` becomes a trap — it is GENERATED, so it must change at `scripts/build-tokens.mjs:125` and be regenerated, never hand-edited, or `npm run tokens:check` (verify step 1) goes RED.

---

## §3 The reach map

| Human-visible surface | Render site (component file:line · prop/attribute) | Reads `BRAND.productName` today? |
|---|---|---|
| Tab title (JS path) | `src/main.tsx:13` — `document.title = BRAND.productName` | **YES** |
| Tab title (pre-JS / no-JS) | `index.html:9` — `<title>` element text | **NO — static.** The browser paints this on every cold load before the bundle parses |
| No-JS fallback body | `index.html:30` — `<noscript>` text | **NO — static** |
| App header / wordmark slot | `src/components/AppShell.tsx:36` — text node after `<span class={styles.dot}/>`, inside `class={styles.brand}` | **YES** |
| Pairing / login screen | `src/components/AuthGate.tsx:23` — `<div class={styles.brand}>` child text | **YES** |
| Explain surface (the hero) | `src/components/CausalChain.tsx:186` — `<p class={styles.permanence}>{t('hero.permanence')}</p>` | **YES** (via `i18n.ts:31`) |
| Boot / catching-up state | `src/components/feedback.tsx:54` — body text after `<strong>Starting up.</strong>` | **YES** (`:26`) |
| Overview lede | `src/views/OverviewView.tsx:32` — `{live ? t('overview.live') : t('overview.catchingUp')}` | **YES** (`:29`, `:30`) |
| Devices lede | `src/views/DevicesView.tsx:34` — `<Page lede={…}>` prop | **YES** (`:27`) |
| Health plain-language | `src/views/HealthView.tsx:19` — `plain:` field on the status meta | **YES** (`:28`) |
| Activity teaching card | `src/views/EventsView.tsx:36` — `<EmptyState hint={…}>` prop | **YES** (`:35`) |
| Origin "outside …" phrase | `src/lib/format.ts:190` — `phrase:` field on `originMeta('EXTERNAL')` | **YES** (`:32`) |
| Auth token help copy | `src/components/AuthGate.tsx:26` — `<p class={styles.lede}>` child | **YES** (`:25`) |
| Error / empty states | `feedback.tsx` (`EmptyState`, `ErrorCard`), `a11y.test.tsx:69` exemplar | **n/a — none carries the product name** |
| Footer | `src/components/AppShell.tsx:57–64` — ThemeToggle · phase pill · Disconnect | **n/a — no name, no legal line** |
| Manifest / PWA install prompt | — | **DOES NOT EXIST** (no webmanifest, `short_name`, or `start_url`) |
| Favicon / app icon | — | **DOES NOT EXIST** (zero tracked icon files; no `<link rel="icon">`) |
| `og:title` / `og:site_name` | — | **DOES NOT EXIST** |
| 404 / offline page | — | **DOES NOT EXIST as a page** — offline is the in-app `AppShell` phase |

**The 16-px / tab-title legibility note for B-1** (reach only — BRAND-SPRINT-1 owns the identity):

- **The pairing screen is the tightest constraint on any surface, and it is not the tab title.** `AuthGate.module.css:22–28` renders the name at `--hs-text-sm` = **0.8125rem ≈ 13 px**, `text-transform: uppercase`, `letter-spacing: 0.02em`, `color: var(--hs-text-secondary)` — a de-emphasized, tracked, all-caps 13-px setting. This is the **first** surface a stranger sees (pre-auth). B-1 must letter-test the ruled name at 13 px uppercase with 2% tracking, in **both** themes, against a secondary-text color.
- **The sidebar wordmark is the roomiest slot:** `AppShell.module.css:14–20` = `--hs-text-md` **1.0625rem ≈ 17 px**, `weight-semibold`, sentence case, paired with a `.dot` glyph. Comfortably above the 16-px floor.
- **The tab title has no CSS reach at all** — the browser chrome sets it (~11–12 px, OS-dependent, truncated hard in a narrow tab). It renders **twice under different values** until the bundle parses: `index.html:9`'s static string first, then `main.tsx:13`'s token. Post-flip these agree; **pre-flip a partial edit would show the new name flashing to the old one**, which is why `index.html:9` is IN and non-optional.
- **Both wordmark slots are plain text nodes** — no SVG lockup, no image, no `alt` text anywhere. A wordmark drop-in replaces one text node per slot; nothing in the census over-invests in a lockup (W-11 discipline holding).

---

## §4 The flip WU, pre-authored (a Files table, not code)

### (a) The Files table — FE territory (`web-ui/dashboard/**`)

| File | Delta (one line) | Class |
|---|---|---|
| `web-ui/dashboard/src/lib/i18n.ts` | `:18` `'HomeSynapse'` → `'{{NAME}}'`; `:5` comment's quoted value → `{{NAME}}` and its "unratified" tense → ratified-at-R-1 | M |
| `web-ui/dashboard/index.html` | `:9` `<title>` text → `{{NAME}}`; `:30` `<noscript>` leading word → `{{NAME}}` | M |
| `web-ui/dashboard/src/views/EventsView.unserved404.test.tsx` | `:153` literal `'HomeSynapse'` → `BRAND.productName` (+ the `i18n` import) — keeps the name-light assertion live under any name | M |
| `web-ui/dashboard/src/lib/i18n.test.ts` | **NEW** — the positive token pin the repo lacks: `expect(BRAND.productName).toBe('{{NAME}}')` + one render assertion each on `AppShell` and `AuthGate` | A |

**The census count for the commit message: "stages exactly 4" (3 M + 1 A).** Drop the new pin and it is 3; drop the false-green fix too and it is 2 — but §4b argues both belong.

### (b) The brand-token test — quoted by name and file

The runbook §2 says the flip is *"census-exact, red-first where a test exists (the brand-token test flips first)."* **The census finds no such test.** The only token-touching assertion is in `src/lib/format.test.ts`, inside `it('never leaves origin a silent blank — UNKNOWN is an honest value')`:

```ts
// src/lib/format.test.ts:46
expect(originMeta('EXTERNAL').phrase).toBe(`outside ${BRAND.productName}`);
```

It **imports** `BRAND` (`format.test.ts:22`), so both sides of the equality move together. **It cannot go red on a flip and cannot gate one.** The second literal is a *negative* assertion:

```ts
// src/views/EventsView.unserved404.test.tsx:153
expect(p.problem.title + (p.problem.detail ?? '')).not.toContain('HomeSynapse');
```

After the flip this still **passes** — and stops testing what it means to test (that the minted `endpoint-not-in-this-release` copy is name-light). A silent false-green, in the one suite whose whole subject is honest copy. Hence rows 3 and 4 of the Files table: **fix the false-green, and add the positive pin the red-first discipline assumes** — authored RED against the working name in the WU's first commit, green on the second.

### (c) Gate predictions

**`npm run verify` → GREEN**, step by step: `tokens:check` (neither `tokens.dtcg.json` nor `tokens.css` is touched — no drift) → `lint` (a string-literal change; no eslint rule keys on it) → `typecheck` (**checked**: `BRAND` is `as const`, so `productName`'s *literal type* changes; `git grep -nE ": *'HomeSynapse'|<'HomeSynapse'>|typeof BRAND"` returns only the declaration itself — **zero annotations or narrowings depend on the value**) → `test` (210/210 today; +n with the new pin) → `build` → `check:bundle` (63.2 / 100 KB gzip at the last green; a name-length delta is bytes) → `check:contract` (11 endpoints, `v1.1.2-2026-07-26`; its `EXPECTED_PROBLEM_PREFIX` is untouched).

**`frontend.yml` → GREEN on the push.** The path filter is `web-ui/dashboard/**` and all four staged files match, so the job triggers; budget and contract steps are unaffected. The gate exists identically at `.github/workflows/frontend.yml` and `web-ui/dashboard/ci/frontend.yml` (**diff: byte-identical** — verified). **Watch:** the README lines below do **not** match the path filter on their own; a README-only commit fires no frontend gate at all.

### (d) The write-territory finding (needs a hub word at H+0–2)

The runbook §2 H+2–6 puts *"enumerated README lines"* in the FE flip WU. **The FE lane writes only under `web-ui/dashboard/`** (skill §3 item 3 / §7). `README.md:1`, `:3`, `:414` are repo-root. Two lawful shapes, hub's call: **(i)** the hub rules a named cross-territory exception for this WU and the count becomes *"stages exactly 7"*; or **(ii)** the README lines split into their own hub/core-lane commit and the FE WU stays *"stages exactly 4"*. **Recommendation: (ii)** — it keeps write-isolation intact, and the two commits are independent (no test, no gate, and no render couples them).

### (e) What the WU must NOT touch (the runbook §3 fence)

- **The two D-1 DO-NOT-SAY sentences** — *"the packaged artifact runs integrations"* and *"the packaged artifact publishes events"* — stand VERBATIM until R-4 lifts them. **Census result: ZERO occurrences in the FE corpus**, so the code flip cannot reach them; the fence binds the WU's commit message and any prose it writes.
- **`https://homesynapse.local/problems/`** at `contract.ts:59`,`:76` · `contract.test.ts:56`,`:63` · `contract-check.mjs:15` — pinned to Core `ProblemType.java:160`. Renaming it reddens `check:contract` and breaks the wire. **The loudest OUT in the census.**
- **`X-HomeSynapse-View-Position`** at `wire-2026-08-16-nonfiring.ts:7` · `wire-2026-08-20-never-triggered.ts:13` — byte-exact historical captures under `fixtures.stability.test.ts` byte-size pins. Editing either turns that suite RED — the detector working correctly.
- **`@homesynapse/dashboard`** (`package.json:2`, `package-lock.json:2`,`:8`) · **`homesynapse.java-conventions`** / **`app/homesynapse-app`** (`build.gradle.kts:6`,`:29`) · every root-README env var, path, unit file, JPMS package, class name and repo slug (§2's OUT table).
- **`src/styles/tokens.css:2`** — GENERATED. Never hand-edit; `npm run tokens:check` is verify step 1.
- **Any claim language anywhere.** The rename buys zero new claims.

---

## §5 The local dry-run block — OPTIONAL, for Nick, ≤ 10 min

> **Nothing here is pushed, committed, or shown to anyone.** It never touches the Pi, the bench, the deploy path, or `main`. It sets a PLACEHOLDER — never a candidate name — proves the token's reach with your own eyes, and restores the tree.

**WHERE: your host checkout, `homesynapse-core/web-ui/dashboard/`. Node 20.x. One act per line.**

```
1.  cd <your-checkout>/homesynapse-core
2.  git --no-optional-locks status --porcelain          # ⏺ EMPTY before you start; if not, stop here
3.  cd web-ui/dashboard
4.  npm ci                                              # skip if node_modules is already current
5.  # edit src/lib/i18n.ts line 18 ONLY:  productName: 'ZZ-PLACEHOLDER',
6.  npm run build                                       # prebuild regenerates tokens.css — expected byte-identical
7.  npm run preview                                     # serves at http://localhost:4173/dashboard/
8.  # walk the §3 checklist below in the browser, then Ctrl-C the preview server
9.  cd <your-checkout>/homesynapse-core
10. git checkout -- web-ui/dashboard/
11. git --no-optional-locks status --porcelain          # ⏺ EMPTY
```

**The screenshot checklist (step 8) — ⏺ each.** Expect ZZ-PLACEHOLDER at: the **sidebar wordmark** · the **pairing screen name** (open a private window, or Disconnect, to see it) · the **tab title once the app has loaded** · the **Devices lede** · the **Overview live/catching-up line** · the **Health live sentence** · the **hero permanence sentence** on any run detail · the **Activity teaching card**. Expect the **working name still showing** at: the **tab title during the first paint, before the bundle parses** (hard-reload with the Network tab throttled to see it) and the **`<noscript>` text** (disable JavaScript and reload). **Those two are the known misses — §2 already caught them, and seeing them is the block working.** ⏺ **A surface showing the working name that is NOT one of those two is a finding: paste it — the census missed a render site.**

**STOP-gate (its own block).**
```
If step 11's porcelain is NOT empty → STOP. Do not build, do not commit, do not
continue. Paste the porcelain output as-is to the hub.
(Most likely cause: step 6's prebuild regenerated src/styles/tokens.css to
non-identical bytes — which is itself a finding worth the stop.)
```

---

## §6 Harvest

1. **The runbook's own census instrument under-covers its own module by 8 files / 17 lines** — its pathspec stops at `src/` + `index.html`. Harmless here (all 17 are OUT), but the H+36–48 sweep should run the module-wide form or it will report a "zero" it did not measure.
2. **The red-first discipline the runbook assumes has no target** — the sole token-touching test imports `BRAND` and is flip-invariant. The flip is ungated today; the fix is one new file (§4a row 4).
3. **A negative-literal assertion goes false-green on rename** — `EventsView.unserved404.test.tsx:153`. The general form worth banking: *an assertion that a literal is ABSENT survives the rename of that literal and silently stops testing.* Worth a grep across the corpus at any future rename.
4. **The flip WU as scoped crosses the FE lane's write territory** (root `README.md`). Needs a hub word before authoring, not during.
5. **The token architecture holds** — 14 of 19 name-rendering sites flow from one line, and the 5 that do not are static-by-doctrine and were already documented as such (`MODULE_CONTEXT.md:49`). W-11 is register-verified, not just claimed. The one growth edge: the standing §4e-7 favicon rider — when a `/dashboard/`-scoped icon lands it mints a NEW token-unreachable IN surface (filename + any SVG text), so it should ship post-flip or carry the ruled name.

**Census commit of record: `89a912e`. Porcelain EMPTY at open and at close. No branch, no stash, no edit, no build in the lane.**

**Next recommended WU:** *FE-SWAP-FLIP* — the H+2–6 code flip, authored from §4's Files table, held INERT until the R-1 word; its §4b test rows are authorable NOW against the working name (the pin's red arm is what proves it gates), if the hub wants the gate in place before H-hour.
