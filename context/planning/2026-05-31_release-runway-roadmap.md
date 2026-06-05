<!--
file: context/planning/2026-05-31_release-runway-roadmap.md
purpose: Re-baselined now->launch roadmap for HomeSynapse v1. Anchors to master-release-plan.md (the original 37-week baseline) and overlays ACTUAL position as of 2026-05-31 + the recomputed latest-start dates for the non-Core tracks (UI, website/docs, distribution). Companion to, not replacement for, the master plan.
audience: Nick, PM
update-cadence: per-milestone (or when the launch target / scope changes)
state-type: future
status: CURRENT — issued 2026-05-31 (M4.B-S1 closeout)
anchors: context/planning/master-release-plan.md (37-week baseline); context/planning/phase-3-milestone-backlog.md (Core milestones); context/status/PROJECT_SNAPSHOT.md (current state)
-->

# HomeSynapse v1 — Release-Runway Re-Baseline (2026-05-31)

**Launch target:** ~late November 2026 (master plan: Nov 25). From **Jun 1** that is **~25 weeks / ~177 days**.

This re-baselines the original `master-release-plan.md` (37-week, 5-workstream roadmap) against where we actually are. It does **not** replace that plan — it corrects the picture and computes the dates that now matter. **Bottom line up front: Core is healthy and on/ahead of its own axis, but the three non-Core tracks (Web UI, Website/Docs, Distribution) are at zero and were supposed to run in parallel from Week 1. They are the real schedule risk, not Core.**

---

## 1. Where we actually are (2026-05-31)

**Core Runtime (W1) — strong.** Phases through the event/persistence/bus foundation are done; we are mid-**M4**:
- Workstream A (projection/derivation foundation) — **COMPLETE** (typed end-to-end + event-time-deterministic; `projectionVersion`=5; HEAD `e73e199`).
- Workstream B Stage 1 (Floor/Area/`Set<HardwareIdentifier>`, AMD-44) — **DONE** `e73e199`.
- **Remaining in M4:** B Stage 2 (EntityRole) + Workstream C (integration-api interface freeze, gated on Research 6 NQ-1..6 + the post-B device model).

**Core still to build after M4** (backlog "Future Major Groups"): **M5** Platform API + test-support, **M6** Configuration, **M7/M8** Automation (core + advanced), **M9** Integration Runtime, **M10** REST API, **M11** WebSocket API, **M12** Observability, **M13** Startup/Lifecycle (full), **M14** Zigbee Integration, **M15** Full integration + performance/validation. ~Eleven major groups; each historically comparable to M2/M3 (M3 = 18 Coder WUs).

**Non-Core tracks — effectively zero:**
- **Web UI (W2)** — no `homesynapse-ui` repo exists. Master plan scheduled it Weeks 11–26 (parallel). Not started.
- **Website + public docs (W3)** — no public-site repo exists (the `homesynapse-core-docs` repo is *internal design docs*, not the Docusaurus site). Master plan scheduled it Weeks 1–35 (parallel from day one). Not started.
- **Distribution / installer (W4)** — no packaging repo exists. Master plan Weeks 19–35. Not started.

The master plan's core assumption was that W2/W3/W4 run in parallel with Core from the start. In practice every session has gone to Core. So those three tracks are not "ahead/behind" — they're a **hidden, compounding backlog**.

---

## 2. The honest critical-path read

Two truths to hold together:

1. **Core has been fast** on the foundation (the plan's P1/P2 ran weeks early). But the *remaining* Core (M4-rest → M15) is the bulk of subsystem implementation — automation, integration runtime, the two API surfaces, observability, lifecycle, and the hardware-dependent **Zigbee** work (the single riskiest item, requiring real devices) plus a 72-hour validation gate. Even at strong velocity this realistically runs into **October**. That is roughly consistent with the master plan (Core/validation complete ~Week 32 / late Oct).

2. **A single developer + AI agents has been a fully-utilized, effectively-serial pipeline.** The master plan's risk register already flags "single developer capacity … on the critical path." The plan banked on AI multiplying capacity enough to run W1+W2+W3+W4 concurrently. That multiplication has gone entirely into Core so far. If the same pattern continues, UI + website + distribution get compressed into Oct–Nov on top of Zigbee + validation — the highest-risk window — which is how launches slip.

**The decision this roadmap forces:** non-Core work cannot stay parked until Core is "done." Either it interleaves into the weekly cadence **starting soon**, or the late-Nov target absorbs the risk, or MVP scope gets cut. (Options in §5.)

---

## 3. Core critical path — remaining milestone bands

Bands are *rough, velocity-dependent estimates*, not commitments. They assume Core stays the primary focus and the per-milestone WUCP discipline holds.

| Band | Core milestones | Rough size | Notes |
|---|---|---|---|
| **Now → mid-Jun** | M4 finish: **B-S2 (EntityRole)** + **Workstream C** (integration-api freeze) | ~1.5–2 wk | C gated on Research 6 NQ-1..6 (your calls — surfaced) + post-B model + P4 Doc-05 currency. |
| **mid-Jun → early-Jul** | **M5** Platform API + test-support; **M6** Configuration | ~2–3 wk | M5 is small (much test-support exists); M6 = YAML/schema/secrets/hot-reload. |
| **Jul** | **M7/M8** Automation (core + advanced) | ~2–3 wk | Trigger/condition/action, command ledger, cascade governance, concurrency modes. Large. |
| **late-Jul → Aug** | **M9** Integration Runtime; **M10** REST API; **M11** WebSocket API | ~4–5 wk | M9 = supervisor/health-FSM/thread-arch (large). M10/M11 partly seeded in M3.6e. **APIs are the W2 dependency.** |
| **Aug → Sep** | **M12** Observability; **M13** Lifecycle (full) | ~2–3 wk | Partly subsumed by M3.6. |
| **Sep → mid-Oct** | **M14** Zigbee Integration | ~3–4 wk | **Highest risk** — real hardware, ZCL + Tuya + Xiaomi codecs, dual coordinator. |
| **mid-Oct → late-Oct** | **M15** Full integration + perf + **72h validation gate** | ~2–3 wk | The go/no-go gate (MVP §8). |

That consumes essentially the whole runway on Core alone. Buffer is thin.

---

## 4. Non-Core tracks — latest-start dates (compute backward from launch)

| Track | Depends on | Earliest useful start | **Latest responsible start** | Why |
|---|---|---|---|---|
| **Website + public docs (W3)** | Almost nothing (positioning, architecture, privacy, supported-devices, getting-started scaffold) | **Now** | **~Jul** | Mostly Core-independent; auto-generated API/config reference needs M10/M11 specs (Aug), but the bulk (positioning, content, structure) can and should start now. Slipping it just compresses it into the launch crunch. |
| **Web UI (W2)** | Live data needs REST+WS APIs (M10/M11, ~Aug). Design system, component library, mock-data dashboard can start earlier. | **~Jun–Jul** (design + scaffold on mock) | **~late-Aug** (to integrate against real APIs and finish by Nov) | The plan allocated ~8–12 weeks. If it starts cold in Sep against a still-moving API, it collides with Zigbee + validation. |
| **Distribution / installer (W4)** | Needs Core mostly running (jlink image, systemd, .deb, install wizard) | **~Sep** | **~mid-Oct** | Packaging is meaningful only once the app boots end-to-end (post-M13). Plan: Weeks 33–35. Compresses fast if Core slips. |

The two that are dangerous to leave at zero are **website/docs** (can start now, no excuse to wait) and **Web UI** (long pole, API-gated but design-startable now).

---

## 5. The strategic choice (for Nick)

Pick the posture; the weekly plans follow from it.

- **(A) Interleave non-Core now (recommended).** Keep Core as the critical-path spine, but start the **website/docs** track immediately (it's Core-independent) and begin **UI design + scaffold on mock data** within a few weeks, so neither is a cold start in the fall. Costs some Core velocity; de-risks the launch date. This is what the master plan always intended — it just hasn't been happening.
- **(B) Core-first, accept the risk.** Drive Core to MVP-complete (~Oct), then sprint UI + website + distribution Oct–Nov. Maximizes Core focus; concentrates the highest risk into the smallest window; most likely to slip the date.
- **(C) Cut MVP scope to protect the date.** Decide now what's truly v1 vs. v1.x (e.g., narrower device support, a thinner dashboard, docs-lite at launch). Revisit `Six_Battlefields_MVP_Strategy.md` for the cut line. Combine with (A) or (B).

My read: **(A)**, with the **website/docs track kicked off this week or next** (lowest dependency, highest slip-cost) and **Core continuing as primary**. The UI long-pole gets a design/scaffold start once B-S2/C land.

---

## 6. Near-term (this is what the weekly plans execute)

- **W23 (Jun 1–7):** finish/advance M4 — author + issue **B Stage 2 (EntityRole)**; in parallel, you work the **Research 6 NQ-1..6** decisions (they gate Workstream C) and PM refreshes **Doc-05** currency. (PM recommendation; see the W23 plan once scope is confirmed.)
- **Decision pending (this doc §5):** the non-Core posture. If (A), W23 or W24 also stands up the **website/docs** track (repo scaffold + positioning/architecture content) as a parallel lane.

---

## 7. Pointers

- Original baseline: `context/planning/master-release-plan.md` (37-week, 5-workstream; phases P1–P7; success criteria §14; risk register §11).
- Core milestones: `context/planning/phase-3-milestone-backlog.md` (Future Major Groups M5–M15).
- Current state: `context/status/PROJECT_SNAPSHOT.md` (HEAD `e73e199`).
- MVP scope / cut line: `context/strategy/Six_Battlefields_MVP_Strategy.md`.
- Workstream C gate: `context/planning/2026-05-31_Workstream-C_gate-status.md` (Research 6 NQ-1..6).

**Bottom line:** Core is on track on its own axis and plausibly completes ~October. The launch date is gated by the three non-Core tracks that haven't started. Decide the §5 posture, then the weekly plans ladder into it.
