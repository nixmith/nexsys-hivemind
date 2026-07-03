<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-07-02 (v14 hub, beat 52 — M9.1 COMMITTED ec2e3b4 CI-green; extensibility assessment filed; fleet: core ec2e3b4 / docs 1509b34 / hivemind a770091+beat-52 / bench 5ceff3b / skills 90f8258). Prior stamp chain preserved in archive/PROJECT_SNAPSHOT-beats-06-41-rotated-2026-07-02.md frontmatter.
-->

# Project Snapshot

> **2026-07-02 (v14 hub, beat 52 — M9.1 LANDED on main: core `ec2e3b4`, ci.yml ✅ + install-smoke ✅; the EXTENSIBILITY & PLUGIN-ECOSYSTEM ASSESSMENT filed.)**
> Selective stage held exactly (26 / 11-web-ui-excluded); hivemind beat-51 `a770091`. DP-B one-line confirm pending (Nick).
> **Assessment** (`context/assessments/2026-07-02_extensibility-and-plugin-ecosystem_PM-assessment.md`, two-survey grounding): D1 breadth YES-by-architecture · D2 AI/AIoT the-substrate-is-the-moat · D3 plugins NOT-YET (the one seam class never formally reserved; SDK/marketplace promised with zero governance footprint) · D4 longevity YES-with-named-dependencies. Escalations: **R-A Doc 18 seam-reservation authorization · R-B AX-7 ruling · R-C Connect-paywall-line review.** Binding-now watchlist: M9.3 profile registry + website IA + the queued DP-B/C/D one-liners.
> Fleet: core `ec2e3b4` · docs `1509b34` · hivemind `a770091`+beat-52 · bench `5ceff3b` · skills `90f8258`.
> **Next:** Nick: DP-B confirm + R-A/R-B/R-C + FE-1b results. Hub: M9.2 JIT authoring on Nick's word (charter notes + both-graph-knobs pre-verification + DP-E seam). Detail: pm-handoff beat-52 (pointer, not copy).**

