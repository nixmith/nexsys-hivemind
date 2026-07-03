<!--
file: context/handoff/2026-07-03_website-lane_ssg-and-developer-page_session_prompt.md
purpose: Dispatch brief for the WEBSITE lane — gate 4's open half. A fresh, write-isolated Cowork conversation running the nexsys-frontend skill: stand up the SSG (Nick rules the framework at lane start), build the launchable site skeleton from the existing content canon, and ship the developer/integrations page in the truthful R-3 posture. Authored by the v15 PM hub.
audience: Frontend lane (fresh Cowork conversation; /nexsys-frontend skill); Nick (SSG ruling, gates, commits).
state-type: session prompt (lane dispatch).
status: READY — launch on Nick's word, parallel to the M9.2 CC lane (write-isolated: this lane NEVER touches integration/**, gradle/**, app/** or any hivemind spine file).
baseline: docs `1509b34` · core `cf3733e` · hivemind at dispatch (re-derive). If core HEAD moves mid-lane (M9.2 landing), run the baseline-shift protocol from your skill's build-and-ci reference: prove the delta disjoint from your surfaces (`homesynapse-core-docs/website/**`, the one core `.gitignore` rider line), record the proof, carry on; intersecting delta = STOP + report.
-->

# Website Lane — SSG bring-up + the developer/integrations page (gate 4's open half)

