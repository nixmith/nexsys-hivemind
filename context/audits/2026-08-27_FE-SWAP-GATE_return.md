<!--
file: context/audits/2026-08-27_FE-SWAP-GATE_return.md
purpose: FE-SWAP-GATE return — the brand-token pin + the false-green fix, per `context/instructions/2026-08-22_FE-lane_SWAP-GATE_brand-token-pin_micro-WU.md` (v56 beat 2, dispatched on R-FE-GATE). Two files landed in the host checkout, uncommitted; `npm run verify` GREEN and the red arm proven (exactly ONE failure) in the lane's reconstructed workspace; the flip-WU count corrected.
audience: the hub (intake) + Nick (commit; `frontend.yml` on the push = the gate of record).
lane: FE (`/nexsys-frontend`). Nothing committed; no branch, no stash.
baseline: homesynapse-core HEAD `dec35be` (two commits past the census's `89a912e`; `git diff --stat 89a912e -- web-ui/dashboard/` EMPTY — the FE corpus is unchanged since the census). Porcelain EMPTY at open.
fences honored: no candidate name anywhere (the pin asserts the WORKING name — that is its point); `i18n.ts`, `index.html`, `README.md`, `tokens.css` untouched on the host (`git diff --quiet` on all four: clean); the D-1 DO-NOT-SAY sentences untouched (not in the FE corpus — census §1b).
filed: 2026-08-27.
-->

# FE-SWAP-GATE — the brand-token pin + the false-green fix (2 files; return)

**Preflight: PASS.** Check 6 — `i18n.ts:18` still reads the working name (R-1 unreleased in code; the snapshot's Next line names this paste for today). Check 7 — the skill mirror is byte-identical (SKILL.md + 5 refs, sha-matched). Check 8 — `:153`'s literal and `format.test.ts:22/:46`'s token-relative form re-verified at source before editing.

## §1 Census (exactly 2 = 1 A + 1 M) — the host porcelain at close

```
 M web-ui/dashboard/src/views/EventsView.unserved404.test.tsx      (4 ++--: 2 insertions, 2 deletions)
?? web-ui/dashboard/src/lib/i18n.test.ts                            (16 lines)
```

| File | Kind | What landed |
|---|---|---|
| `src/lib/i18n.test.ts` | **A** | House idiom (`vitest` `describe/it/expect`, `import { BRAND } from './i18n'`): `expect(BRAND.productName).toBe('HomeSynapse')` under the one-line comment *"The rename gate: this row goes RED at the swap and is updated in the same commit as i18n.ts:18 — W-11."* **The two render rows are OUT, as the instruction ruled:** `git grep -l "AppShell\|AuthGate" -- "web-ui/dashboard/src/**/*.test.tsx"` returns NOTHING — neither component has a render test today, so the file carries the pin only. (Disclosed for the hub: a general harness DOES exist — `@testing-library/preact` + jsdom, used by `EventsView.unserved404` / `WhyNotView.nullability` / `HealthView.wire-hardening` / `poll.survival` — so the two REACH rows are authorable as a follow-up if wanted; not needed for the gate, since census §3 proves the reach by inspection and the flip's `npm run verify` re-proves it at build.) |
| `src/views/EventsView.unserved404.test.tsx` | **M** | `:34` `import { t } from '../lib/i18n';` → `import { BRAND, t } from '../lib/i18n';` (the file's own relative-import style) · `:153` `.not.toContain('HomeSynapse')` → `.not.toContain(BRAND.productName)`. Meaning unchanged (the minted `endpoint-not-in-this-release` copy is name-light); it now survives the rename. Zero literal hits remain in the file. |

## §2 Where the gate ran — the reconstructed workspace (disclosed, not rounded up)

The host `node_modules` is Windows-built (no `@esbuild/*` Linux binary), so the lane's Linux VM cannot run vitest from it, and `npm ci` inside the checkout would have replaced Nick's Windows binaries — **not done.** Instead: the 96-file working tree (95 tracked + the new test; no `node_modules`, no `dist`) tarred to a scratch file (sha `1b6d6b6c…`, removed after staging), rebuilt in the lane sandbox with `npm ci` from the committed lockfile, Node 22.22.2 (CI pins Node 20 — the lockfile-exact install and the gate's steps are the same; **`frontend.yml` on the push remains the gate of record**, and Nick's host `npm run verify` is the host-side confirmation). The three WU-relevant files are hash-identical host ↔ sandbox: `i18n.ts` `fdc37154…` · `i18n.test.ts` `4fe755fb…` · `EventsView.unserved404.test.tsx` `a8e32d82…`.

## §3 `npm run verify` — GREEN (tail)

```
tokens:check — OK (tokens.css matches the token source).
> eslint .                       (clean — no output)
> tsc --noEmit                   (clean — no output)
 Test Files  15 passed (15)
      Tests  211 passed (211)          ← 210 → 211 (the pin-only prediction, exact)
✓ 60 modules transformed.  dist/assets/index-BHlSe5gc.js  104.05 kB │ gzip: 32.90 kB
✓ Within budget (63.2 KB / 100 KB, 36.8 KB headroom).
✓ Contract coverage complete: 11 endpoints, version v1.1.2-2026-07-26.
```

## §4 The red arm — exactly ONE failure (paste)

`i18n.ts:18` → `productName: 'ZZ-PLACEHOLDER',` (sandbox copy only); `npm test`:

```
 ❯ src/lib/i18n.test.ts (1 test | 1 failed) 8ms
     × pins the working product name 6ms

⎯⎯⎯⎯⎯⎯⎯ Failed Tests 1 ⎯⎯⎯⎯⎯⎯⎯

 FAIL  src/lib/i18n.test.ts > brand token > pins the working product name
AssertionError: expected 'ZZ-PLACEHOLDER' to be 'HomeSynapse' // Object.is equality

Expected: "HomeSynapse"
Received: "ZZ-PLACEHOLDER"

 ❯ src/lib/i18n.test.ts:14:31
     14|     expect(BRAND.productName).toBe('HomeSynapse');

 Test Files  1 failed | 14 passed (15)
      Tests  1 failed | 210 passed (211)
```

**Every other test green under the placeholder** — the 14 REACHED sites and the re-keyed `:153` follow the token, as predicted. **No second failure: no hidden literal the census missed.**

## §5 The restore + the porcelain after

Sandbox `i18n.ts` restored from its pre-mutation copy → sha `fdc37154…` (= the host file, byte-identical); `npm test` → **211/211** again. **The host `i18n.ts` was never modified** (the red arm ran on the sandbox copy), so no `git checkout --` was needed on the host; `git diff --quiet -- i18n.ts index.html README.md tokens.css` on the host: clean. Host porcelain at close = §1 exactly: the two files of this WU, nothing else. (Housekeeping, disclosed: my first `git status` from the VM left a zero-byte `.git/index.lock` the VM could not unlink; removed with Nick's delete grant the same minute; every later git read ran with `GIT_OPTIONAL_LOCKS=0`. No lock remains.)

## §6 The updated flip-WU count (the H+2–6 line)

The pin joins the census §2 IN table as **row 8 — `src/lib/i18n.test.ts:14` `toBe('HomeSynapse')` — "the gate"**: **K = 7 → 8 IN lines / 3 → 4 files.** The hub's "5" (beat-2 audit line 43) is right **as FE-territory IN LINES**: `i18n.ts:18`, `i18n.ts:5`, `index.html:9`, `index.html:30` + the pin's `:14` = **5 lines the flip edits under `web-ui/dashboard/`** (+ the 3 README lines in the hub's separate patch = 8). **As FILES it is 3, not 5:** with this WU landed, the flip WU stages exactly **3 M** — `i18n.ts` · `index.html` · `i18n.test.ts` (A → M: the pin's own update) — because the census's row 3 (the re-keyed `:153`) is DONE and never touches again. The runbook's H+2–6 line should read *"stages exactly 3 (3 M) in FE territory; 5 IN lines; README rows in the hub's own patch per ruling (ii)."* The flip's predicted test count stays **211 → 211** (the pin flips, it does not multiply).

## §7 Pushback (one batch)

1. **Instruction arithmetic (non-blocking):** "the flip WU's count becomes 5 (4 + the pin's own update)" double-counts once this WU lands — see §6. Lines 5 / files 3; the hub picks the unit and fixes the runbook line.
2. **The red arm ran in the reconstructed workspace, not on the host checkout** (§2 reason). The proof transfers byte-for-byte (hash-matched inputs, lockfile-exact deps); if the hub wants the host-side arm on record too, it is Nick's optional §5-style 2-minute block: flip `:18`, `npm test`, expect the one failure, `git checkout -- web-ui/dashboard/src/lib/i18n.ts`.
3. **The REACH render rows** (AppShell `:36`, AuthGate `:23`) are OUT per the instruction's own rule; a harness exists (§1). Recommendation: leave them out of the flip too — the census reach map + the build are the proof; a render pin on the wordmark slots would be the first thing a B-1 lockup change breaks for no gain.

**Done-when:** Nick commits the two files (suggested subject: `web-ui: FE-SWAP-GATE — the brand-token pin (i18n.test.ts, A) + the :153 negative assertion re-keyed to BRAND.productName (M); 2 files; red arm proven (1 failure exactly); 210 → 211`) and `frontend.yml` reports GREEN on the push. **Next recommended WU:** *FE-SWAP-FLIP* — 3 M in FE territory, held INERT until the R-1 word; red-first by construction now.
