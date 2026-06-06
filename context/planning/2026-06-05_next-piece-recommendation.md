<!--
file: context/planning/2026-06-05_next-piece-recommendation.md
purpose: PM recommendation for the next major piece after M4 COMPLETE — M5/M6 sequencing, AMD-65 timing, and the website/docs interleave decision. Companion to the M4 retrospective and the release-runway roadmap.
audience: Nick, PM
update-cadence: one-shot (consumed when Nick picks the posture and the W24 plan is written)
state-type: future
status: CURRENT — issued 2026-06-05 (M4 closeout)
anchors: context/planning/2026-05-31_release-runway-roadmap.md (§3 bands, §5 posture); context/audits/2026-06-05_M4-retrospective.md (§8 strategic, P6); context/planning/phase-3-milestone-backlog.md (M5/M6/AMD-65 rows)
-->

# Next Major Piece — Recommendation (post-M4)

**TL;DR — recommendation:** Make the next piece **M5 (Platform API + test-support) run as a deliberately small Core lane, paired with the W3 website/docs standup as a non-preemptable parallel lane.** M6 (Configuration) follows M5 as the next Core band. AMD-65 (the Expectation codec) is cleared opportunistically inside the M5 window as M9 prep — small, not urgent. Do **not** make the next piece pure Core; doing so defers the roadmap's #1 schedule risk a third time.

This is a recommendation and proposed scope only — no coding instruction is issued and no milestone is started in this session (documents-only). Nick picks the posture; the W24 weekly plan ladders into it.

---

## 1. Decision context

M4 is COMPLETE (`8ef9e9f`, watermark AMD-64, `projectionVersion` 5). The candidates for "next" are:

- **M5** — Platform API + test-support. Backlog: *no hard deps*; PlatformPaths impls (Linux, development), HealthReporter, and the test-support module (InMemoryEventStore / SynchronousEventBus / TestClock / NoRealIoExtension).
- **M6** — Configuration System. Backlog deps: state-store (M4 ✓) + persistence (M2 ✓) — both satisfied. YAML pipeline, JSON-Schema validation, AES-256-GCM secret store, hot-reload atomic swap, `ConfigurationAccess`/`ConfigurationProvider` impls. Research 5 is assessed (A−); AMD-66–71 are allocated.
- **AMD-65** — the Expectation persisted codec. QUEUED, BLOCKING-for-M9 only. M9 is ~late-Jul/Aug, so this is queued-not-urgent. Its only hard consumer is M9, and it already ships an executable acceptance test (`@Disabled("AMD-65 pending")`).
- **W3 website/docs standup** — Core-independent. The release-runway roadmap names it the **lowest-dependency, highest-slip-cost** track and the project's real schedule risk. It was W23 Goal 4 — planned, then deferred because M4.C consumed the week.

The binding constraint is the one the roadmap and the M4 retrospective both name: **a single developer + AI agents is an effectively-serial pipeline, and so far 100% of it has gone to Core.** Whatever is chosen as "the next major piece" gets the pipeline; everything else waits. That is why the choice is not merely "M5 or M6" — it is "does non-Core finally get a protected lane, or does it slip again."

---

## 2. M5 vs M6 — sequencing and dependencies

Both M5 and M6 are dependency-unblocked today, so this is a sequencing call, not a gating one. **Recommend M5 first.** Reasons:

1. **M5 is small and dependency-free.** The roadmap rates it "~small (much test-support exists)"; the backlog says "no hard deps." It can start cold with zero authoring prerequisites.

2. **M5 is a force-multiplier for everything after it.** The test-support module produces exactly the doubles every subsequent milestone needs: `TestClock` (which directly addresses the recurring `NO_DIRECT_TIME_ACCESS` / Clock-injection pain that cost us M2.4/M2.5 arch-debt and shows up in every Phase-3 §4c reminder), `InMemoryEventStore` and `SynchronousEventBus` (which make M6 hot-reload tests, M7 automation tests, and M9 supervisor tests cheaper and more deterministic), and `NoRealIoExtension`. Building this *before* M6/M7/M9 lowers the cost and raises the safety of all three. Doing it after means those milestones invent ad-hoc doubles (which is how we got `EchoStateRule`/`StandardCapabilities` lifted out of fixtures under pressure in M4).

