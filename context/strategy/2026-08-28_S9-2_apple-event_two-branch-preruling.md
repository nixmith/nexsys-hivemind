<!--
file: context/strategy/2026-08-28_S9-2_apple-event_two-branch-preruling.md
purpose: The pre-authored two-branch §9-2 (Substrate Thesis condition 2) ruling for Apple's 2026-09-09 event, so the same-day read is a paste, not a deliberation. Recommended by the RS-3/W-MARKET-2 return (F-2); authored at hub beat 9; R-10 (~Sep 5–6) ratifies or refines before the event.
audience: the hub (the 09-09 read) · the R-10 charter docket
state-type: pre-ruling (conditional; executes against the event record)
status: PRE-AUTHORED 2026-08-28. Not a ruling until executed on 09-09.
-->

# §9-2 pre-ruling — Apple event, Wed 2026-09-09, 10:00 PT ("Surprise and shine"; date verified at apple.com/apple-events, 2026-08-28)

## §1 The condition as written

Substrate Thesis §9 condition 2 triggers when a major platform (a) SHIPS an unbypassable enforcement layer between model output and actuation, first, AND (b) OPEN-STANDARDIZES it. Two halves; both required. **The vocabulary stays binary — TRIGGERED or NOT — with the annotation carrying the nuance. "Partially triggered" is banned: a tripwire that admits partial states stops being a tripwire.** (Ruling of record, beat 9, on the operator's reclassification question.)

## §2 What is known going in (verified 2026-08-28)

WWDC26 session 347 documents an OS-runtime, risk-based confirmation gate for App Intents: decline ⇒ *"execution is blocked, and the intent is never invoked"*; policies strengthen-only (*"if we try to set a weaker policy, we get a build error"*); Apple's own guidance: *"focus on deterministic mitigations as a baseline."* HomeKit/home actuation is ABSENT from the session; the mechanism is proprietary; no open-standardization signal exists anywhere. The strongest platform-side L1 fragment on record — and a fragment, not the kernel.

## §3 Branch 1 — ARCHITECTURAL-HALF-MET-NOT-OPEN → NOT TRIGGERED → HOLD-TO-CHARTER (expected)

Fires when: the event ships or extends the confirmation gate — even into Home / a home hub — with no open-standardization act (no published spec, no third-party license, no standards-body contribution).

The read to file (paste-ready): *"§9-2 NOT TRIGGERED at the 09-09 read: half (a) evidenced at most for [scope as announced]; half (b) absent. HOLD to charter. Annotation: [home scope · third-party gating surface · any licensing word]."*

Consequence already priced (return C4-5, adopted): every class-(iii) enforcement sentence survives Apple-in-home — never "no platform confirms high-risk actions"; always the missing kernel (invariants · rate limits · reversibility classes · attribution · durable record), which the documented mechanism does not include.

## §4 Branch 2 — BOTH-HALVES → RE-ADJUDICATE (unlikely)

Fires when: the event both ships the gate for home actuation AND open-standardizes it (publishes the mechanism/policy schema for others to implement, or contributes it to a body).

The act: open the §9-2 re-adjudication at the NEXT hub beat (not same-hour). Inputs: what exactly is open (API vs mechanism vs policy schema) · home scope · whether the open artifact contains any cross-device/cross-principal kernel or only per-intent confirmation. Scoping note: even a triggered condition 2 contests the CONFIRMATION FRAGMENT, not the kernel — the re-adjudication scopes what is actually contested before any posture moves.

## §5 The null read

No home-agent enforcement mention at all → file a one-line NO-CHANGE note against F-2 and close the 09-09 tripwire to the next natural re-read (R-11 or the next W-MARKET refresh).

## §6 Same-week tripwires that ride along

09-02 HA 2026.9 stable (skim the release post for "why it changed" marketing — the C2-5 naming-window watch) · 09-04..08 IFA (Samsung/LG agent announcements; any enforcement vocabulary) · 09-07 SCITT CCF Last Call ends · 09-17 Silabs certification webinar (C1-1 recheck).
