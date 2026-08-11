<!--
file: context/audits/2026-08-10_s31-aug10-consecutive-fail_micro-read_v51-beat-2.md
purpose: Pre-read filing (law 9) for the Aug-10 s31 consecutive FAIL — hypotheses + predictions FILED BEFORE the bundle pull; §6 adjudicates on Nick's paste at a subsequent beat.
audience: hub; Nick (operator block §5)
status: FILED PRE-READ — §6 EMPTY until the paste arrives
context-of-record: the CLOSED Aug-9 read (context/audits/2026-08-09_s31-confirm-timeout_evidence-read_v50-beat-3.md §6) governs the continuation protocol; its Aug-9 adjudications are UNTOUCHED by this filing.
-->

# The Aug-10 s31 consecutive FAIL — micro-read (v51 beat 2)

## 1. The datum (banked per protocol)

Aug-10 digest line: **7/9 · FAIL command-confirm-s31** (terminal phase mismatch: expected CONFIRMED, read CONFIRMATION_TIMED_OUT) · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency n/a(FAIL) · C4 stays n=4. Bundle: `/home/homesynapse/hs-bench/bundles/command-confirm-s31-20260810T083135Z`. Position discipline HELD at the stamps (usb-reenum 083123Z → timeout-honesty 083129Z → s31 083135Z → settle 083137Z LAST); settle PASS 1/1 — the device answered the very next command; restore ASSERTED (`"bench-hero"` PRESENT); survival line verbatim (pid 106823 remains running); exit path normal, code 1; the left-over-process warning = the named KILLMODE-NOT-YET cost. HANDS OFF the S31 was held (Nick's word + the record).

**The consecutive-FAIL branch of the closed §6 FIRES:** the fresh read runs on the REDESIGNED instrument, POST-GATE (the three candidates named in the closed §6). This micro-read does NOT reopen the closed read; it only classifies tonight's signature with a cheap, read-only bundle pull — pre-filed per law 9.

## 2. The prefix arithmetic (why tonight is not automatically the Aug-9 class)

From the journal paste (America/New_York stamps):

| Command | ULID (visible) | Divergence vs prior |
|---|---|---|
| usb-reenum captured | `01KZNCRHFCCG1KPPVGHYM9YW4C` | — |
| timeout-honesty captured | `01KZNCRQED6PFF321KZQQD6HP2` | char 8 (~6 s later) — NORMAL |
| **s31 FAIL JSON `commandId`** | `01KZNCRQED6…` (ellipsized at 11) | **NONE in 11 chars vs timeout-honesty — same-ms timestamp + same first random char** |
| settle captured | `01KZNCRXD6J2FS9FN9673JGTES` | char 8 vs timeout-honesty — NORMAL |

Every adjacent same-night pair diverges at char 8; the FAIL JSON is the sole outlier. On Aug-9 the corrected read proved that night's FAIL JSON carried the s31 leg's OWN command (7 shared chars — normal divergence). Tonight's 11-shared-char display cannot be an own-command minted ~6 s later unless something else is going on. Ownership lives at the per-leg `resolved.json`, never at journal adjacency or display.

## 3. Hypotheses + predictions (FILED PRE-READ)

- **H-WRONGREAD (leading on the visible evidence):** the s31 terminal read adjudicated a FOREIGN command — the FAIL JSON quotes timeout-honesty's command (a command that is TIMED_OUT by that leg's own design). Prediction: §5-C2's `resolved.json` command_id diverges from `01KZNCRQED6` at or before char 11 (a later mint, ~`01KZNCRV`–`01KZNCRX` range); §5-C4's full-width JSON commandId equals `01KZNCRQED6PFF321KZQQD6HP2` exactly. Consequence: a NEW SIGNATURE — banked as the redesigned instrument's first exhibit (post-gate); the Aug-9 refutation stands untouched (that night's ownership was proven at its own bundle); tonight's FAIL is an instrument artifact, not a device timeout.
- **H-OWN-SAME-MS:** the FAIL JSON is the s31 leg's own command, genuinely minted in the same millisecond as timeout-honesty's. Prediction: C2's command_id begins `01KZNCRQED6` and differs from timeout-honesty's only inside the random block. Consequence: ownership sound — an honest timeout (expected-class: the measured distribution is TIMED_OUT 7/13, so two consecutive tails ≈ 29% of night-pairs, unremarkable) — but a same-ms cross-leg mint is a physical anomaly that routes to the redesign as a mint-timing finding.
- **H-DISPLAY:** the ellipsized journal line misrepresents the id. Prediction: C4's full-width commandId differs from the displayed 11 chars. Consequence: ownership adjudicates per C2 alone; a display-only NOTE.
- **Control (anti-vacuous, arc-19):** C3 must return the settle leg's command_id `01KZNCRXD6J2FS9FN9673JGTES`, matching the journal's captured line — proving the resolved.json route yields real ownership. If the control fails, the read is INCONCLUSIVE — STOP, no adjudication.

## 4. One-word adjudication rules (§6 fills on the paste)

**WRONGREAD** / **OWN-SAME-MS** / **DISPLAY** / **INCONCLUSIVE**. Every branch is gate-compatible: no branch touches the false-CONFIRM clause — the failure direction is honest-red in all of them; C1's one-way door is untouched. No retunes, no re-runs, no suite edits under any outcome (HANDS OFF stands); the redesigned-instrument fresh read stays post-gate regardless.

## 5. The operator block (read-only; self-contained; full paths; paste everything either way ⏺ RECORD)

```bash
# WHERE: the bench Pi (ssh pi) — READ-ONLY, no writes; HANDS OFF the S31 stays absolute
# C1 — bundle contents (expect: a resolved.json among the files)
/usr/bin/ls -la /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260810T083135Z/
# C2 — the s31 leg's OWN command id (the ownership instrument)
/usr/bin/cat /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260810T083135Z/resolved.json
# C3 — positive control: the settle leg's resolved.json (expect command_id 01KZNCRXD6J2FS9FN9673JGTES)
/usr/bin/cat /home/homesynapse/hs-bench/bundles/command-s31-settle-20260810T083137Z/resolved.json
# C4 — the FAIL JSON at full width from the bundle (expect the complete commandId, un-ellipsized)
/usr/bin/grep -r "commandId" /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260810T083135Z/ | /usr/bin/head -10
```

If C2 errors (no file by that name), C1's listing shows what exists — paste it all; the hub re-derives the ownership carrier from the listing rather than guessing.

## 6. Adjudication — EMPTY (fills at the next beat on Nick's paste)

## 7. Gate impact — NONE in any branch

The dry-run's GO stands: the s31 read was already named gate-compatible in every branch at S-9; both Aug-9 and Aug-10 failures are honest-red in every hypothesis. One reading NOTE routed to the skeleton (the settle-instrument redesign item): at the measured distribution (TIMED_OUT 7/13 on a best_effort device), an 8/9 bar will honestly miss ~half of nights at this leg — gate day states the distribution context, exactly as D-2 states the amd64 caveat.
