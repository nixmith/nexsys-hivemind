<!--
file: context/audits/2026-08-23_R7b_version-scheme_return.md
purpose: Coder return for R-7b — the version scheme 0.1.0+git<YYYYMMDD.HHMMSS>.g<sha> (R-V), the skeleton fence, HS_DIST_DIR + the git-first order, the setup-node/upload-artifact majors, riders i/j/k, E1.
audience: hub (audit precedes any commit), Nick (the commit; the CI read)
instruction: context/instructions/2026-08-22_R7b_version-scheme_distribution-micro-WU_coding-instruction.md
status: DELIVERED at the bytes; nothing committed, nothing staged. CI on Nick's push = the gate of record (law 16).
-->

# R-7b return — version scheme (distribution-only) · 2026-08-23

**Baseline:** core `e845cd9` (the R-9 landing commit — the instruction's alternate baseline; tree clean at launch). Every STOP gate verified at content: `common.sh` arms + no `HS_DIST_DIR` · `distribution/VERSION` = `0.1.0-skeleton\n` 15 B · both captures without `HS_DIST_DIR` · twins byte-identical, `@v4` ×2, no fence · unit `:31 LogDirectory=` · boot-contract-map pre-R-9 text · rig 23 checks. **Line numbers in `common.sh` shifted +1 vs the instruction** (R-9's health block at `:40–:45`): the version block was `:47–:76`, `_dist_dir` `:49`, the file-before-git consult `:53` — gated CONTENT identical everywhere, report-and-proceed exercised. All rulings executed: **R-V · R-7b-1 STANDS · R-7b-2 IN · riders i/j/k IN.**

## §1 Census — exactly 11 M, 0 A, 0 D (porcelain, lock-free)

