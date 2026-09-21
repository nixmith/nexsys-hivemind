<!--
file: context/audits/2026-09-21_v78-b1_boot-and-intake_audit.md
purpose: The v78 beat-1 audit — the boot at the instrument (the read-set with its bytes; the five HEADs; the twelve preflight checks, one line each) and the two-layer intake of Monday's first message (`R5B-3:` and `IDS:`), with the two reconciliations the preflight ordered (Check 12: seven executed packets; Check 6: the coder-handoff pointer) and the dispatch text's verbatim check.
audience: the v78 hub · Nick (the §0 verdict) · the v79 hub
state-type: audit (filed; never edited after the beat)
status: FILED v78 beat 1 (Mon 2026-09-21 ~07:5x CT; instrument 2026-09-21T12:51:15Z)
-->

# v78 beat 1 — the boot and the intake

## §0 Verdict
`R5B-3:` — the pre-registration `8/9 PASS · 1 SKIP(hue-online)` CONFIRMED verbatim on the first night with the vacuum off and the S31 unloaded. `IDS:` — `automations.ids.yaml` PRESENT on the bench card and VERIFIED durable at the bytes (the ULID's own timestamp is BENCH-CORE-2's first boot; `last_seen` is the nightly's restore restart). The preflight 12/12 after two reconciliations in this beat. The pasted dispatch text is byte-identical to the filed block. Forward work lawful.

## §1 The boot (the instrument first: `Mon Sep 21 12:37:42 UTC 2026`; CT = UTC−5)
The read-set (bytes as printed): the stable prompt 13,017 · `pm-handoff.md:8` 2,044 + the v77 b7 block 2,080 · `PROJECT_SNAPSHOT.md` 3,475 · `OPERATOR-BRIEF_for-Nick.md` 11,789 · the plan §21 7,365 + §2 3,406 · the v77 DR §3 by `cut -c1-300` (≈2,800 of 4,785) · pm-lessons' two newest entries by `cut -c1-420` (≈850) — ≈46.8 KB against the 45 KB budget. Owned: over by ≈1.8 KB; the trim was the two `cut`s, chosen so the decisions' ids and recs and the two lessons' names were read and their bodies were not. The five HEADs in one call: core `13d439f` · hivemind `3bbb1c0` · skills `180375f` · bench `fa01cad` · docs `7221ddc`; porcelain 0 ×5; unpushed 0 ×5; no locks. Every HEAD matches the record (the plan §21.1; the snapshot).

## §2 The preflight (one line per check)
- Check 1 PASS — the snapshot's `last-verified` = `2026-09-20 (v77 beat 7` = the handoff's.
- Check 2 PASS — both spines name v77 b7; the plan of record resolves at `context/planning/2026-09-15_v75_PROGRAM-PLAN_the-six-weeks-to-the-72-hour-run.md`.
- Check 3 PASS — the snapshot cites core `13d439f` = HEAD.
- Check 4 PASS — the backlog exists; 29 DONE rows; the last cited sha `1aa809d` resolves as a commit.
- Check 5 PASS — Open Risks at `:101`; the section's newest date 2026-09-20.
- Check 6 STALE → RECONCILED — `coder-handoff.md:22`'s NEXT WU pointer named MEASURE-2b (LANDED `a6b56d6`) with LINK-READ as "the second session"; re-cut to LINK-READ (the Java slot's next; D-v76-10; D-v77-5 done). Line 8 is stamped at b2 with LINK-READ's dispatch.
- Check 7 PASS — 21 `MODULE_CONTEXT.md` files (22 `include(` lines in `settings.gradle.kts`); none under 1.5 KB.
- Check 8 PASS — `cross-agent-notes.md` is the RETIRED pointer stub (ACTIVE: 0 since 2026-07-27).
- Check 9 PASS — 28/28 identical at the bytes (the three SOURCE trees' per-file md5 vs the session's synced copies; the same 28 lines).
- Check 10 PASS — 101 cited `.md` paths; 96 resolve by basename in a repo's `git ls-files`; the 5 unresolved are pattern strings (`YYYY-MM-DD_topic.md`, `weeks/YYYY-WNN_…`, `months/YYYY-MM_month.md`, `*_orchestrator_session_prompt.md`, `handoff/*_session_prompt.md`), not paths.
- Check 11 PASS — `RealCoreFixture`, `AutomationIdentityCompanion`, `CompanionAutomationIdentityStore`, `FileAutomationIdentityCompanion`, `AtomicYamlWriter`, `StandardExplanationService` resolve in core (`git ls-files`); `NO_DIRECT_FILESYSTEM_IN_CORE` at 2 hits in `HomeSynapseArchRules.java`.
- Check 12 STALE → RECONCILED — 12.1: seven `context/instructions/*.md` carried a live `status:` (H8-a LIVE · R-5B LIVE · MEASURE-2b, FE-115, KO-2, AUTO-ID-1 DISPATCH-READY · BENCH-CORE-1 LIVE) with every lane CLOSED, ACCEPT or DONE in the v77 record → each set to EXECUTED with the prior line kept after `Was:`, bodies untouched; 12.2 = 0 (one LIVE prompt, v67); 12.3 = 0.

