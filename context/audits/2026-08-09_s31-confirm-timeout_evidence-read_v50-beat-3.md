<!--
file: context/audits/2026-08-09_s31-confirm-timeout_evidence-read_v50-beat-3.md
purpose: Evidence read for the Aug-9 nightly divergence — command-confirm-s31 FAIL (terminal phase mismatch: expected CONFIRMED, read CONFIRMATION_TIMED_OUT) at position 8, the first position-8 FAIL after three consecutive position-8 passes. Per-hypothesis predictions FILED HERE BEFORE the bundle read (law 9 + the adopted digest protocol clause 5). The bundle at the Pi is the discriminating instrument; §5 carries the one-word adjudication rules.
audience: the hub (adjudicates on the bundle RECORD); Nick (runs the read-only bundle pull)
state-type: evidence read (pre-read predictions + post-read adjudication slot)
status: FILED-PRE-READ 2026-08-09 (v50 beat 3). HANDS OFF THE S31 — no retunes, no re-runs, no suite edits ride this read under ANY outcome.
governing-rulings: the adopted digest protocol clause 5 (v49 beat 3 — "a divergence is an intake, not a crisis: an evidence read with predictions filed FIRST, no retunes, HANDS OFF the S31") · law 9 (instrument-first; predictions before the read) · the B3.3 "position-8 FAIL escalates to HUE-RESET" clause is ADJUDICATED DISCHARGED-AND-INAPPLICABLE here: it was scoped to the FIRST post-deploy verification fire, which PASSED (v46 beat 5), and the HUE-RESET contingency itself was OVERTAKEN by the HA-5 ruling (the Hue lamp is dead, kept as the W-3 exhibit; replacement adoption is post-gate) — the hue leg's standing SKIP is governed by HA-5, and tonight's s31 FAIL is governed by the digest protocol.
-->

# The Aug-9 s31 Confirm-Timeout Evidence Read (predictions filed pre-read)

## §1 The intake evidence (the digest + journal, received 2026-08-09 in-chat; quoted before any bundle access)

