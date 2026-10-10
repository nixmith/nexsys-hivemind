<!--
file: context/planning/2026-10-10_v103_decision-record.md
purpose: The v103 hub's decision record for Saturday 2026-10-10. Opened at 06:31 CT; at 06:35 Nick said BC9a had not run Friday and that "we have all day to work". It holds Nick's words verbatim, the facts at the instrument, the decisions by id (D-v103-n) and the Carried row. THE ONE DELIVERABLE (D-v103-2): the Pi on `37f05a9` by sha with SOAK-NIGHT-2 launched tonight on its re-stamped packet, and HERO-U2b landed green with its rider. The stretch: AVAIL-API-1 cut and reviewed (dispatch-ready), on a `CARRIER:` word read against the burn-in's own probe lines.
audience: the v103 hub (edited every beat) · the v104 boot (the newest §3 section + the Carried row) · Nick (the ids he can REVERT)
state-type: decision record (one window)
status: LIVE — opened v103 beat 1 (Sat 2026-10-10 ~07:1x CT; instrument 2026-10-10T12:14:20Z; D-v103-1..9).
-->

# v103 — decision record (Sat 2026-10-10)

## §1 Nick's words, verbatim
- **06:31 CT, the paste:** `context/handoff/2026-10-10_v103_dispatch-text.md` from line 9 (line 8 is blank; 20,297 B, ten paragraphs). Identity was checked at eight verbatim anchors across the paragraphs (each found once), the head and the tail. It was not byte-diffed, because the paste was not written out.
- **06:33 CT:** "HIVE LANDED:" with the push output `1219fae..aa15d3e  main -> main` and `aa15d3e (HEAD -> main, origin/main) hivemind: v102 post-close beat 5 — …`.
- **06:35 CT:** "Note: I have not yet launched BC9a, but need you to provide me the prompt for that, and whatever other dispatches you decide we need to do in order. Time: 06:35 CT on Saturday — we have all day to work."
- **06:50 CT:** "BC9a: launched. I will report the return line back to you upon completion, and I will ask you for any additional information and/or input (as necessary) for completing that session, if requested from it. It's important that you are diligent in reviewing HERO-U2b's return as well, then determining how this influences or changes/adds to our plans. Let me know how to proceed from here, while the bench card runs."

## §2 The facts at the instrument (banked; no act)
- **The clock:** `date -u` 2026-10-10T11:32:19Z (06:32 CT). Before 07:00 the harvest card could not have run. After 06:35 it could not run at all, because SOAK-NIGHT-2 never started.
- **The boot read set:** 41.6 KB of file bytes plus the OPEN lessons' headings, inside the 45 KB budget. The v102 DR was read as §3e whole plus a trimmed §3c, because b5 added §3e after the text was cut.
- **HEADs:**
  - core `2b4be09`: porcelain 25 = HERO-U2b's 18 M + 7 ?? under `web-ui/dashboard/src/`; ahead 0; origin/main `2b4be09`, with `37f05a9` an ancestor.
  - hivemind `aa15d3e`: porcelain 1 (the HERO-U2b return, `??`); ahead 0.
  - skills `e9a77a8`: porcelain 0.
  - bench `cddac94` on `bench-142/ir142-config-error-signature`: 5 staged (BENCH-142 + 142b); 10 `tmp_obj` files; no lock; origin/main `cddac94`.
  - docs `5e8eb8b`: porcelain 0.
- **The preflight, one line per check (overall PASS):**
  - C1 PASS.
  - C2 PASS: both spine segments are v102 b5; the freeze list resolves.
  - C3 PASS.
  - C4 INFO: the backlog's last-verified is 2026-08-01, with 29 DONE rows; not re-walked.
  - C5 PASS at the edge: Open Risks' newest date is 2026-10-03, so the section goes STALE tomorrow unless the close touches it.
  - C6 PASS: the coder handoff is at v102 b3; NEXT WU is AVAIL-API-1.
  - C7 PASS: 21 MODULE_CONTEXT files, none a template.
  - C8 PASS: no active entries.
  - C9 PASS: 28/28 at the bytes.
  - C10 PASS: 78 cited; the 5 misses are glob patterns, not files.
  - C11 PASS: `ConfigurationService` and `AvailabilityChangedEvent` resolve.
  - C12 PASS: 3 hits, all exclusions by record (PKG-FRESH-1 for Sunday; SOAK-NIGHT-2 and BC9a until their intakes).
- **Live beats:** 10. The text's "8" was b3's count; post-close b4 and b5 added two. This beat makes 11, so there is no rotation at the boot.
- **`HIVE: LANDED aa15d3e`** matches the hivemind HEAD and origin.

