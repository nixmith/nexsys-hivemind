<!--
file: context/instructions/Research_16B_LLM_Legible_Output_Engineering_Brief.md
purpose: Dispatchable research brief — Research 16-B: LLM-Legible Output Engineering: Structured Logging and Agent-Parseable Tooling (engineering register). Gap-relative to the Locked observability design (Doc 11 + LTD-15 + Doc 07 §11), the event-model correlation machinery (CausalContext at `7c73c91`), and the shipped script idiom (pi-health.sh at `01841ba`). One cycle object: ONE output-contract philosophy serving three consumers — end-users, developers/operators, and LLM agents.
audience: DOCS Project researcher (primary), PM (assessment), Nick (dispatch)
status: READY TO DISPATCH — authored 2026-06-12 (PM, Cowork) per the archived R16 session prompt. Runs SIMULTANEOUSLY with Research 16-A — REC ranges are partitioned; this brief is fully self-contained (never reference a sibling return).
dispatch-target: the DOCS Claude Project (homesynapse-core-docs connector; CORE available for source-grounded follow-ups). Engineering prior art needs spec/docs/source citations — WEB SEARCH IS REQUIRED. If the connector is unreachable mid-run, DECLARE it in §5 per the charter's connector-blind protocol and work from the embeds — do not reconstruct HomeSynapse facts.
rec-block: REC-201–215 (reserved; high-water at authoring = REC-185, the R14/R15 cycle; the sibling holds 186–200 — do not exceed 215)
baseline: homesynapse-core HEAD `01841ba` (scripts-only, on substantive `7c73c91` M6.2) · docs watermark AMD-93 (RATIFIED 2026-06-12) · projectionVersion 5 · event pins 55/24/36 · invariants 163/47
-->

# RESEARCH BRIEF: Research 16-B — LLM-Legible Output Engineering: Structured Logging and Agent-Parseable Tooling

*Target: the Script Output Standard (`scripts/dev/OUTPUT_CONVENTIONS.md` candidate) + the M12 observability evidence base + Doc 11 currency notes. Date: 2026-06-12.*

You are an engineering prior-art researcher for HomeSynapse Core, a local-first, event-sourced smart home runtime in Java 21 on Raspberry Pi-class hardware. Your Project custom instructions carry the `research_mode` charter — the quote-back discipline, disposition buckets, evidence hierarchy, register fences, verbatim external vectors, and honesty-section obligation **apply in full and are not restated here**.

HomeSynapse's development and operating workflow has a third output consumer alongside humans: **LLM agents** (Claude Code / Cowork sessions) that parse pasted script output and log excerpts as a primary workflow. The shipped `pi-health.sh` `READINESS:` line is the in-house precedent — output designed so an agent can rule on it from a paste. Your task is NOT design. It is an **engineering prior-art gap analysis**: how production systems structure logs and CLI output so machines (including LLM agents with bounded context windows) parse them reliably — mapped against what HomeSynapse has already Locked, decided, or shipped, so the PM can extract a Script Output Standard, M12 obligations, and Doc 11 currency notes.

**The disposition table (§4b) is the load-bearing deliverable.** A finding without a disposition row is unusable. A "gap" the Locked design already closes poisons the pipeline.

---

## 0. Quote-back gate [DO THIS FIRST]

Open your return by quoting back, **verbatim**: (a) the §0.2 script-idiom block (all three fenced sub-blocks); (b) the §0.3 Doc 07 §11.2 log-event name list (all 14 names, in order); (c) the §0.4 `CausalContext` record signature AND the `com.homesynapse.event` module-info embed; (d) the §0.5 Register-C paragraph. If you cannot quote them, STOP and return INCOMPLETE. A return that fails the quote-back is discarded unread past §0.

## 0.1 Authoritative state (do not work from memory)

