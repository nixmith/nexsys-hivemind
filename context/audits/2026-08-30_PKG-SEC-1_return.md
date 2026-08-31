<!--
file: context/audits/2026-08-30_PKG-SEC-1_return.md
purpose: Coder-lane return for PKG-SEC-1 (run-smoke token-mode check + version symmetry + the LTD comment; 3 M, shell-only).
instruction: context/instructions/2026-08-28_PKG-SEC-1_run-smoke-token-mode_and_version-symmetry_coding-instruction.md
lane: host-side Claude Code Coder, Windows desk (Git Bash + WSL), 2026-08-30 evening CT.
-->

# PKG-SEC-1 return — token-mode check + version symmetry + LTD comment

## §0 One-screen summary

**Census: exactly 3 M, nothing else.** `git --no-optional-locks status --porcelain`:

```
 M distribution/deb/build-deb.sh
 M distribution/image/build-image.sh
 M distribution/smoke/run-smoke.sh
```

**Baseline verified before editing:** HEAD `7c57d7f`, porcelain clean; `git diff --stat dec35be..HEAD --` over the three files EMPTY (byte-stable since `dec35be`; R-3b touched none of them). No drift → proceeded.

**Gates run, all green:** `bash -n` × 3 OK · ok-site count **21 → 23** (`grep -c 'ok "'`) · build-deb.sh:24 vs build-image.sh:35 VERSION lines **byte-identical** (`cmp` clean) · the §3 644-mutation proof RUN LIVE in WSL (native fs, real chmod — see §3) · `file` reports all three still UTF-8 shell scripts, no CRLF · fences held: zero Java (OpaqueTokenStore read READ-ONLY, the 0600 proof confirmed at `:748–:779`), README/CI-twins/unit untouched, no trailers, NOTHING committed.

**Deviations (3, all cosmetic, disclosed):** (1) the §2(1) comment is wording-verbatim but wrapped over **3 physical lines** to the file's comment width — a ~230-char single line would break the style §3 says to keep; (2) the store path is derived as `"${HS_CONFIG_DIR}/api_tokens"` — the instruction's "or the file's existing var" branch (`HS_TOKEN_FILE` is defined in common.sh as `${HS_CONFIG_DIR}/initial_api_token`, so same-dir holds by construction; check 5 already uses `${HS_CONFIG_DIR}`); (3) `FMODE` is reused sequentially for both pairs, per the instruction's own template.

**Asks:** none blocking. Nick: commit + push; the H12 predictions to read on CI are the instruction §4's (both install-smoke legs green, two new `PASS ... mode 600` lines per leg — the first mechanical confirmation of the R-6/R-8 mint fix on a fresh install).

**Instrument limits hit (details in harvest):** msys `TZ=America/Chicago date` silently falls back to GMT (printed 2026-08-31); this filename's date was re-derived at the instrument via the machine's local CDT clock + the Windows tz database (both say **2026-08-30**). msys path-conversion mangled the `/mnt/c` argument to `wsl` (fixed with `MSYS2_ARG_CONV_EXCL='*'`).

**Proposed commit message paragraph:**

> distribution: PKG-SEC-1 — run-smoke check 5 grows the two token file-mode assertions CI was structurally blind without (the pairing artifact + the api_tokens store, both expected 600; inside the `[ -s "${HS_TOKEN_FILE}" ]` arm so an absent store reds only when the mint is claimed done; the OR-TOKEN-MODE-644 comment names the mint fix at OpaqueTokenStore.writeOwnerOnlyAtomically and the F-S10 Aug-13 644 vintage; ok-sites 21 → 23) + build-deb.sh:24 gains the HS_VERSION forward byte-symmetric with build-image.sh:35 (the R-7b parked INFO: an explicit override now reaches BOTH builds) + build-image.sh:75's JDK-21 warning comment cites LTD-01, not LTD-10 (the constraint the check actually enforces). Zero Java — the mint fix exists at HEAD, verified read-only. Stages exactly 3 (3 M): distribution/smoke/run-smoke.sh, distribution/deb/build-deb.sh, distribution/image/build-image.sh

## §1 The run-smoke diff, verbatim

