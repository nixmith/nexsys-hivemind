<!--
file: context/audits/2026-08-04_REV-1_audit_v45-beat-7.md
purpose: The hub's two-layer audit of the REV-1 physics-spine adversarial-review return — layer-2 byte-verification census, the ACCEPT verdict, the adoption/disposition table, and the two rulings escalated to Nick (the brand-claim reading; F-3's pre-freeze slot). Filed per chat-is-not-a-storage-tier before any adoption banks.
audience: Hub (v45), Nick, the charter beat
state-type: audit adjudication (point-in-time)
status: FILED 2026-08-04 (v45 hub, beat 7)
provenance: Return = context/audits/2026-08-04_REV-1_physics-spine_adversarial-review_return.md (delivered Aug-4, four days early; on-disk as untracked at intake — the lane committed nothing, correct). Layer 2 = hub spot-checks at host bytes, core @ 60d3ab5 (porcelain CLEAN at intake — the read-only law held).
-->

# REV-1 Audit — ACCEPT (v45 beat 7)

## 1. Verdict

**ACCEPT — zero violations; adopted at severity as filed (1 HIGH · 4 MED · 3 LOW · 8 NOTE · 3 refutations).** Layer 1: Section-0-compliant end-to-end — FACT/INFERENCE labeled with confidence, refutations recorded (§5) so they are not re-hunted, an honest per-scope coverage statement including what was deliberately NOT read, the one external source disclosed with its verification limit stated and a bench-pin rider attached (the 0x3F wire layout), pricing arithmetic internally correct (5.19/300 ≈ 1.7 %; 30/300 = 10 %). The lane's incident handling was lawful (the stale `index.lock` moved aside per env-model §4 and disclosed; scratch tars disclosed).

**Layer 2 — 8/8 load-bearing cites byte-verified at host (core @ `60d3ab5`):** `ExactMatch.evaluate` equality-only (:24–28) · the `ReportDeduplicator` design-intent javadoc VERBATIM (":26–28 — a periodic reporter emitting an unchanged value … is a genuine report, not a twin") + the ≤10 s/TSN twin logic (:81–88) · `DEFAULT_CONFIRMATION_TIMEOUT_MS = 30_000` (AMD-90, `PendingCommandLedgerAssembly.java:50`) · the `ZclIngestionUnit` silent `continue` on unrecognized frameIds (:266–268; no 0x003F constant in the file's callback set) · `FRAME_SEND_UNICAST 0x0034` + `APS_OPTIONS_RETRY_ROUTE_DISCOVERY 0x0140` with the RETRY|ROUTE_DISCOVERY javadoc (:112, :124) · `ZigbeeDeviceCache.write` in-place `Files.writeString` (:470–472, its own comment covering racing writers but not torn writes) · `PersistentNetworkParameterStore` temp-then-move (:134–136 — the in-module contrast that makes F-3 sharp) · `PlatformThreadWriteCoordinator.submit`'s interrupt path leaving the item queued (:80–98). The F-1 ledger cite (:427–452) was independently grounded at beat 5 (:421–442 read) — consistent.

## 2. Adoption and disposition (the hub's resolve-locally rulings; two items escalate)

| Finding | Adopted | Disposition |
|---|---|---|
| **F-1/S-2** value-match confirmation accepts non-causal reports (HIGH) | YES — mechanism source-certain; field-corroborated (R-9 cadence) | **ESCALATED — RULING R-A to Nick (below), pre-freeze.** Mechanical fix space = post-gate, folded into candidate (iii)+S-1 |
| **S-1** delivery-phase gap (evidence requested via APS-ack, then discarded) | YES — CONFIRMED at source | Candidate (iii)/P2 charter package: the spec'd seam + the 0x3F bench pin (§6.2) + N-7's DEBUG counter rider. Post-gate |
| **F-2** REPLAY doesn't re-derive supersession (MED) | YES | Post-gate shelf BY NAME + one rebuild-equivalence test noted |
| **F-3** sidecar written in place, non-atomically (MED) | YES | **ESCALATED — RULING R-B to Nick (below): pre-freeze micro-WU S-5c (REC) vs shelf** |
| **F-4/S-4** shutdown/watchdog race (MED) | YES — PARTIAL, bounded, no next-boot corruption | Post-gate hardening pair (stop-guard + close-before-interrupt). The S-4 residual log-grep JOINS the next Pi-trip block with the Aug-4 settle-terminal read |
| **F-5** WriteCoordinator interrupt = failure-reported-but-still-executes (MED) | YES | Post-gate: drain-cancel or contract documentation + caller audit |
| **F-6/F-7/F-8** (LOW ×3) | YES | Post-gate shelf BY NAME with the return's suggested dispositions carried; F-8's intended-vs-accident question rides to Nick AT the shelf ruling |
| **S-3** mesh-warm survey | YES | The two carriers recorded as candidate-(iii) design inputs; nothing pre-freeze (B3.3 needs none of it) |
| **N-1..N-8** | YES as NOTEs | N-4 (synchronous=NORMAL power-cut caveat) → one docs line RIDES S-6 (the DOCS fold); the rest ride the shelf/charter record |
| **R-1/R-2/R-3 refutations** | YES | Banked so the classes are not re-hunted; R-1's temp-then-move is the model F-3 copies |
| §6 next-reads | YES | Items 1–2 join the Pi-trip/pre-build blocks as stated; 3–5 shelf; 6 follows RULING R-A |

**Interplay recorded:** night-2/3 EDGE-PROVEN is NOT disturbed (the return says so and the coincidence arithmetic already priced this mechanism); the blockR settle-caveat is now CLOSED AT SOURCE in the confirming direction. The C-2/DO-NOT-SAY draft gains its first engineering-sourced entry regardless of R-A's outcome: no external claim of delivery-proof until delivery evidence ships.

## 3. THE TWO RULINGS (escalation format)

**RULING R-A — which reading does never-false-CONFIRMED bind? (F-1; pre-freeze; blocking: NO)**
- *(a) STATE-TRUTH (PM REC):* the claim asserts the state view matches the commanded value on real device evidence — TRUE today, zero pre-freeze code; the execution-evidence gap becomes a NAMED, DOCUMENTED limitation (the C-2/DO-NOT-SAY language + one docs line), and S-1/candidate-(iii) upgrade the claim post-gate. Honest because we say exactly what we measure.
- *(b) EXECUTION-EVIDENCE:* requires pre-freeze mechanical change (edge-qualified or delivery-gated confirms) on the critical honesty path days before the freeze — the highest-risk class of change at the worst time.
- PM recommendation: **(a)**, with the limitation language authored at C-2 THIS WEEK and the mechanical closure chartered by name.

**RULING R-B — F-3's slot (blocking: NO):** *(a) PM REC:* pre-freeze micro-WU **S-5c** — copy the in-module temp-then-move idiom to `ZigbeeDeviceCache.write` (+1 torn-write test); small, mechanical, and it protects the F2 producer (a banked MUST's evidence chain) on SD-card power-cuts. *(b)* post-gate shelf. PM recommendation: **(a)**.

## 4. Standing

Beat-6 landed `b4366ef` (exactly 4, pushed). B3.3 + S-5a desk returns PENDING — **the critical path: B3.3 must land audit → commit → Pi pull BEFORE tonight's 04:30 fire.** Scratch cleanup at Nick's leisure (outside git): `_scratch/rev1_core_60d3ab5.tar` · `rev1_hivemind.tar` · `dashboard_1c800b5.tar` · `_to_delete/index.lock.rev1` · the two v44 0-byte temps.
