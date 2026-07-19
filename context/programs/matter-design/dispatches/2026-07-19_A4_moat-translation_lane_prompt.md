<!--
file: context/programs/matter-design/dispatches/2026-07-19_A4_moat-translation_lane_prompt.md
purpose: Dispatch prompt for research lane A4 — how never-false-CONFIRMED / never-false-ALIVE translate onto Matter's interaction model, and what the corpus/bench doctrine looks like for Matter. The differentiating lane.
audience: a fresh write-isolated Cowork research lane (NOT the PM hub; do not load the PM skill).
state-type: session prompt (lane dispatch).
status: READY — authored 2026-07-19 by the Matter design-program hub (launch beat 1).
-->

# Lane A4 — The Moat Translation (what makes OUR Matter integration worth shipping)

You are a **write-isolated research lane** of the Matter/Integrations Design Program (charter: `nexsys-hivemind/context/handoff/2026-07-19_matter-design-program_hub_session_prompt.md`; ruled by Nick 2026-07-19). Your job: the differentiating question — map **never-false-CONFIRMED** and **never-false-ALIVE** onto Matter's interaction model precisely, find where honest confirmation is EASIER than Zigbee and where it is SUBTLER, and define what the compounding-testing doctrine looks like applied to Matter. This lane produces the content that makes the Doc-19 design's "why this is worth shipping" case.

**WRITE ISOLATION (ABSOLUTE):** exactly ONE file: `nexsys-hivemind/context/programs/matter-design/returns/A4_moat-translation_return.md`. No other writes anywhere. All repo reads read-only.

**EVIDENCE DISCIPLINE (two-layer hub audit):** spec claims cite the Matter spec section / SDK source file (the banked base already reached `ReadHandler.h` — that is the bar); tag `[VERIFIED-current: URL, fetched YYYY-MM-DD]` · `[community-reported: URL]` · `[inference — reasoning stated]` · `[banked: repo-path §]`. Labels are claims, quotes are evidence. Distinguish spec-mandated from implementation-observed behavior ruthlessly — the moat lives in that distinction.

## Baseline (banked; ↻ = re-verify, base fetched 2026-07-10)

Roadmap return §3.2 banked: Matter's read/subscribe model is **device-originated, subscription-based, versioned (`DataVersion`), and liveness-checked** (subscription terminates if no report within max interval — verified to `ReadHandler.h`/`AttributePathParams.h`) ↻ · Invoke responses give a CASE-sessioned per-command status distinct from the subsequent state report · for native devices this is "arguably stronger confirmation evidence than Zigbee's attribute reports" [banked inference — your lane proves or refutes it] · **the bridge caveat:** a bridge answers for its endpoints; attestation attaches to the bridge; bridged share is large but unquantified · "nobody else surfaces the native-vs-bridged evidence distinction to users" [banked inference ↻ — verify against current HA/openHAB/SmartThings behavior].

**Baseline shift:** Nick's 2026-07-19 ruling (full design program NOW); the fleet is 5/5 live; the S31 arc just produced a field exhibit of HONEST DOWNGRADE (`confirmation_downgraded … outcome=best_effort` rather than trusting an unverified seed — pm-handoff v33 beat 4) — the exact posture vocabulary your Matter mapping must land in.

## Required reads (in order)

1. The program charter — fences.
2. `context/process/2026-07-18_compounding-testing-doctrine.md` — THE operating charter: verdicts-as-monotone-asset, the ratchet rule, fixture-paired asserts, history-seeded scenarios, metrics-that-only-go-up. Your §5 answer extends this to Matter.
3. The AMD-97 confirmation-characterization amendment (locate in `homesynapse-core-docs/design/amendments/`; also its as-built expression in `homesynapse-core/integration/integration-zigbee/MODULE_CONTEXT.md` and `integration-api`/device-model contexts) — the vocabulary your mapping table lands in: `VERIFIED_REPORTS`/`ON_CHANGE`/`CONFIRMABLE`, expectations (`ExactMatch`/`WithinTolerance`), timeout seeds, degrade rules, `confirmation_downgraded`/best_effort.
4. `homesynapse-core-docs/design/01-event-model-and-event-bus.md` — the three-level lifecycle (`state_reported` → `state_changed` → `state_confirmed`) + the pending-command-ledger sections.
5. `homesynapse-core-docs/design/08-zigbee-adapter.md` §3.6/§3.10/§3.11 — the Zigbee comparator your easier/subtler verdicts are measured against.
6. Roadmap return §3.2 — the banked base.
7. `nexsys-bench/docs/` — skim the acceptance-record + scenario-format docs for what "a scenario" and "a measured envelope" concretely are here (the seeded-log architecture your §5 must serve).

## The questions

