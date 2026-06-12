<!--
file: context/handoff/2026-06-13_R16-logging-UX_brief-authoring_session_prompt.md
purpose: Next-PM-session brief — author the R16 research cycle (logging/observability output UX): two dispatch-ready briefs for the Claude Projects covering (A) the market/human-UX register and (B) the LLM-legible logging engineering register, on the R13–R15 brief pattern. The cycle's object: ONE output-contract philosophy serving three consumers — end-users, developers/operators, and LLM agents — across HomeSynapse Core logging AND the Pi script tooling.
audience: PM (next Cowork session), Nick
status: READY — authored 2026-06-12 post-ratification. MAY RUN PARALLEL to the Pi-evidence session (guardrail below).
-->

# Session Brief — R16 Brief-Authoring: Logging & Observability Output UX (human + LLM)

PM session (nexsys-project-manager skill). **Read `context/process/cowork-environment-model.md` FIRST.** Then the freshness preflight vs PINNED STATE — one glance per check.

## ⚠ PARALLEL-SESSION GUARDRAIL (read second)

The **Pi-evidence session (OQ-15-2)** may be IN FLIGHT in another Cowork conversation. Environment-model rule (b) applies in force: **no structural rewrites of shared hot-path files** (pm-handoff, cross-agent-notes, snapshot) while it may be open — this session's outputs are NEW FILES (two briefs + this archive move + an agenda append); tracker writes are **single-anchor appends only**, and if the Pi session has already written a 2026-06-12/13 record, append BELOW it, never reflow. If in doubt, defer the pm-handoff session record to the end and keep it to one paragraph.

## PINNED STATE (verified 2026-06-12 at authoring — trust, then spot-verify)

- **Shas:** core `01841ba` (scripts-only on `44bce4d`/`e5ea76f`; substantive `7c73c91`) · docs `d7ea212` · hivemind `7d23829`. All pushed. The Pi session may advance these — reconcile what you see, expect script/bench commits only.
- **Ratified ground:** AMD-88..93 + B2 C8/C9 RATIFIED; watermark **AMD-93**; invariants **163/47**; pins 55/24/36. M7 entry-gate rows 1–2+5 closed; row 3 (ordering) in flight via the Pi session + interviews; row 4 (M5-C Increment 1) open.
- **Research high-water: REC-185.** This cycle mints **R16-A = REC-186–200, R16-B = REC-201–215** (15 per brief, the standing pattern).
- **The Projects are research-ready:** both custom instructions carry the new `research_mode` charters (quote-back gate, disposition buckets, Mom-Test evidence hierarchy, register fences, verbatim external vectors, honesty sections) — **this cycle is their first full exercise; brief accordingly** (the briefs lean on the charters instead of restating them, but still embed the quote-back anchors per protocol).
- **Check 9 / index.lock:** verify per the standing answer key; neither blocks brief authoring.

## THE RESEARCH OBJECT (why this cycle exists)

Every HomeSynapse output surface — Core's SLF4J structured logs, the named log events (Doc 07 §11.2), `config_error` payloads, the eventual M10/M13 UI surfaces, AND the Pi script tooling (`pi-health.sh` etc.) — serves **three consumers**: the END-USER ("why did my light turn on?"), the DEVELOPER/OPERATOR (Nick today; contributors later), and **LLM AGENTS** (Claude Code/Cowork parse pasted script output and log excerpts as a primary workflow — the `pi-health.sh` `READINESS:PASS` line + labeled `[OK]/[WARN]/[FAIL]` idiom, shipped `44bce4d`, is the in-house precedent). The cycle researches how to make ONE output-contract philosophy serve all three, short- and long-term. Strategic hook: **Battlefield B3 (explainability) is a named differentiator** and the R14-A debuggability dossier is its evidence base — logging UX is brand surface, not plumbing.

## TASK (strict order)