- homesynapse-core HEAD: **`01841ba`** (2026-06-12, scripts-only; substantive HEAD `7c73c91`, M6.2). On-disk amendment watermark **AMD-93** · `projectionVersion` **5** · event manifest pins **55 / 24 / 36**.
- **Doc 11 (Observability & Debugging) is LOCKED (2026-03-09).** Per LTD-15: SLF4J + Logback + structured JSON encoder; MDC mandatory context fields; log rotation daily / 50 MB per file / 500 MB total cap; **no Prometheus or OpenTelemetry export in MVP** — Doc 11 §14 already accommodates a post-MVP Micrometer facade, so "add an exporter" is settled ground, not a finding.
- **AMD-88..93 RATIFIED 2026-06-12.** AMD-92 fixed the automation event vocabulary: event types/payloads are **frozen ground** — no event-vocabulary changes from this research.
- The observability subsystem is **design-only** (Phase-3 implementation is the M12 window this research feeds). The **script layer is shipped, gate-free, and immediately improvable** — your strongest findings can land there without any ratification machinery.
- Coder-convention ground: production logging uses SLF4J with structured context keys (`entity_id`, `event_type`, `correlation_id`); all time access is Clock-injected; ULIDs render as strings only at API boundaries and logs.
- The standing token-economics law (paid for in-house, 2026-06): **multi-thousand-token single lines defeat line-based pagination and forced agent workarounds** — the same law governs log lines and CLI output destined for agent consumers. Treat bounded line length and bounded output volume as first-class engineering constraints, not niceties.
- Research numbering: this is **Research 16-B**, REC range **201–215**. A sibling brief runs simultaneously in the UX/market register with its own range; you must not reference or anticipate it.

## 0.2 Embedded verbatim — the shipped script idiom (`scripts/dev/pi-health.sh` + `scripts/pi4-validation.sh` at `01841ba`)

The in-house standard your prior art is benchmarked against. Three sub-blocks, verbatim from source:

**(i) Severity-tag output helpers (both scripts):**

```bash
info()   { printf "${BLUE}[INFO]${NC}  %s\n" "$1"; }
ok()     { printf "${GREEN}[OK]${NC}    %s\n" "$1"; }
warn()   { printf "${YELLOW}[WARN]${NC}  %s\n" "$1"; }
fail()   { printf "${RED}[FAIL]${NC}  %s\n" "$1"; }
header() { printf "\n${BOLD}=== %s ===${NC}\n" "$1"; }
```

Color is TTY-gated — when stdout is not a terminal, every color variable is the empty string (`if [ -t 1 ]; then … else RED='' GREEN='' YELLOW='' BLUE='' BOLD='' NC=''; fi`): piped/pasted output carries the `[OK]`/`[WARN]`/`[FAIL]` tags with no ANSI escapes.

**(ii) Labeled `KEY:value` remote-data lines (pi-health.sh batched SSH collection — "Each value is emitted on a labeled line for reliable parsing"):**

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

on the all-checks-passed path (exit 0), and `echo "READINESS:FAIL:${FAILURES}"` on the failure path (exit 1). `pi4-validation.sh` adds: `--dry-run` (print the plan, do nothing), env-var configuration (`PI_HOST`, `PI_PROJECT_DIR`), `-h|--help` banners, timestamped local results directories, and remote exit-code propagation (`exit "${GRADLE_EXIT_CODE}"`).

## 0.3 Embedded verbatim — the named-log-event precedent (Doc 07 §11.2, LOCKED)

"Key log events follow the structured JSON format per LTD-15 with correlation IDs linking to the Run trace." The 14 event names, with levels — quote this list back in §0:

`automation.run.started` (INFO) · `automation.run.completed` (INFO) · `automation.run.failed` (WARN) · `automation.run.skipped` (DEBUG) · `automation.command.dispatched` (DEBUG) · `automation.command.confirmed` (DEBUG) · `automation.command.timed_out` (WARN) · `automation.reload` (INFO) · `automation.conflict` (WARN) · `automation.disabled` (WARN) · `automation.trigger.duration.started` (DEBUG) · `automation.trigger.duration.expired` (DEBUG) · `automation.trigger.duration.cancelled` (DEBUG) · `automation.trigger.duration.limit_exceeded` (WARN)

