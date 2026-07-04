<!--
file: context/process/decision-rationale-index.md
purpose: The index of load-bearing rulings — one line of WHAT + WHY each, with a pointer to where the full rationale lives. Exists so a fresh Claude can DEFEND decisions, not merely obey them, and so nobody re-litigates settled ground. This is an INDEX (pointer-not-copy): the cited source is authoritative; governance-side detail lives in the docs repo's registers/AMDs.
audience: All agents, at need (the PM boot sequence names it); Nick.
state-type: reference (append-on-ruling)
update-rule: the hub appends a row at every strategic/design-point ruling, at WUCP Phase 2 for [REVIEW] clusters, and marks PENDING items when they close.
status: CURRENT
last-verified: 2026-07-03 (v15 hub, beat 60 — authored for the wipe test; rows sourced from the spine, the governance registers, and the beat records cited)
-->

# Decision Rationale Index

**Layer 0 — the standing registers (read these for anything not indexed here):** Locked Technical Decisions (LTD-xx) + Architecture Invariants (172/51 at AMD-97) → `homesynapse-core-docs/governance/`; ratified amendments AMD-01..97 (each carries its own rationale); the strategy layer → `nexsys-hivemind/context/strategy/` (five files; Apache-2.0 licensing + revenue model live there); `Decisions_Quick_Reference` in the docs KB.

## Architecture & process spine (the "why is it built this way" set)

| Ruling | One-line rationale | Where the full rationale lives |
|---|---|---|
| Event-sourced, local-first core; CI is the gate of record | The replayable provenance log IS the product's moat (explainability + honest confirmation); an LLM "verification: clean" is never a gate | Docs 01/05/07; `context/process/ci-as-gate-of-record.md` |
| Five-repo model; hub = single spine-writer; lanes write-isolated | Parallel agents without write collisions; one auditable truth stream | PM skill masthead; `truth-hierarchy-and-pointer-not-copy-discipline.md` |
| Lane routing: backend M-WUs→Claude Code; frontend/research→Cowork; hub authors/audits | Priced empirically — the in-conversation micro-lane cost ~300K tokens (M7.5c-a); CC's compile loop is the shift-left | pm-handoff beat-56 (v14 retrospective); PM SKILL.md masthead |
| Never-false-CONFIRMED (AMD-97-INV-01) + honest actuation ledger | The trust brand is the business; an unconfirmed success rendered as success is the one unforgivable lie | AMD-97 + Doc 07 §3.11; §51 |
| Static composition now; dynamic loading a RESERVED seam (triple-banned) | Ship trust first; reserve the seam formally so activation is additive, never re-architecture | Extensibility assessment D3 (2026-07-02); charter §3 seam 1; **Doc 18 LOCKED 2026-07-03** |
| **Doc 18 LOCKED + EXT-INV-1/2 MINTED (§52; 172/51 → 174/52; watermark stays AMD-97)** | New-design-doc Lock per the §49/§50 precedent — the seven seam reservations + §3.5 namespace governance are now constitutional BEFORE M9.3 freezes the registry; EXT-INV-2 minted UNSCOPED with the rung-2 enforcement arrival named INLINE in the register (the N-2 anti-paper-invariant condition) | Register §52; Doc 18 §6/§7; pm-handoff beat-65 (rulings) + v17 beat-1 (execution) |

## Strategic rulings with preserved verbatim rationale (Nick, beat 57 — the model records)