| File | +/− | What |
|---|---|---|
| `distribution/common.sh` | +34/−13 | (a) the arm: non-tag describe → `_cd="$(TZ=UTC git -C "${_d}" log -1 --format=%cd --date=format-local:%Y%m%d.%H%M%S 2>/dev/null \|\| true)"`, POSIX 8-then-6-digit `case` → `0.1.0+git<cd>.g<sha>`; `*)` → `printf ''` (fail-closed; the `\|\| true` is deviation D3). (b) `_dist_dir` honours `HS_DIST_DIR` first; resolution order now env → **git** → `VERSION` → `../VERSION` → skeleton; header + arm comment rewritten (scheme, why it orders, the audit path cited in-file). |
| `distribution/image/build-image.sh` | +12/−9 | (c) `:35` capture gains `HS_DIST_DIR="${DIST}"`; the passes-but-false comment now names the **skeleton fallback** (fenced in CI by the twins' echo step; the tag is a hypothetical); the `:47` header + `:63` die-message tail read `0.1.0+git<date>.g<id>` (D5). Regex literal untouched. |
| `distribution/deb/build-deb.sh` | +1/−1 | (c) `:24` capture gains `HS_DIST_DIR="${DIST}"` — nothing else. |
| `distribution/ci/install-smoke.yml` + `.github/workflows/install-smoke.yml` | +26/−6 ×2 | (d0) `LTD-10` → `LTD-01` in the corretto comment. (d1) `setup-node@v5` + `upload-artifact@v5`. (d2) echo step: `V="$(HS_DIST_DIR=distribution bash -c …)"`; the skeleton fence `[ "${V}" != "0.1.0-skeleton" ]` AFTER the grammar assert with `::error::… never lawful in CI (actions/checkout leaves .git)`; green line extended: `(scheme 0.1.0+git<YYYYMMDD.HHMMSS>.g<sha>; .deb Version=…; image VERSION=…; sha256 <64-hex>  <deb-basename>)`. (k) Static lint: `command -v systemd-analyze` hard guard → `systemd-analyze --man=no verify … 2>&1 \| tee /tmp/unit-verify.log` → `if grep -q 'Unknown key name' … exit 1` → `unit directives verified` (**the `! grep` form is vacuous under `set -e` — deviation D2, proven below**). `timeout-minutes: 25` untouched. Edited the `distribution/ci` twin, copied, `cmp` exit 0; sha256 `cd83543a…` ×2; nlink=1 ×2. |
| `.github/workflows/ci.yml` | +1/−1 | (e) `upload-artifact@v4` → `@v5` (the Upload test reports step; R-7b-2). |
| `distribution/smoke/version-grammar-test.sh` | +102/−43 | (f) stub git gains `log)` (prints `FAKE_CDATE`) + `FAKE_NOGIT=1` (`rev-parse`→1, `describe` silent); `run_hs_version(describe, cdate)` passes `HS_DIST_DIR="${WORK}/tree/cwd"` (the hermetic cwd itself — the mutation isolates the ORDER, not the dir); arm rows 7 → **10** (three `+git` shapes; `7c9e4fa`+empty-cdate → `''`; VERSION-bypass row — planted skeleton loses to git; `FAKE_NOGIT` + planted `1.2.3` wins — the tarball carrier); accept 7 → **9** (both `+git` shapes; legacy rows retained); **§2b NEW** — 4 `dpkg --compare-versions` ordering rows or ONE explicit SKIP line; carriers 3 → **5** (+ the fence literal per twin); header + count line rewritten; verdict prints the check count and asserts `ran == expected` (30/34 by dpkg presence — a silently-unrun row flips the verdict). Mode 100755 unchanged. |
| `distribution/docs/architecture.md` | +35/−16 | (g) "The version string (post-R-V)": the git-first order + `HS_DIST_DIR`; the scheme with the UTC committer-date invocation; fail-closed `''`; the fence; the ordering argument (prefix, monotone-by-committer-time, depth-free, reproducible) with the F-V1/H-2 history; `:135–:137` RETIRED — "tags begin at the first release … a tag at HEAD would sort BELOW every `0.1.0+…`"; "exactly once … no later install needs the flag". No claim language. |
| `distribution/systemd/homesynapse.service` | +1/−1 | (i) `:31` `LogDirectory=` → `LogsDirectory=` — the one token; nothing else. |
| `distribution/docs/boot-contract-map.md` | +23/−13 | (j) "Health / readiness" rewritten to the shipped posture: the loopback-only `GET`/`HEAD /health` exemption (R-H1), 200 ⇔ LIVE, the unit's `ExecStartPost … --health-path /health` reading no token, check 3 keeps the authed probe BY NAME, **E3 CLOSED at R-9** (return path cited); item 2: the M13 block is a **DANGER note, not a staged flip** (OR-M13-SDNOTIFY HELD; R10-IN-L). |
| `distribution/docs/escalations.md` | +2/−0 | (h) E1: `**(c) taken at R-7 (2026-08-22):** ubuntu-24.04-arm, GitHub-hosted, free for public repos; first arm64 leg 3m01s wall-clock (install-smoke #33).` appended to the E1 block (placement note D6). E3 untouched. |

## §2 The lane's gates (this desk: Windows 11; Git Bash 5.2.26 + msys dash; WSL Ubuntu-24.04 — dash, dpkg 1.22.6, systemd 255)

- **Red-first** (rig extended BEFORE any implementation, run against the untouched tree): `FAILED ✗ (7 of 30)` — the 5 arm/order rows + both fence rows; everything else green. Predicted and got.
- `bash -n` over every `distribution/**/*.sh` (the CI lint loop, verbatim) → `all shell scripts parsed clean`; `sh -n` + `dash -n` (msys) on `common.sh` clean.
- **The test, WSL (dpkg present), whole:**

```text
[version-grammar-test] common.sh=/mnt/c/…/homesynapse-core/distribution/common.sh
PASS  describe '7c9e4fa' cdate '20260822.143100' -> '0.1.0+git20260822.143100.g7c9e4fa'
PASS  describe 'd26777c' cdate '20260822.143100' -> '0.1.0+git20260822.143100.gd26777c'
PASS  describe '7c9e4fa-dirty' cdate '20260822.143100' -> '0.1.0+git20260822.143100.g7c9e4fa-dirty'
PASS  describe '1.2.3' … -> '1.2.3'   ·  PASS '1.2.3-5-gabc1234'  ·  PASS '1.2.3-dirty'
PASS  describe '' cdate '20260822.143100' -> '0.1.0-skeleton'
PASS  describe '7c9e4fa' cdate '' -> ''
PASS  describe '7c9e4fa' cdate '20260822.143100' -> '0.1.0+git20260822.143100.g7c9e4fa' [cwd/VERSION=0.1.0-skeleton planted]
PASS  describe '' cdate '' -> '1.2.3' [FAKE_NOGIT=1, cwd/VERSION=1.2.3 planted]
PASS  grammar accepts ×9 ('0.1.0+git….g7c9e4fa', '…-dirty', the three legacy +g shapes, '1.2.3', '1.2.3-5-gabc1234', '1.2.3-dirty', '0.1.0-skeleton')
PASS  grammar rejects '7c9e4fa' · 'abc' · ''      PASS  charset rejects '0.1.0 x' · '0.1.0+g7c9e4fa:1' · ''
PASS  dpkg orders '0.1.0+git20260822.143100.g7c9e4fa' gt '0.1.0+g7c9e4fa'
PASS  dpkg orders '0.1.0+git20260822.143100.g7c9e4fa' gt '0.1.0+gd26777c'
PASS  dpkg orders '0.1.0+git20260822.143100.g1111111' gt '0.1.0+git20260822.143059.gffffffff'
PASS  dpkg orders '7c9e4fa' gt '0.1.0+git20260822.143100.g7c9e4fa'
PASS  regex literal present ×3      PASS  skeleton fence present ×2
[version-grammar-test] VERSION-GRAMMAR-TEST PASSED ✓  (34 checks)          (exit 0)
```

  Git Bash (no dpkg): `SKIP  ordering rows (no dpkg on this host)` (one line) + `PASSED ✓  (30 checks)`. Extra rows the hub verified, re-proven at dpkg 1.22.6: `<V>+up gt <V>` (update-smoke's `V2`) and `<V>-dirty gt <V>` — both TRUE.
- **Mutation run** (`git show HEAD:distribution/common.sh` → a regular file; `COMMON_SH=… bash distribution/smoke/version-grammar-test.sh`): **FAILED exactly 5** — `describe '7c9e4fa'` / `'d26777c'` / `'7c9e4fa-dirty'` (each `-> '0.1.0+g…'`, expected `+git…`), `describe '7c9e4fa' cdate '' -> '0.1.0+g7c9e4fa'` (expected `''`), and the `[cwd/VERSION=0.1.0-skeleton planted]` row (`-> '0.1.0-skeleton'` — the file wins on HEAD). The hub's derivation of 5, row-for-row. Verdict: `FAILED ✗ (5 of 30 check(s) failed)`, exit 1.
- **`hs_version` proofs** (the live tree, dirty from this WU — the `-dirty` proof for free; committer date of `e845cd9` under TZ=UTC = `20260823.164515`): repo root `HS_DIST_DIR=distribution {bash,sh,dash} -c '. distribution/common.sh; hs_version'` → `0.1.0+git20260823.164515.ge845cd9-dirty` ×3 · from `distribution/` as cwd, with AND without `HS_DIST_DIR` → the same value (the cwd accident is closed at the function, not just at the callers) · WSL dash → same · plain `dash -c '. distribution/common.sh; hs_version'` from root (no env) → same.
- **Unit (i/k), systemd 255:** fixed unit → zero `Unknown key name` lines, fragment verdict `unit directives verified`; **mutation flip:** HEAD's unit through the same fragment → `unit.old.service:31: Unknown key name 'LogDirectory' in section 'Service', ignoring.` → step FAILS. ("marked executable/world-writable" warnings in the WSL transcript are DrvFs mount artifacts; the file is 100644 in the index — the runner's checkout won't show them. The "Command … is not executable" lines appeared and did not fail the step, as designed.)
- **Twins:** `cmp` exit 0, sha256 `cd83543a…` ×2, nlink=1. **PyYAML structural asserts** on all three workflows: 25/25 PASS (14 steps in order; matrix/fail-fast/runs-on/timeout/on.push.paths byte-stable; the five majors as ruled; the lint + echo fragments present; the fence sits between the grammar assert and the `.deb` read; regex literal exactly twice in the echo step — V + STAMPED, as at HEAD; `ci.yml` trio unchanged + `@v5`).
- **Echo-step body ×8 arms** (the step extracted from the twin via PyYAML — never retyped — under `bash -e` with stub `dpkg-deb`/fake tree): green all-match (prints scheme + `sha256 <hex>  <deb>`) · skeleton V → fence exit 1 · bare/empty live V → exit 1 · bare stamped → exit 1 · stamped≠image → exit 1 · live≠stamped → `::warning::` exit 0. 8/8.
- **The `git log`-fails arm:** a stub git whose `log` exits 1 → `hs_version` prints `''`, exit 0 → build-image dies at the charset arm with its message (never a bare abort, never `0.1.0+g<sha>`). Assert fragment ×6 inputs: both `+git` shapes pass · skeleton passes (CI-fenced downstream) · `1.2.3` passes · `7c9e4fa` dies "not tag-shaped" · `''` dies "not a Debian-safe version string".
- **`ls-remote` (verify-before-bump, both majors):** `a0853c24544627f65ddf259abe73b1d18a591444 refs/tags/v5` (actions/setup-node) · `330a01c490aca151604b8cf639adc76d48f6c5d4 refs/tags/v5` (actions/upload-artifact).
- Census 11 M at porcelain; CR=0, trailing LF, `i/lf w/lf` ×11; nothing committed, nothing staged.

## §3 Deviations and pushback (evidence over instruction)

1. **[REVIEW] `upload-artifact@v5` still runs on Node 20 — H-4's "the Node-20 annotation clears" does NOT fully hold at v5.** Evidence: `action.yml` at `refs/tags/v5` (= v5.0.0, the only v5 tag, `330a01c4…`) declares `runs.using: 'node20'`; the v6.0.0 release note states it plainly — "v5 had preliminary support for Node.js 24, however this action was by default still running on Node.js 20. Now this action by default will run on Node.js 24" (v6.0.0, 2025-12-12, tag `b7c566a7…`, `using: 'node24'`, input list byte-identical to v5's: name/path/if-no-files-found/retention-days/compression-level/overwrite/include-hidden-files). `setup-node@v5` IS `node24` — that annotation clears. **The RULED `@v5` is implemented as written** (three files). Consequence for §6: the run will still carry ONE forced-to-Node-24 annotation (upload-artifact) — "zero Node-20 annotations" holds only at `@v6`. If Nick/hub take the pushback pre-commit, the flip is one token ×3 files: `git grep -l 'upload-artifact@v5' \| xargs sed -i 's/upload-artifact@v5/upload-artifact@v6/'` (then re-copy + `cmp` the twins — or I execute it on one word). v7 exists (ESM + an `archive` input; not needed).
2. **[REVIEW] Rider (k)'s literal fragment is a vacuous gate; shipped the `if` form.** `! grep -q 'Unknown key name' …` followed by the echo: bash ignores `set -e` for a `!`-inverted command, so the step CANNOT fail on a match (proven: `bash -e` with the string present → exit 0). Shipped: `if grep -q … then ::error…; exit 1; fi` + a `command -v systemd-analyze` hard guard (an absent verb would otherwise read as success — arc-17). Behavioral contract unchanged (fail on unknown directive — now actually enforced); mutation-verified both ways (HEAD's unit red at `:31`, fixed unit green).
3. **[INFO] `\|\| true` added inside the `_cd` capture.** Under `set -eu` a `git log` that FAILS (vs prints nothing) inside `$( )` aborts the sourced shell — a bare non-zero exit with no message, upstream of the die. `\|\| true` routes that arm to the same fail-closed `''` → build-image's message. Happy path unchanged; proven with a log-exits-1 stub.
4. **[INFO]** `build-deb.sh:24` does not pass `HS_VERSION="${HS_VERSION:-}"` (pre-existing asymmetry with `build-image.sh:35`; only an exported `HS_VERSION` reaches it). Untouched — outside the hunk.
5. **[INFO]** `build-image.sh:47` + the `:63` die-message tail updated `0.1.0+g<id>` → `0.1.0+git<date>.g<id>` (comment/message truth; the regex literal and both assert conditions byte-unchanged). Also FOUND, not edited: `build-image.sh:72` "(reproducibility/LTD-10)" on the JDK-21 check is the same LTD-01/LTD-10 mis-attribution rider (d0) fixed in the twins — one token, hub's call.
6. **[INFO]** E1's resolution line is APPENDED at the end of the E1 block (the instruction's "append", exact text); E3's house style puts `**Status: …**` directly under the heading — say the word and I move it.
7. **[INFO]** "The expected-count line": implemented as the header's `Checks: 34 with dpkg … 30 + one SKIP without` plus a verdict-integrity assert (`ran == expected` by dpkg presence; a silently-unrun row flips the verdict to FAILED).

