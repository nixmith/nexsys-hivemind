<!--
file: context/audits/2026-06-26_Doc17_independent_DOCS_Review_Return.md
purpose: INDEPENDENT, context-isolated, scope-independent DOCS-Project second-opinion review of homesynapse-core-docs/design/17-aiot-and-cloud-readiness.md (DRAFT) before Lock. Its distinct value is INDEPENDENCE ON SCOPE: it rules the §0 new-Doc-17-vs-Doc-16-extension call on the beat's own merits, assesses the [AIOT-INV-1..3] candidates against the citing-composition test, and source-verifies every cited invariant id. Produces a scope verdict + an invariant-candidate verdict + the id source-verification result + a document verdict + a consolidated edit list. Review ONLY -- edits are NOT folded here (review-separate-from-fold; Nick rules scope -> folds -> mints any [AIOT-INV-*] -> co-signs -> Locks).
audience: Nick (rule scope / ratify / fold / Lock), the Doc 17 fold session
state-type: review return (independent design-doc review)
status: COMPLETE 2026-06-26 -- SCOPE VERDICT: NEW DOC is the right cut (independently affirmed on the center-of-gravity criterion), CONDITIONAL on the owns/restates boundary edit S1. INVARIANT CANDIDATES: AIOT-INV-1 MINT-AT-LOCK; AIOT-INV-2 KEEP-AS-PRINCIPLE; AIOT-INV-3 KEEP-AS-PRINCIPLE (or mint only de-duplicated). ID SOURCE-VERIFICATION: all 11 cited ids RESOLVE and say what the beat claims (no fabricated/mis-cited id). DOCUMENT VERDICT: RATIFY-WITH-EDITS (S1/S2 + E1-E5, all NON-BLOCKING; no BLOCKING/REVISE).
reviewed: docs Doc 17 DRAFT on disk at design/17-aiot-and-cloud-readiness.md (host-authoritative file tools). Baseline confirmed at preflight: docs HEAD e47f01e (Doc 16 LOCKED; watermark AMD-94; invariants 169/49) + the Doc 17 DRAFT present / core 5363347 (M7.3 delivered). Preflight PASS.
independence: run as a fresh, context-isolated conversation. The v6 hub's §1 deliberation was NOT read; the prior-art study was NOT read. The companion decision record (D1-D5) WAS read for the ratified-context the beat references, but its framing was treated as a position to pressure-test, not as binding on the scope verdict (see the independence note, §G). Own view formed first, THEN reconciled against the beat's stated lean and the decision record.
-->

# Doc 17 (AIoT + Cloud Readiness) -- INDEPENDENT DOCS-Project Review Return

This is the project's standard pre-Lock independent second opinion (the discipline Doc 15 and Doc 16 passed before Locking), run as a **fresh, context-isolated, scope-independent** session. The beat is a DRAFT reserved-architecture artifact: it builds nothing, mints no invariant at this stage, and carries `[AIOT-INV-1..3]` as PROPOSED candidates. My charge, in order: **rule the §0 scoping call on the beat's own merits**, assess the three invariant candidates, source-verify every cited invariant id, and run the full design-doc review. I formed my own view first and only then reconciled it against the beat's stated lean.

**Bottom line.** SCOPE: **the new-doc cut is RIGHT** -- but for a more precise reason than the beat gives, and conditional on one load-bearing edit (S1). CANDIDATES: mint **one** of the three (AIOT-INV-1); keep the other two as design principles. IDS: **every cited id resolves and is accurately quoted** -- no fabricated or mis-cited id. DOCUMENT: **RATIFY-WITH-EDITS** (all NON-BLOCKING). No BLOCKING question gates V1; the DRAFT posture (watermark stays AMD-94, not self-ratified, no invariant minted at DRAFT) is correct.

---

## A. SCOPE VERDICT (the headline) -- a NEW DOC (Doc 17) is the right cut, **conditional on S1**

**Independently affirmed: "AIoT + Cloud Readiness" rightly earns its own design doc rather than a Doc-16 §3.7/§3.8 extension -- but the doc as drafted does not yet *earn* that status cleanly, because it blurs what it OWNS against what it merely RESTATES. The decisive edit is a scope-boundary section (S1).** My reasoning is independent of the beat's, and my decisive criterion differs from the beat's lead argument.

### A.1 The discriminating criterion (this is why the cut holds)
A subject earns its own design doc iff **(a) its center of gravity lies outside any single existing doc's owned scope, (b) it is a coherent first-class concern a reader would expect to find as a named, discoverable artifact, and (c) housing it in an existing doc would either bloat that doc past its charter or hide the concern.** This is the cross-cutting-vs-contained test -- the same family as the M4-retrospective P1 "epic-under-one-label" smell test, but run in both directions (under-splitting hides scope; over-splitting fragments it).

