<!--
file: context/audits/2026-10-17_HERO-U4_return.md
purpose: HERO-U4 lane return — BC10's real v1.1.7 wire as a fixture (H8 → VERIFIED), IR-174 (a)(b)(c), IR-207's rider, the §0 5–7 string audit; worktree homesynapse-core-hero-u4 at 176adad on hero-u4/real-wire-honest-hero, UNCOMMITTED.
audience: the hub (intake) · Nick
state-type: lane return
status: RETURNED Sat 2026-10-17 14:37 CT
-->

# HERO-U4 return — the real wire and the honest hero

## §0 Card
- `date -u` 2026-10-17 18:49:04Z at start (Sat 13:49 CT; CT = UTC−5); close 19:37 UTC. Instrument: Windows 11 Git Bash, node 22.6.0, npm 10.8.2 — `npm ci`, `npx vitest`, `npm run verify` RAN natively in the worktree; nothing deferred (O-8).
- Worktree: HEAD `176adad` on `hero-u4/real-wire-honest-hero`; porcelain EMPTY at start. `CONTRACT_VERSION` `v1.1.7-2026-10-11`, package.json, lock, contract.ts untouched; 0 lines outside `web-ui/dashboard/`; git read-only verbs only.
- Census N = 13 M + 2 A = 15 (`git -C homesynapse-core-hero-u4 --no-optional-locks status --porcelain -- web-ui/dashboard`). M: design/recovery-card-v1/SPEC.md · src/a11y.test.tsx · src/components/CausalChain.tsx · src/lib/api/fixtures/fixtures.stability.test.ts · src/lib/api/v117-additive.test.ts · src/lib/format.test.ts · src/lib/format.ts · src/lib/i18n.test.ts · src/lib/i18n.ts · src/lib/recovery.test.ts · src/lib/recovery.ts · src/lib/verdicts.test.ts · src/lib/verdicts.ts. A: src/components/CausalChain.commandCount.test.tsx · src/lib/api/fixtures/wire-2026-10-17-entities.ts.
- Red-first (each row's files run alone at HEAD → after): R1 2 suites fail `Failed to resolve import "./fixtures/wire-2026-10-17-entities"` → 77 pass · R2 7 fail / 93 pass (key absent ×3 · retired key resolves ×2 · `unasked` for passive-null · the 67-set) → 100 pass · R3 10 fail / 136 pass (2 keys absent · bare pill ×3 · acted headline beside commandCount 0 ×5) → 146 pass · R4 6 fail / 85 pass (the old texts) → 91 pass. Suite 780 → 813 tests, 35 files, 0 failed.
- Predictions: P1 TRUE (the 15 paths = porcelain at close) · P2 TRUE (10/10 rows validate as A1, whole and alone; 19 keys each, the eleven PRESENT typed-or-null in the emitter's order; recoveryViewPosition 2318441 after timestamp) · P3 TRUE (eight md5s identical before/after; the BC10 fixture joins the pin, 7 → 8) · P4 TRUE ((a)(b)(c) RED by the tests written first) · P5 TRUE (at HEAD the SILENT-SKIP mock renders the silentSkip headline · "Finished in 0.0s, but nothing was changed." · pill "Completed, nothing changed" — GREEN at HEAD, disclosed; the RED found: an acted headline beside commandCount 0 under a CONFIRMED / DISPATCHED / UNCONFIRMED / FAILED row — fixed) · P6 TRUE (§4: 28 rows, 6 RE-WORD).
- Gates: `npm run verify` GREEN — tokens:check · lint 0 · tsc 0 · vitest 35 / 813 · build · bundle 79.6 / 100 KB (JS 48.3 KB, +0.1) · contract 11 endpoints v1.1.7. `frontend.yml`: Nick's push.
- Tags: D-1 the record = 5,638 B JSON + LF (5,639 B), both md5s pinned · D-2 R3 spares a SKIPPED leading row (hero SPEC §3 row 5) · D-3 runs-list pill bare (no commandCount on RunSummary) · D-4 three unconsumed posture helps re-worded · FLIP-1 a11y.test.tsx:99 · FLIP-2 the Q3 (a) permanence pin · FLIP-3 verdicts.test.ts:115 · FLIP-4 lock 63 → 62, files 7 → 8.

## §1 Per-file deltas (web-ui/dashboard/)
- `src/lib/api/fixtures/wire-2026-10-17-entities.ts` A (262 L, 10,343 B, md5 6b8dbcc09960aa39b9baa452fb8a5f06): the BC10 body, 10 rows + meta, emitted by script from the record (IR-89), provenance block; `JSON.stringify` → 5,638 B md5 3dfb721e0c4b2b7aa7df41b00f468f25, + LF = 5,639 B md5 559ac60dc338068ad00313d57288115f.
- `src/lib/api/v117-additive.test.ts` +75/−3: header H8 → VERIFIED; the real-wire block (bytes/md5 · P2 whole and per row · 19 keys typed-or-null · meta order · the wire as it is · V-6); WIRE_MD5 7 → 8.
- `src/lib/api/fixtures/fixtures.stability.test.ts` +24: the BC10 body — A1, both byte counts and md5s, Bearer 0, 10 rows / 1 dark, the list dialect (no pagination; keys appended; meta + recoveryViewPosition).
- `src/lib/i18n.ts` +17/−5: −`recovery.contract.answersNoReports`; +`recovery.l2.lastRecordedCheck.notRecorded` ([AMEND]); +`explain.terminal.commands` / `.one`; 3 re-words (`explain.permanence` · `.error.body` · `.offline.body`); recovery.* stays 67.
- `src/lib/i18n.test.ts` +83/−8: the lock re-extracted by script from SPEC §7 :89–:151 minus :118 (62) + 4 null-arm + U4's row = 67; blocks R2 (a)(b) · R3 keys · R4 re-words + the banned-forms sweep; FLIP-2.
- `src/lib/recovery.ts` +7/−6: the `lead` splitter gone — L2's null arm reads its own row; `reason === null && seen === null` → `passive ? passiveDark() : unasked()`; header line.
- `src/lib/recovery.test.ts` +68/−1: (a) key + source regex · (b) undefined · (c) passive-null → R4, asked-null → R5, S2 unchanged · the 10 real rows at S3 (keys · class sentences · the Hue's L2 · data[4]'s check).
- `design/recovery-card-v1/SPEC.md` 2/2: the R4 and R5 S3 cells end with the hub's sentence, verbatim.
- `src/lib/format.ts` +14: `withCommandCount(label, count)` (integer ≥ 0, else the bare label); `causalHeadline`: COMPLETED ∧ actionCount ≥ 1 ∧ commandCount 0 ∧ leading row ≠ SKIPPED → silentSkip.
- `src/lib/format.test.ts` +24: IR-207 ×4 RED; row 5 (SKIPPED) and row 1 preserved.
- `src/components/CausalChain.tsx` +5/−1: the status label is `withCommandCount(…)` — pill, outcome step, do-nothing step, a11y step text.
- `src/components/CausalChain.commandCount.test.tsx` A (76 L): keys · P5 · the silent-skip pill · 1 command · 2 commands · the inconsistent wire · a bad count appends nothing.
- `src/a11y.test.tsx` +2/−1 (FLIP-1) · `src/lib/verdicts.ts` +6/−3 (3 posture helps) · `src/lib/verdicts.test.ts` +17/−1 (FLIP-3 + the posture block).

## §2 Gates
`npm run verify` GREEN in the worktree (§0); GREEN at HEAD too (780 tests, JS 48.2 KB). Deferred: none. `frontend.yml`: Nick's push of the merged branch. Register: R1 VERIFIED at BC10's real-wire exercise (176adad); R2 · R3 · R4 REPO-COMPLETE, LIVE-VERIFICATION PENDING (the capture's rows and the mock). DoD (skill §9) met; next WU O-9.

## §3 Pushback and observations
- O-1 The record file ends in the shell's LF: 5,638 B compact JSON + 1 = the charter's 5,639 B. Fixture and tests pin both md5s; emitter and mirror agree — P2 clean, no STOP.
- O-2 P3 names `fixtures.stability.test.ts` as the md5 pinner; the seven-file SOURCE md5 pin lives in `v117-additive.test.ts` (:243–:258). The BC10 fixture joined both.
- O-3 Design edits for the hub (beyond R2 (c)'s rows): recovery-card SPEC §7 — strike :118 (`answersNoReports`; §3 R2's S3 cell :38 still names it), add `recovery.l2.lastRecordedCheck.notRecorded`; the §3 "Amended" line (:47) for IR-174 (c). Hero SPEC §7 — add `explain.terminal.commands` / `.one`; TEXT-CHANGE rows for `explain.permanence` · `explain.error.body` · `explain.offline.body`.
- O-4 J3 T-B (176adad) records a SKIPPED row per command that issued nothing, so on that wire `isDoNothingRun`'s `actionsShown === 0` arm no longer fires for an all-skipped run: its pill reads "Completed · 0 commands" (R3) but its terminal line stays "Done in Xs."; `explain.step.nothing.hint`'s "not kept yet" is era-bound. Not widened here — O-9.
- O-5 Cross-lane ask: `RunSummary` (B3 runs list) carries no `commandCount`; the runs-list and overview pills stay bare (D-3). An additive `commandCount` on `runs[]` is the hub's contract call.
- O-6 The rule as built: a CONFIRMED / DISPATCHED / UNCONFIRMED / FAILED leading row beside commandCount 0 renders the silent-skip sentence (the terminal event's count wins); a SKIPPED leading row keeps hero SPEC §3 row 5 (D-2) — `REVERT D-2` makes it unconditional.
- O-7 `postureMeta` has no consumer (posture is not on the v1.1 wire); its "fully confirmed" · "it still works" · "never silently skipped" broke item 7 and were re-worded with pins (D-4) — `REVERT D-4` at will.
- O-8 The prior ledger (D-1 · D-2 · O3) described the Cowork shell; here `.git` resolves natively, deletes work, `node_modules/` and `dist/` are gitignored (porcelain 15 after `verify`). Preflight: Check 2 v1.1.7; Check 7 skill mirror diff empty.
- O-9 Next WU: HERO-U5 — widen the do-nothing status to commandCount 0 whatever the rows show (O-4; verdicts.ts:264–:275 + tests), and the runs-list count once the contract carries it (O-5).

## §4 R4 — the confirmation · durability · completeness strings (register §0 5 · 6 · 7)
| String(s) | Verdict | Item |
|---|---|---|
| `explain.headline.completed.confirmed` · `tail.confirmed` | KEEP | 7 — only on the device's own report |
| `explain.headline.*.dispatched` · `*.unconfirmed` · `*.expiredRestart` · `*.superseded` | KEEP | 7 — no confirmation claimed |
| `explain.mode.confirmed.label/.line/.help` | KEEP | 7 — the item's own form |
| `explain.mode.heldDispatched.*` · `timedOut.*` · `ackedSilent.*` · `expiredRestart.*` | KEEP | 7 — not settled / unknown / never reported |
| `explain.action.detail.confirmedAt(.noDelta)` · `explain.action.pending.color` | KEEP | 7 — one device's report instant |
| `explain.hub.fire.text` · `explain.hub.not.text` | KEEP | 7 — "whether the device confirmed" |
| `whyNot.headline.firedConfirmed(.noTime)` · `whyNot.pill.firedConfirmed` | KEEP | 7 — "the record says"; one run |
| `whyNot.*.actedButUnconfirmed` · `whyNot.body/link.ranFine` | KEEP | 7 |
| verdicts.ts VERDICTS helps + FALLBACK | KEEP | 7 — the device's report, as recorded |
| `postureMeta('verified_reports').help` "fully confirmed" | RE-WORD | breaks 7 → "a command can be confirmed by its own report" |
| `postureMeta('best_effort').help` "it still works" | RE-WORD | breaks 7 → "commands are still sent, but its reports are not guaranteed" |
| `postureMeta('disabled').help` "never silently skipped" | RE-WORD | breaks 7 (IR-207) → "reported as unconfirmed, not as confirmed" |
| `postureMeta('sleepy').help` | KEEP | 7 — a posture, not fitness |
| `explain.permanence` | RE-WORD | breaks 6 + 5 → "Rebuilt from the activity log. Nothing is ever removed from it, so this run stays on record." |
| `explain.chain.noDetail.body` | KEEP | 5 — no-eviction by design (INV-SA-03), not survival |
| `explain.nullName.note` · `explain.mode.notRecorded.help` | KEEP | 5 — a present fact |
| `explain.error.body` | RE-WORD | breaks 5/6 → "This page only reads the record — try again." |
| `explain.offline.body` | RE-WORD | breaks 5 → "Nothing on this page is lost. It fills in when the connection returns." |
| `explain.replaying.body` · `explain.a11y.provisional` | KEEP | 5 / 7 |
| `explain.chain.empty` · `explain.terminal.noSteps` · `explain.headline.completed.none` | KEEP | 7 — the record's own counts |
| `explain.headline.completed.silentSkip` · `explain.terminal.completed.nothing*` · `explain.step.nothing.one/.many` · `whyNot.*.sentNothing` | KEEP | 7 — commandCount 0 is the ledger's word |
| `explain.step.nothing.hint` | KEEP | 7 — true where it renders; era-bound (O-4) |
| `explain.terminal.completed(.noTime)` · `.open*` · `explain.terminal.commands(.one)` | KEEP | 7 — the status word, the count as recorded |
| `recovery.l2.lastRecordedCheck(.notRecorded)` · `.checkWindow` · `.recordEvery` · `.dueBy` | KEEP | 7 — one record, both ends named |
| `recovery.state.quiet.line.recorded(.noReport)` · `.line.edge` | KEEP | 7 — the device's own answer |
| `recovery.state.noCheckRecorded.*` · `unasked.*` · `notResponding.*` · `passive.*` · `left.*` | KEEP | 7 — says what is not known / not asked |
| `recovery.contract.metered/.floor/.passive/.fallback` | KEEP | 7 — the declared contract (R-C) |
| `recovery.act.rejoined` | KEEP | 7 — a report arrived |
RETURNED nexsys-hivemind/context/audits/2026-10-17_HERO-U4_return.md 11968
