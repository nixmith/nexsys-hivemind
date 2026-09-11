<!--
file: context/audits/2026-09-11_HERO-1_return.md
purpose: HERO-1 lane return — the first design of the explainability hero (SPEC.md · states.html · README.md under web-ui/dashboard/design/hero-v1/). Design only; nothing under src/ touched; nothing staged or committed.
status: RETURNED 2026-09-11 (instrument 20:48Z open; CT = UTC−5 → 15:48 CT); reports to the hub.
-->

# HERO-1 — the explainability hero, designed from its empty states outward (return)

## §0 Card
- **Predictions first: P1 MET · P2 MET · P3 MET · P4 MET.** P1: SPEC §3 has 30 explicit cells (5 `RunStatus` × {5 `ActionOutcome` + no-action}), each with a sentence + key, plus the silent-skip row and two mode overrides (superseded / expired-restart never headline as "failed"); its second table has all 4 `NonFiringVerdict` values + 3 derived states, each with a no-time arm; every slot null arm is its own `explain.slot.*` key — no cell infers. P2: `grep -ril` for the three candidate names, the codename and the company name (pattern held by the hub, not written here) over `design/hero-v1/` → no match, run on the tree after the write; `{{NAME}}` appears 6×. P3: `git --no-optional-locks status --porcelain -- web-ui/dashboard/src` → 0 lines at close; under `web-ui/dashboard` only `?? web-ui/dashboard/design/`. P4: the charter's `CausalChain :358–:373 (cascade :372)` is wrong at `eabdbb1` — `contract.ts:367–:385`, `cascade :384`; the `resultOutcome` note is `:346–:353` (charter `:353–:355` = the `settled` note); `commandVerb` is `:519–:532` (charter `:519–:530`). `:140`, `:150`, `:153–:157`, `causalSentence :472`, `WhyNotView.tsx:91` are exact.
- **Baseline held:** HEAD `eabdbb1`; `-- web-ui/dashboard` porcelain EMPTY at open; whole tree clean at open and close.
- **Census (write-set = exactly three files; md5 identical container → disk):** `web-ui/dashboard/design/hero-v1/SPEC.md` 57 427 B `307a07ba…` · `states.html` 80 605 B `e29f21c3…` · `README.md` 881 B (5 lines) `15cd3fae…`. No `git add/stash/checkout/commit`; no installs; `package.json`, Vite, tokens, CI untouched.
- **Instrument limit:** a cloud shell (reaches the tree only through the device bridge) + a Linux VM shell on the Windows tree, no network. `npm run dev` does NOT run there (`rollup/dist/native.js` throws — FE-NULL-1 O3 stands); designed from source + fixtures. Contrast and reading grades computed by script from `tokens.css` and the copy catalog (SPEC §7/§8). Mockups rendered in headless Chromium container-side and inspected; the repo files are the record.
- **Preflight:** CONTRACT_VERSION `v1.1.3-2026-09-06` at source; skill mirror PASS (8/8 md5 identical, `nexsys-skills` source vs the loaded skill); the charter's `{{NAME}}` token rule applied over brand-ref §6.1. Not re-read: PROJECT_SNAPSHOT, Check 12.
- **Defaults taken (SPEC §12 carries the direction-changing ones):** D1 leading action = `actions[0]`; D2 COMPLETED runs device-led, other statuses automation-led frame + one device tail; D3 N3 ("It did run") demoted from `ok` to `info`; D4 the permanence footer written name-free (Register C); D5 era-boundary tell = empty arrays + (`automationName` null ∨ `trigger.type` null); D6 modes 1 and 3 share the warn hue (glyph + label distinguish); D7 all glyphs reuse `MODE_GLYPHS`, no new shape; D8 L2 bodies use `--hs-text-secondary` (muted fails AA on the sunk surface).
- **Questions for Nick:** six, §3 (none blocks the build).

