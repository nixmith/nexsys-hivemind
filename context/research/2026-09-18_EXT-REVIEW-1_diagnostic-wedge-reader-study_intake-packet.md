<!--
file: context/research/2026-09-18_EXT-REVIEW-1_diagnostic-wedge-reader-study_intake-packet.md
purpose: EXT-REVIEW-1 filed verbatim (the body below is byte-identical to `_scratch/v76/2026-09-18_EXT-REVIEW-1_diagnostic-wedge-reader-study_intake-packet.md`, md5 f748dd4804a2f62ab6c251fb6854f754; its own frontmatter names the staging path): a seven-round external critique of the company thesis distilled by an advisory Cowork session into 95 rows — the pre-registration artifacts verbatim. Unadjudicated as written; adjudicated row by row in context/audits/2026-09-18_v76-b3_EXT-REVIEW-1_intake_adjudication_and_the-window-plan.md (the v76 b3 audit); the decisions in context/planning/2026-09-18_v76_decision-record.md.
audience: the hub (the record) · Nick
state-type: intake record (external-origin; never edited; the audit rules on it)
status: FILED v76 beat 3 (Fri 2026-09-18 ~13:0x CT; instrument 2026-09-18T18:02:05Z)
-->

<!--
file: _scratch/v76/2026-09-18_EXT-REVIEW-1_diagnostic-wedge-reader-study_intake-packet.md
purpose: INTAKE PACKET (unadjudicated) — the complete record of a seven-round external critique of the company thesis conducted by Nick with a non-NexSys third party, plus the Cowork session's analysis of each round, the replies Nick actually sent, and every engineering / register / plan consequence that follows. Written FOR THE HUB to adjudicate row by row. Nothing here is a lane return; no charter authorized this work; nothing has been audited at the bytes.
audience: the hub (sole spine-writer; decides what is kept, verified, rejected) · Nick (the decision rows marked NICK)
state-type: intake packet (external-origin; read-only with respect to the spine; NOT written into context/ by the producing session)
status: STAGED Fri 2026-09-18 CT (2026-09-18T17:0xZ) in `_scratch/v76/`. Produced by a Cowork advisory session, not a chartered lane. Every row carries a trust class; the hub rules KEEP / VERIFY / REJECT per row.
-->

# EXT-REVIEW-1 — external critique intake: the diagnostic wedge and the reader study

## §0 The card

**What this is.** Over ~2 days (2026-09-17 → 2026-09-18) Nick ran a seven-round written exchange with one external reviewer (a friend; technically literate; not a NexSys participant; **declined attribution**). It began as a critique of a verbal pitch and converged into a fully specified, pre-registered, falsifiable experiment: a **blinded reader study** comparing the diagnostic value of this project's causal record against Home Assistant's ordinary evidence trail on a fixed incident corpus. The reviewer has pre-registered priors, offered to grade blind, and written stop rules that can fail the thesis.

**What this is not.** Not a research return. Not a lane. Not verified. Not a decision. The reviewer is one person with no visibility into HEAD, the register, the plan or the code; several of his assertions are wrong or assume capabilities that do not exist. The Cowork session that produced this packet argued back in every round; the disagreements are recorded as first-class rows.

**Recommendation in one line.** Keep the *method* (§6), keep four engineering concepts (E-2, E-4, E-6, E-7), keep one process lesson (R-5), **hold the full January study apparatus behind a cheap three-reader pilot** (§6.6), and rule on whether any of it displaces work in the current window.

**Decision rows requiring a ruling**

| Row | Decision | Owner |
|---|---|---|
| D-EXT-1 | Does the reader study enter the plan at all, and at which beat? | HUB + NICK |
| D-EXT-2 | Is the 72-hour run reclassified as a **soak/stability gate** rather than claim proof? (§R-1) | HUB |
| D-EXT-3 | Does "declared input freshness/cadence" (E-4) enter the automation definition language? | HUB |
| D-EXT-4 | Does the read-API freeze admit the additive verdict vocabulary (E-3, E-5, E-6)? | HUB |
| D-EXT-5 | Is the premise gate extended to spoken/informal pitches? (R-5) | HUB |
| D-EXT-6 | HotMobile 2027: submit by **2026-10-09 AoE** or skip this cycle? (FOP-1 finding, 21 days out) | NICK |
| D-EXT-7 | Does the pilot (§6.6) run before or after the current window's committed work? | NICK |

---

## §1 How to read this file — provenance classes

Every substantive statement below carries one tag. The hub should treat the tags as the gate.

| Tag | Meaning | Default hub posture |
|---|---|---|
| `[EXT]` | Asserted by the external reviewer. One person's opinion. No independent basis supplied. | VERIFY or REJECT before any use |
| `[EXT-CITED]` | Asserted by the reviewer **with** a citable source he claims to have checked (e.g. HA docs). | VERIFY at the source |
| `[VER-0917]` | Verified in the FOP-1 research lane on 2026-09-17 at a live source; return filed at `context/research/2026-09-17_FOP-1_return.md` (9,982 B). | KEEP |
| `[CODE-RECALL]` | This session's recollection of repo state **from the b6 audit trail read on 2026-09-17**, NOT a fresh grep. Core has moved since (see §1.1). | GREP before relying on it |
| `[SESSION]` | Analysis/argument produced by the Cowork session. Reasoning, not evidence. | Judge on merits |
| `[NICK-SENT]` | Language Nick actually transmitted to the third party. A soft external commitment exists. | Note as commitment |
| `[OPEN]` | Unresolved; named in §9. | — |

