<!--
file: context/handoff/2026-08-23_PM-mission-control_v57_orchestrator_session_prompt.md
purpose: the banked boot prompt for the v57 PM MISSION-CONTROL hub session (opens ~Mon Aug-24; runs the
         Pelton week). Authored at v56 beat 6 (the close, Sun 19:18 CT). P5 EXECUTED: §2 is generated from
         the beat-6 snapshot digest — the v57 hub re-derives nothing the spine already carries.
audience: the v57 hub.
status: BANKED (v56 beat 6). The spine outranks this file the moment any beat moves something.
-->

# v57 PM MISSION-CONTROL — session boot

## §1 Boot reads — EXACTLY these, in order (~33 KB spine-side; the region-cap law keeps them lean)

1. `context/status/READ-ME-FIRST.md` (967 B) — the launch map. NO ls sweep.
2. `context/handoff/pm-handoff.md` — the frontmatter chain (`:8`) + the how-to-read line + the **NEWEST-3
   beat blocks** + `## Open Risks` ONLY (≈29 KB together). **NEVER read this file whole** (~127 KB; the tail
   is history reachable by pointer).
3. `context/status/PROJECT_SNAPSHOT.md` whole (≈3 KB).
4. `context/planning/2026-08-23_pelton-week_plan-of-record.md` (≈7 KB) — the week program, the decision
   calendar, the A-14 hours check.

Everything else BY POINTER at the act that needs it: `context/audits/2026-08-23_R7b_and_card-sitting_intake_two-layer-audit_v56-beat-5.md` (the rulings of record: @v6, F-S9…F-S21, HOLD-PATCH) · the card-sitting return (⏺ evidence for R-3a) · `context/handoff/2026-08-22_R3-packet_new-blocks_CI-artifact-install_and_E3-restart-proof.md` + the base R-3 packet · the G-2 readiness brief · the swap runbook · the BRAND-SPRINT-1 / FE-SWAP-CENSUS returns · `context/instructions/2026-08-23_skills-lane_W-SKILLS-4_launch-cost-and-conventions_brief.md` · archives ONLY via the archive map, bounded reads on everything large.

## §2 State at banking (v56 beat 6, Sun 2026-08-23 ~19:00 CT — verify zero-drift at launch, then trust the spine)

**HEADs:** core **`dec35be`** (R-7b LANDED, 11-exact; **CI GREEN ×3 checks, ~2 m each** — banked at the run
icons + Nick's word, law 16; the echo-step lines + the install-smoke run id are UNHARVESTED — harvest at the
R-3a finalization, which pins them anyway) · hivemind = the v56 beat-6 commit (3-exact: spine ×2 + this file)
· skills `5105abc` · bench `4539f13` · docs `a53f474`. Porcelains at launch: BOTH EMPTY (verify).
**CLOSED arcs:** R-1/R-2 (code + CI + **HARDWARE** — the card sitting: RED 7 throw-lines/10 rows on
`0.1.0+gd26777c` → GREEN 0/14 on `7c9e4fa`, run-smoke 18/18, boot-health 6/6, restore at byte-identical port
identity) · R-6/R-8 (token ops; §OP-A) · R-7 (arm64 channel) · **R-7b (R-V: `0.1.0+git<YYYYMMDD.HHMMSS>.g<sha>`,
git-first + `HS_DIST_DIR`, the skeleton fence in CI, the rig at 34 checks incl. dpkg ordering,
`upload-artifact@v6`/node24 — zero Node-20 annotations expected on every future run)** · R-9 (loopback
`/health`; the interim operator law RETIRED v56 b4) · W-HIVE-1 (the region-cap law LIVE: pm-handoff `:8`
≤3,000 B · newest-3 ≤18,000 B · Open Risks OPEN-only · snapshot ≤3,500 B; the breaching beat fixes it).
**Bench:** `e845cd9` build; §OP-A/H green (12:11–12:16 CT = 13:11–13:16 ET — F-S21); nightly floor
`8/9 PASS · 1 SKIP(hue-online) · 0.29s/0.28s`. **Held card:** OUT, labeled `hs-fresh — R-3/R-4 rig — 7c9e4fa`;
token state byte-identical as found (`initial_api_token` PRESENT — F-S9); **HOLD-PATCH through R-4** (F-S12;
95 OS packages pending, deliberately). **P-1 BANKED:** the 02P environmental channel LIVE
(23.0 °C / 56 % / 100 %) — A0 GREEN, A′ real (first-order R-10 input).
**Open Risks (OPEN only):** OR-E3-PROBE (sole residue = R-3's E3-GREEN; per F-S9 the block **creates** the
token-absent condition — `mv` aside, delete NOTHING, restore after) · OR-TOKEN-MODE-644 (mint 644 vs rotate
600; CI structurally blind; fix mint-0600 FIRST, then the run-smoke check) · OR-REHOMED-OQ · OR-M13-SDNOTIFY
(T-0 rec; resolves at R-10).
**FENCES (absolute):** the D-1 DO-NOT-SAY pair until R-4 · `distribution/README.md:117` until W2-3 · no
public brand use before G-2 · s31 legs/nightly HANDS OFF until R-5 · the hub NEVER implements · token values
never pasted/logged.