Key fields are snake_case (`run_id`, `automation_id`, `triggering_event_id`, `duration_ms`, …). Every design doc defines its own §11.2 in this dotted-name style (e.g., Doc 11 §11.2: `observability.health.transition`, `observability.jfr.recording_stalled`, `observability.stream.snapshot_dropped`). **PM-observed seed for RQ4 (verify against the docs — do not assume):** the per-subsystem *metric* prefixes in Doc 11 §3.5 are not uniform across subsystems (`hs_events_*`, `hs.device.*`, `config.*` coexist); whether a project-wide naming convention should note this is a DOC-11-CURRENCY question, never an amendment.

## 0.4 Embedded verbatim — the correlation machinery (source at `7c73c91`)

`core/event-model/src/main/java/com/homesynapse/event/CausalContext.java`:

```java
public record CausalContext(
        Ulid correlationId,
        Ulid causationId
) {
```

Javadoc contract: `correlationId` = "the root event's event ID, propagated unchanged through all downstream events in the chain; never null"; `causationId` = "the immediately preceding event's event ID; null for root events only".

`core/event-model/src/main/java/module-info.java` (the standing Research-6 rule: module names and edges are authoritative from this embed, not from any summary):

```java
/**
 * Event model — types, envelope, publisher, store, and bus interfaces.
 */
module com.homesynapse.event {
    requires transitive com.homesynapse.value;
    requires transitive com.homesynapse.platform;

    exports com.homesynapse.event;
}
```

Trace assembly (Doc 11 §3.4, LOCKED): chains are assembled by a single `correlation_id` SQL query + O(n) tree build; reverse lookup ("why is this device in this state?") is the primary diagnostic query (D-07); completeness is detected via terminal event types. **Logs and the event log tell ONE causal story — the trace model is the spine; logging is its narration.** The structured-log `correlation_id` context key (LTD-15/MDC) is the join key between a log line and its chain.

## 0.5 Embedded verbatim — the human-register floor (DAS Consolidated Reference §1.1)

> **Register C — Direct Neutral (UI).** *The system communicating state, action, resolution.* No self-reference (neither "HomeSynapse" nor "we"), minimal words, maximum clarity, never blames, never apologizes, never celebrates. Used for: error messages, status indicators, dialogs, tooltips, empty states, notifications.

Relevant to you because dual-channel design must not fork the philosophy: the human channel obeys this register while the machine channel obeys your stability rules — one contract, two renderings.

## 0.6 Embedded — the decided/Locked ground your findings are gap-relative to

| # | Decided item | Status |
|---|---|---|
| 1 | **The cycle frame:** one output-contract philosophy, three consumers (end-user / operator / LLM agent), spanning Core logging AND script tooling | The research object |
| 2 | **LTD-15 logging stack:** SLF4J + Logback + JSON encoder; MDC context fields (`correlation_id`, `entity_id`, `integration_id`); rotation bounds; no Prometheus/OTel in MVP (post-MVP Micrometer facade accommodated, Doc 11 §14) | LOCKED — adoption questions are *pattern*-level, never *stack*-level |
| 3 | **Doc 11 Locked machinery:** always-on JFR + structured logging; trace assembly by `correlation_id`; per-package dynamic log levels; JFR fields primitives/String only | LOCKED — baseline, never an open question |
| 4 | **AMD-92 event vocabulary RATIFIED:** event types and payloads frozen; log events (§0.3) NARRATE events — they do not mint them | Frozen ground |
| 5 | **The script layer is gate-free:** `scripts/` conventions are PM/Nick territory — your SCRIPT-STANDARD findings are immediately implementable, no ratification | Shipped substrate (`01841ba`) |
| 6 | **Constrained hardware (LTD-02 class):** Pi 4 validation floor; no log-collector daemons, no agent sidecars, no heavyweight pipelines — every adoption recommendation is weighed against this | Standing constraint |

---

## 1. Research questions (answer ALL five; engineering register, spec/docs/source citations)

### RQ1 — Structured-logging prior art (what's worth adopting, with the cost stated honestly)

