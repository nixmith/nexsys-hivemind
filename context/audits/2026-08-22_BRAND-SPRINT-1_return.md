<!--
file: context/audits/2026-08-22_BRAND-SPRINT-1_return.md
purpose: BRAND-SPRINT-1 RETURN — the research half of the G-2 readiness §5 board, executed before the branch word so that on the word (~Wed/Thu Aug-27/28) the build-out is a choice among studied options. Rows returned: B-1 (identity directions, {{NAME}}-parameterized) · B-7 (JP/katakana variant study) · B-2 (the voice/tone §-fold) · B-3 (the website brand-integration map, pointers only) · B-5 (the claim-fence register, table only). Out of scope and untouched: B-4, B-6, B-8.
audience: Nick (rules the directions the day the word lands); the hub (intake audit; ≥5 citation spot-checks).
state-type: research-lane return (read-only; ONE artifact — H11).
fences held (each checkable — see §6.3): nothing public · no candidate name typed into any external form that creates a record (no WHOIS, no registrar, no social-handle probe, no trademark-office SEARCH) · no edits to any repo (this file is the only write) · no vendor or foundry contact · every font/licence claim from the foundry's own page or its source repo, with the fetch date · the D-1 fence survives every sentence · the working name stays everywhere it is today.
not-a-lawyer: research by a non-lawyer (+AI). Every register/field observation is a DESIGN or LINGUISTIC observation about distinctiveness and reading, never a conflict or clearance conclusion. §2.5 stops at what the filing needs; the legal answer is counsel's.
honesty-frame: n=6 individual native speakers, one per market — anecdotal field data, not market research. It prices linguistic risk and register fit, never demand. Weighted accordingly throughout.
filed: 2026-08-22 (filing-day convention).
-->

# BRAND-SPRINT-1 — the build-out board, researched before the word

## §0 Verdict, and the recommendation per row

**The board is studiable before the word, and the study changed two things.** First, the charter's governing design premise — *the F-N4 Z→S drift argues a mark that visually anchors the ZEN- onset* — is **half right and half backwards**, and the raw result files (not the bank's summary) say so: the drift is a real phonemic gap in exactly **one** of six markets (ES), an **orthographic artefact only** in the one other market that names it (DE, where writing "Sendomo" is how a German spells the /z/ the mark wants), and **absent in four** (JP · FR · IT · NL). Meanwhile **five of six markets put the tonic on -DO-**, and the one market that stresses ZEN- (NL) is also the one that read the name as *"air freshener, fresh breath."* A mark that shouts the onset fights the way most of the world says the word, in service of a problem typography cannot fix — you cannot letterform a phoneme into a language that lacks it. The onset device survives **as a letterform, not as a colour or weight contrast**, and the anchoring job moves to the tail. Second, the 07-22 exploration's colour section **argues against a palette that no longer ships**: it computes against the DRAFT design-system values (`#3FA6C9` on `#ECEFF3`, 2.42:1 — reproduced exactly this session), while the shipped token file already supersedes them with a mode-paired system that passes AA everywhere but one 0.03-short case (§1.6). B-1's remaining work is letterforms, a device, and a favicon that **does not exist on any surface today**.

| Row | Recommendation | Confidence |
|---|---|---|
| **B-1** | **Direction B — "The Domo Anchor"** (§1.4): one engineered onset glyph (Z; V for the hedge) carries the distinctiveness over a tail drawn once and never redrawn. A and C held as the branch-B/C fallbacks. | High on the evidence; the 16-px render test is the FE lane's (§6.4). |
| **B-7** | **ゼンドモ** as the katakana of record, **ゼンドーモ** as the defensive variant; carry the katakana as a **separate application**, not a stacked composite — the JPO's own standard-character rule forbids multi-row composition (§2.5). | High on the transliteration; the filing form is counsel's. |
| **B-2** | The fold in §3 is paste-ready: it confirms the calm register, **corrects one thing** (calm is now evidence — and calm is also the risk, per the NL read), and ships two microcopy exhibits. | High. |
| **B-3** | **The runbook's website row is over-scoped by ~19 files.** The rendered site's working-name surface is **one value**: `website/site/src/lib/brand.mjs:14` (§4). | High — verified at the bytes. |
| **B-5** | §5 is the instrument the post-R-4 kit is written against. The live site copy already models the honest form (`ledger-gap-dossier.md:12`) — use it as the template, not a new invention. | High. |

---

## §1 B-1 · Identity directions v1, {{NAME}}-parameterized

### 1.1 What the field actually taught (re-read at the raw files, beside the bank)

The bank's cross-market table is correct and is not disturbed. What follows is what the *raw* result files carry that the bank's §2–§3 adjudication did not name.

| Market | Stress, as the checker wrote it | Onset actually produced | Register words, verbatim |
|---|---|---|---|
| JP | mora-timed; no stress marked | ゼ /ze/ — clean | "because it starts with the word zen, the word zen comes to mind, that's pretty much it" |
| DE | "Zen-DO-mo… stress on DO" | /z/ — **spelled** "Sendomo" because German ⟨z⟩ = /ts/ | "Zen, calmness, something Japanese" |
| FR | `[z][ɛ][n] [d][o][m][o]`; French phrase-stress falls final | /z/ — clean | "calm, peace, nature, birds, domotic, high-quality"; "by far the strongest… clean, serene and high-end" |
| ES | "zen-DO-mo"; **"sen-DO-mo: in some areas, people pronounce 'z' as 's'"** | **/s/ or /θ/ — Spanish has no /z/ phoneme** | "Zen: calm, relaxation, peace · Domo: home, home automation · Senda: path" |
| IT | "[zen-dó-mo] → The stressed syllable is 'do'" | /z~dz/ — clean | "the 'zen' philosophy… meditation and mindfulness" |
| NL | **"ZENDOMO: ZEN-do-mo"** — the only first-syllable stress on the board | /z/ — clean | **"meditation, air freshener, fresh breath"** |

