<!--
file: context/audits/2026-09-10_FE-NULL-1_intake_two-layer-audit_v68-b5.md
purpose: The hub's two-layer intake audit of the FE-NULL-1 return (the causal chain's four null arms + the F4 cascade row in the dashboard mirror; no wire change, no version bump) — the claims read critically, then the hub's own re-executions at the bytes; S3 (the headline delta) ACCEPTED; O1 (the L1 headline ignores outcome) DOCKETED to the hero charter; the landing card handed. Also banks what landed around it: HONESTY-1 `94ae99d` (ci GREEN), the Dependabot vitest bump `3f3f5cc`, the stranded index.lock.
audience: the hub · Nick (§3 the rulings; the card is in the brief §NEXT)
state-type: intake audit (FILED)
status: FILED v68 beat 5 (Thu 2026-09-10 ~19:2x CT; instrument 2026-09-11T00:19Z). Return: context/audits/2026-09-10_FE-NULL-1_return.md (11,218 B; RETURNED line in the file and printed). Verdict: ACCEPT — the landing is Nick's `git add -A web-ui/dashboard` card on `3f3f5cc`; `frontend.yml` on the push = the gate of record.
-->

# FE-NULL-1 — intake audit (two layers)

## §0 Verdict: ACCEPT
P1–P4 MET as declared: the census is exactly the eight §3 files under `web-ui/dashboard/`; the three fixtures are byte-identical; `npm run verify` ran on the Windows desk (the lane got a click-only File Explorer grant and ran a `.bat` from `_scratch/` — the log is `_scratch/fe-null-1_verify.log`): 20 files / 307 tests, 0 failed, `VERIFY_EXIT 0`; P4 found three stale reads of the instruction (S1–S3) and filed them with line cites. One declared delta beyond the letter of row 5 (S3) and one pre-existing `[REVIEW]` the null arms exposed (O1), both ruled §3.

