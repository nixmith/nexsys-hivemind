<!--
file: context/instructions/2026-08-28_PKG-SEC-1_run-smoke-token-mode_and_version-symmetry_coding-instruction.md
purpose: PKG-SEC-1 — the packaging batch that closes OR-TOKEN-MODE-644's residue + the two R-7b parked INFOs, SHELL-ONLY (3 M, zero Java). THE INSTRUMENT CORRECTION THAT RESHAPED THIS WU (v57 beat 7, read at source): the OR's "mint 0600 in core FIRST" half is ALREADY DONE at HEAD — `OpaqueTokenStore.writeOwnerOnlyAtomically` (`api/rest-api/...:742–:770`) writes BOTH `api_tokens` and `initial_api_token` owner-only from the first byte (CREATE_NEW with a 0600 attribute, umask re-assert, ATOMIC_MOVE; its own Javadoc names the old 0644 behavior: "the artifact and the store previously took umask-default 0644"), and `ensureInitialToken()`/`rotate()`/`persist()` all route through it. The held card's 644 files are the Aug-13 PRE-FIX vintage. What remains: (1) run-smoke gains the file-mode check CI is structurally blind without, (2) `build-deb.sh` gains the HS_VERSION forward `build-image.sh` already has, (3) `build-image.sh:75`'s comment cites LTD-01, not LTD-10.
audience: a host-side Claude Code Coder lane (D12; ~20 min) + Nick (commit + push + CI read) + the hub (audit).
status: **ISSUE-READY — HELD UNTIL POST-R-4** (the next core touches are R-3b then this; dispatch Sunday evening 2026-08-30 after the R-4 record files, or any day after). Baseline: the core HEAD of dispatch day (verify at checkout; the three touched files are byte-stable since `dec35be` except any R-3b delta, which touches none of them).
return: nexsys-hivemind/context/audits/<filing-date>_PKG-SEC-1_return.md.
fences: ZERO Java (the mint fix exists; if a .java edit seems needed, STOP — the premise has drifted) · `distribution/README.md` untouched · the CI twins untouched · the systemd unit untouched (R-3b owns it) · no attribution trailers.
-->

# PKG-SEC-1 — the token-mode check + version symmetry + the LTD comment (3 M, shell-only)

## §1 Files to read first

`api/rest-api/src/main/java/com/homesynapse/api/rest/OpaqueTokenStore.java` `:359–:428` + `:735–:790` (READ-ONLY — the proof the mint/rotate/persist paths all write 0600; you change nothing here) · `distribution/smoke/run-smoke.sh` WHOLE (the check-5 region `:139–:150` is the seam; 21 `ok "` sites today; reuse its existing `HS_*` vars and `ok`/`bad` idiom) · `distribution/deb/build-deb.sh` `:24` · `distribution/image/build-image.sh` `:35` (the symmetric form to copy) + `:75` (the comment) · `nexsys-hivemind/context/audits/2026-08-23_card-sitting_Blocks-1-3_operator-return.md` F-S10 (the field observation that minted the OR — the 644 vintage).

## §2 The delta — stages exactly 3 M

**(1) `distribution/smoke/run-smoke.sh` — check 5 grows two mode assertions** (immediately after the existing owner/config-dir lines, same idiom): for the pairing artifact `${HS_TOKEN_FILE}` and for the store file (`api_tokens`, same directory — derive it from the existing vars, e.g. `"$(dirname "${HS_TOKEN_FILE}")/api_tokens"`, or the file's existing var if one exists — read the source):
- `FMODE="$(stat -c '%a' <file> 2>/dev/null || echo '?')"` then `[ "${FMODE}" = "600" ] && ok "<name> mode 600 (owner-only)" || bad "<name> mode ${FMODE}, expected 600"` — one pair per file, guarded so a legitimately-absent store file (pre-first-mint orderings, if any — read the check-5 flow) reports `bad` only when the mint is claimed done (the check already sits inside the `[ -s "${HS_TOKEN_FILE}" ]` arm — keep the new lines inside it).
- A one-line comment above them: *"OR-TOKEN-MODE-644: the mint writes 0600 at HEAD (OpaqueTokenStore.writeOwnerOnlyAtomically); this check makes CI structurally able to SEE a regression — the 2026-08-13 vintage shipped 644 and stayed green (the card-sitting F-S10)."*

**(2) `distribution/deb/build-deb.sh:24`** — the HS_VERSION forward, byte-symmetric with `build-image.sh:35`: `VERSION="$(HS_VERSION="${HS_VERSION:-}" HS_DIST_DIR="${DIST}" bash -c '. "'"${DIST}"'/common.sh"; hs_version')"` (the R-7b audit's parked INFO: an explicit `HS_VERSION` override reaches the image build but not the deb build — asymmetric).

**(3) `distribution/image/build-image.sh:75`** — the comment token only: `(reproducibility/LTD-10)` → `(reproducibility/LTD-01)` (the R-7b audit's parked INFO; LTD-01 is the JDK-21 constraint the warning actually enforces).

## §3 Watch-outs

Shell only; `bash -n` both build scripts + run-smoke after editing · run-smoke's PASS-line count grows 21 → 23 `ok` SITES (the historical "18/18" records are the card-sitting's, never re-pinned — but SAY the new expected line-count in the return so the next operator packet quotes it right) · keep LF endings + the box-comment style · do NOT renumber the check headers · red-first accounting (#18): the mode check's red leg exists HISTORICALLY (F-S10's 644 observation on the Aug-13 vintage) and cannot red at HEAD (the fix landed with R-6/R-8) — green-by-construction, DISCLOSED; the mutation proof: state in the return what the check prints if a file were 644 (run the stat arm against a scratch 644 file locally if the host allows).

## §4 Gates + CI predictions (H12, filed here)

Porcelain = exactly 3 M. On Nick's push: `CI / Build & Check` GREEN · install-smoke BOTH legs GREEN with the fresh runner mint landing 0600 under the new check (**this run is also the first mechanical confirmation of the R-6/R-8 mint fix on a fresh install**) · run-smoke's log shows the two new `PASS ... mode 600` lines per leg · update-smoke unaffected. The hub updates OR-TOKEN-MODE-644 at the banking beat: closes when this lands green (the "mint 0600" half is re-recorded as ALREADY-DONE-AT-HEAD, found at source v57 beat 7). **The hub's audit ALSO sweeps the instrument corpus for the now-stale PASS-count constants** (`grep -rn '18/18\|19 PASS\|18 \[smoke\]\|21 ok'` over `context/{handoff,instructions,process}` + the packets) — the F-S19 class: a pinned count that drifts stale bites the next operator; every hit is either updated or marked historical.

## §5 Return shape (≤ 1.5 pages)

§0 census (3 M, porcelain paste) · §1 the run-smoke diff verbatim + the new ok-site count · §2 the two one-line diffs · §3 `bash -n` results + the 644-mutation statement · §4 pushback · ≤ 3 harvest lines.
