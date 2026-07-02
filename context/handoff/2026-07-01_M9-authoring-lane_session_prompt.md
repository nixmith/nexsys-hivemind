<!--
file: context/handoff/2026-07-01_M9-authoring-lane_session_prompt.md
purpose: Dispatch brief for a write-isolated M9-AUTHORING lane — a fresh Cowork conversation (nexsys-project-manager skill, Mode-3 Director posture) that produces the ISSUE-READY M9 coding instruction (+ pre-verification artifact + a proposed milestone split) against the measured bench corpus and the freshly-ratified AMD-96/97. It AUTHORS; it does not issue — the return routes to the v13 hub for independent source-audit, then Nick routes to the Coder.
audience: the M9-authoring lane (a FRESH Cowork conversation); the v13 hub (reviews the return); Nick (launches; routes the audited instruction).
state-type: session prompt (write-isolated worker lane).
status: READY — authored 2026-07-01 by the v13 hub after the consolidated governance pass (AMD-96 + AMD-97 RATIFIED + FOLDED, INV-ES-09 registered; M9 UNBLOCKED). Launch AFTER the beat-43 hivemind commit.
write-isolation: this lane writes ONLY (a) context/instructions/2026-07-XX_M9*_coding-instruction.md (one or more, per the split it proposes), (b) context/pre-verifications/WU-M9*.md, (c) ONE return file context/audits/2026-07-XX_M9-authoring-lane_return.md. NO spine edits, NO Locked-doc edits, NO core source edits, NO commits (Nick commits host-side on the hub's word).
baseline (RE-DERIVE at preflight — do not inherit): core 52824e9 · docs 1509b34 (watermark AMD-97; invariants 172/51; Doc 02/08/16 as amended TODAY — read the amended text, not memory) · hivemind cea7ae1 (beats 41+42 — note the commit message says "beat 41" but the commit carries both) · bench 5ceff3b (the corpus + fixtures = the acceptance substrate) · skills 846fe56.
-->

# M9-Authoring Lane — the real Zigbee adapter instruction, authored on measured ground

You are a **write-isolated authoring lane** running the **nexsys-project-manager** skill. Your single deliverable: the **ISSUE-READY M9 coding instruction set** — the hero on real silicon — authored against the measured bench corpus as its acceptance spec. You author; the v13 hub audits; Nick issues. Do not self-issue, do not touch the spine.

## 0. Ground first (non-negotiable, in order)

1. `context/process/cowork-environment-model.md` (path duality; the truncated-tail phantom is ACTIVE-INTERMITTENT — host file tools authoritative; `--no-optional-locks` for git reads).
2. `context/process/truth-hierarchy-and-pointer-not-copy-discipline.md` (re-derive every count/signature from source).
3. `project-manager/references/freshness-preflight.md` → run the 11-check preflight. Expect PASS-or-STALE-benign against the baseline above; reconcile-report in your return, but your lane does NOT edit the spine.
4. `project-manager/references/coding-instruction-format.md` + `references/repo-state-protocol.md` + `references/constraint-enforcement.md` + `references/cross-subsystem-awareness.md`.

## 1. The grounding set (read from SOURCE at the pinned SHAs — this is most of the session)

- **The ratified contracts (docs 1509b34):** Doc 08 §3 COMPLETE (§3.1–§3.15 — pay measured attention to §3.3 [as amended by AMD-96: v13–v14 band, measured 7.4.5.0/v13 baseline, VID:PID-not-descriptor-strings port-id, version-at-stack-init], §3.4 interview, §3.5 [Kelvin-at-ingestion CT row], §3.6 [the AMD-97 `confirmation[]` block + DeviceProfile + the engine-consumption caveats], §3.7 [reporting config incl. the NEW OccupancySensing row], §3.10 dispatch, §3.12 IAS, §3.13 network formation, §4 data model, §5 invariants) · Doc 02 §3.6/§3.7/§3.8 (as amended: confirmability override, AMD-97-INV-01) · `design/amendments/AMD-96_*.md` + `AMD-97_*.md` (the ratified texts) · the invariant register §2 INV-ES-09 + §51.
- **The measured acceptance substrate (bench 5ceff3b):** `corpus/coordinators/*`, `corpus/devices/*` (the confirmation blocks + caveats), `fixtures/*` (both event streams + README), `corpus/raw/*` (the diagnostics), `docs/2026-07-01_phase-0-1_bringup-report.md`.
- **The M9 acceptance additions (RATIFIED at beat 42 — fold ALL seven into the instruction's acceptance criteria):** (1) **Configure-Reporting is an explicit acceptance step** — the corpus's ON_CHANGE posture was configured by ZHA; fixture replay cannot catch its omission; M9 must bind + configure reporting itself (Doc 08 §3.7) and prove it; (2) **reporting-config parity** — the measured latency bands are reference-stack-conditioned (ZHA Level min ~1 s vs §3.7's 5 s; CT ~10 s vs 5 s): pin config parity or re-measure under M9's own posture before trusting the timeout bands; (3) **pin the latency reference point** — corpus `on_off` samples are ACK→report; `brightness`/`color_temperature` are command→report; (4) hero binding = `occupancy.occupied` (never `motion`); (5) ingestion dedup (consecutive-TSN duplicate pairs, 8–21 ms); (6) tolerate-not-require IAS enrollment; (7) firmware-version-aware acceptance (band v13–v14; read at stack-init; reflash-re-anchor contingency).
- **The code territory (core 52824e9):** MODULE_CONTEXT.md + **verbatim `module-info.java`** for: `integration-api`, the integration-zigbee scaffold (verify what exists — do NOT assume), `core/device-model`, `core/event-model`, `core/value-model`, `core/event-bus`, `core/persistence`, `core/automation` (the M7.3 `PendingCommandLedger` + M7.4 dispatch seams M9's confirmations feed), `lifecycle` (the M7.4d replay gate M9 must stay green under — INV-ES-09), `app` (composition root; AB-1/AB-2/AB-4 seams). Embed the module-info text verbatim in the instruction (the Research-6 lesson). Verify the serial-transport dependency situation from the version catalog — never assume a library.
- **Process anchors:** `context/planning/phase-3-milestone-backlog.md` (the M9 row + neighbors), `context/lessons/pm-lessons.md` + `coder-lessons.md`, `context/decisions/2026-06-28_bench-test-and-truth-engine_decision-record.md` (consequence (a): the harness/codec DNA-share), `context/decisions/2026-06-20_V1-launch-scope_decision-record.md` (D-OPEN-1).

## 2. Authoring disciplines (the ones that earned their place)

- **Grounding-subagent-before-authoring:** before writing the instruction, run an adversarial source-verification subagent over every type/signature/module-name/SQL-table the draft cites. Zero fabrications is the bar (the M7.5a/M7.5b precedent).
- **Pre-verification artifact:** M9 depends on ≥3 source-state assumptions → write `context/pre-verifications/WU-M9.md` (observed signatures / "absent → must create") BEFORE the instruction; the Coder reads it first.
- **P1 sizing smell:** "M9 is small per D5" is Wave-1-scoped, not license for an epic. If your grounding shows >1 compile-and-commit unit, PROPOSE a split (e.g. transport/auto-detect → interview/codec+reporting → confirmation-engine+hero-E2E) with per-unit done-whens against the backlog row — the hub + Nick rule it.
- **Constraint fan-out:** the AMD-97 `DeviceProfile.confirmation[]` is NEW code (a record + registry per Doc 08 §3.6/§4.3) — apply the record-component/static-factory STOP-check + the consumer/pin survey to everything it touches; §4c Clock-injection reminder applies (integration-zigbee is not whitelisted); event mints: derive from AMD-92/EventTypes whether M9 mints ANY new event type (expectation: ZERO — verify, and pin the counts 71/41/53 in the instruction).
- **Acceptance = the fixtures:** the corpus is the acceptance spec (AMD-97 consumption contract): a `CONFIRMABLE` capability confirms on the captured fixture; `UNCONFIRMABLE` paths render honest `UNCONFIRMED` immediately (AMD-97-INV-01 test shape is written in register §51); the M7.4d replay gate must stay green with the adapter wired (INV-ES-09 — zero side-effects on replay INCLUDING adapter I/O).

## 3. Return contract

ONE return file: the instruction path(s) + the pre-verification path + the proposed split (if any) + open `[Design point]`s for Nick + a self-review against `references/review-and-quality.md`. Report — do not commit. The v13 hub runs the independent audit; Nick issues to the Coder.