## §1 Layer 1 — the claims, read critically
The return's §0 leads with the predictions, the census, the red-first table and the verify line with counts; §3 puts mismatches first, which is the shape we ask for. S1 corrects the instruction's own overstatement (MISSING/wrong-type already threw at HEAD; only the PRESENT-null rows were red) — the honest labelling. S2 corrects the mock line cites (the chains span `:232–:374`). S3 is the lane exceeding the table on the honesty law's own logic: the headline `causalSentence` at HEAD rendered a null subject/target as "Something not on record", a label that reads like a registry accusation; the lane applied the HERO-0 fragments there and declared it `[DELTA-headline]` with a two-hunk revert offered. O1 is a real finding about the hero's L1 sentence, not about this WU. O3 is a desk fact worth keeping (the Linux-side lane cannot run the Windows tree's toolchain without two optional platform packages).

## §2 Layer 2 — the hub's re-executions at the bytes (2026-09-11T00:19Z)
1. **Census at porcelain — VERIFIED:** `git --no-optional-locks status --porcelain` in core = exactly 8 ` M`, all under `web-ui/dashboard/` (`MODULE_CONTEXT.md` · `CausalChain.hardening.test.tsx` · `CausalChain.tsx` · `contract.ts` · `mockData.ts` · `shapes.ts` · `v113-additive.test.ts` · `format.ts`); 0 outside; `??` 0; the diff stat 8 files, +446/−28.
2. **The return file — VERIFIED:** 11,218 B at the named path; last line `RETURNED nexsys-hivemind/context/audits/2026-09-10_FE-NULL-1_return.md 11218`.
3. **The types — VERIFIED at `contract.ts`:** `:322 subjectRef: SubjectRef | null` · `:333 value: string | null` · `:340 targetRef: SubjectRef | null` · `:343 command: string | null`; `CONTRACT_VERSION` unchanged at `v1.1.3-2026-09-06` (:14).
4. **The validators — VERIFIED at `shapes.ts`:** `:259 refOrNull(req(trigger,'subjectRef'…))` · `:278 strOrNull(req(o,'value'…))` (the observedState entries are now validated) · `:290 strOrNull(req(a,'command'…))` · `:291 refOrNull(req(a,'targetRef'…))` (validated for the first time).
5. **The mock's null arms — VERIFIED at `mockData.ts`:** `subjectRef: null` (:326) · `targetRef: null` (:341) · `command: null` (:342) · `value: null` (:370) · `cascade: { parentRunId: null, depth: 1 }` (:387); the header comment cites the emitter lines.
6. **The sentences — VERIFIED at `format.ts`:** `"Something set it off at ${when} — what isn't recorded."` (:37) · `NO_READING_YET` (:40) · `SKIPPED_BEFORE_COMMAND` (:45) · `UNNAMED_TARGET` (:47) · `CASCADE_PARENT_UNRECORDED` (:49) — the HERO-0 wording, exported, not inlined.
7. **The fixtures — VERIFIED:** md5 `896f861d…` · `6f502c7b…` · `05b02fbc…` unchanged (P2).
8. **The tree beneath the work — VERIFIED:** core HEAD is now `3f3f5cc` (the Dependabot merge `#6`: vitest → `^4.1.11` + the lock file, on top of `94ae99d`); the lane's 8 files fast-forwarded cleanly (the bump touched only `package.json`/`package-lock.json`). The lane's verify ran on the pre-bump vitest; **`frontend.yml` on the push re-runs it on the bumped one — that is the gate, as always.**
**NOT re-executed (disclosed):** `npm run verify` (the VM has no toolchain; the log and the return's counts are the claim; CI is the gate); the RED-at-HEAD claims (read at the test file's labels, not re-run).

## §3 Rulings
- **S3 `[DELTA-headline]` — ACCEPTED.** The honesty law reaches every sentence the wire's nulls touch, the headline included; "Something not on record" was an accusation dressed as a label. The lane declared it and offered the revert — the discipline we want.
- **O1 `[REVIEW]` — DOCKETED to the hero charter as its first row, not fixed here:** the L1 headline ignores `action.outcome`/run status (`format.ts:484` `commandVerb('turn_on')` regardless of SKIPPED; `format.test.ts:39` pins only the happy path). A per-outcome L1 sentence is the hero's design decision (`DESIGN: start` is lawful now); an interim one-line arm would pin a sentence the charter is about to own. The null arms land now because they are strictly more honest than HEAD, and the SKIPPED headline now says "a device the run didn't name acted" — wrong verb, no accusation — until the hero charter replaces it.
- **O2 (apostrophes) — the hero charter's normalisation; no act.** **O3 (the toolchain gap) — RECORDED for the next FE instruction and W-SKILLS-9:** one Windows-side `npm i --no-save @rollup/rollup-linux-x64-gnu @esbuild/linux-x64` makes the desk gate runnable from the VM without a grant.
- **The hub's own miss, owned:** the FE-NULL-1 instruction spelled `git status --porcelain -- web-ui/dashboard` WITHOUT `--no-optional-locks` — the ledger's lock-free-porcelain law; the stranded `index.lock` that blocked Nick's HONESTY-1 commit at 18:5x CT is the likely fruit (a Cowork sandbox `git status` can strand one — the coder CLAUDE.md says so). `rm .git/index.lock` was the right move. Every future lane line spells the flag.
- **Banked beside this WU:** HONESTY-1 LANDED `94ae99d` (`39c8dd3..94ae99d`), `ci` GREEN — OR-HONESTY-1-GATE half-closed; **P4 (install-smoke started by itself on the push) is still Nick's one line.** The Dependabot pair (#15/#16, `@vitest/mocker` redirect-mock path traversal, moderate, dev-only — the dev server binds localhost; no production surface) MERGED as `3f3f5cc`, CI green, pulled — no act; the 12 earlier alerts were already closed.

## §4 The landing (Nick's hands; the card is the brief's §NEXT)
`git add -A web-ui/dashboard` on `3f3f5cc` (expects 8), the msg file `_scratch/2026-09-10_core_FE-NULL-1_commit-msg.txt` (no trailers), push; `frontend.yml` green = the gate of record; `ci` runs too. The report-back is one line: `FE-NULL-1: <sha> · frontend <green | red: line>`, plus the owed `install-smoke: ran green | ran red: line | did not run` for `94ae99d`. The hivemind side (the return + this audit) is hub-run in this beat's commit. `_scratch/fe-null-1_*` (four tarballs, a `.bat`, a log) are the lane's scratch — deletable at Nick's convenience.

## §5 Definition of done (this WU)
- [x] The return exists at the named path; audited two-layer; this audit filed.
- [x] The landing card handed (8 paths under one domain); the `frontend.yml` wait-state recorded in §HELD.
- [x] MODULE_CONTEXT updated by the lane (`web-ui/dashboard/MODULE_CONTEXT.md` in the 8); the handoff entry is the hub's at landing (§HELD carries it; the lane was fenced from `coder-handoff.md`).
- [x] O1 docketed as the hero charter's first row; O3 recorded for W-SKILLS-9.
- [ ] `frontend.yml` green on the push (Nick's line) → FE-113b + the hero charter are next in the web-ui domain.
