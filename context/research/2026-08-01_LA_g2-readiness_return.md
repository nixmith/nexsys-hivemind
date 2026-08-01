<!--
file: context/research/2026-08-01_LA_g2-readiness_return.md
purpose: Lane return for Section L-A of the 2026-07-31 strategy-lane briefs — THE G-2 READINESS PACKAGE. Five deliverables (D-1 the legacy-string census · D-2 the token-parameterized migration runbook · D-3 the acquisition checklist · D-4 the clinic/entity prep packet · D-5 the day-of-G-2 runbook) so that when counsel rules at G-2, execution begins the same day.
audience: The hub (intake adjudication); Nick (executes D-3/D-5); the LAUNCH-RUNWAY CHARTER (Aug-12–13) which eats §WHAT CHANGES OUR PLANS.
state-type: lane return (L-A; desk lane, repo access; host-side census run 2026-07-31 evening CDT)
status: FILED — lane commits NOTHING; every output is an inventory, a runbook, a question packet, or draft text. Zero pre-freeze code, zero acquisitions, zero filings, zero posts.
date-note: authored across the 07-31/08-01 boundary (host clock 2026-07-31 21:03 CDT = 2026-08-01 02:03 UTC). Filed under the UTC date to match the brief's named `2026-08-XX_LA_g2-readiness_return.md` pattern. Census HEADs are the 07-31 evening state.
not-a-lawyer: NOTHING here is legal advice, clearance, or a trademark-risk conclusion. Where a question is legal it is filed AS A QUESTION for the clinic/counsel packet (D-4), never answered. Counsel owns legal direction.
token-law: {PRODUCT} · {COMPANY} · {ORG} are unresolved tokens throughout. No candidate name is hardcoded into any runbook step, acquisition row, or draft document. The brand program (`context/strategy/brand-program/`) is read and NOT re-litigated.
-->

# L-A — THE G-2 READINESS PACKAGE (return)

## §0 — Compliance, method, and honest limits

**Section 0 laws, discharged.** Search-first + date-stamped for every web-sourced claim (URL + access date inline). Every load-bearing claim labeled **FACT** / **INFERENCE** / **OPINION** with confidence. Access failures disclosed in §0.3, never routed around. ONE file. Token-parameterization held throughout (§0.2). Nothing legal answered. Nothing acquired, filed, posted, or coded. History untouched — the migration scope in D-2 is **shipping artifacts + forward-facing surfaces only**, per law 6.

**Time-box.** ~half-day. The census (D-1) took the majority of it and is the load-bearing deliverable; D-2's estimates are grounded in D-1's counts rather than in prose.

### §0.1 Grounding reads executed, in the ordered sequence

`context/strategy/brand-program/2026-07-22_brand-architecture_decision-package.md` (Architecture C RATIFIED 2026-07-23; engine register ruled; §5 branch map) · `2026-07-23_domain-handle-claims-refresh.md` (the handle-pattern ruling) · `2026-07-22_launch-readiness_checklist.md` · `context/research/2026-07-31_research-intake_adjudication_v42-beat-12.md` **A-1** (the premise correction) and **C-5** (the migration joins G-2) plus C-1/C-3/C-4/C-6 as they bear on D-5 · `context/handoff/pm-handoff.md` **v43 beat 1** (the executive-horizon scan, X-1..X-6) · `context/strategy/2026-07-27_homesynapse-technical-overview_north-star.md` (including its `verified-at-filing` frontmatter honesty state — the agent-seams sentence is DESIGNED-FOR, not TRUE-TODAY, and that qualifier travels with any external use of the document). `context/research/2026-07-31_R2_brand_return.md` §6.1 was **not** deep-read: the adjudication's C-5 is its ruled distillation and the brief marks the return deep-read-on-demand-only. **INFERENCE, HIGH** — nothing in D-1..D-5 depends on a §6.1 detail the adjudication did not carry forward.

### §0.2 How the token law is held

`{PRODUCT}` = the consumer mark that resolves at G-2. `{COMPANY}` = the ratified quiet parent. `{ORG}` = the future GitHub org handle. Lower-case token forms appear where a machine surface demands one: `{product}` (a DNS label, a package name, a systemd unit, a directory), `{product-namespace}` (the reverse-DNS Java root, e.g. the `<tld>.<company-or-product>` shape), `{org}` (a registry namespace). **The historical strings `NexSys`/`nexsys`/`HomeSynapse`/`homesynapse`/`com.homesynapse` appear ONLY as census targets and as the left-hand side of migration rows** — that is what a census and a runbook are, and law 6 requires the record keep them.

**Token-law self-audit, run in-lane before filing, with its corrections named.** The check is regenerable:

```bash
# The pattern is the candidate set recorded in context/strategy/brand-program/ — sourced,
# deliberately NOT inlined here, because inlining it would itself breach the law being tested.
CANDS='<pipe-separated candidate + parent strings from the brand program, incl. spelling variants>'
grep -nioE "$CANDS" <this-file>   # must return nothing
```

The first pass returned **two hits**, both corrected before filing and both recorded here rather than quietly fixed: (1) a candidate's closest-misspell domain named literally in a D-3.1 acquisition note — rewritten to token form; (2) a candidate company name inside a verbatim X-1 quotation in the D-5 phase-4 precondition table — token-substituted with the substitution marked in-cell. **The lesson worth carrying: the token law is easiest to violate when quoting our own record, because the record is lawfully full of the strings.** Quoting the spine inside a runbook is exactly the seam where the law leaks. The check now returns clean.

### §0.3 Access failures and honest limits (disclosed, not routed around)

1. **`uspto.gov/trademarks/fees-payment-information` returned HTTP 403** to this session (accessed 2026-07-31); `uspto.gov/trademarks/apply/fees` returned 404. The current base filing fee is therefore carried at **MED** confidence from a secondary source (§D-3.4) instead of the registry of record. **The one-minute fix: read the fee schedule at uspto.gov in a browser before any spend.** No fee figure in this return should be spent against without that check.
2. **Registrar retail prices were not probed per-TLD.** Cloudflare's low-cost-domains page states the at-cost policy but publishes no per-TLD table (accessed 2026-07-31). Retail figures in D-3 are therefore ranges anchored to a verified *wholesale* datum, labeled as such.
3. **The census is host-side and git-tracked-only.** `git grep` respects the index, so untracked and ignored files (build outputs, `node_modules`, local scratch) are OUT of every count. That is the correct scope for a migration census — build outputs regenerate — but it means the numbers are **lower bounds on the working tree** and **exact for the shipped tree**. Stated so the hub reads them correctly.
4. **No GitHub org/handle availability probe was run for any candidate name.** Running one would require typing a candidate name into a third-party surface pre-G-2. The brand program's 2026-07-23 refresh already holds the screens for the leading candidate; D-3 is deliberately name-agnostic and pattern-driven instead.
5. **`nexsys-io` org occupancy was not confirmed by search.** A public-web search for the string surfaced a third party operating **"NexSys Labs" at `github.com/Nex-Sys-io`** (accessed 2026-07-31) — one hyphenation away from our current org — but did not surface our own org (consistent with low public visibility). Recorded as a **residual-exposure corroboration of C-5 at MED confidence**, not as a new finding.

### §0.4 Census verification pass (run in-lane; corrections applied and named)

Every D-1 count was re-derived a second time from its stated command before filing, and the derived figures (percentages, subtractions, cross-references between tables) were checked against the raw outputs. **Three corrections were found and applied; they are named here rather than silently fixed:**

1. **Gradle/TOML/properties files carrying a legacy string: 31 → 30.** The first figure came from counting lines in a `grep -c` listing by eye; the corrected figure is `git grep -l … | wc -l`. **Lesson: count with the tool, never off the screen.**
2. **`include(…)` lines: "the other 22 are name-neutral" → 21 of 22.** The original phrasing double-counted the one line that *does* carry the name. Corrected and re-verified with an explicit command whose output is now quoted inline in D-1.4.
3. **Package-path count disambiguated: 51 → "51 distinct paths, of which 31 are leaf directories holding files."** Both numbers are true of different things and the single figure was ambiguous for effort-sizing in D-2 step 3.

None of the three changes any conclusion or any effort estimate. They are filed because a census whose arithmetic is not itself audited is prose with numbers in it.

---

## D-1 — THE LEGACY-STRING CENSUS

**Method.** Host-side (no mount-law exposure), `git grep` against the tracked tree at each repo's HEAD as of the 2026-07-31 evening. `-a` treats every tracked file as text; `-I` skips binaries; `-o` counts *occurrences*, `-l` counts *files*. Every number below is reproducible by pasting its command. Repo HEADs at census time:

```bash
cd <ClaudeFolder>
for r in homesynapse-core homesynapse-core-docs nexsys-bench nexsys-skills; do
  echo -n "$r: "; git -C $r --no-optional-locks rev-parse --short HEAD
  git -C $r remote -v | head -1
done
```

```
homesynapse-core:      60d3ab5   origin  https://github.com/nexsys-io/homesynapse-core.git (fetch)
homesynapse-core-docs: a53f474   origin  https://github.com/nexsys-io/homesynapse-core-docs.git (fetch)
nexsys-bench:          a791c99   origin  https://github.com/nixmith/nexsys-bench.git (fetch)
nexsys-skills:         5bebfcd   origin  https://github.com/nixmith/nexsys-skills.git (fetch)
```