## §3 The week program (detail + hours = the plan of record; these calendar rows are the law)

- **Mon:** Nick pastes the W-SKILLS-4 dispatch (+ optionally FE-SWAP-GATE — both paste blocks sit in
  `_scratch/2026-08-23_v56-beat-4_operator-queue.md` §4). Hub: **P6** (coder-lessons rotation: oldest by
  count → archive, file ≤16 KB, zero content loss) + the R-3a fold-in prep. The LLC state/agent pick is
  branch-independent (~1 h) — offer it Mon/Tue.
- **Tue:** the W-SKILLS-4 return → the census audit (every rule name in = out; retirements BY NAME; two files
  re-counted, three moved rules diffed at the bytes) → Nick commits + the mirror copy (`diff -rq` ×3 pairs —
  Check 9). The 5-min JP mp3 listen any evening.
- **WED/THU: PELTON → THE ONE WORD (§4). Same-day execution.**
- **Fri:** the R-3a operator packet PRINT-READY. Fold: **F-S9** (E3-GREEN creates the absence) · **F-S15**
  (`~/bench.sh start` in EVERY card-swap restore block) · **F-S11** (the SD-5 coordinator fence EXPLICIT:
  unplugged for the whole non-bench-card leg; re-plug only after the card is out) · **E-P5**
  (`vcgencmd get_throttled` in pre-flight) · F-S13 (`sudo` the config glance) · F-S19 (P-3 refreshed;
  "these three AMONG the listing"). **Block I pins the `dec35be` install-smoke run id + its sha256 log line**;
  STOP-gate: Version matches `^0\.1\.0\+git[0-9]{8}\.[0-9]{6}\.g[0-9a-f]{7,}` ; `--allow-downgrades` exactly
  ONCE per card. R-3b stamped ISSUE-READY-pending-measurement (it may also carry `build-image.sh:72`'s LTD-01
  comment token + `build-deb.sh`'s HS_VERSION symmetry if the census stays clean).
- **Sat Aug-29 (daylight, 4–6 h):** R-3a — the custody clone, the drop-in measurement, the packaged boot on
  real silicon, the 30-min evidence window. **Sun Aug-30:** R-3b lands → **R-4** (the ~45-min re-rep on the
  SHIPPED artifact) → **THE FENCE LIFT** — the two D-1 sentences move to the positive-scope register
  ("verified on real hardware at commit ⟨R-3b sha⟩"). The week's prize.
- **Aug-31:** RS-3 / W-MARKET-2 dispatch (or its tripwire). **~Sep 5–6:** the R-10 charter — docket: R-L1 C-1
  · R-L2 T-0 · R-L3 NO (recs) · physics A′/A/B (A0 GREEN) · A-14 confirm · Doc 09 §15 Q1 · READY-ordering
  drift · JDK trajectory · IR emit · events endpoint · FE-STATE-DIALECT · **F-S8** (state-read rendering
  asymmetries: epoch-vs-ISO instants; `{msb,lsb}` entityId not round-trippable).

## §4 THE PELTON WORD — the pre-staged execution map (fires the moment it arrives; outranks everything)

Nick's word: **A-CLEAN / B-MIXED / C-ADVERSE** (optionally "A — ZENDOMO is the name" = R-1 in the same
breath). On ANY word: the reply goes out SAME-DAY from the G-2 readiness brief §1–§2 scaffolds. **On A (or
A+R-1):** the swap program fires per the runbook — the FE flip WU dispatches (red-first if FE-SWAP-GATE
landed; the census is 4–5 files per FE-SWAP-CENSUS) · the hub README patch · `brand.mjs:14` · the B-2 fold
paste · B-1 Direction B charters (~10–16 h of design work QUEUED, never squeezed into the week) · B-7 to
counsel with the filing question · the LLC state/agent pick if not already made. **On B:** the scaffold's
clarify-then-proceed branch; NO public act. **On C:** full stop on brand surfaces; the C-scaffold reply; the
name search re-opens. NOTHING public in any name before G-2, even on A.

