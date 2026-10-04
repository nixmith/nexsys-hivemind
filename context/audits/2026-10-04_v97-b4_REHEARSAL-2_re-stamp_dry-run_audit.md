<!--
file: context/audits/2026-10-04_v97-b4_REHEARSAL-2_re-stamp_dry-run_audit.md
purpose: v97 beat 4 — REHEARSAL 2's packet RE-STAMPED on its date-bound lines only (each edit listed), the fresh dry-run of its harvest on the corpus of record (the v94 b2 script re-pointed; the output beside), the pre-registrations re-printed IN ORDER with the core they are read on, and the 17:25 paste line.
audience: Nick (§3 is the act; §2 the readings he will see) · the v98 hub (§2 is the adjudication order) · the guide (never reads this; the packet is its whole world)
state-type: beat audit (one beat)
status: FILED — v97 beat 4 (Sun 2026-10-04 ~15:5x CT; instrument 2026-10-04T20:58:22Z)
-->

# v97 beat 4 — REHEARSAL 2: the re-stamp, the dry-run, the pre-registrations

## §0 The rule and the instrument
The packet's SUBSTANCE is unedited (D-v96-11; the v97 text's REFUSE line): the hub edited ONLY its date-bound lines — HIVE-CLEAN-3's §2 rows (:3, :6, :14) and the hub's own greps (`tonight|Saturday|Sat |≈ 26 h|≈ 30 h|5b0e20c|0232c69|Sunday|v96|sat1003`), each an anchor matched exactly once, every edit below. The Pi's core sha `5b0e20c` is UNCHANGED in every card (BC8 is Monday; its two card mentions stand; three new mentions name the core the pre-registration is read on); no bench sha is named in the packet (`0232c69` absent before). `tonight` (:11, :65, :139) is relative and true on Sunday — left. Before: 24,825 B; after: 25,742 B.