1. **The CONFIRMED map, precisely:** trace a command through Matter — Invoke over CASE → per-command status response → subsequent subscription report carrying post-state (+ `DataVersion` increment). For each leg: what it PROVES and what it cannot prove (the Shelly `was_on` lesson has an analogue: an Invoke SUCCESS status is acceptance, not outcome — verify how each device type's spec words it, e.g. OnOff vs Level with transition time vs locks). Map onto our three-level lifecycle + ledger: what is dispatch-ack, what is `state_reported` evidence, what earns `state_confirmed`. Where Matter is structurally STRONGER than Zigbee (versioned reports? subscription push guarantees? ordering?) and where WEAKER/subtler (report coalescing? min-interval suppression of intermediate states? status-vs-effect races?) — each verdict spec-cited.
2. **The ALIVE map:** subscription liveness semantics (max-interval as a staleness ceiling; what subscription-drop proves and doesn't), `Reachable` attribute semantics (who computes it, when it lies — especially on bridges), ICD/sleepy devices (SIT/LIT, check-in protocol — what honest availability means per class ↻ verify current spec state), and the comparator: our mains ping ladder / battery 25 h window / the measured envelopes (doctrine §5). Output: per-device-class honest-staleness-bound table — what we could CLAIM per class without ever risking false-ALIVE.
3. **Bridged endpoints (the honesty frontier):** mechanics of bridge attribution (per-endpoint `Reachable`, bridge-level attestation, Bridged Device Basic Information cluster), what an honest per-endpoint posture looks like in AMD-97 vocabulary (provenance recorded bridge-attested; ceiling options — e.g. cap at best_effort vs a new provenance axis — present OPTIONS with evidence, the design rules), and the competitive verify ↻: do HA / openHAB / SmartThings / Alexa surface any native-vs-bridged evidence distinction today? (Screenshots/docs/source — this claim carries the marketing case; it must survive audit.)
4. **The AMD-97 mapping table:** per plausible V1 device class (plug/switch, bulb, contact/motion/occupancy, lock [even if later], bridge-endpoint): expected characterization (`VERIFIED_REPORTS`? `ON_CHANGE`?), confirmable capabilities, expectation shapes, timeout-seed sources (what the spec's timing model implies pre-measurement), degrade rules (subscription-down → ?; bridge-unreachable → ?), and what the bench must MEASURE per class before the values are asserted (the fixture-paired assert rule applies to characterization values too). This table feeds memo B2 (the scope cut: which device types first) — rank classes by honesty-tractability.
5. **The corpus/bench doctrine for Matter:** where the honest capture point is for session-encrypted Matter traffic (wire pcap is CASE-encrypted — the capture seam moves to the controller's decoded interaction layer; evidence per A1 stack option: what each exposes as loggable interaction records), what captured-stream seeding looks like for Matter sessions (the seeded-log architecture consumes event streams — what a "Matter fixture" is), the virtual-DUT option (CHIP's example apps — `chip-all-clusters-app` etc. — as bench instruments: maturity, fidelity caveats ↻), and the ratchet-rule application (what a Matter field incident → scenario pipeline needs on day one). Honest statement of what gets HARDER than Zigbee here (we owned the Zigbee wire; Matter's crypto means the stack mediates our evidence — name the trust consequence per stack option).
6. **The claim, drafted honestly:** three to five candidate one-sentence competitive claims for OUR Matter integration (the "nobody else renders WiFi-plug commands as evidence-confirmed verdicts" analogue), each with its evidence obligations stated (what must be true/measured before the sentence is honest) — the design and the eventual marketing both consume this. Counsel-gated wording stays out (no certification-mark language — A5's lane).

## Known hazards

- Spec-version drift: pin every spec citation to a Matter version (1.4/1.5/1.6) — subscription/ICD semantics evolved across them ↻.
- The banked "stronger than Zigbee" line is an INFERENCE — your job is to prove, refute, or bound it, not to inherit it.
- Report coalescing/min-interval is where false-CONFIRMED hides (a post-command report might be suppressed or merged) — chase this class explicitly; it is the lane's highest-value finding either way.
- The S31 exhibit is the posture model: when evidence is unverifiable, the system DOWNGRADES honestly — your degrade-rule options must always include an honest-downgrade path.

## NOT in scope

No stack pick (A1/A3/B1), no hardware (A2), no certification (A5), no design decisions (present options + evidence; Phase C decides), no code, no core writes, no gate interaction (J1 FROZEN).

## Return format

`§0` executive digest (≤1 page — lead with the easier/subtler verdict and the strongest candidate claim) → `§1–§6` matching the questions → `§7` open questions BLOCKING / NON-BLOCKING for Phase C → `§8` honest gaps. §4's table renders lift-ready for memo B2.

**Done-when:** the single return file exists at the exact path; every spec claim version-pinned and cited; the easier/subtler verdicts each carry at least one primary citation; the competitive-verify (§3) evidenced or honestly marked unverifiable; the B2 table lift-ready.
