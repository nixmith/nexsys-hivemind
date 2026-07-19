<!--
file: context/programs/matter-design/dispatches/2026-07-19_A1_stack-survey_lane_prompt.md
purpose: Dispatch prompt for research lane A1 — the honest state of Matter controller implementations reachable from a Java 21 JPMS local-first system.
audience: a fresh write-isolated Cowork research lane (NOT the PM hub; do not load the PM skill).
state-type: session prompt (lane dispatch).
status: READY — authored 2026-07-19 by the Matter design-program hub (launch beat 1).
-->

# Lane A1 — Matter Stack Survey (evidence dossier; options, no winner)

You are a **write-isolated research lane** of the Matter/Integrations Design Program (charter: `nexsys-hivemind/context/handoff/2026-07-19_matter-design-program_hub_session_prompt.md`; ruled by Nick 2026-07-19). Your job: the honest, evidence-cited state of every route by which a **Java 21 JPMS, local-first, event-sourced** system can act as a Matter controller. You produce an options dossier. **You do not pick a winner** — the fit-walk is lane A3's, the choice is Nick's ruling at memo B1.

**WRITE ISOLATION (ABSOLUTE):** you produce exactly ONE file: `nexsys-hivemind/context/programs/matter-design/returns/A1_stack-survey_return.md`. No other writes anywhere — not the spine, not core/docs/bench/skills, not other program files. All repo reads are read-only.

**EVIDENCE DISCIPLINE (a two-layer hub audit will adjudicate every claim):** tag every load-bearing claim `[VERIFIED-current: URL, fetched YYYY-MM-DD]` · `[community-reported: URL]` · `[inference — reasoning stated]` · `[banked: repo-path §]`. Quotes are evidence; labels are claims — quote version strings, license texts, deprecation notices, and release dates verbatim from primary sources. Every number re-derivable. An honest "could not verify" outranks a confident guess. No vibes.

## Baseline (banked — build on it, don't re-derive; ↻ = re-verify currency, the base was fetched 2026-07-10)

