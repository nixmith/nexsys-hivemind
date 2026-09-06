<!--
file: context/audits/2026-09-06_FE-113_intake_two-layer-audit_v66-b5.md
purpose: The hub's two-layer audit of the FE-113 return (the v1.1.3 mirror in web-ui/dashboard/) under the instruction's pre-filed §8 rules R1–R7 and §0 predictions P1–P4; the rulings on its two [REVIEW]s; the core msg file + census card for Nick's landing (the ONE core-tree lane; frontend.yml = the gate of record); the registers it moves.
audience: the hub · Nick (the landing card, §5) · the FE-113b lane (what H8-a captures for it)
state-type: intake audit
status: FILED v66 beat 5 (Sun 2026-09-06 ~11:2x CT; instrument 2026-09-06T16:1xZ). Return: context/audits/2026-09-06_FE-113_return.md (12,223 B; RETURNED 16:12Z). Verdict: ACCEPT-WITH-TWO-RULINGS (R1 ACCEPT · R2 ACCEPT). Register: REPO-COMPLETE, LIVE-VERIFICATION PENDING → VERIFIED when H8-a's B2 reads the four keys (law #22).
-->

# FE-113 intake — two-layer audit (v66 beat 5)

## §0 Verdict card
**ACCEPT-WITH-TWO-RULINGS.** The return declares 16 = 14 M + 2 A, all under `web-ui/dashboard/`; the hub's lock-free porcelain on Nick's tree reads EXACTLY 14 ` M` + 2 `??` there and nothing outside it. The version pin is `v1.1.3-2026-09-06` at `contract.ts:14`; the four fixture files are md5-identical to HEAD; the lowercase `entity` literal is pinned and never case-normalized; the mock carries nulls on every new key and one dangling ref; the three-way render tests exist for each view (8 · 14 · 6) plus the 25-case additive suite. **The two `[REVIEW]`s are both the hub's authoring misses and both ACCEPT:** R1 — `scripts/contract-check.mjs`'s `EXPECTED_VERSION` (the v65 b3 spine line "`EXPECTED_VERSION` does not exist in the tree" grepped `.ts` only; it lives in a `.mjs` and gates `verify` — a stale fence, owned); R2 — `AutomationsView.ref.test.tsx` as an A (the table's row 9 said "+ its test" when no such test existed at HEAD). **Predictions:** P1 MISSED (11 M + 1 A → 14 M + 2 A: the three named test files are M not extra, R1 +1 M, R2 +1 A) — owned by the hub; P2 MET; P3 MET (`npm run verify` green in one round, 274/274, bundle 64.9/100 KB); P4 MET (five stale reads filed with cites). **Disclosed non-re-executions:** `npm run verify` (the desk VM cannot run the toolchain — I4; the lane ran it in its container on `git archive HEAD`; CI on Nick's push is the gate); the six Playwright screenshots (the lane's description read, not re-rendered). **The landing:** Nick's commit of exactly the 16 + push → `frontend.yml` GREEN = the gate → **passive sample 4/20** rides free (`ci.yml` has no path filter). **Then F-R4-1b dispatches** (its instruction is on disk; the sha slot fills from his push).

## §1 Layer 1 — the return's claims, read critically
The §0 card is ≤3 KB and carries the census with exact paths, the red-first table (22 RED / 252 / 274 at HEAD + 20 tsc type-errors → 274/274, tsc 0), the deviations by tag, the `verify` line with counts and the contract-check stamp. The red-first sort is honest: green-by-construction rows named per file (the absent/null arms that must not change the surface). The lane refused to write `coder-handoff.md` (its §0 fence) and drafted the entry instead — correct reading; the hub folds it (§4). O1 (the default mock's `resultOutcome: 'acknowledged'` beside CONFIRMED actions, contradicting CG §DP-5's live null) is a real H8 false-VALUE candidate the lane did not fix because it sits outside the table — correct restraint; a docket row (FE-MOCK-1) opens below. The return is 12,223 B against a ≤12 KB cap (12,288) — under by 65 B: the b5 mint holds (capped lanes write to the cap).

## §2 Layer 2 — at the bytes (each rule re-executed)
| Rule | Re-executed | Result |
|---|---|---|
| R1 census at porcelain | `git status --porcelain web-ui/dashboard \| awk '{print $1}' \| sort \| uniq -c` | **14 M · 2 ??** — exact; nothing outside `web-ui/dashboard/` |
| R2 the version pin + the RED-at-HEAD claims | `contract.ts:14` = `'v1.1.3-2026-09-06'`; `contract-check.mjs:15` = the same (the return's `:13` cite is off by two — `[INFO]`); HEAD's `contract.ts` carries 1 hit for `deviceId\|lastReported\|triggerRef` (a comment) vs 7 now — the tsc-red claim holds by construction; `LIST_FRESHNESS_NULL_TITLE` absent from HEAD's `i18n.ts` (0) and asserted 4× in `format.test.ts` — T3's red holds | MET |
| R3 the fixtures' md5 | four files under `src/lib/api/fixtures/` md5-identical to HEAD (`896f861d` · `05b02fbc` · `6f502c7b` · `8acb204f`) | MET |
| R4 the mock | `mockData.ts:46/:48` `deviceId: null`; `:48` `lastReported: null`; `:161/:172` `ref: null`; `DANGLING_LAMP_ULID` `:153` (one dangling ref by law) | MET |
| R5 the three-way render tests | `DevicesView.honesty.test.tsx` 8 · `WhyNotView.nullability.test.tsx` 14 · `AutomationsView.ref.test.tsx` 6 · `v113-additive.test.ts` 25 | MET |
| the literal | zero `toLowerCase`/`toUpperCase` in `shapes.ts`/`contract.ts`; `'entity'` pinned as the literal in the additive suite (`:84/:86/:121`) | MET |
| R6 `npm run verify` | NOT re-run by the hub (disclosed); the lane's run 3 at 16:04Z GREEN; the gate of record is `frontend.yml` | disclosed |
| the `contract-check.mjs` delta | `git diff`: 6 + / 4 − — the comment block re-cut for v1.1.3 + the one constant | lawful (R1 below) |

## §3 Rulings
- **R1 (`contract-check.mjs`, +1 M) — ACCEPT.** The constant exists at source and gates the very `verify` the instruction ordered green; the v1.1.2 precedent moved it. The hub's §5 fence rested on the v65 b3 grounding line "`EXPECTED_VERSION` does not exist in the tree", which grepped TypeScript only. Owned. **Mint (for the close): a fence that names a constant is grepped at source across every file type before dispatch** (the lane's own words).
- **R2 (`AutomationsView.ref.test.tsx`, +1 A) — ACCEPT.** Row 9's "+ its test" presumed a test that HEAD did not have; an A is the lawful reading of an M that cannot exist.
- **I1–I4 — noted, no act.** I1 `registry.ts` cites off by 2–3 · I2 the `contract.ts:140` "ENTITY" comment corrected as documentation (the freeze doc's B1 note, v66 b4, says the same) · I3 the handoff entry folded by the hub (§4) · I4 the desk-VM toolchain gap (disk 99% full → `npm ci` ENOSPC) — **FE-DESK-1 gains a line:** the desk needs free disk before `npm ci`; the lane's container pre-gate on `git archive HEAD` with md5 round-trips is a lawful fallback, recorded.
- **O1 → docket row FE-MOCK-1 (next mock touch):** the default mock's two CONFIRMED actions (`mockData.ts:260/:367`) and `scenarios.ts:75` carry `resultOutcome: 'acknowledged'`; the live happy path serves `null` (CG §DP-5; the freeze doc's Row 30 sentence, v66 b4). An H8 false-VALUE class; the `live-nulls` scenario carries the real arm. Fix at the next mock touch (or from H8-a's capture, which FE-113b turns into the fixture that makes the question moot for the recorded shapes).

## §4 WUCP fold (the hub's writes)
`coder-handoff.md` gains the lane's drafted entry verbatim (newest; the FE lane; supersedes nothing on the CORE lane — CG-123's entry stays lane-newest for Core). `coder-lessons.md`: the R1 lesson in one line. The dashboard `MODULE_CONTEXT.md` was updated by the lane (+5/−1: the v1.1.3 beat; the O1 gotcha) — read, accepted.

## §5 The landing — the msg file + the census card (Nick's hands; the ONE core lane lands)
**Msg file:** `../_scratch/2026-09-06_core_FE-113_commit-msg.txt` (no trailers — Nick's commit). **The act (one command; Git Bash; `~/Desktop/Code/ClaudeFolder/homesynapse-core`):**
```bash
cd ~/Desktop/Code/ClaudeFolder/homesynapse-core && git status --porcelain | wc -l && git add -A web-ui/dashboard && git diff --cached --name-status | wc -l && git -c user.name='Nick Smith' -c user.email='nickdsmith1@gmail.com' commit -q -F ../_scratch/2026-09-06_core_FE-113_commit-msg.txt && git log -1 --format='%h' && git push 2>&1 | tail -1
# EXPECTED: 16 · 16 · a new sha · "093d5b4..<sha>  main -> main". Then the Actions page: Frontend CI GREEN (the gate) and CI (Build & Check) GREEN (= passive sample 4/20, free). One line back: `FE-113: landed <sha> — frontend <green|red> · ci <green|red>`.
```
**STOP:** the first count ≠ 16 (something else moved on the tree) or the cached count ≠ 16 → paste, do not commit.

## §6 Registers this landing moves
FE-113 → LANDED on the push; → **VERIFIED** on H8-a's B2 (the four keys read on the wire, the `entity` literal, ISO-8601) — the record's K1–K4. FE-113b's inputs = the H8-a capture (`context/audits/2026-09-06_H8a_v113-wire-capture/`). F-R4-1b's dispatch line: the sha slot = this landing's sha. OR-BUS-SILENT-DROP: the passive count 4/20 on `ci.yml`'s run of this push (bank on Nick's line).