### §1.1 Staleness warnings the hub must apply

1. `[CODE-RECALL]` rows reference core **`3d40b5f`** (v75 b6 grep). The v76 b1 card shows CI #252 green on **`3af6213`**. All code rows are therefore **at least one commit stale** and possibly more. Re-grep before any of them informs an instruction.
2. Schedule statements in this packet assume the **v75 plan of record** (72-hour run Fri 2026-10-30 → Mon 2026-11-02; ≈7 h/week). The **v76 b2 brief re-cut the calendar (Wed 09-24 operative)**. The hub must reconcile every schedule claim here against the current plan of record; where they conflict, this packet is wrong.
3. The device bridge dropped mid-exchange and reconnected at the end. No grep, no HEAD read, and no register read was performed while the analysis was produced. The FOP-1 lane's verifications (2026-09-17) are the only first-hand source used.

---

## §2 What happened — the seven rounds

| # | Reviewer contributed | Session's principal counter | Net movement |
|---|---|---|---|
| 1 | Broad strategy letter: technically valuable, commercially unproven; wedge = multi-site property ops / small commercial; enterprise-grade checklist; safe-AI actuation tiers; correct the compliance claim. | The enterprise wedge contradicts his own cost analysis at ~7 h/week; the differentiator is not setup ease but the silent non-event; the letter has **no timing argument**; substitute *measurement* for *assurance*. | Wedge narrowed to the integrator truck-roll / observability layer. |
| 2 | Rewrote the claim into a falsifiable form; proposed the 72-hour run as a technical gate with a fault-injection matrix; proposed the blinded diagnostic comparison; "a clean run may be uninformative." | The metric table imports **presence-quality numbers from a different program**; ground truth is asymmetric; the watts channel is unlanded; 100 % trace completeness is the wrong target (null census exists). **Gate the record, measure the world.** | Run reclassified; corpus split from soak. |
| 3 | Layered verdict model (state → decision → command → confirmation) with six invariants; coverage orthogonal; 11-case corpus; author-bias controls (frozen manifest, external oracle, randomized order, embarrassment cases); reader packet + scoring; 10-question buyer test. | It is a **DAG, not a chain** (causation/correlation ids); "every *expected* decision" hides the expected-set problem; **all invariants stop lying, none stop uselessness**; split verifier cases from reader cases by cost; add the mismatched-value case. | Usefulness floor requested. |
| 4 | Usefulness floor: 6 of 7 actionable in ≤10 min, 0 unbounded unknowns, 0 false-confident; `verdict_provenance`; determinate / bounded / unbounded taxonomy; "actionable" = one of five operator actions. | The floor is **single-arm** — it forgot the baseline; counts don't scale (he added a 9th packet in the same letter); failures need record/presentation/reader triage; missing **`negative`** and **`superseded`**; `in_progress` is not terminal; tolerance from device capability. | Parity labels requested. |
| 5 | Parity matrix over 8 packets; "ordinary HA evidence bundle" definition; split stale-input into 4A/4B and use 4B; revised gate; `confirmation_verdict` + `confirmation_status`; four-way reader-error triage; second grader. | Only 3 packets are competitive and 2 have architecturally predetermined outcomes — the real unknown is **reader improvisation**; trace retention makes *when the reader looks* decisive; **you cannot explain a non-event without a declared expectation** (4B may be bounded, colliding with the gate); symmetry of the evidence rule; don't contort suppression to suit the baseline. | Priors requested. |
| 6 | Pre-registered baseline priors for packets 4/5/8; minimum meaningful differences; per-packet targets; five interpretation rules; hypothesis statement. | **Power**: per-packet proportions are unresolvable at feasible n (~50 obs/arm/cell needed); pair it; pool the primary; censored median → report resolved-within-cap; 2:30 target is below the task floor; **missed dispatch** is the missing symmetric error; run the **baseline arm first, alone, sequential hardware** as the cheap kill test. | Grading protocol requested. |
| 7 | Accepts blind grading with conditions; refuses sole-adjudicator status; corrects the clustering error; symmetric "correct operational disposition" endpoint; five-point confidence; frozen scoring charter; masked packets; second grader; standalone kill rule request. | The apparatus now costs more than the decision it informs → **crude pilot first**; the answer key must be **system-neutral** or the baseline is graded in a vocabulary it cannot speak; arm-blinding the grader is infeasible → two-stage grading; kill rule must be single-arm; confidence couples with the cap. | Closed. Reviewer declined attribution. |

**Coda (round 7 reply).** Reviewer corrected the session's `p≈0.002` figure: that is the *floor of the scale*, not a prediction, and the floor itself moves with ties. Accepted. He also endorsed the pilot and the kill-quickly sequencing.

---

## §3 External assertions — `X-nn`

Each row: claim, trust class, session position, recommended hub posture.