`context/assessments/2026-07-11_integration-roadmap_research-return.md` §3.4 + §7.1 banked: **python-matter-server DEPRECATED** (final v8.1.2, 2025-12-15 — "rewritten and moved to matterjs-server!") · **matterjs-server** = the Open Home Foundation successor (Apache-2.0, WebSocket API, Beta as of June 2026, HA 2026.6 ships on it; teething issues #164/#694 on record) ↻ · **connectedhomeip** C++ SDK (Apache-2.0) has official Java controller bindings (`examples/java-matter-controller`, desktop-Linux) but no known shipped headless JVM product uses them; openHAB evaluated the Java SDK path and chose matter.js + a Node sidecar (auto-downloading Node 22) instead ↻ · **pure Java: none** (one experimental 2-commit GraalVM matter.js runtime, `digitaldan/matter.js-java`) ↻ · licenses per §7.1 (CHIP Apache-2.0 · matter.js/matterjs-server Apache-2.0).

**Baseline shift since the banked base:** Nick's 2026-07-19 ruling upgraded the "winter arc" posture to a **full design program NOW** (code still gated post-sweep + post-Lock) — so this survey is no longer "cheap insurance for January"; it is the evidence floor for a ratification-grade design. Depth accordingly: primary sources, release histories, issue-tracker hygiene, not blog summaries.

## Required reads (before searching)

1. The program charter (path above) — your fences.
2. The roadmap return §3 + §7.1 (the banked base you extend).
3. `context/process/2026-07-18_compounding-testing-doctrine.md` — the testing culture your evidence feeds.
4. `homesynapse-core-docs/design/18-extension-and-plugin-architecture.md` §3.3 + §7 DP-18-B — the IN_JVM / RESERVED_SUBPROCESS posture your options will be judged against (context only; the judging is A3's).

## The questions (answer all; number your sections to match)

1. **connectedhomeip SDK, today:** current release/tagging model and spec-version coverage; the **Java controller bindings** — what they actually are (JNI surface, build chain GN/ninja, artifact/binary size, platform coverage incl. linux-arm64), how buildable outside the CHIP tree, and the maintenance cost of tracking upstream (release cadence, breaking-change history). Name any shipped headless-JVM product using them (or state none found, with search trail). Verify the openHAB decision record ↻ and quote their stated reasons.
2. **In-process embedding from Java 21:** the honest JNI-vs-FFM picture. Our core is **Java 21** (FFM is preview in 21, final in 22+) — state the JDK-version interaction explicitly and what each route would demand (native artifact packaging per-arch, JPMS native-library loading, crash blast-radius of C++ in our JVM process). Evidence-level, not design.
3. **matter.js / matterjs-server, today ↻:** maturity since the June-2026 Beta — controller feature coverage (commissioning paths incl. BLE, subscriptions, bridge handling, OTA, fabric management), the WebSocket API surface (enumerate the actual API: commands, events, state model — this becomes the IPC-seam evidence A3 consumes), release cadence, open-issue hygiene (the #164/#694 class — resolved?), Node runtime requirements on a Pi (version, RAM/disk footprint), supply-chain posture (dependency count, signing/provenance).
4. **python-matter-server:** confirm the deprecation stands ↻; one paragraph; the HA-legacy note only.
5. **Pure Java, scope honesty:** what a from-scratch Java Matter controller stack actually entails — protocol crypto (PASE/SPAKE2+, CASE/SIGMA), TLV + interaction model, mDNS/DNS-SD, the cluster library breadth, cert/attestation handling, and the conformance surface. State the honest arc-scale in M9-arc units (the Zigbee arc = 14 WUs on a far smaller protocol — `[banked: roadmap return §6.3]`). The `digitaldan` experiment's current state ↻. This option must be priced honestly, not dismissed rhetorically.
6. **The sidecar shape (evidence for A3, not a recommendation):** for matterjs-server specifically — process lifecycle (how HA supervises it, restart/crash behavior, storage/state files it owns and their sensitivity), what the WS seam exposes vs what a controller needs, version-coupling between server and client, and packaging reality on Pi-class hardware (install methods, disk/RAM, Node LTS lifecycle). Name what breaks when the sidecar dies mid-command (evidence from issues/docs, not speculation).
7. **Licenses, re-verified at LICENSE files ↻:** CHIP, matter.js, matterjs-server, and any transitive runtime you'd ship (Node itself). Confirm nothing forces copyleft onto an Apache-2.0 core under each option.
8. **Spec versioning:** how each stack tracks Matter 1.4/1.5/1.6 (what "supports Matter 1.x" means for a *controller*), the certification-blob/PAA trust-store update channel, and the cadence mismatch hazard (controllers lagging devices, banked §3.1 ↻).

## Known hazards

- The Matter ecosystem is marketing-dense: prefer repos, LICENSE files, release pages, and issue trackers over vendor blogs; date every fetch.
- "Supports Matter" claims rarely distinguish device-side from controller-side — always state which side a claim is about.
- The banked base is nine days old; anything ↻ must carry a fresh fetch date even if unchanged.

## NOT in scope (fences)

No winner, no design, no code, no core writes. Not gate work — J1 is FROZEN and criteria-draft §2 fences Matter out of the mid-Aug gate; nothing you write may imply otherwise. Hardware/DUTs are lane A2's; invariant fit-walking is A3's; the honesty-moat mapping is A4's; certification economics are A5's (you only pin licenses).

## Return format

`§0` executive digest (≤1 page, one-turn-readable) → `§1–§8` matching the questions, evidence-tagged → `§9` **option cards** (a: matterjs-server sidecar · b: CHIP-JNI in-process · c: CHIP-FFM in-process · d: pure Java — per card: maturity, controller coverage, maintenance load, runtime cost, license, spec-tracking, unknowns; NO ranking) → `§10` open questions for the design phase, each marked BLOCKING / NON-BLOCKING → `§11` honest gaps (what you could not verify and why).

**Done-when:** the single return file exists at the exact path above, self-contained, every load-bearing claim tagged and dated, option cards symmetrical (no strawmen), RECs absent by design (this lane recommends nothing).
