<!--
file: context/decisions/2026-06-28_bench-test-and-truth-engine_decision-record.md
purpose: The locked strategic reframe of the hardware bench (from "device bring-up for M9" to "the test-and-truth engine") + Nick's five co-signed rulings that flow from it. The durable record the three-stream plan, nexsys-bench, the research dispatch, and the future hardware-grounded-E2E milestone all build on.
audience: the PM hub (reconciles the three streams), the bench lane (Stream A / nexsys-bench), the device-model research lane (Stream B), the Coder (M9 consumes this), DOCS governance (Doc 02/08 + the future hw-E2E seam).
state-type: decision record (strategic; co-signed)
status: RATIFIED 2026-06-28 (Nick co-signed the reframe + the five rulings in-conversation; v10 hub authored).
anchors: context/planning/2026-06-22_hardware-bench-bringup-and-device-characterization_brief.md (the method this reframes/elevates) · context/decisions/2026-06-25_deeper-M7-automation-architecture_decision-record.md (D2 replay-purity — the machinery this leverages; D5 converter-DB — the model the research realizes) · homesynapse-core/lifecycle .../RunPipelineReplaySafetyTest.java (M7.4d — the seeded-log replay proof the bench feeds real data into) · project-knowledge/device-corpus/ (the corpus, migrating into nexsys-bench).
-->

# Bench = the Test-and-Truth Engine — Strategic Reframe + Five Rulings (2026-06-28)

## 1. The reframe (RATIFIED)

The hardware bench is **not** "characterize two devices so M9 has ground truth." It is **the durable engine that turns real-world device behavior into permanent, fast, hardware-free regression tests of HomeSynapse's program logic** — and the thing that converts the differentiator from a design claim into a measured, regression-protected fact.

**The unlocking identity:** *a captured real device event stream is a seeded event log.* M7.4d (`RunPipelineReplaySafetyTest`) already proves we can seed a log, replay it deterministically, and assert the engine's behavior — today, with **synthetic** events. The bench swaps synthetic for **real** (the real report cadence of an SNZB-03P, the real confirmation behavior of a Hue, the real messiness). Transform a real capture into our event-log format once, and **every real-world interaction becomes a deterministic, CI-able regression test with no hardware in the loop at test time.** The event-sourced architecture is precisely what makes real data into a durable test moat; the bench is what feeds it.

**Two consequences locked by this:**
- **(a) The capture harness de-risks M9 directly, not just downstream.** The harness's Zigbee→event-log *transform* shares DNA with the M9 adapter's interview/codec. Building the harness is a head-start on M9, not merely a feeder for it.
- **(b) A future hardware-grounded-E2E milestone is implied.** The real-capture→replay suite, wired as a CI gate extending M7.4d. **Reserve it as a seam now; capture toward it; do not build it yet.**

**The moat is the headline capture target, not a byproduct.** Specifically measure: does a real Hue report the expected state back (→ a genuine `CONFIRMED`)? Does a non-confirming device yield an honest `UNCONFIRMED` rather than a false positive? That measurement is where the durable `confirmed | unconfirmed | failed` differentiator stops being a design assertion.

## 2. The five rulings (co-signed)

**R1 — Replay-as-regression: adopt; capture toward a replayable event-log format from day one.** Honor the raw-vs-transformed split: **capture rich RAW now** (model-agnostic, zero rework — interview + full message stream + timestamps + raw cluster/attribute values), and do the **transform-into-our-event-log AFTER Stream B settles the model**. Discipline: **"capture reconstructable truth, never notes"** — so the later transform is lossless. Keep fixtures as **compact text (event-log JSON)** — git-native, diffable, small (a second reason the replay-toward-log format is right: the regression suite lives in version control, not binaries).