| ID | Assertion | Class | Session position | Posture |
|---|---|---|---|---|
| X-1 | A feature-complete HA alternative is not by itself a business; parity is necessary, not sufficient. | `[EXT]` | Agree. The HA-parity framing was Nick's pitch error, not a product property. | KEEP as framing discipline |
| X-2 | Chain hashing alone does not establish trustworthy auditability; signed checkpoints, key custody, verified time, retention/legal-hold are required. | `[EXT]` | Agree, and it is correct against HASH-1 as understood. HASH-1 is *measurement*, not assurance. | KEEP — do not let HASH-1 be described as audit evidence |
| X-3 | "Complies with local, state and federal laws wherever used" must be retired; replacement wording offered. | `[EXT]` | Agree unreservedly. Retired by Nick in round 1. | KEEP — see R-5 |
| X-4 | The wedge should be multi-site property operations or small commercial buildings. | `[EXT]` | **Reject.** His own enterprise checklist (tenant isolation, SSO/SCIM, data residency, pen-test evidence, RPO/RTO) is a staffed roadmap; incompatible with ~7 h/week. | REJECT (superseded by X-5) |
| X-5 | Revised wedge: an automation observability and confirmation layer that explains silent non-events and unconfirmed physical actions, deployable beside an incumbent control system. | `[EXT]`+`[SESSION]` | Converged position of both parties. | HUB-RULE (strategy) |
| X-6 | HA's automation trace is created **when an automation runs**; documented default retention is **5 stored traces** per automation. | `[EXT-CITED]` | Load-bearing for the whole study. Reviewer says he verified it. | **VERIFY at HA docs** |
| X-7 | HA's event/state model carries context attribution linking related events and state changes. | `[EXT-CITED]` | Plausible; affects the parity label on packet 7. | VERIFY |
| X-8 | HA's troubleshooting docs distinguish an action that ran from one that returned an error, but not that the endpoint reached the intended state. | `[EXT-CITED]` | Consistent with the register's dated line. | VERIFY |
| X-9 | Matter 1.6's Thermostat Suggestions formalize: ecosystem suggests → endpoint evaluates against local context/preferences → may explain a non-follow. | `[EXT-CITED]` | Composes with a system-level why-not one layer up. Matter 1.6 release date **6/17/2026** is `[VER-0917]` at the CSA newsroom; the *ambient-sensing* clause is third-party, not in CSA's release text. | KEEP (date verified); VERIFY the suggestion-explanation clause |
| X-10 | Do not let an LLM be the final authority for a physical action; policy engine outside the model; typed allowlisted actions; treat ingested content as hostile; shadow mode before autonomy. | `[EXT]` | Agree; it is approximately the deterministic policy kernel already claimed as the field's missing floor. Independent derivation of the same architecture is useful corroboration. | KEEP as corroboration only — **not** a new claim |
| X-11 | A clean unattended 72-hour period may be uninformative: no drops, no stale data, no non-confirmations, no races = ordinary operation tested, not the claim. | `[EXT]` | Strongest single point in the exchange. | KEEP |
| X-12 | Pre-registered baseline priors (§6.2) and minimum meaningful differences. | `[EXT]` | Honest (not catastrophic for the baseline); the only genuinely falsifiable artifact produced. | KEEP as pre-registration |
| X-13 | Parity matrix (§6.1): packets 1–3 parity, 4 and 5 blind spots, 6 calibration, 7 partial, 8 secondary. | `[EXT]` | Accepted with one correction: labels 4/5 are *predictions about the incumbent*, not about reader outcomes. | KEEP |
| X-14 | "Ordinary HA evidence bundle": config, trace if any, logbook/history over the window, entity states/attributes in the normal interface, standard context attribution. **No** post-hoc custom logging, SQL, or templates. | `[EXT]` | Accept, **with symmetry** (binds our arm too — see S-9). | KEEP |
| X-15 | Reader-level clustering: 30 reader-by-packet observations are not independent; the exact test's unit is the reader. | `[EXT]` | Correct; the session's earlier phrasing was loose. Conceded. | KEEP |
| X-16 | Packet 5 at 1 h and 24 h is a retention *condition*, not an independent incident; do not double its weight in the pooled primary. | `[EXT]` | Correct. | KEEP |
| X-17 | Primary endpoint must be **correct operational disposition** with error direction retained (unnecessary vs missed dispatch). | `[EXT]` | Correct and important; closes the "suppress truck rolls by making readers wrongly comfortable" hole. | KEEP |
| X-18 | He should not be the only adjudicator (he shaped the rubric and priors); recruit a second grader who does not know the architecture; report disagreement, do not average; adjudicate against the frozen charter before arm revelation. | `[EXT]` | Correct and good faith. Recruiting cost is real and unscheduled. | KEEP; cost in §10 |
| X-19 | Do not pre-register an anticipated p-value; pre-register the statistic and permutation procedure. | `[EXT]` | Correct. | KEEP |
| X-20 | If three competent HA users solve the strongest silent-non-fire case in ~3 min with sound dispatch decisions, stop investing in the truck-roll wedge until a harder/more representative incident or a different buyer problem is found. | `[EXT]` | Accepted **with the asymmetry in S-14**. | KEEP with S-14 attached |

---

## §4 Session analysis — `S-nn`

Arguments made by this session. Reasoning, not evidence. The hub should judge each on merits and may reject any of them.

