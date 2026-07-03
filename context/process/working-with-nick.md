<!--
file: context/process/working-with-nick.md
purpose: The operator contract — who Nick is in this system, his environment, and the observed collaboration patterns a fresh Claude needs on day one. This file describes PREFERENCES and PRECEDENT, not law: Nick overrides any line here by saying so, and this file updates when he does.
audience: All agents (hub + lanes), every session start (the PM boot sequence names it).
state-type: reference
status: CURRENT
last-verified: 2026-07-03 (v15 hub, beat 60 — distilled from the v13–v15 arcs; authored for the wipe test)
-->

# Working with Nick — the operator contract

## 1. Role in the system

Nick is founder, strategic authority, and the ONLY human in the loop. He owns: strategy and scope, all rulings on Locked decisions and design points, ALL git commits and pushes (host-side), the build gate (`./gradlew check` and every CI glance — CI on the pushed commit is the gate of record), the physical bench (Pi 5 + coordinator + devices are his desk), the skill mirror sync, and spend (hardware, services). Agents NEVER commit, never push, never run his gates for him, never modify CI workflows without his explicit adoption, and never declare his gates (bench acceptance, go/no-go, hosting) closed.

## 2. Environment (facts agents get wrong without this file)

Windows machine (`DESKTOP-SRK0P9D`), shell = **MINGW64 git-bash** (paths like `/c/Users/Nick/...`; `!` history-expansion and inner-quote hazards in commit messages — hence the `git commit -F` convention, messages staged in `ClaudeFolder/_scratch/`). 24-thread box; JDK 21 + Gradle 8.8 (wrapper) + Node/npm on the host — **the host toolchain is authoritative; sandbox/VM builds are never the gate of record.** He works in the repos directly; agent worktrees mount the same folder (see the env-model for the path-duality and mount-lag rules). GitHub remotes are split across two accounts — see `infrastructure-map.md`.

## 3. The interaction contract (observed, stable across many sessions)

- **Concision.** His standing preference: as concise and direct as possible. Lead with the outcome; don't recap steps he watched happen. Depth on request — when he says "dive deep," he means source-verified evidence, not longer prose.
- **Exact counts, always.** Every commit handoff states "stages exactly N paths" so his porcelain glance can confirm. Give him the stop condition too ("if host status shows more than N, stop and ping the hub"). He checks. Twice today the count discipline caught real drift.
- **Evidence + recommendation + one decision.** He rules FAST when given: the options, the tradeoffs in one line each, a recommendation with its rationale, and a clear default. He ruled four strategic decision points (DP-B, DP-18-A/B/C) in a single turn when presented this way. Naked options without a recommendation waste his time; recommendations without evidence get challenged.
- **Veto-or-default.** For reversible calls, present the default and proceed unless he vetoes (the SSG=Astro pattern). For one-way doors (identity policy, licensing, paywall lines, security posture), a real ruling with his words on the record — he often supplies richer rationale than asked for; PRESERVE it verbatim in the spine (the DP-18-C reasoning is the model).
- **He pastes full transcripts.** Terminal output comes back complete — treat it as primary evidence and READ it carefully; his pastes have contained load-bearing details nobody flagged (the Dependabot escalation, the zero-JS gate no-op, the 9-path sweep).
- **He second-checks, and expects to be second-checked.** Lanes are instructed to verify the hub's briefs against source; he rewards refutations backed by evidence (the dist-gitignore refutation was celebrated, not resented). Never soften a finding because it contradicts him or a prior brief — but bring the evidence.
- **One-line confirms.** Standing items get re-surfaced each session until closed, compactly. He'll close them in batches when ready. Nagging is fine; re-explaining is not.
- **He delegates deliberately.** When he says "you decide" or "consider carefully what we do next," he means it — decide, state the reasoning briefly, and act. He reviews outcomes, not permission requests.

## 4. Cadence and rhythm

Gates run promptly — usually same-session, often within minutes; author handoffs assuming fast turnaround. Bench/physical tasks queue on his availability (label-first unboxing, pairing, flashing). Commits land in batches at natural boundaries (he'll run 2–3 staged commits in sequence). The mirror sync is a manual act he performs after skill-source edits — Check 9 STALE is normal until he does; remind, don't block on it. He works long arcs: plan for multi-milestone days.

## 5. Risk posture and non-negotiables

The **honesty brand outranks marketing** in every tradeoff (never-false-CONFIRMED, claim→truth tables, publish gates, "says less truthfully" — these are HIS calls repeatedly made the same direction). **Bench-first**: characterization before production pairing; the frozen instrument (MG24 @ 7.4.5.0/v13) stays untouched. **Security defaults conservative**: tokens/keys never in git, logs, messages, or exception text; root logging INFO; encrypt-from-genesis. **Community trust is strategy**: community content is never paywalled (ruled, with rationale, beat 57). When a security-posture election arises (e.g. hashed-TCLK), it is HIS election — present evidence, do not default it.

## 6. What frustrates the collaboration (avoid)

Unverified claims presented as facts (the audit culture exists because these compound); path counts that don't match porcelain; re-litigating recorded rulings; asking questions the spine already answers; verbose narration of routine steps; running ahead of a ruling on a one-way door; skills or briefs that contradict their own mandates (self-inflicted [REVIEW]s cost his attention). When something breaks, he wants the root cause, the class-sweep ("is this defect anywhere else?"), the fix, and the lesson folded — in that order, owned plainly if it was yours.
