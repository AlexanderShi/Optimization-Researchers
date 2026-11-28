# Matteo Fischetti · Evidence ledger

## Contents

- [How to Use, front matter and disclaimer](#how-to-use) · [Taste: marks](#taste-marks) · [Taste: warning signs](#taste-warnings)
- [Method 1](#method-1) · [Method 2](#method-2) · [Method 3](#method-3) · [Method 4](#method-4) · [Method 5](#method-5) · [Method 6](#method-6)
- [Stage workflows and the Routing row](#workflows)
- Heuristics: [1](#heuristic-1) · [2](#heuristic-2) · [3](#heuristic-3) · [4](#heuristic-4) · [5](#heuristic-5) · [6](#heuristic-6) · [7](#heuristic-7) · [8](#heuristic-8) · [9](#heuristic-9) · [10](#heuristic-10) · [11](#heuristic-11) · [12](#heuristic-12)
- [Common misreadings](#misreadings)
- Anatomies: [Benders redesign](#anatomy-benders) · [local branching](#anatomy-local-branching) · [feasibility pump](#anatomy-pump) · [erraticism](#anatomy-erraticism) · [Gomory revisited](#anatomy-gomory)
- [Anti-patterns](#anti-patterns) · [Trajectory, Latest and Lineage](#trajectory) · [Inner tensions](#inner-tensions) · [Mentor voice](#mentor-voice) · [Roundtable Card](#roundtable-card)
- [Honest Boundary](#honest-boundary) · [Corrections](#corrections) · [Promotions and the candidate pool](#promotions) · [Rejected updates](#rejected) · [Held back under the holdout rule](#held-back) · [Sources appendix](#sources) · [Card key](#card-key)

> Date: 2026-11-28 (stage T3.6, team-synthesize). The full evidence behind `../../SKILL.md`. SKILL.md keeps, per item, the strongest statement and cards, a one-line say–do count, at most four variant or correction bullets and a pointer to the matching section here. Each section has up to four parts: **Full-text evidence** (copied word for word from [08-deep-reading-synthesis.md](08-deep-reading-synthesis.md), which is traceable to the cards, with its headings set in bold; or, where 08 has nothing, taken from the named cards), **Counts**, **Added in T3.6** (what this pass wrote into SKILL.md, with card ids) and **Before T3.6 (moved verbatim)** (the SKILL.md item as it stood on 2026-11-14, built from web research, 46 talk decks and the notes 01–06 without full-text reading; kept in fenced blocks, word for word, so nothing is lost). Copied 08 text is left as copied; 08 itself is edited only for links and counts.
>
> **How to read.** `[S011 p. 12]` is paper card S011 at the `[[page N]]` page of the file the card read, the file listed for that ID in [../sources/papers/INDEX.md](../sources/papers/INDEX.md); most files are author preprints, technical reports, manuscripts or arXiv versions, and each card's Read line names the version (column *Version read* of the [card key](#card-key)). Abstract- and metadata-level cards are cited by ID only. Deck keys (EURO12 PDF p.23, CORS15 PDF p.13) are PDF pages of his talk decks, and note pointers (01 SW2, 02 R7, 03 PE-13, 05 Q4, 06 §2.3) are items of the research notes 01–06; both come from the pre-synthesis research. Marks: ✅ evidence · ⚠ variant (kept, nothing deleted) · ✗ contradiction or correction. PD, DM, EP and WM ids are entries of [../technique-catalog.md](../technique-catalog.md). Quotation marks enclose only text copied from a card that copied it verbatim from the text (`verify_card_quotes.py`, 2026-11-28: 358 quotes, 358 exact; every quotation added in T3.6 was re-found in a card and in its text file on 2026-11-28) or, where a deck key follows and in the *Before* blocks, text the pre-synthesis SKILL.md quoted from his decks and the notes. Wording of SKILL.md itself is set in italics.
>
> **Voices.** Full texts in his own voice are few: S109 (2016) and the 2026 notes S161, S163 and S164; S190 and S194 are his talk decks on joint work. S161 states that the idea and the supervision are his and that everything else was done by an AI assistant [S161 p. 4], so its design choices are evidence of what he accepted, not of what he designed. Every other text is co-signed and its "we" cannot be split; several author lists are alphabetical [S040; S059; S097]. Martina Fischetti, a separate researcher, is first author of S154, S100, S143, S150 and S162 and of the abstract-level S131, D016, S103 and S051, and second author of S078; some reference lists write both as "Fischetti, M.", and nothing from such a list is attributed to him. S188 and S192 are theses he supervised, not his writing.
>
> 08 header, copied: **Counting.** One study per pair. From the operator's list: S072 = S073; S057 = S125; S195 (report) = S011; D018 = S110; S033 = D003; S058 = S139; S112 = S024 (probably, not verified); S066 = S004 (IPCO 1996); D001 = S107 (IPCO 1993); S184 = H002 (ISMP 1994 talk abstract); H006, a 2009 draft, may be an early version of S045 (not verified); S178 and D005 are his two parts of the ATMOS 2008 volume S176 (Role skip). From the cards: conference and journal pairs S091 = S006, D002 = S118, D006 = S074, D008 = S095, D010 = S063, D015 = S027, D013 = S097, D004 = S018, S087 = S014, S170 = S052, S054 = S008 (per the work list, the preliminary version); D016 and S051, two editions of one handbook chapter (inferred on the card); talks of a paper S190 → S079 and S194 → S016; one-line-of-work pairs S137 and D019, D007 and S042, S198 and S046, S172 and S144, S186 and S143, S187 and S150; S154 restates S052 in its §§2–3 [S154 p. 2] and is counted with S052 wherever a method's count is at stake (separately for coauthors). The round-2 cards in c2-01 supersede the round-1 cards of S012, S017 and S003; the s2-01 card of H003 supersedes its unreadable s01 card. S188 and S192 are theses he supervised, not his writing, and give no method evidence.
>
> **Not carried.** The cards' reading notes on inconsistencies inside a work (a table that disagrees with its text, a typo, numbers that look carried over) are not findings about the researcher or his coauthors and are not used here. Material that `holdout.md` seals is not used: no point, quote or decision of a sealed item appears in this file, also where another card states the same point, and two candidates that lean on sealed material are withheld ([Held back](#held-back)). The script-generated card index `07-paper-cards.md` and the card batch files under `cards/` state sealed points: this ledger does not link them, and they are not to be opened while using or testing the skill.
>
> **Scope and counts.** One section per SKILL.md item this pass changed, plus the corrections, the promotion record, the rejected updates, the sources and the card key. Answer Standard, Research Integrity Rules, Agentic Protocol, Taste quick-check and the rest of Activation Rules are unchanged in SKILL.md (Activation Rules changed only in its disclaimer line; Research Task Routing in one row). Coverage: `team_status.py --coverage` on 2026-11-28 (198 Scholar rows · 202 distinct works indexed · 132 open full texts · 130 read in full · 1 in part · 56 abstract only · 11 metadata only incl. unreadable · 4 skipped · 0 book material · 358 quotes verified). Word budget after this pass: 11654 words by `answer_standard.py --words` (target about 11500, hard limit 13000). (Note added in the T3.7 review: the committed T3.6 SKILL.md, review fixes included, counts 11908 words by the same script, the count T3.7 starts from.)
>
> **T3.7 (tightening, 2026-11-28).** SKILL.md was brought under its word budget by moving evidence here, not by deleting it: wherever a SKILL.md line was shortened, the line as it stood before is kept word for word, in a fenced block, under **Before T3.7 (moved verbatim)** at the end of the matching section. Sections with such a block: [taste marks](#taste-marks), Methods [1](#method-1) (also the Core Research Methods intro), [2](#method-2), [3](#method-3), [4](#method-4), [5](#method-5) and [6](#method-6), the [stage workflows](#workflows), Heuristics [1](#heuristic-1), [4](#heuristic-4), [9](#heuristic-9), [11](#heuristic-11) and [12](#heuristic-12), the [misreadings](#misreadings), three anatomies ([Benders redesign](#anatomy-benders), [local branching](#anatomy-local-branching), [feasibility pump](#anatomy-pump)), the [anti-patterns](#anti-patterns), the [trajectory](#trajectory) (Latest) and the [inner tensions](#inner-tensions). What moved: Practice lines cut to the strongest three or four cards, one item each leaving Methods 2, 4, 5 and 6 (the 2000–01 precursor, which Misreading 4 keeps; the baseline set after contacts with the vendor's staff, whose card Method 4 step 2 cites; the 2026 correction of an implementation error, which the Honest Boundary and the Corrections list keep; the closure's ceiling, which Method 6 step 4 cites), and the outcome details of the two 2026 re-tests in Method 5 Practice; detail inside variant bullets (Method 1's exact-work clause, Method 2's 2026 counter-case, Method 3's backdoor-branching figures, Method 4's significance-test bullet, Method 5's wording bullet and its 2009 port of an old rule, Method 6's pre-2002 bullet), each bullet keeping its mark and card; four long quotations replaced by unquoted paraphrases or, for Pruning Moves, by its quoted phrase (Method 1 and Method 6 Practice, Heuristics 11 and 12); the provenance notes in three One lines and two steps; wording in pointers and cross-references that repeated another item (the Core Research Methods intro on note pointers, the Stage Workflows pointer, Workflow S step 2, the Workflow F checkpoint, the Benders anatomy's Kelley clause, the anti-pattern's single-run count); anatomy detail beyond about two lines a row (the Steiner entry, the full recipe's times and the April 2015 report in the Benders rows, the fat and slim mechanisms, the bound's behaviour under hard fixing, the note on trace instances not in the paper, the twelve comparisons under Holm's correction); one case each in Taste marks 3 and 4 and Heuristics 1 and 4, and a clause of Heuristic 9; the assistants' product names in Latest; the QAP model files in Tension 2. Misreading 4 was only reworded. Every step instruction and constant and every ✗/⚠ mark stays in SKILL.md; the front matter, How to Use, Activation Rules, Answer Standard, Research Integrity Rules, Research Task Routing, Agentic Protocol, Mentor Voice, the Roundtable Card and the Honest Boundary with its Corrections list are unchanged. Three placements recorded under [Corrections](#corrections) changed: 08 §3 item 12 (the in-out precursor) now stands in Misreading 4 only, not in Method 2 Practice; the full recipe's times of the review table's Benders row and the backdoor-branching figures of its Method 3 row are here only, the corrected claims (the quick shot under 15 minutes each, single runs with no measured spread) staying in SKILL.md. Where an *Added in T3.6* or *Review fix* line in this file quotes SKILL.md wording that T3.7 shortened, the section's Before T3.7 block holds that wording. Budget count: 11908 → 11464 words by `answer_standard.py --words` (target about 11500, hard limit 13000).
>
> **T3.7 review fixes (2026-11-28).** A read-only review of the T3.7 stage found seven minor points, five in SKILL.md and two in this file; all seven were applied. Restored to SKILL.md word for word from the Before T3.7 blocks, which stay as they are: in [Method 5](#method-5) Practice, the outcomes of the two 2026 re-tests (*reuse buys data but neither speed nor energy and only at large batch*; *with a null and a harmful fallback*), and in its earlier-forms bullet the 2009 port of an old rule [S041 p. 11]; the exact-work clause of the handbook-chapter bullet of [Method 1](#method-1); the fat and slim mechanisms of the [Benders redesign](#anatomy-benders) anatomy, without its duplicate key (UFL17 p.14); the bound's behaviour under hard fixing, the [local branching](#anatomy-local-branching) row as it stood before T3.7; the ISCO14 deck case of [Heuristic 1](#heuristic-1) and the reverse-order counter-case of [Heuristic 4](#heuristic-4) [S027 pp. 3–4, 20–24]. The [Method 4](#method-4) limitation on vendor tuning advice now cites the card of the Practice item that T3.7 moved here [S007 p. 6]. In this file notes were appended and nothing was deleted: to three placement records under [Corrections](#corrections) (08 §3 item 12; the Benders and Method 3 rows of the T3.6 review table) and to the T3.6 word count above. The T3.7 paragraph's list of what moved still describes the T3.7 pass itself. Budget count: 11464 → 11569 words by `answer_standard.py --words` (target about 11500, hard limit 13000).

<a id="how-to-use"></a>

## How to Use, front matter and the first-activation disclaimer

### Added in T3.6

- **Front matter**: `researched:` 2026-11-14 → 2026-11-28. The description was 979 characters; it now names the coverage (*131 of 202 indexed works read in full or in part*), drops the parenthetical keyword list of designs and the words *students' theses*, says *his way* for *the Fischetti way* and joins the two closing exclusions; the trigger phrases are unchanged.
- **Evidence format** (new paragraph of How to Use): the card citation form and the [full-text index](../sources/papers/INDEX.md), the deck keys and note pointers, the [technique catalog](../technique-catalog.md) and the [card key](#card-key).
- **Review fix**: the Evidence format names the 2026-11-14 paper keys as cards (UFL17 = S011, BIL20 = S079, MBP26 = S163, FPC26 = S164; [card key](#card-key), column *Pre-synthesis key*) and says that *paper cards* in the Answer Standard means the ledger, the catalog and the cited pages, since the card files hold sealed points.
- **Disclaimer line** (Activation Rules, the only line changed there): the quoted disclaimer is unchanged; added *The record behind it (2026-11-28): of 202 indexed works, 130 read in full and 1 in part, 56 from abstracts and 11 from metadata only, 4 skipped; mostly author preprints, not journal printings.* The line had no wording about unread full texts to replace; the coverage numbers are this member's `team_status.py --coverage` row.
- **Not changed**: the roundtable line of Activation Rules (*skip the disclaimer*) and the rule *Never credit 2002-2019 work with the 2026 apparatus (pre-registration, Holm correction, pinned commits, revalidation of every solution)*. The full texts do not contradict the latter: FP 2.0's confidence intervals, Cochran Q and McNemar tests of 2009 [S041 pp. 15, 17, 20] are not part of the apparatus it lists ([Corrections](#corrections), item 1).

### Before T3.6 (moved verbatim)

Front matter (2026-11-14):

```yaml
---
name: matteo-fischetti
description: |
  Matteo Fischetti's research craft in MILP solver engineering, distilled from his papers, 46 talk decks, code, students' theses and critics' papers (every method before 2026 is co-authored). Use it to design or review primal heuristics, Benders and cut loops, models and computational comparisons the Fischetti way: ask the stock solver first and MIP the critical sub-decision, thin the model out, blame the loop before the component, trust a gain only after seeds and a placebo arm, keep comparisons blind to whose method is whose, re-test old claims. Triggers: "Fischetti lens", "ask Fischetti", "how would Fischetti approach this", "what would Fischetti say about our heuristic", "Fischetti.skill", "用 Fischetti 的视角", or his designs applied to the user's own work (feasibility pump, local branching, proximity search, in-out stabilisation, bet-and-run). Also loaded by milp-roundtable. Not Martina Fischetti. Not for textbook explanations of these methods or general questions.
type: research-craft
researched: 2026-11-14
---
```

Activation Rules, disclaimer line (2026-11-14):

```markdown
- Say once, on first activation: "The following is distilled from Fischetti's public work, not Fischetti's own advice." Do not repeat it. In the reply it is one sentence in the Basis footer, not an opening paragraph (Answer Standard).
```

<a id="taste-marks"></a>

## Research Taste: marks of good research

### Full-text evidence (08 §2.7 and §3, copied)

- **Taste marks.** Mark 1 (a hard open instance falls on ordinary hardware): the open UFL instances 2500-10 and 3000-100 in 824.76 s and 225.25 s [S195 pp. 21–22]; QAP esc128 in seconds and three hard esc instances in under half an hour "on a single quad-core PC" with 8 threads [S067 pp. 2, 10] (§3, item 6). Mark 3 (modest claims, losses printed): [S063 pp. 1, 8–10; S164 pp. 14–20]; variant: losses printed in the tables rather than discussed in the text [S074 pp. 13, 18, 25]. Mark 4 (an unfashionable classical method redone): Benders for UFL as forgotten folklore [S195 pp. 2, 6].

| # | Skill claim (section) | Full texts | Change |
|---|---|---|---|
| 6 | Research Taste mark 1: QAPLIB esc instances *in minutes on a notebook* (CORS15 deck) | The paper reports "a single quad-core PC" with 8 threads; esc128 in seconds, the three hard esc instances in under half an hour [S067 pp. 2, 10] | Keep the deck quote, add the paper's hardware |

### Added in T3.6

- Mark 1: the deck's *in minutes on a notebook* kept; the paper's own runs used "a single quad-core PC" with 8 threads [S067 pp. 2, 10]; open UFL instances fell to a first plug-in separator [S011 p. 11] (the full recipe then needs 824.76 s for 2500-10 and 225.25 s for 3000-100 [S195 pp. 21–22], in the Benders anatomy; review fix: these are not the first separator's times). The pointer *01 SW3(d)* moved to the Before block.
- Mark 2: ten seeds in 2009 [S041 pp. 14–15] (with a more-than-6-of-10 success rule, Method 3).
- Mark 3: losses and the classes where a method does not pay printed [S055 pp. 8–9; S164 pp. 14–20]; sometimes only in the tables [S074 pp. 13, 18]. 08 also lists [S063 pp. 1, 8–10]; it is in the ledger only, since the backdoor-branching table is one run per instance (Method 3).
- Mark 4: Benders for UFL as folklore forgotten for 30 years [S195 pp. 2, 6]; Gomory's pure cutting-plane method, "typically not used in practice", redone on a black-box LP solver [D009 pp. 1, 3].

### Before T3.6 (moved verbatim)

```markdown
### Marks of good research
1. **A hard open instance falls to a simple device on ordinary hardware** (deepened): QAPLIB esc instances "in minutes on a notebook" (CORS15 PDF p.14); open UFLLIB instances solved by a first plug-in separator (01 SW3(d)).
2. **A gain that survives seeds, permutations and a placebo** (deepened): the 2012 redundant-cut demonstration; 5-seed reruns (BIL20 p.16).
3. **Modest claims with losses printed** (new): "SCIP qualifies as a more robust solver" against his own bilinear code (ISMP18 PDF p.16). Counter-case: the bilevel solver's claim to beat problem-specific methods ([05](references/research/05-peer-critique.md) C5).
4. **An unfashionable classical method that fits, redone with today's technology** (deepened): Benders for facility location, "not sexy nowadays as more complicated schemes are preferred #paperability?" (CORS15 PDF p.16).
```

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it, word for word in fenced blocks (links as written in SKILL.md, relative to the skill folder). The shortened lines are in SKILL.md.

*Mark 3:*

```markdown
3. **Modest claims with losses printed** (new): "SCIP qualifies as a more robust solver" against his own bilinear code (ISMP18 PDF p.16). Counter-case: the bilevel solver's claim to beat problem-specific methods ([05](references/research/05-peer-critique.md) C5). Losses and non-paying classes printed [S055 pp. 8–9; S164 pp. 14–20], sometimes only in tables [S074 pp. 13, 18].
```

*Mark 4:*

```markdown
4. **An unfashionable classical method that fits, redone with today's technology** (deepened): Benders for facility location, "not sexy nowadays as more complicated schemes are preferred #paperability?" (CORS15 PDF p.16), folklore forgotten for 30 years [S195 pp. 2, 6]; Gomory's pure cutting planes on a black-box LP solver [D009 pp. 1, 3].
```

<a id="taste-warnings"></a>

## Research Taste: warning signs of bad research

### Full-text evidence (from the cards)

- Warning 1 (a MIP model kept only to describe the problem, then an ad-hoc heuristic): the local-branching paper enters from users who leave the MIP framework for ad hoc heuristics and lose its generality [S001 p. 2]; the joint handbook chapter (with Balas) says an exact MIP solver inside a heuristic "may appear naive at first glance, but it turns out to be effective" [S145 p. 10], and that the stock solver in command mode is often all that is needed [S145 pp. 14–15].
- Warning 3 (many parameters, tuning on the test set), from 08 §2.4: separate tuning and test sets [S078 pp. 8–9; S164 p. 17]; a held-out test set fixed before any run [S162 p. 17]. Lapse, also 08 §2.4: a rule fitted on the instances it is evaluated on, 2012 [D013 pp. 6–10], still in the 2017 journal paper [S097 pp. 9–12]; portfolio members chosen on the 240 instances that score them (2025) [S126 pp. 19, 24–25]. 08 §6 holds *one monotone dial per device* in the pool (no statement in his voice among the cards).
- Warning 4 (a sophisticated component on a narrow testbed): BIL20 is the bilinear paper, card S079; its card records the vanilla arm as the recommended one [S079 pp. 13–16] and seeds used to confirm the selected wins [S079 pp. 10, 16].
- Warning 2 rests on his deck alone; no card adds to it.

### Added in T3.6

- Warning 1: [S001 p. 2]. Review fix: [S145 p. 10] is dropped from this item; that page argues that an exact solver inside a heuristic "may appear naive at first glance, but it turns out to be effective" [S145 p. 10], a Method 6 point (its section above keeps it); only S001 p. 2 says that the generality is lost.
- Warning 3: practice [S078 pp. 8–9; S164 p. 17]; lapse [D013 pp. 6–10].

### Before T3.6 (moved verbatim)

```markdown
### Warning signs of bad research
1. **A MIP model kept only to describe the problem, then an ad-hoc heuristic** (already known; EVO05 PDF p.2).
2. **An algorithm without implementation and test** (new): "Describing an Algorithm without Implementation is like stating a Theorem without Proof #just_a_computational_conjecture" (ISMP18 PDF pp.3-5).
3. **Many parameters, or tuning on the test set** (new): "The more parameters, the easier to make overtuning [→] power-of-ten effect" (EURO12 PDF p.23).
4. **A sophisticated component judged on a narrow testbed** (new): such cut classes "are not beneficial when a large and varied testbed is considered" (BIL20 p.16, joint).
```

<a id="method-1"></a>

## Method 1: Thin the model out before strengthening it

### Full-text evidence (08 §2 and §2.1, copied)

| Method | Cards E / V / C | Works E / V / C | Deep E / V / C | Deep E by period | Say–do after the full texts |
|---|---|---|---|---|---|
| M1 Thin the model out | 43 / 43 / 2 | 34 / 38 / 2 | 34 / 34 / 2 | 6 / 12 / 9 / 7 | ✅; practice older than the skill says: projection 1999–2006, fat and slim models 2007–2009 |


- **Strongest practice.**
  - Projection of auxiliary variables into cuts, a decade before the skill's 2011–2017 range: attacker flow variables replaced by capacity cuts separated by max-flow [S069 pp. 3, 5–6]; the projection named Benders [S073 pp. 3–4, 12–13; S072 pp. 3, 5; S093 pp. 4–6]; time variables and their big-M links dropped for arc variables with time windows as cuts [S028 pp. 2, 5–6]; the arc-only model wins 16 of 22 runs against two linked models [S013 pp. 7–8, 23, 32]; big-M continuous variables projected out of a pure ILP master [S006 pp. 1–4, 7].
  - Fat and slim models, 2007–2009: the fat scenario model kept only as a benchmark and a slim surrogate solved [D004 pp. 4, 8, 13; S018 pp. 11–13; S010 pp. 16–17]; the price of the simplification measured where the unfrozen model is still tractable [S018 pp. 18–20]. The fat/slim words are already in the 2008 light-robustness chapter [S010 p. 16].
  - Benders redesign: allocation variables projected out, costs aggregated, fat and slim chosen per cost class by measurement [S011 pp. 1, 5, 10–15; S195 pp. 2, 5, 12–13, 17–18]; "Recent experience with the Steiner Tree Problem [9] showed that some known MILP models can be “thinned out” by removing unnecessary variables and constraints, with a very significant performance boost." [S195 p. 2].
  - Steiner trees: edge variables dropped under uniform costs, a filter on cheap instance features picks the model per class, thin and fat measured on the same instances, and the thin model loses on one class and runs out of memory on another [S040 pp. 1–2, 4–5, 13–14, 17].
  - Symmetry by aggregation: clones aggregated into types [S067 pp. 3–5]; one variable per orbit, which alone lifts the solved multiple-knapsack count from 65 to 82 [S097 pp. 4–6, 20, 24]; the conference version [D013 pp. 1, 4–6].
  - Model chosen for the instances: by where the feasibility rules live [S012 pp. 6–9]; by size, with a compact, possibly weaker model beyond about 1,000 sites [S154 pp. 7–9]; the 2026 slim MILP field model and its projected master [S143 pp. 17–18, 24–25; S144 pp. 3–4, 7–8; S162 pp. 2–3, 7, 12, 17].
  - Subtraction (step 5): "We then followed an inverse path and disabled/simplified the new features until we found which are the ideas that really made a difference." [S059 p. 5]; three pieces built, measured and removed [S079 pp. 9, 12–13]; one device at a time and all at once [S125 pp. 19–21; S057 pp. 25–26]; ablation arm in every table [S032 pp. 16–19]; 63 portfolio combinations cut to 14 [S126 pp. 12, 24–25]; already in 1995, both cut classes removed at once [S060 pp. 8–9, 11].
- **Stated (co-signed).** A weaker relaxation is no drawback inside a heuristic: "According to our opinion, this is not a drawback within heuristic algorithms, where the main objective is to determine good SCP solutions without insisting in proving optimality." [S003 p. 5]; "In addition, no strict correlation exists between the lower bound value L(u) and the quality of the SCP solution found." [S004 p. 5]. Weak big-M models become effective inside proximity search [S052 p. 24]. "The lesson learned is that, in some cases, the simpler the formulation, the more likely it will not introduce nasty side effects." [S067 p. 7].
- **Say–do update.** ✅ stated and practised, with dates widened: projection from 1999 [S069; S073; S028; S013; S006], fat and slim from 2007 [D004; S018; S010], the heuristic-side preference for a weaker relaxation stated in 1999–2000 [S004 p. 5; S003 p. 5].
- **Variants.** Strengthen first, thin only after the full model fails, then repair with an exact LP [S046 pp. 8–23; S198 pp. 49–63]; the limitation *for exact work he calls the root LP bound critical* has a counter-case, the root bound "is not a discriminating factor" among the QAP forms [S067 p. 7]; subtraction decided per instance class (an ingredient kept because it pays on the hard instances though it slows another class) [S124 pp. 20–22]; cumulative ablation instead of subtraction [S038 pp. 16–18]; a subtraction finding (switching cuts off is faster) reported while the cut version stays in the table [S137 p. 9; D019 pp. 7–8]; the tighter surrogate was the easier model, and modelling the actual weekly rule saved another 2% of duties [S015 p. 11]; dominance thinning stopped where it would cost the solver its generic branching [S092 pp. 3–4, 7–8]; thinning degrees of freedom to cure overfitting [S109 pp. 7–9, 16]; subtraction applied to someone else's pipeline [S161 pp. 1–3].
- **Contradictions.** A 1995 code fattens the model with a vehicle index to strengthen the LP and breaks the vehicle symmetry by ordering constraints [S114 pp. 2, 4]; the joint handbook chapter makes LP tightness the leading criterion, "the formulation with the higher LP optimum is usually preferable" [S145 p. 4; pp. 3–4, 15–16]. Both fit the method's own limitation for exact work and its dating.
- **Proposed text.** Practice: add the 1999–2006 projection line and the 2007–2009 fat/slim line with the cards above; Say–do: *stated 2003–2016, practised from 1999*. Limitations: add the QAP counter-case and the textbook voice.

| # | Skill claim (section) | Full texts | Change |
|---|---|---|---|
| 8 | Method 1 Say–do: practised 2011–2017 | Projection 1999–2006 [S069 pp. 3, 5–6; S073 pp. 3–4; S013 pp. 7–8; S006 pp. 1–4]; fat/slim 2007–2009 [D004 pp. 4, 8; S010 p. 16; S018 pp. 11–13] | Widen the dates |
| 9 | Method 1 limitation: for exact work he calls the root LP bound critical | Counter-case [S067 p. 7]; support in the joint handbook-chapter voice [S145 pp. 3–4] | Add both |
| 17 | Method 1 practice: the train-rescheduling team kept two of about eight ideas, removing the others improves performance (TRI16 deck) | The paper has the subtraction [S059 p. 5] but neither the count nor the improvement claim | Keep the deck as the source of both |

### Counts

Cards linking the method: 43 evidence, 43 variant, 2 contradiction; works after merging pairs 34 / 38 / 2; read in full or part 34 / 34 / 2; deep evidence works by period up to 2000 / 2001–10 / 2011–20 / 2021–26: 6 / 12 / 9 / 7 (08 §2).

### Added in T3.6

- **Evidence block** in the house format: Stated, the VIE15 recipe (the guard quote, CORS15 PDF p.2, and MATH16 moved to the Before block); Practice [S011 pp. 1, 5, 10–15; S069 pp. 3, 5–6; S097 pp. 4–6, 20, 24; S059 p. 5], with the S059 subtraction quote; Say–do *✅ stated (decks 2003–2016) + practised from 1999* with the counts above; four variant or correction bullets: dates [D004 pp. 4, 8] (the 1999 projection card S069 is in the Practice line), strengthen first [S046 pp. 8–23], subtraction per class [S124 pp. 20–22], the 1995 code and the textbook voice [S114 pp. 2, 4; S145 p. 4].
- **Step 5**: one device at a time and all at once [S125 pp. 19–21] (catalog EP26).
- **Limitations**: the QAP counter-case, the root bound "is not a discriminating factor" [S067 p. 7].
- **Review fix**: the ✗ bullet *Practised from 1999 (projection) and 2007 (fat and slim), not only 2011–2017 [D004 pp. 4, 8].* is folded into the Say–do line and marked ✗ there; *the joint textbook* → *the joint handbook chapter* (S145 is the 2017 MOS-SIAM chapter with Balas); the say–do counts are written as evidence/variant/contradiction.
- **Moved out** (kept below): the Steiner, Benders, orbital-shrinking and QAP DOIs of the old Practice line; the TRI16 count *two of about eight ideas* and its quote, which the paper does not carry (08 §3 item 17: the paper has the subtraction [S059 p. 5] but neither the count nor the improvement claim; the deck stays their source).

### Before T3.6 (moved verbatim)

```markdown
### Method 1: Thin the model out before strengthening it
**One line**: When instances are hard, suspect over-modelling first: remove or project out low-role variables, pick the model that fits the instances at hand, then touch the algorithm; when the code works, subtract ideas until removal hurts. (New.)
**Evidence**:
- Stated: 10 or more sources, 2003-2016 (02 R1). His recipe: "1. Choosing a model that better fits the instances of interest 2. Removing variables that play a little role for the problem class of interest 3. Using decomposition to break the problem into smaller pieces" (VIE15 PDF p.7). The guard: "Not to misinterpreted and used as an excuse to address oversimplified models" (CORS15 PDF p.2). For heuristics a polyhedrally weak model can be preferred (MATH16 p.3, joint with Martina Fischetti).
- Practice: the node-only Steiner model (DOI 10.1007/s12532-016-0111-0); Benders projection of allocation variables (DOI 10.1287/mnsc.2016.2461); orbital shrinking and slim QAP models (DOI 10.1016/j.dam.2017.01.015; 10.1287/opre.1120.1073). Subtraction: the train-rescheduling team kept two of about eight ideas, since "removing all the others does not deteriorate (but actually improves) its overall performance !" (TRI16 PDF p.11; DOI 10.1016/j.ejor.2017.04.057).
- Say–do consistency: ✅ stated + practised (2011-2017, joint in every case).
**Steps**:
1. Separate the variables that only describe the problem from those that carry decisions for this class (allocation variables, edge variables under uniform costs, symmetric copies).
2. Choose the model that fits the instances, not the tightest known one; for heuristics a weaker model may win.
3. Project the low-role variables out (Benders), or aggregate symmetric ones along orbits instead of breaking the symmetry.
4. Solve the thin model with stock branch-and-cut plus one callback; report fat and slim models on the same instance and decide per cost class by measurement (Benders anatomy, "Fat or slim").
5. Once it works, remove ingredients one at a time; keep one only if removing it hurts.
6. 🔴 Go back if the thin relaxation bounds no better than the LP, or the simple model no longer answers the real question.
**Applies to stage**: choosing the problem, idea, debugging.
**Different from standard practice**: the reflex is to strengthen a formulation; here the first move is to delete, and ablation is by subtraction.
**Limitations**: with the whole symmetry group the orbital-shrinking bound equals the LP bound on 31 of 39 instances ([05 §8](references/research/05-peer-critique.md)); for exact work he calls the root LP bound critical; later problem-specific methods beat his generic bilevel solver by large factors (05 Q12).
```

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it, word for word in fenced blocks (links as written in SKILL.md, relative to the skill folder). The shortened lines are in SKILL.md.

*Core Research Methods intro (the line above Method 1):*

```markdown
Ordered by exclusivity and increment. Tags: [stated] his own deck or sole-author text; [joint] a co-signed paper whose "we" cannot be split; [practice] what papers and records show was done. Pointers such as "02 R7" or "03 PE-13" name the research note and item behind a claim; full paper titles are under Sources. Say–do counts are cards linking the method, as evidence/variant/contradiction; the full evidence and the pre-synthesis text are in the ledger.
```

*Practice:*

```markdown
- Practice: allocation variables projected out, fat and slim chosen per cost class by measurement [S011 pp. 1, 5, 10–15]; flows projected into max-flow cuts in 1999 [S069 pp. 3, 5–6]; one variable per orbit, solved multiple-knapsack instances 65 → 82 [S097 pp. 4–6, 20, 24]; subtraction: "We then followed an inverse path and disabled/simplified the new features until we found which are the ideas that really made a difference." [S059 p. 5].
```

*Variant bullet 3:*

```markdown
  - ✗ A 1995 code fattens the model [S114 pp. 2, 4]; the joint handbook chapter prefers "the formulation with the higher LP optimum" [S145 p. 4]; both fit the exact-work limitation.
```

<a id="method-2"></a>

## Method 2: Blame the loop, not the component

### Full-text evidence (08 §2 and §2.2, copied)

| Method | Cards E / V / C | Works E / V / C | Deep E / V / C | Deep E by period | Say–do after the full texts |
|---|---|---|---|---|---|
| M2 Blame the loop | 17 / 30 / 2 | 12 / 27 / 2 | 12 / 27 / 2 | 0 / 5 / 7 / 0 | ✅; a 2000–2001 precursor; the controlled-oracle test sits in the 2009 yoyo manuscript, not in S106 |


- **Strongest practice.**
  - The earliest text for steps 3 and 4 is the 2009 yoyo manuscript: the oracle is unchanged, the query point moves to the midpoint between a core point and the LP optimum, and the loop is first tested with a controlled oracle (the LP's own inequalities hidden inside the separator, three cut-quality rules), then on real Benders separation with the same separator in both arms [S174 pp. 1–8].
  - Gomory's method: the stall is put on the loop and the LP solver, "This behavior is in a sense a consequence of the efficiency of the underlying LP solver, that has no reason to change the LP solution once it becomes optimal with respect to the original objective function" [D009 p. 8]; "As new degenerate vertices are created by the cuts themselves, the textbook method enters a feedback loop that is responsible for the exponential growth of the determinant of the current basis, as reported in Figure 4(d)." [S074 p. 14]; diagnosed on stein15 and cured by lexicographic reoptimization with the cut unchanged [D009 pp. 3–5, 7–14; S074 pp. 5–7, 14–15; D011 pp. 3–5].
  - The generator kept, its input changed: cuts read from bases of the original system and relaxed in Lagrangian fashion [S095 pp. 2–6]; GMI cuts read from bases sampled along a subgradient trajectory, with tailing-off detection [D014 pp. 4–6, 11, 15].
  - In-out on disjunctive cuts with "exactly the same separation module" [S106 p. 2; pp. 1–5]; Benders: the curse of Kelley named, the cure borrowed from Lagrangian dual minimization, one separator under three policies on gs250a-1 [S195 pp. 14–17]; "This is perhaps the most important ingredient in our recipe." [S011 p. 12; pp. 12–14]; the root loop moved to in-out on capacitated facility location [S023 pp. 10–11, 18]; the master objective changed to a proximity function [S086 pp. 3–4].
  - **Precursor (2000–2001).** The multiple-depot vehicle scheduling code separates a point between x* and the two best incumbents before x*, "A similar idea was proposed by Reinelt [10]." [S125 p. 11]; without it the root bound on one instance takes 1,400 s instead of 800 s [S125 pp. 11–12, 20–21; S057 pp. 20, 26].
- **Variants.** In 2005–2010 the cure is still the component: a different cut family inside the same loop [D003 pp. 8–9; S033 pp. 11–12], a CGLP normalization [S112 pp. 2, 7–9], a new cut family for Benders [S006 p. 3]; consistent with Common Misreading 3. Separation rounds that return a family spanning the graph [S005 pp. 12–14; S047 p. 24]; the loop idea carried to a subgradient ascent [S004 pp. 7–9], a column-generation loop [S077 pp. 4–5, 10–11], strong branching [D012 pp. 3–4], a repair call site [S126 pp. 13–14], the pump [S164 pp. 2, 4–5, 7, 14] and a local-search query policy [S150 pp. 12–13, 20–21, 24]; the reverse move, the loop kept lexicographic and the cut family swapped for combinatorial nogoods [D019 pp. 6–7].
- **Contradictions.** 2010: the Benders cure is the component and the loop stays standard [S024 pp. 2, 4]; 2026: "No stabilization techniques have been implemented because their benefits turned out to be marginal in our overall solution scheme in preliminary tests." [S144 p. 7].
- **Correction.** The skill's Method 2 practice cites DOI 10.1007/978-3-642-13520-0_17 (S106) for a first test on an LP whose constraint list plays the oracle under artificial cut-quality rules; that test is not in S106, which goes straight to the real lift-and-project separator [S106 pp. 3–5]. It is in the yoyo manuscript [S174 pp. 6–7].
- **Say–do update.** ✅ stated (decks 2010–2026, notes 02 R7) and practised 2008–2026, with the 2000–2001 precursor.
- **Proposed text.** Repoint step 4 to S174; add the precursor to Common Misreading 4; add the 2026 counter-case to the limitations (on time-window TSP with stochastic times, branching raised the bound faster than stabilization [S144 p. 7]).

| # | Skill claim (section) | Full texts | Change |
|---|---|---|---|
| 2 | Method 2 practice: the controlled-oracle test cited to DOI 10.1007/978-3-642-13520-0_17 | Not in S106, which goes straight to the real separator [S106 pp. 3–5]; the test is in the 2009 yoyo manuscript [S174 pp. 6–7] | Repoint to S174 |
| 12 | Common Misreading 4: the in-out loop presented as new in 2009, credited in 2010 | Confirmed [S174 pp. 1–2, 7–8, 12–13; S106 pp. 1–2]; precursor in 2000–2001, a point between x* and two incumbents separated first and credited to Reinelt [S125 pp. 11–12; S057 p. 20] | Add the precursor |
| 22 | Method 2 limitation: one showcase instance since 2016 | The gs250a-1 traces are already in the April 2015 report [S195 pp. 15–17] | *since 2015* |

### Counts

Cards: 17 evidence, 30 variant, 2 contradiction; works 12 / 27 / 2; read in full or part 12 / 27 / 2; deep evidence works by period 0 / 5 / 7 / 0 (08 §2).

### Added in T3.6

- **Evidence block**: Stated, the VRL25 quote (the LAG10 quote moved to the Before block); Practice [S174 pp. 1–8; D009 pp. 7–14; S074 pp. 5–7, 14–15; S011 pp. 12–14; S125 pp. 11–12]; Say–do with the counts; four bullets: the controlled-oracle test repointed from DOI 10.1007/978-3-642-13520-0_17 to the yoyo manuscript [S174 p. 5; S106 pp. 3–5]; the 2005–2010 component cures [D003 pp. 8–9; S033 pp. 11–12]; the two contradictions [S024 pp. 2, 4; S144 p. 7]; the move carried beyond cut loops [S004 pp. 7–9; D012 pp. 3–4; S164 pp. 4–5].
- **Steps 1, 3 and 4**: catalog EP31 [D009 pp. 7–11]; DM6 [D009 pp. 4–5]; DM10; the controlled oracle [S174 pp. 6–7] (file pages: the file's [[page N]] carries printed page N − 1, so the draft's *p. 5* was the printed number).
- **Limitations**: *since 2016* → *since 2015*, the traces being in the April 2015 report [S195 pp. 15–17].
- **Review fix**: the ✗ bullet *The controlled-oracle test is in the yoyo manuscript [S174 p. 5], not in the CPAIOR 2010 paper (DOI 10.1007/978-3-642-13520-0_17) [S106 pp. 3–5].* left the variant list (step 4 and the Corrections list carry it, at [S174 pp. 6–7]); the 2026 S144 case is a ✗ counter-case with its switch signal (the root bound crawled and rose much faster once the solver branched, so Benders cuts went to integer solutions only and stabilization was skipped), repeated at step 6 [S144 p. 7], as 08 §2.2 proposed; step 1 names the EP31 curves and the Benders plot of bound against log time per loop policy, with the active cuts at the end of the root [S011 p. 13]; step 3 says why all ones is a valid start (the master has only 0-1 bounds and Σ y ≥ 2 [S011 pp. 5, 12]) and gives the fallback, a first heuristic solution [S106 pp. 3–4]; step 4 says how to build the controlled oracle [S174 pp. 6–7]; step 5 names the stop rules (catalog DM10, DM12).
- **Moved out** (kept below): the old practice pointer *03 PE-13; DOI 10.1007/978-3-642-13520-0_17* for the controlled-oracle test, and the gs250a-1 sentence, which the Benders anatomy keeps.

### Before T3.6 (moved verbatim)

```markdown
### Method 2: Blame the loop, not the component
**One line**: When a component (Gomory cuts, Benders cuts) is blamed for stalling, instrument the loop that drives it on one small instance and change where the loop queries the oracle, leaving the oracle alone. (Deepened; overturns the common picture of his Benders work.)
**Evidence**:
- Stated: 8 or more decks, 2010-2026 (02 R7). "Kelley + Gomory is problematic in the long run, but ... it is not all Gomory's fault!" (LAG10 PDF p.9); "Slow convergence is generally attributed to the poor quality of Benders cuts, to be cured by a more clever selection policy ... but there is more..." (VRL25 PDF p.9).
- Practice: Gomory trajectories and basis-determinant growth plotted on stein15, lexicographic re-optimisation as the remedy (DOI 10.1007/s10107-009-0335-0; 10.1007/s10107-010-0392-4). The two-point loop was tested first on an LP whose constraint list plays the oracle, with artificial cut-quality rules (03 PE-13; DOI 10.1007/978-3-642-13520-0_17). On gs250a-1 Kelley stalled at the root for 15,000 s; in-out closed it in under a second (Benders anatomy).
- Say–do consistency: ✅ stated + practised (2008-2026).
**Steps**:
1. On one small stalling instance, plot the LP-solution trajectory, a basis-size measure and the bound against iterations.
2. Ask what the loop feeds the oracle: Kelley always separates the current LP optimum, an extreme and unstable point.
3. Change the query: re-optimise lexicographically, or keep a core point (started at all ones), move it halfway towards each new LP optimum and separate near it, or change the master objective. Even a small perturbation of the separated point (their 2ε trick) helps Kelley (UFL17 pp.12-13).
4. Test the new loop first with a controlled oracle (artificial cut-quality rules), then with real separators; every compared loop (Kelley, perturbed Kelley, in-out) calls exactly the same separator (UFL17 p.13).
5. Keep the simplest version that works; without a hook in the tree, stabilise the root only and say why: a better loop inside CPLEX "is however not immediate", and a tight root bound leaves few nodes (UFL17 p.14). Credit the scheme's lineage before calling it new.
6. 🔴 Never judge a cut family weak from a Kelley-loop run; never expect a stabilised pure cutting-plane loop to replace enumeration.
**Applies to stage**: debugging, idea.
**Different from standard practice**: the usual cure for slow Benders is better cut selection; here the separator stays and the query point moves.
**Limitations**: one showcase instance has carried the argument since 2016 (05 §5.2); critiques of his 2010 cut-selection rule are unanswered (05 Q6); on multi-commodity fixed-charge network design (not facility location), a 2026 unrefereed comparison of 50 Benders variants finds direct branch-and-cut fastest overall (arXiv 2607.07899, pp.3, 18).
```

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it, word for word in fenced blocks (links as written in SKILL.md, relative to the skill folder). The shortened lines are in SKILL.md.

*One line:*

```markdown
**One line**: When a component (Gomory cuts, Benders cuts) is blamed for stalling, instrument the loop that drives it on one small instance and change where the loop queries the oracle, leaving the oracle alone. (Deepened; overturns the common picture of his Benders work.)
```

*Practice:*

```markdown
- Practice: the 2009 yoyo manuscript keeps the oracle, moves the query point between a core point and the LP optimum, and tests with a controlled oracle first [S174 pp. 1–8]; Gomory's stall traced on stein15 to the loop and cured by lexicographic reoptimization, the cut unchanged [D009 pp. 7–14; S074 pp. 5–7, 14–15]; one separator under three loop policies on gs250a-1 [S011 pp. 12–14]; a 2000–01 precursor credited to Reinelt [S125 pp. 11–12].
```

*Variant bullet 3 (2026 counter-case):*

```markdown
  - ✗ 2026 counter-case, time-window TSP: the root bound crawled and rose much faster once the solver branched, so Benders cuts went to integer solutions only and stabilization, marginal in tests, was skipped [S144 p. 7].
```

<a id="method-3"></a>

## Method 3: Placebo first: variability as a control arm, then as a resource

### Full-text evidence (08 §2 and §2.3, copied)

| Method | Cards E / V / C | Works E / V / C | Deep E / V / C | Deep E by period | Say–do after the full texts |
|---|---|---|---|---|---|
| M3 Placebo first | 13 / 34 / 19 | 13 / 32 / 18 | 13 / 32 / 18 | 0 / 2 / 7 / 4 | ✅ in the variability papers and in 2026; ✗ elsewhere: 18 works report one run per instance |


- **Strongest practice.**
  - Seeds and a control arm in 2009: "As already discussed, random perturbations are a fundamental ingredient of the FP scheme, so it is not completely fair to compare different variants on a single run." [S041 p. 14]; ten seeds, a more-than-6-of-10 rule, a per-seed scatter, and arbitrary variable orders as control arms [S041 pp. 14–15, 20].
  - Content-free changes before the 2012 statement: multiplying every generated cut by 1,000 lowers the average gap closed from 56.9% to 46.8%, read as "the importance of “small implementation details” when evaluating the performance of a method" [S068 p. 8]; a deliberately wrong rounding as a contrast arm and an LP restart as a mechanism probe [S074 pp. 8, 16]; two branching rules that must give identical trees, so node counts check the implementation [D012 p. 7].
  - Measured, then exploited: 100 seeds on 58 instances, single-thread, with the classes where it does not pay [S055 pp. 2–9]; ten row and column permutations on three solvers to show that the variance is solver-independent [S094 p. 5]; a budget-matched ablation with a random-direction control and a shadow trajectory [S098 pp. 18, 23–24]; 100-seed statistics [S123 pp. 10, 14–16]; variability designed out of a parallel measurement by frozen trees and a given optimum [D017 pp. 12–13, 21–22].
  - Later: a pure-random arm as noise floor, "while a pure random approach (random2) is among the worst methods, allowing us to argue that we are not just looking at noise" [S126 p. 20]; a content-free perturbation of the judge (a 15-degree phase shift) [S150 p. 16]; the A/A null, "Its measured ratio to the baseline has true value one, so its dispersion across seeds tells the reader—and told us—how small a ratio this apparatus can honestly resolve." [S163 p. 2; pp. 5, 16–19].
- **Variants.** One fixed seed in all runs ("For a fair comparison", the text says), spread controlled away rather than measured [S124 p. 16]; spread measured as a diagnostic, 200 perturbed priority orders [S067 p. 12]; best of ten seeds per machine as the resource [S059 pp. 4–5, 8]; seeds in the design but no placebo arm, a declared test family instead [S164 p. 13; S143 pp. 21–25].
- **Contradictions (dated lapses).** One run per instance, no seeds: 2001 [S013 pp. 24, 26], 2003 [S001 p. 14], 2004 [S064 p. 14; S198 p. 27], 2005 [S007 pp. 6–9], 2006 [S006 pp. 14–18], 2007 [S026 pp. 11–12], 2008 [S085 pp. 6–7], 2009 [H006 pp. 11, 16], 2013 [S063 pp. 8–10], 2014 [S154 pp. 10–11], 2016 [S086 pp. 5, 12], 2017 [S016 pp. 20, 22, 29; S097 pp. 7–26], 2018 [S082 pp. 6, 9–12; S133 pp. 2–3], 2020 [S078 pp. 28–34], 2022 [S076 pp. 13–21]. The backdoor-branching gain over the solver, about 15% in arithmetic-mean time and comparable in geometric mean, comes from one run per instance, so it carries no measured spread [S063 pp. 8–10]. (Setting it beside the roughly 25% placebo speed-up of the 2012 EURO deck, a different experiment on other instances and another solver version, is this note's cross-study inference, not a statement of the paper; it is not a verdict on the work, only the general lesson that a placebo must be measured on one's own instances and solver.)
- **Say–do update.** *Practice first* holds for the variability line: control arms in 2009–2012 [S041; S068; S074; D012] precede the 2012 statement, and seeds run through S055, S094, S123 and D017. Outside that line, single runs are the norm from 2001 to 2022 (18 co-authored works, several led by co-authors), and seed reruns are rare (5 seeds to confirm selected wins in 2020 [S079 p. 16]). The skill's sentence *Seeds were in his designs before the statement* should name the line it holds for.
- **Proposed text.** Practice: add the 2009–2012 controls (S041, S068, S074, D012) as the early form of the placebo arm; limitations: *most computational papers outside the variability line report one run per instance (2001–2022)*.

| # | Skill claim (section) | Full texts | Change |
|---|---|---|---|
| 7 | Method 3: seeds in his designs before the statement | True for the variability line [S041 pp. 14–15; S055 pp. 2–9]; one run per instance in 18 other works 2001–2022, among them [S063 pp. 8–10] (§2.3) | Name the line; add the limitation |

### Counts

Cards: 13 evidence, 34 variant, 19 contradiction; works 13 / 32 / 18; read in full or part 13 / 32 / 18; deep evidence works by period 0 / 2 / 7 / 4 (08 §2).

### Added in T3.6

- **Evidence block**: Stated, the EURO12 quote (the ISCO14 credit to Danna moved to the Before block; the erraticism anatomy cites the paper's credit [S055 p. 1]); Practice [S041 pp. 14–15, 20; S068 p. 8; S055 pp. 2–9; S163 pp. 2, 5], with a phrase of the S041 p. 14 quote; Say–do *✅ stated (2012) + practised first in the variability line (2009–2026); ✗ outside it*; four bullets: the single-run works [S063 pp. 8–10], one fixed seed [S124 p. 16], best of ten seeds as the resource [S059 pp. 4–5, 8], 2026 seeds without a placebo arm [S164 p. 13].
- **Step 1**: nodes and LP iterations on a loaded machine [S055 p. 3] (catalog EP24). **Step 2**: the EURO 2012 placebo figure moved here from the old Practice line, with an A/A arm (catalog EP19). **Step 3**: the success rule [S041 pp. 14–15]. **Step 4**: the best-of-k-seeds ceiling first [S055 p. 3] (EP18); Heuristic 6 folded in with its EURO12 phrase; ideal-oracle ceilings and the classes where bet-and-run does not pay [S055 pp. 6–9].
- **Moved out** (kept below): the old sentence *Seeds were in his designs before the statement*, which holds for the variability line only (08 §2.3), and the old pointers ERR14 p.10, DOI 10.1007/s12532-009-0007-3 and 03 PE-24.
- Not carried into SKILL.md: 08's limitation sentence *most computational papers outside the variability line report one run per instance (2001–2022)* is in the first variant bullet instead.
- **Review fix**: Say–do *✅ stated (2012) + practised first in the variability papers (2009–2026); outside them one run per instance in 18 co-authored works (2001–2022), seed reruns rare [S079 p. 16]*; bullet 1 without the cross-study placebo comparison (labelled as this note's inference in the copy above): *the single-run works report gains with no measured spread, e.g. backdoor branching, about 15% in arithmetic-mean time and comparable in geometric mean [S063 pp. 8–10]*; step 2 *measured on your own instances and solver*; step 3 reads the gain against the A/A arm's spread across seeds [S163 p. 2]; step 4 cites catalog EP35 (bet-and-run). The T3.6 bullet was:

```markdown
  - ✗ *Seeds were in his designs before the statement* holds for the variability line only; 18 works (2001–2022) report one run per instance, e.g. a backdoor-branching gain of about 15% no larger than step 2's placebo [S063 pp. 8–10].
```

### Before T3.6 (moved verbatim)

```markdown
### Method 3: Placebo first: variability as a control arm, then as a resource
**One line**: Before believing a speed-up, measure what a change that cannot help produces; put seeds or permutations into the design; then use the spread on purpose. (Deepened; "exploit variability" is already known.)
**Evidence**:
- Stated: 8 or more sources (02 R3). "(Some degree of) erraticism is intrinsic in tree-search nature ... ... you cannot avoid it (important for experiment design) ... and you better try to turn it to your advantage ... though you will never have a complete control of it" (EURO12 PDF p.14). The observation is credited to Danna 2008 (ISCO14 PDF p.8).
- Practice: at EURO 2012 nine single-cut methods gave about 25% average speed-up over CPLEX 12.2, and the cut was redundant and removed: the gain came from perturbed initial conditions (01 SW4). 100 seeds on each of 58 instances, single-thread, in the erraticism paper, with no gain on easy instances (DOI 10.1287/opre.2013.1231; ERR14 p.10). Seeds were in his designs before the statement: 10 seeds and a more-than-6-of-10 success rule in FP 2.0 (DOI 10.1007/s12532-009-0007-3); a median over 5 seeds plus an exact sign test in 2026 (03 PE-24).
- Say–do consistency: ✅ stated + practised (practice first).
**Steps**:
1. Measure the baseline's own spread over k seeds or row-and-column permutations per instance, single-thread on an otherwise idle machine (01 SW4).
2. Add a placebo arm: a perturbation with no content (a redundant cut removed after the root, a changed seed).
3. Count only gains beyond the placebo's; put seeds in the table (a success rule over seeds, or a median over seeds then a paired test over instances).
4. Exploit the spread (bet-and-run): a few short randomised runs, bet on one by a quick criterion that needs only a positive correlation with the a-posteriori best run (H6), finish it; report where it does not pay (easy instances).
5. 🔴 A gain the size of the placebo effect is not a result.
**Applies to stage**: experiment design, judging.
**Different from standard practice**: variability is usually averaged away; here a null perturbation is a formal control arm.
**Limitations**: his baselines ran with CPLEX's dynamic search off; critics note the diversity came from reaching into solver internals (05 Q9); a 2026 preprint finds variability partly predictable (arXiv 2610.12876); cost multiplies by the number of seeds.
```

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it, word for word in fenced blocks (links as written in SKILL.md, relative to the skill folder). The shortened lines are in SKILL.md.

*One line:*

```markdown
**One line**: Before believing a speed-up, measure what a change that cannot help produces; put seeds or permutations into the design; then use the spread on purpose. (Deepened; "exploit variability" is already known.)
```

*Variant bullet 1:*

```markdown
  - ✗ *Seeds were in his designs before the statement* holds mainly for the variability papers; the single-run works report gains with no measured spread, e.g. backdoor branching, about 15% in arithmetic-mean time and comparable in geometric mean [S063 pp. 8–10].
```

*Step 4:*

```markdown
4. Exploit the spread (bet-and-run, catalog EP35): first the best-of-k-seeds ceiling (catalog EP18) [S055 p. 3]; then a few short randomised clones and a bet on one by a quick criterion that needs only "a positive correlation with the a-posteriori best run" (EURO12 PDF p.19; folded from Heuristic 6), a rule for selection inside randomised restarts only; finish it; print ideal-oracle ceilings and where it does not pay (easy instances) [S055 pp. 6–9].
```

<a id="method-4"></a>

## Method 4: A comparison harness blind to which method is yours

### Full-text evidence (08 §2 and §2.4, copied)

| Method | Cards E / V / C | Works E / V / C | Deep E / V / C | Deep E by period | Say–do after the full texts |
|---|---|---|---|---|---|
| M4 Blind harness | 71 / 34 / 19 | 65 / 29 / 16 | 62 / 29 / 16 | 5 / 24 / 23 / 10 | ✅, with dated lapses that recur from 1999 to 2026; significance tests in 2009 and 2025 |


- **Strongest practice.**
  - The dummy callback in 2003, a decade before the erraticism paper: "If some instances are discarded because they are too easy or too hard, they should be too easy or too hard for both codes, as it may be unfair to mark as “too easy” the instances solved in less than a few seconds by just one of the two codes, in that this will put the slower code in an advantageous position." [S070 p. 10]; the same device in later papers [S055 pp. 6–8; D017 pp. 22–23].
  - Same-code arms early: one component switched off in the authors' own code (1995) [S060 p. 11]; the rival's bound re-implemented in the same code [S077 p. 10]; same-engine pairing of the pump with each solver [S026 p. 8].
  - Class rules symmetric in the arms: "the competing methods play an indistinguishable role in the class definition" [S079 p. 14; pp. 10–11]; classes by any compared solver's time [D017 p. 23]; outcome classes on both codes [S006 p. 14]; classes by both solvers [S094 p. 13]; a stated test-bed rule [S063 pp. 7–8].
  - An independent judge as the shared machinery: "However, we decided to implement an external simulation-based validation module that is independent from the optimization model itself" [S018 p. 9; pp. 2, 10–11]; the same validator for every trainer [D004 pp. 6–8; S010 pp. 7, 15; D007 p. 3]; a judge called by no search [S150 pp. 9, 15–16].
  - Untuned new method, stated biases: [S001 pp. 13–15; S085 pp. 5–6; S023 pp. 14, 17]; the bias toward one arm printed and removed by a control arm [S115 p. 4]; the baseline denied an internal shortcut the new arms cannot use, the rival keeping it [D012 pp. 6–7]; rival re-implemented in the same framework and validated against its published results [S027 pp. 22–23; S082 pp. 7, 12; S092 p. 16]; separate tuning and test sets [S078 pp. 8–9; S164 p. 17]; analysis subsets fixed in advance by the challenged method's pilot and every sign re-checked on the full test bed [S164 pp. 11, 13]; held-out test set fixed before any run [S162 p. 17].
  - Vendor-tuned baseline: after "extensive experiments and contacts with ILOG-Cplex staff" the best root setting is presolve off [S007 p. 6].
- **Significance tests before 2026.** FP 2.0 reports relative improvements with 95% confidence intervals and compares variants with a Cochran Q-test followed by post hoc McNemar comparisons [S041 pp. 15, 17, 20]; the 2025 fix-propagate-repair paper tests the discordant cells of a 2×2 success table with McNemar [S126 p. 25]. The skill's Method 4 line *No significance test before 2026* and the Roundtable Card's blind spot *no statistical tests before 2026* are contradicted (§3).
- **Contradictions (dated lapses).** Rival times taken from other machines or papers: 1999 [S069 p. 21], 2001 [S057 pp. 23–24, 28; S125 p. 19], 2006 with a conservative factor [S014 pp. 13, 16], 2016 [S023 pp. 16–17, 20], 2015–16 [S123 pp. 11–13, 17], 2017 [S016 pp. 34–38], 2018 (two machines) [S082 p. 9]. A heuristic called comparable to practitioners' procedures without running any (2000–2001) [S073 p. 7; S072 p. 13]. A rule fitted on the instances it is evaluated on: 2012 [D013 pp. 6–10], still in the 2017 journal paper [S097 pp. 9–12]; portfolio members chosen on the 240 instances that score them (2025) [S126 pp. 19, 24–25]. A class that keeps only instances where the authors' own aggregation closes more than 70% of the gap, which fails the swap test (2013) [D014 pp. 18, 21–22]. A subsample without a stated rule [S101 pp. 16–18]; the authors' own greedy as the only baseline on three instances [S046 pp. 14, 25, 28]; a general-purpose arm where specialized codes exist, conceded in print [S109 pp. 14–15]; a rival entered only as a formulation inside the authors' harness [S144 pp. 3–7, 12]; a 1995 code judged against the optimum with no rival [S005 pp. 19, 25].
- **Say–do update.** ✅ stated and practised; the lapses recur over 1999–2026 rather than in three dated papers, and two works use significance tests before 2026.
- **Proposed text.** Practice: add the 2003 dummy callback and class rule (S070), the external validator (S018, D004, S010), rival re-implementation (S027, S082, S092). Say–do: replace *No significance test before 2026* by *significance tests rare before 2026 (FP 2.0, 2009; fix-propagate-repair, 2025)*; widen the lapse list.

| # | Skill claim (section) | Full texts | Change |
|---|---|---|---|
| 1 | Method 4 Say–do and Roundtable Card Blind spots: no significance or statistical tests before 2026 | 95% confidence intervals, a Cochran Q-test and post hoc McNemar comparisons in 2009 [S041 pp. 15, 17, 20]; a McNemar test in 2025 [S126 p. 25] | *Significance tests rare before 2026 (2009, 2025); a declared apparatus from 2026* |
| 10 | Method 4: dated lapses in 2011, 2012 and 2017 | Lapses recur 1999–2026 (§2.4) | Widen the list; keep the word *dated* |

The 2003 class rule in full: "If some instances are discarded because they are too easy or too hard, they should be too easy or too hard for both codes, as it may be unfair to mark as “too easy” the instances solved in less than a few seconds by just one of the two codes, in that this will put the slower code in an advantageous position." [S070 p. 10]. Keeping instances easy for the rival: "would have been unfair to SCIP as it would have produced a biased dataset" [S079 p. 16].

### Counts

Cards: 71 evidence, 34 variant, 19 contradiction; works 65 / 29 / 16; read in full or part 62 / 29 / 16; deep evidence works by period 5 / 24 / 23 / 10 (08 §2).

### Added in T3.6

- **Evidence block**: Stated, the EURO12 swap rule under the Integrity Rules and its 2003 printed form [S070 p. 10]; the ERR14 and PRX14 quotes moved to the Before block; Practice [S070 p. 10; S055 p. 6; S079 p. 14; S018 p. 9; D004 pp. 6–8; S027 pp. 22–23; S007 p. 6]; Say–do *✅ stated + practised; dated lapses recur 1999–2026*; four bullets: significance tests before 2026 [S041 pp. 15, 17, 20; S126 p. 25], more lapses [S069 p. 21; S016 pp. 34–38; S126 pp. 19, 24–25], the 2013 class [D014 pp. 18, 21–22], a heuristic called comparable without a run [S073 p. 7].
- **Step 2**: both emphasis settings [S001 p. 12]; the rival's settings searched and its failures reported [S007 p. 6]; Heuristic 5 folded in (*by vendor documentation or by asking how to tune it*). **Step 3**: the S079 p. 16 quote. **Step 4**: catalog EP15. **Step 5**: EP11. **Step 6**: an ideal oracle [S055 pp. 6–7].
- **Moved out** (kept below): the old say–do line *No significance test before 2026* (contradicted, 08 §3 item 1) and its three dated lapses (2011, 2017, 2012 with the Bertsimas–Dunning–Lubin report), which the lapse list widens.
- **Review fix**: step 4 adds catalog EP2 (for a branching or cut component, the optimal value as cutoff in every arm); the say–do counts are written as evidence/variant/contradiction.

### Before T3.6 (moved verbatim)

```markdown
### Method 4: A comparison harness blind to which method is yours
**One line**: Build the comparison so that swapping the two method names would change nothing, and every arm passes through the same machinery. (Deepened.)
**Evidence**:
- Stated: 9 or more sources (02 R4), most compactly the EURO12 conclusions quoted under the Integrity Rules. [joint] "For a fair comparison, all codes use a (possibly dummy) callback function, thus deactivating IBM ILOG Cplex's proprietary dynamic search" (ERR14 p.6); "This is a fair policy as the competing methods play an indistinguishable role in the class definition, so no biasing is expected" (ERR14 p.7); "we decided to be very conservative to avoid to overtune our method and to contaminate its outcomes" (PRX14 p.23).
- Practice: the 2005 pump baseline tuned after contact with ILOG staff, with a tuning suggested by Bixby (01 SW2); branching rules compared with preprocessing, heuristics and cuts off and the optimal value as cutoff (DOI 10.1016/j.orl.2012.01.008); a "not too easy nor hopeless" backdoor testbed (DOI 10.1287/ijoc.1120.0531); CPLEX and SCIP reported where they win (03 PE-15, PE-18 to PE-23).
- Say–do consistency: ✅ stated + practised, with dated lapses: an orbital-shrinking rule fitted on its evaluation instances (2011); rivals' published times from other machines (bilevel, 2017); arithmetic means without a test in a 2012 robust study, as Bertsimas, Dunning and Lubin report (DOI 10.1007/s10287-015-0236-z). No significance test before 2026.
**Steps**:
1. Put every arm, baseline included, behind the same interface, so the same solver features are on or off in all (a dummy callback in the baseline).
2. Baseline = what a practitioner would run (heuristic emphasis included), tuned as carefully as your method.
3. Define difficulty classes by a rule in which both methods play the same role, or by a baseline run fixed in advance; keep instances easy for the rival; list every exclusion with its reason.
4. Strip the extras so the idea is compared, not the code; tie an add-on's budget to the baseline's cost (a cut may cost about one root LP).
5. Run the new method untuned or conservative; keep tuning instances out of the evaluation.
6. Print ceilings and losses: an ideal oracle, the commercial solver where faster, any bias against the rival.
7. 🔴 Swap test: if exchanging the method names would change a class, an exclusion or a tuning choice, redo the design.
**Applies to stage**: experiment design, judging, reviewing others' tables.
**Different from standard practice**: fairness is a testable symmetry, not "same time limit, same machine".
**Limitations**: the dummy callback is specific to CPLEX's dynamic search of that era; vendor tuning advice came through personal contacts; his own pre-2026 tables carry the lapses above.
```

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it, word for word in fenced blocks (links as written in SKILL.md, relative to the skill folder). The shortened lines are in SKILL.md.

*Practice:*

```markdown
- Practice: a (possibly dummy) callback in every arm from 2003 [S070 p. 10; S055 p. 6]; classes in which "the competing methods play an indistinguishable role in the class definition" [S079 p. 14]; one external validator for every method [S018 p. 9; D004 pp. 6–8]; the rival re-implemented and validated against its published results [S027 pp. 22–23]; the baseline set after "extensive experiments and contacts with ILOG-Cplex staff" [S007 p. 6].
```

*Variant bullet 1:*

```markdown
  - ✗ *No significance test before 2026* is wrong: FP 2.0 gives 95% confidence intervals and Cochran Q with post hoc McNemar [S041 pp. 15, 17, 20]; McNemar in 2025 [S126 p. 25]. Rare before 2026; the declared apparatus is 2026's.
```

*Step 2:*

```markdown
2. Baseline = what a practitioner would run (heuristic emphasis included; both emphasis settings [S001 p. 12]), tuned as carefully as your method: search its settings and report its failures under each [S007 p. 6], by vendor documentation or by asking how to tune it (folded from Heuristic 5).
```

<a id="method-5"></a>

## Method 5: Re-test your own old claim, and publish whichever way it falls

### Full-text evidence (08 §2 and §2.5, copied)

| Method | Cards E / V / C | Works E / V / C | Deep E / V / C | Deep E by period | Say–do after the full texts |
|---|---|---|---|---|---|
| M5 Re-test your own claim | 11 / 8 / 0 | 11 / 8 / 0 | 10 / 7 / 0 | 0 / 4 / 1 / 5 | ✅; three source pointers of the skill need correcting |


- **Strongest practice.**
  - The 2018 minibatch claim re-tested against the 2019 untuned-baseline objection, conceded on p. 2, rates tuned in every cell, an A/A null and a registered three-outcome rule: "An inconclusive or refuting outcome is published with the same prominence as a supporting one." [S163 p. 6; pp. 1–2, 8, 27–28]; the outcome, reuse buys data but not speed or energy and only at large batch, leads the abstract [S163 pp. 1, 28].
  - The 2005 pump prescription re-tested inside SCIP: the source read with file and line at a pinned commit [S164 p. 9], the measured contrast the 2005 parts added to the implementers' weighted pump against that pump alone [S164 pp. 13–14], the outcome both ways with a null, a harmful fallback and a strong naive arm [S164 pp. 16–19], post hoc additions marked [S164 pp. 13–14], non-detection reported as imprecision [S164 p. 16].
  - The 1988 dominance procedure reopened, its obstacle to adoption conceded on p. 2, a tie-break criterion of the 1988 paper shown wrong by counterexample [S124 pp. 2, 6–8]; the revival runs through Salvagnin's 2005 master's thesis [S096 pp. 19, 27–28].
  - Self-correction in 2026: an implementation error of an earlier submission found, corrected and every dependent number recomputed [S150 pp. 10, 30]; his own branch-and-check of weeks earlier run frozen as published, plus a cutoff run that isolates the proof effort [S162 pp. 2, 13–16].
  - The 2003 local-branching design reopened by a learning study with the original as baseline (no implementation read) [S076 pp. 1–2, 6, 14, 17]; the 2018 side of the re-test already names its untuned rate [S133 pp. 2–3, 5].
- **Variants.** Early-career form: a scheme and conjecture of his Bologna co-authors re-examined, an outcome that cuts both ways [H001]; step 2 practised in 2009 on the earlier pump's source code to port a restart rule [S041 p. 11]; an erratum of their own 1998 definition [S047 p. 50]; the 1992 and 1997 codes with Toth re-run in the 2002 survey (10 and 5 years on) against the newest rival on a common machine [S056 pp. 31, 34–39]; a failure printed that becomes the next study [S064 p. 14]; old devices handed to students with new tools, a revival rather than a re-test [S130 pp. 4, 13; S168 p. 4]; the re-test apparatus aimed at another author's fresh claim [S161 pp. 2, 4].
- **Corrections.** (i) The skill's practice line lists FP 2.0 among the works that dropped the 2005 prescription; the 2026 text does list FP 2.0 among the later works that did not carry cutoff and recovery together, but says it "mentioned it in passing", and keeps "dropped the objective altogether" for others, the co-authored Boosting FP among them [S164 p. 2]. The correction is to the word, not to the category: it does not mean that FP 2.0 kept the prescription. (ii) The limitation *FP 2.0 itself used the static cutoff the 2026 study measures as lossy* needs a nuance: FP 2.0's static bound z*(1 + β) is an evaluation device that grades instance difficulty, while the 2005 dynamic cutoff is only reviewed [S041 pp. 5, 14, 16]; the 2026 text does not say what cutoff FP 2.0 used [S164 p. 2]. (iii) *Through a master's thesis* rests on S096, not on S124, whose text does not mention a thesis [S124 pp. 2, 6–8; S096 pp. 19, 27–28].
- **Say–do update.** ✅ stated (2026, sole author) and practised; the 2008–2010 dominance revival and the 2026 re-tests are the core cases.
- **Proposed text.** Apply corrections (i)–(iii); add the 2026 self-corrections (S150, S162) to the practice line.

| # | Skill claim (section) | Full texts | Change |
|---|---|---|---|
| 3 | Method 5 practice: FP 2.0 listed among the works that dropped the 2005 prescription | FP 2.0 "mentioned it in passing"; Boosting FP "dropped the objective altogether" [S164 p. 2]; both are among the later works that did not carry cutoff and recovery together | Correct the wording, not the category |
| 4 | Method 5 limitation: FP 2.0 used the static cutoff the 2026 study measures as lossy | The static bound z*(1 + β) is FP 2.0's device for grading instance difficulty; the dynamic cutoff is only reviewed [S041 pp. 5, 14, 16]; the 2026 text does not say which cutoff FP 2.0 used [S164 p. 2] | Rephrase as an evaluation device |
| 5 | Method 5 practice: Pruning Moves revives the 1988 procedure *through a master's thesis* | S124 does not mention a thesis [S124 pp. 2, 6–8]; S096 names Salvagnin's 2005 master's thesis [S096 pp. 19, 27–28] | Cite S096 for the thesis |

### Counts

Cards: 11 evidence, 8 variant, 0 contradiction; works 11 / 8 / 0; read in full or part 10 / 7 / 0; deep evidence works by period 0 / 4 / 1 / 5 (08 §2).

### Added in T3.6

- **Evidence block**: Stated, the MBP26 quote (the FPC26 quote moved to the Before block); Practice [S163 p. 6; pp. 1–2, 8; S164 pp. 9, 16–19; S124 pp. 2, 6–8; S150 pp. 10, 30]; Say–do *✅ stated (2026, sole author) + practised 2008–2026*; four bullets: corrections (i)–(iii) of 08 §2.5 [S164 p. 2; S041 pp. 5, 14, 16; S096 pp. 19, 27–28] and the earlier forms [S056 pp. 31, 34–39; S041 p. 11].
- **Step 6**: catalog EP21. **Limitations**: *FP 2.0 itself used the static cutoff the 2026 study measures as lossy* → *FP 2.0's static cutoff only graded difficulty* [S041 pp. 5, 14].
- **Review fix**: bullet 1 reworded; the T3.6 draft *FP 2.0 did not drop the 2005 prescription* inverted S164 p. 2, which lists FP 2.0 among the later works that did not carry cutoff and recovery together. The thesis bullet moved to the Corrections list; the earlier-forms bullet is dated (the 1997 code re-run 5 years on) and names Toth; the Limitations clause *FP 2.0's static cutoff only graded difficulty [S041 pp. 5, 14]* is dropped as a repeat of bullet 2; Practice adds the outcomes: reuse buys data but neither speed nor energy, and only at large batch [S163 pp. 1, 28]; the pump re-test printed with a null and a harmful fallback [S164 pp. 16–19]. The T3.6 bullets were:

```markdown
  - ✗ FP 2.0 did not drop the 2005 prescription: the 2026 text says it "mentioned it in passing" and puts the co-authored Boosting FP among those that "dropped the objective altogether" [S164 p. 2].
  - ✗ The master's thesis behind Pruning Moves (Salvagnin, 2005) is named in *Just MIP it!* [S096 pp. 19, 27–28], not in Pruning Moves.
  - ⚠ Earlier forms: his 1992 and 1997 codes re-run ten years later against the newest rival [S056 pp. 31, 34–39]; old source code read in 2009 to port a rule [S041 p. 11].
```
- **Moved out** (kept below): the old practice line, with *through a master's thesis* (now cited to S096), *lists his own FP 2.0 among the works that dropped the 2005 prescription* (corrected), the 2022 learned neighbourhood size (now in the local-branching anatomy [S076 pp. 1–2]) and the arXiv pointers (in the Sources appendix). The DOI of the 1988 dominance paper (abstract-level card S104) stays in the Practice line.

### Before T3.6 (moved verbatim)

```markdown
### Method 5: Re-test your own old claim, and publish whichever way it falls
**One line**: Treat your own published prescriptions as open: find those the field adopted in part or that rest on an untuned baseline, read what the code really does, re-measure, and publish the restoration or the reversal. (New.)
**Evidence**:
- Stated: 7 or more sources (02 R13). [2026, sole author] "The objection is correct, and it is a methodological one, not a conceptual one: the criticism is not that the idea is wrong but that the 2018 evidence could not tell." (MBP26 p.2). [2026, AI-assisted] "Our recommendation is therefore not a new heuristic but an old one, restored." (FPC26 p.19).
- Practice: "Pruning Moves" (DOI 10.1287/ijoc.1090.0329) revives his 1988 dominance procedure with Toth (DOI 10.1016/0167-6377(88)90025-9) through a master's thesis; local branching's fixed neighbourhood size is learned per instance in 2022 (DOI 10.1609/aaai.v36i4.20294); the 2026 pump study (unreviewed; code DOI 10.5281/zenodo.22810777) reads SCIP's pump with line numbers at a pinned commit and lists his own FP 2.0 among the works that dropped the 2005 prescription; the 2018 minibatch claim (arXiv 1806.07353) is re-tested under pre-registration (arXiv 2609.13922) and finds no gain in speed or energy.
- Say–do consistency: ✅ stated + practised.
**Steps**:
1. List old claims of three kinds: a prescription implementers dropped; a result with a less carefully tuned baseline; a claim under a standing objection.
2. Read the implementation, not papers about it; cite file and line at a pinned commit.
3. Concede a methodological objection in the first pages and design the re-test to answer exactly it.
4. Keep the implementers' default as one arm.
5. Publish the outcome either way; mark what was added after the design was fixed.
6. 🔴 If the re-test cannot separate the effect from a nuisance factor, report it as inconclusive, not negative (a registration rule, MBP26 p.8).
**Applies to stage**: after publication, choosing the problem.
**Different from standard practice**: old claims are usually defended or left alone; here one's own literature is a source of problems.
**Limitations**: a **senior strategy** (early-career version: re-test a claim of your thesis or group, or a prescription implementations dropped). The strongest cases are 2026, unreviewed and AI-assisted; FP 2.0 itself used the static cutoff the 2026 study measures as lossy; no published reply to an outside critic was found (05 §13.7).
```

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it, word for word in fenced blocks (links as written in SKILL.md, relative to the skill folder). The shortened lines are in SKILL.md.

*Practice:*

```markdown
- Practice: the 2018 minibatch claim re-tested against the 2019 untuned-baseline objection under a registered three-outcome rule, "An inconclusive or refuting outcome is published with the same prominence as a supporting one." [S163 p. 6; pp. 1–2, 8], and the outcome, reuse buys data but neither speed nor energy and only at large batch, leads the abstract [S163 pp. 1, 28]; the 2005 pump prescription re-tested inside SCIP, its source read at a pinned commit, the outcome printed both ways, with a null and a harmful fallback [S164 pp. 9, 16–19]; his 1988 dominance procedure with Toth (DOI 10.1016/0167-6377(88)90025-9) reopened, a 1988 criterion shown wrong by counterexample [S124 pp. 2, 6–8]; an implementation error of an earlier submission corrected, every dependent number recomputed (2026) [S150 pp. 10, 30].
```

*Variant bullet 1 (wording):*

```markdown
  - ✗ Wording: the 2026 text does not say FP 2.0 dropped the prescription; among the later works that did not carry cutoff and recovery together it says FP 2.0 "mentioned it in passing", and it puts the co-authored Boosting FP among those that "dropped the objective altogether" [S164 p. 2].
```

*Variant bullet 3 (earlier forms):*

```markdown
  - ⚠ Earlier forms: the 1992 and 1997 codes with Toth, re-run in the 2002 survey (10 and 5 years on) against the newest rival [S056 pp. 31, 34–39]; old source code read in 2009 to port a rule [S041 p. 11].
```

<a id="method-6"></a>

## Method 6: Ask the solver first: MIP it as a quick shot, measure the potential, stop when it works

### Full-text evidence (08 §2 and §2.6, copied)

| Method | Cards E / V / C | Works E / V / C | Deep E / V / C | Deep E by period | Say–do after the full texts |
|---|---|---|---|---|---|
| M6 Ask the solver first | 75 / 27 / 4 | 60 / 25 / 4 | 58 / 25 / 4 | 1 / 23 / 29 / 5 | ✅ 2003–2026; ✗ in the pre-2002 problem-specific codes; reversed moves in 2025–2026 |


- **Strongest practice.**
  - The signal before the turn: "This shows that the state-of-the-art general-purpose ILP solvers are competitive with the best exact algorithms for SCP presented in the literature, and that their performance can sensibly be improved by an external preprocessing procedure." [S003 p. 9].
  - Steps 2–3: one linear constraint around black-box CPLEX 7.0 [S001 pp. 3–5, 9–10]; neighbourhoods as constraints around the unchanged solver, general codes under 2,000 lines against about 6,000 for the problem-specific one [S064 pp. 3–5, 12]; separation as an auxiliary MIP over the multipliers [D003 pp. 3–5; S033 pp. 3–4, 7; S083 pp. 3, 9]; "In a sense, we are using here the approach of “MIPping the dominance test” (i.e., of modeling it as a MILP)" [S124 p. 5]; branching priorities from a set-covering model passed to the default solver [S063 pp. 1, 3–6]; "Our first quick shot": the model written to a file and solved by black-box CPLEX [S067 pp. 9–10]; one bound and route fixings on the unchanged solver after measuring it in two settings with ten seeds [S059 pp. 4–7, 11]; one plugged-in separator solving open instances [S011 pp. 11–12; S195 pp. 21–22]; a bilevel solver as an add-on that touches only the node case the solver cannot handle, "What do we need to add to the MILP solver to handle a MIBLP?" [S194 p. 10; pp. 10–11, 18; S016 pp. 6, 11, 21; S027 pp. 4, 9, 11]; restricted MILPs as the sub-decisions of a matheuristic [S123 pp. 5–7; S117 pp. 2–3, 14, 16; S130 p. 13].
  - Stated (joint): MIPping of crucial decisions defined [S142 pp. 1, 9–11]; the principle behind step 2 and slow MIP separation moved to time-limited preprocessing [S096 pp. 1–2, 8–10, 20]; an exact MIP solver inside a heuristic "may appear naive at first glance, but it turns out to be effective" [S145 p. 10], and the stock solver in command mode is often all that is needed [S145 pp. 14–15].
  - Step 4 (measure the potential first): the closure's ceiling before any fast separator [D003 pp. 6–8; S033 pp. 9–10; S118 pp. 12–13]; a relaxation's potential as a go or no-go [S115 pp. 3–4]; a break-even from a published study, "As a consequence, a speedup of 2x in the FSB implementation would suffice to make it be the fastest option—at least, in the considered SCIP environment." [D012 p. 2]; ideal-oracle ceilings [D017 pp. 14–15]; a best-of-k-seeds table [S055 p. 3]; a census of the roundings a cutoff loses [S164 pp. 3–6].
  - The order of the 2025 ODS talk, in print in 2026 (EJOR, online 2025): monolithic CPLEX, then its built-in Benders to screen splits, then a specialized Benders in callbacks [S144 pp. 4–8, 12]; the 2026 model first given to Gurobi as is [S143 pp. 18, 21, 23, 32].
  - Step 5 (state the black box's limit): "While the choice of the ILP model is essential for the success of our method, it should also be pointed out that solving the basic ILP model by a default algorithm is by no means sufficient to reach reasonable results." [S014 p. 24]; "It appears clear, however, that the MIP approach (as described) is unlikely to be useful for solving to proven optimality nesting instances of practical size." [S046 p. 13]; full integration of backdoor branching would need complete access to the solver's source code [S063 pp. 1, 11]; the costs of wrapping the solver named: effort lost on time-limited nodes [S001 p. 16], two LPs that need better integration [S007 p. 9], an LP solver that stops at its first optimal vertex [D009 p. 8], a callback version that never updates the solver's incumbent [S154 pp. 4–5]; the delivered tool drops the MIP for a GRASP [S082 pp. 12–13, 19].
- **Variant: keep what an expensive call produced (step 5, a third option).** Besides dropping the auxiliary MIP or moving it to preprocessing, the record keeps each call's by-products: a successful auxiliary MILP stored as a pruning move checked cheaply at every node [S124 pp. 9–10, 13]; every strong-branching LP updates all candidates it informs [D012 pp. 3–4]; fractional points of interrupted runs become covering rows, and pseudocosts are read for free [S063 pp. 5–6]; a failed CGLP leaves a certificate that skips later disjunctions [D014 p. 19]; the solver's root cuts on follower MILPs are appended across a decomposition boundary [S090 pp. 16, 18]; routes from LKH-3 runs are pooled and recombined by a set-partitioning MIP [S130 pp. 4, 12–13; S168 pp. 3–5].
- **Other variants.** Before 2002 the general solver is mostly an LP engine or a referee [S004 pp. 21, 25; H003 pp. 5, 12], once a competitive baseline in the 2000 set-covering survey [S003 p. 9]; the separation sub-decision written as an integer program but solved by linear algebra modulo k [S139 pp. 3–4, 10; S058 pp. 3–4, 19]; a propagation engine written from scratch [S041 pp. 5, 11–14]; 2025: sub-MIPs forbidden and the finished method moved into a commercial solver [S126 pp. 3, 8, 19, 24, 26]; 2026: whether the solver is needed at all, answered by reading its optimal solutions [S161 pp. 1–2]; exhaustive GPU enumeration instead of an auxiliary MIP [S162 pp. 12–13]; the solver's source patched [S164 pp. 2, 9, 19].
- **Contradictions (dated, before 2002).** In the problem-specific crew, routing and railway codes no general-purpose MIP solver is run, not even as a baseline [S012 pp. 9, 11; S017 pp. 8–16, 21; S013 pp. 18, 22, 26; S002 p. 9]; consistent with the skill's Trajectory. This holds for those codes, not for the period: where a general solver appears before 2002 it is an LP engine or a referee for bounds (Other variants, [S004 p. 21]), and the 2000 set-covering survey runs CPLEX and MINTO and finds them competitive [S003 p. 9].
- **Say–do update.** ✅ stated and practised 2003–2026 (the time-window paper [S144], EJOR 2026, was online in 2025); not practised in the pre-2002 problem-specific codes; reversed in 2025–2026.
- **Proposed text.** Add the step-5 variant above; cite S144 as the primary source of *the 2025 order*; add S003 p. 9 as the 2000 signal to the Trajectory row 2002–2009.

### Counts

Cards: 75 evidence, 27 variant, 4 contradiction; works 60 / 25 / 4; read in full or part 58 / 25 / 4; deep evidence works by period 1 / 23 / 29 / 5 (08 §2).

### Added in T3.6

- **Evidence block**: Stated, the VV06 quote (the CORS15 Occam quote moved to the Before block); Practice [S001 pp. 3–5, 9–10; S124 p. 5; D003 pp. 6–8; S033 pp. 9–10; S144 pp. 4–8, 12], S144 now the primary source of *the 2026 order* (formerly *the 2025 order*, 06 §3.1; S144 is EJOR 2026, online 2025); Say–do *✅ stated + practised 2003–2026; ✗ in the pre-2002 problem-specific codes; reversed moves in 2025–2026* (formerly *practised to 2018; in 2026 he patches solver source instead*); four bullets: the pre-2002 problem-specific codes [S012 pp. 9, 11; S013 pp. 18, 22, 26], with the solver as an LP engine or a referee [S004 p. 21] and the 2000 survey that finds CPLEX and MINTO competitive [S003 p. 9], the step-5 variant (catalog DM21) [S124 pp. 9–10, 13; D012 pp. 3–4], 2025 [S126 pp. 3, 8, 24, 26], 2026 [S164 pp. 2, 9, 19; S162 pp. 12–13].
- **Step 2**: catalog DM1, DM7. **Step 4**: the closure's ceiling [D003 pp. 6–8]. **Step 5**: moved to preprocessing [S096 pp. 8–10] (after review the by-products option stays only in the ⚠ variant bullet, since 08 §4 rates it ✗ on say–do and on exclusivity); the black box's limit stated as the lesson [S046 p. 13], in the paper's words: "It appears clear, however, that the MIP approach (as described) is unlikely to be useful for solving to proven optimality nesting instances of practical size." [S046 p. 13].
- **Limitations**: the costs of wrapping the solver named in the papers [S001 p. 16; D009 p. 8].
- **Review fix**: bullet 1 rewritten; the T3.6 draft *Before 2002 no general-purpose solver run, not even as a baseline [S012 pp. 9, 11; S013 pp. 18, 22, 26]; the turn is signalled in 2000 [S003 p. 9].* turned a per-work contradiction into a claim about the period, which S003 p. 9 and S004 p. 21 contradict; step 5 drops *or keep its by-products*; *the 2025 order* → *the 2026 order* and Say–do 2003–2026 (S144 is EJOR 2026).
- **Moved out** (kept below): the old practice pointers (Chvátal closure on 2-matching problems, DOI 10.1007/s10107-006-0054-8; the vanilla bilinear code, DOI 10.1016/j.ejor.2019.09.043) and the CORS15 quote.

### Before T3.6 (moved verbatim)

```markdown
### Method 6: Ask the solver first: MIP it as a quick shot, measure the potential, stop when it works
**One line**: See what the general-purpose solver does with the model; hand it the critical sub-decision of your own algorithm as an auxiliary MIP; check the ceiling cheaply; stop elaborating when the first version works. (Deepened; step 1 is already known.)
**Evidence**:
- Stated: 02 R2 (11 or more sources) and R11. "Be smart as an engineer! Model the most critical steps in the design of your own algorithm through MIP models, and solve them (even heuristically) through a general-purpose MIP solver..." (VV06 PDF p.6); "Our very first implementation worked so well that we did not have an incentive to try and improve it #OccamPrinciple" (CORS15 PDF p.26).
- Practice: local branching as one linear constraint around black-box CPLEX 7.0 (DOI 10.1007/s10107-003-0395-5); MIP separation over the first Chvátal closure, begun on 2-matching problems (DOI 10.1007/s10107-006-0054-8); a vanilla bilinear code with intersection cuts implemented but unused (DOI 10.1016/j.ejor.2019.09.043); the 2025 order: CPLEX as a black box, then its built-in Benders, then a specialised Benders in callbacks (06 §3.1).
- Say–do consistency: ✅ stated + practised to 2018; in 2026 he patches solver source instead.
**Steps**:
1. Run the generic solver on the model as it is, then its built-in decomposition, only then your own callbacks.
2. Write the one critical sub-decision (which variables to fix, which cut to add, whether a node is dominated) as an auxiliary MIP and solve it with the same solver, even heuristically.
3. Test with the smallest code (one constraint, one callback); leave extras off; do not duplicate the solver.
4. Measure the potential first: how much gap would the ideal version close? (IPCO05 PDF pp.18-19.)
5. 🔴 Stop improving when the first version works; drop the auxiliary MIP, or move it to preprocessing, when it is too slow; if the black box cannot meet the requirement, state that as the lesson.
**Applies to stage**: choosing the problem, idea, executing.
**Different from standard practice**: the solver becomes the subroutine of its own heuristic, and the stop rule is part of the method.
**Limitations**: MIP-based separation was "exceedingly time consuming" as implemented (MIA06 PDF p.16); local branching and proximity search need binaries and an incumbent; local branching was beaten by RINS and DINS on its own instances (local-branching anatomy).
```

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it, word for word in fenced blocks (links as written in SKILL.md, relative to the skill folder). The shortened lines are in SKILL.md.

*One line:*

```markdown
**One line**: See what the general-purpose solver does with the model; hand it the critical sub-decision of your own algorithm as an auxiliary MIP; check the ceiling cheaply; stop elaborating when the first version works. (Deepened; step 1 is already known.)
```

*Practice:*

```markdown
- Practice: local branching as one linear constraint around black-box CPLEX 7.0 [S001 pp. 3–5, 9–10]; "In a sense, we are using here the approach of “MIPping the dominance test” (i.e., of modeling it as a MILP)" [S124 p. 5]; the closure's ceiling measured before any fast separator [D003 pp. 6–8; S033 pp. 9–10]; the 2026 order: monolithic CPLEX, its built-in Benders, then a specialized Benders in callbacks [S144 pp. 4–8, 12].
```

*Variant bullet 1 (pre-2002 codes):*

```markdown
  - ✗ In the problem-specific crew and routing codes before 2002 no general-purpose MIP solver is run [S012 pp. 9, 11; S013 pp. 18, 22, 26]; where one appears it is an LP engine or a referee for bounds [S004 p. 21]; in 2000 the set-covering survey runs CPLEX and MINTO and finds them competitive [S003 p. 9].
```

<a id="workflows"></a>

## Stage workflows and the Routing row

### Full-text evidence (techniques from 08 §7 and the cards; catalog ids)

- Workflow S step 2(a): the five curves (catalog EP31) [D009 pp. 7–11; S074 pp. 14–16].
- Workflow B: a neighbourhood as one linear constraint (DM1) [S001 pp. 3–5, 7]; separation as a MIP over multipliers (DM7) [D003 pp. 3–5; S033 pp. 4–7]; the ceiling before the separator, the best-of-k-seeds curve and ideal-oracle ceilings (EP18, EP33) [D003 pp. 6–8; S055 pp. 3, 6–7]; H11 and H12 from 08 §5 A and B.
- Workflow C: ten seeds with a success rule (EP17) [S041 pp. 14–15]; exit codes (EP25) [S074 pp. 12–13; D009 pp. 23–24]; tests for small studies (EP20) [S041 pp. 15, 17, 20; S126 p. 25; S150 pp. 14, 19].
- Workflow D step 3: zero-tolerance re-solve, the stress test, every solution re-read (EP27–EP29) [S055 p. 4; S011 p. 16; S195 p. 20; S164 pp. 11, 17].
- Workflow E: ideal-oracle ceilings [S055 pp. 6–7]; the predicted split read first and other splits labelled exploratory (08 §5 B step 5) [S164 pp. 14–15].
- Workflow F: what is not claimed first, null results in a section of their own (WM2, WM5) [S059 pp. 2–3; S164 pp. 1, 13, 16–19]; the checkpoint's 2009-to-2010 change [S174 pp. 1–2; S106 p. 1]; draft revision seen once, a 2015 report reframed for the journal with its numbers kept (WM8) [S195 pp. 1–2, 14, 18, 26].
- Workflow G: old devices handed to students with new tools [S130 pp. 4, 13; S168 p. 4]; the 2003 design reopened by a learning study [S076 pp. 1–2, 6, 14, 17].
- 08 §2.7 digest links: Workflow A (1 E), Workflow F checkpoint (1 E).

### Added in T3.6

- A pointer line under the section heading; Workflow S step 2(a) (EP31); Workflow B steps 1–3, checkpoint and output (DM1, DM7, H11, H12, EP18, EP33); Workflow C steps 1–2 (EP17, EP25, EP20); Workflow D step 3 (EP27–EP29); Workflow E steps 1–3 (ceilings, the predicted split, *→ M3 step 4* for the folded H6); Workflow F step 2, checkpoint and output (WM2, WM5, WM8); Workflow G step 2 [S076 pp. 1–2; S130 pp. 4, 13]. Workflow A unchanged; no new workflow (08 supports none).
- Research Task Routing, review row: *M3, M4 steps 1-7, H6, H7* → *M3, M4 steps 1-7, H7, H12*.
- **Review fix**: Workflow S step 2(a) points to the plots of Method 2 step 1; Workflow C step 2 cites catalog EP22 and EP23 for *03 PE-26* and EP24 for *03 PE-25*, pointers into a note the user may not open; Workflow D step 1 adds controlled conditions first (08 §5 C): optima known by construction [S046 pp. 12–13], a class whose closure theory proves to be the integer hull [S033 p. 8], the component in its pure form [D009 p. 1]; the Workflow F checkpoint names Salvagnin.

### Before T3.6 (moved verbatim)

Research Task Routing, review row:

```markdown
| "Is this result good?" "Review these tables" (theirs or a paper's) | Workflow E plus the swap test | M3, M4 steps 1-7, H6, H7; for a review, list each flaw with the step it fails, not a verdict |
```

Workflows S, B, C, D, E, F and G:

```markdown
### Workflow S: Stuck-project triage
**Input**: code exists, but the bound, the incumbent or the gain over the baseline has stopped improving.
**Steps**:
1. Ask the solver again (→ M6 step 1): current stock solver in default mode, then its built-in decomposition, on the plain model and the hardest instances. If it matches the user's code, go to the Workflow A checkpoint.
2. Name the stall, take one method: (a) a cut or Benders bound crawls at the root → M2 steps 1-3 on one small instance; (b) no or poor incumbent → M6 step 2, after checking which stock heuristics are on; (c) a small or uneven gain → M3 steps 1-3; (d) huge or symmetric instances → M1 steps 1-3.
3. Before adding anything, switch off one at a time every ingredient added since the last working version (→ M1 step 5).
**🔴 Checkpoint (his stop rules)**: stop and write the lesson (→ H7) if the stock solver matches the project, the gain stays within the placebo spread (M3 step 5), or the black box cannot meet the requirement (M6 step 5). Otherwise the record has nothing on abandoning a topic: say so (Activation Rules) and label further advice "not Fischetti-style".
**Output**: the stall type (a-d) and one diagnostic run with its decision rule; nothing more until its result is in.
```

```markdown
### Workflow B: Generating the idea
**Input**: the failure and sub-decision.
**Steps**:
1. Write the sub-decision as an auxiliary MIP (→ M6), or ask whether the model can be thinned instead (→ M1).
2. Try the opposite of the field's reflex (→ H1); move one piece of the last working method (→ H2); borrow a cure from where the pattern is solved (→ H3).
**🔴 Checkpoint**: before coding a separator or neighbourhood, estimate what the ideal version could gain.
**Output**: a one-constraint or one-callback test and a ceiling estimate.

### Workflow C: Designing the experiment
**Input**: two or more arms and a candidate test set.
**Steps**:
1. M4 steps 1-6, then M3 steps 1-3 (spread, placebo arm, seeds in the table).
2. Name the aggregates: shifted geometric mean with its shift, primal integral, performance profiles (03 PE-26); nodes and iterations on a loaded workstation, deterministic ticks on a shared cluster (03 PE-25).
**🔴 Checkpoint**: the swap test (M4 step 7) before the runs; after them, a gain within the placebo or seed spread is no result (M3 step 5).
**Output**: a protocol with arms, classes, exclusions with reasons, seeds, metrics and budgets, fixed before the variants run.

### Workflow D: Executing and debugging
**Input**: the protocol and the code.
**Steps**:
1. Vanilla version first, extras implemented but off (03 PE-14); traces on one or two instances before any table (→ H8).
2. When something stalls, instrument a toy instance and look at the loop (→ M2).
3. Validate cuts and solutions independently, with conservative tolerances where cut validity is at stake (→ H10); when the code works, subtract (→ M1 step 5).
**🔴 Checkpoint**: a failed validity test, or a primal value on the wrong side of the dual bound, stops the campaign; results from before the fix are not mixed with later ones.
**Output**: a log per run, the surviving ingredients, what was switched off.

### Workflow E: Judging the result
**Input**: tables and traces.
**Steps**:
1. Traces on one or two instances before any aggregate (→ H8); compare the gain with the placebo spread (→ M3); print failures, ties, the rival's wins and where the method does not pay (easy instances).
2. Separate an established result from a lead, declared comparisons from post hoc ones, and write the lesson (→ H7); for a selection rule ask only for positive correlation (→ H6).
**🔴 Checkpoint**: if the result cannot be told from a nuisance factor, report it as inconclusive.
**Output**: a claim sentence, a paragraph on what the study does not show, a lesson.

### Workflow F: Writing and presenting (thinner evidence)
**Input**: the result and the lesson.
**Steps**:
1. Present at a small workshop first (→ H8); post slides and preprints as dated records.
2. Give the implementation its own section, in the solver's actual interface; close with lessons learned (→ H7).
**🔴 Checkpoint**: if the scheme has a prior author, rewrite the framing and credit it (his 2009-to-2010 change on the in-out loop).
**Output**: talk, preprint, paper. Not documented: draft revision, splitting the writing, answering referees.

### Workflow G: After publication
**Input**: critiques, new solver versions, new tools.
**Steps**:
1. Name the drawback, adopt the critic's fix as the new baseline, work with the critics (→ H9).
2. Re-test old claims; hand old ideas to students with new tools (→ M5).
**🔴 Checkpoint**: a correct methodological objection is conceded in the first pages of the next paper.
**Output**: a follow-up study, not a reply (some critiques stay unanswered, 05 §13.7).
```

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it, word for word in fenced blocks (links as written in SKILL.md, relative to the skill folder). The shortened lines are in SKILL.md.

*Stage Workflows pointer line:*

```markdown
(full evidence and the pre-synthesis wording: references/research/09-evidence-ledger.md#workflows)
```

*Workflow S step 2:*

```markdown
2. Name the stall, take one method: (a) a cut or Benders bound crawls at the root → M2 steps 1-3 on one small instance (the plots of M2 step 1; catalog EP31 [D009 pp. 7–11]); (b) no or poor incumbent → M6 step 2, after checking which stock heuristics are on; (c) a small or uneven gain → M3 steps 1-3; (d) huge or symmetric instances → M1 steps 1-3.
```

*Workflow F checkpoint:*

```markdown
**🔴 Checkpoint**: if the scheme has a prior author, rewrite the framing and credit it (the 2009-to-2010 change on the in-out loop, with Salvagnin [S174 pp. 1–2; S106 p. 1]).
```

<a id="heuristic-1"></a>

## Heuristic 1: Invert the reflex

### Full-text evidence (08 §2.7, copied)

- **H1 Invert the reflex.** Symmetry exploited, not broken [S067 pp. 3, 12–13]; dual degeneracy used to pick the cleanest vertex [S074 pp. 2, 5–6]; the field's mixture of strong branching and pseudocosts refused, "so as to be forced to find valid alternatives" [D012 p. 2]; the defect turned into the mechanism, overfitting a fixed trained network or a minibatch on purpose [S008 p. 6; S133 pp. 1–2]; the belief that maximal equal spacing is safest overturned [S100 pp. 2, 4, 13]; as a closing lesson rather than a starting hypothesis [S022 p. 16].

### Added in T3.6

- *In print: symmetry exploited [S067 pp. 3, 12–13]; dual degeneracy used [S074 pp. 2, 5–6].*

### Before T3.6 (moved verbatim)

```markdown
1. **Invert the reflex.** Take the opposite of a field reflex (break symmetry, average variability away, strengthen the model, trust the fractional point) as one study's hypothesis. Case: "Step 1: don't break my symmetries!" (NEW11 PDF p.4); "Don't trust the fractional point!" (ISCO14 PDF p.18). It can fail (the orbital-shrinking bound, M1).
```

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it, word for word in fenced blocks (links as written in SKILL.md, relative to the skill folder). The shortened lines are in SKILL.md.

*Heuristic 1:*

```markdown
1. **Invert the reflex.** Take the opposite of a field reflex (break symmetry, average variability away, strengthen the model, trust the fractional point) as one study's hypothesis. Case: "Step 1: don't break my symmetries!" (NEW11 PDF p.4); "Don't trust the fractional point!" (ISCO14 PDF p.18). It can fail (the orbital-shrinking bound, M1). In print: symmetry exploited [S067 pp. 3, 12–13]; dual degeneracy used [S074 pp. 2, 5–6].
```

<a id="heuristic-2"></a>

## Heuristic 2: Move one piece

### Full-text evidence (08 §2.7, copied)

- **H2 Move one piece.** Feasibility moved from constraints into the objective [S085 pp. 1–2, 4]; the pump's distance moved into the LP objective [S007 p. 3]; the objective into a constraint and robustness into the objective [S010 pp. 4–5]; each branching variant moves one piece [D012 pp. 3–5]; a test-set move moved from improving to fathoming [S124 p. 23]; overfitting control moved from objective to constraints [S109 pp. 3, 18].

### Added in T3.6

- The pump case gets its card [S007 p. 3].

### Before T3.6 (moved verbatim)

```markdown
2. **Move one piece.** A new heuristic is the previous one with one requirement moved between constraints and objective. Case: the pump as local branching with the distance moved into the LP objective; proximity search as its dual (03 PE-08).
```

<a id="heuristic-3"></a>

## Heuristic 3: Name the pattern, borrow the cure

### Full-text evidence (08 §2.7, copied)

- **H3 Borrow the cure.** Constraint propagation from CP [S041 pp. 2, 9]; nogoods and test sets [S124 pp. 2–3, 9]; backdoors from AI and resolution search [S063 pp. 2–3]; intersection cuts into bilevel optimization [S027 pp. 4, 12]; relax-dualise-reformulate from min-max regret [S090 p. 5]; the Lagrangian-dual analogy for the Benders loop [S195 pp. 14–15]; a solved twin problem supplies model and solver [S100 pp. 2, 5–7].

### Added in T3.6

- CP propagation in FP 2.0 [S041 pp. 2, 9]; the Benders master as Lagrangian dual minimization [S195 pp. 14–15].

### Before T3.6 (moved verbatim)

```markdown
3. **Name the pattern, borrow the cure.** A module that works and then gets stuck: where is that pattern solved? Case: "We need a META-SCHEME for cut generation !" (CPA10 PDF p.23); CP propagation in FP 2.0.
```

<a id="heuristic-4"></a>

## Heuristic 4: Application first, general method after

### Full-text evidence (08 §2.7, copied)

- **H4 Application first.** Soft fixing in TURNI became local branching [S001 pp. 3–4]; a partner's application defines a new class [S101 pp. 3–6, 14]; the public-challenge version on QAPLIB [S067 p. 2]. Variant, the reverse order: generalize the class, then win on the special cases' own benchmarks [S027 pp. 3–4, 20–24; S090 pp. 5, 18–24; S092 pp. 2, 6–7, 19] (three 2018 papers with Ljubić, Monaci and Sinnl; Inner Tension 5).

### Added in T3.6

- The TURNI case gets its card [S001 pp. 3–4]; the reverse order as a dated variant [S027 pp. 3–4, 20–24]. The public-challenge version on QAPLIB [S067 p. 2] stays in the ledger.

### Before T3.6 (moved verbatim)

```markdown
4. **Application first, general method after.** Win on real instances with a specific code, then restate the trick for any MIP. Case: soft fixing on TURNI became local branching (01 SW1). Early-career version: a public challenge.
```

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it, word for word in fenced blocks (links as written in SKILL.md, relative to the skill folder). The shortened lines are in SKILL.md.

*Heuristic 4:*

```markdown
4. **Application first, general method after.** Win on real instances with a specific code, then restate the trick for any MIP. Case: soft fixing on TURNI became local branching [S001 pp. 3–4]. Early-career version: a public challenge. Reverse order (2018, one group): generalize the class, win on its special cases' benchmarks [S027 pp. 3–4, 20–24].
```

<a id="heuristic-5"></a>

## Heuristic 5: The baseline a practitioner would run (folded into Method 4 step 2)

### Why folded

08 §5, copied: Two new heuristics pass *executable plus at least one more check* and add a rule the skill does not state (A, B). Three updates extend existing items instead of adding new ones (C–E). The skill already has ten heuristics, the top of the framework's 5–10 range. Two of them duplicate method steps: H5 (*the baseline a practitioner would run*) is Method 4 step 2 almost word for word and has no card link, and H6 (*positive correlation is enough*) is already invoked inside Method 3 step 4. Folding H5 and H6 into those steps would keep the list at ten with A and B; the editing step decides.

The rule now stands in Method 4 step 2, with cards: both emphasis settings [S001 p. 12]; the rival's settings searched after "extensive experiments and contacts with ILOG-Cplex staff" [S007 p. 6]; the joint textbook presents re-aiming the stock solver by parameters (heuristic mode) as the first resort, before programs and callbacks [S145 pp. 14–15]. SKILL.md keeps the item's number with a pointer, so that references to Heuristic 5 still resolve.

### Before T3.6 (moved verbatim)

```markdown
5. **The baseline a practitioner would run.** Include the solver's own heuristic setting and ask how to tune it (vendor documentation without contacts; 01 SW2).
```

<a id="heuristic-6"></a>

## Heuristic 6: Positive correlation is enough (folded into Method 3 step 4)

### Full-text evidence (08 §2.7, copied)

- **H6 Positive correlation is enough.** "Therefore, one has to content him/herself with a criterion that gives a positive correlation between the selected run and those that a posteriori behave better than the average." [S055 p. 2]; outside randomized restarts an ideal oracle beats a cheap score only slightly and random sorting loses about 10% [D017 p. 15].

### Why folded

The item was already invoked inside Method 3 step 4 (08 §5). The rule now stands there with its EURO12 phrase and the paper's cards [S055 pp. 2, 5–6]; the limit to selection inside randomised restarts is kept, and outside them an ideal oracle beats a cheap score only slightly [D017 p. 15]. Workflow E and the Routing row now point to Method 3 step 4.

### Before T3.6 (moved verbatim)

```markdown
6. **Positive correlation is enough.** For a selection rule that cannot be perfect: "what we are looking for is just a positive correlation with the a-posteriori best run" (EURO12 PDF p.19). Keep it to selection inside randomised restarts.
```

<a id="heuristic-7"></a>

## Heuristic 7: Close with a lesson and a status label

### Full-text evidence (08 §2.7, copied)

- **H7 Lesson and status label.** From 1996 to 2026 [S022 p. 16; S067 p. 7; S046 pp. 2, 13–14; S054 pp. 1, 12; S100 p. 2; S133 pp. 1–2; S164 pp. 6, 15, 19]; say first what is not claimed [S059 pp. 2–3]. Dated contradictions: no conclusions and no lesson in two 1997–1998 papers [S005 p. 29; S009 pp. 21–22].

### Added in T3.6

- *From 1996 [S022 p. 16; S067 p. 7].* The 08 contradictions (no conclusions and no lesson in two 1997–1998 papers [S005 p. 29; S009 pp. 21–22]) stay here. *Say first what is not claimed* [S059 pp. 2–3] went to Workflow F (catalog WM2).

### Before T3.6 (moved verbatim)

```markdown
7. **Close with a lesson and a status label.** Label claims as computational conjecture, lead or post hoc. Case: "Lesson learned: in most practical cases the inequalities of rank 1 already give a very tight approximation" (MIA06 PDF p.14); "a lead and not an established result" (FPC26 p.19).
```

<a id="heuristic-8"></a>

## Heuristic 8: Talk first, traces before tables

### Full-text evidence (08 §2.7 and §5 C, copied)

- **H8 Traces before tables.** One-instance traces open the papers [S074 pp. 3, 14–16; S195 pp. 15–18; S011 p. 13; S164 pp. 4–5]; Aussois premieres [S001 p. 2; S007 p. 2]. Variant: an early version at a large conference (EURO XIII, 1994) [S009 p. 3].

**C. Controlled conditions first (widens Method 2 step 4 and H8; not a new item)**

Known-answer test beds built by construction [S046 pp. 12–13; S198 p. 52]; a class where theory says the closure is the integer hull [S033 p. 8; D003 pp. 5–6]; an example whose cuts are known to be facets, to show that the failure lies in handling, not in the family [S112 p. 7]; toy ILPs whose CGLP vertices are enumerated [S068 pp. 9–12, 15–17]; the smallest instance with an obvious answer [S100 pp. 10–14]; the component in its pure form, "Our reason for studying them is our belief that these negative properties can be understood and thus remedied only based on a thorough investigation of such procedures in their pure form." [D009 p. 1; S106 pp. 2–4]; synthetic distributions and frozen trees before any real parallel run [D017 pp. 9–15]; a frozen trajectory that every variant sees [S098 p. 18; S052 pp. 21–22]; the controlled oracle of the yoyo manuscript [S174 pp. 6–7].

### Added in T3.6

- [S001 p. 2; S074 p. 3; S195 pp. 15–18]. 08 §5 C widens this item and Method 2 step 4; it adds no new item.
- **Review fix**: 08 §5 C now stands in Workflow D step 1 (known answers before real instances) and Method 2 step 4 (the controlled oracle, [S174 pp. 6–7]).

### Before T3.6 (moved verbatim)

```markdown
8. **Talk first, traces before tables.** Premiere at a small workshop; show traces on one or two instances before any aggregate (Aussois premieres 2002-2016; 03 PE-11, PE-12).
```

<a id="heuristic-9"></a>

## Heuristic 9: Name the drawback first, adopt the critic's fix

### Full-text evidence (08 §2.7, copied)

- **H9 Adopt the critic's fix.** The objective pump taken as the state of the art and second base [S041 p. 16]; the 2026 measured contrast adds the 2005 parts to that pump [S164 pp. 13–14].

### Added in T3.6

- The objective pump as the state of the art in FP 2.0 [S041 p. 16]; in 2026 the 2005 parts added to that pump [S164 pp. 13–14].

### Before T3.6 (moved verbatim)

```markdown
9. **Name the drawback first, adopt the critic's fix.** Case: cycling named in the 2005 pump paper; the objective pump taken as state of the art in FP 2.0; "Boosting the feasibility pump" (DOI 10.1007/s12532-014-0068-9), joint with Boland, Eberhard, Engineer, Savelsbergh and Tsoukalas, after four of them had recast the pump as a proximal method whose restarts escape non-integral local minima (DOI 10.1137/110823596; 05 Q2).
```

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it, word for word in fenced blocks (links as written in SKILL.md, relative to the skill folder). The shortened lines are in SKILL.md.

*Heuristic 9:*

```markdown
9. **Name the drawback first, adopt the critic's fix.** Case: cycling named in the 2005 pump paper; the objective pump taken as state of the art in FP 2.0 [S041 p. 16]; "Boosting the feasibility pump" (DOI 10.1007/s12532-014-0068-9), joint with Boland, Eberhard, Engineer, Savelsbergh and Tsoukalas, after four of them had recast the pump as a proximal method whose restarts escape non-integral local minima (DOI 10.1137/110823596; 05 Q2); in 2026 the 2005 parts are added to that pump [S164 pp. 13–14].
```

<a id="heuristic-10"></a>

## Heuristic 10: Validate what the solver will not re-check

### Full-text evidence (08 §2.7 and §5 D, copied)

- **H10 Validate what the solver will not re-check.** The cut-validity stress test, 10,000 perturbations [S011 p. 16; S195 p. 20]; ε-validity tied to the LP solver's tolerance after Margot [S074 pp. 9–11]; the solver's symmetry handling and dual reductions switched off for correctness [S067 p. 11; S097 pp. 18–19]; tolerances tightened and the solver's wrong answers counted against an exact enumeration [S101 pp. 12, 16–17]; every solution re-read by a separate solver process on the original model [S164 pp. 11, 17]. Extension in §5.

**D. Numerically safe by construction (extends H10)**

H10 checks a posteriori; the record also designs validity in: a cutoff 2cᵀx ≤ 2U − 1 that is tight at no integer point and a lexicographic simplex by reoptimizations instead of a perturbed objective [D009 pp. 4–5, 15, 19]; cut validity tied to the LP solver's reduced-cost test with a conservative ε and integer arithmetic [S074 pp. 10–11]; separation at y* + 2ε, which keeps cuts valid and helps plain Kelley, and a strengthening skipped near 0 and 1 [S011 p. 12; S195 pp. 13–14]; intersection-cut coefficients computed from the original data, so that numerical error only weakens the cut [S016 pp. 18–21; S079 pp. 7–8], with his decks naming tableau accuracy as the risk [S194 pp. 19–20; S190 pp. 9–10]; floating-point facets checked in exact arithmetic and an oracle recomputed by an independent LP [S143 pp. 16, 24].

### Added in T3.6

- The stress test [S011 p. 16]; every solution re-read [S164 pp. 11, 17]; the extension *design validity in* (catalog DM26, DM27) with the cutoff tight at no integer point [D009 p. 15]. Filed as an extension of this item, not a new heuristic (08 §5 D and §10 item 11).
- **Review fix**: the pointer *03 PE-29*, into a note the user may not open, is replaced by its catalog entry, EP28 (the cut-validity stress test) [S011 p. 16].

### Before T3.6 (moved verbatim)

```markdown
10. **Validate what the solver will not re-check.** Case: the incumbent fixed, perturbed and separated 10,000 times after each run, after Margot (DOI 10.1007/s12532-009-0003-7) (03 PE-29); in 2026 every solution file re-read by a fresh solver.
```

<a id="heuristic-11"></a>

## Heuristic 11: Let the search model be wrong; keep the judge exact (new)

### Full-text evidence (08 §4 row A and §5 A, copied)

| Cluster | Works (full or part) | 1 Cross-project | 2 Say–do | 3 Executable, non-standard | 4 Exclusive | Decision |
|---|---|---|---|---|---|---|
| A. Let the search model be wrong; keep the judge exact | 9: S198/S046, D004/S018, S010, D007, S154, S059, S150, S164, S015 | ✅ nesting 2004–09, robustness 2007–09, wind 2014 and 2026, rescheduling 2017, the pump 2026 | ✅ sole-author statement [S164 p. 8]; joint statements [S018 p. 9; S150 pp. 1, 9] | ✅ steps in §5; differs from searching on the most faithful model | ✗ partial: approximate-then-repair and screen-then-confirm are common, and S150 credits multi-fidelity precedents [S150 pp. 3, 6]; overlaps Method 1 step 2 and Method 4 step 1 | Heuristic (§5 A) |

**A. Let the search model be wrong; keep the judge exact and out of the search's reach (proposed H11)**

- **Rule.** Give the search a cheaper or deliberately invalid model and decide acceptance, and the reported quality, with an exact model that the search never calls.
- **Steps.**
  1. Write down the judge first: the original constraints and objective, an exact repair LP, or an external simulator that shares no code with any optimizer [S018 pp. 2, 9–11; D004 pp. 6–7; S010 pp. 7, 15; S150 p. 9].
  2. Put the invalid or simplified guidance only into the search: a cutoff in the projection LP, "The second sees only the constraints of the model and its objective; it is the certificate, and correctness rests on it alone." [S164 p. 8]; a possibly invalid bound on one aggregate variable that the solver's presolve propagates [S059 p. 6]; an interference-free model in a first phase [S154 p. 9]; simplified geometry [S046 pp. 14–21]; frozen precedences that make every model an LP [D004 pp. 2, 4]; a distilled surrogate for screening [S150 pp. 20–21].
  3. Send every candidate through the judge: test and completion LP [S164 p. 7]; fix the combinatorial choices, solve the exact LP, drop the worst item if it fails [S046 pp. 22–23; S198 pp. 61–63]; score with the true objective and switch to the full model when the relaxed one stops improving it [S154 p. 9]; confirm the head of a ranked list with the trusted model [S150 pp. 20–21].
  4. Loosen an invalid restriction only when the solver proves it infeasible, on a ladder fixed in advance [S059 pp. 6, 8].
  5. Report the judge's verdict, the surrogate's distance to the full model over the whole trade-off range [S018 pp. 12, 14–15, 17], and judge sample points drawn independently of every search [S150 pp. 15–16, 31]; "the fidelity of a wake model is not the quality of the layouts optimized under it" [S150 p. 1].
- **Checks.** Cross-project ✅; say–do ✅ (stated 2026, practised 2004–2026); executable ✅; exclusivity partial (§4).
- **Limits.** The judge must be trusted: the reference is one closure on one mesh [S150 p. 10]; a repair can fail and costs items [S046 pp. 22–23]; the price of the simplification has to be measured where the full model is tractable [S018 pp. 18–20].
- **Stages.** Idea, executing, judging. Ties to Method 1 step 2 (weaker model for heuristics) and Method 4 step 1 (shared machinery).

### Added in T3.6

- New item 11 with its rule, the S164 p. 8 quote, an external validator [S018 p. 9] and an exact repair LP [S046 pp. 22–23]; overlap with Method 1 step 2 and Method 4 step 1 stated. Exclusivity is partial (08 §4), so it is a heuristic, not a core method. Catalog DM17, DM18 and EP4 carry its steps.
- **Review fix**: the item leads with the pre-2026 practice [S018 p. 9; S046 pp. 22–23] and tags the S164 quote *stated in 2026 (AI-assisted drafting declared)* [S164 p. 25].

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it, word for word in fenced blocks (links as written in SKILL.md, relative to the skill folder). The shortened lines are in SKILL.md.

*Heuristic 11:*

```markdown
11. **Let the search model be wrong; keep the judge exact** (new). Give the search a cheaper or invalid model; decide acceptance and reported quality with an exact model it never calls: an external validator [S018 p. 9]; an exact repair LP [S046 pp. 22–23]; stated in 2026 (AI-assisted drafting declared): "The second sees only the constraints of the model and its objective; it is the certificate, and correctness rests on it alone." [S164 p. 8]. Overlaps M1 step 2, M4 step 1.
```

<a id="heuristic-12"></a>

## Heuristic 12: Mechanism first (new)

### Full-text evidence (08 §4 row B and §5 B, copied)

| Cluster | Works (full or part) | 1 Cross-project | 2 Say–do | 3 Executable, non-standard | 4 Exclusive | Decision |
|---|---|---|---|---|---|---|
| B. Mechanism first: say where the device should win before the runs | 7: S014, S074, S052, S029, S143, S164, S161 | ✅ 2006–2026 | ✅ sole-author [S164 pp. 3–4]; S161 is weak, its design being the assistant's [S161 p. 4] | ✅ | ✗ partial: subgroup reading is common; the predicted-class and probe-arm form is less so; overlaps Method 2's diagnosis and Method 3's controls | Heuristic (§5 B) |

**B. Mechanism first: say where the device should win before the runs (proposed H12)**

- **Rule.** Before the campaign, write down the mechanism by which the device acts and the instance class where it predicts a gain or a loss; read the results first on that class; probe the mechanism with a cheap intervention.
- **Steps.**
  1. Name the mechanism: the relaxation grip of a proximity objective [S052 p. 5]; "the loss is a matter of support rather than of weights: a weighted objective term discourages such a point, whereas a cutoff removes it from the polyhedron." [S164 p. 3]; the point that defeats a relaxation, constructed before any strengthening [S143 pp. 11–13].
  2. Turn it into an a priori criterion that sorts problem classes, and say that it is heuristic [S164 pp. 3–4].
  3. Test where the method's nature should win, and say so [S052 pp. 20–22].
  4. Probe: an intervention the explanation predicts should help partly, and a deliberately wrong variant [S074 pp. 8, 16].
  5. Read the predicted split as the test and label other splits exploratory [S164 pp. 14–15].
  6. When a component's effect flips sign across instance groups, find the instance statistic that explains the flip [S014 pp. 20, 23–24].
  7. When a rival wins unexpectedly, switch its components off one at a time with a control that removes the obvious confound, then transplant the ingredient [S029 pp. 3, 7–14; p. 15].
- **Checks.** Cross-project ✅ (2006–2026); say–do ✅ (stated in his sole-author 2026 text; the skill's Mentor Voice already carries his deck question asking why a method that works does work); executable ✅; exclusivity partial (§4).
- **Limits.** The probe run of S074 is described but its results are not reported [S074 p. 16]; the criterion of S164 is stated as heuristic [S164 p. 3]; reading an optimum and replacing the solve by its rule [S161 pp. 1–2] is the assistant's design by the note's own account [S161 p. 4].
- **Stages.** Experiment design, judging. Complements Method 3 (attribution by controls) and H7 (declared against post hoc).

### Added in T3.6

- New item 12 with its rule, the S164 p. 3 quote, the probe arm [S074 pp. 8, 16] and the test placed where the method's nature should win [S052 pp. 20–22]. Partial exclusivity (08 §4); S161 is weak evidence, its design being the assistant's [S161 p. 4]. Workflow B step 3 and Workflow E step 2 use it.
- **Review fix**: the item leads with the pre-2026 practice [S074 pp. 8, 16; S052 pp. 20–22] and tags the S164 quote *stated in 2026 (AI-assisted drafting declared)* [S164 p. 25].

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it, word for word in fenced blocks (links as written in SKILL.md, relative to the skill folder). The shortened lines are in SKILL.md.

*Heuristic 12:*

```markdown
12. **Mechanism first** (new). Before the runs, write down how the device acts and where it should win or lose; read that class first; probe the mechanism cheaply: a deliberately wrong variant as probe [S074 pp. 8, 16]; tests where the method's nature should win [S052 pp. 20–22]; stated in 2026 (AI-assisted drafting declared): "the loss is a matter of support rather than of weights: a weighted objective term discourages such a point, whereas a cutoff removes it from the polyhedron." [S164 p. 3].
```

<a id="misreadings"></a>

## Common misreadings

### Full-text evidence (08 §3, copied)

| # | Skill claim (section) | Full texts | Change |
|---|---|---|---|
| 12 | Common Misreading 4: the in-out loop presented as new in 2009, credited in 2010 | Confirmed [S174 pp. 1–2, 7–8, 12–13; S106 pp. 1–2]; precursor in 2000–2001, a point between x* and two incumbents separated first and credited to Reinelt [S125 pp. 11–12; S057 p. 20] | Add the precursor |
| 13 | Common Misreading 5: the 2005 pump had a cutoff with a recovery LP | True [S007 p. 11], but evaluated only in two approximate-LP variants on 26 instances; the basic pump stops at its first solution [S007 pp. 6, 10–13]; in 2007 the cutoff variants are reported as inferior to the pump followed by local branching or RINS [S026 p. 18]; the authors themselves describe local branching as a heuristic approach whose strategy is exact in nature [S085 pp. 2–3] | Add the nuance |
| 23 | Common Misreading 2: adoption into solvers is the authors' statement | Further self-reports: CBC and GLPK implementations of proximity search [S052 p. 23]; a CPLEX uptake resting on a private communication [D012 pp. 9, 13]; one bound-tightening method part of CPLEX 12.6.1 [S029 pp. 15–16]; a 2025 method moved into a commercial solver [S126 pp. 24, 26] | Add as further self-reports |

### Added in T3.6

- Misreading 2: further self-reports [S052 p. 23; D012 pp. 9, 13; S029 pp. 15–16]. Misreading 3: the key ingredient [S011 p. 12]. Misreading 4: [S174 pp. 1–2, 7–8; S106 p. 1] and the 2000–01 precursor [S125 pp. 11–12]. Misreading 5: [S001 pp. 5, 11; S007 p. 11], the cutoff evaluated in two approximate-LP variants on 26 instances [S007 pp. 6, 10–13], reported inferior in 2007 [S026 p. 18]. The authors themselves describe local branching as a heuristic approach whose strategy is exact in nature [S085 pp. 2–3] (08 §3 item 13).
- **Review fix**: Misreading 4, *His own precursor* → *A precursor in his joint work with Lodi and Toth* (S125 is by Fischetti, Lodi and Toth).

### Before T3.6 (moved verbatim)

```markdown
## Common Misreadings

1. **"He is Paolo Toth's doctoral student."** The Mathematics Genealogy Project has no record of him and Toth's page lists seven students without him; a Bologna mentorship is plausible, the advisor is not established ([06 §2.1](references/research/06-trajectory.md)).
2. **"His heuristics sit inside the solvers as he published them."** SCIP's pump is Achterberg and Berthold's objective pump (DOI 10.1016/j.disopt.2006.10.004) with FP 2.0's propagation rounding; stand-alone local branching and proximity search are off in SCIP (both run inside its ALNS, DOI 10.1007/s12532-021-00209-7). Adoption into CPLEX, CBC and GLPK is the authors' own statement; no release note was checked ([05](references/research/05-peer-critique.md) §2.3-§4).
3. **"His Benders contribution is better cut selection."** By the 2017 paper's account the stabilised root loop is the key ingredient; his 2025-26 lectures blame the loop more than the cuts (M2).
4. **"The in-out cut loop is his invention."** The 2009 *yoyo search* manuscript presented it as new; the 2010 paper credits Ben-Ameur and Neto (DOI 10.1002/net.20137) (01 C3).
5. **"Local branching is a primal heuristic."** The 2003 paper presents an exact *strategic* branching scheme around a *tactical* black-box solver (01 SW1). Likewise the 2005 pump did not ignore the objective: it had a cutoff with a recovery LP (01 SW2).
```

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it, word for word in fenced blocks (links as written in SKILL.md, relative to the skill folder). The shortened lines are in SKILL.md.

*Misreading 4:*

```markdown
4. **"The in-out cut loop is his invention."** The 2009 *yoyo search* manuscript presented it as new [S174 pp. 1–2, 7–8]; the 2010 paper credits Ben-Ameur and Neto (DOI 10.1002/net.20137) (01 C3) [S106 p. 1]. A precursor in his joint work with Lodi and Toth: a 2000–01 code separated a point between x* and the two best incumbents first, crediting Reinelt [S125 pp. 11–12].
```

<a id="anatomy-benders"></a>

## Anatomy: Redesigning Benders decomposition for large-scale facility location

### Full-text evidence (cards S011 and S195; 08 §3, copied)

- Read in full: the author preprint of February 11, 2016 [S011] and the report of April 1, 2015 [S195]; one study, counted once. Origin: a sound Lagrangian code is far from trivial, so a simpler approach on an off-the-shelf solver [S011 p. 19; S195 p. 26]; the working hypothesis that old decomposition schemes need a redesign [S011 pp. 1–2]; the report's entry is the Steiner thinning-out: "Recent experience with the Steiner Tree Problem [9] showed that some known MILP models can be “thinned out” by removing unnecessary variables and constraints, with a very significant performance boost." [S195 p. 2].
- Quick shot: one plugged-in separator in stock CPLEX 12.6 solved the open instances 2500-10 and 3000-100 in under 15 minutes each [S011 p. 11]; both texts add that better results need more ingredients [S011 p. 11; S195 p. 13]. The full recipe (branch-up-first, the stabilized loop, the heuristics) then needs 824.76 s and 225.25 s (Table 1) [S195 pp. 21–22].
- Loop: "This is perhaps the most important ingredient in our recipe." [S011 p. 12]; the in-out constants and resets (catalog DM10) [S011 pp. 12–13; S195 p. 15]; on gs250a-1 all three loops call the same separator; Kelley stopped after 15,000 s at the root, in-out took 0.19 s for the root with 748 cuts and finished at 0.41 s (fat); 0.04 s with 4 cuts, finished at 0.06 s (slim) [S011 pp. 13–14]; the same numbers in the 2015 report [S195 pp. 15–17]. "Evidently, one can design a sound cutting plane loop even with very weak/dense cuts, provided that the “Kelley’s curse” is escaped and a different cutting plane scheme is adopted." [S195 p. 14].
- Fat or slim per cost class by measurement [S011 p. 14]; no real bundle method [S011 p. 12]; the validity stress test, which caught tolerance issues in earlier versions [S011 p. 16; S195 p. 20].

| # | Skill claim (section) | Full texts | Change |
|---|---|---|---|
| 22 | Method 2 limitation: one showcase instance since 2016 | The gs250a-1 traces are already in the April 2015 report [S195 pp. 15–17] | *since 2015* |

### Added in T3.6

- Card pages on Origin, Why then, Key insight (with the S011 p. 12 quote), Minimum evidence, Fat or slim, Abandoned paths, Methods shown (H10 added) and the 2015 dating.
- **Review fix**: Minimum evidence separates the quick shot, under 15 minutes each [S011 p. 11], from the full recipe's 824.76 s and 225.25 s [S195 pp. 21–22]; the draft gave those times to the first separator.

### Before T3.6 (moved verbatim)

```markdown
### Redesigning Benders Decomposition for Large-Scale Facility Location (Manag. Sci. 2017, DOI 10.1287/mnsc.2016.2461; with Ljubić and Sinnl)

| Dimension | Content |
|---|---|
| Origin | [joint] Old decomposition schemes deserve a redesign on current software; a sound Lagrangian code was far from trivial, so a stock solver was tried |
| Why then | Callback branch-and-cut had made Benders one separator |
| Key insight | Project out the allocation variables; stabilise the root cut loop instead of following Kelley |
| Minimum evidence | A first separator in CPLEX 12.6 solved open UFLLIB instances 2500-10 and 3000-100 in under 15 minutes each. gs250a-1 (quadratic): Kelley stopped at the root after 15,000 s; in-out closed it in 0.19 s (fat), 0.04 s with 4 cuts (slim) (UFL17 pp.13-14) |
| Fat or slim | Per cost class, by measurement. Slim (one aggregated cost variable) is "a clear winner for the quadratic case": tight root bound, tiny LP, few nodes. Fat (one variable per customer) is much better for linear costs: a weaker root bound means many nodes, where Kelley's single cut per call recomputes bounds poorly (UFL17 p.14) |
| Abandoned paths | No bundle method; Kelley kept in the tree, as a better loop inside CPLEX was not immediate (M2 step 5); the first stabiliser was kept because it worked (his statement) |
| Reception | A later metaheuristic improved 12 upper bounds much faster (different aims); no reply found |
| Methods shown | M1, M2, M6. Unknown: who did what |
```

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it, word for word in fenced blocks (links as written in SKILL.md, relative to the skill folder). The shortened lines are in SKILL.md.

*Origin row:*

```markdown
| Origin | [joint] Old decomposition schemes deserve a redesign on current software; a sound Lagrangian code was far from trivial, so a stock solver was tried [S011 pp. 1, 19]; the 2015 report enters from the Steiner thinning-out [S195 p. 2] |
```

*Minimum evidence row:*

```markdown
| Minimum evidence | A first separator in CPLEX 12.6 solved open UFLLIB instances 2500-10 and 3000-100 in under 15 minutes each [S011 p. 11]; the full recipe needs 824.76 s and 225.25 s [S195 pp. 21–22]. gs250a-1 (quadratic): Kelley stopped at the root after 15,000 s; in-out closed it in 0.19 s (fat), 0.04 s with 4 cuts (slim) (UFL17 pp.13-14) [S011 pp. 13–14], already in the April 2015 report [S195 pp. 15–17] |
```

*Fat or slim row:*

```markdown
| Fat or slim | Per cost class, by measurement. Slim (one aggregated cost variable) is "a clear winner for the quadratic case": tight root bound, tiny LP, few nodes. Fat (one variable per customer) is much better for linear costs: a weaker root bound means many nodes, where Kelley's single cut per call recomputes bounds poorly (UFL17 p.14) [S011 p. 14] |
```

*Abandoned paths row:*

```markdown
| Abandoned paths | No bundle method [S011 p. 12]; Kelley kept in the tree, as a better loop inside CPLEX was not immediate (M2 step 5); the first stabiliser was kept because it worked (his statement) |
```

<a id="anatomy-local-branching"></a>

## Anatomy: Local branching

### Full-text evidence (card S001; 08 §3, copied)

- Read in full: the author preprint "May 2002, Revised December 2002" [S001]. The TURNI seed, 833 duties after 41 CPU minutes, 809 after 55 more [S001 p. 3]; the soft-fixing constraint, "Put in these terms, the question lends itself to a simple answer: just add to the MIP model a linear soft fixing constraint" [S001 p. 3]; the strategic and tactical levels [S001 p. 5]; the complementary branch imposed only after the left node is closed [S001 p. 7]; exact with finite dv_max [S001 p. 11]; the traces tr24-15 [S001 p. 6] and B1C1S1 [S001 p. 11]; 29 instances, k = 20, untuned, "In the previous experiments we deliberately avoided any fine tuning of the LocBra parameters." [S001 p. 13]; first on 23 of 29 [S001 p. 12]; REFINE switched off on arki001 [S001 pp. 10, 12]; effort lost on time-limited nodes [S001 p. 16]; the Aussois premiere [S001 p. 2]. The 2022 learning study keeps the original as baseline [S076 pp. 1–2, 6, 14, 17].

| # | Skill claim (section) | Full texts | Change |
|---|---|---|---|
| 16 | Local-branching anatomy: Aussois 2002 traces on seymour and arki001 | The paper's traces are tr24-15 and B1C1S1; the other anatomy figures (29 instances, k = 20, no fine tuning, first on 23 of 29, TURNI 833 → 809) match [S001 pp. 3, 6, 11–13] | Correct the trace instances or cite the deck |

### Added in T3.6

- Card pages on every row; the trace instances corrected (seymour and arki001, from 01 SW1, are not traced in the paper); the 2022 learned neighbourhood size added to Reception [S076 pp. 1–2].

### Before T3.6 (moved verbatim)

```markdown
### Local branching (Math. Program. 2003, DOI 10.1007/s10107-003-0395-5; with Lodi)

| Dimension | Content |
|---|---|
| Origin | [joint] *Soft fixing* on top of TURNI, a crew-scheduling heuristic, on a Netherlands Railways instance: TURNI stopped at 833 duties after 41 CPU minutes, soft fixing reached 809 after 55 more (01 SW1) |
| Why hard fixing failed | [joint] Which variables to fix is unclear; "Wrong choices at early levels are typically very difficult to detect, even when lower bounds are computed along the way": the bound stays quiet for several fixings, then jumps after an innocent-looking late one; feasible solutions appear only deep in the tree (LB02 PDF p.9) |
| Key insight | Fix how many binaries, not which: one linear constraint on the Hamming distance to the incumbent; the complementary branch keeps the scheme exact |
| Minimum evidence | Aussois 2002 traces on seymour and arki001; 29 instances unsolved in 5 hours, posted online, neighbourhood size fixed at 20, no fine tuning; first on 23 of 29 (01 SW1) |
| Limits conceded | Faster optimality proofs not guaranteed (left open); the refinement step switched off on a general-integer instance (01 F6) |
| Reception | Beaten by RINS and DINS on its own instances, per abstracts and citation contexts (05 Q4); in SCIP only inside ALNS (Misreading 2) |
| Methods shown | M6, H4. Unknown: the authors' shares |
```

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it, word for word in fenced blocks (links as written in SKILL.md, relative to the skill folder). The shortened lines are in SKILL.md.

*Why hard fixing failed row:*

```markdown
| Why hard fixing failed | [joint] Which variables to fix is unclear; "Wrong choices at early levels are typically very difficult to detect, even when lower bounds are computed along the way": the bound stays quiet for several fixings, then jumps after an innocent-looking late one; feasible solutions appear only deep in the tree (LB02 PDF p.9) [S001 p. 3] |
```

*Minimum evidence row:*

```markdown
| Minimum evidence | Aussois 2002 premiere [S001 p. 2]; the paper's traces are tr24-15 and B1C1S1 [S001 pp. 6, 11] (seymour and arki001, from 01 SW1, are not traced in it); 29 instances unsolved in 5 hours, posted online, neighbourhood size fixed at 20, no fine tuning; first on 23 of 29 (01 SW1) [S001 pp. 11–13] |
```

<a id="anatomy-pump"></a>

## Anatomy: The feasibility pump and its 2026 return

### Full-text evidence (cards S007, S085, S026, S164; 08 §3, copied)

| # | Skill claim (section) | Full texts | Change |
|---|---|---|---|
| 13 | Common Misreading 5: the 2005 pump had a cutoff with a recovery LP | True [S007 p. 11], but evaluated only in two approximate-LP variants on 26 instances; the basic pump stops at its first solution [S007 pp. 6, 10–13]; in 2007 the cutoff variants are reported as inferior to the pump followed by local branching or RINS [S026 p. 18]; the authors themselves describe local branching as a heuristic approach whose strategy is exact in nature [S085 pp. 2–3] | Add the nuance |
| 14 | Pump anatomy: random flips published instead of enumeration, which returned in 2007 | A preprint of 16 February 2004 already switches from the pump's almost-feasible point to enumeration by local branching [S085 pp. 1, 4] | Date the return to the 2004 preprint (published 2008) |
| 15 | Pump anatomy, minimum evidence: 37 hard 0-1 instances, one pump failure, CPLEX 8.1 18 and 8 | The revised paper reports 83 instances (44 MIPLIB 2003 plus 39 hard), a Pentium M notebook, 3 pump failures and 19 CPLEX root failures in the chosen setting (25, 41 and 33 in the others) [S007 pp. 1, 5–7] | Say which source the 37-instance figures come from (not in S007), or use the paper's |

- The basic pump stops at its first solution; the cutoff with its recovery LP is in §3.2 [S007 p. 11] and runs only in the variants FP1 and FP2 on 26 instances [S007 pp. 11–13]. The baseline: "As to ILOG-Cplex, after extensive experiments and contacts with ILOG-Cplex staff [23] we found that, as far as the time and quality of the root node solution is concerned, the best results are obtained (perhaps surprisingly) when the MIP preprocessing/presolve is not invoked" [S007 p. 6].
- The 2026 return: the headline comparison is marked as added after the design, in the abstract and in §6 [S164 pp. 1, 14]; twelve declared comparisons under Holm [S164 p. 13].

### Added in T3.6

- Card pages on Origin and Key insight; Minimum evidence now names its source (01 SW2) and gives the paper's own figures [S007 pp. 1, 5–7]; Abandoned paths dated to the 2004 preprint [S085 pp. 1, 4]; the 2026 row [S164 pp. 1, 13–14].
- **Review fix**: Origin tagged [joint] (the card cited is co-signed with Glover and Lodi); the 2026 row gives the outcome: added to SCIP's weighted pump, cutoff plus recovery is better on 116 and worse on 9 of the 176 instances (of 424) where it finds a solution, and the median final gap falls from 59% to 30%, in a comparison marked as added after the declared design [S164 p. 1].

### Before T3.6 (moved verbatim)

```markdown
### The feasibility pump (Math. Program. 2005, DOI 10.1007/s10107-004-0570-3; with Glover and Lodi), and its 2026 return

| Dimension | Content |
|---|---|
| Origin | [stated] Local branching and RINS need an incumbent, so the first feasible solution was the bottleneck; who had the core idea is unknown |
| Key insight | A point is feasible when it equals its own rounding: alternate rounding with an L1 projection |
| Minimum evidence | January 2004, a notebook, 37 hard 0-1 instances: the pump failed once, CPLEX 8.1 18 and 8 times in two settings |
| Abandoned paths | Random flips and restarts published instead of enumeration, which returned in 2007 (DOI 10.1016/j.disopt.2006.10.001) |
| Reception | Critiques of solution quality, cycling, lack of theory; a two-variable counterexample (DOI 10.1137/16M1095962) unanswered in print |
| 2026 return | Unreviewed, AI-assisted: cutoff-plus-recovery measured inside SCIP on MIPLIB 2017; a 116-win, 9-loss comparison was added after the declared design and says so; twelve declared comparisons under Holm's correction |
| Methods shown | M5, H2, H9 |
```

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it, word for word in fenced blocks (links as written in SKILL.md, relative to the skill folder). The shortened lines are in SKILL.md.

*2026 return row:*

```markdown
| 2026 return | Unreviewed, AI-assisted: cutoff-plus-recovery measured inside SCIP on MIPLIB 2017. Added to SCIP's weighted pump it is better on 116 and worse on 9 of the 176 instances (of 424) where it finds a solution, median final gap 59% → 30%; that comparison was added after the declared design and says so; twelve declared comparisons under Holm's correction [S164 pp. 1, 13–14] |
```

<a id="anatomy-erraticism"></a>

## Anatomy: Exploiting erraticism in search (new in T3.6)

### Full-text evidence (card S055)

- Read in full: the revised manuscript OPRE-2012-05-278(R), pp. 1–13, with Monaci [S055]. Entry: sensitivity to initial conditions is "generally viewed as a drawback", and the paper takes the opposite viewpoint; the observation is credited to Danna 2008 and its tie-breaking explanation to the MIPLIB 2010 paper [S055 p. 1]; SAT/CP restarts and the racing ramp-up of parallel MIP are the neighbouring lines, the idea made sequential and "not driven by the need of avoiding idle processors" [S055 pp. 1–2]. "Therefore, one has to content him/herself with a criterion that gives a positive correlation between the selected run and those that a posteriori behave better than the average." [S055 p. 2].
- The value of randomness measured first: 58 medium instances × 100 seeds with CPLEX 12.3; one extra run cuts nodes by about 40% in geometric mean, 100 runs by 7× (Table 1) [S055 pp. 3–4]; nodes and LP iterations reported instead of time because the workstation's load varied [S055 p. 3].
- Design: four ways to diversify as an external user, RAN3 re-optimising a copy of the first LP over the optimal face [S055 pp. 4–5]; eight short-run indicators in priority order, ties towards the unperturbed clone; C = 5 clones, N = 5 nodes [S055 pp. 5–7]; a hybrid that runs the default first [S055 pp. 8–10].
- Fairness: "For a fair comparison, all codes use a (possibly dummy) callback function, thus deactivating IBM ILOG Cplex’s proprietary dynamic search" [S055 p. 6]; classes by the larger node count of the two arms [S055 p. 7]; ideal-oracle ceilings "for benchmark purposes only" [S055 p. 7].
- Results: losses printed from 10 to 10,000 nodes (+140.3%, +83.5% and +53.0% time; the paper calls instances above 1,000 nodes hard, so the third loss is in a hard class), gains on the two largest classes (−28.5% and −17.9% time), 3 more instances solved [S055 pp. 8–9]; the method-versus-default table is one run per instance per arm [S055 pp. 6–9]; a usage rule for the losses, an on/off flag [S055 p. 8].
- Before claiming a new optimum: a zero-tolerance re-solve [S055 p. 4] (catalog EP27).

### Added in T3.6

- New anatomy: Origin, Minimum evidence, Key insight, Fairness and result, Methods shown (M3, M4, M6 step 4).
- **Review fix**: the result row lists the three losing classes and the two winning ones; the draft's *gains on hard ones (−28.5%)* gave only the best class [S055 pp. 8–9].

<a id="anatomy-gomory"></a>

## Anatomy: Gomory's cuts revisited (new in T3.6)

### Full-text evidence (cards S074 and D009)

- Read in full: the author version of "Lexicography and degeneracy: can a pure cutting plane algorithm work?" (Zanette first author, with Balas) [S074] and "On the enumerative nature of Gomory's dual cutting plane method" (Balas first author, with Zanette) [D009]; the IPCO 2008 version D006 is abstract-level.
- Entry: pure cutting-plane methods are typically not used in practice [D009 p. 1; S074 p. 1]; "Our reason for studying them is our belief that these negative properties can be understood and thus remedied only based on a thorough investigation of such procedures in their pure form." [D009 p. 1]; branching as a symptomatic cure, "From the cutting plane point of view, however, the cure is even worse than the disease, in that it hides the real source of the problems." [S074 p. 1].
- Diagnosis on stein15: bound and average cut coefficient, trajectories by multidimensional scaling and basis-determinant growth, cut depth, distance between consecutive separated points, right against wrong rounding [D009 pp. 7–11]; "This behavior is in a sense a consequence of the efficiency of the underlying LP solver, that has no reason to change the LP solution once it becomes optimal with respect to the original objective function" [D009 p. 8]; "As new degenerate vertices are created by the cuts themselves, the textbook method enters a feedback loop that is responsible for the exponential growth of the determinant of the current basis, as reported in Figure 4(d)." [S074 p. 14].
- Remedy: choose the lexicographically minimal optimal vertex, the Gomory cut unchanged [S074 pp. 5–6]; the lexicographic simplex by fixings and reoptimizations of the black-box LP solver [S074 pp. 6–7; D009 pp. 4–5]; the idea credited to the youngest coauthor [S074 p. 2]; ε-validity tied to the LP solver's optimality tolerance [S074 pp. 10–11]; a deliberately wrong rounding as contrast arm [S074 p. 8].
- Evidence and follow-up: stein15, stein27 and bm23 solved by pure cutting planes where the textbook method closes a tiny fraction of the gap [D009 p. 3; S074 p. 14]; the lexicographic method as an implicit enumeration [D009 p. 11]; cures borrowed from branch-and-bound, the cutoff 2cᵀx ≤ 2U − 1 tight at no integer point and a dynamic lexicographic order [D009 pp. 15, 19–21].
- Limits conceded: not competitive with branch-and-bound on most problems [S074 p. 2]; GMI cuts "intrinsically more difficult to handle than GFCs" [S074 p. 25]; results called preliminary [D009 pp. 1, 25]; one run per instance [D009 pp. 21–24].

### Added in T3.6

- New anatomy: Origin, Diagnosis, Key insight, Minimum evidence, Follow-up and limits, Methods shown (M2, H3, H10).

<a id="anti-patterns"></a>

## Research anti-patterns

### Full-text evidence (from the cards)

- Judging a cut family by the Kelley loop: "Evidently, one can design a sound cutting plane loop even with very weak/dense cuts, provided that the “Kelley’s curse” is escaped and a different cutting plane scheme is adopted." [S195 p. 14]; the loop's convergence "heavily depends also on the strategy for generating the next point to cut" [S011 p. 12]; Gomory's stall put on the LP solver and the loop, "This behavior is in a sense a consequence of the efficiency of the underlying LP solver, that has no reason to change the LP solution once it becomes optimal with respect to the original objective function" [D009 p. 8]. S195 and S011 count once (header), so the row cites D009 as its second work, with the VRL25 deck (PDF p.9) for his stated view.
- Comparing randomised variants on one run each: "As already discussed, random perturbations are a fundamental ingredient of the FP scheme, so it is not completely fair to compare different variants on a single run." [S041 p. 14]; the A/A null, "Its measured ratio to the baseline has true value one, so its dispersion across seeds tells the reader—and told us—how small a ratio this apparatus can honestly resolve." [S163 p. 2]; his stated view in the EURO12 deck (PDF p.14). Single runs in 18 co-authored works, several led by co-authors (Method 3); the T3.6 draft called them *his own lapse*.
- Tuning on the test set and dropping instances easy for the rival, in print: keeping such instances [S079 p. 16]; separate tuning and test sets [S078 pp. 8–9].

### Added in T3.6

- Two rows (Kelley-loop verdicts; single runs of randomised variants) and the in-print sources of the first row.
- **Review fix**: each new row cites his deck (VRL25 PDF p.9; EURO12 PDF p.14) and two distinct works in print, [S195 p. 14; D009 p. 8] and [S041 p. 14; S163 p. 2]; the draft's pair [S195 p. 14; S011 p. 12] was one study; *his own lapse in 18 works* → *single runs in 18 co-authored works*.

### Before T3.6 (moved verbatim)

```markdown
## Research Anti-patterns

| Anti-pattern | Why he opposes it (source) | Instead |
|---|---|---|
| Tuning on the test set; many parameters; dropping instances easy for the rival; a cut costing far more than the root LP | EURO12 PDF pp.5, 23 | Untuned settings, disjoint tuning set, swap test, budget tied to the baseline (M4) |
| Duplicating the solver | TRI16 PDF p.13 | MIP the sub-decision, default mode (M6) |
| Over-clever user cuts that slow the solver | ISMP18 PDF p.9 | Vanilla code, extras off |
| A speed-up claimed against a baseline tuned less carefully | MBP26 p.2 (his own 2018 preprint is the case) | Equal tuning care (M5) |
```

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it, word for word in fenced blocks (links as written in SKILL.md, relative to the skill folder). The shortened lines are in SKILL.md.

*Row: comparing randomised variants on one run each:*

```markdown
| Comparing randomised variants on one run each | EURO12 PDF p.14; in print [S041 p. 14; S163 p. 2] (single runs in 18 co-authored works, M3) | Seeds and a success rule (M3) |
```

<a id="trajectory"></a>

## Research trajectory, Latest and Academic Lineage

### Full-text evidence (08 §8 and §9, copied)

**8. Trajectory as seen in the full texts**

Primary topic of each work group, by period (counts of work groups at all read levels; S188 and S192 excluded).

| Period | Groups | Main topics (groups) |
|---|---|---|
| 1986–1990 | 12 | approximation and complexity 6; bounding and branch-and-bound for routing and scheduling 6 |
| 1991–1995 | 19 | polyhedral combinatorics 10; bounding and branch-and-bound 5; branch-and-cut codes 1; cutting planes 1; complexity 1; other applications 1 |
| 1996–2000 | 22 | railway and crew planning 6; polyhedral 4; branch-and-cut codes 4; statistical disclosure control 3; set covering heuristics 2; cutting planes 2; bibliography 1 |
| 2001–2005 | 18 | branch-and-cut codes 6; railway and crew 4; general-purpose primal heuristics 3; disclosure control 2; cutting planes 1; polyhedral 1; other applications 1 |
| 2006–2010 | 30 | cutting planes, closures and the cut loop 10; primal heuristics 5; railway robustness 4; Benders 3; robustness and uncertainty 2; other applications 2; tree search 1; branch-and-cut 1; polyhedral 1; editorial 1 |
| 2011–2015 | 16 | cutting planes and the cut loop 5; tree search, variability and parallelism 4; primal heuristics 4; symmetry 1; wind farms 1; survey 1 |
| 2016–2020 | 29 | machine learning from the MILP side 5; bilevel and interdiction 4; primal heuristics 3; Benders 3; other applications 3; books and surveys 3; nonlinear MIP 2; tree search 2; branch-and-cut 1; railway 1; symmetry 1; wind farms 1 |
| 2021–2026 | 16 | primal heuristics and matheuristics 5; wind farms 3; Benders and decomposition 3; other applications 3; machine learning 2 |

- **1986–1995, Bologna.** Approximation schemes and their worst-case analysis with Martello and Toth [H001; S039; S108; S141; S075], additive bounding and dominance for routing and scheduling [S049 pp. 4, 22; S031; S044; S099; S104], ATSP and Steiner polyhedra [S071; S089; S113; S062; S116; S030 pp. 5–6]. Almost all abstract-level (§11).
- **1996–2001, problem-specific codes for partners.** {0,1/2} and mod-k cuts [S022 pp. 5–10; S139 pp. 3–9]; routing branch-and-cut [S005; S009; S013; S057/S125]; Lagrangian codes for the Italian and Dutch railways [S012 pp. 9–11; S017 pp. 12–16; S004 pp. 5–14; S053 p. 9; S061 p. 9]; statistical disclosure control [H003; S069; S073; S180; S093]. No general-purpose solver as subroutine (Method 6 contradictions), but projection into cuts (§2.1), the in-out precursor (§2.2) and same-code ablation (§2.4) are already there.
- **Turn 1, 2000–2003: the solver becomes the subroutine.** The 2000 survey finds general-purpose ILP solvers competitive with special-purpose exact SCP codes [S003 p. 9]; the soft-fixing refiner of the crew code becomes one constraint on a generic MIP, "Put in these terms, the question lends itself to a simple answer: just add to the MIP model a linear soft fixing constraint" [S001 p. 3]; general codes are a third the size of the problem-specific one [S064 p. 12].
- **2002–2010, general-purpose devices.** Local branching, the pump and its general-integer and propagation versions [S001; S007; S026; S041], combinatorial Benders cuts [S006 pp. 1–7], MIPping closures and its variants [D003; S033; S142; S083; S134], {0,1/2}-cuts inside CPLEX [S070], the MIPping survey [S096]; robust railway timetabling with a separate validator [D004; S018; S010; D007].
- **Turn 2, 2008–2011: from the cut to the loop.** After component-side cures [D003 pp. 8–9; S112 pp. 2, 7–9; S024 pp. 2, 4] the loop becomes the object [S174 p. 1; S106 p. 2; D009 p. 8; S074 p. 14; S095 pp. 2–6].
- **2010–2016, tree search and variability.** Pruning moves, nonchimerical branching, backdoors [S124; D012; S063]; erraticism and sampling [S055; S094 p. 5]; self-splitting [S111; D017]; symmetry by aggregation [S067; D013]; proximity search [S052; S154; S086].
- **Turn 3, 2015–2018: thinning out and general-purpose solvers for harder classes.** The Steiner and UFL redesigns [S195 p. 2; S011; S040], bilevel and interdiction on top of a MILP solver [S016 p. 6; S027; S090; S038], machine learning seen from the MILP side [S109; S054; S008; S133; D018].
- **2019–2025, applied Padova MIP and students.** Vehicle routing with set-partitioning recombination [S130; S168], learning in local branching [S076], wind farms and distancing with Martina Fischetti [S078; S100], fix-propagate-repair into a commercial solver [S126 pp. 24, 26], time-window TSP with Benders [S144; S172].
- **Turn 4, September–November 2026: re-tests and the apparatus.** Sole-author re-tests of his own 2005 and 2018 claims [S164; S163], two-author wind-farm preprints with a trusted judge and certificates [S143; S150; S162], an AI-written note [S161 p. 4]; pre-registration [S163 pp. 8–9], declared families with Holm's correction [S164 p. 13], replication packages [S164; S186; S187].
- **What stayed constant.** The relaxation drives the heuristic, from Lagrangian costs in 1997–2001 [S012 p. 10; S004 pp. 5–14] to the LP point and the relaxation grip of 2005–2016 [S007 p. 3; S052 p. 5; S086 p. 2]; ablation by removal from 1995 to 2025 [S060 p. 11; S126 pp. 24–25]; same-machinery comparisons from the 1990s [S060 p. 11; S077 p. 10] to the dummy callback [S070 p. 10] and the 2026 harnesses [S164 pp. 11, 13]; the closing lesson from 1996 to 2026 [S022 p. 16; S164 p. 19]; cures borrowed from neighbouring fields (§2.7, H3); instances made public from 2001 [S013 p. 22; S125 pp. 24–25].

**9. Collaboration pattern**

Coauthors named on the cards, counted over work groups (S154 counted separately here; S188, S192 excluded; editors counted as coauthors).

| Period | Groups | Sole-author | Most frequent coauthors (groups) |
|---|---|---|---|
| 1986–1990 | 12 | 3 (H001, S141, the thesis S185) | Toth 7, Martello 4, Carpaneto 2, Dell'Amico 1 |
| 1991–1995 | 19 | 4 (S071, S089, S128, S116) | Toth 7, Balas 4, Martello 2, Caprara 2, Salazar González 2 |
| 1996–2000 | 22 | 0 | Toth 9, Caprara 8, Vigo 5, Salazar González 5, Guida (FS) 3 |
| 2001–2005 | 18 | 0 | Toth 6, Lodi 6, Salazar González 4, Caprara 2, Kroon (NS) 2 |
| 2006–2010 | 30 | 1 (S173, abstract) | Salvagnin 7, Lodi 5, Monaci 4, Zanette 3, Balas 2, Bertacco 2, Caprara 2 |
| 2011–2015 | 17 | 0 | Monaci 9, Salvagnin 4, Zanette 3, Lodi 3, Balas 2, Martina Fischetti 2 |
| 2016–2020 | 29 | 4 (S109; S152; the books H005, S088) | Monaci 13, Salvagnin 10, Sinnl 8, Ljubić 7, Lodi 3, Martina Fischetti 2 |
| 2021–2026 | 16 | 4 (S161, S163, S164; S165 metadata) | Martina Fischetti 5, Roberti 4, Salvagnin 3, Cavaliere 3 |

- **Shape.** A Bologna start with Toth and Martello, then Caprara, Vigo and Salazar González on partner codes; Lodi bridges 2001–2010; Salvagnin, Monaci and Zanette carry the general-purpose and cut-loop work; Ljubić and Sinnl the 2015–2019 Benders, Steiner and bilevel line [S011; S040; S016]; Martina Fischetti, Roberti and Cavaliere the 2020s. Totals over all periods: Toth 32 groups, Monaci 27, Salvagnin 24, Lodi 18, Caprara 14, Salazar González 12, Balas 11, Martina Fischetti 9, Martello 9.
- **Partners and settings.** Ferrovie dello Stato planners as coauthors [S012; S053; S081]; Netherlands Railways [S061; S034; S015]; a Siemens Nixdorf application [S013 p. 3]; Alstom instances [S059 p. 2]; EU and national projects [S180 p. 1; H003; S041 p. 21; S016 p. 40].
- **Students.** Thesis material enters papers (§3 item 20) [S096 pp. 19, 27–28; S046 p. 2; S154 p. 2; S109 pp. 4, 8, 14–15]; student coauthors [S133 p. 1; D018; S110; S130; S168]; supervised theses abstract-level [S192; S188].
- **Authorship.** "We" cannot be split; in one 2014 paper he is fourth of six and the text refers to Fischetti and Salvagnin in the third person [S098 p. 18]; alphabetical lists [S040; S059; S097].
- **2026.** Mostly sole-author or with Martina Fischetti; AI assistants declared as drafters, coders and adversarial readers [S164; S143 p. 27; S150], in one note as the main executor [S161 p. 4]; one re-test carries no AI statement [S163].

| # | Skill claim (section) | Full texts | Change |
|---|---|---|---|
| 19 | Latest: 2026 preprints with declared AI assistants | Declared in S143 [S143 p. 27], S150 [S150], S161 [S161 p. 4] and S164; S163 carries no statement on AI assistance [S163]; in S161 the assistant did everything but the idea and the supervision [S161 p. 4] | *Most of them declare AI assistants* |
| 20 | Academic Lineage: master's theses became co-authored papers (inferred) | Salvagnin's thesis into a 2009 chapter [S096 pp. 19, 27–28]; a 2003 dissertation into a 2009 paper, supervision not stated [S046 pp. 2, 34]; Martina Fischetti's thesis into a 2014 paper [S154 p. 2]; variant: a 2012 master's thesis into a sole-authored paper that credits the student in the text [S109 pp. 1, 4, 8, 14–15, 19] | Confirmed, with the variant |

### Added in T3.6

- **Turns in the full texts** (a paragraph under the table, pointing to `06-trajectory.md` §9): [S069 pp. 3, 5–6; S003 p. 9; S001 p. 3; S174 p. 1; D009 p. 8; S195 p. 2; S163 pp. 8–9; S164 p. 13]; constants [S012 p. 10; S052 p. 5; S060 p. 11; S126 pp. 24–25]. The S003 p. 9 quote in full: "This shows that the state-of-the-art general-purpose ILP solvers are competitive with the best exact algorithms for SCP presented in the literature, and that their performance can sensibly be improved by an external preprocessing procedure." [S003 p. 9]. The table rows are unchanged.
- **Latest**: *declared AI assistants* → *in most, declared AI assistants* [S143 p. 27], one doing all but idea and supervision [S161 p. 4], none declared in one re-test [S163] (08 §3 item 19).
- **Academic Lineage**: the thesis-to-paper pipeline confirmed [S096 pp. 19, 27–28; S154 p. 2], once into a sole-authored paper crediting the student [S109 pp. 1, 4] (08 §3 item 20).
- **Review fix**: in SKILL.md the Turns paragraph is replaced by a pointer to 06 §9.2, which holds the same turns; its T3.6 wording:

```markdown
**Turns in the full texts** (06 §9): 1996–2001 partner codes already project into cuts [S069 pp. 3, 5–6]; 2000–03 the solver becomes the subroutine [S003 p. 9; S001 p. 3]; 2008–11 from the cut to the loop [S174 p. 1; D009 p. 8]; 2015–18 thinning out [S195 p. 2]; 2026 re-tests and a declared apparatus [S163 pp. 8–9; S164 p. 13]. Constant: the relaxation drives the heuristic [S012 p. 10; S052 p. 5]; ablation by removal 1995–2025 [S060 p. 11; S126 pp. 24–25].
```

### Before T3.6 (moved verbatim)

```markdown
## Research Trajectory

| Period | Main direction | Trigger | Representative work |
|---|---|---|---|
| 1982-1993 | Bounding, routing (Bologna) | Bologna PhD | DOI 10.1287/opre.37.2.319 |
| 1989-2006 | Branch-and-cut for routing; railway codes | Balas; Ferrovie dello Stato competitions | DOI 10.1287/moor.16.1.42 |
| 2002-2009 | General-purpose MIP heuristics | Mature black-box solvers (stated) | Local branching; feasibility pump |
| 2008-2012 | Gomory's cuts revisited | "Looking inside Gomory" | DOI 10.1007/s10107-009-0335-0 |
| 2010-2016 | Erraticism, sampling | Seed-only swings in CPLEX 12.2 (stated) | DOI 10.1287/opre.2013.1231 |
| 2014-2020 | Thinning out: Benders, Steiner, bilevel | DIMACS 2014 (stated) | DOI 10.1287/mnsc.2016.2461 |
| 2015-2022 | Machine learning from the MILP side | Implementation argument; students | DOI 10.1007/s10601-018-9285-6 |
| 2020-2024 | Lower output; Padova applied MIP | PRIN 2022 grant | DOI 10.1016/j.ejor.2025.07.034 |

### Latest
- September-November 2026: sole- and two-author preprints with replication packages, pre-registered or pre-declared designs, pinned solver commits and declared AI assistants (Anthropic Claude; OpenAI ChatGPT or Codex); two revisit his own claims; all unrefereed. Not to be projected backwards ([06 §6, §7](references/research/06-trajectory.md)).

## Academic Lineage

Bologna (Laurea 1982, PhD 1987; advisor not established; first papers with Martello and Toth) → Fischetti (Padova since 1997; long collaborations with Balas, Caprara, Lodi, Monaci, Ljubić and Sinnl, Salvagnin) → confirmed doctoral students Bertacco (2005), Salvagnin (2009; later in CPLEX development) and Zanette (2008/09). Not his doctoral students: Lodi, Monaci, Defeng Liu, Palasgo. Lodi, Salvagnin, Glover, Ljubić, Sinnl and Monaci are insiders, not outside critics. Master's theses regularly became co-authored papers within 0-4 years (inferred, [06 §2.3](references/research/06-trajectory.md)). Recognition he lists: Edelman Award 2008 (Netherlands Railways team); Harold Larnder Prize 2015; DIMACS Steiner challenge 2014.
```

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it, word for word in fenced blocks (links as written in SKILL.md, relative to the skill folder). The shortened lines are in SKILL.md.

*Latest:*

```markdown
- September-November 2026: sole- and two-author preprints with replication packages, pre-registered or pre-declared designs, pinned solver commits and, in most, declared AI assistants (Anthropic Claude; OpenAI ChatGPT or Codex) [S143 p. 27], one doing all but idea and supervision [S161 p. 4], none declared in one re-test [S163]; two revisit his own claims; all unrefereed. Not to be projected backwards ([06 §6, §7](references/research/06-trajectory.md)). (full evidence: references/research/09-evidence-ledger.md#trajectory)
```

<a id="inner-tensions"></a>

## Inner tensions

### Full-text evidence (08 §2.7 and §3, copied)

- **Inner Tensions.** Tension 1 (simplicity against the 2026 apparatus): an old heuristic restored with 25,440 runs under a declared family [S164 pp. 11, 19]. Tension 2 (code closed): model files and logs on request only [S067 p. 10], but see §3 item 11. Tension 3 (black box enough, yet not enough): [S063 pp. 1, 11; S164 pp. 2, 9, 14, 19]. Tension 5 (general-purpose ambition against problem-specific results): [S027 pp. 3–4, 21; S092 pp. 2, 6–7, 19].

| # | Skill claim (section) | Full texts | Change |
|---|---|---|---|
| 11 | Inner Tension 2 and Honest Boundary: code closed or mostly unreleased until 2026 | In 2017 the bilevel solver, its instances and optimal values are released through co-author Sinnl's page (availability not checked by the reader) [S016 pp. 3, 7, 22, 37, 42]; instances published from 2001 [S013 p. 22; S125 pp. 3, 24–25; S001 pp. 2, 11; D011 pp. 2, 5]; QAP model files and logs on request only [S067 p. 10]; three 2022 GitHub repositories from papers led by Liu and Cavaliere [S076 arXiv v2 pp. 17, 25; S130 pp. 7, 22; S168 p. 1]; 2025 code on request [S126 p. 27] | Qualify Tension 2: code mostly closed until 2026, with the 2017 solver (availability not checked) and the three 2022 repositories as exceptions; instances public from 2001 |

### Added in T3.6

- Tension 1: 25,440 runs [S164 pp. 11, 19]. Tension 2 qualified: the 2017 bilevel solver announced as released through co-author Sinnl's page [S016 pp. 3, 7, 22] (the reader did not check its availability), three 2022 GitHub repositories from papers led by Liu and Cavaliere [S076 arXiv v2 pp. 17, 25; S130 pp. 7, 22; S168 p. 1] and 2025 code on request [S126 p. 27] (review fix: the draft said *except the 2017 bilevel solver*, which missed these cards), instances public from 2001 [S013 p. 22], QAP model files on request [S067 p. 10]. Tension 3: [S063 pp. 1, 11]. Tension 4: *(the M4 lapses, 1999–2026)*. Tension 5: [S027 pp. 3–4, 21].

### Before T3.6 (moved verbatim)

```markdown
## Inner Tensions

- **Tension 1: simplicity against the 2026 apparatus.** 2015: "Be simple (if you can)! #OccamRazor" (CORS15 PDF p.29); 2026: pre-registered factorial campaigns under Holm's correction.
- **Tension 2: implementation is part of the proof, yet the code stayed closed** until the 2026 pump study.
- **Tension 3: do not fight the black box, yet it is not enough.** "Do not waste your time in duplicating stuff already in the MIP solver" and, in the same deck, "Today's technology does not allow a general-purpose MIP solver to be used as a black-box in real-time rescheduling" (TRI16 PDF p.13); in 2026 he patches SCIP.
- **Tension 4: fairness rules against his own tables** (the M4 lapses).
- **Tension 5: general-purpose ambition against problem-specific results** (the bilevel solver, M1 limitations); M1 is itself tailoring to the class.
- **Tension 6: "Theorem. Using cuts within an enumerative scheme is good."** (ISMP18 PDF p.6) becomes "Conjecture: ..." on the same slide in 2026 (AIY26 PDF p.2).
```

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it, word for word in fenced blocks (links as written in SKILL.md, relative to the skill folder). The shortened lines are in SKILL.md.

*Tension 2:*

```markdown
- **Tension 2: implementation is part of the proof, yet the code stayed mostly closed** until the 2026 pump study. Exceptions: the 2017 bilevel solver, announced as released through co-author Sinnl's page (availability not checked) [S016 pp. 3, 7, 22], and three 2022 GitHub repositories from papers led by Liu and Cavaliere [S076 arXiv v2 pp. 17, 25; S130 pp. 7, 22; S168 p. 1]; 2025 code on request [S126 p. 27]. Instances were public from 2001 [S013 p. 22], QAP model files on request [S067 p. 10].
```

<a id="mentor-voice"></a>

## Mentor voice

### Added in T3.6

- One more verbatim slide question from a carded deck: "What do we need to add to the MILP solver to handle a MIBLP?" [S194 p. 10] (the Lunteren 2017 bilevel deck, joint work).

### Before T3.6 (moved verbatim)

```markdown
- **Questions he asks** (verbatim, slide text): "Can we just use a generic MIP solver?" (TRI16 PDF pp.5-6); "Ok, it works ... but WHY?" (ISMP09 PDF p.21); "But ... is this worth doing?" (IPCO05 PDF p.18); "Does it work?" (ISMP18 PDF p.16).
```

<a id="roundtable-card"></a>

## Roundtable Card

### Full-text evidence (08 §3, copied)

| # | Skill claim (section) | Full texts | Change |
|---|---|---|---|
| 1 | Method 4 Say–do and Roundtable Card Blind spots: no significance or statistical tests before 2026 | 95% confidence intervals, a Cochran Q-test and post hoc McNemar comparisons in 2009 [S041 pp. 15, 17, 20]; a McNemar test in 2025 [S126 p. 25] | *Significance tests rare before 2026 (2009, 2025); a declared apparatus from 2026* |
| 18 | Roundtable Card Blind spots: numerics and exactness | Not exact arithmetic, but numerics handled by construction and a posteriori checks: §5 D; tolerances tightened and wrong answers counted in 2004 [S101 pp. 12, 16–17] | *No exact arithmetic; numerics by construction and checks* |

### Added in T3.6

- Blind spots: *numerics and exactness* → *no exact arithmetic (numerics by construction and a posteriori checks [D009 pp. 4–5; S101 pp. 12, 16–17])*; *no statistical tests before 2026* → *statistical tests rare before 2026 (FP 2.0, 2009 [S041 pp. 15, 17, 20])*; added *single runs outside the variability line* (Method 3). Review fix: *numerics thin: safe by construction and checked a posteriori only, no exact arithmetic*, so that the Card still yields the lead to Gleixner on tolerance questions (Routing, Field boundary); *single runs common outside the variability papers*, since seeds are rerun outside them too [S079 p. 16].
- Likely disagreements, Achterberg: the 2026 study adds the 2005 parts to the objective pump rather than replacing it [S164 pp. 13–14].
- For the operator: the milp-roundtable fault line on the pump's objective says that implementers, *his FP 2.0 included*, dropped the cutoff; the 2026 text says FP 2.0 "mentioned it in passing" [S164 p. 2]. The roundtable file is outside this step's scope and was not edited. Review note: do not rewrite the fault line to say that FP 2.0 kept the cutoff; the 2026 text lists FP 2.0 among the later works that did not carry cutoff and recovery together [S164 p. 2]. At most, change *dropped* to *mentioned only in passing* for FP 2.0.

### Before T3.6 (moved verbatim)

```markdown
  - *Achterberg*: weighted objective pump (DOI 10.1016/j.disopt.2006.10.004) against cutoff-plus-recovery (DOI 10.1007/s10107-004-0570-3); components judged over broad libraries (DOI 10.14279/depositonce-1634) against callbacks and one showcase instance.
```

```markdown
- **Blind spots**: one commercial solver, single-threaded, features off; no convergence theory; binary-only neighbourhoods; numerics and exactness; no statistical tests before 2026; 2026 evidence unreviewed and AI-assisted.
```

<a id="honest-boundary"></a>

## Honest Boundary

### Full-text evidence (08 §1, §3 and §11, copied)

| Item | Count | Source |
|---|---|---|
| Card entries | 209 in 29 batch files: round 1 c01–c13 (52 cards) and s01–s10 (74); round 2 a2-01–a2-03 (72), c2-01 (3), s2-01 (3); round 3 s3-01 (5) | digests; 07 |
| Read level | full 132 · partial 3 · abstract 57 · metadata 15 · unreadable 2. Without the four superseded cards: 205 live cards, full 130 · partial 2 · abstract 57 · metadata 15 · unreadable 1 | digests |
| Works with a card | 198; INDEX.md after `mark_read_from_cards.py`: carded 130, skimmed 1, abstract 56, metadata 11, — 4 (Role skip) | INDEX.md |
| Coverage row (`team_status.py`) | 198 Scholar rows · 202 distinct works indexed · 132 open full texts · 130 read in full · 1 in part · 56 abstract only · 11 metadata only incl. unreadable · 4 skipped · 0 book material · 358 quotes verified | 07 |
| Quote gate (2026-11-28) | 358 quotes: 358 exact, 0 equal up to spacing or symbols, 0 not found | `verify_card_quotes.py` |
| Studies after merging pairs | 165 work groups: 112 with a full or partial text (110 without the editorial items D005/S178 and S132), 53 at abstract or metadata level only | this note |
| Method links | 503 link entries on 145 live cards (127 of them read in full or part); 453 point to Methods 1–6, 50 to heuristics, taste marks, tensions, misreadings, an anatomy or the Roundtable Card (§2.7) | digests |
| Pool material | 284 new-pattern-candidate entries on 145 cards (251 on full or partial cards); 701 proof-device entries (603); 710 transferable-technique entries (681) | digests |
| Full or partial work groups by period | 1986–90: 1 · 1991–95: 3 · 1996–2000: 13 · 2001–05: 17 · 2006–10: 28 · 2011–15: 14 · 2016–20: 24 · 2021–26: 12 | digests |
| Abstract or metadata groups by period | 1986–90: 11 · 1991–95: 16 · 1996–2000: 10 · 2001–05: 1 · 2006–10: 2 · 2011–15: 2 · 2016–20: 6 · 2021–26: 4 · undated 1 | digests |

| # | Skill claim (section) | Full texts | Change |
|---|---|---|---|
| 21 | Honest Boundary: no erratum on record | An erratum of their own 1998 definition printed inside a 2002 survey [S047 p. 50]; an own implementation error corrected in 2026 [S150 pp. 10, 30] | Qualify |

**11. Open gaps**

- **Bologna period.** 27 of the 31 work groups of 1986–1995 are abstract or metadata only: additive bounding [S031; S044; S099; S019], the 1988 dominance procedure [S104], the ATSP and Steiner polyhedra [S071; S089; S113; S128; S062; S025; S116]. How he worked then is read off S049, S030, S060 and S114 and the later surveys [S056; S102].
- **Unreadable or unopened texts that bear on the skill.** The compact-against-cutting-plane study S045 has no readable text; H006 may be its early version (not verified), and the judgement of which formulation wins once the solver's preprocessing works rests on H006 [H006 pp. 11, 14] and the S045 abstract [S045]. His comment on the learning-and-branching survey is metadata only [S152], so his stated view of machine learning for branching is not read. The MIP-cut metascheme talk [S173] and the MIC 2013 proximity abstract [S170] are abstract-level.
- **Conference versions.** D002, D006, D008, D010, D015 and S091 are abstract-level; their journal or preprint versions are read (header).
- **Work with Martina Fischetti as first author at abstract level.** S131, D016, S103 and S051: his share is unknown.
- **2025–2026 items at abstract or metadata level.** S151, S166 and S165 (a 2026 sole-author preprint on Fermat, metadata only); the replication packages S186 and S187.
- **Teaching voice.** The Italian textbook [H005] and the self-published book [S088] are abstract-level.
- **Journal versions.** The pump, proximity search, the Benders redesign and *Just MIP it!* were read in author preprints (as the skill's Honest Boundary says); journal-only changes are not known.
- **Unverified pairs.** S112 and S024 as one study; H006 and S045.
- **AI share in 2026.** Declared for S143, S150, S161 and S164, quantified only in S161 [S161 p. 4]; absent in S163.
- **Supervised theses.** S188 and S192 are abstract-level and are not his writing.

### Added in T3.6

- **Full-text coverage** (new bullet): this member's `team_status.py --coverage` row and the card and quote counts (08 §1).
- **Evidence limits**: the open gaps of 08 §11 [S045; S152; S173; H005; S088; S131; D016] and the erratum and self-correction [S047 p. 50; S150 pp. 10, 30], replacing *no referee report, rebuttal, erratum or retraction on record*. H006, a 2009 draft that may be an early version of S045, and the abstract-level works led by Martina Fischetti (S103, S051) are named here only.
- **Claimed but unverified**: *(code mostly unreleased until 2026; one joint solver released in 2017 [S016 pp. 3, 7])*. Review fix: *(code mostly unreleased until 2026; the exceptions, one not checked, are under Tension 2 [S016 pp. 3, 7; S130 p. 7])*; the exceptions themselves (the 2017 solver, availability not checked, and three 2022 GitHub repositories [S076 arXiv v2 pp. 17, 25; S130 pp. 7, 22; S168 p. 1]; 2025 code on request [S126 p. 27]) stand in Tension 2. **Evidence limits**: H006 named beside S045 (a 2009 draft read in full, possibly an early version; not verified). **Validation**: FIDELITY.md is no longer linked; the line warns that it restates the sealed answers, and the Sources appendix lists it among the files not to open.
- **Holdout**: two candidate heuristics held back ([Held back](#held-back)). **Research date** 2026-11-28. **Validation**: *Not rerun after the deep reading.*
- **Corrections from the full texts**: a new subsection of one-line items. After review it keeps the corrections that change advice, the errata and the Pruning Moves thesis, and one line naming the dates and details corrected in place; the fourteen-line T3.6 list is kept under [Corrections](#corrections).

### Before T3.6 (moved verbatim)

```markdown
## Honest Boundary

This skill is distilled from public material and has these limits:
- **Tacit knowledge**: no interview, method essay, award-lecture text or talk transcript exists; his voice survives as slide bullets from 46 decks (2002-2026) and paper prose. How he reads a trace or decides an idea works is visible only through outcomes. OR2 lecture videos were not transcribed.
- **Era and resources**: 2002-2018 a closed commercial solver, callbacks, and direct contact to solver developers; 2026 one author, a cluster, pinned open solvers, declared AI assistants. Methods judged on one commercial solver with features off fared worse when critics re-ran them on CBC or SCIP.
- **Field boundary**: inside the lens: primal heuristics, Benders and cut loops, symmetry by aggregation, variability, measurement. Thin or absent: numerics and exact solving, presolve, conflict analysis, LP internals, column generation before 2025. Bilevel, bilinear, robust and machine-learning work is evidence of habits only.
- **Authorship**: every method before 2026 is co-authored. Martina Fischetti is a separate researcher; wind-farm, distancing, matheuristics and EndoWake work is joint with her.
- **Claimed but unverified** (never treat as methods): that his ideas ended inside general-purpose solvers (self-reported; no release note read); that implementation is part of the result (code mostly unreleased until 2026); that every 2026 number comes from a script (the README's own map lists hand-quoted numbers); a statistical branch-and-cut over clouds of fractional points (an agenda); "the more sophisticated the code, the smaller the speed-up" (no study); that publication norms punish simple ideas (no rejection on record); a taste against metaphor-driven metaheuristics (inferred from a course folder).
- **Evidence limits**: journal versions of the pump, proximity search, the Benders redesign and *Just MIP it!* not read (author preprints were); 44 of 76 critique sources are abstracts or citation contexts; no referee report, rebuttal, erratum or retraction on record.
- **Holdout**: five primary items are sealed for the validation step and are not in this skill.
- **Research date**: 2026-11-14 (notes gathered 2026-11-08). He is living and was publishing at the research date; refresh this skill periodically (at least yearly, and after his 2026 manuscripts are refereed).
- **Validation 2026-11-14**: sealed-item test 9 with the skill / 3 without (5 items; 2 points or less is a tie); task test 8 supported and 0 fabricated grounds with the skill (on the version before the after-validation fixes of 2026-11-14; retention re-test after them: 6 of 6 pass); see [FIDELITY.md](FIDELITY.md).
```

<a id="corrections"></a>

## Corrections from the full texts

### All claims of the pre-synthesis SKILL.md that the full texts change (08 §3, copied)

| # | Skill claim (section) | Full texts | Change |
|---|---|---|---|
| 1 | Method 4 Say–do and Roundtable Card Blind spots: no significance or statistical tests before 2026 | 95% confidence intervals, a Cochran Q-test and post hoc McNemar comparisons in 2009 [S041 pp. 15, 17, 20]; a McNemar test in 2025 [S126 p. 25] | *Significance tests rare before 2026 (2009, 2025); a declared apparatus from 2026* |
| 2 | Method 2 practice: the controlled-oracle test cited to DOI 10.1007/978-3-642-13520-0_17 | Not in S106, which goes straight to the real separator [S106 pp. 3–5]; the test is in the 2009 yoyo manuscript [S174 pp. 6–7] | Repoint to S174 |
| 3 | Method 5 practice: FP 2.0 listed among the works that dropped the 2005 prescription | FP 2.0 "mentioned it in passing"; Boosting FP "dropped the objective altogether" [S164 p. 2]; both are among the later works that did not carry cutoff and recovery together | Correct the wording, not the category |
| 4 | Method 5 limitation: FP 2.0 used the static cutoff the 2026 study measures as lossy | The static bound z*(1 + β) is FP 2.0's device for grading instance difficulty; the dynamic cutoff is only reviewed [S041 pp. 5, 14, 16]; the 2026 text does not say which cutoff FP 2.0 used [S164 p. 2] | Rephrase as an evaluation device |
| 5 | Method 5 practice: Pruning Moves revives the 1988 procedure *through a master's thesis* | S124 does not mention a thesis [S124 pp. 2, 6–8]; S096 names Salvagnin's 2005 master's thesis [S096 pp. 19, 27–28] | Cite S096 for the thesis |
| 6 | Research Taste mark 1: QAPLIB esc instances *in minutes on a notebook* (CORS15 deck) | The paper reports "a single quad-core PC" with 8 threads; esc128 in seconds, the three hard esc instances in under half an hour [S067 pp. 2, 10] | Keep the deck quote, add the paper's hardware |
| 7 | Method 3: seeds in his designs before the statement | True for the variability line [S041 pp. 14–15; S055 pp. 2–9]; one run per instance in 18 other works 2001–2022, among them [S063 pp. 8–10] (§2.3) | Name the line; add the limitation |
| 8 | Method 1 Say–do: practised 2011–2017 | Projection 1999–2006 [S069 pp. 3, 5–6; S073 pp. 3–4; S013 pp. 7–8; S006 pp. 1–4]; fat/slim 2007–2009 [D004 pp. 4, 8; S010 p. 16; S018 pp. 11–13] | Widen the dates |
| 9 | Method 1 limitation: for exact work he calls the root LP bound critical | Counter-case [S067 p. 7]; support in the joint handbook-chapter voice [S145 pp. 3–4] | Add both |
| 10 | Method 4: dated lapses in 2011, 2012 and 2017 | Lapses recur 1999–2026 (§2.4) | Widen the list; keep the word *dated* |
| 11 | Inner Tension 2 and Honest Boundary: code closed or mostly unreleased until 2026 | In 2017 the bilevel solver, its instances and optimal values are released through co-author Sinnl's page (availability not checked by the reader) [S016 pp. 3, 7, 22, 37, 42]; instances published from 2001 [S013 p. 22; S125 pp. 3, 24–25; S001 pp. 2, 11; D011 pp. 2, 5]; QAP model files and logs on request only [S067 p. 10]; three 2022 GitHub repositories from papers led by Liu and Cavaliere [S076 arXiv v2 pp. 17, 25; S130 pp. 7, 22; S168 p. 1]; 2025 code on request [S126 p. 27] | Qualify Tension 2: code mostly closed until 2026, with the 2017 solver (availability not checked) and the three 2022 repositories as exceptions; instances public from 2001 |
| 12 | Common Misreading 4: the in-out loop presented as new in 2009, credited in 2010 | Confirmed [S174 pp. 1–2, 7–8, 12–13; S106 pp. 1–2]; precursor in 2000–2001, a point between x* and two incumbents separated first and credited to Reinelt [S125 pp. 11–12; S057 p. 20] | Add the precursor |
| 13 | Common Misreading 5: the 2005 pump had a cutoff with a recovery LP | True [S007 p. 11], but evaluated only in two approximate-LP variants on 26 instances; the basic pump stops at its first solution [S007 pp. 6, 10–13]; in 2007 the cutoff variants are reported as inferior to the pump followed by local branching or RINS [S026 p. 18]; the authors themselves describe local branching as a heuristic approach whose strategy is exact in nature [S085 pp. 2–3] | Add the nuance |
| 14 | Pump anatomy: random flips published instead of enumeration, which returned in 2007 | A preprint of 16 February 2004 already switches from the pump's almost-feasible point to enumeration by local branching [S085 pp. 1, 4] | Date the return to the 2004 preprint (published 2008) |
| 15 | Pump anatomy, minimum evidence: 37 hard 0-1 instances, one pump failure, CPLEX 8.1 18 and 8 | The revised paper reports 83 instances (44 MIPLIB 2003 plus 39 hard), a Pentium M notebook, 3 pump failures and 19 CPLEX root failures in the chosen setting (25, 41 and 33 in the others) [S007 pp. 1, 5–7] | Say which source the 37-instance figures come from (not in S007), or use the paper's |
| 16 | Local-branching anatomy: Aussois 2002 traces on seymour and arki001 | The paper's traces are tr24-15 and B1C1S1; the other anatomy figures (29 instances, k = 20, no fine tuning, first on 23 of 29, TURNI 833 → 809) match [S001 pp. 3, 6, 11–13] | Correct the trace instances or cite the deck |
| 17 | Method 1 practice: the train-rescheduling team kept two of about eight ideas, removing the others improves performance (TRI16 deck) | The paper has the subtraction [S059 p. 5] but neither the count nor the improvement claim | Keep the deck as the source of both |
| 18 | Roundtable Card Blind spots: numerics and exactness | Not exact arithmetic, but numerics handled by construction and a posteriori checks: §5 D; tolerances tightened and wrong answers counted in 2004 [S101 pp. 12, 16–17] | *No exact arithmetic; numerics by construction and checks* |
| 19 | Latest: 2026 preprints with declared AI assistants | Declared in S143 [S143 p. 27], S150 [S150], S161 [S161 p. 4] and S164; S163 carries no statement on AI assistance [S163]; in S161 the assistant did everything but the idea and the supervision [S161 p. 4] | *Most of them declare AI assistants* |
| 20 | Academic Lineage: master's theses became co-authored papers (inferred) | Salvagnin's thesis into a 2009 chapter [S096 pp. 19, 27–28]; a 2003 dissertation into a 2009 paper, supervision not stated [S046 pp. 2, 34]; Martina Fischetti's thesis into a 2014 paper [S154 p. 2]; variant: a 2012 master's thesis into a sole-authored paper that credits the student in the text [S109 pp. 1, 4, 8, 14–15, 19] | Confirmed, with the variant |
| 21 | Honest Boundary: no erratum on record | An erratum of their own 1998 definition printed inside a 2002 survey [S047 p. 50]; an own implementation error corrected in 2026 [S150 pp. 10, 30] | Qualify |
| 22 | Method 2 limitation: one showcase instance since 2016 | The gs250a-1 traces are already in the April 2015 report [S195 pp. 15–17] | *since 2015* |
| 23 | Common Misreading 2: adoption into solvers is the authors' statement | Further self-reports: CBC and GLPK implementations of proximity search [S052 p. 23]; a CPLEX uptake resting on a private communication [D012 pp. 9, 13]; one bound-tightening method part of CPLEX 12.6.1 [S029 pp. 15–16]; a 2025 method moved into a commercial solver [S126 pp. 24, 26] | Add as further self-reports |

### Where each correction stands in SKILL.md

Lines of the Corrections list after the review: 1 significance tests; 2 seeds; 3 controlled-oracle test; 4 FP 2.0; 5 numerics; 6 code; 7 errata; 8 the Pruning Moves thesis; 9 dates and details corrected in place.

| 08 §3 item | Applied in SKILL.md |
|---|---|
| 1 | Method 4 variant bullet; Roundtable Card Blind spots; Corrections line 1 |
| 2 | Method 2 Practice and step 4 [S174 pp. 6–7]; Corrections line 3 |
| 3, 4 | Method 5 variant bullets 1–2; Corrections line 4 |
| 5 | Corrections line 8 (the Method 5 bullet moved there after review) |
| 6 | Taste mark 1; Corrections line 9 |
| 7 | Method 3 Say–do and variant bullet; Roundtable Card Blind spots; Corrections line 2 |
| 8 | Method 1 Say–do, marked ✗ (the variant bullet folded into it after review); Corrections line 9 |
| 9 | Method 1 Limitations (QAP counter-case) and variant bullet (handbook-chapter voice) |
| 10 | Method 4 Say–do and variant bullets; Tension 4; Corrections line 9 |
| 11 | Tension 2; Honest Boundary, Claimed but unverified; Corrections line 6 (after review with the three 2022 repositories and the 2025 code on request) |
| 12 | Misreading 4; Method 2 Practice; Corrections line 9 (since T3.7: Misreading 4 and Corrections line 9 only; the Method 2 Practice line that carried the precursor is in the [Method 2](#method-2) Before T3.7 block) |
| 13 | Misreading 5; Corrections line 9 |
| 14, 15 | Pump anatomy; Corrections line 9 |
| 16 | Local-branching anatomy; Corrections line 9 |
| 17 | No line after review: the TRI16 count is no longer in SKILL.md (it left with the old Practice line of Method 1) |
| 18 | Roundtable Card Blind spots; Corrections line 5 |
| 19 | Latest; Corrections line 9 |
| 20 | Academic Lineage |
| 21 | Honest Boundary, Evidence limits; Corrections line 7 |
| 22 | Method 2 Limitations; Corrections line 9 |
| 23 | Misreading 2 |

### Found by the T3.6 review (claims of the T3.6 draft corrected before commit)

| Claim of the draft | Full texts | Now in SKILL.md |
|---|---|---|
| Method 6: before 2002 no general-purpose solver run, not even as a baseline | Holds for the problem-specific crew and routing codes [S012 pp. 9, 11; S013 pp. 18, 22, 26]; CPLEX 3.0 runs as a referee for bounds in 1999 [S004 p. 21]; the 2000 survey runs CPLEX and MINTO and finds them competitive [S003 p. 9] | Method 6 Say–do and bullet 1 |
| Tension 2: code closed except the 2017 bilevel solver | Three 2022 GitHub repositories [S076 arXiv v2 pp. 17, 25; S130 pp. 7, 22; S168 p. 1]; 2025 code on request [S126 p. 27]; the 2017 release not checked [S016 pp. 3, 7, 22] | Tension 2; Claimed but unverified; Corrections line 6 |
| Method 5: FP 2.0 did not drop the 2005 prescription | S164 lists FP 2.0 among the later works that did not carry cutoff and recovery together, saying it "mentioned it in passing" [S164 p. 2]; FP 2.0 only reviews the dynamic cutoff [S041 p. 5] | Method 5 bullet 1; Corrections line 4 |
| Benders anatomy: the first separator's times 824.76 s and 225.25 s | The quick shot is reported only as under 15 minutes each [S011 p. 11]; the times are the full recipe's, Table 1 [S195 pp. 21–22] | Benders anatomy, Minimum evidence (since T3.7: only the corrected claim, the quick shot under 15 minutes each, stays in SKILL.md; the full recipe's times are in the [Benders redesign](#anatomy-benders) Before T3.7 block) |
| The controlled-oracle test at [S174 p. 5] | File pages 6–7 (the file's [[page N]] carries printed page N − 1) [S174 pp. 6–7] | Method 2 step 4; Corrections line 3 |
| Method 3: the backdoor gain no larger than step 2's placebo | A cross-study inference; S063 gives about 15% in arithmetic-mean time, comparable in geometric mean, from one run per instance [S063 pp. 8–10] | Method 3 bullet 1 (since T3.7: the bullet without the figures, which are in the [Method 3](#method-3) Before T3.7 block) |
| Erraticism anatomy: gains on hard ones (−28.5%) | The +53.0% class (1,000–10,000 nodes) is hard by the paper's own definition; gains on the two largest classes only [S055 pp. 8–9] | Erraticism anatomy |
| Method 5: the 1992 and 1997 codes re-run ten years later | Re-run in the 2002 survey, 10 and 5 years on [S056 pp. 31, 34–39] | Method 5 bullet 3 |
| Warning 1 and Method 1: S145 as a textbook, cited for the loss of generality | S145 is a 2017 handbook chapter with Balas; only S001 p. 2 says the generality is lost [S001 p. 2; S145 p. 10] | Warning 1; Method 1 bullet 3 |
| Pump anatomy, Origin tagged [stated] on a co-signed paper | [S007 p. 2] is joint with Glover and Lodi | Pump anatomy, Origin [joint] |
| Method 3 and the Card: single runs outside the variability line | Seeds are rerun outside it too, e.g. 5 seeds on selected wins in 2020 [S079 p. 16] | Method 3 Say–do; Card |

### The T3.6 Corrections list before the review (moved verbatim)

```markdown
One line each; detail in the ledger (references/research/09-evidence-ledger.md#corrections).
- Significance tests exist before 2026 [S041 pp. 15, 17, 20; S126 p. 25] (Method 4, Roundtable Card).
- The controlled-oracle test is in the yoyo manuscript [S174 p. 5], not the CPAIOR paper (Method 2).
- FP 2.0 mentioned the cutoff in passing [S164 p. 2]; its static cutoff graded difficulty [S041 pp. 5, 14] (Method 5).
- The Pruning Moves thesis is named in *Just MIP it!* [S096 pp. 19, 27–28] (Method 5).
- QAP hardware: a quad-core PC, 8 threads [S067 pp. 2, 10] (Taste mark 1).
- Seeds: variability line only [S063 pp. 8–10] (Method 3).
- Dates: Method 1 from 1999 [S069 pp. 3, 5–6]; Method 4 lapses 1999–2026; showcase instance from 2015 [S195 pp. 15–17].
- Code release: one joint solver in 2017 [S016 pp. 3, 7] (Tension 2).
- In-out precursor 2000–01 [S125 pp. 11–12]; the 2005 cutoff tested in two variants only [S007 pp. 10–13] (Misreadings 4, 5).
- Pump anatomy: 83 instances, 3 failures [S007 pp. 1, 5–7]; enumeration back by 2004 [S085 pp. 1, 4].
- Local-branching traces: tr24-15 and B1C1S1 [S001 pp. 6, 11].
- The two-of-eight count is the TRI16 deck's, not the paper's [S059 p. 5].
- Numerics: by construction and checks, no exact arithmetic [D009 pp. 4–5] (Roundtable Card).
- AI statements: absent in one 2026 re-test [S163] (Latest).
```

<a id="promotions"></a>

## Promotions and the candidate pool

### 08 §4 and the §5 preamble, copied

**No cluster is promoted to a core method this round; the skill stays at six.** Three clusters reach the size threshold (at least three distinct works read in full or in part) and were run through the four checks strictly.

| Cluster | Works (full or part) | 1 Cross-project | 2 Say–do | 3 Executable, non-standard | 4 Exclusive | Decision |
|---|---|---|---|---|---|---|
| A. Let the search model be wrong; keep the judge exact | 9: S198/S046, D004/S018, S010, D007, S154, S059, S150, S164, S015 | ✅ nesting 2004–09, robustness 2007–09, wind 2014 and 2026, rescheduling 2017, the pump 2026 | ✅ sole-author statement [S164 p. 8]; joint statements [S018 p. 9; S150 pp. 1, 9] | ✅ steps in §5; differs from searching on the most faithful model | ✗ partial: approximate-then-repair and screen-then-confirm are common, and S150 credits multi-fidelity precedents [S150 pp. 3, 6]; overlaps Method 1 step 2 and Method 4 step 1 | Heuristic (§5 A) |
| B. Mechanism first: say where the device should win before the runs | 7: S014, S074, S052, S029, S143, S164, S161 | ✅ 2006–2026 | ✅ sole-author [S164 pp. 3–4]; S161 is weak, its design being the assistant's [S161 p. 4] | ✅ | ✗ partial: subgroup reading is common; the predicted-class and probe-arm form is less so; overlaps Method 2's diagnosis and Method 3's controls | Heuristic (§5 B) |
| C. Keep what an expensive call produced | 7: S124, D012, S063, D014, S090, S130, S168 | ✅ 2010–2022 | ✗ no statement in his voice among the cards | ✅ partly standard (solution pools, strong-branching reuse, set-partitioning recombination in routing) | ✗ | Variant of Method 6 step 5 (§2.6) |

Clusters with three or more full works that are absorbed by an existing method, not promoted: controlled conditions first (10 works; Method 2 step 4 and H8, §5 C); control arms (5 works in the candidate pool and more in Method 3's evidence, §2.3); lexicography as stabiliser and structural device (S096, D011, S137, D019 with S074 and D009; Method 2 step 3); rival re-implemented in one's own framework (S027, S082, S092, S077; Method 4 step 4); generalize the class, then win on the special cases' benchmarks (S027, S090, S092; H4 variant); numerically safe by construction (D009, S011, S016, S079 with the decks S190 and S194; H10, §5 D).

Two new heuristics pass *executable plus at least one more check* and add a rule the skill does not state (A, B). Three updates extend existing items instead of adding new ones (C–E). The skill already has ten heuristics, the top of the framework's 5–10 range. Two of them duplicate method steps: H5 (*the baseline a practitioner would run*) is Method 4 step 2 almost word for word and has no card link, and H6 (*positive correlation is enough*) is already invoked inside Method 3 step 4. Folding H5 and H6 into those steps would keep the list at ten with A and B; the editing step decides.

### What this pass did

- **No new core method**; the skill keeps six (08 §4).
- **Two new heuristics**, items 11 and 12 (08 §5 A, B). To keep the list within the framework's 5–10, Heuristic 5 (a near-verbatim copy of Method 4 step 2, with no card link) and Heuristic 6 (already invoked inside Method 3 step 4) were folded into those steps; their numbers stay in SKILL.md as pointers, so ten live heuristics remain.
- **Three extensions**, not new items: *controlled conditions first* widens Method 2 step 4 and Heuristic 8 (08 §5 C); *numerically safe by construction* extends Heuristic 10 (08 §5 D; catalog DM26, DM27); *keep what an expensive call produced* is a Method 6 step-5 variant (08 §5 E, §2.6; catalog DM21).
- The candidate pool (284 entries on 145 cards) is 08 §6; its clusters stay in the pool or in the catalog as techniques.

<a id="rejected"></a>

## Rejected updates

### 08 §10, copied

1. Promote any cluster to a core method: rejected for this round (§4); none passes all four checks without duplicating Method 1, 2, 3, 4 or 6.
2. Add the 1990s Lagrangian practices (dual-guided greedy, core pricing, multiplier design, additive bounding) as methods or heuristics: rejected; standard practice of the period, and they add no explanatory power to solver-engineering advice; kept as trajectory (§8) and technique (§7.2).
3. Add *Chvátal–Gomory derivation as a separation handle* or the polyhedral facet machinery as methods: rejected; covered by Method 6's separation sub-decision, and polyhedral theory lies outside this team's represented field.
4. Add *release instances, solver and optimal values* as a heuristic: rejected; generic reproducibility; used only to qualify Inner Tension 2 (§3 item 11).
5. Add *controlled conditions first*, *control arms*, *lexicography* or *re-implement the rival* as separate heuristics: rejected; they explain steps of Methods 2, 3 and 4 and are filed there as evidence.
6. Add *generalize the class, then win on the special cases' benchmarks* as a heuristic: rejected; three papers of one year with one coauthor group; H4 variant and Inner Tension 5.
7. Add *big-penalty slack* or *lower bound as an audit* as heuristics: rejected; standard modelling and reporting.
8. Add *one monotone dial per device* as a heuristic: held in the pool; no statement in his voice among the cards, and one case is itself a lapse.
9. Add the 2026 measurement apparatus as a method: rejected; dated to 2025–2026 and covered by Methods 4 and 5 with the skill's rule against projecting it backwards.
10. Add *the defect turned into the mechanism* as a heuristic: rejected; H1 covers it.
11. Add *keep what an expensive call produced* and *numerically safe by construction* as separate heuristics: rejected in favour of a Method 6 step-5 variant and an H10 extension (§5 D, E).
12. Promote patterns seen only in abstracts (hardness with polynomial special cases; worst and average case side by side): rejected; no full or partial card.
13. Carry the cards' reading notes on inconsistencies inside works into the skill: not done (house rule).

Also rejected in T3.6: a new stage workflow (08 supports none); listing every paper read in the Sources appendix (the full-text index and the card key hold them).

<a id="held-back"></a>

## Held back under the holdout rule

Two candidate heuristics would rest on material that `holdout.md` seals; they are named in the stage report only, and no point, quote or decision of a sealed item is used anywhere in this file, in SKILL.md or in the catalog, also where another card states the same point. Card evidence that carries a sealed point was not cited (08 header, *Not carried*; the stage report lists the pages).

<a id="sources"></a>

## Sources appendix

### Added in T3.6

- A **Deep reading (2026-11-28)** line pointing to the [full-text index](../sources/papers/INDEX.md), the card index `07-paper-cards.md` (named, not linked), [08](08-deep-reading-synthesis.md), this ledger and the [technique catalog](../technique-catalog.md).
- The open-notes paragraph now adds that the script-generated card index 07 and the card batch files under `cards/` also state sealed points, and that INDEX.md, 08, the ledger and the catalog hold none. The paper list is unchanged.
- **Review fix**: the validation record FIDELITY.md joins the files not to open (it restates the sealed answers), and the Honest Boundary no longer links it. The Bertsimas–Dunning–Lubin entry, whose only body citation had already moved here (Method 4, Before block), left the paper list; its line:

```markdown
- D. Bertsimas, I. Dunning, M. Lubin, "Reformulation versus cutting-planes for robust optimization", Comput. Manag. Sci. 13 (2016) 195-217, DOI 10.1007/s10287-015-0236-z
```

### Before T3.6 (moved verbatim)

```markdown
## Sources (Appendix)

Research notes open for reading: [04 mentorship](references/research/04-mentorship.md), [05 peer critique](references/research/05-peer-critique.md), [06 trajectory](references/research/06-trajectory.md). Notes 01 (publications), 02 (stated methodology) and 03 (process evidence) in `references/research/` back the pointers above but hold passages sealed for the Phase 4 validation; do not open them before the validation step has run.
```

<a id="card-key"></a>

## Card key

One line per work with a card: year, title and venue as indexed, read level of the best card, batch file, the version read (from the card's Read line, shortened) and the key the pre-synthesis SKILL.md used for it. The batch files under `cards/` hold sealed points: do not open them while testing the skill. Superseded cards: the round-2 cards in `c2-01` replace the round-1 cards of S012 (c01), S017 (c02) and S003 (c02); the `s2-01` card of H003 replaces its unreadable `s01` card. Count once (08 header): S072 = S073; S057 = S125; S195 = S011; D018 = S110; S033 = D003; S058 = S139; S112 = S024 (probably, not verified); S066 = S004; D001 = S107; S184 = H002; S054 = S008; D016 and S051 (two editions); H006 possibly an early version of S045 (not verified). S176, the complete ATMOS 2008 volume, is Role skip; his parts are S178 and D005. S188 and S192 are supervised theses.

| Card | Year | Work (title, venue as indexed) | Read level (best card) | Batch | Version read (from the card's Read line) | Pre-synthesis key |
|---|---|---|---|---|---|---|
| D001 | 1993 | On the monotonization of polyhedra (IPCO, 23-38) | abstract | a2-01 | — | — |
| D002 | 2005 | Mixed-Integer Cuts from Cyclic Groups (IPCO, 1-11) | abstract | a2-02 | — | — |
| D003 | 2005 | Optimizing over the First Chvàtal Closure (IPCO, 12-22) | full | c03 | The whole 11-page conference paper, footnotes and references included. Per its work-list note this is the IPCO 2005 conference version of S033 (Math. … | — |
| D004 | 2007 | Fast Approaches to Robust Railway Timetabling (ATMOS) | full | s04 | (all 16 file pages; the plot data of Figs. 1–3 are extraction debris, Table 2 is readable). First-page check: title and Fischetti, Salvagnin, Zanette … | — |
| D005 | 2008 | ATMOS 2008 Abstracts Collection - 8th Workshop on Algorithmic Approa… (ATMOS) | full | s05 | (all 7 file pages). First-page check: title and editors Matteo Fischetti and Peter Widmayer match (p. 1). The editors' own text is the one-line … | — |
| D006 | 2008 | Can Pure Cutting Plane Algorithms Work? (IPCO, 416-434) | abstract | a2-02 | — | — |
| D007 | 2009 | Robustness in Train Timetabling (CTW, 171-174) | full | s05 | (all 4 file pages = printed pp. 171–174). First-page check: title and authors V. Cacchiani, A. Caprara, M. Fischetti match (p. 1). | — |
| D008 | 2010 | A Relax-and-Cut Framework for Gomory's Mixed-Integer Cuts (CPAIOR, 123-135) | abstract | a2-02 | — | — |
| D009 | 2010 | On the enumerative nature of Gomory's dual cutting plane method (Math. Program. 125(2), 325-351) | full | c05 | All 25 file pages: text, Examples 1-4, Tables 1-4 and references. Figures 2-11 survive only as axis ticks, tree labels and node numbers; they are … | DOI 10.1007/s10107-010-0392-4 |
| D010 | 2011 | Backdoor Branching (IPCO, 183-191) | abstract | a2-02 | — | — |
| D011 | 2012 | A hard integer program made easy by lexicography (Math. Program. 135(1-2), 509-514) | full | s06 | (all 5 file pages of the manuscript dated 16 February 2011, with Tables 1–2 and Figures 1–2). First-page check: title and authors Balas, Fischetti … | — |
| D012 | 2012 | Branching on nonchimerical fractionalities (Oper. Res. Lett. 40(3), 159-164) | full | c06 | Abstract, §§1-5 (pp. 1-10), Table 4 (p. 11) and the performance profiles of Figure 1 (p. 12, read from the caption and the text of p. 10) read in … | DOI 10.1016/j.orl.2012.01.008 |
| D013 | 2012 | Orbital Shrinking (ISCO, 48-58) | full | s06 | (all 11 file pages of the preprint dated 12 July 2011, with Tables 1–2 and Figure 1). First-page check: title and authors Fischetti, Liberti match … | — |
| D014 | 2013 | Approximating the Split Closure (INFORMS J. Comput. 25(4), 808-819) | full | s07 | (all 26 file pages of the author preprint: §§1–5, Algorithms 1–3, Tables 1–5). First-page check: title and authors Fischetti, Salvagnin match (p. 1). | — |
| D015 | 2016 | Intersection Cuts for Bilevel Optimization (IPCO, 77-88) | abstract | a2-02 | — | — |
| D016 | 2018 | Matheuristics (Handbook of Heuristics, 121-153) | abstract | a2-02 | — | — |
| D017 | 2018 | SelfSplit parallelization for mixed-integer linear programming (Comput. Oper. Res. 93, 101-112) | full | s08 | (all 28 file pages of the author preprint submitted on 15 January 2018, printed title "Self-split parallelization for Mixed-Integer Linear … | — |
| D018 | 2019 | Embedded hyper-parameter tuning by Simulated Annealing (arXiv preprint arXiv:1906.01504) | full | s09 | (all 9 pages of arXiv 1906.01504v1, 4 June 2019, marked "Preprint. Under review."; figures read through their captions). First-page check: title and … | — |
| D019 | 2019 | Finding First and Most-Beautiful Queens by Integer Programming (arXiv preprint arXiv:1907.08246) | full | s09 | (all 14 pages of arXiv 1907.08246v1, 18 July 2019, "Preprint. Under review."; appendix solution lists, pp. 10–13, read as data). First-page check … | — |
| H001 | 1986 | Worst-Case Analysis of an Approximation Scheme for the Subset-Sum Pr… (Operations Research Letters 6, 283-284) | abstract | a2-01 | — | — |
| H002 | 1996 | Odd Cut-sets, Odd Cycles, and 0-1/2 Chvatal-Gomory Cuts (Ricerca Operativa 26, 51-80) | abstract | a2-01 | — | — |
| H003 | 1998 | Experiments with Controlled Rounding for Statistical Disclosure Cont… (Journal of Official Statistics 14 (4), 553-…) | full | s2-01 (supersedes s01) | (all 13 file pages: §§1–5, Tables 1–6 and the references; the article has no conclusions section). The font layer drops or garbles mathematical … | — |
| H004 | 1999 | I Turni delle Locomotive (in S. Pallottino, A. Sciomachen (eds.), Sci…) | metadata | a2-02 | — | — |
| H005 | 2018 | Lezioni di Ricerca Operativa (Independently published, ISBN 9781980835011) | abstract | a2-03 | — | — |
| H006 | 2009 | Robustness by cutting planes and the Uncertain Set Covering Problem (Preliminary draft, May 25, 2009 (author's p…) | full | s2-01 | (all 19 file pages: abstract, §§1–4, Tables 1–6 and the references; Figures 1 and 2 are images whose data are not in the text, pp. 14, 17). … | — |
| S001 | 2003 | Local branching (Mathematical programming 98 (1), 23-47, 2003) | full | c03 | The author preprint ("May 2002, Revised December 2002", 24 pp.) was read whole: the main text (pp. 1–17) closely; the appendix tables 6–11 (pp. … | DOI 10.1007/s10107-003-0395-5; local-branching anatomy |
| S002 | 2002 | Modeling and solving the train timetabling problem (Operations research 50 (5), 851-861, 2002) | full | c03 | The whole 24-page author preprint (OCR text) and its reference list were read. Prose and formulas are readable despite OCR noise; the figures in … | — |
| S003 | 2000 | Algorithms for the set covering problem (Annals of Operations Research 98 (1), 353-3…) | full | c2-01 (supersedes c02) | for this copy, which has 12 pages: the text (pp. 1–9), the references (pp. 10–11) and Table 1 (p. 12). Tables 2–4, discussed on pp. 7–9, are not in … | — |
| S004 | 1999 | A heuristic method for the set covering problem (Operations research 47 (5), 730-743, 1999) | full | c02 | The whole undated author preprint (27 pp.): abstract, §§1–9, Tables 1–8, Figures 1–4 and the references. The figures' plotted curves are read from … | — |
| S005 | 1997 | A branch-and-cut algorithm for the symmetric generalized traveling s… (Operations Research 45 (3), 378-394, 1997) | full | c01 | The whole 36-page author preprint ("January 1994; Revised May 1995", p. 1) was read, including Tables 6.1-6.5 (pp. 29, 33-36) and the references. … | — |
| S006 | 2006 | Combinatorial Benders' cuts for mixed-integer linear programming (Operations Research 54 (4), 756-766, 2006) | full | c03 | The whole preprint ("May 24, 2004; Revised, February 16, 2005", 22 pp.), all three tables, both figures and the references. The journal version … | — |
| S007 | 2005 | The feasibility pump (Mathematical programming 104 (1), 91-104, 2…) | full | c03 | The whole "Revised version" manuscript (15 pp.), all five tables and the references. The journal version (Math. Program. 104, 91–104) was not read. | DOI 10.1007/s10107-004-0570-3; pump anatomy |
| S008 | 2018 | Deep neural networks and mixed integer linear optimization (Constraints 23 (3), 296-309, 2018) | full | c10 | Whole text pp. 1-15 (author manuscript); Tables 1-3 read (pp. 12-13); Figures 1-4 survive only as captions (pp. 7-10); reference list read. | DOI 10.1007/s10601-018-9285-6 |
| S009 | 1998 | Solving the orienteering problem through branch-and-cut (INFORMS Journal on Computing 10 (2), 133-14…) | full | c01 | The whole 31-page author preprint (undated; references up to 1997; an early version was presented at EURO XIII, Glasgow, July 1994, p. 3) was read … | — |
| S010 | 2009 | Light robustness (Robust and online large-scale optimization:…) | full | c04 | Whole text pp. 1-21 ("Preliminary draft: December 18, 2008", p. 1; the published chapter not compared); all tables read; references skimmed. | — |
| S011 | 2017 | Redesigning Benders decomposition for large-scale facility location (Management Science 63 (7), 2146-2162, 2017) | full | c08 | pp. 1-19 read closely (models, cut derivations, Algorithm 1 with Lemma 3.1 and Theorem 3.1, implementation §4, results §5, conclusions) and Tables … | UFL17; DOI 10.1287/mnsc.2016.2461; Benders anatomy |
| S012 | 1997 | Algorithms for railway crew management (Mathematical programming 79 (1), 125-141, 1…) | full | c2-01 (supersedes c01) | All 20 preprint pages ("Preprint submitted to Elsevier Science 4 June 1997", p. 1): §§1–4, Tables 1–2 (pp. 12, 18) and the references (pp. 18–20). … | — |
| S013 | 2001 | Solving the asymmetric travelling salesman problem with time windows… (Mathematical programming 90 (3), 475-506, 2…) | full | c02 | ZIB Preprint SC 99-31 (August 1999), all 35 file pages: text, Table 5.2, Tables 8.1–8.6 and the references. The column headings of Tables 8.1–8.5 are … | — |
| S014 | 2006 | An algorithmic framework for the exact solution of the prize-collect… (Mathematical programming 105 (2), 427-449,…) | full | c04 | Whole text pp. 1-25 (author preprint); all tables and figure captions read; the data of Figs. 1 and 4 survive only as stray numbers; reference list … | — |
| S015 | 2009 | The new Dutch timetable: The OR revolution (Interfaces 39 (1), 6-17, 2009) | full | c04 | Whole text, file pp. 1-13 (the published version from the UvA-DARE repository; file p. 1 is the repository cover sheet); Figs. 1-5 (map, bar charts … | — |
| S016 | 2017 | A new general-purpose algorithm for mixed-integer bilevel linear pro… (Operations Research 65 (6), 1615-1637, 2017) | full | c08 | File pp. 3-37 read closely (model, assumptions, FUB cuts, preprocessing, Theorems 1-6, separation MILPs, Algorithm 1, implementation, every … | the bilevel solver (2017) |
| S017 | 1998 | Modeling and solving the crew rostering problem (Operations research 46 (6), 820-830, 1998) | full | c2-01 (supersedes c02) | The whole technical report DEIS-OR-95-6(R) (26 file pages): cover (p. 1), abstract and introduction (pp. 2–4), the general model (pp. 4–11), bounds … | — |
| S018 | 2009 | Fast approaches to improve the robustness of a railway timetable (Transportation Science 43 (3), 321-335, 2009) | full | c05 | All 29 file pages: text, formulas, Tables 1-4, figure captions and references. Figures 1-9 survive only as axis ticks and legends, so their content … | — |
| S019 | 1994 | A branch-and-bound algorithm for the capacitated vehicle routing pro… (Operations Research 42 (5), 846-859, 1994) | abstract | a2-01 | — | — |
| S020 | 1993 | The delivery man problem and cumulative matroids (Operations Research 41 (6), 1055-1064, 1993) | abstract | a2-01 | — | — |
| S021 | 1989 | A branch and bound algorithm for the multiple depot vehicle scheduli… (Networks 19 (5), 531-548, 1989) | abstract | a2-01 | — | — |
| S022 | 1996 | {0, 1/2}-Chvátal-Gomory cuts (Mathematical Programming 74 (3), 221-235, 1…) | full | c01 | The whole 18-page author preprint ("November 1993, revised February 1995", p. 1) and its references were read. The prose is complete; many formulas … | — |
| S023 | 2016 | Benders decomposition without separability: A computational study fo… (European Journal of Operational Research 25…) | full | c07 | I read file pp. 1-28 of the preprint submitted to Elsevier on 7 February 2016: text, Tables 1-5 and references. Figures 1-2 extracted only as axis … | — |
| S024 | 2010 | A note on the selection of Benders’ cuts (Mathematical Programming 124 (1), 175-182,…) | full | c05 | All 8 file pages of the author preprint, titled "On the selection of Benders' cuts" and "Revised 23 February 2010": text, Tables 1-4 and references. … | his 2010 cut-selection rule (05 Q6) |
| S025 | 1995 | The precedence-constrained asymmetric traveling salesman polytope (Mathematical programming 68 (1), 241-265, 1…) | abstract | a2-01 | — | — |
| S026 | 2007 | A feasibility pump heuristic for general mixed-integer problems (Discrete Optimization 4 (1), 63-76, 2007) | full | c04 | Whole text pp. 1-23 (author preprint dated "May 31, 2005; Revised November 3, 2005", p. 1); all tables read; Figs. 3-5 are incumbent-over-time plots … | DOI 10.1016/j.disopt.2006.10.001 |
| S027 | 2018 | On the use of intersection cuts for bilevel optimization (Mathematical Programming 172 (1), 77-103, 2…) | full | s08 | (all 28 file pages: IRIS cover sheets pp. 1–2, manuscript pp. 3–28). First-page check: the manuscript is titled "Intersection cuts for bilevel … | — |
| S028 | 2000 | A polyhedral study of the asymmetric traveling salesman problem with… (Networks: An International Journal 36 (2),…) | full | s02 | (all 21 file pages; the file is ZIB Preprint SC 97–11 of February 1997, not the Networks printing; figures are extraction debris). First-page check … | — |
| S029 | 2016 | On handling indicator constraints in mixed integer programming (Computational Optimization and Applications…) | full | s07 | (all 18 file pages of the author preprint dated 24 April 2015: §§1–7, Tables 1–4). First-page check: title and Fischetti among the seven authors … | — |
| S030 | 1995 | The symmetric generalized traveling salesman polytope (Networks 26 (2), 113-123, 1995) | full | s01 | (all 25 file pages of the author preprint dated Bologna, February 28, 1995; figures are extraction debris, and the text layer drops ligatures such as … | — |
| S031 | 1989 | An additive bounding procedure for combinatorial optimization problems (Operations Research 37 (2), 319-328, 1989) | abstract | a2-01 | — | — |
| S032 | 2006 | A new ILP-based refinement heuristic for vehicle routing problems (Mathematical Programming 105 (2), 471-499,…) | full | s04 | (all 32 file pages of the Math. Program. manuscript, received May 23, 2004, revised October 13, 2004; the appendix, pp. 23–30, lists the routes of … | — |
| S033 | 2007 | Optimizing over the first Chvátal closure (Mathematical Programming 110 (1), 3-20, 2007) | full | c04 | Whole text pp. 1-14. Version check (as the work-list note asks): the file is the Mathematical Programming submission ("Received: July 28, 2005 / … | DOI 10.1007/s10107-006-0054-8 |
| S034 | 2005 | Reinventing crew scheduling at Netherlands Railways (Interfaces 35 (5), 393-401, 2005) | full | s04 | (all 23 file pages of the ERIM Report Series version ERS-2004-046-LIS, June 2004, not the Interfaces article; Figures 1–3 survive as captions only). … | — |
| S035 | 1994 | Weighted k-cardinality trees: Complexity and polyhedral structure (Networks 24 (1), 11-21, 1994) | abstract | a2-01 | — | — |
| S036 | 1993 | Heuristic algorithms for the multiple depot vehicle scheduling problem (Management Science 39 (1), 115-125, 1993) | abstract | a2-01 | — | — |
| S037 | 2011 | Heuristics in mixed integer programming (Wiley Encyclopedia of Operations Research a…) | abstract | a2-02 | — | — |
| S038 | 2019 | Interdiction Games and Monotonicity, with Application to Knapsack Pr… (INFORMS Journal on Computing 31 (2), 390-41…) | full | s09 | (all 28 pages of the author preprint titled "Interdiction Games and Monotonicity", without the journal subtitle; Figures 2–3 survive only as axis … | — |
| S039 | 1987 | The fixed job schedule problem with spread-time constraints (Operations Research 35 (6), 849-858, 1987) | abstract | a2-01 | — | — |
| S040 | 2017 | Thinning out Steiner trees: a node-based model for uniform edge costs (Math. Program. Comput. 9(2), 203-229) | full | c09 | on the preprint (the DIMACS 11 version, per the work-list note the author PDF thinning_out_Steiner_trees_dimacs11.pdf). Main text pp. 1-19 and … | DOI 10.1007/s12532-016-0111-0 |
| S041 | 2009 | Feasibility pump 2.0 (Mathematical Programming Computation 1 (2),…) | full | c05 | All 24 file pages: text, Figures 2-4 (pseudocode), Tables 1-5 and references. Figures 1 and 5 survive only as axis ticks; they are read through their … | DOI 10.1007/s12532-009-0007-3 (FP 2.0) |
| S042 | 2012 | A Lagrangian heuristic for robustness, with an application to train… (Transportation Science 46 (1), 124-133, 2012) | full | s07 | (all 16 file pages of the author preprint: abstract, §§1–7, Algorithm 1, Tables 1–5). First-page check: title and authors Cacchiani, Caprara … | — |
| S043 | 1997 | A polyhedral approach to the asymmetric traveling salesman problem (Management Science 43 (11), 1520-1536, 1997) | abstract | a2-01 | — | — |
| S044 | 1992 | An additive bounding procedure for the asymmetric travelling salesma… (Mathematical programming 53 (1), 173-197, 1…) | abstract | a2-01 | — | — |
| S045 | 2012 | Cutting plane versus compact formulations for uncertain (integer) li… (Mathematical Programming Computation 4, 239…) | abstract | a2-02 | — | — |
| S046 | 2009 | Mixed-integer programming models for nesting problems (Journal of Heuristics 15 (3), 201-226, 2009) | full | s05 | (all 34 file pages of the author preprint dated 18 September 2006, revised 20 September 2007; the text layer drops the "fi" and "ff" ligatures, e.g. … | — |
| S047 | 2002 | The generalized traveling salesman and orienteering problems (The traveling salesman problem and its vari…) | full | s03 | (the prose of file pp. 3–56; the text is an OCR layer of a pre-publication draft whose formulas and several table bodies (Tables 1.6, 1.7, 1.9, 1.10) … | — |
| S048 | 1989 | The fixed job schedule problem with working-time constraints (Operations Research 37 (3), 395-403, 1989) | abstract | a2-01 | — | — |
| S049 | 1988 | An additive approach for the optimal solution of the prize-collectin… (Publication of: Dalctraf, 1988) | full | s01 | (all 26 file pages; the prose is readable, but the numeric bodies of Tables 1–4 and Figures 1–4 are lost in the OCR layer, so no table numbers are … | — |
| S050 | 1997 | Branch-and-cut algorithms (Annotated bibliographies in combinatorial o…) | metadata | a2-02 | — | — |
| S051 | 2025 | Matheuristics by Examples (Handbook of Heuristics, 1-35, 2025) | abstract | a2-02 | — | — |
| S052 | 2014 | Proximity search for 0-1 mixed-integer convex programming (Journal of Heuristics 20 (6), 709-731, 2014) | full | c07 | I read file pp. 1-26: text, Tables 1-4 and references. Figures 2-4 extracted only as axis ticks and legends, so I read them through the text that … | PRX14; DOI 10.1007/s10732-014-9266-x |
| S053 | 1999 | Solution of large-scale railway crew planning problems: The Italian… (Computer-Aided Transit Scheduling: Proceedi…) | full | s01 | (all 17 file pages of the author preprint; ligatures dropped in the text layer). First-page check: title and authors Caprara, Fischetti, Guida, Toth … | — |
| S054 | 2017 | Deep neural networks as 0-1 mixed integer linear programs: A feasibi… (arXiv preprint arXiv:1712.06174, 2017) | full | s08 | (all 13 file pages of arXiv v1, 17 December 2017, p. 1). First-page check: title and authors Matteo Fischetti and Jason Jo match (p. 1). Per the work … | — |
| S055 | 2014 | Exploiting erraticism in search (Operations Research 62 (1), 114-122, 2014) | full | c07 | I read file pp. 1-13 of the revised manuscript OPRE-2012-05-278(R): text, Tables 1-5 and references. | ERR14; DOI 10.1287/opre.2013.1231 |
| S056 | 2002 | Exact methods for the asymmetric traveling salesman problem (The traveling salesman problem and its vari…) | full | s03 | (the prose of file pp. 3–39; OCR layer of a pre-publication draft whose formulas and table bodies (Tables 2.2–2.7) are only partly legible … | — |
| S057 | 2001 | A polyhedral approach to simplified crew scheduling and vehicle sche… (Management Science 47 (6), 833-850, 2001) | full | s02 | (all 32 file pages of the author preprint "Revised, December 2000"; the text layer drops the ligatures fi, ff and fl, and the figures are debris). … | — |
| S058 | 2000 | On the separation of maximally violated mod-k cuts (Mathematical Programming 87 (1), 37-56, 2000) | full | s02 | (all 20 file pages; figure debris on pp. 6, 8, 10–11, 13–14 skipped). First-page check: title and authors Caprara, Fischetti, Letchford match (p. 1) … | — |
| S059 | 2017 | Using a general-purpose mixed-integer linear programming solver for… (European Journal of Operational Research 26…) | full | c09 | on the preprint (the author preprint dated February 5, 2017). The whole text pp. 1-15: introduction, model description, Tables 1-2, conclusions, the … | DOI 10.1016/j.ejor.2017.04.057 (paper behind the TRI16 deck) |
| S060 | 1995 | Exact and approximate algorithms for the index selection problem in… (IEEE Transactions on Knowledge and Data Eng…) | full | s01 | (all 15 file pages: IEEE reprint cover p. 1, article pp. 2–14, back cover p. 15; OCR layer with partly garbled formulas and tables). First-page … | — |
| S061 | 2001 | Crew scheduling for Netherlands railways “destination: customer” (Computer-aided scheduling of public transpo…) | full | s02 | (all 15 file pages of an author manuscript with running page numbers; the map and the Gantt charts are not in the text layer). First-page check … | — |
| S062 | 1993 | A lifting procedure for the asymmetric traveling salesman polytope a… (Mathematical Programming 58 (1), 325-352, 1…) | abstract | a2-01 | — | — |
| S063 | 2013 | Backdoor branching (INFORMS Journal on Computing 25 (4), 693-70…) | full | c06 | Abstract and §§1-5 (pp. 1-11), Table 1 (pp. 9-10) and the pseudocode of Figures 1-2 (pp. 4, 7) read in full; references (pp. 11-13) skimmed. The file … | DOI 10.1287/ijoc.1120.0531 |
| S064 | 2004 | A local branching heuristic for mixed‐integer programs with 2‐level… (Networks: An International Journal 44 (2),…) | full | s03 | (all 23 file pages of the author preprint dated April 2003, revised October 2003; the figure on p. 15 is not in the text layer). First-page check … | — |
| S065 | 2000 | Frequency assignment in mobile radio systems using branch-and-cut te… (European Journal of Operational Research 12…) | abstract | a2-02 | — | — |
| S066 | 1996 | A heuristic algorithm for the set covering problem (International Conference on Integer Program…) | abstract | a2-01 | — | — |
| S067 | 2012 | Three ideas for the quadratic assignment problem (Operations research 60 (4), 954-964, 2012) | full | c06 | Abstract, §§1-5 (pp. 1-16), Tables 1-3 (pp. 10, 12, 15) and footnotes 1-3 (pp. 2, 12, 15) read in full; Figures 1-3 (pp. 3, 14, 15) read from … | DOI 10.1287/opre.1120.1073 |
| S068 | 2011 | On the separation of disjunctive cuts (Mathematical Programming 128 (1), 205-230,…) | full | s06 | (all 24 file pages of the manuscript, reference list skimmed; figure axes are extraction debris; the text ends with the set-covering section, without … | — |
| S069 | 1999 | Models and algorithms for the 2-dimensional cell suppression problem… (Mathematical Programming 84 (2), 1999) | full | s01 | (all 30 file pages; §1–6 read, Tables 1–5 on pp. 22–29 skimmed, figure debris skipped). First-page check: title and authors Fischetti and Salazar … | — |
| S070 | 2007 | Embedding {0, ½}-Cuts in a Branch-and-Cut Framework: A Computational… (INFORMS Journal on Computing 19 (2), 229-23…) | full | s04 | (all 16 file pages of the "Preliminary Draft, October 28, 2003", titled "Embedding Cuts in a Branch&Cut Framework: a Computational Study with {0 … | — |
| S071 | 1991 | Facets of the asymmetric traveling salesman polytope (Mathematics of Operations Research 16 (1),…) | abstract | a2-01 | — | — |
| S072 | 2001 | Solving the cell suppression problem on tabular data with linear con… (Management Science 47 (7), 1008-1027, 2001) | full | s02 | (all 20 file pages of the published article; the Greek dual-variable symbols are lost in the formulas). First-page check: title and authors Fischetti … | — |
| S073 | 2000 | Models and algorithms for optimizing cell suppression in tabular dat… (Journal of the American Statistical Associa…) | full | s02 | (all 13 file pages of a scanned print with an OCR text layer: the prose is readable with OCR errors, but the numbers in Tables 1–5 are partly garbled … | — |
| S074 | 2011 | Lexicography and degeneracy: can a pure cutting plane algorithm work? (Mathematical programming 130 (1), 153-176,…) | full | c06 | Abstract and §§1-8 (pp. 1-25) read in full; Tables 1-4 (pp. 11, 13, 18, 19) read, with exit codes and gap columns counted row by row; Figures 1-9 … | DOI 10.1007/s10107-009-0335-0 |
| S075 | 1992 | Approximation algorithms for fixed job schedule problems (Operations Research 40 (1-supplement-1), S9…) | abstract | a2-01 | — | — |
| S076 | 2022 | Learning to search in local branching (Proceedings of the aaai conference on artif…) | full | c10 | of the extended version arXiv v2. The file is arXiv 2112.02195v2 (3 Aug 2022), retitled "Revisiting local branching with a machine learning lens" and … | DOI 10.1609/aaai.v36i4.20294 |
| S077 | 2002 | Exact algorithms for minimum routing cost trees (Networks: An International Journal 39 (3),…) | full | s03 | (all 13 file pages). First-page check: title and authors Fischetti, Lancia, Serafini match (p. 1). | — |
| S078 | 2020 | Heuristic algorithms for the wind farm cable routing problem (Applied Energy 278, 115617, 2020) | full | s09 | (all 40 file pages: the DTU Orbit cover, p. 1, and the peer-reviewed manuscript dated 23 June 2019, pp. 2–40; the figures survive only as captions). … | — |
| S079 | 2020 | A branch-and-cut algorithm for mixed-integer bilinear programming (European Journal of Operational Research 28…) | full | c10 | Whole text pp. 1-21 (author preprint, "February 22, 2019; Revised, 20 September 2019", p. 1); Algorithms 1-2, Tables 1-4 and the captions of Figures … | BIL20; DOI 10.1016/j.ejor.2019.09.043 |
| S080 | 1993 | An efficient algorithm for the min-sum arborescence problem on compl… (ORSA Journal on Computing 5 (4), 426-434, 1…) | abstract | a2-01 | — | — |
| S081 | 2001 | Solution of real-world train timetabling problems (Proceedings of the 34th annual Hawaii inter…) | full | s02 | (all 24 file pages of an OCR text of a preprint; the prose is readable, but formulas are partly garbled and the numeric bodies of Tables 1–9 are … | — |
| S082 | 2018 | Array designer: automated optimized array design for functional near… (Neurophotonics 5 (3), 035010-035010, 2018) | full | s08 | (all 20 file pages: SPIE cover p. 1, the published open-access article pp. 2–20, CC BY 3.0, p. 2). First-page check: title and authors Brigadoi … | — |
| S083 | 2008 | Projected Chvátal–Gomory cuts for mixed integer linear programs (Mathematical Programming 113 (2), 241-257,…) | full | s05 | (all 16 file pages of the "preliminary draft: December 15, 2005", p. 1; the published version was not read). First-page check: title and authors … | — |
| S084 | 2000 | A polyhedral approach to an integer multicommodity flow problem (Discrete Applied Mathematics 101 (1-3), 13-…) | abstract | a2-02 | — | — |
| S085 | 2008 | Repairing MIP infeasibility through local branching (Computers & operations research 35 (5), 143…) | full | s05 | (all 10 file pages of the author preprint dated February 16, 2004, revised September 3, 2005; the journal version was not read). First-page check … | — |
| S086 | 2016 | Proximity Benders: a decomposition heuristic for stochastic programs (Journal of Heuristics 22 (2), 181-198, 2016) | partial | s07 | (all 13 file pages of the author preprint dated 7 December 2015, §§1–5 and Tables 1–3 read, but the text layer drops words and phrases throughout … | — |
| S087 | 2005 | Solving the prize-collecting Steiner tree problem to optimality (ALENEX/ANALCO 2005, 68-76, 2005) | full | s04 | (all 9 file pages; figure graphics are extraction debris, Tables 1–3 readable). First-page check: title and the six authors, Fischetti last with DEI … | — |
| S088 | 2019 | Introduction to mathematical optimization (M. Fischetti, 2019) | abstract | a2-02 | — | — |
| S089 | 1991 | Facets of two Steiner arborescence polyhedra (Mathematical Programming 51 (1-3), 401-419,…) | abstract | a2-01 | — | — |
| S090 | 2018 | A dynamic reformulation heuristic for Generalized Interdiction Probl… (European Journal of Operational Research 26…) | full | s08 | (all 31 file pages: IRIS cover sheets pp. 1–2, accepted manuscript pp. 3–31). First-page check: title and authors Fischetti, Monaci, Sinnl match (p. … | — |
| S091 | 2004 | Combinatorial Benders’ cuts (International Conference on Integer Program…) | abstract | a2-02 | — | — |
| S092 | 2018 | Least cost influence propagation in (social) networks (Mathematical Programming 170 (1), 293-325,…) | full | s08 | (all 25 file pages of the author preprint dated 3 May 2018, p. 1, appendix tables included). First-page check: title and authors Fischetti, Kahr … | — |
| S093 | 2003 | Partial cell suppression: a new methodology for statistical disclosu… (Statistics and Computing 13 (1), 13-21, 2003) | full | s03 | (all 9 file pages). First-page check: title and authors Fischetti and Salazar-González match (p. 1). | — |
| S094 | 2016 | Improving branch-and-cut performance by random sampling (Mathematical Programming Computation 8 (1),…) | full | c08 | pp. 1-17 read closely (text, Algorithm 1, Tables 1-7); appendix Table 8 (pp. 18-21) and the references (pp. 17-18) skimmed. | DOI 10.1007/s12532-015-0096-0 |
| S095 | 2011 | A relax-and-cut framework for Gomory mixed-integer cuts (Mathematical Programming Computation 3 (2),…) | full | s06 | (file pp. 1–19, the whole text; appendix Tables 8–11 on pp. 21–26 skimmed). First-page check: title and authors Fischetti, Salvagnin match (p. 1). | — |
| S096 | 2009 | Just MIP it! (MATHEURISTICS: Hybridizing metaheuristics a…) | full | s06 | (all 28 file pages of the author preprint, reference list skimmed; the text has no conclusions section and ends with the dominance experiments, p. … | — |
| S097 | 2017 | Orbital shrinking: Theory and applications (Discrete applied mathematics 222, 109-123,…) | full | c09 | on the preprint (the author manuscript, "Noname manuscript No.", p. 1). The whole text pp. 1-28: §§1-8 with all proofs, Tables 1-8, Figure 1 (its … | DOI 10.1016/j.dam.2017.01.015 |
| S098 | 2014 | Boosting the feasibility pump (Mathematical Programming Computation 6 (3),…) | full | c07 | I read file pp. 1-32 of an undated author manuscript, whose web references were "Last accessed 24/05/11" (pp. 25-26): text, algorithms and … | DOI 10.1007/s12532-014-0068-9 (Boosting FP) |
| S099 | 1989 | New lower bounds for the symmetric travelling salesman problem (Mathematical Programming 45 (1), 233-254, 1…) | abstract | a2-01 | — | — |
| S100 | 2023 | Safe distancing in the time of COVID-19 (European journal of operational research 30…) | full | s10 | (all 24 file pages: repository cover p. 1, accepted author manuscript pp. 2–22, references pp. 21–24; the figures are not in the text layer, so only … | — |
| S101 | 2008 | The linear ordering problem with cumulative costs (European Journal of Operational Research 18…) | full | s05 | (all 19 file pages of the author preprint dated October 13, 2004; Figures 1–3 survive only as captions and axis labels; the journal version was not … | — |
| S102 | 2002 | Polyhedral theory for the asymmetric traveling salesman problem (The traveling salesman problem and its vari…) | full | s03 | (file pp. 1–47 of the preprint dated January 2001 and marked "Book Chapter"; figures are extraction debris; references pp. 47–49 skimmed). First-page … | — |
| S103 | 2023 | Integrated layout and cable routing in wind farm optimal design (Management Science 69 (4), 2147-2164, 2023) | abstract | a2-02 | — | — |
| S104 | 1988 | A new dominance procedure for combinatorial optimization problems (Operations Research Letters 7 (4), 181-187,…) | abstract | a2-01 | — | DOI 10.1016/0167-6377(88)90025-9 |
| S105 | 2003 | Solving real-world ATSP instances by branch-and-cut (Combinatorial Optimization—Eureka, You Shri…) | abstract | a2-02 | — | — |
| S106 | 2010 | An in-out approach to disjunctive optimization (International Conference on Integration of…) | full | c05 | All 5 file pages of the extended abstract: abstract, §§1-4, Table 1 and references. First-page check: title and authors Fischetti, Salvagnin match … | DOI 10.1007/978-3-642-13520-0_17 |
| S107 | 1997 | On the monotonization of polyhedra (Mathematical Programming 78 (1), 59-84, 1997) | abstract | a2-02 | — | — |
| S108 | 1987 | Worst-case analysis of the differencing method for the partition pro… (Mathematical Programming: Series A and B 37…) | abstract | a2-01 | — | — |
| S109 | 2016 | Fast training of support vector machines with Gaussian kernel (Discrete Optimization 22, 183-194, 2016) | full | s08 | (all 19 file pages of the author preprint). First-page check: title and sole author Matteo Fischetti match (p. 1). | — |
| S110 | 2021 | Embedding Simulated Annealing within Stochastic Gradient Descent (OLA 2021 (Communications in Computer and In…) | full | s09 | (all 12 pages of an author copy in CCIS layout, without DOI or venue on the page; figures read through captions). First-page check: title and authors … | — |
| S111 | 2014 | Self-splitting of workload in parallel computation (International Conference on Integration of…) | full | s07 | (all 12 file pages of the author copy: §§1–5, Table 1). First-page check: title and authors Fischetti, Monaci, Salvagnin match (p. 1). | — |
| S112 | 2009 | Minimal infeasible subsystems and Benders cuts (Mathematical Programming to appear, 2009) | full | s06 | (all 17 file pages of the undated manuscript, with Tables 1–3 and Figures 1–2). First-page check: title and authors Fischetti, Salvagnin, Zanette … | — |
| S113 | 1992 | The fixed-outdegree 1-arborescence polytope (Mathematics of Operations Research 17 (4),…) | abstract | a2-01 | — | — |
| S114 | 1995 | Experiments with a multi-commodity formulation for the symmetric cap… (Proceedings of the 3rd Meeting of the EURO…) | full | s01 | (all 5 file pages of the preprint dated Bologna, April 30, 1995; ligatures dropped in the text layer). First-page check: title and authors Fischetti … | — |
| S115 | 2008 | How tight is the corner relaxation? (Discrete Optimization 5 (2), 262-269, 2008) | full | s05 | (all 11 file pages of the author preprint dated October 25, 2005, revised April 30, 2006; the journal version was not read). First-page check: title … | — |
| S116 | 1995 | Clique tree inequalities define facets of the asymmetric traveling s… (Discrete Applied Mathematics 56 (1), 9-18,…) | abstract | a2-01 | — | — |
| S117 | 2015 | MIP‐and‐refine matheuristic for smart grid energy management (International Transactions in Operational R…) | full | s07 | (all 18 file pages of the author preprint dated October 2012, revised 13 March 2013: §§1–6, Algorithm 1, Table 1). First-page check: title (with a … | — |
| S118 | 2007 | Mixed-integer cuts from cyclic groups (Mathematical Programming 109 (1), 27-53, 2007) | full | s04 | (all 29 file pages of the preprint dated September 10, 2005, which says that an earlier version was presented at IPCO XI in Berlin, June 2005 (p. 3) … | — |
| S119 | 2000 | Scheduling train drivers and guards: the Dutch" Noord-Oost" case (Proceedings of the 33rd Annual Hawaii Inter…) | abstract | a2-02 | — | — |
| S120 | 1999 | Lifted cycle inequalities for the asymmetric traveling salesman prob… (Mathematics of Operations Research 24 (2),…) | abstract | a2-02 | — | — |
| S121 | 1997 | A branch‐and‐cut algorithm for the resource‐constrained minimum‐weig… (Networks: An International Journal 29 (1),…) | abstract | a2-02 | — | — |
| S122 | 1988 | A hybrid algorithm for finding the kth smallest of n elements in O (… (Annals of Operations Research 13 (1), 399-4…) | abstract | a2-01 | — | — |
| S123 | 2016 | Mixed-Integer Linear Programming Heuristics for the PrePack Optimiza… (Discret. Optim. 22, 195-205) | full | s08 | (all 20 file pages of the author preprint submitted on 11 March 2015, p. 1). First-page check: title and authors Fischetti, Monaci, Salvagnin match … | — |
| S124 | 2010 | Pruning moves (INFORMS Journal on Computing 22 (1), 108-11…) | full | c06 | Abstract and §§1-7 (pp. 1-23) read in full, including Tables 1-6 (pp. 16-22) and the worked example of Figure 1 (pp. 6-8, read from the extracted … | DOI 10.1287/ijoc.1090.0329 (Pruning Moves) |
| S125 | 2001 | A branch-and-cut algorithm for the multiple depot vehicle scheduling… (—) | full | s02 | (all 25 file pages of the author PDF, undated, citing a 1999 oral communication, p. 24; the text layer drops ligatures). First-page check: title and … | — |
| S126 | 2025 | A fix-propagate-repair heuristic for mixed integer programming (Mathematical Programming Computation 17 (1)…) | full | c11 | — | — |
| S128 | 1992 | Three Facet-Lifting Theorems for the Asymmetric Traveling Salesman P… (IPCO, 260-273, 1992) | metadata | a2-01 | — | — |
| S129 | 2006 | Robust optimization through branch-and-price (Proceedings of the 37th annual conference o…) | metadata | a2-02 | — | — |
| S130 | 2022 | An integrated local-search/set-partitioning refinement heuristic for… (Mathematical Programming Computation 14 (4)…) | full | s09 | (all 27 pages of the MPC manuscript dated 14 June 2022; the box plots of Figs. 2–4 survive only as labels). First-page check: title and authors … | — |
| S131 | 2015 | Optimal turbine allocation for offshore and onshore wind farms (Optimization in the Real World: Toward Solv…) | abstract | a2-02 | — | — |
| S132 | 2007 | Integer Programming and Combinatorial Optimization: 12th Internation… (Springer, LNCS 4513, 2007 (editors M. Fisch…) | full | s3-01 | (all 8 file pages of the open front matter: series page, title page, imprint, preface, committee page and three contents pages; the 36 papers, by … | — |
| S133 | 2018 | Faster SGD training by minibatch persistency (arXiv preprint arXiv:1806.07353, 2018) | full | c10 | Whole text pp. 1-7 (arXiv v1, 19 Jun 2018, marked "Preprint. Work in progress.", p. 1); Figures 1-5 survive only as captions and axis labels (pp. … | arXiv 1806.07353 |
| S134 | 2010 | On the knapsack closure of 0-1 Integer Linear Programs (Electronic Notes in Discrete Mathematics 36…) | full | s06 | (all 6 file pages; equation numbers are displaced in the extraction, the text is readable). First-page check: title and authors Fischetti, Lodi match … | — |
| S135 | 2003 | Optimisation of the interconnecting network of a UMTS radio mobile t… (European Journal of Operational Research 14…) | full | s03 | (all 12 file pages). First-page check: title and authors Fischetti, Romanin Jacur, Salazar González match (p. 1). | — |
| S137 | 2018 | Chasing first queens by integer programming (International Conference on the Integration…) | full | s09 | (all 14 file pages of the author preprint dated 10 January 2018; the appendix solution lists, pp. 9–12, read as data). First-page check: title and … | — |
| S139 | 1999 | On the Separation of Maximally Violated mod-k Cuts (International Conference on Integer Program…) | full | s01 | (all 12 file pages of the author copy, which has no printed page numbers; figure debris skipped). First-page check: title and authors Caprara … | — |
| S140 | 2006 | New facets of the STS polytope generated from known facets of the AT… (Discrete Optimization 3 (1), 3-19, 2006) | full | s04 | (all 32 file pages of the preprint dated January 12, 2005; figures of inequality supports and lifting trees are extraction debris, the text, theorems … | — |
| S141 | 1990 | A new linear storage, polynomial-time approximation scheme for the s… (Discrete applied mathematics 26 (1), 61-77,…) | abstract | a2-01 | — | — |
| S142 | 2007 | Mipping closures: An instant survey (Graphs and Combinatorics 23 (Suppl 1), 233-…) | full | s04 | (all 12 file pages of an undated author preprint titled "MIPping closures: an instant survey"). First-page check: title and Fischetti, Lodi match (p. … | — |
| S143 | 2026 | EndoWake: Modeling wind by linear programming for wind farm layout o… (arXiv preprint arXiv:2609.40157, 2026) | full | c11 | — | — |
| S144 | 2026 | Models and algorithms for the time window assignment traveling sales… (European Journal of Operational Research 32…) | full | c11 | — | the 2025 order (06 §3.1) |
| S145 | 2017 | Integer (Linear) Optimization (Advances and Trends in Optimization with En…) | full | c10 | Whole text pp. 1-19 (author preprint): body pp. 1-16, reference list pp. 16-19 skimmed; Fig. 1 survives only as labels (p. 7) and the displayed … | — |
| S147 | 1998 | An LP-based heuristic approach to the crew scheduling problem (Proceedings TRISTAN III, 1998) | metadata | a2-02 | — | — |
| S150 | 2026 | GPU-accelerated wind farm layout search with a distilled endogenous… (arXiv preprint arXiv:2610.07844, 2026) | full | c12 | All of pp. 1–34 (abstract, §§1–8, funding, acknowledgments, AI declaration, CRediT, data availability, appendices A–C); references pp. 34–40 skimmed. … | — |
| S151 | 2025 | Column Generation Algorithms for the Pickup and Delivery Problem wit… (Beyond Frontiers of Operations Research: Em…) | abstract | a2-02 | — | — |
| S152 | 2017 | Comments on: On learning and branching: a survey (Top 2 (25), 237-238, 2017) | metadata | a2-02 | — | — |
| S154 | 2014 | Proximity search heuristics for Mixed Integer Programs (Proceedings of the 26th RAMP Symposium, Hos…) | full | s3-01 | (all 12 file pages = printed pp. 159–170: abstract, §§1–4, Tables 1–2, acknowledgements and references). The text is OCR: most formulas, including … | — |
| S161 | 2026 | Just sort it! A note on the LP behind rank-one anti-loop edits (arXiv preprint arXiv:2611.21432, 2026) | full | c12 | All of pp. 1–4 (abstract, §§1–4, Role of AI, data and code, references). Version read: arXiv:2611.21432v1 [cs.LG] (16 Nov 2026, p. 1); title and sole … | — |
| S162 | 2026 | A Dantzig-Wolfe reformulation of the EndoWake model for optimal wind… (arXiv preprint arXiv:2610.39503, 2026) | full | c12 | All of pp. 1–23 (abstract, §§1–8, appendices A–B, data availability, CRediT, acknowledgments, AI declaration); references pp. 23–25 skimmed. Version … | — |
| S163 | 2026 | Minibatch persistency, eight years later: what batch reuse costs in… (arXiv preprint arXiv:2609.13922, 2026) | full | c12 | All of pp. 1–29 (abstract, §§1–8, acknowledgments) and appendices A–C (pp. 31–36); references pp. 29–31 skimmed; the figures are present only as … | MBP26; arXiv 2609.13922 |
| S164 | 2026 | Feasibility Pump with Objective Cutoff: A Computational Study (—) | full | c13 | Abstract and §§1-8 (pp. 1-20) read in full; Appendix A, Tables 5-9 (pp. 20-23), read in full; references (pp. 24-25) and Statements and Declarations … | FPC26; 2026 pump study (Zenodo 10.5281/zenodo.22810777) |
| S165 | 2026 | A digital twin of Fermat in 1637: reconstructing the marvellous proo… (—) | metadata | a2-03 | — | — |
| S166 | 2025 | An improved compact formulation for the assortment optimization prob… (Journal of the Operational Research Society…) | abstract | a2-03 | — | — |
| S168 | 2022 | A Vehicle Routing heuristic based on accelerated LKH-3 coupled with… (12th DIMACS Implementation Challenge: Vehic…) | full | s09 | (all 7 pages; no printed page numbers). First-page check: title and authors Francesco Cavaliere, Matteo Fischetti, Keld Helsgaun match (p. 1). | — |
| S170 | 2013 | Proximity Search (10th Metaheuristics International Conferenc…) | metadata | a2-02 | — | — |
| S171 | 2013 | Alberto Caprara (1968-2012): Scientific Contributions (OPTIMA, 1-11, 2013) | full | s07 | for the article (file pp. 1–11: text pp. 1–9 read in full, the reference list pp. 9–11 checked); the rest of the issue (pp. 11–16: "Memories" by … | — |
| S172 | 2025 | A Benders Decomposition Approach to the Time Window Assignment Trave… (ODS 2025, International Conference on Optim…) | full | c11 | — | — |
| S173 | 2010 | Towards a MIP-Cut metascheme (International Conference on Integration of…) | abstract | a2-02 | — | — |
| S174 | 2009 | Yoyo search: a bisection cutting-plane method (—) | full | s06 | (all 13 file pages of the manuscript dated 20 November 2009, with Tables 1–4). First-page check: title and authors Fischetti, Salvagnin match (p. 1). | the 2009 yoyo search manuscript |
| S178 | 2008 | ATMOS 2008 Preface--8th Workshop on Algorithmic Approaches for Trans… (8th Workshop on Algorithmic Approaches for…) | full | s05 | (all 5 file pages: title page, imprint, series page and the two-page preface). First-page check: "Edited by" Matteo Fischetti and Peter Widmayer (p. … | — |
| S180 | 2001 | Combining complete and partial cell suppression methodologies in sta… (Statistical Journal of the United Nations E…) | full | s03 | (all 7 file pages). First-page check: title and authors Matteo Fischetti and Juan-José Salazar-González match (p. 1). The relation symbols (≤, ≥) of … | — |
| S184 | 1994 | Odd cut-sets, odd cycles, and 0-1/2 Chvatal-Gomory cuts (Univ. of Michigan, Ann Arbor, MI (United St…) | abstract | a2-01 | — | — |
| S185 | 1987 | Modelli e algoritmi per problemi di routing e di scheduling dottorat… (Alma Mater Studiorum-Università di Bologna,…) | metadata | a2-01 | — | — |
| S186 | 2026 | Replication package for" EndoWake: Modeling Wind by Linear Programmi… (Zenodo, 0) | abstract | a2-03 | — | — |
| S187 | — | Technical note for GPU-accelerated wind farm layout search with a di… (—) | metadata | a2-03 | — | — |
| S188 | 1996 | Optimización combinatoria poliédrica: problemas de rutas-localización (Doctoral thesis, Universidad de La Laguna (…) | abstract | a2-03 | — | — |
| S189 | — | Exact and approximate algorithms for bus driver scheduling problems… (—) | metadata | a2-03 | — | — |
| S190 | 2019 | Intersection Cuts for Quadratic Mixed-Integer Optimization (ODS 2019, Genova, 4-7 September 2019 (slide…) | full | s3-01 | (all 16 slides as text; formulas and the results of slides 13–15 are images missing from the text layer, so those slides give titles only). … | — |
| S192 | 2020 | Metaheuristic frameworks for deep neural network training (Master's thesis, University of Padova (cand…) | abstract | a2-03 | — | — |
| S194 | 2017 | Exact Algorithms for Mixed-Integer Bilevel Linear Programming (Lunteren Conference on the Mathematics of O…) | full | s3-01 | (all 21 slides as text; the formulas, the example's plots and the body of slide 20, on numerically safe intersection cuts, are images missing from … | — |
| S195 | — | Thinning out facilities: Lagrange, Benders, and (—) | full | s10 | (all 31 file pages: text pp. 1–23 and 26–28, Tables 1–5 pp. 22 and 24–27, references pp. 28–31; Figures 1 and 2 survive only as axis labels and cut … | (report form of UFL17) |
| S196 | 2016 | Solving Congested Facility Location by Branch-and-Cut (ROADEF 2016, 17th ROADEF conference, Compiè…) | abstract | a2-03 | — | — |
| S198 | 2004 | Exact and Heuristic Methods for Nesting Problems (Report, DEI, University of Padova, 1 April…) | full | s3-01 | (all 81 file pages: front matter, Chapters 1–7, acknowledgements, Appendix A and the bibliography; the figures survive only as labels and sub- and … | — |