| ID | Argument | Bears on |
|---|---|---|
| S-1 | The differentiator is not setup ease. It is the silent non-event and the unconfirmed action — narrow, dated, refutable, and matching the register's HA line (RS-3 §6.1-1, 2026-08-28, refutable from 09-02). | Positioning |
| S-2 | The reviewer's letters contained **no timing argument**. Matter 1.6 (6/17/2026) with Joint Fabric and thermostat suggestions is an intent-evaluated-against-local-policy model — architecturally what was built — and provisional definitions are moldable. | Positioning |
| S-3 | Substitute **measurement for assurance** at this stage: pen tests, SOC-2-adjacent evidence and references are unaffordable; a measurement nobody in the field publishes is not. | Evidence strategy |
| S-4 | **Gate the properties of the record; measure the properties of the world.** Record properties (partition, terminality, no unflagged unconfirmed command) are zero-tolerance and mechanically checkable. World properties (how often a sensor lied) are counted and published, defects included. | §6, verifier |
| S-5 | The four presence-quality numbers (latency-to-detect, latency-to-clear, false-clear-while-stationary, false-hold-after-vacancy) belong to the **dataset/longitudinal program**, not to the unattended run. They are properties of a sensor and a room; there is no ground truth for them on a bench over a weekend. Conflating them is a register risk. | R-2 |
| S-6 | Latency must be **attributed**: core-attributable (report received → decision → command → confirmation) reported separately from the device's reporting interval. `[CODE-RECALL]` the reporting config on the metering cluster is min 5 s / max 3600 s / change 10, which would dominate any end-to-end figure. Publishing end-to-end p95 publishes someone else's firmware. | Measurement design |
| S-7 | The causal structure is a **DAG, not a chain**: one observation fans out to several automations; a command's state change is itself an observation. Carry **causation id** (direct cause) and **correlation id** (root) separately. Cheap now in an append-only store; miserable to retrofit once verifier, manifests and packets assume a linear trace. | E-1 |
| S-8 | **You cannot explain a non-event without a declared expectation.** If the system records evaluations that happened, "why didn't it fire" for an absent input can only be bounded, not determinate, unless input freshness/cadence is declared. This is the deepest design consequence of the exchange and it generalizes: the answerable why-not set is bounded by the declared-expectation set. | E-4, and the gate collision in §6.3 |
| S-9 | The evidence-bundle rule (X-14) binds **both** arms. The reader sees the rendered record, not a query against the event store. This is the most tempting and most invisible cheat in the design. | §6 |
| S-10 | The baseline arm should be **validated by a partisan** of the baseline before incidents run — one HA power user who will not be reading packets — to pre-empt "you built a weak baseline." | §6 |
| S-11 | Do **not** contort the implementation so the baseline's trace looks good (the reviewer suggested making suppression deliberately trace-visible). Match the **scenario**, not the mechanism. A benchmark that reshapes the product is designing the product. | §6 |
| S-12 | **Retention decay should be a measured variable, not a protocol assumption.** Capture packet 5 at 1 h and 24 h. This is the empirical test of the register's "self-purging store" clause and is more publishable than the headline comparison. | R-4 |
| S-13 | Run the **baseline arm first, alone, on sequential hardware**. Packets are static artifacts, so the arms need not be simultaneous — one fleet, one coordinator. This makes the cheapest possible kill test available without the vocabulary work, the product's study build, or January. | §6.6 |
| S-14 | **The pilot can kill; it cannot confirm.** Self-selected volunteers and an observing founder push toward readers succeeding (the kill direction), so a pilot where they succeed is strong evidence against the wedge. Incident selection is the lever Nick controls and pushes the other way, so a pilot where they struggle may only mean he chose well. Asymmetric; must be written down before the calls. | §6.6, §10 |
| S-15 | **Every invariant proposed stops the product lying; none stop it being useless.** A record answering `coverage: unavailable` four times in ten passes every honesty gate and is never opened twice. | §6.3 |
| S-16 | The answer key must be **system-neutral**. The reviewer's accepted answer for 4B was written in our vocabulary ("declared cadence window"), which a HA reader cannot produce; he simultaneously rejected "no trace means the automation did not run," which is a correct causal statement in the baseline's ontology when paired with a stale-input observation. A biased key is the failure mode the key exists to prevent. | §6.5 |
| S-17 | **Arm-blinding the grader is infeasible** (one arm is a decision record with coverage and confirmation verdicts; the other is YAML + a trace tree or its absence + a history table). Restructure to **two-stage grading**: blind on response sheets; unblinded only for the confident-wrong adjudication subset. | §6.5 |
| S-18 | **Ties bound the analysis.** Under sign-flip permutation each tied reader halves the permutation space: 10 readers, no ties → floor ≈0.002; 3 ties → ≈0.016; 5 ties → ≈0.06. Mitigate by buying **instances, not classes** (a second silent-non-fire instance costs far less than a second reader). | §6.4 |
| S-19 | The **economic divergence branch**: accuracy and dispatch can move apart. If readers are less accurate but equally unlikely to dispatch, the wedge is technician *time*, not truck rolls — roughly a 50:1 cost asymmetry (a dispatch is a couple hundred dollars; four minutes of remote diagnosis is a few dollars). Different buyer, different price. Pre-commit while hypothetical. | §10, D-EXT-1 |
| S-20 | With a forced cap, capped readers report low confidence, so the slower arm structurally shows less false confidence. Report false confidence among **completed** responses separately. | §6.3 |
| S-21 | The 2:30 target for packet 8 is below the **task floor** (a reader needs ~60–90 s just to read the packet). Calibrate by having one reader run each packet **with the answer key**, told only to find and cite the decisive line. | §6.4 |
| S-22 | Define the full vocabulary now, **implement only the values the corpus exercises**; the API omits the rest. Otherwise surface ships under a frozen contract with no test behind it. | E-12, R-7 |

---

## §5 Commitments already transmitted — `C-nn`

These are in the hands of a third party. They are soft (a friend, no contract) but they exist and they create schedule expectations.