## §3 The decisions (beat 1, Sat 2026-10-10 ~06:4x–07:3x CT)
- **D-v103-1 — The premise changed at 06:35, and the day is re-planned by id.**
  - BC9a did not run Friday, so the Pi still runs `df2bc62`. SOAK-NIGHT-2 never started and there is no harvest this morning.
  - **Ruled:** BC9a runs this morning, re-stamped (D-v103-3).
  - **The soak night moves one day:** S0 and S1 Saturday ≈ 21:00 CT; S2 Sunday 07:00 CT (D-v103-4). The adjudicated window keeps SOAK-NIGHT-1's night hours, so CEILING 2 stays a like-for-like test. A daytime window would test the detector under more household traffic and could pass falsely: a sample vetoes a green, it never grants one.
  - **The day between BC9a and S0 is a burn-in.** Its probe lines sit in LOG0 before MARK0 and are counted by nothing. They are read once, at the bytes, as the `CARRIER:` H10's refutable-by (P3′'s substance: a floor-class device answering every 60-s probe for hours).
  - **BC9 + REHEARSAL 3 moves to Sunday**, because its premise is P2′.
  - **PKG-FRESH-1 stays Sunday ≈ 19:00** unless its card can run this afternoon without touching the soak; the hub reads that card at beat 2.
  - **Dry-run #1 stays Monday.** Its packet's dry-run completes on SOAK-NIGHT-2's S2.
  - **The bench landing stays gated on `BC9a:` alone.**
  - **The window:** Nick's "we have all day" runs the window under the stable prompt's §1b.8 (≤ 8 beats; no new block after beat 6), not the text's ≤ 4, because the text's deliverable was bound to a harvest that moved.
  - REVERT-able by id.
