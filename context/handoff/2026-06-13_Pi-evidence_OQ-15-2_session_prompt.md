<!--
file: context/handoff/2026-06-13_Pi-evidence_OQ-15-2_session_prompt.md
purpose: Next-PM-session brief — the GUIDED PI EVIDENCE RUN: Pi readiness → pi4-validation.sh first exercise → the M5-D AES-GCM write-path microbench → OQ-15-2 RESOLVED (the MVP encrypted-scope list fixed) → M6.3 gate 1-of-3 closed + the C9 energy-scope reconciliation input. Carries a PINNED STATE block + the guide-and-paste interaction model (the sandbox cannot reach the Pi).
audience: PM (next Cowork session), Nick (runs every on-device command)
status: READY — authored 2026-06-12 at the ratification/hygiene closeout. The Pi is powered on and Nick is at the keyboard; this is the M6-critical-path unlock that has slipped three weeks.
-->

# Session Brief — Pi Evidence Run: OQ-15-2 Microbench (+ pi4-validation first exercise)

PM session (nexsys-project-manager skill). **Read `context/process/cowork-environment-model.md` FIRST** (§5 now carries the bulk-edit source rule + line-anchored-heading corollary, both paid for 2026-06-12). Then the freshness preflight vs the PINNED STATE below — one glance per check.

## INTERACTION MODEL (this session's defining constraint — read before anything)