- **F-B3 (the pushback the brief invited).** The drift is **1 of 6 phonemic** (ES — no letterform supplies a missing phoneme), **1 of 6 orthographic** (DE — the checker's "Sendomo" *is* the /z/ onset, written the German way), **4 of 6 clean**. Anchoring the onset to defeat the drift buys almost nothing; anchoring it for *distinctiveness* still buys plenty — which is why the device survives in a different form.
- **F-B4 (new, load-bearing).** Five of six put the tonic on **-DO-**. A wordmark whose visual weight sits on ZEN- is out of phase with how the mark is spoken almost everywhere. The tail is where the stress is, where the *home* meaning is (FR *domotique* · ES *"Domo: home, home automation"* · IT *"we mainly relate it to 'home'"*), and where 100% of the hedge transfer lives.
- **F-B1 (new; the NL category drift).** ZENDOMO scored 5/5 in NL and the bank flagged nothing — but the unprompted first-three-things were *"meditation, air freshener, fresh breath."* A **CPG category read**, not a rude one: at maximum calm the name drifts toward household consumable, and nothing in the name corrects it. **The identity has to say "infrastructure" out loud, because the name will not.** This is the most useful thing the field handed the wordmark exercise, and it points away from soft/rounded/wellness letterforms — the exact register a "calm" brief would otherwise walk into.

### 1.2 Constraints every direction inherits (verified, not assumed)

| Constraint | Source, at the bytes |
|---|---|
| Wordmark-only at launch; a future symbol must not force reflowing the wordmark; usage governance ships with any symbol day one | W-6 + W-3a #2 — `2026-06-12_website-brand-deliberation_draft-rulings.md:28`, `:37` |
| One accent with the interaction monopoly; warmth illustration-only; **red retired from the identity** (error register owns it) | W-9 (`:42`) + identity exploration §6 ruling 4 |
| Handles are **`{{name}}hq`-canonical uniformly**; bare name on package registries | `2026-07-23_domain-handle-claims-refresh.md` §C.1 — so the lockup must survive a 10-character `zendomohq` and `@zendomohq` |
| Never a CDN / Google Fonts; fonts self-hosted, subset, served from loopback | `web-ui/dashboard/src/styles/fonts.css:4` (INV-LF-01); reproducible `pyftsubset` recipe at `src/styles/fonts/README.md` |
| The shipped UI face is **Inter variable, 25,388-byte subset**; weights 400/500/600 in use | `src/styles/fonts/inter-variable-subset.woff2`; `tokens.css:53–55` |
| **No favicon exists on either surface** — `web-ui/dashboard/index.html` has no `rel=icon`; `website/site/` has no `public/` directory | verified by grep + `ls`; §4 row 6 |
| The wordmark is a **string**, not an asset | dashboard `i18n.ts:18`; site `brand.mjs:14` |

**Letterform facts of the string** (the 07-22 TAMORO paragraph, re-derived): **ZENDOMO** — 7 letters, 3 syllables, two O's, **no descenders in either case** (lowercase carries one ascender, the *d*). **VERDOMO** — same length, same syllable shape, same two O's, same no-descender property, and it shares **five of seven glyphs in position**: `_E_DOMO`. The two candidates differ **only at positions 1 and 3**. That fact is what the recommendation is built on.

### 1.3 The schematic (Direction B, with the hedge swap beneath)

<svg viewBox="0 0 520 175" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Schematic: an engineered Z onset glyph over a tail rule under DOMO, with the V swap for the hedge shown beneath." style="max-width:100%;height:auto;color:currentColor">
  <g fill="currentColor">
    <path d="M20,20 H70 V31 L37,59 H70 V70 H20 V59 L53,31 H20 Z"/>
    <text x="80" y="70" font-family="Inter,'Helvetica Neue',Arial,sans-serif" font-size="50" font-weight="700" letter-spacing="-1">ENDOMO</text>
    <rect x="148" y="79" width="134" height="4"/>
    <text x="292" y="46" font-family="Inter,Arial,sans-serif" font-size="11" opacity="0.75">onset = the ONE cut glyph (distinctiveness)</text>
    <text x="292" y="62" font-family="Inter,Arial,sans-serif" font-size="11" opacity="0.75">tail = the tonic in 5/6 markets + the home</text>
    <text x="292" y="76" font-family="Inter,Arial,sans-serif" font-size="11" opacity="0.75">meaning + 100% of the hedge transfer</text>
    <path d="M20,100 H34 L45,138 L56,100 H70 L53,150 H37 Z"/>
    <text x="80" y="150" font-family="Inter,'Helvetica Neue',Arial,sans-serif" font-size="50" font-weight="700" letter-spacing="-1">ERDOMO</text>
    <rect x="148" y="159" width="134" height="4"/>
    <text x="292" y="132" font-family="Inter,Arial,sans-serif" font-size="11" opacity="0.75">branch C: two glyphs re-cut (Z→V, N→R).</text>
    <text x="292" y="147" font-family="Inter,Arial,sans-serif" font-size="11" opacity="0.75">The tail, the rule, the spacing: untouched.</text>
  </g>
</svg>

*Schematic, not a cut: the letters sit in a fallback stack to show proportion and anchoring logic; the drawn glyph shows the flat-shear terminal language. Everything renders in `currentColor` — the monochrome-survivability rule made literal.*

### 1.4 The three directions

Every face below verified **SIL Open Font License 1.1** at the foundry page or its source repo, fetched 2026-08-22 (§6.1). No direction requires a paid asset.

| | **A — "The Anchored Onset"** (the charter as written) | **B — "The Domo Anchor"** — **RECOMMENDED** | **C — "Quiet Infrastructure"** (the floor / standing interim) |
|---|---|---|---|
| **The idea** | All-caps geometric grotesk; ZEN- carried by an explicit contrast device — a weight step (ZEN 800 / DOMO 500) or the accent on the first three letters | All-caps, tight-tracked, monochrome-first, **one** engineered glyph: a Z with flat-shear terminals, its diagonal cut to the same angle as the O aperture, over a tail carrying a hairline rule (or a tracking step) under -DOMO. The two O's stay the squared "enclosure" rounds from the 07-22 W-A language | The wordmark **is** the product's own type system, typeset to spec: Inter 700, tracking −2 to −3%, at most one ownable modification, no device. Distinctiveness comes from the system around it |
| **Typographic stance** | **Archivo** (Omnibus-Type, Héctor Gatti) — OFL 1.1, `OFL.txt`, variable **weight + width**. The width axis is the honest reason to pick it: a Condensed instance is what survives a narrow lockup and the `{{name}}hq` handle | **Inter** (Rasmus Andersson / RSMS) — OFL 1.1 — as the *drawing substrate*, since it is already the product's voice and already in the image at 25 KB. The mark is a **derived cut**: Z, aperture and tracking drawn; everything else re-renders from the token | **Inter**, unmodified. Optionally **Space Grotesk** (Florian Karsten, OFL 1.1, derived from Colophon's Space Mono) for a more opinionated display voice — its idiosyncratic lowercase argues against it for a calm register |
| **Onset device** | Weight/colour contrast on ZEN-, plus a flat-shear Z apex | **Letterform only** — nothing that dies in monochrome | None |
| **Colour stance** | Accent on the onset — **and this is where it breaks** (§1.6): a two-tone mark loses its whole idea in monochrome, in a favicon, and on an embossed label; on light it must use `--hs-accent-600`, never `-500` | **None in the mark** — it is `currentColor`. The direct answer to F-B1: an infrastructure mark does not need colour to be itself | None |
| **Dashboard-first (16 px tab / 0.5 cm label)** | Two-tone at 16 px is unreadable; needs a separate mono favicon anyway | Survives by construction — the cut glyph *is* the favicon candidate (the monogram the tab needs; §6.4) | Survives; but leaves the favicon problem entirely unsolved |
| **Dark/light pair** | Two variants per theme (four assets) once colour enters the mark | **One asset.** `currentColor` inherits `--hs-text` in both themes: 16.53:1 dark, 16.40:1 light | One asset, same property |
| **Accessibility floor** | AA passes only if the coloured half uses accent-600 on light (6.38:1); accent-500 is 4.47:1 (§1.6) | AAA in both themes at the text token; the wordmark is large text (3:1 floor, SC 1.4.3) with vast headroom | Same as B |
| **Cost to execute** | ~14–20 h, **$0 paid assets** | ~10–16 h, **$0 paid assets**; ~2–4 KB for a 7-glyph subset if the cut ever ships as a font rather than SVG | **An afternoon** |
| **What it forecloses** | A single-colour mark — once two-tone is the brand, the mono version reads as degraded | A mark readable at a glance as *warm*; this direction is deliberately cool | Nothing. That is the point |
| **Transfer to the hedge** | The device transfers; **the argument does not** — VER- is not a morpheme any market recognised as meaning anything but *green* (F-N1) | **Strongest on the board, and measurable:** positions 2 and 4–7 (`E`,`D`,`O`,`M`,`O`) are identical. Branch C re-cuts **two glyphs** (Z→V, N→R) and keeps tail, rule, aperture language, tracking and clearspace — **days, not weeks**, against the 07-22 map's "1–2 weeks for an unrelated fallback" | Zero cost, any name |
| **Honest read** | It executes the charter, and the charter's premise does not survive §1.1 | It buys distinctiveness where distinctiveness is cheap (one glyph) and spends nothing where the field says the value is (the tail) | The 07-22 W-B position, unchanged, and still correct as the **standing interim** — the mark that presumes nothing and guarantees the program is never blocked on type work. It is not a launch mark |

