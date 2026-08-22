<!--
file: context/instructions/2026-08-22_R7_arm64-artifact-channel_coding-instruction.md
purpose: R-7 / W2-1 — THE ARM64 ARTIFACT CHANNEL (S-10 Tier 2: "the distribution moat's highest-leverage item; unblocks any external installer story; the H3 rep is its acceptance template") PULLED FORWARD at v55 beat 4 because every gate it needs is already satisfied (no bench, no hardware; CI is its own gate of record) and the Block-0 build of 2026-08-22 just proved why it matters: the only way to produce an installable arm64 `.deb` today is a manual build on the bench card. After this WU, every push that touches `distribution/**` produces BOTH a clean-machine-smoked amd64 artifact AND a clean-machine-smoked arm64 artifact as CI artifacts — the same `run-smoke.sh` on a second architecture (H13: one instrument, two rigs), and R-9's install-rehearsal cadence gains an artifact source. Two packaging riders found at the instrument ride with it: F-V1 (the `hs_version` bare-id arm — an apt-downgrade trap) and the CI action-deprecation annotations observed on run #214.
audience: the R-7 Coder lane (host-side Claude Code per D12 — shell + YAML only; NO gradle loop needed; `bash -n` + the CI runs on the push are the gates) + Nick (the dispatch word + the commit + the CI verdict paste — or the hub reads it at the run page).
status: ISSUE-READY (v55 beat 4). Baseline: core `33861ad` (verify at launch; porcelain clean). SEQUENCING: never concurrently with another host-CC lane on the same checkout (R-6/R-8 is the other ISSUE-READY core WU — run them one after the other, either order; the hub recommends R-7 FIRST: smaller, faster, and it hands R-3b a CI-built arm64 artifact).
return: nexsys-hivemind/context/audits/<filing-date>_R7_arm64-artifact-channel_return.md (filing-day dated, America/Chicago). The lane commits NOTHING — the hub audits, Nick commits; the install-smoke run on the push (BOTH matrix legs) is the gate of record (law 16).
dispatch: "Read nexsys-hivemind/context/instructions/2026-08-22_R7_arm64-artifact-channel_coding-instruction.md and execute it. - /nexsys-coder"
pre-verification: context/pre-verifications/WU-R7.md (P1–P8) — READ FIRST; any mismatch is a STOP-and-flag.
rulings embedded (H10; unre-worded rows stand as RECOMMENDED at dispatch): R-D the F-V1 version-scheme fix — IN (recommended; one-time `--allow-downgrades` on our two internal cards, written into the R-3/R-4 packets by the hub) / OUT · R-E the action-major bumps (setup-java@v5; checkout/setup-gradle if a v5 exists) — IN (recommended; CI proves them) / OUT.
-->

# Coding Task: R-7 / W2-1 — the arm64 artifact channel (+ F-V1 + the action-deprecation rider)

**Subsystem:** distribution + CI (`.github/workflows/`, `distribution/ci/`, `distribution/common.sh`, `distribution/image/build-image.sh`, `distribution/docs/`). **Design Docs:** Doc 12 (boot contract / packaging), the distribution skeleton lane return (2026-06-26), the H3 Stage-1/Stage-2 returns (the install-rehearsal evidence class R-9). **Phase:** 3-Implementation (scripts + workflow YAML; zero Java). **Task brief reference:** S-10 §1 R-7 (W2-1), pulled forward v55 beat 4.

## What this implements (the engineering why)

`install-smoke.yml` builds the image + `.deb` on `ubuntu-latest` (amd64), installs it on that clean runner, runs the nine smoke checks and update-smoke, and uploads `homesynapse_<ver>_amd64.deb` + the tarball. The product runs on a Raspberry Pi 5 (arm64). Today the arm64 artifact exists only when an operator builds it by hand on the bench card (Block 0, 2026-08-22 04:18 Pi-time: `build-image.sh` + `build-deb.sh`, ~2 min, then `scp` through the desktop to the held card). **This WU makes the install-smoke job a two-architecture MATRIX** — `ubuntu-latest` (amd64, unchanged) and `ubuntu-24.04-arm` (arm64; GitHub-hosted, free for public repositories — this repository is public: its Actions pages render without a login) — so every push touching `distribution/**` yields an arm64 `.deb` that has ALREADY passed run-smoke checks 1–9 + update-smoke on a clean arm64 machine. `hs_deb_arch` (`common.sh` :75–:85) derives the arch from `dpkg --print-architecture` on the runner, so the scripts need no arch parameter; Corretto 21 and Node 22 ship aarch64 builds; sqlite-jdbc's aarch64 native is the one the Pi already runs.

