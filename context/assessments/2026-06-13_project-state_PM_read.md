<!--
file: context/assessments/2026-06-13_project-state_PM_read.md
purpose: PM state-of-the-project read (Nick re-entry + input to the 2026-06-14 W25-rollover converge session). Source-verified across the three repos. READ-ONLY analysis — does NOT touch the governance spine; the masthead reconciliation it flags is the converge session's job.
audience: Nick, PM
state-type: assessment (point-in-time read)
status: DELIVERED 2026-06-13
-->

# Project State — PM Read (2026-06-13)

**Scope:** HomeSynapse Core (`homesynapse-core`), the hivemind (`nexsys-hivemind`), and the design corpus (`homesynapse-core-docs`). Source-verified, not copied from the snapshot. Freshness preflight run as part of this read.

---

## Freshness verdict: STALE (presentation-layer only; binding governance is correct)

Two checks flag STALE; the rest pass.

- **Check 9 (skill mirrors): STALE — expected.** The known post-edit/pre-sync state the project tolerates; clears on Nick's next mirror sync.
- **Check 11 (currency): STALE — the real finding.** The `PROJECT_SNAPSHOT.md` "Current state" line and the `pm-handoff.md` masthead still narrate **watermark AMD-87 / "B2 C8/C9 PROPOSED" / "fold aborted."** That is contradicted by ground truth in the docs repo: **AMD-88..93 and B2 C8/C9 are all RATIFIED (2026-06-12), watermark 93, invariants 163/47, AMD-04 superseded by AMD-91** — confirmed in the AMD files' own status lines, `Architecture_Invariants_v1.md` (line 1066: "Total: 163 invariants across 47 categories … AMD-88..93 ratified 2026-06-12"), the cross-agent-notes "watermark 93" pointer, and the snapshot's *own* "Next action" line ("re-upload the 5 spine files … they now read RATIFIED/163-47/watermark-93"). The snapshot is therefore internally inconsistent (87 in one line, 93-spine in another). Secondary currency lag: the snapshot's code counts (724 files / 1,422 tests) are copied-forward from 2026-05-28 and now understate source by a lot (see below).

**Interpretation:** this is a stale-masthead residual, not a real ambiguity about what's true. The binding artifacts — the ratified AMD files, the invariants register, the Locked design docs, the code — are all correct and committed. The drift is confined to two hivemind state-doc summary lines that weren't swept when the ratification folded (most likely the 2026-06-12 hot-path rotation rewound the masthead after the ratification closeout). **Per CONFLICTED-handling discipline I have NOT edited the spine.** The reconciliation is already scheduled: `2026-06-14_W25-rollover_W26-scoping_synthesis_session_prompt.md` explicitly owns the masthead reconciliation and three-lane synthesis. Recommend it run as planned and correct the watermark-87 / C8-C9-PROPOSED lines and refresh the code counts.

---

## Where the project actually is

