<!--
file: context/audits/2026-09-23_v79-b5_CLOSE_long-term-read_record-hygiene_v80-text_audit.md
purpose: The v79 close (beat 5) — Nick's two facts and two steers; the long-term read that chose the next window (two read-only lanes with file:line cites; the hub's re-reads); the determination; the record cleaned (what moved, the conservation checks, the bytes before and after); the repos' census; the v80 dispatch text and what changed from v79's form.
audience: the hub (v80 reads §2 when THE HORIZON RE-CUT sends it here) · Nick (§0)
state-type: audit
status: FINAL — v79 b5 (Wed 2026-09-23 ~16:5x CT; instrument 2026-09-23T21:51:35Z)
-->

# v79 b5 — THE CLOSE: the long-term read, the record cleaned, the v80 text

## §0 The ruling of the beat
The application is commissioned and the `.com` is owned, so the company side now waits on counsel's draft and the prepayment; nothing public moves before FILED and the receipt. The path to the run moves Thursday (the plugs) and next week (rehearsal 1). Read against the long-term plan, the plan of record stops at the run: the install flow, the launch content and the launch itself are scheduled nowhere. v80 therefore carries one deliverable on the path (rehearsal 1's packet on the metered fleet) and one desk item for the horizon (THE HORIZON RE-CUT, Saturday), with the company's private work (FIN-1, the strategy pass for Monday's outreach, the B-1 charter, the attorney search) and the research lanes that have instruments beside them. The record was cleaned first, so v80 boots on one screen.

## §1 The intake
- Nick's words (the DR §1e): the application commissioned and handed to counsel; the `.com` owned; "until Monday"; steer 1 (the context window; the day's deviation; clean the repos and the record; the next hub prompt); steer 2 (consult the short- and long-term plans, then decide).
- Not yet said: whether the agreement's two corrections landed; how the prepayment was paid (`PREPAY:`); the registrant and the settings on the `.com`.

## §2 The long-term read (the lanes' digests, condensed; their cites, re-read by the hub where marked ✓)
**Product** — master-release-plan (MRP), phase-3-milestone-backlog (BL), research-agenda (RA), the root Technical_Roadmap_v1 (TR):
- MRP (verified 05-22): V1 Mar 13 → Nov 25. P4 Integration & Zigbee Sep 14 – Oct 11, gate 50 devices stable 24 h; P5 System Validation Oct 12 – 25, gate 72 h stability + perf targets; P6 Distribution & Website Oct 26 – Nov 15, gate "install flow works end-to-end"; P7 Launch Prep & Buffer Nov 16 – 25 (MRP:57–63 ✓). P6's rows: final `.deb` packages (aarch64 + x86_64), an APT repository, GPG signing, a download page; the install flow tested from a fresh Raspberry Pi OS through the install command, the wizard, Zigbee discovery and pairing to a live dashboard; the launch content — the Getting Started guide, the release notes, the changelog, docs CI (MRP:232–234 ✓). The dependencies: the 72 h pass blocks the packaging; the install test blocks the launch — "cannot launch without verified install experience" (MRP:322–323 ✓).
- BL: its milestone rows are a historical record; the operative program was the S-10 close as of 08-18 (BL:13 ✓); M15's performance gate (> 500 events/s, < 5 ms p99 state query) needs M13 + M14 (BL:136). Rows the lane flagged for the run — the B3 autostart KillMode defect's in-repo fix (BL:15), the health endpoint not built (BL:27), CMD-LANES at ~4–6-actuator fanout (BL:122) — predate v75 and are checked against the plan of record before any use.
- RA (05-22/06-15): R3–R16 feeding M3.7–M14; SPIKE-DC overdue; the Key-Portability return unrecorded (a backup/restore input, a P6 concern) (RA:500–514).
- TR (09-07, not in git): a personal technical curriculum, not a product plan; its banner names the v66 STATE-OF-THE-PROGRAM as the plan of record (TR:1–2).

**Company** — the strategy of record (SoR), BRAND-G2-EXEC (G2), the Founder Operating Plan (FOP):
- SoR: gates, not dates; P1 name + charter; P2 surface (W2 under the new identity; the story kit; the LICENSE-flip window); the launch moment — the confirmatory IP assignment → the Member consent → the flip with the rename in-tree; fallback, the un-renamed tree if the rename slips past 10-31; the 10-01 quarterly is its gate check (SoR:59 ✓); P3 fleet, exit the Nov-25 runway; FIN-1 (SoR:23–28, 45).
- G2: the draft → FILED (the handles dormant, the evidence log) → the receipt (the spoken side) → B-1 → W2 → the launch moment; the rename WU "never before the 72-hour run's evidence is safe" (G2:22 ✓).
- The conflicts the lane found, ruled here: the `.com` "on FILED" vs "now" → the later amendment governs (D-v79-9), EXECUTED; the outreach Fri vs Mon → D-v79-7 (`mon`) governs; the rename vs the 10-31 fallback → into THE HORIZON RE-CUT; founder hours ≈ 15/wk (SoR) vs ≈ 7/wk (the plan §0) → the plan governs; FOP is an Aug-10 baseline with 13 of 34 checked claims false (FOP-1) → not a source.

