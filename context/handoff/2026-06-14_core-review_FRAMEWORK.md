<!--
file: context/handoff/2026-06-14_core-review_FRAMEWORK.md
purpose: Shared review machinery for the two-part homesynapse-core review (Sessions A + B) and its converge. Defines the stance, the Step-0 discipline, the per-module checklist, the defect taxonomy, the finding format, and the guardrails — everything identical across A and B. Each session prompt carries only its scope + focus and points here.
audience: PM (Cowork) running Review Session A or B
state-type: reference (review-specific, one-shot)
status: READY
-->

# Core-Review Framework (shared by Sessions A and B)

Read this in full at session start, alongside your session-specific prompt (A or B). This file is the *how*; your prompt is the *what* (which modules, which focus, which output file).

## Stance

You are the PM / most-senior systems architect + Java engineer (`nexsys-project-manager` hat). This is a **review**, not a coding session. Three jobs, in order: (1) build a correct model of your assigned modules from source; (2) adversarially hunt defects — correctness, security/crypto, and **test-suite weakness** (tests that wouldn't catch a real regression), plus drift and forward-risk; (3) surface M7+ research avenues. **Surface, do NOT fix** — every fix is a downstream instruction Nick triages.

## Calibrated honesty (the prime directive)

Cowork **cannot run Gradle** — this is a static, read-and-reason review. The hard lesson from the cycle that shipped M6.3: an LLM review is not the compiler or the test runner — an "adversarial review" declared a build "compile CLEAN" twice while real tooling found an unhandled checked exception and a migration that rolled back every DB-init. Therefore, **tag every finding**:

- **[VERIFIED-FROM-SOURCE]** — provable by reading: a contract mismatch, a missing case, a logic error, a drift visible in the bytes, a `synchronized` on a VT path. Cite `file:line`.
- **[HYPOTHESIS — NEEDS GATE]** — anything about runtime behavior: a test would pass/fail, a race, a performance claim. **Never assert these as fact.** For each one that matters, write the **exact Claude Code check** that would confirm it (the precise `:module:test --tests …`, the grep, the command, and the expected result). Cowork can't run it; Claude Code can — and Nick dispatches those deliberately, only where the answer is worth the round-trip.

The review's worth is measured in specific, evidence-cited, correctly-calibrated findings — **not** in a clean bill of health.

## Step 0 — preflight, environment, read-first set (MANDATORY)

1. **Invoke `nexsys-project-manager`; run the freshness preflight** (`project-manager/references/freshness-preflight.md`). Baseline: **M6 COMPLETE (4-of-4)**, core HEAD `1eddd9a`, hivemind `bbec2c7`, watermark AMD-93, invariants 163/47, projectionVersion 5, 22 Gradle subprojects, `./gradlew check` GREEN (147). If the snapshot still says M6.3 is "UNCOMMITTED," that is the one known staleness — it is committed at `1eddd9a`. CONFLICTED → escalate to Nick before reviewing.
2. **Environment realities:** the **truncated-tail mount artifact may be ACTIVE** — sandbox `git` is **quarantined** (it showed phantom diffs + left `index.lock`s last cycle); **do NOT run `git` in the sandbox**. **Host Read tools are authoritative.** You may read existing `*/build/reports/` and `*/build/test-results/` if present, but assume nothing about runtime you didn't read.
3. **Read-first set (your review lenses):** `context/status/PROJECT_SNAPSHOT.md`; the relevant **Locked design docs** for your modules + `Architecture_Invariants_v1.md` (the INV/LTD/AMD constitution); `coder/references/deviation-and-quality.md` §6 (Source Trust Hierarchy). Read the design doc for each module **before** its source, so you review against the contract.

## Source-of-truth discipline

`MODULE_CONTEXT.md`, handoff docs, and even design docs are **summaries and intentions** — they drift from, and occasionally fabricate against, the code (the preflight Check-11 hazard; the `MinimalDerivationRule`-that-never-existed precedent). **Every claim is verified against actual `.java`/`.sql`/`.kts` source, cited `file:line`.** MODULE_CONTEXT is the map; source is the territory; any disagreement is itself a **DRIFT finding**.

## Per-module checklist (apply to every module in your scope; depth scales with the PRIORITY marks in your prompt)

1. **Model** — in your own words from source: responsibility + the exported API (read `module-info.java` for the real JPMS name/edges, then the exported types).
2. **Contract verification (Check-11)** — spot-check MODULE_CONTEXT's inventory + cross-module contracts against source; drift is a finding.
3. **Implementation correctness** — the load-bearing impl classes: logic errors, off-by-one, boundary/null/empty handling, error paths (**fail closed** where integrity/security demands), resource handling (try-with-resources on `Connection`/`InputStream`/file handles).
4. **Test-suite adversarial audit** (give this real weight) — for each key contract, would a test **fail if the impl were subtly broken** (mutation mindset)? Flag tautological/weak assertions, pass-for-the-wrong-reason tests, over-mocking that skips the real path, missing edge cases, timing/order flakiness, and **direct-time-access in test code** (`Instant.now()`/`System.nanoTime`/`currentTimeMillis`/`Clock.systemUTC()`) — the `NO_DIRECT_TIME_ACCESS` ArchUnit rule only scans app-visible classes (corrected 2026-06-13), so non-app **test** modules can hide violations the gate never catches.
5. **Constraint compliance** — the INVs/LTDs the module touches: especially **LTD-11** (no `synchronized` on any VT path — grep it), **LTD-04** (typed ULID, BLOB(16), Crockford only at boundaries), **LTD-15** (no key/secret/PII-plaintext in logs or events), plus the module's Locked behavioral contracts.
6. **Security posture** (mandatory for `configuration`/`persistence`/`api`/`integration`) — input validation, injection (string-built SQL, YAML), path traversal, fail-closed-on-error, secret/key handling, crypto specifics.
7. **Forward-risk + M7-readiness** — what works now but risks breaking at scale, on the Pi-4 floor, or when M7+ builds on it.
8. **Ledger row** — module → depth (deep/medium/light) → finding IDs.

## Defect taxonomy (the specific hunt — cross-cutting sweeps + per-module reads)

- **Concurrency / virtual threads:** `synchronized` in production (LTD-11 carrier pinning); single-writer actually single-writer; read-connection thread-confinement; checkpoint atomicity; bus delivery/backpressure races; double-close/double-abandon idempotency.
- **Crypto (highest stakes):** counter-nonce uniqueness + durability beyond the one §13.4 test (concurrent publishers on one scope? `dek_ref` parse with a colon-bearing `scope_id`?); the random-IV(secrets)/counter-nonce(payload) fence; **`identity` scope keyed but maps to zero MVP event types** — what if an event resolves there?; **null-cipher fail-closed** (encrypted scope + enabled + no cipher must throw, not write plaintext); machine-local-root threat-model honesty (partial INV-PD-03 — nothing over-claims "safe if stolen"); the **cold-start cipher warmup** (did it land?); GCM tag handling; key material never logged (LTD-15).
- **SQL / migrations:** `MigrationRunner.splitSqlStatements` emitting a trailing comment-only fragment as a statement is a **CONFIRMED** finding — record it + propose the one-line guard + sweep for siblings (other string-built SQL, any migration with a trailing comment, `prepareStatement` on multi-statement text).
- **Config parsing:** YAML safe-load; the AMD-71 `toRealPath` traversal guard; `!secret`/`!env`/`!include` resolution on **both** load and reload (the M6.2 write-path-leak class); schema-validation fail-closed.
- **Serialization round-trips:** the Jackson codecs; the `Expectation` tagged-union (exhaustive no-`default` switch); `AttributeValue` float-bit identity; the canonical-metadata serializer the (un-activated) chain will depend on — deterministic + dual-format-safe?
- **Event-sourcing invariants:** write-ahead persistence (INV-ES-04); per-entity `subject_sequence` monotonicity (per-entity, not global); `global_position` monotonicity; idempotent replay; `eventTime` vs `ingestTime` (never `Instant.now()` for `eventTime`).
- **JPMS / contract direction:** moduleGraphAssert passes — understand *why* (the seam patterns, the value-model leaf, qualified exports); confirm no exported type leaks a higher-layer domain type (the AMD-52/AMD-70 cycle class).
- **Reserved-but-unbuilt register** (design ≠ implementation; a consumer might wrongly rely on these): chain-hash **activation** (Doc 15 §3.3 — column exists, real computation NOT built); **Ed25519 signing** (§3.7 — not built); the **crypto-shred operation** (post-MVP); the **OR-M6-NONCE restore half** (R-α open); the **`identity` scope** (keyed, unpopulated); **`main()` runtime construction** (not wired). Catalog each with its doc reference + the premature-reliance risk.
- **Drift:** MODULE_CONTEXT vs source; stale design-doc currency (e.g., Doc 01 §14 still says hash-chaining "not implemented"); count/type pins that no longer match.

## Finding format, severity, disposition

Findings table per module: `ID | severity | type | file:line | issue (one line) | recommendation | disposition | tag`.
- **Severity:** BLOCKING (breaks a shipped contract / security hole / data-loss) · HIGH (real bug or strong test-weakness on a critical path) · MEDIUM (latent risk / moderate gap / misleading drift) · LOW (minor) · INFO/RESEARCH.
- **Type:** correctness · security · test-weakness · concurrency · serde · drift · forward-risk · research.
- **Disposition:** needs-coding-instruction · needs-claude-code-verification · needs-research-dispatch · needs-doc-fix · needs-Nick-decision · accept-as-is.
- **Tag:** [VERIFIED-FROM-SOURCE] or [HYPOTHESIS — NEEDS GATE] (+ the exact Claude Code check for the latter).

## Signal discipline (anti-noise — the converge depends on this)

A review that reports 200 findings is useless: it buries the five that matter and the converge drowns. **Optimize for signal — the findings that change what we do.** Concretely:

- **Materiality bar.** Report **individually only BLOCKING / HIGH / MEDIUM** findings. Roll **LOW + INFO + nits** into a single short "Minor observations" list per module (a one-line theme + count), never an enumeration. If a module yields only nits, say so in one line and move on — the coverage ledger proves you looked.
- **Every reported finding passes "so what / now what":** it names a concrete consequence **and** a disposition. A pure observation with no action is noise — roll it up or omit it.
- **De-duplicate within your session.** One root cause that recurs across modules is **one cross-cutting finding**, not five — report it once, list the sites.
- **Depth over breadth in reporting.** One well-evidenced, correctly-tagged finding beats five vague ones. A vague "this might be fragile" with no `file:line` and no consequence is noise — either sharpen it to a real finding or drop it.
- **The executive summary must stand alone** — the handful of findings that matter, the health verdict, the forward call. The per-module tables are reference, not the headline. Assume Nick reads only the exec summary unless a finding pulls him deeper.
- **Keep the document usable.** Tight, ranked, dispositioned. You are writing an input the converge will synthesize and Nick will act on — not a transcript of everything you read.

## Guardrails

- **Surface, do NOT fix.** No edits to production code, tests, or large governance files. Your only write is your audit deliverable (a clean new-file write).
- **Host Read tools only; no sandbox `git`.**
- **Source is truth** over any doc; disagreements are findings.
- **Calibrated honesty** on every finding; cite `file:line`.
- **Coverage ledger is the honesty contract** — every module in your scope earns at least a model+contract+test-strength pass and a ledger row. Depth-prioritize per the PRIORITY marks; if budget runs short, STOP cleanly and name the un-reviewed/light modules. Never fake coverage.
- **Stay in your lane** — review your assigned modules; build only as much model of out-of-scope dependencies as you need; the converge session merges A + B.
