<!--
file: context/audits/2026-09-28_v85-b3_BENCH-CORE-6_cut_prior-ledger-gate_audit.md
purpose: The v85 beat-3 audit — BENCH-CORE-6 cut by BC5's form through THE PRIOR-LEDGER GATE (law 15; #31), with PI-PROBE-3 (a)/(b) and P4 sample 5 pre-registered; the greps against the prior record listed here as the law requires; ONE hivemind card for beats 1–3 (D-v85-19).
audience: the hub · the BC6 guide (§2 is what its EXPECTED lines rest on) · Nick
state-type: audit (a cut through the gate)
status: FILED — v85 beat 3 (Mon 2026-09-28 ~14:2x CT; instrument 2026-09-28T19:24:17Z)
-->

# v85 beat 3 — BENCH-CORE-6 cut through the prior-ledger gate (Mon 2026-09-28 ~14:2x CT; instrument 2026-09-28T19:24:17Z)

## §0 The cut
`context/instructions/2026-09-28_bench-card_BENCH-CORE-6_core-to-40412f9_installDist_operator-session-prompt.md` (18,135 B) by BC5's form (`context/instructions/2026-09-27_bench-card_BENCH-CORE-5_core-to-1f1d1e0_installDist_operator-session-prompt.md`, read whole in two ranges). The deltas, and nothing else: the shas (`1f1d1e0` → `40412f9`; `behind=2` — `git rev-list --count 1f1d1e0..40412f9` = 2: `a5b9e33`, `40412f9`); the outputs path under `_scratch/v85/`; Block 0 reads the Pi's bench sha (`352296d` after the evening packet's Part A — a STOP if not); Block 0b greps today's boot logs (`bench-2026-09-28-*.log`); Block 3's class proof on `StalenessConfig` / `StateStoreSchema` (both at `40412f9`: `ls core/state-store/src/main/java/com/homesynapse/state/ | grep -c` = 2) and its live-order grep gains the state projection's token from the source (`StateProjection.java` :588: `StateProjection {} caught up at position {}; projection.replay.duration_ms={} events_replayed={}`); Block 4 times itself from the running JVM's start (`ps -o lstart=` → `date -d`) for P4 sample 5 at +90 s, prints the true offset, reads +180 s with `stale`/`staleAfter`, and greps the night's three newest boot logs for `permit_join_opened` (BC5 obs. 16). The guide's STATE line refuses a start past 20:15 CT. No BENCH-PULL block.

## §1 THE PRIOR-LEDGER GATE (law 15) — the greps, listed
- The record: BC5's guide notes `context/audits/2026-09-27_BENCH-CORE-5_guide-notes.md` (19,624 B) — `## Observations for the hub` (16) and `## What this card did not verify` read whole; the BC5 intake audit `context/audits/2026-09-27_v83-b4_BC5-intake_the-close_audit.md` grepped `-i 'deviat\|carried\|obs\. \|IR-8[0-9]\|STOP'` (its line 35 carries obs. 1, 2, 3, 5, 6, 10, 12, 13, 15 as the intake's carries; no deviation names a command string).
- Every reused command string (Blocks 0, 0b, 1, 2, the poll, 3, 4) is BC5's, edited only as §0 says; every named witness (`hs-dev-1`, the `pi` alias, `~/bench.sh`, the three plug ULIDs — `scenarios/constants.yaml` :76–:78, the db path by `find`, the digests file, the timer name) re-appears unchanged.
- Carried as EXPECTED: obs. 2 (one poll suffices), obs. 5 (two boots inside Block 3 — the counts are the second boot's), obs. 14 (the `cache_loaded=` and `grep -n` prefixes). Answered: obs. 7 (the state projection's token named — the live-order read now discriminates registry-first from state-first); obs. 16 (Block 4's last line greps the night's boots). Deferred, named: obs. 4 / IR-77 (`config/`'s mtime moving at boot-health boots — not this card's question; the read stays BC5's), the running JVM's classpath (`/proc/<pid>/cmdline` — the chain of sequence + the jar's contents stands), the `energy_meter` 7200-s branch (no energy attribute read).
- BC5's three prior-ledger fixes (obs. 3: `Fast-forward` printed; the BUILD stamp filled — IR-64; the poll finds the same log) are in the strings as carried.

## §2 The pre-registrations (adjudicated at the intake, mismatches first)
| # | Predicted | The inverse (a RESULT, never a STOP) |
|---|---|---|
| PI-PROBE-3 (a) | `registry.projection_live` BEFORE `StateProjection … caught up at position` in the boot log — the gate (IR-61b) | state-first, or one line only |
| PI-PROBE-3 (b) | the TR3's `staleAfter` SET (≈ lastReported + 1200 s) at the immediate read, BEFORE its first post-boot report — the checkpoint holds IR-61's values (BC5 obs. 9) and the gate lets the replayed report find its entity | null with a `lastReported` older than the JVM start = the race persists past the gate; a `lastReported` newer than the JVM start = moot |
| P4 sample 5 (+90 s) | the record's PREDICTED arm — a Gen4 UNAVAILABLE or `age` > 60 s — vs the inverse (all three fresh); samples 1–4 were all clean | either arm is the sample; an UNAVAILABLE queues IR-56's Java unit behind PJ-2 (D-v85-12) |
| the deploy | boot-health 6/6 · 0 forbidden · `network_resumed` channel 20 / PAN 0x774c · formed 0 · relinked 9 · adopted 0 · registry rows 9 · `deployed=40412f9` · `ir61b-class-in-tree=2` · probe ciphered 0 · every 2026-09-28 boot log `permit_join_opened=0` · `staleAfter@180s` 3 set | a STOP by the card's own rules, or a RESULT written into the line |
| Tuesday's nightly (D-v85-7) | on (core `40412f9`, bench `352296d`) once BC6's line lands: `8/9 PASS · fleet: 9/9 · re-seen 9`, 0 forbidden; the S31 floor as Monday's | a STOP tonight → (`1f1d1e0`, `352296d`), the same line |

## §3 Layer 2 — re-executed and not
Re-executed: `git rev-list --count 1f1d1e0..40412f9` and the two commits' subjects; the two class files at `40412f9`; `StateProjection.java` :588's format and `projectionId.value()`; the plug ULIDs in `constants.yaml`; BC5's card whole (two ranges) and its notes' §Observations and §did-not-verify whole. Not re-executed: the Pi (nothing touched); `date -d "$(ps -o lstart= …)"` on the Pi's coreutils (GNU on Raspberry Pi OS; Block 4 prints the parsed start, so a parse failure shows as an empty `start=` and the offsets read from `+<n>s`, which the guide writes as read).

## §4 ONE card for beats 1–3 (D-v85-19)
The evening packet's Part C re-cut to 17 = 9 M + 8 A (`_scratch/v85/2026-09-28_hivemind_v85-b1b2b3_commit-msg.txt`; the b1b2 message file retired unrun); Part E names this card. The census at the splice's end: 9 M + 8 A at porcelain.
