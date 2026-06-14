<!--
file: context/audits/2026-06-15_core-review_CONVERGE_synthesis.md
purpose: The converge deliverable for the two-part homesynapse-core review. Synthesizes Sessions A (modules 1-8, data/crypto spine) + B (modules 9-22, runtime/automation/M7) into ONE ranked, de-duplicated, dispositioned backlog + the cross-session seams + the M7-forward readiness package + the Claude-Code-verification shortlist. Synthesis, not concatenation.
audience: Nick, the next (M7.1-prep) session
state-type: audit / synthesis (review-specific, one-shot)
status: COMPLETE
review-baseline: core HEAD 1eddd9a (M6 COMPLETE 4-of-4, M6.3 committed); watermark AMD-93; invariants 163/47; projectionVersion 5; 22 Gradle subprojects. Static read-and-reason converge — Cowork cannot run Gradle; sandbox git quarantined; host Read tools authoritative.
inputs: context/audits/2026-06-14_core-review_A_data-crypto-spine.md · context/audits/2026-06-14_core-review_B_runtime-automation-M7.md · the 2026-06-14 FRAMEWORK · the M7 planning set + standing research set
-->

# Converge — Synthesis & the M7-Forward Plan

**PM / senior systems architect (`nexsys-project-manager` hat), Cowork, static converge (no Gradle).** This is the session that merges A + B into one picture and a confident M7-forward direction. Where a finding drives a backlog rank or the M7 call, I re-verified it against `.java` source with host Read/Grep (cited below); I did not propagate an A/B claim I had not re-confirmed.

**Preflight (review lens):** PASS-for-review. Both audits ran against the framework baseline `1eddd9a`; the one known staleness (PROJECT_SNAPSHOT masthead still reads M6.3-uncommitted) is framework-pre-cleared. No CONFLICTED state. A converge is a read-only review, not forward work — drift is captured as findings, nothing is fixed here. Source-round-trip spot-checks this session: the placeholder automation event records, `RunStatus`, the C1-interim pin, type-residency, the B-H1 server wiring, and the F-A1 decrypt path all resolve in source exactly as the audits cite (§ "Verification re-checks" at foot).

---

## 1. Executive summary (stands alone)

**Unified health verdict — the core is sound where built; the product is not yet runnable, and the two things that make it runnable each carry one HIGH.** Sessions A and B reviewed disjoint halves and reached the same shape of answer. The event-sourcing spine and the M6.3 at-rest crypto (A) are built right — counter-nonce durability is fsync-ahead-of-return, the write path is fail-closed, the YAML/secret surface is solid, and the historically dangerous spots (derived-event `eventTime`, the `Expectation` codec, the `DerivationRule` fabrication) are all clean. The M3.x runtime that exists (B) is coherent, crash-safe, and the on-device ITs genuinely prove recovery. **There is no BLOCKING finding in either half** — because nothing ships yet: `main()` is a one-line stub, so the crypto is inert and the HTTP surface is unexposed.

**The two HIGH findings are independent today but detonate at the same milestone — app-bootstrap (when `main()` wires `HomeSynapseCore`).** That is the converge's headline insight, invisible to either session alone:

- **C1 / B-H1 (HIGH, security):** the composition root stands up an unauthenticated HTTP server (`installReadinessGate` only; `app.start(httpPort())` with no `.host()`); INV-SE-02's enforcing code (`AuthMiddleware`/`RateLimiter`) is unimplemented. The moment `main()` is wired, this is a live unauthenticated surface.
- **C2 / F-A1 (HIGH, forward):** a read-path decrypt failure throws and aborts the whole replay — no per-row `DegradedEvent` degrade like codec failures get. The moment `main()` activates `payloadCipher`, a lost/corrupt key makes the store unreplayable (vs INV-RF-04), and the future crypto-shred breaks replay (vs INV-PD-07).

Neither HIGH is on the M7 critical path. **The app-bootstrap milestone must carry both** (auth + the confidentiality-vs-availability contract) plus the lifecycle reconciliation (C9/B-M1) — it is a high-density latent-defect milestone and should be gated before `main()` is wired.