**FACT, HIGH — the fleet is split across TWO GitHub namespaces, and one of them is a personal account.** Core and docs sit under the org `nexsys-io`; bench and skills sit under the personal account `nixmith`. This was not in the record I read and it changes D-2 step 1 from "rename an org" to "consolidate two namespaces into one."

### D-1.1 The totals (all four repos)

```bash
for r in homesynapse-core homesynapse-core-docs nexsys-bench nexsys-skills; do
  echo "=== $r ==="
  echo -n "occurrences: "; git -C $r grep -aoIE 'NexSys|nexsys|HomeSynapse|homesynapse' -- . | wc -l
  echo -n "files: ";       git -C $r grep -alIE 'NexSys|nexsys|HomeSynapse|homesynapse' -- . | wc -l
  echo -n "tracked files: "; git -C $r ls-files | wc -l
done
```

| Repo | Occurrences | Files carrying ≥1 | Tracked files | Share of tree |
|---|---:|---:|---:|---:|
| `homesynapse-core` | **9,986** | 1,329 | 1,420 | 93.6% |
| `homesynapse-core-docs` | **3,898** | 176 | 201 | 87.6% |
| `nexsys-bench` | **103** | 29 | 69 | 42.0% |
| `nexsys-skills` | **298** | 27 | 45 | 60.0% |
| **Fleet** | **14,285** | **1,561** | **1,735** | **90.0%** |

