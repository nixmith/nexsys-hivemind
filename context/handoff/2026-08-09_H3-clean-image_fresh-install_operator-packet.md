<!--
file: context/handoff/2026-08-09_H3-clean-image_fresh-install_operator-packet.md
purpose: The H3 clean-image fresh-install rep — operator-support packet for a DEDICATED fresh Cowork session that works interactively WITH Nick tonight (2026-08-09, the named slot held on his word, v50 beat 4). Goal: close the go/no-go ledger's H3 MUST row — "one documented fresh install onto a clean Pi image (install.sh or deb) reaching a healthy boot (health-probe green) with the runbook's steps as written" — with the evidence captured to the gate-day bar, plus a findings-only insight rider for S-10.
audience: the H3 operator-support lane (a fresh Cowork session; no role skill required — this packet is self-contained). Nick runs hands; the session authors every command and makes mistakes impossible.
status: DISPATCH-READY. Dispatch line: "Read nexsys-hivemind/context/handoff/2026-08-09_H3-clean-image_fresh-install_operator-packet.md and execute it."
return: nexsys-hivemind/context/audits/2026-08-09_H3-clean-image_fresh-install_operator-return.md — a lane is verified at its RETURN ON DISK. If this session cannot write that file, the complete RECORD pastes to Nick who relays it; the hub files it verbatim-as-received (the H3-precedent form).
-->

# H3 — Clean-Image Fresh-Install Rep (operator-support packet; tonight)

## Section 0 — Mission, mode, and the hard fences (read whole before any act)

**The criterion, frozen (ledger H3 [MUST]):** install-smoke is green standing in CI (the harness half — build image → .deb → install on a clean machine → boot → loopback health probe → RUNNING + token + auth enforced). The remaining evidence act is the SAME flow on REAL hardware: a fresh-flashed clean Pi image, the documented install path run AS WRITTEN, reaching a healthy boot with the health probe green. **Done-when:** the probe reads green on the fresh install, the full command log + probe output + timings are captured, the bench is verified restored, and the return is filed.

