<!--
file: context/planning/2026-10-10_v103_decision-record.md
purpose: The v103 hub's decision record for Saturday 2026-10-10. Opened at 06:31 CT; at 06:35 Nick said BC9a had not run Friday and that "we have all day to work". It holds Nick's words verbatim, the facts at the instrument, the decisions by id (D-v103-n) and the Carried row. THE ONE DELIVERABLE (D-v103-2): the Pi on `37f05a9` by sha with SOAK-NIGHT-2 launched tonight on its re-stamped packet, and HERO-U2b landed green with its rider. The stretch: AVAIL-API-1 cut and reviewed (dispatch-ready), on a `CARRIER:` word read against the burn-in's own probe lines.
audience: the v103 hub (edited every beat) · the v104 boot (the newest §3 section + the Carried row) · Nick (the ids he can REVERT)
state-type: decision record (one window)
status: CLOSED at beat 3, the close (Sat 2026-10-10 ~09:0x CT; instrument 2026-10-10T14:07:49Z; D-v103-18..28; v104's text cut). Was: LIVE — beat 2 (Sat 2026-10-10 ~08:1x CT; instrument 2026-10-10T13:10:57Z; D-v103-10..17). Opened v103 beat 1 (Sat 2026-10-10 ~07:1x CT; instrument 2026-10-10T12:14:20Z; D-v103-1..9).
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

## §3b Beat 2 (Sat 2026-10-10 ~08:2x CT): BC9a intaken; the bench, the hivemind and the core landed (`409547c`, CI green); TRIAGE executed; the horizon rows written; the burn-in read cut
- **D-v103-10 — BC9a RETURNED (Nick 07:56) and INTAKEN ACCEPT.** The audit is `context/audits/2026-10-10_v103-b2_BC9a_bench-landing_r1_intake_audit.md` (§1–§3).
  - **The Pi runs `37f05a9` BY SHA since 07:17 CT** (BOOT0 `bench-2026-10-10-081747.log`, Pi-local 08:17:47 EDT). Boot-health is PASS 6/6 at 10/10; `formed=0 resumed=1 relinked=10`.
  - **P1 and P2 HELD.** P1 was read against C2's re-stamped EXPECTED; its own sentence stands as cut.
  - **P3–P5 and P7 RECORDED.** The S31 was probed 4.652 s after `network_resumed`, then every ≈ 60 s, all `ok`. So the "`pings=0` right after a boot" premise is refuted for the floor class across a restart.
  - **P6 arm (a). P-v103-1 HOLDS:** the Hue reads `UNAVAILABLE · None · None · None` on `37f05a9`.
  - **The guide's two judgment calls are right.** The card's `p > 849602` was the hub's wording: the registry subscriber logs the last registration event's position.
  - **Layer 2:** the kept log's greps and the subscriber's source.
  - BC9a's card → EXECUTED.
- **D-v103-11 — `BENCH: LANDED 32bac40`** (the card's paste, 07:56).
  - The commit, fast-forward and push ran: 5 files, `cddac94..32bac40`.
  - The card's last read crashed on the Windows console's cp1252, on a "→" in a test name. The hub re-ran it at `32bac40` on the device: `verify72h selftest: 48 check(s), 0 failure(s)`, engine 42/0.
  - **IR-146 minted:** a card's `python3` on the desk runs under `PYTHONIOENCODING=utf-8`.
  - IR-142 is LANDED; it closes on the Pi at BENCH-PULL-9, in BC9's card, whose STATE line names `32bac40`.
- **D-v103-12 — `HIVE: LANDED 9cef3e7`** (the b1 card: 12 files; the census held 12 = 12).
  - The b1 card was the library's un-gated form: `card()` puts a `;` before `git commit`. This is IR-101's defect, OPEN since v87; every card since kept it.
  - **From b2, every hub card is gated by test,** written by the beat script: `[ N -eq expected ] && [ trailers -eq 0 ] && git commit … && git push`, never a `;` before a commit or a push.
  - IR-101 stays OPEN until a library ships the gated card. v3 adds `beat()` only.
- **D-v103-13 — HERO-U2b-r1 RETURNED (07:57; 2,989 B) and INTAKEN ACCEPT.**
  - Three files only, with md5s equal to the return's. `src/` is byte-identical to the U2b snapshot.
  - The hub's `npm run verify` in a clean container exits 0: contract-check ✓ 11 endpoints at v1.1.6-2026-10-09.
  - **The core landing card was handed ≈ 08:0x:** `_scratch/v103/b2/card_core_hero_u2b_land.txt`. It is gated (HEAD `2b4be09` · `main` · no lock · trailers 0 · staged 28 = 21 M + 7 A · nothing outside `web-ui/dashboard/`) and was dry-run in a throwaway repo (28 commit, 29 refuse).
  - **It ran at 08:06: `CORE: LANDED 409547c`** (28 files, 1,798+/61−; `2b4be09..409547c`). **`CI: green`** — Nick: "All CI and checks have passed green in GitHub for this core commit." `CI:` for `2b4be09` is superseded: `409547c` is its child on the same paths and was not read separately.
  - **THE WEB-UI DOMAIN IS FREE.** The card on the real wire (the Hue as the fifth state) is the domain's next act, cut at beat 3 (LIVE-RENDER-1).
- **D-v103-14 — `TRIAGE: adopt` EXECUTED** (Nick's word of v101 b6; D-v101-27's reasons, row by row).
  - **RETIRED:** IR-45 · 60 · 63 · 76 · 83 · 96 · 102 · 107 · 114 · 120.
  - **IR-56 stays OPEN until its condition row is written into dry-run #1's packet at the cut.** The condition row is the 90-s post-restart read at the class's naming time. BC9a sharpens it: across a restart the floor class's silence clock carries over from the sidecar seed, so a silent plug can be named within ≈ 2 min of `network_resumed`.
  - `REVERT IR-n` is honored per row.
- **D-v103-15 — The horizon rows by id (D-v102-24, Nick's F and G).** Written into `context/planning/2026-10-02_v93_THE-HORIZON_post-run-rows_Oct15-Nov25.md` as §13:
  - **C11:** three outreach asks, by Oct 17.
  - **C12:** `TAILSCALE: expiry-off` and `REMOTE:` before PI-2 lands Oct 20.
  - **C13:** the second coordinator stick, a FIN row, by Nov 10, before pilot zero's install.
  - **C14:** `TM:` and `ATTORNEY-DRAFT:`, each dated back from the December narrative with its lead time beside it.
  - **J10 annotated:** `STARTER: a` re-shaped the starters. Presence, Sun and Time are EMPTY Tier-2 records at `37f05a9` (`AutomationDefinitionLoader.java:448–:450`).
  - **J11 minted:** TimeTrigger + SchedulerService, after the freeze. It is a composition-root change and takes the one-way-door review.
- **D-v103-16 — THE BURN-IN READ (BURNIN-1) cut:** `_scratch/v103/b2/card_burnin1.txt`.
  - Read-only, the desk, one paste, at ≈ 10:30 CT or later (≥ 3 h after BOOT0).
  - **Dry-run on the corpus:** BOOT0 (the S31 row: 5 · ok 5 · gaps 0) and BC8's BOOT0 (G4-2 dark 1 / up 1, its link lines whole); `_scratch/v103/b2/burnin1_dry-run.txt`.
  - **Pre-registered (P-v103-2):** the S31 answers every floor probe for ≥ 3 h — pings ≈ the minutes since its first probe (± 10 %), all `ok`, gaps > 90 s ≤ 5. If it HOLDS, the carrier's (d) is (a) for the floor class, and the H10 returns refined before `CARRIER:` is asked. If it does not, (d) stands as written.
- **D-v103-17 — THE SUNDAY SHAPE, an H10 for Nick (`SUNDAY: rec | PKG-FRESH-1: sat`, with `CAPACITY: Sun rig <h>`).**
  - **Options:**
    - (a) PKG-FRESH-1 this afternoon, re-stamped: the Pi powered down and the dongle out for ≈ 1.5 h, five hours before the soak's window, on its first-ever card swap.
    - (b) Sunday: S2 at 07:00 → v104 → BC9 + REHEARSAL 3 ≈ 13:00–17:00 (re-stamped at v104 with P2′'s premise and BP9 `32bac40`) → PKG-FRESH-1 ≈ 19:00 as already dated.
  - **PM recommendation: (b).** The Pi stays untouched from BC9a to the harvest, so the soak's first night under AVAIL-SHAPE carries no coordinator outage, and the sensor's row (P6′) is not confounded.
  - **Refutable-by:** `CAPACITY: Sun rig < 6 h` → BC9 Sunday evening, PKG-FRESH-1 Monday daytime before dry #1.
  - **Blocking:** nothing today.
- **Carried into v103 b3:**
  - **Open words:** `HIVE: LANDED <sha>` (the b2 card) · `BURNIN-1: done` (≈ 10:30+) → the H10 refined → `CARRIER:` · `SUNDAY:` / `CAPACITY:` · `RESEARCH-LH: comparator | quiet-week`.
  - **Beat 3's blocks:**
    - BURNIN-1's read at the bytes, with P-v103-2 adjudicated first;
    - the carrier's H10 refined;
    - AMD-103 drafted on `CARRIER:`;
    - BEAT-RENDERER-2's charter cut from IR-140;
    - LIVE-RENDER-1 cut (the card on the real wire at `37f05a9`: read-only, Nick's desk, through an ssh tunnel to the Pi's loopback API);
    - the dry-run #1 packet's cut, with IR-56's row.
  - **The rotation:** this beat leaves 12 live beats, so beat 3 rotates before it inserts.

## §3c Beat 3 — THE CLOSE (Sat 2026-10-10 ~09:0x CT; instrument 2026-10-10T14:07:49Z): BURNIN-1 read; `CARRIER: f` ruled by Nick; PKG-FRESH-1 pulled to this morning and launched; the deliberation filed as the plan forward; the soak re-aimed; the rotation; v104's text
### Nick's words, verbatim
**08:31 (the message, with the b2 card's output):** "Provide me the prompt to kick off the PKG-FRESH-1 session — and while I run that, I need you to very carefully deliberate and decide on how we proceed from here."

**08:31 (the attachment, filed whole; md5 `eb744628e3ec`, 5,924 B):**

> Verdict: (f) is the right family — say CARRIER: f — but not as written. Three amendments and one correction before AMD-103 is drafted.
>
> Why the other four fall, on first principles. Event sourcing stores facts the domain needs to re-derive its sentences; it does not store every sample a sensor loop took. (a) stores samples — and the number that kills it is not today’s 36K/day but the one-way door: a Pi replaying a year of 100-device probe answers at boot, which is the exact cost D-v102-21 told us to put a number on. (b) is the inverse mistake — it buys freshness by breaking “the store read where the store has the event” and the household-sentence test in the same move, and it adds a module edge the architecture refuses. (c) keeps today’s blind spot: a healthy quiet device has no evidence of life in the record. (d) was a hypothesis about the floor class and the data refuted it; good — that is what the refutable-by was for.
>
> What is actually going on. The 1,190/day is not a property of the event model. It is the probe schedule — asking a device that has answered for hours again every ~72 s. The carrier question only decides what fraction of those observations to record; (f) decouples the two, which is right, because the fast schedule is what buys 2–3 minute dark detection, and that part already works and is already recorded (the transition). From what I know of the incumbents — the comparator lane must confirm these, I am recalling, not citing — Z2M pings active devices on a 10-minute default, ZHA considers a mains device unavailable only after ~2 hours of silence, and none of them records probe outcomes at all; availability is a boolean in memory. So the market’s bar is coarse detection and no record. Minute-scale detection plus an hourly recorded proof of life clears that bar on both axes without per-probe recording. (f) is sufficient; (a) was never necessary.
>
> Amendment 1 — put counters on the hourly event (costs zero events, closes a real hole). The recorded answer carries answeredSinceLastRecord, missedSinceLastRecord, windowStart. Today a device that misses every other probe never reaches PROBE_MISSES_TO_DARK = 2, resets on each answer, and leaves nothing in the record — OR-S31-INTERMITTENT and the Hue are invisible under today’s model and under (f) as written. With the counters the record says “checked 49 times this hour, answered 49” or “answered 37 of 49” — the flaky-mesh sentence the card needs later, and the evidence those two open risks have been missing. Carry the link {lqi, rssiDbm} reading from the answered probe too if J1’s shape allows it; one hourly link sample per quiet device is the mesh-health history for free. Keep the bound strict: no extra emission on a single miss-then-answer flicker; the counters carry it.
>
> Amendment 2 — the policy goes in the record, and the window is monotonic. The boot/interview contract event carries the class, report interval, silence limit and the record interval (3600 s). Otherwise “checked hourly” is a sentence written from the source code, not the files. And the “hour” must be a rolling window on the monotonic clock — emit when ≥ 3600 s have elapsed since this device’s last recorded answer — not a wall-clock bucket. We put timedatectl in every packet precisely because the Pi’s clock steps; a wall-clock bucket double-records across a forward step and skips one across a backward step. The event’s at stays wall-clock for the record.
>
> Amendment 3 — the projection needs a stale-record arm, or (f) lies by omission. Under (f) the card infers “still answering” from “answered at 7:02 and no dark transition since”. That inference is only valid while the tracker is alive. If the thread dies or the stick is pulled, the record goes silent for every device at once — no transitions, no answers — and the card would show “answered at 7:02” forever. The contract event makes this detectable: no record for a quiet device in more than one record interval plus slack means “no check recorded since 7:02”, a sixth honest cell beside the fifth state. AVAIL-API-1’s instruction must say this; the SPEC’s table today has no such arm.
>
> Amendment 4 — derive the constant, don’t feel it. One hour is a reasonable default (10 devices 240/day; 100 devices 2,400/day, ~3% of today’s rate), but the correct derivation is the replay budget: events/day × retention × filed replay rate ≤ boot budget. Make it a class constant in config with 3600 as the default, recorded by Amendment 2, and revisit from the dry-run #1 packet’s numbers rather than now.
>
> The correction — the refutable-by tests the wrong thing. (f)’s bound is independent of the probe rate by construction; whether the S31 runs at 50/h or 25/h changes (a) and (d), not (f). The soak read that actually bears on (f) is whether the S31 shows single-miss flickers at any meaningful rate — which decides how much Amendment 1 matters, and whether an hour is too coarse to localize them for that one class. Re-aim it there.
>
> AMD-103’s shape, then. Two event types under Doc 01 §4.3, the principle quoted: probe_answered (a fact — that probe at at was answered — sampled under a recorded policy, with the counters) and the per-device availability contract at interview/boot. The existing projection ignores both, so no bump for it; the recovery-card projection is new at version 1, and its replay from the store’s beginning touches only the AvailabilityChanged events that exist today — the number the review must state, and it will be small. Codec roster pins move in lockstep as AMD-99 R-E requires. Do not add the port; do not change the probe cadence in this unit — that is a separate product question (how fast must a dead plug be noticed) that the comparator lane’s data should inform later, and it would also change what “asked twice” means.

**08:46:** "PKG-FRESH-1 has been launched. This hub/orchestration conversation is beginning to get long in both length and context window/tokenization. We should carefully close out and take care to plan out our full next session (and prepare the next hub session so it can receive the results of PKG-FRESH-1 when ready)."

**08:57 (Nick: "Also, from the PKG-FRESH-1 session:" — the guide's text, filed whole):**

> PKG-FRESH-1 PRE-A (the guide, ~08:55 CT; before A1 — the held card in and running, nothing on the rig touched). A read-only desk pre-check (teed as `=== PRE-A` at the top of _scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_outputs.txt) found two premise gaps; each would STOP the sitting with the held card out.
> 1. KNOWN_HOSTS COLLISION AT A3 — the desk's ~/.ssh/known_hosts line 13 = `192.168.1.80 ED25519 SHA256:rzZUoqAKvw5gQ0rjGheaKMY0VxaDCoNTPRfM56UrCJQ`: the OLD hs-fresh card's key (R-4b's "Permanently added '192.168.1.80'" 09-04; the same print at H8a's operator record :256). The board takes .80 whichever card is in (E-P3; R-4b "no DHCP reassignment"); hs-fresh-1 has new keys, so A3's accept-new refuses a CHANGED key. `ssh -G pi`: hostname hs-dev-1 · checkhostip no — pi's trust is its own entry; no option below touches it. RULE ONE: (a) `ssh-keygen -R 192.168.1.80` once on the desk before A1 (the one stale entry out; ssh keeps known_hosts.old; every card command verbatim) · (b) the guide adds `-o UserKnownHostsFile=~/.ssh/known_hosts_fresh1` to the fresh-card ssh/scp in A3 B1 B2 B3 C2 D1 (nothing removed) · (c) as written — A3 STOPs, Part D restores.
> 2. THE ARTIFACT IS NOT AT THE CARD'S PATH — ~/fresh1-artifact does not exist on the desk, and Thursday's 0a output is in no file under _scratch (no 2026-10-08_ outputs file). Part 0's own rule (re-run when the artifact is missing) applies: the guide is re-running 0a now; the 49455fc artifact is inside its 7-day retention (≈ Sun 10-11 16:3x CT). Say if you want otherwise.
> The guide shows A1 only after your ruling on 1 and a green 0a, and before 10:00 CT.

**08:59 (Nick: "Another thing from the PKG FRESH which you must carefully consider:" — the guide's text, filed whole):**

> PKG-FRESH-1 0a: STOP (~08:58 CT; desk only; the rig untouched — RULE WITH PRE-A item 1). 0a's block re-run verbatim → `debs=1`, but the .deb is `./deb/build/homesynapse_0.1.0+git20260903.124041.gef02d13_arm64.deb`, sha256 `48a33b0dc614a7f74fd0e0a279480e3c2f1f8e1e952f3195f0ffdbad1c626003` — byte-identical to R-4b's record (:14 :65 :67): ~/Downloads/distribution-artifacts-arm64.zip is the Sep 3 ef02d13 zip, not 49455fc's. 0a's EXPECTED (the name carries g49455fc) fails. Thursday's Part 0 "debs=1" is not corroborated: no ~/fresh1-artifact existed before today's run and no 0a record exists anywhere. ~/fresh1-artifact now holds the stale ef02d13 .deb (B1 would have shipped it; its Version line would have caught it with the held card out).
> PROPOSED (nothing deleted; 0a and B1 stay verbatim) — RULE: (1) `mv ~/fresh1-artifact ~/fresh1-artifact.ef02d13-stale` · (2) `mv ~/Downloads/distribution-artifacts-arm64.zip ~/Downloads/distribution-artifacts-arm64.ef02d13-sep03.zip` · (3) 0a's browser leg as written: the 49455fc push run (Sun 10-04 ≈ 16:3x CT) → its conclusion → the arm64 job → the "Version-grammar echo" line → Summary → Artifacts → distribution-artifacts-arm64 (it saves under the freed name; retention ≈ Sun 10-11 16:3x CT) · (4) 0a's bash block verbatim → EXPECTED debs=1 · g49455fc · sha256 = the echo line. Or workflow_dispatch / another sha by your word.

### The decisions
- **D-v103-18 — BURNIN-1 READ at the bytes, and P-v103-2 ADJUDICATED PARTIAL.**
  - **The read:** `_scratch/v103/burnin/BURNIN-1.txt`; pi-clock 13:14:42Z (08:14 CT); LOG `bench-2026-10-10-081747.log`; `deployed=37f05a9` · `bench=cddac94`; ash 6 · handoffs 1.
  - **The S31:** 46 probes, all `ok`, first 08:18:20.703 → last 09:13:56.099 Pi-local (55.6 min; 49.6/h ≈ 1,190/day). 11 gaps over 90 s. Its own frames: `2 2 2 2 2` per 10-min window.
  - **The adjudication:**
    - "all `ok`" HELD.
    - "pings ≈ the minutes (± 10 %)" MISSED: 46 against 55.6, −17 %.
    - "gaps > 90 s ≤ 5" MISSED: 11.
    - One reason for both misses: each own frame restarts the 60-s silence, and the prediction ignored the S31's own reports.
    - The window was 56 min, not ≥ 3 h; the card ran early, and the soak night carries the long read (P11′).
  - **What it was for still holds:** for the floor class, (d)'s "one per silence episode" is one per probe, i.e. (a). So the H10 was refined to (f), and Nick ruled it (D-v103-20).
- **D-v103-19 — `HIVE: LANDED 9b6f5df`** (the b2 card; 10 files). It is HEAD at this beat's instrument.
- **D-v103-20 — `CARRIER: f`, RULED BY NICK at 08:31 with four amendments and a correction** (verbatim above).
  - **A1:** the counters on the hourly record (+ `link`).
  - **A2:** the policy in the record; the window is monotonic.
  - **A3:** the stale-record arm.
  - **A4:** the constant is derived — a class constant, default 3600, revisited from dry-run #1's numbers.
  - **The correction:** the soak's read is re-aimed at the S31's single-miss flickers.
  - **AMD-103's shape as he gave it:**
    - two types under Doc 01 §4.3, the principle quoted;
    - no bump of the existing projection;
    - the recovery-card projection new at v1, its replay number stated;
    - R-E's pins in lockstep;
    - no port; no cadence change.
  - **PROBE-ANSWERED-1** (the freeze list) is absorbed into AMD-103 + AVAIL-API-1.
- **D-v103-21 — PKG-FRESH-1 PULLED TO SATURDAY MORNING on Nick's word; re-stamped and LAUNCHED 08:46.**
  - **The re-stamp:** 08:33; md5 `cb324631eade` → `8761c1c1b5c7`; 27,226 → 28,021 B. The dry-run (`_scratch/v103/b3/fresh1_dry-run_v103.txt`) is COMPLETE with no FAIL.
  - **The `SUNDAY:` H10 (D-v103-17) is OVERTAKEN.** Sunday now holds S2 and BC9 + REHEARSAL 3.
  - **The soak:** its LOG0 is D2's boot, still `37f05a9`.
  - **The line:** `PKG-FRESH-1: <line>` is v104's first bank.
- **D-v103-22 — THE DELIBERATION'S THREE FINDINGS** (the plan §2):
  - **F1 — the replay path.** The bus replays the whole log through `readFrom` (`ReplayDriver.java:28`, `:64`, `:111`). `readByType` over `idx_events_type` exists and is unused here. `/health` is keyed to the state projection.
    - So "touches only the AvailabilityChanged events" holds for a type-scoped catch-up only.
    - AMD-103's review states the path and its number.
    - The rec is (a), with the instrument first. The word is `AMD-103-PATH:`.
  - **F2 — D2 is a long-gap resume, and the first read of P3′'s question.** → P12′.
  - **F3 — the tracker's silence is the wall clock** (`StandardAvailabilityTracker.java:462`, `:479`). → **IR-147 minted (post-run).**
- **D-v103-23 — THE SOAK RE-AIMED (Nick's correction).** SOAK-NIGHT-2:
  - **P11′** (the S31's flickers; arms 0 · 1–9 · ≥ 10) and **P12′** (the long-gap resume) added to §P′;
  - two read lines: S0 prints LOG0's first availability lines; S2 prints each S31 timeout with its next probe;
  - two slots added to the one line;
  - the status line amended.
  - **Dry-run on the corpus:** BOOT0, BC8's BOOT0, and a labelled synthetic fixture for the timeout read. The audit is `_scratch/v103/b3/soak2_amend_dry-run.txt`.
- **D-v103-24 — THE PLAN FORWARD FILED:** `context/planning/2026-10-10_v103_THE-ROAD-FROM-CARRIER-F_plan-forward.md`. It holds:
  - AMD-103's drafting brief (§3);
  - HERO-U2c, the FE note (§4);
  - AVAIL-API-1: cut Mon; the lane Tue–Thu; landed Fri Oct 16 as the target, Oct 20 the last day (§5);
  - the rig to the freeze, BC10 included (§6);
  - the comparator pre-read (§7);
  - the order (§8);
  - five words (§9).
- **D-v103-25 — THE COMPARATOR PRE-READ** (the hub's agent; primary sources fetched today). Nick's three recollections, each CONFIRMED with qualifiers:
  - **Z2M:** a 10-min silence timer, and opt-in.
  - **ZHA:** 7,200 s, and it asks first (a Basic read; two misses).
  - **The record:** no structured per-probe history in Z2M or ZHA; NOT FOUND for SmartThings, deCONZ and Hubitat.

  This is a pre-read, not the lane. The lane needs `RESEARCH-LH: comparator`.
- **D-v103-26 — BEAT-RENDERER-2's charter FILED DISPATCH-READY** (`context/instructions/2026-10-10_hivemind-lane_BEAT-RENDERER-2_ledger-state_caps_probe_card-v2_charter.md`).
  - **Premises re-read at this beat:** v2 `99e87f2dbafa` · v3 `fc79eee9d1af` · `render_state.py` `72372aa8bfb3` · `test_render_state.py` `9774347342bc` · `state.yaml` `0812b89782f3`.
  - **Dispatch:** on `RENDERER-2: today`.
- **D-v103-27 — THE CLOSE, on Nick's 08:46 word.**
  - v104's text is cut: `context/handoff/2026-10-10_v104_dispatch-text.md`. It covers Saturday afternoon and evening, with PKG-FRESH-1's line as the first bank. THE ONE DELIVERABLE: the intake, plus AMD-103 drafted and reviewed.
  - THE ROTATION: 12 live → the oldest six VERBATIM to `archive/pm-handoff-beats-v101b4-v102b1-rotated-2026-10-10.md`, leaving 7 live after this block.
  - The v103 text is EXECUTED, and this DR is CLOSED.
  - LIVE-RENDER-1's card (`_scratch/v103/b2/card_live_render1.txt`) is carried to v104 unhanded, because the Pi is mid-swap.
- **D-v103-28 — PKG-FRESH-1's PRE-A and 0a STOP, RULED (08:5x; both before A1; the rig untouched, the held card in).**
  - **(1) The known-hosts collision at A3: (a).** The desk's `~/.ssh/known_hosts` line 13 holds the OLD hs-fresh card's key for `192.168.1.80`.
    - The fix: `ssh-keygen -R 192.168.1.80` once, gated. Exactly one line, not naming `hs-dev-1`.
    - The guard: `ssh -o BatchMode=yes pi true` before and after. `pi` resolves to hs-dev-1 with `checkhostip no`, so its trust is its own entry.
    - The undo: `known_hosts.old` restores it.
    - Every card command stays verbatim. PKG-FRESH-2's card carries a per-card `UserKnownHostsFile` from its cut.
  - **(2) The artifact: the guide's (1)–(4) ADOPTED as proposed.** 0a's verbatim re-run found `debs=1`, but the `.deb` was `…git20260903.124041.gef02d13_arm64.deb`, sha256 `48a33b0d…6003`: the Sep 3 zip in `~/Downloads`, byte-identical to R-4b's record.
    - 0a's EXPECTED (`g49455fc`) failed, as it should, with the held card still in.
    - The renames, nothing deleted: `~/fresh1-artifact` → `.ef02d13-stale`; the Sep 3 zip → `…ef02d13-sep03.zip`.
    - Then 0a's browser leg as written: the `49455fc` push run's `distribution-artifacts-arm64`, inside its retention to ≈ Sun 16:3x CT.
    - Then 0a's bash block verbatim. EXPECTED: `debs=1` · `g49455fc` · the sha256 equal to the run page's echo line.
    - STOP before A1 on any miss. P7's `workflow_dispatch` re-mint is the fallback, by the hub's word.
  - **BOTH ARE THE HUB'S MISSES:**
    - The re-stamp carried "Part 0 DONE Thu: `debs=1`" and the STATE line pre-filled "the artifact on the desk: yes" from Thursday's record line. No outputs file corroborates it; no `~/fresh1-artifact` existed before today.
    - The dry-run ran on the corpus, never on the desk's ssh trust.
  - **The lesson for v104** (a pm-lessons row):
    - A re-stamp re-reads every DONE it carries at an outputs file's bytes, or marks it UNVERIFIED.
    - A card's desk-state premises (known_hosts, artifact paths) are read in a PRE-A block before any hands act. This guide did that on its own.
  - **P7's adjudication** (v104) records Thursday's uncorroborated Part 0 as a finding.
- **Carried into v104:**
  - **OPEN words:**
    - `HIVE: LANDED <sha>` (this close card) · `PKG-FRESH-1: <line>`;
    - `AMD-103-PATH: a|b` · `BC10: oct17|oct18|no` · `RESEARCH-LH: comparator|quiet-week` · `RENDERER-2: today|later` · `AMD-103: ratify|edits`;
    - `SOAK-NIGHT-2:` (Sun) · `CAPACITY: Sun rig <h>` · `FOREIGN:`;
    - the standing words (`REMOTE:` · `FINALS:` · `DISCOVERY:` · `ATTORNEY-DRAFT:` · `TAILSCALE:` · `OUTREACH:`).
  - **v104's blocks** are its text's, in order.