## §5 Session mechanics (compressed; the PM skill + the audit corpus carry the rest)

Beat cycle: intakes → work product → spine writes (chain segment ≤300 chars prepended at `:8` + the beat
block prefix-prepended; the WRITING beat enforces the region caps) → census-exact orders (**"stages exactly
N"** · msg via `git commit -F ../_scratch/<file>.txt` · the glance + STOP-gate in its OWN block · **NO
attribution trailers EVER**). Two-layer audits on every intake: claims re-executed at the bytes/diffs/
primaries; labels are claims, quotes are evidence; L3 secret scan (zero 64-hex/43-char runs) every time.
Law 37 (returns verified ON DISK) · law 5 (landings verified AT PORCELAIN) · law 16 (CI banks at run pages/
API/Nick's paste; banked verdicts FINAL — never re-derive) · H12 (predictions FILED BEFORE runs, derived from
artifacts; misses OWNED on the record — v56 owned three hub defects and was stronger for it) · H10 (every
escalation = branches + recommendation + a one-word ask; open-ended questions are a defect) · H13 (one
byte-identical instrument across compared runs). Device bridge: reads via `$HOME/mnt/ClaudeFolder/…`; writes
= container-edit → SendUserFile → device_commit_files (Windows-form paths); porcelain spelled
`git --no-optional-locks status --porcelain`; status/numstat SPLIT and scoped (H14; the dirty-mount 45 s
ceiling → split further); dotfile globs miss `.github`-prefixed exports — glance `.*` too; a stale
`index.lock` → `mv` to `_scratch/_to_delete/` (delete NOTHING); NEVER re-stage a same-path file expecting
fresh bytes (stale cache — write to a NEW path); H17 (never read predecessor scratch beyond named handoffs);
NUL-scan every authored file pre-delivery (write "backslash-u-0000" as prose, never the literal); **Pi-side
clocks are ET — label ET or Z, never bare CT** (F-S21). Fable 5 Extra on every lane: denser briefs, expect
strengtheners; capability never substitutes for verification.

## §6 First acts

The launch verification (zero-drift: the §1 reads against §2; porcelains — hivemind at the beat-6 sha, core
`dec35be`, both EMPTY) → the Monday program (§3): P6 + the R-3a fold-in prep, authoring ahead of need so
every beat ends with the next paste blocks on disk → the W-SKILLS-4 return intake when it arrives. The
Pelton word OUTRANKS everything the moment it lands (§4). Record the dispatch text in the beat-1 spine write.
