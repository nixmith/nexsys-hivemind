<!--
file: context/audits/2026-08-23_R7b_and_card-sitting_intake_two-layer-audit_v56-beat-5.md
purpose: v56 beat-5 two-layer intake audit of (A) the R-7b version-scheme return
         (context/audits/2026-08-23_R7b_version-scheme_return.md, 16,157 B on disk) and
         (B) the Blocks 1-3 card-sitting operator return
         (_scratch/card-sitting-2026-08-23/…_operator-return.md, 47,114 B on disk; copied to
         context/audits/ at this beat's order). Layer 1 = the lanes' claims; layer 2 = re-executed
         at the bytes/diffs/primaries by the hub. Rulings for both returns are IN THIS FILE.
audience: Nick · the hub · the v57 hub.
status: FILED (v56 beat 5). Verdicts: R-7b ACCEPT (with @v6 RULED IN pre-commit) · Blocks 1-3 ACCEPT.
-->

# v56 beat 5 — the R-7b + card-sitting intake audit

## §A R-7b — VERDICT: ACCEPT. All 11 files verified at their diffs; both [REVIEW]s ruled below.

**Instruments.** Working-tree diffs vs `e845cd9` exported per file to `_scratch/v56-b5/` (42,740 B / 11 files)
and re-read whole in the hub container; porcelain re-run split (`-uno` = EXACTLY the 11-M census, 0 A 0 D;
scoped untracked scan over `.github`+`distribution` = EMPTY); numstat re-run = the return's table EXACTLY
(263+/109−; common.sh +34/−13 · rig +102/−43 · twins +26/−6 ×2 · build-image +12/−9 · architecture +35/−16 ·
boot-contract-map +23/−13 · escalations +2/−0 · unit/ci.yml/build-deb +1/−1 each). NUL scan (grep -P '\x00')
over all 11 diffs: CLEAN. L3 (64-hex / 43-char-base64 runs): ZERO — the one 64-hex surface (`sha256 ${DEB_SHA}`)
is computed at CI runtime, no literal in the diff.

**Layer-2 claims re-executed — ALL CONFIRMED:**
- **common.sh:** resolution order is now env → git → `VERSION` → `../VERSION` → skeleton AT THE BYTES (the two
  file-consults moved BELOW the git block); `_dist_dir` honours `HS_DIST_DIR` first; the arm is
  `TZ=UTC git -C "${_d}" log -1 --format=%cd --date=format-local:%Y%m%d.%H%M%S` with the POSIX 8-dot-6 `case`
  pattern (`.` is literal in a case glob — checked) and `printf ''` fail-closed; `|| true` inside the capture
  (D3 ACCEPTED — routes a FAILING `git log` to the same fail-closed `''` under `set -eu`).
- **Twins:** hunk-identical after path normalization (diff-of-diffs, exit 0) — LTD-01 comment fix, `setup-node@v5`,
  the echo step with `HS_DIST_DIR=distribution`, the skeleton fence AFTER the grammar assert, the sha256-bearing
  green line, and the rider-k verify block in the `if grep … exit 1` form with the `command -v` hard guard.
- **Rig:** the 34-check census re-derived from the diff = 10 arm + 9 accept + 3 + 3 reject + 4 ordering + 5
  carriers ✓; verdict-integrity assert (`ran == expected`, 30+ORDERING_ROWS) present ✓; the mutation-5 derivation
  re-derived row-for-row (three `+git` arm rows, the empty-cdate row, the VERSION-bypass row — and the FAKE_NOGIT
  row passes on the OLD order, correctly not counted) ✓; red-first 7 = those 5 + both fence rows ✓; the "5 of 30"
  / "7 of 30" wordings are the Git-Bash (no-dpkg) RAN — coherent ✓; mode 100755 unchanged ✓.
- **Unit / boot-contract-map / architecture / escalations:** `:31` `LogsDirectory=` one token ✓; §Health rewritten
  to the shipped R-9 posture with E3 CLOSED + the M13 DANGER-note reframe ✓; the version-string section carries the
  git-first order, the ordering argument, fail-closed, the fence, and the `:135–:137` retirement ✓; E1 (c) appended
  verbatim ✓.
- **Lane closeout (hivemind):** coder-handoff +11/−2 (the R-7b entry prepended, both [REVIEW]s carried honestly),
  coder-lessons +6/−0 (one well-formed lesson: `! grep` vacuity + existence-vs-runtime verification + the msys
  PATH drive-colon note). ACCEPT.

**RULING 1 — `upload-artifact` → `@v6` IN (executed by Nick pre-commit; the queue §1 step 0).** The hub re-verified
at the primary: `action.yml` at `refs/tags/v6` declares `runs.using: node24` and the input set is byte-identical to
v5's (name/path/if-no-files-found/retention-days/compression-level/overwrite/include-hidden-files). H-4's intent
was ANNOTATION-CLEARING, and v5 is `node20` — the coder's pushback is correct and the ruled `@v5` was the hub's
under-verification (existence checked, runtime not; the coder's lesson names it exactly). The GitHub tag-sha API
read 403'd (rate-limited from the container) — the workflows pin MAJORS, not shas, so the load-bearing facts
(node24 + identical inputs) are verified and sufficient. The flip is one token ×3 files; the rig's carrier checks
are version-agnostic, so NO rig change rides it; numstat shape and the 11-M census are unchanged.

**RULING 2 — rider (k)'s reshape ACCEPTED; the hub OWNS the vacuous fragment.** The instruction's literal
`! grep -q 'Unknown key name' …` can never fail a `set -e` step (bash exempts `!`-inverted commands from `-e`) —
a gate the hub authored that could not gate. Hub authoring defect, owned on the record (the arc-7/arc-17 class:
every new CI assert gets a mutation flip — the coder ran the flip the hub's rider skipped). The shipped
`if grep … exit 1` + `command -v systemd-analyze` guard is the correct form, mutation-proven both ways.

**[INFO] adjudications:** (3) `|| true` ACCEPT (above). (4) `build-deb.sh:24`'s missing `HS_VERSION="${HS_VERSION:-}"`
symmetry — parked on the packaging batch (one token; rides the next distribution touch). (5) `build-image.sh:72`'s
"(reproducibility/LTD-10)" mis-attribution (should be LTD-01) — FOUND-not-edited stands; NOT folded into this
commit (the audited bytes are the commit; a one-token comment rides R-3b or the packaging batch). (6) E1 placement
STANDS as shipped (the instruction said append; a style move costs a diff line for zero content). (7) The
count-line implementation (header + verdict-integrity assert) ACCEPT — stronger than the ruled prose.

## §B Blocks 1-3 — VERDICT: ACCEPT. The sitting is complete, disciplined, and layer-2-coherent.

**Hub cross-checks (independent):** the packet md5 re-run by the hub on the device = `bd42cb93…` @ 27,639 B —
the "packet UNCHANGED" claim CONFIRMED at the hub's own instrument · the uploaded return (47,114 B) = the on-disk
copy byte-for-byte · the digest lines = Nick's beat-4 paste verbatim (0.29s/0.28s) · the P-1 `/state` body = the
banked paste field-for-field (56.0 / 100 / 23.0 / stateVersion 78574 / viewPosition 112516) and the epoch-instant
coherence check re-done (read 25.8 s after lastReported; lastChanged trails by exactly 10 s — sound) · the §3.4
rotation listing = the hub's §OP-A record exactly (300 B/44 B, `-rw-------`, mtimes 13:12) · the artifact pair
hashes = the Block-0 banked pair (`ed82ae8f…` / `db57fa90…`) on all THREE hops · the port-identity string = the
2026-07-25 Rosonway record byte-identical · the RED throw signature = the F-23/R-1 class exactly
(`BusMetricsJfr.recordWriterQueueDepth:59`). **R-1/R-2's hardware half is PROVEN**: RED 7 throw-lines/10 rows on
`0.1.0+gd26777c` → GREEN 0/14 on `7c9e4fa`, one card, one byte-identical instrument, + run-smoke 18/18 with check
4's two positive lines — the first hardware green of the write-path assert. Restore closed at boot-health 6/6,
fleet 5+1, coordinator at byte-identical port identity. F-S18 (bare-id `gt` proven live by the flag-less upgrade)
CONVERGES with the rig's ordering row 4 — hardware and dpkg agree.

**Rulings on the four (+ the rest):**
- **F-S9 ACCEPT — R-3 premise corrected.** `initial_api_token` is PRESENT on the held card; the E3-GREEN block
  does not inherit its precondition and must CREATE it: `mv` the artifact aside (delete NOTHING), restart, prove
  `active`, `mv` back. Folds into the R-3a packet finalization (Fri act).
- **F-S15 ACCEPT — restore-block law.** `~/bench.sh start` is written into EVERY card-swap restore block from now
  on (R-3a, R-4, the Pelton-day swap runbook). Proven necessary, not theoretical.
- **F-S11 ACCEPT.** The SD-5 coordinator fence (unplugged for the whole non-bench-card leg; re-plug only after the
  card is out) is written EXPLICITLY into R-3a/R-4 — it was load-bearing (the held card's zigbee custody store
  wrote live during RED).
- **F-S10 ACCEPT — new OPEN risk (OR-TOKEN-MODE-644).** The packaged first-run mint writes token files 644 where
  the rotate path writes 600; the 700 config dir is the only shield; run-smoke checks dir-mode/ownership so CI is
  structurally blind. Fix = mint 0600 explicitly (core, packaging batch) THEN extend run-smoke with a file-mode
  check (that order — the check first would go red). Both observed halves in one sitting make this evidence-grade.
- **F-S21 CONFIRMED — the hub OWNS the label.** The §OP-A/§OP-H window was recorded "13:11–13:16 CT"; the store
  mtimes (13:12 Pi/ET), the boot log (13:15:19 ET), and the arithmetic of Nick's 12:20 CT report (a sitting
  "13:11–13:16 CT" would post-date the message reporting it) all say the window was **ET = 12:11–12:16 CT**.
  Reconciled AT SOURCE this beat (the beat-4 block's label corrected in pm-handoff; the beat-4 commit message is
  immutable history — this audit is its correction of record). Exactly the class the Z-stamp convention exists
  for; hub records now carry the Pi-side clock as ET or as Z.
- **F-S7 — the Aug-22 nightly confounder DISCHARGED** on a negative result (confounded and clean nights identical;
  Δ 10 ms). The wait-state closes this beat. **F-S19/F-S13 ACCEPT** (successor-packet craft: refresh P-3 +
  "these three among the listing" phrasing; `sudo` on the config glance). **F-S6 the hub OWNS**: the pair was
  staged Sat 2026-08-22 ~03:20 CT, not "Thursday" — the standing-ask prose is corrected this beat. **F-S12
  ruling: HOLD-PATCH (rec)** — the held card stays at its Aug-13 OS state through R-3a/R-4 (the artifact must be
  the only variable); patch lands after R-4, before RS-3-era work. **F-S8 → the R-10 docket** (state-read rendering
  asymmetries: epoch-vs-ISO instants; `entityId` `{msb,lsb}` not round-trippable from the body). **F-S14/S16/S17/S20
  banked as notes.** **E-P3/E-P5 absences recorded**; E-P5's `vcgencmd get_throttled` folds into R-3a's pre-flight
  (cheap there, and R-3a wants the throttle baseline anyway).
- **Deviations D-1…D-5 + the zero-effect slip: ALL ACCEPTED** (withdrawals disclosed as absences, not passes —
  correct form; D-3/D-4 justified by F-S11/F-S15 and now codified).

## §C Banked this beat

Nightly digests **2026-08-22 + 2026-08-23** (8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency
0.29s/0.28s — the pre-swap floor, green) · **P-1** (the 02P environmental channel LIVE in the state store:
temperature_c 23.0 / humidity_pct 56.0 / battery_pct 100; RS-2's tripwire does NOT fire; A0 GREEN, A′ real —
a first-order R-10 charter input) · the card-sitting evidence set (§8 of the return) · CI on `e845cd9` stays
banked NICK-REPORTED (the container's unauthenticated API reads are still rate-limited — the R-7b-commit run
banks fresh at its own pages/paste).

## §D CI predictions for the R-7b push — FILED BEFORE THE PUSH (H12), @v6 form

Build & Check GREEN ~3 min, zero Java delta (rest-api **147** · lifecycle **62** · app **24**). install-smoke
BOTH legs GREEN (~2m45s amd64 / ~3m01s arm64): Static lint prints `all shell scripts parsed clean` → the rig's
**34 PASS rows + `VERSION-GRAMMAR-TEST PASSED ✓  (34 checks)`** (ubuntu runners carry dpkg) → `unit directives
verified`; the echo step prints `hs_version=0.1.0+git<committer-date-UTC-of-the-pushed-commit>.g<its-sha>`
(NO `-dirty` — clean checkout), then the green line with the scheme name, matching `.deb Version=`/`image
VERSION=`, and `sha256 <64-hex>  homesynapse_0.1.0+git<date>.g<sha>_<arch>.deb`; **19** `[smoke] PASS` lines/leg;
update-smoke GREEN (`V2=<ver>+up`; `+up gt` proven at dpkg on the desk); artifacts
`distribution-artifacts-{amd64,arm64}` upload via `upload-artifact@v6` (node24). **Node-20 annotations: ZERO.**
Plausible REDs: none specific remaining (v6 inputs verified identical; dash-compat proven ×2 shells; the v5-input
-rename class excluded). Any red = STOP, paste the job log lines; do not re-run.

## §E Orders

Core 11-M order + the hivemind 7-file beat-5 order: `_scratch/2026-08-23_v56-beat-5_operator-queue.md`
(msg files `_scratch/2026-08-23_core_R7b_commit-msg.txt` · `_scratch/2026-08-23_hivemind_v56-beat-5_commit-msg.txt`).
The R-3a finalization (Fri) consumes F-S9/F-S15/F-S11 + this return's ⏺s + the R-7b run id at Block I.