**Phase 3 (test-first implementation), at the M6 → M7 boundary.** (Note: the PM skill's "M5 window" framing is itself stale — verified 2026-06-07; the project has moved on.)

- **Design (Phase 1): COMPLETE.** All 14 design docs Locked + Doc 15 (Cryptographic Architecture) Locked. Amendment watermark **AMD-93**; **163 invariants / 47 categories**.
- **Interface specs (Phase 2): FROZEN** (2026-03-20; all production modules' interfaces compiled clean under `-Xlint:all -Werror`).
- **M0–M5-A: COMPLETE.** Foundation, persistence, event-bus, state-projection, composition root, M4 device-model expansion + integration-api freeze (AMD-54..64), M5-A platform-systemd + Expectation codec.
- **M6 (Configuration): 3-of-4 COMPLETE.** M6.1 (YAML pipeline + JSON-Schema validation), M6.2 (SecretStore + per-scope key management, HKDF, AES-256-GCM DEK/KEK), M6.4 (hot-reload atomic swap + write path) all committed, full `./gradlew check` GREEN. **M6.3 (at-rest payload encryption) is the open piece — triple-gated** (see critical path).
- **M7 (Automation): entry-gate open, contracts ratified.** AMD-88..93 are RATIFIED and now the binding contract shapes for all M7.x work (TriggerDefinition, Selector/SemanticTag/IncludedRoles, ActionDefinition, RunCausalChain-supersedes-AMD-04, automation event vocabulary, schema posture). Entry-gate rows 1–2+5 closed; rows 3 (interview half) and 4 (M5-C approve) remain.

**Build & tree state (source-verified today):**
- Core HEAD `824d6ba` (substantive code HEAD `7c73c91` M6.2; `824d6ba`/`01841ba`/`e5ea76f` are scripts/docs-only). **Working tree CLEAN.** Build GREEN (`./gradlew check`, 147 tasks: ArchUnit + spotless + moduleGraphAssert). No open deferred build gates.
- **22 Gradle subprojects** (≈17 JPMS-compiled production modules + `platform-systemd`/`test-support`/`web-ui:dashboard` scaffold stubs + `testing:integration-tests` on-device ITs + `spike:wal-validation` throwaway).
- **~573 main Java files + ~230 test + ~41 testFixtures; ~2,002 test methods** (vs the snapshot's stale 724/1,422). `projectionVersion` 5.
- Docs HEAD `8002b7e` (2 uncommitted: `website/README.md` modified + `website/design-system/` untracked — the brand-lane import). Hivemind HEAD `5e4943a` (5 uncommitted: the W25 prompt + this session's brand/naming/state assessments + the draft-rulings). These are parallel-lane artifacts awaiting Nick's host-git commit — not drift.

---

## Critical path & the bottleneck

The constraint has been **Nick's review/ratification + hardware/interview load, not agent output** — authoring/implementation outruns the gate. Right now:

1. **THE BOTTLENECK: the energy/erasure interviews** (institutional buyers — Grid/Assure/Care). Unscheduled for a **third consecutive week**. They are the **sole open evidence gate for M6.3** *and* the deciding input for the **M6.3-vs-M7 ordering call** at the W25/W26 boundary. The microbench half (OQ-15-2) resolved 5 days early — `encrypted_scopes` confirmed `[identity, presence_personal]` — so interviews are the only thing left on row 3. A third slip makes the ordering call undecidable, which would idle Core. Calendar-bound; **Nick's to schedule** — highest-leverage unblock.
2. **M5-C Increment 1 awaits Nick's APPROVE** of `homesynapse-core-docs/website/pages/config-superiority.md`. That approve flips M7 entry-gate row 4 and lifts the "no new Core instruction" floor. *(Caveat: this is the website/copy lane, now entangled with the rename — the page was drafted name-light per W-11, so approve is still possible, but you may prefer to hold website copy until product-naming settles. Flagging the interaction, not forcing it.)*
3. **Next Core code WU is M6.3** — instruction is ready to author the moment interviews land + the ordering call is made. It carries the confirmed encrypted set, **OR-M6-NONCE** (counter-nonce crash/restore monotonicity — a cryptographic-correctness blocker), and the cold-start cipher-warmup beat. After that, **M7.1** unblocks once rows 3+4 close.

Two open risks tracked, both correctly parked: **OR-M6-NONCE** (rides the M6.3 instruction) and **OR-M13-SDNOTIFY** (sd_notify transport deferred to M13; decision matrix authored, gated on the GraalVM spike + WatchdogSec call).

---

## The runway reality (the thing worth keeping in view)

Launch target **Nov 25, 2026 — ~165 days out.** Per the 2026-05-31 re-baseline, the honest read is unchanged and important:

**Core is healthy and on/ahead of its own axis** (foundation ran weeks early; remaining M6.3 → M7/M8 → M9 → M10/M11 → M12/M13 → M14 Zigbee → M15 validation realistically runs into ~October). **The schedule risk is not Core — it's the three non-Core tracks, which are at or near zero:**
- **Web UI** (`homesynapse-ui`) — does not exist. Long pole; API-gated (M10/M11, ~Aug) but design/scaffold-startable now.
- **Website + public docs** — only the internal design-doc repo exists; no public site. Startable now (the M5-C work is the first toe in this water). **This is where the brand/naming work reconnects** — and why the rename clearance is on the real critical path, not a side quest.
- **Distribution/installer** — does not exist; needs Core booting end-to-end (~post-M13, Sep).

A single developer + agents has been an effectively-serial pipeline pointed almost entirely at Core. The structural mitigation already adopted is the **M5-C non-preemptable floor** (P6) — website/docs work is not tradeable to accelerate Core. The re-baseline's forcing question still stands: non-Core has to interleave into the weekly cadence soon, or late-Nov absorbs the risk, or MVP scope gets cut.

---

## To regain Core focus — the re-entry checklist

1. **Schedule the energy/erasure interviews.** Single highest-leverage action; unblocks M6.3 and the ordering call. Everything Core waits behind this.
2. **Make (or defer) the M5-C row-4 approve** on `config-superiority.md` — quick, lifts the new-Core-instruction floor. Defer only if you'd rather freeze website copy until the product name lands.
3. **Run the 2026-06-14 W25-rollover converge session** as planned — it flips W24→COMPLETE, scopes W26, makes the M6.3-vs-M7 ordering call, and (importantly) **reconciles the stale masthead** (watermark 87→93, B2 C8/C9 PROPOSED→RATIFIED, refresh the 724/1,422 counts to ~803/~2,002).
4. **Host-git commit the parallel-lane artifacts** (docs `website/` changes; hivemind assessments + draft-rulings) so the working trees are clean before Core resumes.
5. **Then issue M6.3** (or M7.1, per the ordering call). Contracts are ratified; the path is clear.

**One-line status:** Core is in strong shape (M6 nearly done, M7 contracts ratified, build green, tree clean); the only things standing between here and the next Core milestone are an interview you need to schedule and a one-click copy approval — plus a stale governance masthead that the already-scheduled converge session will fix.