You are the frontend/brand lane (nexsys-frontend skill). The dashboard is live end-to-end (FE-1b, core `cf3733e`); `install-smoke` is green on every push — **the website is the LAST unstarted go/no-go surface (gate 4's open half; mid-Aug gate ~Aug 16).** The content canon exists and is good; what's missing is the build system, the assembled site, and the developer page. Ship the smallest launchable, truthful site — not a bigger content project.

## 0. Ordered reading (ground before building)

1. Your skill (nexsys-frontend) — brand/design-system/a11y gates + the lane-return protocol + build-and-ci discipline (baseline-shift, explicit-list staging, gate-copy recipe pointer).
2. `nexsys-hivemind/context/planning/2026-06-29_frontend-master-plan.md` — §0 (website rank-2 status), §1.3 (SSG research: Astro recommended — zero-JS islands, Vite 6 = the dashboard's tool, `@astrojs/preact` lets the site reuse dashboard Preact components + `tokens.css`; 11ty = config-light fallback; Hugo = fast but no component model), §1.6 (open decisions), §5 (Nick rules).
3. `homesynapse-core-docs/website/` — the FULL tree first (`README.md` open items, the design-system canon [visual/typography/voice-and-tone/design-vision — DRAFT status], brand-direction research, the four flagship pages: `config-superiority.md` [reviewer-grade], `index.md` [skeleton landing], `explainability` / `no-cloud-account` / `ledger-gap-dossier` [stubs]).
4. `nexsys-hivemind/context/planning/2026-06-13_strategy-refresh-drafts_R15.md` — the **D-4 messaging rule** (ratified): *privacy is a segment lead, not THE lead* — mainstream-homeowner surfaces lead with **reliability, works-together, plug-and-play**; privacy-first framing leads ONLY prosumer/EU segments (with the dated Data Act/CRA teeth). Privacy never disappears — it stops being the headline where it doesn't sell.
5. `nexsys-hivemind/context/planning/2026-07-02_Doc-18_requirements-charter.md` (R-3 context) + `context/assessments/2026-07-02_extensibility-and-plugin-ecosystem_PM-assessment.md` §3 item 2 — the developer-page obligation and its truthfulness rule.
6. `nexsys-hivemind/context/assessments/2026-07-02_plugin-ecosystem-wars_research-dossier.md` — **L-12** (the positioning voice you will write in): *ecosystem-killing migrations share a signature: kill date announced before replacement parity, "seamless" promises, tooling removed mid-transition (SmartThings Groovy; Chrome MV3).* NexSys's counter-position: **breaking changes are a contract** — versioned, migrated, never a rug-pull. This is the developer page's spine.
7. `nexsys-hivemind/context/audits/2026-07-03_frontend-dev-lane_FE-1b_return.md` §4 — the hazards mined for you below came from here.

## 1. Nick's ruling at lane start (veto-or-default)

**SSG framework.** Default = **Astro** (the master plan's researched recommendation; the component/token sharing with the dashboard is the differentiating win). Nick may veto to 11ty at lane start; a veto changes scaffolding only, not scope. Record the ruling in your return. Do NOT begin scaffolding before the ruling is on record (one line from Nick suffices).

**Site build location.** Follow the master plan's placement (with the content in `homesynapse-core-docs/website/`); if the plan leaves it open, propose at most TWO options with one-line tradeoffs at the same veto-or-default gate (default: scaffold alongside the content it builds).

## 2. Scope (the smallest launchable truth)

1. **SSG scaffold** per the ruling: builds locally with one command; consumes the design-token canon (`tokens.css` reuse per the master plan if Astro); zero-JS-by-default pages; the DRAFT design-system canon is your styling authority (you are its enforcement gate — where the canon is silent, decide and record, don't invent a second system).
2. **Assemble the launchable skeleton:** landing (`index` — build OUT the skeleton), `config-superiority` (reviewer-grade content — make it render beautifully; content edits only where rendering demands), and honest SHORT versions of the three stubs (a stub page that says less truthfully beats a padded page — no filler prose).
3. **The developer/integrations page (R-3 — the assessment's watchlist item 2):** the truthful posture — *"SDK maturing — the adapter contract is frozen and documented"*; what exists TODAY (the frozen 2-type SPI, the documented adapter contract, Apache-2.0 core), what is coming (honestly staged, no dates you can't source); the **L-12 voice**: breaking changes are a contract (semver'd, migrated, deprecation floors — mirror the DP-18-A recommendation language WITHOUT presenting it as ratified; it is pending Nick's ruling). **Every integration/device claim must match shipped truth at publish** — today that means: the spine is live, the dashboard is live, real-device Zigbee is IN PROGRESS (M9.x). No device-count marketing. No "works with 2,000 devices". The bench-measured honesty story (confirmed vs unconfirmed) is exactly the brand — use it.
4. **IA per D-4:** segment-routed messaging — mainstream surfaces lead reliability/works-together/plug-and-play; prosumer/EU surfaces lead privacy with named-regulation teeth. Structure navigation so the segments diverge AFTER a shared truthful landing, not via duplicate sites.
5. **Rider (first commit, core repo, 1 line):** add `web-ui/dashboard/dist/` to the core `.gitignore` (the FE-1b finding — host `npm run verify` creates an un-ignored `dist/`). Separate 1-line commit, message provided in your return.

## 3. Hazards (mined from prior returns — do not re-pay)

- **Explicit-list staging, never `add -A`:** the FE-1b lesson — an untracked `dist/` nearly rode a sweep. Every commit you prepare states exact paths + counts (env-model §10 audit; your skill points there).
- **Truthfulness is a hard gate, not a tone:** every factual product claim on every page gets a source row in your return (claim → shipped-truth citation: file/commit/measured value). An unsourced claim ships as a question, not a statement. This is the anti-fabrication discipline applied to marketing — the R-3 rule exists because the strategy's SDK promise outran governance once already.
- **No secrets, no tokens:** you should need no running Core; if you run anything, nothing minted enters git or a commit message (FE-1b §6 hygiene).
- **Mount lag:** recently edited files can lag >30 min in the VM view — host file tools are authoritative; if a VM-side build must see fresh edits, use the gate-copy recipe (your skill's pointer; env-model §5).
- **Write isolation:** your surfaces are `homesynapse-core-docs/website/**` (+ scaffold location per §1 ruling) and the single core `.gitignore` line. The M9.2 CC lane owns `integration/**`/`gradle/**`/`app/**` in core this window. You never write hivemind spine files — your return is a new audit file + a cross-agent note append.
- **CI:** do NOT add or modify workflows silently. If the site should gate in CI (it should, eventually), PROPOSE the workflow shape in your return as a decision for Nick (name: `website.yml`; trigger paths; build-only vs link-check) — one paragraph, not an implementation.

## 4. Return contract (write-isolated; hub two-layer audits)

File `nexsys-hivemind/context/audits/2026-07-03_website-lane_return.md` + a cross-agent note append. Carry: the SSG ruling record; what was built (re-derivable counts: pages, components, files); the claim→truth source table; the D-4 conformance note (which surface leads with what and why); a11y/brand gate results per your skill; build command + local-build evidence; the §10-audited commit set (exact paths + counts, messages via `_scratch/` `git commit -F`); the proposed-CI paragraph; honest gaps + next-lane pointer (candidates: content build-out for the three stubs, website CI, FE T2 backlog [ExplainHub zero-state, hero differentiation, mobile-first] — rank them). Do NOT declare gate 4 closed — that's the hub's call on Nick's deploy/hosting decisions, which are OUT of your scope.

## 5. Done-when

(1) The ruled SSG builds the site locally, one command, green. (2) Landing + config-superiority + developer page + three honest stubs render on-brand (canon-conformant, WCAG-checked per skill). (3) D-4 IA in place. (4) Claim→truth table complete — zero unsourced claims. (5) The dist-gitignore rider commit prepared. (6) Return filed per §4 with audited commit sets. Anything less ships as an honest partial with the gap named.
