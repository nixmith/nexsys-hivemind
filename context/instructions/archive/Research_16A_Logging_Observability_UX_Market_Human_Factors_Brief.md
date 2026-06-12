<!--
file: context/instructions/Research_16A_Logging_Observability_UX_Market_Human_Factors_Brief.md
purpose: Dispatchable research brief — Research 16-A: Logging & Observability UX: Market and Human Factors (community-evidence / UX-market register). Gap-relative to the Locked observability design (Doc 11 + Doc 07 §11 + Doc 13), the DAS voice/register standards, and the shipped script idiom (pi-health.sh at `01841ba`). One cycle object: ONE output-contract philosophy serving three consumers — end-users, developers/operators, and LLM agents.
audience: DOCS Project researcher (primary), PM (assessment), Nick (dispatch)
status: READY TO DISPATCH — authored 2026-06-12 (PM, Cowork) per the archived R16 session prompt. Runs SIMULTANEOUSLY with Research 16-B — REC ranges are partitioned; this brief is fully self-contained (never reference a sibling return).
dispatch-target: the DOCS Claude Project (homesynapse-core-docs connector). RQ1–RQ3 and RQ5 are web-evidence-heavy — WEB SEARCH IS REQUIRED. If the connector is unreachable mid-run, DECLARE it in §5 per the charter's connector-blind protocol and work from the embeds — do not reconstruct HomeSynapse facts.
rec-block: REC-186–200 (reserved; high-water at authoring = REC-185, the R14/R15 cycle; the sibling holds 201–215 — do not exceed 200)
baseline: homesynapse-core HEAD `01841ba` (scripts-only, on substantive `7c73c91` M6.2) · docs watermark AMD-93 (RATIFIED 2026-06-12) · projectionVersion 5 · event pins 55/24/36 · invariants 163/47
-->

# RESEARCH BRIEF: Research 16-A — Logging & Observability UX: Market and Human Factors

*Target: the Script Output Standard + the M12 observability evidence base + M10/M13 UI inputs + Doc 11 currency notes + M5-C superiority copy. Date: 2026-06-12.*

You are a market-evidence researcher for HomeSynapse Core, a local-first, event-sourced smart home runtime in Java 21 on Raspberry Pi-class hardware. Your Project custom instructions carry the `research_mode` charter — the quote-back discipline, the disposition-bucket method, the Mom-Test evidence hierarchy, register fences, verbatim external vectors, and the honesty-section obligation **apply in full and are not restated here**.

Every HomeSynapse output surface — the structured SLF4J logs, the named log events (Doc 07 §11.2 class), `config_error` payloads, the eventual M10/M13 UI surfaces, and the Pi script tooling — serves **three consumers**: the END-USER ("why did my light turn on?"), the DEVELOPER/OPERATOR, and LLM AGENTS that parse pasted output. This brief owns the **human half** of that triangle: what the market evidence says about logs, traces, error messages, and diagnostic UX that real users and operators can actually read, trust, and act on. Your task is NOT design. It is a **community-evidence and teardown gap analysis in the UX/market register**, mapped against ground HomeSynapse has already Locked or shipped, so the PM can route findings to the five landing zones above.

**The disposition table (§4b) is the load-bearing deliverable.** A finding without a disposition row is unusable. A "gap" that the Locked design already closes poisons the pipeline.

---

## 0. Quote-back gate [DO THIS FIRST]

Open your return by quoting back, **verbatim**: (a) the §0.2 script-idiom block (all three fenced sub-blocks); (b) the §0.3 Doc 07 §11.2 log-event name list (all 14 names, in order); (c) the §0.4 Register-C paragraph. If you cannot quote them, STOP and return INCOMPLETE. A return that fails the quote-back is discarded unread past §0.

## 0.1 Authoritative state (do not work from memory)

