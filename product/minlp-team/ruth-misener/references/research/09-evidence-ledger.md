# Ruth Misener · Evidence ledger

## Contents

- [Taste: marks of good research](#taste-marks) · [Taste: warning signs](#taste-warnings)
- [Method 1](#method-1) · [Method 2](#method-2) · [Method 3](#method-3) · [Method 4](#method-4) · [Method 5](#method-5)
- [Heuristics 1–11](#heuristic-1) ([4](#heuristic-4), [6](#heuristic-6), [10](#heuristic-10), [11](#heuristic-11))
- [Workflows and routing](#workflows)
- Anatomies: [APOGEE](#anatomy-apogee) · [GloMIQO](#anatomy-glomiqo) · [ANTIGONE](#anatomy-antigone) · [trained models](#anatomy-trained-models) · [P-split](#anatomy-p-split) · [LMTD](#anatomy-lmtd) · [GALINI](#anatomy-galini)
- [Anti-patterns](#anti-patterns) · [Trajectory](#trajectory) · [Inner tensions](#inner-tensions)
- [Honest Boundary](#honest-boundary) · [Corrections](#corrections) · [Sources](#sources) · [Card key](#card-key)

> Date: 2026-11-19 (stage T3.6, first synthesis round). The full evidence behind `../../SKILL.md`. SKILL.md keeps, per item, the strongest statement and cards, a one-line say–do count, at most four variant/correction bullets and a pointer to the matching section here. Each section below has up to four parts: **Full-text evidence** (copied from `08-deep-reading-synthesis.md`, which is traceable to `cards/`), **Variants and contradictions** (08 §3), **Added in T3.6** (what this pass wrote into SKILL.md, with card ids) and **Before T3.6 (moved verbatim)** (the SKILL.md item as it stood on 2026-10-10, built from web research, so nothing is lost; its `[02 L1.4]`-style citations point to the web-research notes `01-…06-*.md` in this folder, and its links were re-pointed to work from this folder).

**How to read.** `[S011 p. 17]` is paper card S011 in [07-paper-cards.md](07-paper-cards.md), at the page of the file the card read (mostly an arXiv or author preprint; journal pagination was not read; check the journal page before citing it in a paper). Abstract- and metadata-level cards are cited without pages. Per-card method links (✅ evidence, ⚠ variant, ✗ contradiction) are in the `Methods linked` column of 07; proof devices (P), design moves (D), experiment protocols (E) and writing moves (WM; renamed from W on 2026-11-19 so they do not collide with her written statements W1-W14 of note 02) are in [../technique-catalog.md](../technique-catalog.md). Quotation marks enclose only text copied from a card's verified quote list (`verify_card_quotes.py`, 2026-11-19: 222 quotes, 222 exact) or from the pre-synthesis SKILL.md (whose quotes come from the web-research notes; spoken quotes are YouTube auto-captions, ASR). Cards that record typos or internal inconsistencies of a paper are reading notes and are not used here; 08 §7.4 keeps one neutral general lesson.

**Scope.** Sections exist for every SKILL.md item that this pass condensed or changed: the two taste lists, Methods 1–5, Heuristics 1–11, the workflows, the seven signature-work anatomies (since the fix pass, LMTD and GALINI only here), the anti-patterns, the trajectory, the inner tensions, the Honest Boundary, the corrections, the sources moved out of SKILL.md and the card key. The routing table, the Agentic Protocol and the Roundtable Card additions are recorded under [Workflows and routing](#workflows). Frontmatter, Activation Rules (only the first-activation disclaimer changed), Answer Standard, Research Integrity Rules, the taste quick-check, Mentor Voice and Academic Lineage are complete in SKILL.md.

**Fix pass (2026-11-19, after three read-only reviews).** Four claims were corrected (Method 1's detection line, Method 5 step 6's citation, the LMTD minimum evidence, Heuristic 2's Royal Mail case); the LMTD and GALINI anatomies and some T3.6 bookkeeping moved back here; Heuristic 6 was folded into Heuristic 4; the catalog's writing moves became WM1-WM10. Each affected section has a **Fix pass** line saying what changed and keeps the text it replaced; replaced T3.6 SKILL.md wording is set in italics, not quotation marks, since it is neither card text nor pre-synthesis text.

**Tighten pass (2026-11-19, stage T3.7).** SKILL.md was condensed from 12030 to 11370 words (`wc -w`) without loss. Every SKILL.md line this pass shortened is kept here word for word, in a **Before T3.7 (moved verbatim)** part at the end of its section: Methods 1–5, both taste lists, Heuristics 1, 2, 4, 5, 7, 8, 9, 10 and 11, the routing row on solver choice and two rows of the stages table (under [Workflows and routing](#workflows)), the trajectory's Latest paragraph and three inner tensions. SKILL.md keeps each method's strongest statement and at most three cards per heuristic; Heuristics 1, 2, 10 and 11 now cite their sources without quoting them (the quotes are here); the extra quotes, case lists, case DOIs and the examples behind the stop rules are here. This partly reverses the fix pass (Method 1's detection bullet, the Stated pointers of Methods 2 and 4, Heuristic 4's long-horizon examples, the per-step and per-gate cards of Heuristics 10 and 11, the stages table's drafting quote and MEng sentence) and drops T3.6's WM2 cards from the drafting row; the **Fix pass** lines in those sections describe the state before T3.7, which is the text of each **Before T3.7** part, and each of those parts says what T3.7 cut. Frontmatter, How to Use, Activation Rules, Answer Standard, Research Integrity Rules, the anatomies, the Roundtable Card, the Honest Boundary and its corrections list were not changed.

**T3.7 fix round (2026-11-19, after a read-only review).** Eight minor findings, each checked against the cards, the notes or the full text before use; SKILL.md went from 11370 to 11493 words. Back in SKILL.md: Method 1's stop-rule parenthetical on the withdrawn theorem, word for word [03 PE-34]; Method 2's written-statement pointer (C9, W9), the contradiction named in its say–do line [S056 p. 16], the P-split journal outcome in step 6 with the abstract's qualifier outside the quotation marks [S046 p. 1] (card c16 confirms the claim on pp. 1 and 26; the quoted words are the abstract's, and the conclusion restates them in other words), and the NeurIPS reviewer's request worded as asked [03 §5.5]; Method 3 step 7's role sentence, now marked inferred as 03 PE-41 marks it; Method 4's T6 pointer as the fix pass had it, and the card's GloMIQO default sentence in step 4 [S004 p. 13]; Heuristic 1's broken assumption as a paraphrase (T10 [45:19]); Heuristic 10's cards for steps 3 and 7 [S045 p. 30; S055 pp. 11–12], still three cards in all. Each section's **Before T3.7** part gives the details; T3.7 wording that this round replaced is set in italics there. In this ledger: the routing row moved under [Workflows and routing](#workflows) has a three-column header again (under a two-column header GFM drops a row's third cell), and a claim-audit note follows the supervision row. Rows 13, 14, 16 and 17 of [10-claim-audit.md](10-claim-audit.md) cite SKILL.md lines whose audited clauses are no longer in SKILL.md: they are here ([Workflows and routing](#workflows), [Heuristic 11](#heuristic-11)), and the cards of rows 13 and 16-17 also in catalog WM2 and D3; that file is append-only and outside this step, so its dated note is left to the operator, as is narrowing its k=8 partial (Method 3 Practice, [S081 pp. 6, 26–28]), which predates T3.7.

<a id="taste-marks"></a>

## Taste: marks of good research

### Added in T3.6

- Mark 1: her essay frames Floudas's contribution as pushing the tractability boundary through applications [S143 p. 12]; the GloMIQO paper leaves open whether "a slower solution time on the smaller problems is a price we pay for addressing the exceptionally large problems" [S004 p. 26].
- Mark 2: the essay quote now has its card page, "But Chris was never interested in toy problems or proofs of concept." [S143 p. 13]; the 2571-instance suite with freeze date and exclusion rule [S001 pp. 8–10; S123 p. 1]; a test of a new relaxation on a real application model with tens of thousands of variables before calling it relevant [S143 p. 13].
- Mark 3: "This suggests that MILP solvers are not necessarily best used as black boxes, but application-specific considerations can help to improve their effectiveness." [S005 p. 7]; "researchers may be able to find and exploit special mathematical structure for particular problem classes" [S145 p. 3].
- Mark 4: the practitioner's operating constraints become first-class objects of the formulation: cost of moving and delayed observations [S039 pp. 3–4, 7, 9], measurement delay and costly initial-condition switches [S086 pp. 1, 6], transition constraints [S059 pp. 4–7], NChooseK and similar constraint types [S044 pp. 2–3] (08 §2.6, H1).
- Mark 5: runtime plug-ins for developers in GALINI [S087 pp. 2–4]; switchable formulations [S006 p. 4]; a polymorphic term class [S001 pp. 4, 8]; plug-in detectors [S068 pp. 9–10] (catalog D4).
- **Fix pass**: two T3.6 clauses left SKILL.md and stay only here (former SKILL.md wording in italics, here and below): mark 1's *her essay credits Floudas with pushing that boundary through applications [S143 p. 12]* (her account of her advisor, not her own taste) and mark 5's *GALINI's runtime plug-ins [S087 pp. 2–4]* (repeated in Workflow B step 5).

### Before T3.6 (moved verbatim)

1. **It moves the tractability boundary**; a 10% speed-up is a solver company's job. "I want to be able to solve problems that other places can't solve" (T7 [32:22], ASR); W11 [02 L1.1, C2].
2. **It is tested on real, application-sized instances.** Floudas "was never interested in toy problems or proofs of concept" (essay W1, p. 13); practice: 2571 problems for ANTIGONE, the rebuilt minlp.org set [03 PE-01, PE-02].
3. **It exploits structure ("insider information")**, not a black box: her most repeated belief, 7 sources 2014-2023 [02 C1]; "this isn't just black box optimization right ... there's an underlying structure" (T2 [56:12], ASR).
4. **Good problems are messy: several complications at once.** "I am not the kind of academic who wishes to live in an ivory tower" (T8 [30:04], ASR); Heuristic 1 [02 C12, C14].
5. **It ends in software others can extend or switch**: ANTIGONE architected for future term classes [03 PE-29]; OMLT's switchable formulations [01 SW4]; [02 C7, C15].

### Before T3.7 (moved verbatim)

Condensed in SKILL.md on 2026-11-19 (stage T3.7, tighten). The SKILL.md text as it stood before this pass, word for word:

*Mark 3:*

3. **It exploits structure ("insider information")**, not a black box: her most repeated belief, 7 sources 2014-2023 [02 C1]; "this isn't just black box optimization right ... there's an underlying structure" (T2 [56:12], ASR); in print, "MILP solvers are not necessarily best used as black boxes" [S005 p. 7].

*Mark 4:*

4. **Good problems are messy: several complications at once.** "I am not the kind of academic who wishes to live in an ivory tower" (T8 [30:04], ASR); Heuristic 1 [02 C12, C14]; operating constraints become formulation objects [S039 pp. 3–4; S086 pp. 1, 6].

<a id="taste-warnings"></a>

## Taste: warning signs of bad research

### Added in T3.6

- Warning 1: exactly one parameter setting across all 399 GloMIQO runs [S004 p. 13]; "We show the method is robust to the choice of its single hyper-parameter and provide a parameter-free alternative." [S039 p. 1].
- Warning 2: her group withholds strengthenings only its own method could use: "Our numerical comparisons do not include locally valid bounds on the α-variables, as such bounds are typically not easily obtainable and could give the P-split formulations an unfair advantage." [S046 p. 17]; solver parameters fixed across formulations, "The default (automatic) parameter selection in Gurobi caused large variations in the results that were due to different solution strategies rather than differences between formulations." [S040 p. 11].
- Warning 3: the SnAKe paper fixes the stuck-at-local-optimum failure of naive resampling with ε-Point Deletion [S039 pp. 3–7]; the do-not-use statements of Heuristic 7 are the printed form of the second half of this warning [S003 p. 9; S081 p. 9].

### Before T3.6 (moved verbatim)

1. **A new parameter without evidence that one setting works across a class**, or re-tuned per comparison: "I introduced a parameter I don't like to introduce parameters" (T11 [29:40], ASR); T2 [21:05] (Integrity Rule 4) [02 L1.7, C4].
2. **Winning on a metric you invented, over a weakened baseline, or outside the class that carries the result**: T11 [29:52]; "data sets that happen to be perfect for my research" (T1 [17:10], ASR); Dagstuhl working group (joint): "users of solver software should not rely on simplistic comparisons" (doi:10.4230/DagRep.8.2.64).
3. **A design that defeats its own purpose, or a method outside its domain**: SnAKe, "I had taken a global optimization method and I had turned it into a local optimization method" (T11 [26:06], ASR); "one thing i really dislike is techno solutionism" (T1 [27:54], ASR) [02 L1.9, L5.4].

### Before T3.7 (moved verbatim)

Condensed in SKILL.md on 2026-11-19 (stage T3.7, tighten). The SKILL.md text as it stood before this pass, word for word:

*Warning 2:*

2. **Winning on a metric you invented, over a weakened baseline, or outside the class that carries the result**: T11 [29:52]; "data sets that happen to be perfect for my research" (T1 [17:10], ASR); Dagstuhl working group (joint): "users of solver software should not rely on simplistic comparisons" (doi:10.4230/DagRep.8.2.64); bounds withheld that "could give the P-split formulations an unfair advantage" [S046 p. 17].

<a id="method-1"></a>

## Method 1: Structure detection as "insider information"

### Full-text evidence (08 §2, copied)

- **Strongest cards**:
  - Reading the model as written, in 2010: the EPA emissions law read for structure the predecessor model missed, "closer examination (Figure 1) shows that the function is, without approximation, piecewise-linear." [S025 p. 13]; redundant tracking and binaries removed and an edge-concave remainder found, each exploited in the relaxation [S025 pp. 2-3, 10, 17-18, 23]. This is the earliest instance in the corpus.
  - The recognition layer in her solvers: reformulation and detection before relaxation, the detected structure reused for bounding [S004 pp. 4-11]; term classes with convexity and edge-concavity labels [S001 pp. 4-8]; term classes in an inheritance hierarchy with polymorphic relaxation choice and an interval-Hessian edge-concavity test [S032 pp. 6, 10-12].
  - Her single-author statement of 2014: "researchers may be able to find and exploit special mathematical structure for particular problem classes" [S145 p. 3].
  - Plot, prove, exploit: the reciprocal of LMTD plotted, read as convex, proved and exploited with tangent cuts [S024 pp. 10-17]; the student's account in the supervised MEng report, "We see from Figure 3.1 that the reciprocal of LMTD has a shape that looks convex (where defined, the epigraph looks convex), we will not only prove that this is true but we will use this to form a suitable approximation." [S100 p. 42].
  - The detector validated like an instrument: "SUSPECT does not have false positives on the test set, this gives confidence in the implementation and makes it possible to use it for solver selection." [S068 p. 10], every miss listed [S068 pp. 29-31]; the SKILL.md numbers (1527 problems; 1275 of 1392 matched) are confirmed [S068 p. 10].
  - Step 4 in code, structure carried by the modelling object: "The advantage of this approach is that, although GALINI itself is unaware of the pooling problem, GALINI can, through this library, behave as if it has perfect knowledge of its structure." [S072 p. 2].
  - Verification and graphs: dependencies between ReLU states exploited, "This suggests that MILP solvers are not necessarily best used as black boxes, but application-specific considerations can help to improve their effectiveness." [S005 p. 7]; graph symmetry the solver cannot see, "However, because the MIP solver does not have access to the input graph structure, it needs to consider all possible automorphic graphs with 616 + 411 nodes." [S051 p. 6], removed by constraints whose completeness is proved [S051 pp. 4-6; S128 pp. 10-15]; topology and perturbation budgets used for bounds that interval arithmetic ignores [S050 pp. 4-5, 9].
- **Say–do update**: stated and practised from 2010 [S025 pp. 3, 13] to 2025 [S128 pp. 10-16]; keep ✅. Three corrections of detail:
  1. Step 6 (exploit and measure inside the full B&B) is missing in the detection-line papers: symmetry characterised without exploitation [S076 p. 5], detection without any B&B run [S120 p. 19], one six-point experiment [S091 pp. 7-10], detection with solver integration deferred [S068 p. 11]. The gain was measured where her own code exploited the structure [S024 pp. 24-29; S072 pp. 19-21], and the detection cost was measured inside a solver: "Time spent computing special structure is negligible compared to FBBT, so GALINI recomputes special structure at every node without any code optimization." [S087 p. 4].
  2. Step 5 (validate against a labelled oracle) is practised for SUSPECT [S068 p. 10] and, in a new form, for graph encodings: a completeness proof plus exact counts against OEIS [S128 pp. 11-16] or a solution-pool count [S051 p. 9]. It is not practised for the binary-layered-graph detector, shown on one example [S120 pp. 16-17; S091 p. 7].
  3. Step 3 gets a check SKILL.md lacks: "symmetry in the original problem does not imply the same symmetry in the relaxed problem and vice versa." [S120 p. 6]; generate RLT or McCormick auxiliaries for every member of an orbit so the relaxation keeps the symmetry [S120 pp. 8-9].
- **Limitations**: her own 2014 text names the convexity gap (no composition rules; a missed composite-term detection) [S001 pp. 8, 14]. The pattern-matcher quote in SKILL.md step 7 (AIChE J. 2016) is still unread in full; only the abstract is carded [S064; D001].
- **Proposed Practice additions**: [S025 pp. 3, 13] (2010, earliest); [S032 pp. 10-12]; [S087 p. 4] (cost measured); [S128 pp. 11-16] (step 5 by proof and count). Data-driven variant in §3.1.

### Variants and contradictions (08 §3)

| Method | Variant | Cards |
|---|---|---|
| M1 | Structure kept exact rather than detected, in data-driven models: model only the unknown part and keep known analytical objectives, kinetics, additivity or conservation laws exact | [S095 pp. 3-4; S034 pp. 2, 5; S075 pp. 2, 4; S059 pp. 4, 9; S086 pp. 6, 9; S115 pp. 1-3, 6; S015 pp. 1-2; S014 pp. 6, 9] |
| M1 | Structure used to map tractability (complexity classes, a P/NP boundary) rather than detected in a solver | [S049 pp. 2-3, 22, 27-28; S069 pp. 5, 11; S135 p. 3] |
| M1 | Structure exploited through a logic solver's cores | [S058 pp. 6-8] |
| M1 | Non-detection by design in a neutral library (joint voice) | [S010 pp. 8, 15] |
| M1 | Detection without exploitation or labelled validation (step 6 absent in all four; step 5 also absent except in S068, which validated against MINLPLib labels [S068 p. 10]; corrected in the fix pass) | [S076 p. 5; S120 pp. 16-19; S091 p. 7; S068 p. 11] |

No contradiction link targets Method 1. The 2017-2020 detection papers are recorded as contradicting Method 4's stop rule (see [Method 4](#method-4)).

### Added in T3.6

- **Condensed into SKILL.md**: Stated, the epigraph plus [S145 p. 3]; Practice [S025 p. 13; S004 pp. 4–11; S024 pp. 10–17; S068 pp. 10, 29–31; S051 pp. 4–6]; say–do from 08 §2 (52 distinct cards: 35 evidence, 33 of them read in full or in part; 19 variant; 0 contradiction); four variant bullets (the detection line stops at detection [S120 p. 19; S068 p. 11; S024 pp. 24–29]; the symmetry check [S120 pp. 6–9]; detection cost measured in GALINI [S087 p. 4]; the data-driven variant [S095 pp. 3–4; S015 pp. 1–2]).
- **Step 2**: plot, then prove, then exploit with tangent cuts [S024 pp. 9–17] (catalog P5); the student's account in the supervised MEng report [S100 p. 42].
- **Step 4**: the structure carried by the modelling object: "The advantage of this approach is that, although GALINI itself is unaware of the pooling problem, GALINI can, through this library, behave as if it has perfect knowledge of its structure." [S072 p. 2].
- **Step 5**: the SUSPECT quote now has its card page [S068 p. 10]; misses listed [S068 pp. 29–31]; for encodings, completeness proved and solutions counted exactly [S128 pp. 11–16; S051 p. 9] (P4, E7).
- **Step 7**: unchanged; the pattern-matcher quote (AIChE J. 2016) is still not re-read in full: only abstract-level cards exist [S064; D001]. The GALINI measurement is in the variant bullet.
- **Limitations**: the convexity gap is self-reported in 2014, no composition rules and a missed composite-term detection [S001 pp. 8, 14].
- **Not added** (08 §10): exact encodings with correctness proofs as a separate method (standard MIP practice; kept as step 5 evidence).
- **Fix pass**: the first variant bullet read *The 2017-2020 detection papers stop before steps 5-6 [S120 p. 19; S068 p. 11]*. That is false for SUSPECT, which did step 5: MINLPLib labels as the oracle, 1275 of 1392 matched, no false positives, every miss listed [S068 pp. 10, 29–31]; only step 6 is deferred [S068 p. 11]. The bullet now says step 6 is missing in all four detection papers [S076 p. 5; S120 p. 19; S091 pp. 7–10; S068 p. 11] and step 5 only in the symmetry papers [S076 p. 5; S120 pp. 16–17; S091 p. 7] (as 08 §2 M1 items 1-2 have it). The symmetry check moved into step 3, tagged D7 [S120 pp. 6–9]; the GALINI cost datum moved into step 7 as a counter-case [S087 p. 4]; step 2 points to the LMTD anatomy, which now lives only here.

### Before T3.6 (moved verbatim)

**One line**: Read how practitioners write their models, find the structure they left implicit (redundant equalities, a named structure such as pooling, an already-convex function, a symmetry), turn it into a detector, validate the detector like an instrument, then let the relaxation exploit it.

**Evidence**:
- Stated: C1, 7 sources 2014-2023 [02 L1.4, L3.1]; the epigraph; on redundant equations: "This was already known. But what we did was that we actually um found ways of getting these equations." (T8 [12:44], ASR).
- Practice: GloMIQO (doi:10.1007/s10898-012-9874-7) and ANTIGONE (doi:10.1007/s10898-014-0166-2); pooling recognition (doi:10.1002/aic.15308); LMTD convexity (doi:10.1016/j.compchemeng.2016.07.001); symmetry (doi:10.3390/pr7110838); SUSPECT (doi:10.1007/s11590-019-01396-y); GNN symmetry breaking (arXiv:2305.09420) [03 PE-15, PE-29, PE-49].
- Say–do consistency: ✅ stated + practised in all four career eras.

**Steps**:
1. Read the models people actually write ("you have a lot of variables that are sort of like x is equal to y", T8 [11:42], ASR).
2. Plot the ugly function before relaxing it: the LMTD expression "actually looks like its own relaxation already" (T8 [14:16], ASR).
3. State the structure so a program can match it: term classes in an inheritance hierarchy, a named structure found by functional programming, a binary layered graph, symmetry-breaking constraints over GNN inputs.
4. Where rules are brittle ("hard-coded rules are easily tricked", T4 [12:39], ASR), build "a hybrid between automatic detection and disciplined programming" (T4 [13:43], ASR).
5. Validate against a labelled library used as an oracle: SUSPECT on all 1527 MINLPLib 2 problems, 1275 of 1392 processed matched, every miss listed; "SUSPECT does not have false positives on the test set, this gives confidence in the implementation and makes it possible to use it for solver selection." [03 PE-15]
6. Exploit it (redundant equations, edge-concave facets, a convex relaxation), and measure the gain inside the full branch-and-bound (→ Method 4).
7. Measure the detection cost on problems without the structure: the pooling pattern-matcher stayed out of ANTIGONE "because, at this point, the pattern-matching time significantly slows down ANTIGONE performance on non-pooling problems" (doi:10.1002/aic.15308, p. 3093, as quoted in santanu-s-dey note 05 §4.1; not re-read here).

**🔴 Stop rules**: a detector with false positives stays out of the default path; detection that slows the general case becomes a plug-in or option; a failed structure theorem is withdrawn publicly and replaced by a counterexample (arXiv:1712.05222 v3: "Theorem 1,2 are incorrect"; filed by the student, her role not recorded) [03 PE-34].

**Applies to stage**: problem choice; idea and formulation design.

**Different from standard practice**: textbook spatial B&B relaxes the model term by term. Here a recognition layer comes first, and detection quality is itself an experimental object with misses listed.

**Limitations**: only as good as its structure library and bound inference: factorable relaxations still "abstract away much of the nonlinear structure" (doi:10.1137/22m1515537); missed convexity (doi:10.1007/s11081-018-9411-8); guessed bounds gave a "grossly suboptimal" result (doi:10.1007/s11590-015-0880-9) [05 PC-01-PC-05].

### Before T3.7 (moved verbatim)

Condensed in SKILL.md on 2026-11-19 (stage T3.7, tighten). T3.7 cut back fix-pass wording here under the tighten rule (one-line variant bullets): the first variant bullet kept two of the four detection papers' cards [S120 p. 19; S068 p. 11] and lost the symmetry papers' step 5 cards and the measured-gain clause, which SKILL.md keeps in the inner tension *Detect vs exploit* [S024 pp. 24–29]; the **Fix pass** line above describes the text below. The T3.7 fix round put the stop-rule parenthetical back word for word. The SKILL.md text as it stood before this pass, word for word:

*Evidence, Stated:*

- Stated: the epigraph (C1, 7 sources 2014-2023 [02 L1.4, L3.1]); in print: "researchers may be able to find and exploit special mathematical structure for particular problem classes" [S145 p. 3].

*Variants/corrections, first bullet:*

  - ⚠ The 2017-2020 detection papers stop before step 6: no gain measured inside a B&B [S076 p. 5; S120 p. 19; S091 pp. 7–10; S068 p. 11]. Step 5 is done for SUSPECT [S068 p. 10], not in the symmetry papers [S076 p. 5; S120 pp. 16–17; S091 p. 7]. Gains were measured where her code exploited the structure [S024 pp. 24–29].

*Step 5:*

5. Validate against a labelled library used as an oracle: SUSPECT on all 1527 MINLPLib 2 problems, 1275 of 1392 processed matched, every miss listed; "SUSPECT does not have false positives on the test set, this gives confidence in the implementation and makes it possible to use it for solver selection." [03 PE-15; S068 p. 10]. For an encoding: a completeness proof plus exact solution counts [S128 pp. 11–16] (P4, E7).

*Stop rules:*

**🔴 Stop rules**: a detector with false positives stays out of the default path; detection that slows the general case becomes a plug-in or option; a failed structure theorem is withdrawn publicly and replaced by a counterexample (arXiv:1712.05222 v3: "Theorem 1,2 are incorrect"; filed by the student, her role not recorded) [03 PE-34].

<a id="method-2"></a>

## Method 2: Between formulations: the parameterised family between two textbook extremes

### Full-text evidence (08 §2, copied)

- **Strongest cards**:
  - The core text: two extremes plus the folklore, knob P, endpoints proved by Fourier-Motzkin projection and a bijective linear map, a conditional hierarchy, a sweep across P and classes against both extremes [S040 pp. 1-13]; "Note that the P-split formulations are in general robust towards the choice of P." [S040 p. 12].
  - The journal version, now read: bottom endpoint (Thm 1), hierarchy by aggregation (Thm 2), top endpoint for affine disjuncts (Thm 5) and a ceiling (Thm 6: no P-split forms the hull of a fully disjoint, strictly convex disjunction) [S046 pp. 6-13]; 344 instances [S046 pp. 2-3, 20-21]; shipped as a Pyomo.GDP plugin and an OMLT partitioning strategy [S046 pp. 3, 16]; "Without this structure, the P-split formulations do not necessarily have an advantage over either the big-M or convex hull formulation." [S046 p. 26].
  - The ReLU case: "The formulations are hierarchical: their relaxations start at a big-M equivalent and converge to the convex hull." [S013 p. 1]; N swept from 1 to 10 with random and deliberately uneven partitions as controls [S013 pp. 7-9]; "While these formulations have tighter relaxations, they can perform worse than big-M due to having more difficult branch-and-bound subproblems." [S013 p. 5].
  - Other families: an n-dimensional SDP family from an SOCP-type relaxation to the full SDP, with the choice of n labelled heuristic guidelines [S021 pp. 6-8, 29-30]; partial Lasserre between levels 1 and 2 with a random control [S078 pp. 6-7, 12-14] and the choice left open, "Although the partial relaxation showed potential, there is still the question of how to select the parameters r and p in the partial relaxation." [S078 p. 20].
  - Parameter hygiene: one setting for all 399 GloMIQO runs [S004 p. 13]; "We show the method is robust to the choice of its single hyper-parameter and provide a parameter-free alternative." [S039 p. 1]; "We also aim to eliminate the need for the minimum number of experiments parameter by integrating over the Gaussian process hyperparameters." [S099 p. 4]; a prior parameter removed [S081 p. 5]; the parameter-free selector preferred [S031 p. 19].
  - The origin she names: "Why did these piecewise approximations work so well? How could we eliminate the computational dependence on parameters?" [S143 p. 13].
- **Say–do update**: keep ✅ with "partly kept", now dated from the full texts:
  1. The practice is older than P-split: the partition-level family (N_P = 1, McCormick, up to 16) was swept on 25 pooling problems with both encodings in 2011 [S009 pp. 28-30].
  2. Before that, the level was chosen per topology from experience: "The industrially-sized 15-Plant test case was solved to a 0.1% optimality gap after some experience with the particular topology by predicting a good partitioning level for the problem." [S152 p. 99]; [S025 p. 24].
  3. The parameter rule: robustness is claimed [S040 p. 12], but the journal version reports that the best P varies by class, that two to four variables per split perform well on clustering and P_ball (ReLU nets: P = 2 or 4 splits fastest, P = 50 slowest [S046 pp. 23, 25]), and that P has no selection rule [S046 pp. 22-23, 26]; for ReLU nets the best N is problem-dependent [S013 p. 8]. SKILL.md's "no rule for choosing the parameter published" stands; a practical range is now published.
  4. Step 5's controls (random and deliberately weak partitions) are in the NeurIPS paper [S013 p. 7], not in the CPAIOR or journal P-split papers, which use ordered-index partitions only [S040 p. 11; S046 p. 22].
  5. Step 7 (delete the parameter) is practised four ways: a parameter-free variant [S039 p. 1], a prior parameter removed [S081 p. 5], an outer BO that sets the robustness level for the user [S033 pp. 15-16, 27-29], a planned removal [S099 p. 4].
- **Proposed Practice additions**: [S009 pp. 28-30] (2011); [S046 pp. 6-13, 22-23]; [S013 pp. 5, 7-9]; [S039 p. 1].

### Variants and contradictions (08 §3)

| Method | Variant | Cards |
|---|---|---|
| M2 | Parameter set per topology from experience (2010) or numerically per instance (2021) | [S152 p. 99; S025 p. 24; S020 pp. 11, 20, 24] |
| M2 | A probabilistic knob between the nominal and the fully robust solution, exposed to the user and set by bisection or an outer BO | [S055 pp. 11-12, 21-22; S033 pp. 9-10, 15-16, 27-29] |
| M2 | Nested levels used for warm starts, not a family between extremes | [S088 pp. 8, 10-12] |
| M2 | A knob between two greedy orders fixed by analysis | [S135 pp. 3, 13, 18] |
| M2 | New parameters without a robustness sweep | [S023 pp. 2, 8, 22; S039 p. 7; S083 pp. 3, 5, 11] |

Contradiction (08 §3.2, item 1):

1. **M2 ✗** [S056 p. 16]: two extremes (prediction accuracy, robustness) are each optimised and the family between them is left as future work. Method 2 is a formulation habit; in a co-authored chemometrics paper with a black-box optimiser it is not applied. Scope note.

Corrections of SKILL.md claims (08 §3.3):

| SKILL.md claim | What the full texts show | Proposed change |
|---|---|---|
| Method 2 Limitations: choosing N has no theory; U8 | Robustness claimed [S040 p. 12]; best P varies by class, two to four variables per split perform well on clustering and P_ball (ReLU nets: P = 2 or 4 splits [S046 pp. 23, 25]), no rule [S046 pp. 22-23, 26]; N problem-dependent [S013 p. 8]; choice left open [S078 p. 20] | Keep the no-rule limitation; add the published practical range |
| Method 2 step 5: random partitions and a deliberately weaker variant as controls | In the NeurIPS paper [S013 p. 7], not in the CPAIOR and journal P-split papers [S040 p. 11; S046 p. 22] | Mark the controls as practised in one of the three texts |
| Method 2 Evidence: "N = 2/4/8 ablations" (MP 2012) | Swept on packing only; N = 4 for pooling inherited [S011 p. 17] | Scope the citation |

### Added in T3.6

- **Condensed into SKILL.md**: Stated, the T11 quote (the essay's origin question moved here: "Why did these piecewise approximations work so well? How could we eliminate the computational dependence on parameters?" [S143 p. 13]); Practice [S009 pp. 28–30; S040 pp. 1–13; S046 pp. 6–13, 20–23; S013 pp. 5, 7–9; S078 pp. 6–7, 12–14]; say–do from 08 §2 (33 distinct cards: 14 evidence, 21 variant, 1 contradiction); three ⚠ bullets and one ✗ bullet as in 08 §3.
- **Steps**: step 2 adds the SDP family [S021 pp. 6–8] (D1); step 3 names the proof devices, projection for the bottom and aggregation for the order [S046 pp. 6–8] (P1, P2), and asks for a ceiling (Heuristic 4) [S046 pp. 12–13]; step 5 cites the one text with controls [S013 p. 7]; step 7 [S039 p. 1] (other ways to delete a parameter: a prior parameter removed [S081 p. 5], an outer BO that sets the robustness level [S033 pp. 15–16, 27–29], a planned removal [S099 p. 4]); step 8 the Pyomo.GDP plugin and OMLT partitioning strategy [S046 pp. 3, 16].
- **Limitations**: the scope sentence "Without this structure, the P-split formulations do not necessarily have an advantage over either the big-M or convex hull formulation." [S046 p. 26]; best N problem-dependent [S013 p. 8]; tighter members "can perform worse than big-M due to having more difficult branch-and-bound subproblems" [S013 p. 5]. The 2026-10-10 sentence "Full texts of P-split and NeurIPS 2021 not read." no longer holds (see [Corrections](#corrections)).
- **Fix pass**:
  - Stated: the pointer C9 [02 L3.2] (Goldilocks, W9) is back in SKILL.md; the full project-page quote stays below.
  - The T3.6 variant bullet *Best P varies by class; a practical range of 2-4 variables per split, no rule [S046 pp. 22–23, 26]* applied the clustering result to every class. The range is now in Limitations and U8, scoped by class: 2-4 variables per split on clustering, semi-supervised clustering and P_ball [S046 p. 23]; for ReLU nets the smaller splits P = 2 or 4 are fastest and P = 50 slowest [S046 pp. 23, 25]; ReLU partitions decline near N ≥ 7 [S013 p. 8].
  - Moved here from SKILL.md: *Earlier, the level was set per topology from experience [S152 p. 99]; the 2012 N = 2/4/8 sweep was on packing only [S011 p. 17]* (the second half stays in Corrections) and the ✗ bullet *Not applied in a co-authored chemometrics paper [S056 p. 16]*, which the say–do line now names as a scope note.
  - Steps gain the ReLU specifics the cards give: step 2, partitions balanced by weight, equal size via sorted weights or equal range with 5%/95% quantiles (N ≥ 3), random and uneven controls [S013 pp. 6–7]; ordered indices when variables play symmetric roles [S046 p. 22]; step 3, the hierarchy needs additive bounds (a box or interval arithmetic) and fails in Fig. 1 under the tightest valid bounds [S046 pp. 6–8]; step 5, interval vs per-partition OBBT, 2N + 2 LPs per neuron capped at 5 s with an interval fallback [S013 p. 9], and with OBBT poorly chosen partitions lose to big-M [S013 p. 8]; step 6, settings fixed across formulations (catalog E9: Gurobi MIPFocus = 3, Cuts = 1, MIQCPMethod = 1 for all, PreMIQCPForm = 2 for the hull only [S046 pp. 21–22]; MIPFocus = 3 for consistent solution approaches [S013 p. 16]), and when the hull is intractable (over five minutes to pass the root on ReLU nets [S046 p. 22]) a comparison with big-M plus hull cuts swept over cut frequency [S013 p. 8].

### Before T3.6 (moved verbatim)

**One line**: When two classical formulations each win somewhere (big-M light and weak, convex hull tight and heavy; low and high Lasserre levels), make the interpolating family the contribution: prove its endpoints and order, admit the parameter up front, then show one setting holds across a class, or remove it.

**Evidence**:
- Stated: C9, C4 [02 L3.2, L1.7, L5.1]; a talk title used at five venues (Inner Tensions); "Prior literature often observes that the big-M formulation is too light and the convex hull formulation is too heavy. Our Goldilocks-style solution makes the optimization formulation just right for the application." (W9, project page); "alert alert I'm going to introduce a parameter and then try to um uh show you that the parameter wasn't very important and also that we can get rid of the parameter" (T11 [28:23], ASR).
- Practice: P-split (doi:10.1007/978-3-030-78230-6_19; doi:10.1007/s10107-025-02232-1); partition-based ReLU (arXiv:2102.04373); partial Lasserre (doi:10.1007/s11081-022-09763-y); N = 2/4/8 ablations (doi:10.1007/s10107-012-0555-6) [03 PE-18, PE-20].
- Say–do consistency: ✅ stated + practised, **partly kept**: robustness shown on the families tested; no rule for choosing the parameter published [05 PC-16].

**Steps**:
1. Name the two extremes and where each wins, folklore included (the "folklore observation that extended convex hull formulations tend to perform worse than expected").
2. Find the interpolating knob: P partitions of an additively separable constraint, partitions of a ReLU node's inputs, partial Lasserre levels, piecewise segments.
3. Prove endpoints and order ("the relaxations form a hierarchy starting from a big-M equivalent and converging to the convex hull", CPAIOR abstract); keep proof assumptions apart from practical ones (T2 [37:18], ASR).
4. Put the parameter's cost first ("good God Ruth you use a lot of parameters", T7 [02:16], ASR).
5. Sweep a small grid across classes with controls: random partitions and a variant "that we posit would be even weaker" (T2 [28:38], ASR); never re-tune per comparison.
6. Report nodes and time against both extremes on the same instances (P-split journal: "a similar number of explored nodes as the convex hull formulation, while reducing the solution time by an order of magnitude").
7. Try to delete the parameter (SnAKe offers "a parameter-free alternative", arXiv:2202.00060).
8. Ship the family as a switch, not a verdict (`ReluPartitionFormulation` in OMLT).

**🔴 Stop rules**: if you cannot say which value is best, label the rule heuristic ("so it's going to be it's going to be heuristic", T7 [23:56], ASR); drop a variant that "kind of works um but uh not really" (T7 [33:21], ASR); report a failed idea as failed [02 D2, D5].

**Applies to stage**: formulation design, experiment design, judging results.

**Different from standard practice**: the usual choice is one formulation, or tuning big-M constants. Here the family is the result and its parameter a lever for the user.

**Limitations**: needs two known extremes and the P-split assumptions (additive separability); choosing N has no theory ("I do wish the authors left us with a clearer story on how N should be selected", NeurIPS 2021 reviewer) [03 §5.5]. Full texts of P-split and NeurIPS 2021 not read.

### Before T3.7 (moved verbatim)

Condensed in SKILL.md on 2026-11-19 (stage T3.7, tighten). T3.7 also dropped the Stated pointer that the fix pass had put back (see **Fix pass** above) and the step 6 outcome. The T3.7 fix round restored the pointer as *written: W9, Goldilocks (C9 [02 L3.2])*, named the contradiction in the say–do line again, put the step 6 outcome back with its qualifier outside the quotation marks, *(P-split journal, for many of the test problems: [the quoted words] [S046 p. 1])*, and replaced the T3.7 Limitations wording *(a NeurIPS 2021 reviewer asked for one [03 §5.5])*, which read the reviewer's wish for a clearer story on choosing N as a request for a theory, with *(a NeurIPS 2021 reviewer asked how N should be selected [03 §5.5])*. The SKILL.md text as it stood before this pass, word for word:

*Evidence, Stated:*

- Stated: C9 [02 L3.2] (Goldilocks, W9); "alert alert I'm going to introduce a parameter and then try to um uh show you that the parameter wasn't very important and also that we can get rid of the parameter" (T11 [28:23], ASR).

*Evidence, Say–do:*

- Say–do: ✅ stated + practised, **partly kept**: robustness shown on the families tested; no rule for choosing the parameter published [05 PC-16]; cards: 33 (all read in full or in part); links: 14 evidence, 21 variant, 1 contradiction (a scope note: not applied in a co-authored chemometrics paper [S056 p. 16]).

*Step 3:*

3. Prove endpoints and order ("the relaxations form a hierarchy starting from a big-M equivalent and converging to the convex hull", CPAIOR abstract): projection for the bottom, aggregation for the order [S046 pp. 6–8] (P1, P2), and a ceiling (→ Heuristic 4). The order needs additive bounds (a box, interval arithmetic); with the tightest valid bounds it can fail [S046 pp. 6–8]. Keep proof assumptions apart from practical ones (T2 [37:18], ASR).

*Step 4:*

4. Put the parameter's cost first ("good God Ruth you use a lot of parameters", T7 [02:16], ASR).

*Step 6:*

6. Report nodes and time against both extremes on the same instances, with settings fixed across formulations (E9) (P-split journal: "a similar number of explored nodes as the convex hull formulation, while reducing the solution time by an order of magnitude"). If the hull is intractable (ReLU nets: over five minutes to pass the root [S046 p. 22]), compare against big-M plus hull cuts swept over cut frequency [S013 p. 8].

*Stop rules:*

**🔴 Stop rules**: if you cannot say which value is best, label the rule heuristic ("so it's going to be it's going to be heuristic", T7 [23:56], ASR); drop a variant that "kind of works um but uh not really" (T7 [33:21], ASR); report a failed idea as failed [02 D2, D5].

*Limitations:*

**Limitations**: needs two known extremes and the P-split assumptions (additive separability; without them P-split formulations "do not necessarily have an advantage" [S046 p. 26]); choosing N has no theory ("I do wish the authors left us with a clearer story on how N should be selected", NeurIPS 2021 reviewer) [03 §5.5]; the best N or P is problem-dependent, with class-specific ranges only: 2-4 variables per split on clustering and P_ball, P = 2 or 4 splits on ReLU nets (P = 50 slowest), a decline near N ≥ 7 [S046 pp. 22–25; S013 p. 8].

<a id="method-3"></a>

## Method 3: The partner's trained model is the problem: constraints, then a toolkit

### Full-text evidence (08 §2, copied)

- **Strongest cards**:
  - The founding text: BASF's gradient-boosted trees written as constraints, their piecewise-constant structure driving branching and bounding, a PCA-based penalty keeping the optimiser near the data, a public UCI stand-in next to the confidential instance [S020 pp. 1, 5-18]; "The Gurobi heuristics generally outperform the B&B algorithm, but the B&B algorithm derives better lower bounds." [S020 p. 22].
  - ENTMOOT: "While Gurobi 9 is still the best choice for small and moderate instances, i.e. instances that commonly occur in design of experiments, we want to highlight that algorithmic elements exploiting the underlying structure of tree-based models can help when scaling the optimization efforts." [S023 p. 19].
  - The toolkit: "In OMLT, competing optimization formulations become alternatives: users can switch between the Section 3 formulations and find the best for a specific application." [S006 p. 4]; Imperial-Sandia-CMU authorship with equal senior credit [S006 p. 1].
  - The neural line: exact MILP encodings with the piecewise-linear structure exploited in B&B [S005 pp. 2-5; S013 pp. 2-3]; GNNs written as constraints in OMLT with two switchable formulations [S051 pp. 2, 7-10; S038 pp. 5-10]; verification reusing the encoding, with OMLT's GNN code used to debug the SCIP implementation [S050 pp. 2-3, 6].
  - Step 8 in practice: the BO acquisition solved globally as a MISOCP over a tree-kernel GP [S047 pp. 4-6], as a MIP over a fully Bayesian tree kernel [S081 pp. 6, 26-28] and over graph kernels [S093 pp. 3, 6-7; S067 pp. 2-3, 7-8].
  - The stated programme: ReLU nets as MILPs, trees optimised globally, the algebraic model handed to global solvers [S014 pp. 20-21]; "The second, mathematical programming-led, perspective is important for PSE domains where the optimization problems being solved are so difficult that a surrogate model must conform to specific properties." [S015 p. 1].
  - The first public form, 2018, with risk control still in its title [S119 p. 17].
- **Say–do update**: stated and practised from 2018 [S119 p. 17] to 2026 [S067 pp. 2-3]; keep ✅. Four refinements:
  1. The stance predates ML: in 2014-2015 the partner lab's mechanistic bioreactor model was the optimisation problem, written as an MINLP and solved with her own solver [S085 pp. 1-2; S045 pp. 2-3]; "The model is implemented in GAMS 24.1 and solved using the MINLP solver ANTIGONE 1.1 (Misener and Floudas, 2013; 2014)." [S042 p. 7]. A data-defined lookup table written as MILP constraints is a 2010 precursor [S012 pp. 1-2, 15-21].
  2. Step 4's device varies by model class: a PCA penalty for trees, whose failure on clustered data the authors concede [S020 pp. 17, 26]; a distance-to-data penalty in ENTMOOT [S023 p. 10]; data-set bounds on atom, bond and ring counts for GNNs [S051 pp. 8, 25; S038 p. 14]; a learned SVM failure boundary [S071 pp. 3-4]; a stated condition to constrain surrogates against extrapolation [S015 p. 1]. Step 4 should name the family, not the PCA penalty alone.
  3. From 2022 the model is often chosen for its encodability instead of being given by the partner (variant, §3.1): "Therefore, it is not that we chose shortest-path kernel first for specific reasons then developed necessary formulations, but that the fundamental advances in graph optimization led us to shortest-path kernels." [S067 p. 20]; [S047 p. 6; S071 p. 3].
  4. Step 7's design (one interface, rival options as switches) recurs outside trained models: design-of-experiments criteria [S041 pp. 19-21, 34], solver components [S087 pp. 3, 11], robust reformulations and uncertainty sets [S057 pp. 2, 6, 15; H001], acquisition functions [S031 pp. 2, 12, 19].
- **Proposed Practice additions**: [S020 pp. 5-18, 22]; [S047 pp. 4-6]; [S081 pp. 6, 26-28]; [S051 pp. 7-10]; step 6 stand-ins [S031 pp. 17-18; S097 pp. 3, 13].

### Variants and contradictions (08 §3)

| Method | Variant | Cards |
|---|---|---|
| M3 | The partner's mechanistic (not learned) model as the problem, 2014-2015 | [S085 pp. 1-2; S045 pp. 2-3; S042 pp. 7-8; H002 p. 1] |
| M3 | The model chosen for its encodability (reverse direction) | [S067 p. 20; S047 p. 6; S071 p. 3; S015 p. 1; S028 p. 16] |
| M3 | The trained score dropped: the MIP used as a constrained generator, "Instead of pursuing optimality, this paper exploits the ability of MIP in molecular generation and proposes Limeade as an end-to-end tool from real-world needs to feasible molecules." | [S090 pp. 1, 4, 11] |
| M3 | A learned surrogate fed to a local solver, or a meta-learned prior, instead of an exact encoding | [S080 pp. 8-10; S075 pp. 4-5; S113 p. 10; S086 pp. 6, 8] |
| M3 | The practitioner's trusted estimator kept and wrapped with uncertainty | [S066 pp. 3-6] |
| M3 | The switchable-options design applied outside trained models | [S041 pp. 19-21, 34; S087 pp. 3, 11; S057 pp. 2, 6, 15; S031 pp. 2, 12, 19; S086 pp. 6, 8] |

No contradiction link targets Method 3. Corrections of SKILL.md claims (08 §3.3):

| SKILL.md claim | What the full texts show | Proposed change |
|---|---|---|
| Method 3 step 4: a penalty on distance from a PCA subspace | The PCA penalty is the tree paper's, with its stated failure on clustered data [S020 pp. 17, 26]; other devices elsewhere [S023 p. 10; S051 pp. 8, 25; S071 pp. 3-4; S015 p. 1] | Name the family of near-data devices |

### Added in T3.6

- **Condensed into SKILL.md**: Stated, the OMLT sentence with its card page [S006 p. 4] (the spoken T6 quote stays below); Practice [S020 pp. 1, 5–18; S023 p. 19; S051 pp. 7–10; S047 pp. 4–6; S081 pp. 6, 26–28]; say–do from 08 §2 (44 distinct cards: 27 evidence, 20 variant, 0 contradiction); variants: the mechanistic precursor [S045 pp. 2–3; S042 p. 7], the near-data family [S020 pp. 17, 26; S023 p. 10; S051 p. 8], encodability first [S067 p. 20], the switchable design outside trained models [S087 pp. 3, 11; S057 pp. 2, 6, 15].
- **Steps**: step 4 names the family (catalog D5) and keeps the PCA wording; step 5 [S023 p. 19]; step 6 [S020 p. 18] (more stand-ins: GP posterior samples of anonymised BASF data [S031 pp. 17–18]; partner data released openly [S097 pp. 3, 13]); step 8 [S047 pp. 4–6].
- **Not added** (08 §10): grey-box modelling and choosing the model for its encodability as methods; they are a Method 1 and a Method 3 variant.
- **Fix pass**: the variant bullet *Step 4 is a family of near-data devices; the PCA penalty fails on clustered data [S020 pp. 17, 26; S023 p. 10; S051 p. 8] (D5)* repeated step 4; its cards now sit in step 4 itself.

### Before T3.6 (moved verbatim)

**One line**: Treat the partner's predictive model (tree ensemble, neural network) as structured constraints, not a black box; optimise over it globally by exploiting its piecewise structure; then generalise behind one interface where rival formulations become switchable options.

**Evidence**:
- Stated: "we can put these optimization formulations in competition and then the user can get whatever is the best without having to experiment with implementing every single one" (T6 [07:42], ASR); "In OMLT, competing optimization formulations become alternatives: users can switch between the Section 3 formulations and find the best for a specific application." (OMLT paper) [02 L3.3, L4.7; 01 SW4].
- Practice: gradient-boosted trees (doi:10.1287/ijoc.2020.0993) → ENTMOOT (doi:10.1016/j.compchemeng.2021.107343) → OMLT (arXiv:2202.02414) → tree-kernel BO (arXiv:2207.00879) → BARK (arXiv:2503.05574); CI, coverage, a public stand-in instance [03 PE-17, PE-25, PE-27].
- Say–do consistency: ✅ stated + practised, 2017-2026.

**Steps**:
1. Start from the model the partner trusts (BASF tree ensembles "for picking the best chemical process catalyst", arXiv:1803.00952 v1).
2. Write it as constraints and name its structure: trees piecewise constant, ReLU nets piecewise linear, GNNs with graph symmetries.
3. Solve exactly where possible: heuristics for feasible points plus a structure-exploiting branch-and-bound.
4. Keep the optimiser near the data (a penalty on distance from a PCA subspace of the training data) [05 PC-04].
5. Concede where the generic tool is better: "While Gurobi 9 is still the best choice for small and moderate instances ..." (ENTMOOT).
6. Release a public stand-in for the confidential instance; the partner's data stays with the partner [03 PE-25].
7. Generalise and harden: one interface for NN and GBT models with switchable formulations (complementarity, big-M, partition); tests, coverage, notebooks in CI, COIN-OR. Her hands-on role is gatekeeping: 21 OMLT commits, 20 of them PR merges [03 PE-41, PE-42].
8. Reuse it in BO: optimise the acquisition function globally as a MINLP.

**🔴 Stop rules**: if a specialised tool from another community does the task better, say so; if solutions leave the training region, the "optimum" is not credible; if the tool rests on one student, find an external co-maintainer or accept that it will freeze (GPdoemd, suspect, romodel stalled; OMLT with Sandia and CMU kept releasing) [04 F6; 03 PE-43].

**Applies to stage**: problem choice, formulation design, release.

**Different from standard practice**: ML samples a trained model as a black box; OR papers present formulations as rivals. Here the model is the problem and the rivalry a user setting.

**Limitations**: learned trust regions beat PCA "in 18 cases out of 21" on synthetic data (doi:10.1287/ijoc.2022.0312); tighter tree formulations exist (doi:10.1287/opre.2022.0150); exact encodings of large nets do not scale (arXiv:2401.03451; her words: "sometimes it's going to be a stupid idea", T7, ASR) [05 PC-04, PC-10, PC-14]. The toolkit side presupposes developer funding; a lone researcher should use OMLT and contribute one formulation.

### Before T3.7 (moved verbatim)

Condensed in SKILL.md on 2026-11-19 (stage T3.7, tighten). The T3.7 fix round gave step 7 its role sentence back, marked as inferred, as 03 PE-41 marks it: *Her role (inferred): maintainer and gatekeeper; 20 of her 21 OMLT commits are PR merges [03 PE-41, PE-42].* The SKILL.md text as it stood before this pass, word for word:

*Step 7:*

7. Generalise and harden: one interface for NN and GBT models with switchable formulations (complementarity, big-M, partition); tests, coverage, notebooks in CI, COIN-OR. Her hands-on role is gatekeeping: 21 OMLT commits, 20 of them PR merges [03 PE-41, PE-42].

*Stop rules:*

**🔴 Stop rules**: if a specialised tool from another community does the task better, say so; if solutions leave the training region, the "optimum" is not credible; if the tool rests on one student, find an external co-maintainer or accept that it will freeze (GPdoemd, suspect, romodel stalled; OMLT with Sandia and CMU kept releasing) [04 F6; 03 PE-43].

*Limitations:*

**Limitations**: learned trust regions beat PCA "in 18 cases out of 21" on synthetic data (doi:10.1287/ijoc.2022.0312); tighter tree formulations exist (doi:10.1287/opre.2022.0150); exact encodings of large nets do not scale (arXiv:2401.03451; her words: "sometimes it's going to be a stupid idea", T7, ASR) [05 PC-04, PC-10, PC-14]. The toolkit side presupposes developer funding; a lone researcher should use OMLT and contribute one formulation.

<a id="method-4"></a>

## Method 4: Judge a component inside the whole solver; the default follows the evidence, not authorship

### Full-text evidence (08 §2, copied)

- **Strongest cards**:
  - The defining source: "our goal is to design the best overall algorithm that can address any pooling problem" [S009 p. 23]; the verdict split by partition regime [S009 p. 29]; "Therefore, we will continue using the linear relaxation scheme to solve pooling problems." [S009 p. 30].
  - Cumulative ablation and class-split verdict: "This holistic view makes the comparisons fairly subtle but also allows us to draw better-informed conclusions." [S011 p. 17]; "When McC or McC + EC are sufficient to solve the process network problem, they tend to do so faster than the piecewise schemes, but the best strategies for closing the gap on the most difficult problems are the piecewise methods." [S011 p. 19].
  - The default against her own novelty: "Therefore, the default in GloMIQO is not to use the piecewise-linear relaxations." [S004 p. 13]; a tightening dropped because it "significantly increased the problem solution time without notable change in the objective function" [S025 p. 22].
  - Every cut class alone, every pair and all three inside GALINI's branch-and-cut on the whole library [S087 p. 16]; class-specific plug-ins off by default with a class-split verdict [S072 pp. 15-16, 19, 21].
  - The same logic outside solvers: exact acquisition optimisation judged in full BO runs against a sampling variant of the same algorithm [S047 p. 8]; "Note that a better kernel may not necessarily translate to better optimization results" [S093 p. 8]; surrogates graded by the simulated feasibility and cost of the final design, not by training error [S071 pp. 5, 7].
- **Say–do update**: keep ✅. Authorship earns no default in six more cases, 2022-2025: her group's partition formulation offered as one option, not the default [S006 p. 4]; "While this heuristic gives good results in a variety of benchmarks, it is not principled and hence potentially sub-optimal." [S081 p. 1]; "SnAKe is limited in some practical aspects." [S083 p. 2]; her group's symmetry-breaking constraints switched off by default [S090 pp. 11, 16]; one of her group's shortest-path kernels the worst performer in a benchmark she co-authored [S097 p. 20]; the simpler kernel winning in the loop [S093 p. 9]. Two scoping corrections:
  1. Step 2's cumulative ablation is in the 2012 relaxation paper and in GALINI [S011 pp. 17-19; S087 p. 16], not in the GloMIQO and ANTIGONE papers, which attribute wins through worked instances or solver-versus-solver profiles [S004 pp. 8, 24-25; S001 pp. 17-18].
  2. The stop rule "no full-algorithm result → no claim from the root alone" is not applied in three texts: detection only [S120 p. 19]; the SDP cut-scoring preprint, whose evidence stops at the root cut loop [S021 pp. 26, 31-32], although the 2018 conference abstract of the same work describes integration into ANTIGONE [S136]; the partial Lasserre bound judged stand-alone against the exact solver's time to match [S078 pp. 11-12].
- **Proposed Practice additions**: [S087 p. 16] (pairwise ablation); [S081 p. 1; S090 pp. 11, 16; S097 p. 20] (own work re-graded); [S005 pp. 5-8] (a component switched off where it does not pay, its callback frequency swept).

### Variants and contradictions (08 §3)

| Method | Variant | Cards |
|---|---|---|
| M4 | No internal ablation; wins attributed through worked instances or solver profiles | [S004 pp. 8, 24-25; S001 pp. 17-18] |
| M4 | Stability fixed as a default with no user switch | [S032 p. 15] |
| M4 | A portfolio instead of a default; a size-split verdict with no default | [S050 p. 9; S067 pp. 9, 23] |
| M4 | Evidence stopping at the root cut loop, a stand-alone bound or a stripped-down host | [S021 pp. 26, 31-32; S078 pp. 11-12; S063 pp. 12, 14] |
| M4 | The whole-system logic outside solvers: a treatment model, a prediction pipeline, a BO loop, a statistical model | [S070 pp. 17, 24-26; S098 p. 4; S082 pp. 10-13; S115 pp. 7, 22] |

Contradiction (08 §3.2, item 2):

2. **M4 ✗** [S120 p. 19]: value is claimed for detection without any branch-and-bound run. With [S068 p. 11; S091 pp. 7-10] this marks the 2017-2020 detection line as stopping short of M4's stop rule (§2 M1, M4).

Correction of a SKILL.md claim (08 §3.3):

| SKILL.md claim | What the full texts show | Proposed change |
|---|---|---|
| Method 4 step 2: cumulative ablation (cites MP 2012); Signature Work GloMIQO | The ablation is in MP 2012 [S011 pp. 17-19] and GALINI [S087 p. 16]; GloMIQO and ANTIGONE have none [S004 pp. 8, 24-25; S001 pp. 17-18] | Note it under step 2 |

### Added in T3.6

- **Condensed into SKILL.md**: Stated, the APOGEE sentence: the card holds its opening, "our goal is to design the best overall algorithm that can address any pooling problem" [S009 p. 23]; the full sentence is from note 01 (SW1). Practice [S011 pp. 17–19; S087 p. 16; S004 p. 13; S081 p. 1; S090 pp. 11, 16]; say–do from 08 §2 (44 distinct cards: 30 evidence, 14 variant, 1 contradiction); variants: no internal ablation in GloMIQO and ANTIGONE [S004 pp. 8, 24–25; S001 pp. 17–18]; ✗ root-only or stand-alone evidence [S120 p. 19; S021 pp. 26, 31–32; S078 pp. 11–12]; the same logic outside solvers, "Note that a better kernel may not necessarily translate to better optimization results" [S093 p. 8], and a portfolio instead of a default [S050 p. 9; S067 pp. 9, 23].
- **Steps**: step 2 card pages [S011 p. 17; S087 p. 16] (E4); step 4 [S004 p. 13]; step 5 [S009 pp. 29–30]; step 6 adds the frequency sweep of an expensive component [S005 pp. 5–8] (E15) and points to Heuristic 11; step 8 [S081 p. 1]. Kept here, not in SKILL.md: the class-split verdict on process networks, "When McC or McC + EC are sufficient to solve the process network problem, they tend to do so faster than the piecewise schemes, but the best strategies for closing the gap on the most difficult problems are the piecewise methods." [S011 p. 19]; a tightening dropped because it "significantly increased the problem solution time without notable change in the objective function" [S025 p. 22]; more own-work re-grading [S083 p. 2; S097 p. 20; S093 p. 9].
- **Not added** (08 §10): *concede the specialised tool's turf* and *portfolio instead of default* as heuristics (covered by Heuristic 7, Method 3 step 5 and Method 4 step 7).
- **Fix pass**: the T3.6 bullet *✗ Root-only or stand-alone evidence in three texts [S120 p. 19; S021 pp. 26, 31–32; S078 pp. 11–12]* marked all three as contradictions, but only [S120 p. 19] is a contradiction link; the other two are variants (08 §3.1, M4 row), so the bullet is split into ✗ and ⚠. Stated gets back the pointer T6 [09:26, 12:26] (ASR) [02 L1.8] (both quotes are below). Step 6 is tagged E15. The say–do line counts cards read in full or in part: 43 of 44.

### Before T3.6 (moved verbatim)

**One line**: Grade a new relaxation, cut or detector by what it adds to the complete algorithm across classes, not by its root bound on its home class; make the robust variant the default even when that switches off your own novelty, and ship class-specific gains as documented options.

**Evidence**:
- Stated: "our goal is to design the best overall algorithm that can address any pooling problem, so we are interested in the performance of the two relaxations when they are incorporated into the APOGEE algorithm rather than in an isolated root node relaxation." (APOGEE paper) [01 SW1]; "i am a big fan of this partition based formulation because i am a co-author on this paper but i don't know if for a very particular application if this partition-based formulation is going to be better" (T6 [09:26], ASR); "you don't have to take our word for it" (T6 [12:26], ASR) [02 L1.8].
- Practice: APOGEE (doi:10.1016/j.compchemeng.2011.01.026) and GloMIQO defaults against her own novelty [03 PE-33]; BARK re-grades her group's tree kernels [05 R3] (steps 4, 5, 8).
- Say–do consistency: ✅ stated + practised, repeatedly against her own work.

**Steps**:
1. Define the deliverable as the best overall algorithm for a class, not the best root bound.
2. Run a cumulative ablation inside the full B&B (MP 2012: McCormick → + edge-concave facets → + piecewise linear → + logarithmic partitioning; root gap, nodes, time, error bars; "This holistic view makes the comparisons fairly subtle but also allows us to draw better-informed conclusions."). With several component classes, run every pair and all together [03 PE-18, PE-19].
3. Split the verdict by class: edge-concave aggregations valuable "in any MIQCQP", whereas "the piecewise-linear underestimation scheme is best applied to specific classes" [01 SW2].
4. Choose the default for robustness: "Therefore, the default in GloMIQO is not to use the piecewise-linear relaxations ... Users are strongly encouraged to experiment with activating the piecewise-linear options for models that do not solve within a reasonable amount of time" [01 SW2].
5. Prefer stability over novelty: after "numerical difficulty" on three large instances, "we will continue using the linear relaxation scheme to solve pooling problems." [01 SW1]
6. Measure the cost on non-target problems (→ Method 1 step 7).
7. Say when special-purpose code beats your general one: "our pooling problem-specific solver APOGEE [65] regurally [sic] outperforms the more generic work presented here." [01 §1.9]
8. Re-grade your own earlier work: BARK calls the 2022 tree-kernel heuristic "not principled and hence potentially sub-optimal" [05 R3].

**🔴 Stop rules**: numerical trouble on large instances → the stable variant; gains in one class → opt-in; slowdown on non-target problems → out of the default path; no full-algorithm result → no claim from the root alone.

**Applies to stage**: experiment design, judging results.

**Different from standard practice**: papers usually test a relaxation at the root or on its home class, then turn it on. Here authorship earns no default.

**Limitations**: needs a full solver to ablate inside (not pure theory); switching off your own novelty is easier with a reputation; a one-class user needs a plug-in (GALINI pooling, doi:10.1016/j.compchemeng.2022.107660), not a default.

### Before T3.7 (moved verbatim)

Condensed in SKILL.md on 2026-11-19 (stage T3.7, tighten). T3.7 dropped the Stated pointer T6 [09:26, 12:26] that the fix pass had put back (see **Fix pass** above) and the provenance note *full sentence [01 SW1]* (the full sentence is on S009 p. 23 of the full text; the card verifies its opening), and condensed step 4's quote. The T3.7 fix round restored the pointer word for word and put the card's sentence back in step 4 [S004 p. 13], replacing the T3.7 paraphrase *GloMIQO ships its piecewise-linear relaxations off and tells users to try them on models that do not solve in reasonable time* with the quoted sentence followed by *users are told to try them on models that do not solve in reasonable time*. The SKILL.md text as it stood before this pass, word for word:

*Evidence, Stated:*

- Stated: "our goal is to design the best overall algorithm that can address any pooling problem, so we are interested in the performance of the two relaxations when they are incorporated into the APOGEE algorithm rather than in an isolated root node relaxation." (APOGEE paper [S009 p. 23]; full sentence [01 SW1]); on her own formulation as one option, T6 [09:26, 12:26] (ASR) [02 L1.8].

*Step 2:*

2. Run a cumulative ablation inside the full B&B (MP 2012: McCormick → + edge-concave facets → + piecewise linear → + logarithmic partitioning; root gap, nodes, time, error bars; "This holistic view makes the comparisons fairly subtle but also allows us to draw better-informed conclusions." [S011 p. 17]). With several component classes, run every pair and all together [03 PE-18, PE-19; S087 p. 16] (E4).

*Step 4:*

4. Choose the default for robustness: "Therefore, the default in GloMIQO is not to use the piecewise-linear relaxations ... Users are strongly encouraged to experiment with activating the piecewise-linear options for models that do not solve within a reasonable amount of time" [01 SW2; S004 p. 13].

<a id="method-5"></a>

## Method 5: Benchmark like an auditor

### Full-text evidence (08 §2, copied)

- **Strongest cards**:
  - GloMIQO: newest versions dated, vendor licences, one feasibility tolerance, back-to-back runs, a Perl check with benign and troublesome failures, gaps recovered from logs of crashed competitors, bounds added by others removed [S004 pp. 18-22]; correctness findings about competitors written in (infeasible returns on over half the cases for one code, a wrong optimum for another) [S004 pp. 25-26].
  - ANTIGONE and its test suite: 2571 instances with freeze dates and an exclusion rule, a rebuilt minlp.org set, a Perl check with a stated violation threshold, lower bounds based on guessed bounds discarded, gap-at-limit profiles [S001 pp. 8-11, 17]; "Recall that the standard libraries are dynamic entities; we are using the latest versions as of 11 March 2013." [S123 p. 1]; "ANTIGONE derives the core of its strength from quadratic instances." [S001 p. 17].
  - The re-check rule in her words: "Instances where solvers returned infeasible points but claimed they were ε-global optimum points, local optimum points, or integer feasible points were automatically relabeled as failures (fl)." [S032 p. 18].
  - Strengthened rivals: the commercial rival run with her components as time-counted and oracle variants [S072 pp. 17-18]; the hull given its own best solver flag [S040 p. 11; S046 pp. 21-22]; "Our numerical comparisons do not include locally valid bounds on the α-variables, as such bounds are typically not easily obtainable and could give the P-split formulations an unfair advantage." [S046 p. 17]; "For each Max-Cut instance, our comparisons are with respect to the fastest time of these four implementations that reached the solution" [S078 p. 11].
  - Ground truth in learned-model papers: "We cannot know the ground truth of a robust instance without complete enumeration or relying on a solver’s numerical tolerances" [S050 p. 9]; labels only where all solvers agree, and a solver bug found and reported [S050 pp. 9, 13].
  - Losses written in: GALINI not competitive with Gurobi on sparse instances [S072 p. 21]; "But the hybrid MILP/SMT method is weaker than either MILP or SMT on a minimum makespan model." [S155 p. 1].
- **Say–do update**: keep ✅, scoped by genre and date:
  1. The full protocol, including a script re-checking every returned point, is in the 2013-2014 solver papers [S004 p. 19; S001 pp. 10-11; S032 p. 18]. The GALINI papers keep strengthened rivals, harmonised tolerances and profiles but describe no feasibility re-check, and the pooling study runs one competitor on one machine [S087 pp. 16-17; S072 pp. 16-21].
  2. The 2010-2012 papers precede the protocol: no competitors and no independent verification [S012 pp. 24-28; S025 pp. 26-27; S011 p. 19]; the 2011 APOGEE study has a documented set with known optima and listed failures but no competitor [S009 pp. 9, 23, 28-30]. This confirms the SKILL.md dating.
  3. In surrogate and data-driven papers the re-check moves to the truth model: every returned design re-simulated [S071 pp. 4-5]; 10^6 samples from the true distribution and an a posteriori global check [S055 pp. 19-20]; "Complete enumeration serves here as a validation tool to ensure successful termination of the ENTMOOT solver." [S056 p. 7]; published optima re-evaluated before extending, Monte Carlo checks of constraint violation [S080 pp. 13-15]; competitor objectives re-evaluated by hand, "In fact, both CPLEX 12.7 or Gurobi 7.5.2, may produce incorrect outputs due to solver tolerances, hence a specialized fixing method may be necessary." [S020 p. 39].
  4. In BO and ML venues the group follows the venue's protocol (seeds, quantiles, wall-clock-matched baselines, published baseline code) and drops the solver-paper items [S081 pp. 7-9, 17; S093 pp. 7, 9, 17-19; S059 pp. 9, 17-18, 27]; detection, tool and demonstration papers carry no benchmark [S091 pp. 7-10; S090 pp. 13-19; S073 p. 2].
  5. Set-up time accounting: kept in 2023 (timings with and without the authors' construction code [S078 pp. 13-14]; timings including model building [S071 p. 13]); not stated in 2021 [S013 pp. 9, 16]; OBBT bound time not included in the 2026 journal NN table [S046 p. 25]. Repeated runs: none in 2021 [S013 p. 16]; 50 runs per cell over model and solver seeds in 2023 [S051 pp. 9-10].
  6. Proposed step 1b, audit the inherited model or instance before using it (practice only; no stated rule in note 02): the predecessor's emissions model diffed against the primary legal text, the law followed where sources disagree [S025 p. 3]; a published heat-exchanger model corrected against its GAMS file with a change log [S100 pp. 111, 116-118]; a library's reported optimum shown to rest on a perturbed LMTD [S024 p. 24]; "The proofs lead to the unexpected outcome that the famous Haverly [33] pooling instances, i.e. the first-recorded pooling instances, belong to a strongly-polynomial subclass!" [S049 p. 2]; the classic published instance re-solved before extending, "Since the problem formulation is identical, we assume this discrepancy is due to the improvement in optimisation solvers after 20 years." [S080 p. 13]; the prior best re-run on current hardware and software [S152 p. 98].
- **Proposed Practice additions**: [S032 p. 18]; [S072 pp. 17-18]; [S050 pp. 9, 13]; [S071 pp. 4-5]; step 1b as above.

### Variants and contradictions (08 §3)

| Method | Variant | Cards |
|---|---|---|
| M5 | Before the protocol (2010-2012): no competitors or independent verification | [S012 pp. 24-28; S025 pp. 26-27; S009 pp. 9, 23, 28-30; S011 pp. 16, 19] |
| M5 | One solver (her own, or one commercial code) or one competitor on one machine | [S048 pp. 15-20; S072 pp. 16-21; S040 p. 11; S046 p. 22] |
| M5 | The BO/ML-venue protocol (seeds, quantiles, matched budgets) | [S081 pp. 7-9, 17; S093 pp. 7, 9, 17-19; S035 pp. 15-16; S023 pp. 14, 17-18, 29; S059 pp. 9, 27] |
| M5 | Own tool tuned per benchmark; single runs | [S005 p. 6] |
| M5 | The baseline is the partner's historical practice | [S079 p. 28] |
| M5 | Instances excluded when a patched competitor returned infeasible points, instead of counted as its failures | [S050 p. 13] |
| M5 | A constructed best case bounds the possible gain, in place of oracle runs | [S077 pp. 9-10] |

Contradictions (08 §3.2, items 3-8):

3. **M5 ✗** [S091 pp. 7-10]: no benchmark set, no competitor and no detection-cost measurement in the 2019 symmetry paper.
4. **M5 ✗** [S095 pp. 5-6]: a single genetic-algorithm baseline at fixed settings in a six-page conference application, with the exclusion stated: "The computational time required to choose the next query point has not been taken into account since our focus is on applications where evaluating the black-box function is significantly more expensive than optimising for the next query point." [S095 p. 5].
5. **M5 ✗** [S090 pp. 13-19]: a tool paper evaluated by one case study, without baseline or timings.
6. **M5 ✗** [S113 pp. 14, 17-21]: the BO-venue protocol (five repetitions, unequal initial budgets, normalisation from one GP run), partly kept through a strengthened baseline, a second cost axis and a written loss [S113 pp. 14, 18-19, 21].
7. **M5 ✗** [S100 p. 101]: in the supervised MEng report an anomalous bound is attributed to numerical error with no reported re-run, the rule SKILL.md already marks as not always kept; the same report audits the published model and writes its losses in [S100 pp. 99, 116-118].
8. One more M5 contradiction link records a reading note about the internal consistency of a text, not a practice; under the house rule it is not carried forward.

None overturns a method. Together they scope M5 to solver-comparison papers, and M1 step 6 and M4's stop rule to papers whose structure her own code exploits. Proposed M5 Practice wording: *every 2013-2014 solver paper in full; strengthened rivals and profiles in later solver and formulation papers; the venue's protocol in BO and ML papers; none in detection, tool and demonstration papers*.

Corrections of SKILL.md claims (08 §3.3):

| SKILL.md claim | What the full texts show | Proposed change |
|---|---|---|
| Method 5 one line: "a script re-checking every answer any solver returns"; Practice: "every solver paper since 2012" | Perl re-check described in the 2013-2014 solver papers [S004 p. 19; S001 pp. 10-11; S032 p. 18], not in the GALINI papers [S087 pp. 16-17; S072 pp. 16-21] | Date the re-check; scope as in §3.2 |
| Method 5 Say–do lapse (NeurIPS 2021: OBBT time excluded, single runs) and Inner Tension "Count every second vs the accounting used" | Single runs and unstated OBBT accounting confirmed from the full text [S013 pp. 9, 16]; OBBT time again not included in 2026 [S046 p. 25]; kept in 2023 [S078 pp. 13-14; S071 p. 13; S051 pp. 9-10]. The "variability" remark comes from the review thread, which no card covers | Add the 2023 and 2026 data points |

### Added in T3.6

- **Condensed into SKILL.md**: Stated, the BiqCrunch quote (T3, ASR); Practice [S004 pp. 18–22; S001 pp. 8–11, 17; S072 pp. 17–18; S050 pp. 9, 13]; say–do from 08 §2 (81 distinct cards: 40 evidence, 41 variant, 6 contradiction links); variants: the re-check dated [S004 p. 19; S001 pp. 10–11; S087 pp. 16–17], the venue protocol [S081 pp. 7–9], set-up time by year [S078 pp. 13–14; S013 p. 16; S046 p. 25], the ✗ papers without benchmark [S091 pp. 7–10; S090 pp. 13–19], the new step 1b [S025 p. 3; S080 p. 13]. The 2026-10-10 Practice line ("every solver paper since 2012 ...") is below; it is scoped by 08 §3.2 and §3.3.
- **Step 1b (new; practice only, no stated rule)**: [S025 p. 3; S100 pp. 116–118; S080 p. 13] (E8); further cases: "The proofs lead to the unexpected outcome that the famous Haverly [33] pooling instances, i.e. the first-recorded pooling instances, belong to a strongly-polynomial subclass!" [S049 p. 2]; a library optimum resting on a perturbed LMTD [S024 p. 24]; the prior best re-run on current hardware [S152 p. 98]. Four-way check (08 §4):

| Cluster (merged by meaning) | Cards read in full/part | 1 Recurrence | 2 Say–do | 3 Executable, non-standard | 4 Exclusivity | Result |
|---|---|---|---|---|---|---|
| Audit the inherited model or instance | S025, S152, S024, S100, S049, S080 (6) | ✅ 2010-2021 | ✗ no stated rule | ✅ | ⚠ | M5 step 1b (§2) |

- **Other steps**: step 1 [S001 pp. 8–10]; step 2, settings fixed across formulations [S040 p. 11] (E9); step 3 [S072 pp. 17–18] (E2), and, kept here, withholding from one's own method what the rival cannot get [S046 p. 17]; step 6 [S001 pp. 10–11; S004 p. 19] and, without a solver's answer to check, re-simulation or sampling [S071 pp. 4–5; S055 pp. 19–20] (E1); step 7 class slices and a primal/dual split [S001 pp. 17–18; S072 p. 21] (E6), set-up time in its own column (E10); step 8 [S001 p. 17] (WM1).
- **Fix pass**:
  - Step 6 cited [03 PE-13; S004 p. 19] for two sentences that are ANTIGONE's: "a Perl script asserted the feasibility of the solution returned by each solver. Instances where solvers returned infeasible points were automatically relabeled as failures (fl)." is on S001 p. 10, "based on guessed variable bounds" on S001 p. 11; GloMIQO words the rule differently on S004 p. 19, where "benign" and "troublesome" are. The citation is now [03 PE-13; S001 pp. 10–11; S004 p. 19]. The card-verified form of the rule is the 2014 signomial paper's, "Instances where solvers returned infeasible points but claimed they were ε-global optimum points, local optimum points, or integer feasible points were automatically relabeled as failures (fl)." [S032 p. 18]; GloMIQO has the same sentence without "(fl)" [S004 p. 19].
  - Say–do: 5 contradictions, not 6; the sixth contradiction link is a reading note (08 §3.2 item 8) and is not counted. Cards read in full or in part: 76 of 81.
  - Step 1b now carries its status, *practice only; no stated rule* (08 §4: say–do ✗ for this cluster), the supervised MEng report is labelled as such [S100 pp. 116–118], and the library-optimum check [S024 p. 24] is in the step. The duplicate variant bullet *Practised, never stated: audit the inherited model or instance (step 1b) [S025 p. 3; S080 p. 13]* left SKILL.md.
  - Step 7 adds the remaining-gap rule when more than half of a class times out [S046 p. 24] (E14); step 8 is tagged WM1.
- **Ground truth in learned-model papers** (kept here): "We cannot know the ground truth of a robust instance without complete enumeration or relying on a solver’s numerical tolerances" [S050 p. 9]; "Complete enumeration serves here as a validation tool to ensure successful termination of the ENTMOOT solver." [S056 p. 7].

### Before T3.6 (moved verbatim)

**One line**: The largest documented test set, competitors at their newest versions with harmonised tolerances, a strengthened baseline and oracle runs, a script re-checking every answer any solver returns, time and remaining-gap profiles, and losses and class scope written into the paper.

**Evidence**:
- Stated: "we compare to big crunch [= BiqCrunch] basically as an oracle to make it so that things are a bit more fair for big crunch ... we run big crunch four times and we pick the best of the four big crunch uh answers just to try to be less abusive" (T3 [24:29], ASR); "i thought in our paper we should also have um timings where we are including our building" (T3 [29:04], ASR) [02 C5, C6, L4.2].
- Practice: every solver paper since 2012 (GloMIQO, ANTIGONE, GALINI, the 2021 pooling study, partial Lasserre) [03 PE-01-PE-13, PE-21-PE-24, PE-30-PE-32].
- Say–do consistency: ✅ stated + practised, with a documented lapse: NeurIPS 2021 excluded OBBT time, used single runs, put an anomaly down to "variability" [03 PE-36, C2]. Exclusivity is the weakest of the five (Sahinidis also values large public comparisons).

**Steps**:
1. Test set: the largest documented set with provenance, freeze date and exclusion rule (ANTIGONE: 2571 problems); rebuild an unusable community set (115 minlp.org problems); add partners' models.
2. Competitors at their newest versions (asked from vendors if needed), stated as moving targets; harmonised tolerances, otherwise defaults, runs back to back [03 PE-07, PE-08].
3. Strengthen the baseline: give it your components; add oracle runs ("an oracle providing a list of valid cuts"); tune the closest rival or keep its best of several runs [03 PE-09-PE-11].
4. Give competitors the benefit of the doubt on parsing failures, and write that down.
5. Calibrate difficulty so the baseline solves some instances (→ Heuristic 3).
6. Verify independently: "a Perl script asserted the feasibility of the solution returned by each solver. Instances where solvers returned infeasible points were automatically relabeled as failures (fl)."; separate "benign" from "troublesome" failures; discard lower bounds "based on guessed variable bounds" [03 PE-13].
7. Report time and gap-at-limit profiles, one worked instance per class, exact versions and hardware, averages over commonly solved instances only [03 PE-21-PE-24].
8. Write losses and scope in: "In this case, the GALINI performance is not competitive with Gurobi."; "ANTIGONE derives the core of its strength from quadratic instances." [03 PE-30, PE-31]

**🔴 Stop rules**: an infeasible answer is a failure, not a time; a bound on guessed variable bounds is not reported; a self-invented metric comes with the standard one; an anomaly is re-run before blaming "variability" (the method's rule, not always kept).

**Applies to stage**: experiment design and execution, judging results.

**Different from standard practice**: many papers trust competitors' default runs and status codes and report time on solved instances. Here every answer is checked, the competitor strengthened, and the gap at the limit is a headline.

**Limitations**: needs licences and compute. Comparisons age when one side freezes: ANTIGONE fell from 2nd of 5 to 5th of 7 in Mittelmann's MINLP benchmark (Apr 2017 → Feb 2024), was dropped in 2025, yet in May 2026 still solved the most continuous nonconvex QPLIB instances (35 of 102) [05 §4, PC-06]. Date every comparison; say which side is frozen.

### Before T3.7 (moved verbatim)

Condensed in SKILL.md on 2026-11-19 (stage T3.7, tighten). The SKILL.md text as it stood before this pass, word for word:

*Evidence, Say–do:*

- Say–do: ✅ stated + practised in solver-comparison papers; lapse in NeurIPS 2021 (OBBT time excluded, single runs, an anomaly put down to "variability") [03 PE-36, C2]; cards: 81 (76 read in full or in part); links: 40 evidence, 41 variant, 5 contradictions (a sixth contradiction link is a reading note and is not counted). Exclusivity is the weakest of the five.

---

<a id="heuristic-1"></a>

## Heuristic 1: Choose by broken assumption

- **H1 (choose by broken assumption)**: [S039 pp. 1-3; S086 pp. 1, 6; S082 pp. 2, 16; S083 p. 2; S113 pp. 1-2, 5; S115 p. 2; S097 pp. 2-3; S031 pp. 1-2; S014 pp. 1-3; S152 pp. 97-98]; "However, in an industrial chemistry setting, existing BO and active learning software would require substantial adaptation prior to deployment." [S044 p. 2]. The practitioner's operating constraints become first-class objects of the formulation: cost of moving and delayed observations [S039 pp. 3-4, 7, 9], measurement delay and costly initial-condition switches [S086 pp. 1, 6], transition constraints [S059 pp. 4-7], NChooseK and similar constraint types [S044 pp. 2-3], chemistry rules added after inspecting the optimiser's molecules [S038 pp. 17-18, 20-21]; "However, we emphasise that we cannot fully use both tools simultaneously without asynchronicity arising." [S031 p. 9].

**Added in T3.6**: SKILL.md cites [S039 pp. 3–4; S086 pp. 1, 6].

**Before T3.6 (moved verbatim)**:

1. **Choose by broken assumption.** If a standard method's assumptions collide with two or more of an application's complications, take it: "we always assume that we're able to sample the space wherever we wish um at any one time ... this is of course not going to be this the case in many chemistry applications" (T10 [45:19], ASR). Cases: doi:10.1016/j.compchemeng.2023.108194; arXiv:2402.08406.

**Before T3.7 (moved verbatim)**:

Condensed in SKILL.md on 2026-11-19 (stage T3.7, tighten). T3.7 left the T10 pointer without saying which assumption broke; the T3.7 fix round says it as a paraphrase, without quotation marks: *in BO, the usual assumption that one can sample anywhere at any time fails in many chemistry applications, T10 [45:19], ASR*. The SKILL.md text as it stood before this pass, word for word:

*Heuristic 1:*

1. **Choose by broken assumption.** If a standard method's assumptions collide with two or more of an application's complications, take it: "we always assume that we're able to sample the space wherever we wish um at any one time ... this is of course not going to be this the case in many chemistry applications" (T10 [45:19], ASR). Cases: doi:10.1016/j.compchemeng.2023.108194; arXiv:2402.08406; move costs and delays become formulation objects [S039 pp. 3–4; S086 pp. 1, 6]. (ledger `#heuristic-1`)

<a id="heuristic-2"></a>

## Heuristic 2: Industrial instance first, general class second, public stand-in released

- **H2 (industrial instance first, general class second, public stand-in)**: UCI concrete next to BASF [S020 p. 18; S023 p. 18]; GP posterior samples of anonymised BASF data [S031 pp. 17-18]; partner data withheld with public stand-ins [S066 pp. 6, 11]; partner data released openly [S097 pp. 3, 13]; a Schlumberger case with public data [S055 pp. 1, 3, 13-16]; Royal Mail data first, the general class second [S135 pp. 2, 20]. The arc in her thesis abstract, "Effectively, the arc of this dissertation is to begin with modeling and globally optimizing pooling problems and expand into an optimization framework that broadly addresses MIQCQP and MISO." [S092], and its 2025 form, "This paper aims to distill the fundamental contributions of our recent works [45, 46, 47, 48] and extend them from specific applications to general settings." [S128 p. 2]. Variant: BASF co-authors with a literature model and no stand-in [S113 pp. 1, 13, 21].

**Added in T3.6**: SKILL.md cites [S020 p. 18; S135 pp. 2, 20].

**Fix pass**: the Royal Mail case was listed as *industrial instance first, general class second, public stand-in released*, but no public stand-in is reported and part of the data is encrypted for confidentiality [S135 p. 20]; SKILL.md now says it supports the first two parts only.

**Before T3.6 (moved verbatim)**:

2. **Industrial instance first, general class second, public stand-in released**; the partner's data stays inside ("the bsf data is within bsf", T1 [03:46], ASR). Case: gradient-boosted trees v1 → v3 and the concrete instance [03 PE-25].

**Before T3.7 (moved verbatim)**:

Condensed in SKILL.md on 2026-11-19 (stage T3.7, tighten). The SKILL.md text as it stood before this pass, word for word:

*Heuristic 2:*

2. **Industrial instance first, general class second, public stand-in released**; the partner's data stays inside ("the bsf data is within bsf", T1 [03:46], ASR). Case: gradient-boosted trees v1 → v3 and the concrete instance [03 PE-25; S020 p. 18]; Royal Mail: data first, then the general class, without a public stand-in (data partly encrypted) [S135 pp. 2, 20]. (ledger `#heuristic-2`)

<a id="heuristic-3"></a>

## Heuristic 3: Calibrate so the baseline wins some instances; add weak controls

- **H3 (calibrate so the baseline wins some; weak controls)**: perturbation sizes set so some big-M problems solve [S013 p. 7]; an ℓ1 budget to keep problems solvable [S046 p. 19]; a solvent-blind floor, "many of these models fail to outperform the baseline model, which does not use any solvent information." [S097 p. 7]; pooled and no-transfer controls plus an uncorrelated synthetic case [S082 pp. 5, 9]; matched controls that differ in one component [S023 p. 22; S047 p. 8; S077 pp. 3, 9; S115 pp. 7, 22; S126 p. 18]. Variant (joint voice): a library calibrated toward hard instances, "Thanks to these extensive preliminary tests, we discarded all instances that are solved by at least 30% of the complete solvers within a time limit of 30 seconds." [S010 p. 15].

**Added in T3.6**: SKILL.md cites [S013 p. 7]; the ℓ1 budget [S046 p. 19] is here.

**Before T3.6 (moved verbatim)**:

3. **Calibrate so the baseline wins some instances; add weak controls**: "Perturbations ε1 were selected such that some big-M problems were solvable within 3600s" [03 PE-06]; T2 [33:02], ASR.

<a id="heuristic-4"></a>

## Heuristic 4: Prove the hierarchy, experiment for the rest, label it (extended)

- **H4 (prove the hierarchy, experiment for the rest, label it)**: exactness proved, performance shown experimentally [S093 pp. 4, 9, 14-16]; where the theorem's conditions fail, a numerical feasibility check instead, "For the instances considered in this work, the obtained solution always turns out to be feasible." [S055 p. 19]; the failed regret analysis recorded [S081 pp. 23-26]; "We cannot prove that the algorithm will always converge to the same point, but this section demonstrates our computational experience that results of the Appendix D algorithm give answers within 10% of one another." [S065 p. 16]; "While we include some mathematical analysis in Sections 3.6 and 3.7, it is not fully rigorous and it is only meant to illustrate the importance of the Point Deletion heuristic." [S039 p. 14]. Extension in §5.

Extension proposed in 08 §5 (copied):

- **Added step**: before shipping a relaxation or formulation family, prove one negative result about it: a class where it cannot tighten anything, routed to another tool [S011 p. 9]; a ceiling, a class whose hull no member of the family reaches [S046 pp. 12-13]; the smallest example where the hierarchy fails without its hypothesis [S040 pp. 8-9]; a point showing two relaxations are not ordered [S078 p. 12]; the hardness frontier of each restrictive assumption [S049 pp. 22, 27-28, 31]; tight worst-case ratios and integrality gaps [S061 pp. 12, 17-18; S135 p. 6]; symmetry not preserved by a partial relaxation [S120 pp. 6-9]; necessary conditions as tractable certificates when optimality is NP-hard to explain, "We have restricted attention to feasible and efficient (rather than optimal) solutions because answering and explaining why an arbitrary schedule is optimal in polynomial time is ruled out due to NP-hardness of makespan scheduling, unless P=NP." [S017 p. 3].
- **Absorbed H6**: the long-horizon form of the same act, keeping a "why does it work?" question open until a structural result answers it [S143 p. 13; S049 pp. 2, 32; S024 p. 16]. With H11 added and H6 folded into H4, the heuristic list stays at ten, inside the framework's range of 5-10. If H6 is kept separate instead, drop its "One documented instance" qualifier.

Four-way check of the boundary cluster (08 §4):

| Cluster (merged by meaning) | Cards read in full/part | 1 Recurrence | 2 Say–do | 3 Executable, non-standard | 4 Exclusivity | Result |
|---|---|---|---|---|---|---|
| Prove the boundary of your own construction (ceilings, classes where a cut cannot help, hardness frontiers, non-containment) | S011, S040, S046, S049, S061, S078, S120, S135, S017 (9) | ✅ 2012-2026 | ⚠ statements of scope inside papers [S046 p. 26; S049 p. 32], no stated method in note 02 | ✅ | ✗ negative results about relaxations are the core output of other MINLP Team lenses (Dey, Burer; team.json hints); in her texts they support a positive construction [S046 pp. 12-13; S011 p. 9] | H4 extension (§5) |

**Added in T3.6**: SKILL.md adds the boundary step with [S011 p. 9; S046 pp. 12–13; S040 pp. 8–9] (catalog P3). Heuristic 6 was **not** folded into this item: folding would renumber Heuristics 7–11, while the protected Activation Rules cite "Heuristic 7" by number. Heuristic 6 therefore stays as its own item (08 §5 allows this), and the list has eleven items, one above the framework's guideline of five to ten.

**Fix pass**: folding does not force renumbering. Heuristic 6's content (the Floudas question, [S049 pp. 2, 32], [S024 p. 16; S069 p. 11]) is now the long-horizon form inside this item, and slot 6 stays as a one-line pointer, so Heuristics 7-11, including the "Heuristic 7" that the protected Activation Rules cite, keep their numbers. The list has ten heuristics. The two later examples are called shorter-horizon structural answers: they explain a published model's behaviour [S024 p. 16] or map complexity [S069 p. 11] rather than answer a long-kept question.

**Before T3.6 (moved verbatim)**:

4. **Prove the hierarchy, experiment for the rest, label it**: "I can only say it experimentally" (T7 [38:41], ASR). Not exclusive to her.

**Before T3.7 (moved verbatim)**:

Condensed in SKILL.md on 2026-11-19 (stage T3.7, tighten). T3.7 cut the fix pass's long-horizon form (see **Fix pass** above) to a pointer under the tighten rule (heuristics: one or two lines, at most three cards): SKILL.md names the question and points to the APOGEE anatomy, whose header and closure row carry the DOI and [S049 pp. 2, 32]; the Floudas quote and the shorter-horizon answers [S024 p. 16; S069 p. 11] are in the text below ([S024 p. 16] also in SKILL.md's corrections list). The SKILL.md text as it stood before this pass, word for word:

*Heuristic 4:*

4. **Prove the hierarchy, experiment for the rest, label it**: "I can only say it experimentally" (T7 [38:41], ASR). Not exclusive to her. Also prove one negative result about your construction: a class it cannot tighten [S011 p. 9], a ceiling [S046 pp. 12–13], a counterexample without the hypothesis [S040 pp. 8–9] (P3). Its long-horizon form (formerly Heuristic 6): keep the "why does it work?" question until a structural result answers it, "I finally have a first answer to these questions Chris asked me eight years ago" (essay W1, p. 13), answered by a complexity characterisation (doi:10.1007/s10898-017-0577-y) [S049 pp. 2, 32]; shorter-horizon structural answers [S024 p. 16; S069 p. 11]. (ledger `#heuristic-4`, `#heuristic-6`)

<a id="heuristic-5"></a>

## Heuristic 5: Weakness first; concede precisely; restate novelty

- **H5 (weakness first; concede precisely; restate novelty)**: no card names it. Related writing evidence: her method's limits listed first [S083 p. 2]; the lost guarantee written next to the gain, "Since the DSA algorithm never uses all of the data, we cannot assert global algorithm convergence." [S029 p. 6]; an appendix arranged as answers to reviewer questions [S067 pp. 20-23]. The review thread behind H5 is not a card.

**Added in T3.6**: no card covers the review thread; SKILL.md keeps the item unchanged except the note that one thread is readable. Workflow E keeps the appendix-as-answers move [S067 pp. 20–23] in the technique catalog (W10).

**Before T3.6 (moved verbatim)**:

5. **Weakness first; concede precisely; restate novelty.** NeurIPS 2021: "Your observation is correct, formulation (13)–(17) cannot be tighter than the convex hull formulation presented by Anderson et al. unless ..."; then "The fundamental advancements novel to this work are (i) ... and (ii) ..."; the score rose from 6 to 7 [03 PE-36]. One readable thread only.

**Before T3.7 (moved verbatim)**:

Condensed in SKILL.md on 2026-11-19 (stage T3.7, tighten). The SKILL.md text as it stood before this pass, word for word:

*Heuristic 5:*

5. **Weakness first; concede precisely; restate novelty.** NeurIPS 2021: "Your observation is correct, formulation (13)–(17) cannot be tighter than the convex hull formulation presented by Anderson et al. unless ..."; then "The fundamental advancements novel to this work are (i) ... and (ii) ..."; the score rose from 6 to 7 [03 PE-36]. One readable thread only. (ledger `#heuristic-5`)

<a id="heuristic-6"></a>

## Heuristic 6: Keep the "why does it work?" question; answer it structurally

- **H6 (keep the "why does it work?" question; answer it structurally)**: no longer one instance. The Floudas question [S143 p. 13] answered by the pooling complexity paper [S049 pp. 2, 32]; "The convexity result in this manuscript justifies why the Escobar and Grossmann (2010) model works better with the LMTD term moved to the objective." [S024 p. 16]; complexity tables as structural answers [S069 p. 11]. Merge with H4 proposed in §5.

**Added in T3.6**: "One documented instance" dropped; three instances [S049 pp. 2, 32; S024 p. 16; S069 p. 11]; the essay's origin of the question [S143 p. 13]; called the long-horizon form of Heuristic 4 (08 §5) without merging the two (see [Heuristic 4](#heuristic-4)).

**Fix pass**: merged into Heuristic 4 (see there); SKILL.md keeps item 6 as a pointer. The T3.6 item read: *6. Keep the "why does it work?" question; answer it structurally: [the essay quote below] (essay W1, p. 13), answered by a complexity characterisation (doi:10.1007/s10898-017-0577-y) [S049 pp. 2, 32]; two more instances [S024 p. 16; S069 p. 11]; the long-horizon form of Heuristic 4.*

**Before T3.6 (moved verbatim)**:

6. **Keep the "why does it work?" question; answer it structurally**: "I finally have a first answer to these questions Chris asked me eight years ago" (essay W1, p. 13), answered by a complexity characterisation (doi:10.1007/s10898-017-0577-y). One documented instance.

<a id="heuristic-7"></a>

## Heuristic 7: Write the do-not-use conditions next to the method

- **H7 (do-not-use conditions next to the method)**: "Thus, it should be stressed that when a problem can be sufficiently described by a well-posed, explicit MINLP formulation, then CDFO methods are not recommended." [S003 p. 9]; "it is highly relevant to application domains where there is high reward for fractional improvements and sufficient time to explore the search space" [S145 p. 2]; "Problems of this size are, practically speaking, out of the range of current deterministic global optimization technology, so we are left to consider heuristics and gradient-based approaches." [S029 p. 2]; "The method suffers from standard BO challenges where the tree kernel may not be a good prior for the underlying black-box function, e.g., purely continuous feature spaces." [S047 p. 6]; "We therefore recommend BARK for BO settings where the objective is expensive to evaluate, taking at least several minutes, or having a large associated financial cost." [S081 p. 9]; [S046 pp. 10, 26; S077 pp. 1, 14; S086 p. 10; S090 p. 4; S113 p. 21; S126 p. 10; S028 pp. 14-16; S095 p. 5; S034 p. 11]. The habit runs from 2014 [S145 p. 2] to 2026 [S126 p. 10].

**Added in T3.6**: SKILL.md cites [S003 p. 9; S081 p. 9] as the printed form, 2016-2025.

**Before T3.6 (moved verbatim)**:

7. **Write the do-not-use conditions next to the method**: BO "should only be used when acquiring new data is expensive and we have limited other knowledge" (T10 [20:26], ASR); ANTIGONE's quadratic scope; GloMIQO's opt-in advice [02 C11; 03 PE-31].

**Before T3.7 (moved verbatim)**:

Condensed in SKILL.md on 2026-11-19 (stage T3.7, tighten). The SKILL.md text as it stood before this pass, word for word:

*Heuristic 7:*

7. **Write the do-not-use conditions next to the method**: BO "should only be used when acquiring new data is expensive and we have limited other knowledge" (T10 [20:26], ASR); ANTIGONE's quadratic scope; GloMIQO's opt-in advice [02 C11; 03 PE-31]; in print, 2016-2025 [S003 p. 9; S081 p. 9]. (ledger `#heuristic-7`)

<a id="heuristic-8"></a>

## Heuristic 8: Collaborate through shared code; recruit critics and examinees

- **H8 (collaborate through shared code; recruit critics)**: the SnAKe critic Krause co-authors the transition-constrained BO paper [S059 p. 1]; a verification collaboration begun at a seminar, with OMLT's GNN code used to debug the SCIP implementation [S050 pp. 6, 10]; her group's ENTMOOT plugged into an industry consortium's package [S044 pp. 3-4]; Kronqvist co-authors the 2020 verification paper [S005 p. 1].

**Added in T3.6**: SKILL.md cites [S059 p. 1].

**Before T3.6 (moved verbatim)**:

8. **Collaborate through shared code; recruit critics and examinees**: "we switched to a model of just actively contributing to the same open-source projects" (W11). Kronqvist (2019 solver critique; she examined his thesis) became a fellow; Krause (SnAKe critique) co-authored arXiv:2402.08406 [05 R2]. The examining → hiring link is inferred.

**Before T3.7 (moved verbatim)**:

Condensed in SKILL.md on 2026-11-19 (stage T3.7, tighten). The SKILL.md text as it stood before this pass, word for word:

*Heuristic 8:*

8. **Collaborate through shared code; recruit critics and examinees**: "we switched to a model of just actively contributing to the same open-source projects" (W11). Kronqvist (2019 solver critique; she examined his thesis) became a fellow; Krause (SnAKe critique) co-authored arXiv:2402.08406 [05 R2; S059 p. 1]. The examining → hiring link is inferred. (ledger `#heuristic-8`)

<a id="heuristic-9"></a>

## Heuristic 9: Release per paper

- **H9 (release per paper)**: code published with the paper [S068 pp. 2, 6, 12]; a generic and a use-case repository [S082 p. 31]; case studies importable as package examples [S057 p. 14]; benchmark case studies shipped inside the package [S041 pp. 19, 36]; the 2011 solver released with its full test suite preloaded in a GUI [S009 pp. 30-31]; code and data announced [S098 p. 7].

**Added in T3.6**: SKILL.md cites [S068 p. 12]; the 2011 solver released with its test suite preloaded [S009 pp. 30–31] is in Workflow E step 1.

**Before T3.6 (moved verbatim)**:

9. **Release per paper**: pip-installable code with the preprint (OMLT 1.0 on PyPI four days after arXiv v1); one repository per paper; contributors and funding named [03 PE-27, PE-28]. Her paper videos lapsed after 2024-11-04.

**Before T3.7 (moved verbatim)**:

Condensed in SKILL.md on 2026-11-19 (stage T3.7, tighten). The SKILL.md text as it stood before this pass, word for word:

*Heuristic 9:*

9. **Release per paper**: pip-installable code with the preprint (OMLT 1.0 on PyPI four days after arXiv v1); one repository per paper; contributors and funding named [03 PE-27, PE-28; S068 p. 12]. Her paper videos lapsed after 2024-11-04. (ledger `#heuristic-9`)

<a id="heuristic-10"></a>

## Heuristic 10: Make uncertainty explicit and agree its assumptions with the stakeholder (now executable)

- **H10 (make uncertainty explicit)**: executable steps found; upgraded in §5.

The eight steps (08 §5, copied):

1. State why the uncertainty model fits the decision: "Observe here that robust optimisation is, as a conservative method for representing uncertainty, an appropriate choice for optimising a bioreactor where we have to prioritise consistent, effective cellular expansion and require a high degree of certainty that each individual bioreactor will operate." [S085 p. 4].
2. Tabulate each risky modelling assumption with its consequence if violated and how to check or mitigate it [S045 pp. 9-10].
3. Match the optimality tolerance to the parameter uncertainty: "a tight duality gap is meaningless for these uncertain parameters." [S045 p. 30].
4. Calibrate the practitioner's safety-factor baseline to the rigorous answer (the smallest factor that makes the nominal design robustly feasible) [S048 pp. 14-15, 19-20].
5. Report which decisions change under uncertainty and which stay invariant, with the physical reason [S042 p. 8; S060 p. 8]; "uncertainty in mass transfer leads us to design a smaller bioreactor with more hollow fibres." [S085 p. 5].
6. Prove feasibility where you can and measure the rest: "Theorem 1 only guarantees solution feasibility, not optimality." [S033 p. 9]; when a theorem's conditions fail, check the solution a posteriori with an exact solver or sampling [S055 pp. 19-20].
7. Take the robustness parameter off the user by bisection on sampled feasibility or an outer optimisation [S055 pp. 11-12; S033 pp. 15-16, 27-29].
8. Keep more than one analysis type: "we cannot tie ourselves to a single uncertainty analysis method; we want to build consensus between disparate analysis types." [S060 p. 11]; ship rival robust solution approaches behind one model object [S057 pp. 2, 6, 15].

Further cases: lexicographic first-stage plans that recover better after disruptions [S052 pp. 14-17, 21-23; S079 pp. 21-22]; uncertainty wrapped around the practitioner's estimator [S066 pp. 3-6].

Four-way check of the uncertainty cluster (08 §4):

| Cluster (merged by meaning) | Cards read in full/part | 1 Recurrence | 2 Say–do | 3 Executable, non-standard | 4 Exclusivity | Result |
|---|---|---|---|---|---|---|
| Make uncertainty explicit with checks | S045, S085, S042, S060, S048, S033, S055, S057, S066, S052, S079 (11) | ✅ 2014-2023 | ✅ H10's stated quote (Q1) | ✅ | ✗ robust optimisation is shared practice; her robust counterparts reuse published reformulations [S085 p. 5; S033 p. 8] | H10 upgrade (§5) |

**Added in T3.6**: SKILL.md lists five of the eight steps with [S045 p. 30; S048 pp. 14–15; S055 pp. 19–20] and drops "Executable only in outline."

**Fix pass**: SKILL.md now lists all eight steps, each with its cards: steps 1, 2, 5, 7 and 8 gained [S085 p. 4], [S045 pp. 9–10], [S042 p. 8; S060 p. 8], [S055 pp. 11–12; S033 pp. 15–16] and [S060 p. 11]; step 7 points to Method 2 step 7 (delete the parameter).

**Before T3.6 (moved verbatim)**:

10. **Make uncertainty explicit and agree its assumptions with the stakeholder**: "if you don't have an understanding embedded into your optimisation that the world is an uncertain place, then you're probably going to get a bogus solution that is going to hurt you once you implement it." (Q1, Imperial Stories, 2021). Cases: doi:10.1021/acs.iecr.9b01772; doi:10.1007/s10107-021-01762-8. Executable only in outline.

**Before T3.7 (moved verbatim)**:

Condensed in SKILL.md on 2026-11-19 (stage T3.7, tighten). T3.7 cut the fix pass's per-step cards (see **Fix pass** above) to three under the tighten rule (heuristics: at most three cards) and dropped the Q1 quote and the case DOIs. The T3.7 fix round put back the cards of step 3 [S045 p. 30] and of step 7's bisection [S055 pp. 11–12], so SKILL.md cites S045, S048 and S055 on steps 2, 3, 4, 6 and 7; the cards of steps 1, 5 and 8 [S085 p. 4; S042 p. 8; S060 p. 8; S060 p. 11] and of step 7's outer BO [S033 pp. 15–16] are in the eight steps above and in the text below. The SKILL.md text as it stood before this pass, word for word:

*Heuristic 10:*

10. **Make uncertainty explicit and agree its assumptions with the stakeholder**: "if you don't have an understanding embedded into your optimisation that the world is an uncertain place, then you're probably going to get a bogus solution that is going to hurt you once you implement it." (Q1, Imperial Stories, 2021). Cases: doi:10.1021/acs.iecr.9b01772; doi:10.1007/s10107-021-01762-8. Steps: state why the uncertainty model fits the decision [S085 p. 4]; tabulate risky assumptions with consequence and check [S045 pp. 9–10]; match the tolerance to the uncertainty ("a tight duality gap is meaningless for these uncertain parameters." [S045 p. 30]); calibrate the practitioner's safety factor [S048 pp. 14–15]; report which decisions stay invariant [S042 p. 8; S060 p. 8]; check a posteriori where a theorem's conditions fail [S055 pp. 19–20]; set the robustness level for the user by bisection on sampled feasibility or an outer BO [S055 pp. 11–12; S033 pp. 15–16] (→ Method 2 step 7); keep more than one analysis type [S060 p. 11]. (ledger `#heuristic-10`)

<a id="heuristic-11"></a>

## Heuristic 11: Put an expensive component behind a cheap gate (new, 2026-11-19)

Proposal and evidence (08 §5, copied):

**One line**: before adding an expensive component to a solver, give it a cheap gate (a necessary or cheap sufficient test, a coarse relaxation for bounds tightening, the cheap part of the objective for strong branching, a selector learned in the top levels or offline, a rationed callback), and measure the gate's cost against the solver's own routine work.

**Cards (eleven works read in full or in part plus one abstract, 2010-2024)**:
- coarse relaxation for OBBT, fine relaxation for the node [S025 p. 24];
- a necessary and a cheap sufficient dominance test, so only passing cuts are generated at every node; non-dominant facets reused for FBBT [S011 pp. 6-7, 14];
- learn-then-freeze adaptive RLT in the top three tree levels [S004 p. 14];
- strong branching on the cheap convex part, expensive bound updates deferred [S020 pp. 10, 15-16];
- the coarse level's solution projected first, then used to warm-start the next level [S088 pp. 10-12, 19-22];
- an expensive analyser switched off where it does not pay, its callback frequency swept [S005 pp. 5-6, 8];
- an offline-trained selector decides where to pay for SDP cuts: "An expensive approximation may be useful for a specific application, but general-purpose solvers cannot invest too much time in possibly unproductive cutting surfaces." [S021 p. 2]; "We seek an inexpensive oracle that will tell us when it is relevant to generate a cut and over which variables." [S136]; [S119 pp. 6-7];
- detection cost measured against FBBT [S087 p. 4];
- the MIP stopped once the sign question is answered; branching-dependent bounds added as local cuts only when violated [S050 p. 7];
- a weak relaxation without added binaries used as a cheap certificate [S024 p. 29].

**Checks**: recurrence ✅; say–do ✅ ([02] W9; [S021 p. 2]; [S136]); executable ✅; exclusivity ✗ (§4). → heuristic.

**Steps**: (1) name the expensive component and the routine per-node work it competes with (FBBT, LP solves) [S087 p. 4]; (2) find its gate: a necessary condition, the cheap part of a separable objective, a coarse level, or a selector trained before deployment [S011 pp. 6-7; S020 pp. 15-16; S021 pp. 14-15]; (3) use the coarse relaxation for bounds tightening and the fine one for node bounds [S025 p. 24]; (4) learn which expensive cuts matter near the root, then freeze them [S004 p. 14]; (5) sweep the call frequency, report the cost curve and switch the component off on classes where it does not pay (→ Method 4) [S005 pp. 6, 8]; (6) report the gate's own cost.

**Stop rule**: if the learned or cheap rule does worse than random, fall back to the exact rule [S021 pp. 24-25].

Four-way check (08 §4):

| Cluster (merged by meaning) | Cards read in full/part | 1 Recurrence | 2 Say–do | 3 Executable, non-standard | 4 Exclusivity | Result |
|---|---|---|---|---|---|---|
| Spend the expensive relaxation only where a cheap one has failed | S025, S011, S004, S020, S088, S005, S021, S087, S050, S024, S119 (11) | ✅ 2010-2024, seven coauthor lines (Floudas, Mistry, Baltean-Lugojan, Campos, Lomuscio, Ceccon, Hojny) | ✅ her MINLP project page (W9) says the group generates the computationally inexpensive cuts first [02]; [S021 p. 2]; [S136] | ✅ | ✗ cheap-first separation is common solver engineering; her learned RLT rule credits the a priori literature [S004 p. 14] | Heuristic H11 (§5) |

**Added in T3.6**: SKILL.md item 11 with [S011 pp. 6–7; S087 p. 4; S021 pp. 2, 24–25]; Honest Boundary U2 marked resolved; Workflow B step 7 and a routing row point here; catalog D3, D11, E15. Exclusivity fails, so it is a heuristic, not a method ("Not exclusive to her").

**Fix pass**: the T3.6 title, *Spend the expensive relaxation only where a cheap one has failed* (08's cluster name, kept in the copied tables above and below), claimed escalation after a cheap step fails; most cards show gating or selection instead (dominance tests [S011 pp. 6–7], a coarse relaxation for OBBT [S025 p. 24], learn-then-freeze RLT [S004 p. 14], an offline selector [S021 pp. 14–15]); only the coarse-to-fine case is escalation [S088 pp. 10–12]. The item is retitled *Put an expensive component behind a cheap gate*; each gate now carries its card in SKILL.md, the swept callback [S005 pp. 5–8] is named, and the tags D3, D11, E15 appear there. U2 left the Honest Boundary's unverified list (a "Resolved" line follows it). The Roundtable Card no longer lists the cheap gate in its default recommendation, since the heuristic fails exclusivity.

**Before T3.7 (moved verbatim)**:

Condensed in SKILL.md on 2026-11-19 (stage T3.7, tighten). T3.7 cut the per-gate cards that the fix pass had written into SKILL.md (see **Fix pass** above) to three under the tighten rule (heuristics: at most three cards): the necessary or cheap sufficient test [S011 pp. 6–7], the swept callback [S005 pp. 5–8] and the stop rule [S021 pp. 24–25]. The other gates' cards, the coarse relaxation [S025 p. 24], the selector learned near the root [S004 p. 14] or offline [S021 pp. 14–15] and the gate's cost [S087 p. 4], are in the cards and steps above, in catalog D3 and D11 and in the text below; the quote [S021 p. 2] is in the cards above and in the text below. The SKILL.md text as it stood before this pass, word for word:

*Heuristic 11:*

11. **Put an expensive component behind a cheap gate** (new; resolves U2): a necessary or cheap sufficient test [S011 pp. 6–7], a coarse relaxation for bounds tightening [S025 p. 24], a selector learned near the root [S004 p. 14] or offline [S021 pp. 14–15], a callback whose frequency is swept [S005 pp. 5–8]; report the gate's cost [S087 p. 4] (D3, D11, E15). "general-purpose solvers cannot invest too much time in possibly unproductive cutting surfaces." [S021 p. 2]; if the learned rule does worse than random, use the exact rule [S021 pp. 24–25]. Not exclusive to her. (ledger `#heuristic-11`)

<a id="workflows"></a>

## Workflows and routing

### Added in T3.6

- **Routing**: a row for expensive components (Heuristic 11); the uncertainty row now points to executable steps; the Workflow C row names step 1b; "Why does this relaxation work so well?" points to Heuristics 6 and 4.
- **Agentic Protocol, Step 2**: open her paper's card before searching the web.
- **Roundtable Card**: the default recommendation adds expensive components behind a cheap gate (Heuristic 11); the push-back list adds an inherited instance used without an audit (Method 5 step 1b). The rest of the card is unchanged.
- **Workflow B step 4** (08 §5, copied):

The cluster passes three checks (§4), but Workflow B step 4 ("Borrow from a neighbour") already carries the stated claim [02 C10; 02 L2.6], so the cards go there as practice and protocol rather than as a duplicate heuristic.
- **Practice**: logarithmic encodings from the MIP community carried into piecewise McCormick relaxations and their claim tested inside the full solver [S009 pp. 3, 19, 29]; SMT in place of constraint programming inside a published decomposition, everything else held fixed [S155 p. 3; S058 pp. 1, 4-7]; approximation ratios for practitioners' heuristics in process systems engineering [S061 pp. 9-12, 35-36; S069 p. 2; S135 pp. 2-3; S079 p. 32]; argumentation as an explanation layer [S017 pp. 1, 4, 8; S073 p. 2]; MILP structure exploitation brought into neural-network verification [S005 pp. 1-2, 6]; a convex relaxation over visitation polytopes brought into BO planning [S059 pp. 4-7].
- **Protocol** (executable): name the neighbour's device and its claim; hold the rest of the published pipeline fixed and swap one component [S155 p. 3]; test the claim inside your own full solver or classes [S009 p. 29]; write where the import loses, "ManyOpt is frequently slower than state-of-the-art MINLP solvers, but it offers the trade-off of a completely different method to address the problem." [S058 p. 13]; [S155 p. 1]; for a position paper, list the intellectual differences, the definitions the other side needs, four uses each with one published example, per-problem complexity tables and numbered open questions [S069 pp. 1-6, 11, 22-23].

- **Workflow B**: step 1 adds the data-driven variant (D6); step 5 cites GALINI's plug-ins [S087 pp. 2–4] (D4); step 7 is new (Heuristic 11).
- **Workflow C**: step 1 includes step 1b; step 5 is new: matched controls that differ in one component [S047 p. 8; S021 p. 25] (E3); more cases [S023 p. 22; S077 pp. 3, 9; S082 pp. 5, 9].
- **Workflow D**: step 1 adds E6 (cases: 10%-tie win counts [S009 pp. 28–29], slices by structural class [S001 pp. 17–18], the primal or dual side of the gap [S072 p. 21]); step 5 adds WM1 [S155 p. 1; S072 p. 1] and WM5 [S088 p. 26].
- **Workflow E**: step 1 cites the solver released with its test suite [S009 pp. 30–31].
- **Stages without a method**: reviews share a layout, technique catalog WM2 [S003 p. 12; S014 p. 2]; two MEng projects she supervised became group papers [S100 p. 13; S024 p. 15; S117 p. 3; S135 p. 20]; still no method for drafting research articles or for supervision (08 §3.3).

### Fix pass (2026-11-19)

- **Routing**: drafting questions have their own row: Workflow D step 5 and the catalog's writing moves WM1-WM10, offered as practice seen in her co-authored papers, not a stated drafting process; supervision, literature search, grants, leaving a line and refereeing keep the "no distillable Misener method" row. "Why does this relaxation work so well?" points to Heuristic 4 (Heuristic 6 folded into it). The uncertainty row says "eight steps".
- **Agentic Protocol, Step 2**: footer references take authors, venue and year from the card's header and coauthor line or from [Sources](#sources).
- **Roundtable Card**: a line on citing in a brief (cards first, research notes only where no card covers the claim), which supersedes the protected Activation Rules' *(no paper cards yet)*; the default recommendation drops the T3.6 addition *expensive components behind a cheap gate* (Heuristic 11 fails exclusivity, 08 §4); the push-back item reads *an unaudited inherited instance (her papers' practice, not a stated rule)* instead of *an inherited instance used without an audit*.
- **Stage Workflows intro**: the changelog line *Card refs added on 2026-11-19 and the earlier wording: ledger `#workflows`.* became a plain pointer.
- **Stages table**: the drafting row is narrowed to her drafting process (no source) and points to the writing moves; the quote is now the contiguous "writer of scientific texts" from one thesis acknowledgement (the earlier *as a writer of scientific texts* skipped words of the original; full wording in note 04 §4); the MEng sentence cites the group-paper links [S024 p. 15; S135 p. 20] next to [S100 p. 13; S117 p. 3].
- **Workflow D step 5 and the anti-patterns**: the catalog's writing moves are cited as WM1, WM4, WM5; a bare (W1) now always means her Floudas essay.

### Before T3.6 (moved verbatim)

Research Task Routing:

| User says | Workflow | Main methods |
|---|---|---|
| "Is this topic worth doing?" | Workflow A | Method 1 + Heuristics 1, 2, 7 + Taste quick-check |
| "How do I attack this model?" "Where is the structure?" | Workflow B | Method 1 |
| "Big-M or hull?" "Which relaxation level?" | Workflow B, step 2 | Method 2 |
| "A trained model (trees, ReLU net, GNN) sits inside my problem" | Workflow B, step 3 | Method 3 |
| "My BO acquisition needs a global optimum" | Workflow B, step 3 | Method 3 steps 2-4, 8; Heuristic 7 |
| "Which solver should I use?" "Is my model convex?" | Workflow B step 1, then Method 5 | Method 1 step 5 (SUSPECT's use "for solver selection" [03 PE-15]); class and structure before solver (inferred [05 §7]); Method 5 limitations (date benchmarks) |
| "My parameters or data are uncertain" | Heuristic 10 (outline only; say so) | [02 C16] |
| "How do I design the experiment? Which baselines?" | Workflow C | Method 5, Method 4 step 2, Heuristic 3 |
| "Are these results good? Should it be on by default?" | Workflow D | Method 4, Method 2 step 7 |
| "My project is stuck" "It works at the root but not in the solver" "Worse than expected; keep going?" | Workflow F | Method 4, Method 2 stop rules, Method 5 step 6 |
| "Release the code / plan the talk / answer the referee" | Workflow E | Heuristics 5, 8, 9 |
| "Why does this relaxation work so well?" | Heuristic 6 (one documented instance) | Method 2 |
| Convex-MINLP decomposition, worst-case or convergence proofs, copositive/SDP theory | Outside this lens (Activation Rules) | Method 5 reporting rules only |
| Paper drafting, supervision, literature search, grant writing, leaving a line, refereeing | No distillable Misener method: give generic advice labelled "not Misener-style" | — |

If two rows match, run the earlier stage first (A → B → C → D → E) and name the other row as the follow-up. A stuck or failing project goes to Workflow F first, even if another row also matches.

Workflow B:

**Input**: the problem card and the partner's model or code.

**Steps**:
1. Read the model as written for redundant equalities, named structures, convex pieces, symmetry (→ Method 1 steps 1-3).
2. If two textbook formulations bracket the problem, design the family between them (→ Method 2 steps 1-3).
3. If part of the model is learned from data, write it as constraints (→ Method 3 steps 1-3).
4. Borrow from a neighbour: multiparametric programming from control, verification, the "jedi masters" of MIP heuristics [02 L2.6, L3.5].
5. Design for extension: what will others plug in later? [03 PE-29]
6. Prove the endpoints and hierarchy; label the rest experimental (→ Heuristic 4).

**🔴 Checkpoint**: if the idea tightens nothing, say so ("i do not claim that i am tightening anything", T3 [18:01], ASR); the claim must then come from speed or scale. A new parameter goes on slide 1 with a planned robustness test.

**Output**: a formulation note: structure exploited, family and parameter, propositions with assumptions (proof vs practical), extension points.

Workflow C:

**Input**: the formulation note, an implementation, candidate test sets.

**Steps**:
1. Method 5 steps 1-6: test set, competitors, settings, strengthened baseline, calibration, independent verification.
2. Method 4 step 2: cumulative ablation inside the full solver.
3. Method 2 step 5: parameter sweep with random and deliberately weak controls.
4. One repository per paper, scripts mapped to figures (→ Heuristic 9).

**🔴 Checkpoint**: baseline solves nothing → recalibrate; solves everything → too easy. Infeasible returned points are failures; bounds on guessed variable bounds are dropped; anomalies are re-run.

**Output**: run logs, verified tables, time and gap-at-limit profiles.

Workflow D:

**Input**: verified tables, ablations, sweeps.

**Steps**:
1. Grade per class, then decide the default (→ Method 4 steps 3-6).
2. Purpose check: has the design defeated its own goal (global turned local, as in SnAKe)? "I should have understood this" (T11 [28:13], ASR).
3. Metric check: the standard metric next to any new one.
4. Parameter check: one setting across the class, or label the rule heuristic (→ Method 2).
5. Write the loss-and-scope paragraph (→ Method 5 step 8).
6. Outside validation: has a solver developer implemented it (Bonami, per T7 [32:43], ASR) or a competing group extended it? [02 L5.3]

**🔴 Checkpoint**: if a student reports "this doesn't actually work" (T11 [25:58], ASR), stop and re-derive; in SnAKe the student's fix became the contribution [04 T9]. A one-class gain does not become the default.

**Output**: a claims list tagged proved, experimental or class-scoped, plus the default decision.

Workflow E:

**Input**: accepted paper, code, slides, reviews.

**Steps**:
1. Release: pip-installable code with the preprint, README with citation and contributor-funding credit, public instances (→ Heuristics 2, 9).
2. Talk: weakness on slide 1; credit the student ("if at any point I refer to my work I actually mean their work", T11 [02:47], ASR); end with an open-challenge list and ask "what's missing on this list" (T4 [25:00], ASR).
3. Reviews: concede the precise error, keep the core claim with a worked example, restate novelty as numbered contributions (→ Heuristic 5).
4. Critique: absorb and reposition, work with the critic (→ Heuristic 8); withdraw an incorrect theorem publicly [05 R1-R3; 03 PE-34].

**🔴 Checkpoint**: if a tool rests on one leaving student, hand it over or mark it frozen in the README now. Her record shows tools freezing silently instead (GALINI, SUSPECT) [03 PE-43].

**Output**: release checklist, talk deck, response letter, maintenance plan.

Stages without a distillable Misener method:

Say "no distillable Misener method", give generic practice and label it "not Misener-style".

| Stage | Why |
|---|---|
| Paper drafting and revision | No source on how she writes; students thank her "as a writer of scientific texts" without saying how [04 §4] |
| Supervision mechanics | Meetings, draft review, topic assignment, stopping projects, authorship: undocumented; acknowledgements only. Context: postdocs and fellows as day-to-day mentors (6 of 11 theses) [04 S4] |
| Literature search | One remark only (T11 [16:52]) |
| Grant writing | One source (T8): mutual critique of grants [02 L6.5] |
| Leaving a line | Exits show only as silence at grant ends; her account: "very opportunistic" [06 §5] |
| Refereeing | Only Top Reviewer (NeurIPS 2022, 2023) and Area Chair (2024) records [06 §1.1] |

### Before T3.7 (moved verbatim)

Condensed in SKILL.md on 2026-11-19 (stage T3.7, tighten). In the stages table T3.7 cut back the fix pass's drafting quote and MEng sentence (see **Fix pass (2026-11-19)** above) and T3.6's WM2 cards; the rows below are the state before T3.7. The T3.7 fix round gave the routing row its three-column header (Research Task Routing's) in place of the stages table's two-column one, so the row's third cell renders; the row text is unchanged. The SKILL.md text as it stood before this pass, word for word:

*Research Task Routing, solver-choice row:*

| User says | Workflow | Main methods |
|---|---|---|
| "Which solver should I use?" "Is my model convex?" | Workflow B step 1, then Method 5 | Method 1 step 5 (SUSPECT's use "for solver selection" [03 PE-15]); class and structure before solver (inferred [05 §7]); Method 5 limitations (date benchmarks) |

*Stages without a distillable Misener method, drafting row:*

| Stage | Why |
|---|---|
| Paper drafting and revision | No source on her drafting or revision process; a thesis thanks her for help as a "writer of scientific texts" without saying how [04 §4]. Her co-authored papers show the writing moves of catalog §4 (WM1-WM10; reviews as maps, WM2 [S003 p. 12; S014 p. 2]): offer them labelled as observed in her papers |

*Stages without a distillable Misener method, supervision row:*

| Stage | Why |
|---|---|
| Supervision mechanics | Meetings, draft review, topic assignment, stopping projects, authorship: undocumented; acknowledgements only. Context: postdocs and fellows as day-to-day mentors (6 of 11 theses) [04 S4]. Two MEng projects she supervised became group papers [S100 p. 13; S024 p. 15; S117 p. 3; S135 p. 20] |

Claim audit 2026-11-19 k=14 ([10-claim-audit.md](10-claim-audit.md)): the S135 p. 20 part is partial (the card links S135 to the MEng line only through authorship).

---

<a id="anatomy-apogee"></a>

## Anatomy: APOGEE (2009-2011), closed in 2018

### Full-text basis

- APOGEE paper read in full [S009]: two prior large-scale studies with linearly many binaries and the Vielma-Nemhauser logarithmic models as the entry [S009 pp. 1–3]; the judging principle stated before the results [S009 p. 23]; 25 problems × 7 partition levels × 2 encodings inside the full branch-and-bound, with a 10% tie rule [S009 pp. 28–30]; "Therefore, we will continue using the linear relaxation scheme to solve pooling problems." [S009 p. 30]; the free tool with a GUI and the test suite [S009 pp. 30–31].
- The 2010 precursors read in full: the emissions-law model and its relaxations [S025]; the four-page TOGO abstract, where the partition level was chosen per topology "after some experience with the particular topology" [S152 p. 99].
- Origin: the essay [S143 p. 13] (the 2026-10-10 quote is from note 01; the card's own quotes are on the same page).
- Closure: "The position on the P/NP boundary of the multiple outputs and one pool subclass is thus an ideal starting point for approximating algorithms that cross into NP-hardness." [S049 p. 32]; Haverly's instances in a strongly-polynomial subclass [S049 p. 2].
- GloMIQO's default against the piecewise schemes [S004 p. 13].

### Before T3.6 (moved verbatim)

doi:10.1021/ie8016048 · doi:10.1016/j.compchemeng.2011.01.026 · doi:10.1007/s10898-017-0577-y

| Dimension | Content |
|---|---|
| Origin | Stated: the advisor's intuition that "piecewise linear underestimators seemed to be effective in solving the pooling problem" (essay p. 13) |
| Key insight | Relax bilinear terms piecewise; judge every relaxation inside the whole algorithm |
| Minimum evidence | 25 pooling problems × 7 partition levels × 2 schemes; logarithmic wins at high counts, but the whole algorithm is fastest at low counts, where linear wins [01 SW1] |
| Abandoned path | Her logarithmic novelty; later piecewise relaxations off by default in GloMIQO |
| Reception | Dey & Gupte's factor-n worst-case bound (doi:10.1287/opre.2015.1357), which she absorbs as having "further unpacked this relationship"; Nagarajan et al. back linear unless many partitions are needed (doi:10.1007/s10898-018-00734-1) [05 R1, PC-11] |

<a id="anatomy-glomiqo"></a>

## Anatomy: GloMIQO and the MIQCQP relaxations (2012/13)

### Full-text basis

- MIQCQP relaxation paper read in full [S011]: edge-concave facets only where they dominate the termwise relaxation, a necessary and a cheap sufficient dominance test, non-dominant facets reused for bounds tightening [S011 pp. 5–8, 13–14]; the cumulative ablation and class-split verdict [S011 pp. 17–19]. The "N = 2/4/8" grid was run on packing only; pooling inherited N = 4 [S011 p. 17].
- GloMIQO paper read in full [S004]: reformulation and detection before relaxation [S004 pp. 4–11]; one parameter setting for all runs and the default decision [S004 p. 13]; the benchmark protocol and findings [S004 pp. 18–26]; no component ablation; wins attributed through worked instances [S004 pp. 8, 24–25]; "We do not know if it would be possible for GloMIQO to dynamically abandon its more elaborate approach under circumstances where a SCIP-like algorithm is more effective or if a slower solution time on the smaller problems is a price we pay for addressing the exceptionally large problems." [S004 p. 26].
- GloMIQO 2 is known from its abstract only [S026]; the GloMIQO 2.2 test-suite report from metadata only [S102].

### Before T3.6 (moved verbatim)

doi:10.1007/s10107-012-0555-6 · doi:10.1007/s10898-012-9874-7 · GloMIQO 2: doi:10.1080/10556788.2014.916287 (not read)

| Dimension | Content |
|---|---|
| Origin | Stated: Floudas required "a promise to write and publicly release a global MINLP solver" (2008); she "told him he was being unreasonable" (essay p. 14) |
| Key insight | Find structure the user did not declare; add edge-concave facets that dominate termwise McCormick; then branch and bound |
| Minimum evidence | 399 problems vs BARON, Couenne, LindoGLOBAL, SCIP: fastest on 68%, 81% solved within the limit; every answer Perl-checked; "Couenne 0.4 returns an infeasible point in over half of the 399 test cases" [01 SW2] |
| Evidence against | SCIP faster on smaller instances; APOGEE beat it on pooling; SCIP 8 disabled re-implemented edge-concave cuts (doi:10.1007/s10898-023-01345-1) |
| Reception | *J. Global Optim.* Best Paper 2013; "the work that got me hired" (T8 [11:12], ASR) |

<a id="anatomy-antigone"></a>

## Anatomy: ANTIGONE (2014)

### Full-text basis

- ANTIGONE paper read in full [S001]: "the intellectual contribution is the way ANTIGONE ties together its many constitutive algorithms." [S001 p. 2]; term classes with convexity and edge-concavity labels [S001 pp. 4–8]; 2571 instances, rebuilt minlp.org set, freeze date, exclusion rule, Perl check with a stated threshold, guessed-bound lower bounds discarded, profiles [S001 pp. 8–11, 17]; slices by structural class and the scope sentence "ANTIGONE derives the core of its strength from quadratic instances." [S001 pp. 17–18]; no composition-rule convexity detection, a missed composite-term detection admitted [S001 pp. 8, 14].
- The test suite as its own report [S123 pp. 1–2]; the signomial framework that preceded it [S032 pp. 2, 10–12, 18].
- The extension point moved to GALINI: a solver built for developers to extend at runtime [S087 pp. 2–3].

### Before T3.6 (moved verbatim)

doi:10.1007/s10898-014-0166-2 (her most cited work)

| Dimension | Content |
|---|---|
| Key insight | Stated: "the intellectual contribution is the way ANTIGONE ties together its many constitutive algorithms"; term types are C++ classes so future relaxations plug in [03 PE-29] |
| Minimum evidence | 2571 problems × 5 solvers, the Perl check, gap profiles [03 PE-01] |
| Evidence against | Her own: "ANTIGONE derives the core of its strength from quadratic instances." Outside: missed convexity, guessed bounds, frozen code declining in benchmarks [05 PC-01, PC-02, §4] |
| Abandoned path | No ANTIGONE 2; extension point moved to GALINI. Why: unknown (U3 single-source) |

<a id="anatomy-trained-models"></a>

## Anatomy: Optimising over trained models (2018-2025)

### Full-text basis

- Gradient-boosted trees, read as arXiv v3 [S020]: BASF tree ensembles as constraints, structure-driven branching and bounding, a PCA-based penalty, a public UCI stand-in [S020 pp. 1, 5–18]; "The Gurobi heuristics generally outperform the B&B algorithm, but the B&B algorithm derives better lower bounds." [S020 p. 22]; the risk wording stays in the v3 body [S020 pp. 1, 5]; the 2018 seminar abstract still has risk control in its title [S119 p. 17].
- ENTMOOT, read as arXiv v3 [S023]: "While Gurobi 9 is still the best choice for small and moderate instances, i.e. instances that commonly occur in design of experiments, we want to highlight that algorithmic elements exploiting the underlying structure of tree-based models can help when scaling the optimization efforts." [S023 p. 19].
- OMLT [S006 p. 4]; tree-kernel BO [S047 pp. 4–6, 8]; BARK re-grading the earlier heuristic [S081 p. 1].

### Before T3.6 (moved verbatim)

doi:10.1287/ijoc.2020.0993 · doi:10.1016/j.compchemeng.2021.107343 · arXiv:2202.02414 · arXiv:2207.00879 · arXiv:2503.05574

| Dimension | Content |
|---|---|
| Origin | BASF seed project (2017); being "in a computer science department" (T8 [46:34], ASR) |
| Why then | Mišić's tree-ensemble preprint came nine months earlier and her v1 cites it: early follower on trees, then toolmaker [06 T8] |
| Key insight | A trained model is structured constraints; rival formulations become alternatives |
| Minimum evidence | A BASF catalysis instance and a public concrete-mixture instance; heuristics plus exact B&B |
| Abandoned path | v1's "risk control" framing left the title by v3; reason not stated [03 PE-38] |
| Reception | COIN-OR Cup 2022 |

<a id="anatomy-p-split"></a>

## Anatomy: P-split and partition-based ReLU formulations (2021-2026)

### Full-text basis

- CPAIOR paper, read as arXiv v1 [S040]: two extremes and the folklore, knob P, endpoints by Fourier-Motzkin, a conditional hierarchy and a worked example where it fails without its hypothesis, a sweep across P and classes [S040 pp. 1–13]; "Note that the P-split formulations are in general robust towards the choice of P." [S040 p. 12].
- NeurIPS 2021, read as arXiv v2 [S013]: "The formulations are hierarchical: their relaxations start at a big-M equivalent and converge to the convex hull." [S013 p. 1]; N swept from 1 to 10 with random and uneven controls [S013 pp. 7–9]; best N problem-dependent [S013 p. 8].
- Journal version, read as arXiv v3 [S046]: Theorems 1, 2, 5 (endpoints and hierarchy) and 6 (ceiling) [S046 pp. 6–13]; 344 instances [S046 pp. 18–26]; a practical range of two to four variables per split on clustering and P_ball, P = 2 or 4 splits on ReLU nets, and no rule [S046 pp. 22–25]; Pyomo.GDP plugin and OMLT strategy [S046 pp. 3, 16]; the scope sentence [S046 p. 26].

### Before T3.6 (moved verbatim)

doi:10.1007/978-3-030-78230-6_19 · arXiv:2102.04373 · doi:10.1007/s10107-025-02232-1 (full texts not read)

| Dimension | Content |
|---|---|
| Origin | Stated (ASR): a question from Lomuscio's verification group (T8 [21:25]); partition idea credited to Kronqvist |
| Key insight | Interpolate between big-M and hull with one parameter P |
| Minimum evidence | Hierarchy theorem; K-means, P_ball, ReLU networks; the journal version has 344 instances |
| Reception | CPAIOR Distinguished Paper; NeurIPS accepted after review, the N-selection question still open |

<a id="anatomy-lmtd"></a>

## Anatomy: LMTD convexity, from a student's plot to a proof (2015-2016), new on 2026-11-19

- **Why added**: a work read in full that carries Method 1 steps 2 and 6, Heuristic 6 and the audit step 1b of Method 5, and shows how a supervised MEng project became a group paper (08 §3.3, §9).
- **Origin**: an MEng project she supervised (Miten Mistry; second marker Panos Parpas), presented at EUROPT and ISMP 2015, then published with the student as first author [S100 p. 13; S024 p. 15].
- **Key insight**: approximate the reciprocal of LMTD, whose error enters the model linearly, prove it C² and strictly convex on the positive quadrant once limits are added, and use tangent cuts without binaries inside an iteratively refined MILP [S024 pp. 9–17, 21–22]; the proof devices are polar coordinates and L'Hôpital along the indeterminate line, and Hessian minors after w = e^n [S024 pp. 9–14; S100 pp. 44–61] (catalog P5).
- **Minimum evidence**: the student's account, "We see from Figure 3.1 that the reciprocal of LMTD has a shape that looks convex (where defined, the epigraph looks convex), we will not only prove that this is true but we will use this to form a suitable approximation." [S100 p. 42]; three small MINLPLib2 heat-exchanger instances; within 33 s the weak variants (no added binaries) give lower bounds better than the library-reported solver bounds on two of them, and the third cannot be compared because the library value rests on a perturbed LMTD [S024 pp. 24, 28–29].
- **Audit**: a feasible point below the library's "global" value because of a perturbed LMTD [S024 p. 24]; the published model corrected against its GAMS file with a change log [S100 pp. 116–118].
- **Why it works**: "The convexity result in this manuscript justifies why the Escobar and Grossmann (2010) model works better with the LMTD term moved to the objective." [S024 p. 16].
- **Limits written in**: three small instances, no convergence step in the implementation, fresh MILP solves limit scalability [S024 pp. 23, 28]; "We find that, as it stands, the algorithm fails to scale in the directions that we want it to scale." [S100 p. 99]; "The solvers appear to be finding the global solutions however providing a certificate is not so easy as the lower bounds placed on the problems are not informative." [S024 p. 33].
- **Methods**: Method 1 steps 2 and 6; Method 5 step 1b; Heuristic 4 (formerly 6).
- **Fix pass**: the condensed table left SKILL.md (seven anatomies were above the framework's three to five; SKILL.md keeps a pointer from Method 1 step 2 and from the anatomy section). Its minimum-evidence row overstated the result: *bounds better than those reported for global solvers on three instances [S024 pp. 23–32]*. Tables 10-11 show better lower bounds on Models 1 and 2 only (gaps 23% vs 35%, 2-5% vs 7%), and the paper cannot compare Model 3's gap [S024 p. 29]; the corrected wording is in the bullet above. The other rows, as they stood: origin, an MEng project she supervised, presented in 2015, published with the student first [S100 p. 13; S024 p. 15]; key insight, the reciprocal of LMTD is C² and strictly convex once limits are added, so tangent cuts need no binaries [S024 pp. 9–17] (P5); audit and explanation, a library optimum rested on a perturbed LMTD [S024 p. 24] and the proof explains a published model's behaviour [S024 p. 16]; limits written in, three small instances, no convergence step in the code [S024 pp. 23, 28].

<a id="anatomy-galini"></a>

## Anatomy: GALINI and the pooling problem at scale (2017-2022), new on 2026-11-19

- **Why added**: two works read in full or in part that carry Method 1 step 4 (structure carried by the modelling object), Method 4 (plug-ins off by default, the cut ablation) and Method 5 step 3 (a rival given her components), with the losses written in.
- **Origin**: the EPSRC Early Career Fellowship "GALINI" (2017-2022, note 01 §1.1); of about 30 MIQCQP solvers only SCIP and MINOTAUR target developers, and GALINI lets them extend a solver at runtime without modifying it [S087 pp. 2–3].
- **Key insight**: "The advantage of this approach is that, although GALINI itself is unaware of the pooling problem, GALINI can, through this library, behave as if it has perfect knowledge of its structure." [S072 p. 2]; class-specific plug-ins (a convex relaxation as cut generator, a MIP restriction as primal heuristic) enabled by configuration [S072 pp. 2, 6–16].
- **Minimum evidence**: Gurobi 9.1 in six configurations, including time-counted and oracle use of her components; performance profiles on time and gap; a lower-bound/upper-bound breakdown that locates the win on the largest dense instances in the upper bound [S072 pp. 16–23, 28–35]. The general solver paper ablates every cut class alone, in pairs and together on MINLPLib 2 and QPLIB [S087 pp. 16–18].
- **Evidence against**: not competitive with Gurobi on sparse instances; node throughput much slower [S072 p. 21]; the restriction kept a true restriction: "We decided not to disable the non-linear constraints since by doing that the new model would not be a restriction of the original model, creating a subtle bug that is difficult to debug for users." [S072 p. 16].
- **Abandoned path**: the general paper stayed a preprint [S087]; no code commits after 2022-07-14 (note 03 PE-43); U6 in the Honest Boundary.
- **Methods**: Method 1 step 4; Method 4 steps 3-4; Method 5 steps 3 and 8.
- **Fix pass**: the condensed table left SKILL.md, whose Method 1 step 4, Method 4 limitations, Method 5 steps 3 and 8, the Workflow E checkpoint, the inner tensions and U6 already carry each row; SKILL.md points here from the ANTIGONE anatomy. The rows, as they stood: origin, the EPSRC fellowship *GALINI* (2017-2022) [01 §1.1], a solver developers extend at runtime [S087 pp. 2–3]; key insight, the modelling layer carries the structure [S072 p. 2]; minimum evidence, plug-ins off by default, Gurobi in six configurations given her components, smaller gaps on the largest dense instances [S072 pp. 15–23]; evidence against, not competitive with Gurobi on sparse instances [S072 p. 21]; abandoned path, general paper a preprint, no code commits after 2022-07-14 [03 PE-43].

<a id="anti-patterns"></a>

## Anti-patterns

**Added in T3.6**: a toy explains a device before its evidence (catalog WM4) [S020 pp. 4, 12, 14, 17; S040 pp. 8–9; S013 pp. 6–7; S011 p. 8; S145 p. 2; S032 p. 8]. Candidate anti-patterns considered and not added: root-only evidence (already a Method 4 stop rule); detection without exploitation (recorded as a Method 4 contradiction and an inner tension, not as her stated rule).

**Before T3.6 (moved verbatim)**:

See Research Taste, Warning signs 1-3 (per-comparison tuning, invented metrics, techno-solutionism; instead Heuristic 7, Method 2 step 5, Method 5) and Method 1 step 4 (brittle rule-based detection). Not listed there: toy examples as motivation, "we're not going to use examples this small to try and motivate ..." (T2 [18:53], ASR); instead Taste mark 2.

<a id="trajectory"></a>

## Trajectory

### Full-text evidence (08 §8 and §9, copied)

| Period | Works with a card [read in full/part] | Main topics (cards) |
|---|---|---|
| 2005-09 | 5 [0] | Pooling reviews and piecewise-linear comparisons, abstract level only [S007; S008; S022; S125; S153] |
| 2010-14 | 30 [15] | Pooling with emissions constraints and APOGEE [S025; S152; S009]; piecewise approximations [S012]; MIQCQP relaxations, GloMIQO, ANTIGONE, the MISO framework and test suite [S011; S004; S001; S032; S123]; a bioreactor MINLP in a biomedical consortium [S045; S085; H002; S054] |
| 2015-19 | 52 [36] | Biomedical consortium papers, mostly as a middle author [S042; S043; S070; S060]; structure and symmetry detection [S076; S120; S091]; heat recovery and approximation algorithms [S024; S100; S061; S135]; SMT and argumentation [S155; S058; S017]; BO and design of experiments with Deisenroth's students [S029; S095; S075; S034; S041]; robust optimisation with Wiebe [S033; S048]; pooling complexity [S049]; ML inside the solver [S021]; community work [S003; S143; S119; S010]; Lasserre multilevel [S088] |
| 2020-24 | 41 [35] | Optimisation over trained models: trees, ReLU nets, GNNs, OMLT [S020; S005; S013; S023; S006; S035; S051; S038; S050]; intermediate formulations [S040; S063]; GALINI and SUSPECT [S087; S072; S068]; robust GP constraints and ROmodel [S055; S057]; surrogate perspectives [S014; S015]; BO with BASF [S039; S047; S031; S083; S059; S077]; partial Lasserre [S078]; chemometrics and statistics [S056; S066; S098] |
| 2025-26 | 17 [14] | BO over graphs and molecules [S093; S067; S128; S090]; tree kernels and meta-learned BO [S081; S086; S113]; datasets and frameworks for chemistry [S097; S044; S028]; GPLVMs [S115; S126]; the journal P-split paper [S046] |

**Turns visible in the texts**:
1. **Pooling to general solvers, 2011-2014**: the thesis arc [S092]; the MIQCQP paper as the bridge from pooling-specific to generic relaxations [S011 p. 2]; GloMIQO and ANTIGONE [S004; S001 p. 2].
2. **Computational partner in a biomedical consortium, 2014-2018**: the partner lab's bioreactor model solved with ANTIGONE [S042 p. 7; S045 pp. 2-3]; robust follow-up [S060 pp. 2, 4]; middle-author biology papers [S037; S096].
3. **C++ solvers to Python tools and theory, 2016-2022**: SUSPECT in Pyomo [S068 pp. 2, 6]; GALINI as an extensible solver [S087 p. 3; S072 p. 2]; structure theory for pooling [S049 pp. 2-3]; approximation algorithms [S069 p. 2].
4. **ML inside the solver, then optimisation over trained models, 2018-2022**: offline-learned cut selection [S021 pp. 1-3; S119 pp. 6-7]; trees, nets and the toolkit [S020; S013; S006].
5. **BO for chemistry with BASF, then graphs, 2022-2026**: [S039 p. 1; S047 pp. 1, 10; S081 pp. 1, 9; S067 pp. 2-3]; the group's statistics line with Filippi, where she is a middle author [S066 p. 12; S115; S126].
6. **Formulation theory kept on the side throughout**: P-split 2021-2026 [S040; S013; S046]; Lasserre 2019-2023 [S088; S078].

**What stayed constant**: structure first, from the 2010 emissions law [S025 p. 13] to the 2025 graph encodings [S128 pp. 10-16]; pooling as the test bed, 2010 to 2022 [S025; S009; S011; S049; S048; S072; S057 pp. 15-16]; exact or global solves where possible [S020 pp. 8-14; S047 pp. 5-6; S067 pp. 2-3]; losses written in, 2012 to 2026 [S011 p. 19; S004 p. 26; S155 p. 1; S072 p. 21; S115 p. 8; S046 p. 26]; parameter scepticism, 2013 to 2025 [S004 p. 13; S143 p. 13; S039 p. 1; S081 p. 5].

- **PhD and postdoc era (2009-2014)**: Floudas co-authors 29 of the works with a card; the solver and pooling papers are two- or three-author papers with him [S012; S011; S004; S001; S032; S123; S152], with Gounaris on pooling [S025] and Thompson on APOGEE [S009]. Two pieces are single-author: the 2014 CPSE newsletter [S145] and the 2016 Floudas essay [S143].
- **Biomedical consortium (2013-2018)**: Panoskaltsis (23 works), Mantalaris (21), Pistikopoulos (19), Fuentes-Garí (19), Velliou (13). She is first and corresponding author on the bioreactor optimisation papers [S045; S085; H002] and a middle author on the others [S054; S042; S037; S096].
- **Students and fellows (2016-2026)**: Tsay (18 works), S. Zhang (12), Mistry (9), Letsios (8), Kronqvist (8), Ceccon (7), Baltean-Lugojan (7), Wiebe (7), Olofsson (7), Thebelt (7), Qing (7), Folch (7), Campos (7), Sedgwick (7), Kouyialis (6), Odgers (5). Two-author papers with a student carry several lines: pooling theory [S049], LMTD convexity [S024], symmetry [S120; S076], SMT [S155], GALINI pooling [S072], ROmodel [S057], graph encodings [S128]. From 2016 the student is first author and she is last or corresponding author [S128; S090; S081; S086; S067].
- **Industry**: BASF (R. M. Lee 15 works, Shafei 10, Walz 8) from the tree paper onward [S020; S023; S047; S081; S113]; Schlumberger [S033; S048; S055]; Royal Mail [S117 p. 3; S135; S079]; Eli Lilly [S066 p. 13; S056]; IBM CPLEX developers [S021; S136]; Bayer [S041]; an Evonik-led consortium [S044].
- **Neighbouring communities at Imperial**: ML with Deisenroth (7 works) and van der Wilk (8) [S029; S075; S039; S059]; verification with Lomuscio [S005] and Huth [S058]; argumentation with Toni [S017; S073]; numerical optimisation with Parpas [S088; S078]; statistics with Filippi [S066; S115; S126]; outside optimisation, air-quality GPs begun at a Dagstuhl seminar [S098 p. 7].
- **Community roles**: Dagstuhl report co-editor [S119]; a 13-author library paper [S010]; a two-author perspective with Biegler [S015].
- **Students' projects as seeds**: two MEng projects she supervised became group papers [S100 p. 13; S024 p. 15; S117 p. 3; S135 p. 20].
- **Frequencies by period** (co-authors on ≥2 works with a card in the period): 2005-09 Floudas 5, Gounaris 4; 2010-14 Floudas 20, Fuentes-Garí 9, Velliou 8, Pistikopoulos 8, Panoskaltsis 8, Mantalaris 7, Brito dos Santos 4, Gounaris 3, Rende 3, J. Li 2, Skjäl 2, Westerlund 2, Pefani 2; 2015-19 Panoskaltsis 15, Mantalaris 14, Pistikopoulos 10, Fuentes-Garí 10, Georgiadis 7, Kouyialis 6, Olofsson 6, Deisenroth 6, Mistry 5, Baltean-Lugojan 5, Allenby 5, Velliou 5, Brito dos Santos 5, Floudas 4, Letsios 4, Kostoglou 4, Pefani 4, Wiebe 3, Cecílio 3, Bonami 3, Geris 3, Mehrian 3, Tahlawi 3, and nine at 2; 2020-24 R. M. Lee 10, Tsay 10, Thebelt 7, Kronqvist 7, Walz 7, S. Zhang 6, Ceccon 5, Shafei 5, Folch 5, Sudermann-Merx 4, Wiebe 4, Mistry 4, van der Wilk 4, Campos 4, Letsios 4, Sedgwick 3, Odgers 3, and eleven at 2; 2025-26 Tsay 8, Qing 7, S. Zhang 6, Shafei 5, R. M. Lee 5, Xie 4, van der Wilk 4, Langdon 4, Kappatou 4, Sedgwick 4, Boyne 3, and six at 2. The counts include abstract- and metadata-level cards (computed from the digests' coauthor fields).

### Added in T3.6

The SKILL.md paragraph after the table names the biomedical-consortium turn [S045 pp. 2–3; S042 p. 7], the BO-for-chemistry turn [S039 p. 1; S067 pp. 2–3] and formulation theory on the side [S088; S078; S046]. The table and the "Latest" paragraph are unchanged; note 06 has a dated update section.

**Fix pass**: that sentence left SKILL.md, which now points here; it changed no advice, and its last clause read an interpretation as fact. As it stood: *The full texts keep these eras and sharpen two turns: a biomedical consortium, 2014-2018 [S045 pp. 2–3; S042 p. 7], and BO for chemistry with BASF from 2022, then graphs [S039 p. 1; S067 pp. 2–3]; formulation theory stayed on the side [S088; S078; S046].* A reading the cards support: formulation theory continued alongside the other lines, in P-split 2021-2026 [S040; S013; S046] and Lasserre 2019-2023 [S088; S078] (turn 6 above).

### Before T3.6 (moved verbatim)

| Period | Direction | Trigger | Representative work |
|---|---|---|---|
| 2007-2012, Princeton | Pooling relaxations; a public global solver | Advisor's intuition and 2008 demand [06 T1, T2] | doi:10.1016/j.compchemeng.2011.01.026 |
| 2012-2017, Imperial | ANTIGONE; heat recovery, symmetry, structure detection | Move to the UK; first students [06 T3-T5] | doi:10.1007/s10898-014-0166-2 |
| 2017-2022, EPSRC fellowship | Python/Pyomo tools, uncertainty, learning inside solvers (dropped), trained models | Fellowship; BASF seed [06 T6-T8] | doi:10.1007/s11590-019-01396-y |
| 2021-2026, BASF/RAEng chair | OMLT, intermediate formulations, BO over trees and graphs | Industrial partner; ML venues [06 T8-T10] | arXiv:2202.02414; doi:10.1007/s10107-025-02232-1 |

Her constant: "So all I've been doing here at Imperial uh is basically figuring out how to relax better." (T8 [05:37], ASR). Her variable: domains, "very opportunistic".

### Before T3.7 (moved verbatim)

Condensed in SKILL.md on 2026-11-19 (stage T3.7, tighten). The SKILL.md text as it stood before this pass, word for word:

*Research Trajectory, Latest:*

2025-10-10 to 2026-10-10 [06 §7]: P-split in *Math. Program.* 218; BoGrape (BO over graphs, ICLR 2026); Catechol benchmark (NeurIPS 2025); preprints arXiv:2605.05382 (meta-learning BO with BASF), arXiv:2610.03647; SIAM OP26 plenary on optimising over graphs scheduled (delivery not confirmed). No new MINLP solver or formulation paper; OMLT upkeep sits with collaborators. Group: 3 postdocs, 1 PhD student.

<a id="inner-tensions"></a>

## Inner tensions

**Added in T3.6**:
- *Count every second vs the accounting used*: set-up time counted in 2023 (timings with and without the authors' construction code [S078 pp. 13–14]; timings including model building [S071 p. 13]); OBBT bound time not included in the 2026 journal table [S046 p. 25]; 50 runs per cell over model and solver seeds in 2023 [S051 pp. 9–10].
- *Detect vs exploit* (new): the detection line stops at detection [S120 p. 19; S091 pp. 7–10; S068 p. 11; S076 p. 5]; gains measured where her code exploited the structure [S024 pp. 24–29; S072 pp. 19–21]; detection cost measured in GALINI [S087 p. 4]. No text states why the detection line stopped (08 §11).

**Before T3.6 (moved verbatim)**:

Kept as tensions, not resolved.

- **Proofs "boring" vs steady theory.** "just a convergence proof or something to just work ... probably you got to find somebody else because it's boring and I'm not interested." (T8 [30:35], ASR) — against the P-split hierarchy, the 2018 complexity paper, and "i think the laser [= Lasserre] hierarchy is the the coolest thing ever" (T3 [00:47], ASR). Inferred reading: she rejects routine component proofs, not structural theory.
- **Love parameters vs dislike them.** The "Love Parameters" talk title — against "I don't like to introduce parameters" (T11 [29:40], ASR) and Floudas's push to "eliminate the computational dependence on parameters" (W1).
- **Opportunism vs one spine.** "very opportunistic", "pub buddies" — against "figuring out how to relax better" and a planned 2017 grant programme. Inferred: method constant, domains opportunistic.
- **Count every second vs the accounting used.** Timings including building (T3); permuted-model runs (Dagstuhl, joint) — against NeurIPS 2021: OBBT time excluded, single runs, an anomaly called "variability" [03 PE-36, C2].
- **Release and community vs dormant tools.** "build an international user community" (W11) — against GALINI (no code commits since 2022-07-14, general paper a preprint), ANTIGONE frozen at 1.1, no video after 2024-11-04.
- **Champion of piecewise relaxations vs shipping them off**; builder of general solvers vs special-purpose APOGEE beating her generic code and GALINI published only as the pooling version [01 §1.9; 03 PE-33].
- One line each: "Autonomous research machines" (talk title) vs "I personally would not want everything automated" (T10 [51:59], ASR); industry gives little "jumping forward" (T8 [45:03], ASR) vs press quotes on industrial impact; depth (one spine, an eight-year pooling question) vs pivot (ANTIGONE and six lines dropped silently) [06 §4, §5].

**Before T3.7 (moved verbatim)**:

Condensed in SKILL.md on 2026-11-19 (stage T3.7, tighten). The SKILL.md text as it stood before this pass, word for word:

*Proofs "boring" vs steady theory:*

- **Proofs "boring" vs steady theory.** "just a convergence proof or something to just work ... probably you got to find somebody else because it's boring and I'm not interested." (T8 [30:35], ASR) — against the P-split hierarchy, the 2018 complexity paper, and "i think the laser [= Lasserre] hierarchy is the the coolest thing ever" (T3 [00:47], ASR). Inferred reading: she rejects routine component proofs, not structural theory.

*Count every second vs the accounting used:*

- **Count every second vs the accounting used.** Timings including building (T3); permuted-model runs (Dagstuhl, joint) — against NeurIPS 2021: OBBT time excluded, single runs, an anomaly called "variability" [03 PE-36, C2]. Later: set-up time counted in 2023 [S078 pp. 13–14], OBBT time excluded in 2026 [S046 p. 25].

*One line each (three more tensions):*

- One line each: "Autonomous research machines" (talk title) vs "I personally would not want everything automated" (T10 [51:59], ASR); industry gives little "jumping forward" (T8 [45:03], ASR) vs press quotes on industrial impact; depth (one spine, an eight-year pooling question) vs pivot (ANTIGONE and six lines dropped silently) [06 §4, §5].

<a id="honest-boundary"></a>

## Honest Boundary

### Coverage (08 §1, copied)

| Item | Count | Source |
|---|---|---|
| Scholar rows / distinct works indexed | 155 / 147 | 07 coverage row (`team_status.py --coverage`) |
| Open full text on disk | 104 | 07 coverage row |
| Card entries / works with a card | 146 / 145 | digests |
| Read in full | 77 works | digests |
| Read in part | 23 works (22 supplement short cards; one MEng report read at chapter level, S100) | digests |
| Abstract only | 27 works | digests |
| Metadata only | 17 works | digests |
| Unreadable | 1 work: the text file of [S116] has headings only. One more entry, [S138] in s04, held the text of the 2020 journal paper S069; its abstract card in a2-02 counts | digests |
| Indexed rows without a card | 2 talks with Role skip (S105, S133) | INDEX.md |
| INDEX Read column after `mark_read_from_cards.py` | carded 77, skimmed 23, abstract 27, metadata 17, unreadable 1, — 2 | script output, 2026-11-19 |

Distinct works per five-year period (best card per id; read in full or in part in brackets): 2005-09 5 [0], 2010-14 30 [15], 2015-19 52 [36], 2020-24 41 [35], 2025-26 17 [14].

Version caveat for every page below: most texts are author preprints or arXiv versions, not typeset journal versions (batch page-mapping notes of c01, c02, c08, c11, c16). For example the journal P-split paper was read as arXiv v3 [S046], the gradient-boosted-tree paper as arXiv v3 [S020], ENTMOOT as arXiv v3 [S023], the CPAIOR paper as arXiv v1 [S040] and the GALINI pooling paper as arXiv v1 [S072].

### Open gaps (08 §11, copied)

- **Abstract only**: the 2009-2012 pooling, gas-lift and crude-oil papers [S007; S008; S016; S018; S022; S027]; GloMIQO 2 [S026]; the αBB generalisation [S036]; the 2016 pooling-detector paper that is the source of SKILL.md Method 1 step 7 [S064; D001]; the 2021 PSE perspective [S002]; robust pooling and ROmodel conference versions [S118; H001]; conference abstracts [S084; S104; S127; S136; S138].
- **Text on disk but not read in full**: the 315-page PhD thesis, carded from its abstract [S092]; two one-page minlp.org problem statements [S150; S151]; the ESCAPE-28 approximation-algorithms paper, whose file held the journal version [S138].
- **Unreadable**: [S116] needs OCR or a new extraction.
- **Metadata only**: 17 works, among them the GloMIQO 2.2 test-suite report [S102], process synthesis [S019], 2009-2010 proceedings papers on pooling and piecewise approximation [S124; S125; S153], the PSE 2018 design-of-experiments paper [S074], PDE-constrained MINLP [S107] and biomedical meeting abstracts [S111; S112; S089; S101; S122].
- **Versions**: journal pagination is not available for most papers (§1); no card compares a preprint with its published version.
- **Authorship shares**: her individual role is stated only where a contribution statement exists [S091 p. 10; S066 p. 12; S071 p. 13; S082 p. 35; S043 p. 15]; section authorship of the reviews is not stated [S003; S015]; company voice in [S044].
- **Partial reads**: 23 works were read in part; for example the approximation proofs [S079; S052] and most appendix proofs of [S061] were not read.
- **Reasons for turns**: no text states why she left C++ solver development, why the detection line stopped at detection, or why the general GALINI paper stayed a preprint; the cards record dates only (§8).
- **SKILL.md items no card touches**: U1 ("fail fast"), U3, U4, U6, U9; the review exchanges behind H5 and the NeurIPS 2021 "variability" remark.

### Added in T3.6

- Coverage bullet and the first-activation disclaimer use this member's row of `team_status.py --coverage` (2026-11-19): 155 Scholar rows, 147 distinct works indexed, 104 open full text, 77 read in full, 23 in part, 27 abstract only, 18 metadata only including one unreadable, 2 skipped, 222 quotes verified.
- "Not read" now lists only works without a full-text card (08 §11); the four works read since 2026-10-10 are in [Corrections](#corrections).
- U2 resolved into Heuristic 11; U5, U7, U8 annotated from the cards; the reason the detection line stopped added to the unstated reasons. Items no card touches: U1, U3, U4, U6, U9 (08 §11).

### Fix pass (2026-11-19)

- U2 left the "Claimed but unverified" list, whose items the protected Activation Rules forbid presenting as her methods; a **Resolved** line after the list says it is Heuristic 11 and that the rule does not apply to it. The T3.6 entry read: *U2 "generate the computationally inexpensive cuts first" (W9 only) — resolved: practised in eleven works, now Heuristic 11 [08 §5]*.
- U8 now carries its annotation in SKILL.md: partly verified, class-specific ranges, no selection rule [S046 pp. 22–25] (the T3.6 pass had reported this annotation without writing it).
- Corrections from the full texts: the roundtable line (*the protected Activation Rules still say "no paper cards yet"; 145 works now have cards, citable in a brief's evidence field*) moved into the Roundtable Card as a citing rule; the Method 1 line is corrected (step 6 missing; step 5 only for SUSPECT [S068 pp. 10–11]); the "Now read" line names the six-page conference-format version of Misener & Biegler 2023 [S015].

### Before T3.6 (moved verbatim)

This skill is distilled from public information and has these limits:

- **Tacit gaps**: how she spots which hidden structure is worth detecting, picks the extremes and the knob, decides a component should be off by default; one-to-one meetings undocumented.
- **Stated layer**: mostly YouTube ASR; the BCS Needham podcast (T9) is low-grade local ASR with inferred speaker attribution.
- **Claimed but unverified** (never methods):
  - U1 "fail fast" in primal heuristics (T4/W14 only; unlinked to the student's "aim high but fail fast");
  - U2 "generate the computationally inexpensive cuts first" (W9 only);
  - U3 left solver development because industrial teams (FICO Xpress) now lead it — **single-source, low-grade ASR**;
  - U4 "would not want everything automated" — no practice trace;
  - U5 practical rules for combining SDP and RLT cuts (2015 open problem) — NN-scored SDP-cut preprint never published;
  - U6 GALINI user community, "We have achieved what we wrote in the grant proposal" — general paper (Ceccon, Baltean-Lugojan, Bynum, Li, Misener, 2021) a preprint, code dormant;
  - U7 permuted-model experiments as standard (Dagstuhl, joint) — not followed in NeurIPS 2021;
  - U8 one parameter setting "consistently stays good" — partly verified, no selection rule;
  - U9 videos "for every research paper" — lapsed after 2024-11-04.
- **Unstated reasons**: leaving ANTIGONE/C++; the unpublished general-GALINI and SDP-cut papers; the P-split delay; the PhD cohort falling from 7-8 to 1.
- **Era and resources**: PhD on one workstation with donated licences; later eras assume EPSRC developer money, BASF studentships and Sandia co-maintainers (Method 3's toolkit side does not transfer to a lone researcher).
- **Field boundary**: not her voice on convex-MINLP decomposition theory, worst-case theory, copositive/SDP theory or non-expert solver defaults; BO for chemistry is outside the team field.
- **Integrity record**: no statement against misconduct found; no errata or retractions on 151 OpenAlex works or 105 Crossref records [03 PE-35].
- **Not read**: her PhD thesis; the published P-split, NeurIPS 2021, GloMIQO 2 and Misener & Biegler 2023 (doi:10.1016/j.compchemeng.2023.108411) texts; Castro, Liao & Liang 2022; NeurIPS 2022-24 and ICLR 2026 review threads (blocked).
- **Research date**: 2026-10-10. Misener is active (new preprints in 2026); later work is not covered. Update this skill periodically, at least yearly.

<a id="corrections"></a>

## Corrections from the full texts

### Claims of SKILL.md that the full texts contradict or correct (08 §3.3, copied)

| SKILL.md claim | What the full texts show | Proposed change |
|---|---|---|
| Honest Boundary, "Not read": the published P-split, NeurIPS 2021, GloMIQO 2 and Misener & Biegler 2023 texts; Method 2 Limitations: "Full texts of P-split and NeurIPS 2021 not read"; Signature Work P-split: "(full texts not read)" | Read: the journal P-split paper as arXiv v3 [S046], the CPAIOR paper as arXiv v1 [S040], NeurIPS 2021 as arXiv v2 [S013], Misener & Biegler 2023 in a six-page conference format [S015]. Still abstract-only: GloMIQO 2 [S026]; the PhD thesis, whose 315-page text is on disk but was carded from its abstract [S092] | Move the four works out of "Not read"; keep GloMIQO 2 and the thesis there |
| Method 2 Limitations: choosing N has no theory; U8 | Robustness claimed [S040 p. 12]; best P varies by class, two to four variables per split perform well on clustering and P_ball (ReLU nets: P = 2 or 4 splits [S046 pp. 23, 25]), no rule [S046 pp. 22-23, 26]; N problem-dependent [S013 p. 8]; choice left open [S078 p. 20] | Keep the no-rule limitation; add the published practical range |
| Method 2 step 5: random partitions and a deliberately weaker variant as controls | In the NeurIPS paper [S013 p. 7], not in the CPAIOR and journal P-split papers [S040 p. 11; S046 p. 22] | Mark the controls as practised in one of the three texts |
| Method 2 Evidence: "N = 2/4/8 ablations" (MP 2012) | Swept on packing only; N = 4 for pooling inherited [S011 p. 17] | Scope the citation |
| Method 3 step 4: a penalty on distance from a PCA subspace | The PCA penalty is the tree paper's, with its stated failure on clustered data [S020 pp. 17, 26]; other devices elsewhere [S023 p. 10; S051 pp. 8, 25; S071 pp. 3-4; S015 p. 1] | Name the family of near-data devices |
| Signature Work, trained models: "v1's 'risk control' framing left the title by v3" | The v3 body still speaks of risk [S020 pp. 1, 5]; the 2018 seminar abstract still has risk control in its title [S119 p. 17] | Say it left the title, not the text |
| Method 4 step 2: cumulative ablation (cites MP 2012); Signature Work GloMIQO | The ablation is in MP 2012 [S011 pp. 17-19] and GALINI [S087 p. 16]; GloMIQO and ANTIGONE have none [S004 pp. 8, 24-25; S001 pp. 17-18] | Note it under step 2 |
| Method 5 one line: "a script re-checking every answer any solver returns"; Practice: "every solver paper since 2012" | Perl re-check described in the 2013-2014 solver papers [S004 p. 19; S001 pp. 10-11; S032 p. 18], not in the GALINI papers [S087 pp. 16-17; S072 pp. 16-21] | Date the re-check; scope as in §3.2 |
| Method 5 Say–do lapse (NeurIPS 2021: OBBT time excluded, single runs) and Inner Tension "Count every second vs the accounting used" | Single runs and unstated OBBT accounting confirmed from the full text [S013 pp. 9, 16]; OBBT time again not included in 2026 [S046 p. 25]; kept in 2023 [S078 pp. 13-14; S071 p. 13; S051 pp. 9-10]. The "variability" remark comes from the review thread, which no card covers | Add the 2023 and 2026 data points |
| Honest Boundary U2: "generate the computationally inexpensive cuts first" claimed, unverified | Practised in eleven works read in full or in part, 2010-2024 (§5, H11) | Remove from the unverified list |
| Honest Boundary U5: the NN-scored SDP-cut preprint never published | The 2019 preprint is now read: an n-dimensional family with heuristic guidelines, evidence at the root cut loop only, "There is no advantage for using our proposed sparse cuts for fully-dense instances." [S021 pp. 26-27, 29, 31-32]; the 2018 abstract describes integration into ANTIGONE [S136] | Keep U5 (no journal version in the cards); add what the preprint shows |
| Honest Boundary U7: permuted-model experiments as standard (joint) | Joint statement confirmed, "the need to incorporate experimentation on permuted models as has become standard in the MIP community;" [S119 p. 22]; no repeated runs in 2021 [S013 p. 16]; 50 runs over model and solver seeds in 2023 [S051 pp. 9-10] | Partly followed from 2023 |
| Heuristic 6: "One documented instance" | Three [S049 pp. 2, 32; S024 p. 16; S069 p. 11] | Drop the qualifier; see the H4/H6 merge (§5) |
| Heuristic 10: "Executable only in outline" | Steps practised in eleven works (§5) | Make it executable |
| Stages without a method: "Paper drafting and revision ... No source on how she writes" | Review and position papers share a structure: a component map or taxonomy with excluded cells, closing with numbered open questions [S003 pp. 12, 26, 45-55; S014 pp. 2, 7-18; S069 pp. 22-23; S028 pp. 14-17; S145 p. 3] | Narrow to research articles; point reviews to §7.4 WM2 |
| Stages without a method: supervision mechanics undocumented | Two industrial lines began as MEng projects she supervised: LMTD convexity, presented at EUROPT and ISMP 2015 and then published [S100 p. 13; S024 p. 15], and Royal Mail scheduling, run with the partner's data science group and cited by the group paper [S117 p. 3; S135 p. 20] | Add one line of evidence; still no method |
| Activation Rules (roundtable): "cite research notes as [0N item] (no paper cards yet)" | 145 works now have cards (07) | Allow card citations |
| Method 1 Limitations: missed convexity (from a critic) | Her 2014 text names the gap itself [S001 pp. 8, 14] | Add the self-report |

### Where each correction landed in SKILL.md (2026-11-19)

1. "Not read" (Honest Boundary), Method 2 limitations and the P-split anatomy: the four works moved out of "Not read" [S046; S040; S013; S015]; GloMIQO 2 [S026] and the thesis [S092] stay.
2. Method 2 Limitations and U8: the practical ranges added, scoped by class (2-4 variables per split on clustering and P_ball; P = 2 or 4 splits on ReLU nets) [S046 pp. 22–25; S013 p. 8]; the no-rule limitation kept. (In T3.6 a single unscoped range went into a variant bullet only; the fix pass moved it here.)
3. Method 2 step 5: the controls cited to the one text that has them [S013 p. 7]; a variant bullet records the two that do not [S040 p. 11; S046 p. 22].
4. Method 2 evidence: "N = 2/4/8 ablations" scoped to packing [S011 p. 17] (variant bullet).
5. Method 3 step 4: the near-data family named (D5) [S020 pp. 17, 26; S023 p. 10; S051 p. 8].
6. Trained-models anatomy: the framing left the title by v3, not the text [S020 pp. 1, 5].
7. Method 4 step 2 and the GloMIQO anatomy: the ablation located in MP 2012 and GALINI [S011 pp. 17–19; S087 p. 16] (variant bullet).
8. Method 5 Practice and one line: the re-check dated to 2013-2014 [S004 p. 19; S001 pp. 10–11; S032 p. 18] (variant bullet).
9. Method 5 say–do and Inner Tensions: the 2023 and 2026 data points [S078 pp. 13–14; S046 p. 25].
10. U2 → Heuristic 11; U5 annotated [S021 pp. 26, 31–32]; U7 annotated [S051 pp. 9–10].
11. Heuristic 6: three instances; Heuristic 10: executable.
12. Stages table: reviews' layout (WM2) and the MEng seeds.
13. Activation Rules, roundtable line "(no paper cards yet)": **not edited** (protected section; only the first-activation disclaimer may change in this step). The line predates the cards: 145 works now have cards (07), so a roundtable brief's evidence field may cite `[ruth-misener card S011 p. 17]`. Fix pass: the citing rule now sits in the Roundtable Card, which a convened member must read, and says it supersedes the old wording; changing the protected line itself is left to the operator. After T3.6 (2026-11-19) the operator rewrote the line to cite paper cards first, dropped the Roundtable Card's "supersedes" sentence, and changed "U1-U9" in the method-label line to "U1 or U3-U9" (U2 is now Heuristic 11).
14. Method 1 Limitations: the self-reported convexity gap [S001 pp. 8, 14].
15. Fix pass (2026-11-19, after three read-only reviews): Method 1's detection-line bullet (step 6 missing in all four papers, step 5 done for SUSPECT [S068 p. 10]); Method 5 step 6's citation [S001 pp. 10–11; S004 p. 19]; the LMTD minimum evidence (two of three instances comparable [S024 pp. 24, 29]); Heuristic 2's Royal Mail case (no public stand-in [S135 p. 20]); Method 4's ✗ bullet split; Method 5's contradiction count (5, plus one reading note); Misener & Biegler 2023 read in a six-page conference-format version [S015]. Each is detailed under its section's **Fix pass** line.
16. Tighten (T3.7) and its fix round (2026-11-19): items 11 and 12 now land partly in this ledger. Heuristic 6's instances are in [Heuristic 4](#heuristic-4) (SKILL.md keeps [S049 pp. 2, 32] in the APOGEE anatomy and [S024 p. 16] in its corrections list); the stages table's WM2 cards and MEng seeds are in [Workflows and routing](#workflows). Item 15's Method 1 bullet keeps two of its four cards in SKILL.md (see [Method 1](#method-1)).

### Promotions considered (08 §4, copied)

**No promotion this round.** The skill stays at five core methods. Eight clusters reached three or more distinct cards read in full or in part; each fails at least one of the four checks.

| Cluster (merged by meaning) | Cards read in full/part | 1 Recurrence | 2 Say–do | 3 Executable, non-standard | 4 Exclusivity | Result |
|---|---|---|---|---|---|---|
| Spend the expensive relaxation only where a cheap one has failed | S025, S011, S004, S020, S088, S005, S021, S087, S050, S024, S119 (11) | ✅ 2010-2024, seven coauthor lines (Floudas, Mistry, Baltean-Lugojan, Campos, Lomuscio, Ceccon, Hojny) | ✅ her MINLP project page (W9) says the group generates the computationally inexpensive cuts first [02]; [S021 p. 2]; [S136] | ✅ | ✗ cheap-first separation is common solver engineering; her learned RLT rule credits the a priori literature [S004 p. 14] | Heuristic H11 (§5) |
| Prove the boundary of your own construction (ceilings, classes where a cut cannot help, hardness frontiers, non-containment) | S011, S040, S046, S049, S061, S078, S120, S135, S017 (9) | ✅ 2012-2026 | ⚠ statements of scope inside papers [S046 p. 26; S049 p. 32], no stated method in note 02 | ✅ | ✗ negative results about relaxations are the core output of other MINLP Team lenses (Dey, Burer; team.json hints); in her texts they support a positive construction [S046 pp. 12-13; S011 p. 9] | H4 extension (§5) |
| Import one device from a neighbouring community | S009, S155, S058, S061, S069, S135, S079, S017, S073, S005, S059 (11) | ✅ 2011-2024 | ✅ [02 C10] (6 stated sources); [S069 p. 2; S058 p. 1] | ✅ | ✗ the imported devices are presented as the neighbours' [S155 p. 3; S009 pp. 3, 19; S069 pp. 3-4] | Heuristic-eligible; written into Workflow B step 4 (§5) |
| Keep known structure exact; model only the unknown part | S095, S034, S075, S066, S059, S086, S115, S015 (8) | ✅ 2017-2025 | ✅ Taste mark 3 (T2) and [S015 p. 1] | ✅ | ✗ rival surrogate and grey-box tools are listed alongside [S015 p. 4] | M1 variant (§3.1) |
| Choose the model for its encodability | S067, S047, S071, S015, S028 (5) | ✅ 2022-2026 | ✅ [S067 p. 20; S015 p. 1] | ✅ | ✗ rival algebraic-surrogate tools (ALAMO) are listed [S015 p. 4] | M3 variant (§3.1) |
| Prove the encoding exact; count what symmetry breaking removes | S051, S038, S093, S128, S067 (5) | ⚠ one research line, 2023-2026 | ✅ "There are often multiple ways to encode a combinatorial problem, but insufficient constraints result in an unnecessarily large search space with symmetric solutions, while excessive constraints may cutoff feasible solutions from the search space." [S093 p. 4; S128 p. 4] | ✅ | ✗ exactness proofs are standard in MIP modelling [S128 pp. 2-6] | M1 step 5 and M3 step 2 evidence |
| Audit the inherited model or instance | S025, S152, S024, S100, S049, S080 (6) | ✅ 2010-2021 | ✗ no stated rule | ✅ | ⚠ | M5 step 1b (§2) |
| Make uncertainty explicit with checks | S045, S085, S042, S060, S048, S033, S055, S057, S066, S052, S079 (11) | ✅ 2014-2023 | ✅ H10's stated quote (Q1) | ✅ | ✗ robust optimisation is shared practice; her robust counterparts reuse published reformulations [S085 p. 5; S033 p. 8] | H10 upgrade (§5) |

Why no merger or replacement: each cluster is explained by an existing method once that method's scope or steps are updated (§2, §3.1), so a sixth method would duplicate one of the five. The closest call, the cheap-screen cluster, explains a solver-design habit that M4 (a judging habit) does not, but it fails exclusivity, so it enters as a heuristic.

### Rejected updates (08 §10, copied)

1. **A new heuristic for importing from neighbouring communities** (S009, S155, S058, S061, S069 and others): it duplicates Workflow B step 4, which already carries the stated claim [02 C10]; written there (§5).
2. **A method or heuristic for exact encodings with correctness proofs** (S051, S093, S128, S067, S038): standard in MIP modelling; absorbed as M1 step 5 and M3 step 2 evidence.
3. **A heuristic for auditing inherited models** (S025, S100, S080, S152, S024, S049): no stated rule, and the move sits inside M5's auditor scope; proposed as M5 step 1b.
4. **A method for grey-box modelling** (S095, S034, S075, S066, S059, S086, S115): an M1 variant; M1 explains it once its scope reads *detected, or kept exact*.
5. ***Architecture as the contribution*** (S001, S032, S145, S143, S072): restates Taste mark 5 and Workflow B step 5.
6. ***Concede the specialised tool's turf*** and ***portfolio instead of default*** (S006, S029, S050): H7, M3 step 5 and M4 step 7 already cover them.
7. **Matched controls, tie counting, primal/dual attribution, slicing by class as heuristics**: protocol detail for Workflow C; kept in §7.3.
8. **Retrospective pool-based BO and datasets as contributions** (S081, S082, S097): BO-venue evaluation outside the team field; §7.3 and an H2 variant.
9. **A review-structure heuristic** (S003, S014, S028, S069, S145): scoped to reviews; proposed as a note in the stages table rather than a numbered heuristic, to keep the list at ten.
10. **Approximation-error accounting as a heuristic** (S012, S024, S100, S025, S036): a relaxation-design technique that changes no decision the skill makes; kept in §7.1-7.2.
11. **Single-card candidates** in §6 marked pool: below the threshold of three works.
12. **Consortium practices where she is a middle author** (blinded validation, confounder simulation, the lab-wide loop; S043, S037, S054): not her method; the blinded experiment is credited to a coauthor [S043 p. 15].
13. **Reading-note inconsistencies inside single works**: not findings about the researcher or coauthors; not carried into SKILL.md (one neutral lesson in §7.4).

### How to Use before T3.6 (moved verbatim)

**Strengths** (stages with evidence): problem choice; relaxation and formulation design for nonconvex MINLP / MIQCQP (structure detection, edge-concave and piecewise relaxations, formulations between big-M and the hull); optimisation over trained models and the global acquisition step of Bayesian optimisation (BO); experiment design; judging results and solver defaults; release and reviews.

**Weak spots**: the stages in Stage Workflows' last table; the Field boundary (Honest Boundary).

**Domain fit**: algebraic MINLP / MIQCQP models with recurring structure (pooling, process networks, disjunctions, embedded ML surrogates). Her post-2021 main line, BO for chemistry, is outside this team's field; answer it only where it touches MINLP.

**Citations**: `[02 L1.4]` = note 02, item L1.4: [01 publications](01-publications.md), [02 methodology](02-methodology.md), [03 process evidence](03-process-evidence.md), [04 mentorship](04-mentorship.md), [05 peer critique](05-peer-critique.md), [06 trajectory](06-trajectory.md). T1-T11 = her recorded talks, W1-W14 = her written statements (list in note 02 §A). **Stated** = she said or wrote it; **practice** = the record shows it; **observed** = others recorded it. Spoken quotes are YouTube auto-captions (ASR). Papers are multi-author: "she" often means "her group, with her as last author".

---

<a id="sources"></a>

## Sources moved out of SKILL.md

SKILL.md's "Papers (primary)" list was replaced by a pointer on 2026-11-19; each paper there is cited inline with its DOI or arXiv id or by its card. The list as it stood (moved verbatim):

- Pooling: Gounaris, Misener, Floudas, Ind. Eng. Chem. Res. 2009, doi:10.1021/ie8016048; APOGEE, Comput. Chem. Eng. 2011, doi:10.1016/j.compchemeng.2011.01.026; Baltean-Lugojan, Misener, J. Global Optim. 2018, doi:10.1007/s10898-017-0577-y
- Solvers: Misener, Floudas, MIQCQP relaxations, Math. Program. 2012, doi:10.1007/s10107-012-0555-6; GloMIQO, J. Global Optim. 2013, doi:10.1007/s10898-012-9874-7; GloMIQO 2, Optim. Methods Softw. 2015, doi:10.1080/10556788.2014.916287; ANTIGONE, J. Global Optim. 2014, doi:10.1007/s10898-014-0166-2; GALINI pooling, Comput. Chem. Eng. 2022, doi:10.1016/j.compchemeng.2022.107660
- Structure detection: AIChE J. 2016, doi:10.1002/aic.15308; Comput. Chem. Eng. 2016, doi:10.1016/j.compchemeng.2016.07.001; Processes 2019, doi:10.3390/pr7110838 (arXiv:1712.05222); SUSPECT, Optim. Lett. 2020, doi:10.1007/s11590-019-01396-y
- Trained models: gradient-boosted trees, INFORMS J. Comput. 2021, doi:10.1287/ijoc.2020.0993 (arXiv:1803.00952); ENTMOOT, doi:10.1016/j.compchemeng.2021.107343; OMLT, JMLR 2022, arXiv:2202.02414
- Intermediate formulations: Kronqvist, Misener, Tsay, CPAIOR 2021, doi:10.1007/978-3-030-78230-6_19, and Math. Program. 2026, doi:10.1007/s10107-025-02232-1; NeurIPS 2021, arXiv:2102.04373; partial Lasserre, Optim. Eng. 2023, doi:10.1007/s11081-022-09763-y
- BO and surrogate line: arXiv:2207.00879; arXiv:2503.05574; arXiv:2202.00060; arXiv:2402.08406; arXiv:2305.09420; doi:10.1016/j.compchemeng.2023.108194; doi:10.1021/acs.iecr.9b01772; doi:10.1007/s10107-021-01762-8; recent arXiv:2605.05382, arXiv:2610.03647
- Furini et al., "QPLIB: a library of quadratic programming instances", Math. Program. Comput. 2019, doi:10.1007/s12532-018-0147-4

The Misener & Biegler 2023 entry under "Stated methodology (primary)" read "(abstract only)" before; it is now read in a six-page conference-format version, most likely the FOCAPO/CPC-format text rather than the journal article [S015].

<a id="card-key"></a>

## Card key

Every card id cited in SKILL.md, this ledger or the technique catalog: year, title (as in `07-paper-cards.md`), read level and batch file. Abstract-, metadata-level and unreadable cards are cited by id only.

| Card | Year | Title | Read level | Batch |
|---|---|---|---|---|
| D001 | 2016 | Using functional programming to recognize named structure in an optimization problem: Application to pooling | abstract | a2-01 |
| H001 | 2021 | ROmodel: A Python Robust Optimization Modeling Toolbox | abstract | a2-02 |
| H002 | 2014 | Optimisation under uncertainty for a bioreactor that produces red blood cells | full | s01 |
| S001 | 2014 | ANTIGONE: algorithms for continuous/integer global optimization of nonlinear equations | full | c02 |
| S002 | 2021 | Process systems engineering–the generation next? | abstract | a2-02 |
| S003 | 2016 | Global optimization advances in mixed-integer nonlinear programming, MINLP, and constrained derivative-free optimization, CDFO | full | c04 |
| S004 | 2013 | GloMIQO: Global mixed-integer quadratic optimizer | full | c02 |
| S005 | 2020 | Efficient verification of relu-based neural networks via dependency analysis | full | c07 |
| S006 | 2022 | OMLT: Optimization & machine learning toolkit | full | c09 |
| S007 | 2009 | Advances for the pooling problem: Modeling, global optimization, and computational studies | abstract | a2-01 |
| S008 | 2009 | Computational comparison of piecewise− linear relaxations for pooling problems | abstract | a2-01 |
| S009 | 2011 | APOGEE: Global optimization of standard, generalized, and extended pooling problems via linear and logarithmic partitioning schemes | full | c01 |
| S010 | 2019 | QPLIB: a library of quadratic programming instances | full | c06 |
| S011 | 2012 | Global optimization of mixed-integer quadratically-constrained quadratic programs (MIQCQP) through piecewise-linear and edge-concave relaxations | full | c02 |
| S012 | 2010 | Piecewise-linear approximations of multidimensional functions | full | c01 |
| S013 | 2021 | Partition-based formulations for mixed-integer optimization of trained ReLU neural networks | full | c08 |
| S014 | 2022 | Maximizing information from chemical engineering data sets: Applications to machine learning | full | c09 |
| S015 | 2023 | Formulating data-driven surrogate models for process optimization | full | c11 |
| S016 | 2012 | Continuous‐time modeling and global optimization approach for scheduling of crude oil operations | abstract | a2-01 |
| S017 | 2019 | Argumentation for explainable scheduling | full | c07 |
| S018 | 2010 | Global optimization of large-scale generalized pooling problems: quadratically constrained MINLP models | abstract | a2-01 |
| S019 | 2012 | Global optimization of a MINLP process synthesis model for thermochemical based conversion of hybrid coal, biomass, and natural gas to liquid fuels | metadata | a2-01 |
| S020 | 2021 | Mixed-integer convex nonlinear optimization with gradient-boosted trees embedded | full | c08 |
| S021 | 2019 | Scoring positive semidefinite cutting planes for quadratic optimization via trained neural networks | full | c07 |
| S022 | 2009 | Global optimization of gas lifting operations: A comparative study of piecewise linear formulations | abstract | a2-01 |
| S023 | 2021 | ENTMOOT: A framework for optimization over ensemble tree models | full | c09 |
| S024 | 2016 | Optimising heat exchanger network synthesis using convexity properties of the logarithmic mean temperature difference | full | c05 |
| S025 | 2010 | Mathematical modeling and global optimization of large-scale extended pooling problems with the (EPA) complex emissions constraints | full | c01 |
| S026 | 2015 | Dynamically generated cutting planes for mixed-integer quadratically constrained quadratic programs and their incorporation into GloMIQO 2 | abstract | a2-01 |
| S027 | 2012 | Scheduling of crude oil operations under demand uncertainty: A robust optimization framework coupled with global optimization | abstract | a2-01 |
| S028 | 2025 | Cross-disciplinary perspectives on the potential for artificial intelligence across chemistry | full | c13 |
| S029 | 2016 | Bayesian optimization with dimension scheduling: Application to biological systems | full | s02 |
| S031 | 2023 | Combining multi-fidelity modelling and asynchronous batch Bayesian Optimization | full | c11 |
| S032 | 2014 | A framework for globally optimizing mixed-integer signomial programs | partial | s01 |
| S033 | 2018 | Data-driven optimization of processes with degrading equipment | partial | s03 |
| S034 | 2019 | Bayesian multiobjective optimisation with mixed analytical and black-box functions: application to tissue engineering | partial | s04 |
| S035 | 2022 | Multi-objective constrained optimization for energy applications via tree ensembles | partial | s06 |
| S036 | 2012 | A Generalization of the Classical αBB Convex Underestimation via Diagonal and Nondiagonal Quadratic Terms | abstract | a2-01 |
| S037 | 2015 | Towards unravelling the kinetics of an acute myeloid leukaemia model system under oxidative and starvation stress: a comparison between two-and three-dimensional cultures | partial | s01 |
| S038 | 2024 | Augmenting optimization-based molecular design with graph neural networks | full | c12 |
| S039 | 2022 | SnAKe: Bayesian optimization with pathwise exploration | full | c10 |
| S040 | 2021 | Between steps: Intermediate relaxations between big-M and convex hull formulations | full | c09 |
| S041 | 2019 | GPdoemd: A Python package for design of experiments for model discrimination | partial | s04 |
| S042 | 2015 | A systematic framework for the design, simulation and optimization of personalized healthcare: making and healing blood | partial | s02 |
| S043 | 2015 | A mathematical model of subpopulation kinetics for the deconvolution of leukaemia heterogeneity | partial | s02 |
| S044 | 2025 | BoFire: Bayesian optimization framework intended for real experiments | full | c13 |
| S045 | 2014 | Global superstructure optimisation of red blood cell production in a parallelised hollow fibre bioreactor | partial | s01 |
| S046 | 2026 | P-split formulations: a class of intermediate formulations between big-M and convex hull for disjunctive constraints | full | c16 |
| S047 | 2022 | Tree ensemble kernels for Bayesian optimization with known constraints over mixed-feature spaces | full | c10 |
| S048 | 2019 | Robust optimization for the pooling problem | full | c07 |
| S049 | 2018 | Piecewise parametric structure in the pooling problem: from sparse strongly-polynomial solutions to NP-hardness | full | c06 |
| S050 | 2024 | Verifying message-passing neural networks via topology-based bounds tightening | full | c12 |
| S051 | 2023 | Optimizing over trained GNNs via symmetry breaking | full | c11 |
| S052 | 2021 | Exact lexicographic scheduling and approximate rescheduling | partial | s06 |
| S053 | 2017 | A quantitative three-dimensional image analysis tool for maximal acquisition of spatial heterogeneity data | full | s02 |
| S054 | 2014 | A framework for the design, modeling and optimization of biomedical systems | full | s01 |
| S055 | 2022 | A robust approach to warped Gaussian process-constrained optimization | full | c10 |
| S056 | 2023 | An optimization approach coupling preprocessing with model regression for enhanced chemometrics | partial | s06 |
| S057 | 2022 | ROmodel: modeling robust optimization problems in Pyomo | full | s06 |
| S058 | 2018 | Satisfiability modulo theories for process systems engineering | full | s03 |
| S059 | 2024 | Transition constrained Bayesian optimization via Markov decision processes | full | c13 |
| S060 | 2018 | Stem cell biomanufacturing under uncertainty: a case study in optimizing red blood cell production | full | s03 |
| S061 | 2018 | Heuristics with performance guarantees for the minimum number of matches problem in heat recovery network design | full | s04 |
| S063 | 2021 | A disjunctive cut strengthening technique for convex MINLP | partial | s06 |
| S064 | 2016 | Using functional programming to recognize named structure in an optimization problem: application to pooling | abstract | a2-01 |
| S065 | 2016 | A personalized framework for dynamic modeling of disease trajectories in chronic lymphocytic leukemia | partial | s02 |
| S066 | 2023 | Probabilistic predictions for partial least squares using bootstrap | full | s07 |
| S067 | 2026 | BoGrape: Bayesian optimization over graphs with shortest-path encoded | full | c16 |
| S068 | 2020 | SUSPECT: MINLP special structure detector for Pyomo | full | c08 |
| S069 | 2020 | Approximation algorithms for process systems engineering | partial | s05 |
| S070 | 2015 | Selecting a differential equation cell cycle model for simulating leukemia treatment | partial | s02 |
| S071 | 2023 | Data augmentation driven by optimization for membrane separation process synthesis | full | s07 |
| S072 | 2022 | Solving the pooling problem at scale with extensible solver GALINI | full | c11 |
| S073 | 2020 | AI-assisted schedule explainer for nurse rostering | full | s05 |
| S074 | 2018 | Design of experiments for model discrimination using Gaussian process surrogate models | metadata | a2-02 |
| S075 | 2018 | Design of Experiments for Model Discrimination Hybridising Analytical and Data-Driven Approaches | full | s04 |
| S076 | 2017 | Detecting symmetry in designing heat exchanger networks | full | s03 |
| S077 | 2024 | Dependence in constrained Bayesian optimization: When do we need it and how does it help? | full | c13 |
| S078 | 2023 | Partial Lasserre relaxation for sparse Max-Cut | full | c12 |
| S079 | 2021 | Approximate and robust bounded job start scheduling for Royal Mail delivery offices | partial | s06 |
| S080 | 2021 | Design of dynamic experiments for black-box model discrimination | partial | s06 |
| S081 | 2025 | BARK: A fully Bayesian tree kernel for black-box optimization | full | c14 |
| S082 | 2025 | Transfer learning Bayesian optimization for competitor DNA molecule design for use in diagnostic assays | full | c14 |
| S083 | 2023 | Practical path-based Bayesian optimization | full | s07 |
| S084 | 2020 | Global optimization with ensemble machine learning models | abstract | a2-02 |
| S085 | 2014 | Robust superstructure optimisation of a bioreactor that produces red blood cells | full | s01 |
| S086 | 2025 | System-aware neural ODE processes for few-shot Bayesian optimization | full | c14 |
| S087 | 2020 | GALINI: An extensible mixed-integer quadratically-constrained optimization solver. | partial | s05 |
| S088 | 2019 | A multilevel analysis of the Lasserre hierarchy | partial | s04 |
| S089 | 2015 | Global Sensitivity Analysis for a Model of B-Cell Chronic Lymphocytic Leukemia Disease Trajectories | metadata | a2-01 |
| S090 | 2025 | Limeade: Let integer molecular encoding aid | full | c15 |
| S091 | 2019 | Symmetry detection for quadratic optimization using binary layered graphs | full | c07 |
| S092 | 2012 | Novel global optimization methods: theoretical and computational studies on pooling problems with environmental constraints | abstract | a2-01 |
| S093 | 2025 | Global optimization of graph acquisition functions for neural architecture search | full | c15 |
| S095 | 2017 | Bayesian multi-objective optimisation of neotissue growth in a perfusion bioreactor set-up | full | s03 |
| S096 | 2014 | Key environmental stress biomarker candidates for the optimisation of chemotherapy treatment of leukaemia | full | s01 |
| S097 | 2025 | The catechol benchmark: Time-series solvent selection data for few-shot machine learning | full | c15 |
| S098 | 2023 | Gaussian processes for monitoring air-quality in Kampala | full | s07 |
| S099 | 2020 | Design of Experiments for Verifying Biomolecular Networks | full | s05 |
| S100 | 2016 | Increasing energy efficiency in industrial plants: Optimising heat exchanger networks | partial | b02 |
| S101 | 2015 | Cell cycle model selection for leukemia and its impact in chemotherapy outcomes | metadata | a2-01 |
| S102 | 2015 | Mixed-Integer Quadratically-Constrained Quadratic Programs: GloMIQO 2.2 Test Suite | metadata | a2-01 |
| S104 | 2025 | Molecular design using graph Bayesian optimization with shortest-path kernels | abstract | a2-02 |
| S107 | 2018 | Algorithms for mixed-integer optimization constrained by partial differential equations | metadata | a2-02 |
| S111 | 2014 | Evolution of an AML model system under oxidative & starvation stress: a comparison between two and three dimensional cultures | metadata | a2-01 |
| S112 | 2014 | Development and experimental validation of a cyclin-based population balance model of the cell cycle in leukemia cell lines | metadata | a2-01 |
| S113 | 2026 | Meta-learning for sample-efficient Bayesian optimisation of fed-batch processes | full | c17 |
| S115 | 2025 | Weighted-Sum of Gaussian Process Latent Variable Models | full | c15 |
| S116 | 2023 | Competitive Amplification Networks enable molecular pattern recognition with PCR | unreadable | s07 |
| S117 | 2019 | A practical analysis of optimisation and recovery under uncertainty | partial | s05 |
| S118 | 2019 | The robust pooling problem | abstract | a2-02 |
| S119 | 2018 | Designing and implementing algorithms for mixedinteger nonlinear optimization | full | c06 |
| S120 | 2017 | Symmetry Detection for Quadratically Constrained Quadratic Programs Using Binary Layered Graphs | full | c05 |
| S122 | 2015 | Development of an ex vivo bone marrow mimicry microenvironment in a novel 3D hollow fibre bioreactor | metadata | a2-01 |
| S123 | 2014 | Mixed-integer nonlinear optimization problems: ANTIGONE 1.0 test suite | partial | s01 |
| S124 | 2010 | Global Optimization and Parametric Analysis of Large-Scale Extended Pooling Problems | metadata | a2-01 |
| S125 | 2009 | Advances in Global Optimization for Standard, Generalized, and Extended Pooling Problems with the (EPA) Complex Emissions Model Constraints | metadata | a2-01 |
| S126 | 2026 | Amortized Structured Stochastic Variational Inference for Gaussian Process Latent Variable Models | full | c17 |
| S127 | 2025 | A Meta-Learning Approach for Few-Shot Bayesian Optimization of Batch Chemical Processes | abstract | a2-02 |
| S128 | 2025 | Beyond adjacency: Graph encoding with reachability and shortest paths | full | c16 |
| S135 | 2019 | Approximating Bounded Job Start Scheduling with Application in Royal Mail Deliveries Under Uncertainty | partial | s05 |
| S136 | 2018 | Online Generation Via Offline Selection of Strong Linear Cuts from a Semidefinite Programming Relaxation | abstract | a2-02 |
| S138 | 2018 | Approximation Algorithms for Process Systems Engineering | abstract; unreadable | a2-02; s04 |
| S143 | 2016 | In memoriam: Christodoulos Achilleus Floudas | full | c05 |
| S145 | 2014 | Deterministic Global optimisation at CPSE: Models, Algorithms, and Software | full | c03 |
| S150 | 2011 | Generalized Pooling Problem | metadata | a2-01 |
| S151 | 2010 | Extended Pooling Problem with the Summer Time (EPA) Complex Emissions Constraints | metadata | a2-01 |
| S152 | 2010 | Global Optimization of Large-Scale Extended and Generalized Pooling Problems: Mixed-Integer Nonlinearly Constrained Models | full | b01 |
| S153 | 2009 | Multidimensional Piecewise-Affine Approximations for Gas Lifting and Pooling Applications | metadata | a2-01 |
| S155 | 2017 | Integrating Mixed-Integer Optimisation and Satisfiability Modulo Theories: Application to Scheduling | full | s03 |
