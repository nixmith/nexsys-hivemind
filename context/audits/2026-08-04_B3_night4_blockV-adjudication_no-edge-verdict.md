<!--
file: context/audits/2026-08-04_B3_night4_blockV-adjudication_no-edge-verdict.md
purpose: The BLOCK-V adjudication — A-9's first live artifact + the morning lastChanged read close night-4's level-1 with a VERDICT REVISION: night-4 shows NO REPORTED EDGE (H-2b revived for that night), while nights 2–3 remain EDGE-PROVEN. The per-night mechanism VARIES inside one umbrella class — the boot-adjacent window is hostile END-TO-END (dispatch, delivery, reporting) — which the ruled B3.3 position fix exits entirely. Mints the DELIVERY-PHASE GAP as a named finding feeding REV-1 and charter candidate (iii).
audience: Hub (v45), Nick, REV-1, the charter beat
state-type: adjudication (point-in-time)
status: FILED 2026-08-04 (v45 hub, beat 6)
provenance: Nick's BLOCK-V paste (the Aug-4 FAIL bundle ls + post-window-state.json + MANIFEST + the 11:31:32Z state read). Parents: the night-3 evidence read · the blockR adjudication · the R8/R9 addendum (the pre-stated discriminator this file resolves).
-->

# BLOCK-V Adjudication — night-4 reads NO REPORTED EDGE (v45 beat 6)

## 1. The instrument worked — both new arms, first live exercise, both honest

- **A-9 fired correctly on its first real FAIL:** `post-window-state.json` present, labeled, verbatim, untruncated — captured at 08:30:57.829Z, ~6 s after the turn_on. The night-2 evidence gap (no post-window read) is closed by mechanism, one WU later.
- **A-6's tiered capture reported an HONEST absence:** `app-log-slice.log ABSENT — window read + bundle-time marker-offset re-read both returned zero lines — the app wrote nothing in the run window` (state reports do not log at INFO; the tiers ran and said so). `journal-slice.txt` DROPPED as designed.

## 2. The arithmetic (against the pre-stated addendum-§3 discriminator)

- **A-9 at 08:30:57.8Z:** `on=false` · `stateVersion=4815` · **`lastChanged=1785745896.014` = 08:31:36.014Z AUG-3 — frozen** · `lastReported=1785832105.5` = 08:28:26Z (the day-boot's last periodic report, ~2 min BEFORE the nightly began) · `lastUpdated=1785832256.98` = 08:30:56.98Z — the CONFIRMATION_TIMED_OUT moment itself (the lifecycle verdict bumps `lastUpdated`; device truth lives in `lastReported`/`lastChanged`).
- **The morning read at 11:31:32Z (7 h later — far past any view lag):** `on=false` · `stateVersion=4857` (+42 in ~3 h ≈ the established ~4–5-min cadence) · **`lastChanged` STILL 08:31:36.014Z Aug-3.**
- **Verdict per the pre-stated rule: FROZEN ⇒ NO EDGE WAS EVER REPORTED on night-4.** The pre-filed A-9 view-lag caveat is satisfied — the 7-hour read, not the +6 s read, carries the verdict.

## 3. The verdict revision — the mechanism VARIES per night inside one class

- **Nights 2–3: EDGE-PROVEN** (unchanged — the settle off-edge confirms at 143 ms / 3.59 s, coincidence ≈10⁻⁵ at the measured cadence): the turn_on EXECUTED; the ON-edge report was late/absent; the OFF-edge report flowed.
- **Night-4: NO REPORTED EDGE — H-2b (boot-window command loss) REVIVED and LEADING for this night.** The relay's reported state never left OFF across the entire window. The alternative — edges occurred but BOTH reports were lost where nights 2–3 lost only the ON — is priced DISFAVORED; **the one residual read that closes it is the Aug-4 settle bundle's terminal disposition** (`command-s31-settle-20260804T083138Z/api-captures.json`: TIMED_OUT = the no-change class ⇒ relay was already OFF ⇒ command-loss confirmed; a fast CONFIRMED would reopen the question via same-value matching). Rides the next Pi trip — it does not gate the fix.
- **The umbrella class consolidates: the ~0.77 s-post-resume window is hostile END-TO-END** — dispatch succeeds at the API layer every night (`DISPATCHED` at +4 ms), but delivery and/or evidence fail variably beneath it. Some nights the command acts and under-reports (2–3); some nights it apparently never acts (4). **B3.3 exits the window entirely** (+40–55 s is measured-healthy for dispatch AND reporting, settle-proven two nights, ten seconds after a dongle power-cycle even) — **the ruled fix stands, STRENGTHENED: it cures both observed failure shapes.** Tonight's prediction is unchanged: `8/9 PASS · 1 SKIP(hue-online) · ON-latency present`; a position-8 FAIL escalates to HUE-RESET, never a retry.

## 4. THE DELIVERY-PHASE GAP — minted as a named finding (feeds REV-1 §S-1 + charter candidate (iii))

The command lifecycle carries `ACCEPTED → DISPATCHED → CONFIRMED | CONFIRMATION_TIMED_OUT`. **`DISPATCHED` means "handed to the integration" — the system records NO radio-level delivery evidence**, so delivered-but-unconfirmed and never-delivered are indistinguishable in the record (exactly the night-2/3 vs night-4 ambiguity this thread had to resolve with bench forensics). The EZSP layer plausibly RECEIVES per-message send/delivery status the adapter currently discards. Surfacing it as lifecycle evidence ("dispatched → delivered → confirmed") would have closed this thread in one morning and is the write-path twin of the availability thesis: evidence at every hop, honestly labeled. REV-1 verifies the mechanics (evidence-required, refute-welcome); the build-out is post-gate, chartered under candidate (iii)/P2.

## 5. Standing

Beat-5 landed `c5e9d6d` (exactly 5, pushed). B3.3 + S-5a dispatched by Nick (desk, parallel lanes) — the two-layer audits are the hub's next intakes; the Pi pull block issues on the B3.3 audit; **tonight's 04:30 fire adjudicates the fix.** Hands off the S31 throughout. If tonight PASSes, the s31 thread CLOSES as mechanism-pinned-and-cured (the H2/B3 ledger-rider retirement then rides a later beat WITH its grounding read), and the thread's arc — three honest FAIL nights, instrument hardening, a measured mechanism, a data-only cure — is designated exhibit material for the C-3 publishing thesis.
