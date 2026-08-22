<!--
file: context/audits/2026-08-22_R7_arm64-artifact-channel_return.md
purpose: Coder return for WU R-7 / W2-1 — the arm64 artifact channel (the install-smoke two-architecture matrix) + rider F-V1 (R-D, the hs_version bare-id arm + the grammar assert + its fixture-paired test) + rider R-E (the action-major bumps). Filed 2026-08-22 (America/Chicago) against core HEAD 62dbca3 (the instruction's baseline 33861ad + the R-6/R-8 commit; the WU's trees byte-identical — §0).
audience: the hub (audit), Nick (commit + the CI verdict), the next lane.
instruction: context/instructions/2026-08-22_R7_arm64-artifact-channel_coding-instruction.md · pre-verification: context/pre-verifications/WU-R7.md
status: DELIVERED — the lane commits NOTHING; the hub audits, Nick commits; the install-smoke run on the push (BOTH matrix legs) + Build & Check is the gate of record (law 16).
-->

# R-7 / W2-1 — the arm64 artifact channel — return (2026-08-22)

**One line:** `install-smoke` is now a two-leg matrix (`ubuntu-latest`/amd64 unchanged + `ubuntu-24.04-arm`/arm64, `fail-fast: false`, per-arch artifact names) with an in-workflow ARCH-TRUTH assert and a VERSION-GRAMMAR echo after "Assemble .deb"; `hs_version` wraps EVERY non-tag-shaped describe id as `0.1.0+g<id>` (the `*.*` discriminator) and `build-image.sh` dies on any version of record that is not `^[0-9]+\.[0-9]+\.[0-9]+`, with `smoke/version-grammar-test.sh` (23 checks, mutation-verified twice) wired into the Static-lint step; `setup-java`/`checkout`/`setup-gradle` ride `@v5` in all three workflow files (every major verified to exist at the marketplace); `docs/architecture.md` gains "The artifact channel". Zero Java · zero `build.gradle.kts` · zero `README.md`. Census **exactly 7** (6 M + 1 A — the R-D-IN / R-E-IN count).

## §0 — P1–P8 re-verification at the checkout

