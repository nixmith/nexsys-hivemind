# Context Engineering & Skills Expansion — Deep-Research Return

**Date:** 2026-08-02 · **Status:** COMPLETE — proposes, does not ratify · **Requested by:** Nick
**Scope:** (1) refresh the June-2026 skills research with everything that has changed or firmed up since; (2) audit the three live orchestrator skills against current evidence; (3) rule on per-module skills; (4) advise the W-SKILLS v44 pass; (5) advise W-EXEC design and the exec-persona question.
**Method:** four parallel fresh-context research lanes — (a) recon of `nexsys-skills/` design corpus + the three live SKILL.md trees, (b) Anthropic official skills guidance, (c) context-engineering state of the art, (d) granularity/longevity + persona-prompting evidence. ~60 sources; every load-bearing claim carries its URL. Evidence labels: **[STRONG]** controlled study or vendor eval numbers · **[VENDOR]** official Anthropic guidance · **[PRACTITIONER]** credible production report · **[ANECDOTE]** community observation.
**Known gap:** `nexsys-hivemind/` (weeks plans, law harvest, v42–v43 arc) was not staged. Terms `W-SKILLS`, `law harvest`, `v42/v43`, `ghost-commit`, `operator-packet` appear nowhere in the staged corpus or the live skills — this return treats your description of them as authoritative and flags where a hivemind read is needed before executing.

---

## §0 Executive summary (the six rulings this return supports)