## §3 The intake, two-layer
**`R5B-3:`** — Nick's paste (`ssh pi`, `hs-dev-1`, `12:29:01Z`): `2026-09-21 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · fleet: 6/6 · re-seen 6 · bench-hero RESTORED ✓ · ON-latency 0.16s`, beside the 09-20 line (`7/9 · FAIL command-confirm-s31 · bundle …T083121Z · 1 SKIP(hue-online) · fleet: 6/6 · re-seen 6 · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)`), which matches the record's `R5B-2:` field for field. Layer 1: the pre-registration (`8/9 PASS · 1 SKIP(hue-online)`, the b7 close) is met verbatim; the fleet floor `6/6 · re-seen 6` holds; `ON-latency 0.16s` is the S31's command→confirm latency on a real ON-edge — the first such datum since 09-18. Layer 2: `nexsys-bench/scenarios/command-confirm-s31.yaml:4` — the suite's last leg (`command-s31-settle`) leaves the relay OFF, so the card's S31 is OFF and unloaded after the nightly as before it; `tools/nightly.sh:22–:23` — the nightly restarts Core twice (quiesce, then restore). **Adjudication:** the S31 FAIL class (09-12, 09-18, 09-20) is consistent with the vacuum's overcurrent trips as its cause — one PASS night is consistent, not proof; OR-NIGHTLY-0902-S31 stays OPEN with the instrument continuing: `R5B-4:` (Tue) and `R5B-5:` (Wed) on the same state (nothing changed on the card); a FAIL on the unloaded S31 refutes the vacuum cause → its own row and instrument (the bundle's `api-captures.json` against the journal). No act on the S31 before rehearsal 1's packet.

**`IDS:`** — `-rw-rw-r-- 1 homesynapse homesynapse 253 Sep 21 04:31 /home/homesynapse/hs-bench/config/automations.ids.yaml`; `head -8`: the header comment (`engine-managed (Doc 07 §4.1; AMD-93 §2.3). Do not edit.`), `schema_version: 1`, `automations: bench-hero: id: 01M2ZR8EG9FW8CYJP6SJ9DBBHE`, `last_seen: 2026-09-21T08:31:29Z`, `triggers: '0': 01M2ZR8EGD0PZNS9SPGFKGN83B`. Layer 1: present at the path AUTO-ID-1 wires (`configDir.resolve("automations.ids.yaml")`, the plan §21.5), one automation (bench-hero) and one trigger, 253 B — the b7 say-back error (`ids.yaml present` predicted before a read) is now a read. Layer 2 (the hub's own instrument): a ULID's first ten characters are its mint time — `01M2ZR8EG9…` decodes to `2026-09-20T15:51:49.001Z` and the trigger's `01M2ZR8EGD…` to `…:49.005Z` = BENCH-CORE-2's first boot on `13d439f` (the record: `c819a02 → 13d439f at 15:52Z`); `last_seen 2026-09-21T08:31:29Z` = the nightly's restore restart (04:31 EDT; the timer 04:30). The same id after two restarts and bench-hero's ABSENT interval (the quiesce removes it; the 30-day retention keeps the row) is the durability AUTO-ID-1 was written for, seen on the card, not in a test — the F-1 shape (every restart mints new ids) refuted on the bench card. (For scale: the S31 entity's `01KXW1W1SB…` decodes to 2026-07-19T02:04Z, the fleet's first adoption.) Not re-executed from here: the digest line's bytes on the Pi and the 09-21 quiesce-evidence file — Nick's paste is the reading of record.

## §4 The dispatch text
The pasted text (8,327 B, md5 `42bce6b2f3acef9c328985578e7649f9`) is byte-identical to `context/handoff/2026-09-20_v78_dispatch-text.md:11–27` (the fenced block). That file IS the verbatim record; its `status:` is set EXECUTED here (no duplicate file). The terminal paste beside it is saved at `_scratch/v78/2026-09-21_v78_dispatch-text_as-pasted.txt`.

## §5 THE ONE DELIVERABLE (Mon → Wed)
THE THURSDAY PACKET DISPATCH-READY through THE PRIOR-LEDGER GATE by Tuesday night — the `adopt_devices` edit, the constants re-mint (the ULIDs read AFTER the adoption, never predicted), the hero-less variant, the scenario in tmux — with LINK-READ chartered at b2 and intaken beside it, and rehearsal 1's packet cut behind it. Thursday 09-24 is v79's hardware day and opens on cards, not on authoring. The rest of the week's rows (the strategy pass, VERDICT-VOCAB-1, PELTON-READY, `HARNESS-PLUG:`, `SHAKE`, `FOP: apply`, AMD-100's card, the H8-b read) serve or follow it and are taken in §HELD's order.

## §6 The beat's edits
pm-handoff (line 8 rotated: the v77 b6 segment → the archive as rotation 150; the b1 block; the OR-NIGHTLY-0902-S31 status line) · the snapshot (the chain; the digest) · the brief (§NEXT; §HELD rows; §DONE) · `coder-handoff.md:22` · `context/handoff/2026-09-20_v78_dispatch-text.md` status · the seven instruction files' status · this audit. Census computed from porcelain inside the splice: hivemind 14 = 13 M + 1 A.
