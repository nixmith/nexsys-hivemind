<!--
file: context/planning/2026-09-14_v75_decision-record.md
purpose: THE v75 DECISION RECORD — Nick's words of the window verbatim (§1), the decisions packaged in H10 form (§3), the rulings folded from his sharpenings (§4). Opened v75 beat 2 (Mon 2026-09-14; instrument 2026-09-14T19:28:03Z) on his beat-1 report. D-v75-1 was packaged in the b1 audit §6 and is RULED here.
audience: Nick (§3 — one word each) · the hub (§1/§4 bind every charter of the window)
state-type: decision record
status: LIVE — opened v75 beat 2. D-v75-1 RULED `FRAME: a`; D-v75-2 (the strategy/market pass), D-v75-3 (cascade parentage), D-v75-4 (the for_duration defect's order) PACKAGED, words open.
-->

# v75 — decision record

## §1 Nick's words, verbatim
**Mon 2026-09-14 ~14:1x CT, on the b1 landing (`cc17ce7`) and the IR-1 run (`IR1: RETURNED … 576`):** "This beat 1 re-pinned H8-a, cut R-5B through 28 greps, wrote the IR-1 instrument and packaged a decision in one beat — the scratch folder shows seven splice attempts to get it through the caps. That is a heavy first beat. Beat 2 should be lean: 114c and FE-114 authored and pasted, nothing else, so the packets sit unchanged until Saturday. Now, F-R4b-C is in R-4b's record at line 393 — `zigbee.reporting_configured: device=0x00124B002FA8D1C5 clusters=1 verified=0 degraded=1` — the emitter at `ZigbeeIntegrationAdapter.java:1020` counts the plug's input clusters that sit in the adapter's default reporting table, which includes 0x0B04 and 0x0702; `EzspCoordinatorProtocol.java:321`'s own comment shows a metering plug reading `clusters=3`. So the map's "no corpus entry" was a miss here, the S31 printed 1, and re-reading it on `6bd8508` with the prediction `clusters=1` is the right refutable-by for `PLUG: two`. And `ZclIngestionUnit.java:128` declares `onFrame(IEEEAddress device)` as a bare hook with no log line on the accepted-frame path — the tokens you can see (`device_join`, `child_join`, `key_established`) are lifecycle, not frames. No packet block can count frames on this artifact. You, as the hub, read the source rather than my brief, which is exactly the two-layer habit working against its own author (the previous, v74 hub/orchestration session). Help shape how we would proceed — the words, in order. You must determine what coding, discussion, and/or research sessions we should dispatch and coordinate, from here. `FRAME: a`. Option (b) is the tail-of-a-tired-session hazard in another costume: a code change to `integration-zigbee` before Saturday means a new artifact, a new CI sample, both packets re-pinned on Friday, and the rig running on a `.deb` the gate has not been re-cut against — and it puts a Java WU ahead of 114c, breaking the series you set (114c → ENERGY-READ → LINK-READ). The store count per device over the window, named as a lower bound, is an honest measurement now, and the per-frame counter belongs where the intake already put it: LINK-READ's first row. Two sharpenings for the hub to carry: the bound should be split by row kind so it is a bound per frame class, with the known multiplier stated (M9.3's deduplicated twins — every SNZB event arrives twice — so the true rate is at least 2× the state rows for those devices); and when the counter is written, its home is `onFrame` (a per-IEEE counter with one periodic INFO summary line, never per-frame logging), so LINK-READ's first row stays small. The "root logger INFO with no runtime knob" is worth its own register row — a runtime log-level knob is an operator instrument every rig packet keeps wishing for — but not before Saturday. We need to plan out how we should most optimally use our time for building the smart home core, researching or testing, etc. On the S31 re-read, one addition: F-R4b-C was filed as unexplained — reporting bound but degraded on a mains device. R-5B's re-read should ⏺ `verified=` and `degraded=` beside `clusters=`, so the sitting either closes that finding or carries it forward with a second reading; the count alone answers the plug question but not the finding."

## §3 The decisions
- **D-v75-1 — the frame-count block: `FRAME: a|b`. RULED `FRAME: a` (Nick, §1) with two sharpenings and one register row (§4).** The b1 audit §6 carries the H10. Applied at b2: R-5B's B3 EXPECTED and §H (the bound per frame class; the SNZB 2× multiplier; no command string changed); IR-20 amended (the counter's home is `onFrame`; one periodic INFO summary line); IR-21 added (the runtime log-level knob — an operator instrument; not before Saturday).

