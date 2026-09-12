<!--
file: context/audits/2026-09-11_HERO-1b_intake_two-layer-audit_v70-b9.md
purpose: The hub's two-layer intake audit of HERO-1b's return (context/audits/2026-09-11_HERO-1b_return.md, 12,242 B): the claims read critically, the hub's re-execution at the bytes on the device, the rulings on D1–D7 and the two [REVIEW] rows, the landing card's shape, and what HERO-1c inherits.
audience: the hub · Nick (§0)
state-type: intake audit (filed; never rewritten)
status: FILED at v70 beat 9 (Fri 2026-09-11 ~22:1x CT; instrument 2026-09-12T03:13:45Z) — the post-close intake, on Nick's word.
-->

# HERO-1b intake — two layers (v70 beat 9)

## §0 Verdict
**ACCEPT.** B1–B7 and B9 landed under `web-ui/dashboard/src/` with a test per row, RED at HEAD then GREEN (B6 the named preservation row); the census is exactly what porcelain shows (16 M + 1 A); the fixtures are byte-identical; `npm run verify` ran on a real Linux toolchain (21 files / 392 tests / 0 failed; bundle 69.9 of 100 KB; contract-check OK; exit 0); `frontend.yml` on Nick's push is the gate of record. P1 MISSED on the charter's own count (the charter's table named 15 files and guessed a scenario file that does not exist; the lane's 16 + 1 is the truth and two of them are ruled below); P2–P5 MET. The return adjudicates first, names every artifact, and files the six §10 sentences verbatim. HERO-1c is named and grounded.

## §1 Layer 1 — the claims, read critically
The card leads with the predictions and owns the miss. The red-first column is per row with counts (47 of 54 headline assertions red at HEAD; 11/11, 3/6, 3/4, 4/4). D1 catches a contradiction between the charter's R5 ("word for word") and the wire (`firingValue` null on every run today) and resolves it the honest way: the screen says "changed at", never "detected motion" the wire did not carry. D4 removes the wire's `explanation` sentence from the why-not card on the design of record and says how to revert. D2/D3/D5 name SPEC gaps by line. The skill note corrects O3 (the Linux VM runs the toolchain with `node_modules` outside the mount).

## §2 Layer 2 — the hub's re-execution at the bytes (device, 2026-09-12T03:13:45Z)
1. **Census at porcelain, scoped:** `git status --porcelain -- web-ui/dashboard` = 16 M + 1 A; nothing under `design/`; numstat +1,337 / −285.
2. **Fixtures:** `src/lib/api/fixtures/` shows no change at porcelain; md5 prefixes `896f861d` · `6f502c7b` · `05b02fbc` match the return.
3. **Name-light (R4):** `BRAND.productName` = 0 in `format.ts`, `CausalChain.tsx`, `StatusPill.tsx`, `WhyNotView.tsx`; its 9 uses in `i18n.ts` are the pre-existing non-hero keys (`auth.`, `boot.`, `devices.`, `health.`, `overview.`, `origin.`, `events.`); no " we " in `i18n.ts`. The `{{NAME}}` token is the design files' convention; in source the brand accessor is the single indirection — R4 read accordingly.
4. **R5:** the six sentences quoted in the return match SPEC §10 word for word except the two wire-owned slots (`{triggerVerb}` → "changed" while `firingValue` is null; `{time}` with the date). Ruled below.
5. **The tests:** `format.test.ts` carries 51 top-level `it(` (the return counts 54 including nested forms); the vitest total 392 against 307 at HEAD is the lane's measurement, not re-run here.
6. **The gate:** not re-run by the hub (no Node toolchain in the hub's shell); `frontend.yml` on the push is the gate of record and banks as one spine line.
**Not re-executed (disclosed):** the red-at-HEAD counts per row (read against the return's description, not re-run); the bundle size.

## §3 Rulings (DELEGATE — Nick's `REVERT <row>` flips any one)
- **D1 — ACCEPT; R5 stands modulo the wire-owned slots.** "Detected motion" lands when `firingValue` is populated (EXPLAIN-114a's key; B8's row). The charter's R5 was over-strict against its own B7.
- **D4 — ACCEPT.** The design of record (SPEC §2) gives the wire's `explanation` no slot, and Core's DP-B2 sentence (`StandardExplanationService.java:355–:356`, "last fired and confirmed at …") claims what Q1 (a) declined to infer from a run id. Docketed for the Core side: EXPLAIN-114b carries `FIRED_CONFIRMED` evidence into that sentence or drops the claim.
- **The two files beyond the table ([REVIEW]) — ACCEPT:** `WhyNotView.module.css` (+2, the `.body` class) and `WhyNotView.nullability.test.tsx` (two assertions pinning the keyed N2 sentence).
- **D2, D3, D5 — the SPEC gaps** (a terminal-line key; the N4/N6 no-time keys; a null/unknown action-outcome headline cell) → one SPEC §7 amendment, the hub's, docketed with HERO-1c's charter.
- **D6/D7 → HERO-1c** (the action step lines and helps from §5/§7; retire `format.ts:208`'s "We sent it"; wire the catalog keys outside the B-rows).
- **MODULE_CONTEXT** (`web-ui/dashboard/MODULE_CONTEXT.md` exists; the write-set excluded it): the hub's WUCP Phase-2 obligation — written with HERO-1c's landing.
- **The skill note** → W-SKILLS-9: the frontend skill's O3 sentence ("the Linux shell cannot run the toolchain") is corrected to "with `node_modules` installed outside the mount, it can".

## §4 The landing (Nick's hands)
`git add -A web-ui/dashboard` → 17 = 16 M + 1 A → the commit from `_scratch/2026-09-11_core_HERO-1b_commit-msg.txt` → push; `frontend.yml` GREEN is the gate; the `ci` run on the same push is another sample of the bus class. Land it AFTER FIX-2b-i's card so the Java sample stands alone.