1. **Step-0** (light): preflight glances; sha reconcile of whatever HEADs exist; archive this prompt when consumed.
2. **Read the ground (the embeds come from here — this is most of the session's reading):**
   - **Doc 11 (Observability & Debugging)** — the owning design doc; its log/metric/trace surfaces and §-anchors.
   - **Doc 07 §11.2** (named structured log events — `automation.cascade.depth_exceeded` etc.) + Doc 13 (Web UI observability MVP) skim.
   - **`DAS_Consolidated_Reference_v1.md`** — the voice/register standards (Register C error-message voice: no "we"/"sorry"/"please") — the human-register floor already exists; the briefs must build on it, not rediscover it.
   - **`scripts/dev/pi-health.sh` + `scripts/pi4-validation.sh`** — the current script idiom (`[INFO]/[OK]/[WARN]/[FAIL]`, labeled `KEY:value` remote-data lines, the `READINESS:` machine-parseable summary, `--dry-run`, env-var config). This is the de-facto in-house standard the research benchmarks against.
   - **Coder conventions:** SLF4J structured context keys (`entity_id`, `event_type`, `correlation_id` — review-and-quality §Code Quality); the environment-model §8 token-economics lesson (mega-lines defeat pagination — the same law governs log lines for agent consumers).
   - **Strategy hooks:** Six Battlefields B3 (file 1); the R14-A assessment §3.3 dossier + REC-145 (no-ring-buffer attestation); merged disposition §2e (M5-C backlog rows this research can strengthen).
   - **Invariants:** INV-ES-06 (every state change explainable), the TO category (§7), INV-MU-01 (attribution surfaces).
3. **Author R16-A — "Logging & Observability UX: Market and Human Factors" (DOCS Project venue; REC-186–200; UX/market register):** RQs spanning — (1) smart-home market pain: what do HA/Hubitat/SmartThings/Homey users and operators actually complain about in logs/traces/debug UX (the R14-A method: installed workarounds > complaints > requests); (2) best-in-class teardowns from the BROADER dev-tools market: the error-message grammar school (Rust/Elm: what-happened + why + what-to-do-next), CLI excellence (the Tailscale/gh/cargo class), progressive disclosure, severity/color conventions and no-color-only semantics (accessibility), timestamp/locale discipline, noise budgets and log-level abuse failure modes; (3) the END-USER register: what "readable logging" means for non-technical smart-home users (the B3 explainability surface — plain-language causality, not syslog); (4) per-audience needs matrix (end-user / operator / contributor); (5) anti-requirements (what failed: over-colored walls of text, emoji-as-semantics, vendor logging dashboards nobody reads). **Fence: positioning/UX register — no code obligations, no event-vocabulary changes (AMD-92 is frozen ground), no Doc 11 re-litigation; findings route to M12/M10/M13 inputs, Doc 11 currency notes, the scripts standard, and M5-C copy.**
4. **Author R16-B — "LLM-Legible Output Engineering: Structured Logging and Agent-Parseable Tooling" (DOCS Project venue, engineering register — CORE available for source-grounded follow-ups; REC-201–215):** RQs spanning — (1) structured-logging prior art with exact citations: OpenTelemetry log/trace semantic conventions, JSON Lines vs logfmt, systemd journal fields, SLF4J/MDC patterns — what's worth adopting for a Pi-class, local-first system (no OTel collector dependency — weigh cost honestly); (2) **the agent-consumer contract**: what makes CLI/log output reliably parseable by LLM agents — stable line-anchored keys, machine-parseable summary lines (the `READINESS:` precedent), dual-channel design (pretty TTY vs `--json`/`--kv` stream), bounded-output + tail-with-summary patterns (context-window economy), deterministic ordering, no ANSI/spinners in non-TTY, exit-code semantics; (3) correlation propagation: `correlation_id` from `CausalContext` through log lines → the trace-assembly story (logs and the event log tell ONE causal story — the §4.2 trace model is the spine, logging is its narration); (4) the named-log-event taxonomy (Doc 07 §11.2 style) generalized: a project-wide log-event naming convention proposal; (5) the SCRIPT-layer standard: codify the pi-health idiom into a written convention every future script follows (severity tags, KEY:value data lines, summary line, --dry-run, env config, agent-paste ergonomics). **Fence: engineering register — proposals land as a CONVENTION/STANDARD candidate + Doc 11/M12 inputs, NOT as amendments (nothing here touches frozen contracts; the scripts layer is gate-free and immediately implementable).**
5. **Both briefs:** the R13–R15 pattern verbatim — masthead with venue + REC range + register fence; §0 quote-back anchors (embed the pi-health idiom block + the Doc 07 §11.2 event names + the DAS Register-C rule as the quote-back set); mandatory disposition table with buckets (SCRIPT-STANDARD / M12-INPUT / M10-M13-INPUT / DOC-11-CURRENCY / M5-C-COPY / FUTURE / REJECT); honesty section + freshness horizons + Mom-Test hierarchy (the charters carry the definitions — cite, don't restate); web search required; connector-blind declaration protocol. Self-review ×2 each (the standing discipline).
6. **Research-agenda append** (single-anchor): the R16 cycle row (two briefs, REC ranges, venues, dispatch = Nick veto-or-default).
7. **Closeout (minimal-footprint per the guardrail):** one-paragraph pm-handoff append + cross-agent single-anchor append (Nick action: dispatch both briefs to the DOCS Project in separate fresh conversations; save returns to `context/instructions/` → returns to docs `research/returns/` per the standing flow); commit messages handed over.

## DELIVERABLE ROUTING (so the briefs aim at real landing zones)

Returns → serialized PM assessments → merged disposition (the R14/R15 machinery) → routes into: **(a) the Script Output Standard** (a new `scripts/dev/OUTPUT_CONVENTIONS.md` — immediately implementable, no gate; pi-health retrofitted as the reference implementation); **(b) Doc 11 currency notes + the M12 observability milestone's evidence base**; **(c) M10/M13 UI-surface inputs** (parked, not drafted); **(d) M5-C copy** (the B3 explainability story, strengthened); **(e) anti-requirements registered**. Nothing in this cycle amends frozen contracts.

## TOKEN DISCIPLINE

Doc 11 + DAS + the two scripts are the heavy reads — budget there. Do NOT re-read the AMD block, the review return, or the strategy files beyond the B3 section. The briefs are the precision items: exact §-anchors, verbatim embeds, tight RQs. The charters in the Projects' custom instructions carry the methodology — briefs cite it rather than restating (that's WHY we upgraded them).

## STANDING NICK-PACED ITEMS (surface, don't block on)

Pi-evidence session in flight (OQ-15-2 — its closeout owns the shared-file rewrite rights if both sessions are open) · energy/erasure interviews · M5-C Increment 1 (row 4; this cycle's returns strengthen its copy but DO NOT gate it) · D-1..D-7 vetoes · spike-dir `git rm` + DOCS-connector deselection advisory · FUTURE-AMD queue.