- homesynapse-core HEAD: **`01841ba`** (2026-06-12, scripts-only; substantive HEAD `7c73c91`, M6.2). On-disk amendment watermark **AMD-93** · `projectionVersion` **5** · event manifest pins **55 / 24 / 36**.
- **Doc 11 (Observability & Debugging) is LOCKED (2026-03-09).** Always-on JFR + structured logging + health aggregation; the causal chain as the primary diagnostic tool; trace reverse lookup ("why is this device in this state?") as the primary diagnostic query (Doc 11 §3.4, D-07); dynamic per-package log levels (§3.6). You measure the market against this — you never re-open it.
- **AMD-88..93 RATIFIED 2026-06-12.** AMD-92 fixed the automation event vocabulary: event types and payloads are **frozen ground** — no finding may propose event-vocabulary changes.
- The observability subsystem is **design-only** (no Phase-3 implementation yet — that is the M12 window this research feeds). The script layer (§0.2) is **shipped and gate-free**.
- Research numbering: this is **Research 16-A**, REC range **186–200**. A sibling brief runs simultaneously in the engineering register with its own range; you must not reference or anticipate it.

## 0.2 Embedded verbatim — the shipped script idiom (`scripts/dev/pi-health.sh` + `scripts/pi4-validation.sh` at `01841ba`)

This is the de-facto in-house output standard your teardowns benchmark against. Three sub-blocks, verbatim from source:

**(i) Severity-tag output helpers (both scripts):**

```bash
info()   { printf "${BLUE}[INFO]${NC}  %s\n" "$1"; }
ok()     { printf "${GREEN}[OK]${NC}    %s\n" "$1"; }
warn()   { printf "${YELLOW}[WARN]${NC}  %s\n" "$1"; }
fail()   { printf "${RED}[FAIL]${NC}  %s\n" "$1"; }
header() { printf "\n${BOLD}=== %s ===${NC}\n" "$1"; }
```

Color is TTY-gated — when stdout is not a terminal, every color variable is set to the empty string (`if [ -t 1 ]; then … else RED='' GREEN='' YELLOW='' BLUE='' BOLD='' NC=''; fi`), so piped/pasted output carries the `[OK]`/`[WARN]`/`[FAIL]` tags with no ANSI noise.

**(ii) Labeled `KEY:value` remote-data lines (pi-health.sh batched SSH collection):**

```bash
echo "HOSTNAME:$(hostname)"
echo "MEM_AVAIL:$MEM_AVAIL"
echo "THROTTLED:${THROTTLED#throttled=}"
```

parsed by `get_val() { echo "$REMOTE_DATA" | grep "^$1:" | head -1 | cut -d: -f2-; }`.

**(iii) The machine-parseable summary line (pi-health.sh exit paths):**

```bash
# Machine-parseable summary (agents parse pasted output on this line):
echo "READINESS:PASS"
```

on the all-checks-passed path (exit 0), and `echo "READINESS:FAIL:${FAILURES}"` on the failure path (exit 1). `pi4-validation.sh` adds the rest of the idiom: `--dry-run` (print the plan, do nothing), env-var configuration (`PI_HOST`, `PI_PROJECT_DIR`), `-h|--help` banners, and exit-code propagation from the remote run.

## 0.3 Embedded verbatim — the named-log-event precedent (Doc 07 §11.2, LOCKED)

"Key log events follow the structured JSON format per LTD-15 with correlation IDs linking to the Run trace." The 14 event names, with levels — quote this list back in §0:

`automation.run.started` (INFO) · `automation.run.completed` (INFO) · `automation.run.failed` (WARN) · `automation.run.skipped` (DEBUG) · `automation.command.dispatched` (DEBUG) · `automation.command.confirmed` (DEBUG) · `automation.command.timed_out` (WARN) · `automation.reload` (INFO) · `automation.conflict` (WARN) · `automation.disabled` (WARN) · `automation.trigger.duration.started` (DEBUG) · `automation.trigger.duration.expired` (DEBUG) · `automation.trigger.duration.cancelled` (DEBUG) · `automation.trigger.duration.limit_exceeded` (WARN)

Key fields are snake_case (`run_id`, `automation_id`, `triggering_event_id`, `duration_ms`, …). Every design doc defines its own §11.2 in this style (e.g., Doc 11 §11.2: `observability.health.transition`, `observability.jfr.recording_stalled`).

## 0.4 Embedded verbatim — the human-register floor (DAS Consolidated Reference §1.1)

> **Register C — Direct Neutral (UI).** *The system communicating state, action, resolution.* No self-reference (neither "HomeSynapse" nor "we"), minimal words, maximum clarity, never blames, never apologizes, never celebrates. Used for: error messages, status indicators, dialogs, tooltips, empty states, notifications.

