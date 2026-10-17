<!--
file: context/audits/2026-10-17_v112-b6_DELIB-PACK_source-pack.md
purpose: the source pack for the deliberation (DELIB-1): Nick's §B–§D of 2026-10-12 claim by claim against the record; the six anchors (IR-197's transport · the 4-GB board · 17.8 GB/yr · the replay numbers · the seven weeks · the 2027 skeleton); the R&D guide mapped; what moved since Oct 12; eight open questions; seven contradictions — every row cited.
audience: the v113 hub (the deliberation) · ROADMAP-1
state-type: audit input (a hub-side source pack)
status: FILED v112 b6 (Sat 2026-10-17) — compiled by a hub-side helper at hivemind `f9ab3ed`, core `176adad`, docs `e2a5844`, bench `7e03c81`; its script re-read 69 cited lines; the hub re-reads every row the deliberation rules on
-->

# DELIB-PACK — Nick's §B–§D (2026-10-12) against the record

Source pack for Sunday's deliberation. Read 2026-10-17: hivemind `f9ab3ed` · core `176adad` · docs `e2a5844` · bench `7e03c81`.

**Paths** (in `nexsys-hivemind/context/` unless named): DR110/111/112 `planning/2026-10-1{2_v110,4_v111,6_v112}_decision-record.md` · IR, MR `planning/{improvement-register,measurement-record}.md` · HZ `planning/2026-10-02_v93*` · H1 `research/2026-10-12_HORIZON-1*` · in `audits/`: H1A `2026-10-13_v110-b3*`, D2A `2026-10-14_v111-b1*`, G2A `2026-10-15_v111-b2*`, S1A `2026-10-15_v111-b3*`, BCA `2026-10-17_v112-b3*`, DRN/DRO `2026-10-12_DRY-RUN-1_Mon_{guide-notes,raw-outputs}.md`, RIL `2026-08-22_R10-IN-L*` · LA, LV `assessments/2026-06-06_{core-language,rust-velocity}*` · PMH `handoff/pm-handoff.md` · SY `status/state.yaml` · GD `strategy/2026-10-15_RD-GUIDE*` · UC `instructions/2026-10-12_unit-cards*` · O2 `strategy/2026-10-12_OUTREACH-2_two*` · LTD `homesynapse-core-docs:governance/*Locked_Decisions.md` · BAR `nexsys-bench:docs/2026-07-06_m9.4-bench-acceptance-record.md`.

## 1. §B–§D claim by claim → the record now
Verbatim from DR110:27–97. Cited, not quoted (the cap): :28–36 (the intake's form; v109's findings, ruled 24 ACCEPTED · 5 CORRECTED · 9 DEFERRED, H1A:11), :42, :57–58 (costs, gains → C1–C6), :67–68 (prior art → C8), :86.

- **B1** :37 «PI-2's coordinator: a firmware probe in PI-2's card before Tue Oct 20; reflash 7.4.5.0 if it reports v14 (analysis §2, item 2).» → **REFUTED for the MG24**: no 7.4.x image could be named Oct 15 (DR111:224). **Re-planned:** `KIT-DONGLE: both` — the MG21 coordinates the pilot, its first PI-2 pairing a corpus entry (DR111:234); `KIT-ORDER:` open, needed Tue (DR112:123).
- **B2** :38 «GATE-2: its evidence first (the landed `timeout_causes` classifier over the S31 corpus), then my stance (N3) by Oct 22.» → **DONE; re-dated:** 1,714 timeouts = Hue 1,671 · S31 43 (G2A:12); `N3:` by Oct 20, rec (c) (DR111:233; G2A:49).
- **B3** :39 «SCHEMA-1: chartered for Nov 2, not Oct 20» → **DONE early** (S1A:11); `RETENTION:` by Nov 2, rec (c) (S1A:49).
- **B4** :40 «N1 (counsel: the filing receipt; the two instruments) is mine this week.» → **OPEN; the pilot's long pole:** no answer on record (SY:85); the consent needs re-scoping for LICENSE (b) (IR:228); the flip or a per-household permission precedes the first outside install (IR:229).
- **B5** :41 «HORIZON-1's 12 sessions plus RUNTIME-1 (§C) must fit my ≈ 30 h/week until December, against THE HORIZON's rows.» → **CONFIRMED on paper:** 11 sessions, ≈ 29 of Nick's hours in nine weeks; RUNTIME-1 "measurement, not a session" (H1A:77). Hours spent UNKNOWN.
- **B6** :43–46 pass 2 by v110's close, ending «the outline of pass 3.» → ruling and map MET; **the outline NOT MET, carried twice** (DR110:218; DR111:145) → Oct 18 (DR111:233).
- **B7** :47 «Pass 3 is one strategy of record, v2, by Dec 1. It replaces the scattered strategy files rather than adding one» → **UNTESTED:** ROADMAP-1 Nov 10 → Dec 1, 10 h (H1A:72); one strategy file added since, the guide (DR112:113).
- **B8** :49 «the one-way doors, with their dates» → **dated, scattered:** `LICENSE:`/`RETENTION:` Nov 2; flip Nov 3–9 (IR:211); on-disk format at the first household event, Nov 19 (H1:19; GD:131), IR-214's upcaster first (DR112:111); ACK-1's vocabulary not Nov 2–19 (IR:206); the name (H1:57).
- **B9** :50–51 «the R&D program; the 2027 skeleton the December ruling chooses among» → §3, A6.
- **B10** :52 «the language/runtime ADR (§C)» → the ADR of record is LTD-01, reversal at RSS > 2.5 GB, GC > 500 ms, carriers > 75 % (LTD:71), Locked path (RIL:81).
- **B11** :53 «the process and skills plan» → PROCESS-2 Nov 3 → Dec 14 (H1A:73), behind AVAIL-2 (DR111:236).

