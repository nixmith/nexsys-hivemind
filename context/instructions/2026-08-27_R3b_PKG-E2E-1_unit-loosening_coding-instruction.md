<!--
file: context/instructions/2026-08-27_R3b_PKG-E2E-1_unit-loosening_coding-instruction.md
purpose: R-3b — the PKG-E2E-1 repo delta: the MEASURED serial-coordinator loosening lands in `distribution/systemd/homesynapse.service` byte-identical to the drop-in text the R-3a rehearsal proved on the held card (H13: one instrument), + one documentation row. Authored AHEAD at v57 beat 3 (Thu 2026-08-27) per the SKELETON's §5 (`context/instructions/2026-08-21_R3_PKG-E2E-1_packaged-integration-run_coding-instruction_SKELETON.md`, RULED CLONE); the ⟨MEASURED-TEXT⟩ slot fills from the R-3a record before dispatch.
audience: a host-side Claude Code Coder lane (D12 — the R-3b lane; ~30 min) + Nick (commit + push + the CI read) + the hub (audit).
status: **ISSUE-READY-PENDING-MEASUREMENT** — dispatch ONLY after the hub stamps §2 with the measured text from `context/audits/2026-08-29_R3a_rehearsal_operator-record.md` (§9's FINAL drop-in — the text that produced `zigbee.network_resumed`, including any P-b/P-c-forced additions). Baseline: core `5051fa5` (the unit file is byte-identical there to `dec35be`'s — the FE gate touched only `web-ui/`); verify at checkout.
return: nexsys-hivemind/context/audits/<filing-date>_R3b_unit-loosening_return.md (filing-day dated, America/Chicago).
fences: ZERO Java (a .java edit seeming necessary = STOP + flag) · `distribution/README.md` UNTOUCHED (the :117 fence holds until W2-3) · the CI workflow twins UNTOUCHED · the DANGER block (Type=notify, `homesynapse.service:103+`) UNTOUCHED · no attribution trailers (nothing is committed by the lane anyway — Nick commits).
-->

# R-3b — the unit loosening (2 M; the measured text ships verbatim)

## §1 Files to read first

`distribution/systemd/homesynapse.service` WHOLE (the edit target; at `5051fa5` the seam is: the RAMP comment `:91–:95` — whose sketch names a NODE-path `DeviceAllow=/dev/ttyUSB0 rw`, superseded by the measured CLASS form — directly above **`PrivateDevices=yes` at `:96`**; the hardening context: `ProtectSystem=strict :73` · `PrivateTmp=yes :75` · `RestrictAddressFamilies :88` · `SystemCallFilter=@system-service :89` / `SystemCallErrorNumber=EPERM :90`; the DANGER block `:103+` stays) · `context/pre-verifications/WU-R3.md` (P1 pins the line numbers; P10/P11 the artifact grammar + preservation assertion) · `context/audits/2026-08-29_R3a_rehearsal_operator-record.md` §7/§9 (the measured text + which prediction arm fired) · `distribution/deb/build-deb.sh` (the unit is copied VERBATIM into the package — no second copy to edit) · `distribution/docs/boot-contract-map.md` (the row lands here) · `distribution/smoke/run-smoke.sh` (context only: no check reads the hardening block — the gate certifies boot/serve under the loosened unit).

## §2 The delta — stages exactly 2 M

**(1) `distribution/systemd/homesynapse.service`:** replace the RAMP comment block `:91–:95` AND the `PrivateDevices=yes` line `:96` with: (a) a provenance comment — *"Serial coordinator access — MEASURED on the held card (R-3a rehearsal, 2026-08-29, drop-in 10-serial-coordinator.conf; nexsys-hivemind context/audits/2026-08-29_R3a_rehearsal_operator-record.md): the packaged service resumed the six-device network under exactly these lines (`zigbee.network_resumed: channel=20 panId=0x774c`). Class rules (`char-ttyUSB`/`char-ttyACM`, majors 188/166) survive replug renumbering where a node path would not; `DevicePolicy=closed` keeps only the standard pseudo-devices; `SupplementaryGroups=dialout` matches the node's root:dialout 0660."* — then (b) the measured `[Service]` lines **VERBATIM (H13)**:

```
⟨MEASURED-TEXT — filled by the hub from the R-3a record §9; the candidate was:
PrivateDevices=no
DevicePolicy=closed
DeviceAllow=char-ttyUSB rw
DeviceAllow=char-ttyACM rw
SupplementaryGroups=dialout
— if P-b/P-c forced additional lines on the card, the FINAL working text is what ships, byte-identical.⟩
```

Rules: the lines land at the seam (where `PrivateDevices=yes` stood), in the drop-in's exact order; every OTHER hardening line keeps its position and value; the DANGER block and the `ExecStartPost` probe line are untouched.

**(2) `distribution/docs/boot-contract-map.md`:** ONE row in the packaged-path model — the serial-device posture: class-based `DeviceAllow` (`char-ttyUSB`/`char-ttyACM`) + `SupplementaryGroups=dialout` + `PrivateDevices=no`/`DevicePolicy=closed`, measured R-3a 2026-08-29; what STAYS hardened (`ProtectSystem=strict`, `PrivateTmp`, the syscall filter, `RestrictAddressFamilies`); pointer to the unit's provenance comment. Match the file's existing row idiom.

(The `integration/integration-zigbee/MODULE_CONTEXT.md` gotcha row — packaged-path custody location + the resume-or-form consequence for migrations — is the HUB's own fold at intake, NOT in your census: the F-14-row precedent.)

## §3 What to watch out for

`PrivateDevices=yes` would MASK `DeviceAllow` (it installs its own device policy) — the measured text replaces it, never coexists with it · systemd class syntax is exactly `DeviceAllow=char-ttyUSB rw` (no `/dev/`) · keep LF-only endings + the file's comment style (`# ─` rules) · do NOT reorder unrelated lines: the review diffs this file expecting EXACTLY the seam hunk · zero Java, zero README, zero workflow bytes · the arch-rule test-clock reminder is N/A (no Java, no tests in census) · red-first accounting (#18): no fixture can red at HEAD for a unit-file change — the rehearsal's own RED arms (E3-RED; P-b/P-c if they fired) are the red leg, DISCLOSED in the return, never simulated.

## §4 Gates (in-lane, then the gate of record)

In-lane: `systemd-analyze verify distribution/systemd/homesynapse.service` if the host has systemd-analyze (WSL/Git Bash likely NOT — flag its absence, do not fake it); a byte-diff of the shipped lines against the record's measured text (paste the `diff` output in the return — H13's proof); porcelain spelled `git --no-optional-locks status --porcelain` = exactly the 2 M. **Gate of record: CI on Nick's push** — `distribution/**` triggers install-smoke: predictions (H12, filed here): `CI / Build & Check` GREEN · install-smoke BOTH legs GREEN (the loosened unit still boots/serves on a runner with no serial device — the new lines are inert there; run-smoke 18/18; update-smoke zero-loss; the rig's 34 checks) · the echo step prints `hs_version=0.1.0+git<push-commit-UTC-date>.g<sha>` · **the arm64 leg's `version-grammar echo green: … sha256 …` line is R-4's origin hash** (the hub pins it into the R-4 packet). Zero Node-20 annotations.

## §5 Return shape (≤ 2 pages)

§0 census (2 M exact, porcelain paste) · §1 the seam diff verbatim + the H13 byte-diff vs the measured text · §2 the docs row verbatim · §3 gates run/flagged · §4 pushback (a line the measurement demands that seems wrong at the source = say so, do not silently ship it) · ≤ 3 harvest lines.
