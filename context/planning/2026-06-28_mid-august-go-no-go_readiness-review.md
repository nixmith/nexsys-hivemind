<!--
file: context/planning/2026-06-28_mid-august-go-no-go_readiness-review.md
purpose: A candid, evidence-based mid-August go/no-go readiness review — the honest critical-path read (not a status recap) the v11 hub produced during the M7.5b coding wait. Assesses the four go/no-go gates, the real dependency chain + thin slack, the ~7-week absorption question, the two pacing risks + contingencies, and concludes on the critical path.
audience: Nick (the go/no-go owner + the strategic call); the v11 PM hub (carries the conclusions into orchestration); the bench/frontend/M9 lanes.
state-type: planning / readiness review (decision-support).
status: AUTHORED 2026-06-28 by the v11 hub (M7.5b in the Coder's hands). Evidence-based against the committed fleet (core 9ec5949 / docs 75d0345 / hivemind 9f12f80 / bench 2c0a33c). A living read — refresh at the next beat that moves a gate.
horizon: ~Aug 16 go/no-go = 49 days (~7.0 weeks) out; Nov 25 launch = 150 days out.
-->

# Mid-August Go/No-Go — Readiness Review (candid critical-path read)

**The frame.** Mid-August (~week 8, ~Aug 16) is a **readiness checkpoint, not the launch** (Nov 25). The question it answers is: *are the four gates credibly on track for Nov 25?* So each gate below is read as "credibly reachable by mid-Aug, on the current chain?" — and the review's job is to surface where that is **not** yet true while it is cheap to act on.

**Bottom line up front.** Gate 1 is done. The other three all funnel through one upstream dependency — **the bench** — which **has not started first-light**, and through **two long poles that are earlier than their calendar position implies** (the frontend hero views are unbuilt; M9 is unscoped pending the bench). Seven weeks is **tight but credible for a "conditional go"** — *if* bench first-light happens in the next several days and M9 is held to the curated Wave-1 set. The dominant schedule risk is not any single build; it is **the bench not starting**, because it gates two of the four gates at once. That is the thing to attack now.

---

## 1. The four gates — where each actually stands

| Gate | Honest status | What's real | What's missing |
|---|---|---|---|
| **1. Engine LIVE** | ✅ **DONE** | The M7.4 arc is complete + committed: the pipeline fires → dispatches → **confirms** end-to-end on the real composition root (`9ec5949`). OR-M7-WIRING resolved; D2 replay-purity CI-pinned. | Nothing. This gate is closed. |
| **2. Hero on real data** | 🟡 **PARTIAL — the API half is nearly there; the rendering + real-data halves are not** | Read-API: M7.5a (`/runs` + causal-chain) DONE + committed; M7.5b (`/non-firing` + `/automations`) in the Coder's hands. The frozen v1.1 contract is stable. | **(a) Frontend rendering it:** `web-ui/dashboard/` is a *buildable scaffold* — Preact+TS, FRONTEND_DOCTRINE, contract-check, bundle-size gate, `ci/frontend.yml` all in place, but `src/` is still just `app.tsx`/`main.tsx` (last web-ui commit = the Track-A first beat `b296e76`). **The hero views are not built.** The `nexsys-frontend` skill was *just* stood up to staff this — so most of the ~6–8 week long-pole is **ahead**, and its velocity is **unproven**. **(b) Real data:** the hero today renders on synthetic events; real device `state_reported` needs **bench first-light** (Stream A) — not yet run. |
| **3. Hardware validating** | 🔴 **NOT STARTED — the longest sequential pole** | The pieces are *designed*: AB-4 (cipher) is authored + un-gated (AMD-94 ratified); the bench is scaffolded; the corpus model + the M9-acceptance contract are reconciled (Stream B); AMD-87 (the prior pre-M9 codec blocker) is **already cleared** (`7f44bed`). | The whole build chain: **bench first-light → AB-4 → M9 (real Zigbee) → 72h-stable validation.** M9 is the big sequential item, and **its size is gated on what the bench finds** (the open D5 re-open trigger). AMD-CAND-1 (confirmation characterization) must ratify before M9's confirmation acceptance. |
| **4. Install proven** | 🟡 **HARNESS EXISTS — needs green on the head** | `distribution/` is well-developed: `install.sh`, `build-deb.sh`, `build-image.sh`, systemd unit, `smoke/run-smoke.sh` + `health-probe.sh`, update path, `ci/install-smoke.yml` (gate #4). The hard scaffolding is done. | **install-smoke GREEN on HEAD** (green-up pending). Lower-risk than gates 2/3 — the harness is built; it needs an installable head and a green run. Mostly de-risked; sequence it after the engine + a validated build. |

---

## 2. The dependency chain — what gates what, and where the slack is thin

```
  CRITICAL PATH (hardware + real-data):
  bench first-light ──► AB-4 (cipher, hard-order) ──► M9 (real Zigbee) ──► 72h-stable ──► install-smoke green
        │                                               ▲   ▲   ▲
        │ corpus + AMD-CAND-1 values + "modest map?"────┘   │   │
        │ (M9 acceptance spec; M9 SIZE gated here)          │   │
        │                                       AB-4 done ──┘   │
        │                                  AMD-CAND-1 ratify ───┘ (confirmation acceptance)
        │
        └──► real device state_reported ──► GATE 2 real-data half

  PARALLEL LONG-POLE (rendering):
  frontend hero views (scaffold ──► why-fired + did-confirm + why-not, on the real M7.5a/b endpoints) ──► GATE 2 render half
```

**Read the chain honestly:**

- **The bench is upstream of two gates at once.** It feeds gate-2's real-data half (real `CONFIRMED`/`UNCONFIRMED`) *and* the entire gate-3 chain (it is M9's acceptance spec, supplies the AMD-CAND-1 measured values, and **determines M9's size** via the D5 "is the `exposes`→capability map modest on real silicon?" trigger). Nothing on the hardware side or the real-data side moves until first-light runs. **This is the single thinnest piece of slack in the plan** — not because the work is huge, but because so much sits *behind* it and it is Nick's-hands-gated.
- **AB-4 → M9 is a hard sequential order** (trust-hygiene: cipher before real device data is written). AB-4 itself is small (authored, un-gated) but it is a gate, not a parallel task.
- **M9 is the long sequential pole**, and uniquely it is **un-sized until the bench reports.** A clean map → M9 is the Wave-1 adapter + codec (weeks). A messy map → M9 grows toward the curated-subset fallback (D5) and eats more of the runway.
- **72h-stable is a wall-clock floor** — 3 days minimum that cannot be compressed, and it sits *after* M9. For gate 3 to read "validating" by mid-Aug, M9 must land with ≥ ~1 week to spare.
- **The frontend is the parallel long-pole** with "no slack" (the contract-freeze's own characterization). It does **not** gate the hardware chain, but it gates gate-2's render half. Its risk is independent: even if the bench + M9 land, gate 2 is not "hero on real data" until a UI renders it.

---

## 3. Does ~7 weeks absorb it? — honest verdict + the two pacing risks

**Verdict: tight but credible for a *conditional* go — contingent on two things happening, and one of them is in the next few days.**

A realistic mid-Aug target is **not** "all four gates green for launch"; it is: gate 1 ✅; gate 2 = read-API done + bench producing real data + the frontend rendering *at least the two hero reads*; gate 3 = M9 landed + 72h validation in progress or done on the Wave-1 set; gate 4 = install-smoke green. That is a legitimate "conditional go" toward Nov 25. Reaching even that requires:

**Pacing risk A — the frontend's actual build progress (the parallel long-pole).** It is a scaffold today; the hero views are unbuilt and the lane's velocity is unproven. Seven weeks is within the ~6–8 week budget *only if the build is actually moving now*. **The cheap action: get a real progress read on the frontend lane this week** — is it building hero views against the M7.5a mocks, or still at scaffold? If it's stalled, that's the earliest, cheapest place to lose mid-Aug. **Contingency if it slips:** scope the frontend hero to the **two differentiator reads only** — "why didn't it fire?" + "did the device confirm?" — on the real M7.5a/b endpoints, and defer device-list/health/polish. The differentiator is the demo; a minimal honest hero on real data beats a broad unfinished dashboard. The go/no-go can be taken on that.

**Pacing risk B — M9's size, gated on the bench.** M9 is the longest sequential build and it cannot be scoped until first-light shows whether real silicon maps cleanly. **The cheap action: run bench first-light ASAP** — it converts M9 from "unknown size" to "scoped," and it does so weeks before M9 would otherwise start. **Contingency if the map is messy (M9 balloons):** the bench surfaces this *early by design* — scope M9 to the **curated Wave-1 hero set** (Hue + SNZB-03P + the immediate device breadth), lean on the D5 curated-subset fallback, and defer device breadth to post-go/no-go. M9-for-the-hero, not M9-for-the-catalog.

**The meta-risk that dominates both:** the bench is the critical path *and* it is the one thing the hub cannot advance autonomously — it needs the physical session. Every day first-light slips, it slips M9 sizing, the gate-2 real-data half, and the AMD-CAND-1 measured anchor, simultaneously. **The highest-leverage schedule-protective action available right now is bench first-light.** Surfaced now, while re-sequencing is free.

---

## 4. Conclusion — the bench is the critical path; first-light is the next focused block

This review confirms the standing belief: **the bench is the critical path and the next focused block to attack.** It is the common upstream of the two unbuilt gates, and **first-light pays off three ways in one physical session:**

1. **The moat measurement** — real `CONFIRMED` on the Hue (does it report the authoritative attribute back?) and honest `UNCONFIRMED` on a non-confirming path / the SNZB-03P. The `confirmed | unconfirmed | failed` differentiator stops being a design claim.
2. **The open D5 re-open trigger** — is the `exposes`→capability map "modest" on real silicon? A clean map confirms the declarative-core weighting (and keeps M9 small); a messy one re-weights toward the curated-subset fallback *before* M9 is committed.
3. **The AMD-CAND-1 confirmation-block values** — so the governance amendment anchors on **measured fact, not inference** (`confirmability`/`reportsAuthoritative`/`reportingPosture` per device).

The Phase-0 runbook is ready and the hub is standing by to orchestrate it **command-by-command** the moment the physical session is set up — holding its order: **Ethernet verified before Wi-Fi/2.4 GHz off** (don't cut your own SSH), and **the MG24 firmware reflash before any measurement** (factory 8.0.2/v14 carries the `ASH_ERROR_TIMEOUT` cluster; measure on known-good firmware only). The bench Phase-1 capture now records toward the confirmation block, so first-light produces the corpus values directly.

**What the hub does in parallel while the bench waits** (all non-Core-blocking, none tripping the deferred-gate or phantom guardrails): hold M7.5b for WUCP Phase 2; keep the quick-wins one-decision-away (AMD-CAND-1 dispatch ready to route; the AMD-CAND-2/3 Doc 02/08 fold pre-drafted; the D2 INV-id proposal ready to route; OR-GATE-M7.4 ready for Nick's Actions-tab confirm). The two genuinely schedule-bearing asks for Nick: **(1) run bench first-light soon**, and **(2) get an honest frontend-progress read this week.**