Judged against it:
- **Center of gravity is genuinely distributed, and it is NOT Doc 16.** The four load-bearing subjects sit *outside* the automation layer Doc 16 owns: the **immutable-log-as-universal-substrate** thesis is an event-model / persistence concern (Doc 01 / Doc 04); the **cloud-replication-outward** seam is a persistence / distribution concern; the **SBOM / signed-update** seam is a security / lifecycle concern (Doc 12 / INV-PD-08); and the **AI-safety frame** cuts *across* authoring (Doc 16 §3.2), reasoning (Doc 16 §3.3), device-intelligence (Doc 02 / Doc 05), and dispatch (Doc 07). Folding these into Doc 16 would be the categorical-mismatch *inverse* of a clean cut -- hosting non-automation content in the automation-layer doc -- and would require reopening a **Locked** doc to do it. -> favors a new doc.
- **AIoT is now a first-class strategic direction** (Nick, 2026-06-25), so a discoverable named artifact is warranted over a buried decision line. -> favors a new doc. *(But see A.3: this argument alone is insufficient.)*
- **Doc 16 already anticipates and defers the adjacent docs.** Doc 16 §2.2 ("Does Not Own") explicitly assigns full federation to "its own post-M8 design doc, which mints its own invariants" and the full honest-hybrid feature to "its own tight design doc," reserving only the §3.5 seam and the §3.6 cut-line. A coordinating readiness doc that *names* the AIoT+cloud direction is therefore **structurally consistent with Doc 16's own design**, not a violation of it. -> favors a new doc.