1. **The digest line:** `2026-08-09 quiesced AUTO floor: 7/9 · FAIL command-confirm-s31 · bundle /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260809T083132Z · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)`.
2. **The FAIL line (journal, width-truncated):** `[FAIL] command-confirm-s31 — terminal phase mismatch: expected CONFIRMED, read CONFIRMATION_TIMED_OUT — {"data":{"commandId":"01KZJTBXKXW5` — the JSON cuts off at exactly those 12 ULID characters.
3. **The immediately-preceding leg** (timeout-honesty-no-change, PASS 2/2, bundle `…083126Z`) printed `captured command_id = '01KZJTBXKXW5FYE9D83EPZNAJX'` — a command whose terminal phase is CONFIRMATION_TIMED_OUT **by that leg's own design** (it commands an unconfirmable target, waits out the window, and asserts the honest TIMED_OUT phase + no state change).
4. **The clue this read turns on:** the FAIL JSON's visible 12 characters `01KZJTBXKXW5` are byte-identical to the timeout-honesty command's first 12. ULIDs mint 10 timestamp chars + 16 random; two DISTINCT commands minted ~6 s apart (the s31 bundle stamp is `083132Z`, the timeout-honesty stamp `083126Z`) should differ within the first 10. A 12-char match across distinct commands requires same-millisecond minting plus 2 matching random chars — vanishingly unlikely. The truncation means this is STRONG-NOT-CONCLUSIVE; the bundle's full JSON decides.
5. **Position discipline HELD:** bundle-stamp sequence boot-health `083051Z` → (hue SKIP) → timeout-absent `083057Z` → supersession `083103Z` → identify-honest `083105Z` → usb-reenum `083120Z` → timeout-honesty `083126Z` → **s31 `083132Z` (position 8)** → settle `083133Z` (LAST). The s31 leg fired ≈ +41 s after the suite boot's `zigbee.network_up` (`04:30:51.396` local ↔ `083051Z`-era) — INSIDE the healthy +40–55 s band the B3.3 ruling measured. **This FAIL is NOT the closed boot-window class; the closed s31 thread stays closed; this is a new read.**
6. **The device answered the very next command:** `command-s31-settle PASS 1/1` (settle command `01KZJTC3JMR0MCM5XEJMBQPBZC`, bundle `083133Z`) — the S31 relay was alive and confirming within ~1 s of the FAIL adjudication.
7. **Infrastructure behaved as designed:** honest FAIL, exit path normal code 1 (`Result=exit-code / ExecMainStatus=1` is the wrapper's honest red, not a crash), quiesce evidence copied INTO the failure bundle, restore ASSERTED (bench-hero PRESENT), survival line verbatim (`Unit process 100370 (java) remains running after unit stopped`), app alive at pgrep. The left-over-process warning at start (`Found left-over process 96068`) is the expected KillMode=process artifact from the Aug-8 survivor (KILLMODE-APPLY remains NOT-YET; this journal noise is a named cost of NOT-YET, on the record).

## §2 The hypotheses — predictions FILED BEFORE the bundle read

**H-I — instrument mis-read (command-identity collision in the runner's terminal-phase read).** The s31 leg adjudicated the WRONG command's terminal phase — the timeout-honesty leg's command (which is TIMED_OUT by design) — via a stale captured variable, a mis-scoped latest-command query, or a failed s31 command mint falling through to the prior command. Supporting texture already visible: the s31 FAIL path printed NO `captured command_id` line of its own (every passing leg printed one; the `settle_command_id` that follows belongs to the settle leg).
*Predictions:* (a) the bundle's failure JSON `commandId` == `01KZJTBXKXW5FYE9D83EPZNAJX` EXACTLY; (b) the bundle/event slice shows either NO fresh s31 command minted this leg, or a fresh s31 command with a DIFFERENT ULID whose own terminal phase is NOT what the leg adjudicated.
*If confirmed:* the FAIL is FALSE — the S31 and the core are exonerated on tonight's evidence (the settle PASS corroborates); the night re-adjudicates as "8/9-equivalent with one instrument defect"; a bench-RUNNER defect WU charters (terminal-read scoping / capture hygiene — an instrument fix, NOT an s31 retune, and it does not touch core); the C4 distribution takes no datum; the bar discipline holds.

**H-D — real confirmation timeout at the device.** A fresh s31 command was minted and dispatched; the S31 sent no confirming report inside the confirmation window; the phase honestly read CONFIRMATION_TIMED_OUT.
*Predictions:* (a) the failure JSON `commandId` is a DISTINCT ULID (timestamp plausibly between the timeout-honesty and settle mints, ≠ `01KZJTBXKXW5FYE9D83EPZNAJX`); (b) the event slice shows the s31 command dispatched with NO device report within the window; (c) the settle command then confirmed normally (it did — PASS 1/1).
*If confirmed:* the first real position-8 confirmation timeout on record, n=1 against 3 consecutive passes. NO retune, NO re-run — the Aug-10 04:30 fire is the standing next instrument; a SECOND consecutive real FAIL buys the deeper read (radio-conditions and report-path arms, predictions to be filed then). The C4 gap is noted; the confirmation-truth position is UNTOUCHED (an honest TIMED_OUT is the product working).

**H-L — late delivery (report after window).** As H-D, but the bundle/event slice additionally shows the device's state report ARRIVING AFTER the window closed, or post-leg state consistent with the command eventually applying.
*Predictions:* H-D(a) + a visible late report event, or a state read showing the commanded value landed post-window.
*If confirmed:* a live field exhibit of report-after-window — routes DIRECTLY to the L-F delivery-evidence closure intake (due Tue 09:00) as a named corroborating datum; same discipline as H-D otherwise (no retune; Aug-10 adjudicates continuation).

**Prior stated honestly, pre-read:** the 12-char ULID match makes H-I the leading hypothesis, but the journal truncation is exactly why this files as a prediction and not a verdict. H-D/H-L remain fully live until the bundle speaks.

## §3 The discriminating read (read-only; Nick's paste-block is in the beat-3 chat record)

The bundle pull is three read-only acts on the Pi: (1) list the bundle contents; (2) grep the bundle for the timeout-honesty ULID `01KZJTBXKXW5FYE9D83EPZNAJX` — WITH the anti-vacuous control grep for `commandId` generally (a zero-hit run on both = a vacuous read, re-pull, never adjudicate on it); (3) cat the terminal/failure JSON and any event-slice file. RECORD: paste either way.

## §4 One-word adjudication rules (the hub rules on the RECORD)

- ULID grep HITS inside the s31 failure JSON ⇒ **H-I CONFIRMED** (false FAIL; runner-defect WU charters; night re-adjudicates 8/9-equivalent).
- ULID grep ZERO (control positive) + distinct commandId + no in-window report ⇒ **H-D** (real, n=1; Aug-10 adjudicates continuation).
- As H-D plus a visible late report ⇒ **H-L** (routes to L-F).
- Anything else ⇒ the read STAYS OPEN; no adjudication; the Aug-10 fire proceeds untouched either way.

## §5 What does NOT happen under any outcome

No s31 hardware touches · no manual re-runs · no suite/constants edits · no confirmation-window retunes · no core or bench code changes pre-adjudication (and none pre-freeze without Nick's explicit word even post-adjudication — a confirmed H-I runner defect CHARTERS a fix, the charter prices when it lands). The nightly keeps firing on its own schedule; its next verdict banks per law 16.

## §6 Adjudication (POST-READ SLOT — empty at filing; the hub writes the verdict here on the bundle RECORD)

*(reserved)*
