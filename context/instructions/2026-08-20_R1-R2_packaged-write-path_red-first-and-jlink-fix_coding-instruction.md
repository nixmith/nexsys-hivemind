<!--
file: context/instructions/2026-08-20_R1-R2_packaged-write-path_red-first-and-jlink-fix_coding-instruction.md
purpose: THE SEMESTER ANCHOR — R-1 (the packaged-runtime write-path assert, red-first) + R-2 (the jlink fix in the ruled subsuming form: full-lib jdeps + the build-time FLOOR-presence assert). Closes F-23's product gap the measured-then-green way (H7): the surface gets its instrument FIRST, watched RED on the real broken artifact (the held card), then the fix turns it green. R-4's fence lift (the two D-1 DO-NOT-SAY items) depends on this WU's chain completing through R-3/R-4 — nothing in THIS WU lifts any claim.
audience: the R-1/R-2 Coder lane (host-side Claude Code, per D12; targeted verification only — scripts, no gradle compile loop needed) + Nick (the §OP Saturday card legs).
status: ISSUE-READY. Baseline: core `c091f7c` (verify at launch; porcelain clean except the known `?? _scratch/`). Execute: weekend 1 (Sat 2026-08-22); the desk half may run Fri evening.
return: nexsys-hivemind/context/audits/<filing-date>_R1R2_return.md (filing-day dated, America/Chicago). The lane commits NOTHING — the hub audits, Nick commits; CI on the push is the gate of record (law 16).
dispatch: "Read nexsys-hivemind/context/instructions/2026-08-20_R1-R2_packaged-write-path_red-first-and-jlink-fix_coding-instruction.md and execute it. - /nexsys-coder"
-->

# R-1/R-2 — The Packaged Write-Path Assert (red-first) + The jlink Fix

## §0 Context and objective (why this is the anchor)

**The measured defect (F-23, CRITICAL — established at source, v51 beats 5–6; H3 return §3.1/§9.3/§9.4):** `build-image.sh` computes the jlink module set from a SINGLE root jar (the app jar) and a FLOOR that lacks `jdk.jfr` — but the production bus wires `BusMetrics.jfr()` unconditionally (`HomeSynapseCore.java` ~:485), and event-bus carries a full `jdk.jfr` consumer surface. **On the jlinked runtime, every publish's metrics emission touches the absent module and the error escapes uncaught: the packaged artifact boots, goes RUNNING, serves health/auth/dashboard — and cannot persist events. A boot-and-idle shell, and the gate's assert set structurally cannot see it** (install-smoke has been green on it all along — §9.3; the false-confidence exhibit of the semester). The H3 return itself named the fix's first half: "Assert integration health in install-smoke — the single highest-leverage item."

