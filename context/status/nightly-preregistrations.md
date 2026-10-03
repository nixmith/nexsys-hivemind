<!--
file: context/status/nightly-preregistrations.md
purpose: One row per night for the 03:30 CT nightly — the expected line pre-registered BEFORE it runs (by whom, where), Nick's observed line, the verdict clause by clause, and the reading. Opened v94 beat 2 on Nick's word (Sat 2026-10-03 07:22 CT: "a standing nightly pre-registration file … compounds into the run's evidence and IR-118's story for free"; D-v94-15). Kept at each hub close: the next night's expected row is written before the close; the observed row is filled at the next boot from Nick's `NIGHTLY:` line. The digest's two fleet numbers are REGISTRY reads (`nexsys-bench/tools/runner/nightly_digest.py:151–172`: `adopted` = the now-set's size; `re-seen` = the now-set ∩ the prior read) — neither sees a dark device (IR-118); `avail:` is the unit that will.
audience: the hub (writes the expected row at each close; adjudicates at each boot) · Nick (reads; his one line fills the observed cell) · the run's intake (the evidence trail)
state-type: standing ledger (appended; a row is never edited after its verdict)
status: LIVE — opened v94 beat 2 (Sat 2026-10-03 ~07:5x CT; instrument 2026-10-03T12:54:05Z)
-->

# Nightly pre-registrations (03:30 CT; one row per night)

| Night | Expected (pre-registered by) | Observed (Nick's line) | Verdict | The reading |
|---|---|---|---|---|
| Fri 2026-10-02 | `FAIL boot-health · fleet: 10/9` (the 1b intake audit §2.5, on the configs the sitting left edited) | `FAIL boot-health` — BH-2's forbidden `permit_join_opened` under the 1b key; reproduced on the desk at v92 b5 | REFUTED as written: the digest's arms were predicted, the scenario's FORBIDDEN list was not | the validator lesson's clause (c): a pre-registration of a scenario's verdict reads that scenario's forbidden list; the configs stayed live through the nightly (THE RESTORE RUNS BEFORE THE GAP) |
| Sat 2026-10-03 | `8/9 PASS · fleet: 10/10 · re-seen 10 · 6/6 · 0 forbidden` (v93 b6, the v94 dispatch) | `2026-10-03 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · fleet: 10/10 · re-seen 9 · bench-hero RESTORED ✓ · ON-latency 0.34s` | `8/9` HELD · `10/10` HELD · `re-seen 10` REFUTED (9: Friday's read knew nine ids; the sensor, adopted Fri 06:10 CT, was the tenth — the clause assumed the prior read knew ten) · `6/6` · `0 forbidden` UNREAD (not in the line; not asked) | both fleet numbers are registry reads; the sensor was UNJOINED all night and neither number saw it — IR-118's exhibit at the bytes (D-v94-5, corrected D-v94-12) |
| Sun 2026-10-04 | `8/9 PASS · 1 SKIP(hue-online) · fleet: 10/10 · re-seen 10 · 6/6 · 0 forbidden` (v94 b2, P8 of REHEARSAL 2's packet) — `re-seen 10` whether or not the sensor joined tonight (both reads now know ten ids); the 03:30 boot `formed=0 · relinked=10 · permit=0` | — | — | a `10/10 · re-seen 10` over a dark sensor would be IR-118's second exhibit; the sensor's own state is read in the morning from the API (`lastReported`), never from the digest |
