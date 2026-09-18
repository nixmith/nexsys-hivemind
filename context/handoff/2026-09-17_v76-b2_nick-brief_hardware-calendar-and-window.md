<!--
file: context/handoff/2026-09-17_v76-b2_nick-brief_hardware-calendar-and-window.md
purpose: Nick's v76 b2 brief, verbatim (the body below is byte-identical to `_scratch/v76/2026-09-17_v76-b2_nick-brief_hardware-calendar-and-window.md`, md5 da2c322d27decd8b5fdc198e8750a9b8): the order placed, the hardware calendar, four DEVICE-SET edits, the reporting-volume row, the Monday divisor read, the window, the narrowed strategy brief, his confidence ranking. Attacked in context/audits/2026-09-17_v76-b2_nick-brief_hardware-calendar_attack_audit.md.
audience: the hub (the record) · Nick (his own words, on disk)
state-type: brief record (Nick's words; never edited)
status: FILED v76 beat 2 (Thu 2026-09-17 ~21:1x CT; instrument 2026-09-18T02:15:55Z)
-->

# NICK -> v76 b2 — the order placed, the hardware calendar, four DEVICE-SET edits, one row to attack

Thu 2026-09-17 evening CT. Read this as a brief, not a dispatch: §4 and §5 are mine
rather than the plan's, and I want them attacked before they are absorbed.

## §1 WORDS

```
HIVE: LANDED 5bbbd14
DEVICES: extended <edits — §3>
GAPS: neither
HOTMOBILE: skip
FOP: apply
STRATEGY: after-R5B — with a narrowed brief (§7)
CASCADE: engine
AMD100: ratify
NAME: (silence = ii, unchanged)
REPIN: none — Saturday stays pinned to 6bd8508's run #56
```

`HIVE: LANDED 5bbbd14` verified before writing this: nexsys-hivemind HEAD
`5bbbd1443f888d3507d2b67f30490d807116f976`, porcelain 0, ahead 0. The other four
HEADs unmoved — core `3af6213` · skills `180375f` · bench `f3631cb` · docs `7221ddc`.

`PROTECT: done` — I click the six tonight. If the next beat has no `PROTECT: done`
from me, chase me for it. It has been owed since 09-10, and every audit in this
project rests on history being immutable.

`ERIK:` — no line. I send him one tonight with a date in it: if nothing by Fri 09-25
I plan around the opinion rather than waiting on it. The knockout lane should not sit
behind an unanswered email.

## §2 THE HARDWARE CALENDAR — at the order, not at the plan

Two Amazon orders placed Thu 2026-09-17, $202.21 total.

| Arrives | Item | Role |
|---|---|---|
| **Sat 09-19** | Third Reality Smart Plug Gen3 | metered plug, vendor 2 |
| **Sat 09-19** | SONOFF SNZB-06P24 | IR-18, mmWave presence |
| **Sat 09-19** | clamp lamp x2 (EP 18/2, 6 ft) | the load fixture |
| **Sat 09-19** | SURAIELEC watt meter | cross-check B1 |
| **Mon 09-21** | "Upgraded" watt meter | cross-check B2 |
| **Wed 09-24** | P3 P4460 Kill A Watt EZ | **reference A** |
| **Wed 09-24** | 40 W A15 E26 appliance bulbs x4 | **the known load** |

**THE CORRECTION THAT MATTERS: Saturday's box enables no measurement.**

The reference meter and the load both land Wed 09-24. The Saturday and Monday items
are two Zigbee devices THE ADOPTION FENCE forbids pairing, a cross-check meter with
nothing yet to cross-check against, and clamp lamps with no bulbs.

So the operative hardware date is **Wed 09-24, not Sat 09-19**. Saturday's delivery is
inventory, not capability. Plan §2 row 3's "units in hand by the week of 09-28" is
still MET with four days to spare and rehearsal 2 (wk 10-05) is untouched — but no
metering act is possible before Wednesday, and I do not want a beat written that
assumes otherwise.

The consequence I want planned around: **every hour between now and Wednesday is desk
work.** There is no hardware-gated act anywhere in the window. That is not a problem
to route around — it is the window's actual shape, and it argues for landing
ENERGY-READ and the bench scenario BEFORE Wednesday, so the hardware walks into a
finished harness rather than the reverse.

**Unconfirmed in my own order:** I do not see the Hue SML003 in either order. If it is
absent it does not block — ZIGBEE-GAPS row 7's instrument is "unit tests on recorded
signatures," and SML003's EP2 signature is published at zha-device-handlers #1417, so
IR-24 needs the signature, not the device. It costs IR-18 its second vendor, in
October. Flagging rather than assuming.

## §3 DEVICE-SET / D-v75-6 — four edits, all forced by stock

**(a) The PN2000 is DISCONTINUED. So is the UNI-T UT230B-US, its closest replacement.**
Checked at the makers: poniie.com has no cart for it; UNI-T's own product page and the
Amazon listing are both dead. The PN2500 is not a substitute — it is a 25 A Wi-Fi
EV-charger pass-through monitor, and at 0.67 A I would be reading at ~1% of its range.

The finding behind the finding: **the spec'd consumer plug-meter tier no longer exists
in production.** What remains is sub-$25 generics publishing no accuracy figure at all,
and bench power analyzers from ~$1,500 (Yokogawa WT300E, Fluke Norma). Poniie and
UNI-T *were* the middle tier. DEVICE-SET §1 should carry this as a market row, because
it also means the P4460 already ordered is one of the last instruments in that tier:
the scarce thing is the one we have, not the one we lost.

**(b) A and B SWAP. A = P4460.** The P4460 manual's spec table, read whole: active
power 0–1875 W **0.5% typ / 2% max**; RMS current 0.00–15.00 A 0.3%/1%; RMS voltage
85–125 V 0.2%/1%. Its watt resolution — DEVICE-SET §4's open row — reads 0.1 W in the
secondary record; I confirm it at the display on 09-24.

The PN2000's Class 1.0 is **twice as loose on power**. Its only edge was 0.01 W
resolution, which at an 80 W load is 0.0125% and vanishes inside every other term.
D-v75-6's refutable-by was "a meter under $100 stating Class 0.5 or better on POWER."
The P4460 states it. **The refutable-by fired from inside the order.**

**(c) B becomes TWO no-spec generics of different brands** (Suraielec, "Upgraded"),
replacing the single PN2000 at lower total cost. The reasoning, to attack:

1. The predicted failure is not a few percent. DEVICE-SET note 3 predicts
   acPowerDivisor in {1, 100} — a **100x ambiguity**. A $20 meter resolves that
   perfectly; no specification is needed to distinguish 80 from 8,000.
2. B's other job is catching A being systematically wrong, and for that a DIFFERENT
   MANUFACTURER matters more than a published class. A no-spec meter from another
   vendor beats a second P3 unit with a spec sheet, because two P3 units share a shunt
   design and would agree while both were wrong.
3. Two Bs make a disputed reading ATTRIBUTABLE rather than merely detected: if both Bs
   agree with each other and disagree with A, A is the odd one out. The single-B design
   could detect a dispute but never resolve it. That resolution is the part of the
   PN2000's job I am buying back — for $40 instead of the HOBO's $335.

**(d) THE LOAD RISES TO 80 W** (two 40 W lamps, two clamp lamps — both ordered). The
band at a divisor-1 Gen4, where the plug reports integer watts:

```
as written (PN2000 A, 40 W):  1.0% + 0.5/40 + 1.6*(0.3/120) = 1.00 + 1.25 + 0.40 = 2.65%
as ordered (P4460 A, 80 W):   0.5% + 0.5/80 + 1.6*(0.3/120) = 0.50 + 0.63 + 0.40 = 1.53%
```

The band nearly halves — every `within` verdict becomes a materially stronger claim —
and 0.67 A sits 3.3x above the P4460's 0.2 A spec floor instead of 1.6x above it.

**METHOD EDIT, the §2 block.** XCHK can no longer be computed from two published
classes. Replace it with a characterization step on 09-24:

```
CHAR   before any rep: A + B1 + B2 on the same 80 W load, ~20 simultaneous readings.
       Record each B's OFFSET from A and its SPREAD. The measured spread becomes the
       XCHK threshold, in place of a published class.
RULE   record the offset; NEVER correct for it. Zeroing B against A calibrates B to A
       and propagates A's systematic error invisibly into the cross-check.
```

This is a transfer-standard characterization at our own operating point, on our load,
at our line voltage — arguably a better number than a manufacturer's population claim.
But it is a real change to THE MEASUREMENT RECORD's first row and I want it audited as
such, not absorbed.

**The chain gains a meter.** `wall -> A -> B1 -> B2 -> PLUG -> LAMP` means three tares
(BSELF becomes B1SELF + B2SELF) and three self-consumptions stacked above the DUT. T1
needs re-writing for it. If you judge three meters in series not worth the added tare
complexity, the fallback is A + B1 with B2 held as a spare — say so and I run it that
way.

## §4 THE ROW I WANT YOU TO ATTACK — ENERGY-READ's reporting volume

The one thing here that is mine rather than the plan's, and the one I most want a
hostile read on.

**Read at `3af6213`, `ReportingConfigurator.java` DEFAULTS:**

```
0x0B04 (ActivePower, attr 0x050B):  min 5 s · max 3600 s · reportableChange 10 raw
0x0702 (CurrentSummationDelivered): min 5 s · max 3600 s · reportableChange  5 raw
```

Both thresholds are in RAW units, against a divisor nothing in main src has ever read:
`grep -rn 'ivisor\|ultiplier'` over integration/ and core/ excluding tests returns only
`BackoffParameters`. There is no scaling layer at all — ENERGY-READ builds it from zero.
Both clusters ARE in DEFAULTS, so `configureDevice` configures them today for any
endpoint listing them (the Gen4's EP1 lists 0006/0702/0B04/FC21), while
`ClusterHandlers.forDevice` has no handler for either, so every frame dies at
`publishStateReported`'s unadopted guard. **HEAD already asks a metered plug to flood
it and throws the result away.** THE ADOPTION FENCE is doing more work than its name
suggests.

The volume, at the predicted divisors, 80 W load:

**CERTAIN — 0x0702 floods regardless of divisor.** It is a monotonic accumulator, so it
crosses ANY fixed threshold eventually. At seMetering divisor 1e6, 5 raw = 5 mWh; at
80 W that accrues in 0.225 s, so reporting clamps to the 5 s min interval.
→ **720 frames/hour/device, on any load, at any plausible divisor.**

**CONDITIONAL on divisor 100 — 0x0B04 adds the same.** 10 raw = 0.1 W there, and line
noise alone (1.6*dV/V = 0.4% of 80 W = 0.32 W) exceeds it continuously.
→ another 720 frames/hour/device. At divisor 1 (10 raw = 10 W) this leg is quiet except
on edges plus the hourly max-interval heartbeat. My flood claim is strong only for
0x0702; I want that distinction preserved, not flattened into one number.

Over the 72-hour run, three metered plugs (2x Gen4 + TR3):

```
floor   (divisor 1)   ~155,000 metering events
ceiling (divisor 100) ~311,000 metering events
```

Either way metering is the large majority of the run's total event volume, and the
multiplier between floor and ceiling is a constant we have never read.

**UNKNOWN — whether that volume matters.** This is the actual gap: nothing measures it.
`BusSoakIT` is K=20 hero loops reporting delivery latency p50/p99/max and an anomaly
count. No sustained-RATE dimension, no storage-growth dimension, no memory-over-hours
dimension. The 72-hour run in October would be the first time this system has ever run
for 72 hours.

**What I am asking for, and why it is small.** Not a new lane. Two folds:

1. **Into ENERGY-READ's charter.** IR-25 is framed as a correctness fix (the
   divisor-scaled reportable change). Make it a SIZED decision — require the charter to
   state predicted frames/hour/device at each candidate divisor, before and after the
   scaling, as a §. The z-style scaling (`change = engineering_units * divisor`) takes
   0x0702 from 720/hour to roughly 16/hour at 80 W: a ~45x reduction. That is not a side
   effect of the correctness fix, it is arguably the larger consequence, and it should
   be chosen deliberately rather than inherited.
2. **Into the bench lane's owed `metering-known-load.yaml`,** or beside it: a
   sustained-rate row — N frames/sec for M minutes against the ingestion path, recording
   events/sec, DB growth/hour and heap over time. Desk work. No hardware. Available all
   week.

**Refutable-by, ordered by how much each would cost me:**

- a device profile in the fixture set that puts `configure_reporting` in
  `interviewSkips` for metered plugs by default → the flood never configures and the
  row shrinks to a fixture note;
- a real Gen4 read showing acPowerDivisor = 1 AND a seMetering multiplier/divisor pair
  making 5 raw a coarse quantity → the certain leg weakens;
- an existing bench or CI row I have not read that already measures sustained event
  rate or DB growth → the instrument exists and I withdraw fold 2;
- your own read that 311k events over 72 h sits comfortably inside measured headroom →
  say so with the number and I stop raising it.

I am not claiming the run will fail. I am claiming the largest single input to the run's
event budget is unmeasured and set by a constant we have never read, three weeks before
a four-day unattended run we cannot cheaply repeat.

## §5 PROPOSED PACKET — the Gen4 divisor read, next week

**The prize.** DEVICE-SET note 3 predicts acPowerDivisor in {1, 100}; no Gen4 read on
record shows 10. The fixture replays 1/10/100 precisely because the value is unknown.
Today that value is retired at rehearsal 2 (wk 10-05) — three weeks before the run,
with one week of float behind it under the slip rule. It also sets §4's volume.

**The act.** After the sitting and after Sunday's intake is filed: update both Gen4
units to firmware 2.0.0 over Wi-Fi (no Zigbee interaction — this can happen Friday),
then a READ-ONLY interview of ONE unit: no adoption, `configure_reporting` in
interviewSkips, device removed afterward. ~20 minutes at the rig. Answers the divisor
P-row; IR-20(a)'s device-type print (0x010A -> `fallback` -> SWITCH at
`EndpointClassifier.java:41/:99/:102/:186`, which I want to SEE rather than infer); and
whether firmware 2.0.0 actually adds cluster 0x0400 as the Shelly changelog claims while
the device-features doc does not.