### 1.5 The recommendation

**Develop B. Keep C standing. Hold A as the branch-B argument.**

- **Branch A (clean):** B charters at the R-1 word; C stays live on every surface until B's spec is signed, so nothing waits.
- **Branch B (mixed/trims):** the trims are argued from **A vs B** — A's two-tone is what a stylised design-mark application would carry beside a standard-character one, if counsel ever wants it; B ships regardless.
- **Branch C (adverse):** B transfers to VERDOMO for **two re-cut glyphs**. Every other artifact in this return — the colour stance, the tail rule, the accessibility floor, the katakana method, and all of §3/§4/§5 — is name-parameterized and transfers at **zero cost**.

### 1.6 The accessibility floor (computed this session against the SHIPPED tokens)

Method: WCAG 2.x relative luminance, exact hexes as they stand in `web-ui/dashboard/src/styles/tokens.css`. **Method cross-check:** recomputing the 07-22 exploration's own legacy pairs reproduced its published figures exactly (`#3FA6C9` on `#ECEFF3` = 2.42:1; on `#0B0F14` = 6.87:1), so these numbers are on the same instrument.

| Pair (shipped token) | Ratio | Verdict |
|---|---|---|
| `--hs-text #eceff3` on `--hs-bg #0d1014` (dark) | **16.53:1** | AAA |
| `--hs-text #161a20` on `--hs-bg #f6f8fa` (light) | **16.40:1** | AAA |
| `--hs-link`/`--hs-focus-ring` = accent-300 `#6db8e8` on dark bg | **8.78:1** | AAA |
| **`--hs-link`/`--hs-focus-ring` = accent-500 `#1577be` on light `--hs-bg #f6f8fa`** | **4.47:1** | **0.03 short of AA-normal**; passes on `--hs-surface #ffffff` (4.76:1) |
| `--hs-accent-600 #11608f` on light bg | **6.38:1** | AA normal / AAA large |
| state triad dark — ok / warn / error | 9.91 / 9.80 / 7.85 | AAA |
| state triad light — ok / warn / error | 5.40 / 6.56 / 5.40 | AA normal |
| `--hs-unknown-500` (the honest UNKNOWN) dark / light | 8.29 / 6.04 | AAA / AA normal |

