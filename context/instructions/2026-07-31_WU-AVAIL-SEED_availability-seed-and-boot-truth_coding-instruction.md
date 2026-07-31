# WU-AVAIL-SEED — the availability seed + boot truth (core repo)

**Issued:** 2026-07-31 (v42 hub, beat 9) · **Producer:** Coder (host-CC desk session, `homesynapse-core`) · **Baseline:** core `4288a9d`, working tree CLEAN at dispatch (hub-verified this beat) · **Return:** `context/audits/2026-07-31_WU-AVAIL-SEED_return.md` · **Gate-critical:** this WU is **the F2 [M] producer** — the last genuinely-open non-scheduled MUST on the 29-row ledger. Freeze is Aug-14 EOD; the attended F2 rep must run on the FIXED build before Aug-10.

---

## §0 Mission

Close F-14's two defect layers so that **served availability is always evidence-based**: (1) stop manufacturing an evidence-free "available" at boot; (2) read back the sidecar's written-never-read availability seed so silent devices enter tracking and timeouts can fire; plus the restart-clock persistence that makes the 25 h battery path fireable across nightly restarts, and the observability surface that makes the ping arm visible to future instrument reads. **The law this WU serves: never-false-ALIVE.** A brief false-UNAVAILABLE that self-heals on next evidence is the acceptable failure direction; an evidence-free AVAILABLE is never acceptable.

## §1 The finding (F-14, CLOSED at v42 beat 8 — mechanism, source-anchored)

- **L1 — the manufactured boot burst:** `ZigbeeAdoptionSlice` (relink path, `:553`-era) publishes `AvailabilityChangedEvent("unknown", "available")` under the **DEVICE subject** for every registry device, every boot — an evidence-free availability assertion. Instrument-proven: the DEVICE-subject bursts match the boot relink lines to the millisecond; the days-dead Hue rode every burst.
- **L2 — the written-never-read seed:** the adapter constructs `StandardAvailabilityTracker` with a hardcoded empty seed (`Map.of()` at `ZigbeeIntegrationAdapter:318`-era) while `ZigbeeDeviceCache` faithfully persists `lastKnownAvailability` per device on every transition (`zigbee-devices.json`, its own §8.1 M-1 doc) and **never reads it back**. Consequence: a device silent since before the last restart never enters tracking (`recordFrame` never fires; `evaluateAvailabilityTimeouts` iterates only tracked devices), and the projection replays the last logged availability indefinitely.
- **L3 — the unexercised arm (NOT broken):** the mains ping arm (`productionLoop → runCycleOnce → evaluateAvailabilityTimeouts`) has never been exercised against a dead device — the 07-29 boot log shows the Hue was never tracked in any post-07-19 boot (its identify DefaultResponse does not ride `recordFrame`). Do not "fix" the ping arm; the F2 attended rep gives it its first live exercise post-deploy.
- **Aggravator:** seeded `lastSeen = boot` means the 25 h battery timeout resets on every restart — structurally unfireable once the bench suite restarts the stack nightly.

## §2 Standing law binding this WU