```diff
@@ -144,6 +144,13 @@ if [ -s "${HS_TOKEN_FILE}" ]; then
     # Config dir must not be world/other-accessible (secrets are 0600-class).
     CMODE="$(stat -c '%a' "${HS_CONFIG_DIR}" 2>/dev/null || echo '?')"
     case "${CMODE}" in *0|*00) ok "config dir mode ${CMODE} (no world access)";; *) bad "config dir mode ${CMODE} allows other access";; esac
+    # OR-TOKEN-MODE-644: the mint writes 0600 at HEAD (OpaqueTokenStore.writeOwnerOnlyAtomically);
+    # this check makes CI structurally able to SEE a regression — the 2026-08-13 vintage
+    # shipped 644 and stayed green (the card-sitting F-S10).
+    FMODE="$(stat -c '%a' "${HS_TOKEN_FILE}" 2>/dev/null || echo '?')"
+    [ "${FMODE}" = "600" ] && ok "pairing token mode 600 (owner-only)" || bad "pairing token mode ${FMODE}, expected 600"
+    FMODE="$(stat -c '%a' "${HS_CONFIG_DIR}/api_tokens" 2>/dev/null || echo '?')"
+    [ "${FMODE}" = "600" ] && ok "token store (api_tokens) mode 600 (owner-only)" || bad "token store (api_tokens) mode ${FMODE}, expected 600"
 else
     bad "no pairing token at ${HS_TOKEN_FILE}"
 fi
```

**New ok-site count: 23** (was 21; the next operator packet should quote 23 `ok` sites / up-to-23 PASS lines on a full systemd-mode run — the historical "18/18" records stay historical, never re-pinned). Check headers NOT renumbered.

**Store-absence semantics, confirmed at source:** `ensureInitialToken()` (OpaqueTokenStore `:366–:381`) mints (which persists the store) **before** `writeArtifact()` writes the pairing artifact — so inside the `[ -s "${HS_TOKEN_FILE}" ]` arm an absent `api_tokens` is a true defect and correctly reds (`mode ?, expected 600`). Pre-first-mint orderings never enter the arm.

## §2 The two one-line diffs

`distribution/deb/build-deb.sh:24` (now byte-identical to build-image.sh:35 — `cmp` verified):

```diff
-VERSION="$(HS_DIST_DIR="${DIST}" bash -c '. "'"${DIST}"'/common.sh"; hs_version')"
+VERSION="$(HS_VERSION="${HS_VERSION:-}" HS_DIST_DIR="${DIST}" bash -c '. "'"${DIST}"'/common.sh"; hs_version')"
```

`distribution/image/build-image.sh:75` (comment token only):

```diff
-[ "${JFEATURE}" = "21" ] || log "WARNING: JDK feature version is ${JFEATURE}, expected 21 (reproducibility/LTD-10)."
+[ "${JFEATURE}" = "21" ] || log "WARNING: JDK feature version is ${JFEATURE}, expected 21 (reproducibility/LTD-01)."
```

## §3 Gates + the 644-mutation statement

`bash -n` clean on all three edited files (Git Bash, bash 5.x).

**Red-first accounting (#18), disclosed as the instruction pre-ruled:** the check is green-by-construction at HEAD — the red leg exists HISTORICALLY (F-S10: the 2026-08-13 vintage shipped both files 644 and run-smoke stayed green because no check looked). The mutation proof was run LIVE: the exact stat-arm fragment (same vars, same `ok`/`bad` strings) against scratch files in WSL (native fs — real chmod; NTFS/Git-Bash chmod is not faithful). Output verbatim:

```
-- mutation: artifact chmod 644 --
[smoke] FAIL  pairing token mode 644, expected 600
-- healthy: artifact chmod 600 --
[smoke] PASS  pairing token mode 600 (owner-only)
-- mutation: store file absent --
[smoke] FAIL  token store (api_tokens) mode ?, expected 600
-- healthy: store file 600 --
[smoke] PASS  token store (api_tokens) mode 600 (owner-only)
```

So: a recurrence of the F-S10 vintage now prints `[smoke] FAIL  pairing token mode 644, expected 600` (and the store twin), flips the run-smoke verdict, and reds both CI legs.

## §4 Pushback

None that blocks. One observation, no action taken: `stat -c '%a'` is GNU-coreutils-only (not busybox/BSD portable) — but it is already check 5's established idiom (the OWNER and CMODE lines), and every target rig (ubuntu runners, Debian cards) carries coreutils; changing it was out of scope and would have widened the diff.

## Harvest (≤3)

- **Desk gotcha:** msys/Git-Bash `date` silently ignores IANA `TZ=` names (no tzdata) and reports GMT — `TZ=America/Chicago date` printed 2026-08-31 while true CT was 2026-08-30 19:38 CDT. Cross-derive CT from the machine's local clock or `powershell [System.TimeZoneInfo]::ConvertTimeBySystemTimeZoneId(...,'Central Standard Time')` on this desk.
- **Desk gotcha:** Git Bash path-converts `/mnt/c/...` arguments before they reach `wsl -e` (prefixes the Git install dir); `MSYS2_ARG_CONV_EXCL='*'` disables it. Companion to the known backslash-halving/drive-colon-split entries.
- The OpaqueTokenStore Javadoc at `:744–:746` self-names the old 0644 behavior ("the artifact and the store previously took umask-default 0644") — a good anchor if the hub wants a code-side cross-reference when closing OR-TOKEN-MODE-644.