**Two findings, neither invented:**

1. **The 07-22 colour section is superseded by shipped code.** Its proposed light-mode fixes (`#23708A`, `#7E621F`, `#A34A4A`, `#35715E`) were never needed as authored — the shipped file already implements a mode-paired system with different, passing values. **B-1 should not re-open colour.** Fold exploration §3 as SUPERSEDED-BY-SHIPPED; keep §3a's all-users mandate, still binding and still unexecuted on the CVD half.
2. **One 0.03 shortfall.** `--hs-accent-500` serves as `--hs-link` and `--hs-focus-ring` in light mode; on `--hs-bg` (not `--hs-surface`) that is 4.47:1 against a 4.5:1 floor — fine as a UI component and as large text, short for a normal-size link sitting on the page background. **Consequence for B-1: any coloured element of the mark on light uses `--hs-accent-600` (6.38:1), never `-500`.** Whether a live normal-size link actually renders on `--hs-bg` is an FE-lane check, not a claim made here.

Large-text relief applies to the wordmark: SC 1.4.3 requires **4.5:1 normal, 3:1 large**, large = "at least 18 point or 14 point bold" (≈24 px, ≈18.5 px bold) — W3C, fetched 2026-08-22. A favicon is not text and is governed by SC 1.4.11's 3:1 non-text floor.

---

## §2 B-7 · The JP/katakana variant study

### 2.1 The record's honest state — read this first

**The JP checker produced no written katakana.** The paste carries her renderings only as prose — *"If you pronounce it in katakana though, the Harry Potter-ness goes down quite a bit"* — plus the operator's note, *"Her opinion was that VERDOMO was the most natural sounding for katakana,"* plus an **mp3 that is not in the results directory** (the bank's provenance line calls it "an operator-held exhibit"). The audit bar asks for the checker's own rendering beside each reading. **It does not exist in the record.** Everything in §2.2 is therefore *this lane's* transliteration under standard conventions, labelled as such; **the checker's audio is the instrument that would confirm it** — a five-minute listen Nick can run without spending anything or telling anyone.

### 2.2 The candidate forms

| Latin | Katakana | Romaji | Morae | Default reading | Note |
|---|---|---|---|---|---|
| **ZENDOMO** | **ゼンドモ** | *zendomo* | 4 (ゼ・ン・ド・モ) | The default: direct mora-for-mora mapping; the moraic ン is the only non-CV unit | **Recommended as the mark of record** |
| ZENDOMO | ゼンドーモ | *zendōmo* | 5 | Likely enough to own defensively — Japanese readers routinely lengthen a stressed penultimate in Latin loans, and the source stresses -DO- in 5/6 markets (§1.1) | The defensive variant |
| **VERDOMO** | **ベルドモ** | *berudomo* | 4 | The conventional rendering: Japanese has no /v/ phoneme; バ行 is the standard substitution | The hedge's mark of record |
| VERDOMO | ヴェルドモ | *verudomo* | 4 (5 kana) | The faithful transcription using ヴ | The defensive variant |

**Why the checker's "most natural in katakana" verdict lands on VERDOMO, and it is not a fluke:** ベルドモ is **entirely open-syllable** — four clean CV morae, the most native-legal shape a foreign word can have. ゼンドモ carries one moraic ン. Both are comfortable; ベルドモ is smoother by construction. It is the one axis on which the hedge genuinely beats the primary.

### 2.3 Near-word / homophone check (dictionary-sourced; all fetched 2026-08-22)

| Element | What it lands on (JMdict via Jisho) | Reading |
|---|---|---|
| **ゼン** | **禅** "Zen Buddhism; dhyana (profound meditation)" (common, N1) · **全** "all; whole; entire; complete" (common) · **善** "good; goodness; virtue" (common) · **前** "previous; former; before" (common) | **Unusually good** — three of the four common ぜん words are *meditation*, *whole/complete*, *good*. The checker's own read ("the word zen comes to mind, that's pretty much it") is the field confirmation. |
| **どうも** | adverb: "thanks · very (sorry) · quite; really · somehow · hello/goodbye" — **common, JLPT N5** | Benign-to-warm, and the most everyday politeness word in the language. It attaches to the **long-vowel** ゼンドーモ, not the short ゼンドモ — an argument for owning ゼンドーモ defensively rather than adopting it. |
| **ども** (suffix) | The humble/plural personal suffix (私ども) and 子供 *kodomo*, "child" | Benign; softening/humble register. |
| **どもる** 吃る | "to stammer; to stutter" — godan intransitive, usually written in kana | **The one item worth naming.** A *verb stem*, not a homophone: ゼンドモ ≠ どもる, and the shared string is only ドモ, non-initial. **The field tested for exactly this and did not find it** — "I cannot come up with anything that sounds similar to the 3 words that are rude/inappropriate… 100% no problems… even in front of children," 5/5. Recorded as a desk-layer item the field cleared, routed to the JP-wave counsel as an FYI, not a flag. |
| **ヴェルドモ vs ヴォルデモート** | Voldemort renders ヴォルデモート *Vorudemōto* — 6 morae, different second-mora vowel, a moraic ー in the fourth | Corroborates the checker exactly: the kana forms are plainly distinct. |