> **2026-07-02 (v14 hub, beat 51 — M9.1 DELIVERED by Claude Code + hub-audited ACCEPT; gate GREEN round 2 [`check` 149]; THE INTEGRATION SPINE IS LIVE.)**
> `command_issued` → `command_dispatched` → `CommandRoutingSubscriber` causation-join → `CommandHandler.handle(CommandEnvelope)` on per-adapter VT executors. First `IntegrationSupervisor` impl (DP-10 FSM · DP-11 threads · W8 clock-driven backoff · DP-9 zero-mint lifecycle events), the public assembly, Phase-6 wiring behind the canonical 7-arg `HomeSynapseCore` ctor (empty factories skip Phase 6 — `Main` byte-identical). **INV-ES-09 pinned** by the extended replay gate (routable registered fake; recorder-zero-across-REPLAY + LIVE positive control). Zero mint 71/41/53; zero DDL.
> Round-1 bounce: `:assertMaxHeight` (the ruled lifecycle→integration-runtime edge deepens the ruled path 7→8; ceiling raised with a do-not-raise note). Lessons: pin BOTH module-graph knobs at pre-verification; CC's in-session Gradle was permission-DENIED — allow targeted compile/test for M9.2 to recover the shift-left.
> Rulings: all four [REVIEW]s ACCEPT (corrected-B7/DP-12 Function param · DP-3 decoder pair · W4 abandon() gateway [Nick co-signs at commit] · maxHeight). The lane's fleet fixed 4 supervisor lifecycle bugs in-session (+1 regression). DP-B = already ruled at beat 46 (deterministic derivation = permanent policy) — Nick one-line confirm before M9.2.
> Change set EXACTLY 26 core paths — SELECTIVE stage (exclude `web-ui/`; the 11 web-ui files are FE-1b's, in flight). Messages staged: `_scratch/2026-07-02_core_m91_commit-msg.txt` + `_scratch/2026-07-02_hivemind_beat-51_commit-msg.txt` (5 paths).
> Fleet: core `e3d7296`+M9.1-wt(26) · docs `1509b34` · hivemind `91203c1`+beat-51 · bench `5ceff3b` · skills `90f8258`.
> **Next:** Nick: selective core commit → push → ci.yml+install-smoke glance → hivemind beat-51 → DP-B one-line confirm. Hub: M9.2 JIT authoring (grounding-subagent; charter notes + both-knobs pre-verification). FE-1b return → audit → its own commit. Detail: pm-handoff beat-51 (pointer, not copy).**

> **2026-07-02 (v14 hub, beat 50 — M7.5c-a LANDED: `check` 149 GREEN → core `e3d7296` pushed → ci.yml ✅ + install-smoke ✅ on the push. OR-GATE-M7.5c-a RESOLVED; M9.1 UNBLOCKED + ROUTED to Claude Code.)**
> One hub-fixed gate round (2 AssertJ capture errors, test-only; lesson recorded — within the P5 one-round target). Hivemind beat-49 committed `8a34a7f`.
> **Discovery (spine correction):** `install-smoke.yml` is ACTIVE on main (since `652f9b3`) and green on every push — the carried "install-smoke UNSCHEDULED" gate-4 item is CORRECTED; the residual gate-4 surface is the WEBSITE build only (content exists; lane launches after FE-1b).
> **Routing (Nick):** M9.x → Claude Code (host-side compile loop; the hub stays single-spine-writer + auditor; returns ride coder-handoff/cross-agent per protocol) · FE-1b → a separate Cowork lane (prompt: `context/handoff/2026-07-02_FE-1b_v111-fold-and-live-smoke_session_prompt.md`).
> Executed: the beat-46-ruled backlog M9-row split (M9.1 NEXT-ROUTED · M9.2–4 JIT · M9-deferred; charter-pointed) + beat-50 currency note; W27 midweek block; M9.1 dispatch annotation (HEAD `52824e9`→`e3d7296`, delta disjoint from the read-set; CC re-runs the STOP gates per the instruction's own baseline clause).
> Fleet: core `e3d7296` · docs `1509b34` · hivemind `8a34a7f`+beat-50 · bench `5ceff3b` · skills `90f8258`.
> **Next:** FE-1b launch (Nick, fresh Cowork) ∥ M9.1 (Nick opens Claude Code) → hub audits both returns → M9.2 JIT authoring → website lane after FE-1b → M9.3/M9.4 → bench acceptance + 72 h soak (NQ-6 during). Detail: pm-handoff beat-50 (pointer, not copy).**

> **2026-07-02 (v14 hub, beat 49 — M7.5c-a DELIVERED by the first in-conversation Coder lane; hub two-layer audit = WUCP Phase 2 ACCEPT, zero defects.)**
> A4 `/internal/projection` + A5 `/internal/dlq` now emit the frozen v1.1.1 `{data, meta}` envelope (DRIFT-1 close): A4 data = frozen {mode, viewPosition, lagEvents, projectionVersion} + ruled extras {entityCount, ready}; A5 data = {depth, parkedSubscribers} + additive `subscribers[]`. `lagEvents` = max(0, logHead − cursor) via a composition-root `LongSupplier` (`eventStore::latestPosition`); `PROJECTION_VERSION` hoisted to a single constant feeding both `StateProjection.create` and the gateway.
> RULED: parkedSubscribers = dlqDepth>0 ACCEPT (A5's DLQ framing; SUSPENDED visible via additive mode) · P6 ETag note-and-defer ACCEPT (304 is an API-wide non-feature; parity delivered) · P2 idiom-not-helper LOGGED (nine-handler extraction = post-M9 candidate WU).
> Change set EXACTLY 10 core files, hub-verified porcelain-exact (2 endpoints · RestFilters 5→8-arg gateway · HomeSynapseCore wiring · 2 test classes, 11 tests, Clock.fixed throughout · EndpointE2eIT consumer → `$.data` paths · 3 MODULE_CONTEXTs). Zero mint 71/41/53; both module-infos + every build file UNCHANGED; zero DDL.
> Check-8 archival EXECUTED at this quiescent window (separator relocated above the six ruled 06-27/28 notes; M7.5c-a note sole active). Beat-48 committed+pushed by Nick: hivemind `dd162e2`.
> **OR-GATE-M7.5c-a OPEN** — Nick: targeted + full `check` → core commit (staged `_scratch/2026-07-02_core_m75ca_commit-msg.txt`, stages exactly 10) → push → `ci.yml` glance. M9.1 routing BLOCKED until resolved (§4b); FE-1b launches on the landing.
> Fleet: core `2786526`+M7.5c-a-wt · docs `1509b34` · hivemind `dd162e2`+beat-49 · bench `5ceff3b` · skills `90f8258`.
> **Next:** gate → core push+CI → M9.1 (serial Coder lane) ∥ FE-1b (frontend lane). W27-plan + backlog M9-row updates ride the M9.1 issuance edit. Detail: pm-handoff beat-49 (pointer, not copy).**

> **2026-07-02 (v14 hub, beat 48 — LAUNCHED; the deferred spine rotation EXECUTED — phantom-safe, file-tools-only; preflight STALE-benign → reconciled → re-run PASS, all 11 checks.)**
> Rotated: snapshot masthead beats 6–41 (27 entries) → `archive/PROJECT_SNAPSHOT-beats-06-41-rotated-2026-07-02.md`; the 2026-06-19/21-era Current-Work-Unit blocks (5) + the pre-beat-era Recent-Session-Log rows (30) → `archive/PROJECT_SNAPSHOT-work-unit-blocks-and-session-log-rotated-2026-07-02.md`; pm-handoff beats 5–43 (33 sections) → `archive/pm-handoff-beats-rotated-2026-07-02.md`.
> The v11-era Latest-commits / Last-updated / Current-state fields RETIRED to pointers (truth-hierarchy — they had drifted to AMD-95/170/50-era claims); retained beats converted to short-paragraph blocks (env-model §8). Live spine: snapshot ~38 KB (was 154.8) · pm-handoff ~25 KB (was 138.9).
> Check-8: the six ruled 06-27/28 Coder notes queued for below-separator archival at the M7.5c-a WUCP quiescent window (env-model §2b Coder-in-flight caution). pm-lessons +3 (two-grep absence rule · `add --dry-run` lock · keep-both-audit-layers). OR-GATE-M7.4 ledger-reconciled RESOLVED (beat-43 ci.yml subsumption). v13 prompt archived.
> Method: three write-disjoint agents under hub two-layer audit — one agent transcription defect self-caught pre-write, one hub post-return frontmatter correction; the redundancy is the mechanism.
> Fleet: core `2786526` · docs `1509b34` · hivemind `b9349e8`+beat-48 · bench `5ceff3b` · skills `90f8258`.
> **Next:** Nick commits beat-48 (hivemind only; HOST porcelain = 9 paths — the VM view lags pm-lessons.md per §2; message staged `_scratch/2026-07-02_hivemind_beat-48_commit-msg.txt`) → M7.5c-a → FE-1b on its landing → M9.1 on its WUCP close. Detail: pm-handoff beat-48 (pointer, not copy).**

> **2026-07-02 (v13 hub, beat 47 — the v13 CLOSE) — pre-commit audit standing (env-model §10, Nick's check institutionalized); `git add --dry-run` lock hazard + >30 min lag correction folded; v14 AUTHORED (first-act: the deferred rotation via a phantom-safe file-tools-only method — do not re-defer). Fleet: core `2786526` (FE-1 committed, 16 files audited-clean) · docs `1509b34` · hivemind `41a105d`+beat-47 · bench `5ceff3b` · skills `0825409`. M7.5c-a routes to the Coder NOW; M9.1 issue-ready (corrected); FE-1b awaits M7.5c-a; the website lane + install-smoke are the two unstarted mid-Aug surfaces. Detail: pm-handoff beat-47 (pointer, not copy).**

> **2026-07-02 (v13 hub, beat 46) — both lane returns AUDITED + ADJUDICATED (detail: pm-handoff beat-46 — pointer, not copy).
> Verdicts: M9-authoring = PASS-with-one-correction (WU-M9.1 §A31/B7 "no ConfigurationAccess impl" REFUTED — `ScopedConfigurationAccess` exists; correction folded into WU + instruction);
> FE-1 = PASS, two drifts adjudicated on the truth hierarchy with OPPOSITE rulings (DRIFT-1 bare `/internal/*` → Core conforms [M7.5c-a micro-WU, ISSUED, sequenced BEFORE M9.1]; DRIFT-2 URI problem-type → the freeze mis-transcribed Locked Doc 09 → v1.1.1 amendment FOLDED).
> Nick's four rulings: DP-A ratify-all (M9.1→M9.4 split + C/D/E/F) · DP-B deterministic identity policy · DRIFT-1 conform-first · DRIFT-2 amend-freeze.
> Coder sequence: M7.5c-a → M9.1 (corrected, issue-ready) → M9.2–M9.4 JIT from the return's charter. FE-1b after M7.5c-a lands.
> The FE lane's uncommitted `web-ui/dashboard/**` commits on this beat (message staged).
> core `52824e9`+FE-1-uncommitted · docs `1509b34` · hivemind `07f3065`+beats-46/lane-files · bench `5ceff3b` · skills `0825409`.**

> **2026-07-01 (v13 hub, beat 44) — skill-source precision pass: pointer-not-copy applied to BOTH skill mastheads; Check 9 → STALE pending Nick's mirror sync.**
> Nick's directive: audit ClaudeFolder (esp. the two skills) for precisely-articulated, token-economical instruction design. Method: an Explore-agent survey + hub direct verification of every load-bearing claim before editing.
> **Applied (hivemind skill sources):** (1) `project-manager/SKILL.md` masthead — the copied volatile state (HEADs/watermark/counts/"next slot," stale at AMD-95/170/50/`eed477e`) REPLACED by an explicit **state-pointer rule**
> ("this file carries no project state; re-derive at preflight; a state claim in a skill file is stale by construction") + the durable disciplines retained;
> (2) the PM Mode-3 §"Phase 3 vocabulary" 2026-06-19-era state narrative (cited the June-19 hub prompt as standing + W26 as current) REPLACED by durable vocabulary + a pointer paragraph;
> (3) `coder/SKILL.md` masthead — same restructure (durable build disciplines retained; state → pointer; the illustrative count cite de-fanged to `NN/NN/NN`);
> (4) `freshness-preflight.md` internal-consistency fix ("10-check superset"/"ten checks" strays → eleven);
> (5) `coder-handoff.md` frontmatter restamped (had frozen at 2026-05-27/M3.7 while the body ran to AB-4; now points at the newest entry + spine as authoritative).
> **Verified-refuted (no edit):** the survey agent's "CLAUDE.md says 19-module but actual is 22" claim is FALSE — exactly 19 `module-info.java` main source sets exist; CLAUDE.md is correct (trust-but-verify catches subagents too).
> **Verification:** both mastheads grep-clean of state tokens; preflight strays 0; no NUL/encoding damage (the VM "binary" flag was a long-line grep heuristic).
> **Logged, deferred:** the mega-line/token-economy overhaul (~440 lines >600 chars across the hot path, worst = coder-lessons; fold into the phantom-gated beat-block rotation, converting snapshot beats to short-paragraph entries per env-model §8);
> a coder/references content-refresh pass post-M9 (dates old, content verified functionally coherent by survey — restamp only with a real content pass).
> **Check 9 is STALE by design** — Nick runs the external mirror sync (preferably BEFORE launching the two lanes so they load the clean skills; not blocking — both lane prompts pin baselines + mandate the preflight, which overrides any stale skill masthead).
> **Next:** Nick: beat-44 commit → mirror sync → launch the two lanes (unchanged from beat 43). core `52824e9` · docs `1509b34` · hivemind `45de9b5`+beat-44 · bench `5ceff3b` · skills `846fe56`.

> **2026-07-01 (v13 hub, beat 43) — the beats-41/42 fleet is COMMITTED + PUSHED (all five repos); ci.yml VERIFIED GREEN on core HEAD; the two parallel lanes are AUTHORED and launch-ready.**
> Nick ran the full host-side package: docs **`1509b34`** (AMD-96 + AMD-97 + INV-ES-09 — the governance fold, 7 files) · hivemind **`cea7ae1`** (carries beats 41 AND 42 — the message says "beat 41"; cosmetic)
> · core **`52824e9`** (the frontend.yml source-copy sync) · skills **`846fe56`** (the nexsys-frontend carry — the v12 residual CLOSED) · bench holds `5ceff3b`.
> **Bench `git status` clean in Nick's terminal — the phantom diagnosis is CONFIRMED** (the VM's mass-deletion view was a truncated read of `.git/index`; nothing was ever wrong host-side).
> **Gate of record: `ci.yml` GREEN on `52824e9`** (screenshot-verified: Build & Check 3m5s, Gradle 8.8, `check` ✅) — this subsumes the OR-GATE per-commit residual for the whole ancestor chain (AB-4/M7.5a/b/frontend).
> **`frontend.yml` note:** its path filter is `web-ui/dashboard/**`, so `dbb0109` (which touched only `.github/workflows/`) could never have triggered it — **`52824e9` is its FIRST triggering push**; Nick's Actions glance on that run is the one open gate item.
> **Dependabot re-surfaced at push: 5 (1 critical, 1 high, 3 moderate)** — the Security-tab shipped-vs-dev triage stays open (beat-33 decision tree; Jetty-via-Javalin prime suspect).
> **New CI-housekeeping residual (logged):** the Actions annotation — checkout@v4 / setup-java@v4 / setup-gradle@v4 target deprecated Node 20; bump the action majors at a convenient window (non-blocking).
> **Lanes authored (launch after the beat-43 commit):** `context/handoff/2026-07-01_M9-authoring-lane_session_prompt.md` (write-isolated M9 instruction authoring against corpus 5ceff3b + AMD-97 at docs 1509b34 + the seven acceptance additions; returns to the hub for audit)
> + `context/handoff/2026-07-01_frontend-live-integration_FE-1_session_prompt.md` (FE-1 per FE1_GO_LIVE.md + the four E5 rendering semantics as one-click scenarios; M9-independent; needs Nick for the Core boot + token).
> **Next:** Nick commits beat-43 (hivemind) → launches both lanes as fresh Cowork conversations → returns route here. core `52824e9` · docs `1509b34` · hivemind `cea7ae1`+beat-43 · bench `5ceff3b` · skills `846fe56`.

> **2026-07-01 (v13 hub, beat 42) — THE GOVERNANCE QUEUE IS RATIFIED + FOLDED (Nick's four rulings): AMD-96 + AMD-97 RATIFIED, INV-ES-09 registered — watermark AMD-95→97, invariants 170→172/51. M9 IS UNBLOCKED.**
> Nick ruled via the v13 decision pass: (1) **AMD-96 consolidate+ratify** — folded with the CAND-2/3 verbatim diffs as §2.A/§2.B (Kelvin-at-ingestion CT row + 0x010D note + §3.10 light-row color de-invite + §3.6 non-precluding note; all BEFORE anchors confirmed verbatim)
> + the bench §3.3 currency (measured baseline 7.4.5.0/v13; v14/ASH batch contingency; VID:PID port-id rule, never descriptor strings; version-at-stack-init) + the NEW Doc 08 §3.7 OccupancySensing row;
> (2) **AMD-97 ratified with full fold** — Doc 08 §3.6 `confirmation[]` (8 fields stated; enum `degradeRule`; the E5 taxonomy split carried by `confirmability × reportsAuthoritative`; measured Wave-1 worked example + corpus pointer; 4 engine-consumption caveats)
> + Doc 02 §3.8 confirmability override + **AMD-97-INV-01 (never-false-CONFIRMED, §51)** + the Doc 16 §4 V1-wire-subset recording note;
> (3) **D2 → INV-ES-09** (§2), watermark-neutral, FSM+per-subscriber-guard text, AIOT-INV-1 citation fixed in both register locations;
> (4) **next = M9 authoring + FE-1 live-integration lane in parallel.**
> **Verification: every edit grep-confirmed; the invariant total re-derived from the §17 table = 172 exactly; nav-index currency-fixed (its watermark line had trailed at AMD-87).**
> The three hivemind governance files closed (RATIFIED/APPLIED status lines). Docs-repo commit PREPARED for Nick (`_scratch/2026-07-01_host-side_commands.md`, updated — docs commit added; all commits host-side, phantom active).
> **Next Core slot: author M9** against the measured corpus + AMD-97 + the beat-41 acceptance additions (fresh-context session recommended; grounding-subagent-before-authoring).
> **Frontend: launch FE-1 live-integration** (M9-independent; route the E5 rendering semantics). docs `75d0345`+AMD-96/97-fold-uncommitted · core `dbb0109` · hivemind `89da546`+beats-41/42 · bench `5ceff3b` · skills `5bc78bc`+carry.

**Last updated:** RETIRED as a field (v14 hub, 2026-07-02) — the NEWEST masthead beat above is the authoritative last-updated record (truth-hierarchy: never trust a copied stamp; the v11-era narrative this field carried is in git history, pre-rotation blob).

**Current state:** POINTER, not copy (v14 hub, 2026-07-02) — re-derive from the NEWEST masthead beat above + the backlog's newest currency note + `git log` per repo. This field carried a v11-era narrative that had drifted against the ratified state (AMD-95/170/50 vs the actual AMD-97/172/51; "AB-4 uncommitted" vs long-committed); retired per the truth-hierarchy discipline, prior text in git history. Durable frame only: the Core engine ACTS, CONFIRMS, EXPLAINS (both hero halves on the live log), and ENCRYPTS-AT-REST from genesis; the dashboard is live-integrated; the moat is measured (bench) and ratified (AMD-97). Phase 3 — test-first implementation.
**Open flags:** See **`## Open Risks`** below for the live list. **Standing deferred:** OR-M13-SDNOTIFY (sd_notify AF_UNIX-datagram transport -> M13; JDK-21 has no AF_UNIX SOCK_DGRAM; seam-tested; M5-D decision matrix authored). **No open deferred build gates** (M7.2b GREEN, zero gate-fix rounds). **Check 9 PASS as of 2026-07-02** (both mirrors verified byte-identical at the v14 launch preflight; goes STALE again after any skill-source edit until Nick's next mirror sync). The M6-era open-flags ledger (AMD-66..71 / OR-M6-NONCE / OR-PD-07-AMD, all RESOLVED) rotated -> the 2026-06-22 archive.
**Hardware (standing):** **Wave 1 ✅ RECEIVED 2026-06-23** — MG24/EZSP + Philips Hue RGBW 2-pack + 2× SNZB-03P motion + USB extension = the FULL hero set (the MG24/EZSP runs motion→light on its own). **Wave 2 (ZBDongle-P/ZNP second path + device breadth) ORDERED, not yet received.** **Meantime strategy = FRONT-LOAD the bench** (the highest-leverage parallel track now): characterize on the EZSP path via a reference stack (no M9 code) → device corpus + durable TEST FIXTURES (M9 acceptance + M7.4 E2E) → Doc 02/08 MATCH/GAP verdicts → harden the repeatable device-onboarding pipeline so Wave 2 + every future device flow through it seamlessly. See `context/planning/2026-06-22_hardware-bench-bringup-and-device-characterization_brief.md` + the v6 prompt §8.E + the fan-out Session C.
**M4 retrospective:** `context/audits/2026-06-05_M4-retrospective.md` (sizing, the instruction-scope-miss pattern + the consumer/pin survey fix, deferred-gate shift-left, the partial-closeout finding, the debt register, strategic/velocity, and the keep-doing list). For M4 execution history see the Recent Session Log below.
**Latest commits:** RETIRED as a field (v14 hub, 2026-07-02) — re-derive fleet state from the NEWEST masthead beat above + `git log` per repo (truth-hierarchy: never trust a copied HEAD). The v11-era narrative this field carried is preserved in `archive/PROJECT_SNAPSHOT-beats-06-41-rotated-2026-07-02.md`.
**Current phase:** P3 — Implementation (test-first).
**Days remaining:** ~151 (to Nov 25, 2026)
**Launch target:** November 25, 2026 · **Mid-August go/no-go ≈ week 8** (the 4 gates: engine LIVE / hero on real data / hardware validating / install proven)

---

## Current Work Unit

**Current work unit:** re-derive from the NEWEST masthead beat above (pointer, not copy — v14 hub, 2026-07-02).

_The 2026-06-19/21-era work-unit blocks + the pre-beat-era Recent Session Log rows rotated 2026-07-02 → `context/status/archive/PROJECT_SNAPSHOT-work-unit-blocks-and-session-log-rotated-2026-07-02.md`; the M3.7/M4-era blocks rotated 2026-06-12 → `context/status/archive/PROJECT_SNAPSHOT-priors-rotated-2026-06-12.md` (git-object-sourced from `58794d7`)._

## Design Documents

All 14 design documents are Locked (Phase 1 — System Design Documentation is complete).

| # | Document | Status |
|---|----------|--------|
| 01 | Event Model & Event Bus | Locked |
| 02 | Device Model & Capability System | Locked |
| 03 | State Store & State Projection | Locked |
| 04 | Persistence Layer | Locked |
| 05 | Integration Runtime | Locked |
| 06 | Configuration System | Locked |
| 07 | Automation Engine | Locked + AMD-25 integrated (2026-03-18) |
| 08 | Zigbee Adapter | Locked |
| 09 | REST API | Locked |
| 10 | WebSocket API | Locked |
| 11 | Observability & Debugging | Locked |
| 12 | Startup, Lifecycle & Shutdown | Locked |
| 13 | Web UI (Observability MVP) | Locked |
| 14 | Master Architecture Document | Locked |

**Post-foundational design docs (Locked outside the original 14):** **Doc 15** — Cryptographic Architecture (Locked 2026-06-07; AMD-94 folded 2026-06-19). **Doc 16** — Superior Automation Layer (**Locked 2026-06-20**; INV-SA-01..04 registered as §49 of the invariants register; clears the M7.2b entry-gate).

## Committed M3 Design Artifacts (informational)

| Artifact | Path | Date | Notes |
|---|---|---|---|
| Cross-tier deployment audit | `nexsys-hivemind/context/audits/2026-05-19_cross-tier-deployment-audit.md` | 2026-05-19 | Closed-out audit of cross-tier deployment surface. Informed M3.6 composition root design. |
| M3 audit gap-closure research (Artifact 1) | `homesynapse-core-docs/research/2026-05-20_M3_Audit_Gap_Closure_v1.md` | 2026-05-20 | Identified and closed audit-trail gaps prior to M3.4b/M3.6. |
| M3.6 Composition Root Design | `homesynapse-core-docs/design/2026-05-20_M3.6_Composition_Root_Design.md` | 2026-05-20 | Authoritative composition-root design that M3.6 implements against. |

## Interface Specifications (Phase 2 — FROZEN)

Phase 2 completed 2026-03-20 with all 16 JPMS-compiled subsystem modules specified (plus 3 scaffold modules — platform-systemd, test-support, dashboard — that have MODULE_CONTEXT.md placeholders but no compiled Java yet). See `context/planning/phase-2-block-backlog.md` for the frozen historical record of Blocks A–S. Summary at Phase 2 close: 16 modules specified, ~402 production Java files, all module-info.java files compile clean with `-Xlint:all -Werror`. AMD-33 subsequently (2026-04-10) ratified DomainEvent as permanently non-sealed.

## M3 Governance (committed 2026-05-16)

| Amendment | Status | Scope |
|---|---|---|
| AMD-41 | APPLIED | State Projection Execution Model |
| AMD-42 | APPLIED | Subscriber Lifecycle and Isolation |
| AMD-43 | APPLIED | Backpressure and Observability |

13 new invariants: INV-BUS-01..03, INV-PROJ-01/04/NEW-01, INV-WRITER-01, INV-SUB-ISO-01..06. DEC-M3-01 through DEC-M3-17 locked (DEC-M3-14/15 added 2026-05-17; DEC-M3-16 added 2026-05-20 — composition-root visibility strategy; DEC-M3-17 added 2026-05-20 — HealthSignal + HealthLevel transitive visibility promotion alongside QueueSaturationHealthCheck, DEC-M3-16 addendum). PLAN-M3-CONSOLIDATED-02 committed as the M3 implementation authority.

## Phase 3 Implementation Status

Phase 3 began after Phase 2 closeout on 2026-03-20. Progress:

| Milestone / WU | Status | Date | Notes |
|---|---|---|---|
| M0 | COMPLETE | 2026-04-04 | AMD-31, traceability, MODULE_CONTEXTs |
| M1 | COMPLETE | ~2026-04-08 | Contract tests + in-memory implementations |
| M2 | COMPLETE | 2026-05-01 | Full persistence layer |
| M2-bridge | COMPLETE | 2026-05-02 | AMD-34–37, structural hardening |
| M3.1 | COMPLETE | 2026-05-17 | InProcessEventBus core (14 types) |
| M3.2 | COMPLETE | 2026-05-17 | REPLAY→TRANSITION→LIVE bus-side (16 types) — `0bade6a` |
| M3.3 | COMPLETE | 2026-05-17 | Backpressure, metrics, observability (29 types) — `a5d4b2a` |
| M3.5a | COMPLETE | 2026-05-18 | StateProjection vertical slice — `a2aff9c` |
| Bus-Fix Piece A | COMPLETE | 2026-05-18 | `DerivedWriteRateLimit` visibility promotion — `fceafe8` |
| M3.5b | COMPLETE | 2026-05-18 | StateProjection production persistence — `08d0136` |
| Projection-checkpoint wiring | COMPLETE | 2026-05-19 | `StateCheckpointSource` + 10 MB advisory guardrail — `56aaa4b` |
| Supervisor DLQ wiring | COMPLETE | 2026-05-19 | `SubscriberSupervisor` constructs `DeadLetter` — `ed5862c` |
| M3.4a | COMPLETE | 2026-05-19 | Integration-tests module + harness + BurstLoadIT + HeapBudgetIT — `5ae7912` |
| M3.4b | COMPLETE | 2026-05-19 | Sustained-load + crash-recovery IT tests — `adf04d2` |
| M3.6a | COMPLETE | 2026-05-20 | Profile-driven persistence config — DeploymentProfile 6 fields, LockingMode enum, profile-driven PRAGMAs — `17c40b6` |
| M3.6b | COMPLETE | 2026-05-20 | EventBusConfig record, InProcessEventBus public (DEC-M3-16), ReplayWindowQueue parameterized — `df2743a` |
| M3.6c | COMPLETE | 2026-05-20 | Per-module event-class manifests (Q3 gap closure) — `38d3e30` |
| M3.6d-a | COMPLETE | 2026-05-20 | Composition-root satellite changes — SqliteStateStore→StateCheckpointSource, QueueSaturationHealthCheck+HealthSignal+HealthLevel public (DEC-M3-17), ReadinessSource, ReconciliationTest 4/5, Tier 9 un-disabled, HomeSynapseConfig + SharedScheduler + ThrowingStateQueryService skeletons, SLF4J wiring — `25bc23b` |
| M3.6d-b | COMPLETE | 2026-05-21 | PersistenceFactory + HomeSynapseCore composition-root wiring — 4-commit cohort: WriteCoordinator.queueSize() (`a33ee40`), production SubscriberReadConnectionFactory (`a59b64e`), PersistenceFactory public gateway (`725353d`), HomeSynapseCore facade (`dfb045e`). OR-M3-14 prerequisites bundled. — `dfb045e` |
| M3.6e.1 | COMPLETE | 2026-05-22 | MaterializedStateQueryService + ReadinessFilter + RestFilters + Javalin bootstrap + DeploymentProfile thread pool sizing. 6 created, 13 modified. Two follow-up fix rounds (Xlint:exports gateway pattern, Gradle/JPMS scope alignment). 7 deviations (none blocking). Sixteenth CC WU. — `b71ed37` |
| M3.6e.2 | COMPLETE | 2026-05-22 | Admin endpoints (DlqStatusEndpoint, ProjectionStatusEndpoint) + entity query endpoints (ListEntitiesEndpoint, GetEntityEndpoint, GetEntityStateEndpoint) + EndpointContext SPI + 2 RestFilters gateway methods + 2 ArchUnit rules (QUERY_SERVICE_READ_ONLY, REST_ENDPOINTS_NO_EVENT_PUBLISHING) + HomeSynapseCore 16-step bootstrap. 15 created, 6 modified, 19 test methods. 5 deviations (none blocking). Seventeenth CC WU. M3.6 COMPLETE. — `76288af` |
| M3.7 | COMPLETE | 2026-05-27 | E2E integration tests + abandon() + checkpoint key fix + TESTING policy. M3 COMPLETE. |
| M4 scoping | COMPLETE | 2026-05-28 | PLAN-M4-CONSOLIDATED authored; canonical scope; KB de-poison applied. Next: M4.0a. |

## Code State

- **Repository:** homesynapse-core, **22 Gradle subprojects** (per `settings.gradle.kts`; source-verified 2026-06-13): ~16–17 JPMS-compiled production modules + 3 scaffold-only (platform-systemd, test-support, web-ui:dashboard) + `testing/integration-tests` (on-device ITs, classpath-only test code) + `spike:wal-validation` (throwaway spike — standing `git rm` advisory).
- **Production + test Java files:** **~803** (573 main + 230 test; +41 testFixtures ≈ 844) (source-verified 2026-06-13; supersedes the 724 count from 2026-05-28 — growth from M4.B/M4.C/M5-A/M6.1/M6.2/M6.4). Across the JPMS-compiled production modules (post-M3.6e.2 addition of `MaterializedStateQueryService`, `ReadinessFilter`, `RestFilters` in state-store/rest-api, plus `DeploymentProfile` thread-pool fields, `HomeSynapseCore` Javalin bootstrap wiring, `StateQueryService.materialized()` static factory). Test files: **~2,002 @Test/@ParameterizedTest/@RepeatedTest methods** (source-verified 2026-06-13; supersedes the 1,422 count from 2026-05-28) across ~173 test files and ~35+ testFixtures files (M3.6e.1 added: `MaterializedStateQueryServiceTest` (10 tests), `ReadinessFilterTest` (8 tests), `DeploymentProfileTest` (4 tests), `HomeSynapseCoreTest` stateQueryService test, `StateQueryServiceTest` updated assertion).
- **Event-bus module (post-M3.6d-a):** 19 public + 14 package-private = 33 top-level types. M3.6d-a promoted `QueueSaturationHealthCheck`, `HealthSignal`, `HealthLevel` to public (DEC-M3-17 — transitive 3-type chain because the public constructor's `Consumer<HealthSignal>` parameter would have triggered `-Xlint:exports` otherwise). M3.6b added `EventBusConfig` (public record, 2 fields: `replayQueueCapacity`, `publisherBlockedDepthThreshold`; `HOME_DEFAULT` constant). `InProcessEventBus` promoted to `public` (DEC-M3-16); new canonical 7-arg constructor accepting `EventBusConfig`. `PUBLISHER_BLOCKED_DEPTH_THRESHOLD` replaced by instance field from config. `ReplayWindowQueue` capacity parameterized (default 10,000 via no-arg; custom via `ReplayWindowQueue(int)`). `InProcessEventBusFactory` gained `createWithConfig(...)`. `EventBus` interface has 8 methods (4 abstract Phase 2, 4 default M3.1). `BusMetrics` interface (7 canonical metric names) with `BusMetricsJfr` JFR-native implementation.
- **Persistence module (post-M3.6d-b):** 48 types (was 45). M3.6d-b added `PersistenceFactory` (public final class — static `start()` factory, 8 store/infrastructure accessors returning public interface types, `AutoCloseable`), `SqliteSubscriberReadConnectionFactory` (package-private — production impl of `SubscriberReadConnectionFactory`, creates per-subscriber dedicated platform-thread executor + SQLite read connection; INV-SUB-ISO-02), `SqliteSubscriberReadExecutor` (package-private — per-subscriber read executor backed by a single platform thread and dedicated `Connection`; close() shuts down executor and connection). `WriteCoordinator` interface gained `int queueSize()` (DEC-M3-14); `PlatformThreadWriteCoordinator` implements it by exposing the bounded executor's queue size. `SqlitePersistenceLifecycle` expanded from 4-store to 6-store construction: now also constructs `SqliteStateStore` + `SqliteDeadLetterStore` during `start()`, with a separate `Include.ALWAYS`-configured `ObjectMapper` for `CheckpointSerializer` (distinct from the `NON_NULL` `PersistenceObjectMapper.create()` used for event payloads). New accessors: `stateStore()`, `deadLetterStore()`, `subscriberReadConnectionFactory()`. Module-info gained no new directives (all dependencies already present from M3.6d-a). `SqliteStateStore` now `implements StateCheckpointSource` (method renamed `serialize(int)` → `serializeCheckpoint(int)`, both `serializeCheckpoint` and `loadedProjectionVersion()` promoted to public via interface; class itself remains package-private — only the two interface methods are externally visible). M3.5b added `SqliteStateStore` (ConcurrentHashMap-backed materialized view + checkpoint-driven recovery), `SqliteDeadLetterStore` (UPSERT on (subscriber_id, event_position)), `CheckpointSerializer`, `CheckpointData`, `AtomicCheckpointWriter.writeAtomicCheckpointWithDlqPark()` (three-way atomic write — subscriber checkpoint + view checkpoint + DLQ park), V004 DLQ operational indices migration. Two ObjectMapper configurations coexist: `PersistenceObjectMapper.create()` returns `NON_NULL` for event payloads; checkpoint serialization requires `ALWAYS` and is constructed at composition time (composition-root wiring lands in M3.6d-b).
- **State-store module (post-M3.6e.1):** 20 public + 2 package-private types (M3.6e.1 added `MaterializedStateQueryService` — package-private final, backed by `StateStore`, recomputes stale at read time via injected `Clock`; `StateQueryService.materialized(StateStore, ReadinessSource, Clock, LongSupplier)` public static factory exposes construction surface per DEC-M3-16 pattern). `ReadinessSource` public interface (single method `mode() → SubscriberMode`). Projection-checkpoint wiring's `StateCheckpointSource` interface in scope. Advisory 10 MB checkpoint-size guardrail enforced.
- **Lifecycle module (post-M3.6e.2):** 8 public + 2 package-private types. M3.6e.2 expanded `HomeSynapseCore`: bootstrap sequence now 16 steps (14 from M3.6e.1 + 2 from M3.6e.2: entity query endpoint registration via `RestFilters.addEntityEndpoints` + admin endpoint registration via `RestFilters.installAdminEndpoints`). M3.6e.1 added steps 11-12 (added step 11: `MaterializedStateQueryService` wiring via `StateQueryService.materialized(stateStore, this, clock, () -> stateProjection.cursorPosition())`, step 12: Javalin server construction with `QueuedThreadPool(profile.javalinMaxThreads(), profile.javalinMinThreads())` + `RestFilters.installReadinessGate(app, this)` + `app.start(7070)`). `stateQueryService()` now returns the real `MaterializedStateQueryService` (replaces `ThrowingStateQueryService` placeholder). Module-info gained `requires com.homesynapse.api.rest`, `requires io.javalin`, `requires org.eclipse.jetty.util`. `DeploymentProfile` gained `javalinMinThreads()`/`javalinMaxThreads()` accessors for Javalin thread pool sizing: STUDIO(1/4), HOME(2/8), PERFORMANCE(4/16).
- **testing/integration-tests module (M3.4a + M3.4b):** Module #20. Tests gated on `-PpiProfile` (off by default; excluded from `./gradlew check`). Five IT tests: `BurstLoadIT`, `HeapBudgetIT` (M3.4a), `Pi4SustainedLoadIT`, `Pi4D1SpikeIT`, `CrashRecoveryIT` (M3.4b). `IntegrationTestHarness` composes `PersistenceTestHarness` + `InProcessEventBusFactory` against a real `@TempDir` SQLite file, with `startThrottled()` and `startForCrashSimulation()` factories (M3.4b). JVM constraints: `-Xmx256m -Xms256m -XX:ActiveProcessorCount=4 -XX:+UseG1GC -XX:MaxGCPauseMillis=100`.
- **MODULE_CONTEXT.md:** 20 files exist total — 17 populated substantively (including `testing/integration-tests` populated during WUCP Phase 2 reconciliation), 3 stubs (platform-systemd, dashboard, test-support). `core/event-bus/MODULE_CONTEXT.md` updated in M3.6b (EventBusConfig, InProcessEventBus public + 7-arg constructor, ReplayWindowQueue parameterized, InProcessEventBusFactory.createWithConfig). `core/persistence/MODULE_CONTEXT.md` updated in M3.6a (DeploymentProfile 3→6 fields, DatabaseExecutor accepts profile, LockingMode enum, PersistenceLifecycle Javadoc cleaned). `core/state-store/MODULE_CONTEXT.md` updated in projection-checkpoint wiring (added `StateCheckpointSource`, byte[0] stub deprecation note, projectionVersion authoritative source).
- **Rest-api module (post-M3.6e.2):** 28 Phase 2 public types + 2 M3.6e.1 types + 8 M3.6e.2 package-private types = 38 Java files. M3.6e.2 added `EndpointContext` (package-private SPI interface), `JavalinEndpointContext` (adapter), `EndpointResponses` (utility), `ListEntitiesEndpoint`, `GetEntityEndpoint`, `GetEntityStateEndpoint`, `DlqStatusEndpoint`, `ProjectionStatusEndpoint` (all package-private endpoint handlers). `RestFilters` gained 2 new public methods (`addEntityEndpoints`, `installAdminEndpoints`). M3.6e.1 added `ReadinessFilter` (package-private — implements `io.javalin.http.Handler`, 503 rejection with RFC 9457 problem detail body + `X-HomeSynapse-Projection-State` + `Retry-After: 5` headers) and `RestFilters` (public final utility — `installReadinessGate(Object javalinApp, ReadinessSource)` with deliberate `Object` typing to erase Javalin from the public API surface per DEC-M3-16). Module-info gained `requires transitive com.homesynapse.state`, `requires com.homesynapse.event.bus`, `requires io.javalin`, `requires org.slf4j`. Build.gradle.kts: `implementation` → `api` for state-store (fixes JPMS scope mismatch — websocket-api `requires transitive com.homesynapse.api.rest` needs state-store transitively visible). `ProblemType` enum gained `STATE_STORE_REPLAYING` (D-7).
- **Tests:** **~2,002** @Test methods total (source-verified 2026-06-13; supersedes 1,422 from 2026-05-28). Contract test suites: `EventStoreContractTest` (27), `EventBusContractTest` (50), `WriteCoordinatorContractTest` (11), `CheckpointStoreContractTest` (9), `ViewCheckpointStoreContractTest` (10), `DeadLetterStoreContractTest` (10). M3.6e.1 added `MaterializedStateQueryServiceTest` (10 — 4 staleness-recomputation, 3 snapshot variants, 1 unmodifiable-map, 1 view-position, 1 isReady-delegation), `ReadinessFilterTest` (8 — LIVE pass-through, 3 non-LIVE 503 with diagnostic headers, RFC 9457 body shape, mode-freshness), `DeploymentProfileTest` (4 — all 3 profiles + min≤max invariant), `StateQueryServiceTest` assertion updated to 6 methods (D-3 static factory). M3.6d-a added `ReconciliationTest` (4 of 5 methods — OR-M3-13) + `SharedSchedulerTest` (5). Prior: M3.5b added `AtomicCheckpointWriterDlqTest` (3), `CheckpointSerializerTest` (12+), `SqliteStateStoreTest` (12). Supervisor DLQ wiring added `SubscriberSupervisorTest` (12). M3.4a added `BurstLoadIT` + `HeapBudgetIT` (gated). M3.4b added `ThrottledWriteCoordinatorTest` (9) + `Pi4SustainedLoadIT` + `Pi4D1SpikeIT` + `CrashRecoveryIT` (gated).
- **Traceability:** 01-event-model.md (44 entries), 12-lifecycle.md (2 entries). Stub indexes remain for docs 02–11, 13, 14 — Phase 2 traceability debt carries into Phase 3.
- **Last build gate:** RESOLVED. Full `./gradlew check` GREEN (139 tasks) at HEAD `98f705b` on 2026-05-30 (M4.0b-3, AMD-51 typed comparator + `projectionVersion` 2→3; `:core:device-model:check` + `:core:state-store:check` + `:lifecycle:lifecycle:check` GREEN). Build confirmed by Nick. The `:testing:integration-tests:test -PpiProfile=throttled` run was not held to completion — `Pi4D1SpikeIT` is a fixed 30-min soak (not a hang), excluded from the default `check`, and AMD-51 does not touch the path it exercises; not a blocker. **No deferred build gates open.** Prior: `60b4185` M4.B3, `7610296` M4.0b-2 — both GREEN.

## Active Work

- **Last completed:** M3.6e.2 via Claude Code (2026-05-22, `76288af`). M3.6 COMPLETE — all seven sub-WUs shipped. Seventeen CC WUs total.
- **Next:** M3.7 scoping via research pipeline. E2E integration tests. Estimated Coder time: 6–8h.
- **Claude Code workflow validated:** acceptEdits mode, Opus 4.7 xhigh, deny git commit/push/gradlew. PM generates task instruction → Claude Code executes → Nick reviews git diff, runs build gate, commits. Through M3.6e.2, seventeen Claude Code WUs executed via this workflow. Bus-Fix Piece A and SLF4J follow-up patch were direct edits by Nick.

## Blocking Issues

None. No unresolved deferred build gates. All M3.6a through M3.6e.1 build gates GREEN at commit time.

## Open Risks

- **OR-M3-17 — FULLY CLOSED (M4.0b-1, 2026-05-29, `cf1a97e`).** The no-op `MINIMAL_DERIVATION_RULE` lambda (the M3.7 placeholder that closed the *symptom*) is now replaced by the production `ProductionDerivationRule` (package-private in `com.homesynapse.state`, reached via `DerivationRule.production()`), which publishes a real `state_changed` on a canonical-attribute change. Real derivation has shipped per DEC-M3-10 + REC-28.
- **OR-M3-18 — FULLY CLOSED (M4.0b-1, 2026-05-29, `cf1a97e`).** The `MinimalProjectionAdvancer` placeholder is removed and replaced by `DispatchingProjectionAdvancer` (REC-28 — package-private, constructor-injected `EnvelopeHandler` map, no `ServiceLoader`, forward-all with exact cursor parity). The advancer class file was deleted from `lifecycle`.
- **OR-M3-12 — DEC-M3-17 governance entry (NEW 2026-05-20):** RESOLVED in this WUCP Phase 2 closeout. HealthSignal + HealthLevel public promotion alongside QueueSaturationHealthCheck logged as DEC-M3-17; entries appended to Current_State §3 ledger, Locked_Decisions Phase 3 milestone section, and `context/decisions/phase-3-cross-module-decisions.md`. No further action.
- **OR-M3-13 — ReconciliationRecordsMetadataInDataSlot — RESOLVED (M4.0a, 2026-05-29, `a441fdf`).** Reconciliation metadata (`reconciledAt`/`reconciledFromVersion`/`reconciledToVersion`) is now populated via the extended `StateCheckpointSource.serializeCheckpoint(...)` surface, threaded through `StateProjection.initialize()`'s version-mismatch reconciliation branch; `SqliteStateStore` writes the values instead of `null`. `ReconciliationTest`'s deferred 5th method (`reconciliationRecordsMetadataInDataSlot`) is un-deferred and passing — it asserts `reconciledToVersion == 2`, the value M4.0b's backfill gate binds to. AMD-41 §3.2.4's metadata-recording requirement is now met.
- **OR-M3-14 — M3.6d-b prerequisite infrastructure (NEW 2026-05-20):** RESOLVED 2026-05-21. All three prerequisite pieces shipped in the M3.6d-b 4-commit cohort: (1) `WriteCoordinator.queueSize()` at `a33ee40`; (2) production `SqliteSubscriberReadConnectionFactory` at `a59b64e`; (3) `SqlitePersistenceLifecycle` 6-store expansion + `PersistenceFactory` public gateway at `725353d`. `HomeSynapseCore` composition root completed at `dfb045e`. Build GREEN.

## Tracked Gaps (carry forward)

1. **Tier 9 `reconciliationOnVersionMismatch` test still `@Disabled("M3.5a")`** — re-enablement was split out of Bus-Fix Piece A. Now tracked under M3.6 lifecycle wiring (depends on `bus.resume()` VT re-spawn fix).
2. **`bus.resume()` does not re-spawn VT** — pre-existing M3.1 limitation; deferred to M3.6 lifecycle wiring.
3. **Overflow test slow (~5-15s)** — consider `@Tag("slow")` if suite time grows.
4. **JFR-native emission is accepted design debt** — pull-based metrics consumer (Prometheus/OTLP) will need typed adapter layer in M4+.
5. **Publish-latency metric is bus-side only** — end-to-end publish latency is a persistence-module metric for future observability pass.
6. **`lagEvents` approximation** — uses `pendingPositions.size()` instead of writer-tail-minus-delivered-position. To be revisited under M3.4b Pi4SustainedLoadIT if accuracy proves insufficient.
7. ~~**Composition root for ALWAYS-configured ObjectMapper**~~ — **CLOSED (M3.6d-b `725353d`).** `SqlitePersistenceLifecycle.start()` now constructs a separate `ALWAYS`-configured `ObjectMapper` for `CheckpointSerializer`, distinct from `PersistenceObjectMapper.create()` (`NON_NULL`). Wired through `PersistenceFactory`.
8. ~~**`QueueSaturationHealthCheck` and `DerivedWriteRateLimit` lifecycle wiring deferred**~~ — **CLOSED (M3.6d-b `dfb045e`).** `HomeSynapseCore.start()` constructs both and passes them to `SharedScheduler`.
9. ~~**`DerivedWriteRateLimit.refill()` externally called**~~ — **CLOSED (M3.6d-b `dfb045e`).** `SharedScheduler` calls `refill()` every 50 ms via `safelyInvoke(rateLimit::refill)`.
10. ~~**Defence-in-depth `IllegalStateException` for `EventPublisher.publish()` from REPLAY**~~ — **CLOSED (M3.6d-b `dfb045e`).** `HomeSynapseCore` subscribes the projection with `SubscriptionFilter.all()` + `coalesceExempt=true`; the bus's mode FSM prevents publish calls during REPLAY. The composition root wiring itself is the defence.
11. **Post-shutdown defensive handling in stores** — `SqliteDeadLetterStore` (and siblings) will throw uncaught exceptions if methods are called after `DatabaseExecutor.shutdown()`. Pre-existing pattern, not an M3.5b regression. Track for a future hardening pass.
12. ~~**`AtomicCheckpointWriter` code duplication**~~ — **CLOSED (M4.0a / H2, `a441fdf`).** Shared `executeInTransaction(context, work)` helper extracted; both `writeAtomicCheckpoint` and `writeAtomicCheckpointWithDlqPark` route through it.

## Schedule Position

**Significantly ahead of Master Release Plan.** The 37-week plan placed Weeks 1–10 as "Interface Specification" — the project finished that work in 7 days (Mar 14–20). Phase 3 persistence subsystem (M2.x) complete. Event bus production implementation with full REPLAY→LIVE algorithm + backpressure + persistent DLQ + state projection + integration tests (including sustained-load and crash-recovery) all landed in the M3.1–M3.4b window (May 16–19). See the Phase 3 Progress Annotation in `master-release-plan.md` for actual vs planned dates.

## Next on Critical Path

1. **M4 next-part scope/plan** (fresh Cowork conversation) — formally define the scope of the next M4 segment: **Workstream B** device-model breadth (AMD-44 Floor/EntityRole impl, Research 8 REC-23–30) and **Workstream C** integration-api interface freeze (Research 6 REC-41–51, P3-gated on Nick's NQ-1..6), plus the **AMD-52** typed-`StateChangedEvent` serializer/replay design beat (OQ-05-08). Surface deep-research needs (e.g. Axon and other event-sourced platforms) to de-risk scale/maintainability — grounded in concrete forward design questions, not invented problems.
2. ~~**AMD-51 §2.6 erratum**~~ — **DONE 2026-05-31** (docs repo). The missing-schema → `StringValue` string-compare fallback (M4.0b-3 D-1) is recorded as the ratified no-schema behaviour in AMD-51 §2.6; the amendment now matches shipped code. (Commit pending with the docs-repo warm-up batch.) Also DONE: the KB doc-currency punch-list (0a-ii) — `HomeSynapse_Current_State`/`Knowledge_Primer`/`Navigation_Index`/`Decisions_Quick_Reference` brought current to `98f705b`/`projectionVersion` 3/watermark AMD-51.
3. **Phase 2 traceability debt** — 10 stub indexes remain (docs 02–11, 13, 14); state-store/device-model M4.0b-3 entries also pending. Low priority; batch later.

## Recent Session Log

| Date | Agent | What Happened |
|------|-------|---------------|
| 2026-06-26 (v7 beat 12 — §3 decisions ruled + governance closed + M7.4a issued) | PM (Cowork) + Nick | **§3 CONSOLIDATED DECISION PASS: 12 decisions, Nick co-signed all four groups as recommended.** Folded on disk (pending Nick's commit): **AMD-95 RATIFIED** (Doc 07 §3.11 reconciled + AMD-90 §11; watermark 94→95); **Doc 17 LOCKED + AIOT-INV-1 minted** (INV-AC §50; 170/50; AIOT-INV-2/3 principles); **Wave-1 reconciliation record + AMD-96 PROPOSED** (Doc 02/08 currency: White/CT, Kelvin-canonical, EZSP-v14, occupancy binding); **lane-integration note** (C8 `name` field folded into v1.1; C9 Doc 13 currency; C10 CI drops=Nick; C11 E2 bind-host Core WU ahead of M9 wizard +E1/E3/E6; C12 doctrine shared-home); **M7.4a ISSUE-READY** (producer + co-located dispatch subscriber + paired teardown). D-07-A deferred to M8. Nick's next: commit + the 2 CI drops + route M7.4a. |
| 2026-06-26 (v7 hub launch + preflight reconcile) | PM (Cowork) | **v7 mission-control hub LAUNCHED (supersedes the token-heavy v6).** Ground: env-model → V1 record + v6 forward plan + §1 record → 11-check preflight = **STALE-benign, zero CONFLICTED** (Checks 1/3 snapshot currency-lag behind beats 8-11; Check 8 cross-agent-note archival; **Check 9 PASS** — mirrors byte-identical). Baselines CONFIRMED (core `b296e76` / docs `f54d0e0` / hivemind `cd8b046` = the masthead's "+ beat-11 reconcile + v7 land on top"). Reconciled this snapshot (masthead/Latest-commits/this row + the v7-launch top note) + archived the resolved M7.3/M7.2b cross-agent notes → PASS. **Next (the v7 hub's first substantive act): the §3 consolidated decision pass (12 decisions, Nick rules) → governance close-out → M7.4a.** Flagged the harmless 0-byte `nexsys-hivemind/.git/index.lock.cleared-by-cowork-2026-06-26` leftover (no active lock anywhere; Nick deletes at leisure). |
| 2026-06-26 (beat 11 — Track-A first returns + decisions consolidated) | PM (Cowork v6) | **The development fleet's first beat returned** (all write-isolated; spine untouched). Frontend-dev: buildable Preact+TS SPA (`web-ui/dashboard/`, 65 files), both hero halves over the frozen v1.1 contract, mock seam, 1-2s polling, verified GREEN. Distribution: the one-command-install skeleton (`distribution/`, 23 files) — jlink→systemd→`.deb`/`install.sh`→container install-smoke = mid-Aug gate #4; escalations E1-E8. Bench Session C: device-corpus knowledge layer + verdicts + MG24/EZSP-v14 fingerprint — **PHYSICAL CAPTURE PENDING (Nick's desk)**; escalations ESC-W1-HUE-01/COORD-01/SNZB03P-01. Consolidated decision set assembled → the v7 prompt §3. |

_Older session-log rows (2026-06-04 → 2026-06-07 era, 30 rows) rotated 2026-07-02 → the archive file above; the masthead beats are the session record from 2026-06-21 onward._
