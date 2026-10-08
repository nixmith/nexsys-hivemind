<!--
file: context/planning/2026-10-07_v99_WHERE-THE-HOURS-GO_Oct8-Oct30.md
purpose: Nick's ask at the v99 close (21:02 CT: "fully plan out how we can most optimally spend our time on coding, development, etc. for our smart ecosystem & company") answered as a hub note: where the hours go from Thu 10-08 to the run (Oct 30), by lane and by what each hour buys, with the tradeoffs named — the rig's critical path, the desk's small Java, the renderer as the hub's own payback, the FE lane's product-truth cluster, the company's dated rows, and the hub's cost. It extends `2026-10-04_v98_HOW-WE-PROCEED_from-here.md` (§2's critical path stands; §3 is superseded by D-v99-12) with what Wednesday taught. Framed as design problems and tradeoffs, not as a schedule; the schedule is THE WEEK (D-v99-12) and THE HORIZON.
audience: Nick (the allocation and its tradeoffs; three words he can give) · the v100+ hubs (the lane priorities until the freeze)
state-type: strategy note (one cut; retired by the Oct 14 close pass)
status: FILED v99 beat 3 (Wed 2026-10-07 ~21:1x CT; instrument 2026-10-08T02:11:44Z).
-->

# Where the hours go — Thu 10-08 → the run (Oct 30), after Wednesday

## §1 What Wednesday changed in the allocation
Three readings move hours, none moves a date. (1) **J1 works on silicon** — 65 s to name a dark plug, the design number to the tenth; the resume on the first frame. The availability model is no longer a premise; it is a fact the product can say. (2) **The product's freshness words disagree with each other at the API** (IR-132 an epoch float where ISO is expected; IR-133 no "last seen" on a healthy device until something happens to it; IR-134 `stale=False` beside `UNAVAILABLE`). These are not rig findings; they are what a household's dashboard would show. (3) **The hub's own cost is now the measured bottleneck**: three beats tonight ran with zero assert trips because every cap was probed in the container first — but the brief sat at 12,226 of 12,288 bytes and the snapshot at 3,495 of 3,500. The renderer is not a nicety; it is the difference between a hub that spends its window on the program and one that spends it fitting prose to ceilings.

## §2 The rig — the critical path; one hardware act per evening (your rule, kept)
The rig buys the only thing nothing else can: evidence on real silicon. Its chain to the run is short and fixed: **the soak (running) → BC9 + REHEARSAL 3 Fri (J2 to the Pi) → dry 24 h #1 Mon 10-12 → dry #2 Oct 22–23 → THE FREEZE → the run Oct 30.** Every rig evening between is either this chain or PKG-FRESH-1 (gate (i)'s instrument, five weeks early — one evening, Thu or Sat, under the two fences). **Tradeoff:** a rig evening spent on anything else (a second soak sample, a Hue re-drive) delays the chain a day each; the Hue and the sensor's class questions wait for R6's matrix nights after the run. **What the rig does not need from the desk before Friday:** nothing — BC9 deploys `49455fc`, which is on `main` and green.

## §3 The desk — the Java is small by design; the renderer first
- **BEAT-RENDERER-1 (≤ 3 h; the hivemind, not core).** Pays back in every hub window after it: the digest and §DIGEST by generation, `beat()` as one call. Your own row (D-v94-16). **First desk block, whichever day has it.**
- **CONFIG-ERROR-1 + IR-122 (+ IR-126, + IR-132 as a rider; ≈ 2 h Saturday).** A dead knob removed or made honest; the epoch float fixed in the same lane if its module allows. Small, bounded, one review. **Tradeoff:** it is not on the run's path; it is on the pilot's — a household that sets `mains_timeout_minutes: 5` and sees nothing change loses trust in every other knob.
- **STARTER-1 (on your word).** As named it is a Java unit, not config (D-v99-11). My rec `a` buys a household's first "it did something" and "it told me something went dark" with zero Java before the freeze; `b` buys a schedule the engine should have eventually, at the cost of a desk day and a composition-root review now. **The question to answer is not "which is faster" but "which first impression do we want the pilot to form" — the engine's deterministic floor (a thing went dark and it told you) is the differentiator; a schedule is table stakes.**
- **The Java slot's ceiling before the freeze:** J3 as-dated (Oct 19–21), IR-56 only on an UNAVAILABLE sample, the hysteresis unit only if the soak's P2 > 2. **Nothing else enters the Java tree before Oct 23** — the freeze is the program's promise to the run.

## §4 The frontend lane — the product-truth cluster (one Cowork lane, Wed–Sun daytime, no rig)
HERO-1 and U2a were already FE-lane work (the perspective §5.1). Wednesday adds the cluster they should carry together: **the dashboard must not lie about freshness.** One charter: the explainability hero (why did it fire · why didn't it · did it actually confirm) + THE RECOVERY CARD (J2's real shape) + the freshness rule — `lastSeenAt` when present, `lastReported` as the fallback (IR-133), one word for "silent" (IR-134), ISO everywhere (IR-132's contract note). **Tradeoff:** the FE lane runs beside the rig and the desk because it touches neither tree the rig or the Java slot owns; its cost is the hub's charter hour and its own intake. It is the cheapest hour in the program per unit of pilot-visible value.

## §5 The company — dated rows, no hub hours
The attorney (aim Oct 8) → `DRAFT:` → the ten-item read → sign → FILED → the receipt → the rename WU; `TM:`; the three conversations; the kit lists (THE HORIZON C1). The hub's only act is reading the draft the day it lands. **Tradeoff:** every public word waits on the receipt (THE PREMISE, D-v80-3); nothing here is accelerated by hours, only by the attorney's calendar.

## §6 The hub — one window a day at most, the renderer in it
Two hub windows a day is the ceiling you set; one is the norm. A window's cost tonight: ≈ 118 calls, ≈ 300 KB read, three cards. After the renderer lands, the target is **one hivemind card per window** (IR-131 (c)) and a boot under 40 KB. **Tradeoff:** the renderer's three desk hours are yours, not the hub's — they come out of Thursday or Saturday's desk block; the payback begins the window after it lands and compounds to the run.

## §7 Three words, when you are ready (none tonight)
- `STARTER: a | b | c` (D-v99-11 — the first impression question).
- `DESK-ORDER: renderer-first | config-first` (default renderer-first; `config-first` only if Saturday is the sole desk block before the freeze and the knob matters more to you than the hub's cost).
- `FE-SLOT: <day>` (the one Cowork FE lane for the product-truth cluster — any day Wed 10-07 → Sun 10-11 daytime; the charter is cut by v100 on the word).