3. **M6 is the bigger, security-sensitive piece and benefits from M5's tooling.** M6 carries an AES-256-GCM secret store and a hot-reload atomic swap — exactly the kind of state-machine-under-concurrency work that is far easier to test deterministically with `SynchronousEventBus` + `TestClock` in hand. M5-first means M6 is built on the better test substrate.

4. **M6 has a PM-side authoring prerequisite that parallelizes cleanly behind M5.** M6's amendments (AMD-66–71) are currently allocated/deferred-to-M6, not yet ratified, so M6 cannot start coding until they're authored and reviewed. That authoring is PM work that can run *while the Coder executes M5*. (Note: AMD-67 was deferred on REC-41; REC-41 became AMD-54/55 and froze in M4.C, so the schema-versioning pattern AMD-67 waited on now exists — the PM should confirm at M6 authoring that this unblocks it. This is a small, concrete way M4.C paid forward into M6.)

The cost of M5-first is that it pushes M6 — which is on the M7 critical path — back by one small milestone. That cost is real but minimal (M5 is days, not weeks) and is repaid immediately by the test substrate. **Sequence: M5 → M6 → M7/M8.**

---

## 3. AMD-65 — clear it in the M5 window, don't headline it

AMD-65 is the cleanest "defer-well" item we have: tracked, BLOCKING-for-M9-only, with an acceptance test already in the tree. M9 is ~late-Jul/Aug, so it is genuinely not on the near-term critical path and should **not** be the next major piece.

But it is small (the AMD-52 bit-anchored-float precedent makes `WithinTolerance(double,double)` a known quantity; the other three Expectation variants are trivial), and the M4.C context that surfaced it is fresh *now*. Recommend authoring it during the M5 window — PM authors the amendment on the lightweight block-track (retrospective §6 / P4), it gets a lightweight DOCS review, and it becomes a small Coder WU that can ride alongside or just after M5. This clears the M9 prerequisite while the iron is hot, rather than re-loading the whole `Expectation`/`CapabilityInstance` serde context in August. If the M5 window is tight, it slips to just-before-M9 with no harm — but the cheap, low-risk move is to knock it out now.

---

## 4. The interleave decision — stand up website/docs NOW (the crux)

**Recommend: yes, interleave the W3 website/docs standup now, as a non-preemptable parallel lane — do not defer it a third time.**

