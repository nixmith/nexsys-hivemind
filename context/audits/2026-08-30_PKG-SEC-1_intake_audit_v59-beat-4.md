<!--
file: context/audits/2026-08-30_PKG-SEC-1_intake_audit_v59-beat-4.md
purpose: The hub's two-layer audit of the PKG-SEC-1 Coder-lane return (2026-08-30_PKG-SEC-1_return.md, 8.3 KB) — layer 1 the return read whole; layer 2 the hub re-executed at the instrument against the ACTUAL git diff (D2).
audience: Nick (commit + push + CI read) · the spine
state-type: intake audit (v59 beat 4)
status: FILED. VERDICT: ACCEPT, CLEAN — zero blocking notes. Gate of record: CI on Nick's push; OR-TOKEN-MODE-644 closes at green.
-->

# PKG-SEC-1 intake audit (v59 beat 4)

## §0 Verdict
**ACCEPT, CLEAN.** The delta is §2-exact, census-exact (3 M at `7c57d7f`, nothing committed), all fences held, and every gate the lane claimed was RE-RUN by the hub at the instrument, not taken from the report.

## §1 Layer 2 — hub re-execution at the bytes (each check re-run, not re-read)
- Porcelain: exactly 3 M — the three named files, nothing else; HEAD `7c57d7f` unmoved.
- The FULL diff read (D2): run-smoke +7 lines inside the `[ -s "${HS_TOKEN_FILE}" ]` arm, immediately after the config-dir check — comment wording-verbatim over 3 physical lines (disclosed dev-1), FMODE pair for `${HS_TOKEN_FILE}` and `${HS_CONFIG_DIR}/api_tokens` (the instruction's sanctioned existing-var branch, dev-2), existing ok/bad idiom, no check headers touched. build-deb.sh:24 = the exact §2(2) form. build-image.sh:75 = LTD-10→LTD-01, one token.
- ok-sites re-counted: **23** (was 21) ✓. `bash -n` re-run ×3: clean ✓. LF re-verified ×3 (no CR bytes) ✓. build-deb:24 vs build-image:35 `cmp`: **IDENTICAL** ✓.
- The 644-mutation proof ran LIVE (WSL native fs) with BOTH arms quoted — the anti-vacuous pairing (#19) satisfied; an F-S10 recurrence now reds both CI legs.
- Store-absence semantics verified at source by the lane (`ensureInitialToken` mints before `writeArtifact` — OpaqueTokenStore `:366–:381`): an absent `api_tokens` inside the -s arm is a true defect. Sound.
- Deviations 3/3 cosmetic, disclosed, within the instruction's own branches — ACCEPT. Pushback: the GNU-`stat` note is correct and correctly not acted on.
- Note: the `git diff` CRLF warnings on Nick's checkout concern OTHER files (build.gradle.kts, docs, fixtures — the known autocrlf class); the three touched files are LF-clean.

## §2 The §4 stale-constant sweep (run this beat)
10 hits. 9 = HISTORICAL BY CONSTRUCTION (dated operator packets, superseded v56/v57 prompts, pm-handoff beat blocks, the two instructions' own before-counts) — the instruction pre-ruled the card-sitting "18/18" class never re-pins. 1 ACTED: `handoff/coder-handoff.md` carried an R-9-era NEXT-WU block quoting "19 PASS lines" — a CURRENCY STAMP now heads it (R-9/R-7b/R-3b landed; current WU = PKG-SEC-1; ok-sites now 23).

## §3 What banks at CI green
Nick: review diff → stage exactly the 3 → `commit -F ../_scratch/2026-08-30_core_PKG-SEC-1_commit-msg.txt` → push → relay: Build & Check GREEN · install-smoke BOTH legs GREEN with the two new `PASS ... mode 600` lines per leg (the first mechanical confirmation of the R-6/R-8 mint fix on a fresh install) · update-smoke unaffected. Then the hub banks the verdict, CLOSES OR-TOKEN-MODE-644 (the mint half re-recorded ALREADY-DONE-AT-HEAD, v57 b7), and the desk-gotcha harvest (msys TZ silent-GMT fallback · MSYS2_ARG_CONV_EXCL) rides the next lessons fold.