**The hub's own grep:** `install flow|fresh pi|installer|apt repo|packaging|distribution|\.deb` over the v66, v73 and v75 plans and the September plan of record → only the CI `.deb` cites (the bench card's builds), no P6 or P7 row. **The finding:** the plan of record ends at the run; P6 and P7 have no rows (OR-HORIZON-UNPLANNED; D-v79-11).

## §3 The determination (why this order)
1. The path first. The run moves with any row that slips (the plan §5's slip rule); rehearsal 1 is the next open row, and Thursday's adoption and Half 2 feed it.
2. The horizon second. It costs no hours of Nick's and no rig time, and a Nov-25 launch needs the install flow built in the three weeks after the run unless it is planned now.
3. The company third, as words and minutes. FIN-1 is due the day the money moved; the strategy pass is D-v79-7's; the B-1 charter and the attorney search are drafts; nothing is public.
4. Research only with an instrument: 7a (tonight), the K-refresh (after Thursday), C-S0-1 (from Monday).

## §4 The record cleaned (asserted inside the splice)
- pm-handoff 84849 → 55643 B. The Open Risks 48539 → 23376 B: 32 older status bullets (26895 B) moved verbatim to `context/handoff/archive/open-risks-status-history-rotated-2026-09-23.md` — OR-NIGHTLY-0902-S31 2 · OR-FAILCHAN 10 · OR-BUS-SILENT-DROP 20; each live entry keeps its class, owner and three newest status bullets and gains a pointer; BUS-SILENT-DROP gains one "Now" line (the counter 13/20); OR-HORIZON-UNPLANNED added. The beats: v77 b5–b7 (6992 B) → `context/handoff/archive/pm-handoff-beats-v77b5-v77b7-rotated-2026-09-23.md`; 10 live after b5. The chain: the v79 b3 segment rotated (159 counted). The conservation: for every line, before − moved + added = after; every moved line found verbatim in its archive.
- The banners: `master-release-plan.md`, `phase-3-milestone-backlog.md`, `research-agenda.md` — `status: CURRENT` → STALE BASELINE, one blockquote under the title pointing to the plan of record and THE HORIZON RE-CUT. The root `Technical_Roadmap_v1.md` and `Founder_Operating_Plan_v1.md` carry their own banners (outside git; untouched).
- **Owned (the hub):** splice B wrote the plan and the DR before the snapshot's cap assert failed (3,525 > 3,490) — against THE GUARDED-SPLICE LAW's order (compute and assert every file, then write). Splice B2 (a fresh name) verified both writes at their anchors, normalized their stamps to the beat's one instrument reading (splice A's), trimmed the snapshot's digest and went on; nothing else had been written. The lesson for v80: a splice writes last.
- FIN-1's page is written outside git (`ClaudeFolder/legal/NexSys-LLC/finance/2026-09-23_FIN-1_member-contribution-record.md`, with a `receipts/` folder beside it): company money and receipts stay out of the repositories.

## §5 The repos
Five repos on `main`, even with `origin/main`, no stash: core `d22a8a4` · bench `fa01cad` · docs `7221ddc` · skills `180375f` at porcelain 0; hivemind `ae3f2a1` + this close card. Core carries four local branches merged into `main` (`claude/confident-williamson`, `m3.2-replay-transition`, `m3.3-backpressure-metrics`, `m3.5a/state-projection-vertical-slice`); the remote has `main` only → `git branch -d` on the card. The `ClaudeFolder` root's loose files (counsel's letter, the search reports, the two August baselines) stay where the record cites them.

## §6 The v80 text
The v79 form is kept: the stable prompt's §1 boot; the laws by name (the laws sentence copied from v79's text byte for byte); the state; the first message; the window; the words; the refusals; the reads beyond §1. Changed: the boot read is the plan §25; the window runs Thu → Mon on §25's table; the one deliverable is rehearsal 1's packet; THE HORIZON RE-CUT is placed on Saturday; the context rule is written into the laws (a beat ≤ ≈70K tokens; long reads by section or by a read-only lane with cites; the close at the sixth beat or before ≈60 % of the context, on a clean record, with the next text).

## §7 Refutable-by
A long-term row the lanes misread (the cites are in §2; any one re-read at the source overrules this audit) · a pointer broken by the rotations (the archive map carries both new rows) · `PREPAY: not-yet` (then FILED waits, and §25's company line moves by the same days).
