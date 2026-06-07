<!--
file: context/handoff/2026-06-07_M5-D_evidence_session_prompt.md
purpose: Cowork session prompt — M5-D (evidence lane) of the M5 window, run in parallel with M5-A Part 2 (Claude Code). Doubles as the M5-A Part 2 WUCP Phase 2 review when the Coder output lands.
audience: PM (Cowork), Nick
-->

You are resuming as PM on NexSys / HomeSynapse Core. Invoke the
nexsys-project-manager skill and run the mandatory session-start freshness
preflight before anything else. Source-verify everything with the Read tool
against the actual repos (homesynapse-core, homesynapse-core-docs,
nexsys-hivemind); the in-sandbox git is not authoritative and commits go
through host git. Read pm-handoff.md and PROJECT_SNAPSHOT.md for the
authoritative state — do not work from any summary alone.

Frame: this is the **M5-D "evidence" lane** of the M5 window, running in
PARALLEL with M5-A Part 2 (the AMD-87 Expectation codec), which Claude Code is
executing separately from `context/coding-instructions/M5-A-Part2_AMD87_Expectation_Codec.md`.
You are the quality gate, not an executor: you AUTHOR the specs, guides, and
decision-support here; Nick (or hardware, or Claude Code) runs them. Do not
claim to run a Pi-4 benchmark or conduct interviews — produce the artifacts that
let Nick do so. STOP and raise anything that doesn't reconcile against source
rather than engineering around it.

Current state to internalize first (expect preflight PASS at HEAD `8028337`):
M5-A Part 1+3 committed `8028337`; the M5-window crypto + codec ratification is
COMPLETE — **Doc 15 (Cryptographic Architecture) is LOCKED**, **AMD-86** (INV-PD-07
narrow + INV-PD-03 at-rest posture) and **AMD-87** (Expectation codec) are
RATIFIED, on-disk amendment watermark **AMD-87**. M5-A Part 2 is un-gated and
with Claude Code. Open Risks of interest: **OR-M6-NONCE** (counter-nonce
crash/restore durability, [BLOCKING-for-M6-impl]) and **OR-M13-SDNOTIFY**
(sd_notify transport → M13).

Read before working M5-D:
  - `homesynapse-core-docs/design/15-cryptographic-architecture.md` (LOCKED) —
    esp. §2.3 (the D2 MVP/post-MVP line), §3.2 (write-path integration point),
    §3.4 (at-rest envelope encryption + the encrypted-scope set), §3.5/§12
    (the honest machine-local threat model), §9 (`crypto.encryption.encrypted_scopes`
    config), §10 (Performance Targets — the Pi-4 floor: AES-256-GCM ~30–60 µs/event,
    ≥500 ev/s sustained on sensitive scopes, **Pi-4 has no ARM crypto extensions**),
    §13.3/§13.4 (the perf + counter-nonce tests), §15 (Open Questions — OQ-15-2 is
    the microbench; OQ-15-1/3/4), §16 (Summary of Key Decisions).
  - `homesynapse-core-docs/design/amendments/AMD-86_INV-PD-07_Crypto-Shred-MVP-Scope_and_INV-PD-03_At-Rest-Posture.md`
    — esp. §3 (the **re-scope-up trigger**: the M5-D energy/institutional
    interviews carry the verifiable-erasure question; if a launch-window buyer
    requires it, AMD-86 is revisited BEFORE M6 freezes the write path) and the
    INV-PD-03 partial-at-MVP posture.
  - `nexsys-hivemind/context/decisions/2026-06-06_post-M4_M5-window_decisions.md`
    — D2 (crypto-shred POST-MVP, build infra/at-rest at MVP), D4 (energy
    shape-now-features-later), D5 (language spikes ride the window, window doesn't
    wait on the language call).
  - `nexsys-hivemind/context/audits/2026-06-06_M3-M4_foundation-readiness-assessment.md`
    — F2 (Expectation evaluate deferral) and F3 (backup/restore — the OR-M6-NONCE
    co-design counterpart).
  - The language-replatform context for the sd_notify spike:
    `nexsys-hivemind/context/assessments/2026-06-06_core-language-replatform-assessment.md`
    + `2026-06-06_rust-velocity-compounding-analysis.md` (the GraalVM native-image
    decision the sd_notify mechanism is entangled with).
  - The strategy layer for the erasure/energy interviews (use the `docx` skill for
    the `.docx` files): the data-readiness + revenue/institutional framing in
    `nexsys-hivemind/context/strategy/` (catalog in `strategic-context-map.md §2`).