**R2 — The bench gets its own repo: `nexsys-bench` (the FIFTH repo).** It is not production code (out of `homesynapse-core`'s tree / JPMS graph / CI / bundle) and not throwaway (it is infrastructure-as-code + the harness that seeds the long-term onboarding pipeline). Stand it up as its own GitHub repo on the `nexsys-skills` pattern — own CI, own history, own `.gitignore`. Fixtures as text; any unavoidable raw binary dump is gitignored/LFS'd, but the event-log-JSON form is preferred. It is **write-isolated to the bench stream**; its returns reconcile into the spine at the hub. The commit-push-before-launch discipline is now **five repos: core / docs / hivemind / skills / bench.**

**R3 — Networking: wired Ethernet, onboard 2.4 GHz radio OFF — correctness, not polish.** A bench host transmitting on Zigbee's band next to the coordinator contaminates the measurements. Pi on wired Ethernet; Wi-Fi/2.4 GHz radio off the air; coordinator on the USB extension (in the Wave-1 kit), away from the Pi body. Build the IaC to **assume wired + radio-off**, but document the fallback (5 GHz only, power-save off, dongle-on-extension) so it is reproducible either way. **Fold dongle bring-up into Phase 0:** the udev rule (stable symlink + autosuspend OFF — autosuspend dropping the coordinator is a real failure mode; assessment showed `autosuspend=2`), and the **NCP firmware reflash** for the factory-MG24 `ASH_ERROR_TIMEOUT` cluster (AMD-96 research) — **reflash during bring-up, not after measuring on bad firmware.**

**R4 — Capture approach: ZHA-first + our own thin harness (hybrid).** Lead with **ZHA/bellows** for first-light (bellows is the mature EZSP path; prove motion→light fast; keep ZHA as the cross-check reference + the pairing UI). Then build **our own thin zigpy/bellows capture harness** for the reproducible, replayable fixtures (our code, CI-able, the M9-adapter precursor). **Cross-validate** our harness's captures against ZHA's view before we trust our fixtures. Do not over-bias to our-own-code at first-light — ZHA de-risks the bring-up; the harness earns its place the moment the hardware is proven.

**R5 — Stream B (device-model research) scope: confirmed + three sharpenings.** Survey device-representation models (HA `components/` · Z2M converters/`exposes` · zigpy `zha-device-handlers` quirks · deCONZ DDF · Matter device-types/clusters), evaluate against **local-first / event-sourced / ZCL-aligned / must-degrade-honestly**, return a concrete **corpus model + onboarding-pipeline** recommendation. Sharpenings: **(a)** it must **realize the RATIFIED D5** (adapt-the-data + curated-subset fallback) and **Locked Doc 02** — frame as "the corpus model that realizes D5," not a greenfield that could contradict locked decisions; **(b)** it must **first-class the confirmation semantics** (does the device confirm? its expected-outcome / `ConfirmationMode`) — the corpus supports the confirmed/unconfirmed moat, not just clusters; **(c)** it must **return the onboarding pipeline** (interview → corpus → device-model → M9 acceptance), the durable thing the bench harness seeds. Web-backed source discipline (honest UNVERIFIED flags). Launch now — parallel to Phase 0/1, upstream of Stream A Phase 2.

## 3. The three-stream orchestration (single-spine-writer, done right)

- **Hub (this conversation lineage):** sole spine-writer; reconciles all three streams' returns.
- **Stream A — the bench** (`nexsys-bench`; Nick's hands + hub orchestration; write-isolated): Phase 0 make-the-instrument (Pi → durable host + ZHA + dongle/firmware) → Phase 1 raw ground-truth capture (interview + replayable fixtures; the moat measurement) → Phase 2 (post-Stream-B) the durable corpus model + the transform + the replay-test substrate.
- **Stream B — device-model research** (write-isolated research session): R5 scope. Returns the model + pipeline; feeds Doc 02/08 + M9 + Stream A Phase 2.
- **Stream C — Core** (Coder/Claude Code; low-touch but MOVING): M7.5b is the next Core slot — must not let the bench's gravity starve the critical path.

**Convergence:** Stream A raw captures + Stream B model → the durable corpus + the replay-test substrate → M9 acceptance + Doc 02/08 amendments + the hardware-grounded regression suite (the reserved seam).

**Forward note (later trigger, not now):** once the bench pattern is proven, it becomes a `nexsys-bench` **skill** on the exact playbook `nexsys-frontend` just validated — captured here, not instantiated.
