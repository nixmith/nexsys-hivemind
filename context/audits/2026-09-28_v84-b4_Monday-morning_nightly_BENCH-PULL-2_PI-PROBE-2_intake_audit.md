<!--
file: context/audits/2026-09-28_v84-b4_Monday-morning_nightly_BENCH-PULL-2_PI-PROBE-2_intake_audit.md
purpose: The v84 hub's beat-4 audit — Monday morning's three acts intaken at the bytes: the nightly's line against its pre-registration (MATCH), BENCH-PULL-2 (the Pi at `9fa2382`; IR-76 satisfied), PI-PROBE-2 (CONFOUND — IR-83's immediate null was the old checkpoint's); the Java and bench lanes handed (Acts 4–5); W-SKILLS-10 pulled forward on Nick's word and cut.
audience: the hub · Nick · v85
state-type: audit (filed once; never edited)
status: FILED — Mon 2026-09-28 ~06:0x CT (instrument 2026-09-28T11:07:07Z)
-->

# v84 beat 4 — Monday morning

## §0 Verdict
THREE ACTS LANDED, ALL AS PRE-REGISTERED OR RULED. (1) The nightly MATCHES: `2026-09-28 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · fleet: 9/9 · re-seen 9 · bench-hero RESTORED ✓ · ON-latency 0.37s` — the first nightly on core `1f1d1e0` with BH-2, run on bench `58b5b45` (the Pi's clone at read time, porcelain 0); BH-2's forbidden entry is inside boot-health (`boot-health.yaml` :67), so 8/9 PASS is 0 `permit_join_opened` hits; D-v83-24 stands. (2) BENCH-PULL-2: `58b5b45` → `9fa2382` fast-forward, porcelain 0, `bh2=3 fresh=1 v72h=1`, `selftest: 41 check(s), 0 failure(s)`, `verify72h selftest: 25 check(s), 0 failure(s)` — IR-76 satisfied for the VERIFY-72H-A landing; EXPORT-1's `export` verb is on the Pi. (3) PI-PROBE-2: `VERDICT CONFOUND (report at or below the checkpoint) ckpt=384196 tr3_last=383919` — TR3's last `state_reported` (event_time 1790549598535246 µs = 2026-09-27T22:53:18.535Z, the record's stamp to the millisecond) sat 277 positions below the state projection's checkpoint (384196, written 22:57:29.935Z; head 384198); the new core replayed two events and never re-derived TR3's `staleAfter`; the null BC5 read was `e96dce8`'s checkpoint value. D-v83-25's ruling CONFIRMED; IR-83 UNOBSERVED, not refuted; IR-61b's gate stays (D-v84-14). `HIVE: LANDED 84ecb17` banked at the porcelain (18 files; 0 trailers).

## §1 The readings, filed
`context/audits/2026-09-28_NIGHTLY_digest-read.txt` (703 B; the last three digest lines — 09-26 the S31 FAIL night, 09-27 and 09-28 PASS) · `context/audits/2026-09-28_BENCH-PULL-2_outputs.txt` (329 B) · `context/audits/2026-09-28_PI-PROBE-2_outputs.txt` (694 B; every subscriber checkpoint in the backup: `automation_engine` 384198 · `command_dispatch_service` 370844 · `integration_supervisor` 370844 · `pending_command_ledger` 384197 · `registry_projection` 370844 · `state_projection` 384196). All three copied byte-for-byte from `_scratch/v84/`.

## §2 The morning's dispatches (Nick's hands; the cap two lanes + hands)
Act 4 the Java lane (LOCK-1 then IR-61b; one Claude Code session on `1f1d1e0`; LOCK-1's §14 paste) · Act 5 the bench lane (VERIFY-72H-A2; a fresh Cowork session on `9fa2382`; the charter's §5 paste). Both handed 06:0x CT; both unattended; the returns owed at `context/audits/2026-09-28_LOCK-1_return.md`, `…_IR61b_return.md`, `…_VERIFY-72H-A2_return.md`. W-SKILLS-10 (`context/instructions/2026-09-28_desk-lane_W-SKILLS-10_the-fold-of-the-week_charter.md`, 11,492 B) DISPATCH-READY at the first free slot (D-v84-19).

## §3 Layer 2 — re-executed and not
Re-executed: the three output files' bytes and the greps that read them (the PASS line count 1; `VERDICT CONFOUND` 1; `Fast-forward` and both selftest lines present); the two epoch-µs stamps converted at the instrument (Python, UTC); `boot-health.yaml` :67 (BH-2's forbidden entry is a boot-health row); the hivemind landing at porcelain. Not re-executed: the Pi (read by Nick's blocks, not by the hub); the backup's row content beyond the four queries; the lanes (not yet returned).
