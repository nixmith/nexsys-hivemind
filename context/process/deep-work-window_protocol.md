<!--
file: context/process/deep-work-window_protocol.md
purpose: Lane C of the refinement program (the charter `context/planning/2026-09-05_v64_effectiveness-second-check_and_refinement-program_charter.md` §3) — how ONE window (a hub session, a coder lane, a research lane, a test session) is shaped for a hard problem, so that its depth is spent on the problem and its discipline is checkable at the bytes. Written FIRST (Nick's guard 1) so that W-SKILLS-7 and every later lane dispatch under it.
audience: the hub (shapes every dispatch by it) · every lane (reads §2 as its own contract) · Nick (the §5 one-screen check when he opens a window)
state-type: process protocol (durable; no project state — HEADs, WUs, dates live in the spine)
status: LIVE from v65 beat 1a (Sat 2026-09-05 ~21:42 CT; instrument 2026-09-06T02:42Z). Refined by later passes; ruled laws are never edited here, only added.
-->

# The deep-work window protocol

**The claim this protocol rests on (v62–v64, on the evidence):** the windows that produced the most were the ones that held ONE problem whole — v63 (FIX-1 authored on source, its lane dispatched), v64 (the FIX-1 return audited at the bytes, two cards cut) — and the cost centre in every retrospective was sequencing, not depth: a hub that carried a boot, an audit, two authoring blocks and a close in one window lost time to context, not to thinking (the charter §1). The protocol turns that corollary into a rule with a check.

## §1 One problem per window
A window is opened FOR one problem and closed ON its deliverable. "One problem" means one object the window will leave on disk — a coding instruction, an audited return with its cards, a research verdict, a strategy card, a protocol — plus whatever the spine needs to record it. A second problem enters a window only as (a) an intake that preempts (a lane's return, a red on `main`, an operator's word) or (b) authoring AHEAD OF NEED for the next window, done after the deliverable is on disk and never before. **The check:** the window's spine block names its ONE deliverable in its header line; a header that names two is the tripwire firing late.

## §2 The dispatch names the deliverable, the read-set and the predictions
Every dispatch (a hub session prompt, a lane instruction, a research charter) carries, in this order, before the work: **(1) THE ONE DELIVERABLE** — its path, its cap in bytes, its §0-first shape; **(2) THE READ-SET, IN ORDER** — the files that are law for this window (the newest spine beat, the charter's own section, the instruction's §0), each by path, with "nothing older" stated; **(3) THE PREDICTIONS** — what the window expects to find, filed BEFORE the first read (H12): a census it will land, a mechanism it expects at source, a verdict word's conditions, a count. A prediction is adjudicated FIRST when the evidence arrives — a miss is owned in writing, never explained away (the v64 mint). **(4) THE FENCES** it holds (one lane on the core tree; stage nothing; `TOKLEN-OK`; no name in chat; whichever apply) and **(5) THE CLOCK** — the window's budget and its close condition. A dispatch missing any of the five is re-cut before it is pasted.

## §3 Source-first inside instrument-first
Instrument-first means a live-behaviour premise cites a filed measurement or orders the instrument (arc 1). Source-first, inside it, means: **before ordering the run, read the producer of the artifact the run will yield** — the test's throw, the workflow's upload step, the driver's branch the rig actually reaches. v63 retired two of four ruled instruments this way (the §10-O hunk unreachable in driven mode; CI uploads HTML only) and v64 found the stamp defect (the throw printed no resting checkpoint) — each a run that would have measured nothing. **The order of reads in a deep-work window:** the spine → the charter's own section → the SOURCE the deliverable depends on (MODULE_CONTEXT + `module-info.java` + the producer) → the corpus/the evidence → then authoring. A read that is not on this list is a read the window did not need.

## §4 The boot lean
The boot is pointer-form beyond the listed reads: the newest three beats + the snapshot + the named §0/verdict surfaces + the window's own read-set; archives only via the archive map; a >~15 KB return read §0 first, then targeted sections; the same file never read twice in a window (bank on disk, point rather than copy — the token economy). A hub window's boot is ≈25–30 KB of reads; a lane's boot is its charter section + its read-set and nothing else. **The check:** the intake audit's §0 lists every file the boot read; a list longer than the dispatch's read-set + the spine is a boot that wandered.

## §5 The tripwire and the close
**The tripwire:** past mid-session — or the moment the window's deliverable is on disk, whichever is first — the next window's skeleton is authored (its dispatch's five parts, §2, with slots), so the close never waits on authoring. **The close is on the deliverable, never on the agenda's remainder:** a window closes when its one object is on disk, committed census-exact, the spine written, the next window's skeleton live, and the operator's queue re-cut — with context to spare. A window that continues past its deliverable does so only for intakes (§1) and only while context is healthy; "one more block" after the tripwire is the cliff the v61–v64 closes learned to refuse. **The check:** the closing beat's header says "closed on context health" and names what it deliberately left to the next window.

## §6 What goes to a lane; what stays with the hub
**A lane for anything that RUNS:** code (a coder lane in the core tree, one at a time), a research pass (a fresh Cowork window, read-only web, one return file), a hardware session (a navigator packet in the three-tier license shape), a skills pass (a fresh window on the skills' source trees). A lane's contract is §2 verbatim; it returns ONE file at the named path with `RETURNED <path> <bytes>` as its last line; it stages nothing and commits nothing. **The hub for anything that RULES:** the audit at the bytes (two layers; the non-re-executions disclosed), the cards, the spine, the operator queue, every H10. The hub never implements and never runs a lane's instrument itself — it re-executes the lane's CLAIMS (2–3 checks minimum) and that is a different act. **A hub that finds itself running loops is a hub that should have dispatched a lane; a lane that finds itself ruling is a lane that should have filed a `[REVIEW]` and stopped.**

## §7 The five rituals, where they apply (v65; bounded so that thinking buys deliverables, never verbosity)
In a hub window: **the alternative-shape paragraph** rides every charter, instruction or block the hub authors (one paragraph; one verdict; a losing plan is re-cut before dispatch) · **the leverage line** rides every spine block (the single act that unblocks the most downstream work, its dependency named; if the operator's, it is Act 1 of his queue) · **the 2029 test** rides every long-tail decision (three sentences: glad · regret · the refutable fact) · **pre-registration** rides every adjudication (the frame, then the return) · **the four-lane map** is re-cut when a lane lands, never more often than a beat. In a lane window: §2's predictions ARE the lane's pre-registration; a lane's `[REVIEW]` with line cites is its alternative shape.

## §8 The window budget (one line; Lane B's `window-budget.md` expands it)
A hub window holds: the boot (§4) + ONE audit + ONE authoring block + the next skeleton + the close — ≈five commits; a read-only corpus check no more often than once per 15 minutes; the guarded-splice script fresh per beat (the exemplar is a shape). A lane window holds one deliverable and its return; its clock is stated in the dispatch (4–8 h for research; ≈2–4 h for a coder WU; a partial return at the deadline outranks a complete one after it).

**The alternative shape this protocol did not take:** a per-role protocol (one for the hub, one for coders, one for research), each carrying its own boot and close — rejected: the disciplines are the same five parts in every window (the deliverable, the read-set, the predictions, the fences, the clock), and three files would drift apart at the first pass; one protocol with §6's split keeps the role difference to the one place it lives — who runs and who rules.

## §9 The one-screen check (Nick, when he opens a window; the hub, before it pastes)
- The dispatch names ONE deliverable with a path and a cap.
- The read-set is listed in order, with "nothing older".
- At least one prediction is written that the evidence could refute.
- The fences that apply are named; "stage nothing; commit nothing" is present for a lane.
- The clock and the close condition are stated.
- The last line the window will print is known (`RETURNED <path> <bytes>` for a lane; the census card for a hub beat).
