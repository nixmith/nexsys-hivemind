<!--
file: context/handoff/2026-06-13_next-coding-instruction_session_prompt.md
purpose: Cowork PM session prompt — author the NEXT Core coding instruction (default target: M6.3 at-rest payload encryption, ISSUE-READY pending its gate), make the M6.3-vs-M7 ordering call explicit, and hand off the side-research candidates for the two Claude Projects.
audience: PM (Cowork), Nick
state-type: session prompt
status: READY (Nick dispatches as a fresh Cowork PM conversation)
pinned-state (2026-06-13): core substantive HEAD `7c73c91` (M6.2) / repo HEAD `824d6ba` (scripts/docs-only) · docs `8002b7e` · hivemind `5e4943a` · watermark AMD-93 · invariants 163/47 · projectionVersion 5 · `./gradlew check` GREEN (147)
-->

# Session Prompt — Author the Next Core Coding Instruction

**You are the PM (Mode 3, Director).** Your primary output this session is a single ISSUE-READY coding instruction for the Coder, per `project-manager/references/coding-instruction-format.md`. Default target: **M6.3 (at-rest payload encryption)** — the last open M6 piece. Authoring runs ahead of the gate (the binding constraint is Nick's evidence gate, not agent output); the instruction is authored now and *issued* only when its gate clears.

## Step 0 — Freshness preflight + pinned state (MANDATORY)

1. Run the full freshness preflight (`project-manager/references/freshness-preflight.md`).
   - **Expected result: PASS, except Check 9 STALE (skill-mirror sync pending).** The spine was reconciled 2026-06-13 (currency pass): watermark 87→93, B2 C8/C9 PROPOSED→RATIFIED, code counts refreshed (~803 files / ~2,002 tests / 22 subprojects). If the preflight shows the *old* watermark-87 / C8-C9-PROPOSED text as current, you are reading a pre-2026-06-13 copy — re-pull.
   - **Check 9 — mirror sync owed by Nick (3 files):** `project-manager/SKILL.md`, `project-manager/references/coding-instruction-format.md` (a pre-existing unmirrored edit), `coder/SKILL.md`. Confirm Nick has run the `diff -rq` sync before relying on the read-only skill mirror; the writable source under `ClaudeFolder/nexsys-hivemind/` is authoritative.
2. Pin SHAs at session start and reconcile: core substantive `7c73c91` / repo `824d6ba`; docs `8002b7e`; hivemind `5e4943a`. Truncated-tail mount artifact may be ACTIVE — host file tools (Read/Edit/Write) authoritative for every write; never VM read-modify-write of governance worktree files.
3. **Read before authoring:** the reconciled `PROJECT_SNAPSHOT.md` masthead + Current Work Unit; `pm-handoff.md` masthead (the 2026-06-13 RECONCILED banner + Open Risks **OR-M6-NONCE**); Doc 15 (Cryptographic Architecture) **§3.4 (counter-nonce), §6 (failure modes), §7.3 (one-key-system), §8.2, §13.4 (testing strategy), §9 (`encrypted_scopes`)**; `Architecture_Invariants_v1.md` §35 (AMD-86-INV-01) + the at-rest posture; and the M6.2 surface in `core/configuration/MODULE_CONTEXT.md` + `core/persistence/MODULE_CONTEXT.md`. Verify all cited type signatures against source (Step-3 discipline; embed the actual `module-info.java` text for every touched module — the Research-6 lesson).

## The ordering call (resolve at the top of session; escalate to Nick)

Both M6.3 and M7.1 are **interview-gated** (the energy/erasure interviews gate M6.3's write-path freeze *and* M7 entry-gate row 3). Present Nick this decision package, then proceed on his ruling (default = the PM recommendation):

- **PM recommendation — author M6.3 ISSUE-READY now.** It is the last M6 piece; its remaining evidence gate is a *no-trigger confirm* (per the W24 plan, M6.3 proceeds on the no-trigger assumption, with the write-path freeze held only until the interviews confirm "no operational-erasure requirement" — a "no" loses nothing, the categories are encrypted-on-write regardless). Authoring ahead of the interview gate is the standard play and costs nothing if the interview later re-opens AMD-86 (the guardrail re-opens it *before* the write path freezes).
- **Alternative — M7.1.** Only if Nick rules to defer M6.3's write-path freeze and open automation first. M7.1's contracts (AMD-88..93) are ratified and binding; but row 3 (interviews) + row 4 (M5-C approve) still gate the *issue*, so it's no less gated than M6.3.
- **Non-interview-gated fallbacks (if Nick wants Core motion with zero gate exposure):** (a) the REC-204 stderr retrofit of `pi-health.sh` / `pi4-validation.sh` / the OQ-15-2 driver + the F1/F3 `pi4-validation.sh` Git-Bash fix (small, queued advisory); (b) an M5-D spike (GraalVM native-image C15 / Gen-ZGC-vs-G1 C16) — Coder-authored throwaway, Nick-run, feeds the LTD-01 ledger. These keep the pipeline moving without touching the gated path.

## Primary task — the M6.3 coding instruction (must carry, verbatim where noted)

Author per `references/coding-instruction-format.md`. Non-negotiable contents:

1. **The M6.2 surface M6.3 builds on** (verify signatures against source): `ScopeKeyManager.encrypt/decrypt`; the `Main.payloadCipher(Path, Clock)` factory; the `HomeSynapseCore` 5-arg ctor with the **nullable** `PayloadCipher` (held-not-consumed since M6.2); persistence `PayloadCipher`/`EncryptedPayload` (java.base-only). **R-2 from M6.2 stands: extending the frozen `PersistenceFactory` gateway to forward the cipher IS M6.3's wiring step** — that is expected, not a Phase-2-interface change.
2. **The confirmed scope set:** `encrypted_scopes` default `[identity, presence_personal]` (OQ-15-2 RESOLVED 2026-06-12; disposition in `context/assessments/`). Encrypt-on-write for these scopes only; everything else stays plaintext (Doc 15 §3.4 PII grounds).
3. **OR-M6-NONCE (embed verbatim from `pm-handoff.md` Open Risks; [BLOCKING-for-M6-impl]):** the per-scope 96-bit GCM counter-nonce must be **durable and strictly monotonic across crash AND restore**. (a) persist the per-scope counter high-water mark atomically with — or ahead of — the encrypted write, and re-init from the persisted max on boot, never from memory; (b) co-design with the deferred backup/restore (foundation-readiness F3) so a restore can never resume a scope at a counter ≤ any value already used under that DEK (rotate the DEK on restore, or carry the high-water mark in the backup). **Close condition: the Doc 15 §13.4 kill-mid-encrypt nonce-monotonicity test GREEN.** Keep the random-IV-here (M6.2 secrets) / counter-nonce-there (M6.3 payloads) fence explicit.
4. **Cold-start cipher-warmup beat** (M6.3 scoping input from the Pi-evidence session): first ~100 encrypts after JVM start cost 80–700 µs (first op ~2–3 ms) as C2 compiles the software-AES path — add a `JacksonWarmup`-style cipher warmup so the write path isn't cold on first use.
5. **Tense-truth:** at-rest payload encryption is ratified *design* (Doc 15 LOCKED); M6.3 is the *implementation*. No copy/claim drift.
6. **MODULE_CONTEXT reads** for `configuration`, `persistence`, `lifecycle`, `app` in the "Files to Read"; the **§4c Clock-injection reminder** as **corrected 2026-06-13** (it is a self-enforced convention outside app's own tests — the gate only catches app-visible classes; do not assert the rule reaches non-app test code).
7. **Done-when:** instruction is ISSUE-READY on disk (NOT issued — gate-held per the ordering call); when issued and implemented: full `./gradlew check` GREEN + the §13.4 nonce-monotonicity test passing + PM WUCP Phase 2 APPROVE. Carry the deferred-build-gate tracking discipline.

## Side-research highlight (hand off — see the companion candidates doc)

Surface, do not solve this session: the open technical questions worth side-research in the two Claude Projects are enumerated in **`context/planning/2026-06-13_side-research-candidates_CORE-DOCS.md`**. The two most adjacent to M6.3's neighborhood: (a) **crash-safe backup/restore for an event-sourced + per-scope-encrypted store** (the F3 co-design OR-M6-NONCE leans on — a DOCS-Project design-research candidate); (b) the **C15 GraalVM native-image spike** (entangled with OR-M13-SDNOTIFY transport — a CORE spike). Confirm with Nick which to dispatch; nothing here blocks authoring M6.3.

## Guardrails

M6.3 stays inviolate behind its gate until Nick says go; Locked docs + ratified AMD-88..93 inviolate; OR-M6-NONCE embedded verbatim; **no scope creep** — the §4c reach decision (whitelist module test source sets vs. extend the app ArchUnit run) does NOT fold into M6.3, it rides the next app-module-touching WU. Single-anchor appends to shared files; the 2026-06-14 W25-rollover converge session owns the masthead/rollover synthesis. Commit messages handed to Nick (`!`-free, plain `-m`, or `git commit -F <file>`).