**Rider F-V1 (found at the instrument — the Block-0 build printed `version=7c9e4fa`):** `hs_version` (`common.sh` :49–:70) wraps a bare `git describe --always` id as `0.1.0+g<id>` ONLY when the id begins a–f (`:62–:65`: `[0-9]*) printf '%s' "${_v}"` — the arm meant for TAG-shaped versions catches digit-leading shas). Consequence: dpkg orders `7c9e4fa` ABOVE `0.1.0+gd26777c`, and the NEXT a–f-leading id (`0.1.0+ga…`) sorts BELOW `7c9e4fa` → `apt install` refuses it as a downgrade. The fix makes the wrapper unconditional for bare ids and adds a GRAMMAR ASSERT at the capture site (H12): a version of record always matches `^[0-9]+\.[0-9]+\.[0-9]+` (tag-shaped upstream), or build-image dies naming the bad string. **One-time cost, disclosed:** our two internal cards that carry `7c9e4fa` will need `--allow-downgrades` exactly once (the hub writes it into the R-3/R-4 packets); no external install exists yet, so the scheme is corrected before it can bite anyone else.

**Rider R-E (observed at CI run #214 on `33861ad`):** "Node.js 20 is deprecated … actions/checkout@v4, actions/setup-java@v4, gradle/actions/setup-gradle@v4 … forced to run on Node.js 24" and "setup-java v4 is deprecated … migrate to actions/setup-java@v5". Bump `actions/setup-java` to `@v5` in all three workflow files (ci.yml, install-smoke.yml, the twin); bump `actions/checkout` and `gradle/actions/setup-gradle` to `@v5` ONLY if those majors exist on the marketplace at execution (verify; if absent, leave at v4 and say so in the return). CI green on the push is the proof; a red from a bump = revert that one bump, disclose, never retune blind.

## Files to read before starting

| File | Why |
|---|---|
| `context/pre-verifications/WU-R7.md` | THE GATE — P1–P8 at your checkout |
| `.github/workflows/install-smoke.yml` WHOLE + `distribution/ci/install-smoke.yml` (the twin; byte-identical at `33861ad` — P3) | the job you matrix-ify; the WIRING-SEAM header stays verbatim in both |
| `.github/workflows/ci.yml` WHOLE | the R-E bumps (setup-java@v5) + the Build & Check job you must NOT otherwise touch |
| `distribution/common.sh` :47–:86 | `hs_version` (the F-V1 arm at :62–:65) and `hs_deb_arch` (:75–:85) |
| `distribution/image/build-image.sh` :36–:60 | `VERSION="$(…hs_version)"` + the toolchain preflight — where the grammar assert lands (after the `VERSION=` line, before any use) |
| `distribution/deb/build-deb.sh` :24–:30 | `VERSION`/`ARCH` → the `.deb` filename |
| `distribution/smoke/run-smoke.sh` + `distribution/update/update-smoke.sh` | unchanged — they run on both legs; read them so the matrix step names stay truthful |
| `distribution/.gitignore` | `image/build/`, `deb/build/`, `*.deb`, `*.tar.gz` ignored — artifacts never enter the tree |
| `distribution/docs/architecture.md` | the doc that gains the artifact-channel section (README.md is FENCED — P7) |
| `distribution/README.md` | READ-ONLY; line 117 is claim-fenced until W2-3; this WU touches NOTHING in it |
| the H3 Stage-2 return `nexsys-hivemind/context/audits/2026-08-09_H3-clean-image_fresh-install_operator-return.md` §9.2–§9.5 | the evidence class the arm64 leg serves (F-24: "the hardened unit has never executed outside GitHub's amd64 Ubuntu runner" — after this WU it executes on an arm64 runner on every push) |

No `MODULE_CONTEXT.md` / `module-info.java` applies (zero Java).

## Files to create or modify

### A. The matrix (`.github/workflows/install-smoke.yml` M + `distribution/ci/install-smoke.yml` M — edit BOTH identically; hardlink pre-check `stat -c %h` first, env-model §12; `diff` them before and after)

- `jobs.install-smoke` gains `strategy: { fail-fast: false, matrix: { include: [ { runner: ubuntu-latest, arch: amd64 }, { runner: ubuntu-24.04-arm, arch: arm64 } ] } }`, `runs-on: ${{ matrix.runner }}`, `name: Build image + .deb, install-smoke on a clean ${{ matrix.arch }} machine`. `fail-fast: false` so one leg's red never hides the other's verdict (law 16 banks each leg).
- The artifact upload step: `name: distribution-artifacts-${{ matrix.arch }}` (two distinct artifacts per run; the amd64 name changes from `distribution-artifacts` — disclose it).
- A new step after "Assemble .deb", both legs: **the arch-truth assert** — `dpkg-deb --field "$(ls -1t distribution/deb/build/homesynapse_*.deb | head -1)" Architecture` must print exactly `${{ matrix.arch }}`, else exit 1 naming both strings (passes-but-false comment: an amd64 jlink image packaged under an arm64 label would pass every later check on the same runner — the field is the cheapest honest discriminator; the runtime probe downstream is the second).
- A new step after the arch assert: **the version-grammar echo** — print `hs_version`'s output and assert `^[0-9]+\.[0-9]+\.[0-9]+` (same regex as build-image's assert; H13 byte-identical in both rigs).
- Keep every existing step byte-identical otherwise (static lint, build, assemble, sqlite3 prereq, run-smoke, update-smoke, journal capture). `timeout-minutes` stays 25 (observe the arm64 leg's time in the return; raise only with the measurement).
- `on.push.paths` gains `.github/workflows/install-smoke.yml` so a workflow edit re-runs the gate on itself.

### B. F-V1 (`distribution/common.sh` M; `distribution/image/build-image.sh` M) — **RULING R-D: IN (recommended) / OUT**

- `hs_version`: replace the `case` at :62–:65 with one that wraps EVERY non-tag-shaped describe output: `case "${_v}" in *.*) printf '%s' "${_v}" ;; *) printf '0.1.0+g%s' "${_v}" ;; esac` — a tag-shaped describe (`1.2.3`, `1.2.3-5-gabc1234`, `1.2.3-dirty`) always contains a dot; a bare commit id (with or without `-dirty`) never does. Rewrite the :57–:61 comment to describe the NEW rule and name the 2026-08-22 exhibit (`7c9e4fa` printed bare; `0.1.0+gd26777c` wrapped — the a–f-only asymmetry). Keep the `HS_VERSION` env override (:50) and the `VERSION` file lookups (:52–:53) untouched.
- `build-image.sh`: immediately after the `VERSION=` line (:36), the grammar assert: `case "${VERSION}" in *[!0-9A-Za-z.+~-]*|'') die "version of record '${VERSION}' is not a Debian-safe version string" ;; esac; printf '%s' "${VERSION}" | grep -Eq '^[0-9]+\.[0-9]+\.[0-9]+' || die "version of record '${VERSION}' is not tag-shaped (expected ^[0-9]+\.[0-9]+\.[0-9]+ — hs_version must wrap bare ids as 0.1.0+g<id>)"` with a three-line teaching comment (the F-V1 mechanism + the downgrade consequence). `# passes-but-false input: a tag named like a version but semantically wrong (e.g. an old tag reachable from HEAD) — bounded by the repo carrying no tags today and by the R-9 install-rehearsal cadence.`
- A `bash` fixture test is OWED for this function (arc-discipline 10: every new assert ships with fixtures proving its PASS and its false-verdict boundary): `distribution/smoke/version-grammar-test.sh` (A) — runs `hs_version` under `HS_VERSION=` overrides for `7c9e4fa` (expect `0.1.0+g7c9e4fa`), `d26777c` (expect `0.1.0+gd26777c`), `7c9e4fa-dirty` (expect `0.1.0+g7c9e4fa-dirty`), `1.2.3` (expect `1.2.3`), `1.2.3-5-gabc1234` (expect itself) — NOTE: `HS_VERSION` bypasses the case arm (:50 returns it verbatim), so the test must exercise the arm through a FAKE `git describe` (a stub `git` on PATH in a temp dir, or a function override after sourcing) — design it so the arm itself is what runs; then assert the build-image grammar regex accepts the five wrapped/tag outputs and REJECTS `7c9e4fa`/`abc`/`` (the false-verdict boundary). Wire it into the workflow's "Static lint" step (both twins) so CI runs it on every push.

### C. Docs (`distribution/docs/architecture.md` M) — one section "The artifact channel": what CI produces per push (two artifacts, names, retention), how to fetch an artifact for a Pi install (the `gh run download` idiom AND the browser path — `gh` is absent on the Pi; download on the desktop, `scp` to the Pi, `sha256sum` on every hop — the card-sitting packet's idiom), the version-string rule post-F-V1, and the one-time `--allow-downgrades` note for cards carrying a bare-id version. No claim language: the artifact channel is a BUILD fact; the D-1 fences stand verbatim; `README.md` untouched.

### D. R-E (`.github/workflows/ci.yml` M + the two install-smoke twins, already M) — **RULING R-E: IN (recommended) / OUT**: `actions/setup-java@v4` → `@v5` in all three; `actions/checkout` / `gradle/actions/setup-gradle` → `@v5` only if the major exists (verify at the marketplace at execution; disclose per action).

## Technical specification — contracts

- **Both legs run the SAME scripts byte-for-byte; only the runner differs.** Any per-arch branch in a script is a defect (the arch comes from `hs_deb_arch`'s `dpkg --print-architecture`).
- **The amd64 leg's behavior is unchanged** except the artifact name; its nine checks + update-smoke remain the gate of record for the amd64 path; the arm64 leg becomes the gate of record for the arm64 path from this WU on.
- **The arch-truth assert and the version-grammar assert are in-workflow PLUS in-script** (the grammar assert lives in `build-image.sh`; the workflow echoes it) — one instrument, two rigs.
- **Zero Java; zero `build.gradle.kts`; zero README.** The R-3 systemd-unit seam is untouched (R-3b owns it).

## Verification (the lane's gates, then CI)

`bash -n` on every touched `.sh` · `shellcheck` if present (flag if absent) · run `distribution/smoke/version-grammar-test.sh` locally (must pass; show its output) · `diff` the twins (byte-identical) · `yamllint`/`actionlint` if present (flag if absent) · the census exactly as the table. **CI on the push = the gate of record: BOTH install-smoke legs green + Build & Check green**; the arm64 leg's log carries the same six `[build-image]` lines Block 0 printed on the Pi, with `arch=arm64` and the 16-module `--add-modules` line — quote them in the return (H12: expected values derived from the 2026-08-22 Block-0 log, which is the artifact). If `ubuntu-24.04-arm` is not schedulable for this repository (the job sits "queued" >10 min or errors with an unavailable-label message), STOP and flag: the fallback is a QEMU job (`docker/setup-qemu-action` + an `arm64v8/ubuntu` container) — NOT authored here; the hub rules.

## Files table (census-exact)

| File | Kind |
|---|---|
| `.github/workflows/install-smoke.yml` | M |
| `distribution/ci/install-smoke.yml` | M |
| `distribution/common.sh` | M (R-D) |
| `distribution/image/build-image.sh` | M (R-D) |
| `distribution/smoke/version-grammar-test.sh` | A (R-D) |
| `distribution/docs/architecture.md` | M |
| `.github/workflows/ci.yml` | M (R-E) |

**Stages exactly 7 (R-D IN, R-E IN) / 4 (R-D OUT, R-E IN: drop the three R-D rows) / 6 (R-D IN, R-E OUT: drop ci.yml) / 3 (both OUT).** Anything else dirty = STOP.

## What to watch out for

The twins' WIRING-SEAM header comment stays verbatim · hardlink pre-check on all touched files (env-model §12) · `fail-fast: false` is load-bearing · matrix `include` keeps `runs-on` a string (no array) · the artifact-name change is a consumer-visible change (disclose; nothing consumes it yet) · `hs_version`'s `--dirty` suffix must survive the new arm (`0.1.0+g7c9e4fa-dirty` is a valid Debian version) · the grammar regex is identical in the script and the workflow (copy, don't retype) · `HS_VERSION` override bypasses the arm — the test must drive the arm through a stubbed `git` · `set -euo pipefail` in build-image: a `die` inside `$( )` command substitution does not abort the script — place the assert OUTSIDE any substitution · `ubuntu-24.04-arm` runners have no `sqlite3` preinstalled either — the existing prereq step covers it · never touch `README.md` (:117 fence) · no attribution trailers; the lane commits nothing.

## Return shape

§0 P1–P8 · §1 per-file diffs (hunk summary) · §2 the asserts as shipped (verbatim) + the version-grammar test output · §3 desk gates · §4 census at porcelain (flag spelled) · §5 deviations/pushback · §6 the R-D/R-E words as received · §7 next-WU pointer (R-6/R-8 if not yet run; else the R-3b rebuild rides the new channel). Welcome technical pushback — if the bytes contradict this instruction, your flag is the deliverable.
