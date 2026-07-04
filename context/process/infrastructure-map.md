<!--
file: context/process/infrastructure-map.md
purpose: The one-page map of physical/digital infrastructure a fresh agent cannot derive from code alone — remotes, CI, toolchain, bench hardware, permission surfaces. Facts here are VOLATILE-ish: verify anything load-bearing at need (pointer-not-copy applies; the spine + a fresh check outrank this page).
audience: All agents; Nick.
state-type: reference
status: CURRENT
last-verified: 2026-07-03 (v15 hub, beat 60 — authored for the wipe test; every fact below observed this date)
-->

# Infrastructure Map

## 1. Repositories and remotes (the five-repo model + one extra)

| Local (under `ClaudeFolder/`) | Remote (observed from pushes) | Purpose |
|---|---|---|
| `homesynapse-core` | `github.com/nexsys-io/homesynapse-core` (org account) | The product: Java 21/JPMS/Gradle, 20+ modules, `web-ui/dashboard/` (Preact SPA), `distribution/` |
| `homesynapse-core-docs` | (verify remote at need) | Design docs 01–17 (+18 in authoring), `governance/` (AMDs, invariant register), `research/`, `website/` (content canon + the Astro site at `website/site/`) |
| `nexsys-hivemind` | `github.com/nixmith/nexsys-hivemind` (personal account) | The shared brain: `context/` spine + protocols + lessons + instructions + audits; `coder/` + `project-manager/` = WRITABLE SKILL SOURCES |
| `nexsys-bench` | (verify at need) | The test-and-truth engine: coordinator corpus, captured fixtures (replayable event streams), phase reports |
| `nexsys-skills` | (verify at need) | The skills-system repo: `orchestrators/nexsys-frontend/` (the frontend skill's writable source) + the 4-tier scaffold (`design/` — the MIGRATED skills-architecture corpus, 14 tracked files, formerly in the unversioned skills-initiative/ — plus `disciplines/ domain/ harness/ stewardship/ sync/`, `MANIFEST.yaml`); the full build stays DEFERRED post-V1 per the 2026-06-27 ruling |
| `_scratch/`, `_archive/` | unversioned | Commit-message staging (`git commit -F`); parked material. (`skills-initiative/` is an EMPTY HUSK — its corpus migrated to `nexsys-skills/design/`; delete the directory at leisure) |

**Account split matters:** core lives in the `nexsys-io` org; the hivemind on `nixmith`. Visibility (public/private) is NOT recorded here — verify before anything secret-adjacent or before publishing links (the website's GitHub link is publish-gated on this plus W-11/W-2).

## 2. CI (gates of record — on the PUSHED commit)

| Workflow | Repo | Trigger/scope | Status (2026-07-03) |
|---|---|---|---|
| `ci.yml` (Build & Check) | core | every push — full `./gradlew check` (arch rules, count pins, graph guards) | ACTIVE, the primary gate |
| `install-smoke.yml` | core | every push — the one-command-install container smoke | ACTIVE since `652f9b3`, green streak = gate 4's install half |
| `frontend.yml` | core | path-filtered `web-ui/**` — dashboard build/verify | ACTIVE |
| `website.yml` | docs | PROPOSED (build-only, path `website/**`, sparse core checkout for tokens) | awaiting Nick's adopt ruling |

**Dependabot (core): 5 enumerated on the 2026-07-03 push — 1 critical, 1 high, 3 moderate — triage OVERDUE (standing ledger item).** Candidates: `web-ui/dashboard/package-lock.json` (→ frontend micro-WU) or actions bumps; M9.2 added no npm surface (jSerialComm is Maven). Separately: the website site's `npm audit` shows 2 (1 high) in the BUILD tree only — the shipped site has zero runtime JS.

## 3. Toolchain

Host (authoritative): Windows + MINGW64 git-bash · JDK 21 (the VM sandbox has JDK 11 — one reason in-sandbox Gradle is banned) · Gradle 8.8 via wrapper (`-Werror` rides the convention plugins — never pass it as a CLI flag) · Node/npm (dashboard + website; host esbuild fine — the SANDBOX esbuild SIGSEGVs, env-model §9) · `scripts/clean.sh` in core is BUILD-ONLY (never touches `.homesynapse/` runtime state). Claude Code: permission allow-list lives in `homesynapse-core/.claude/settings.json`; the working form is `"Bash(./gradlew:*)"` (prefix rule) — exact-string rules failed twice (M9.1, M9.2), each costing a gate round. **Root cause found + fix PROVEN (v17/M9.3, 2026-07-04): a `"Bash(./gradlew *)"` DENY-list entry was overriding every allow — deny beats allow in CC; the fix = REMOVE the deny entry + the colon-form allow + RESTART the CC session; M9.3 then ran targeted compile/test green in-session (the lane-routing shift-left is real).** Keep the git-commit/push/merge/reset/rebase denials permanently. Version catalog: `gradle/libs.versions.toml` (LTD-10 — pinned versions, deliberate updates only; license elections recorded at the catalog line, e.g. jSerialComm's Apache-2.0).

## 4. Bench (physical — Nick's desk)

`hs-dev-1` = Raspberry Pi 5. Reference coordinator: **SONOFF Dongle Plus MG24** (EFR32MG24, VID:PID `10c4:ea60`, SONOFF-branded USB descriptor strings), **FROZEN at EmberZNet 7.4.5.0 build 0 / EZSP v13** — the M9 acceptance baseline; udev-pinned at `/dev/zigbee`, black USB-2.0 port, powered/autosuspend-off; **do not reflash/touch — it is the calibrated instrument**. Wave-1 devices captured in `nexsys-bench/corpus/` + `fixtures/` (Hue LCA017 confirming; SNZB-03P motion). Wave-2 (ordered/arriving): ZBDongle-P (ZNP silicon — enables the second transport; NOTE the PortLocator same-VID:PID limitation before any two-stick topology), a BEST_EFFORT-class sleepy sensor (priority — the untested confirmability leg), an energy plug. Reference stack for cross-checks: ZHA/bellows (Home Assistant); flasher: `universal-silabs-flasher`.

## 5. Permission/secret surfaces (never cross these)

Bearer/pairing tokens and network keys: never in git, commit messages, logs, exception text, or `toString()` (INV-SE-03 class). `.homesynapse/` runtime state, `*.db`, `node_modules/`, `dist/`, build output: ignored classes — verify per env-model §10 before any staging list. The skills mirror (`.claude/skills/` cache) is read-only — writable sources are in the repos (§1); Nick syncs manually (Check 9).
