<!--
file: context/audits/2026-07-03_website-lane_return.md
purpose: Lane return — the website lane (gate 4's open half): SSG bring-up (ruled), the launchable site skeleton from the content canon, and the R-3 developer/integrations page. The write-isolated frontend lane's ONE return file to the v15 hub.
audience: the Core/PM hub (two-layer audit + folds; one refutation to fold; rulings to note); Nick (deletes the stale index.lock, runs the host gate, commits).
state-type: lane return (audit)
status: RETURNED 2026-07-03. Lane baseline at start: core cf3733e · docs 1509b34 · hivemind re-derived e81a22a (beat-57 committed) — per the brief. Core HEAD UNMOVED through closeout (re-verified; no baseline shift occurred, so the §7 baseline-shift protocol never triggered). Preflight: PASS (all 8 checks; mirror byte-identical; the hivemind VM porcelain flags were the known truncated-tail mount artifact, host tails verified intact).
write-isolation: honored — writes under homesynapse-core-docs/website/** + this file + one cross-agent note append + 2 _scratch/ commit messages. ZERO core-repo writes (the planned 1-line rider is REFUTED, §6 — even the single sanctioned core touch turned out not to be needed). No spine edits, no commits (Nick commits host-side), no CI files added or modified (§8 is a proposal only). No Core run, no token minted, no secrets anywhere in the change set.
-->

# Website Lane Return — the site skeleton is up (Astro, ruled), the developer page ships truthful

**Bottom line.** The SSG ruling is on record (Astro; built in the docs repo at `website/site/`), the skeleton builds green in one command (6 pages, zero-JS enforced, shared tokens consumed cross-repo), the landing is built out inside the D-4 IA, the three stubs render as short honest public pages, and the R-3 developer page ships in the truthful "SDK maturing — the adapter contract is frozen and documented" posture with a complete claim→truth table (§4). Second-checking the brief per Nick's instruction surfaced one refuted premise (the dist-gitignore rider — §6) and three prompt-vs-source corrections (§5). Zero unsourced claims ship; gate 4 is NOT declared closed (hosting/deploy are out of this lane's scope).

## 1. Ruling record (the §1 veto-or-default gate — Nick, 2026-07-03, in-session)

- **SSG = Astro** (default confirmed, no veto). Scaffold pinned to **Astro ^5.18** deliberately: the 5.x line runs **Vite 6 — the dashboard's exact build tool** (the master plan §1.3 differentiating rationale). Astro 6/7 (current latest 7.0.6) ride Vite 7/8; that bump should be coordinated with the dashboard's Vite, never taken silently. `@astrojs/preact` (the component-sharing/live-hero-embed seam) is deliberately NOT installed yet — it lands with the first real island (D-FE-6 gates the hero embed on real-device-data demo-readiness); the skeleton needs no framework JS at all.
- **Location = `homesynapse-core-docs/website/site/`** (Nick ruled option 1 — the docs repo, alongside the canon it renders, in the ruled 2026-06-12 content venue; zero tree-sharing with the M9.2 CC lane; marketing churn stays out of core's history and CI).

## 2. What was built (re-derivable counts)

**Pages: 6 rendered routes** — `/` (landing, built out) · `/config-superiority/` (reviewer-grade canon, rendered; content edits = name-tokenization only, 3 lines) · `/explainability/` · `/no-cloud-account/` · `/ledger-gap/` (short honest public versions; Increment-2 planning stubs preserved verbatim in-file) · `/developers/` (NEW — §4).

**Site scaffold: 19 files** under `website/site/` (verify: `find website/site -type f -not -path "*/node_modules/*" | wc -l` = 19): config (5: package.json, package-lock.json, astro.config.mjs, tsconfig.json, .gitignore) · src (9: content collection config, brand + route modules, site.css, Base layout, ThemeToggle component, 2 page components, README counted below) · plugins (3: brand substitution, provenance-comment stripping, canon-link rewriting) · scripts (2: shared-source preflight, zero-JS gate) · README.md (ruling record + defaults + publish gates).

**Components: 2** (.astro): `Base` (Calm Canvas shell: header/wordmark/nav/canvas/footer) + `ThemeToggle` (dark/light/system, vanilla inline JS, text+shape state). **Canon edits: 6 files** (index.md built out; 3 stubs rewritten short-honest; config-superiority name-tokenized; README.md map/open-items updated). **Canon new: 1** (pages/developers.md).

**What the build does by construction** (each verified in the built output, §7): name-light `{{productName}}`/`{{companyName}}` substitution from ONE brand module (W-11/D-FE-9 mirror — rename = 2 values in 1 file); provenance comments stripped from every rendered page ("strip at publish," automated); canon `.md` links rewritten to routes via one route map; the dashboard's GENERATED `tokens.css` + self-hosted Inter subset consumed cross-repo (sibling checkout, loud preflight failure if absent — pointer-not-copy, zero drift); zero-JS-by-default ENFORCED as a postbuild gate (no script bundles may be emitted); `noindex` on every page until the W-5 publish gate.

## 3. D-4 conformance note (which surface leads with what, and why)

- **Landing (mainstream-facing):** leads reliability ("A smart home that works. Every time. For years.") → works-together → ownership. Privacy present ("Yours"), never the headline. **"Plug-and-play" deliberately absent — the W-4 install-story embargo overrides D-4's generic phrasing** (the tense-truth gate; the landing's Increment-1 copy already complied and stays compliant).
- **The segment fork is one section on the shared landing** (§Who it's for): mainstream → "just works"; prosumers/HA-refugees → the dossier receipts; developers → `/developers/`. **Segments diverge AFTER one truthful landing, not via duplicate sites** (the brief's §2.4 requirement, literally implemented as IA).
- **Prosumer/EU privacy lead lives exactly one place:** `/no-cloud-account/` — privacy-forward framing with the named, dated regulation tooth (Data Act, Regulation (EU) 2023/2854, applicable since 2025-09; CRA deliberately not cited — its obligations post-date publish horizons and belong to the REC-174 dated page).
- **Developer surface:** Register A, reliability-of-contract lead (the L-12 spine) — the segment rule's correct register for that audience.

## 4. The developer page (R-3) + the claim→truth table

Posture shipped verbatim: **"SDK maturing — the adapter contract is frozen and documented"** (assessment §3 watchlist item 2). Voice: L-12 — breaking changes are a contract. The page's own provenance appendix carries the full per-claim sourcing; the load-bearing rows, consolidated:

| # | Claim (as shipped) | Shipped-truth source |
|---|---|---|
| 1 | Two interfaces + optional command handler; 4 required methods + 4 optional hooks; frozen; additive-only since freeze | 2026-07-02 extensibility assessment §1 (IntegrationFactory 2m + IntegrationAdapter 4+4 AMD-55 hooks + optional CommandHandler; frozen M4.C, AMD-54..64); additive-only per AMD-55-INV-01 (charter §2) |
| 2 | One module dependency; engine never depends on integrations; Core boots/passes CI with the set empty | assessment §1 (`requires com.homesynapse.integration` — literal kept out of copy for name-light); M9.1's empty-factories Phase-6 skip, core `ec2e3b4`; EXT-INV-1 candidate ground (charter §2) |
| 3 | Test fixtures ship (stub context + reference test adapter) | assessment §1: testFixtures shipped (StubIntegrationContext/TestAdapter) |
| 4 | Command spine live end-to-end; replay safety pinned by CI | M9.1 landed core `ec2e3b4` (spine E2E vs registered fake, T18–T20; INV-ES-09 pinned in the extended replay gate, runs in `check`) |
| 5 | Honest actuation: confirmed/failed/expired; unconfirmed never rendered as success | Doc 07 §3.11.2 ledger (shipped M7.3) + AMD-97 ratified semantics + AMD-97-INV-01 (§51) |
| 6 | First radio integration (Zigbee) in progress on real hardware now | M9.2 authored ISSUE-READY 2026-07-03 (beat-57); bench Wave-1 hardware received 2026-06-23; claim phrased "being brought up," not shipped |
| 7 | No device-count marketing; no dynamic loading yet (reserved seam); no sandbox claims before the rung exists | brief §2.3; assessment §2 (dynamic loading triple-banned, amendable seam); DP-18-B RULED (beat-57) — the honesty rule as doc text |
| 8 | Ecosystem-killing-migration signature (kill-date-before-parity, "seamless" promises, tooling removed mid-transition) | dossier L-12 [ST-1/2/3/6, CR-1/2/7] — receipts-backed; platforms kept general in copy; C2 direction (dated/specific allowed, anxiety framing avoided) |
| 9 | Versioning policy: semver + declared compat range + forward-only migration + named deprecation floor | **DP-18-A RATIFIED beat-57** (see §5.2) — stated as policy; the floor's N deliberately unquantified (unpinned until Doc 18 Locks) |
| 10 | Seam activation is additive — never re-architecture, never forced migration | charter §1 done-if criterion (L-12, L-13) |
| 11 | Community integrations never paywalled | **DP-18-C RULED (a) beat-57** — the principle ruled TODAY; phrased as forward commitment |
| 12 | Extension architecture doc in authoring; curated wave first; marketplace only with the trust floor | charter (final, 2026-07-02) + beat-57 ("Doc 18 authoring FULLY UNBLOCKED — the hub's immediate next work product"); DP-18-B (curated IN_JVM wave-1); charter §3 seam 7 (the floor). **No dates anywhere** |
| 13 | Apache-2.0 licensed | **⚠ PUBLISH-GATED** (§5.1): the LOCKED licensing decision (Revenue_Model_and_Licensing_Strategy.md) — but the repo LICENSE at authoring is the pre-release proprietary placeholder. Gate row in the page's provenance: verify the LICENSE flip before publish (config-superiority tense-gate precedent) |

Landing/stub pages: every new sentence carries a provenance row in its page appendix (event-sourced record + non-firing answer = M7.5a/b shipped; ledger = M7.3 + AMD-97; "measured on real hardware" = bench Wave-1 corpus, values deliberately not quoted — pointer-not-copy; the ledger page's category superlative recast into the counsel-safe "to our knowledge" form; competitor specifics [HA trace caps, Insteon narrative] deliberately DEFERRED to the Increment-2 dossiers where their receipts can ride along). **Zero unsourced claims ship; where evidence wasn't ready, the page says less** (the brief's "says-less-truthfully" rule, applied).

## 5. Prompt-vs-source corrections (the second-check Nick asked for)

1. **"Apache-2.0 core" is not repo-true today.** Core `LICENSE` = proprietary/all-rights-reserved (pre-release, build-hidden per W-2). Apache-2.0 is the Locked strategy decision. Handled: publish-gated claim (§4 row 13). **Hub/Nick action: the LICENSE flip must land before the developer page publishes.**
2. **DP-18-A is RATIFIED, not "pending Nick's ruling"** — the brief's §2.3 line is stale against beat-57's own rulings (same beat as the dispatch). Handled: the policy is stated with ruling-backed confidence; unpinned specifics (deprecation-floor N) stay unquantified.
3. **W-4 embargo vs D-4's "plug-and-play" phrasing:** the brief's §2.4 restatement of D-4 names plug-and-play as a mainstream lead; W-4 (install story UNDECIDED) embargoes that claim. The master plan §3.1 resolution applied: mainstream leads reliability + works-together + the explainability proof. Also noted: D-4 itself is verified binding (ruled register rule, ACCEPTED 2026-06-12 per the landing's provenance + W-1's cross-reference) but its R15 strategy-FILE fold (Six_Battlefields) has not landed — a hub docs-pass item, no effect on this lane.

## 6. The dist-gitignore rider: REFUTED — commit 1 is intentionally absent

The brief's §2.5 ("add `web-ui/dashboard/dist/` to the core .gitignore — the FE-1b finding") rests on a false premise. Evidence, re-derivable:

- `git check-ignore -v web-ui/dashboard/dist/` → matched by **`web-ui/dashboard/.gitignore:3` (`dist/`)** — a module-local ignore file that has existed **since `b296e76` (2026-06-26, the first frontend beat)**, whose own header says "the root .gitignore also covers these."
- The root `.gitignore` line 118 carries unanchored **`dist/`** (Node/Frontend section) — matching any depth, including the dashboard's.
- `git ls-files web-ui/dashboard/dist` → **0 tracked files** (no tracked-file override of the ignore).

So `dist/` is **doubly ignored and always was** during FE-1b; an ignored directory can neither appear in `git status` nor ride an `add -A` sweep. The FE-1b return's "un-ignored dist/" observation (and its §6 note) is refuted by source; explicit-list staging remains correct discipline for the OTHER reasons (untracked/parallel-lane files). Committing a third, redundant ignore line to core on a refuted premise would ship exactly the unverified-claim class this project's audit culture exists to catch — so **no core commit is made, and this lane's core-repo write surface ends at zero files.** Hub: fold the refutation (the FE-1b finding routes to CLOSED-REFUTED).

## 7. Build command + local-build evidence + the deferred gate of record

**One command, green:** `cd website/site && npm ci && npm run build` — prebuild runs the shared-source preflight, postbuild enforces zero-JS. In-lane result: **6/6 pages built; zero-JS gate OK**; rendered-output checks all pass (provenance-comment leak 0; placeholder leak 0; `.md`-link leak 0; brand substitution verified; noindex/lang/skip-link present; total shipped assets ≈ 35 KB = 9.7 KB CSS + the 25.4 KB shared Inter subset; no JS files emitted — the only scripts are the inline theme boot + toggle).

**Env-model honesty (how the in-lane build ran):** the session VM's shared disk was full and **esbuild's native binary SIGSEGVs under this sandbox** (Go-runtime class; rollup's native loads fine; sharp bus-errors — untouched, no images). The build therefore ran on `/tmp` from an exact-layout copy **proven ≡ mount by md5 over all 22 site+canon files**, with a `esbuild → esbuild-wasm` override applied **to the build copy only**. The committed tree is native-esbuild (package.json clean; package-lock.json regenerated lock-only from the clean manifest — no wasm anywhere in it).

**DEFERRED-BUILD-GATE (the gate of record — Nick, host-side, native toolchain):**
```
cd C:\Users\Nick\Desktop\Code\ClaudeFolder\homesynapse-core-docs\website\site
npm ci
npm run build     # expect: preflight OK → 6 pages → zero-JS gate OK
npm run dev       # optional: eyeball at http://localhost:4321
```
Target commit: the 26-path docs-repo change set below. (Windows host esbuild is unaffected by the sandbox issue.)

**a11y/brand gate results (skill checklist):** WCAG — skip-link + `lang="en"` + landmark structure on every page; heading order clean (h1→h2→h3, verified in output); visible `:focus-visible` rings (token color); `prefers-reduced-motion` honored globally; nav/toggle targets ≥24px (2.5.8); non-sticky header (nothing can obscure focus, 2.4.11); theme state conveyed by text+shape, never color alone; color pairs are the dashboard's AA-tuned tokens used on their intended surfaces (tokens.css is the contract). Brand — calm-neutral throughout; NO textures/brand-moments/illustrated hero (W-8/9/10 await the sample-round veto); wordmark typeset from the brand token (W-6: rename-survivable, monochrome-survivable, no image lockup); one accent with the interaction monopoly (W-9, inherited from tokens); voice registers A (developers) / B (landing, dossier shorts) held; footer carries "a NexSys product" via the company token (W-7) + the truthful no-tracking line ("loads no third-party resources, runs no analytics; stores only your theme choice, on your device" — true by construction, INV-LF-01 posture). Stranger-test: no explanation surface ships on the site yet (the hero embed is D-FE-6-gated), so the mom-test bar had no new subject; all copy held to ≤~20-word sentences where structural.

## 8. Proposed CI (decision for Nick — NOT implemented; no workflow file was touched)

Propose `website.yml` in the **docs repo**: trigger `push` with path filter `website/**`; one job = checkout docs repo + a second, sparse checkout of `homesynapse-core` at the sibling path (only `web-ui/dashboard/src/styles/` is needed) → `cd website/site && npm ci && npm run build`. Build-only is the right V1 gate: the build already fails on missing shared sources, emitted JS, or broken canon routing by construction; a link-checker adds value only when external links enter the content (today every link is internal), so defer it. Decision: adopt now (locks the gate before content Increment 2 churns the canon) vs. at the hosting/deploy decision — hub's call; this lane recommends now, it is ~20 lines and gate-4-relevant.

## 9. Defaults taken (recorded, revisable — the §2.1 "canon silent → decide and record" duty)

(1) Site theme default light-leaning (stored > OS > light), dark first-class, same tokens — master plan §4.1's recommendation; the dashboard's dark-default ruling is dashboard-scoped. (2) Site reading scale = typography-reference §3–§4 (Major Third, 65ch, 1.6) as `--site-*` derivations over the shared primitives — extension, not a second system. (3) Analytics: none at all (master plan option (a)); the footer states it. (4) Astro ^5.18 pin (Vite-6 sameness). (5) `noindex` until W-5. (6) Non-sticky header. (7) Name tokens extended to the COMPANY name (the W-7 footer line renders from `BRAND.companyName` — W-11 renames both names, so both are tokens). (8) Route names: `/ledger-gap/` for `ledger-gap-dossier.md` (reads public, not internal). (9) The three stubs' Increment-2 planning content preserved verbatim inside their comment blocks (nothing lost for the dossier author; the site strips comments from output anyway).

## 10. §10-audited commit set (Nick, host-side; messages via `git commit -F`)

**⚠ FIRST: a stale 0-byte `.git/index.lock` sits in the DOCS repo** (created by a VM-side `git status` this session; deletion is permission-gated in-session — the known 2026-06-26 class). Delete it or the commit fails:
`rm C:\Users\Nick\Desktop\Code\ClaudeFolder\homesynapse-core-docs\.git\index.lock`

**Commit A — docs repo (stages EXACTLY 26 paths: 20 new + 6 modified, all `website/**`):**
```
cd /c/Users/Nick/Desktop/Code/ClaudeFolder/homesynapse-core-docs
git add website/README.md website/index.md website/pages/config-superiority.md website/pages/explainability.md website/pages/ledger-gap-dossier.md website/pages/no-cloud-account.md website/pages/developers.md website/site/.gitignore website/site/README.md website/site/astro.config.mjs website/site/package.json website/site/package-lock.json website/site/tsconfig.json website/site/plugins/remark-brand.mjs website/site/plugins/remark-canon-links.mjs website/site/plugins/remark-strip-comments.mjs website/site/scripts/check-shared-sources.mjs website/site/scripts/check-zero-js.mjs website/site/src/content.config.ts website/site/src/lib/brand.mjs website/site/src/lib/routes.mjs website/site/src/styles/site.css website/site/src/layouts/Base.astro website/site/src/components/ThemeToggle.astro "website/site/src/pages/[...slug].astro" website/site/src/pages/index.astro
git commit -F /c/Users/Nick/Desktop/Code/ClaudeFolder/_scratch/2026-07-03_docs_website-lane_commit-msg.txt
```
Audit: `git status --short` in the docs repo shows exactly these 26 + nothing outside `website/` (verified in-lane: 0 non-website paths). `node_modules/`, `dist/`, `.astro/` are covered by `website/site/.gitignore` (in the set). No secrets, no runtime state, no build output staged.

**Commit B — hivemind (stages EXACTLY 2 files):**
```
cd /c/Users/Nick/Desktop/Code/ClaudeFolder/nexsys-hivemind
git add context/audits/2026-07-03_website-lane_return.md context/handoff/cross-agent-notes.md
git commit -F /c/Users/Nick/Desktop/Code/ClaudeFolder/_scratch/2026-07-03_hivemind_website-lane-return_commit-msg.txt
```
(If the hub has in-flight edits on cross-agent-notes.md at commit time, stage this lane's two paths only — they are the whole set above; the tree was at `e81a22a` clean when this lane appended.)

**Commit C (core): NONE — intentionally absent** (§6). This lane wrote zero core files.

## 11. Honest gaps + ranked next-lane pointer (refuse-to-close)

**Gaps, named:** the three dossiers are honest SHORTS, not reviewer-grade (W-5 PG-1 remains open — the binding gate-4 content gap); no wordmark SPEC yet (W-6 task; producible name-light at design-system v0); no screenshots/hero embed (D-FE-6 gated on real-device data); follow-the-build CTA mechanics name/publish-blocked (TODO-fenced in the canon); hosting/analytics-adoption/deploy = hub's (gate 4 closure is therefore NOT declared); design-system reconciliation C1–C11 still open (the site consumed tokens.css as truth per the master-plan direction, which is the reconciliation's endpoint anyway); the `@astrojs/preact` island seam documented but not installed; in-session native-esbuild verification impossible in this sandbox class (future frontend lanes: plan the /tmp-copy + wasm-override pattern, or defer the gate).

**Next-lane candidates, ranked:** **(1) Content build-out** — the three stub dossiers to config-superiority reviewer-grade (pure copy work, the W-5/PG-1 binding gap, parallel-safe vs M9.x; the preserved in-file planning stubs + receipt obligations are ready to execute). **(2) Website CI** (`website.yml` per §8 — ~20 lines once Nick rules adopt-now). **(3) FE T2 backlog** (ExplainHub zero-state (d), hero differentiation polish, mobile-first hero) — dashboard polish, lower gate-4 leverage. This lane recommends (1).