Survey with exact citations: **OpenTelemetry log/trace semantic conventions** (field names, trace/span correlation conventions — as a *vocabulary* to borrow from, given the collector/exporter is explicitly out of MVP scope; weigh partial-adoption cost honestly); **JSON Lines vs logfmt** (parse reliability, human readability, tooling ecosystems, failure modes of each); **systemd journal fields** (the uppercase field convention, `MESSAGE_ID`, priority mapping — relevant because HomeSynapse runs under systemd); **SLF4J/MDC patterns** (context propagation across threads — note HomeSynapse runs work on virtual threads; MDC inheritance behavior there is a real engineering question); key-naming conventions (snake_case vs dotted vs camelCase; collision discipline). Verdict per item: ADOPT-AS-PATTERN (M12-INPUT) / ADOPT-IN-SCRIPTS (SCRIPT-STANDARD) / REJECT-WITH-REASON — for a Pi-class, local-first system with no collector.

### RQ2 — The agent-consumer contract (the cycle's distinctive RQ)

What makes CLI/log output reliably parseable by LLM agents? Assemble the prior art AND the failure evidence: **stable line-anchored keys** (the `KEY:value` discipline — §0.2(ii)); **machine-parseable summary lines** (the `READINESS:` precedent — §0.2(iii); cf. TAP version lines, `git status --porcelain` stability guarantees, exit-status conventions); **dual-channel design** (pretty TTY vs `--json`/`--porcelain`/`--kv` streams; how gh/kubectl/terraform/systemctl gate this; auto-detection vs explicit flags); **bounded output + tail-with-summary patterns** (context-window economy — an agent pasted 400 lines needs the verdict in the last 3; what conventions exist for head/tail-stable output); **deterministic ordering** (sorted keys, stable section order — diff-ability and agent reliability); **no ANSI/spinners/carriage-return tricks in non-TTY output** (cite the conventions: `NO_COLOR`, `CLICOLOR`, isatty gating); **exit-code semantics** (0/1/2-class taxonomies, e.g. grep's, diff's; what an agent can infer from an exit code it cannot see vs a summary line it can). Where documented LLM-specific evidence exists (agent-tooling guides, MCP/CLI design notes, "design your CLI for AI" engineering posts from credible sources), cite it; where it does not, say so and reason from the adjacent machine-consumer prior art. Verdict: the candidate rule-set for the Script Output Standard, each rule sourced.

### RQ3 — Correlation propagation: one causal story across logs and events

