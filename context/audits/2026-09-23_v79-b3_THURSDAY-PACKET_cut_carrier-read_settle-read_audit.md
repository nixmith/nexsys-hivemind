<!--
file: context/audits/2026-09-23_v79-b3_THURSDAY-PACKET_cut_carrier-read_settle-read_audit.md
purpose: The v79 beat-3 audit — THE THURSDAY PACKET cut (the window's ONE deliverable): the carrier read and the settle bundles intaken at the bytes, the premise corrections they forced in THE THURSDAY ORDER, the scripts' self-test, THE PRIOR-LEDGER GATE's greps, one hub error corrected (the b2 settle claim), and the ONE act.
audience: the hub (the re-mint beat) · Nick (§0)
state-type: beat audit
status: FILED v79 beat 3 (Wed 2026-09-23 ~07:2x CT; instrument 2026-09-23T12:21:57Z).
-->

# v79 beat 3 — THE THURSDAY PACKET, cut

## §0 Verdicts
- **`HIVE: LANDED ae3f2a1`** — at the instrument: HEAD `ae3f2a1` = `origin/main`, porcelain 0, 10 files = the census.
- **`CARRIER: READ-END · settle 60`** — `_scratch/v79/2026-09-23_carrier-read.txt` (5,746 B; the Pi at 2026-09-23T12:08:46Z) and 60 `command-s31-settle` bundles.
- **THE THURSDAY PACKET: DISPATCH-READY** — `context/instructions/2026-09-24_THURSDAY-ORDER_the-three-plugs_operator-packet.md` + four scripts (`context/instructions/2026-09-24_THURSDAY-ORDER_scripts/T0.sh · T1.sh · T2.sh · T3.sh`). Half 1 (T-A → T3) whole; Half 2 (T4 → T8) shaped, cut at the re-mint beat from T3's capture.
- **The order changed at the bytes (the packet §4):** the adoption edits `integrations/zigbee.yaml` (the carrier `!include`s it, line 2) — not the carrier; so **no hero-less or live-basis regeneration** (both carry the include; the carrier's 1,208 B do not move; the `cmp` stays IDENTICAL); **tmux ABSENT** on the Pi → installed at T-A; the Gen4 firmware and Shelly's Zigbee switch at T-A (DEVICE-SET note 4); the load step by the lamp (no dashboard toggle); `~/bench.sh` → `~/nexsys-bench/tools/bench.sh`.
- **The settle bundles correct a b2 claim (hub error, owned):** the suite runs `command-s31-settle` LAST, as the park (`constants.yaml:345–:346`), after the confirm leg — not "immediately before" as the confirm leg's own comment says (stale since the 08-04 suite-position ruling). On the three relay-already-ON nights the settle's turn_off CONFIRMED (08-27 0.365 s · 09-05 0.927 s · 09-18 0.359 s), and the previous nights' parks were CONFIRMED too: the relay went ON between nights, outside the suite, and the confirm leg never establishes OFF before its turn_on. The b2 read's "the settle leg's claim refuted" is withdrawn; IR-51 re-cut to the confirm leg's missing precondition; the S31 read gains its §4 correction; the OR row re-worded.
- **One more S31 datum (a fact, no theory):** 53 of 60 parks CONFIRMED, 7 timed out (07-30, 07-31 ×2, 08-04, 08-14, 08-15, 08-20). On 09-22 the park's turn_off CONFIRMED in 0.133 s, six seconds after the lost turn_on, with A-9 reading OFF in between — the plug answered the next command at once.

## §1 The scripts' self-test (on the device VM, a mock rig: a stub `bench.sh`, a stub `curl`, a scripted log)
T0 → T3 end to end: the window key written once and kept on a re-run; three proposals parsed (a comma inside a manufacturer name included), written in pairing order with their labels, the window kept, the other keys unchanged; the window removed at T3; the capture listed; Bearer 0. The STOP paths: two proposals instead of three → `T2-STOP — nothing written, nothing restarted` (no restart counted, the file's md5 unchanged). Both list styles (quoted strings; bare hex) written in the style the file already uses.

## §2 THE PRIOR-LEDGER GATE — the greps as run (v79 b3)
`grep -n -E '^(- \*\*)?D-[0-9]+' context/audits/2026-09-06_H8a_real-wire_operator-record.md context/audits/2026-09-19_R-5B_operator-record.md | cut -c1-240` → H8-a D-1..D-5 (lines 386 · 415 · 417 · 421 · 423) and R-5B D-1..D-7 (420 · 422 · 424 · 428 · 429 · 431; D-4 is the D-3 addendum's poll summary); each hit and its answer is the packet §5. The S31 row: by deviceId `01KXW1W1RR66GV98D9QDPB4VXY` / entityId `01KXW1W1SBJZERC9MBAMV2DWKE` (the carrier read's entity listing) — no card touches it. The `~/r5b` copy: its lesson is T3's copy-home with the Bearer count.

## §3 The window's plan from here
Tonight: SHAKE, then 7a. Thu: T-A → T3 (Nick) → the re-mint beat (the hub: Half 2 cut from the capture) → T4 → T8 (Nick). BRAND-G2-EXEC's re-cut beside Thursday (before the filing). Fri: the digest read → BENCH-CORE-3 → the outreach on the embargo side. Counsel's draft: the hub's read + the register knockout → sign → FILED → the `.com`.

## §4 Order
hivemind 14 = 7 M + 7 A by explicit paths (computed from porcelain inside the splice); the message file `_scratch/v79/2026-09-23_hivemind_v79-b3_commit-msg.txt`.