| Ruling | One-line rationale | Full rationale |
|---|---|---|
| **DP-B: deterministic integration identity = PERMANENT** | Restart/reinstall-stable pure function; no identity file to corrupt/lose; the rename hazard is a NAMING-layer problem Doc-18 §3.5 defuses before M9.3 makes anything one-way | pm-handoff beat-57 (verbatim); first ruled beat 46 |
| **DP-18-A: semver + declared compat range + forward-only migration + NAMED deprecation floor** (strict immutability rejected) | One ruling unlocks community components AND AI-as-author; AMD-93-aligned (composes, no new mechanism); the named floor = the anti-SmartThings pledge as MECHANISM | pm-handoff beat-57; charter §4; dossier L-12/L-13 |
| **DP-18-B: wave-1 curated IN_JVM; RESERVED_SUBPROCESS = the intended non-curated rung; no-sandbox-claims honesty rule as doc text** | Matches what's built + the HA analog; AMD-63 bought the enum slot for exactly this; for a trust company one over-claimed sandbox costs more than every marketing sentence it earned | pm-handoff beat-57; charter §4 |
| **DP-18-C: (a) — community content NEVER paywalled; Connect rewords to convenience** | The community is the growth engine, not a gated feature; the paywall guards an empty room today while the reputational cost lands at pricing-page publish; revenue re-homes to the hosted/verified/one-click CHANNEL — "monetize trust, not access"; the PRINCIPLE is ruled now, wording polishes at pricing time; reword rides Doc 18's docs pass | pm-handoff beat-57 (verbatim — the fullest record); dossier L-24 |
| **OQ-1: DP-18-A deprecation floor = 6 release cycles + a Repairs-class migration surface, SEMANTIC PINNED** | "Release cycle" is undefined until the cadence is — floor never below LTD-16's one-major-version minimum; the wall-clock re-expression rides the release-cadence decision; "the automated-migration surface matters more than the number" | pm-handoff beat-65 (verbatim); L-11/HA ADR-0021 |
| **N-2: EXT-INV-2 minted UNSCOPED with the enforcement-arrival deferral INLINE in the register entry ("second half CI-testable at ladder rung 2")** | Anti-paper-invariant: "AIOT-INV-1 works because the deferral is named and scheduled inline… honest rather than promissory" — binding on the §52 registration text at Lock | pm-handoff beat-65 (verbatim) |

## M9 arc (Zigbee) rulings

| Ruling | One-line rationale | Source |
|---|---|---|
| DP-A: M9 split M9.1→M9.4, spine-first | INV-ES-09 replay-guard must exist BEFORE any real adapter I/O | M9 split charter §3 (`context/audits/2026-07-02_M9-authoring-lane_return.md`); beat 46 |
| DP-C: EZSP-first; full ZnpTransport deferred to Wave-2 | The bench instrument is EZSP silicon; ZNP ships as probe-encode only until ZBDongle-P arrives | charter §3 M9.2 row |
| DP-D: Tuya/Xiaomi manufacturer codecs deferred | No captured corpus for them yet; scaffold types reserved | charter §3 deferred list |
| DP-E: coordinator-backup/export seam RESERVED (zero code) | Un-backed-up coordinators strand whole networks; cheap to not-preclude now, existential later | charter §4; M9.2 instruction D-M92-8 |
| DP-F: fresh-network re-pair story rehearses at M9.4 bench acceptance | The operator token-lockout trap (FE-1b finding (a)) needs a documented recovery story before real users | beat 54 routing; v16 §3 |
| M9.2 R1–R7 (slf4j edge; test-support; bitmask 0x1B04; >v14→PIE band-edge; resume-mismatch→PIE never-silently-re-form; 43% stub arithmetic; resetSession) | Each preserves a Locked contract or reference-implementation ground the literal spec couldn't; all seven ACCEPT | pm-handoff beat-58 (rulings + evidence) |
| Checked-PIE seam rule + classifier-wrap trap (M9.4-binding, Matter-general) | `ExceptionClassifier` is bare-instanceof BY DESIGN (HA anti-pattern guard) — permanent failures must arrive UNWRAPPED via the package-private checked seams | zigbee MODULE_CONTEXT gotchas; pm-handoff beat-58 forward-risk register |
| maxHeight 7→8 (module graph) | The ruled lifecycle→integration-runtime edge is an intended layer; ceiling stays honest, do-not-raise-again note in root build.gradle.kts | M9.1 [REVIEW] record, beat 51 |
| **DP-1 (M9.3): `confirmation[]` realized 9→10 via a discrete Mode-2 AMD citing AMD-97, at the TOP of M9.3** | The moat becomes load-bearing, regression-protected schema — "the single most strategically important freeze in M9.3"; eight fields embedded verbatim, tests from measured bench values; "freeze it as governance, don't let it ride in on implementation churn" | pm-handoff beat-65 (verbatim); dossier §A |
| **DP-2 (M9.3): sealed `MatchCriteria` — ALL THREE variants defined now (`Fingerprint` shaped from the corpus IR), matching implemented for two** | The sealed-type door closes once, completely — exhaustive switches settle forever; Wave-2's first TS0601 populates an existing variant, never a re-seal; "reserving-but-not-shaping leaves a smaller version of the same door open" | pm-handoff beat-65 (verbatim); dossier §B; Doc 18 §3.5(d) |
| **DP-3 (M9.3 stated doctrine): "freeze the schema, defer the behavior"; W2-VAL debt tracked** | Records/sealed hierarchies are cheap-right-now, expensive-later, and the bench shapes them; silicon-needing behavior (codec path, adversarial sleepy-stall, OTA re-characterize) is Wave-2-validated; sleepy-stall + OTA legs de-risk as SYNTHETIC seeded-log fixtures pre-hardware | pm-handoff beat-65 (verbatim); backlog W2-VAL row |
| **THE NORTH STAR (the M9.x freeze arc): one-way-door precision outranks velocity** | "The one-way doors are the moat — the confirmation schema, the match-key type, the namespace convention, the extension invariants. Everything being frozen right now is the differentiation itself… rush the freezes and no amount of later velocity buys them back" | pm-handoff beat-65 (verbatim) |

