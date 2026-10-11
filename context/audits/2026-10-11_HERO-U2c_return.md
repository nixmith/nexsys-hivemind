<!--
file: context/audits/2026-10-11_HERO-U2c_return.md
purpose: HERO-U2c lane return. The recovery card re-cut under CARRIER: f (AMD-103 as ratified): FIELDS §3 on the record's keys; SPEC §3's S3 column re-read with its null forms; R6, the sixth cell, beside the fifth state; SPEC §4 · §7 · §11 · §12; states.html. Design only.
audience: the hub (two-layer audit, charter §8) · Nick (SPEC §12 Q9–Q12 in one batch; the git add card after ACCEPT)
state-type: lane return (frontend; design mode)
status: RETURNED Sun 2026-10-11. DESIGN-ONLY: nothing touched a wire.
-->

# HERO-U2c — return

## §0 The card
- **Instrument.** `date -u` 13:53:45 UTC Sun 2026-10-11 → CT 08:53 (UTC−5). Shell on Nick's computer: git read verbs (status, diff, log, show with `--no-optional-locks`; ls-files, config --get), grep, python3, md5sum. Node 22.23.2 present; the toolchain not run (no installs; `npm run dev` needs a Linux `npm ci`). No gate, Java or wire. Mockups rendered headless here, from an md5-equal copy.
- **Start:** `web-ui/dashboard` porcelain EMPTY; core `6a03403d`, main. **AMD-103:** the docs card (`e2a5844`, md5 `6694f075`) = DRAFT v7 (`371cd241`) byte for byte, bar the header; R-B, R-C, R-G, §3, §4 read whole.
- **Census: 4 M, nothing else; git read verbs only.** `homesynapse-core/web-ui/dashboard/design/recovery-card-v1/FIELDS.md` 8,810 B `ca19e9028fe0` · `…/SPEC.md` 57,242 B `2d13c5b8357b` · `…/states.html` 82,652 B `5df972a8f3a5` · `…/README.md` 1,777 B `28dd3fa6a2f4`; plus this return.
- **P1 HOLDS (+2).** Both per-probe rows RETIRED with AMD §3's reason (kept, marked). The record's keys are in, each NOT-ON-WIRE · PROPOSED with its AMD row (R-B ×4, R-C ×5, R-G derived); `integrationId`, `ieeeAddress` stay. Added: `meta.recoveryViewPosition` (AMD §3) and the fifth-state row (P5). `windowStart` and the link triple are outside AMD §3's list (Q12).
- **P2 HOLDS.** `grep -ril` with `_scratch/blocked-names.txt` (`2568eb2d9314`) plus the working names: 0 files. `{{NAME}}` counts unchanged (0·1·3·3).
- **P3 HOLDS.** `src/` porcelain empty at start and close.
- **P4 HOLDS, 3.** (a) Freeze `:255–:265` overruns a 260-line file; the additive rule is `:260`, and "beside, never under" is AMD §3's text. (b) §2's "from v4": the ground is v7's (v4 lacks the on-change restart, NE4, NE3: grep 0/0/0). (c) "U3 computes it" vs R-G's "core's clock": inputs off the wire (Q10).
- **P5 HOLDS.** The key is lost; S2's two arms carry S3; the restart arm is NOT SAYABLE AT S3 (Q9).
- **P6 HOLDS.** 7/7 S3 cells carry **Null** = S2; §3's header states precedence and the null rule.
- **Defaults.** R6 is a row (AVAILABLE family): L1, hourglass, unknown hue, no act; never on UNAVAILABLE; R5 stands on UNKNOWN. {t} = the newest of R-G's four instants; the core serves R-G. The window is named at both ends, never "this hour", never summed. Floor sentence re-cut. `missesToDark` ≠ 2 → bare label.
- **Keys (PROPOSED):** `probeAnsweredAt` · `probeWindowStart` · `probesAnswered` · `probesMissed` · `probeLink` · `availabilityClass` · `reportIntervalSeconds` · `silenceLimitSeconds` · `missesToDark` · `recordIntervalSeconds` · `meta.recoveryViewPosition`; R-G derived, no key; `integrationId` · `ieeeAddress` stay.
- **For Nick:** SPEC §12 Q9 restart ambiguity · Q10 where R-G is computed · Q11 R6's form · Q12 `windowStart` and link on the wire. None blocks the card; Q10 blocks R6's build row, Q12 the L2 window row.