| ID | Commitment | Round |
|---|---|---|
| C-1 | The HA-parity framing retracted; the compliance sentence retired and replaced with the reviewer's wording. | 1 |
| C-2 | The wedge is the integrator observability layer, not multi-site enterprise; design partners, not a dealer program. | 1 |
| C-3 | The claim will not be "our automation is more reliable"; it is the fired / did-not-fire / fired-without-confirmation formulation (§6.0), and it **may not be asserted until the comparison runs**. | 2 |
| C-4 | Corpus split by audience (machine-checked vs reader-scored); restart and duplicate cases become verifier cases; late-confirmation, transport failure and duplicate injection deferred with reasons published. | 3 |
| C-5 | The mismatched-value case added to the corpus. | 3 |
| C-6 | Reader protocol: counterbalanced order, 10-minute cap with a forced dispatch decision, "which line told you" recorded, record/presentation/reader triage. | 4 |
| C-7 | Diagnostic latency declared (24 h) with HA left at defaults and settings disclosed; packet 5 captured at 1 h and 24 h as a decay condition. | 5 |
| C-8 | Input freshness/cadence becomes part of the automation definition, so absence is a checkable predicate. | 5 |
| C-9 | Pairing, pooled primary endpoint, within-reader permutation test; per-packet accuracy published as a full matrix, not gated. | 6 |
| C-10 | Baseline arm runs **first and alone**, sequential hardware. | 6 |
| C-11 | The pre-registered statistical procedure (statistic, sign-flip scheme, zero handling, two-sidedness, exhaustive enumeration) — not an anticipated p-value. | 7 |
| C-12 | A crude three-reader pilot precedes the full apparatus; the asymmetry (S-14) is written on the one-page pre-registration. | 7 |
| C-13 | "The next thing I send you is data, not another draft." | 7 |
| C-14 | Reviewer **declined attribution**; he is not to be named in any outward artifact. | 7 |

---

## §6 The protocol as it now stands — the reusable artifact

This is the part worth keeping regardless of what the hub decides about the wedge.

### §6.0 The falsifiable claim (reviewer's wording, round 2) `[EXT]`

> "For a defined automation incident, our system can determine whether the automation fired, did not fire, or fired without producing a confirmed device-state change—and can identify the causal reason fast enough to reduce diagnostic labor compared with the incumbent evidence trail."

**Register note:** the trailing clause ("reduce diagnostic labor compared with the incumbent evidence trail") is **not** register-supported and cannot leave the building until data exists. See R-3.

### §6.1 Corpus and parity labels `[EXT]` (verbatim labels)

| Packet | Baseline prediction | Competitive status |
|---|---|---|
| 1. Normal control | Parity — determinate | Comprehension control |
| 2. Predicate false | Parity — determinate | None |
| 3. Suppression / cooldown | Parity — determinate, if inside the run | Fairness control (see S-11) |
| 4. **Silent non-fire / absent qualifying evaluation (4B)** | **Incumbent blind spot** | **Primary** |
| 5. **Command issued; no confirmation by deadline** | **Partial evidence, no terminal answer** | **Primary** |
| 6. Known observability hole | Universal limit / calibration | Honesty test, not a win |
| 7. External state change | Partial evidence | Possible |
| 8. Mismatched value after command | Partial evidence, no semantic verdict | Secondary |

4A (freshness predicate evaluated *inside* a run) is parity and is **not** used; 4B (no qualifying evaluation occurs at all) is the case. Deferred with published reasons: plugin failure (no plugin system), watt-based independent confirmation (classification + cluster consumption absent), long-term mesh degradation, vendor API change, presence false-clear/false-hold, multi-controller conflict.

### §6.2 Pre-registered baseline priors `[EXT]` (verbatim — do not paraphrase)

| Packet | Correct cause | Median time to forced decision | Unnecessary dispatch |
|---|---:|---:|---:|
| 4 | 55 % | 6:45 | 20 % |
| 5 | 45 % | 7:30 | 25 % |
| 8 | 60 % | 5:30 | 12 % |

Minimum meaningful difference: correct-cause **+25 pp**; median time **≥3 min faster**; unnecessary dispatch **≥10 pp lower**. Per-packet targets: 4 → ≥80 % / ≤3:45 / ≤10 %; 5 → ≥70 % / ≤4:30 / ≤15 %; 8 → ≥85 % / ≤2:30 / ≤5 %.

Scoring conventions: "correct cause" = the actual causal class, not a plausible symptom; "insufficient evidence" is epistemically correct but does **not** count as correct cause; a capped reader scores 10:00; priors are for competent HA power users, not average users and not professional integrators.

**Session amendments** `[SESSION]`: the nine conjunctive thresholds are a false-negative machine at feasible n (S-18, §6.4); the 2:30 target is below the task floor (S-21); report resolved-within-cap rather than a censored median.

### §6.3 The usefulness gate `[EXT]` (verbatim, final form)

> **Usefulness Gate:** Every case designated as intended-observable must yield a determinate answer. At most one result may be bounded unknown, and it must be the pre-designated observability-hole case. No result may be an unbounded unknown. No reader may reach a confident but incorrect conclusion that is supported, implied, or materially encouraged by the rendered record.

Result taxonomy: **determinate** / **bounded unknown** (names what cannot be known, which interface or evidence is missing, and the next check) / **unbounded unknown**. "Actionable" = the reader can select one of: no dispatch · remote check/remediation first · wait/retry under a named rule · dispatch · escalate due to a bounded evidence gap.