## §1 The edits (date-bound lines only)
- :3 the sitting's day (the census §2 :3): `purpose: REHEARSAL 2's packet (THE WEEKS AHEAD §10 Sat 10-03; the v94 dispatch's ONE DELIVERABLE)` → `purpose: REHEARSAL 2's packet (THE WEEKS AHEAD §10 Sat 10-03 → SUNDAY 10-04, D-v95-25; the v94 dispatch's ONE DELIVERABLE)`
- :6 the status line (the census §2 :6): `:6 status` → `re-stamped v97 b4 … Was: …`
- :9 the heading's day: `# REHEARSAL 2 — the sensor's join · a restart under declared loads · IR-56's power-cycle (Sat 2026-10-03, 1…` → `# REHEARSAL 2 — the sensor's join · a restart under declared loads · IR-56's power-cycle (Sun 2026-10-04, 17:30 → ≤ 21:00 CT; re-stamped …`
- :13 the adjudicating hub: `**The pre-registrations (adjudicated by the hub Sunday, never by the guide):**` → `**The pre-registrations (adjudicated by the hub at v98, Sunday night, never by the guide):**`
- :14 P1's dark span 26 h → 54 h (the census §2 :14) with D-v95-13's pre-registration beside it (the dispatch's order; D-v95-13 said 'no packet edit' for Saturday — the span crossed the arm since): ``AVAILABLE stale=False lastReported=2026-10-02T16:19:36Z` (IR-121: ≈ 26 h dark and still AVAILABLE — the ex…` → ``avail=? stale=False lastReported=2026-10-02T16:19:36Z` (≈ 54 h dark since Fri 11:19 CT; THE HUB'S PRE-REGISTRATION OF RECORD is D-v95-13…`
- :19 P6's 'Sunday': `(the Java unit is queued Sunday)` → `(the Java unit is queued after J2)`
- :21 P8's nightly (the first after a Sunday sitting is Monday's): `**P8** (Sunday 03:30's nightly, read by the hub)` → `**P8** (Monday 03:30's nightly — the first after the sitting — read by the hub)`
- :37 EXPECT (P1)'s sensor line — the guide records either avail; no STOP (the span-bound reading): ``SENSOR avail=AVAILABLE stale=False W=None lastReported=2026-10-02T16:19:36Z` (the IR-121 exhibit; a newer …` → ``SENSOR avail=AVAILABLE|UNAVAILABLE stale=False W=None lastReported=2026-10-02T16:19:36Z` (either `avail` is RECORDED — D-v95-13 expects …`
- the output directory of every card and the return path (card 0's `mkdir -p` creates it): `_scratch/v94/sat1003/reh2 ×12` → `_scratch/v97/sun1004/reh2 ×12`
- :139 the intaking hub: `The hub (v96) intakes at the bytes; nothing else is asked tonight.` → `The hub (v98) intakes at the bytes; nothing else is asked tonight.`

## §2 The fresh dry-run on the corpus (`_scratch/v97/reh2/reh2_dry-run.txt`; the script `reh2_dry-run_v97.sh` = the v94 b2 script with `P=` re-pointed at the re-stamped copy; the corpus `_scratch/v93/sensor/bench-2026-10-02-124849.log.after-rejoin`, 176,487 B)
Result: DRY RUN COMPLETE; no FAIL/INVALID/UNKNOWN; the byte-mark watch reproduces the :37 relink at `MARK=0 → i=1` and reads 0 new lines at `MARK=EOF`; every heredoc `bash -n` OK with the slots filled; every ULID KNOWN; every IEEE in the record; non-ASCII in code blocks 0. Against the v94 b2 output (the same corpus): DIFFERENT — the lines that differ are read below.
    === dry run 2026-10-04T20:59:05Z · packet 25742 B · corpus 176487 B ===
    --- 1. pj_valid (tools/bench.sh:91-95) on every permit-join argument in the packet
    VALID 254 'REH2 SNZB06P24 join'
    --- 2. every ULID in the packet is 26 Crockford chars AND in constants.yaml remembered-ulids
    KNOWN 01KXW1W1SBJZERC9MBAMV2DWKE
    KNOWN 01M3DM74SGEY7RXVDYSM4PK2XA
    KNOWN 01M3DPGF6Y4YXNXDHBW38ZEX2G
    KNOWN 01M3DPKN9WD9B88Q4SVDMSBJVS
    KNOWN 01M3Y4YA6YSYQWVE9ET8FT4HWQ
    ulids: 5
    --- 3. every IEEE in the packet is in the record (nexsys-hivemind, grep -rl count)
    0x4CE175B4C0700000 in 31 files
    0xA4C13814CE41FFFF in 16 files
    0xACEBE6FFFEF25A2C in 24 files
    0xACEBE6FFFEF733DC in 25 files
    --- 4. bash -n on every heredoc body in the packet
    EOF_0 bash -n OK
    outer bash -n OK
    EOF_1A bash -n OK
    outer bash -n OK
    EOF_1C bash -n OK
    outer bash -n OK
    EOF_2A bash -n OK
    outer bash -n OK
    EOF_2B bash -n OK
    outer bash -n OK
    EOF_2C bash -n OK
    outer bash -n OK
    EOF_3A bash -n OK
    outer bash -n OK
    EOF_3C bash -n OK
    outer bash -n OK
    EOF_4A bash -n OK
    outer bash -n OK
    heredocs: 9
    --- 5. the 1c watch loop RUN on the corpus, sleeps removed: (a) MARK=0 must break at i=1 on the pre-existing :37 relink; (b) MARK=EOF must run all 24 and read 0 new lines
    MARK=0 → broke at i=1 · new-sensor-lines=1 proposed-new=0 adopted-new=0 keyfail-new=1 closed=0
    MARK=176487 → broke at i=24 · new-sensor-lines=0 proposed-new=0 adopted-new=0 keyfail-new=0 closed=0
    --- 6. the 3c watch loop RUN on the corpus for G4-1 (0xACEBE6FFFEF733DC), MARK=0 and MARK=EOF
    MARK=0 → broke at i=1 · g41-new-lines=48 · the sleep arithmetic: 115
    MARK=176487 → broke at i=18 · g41-new-lines=0 · the sleep arithmetic: 30
    --- 7. the harvest greps on the corpus (each token the log carries at least once, or the count is declared 0 and expected)
    launched=1 projection_live=1 formed=0 resumed=1 relinked=11 sensor-relinked=1 opened=1 closed=0 keyfail=1 summaries=470
    12:49:01.691 [hs-sub-registry_projection] INFO  c.h.l.RegistryProjectionSubscriber -- registry.projection_live: devices=10 entities=10 position=849602
    link device=0xACEBE6FFFEF733DC frames=219 last_lqi=216 last_rssi_dbm=-46 last_link_at=2026-10-03T00:39:02.480901367Z
    link device=0x4CE175B4C0700000 frames=125 last_lqi=216 last_rssi_dbm=-46 last_link_at=2026-10-03T00:38:59.414954851Z
    link device=0xACEBE6FFFEF25A2C frames=118 last_lqi=188 last_rssi_dbm=-53 last_link_at=2026-10-03T00:39:04.080484582Z
    link device=0xA4C13814CE41FFFF frames=0 last_lqi=- last_rssi_dbm=- last_link_at=-
    --- 8. the python state parsers against a JSON of the documented shape (SYNTHETIC — the live shape is the BENCH-CORE-3 card's :63, read at BC6b)
    avail=AVAILABLE stale=False on=True W=2.4 lastReported=2026-10-02T16:19:36Z
    avail=AVAILABLE stale=False lux=35.2 occupied=True lastReported=2026-10-02T16:19:36Z
    2 rows; 1 AVAILABLE; unavailable: ['DHE40F']
    --- 8b. permit_join_closed exists at source (the corpus has 0): 16 files
    --- 9. the bench verbs the packet uses exist in tools/bench.sh usage
    verb restart: present
    verb state: present
    verb api_token: present
    verb permit-join: present
    46:  ln -sf "$log" "$CUR"
    --- 10. no em dash or non-ASCII inside any code block

## §3 The pre-registrations IN ORDER, with the core they are read on (the v98 hub adjudicates in this order; the guide never adjudicates)
1. **D-v95-13's sensor row FIRST** (card 0; read on `5b0e20c`): `availability=UNAVAILABLE` + `stale=false` — the 25-h `SILENCE_TIMEOUT` arm (D-v95-10); the sensor dark ≈ 54 h since its Leave Fri 11:19 CT (`lastReported=2026-10-02T16:19:36Z`). The J1 pre-verification §4, verbatim: "`AVAILABLE` at P1 REFUTES row 2's arm for this device and is J1's first finding: the lane's plan then names why (the seed's instant refreshed at a boot; the device's PowerSource read as mains with pings succeeding — impossible off-network; or the evaluation not reached) before any write. Either reading changes no card tonight."
2. **D-v94-25's P1/P6** — P1 the clone `5b0e20c`, `key-lines=0 · adopt=10 · warn-lines=0`, ten entity rows, the Hue `UNAVAILABLE` (IR-112); P6 G4-1's power-cycle chain inside 90 s (`device_announce` or `child_join`/`SECURED_REJOIN` → `device_relinked`) and `AVAILABLE` with a newer `lastReported` at +120 s — or THE SILENT RESUME (no line in 90 s, the API still on 3a's instant): IR-56's shape on a plug, RECORDED.
3. **Card 1's chain** — IR-117's "always leaves": a `child_join` or a bare `device_announce` for `0xA4C13814CE41FFFF` inside 120 s after the mark, then `device_relinked` (the same id `01M3Y4YA6KMH7JDEF5YMMJ3YND`; no new adoption) → `reporting_reapply` → `reporting_configured`; arm (ii) `JOIN: none` NAMED — the sitting continues. IR-115's third sample: `keyfail-new` 0 or 1, RECORDED.
4. **IR-56's sample 6** = P6 above (the first power-cycle sample on a plug; samples 1–5 were app restarts).
5. **`re-seen 10` either way** (P8; Monday 03:30's nightly, read by the hub): `8/9 PASS · 1 SKIP(hue-online) · fleet: 10/10 · re-seen 10 · 6/6 · 0 forbidden` whether or not the sensor joined — a dark sensor under `10/10 · re-seen 10` is IR-118's second exhibit (`avail:` is the line that would tell; the soak-night unit).
THE RESTORE RUNS BEFORE THE GAP: this packet writes no config (card 4's `restore-check` expects `key-lines=0 · warn-lines=0`, the carrier's md5 equal to card 0's); the window closes itself at 254 s; nothing stays live across the sitting's end — the lesson is satisfied by construction and card 4 proves it.

## §4 The act (17:25)
Nick pastes the file `context/instructions/2026-10-03_REHEARSAL-2_sensor-join_restart-under-loads_IR-56-power-cycle_operator-session-prompt.md` WHOLE (from the file on disk — this re-stamped version) into a FRESH Cowork conversation with `ClaudeFolder` connected; the guide opens 17:30; ≤ 21:00; the return at `_scratch/v97/sun1004/reh2/REHEARSAL-2_guide-return.md`; Nick's one line `RETURNED <path> <bytes>` → v98. No hardware act before 17:30.