**The ruled shape (S-10 R-1/R-2 + the D-5 red-first ruling, ratified):** R-1 the assert LANDS FIRST and is **watched RED against the held card** (the known-bad fixture — the H3 Stage-2 card with `0.1.0+gd26777c` installed; its hold is load-bearing); THEN R-2 the fix in the SUBSUMING form (full-lib jdeps + build-time FLOOR-presence assert) turns it green. The repo lands assert+fix together (one push, CI green — the card carries the red leg's evidence; DP-3 honored by hardware ⏺, not a CI red on main).

**Read FIRST:** `context/pre-verifications/WU-R1R2.md` (P1–P9) — verify every row at your checkout BEFORE implementing; any mismatch is a STOP-and-flag, never a silent adaptation.

## §1 Files to read (before writing anything)

`context/pre-verifications/WU-R1R2.md` (the gate) · `distribution/image/build-image.sh` WHOLE · `distribution/smoke/run-smoke.sh` WHOLE · `distribution/common.sh` (the `HS_*` vars — P5) · `.github/workflows/install-smoke.yml` + `distribution/ci/install-smoke.yml` (the twins — P8) · `distribution/smoke/health-probe.sh` (the probe idiom to match) · `core/event-bus/…/BusMetrics.java` + `BusMetricsJfr.java` (P2/P7) · `lifecycle/…/HomeSynapseCore.java` :470–:500 region (P1) · MODULE_CONTEXT.md for **app**, **event-bus**, **persistence** (evidence context; NO Java module is touched by this WU, so no module-info embeds apply — scripts and workflow YAML only) · the H3 return `nexsys-hivemind/context/audits/2026-08-09_H3-clean-image_fresh-install_operator-return.md` §3.1, §9.3, §9.4.

## §2 The work

### R-1 — the write-path assert (run-smoke.sh, new check in the file's own style)

Add **one new check block** after the health-probe check (own `╔══` banner, next number, `ok`/`bad` idiom, `dump_logs` on fail): **"EVENT WRITE PATH IS LIVE"** — two probes, BOTH must pass:

1. **Persistence probe:** the events DB under the pinned `HS_DATA` path contains **≥ 1 event row** committed by this boot (P6 pins the path + the boot-time emission at source; sqlite3 is precedented in this workflow — install it in the smoke step the same way update-smoke does, or reuse if present). Prefer an assertion that survives restarts (row count ≥ 1 on a fresh install is sufficient for this gate; do not over-engineer a position-delta).
2. **Uncaught-throw scan:** the service journal + `/var/log/homesynapse-stdout.log` contain **ZERO** occurrences of the P7-pinned failure signature (`NoClassDefFoundError`-class on `jdk.jfr`/`BusMetrics` paths — grep the REAL signature you pinned, plus the generic class as a second net).

**The D-6 line (write it INTO the check as a comment, verbatim form):** `# passes-but-false input: an artifact that persists events but throws only on swallowed JFR paths (probe 2 exists for it); a runtime whose boot legitimately persists zero rows (P6 refutes this at source — if P6 fails, this check's form is wrong: STOP).`

**Anti-vacuous pairing (arc-19):** on PASS, the check prints the observed row count and the grep'd-zero line — positive evidence, never silence.

### R-2 — the jlink fix (build-image.sh, the ruled subsuming form)

1. **Full-lib jdeps:** replace the single-root invocation (:79–:83) — every jar in `${IMAGE}/lib` becomes a root (`--print-module-deps` over the full set; keep `--ignore-missing-deps --multi-release`). Union with FLOOR exactly as now.
2. **FLOOR gains `jdk.jfr`** (belt AND suspenders with #1 — the reflective-reach rationale at :84 applies to JFR registration).
3. **The build-time FLOOR-PRESENCE ASSERT:** after jlink, for EVERY module in `${ADD_MODULES}`: `"${IMAGE}/runtime/bin/java" --list-modules` must contain it — `die` loudly on any absence, printing the missing name. `# passes-but-false input: a module listed but broken at link — bounded by jlink's own --dedup-legal-notices=error-if-not-same-content and the R-1 runtime probe downstream.`
4. **Fix the :75–:77 comment to describe the actual invocation** (the comment/code divergence is PART of the defect — F-23's record says so).

### CI (the twins, in sync)

`.github/workflows/install-smoke.yml` AND `distribution/ci/install-smoke.yml`: ensure sqlite3 is available BEFORE run-smoke (move/duplicate the existing apt-install line from the update-smoke step, same idiom). **P8's hardlink pre-check + diff first.** No other workflow changes; the paths-trigger already covers `distribution/**`.

### OUT OF SCOPE (hard fences)

**PKG-E2E-1 / R-3** (PrivateDevices loosening · the rehearsal rig · any integration-under-load run — MINTED DISTINCT, weekend 2) · the systemd unit file · `distribution/README.md` (its :117 "deterministic and self-checksumming" line is DO-NOT-SAY-fenced until W2-3 — touch nothing there) · every claim surface (the D-1 fence stands verbatim until R-4) · the events endpoint · Java source (zero `.java` edits — if you find yourself needing one, STOP and flag) · `bench.sh`/nightly machinery (HANDS OFF).

## §3 Verification (the lane's own gates, then the hardware)

Desk (in-lane): `bash -n` every touched script · shellcheck if available · the census exactly as §4 · re-read P1–P9 post-edit (still true). **NO gradle run needed** (zero Java). The red/green legs are the §OP card sitting (Nick, Sat); **CI green on the pushed commit = the gate of record** (law 16; banks at the next hub beat).

**Red-first accounting (#18, disclosed):** the CI leg is **green-by-construction** (assert+fix land together); the RED leg's instrument is the held card running the known-bad artifact — §OP records it BEFORE the fix is installed there. That ⏺ pair (RED on `0.1.0+gd26777c` → GREEN on the rebuilt artifact) is the WU's red-first evidence of record. **#22 (live-wire bar): N/A-disclosed** — no FE surface is touched; the packaged-runtime probes ARE this WU's real-wire exercise.

## §4 Files table (census-exact; the commit stages EXACTLY these)

| File | Kind |
|---|---|
| `distribution/image/build-image.sh` | M |
| `distribution/smoke/run-smoke.sh` | M |
| `.github/workflows/install-smoke.yml` | M |
| `distribution/ci/install-smoke.yml` | M |

**Stages exactly 4 M.** Anything else dirty at your porcelain = STOP (another writer's work stages never).

## §5 What to watch out for

The comment/code divergence class (fix comments WITH code) · the twins must end byte-identical in their shared body (the wiring-seam header comment may lawfully differ — flag if unsure) · hardlink pre-check per env-model §12 before EVERY edit (P8) · `run-smoke` uses `set -uo pipefail` NOT `-e` — your check must count via `bad`, never exit early · the probe must not require the repo tree at runtime beyond what run-smoke already assumes · do NOT "improve" unrelated checks (delta-only) · arc-4c (Clock reminder): N/A — no Java · the §OP block is ZERO-PLACEHOLDER (H1) and is part of THIS instruction — do not rewrite it, it ships as authored below.

## §OP — the Saturday card sitting (Nick; operator block; ~45–60 min; NEVER inside 03:00–04:15 CT)

**Goal:** the RED ⏺ on the known-bad artifact, then the GREEN ⏺ on the fixed one. **The bench card comes OUT only after a normal shutdown; the coordinator NEVER attaches to the held card (SD-5).**

**Block 1 — RED on the held card (the artifact already installed there — change NOTHING first):**
```
# On the Pi, booted from the HELD card (the H3 Stage-2 card, 0.1.0+gd26777c installed):
systemctl status homesynapse.service --no-pager | head -12
sudo ls -la /var/lib/homesynapse/data/ 2>/dev/null
sudo find /var/lib/homesynapse -name '*.db' -exec sh -c 'echo "== {} =="; sudo sqlite3 {} "select count(*) from events" 2>&1' \; 2>/dev/null
sudo journalctl -u homesynapse.service -b --no-pager | grep -ciE "NoClassDefFoundError|jdk.jfr|BusMetrics" 
sudo journalctl -u homesynapse.service -b --no-pager | grep -iE "NoClassDefFoundError|jdk.jfr|BusMetrics" | head -5
```
**⏺ RECORD every line of output.** Expected (the F-23 prediction, filed pre-read): a zero/absent events row count AND/OR nonzero throw-signature hits. **Either red proves the assert class; BOTH clean = F-23's upper bound is REFUTED at the instrument — STOP, ⏺, the hub adjudicates (that is a finding, not a failure).** (If `sqlite3` is absent on the card: `sudo apt-get install -y sqlite3` — additive, lawful, ⏺ it.)

**Block 2 — the fixed build + GREEN (same card, after the Coder's tree is pulled to the Pi):**
```
cd ~/homesynapse-core && git pull && git log --oneline -1
distribution/deb/build-deb.sh
sudo apt install -y --reinstall ./distribution/deb/build/homesynapse_*_arm64.deb
sudo distribution/smoke/run-smoke.sh
```
**⏺ RECORD:** the build's jlink `--add-modules` line (jdk.jfr must appear) + the FLOOR-presence assert's output + the run-smoke verdict incl. the NEW check's positive-evidence lines. **Expect: INSTALL-SMOKE PASSED with the write-path check green.** Any FAIL = ⏺ verbatim + stop; the hub adjudicates — never retune on the card.

**Block 3 — restore:** normal shutdown → held card OUT (labeled, kept — it is R-3/R-4's rig) → bench card IN → boot → `~/bench.sh scenario boot-health` → **⏺ the [PASS] floor.** (A swap spanning 03:30 CT fires the missed nightly on restore — priced; do the sitting in daylight.)

## §6 Return shape

§0 P1–P9 re-verification results · §1 per-file diffs summary (before→after per hunk) · §2 the D-6 lines as shipped · §3 desk gates (bash -n/shellcheck) · §4 census at porcelain (lock-free, flag spelled) · §5 deviations/pushback (evidence over instruction — flag, never silently comply) · §6 the §OP ⏺ intake slots (the hub folds Nick's pastes) · §7 next-WU pointer (R-3/PKG-E2E-1, weekend 2). Welcome technical pushback — if the bytes contradict this instruction anywhere, your flag is the deliverable.