Confidence 1–5; `false_confidence = (incorrect cause OR incorrect disposition) AND confidence ≥ 4`, split into **reader** false confidence and **record-induced** false confidence (the rendered evidence implies the wrong conclusion, hides a material qualification, overstates what is established, or presents a derived conclusion as observed).

**Known collision** `[SESSION]`: packet 4B may only be answerable as a *bounded* unknown unless E-4 lands, and the gate permits exactly one bounded unknown, already spent on packet 6. Either 4B fails on a technicality or freshness/cadence declaration becomes part of the automation definition. This is D-EXT-3.

**Amendments** `[SESSION]`: the gate is otherwise **single-arm** and must be paired with the comparative measures; every non-determinate result is triaged (evidence absent / present but missed / present but rendered misleadingly / reader guessed against clear evidence) and only the third counts against the hard zero; false confidence is reported among completed responses separately (S-20).

### §6.4 Statistics `[EXT]` + `[SESSION]`

- **Unit**: the reader. Reader-by-packet observations are clustered and are not independent (X-15).
- **Primary endpoint**: correct operational disposition, paired, pooled across the competitive packets, with error direction (unnecessary vs missed dispatch) retained.
- **Test**: within-reader sign-flip permutation on the mean signed difference in disposition errors; zero differences excluded from the flip space; two-sided; **exhaustively enumerated**, not sampled (2^n is trivial at this size).
- **Pre-register the procedure, never an anticipated p-value** (X-19).
- **Ties bound the floor** (S-18). Mitigation: more **instances per class**, not more classes; an incomplete counterbalanced design keeps per-reader load sane; most parity packets can be dropped from reader time since both parties predicted their outcome.
- **Power reality** `[SESSION]`: detecting 0.55 vs 0.80 at conventional power needs ~50 observations per arm per cell. Per-packet proportions are descriptive, not inferential, at any feasible n.
- Packet 5's 1 h / 24 h pair is a **decay condition**, reported separately, not double-weighted (X-16).

### §6.5 Grading `[EXT]` + `[SESSION]`

Frozen **scoring charter** before any reader sees a packet, containing per packet instance: packet id, incident class, ground-truth causal class, **accepted correct-cause answers** (and abbreviated accepted forms, and disallowed-but-plausible answers), required evidence elements, allowed bounded-unknown answer if any, correct operational disposition, acceptable alternatives, expected confidence caveat. Hash-commit for pre-registration (explicitly *not* a tamper-proofing claim).

**Session amendments**: the accepted-answer set must be **system-neutral** (S-16) — e.g. "the automation never ran because sensor X stopped reporting after T", which both arms can express and only one can produce without inference. Arm-blinding is infeasible; use **two-stage grading** (S-17). A second grader who does not know the architecture is required for credibility, and **his anonymity reduces the external-validation value** (R-9).

### §6.6 The pilot — the cheap screen `[SESSION]`, endorsed `[EXT]`

Three competent HA power users. No blinding, no charter, no second grader. Nick present. The two strongest cases (4B and 5) in an HA instance. One page pre-registered beforehand: the incident, what counts as solving it, the ten-minute cap, the kill rule, and the asymmetry.