**The M7-forward call: M7 is READY to build, with two cheap fix-firsts and no research-first blocker on the M7 path.** The 53-type automation contract is sound to build on, every live surface it consumes exists and is exported, and all three M7 safety pins hold in source today (type-residency, the C1-interim no-publish pin, LTD-11) — re-verified this session. The two fix-firsts are doc/record items (C3 cascade-governance doc drift; C4 the placeholder event records), both small. The standing entry-gate rows **3 (energy/erasure interviews) + 4 (M5-C Increment 1 approve)** still govern *issue* — row 4 is one Nick veto away; row 3 is the sole open evidence gate and carries the M6.3-vs-M7 ordering call. **Nothing BLOCKING; nothing stops M7.1 prep from starting now.**

**Top of the backlog (full table §2):**

| ID | sev | M7? | one-line | disposition |
|---|---|---|---|---|
| **C1** (B-H1) | HIGH | no (app-bootstrap) | Unauthenticated composition-root HTTP surface; INV-SE-02 unenforced | Nick-decision + coding-instruction |
| **C2** (F-A1) | HIGH | no (gates crypto-shred) | Read-path decrypt failure aborts whole replay; no DegradedEvent degrade | Nick-decision + coding-instruction |
| **C3** (B-M2) | MED | **fix-first M7.2** | Cascade governance docs the superseded AMD-04 model, not AMD-91/RunCausalChain | doc-fix |
| **C4** (B-M3) | MED | **fix-first M7 F5** | Placeholder automation event records can't express INTERRUPTED/CONDITION_NOT_MET (**cross-seam**) | coding-instruction |
| **C5** (F-A3) | MED | no | Event→scope mapping duplicated; pin checks the mirror in isolation | coding-instruction |
| **C6** (F-A2) | MED | no | Random-IV + counter-nonce share one DEK (NIST SP 800-38D §8.3) | Nick-decision + governance pin |
| **C7** (F-B1) | MED | no | `MigrationRunner.splitSqlStatements` emits comment-only fragments (CONFIRMED) | coding-instruction |
| **C8** (F-A4+F-A5a) | MED | no | Crypto write-path fail-closed hardening: ctor invariant + fatal nonce dir-fsync | coding-instruction |
| **C9** (B-M1) | MED | no (app-bootstrap) | Disjoint lifecycle abstractions (`SystemLifecycleManager` vs `HomeSynapseCore`) | coding-instruction + Nick-decision |

Tier-2 (real, milestone-deferred, not M7-gating): C10–C15 — §2.

---

## 2. The ranked, de-duplicated backlog

Globally re-ranked by severity × M7-impact × effort; A's and B's findings collapsed where they share a root cause (sites listed). Format: `ID (source) | sev | type | site(s) | issue | recommendation | disposition | tag`. Every row passes "so-what / now-what." LOW/INFO stay rolled-up in the source audits.

### Tier 1 — act-soon / M7-gating / pre-app-bootstrap

**C1 (=B-H1) · HIGH · security/forward-risk** — `lifecycle/.../HomeSynapseCore.java:408-435`; `RestFilters` (no auth method); `AuthMiddleware`/`RateLimiter` (zero impls).
Issue: the composition root installs only `RestFilters.installReadinessGate` as a `before` filter and calls `app.start(config.httpPort())` (no `.host()`, no auth, no rate-limit); `/internal/*` admin endpoints sit outside even the readiness gate. INV-SE-02 ("auth mandatory on every external interface; no local-trust exception") has no enforcing implementation. Latent only because `main()` is a stub.
Rec: gate the app-bootstrap milestone on `AuthMiddleware before("/api/*")` + `RateLimiter`; decide bind posture (loopback-default vs all-interfaces). Confirm auth-before-network-exposure is a tracked milestone — it currently is not.
Disposition: **needs-Nick-decision + needs-coding-instruction.** Tag: [VERIFIED] (wiring; re-confirmed `:412` + `:434`); the all-interfaces exposure is [HYPOTHESIS] → CC-1.

