<!--
file: context/audits/2026-09-14_v74-b5_HERO-1d_intake_two-layer-audit.md
purpose: The hub's two-layer intake of HERO-1d's return (`context/audits/2026-09-13_HERO-1d_return.md`, 11,613 B): the claims read critically (§1), the hub's re-execution at the bytes on the device (§2), what was not re-executed (§3), the verdict, the rulings and the register rows (§4).
audience: the hub · Nick (the verdict; the web-ui card) · FE-114's author
state-type: intake audit (FILED at v74 beat 5)
status: FILED — Mon 2026-09-14 ~06:5x CT (instrument 2026-09-14T11:53:23Z); verdict ACCEPT; the landing = the web-ui card (`git add -A web-ui/dashboard`, 17); frontend CI on Nick's push is the gate of record
last-verified: 2026-09-14 (v74 beat 5)
-->

# HERO-1d — intake, two layers

## §0 Card
- **The return:** at the named path; last line = its byte count (11,613); §0 3,132 B. Returned Sun 09-13 ~21:5x CT (the lane ran the same evening it was pasted); Nick relayed it Mon 09-14 ~06:4x CT.
- **Verdict: ACCEPT.** 17 = 14 M + 3 A, all under `web-ui/dashboard/`, nothing outside (the whole core porcelain = the dashboard's 17); +350/−39 tracked; 0 existing `expect` lines removed, 43 added; 24 keys added to the catalog (25 added lines less the D6-modified `explain.action.pending.color`); six byte-identity spot checks 6/6; `colour` 11 residual (the five named sites 0); SPEC: 24 rows in the charter's form + the amendment line, D6's three lines; the lint block with its three selectors present. P2 and P5 FAILED on their counts and the lane said so with the reasons — the instrument's reach and the charter's undercount — both honest, both filed below.
- **The landing:** the web-ui card (`git add -A web-ui/dashboard`, 17; the msg file `_scratch/v74/2026-09-14_core_HERO-1d_commit-msg.txt`); `frontend.yml` on the push is the gate of record; the push is a counter sample (`CI: <sha> frontend … check … bus-soak …`).
- **Rulings (the hub's, reversible by REVERT):** (1) the product copy's dialect of record is US English — the catalog's keys already say `color`; `Cancelled` stays (it mirrors the enum and is accepted US usage); the residual `recognise` · `behaviour` · `neighbours` and the SPEC-prose/`states.html` `colour` lines are TEXT changes and go through §7 at FE-114 (IR-13). (2) The lint's pattern is widened at FE-114 (IR-12). (3) The two unconsumed terminal rows (`explain.terminal.interrupted` "Cut off before it finished."; `.noSteps`) are text changes ruled in FE-114's charter, not here. (4) `format.ts` `pendingHint`'s literal = the catalog's `explain.action.pending.color` — a zero-visible swap at FE-114 (IR-14).

## §1 The claims, read critically
The §0 card is specific: the instrument (node 22.6 · vitest 4.1.10 · ESLint 9.39.4 installed vs 10.7.0 locked — the lint also run under `npx eslint@10.7.0`, exit 0), the census with paths, the red-first table per row with the preservation rows named (the condition line and the cascade link were green at HEAD because their keys already equalled the literals — the charter predicted red; the lane disclosed it), P1–P5 adjudicated with two failures owned, the gates with counts (`npm run verify` GREEN: 27 files / 480 tests; the bundle 70.3 KB / 100 KB; the contract check 11 endpoints), five deviations by tag. §3 carries the finding that matters for the next charter: the charter's regex needs three bare words after a capital and cannot see apostrophes, two-word runs or a capital before an interpolation — nine of the hub's sites — and sees two the hub omitted; the rows keyed all of them regardless. The UK/US census is counted, not changed, per D6's own rule.

## §2 The hub's re-execution (device, 2026-09-14T11:53Z)
1. **Porcelain:** core 17 rows, every path under `web-ui/dashboard/`; 3 `??` (`CausalChain.terminal.test.tsx`, `RunsView.test.tsx`, `RunChainView.test.tsx`); `git diff --numstat` +350/−39 (the return's numbers exactly); SPEC +29/−3 at numstat (the return says +28/−4 — the same diff counted differently at a moved line), `eslint.config.js` +26/−0, `i18n.ts` +39/−1.
2. **No expectation removed:** `git diff -U0 -- 'web-ui/dashboard/**/*.test.ts*' | grep -cE '^-\s*expect'` = 0; added = 43.
3. **The keys:** 25 added key lines in `i18n.ts`, one of them the modified `explain.action.pending.color` → 24 new keys, the names the return lists (D1 ×7 · D2 ×4 · D3 ×5 · D4 ×8).
4. **Byte-identity, six spot checks:** "Nothing was changed: the planned step ended without sending a command." · " (recovered from the recorded reason — this record predates the current hub software)" · "← See what triggered this run" · "Choose the automation you expected to run." · "Pick a run to see exactly why it fired, step by step." · "Done — one outcome has not settled yet." — each present once in the catalog, character for character.
5. **`colour`:** `grep -rni colour web-ui/dashboard/src web-ui/dashboard/design | wc -l` = 11 (the return's 11); the five named sites 0.
6. **SPEC:** 24 lines ending `| HERO-1d |`; the amendment line once.
7. **The lint:** the config block present with the three selectors and the message. A python approximation of the three patterns over the six files reads 2 "hits" after — both comment text my line-crossing regex captured, not JSX text nodes — and ~14 at HEAD by the same approximation; the AST truth (0 after; 11 at HEAD) is the lane's ESLint run, confirmed by CI's `npm run lint` on the push.
8. **MODULE_CONTEXT:** the HERO-1d paragraph present (2 mentions).

## §3 Not re-executed (disclosed)
`npm run verify` (vitest, tsc, the build, the bundle check) — `node_modules` lives outside the mount on the Windows desk; the device VM has node but not the tree's modules. CI is the gate of record: `frontend.yml` on Nick's push runs lint · typecheck · test · build. The lane's ESLint AST counts (11 → 0) are accepted on the config block's presence and CI's lint, not re-run here.

## §4 Verdict, rulings, the register
**ACCEPT.** The charter → EXECUTED with the landing. **IR-8 RETIRED** on HERO-1d's landing (the lint is inside `npm run verify`). **IR-12** — the lint pattern's reach: widen to ≥2 words with apostrophes and a capital before an interpolation; add a `Property > Literal` selector for the pill objects; the lane's widened pattern read 19 at HEAD — FE-114's charter carries it as a row. **IR-13** — the register sweep: US English is the dialect of record (ruled above); the residual UK spellings and the SPEC-prose/`states.html` `colour` lines are §7 text changes at FE-114; `Cancelled` stays. **IR-14** — `format.ts` `pendingHint` (:217) duplicates the catalog's `explain.action.pending.color`; a zero-visible swap at FE-114. FE-114's charter also rules the two unconsumed terminal rows (the lane's (d)). The charter nits (the two line numbers off by four; the mirror path on the desk) are noted, no act.