### 2.4 Wordmark consequence (does the katakana set at the same visual weight as the Latin mark?)

| Direction | ゼンドモ beside the Latin mark | Verdict |
|---|---|---|
| **A — Anchored Onset** | **Breaks.** ゼン is two kana against three Latin letters; a weight or colour step on two of four kana reads as an error, not a system. Japanese gothic faces also carry far less weight range than a Latin variable grotesk. | Poor fit |
| **B — Domo Anchor** | **Works cleanly.** The tail rule maps to ドモ with no redraw; the one-cut-glyph logic maps to ゼ. Kana sit on a square em body, so a rule under the last two kana is *more* natural than under Latin. | **Best fit** |
| **C — Quiet Infrastructure** | Works by definition — set the kana in the companion face at matched optical weight and stop. | Fine |

**The companion face** — both verified **SIL Open Font License 1.1** at the source repo, fetched 2026-08-22:
**Noto Sans CJK / Noto Sans JP** (licence file read at `notofonts/noto-cjk/Sans/LICENSE`) — the safe default, broadest coverage, the reference CJK face. **Zen Kaku Gothic New** (Yoshimichi Ohira, `googlefonts/zen-kakugothic`) — a basic Japanese gothic with a gentler, less mechanical skeleton. *Design observation, no legal content: the family is literally named **Zen**.* For a mark named ZENDOMO that is either a small gift or a small nuisance — it collides in every search for "zendomo font."
**Coverage caveat, stated because it was not verified:** neither repo page enumerates its kana/kanji/Latin coverage. Confirm before either is specced.
**Cost note the local-first rule forces:** a full JP face is megabytes and INV-LF-01 forbids a CDN — but the katakana mark needs **four to five glyphs**, and the dashboard already ships a documented, reproducible `pyftsubset` recipe (`src/styles/fonts/README.md`). A ゼンドモ subset is **well under 5 KB** — a rounding error against the 25 KB Inter subset already in the image.

### 2.5 What the filing wave needs (and where this stops)

The JP-first wave is naming-package §6 step 7 — direct-national, JP first, inside the ~6-month Paris window (≈ H1-2027 on a ~September US filing). Two facts from the JPO's own Article 5 examination guideline (Part IV, fetched 2026-08-22) bear on what the design must hand counsel:

1. **Standard characters permit mixed scripts** — "Chinese characters, kana, alphabetic characters, etc. can be used in combination," within a 30-character limit counting spaces.
2. **Standard characters forbid the lockup** — a mark loses standard-character status if it uses different font styles, differing point sizes, colouring, **or vertical writing or multi-row composition**.

**The design consequence, which is all this lane may say:** a Latin-over-katakana *stacked* lockup — the natural visual form — **cannot be a standard-character mark**. The available shapes are (a) two separate standard-character applications, `ZENDOMO` and `ゼンドモ`; (b) one standard-character application on a single line, `ZENDOMO ゼンドモ`; or (c) a stylised design-mark application carrying the stacked lockup, which then protects the *styling* as much as the word. **Which of those to file, in which classes, and in what order is counsel's answer, not this lane's.** The note to carry into the wave: **the katakana is a mark decision, not a translation decision**, and it belongs on the table at the same sitting as the US filing so the Paris window is not spent discovering it. Japan is **first-to-file** (JPO, Outline of the Trademark System, fetched 2026-08-22), which is the whole reason the wave is JP-first.

---

## §3 B-2 · The voice/tone §-fold (paste-ready — drop into `2026-07-22_voice-tone-messaging_platform.md`)

> ### §1a — What the field record confirms, and the one thing it corrects (fold of 2026-08-19; n=6, anecdotal)
>
> **Confirmed: the calm register is not a preference, it is an observation.** Across six markets, one checker each, the intended register fired **unprompted in all six** — *"calm, peace, nature, birds… clean, serene and high-end"* (FR) · *"Zen, calmness"* (DE) · *"calm, relaxation, peace"* (ES) · *"meditation and mindfulness"* (IT) · *"meditation"* (NL) · *"the word zen comes to mind, that's pretty much it"* (JP). Register B — Calm Neighbour — is the register the name itself already sets, so copy that raises the temperature now works against the product's own name, not merely against a style guide. Zero curse-adjacency and zero hesitation-to-say-aloud, in any market.
>
> **Confirmed: the home reading arrives without help.** *-domo* was read as *domotique* / *"Domo: home, home automation"* / *"we mainly relate it to home"* unprompted in all three Romance markets. Copy never has to explain that this is a home product. It should stop trying.
>
> **Corrected: calm is also the risk.** One market's unprompted first-three-things were *"meditation, **air freshener, fresh breath**."* Nothing rude, and it still scored 5/5 — but it is a **category drift**, and it is the one thing the name cannot correct on its own: at maximum calm the product reads as a household consumable rather than as infrastructure. **The correction is a rule, not a rewrite:** every calm sentence must be load-bearing. Calm delivered as *reticence about a hard fact* reads as infrastructure; calm delivered as *atmosphere* reads as air freshener. Nothing in §1–§7 changes; §2's Register-B definition gains one line — **"unhurried, context before detail, warm without casual" now also means: never atmospheric. If a calm sentence carries no fact, cut it.**
>
> **Two exhibits (both Register C, both fenced-clean per the claim register).**
>
> - **Exhibit 1 — the honest unknown, as reticence rather than atmosphere.** ✓ *"Sent. The lock hasn't reported back yet."* ✗ *"Everything's calm — we'll let you know when your lock checks in."* The first is calm because it withholds a claim it cannot make. The second is calm because it is decorating.
> - **Exhibit 2 — the non-firing answer, in the field's own register.** ✓ *"It didn't run. The porch light was already on at 18:04, so the condition was false."* ✗ *"No need to worry — nothing needed to happen here!"* Same tone of voice, opposite amount of information.
>
> **Unchanged by this fold:** the message hierarchy and its ruled order · the §6 claim rails verbatim · the T-1/T-3/T-4 live set and the T-2/T-5 strike · every capability sentence's fence (the register at `context/audits/2026-08-22_BRAND-SPRINT-1_return.md` §5). The tomorrow register stays SUPERSEDED-PENDING; **the field is now the strongest available argument for the calm/home axis** at the Q-B ruling — this fold is the evidence, not the ruling.

