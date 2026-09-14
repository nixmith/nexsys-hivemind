<!--
file: context/audits/2026-09-13_v74-b2_W-SKILLS-9_intake_two-layer-audit.md
purpose: The hub's two-layer intake of W-SKILLS-9's return (`context/audits/2026-09-13_W-SKILLS-9_return.md`, 8,853 B): the claims read critically (§1), the hub's own re-execution at the bytes (§2), what was not re-executed (§3), the verdict and the register row (§4).
audience: the hub · Nick (the verdict; the two cards) · the next skills lane
state-type: intake audit (FILED at v74 beat 2)
status: FILED — Sun 2026-09-13 ~19:3x CT (instrument 2026-09-14T00:36:45Z); verdict ACCEPT
last-verified: 2026-09-13 (v74 beat 2)
-->

# W-SKILLS-9 — intake, two layers

## §0 Card
- **The return:** exists at the named path; last line `RETURNED nexsys-hivemind/context/audits/2026-09-13_W-SKILLS-9_return.md 8853` = its byte count. Nick's relay (Sun 09-13 ~19:3x CT): hivemind 10 M + 1 A, skills 4 M, zero rule names lost, Check 12's three sections byte-identical, P4 on four wrong cites — every count re-derived below.
- **Verdict: ACCEPT.** Zero rule names lost (the hub's census 68 → 73 distinct, 0 lost); the three Check 12 sections identical; 13/13 md5s equal; `pm-lessons.md` changed only in nine heading lines; no SKILL.md gained a sha or a beat number; the fold rows resolve at the lines the return names. **Check 9 PASS 28/28** — Nick's account sync equals the post-fold SOURCE trees at every md5 (the record catches up on the two cards).
- **Register:** IR-11 — the charter's census (9 hivemind, 3 skills) was typed, not counted from its own fold table (10, 4). The lane's P1 refutation is the finding; the instrument is a charter self-check.
- **Census for the cards:** hivemind 18 = 16 M + 2 A (the lane's 10 M + the return; the audit; the register; the charter's status; the four spine files) by explicit paths; skills 4 M by explicit paths.

## §1 The claims, read critically
The return's §0 claims: a baseline of empty porcelain at 00:04Z (true at 23:56Z per the hub's own boot HEADs); one `M` row not the lane's (the H8-a packet, the hub's b1 re-cut at 00:10Z — correctly attributed, correctly left out of the lane's census); 10 M + 1 A in the hivemind and 4 M in the skills (the charter's 9 and 3 were wrong — the lane's P1 refutation stands); 78 → 82 rule names, 0 lost; arcs 55 → 57; the Check 12 section md5 `3a3e14b4…` / 3,275 B in all three copies; four wrong cites in the charter (a "commit-boundary arc" that did not exist in the ledger; a Check-12 sentence already at HEAD; the census arithmetic; `pm-lessons.md` "lines 316–342" for a 341-line file) plus the mint's `splice_lib_v2.py` pointer corrected to v1 with `precheck()` named as the next version's block. The claims are specific, cite lines, and the deviations are declared with the rows. Nothing in the return asks the hub to take a count on faith.

## §2 The hub's re-execution (device, 2026-09-14T00:36Z)
1. **Rule-name census** — `grep -o` of every `**THE …**` / `**UPPER-CASE NAME**` token over the 14 files (10 hivemind + 4 skills) at HEAD (`git show HEAD:`) and in the tree: **68 → 73 distinct, 0 lost, 5 gained** (THE CORRECTION-BEFORE-FREEZE RULE · THE HANDS RULE — re-cuts THE COMMIT-BOUNDARY LAW · THE OUTPUTS-PATH MIRROR · THE REGISTER OF RECORD · THE SAME-PATH RE-WRITE). The lane's pattern counted 78 → 82; the two patterns differ in width, agree on zero lost.
2. **The ledger's arcs** — `(56)` and `(57)` present at `laws-ledger.md:79–80` with the addendum line at :78; the status line names them.
3. **Check 12's shared section** — `sed -n '/^### Check 12/,/^## 3\./p'` less its last line: md5 `404da674` / 3,276 B in `project-manager/references/freshness-preflight.md`, `coder/references/freshness-preflight.md` and `nexsys-skills/orchestrators/nexsys-frontend/references/freshness-preflight.md` — identical (the lane's `3a3e14b4…` / 3,275 B is the same section cut one byte differently).
4. **The md5 list** — the return's §3 (13 files) against `md5sum` of the tree: 13 equal, 0 mismatched.
5. **State-free SKILL.md** — 0 seven-hex shas in the three; `beat [0-9]` count unchanged (PM: 1 at HEAD, 1 in the tree — the pre-existing v69 provenance line); the diffs 6+/4−, 2+/2−, 2+/2−.
6. **`pm-lessons.md`** — `diff -U0`: 0 changed lines outside `## 20…` headings; 9 headings gained `— FOLDED W-SKILLS-9`; the file is 341 lines (P4 iv).
7. **The fold rows resolve** — CIF's Additions at :561 (#31 THE PRIOR-LEDGER GATE); the WUCP rig line at :310; R&Q §3's rule at :195; the environment model's §12 addendum at :103–105 (the same-path re-write; the outputs-path mirror).
8. **Check 9 now** — the SOURCE trees' 28 md5s (device) against the session's synced copies (container): 28/28 identical — Nick's "fully updated the skills" line verified at the bytes; the synced PM SKILL.md's status line reads W-SKILLS-9.

## §3 Not re-executed (disclosed)
- The lane's per-row `str.replace` script (`$HOME/w9/rep.py`, outside the mount) — not read; its effect is the diff, which §2 covers.
- The four corrected cites' wording was not re-read line by line beyond §2.2 and §2.7 (the arcs and the rows exist where the return says).
- The lane's byte deltas per file (its §1) — not re-summed; `git diff --stat` reads 48+/25− across the ten hivemind files and 9+/6− across the four skills files.

## §4 Verdict and the register
**ACCEPT.** The charter's status → EXECUTED with this commit. **IR-11** appended to `context/planning/improvement-register.md`: a fold charter's census must be counted from its own fold table (distinct target files) before it is stated; W-SKILLS-9's charter typed 9/3 against a table of 10/4 — the lane refuted P1 and was right.