**Baseline deviation (disclosed first, per Nick's dispatch word):** HEAD at launch is **`62dbca3`** (the R-6/R-8 TOKEN-OPS commit), not the instruction's `33861ad`. `git diff --name-status 33861ad 62dbca3 -- distribution .github` = exactly `M distribution/deb/homesynapse-token` + `A distribution/docs/token-rotation.md` — both outside this census; every file this WU reads or touches hashes IDENTICAL across `33861ad` → `62dbca3` → worktree (11 blobs compared by `git rev-parse <rev>:<path>` vs `git hash-object`). Porcelain EMPTY at launch (`git --no-optional-locks status --porcelain`). Report-and-proceed, not STOP. Duplicate-dispatch check: no R-7 handoff entry, no R-7 return on disk — a fresh dispatch.

| # | Verified at 62dbca3 | Outcome |
|---|---|---|
| P1 | One job `install-smoke` (`name: Build image + .deb, install-smoke on a clean machine`, `runs-on: ubuntu-latest`, `timeout-minutes: 25`); steps Checkout `@v4` · JDK 21 `setup-java@v4` corretto · `setup-gradle@v4` · `setup-node@v4` (22) · Static lint (`bash -n`) · Build image · Assemble .deb · sqlite3 prereq · Install-smoke (`sudo --preserve-env=JAVA_HOME`) · Update-smoke · Upload (`upload-artifact@v4`, `distribution-artifacts`, 7 days, `if: always()`) · journal on failure; triggers push main/develop on the six paths, PR main on four, `workflow_dispatch`. No matrix. | ✓ |
| P2 | `hs_deb_arch()` `:75–:84` — `HS_ARCH` override → `dpkg --print-architecture` → `uname -m` mapping (`aarch64\|arm64` → `arm64`) | ✓ (unchanged by this WU) |
| P3 | `diff` of the twins EMPTY at the worktree; `stat -c %h` = 1 on both (and on every other touched file) — no hardlink class | ✓ |
| P4 | `hs_version()` `:49–:70`: `HS_VERSION` `:50` · `VERSION` lookups `:52–:53` · `git describe --tags --always --dirty` `:55` · the comment `:57–:61` · the `case` `:62–:65` (`[0-9]*) printf '%s'` / `*) printf '0.1.0+g%s'`) · fallback `0.1.0-skeleton` `:69`. `git tag` EMPTY (no tags — the grammar assert's passes-but-false input is absent) | ✓ |
| P5 | `VERSION="$(HS_VERSION=… bash -c '. …/common.sh; hs_version')"` at **`:35`** and `ARCH=` at **`:36`** (the pre-verification says `:36`/`:37` — off by one; content exact) · `log`/`die` `:43–:44` · preflight `:47–:56` · `log "version=…"` `:58` (exact) | ✓ (§5 item 2) |
| P6 | `distribution/.gitignore`: `image/build/`, `deb/build/`, `**/build/`, `*.deb`, `*.tar.gz`, `*.prev`, `*.old` — the new `smoke/*.sh` is NOT ignored (porcelain shows it `??`) | ✓ |
| P7 | `README.md:117` "deterministic and self-checksumming" present; README untouched — the census carries no README line | ✓ |
| P8 | Repo public (`origin` = `https://github.com/nexsys-io/homesynapse-core.git`); majors at the marketplace via `git ls-remote --tags`: `actions/checkout` v4 · **v5** · v6 · v7 (latest `v7.0.1`) · `gradle/actions` v4 · **v5** · v6 (latest `v6.3.0`) · `actions/setup-java` v4 · **v5** (latest `v5.7.0`, no v6) · (`actions/setup-node` v5/v6/v7 and `actions/upload-artifact` v5/v6/v7 also exist — outside R-E's named list, §5 item 10). Whether `ubuntu-24.04-arm` schedules for this repository is decided by the run on the push (the QEMU fallback stays the hub's ruling). | ✓ |

**Not in P1–P8, found at the bytes (§5 item 8):** `distribution/VERSION` is a TRACKED file holding `0.1.0-skeleton`, and `_dist_dir()` resolves from the CALLER's `$0` — under the `bash -c` idiom both build scripts use, that is the cwd. CI and the bench build from the repo root, so the `git describe` path runs; from `distribution/` or `distribution/image/` as cwd the file would win and the version of record would be `0.1.0-skeleton`. Untouched (the instruction fences `:50`/`:52–:53`); flagged.

## §1 — per-file hunk summary (7 files: 6 M + 1 A)

| File | Kind | Hunks |
|---|---|---|
| `.github/workflows/install-smoke.yml` | M (+62/−7) | `on.push.paths` + `'.github/workflows/install-smoke.yml'` · job `name` → `… on a clean ${{ matrix.arch }} machine` · a 4-line teaching comment + `strategy: fail-fast: false / matrix: include: [{runner: ubuntu-latest, arch: amd64}, {runner: ubuntu-24.04-arm, arch: arm64}]` · `runs-on: ${{ matrix.runner }}` (string; the trailing comment kept) · `checkout@v5` / `setup-java@v5` / `setup-gradle@v5` · Static lint step renamed `(… + the version-grammar fixtures)` and gains `bash distribution/smoke/version-grammar-test.sh` · NEW step "Arch-truth assert (.deb Architecture == ${{ matrix.arch }})" after Assemble · NEW step "Version-grammar echo (hs_version is tag-shaped; the .deb carries it)" after it · upload `name: distribution-artifacts-${{ matrix.arch }}`. Every other step byte-identical; header lines 1–17 (the WIRING SEAM) verbatim (diff-proven against HEAD). |
| `distribution/ci/install-smoke.yml` | M | byte-identical twin (sha256 `85039248…` on both; `diff` empty post-edit). |
| `distribution/common.sh` | M (+15/−10, R-D) | `hs_version`: the `:57–:61` comment rewritten (the NEW rule, the 2026-08-22 exhibit `7c9e4fa` bare vs `0.1.0+gd26777c` wrapped, the dpkg-orders-a-bare-id-as-a-number consequence, the digit-leading-tag law); the `case` → `*.*) printf '%s'` / `*) printf '0.1.0+g%s'`. `:50` and `:52–:53` untouched; POSIX sh (`dash -n` clean); mode `100755` preserved. |
| `distribution/image/build-image.sh` | M (+16, R-D) | NEW block "── Version-of-record grammar assert (F-V1) ──" immediately after `die()` (`:44`; §5 item 3): the charset `case` (`*[!0-9A-Za-z.+~-]*\|''` → `die "… is not a Debian-safe version string"`) + `printf '%s' "${VERSION}" \| grep -Eq '^[0-9]+\.[0-9]+\.[0-9]+' \|\| die "… is not tag-shaped (expected … — hs_version must wrap bare ids as 0.1.0+g<id>)"` — the instruction's strings verbatim, outside any `$( )`, before the first use of `VERSION` (`:58`); the passes-but-false comment verbatim. |
| `distribution/smoke/version-grammar-test.sh` | A (115 lines, R-D) | §2. |
| `distribution/docs/architecture.md` | M (+80) | NEW "## The artifact channel {#artifacts}": the matrix + the one-instrument law + E1 option (c) taken · the two asserts · the artifact table (names, contents, 7-day retention) · the `if: always()` caveat (the verdict is the job, never the artifact's existence) · "Fetching an artifact for a Pi install" (`gh run list`/`gh run download -n distribution-artifacts-arm64` + the browser path; `scp` + `sha256sum` on every hop; `apt install ./…`) · "The version string (post-F-V1)" (the resolution order, the dot discriminator, the digit-leading-tag law, the Why, the one-time `--allow-downgrades` + the untagged-builds caveat). No claim language; the D-1 fences untouched. |
| `.github/workflows/ci.yml` | M (+3/−3, R-E) | `checkout@v4→v5` · `setup-java@v4→v5` · `setup-gradle@v4→v5`; the Build & Check job otherwise byte-identical (`upload-artifact@v4` kept). |

## §2 — the asserts as shipped (verbatim) + the test output

**`common.sh` — the arm:**
```sh
            case "${_v}" in
                *.*) printf '%s' "${_v}" ;;
                *)   printf '0.1.0+g%s' "${_v}" ;;
            esac
```

**`build-image.sh` — the grammar assert (after `die()`, before section 0):**
```bash
case "${VERSION}" in
    *[!0-9A-Za-z.+~-]*|'') die "version of record '${VERSION}' is not a Debian-safe version string" ;;
esac
printf '%s' "${VERSION}" | grep -Eq '^[0-9]+\.[0-9]+\.[0-9]+' \
    || die "version of record '${VERSION}' is not tag-shaped (expected ^[0-9]+\.[0-9]+\.[0-9]+ — hs_version must wrap bare ids as 0.1.0+g<id>)"
```

**The workflow — arch-truth (both twins; `${{ matrix.arch }}` is the leg's arch):**
```bash
DEB="$(ls -1t distribution/deb/build/homesynapse_*.deb | head -1)"
ACTUAL="$(dpkg-deb --field "${DEB}" Architecture)"
if [ "${ACTUAL}" != "${{ matrix.arch }}" ]; then
  echo "::error::arch-truth assert FAILED: ${DEB} carries Architecture='${ACTUAL}', this leg is '${{ matrix.arch }}'"
  exit 1
fi
echo "arch-truth assert green: ${DEB} Architecture=${ACTUAL} == matrix.arch=${{ matrix.arch }}"
```

**The workflow — version-grammar echo (the live output + the stamped field, the same regex; §5 item 4):**
```bash
V="$(bash -c '. "distribution/common.sh"; hs_version')"
echo "hs_version=${V}"
printf '%s' "${V}" | grep -Eq '^[0-9]+\.[0-9]+\.[0-9]+' \
  || { echo "::error::version of record '${V}' is not tag-shaped (expected ^[0-9]+\.[0-9]+\.[0-9]+)"; exit 1; }
DEB="$(ls -1t distribution/deb/build/homesynapse_*.deb | head -1)"
STAMPED="$(dpkg-deb --field "${DEB}" Version)"
IMAGE_STAMP="$(cat distribution/image/build/opt/homesynapse/VERSION)"
printf '%s' "${STAMPED}" | grep -Eq '^[0-9]+\.[0-9]+\.[0-9]+' \
  || { echo "::error::${DEB} carries Version='${STAMPED}', which is not tag-shaped"; exit 1; }
[ "${STAMPED}" = "${IMAGE_STAMP}" ] \
  || { echo "::error::${DEB} carries Version='${STAMPED}' but the image VERSION file says '${IMAGE_STAMP}'"; exit 1; }
[ "${STAMPED}" = "${V}" ] \
  || echo "::warning::hs_version now says '${V}' but the build stamped '${STAMPED}' — the tree changed between build and echo (a -dirty suffix?)"
echo "version-grammar echo green: ${V} (tag-shaped; .deb Version=${STAMPED}; image VERSION=${IMAGE_STAMP})"
```

**`version-grammar-test.sh` — the rig:** a stub `git` on PATH (answers `-C <dir> rev-parse` → 0 and `-C <dir> describe …` → `$FAKE_DESCRIBE`), `hs_version` run from a hermetic `mktemp` cwd that carries no `VERSION` file with `HS_VERSION=` empty, through the exact `bash -c '. common.sh; hs_version'` invocation `build-image.sh` uses — so the `case` arm is what runs (both bypasses — the env override and the VERSION file beside the caller — are disabled by construction). `COMMON_SH=<path>` drives another `common.sh` (the mutation check). Three charges: (1) seven arm fixtures · (2) the grammar regex accepts seven wrapped/tag outputs and REJECTS `7c9e4fa`/`abc`/`` + the Debian-safe charset arm mirrored (rejects `0.1.0 x`, `0.1.0+g7c9e4fa:1`, ``) · (3) the literal `grep -Eq '^[0-9]+\.[0-9]+\.[0-9]+'` is present byte-for-byte in its three carriers (`build-image.sh` + both twins). `set -uo pipefail` (every fixture runs and reports — the run-smoke idiom); exit 0/1/2.

**Output on the shipped `common.sh` (GREEN, 23/23):**
```
[version-grammar-test] common.sh=…/homesynapse-core/distribution/common.sh
[version-grammar-test] PASS  describe '7c9e4fa' -> '0.1.0+g7c9e4fa'
[version-grammar-test] PASS  describe 'd26777c' -> '0.1.0+gd26777c'
[version-grammar-test] PASS  describe '7c9e4fa-dirty' -> '0.1.0+g7c9e4fa-dirty'
[version-grammar-test] PASS  describe '1.2.3' -> '1.2.3'
[version-grammar-test] PASS  describe '1.2.3-5-gabc1234' -> '1.2.3-5-gabc1234'
[version-grammar-test] PASS  describe '1.2.3-dirty' -> '1.2.3-dirty'
[version-grammar-test] PASS  describe '' -> '0.1.0-skeleton'
[version-grammar-test] PASS  grammar accepts '0.1.0+g7c9e4fa'
[version-grammar-test] PASS  grammar accepts '0.1.0+gd26777c'
[version-grammar-test] PASS  grammar accepts '0.1.0+g7c9e4fa-dirty'
[version-grammar-test] PASS  grammar accepts '1.2.3'
[version-grammar-test] PASS  grammar accepts '1.2.3-5-gabc1234'
[version-grammar-test] PASS  grammar accepts '1.2.3-dirty'
[version-grammar-test] PASS  grammar accepts '0.1.0-skeleton'
[version-grammar-test] PASS  grammar rejects '7c9e4fa'
[version-grammar-test] PASS  grammar rejects 'abc'
[version-grammar-test] PASS  grammar rejects ''
[version-grammar-test] PASS  charset rejects '0.1.0 x'
[version-grammar-test] PASS  charset rejects '0.1.0+g7c9e4fa:1'
[version-grammar-test] PASS  charset rejects ''
[version-grammar-test] PASS  regex literal present in distribution/image/build-image.sh
[version-grammar-test] PASS  regex literal present in .github/workflows/install-smoke.yml
[version-grammar-test] PASS  regex literal present in distribution/ci/install-smoke.yml
────────────────────────────────────────────────────────
[version-grammar-test] VERSION-GRAMMAR-TEST PASSED ✓
```

**Mutation runs (arc-discipline 7 — the verdict must flip):**
- **Mutant 1 — HEAD's arm** (`COMMON_SH=<git show HEAD:distribution/common.sh>`): `FAIL describe '7c9e4fa' -> '7c9e4fa'` · `FAIL describe '7c9e4fa-dirty' -> '7c9e4fa-dirty'` · `FAILED ✗ (2 check(s) failed)`, exit 1. **Two, not three:** `d26777c` begins with `d` (a–f), so HEAD's arm wrapped it even then — the instrument corrected my own header comment, which had said "three" (§5 item 7).
- **Mutant 2 — a retyped regex in a scratch copy of the build-image carrier** (`[.]` for `\.`, the real tree untouched): `FAIL regex literal grep -Eq '^[0-9]+\.[0-9]+\.[0-9]+' missing in distribution/image/build-image.sh (copy, don't retype)` · `FAILED ✗ (1 check(s) failed)`, exit 1. (A first attempt via `sed` silently did not apply — caught because the carrier still showed the original literal; redone via Python and re-proven.)

## §3 — desk gates (this desk: Windows 11, Git Bash; no JDK/Gradle run — NONE owed, zero Java)

- **Parses:** `bash -n` over every `distribution/**/*.sh` (9 files incl. the new test) clean · `sh -n` + `dash -n` on `common.sh` (POSIX) clean.
- **The test:** GREEN 23/23 (above); the two mutants flip the verdict (above).
- **The build-image assert fragment**, extracted and run under `set -euo pipefail` with the real `die`: `'7c9e4fa'` → exit 1 "not tag-shaped" · `'0.1.0+g7c9e4fa'` / `'0.1.0+g7c9e4fa-dirty'` / `'1.2.3-5-gabc1234'` / `'0.1.0-skeleton'` → pass through · `''` / `'0.1.0 x'` / `'0.1.0+g7c9e4fa:1'` → exit 1 "not a Debian-safe version string" · `'v1.2.3'` → exit 1 "not tag-shaped" (the digit-leading-tag law holds).
- **YAML:** all three workflows parse (PyYAML 6.0.2); structural asserts GREEN — `on.push.paths` carries the workflow path; PR paths unchanged; `fail-fast` is `False`; `matrix.include` == the two `{runner, arch}` rows; `runs-on` is the STRING `${{ matrix.runner }}`; `timeout-minutes` 25; 14 steps in order (Assemble < Arch-truth < Version-grammar echo < sqlite3 prereq; Static lint < Build image); `uses` majors exactly as ruled (`checkout@v5`, `setup-java@v5`, `setup-gradle@v5`; `setup-node@v4` + `upload-artifact@v4` kept); the upload `name`/`if`/`retention-days`; `ci.yml`'s four `uses` + the `Run check` step byte-exact. (`yamllint`/`actionlint` ABSENT on this host — flagged; `shellcheck` ABSENT — flagged; CI's Static-lint step re-runs `bash -n` + the test on the push.)
- **The two step bodies**, extracted from the YAML and run in a scratch workspace with a stub `dpkg-deb` under GitHub's default `bash -eo pipefail`: (a) green path → `arch-truth assert green: … Architecture=arm64 == matrix.arch=arm64` + `version-grammar echo green: 0.1.0-skeleton (tag-shaped; .deb Version=0.1.0-skeleton; image VERSION=0.1.0-skeleton)`, exit 0 ×2 · (b) the `.deb` says `amd64` on the arm64 leg → `::error::arch-truth assert FAILED …`, exit 1 · (c) stamped `Version: 7c9e4fa` → `::error::… not tag-shaped`, exit 1 · (d) stamped ≠ image `VERSION` → `::error::…`, exit 1 · (e) live ≠ stamped with stamped == image → `::warning::… the tree changed between build and echo (a -dirty suffix?)`, exit 0 · (f) `HS_VERSION=7c9e4fa` live → `::error::version of record '7c9e4fa' is not tag-shaped`, exit 1 before any `dpkg-deb` call. (The live `hs_version` in a non-repo scratch dir resolves to the `0.1.0-skeleton` fallback, as designed.)
- **Twins:** `diff` EMPTY post-edit (sha256 `85039248069ad080…` ×2); header lines 1–17 verbatim vs HEAD; hardlinks `%h`=1 on all 7 touched files (pre- and post-edit); CR bytes 0 and a trailing newline on all 7 (`.gitattributes` LF law); `common.sh`/`build-image.sh` keep mode `100755`.
- **Marketplace:** `git ls-remote --tags` (no `gh` on this desk) — the table in P8.
- **Self-review:** no per-arch branch in any script (the arch comes only from `hs_deb_arch`); the regex literal identical in its three carriers (test-pinned); `README.md` untouched; zero `.java`, zero `build.gradle.kts`, zero `module-info`; the `-dirty` suffix survives the arm (`0.1.0+g7c9e4fa-dirty` — a valid Debian version: upstream `0.1.0+g7c9e4fa`, revision `dirty`).

**Expected arm64-leg log (H12 — derived from the 2026-08-22 Block-0 log, the artifact of record; the hub quotes the real lines from the run):** `[build-image] version=0.1.0+g<sha> arch=arm64 jdk=21` (the sha of the pushed commit, now WRAPPED — the only line that differs from Block 0's `version=7c9e4fa`) · `[build-image] bundled 55 jars` · `[build-image] jlink --add-modules java.base,java.desktop,java.instrument,java.logging,java.management,java.naming,java.net.http,java.security.jgss,java.sql,java.xml,jdk.crypto.cryptoki,jdk.crypto.ec,jdk.jfr,jdk.management,jdk.unsupported,jdk.zipfs` (16, `jdk.jfr` present, no `Warning` token) · `[build-image] jlinked runtime → 61M` · `[build-image] floor-presence assert green: all 16 requested modules present in the runtime` · `[build-image] wrote MANIFEST.sha256 (147 entries)`; then `arch-truth assert green: … Architecture=arm64 == matrix.arch=arm64` and `version-grammar echo green: 0.1.0+g<sha> (tag-shaped; .deb Version=0.1.0+g<sha>; image VERSION=0.1.0+g<sha>)`; run-smoke checks 1–9 PASS; update-smoke `derived v2=0.1.0+g<sha>+up`. The amd64 leg prints the same with `arch=amd64`. **Observe and file the arm64 leg's wall-clock** (cold Gradle + jlink on a 4-vCPU Cobalt runner; `timeout-minutes` stays 25 until measured).

## §4 — census at porcelain (lock-free: `git --no-optional-locks status --porcelain`)

```
 M .github/workflows/ci.yml
 M .github/workflows/install-smoke.yml
 M distribution/ci/install-smoke.yml
 M distribution/common.sh
 M distribution/docs/architecture.md
 M distribution/image/build-image.sh
?? distribution/smoke/version-grammar-test.sh
```
**= 7** (6 M + 1 A) — exactly the R-D-IN / R-E-IN table. `git diff --stat` (tracked): 6 files, +219/−26. Nothing else dirty; nothing committed; no attribution trailers anywhere. The new test's index mode will be `100644` when added from this Windows checkout (the R-6/R-8 helper precedent) — the workflow invokes it as `bash distribution/smoke/version-grammar-test.sh`, so CI does not depend on the bit; `git add --chmod=+x distribution/smoke/version-grammar-test.sh` is Nick's call for consistency with the other `smoke/*.sh` (all `100755`).

## §5 — deviations and pushback (evidence over instruction)

1. **[REVIEW] Baseline.** HEAD `62dbca3` ≠ `33861ad`; the census trees byte-identical (§0). Proceeded on Nick's dispatch word.
2. **[INFO] Pre-verification line numbers.** `VERSION=` is `build-image.sh:35` and `ARCH=` `:36` (P5 said `:36`/`:37`); everything else exact.
3. **[INFO] The assert's placement.** The instruction says "immediately after the `VERSION=` line"; `die()` is defined at `:44`, so an assert at `:37` would call an undefined function (exit 127 with no message). Placed as its own labeled block directly after `die()` and before "── 0. Toolchain preflight" — still outside any `$( )` and before the first use of `VERSION` (`:58`).
4. **[INFO] The version-grammar echo is tightened beyond "print and assert".** It asserts the regex on the LIVE `hs_version` output (the spec) AND on the `.deb`'s stamped `Version` (the version that ships), asserts stamped == the image's `VERSION` file (build-internal consistency — `build-image.sh` and `build-deb.sh` each compute `hs_version` independently, so a tree dirtied between them would disagree), and only WARNS when live ≠ stamped (the tree changed after the build — a `-dirty` suffix; on the runner `npm ci` + gitignored `build/`/`dist/`/`src/main/resources/dashboard/` keep it clean, so the warning is not expected). Names the dirtiness class without a false red.
5. **[INFO] The Static-lint step's name** gained "+ the version-grammar fixtures" so it stays truthful; the test is invoked through `bash` (item in §4).
6. **[INFO] Test fixtures above the pins.** The five named arm fixtures + `1.2.3-dirty` (the comment names it) + the empty-describe → `0.1.0-skeleton` fallback (pins the fallback survives the new arm); the Debian-safe charset arm mirrored with its own reject set; the three-carrier literal pin (makes "copy, don't retype" mechanical — Mutant 2 proves its boundary).
7. **[INFO] The mutation count corrected at the instrument.** HEAD's arm fails TWO fixtures (`7c9e4fa`, `7c9e4fa-dirty`), not three — `d26777c` is a–f-leading and was wrapped even at HEAD (the asymmetry F-V1 names). The test's header said "three" before the run; corrected to "the two digit-leading bare-id rows; d26777c wrapped even then". Nothing else changed.
8. **[REVIEW] Found at the bytes — `hs_version`'s VERSION-file lookup is cwd-dependent.** `_dist_dir()` is `dirname "$0"`; under `bash -c '. …/common.sh; hs_version'` (both `build-image.sh:35` and `build-deb.sh:24`) `$0` is `bash`, so it resolves to the CWD, and the lookups are `<cwd>/VERSION` and `<cwd>/../VERSION`. `distribution/VERSION` (tracked, `0.1.0-skeleton`) is therefore found only when the operator's cwd is `distribution/` or `distribution/image/`; from the repo root (CI, the Block-0 packet) the `git describe` path runs. The version of record depends on where the operator stands. Untouched — the instruction fences `:50`/`:52–:53`. Options for the hub: delete `distribution/VERSION` (the comment's "distribution/VERSION" intent has never been the CI behavior), or have both build scripts export `HS_DIST_DIR="${DIST}"` and let `_dist_dir` prefer it. The grammar assert accepts `0.1.0-skeleton` either way, so no build dies on this today.
9. **[REVIEW] TECHNICAL PUSHBACK — "exactly once" is true for the `7c9e4fa` → `0.x` transition only; `+g<sha>` builds do not order among themselves.** dpkg compares `0.1.0+g7c9e4fa` vs `0.1.0+gd26777c` segment-wise after the common `0.1.0+`: non-digit `g` vs `gd` (a prefix sorts first) ⇒ `g7c9e4fa` < `gd26777c`; the next commit's sha decides the direction at random, so moving a card between two untagged builds needs `--allow-downgrades` about half the time. Confirm on any Debian host with one command: `dpkg --compare-versions 0.1.0+g7c9e4fa lt 0.1.0+gd26777c && echo lt`. A monotone scheme along `main` — `0.1.0+git<N>.g<sha>` with `N=$(git rev-list --count HEAD)` — would order every untagged build, and `git describe` with a real tag (`1.2.3-5-gabc1234`) already carries such a counter. **Implemented as specified** (`0.1.0+g<id>`; the fixtures, the docs and the R-3/R-4 packet note all say so); the doc discloses the residual in one sentence ("the clean fix is a tag"). Contract impact of the alternative: the version-string format (consumer-visible) — the hub's call, not this lane's.
10. **[INFO] `actions/setup-node@v4` and `actions/upload-artifact@v4` kept** (outside R-E's named list); v5 majors exist for both (P8) and the same Node-20 annotation will list them on install-smoke runs — a one-line follow-up once the hub wants them, each proven by CI per the revert-on-red law.
11. **[INFO] PR paths unchanged** — the instruction adds the workflow path to `on.push.paths` only.
12. **[INFO] Docs:** the section states E1 option (c) (a native arm64 runner) is taken; `docs/escalations.md` is outside the census (§7).
13. **Disclosed — the arm64 leg's schedulability and wall-clock are unmeasured until the push**; the QEMU fallback is not authored here (the hub rules on a >10-min queue or an unavailable-label error).
14. **Disclosed — `shellcheck`, `yamllint`, `actionlint`, `gh`, `dpkg` ABSENT on this desk**; the marketplace check used `git ls-remote`, the YAML gate PyYAML + structural asserts, the step bodies a stub `dpkg-deb`.
15. **Glossary spot-check:** N/A (no Java types); names follow the distribution vocabulary already in the tree (`hs_version`, `hs_deb_arch`, `install-smoke`, `run-smoke`, `update-smoke`, `distribution-artifacts`).

## §6 — the rulings as received

- **R-D (F-V1): IN** — the arm, the grammar assert (strings verbatim), the fixture-paired test wired into Static lint, the one-time `--allow-downgrades` disclosed in the doc (the hub writes it into the R-3/R-4 packets). The residual ordering caveat: §5 item 9.
- **R-E: IN** — `actions/setup-java@v5` in all three files; `actions/checkout@v5` and `gradle/actions/setup-gradle@v5` bumped because both majors EXIST (`git ls-remote --tags`: checkout v5 `fbc6f39…`, gradle/actions v5 `4c12511…`, setup-java v5 `b6effb0…`). CI on the push is the proof; a red from a bump = revert that ONE bump, disclose, never retune blind.

## §7 — next-WU pointers (their own WUs; nothing here changed)

1. **Nick:** stage EXACTLY the 7 (`git add --chmod=+x distribution/smoke/version-grammar-test.sh` optional) → commit → push `main`. **The gate of record:** install-smoke on that push, BOTH legs green (quote the arm64 leg's six `[build-image]` lines + the two green assert lines + its wall-clock) + Build & Check green (the three R-E bumps proven). A queued-forever or unavailable-label arm64 leg = STOP, the hub rules the QEMU fallback.
2. **R-3b rides the new channel:** the CI-built `homesynapse_0.1.0+g<sha>_arm64.deb` from `distribution-artifacts-arm64` (already run-smoke'd on arm64) replaces the manual bench build; the R-3/R-4 packets carry the one-time `--allow-downgrades` for the two cards on `7c9e4fa` (and, per §5 item 9, for any later untagged move).
3. `docs/escalations.md` E1 → option (c) taken (hub-owned doc).
4. `distribution/VERSION` vs `_dist_dir` (§5 item 8) — delete or `HS_DIST_DIR`.
5. The version scheme's monotonicity (§5 item 9) — rule on `0.1.0+git<N>.g<sha>` or a first tag.
6. `setup-node`/`upload-artifact` majors (§5 item 10).
7. Optional hardening the hub may want in the Static-lint step: a `cmp` of the two twins on every push (P3 made mechanical) — not shipped, outside the charge.

## WUCP Phase 1: Coder Closeout

- [x] MODULE_CONTEXT.md: N/A — zero Java; no module touched (the instruction: "No MODULE_CONTEXT.md / module-info.java applies")
- [x] coder-handoff.md updated (the R-7 DELIVERED entry prepended)
- [x] Deferred build gate flag: **N/A-BY-DESIGN** — scripts + workflow YAML only; no gradle owed or run. The gate OF RECORD is CI on Nick's push (law 16): install-smoke BOTH legs + Build & Check
- [x] coder-lessons.md appended: the dot-discriminator / digit-leading-id version trap + the fixture rig that must defeat the function's own bypasses + the mutation count corrected at the instrument
- [x] Cross-agent note: channel RETIRED (2026-08-18) — cross-agent facts ride this return + the handoff entry
- Timestamp: 2026-08-22 (filed America/Chicago)