- **C1** :56 (§C: the v109 hub's position, to test, :55) «where does a second language earn its cost?» → **CONFIRMED by prior record:** Jun 6 — harden Java; a Rust sidecar at the INV-RF-01 seam only on a real requirement (LA:33); AI lanes "measurably more productive in Java than in Rust today" (LV:100); its spike (LV:86): no return.
- **C2** :60 «None of HORIZON-1's bottlenecks is a language problem: F1 is a pragma, F18 an O(n) scan, F27 sequential probes, F25/F26 protocol handling, F28 firmware.» → **CONFIRMED, strengthened:** each has a non-language fix (IR:203–213); IR-148, which looked like JVM startup, was a whole-log walk, fixed in Java (A4).
- **C3** :61 «Java is already memory-safe (the NSA/CISA guidance lists it beside Rust).» → CONFIRMED (LA:25).
- **C4** :62 «The JVM's real costs are footprint and startup (`-Xms512m -Xmx1536m` under `MemoryMax=2G` means a 4 GB Pi in practice), plus the watchdog's missing transport (F6: a stock JDK can't send `sd_notify`'s datagram).» → **SHARPENED:** startup is not today's cost (A4); footprint unmeasured at scale (A2); transport A1.
- **C5** :63 «The strongest case for Rust is the board: at fleet scale on a 1–2 GB board, a JVM is tight.» → **UNTESTED, no target:** no 1–2 GB board or BOM on record; PI-2's RAM UNKNOWN (UC:88); Pi 5 2 GB $55 · 4 GB $70, Dec-2025 list (H1:495): $15 a hub.
- **C6** :64 «Cheaper fixes to verify: JDK 25 LTS (FFM is final, so `sd_notify` via libsystemd; the AOT cache for startup; compact object headers), heap tuning, and GraalVM native-image as a measured option.» → **UNTESTED:** 25 amends LTD-01 (LTD:46, :50); 21 supported ≥ Dec 2029 (H1:496); AppCDS already in the 21 image path (core `distribution/image/build-image.sh:153`); the Jun 6 native-image spike (LA:35): no return.
- **C7** :65 «Nothing measured on the Pi exists on record for memory, startup or boot-to-ready.» → **REFUTED** (X1).
- **C8** :66 «at most one native language, and it is Rust; no new C/C++» … :69 «firmware for a device of our own, if we ever make one (embedded Rust, e.g. Embassy).» → (a) agents: consistent (IR:208; APPLIANCE-1 Q1, H1A:76). (b) MATTER-1 **SHARPENED:** `Confirmability`, `DeviceProfile`, `ReportingPosture` are Zigbee-module types; no mature Java Matter SDK; CSA ≈ $7k/yr + $3k/cert (H1:474). (c) X4.
- **C9** :70 «Java stays for the event store, the automation and explain engines, availability (R2) and simulation (R1). Probably also the fleet engine» → consistent (H1A:75); LICENSE (b) splits the fleet engine by license (IR:211).
- **C10** :71 «The boundary is a process, not FFI … The sidecar publishes into the log as an adapter» → UNTESTED; "an in-JVM plugin can forge the attribute reports" (GD:120) bears on any publishing adapter.
- **C11** :72–76 «Revisit when:» (board/BOM · MATTER-1 · own device · C/C++) → **one fact, two places:** LTD-01's own triggers (LTD:71); the guide plans our own device for 2027 (GD:17, :125).
- **C12** :77 «no new-language code before the run, and nothing in the pilot's path.» → CONFIRMED (SY:98).
- **C13** :78–85 «RUNTIME-1: research plus one Pi measurement, post-run or on a spare card (never the run's).» It measures «memory, startup and boot-to-ready on JDK 21 vs JDK 25 (with the AOT cache) vs native-image; the FFM watchdog; the appliance-OS assembly options; Matter's process model; the BOM threshold at which a smaller runtime pays.» → **HALF-SCHEDULED:** PI-2's SSD boot Tue is the first point (DR111:215); the rest undated; the ADR "is pass 3's" (H1A:77). The guide keeps experiments off PI-2, "the first household's hub" (GD:113); no spare Pi on record.

- **D1** :89 «Adopt the v109 analysis §4 rules at once» (:90–94 the five) → **PARTLY:** adopted (DR110:189); a cap raised by named edit (DR111:227); no retirement rule, laws accrue (DR111:245; DR112:128); one fact, one place: the measurement ledger stopped Sep 28 (MR:6), so 17.8 GB/yr, 92 k/s, 0.584 s live in audits only.
- **D2** :95 «the share of commits that touch the spine, and my cards this window» → 75 % · 7 cards (DR110:219); 100 % · 9 (DR111:244): the share rose.
- **D3** :96–97 «PROCESS-2 designs the rest … fewer, denser artifacts» → not started; DR bytes 32,551 · 71,058 · 28,006 (v110–v112).

## 2. The six anchors
- **A1 IR-197's transport.** IR-197: a stock JDK "has one: `NotifyAccess=all` + `systemd-notify --ready` / `WATCHDOG=1` from a child process … Not yet proven" (IR:208; H1A:20). August priced it lower: a short-lived child's message may be ignored "even if NotifyAccess=all is set"; `--pid=` needs privileges the unit lacks (RIL:79); "process-per-heartbeat is poor on a Pi" (PMH:141); FFM is "the best transport by every column" once the pin moves (RIL:81); rec T-0, ruled HOLD Sep 4 (RIL:109; PMH:143). Today `Type=exec` (core `distribution/systemd/homesynapse.service:24`): the pets go to a no-op (core `HomeSynapseCore.java:1852–1860`). **Corrected, contested, untested.**
- **A2 the 4-GB board.** LTD-01's Constrained tier: "Raspberry Pi 5, 4 GB RAM" (LTD:52) = hs-dev-1 (DRN:91). Only JVM RSS on record: 204,608 / 212,240 KB at 13,790 events, July (BAR:41); at 2.32 M UNKNOWN until PI-2. Page cache: 3,511 MiB available, Core stopped (DRO:116); the 1.16 GB store (BCA:25) at +48.4 MB/day passes it ≈ Dec 8 (arithmetic). Guide: "the 4 GB and single-SQLite ceilings above about 200 devices" (GD:133); an AI HAT+ 2 needs the SSD's PCIe lane (GD:112).
- **A3 17.8 GB/yr.** D2's `du`: 48,812,032 B in 24.194 h = 48.4 MB/day, 504 B/row; 96,879 rows/day × 365 × 504 B = 17.8 GB/yr (D2A:34); the 17.5 ruling (501 B/row × 95.6 k rows/day, H1A:19) stands within 2 % (DR111:172). Ten devices, 64–66 % `state_reported` (D2A:33): posture first. Retention rule 2 settles the rig at 2.06 GB, a 60-s home at 0.86 GB (S1A:28).
- **A4 the replay numbers.** `37f05a9` (dry-run #1, 1.88 M events): cold exit 99 at +49.6 s, the walk unfinished 45.4 s after `Loaded` (cold < ≈ 41 k events/s, arithmetic); warm registry +20.4 s, ≈ 92 k events/s (IR:159). `176adad` (BC10, 2.32 M): `Loaded` +1.415 s, registry +1.999 s (0.584 s cold · 0.131 s warm), radio +13.868 / +9.730 s (BCA:18, :28); IR-148 CLOSED, no pre-warm (IR:200). A normal boot is O(tail); "45 s" = a 4.11 M-row state rebuild at the warm rate, computed (S1A:26, :28). UNKNOWN: cold s/1e6 events; year-three boot (H1:126).
- **A5 the seven weeks** = Oct 13 → Dec 1 (DR110:170, :47): Oct 18 rollback + this deliberation · 19 sitting · 20 PI-2, `N3:` · 22–23 dry-run #2 → freeze · Oct 30–Nov 2 the run (DR112:33) · Nov 2 `LICENSE:`, `RETENTION:` · Nov 3–9 flip, TAIL-1 trial (IR:211, :203) · Nov 10–18 HYGIENE-1 (IR:207) · Nov 18 two gates (fresh-card E2E; filing receipt) or outside installs slip to December (HZ:14) · Nov 19–25 first outside install (IR:229) · ROADMAP-1 Nov 10 → Dec 1 (H1A:72).
- **A6 the 2027 skeleton.** None before Oct 15 (H1:42). ROADMAP-1: three beachhead briefs, the Dec 1–14 procedure, a 2027 quarterly plan (H1:111); Q1 named APPLIANCE-1, MATTER-1, PROVENANCE-1, LEDGER-1, MESH-1, PROBE-1, MODEL-1, SIM-1 (H1:116; H1A:76). Guide: Dec–Mar harden, 5–10 homes; 2027 B-1 → B-2 kernel → B-3 shadow proposers → B-4 counterfactual replay, chain live, first signed witness (GD:16–17); its sequencing chart is not in the filed bytes (GD:161).

## 3. The R&D guide (read whole) → rows
- **T1** power/storage/time → B8, A3, A4; its write bound, "roughly 2.7 GB a day" (GD:60), is IR-213's open number (IR:224), RETENTION (c)'s test (S1A:49).
- **T2** radio → B1, C8. NEW: the PCIe link "radiates near 2.5 GHz too" (GD:72); PI-2's SSD rides it.
- **T3** statistics → B2 (185 CONFIRMED of 3,009, GD:9). NEW: error bars; ≈ 200 induced failures per class for "< 1.5 %" (GD:86).
- **T4** floor → A6. NEW: the hazardous-load gate (GD:101); Doc 08's decoupled mode (GD:96). **T5** AI → C5, A2. NEW: no proposer seam (GD:40).
- **T6** trust → C8, C10. NEW: Doc 15's TPM claim is wrong (GD:121); `chain_hash` is zeros (GD:38). **T7** scale → A2–A4, B3, X6; its first experiment is A4's UNKNOWN (GD:137).
- Sensing branch (GD:140), P-12..P-15 (GD:154–157): NEW; rows only after this test (DR112:113). Method additions (GD:246) → D1.

## 4. Moved since Oct 12
Dry-run #1/D2 (A3, A4; 57 % timed out, IR:202) · Oct 13 HORIZON-1 ruled (H1A:11), the mandate, `KIT-STORAGE: a` (DR110:125, :134) · Oct 15 GATE-2, SCHEMA-1, BP11, claims §0 5–7 (DR111:225), `KIT-DONGLE: both` · Oct 17 T-B + GO (DR112:111) → IR-148 CLOSED (DR112:127); LICENSE-1 → IR-217..219 (B4; DR112:121–123); PKG-FRESH-1b into PI-2 (DR112:131) · open: `KIT-ORDER:`, `N3:`, `LICENSE:`, `RETENTION:`, `N1:`, `OUTREACH:` (SY:85–86).

## 5. Open questions for Nick
1. 2027 frame: HORIZON-1's Q1 lanes (H1:116) or the guide's B-1..B-4 (GD:17)?
2. Is a 1–2 GB board a target? Is PI-2 4 or 8 GB, and the first household's hub (GD:113)?
3. Does "no new C/C++" bind the signed node (GD:125)?
4. Watchdog: IR-197's child pet post-run, or FFM with 21 → 25 (RIL:81) — and when?
5. By Nov 25: one outside household (GD:15), two (O2:38) or three (HZ:94)?
6. RUNTIME-1's comparisons: hs-dev-1 on a spare card, post-run?
7. Keep-everything passes the board's free RAM ≈ Dec 8 (A2): accept rebuild exposure until the snapshot rule?
8. The runtime ADR: amend LTD-01 (one place) or a new record?

## 6. Contradictions found
- **X1** C7 was false on Oct 12: RSS (BAR:41); boot stamps, Sep 28 (MR:35).
- **X2** IR-197 corrects F6 without RIL:79's caveat or PMH:141; H1A:20's "FFM … not the cheapest" vs RIL:81.
- **X3** B1's MG24 reflash: no 7.4.x file could be named (DR111:224).
- **X4** C8(c) vs the guide's node on the nRF Connect SDK's Zigbee add-on or an EFR32MG24 (GD:125); no Rust Zigbee stack in the record.
- **X5** §D «lighter, now»: spine share 75 % → 100 % (DR110:219; DR111:244); the cap rose (DR111:227).
- **X6** GD:133's "about 45 s against a 30 s boot gate": a normal boot is O(tail); 45 s prices a rebuild (S1A:26).
- **X7** Nov 25's pace: GD:15 · O2:38 · HZ:94 disagree.