The M5-D work — three deliverables, in priority order. Reason through each
against source; do not invent numbers or problems:

  1. **Pi-4 AES-256-GCM write-path microbench (resolves OQ-15-2) — PRIORITY; it
     has a Core-design feedback loop and gates the M6 write-path freeze.** Doc 15
     §3.4/§9 names the default encrypted set (identity + person-linked presence);
     §15.2/§16 say the *exact* category list is "tuned by the Lane D Pi-4
     microbench, with a category falling back to plaintext-at-rest only where Pi-4
     perf forces it." Produce a **runnable benchmark specification + decision
     criteria**: (a) exactly what to measure — per-event AES-256-GCM encrypt cost
     at the Doc 15 §3.2 write-path point on a Pi-4, with ARM-intrinsics-off
     reality (§10), warm/cold, against the projected write rates of each
     candidate sensitive-PII category; (b) the methodology (harness shape, JMH or
     a fixed-corpus timer, the JVM flags matching the Pi-4 deployment profile,
     how to source representative payload sizes); (c) the **decision rule** — the
     Pi-4 budget (the §10 ~30–60 µs/event + ≥500 ev/s-sustained envelope) that
     decides whether a category encrypts-on-write at MVP or falls back to
     plaintext-at-rest, stated as a pass/fail threshold per category; (d) what the
     result writes back into — the Doc 15 §9 `encrypted_scopes` list and the §3.4
     category set (this is a TUNING within the Locked design, NOT a Doc 15
     re-open). Note it RESOLVES OQ-15-2 and is a prerequisite for the M6 at-rest
     encryption WU. Do NOT re-open Locked Doc 15; if the microbench somehow
     implied a design change rather than a list-tuning, STOP and escalate.

  2. **Energy + erasure interview guide (the D2 re-scope-up trigger + D4 energy
     shape).** Produce a structured interview guide for the launch-window
     energy/institutional conversations: (a) the **verifiable-erasure questions**
     that determine whether a launch-window buyer requires operational
     crypto-shredding — the explicit AMD-86 §3 re-scope-up trigger that, if
     tripped, re-opens AMD-86 BEFORE M6 freezes the write path (frame the
     question so a "yes" is unambiguous and actionable); (b) the **energy-data
     questions** (D4 shape-now-features-later) — what energy event shape MVP must
     expose so the post-MVP energy features are non-breaking. For each question,
     state the decision it feeds and the threshold for action. Ground the framing
     in the strategy layer (data-readiness + institutional revenue), not invented
     personas.

  3. **sd_notify transport-mechanism spike / decision matrix (OR-M13-SDNOTIFY).**
     Pure OpenJDK 21 has no AF_UNIX SOCK_DGRAM (JEP 380 = stream only), so the
     real sd_notify transport is deferred to M13 behind the `NotifyTransport`
     seam. Produce a decision matrix comparing the two mechanisms — (a) a JNR/JNA
     native binding (needs a `libs.versions.toml` entry + approval; interacts with
     the GraalVM native-image decision), (b) a `systemd-notify` subprocess
     fallback (watchdog-PID caveats, process-per-heartbeat cost on a Pi) — with a
     PM recommendation and an explicit flag of the GraalVM entanglement (cite the
     language-replatform assessment). This informs M13 and the M5-D evidence call;
     no catalog dependency is added now.

Deliverables for the M5-D portion: the microbench spec + decision criteria
(written so Nick can run it on a Pi-4 and resolve OQ-15-2); the interview guide;
the sd_notify decision matrix + recommendation. Save each as a dated artifact
under the appropriate `nexsys-hivemind/context/` location, update the W24
charter's M5-D lane + the relevant Open Risks, and give Nick a commit message.
Run the WUCP-style closeout for the documents you produce.

— THEN, LATER IN THIS SESSION (when Nick pastes it): the M5-A Part 2 result —

When Nick pastes the **M5-A Part 2 (AMD-87 Expectation codec) Claude Code output
+ his build-gate result**, SWITCH to **WUCP Phase 2 review of Part 2** (re-run the
freshness preflight first if the codebase HEAD moved). Source-verify the codec
against the RATIFIED `AMD-87_Expectation_Persisted_Codec.md` §2 and the standalone
instruction `context/coding-instructions/M5-A-Part2_AMD87_Expectation_Codec.md`:
read every changed `.java` file against source (not the completion report) and
confirm — the tagged-union `{"t":…}` envelope keyed on the `Expectation`
*interface*; the exhaustive no-`default` switch over the four permits
(`ExactMatch(AttributeValue)` / `AnyChange(AttributeValue)` delegating `v` to the
existing `AttributeValue` codec, `EnumTransition(String)`, `WithinTolerance(double,
double)` reusing the AMD-52 bit-anchored-float helper); **AMD-87-INV-01** (per-permit
lossless round-trip + the un-`@Disabled` `capabilityAdded_onOff_roundTrips`
passing, decoding to the real event not `DegradedEvent`); the lone JPMS change
`persistence requires com.homesynapse.device` is acyclic; the `@Disabled("AMD-65
pending")` was deleted (not re-numbered) and the `TestEventSamples:315` AMD-65
Javadoc retired; no `@JsonTypeInfo` / domain annotations (Rule 10); no new
persisted shape / event-store migration / `projectionVersion` bump. Adjudicate any
deviations ([BLOCKING]/[REVIEW]/[INFO]) on first-principles correctness. Then run
the full **WUCP Phase 2 closeout across the six-file set** (PROJECT_SNAPSHOT,
pm-handoff, cross-agent-notes, coder-handoff, milestone-backlog, weekly) +
`core/persistence/MODULE_CONTEXT.md`, flip the M5-A Part 2 deferred build gate to
RESOLVED with the commit SHA Nick provides, run the dual-skill-mirror `diff -rq`
(Check 9), and give Nick the homesynapse-core + nexsys-hivemind commit messages.
With Part 2 committed + closed, M5-A is COMPLETE and the M9 command-bearing-
CapabilityAdded prerequisite is cleared — note that forward.

Throughout: source-verify, STOP on any mismatch, and keep Locked Doc 15
inviolate (the microbench tunes the encrypted-scope list within it; only the
erasure interviews can trigger an AMD-86 re-open, via the formal pipeline).