**Against it, honestly:**

- It cuts against §WHAT-YOU-DO-NOT-DO ("pair the Gen4 plugs before ENERGY-READ") and
  against THE ADOPTION FENCE as written. My argument is that the fence governs
  ADOPTION — trusting a device's numbers — and an interview is a read, not a trust. But
  that distinction is one the fence does not currently make, and minting it is yours.
- **NOT during Saturday's sitting.** A seventh device joining mid-sitting contaminates
  R-5B's fleet floor, the re-seen/adopted split and the S31 count.
- A join is a `tc_join`. Whether that muddies P-B2's ZDO analysis before C-003's clause
  is drafted, you know and I do not. If it does, this waits until after C-003.
- **Unverified premise:** I do not know that HEAD can interview WITHOUT adopting.
  `SKIP_CONFIGURE_REPORTING` exists in the profile's interviewSkips and
  `publishStateReported` drops unadopted reports, but I found no interview-only mode.
  If this needs code, the row costs a lane-day instead of twenty minutes and I would
  rather it wait for rehearsal 2. **Check this before anything else in this section.**

The word, if you want one: `GEN4-READ: mon | after-C003 | rehearsal-2`. My preference is
`mon`; my confidence is low, because three of the four considerations above are yours to
judge, not mine.

## §6 HOW I WANT THE WINDOW SPENT — Thu evening -> Wed 09-24