- **D-v75-2 — the strategy/market pass ("how we should most optimally use our time for building the smart home core, researching or testing"): `STRATEGY: now|after-R5B|fold`.**
```
ESCALATION TO NICK
Task: the deeper market/IoT strategy pass with the moat curriculum as its research frame (your close brief at v74; your line at v75 b1)
Question: When does the research lane run, given the cap (two lanes + your hands) and this week's calendar?
Options:
(a) now — a read-only research lane chartered at b3 and pasted when a slot frees (this week's slots: 114c + FE-114 tonight; the knockout charter Tuesday; the bench lane when Java frees). Cost: one lane-day + one intake beat; a slot the knockout or the bench lane would take. Risk: a map that outruns the rig — bounded by the register's field-language law (a market row feeds a date-armored field sentence or a design constraint, or it does not enter) and by "every row names its instrument". Buys: October's charters (ENERGY-READ · LINK-READ · rehearsal 1) written with the market's constraints in them.
(b) after R-5B — the same lane, chartered at b7 with October's charters, pasted the week of 09-21 after the sitting's intake. Cost: the same lane-day, a week later. Risk: none the calendar shows — October's charters are authored ahead and dispatched by nothing before R-5B anyway. Buys: the lane reads the sitting's facts (the fleet floor on six devices, the ZDO clause, the S31's count) and the 114c/FE-114 landings; no slot contention this week; your hours this week go to the sitting.
(c) fold — the hub's own read at the October re-cut (b7), no lane. Cost: a beat. Risk: the hub's context is the limit; the strategy layer is ~100 KB and the market is outside the corpus. Buys: nothing a lane would not buy better.
PM recommendation: (b) — the week's two slots are spoken for by the code lanes that make Saturday's packets richer, the knockout lane is Tuesday's, and a strategy pass grounded on the sitting's facts is worth more than one grounded on the plan's predictions.
Refutable-by: a slot standing free by Wednesday with the knockout lane returned (then (a) costs nothing extra).
Blocking: no. The word: `STRATEGY: now|after-R5B|fold`; silence = (b).
```

- **D-v75-3 — cascade parentage (`cascade.parentRunId` is always null at HEAD): `CASCADE: engine|bridge|drop`.**
```
ESCALATION TO NICK
Task: where a run's parent is minted — the v75 b2 audit §3 K1 (every run starts at RunCausalChain.root(); the causal chain breaks at the device's state_reported root; RunCausalChain.extend has no caller)
Question: Does parentage become an engine fact, a read-time bridge, or a dropped key?
Options:
(a) engine — at run initiation the RunInitiator asks the pending-command ledger whether the triggering event's causation (a state_reported id) confirmed a tracked command; if so the run extends the parent's chain (the unused RunCausalChain.extend/ChainLink — the substrate's own intended path) and cascadeDepth counts for real. Cost: one Core WU (CASCADE-1), a module boundary crossed (automation ↔ the ledger; ARCH-RULE-REACH survey), ~1–2 lane-days. Risk: the ledger's confirmation window (a report that confirms a command minutes later); dedup/cascade limits gain teeth and may bite a legitimate chain — the bench measures. Buys: parentRunId on the wire for every confirmed cascade; the hero's "because automation A turned the lamp on" sentence; loop detection with a real depth.
(b) bridge — at read time, for the confirmed case only: the run's triggering causation → a state_confirmed with that reportEventId → its correlation → the parent's automation_triggered (a bounded time-range scan). Cost: ~half a lane-day. Risk: partial (unconfirmed commands never link); a second scan per explain. Buys: the key non-null for the common case without touching the engine.
(c) drop — the key stays null; the dashboard says "parent not recorded" forever. Cost: none. Buys: nothing.
PM recommendation: (a), as a November row after the 72-hour run's three questions — the run will show whether cascades matter in the household before the engine learns them; the key stays null until then.
Refutable-by: the 72-hour run's first "why did it fire?" that a parent would have answered (then (a) moves up).
Blocking: no. The word: `CASCADE: engine|bridge|drop`; silence = (a) in November.
```