### A.2 Why this is NOT over-structure (a doc that reserves seams but builds nothing)
A reserve-only doc is a legitimate scope (the prompt's own framing; cf. Doc 16 §3.5/§3.6, which reserve without building). The test for over-structure is: **strip out everything already owned elsewhere -- does enough genuinely-new, genuinely-cross-cutting material remain to justify a doc rather than a Doc-14 note?** It does: the **AI-safety frame** (cross-cutting, candidate-invariant-bearing), the **cloud-replication seam**, the **SBOM/update seam**, the **substrate thesis as a named cross-cutting principle**, and the **AIoT direction as four coherent named seams**. That is doc-weight, not note-weight. So the new-doc cut clears the bar from below as well as above.

### A.3 Where I diverge from the beat's reasoning (the independent contribution)
The beat leads with **"a first-class strategic direction earns a named architectural artifact."** That is true but, by itself, **insufficient** -- it would equally justify a single Doc-14 master-architecture note. What actually makes this a full *new doc* is the **center-of-gravity / categorical-fit** argument in A.1 plus the **doc-weight reserved content** in A.2. The headline reason should be "the subject's center of gravity lies outside Doc 16's charter and carries its own candidate invariants," not "AIoT is important." I reached the same outcome as the hub's lean by a different and, I think, more defensible route -- which is the value of an independent pass.

### A.4 The real counter-pressure the beat under-addresses -- the **fragmentation hazard** (this drives S1/S2)
The strongest argument *against* a new doc is not "fold it into Doc 16"; it is **double/triple-reservation drift.** As drafted, Doc 17 re-states seams that are already owned elsewhere, without a boundary that says so:
- The **federation seam** is owned by Doc 16 §3.5 + **INV-SA-02** (Locked). Doc 17 §4 re-tabulates it.
- The **local/cloud cut-line** is owned by Doc 16 §3.6. Doc 17 §3.4 restates it.
- The **enterprise audit projection** is owned by Doc 16 §3.3 (default-off). Doc 17 §4 re-lists it.
- **Crypto-shred** is owned by Doc 15 / **INV-PD-07** (MVP-narrowed by AMD-86). Doc 17 §4 re-lists it.
- And Nick has already ruled (PROJECT_SNAPSHOT, the B-1/B-2/B-3 rulings) that **B3-federation and honest-hybrid each get their own sequenced docs** -- so these seams now risk being described in a **third** place: Doc 16 (the seam) -> Doc 17 (the "readiness") -> the future B3/honest-hybrid docs (the full feature).

This is exactly the "over-splitting fragments it" failure. The companion decision record concedes the point in passing -- it lists federation, the audit projection, AX-7, and crypto-shred as **"already reserved in Locked Doc 16; reaffirmed here as non-precluding"** -- but the beat does not carry that owns-vs-reaffirms distinction onto its own face. **The new-doc verdict is therefore CONDITIONAL on S1:** Doc 17 must add a scope-boundary section that crisply separates (i) what it **OWNS** (net-new: the AI-safety frame, the cloud-replication seam, the SBOM/update seam, the substrate-as-named-principle, the AIoT direction), (ii) what it **RESTATES/REAFFIRMS** (federation, cut-line, audit, crypto-shred -- owned by Doc 16/Doc 15), and (iii) what it **COORDINATES-WITH-but-does-not-pre-empt** (the planned B3-federation + honest-hybrid docs). With S1, the new-doc status is clean; without it, the doc *is* the fragmentation risk it should be foreclosing.

### A.5 Scope bottom line
**New doc, not a Doc-16 extension -- RIGHT.** It avoids both failure directions: under-splitting (burying a cross-cutting, now-first-class direction inside the automation doc) and -- once S1 lands -- over-splitting (re-reserving owned seams in a way that drifts). The verdict requires no structural rewrite, only the S1 boundary section and the S2 coordinate-not-pre-empt clause.

---

## B. INVARIANT-CANDIDATE VERDICT (§6) -- mint **one** of three; keep two as principles

The test (the project's own, from the INV-SA-03/04 minting at the Doc 16 Lock, and INV-GA-02): a candidate is minted first-class only if it **adds a constraint its cited parents do not already impose** and it **cites those parents** -- it must not be a droppable near-duplicate. Applying it per candidate:

| Candidate | Cited parents | Adds a constraint the parents do not impose? | Verdict |
|---|---|---|---|
| **AIOT-INV-1** -- AI is never an autonomous actuator | INV-SA-04 / AMD-90-INV-01 + decision-record D2 | **Yes.** The parents bind the *engine* (no autonomous re-issue/retry; no side-effects on replay). None binds a **new actor class (AI)** to proposer-only. AIOT-INV-1 adds "no AI code path actuates a device or mutates state outside the engine; every AI-originated effect enters as a proposed definition/command." That is a genuinely new constraint -- the same *kind* of "formalize an anti-requirement as an invariant" move that made INV-SA-01 novel. | **MINT-AT-LOCK** (with the parentage fix in E2). This is the "safest AIoT" moat in invariant form -- worth first-class status; and minting a non-preclusion invariant for an unbuilt seam is exactly the INV-SA-02 precedent. |
| **AIOT-INV-2** -- Cloud is non-authoritative and non-required | INV-LF-01/02 + INV-SA-02 + Doc 16 §3.6 | **No (near-duplicate).** INV-LF-02 already states cloud "may never be required for any core function... no core code path may include a network call to an external service that, if it fails, degrades core functionality," and INV-LF-01 already gives "core works without internet." INV-SA-02 already gives "scope additive, no log migration." The testable content of AIOT-INV-2 (WAN-down -> everything still runs; keys never leave the machine) is **fully covered** by the parents. | **KEEP-AS-PRINCIPLE.** Record it as a design principle; do not mint. The non-preclusion rests entirely on INV-LF-01/02 + INV-SA-02. Minting it creates the droppable-near-duplicate the test (and INV-GA-02's identifier-permanence discipline) warns against. |
| **AIOT-INV-3** -- Every AI decision is explainable and auditable (no parallel AI trace store) | INV-SA-03 + INV-ES-06 | **Marginal, and mis-parented.** INV-SA-03 ("Explanation Is a Pure Projection of the Log... no parallel trace store exists") already carries the whole "no parallel trace store" guarantee, and INV-SA-03 is *itself* a citing composition of INV-ES-06 (+ INV-ES-01 + INV-TO-03) -- so citing **both** INV-SA-03 and INV-ES-06 is **redundant** (the parent already subsumes the grandparent). The only arguably-new content is binding a *future AI reasoner/author* to read the projection rather than build its own trace DB -- but INV-SA-03's "no parallel trace store" is general enough to reach that already. | **KEEP-AS-PRINCIPLE** (or mint only de-duplicated). If Nick prefers to mint, it must drop the redundant INV-ES-06 citation, cite INV-SA-03 alone, and state the precise AI-specific strengthening ("no AI subsystem maintains a parallel trace/decision store; all AI-decision provenance is a projection of the log"). Absent a constraint beyond INV-SA-03, keep as principle. |

**Summary:** AIOT-INV-1 = mint (the genuinely-novel AI-actor-routing constraint); AIOT-INV-2 = keep-as-principle (covered by INV-LF-02 + INV-SA-02); AIOT-INV-3 = keep-as-principle, or mint only with de-duplicated parentage. This mirrors the Doc 16 precedent shape (there, 2 of 4 were novel-mints and 2 were citing-compositions); here at most 1 of 3 is a clean mint. The beat itself already offers keep-as-principle as the fallback (§6 closing, §7-Q2), so this verdict sits inside the options it surfaced.

**Minting mechanics, if AIOT-INV-1 is minted at Lock.** Per the §49 / new-design-doc-Lock precedent and INV-GA-02 (identifiers permanent, assigned at ratification): it would open a **new subsystem invariant category** (e.g. an `INV-AC` "AIoT + Cloud Readiness" family, the way Doc 16 opened `INV-SA` at §49), registered in the §0.3 prefix table + the §17 index + the §18 traceability matrix in the **same commit** as the Lock; invariant count **169 -> 170**; and -- because a new-doc Lock is **not** an amendment -- the **watermark stays AMD-94** (the drift discriminators are the count and the Locked-doc set, exactly as recorded for the Doc 16 Lock).

---

## C. INVARIANT-ID SOURCE-VERIFICATION -- every cited id RESOLVES and is accurately quoted

Each id checked against `governance/Architecture_Invariants_v1.md` (the §17 index + the body definition; the §49 INV-SA section; the §44 / §35 amendment sections). **No fabricated id; no mis-citation** -- the Research-6 fabricated-id failure does not recur here.

| Cited id (beat) | Resolves? | Register location | Says what the beat claims? |
|---|---|---|---|
| **INV-LF-01** | RESOLVES | §1 + §17 index | Yes -- "Core Functionality Without Internet." Supports "every automation decision runs locally." |
| **INV-LF-02** | RESOLVES | §1 + §17 index | Yes -- "Cloud Enhancement, Never Cloud Dependence"; the body's three-level no-outbound-capability enforcement supports the §3.4 cut-line / outbound-port framing exactly. |
| **INV-RF-01** | RESOLVES | §3 + §17 index | Yes, with a note -- "Integration Isolation." The beat (§3.4) extends it to a cloud accelerator as a "failure-isolated outbound adapter." Defensible (the isolation principle applies), but the cloud accelerator is not literally an "integration (device protocol adapter, third-party connector, plugin)"; INV-LF-02 is the tighter cite for "not a dependency," INV-RF-01 for "failure-isolated." Loose-but-acceptable. |
| **INV-ES-01** | RESOLVES | §2 + §17 index | Yes -- "Events Are Immutable Facts." Supports "immutable... log" in §2.1. (For the §3.1 "projections are derivable, replaceable... never a second source of truth" claim, **INV-ES-02** is the tighter parent -- see E1.) |
| **INV-ES-06** | RESOLVES | §2 + §17 index | Yes -- "Every State Change Is Explainable." But note it is already a parent of INV-SA-03, making the AIOT-INV-3 dual-citation redundant (B / E2). |
| **INV-SA-01** | RESOLVES | §49 + §17 index (line 1069) | Yes -- "Expressiveness Expands Only Into the Sealed Model (no runtime DSL)." Supports AI-as-author -> sealed permits. |
| **INV-SA-02** | RESOLVES | §49 + §17 index (line 1070) | Yes -- "Federation Non-Preclusion." The body even pre-states the beat's own claim that materializing `ScopeRef` is a formal AMD that must be AMD-94-envelope-slot-compatible. Exact match. |
| **INV-SA-03** | RESOLVES | §49 + §17 index (line 1071) | Yes -- "Explanation Is a Pure Projection of the Log (no parallel trace store)." Supports AI-as-reasoner + AIOT-INV-3. |
| **INV-SA-04** | RESOLVES | §49 + §17 index (line 1072) | Yes -- "Running Automations Degrade Deterministically." Supports the safety frame + AIOT-INV-1. |
| **INV-PD-07** | RESOLVES | §6 (base) + §35 (AMD-86 narrowing) + §17 index | Yes -- "Crypto-Shredding for Sensitive Data Lifecycle." The beat's §4 framing ("infrastructure/seams at MVP; operational shred post-MVP; interacts with retention D4") matches the AMD-86-narrowed body precisely (per-scope key infra at MVP; operational shred lands with the first cloud/institutional consumer). |
| **AMD-90-INV-01** | RESOLVES | §44 (body) + §17 index (line 1059) | Yes -- "Confirmation Never Blocks Runs and Never Retries... at no policy value does the engine re-issue a command autonomously." Matches "no-autonomous-retry contract" exactly. |

**Non-invariant references also confirmed:** **Doc 16 §3.3** (Explainability / audit -- exists, owns the audit projection), **Doc 16 §3.2** (component model -- exists), **Doc 16 §3.5/§3.6** (federation seam / cut-line -- exist), **AX-7 = Doc 16 OQ2** (component versioning/deprecation -- confirmed as a Doc 16 §15 NON-BLOCKING open question), **decision-record D2** (pure-function-replay) and **D4** (retention) -- confirmed. **AMD-94** 1-byte envelope-version slot -- confirmed.

**One sequencing flag (feeds E2), not a mis-citation:** **decision-record D2 is a ratified *decision*, not yet a registered *invariant*** -- the decision record explicitly defers minting D2's canonical `INV-...` id to "the normal review->ratify fold" and states "the PM does not mint the canonical id unilaterally." AIOT-INV-1 cites "D2" as a parent; at mint time it should cite the **registered** parents (INV-SA-04, AMD-90-INV-01) plus the D2-derived invariant **once that is minted** -- or cite D2 as "decision-record D2 (canonical invariant pending registration)." This keeps the composition from citing a parent that has no canonical id yet.

---

## D. DOCUMENT VERDICT -- **RATIFY-WITH-EDITS** (S1/S2 + E1-E5, all NON-BLOCKING)

No BLOCKING and no REVISE finding (review-and-quality §5: the doc does not misunderstand its subject, violates no unpatchable invariant, introduces no dependency-direction violation, and silently changes no Locked contract). Judged as a readiness/reservation doc per review-and-quality §1:

- **Precision -- PASS-WITH-EDITS.** Each reserved seam has a concrete non-preclusion mechanism (additive log-shipping; envelope-level scope; expansion-into-sealed-permits; LIVE-only log consumers; per-scope key destruction). The one place precision is asserted rather than operationalized is the **AI-proposes/engine-disposes** frame -- it states "no AI code path actuates outside the engine" without naming the **structural** mechanism that enforces it (the composition-root analog of INV-LF-02's "core has no outbound network capability"). -> **E3.**
- **Consistency -- PASS-WITH-EDITS.** Cross-references resolve to **real** sections (Doc 16 §3.2/§3.3/§3.5/§3.6; INV-SA/LF/RF/ES/PD ids; AMD-90-INV-01; AX-7; D2/D4; AMD-94). Two items: the **"NEW reserved seam"** labels overstate novelty (both new seams compose over existing invariants) -> **E4**; and the owns-vs-restates blur -> **S1**.
- **Invariant coverage -- PASS-WITH-EDITS.** Every cited id resolves and is accurate (§C). The independent §17 scan found **relevant-but-uncited** invariants -> **E1**.
- **Genuinely-non-precluding test (each seam) -- PASS.** No seam smuggles a design decision. The two flagged seams are clean: the **cloud-replication** seam defers "event-log-shipping vs CRDT sync" to the future federation/cloud doc (§7.3) and reserves only "replicates outward, additive"; the **SBOM/update** seam reserves only, with conformity-class sizing post-MVP. Both are genuinely non-precluding -- the edits (E1/E4) are about *citing the existing invariants they rest on* and *not overstating novelty*, not about a smuggled decision.
- **Open-question discipline -- PASS.** §7 lists 5 open questions, each explicitly NON-BLOCKING, with an explicit "No `[BLOCKING]` question gates V1." Verified none gates V1: scoping (Nick's call at review), invariant status (this review + Nick), cloud-replication shape (deferred to the future doc), AX-7 (a pre-existing Doc 16 OQ), CRA/PSTI sizing (post-MVP research). Correct.
- **DRAFT posture -- PASS (correct).** Watermark stays AMD-94 (a new-doc Lock is not an amendment -- confirmed against the §49 precedent); not self-ratified (goes through DOCS review -> Nick co-sign, like Doc 16); no invariant minted at DRAFT (candidates are PROPOSED). All three postures are correct as stated.

The edit list is larger than a single-issue review because the independent invariant scan and the scope-boundary analysis each surfaced items -- but **every edit folds cleanly and none gates the Lock.**

---

## E. CONSOLIDATED EDIT LIST (all NON-BLOCKING)

> Disposition: **S** = scope-clarity (tied to the SCOPE verdict); **E** = document edit (tied to the DOCUMENT verdict). "Resolve at Lock" items are ratification mechanics for the fold commit, not DRAFT defects.

### S1 -- Add a scope-boundary section: OWNS / RESTATES / COORDINATES-WITH. **[load-bearing for the new-doc status]**
Doc 17 currently has no §2-style "owns / does-not-own" section (Doc 16 has one -- §2.1/§2.2). Add it, with three explicit columns/lists:
- **OWNS (net-new):** the AI-safety frame (§3.3) and its candidate invariant; the cloud-replication seam (§4); the SBOM/signed-update/vuln-disclosure seam (§4); the substrate-as-a-named-cross-cutting-principle (§2.1/§3.1); the AIoT direction as four named seams (§3.2).
- **RESTATES / REAFFIRMS (owned elsewhere -- do not re-reserve):** federation seam (Doc 16 §3.5 / INV-SA-02); the local/cloud cut-line (Doc 16 §3.6); the enterprise audit projection (Doc 16 §3.3); crypto-shred (Doc 15 / INV-PD-07). Mark each row in the §4 table with its owning doc and the word "restated, not owned here."
- **COORDINATES-WITH but does NOT pre-empt:** the planned **B3-federation** doc and the **honest-hybrid** doc (Nick's B-1/B-2/B-3 rulings). State that Doc 17 reserves the *direction* and the two genuinely-new seams; the full federation/cloud *mechanics and invariants* are those docs' to mint.

This is what earns the new-doc cut and forecloses the three-way (Doc 16 -> Doc 17 -> B3/hybrid) drift hazard.

### S2 -- One sentence pinning the coordinate-not-pre-empt boundary in §5 (Boundaries).
§5 already lists the cloud/federation runtimes as OUT. Add: "This doc does not pre-empt the planned B3-federation and honest-hybrid design docs; it reserves the AIoT+cloud *direction* and the two new seams (cloud-replication, SBOM/update) and defers all federation/cloud *mechanics and their invariants* to those docs." (Closes the gap the decision record flags as "reaffirmed... already reserved in Locked Doc 16.")

### E1 -- Invariant coverage: cite the uncited-but-on-point invariants. **[the independent §17-scan deliverable]**
Add each with its mechanism:
- **INV-LF-05 (Convergent Sync Architecture)** -- governs the **cloud-replication seam** (§4) and the §7.3 "event-log-shipping vs CRDT sync" open question. INV-LF-05 *already* reserves the convergent-sync property (deltas, per-entity sequences, no central coordinator) and *already* leaves the algorithm open. The cloud-replication seam rests on it; cite it. **[most on-point missing invariant for the cloud seam]**
- **INV-PD-08 (Tamper-Evident System Integrity)** + **INV-CS-05 (Update Safety Mechanisms)** -- govern the **SBOM/signed-update seam** (§4). INV-PD-08 *already* mandates cryptographically signed update packages, signature verification, and integration provenance; INV-CS-05 *already* covers update-safety. The "signed-update" reservation is architecturally **owned by INV-PD-08**, with CRA/PSTI as the external *driver*, not the *reservation mechanism*. Cite both. **[most on-point missing invariant for the SBOM seam -- and the same INV-PD-08 catch the Doc 16 independent review made]**
- **INV-ES-02 (State Is Always Derivable from Events)** -- the tight parent for the §3.1 claim "projections... are derivable, replaceable optimizations over the log -- never a second source of truth." The beat cites INV-SA-03 + INV-ES-01 there; INV-ES-02 is the one that says it directly. Add it.
- *(Optional, lower)* **INV-ES-03 (Per-Entity Ordering with Causal Consistency)** and **INV-ES-07 (Event Schema Evolution)** -- for the "causally-chained" substrate language and the cloud-replication "No payload change" claim (paired with decision-record D3 additive versioning).

### E2 -- Right-size and re-parent the invariant candidates (per §B). **[Resolve at Lock]**
- Mint **AIOT-INV-1** as the sole first-class candidate; keep **AIOT-INV-2** and **AIOT-INV-3** as design principles (or mint AIOT-INV-3 only with de-duplicated parentage).
- Fix **AIOT-INV-1 parentage:** cite the *registered* parents (INV-SA-04, AMD-90-INV-01); cite D2 as "decision-record D2 (canonical invariant pending registration per the decision record's forward action)" -- or mint the D2 pure-function-replay invariant in the same fold so the composition cites a real id, not a decision id.
- Fix **AIOT-INV-3 redundancy:** drop the INV-ES-06 citation (INV-SA-03 already subsumes it); cite INV-SA-03 alone.

### E3 -- Operationalize "AI proposes; the engine disposes" **structurally**, not just by assertion. **[converts AIOT-INV-1 from asserted to enforced]**
§3.3 asserts "no AI code path actuates a device or mutates state outside the engine." Pin the *mechanism*, mirroring INV-LF-02's three-level enforcement: **a future AI module is wired at the composition root as a proposer-only adapter behind the inbound proposed-definition / proposed-command port, with no actuation capability and no outbound device/dispatch dependency** -- the same structural denial that gives core no outbound network capability. This is the enforcement AIOT-INV-1 needs to be a testable invariant rather than a principle ("wire a mock AI module; assert it cannot reach `ActionExecutor`/dispatch except via a proposed definition that the engine governs").

### E4 -- Re-label the two "NEW reserved seam" rows; they overstate novelty. **[ties E1 to S1]**
In the §4 table: the **cloud-replication** seam is a newly-*named* seam over **INV-LF-02 / INV-LF-05** (cross-instance sync + off-site backup are already reserved); the **SBOM/update** seam is a newly-*named* seam over **INV-PD-08 / INV-CS-05** (signed-update + provenance already reserved). Change "NEW reserved seam" -> "newly-named seam over existing reservations (cite the invariants)." Also add a one-line **non-preclusion-honesty clause** for cloud-replication: "outward cloud-replication does not foreclose or narrow the **INV-LF-05** convergent multi-instance-sync property; the federation/cloud doc owns the sync semantics" -- so a reader does not mistake "replicates outward" for a narrowing of INV-LF-05. (Directly analogous to the Doc 16 review's S2 ScopeRef honesty clause.)

### E5 -- Template / metadata + Lock-fold mechanics. **[Resolve at Lock; minor]**
- Add the standard design-doc **metadata header** (document type, status, subsystem, dependencies-with-section-refs, **dependents**, author, date). Populate **dependents** with the planned B3-federation + honest-hybrid + the future AI-milestone docs.
- Note the Lock-fold mechanics for the fold session (per the §49 new-doc-Lock precedent): a **Doc-14 master-architecture catalog entry** + the **Design-Documents table** row (Doc 17); the **§0.3 + §17 + §18** register stubs for the new `INV-AC` category **iff** AIOT-INV-1 is minted; watermark stays **AMD-94**; count **169 -> 170** iff one candidate mints.
- *(Low)* If "AIoT" and "universal substrate" are to be canonical terms, add Glossary entries at the fold (the doc mints no types, so this is minor) -- and keep "component-based automation definitions" consistent with Doc 16's canonical `AutomationComponent`.

---

## F. ANTI-REQUIREMENTS -- each tested for *operationalization*, not mere assertion

| Anti-requirement | Operationalized by (in the reservation) | Verdict |
|---|---|---|
| **Local-first inviolate** (cloud strictly additive; keys never leave the machine) | §3.4 cut-line restatement + INV-LF-01/02 three-level enforcement (composition root wires only-local deps; core has no outbound capability) + the §4 cloud-replication "additive, never a dependency." | **PASS (structural, inherited).** Rests on INV-LF-02 + Doc 16 §3.6; not newly built, correctly so. E1 adds INV-LF-05 as the convergent-sync parent. |
| **AI proposes / the engine disposes** (no autonomous actuation; no engine retry -- AMD-90-INV-01) | §3.3: AI proposal -> proposed definition/command -> deterministic engine (expansion into sealed permits + no-autonomous-retry + pure-function-replay) -> auditable. | **PASS-AS-RESERVATION, but asserted not structural** -> **E3.** The frame is correct and rests on real parents (INV-SA-04 / AMD-90-INV-01 / D2), but the *enforcement mechanism* (composition-root proposer-only port) is not yet pinned. E3 closes this. |
| **Explanation is a pure projection of the log** (no parallel trace store -- INV-SA-03) | §3.2 AI-as-reasoner reads the explanation projection; "no parallel trace store to build or trust." | **PASS (structural).** Rests squarely on INV-SA-03. |
| **No destructive forced migration** (federation/scope additive -- INV-SA-02) | §4 federation row (ScopeRef additive; materialization is a formal AMD, AMD-94-slot-compatible) + cloud-replication "No payload change" (pair with decision-record D3 additive versioning + INV-ES-07). | **PASS.** Rests on INV-SA-02; E1 (optional) adds INV-ES-07 / D3 for the replication "no payload change" claim. |

---

## G. Independence note + provenance

**Independence honored.** I formed the scope view first, from the beat + the Locked dependency docs + the spine current-state, then reconciled against the beat's stated lean and the companion decision record. The decision record (read for the ratified D1-D5 context the beat references) **does** carry mild scope-advocacy -- its purpose framing presupposes "a separate, co-equal artifact... kept cleanly apart" (a new-doc lean) -- so I treated its framing as a position, not a settled call. My decisive criterion (center-of-gravity / categorical fit, A.1) is **independent of** the record's framing and **differs from** the beat's lead argument ("first-class direction earns a named artifact"), which I judged insufficient on its own (A.3). The record's own "already reserved in Locked Doc 16; reaffirmed here" line, plus the snapshot's B-1/B-2/B-3 rulings, are what surfaced the fragmentation hazard (A.4) that the beat's framing does not foreground -- i.e. the independent pass found the risk the advocacy framing smooths over.

**Reads (independence-preserving):** the environment model (first); PROJECT_SNAPSHOT (current-state grounding only); Doc 17 in full; Doc 16 §2.1/§2.2/§3.1-§3.6 + its section map (the extension-alternative host); the Architecture Invariants §0.3-adjacent prefix context + §1/§2/§3/§6 bodies (LF/ES/RF/PD families) + §35 (AMD-86) + §44 (AMD-90-INV-01) + §49 (INV-SA) + the §17 index; the companion decision record (D1-D5); review-and-quality §1; constraint-enforcement; and the prior **Doc 16** independent review return (as the format/discipline precedent). **Not read (independence rule):** the v6 hub's §1 deliberation; the 2026-06-23 prior-art study. Scope judged on the doc + the Locked deps + the spine.

**Baseline confirmed at preflight (PASS):** docs HEAD **e47f01e** (Doc 16 LOCKED; watermark **AMD-94**; invariants **169/49**) with the **Doc 17 DRAFT present** at `design/17-aiot-and-cloud-readiness.md`; core **5363347** (M7.3 delivered). No truncated-tail artifact observed (Doc 17 tail intact on the host file tools).

---

## H. DONE-WHEN / hand-off to Nick

**Review only -- edits are NOT folded here** (review-separate-from-fold). The path: Nick **rules the scope** (new Doc 17 vs Doc-16 extension -- this review's independent verdict is **new doc, RIGHT, conditional on S1**) -> **folds** the consolidated edits (S1/S2 + E1-E5) -> **mints `[AIOT-INV-1]`** (de-duplicated, parentage fixed; keeps AIOT-INV-2/-3 as principles or mints AIOT-INV-3 only de-duplicated), opening the new `INV-AC` category in §0.3/§17/§18 in the **same commit** (count 169 -> 170; **watermark stays AMD-94** -- a new-doc Lock is not an amendment) -> **co-signs** -> **Doc 17 Locks** (as Doc 17, or as the Doc-16 extension Nick rules). None of the edits gates the Lock; all are NON-BLOCKING. The scope verdict requires no structural rewrite beyond the S1 boundary section.

### Suggested commit message (bang-free, backtick-free; use git commit -F)
```
docs(audit): add independent DOCS-Project review of Doc 17 (AIoT + Cloud Readiness) - new-doc cut affirmed (conditional), RATIFY-WITH-EDITS

Fresh, context-isolated, scope-independent second opinion on
homesynapse-core-docs/design/17-aiot-and-cloud-readiness.md (DRAFT).
Rules the §0 new-Doc-17-vs-Doc-16-extension call on the beat's own
merits, assesses the three [AIOT-INV] candidates, and source-verifies
every cited invariant id.

SCOPE VERDICT: a NEW doc (Doc 17) is the right cut - independently
affirmed on the center-of-gravity criterion (the subject's weight, the
substrate thesis, cloud-replication, SBOM/update, and the cross-cutting
AI-safety frame, lies outside Doc 16's automation charter), NOT on the
beat's lead "first-class direction" argument, which alone would justify
only a Doc-14 note. CONDITIONAL on S1: add an owns / restates /
coordinates-with boundary section, because as drafted the doc re-states
seams Doc 16 (federation, cut-line, audit) and Doc 15 (crypto-shred)
already own, risking the three-way Doc16 -> Doc17 -> B3/hybrid drift.

INVARIANT CANDIDATES: mint one of three. AIOT-INV-1 (AI is never an
autonomous actuator) MINT-AT-LOCK - it adds an AI-actor-routing
constraint its parents do not impose. AIOT-INV-2 KEEP-AS-PRINCIPLE -
near-duplicate of INV-LF-02 + INV-SA-02. AIOT-INV-3 KEEP-AS-PRINCIPLE
or mint only de-duplicated - overlaps INV-SA-03, which subsumes the
redundant INV-ES-06 citation.

ID SOURCE-VERIFICATION: all 11 cited ids RESOLVE and are accurately
quoted (INV-LF-01/02, INV-RF-01, INV-ES-01/06, INV-SA-01..04, INV-PD-07,
AMD-90-INV-01; plus Doc 16 sections, AX-7, D2/D4). No fabricated or
mis-cited id. Flag: decision-record D2 is a ratified decision, not yet a
registered invariant - re-parent AIOT-INV-1 accordingly.

DOCUMENT VERDICT: RATIFY-WITH-EDITS (S1/S2 + E1-E5, all NON-BLOCKING; no
BLOCKING/REVISE). E1 cites uncited-but-on-point invariants (INV-LF-05
for cloud-replication; INV-PD-08 + INV-CS-05 for SBOM/update; INV-ES-02
for the substrate claim). DRAFT posture correct: watermark stays AMD-94,
not self-ratified, no invariant minted at DRAFT. No BLOCKING question
gates V1.

Review only - edits NOT folded (review-separate-from-fold). Nick rules
scope -> folds -> mints [AIOT-INV-1] de-duplicated (count 169 -> 170,
watermark stays AMD-94) -> co-signs -> Doc 17 Locks.
```
