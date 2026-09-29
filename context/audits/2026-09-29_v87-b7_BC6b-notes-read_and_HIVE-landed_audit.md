<!--
file: context/audits/2026-09-29_v87-b7_BC6b-notes-read_and_HIVE-landed_audit.md
purpose: v87 beat 7 — the v87 hivemind card banked at porcelain (`52ff1bb`; the gated form's first run); BENCH-CORE-6b's second layer — the guide's one line and its notes (28,186 B) read against the b6 audit and the outputs file; the three observations that carry; the threshold arithmetic resolved at source; THE WEEKS AHEAD row 2 corrected.
audience: the v87 hub · the v88 boot (by §0)
state-type: audit (a second-layer intake)
status: FILED — Tue 2026-09-29 ~18:0x CT (instrument 2026-09-29T23:00:23Z)
-->

# v87 beat 7 — the card landed; BC6b's notes read

## §0 Verdict
**`HIVE: LANDED 52ff1bb` BANKED** (24 = 13 M + 11 A at the card's own count; trailers 0). **BC6b's notes: CONSISTENT with the outputs file and the b6 audit; three observations carry** — the TR3's unrecorded 8.4 W load (`TR3:` asked), the nightly line's missing `forbidden` field (IR-105; v88's pair text corrected), the card's stale header text (the EXPECTED lines governed; a transform rule for W-SKILLS-10). The 1200-s `staleAfter` offsets are the design of record; the plan's row 2 carried a superseded number and is corrected.

## §1 The card (Layer 1 Nick's transcript; Layer 2 the instrument)
`24` · `staged: 24 (expect 24)` · `[main 52ff1bb] hivemind: v87 beats 1–6 — …` · `24 files changed, 631 insertions(+), 67 deletions(-)` · `df106bc..52ff1bb main -> main`. Re-executed: hivemind HEAD `52ff1bb`, porcelain 0, ahead 0, `git log -1 --format=%B | grep -ci 'Co-Authored\|Claude-Session'` = 0.

## §2 The guide's one line vs the outputs file
`BENCH-CORE-6b: deployed 40412f9 (pinned) · boot-health 6/6 · rows 589703→590038 · relinked 9 · plugs@+121s A/A/A · plugs@+180s A/A/A · staleAfter@180s 3 set · ir61b-class-in-tree=2 · live-order registry-first · TR3-immediate set · probe ciphered=0 · boot-logs permit_join_opened=0 · nightly 2026-09-29 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · fleet: 9/9 · re-seen 9 · bench-hero RESTORED ✓ · ON-latency 0.31s · outputs … 8587 · notes … 28186` — every field is in the outputs file as the b6 audit read it; `rows 589703→590038` from B0 (`589703`) and B3 (`590038`). MATCH.

## §3 The notes against the b6 audit (28,186 B; 19 observations; none a STOP)
Consistent: the record section (the outputs file's sha256 read back after every block; the card byte-identical to the folder's copy; the clocks — Pi-local = UTC−4 throughout); per-block verdicts (all match); the readings (a) registry-first by 16 ms with its two caveats, (b) the TR3 SET with the checkpoint-provenance caveat, (c) sample 5 inverse at +121 s, (d) ciphered 0 on 589,760 rows, (e) the boot-log gate; obs. 2 the fence held and the clone is detached (a future card's `ref=` reads `HEAD`); obs. 3 the two prior-ledger fixes hold; obs. 6 the new-Core evidence chain (`StalenessConfig.java` and `StateStoreSchema.java` absent from `1f1d1e0`, present in `40412f9` — `ir61b-class-in-tree=2` is not satisfiable by the old jar); obs. 12 the row rates (~72/min since BC5; the DB 292 MB, +2.2 MB/h); obs. 13 the build 16 executed / 44 up-to-date.
| Carries | What | Disposition |
|---|---|---|
| obs. 10 | the TR3 reads `on=True W=8.4` on both sample lines; BC3/BC4/BC5 read `W=0.0`; no card placed a load | `TR3: <what is on it>` asked; the run's loads planned after the word; the cadence reading (b6 audit §3) re-read with the load known |
| obs. 17 | the nightly digest line has no `forbidden` field; the pre-registration's "0 forbidden" was not readable from it | IR-105 — a pre-registration names the source line of every field (IR-93's class); v88's pair text: the digest line's fields + boot-health's `0 forbidden` from the nightly's bundle |
| obs. 18 | stale header text carried from BC6 ("MONDAY EVENING"; "352296d by BENCH-PULL-3"; "Tuesday's nightly … 352296d") | the EXPECTED lines governed; the card as run is the record, not edited; W-SKILLS-10: a transform lists every replaced token and greps the result with `-i` |
| obs. 7 (ii) | the WITHOUT-gate order on `1f1d1e0` is readable from `bench-2026-09-29-043131.log` | a one-line read-only act in v88's block 1 (`grep -n 'registry.projection_live\|caught up at position'` on that log) |
| obs. 4 | `config/` mtime moved by the boot-health boot (the fourth in a row) | IR-77's standing read; nothing new |

## §4 The threshold arithmetic, resolved at source
Every plug's `staleAfter − lastReported` = 1200.000 s (the TR3 at +20 s; both Gen4s at +121/+180 s). Source (`8deef4b`): `core/device-model/.../PowerMeter.java:52` `EXPECTED_REPORT_INTERVAL = Duration.ofSeconds(1200)`; `EnergyMeter.java:57` 7200 s; the rule from `context/audits/2026-09-27_IR61_independent-review.md` (a capability's interval = a margin × the maximum interval the core configures — 2 × 600 s for ActivePower); `nexsys-bench/scenarios/constants.yaml:499–500` `stale-power-meter-s: 1200 · stale-energy-meter-s: 7200`. THE WEEKS AHEAD §7 row 2 read "`power_meter` 180 s from the measured cadences … G4-2's 12.5-min silence flagged at 3 min" — the pre-review proposal — corrected in place this beat. Consequence for the run's attestation: a metered silence flags at 20 min (power) / 2 h (energy); a silence inside the margin (G4-2's 12.5 min) is by design not stale.

## §5 Not re-executed
The Pi's lines (the teed file); the guide's desk `git ls-tree` read (obs. 6) — consistent with the hub's own `git ls-files` at `8deef4b` (both files tracked).