**C2 (=F-A1) · HIGH · correctness/security (forward)** — `core/persistence/.../SqliteEventStore.java:804-810` + `:896-913`.
Issue: `fromRow` routes any `dek_ref`-bearing row through `decryptStoredPayload`, which **throws** on missing cipher (`:899`), malformed `dek_ref` (`:906`), GCM auth-fail, or a destroyed key. No per-row catch → one bad row fails the whole `readRows` batch. This deliberately contrasts with codec parse failures, which degrade to `DegradedEvent` so the read continues (class Javadoc `:88`; `decodeCategories` falls back to SYSTEM "so the read still succeeds" `:846`). Consequences: a lost/corrupt `.root-key` → the **entire store is unreplayable** (vs INV-RF-04); when crypto-shred lands, replay across a shredded event throws (vs INV-PD-07). The missing-cipher-on-read and shredded-key-on-read paths have **no test**.
Rec: decide the confidentiality-vs-availability contract **before** crypto-shred is built — most likely catch decrypt failure in `fromRow` and emit `DegradedEvent` for the shredded/undecryptable case, keeping a hard fail only for "cipher entirely unwired but encrypted rows exist." Add tests for both read-side failure modes.
Disposition: **needs-Nick-decision (design tradeoff) + needs-coding-instruction (crypto-shred WU).** Tag: [VERIFIED] (throw/no-catch mechanism re-confirmed; INV implications reasoned). Research-first: NEW-1 / R-α (§5).

**C3 (=B-M2 / B-12a) · MED · drift · FIX-FIRST before M7.2** — `core/automation/.../RunContext.java:30-36` + `automation/MODULE_CONTEXT.md:200,316`.
Issue: cascade governance is still documented as the superseded **AMD-04** model (`cascadeDepth:int`, `max_cascade_depth` 8/1-32, `cascade_depth_exceeded`). **AMD-91 superseded AMD-04** (F4: `cascadeDepth`→`causalChain: RunCausalChain`; same-automation cycle detection with a distinct diagnostic). A Coder building M7.2 cascade governance from the contract/MODULE_CONTEXT — not the charter — builds the depth-only model and misses cycle detection.
Rec: update the `RunContext` Javadoc + MODULE_CONTEXT to cite AMD-91 and flag the F4 reshape as M7.2 work. Cheap.
Disposition: **needs-doc-fix (before M7.2).** Tag: [VERIFIED].

**C4 (=B-M3 / B-12b) · MED · forward-risk/drift · FIX-FIRST for M7 F5 · CROSS-SEAM (A×B)** — `core/event-model/.../AutomationTriggeredEvent.java:16-19` + `AutomationCompletedEvent.java:31-35` (Session A's module) vs `core/automation/.../RunStatus.java:64,78` (Session B's module).
Issue: the on-disk automation event records are minimal placeholders below the F5 spec. `AutomationCompletedEvent`'s `status` string is documented {`success`,`failure`,`aborted`} and **cannot express** `RunStatus.INTERRUPTED` (the §3.10 zombie-Run terminal) or `CONDITION_NOT_MET` — both of which exist in the automation `RunStatus` enum today. `AutomationTriggeredEvent` carries only `triggerType`/`triggerDetail` — none of F5's `matched_triggers`/`resolved_targets`/`definition_hash`.
Rec: M7's F5 slice must widen these (field-additions per AMD-88-INV-01) **before any production publish**, honoring type-residency (flatten — no `RunStatus` in payload) and AMD-52 codec discipline. Settle the widening design at M7.1 scoping. The records live in event-model (A); the requirement is automation's (B) — see §3.
Disposition: **needs-coding-instruction (M7 F5) + converge seam.** Tag: [VERIFIED] (both records + `RunStatus` re-read this session).

**C5 (=F-A3) · MED · drift/test-weakness** — canonical `config/.../EncryptionScope.java:123-133`; mirror `core/persistence/.../SqliteEventStore.java:881-885`.
Issue: the category→scope mapping exists twice (config canonical + persistence String mirror, intentional to avoid a `persistence→config` edge). The pin (`AtRestEncryptionWritePathTest`) checks the mirror in isolation — it never cross-checks the canonical (it can't; persistence has no `config` dep). A future change to the canonical mapping diverges silently: a sensitive event written **plaintext**, or under a `scope_id` the key store doesn't match (→ C2 decrypt-fail).
Rec: add a cross-module agreement test in `app` (sees both) asserting persistence's classification matches `EncryptionScope.scopeIdFor` for every `EventCategory`, driven through the public publish/read path. (The test lands in `app` — Session B's module 17; minor seam.)
Disposition: **needs-coding-instruction.** Tag: [VERIFIED].