The case is in the M4 retrospective §8 and the roadmap §5, and M4 is the proof: posture (A) was adopted for W23, the website/docs standup was W23 Goal 4, and it was deferred because M4.C took the week. "Interleave when Core allows" has empirically resolved to "never," because Core always has gravity (it's the spine, it has momentum, the next milestone is always queued). With 173 days to the Nov 25 target, ~11 Core major groups still to build (including the highest-risk Zigbee work and a 72-hour validation gate), **and** three non-Core tracks at zero, the website/docs track cannot keep losing to whatever Core milestone is in flight. If it does, it compounds into a fall crunch stacked on top of Zigbee + validation — the roadmap's stated slip mechanism.

The reason **now** is the right moment: M5 is the smallest Core milestone on the board. The slack M5's small size creates is exactly the room to start the parallel lane without stalling Core. If we wait for a "quieter" window, there won't be one — M6 is bigger, M7/M8 is large, and M9–M15 are the back half of the runway.

What "non-preemptable" means concretely: the W24 weekly plan gives the website/docs lane a defined first-week increment and a Done-when, and that increment is **not** allowed to be traded away to accelerate M5. (Retrospective P6.) This is the structural floor that makes posture (A) real instead of aspirational.

A note on scope discipline: the website/docs lane is genuinely Core-independent for the bulk of its first increment (positioning, architecture, privacy framing, structure) — the only Core-gated piece is the auto-generated API/config *reference*, which needs the M10/M11 specs (~Aug). So starting now buys the Core-independent 80% and leaves only the reference for later. There is no dependency excuse to wait.

---

## 5. The recommendation, concretely

**Next piece = M5 (Core, small) + W3 website/docs standup (non-Core, protected), run as parallel lanes. M6 follows M5. AMD-65 cleared in the M5 window.**

Pipeline shape for the next ~1–2 weeks:

- **Lane 1 (Core, Coder):** M5 — Platform API + test-support. While the Coder executes M5, the **PM authors AMD-66–71** (M6 config amendments) and **AMD-65** (Expectation codec, lightweight block-track) so M6 and the M9-prerequisite are review-ready the moment M5 lands.
- **Lane 2 (non-Core, PM/Hivemind):** the W3 website/docs standup — non-preemptable.
- **Then:** M6 (Configuration) as the next Core band; AMD-65 Coder WU slotted opportunistically; M7/M8 after M6.

### Proposed scope — M5 (Platform API + test-support)

*Sketch for the W24 plan and the eventual coding instruction; not the instruction itself.*

- **Platform API:** `PlatformPaths` implementations (Linux + development profiles); `HealthReporter`. Confirm against `platform/platform-api/MODULE_CONTEXT.md` + verbatim `module-info.java` at instruction time (Research-6 embedding rule).
- **test-support module:** `InMemoryEventStore`, `SynchronousEventBus`, `TestClock` (`Clock.fixed(...)` factory — the canonical injection that retires the recurring `NO_DIRECT_TIME_ACCESS` foot-gun), `NoRealIoExtension`. This module is whitelisted (`com.homesynapse.test..`), so the §4c arch-rule reminder does **not** apply to it — but everything that *consumes* it downstream is non-whitelisted, so the test doubles must themselves inject `Clock` cleanly.
- **Apply retrospective P2 (consumer/pin survey) at instruction time:** if M5 touches any enum/registry/manifest set (e.g., a health-status enum or a platform-profile set), enumerate every count-pin / aggregator / switch before issue so M5 goes GREEN in one round.
- **Size:** small. One coding milestone, no expected amendment beyond what M5's own contracts need. Deliberately small so Lane 2 has room.
- **Done-when:** M5 committed + build GREEN (full `./gradlew check`) + PM WUCP Phase 2 → APPROVE, with the closeout run against the enumerated artifact checklist (retrospective P3).

### Proposed scope — W3 website/docs standup (first increment)

*Per the roadmap §4 and master-release-plan §4.3; the Core-independent increment.*

- Scaffold the public site (Docusaurus per master plan §4.3) in a new repo (`homesynapse-site` or equivalent — confirm naming with Nick); apply the brand/design-system shell.
- Draft 3–4 positioning/architecture pages sourced from the Locked design docs + `context/strategy/` (What is HomeSynapse / Architecture Overview / Privacy Promise / Supported-Devices-or-Getting-Started scaffold).
- Explicitly **out of scope** this increment: the auto-generated API/config reference (M10/M11-gated, ~Aug).
- **Done-when:** site builds locally/staging; the initial positioning/architecture pages are drafted and reviewable.

---

## 6. Why not the alternatives

- **Not "M6 first."** M6 is bigger, security-sensitive, has an un-ratified amendment prerequisite (AMD-66–71), and benefits from M5's test substrate. M5-first costs only days and repays them immediately. M6 is the clear *second* piece.
- **Not "AMD-65 + M9 next."** M9 is ~late-Jul/Aug and depends on M5/M6/M7 maturity; pulling it forward now would jump the queue past its own prerequisites. AMD-65 rides the M5 window instead.
- **Not "pure Core (M5 then M6) and defer website/docs again."** This is the path of least resistance and the one M4 already walked. It defers the roadmap's #1 risk a third time and concentrates non-Core into the fall crunch. The whole point of posture (A) is that the parallel lane gets a protected floor — and the M5 window, being the smallest, is the cheapest place to install that floor.

---

## 7. What Nick needs to decide

1. **Confirm the posture:** M5 + protected website/docs parallel lane (recommended), vs. pure-Core M5→M6 (defers non-Core again), vs. an MVP-scope cut (roadmap §5C).
2. **Confirm M5-before-M6** sequencing (recommended) or override to M6-first.
3. **Confirm AMD-65 timing** — M5-window authoring (recommended) vs. just-before-M9.
4. **Website/docs repo name + hosting** (Docusaurus per master plan §4.3) so the standup can scaffold.

On Nick's confirmation, the PM writes the W24 weekly plan to ladder into the chosen posture, authors AMD-66–71 (+ AMD-65), and issues the M5 coding instruction (with the P2 consumer/pin survey applied).

---

**Companion documents:** M4 retrospective (`context/audits/2026-06-05_M4-retrospective.md`, esp. §8 + P6); release-runway roadmap (`context/planning/2026-05-31_release-runway-roadmap.md`, §3/§5).
