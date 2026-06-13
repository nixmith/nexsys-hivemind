<!--
file: context/planning/2026-06-13_side-research-candidates_CORE-DOCS.md
purpose: Enumerated side-research candidates for the two Claude Projects (CORE / DOCS) — the open technical questions worth investigating in parallel to provide insight and technical guidance for upcoming Core milestones. Companion to the 2026-06-13 next-coding-instruction session prompt.
audience: Nick, PM
state-type: planning / research-agenda delta
status: READY — Nick selects + dispatches (veto-or-default); each lands as an R-series return, PM-assessed
-->

# Side-Research Candidates — CORE / DOCS Projects (2026-06-13)

These are the open technical questions whose answers would de-risk or sharpen upcoming Core work. They run **in parallel** to the Core coding pipeline (they don't compete for the Coder or Nick's ratification gate — they compete only for dispatch attention). Each is dispatched as an R-series return to the named Project (fresh conversation; web search where applicable; the standard quote-back set + bucket structure; PM-assessed on return per the established cycle). **Routing convention:** design/architecture/market research → **DOCS Project**; code-empirical spikes → **CORE Project** (Coder-authored throwaway, Nick-run, never production).

Recommended dispatch order is by adjacency to current work (R-α and R-β first).

---

## R-α — Crash-safe backup/restore for an event-sourced + per-scope-encrypted store  → DOCS Project
- **Question:** What backup/restore design preserves GCM nonce-monotonicity across a restore (DEK-rotation-on-restore vs. carry-the-high-water-mark-in-backup), stays crash-atomic, and supports partial/per-entity backfill — for a store where only `[identity, presence_personal]` scopes are encrypted-on-write?
- **Why now:** **OR-M6-NONCE's restore half leans directly on this** (a restore must never resume a scope at a counter ≤ any value already used under that DEK). M6.3 can author the write-path now, but the backup/restore *co-design* needs this answer to fully close. Also a forward operational feature (foundation-readiness F3) and the home of the deferrable OQ-05-07 backfill residuals.
- **Unblocks:** M6.3's restore co-design; the deferred backup/restore feature; OQ-05-07 closure.
- **Readiness:** HIGH — Doc 15 §3.4/§6 + OR-M6-NONCE define the constraint set; ready to brief immediately.

## R-β — GraalVM native-image (C15) + Gen-ZGC-vs-G1 Pi pause (C16) spikes  → CORE Project (empirical)
- **Question:** Does a closed-world native-image build of Core survive (reflection/JPMS/SQLite-JNI/Jackson config), and what startup/footprint does it buy on a Pi? Separately, G1 vs Generational ZGC pause distribution under the Pi load profile? And — the entangled sub-question — do JNR/JNA-class reflection bindings survive C15's closed-world config (this settles **OR-M13-SDNOTIFY**'s subprocess-vs-FFM transport choice)?
- **Why now:** Feeds the **LTD-01 reversal-criteria ledger** (the standing Java-vs-Rust replatform question) with real numbers, and is the gating input for the M13 sd_notify transport decision (decision matrix already authored, PM rec = defer-to-M13 gated on exactly this spike).
- **Unblocks:** the M13 transport pick; the LTD-01 trajectory; the WatchdogSec lifecycle call.
- **Readiness:** HIGH — both spikes are scoped in the M5-D decision matrix + the language-replatform assessment; Coder authors throwaway, Nick runs on the Pi.

## R-γ — M9 Integration Runtime: supervisor / health-FSM / thread architecture  → DOCS Project
- **Question:** Best-practice supervisor and health-FSM patterns for integration adapters on constrained hardware — failure isolation, restart backoff/circuit-breaking, the health state machine, and the empirical restart-rate default (the known **NQ-6 pre-M9 spike**: 1/60s global + per-descriptor override).
- **Why now:** M9 is flagged "large" in the runway (supervisor/health-FSM/thread-arch). De-risking the architecture *before* scoping prevents the M4-style "size discovered in arrears." M9 is the next major subsystem after the M6→M7 band.
- **Unblocks:** M9 scoping/charter; the NQ-6 restart-default empirical.
- **Readiness:** MEDIUM — Doc 05 (Integration Runtime, Locked) is the design anchor; brief scopes the open empirical/pattern questions, not a redesign.

## R-δ — M14 Zigbee integration de-risk (highest-risk milestone)  → DOCS Project
- **Question:** Device-conformance + codec-quirk corpus for the real-hardware path — Tuya/Xiaomi non-standard ZCL clusters, dual-coordinator strategy, and a real-device test matrix.
- **Why now:** M14 is **the single riskiest milestone** (real hardware, ~Sep–Oct, late in the runway). Front-loading the research while there's runway slack avoids colliding device-quirk discovery with the M15 validation crunch. Builds on the existing `2026-03-22_Matter_Device_Conformance_Research_Plan.md` + Doc 08.
- **Unblocks:** M14 scoping; the real-device procurement + test plan (hardware lead time matters).
- **Readiness:** MEDIUM — Doc 08 (Zigbee Adapter, Locked) + the Matter conformance plan anchor it; this is the largest-effort candidate.

## R-ε — M12 Observability: MDC propagation on virtual threads (Java 21)  → DOCS Project (or CORE empirical)
- **Question:** The explicit-copy MDC mechanism on virtual threads (TaskDecorator-style, per LTD-01 — Java 21 is locked, Scoped Values are trajectory-only), the noise-budget, and `correlation_id` propagation across vthread boundaries. Discharges the **R16-B disposition §2b obligations** (correlation_id pin; naming convention; noise-budget test; `config_error` message register).
- **Why now:** vthread MDC is a known Java-21 sharp edge; settling the pattern before M12 prevents observability rework. R16 already laid the groundwork — this is the M12-scoping deepening, not a fresh start.
- **Unblocks:** M12 scoping; the disposition §2b obligations.
- **Readiness:** MEDIUM — R16 merged disposition is the input; can wait until M9/M10/M11 land (M12 is further out).

---

## Not research — internal decisions to park (noted for completeness)
- **§4c ArchUnit reach decision** (whitelist module test source sets vs. extend the app ArchUnit run) — rides the next app-module-touching WU; the *wording* half was corrected 2026-06-13. Not a Project research item.
- **OQ-05-07** (Research 9 residuals — operator rebuild / partial backfill / observability / failure semantics) — deferrable; folds naturally into **R-α** if/when dispatched.

## Dispatch note
Pick the set Nick wants; **R-α and R-β are the highest-leverage now** (both adjacent to live work — M6.3's restore co-design and the M13/LTD-01 fork). R-γ/R-δ are runway-de-risking and can lead the next research cycle. Honor the standing research discipline: fresh conversation per brief, web search required for the DOCS-Project items, verbatim quote-back set, bucket structure, anti-requirements bind, PM serialized assessment on return.