- **The ruled boot semantic (Nick, at F1's landing — the boot-UNKNOWN trap):** availability at boot is honest-UNKNOWN until first evidence or an honest timeout verdict. The system never asserts "available" without evidence.
- **J1 is FROZEN** — nothing in this WU touches criteria text; the ledger is hub-owned.
- **Zero bench changes. Zero hivemind changes from this lane.** Core only.
- **The lane commits NOTHING** — the hub's two-layer audit precedes any commit order; return the exact porcelain census.
- **No attribution trailers ever; tokens by file-path reference, never by value; never `set -x` where a token could reach a log.**
- **Build grant (the DASH-SERVE/CMD-API precedent):** the targeted test loop + **ONE full `./gradlew check`** against the final tree + spotlessApply on touched modules. CI on the pushed commit remains the gate of record.

## §3 Design points

### DP-1 — THE SEED (the written-never-read half dies)
Replace the empty construction seed with one derived from the sidecar: per-device `lastKnownAvailability` plus DP-4's `lastEvidenceAt` where present. **Seed semantics (the ruled law):** seeding ENTERS every persisted device into tracking so `evaluateAvailabilityTimeouts` iterates it from the first cycle — but a seeded value **never counts as fresh evidence** and seeding **publishes nothing by itself** (T-3). A seeded mains device that stays silent must reach UNAVAILABLE within one mains evaluation window from boot (T-1). A seeded battery device's timeout clock rides the persisted timestamp (DP-4), never boot time (T-2). If the tracker's internal model cannot distinguish seeded-stale from evidenced, grow it minimally (package-private; no new public types).

### DP-2 — BOOT TRUTH (the served view stops lying)
**The floor (mandatory):** post-boot, a dead seeded mains device is SERVED as UNAVAILABLE within one mains window, with no manual intervention — i.e. DP-1's timeout verdict propagates through the normal publish → projection → read path (T-7). Evidence-free AVAILABLE served beyond that window = defect.
**The stretch (implement if lawful within bounds):** if the read surface's existing `stale` field (the F2 discriminator read `"availability":"AVAILABLE","stale":false`) can honestly mark the pre-convergence window — seeded-not-yet-evidenced ⇒ `stale:true` — implement that; cite the field's current derivation at source in the return.
**Rejected mechanisms (STOP, do not build):** per-boot per-device event floods into the store (a boot storm of manufactured "unknown" transitions is the same disease as L1 — G-2); any read-path mechanism that requires an arch-rule exemption or a rest→integration layering breach (G-3: implement the floor, record the stretch design as an OBS, never edit arch rules from this lane).

### DP-3 — THE RELINK EMISSION (rides Nick's DP-B ruling; both branches pre-ruled)
- **Branch STOP (hub REC):** remove the `AvailabilityChangedEvent("unknown", "available")` publish from the relink path entirely. The relink log line stays. Boot availability is owned by DP-1/DP-2. The DEVICE-subject evidence-free burst dies (T-5).
- **Branch HONEST (if Nick rules to keep an emission):** the emission may assert only what is true at relink time — which under the ruled boot semantic is UNKNOWN; an unchanged-state publish is churn, so this branch reduces to: publish only tracker-truth transitions, never a manufactured "available". (Pre-stated so the ruling costs one word.)
- **The dispatch line carries the ruling.** Absent at session start ⇒ G-4: implement DP-1/2/4/5, leave DP-3 untouched, note it in the return.

### DP-4 — THE RESTART CLOCK (the 25 h battery path becomes fireable)
Persist evidence recency in the sidecar: an **additive** per-device field (`lastEvidenceAt`, ISO-8601 UTC) maintained so a restart does not orphan the battery clock. **Write-rate floor:** written on every availability transition + a coarse periodic flush (5–15 min class; state the chosen rate and mechanism in the return) + a shutdown hook if one exists — per-frame file writes are NOT required. **Pinned reasoning (do not over-engineer):** persisted time is a lower bound on true recency; the worst case is a brief false-UNAVAILABLE that self-heals on the next report — the lawful failure direction. Never-false-ALIVE is the law; false-ALIVE-avoidance always wins ties. **Compat (G-3-class):** additive only; an old-format sidecar (absent field) loads without throwing, and its devices seed with unknown recency handled per DP-1 semantics (T-4).

### DP-5 — OBSERVABILITY (the one-grep instrument surface)
(a) The boot seed line, once per boot, INFO: `zigbee.availability_seeded: devices=N from_sidecar=K unknown=U`. (b) Per-ping outcome, DEBUG: `zigbee.availability_ping: device=<ieee> outcome=<ok|timeout|error> rttMs=<n>` — the arm F-14's instruments could not see. (c) Verify the existing `zigbee.availability_changed` line fires identically on seed-originated timeout transitions. (d) The `availability_publish_conflict` WARN untouched (verified present at `:1140-1165`-era). Grep-stable tokens; document them in MODULE_CONTEXT per WUCP.

## §4 STOP-gates

- **G-1:** any event-store schema change or NEW event type required → STOP, return the design sketch instead of code.
- **G-2:** DP-2's floor unreachable without a per-boot event flood → STOP with the sketch.
- **G-3:** DP-2's stretch demands an arch exemption or non-additive sidecar change → floor only + OBS; never rule edits, never breaking schema.
- **G-4:** DP-3 ruling absent from the dispatch line → skip DP-3 lawfully, note in return.
- **G-5:** pre-code re-verification fails — any §6 pin drifted from `4288a9d` → STOP, report the drift.

## §5 Tests (red-first; fixture-paired — every PASS proves its false-verdict boundary)

- **T-1 (RED at `4288a9d`, quoted):** seeded-from-sidecar mains device, zero frames → UNAVAILABLE within one evaluation window. Pre-fix red reason: `Map.of()` ⇒ never tracked.
- **T-2 (RED at `4288a9d`, quoted):** seeded battery device, persisted `lastEvidenceAt` > 25 h old → the battery timeout fires at first evaluation. Pre-fix red reason: clock seeds from boot.
- **T-3:** construction/seeding publishes ZERO availability events (the anti-churn pin).
- **T-4:** old-format sidecar (absent `lastEvidenceAt`) loads without throw; devices enter tracking per DP-1.
- **T-5 (Branch STOP only):** the boot relink path publishes ZERO availability events; the relink log line preserved.
- **T-6:** a seeded-available device with prompt fresh evidence publishes NO redundant transition (steady-state boots stay event-quiet).
- **T-7 (the DP-2 floor):** integration-level — post-boot, the dead seeded device's SERVED availability reaches UNAVAILABLE within the window (ride the existing projection/read-path test machinery; cite what you reuse).

## §6 Pins (measured 2026-07-31 at `4288a9d` clean; symbols are the anchors, line numbers are hints; G-5 re-verifies ALL before code)

- `ZigbeeIntegrationAdapter.java:318` — `availabilityTracker = new StandardAvailabilityTracker(clock,` … the `Map.of()` construction site (grep-verified this beat).
- `ZigbeeAdoptionSlice.java:553` — `new AvailabilityChangedEvent("unknown", "available"),` — the relink emission (grep-verified this beat).
- `StandardAvailabilityTracker.java` + `ZigbeeDeviceCache.java` carry `lastKnownAvailability` (grep-verified this beat); the cache writes it via `setAvailability`; `zigbee-devices.json` is the carrier.
- `ZigbeeIntegrationAdapter:735`-era — `productionLoop` drives `runCycleOnce → evaluateAvailabilityTimeouts`; `:1140-1165`-era `publishForEntities` with the `SequenceConflictException` swallow + `availability_publish_conflict` WARN.
- `StateProjection.java:856`-era — the `AvailabilityChangedEvent` handler; `ListEntitiesEndpoint.java:160`-era — the read surface.

## §7 Census expectation + return format (WUCP)

Files: integration-zigbee main + test trees, MODULE_CONTEXT.md; nothing outside integration-zigbee unless the DP-2 floor demands a projection/read-path touch WITHIN arch law (name it in §2 of the return if so). Return sections: **§1** P0 re-verification transcript (G-5) · **§2** per-DP disposition with source citations · **§3** the test record (red quotes at baseline + green on the final tree + the boundary pairs; the full-check line) · **§4** the exact porcelain census · **§5** STOP-gate status ×5 · **§6** deviations, severity-honest ([REVIEW]/[INFO]/OBS) · **§7** the DP-2 mechanism memo (what was built, what was rejected, why) · **§8** the next-WU pointer (refuse-to-close: the hub audit precedes any commit; post-deploy, the attended F2 rep proves BOTH directions on the fixed build and gives the ping arm its first live exercise, pairing with the B3 §10 rejoin-race rep).