Within the cap (two lanes + my hands). Nothing here asks for a third lane.

**Java slot — ENERGY-READ**, chartered b2, dispatched Friday, landing before Wednesday.
Unchanged by the hardware delay: the plan already puts the corroboration leg's code
before the plugs are in hand, and the fixture replays 1/10/100 regardless. IR-15 first
stays right — IR-15 (`EndpointClassifier:175–178`) and IR-24 (`:41,:99–101`) are the
same file, so one session over the classifier avoids a second pass and a second CI
cycle. §4 fold 1 goes in the charter.

**Slot 2 — the bench lane**, free, already owing `field_within`,
`metering-known-load.yaml` and the `link-quality.yaml` skeleton. All three are dry-run
and selftest only; none needs hardware; `metering-known-load.yaml` is the scenario
rehearsal 2 runs, so writing it before the hardware lands is exactly the "walk into a
finished harness" move. §4 fold 2 goes here.

**FE-115** stays at b3 as planned — it wants H8-a's real-wire read and cannot move
earlier than Sunday.

**The knockout charter** (D-v74-1) on any free beat, as already slated.

**My hands:**

```
Thu (tonight)  this brief · PROTECT: done, six clicks · the LLC registrar lookup
               (charter 46564936K, one minute) · one line to Erik with a date in it
Fri 09-18      the b2 landing card if there is one · BOTH Gen4 firmware updates over
               Wi-Fi (no rig interaction, so this is free of Saturday)
Sat 09-19      THE SITTING, 10:00, 2.5 h. Untouched. Nothing above competes with it.
Sun 09-20      R5B-2: one paste
Mon 09-21+     the §5 packet if you rule it in
Wed 09-24      unbox · verify the clamp sockets are ceramic and rated well above 40 W
               before a hot incandescent goes in one · burn a bulb in for an hour
               unattended · run the §3 CHAR step on all three meters (~20 min).
               Hardware complete.
```

