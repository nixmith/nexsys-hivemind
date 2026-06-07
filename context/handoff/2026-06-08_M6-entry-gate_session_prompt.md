<!--
file: context/handoff/2026-06-08_M6-entry-gate_session_prompt.md
purpose: Cowork session-kickoff prompt — Monday 2026-06-08, W24. Opens the week on the M6 entry-gate (W24 Lanes 1+2): author the M6 config amendments + charter M6 multi-piece + draft the gated M6.1 instruction, with the B2 schema decisions riding alongside. Doubles, later, as the OQ-15-2 / AMD-86-§3 writeback session when Nick brings microbench numbers or interview results.
audience: PM (Cowork), Nick
-->

You are resuming as PM on NexSys / HomeSynapse Core. **Invoke the `nexsys-project-manager` skill and run the mandatory session-start freshness preflight before anything else.** Source-verify everything with the Read tool against the actual repos (`homesynapse-core`, `homesynapse-core-docs`, `nexsys-hivemind`); the in-sandbox git is not authoritative and commits go through host git. Read `pm-handoff.md` and `PROJECT_SNAPSHOT.md` for the authoritative state — do not work from any summary alone.

**Current state to internalize first (expect preflight PASS at HEAD `7f44bed`):**
- **M5-A COMPLETE** (Parts 1+2+3). Part 2 — the **AMD-87 `Expectation` persisted codec** — is **COMMITTED `7f44bed`** (full `./gradlew check` GREEN, 147 tasks; PM WUCP Phase 2 → APPROVE; 3 `[INFO]` accepted). **The M9 command-bearing-`CapabilityAdded` prerequisite is CLEARED.**
- **M5-B/B1 DONE** — **Doc 15 (Cryptographic Architecture) is LOCKED**; **AMD-86** (INV-PD-07 narrow + INV-PD-03 at-rest posture) and **AMD-87** RATIFIED; on-disk amendment watermark **AMD-87**; `projectionVersion` 5.
- **M5-D** — the three evidence artifacts are **AUTHORED + independently reviewed (RATIFY-grade)** and live in `context/assessments/2026-06-07_M5-D_*`: the **Pi-4 AES-GCM microbench spec** (resolves **OQ-15-2**), the **energy/erasure interview guide** (carries the **AMD-86 §3** verifiable-erasure re-scope-up trigger), and the **sd_notify decision matrix** (OR-M13-SDNOTIFY). They await Nick to **run** (the Pi-4 bench, the interviews, the GraalVM/GenZGC spikes).
- **The week's plan:** `context/planning/weeks/2026-W24_jun08-jun14.md` (re-cut 2026-06-07 EOD) frames W24 as **"M5-window closeout + M6 entry-gate close & kickoff."**

**Open Risks of interest:** **OR-M6-NONCE** (counter-nonce crash/restore durability, [BLOCKING-for-M6-impl]) and **OR-M13-SDNOTIFY** (sd_notify transport → M13).

---

**This session's task — the M6 entry-gate (W24 Lanes 1 + 2), leverage-ordered to Nick's gate.** The M6 entry-gate is **half-closed**: the crypto side (Doc 15 + AMD-86) landed with M5-B/B1. This session closes the **config-amendment side** and **charters + kicks off M6**. Reason through each against source; do not invent numbers or problems.