**Standalone kill rule** (session restatement of the reviewer's, made single-arm so it is evaluable before our arm exists):

> If competent Home Assistant users reach ~80 % correct-cause classification with a median forced-decision time of about four minutes and few disposition errors, then the maximum available improvement is ~20 pp plus whatever time sits above the task floor, and that ceiling is too low to carry a cost-reduction claim for that incident class.

**Asymmetry (S-14):** the pilot can kill the wedge; it cannot confirm it.

**Recruitment note** `[SESSION]`: r/homeassistant, the community forum, the HA Discord dev channels. Say plainly that something is being built in this space and that the question is how well the existing evidence works. **The premise gate binds the recruitment post** — no product claims in it, or the readers are primed before they are measured.

### §6.7 The buyer test (pre-code) `[EXT]` + `[SESSION]` edits

Ten integrator conversations, calendar-bound rather than hours-bound, run **before** more product work. Reviewer's decision rule: if ambiguous diagnostics are consistently billable, acceptable and profitable for the integrator, the buyer is probably not the integrator (it may be the property owner, end customer, equipment vendor, or an integrator under fixed-price service obligations) — **a valuable result even if it ends the wedge**.

Session edits: lead with the concrete-recall question ("tell me about the last incident where you could not tell why an automation did or did not act"); replace the solution question ("would you install a read-only diagnostic sidecar") with a behavioural one; add "what do you do today when you can't tell" (the workaround is the competitor) and "whose warranty does a sidecar put at risk". Note: the CEDIA Expo window (Sept 1–4, Denver) has passed `[VER-0917]`, so this is outreach and waiting, not a two-day sweep.

---

## §7 Engineering implications — `E-nn`

All code statements are `[CODE-RECALL]` at `3d40b5f` and **stale** (see §1.1). Each row is a candidate, not an instruction.

| ID | Concept | What exists (recall) | What it would take | Prereq for the run? |
|---|---|---|---|---|
| E-1 | **causation id + correlation id** (DAG, not chain) | Append-only store; ordered views (HASH-1) | Event-level id pair; cheap now, expensive after the verifier/manifests assume linearity | No |
| E-2 | **Is a decision record emitted on non-fire, or reconstructed by replay?** | Unknown to this session. 114c added condition-definition + by-id read, which hints at query-time reconstruction | A grep, then a design ruling. **Gates the verifier's meaning**: if reconstructed, the verifier checks the reconstructor, and a bug there is a confident wrong answer | **Yes — answer first** |
| E-3 | **`verdict_provenance`** — session's 4-way: recorded at decision time / derived by the same evaluator over durable inputs / derived over inferred inputs / unavailable | v1.1 FROZEN, additive 114a–c, stamp v1.1.5 | Additive API field **and** it must reach the rendered hero sentence, or the UI manufactures confidence (the keyless-sentence lint exists to prevent exactly this) | No (Nov–Dec) |
| E-4 | **Declared input freshness / cadence in the automation definition** | Not known to exist | Config/language change + predicate evaluation + a why-not verdict. Turns absence into a checkable predicate; makes 4B determinate | No, but D-EXT-3 |
| E-5 | **`confirmation_verdict`** = matched / adjusted_within_declared_tolerance / mismatched / rejected / timed_out / superseded / unavailable, **plus `confirmation_status`** = pending / terminal; with desired_state, observed_state, comparison_rule, comparison_tolerance | C-002's confirmation leg | Additive API + UI. `in_progress` is a status, not a terminal verdict; `superseded` preserves both commands so A does not become a phantom timeout | No (Nov–Dec) |
| E-6 | **`coverage`** = complete / partial / unavailable, with a **stable capability identifier** | HERO-0 null census at v1.1.3 (may have narrowed with 114a–c) | The identifier space should be shared with the ZIGBEE-GAPS coverage map and, later, a published compatibility matrix. Tolerance (E-5) should also derive from the same capability descriptors | No |
| E-7 | **Determinism / replay invariant in CI**: replay the log, assert derived verdicts equal recorded verdicts wherever both exist | DUR-1 (run on expiry) + HASH-1 (ordered views) accepted red→green after MEASURE-1's red probes (IR-22/IR-23) | Converts the observed-vs-reconstructed caveat from a disclosure into a test result | Strongly recommended |
| E-8 | **Verifier script for record properties** (partition, terminality, no unflagged unconfirmed command, no unpartitionable interval) | — | The Oct-30-era gate; must be mechanical, or Nick grades his own homework | **Yes** |
| E-9 | **Watt-corroborated confirmation** | `ClusterHandlers` 8 handlers (OnOff, Level, Color, Occupancy 0x0406, PowerConfiguration, Temperature 0x0402, Humidity 0x0405, IasZone 0x0500) — **none** for 0x0B04 / 0x0702 / 0x0400. `ReportingConfigurator` knows 0x0B04 and 0x0702. `EndpointClassifier` :41 0x0051→SMART_PLUG. Owned Gen4 identifies as **0x010A** (F-b6-2 gap). ENERGY-READ fence stands | Classification + cluster consumption + divisor semantics + ENERGY-READ green | **Yes, if the run's "corroborated by watts" design is to hold** — see O-9 |
| E-10 | **Receipt order vs occurrence order** as distinct facts | BUS-ORDER-1 (read-forward live delivery), notify-order/census-truth work | A record whose story depends on arrival order should show both | No |
| E-11 | **Late-confirmation correction record** (append, never mutate; "unconfirmed at decision time, evidence arrived later") | — | New response shape under a frozen contract → additive or deferred. **Deferred** in the corpus | No |
| E-12 | **Implement only exercised enum values**; define the rest in the design doc; API omits unimplemented values | — | Policy, not code | — |

---

## §8 Repo / register / plan impact — `R-nn` (hub must rule)

| ID | Issue | Recommendation |
|---|---|---|
| R-1 | **The 72-hour run's purpose changes.** With a corpus doing the falsification, the unattended run proves stability over duration (no drift, no unbounded growth, nothing that appears only at hour 40), not the claim. Two artifacts, named separately, or three weeks of prep produce a result nobody agreed how to read. | Rule D-EXT-2 |
| R-2 | **Presence-quality metrics must not attach to the run.** They are dataset-program properties. Any card or outward line conflating them is a register exposure. | KEEP as a fence |
| R-3 | **New claim candidates are embargoed.** "Reduces diagnostic labor compared with the incumbent evidence trail" is not register-supported. It may not leave the building until the study runs. FENCE-BUS's "every"-class discipline applies to every sentence in §6.0. | KEEP |
| R-4 | **The register's HA line is now scheduled to be tested.** RS-3 §6.1-1 (2026-08-28, refutable from 09-02) asserts HA answers why-did-it-fire, records no reason for a legitimate non-fire, no confirmation verdict, and rides a self-purging store. S-12 makes the self-purging clause an empirical measurement. Hub should decide in advance whether a result refines, supersedes or re-dates that row. | HUB-RULE |
| R-5 | **Premise-gate extension.** The gate binds code and outward text. This exchange began because a *verbal* pitch carried an unsupported compliance claim and an HA-parity framing the register does not grant. Recommend a pm-lessons row: the gate binds spoken and informal pitches, and a recruitment post is outward text. | Recommend KEEP |
| R-6 | **Vocabulary governance.** `confirmed`, `inhibited`, `bounded unknown`, `unavailable`, `determinate` will harden simultaneously in API, UI, manifests and reader packets, and then in outward text. Register-check the words before they harden. | Recommend KEEP |
| R-7 | **Read-API freeze pressure.** E-3, E-5, E-6 are additive v1.1.x. At least one deferred corpus case (late confirmation) is a new response shape. If a large share of the corpus needs new fields, the freeze — not the benchmark — is the binding constraint. | Rule D-EXT-4 |
| R-8 | **Schedule.** The full apparatus is ~40–60 h of study administration at ~7 h/week. The pilot (§6.6) is the proposed resolution; the buyer calls are calendar-bound and can start without consuming build hours. **All of this assumes the v75 calendar; v76 b2 re-cut it.** | Rule D-EXT-7 |
| R-9 | **Third-party dependency.** An external reviewer now holds pre-registered priors and has offered blind grading, and has **declined attribution**. An anonymous grader is worth materially less to a design partner than a named one; the "independent validation" value of the arrangement is reduced accordingly. No external party may be named in outward text (C-14). | Note in the DR |
| R-10 | **FOP-1 corrections remain live.** The 2026-09-17 return found 13 FALSE rows in the founder operating plan. The time-critical one is **HotMobile 2027, due Fri 2026-10-09 AoE** (the FOP schedules it Jan–Mar 2027) — 21 days from today. | Rule D-EXT-6 |

---

## §9 Open questions — `O-nn`

| ID | Question | How answered |
|---|---|---|
| O-1 | Does the system emit a decision record on non-fire, or reconstruct by replay? (E-2) | Grep at HEAD |
| O-2 | What gating-reason verdict vocabulary does v1.1.5 emit today? Map the corpus's injected conditions onto existing arms; sort into (a) already emitted, (b) additive verdict needed, (c) out of scope | Grep + design doc; ~1 afternoon |
| O-3 | Is the HERO-0 null census (v1.1.3) still accurate after 114a/b/c? | Diff |
| O-4 | Can the bench harness (P-1 power harness primitive, nexsys-bench) produce the scripted incidents, or is new harness work required? | Read the bench repo |
| O-5 | HA baseline facts: stored-traces default, recorder retention default, trace persistence across restart, context attribution semantics (X-6, X-7, X-8) | HA docs, before pre-registering |
| O-6 | Reader recruitment: channel, count, and whether a volunteer panel of the size the statistics need is reachable at all | Outreach |
| O-7 | Who is the second grader (must not know the architecture)? | Recruiting |
| O-8 | Does C-002's confirmation-leg language cover the mismatched-value case, or is a new row/qualifier required? | Register read |
| O-9 | If ENERGY-READ does not land before the run, does the run's "every confirmation corroborated by a plug's own watts" design degrade gracefully, or does the run's stated shape change? | Hub + plan |
| O-10 | Does the current (v76) calendar admit any of this, and at which beat? | Hub |

---

## §10 Risks

1. **Scope creep by methodology.** Seven rounds produced a rigorous study and zero product code. The apparatus is now larger than the decision it informs. The pilot exists to stop this; if the pilot itself acquires a charter, a manifest and a grader, the mechanism has failed.
2. **Author bias.** Nick authors the incidents, the record, the rendering and (absent a second grader) the scoring. Every control in §6.5 exists against this and none of them fully removes it.
3. **Pilot misread.** S-14's asymmetry is the specific trap: a difficult pilot is weak evidence *for* the wedge and will feel like validation.
4. **Economic divergence.** If accuracy moves and dispatch does not, the wedge shrinks from truck rolls (~$150–300 each) to technician minutes (~$5), a ~50:1 reduction in the claim's value, with a different buyer.
5. **Vocabulary hardening before test.** Shipping the full enum under a frozen contract with no test behind it (mitigated by E-12/S-22).
6. **Calendar collision.** Under the v75 plan: Oct 30 was simultaneously the run start, the Activate close (12:00 PT) and the Innovation Crossroads close (20:00 ET) `[VER-0917]`. v76 b2 has re-cut the calendar; the collision must be re-checked, not assumed.
7. **External expectation.** C-13 promises data, not another draft. Silence is fine; another protocol round is not.

---

## §11 What this session would keep, and what it would drop

**Keep (high confidence):** S-4 (gate the record, measure the world) · S-8 / E-4 (no explanation of a non-event without a declared expectation) · E-7 (determinism invariant) · E-2 (settle recorded vs reconstructed) · E-6 (one identifier space for coverage, gaps and tolerance) · X-11 (a clean run may be uninformative) · X-17 (symmetric disposition endpoint) · S-13 + §6.6 (baseline-first, pilot-first) · S-14 (the asymmetry) · S-16 (system-neutral answer key) · R-5 (premise gate binds spoken pitches).

**Keep (as pre-registration artifacts, verbatim):** §6.1, §6.2, §6.3, and the kill rule in §6.6.

**Drop or hold:** X-4 (the enterprise wedge) · the nine conjunctive thresholds as gates · the full January apparatus until the pilot returns · the presence-metric framing for the run · any use of §6.0's comparative clause before data exists.

**Verify before use:** X-6, X-7, X-8, X-9's suggestion-explanation clause, and every `[CODE-RECALL]` row.

---

## §12 Not in this packet

- The seven letters and seven replies **verbatim**. They exist only in the Cowork transcript. This packet is the distillation; the pre-registration artifacts (§6.1–§6.3, §6.6) are reproduced verbatim because they are commitments and must not be paraphrased. If the hub wants the full text it must be exported from the transcript before the session ages out.
- Any grep, HEAD read, register read or byte-level check. None was performed.
- Any write into `nexsys-hivemind/context/`. The hub is the sole spine-writer; this packet is staged in `_scratch/v76/` deliberately.
- Any product-name candidate, per standing practice.

STAGED _scratch/v76/2026-09-18_EXT-REVIEW-1_diagnostic-wedge-reader-study_intake-packet.md 45110 B — unadjudicated; no charter; not audited at the bytes.