The shape of it: **the readiness work is entirely software and entirely available now.**
"Hit the ground running when the devices arrive" resolves to "land ENERGY-READ and write
the bench scenario in the six days before Wednesday," not to anything Saturday's box
makes possible.

## §7 STRATEGY — the narrowed brief

`STRATEGY: after-R5B` stands. But cut D-v75-2's brief down, because a general market/IoT
pass is the kind of lane that returns 100 KB nobody acts on.

The question I want answered comes out of ZIGBEE-GAPS §3: our 29.7% is weighted by the
corpus's long tail of definitions, not by units sold. Of the ten retail best-seller
categories the lane read, two have no Zigbee row at all, four are already covered,
metering is in flight — and the only remaining head-of-shelf misses are **color and
buttons**, the exact two rows we fenced. At corpus weighting those are "+14.5 and +6.9
pp." At retail weighting they are the #1 and #5 best-selling categories in the store.

So `GAPS: neither` is right for October — the run's gate has no color or button row, and
every Java lane-day before the soak belongs to ENERGY-READ and LINK-READ. But the
NOVEMBER ranking should be built on retail position rather than corpus percentage, and
the strategy lane's brief should be exactly that: **which number does a stranger ask for
first, and which weighting makes it honest.** THE PREMISE GATE already governs the
outward text; this decides what the outward number even is.

## §8 WHERE I AM LEAST CONFIDENT

Ranked, so you know where to push:

1. **Whether HEAD can interview without adopting** (§5). Unverified. If it cannot, §5
   collapses. Check this first.
2. **Whether 155k–311k metering events over 72 h is actually a problem** (§4). Genuinely
   unknown — which is my point, but it also means the row could be sizing a non-issue.
   The cost of finding out is a bench row, not a lane.
3. **The 0x0B04 leg of §4** is conditional on divisor 100. The 0x0702 leg is structural.
   Do not let them be read as one claim.
4. **Whether a post-sitting Gen4 join muddies C-003's ZDO read.** You have P-B2's shape;
   I do not.
5. **The P4460's 0.1 W resolution** is corroborated from a secondary source, not from
   P3's own sheet, which omits it. Verified at the display 09-24, not before.
6. **Whether three meters in series is worth the third tare** (§3). Fallback named.
7. **Whether the Hue SML003 is in my order at all** (§2). Checking; not blocking.

Nothing here is blocking except `DEVICES:`, which is already spent — the order is placed
and the money is gone. Everything else you can overrule at b2 and I lose nothing but the
argument.