How do production systems thread one correlation identity through every output surface, and where does it break? Survey: OTel trace/span-id-in-logs conventions; systemd journal cross-unit correlation practice; the MDC-propagation failure classes (thread pools, async boundaries — and the virtual-thread story in modern Java); correlation-id-in-CLI-output practice (request IDs printed on failure for support workflows). Gap-relative: §0.4 is the spine — `CausalContext.correlationId` propagated unchanged through chains, trace assembly by single query, the `correlation_id` MDC key as the log↔chain join. Verdict: what correlation rules the M12 logging implementation must pin (e.g., every log line emitted while handling an event carries that event's `correlation_id`; script output referencing system state carries the relevant id when available), expressed as M12-INPUT obligations INSIDE Locked contracts — plus any genuine contract gap → FUTURE.

### RQ4 — The named-log-event taxonomy, generalized

The §0.3 precedent (`automation.run.started` class) is per-design-doc. What does prior art say about project-wide log-event naming: hierarchical dotted names (depth discipline, verb tense conventions, started/completed pairing); event-name registries and collision governance (cf. OTel semantic-convention governance, systemd `MESSAGE_ID` catalogs); level-assignment discipline (what's INFO vs DEBUG vs WARN — keyed to who must act); the stable-name-as-API problem (log names that tools grep become contracts — deprecation discipline). Deliverable: a project-wide log-event naming-convention PROPOSAL (a convention candidate, not an amendment) that the existing §0.3/§11.2 tables already satisfy or could satisfy with currency notes — flag any per-doc §11.2 inconsistencies you find as DOC-11-CURRENCY rows (the §0.3 PM-observed metric-prefix seed included, verified against the actual doc text).

### RQ5 — The script-layer standard: codify the pi-health idiom

Turn §0.2 into a written convention every future HomeSynapse script follows. Survey what the strongest CLI/script style guides actually mandate (Google Shell Style Guide, the CLI guidelines literature, established projects' contributing docs) and merge with the shipped idiom: severity tags (`[INFO]/[OK]/[WARN]/[FAIL]` — exact spacing/format rules); labeled `KEY:value` data lines (charset, escaping, multi-value discipline); the machine-parseable summary line (naming pattern — is `READINESS:` generalizable to `RESULT:`/`SUMMARY:` families?; position-last guarantee; grep-anchor stability); `--dry-run` semantics; env-var configuration precedence; `-h|--help` content floor; TTY-gated color; exit-code taxonomy; agent-paste ergonomics (bounded sections, the tail-carries-the-verdict rule, no interactive prompts in non-TTY). Deliverable: the section-by-section skeleton of `scripts/dev/OUTPUT_CONVENTIONS.md` with each rule evidence-cited — the PM drafts the final document; you supply the sourced rule-set and the deltas between the shipped idiom and best practice (including anything pi-health gets WRONG — that is a finding, not an embarrassment).

---

## 2. Mandatory document format

```
# Research 16-B: LLM-Legible Output Engineering — Structured Logging and Agent-Parseable Tooling
*Target: HomeSynapse Script Output Standard + M12 evidence base + Doc 11 currency.
 Date: YYYY-MM-DD.*

## 0. Quote-back gate [M — FIRST] — per §0 above.

## 1. Executive Summary [M] — 5–8 verdict bullets; every bullet takes a position with a
     one-sentence defense. "X is worth investigating" is banned. Flag the single
     highest-impact finding AND the single rule the shipped idiom most needs to fix.

## 2. Prior-Art Deep Dives [M] — one subsection per system/convention surveyed (RQ1–RQ5
     coverage). Each: (a) the mechanism, precisely (field names, defaults, guarantees);
     (b) ≥1 direct quotation from a primary source (spec, docs, source, style guide)
     WITH URL; (c) documented failure modes; (d) the gap-relative lesson, citing the
     §0.2–§0.6 anchor it is relative to.

## 3. Cross-Cutting Analysis [M]
   - 3.1 Convention concept map: concern (format | naming | correlation | dual-channel |
         summary-line | exit codes | bounded output) | surveyed answers | HomeSynapse
         ground (cited §0.2–§0.6 anchor).
   - 3.2 THE AGENT-CONSUMER CONTRACT TABLE (RQ2): rule → prior-art source → shipped-idiom
         status (SATISFIES / VIOLATES / SILENT) → disposition route.
   - 3.3 The correlation narration map (RQ3): output surface → how the one causal story
         appears there → the join key → M12 pin or FUTURE gap.
   - 3.4 Over-engineering check: conventions prior art says are unnecessary at
         HomeSynapse's scale (single host, single writer, no fleet) — defend or flag
         each (honesty section; REJECT-candidates).

## 4. Findings + Recommendations [M]
   - 4a. REC-numbered findings, REC-201 through at most REC-215, ranked
         (impact × confidence)/cost. Each REC: concern class; evidence (≥1 primary
         source); gap-relative statement; concrete recommendation; effort class
         (S/M/L, prose).
   - 4b. THE DISPOSITION TABLE [M — load-bearing]: EVERY REC maps to EXACTLY ONE of:
           SCRIPT-STANDARD (lands in the planned scripts/dev/OUTPUT_CONVENTIONS.md —
             gate-free, immediately implementable)
         | M12-INPUT (evidence/obligation for the M12 observability milestone,
             INSIDE Locked Doc 11/LTD-15 contracts — a pattern, a pin, a test)
         | M10-M13-INPUT (UI-surface input — parked, not drafted)
         | DOC-11-CURRENCY (a currency-note candidate on Locked text — never
             re-litigation; rides the next Doc-11-touching amendment)
         | M5-C-COPY (website/docs superiority material, if a finding is genuinely
             positioning-grade)
         | FUTURE (contract delta — sketch, do NOT draft)
         | REJECT (reasoned — prior art says HomeSynapse should NOT do this).
         No REC in two buckets. No bucket empty by laziness — if genuinely empty, say why.

## 5. Caveats and Open Questions [M] — source reliability; spike candidates (anything
     needing empirical validation, e.g. MDC-on-virtual-threads behavior); connector-blind
     declaration if applicable; explicit INCOMPLETE-EVIDENCE if web reach was too shallow.

## 6. Appendix: Sources [M] — URL families grouped by system/spec; every factual claim
     traceable.

## 7. HomeSynapse Code-Level Implications [LIGHT] — observations ONLY, routed through
     §4b. NO module-info proposals, NO new types, NO contract drafts, NO event-vocabulary
     changes. Exact §0.2/§0.3/§0.4 identifiers only.
```

## 3. Evidence standards

The charter's standards apply in full (primary sources with URLs — specs, official docs, source code, style guides are primary, blog summaries secondary; precision over breadth — "OTel has log conventions" is useless, the field names and semantics are the finding; take positions; no fabricated identifiers — HomeSynapse names come from §0.2–§0.4 verbatim or the connector, and if a fact is in neither, request it in §5). The charter's freshness horizons apply — date every source; spec/convention versions cited (OTel semantic conventions especially) must name the version, since they move. Cycle-specific additions: **any external-standard constant or field name you cite (journal fields, OTel attribute names, exit codes) must carry its source citation verbatim**, and **LLM-agent-specific claims must be either cited to credible engineering sources or explicitly labeled as reasoned extrapolation from machine-consumer prior art** — do not launder speculation as evidence.

## 4. Guardrails (violations = the finding is discarded)

1. **Register fence: engineering register — proposals land as CONVENTION/STANDARD candidates + M12/Doc-11 inputs, NEVER as amendments.** You cannot change contracts: LTD-15's stack, Doc 11's architecture, AMD-92's event vocabulary, and the JFR field constraints are baselines to measure against, never open questions. Contract-delta implications route to FUTURE, sketched not drafted.
2. **No collector creep.** Any recommendation that implies an OTel collector, log-shipping daemon, sidecar, or external aggregation service on the Pi is a REJECT-candidate by default (§0.6 row 6) — argue it into a different bucket only with exceptional evidence, or bucket it FUTURE for post-MVP cloud lanes.
3. **The script layer is the immediate lane; Core logging is the M12 lane.** Keep them distinct in every disposition row — a rule can appear in both lanes only as two RECs (one SCRIPT-STANDARD, one M12-INPUT), each justified.
4. **REC numbering: 201–215 ONLY** (append-only global register; the sibling owns 186–200; high-water 185).
5. **Stay in register.** Human-factors evidence (forum pain, readability studies, end-user register design) is the SIBLING research's register — if you trip over strong community/UX evidence, note it in §5 as out-of-register, one line, and move on.
6. Produce ONE complete markdown document. Do not truncate.

## 5. What the PM does with the return (so you aim at it)

The PM runs the standard serialized A–F assessment, source-verified. **Your return is folded FIRST** (engineering constrains what the output contract can promise; the sibling's human evidence then prioritizes which promises matter). Routes: SCRIPT-STANDARD rows → the PM-drafted `scripts/dev/OUTPUT_CONVENTIONS.md` with pi-health retrofitted as the reference implementation (gate-free, can ship immediately); M12-INPUT rows → the M12 observability milestone's evidence base and instruction obligations (correlation pins, naming convention, MDC patterns); DOC-11-CURRENCY rows → the currency-note queue (rides the next Doc-11-touching amendment); M10-M13-INPUT rows → the parked UI lane; M5-C-COPY rows → the website superiority backlog; FUTURE rows → Nick's queue; REJECTs → the anti-requirements register with reasoning. Your §3.2 agent-consumer contract table and §3.3 correlation map are the cycle's distinctive deliverables — §3.2 IS the draft skeleton of the Script Output Standard. A finding that cannot be placed in that machine is a finding you should sharpen or drop.