- **D-v103-2 — THE ONE DELIVERABLE.** The Pi on `37f05a9` by sha, with SOAK-NIGHT-2 launched tonight on its re-stamped packet, and HERO-U2b landed green with its rider. The stretch, under the cap: the burn-in's probe lines read at the bytes → `CARRIER:` → AMD-103 drafted → AVAIL-API-1 cut and reviewed, dispatch-ready.
- **D-v103-3 — BC9a's card RE-STAMPED in the lesson's form (pm-lessons 2026-10-07).**
  - **The script:** `_scratch/v103/b1/bc9a_restamp_v103b1.py`, probed in the container on a staged copy first. 25 anchors: 24 counted once each, plus the outputs name ×9.
  - **What moved:**
    - the day words Fri → Sat;
    - the start gate 20:45 → 12:00 CT and Part E's close 21:00 → 13:00 CT;
    - the outputs and guide-notes names to `2026-10-10_`;
    - Part A's EXPECTED to Saturday 03:30's nightly boot;
    - C2's `origin-main` to `main`'s newer head (`da9ca3d` and `2b4be09` are recorded, never deployed — `da9ca3d` first deploys by dry-run #2's card);
    - the soak's S0 to ≈ 21:00 CT.
  - **Unchanged:** every command, except that the dated outputs name moved. The pre-registrations stand as cut.
  - **The dry-run re-run on the corpus:** COMPLETE, no FAIL (`_scratch/v103/b1/bc9a_dry-run_v103.txt`). The clock words printed for the hub's eyes are all deliberate.
  - **Handed ≈ 06:45** with the STATE line filled: `HIVE: LANDED aa15d3e · AVAIL-LINE-1: LANDED cddac94`. Nick launched it at **06:50**.
- **D-v103-4 — SOAK-NIGHT-2's packet RE-STAMPED.**
  - **The script:** `_scratch/v103/b1/soak2_restamp_v103b1.py`, probed first; 18 anchors, each counted once.
  - **What moved:**
    - S0 and S1 to Saturday ≈ 21:00 CT; S2 to Sunday 07:00 CT;
    - LOG0 → `bench-2026-10-10-…`; LOG1 → `bench-2026-10-11-…`; the digest's date → 2026-10-11;
    - S0's `bench=` EXPECT → BC9a's BP8 sha (`cddac94`). The cut's `ba846c2` predated AVAIL-LINE-1's landing and would have read as a false STOP;
    - the intake → v104, Sunday ≈ 07:30; P2′'s BC9 → Sunday.
  - **Unchanged:** the clock gates (21:30 and 23:00), every command and §P′.
  - **The dry-run re-run:** COMPLETE, no FAIL (`_scratch/v103/b1/soak2_dry-run_v103.txt`). Its one "superior" hit is the packet's own rule sentence, as at the cut.
  - `SOAK-S1: run` is the hub's word at tonight's hand-off.
- **D-v103-5 — HERO-U2b RETURNED and INTAKEN ACCEPT-WITH-RIDER.**
  - The return is `context/audits/2026-10-09_HERO-U2b_return.md` (12,258 B). The audit is `context/audits/2026-10-10_v103-b1_HERO-U2b_intake_two-layer_audit.md`.
  - **Layer 2:** the census at porcelain is 25. The gates, re-run in a clean container, match the return exactly (682 / 6 todo; build; 77.2 KB; contract-check ✗ on the pin). The rider's three changes were proven on a throwaway copy (✓ 11 endpoints; lint 0; DevicesView 10). Red-first reproduced on HEAD's tree (14 of 24 red). The fixture row equals the capture's `data[7]` at the bytes. SPEC §7's 59 strings are verbatim, plus the 4 [AMEND] keys. P6 holds. The card was rendered by the hub in light and dark (`_scratch/v103/b1/hero-u2b_devices_recovery-states_{light,dark}.png`).
  - **The rider HERO-U2b-r1** carries three changes: the pin's fifth literal home (`scripts/contract-check.mjs:22`), the hero-literal lint scope (+2 files) and SPEC §7 → 63 rows. Its brief is the audit's §4; its line is `_scratch/v103/b1/line_hero_u2b_r1.txt`, handed ≈ 07:1x.
  - The landing card follows the rider's intake: core, census 28 = 21 M + 7 A, then `CI:`. The web-ui domain is held until then.
- **D-v103-6 — AUDIT CORRECTION: v102 b3's N1 is RETRACTED.**
  - At `37f05a9` the tracker's seed is in-memory only (`StandardAvailabilityTracker.java:281–:291`, no listener call). Every published transition carries a non-null reason (`:564–:619`). The one publisher, `ZigbeeIntegrationAdapter.java:2101–:2129`, writes a null reason only for a null reason.
  - So UNAVAILABLE ∧ reason null ∧ `lastSeenAt` null on the wire is a pre-J1 event that was never superseded: dark since before J1 and, under the sweep's skip, not asked since startup. That is SPEC §3's S2 R5 cell, which the lane built.
  - N1 had read the tracker's memory as the wire. The charter's watch-out from N1 was the hub's error. The lane's untagged departure from it is a return-discipline note only.
  - **Pre-registered (P-v103-1), before BC9a's line is read:** the Hue reads `availability=UNAVAILABLE availabilityReason=None` at `37f05a9`. If it reads `silence_timeout`, the retraction re-opens.
- **D-v103-7 — IR-144 and IR-145 minted.** Ids were grepped first; none above IR-143 existed.
  - IR-144: the HERO-U2b charter's five authoring defects, with the instrument that catches them before dispatch.
  - IR-145: the FE mirror declares the J1 keys on A1 only, while A2/A3 carry them on the wire (`EntityStateJson.java:66–:68` @ `2b4be09`). It is a later FE row, not AVAIL-API-1's. This corrects the hub's first reading of the return's §3.7 (a), said to Nick at ≈ 07:1x and corrected at ≈ 07:2x.
- **D-v103-8 — What HERO-U2b changes in the plan.**
  - **The card on silicon is pulled forward.** After the landing, the S2 card reads the real wire at `37f05a9`: the Hue as the fifth state, the Shelly plugs as "Reporting". This is the explanation path's first step on hardware (D-v101-39 (2)), and it no longer waits for AVAIL-API-1.
  - **AVAIL-API-1's cut** names which reads carry the S3 keys. The FE's six S3 `test.todo` keys become the next FE unit's red rows.
  - **HERO-U2c (row 3, the act)** waits until after the run, because its write endpoint is not on the freeze list.
  - **Q5 stays open** for devices that went dark after J1 (the restart ambiguity). Q5 (c) remains a tracker change in IR-56's family for AVAIL-API-1's review.
- **D-v103-9 — The beat's hygiene.**
  - The v103 text → PASTED; HERO-U2b's charter → EXECUTED.
  - The brief's §DIGEST: the week line and the Pi sentence re-cut by id; the full digest re-cut at the close.
  - §DONE: v101's and v102's ledger lines condensed to one line each (the beats and shas are kept; the detail is in their DRs).
  - **TRIAGE (the eleven RETIRED, IR-56's condition row) and the horizon rows of D-v102-24 are beat 2's.**
- **Carried into v103 b2:**
  - **Open words:** `BC9a: <its one line>` · `HERO-U2b-r1: RETURNED <path> <bytes>` · `HIVE: LANDED <sha>` (the b1 card) · `BENCH: LANDED <sha>` (after `BC9a:`) · `CORE: LANDED <sha>` + `CI:` (after the rider) · `CI:` (`2b4be09`) · `CARRIER:` (after the burn-in's read) · `RESEARCH-LH: comparator | quiet-week` · `FOREIGN:` · `CAPACITY:` (Sun rig).
  - **Beat 2's blocks:**
    - BC9a's intake, two-layer, with P-v103-1 adjudicated first;
    - the bench landing card;
    - TRIAGE executed;
    - the horizon rows by id;
    - PKG-FRESH-1's card read for a Saturday slot;
    - the burn-in's read card cut.