---

## §4 B-3 · The website brand-integration map (pointers; nothing edited)

Instruments run read-only exactly as spelled in runbook §2: `git -C homesynapse-core-docs grep -li "homesynapse" -- "website"` → **20 files**, then line-resolved and classified.

| # | Surface | file:line | Class | B-1 restyles? |
|---|---|---|---|---|
| 1 | **The product-name token** — the site's single source of truth | `website/site/src/lib/brand.mjs:14` | **IN — the one-line flip** | — |
| 2 | The company token (`NexSys`) | `brand.mjs:16` | **OUT — the parent is not renaming** (Architecture C: the parent stays quiet) | — |
| 3 | Page `<title>`, header wordmark, footer attribution | `Base.astro:19`, `:50`, `:65` | **OUT of the rename — already tokenized**; all three render from row 1 | **Yes** — `:50` is the wordmark's live home |
| 4 | Canon page copy (index + 5 dossiers) | `{{productName}}`/`{{companyName}}`, substituted at build by `plugins/remark-brand.mjs`; 8 placeholders across 6 lines of `index.md`, **zero literal-name hits there** | **OUT — already tokenized** | No |
| 5 | Literal working-name hits in `website/pages/*.md` (5 files) | all inside `<!-- … -->` provenance blocks — e.g. `ledger-gap-dossier.md:20–38`, `no-cloud-account.md:18–33` | **OUT — stripped at build** by `plugins/remark-strip-comments.mjs`; they never reach HTML | No |
| 6 | **manifest · og/meta · favicon · apple-touch · 404** | **absent.** No `public/` directory; grep for `og:`/`favicon`/`manifest`/`apple-touch`/`404` across `website/site` returns **zero**; `src/pages/` holds exactly `index.astro` and `[...slug].astro` | **NEITHER — these are NEW assets at the word, not renames** | **Yes — this is B-1's real website deliverable.** Independently corroborated on the other surface: the FE lane's census (`2026-08-22_FE-SWAP-CENSUS_return.md` §3, §4e-7) found the same void in `homesynapse-core` — "no manifest, no PWA, no favicon, no `og:`/`apple-` meta, no 404/offline page." **The two halves converge: the favicon is a single greenfield deliverable serving both surfaces, and per that return's §4e-7 rider it should ship post-flip or already carry the ruled name.** |
| 7 | `<meta name="robots" content="noindex">` | `Base.astro:30` | **OUT — but a gate**: the site is deliberately unindexed pre-publish (W-2/W-5) and must stay noindex through the swap | No |
| 8 | `theme-color` and the stored theme key `hs-theme` | `Base.astro:38`, `ThemeToggle.astro:16` | **OUT — a lawful technical identifier.** Renaming it silently discards every visitor's stored theme choice for no user value | No |
| 9 | Repo-path references (build config, guards, style provenance) | `astro.config.mjs:15` · `check-shared-sources.mjs:11,25,26,27` · `styles/site.css:4` · `site/README.md:35` | **OUT — lawful technical identifiers** | No |
| 10 | Design-system canon — **9 files, 118 matching lines** (voice-and-tone 46 · visual-design 17 · content-types 14 · documentation-style-guide 14 · website-design-vision 14 · typography 6 · README 2 · 2 research files 5) | e.g. `visual-design-reference.md:204` "HomeSynapse Blue `#3FA6C9`" | **DEFER — not a rendered surface** (the collection loads only `index.md` + `pages/*.md`, `content.config.ts:8`); all DRAFT-pending-reconciliation | Indirectly: **the name-bearing colour token names die here** — and `#3FA6C9` is not the shipped accent (`#1577be`), so the canon is stale on the hex too |

**The finding.** Runbook §1 budgets the marketing site as *"~20 files carry the working name — a website-lane pass: copy + config + manifest."* At the bytes, the rendered site's working-name surface is **one value**, `brand.mjs:14`; the other 19 files are internal canon, stripped comments, or repo paths. **The website half of the swap is a one-line flip plus a build**, exactly like the dashboard half — and the H+6–12 budget is better spent on **row 6**, the assets that do not exist yet. Suggested runbook fold (hub's call, not this lane's edit): re-word §1's website row from *"~20 files"* to *"one token + the never-yet-authored icon/og/manifest set,"* and move the design canon to its own post-reconciliation row.

---

## §5 B-5 · The claim-fence register (no prose; the instrument the post-R-4 kit is written against)