**The mode (Nick's directive, verbatim in intent):** this session exists to get the best possible evidence AND to guide Nick so he makes no mistakes. Every operator act ships as a §8-compliant paste block: self-contained · full paths · ONE act per block where a failure needs its own adjudication · the expected output token NAMED for every command · anti-actions explicit · every placeholder carries its own FILL-IN-BEFORE-RUNNING warning line · STOP-gates in their OWN blocks · ⏺ RECORD paste-either-way. Before issuing ANY command, verify the verb/flag/path exists at source (read the actual scripts) — never ship a guessed command. Walk one phase at a time; wait for Nick's paste before the next.

**THE HARD FENCES (absolute; a violated fence = abort + restore + report):**
1. **The live bench is untouchable.** The bench Pi (hs-dev-1) currently runs the production bench + the 04:30 nightly. Its SD card is removed intact, labeled, and set aside — NOTHING writes to it. Every bench device stays untouched; HANDS OFF the S31 (a standing evidence read is open on it).
2. **The SD-5 rail: the Zigbee coordinator stays PHYSICALLY DISCONNECTED for the entire rep.** No network forms, no join, no radio traffic. The rep proves BOOT + HEALTH + AUTH, exactly the install-smoke assert set — the radio is out of scope by design (the no-non-bench-network hard gate is ratified law; a fresh app must never get the chance to form a network).
3. **The nightly fence:** the bench must be FULLY RESTORED — original card back, booted, the app alive at pgrep, one API read green — with wide margin before the 04:30 America/Chicago fire; target the whole rep complete by midnight. An abort at ANY step = restore the bench FIRST, then report; the rep re-slots without argument (any slot before Fri Aug-14 EOD keeps the row clean).
4. **Read-only on every repo.** This session's only write is the return file. NO code fixes, NO installer edits, NO doc edits mid-rep — a runbook/script step that fails as written is a FINDING (arguably the most valuable outcome), never a live patch. Gate sovereignty: freeze 2026-08-14 EOD; nothing this session produces moves code.
5. **Evidence discipline:** capture verbatim — every command as run, every output, timings at the named marks (flash start/end · first boot · install start/end · probe green · restore verified). Record AS-DOCUMENTED vs AS-RUN for every step: the criterion measures the documentation's reproducibility as much as the artifact's (this is the W-2 claim surface — install claims proven at an instrument, at a pre-stated bar).

**Baseline:** core `d26777c` (main; the gate of record CI #208 + install-smoke #28 green on `ca0f41d`). The installed artifact must be traceable to a commit — record WHICH commit the built/transferred artifact derives from in the return.

## Section 1 — The rep, phased (each phase = read the sources, author the blocks, wait for the paste)

**Phase 0 — inventory + fences (interactive; STOP-gated).** Ask Nick: (a) is there a spare Pi, or does the rep swap cards on hs-dev-1? (b) is there a spare SD card (≥16 GB) + a card reader/writer? (c) is the imaging tool available (Raspberry Pi Imager or equivalent)? Branch on the answers. **If no spare card AND no spare Pi exists tonight: STOP — report to the hub for a re-slot; never improvise onto the bench card.** Confirm the fences aloud in the chat: bench card out + labeled · coordinator unplugged · clock margin to 03:30 CT stated.

**Phase 1 — flash the clean image.** Derive the target OS image (distro + version + 64/32-bit) from `homesynapse-core/distribution/README.md` + `distribution/docs/` + `distribution/image/` at source — the docs' stated target IS the spec; if the docs do not state one, that is FINDING #1 (record it, then use the docs' closest implication and record the choice). Author the flash steps; verify boot to a shell.

**Phase 2 — obtain the artifact.** Prefer the .deb one-command path (the distribution README's headline: `sudo apt install ./homesynapse_<version>_<arch>.deb`); derive the BUILD/assemble commands from `distribution/` at source (deb/ · image/ · common.sh) — building on the desktop or Pi per the docs is lawful (not a repo write). The no-dpkg `install.sh` path is the documented fallback. Record which path ran and why.

**Phase 3 — the documented install, AS WRITTEN.** Run the one-command install exactly per the docs. Expected per the distribution README: runtime image laid down · homesynapse user + state dirs created · systemd service installed/enabled/started · health wait · first-run pairing-token path printed. Capture everything; every deviation = a numbered finding.

**Phase 4 — the probe set (the install-smoke assert set, on-Pi).** Health probe green (loopback) · service RUNNING at systemd · the token present at its printed path · auth enforced (an unauthenticated probe rejected, an authenticated one accepted) — derive the exact probe commands from the install-smoke workflow + distribution/smoke/ at source. ⏺ RECORD: the probe outputs verbatim. **This green = the H3 evidence moment; timestamp it.**

**Phase 5 — clean stop (optional legs only if the clock is comfortable).** Stop the service cleanly; the uninstall-data-preserved and update-smoke legs are CI-proven and OPTIONAL on-Pi — do not spend the nightly margin on them; skipping is recorded, not silent.

**Phase 6 — RESTORE THE BENCH (mandatory; the rep is not done without it).** Original card back in hs-dev-1 → boot → the app alive at pgrep → one authed entities read green → state the margin to 04:30. ⏺ RECORD.

**Phase 7 — file the return.** One file at the named path: the phase log (commands + outputs verbatim) · the timings table · the AS-DOCUMENTED vs AS-RUN deviation table · the findings (Section 2) · a self-audit (what was skipped, the weakest evidence, what a hostile reviewer attacks).

## Section 2 — The insight rider (findings-only; this is where "deep insight" lives)

After Phase 6, write into the return: (1) **the friction log** — every manual step, ambiguity, undocumented prerequisite, or deviation, each anchored to the doc/script file+line that should have covered it; (2) **the reproducibility verdict in one paragraph** — could a competent stranger with only the docs reach probe-green, and where exactly would they fail; (3) **a PROPOSED-only improvements list** (3–7 items, each priced S/M under the 15 h/wk A-14 floor) for the S-10 charter's W-2 scope (reproducible-install as a claim surface: toolchain pinning · declarative unit/drop-in state · install-rehearsal as an evidence class). NO fixes now; the charter adopts or declines. Where an observation suggests a coding direction, state it as a NAMED CANDIDATE for the post-gate queue — never as a work order.

## Section 3 — Named sources (read in this order before Phase 0)

1. `homesynapse-core/distribution/README.md` — the install path's own contract (the one-command meaning).
2. `homesynapse-core/distribution/docs/` (all files) + `distribution/install/install.sh` + `distribution/deb/` + `distribution/image/` + `distribution/smoke/` + `distribution/systemd/` — the mechanics at source; every command you author traces here.
3. `homesynapse-core/.github/workflows/install-smoke.yml` — the assert set of record (what "proven" means).
4. `nexsys-hivemind/context/assessments/2026-07-11_go-no-go-criteria_draft.md` — the H3 row + ratification block (the frozen bar this rep serves).
5. `nexsys-bench/docs/2026-06-28_phase-0_pi-bench-bringup_runbook.md` — Pi-side conventions ONLY (ssh/user/paths); the bench bring-up is NOT this rep — re-run none of it.
6. Environment data: on the BENCH image, `journalctl --user` is dead (use `systemctl --user status`) — on the FRESH image this may differ; verify at the instrument before relying on either. The fresh install runs as a SYSTEM service per the distribution docs — derive the journal route accordingly.
7. `nexsys-hivemind/context/research/2026-08-02_A14_attended-hours_charter-input.md` — the sizing floor for Section 2's pricing.

**Known hazards:** the S31 evidence read is OPEN (touch nothing bench-side beyond the Phase-6 restore reads) · the Hue is dead-and-kept by ruling (ignore it) · the distribution workspace was built as a skeleton lane — expect version/path drift between its docs and the current artifact; drift IS the finding class this rep exists to surface, not a blocker to route around silently.