## §1 What was designed (one line each)
1. SPEC §1–§2: purpose + IA — three questions, two disclosure levels, what never appears (index paths, ids, a free graph); the hub keeps its shape, copy only changes.
2. SPEC §3: the L1 grammar — 30 cells + overrides + the 7 why-not rows, slot table with every null arm keyed; a SKIPPED/FAILED/CANCELLED/INTERRUPTED run never opens with a device acting (the O1 defect closed at the grammar).
3. SPEC §4: the four empty states as full copy, HERO-0's words improved where the mom test asked (each change justified).
4. SPEC §5: the five modes + three neighbours (label · glyph · tone · line · help), the per-capability window with no UI timer, idempotent no-report, `UNCONFIRMABLE` → immediate honest UNCONFIRMED, superseded expiry.
5. SPEC §6: EXPLAIN-1..9 — today's sentence / landed sentence / key, per surface.
6. SPEC §7: the copy table, 140 keyed strings, Register C, grade + words/sentence measured, DAS §2.2 banned list zero hits by script.
7. SPEC §8–§9: AA computed for every pair in both themes (all state pairs pass; three pairs to avoid named); tokens by state; two token REQUESTS (T1 light muted-on-bg 4.28 < 4.5; T2 margin on the light ok/error pills).
8. SPEC §10–§12: the six-sentence acceptance script, nine ordered build rows (B1 = `causalSentence` per outcome with its test), six questions.
9. `states.html`: 94 cards, each dark + light — the reference run card, all 30 cells + 3 extras, the modes exhibit (R6), the four empty states, N1–N7, the error/offline/replaying posture; token values named in comments; no scripts, no external resources.

## §2 Coverage counts
- Headline table: **30 / 30** (RunStatus × {ActionOutcome ∪ none}) + 3 extra rows (silent skip, 2 overrides). Slot null arms: **12 / 12** keyed.
- Why-not table: **7 / 7** (4 verdicts + 3 derived), each with a no-time arm where `{time}` can be null (5 rows).
- Empty states: **4 / 4** (title + body + placement). Confirmation modes: **5 / 5** distinct + 4 neighbours.
- EXPLAIN rows: **9 / 9** with today / landed / key. Copy table: 140 strings; longest sentence 21 words; 85 gradeable sentences, 81 ≤ 9.0, max 9.3.
- Contrast: **20 / 20** state pairs ≥ 4.5:1 (10 per theme); 3 non-hero pairs below AA named and avoided.

## §3 Questions for Nick (mirroring SPEC §12; `HERO1: Qn <word>`)
- **Q1** N3 inference wording until `FIRED_CONFIRMED`: (a) "It has run — most recently at {time}." info + link (rec) · (b) keep "It did run" ok · (c) refuse the inference.
- **Q2** sent-but-unconfirmed headline verb: (a) "was asked to turn on" (rec) · (b) "was sent the command to turn on" · (c) "should be turning on" (rejected by the honesty law).
- **Q3** permanence footer: (a) name-free, Register C (rec) · (b) keep `{{NAME}}` as the one brand moment on the run page.
- **Q4** non-completed runs automation-led (rec) vs device-led with a negated verb.
- **Q5** token requests: (a) rule T1 + T2 (rec) · (b) T1 only · (c) defer.
- **Q6** era-boundary tell: (a) name/type-null + empty arrays (rec, now) · (b) ask Core for a `skeleton`/era marker (cross-lane, v1.1.4+).
- Cross-lane asks recorded: the EXPLAIN-1..9 keys (v1.1.4 owns them); Q6(b); a confirmed-from-cache indicator for the idempotent no-report case.

## §4 Next recommended lane (refuse to close)
The hub's audit (R1–R7; R4 grep and R6 `states.html` open) → Nick's `git add -A web-ui/dashboard/design` card and the `HERO1:` ruling batch → **HERO-1b / FE-114**: SPEC §11 B1–B7 on the then-current mirror (B1 first: `causalSentence` per outcome with its test — one small PR), B8 as each v1.1.4 key lands. Register: DESIGN-COMPLETE, BUILD PENDING; nothing here is live-verified because nothing here runs.

RETURNED nexsys-hivemind/context/audits/2026-09-11_HERO-1_return.md 7294