By token (note `com.homesynapse` is a subset of the `homesynapse` count — grep's leftmost-longest alternation resolves the overlap in favor of the longer literal only when the pattern is run alone, so these are counted per-token and are NOT column-additive):

```bash
for r in homesynapse-core homesynapse-core-docs nexsys-bench nexsys-skills; do
  echo "=== $r ==="
  for t in 'com\.homesynapse' 'HomeSynapse' 'homesynapse' 'NexSys' 'nexsys'; do
    echo -n "  $t : "; git -C $r grep -aoIE "$t" -- . | wc -l
  done
done
```

| Token | core | docs | bench | skills |
|---|---:|---:|---:|---:|
| `com.homesynapse` | 5,920 | 1,056 | 0 | 0 |
| `HomeSynapse` | 2,059 | 1,614 | 29 | 32 |
| `homesynapse` | 6,648 | 2,001 | 45 | 47 |
| `NexSys` | 1,207 | 133 | 2 | 3 |
| `nexsys` | 72 | 150 | 27 | 216 |

**INFERENCE, HIGH:** the `NexSys` count in core (1,207) is almost entirely the per-file copyright header, not prose — see D-1.7. That matters because it is the *same* surface the Apache-2.0 flip rewrites, so the two edits are one pass, not two.

### D-1.2 Class 1 — JPMS module names + package directories (core only)

```bash
cd homesynapse-core
git ls-files | grep -c 'module-info\.java$'
git grep -hoE '^\s*(open\s+)?module\s+[A-Za-z0-9_.]+' -- '*module-info.java' | sed 's/^ *//' | sort
git ls-files | grep -oE '(^|/)com/homesynapse/[a-z0-9/]*' | sort -u | wc -l
git grep -aoIE '^package com\.homesynapse[^;]*;'          -- '*.java' | wc -l
git grep -aoIE '^import (static )?com\.homesynapse'       -- '*.java' | wc -l
git grep -aoIE 'requires (static |transitive )*com\.homesynapse[a-z.]*' -- '*module-info.java' | wc -l
git grep -aoIE '(exports|opens) com\.homesynapse[a-z.]*'  -- '*module-info.java' | wc -l
git ls-files | grep -c '/com/homesynapse/'
```

| Surface | Count |
|---|---:|
| `module-info.java` files | **19** |
| Distinct JPMS module names | **19** |
| Distinct package paths under `com/homesynapse/` (incl. intermediate) | **51** |
| …of which are LEAF directories actually holding files | **31** |
| `package com.homesynapse…;` declarations | **1,144** |
| `import [static] com.homesynapse…` statements | **3,152** |
| `requires …` clauses naming a `com.homesynapse` module | **68** |
| `exports` / `opens` clauses | **18** |
| Tracked files living under a `/com/homesynapse/` path | **1,145** |
| `com.homesynapse` occurrences in `*.java` | **4,902** |
| `com.homesynapse` occurrences in `*.md` | **983** |

The 19 module names, verbatim:

```
com.homesynapse.api.rest        com.homesynapse.integration.runtime   com.homesynapse.persistence
com.homesynapse.api.ws          com.homesynapse.integration.zigbee    com.homesynapse.platform
com.homesynapse.app             com.homesynapse.it                    com.homesynapse.platform.systemd
com.homesynapse.automation      com.homesynapse.lifecycle             com.homesynapse.state
com.homesynapse.config          com.homesynapse.observability         com.homesynapse.value
com.homesynapse.device          com.homesynapse.event
com.homesynapse.event.bus       com.homesynapse.integration
```

**INFERENCE, HIGH — the arithmetic names the residue an IDE refactor will miss.** 1,144 package declarations + 3,152 imports = 4,296 of the 4,902 `com.homesynapse` occurrences in Java. **The remaining ~606 live in string literals, Javadoc, and comments** — exactly the class a "Rename Package" refactor leaves behind silently. The ArchUnit pins below are the largest and most dangerous sub-population of those 606, because they are string literals that a compiler cannot check.

### D-1.3 Class 1b — the ArchUnit package pins (the pin class, called out separately)

```bash
git grep -aoIE '"com\.homesynapse[^"]*"' -- 'testing/**' '*ArchRules*' | wc -l
git grep -nIE '"com\.homesynapse' -- '*ArchRules*.java' | head
```

**37 string-literal package pins**, concentrated in `app/homesynapse-app/src/test/java/com/homesynapse/app/HomeSynapseArchRules.java` (`resideInAPackage("com.homesynapse..")`, per-layer `resideOutsideOfPackage(…)`, and the layered-architecture package lists at lines ~146–197).

**OPINION, HIGH — this file is the single highest-risk artifact in the whole migration, and it fails SAFE.** ArchUnit rules keyed to a package that no longer exists do not error; they match zero classes and pass vacuously. A rename that updates the packages but misses these pins produces a **GREEN build with the architecture enforcement silently switched off** — and the enforcement layer is the north star's own stated symmetry ("the harness enforces; the model only proposes… ArchUnit rules, JPMS module boundaries, and exhaustive sealed switches enforce architectural correctness"). D-2 therefore carries a mandatory negative control for this step.

### D-1.4 Class 2 — Gradle coordinates, project names, convention plugins

```bash
grep -nE 'rootProject|^include' settings.gradle.kts
git grep -nIE '^\s*group\s*=' -- 'build.gradle.kts'
git ls-files 'build-logic/**' | grep 'gradle.kts$'
git grep -oIE 'homesynapse\.[a-z-]+-conventions' -- '*.gradle.kts' | wc -l
git grep -cIE 'homesynapse|HomeSynapse|nexsys|NexSys' -- '*.gradle.kts' '*.toml' '*.properties'
```

| Surface | Value / count |
|---|---|
| `settings.gradle.kts:1` | `rootProject.name = "homesynapse-core"` |
| `build.gradle.kts:6` | `group = "com.homesynapse"` (inherited by every subproject at `:13`) |
| Gradle project path carrying the name | `include("app:homesynapse-app")` — **1**, and it is load-bearing (see D-1.6) |
| Convention-plugin FILES named `homesynapse.*` | **4** (`homesynapse.{application,java,library,test-fixtures}-conventions.gradle.kts`) |
| Apply sites referencing those plugin ids | **25** |
| Gradle/TOML/properties files carrying ≥1 legacy string | **30** |
| npm package name (`web-ui/dashboard/package.json` + lockfile) | `@homesynapse/dashboard` — **3 occurrences** |

**FACT, HIGH:** of the 22 `include(…)` lines, **21 are name-neutral** (`core:event-model`, `api:rest-api`, …). Only `app:homesynapse-app` moves — verified: `grep -E '^include\(' settings.gradle.kts | grep -icE 'homesynapse|nexsys'` → `1`.

### D-1.5 Class 3 — repo names, remotes, and CI

Repo names and remotes: §D-1 header (4 repos, 2 namespaces). CI:

```bash
git ls-files '.github/**'
git grep -cIE 'homesynapse|HomeSynapse|nexsys|NexSys' -- '.github/**'
git grep -nIE 'homesynapse|HomeSynapse|nexsys|NexSys' -- '.github/workflows/install-smoke.yml'
```

| Workflow | Legacy-string hits |
|---|---:|
| `.github/workflows/ci.yml` | **0** |
| `.github/workflows/frontend.yml` | **0** |
| `.github/workflows/install-smoke.yml` | **5** |

The five, verbatim: a header comment (`:1`), two artifact globs (`distribution/image/build/homesynapse_*.tar.gz`, `distribution/deb/build/homesynapse_*.deb` at `:82–83`), and two systemd assertions (`journalctl -u homesynapse.service`, `systemctl status homesynapse.service` at `:89–90`).

**FACT, HIGH — CI is the cheapest class in the entire migration (5 lines in 1 of 3 workflows), and our workflows consume only marketplace actions, none self-hosted.** That second half matters: GitHub's rename documentation warns that "GitHub will not redirect calls to an action hosted by a renamed repository. Any workflow that uses that action will fail with the error `repository not found`" ([GitHub Docs, accessed 2026-07-31](https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository)). We host no action, so that failure mode cannot fire on us.

### D-1.6 Class 4 — YAML / config / deployment surfaces (the live-state class)

```bash
git grep -nIoE '/(etc|var|opt|usr/(lib|share|local))/[A-Za-z0-9._/-]*homesynapse[A-Za-z0-9._/-]*' -- . \
  | sed 's/^[^:]*:[0-9]*://' | sort | uniq -c | sort -rn
git grep -aoIE 'HOMESYNAPSE_[A-Z_]+' -- . | wc -l
git grep -hoIE 'HOMESYNAPSE_[A-Z_]+' -- . | sort -u
git grep -aoIE 'homesynapse|HomeSynapse|nexsys|NexSys' -- 'distribution/**' | wc -l
git grep -aoIE 'homesynapse|HomeSynapse|nexsys|NexSys' -- 'scripts/**' | wc -l
```

| Surface | Count / value |
|---|---|
| `distribution/**` occurrences (22 files) | **225** |
| `scripts/**` occurrences | **81** |
| systemd unit | `distribution/systemd/homesynapse.service`; `User=homesynapse`, `Group=homesynapse` (`:24–25`) |
| Unit name referenced in deb maintainer scripts | `HS_UNIT="homesynapse.service"` in `postinst`, `postrm`, `prerm` |
| `/opt/homesynapse` | 27 (+ `/opt/homesynapse/bin/homesynapse` ×7, `/opt/homesynapse-tests` ×3) |
| `/var/lib/homesynapse` | 26 (+ `/tmp` ×7, `/config/initial_api_token` ×4, `/backups` ×3) |
| `/etc/homesynapse` | 14 (incl. `/etc/homesynapse/homesynapse.env` ×5) |
| `/var/log/homesynapse` | 11 (+ `/var/log/homesynapse-stdout.log` ×4) |
| On-disk state filenames | `homesynapse-events.db`, `homesynapse.jsa`, `homesynapse.yaml` |
| Environment-variable keys | **7 distinct**, **44 occurrences**: `HOMESYNAPSE_{HOME, BIND_HOST, HTTP_PORT, JVM_OPTS, CDS_ARCHIVE, PURGE_DATA, TOKEN_FILE}` |
| Shipped artifact names | `distribution/deb/homesynapse-token`, `distribution/systemd/homesynapse.env.example`, `homesynapse_*.deb`, `homesynapse_*.tar.gz` |

**OPINION, HIGH — this is the only class with LIVE STATE behind it, and it is therefore the only class that is not a text edit.** Every other class is a string in a file that regenerates. These are directories, a Unix user, a Unix group, a systemd unit, and a SQLite database that exist right now on the bench Pi with the nightly timer pointed at them. Renaming them is a *host migration*, not a *sed*. D-2 step 5 treats it as such and D-2 asks the hub for one ruling.

### D-1.7 Class 5 — public-facing README / docs, and the copyright header

```bash
git grep -lIE 'Copyright \(c\).*NexSys' -- . | wc -l      # 1179
git grep -aoIE 'Copyright \(c\)[^\n]*NexSys' -- . | wc -l  # 1188
git grep -aoIE 'HomeSynapse Core' -- . | wc -l              # 1274
head -1 LICENSE                                              # core
head -1 ../homesynapse-core-docs/LICENSE                     # docs
```

| Surface | Count / value |
|---|---|
| Source files carrying a `Copyright (c) … NexSys` header | **1,179 files / 1,188 occurrences** |
| `HomeSynapse Core` (product-string in headers + prose) | **1,274** |
| core `LICENSE` line 1 | `Copyright (c) 2026 NexSys. All rights reserved.` — **proprietary, all-rights-reserved** |
| docs `LICENSE` line 1 | `Copyright (c) 2025-2026 NexSys Technologies. All rights reserved.` — proprietary, **and a THIRD company-name variant** |
| core `README.md` | 26 occurrences |
| core `docs/**` | 729 |
| core `CONTEXT.md` | 7 |
| core `MODULE_CONTEXT.md` ×21 | **880** |
| docs repo `website/**` | **188** across 20 files (the marketing-site tree; `website/site/package.json` name is `marketing-site` — name-neutral) |
| docs repo `design/**` | 1,335 · `research/**` 1,481 · `governance/**` 442 · `archive/**` 327 · `operations/**` 62 · `foundations/**` 59 |
| docs repo filenames whose BASENAME carries a legacy string | **19 of 201** |

**FACT, HIGH — a third company-name string is in the record: "NexSys Technologies" (docs LICENSE), distinct from "NexSys" (core LICENSE).** Neither matches the ratified quiet-parent name. Both are all-rights-reserved proprietary grants, which is the **H6 LICENSE mismatch** the handoff names — the north star states publicly that "the core is Apache 2.0," and the shipped LICENSE files say the opposite today.

**INFERENCE, HIGH — the copyright-header surface and the Apache-2.0 flip surface are THE SAME 1,179 files.** Doing them as one pass costs one pass. Doing them as two costs two full-tree edits and two review cycles, and leaves a window in which the headers name an entity that does not hold the rights.

### D-1.8 Class 6 — web-ui strings

```bash
git grep -aoIE 'homesynapse|HomeSynapse|nexsys|NexSys' -- 'web-ui/**' | wc -l   # 55
git grep -alIE 'homesynapse|HomeSynapse|nexsys|NexSys' -- 'web-ui/**' | wc -l   # 31
git grep -aoIE '\-\-hs-' -- 'web-ui/**' | wc -l                                  # 640
git grep -aoIE 'homesynapse\.local' -- . | wc -l                                 # 12
sed -n '16,20p' web-ui/dashboard/src/lib/i18n.ts
```

**FACT, HIGH — the user-visible product name in the SPA is already a single token.** `web-ui/dashboard/src/lib/i18n.ts` defines `BRAND.productName` with the in-file comment: *"BRAND.productName is the SINGLE source of truth for the product name. The rename (W-11) is unratified, so the value stays 'HomeSynapse' — but every user-facing surface references this token, so the eventual swap is one line. NEVER hardcode the product name (name-light)."* Every catalog string interpolates `${BRAND.productName}`.

The frontend lane already paid this bill. **The entire user-visible rename of the dashboard is ONE LINE.** The remaining 54 web-ui occurrences are developer-surface: file-header comments, the `index.html` `<title>`/`<noscript>`, the README, the npm package name/description, the token-generator header, and the contract mirror.

Two web-ui sub-surfaces are **not** one-line and need naming:

- **`--hs-` CSS custom-property prefix — 640 occurrences.** Generated, not hand-written: `web-ui/dashboard/src/styles/tokens/tokens.dtcg.json` pins each token's exact CSS variable name in `$extensions.hs.var`, and `scripts/build-tokens.mjs` emits `tokens.css` from it. **OPINION, HIGH: LEAVE IT.** It is an internal CSS namespace with zero user visibility, zero public-surface exposure, and a 640-site blast radius; `hs` is also a plausible initialism for a future name. Changing it buys nothing and risks a design-token regression on G-2 day.
- **`https://homesynapse.local/problems/` — 12 occurrences, and it is FROZEN CONTRACT.** See D-1.9.

### D-1.9 The flagged row — the problem-type URI prefix is a contract surface, not a string

```bash
git grep -nIE 'homesynapse\.local' -- '*.java' '*.ts' '*.mjs'
```

| Site | Role |
|---|---|
| `api/rest-api/…/ProblemType.java:160` | `private static final String TYPE_URI_PREFIX = "https://homesynapse.local/problems/";` (+ Javadoc `:19`, `:213`) |
| `web-ui/dashboard/src/lib/api/contract.ts:76` | `PROBLEM_TYPE_URI_PREFIX` — the frozen-contract TypeScript mirror |
| `web-ui/dashboard/src/lib/api/contract.test.ts:63` | pins the exact string |
| `web-ui/dashboard/scripts/contract-check.mjs:15` | `EXPECTED_PROBLEM_PREFIX` — trips CI on drift |

**FACT, HIGH:** this string is part of the **FROZEN v1.1 read-API contract** (current stamp v1.1.2-2026-07-26, Doc 09 §3.8), mirrored field-for-field client-side, pinned by a test, and guarded by a CI drift-checker built specifically to fail when it changes.

**OPINION, HIGH — this is a contract amendment, not a rename step, and the charter should rule it explicitly.** Two honest observations for that ruling: (a) RFC 9457 problem *type* URIs are opaque identifiers and are not required to resolve, so nothing breaks functionally if the host label stays historical — but a public repo whose error payloads emit a third party's brand is exactly the C-5 embarrassment, one layer deeper than the repo URL; (b) the amendment is **free exactly once**, right now, while the contract has zero external consumers. Post-launch it is a breaking change to a frozen contract with a deprecation window. The cheap moment is G-2 day.

### D-1.10 Class 7 — bench + skills

```bash
git -C nexsys-bench  grep -nIE 'homesynapse|HomeSynapse|nexsys|NexSys' -- .   # 103 occ / 29 files
git -C nexsys-skills grep -cIE 'homesynapse|HomeSynapse|nexsys|NexSys' -- . | sort -t: -k2 -rn
```

The bench's rename-sensitive constants — every one of these is a live operational dependency of the **nightly timer**, not documentation:

| Constant | Site |
|---|---|
| `~/hs-bench` (config, data, quiesce-hold paths) | `scenarios/constants.yaml:248,253,261,262`; `tools/bench.sh:76` |
| `~/homesynapse-core/app/homesynapse-app/build/install/homesynapse-app/bin/homesynapse-app` | `tools/bench.sh:7` — **the APP constant; it embeds the Gradle project path from D-1.4** |
| `PAT='[c]om.homesynapse.app.Main'` | `tools/bench.sh:10` — **the process-match pattern; it embeds the JPMS root from D-1.2** |
| `~/hs-bench/config/homesynapse.yaml`, `homesynapse.heroless.yaml`, `homesynapse.live-basis.yaml` | `scenarios/constants.yaml:253,261,262` |
| `~/hs-bench/data/homesynapse-events.db` | `tools/bench.sh:76` |
| `~/nexsys-bench` deploy path + `ln -sf … ~/bench.sh` | `tools/runner/README.md:190–191` |
| Pi host `hs-dev-1`, user `homesynapse` (uid 1000), `/mnt/nvme/homesynapse` | `iac/bootstrap.sh:17–20,38`; bringup report |
| `iac/99-zigbee-coordinator.rules`, `iac/docker-compose.yml` headers | `nexsys-bench` self-references |

**INFERENCE, HIGH — the bench is coupled to core's rename through TWO constants that a core-only migration silently breaks**: `bench.sh:7` (the installDist path, which contains the Gradle project name `homesynapse-app` twice) and `bench.sh:10` (the pkill pattern, which contains the JPMS package root). Rename core without touching bench and the nightly regime does not error loudly — `bench.sh` stops finding the app and stops matching the process. **The nightly-numbers publishing obligation (C-3) is the asset this quietly kills.**

Skills: 298 occurrences / 27 files, concentrated in the `nexsys-frontend` orchestrator skill (24 in its `SKILL.md`, 13 in `CLAUDE.md`) and the design-record files. **The skill NAMES themselves are the migration surface** — `nexsys-frontend` is a loadable skill identifier, and `nexsys-coder` / `nexsys-project-manager` are named in the hivemind. **OPINION, MED: these are internal tooling identifiers with no public surface; defer them out of the G-2 window entirely** unless the skills repo is going public, which nothing I read says it is.

### D-1.11 Census summary — the classes ranked by what they actually cost

| # | Class | Occurrences | Nature | Mechanical? |
|---|---|---:|---|---|
| 1 | Java packages + JPMS modules | 4,902 (core) | IDE refactor + `git mv` | Yes, except ~606 literal/doc sites |
| 1b | **ArchUnit string pins** | **37** | String literals that fail SAFE | **No — needs a negative control** |
| 2 | Gradle coordinates + project name | ~40 sites | Edit + one build | Yes |
| 3 | Repo names / 2 namespaces | 4 repos | GitHub UI | Yes |
| 4 | CI | 5 lines, 1 of 3 workflows | Edit | Yes |
| 5 | **Deployment / live state** | ~306 (`distribution` + `scripts`) | Host migration | **No — live state on the Pi** |
| 6 | Docs, forward-facing only | ~950 in-scope (of 5,300+) | Prose edit | Yes |
| 7 | web-ui user-visible | **1 line** | Token swap | Yes |
| 7b | `--hs-` CSS prefix | 640 | Generator config | **REC: don't** |
| 8 | **Problem-type URI prefix** | **12** | **Frozen-contract amendment** | **No — hub ruling** |
| 9 | Copyright headers | 1,188 | Same pass as the Apache-2.0 flip | Yes |
| 10 | Bench constants | ~20 sites | Edit + one nightly cycle | Yes, but couples to #1 and #2 |

---

## D-2 — THE MIGRATION RUNBOOK (token-parameterized)

**BOUNDARY, stated explicitly as the brief requires: this runbook SIZES the post-gate coding work unit. It does not author it, and it is not an instruction.** No step here is executable as written. The hub authors the WU as a proper coding instruction post-gate, against the freeze-runway discipline, with red-first tests and named gates. Gate sovereignty holds: **zero pre-freeze code**.

**Sequencing law for this runbook:** steps 1→8 are ordered by *dependency*, and three of them are one-way doors (marked ⚠). Effort is focused-hours for one person who already knows the tree; risk is the probability-weighted cost of getting it wrong, not the probability alone.

### Step 1 — GitHub `{ORG}` creation + repo consolidation ⚠

| | |
|---|---|
| **Effort** | 30–45 min |
| **Risk** | **LOW pre-launch, HIGH post-launch** — this is the step whose cost is *entirely* determined by when it runs |
| **Blocks** | Every step that references a remote URL; the whole D-5 public-ready sequence |

1. Create the org `{ORG}` (free, immediate). **Precondition:** `{ORG}` must be free in GitHub's *shared* user/org namespace — a dormant *user* with that handle blocks org creation. The 2026-07-23 refresh already established this failure mode empirically for the leading candidate and Nick already **RULED** the mitigation: a house-suffix pattern (`{org}hq`-class) is canonical uniformly across platforms. **That ruling is the reason step 1 cannot stall on G-2 day.**
2. Transfer `homesynapse-core` and `homesynapse-core-docs` from `nexsys-io` → `{ORG}`; transfer `nexsys-bench` and `nexsys-skills` from the personal account `nixmith` → `{ORG}`. Then rename each repo.
3. Update all four local remotes: `git remote set-url origin …`.

**Redirect behavior, FACT-tier and dated (all [GitHub Docs, accessed 2026-07-31](https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository)):**

- On **rename**: "all `git clone`, `git fetch`, or `git push` operations targeting the previous location will continue to function as if made on the new location." Issues, wikis, stars, followers redirect. **GitHub Pages project-site URLs do NOT.** Actions hosted in the repo do NOT redirect.
- On **transfer** ([transferring-a-repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository)): issues, PRs, wiki, stars, watchers, webhooks, secrets, deploy keys and history all move; Git LFS objects move in background; **Pages do not redirect**; org→personal transfers drop read-only collaborators (not our direction).
- On **org rename** ([renaming-an-organization](https://docs.github.com/en/organizations/managing-organization-settings/renaming-an-organization)): repo web links redirect, but **the old org profile page 404s, API requests using the old org name 404, `@mentions` of old team names do not redirect, and the old org name becomes available for anyone to claim.**
- **Name-reuse trap:** "If you create a new repository under your account in the future, do not reuse the original name of the renamed repository. If you do, redirects to the renamed repository will no longer work."

**OPINION, HIGH — every one of those caveats is worth approximately zero to us, and that is the entire argument for doing this at G-2 rather than after launch.** There are no external clones, no external forks, no Pages site, no published packages, no marketplace action, no inbound links worth preserving. The redirect machinery exists to protect an ecosystem we do not yet have. **The day we have one, this step costs a permanent redirect debt and a public "we renamed" post.** Today it costs 45 minutes and nobody notices.

**One-way-door note:** after the `nexsys-io` org is renamed or vacated, the name is claimable by a third party. Given the adjudication's finding that NexSys is knockout-DEAD on two live renewed Class-009 registrations, **losing the handle is a feature, not a cost** — but the `Nex-Sys-io` near-neighbor observed in §0.3 means we should not expect the string to stay quiet.

### Step 2 — Gradle coordinates + project names

| | |
|---|---|
| **Effort** | 1–2 h |
| **Risk** | **MED** — one change here silently breaks the bench (step 6) |
| **Blocks** | Step 3 (packages), step 6 (bench constants) |

`settings.gradle.kts:1` `rootProject.name` → `{product}-core`. `build.gradle.kts:6` `group = "com.homesynapse"` → `{product-namespace}`. `include("app:homesynapse-app")` → `app:{product}-app`, **plus the directory `app/homesynapse-app/` → `app/{product}-app/`**. The 4 `homesynapse.*-conventions.gradle.kts` files → `{product}.*-conventions.gradle.kts`, plus their 25 apply sites. `web-ui/dashboard/package.json` name `@homesynapse/dashboard` → `@{org}/dashboard`, and regenerate `package-lock.json` (do not hand-edit).

**Verification gate:** `./gradlew check` green, and `./gradlew :app:{product}-app:installDist` produces the launcher at the new path. **Record that new path — step 6 consumes it.**

### Step 3 — JPMS `com.homesynapse.*` → `{product-namespace}.*` ⚠

| | |
|---|---|
| **Effort** | **3–5 h** including build/test cycles |
| **Risk** | **MED mechanically, HIGH for the pin class** |
| **Blocks** | Steps 4, 6, 7; the Apache-2.0 flip (step 9 folds into it) |

Ordered sub-steps, each with its census anchor:

1. IDE "Rename Package" over the package tree (51 distinct paths, 31 leaf directories holding files) — moves 1,145 files, rewrites 1,144 declarations and 3,152 imports. Use `git mv` semantics so history follows.
2. The 19 `module-info.java` files: 19 module names, 68 `requires`, 18 `exports`/`opens`.
3. **The 37 ArchUnit string pins.** ⚠ **These are the ones the refactor does not see.**
4. The ~606 residual literal/Javadoc/comment sites (`4,902 − 1,144 − 3,152`).
5. The 6 `HomeSynapse*`-prefixed type names (`HomeSynapseCore`, `HomeSynapseConfig`, `HomeSynapseException`, `HomeSynapseArchRules`, `HomeSynapseE2eHarness`, `HomeSynapseAssertions`) + their 4 test counterparts.
6. `MODULE_CONTEXT.md` ×21 (880 occurrences) and the 983 `com.homesynapse` sites in `*.md`.

**MANDATORY NEGATIVE CONTROL for sub-step 3 (the single most important line in this runbook).** ArchUnit rules pinned to a non-existent package match zero classes and **pass vacuously** — a missed pin yields a GREEN build with architecture enforcement silently disabled. Before declaring step 3 done, the WU must **deliberately introduce a known architecture violation and confirm the suite goes RED.** A green suite is not evidence here; a suite that *catches a planted violation* is. This is the same anti-vacuous discipline the bench record already applies to silent-success classes.

### Step 4 — CI

| | |
|---|---|
| **Effort** | 15 min |
| **Risk** | LOW |
| **Blocks** | Nothing; it is the verification surface for steps 2–3 |

Five lines in `install-smoke.yml` only (`:1` comment, `:82–83` artifact globs, `:89–90` systemd assertions). `ci.yml` and `frontend.yml` need no edit. Re-run both to confirm green before touching the Pi.

### Step 5 — the Pi redeploy surface ⚠ (the live-state step)

| | |
|---|---|
| **Effort** | 2–3 h edit + **one clean-install verification run** |
| **Risk** | **HIGH** — the only step with running state and an operational timer behind it |
| **Blocks** | Step 6; the deployed-build half of any post-gate demo |

The edit surface: unit `homesynapse.service` → `{product}.service`; `User=`/`Group=homesynapse` → `{product}`; `/opt/homesynapse` (27) → `/opt/{product}`; `/var/lib/homesynapse` (26+) → `/var/lib/{product}`; `/etc/homesynapse` (14) → `/etc/{product}`; `/var/log/homesynapse*` (11+4) → `/var/log/{product}*`; the 7 `HOMESYNAPSE_*` env keys (44 occurrences) → `{PRODUCT}_*`; deb package name, `conffiles`, `postinst`/`postrm`/`prerm` `HS_UNIT`; `homesynapse-token`; `homesynapse.env.example`; `homesynapse.jsa`; `homesynapse-events.db`; `homesynapse.yaml`.

**THE ONE RULING THIS RUNBOOK ASKS THE HUB FOR: cut over by reinstall, or write a data migration?**

**REC: reinstall.** Grounds — (a) the bench Pi is an instrument, not a customer; (b) the event store is *evidence* and is preserved by copying the DB file to the new path, which is a `cp`, not a migration; (c) writing and testing a path/user/unit migration script costs more than the reinstall and creates a permanent maintenance artifact for a one-time event with zero installed base; (d) a clean install is *also* the verification that the renamed distribution surface actually works end-to-end, which we need anyway. **Risk accepted:** one bench evening of downtime and one interrupted nightly cycle, both schedulable. **The counter-argument the hub should weigh:** if any acceptance evidence depends on process continuity across the window (a soak, an uptime claim), reinstall breaks it — check the criteria table before scheduling.

**INFERENCE, HIGH:** the Unix user rename is the sub-step most likely to bite. `User=homesynapse` owns `/mnt/nvme/homesynapse` on the bench (uid 1000, per `iac/bootstrap.sh`). A rename that changes the unit's `User=` without re-chowning the data tree produces a service that starts and then fails on the event store — and the bench's own recorded history already contains one exec-bit/ownership class of failure, so this is a live pattern, not a hypothetical.

### Step 6 — bench constants

| | |
|---|---|
| **Effort** | 1–2 h + **one full nightly cycle to confirm the timer still fires** |
| **Risk** | **MED, and it fails QUIETLY** |
| **Blocks** | The C-3 nightly-numbers publishing asset |

`tools/bench.sh:7` (APP path — consumes step 2's new project path), `tools/bench.sh:10` (`PAT` — consumes step 3's new package root), `tools/bench.sh:76` (events DB path), `scenarios/constants.yaml:248,253,261,262` (`~/hs-bench` config carriers + the heroless/live-basis variants), `tools/runner/README.md:190–191` (deploy path + symlink), `iac/bootstrap.sh:17–20,38` (NVMe layout + user), the `iac/` file headers, and the host/user identities (`hs-dev-1`, `homesynapse` uid 1000, `/mnt/nvme/homesynapse`).

**Verification gate: one complete nightly fire, not a manual run.** `bench.sh` failing to find the app or match the process does not raise; it produces a quiet non-result. **The digest is the instrument** — a nightly that runs and reports is the only acceptable evidence this step landed.

**OPINION, MED:** `~/hs-bench` and `hs-dev-1` are operator-surface abbreviations with no public exposure. They can carry the historical initialism indefinitely at zero cost. **REC: rename them in the same pass anyway** — not for correctness but because a half-renamed operator surface is a standing source of confusion for exactly the second-human-picks-this-up scenario X-6 names, and the marginal cost inside this WU is minutes.

### Step 7 — web-ui

| | |
|---|---|
| **Effort** | 1 h |
| **Risk** | LOW |
| **Blocks** | Nothing |

`i18n.ts` `BRAND.productName` — **one line, and the entire user-visible surface follows.** Then: `index.html` `<title>` + `<noscript>`, `web-ui/dashboard/README.md`, `package.json` name + description, `scripts/build-tokens.mjs` header, `vite.config.ts` comment, the `src/lib/**` file-header comments. **Do NOT touch the 640 `--hs-` custom properties** (D-1.8). **Do NOT touch `PROBLEM_TYPE_URI_PREFIX` in this step** — it is step 8.

### Step 8 — the frozen-contract amendment (hub ruling required, NOT a rename step)

| | |
|---|---|
| **Effort** | 30 min of edits + a contract-version stamp + FE-lane coordination |
| **Risk** | **LOW today, HIGH after launch** |
| **Blocks** | Nothing technically; it blocks *honesty* on the public error surface |

If the hub rules the prefix changes: `ProblemType.java:160` (+ Javadoc `:19`, `:213`), `contract.ts:76`, `contract.test.ts:63`, `contract-check.mjs:15`, and a **contract version bump** (currently `v1.1.2-2026-07-26`) with the amendment recorded at `context/decisions/`. Core and FE must land together or `contract-check.mjs` trips CI — which is the guard working correctly.

### Step 9 — docs forward-fold + the LICENSE/header pass

| | |
|---|---|
| **Effort** | 2–4 h (forward-facing set only) |
| **Risk** | LOW |
| **Blocks** | Public-ready in D-5 |

**Scope is bounded by law 6 — history is never rewritten.** IN scope: core `README.md` (26), `CONTEXT.md` (7), `distribution/README.md`, `web-ui/dashboard/README.md`, the docs repo `website/**` tree (188 across 20 files), and the titles/headers of the 18 Locked design docs. OUT of scope: the docs repo's `research/`, `archive/`, `governance/` trees (2,250 occurrences), the 19 legacy basenames, every historical plan and report, and the entire hivemind spine. Those keep their strings forever, by law.

**Fold the copyright/LICENSE pass into this step**, not a separate one: 1,179 files carry `Copyright (c) … NexSys`, both `LICENSE` files are all-rights-reserved proprietary, and the docs LICENSE carries a *third* company string ("NexSys Technologies"). **The Apache-2.0 flip rewrites this exact file set.** Its *timing* is gated on X-1 (entity formed + IP assigned) and is a D-4 question, not a step this runbook schedules.

### D-2 summary — the honest total

| Step | Effort (focused h) | Risk |
|---|---:|---|
| 1 GitHub org + repos ⚠ | 0.5–0.75 | LOW now / HIGH later |
| 2 Gradle | 1–2 | MED |
| 3 JPMS + packages ⚠ | 3–5 | MED / HIGH at the pins |
| 4 CI | 0.25 | LOW |
| 5 Pi redeploy ⚠ | 2–3 + a verification run | **HIGH** |
| 6 Bench constants | 1–2 + one nightly | MED (quiet failure) |
| 7 web-ui | 1 | LOW |
| 8 Contract amendment | 0.5 | LOW now / HIGH later |
| 9 Docs + headers | 2–4 | LOW |
| **Total** | **~11.5–18.5 h** | — |

**OPINION, HIGH — this is 2–3 working days, not an afternoon, and the charter should budget it that way.** The word "rename" undersells it: three of nine steps are one-way doors, one carries live state, one fails vacuously green, and one is a frozen-contract amendment. **The single largest risk in the whole package is treating it as a sed.**

---

## D-3 — THE ACQUISITION CHECKLIST

**ANTI-ACTION, restated at the top where it cannot be missed: ACQUIRE NOTHING BEFORE THE RULING.** This checklist exists so that acquisition takes one hour instead of one week. Every row is name-agnostic; the leading candidate's own screens live at `context/strategy/brand-program/2026-07-23_domain-handle-claims-refresh.md` and **transfer to this checklist only if G-2 ratifies that candidate — they are void on any other branch.**

### D-3.1 Domains

**Wholesale anchor, FACT, HIGH:** Verisign's `.com` wholesale price is **$10.26/yr rising to $10.97/yr effective 2026-11-01** ([Domain Name Wire, 2026-04-23, accessed 2026-07-31](https://domainnamewire.com/2026/04/23/breaking-verisign-raising-wholesale-com-prices/)). At-cost registrars (Cloudflare Registrar states it sells "at cost, for the exact price offered by registries… no markups and no hidden fees" — [accessed 2026-07-31](https://www.cloudflare.com/application-services/solutions/low-cost-domain-names/)) land near that; conventional retail adds a few dollars plus ICANN's $0.18 fee. **Per §0.3 limit 2, the ranges below are anchored inference, not quoted prices.**

| Priority | Row | Est. first-year | Speed if unregistered | Note |
|---|---|---|---|---|
| **P0** | `{product}.com` | $11–22 **if open**; **aftermarket if held** | Instant / **days–weeks** | The one row that can blow the budget and the schedule. If held, it is a negotiation, not a purchase |
| **P0** | `{ORG}`-pattern fallback `.com` (`get{product}.com` / `{product}hq.com`) | $11–22 | Instant | **Buy this even if `{product}.com` is open** — it is the launch's insurance against a stalled negotiation |
| **P1** | `{product}.dev` | ~$12–20 | Instant | Natural docs/developer surface for a local-first product; HSTS-preloaded TLD |
| **P1** | `{product}.app` | ~$14–22 | Instant | HSTS-preloaded |
| **P2** | `{product}.io` | ~$32–60 | Instant | Historically the dev-infra default; priced accordingly |
| **P2** | `{product}.co`, `.tech` | ~$12–35 | Instant | Only if the family is already partly held |
| **P3** | Defensive: the single closest misspell + one common TLD variant | ~$11–25 each | Instant | **Cap the defensive set at 2–3 rows.** Defensive registration is unbounded by construction; the fence is optional taste |

**FACT, HIGH — the cautionary exhibit, and it is ours:** `homesynapse.com` is a **third party's live countdown page under a HomeSynapse logo** (adjudication C-5). A name we used internally for the entire life of the project is publicly occupied by someone else's launch. **INFERENCE, HIGH:** the lesson is not "buy more domains," it is **"the gap between choosing a name and holding its `.com` is the window in which this happens."** D-5 closes that window to hours.

**Two one-minute checks still owed by Nick** (standing wait-state items, both from C-5, both unresolved in the record I read): is `homesynapse.com`'s registrar ours? Is GitHub user `homesynapse` (ID 257191284) ours? Plus the 07-23 refresh's open item, held in token form: is the leading candidate's closest-misspell `.com` (the double-letter variant that refresh probed) already Nick's, or third-party? — if third-party, accept the fence and move on.

### D-3.2 GitHub `{ORG}` — free, instant, and the namespace trap

| Row | Cost | Speed | Note |
|---|---|---|---|
| Org `{ORG}` | **$0** | **Immediate** | Free tier is sufficient for public repos |
| Contingency: `{org}hq` / `get{org}` / `{org}-io` pattern | $0 | Immediate | **Already RULED as canonical uniformly (2026-07-23)** — no G-2-day decision needed |

**FACT, HIGH — the trap, and the reason the ruled pattern matters:** GitHub users and orgs share ONE namespace, so a dormant *user* account blocks org creation. And GitHub will not free it on inactivity: *"We do not accept requests to release, transfer, or reclaim usernames on the basis that they appear inactive or unused"* — *"Valid trademark-related complaints are the only requests we review for possible release of a username that is already claimed"* ([GitHub Username Policy, accessed 2026-07-31](https://docs.github.com/en/site-policy/other-site-policies/github-username-policy)).

**INFERENCE, MED:** the trademark route is real but is (a) counsel-adjacent, (b) only available *after* registration, and (c) discretionary. **It is a post-launch recovery path, never a G-2-day plan.** The ruled house-suffix pattern is what makes step 1 unstallable.

### D-3.3 Package, image, and social namespaces

| Namespace | Cost | Speed | Note |
|---|---|---|---|
| npm scope `@{org}` | $0 | Immediate | Consumes `@homesynapse/dashboard` (D-1.4). Scope should match the GitHub org |
| Docker Hub `{org}` | $0 | Immediate | The product distributes as an image — this is load-bearing, not optional |
| PyPI `{product}` | $0 | Immediate | Defensive only; nothing in the stack is Python |
| Maven Central `{product-namespace}` | $0 | **days** | ⚠ **Requires domain-ownership verification.** Only if we ever publish artifacts; not a launch dependency. **Sequence it after the `.com` lands** |
| Social handles, `{org}hq`-class **uniformly** | $0 | Immediate | **RULED 2026-07-23** — uniformity beats opportunism; claim the bare name defensively where free, but never as canonical |
| YouTube / X / Instagram / TikTok / LinkedIn / Reddit | $0 | Immediate, but **logged-in desk work** | Automated probes are blocked by robots/login walls in every prior pass — **the 5-minute logged-in check on G-2 morning is the only reliable screen** |

**Which channels we actually claim vs. staff** is L-B's question (Q-5), not this lane's. **Claiming is cheap and defensive; staffing is a fall-semester attended-hours commitment.** D-3 claims; the charter staffs.

### D-3.4 Filing costs — pointer only, plus one honest correction

The brand decision package §4 holds the banked benchmarks (comprehensive search $1,200 PAID; ~$550/class government-fee budget for a custom-ID filing; the $3,000 whole-US bundle as the phase-2 benchmark ceiling; ~$4–6k/mark for the foreign wave). **This lane does not re-derive them and does not price counsel's work.**

One dated check attempted and partially blocked (§0.3 limit 1): the USPTO's own fee pages returned **403 and 404** to this session on 2026-07-31. A secondary source confirms the January 18, 2025 restructure **eliminated the TEAS Plus ($250) / TEAS Standard ($350) tiers in favor of a single $350 base fee per class plus surcharges** ([tmarkmetric, accessed 2026-07-31](https://tmarkmetric.com/insights/uspto-trademark-fees-2026)) — **FACT of the restructure, MED confidence on currency, and the surcharge amounts were NOT verified.** The decision package's ~$550/class custom-ID budget is arithmetically consistent with $350 base + a custom-identification surcharge, which is corroboration, not confirmation. **Read the USPTO fee schedule in a browser before any spend.**

### D-3.5 The acquisition run — what "one hour" actually looks like

Ordered, with the parallelism marked, so G-2 day is execution and not decision:

1. **(5 min)** Logged-in desk check: the 5 social handles + npm user + the `{product}.com` registrar status. *Serial — everything else keys off it.*
2. **(10 min)** `{product}.com` **or** the pattern fallback. If the primary is held: **buy the fallback immediately and open the negotiation in parallel.** Do not let a broker set the launch date.
3. **(5 min, parallel)** `.dev`, `.app`, and the ≤3 defensive rows at the same registrar.
4. **(5 min, parallel)** GitHub `{ORG}` — free, immediate.
5. **(10 min, parallel)** npm scope, Docker Hub org, PyPI defensive.
6. **(15 min, parallel)** Social handles, `{org}hq`-class uniformly.
7. **(5 min)** Log every acquisition — **registrar, date, price** — into the counsel lane's next inventory pass. *This is a standing discipline from the 07-23 refresh §D, not a new rule.*

**Total ≈ 55 min if `{product}.com` is open. If it is held, the fallback is claimed in the same hour and the negotiation runs on its own clock — D-5 is explicitly designed not to block on it.**

---

## D-4 — THE CLINIC / ENTITY PREP PACKET (X-1 operationalized)

**NOT LEGAL ADVICE. Every item below is a QUESTION, by construction.** Counsel and the clinic own the answers. This lane's job is to make sure no question is discovered late.

### D-4.0 What a law-school IP clinic actually is (FACT-tier context that shapes the questions)

The USPTO **Law School Clinic Certification Program** covers **60+ participating law schools** where students, supervised by faculty, provide **pro bono** IP services. On the trademark side students draft and file applications, handle office actions, and correspond with examining attorneys. **Client acceptance is discretionary per school, and each school has a defined geographic service area** ranging from a single state to nationwide ([USPTO, accessed 2026-07-31](https://www.uspto.gov/learning-and-resources/ip-policy/public-information-about-practitioners/law-school-clinic-1)).

**INFERENCE, HIGH — and this is the structural point that generates Q-6 below:** a *trademark* clinic is chartered for trademark prosecution. **Entity formation, IP assignment, and university-policy negotiation are transactional/business-law work, which is typically a DIFFERENT clinic or a different engagement entirely.** X-1 names two distinct acts (form the entity; assign the IP) and the trademark filing is a third. **Do not assume one intake covers all three.** Q-6 asks this first, because its answer determines whether one conversation or three are needed — and the Aug-12–13 charter needs that number.

### D-4.1 The question list

**A. Entity**

1. For a solo-founder software company that intends to release its core under Apache-2.0 and hold a trademark: what entity type, and in what state? What actually turns on the choice at this stage versus what can be changed later at low cost?
2. Does the answer change because the founder is a student, and because the work is aligned with a university capstone?
3. What is the realistic timeline from "decide" to "formed and able to own IP and be the applicant-of-record on a filing"? **What is the *earliest* date the entity could be the owner at filing?** *(This is the scheduling question the whole G-2 sequence hangs on.)*
4. What ongoing obligations does formation create — registered agent, annual reports, franchise tax, separate accounts — and what is the realistic annual carrying cost?

**B. IP assignment**

5. What instrument assigns founder-personal IP (existing code, docs, designs, the brand assets) into the entity, and what does it need to recite to be effective?
6. Does the assignment need to be recorded anywhere, and does it need to precede the Apache-2.0 flip, the trademark filing, or both?
7. What happens to work product created *before* formation — is a single assignment at formation sufficient, or does each pre-formation artifact need separate treatment?
8. Are there contributions from anyone other than the founder in the repositories today, and if so what does that change? *(Bring-list item 1 exists so this can be answered from evidence rather than memory.)*

**C. University IP policy × capstone alignment**

9. What is this university's IP policy for student-created software, and does it claim any interest in work created by a student outside of coursework?
10. **Does aligning the project with a capstone change the university's claim** — and if so, is there a written acknowledgement, waiver, or carve-out that is normally available *before* the capstone begins?
11. Does use of any university resources (facilities, licensed software, advisor time, funding) alter the analysis?
12. Is there a conflict between the university's policy and the entity's ownership, and if so, what is the standard order of operations to resolve it cleanly? **What is the deadline by which it must be resolved to avoid a problem at the capstone's start?**

**D. Trademark filing scope**

13. On the Pelton comprehensive search results: what filing scope is supportable, and in which classes? **Class 009 is the primary; is Class 042 warranted at filing or later?** *(The brand package prices 9+42 now with 45/11 later — is that sequencing sound?)*
14. Standard characters first, logo later as a separate filing — is that still the right sequence given the results?
15. **What is the ideal owner-at-filing given the entity timeline in Q-3** — the founder personally, or the entity? What is the cost and risk of filing personally and assigning later versus waiting for formation?
16. Intent-to-use versus use-in-commerce, given that nothing is public yet and launch is deliberately gated? **What starts the clock, and what is the risk of filing ITU before a launch date is certain?**
17. On the quiet-parent companion mark: does the ratified architecture (one consumer mark forward, the parent legally real but publicly quiet) change the filing recommendation for the parent, and does the parent need a filing at all at this stage?
18. What use, if any, is safe *before* the filing — and specifically, **does a public GitHub repository under the new name constitute use?** *(This is the single question that gates the entire D-5 sequence.)*

**E. Apache-2.0 flip timing**

19. Can the flip precede formation and assignment, or must it follow? What is the actual risk of flipping while the IP is founder-personal?
20. The core LICENSE says `Copyright (c) 2026 NexSys. All rights reserved.` and the docs LICENSE says `Copyright (c) 2025-2026 NexSys Technologies. All rights reserved.` — **neither string is a formed entity and they are not the same string.** What should the copyright line say at the flip, and does the inconsistency create any problem to clean up?
21. What NOTICE / attribution / header discipline should accompany the flip across ~1,179 files?
22. Does an Apache-2.0 release affect the trademark position — and what is the standard way to reserve the mark while granting the patent and copyright licenses the license requires?
23. Third-party licensing: the design record contemplates a converter-database pipeline built on data from other ecosystems. **What licensing question should we be asking about ingesting third-party device data, and is that a question for this clinic or for outside counsel?** *(Flagged, not asked in depth — L-B owns the substance.)*

**F. Scope of the engagement**

24. **Does this clinic handle entity formation and IP assignment, or only trademark prosecution?** If only the latter, who handles the former, and what does that cost?
25. What is the clinic's geographic service area, and does the founder qualify?
26. What is the intake timeline, and does it align with an academic calendar? **What is the latest date to apply for the coming semester?** *(A clinic that starts in September cannot serve an August need — this question is why the packet exists now.)*
27. What conflict-of-interest checks apply, and could the university's own IP interest (Q-9–12) create a conflict for a university-run clinic? *(Flagged as a possibility to raise, not as an assertion.)*
28. When does a matter exceed the clinic's scope and require outside counsel-of-record, and how is that handoff normally handled?
29. What does the clinic need from the client — documents, decisions, response turnaround — and what does it expect the client to do independently?

### D-4.2 The bring-list

1. **The repository inventory** — 4 repos, 1,735 tracked files, 2 GitHub namespaces (one an org, one a personal account), current LICENSE state on both licensed repos, and the contribution history. **D-1 IS this document; it answers Q-8 from evidence.**
2. **A one-paragraph invention description in plain language.** Draft text, unratified, tokens held:

   > *{PRODUCT} is a local-first automation platform for homes and buildings. It runs entirely on the owner's own hardware — a Raspberry Pi is the reference target — with no dependency on a vendor cloud. Its distinguishing property is that it keeps a permanent, tamper-evident, append-only record of every state change and every action, so the system can always answer what happened, in what order, and why — including why an automation did NOT fire, and whether a device actually confirmed a command rather than merely being told to act. It is written in Java, stores its record in SQLite, and communicates with devices over Zigbee. {COMPANY} is the company; the core software is intended for release under the Apache License 2.0.*

   *(Deliberately free of positioning language. The D5 language law binds any messaging text; a clinic intake is not the place to argue a category.)*
3. **The brand decision-package pointer** — `context/strategy/brand-program/2026-07-22_brand-architecture_decision-package.md` (Architecture C ratified 2026-07-23: one consumer mark forward, parent legally real and publicly quiet, editions by descriptor) plus `2026-07-23_domain-handle-claims-refresh.md` and the counsel-package `2026-07-15_entity-status-note.md`.
4. **The capstone linkage** — the course, the term, the advisor, the deliverable, and how the project maps to it. **Needed before Q-9–12 can be answered.** *(Not in the record I read; Nick supplies it.)*
5. **The Pelton comprehensive search + written analysis** (~Aug-5) — the instrument the Section D questions are asked *against*. **The clinic conversation is materially better after it lands than before.**
6. **The engagement tracker** — `context/strategy/counsel-package/2026-07-21_engagement-tracker.md`, so the clinic sees what is already engaged and paid.

**OPINION, HIGH — the single most schedule-critical item in this entire package is Q-26.** Clinic intake runs on an academic calendar. If the coming semester's intake closes before Nick applies, X-1 slips by a full term — and X-1 gates the Apache-2.0 flip, which gates public launch. **The clinic inquiry is already drafted and already ruled GO (v43 beat 1). It is a wait-state item with a hard external deadline nobody controls. Send it.**

---

## D-5 — THE DAY-OF-G-2 RUNBOOK

**From "counsel rules" to "public-ready."** Owners: **N** = Nick · **H** = the hub · **L** = a lane session. Durations are focused-work, not elapsed. **This runbook assumes the GREEN branch** (the name reads clear-enough); §5 of the decision package governs the adverse branches, and G-0 below routes to them.

**Standing constraint that shapes everything below: no public use of any candidate mark before G-2** — and per D-4 Q-18, **whether a public repo under the new name is "use" is an open question for counsel.** Phases 1–3 are all private. **Phase 4 is the only irreversible one, and it does not start until Q-18 is answered.**

### G-0 — The branch check (N, 15 min, blocks everything)

Read the Pelton comprehensive search + written analysis. **Rule R-1: the name.** Then route:

- **GREEN** → this runbook, from G-1.
- **ADVERSE on the leading candidate** → the ruled adverse-branch instrument (knockout screen + file on the fallback, ~$300–600); the brand criterion of record forces the real question back to Nick — accept the evocation loss, or re-run the candidate funnel. **Architecture C is name-agnostic and does not change.** This runbook resumes at G-1 once a name exists.
- **ADVERSE compound** → decision-package §5 branch 3.

**Everything after G-0 is name-agnostic. That is the whole point of the token law.**

### Phase 1 — Fill the tokens (H + N, ~1 h, blocks phases 2–4)

| # | Act | Owner | Dur | Blocks |
|---|---|---|---|---|
| 1.1 | Record the ruling verbatim at `context/decisions/`; stamp the brand program's R-1-HELD state as RESOLVED | H | 20 min | The spine's authority for every downstream act |
| 1.2 | Resolve `{PRODUCT}`, `{COMPANY}`, `{ORG}` to strings; resolve the derived machine forms — `{product}` (DNS label / unit / directory), `{product-namespace}` (the reverse-DNS Java root), `{org}` (registry namespace) | N + H | 20 min | **Everything.** Nothing below is executable until these five strings exist |
| 1.3 | Confirm the `{org}hq`-class handle pattern against the ruled uniformity rule | H | 10 min | D-3 phase 2 |
| 1.4 | Name the `{product-namespace}` explicitly and check it as a Java identifier (no reserved words, no hyphens, lowercase segments) | H | 10 min | D-2 step 3 — **a namespace that will not compile discovered at step 3 costs hours** |

### Phase 2 — Acquisitions (N, ~1 h, mostly parallel)

Run **D-3.5** exactly as written: the 5-minute logged-in desk check, then `{product}.com` or the pattern fallback, then domains / GitHub `{ORG}` / package registries / socials in parallel, then the acquisition log.

**Two hard rules.** (1) **The `{product}.com` negotiation NEVER blocks the sequence** — if the primary is held, claim the pattern fallback in the same hour and let the broker run on its own clock. (2) **GitHub `{ORG}` is claimed in this phase even though it is not used until phase 3** — it is free, instant, and the namespace is first-come-first-served with no inactivity reclaim.

**Blocks:** phase 3 step 1 needs `{ORG}` to exist. Nothing else in phase 3 depends on phase 2.

### Phase 3 — Migration execution (L + N, ~2–3 working days, PRIVATE)

**The hub authors the WU first** (½–1 day, H) — D-2 is the sizing input, not the instruction. Then execute D-2 steps 1→9 in dependency order, with these gates:

| Gate | After step | Evidence required |
|---|---|---|
| **G-A** | 2 (Gradle) | `./gradlew check` green **and** the new `installDist` launcher path recorded |
| **G-B** | 3 (packages) | ⚠ **The planted-violation negative control goes RED.** A green suite is NOT evidence — see D-2 step 3 |
| **G-C** | 4 (CI) | All three workflows green on the renamed tree |
| **G-D** | 5 (Pi) | Clean install from the renamed distribution boots and serves |
| **G-E** | 6 (bench) | **One complete NIGHTLY fire reports a digest** — not a manual run |
| **G-F** | 7–9 | FE + core land together (`contract-check.mjs` is the guard); forward-facing docs consistent |

**Repos stay PRIVATE through this entire phase.** Nothing here is public use of anything.

### Phase 4 — The LICENSE flip (N + H, ~2 h of work, gated on X-1, NOT on phase 3) ⚠

**This is the irreversible one, and it is the step this runbook most wants to slow down.**

| Precondition | Source | State in the record I read |
|---|---|---|
| Entity formed | X-1 | **NOT DONE** — X-1 verbatim, token-substituted: "{COMPANY} is a locked NAME; no record read shows a formed ENTITY" |
| Founder IP assigned into the entity | X-1 | **NOT DONE** |
| Counsel/clinic has blessed the flip's timing relative to formation and assignment | D-4 Q-19–22 | **NOT ASKED** — the clinic inquiry is drafted and ruled GO, not sent |
| The copyright line's correct text is known | D-4 Q-20 | **NOT ANSWERED** — and three inconsistent strings are in the tree today |

Acts, once the preconditions hold: replace both `LICENSE` files with Apache-2.0; rewrite the header across **1,179 files** with the blessed copyright line (**fold into D-2 step 9 — same file set, one pass**); add `NOTICE` if counsel advises; state the trademark reservation per Q-22.

**OPINION, HIGH — phase 4 is the true critical path of the entire launch, and it is the one phase no amount of engineering effort shortens.** Phases 1–3 are within our control and take days. Phase 4 waits on an entity, an assignment, and a clinic intake calendar that answers to a semester. **The charter should treat X-1 as the launch's long pole and D-2 as the short one.** Reversing that intuition — treating the code migration as the hard part — is the failure mode this deliverable exists to prevent.

### Phase 5 — Public-ready (N + H, gated on phase 4 AND on D-4 Q-18)

| # | Act | Owner | Dur | Blocks / Note |
|---|---|---|---|---|
| 5.1 | **Confirm with counsel that a public repo under the new mark is safe use** (Q-18) | N | — | ⚠ **HARD GATE. Nothing below runs until this is answered.** |
| 5.2 | Flip the repos public | N | 15 min | The C-4 artifact-first shape requires a shipped, runnable repo |
| 5.3 | The X-2 pre-launch minimum: `SECURITY.md` + a disclosure channel + a stated response posture; signed release artifacts | H authors, N rules | 2–4 h | ⚠ **A truth/trust brand invites adversarial scrutiny on day one.** Do not go public without it |
| 5.4 | The X-3 governance minimum: `CONTRIBUTING.md`, code of conduct, DCO-vs-CLA ruling, triage posture | H authors, N rules | — | **L-B owns the substance (Q-2/Q-3); L-A only marks it as a phase-5 blocker** |
| 5.5 | The C-2 sleepy/battery position paper — **REQUIRED BEFORE ANY PUBLIC AVAILABILITY CLAIM** | H | — | Adjudication C-2 names it a charter deliverable |
| 5.6 | The X-5 safety/liability language (not-a-life-safety-system) + the A-2 honesty discipline: **mechanism claims, never speed claims** | H | — | A-2 — our windows are numerically identical to Z2M's; a speed claim is falsifiable |
| 5.7 | The X-4 written telemetry ruling, stated once in the repo | N rules | 30 min | Cheap now, expensive retrofitted |
| 5.8 | Launch messaging set per **C-1**, with the **D5 language law binding every line** | H | — | The floor is MISSING from the field, not superior. Never restate as deterministic-beats-model |
| 5.9 | Then and only then, the C-4 shape: repo-first → **community-submitted** Show HN (mechanism-forward title, grievance frame) → selfh.st → YouTube weeks later. **Product Hunt: DROPPED** | N | — | **Community-submitted means we do not post it.** That constrains timing in a way we do not control |

### D-5 dependency summary

```
G-0 ruling (15 min)
 └─> Phase 1 tokens (1 h) ──> Phase 2 acquisitions (1 h) ──> [{ORG} exists]
                          └──> Phase 3 migration (2–3 days, PRIVATE) ──> gates G-A..G-F
                                                                          │
X-1 entity + assignment ── clinic intake ── Q-19..Q-22 ──> Phase 4 LICENSE flip ⚠
                                                             │
                                             D-4 Q-18 ──> Phase 5 public-ready
                                                             └─> 5.3 SECURITY + 5.5 C-2 + 5.6 X-5 + 5.8 C-1
                                                                  └─> 5.9 the C-4 launch shape
```

**The shape of it in one sentence: phases 1–3 are ours and take days; phase 4 is counsel's and the university's and takes as long as it takes; phase 5 is bounded by phase 4 and by a community we do not control.**

---

**Sources (web, all accessed 2026-07-31):**

- [GitHub Docs — Renaming a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository)
- [GitHub Docs — Transferring a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository)
- [GitHub Docs — Renaming an organization](https://docs.github.com/en/organizations/managing-organization-settings/renaming-an-organization)
- [GitHub Docs — GitHub Username Policy](https://docs.github.com/en/site-policy/other-site-policies/github-username-policy)
- [USPTO — Law School Clinic Certification Program](https://www.uspto.gov/learning-and-resources/ip-policy/public-information-about-practitioners/law-school-clinic-1)
- [Domain Name Wire — Verisign raising wholesale .com prices (2026-04-23)](https://domainnamewire.com/2026/04/23/breaking-verisign-raising-wholesale-com-prices/)
- [Cloudflare — Low-cost domain names (at-cost policy; no per-TLD table published)](https://www.cloudflare.com/application-services/solutions/low-cost-domain-names/)
- [tmarkmetric — USPTO trademark fees 2026 (secondary source; USPTO's own fee pages returned 403/404 to this session)](https://tmarkmetric.com/insights/uspto-trademark-fees-2026)
- [Apache Software Foundation — Source header and NOTICE policy](https://www.apache.org/legal/src-headers.html)

---

## WHAT CHANGES OUR PLANS

Seven findings, each one sentence plus its evidence pointer. Written last, written hard.

1. **The migration is 2–3 working days across nine steps, not an afternoon of renaming — and three steps are one-way doors, one carries live state, one fails vacuously green, and one is a frozen-contract amendment; the charter must budget it as a real WU with a clean-install verification, not as a chore.** → D-2 summary table (~11.5–18.5 focused hours); D-1.11.

2. **The fleet is split across TWO GitHub namespaces and one of them is a personal account (`nexsys-io` holds core+docs; `nixmith` holds bench+skills), so step 1 is a consolidation, not a rename — and this was not in the record.** → D-1 header, `git remote -v` ×4.

3. **`HomeSynapseArchRules.java`'s 37 string-literal package pins fail SAFE: a missed pin yields a GREEN build with architecture enforcement silently switched off, so the WU must plant a deliberate violation and confirm RED before the step is called done.** → D-1.3; D-2 step 3 negative control; the north-star's own harness-enforces symmetry is what is at stake.

4. **X-1 — not the code — is the launch's long pole, because the LICENSE flip is gated on a formed entity, an executed IP assignment, and a clinic intake that answers to an academic calendar; the clinic inquiry is drafted and ruled GO and remains unsent, and Q-26 (the intake deadline) is the single most schedule-critical unknown in this package.** → D-5 phase 4 preconditions table; D-4 §F; pm-handoff v43 beat 1 X-1.

5. **The frontend already paid the rename bill — `BRAND.productName` in `i18n.ts` makes the entire user-visible product rename ONE LINE — while the frozen `https://homesynapse.local/problems/` contract prefix is a genuine amendment that is free exactly once, right now, and expensive forever after launch; the charter should rule that prefix explicitly rather than let it ride as a string.** → D-1.8, D-1.9; contract stamp `v1.1.2-2026-07-26`.

6. **Renaming core without touching the bench silently kills the nightly regime — `bench.sh:7` embeds the Gradle project path and `bench.sh:10` embeds the JPMS package root, and neither failure raises an error — which puts the C-3 nightly-numbers publishing asset (the category's only precedent-free differentiator) at risk from a step that looks unrelated.** → D-1.10; D-2 step 6 gate G-E: one complete nightly fire, not a manual run.

7. **Three inconsistent proprietary company strings ship in the tree today — `NexSys` (core LICENSE), `NexSys Technologies` (docs LICENSE), and 1,188 `Copyright (c) … NexSys` file headers — against a north star that publicly states "the core is Apache 2.0"; the flip and the header rewrite touch the SAME 1,179 files as the rename, so they are one pass if sequenced together and three if not.** → D-1.7; D-2 step 9; D-4 Q-20.

**Proposed charter disposition (the lane recommends; the hub adjudicates; the charter orders):** send the clinic inquiry **this week** — it is the only item on this list whose deadline is set by someone else. Everything in D-2 waits for G-2 by design and costs nothing to hold. Everything in D-3 costs under an hour once a name exists. **The one thing that cannot be compressed later is the one thing that has not been started.**