## §1 FIELDS §3 as re-cut
- The heading is kept. A paragraph states the source: the record, through the recovery-card projection, appended at v1.1.7 after v1.1.6. It also says every key is PROPOSED and states the null state.
- **Rows:** 2 retired, 14 new or re-sourced, 4 kept verbatim. RETIRED: `lastProbeOutcome` + `lastProbeAt`; `probeMisses`.
  - R-B: `probeAnsweredAt` (the reply instant; at most one record per device per interval, plus one per tracker start) · `probeWindowStart` · `probesAnswered` · `probesMissed` · `probeLink` (its `at` is `linkAt`, never the reply's).
  - R-C: `availabilityClass` (it names the arm, `T:550`) · `reportIntervalSeconds` (null for every floor device) · `silenceLimitSeconds` · `missesToDark` (`T:110`) · `recordIntervalSeconds` (null for passive).
  - Also: `meta.recoveryViewPosition`; R-G's bound (its inputs and which are off the wire); seeded-never-asked (re-derived).
- **Cites.** `AMD R-x` / `AMD §n` point to the docs card. Every `T:`/`A:` line was re-read at `6a03403d`; both files are unchanged since `da9ca3d`.
- **§1–§2.** §1 is unchanged. One row group moved: `availabilityReason` · `lastSeenAt` · `link` have been IN-MIRROR since v1.1.6 (HERO-U2b `409547c`; `C:280` · `:285` · `:289`). §2's heading now says so; its rows are unchanged.

## §2 SPEC's changes
- **§3.**
  - Header: six rows; S3 = the record's keys; precedence (`availability` picks the family, the record chooses within it); the null rule.
  - `checkedTime` is the last RECORDED answer.
  - R1 and R2 turn on `probeAnsweredAt` vs `lastReported`. Quiet can trail the silence by up to one record interval, and until then the row is R1 with its age. R2 gains its null-`lastReported` arm, and its L2 window is named at both ends.
  - R3 is as at S2: "twice" is `missesToDark`; ≠ 2 gives the bare label, and null keeps S2's basis.
  - R4 reads the contract; R5 follows P5.
  - **R6** sits beside R5: not sayable at S1 or S2; its S3 rule; the reasons it is a row, not a cell; never on UNAVAILABLE (`T:449`, `:465`: no record is owed).
  - Coverage: 7 × 3 = 21 of 21.
- **§4.** The class and the numbers come from R-C. The floor sentence is re-cut, and the fallback covers S3's nulls.
- **§7.** 5 rows retired (`quiet.line`, `l2.lastAsked`, `l2.outcome.{ok,timeout,error}`), 9 added, 1 changed (floor): 67 rows. New slots: `checkedTime` · `windowStart` · `answered` · `missed` · `recordInterval`. Level ≤ 5.8; ≤ 14 words.
- **§11** row 4 is re-pointed: the keys; the null gate; R6's arm and glyph; the catalog move; the `test.todo` rows re-keyed; a v1.1.7 test with a catching-up scenario.
- **§12** gains Q9–Q12; Q5 now notes that its S3 half is retired.
- **Outside the five named sections**, one clause each to stay consistent: §2 (six rows; L2's newest check) · §6 B (six rows) · §8 (R6's shape; the R5/R6 pair) · §9 (R6 unknown) · §10 (sentence 8, R6).

## §3 states.html's changes
- **A new section, "§3 R6 — the sixth cell beside the fifth state", in dark and light.** R5 (Porch Lamp) sits beside R6 ("No check recorded since 3:02 am"). Below them, the same plug: as R2 inside the bound, and in its null form (catching up → S2's "Reporting" with its age). Captions cover shape, words and hue, and precedence.
- **The S3 cards are on the record.** All 22 "Last asked" rows became "Newest check on record". The Quiet lines read "It answered the newest check on record, at …", with window and recording rows. R3's L2 shows the answer before the dark edge, and the P5 caption gains the (f) note. The header comment and the §3 heading are amended.
- **Proven.**
  - Inverting the edit script rebuilds the baseline md5 (`5e68eacc`).
  - No script, no external request; tags balanced; no horizontal scroll at 390 px.
  - R6's pill: 7.24 / 7.59 dark, 5.17 / 6.04 light.

## §4 Findings
1. **The v1 floor sentence was wrong for the floor class.** "Reports at least every minute" stated the ask threshold as a report cadence; R-C records no report interval for that class. Re-cut: "This {kind} has no report schedule on record."
2. **"Since {windowStart}" alone overstates the window.** The window ends at the record's `at`, not now, so the copy names both ends (this refines charter §4).
3. **R-G's inputs are off the wire.** The keys AMD §3 lists lack the newest `availability_changed`'s and contract's instants, the 5-s deadline, one sweep and N; `meta.timestamp` (freeze `:33`) is the core's clock (Q10).
4. **FIELDS §1's `C:` cites were off even at `da9ca3d`.** Four of five rows: they read `:244/:245/:246/:250`, where name, availability, stale and deviceId sit at `:241/:242/:243/:247`. At `6a03403d` the lines are `:264/:265/:266/:270/:274`. Left as is (§1 unchanged).
5. **Pre-existing, not from this edit:** with every L2 `<details>` open at a 1320-px viewport, the "Quiet" stage section overflows by 86 px. The baseline overflows identically; with the details closed (the default) it fits.
6. **Open for AVAIL-API-1:** which source fills R-C's `reportIntervalSeconds` for a passive device. FIELDS keeps U2a's declared interval (`A:872–:882`), and R4's Quiet depends on it (Q4).
7. **Grading method:** a vowel-group Flesch–Kincaid that reproduces §7's slot-free rows. textstat's dictionary fetch was refused by the proxy and was not bypassed.
8. **Verification register: DESIGN-ONLY.** Next WU: AVAIL-API-1's cut (after this landing, REGISTRY-COLD-1 and R-F's number), with Q10 and Q12 settled at the bump; then U3 builds SPEC §11 row 4.
RETURNED nexsys-hivemind/context/audits/2026-10-11_HERO-U2c_return.md 9086
