<!--
file: context/audits/2026-08-15_G1-runbook_desk-adjudication_and_exhibit-readiness.md
purpose: DESK RETURN on the dispatch "read the G1 gate-day demo runbook and execute it." Three products: (1) the EXECUTION ADJUDICATION — what "execute" can and cannot mean from a remote hub session, measured not assumed; (2) the ORDERING FINDING — the local clock says the READ has not arrived and tonight's commissioned act is the REHEARSAL, not the performance; (3) the ACT-BY-ACT EXHIBIT-READINESS ADJUDICATION at the FE source, which is the desk half of the G-8/G-9 work the bench return left PARTIAL. Includes a zero-placeholder rehearsal card.
audience: the PM mission-control hub (v53) — intake per law 37. Nick (operator).
state-type: desk return / audit INPUT. Layer-1 desk evidence, NOT a gate. Refutation welcome in BOTH directions.
filed: 2026-08-15 ~20:45 CT, remote Cowork session under /nexsys-project-manager. Uncommitted; the hub's next order stages it.
laws honored: freeze GOVERNS (zero writes to any repo but this file; no build, deploy, pull, config edit, scenario, retune) · L3 (no token material was requested, received, or appears here) · findings-never-fixes · arc-discipline 1 (never author on an unmeasured hop — every capability claim below cites the instrument that measured it) · arc-discipline 13 (deploy-state re-derived at the instrument, never inferred) · arc-discipline 34 (chat is not a storage tier — this is filed, not banked in a transcript).
scope declaration: this session did NOT run the demo, did NOT touch the Pi, and has NO bench access. Every act-readiness claim below is derived from FE/core SOURCE at the working tree, and is explicitly labelled DEPLOY-UNVERIFIED wherever the deployed Pi build is the thing that actually matters.
-->

# G1 Runbook — Desk Adjudication + Exhibit Readiness

**Dispatch received:** *"Read `nexsys-hivemind/context/handoff/2026-08-14_G1_gate-day-demo_runbook.md` and execute it."*
**Runbook integrity:** the uploaded copy is byte-identical to the repo copy (`md5 81b43b07d0cda560b7d26523a4b850c4`, both 5 637 B). No drift; the file read is the file of record.

---

> # ⚠ THE HEADLINE — two things the hub must rule on before anything else
>
> **(1) The READ has not arrived. It is Saturday night.** The container clock reads **2026-08-16 01:45 UTC**, which in the operator's zone (`America/Chicago`, UTC−5) is **Sat 2026-08-15 20:45 CT**. The session banner's "Sunday, August 16" is the UTC date, not the operator's. Corroborated by the spine: the bench-evening return was filed at **18:19 CT today**, the v53 prompt banked at **18:41 CT today**, and both are hours old.
> **Consequence:** the runbook is the **gate-day** script and its own §4 protocol places it **LAST at the READ**. Running it now as the performance would execute the gate artifact a day early and out of its ruled order. **Tonight's commissioned act is the runbook's own `## Rehearsal` section — "Sat evening, once" — which is exactly what G-8 ruled RUN-TONIGHT-AS-COMMISSIONED and what the bench return recorded as `NOT RUN` (Block C, operator-directed hold).**
> **So the lawful reading of "execute it" tonight is: run the REHEARSAL, once, timed.** That is a decision for Nick, not an inference this session gets to act on — §6 row DX-A.
>
> **(2) The rehearsal is a ONE-SHOT instrument and it is currently pointed at exhibits that may not exist.** The runbook's Acts 1 and 3 select their exhibits by a rule — *"the most recent NIGHTLY bench-hero run (last night's fire)"* — that the bench return's own evidence contradicts: the explain surface's **newest run is Aug-11**, while nightlies fired every night through Aug-15. Under the runbook's no-iteration rule, a rehearsal driven by the literal script spends its single run discovering that. **§5 is a re-pinned rehearsal card that spends the run on an exhibit INVENTORY first — which is what G-8's own ruling already says the rehearsal now doubles as.**

---

## §1 Verdict table

