<!--
file: context/audits/2026-09-23_v80-b1_laneB_horizon-recut-inputs_digest.md
purpose: Lane B's digest, VERBATIM — the INPUTS for THE HORIZON RE-CUT (D-v79-11; Saturday, desk-only): what the record already holds and lacks between the run (Oct 30 – Nov 2) and the launch (P6 the install flow end-to-end; P7 launch prep → Nov 25), with file:line cites, by a read-only in-conversation lane (D12). Its closing list "WHAT THE RE-CUT MUST DECIDE" is pre-registered as D-v80-8's eight questions; the hub's layer-2 re-executions are in the b1 audit §5. Nothing here is a ruling.
audience: the v80 hub (Saturday's re-cut beat) · Nick (the launch posture is his word) · the v81 hub
state-type: lane digest (evidence; read-only lane)
status: FILED v80 beat 1 (Wed 2026-09-23 ~23:2x CT; instrument 2026-09-24T04:29:21Z). Lane: in-conversation, read-only, ≈170K tokens, 38 tool calls. The `$` + double-brace expression quoted at item 5 is a verbatim workflow line, not spine text.
-->

# Lane B — THE HORIZON RE-CUT's inputs (verbatim return)

GROUNDING DIGEST — HORIZON RE-CUT inputs (read-only). Paths: nexsys-hivemind/context/ unless a repo is named. AUDIT=audits/2026-09-23_v79-b5_CLOSE_long-term-read_*.md; MRP=planning/master-release-plan.md; SoR=strategy/2026-08-27_company-and-brand-build_strategy-of-record.md; G2=strategy/2026-09-23_BRAND-G2-EXEC_re-cut_*.md; PLAN=planning/2026-09-15_v75_PROGRAM-PLAN_*.md; DR=planning/2026-09-23_v79_decision-record.md; PMH=handoff/pm-handoff.md.

1. AUDIT §2. :22 RA "the Key-Portability return unrecorded (a backup/restore input, a P6 concern) (RA:500–514)". :28 "the rename vs the 10-31 fallback → into THE HORIZON RE-CUT"; "founder hours ≈ 15/wk (SoR) vs ≈ 7/wk (the plan §0) → the plan governs". :30 "the plan of record ends at the run; P6 and P7 have no rows (OR-HORIZON-UNPLANNED; D-v79-11)". :34 "a Nov-25 launch needs the install flow built in the three weeks after the run unless it is planned now."
Verdict: finding EXISTS; P6/P7 rows MISSING.

2. MRP. :232 "Final .deb packages (aarch64 + x86_64). APT repository ... Download page on homesynapse.com. GPG signing." :233 "fresh Raspberry Pi OS -> visit homesynapse.com -> copy install command -> run -> wizard opens in browser -> Zigbee discovered -> devices paired -> dashboard live ... under 30 minutes." :234 "Getting Started guide with real screenshots ... Release notes page. Changelog. Update docs CI to auto-publish." :246–247 P7: community infra, "Soft launch to selected testers ... Go/no-go decision made." :325 "Cannot launch without verified install experience."
Verdict: STALE (:13 "intent, not schedule"); deliverables COMMITTED-BY-RECORD as intent.

3. SoR (newest; :6 RATIFIED v1.2). :27 P2 "the website wave W2 under the new identity ... the LICENSE flip decision window opens (its gate: the §VIII(4) consent)". :28 P3 "contributions OPEN at the LICENSE flip ... Exit: the Nov-25 runway is reached with a product, a name, a surface, and a fleet story that are all evidence-backed." :59 "THE LICENSE FLIP — confirmatory IP assignment → §VIII(4) Member consent → the flip, landing with the rename in-tree (one launch moment); fallback: the un-renamed tree if the rename slips past 10-31; the 10-01 quarterly is its gate check, not its date".
Verdict: COMMITTED-BY-RECORD (gates; no date past 10-31 but Nov-25).

4. G2. :20 B-1 → "a wordmark and the design tokens ... a frontend/brand lane after THE THURSDAY ORDER" (SoR :26 "~10–16 h"). :21 W2 → "the pilot's page first | the first written public surface". :22 launch moment → "the name in the code, the README and the repositories | the two company instruments signed (§4) | the rename WU ... never before the 72-hour run's evidence is safe". :34 fenced until their row: the written name, wordmark, rename, the LA trade-name filing ("rides W2"), the consent + IP assignment ("a business attorney before the LICENSE flip; the hub drafts that search at the P2 seam").
Verdict: EXISTS; undated; :22 (rename after Nov 2) collides with the 10-31 fallback.

5. homesynapse-core. Tracked: .github/workflows/{ci,install-smoke}.yml; distribution/ (deb/, image/, install/, smoke/, systemd/, update/, docs/). install-smoke.yml :19–25 push main/develop, PR→main (paths distribution/app/lifecycle/api), workflow_dispatch; :32 job "Build image + .deb, install-smoke on a clean ${{ matrix.arch }} machine"; :4–6 "install on a clean machine → boot → loopback health probe → assert RUNNING + token + auth enforced → stop → uninstall (data preserved) → update-smoke (zero event loss)". Signing/APT repo: NOT FOUND (two forms: `gpg|reprepro|aptly|apt-repo|dpkg-sig|debsign|InRelease`; `sign` → KillSignal only). systemd unit EXISTS. control.in :4 "homesynapse@nexsys.example", :9 "https://nexsys.example/homesynapse". pairing-wizard-seam.md :1–3 "DESIGN ONLY ... Nothing in this file is implemented".
Verdict: .deb + smoke EXISTS (CI-only); signing, APT repo, download page, install command, wizard MISSING.

6. homesynapse-core-docs. Only hit: operations/pi5-developer-setup-guide.md (:3–5 Active, last validated 2026-04-02) — developer setup, not Getting Started. Getting Started / install guide / release notes / changelog / deployment: NOT FOUND (two forms: `install|getting-started|release|deploy|operat`; `guide|quick|start|notes|changelog`). website/README.md :5 "INCREMENT 1 — skeleton + one page draft (2026-06-12) ... (no site repo exists)", :10 "static-site-generator decision is deliberately NOT made"; website/index.md :1 "DRAFT", :3 "# {{productName}}".
Verdict: MISSING; website = 06-2026 draft, no build.

7. Fresh-install stop-proof. The rep: audits/2026-08-09_H3-clean-image_fresh-install_operator-return.md :11. Stop-proof = the clean systemd stop grade: audits/2026-09-06_H8a_real-wire_operator-record.md :13 "THE STOP-PROOF CLEAN, TWICE", :29–30 on `6bd8508` (F-1 open). Stands: PLAN :157 "THE HELD CARD hs-fresh runs the `6bd8508` .deb"; :172 "toward P6 there is the CI-built arm64 .deb (install-smoke) and the held card's fresh-install stop-proof, nothing else"; PMH :87.
Verdict: EXISTS (09-06, 6bd8508); not MRP :233's fresh-Pi-OS-via-install-command flow.

8. Stale baselines — :8 on all three "status: STALE BASELINE — bannered v79 b5 (2026-09-23); the plan of record outranks this file". master-release-plan.md 36,944 B (:9 last-verified 2026-05-22); phase-3-milestone-backlog.md 89,025 B (:9 2026-08-01); research-agenda.md 58,270 B (:9 2026-05-22). DR :67 "the three stale baselines re-issued or retired".
Verdict: STALE; disposition COMMITTED-BY-RECORD to the re-cut.

9. strategy/ hits (9 files): SoR :59 · 2026-09-04_R10-sitting_THE-WORDS_ruling-record.md :45 "R-2 (b) ... one launch moment; 10-01 quarterly = gate check; fallback: rename slips past 10-31 → flip on the un-renamed tree" · 2026-09-05_post-MVP-horizon_strategy-card-INPUT.md :61 "S-1: no wedge date spoken before the flip date is scheduled" · G2 :19 "the buyer conversations may carry the name", :21, :31 "the first software delivered to a pilot household under the name, the first sale". "launch posture": not in strategy/ — only PLAN :172, DR :67, PMH :88 ("one word: the launch posture"). "pilot's freeze": NOT FOUND (two forms: `pilot.s freeze`, `pilot-freeze`). "first customers": NOT FOUND.
Verdict: launch moment COMMITTED-BY-RECORD; "launch posture" undefined.

10. The 10-01 quarterly: planning/2026-09_september_plan-of-record.md :70 "10-01 the quarterly checkpoint (registered office/agent · the LICENSE-flip gate · the NFCU share-minimum — the new rider)"; SoR :59 "its gate check, not its date"; PLAN :172 "The 10-01 quarterly gate check reads it [the re-cut]".
Verdict: EXISTS (a checkpoint row, no file); COMMITTED-BY-RECORD to read the re-cut.

WHAT THE RE-CUT MUST DECIDE
1. P6 rows off Nov 2 with instruments: signed .deb, APT repo, download page, install command are NOT FOUND in core (item 5) while MRP :232–233,:325 make the install flow the launch gate.
2. The in-browser wizard step (MRP :233) is DESIGN ONLY (pairing-wizard-seam.md :1–3): in P6 scope, or the flow re-cut without it.
3. Getting Started, release notes, changelog (MRP :234) have no file (item 6); the website is a 06-2026 draft with no SSG decision (website/README.md :5,:10) — who builds W2, when, against B-1 (G2 :20–21).
4. Rename vs 10-31: G2 :22 holds the rename until the run's evidence is safe (run ends Nov 2); SoR :59 falls back to the un-renamed tree past 10-31; control.in :4,:9 carries placeholder domains — rule the fallback or move the date (AUDIT :28).
5. The business-attorney search for the §VIII(4) consent + confirmatory IP assignment (G2 :34, "at the P2 seam") has no row; the flip waits on it (SoR :59).
6. Which P7 rows (MRP :246–247) survive at ≈7 h/wk (AUDIT :28) against the P3 exit (SoR :28).
7. The three stale baselines: re-issue or retire each (DR :67; item 8), incl. the RA's Key-Portability/backup-restore P6 concern (AUDIT :22).
8. "Launch posture" (PLAN :172; PMH :88) is defined nowhere in strategy/ (item 9) — the re-cut must name the options Nick chooses between.
