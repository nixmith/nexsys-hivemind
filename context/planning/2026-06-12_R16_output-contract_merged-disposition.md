<!--
file: context/planning/2026-06-12_R16_output-contract_merged-disposition.md
purpose: R16 merged disposition — REC-186–215 (16-A UX/market + 16-B engineering) adjudicated into the seven cycle buckets; the anti-requirements register; the read-out. The bucket table here is authoritative for the cycle.
audience: PM (M12/M10-M13/M5-C consumers), Nick
state-type: disposition record
status: COMPLETE — both returns assessed 2026-06-12 (16-B A, 16-A A−; assessments in context/assessments/); high-water now REC-215
last-verified: 2026-06-12 (assessment session)
-->

# R16 Output-Contract Cycle — Merged Disposition (REC-186–215)

Fold order honored: **16-B first** (engineering constrains what the contract can promise), then 16-A (human evidence prioritizes which promises matter). Inputs: `2026-06-12_Research_16B_PM_Assessment.md` + `2026-06-12_Research_16A_PM_Assessment.md`. Zero discards across 30 RECs. Every REC routes to exactly one bucket.

## 1. Collisions adjudicated (the merged-pass actions)

1. **A-186 ⊆ B-201/202/203 (the OUTPUT_CONVENTIONS core).** A merge, not a conflict: A-186 is the promote-the-idiom umbrella with the human-factors rationale; B-201–203 are its load-bearing sections (verdict line, porcelain-grade stability, `KEY:value` spec). The draft cites A for *why*, B for *what*.
2. **A-187 ⊆ B-205 (+ the accessibility floor).** Merged into one draft rule: never color-only (WCAG SC 1.4.1, A's citation), honor `NO_COLOR` (B's no-color.org citation), keep the existing `[ -t 1 ]` gate. One rule, two registers of evidence.
3. **A-196 re-routed DOC-11-CURRENCY → M12-INPUT, folded into A-190.** The Rust-not-Elm voice rule (impersonal what+why+fix; never first-person "I") lives once, in the M12 register guidance — Doc 11's Locked text has no Elm reference to annotate.
4. **B-209 trimmed.** `--json`/`--kv` accepted as a documented extension point; the auto-emit-on-non-TTY clause dropped (contradicts B's own REC-202 stability doctrine). Machine lines stay unconditional — the shipped dual-encode idiom is the standard.
5. **B-211 corrected against LTD-01.** Java 21 is locked ground: the M12 MDC-propagation mechanism is explicit MDC copy (TaskDecorator-style); JDK-25 Scoped Values are recorded as a trajectory-conditional only.
6. **A-195 single-bucketed.** The "verify paste-survival in the standard" clause is absorbed by B-201/206 (it is a stated design principle of the draft); the REC remains M5-C-COPY only.
7. **Register fences held in both directions** (each return routed the other's register out via §5 one-liners); REJECT sets complementary, no overlap, no contradiction.

## 2. The merged table — every REC, exactly one bucket

### 2a. SCRIPT-STANDARD → `scripts/dev/OUTPUT_CONVENTIONS.md` (DRAFTED THIS SESSION — gate-free, core repo)

| REC | Rule (as landed in the draft) | Source |
|---|---|---|
| B-201 (+A-186) | Line-anchored verdict line, last, color-free: `<VERDICT_KEY>:PASS` / `<VERDICT_KEY>:FAIL:<detail>` | TAP `^ok` / grep verdict-in-text / shipped `READINESS:` |
| B-202 (+A-186) | Machine format is porcelain-grade: stable, color-free, config-independent; changes versioned, never silent | git `--porcelain` v1 guarantee |
| B-203 (+A-186) | Labeled `KEY:value` data lines: UPPERCASE_SNAKE keys, no `:` in keys, one datum/line, `cut -d: -f2-`-safe | git porcelain / JSON Lines / shipped `get_val` |
| B-204 | Diagnostics→stderr, machine output→stdout — **the retrofit fix** (pi-health.sh, pi4-validation.sh, oq-15-2 driver all currently violate) | Google Shell Style Guide / clig.dev; defect confirmed TRUE at `01841ba` |
| B-205 (+A-187) | Never color-only; honor `NO_COLOR`; keep the `[ -t 1 ]` gate; text tags carry semantics | WCAG SC 1.4.1 / no-color.org |
| B-206 | Bounded output; tail carries the verdict; no unbounded remote blobs; bounded line length (the token-economics law) | Anthropic 25k-token default / in-house law |
| B-207 | Exit codes: 0 pass / 1 fail / 2 usage; propagate remote codes; the verdict line carries what `$?` cannot (paste-blindness) | grep 0/1/2 / clig.dev / shipped `exit "${GRADLE_EXIT_CODE}"` |
| B-208 | CLI ergonomics floor: `-h\|--help`, `--dry-run`, env-var config block + precedence, no interactive prompts when non-TTY | clig.dev / shipped pi4-validation |
| B-209 (trimmed) | Optional explicit `--json`/`--kv` extension point; machine lines remain unconditional; no isatty content-switching | clig.dev / terraform `-json`; PM ruling #4 |

### 2b. M12-INPUT (observability milestone evidence base + instruction obligations, INSIDE Locked Doc 11/LTD-15)

| REC | Obligation | Note |
|---|---|---|
| B-210 | PIN + test: every log line emitted while handling an event carries that event's `correlation_id` (MDC) | inside LTD-15/Doc 11 §3.4 |
| B-211 (corrected) | PIN + spike: MDC propagation across virtual-thread boundaries — explicit MDC copy on Java 21 (LTD-01); test with `-Djdk.traceVirtualThreadLocals=true`; assert no cross-event leakage; Scoped Values = trajectory note only | the cycle's one L-effort item |
| B-212 | Project-wide dotted log-event naming convention candidate: `subsystem.noun.verb[.state]`, depth discipline, started/completed pairing, level keyed to who-must-act | §0.3/Doc 11 §11.2 already satisfy |
| B-213 | Stable-log-name-as-API deprecation discipline: names are deprecated, never silently renamed | OTel governance model |
| A-188 | The log-dive corpus filed as INV-TO-04's named target (motivating evidence for M12) | HA/Hubitat/SmartThings/Homey corpus |
| A-189 | Noise-budget test: routine-path events stay ≤ DEBUG; WARN reserved for genuine anomalies (guards Doc 07 §11.2's discipline) | complements B-212 (test vs convention) |
| A-190 (+A-196) | `config_error` message-content register: what+why+what-to-do-next, impersonal (Rust's structure, never Elm's "I" — Register C) | content only; schema untouched |
| A-197 | Negative-trace ("why didn't it fire?") corpus filed under Doc 11 §15 OQ1 — evidence only, resolution stays open | all four platforms unanswerable |

### 2c. M10-M13-INPUT (UI lane — parked, not drafted)

| REC | Parked input |
|---|---|
| A-191 | Plain-language causality rendering rule for the end-user trace view ("X happened because Y", friendly names, same `correlation_id` events the operator sees raw) |
| A-192 | Friendly-name vs stable-ID vocabulary split: user surfaces render friendly names; operator/agent surfaces retain stable IDs |

### 2d. DOC-11-CURRENCY (queue — rides the next Doc-11-touching amendment; Locked-doc fence respected)

| REC | Currency note |
|---|---|
| B-214 | Doc 11 §3.5 metric-prefix non-uniformity — verified TRUE and understated: ten subsystem rows in ≥3 styles (`hs_events_*`/`hs_state_store_*`/`hs_persistence_*`/`hs_automation_*` · `hs.device.*`/`hs.integration.*`/`hs.zigbee.*`/`hs.api.*`/`hs.ws.*` · bare `config.*`); note the Prometheus-style `.`→`_` rewrite relevance if the post-MVP Micrometer facade lands. A note, never an amendment. |

### 2e. M5-C-COPY (website/docs superiority backlog — consumed by M5-C Increment 1 if it has not yet run [prompt still on disk, unarchived = not run]; otherwise Increment 2. Do NOT retro-inject into a completed Increment 1.)

| REC | Copy item |
|---|---|
| A-193 | The no-ring-buffer/no-eviction attestation ("the trace is still there next week") — vs HA last-5 `stored_traces` default + Hubitat ~1 MB purge, both verified at official docs |
| A-194 | THE FLAGSHIP: the B3 plain-language-causality dossier (§3.3 of the A-return) — spine: HA's maintainer-run "Month of WTH" porch-light thread (219488, verified exact) + "rendering, not data" + Homey's missing attribution + the eviction contrast. Joins the ledger-gap dossier + no-templating-DSL claims. |
| A-195 | "Logs survive an LLM paste" property (TTY-stripped tags + stable `READINESS:` line) — register check at the M5-C session (Register B voice, DAS bans apply) |

### 2f. FUTURE (Nick's queue — sketched, not drafted)

| REC | Sketch |
|---|---|
| B-215 | Optional correlation-id echo in script output (a labeled line joining a paste to the event chain) — when scripts act on correlated runtime operations, post-M12 |

### 2g. REJECT — the anti-requirements register (binding)

| Item | Source | Reason |
|---|---|---|
| Emoji-as-semantics in logs/CLI | A-198 | Parse hazard + documented crash class; bracket-tags already correct; text must carry semantics |
| Silently-lossy / opt-in-only primary log surface | A-199 | The SmartThings arc (1-in-4 drops → surface deleted); reliability is a UX property |
| Euphemistic "friendly" error copy | A-200 | Anti-Register-C; DAS bans restated as guardrail |
| OTel/OTLP collector, log-shipping daemon, sidecar on the Pi | B §3.4 | LTD-15 verbatim ("No Prometheus… No OpenTelemetry in MVP") + §0.6 row 6; post-MVP Micrometer facade already accommodated (Doc 11 §14) |
| systemd-style 128-bit `MESSAGE_ID` hex catalog | B §3.4 | Dotted event names already serve the stable-type-ID role, human-legibly |
| logfmt as production wire format | B §3.4 | LTD-15 locks JSON lines explicitly; two formats = double parser surface |
| Full W3C `traceparent` machinery | B §3.4 | Solves cross-service propagation a single-host system doesn't have; `CausalContext` covers in-process causality |
| OTel SeverityNumber (1–24) normalization | B §3.4 | §0.3 levels + journal 0–7 mapping sufficient at single-host scale |

## 3. Read-out

**The cycle's one defect-fix ships immediately:** REC-204 (diagnostics→stdout) is a confirmed-TRUE defect in both shipped scripts and the OQ-15-2 driver; the OUTPUT_CONVENTIONS draft carries the retrofit list. **The cycle's prominent honest negative (16-A §3.4, top-billed here per its evidential weight): the B3 risk is data-without-register** — the Locked record's plain-language rendering register is thinner than its data machinery; if that register is never specified, "B3 is a data claim wearing a UX claim's clothes." Routed concretely: A-190 (M12 message register), A-191 (M10/M13 rendering rule), A-194 (the dossier states the *claim* the register must eventually cash). **Validation findings:** the Locked direction is affirmed across the board — log-diving pain is INV-TO-04's named target (A-188), always-on diagnostics and per-package levels survived the over-engineering check on human evidence, and the shipped pi-health idiom is independently assessed best-in-class by both registers (the highest-leverage move was codification, not invention — done this session). **High-water: REC-215.** Counts: SCRIPT-STANDARD 11 RECs → 9 rules · M12-INPUT 8 · M10-M13 2 · DOC-11-CURRENCY 1 · M5-C-COPY 3 · FUTURE 1 · REJECT 3 RECs + 5 anti-requirements. Zero discards; zero fabrications in either return; grades A (16-B) / A− (16-A).
