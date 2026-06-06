<!--
file: project-knowledge/CLAUDE_PROJECT_KNOWLEDGE_SOURCES.md
purpose: Which knowledge sources each Claude Project (CORE, DOCS) should connect, and — for the nexsys-hivemind GitHub connector — exactly which folders to SELECT vs LEAVE UNSELECTED so the project-knowledge capacity budget isn't blown. Nothing in the repo is deleted; this is a per-Project sync-selection spec.
audience: Nick
update-cadence: ad-hoc (when the Projects' roles or the repo's top-level layout change)
state-type: reference
status: CURRENT
last-verified: 2026-06-05 — created to solve the DOCS Project hitting 117% capacity when the whole nexsys-hivemind repo was synced.
-->

# Claude Project Knowledge Sources — Sync Selection Spec

## The mechanism (no repo changes required)

The Claude Projects GitHub connector lets you **select specific files and folders** at connect time, and change them later via the **"Configure files"** icon — you do **not** have to sync a whole repo. (Support: *Use the GitHub integration* → Projects → "Use the file browser to select specific files and folders"; best practice #4: "avoid selecting unnecessary files to keep within token limits.") So the fix for the DOCS capacity overflow is to **deselect the folders DOCS doesn't use** — everything stays in `nexsys-hivemind`; the Project just doesn't index the parts irrelevant to its job.

## Why it overflows

`nexsys-hivemind` is ~3.7 MB. ~2.3 MB of that is **operational / skill-source / implementation** content that the **DOCS** Project (AMD-vs-design-doc fidelity review) never reads. The **design/governance/research** subset DOCS actually needs is only ~1.4 MB. Syncing the whole repo adds ~55 points of capacity (the observed 62% → 117%); syncing only the ~1.4 MB subset adds ~21 → lands DOCS near **~83%**, with headroom.

---

## DOCS Project — recommended selection

**Primary knowledge source:** `homesynapse-core-docs` (design docs, governance, `design/amendments/`) — this is what DOCS reviews against. Connect it fully (or near-fully); it's the review target.

**`nexsys-hivemind` — SELECT only these (≈1.4 MB):**

| Folder | Why DOCS needs it |
|---|---|
| `context/governance/` | project-instructions / review framing |
| `context/decisions/` | DEC / D-NN cross-module decisions referenced by AMDs |
| `context/assessments/` | research PM assessments — the "why" behind each AMD |
| `context/audits/` | review returns + retrospectives (incl. the AMD-54..64 review return + the M4 retrospective) |
| `context/planning/` | roadmap, milestone backlog, research-agenda (what's planned and why) |
| `context/protocols/` | WUCP and related governance protocols |
| `context/process/` | process docs |
| `context/strategy/` *(optional)* | mostly `.docx` (extraction is lossy) + 2 small `.md` — include only if a review needs positioning/data-contract framing |

**`nexsys-hivemind` — LEAVE UNSELECTED (≈2.3 MB — DOCS doesn't use these):**

`context/handoff/` (784 K — pm/coder/cross-agent handoffs, operational continuity), `context/lessons/` (204 K — coder implementation gotchas), `context/coding-instructions/` (368 K) and `context/instructions/` (336 K — Coder/research briefs), `context/status/` (84 K — operational snapshot), `context/relay/` (76 K), `context/pre-verifications/` (12 K), `benchmarks/` (148 K — skill evals), and the skill sources `coder/` (136 K) + `project-manager/` (144 K) (these mirror to `.claude/skills/` and are not knowledge content).

**Spine optimization:** the 5 curated files in `project-knowledge/` are best **uploaded individually** to DOCS (same as CORE — keeps them in precise direct-context, not RAG). If you do that, also **leave `project-knowledge/` unselected** in the connector to avoid double-counting that 220 K.

---

## CORE Project — for reference

CORE (architecture/AMD authoring + external review) legitimately uses more of the operational context. Connect `homesynapse-core-docs` + `homesynapse-core` (code) as before, plus — if you add `nexsys-hivemind` — you can include the same design/governance/research subset and additionally `context/lessons/` (coder-lessons inform CORE's reviews). Keep the 5 `project-knowledge/` spine files as individual uploads (the 12-file / direct-context discipline in `README.md`).

---

## Notes

- **Reversible:** selection is per-Project and changeable anytime via "Configure files" + "Sync now." If a specific review needs a normally-excluded file, add it for that review and remove it after.
- **RAG vs direct context:** a repo this size (dozens of files) will index in RAG/search mode regardless — fine for *supplementary* context. The precise fidelity diffs are against the `homesynapse-core-docs` design docs (the primary source) and the individually-uploaded spine, which stay reliable.
- **`.claudeignore`:** a gitignore-style ignore is documented for Claude Code, but the **Projects** GitHub connector's documented control is the "Configure files" selector — use that. (If you want a repo-side declarative exclude, test whether the connector honors `.claudeignore` before relying on it.)
- **Capacity figures are approximate** (token density varies by file type; `.docx` counts differently than `.md`). The relative magnitudes hold: `context/handoff/` alone is the single biggest excludable chunk (~12 points).