## Frontend / website / brand rulings

| Ruling | One-line rationale | Source |
|---|---|---|
| D-4 (REC-180): privacy is a SEGMENT lead, not THE lead | Mass-market buys reliability/works-together; privacy converts prosumer/EU (with dated regulation teeth) — messaging rule, not scope change | R15 drafts (`context/planning/2026-06-13_strategy-refresh-drafts_R15.md`); ACCEPTED 2026-06-12 |
| W-4: install-story claims embargoed | No "plug-and-play" until the install story is ruled — tense-truth gate | frontend master plan §3.1 |
| W-11 name-light + D-FE-9 | Rename-readiness: product/company names are TOKENS everywhere (site + dashboard); rename = 2 values in 1 file | master plan; website-lane return §2 |
| SSG = Astro ^5.18 in the DOCS repo at `website/site/` | Vite-6 sameness with the dashboard (component/token sharing seam); content-adjacent; zero tree-sharing with core lanes; marketing churn out of core CI | beat 59 ruling record; website-lane return §1 |
| R-3 truthful developer posture + claim→truth tables as a HARD gate | Integration claims match shipped truth at publish; the strategy's SDK promise outran governance once — never again | assessment §3/watchlist 2; website-lane return §4 |
| Apache-2.0 claim PUBLISH-GATED | The LICENSE flip (strategy-locked) hasn't landed in-repo; tense-honesty until it does | website-lane return §5.1; strategy: Revenue_Model_and_Licensing_Strategy |

## PENDING (surface until closed — do not treat as ruled)

**hashed-TCLK** (Nick security election, M9.4 window, bench-informed) · **classifier cause-walk-for-PIE-only** (hardening candidate, M9.3/M9.4 window) · **website.yml adopt-now** (recommended, awaiting Nick) · **LICENSE-flip timing** (blocks developer-page publish only) · **W-5 publish gate / hosting / deploy** (gate-4 closure = Nick's). _AX-7 formal-AMD-shape CLOSED at the 2026-07-03 Doc 18 Lock: the direction's formal governance home is Locked Doc 18 §7.2 (watermark-neutral, §49/§50 precedent); the mechanism AMD rides Doc 16 OQ2 when an SDK/marketplace milestone actually schedules it (the OQ-2 class — deliberately not pre-authored)._
