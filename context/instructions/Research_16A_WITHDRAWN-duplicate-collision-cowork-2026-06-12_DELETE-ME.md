<!--
file: context/instructions/Research_16A_Logging_Observability_UX_Brief.md
purpose: Dispatchable research brief — Research 16-A: Logging & Observability UX: Market and Human Factors (market/UX register). Gap-relative to the Locked Doc 11 surface, the DAS Register-C voice floor, the shipped pi-health script idiom, and the ratified AMD-92 event vocabulary. One output-contract philosophy, three consumers: end-users, developers/operators, LLM agents.
audience: DOCS Project researcher (primary), PM (assessment), Nick (dispatch)
status: READY TO DISPATCH — authored 2026-06-12 (PM, Cowork) per the R16 brief-authoring session prompt. Runs SIMULTANEOUSLY with Research 16-B — REC ranges are partitioned; this brief is fully self-contained (never reference a sibling return).
dispatch-target: the DOCS Claude Project (homesynapse-core-docs connector). RQ1/RQ2/RQ3/RQ5 are web-evidence-heavy — WEB SEARCH IS REQUIRED. If the connector is unreachable mid-run, DECLARE it per your research_mode charter, work strictly from this brief's embeds, and reconstruct nothing. Fallback if web reach proves too shallow: return what you have marked INCOMPLETE-EVIDENCE per §3 — the PM splits evidence-gathering to a generic deep-research run; the disposition pass is NEVER the generic run.
rec-block: REC-186–200 (reserved; high-water at authoring = REC-185, Research 15; the sibling holds 201–215 — do not exceed 200)
baseline: homesynapse-core HEAD `01841ba` (scripts-only, atop substantive HEAD `7c73c91`/M6.2 and docs-only `e5ea76f`) · docs `d7ea212` · amendment watermark **AMD-93** (AMD-88..93 + B2 C8/C9 RATIFIED 2026-06-12) · invariants 163/47 · projectionVersion 5 · event pins 55/24/36 on disk (AMD-92's raises land at M7 implementation, not yet in source)
-->

# RESEARCH BRIEF: Research 16-A — Logging & Observability UX: Market and Human Factors

*Target: the Script Output Standard + M12 observability evidence base + M10/M13 UI inputs + Doc 11 currency + M5-C website/docs superiority material. Date: 2026-06-12.*

You are a market-evidence researcher for HomeSynapse Core, a local-first, event-sourced smart home runtime in Java 21. Every HomeSynapse output surface — the structured SLF4J logs, the named log events, `config_error` payloads, the eventual UI surfaces, and the developer script tooling — serves **three consumers at once**: the END-USER ("why did my light turn on?"), the DEVELOPER/OPERATOR, and **LLM AGENTS** that parse pasted script output and log excerpts as a primary workflow. Your task is NOT design. It is a **market and human-factors evidence pass in the Mom-Test register**: what do real users and operators suffer in smart-home logging/trace/debug UX, what does the broader dev-tools market's best-in-class output design actually look like (with the mechanism, not the vibe), and what does "readable logging" mean for a non-technical smart-home user — so the PM can route findings into one coherent output-contract philosophy.

Strategic hook you are feeding: **Battlefield B3 (explainability) is a named HomeSynapse differentiator** — "A non-developer user can answer 'why did the porch light turn on at 3am?' by looking at the event trace in the UI." Logging UX is brand surface, not plumbing. The R14-A debuggability dossier is B3's evidence base; this cycle extends it from automation traces to the whole output surface.

**The disposition table (§4b) is the load-bearing deliverable.** A finding without a disposition row is unusable. A "gap" that is actually covered by Locked machinery you didn't read poisons the pipeline.

---

## 0. Quote-back gate [DO THIS FIRST]

Open your return by quoting back, **verbatim**: (a) the §0.2 pi-health idiom block (all four fenced excerpts); (b) the §0.3 Doc 07 §11.2 event-name list (all 12 names); (c) the §0.4 DAS Register-C rule (both quoted passages). If you cannot quote them, STOP and return INCOMPLETE. A return that fails the quote-back is discarded unread past §0. (Your Project instructions' research_mode charter defines why this gate exists — it is the admission gate and the anti-fabrication anchor.)

## 0.1 Authoritative state (do not work from memory)

- homesynapse-core HEAD **`01841ba`** (2026-06-12, scripts-only — pi-health.sh; substantive HEAD remains `7c73c91`, M6.2). Docs HEAD **`d7ea212`**; on-disk amendment watermark **AMD-93**; invariants register 163 invariants / 47 LTD-class rows; event manifest pins **55 / 24 / 36** on disk.
- **AMD-92 (automation event vocabulary) is RATIFIED frozen ground.** Its event mints/reshapes land at M7 implementation. You may not propose event-vocabulary changes of any kind.
- **Doc 11 (Observability & Debugging) is LOCKED (2026-03-09).** It is your gap-relative baseline, never an open question. Findings about Doc 11 route as DOC-11-CURRENCY notes (staleness/superiority observations), not redesign.
- Research numbering: this is **Research 16-A**, REC range **186–200**. Research 16-B (engineering register) runs simultaneously with range 201–215; you must not reference or anticipate it.
- Your venue's research_mode charter (in the Project custom instructions) carries the standing methodology — the Mom-Test evidence hierarchy, freshness-horizon dating, source-reliability grading, the honesty-section requirement, register fences, verbatim-external-vector quoting. This brief cites those disciplines rather than restating them; they are all in force and graded.

## 0.2 Embedded verbatim — the shipped script idiom (`scripts/dev/pi-health.sh` at `01841ba`)

This is the de-facto in-house output standard your market evidence is benchmarked against. Four excerpts, verbatim:

**(a) Severity-tagged output helpers (lines 41–45):**

```bash
info()   { printf "${BLUE}[INFO]${NC}  %s\n" "$1"; }
ok()     { printf "${GREEN}[OK]${NC}    %s\n" "$1"; }
warn()   { printf "${YELLOW}[WARN]${NC}  %s\n" "$1"; }
fail()   { printf "${RED}[FAIL]${NC}  %s\n" "$1"; }
header() { printf "\n${BOLD}=== %s ===${NC}\n" "$1"; }
```

**(b) TTY-conditional color (lines 27–36) — ANSI only when stdout is a terminal:**

```bash
if [ -t 1 ]; then
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    YELLOW='\033[1;33m'
    BLUE='\033[0;34m'
    BOLD='\033[1m'
    NC='\033[0m'
else
    RED='' GREEN='' YELLOW='' BLUE='' BOLD='' NC=''
fi
```

**(c) Labeled `KEY:value` remote-data lines (the batched-SSH parse contract, lines 120–121, 130, 137, 164):**

```bash
# Gather all diagnostic data in a single SSH call to minimize round trips.
# Each value is emitted on a labeled line for reliable parsing.
echo "HOSTNAME:$(hostname)"
echo "MEM_TOTAL:$MEM_TOTAL"
echo "THROTTLED:${THROTTLED#throttled=}"
```

**(d) The machine-parseable summary line + exit-code contract (lines 434–436, 441–443):**

```bash
    # Machine-parseable summary (agents parse pasted output on this line):
    echo "READINESS:PASS"
    exit 0
    # ... failure path:
    echo "READINESS:FAIL:${FAILURES}"
    exit 1
```

Companion script `scripts/pi4-validation.sh` shares the helpers and adds `--dry-run` (validate config, print the plan, do nothing) and env-var configuration (`PI_HOST`, `PI_PROJECT_DIR`) with defaults.

## 0.3 Embedded verbatim — the named structured log events (Doc 07 §11.2 style, the project's event-naming idiom)

From Locked Doc 07 §11.2 (lines :938–:951) and §3.7.1 (:347) — dot-separated `subsystem.noun.verb` names, each with a level and a fixed key-field set:

`automation.run.started` · `automation.run.completed` · `automation.run.failed` · `automation.run.skipped` · `automation.command.dispatched` · `automation.command.confirmed` · `automation.command.timed_out` · `automation.trigger.duration.started` · `automation.trigger.duration.expired` · `automation.trigger.duration.cancelled` · `automation.trigger.duration.limit_exceeded` · `automation.cascade.depth_exceeded`

Doc 11 §11.2 carries the same idiom for the observability subsystem itself (e.g., `observability.health.transition` at INFO/WARN/ERROR by target status; `observability.jfr.recording_stalled`; `observability.trace.partial_result`). Every subsystem's design doc defines its own §11.2 table. This naming convention is established practice; your register may assess how it lands with humans, but its generalization into a project-wide convention is the SIBLING research's job.

## 0.4 Embedded verbatim — the DAS Register-C voice floor (`governance/DAS_Consolidated_Reference_v1.md` §1.1, §2.1)

> **Register C — Direct Neutral (UI).** *The system communicating state, action, resolution.* No self-reference (neither "HomeSynapse" nor "we"), minimal words, maximum clarity, never blames, never apologizes, never celebrates. Used for: error messages, status indicators, dialogs, tooltips, empty states, notifications.

> | Something went wrong | [describe what happened] | error, oops, uh-oh, something went wrong |

The human-register floor for error/status voice ALREADY EXISTS and is canonical governance. Your findings must build on it — e.g., what grammar/structure best-in-class error output adds on top of a neutral voice — never rediscover or contradict it. ("Never apologizes" is settled; do not return evidence that apologetic error copy tests well.)

## 0.5 The decided/Locked ground your findings must be gap-relative to

| # | Ground | What it already answers | Status |
|---|---|---|---|
| 1 | Doc 11 §0–§1, §3.4, §4.2 | The causal-chain trace is the primary diagnostic tool; reverse lookup ("why is this device in this state?") is the primary query; five query patterns; completeness detection with 30s/300s thresholds; competitive gap already documented (no surveyed platform answers "why?" end-to-end) | **LOCKED** |
| 2 | Doc 11 §3.6, D-11 | Per-package dynamic log levels at runtime via REST/UI (no CLI required), `com.homesynapse.*` prefixes only, non-persistent | **LOCKED** |
| 3 | LTD-15 | SLF4J → Logback → JSON lines to file; console plain-text via systemd journal; mandatory `correlation_id`/`entity_id`/`integration_id` MDC fields; rotation 50 MB/day, 500 MB cap; no Prometheus/OTel in MVP | **LOCKED** |
| 4 | INV-ES-06, INV-TO-01..04 | Every state change explainable; behavior observable; logs structured, contextual, **queryable through the UI without grep**; INV-MU-01 reserves identity-aware attribution surfaces | **Invariants** |
| 5 | DAS Register C (§0.4) + banned-pattern list | Error-message voice floor; "oops"-class copy banned; specificity principle (claims carry mechanisms) | **Canonical** |
| 6 | The pi-health idiom (§0.2) | Severity tags, TTY-conditional color, labeled data lines, machine summary, exit codes | **Shipped `44bce4d`/`01841ba`** |
| 7 | B3 (Six Battlefields §3) | The explainability claim and demo ("porch light at 3am" answerable by a non-developer in the UI) | **Strategy, named differentiator** |
| 8 | R14-A returns (REC-141..155, assessed) | The automation-specific debuggability dossier, the no-trace-ring-buffer attestation (REC-145), event-sourced-explainability pain citations (REC-182) | **Assessed + merged** |

"HomeSynapse should add causal tracing" is a FAILED finding — row 1 already owns it. Useful findings identify *specific deltas*: a presentation grammar, a per-audience disclosure rule, a noise-budget norm, an anti-requirement — with evidence.

---

## 1. Research questions (answer ALL five; market/human evidence, Mom-Test standard)

### RQ1 — Smart-home market pain: logs, traces, and debug UX

What do **Home Assistant, Hubitat, SmartThings, Homey** (and openHAB/Node-RED where evidence is strong) users and operators actually suffer in logging/trace/debug output? Apply the R14-A method: **installed workarounds > complaints > feature requests.** Cover at minimum: log-volume overwhelm and signal-to-noise (what do users filter, grep, or give up on); the "log diving" barrier for non-developers (B3's foil); trace/history eviction pain (the HA recorder/history class); per-integration log-level juggling; what third-party tools users bolt on (log viewers, dashboards, parsers) and what THAT reveals about the native surface's failure. For each pain class: what happened (cited), who suffers it (end-user vs operator), and the gap-relative verdict against §0.5 (does the Locked surface structurally close it, partially close it, or not address it — cite the row).

### RQ2 — Best-in-class output design across the broader dev-tools market

Teardowns, with mechanisms: (a) **the error-message grammar school** — Rust and Elm compiler diagnostics (what-happened + why + what-to-do-next structure, span highlighting, error codes with explainers); (b) **CLI output excellence** — the Tailscale/`gh`/`cargo` class: status verbs, progressive disclosure (`-v` tiers), summary-first composition, color/symbol conventions; (c) **severity and color semantics** — cross-tool conventions, and the accessibility rule that color must never be the only carrier of meaning (cite WCAG-grade or tool-documented practice); (d) **timestamp and locale discipline** — ISO 8601 vs relative time, UTC vs local, what bites users; (e) **noise budgets and log-level abuse** — documented failure modes of INFO-spam, WARN-that-means-nothing, and alert fatigue norms. Every teardown names the mechanism precisely enough that an engineer could replicate it, and quotes the source's own wording for load-bearing vectors (your charter's verbatim-vector rule).

### RQ3 — The END-USER register: what "readable logging" means for non-technical users

B3's claim is that a non-developer answers "why did the porch light turn on at 3am?" from the UI. What does the evidence say about presenting **plain-language causality** to non-technical users — not syslog with friendlier fonts? Cover: natural-language event narration attempts (any platform/product that renders machine events as human sentences — smart-home or adjacent consumer products); what non-technical users actually understand of severity/level vocabulary; causality presentation (chains, timelines, "because" phrasing) vs raw chronology; where plain-language rendering has FAILED (over-simplification that destroyed diagnostic value, or uncanny/wrong narrations that destroyed trust). Gap-relative spine: Doc 11 §4.2's TraceChain already stores the causal tree; the question is the human rendering layer's grammar, and the evidence for/against specific renderings.

### RQ4 — The per-audience needs matrix

Synthesize RQ1–RQ3 into a needs matrix for the three consumers: **end-user / operator (Nick today, contributors later) / LLM agent** — per output surface (UI trace view, structured log file, console/journal output, script output). For each cell: what that audience needs the surface to do, the evidence line that supports it, and where the needs CONFLICT (e.g., end-user brevity vs operator completeness vs agent parseability). Conflicts are first-class findings — the PM needs to know where one output contract cannot serve all three without explicit dual-channel or disclosure-tier design. (Flag the implication; the engineering mechanism is the sibling's register.)

### RQ5 — Anti-requirements: what failed

The reasoned REJECT catalog (your charter makes anti-requirements first-class). Document with evidence: over-colored walls of text; emoji-as-semantics in logs/CLIs (and where symbols DO work — the distinction matters); vendor logging dashboards nobody reads (cited abandonment/disuse evidence); log UIs that demo well and fail in anger; gamified or personality-laden system output that aged badly; any platform's attempt at "friendly logs" that users turned off. Each anti-requirement: the failure mechanism, its structural cause, and the explicit boundary (what nearby thing is still GOOD — e.g., severity color per §0.2(b) is in-house practice; the anti-requirement is color-as-sole-carrier or color-noise, not color).

---

## 2. Mandatory document format

```
# Research 16-A: Logging & Observability UX — Market and Human Factors
*Target: HomeSynapse Script Output Standard + M12 + M10/M13 + Doc 11 currency + M5-C. Date: YYYY-MM-DD.*

## 0. Quote-back gate [M — FIRST] — per §0 above.

## 1. Executive Summary [M] — 5–8 verdict bullets; every bullet takes a position with a
     one-sentence defense. "X is worth investigating" is banned. Flag the single
     highest-impact finding AND the single strongest B3-supporting evidence item.

## 2. Evidence Deep Dives [M] — one subsection per platform/tool family studied
     (smart-home platforms per RQ1; dev-tools exemplars per RQ2). Each: (a) how it
     solves/fails the RQ families; (b) ≥1 direct quotation from a primary source WITH
     URL; (c) what users DID (Mom-Test); (d) the gap-relative lesson, citing the §0.5
     row it is relative to.

## 3. Cross-Cutting Analysis [M]
   - 3.1 Pain-class concept map: class | HA | Hubitat | SmartThings | Homey |
         HomeSynapse (Locked mechanism, cited §0.5 row).
   - 3.2 The error-message grammar distillation (RQ2a): the structural elements
         best-in-class diagnostics share, each with its source exemplar.
   - 3.3 The per-audience needs matrix (RQ4) — including the conflict register.
   - 3.4 The B3 dossier extension: assembled evidence that plain-language causality
         for end-users is an unserved market need — or an honest finding that it isn't.
   - 3.5 Over-engineering check: Locked observability machinery NO surveyed market
         actually demands — defend or flag each (honesty section; REJECT-candidates).

## 4. Findings + Recommendations [M]
   - 4a. REC-numbered findings, REC-186 through at most REC-200, ranked
         (impact × confidence)/cost. Each REC: pain/exemplar citation; evidence
         (≥1 primary source); gap-relative statement (§0.5 row); concrete
         recommendation IN THIS REGISTER (presentation/copy/disclosure/standard
         content — never a type, event, or contract); effort class (S/M/L, prose).
   - 4b. THE DISPOSITION TABLE [M — load-bearing]: EVERY REC maps to EXACTLY ONE of:
           SCRIPT-STANDARD (content for the written script-output convention —
             tone, severity vocabulary, disclosure norms; the mechanism side is the
             sibling's)
         | M12-INPUT (evidence for the M12 observability milestone's implementation
             choices inside Locked Doc 11 contracts)
         | M10-M13-INPUT (REST-API/Web-UI surface inputs — parked, not drafted)
         | DOC-11-CURRENCY (a dated currency/superiority note on the Locked doc —
             never a redesign)
         | M5-C-COPY (website/docs superiority material — the B3 story)
         | FUTURE (post-MVP lane, incl. anything needing a contract delta — do NOT
             draft it)
         | REJECT (reasoned anti-requirement — first-class).
         No REC in two buckets. No bucket empty by laziness — if genuinely empty, say why.

## 5. Caveats and Open Questions [M] — per your charter: source-reliability grading,
     freshness horizons on load-bearing claims, findings AGAINST our design, explicit
     INCOMPLETE-EVIDENCE declaration if web reach was too shallow, connector-blind
     declaration if the docs connector was unreachable.

## 6. Appendix: Sources [M] — URL families grouped by platform/tool; every factual
     claim traceable.
```

## 3. Evidence standards (non-negotiable)

Your Project instructions' research_mode charter governs in full: primary sources with URLs and dates; the Mom-Test hierarchy (installed workarounds and shipped hacks outrank feature requests outrank forum opinions; maintainer scope statements are gold-grade); 2+ independent reports or a maintainer statement for community claims; verbatim quoting of external vectors; freshness horizons; per-claim reliability grading; a REJECT bucket as a first-class deliverable; the honesty section. Two brief-specific additions:

1. **Take positions.** Every section concludes with a verdict. "Worth investigating" is banned.
2. **Gap-relative or it didn't happen.** Every finding cites its §0.5 row. Findings that re-propose Locked machinery score ALREADY-COVERED inside the relevant bucket's narrative and are not recommendations. **Web search is required**; if reach is too shallow, declare INCOMPLETE-EVIDENCE in §5 rather than padding.

## 4. Guardrails (violations = the finding is discarded)

1. **Register fence: positioning/UX.** No code obligations of any kind — no type names, no milestone-numbered engineering items, no event names minted, no module or schema talk. Where a finding implies a mechanism, flag the implication in prose and let the PM route it (the sibling research owns the engineering register). Structured-logging formats, parser contracts, and correlation propagation are OUT of your register entirely.
2. **AMD-92 is frozen ground.** No event-vocabulary changes, additions, or renames — the ratified vocabulary and the Doc 07/Doc 11 §11.2 tables are baselines to measure presentation against, never proposals to amend.
3. **No Doc 11 re-litigation.** The trace model, health tiers, JFR posture, and dynamic-log-level design are LOCKED. Deltas route as DOC-11-CURRENCY notes or FUTURE — never as redesign findings.
4. **The DAS Register-C floor is settled** (§0.4). Build on it; never contradict it.
5. **REC numbering: 186–200 ONLY** (append-only global register; the sibling owns 201–215; high-water 185).
6. Produce ONE complete markdown document. Do not truncate.

## 5. What the PM does with the return (so you aim at it)

The PM runs the standard serialized assessment, source-verifies citations, and folds your disposition table into the R16 merged pass alongside the sibling: SCRIPT-STANDARD rows → the written script-output convention (`scripts/dev/OUTPUT_CONVENTIONS.md` — immediately implementable, no gate); M12-INPUT rows → the M12 observability milestone's evidence base; M10-M13-INPUT rows → parked UI-surface inputs; DOC-11-CURRENCY rows → dated currency notes on the Locked doc; M5-C-COPY rows → the B3 explainability story in the website/docs lane (joining the R14-A dossier, REC-145, and REC-182); FUTURE rows → Nick's queue; REJECTs → the anti-requirements register. Nothing in this cycle amends frozen contracts. A finding that cannot be placed in that machine is a finding you should sharpen or drop.
