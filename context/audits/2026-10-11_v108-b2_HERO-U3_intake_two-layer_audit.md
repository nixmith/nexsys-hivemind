<!--
file: context/audits/2026-10-11_v108-b2_HERO-U3_intake_two-layer_audit.md
purpose: The hub's two-layer intake of HERO-U3's return (the recovery card's S3 column on the v1.1.7 record; build mode; the worktree ../homesynapse-core-hero-u3 on hero-u3/recovery-card-live at 2a54145): the lane's claims read critically, the hub's own re-execution at the bytes against the charter's pre-filed rules R1–R8, the ten pushback items RULED, the disclosed non-re-executions, and the landing form (the commit in the worktree; main by --ff-only; frontend.yml the gate).
audience: the hub (the landing card; HERO-U3-W's charter at BC10) · Nick (the rulings, by id) · the v109 boot
state-type: intake audit (two-layer; LANDING-READY)
status: FILED v108 beat 2 (Sun 2026-10-11 ~19:5x CT; instrument 2026-10-12T00:50:19Z) — LANDING-READY; the card `_scratch/v108/b2/card_b2_hero-u3_landing.txt` handed; `CORE: LANDED <sha>` · `CI: green | red` pending
-->
# v108 b2 — HERO-U3 intake, two layers

## §0 The verdict
**LANDING-READY.** The return (`context/audits/2026-10-11_HERO-U3_return.md`, 11,508 B; the `RETURNED` line its last, its bytes the file's — R7) declares N = 24 = 21 M + 3 A under `web-ui/dashboard`; the hub's diff of the worktree against `main` at `2a54145` reads the same 24 and nothing outside (R1). The gate of record is `frontend.yml` on Nick's push; the lane ran `npm run verify` on a `/tmp` copy proven byte-identical to the worktree (780 tests; bundle 79.6 of 100 KB; the contract check on `v1.1.7-2026-10-11`) — a Layer-1 claim this VM cannot re-run (§4). Nick's words: `HERO-U3: running now` (19:04 CT) · `HERO-U3: RETURNED nexsys-hivemind/context/audits/2026-10-11_HERO-U3_return.md 11508` (19:39 CT).

## §1 Layer 1 — the claims, read critically
- The census names one file outside `src/`: `scripts/contract-check.mjs:26` — the pin's seventh home the charter missed and the hub widened at 19:02 CT (O-1; [HUB-1]). Consistent with the return's §0 and the diff.
- Red-first: 72 of 445 rows red on HEAD's code; P2 SPLIT and disclosed (the absent/null/value arms green at HEAD because HEAD's validator ignores unknown keys; only the wrong-type rows red) — the honest reading, in the form the house asks for (the green-by-construction carve-out named).
- P3: `recoveryRow` HEAD ≡ new on 2,124 inputs — a strong identity claim; the hub re-executed its premise (the S2 path untouched) only by the diff's shape (`recovery.ts` changed; the lane's equivalence script not re-run).
- [D-1] the worktree's `.git` is a file holding a Windows gitdir; the lane drove git with `--git-dir`/`--work-tree` — the same fact the hub recorded at D-v108-6 (b).
- [D-3] `DevicesView.tsx` passes the list's meta to both cards; [D-4] four files edited outside §3's names (`format.ts`, `verdicts.ts`, `i18n.ts`, tests) — small, named, inside `src/`; [D-5] the toggle as two scenario chips — accepted as the charter's "a toggle" in the DevPanel's own idiom.

## §2 Layer 2 — re-executed by the hub (from the mount; every command named)
- **R1 the census:** `diff -rq homesynapse-core-hero-u3/web-ui/dashboard homesynapse-core/web-ui/dashboard -x node_modules -x dist -x .vite` → `Files … differ` 21 · `Only in homesynapse-core-hero-u3` 3 (`src/components/DevPanel.test.tsx` · `src/lib/api/fixtures/emitter-2026-10-11-entities-v117-row.ts` · `src/lib/api/v117-additive.test.ts`) · `Only in homesynapse-core` 0; `diff -rq` of the two repositories excluding `web-ui`, `.git`, `build`, `.gradle`: only `main`'s untracked/ignored desk files (`.claude`, `.idea`, `CLAUDE.md` `!!`) — nothing tracked differs outside the dashboard. The 24 sorted names' md5 `e4ada7ff3f4b94eca84df212667816a5` (`_scratch/v108/b2/hero-u3_paths.txt`) is the card's set gate.
- **The version pin, both homes:** `scripts/contract-check.mjs:26` `EXPECTED_VERSION = 'v1.1.7-2026-10-11'` · `src/lib/api/contract.ts:14` `CONTRACT_VERSION = 'v1.1.7-2026-10-11'`; `RECOVERY_KEYS` declared at `contract.ts:305` ("the eleven keys in the wire's order — the mirror of EntityStateJson.RECOVERY_KEYS (:62–:65); read by name"); `recoveryViewPosition` read in 25 non-test lines under `src/`.
- **R2 (sampled):** `grep -c meta` in `recovery.ts` — HEAD 0, the worktree 5: `stageOf reads no meta` at HEAD is true at the bytes; the row's red stands.
- **R3:** `diff -rq` of `src/lib/api/fixtures/` → 0 differing; 8 files at HEAD, 9 in the worktree (the new emitter row) — the seven wire fixtures and `fixtures.stability.test.ts` unchanged.
- **R4:** `grep -rn '{{NAME}}\|"we \|We ' src/lib/recovery.ts src/lib/i18n.ts src/components/RecoveryCard.tsx` → 1 hit, `i18n.ts:344`, the doc comment that states the rule ("no product name, no `{{NAME}}`, no "we""); 0 in strings.
- **R8:** `grep -n 'silenceLimitSeconds\|missesToDark' src/lib/recovery.ts` → 7 hits; 0 inside an arithmetic expression (the lane's :135 :142 :180 :380 are call arguments and comparisons, as it says).
- **R7:** the last line `RETURNED nexsys-hivemind/context/audits/2026-10-11_HERO-U3_return.md 11508`; `wc -c` 11508.
- The worktree carries no `node_modules` (`ls -d node_modules` → none) — the desk needs `npm ci` there before a local `npm run verify`; CI needs nothing.

## §3 The pushback and observations, RULED (each by id; refutable by `REVERT O-n`)
- **O-1** the seventh pin home — the charter's miss, owned by the hub; widened at 19:02 CT. No act.
- **O-2** `{kind}`: no entity read carries a device class word; the card says "device" (SPEC §7's generic). **RULED: "device" stands.** A class word on the read is a Java row (post-run; IR-173); SPEC §4's "plug"/"sensor" are the examples' words, not a wire promise.
- **O-3** "Newest check on record: Not recorded." has no §7 key (composed from two). **RULED: key it** — one §7 row; rides HERO-U3-r1 (IR-174).
- **O-4** the ≤ 60-s seconds form has no §7 row; under two whole minutes the fallback. **RULED: the fallback stands** until a real capture shows a sub-minute record interval on the wire (none can: the probe cadence is minutes).
- **O-5** `recovery.contract.answersNoReports` has no wire-decidable rule; unconsumed. **RULED: retire the sentence** (an unconsumed string is a false promise in the catalog); rides HERO-U3-r1 (IR-174).
- **O-6** passive ∧ UNAVAILABLE ∧ reason null ∧ lastSeenAt null — claimed by R4 S3 and R5 S3; built as R5 ("It has not been asked yet"), which promises an ask a passive device never gets. **RULED: R4's form** — a passive device is never asked by design; the sentence must not promise it. Rides HERO-U3-r1 (IR-174); SPEC §3's two rows get the precedence sentence at the re-cut.
- **O-7** an answer ≤ lastReported beside S2's ping_success edge: the edge form kept (true on the wire). **RULED: accepted as built.**
- **O-8** `FIELDS.md` §3 at `2a54145` lists `probeLink` PROPOSED and has no `recordDueBy`/`recordOverdueSince` rows; the A2/A3 types never mirrored v1.1.6's triple; `EntityStateJsonV117Test.java:45` says "after viewPosition" while its assertion pins after `timestamp`. **RULED: a register row** (IR-172) — the core's FIELDS.md and the test's comment lag the emitter; a one-line doc fix on the Java side, not this lane's.
- **O-9** the charter's cites drifted by a few lines (`appendRecoveryKeys` :124–:155; the helper :157–:167; the placement sites; `recovery.test.ts` :298–:306; `contract.ts` :258–:313) — IR-161's class, after a re-point; INFO. The lane read the bytes, as the charter ordered.
- **O-10** WhyNotView's card reads the registry census (no meta) and shows S2 forms; `recovery-states` serves no A3 so its drawer errors before the card (pre-existing). **RULED: known** — HERO-U3-W's §7 rows (the why-not surface) at BC10's intake. Bundle +2.4 KB; 20.4 KB headroom — noted.

## §4 Disclosed — NOT re-executed
- `npm run verify` (vitest 780, lint, tsc, the bundle, the contract check): this VM has no `node_modules` in the worktree and a full disk; the lane's run on a byte-identical copy is Layer 1; `frontend.yml` on the push is the gate of record.
- R5 (the S3 sentences word for word against SPEC §3/§4/§7): sampled, not swept — `i18n.ts:373` ("Nothing from this device since startup. It has not been asked yet.") and `:421` ("Not recorded.") present; the sweep is HERO-U3-W's at the live pass, where the sentences meet a real payload.
- P3's 2,124-input equivalence script and the mutation runs — the lane's instruments on its scratch copy.
- The worktree's git state (branch, index) — unreadable from this mount (D-v108-6 (b)); the card asserts it on Nick's desk before it stages a byte.

## §5 The landing form
The commit IN THE WORKTREE on `hero-u3/recovery-card-live` (`git add -A -- web-ui/dashboard`; N = 24; the set md5 `e4ada7ff…`; the trailer grep; `git commit -F ../_scratch/v108/b2/2026-10-11_core_HERO-U3_commit-msg.txt`), then in `homesynapse-core`: `main` = `2a54145`, porcelain 0 → `git merge --ff-only hero-u3/recovery-card-live` → `git push` → `frontend.yml`. Say back `CORE: LANDED <sha>`, then `CI: green | red`. The worktree's removal is a later card. The web-ui domain is FREE after the landing; B-1's stub charter may name the slot.

## §6 What the hub files from this intake
- IR-172 — `FIELDS.md` §3 and `EntityStateJsonV117Test.java:45` lag the emitter (O-8).
- IR-173 — no device-class word on any entity read; the card's `{kind}` is "device" (O-2).
- IR-174 — HERO-U3-r1: the O-3 key, the O-5 retirement, the O-6 R4 form — one rider with HERO-U3-W at BC10's intake.
- The next FE unit of record: HERO-U3-W (the return's §4) — one real v1.1.7 `/api/v1/entities` capture at BC10 filed `wire-2026-10-17-…`, v117 re-pinned to it (H8 → VERIFIED); then O-2..O-5's §7 rows and the why-not surface.