1. **Author the M6 config amendments — PRIORITY (the gate-closer).** Author **AMD-66–71** (the M6 configuration block; **Research 5**, PM-assessed A−) **+ the Doc 06 `SecretStore.setAll(Map)` atomic-multi-key-durable-write currency amendment** (the requirement Doc 15 §7.3 places on Doc 06 beneath AMD-60's `CredentialRotator.rotate(Map)`). Assign AMD numbers at authoring per P2. **Confirm at authoring** that AMD-67's REC-41 blocker stays cleared by the M4.C config-schema-versioning freeze (the next-piece rec flagged this — verify against source). Produce the **DOCS-Project review prompt** for the block (these freeze config/secret contracts → full review discipline, not just P4 for the load-bearing ones). → Nick dispatches the review + ratifies.

2. **Charter M6 as MULTIPLE first-class pieces (P1) + draft the gated M6.1.** M6 is **large** (config pipeline + secret store + per-scope key-management + at-rest encryption + hot-reload) — **do NOT let it discover its size in arrears as M4 did.** Charter it as first-class lane pieces, each with a backlog row + done-when:
   - **M6.1 — config pipeline:** YAML loading, JSON-Schema validation, `ConfigurationAccess` / `ConfigurationProvider` impls, on `PlatformPaths.configDir()` (M5-A). **Not crypto-gated** → startable once AMD-66–71 ratify.
   - **M6.2 — secret store + per-scope key-management infrastructure:** the DEK/KEK manager, the **`PayloadCipher` seam** (consumer-defined in persistence, impl in config), `scope_keys`. Gated on Doc 15 (done) + AMD-66–71.
   - **M6.3 — at-rest write-path encryption:** the sensitive-PII categories encrypted-on-write. **GATED — see guardrails.**
   - **M6.4 — hot-reload atomic swap.**
   **Embed verbatim into the charter** (so they survive into M6.2/M6.3): the **E2 `com.homesynapse.app` composition-root bridge** (Doc 15 §3.8 — the persistence↔config cycle-avoidance, the AMD-45 injection pattern) and **OR-M6-NONCE** (Doc 15 §6 / §13.4 — the per-scope counter-nonce must be durable + strictly monotonic across crash AND restore; co-design with the deferred backup/restore F3). Then **draft the M6.1 coding instruction** (apply the **P2 consumer/pin survey**; embed the verbatim `module-info.java` for the config module per the Research-6 rule; gated on AMD-66–71 ratification).

3. **M5-B/B2 — the regret-proof schema decisions (ride alongside the M6 amendments).** The schema-irreversibles the immutable log makes now-or-never: **C8 `actorRef` identity semantics** and **C9 the energy event *shape*** (shape only, no features — D4; ground it in the data-readiness §4 field set — `power_measurement` attributes + the aggregate fields — and let the M5-D microbench/interview signal refine it). **C10 payload-typing posture** if gate capacity remains. Each must pass the **contract-freeze-readiness gate** (round-trips / enforceable / owner-doc) before any downstream milestone leans on it.

**Guardrails (do not violate):**
- **M6 MUST be chartered as multiple first-class pieces (P1).** A single "M6" line that hides config + key-manager + at-rest encryption + hot-reload is the M4 epic-in-disguise mistake.
- **Do NOT issue M6.3 (at-rest write-path encryption) yet.** It is gated on three things, two of which Nick is still running: **(a) OQ-15-2** (the exact encrypted-scope set, from the Pi-4 microbench) + **(b) the energy/erasure interview signal** (confirming no launch-window buyer requires operational crypto-shredding — AMD-86 §3; if one does, AMD-86 re-opens via the **formal pipeline before M6 freezes the write path**) + **(c) OR-M6-NONCE** co-design. M6.1/M6.2 do **not** wait on these.
- **Keep Locked Doc 15 inviolate.** The microbench tunes the encrypted-scope **list** (a Doc 15 §9 default, not a re-open); only the erasure interviews can re-open AMD-86, via the formal pipeline. If authoring surfaces a Doc 15 design gap, STOP and escalate.
- **Independent (DOCS-Project-style) review** for the AMD-66–71 block + the B2 schema decisions — they freeze contracts, the way Doc 15/AMD-86/87 and the M5-D evidence got reviewed.

**In parallel (Nick's pace — these unblock M6.3 + populate the LTD-01 ledger, and don't block this session):** run the **Pi-4 AES-GCM microbench** → resolves **OQ-15-2** (writes the resolved set back into the Doc 15 §9 `encrypted_scopes` default — a list-TUNING, not a re-open); **schedule + begin the energy/erasure interviews** (calendar-bound — the long pole; start early); the **GraalVM native-image (C15) + Gen-ZGC-vs-G1 (C16) Pi spikes** → LTD-01 reversal-criteria ledger. **M5-C website/docs** is the non-preemptable parallel floor (P6/D3).

**Read before working the M6 entry-gate:**
- `nexsys-hivemind/context/planning/weeks/2026-W24_jun08-jun14.md` — the week's plan (lanes, gate-capacity sequencing, what spills).
- `nexsys-hivemind/context/decisions/2026-06-06_post-M4_M5-window_decisions.md` — D2 (crypto MVP scope, M6 sizing) + D4 (energy shape-now).
- **Research 5 (the AMD-66–71 source):** `nexsys-hivemind/context/assessments/2026-05-22_Research_5_PM_Assessment.md` (the A− assessment) + `homesynapse-core-docs/research/returns/2026-05-22_Research_05_Configuration_System.md` (the return) + `nexsys-hivemind/context/instructions/Research_5_Configuration_Brief.md`.
- `homesynapse-core-docs/design/06-configuration-system.md` (Locked — what AMD-66–71 amend; esp. §8.5 `SecretStore`) + `homesynapse-core-docs/design/amendments/AMD-60_Security_Services_Aggregator.md` (`CredentialRotator`).
- `homesynapse-core-docs/design/15-cryptographic-architecture.md` — **§3.8** (the E2 `com.homesynapse.app` bridge + `PayloadCipher` seam), **§6 / §13.4** (OR-M6-NONCE), **§7.3** (the Doc 06 reconciliation + the `SecretStore.setAll` requirement), **§9** (`encrypted_scopes`).
- `homesynapse-core/config/configuration/MODULE_CONTEXT.md` + its `module-info.java` (the config module's current state — embed the verbatim module-info in the M6.1 instruction).
- The M5-D microbench spec (`context/assessments/2026-06-07_M5-D_Pi4_AES-GCM_write-path_microbench_spec_OQ-15-2.md`) — the OQ-15-2 writeback target for §9.

---

**— THEN, LATER (when Nick brings results):** when Nick pastes **Pi-4 microbench numbers** → switch to the **OQ-15-2 writeback**: fold the resolved encrypted-scope set into the Doc 15 §9 default + the M6.3 scope (a list-tuning, NOT a Doc 15 re-open; STOP-and-escalate if a result implies a design change). When Nick brings **interview results** → if a launch-window buyer trips the AMD-86 §3 verifiable-erasure trigger, **re-open AMD-86 via the formal pipeline before M6 freezes the write path**; otherwise record "trigger not tripped" and M6.3 proceeds on the current scope.

**Deliverables for this session:** AMD-66–71 + the Doc 06 currency amendment (authored, with the DOCS-review prompt); the M6 charter (multi-piece, carrying the E2 bridge + OR-M6-NONCE); the gated M6.1 coding instruction; the B2 schema decisions (C8 + C9, contract-freeze-ready). Save each as a dated artifact under the appropriate `context/` location, update the W24 charter + backlog + Open Risks, run the WUCP-style closeout, and give Nick the commit messages.

Throughout: source-verify, STOP on any mismatch, keep Locked Doc 15 inviolate, lane-track M6 (P1), and independent-review the contract-freezing amendments.