The DAS also bans "oops/uh-oh", exclamation marks, and "simply/just/easily" everywhere. **The human-register floor already exists — your findings build on it, never rediscover it.** A finding that proposes "error messages should be calm and blame-free" scores ALREADY-COVERED.

## 0.5 Embedded — the decided/Locked ground your findings are gap-relative to

| # | Decided item | Status |
|---|---|---|
| 1 | **The cycle frame:** one output-contract philosophy, three consumers (end-user / operator / LLM agent), spanning Core logging AND script tooling | The research object — your RQ4 matrix makes it concrete |
| 2 | **Battlefield B3 (Explainability) is a named differentiator:** "A non-developer user can answer 'why did the porch light turn on at 3am?' by looking at the event trace in the UI." Its evidence base already includes the R14-A ledger-gap dossier and the no-trace-ring-buffer attestation (traces are log events assembled by `correlation_id`; the HA-class trace-eviction problem is structurally absent) | LOCKED strategy + assessed evidence — extend it, don't re-derive it |
| 3 | **Doc 11 Locked machinery:** always-on (never opt-in) diagnostics; causal chain as primary tool; reverse lookup as the primary diagnostic query; tiered compositional health with reason strings; per-package dynamic log levels; Prometheus/OTel/remote-shipping deferred post-MVP (§14); negative traces ("why DIDN'T it fire?") an open question with three options (§15 OQ1) | LOCKED — baseline, never an open question (OQ1's *evidence* is in scope; its *resolution* is not yours) |
| 4 | **Doc 13 (Web UI observability MVP) Locked surfaces:** three-level progressive disclosure (System Overview → Service Detail → Event Trace); trace timeline with domain color-coding; traffic-light health with WCAG-AA contrast choices | LOCKED design — UI findings land as M10/M13 INPUT, parked |
| 5 | **INV-TO-04 (verbatim):** "System logs must be structured (machine-parseable), contextual (include correlation IDs that trace from trigger event through automation evaluation to device command), and queryable through the UI for common diagnostic scenarios. A user investigating 'why did the lights turn on at 3 AM?' must be able to find the answer through the interface without grep." | Invariant — the bar every finding measures against |
| 6 | **`config_error` (Doc 06 §4.5):** one DIAGNOSTIC event per ERROR-severity validation issue; payload carries `path`, `severity`, `message`, `applied_default`, `trigger`; `ConfigIssue` carries an optional `yamlLine` | Shipped M6 surface — an existing error-payload exemplar |

---

## 1. Research questions (answer ALL five; community evidence per the charter's Mom-Test hierarchy)

### RQ1 — Smart-home logging/debugging pain catalog

What do Home Assistant, Hubitat, SmartThings, and Homey users and operators **actually** complain about — and more importantly, work around — in logs, traces, and debug UX? Installed workarounds outrank complaints outrank feature requests. Cover at minimum: log-diving as the de-facto HA debugging method (the INV-TO-04 failure mode it names); log noise and volume (what users filter, mute, or stop reading); trace/debug-view usability in practice (who actually uses HA automation traces, and where do they give up?); log access ergonomics (SSH-and-grep vs in-UI; what non-technical users do when told "check the logs"); operator habits (what third-party log viewers, dashboards, or add-ons people install — and which installed tools go unused). For each pain class: what happened (cited), what users DID, and the gap-relative verdict against §0.5 rows 2/3/5.

### RQ2 — Best-in-class teardowns from the broader dev-tools market

Where has output UX been engineered demonstrably well, and what transfers to a Pi-class smart-home runtime? Tear down at minimum: the **error-message grammar school** (Rust and Elm compilers: what-happened + why + what-to-do-next, span/context display, error codes with lookup); the **CLI excellence class** (the Tailscale / `gh` / `cargo` tier: status verbs, progressive verbosity, human summary + machine detail); **progressive disclosure** in diagnostic UIs; **severity and color conventions** — including the accessibility floor (never color-only semantics; `NO_COLOR`/TTY conventions; colorblind-safe palettes); **timestamp and locale discipline** (relative vs absolute, UTC vs local, ISO-8601 adoption); **noise budgets and log-level abuse** (WARN fatigue, everything-is-ERROR, the log-level inflation failure mode). Each teardown: the specific mechanism, ≥1 primary-source quotation with URL, and what it implies for a §0.5-anchored surface.

### RQ3 — The end-user register: plain-language causality

What does "readable logging" mean for a NON-technical smart-home user? The B3 claim (§0.5 row 2) requires a non-developer to answer the 3am question from a trace — that is a **prose register problem**, not just a data problem. Find the evidence: platforms or products that render event history as plain-language narrative (timelines, activity feeds, "X happened because Y") and how users respond; where syslog-register output is shown to laypeople and what happens; the vocabulary problem (entity IDs vs friendly names in user-facing surfaces); how much causality detail a non-technical user wants before it becomes noise. Verdict: what register/vocabulary rules should govern the end-user rendering of the SAME underlying events the operator sees raw — building on §0.4, never duplicating it.

### RQ4 — The per-audience needs matrix

The cycle's integrating deliverable (§3.2 of your return): for each output surface family (live log stream · named log events · error/validation messages · trace/causality views · health status · script/CLI output), what does each of the three consumers need — END-USER, OPERATOR/CONTRIBUTOR, LLM AGENT? You own the two human columns with evidence; for the agent column record only **market evidence visible in your register** (e.g., users pasting logs into ChatGPT/Claude and what breaks — a real, documentable behavior class) and leave engineering mechanics to the sibling register. Identify per row: where one well-designed surface serves all three, and where the evidence demands dual-channel output (human-pretty vs machine-stable). Verdict per row, anchored to §0.5.

### RQ5 — Anti-requirements: what demonstrably failed

The honest-negative catalog: over-colored walls of text; emoji-as-semantics in CLI/log output; vendor logging dashboards nobody reads; alert/notification fatigue; debug modes so verbose they bury the answer; "friendly" error messages that hide the actual error (the anti-Register-C failure); gamified or celebratory status UX in infrastructure tools. Each: cited evidence that it failed (user abandonment, maintainer reversal, community mockery — Mom-Test grade), and the REJECT-candidate or copy-guardrail it implies.

---

## 2. Mandatory document format

```
# Research 16-A: Logging & Observability UX — Market and Human Factors
*Target: HomeSynapse Script Output Standard + M12 evidence base + M10/M13 inputs +
 Doc 11 currency + M5-C copy. Date: YYYY-MM-DD.*

## 0. Quote-back gate [M — FIRST] — per §0 above.

## 1. Executive Summary [M] — 5–8 verdict bullets; every bullet takes a position with a
     one-sentence defense. "X is worth investigating" is banned. Flag the single
     highest-impact finding AND the single strongest B3-differentiator evidence item.

## 2. Deep Dives [M] — one subsection per platform/teardown target (RQ1 platforms +
     RQ2 exemplars; HA deepest among platforms). Each: (a) mechanism or failure,
     precisely; (b) ≥1 direct quotation from a primary source WITH URL; (c) what users
     DID (Mom-Test); (d) the gap-relative lesson, citing the §0.2–§0.5 anchor.

## 3. Cross-Cutting Analysis [M]
   - 3.1 Pain-class concept map: pain class | HA | Hubitat | SmartThings | Homey |
         best-in-class answer (RQ2) | HomeSynapse ground (cited §0.5 anchor).
   - 3.2 THE PER-AUDIENCE NEEDS MATRIX (RQ4) — the cycle's integrating table.
   - 3.3 The explainability-brand dossier (RQ3 + RQ1): the assembled evidence that
         plain-language causality is an unserved need and HomeSynapse's Locked ground
         already holds the data for it — or an honest finding otherwise. M5-C-grade.
   - 3.4 Over-engineering check: Locked observability machinery the human evidence
         says no one needs — defend or flag each (honesty section; REJECT-candidates).

## 4. Findings + Recommendations [M]
   - 4a. REC-numbered findings, REC-186 through at most REC-200, ranked
         (impact × confidence)/cost. Each REC: pain/teardown citation; evidence
         (≥1 primary source); gap-relative statement; concrete recommendation;
         effort class (S/M/L, prose).
   - 4b. THE DISPOSITION TABLE [M — load-bearing]: EVERY REC maps to EXACTLY ONE of:
           SCRIPT-STANDARD (lands in the planned scripts/dev/OUTPUT_CONVENTIONS.md —
             gate-free, immediately implementable)
         | M12-INPUT (evidence/obligation for the M12 observability milestone,
             INSIDE Locked Doc 11 contracts — a default, a register rule, a test)
         | M10-M13-INPUT (UI-surface input — parked, not drafted)
         | DOC-11-CURRENCY (a currency-note candidate on Locked text — never
             re-litigation; rides the next Doc-11-touching amendment)
         | M5-C-COPY (website/docs superiority material — the B3 story)
         | FUTURE (contract delta or post-MVP feature — sketch, do NOT draft)
         | REJECT (reasoned — evidence says HomeSynapse should NOT do this).
         No REC in two buckets. No bucket empty by laziness — if genuinely empty, say why.

## 5. Caveats and Open Questions [M] — source reliability; connector-blind declaration
     if applicable; explicit INCOMPLETE-EVIDENCE declaration if web reach was too shallow.

## 6. Appendix: Sources [M] — URL families grouped by platform/exemplar; every factual
     claim traceable.

## 7. HomeSynapse Code-Level Implications [LIGHT] — observations ONLY, routed through
     §4b. NO new types, NO contract drafts, NO event-vocabulary proposals. Exact
     §0.2/§0.3 identifiers only.
```

## 3. Evidence standards

The charter's standards apply in full (primary sources with URLs; Mom-Test hierarchy — installed workarounds > complaints > requests; 2+ independent reports or a maintainer statement for community claims; take positions, "worth investigating" is banned; no fabricated identifiers — HomeSynapse names come from §0.2/§0.3 verbatim or the connector, and if a fact is in neither, request it in §5). The charter's freshness horizons apply — date every source; smart-home platform behavior older than ~2 years must be flagged as possibly stale and re-verified where it carries a finding. Cycle-specific addition: **teardown claims about a tool's output behavior (RQ2) must cite the tool's own docs, source, or changelog — not a listicle.** Web search is required; declare INCOMPLETE-EVIDENCE rather than padding.

## 4. Guardrails (violations = the finding is discarded)

1. **Register fence: positioning/UX-market register — NO code obligations.** You may not mint implementation obligations, schema changes, or event-vocabulary changes. AMD-92's event vocabulary and Doc 11's architecture are frozen ground to measure against, never open questions. Findings route ONLY to the §4b buckets.
2. **No Doc 11 re-litigation.** "HomeSynapse should make traces queryable" is a discarded finding (§3.4/D-07 already do); a finding must identify a *specific human-factors delta* with evidence. Doc 11 §15 OQ1 (negative traces): your evidence on the "why didn't it fire?" need is welcome and routes to M12-INPUT — proposing the resolution is out of scope.
3. **Engineering mechanics are the sibling's register.** Structured-format selection (JSON Lines vs logfmt), agent-parseability engineering, correlation propagation internals: if you trip over strong evidence there, note it in §5 as out-of-register, one line, and move on.
4. **REC numbering: 186–200 ONLY** (append-only global register; the sibling owns 201–215; high-water 185).
5. **DAS compliance in your own copy-adjacent output:** any recommended user-facing wording must itself satisfy §0.4 and the DAS bans (no "oops", no exclamation marks, no "simply").
6. Produce ONE complete markdown document. Do not truncate.

## 5. What the PM does with the return (so you aim at it)

The PM runs the standard serialized A–F assessment, source-verified, then folds your disposition table with the sibling's into one merged pass (the R14/R15 machinery). Routes: SCRIPT-STANDARD rows → the new `scripts/dev/OUTPUT_CONVENTIONS.md` (pi-health retrofitted as reference implementation — gate-free); M12-INPUT rows → the M12 observability milestone's evidence base and instruction obligations; M10-M13-INPUT rows → the parked UI lane; DOC-11-CURRENCY rows → the currency-note queue; M5-C-COPY rows → the website/docs superiority backlog (joining the ledger-gap dossier, the no-ring-buffer attestation, and the no-templating-DSL structural-absence claims); FUTURE rows → Nick's queue; REJECTs → the anti-requirements register. Your §3.2 matrix and §3.3 dossier are the cycle's flagship deliverables — the matrix shapes the output-contract philosophy itself; the dossier feeds the B3 brand surface. A finding that cannot be placed in that machine is a finding you should sharpen or drop.
