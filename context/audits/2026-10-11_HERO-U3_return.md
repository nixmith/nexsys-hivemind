<!--
file: context/audits/2026-10-11_HERO-U3_return.md
purpose: HERO-U3 frontend lane return — the recovery card's S3 column on the v1.1.7 record (build mode).
audience: the hub (two-layer intake) · Nick (the landing card after the intake)
state-type: lane return · charter: context/instructions/2026-10-11_frontend-lane_HERO-U3_recovery-card-on-the-live-record_v1.1.7_coding-charter.md (20,488 B, md5 9cb764d6…)
status: RETURNED 2026-10-12T00:35Z (Sun 2026-10-11 19:35 CT) · worktree homesynapse-core-hero-u3 @ 2a54145 on hero-u3/recovery-card-live, UNCOMMITTED
-->
# HERO-U3 — return: the recovery card on the live record (v1.1.7)

## §0 Card
**Instrument.** `date -u` 2026-10-11T23:34:58Z; CT = UTC−5. Linux VM: node 22.23.2 · npm 10.9.8 · git 2.34.1 — runs vitest and `npm run verify` on a `/tmp` copy (O3); not in the mount, not `frontend.yml`, not the Pi. HEAD `2a54145`, porcelain EMPTY at start [D-1]; main checkout porcelain 0 at start and close.

**Census** (porcelain `-- web-ui/dashboard`, at close): **N = 24 = 21 M + 3 A**; 23 in `src/`, 1 the hub's. M `scripts/contract-check.mjs` [HUB-1] · `src/` M `a11y.test.tsx` · `src/components/` M `RecoveryCard.tsx` `RecoveryCard.test.tsx`, A `DevPanel.test.tsx` · `src/lib/` M `format.ts` `format.test.ts` `i18n.ts` `i18n.test.ts` `recovery.ts` `recovery.test.ts` `verdicts.ts` · `src/lib/api/` M `contract.ts` `contract.test.ts` `shapes.ts` `v113-additive.test.ts` `v114-additive.test.ts` `v115-additive.test.ts` `v116-additive.test.ts`, A `v117-additive.test.ts` · `src/lib/api/fixtures/` A `emitter-2026-10-11-entities-v117-row.ts` · `src/lib/api/mock/` M `mockTransport.ts` `scenarios.ts` · `src/views/` M `DevicesView.tsx`.

