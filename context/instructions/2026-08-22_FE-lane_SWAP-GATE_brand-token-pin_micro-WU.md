<!--
file: context/instructions/2026-08-22_FE-lane_SWAP-GATE_brand-token-pin_micro-WU.md
purpose: FE-SWAP-GATE — a fence-clean FE micro-WU minted by the FE-SWAP-CENSUS return (`context/audits/2026-08-22_FE-SWAP-CENSUS_return.md` §4b, harvest 2–3): the G-2 swap runbook assumes "red-first — the brand-token test flips first", and the census found that test DOES NOT EXIST — the only token-touching assertion (`src/lib/format.test.ts:46`) imports `BRAND` and is flip-invariant, and `src/views/EventsView.unserved404.test.tsx:153` asserts `.not.toContain('HomeSynapse')` on a hardcoded literal that goes silently FALSE-GREEN after any rename. This WU lands the gate BEFORE H-hour so the flip is red-first by construction: (1) a positive token pin that is GREEN today and RED the moment the token flips; (2) the negative assertion re-keyed to the token so it keeps testing name-light copy under any name. Two files; zero user-visible change; the working name stays everywhere.
audience: an FE lane (`/nexsys-frontend`; host-side or fresh Cowork — no build in a sandbox; Nick runs `npm run verify` on his host; `frontend.yml` on the push is the gate of record) + Nick (commit; CI read) + the hub (audit).
status: ISSUE-READY (v56 beat 2). Baseline: core `89a912e` (the census commit; `web-ui/dashboard/` unchanged since). Dispatch on Nick's word R-FE-GATE (AUTHOR-NOW was ruled at beat 2; DISPATCH is his call — it costs one commit + one CI run; value = the Pelton-day flip becomes red-first and the false-green is closed before it can lie).
return: nexsys-hivemind/context/audits/<filing-date>_FE-SWAP-GATE_return.md (filing-day dated; ONE artifact). The lane commits NOTHING; Nick commits; `frontend.yml` GREEN on the push = done-when (plus the red-arm proof below).
dispatch: "Read nexsys-hivemind/context/instructions/2026-08-22_FE-lane_SWAP-GATE_brand-token-pin_micro-WU.md and execute it. - /nexsys-frontend"
fences: no candidate name anywhere (the pin asserts the WORKING name `'HomeSynapse'` — that is the point: it is the string the flip will change); nothing under `web-ui/dashboard/src/lib/i18n.ts` changes; no `index.html` change; no README change; the D-1 DO-NOT-SAY sentences untouched (they do not live in the FE corpus — census §1b); `tokens.css` never hand-edited.
-->

# FE-SWAP-GATE — the brand-token pin + the false-green fix (2 files)

## 0. Read first

The census return §2 (IN/REACHED tables), §4a (the Files table this WU takes rows 3–4 from), §4b (the two assertions, quoted), §4c (the gate predictions) · `web-ui/dashboard/src/lib/i18n.ts` whole · `src/lib/format.test.ts:1–:50` (the house test idiom: imports, `describe/it/expect`) · `src/views/EventsView.unserved404.test.tsx:140–:160` · `web-ui/dashboard/MODULE_CONTEXT.md` §FE-3 / D-FE-9 / W-11 (the single-source decision) · `.github/workflows/frontend.yml` (the path filter `web-ui/dashboard/**`).

## 1. Files (census-exact: **2 = 1 M + 1 A**)

| File | Kind | Delta |
|---|---|---|
| `web-ui/dashboard/src/lib/i18n.test.ts` | **A** | The positive pin, in the house idiom: `expect(BRAND.productName).toBe('HomeSynapse')` with a one-line comment stating its purpose (*the rename gate: this row goes RED at the swap and is updated in the same commit as `i18n.ts:18` — W-11*); plus one render assertion each that the sidebar wordmark (`AppShell.tsx:36`) and the pairing-screen brand slot (`AuthGate.tsx:23`) render `BRAND.productName` (token-relative — these stay green across the flip and prove the REACH, per census §3). Use the existing component-test harness the repo already uses for `AppShell`/`AuthGate` (find it: `git grep -l "AppShell\|AuthGate" -- "web-ui/dashboard/src/**/*.test.tsx"`); if neither component has a render test today, the two render rows are OUT and the file carries the pin only — say which in the return. |
| `web-ui/dashboard/src/views/EventsView.unserved404.test.tsx` | **M** | `:153` `.not.toContain('HomeSynapse')` → `.not.toContain(BRAND.productName)` (+ the `BRAND` import from `../lib/i18n` — match the file's relative-import style). The assertion's meaning is unchanged (the minted `endpoint-not-in-this-release` copy is name-light); it now survives the rename. |

## 2. The red arm (the proof that the gate gates — #18; report it, do not commit it)

On the host checkout, with the two files in place and `npm run verify` GREEN: temporarily set `i18n.ts:18` to `productName: 'ZZ-PLACEHOLDER'`, run `npm test` (or the verify script's test step) → **exactly ONE failure**: the new pin (`toBe('HomeSynapse')`); every other test green (the REACH rows and the re-keyed negative assertion follow the token). Then `git checkout -- web-ui/dashboard/src/lib/i18n.ts` → porcelain shows ONLY the two files of this WU. Paste the one-failure output into the return. (A second failure anywhere = a hidden literal the census missed — STOP, paste.)

## 3. Predictions (H12)

`npm run verify` GREEN: `tokens:check` untouched · lint clean · typecheck clean (the pin compares a `string` literal type — `as const` makes `BRAND.productName` the literal type `'HomeSynapse'`; `toBe('HomeSynapse')` is well-typed; at the swap both sides change together) · tests 210 → 211–213 · build/bundle/contract unaffected. `frontend.yml` GREEN on the push (both files match the path filter). The census commit of record stays `89a912e`; this WU changes no census class (the pin is a TEST literal — it joins the §2 IN table as row 8, "the gate", so the flip WU's count becomes **5** (4 + the pin's own update) — record that in the return so the runbook's H+2–6 count is right).

## 4. Return shape (≤ 1 page)

Census (2) · the verify output tail · the red-arm one-failure paste · the porcelain after restore · the updated flip-WU count · pushback.