**C6 (=F-A2) · MED · security/forward-risk** — `config/.../StandardScopeKeyManager.java:149-196`; test `ScopeKeyManagerPayloadNonceTest.java:164-178`.
Issue: `encrypt()` (random 96-bit IV) and `encryptPayload()` (deterministic counter nonce) both resolve the **same per-scope DEK**; nothing binds a scope to one construction. The `fence_randomIvPathUnchanged` test exercises both on scope `identity` — the **NIST SP 800-38D §8.3** anti-pattern ("the deterministic and the RBG-based construction shall not both be used" for one key). Safe in production today only by unenforced scope-disjointness.
Rec: bind each scope to exactly one nonce strategy (namespace, or guard `encryptPayload`/`encrypt` to reject a scope that has issued the other), encode as an enforced invariant + a NIST citation in Doc 15 §3.4. Reconsider the one-scope fence test.
Disposition: **needs-Nick-decision / governance pin + coding-instruction.** Tag: [VERIFIED].

**C7 (=F-B1) · MED · correctness/forward-risk · CONFIRMED** — `core/persistence/.../MigrationRunner.java:429-463`.
Issue: the splitter appends comment characters into the current buffer; a `--` comment after the final `;` becomes a non-empty trailing fragment emitted as a statement → sqlite-jdbc rejects → migration fails. This **broke every DB-init in the V005 gate-fix round 2 (2026-06-13)** — independently corroborated in PROJECT_SNAPSHOT's M6.3 record ("round 2 regression: V005 trailing-comment migration idiom broke all DB-init"). The fix was applied in the V005 SQL header, **not the splitter**, so it remains a latent trap for the next migration author. Sibling sweep CLEAN at HEAD.
Rec: one-line guard — strip `--`-to-EOL before adding a fragment, skip if the remainder is blank. Keep the V005 header note as belt-and-suspenders.
Disposition: **needs-coding-instruction.** Tag: [VERIFIED] (CONFIRMED). Regression-pin test rides the fix (not a CC dispatch).

**C8 (=F-A4 + F-A5a) · MED · security-hygiene/forward-risk** — `core/persistence/.../SqliteEventStore.java:302-318` (ctor); `config/.../AtomicYamlWriter.java:131-142` (nonce dir-fsync).
Issue (bundled — one crypto-write-path hardening instruction): (a) the `SqliteEventStore` ctor Javadoc says "null cipher ⇒ encryptedScopes MUST be empty" but the ctor only assigns — no guard; a real misconfig surfaces late (first sensitive publish), not at startup. (b) the OR-M6-NONCE high-water durability rests on `fsyncDirectory(parent)`, whose POSIX `IOException` is **swallowed at DEBUG**; a silent dir-fsync failure on the catastrophic-if-wrong nonce path could leave the rename non-durable → a post-crash nonce repeat breaks AES-GCM.
Rec: (a) add a fail-fast ctor guard (or correct the Javadoc to state write-time fail-closed is the contract); (b) on the **nonce-counter write specifically**, treat a dir-fsync `IOException` as fatal (fail-closed), not DEBUG-swallow.
Disposition: **needs-coding-instruction / needs-doc-fix.** Tag: [VERIFIED].

**C9 (=B-M1) · MED · forward-risk/composition (app-bootstrap)** — `lifecycle/.../SystemLifecycleManager.java:30` (interface, no impl); `HomeSynapseCore.java` (concrete, test-only construction); `app/.../Main.java:27-29` (stub).
Issue: two disjoint lifecycle abstractions. `SystemLifecycleManager` — the Doc-12 orchestrator `module-info` names as the `main()` entry point, owning the init phases, the health loop (§3.10) and the systemd watchdog — is an unimplemented interface that never references `HomeSynapseCore`, the real composition root (constructed only in tests). So platform-systemd's `SystemdHealthReporter` has no path to the running system.
Rec: the app-bootstrap milestone must reconcile (either `main()` constructs `HomeSynapseCore` directly and the 6-phase/health-loop model is re-homed, or `SystemLifecycleManager` wraps `HomeSynapseCore`); pin the health-loop/watchdog wiring with a test. Decide explicitly.
Disposition: **needs-coding-instruction + needs-Nick-decision.** Tag: [VERIFIED]. Rides app-bootstrap with C1.

### Tier 2 — real, milestone-deferred, NOT M7-gating