| Item | Verdict | One line |
|---|---|---|
| **Runbook read + integrity** | **DONE** | Byte-identical to repo; read whole, with the freeze-day block, the bench-evening packet + return, the gate-weekend plan, and the v53 prompt as context. |
| **"Execute it" — the live demo** | **NOT EXECUTABLE BY THIS SESSION** | Measured, not assumed — see §2. The runbook's own `audience:` line already assigns it to Nick's hands. |
| **Ordering** | **⚠ FINDING — DX-1** | Local time is Sat 20:45 CT; the READ is tomorrow; tonight's act is the rehearsal. |
| **Act 1 — "why did it fire"** | **AT RISK — exhibit unpinned + nav path wrong** | DX-2, DX-3, DX-4. A source-grounded better entry path exists (DX-4) and may dissolve the F-13/F-14 presentation problem. |
| **Act 2 — "why didn't it"** | **PATH VERIFIED AT SOURCE; live availability unverified** | DX-5. Real picker, real 4-value verdict vocabulary. |
| **Act 3 — "did it actually confirm"** | **HIGHEST NARRATION RISK IN THE DEMO** | DX-6 (the honest-UNCONFIRMED tile may render as a red `Failed`), DX-7 (exhibit-2's source may carry no run at all), DX-8 (exhibit-1's latency pool is stale). |
| **Close — the availability tile** | **PASS — fully source-verified** | DX-9. Shipped copy matches the runbook's narration word for word. The safest act in the demo. |
| **The spoken "~1,700+ verdicts, zero false CONFIRMs"** | **SUBSTANTIATED** | DX-10. Reconciled at 1,728 on a ratified counting basis. One precision REC attached. |
| **Freeze** | **HELD** | This session wrote exactly one file — this one. Zero repo edits, zero commands on any host but read-only greps of the working tree. |

---

## §2 The execution adjudication — why this session cannot run the demo, measured

The runbook's `audience:` field reads *"Nick (runs it at the READ …); the hub (evidence steward at the read)."* The hub's role in this artifact is **steward**, not performer. That alone settles it, but the dispatch said "execute," so the capability question was measured rather than asserted (arc-discipline 1):