**The Cowork sandbox has NO route to the Pi** (Tailscale/SSH live on Nick's machine, outside the sandbox). This session is a **guided evidence run**: the PM produces exact, copy-paste-ready command blocks; **Nick executes them in his own terminal (`ssh pi`, user `homesynapse`, host `hs-dev-1`) and pastes RAW outputs back as fenced blocks**; the PM analyzes each paste before issuing the next step. Rules: (a) one verification-bearing step per exchange — never stack commands whose later steps depend on earlier outputs; (b) NEVER assume or fabricate an output — wait for the paste; (c) transcribe result numbers into the spec's §8 block EXACTLY as pasted (host file tools); (d) long benchmark runs: give Nick the command + expected duration, let him return with output when done.

## PINNED STATE (verified 2026-06-12 at the hygiene closeout — trust, then spot-verify)

- **Ratified ground:** AMD-88..93 + B2 C8/C9 **RATIFIED 2026-06-12**; on-disk watermark **AMD-93**; invariants **163/47**; AMD-04 SUPERSEDED. **M7 entry-gate: rows 1–2 + 5 ✅ · row 3 ⛔ (the M6.3-vs-M7 ordering call — needs the microbench [THIS SESSION] + the energy/erasure interviews [Nick, human work]) · row 4 ⛔ (M5-C Increment 1).** M6.3 triple gate: OQ-15-2 (THIS SESSION) + AMD-86 §3 interview signal + OR-M6-NONCE (rides the M6.3 instruction authoring).
- **Shas:** core `e5ea76f` (substantive `7c73c91`) — GREEN 147, pins 55/24/36, `projectionVersion` 5 · docs `d7ea212` · hivemind `988ea4d` **+ expect one small straggler commit** (the two `project-knowledge/CLAUDE_PROJECT_*` custom-instruction sources — Nick's `git add context/` missed them; verify committed at Step-0, flag if not).
- **Check 9:** Nick reports repos/spine synced — verify with one `diff -rq` glance; PASS or the known one-file STALE both acceptable. **`index.lock.cleared-by-cowork-2026-06-12`: verify deleted — if STILL present this is the FIFTH flag; make it loud.**
- **Hot-path state:** snapshot 107K / cross-agent 18K / pm-handoff 59K post-rotation; the CURRENT POINTER is the 2026-06-12 RATIFIED one.
- **The Pi (from Current_State §7):** Raspberry Pi **5** dev unit `hs-dev-1`, Kioxia BG4 256GB NVMe at `/var/lib/homesynapse` (ext4, noatime, label `homesynapse-data`), Tailscale, `ssh pi`, user `homesynapse`, Corretto 21 via apt, systemd `MemoryMax=2G`/`MemoryHigh=1536M` target. **It has not been touched in weeks** — assume drift (OS packages, repo checkout, clock, thermal baseline) until verified.

## TASK (strict order)

1. **Step-0:** preflight vs pinned (one glance each); reconcile the straggler-commit sha + any new HEADs into mastheads; index.lock + Check 9 verifications above.
2. **High-value reads (the session's law):** `context/assessments/2026-06-07_M5-D_Pi4_AES-GCM_write-path_microbench_spec_OQ-15-2.md` **IN FULL** (run protocol + per-category decision rule + the empty §8 RESULTS/DECISION block + the guardrail: this TUNES the Doc 15 §9 encrypted-scope LIST — never a Doc 15 re-open; a design-change implication → STOP + escalate); `homesynapse-core/scripts/pi4-validation.sh` (never yet exercised on-device — read what it checks before running it); Doc 15 §9/§10 ONLY as the spec cites them.
3. **Pi readiness phase (guided, ~15 min):** SSH reachability → `uname -a` + OS update state (apt) → Corretto 21 presence/version → NVMe mount + free space + `noatime` → clock sync (`timedatectl`) → **thermal/throttle baseline (`vcgencmd get_throttled` + temp — benchmark validity depends on an unthrottled device)** → repo state on the Pi (clone/pull to current main per the spec's deploy path). Fix-as-you-go with Nick; record every drift found.
4. **`pi4-validation.sh` first exercise:** run, paste, adjudicate. Failures here are FINDINGS (environment drift), not necessarily blockers — the PM rules which gate the microbench.
5. **THE MICROBENCH (the session's payload):** build/deploy the harness per the spec; warmups + runs per protocol; Nick pastes raw results → PM fills the spec's **§8 RESULTS BLOCK verbatim** → apply the **per-category decision rule** → **OQ-15-2 RESOLVED: the MVP encrypted-scope list is FIXED.** ⚠ **Hardware caveat:** the spec targets the Pi-4 BUDGET and the device is a Pi 5 — follow the spec's own floor-handling language if present; if silent, record results as Pi-5 numbers with an explicit floor-extrapolation caveat and surface the residual to Nick as a ruling (Pi-5-bounds-accepted vs a later Pi-4 confirmation run). Do NOT silently equate the two.
6. **Consequence propagation:** OQ-15-2 disposition artifact (the filled §8 + a dated decision note); **Doc 15 §9 `encrypted_scopes` default tuned per the result** (the sanctioned currency edit, per the spec's guardrail); the **C9 §3.4 energy-scope reconciliation** resolved the same way (the staged list-tuning from the C9 record — energy in or out of the encrypted set per the measured budget); **M6.3 gate state → 1-of-3 CLOSED** in snapshot/charter/coder-handoff pointer; row-3 input half-delivered (interviews remain).
7. **Stretch (only if the window and the evening allow):** kick off the **60-minute sustained-load soak on `hs-dev-1`** (the never-run quiet-evening item; `@Tag("soak")` suite per Current_State §6) — start it, let it run unattended, collect in a follow-up session.
8. **Closeout:** WUCP drift check; **author the M5-C Increment 1 session prompt** (row 4 — charter from merged disposition §2e + the D-1..D-7 vetoes Nick rules at that session's start); handoffs; commit messages handed over (`git commit -F` if any message contains `!`).

## TOKEN DISCIPLINE

The microbench spec is the law — do NOT re-derive crypto budgets, scope candidates, or decision thresholds (the spec carries them, independently reviewed). Do not re-read the AMD block, the review return, or the merged disposition (ratified ground; the trackers carry the state). Doc 15: only the spec-cited sections. The window's precision item is the §8 fill + the decision rule application — spend it there, and on careful one-step-at-a-time device guidance.

## STANDING NICK-PACED ITEMS (surface, don't block on)

**Energy/erasure interviews** (`context/assessments/2026-06-07_M5-D_energy-erasure_interview_guide.md` — the OTHER half of row 3 AND the AMD-86 §3 signal; the microbench alone does not unlock the ordering call) · **M5-C Increment 1** (row 4 — the prompt this session authors; runnable as a PARALLEL Cowork conversation, content register) · D-1..D-7 strategy-draft vetoes (feed M5-C) · spike-dir `git rm` + DOCS-connector deselection (advisory queue, pm-handoff) · backlog DONE-row compression (next governance window) · FUTURE-AMD queue at a quiet window.