| # | The sentence the story will want | Its fence today, and the carrier | What lifts it | The honest sentence available NOW (layered: what is MISSING) |
|---|---|---|---|---|
| 1 | "The packaged artifact runs integrations." | **D-1 DO-NOT-SAY, verbatim on every surface** — carrier: the D-1 pair, standing per the v56 §fences and `PROJECT_SNAPSHOT.md:21` | R-4's audited return on disk (H9) → **into the positive-scope register** | "The integration runs on the bench from source. Whether the *packaged* artifact does is a question we are answering with a hardware re-rep, not an assertion." |
| 2 | "The packaged artifact publishes events." | **D-1 DO-NOT-SAY, verbatim** — same carrier | R-4's return, then the positive-scope form pre-authored in the R-3 skeleton: *"verified on real hardware at commit ⟨SHA⟩ … the re-rep record at context/audits/…"* | "Events are published in the running system. The packaged path's own evidence is being produced." |
| 3 | "The image build is deterministic and self-checksumming." | **DO-NOT-SAY until W2-3** — carrier: `distribution/README.md:117`, verbatim in-file (ruled D-1 PROCEDURAL+FENCE) | **W2-3's post-gate re-verification.** Note R-4 does **not** lift this one | "The build pins its JDK and tool versions. Whether that yields byte-reproducibility is a claim we re-verify post-gate before we make it." |
| 4 | "The event model reserves the seams for agents as a first-class subject type." | **Never quoted externally without the DESIGNED-FOR flag** — carrier: the north-star frontmatter's verified-at-filing note ("DESIGNED-FOR, not TRUE-TODAY — no agent SubjectRef type; no proposal/adjudication event types") | **AGENT-SEAMS landing** (post-gate) | "The architecture is designed for it, and the governance half exists (Doc 17 Locked, AIOT-INV-1 §50). The agent subject type and the proposal/adjudication events do not exist yet." |
| 5 | "Proven in CI." | **The H9 instrument register** — CI green is not hardware truth; carrier: the H3 return §9.3 exhibit, *CI green on the broken artifact all along* | Nothing lifts it — it is **replaced**, always, by naming the instrument | "Green in CI at commit ⟨SHA⟩" *or* "verified on real hardware at commit ⟨SHA⟩" — never the unqualified word "proven." |
| 6 | "It confirms that the device actually did it." | **SAY FREELY** (platform §6 rail), bounded by row 7 | — | Ships as-is; the live site already models it (`ledger-gap-dossier.md:7`). |
| 7 | "The command was delivered." | **Any delivery-proof claim is fenced** — carrier: platform §6, folded 2026-08-06 per the REV-1 audit + Nick's R-A ruling (DISPATCHED = hand-off to the radio; CONFIRMED = STATE-truth; the record cannot distinguish delivered from never-delivered) | **The chartered delivery-evidence closure (S-1 / candidate-(iii)) shipping** | "We record that the command was dispatched, and whether the device's own report evidenced the commanded state. What we cannot yet show you is the radio layer in between — so we do not claim it." |
| 8 | "The only / the first / unique / patented…" | **Pre-counsel rail, platform §6** | Counsel, per claim | The live template, already shipped: *"To our knowledge, no other platform in the category maintains this record"* — `ledger-gap-dossier.md:12`. |
| 9 | "Competitors' traces vanish on restart." | **Corrected baseline — never say** (HA persists traces to disk; the real limits are the trace cap and the absent never-triggered trace) | Nothing; it is false as stated | "Home Assistant keeps a capped number of stored traces and does not record a trace for an automation that never triggered. Ours is a projection of a complete log, so the run you need is always reconstructable." |
| 10 | "Plug-and-play." | **W-4 embargo** until the install story is ruled | The install-story ruling | Describe the actual install steps. |
| 11 | The enforcement position (deterministic floor vs model judgment). | **The D5 language law** — carrier: `Substrate_Thesis_v0.md` frontmatter + §3.1, *"The claim is not that L1 beats L2 — that would be wrong, and it's the failure mode to avoid when this thesis gets restated by others"* | **Nothing lifts it.** The layered form is the permanent form | "A probabilistic filter with no categorical floor beneath it provides no guarantee, only a lowered error rate. The floor is **missing from the field** — not superior to what the field ships." |
| 12 | Anything a future paid or cloud tier would have to retract. | **The Connect-proof rule** (platform §6) | — | Say only what survives a paid tier existing. |

---

## §6 Sources, harvest, and what could not be done read-only

### 6.1 External sources — every one primary; all fetched 2026-08-22

| Source | What it grounds |
|---|---|
| rsms.me/inter · github.com/rsms/inter | Inter — SIL Open Font License 1.1; Rasmus Andersson (DBA RSMS); variable font |
| github.com/Omnibus-Type/Archivo | Archivo — SIL OFL 1.1 (`OFL.txt`); Héctor Gatti; **weight + width** axes |
| github.com/floriankarsten/space-grotesk | Space Grotesk — SIL OFL 1.1; Florian Karsten, 2018; derived from Colophon's Space Mono |
| github.com/googlefonts/zen-kakugothic | Zen Kaku Gothic New — SIL OFL 1.1 (`OFL.txt`); Yoshimichi Ohira |
| github.com/notofonts/noto-cjk/blob/main/Sans/LICENSE | Noto Sans CJK — SIL Open Font License, Version 1.1 (26 February 2007) |
| jetbrains.com/lp/mono | JetBrains Mono — SIL OFL 1.1, "free of charge, for both commercial and non-commercial purposes" |
| w3.org/WAI/WCAG22/Understanding/contrast-minimum.html | SC 1.4.3 — 4.5:1 normal, 3:1 large; large = ≥18 pt or 14 pt bold (≈24 px / ≈18.5 px bold) |
| jpo.go.jp/e/system/laws/rule/guideline/trademark/kijun/document/index/0400.pdf | JPO Examination Guidelines Part IV, Art. 5 — standard characters: mixed scripts permitted, ≤30 characters; **disqualified by differing sizes, colouring, or vertical/multi-row composition** |
| jpo.go.jp/e/system/trademark/gaiyo/chizai08.html | JPO Outline of the Trademark System — registrable subject matter; **first-to-file** |
| jisho.org/search/どうも · /どもる · /ぜん | JMdict: どうも (common, N5) · どもる 吃る ("to stammer; to stutter") · 禅 / 全 / 善 / 前 (all common) |

