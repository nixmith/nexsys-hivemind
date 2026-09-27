<!--
file: context/instructions/2026-09-13_HERO-1c_AUDIT-CORRECTION_D3-generic-labels_D2-two-rows.md
purpose: AUDIT CORRECTION for HERO-1c — do not re-run the WU. Two items the intake ruled before the landing: D3 (the state-card labels are hero-scoped on every page) and D2 (two §7 rows the catalog lacks). Applied on top of the uncommitted HERO-1c tree; the census of the landing is re-derived at the intake.
audience: the HERO-1c correction lane (a fresh Cowork conversation; the nexsys-frontend skill) · the hub · Nick (§3 is his paste)
state-type: audit correction (small; self-contained)
status: EXECUTED — applied 2026-09-13 22:27–22:32Z (the HERO-1c return §5; RED 4 → GREEN 76 and RED 4 → GREEN 126; verify exit 0), audited ACCEPT at v73 beat 6, landed core `93390f0` — banked v73 beat 7 (Sun 2026-09-13 ~18:1x CT; instrument 2026-09-13T23:18:34Z).
-->

# HERO-1c — AUDIT CORRECTION (D3 the generic labels · D2 two rows)

## §0 The contract
- `date -u` first. Baseline: `homesynapse-core` at `fed99e8` with the HERO-1c tree UNCOMMITTED — `git status --porcelain -- web-ui/dashboard` shows 18 ` M` + 3 `??` and nothing outside the domain; stop and report otherwise. Never `git add`/`commit`/`stash`/`checkout`.
- **Do not re-run HERO-1c.** Apply the rows below only; every new assertion red before its edit (say how), then green; `npm run verify` green at the end.
- **The return:** append a `## §5 Correction` section to `nexsys-hivemind/context/audits/2026-09-13_HERO-1c_return.md` (≤2 KB: the rows applied, the red-then-green per row, the new census `N = a M + b A`, the verify counts) and end the file, in the file and printed, with a NEW last line `RETURNED nexsys-hivemind/context/audits/2026-09-13_HERO-1c_return.md <bytes>`.

## §1 D3 — the generic app pair; the hero views pass the hero rows
1. `src/lib/i18n.ts`: four keys — `"ui.loading": "Loading…"` · `"ui.error.title": "This page couldn't be loaded."` · `"ui.error.body": "The hub answered with an error. Try again."` · `"ui.error.retry": "Try again"`. (App copy, not SPEC §7: §7 is the hero's table.)
2. `src/components/feedback.tsx`: `Loading`'s default label = `t('ui.loading')`; `ErrorState` takes optional `title`/`body`/`retry` with the `ui.error.*` defaults; `OfflineState` and `ReplayingBanner` unchanged (their copy is generic).
3. `src/components/Resource.tsx`: optional `labels?: { loading?: string; errorTitle?: string; errorBody?: string }` passed through to `Loading`/`ErrorState`; the `'auth'` arm keeps "Signing in…" (HERO-1d's keyless set).
4. The three hero views pass the hero rows at their `Resource` mounts — `RunChainView.tsx:31`, `WhyNotView.tsx:61` and `:159`, `ExplainHubView.tsx:42`: `labels={{ loading: t('explain.loading'), errorTitle: t('explain.error.title'), errorBody: t('explain.error.body') }}`.
5. Tests: `feedback.test.tsx` pins the generic defaults AND the hero override; `app.errorPosture.test.tsx:103` and `EventsView.unserved404.test.tsx:175` re-point their spinner pins to `ui.loading` (non-hero pages), `WhyNotView.nullability.test.tsx:90` stays on `explain.loading`; one new assertion (in `app.errorPosture` or a view test you ground) pins that the DEVICES page's loading label is `t('ui.loading')` — RED at HEAD (it renders `explain.loading` today).
6. `web-ui/dashboard/MODULE_CONTEXT.md` hero section: one sentence — the state primitives default to the app's `ui.*` pair; the hero views pass the `explain.*` rows through `Resource`'s `labels`.

## §2 D2 — two §7 rows (the hub's text; append after SPEC `:279`, before the blank line and `## §8`)
```
| `explain.mode.notRecorded.help` | What happened to this step was not recorded. The step itself is preserved. | action step help / pill title, outcome null (HEAD's sentence, given its key) | — | 4.1 | 7 |
| `explain.mode.settledFailed.lineNoCommand` | No command was sent to {target} — this step failed{reasonClause}. | action step line, FAILED with `command` null and a named target (D2: the `act` arm is the SPEC's null verb and reads wrongly) | target·reasonClause | 4.9 | 13 |
```
Then: the two keys in `src/lib/i18n.ts` with the same strings; `verdicts.ts` `actionVerdict`'s not-recorded arm reads `t('explain.mode.notRecorded.help')` (the literal goes; the skipped mode's `''` stays by design — after this, `awk '/export function actionVerdict/,0' verdicts.ts | grep -c "help: '"` reads `1`); `CausalChain.tsx` `actionStepLine`: FAILED with `command` null and a named target renders `explain.mode.settledFailed.lineNoCommand`; tests: `verdicts.test.ts` pins the not-recorded help to the catalog (red at HEAD — the literal differs from nothing; it is the same text, so this one is green-by-construction: say so); `CausalChain.modes.test.tsx` gains the null-command FAILED row (RED at HEAD: "The command to act …"); `i18n.test.ts` pins the two SPEC strings = the catalog strings (the R3 check extended to `:280`–`:281`).

## §3 The dispatch line (Nick pastes into a FRESH Cowork conversation with `ClaudeFolder` connected)
```
date -u first. You are the HERO-1c AUDIT-CORRECTION lane for NexSys/HomeSynapse — boot as the nexsys-frontend skill. Do NOT re-run HERO-1c. Baseline: homesynapse-core at fed99e8 with the HERO-1c tree uncommitted (`git status --porcelain -- web-ui/dashboard` = 18 M + 3 ??; nothing outside). Read nexsys-hivemind/context/instructions/2026-09-13_HERO-1c_AUDIT-CORRECTION_D3-generic-labels_D2-two-rows.md WHOLE and apply §1 then §2 exactly, each new assertion red before its edit, then green; run npm run verify; never git add/commit/stash/checkout. Append §5 Correction to nexsys-hivemind/context/audits/2026-09-13_HERO-1c_return.md (≤2 KB) and end it with a new last line RETURNED nexsys-hivemind/context/audits/2026-09-13_HERO-1c_return.md <bytes>; say that line to Nick.
```