NO BLOCKING DEVIATIONS.

## §4 CI predictions (H12 — the instruction's §6, corrected by §3.1)

Build & Check GREEN ~3 min, zero Java delta (rest-api 147 · lifecycle 62 · app 24); `upload-artifact@v5` uploads (inputs verified present at v5). install-smoke BOTH legs GREEN (~2m45s / ~3m00s); Static lint prints the CI lint line, **34 PASS rows + `VERSION-GRAMMAR-TEST PASSED ✓  (34 checks)`** (ubuntu runners have dpkg), then `unit directives verified`; the echo step prints `hs_version=0.1.0+git<cd-of-the-pushed-commit>.g<sha>` and the green line with the scheme name + `sha256 <hex>  homesynapse_0.1.0+git<date>.g<sha>_<arch>.deb`; **19** `[smoke] PASS` lines/leg (R-9 landed first); update-smoke GREEN (`V2 = <ver>+up` — `+up gt` base proven at dpkg here); artifacts `distribution-artifacts-{amd64,arm64}`. **Node-20 annotations: ONE remains (upload-artifact\@v5, `using: node20`) — zero only if the §3.1 flip to `@v6` is taken.** Plausible REDs unchanged from the instruction (an upload-artifact\@v5 input rename is now ~excluded — inputs diffed; a dash-incompatibility ~excluded — the arm ran under msys dash + WSL dash).

## §5 Next (refuse-to-close)

Hub audit on this return (incl. the §3.1 ruling: `@v5` stands vs the one-token `@v6`) → Nick commits the 11 M → **CI on that push = the gate of record** → R-3b (the packet rides `distribution-artifacts-arm64`, now hash-verifiable from the run log; the one-time `--allow-downgrades` on the two `7c9e4fa` cards; first block = the artifact-absent restart proof). Fenced out per §3, untouched: tags, the packets' downgrade line, `README.md:117`, E3/R-9 files, `timeout-minutes`, Java.