**Internal sources** are cited inline by `file:line` throughout §§1–5 and were read at the bytes this session — load-bearing: the results bank + all six raw deliverables beside it, `2026-07-22_identity-system_exploration.md`, `2026-07-22_voice-tone-messaging_platform.md`, `2026-07-23_domain-handle-claims-refresh.md`, naming-package §6, the G-2 swap runbook, the G-2 readiness brief, `2026-06-12_website-brand-deliberation_draft-rulings.md`, `Substrate_Thesis_v0.md` §3.1/§5/§9, the north-star frontmatter, `distribution/README.md:117`, and the shipped `tokens.css` / `fonts.css` / `brand.mjs` / `Base.astro`.

### 6.2 Harvest (5)

1. **F-B1 — the NL category drift.** *"meditation, air freshener, fresh breath"* — unprompted, at 5/5, and **unadjudicated in the bank**. The one market that stresses the ZEN- onset is the one that read the name as a household consumable. Re-briefs the identity (§1.1) and adds a rule to Register B (§3).
2. **F-B3/F-B4 — the onset premise is out of phase.** The Z→S drift is phonemic in 1 of 6 markets and orthographic in 1 more; **five of six put the tonic on -DO-**. The charter's onset device survives only as a letterform; the bank's F-N4 should be folded to say so.
3. **The 07-22 colour section is superseded by shipped code.** It computes against `#3FA6C9`/`#ECEFF3` (DRAFT canon); the shipped accent is `#1577be` in a mode-paired system that passes AA. B-1 should not re-open colour — and `visual-design-reference.md:204` is stale on the hex.
4. **One 0.03 accessibility shortfall, and one absent asset class.** `--hs-accent-500` on `--hs-bg` in light mode is 4.47:1 against a 4.5:1 floor while serving as `--hs-link`/`--hs-focus-ring`; and **no favicon, manifest, og-image or 404 exists on either surface** — independently found by both halves of the census (this lane on the website; the FE lane on `homesynapse-core`, `2026-08-22_FE-SWAP-CENSUS_return.md` §3). The browser-tab identity is greenfield, not a rename, and it is one deliverable for two surfaces.
5. **The ES Digimon morphology note** (ES doc, ZENDOMO cell): *"All three names can sound like Digimon names in Spanish simply by adding an 'n' at the end… and placing the stress on the last syllable."* Benign and unadjudicated; it prices one future decision — never mint an *-ón*-suffixed variant or a mascot in Spanish-language markets.

### 6.3 Fence compliance (each one checkable)

Nothing public. No candidate name entered any external form: no WHOIS, no registrar, no marketplace, no social-handle probe, **and no trademark-office search** — the two JPO pages read are the *procedural* guideline on standard characters and the general system outline; neither takes a query, neither was given a name, and neither creates a record. No repo was edited: this file is the only write, and it is a new file. No vendor or foundry was contacted; every licence claim came from the foundry's own page or its source repository. The D-1 pair appears in this document only inside §5, quoted as fenced, never asserted. The working name stays everywhere it is today.

### 6.4 What could not be done read-only (hand these to the word)

1. **The 16-px and 0.5-cm legibility tests need a rendered build** — the FE lane's job at the word. What arithmetic alone gives: at a 16-px tab a 7-letter wordmark yields ~2.3 px per glyph and **is not a candidate** — the favicon must be a device or monogram, and none exists on either surface today (§4 row 6). At 5 mm on a device label the wordmark is comfortable (~40 px tall at 203 dpi, ~59 px at 300 dpi), so the label is a wordmark surface and the tab is not.
2. **The JP audio was not listened to.** The mp3 is operator-held and absent from the results directory. The bank says its absence blocks nothing, and it does not block this study — but it is the **only instrument that would confirm §2.2 against the checker's own mouth**, at the cost of a five-minute listen.
3. **The companion JP face's coverage was not verified** (kana/kanji/Latin sets for Noto Sans JP and Zen Kaku Gothic New) — the repo pages do not enumerate it. Confirm before either is specced.
4. **CVD simulation** (deuteranopia/protanopia/tritanopia) of the shipped state triad — mandated by the all-users colour mandate §3a-2, still unexecuted, and it needs a rendering tool this lane did not have.
5. **No letterforms were drawn.** §1.3 is a schematic in a fallback stack, not a cut. Direction B's glyph work is the charter, and the ~10–16 h estimate is this lane's, not a quote.

### 6.5 Pushback, stated plainly

Two, both invited. **First**, the F-N4 premise governing B-1's charter does not survive the raw field files: anchoring the ZEN- onset to fight the drift fixes nothing in the one market where the drift is real (ES has no /z/ phoneme; typography cannot supply one), is unnecessary in four, and is out of phase with the tonic in five. The device is worth keeping for *distinctiveness*; it is not worth keeping for the reason the board gave. **Second**, no direction here needs a paid asset — and that is a finding, not a convenience: Inter is already in the image at 25 KB, Archivo and Space Grotesk are OFL, and the recommended direction draws **one glyph**. If a paid face were genuinely required to make the mark honest, the price would be named here instead. What *is* required, and is not free, is time: Direction B is ~10–16 hours of real letterform work by someone who can draw, and pretending otherwise is the only way this recommendation goes wrong.
