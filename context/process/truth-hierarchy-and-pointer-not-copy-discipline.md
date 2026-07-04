<!--
file: context/process/truth-hierarchy-and-pointer-not-copy-discipline.md
purpose: The standing discipline that prevents context-rot across the three repos — the truth hierarchy + pointer-not-copy + verify-against-source. The "do-now" half of the skills-initiative (SD-1/SD-2/SD-10) that the v7 hub carries while the full skills build is deferred. Read by every hub/skill that caches or cites project facts.
audience: PM hub, Coder, every skill, anyone authoring a summary/quick-reference
state-type: process / discipline
status: CURRENT — adopted 2026-06-27 (v7 hub) per the skills-architecture PM-assessment §4 (the cheap rot-fix to adopt now; full skills build deferred post-V1).
inputs: nexsys-skills/design/2026-06-26_skills-architecture_PM-assessment.md · nexsys-skills/design/2026-06-26_skills-internal-inventory_v0.md (F1/F2/F3) · nexsys-skills/design/2026-06-26_Skills-Architecture_design_v1.md (SD-1/SD-2/SD-10). (Paths retargeted 2026-07-04: the corpus MIGRATED from the unversioned skills-initiative/ into the VERSIONED nexsys-skills repo — 14 tracked files under design/.)
-->

# Truth-Hierarchy + Pointer-Not-Copy Discipline

The single fix for the context-rot this project has repeatedly paid for (the 2026-04-11 arch-debt retrospective; the `project-knowledge` staleness — inventory F2). **Adopt the discipline now; the full skills system is deferred (post-V1).**

## 1. The truth hierarchy (which layer is authoritative)

| Rank | Layer | Repo | Authority for | Drift property |
|---|---|---|---|---|
| 1 | **Code (the territory)** | `homesynapse-core` | what exists / compiles / the tests prove | cannot self-drift |
| 2 | **Locked design docs + registers (the contracts)** | `homesynapse-core-docs` | contracts, intent, invariants, watermark | changes only by ratified amendment |
| 3 | **Operational memory (working notes)** | `nexsys-hivemind` | current state, plans, handoffs, summaries | drifts continuously |

**The empirical proof this is the right anchor:** the only layer that has rotted is the *derived-copy* layer (`project-knowledge`), not the code and not the Locked docs (F2).

## 2. The rules

1. **Pointer, not copy.** A skill, MODULE_CONTEXT, or summary **points at** the authoritative source for any volatile fact (counts, watermark, signatures, HEADs) — it does not copy the value in. Copies drift; the source does not. Carry a durable *mental model* (which is stable), route to truth code-first.
2. **Verify-against-source before trust (SD-1/SD-2).** Any cached number or signature is suspect until re-derived from the authoritative layer. Never propagate a stated total — re-derive it (the invariant register's own rule: "re-derive from the §17 table"; the consumer/pin survey's "re-derive counts from source"). This is already the freshness-preflight Check 11 + the WUCP source round-trip; this note generalizes it to every cached artifact.
3. **Regenerate-from-source or retire — never hand-maintain a copy.** A derived quick-reference (the `project-knowledge` class) is either regenerated from its source on demand or retired. A hand-maintained copy is a rot generator (F2/F3). `HomeSynapse_Current_State.md` is redundant with `PROJECT_SNAPSHOT.md` — the live spine is the one source.
4. **A claimed gate must be verified actually-green before it is trusted.** (The 2026-06-27 lesson: "CI-as-gate-of-record" was logged as adopted 2026-06-21 but had never run green — `gradlew` was non-executable since the init commit, so `ci.yml`'s `./gradlew check` had always exited 126. Adopting a gate ≠ the gate passing. Verify the green run before recording the gate as live — the M2.5 retrospective class, one level up.)

## 3. Scope / what this supersedes-in-practice

- Applies to: every skill (`nexsys-coder`/`-project-manager`/future), every MODULE_CONTEXT, `project-knowledge/*`, and any assessment/quick-reference that caches a project fact.
- The full skills architecture (the 4-tier model, the maintenance harness, the eval suite, the ~38-skill catalog, the stewardship tier) is **captured in `nexsys-skills/design/` (VERSIONED — 14 tracked files; migrated from the unversioned `skills-initiative/`, whose empty husk directory is deletable) and deferred** — this note is the cheap discipline that holds the line until then. The deferral was re-affirmed with evidence at the 2026-07-04 v17 skills pass: the discipline ran five beats, two CC lanes, and four Cowork lanes with zero skill-staleness incidents.
- The deferred-but-ratifiable design is `nexsys-skills/design/2026-06-26_Skills-Architecture_design_v1.md` (route through independent review → Nick co-sign → Lock when Nick chooses — ratifying the *design*, not a commitment to build now).