| ID (source) | sev | site / theme | disposition |
|---|---|---|---|
| **C10** (B-M4+B-9a+B-10a+B-18a) | MED | Behavioral invariants in **contract-only modules** are unpinned — backoff schedule re-impl'd in test (B-9a), AUTH_FAILED routing untested (B-10a), AMD-56/62 integration behavior (B-M4), sd_notify ctor (B-18a). Root cause: the production code is unwritten (B-CC2). | needs-coding-instruction at each module's milestone (M9/M13) — re-pin when code lands |
| **C11** (B-M5 / B-14a) | MED | websocket-api backpressure undelivered — 25 files of scaffold, no bounded-buffer/`CLIENT_TOO_SLOW` impl. M7's `RunManager` live-trace streaming is its first consumer (later). | needs-coding-instruction (WS milestone) |
| **C12** (B-M6) | MED | Premature/empty surface — app `runtimeOnly(:web-ui:dashboard)` packages an empty JAR; `spike/wal-validation` in-tree with committed `.db` blobs (standing `git rm` advisory). | needs-coding-instruction / needs-Nick-decision (hygiene) |
| **C13** (F-C1) | MED | event-bus retry/backoff is dead code while `SubscriberSupervisor`'s Javadoc advertises it as active. No correctness hole (events park durably; circuit breaker works). | needs-doc-fix + reserved-register |
| **C14** (B-M7 / B-15a) | MED | `SystemHealth` Javadoc promises "exactly three tiers"; the ctor only null-checks. 0 tests leave ~12 observability records' validation unpinned. | needs-coding-instruction / needs-doc-fix (M11/M12) |
| **C15** (B-9b+B-10b+B-CC4) | MED→LOW | Systemic MODULE_CONTEXT/inventory drift (integration-api/runtime counts; rest-api/ws/zigbee package+field nits; the auth `before("/api/*")` gate described in MODULE_CONTEXT/build/module-info **as if wired** when production has only the readiness gate). **B-M2 carved out as C3** (the one materially-misleading instance). | needs-doc-fix (batch currency sweep) |

**Rolled-up, not itemized (in the source audits):** A's per-module minors (non-finite `AttributeValue` serde edge; the colon-bearing `dek_ref` `NumberFormatException` nicety; value-model's 0 own tests); B's `B-CC3` test-side direct-time-access invisible to the `NO_DIRECT_TIME_ACCESS` gate (all test-side, none a production violation); the two integration-IT minors (DLQ empty-shape, shutdown not-a-hang — both honestly disclosed Phase-3 gaps). None changes a near-term decision.

### Reserved-but-unbuilt register (consolidated A+B — a consumer must not assume these work)

Crypto side (A, verified from source): **crypto-shred operation** (`destroyedAt` field + decrypt guard exist; no setter — only the unreadability property ships); **OR-M6-NONCE restore half** (write-path discharged; rotate-on-restore NOT built — R-α); **`identity` scope** (keyed, maps to zero MVP event types — safe by construction; a future identity event must wire **both** config + the persistence mirror or it ships plaintext — see C5); **chain-hash activation** (`chain_hash` = 32-byte ZERO for every event; computation not built — Doc 01 §14 "not implemented" is accurate); **Ed25519 signing** (absent). Runtime side (B): **`main()` runtime construction** + `AuthMiddleware`/`RateLimiter` (app-bootstrap — C1); **`SystemLifecycleManager`** (C9); the entire **automation engine** (M7), **`IntegrationSupervisor`** + Zigbee stack (M9/M14), **websocket-api** + **observability** behavior; **`IntegrityService`** (M12 — does not exist even as a seam); sd_notify real transport (M13, fails-closed at construction). **Implication: at-rest encryption is real, tested, and correct — but inert until app-bootstrap activates `payloadCipher`. That same milestone makes C1 and C2 live.**

---

## 3. Cross-session seams (where A meets B — what neither session could see alone)

**Seam 1 — the two HIGH findings detonate at one milestone: app-bootstrap.** A reviewed crypto (F-A1) and B reviewed the composition root (B-H1) independently. They converge: when `main()` wires `HomeSynapseCore`, it simultaneously (a) activates `payloadCipher` — making C2's decrypt-abort a live availability risk — and (b) exposes the HTTP surface — making C1's no-auth a live security hole — and (c) first exercises the cipher adapter that today only `PayloadCipherBridgeTest` touches. **App-bootstrap is therefore a high-density latent-defect milestone that must carry, in one gate: the auth implementation (C1), the confidentiality-vs-availability contract (C2), and the lifecycle reconciliation (C9/B-M1).** This is the single most important converge conclusion: do not let app-bootstrap be scoped as "just wire `main()`."