1. **The June research doc holds up.** Its 8 principles are re-confirmed by everything newer. What's new since June is mostly *mechanism knowledge* (how Claude Code actually budgets, truncates, and re-attaches skills) and *harder numbers* on context rot and self-editing failure modes. Fold the deltas (§1–§2); do not re-litigate the architecture.
2. **The most valuable "skills expansion" available to you is subtraction, not addition.** All three live skills exceed the 5,000-token body budget; PM and coder carry 33–36% always-loaded masthead; the frontend skill's §4a–§4e is a direct SK-INV-01 breach. The audit (§3) is itemized so the v44 pass can execute it.
3. **Per-module skills: yes in principle, no as a batch.** The design already contains the right selector — deliberation trigger T3 (same mental model re-derived ≥3×). Build module skills one at a time on demand-evidence, never as a 13-skill drop (§4).
4. **W-SKILLS v44: run it as a delta-edit pass with a rule census, never a rewrite.** The strongest new academic result of the year (ACE, ICLR 2026) is precisely about why LLM rewrite passes silently destroy accumulated laws. Your practiced rule-census mechanic is independently validated — keep it, and add the structural moves in §5.
5. **W-EXEC: your PM's ruling is correct, and the evidence base now says *why*.** Author after the charter. An executive skill built from ratified doctrine is an "encoded preference" skill grounded in real artifacts — the category Anthropic's own guidance says works. Authored pre-charter it would be a generic-LLM-knowledge skill — the category the guidance explicitly warns against. Design question-set: Appendix A (§6).
6. **Personas: encode the mechanisms, not the men.** The accuracy literature is now unusually clean: named/expert personas do not improve factual accuracy or reasoning, and sometimes damage it; what works is encoding the actual decision procedures (Bezos's door test, Grove's inflection-point audit, Jobs's kill-list). Build W-EXEC as a *council of named lenses* where each lens is a framework with an evidence trail, not an impersonation (§7).

---

## §1 What changed since the June research (the delta harvest)

The June doc ("Maintaining a Large, Long-Lived Library…") remains the base layer. These are the additions and corrections a v44 pass should fold.

### 1.1 The skills listing is budgeted and silently evicts — new, load-bearing **[VENDOR]**

The June doc knew descriptions cost ~80 tokens each. What's now documented is the *enforcement mechanism* in Claude Code:

- The whole skills listing gets **1% of the model's context window** (`skillListingBudgetFraction`, overridable via `SLASH_COMMAND_TOOL_CHAR_BUDGET`). https://code.claude.com/docs/en/skills
- Each skill's `description` + `when_to_use` is **truncated at 1,536 characters** — "put the key use case first." Same source.
- On overflow, Claude Code **drops descriptions starting with the least-invoked skills** (names kept). Community reverse-engineering documents the eviction score as usage-count with a 7-day half-life — "a brand-new skill with zero invocations ranks first for removal" **[ANECDOTE]**. https://happyskills.ai/blog/why-your-skill-never-fires/ · https://blog.fsck.com/2025/12/17/claude-code-skills-not-triggering/
- `/doctor` estimates listing cost; `/context` shows the post-budget Skills row.

**Implication for NexSys:** the frontend description (974 chars) is fine against 1,024 but any future `when_to_use` additions eat the same 1,536-char cap. More importantly: *catalog growth now has a hard failure mode* — a 38-skill catalog with fat descriptions will silently evict its newest members. This retro-justifies SD-4 (co-trigger ≤3 governs, not catalog size) and adds a new corollary: **description budget is a shared pool; every skill added taxes the triggering reliability of every other skill.**

### 1.2 Skill-body lifecycle inside a session — new **[VENDOR]**

- Invoked skill content **persists for the rest of the session** as one message → write standing instructions, not one-time steps.
- On auto-compaction, each skill's most recent invocation is re-attached keeping the **first 5,000 tokens each**, within a **combined 25,000-token budget**, most-recent-first. https://code.claude.com/docs/en/skills

**Implication:** anything past the first ~5,000 tokens of a SKILL.md can vanish mid-session on compaction. For PM (~8–12k tokens) that means the *back half of the skill — including §4c and §6 "What You Never Do" — is the part that gets dropped.* Front-load the laws; push the rest to references. This converts the 5,000-token budget from a style preference into a survival boundary.

### 1.3 New frontmatter machinery worth adopting selectively **[VENDOR]**

Claude Code now documents (all optional): `when_to_use` (extra trigger phrases), `disable-model-invocation` (user-only; removes description from context entirely), `user-invocable: false`, `allowed-tools` / `disallowed-tools`, `model`, `effort`, `context: fork` (run as subagent) + `agent`, `paths` (glob-scoped auto-activation), skill-scoped `hooks`, and `!`-prefixed dynamic context injection. https://code.claude.com/docs/en/skills

Candidates for NexSys:
- **`paths` scoping** for a future frontend split (`web-ui/dashboard/**`) and for module skills (`event-model/**`) — makes module-skill routing structural instead of purely description-matched.
- **`context: fork`** for disciplines like `deep-research-session` — a skill that *is* a fresh-context lane can now declare that.
- **`disable-model-invocation: true`** for stewardship skills — SK-INV-08 (human-gated) can be partially *enforced by frontmatter* rather than by prose.
- Caveat: these are Claude Code extensions; the open spec (agentskills.io) marks even `allowed-tools` experimental. Cowork/cloud sessions sync account skills and may not honor every field — verify per-surface before relying on one.

### 1.4 Official authoring guidance consolidated (agentskills.io, Dec 2025 → now)

Agent Skills became an **open standard** (agentskills.io, adopted by Gemini CLI, Copilot, Cursor, Codex et al.), with an Anthropic-maintained authoring canon. Key rules, several new since June:

- Description: 1–1,024 chars, third-person capability statement + pushy "Use when…" trigger clause; **"err on the side of being pushy"**; fix overtriggering by stating what the skill does *not* do. https://agentskills.io/skill-creation/optimizing-descriptions
- Body: **<500 lines / <5,000 tokens**; references **one level deep**; reference files >100 lines need a table of contents; conditional-load phrasing ("Read `references/api-errors.md` if the API returns non-200") beats generic pointers. https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- **Degrees-of-freedom framework** (new framing): high freedom = prose heuristics; medium = pseudocode with parameters; low = exact scripts for fragile ops. Match specificity to fragility.
- Named anti-patterns: too many options ("pick a default with one escape hatch"), over-explaining ("assume Claude is smart"), time-sensitive info in bodies, voodoo constants, deep nesting, inconsistent terminology.
- **"Explain the why"**: "Reasoning-based instructions ('Do X because Y tends to cause Z') work better than rigid directives." And the pruning test: *"Would the agent get this wrong without this instruction?" If no, cut it.*
- Trigger evals: ~20 labeled queries (half should-trigger, half tricky near-miss negatives), 3 runs each, 60/40 train/validation, select by validation score, "five iterations is usually enough." https://agentskills.io/skill-creation/evaluating-skills
- **skill-creator got a major update 2026-03-03**: evals, benchmarking (pass rate/time/tokens), blind A/B comparator agents, description-optimization loop. It now covers a real fraction of what the June doc said only third-party tools (`skill-eval`, `skills-check`) provided — re-evaluate the harness build list against it before building anything. https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills
- Validation tooling: `skills-ref validate ./my-skill` from the standard's reference implementation. https://github.com/agentskills/agentskills

### 1.5 Stale-claims check on the June doc

Flagged for correction in the next research fold: star counts (anthropics/skills now ~149k, not 155k), the agentskills.io client list (~40 → much larger post-standardization), "SkillGuard isn't shippable" (unverified either way — recheck), "agent teams experimental" (Claude Code has since merged commands into skills and shipped subagent composition both directions: `context: fork` on skills, `skills:` preload on agents).

---

## §2 Context-engineering findings that bind on skill authoring

The discipline's one-line definition (Karpathy): *"filling the context window with just the right information for the next step."* The findings below are the ones with direct editorial consequences for SKILL.md files.

### 2.1 Length is a measured tax, not a style preference

- **Context rot [STRONG]:** across 18 models, "performance varies significantly as input length changes, even on simple tasks" — degradation is monotonic with length even when difficulty is constant. https://www.trychroma.com/research/context-rot
- **Focused beats full [STRONG]:** LongMemEval — a ~300-token focused prompt materially beats a ~113k-token prompt *containing the same relevant information*, for all models tested; thinking modes narrow but don't close the gap.
- **Anthropic's frame [VENDOR]:** models have a finite "attention budget"; "every new token introduced depletes this budget." https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- **The official CLAUDE.md warning [VENDOR]:** "Bloated CLAUDE.md files cause Claude to ignore your actual instructions… If Claude keeps doing something you don't want despite having a rule against it, the file is probably too long and the rule is getting lost." https://code.claude.com/docs/en/best-practices

### 2.2 Position and phrasing govern retrieval

- **Position [STRONG]:** U-shaped attention — beginning and end of context are reliable; the middle is the worst real estate (Lost in the Middle, arXiv 2307.03172; reconfirmed at length by Chroma 2025). Put laws at the top of the file; recite live state at the end of context (Manus's `todo.md` recitation pattern exploits exactly this).
- **Similarity [STRONG]:** the lower the semantic similarity between an instruction and the task phrasing that should invoke it, the steeper the degradation with length (Chroma). *Write rules in the vocabulary the tasks will use* — this is also the mechanistic case for concrete good/bad examples over abstract directives.
- **Distractors compound [STRONG]:** loosely related prose around a rule actively degrades retrieval of the rule, worse with length. Masthead changelogs sitting above the laws are, in retrieval terms, distractor mass.
- **Negation [emerging]:** accumulating "NEVER…" prohibitions degrades compliance; positive framing with sparing, emphasized negatives is the practitioner synthesis. In tension, official docs endorse "IMPORTANT"/"YOU MUST" emphasis — both can be true: emphasize a few negatives, don't stack dozens. https://eval.16x.engineer/blog/the-pink-elephant-negative-instructions-llms-effectiveness-analysis
- **Format [STRONG but model-specific]:** meaning-preserving format changes swing accuracy up to tens of points, and sensitivity doesn't transfer between models (FormatSpread, arXiv 2310.11324) — so format tweaks are empirical questions for *your* model; don't cargo-cult.

### 2.3 Self-editing instruction files: the ACE result **[STRONG — the headline finding for W-SKILLS]**

"Agentic Context Engineering" (arXiv 2510.04618, ICLR 2026) formalizes the two failure modes of letting an LLM maintain its own playbook:

- **Brevity bias** — summarization erodes domain detail.
- **Context collapse** — "iterative rewriting erodes details over time"; wholesale re-summarization silently deletes hard-won rules.

Their fix — structured **incremental delta updates** by separate generator/reflector/curator roles, never wholesale rewrites — produced +10.6% on agent benchmarks with no labeled supervision.

**This is an independent validation of two things NexSys already invented in practice:** the rule census ("23-in / 28-out with every prior name surviving") is a manual anti-context-collapse check, and the currency-pass structure (dedicated fresh lane, per the full-bar-at-fresh-context law) is the curator role. The census should be promoted from practiced habit to written law of the currency pass (§5).

Related, same direction: Anthropic's long-running-harness post found models corrupt Markdown state files more readily than JSON ("the model is less likely to inappropriately change or overwrite JSON files") — relevant to any file the steward *writes*, e.g. the rot-incident tally. https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents

### 2.4 Fresh contexts beat heroic sessions — now quantified

- Multi-turn drift: average **39% drop** single-turn → multi-turn; "when LLMs take a wrong turn… they get lost and do not recover" (arXiv 2505.06120) **[STRONG]**.
- Official guidance: after two failed corrections, `/clear` and rewrite — "a clean session with a better prompt almost always outperforms a long session with accumulated corrections" **[VENDOR]**.
- Subagent returns should be **1,000–2,000-token distilled summaries** [VENDOR] — a concrete sizing target for your lane-return docs.
- The Cognition-vs-Anthropic disagreement resolves cleanly: parallelize read-heavy research (Anthropic measured 90.2% uplift, at ~15× tokens), keep write/code single-threaded (Cognition: "actions carry implicit decisions, and conflicting decisions carry bad results"). Design v1 §8.5 (cross-module work forks read-only Explore subagents, synthesizes in parent) already matches the synthesis.

Your fresh-context law and the operator-packet/handoff discipline are, per this literature, not idiosyncrasies — they are the published best practice, arrived at independently. Fold that into the skills as *why* text ("do X because Y"), which the guidance says improves adherence.

---

## §3 Audit: the live library vs. the evidence (input to v44)

Measured against §1–§2. All three skills pass on line count and description length; **all three fail the 5,000-token body budget** — and §1.2 makes that budget a compaction survival boundary, not a lint warning.

| | PM | Coder | Frontend |
|---|---|---|---|
| SKILL.md words (≈tokens) | 6,316 (~8.2k) | 4,529 (~5.9k) | 5,165 (~6.7k) |
| Masthead share of file | **36%** (17.4 KB) | **33%** (11.3 KB) | 10% |
| Description chars | 717 | 783 | 974 |
| references/ | 6 files / 17.1k words | 5 files / 12.8k words | 5 files / 6.5k words |

**A. The mastheads are distractor mass in the worst position.** 28 indexed arc-laws (PM) and four parallel arc blocks (coder) sit in an always-loaded HTML comment above the operating sections. Per §2.2, changelog/provenance prose adjacent to laws actively degrades law retrieval; per §1.2, it also pushes the operative back half of the file past the compaction boundary. Move: laws stay (they ARE the skill), but as a lean top-of-body section; the v23→v40 arc history, `last-verified` changelogs, and compression notes move to `references/arc-history.md` (or MANIFEST, where SK-INV-06 says provenance belongs). Note the PM's own line 13 admits the pattern: compression passes are losing to accretion (17→28 rules in two passes).

**B. `freshness-preflight` has tripled, not de-duped.** F3 was flagged 2026-06-27 (162/231-line duplicates); there are now three forks (PM 11 checks / coder 7 / frontend 8). This is the exact "one term per concept, one home per fact" violation the official anti-pattern list names, and the shared-discipline extraction (`disciplines/freshness-preflight`) is the design's own answer. Highest-value single de-dup in the library.

**C. The frontend skill's §4a–§4e is the library's largest SK-INV-01 breach** — ~14 KB of accreted wire truth (enum values, field names, commit SHAs, file:line pointers, measured timings) inside the skill that most loudly cites SK-INV-01, hedged ~6 times with "these are POINTERS, re-read the source." The hedge is an admission. Move the durable *mental model* up, the volatile facts out to the cited sources, and delete superseded bullets (the skill's own v1.7 expiry-hygiene rule, applied to §4). Also: "Pelton results ~Aug-5" is hard-dated and goes stale within days — exactly the "time-sensitive info" anti-pattern.

**D. The Clock-injection law has five+ homes** (coder §2, §8, java-patterns §11, testing-standards §8, PM §4c, coding-instruction-format:484). Pick the authoritative home (coder skill), pointer from the rest. SK-INV-02.

**E. Small but telling rot exhibits, still live:** README's SD-5 mis-citation (found 2026-06-27, uncorrected — a ghost-commit-class exhibit in the skills repo itself); PM/coder Check-9 scripts still resolving mirror sources to the pre-`nexsys-skills` hivemind paths; the `orchestrators/nexsys-frontend/` directory asserted by MANIFEST and the skill's own masthead but absent from the repo tree (either staging artifact or a real writable-source gap — **verify before v44**, because if the writable source is missing, the mirror is the only copy and Check-9 is guarding the wrong direction).

**F. Zero evals, zero provenance, zero budget enforcement exist yet** — every SK-INV-05/06 mechanism is still designed-only. The one live integrity instrument is the manual rule census. Given §1.4 (skill-creator now ships evals, benchmarking, A/B comparison, description optimization), the cheapest Rung-0 is no longer "build the harness" but "adopt skill-creator's loop + `skills-ref validate` + the one Gradle drift-check nobody else will build for you." That re-scopes SD-5's build list materially.

**G. Descriptions are good; add negative boundaries.** All three follow the pushy-trigger doctrine. None state what they are *not* for (the skill-architect SPEC draft does). With co-triggering risk among three sibling role skills sharing verbs ("review," "design," "write"), add one boundary clause each — official guidance for overlap is precisely "clarify the boundary between this skill and adjacent capabilities."

---

## §4 Ruling input: per-module skills

**Yes to the tier, no to the batch.** The evidence, old and new, converges:

1. **Selection degrades with catalog size and confusability, not just size** — tool/skill-selection studies show 7.6–85.6% degradation as catalogs grow (LongFuncEval, arXiv 2505.10570) [STRONG], and the June doc's SkillsBench numbers already showed the marginal skill's value collapsing past 2–3 co-loaded (+18.6pp → +5.9pp). The new eviction mechanics (§1.1) add a silent failure mode: more skills = thinner shared description budget.
2. **The design already contains the correct build selector.** Deliberation T3: build the specific module/seam skill whose mental model has been **re-derived by ≥3 independent fresh sessions**. That is demand-paged skill creation — build what sessions actually keep paying to re-derive, in the order the re-derivation tax reveals. The 13-module catalog is a *namespace*, not a work order.
3. **The extraction sources already exist.** Coder's `homesynapse-mental-model.md` is a proto module-skill bundle (event log, envelope, device model, integration boundary, SQLite store…); PM's 9-row MODULE_CONTEXT table and cross-subsystem references are the Tier-2 seed material. First module skills should be *extractions with a rule census*, not fresh authorship.
4. **Use `paths` scoping when you build them** (§1.3) so module skills activate structurally on file location, reducing the description-confusability load. And keep design §8.5's law: module skills are mutually exclusive at the active layer; cross-module work forks read-only subagents rather than stacking skills.
5. **Sequencing stands as designed:** Rung 1 = `event-model-and-bus` (or whichever module T3 actually fires on first), hardest module as graduation exam, never two unknowns at once. The one amendment this return proposes: re-scope Rung 0 around skill-creator's now-shipped eval loop (§3F) so SK-INV-05 can be enforced from the first module skill.

**Counter-consideration, honestly stated:** a per-module skill is a new standing maintenance liability in a library that currently fails its own budgets and has zero drift detection. Every module skill added before the harness exists increases the rot surface the harness is supposed to watch. That is the strongest argument for T3-gating rather than enthusiasm-gating.

---

## §5 The W-SKILLS v44 pass — recommended execution order

Framing: v44 is two distinct jobs and should be run as two lanes (fresh context each, per your own law): **(a) the law fold** (v42–v43 harvest → PM + siblings) and **(b) the structural conformance pass** (this return's audit). Folding new laws into files that are over budget makes the budget problem worse; do (b) first or concurrently, never after.

1. **Pre-flight:** resolve §3E's `orchestrators/nexsys-frontend/` writable-source question; fix the SD-5 mis-citation and the Check-9 stale paths while in there.
2. **Structural pass (per skill):** masthead → `references/arc-history.md` + MANIFEST; laws to top-of-body (position, §2.2); verify each file's first 5,000 tokens contain everything that must survive compaction (§1.2); delete expired caveats (frontend's own v1.7 rule, applied everywhere); run the pruning test line-by-line ("would the agent get this wrong without this line?").
3. **De-dup pass:** freshness-preflight → one shared discipline skill (F3, two months open); Clock law → one home + pointers (§3D). Note both set Check-9 STALE until your mirror sync.
4. **Law fold (v42–v43 harvest):** delta-edits only — add each law as a named indexed entry with its pointer; **rule census in / out with every prior name surviving** is now written law of the pass, not habit (ACE, §2.3). Where a law has a *why*, write the why ("do X because Y causes Z" outperforms bare directives, §1.4).
5. **Description pass:** add one negative-boundary clause per orchestrator (§3G). If you touch descriptions, run the cheap trigger eval (20 queries, 3×, 60/40) via skill-creator rather than eyeballing.
6. **Close:** rule-census totals + file token counts recorded in the pass return; both mirrors diff-clean; a one-line skills-trigger check (T1–T5) appended per the deliberation's cadence rider.

Timing in the Aug 3–4 lull is fine; the structural pass (2–3) is the part worth protecting if the lull shrinks — it compounds into every future session, while the law fold can ride any later pass.

---

## §6 W-EXEC — the executive skill

**Endorse the PM's ruling (design now, author post-charter), with the evidence attached.** The official grounding doctrine is explicit: don't let an LLM generate a skill from generic knowledge — extract from real artifacts (decisions made, corrections issued, formats that worked). https://agentskills.io/skill-creation/best-practices.md Pre-charter, W-EXEC's only available source *is* generic LLM knowledge plus speculation; post-charter, its source is ratified doctrine with evidence receipts — the substrate thesis, the bets-table cadence, conditions-not-dates, the truth-brand laws, the hours-budget discipline. Anthropic's own taxonomy distinguishes "capability uplift" skills from **"encoded preference" skills** — W-EXEC is the purest encoded-preference skill in your catalog, and encoded preferences must exist before they can be encoded.

Design considerations from the evidence:

- **It is a thinking instrument, not a knowledge cache** — high degrees-of-freedom per the official framework: prose heuristics, question sets, and rubrics, not procedures. This is the skill where "right-altitude" prompting matters most: strong heuristics, zero hardcoded conclusions.
- **Question-set architecture beats answer architecture.** The one practitioner genre that consistently reports value from advisory prompts attributes it to structured interrogation, not simulated wisdom ("the framework dominated the value"). W-EXEC's body should be mostly questions the executive session must answer, ordered, with escalation rules for when an answer is missing from the charter.
- **Trigger design:** W-EXEC's description needs the strongest negative boundary in the catalog — it must never co-trigger with PM work ("quarterly re-read," "bets table," "charter" yes; task briefs, WUCP, coding instructions never). It is also the natural candidate for `disable-model-invocation: true` — an executive session is something *Nick convenes*, not something the model wanders into.
- **Cadence hooks belong in the skill:** the quarterly re-read trigger, the conditions-not-dates review, and a standing instruction that any session finding charter-doctrine violated files it to the tally rather than silently adapting — this is how the skill becomes the longevity instrument you want, staying current *by procedure* as the market moves rather than by embedded market facts that rot.
- **The design brief as a named charter input** is the correct mechanic — it means the charter session itself is the eval fixture for W-EXEC v1: author the skill, then re-run the charter's hardest three decisions cold with the skill loaded and check it reproduces the ratified reasoning (a depth-probe eval, per the skill-architect SPEC's pattern).

**Appendix A carries a draft design-brief question-set** so the "design its question-set now" half of the ruling can execute today without pre-encoding any conclusions.

---

## §7 Personas: the evidence, and how to get the value without the costume

The literature here is unusually decisive, and it splits exactly along the line you'd want it to:

**What does not work — identity as persona [STRONG, replicated]:**
- 162 personas × 2,410 questions across 4 model families: personas "did not improve model performance"; per-persona effects "largely random" (arXiv 2311.10054).
- 2025 replication on frontier models (Wharton, GPQA Diamond + MMLU-Pro): "persona prompts generally did not improve accuracy… Expert personas showed no consistent benefit"; mismatched personas went negative; recommendation: "focus on task-specific instructions" (arXiv 2512.05858).
- 2026 reconciliation (PRISM, arXiv 2603.18507): personas *help* style/format/safety-alignment tasks (+0.40–0.65 MT-Bench writing/roleplay) and *hurt* knowledge retrieval (−3.6% MMLU) — which explains the conflicting folklore.
- On some datasets, ~14% of questions answered correctly *without* a persona flip to wrong *with* one (arXiv 2408.08631).

**The risks are real and specific:** persona-induced hidden bias (arXiv 2311.04892); sycophancy amplification when the prompt flatters an authority identity (Anthropic, arXiv 2310.13548); and **persona drift** — in real Claude Code sessions of 3,700–9,700 turns, persona/register drift is universal and "in-session compaction does not reliably reset" it (ContextEcho, arXiv 2605.24279) — so a costume set in a skill file wouldn't even survive the sessions it's meant to govern. On naming real executives: right-of-publicity law targets commercial use of identity, and a private internal prompt file is far from that fact pattern, but risk rises if outputs are published in ways implying endorsement or mimicry — and I'm not a lawyer, so if W-EXEC material ever becomes external-facing (investor docs, marketing), have that reviewed. The clean mitigation is the same as the effectiveness recommendation: encode the framework, not the identity.

**What does work — mechanisms with names as citations, not costumes:**

The same literature that kills "respond as Steve Jobs" supports detailed, instruction-specific expert *content* (ExpertPrompting's gains came from injected domain specifics, not names) and structured multi-perspective interrogation (Solo-Performance-Prompting's gains — GPT-4-class only — came from forcing distinct analytical passes). So build the trait-borrowing you want as a **council of lenses**, one reference file per lens, each lens = the executive's actual operating mechanism stated as procedure + the questions it forces:

- **Bezos lens** — reversibility: classify the decision one-way vs two-way door; two-way → decide fast with ~70% of the information; one-way → slow down, write the six-pager; disagree-and-commit recorded by name; working-backwards/PR-FAQ for anything new.
- **Grove lens** — paranoia audit: what 10× force is forming; is this signal or noise a strategic inflection point; what would a new management team do walking in today; OKR discipline on the quarter.
- **Jobs lens** — focus: what are we saying *no* to this quarter (the kill-list is a deliverable, not a vibe); is the substrate thesis still the thing the whole stack serves; simplicity as a forcing function on the product surface.
- Add lenses only when the charter shows a recurring decision type none of the existing lenses interrogates well (same T3 logic as module skills — demand-paged, not collected).

Each lens cites its sources (the shareholder letters, *Only the Paranoid Survive*) — which keeps it honest, auditable, and refreshable, and gives W-EXEC exactly the property you asked for: followers can copy features; a doctrine with evidence receipts, interrogated quarterly through named mechanical lenses, is an operating system.

Where a *style* borrow is legitimately wanted (e.g., the truth-brand voice in external copy), that's the one place the persona literature says personas do help (style/format tasks) — put it in `nexsys-frontend`'s brand layer as concrete voice examples, not in W-EXEC.

---

## Appendix A — Draft W-EXEC design-brief question-set (a charter input, per the ruling)

*Purpose: these are the questions whose ratified answers become W-EXEC's body. Unanswered = the charter owes an answer or the skill stays silent on it. No question below encodes a conclusion.*

**Identity & invocation**
1. Who convenes an executive session, and can the model ever self-trigger one? (Recommended default: Nick-only; `disable-model-invocation: true`.)
2. What is the skill's negative space — which adjacent work (PM briefs, WUCP, coding) must it refuse and route back?

**Doctrine to encode (post-charter)**
3. State the substrate thesis in one paragraph as the moat frame. What evidence receipt does each claim carry?
4. What is the bets table's schema and cadence? What retires a bet? What promotes one?
5. Conditions-not-dates: enumerate the standing conditions being watched, each with its falsifier and its source-of-truth pointer.
6. The truth-brand laws: enumerate, each with its origin exhibit.
7. The hours-budget discipline: the budget, the floor rules, who may spend against it.

**Lenses (§7)**
8. Which decision types recur? Map each to a lens (reversibility / paranoia-audit / focus / other). Which lens is the default when types conflict?
9. For each lens: its procedure in ≤10 lines, the 3–5 questions it forces, its source citations.

**Cadence & longevity**
10. Quarterly re-read: what triggers it (date, condition, or tally event), what it must re-verify, what it may amend without Nick.
11. What market/technology change classes invalidate charter doctrine (vs merely inform it), and where does a session file a suspected invalidation?
12. What is W-EXEC's own refresh law — which currency pass owns it, and what is its rule-census equivalent (doctrine-census)?

**Evals (SK-INV-05, before first sync)**
13. Depth-probe: which 3 hardest charter decisions must a cold session with W-EXEC reproduce the reasoning for?
14. Trigger eval: 10 should-fire phrasings, 10 near-miss should-not (PM-flavored) phrasings.
15. Retirement test criterion: what would prove the model no longer needs the skill?

---

## Appendix B — Source index (load-bearing subset)

**Official/vendor:** Agent Skills spec & authoring canon (agentskills.io: specification · skill-creation/best-practices.md · optimizing-descriptions · evaluating-skills) · platform.claude.com skills overview & best-practices · code.claude.com/docs/en/skills (budgets, truncation, compaction re-attach, frontmatter extensions) · code.claude.com/docs/en/best-practices (CLAUDE.md doctrine) · anthropic.com/engineering: equipping-agents-for-the-real-world-with-agent-skills · effective-context-engineering-for-ai-agents · effective-harnesses-for-long-running-agents · multi-agent-research-system · claude.com/blog: skills launch · skill-creator update (2026-03-03) · context-management · steering-claude-code.

**Studies:** Chroma context rot (trychroma.com/research/context-rot) · Lost in the Middle (arXiv 2307.03172) · LLMs Get Lost in Multi-Turn (2505.06120) · ACE (2510.04618, ICLR 2026) · FormatSpread (2310.11324) · prompt-format impact (2411.10541) · Let Me Speak Freely (2408.02442) · LongFuncEval (2505.10570) · personas: 2311.10054 · Wharton 2512.05858 · PRISM 2603.18507 · 2408.08631 · ExpertPrompting 2305.14688 · SPP 2307.05300 · Bias Runs Deep 2311.04892 · sycophancy 2310.13548 · ContextEcho persona drift 2605.24279.

**Practitioner:** Manus context-engineering lessons · Cognition "Don't Build Multi-Agents" · HumanLayer advanced context engineering · Lance Martin (taxonomy; Claude Diary) · SwirlAI state-of-context-engineering-2026 · happyskills.ai / blog.fsck.com (eviction mechanics) · Lee Hanchung skills deep-dive · Arize skills-vs-MCP eval · MindStudio context-rot pieces · Paul Silva virtual-board writeup · Authors Alliance / CRS LSB11052 (right of publicity).