- **D-v75-4 — the for_duration defect candidate (IR-22): `DUR: measure|later`.**
```
ESCALATION TO NICK
Task: at 6bd8508 a for_duration trigger's expiry publishes trigger_duration_expired and validates, but initiates NO run (the v75 b2 audit §2 items 1–2: evaluateMatches starts the timer instead of matching; triggerMatchesEvent has no expiry arm; consumedEventType maps nothing to the expired type; the subscriber's arm is REPLAY bookkeeping; no test asserts a run after expiry; the javadoc's "the trigger still fires" is unimplemented)
Question: Is the "for 10 minutes" automation class measured this week, or does it wait for October's re-cut?
Options:
(a) measure — DUR-0: one RED unit test in DurationTimerTest (a for_duration automation; the injected clock advanced past expiry; initiateRun / automation_triggered asserted), ≈1 coder-hour, right after 114c's landing (Wednesday); if RED, DUR-1 (initiate the run on expiry with the expired envelope as the triggering event; the firing value via startingEventId; ≈half a lane-day + tests) runs BEFORE ENERGY-READ. Cost: a day of the Java slot. Risk: none to the sitting (the artifact stays 6bd8508). Buys: a core trigger class that silently never fires becomes a fact or a misread within the week; the hero's forDuration sentences get their engine.
(b) later — the register row waits for October's re-cut; the series 114c → ENERGY-READ → LINK-READ stands.
PM recommendation: (a) — a silent no-fire on a trigger class the product's canonical automation ("when motion has been absent for N minutes…") depends on outranks a new device class; the measurement is an hour; the fix, if needed, is small and read-side-free.
Refutable-by: a bench scenario or test showing a for_duration automation firing at HEAD (then IR-22 closes as the hub's misread and nothing moves).
Blocking: no. The word: `DUR: measure|later`; silence = (a).
```

## §4 Rulings folded from Nick's sharpenings (binding on the charters that carry them)
- The frame bound is per FRAME CLASS with the known multiplier stated (the SNZB twins → ≥ 2× the state rows); the counter's home is `onFrame` — a per-IEEE counter, one periodic INFO summary line, never per-frame logging (IR-20; LINK-READ's first row).
- A runtime log-level knob is an operator instrument (IR-21) — after Saturday.
- The S31 re-read ⏺'s `verified=` and `degraded=` beside `clusters=`; the sitting closes F-R4b-C on `verified=1` or carries it with a second reading (R-5B §H).
- Beat 2 is lean: 114c and FE-114 authored and pasted; the packets sit unchanged until Saturday (the b2 edits to R-5B are EXPECTED/§H prose on Nick's own asks; no command string changed); no re-pin before Saturday unless Nick says `REPIN: <sha>`.
- The words of the week, in order: `HIVE: LANDED <sha>` (the b2 card) → the two pastes (114c to host-side Claude Code; FE-114 to a fresh Cowork) → `114C:`/`FE114: RETURNED <path> <bytes>` → `Activate: hold` Tuesday (the email as one paste) → `NAME:` silence = ii (the knockout lane Tuesday, on a free slot) → `PLUG-CARD:` (Wed–Thu, after the dossier micro-lane) → `DUR:` (Wed, after 114c lands) → `H8: Sat 09-19 <hh:mm>` → the sitting → `R5B-2:` Sunday → `STRATEGY:`/`CASCADE:` whenever.
