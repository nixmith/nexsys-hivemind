<!--
file: context/audits/2026-09-23_v79-b1_boot_intake_PELTON-ruling_audit.md
purpose: The v79 beat-1 audit — the boot at the instrument (the read-set with its bytes; the five HEADs; the twelve preflight checks, one line each), the intake of Nick's first message at the bytes (the two landings, the 09-22 digest line, the opinion), the new Open Risk the 09-22 line fired, and the pointer to THE PELTON RULING (filed as its own file).
audience: the hub · Nick (§0)
state-type: beat audit
status: FILED v79 beat 1 (Wed 2026-09-23 ~00:5x CT; instrument 2026-09-23T05:55:41Z).
-->

# v79 beat 1 — the boot; the intake; THE PELTON RULING

## §0 Verdicts
- **The boot:** `date -u` 2026-09-23T05:31:58Z (Wed 00:31 CT); the read-set 41,459 B ≤ 45 KB (§1); the HEADs = the record plus one landing (core `d22a8a4` = the IR-40 + IR-44 card); porcelain 0 ×5, ahead 0 ×5, no lock; the preflight 12/12 PASS (§2).
- **`CORE: IR40 d22a8a4` + `CI: d22a8a4 green` (Nick's note 1) → the closure counter 13/20.** At the instrument: core HEAD `d22a8a4` = `origin/main`, porcelain 0; the card's own output (porcelain 6, `staged: 6 (expect 6)`, the trailer gate passed, `6 files changed, 365 insertions(+), 1 deletion(-)`, one create = the plan test, `d2cddb1..d22a8a4`). CI green is Nick's word; the run was not re-read from here.
- **`HIVE: LANDED 1c81051`** (v78 b5): `staged: 15 (expect 15)`, four creates as ordered, `9b92e4e..1c81051`; HEAD = `origin/main`, porcelain 0.
- **`R5B-4:`** — the 09-22 line, read off the tail Nick pasted (the ssh at 05:25:19Z): `7/9 · FAIL command-confirm-s31 · bundle /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260922T083122Z · 1 SKIP(hue-online) · fleet: 6/6 · re-seen 6 · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)`. The pre-registration (`8/9 PASS · 1 SKIP(hue-online)`) is REFUTED on the second night with the S31 OFF and unloaded, and the v77 b7 pre-registration (unchanged from b6) FIRES ("a fourth `FAIL command-confirm-s31` (09-12, 09-18, 09-20 so far) → the intermittent becomes its own OR row with an instrument") → **OR-S31-INTERMITTENT** opened (§3). Nick's note 2 says R5B-4 is not done; the hub reads the line from his paste, and the morning read re-reads it beside R5B-5.
- **`R5B-5:` not yet** — the nightly runs 03:30 CT (08:30Z); the tail was read at 05:25Z. Handed at its time as the morning read (§3's first instrument rides with it).
- **`ERIK: RETURNED`** — `ClaudeFolder/PALOKI search opinion 20260922.pdf` (298,406 B) + `ClaudeFolder/TM Search_PALOKI_(Word Search)_20260918.docx` (2,072,953 B); no class word given — Nick asked the hub to analyze and decide. **CLASS: CLEAR, RULED on the letter's sentence (D-v79-1); the filing scope 9 + 42 (D-v79-2, REC).** The ruling: `context/strategy/2026-09-23_PELTON-RULING_{{NAME}}_CLEAR.md` (the test clause by clause; the enclosure read row by row — three silences, asked in the email; RS-13's pre-registration HELD). The letter verbatim: `context/research/2026-09-23_PELTON-OPINION_{{NAME}}_letter-verbatim.md`. The act: `context/strategy/brand-program/2026-09-23_ERIK-EMAIL_{{NAME}}_filing-go-word.txt`.
- **`SHAKE:` · `BOX: B2` · `7A:`** — not yet (Nick's note 2).
- **The dispatch text:** the paste = the filed block of `context/handoff/2026-09-23_v79_dispatch-text.md` (lines 11–23, 6,222 B, 13 lines) at 11 anchors, first line to last (sampled, not md5) → status EXECUTED (PASTED).
- **The window's ONE deliverable:** THE THURSDAY PACKET (the dispatch's block 2), from beat 2. Beat 1 carried the intakes and the ruling Nick asked for first.

## §1 The read-set (bytes)
The session prompt 13,017 · `pm-handoff.md:8` 1,954 + the v78 b5 block 2,393 · `PROJECT_SNAPSHOT.md` 3,499 · `OPERATOR-BRIEF_for-Nick.md` 11,921 · the v78 DR §3 4,275 · the plan §23 4,400 → **41,459 B**. Beyond §1, each sent by a block: the preflight reference by range; PELTON-READY (7,439); RS-13 §0 and two greps; the v67 b6 ruling by grep; the 09-09 packet §1–§3 and A2; the 09-09 email; the 08-28 card §3; the LLC packet (one grep); `splice_lib_v1.py` (6,569; md5 `d6780d13…` asserted).

## §2 The preflight (one line per check)
- 1 PASS — the snapshot's `last-verified` = `2026-09-23 (v78 beat 5` = the handoff's.
- 2 PASS — both spines name v78 b5; the plan of record resolves.
- 3 PASS — the snapshot cites core `d2cddb1` + the IR-40 card; HEAD `d22a8a4` is that card.
- 4 PASS — the backlog: 29 DONE rows; the last cited sha `1aa809d` resolves as a commit.
- 5 PASS — Open Risks at `:103`; the section's newest date 2026-09-21.
- 6 PASS — `coder-handoff.md:22` names the Java slot's candidates (LINK-READ-2 = IR-45 after Thursday; MC-ROTATE-1 between units); the choice is this window's.
- 7 PASS — 21 `MODULE_CONTEXT.md` files; the smallest 8,710 B.
- 8 PASS — `cross-agent-notes.md` is the RETIRED stub (0 active).
- 9 PASS — 28/28 identical at the bytes (the sorted per-file md5 lists hash to `c1c386f6…` on both sides).
- 10 PASS — 103 cited `.md` paths; 98 resolve by basename in a repo's `git ls-files`; the 5 unresolved are pattern strings.
- 11 PASS — `SqliteEventStore`, `HomeSynapseCore`, `StandardAvailabilityTracker`, `ZclIngestionUnit`, `LinkReading`, `SqliteEventStoreTimeRangePlanTest`, `HomeSynapseCoreStartupFailureTest` resolve (`git ls-files`); `idx_events_event_time` in 5 `.java` files, `SCAN_BATCH` in 4.
- 12 PASS — 12.1 0 · 12.2 0 · 12.3 0.

## §3 OR-S31-INTERMITTENT — opened
The FAIL nights on `command-confirm-s31`: 09-02 (OR-NIGHTLY-0902-S31), 09-12, 09-18, 09-20 (the vacuum on the S31), 09-22 (the S31 OFF and unloaded since 09-20 ~15:42Z; 09-21 passed on the same state). The load is refuted as the sole cause; no mechanism is on record, and none is allowed before the reads (arc 28). **The instrument, in order:** (1) the 09-22 bundle's `verdict.txt` and its file listing, read in the morning beside `R5B-5:` (one command); (2) the bundle's `api-captures.json` against the journal's zigbee lines at 08:31Z (the hub's read card after (1)); (3) LINK-READ's reading on the S31 once LINK-READ deploys to the bench card after THE THURSDAY ORDER. It bears on `HARNESS-PLUG:` (rehearsal 1). It gates nothing on Thursday: the adoption is three new plugs, and the S31 stays OFF and unloaded (the fence).

## §4 Not re-executed · hub errors owned
Not re-executed: the CI run on `d22a8a4` (Nick's word); the 09-22 bundle (the rig is not reachable from here); the register after the report's data date (counsel, email item 3). Hub error owned: none this beat.

## §5 Order
hivemind 12 = 6 M + 6 A by explicit paths (computed from porcelain inside the splice); the message file `_scratch/v79/2026-09-23_hivemind_v79-b1_commit-msg.txt`.
