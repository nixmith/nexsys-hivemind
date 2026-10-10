<!--
file: context/planning/2026-10-10_v103_THE-ROAD-FROM-CARRIER-F_plan-forward.md
purpose: Nick's ask at 08:31 CT ("while I run that, I need you to very carefully deliberate and decide on how we proceed from here"), answered at v103's close: the road from `CARRIER: f` (his four amendments and one correction) to the recovery card's third state on silicon before the freeze. It holds AMD-103's drafting brief, the FE note, AVAIL-API-1's cut and the rig through Oct 23. It names three findings in the source that change details, not direction, and the five words that are Nick's.
audience: Nick (§0, §8, §9) · the v104 hub (§3 is AMD-103's drafting brief; §8 is its order) · every hub to the freeze (§5–§6)
state-type: planning (one cut; LIVE until AVAIL-API-1 lands or moves post-run)
status: FILED v103 beat 3, the close (Sat 2026-10-10 ~09:0x CT; instrument 2026-10-10T14:07:49Z). Written BEFORE PKG-FRESH-1's return was read, so P12′ (§2 F2) is a prediction of record.
-->

# The road from `CARRIER: f` — how we proceed (Sat 2026-10-10)

## §0 The decision
**`CARRIER: f` as amended stands, and nothing in the deliberation moves a date.**
1. **AMD-103 is drafted this afternoon by v104**, in Nick's shape: two types under Doc 01 §4.3, the principles quoted, R-E's arithmetic re-grepped. An agent that has not seen the drafting reviews it. Then `AMD-103: ratify`, then the docs card.
2. **The FE note runs beside it** (HERO-U2c, design mode): FIELDS §3 is re-cut under (f), and SPEC §7 gains the sixth cell (A3). AVAIL-API-1 is cut from FIELDS.md and from nothing else.
3. **AVAIL-API-1 is cut Monday.** The cut names the replay path and states its number from an instrument, not a guess (F1).
   - The Java lane runs Tue–Thu in two phases: the record, then the read.
   - Target: landed Fri Oct 16. The freeze list's last day is Tue Oct 20.
4. **One rig night on the landed sha comes before dry-run #2** (BC10; a word, §9).

The comparator lane serves the December sentences and the later cadence question, not this unit. Three findings in the source (§2) sharpen AMD-103's review and tonight's soak; none reverses the verdict.

## §1 Where we stand at the close
- **The repos:** core `409547c` on `main` (HERO-U2b; CI green) · bench `32bac40` · docs `5e8eb8b` · hivemind `9b6f5df`.
- **The Pi:** `37f05a9` by sha since 07:17 CT. PKG-FRESH-1 (launched 08:46) swaps the cards; the Pi runs `37f05a9` again from its D2 boot.
  - Before A1, the guide's PRE-A found two desk premises the hub had missed: the stale `.80` known-hosts key, and Thursday's uncorroborated Part 0. 0a then caught a Sep 3 `ef02d13` `.deb`.
  - Both were ruled at 08:5x (D-v103-28): (a) with a `pi` guard; the renames, and `49455fc`'s artifact re-downloaded.
- **BURNIN-1** (pi-clock 13:14:42Z, i.e. 08:14 CT; `_scratch/v103/burnin/BURNIN-1.txt`):
  - The S31 was probed 46 times in 55.6 min (49.6/h, ≈ 1,190/day), all `ok`.
  - 11 gaps over 90 s. Its own frames: 2 per 10 min.
  - **P-v103-2 PARTIAL:**
    - All `ok` HELD.
    - The rate MISSED: 46 against 55.6, −17 %.
    - The gaps MISSED: 11 > 5.
    - One reason for both misses: each of the S31's own frames restarts the 60-s silence, and the prediction ignored those frames.
    - The window was 56 min, not ≥ 3 h; the soak night carries the long read.
  - The conclusion it existed for holds: for the floor class, (d) is (a). So the H10 was refined to (f), and Nick ruled `CARRIER: f` with A1–A4 and the correction (verbatim in the DR §3c).
- **The volume under (f):** one record per probed device per hour = 24 a day. That is 240/day for 10 devices and 2,400/day for 100. Under (a), the S31 alone writes ≈ 1,190/day.

## §2 What the deliberation found in the source (details, not direction)
**F1 — the replay path (the number AMD-103's review must state).**
- **How the bus replays:** it pages the WHOLE log through `readFrom` and filters in process (`ReplayDriver.java:28`; `MAX_REPLAY_PAGE = 500` at `:64`). A subscriber starts from its checkpoint (`:111`); a new subscriber's checkpoint is 0.
- **The index-backed read exists but is unused here:** `readByType` over `idx_events_type (event_type, global_position)` (`SqliteEventStore.java:662`; `V001__initial_event_store_schema.sql:58`). Only the explanation service calls it.
- **So the statement is path-dependent.** "Its replay … touches only the AvailabilityChanged events" holds for a type-scoped catch-up. It does not hold for a standard subscriber: a standard recovery-card projection at v1 pages every row of the held card's store at its first boot, once (1,644,011 rows at BC9a's C3; ≈ 823 MB).
- **What the pass does and does not risk:** `/health` is keyed to the state projection only (`HealthEndpoint.java:23`, `:99`), so the 90-s readiness gate is safe. But the I/O lands in the boot's first minutes, beside the resume and the first probes, and the card's third state is not current until the pass ends.
- **No replay rate is on file:**
  - the spike's Pi pass was never run;
  - Doc 03 §8's 50,000 events/s is a target;
  - the dev box's 10⁶ events in 625 ms are synthetic.
- **Path (a): the standard subscriber.** Its number comes from an instrument:
  - the type counts and a timed full scan of BACKUP-1's copy, in dry-run #1's Part 0;
  - then the real rate from the new projection's own `projection.replay.duration_ms` line at BC10.
- **Path (b): a type-scoped catch-up via `readByType`, then LIVE.** Its number is the three types' counts. Its price is a new seam in the REPLAY → LIVE handoff (AMD-42 · AMD-101 — the bus's hardest-won invariants) in the week before the freeze.
- **The hub's rec: (a).** The machinery is proven, and the rate is needed anyway:
  - A4's derivation;
  - UPGRADE-1 (Nov 10);
  - every future projection on a year-old household pays the same pass (the held card's 1.64 M rows ≈ a 50-device home's year at Doc 01 §10's 4,000/day).
- **The escape:** a measured pass over a ceiling the review names turns the instruction to (b), or moves the third state post-run.

**F2 — PKG-FRESH-1's D2 boot is a long-gap resume, and the first read of P3′'s question.**
- The tracker seeds every device's silence from the sidecar; BC9a showed the S31 probed 4.65 s after the resume. `evaluateTimeouts` (`StandardAvailabilityTracker.java:456–:497`) asks every mains device whose silence exceeds its limit.
- After the swap, the gap is ≫ 660 s. So the metering class (G4-1 · G4-2 · TR3) is asked at the first sweep, before its own first report. This is the first time on silicon that any of them is asked under AVAIL-SHAPE.
- IR-137 records the plug class unanswered 7 of 7 at `49455fc`. If they still do not answer, each is named dark ≈ 10–15 s after the resume and comes back on its first report. That is one pair per plug in LOG0's first minutes: before MARK0, so outside P2′'s count.
- **Pre-registered as P12′** (SOAK-NIGHT-2 §P′), with S0's added line as its read.

**F3 — the tracker's silence is measured on the wall clock.**
- `now = clock.instant()` at `:462`; `Duration.between(snapshot.lastSeen(), now)` at `:479`. So Nick's A2 hazard applies to the probe schedule too, not only to the record window.
- **The failure:** at a cold packaged boot, the unit starts after `network-online.target`, possibly before NTP has synced on a board without an RTC. A forward step past 660 s would then name the metering class dark falsely. A step past a passive device's limit would name it `silence_timeout`.
- **Not in AMD-103** (no cadence change in this unit). **IR-147 minted (post-run):** measure silence on a monotonic source within the process, and convert the seed once at start.

## §3 AMD-103 — the drafting brief (v104 drafts; an agent reviews; Nick ratifies)
**The form is AMD-102's:** the ruling box R-A… · §1 the locked text quoted at the docs sha · §2 the text after ratification · §3 what does not change · §4 the realization · §5 the DAS check · §6 exhibits.

**The rows the draft settles:**
1. **The two types.** Core, underscored, beside `availability_changed`, because they are cross-integration facts.
   - `probe_answered`, and the per-device contract. The hub proposes `availability_contract_declared` for the contract; the draft fixes both names.
   - Category `device_state` (Doc 01 §4.4 `:615`).
2. **`probe_answered` (A1).**
   - **Payload:**
     - `at` — wall clock; the answered probe's instant;
     - `windowStart`;
     - `answeredSinceLastRecord` · `missedSinceLastRecord`;
     - `link` `{lqi, rssiDbm}` | null — J1's `LinkReading`, when the reply carried one.
   - **Emission:** per device, on a MONOTONIC source (an injected `LongSupplier` over `System.nanoTime`; A2):
     - the first answered probe after a boot (the monotonic clock does not survive one — the hub's reading of A2; the draft states it);
     - then the first answered probe ≥ the record interval after the last recorded one;
     - never on a flicker.
   - **Priority:** DIAGNOSTIC (7 d). The hub proposes Doc 01 §3.3's one-level elevation: an instance with `missed > 0` goes to NORMAL (90 d), so a flaky hour outlives a clean one.
3. **The contract (A2).**
   - **Payload:**
     - `class` — mains-metered | mains-floor | passive;
     - `reportIntervalSeconds` | null;
     - `silenceLimitSeconds`;
     - `missesToDark` (2; "asked twice" is a contract term);
     - `recordIntervalSeconds` (3600; null for passive, which is never asked).
   - **Emission:** per device at every boot and re-interview, at NORMAL. This is bounded by boots, heals itself across retention and anchors A3 after a restart. The alternative is on change only; the review weighs it against Doc 01 §6.4 (a purge before a replay from 0).
4. **Rule T1 (`:132`) widened to seven types,** with the three principles quoted at their lines:
   - `:33` raw facts in, derived knowledge out;
   - `:41` the model records facts, not policy — the contract RECORDS the policy and never enforces it;
   - `:39` priority is a retention property, not a correctness one.
5. **R-E arithmetic, re-grepped at the draft (no ungrepped premise):**
   - EventTypes 76 → 78 (`EventTypesTest:46`);
   - the `@EventType`/codec/registry counts each +2 (`EventTypeRegistryTest:131` pins `hasSize(43)`; BOOT0 logs `EventTypeRegistry initialized with 58`);
   - +2 `EventCategoryMapping` rows;
   - every count pin moves in the SAME change (AMD-99 §7).
6. **The projections.**
   - The existing state projection ignores both types, so it does not bump.
   - The recovery-card projection is NEW at v1. **Its path (F1) and number are stated** — from the instrument, or the cut waits for it (D-v102-21).
7. **The stale-record arm (A3).**
   - **Evidence:** the state projection's `lastReported` (FIELDS §1) or the device's latest record of the three types. Without `lastReported`, a chatty plug that is never asked would read stale.
   - **The bound:** the longest a live tracker can leave the device without a record:
     - an asked class: `recordIntervalSeconds` + its time-to-dark (silence limit + K × 5 s);
     - the passive class: its silence limit + one sweep.
   - **Computed** at read time, on the core's clock.
   - **The sixth cell:** "No check recorded since {t}", beside the fifth state.
8. **What does not change:** the probe cadence · a port (none) · the existing projection · `availability_changed`'s shape.
9. **The review** (an agent that has not seen the drafting; D-v101-33's form). Its questions:
   - the FROZEN v1.1 read contract's rule on additive keys, from the contract's own text in the docs repo;
   - F1's path and number;
   - retention × the stale arm;
   - Rule T1's wording;
   - the R-E counts;
   - the monotonic window across a restart.

**The exhibits:**
- Nick's verdict (the DR §3c, verbatim);
- D-v102-14 · D-v102-21;
- BURNIN-1's numbers;
- the comparator pre-read (§7).

## §4 The FE note — HERO-U2c (design mode; a Cowork lane; ≤ 1.5 h; `design/` only)
- **FIELDS §3 re-cut under (f).** The per-probe live keys (`lastProbeOutcome` · `lastProbeAt` · `probeMisses` — (a)/(b)'s) give way to the record's:
  - the last `probe_answered` (`at` · the two counters · `windowStart` · `link`);
  - the contract's five fields;
  - the stale bound.
  - `integrationId` and `ieeeAddress` stay (the act's path).
- **SPEC §7 gains the sixth cell** and the third state's sentences under (f) — e.g. "Quiet since 03:02 · checked 07:02, it answered" and "answered 37 of 49 checks this hour" — with Level and Words by the SPEC's method.
- **Dispatched after AMD-103's draft is filed** (it reads the draft's payloads). It lands as a core commit, `web-ui/dashboard/design/` only.

## §5 AVAIL-API-1 — the cut and the lane
**When:** cut Mon Oct 12 (v105 or v106), after `AMD-103: ratify` and HERO-U2c's landing; its pre-verification runs at the sha it is cut at.

**What — two phases, one review:**
1. **THE RECORD:**
   - the two types and R-E's pins;
   - the tracker's emission (the counters · the monotonic window · `link`);
   - the contract at boot and re-interview.
2. **THE READ:**
   - the recovery-card projection v1, on the ruled path, logging `projection.replay.duration_ms` and `events_replayed` as the state projection does (`StateProjection.java:588`);
   - the keys FIELDS §3 names;
   - the stale arm;
   - IR-143 rides.

**After it:** HERO-U3 wires the S3 cells (IR-145's mirror keys; contract v1.1.7).

**The gate:** the independent review before the landing card; CI is the gate of record.

**Dates:** target landed Fri Oct 16; the freeze list's last day is Tue Oct 20. Past it, the third state goes post-run — the mocked card ships and S1/S2 are live.

## §6 The rig to the freeze (one hardware act per evening)
- **Tonight ≈ 21:00: SOAK-NIGHT-2** (S0 + S1). Added at this close:
  - **P11′** — Nick's correction: the S31's single-miss flickers;
  - **P12′** — the long-gap resume;
  - two read lines — S0 prints LOG0's first availability lines; S2 prints each S31 timeout with its next probe;
  - dry-run on the corpus.
  - **Sun 07:00 S2** → v105.
- **Sun ≈ 13:00–17:00: BC9 + REHEARSAL 3.** Re-stamped at v105: BP9 `32bac40`; a cached boot expects 0 `reporting_cluster` lines; `CAPACITY:` and `FOREIGN:`.
- **Mon Oct 12: dry-run #1.** Its packet gains two rows for F1 and A4:
  - the type counts (`availability_changed` and the store's rows);
  - a timed full scan of BACKUP-1's copy — the replay floor, read on the copy, never the live store.

  These join the rows already ruled: `du` · `timedatectl` · IR-56's row · BACKUP-1 Part 0 · STARTER-1 Part 0b · F-6 per class · the automation-runs row.
- **Oct 17–18: BC10 + SOAK-NIGHT-3** (the word `BC10:`). The landed sha on a backed-up card:
  - AMD-102 R-E's `issues=0` read;
  - the first `probe_answered` and contract rows read from the store;
  - the new projection's replay timed at its first boot.

  The one-way door is opened with a restore behind it, not inside dry-run #2.
- **Then:**
  - Oct 19–21: J3 as dated;
  - Oct 20: PI-2;
  - Oct 22–23: dry-run #2 → THE FREEZE;
  - Oct 30 – Nov 2: the run.

## §7 The comparator pre-read (the hub's agent; primary sources fetched today — a pre-read, not the lane)
| Nick's recollection (08:31) | Verdict | The numbers |
|---|---|---|
| Z2M pings active devices on a 10-minute default | CONFIRMED, with two qualifiers | `availability.active.timeout` 10 min is a silence timer ("check-in every 10 minutes. If they don't, they will be pinged"): a `genBasic` read, tried twice 3 s apart; online/offline published retained on change; passive 1,500 min, never pinged; **the feature is off by default** |
| ZHA marks a mains device unavailable after ≈ 2 h | CONFIRMED — and ZHA asks first | `consider_unavailable_mains` 7,200 s (battery 21,600 s); a 30–45-s check loop; past the threshold, one Basic `manufacturer` read per cycle; unavailable after 2 missed |
| No incumbent records probe outcomes | CONFIRMED for Z2M and ZHA · NOT FOUND for SmartThings, deCONZ, Hubitat | Z2M and ZHA keep availability in memory (Z2M logs failed pings at warning); SmartThings exposes ONLINE/UNHEALTHY/OFFLINE + `lastUpdatedDate` |

**What it changes in the sentence:**
- Both incumbents ASK before naming a mains device dark — a Basic read, twice — so K = 2 is common practice. What differs is the threshold (10 min and opt-in · 2 h · ours 70 s / 670 s) and the record.
- The safe wording: "no structured, queryable per-probe history in the sources checked".

**Sources:**
- zigbee2mqtt.io/guide/configuration/device-availability.html
- github.com/Koenkk/zigbee2mqtt/blob/master/lib/extension/availability.ts
- github.com/zigpy/zha/blob/dev/zha/application/const.py (and `zha/zigbee/device.py`)
- developer.smartthings.com/docs/devices/health

The lane (`RESEARCH-LH: comparator`; D-v102-23's form) re-checks these and adds automation tracing.

## §8 The order
**Sat:**
1. The v103 close card.
2. PKG-FRESH-1 (running).
3. **v104 boots** with `PKG-FRESH-1: <line>`.
4. Its intake, two layers: P1–P7 of the card, with P12′'s first read at D2.
5. LIVE-RENDER-1 (the Pi back on `37f05a9`; ≈ 10 min at the desk).
6. AMD-103 drafted, then its review, then `AMD-103:`.
7. BEAT-RENDERER-2 dispatched when the desk is free (≤ 3 h; its own worktree).
8. ≈ 21:00 the soak from disk.
9. v104's close cuts v105's text.

**Sun:** S2 → v105 → BC9 + REHEARSAL 3 → HERO-U2c → the AMD-103 docs card → the dry-run #1 packet cut and dry-run.

**Mon:** dry-run #1 → AVAIL-API-1 cut.

**Tue–Thu:** the lane.

**Fri:** the review and the landing.

## §9 Nick's words (H10; silence = the recommendation; each refutable by the word or by `REVERT`)
1. **`AMD-103-PATH: a | b`** — the recovery-card projection's replay path (F1).
   - Rec: **a**, with the instrument first.
   - Refutable-by: dry-run #1's timed scan over the ceiling the review names.
   - Blocking: AVAIL-API-1's cut (Mon), not the draft.
2. **`BC10: oct17 | oct18 | no`** — one rig night on the landed sha before dry-run #2.
   - This amends "`da9ca3d` first deploys by dry-run #2's card"; BC10 carries AMD-102 R-E's read.
   - Rec: **the evening after the landing**.
   - Refutable-by: a landing after Oct 18.
   - Blocking: nothing before Oct 16.
3. **`RESEARCH-LH: comparator`** — the lane, Sunday or Monday daytime (Cowork; no rig; no code).
   - Rec: **yes**; the 08:31 verdict already assumes it.
4. **`RENDERER-2: today | later`** — BEAT-RENDERER-2 (IR-140): the hub's per-beat cost, and the gated card that closes IR-101.
   - Rec: **today**, after PKG-FRESH-1 returns; it answers the context cost named at 08:46.
5. **`AMD-103: ratify | edits <…>`** — after v104's draft and its review.

## §10 Refutable-by (the plan as a whole)
- **D2's boot shows the metering class ANSWERING the probe.** Then P3′ is answered early and IR-137 records it; the contract regime's premise is re-read before AMD-103's class rows.
- **The S31 flickers ≥ 10 tonight.** Then the floor class's record interval is revisited BEFORE the cut (A4).
- **The review is NOT-READY on a blocking finding Nick must rule.** Then the cut slips a day; Oct 20 holds.
- **AVAIL-API-1 is not landed by Oct 20.** Then the third state goes post-run, and the mocked card ships.
- **Dry-run #1's scan exceeds the ceiling.** Then path (b), or the third state goes post-run.
