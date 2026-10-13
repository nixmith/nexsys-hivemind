<!--
file: context/planning/2026-10-12_v110_decision-record.md
purpose: v110's decision record — Nick's words verbatim (§1: his first message and his 7,725-B addendum), the facts at the instrument (§2), the decisions by beat (§3 →). v110 opened Mon 2026-10-12 18:17 CT on v110's text (`handoff/2026-10-12_v110_dispatch-text.md`); its order is the addendum's §E.
audience: the v110 hub · every hub after it (a v110 ruling is cited by its D-v110-n) · Nick
state-type: decision record
status: LIVE — v110 beat 2 (Mon 2026-10-12 ~20:5x CT; instrument 2026-10-13T01:54:34Z): dry-run #1's Monday half intaken; the window open; D2 20:04 CT; D-v110-11..18. Prior: v110 beat 1 (Mon 2026-10-12 ~18:3x CT; instrument 2026-10-12T23:35:17Z): the boot; BENCH-BOOT-1 INTAKEN ACCEPT; its landing card handed; the addendum filed.
-->
# v110 — decision record

## §1 Nick's words, verbatim
**18:17 CT, the first message** (after v110's text, pasted from `handoff/2026-10-12_v110_dispatch-text.md` line 9 on): `TIME: 18:17 CT HIVE: LANDED e6a7ecc CAPACITY: Mon 3 hours · Tue 5 hours BENCH-BOOT-1: RETURNED context/audits/2026-10-12_BENCH-BOOT-1_return.md 8017 staged=6 tree=a17a7754d4c12f27ad48d9f14ebdb1e5ccb8f9e9 HORIZON-1: RETURNED context/research/2026-10-12_HORIZON-1_long-horizon-critical-review_return.md 127779 (md5 f29982af6575bf117e3ea2a8fa857e7a), with the v109 hub's pass-1 analysis: context/audits/2026-10-12_v109-post-close_HORIZON-1_pre-intake-analysis.md 12571 (md5 54e22d18fd188d1b8e6adc3c5996e4e5) DRY-RUN-1 (Mon): not yet — it starts ≈ 19:00 CT`

**18:18 CT, the addendum** (7,725 B, md5 `4f730c7bb4adedaf652b0ce040668a97`; the copy `_scratch/v110/b1/nick_addendum_2026-10-12.md`), verbatim:

## A. Tonight — the dry-run comes first
- **18:55:** the v109 session hands me dry-run #1 (`instructions/2026-10-12_DRY-RUN-1_BACKUP-1-K-4-F1-A4-R4_operator-session-prompt.md`, pasted whole into a fresh conversation).
- **You own everything after that:**
  - the intake of `DRY-RUN-1 (Mon): <line>`;
  - any stop or deviation the guide session raises;
  - D2 tomorrow at ≈ 19:00 CT, with IR-56's read added to D2's card (your item (ii)) before then.
- **Iterate carefully.** Anything I do at the rig is one action, one line back. Nothing is added to tonight's packet (v109's rule: no rider without its own dry-run).
- **Beat 1 (BENCH-BOOT-1) can start now.** If it isn't done by 18:50, park it at a clean point and resume after the line.
- **The `/sessions` volume is still full** (1.5 MB free at 17:18 CT; IR-181); HORIZON-1 lost its link at 16:50.
  - If the guide session can't reach my computer: the packet is self-contained, so I carry on and bring the line back.
  - If you can't reach it (`SHELL: down`): say so first, and follow your text's IR-181 line.

## B. HORIZON-1 — intake, then iterate to one result
- **Its intake is its own beat**, after beat 1 and after the dry-run's line — not part of beat 1. Two layers as always.
- **The v109 analysis is where layer 2 starts:**
  - F1 sharpened against INV-ES-04, with one correction;
  - F25, F28, F19/F29, F21, F12, the name filing and F13 confirmed;
  - F31 plausible;
  - Home Assistant's `not_triggered` confirmed by fetch;
  - its additions A1–A7.
- **Reading:** the return's body whole; Appendix B by finding id only.
- **Time-critical first:**
  1. **PI-2's coordinator:** a firmware probe in PI-2's card before Tue Oct 20; reflash 7.4.5.0 if it reports v14 (analysis §2, item 2). Confirm the coordinator is in hand; if a purchase is needed, put it to me as a decision.
  2. **GATE-2:** its evidence first (the landed `timeout_causes` classifier over the S31 corpus), then my stance (N3) by Oct 22.
  3. **SCHEMA-1:** chartered for Nov 2, not Oct 20 (§2, item 4).
  4. **N1** (counsel: the filing receipt; the two instruments) is mine this week. Remind me once.
- **Fit to capacity:** HORIZON-1's 12 sessions plus RUNTIME-1 (§C) must fit my ≈ 30 h/week until December, against THE HORIZON's rows. They replace rows; they don't pile on.
- **Be as critical of the v109 analysis as of the return.** Where you disagree, say why, with evidence.
- **The iteration:** v109 was pass 1; you are pass 2. By your close:
  - the HORIZON-1 ruling: each finding ACCEPTED, CORRECTED or DEFERRED, into register rows;
  - the session map fitted, with the first charters cut;
  - the outline of pass 3.
- **Pass 3 is one strategy of record, v2, by Dec 1.** It replaces the scattered strategy files rather than adding one, and holds:
  - the thesis and the moat, restated;
  - the one-way doors, with their dates;
  - the R&D program;
  - the 2027 skeleton the December ruling chooses among;
  - the language/runtime ADR (§C);
  - the process and skills plan.

## C. Languages and runtime — the v109 hub's position (test it; don't adopt it)
- **The design problem:** where does a second language earn its cost?
  - Costs: a second toolchain and CI; a boundary to design, version and test; a second review surface for one founder plus AI lanes.
  - Gains: footprint and startup (cheaper boards, faster recovery); latency without GC; memory safety where the alternative is C/C++.
- **The evidence now:**
  - **None of HORIZON-1's bottlenecks is a language problem:** F1 is a pragma, F18 an O(n) scan, F27 sequential probes, F25/F26 protocol handling, F28 firmware. A rewrite fixes none of them, and it discards the frozen, golden-tested surface the claims rest on.
  - **Java is already memory-safe** (the NSA/CISA guidance lists it beside Rust). Rust's safety edge is over C/C++, not over Java.
  - **The JVM's real costs** are footprint and startup (`-Xms512m -Xmx1536m` under `MemoryMax=2G` means a 4 GB Pi in practice), plus the watchdog's missing transport (F6: a stock JDK can't send `sd_notify`'s datagram).
  - **The strongest case for Rust is the board:** at fleet scale on a 1–2 GB board, a JVM is tight. That is why memory is the first measurement.
  - **Cheaper fixes to verify:** JDK 25 LTS (FFM is final, so `sd_notify` via libsystemd; the AOT cache for startup; compact object headers), heap tuning, and GraalVM native-image as a measured option.
  - **Nothing measured on the Pi exists on record** for memory, startup or boot-to-ready. Measure before deciding.
- **Policy:** at most one native language, and it is Rust; no new C/C++. It belongs only here:
  - (a) **the appliance layer's agents**, and only where proven parts don't fit. Try first: systemd's hardware watchdog, RAUC or Mender A/B updates, TUF-signed metadata. Prior art: Bottlerocket's Rust agents and the `tough` TUF library.
  - (b) **a second radio path (MATTER-1).** The reference stacks are C++ (connectedhomeip, OpenThread), and `rs-matter` exists in Rust. Always a separate process behind the IntegrationAdapter seam, the way Home Assistant runs its Matter server and Thread border router.
  - (c) **firmware for a device of our own**, if we ever make one (embedded Rust, e.g. Embassy).
- **Java stays** for the event store, the automation and explain engines, availability (R2) and simulation (R1). Probably also the fleet engine, which reuses the event model.
- **The boundary is a process, not FFI:** a Unix-domain socket with a versioned schema. The sidecar publishes into the log as an adapter, and can crash without taking the record down. FFM only for tiny calls like `sd_notify`.
- **Revisit when:**
  - measured memory or startup blocks a target board or a buyer's BOM;
  - MATTER-1 says yes;
  - we design our own device;
  - we would otherwise write C/C++.
- **Timing:** no new-language code before the run, and nothing in the pilot's path.
- **RUNTIME-1:** research plus one Pi measurement, post-run or on a spare card (never the run's). It measures:
  - memory, startup and boot-to-ready on JDK 21 vs JDK 25 (with the AOT cache) vs native-image;
  - the FFM watchdog;
  - the appliance-OS assembly options;
  - Matter's process model;
  - the BOM threshold at which a smaller runtime pays.
  
  Output: the language/runtime ADR.
- I have hands-on Rust and C, so a native component has a reviewer.

## D. The process — lighter, now
- **Adopt the v109 analysis §4 rules at once:**
  - one fact, one place;
  - decision ids for choices only;
  - one audit per return;
  - render or raise the caps that cost refusals;
  - a retirement rule for laws.
- **At your close, report the measures:** the share of commits that touch the spine, and my cards this window.
- **PROCESS-2 designs the rest**, including the skills (`nexsys-project-manager`, `nexsys-coder`) and the next orchestrator prompt. Skill changes come to me as proposals.
- **Make every token count:** fewer, denser artifacts, and one clear act at a time.

## E. Order and guardrails
- **My suggested order** (change it with a reason):
  1. beat 1, BENCH-BOOT-1;
  2. the dry-run's line;
  3. (ii) D2's card with IR-56, before Tue 19:00;
  4. the HORIZON-1 intake (§B);
  5. (iii) KIT-STORAGE after the dry-run's F1 number;
  6. (iv) the unit cards LIVE;
  7. (vi) BC10's card (Fri);
  8. the deliberation and the outline (§B–§D);
  9. THE CLOSE (v111's text).
  
  (v) the device-coverage charter folds into HORIZON-1's map. (vii) housekeeping and (viii) DOCS-3a go to v111 unless a quiet beat appears.
- **Standing:**
  - Java closed by rule until the freeze;
  - no deploy but `37f05a9`;
  - no device purchases before the pilot households answer;
  - ≤ 6 beats;
  - your text's laws stand.

## §2 The facts at the instrument (banked; no act)
- **The boot (23:18:21Z = 18:18 CT):** the shell UP; `/sessions` 9.8 G, 9.0 M free (IR-181; `TMPDIR=/tmp` on every call). The read-set ≈ 35 KB. HEADs: core `176adad` · docs `e2a5844` · hivemind `e6a7ecc` (`??` ×3: the BENCH-BOOT-1 return, the HORIZON-1 return, the v109 pass-1 analysis) · skills `e9a77a8` · bench `ceb08c5` + 6 staged on `bench-boot-1/run-and-delegation`; push counts 0; no locks. Check 9 28/28; Check 12 0 · 0 · 0; `render_state.py --check` 7 MATCH. PASS.
- **BENCH-BOOT-1's return** (8,017 B; md5 `e7f044c92e29…`): the lane's `write-tree` `a17a7754d4c12f27ad48d9f14ebdb1e5ccb8f9e9` = the hub's own; the four suites on the staged tree 57/0 · 42/0 · 54/0 · 42/0 (the hub, device shell, Python 3.10.12); row 7 `1 0 0 0`; RED re-run 42/12 (12, not 13: the hub's copy kept the unit file, so r9 is green); the delegation against the hub's own stubs (seven scenarios) holds — the audit §2.
- **The hub's own hazard:** `git write-tree` on the device left `nexsys-bench/.git/index.lock` (the no-delete rule); renamed `.git/stale-index-lock-v110b1-231126Z`; the card deletes it by exact path.
- **HORIZON-1** returned 127,779 B (md5 `f29982af…`) with the v109 hub's pass-1 analysis (12,571 B; md5 `54e22d18…`); both `??`, neither read this beat (its intake is its own beat — Nick's §B).

## §3 The decisions (beat 1, Mon 2026-10-12 ~18:3x CT)
- **D-v110-1 — the boot:** PASS as §2; `HIVE: LANDED e6a7ecc` = the instrument.
- **D-v110-2 — the order is Nick's addendum §E:** beat 1 BENCH-BOOT-1 → the dry-run's line → (ii) D2's card + IR-56 (before Tue 19:00) → the HORIZON-1 intake (its own beat; two layers; the v109 analysis is where layer 2 starts and is read as critically as the return) → (iii) `KIT-STORAGE:` on F1's number → (iv) the unit cards LIVE → (vi) BC10's card → the deliberation and pass 3's outline (§B–§D) → the close (v111's text; the two measures). (v) folds into HORIZON-1's map; (vii) and (viii) go to v111 unless a quiet beat appears. ≤ 6 beats; Mon 3 h · Tue 5 h.
- **D-v110-3 — the window's deliverables:** ONE, named at beat 1 — BENCH-BOOT-1 intaken at the bytes and its landing card in Nick's hands (MET at b1); and by the close, Nick's §B — the HORIZON-1 ruling into register rows (ACCEPTED / CORRECTED / DEFERRED per finding), the session map fitted to ≈ 30 h/week with the first charters cut, pass 3's outline.
- **D-v110-4 — BENCH-BOOT-1 INTAKEN ACCEPT** (`audits/2026-10-12_v110-b1_BENCH-BOOT-1_intake_two-layer_audit.md`): Unit A whole; Unit B at six of seven paths (D2: `nightly_digest.py` already reconfigures at `:708`). §6's row-7 line was cut on a false premise (each suite's own output as the only cp1252 hazard; T3c's children `export.py`/`grader.py` print `→`/`—`) — the miss is the charter's; the lane obeyed §3's table. **D1 → IR-183 widened** (the tool half: two reconfigure lines in each tool's `__main__`; rides the next bench lane — NOT a rider on this landing, which has no dry-run of its own and would change the recorded tree). D3, D4, D7 ACCEPT; D5, D6 INFO. **F1 → IR-185** (the unit cards' BLOCK 3: the legacy `bench.sh stop` BEFORE `systemctl --user enable`, then the delegated `start`); **F2 → IR-186** (`reset-failed` after a refused delegated restart — the unit cards and BC10's rollback carry the line); **F4 → IR-187** (the unit's environment has no login shell; `java` on the launcher's PATH is a premise the Oct 19 sitting's health read tests); F5 INFO.
- **D-v110-5 — the landing card** (`_scratch/v110/b1/card_bench_land.txt`; the message `2026-10-12_bench_BENCH-BOOT-1_commit-msg.txt`, 3,475 B, 0 trailers) in Nick's form (D-v109-12): the one deletion by exact path; `write-tree` asserted = `a17a7754…` before the commit and `HEAD^{tree}` = it after; `porcelain=0` the last read; ff-only onto `main`; the push. The unit is NOT enabled by the card; the Oct 19 sitting enables it (F1's order). BC10's pull names the landed sha beside BP9 + BP10.
- **D-v110-6 — the lesson** (pm-lessons 2026-10-12): a lane's staged tree is read on the device by `git archive <tree-sha>`; `git write-tree` and every other index-writing verb are Nick's shell's — the device cannot unlink the lock it makes.
- **D-v110-7 — the v109 analysis §4 rules ADOPTED at once** (Nick's §D, his words): one fact, one place · decision ids for choices only · one audit per return · render or raise the caps that cost refusals · a retirement rule for laws. Applied from this beat: this DR records choices only (the facts are §2's, once); one audit per return; a cap that refuses a true line is raised in `render_state.py`'s CAPS by a named edit, never worked around. PROCESS-2 designs the rest (the two skills and the next orchestrator prompt); skill changes reach Nick as proposals.
- **D-v110-8 — the two measures at the close** (Nick's §D): the share of this window's commits that touch the spine, and the count of cards handed to Nick. The counters open: cards handed = 1 (the bench landing).
- **D-v110-9 — staged this beat (13):** the BENCH-BOOT-1 return (its audit's beat) · the audit · this DR · the DONE archive — new; the register (IR-183's cell; IR-185..187) · the charter (status) · v110's text (status) · pm-lessons · `state.yaml` · the snapshot · the brief · pm-handoff · the chain archive — modified. The HORIZON-1 return and the v109 analysis stay `??` until their intake beat.
- **D-v110-10 — the splice's own miss, and the bench landing banked:** splice_1 wrote the spine, then died at `--check` — `beat()` renders only the two digests; the brief's status, held and words regions are `--write`'s, and splice_1 never ran `--probe` on its temp state (the v109 b4 form did). The held region had grown 1,069 B (the brief would be 13,398 B > 12,288): splice_2 trims the rows (the research row to a pointer at this DR; the bench and hivemind rows to their facts) → `--probe` → `--write` → `--check` 7 MATCH. The law, into the next splice form: `--probe` on the temp state before `beat()`, every time. **`BENCH: LANDED 6a40a10`** (Nick, 18:36 CT): the card's reads as asked — `HEAD^{tree}` = `a17a7754…`, ff onto `main`, pushed, `porcelain=0`; the desk's `bench.sh selftest: 42 check(s), 38 failure(s)` is the return §6's known Windows-desk reading (`bash` = the WSL launcher), not the tree's (42/0 on the device at the same tree) — the card asked the desk for a suite the return said the desk cannot run; the hub's miss, no act. BC10's bench pull names `6a40a10`. (recovery Mon 2026-10-12 ~18:3x CT; instrument 2026-10-12T23:38:59Z)

## §3b Beat 2 (Mon 2026-10-12 ~20:5x CT): dry-run #1's Monday half INTAKEN; the window OPEN; D2 named 20:04 CT; the deviations and the findings; Tuesday's order
- **D-v110-11 — D0b AMEND** (19:39 CT, on the guide's stop): the sqlite3 CLI's `.backup` loops 100-page steps and restarts on every concurrent commit — on the Core's store it never finishes; the one-step Python backup (one `sqlite3_backup_step(-1)`, a consistent WAL snapshot, writers unblocked) replaces it; one `method:` line; everything else byte-identical; the guide tested both ways and stub-dry-ran the amended card. The Pi's copy took 28 s; md5 both sides.
- **D-v110-12 — W1-CONTINGENCY yes** (20:01 CT): P2″ failed as written (the plain warm relaunch exited 99 at 43.5 s); the one allowed restart was made as warm as it could be — a read-only `cat` of the store and its WAL (31 s; the cache 943 → 1,296 MB on a 4-GB board), then one `bench.sh start`: the registry live 20.4 s after `Loaded`, `network_resumed`, `running (pid 12899)`; the window opened 20:03:53 CT; the Core was down ≈ 12 min.
- **D-v110-13 — DRY-RUN-1 (Mon) INTAKEN** (`audits/2026-10-12_v110-b2_DRY-RUN-1-Mon_intake_two-layer_audit.md`; the guide's notes and the raw outputs copied into `audits/` verbatim): P0″ HELD · P1″ EXPECTED · P2″ FAILED → the contingency booted · P3″ PASS (the IT ran; 7,971 ms → 4 ms) · BACKUP-1 Part 0 DONE · the D0 halves of P6″–P9″ RECORDED · the rest at D2. K4 at `176adad` (the EXPECT's `2a54145` stale) ACCEPT.
- **D-v110-14 — the findings:** IR-148's cell (the deterministic reproduction; the 9.6-s warm margin at 941 MB, ≈ 92 k events/s against ≈ 95.6 k rows/day → `37f05a9`'s warm boot overruns the gate ≈ Oct 22; the fix `af46e11` + `6a03403` in every Friday candidate); IR-188 (`.backup` on a live store — BACKUP-1's form is the one-step copy); IR-189 (the launcher pre-warm); IR-190 (the packet form for dry-run #2); IR-191 (the confirmation-timeout share on the desk copy).
- **D-v110-15 — D2 at 20:04 CT Tuesday** (the window opened 20:03:53 CT; the packet's ≈ 19:00 assumed an earlier opening): the amended D2 card — IR-56's read-only lines (D-v85-12's row from LOG1 after `launched`; D-v101-32's condition) and the slots FILLED (`bench-2026-10-12-210302.log 11406 1877415`) — is the paste Nick brings to the guide (`_scratch/v110/b2/D2_card_IR56_filled.txt`; stub-dry-run before and after the fill); the packet file's D2 section carries the same text; D2's line goes to v111 (v110 closes before 20:04 — D-v110-18). The D1.txt slots are VOID.
- **D-v110-16 — the rollback target, for Friday's go/no-go (the hub's recommendation; Nick rules Friday):** the run's rollback binary must be a post-REGISTRY-COLD-1 build (`ba08dd8` at the oldest), never `37f05a9` — its warm margin expires ≈ Oct 22 and its cold boot fails today; Sun Oct 18's binary-rollback rehearsal carries the pre-warm (D-v110-12's block) and reads `projection_live − Loaded` as the margin. BC10's one cold start (IR-113/123's reading) is also IR-148's "after" — the card names it.
- **D-v110-17 — `KIT-STORAGE:` asked Tuesday, in H10 form** (F1's number is in: volume does not gate — 941 MB against 101 GB free, ≈ 48 MB/day; the SD's read speed does — 30 MB/s on the pre-warm, the cold-boot replay's floor; PI-2 Tue Oct 20): (a) order the SSD + adapter now for PI-2 — the one measurement of SD vs SSD on the same binary, and a cold-boot-tolerant second Pi; (b) SD only, the SSD deferred to the pilots' answers; (c) not yet, until Friday. The hub's rec: (a) — refutable by the pilot-class answer "the household board is SD-only".
- **D-v110-18 — Tuesday's order** (Nick's §E; ≤ 6 beats; his 5 h): the b1 and b2 cards first (desk pastes; b2's gate reads b1's subject) → b3 the HORIZON-1 intake (its own beat; two layers; the v109 analysis read as critically as the return) → b4 (iv) the unit cards LIVE on the re-cut (IR-185..187; the stub-ssh dry-run against `6a40a10`) + (vi) BC10's card drafted (BACKUP-1 one-step; the deploy sha per the Fri word; the cold start = IR-148's "after"; the evidence lines by id) → b5 the deliberation (§B–§D) and pass 3's outline → b6 THE CLOSE with v111's text and the two measures (cards handed so far: 2 — the bench landing, b1; b2's makes 3). D2's line (≈ 20:10 CT) → v111 beat 1.