**Seam 2 — the automation event records (C4): a contract A owns, a requirement B raised.** `AutomationTriggeredEvent`/`AutomationCompletedEvent` live in `com.homesynapse.event` (A's module 3). A reviewed event-model for spine correctness and correctly found the records **well-formed** (no A finding). B reviewed them for M7-automation-readiness and correctly found them **semantically insufficient** (`status` can't express `INTERRUPTED`/`CONDITION_NOT_MET`, which `RunStatus` already has). **This is not an A/B disagreement — both lenses are right.** The reconciliation: the records are correct-as-built and must be widened in M7's F5 slice; the widening is an **event-model change (A's territory) driven by an automation requirement (B's territory)** that must honor type-residency (flatten — no `RunStatus` in payload) and AMD-52 codec discipline. The design beat spans both modules; settle it at M7.1 scoping.

**Seam 3 — the crypto is shipped but dormant; the apex that activates it is unbuilt.** A: "at-rest encryption is NOT active at runtime until app-bootstrap wires the cipher." B: "`main()` is a stub; `HomeSynapseCore` is constructed only in tests." Same fact, two sides. Consequence beyond Seam 1: the cross-module mapping-agreement test C5 recommends must land in `app` (B's module 17) but tests a config↔persistence contract A found — the fix crosses the seam too.

**No A/B contradictions were found.** The sessions reviewed disjoint module sets (1-8 / 9-22) with exactly one shared artifact (the automation event records, Seam 2). Every shared-boundary claim was re-checked against source this session and the two audits agree.

---

## 4. The M7-forward readiness package (the headline deliverable)

**Call: M7 is READY to build. Two cheap fix-firsts; no research-first blocker on the M7 path. Issue is gated by entry-gate rows 3 + 4 (Nick's), not by engineering readiness.**

### READY for M7.1 (verified in source, A + B + this session's re-checks)
- **The 53-type automation contract is sound to build on** — sealing total, collections defensively copied, identifiers typed (`RunId` wraps `Ulid`, LTD-04), compact constructors validate, zero `synchronized`, zero direct-time-access, zero publish sites (B, module 12 DEEP).
- **Every live surface automation consumes exists and is exported** — `EventEnvelope`/`EventId`/`CommandIdempotency` (event-model), `Expectation` (device-model), `StateSnapshot`/`Availability` (state-store); A independently confirmed these module contracts are exact, and the `Expectation` codec is shipped + round-trip-tested (B's refuted candidate finding confirmed it active, not `@Disabled`).
- **All three M7 safety pins hold in source today** (re-verified this session): type-residency — no `RunId`/`RunStatus`/`PendingStatus` in any event-model payload (grep clean); the C1-interim pin — zero production `automation_triggered` publish sites (only the record defs, the `EventTypes` constant, tests, and docs reference the types); LTD-11 clean.
- **The spine automation publishes into is correct** (A): per-entity sequence, `eventTime`/`ingestTime` separation, write-ahead durability, the compile-exhaustive `Expectation` tagged-union codec.
- **The config substrate M7.1 loads definitions through** (M6.1/6.2/6.4) is shipped; its security surface (YAML traversal guard, `!secret`/`!env` resolution on load+reload, fail-closed validation) is solid (A).
- **Entry-gate rows 1, 2, 5 CLOSED** — AMD-88..93 + B2 C8/C9 ratified; automation MODULE_CONTEXT current re permit-count; survey rows build per-instruction.

### FIX-FIRST (must close before M7 builds on them — both cheap, both confirmed in source)
- **C3 / B-M2 — before M7.2:** retire the superseded-AMD-04 cascade-governance docs (`RunContext` Javadoc + MODULE_CONTEXT) in favor of AMD-91/`RunCausalChain` + cycle detection. A doc-fix; do it before the M7.2 instruction is drafted so the implementer doesn't build the depth-only model.
- **C4 / B-M3 — before the M7 F5 event slice:** widen the placeholder automation event records to carry the F5 fields and the full `RunStatus` vocabulary (`INTERRUPTED`/`CONDITION_NOT_MET`), flattened per type-residency, AMD-52-coded. This is an M7 F5 work item; settle the *design* at M7.1 scoping (Seam 2).

### RESEARCH-FIRST
- **On the M7 path: none.** M7.1/7.2/7.3 touch no crypto and no unbuilt upstream; the trigger-storm benchmark (REC-157) and the confirmation-deadline calibration spike (REC-161) are charter-obligation empirical spikes **embedded in the M7.x instructions** (investigation triggers), not blocking research dispatches.
- **On the parallel crypto / app-bootstrap track (not M7-blocking): R-α + NEW-1** — the confidentiality-vs-availability contract for the encrypted log (C2) and the backup/restore nonce-monotonicity co-design should return before the crypto-shred / backup-restore WUs are designed. See the research doc (deliverable 2).

### Standing entry-gate — governs ISSUE, not readiness (fold-in)
- Row 1 (AMD block) ✅ · Row 2 (C8 `actorRef`) ✅ · Row 5 (MODULE_CONTEXT + survey) ✅.
- **Row 4 (M5-C Increment 1 — the P6 Lane-4 structural gate): drafted-awaiting-veto.** Nick's APPROVE on `homesynapse-core-docs/website/pages/config-superiority.md` flips it and lifts the no-new-Core-instruction condition. One action away.
- **Row 3 (energy/erasure interviews): OPEN — the principal remaining gate.** Nick-paced; it is the sole open evidence input and it carries the **M6.3-vs-M7 ordering call** (does app-bootstrap activate crypto before or after M7?). Note M6.3 itself already LANDED GREEN, so row 3's live relevance is now the ordering decision, not M6.3 completion.

### Recommended M7 entry sequence
1. **Nick: veto the M5-C config-superiority draft** → closes row 4, lifts the Lane-4 condition.
2. **Land C3** (cascade doc-fix) now — cheap, and it must precede the M7.2 instruction.
3. **Nick: the energy/erasure interviews** → closes row 3 + resolves the M6.3-vs-M7 ordering call.
4. **Issue M7.1** (trigger/condition path) per the charter §4.3 checklist, carrying the standing carry-pins (type-residency, manifest fan-out + **publish-count** survey, AMD-52 codec, C8 stamping, §4c Clock-injection) **plus the converge pin: a composition-root manifest-survey + a lifecycle wiring test** — the AMD-92-INV-02 "full manifest before first publish" forcing point and the subscribe-after-state-store-catch-up ordering are exactly the latent-defect sites no module-local test pins (B's forward-readiness note on `HomeSynapseCore.start()`).
5. **M7.2** (run/action/dispatch) — only after C3 is closed, so cascade governance is built on AMD-91; settle the C4 F5 record-widening here or at the F5 slice.
6. **M7.3** (pending command ledger).

The two HIGH findings (C1, C2) and C9 do **not** sequence into M7 — they sequence into **app-bootstrap**, which should be gated separately (Seam 1) and is independent of the M7 build.

---

## 5. Claude-Code-verification shortlist

The framework's HYPOTHESIS findings, filtered to the few where an empirical answer **changes a decision** (not a speculative dump). Most converge findings are [VERIFIED-FROM-SOURCE] and need no gate. Three candidates:

**CC-1 — Does the composition root actually bind all-interfaces? (calibrates C1 urgency).**
- Static half **already PM-confirmed this session**: no `.host(` in `lifecycle` production code (only the readiness gate is installed); the `before("/api/*")` references are MODULE_CONTEXT/build comments describing an unbuilt gate.
- Empirical half (CC): a test that starts `HomeSynapseCore` and asserts the bound socket answers on a **non-loopback** address — plus `grep -rn "\.host(" lifecycle api` (expect none).
- Why: confirms whether the unauthenticated exposure is all-interfaces (urgent — internet-reachable on a misconfigured LAN) or loopback (less urgent). Pass (loopback) vs fail (all-interfaces) sets the auth-milestone priority. **Cheap; worth it.**

**CC-2 — Per-event fsync cost on the Pi-4 floor (F-A5b). Dispatch only when widening `encrypted_scopes` is contemplated.**
- CC: a JMH-style bench of the full `encryptPayload` (incl. the `scope_nonce_counters.json` atomic rewrite + 2 fsyncs) at 60 ev/s presence-burst on the Pi-4, measuring write-thread occupancy + p99 publish latency vs the plaintext path.
- Why: the OQ-15-2 microbench measured the encrypt op, not (visibly) the per-event nonce-counter fsync pair on the single write thread. **Gates a FUTURE decision** (widening encrypted scopes to a high-volume category), not a current one — so **defer the dispatch until that decision is live.** Mark tracked, not now.

**CC-3 (optional, low) — Demonstrate C2's blast radius.** A test reading an encrypted DB with a `null` cipher / destroyed key → expect the whole-batch throw. The mechanism is already [VERIFIED] from source, so this only *demonstrates* the blast radius for the crypto-shred design review; it does not change the degrade-vs-fail-closed decision (which the source already supports making). Dispatch only if Nick wants the empirical exhibit for that design beat.

**Net: CC-1 is the one worth dispatching now. CC-2 is tracked-until-relevant. CC-3 is optional.**

---

## Verification re-checks (this session, host Read/Grep on core `1eddd9a` tree)

- C4/Seam-2: `AutomationCompletedEvent(String status, String failureReason, long durationMs)`, status Javadoc'd {success,failure,aborted}; `AutomationTriggeredEvent(String triggerType, String triggerDetail)`; `RunStatus` enum carries `CONDITION_NOT_MET` (`:64`) + `INTERRUPTED` (`:78`). Gap confirmed.
- M7 pin (C1-interim): the only references to the two automation event types repo-wide are the record defs, `EventTypes.java` (the constant), 4 test files, and 2 docs — **zero production publish sites.**
- M7 pin (type-residency): `grep RunId|RunStatus|PendingStatus` in `event-model/src/main` → **no matches.**
- C1/B-H1: `HomeSynapseCore.java:412` installs only `installReadinessGate`; `:434` `app.start(config.httpPort())`; no `.host(`/auth in production.
- C2/F-A1: `SqliteEventStore.java:806-809` routes `dek_ref`-bearing rows through `decryptStoredPayload` (throws at `:899`/`:906`) with no per-row catch; `:846` shows the contrasting DegradedEvent-posture fallback for categories.
- C7/F-B1: independently corroborated by PROJECT_SNAPSHOT's M6.3 record of the V005 round-2 DB-init regression.

---

## Commit message (handed to Nick — `!`-free)

```
docs(audit): add converge synthesis — M7-forward plan (core-review A+B)

Synthesizes Review Sessions A (modules 1-8) and B (modules 9-22) into one
ranked, de-duplicated, dispositioned backlog + the cross-session seams + the
M7-forward readiness package + the Claude-Code-verification shortlist.
Baseline core 1eddd9a (M6 4-of-4), watermark AMD-93, projectionVersion 5.
Preflight PASS-for-review. No BLOCKING finding.

Unified verdict: the core is sound where built; the product is not yet
runnable. The two HIGH findings are independent today but both go live at
app-bootstrap (when main() wires HomeSynapseCore): C1 (=B-H1) unauthenticated
HTTP surface, INV-SE-02 unenforced; C2 (=F-A1) read-path decrypt failure
aborts the whole replay. App-bootstrap must carry auth + the confidentiality-
vs-availability contract + the lifecycle reconciliation (C9) in one gate.

M7-forward: READY to build. The 53-type automation contract is sound, every
consumed surface exists, and the three safety pins hold in source (re-verified:
type-residency, C1-interim no-publish, LTD-11). Two cheap fix-firsts: C3
cascade-governance doc drift (AMD-04 -> AMD-91) before M7.2; C4 the placeholder
automation event records (cannot express INTERRUPTED/CONDITION_NOT_MET) before
the M7 F5 slice. No research-first blocker on the M7 path. Entry-gate rows 3
(interviews) + 4 (M5-C approve) still govern issue.

Backlog: 2 HIGH (C1, C2), 7 Tier-1 MED (C3-C9), 6 Tier-2 MED (C10-C15,
milestone-deferred). CC-verification shortlist: CC-1 (bind-address) worth
dispatching now; CC-2 (per-event fsync bench) tracked-until-relevant; CC-3
optional. No production code, tests, or governance files modified.

File: context/audits/2026-06-15_core-review_CONVERGE_synthesis.md
```

---

*End of converge synthesis. Companion: `context/planning/2026-06-15_M7-plus_research-avenues.md` (consolidated research). No production code, tests, or governance files were modified — the sole writes are the two deliverables.*