**Red-first** (new/changed tests on HEAD's code: 72 red / 445):
| Row | RED at HEAD — how | GREEN |
|---|---|---|
| 1 bump | 20: wrong-type ×12 + by-name (keys ignored) · `RECOVERY_KEYS` undefined · pin ×6 | ✓ |
| 2 gate | 1: `stageOf` reads no meta | ✓ |
| 3 cells | 25: S3 cells ×18 (todo → test) · card ×2 · catalog ×4 · `elapsedExceeds` | ✓ |
| 4 sentence | 6: `contractSentence` ×4 · `wholeMinutes` · kind | ✓ |
| 5 L2 | 5: L2 ×4 · `recordIntervalWord` | ✓ |
| 6 honesty | 5: R6 instant · bound inputs · R8 scan · `messageKeys` ×2 | ✓ |
| 7 mock | 10: v117 ×5 · recovery ×2 · DevPanel · a11y ×2 | ✓ |

**Predictions.** P1 HOLDS (re-read after this file). P2 SPLIT: the absent/null/value arms are green at HEAD by construction; the wrong-type rows are the red; S3 cells red but the two "as at S2" cells (§2). P3 HOLDS: 7 md5s unchanged; `recoveryRow` HEAD ≡ new on 2,124 inputs. P4 HOLDS on the O3 copy; `frontend.yml` PENDING the push. P5 HOLDS (§2). P6 HOLDS: 4 cites (O-9).

**Gates.** `npm run verify` GREEN 00:29:41Z→00:30:04Z: tokens · lint 0 · tsc 0 · 34 files / 780 tests · build · bundle 79.6 / 100 KB · contract ✓ `v1.1.7-2026-10-11`. Desk: `cd web-ui/dashboard && npm ci && npm run verify`.

**Deviations.** [HUB-1] `contract-check.mjs:26` only. [D-1] `.git` holds a Windows gitdir: git ran as `--git-dir=…/.git/worktrees/homesynapse-core-hero-u3 --work-tree=… --no-optional-locks`. [D-2] `npm ci` once, on a `/tmp` copy of the lockfile. [D-3] `DevicesView.tsx` passes the list's meta to both cards. [D-4] outside §3's names, in `src/`: `format.ts`, `verdicts.ts`, `i18n.ts`, tests. [D-5] the toggle = two scenario chips.

## §1 Per-file deltas (paths under `src/` unless named; numstat)
- `lib/api/contract.ts` +70/−4: the pin + the v1.1.7 block; `RecoveryCardKeys` (eleven optional-nullable keys, wire order, a one-line ADDITIVE comment each), `RECOVERY_KEYS` (`satisfies`), `RecoveryKey`; A1/A2/A3 `extends RecoveryCardKeys`; `ResponseMeta.recoveryViewPosition?` after `timestamp`. `scripts/contract-check.mjs` +1/−1 [HUB-1].
- `lib/api/shapes.ts` +41: `intOrNull` · `countOrNull` · `recoveryKeys()` on A1 rows and A2/A3 data, by name; `meta()` types a present `recoveryViewPosition` (int ≥ 0 | null).
- `lib/recovery.ts` +240/−75: `S3`; `stageOf(row, meta?)`; `contractSentence(row, stage, kind = 'device')`. AVAILABLE: R6 first (the served `recordOverdueSince`; L2 `dueBy`) · R4 passive (Quiet only past a declared interval) · R2 `recorded` (an answer after the report; the noTime arm) · S2's edge as R2's null arm · R1 with the class sentence. UNAVAILABLE: R5 (S2's arm) · `leave` · passive dark · R3 (`missesToDark` ≠ 2 → the bare label, the class sentence as its line). L2 adds `lastRecordedCheck` · `checkWindow` · `recordEvery`. S1/S2 paths unchanged.
- `lib/format.ts` +25: `RECOVERY_KIND_FALLBACK` · `wholeMinutes` · `recordIntervalWord` · `elapsedExceeds` — the only seconds arithmetic. `lib/verdicts.ts` +5/−3: the hourglass (states.html's path). `lib/i18n.ts` +22/−9: §7 as amended by U2c (−5, +9, floor re-cut; 67 rows, by script) + `messageKeys()`.
- `components/RecoveryCard.tsx` +12/−4: `meta?` → `stageOf(row, meta)`. `views/DevicesView.tsx` +6/−4 [D-3].
- `lib/api/mock/scenarios.ts` +103: `MockDataset.recoveryViewPosition?`; `recovery-live`, 9 rows (metered R2 with a full record · metered R1 · floor, no answer · passive · R6 · R3 beside a served past bound · R5 · LIVE with nothing recorded · UNKNOWN, no device) with A3 records; `recovery-catching-up`, the same fleet all null, position null. `mockTransport.ts` +18/−4: the entity reads' meta; A2's eleven keys.
- Tests: `v117-additive.test.ts` (A, 42) · the fixture (A) · `DevPanel.test.tsx` (A, 1) · `recovery.test.ts` (6 todo → 38) · `RecoveryCard.test.tsx` (+4) · `i18n.test.ts` (+5; the lock re-extracted) · `format.test.ts` (+4) · `a11y.test.tsx` (+2) · the pin, one line in 5 files. The scenario loop now validates both new scenarios (`contract.test.ts` 52 → 54).

S3 strings, word for word (SPEC §7, by script):
- `contract.metered` This {kind} reports at least every {reportMinutes} minutes. After {askMinutes} minutes of silence it is asked.
- `contract.floor` This {kind} has no report schedule on record. After one minute of silence it is asked.
- `contract.passive` This {kind} reports when something changes. It is never asked.
- `contract.fallback` If this device goes quiet for a while, it is asked. How long is not shown here yet.
- `state.quiet.line.recorded` No report since {time}. It answered the newest check on record, at {checkedTime}.
- `state.quiet.noTime.label` Quiet (asked, answered)
- `state.quiet.line.recorded.noReport` No report on record. It answered the newest check on record, at {checkedTime}.
- `state.passive.quiet.label` Quiet since {time}
- `state.passive.quiet.line` No report since {time}. This device is never asked.
- `state.noCheckRecorded.label` No check recorded since {time}
- `state.noCheckRecorded.line` A newer check was due by now. What the device is doing is not known.
- `l2.lastRecordedCheck` Newest check on record: {absoluteTime} — answered
- `l2.checkWindow` Checks in that record: {windowStart} to {checkedTime} — {answered} answered, {missed} missed
- `l2.recordEvery` Recording: one answered check per {recordInterval} at most, plus one after each restart
- `l2.dueBy` Newer check due by: {absoluteTime}

## §2 The gates
- Baseline at `2a54145` (the O3 copy = `git archive 2a54145 web-ui/dashboard`, 128 files ≡ the worktree): `npm run verify` GREEN, 682 + 6 todo, bundle 77.2 KB.
- RED: HEAD's code (cmp-equal) + the 12 new/changed test files + the fixture → 72 / 445 (§0). Green by construction, disclosed: v117's 22 preservation rows; 6 recovery rows (not-LIVE ×3; `leave`, the open vocabulary — "as at S2"; never-infers-R6); 2 card byte-identity rows. Teeth by mutation (scratch copy): null position ignored → 5 red · the gate's key half dropped → 2 · "we" → 4 · `(x ?? 0) * 1000` → 1 · R6 inferred → 1 · R6 time from the record → 1 · `/ 1` → 1 · control 0.
- GREEN (§0); the gated copy ≡ the worktree after the run (110 files, md5), `tokens.css` identical.
- P3: HEAD's `recoveryRow` vs the new one — 177 rows (every scenario row, the real wire rows, the emitter legs) × 4 instants × 3 metas (none · v1.1.6 · not-LIVE) = 2,124 identical. P5: the golden strings, keys and values extracted by script from `EntityStateJsonV117Test.java` (md5 bb3ff1f5…); v117 pins the stripped row and record to GOLDEN_V116_LIST / _RECORD; the R6 leg's meta is composed, said in the file.
- R4 grep: 0. R8: `recovery.ts` names the three inputs on 4 code lines (:135 :142 :180 :380) — call arguments and comparisons; the other hits are comments.

## §3 Pushback and observations
- O-1 The charter's write-set missed the pin's seventh home (`contract-check.mjs:26`; the skill's §5.1 "both places"); raised mid-lane, widened by the hub at 19:02 CT.
- O-2 `{kind}`: no entity read carries a device class word, so the card says "device" (§7's generic value); SPEC §4's "plug" / "sensor" hold word for word in tests by argument. Hub: a class word on the read, or §4 re-cut.
- O-3 "Newest check on record: Not recorded." (SPEC §3 R1/R3/R5 S3; states.html) has no §7 key — composed from `recovery.l2.lastRecordedCheck`'s lead + `recovery.l2.notRecorded`. Hub: key it.
- O-4 §4's ≤ 60-s seconds form has no §7 row: under two whole minutes → the fallback.
- O-5 `recovery.contract.answersNoReports` ("the Hue exhibit … a months-old {t}") has no wire-decidable rule: unconsumed. Hub: a rule, or retire.
- O-6 passive ∧ UNAVAILABLE ∧ reason null ∧ lastSeenAt null is claimed by R4 S3 and R5 S3; built as R5, whose "It has not been asked yet" promises an ask a passive device never gets. Hub: rule.
- O-7 An answer ≤ lastReported (R1 S3) beside S2's ping_success edge: the edge form kept (true, on the wire). Hub may rule.
- O-8 FIELDS.md §3 at 2a54145 still lists `probeLink` PROPOSED and has no `recordDueBy` / `recordOverdueSince` rows. The A2/A3 types never mirrored v1.1.6's triple, so "after `link`" is literal on A1 only. `EntityStateJsonV117Test.java:45` says "after viewPosition"; its assertion (:301–:302) pins after `timestamp`.
- O-9 (P6) `appendRecoveryKeys :124–:153` → :124–:155 · "`:158–:164`" → the helper is :157–:167; the placement is GetEntityEndpoint.java:155–:158 · GetEntityStateEndpoint.java:148–:151 · ListEntitiesEndpoint.java:209–:212 · `recovery.test.ts:298–:323` → the todo block is :298–:306 · `contract.ts :265–:310` → :258–:313.
- O-10 WhyNotView's card reads the registry census (no meta): S2 forms there. `recovery-states` serves no A3, so its drawer errors before the card (pre-existing). Bundle +2.4 KB; 20.4 KB headroom.

## §4 WUCP Phase-1
- [x] §0's checks stood for the preflight (charter §1: nothing older); volatile facts re-derived at `2a54145`.
- [x] The contract consumed field for field; mocks present-but-null; no invented shape (no `probeLink`).
- [x] States honest and distinct; no token changed; axe on every S3 state; R5 / R6 apart with the colour covered; copy test-locked (67).
- [x] Under budget; gate green (O3), `frontend.yml` on the push; nothing phones home; `{{NAME}}` / "we" 0.
- Register: REPO-COMPLETE, LIVE-VERIFICATION PENDING — the first v1.1.7 wire is BC10 (Sat Oct 17).
- Next WU: HERO-U3-W at BC10's intake — one real v1.1.7 `/api/v1/entities` capture filed `wire-2026-10-17-…`, v117 re-pinned to it (H8 → VERIFIED); then O-2..O-5's §7 rows and the why-not surface's meta (O-10).

RETURNED nexsys-hivemind/context/audits/2026-10-11_HERO-U3_return.md 11508