| Hop the demo needs | Instrument run | Result |
|---|---|---|
| SSH tunnel `-L 7070` from the operator's Windows box to the Pi | — | The Windows host is not a surface this session can drive; the device bridge exposes **mounted folders**, not a shell on that host. |
| A shell on the Pi | `device_bash` (runs in the operator's local Linux VM) | **NO NETWORK ACCESS** by construction — cannot reach the Pi. |
| A network path from the cloud container | cloud `bash` | Allowlisted egress only; **no route to the operator's LAN**. |
| A browser to drive the dashboard | `mcp__claude-in-chrome__list_connected_browsers` | Returned **`[]`** — **no Chrome extension is connected to this account.** Measured at 20:45 CT. |
| The API token | — | **L3 structurally forbids it** ("THE TOKEN NEVER ENTERS A CONVERSATION"). Even a connected browser would not change this: the token is read on the Pi terminal and typed into the browser by the operator, and it must be entered *before* the demo clock starts. |

**Verdict: NOT-EXECUTABLE-BY-HUB-SESSION.** No workaround is sought, and none should be: three of the five rows are physical facts about where this session runs, and the fourth is a law. **What a desk session *can* execute is the runbook's pre-flight — which is the rest of this document.**

---

## §3 DX-1 — the ordering finding (HIGHEST PRIORITY)

- **Now:** Sat 2026-08-15 **20:45 CT** (2026-08-16 01:45 UTC).
- **The READ:** Sun 2026-08-16. **Not today.**
- **The Sunday 03:30 CT nightly:** fires in **~6 h 45 m**. It has **not** fired. The v53 prompt's falsifiable prediction (first radio-present fire since Aug-13 on hop-verified cabling `3-2.4.2`; 7–8/9 confirms coordinator-absence was the whole story; 3/9 fires the pre-ruled G-11 rig recovery) is **still live and still falsifiable**. Nothing in this return touches it.
- **The runbook's own placement:** *"read LAST at the READ per the ledger's own §4 protocol."* Executing the performance today would break that order for no gain.
- **Tonight's commissioned act:** the runbook's `## Rehearsal` — *"Sat evening, once … One run only — findings ⏺ to the hub; no iteration, no tuning."* G-8 ruled it RUN-TONIGHT-AS-COMMISSIONED; the bench return recorded Block C **NOT RUN** at 18:19 CT under an operator-directed hold pending exactly this guidance.

**This session did not decide which reading of "execute it" Nick meant. §6 row DX-A puts it to him in one word.**

---

## §4 Act-by-act exhibit readiness — adjudicated at FE/core source

Method: the deployed *client* is a build of `homesynapse-core/web-ui/dashboard`; the deployed *server* is a build of core. Both were read at the working tree. **Everything below is a claim about the CODE. Where the claim that matters is about the PI'S DEPLOYED BUILD, it is labelled DEPLOY-UNVERIFIED** — because deploy-state is re-derived at the instrument and never inferred from an ordered sequence (arc-discipline 13), and the freeze forbids deploying to make it true.

### DX-2 — Act 1's exhibit-selection rule is contradicted by the evidence already on file

The runbook: *"the most recent NIGHTLY bench-hero run (last night's fire)."*
The bench return's A1 transcription: the runs list's **newest entry is 4 days old (Aug-11)**, and the visible history spans **Aug-4 → Aug-11** — while the digest shows the nightly firing **every night through Aug-15**. Nightly scenario runs therefore **do not reliably surface as explain-surface automation runs**; F-8 records the same and correctly notes the series was already sparse (nothing on Aug-8 or Aug-9 either, multiple runs on some days), so this is not a one-run-per-night surface at all.

Tonight this is sharper still: Aug-14/15 had **no radio at all** (F-0), and G-7 excluded them. So even a perfect Sunday fire is not guaranteed to produce an Act-1 exhibit.

**⇒ Act 1 must be re-pinned to a specific, verified historical run ID. The rehearsal is the act that pins it.**

### DX-3 — the runs list cannot name anything, at source

`format.ts:268` — `runName(name)` returns the literal `'An earlier automation'` **when the run summary's `name` is `null`**; `format.ts:274` carries the paired sentence *"This run happened under an earlier version of your automations, so its name is no longer on record. The run itself is preserved."* F-13's observation is therefore not a bug and not a data glitch: **every visible run predates the current automations config**, so its name is genuinely off the record. Under the freeze this is unfixable, and it is a real problem for Act 1's script, which says *"name the trigger."*

### DX-4 — ⭐ THE ONE HIGH-VALUE CORRECTION: enter Act 1 through the Ask-why hub, not the runs list

Two source facts the runbook does not use:

1. **F-15 confirmed at source.** `AppShell.tsx:11-18` ships nav `Overview · Ask why · Devices · Activity · Automations · Health`. **There is no "Runs" item.** The runbook's *"Runs surface"* names a screen that does not exist by that name; the list lives at `#/explain/runs`, under **Ask why**.
2. **`ExplainHubView.tsx` — the `/explain` hub carries a "Your automations" list that the runbook never mentions.** Per row it renders **`a.name`** (the *current* automation's real name), an On/Off pill, and **two deep links**: **"Why did it fire?"** → `#/explain/run/{a.lastRunId}` (rendered only when `lastRunId` exists; otherwise the row reads **"No runs yet"**) and **"Why didn't it?"** → `#/explain/why-not/{a.automationId}`.

**Why this matters more than any other line in this return:** a run reached through a *current, named* automation's `lastRunId` is by construction **not** one of the orphaned pre-config-change runs — so it should carry a resolvable name, which would dissolve **F-13 and F-14 for the demo without touching a line of code.** And the same screen serves **Act 2's** entry.

**Honest caveat, stated plainly:** this is unverified against live data. If every current automation row reads **"No runs yet,"** then Act 1 has **no named exhibit at all** under the freeze, and the fallback narration is the plan of record. **The `/explain` hub is the single screen that answers this — in one glance, in about ten seconds.** That is why §5 makes it the rehearsal's first act.

### DX-5 — Act 2's path is real; its live availability is DEPLOY-UNVERIFIED

`WhyNotView.tsx` with no `automationId` renders a **picker** (`#/explain/why-not`) listing automations by name; with one, it calls `api.getNonFiring(automationId)` and renders the frozen **4-value** verdict — `NEVER_TRIGGERED` · `CONDITION_NOT_MET` · `ACTED_BUT_UNCONFIRMED` · `DISABLED` — as one plain sentence plus the gating fact, with a `DP-B2` nuance (a clean recent run arrives as `NEVER_TRIGGERED` with a `lastRelevantRunId`, and is deliberately **not** presented as clean success) and a "sent nothing" branch. The vocabulary the runbook asks Nick to narrate ("never-triggered / condition-false / didn't-confirm") **is exactly what ships.** `endpoints.ts` binds it to `GET /api/v1/automations/{id}/non-firing`.

**Two honest notes.** (a) The endpoint's live status on the deployed build is **DEPLOY-UNVERIFIED** — the bench return's A1 exercised `B3:runs` and `B3:causalChain`, never `B3:nonFiring`. (b) The runbook prefers *"the no-change class."* The no-change run Nick already saw at A1 (*"all 9 planned steps ended without sending a command"*) is a **run**, not a non-firing explanation — different surface, different law. Conflating them at the READ would be an unforced error; naming the distinction aloud is a strength.

### DX-6 — ⚠ Act 3's centrepiece may render RED. This is the demo's largest narration risk.

`lib/verdicts.ts` states the rule in its own comments and implements it:

> *"Zigbee's honest-unconfirmed reasons are profile-note-driven (variable), so they are **NOT** pattern-matched — that class stays FAILED-rendered until the core fix carries the raw outcome (a recorded limitation, not a guess)."*

Mechanically: on a **pre-v1.1.2 payload** (no first-class `resultOutcome` on the wire), a Zigbee honest-unconfirmed action arrives flattened as `outcome: FAILED`; `classifyRecordedReason()` returns `null` because the reason is a variable profile note; the action therefore falls to **mode `settled-failed`, label `Failed`, tone `error`** — a red pill reading *"The command failed."*

That is the exact tile Act 3 exhibit 2 asks Nick to point at while saying *"the system says so instead of lying."* **If the wire is pre-v1.1.2, the tile contradicts the sentence.**

**The good news, verified at core source:** the fix is **in the code**. `RunExplanation.java:159-177` documents and carries `resultOutcome` (nullable) and `settled`; `StandardExplanationService.java:708-727` threads the last causation-matched `command_result.outcome` through every branch including the `UNCONFIRMED` one (`:720`); `:740-750` implements the settled derivation. `verdicts.ts` consumes the first-class field when present and keeps the recovery path only as graceful degrade.

**What is NOT established: that the Pi's deployed build emits it.** The bench return's A1 opened exactly **one** run, and it was a **no-change run with zero actions** — which exercises neither path. The `verdicts.ts` comment calling the recovery path *"the deployed surface until the SKIP-VIS deploy"* is a **stale comment relative to core HEAD**, and a stale comment is not deploy evidence in either direction.

**⇒ DEPLOY-UNVERIFIED, and it is cheap to settle.** Open **one run that has actions** and read the pill labels. If they come from the five-mode vocabulary — `Confirmed` · `Sent — no reply` · `Replaced` · `Accepted, never confirmed` · `Sent — not settled yet` · `Not recorded` — the v1.1.2 wire is live and Act 3's narration stands as written. If failures render a generic red **`Failed`**, the wire is pre-v1.1.2 and **Act 3's script needs its sentence pre-adjusted before the READ, not discovered during it.**

### DX-7 — Act 3 exhibit 2's *source* is also at risk, independently of DX-6

The runbook: *"a `CONFIRMATION_TIMED_OUT` from the s31 leg's recent nights IS the exhibit."*
`command-confirm-s31` is a **bench scenario** — a direct command POST by the runner — not necessarily an **automation run**, and the causal-chain surface renders automation runs. Whether the s31 leg leaves a run detail with action verdicts at all is **unverified**. Compounding it: G-7 excluded Aug-14/15 as rig-invalid, so "recent nights" for a *radio-present* s31 timeout means **Aug-13 at the latest** (prior radio-present FAILs: Aug-9, Aug-10, Aug-13) — and Aug-12/13 are **absent from the explain surface** (F-8).

### DX-8 — Act 3 exhibit 1's latency pool is stale

Measured `ON-latency` in the 15-night window: `3.65 · 0.30 · 0.17 · 0.36 · 0.16 · 0.30` s. The most recent is **Aug-12 (0.30 s)**; Aug-13 read `n/a(FAIL)`; Aug-14/15 are rig-invalid. Aug-12 is **not on the explain surface**. So exhibit 1's candidate pool is the **Aug-4 → Aug-11** runs, and the runbook's *"read the number aloud"* needs a run that actually carries a measured value. **Pin it at the rehearsal.**

### DX-9 — the Close act is fully source-verified. It is the safest act in the demo.

`OverviewView.tsx:88-115` ships exactly the four rows the runbook narrates — **`Available` (n of total) · `Offline` · `Not determined yet` · `Stale readings`** — under the line **"Counts reflect each device's last report — not a live connection test."** The source comment states the intent in the same register the runbook uses: *"Available" is what the system last CONCLUDED from reports, never a live-contact claim.* The runbook's closing sentence — *"even the summary tile refuses to claim what it hasn't measured"* — is a fair description of shipped code. **No change recommended.**

### DX-10 — the spoken verdict count is substantiated; one precision REC

Reconciled at **1,728 cumulative recorded verdicts, zero false CONFIRM** — the event-level split being **19 `state_confirmed` + 1 024 `command_confirmation_timed_out` + 685 `command_result`** (`context/assessments/2026-07-11_go-no-go-criteria_draft.md` C1, the v42-beat-3 citation reconciliation; the counts-by-event-type form with positions-citable-on-demand was **RULED** to satisfy the positions-cited clause, Nick's word, v43 beat 3). C1 is **EXCEEDED** — 8.6× the N≥200 MUST. The runbook's *"~1,700+"* is accurate and conservative.

**REC (hub/Nick rules, not a defect):** only **19** of the 1,728 are `state_confirmed`. *"Zero false CONFIRMs across ~1,700+ recorded verdicts"* is **true**, but a listener can hear *"1,700 confirmations."* One clause closes it — *"…recorded verdicts of every class, of which the confirmations are one"* — and it costs three seconds. Given D-1 already ships a hardened fence with DO-NOT-SAY items and a dagger-at-the-read, this belongs in that fence or nowhere; this session does not rule on it.

### DX-11 — a free instrument the rehearsal already carries (F-21)

F-21 left the app's **port re-acquisition after the 16:38 re-attach UNVERIFIED**, and it is the residual that could make Sunday's fire fail *even with the radio present*. The runbook's **Close** act already lands on the Overview availability tile. **Reading the `Available n of total` row there — and whether the S31 shows a last-report after 16:38 — is not a new act, a new command, or a freeze exception. It is an observation at a screen the script already opens.** If devices read `Available` on fresh reports, the app has the port and F-21 substantially discharges hours before the 03:30 fire, for free. If they read `Not determined yet` / `Stale`, the hub has that signal **before** the fire rather than after it. **Recorded as an observation to make, not an act to add.**

---

## §5 The rehearsal card — zero-placeholder, ready to run tonight

**Only if Nick rules DX-A = REHEARSE.** This is the runbook's own script with the exhibit-selection re-pinned per DX-2/DX-4 and the nav corrected per DX-4. **Nothing is added to the bench; every step is a browser read.** Laws carried unchanged: **L3** (token read on the Pi terminal, typed into the browser only, entered BEFORE the clock) · **one run only, no iteration, no tuning** · **findings-never-fixes** · **HANDS OFF the s31 legs and the nightly machinery** · **the freeze governs — nothing deploys.**

**Setup (before the clock; not counted).** Windows terminal, leave running:

```
ssh -N -L 7070:127.0.0.1:7070 pi
```

Browser → `http://localhost:7070/` → AuthGate. On the **Pi** terminal:

```
cat /home/homesynapse/hs-bench/config/initial_api_token
```

Read on screen, type into the browser field only (⚠ L3). Fallback path if absent: `cat /home/homesynapse/.homesynapse/config/initial_api_token`. *(A1 confirmed the first path is the live one; one rejected entry occurred there and was operator-side — enter it unhurried, before the clock.)*

**Act 0 — THE EXHIBIT INVENTORY (~3 min, before the timer). This is the act that makes the single rehearsal run worth its cost.**

Navigate to **`#/explain`** — the sidebar item is **"Ask why."** ⏺ RECORD, from the **"Your automations"** section:

1. how many automations are listed, and **their names verbatim**;
2. for each row, whether it offers **"Why did it fire?"** or reads **"No runs yet"**;
3. **the single most important datum in this rehearsal:** does **any** row offer "Why did it fire?" — *(yes ⇒ Act 1 has a NAMED exhibit and F-13/F-14 dissolve for the demo; no ⇒ Act 1 runs on an orphaned run and the fallback narration is the plan of record — a FINDING for the READ, not a repair.)*

Then click the **"Why did it fire?"** of the first row that offers one (fall back to `#/explain/runs` → newest entry only if none does). ⏺ RECORD which you used.

**Act 1 — "Why did it fire?" (~3 min; timer ON from here).** Walk the chain aloud, one hop per sentence: trigger event (name the log token on the tile) → condition evaluation → each action with its verdict. State the continuity line once: *"every tile here carries the same token the event log carries — this is a projection of the log, not a story about it."* ⏺ RECORD the run id + whether the automation **NAME resolved** or read "An earlier automation" + screenshot the full chain.

**Act 2 — "Why didn't it?" (~2.5 min).** From `#/explain` click **"Why didn't it?"** on a named row (or go to `#/explain/why-not` for the picker). ⏺ RECORD which automation, the **verdict word** rendered (`NEVER_TRIGGERED` / `CONDITION_NOT_MET` / `ACTED_BUT_UNCONFIRMED` / `DISABLED`), and the explanation **verbatim**. Read it aloud; state the law: *"never-triggered / condition-false / didn't-confirm are distinguished — and this is derived from the log; it never upgrades or replaces a verdict."* Screenshot. **If the surface errors or empties: ⏺ it and move on — that is the DX-5(a) answer and it is worth having.**

**Act 3 — "Did it actually happen?" (~3 min). Read the PILL LABELS first — they answer DX-6.** On a run detail **that has actions**, ⏺ RECORD **every action pill label verbatim**, then hunt the three exhibits:

1. **CONFIRMED with latency** — a `Confirmed` pill carrying a measured value; read the number aloud. ⏺ the value.
2. **Honest-UNCONFIRMED with its measured reason** — ⏺ **the exact label**. `Sent — no reply` / `Accepted, never confirmed` ⇒ **the v1.1.2 wire is deployed and Act 3's script stands.** A generic red **`Failed`** ⇒ **pre-v1.1.2 wire; the narration needs pre-adjusting before the READ** (DX-6). **Either outcome is a good rehearsal result — one confirms the script, the other prevents a contradiction in front of the room.**
3. **Deliberately-superseded, verdict-free** — a `Replaced` pill (label + glyph + tone, no verdict claim). ⏺ present / absent.

*(If no run in the visible history has actions at all: ⏺ that fact and stop Act 3 — it is the finding, and it is exactly what the READ needs to know in advance.)*

**Close (~1 min).** `#/overview` → the availability tile. ⏺ RECORD the four rows **as numbers** — `Available n of total` · `Offline` · `Not determined yet` · `Stale readings` — plus the "last report — not a live connection test" line. Narrate: *"even the summary tile refuses to claim what it hasn't measured."* **Then the DX-11 free read: do the counts show devices Available on fresh reports (post-16:38)?** ⏺ it — that is F-21's answer, hours before the 03:30 fire. **Stop the timer. ⏺ the elapsed time.**

**If something breaks mid-rehearsal:** narrate it as evidence, do not fix it (the runbook's own rule). ⏺ what rendered, move to the next act. Findings are tomorrow's read-material, not tonight's repairs.

---

## §6 Decision rows for the hub — one-word-rulable

| # | Question | Options | This session's REC |
|---|---|---|---|
| **DX-A** | What does "execute the runbook" mean tonight? | **REHEARSE** (run §5 once, timed) · **HOLD** (nothing tonight; the READ runs the runbook cold) · **PERFORM** (run the gate-day demo now) | **REHEARSE.** G-8 already ruled it; the bench return left it the only open block; the runbook itself commissions it for Sat evening; and §4 shows three acts whose exhibits are unpinned. **PERFORM is not recommended** — it executes a gate artifact a day early and out of the ledger's §4 order. |
| **DX-B** | Does Act 1 enter via the **Ask-why hub's named-automation list** rather than the runs list? | **ADOPT** · **DECLINE** | **ADOPT.** Source-verified; costs nothing; may dissolve F-13/F-14 for the demo; and it corrects a nav name (F-15) that would otherwise misfire live. |
| **DX-C** | Is the **Act-0 exhibit inventory** added ahead of the timer? | **ADOPT** · **DECLINE** | **ADOPT.** G-8's own ruling says the rehearsal now doubles as an exhibit inventory; this makes that explicit instead of hoping the script discovers it. |
| **DX-D** | **DX-6** — how is Act 3 exhibit 2 handled if the deployed wire is pre-v1.1.2 and the tile reads red `Failed`? | **PRE-ADJUST the narration** (name the flattening honestly as a known client-side limitation with the fix already in core) · **DROP exhibit 2** · **RULE AT THE REHEARSAL'S ⏺** | **RULE AT THE REHEARSAL'S ⏺** — the pill label settles it in one glance and costs nothing to obtain. If it does read red, **PRE-ADJUST rather than DROP**: naming a known, already-fixed-in-core rendering limitation *is* the honesty posture, and it is far stronger than a surprise in the room. |
| **DX-E** | **DX-10** — does the D-1 fence gain the one clause distinguishing *verdicts of every class* from *confirmations*? | **ADOPT** · **DECLINE** | **ADOPT** if the fence is still editable; it is three seconds of speech against a real mishearing risk. **Nick's call — it touches the D-1 language he already hardened.** |
| **DX-F** | **DX-11** — is the availability-tile read recorded as F-21's discriminator? | **ADOPT** · **DECLINE** | **ADOPT.** Zero cost, no new act, no freeze exception, and it moves F-21 from "residual risk at the READ" to "measured before the fire." |

---

## §7 What this session did NOT do — the limits of this return

Stated so the hub can price it honestly:

1. **Did not touch the Pi, the bench, or any repo but this file.** No build, deploy, `git pull`, config/constants/YAML edit, scenario invocation, retune, or restart. The freeze is untouched.
2. **Did not run the demo or the rehearsal**, and did not ask for the token (L3).
3. **Did not verify anything about the DEPLOYED build.** Every source claim in §4 is about the working tree. `A1` proved the chain renders and the item-1 null-crash is gone; it did **not** prove the deployed wire carries `resultOutcome`, and this return does not claim it does.
4. **Did not run the full 11-check freshness preflight to PASS.** Checks 1/5/6/8/10 and the Check-3 `git log` comparison were **not** run — the dispatch was gate-day-critical and time-boxed, and the newest spine artifacts (v53 prompt 18:41 CT, PROJECT_SNAPSHOT chain, the bench return 18:19 CT) are hours old, which is the freshness the checks exist to establish. **Check 9 records as STALE (mirror unverified from remote)** per the standing remote caveat — Nick's `diff -rq` is the instrument of record. **This return is therefore an INPUT, not a gate**, and no forward authoring rides it.
5. **Did not adjudicate the Sunday digest** — it has not fired. The v53 prediction stands untouched.
6. **Did not rule on anything.** DX-A…DX-F are RECs. The hub and Nick rule.

**Refutation welcome in both directions.** The load-bearing desk claims are cheap to check: `AppShell.tsx:11-18` (nav), `ExplainHubView.tsx` (the named-automation list + both deep links), `format.ts:268,274` (the name fallback), `verdicts.ts` (the not-pattern-matched Zigbee comment + `actionVerdict`'s `FAILED` default), `RunExplanation.java:159-177` / `StandardExplanationService.java:708-727,740-750` (`resultOutcome` + `settled` present in core), `OverviewView.tsx:88-115` (the four rows).

---

## §8 Route-back

*Intakes as the next v53 hub beat. The hub rules DX-A first — it is time-boxed by tonight — then DX-B/DX-C fold into the rehearsal card, DX-D waits on the rehearsal's ⏺, and DX-E/DX-F are one word each. If DX-A = REHEARSE, the rehearsal's ⏺ set supersedes §4's DEPLOY-UNVERIFIED labels with instrument evidence and the bench return supersedes-in-place with Block C complete. The Sunday 03:30 digest remains the standing next instrument and is untouched by this return.*

---

*End of return. Layer-1 desk evidence. Every capability claim cites the instrument that measured it; every source claim cites the file. No API token material appears anywhere in this file. Nothing here retro-fails a closed ledger row.*
