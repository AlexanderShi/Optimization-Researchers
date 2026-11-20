# Sven Leyffer · Evidence ledger

> Date: 2026-11-19 (stage T3.6, first synthesis round; stage T3.7, tightening, and its review fixes, the same day). The full evidence behind `SKILL.md`. SKILL.md keeps, per item, the strongest statement and cards, a one-line say–do count, at most four variant/correction bullets and a pointer to the matching section here. A section has some of these parts, in this order: **Full-text evidence** (from the paper cards, copied from `08-deep-reading-synthesis.md`, which is traceable to `cards/`; an anatomy section has **Full rows in SKILL.md after T3.6** instead, the table as it stood after T3.6), **Added in T3.6** (what this pass wrote or changed, with card ids), **Review fixes (T3.6)** (what the T3.6 review changed), **Before T3.6 (moved verbatim)** (the SKILL.md item as it stood before this pass, built from web research, so nothing is lost; its `[02 §1.1]`-style citations point to the web-research notes `01-…06-*.md` in this folder), **Before T3.7 (moved verbatim)** and **Review fixes (T3.7)** (both below). Some sections also hold verbatim copies from 08 under headings that name their source (for example **Promotion table (08 §4)**, **Proposal (08 §5, verbatim)**, **08 §3.2, verbatim**) or card detail (**Further detail from the cards**). Stage T3.7 took SKILL.md from 12,613 to 11,487 words (`wc -w`) and added a part to each section whose SKILL.md lines it shortened or moved: **Before T3.7 (moved verbatim)**, those lines as they stood before the pass, with the context they need (the SKILL.md subsection in bold, the Evidence or Steps label, the table header); unchanged lines are not repeated, and the anatomy rows it shortened are the rows given above them under **Full rows in SKILL.md after T3.6**. Its review then put some of that wording back into SKILL.md (11,652 words after the fixes); **Review fixes (T3.7)** says what came back and why, and the copies under **Before T3.7** stay as they were. In moved text, heading lines are shown in bold and relative links are rewritten to resolve from this folder; the text is otherwise unchanged.

**How to read.** `[S012 p. 9]` is paper card S012 in `07-paper-cards.md`, at the `[[page N]]` page of the file read (as listed in `../sources/papers/INDEX.md`). Many core works were read in a report, preprint or arXiv version, not the journal: a version word (`TR`, `arXiv`, `preprint`) marks some, as the card says; others are mostly unmarked here, notably S001, S003, S009, S015, S048 (reports, preprints) and S031, S065, S119, S126, D001 (arXiv); SKILL.md and the review-fix notes mark S126 and D001 as arXiv [08 §1]. Catalog ids: P, D, V (evaluation protocols, named E before the review fix), W. Abstract-, metadata- and unreadable-level cards are cited by id only. Related texts count once: S020 and S013 are the same NA/210 report text; S129 is the preprint of S037; S067 and D001 are two versions of the PIPA counterexample; H014 is the preprint of S121; S165 extends S160; S162 corrects S096 [08 §1]. Most works are coauthored, and from about 2013 on Leyffer is often a middle or last author, so a practice in a team paper is evidence about the team's record [08 §1, §9]. Quotes are copied from cards that copied them verbatim (`verify_card_quotes.py`: 329 found, 0 not found); where the text extraction dropped letters, a quote either keeps the damage, as the cards do, or restores the letters in brackets (`[c]onvergen[c]e`). Cards that record typos or internal inconsistencies of a work are reading notes and are not used here. Named proof devices, design moves, evaluation protocols and writing moves are in `../technique-catalog.md`.

## Contents

- [Taste: marks of good research](#taste-marks)
- [Taste: warning signs of bad research](#taste-warnings)
- [Method 1: Own the instrument: integrate at the iteration level, strip tooling restrictions, expose building blocks](#method-1)
- [Method 2: Base and extension: carry the home NLP toolkit into a new class](#method-2)
- [Method 3: Counterexample discipline: smallest breaking example, hypothesis check, run it, redesign](#method-3)
- [Method 4: The test library as a maintained research instrument](#method-4)
- [Method 5: Calibrated claims on self-built, fairness-stated baselines](#method-5)
- [Method 6: Read the solver's numbers, then fix the formulation before the method](#method-6)
- [Method 7: Certify the notion you claim: grade every method by it, print what is not certified](#method-7)
- [Heuristic 1: Ablate from a plain baseline, one feature at a time](#heuristic-1)
- [Heuristic 2: Prototype up a ladder of tiny classics](#heuristic-2)
- [Heuristic 3: Numbers first, theory second](#heuristic-3)
- [Heuristic 4: A subproblem your method creates can be the next line](#heuristic-4)
- [Heuristic 5: Transfer and combine proofs; state novelty as the gap a known area leaves](#heuristic-5)
- [Heuristic 6: (2026, era-bound) Write the brief yourself; let agents draft and attack](#heuristic-6)
- [Heuristic 7: Let the downstream use choose the upstream research](#heuristic-7)
- [Heuristic 8: Do the brute-force arithmetic first](#heuristic-8)
- [Heuristic 9: When corrected, credit the corrector and change method rather than argue](#heuristic-9)
- [Heuristic 10: Build a new evaluation tool when the standard one cannot answer your question](#heuristic-10)
- [Heuristic 11: Keep the model separate from its discretization and solve coarse to fine](#heuristic-11)
- [Heuristic 12: Show every technique on one tiny computed example; thread one running example through theory, reformulation and code](#heuristic-12)
- [Stage workflows (changes and earlier wording)](#workflows)
- [Research task routing and agentic protocol (earlier wording)](#routing)
- [How to Use and frontmatter (earlier wording)](#how-to-use)
- [Anatomy: Solving mixed integer nonlinear programs by outer approximation (Fletcher and Leyffer, Math. Program. 66, 1994, doi:10.1007/BF01581153)](#anatomy-oa)
- [Anatomy: Integrating SQP and Branch-and-Bound for MINLP (Leyffer, Comput. Optim. Appl. 18(3), 2001, doi:10.1023/A:1011241421041), with FilMINT (doi:10.1287/ijoc.1090.0373) and Minotaur (doi:10.1007/s12532-020-00196-1)](#anatomy-sqp-bb)
- [Anatomy: Nonlinear programming without a penalty function (Fletcher and Leyffer, Math. Program. 91(2), 2002, doi:10.1007/s101070100244)](#anatomy-filter)
- [Anatomy: MPECs solved as NLPs (Fletcher and Leyffer, Optim. Methods Softw. 19(1), 2004, doi:10.1080/10556780410001654241; with Ralph and Scholtes, SIAM J. Optim. 17(1), 2006, doi:10.1137/S1052623402407382; MacMPEC)](#anatomy-mpec)
- [Anatomy: McCormick envelopes in mixed-integer PDE-constrained optimization (Leyffer and Manns, Math. Program. 218, 2025, doi:10.1007/s10107-024-02181-1; Correction doi:10.1007/s10107-026-02330-8)](#anatomy-mccormick)
- [Anatomy: Certified B-stationarity, from the SLPEC filter (2007) to MPECopt (2026)](#anatomy-b-stationarity)
- [Anatomy: Trust regions on integer controls, SLIP (2022) and binary trust-region steepest descent (2023)](#anatomy-slip)
- [Research anti-patterns](#anti-patterns)
- [Research trajectory](#trajectory)
- [Academic lineage and collaboration pattern](#academic-lineage)
- [Inner tensions](#inner-tensions)
- [Roundtable Card](#roundtable-card)
- [Honest boundary](#honest-boundary)
- [Corrections from the full texts](#corrections)
- [Candidate pool (not promoted)](#candidate-pool)
- [Sources: primary papers listed before T3.6](#sources-papers)
- [Sources: students, collaborators and peers](#sources-secondary)
- [Card key](#card-key)

<a id="taste-marks"></a>

## Taste: marks of good research

### Added in T3.6

- **Item 6 (new): It prints its own boundary.** "better heuristics for nonconvex MINLP problems remain an open problem" [S009 p. 11]; the restoration case MPECopt does not treat is named [S126 p. 25]; the a priori lower bound "only improves over trivial bounds when the mesh size is already quite fine and the involved constants can be estimated well" [S096 arXiv p. 32]; also [S055 p. 10; S007 p. 22; S091 p. 3]. Basis: the "print what is not certified" cluster of the Method 7 promotion [08 §4].
- **Card evidence added to items 1-5**: item 1, the NA/182 callback [S009 p. 10] and FilMINT's design philosophy, linearizations treated "in a manner similar to the way cutting planes are treated by a branch-and-cut algorithm for MILP" [S015 p. 18]; item 2, MPECs as NLPs against the received verdict [S020 pp. 1–2; S057 p. 15] and the thermal-insulation paper that fixes the formulation first [S043 pp. 8–9]; item 3, "while the NLP solvers are generally very robust, one still requires a proof such as the one given in Subsection 5.2 to ascertain the quality of the solutions they produce." [S031 p. 18], and Taste 3 is mentioned in 22 cards [08 §2]; it is now the judgement behind Method 7; item 4, safeguard firing tables [S001 pp. 23–24]: "The aim is to interfere as little as possible with the SQP iteration but to do enough to give a bias towards [c]onvergen[c]e." [S001 p. 2] (letters lost in the text extraction restored in brackets; the card copies the damaged form); item 5, Uno generates solvers from ingredients [S119 p. 3], and the Minotaur paper states its aim as no overhead from flexibility [S032 TR p. 16].

### Review fixes (T3.6)

- Item 4: the two halves now carry their own pages: safeguards rarely fire (firing tables) [S001 pp. 23–24]; failures kept in the statistics, filter SQP failing on 6 of 159 large problems and LANCELOT on 24, crashes in Table 1 [03 E10; S001 pp. 18, 21–22].

### Before T3.6 (moved verbatim)

**Marks of good research**

1. **It crosses the integer/continuous divide by integration, not by decomposition along software lines.** "I really like this trick because it sort of goes from the integer side back to the continuous side" (2024, ASR) [02 §1.8]; practice: NA/182 callbacks, FilMINT, MIPDECO [01 S2, S4, S5].
2. **It makes a received "unsafe" or "hopeless" verdict obsolete through careful formulation plus a reliable solver.** MPECs as NLPs (anatomy 4) [06 Turn E; 03 E52]; thermal insulation from black box to smooth MINLP [02 §3.8].
3. **A result is only as good as the guarantee behind it.** "I don't even know what it means if you're converging to a stationary point" (2024, ASR) [02 §1.5]; his lines end in convergence theory (filter 2002, MPEC 2006, McCormick 2025) [01 S3, S5].
4. **Safeguards interfere as little as possible with Newton's method; robustness counts alongside speed.** "the development of global optimization safeguards that interfere as little as possible with Newton's method" (2006) [01 S3]; failures kept in the statistics [03 E10].
5. **It leaves infrastructure others can extend.** Praise of Fletcher's open QP code (2016) [02 §1.3]; Minotaur and Uno aims [02 §7.2].

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Marks of good research**

1. **It crosses the integer/continuous divide by integration, not by decomposition along software lines.** "I really like this trick because it sort of goes from the integer side back to the continuous side" (2024, ASR) [02 §1.8]; NA/182 callbacks, FilMINT, MIPDECO [01 S2, S4, S5; S009 p. 10].
2. **It makes a received "unsafe" or "hopeless" verdict obsolete through careful formulation plus a reliable solver.** MPECs as NLPs [06 Turn E; S020 pp. 1–2]; thermal insulation from black box to smooth MINLP [02 §3.8; S043 pp. 8–9].
3. **A result is only as good as the guarantee behind it.** "I don't even know what it means if you're converging to a stationary point" (2024, ASR) [02 §1.5]; even robust NLP solvers need "a proof such as the one given in Subsection 5.2 to ascertain the quality of the solutions they produce" [S031 p. 18]. Method 7 gives this judgement steps.
4. **Safeguards interfere as little as possible with Newton's method; robustness counts alongside speed.** "the development of global optimization safeguards that interfere as little as possible with Newton's method" (2006) [01 S3]; safeguards rarely fire [S001 pp. 23–24]; failures kept in the statistics [03 E10; S001 pp. 18, 21–22].
5. **It leaves infrastructure others can extend.** Praise of Fletcher's open QP code (2016) [02 §1.3]; Minotaur and Uno [02 §7.2; S119 p. 3].
6. **It prints its own boundary.** "better heuristics for nonconvex MINLP problems remain an open problem" [S009 p. 11]; an untreated case named [S126 arXiv p. 25].

### Review fixes (T3.7)

- Item 4: his 2006 statement is back before the practice, so the bold title is attributed again: "the development of global optimization safeguards that interfere as little as possible with Newton's method" (2006) [01 S3]. Item 1's 2024 lecture quote stays here only (auto-caption wording, approximate; word budget).

<a id="taste-warnings"></a>

## Taste: warning signs of bad research

### Added in T3.6

- **Item 4 (new): a stopping point that admits a descent direction, or success counted by solver status.** "Weaker stationarity notions exist, but most allow first-order descent directions, making them too weak as practical stopping criteria [46]." [S126 p. 3]; "A common drawback of the NLP-based approach for MPECs is that it can converge to spurious stationary points, such as C-stationary or M-stationary points, with trivial descent directions." [S069 preprint p. 3]; two-variable examples with A-, C- and M-stationary points that admit descent [S042 pp. 5–7]. Basis: Method 7 promotion [08 §4].
- **Item 5 (new): a hand-set parameter that an acceptance test could decide.** "First, we remove the need for the arbitrary parameters in [2] by interpreting these parameters as a trust-region radius." [S048 p. 3]; penalty parameters force hard user decisions and fail both ways [S001 pp. 1–2]; the funnel sets the ADMM penalty adaptively: "Unlike traditional ADMM methods that use a fixed penalty parameter, we adopt the funnel-based strategy in [5] to adaptively increase the penalty when constraint infeasibility is high." [S164 p. 4]; forcing sequences replaced [S077 p. 3; S110 p. 4]. Basis: the Method 2 practice note [08 §2].
- **Item 2**: the Maratos example is anchored to the filter papers [S001 pp. 7–8; S019 p. 8] (correction 3); the narrow-test-class objection also opens the 1994 OA paper [S003 pp. 2, 12].
- **Taste quick-check**: one question added, "Does termination certify the notion the user needs, and is every competitor graded by it? (no → Method 7)".

### Review fixes (T3.6)

- Item 2: the word "shattered" is from the 2006 history [S019 p. 8]; the example is also in the filter report [S001 pp. 7–8].
- Item 4: qualified "(in method design)", because his 2017 essay keeps reliable NLP solvers as the practical MPEC approach [H004 p. 9]; the second half (success counted by solver status) is marked as inferred from practice, competitors graded by certificate [S126 arXiv pp. 34, 40].

### Before T3.6 (moved verbatim)

**Warning signs of bad research**

1. **Brute force or black boxes where structure could be exposed.** "exascale machine would run longer than age of universe!" (2013) [02 §1.7]; "Snag: Solver looses model insight" (2016) [02 §4.9].
2. **One good example, or a narrow test class, taken as evidence.** "the following example shattered the hope that filter methods can avoid the Maratos effect in general" [02 §3.4]; "the test problems are limited to the case where f and g are both linear functions in y" [03 E43].
3. **A hard-looking problem whose difficulty comes from its formulation.** The IEEE 802.11 "one horrible constraint", taught 2013, 2016, 2018 [02 §1.10]; "I'm just predicting complete garbage" for surrogates outside their training data (2024, ASR) [02 §2.6].

**Taste quick-check before T3.6 (moved verbatim)**

- [ ] Does the method rely on a restriction from the software rather than the mathematics? (yes → Method 1)
- [ ] Can you state your base in one sentence, and list its assumptions that may fail here? (no → Method 2)
- [ ] Have you built the smallest failing example and checked it against the theory's hypotheses? (no → Method 3)
- [ ] Is there an untried linear or convex reformulation; have you read the log for a CQ failure? (Method 6)
- [ ] Will the test set, known values and formulation variants be public and correctable? (no → Method 4)
- [ ] Does the comparison state its fairness rule, filter bias, date and versions? (no → Method 5)
- [ ] Is there a convergence guarantee, and does stationarity mean anything for this model? (no → Taste 3)

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Warning signs of bad research**

1. **Brute force or black boxes where structure could be exposed.** "exascale machine would run longer than age of universe!" (2013) [02 §1.7]; "Snag: Solver looses model insight" (2016) [02 §4.9].
2. **One good example, or a narrow test class, taken as evidence.** "the following example shattered the hope that filter methods can avoid the Maratos effect in general" [02 §3.4; S019 p. 8; example also in S001 pp. 7–8]; "the test problems are limited to the case where f and g are both linear functions in y" [03 E43].
3. **A hard-looking problem whose difficulty comes from its formulation.** The IEEE 802.11 "one horrible constraint", taught 2013, 2016, 2018 [02 §1.10]; "I'm just predicting complete garbage" for surrogates outside their training data (2024, ASR) [02 §2.6].
4. **A stopping point that admits a descent direction (in method design), or success counted by solver status.** Weaker notions "allow first-order descent directions, making them too weak as practical stopping criteria" [S126 arXiv p. 3]; "spurious stationary points" [S069 preprint p. 3; S042 pp. 5–7]. The second half is inferred from practice: competitors graded by certificate, not status [S126 arXiv pp. 34, 40].
5. **A hand-set parameter that an acceptance test could decide.** "we remove the need for the arbitrary parameters in [2] by interpreting these parameters as a trust-region radius" [S048 p. 3]; penalty parameters as a burden on users [S001 pp. 1–2].

**Taste quick-check**

- [ ] Does the method rely on a restriction from the software rather than the mathematics? (yes → Method 1)
- [ ] Can you state your base in one sentence, and list its assumptions that may fail here? (no → Method 2)
- [ ] Have you built the smallest failing example and checked it against the theory's hypotheses? (no → Method 3)
- [ ] Is there an untried linear or convex reformulation; have you read the log for a CQ failure? (Method 6)
- [ ] Will the test set, known values and formulation variants be public and correctable? (no → Method 4)
- [ ] Does the comparison state its fairness rule, filter bias, date and versions? (no → Method 5)
- [ ] Is there a convergence guarantee, and does stationarity mean anything for this model? (no → Taste 3)
- [ ] Does termination certify the notion the user needs, and is every competitor graded by it? (no → Method 7)

### Review fixes (T3.7)

- Taste quick-check: each question again says which answer sends the reader to a method (yes → Method 1; no → the others). The fourth question, as T3.7 shortened it, points to Method 6 on "no" for both of its halves, so it carries "no →" as well.

<a id="method-1"></a>

## Method 1: Own the instrument: integrate at the iteration level, strip tooling restrictions, expose building blocks

### Counts for all methods (08 §2)

| Method | Cards (E / V / C) | Full or partial | Evidence by period | Say–do after the full texts |
|---|---|---|---|---|
| M1 Own the instrument | 60 (47 / 13 / 0) | 56 | 4 / 7 / 14 / 11 / 5 / 5 (+1 undated) | ✅ stated + practised, 1993–2026 |
| M2 Base and extension | 128 (110 / 19 / 0) | 118 | 5 / 16 / 17 / 21 / 28 / 21 (+2) | ✅; step 5 moves from inferred to practised |
| M3 Counterexample discipline | 48 (39 / 11 / 0) | 48 | 4 / 9 / 6 / 5 / 7 / 8 | ✅; step 3 qualified |
| M4 Test library as instrument | 32 (24 / 6 / 2) | 31 | 2 / 7 / 8 / 4 / 2 / 1 | ✅ for algorithm test libraries; ⚠ for application models |
| M5 Calibrated claims | 103 (65 / 42 / 3) | 100 | 4 / 9 / 12 / 10 / 19 / 11 | ✅ with recurring, documented gaps |
| M6 Read the numbers, fix the formulation | 85 (77 / 8 / 0) | 83 | 4 / 9 / 16 / 19 / 16 / 12 (+1) | ✅; the linear > convex > nonconvex ordering is qualified |

### The section intro before T3.6 (moved verbatim)

**Core Research Methods**

Six methods passed the four Phase 2 checks (recurrence, say–do, executable, exclusive), most exclusive first. Full evidence: [02](02-methodology.md), [03](03-process-evidence.md).

### Full-text evidence (08 §2)

**Method 1 · Own the instrument** (08)

- **Strongest practice.** The thesis names the packaged NAG solver's limits as a cost (one warm-start level, no phase I output) and uses hot starts and final-tableau pricing where he owns the code [S016 pp. 31, 40–42, 77, 80]. MIQP child bounds come from the owned QP solver's final tableau [S010 pp. 3–7]. The 1998 integrated SQP–B&B traces a restriction to the packaged solver, reads SQP linearizations as cuts and attaches through a callback after each SQP step [S009 pp. 1–2, 4–6, 10]. Strong branching reuses stored QP factors; a single QP gains a factor of 2–3, a hot-started QP up to 40 [S149 pp. 6–8; S028 TR pp. 11–14]. QP-diving is designed around the hot-startable QP layer [S049 pp. 4–7]. FilMINT is built through framework callbacks without core changes [S015 pp. 9, 18]. Minotaur and Uno decompose solvers into swappable classes and validate by rebuilding known solvers as presets [S032 TR pp. 5, 12–15, 20–21; S119 pp. 5, 14–15, 21–23]; the funnel is built by modifying the filter component [S114 arXiv pp. 2, 4, 12].
- **Stated.** In the Fletcher interview he links Dundee practice to writing software [H005 p. 4].
- **New practice the cards add (proposed steps).**
  1. *Price the inner re-solve before designing the outer loop.* The ranking of B&B against decomposition is explained by the cost of a child QP (one to two pivots) and predicted to change when nodes need several QPs [S010 p. 12]; parallel tasks were resized because warm-started NLPs took one to two QPs [S039 pp. 8–9, 14]; a timing table of NLP vs cold QP vs hot QP motivates QP-diving [S049 p. 5] and approximate strong branching [S149 p. 8; S028 TR p. 14]; in quantum control the matrix exponentials per greedy decision are counted and precomputed first [S134 arXiv pp. 7–8]. Six works, 1998–2025.
  2. *Read the outer proof for its minimal requirements and spend the slack on inexact inner solves.* The survey states that NLP-BB needs global optimality only at pruned nodes and only a branching variable elsewhere, and uses this for inexact SQP solves and QP-diving [S002 pp. 24, 29]; the thesis budgets the outer tolerance from the inner tolerances [S016 pp. 96–103]; MPECopt proves which MILP solves may stop early and checks the saving with node-count histograms [S126 pp. 29–30, 34–37]; early branching uses a convergence-rate trigger [S009 p. 9].
  3. *Unify a method family as relaxations of one exact master.* The exact but impractical reformulation is stated first and every algorithm derived as its relaxation, so worst cases and strength orders transfer [S101 pp. 3–6; S016 pp. 56–57; S002 pp. 34–35]; the Uno paper generates algorithms as combinations of ingredients and classifies fifteen solvers in one table [S119 pp. 3, 14–15].
- **Variants.** Late works integrate at the iteration level through off-the-shelf solvers' hooks rather than owned code: MILP stopped at the first improving point and LPEC outputs read as active sets, with IPOPT, Gurobi and HiGHS unmodified [S126 pp. 11, 32, 37]; adjoint callbacks of an off-the-shelf integrator [S091 pp. 20, 35]; lazy-constraint callbacks [S093 pp. 25–26; S155 pp. 11, 15]. One recent paper decomposes into separate solver blocks instead [S164 pp. 3–4]. The cost of owning a framework is stated by the Minotaur paper itself: the goal is no overhead from flexibility, not the fastest solver [S032 TR p. 16].

### Added in T3.6

- **Condensed into SKILL.md**: Stated = the epigraph [S009 p. 2]; Practice [S016 pp. 31, 40–42, 77, 80; S009 pp. 4–6, 10; S149 pp. 6–8]; Say–do from the counts table above (60 cards: 47 evidence, 13 variant, 0 contradiction; 56 read in full or in part); variant bullet on off-the-shelf hooks [S126 pp. 11, 32, 37; S091 pp. 20, 35]. Dropped from the condensed block, kept here: "there is no need to compute a lower bound if the linearizations in the SQP solver are interpreted as cutting planes." [02 §3.3]; Minotaur and Uno presets [S032 TR pp. 12–15; S119 pp. 14–15, 21–23]; the decomposition variant [S164 pp. 3–4].
- **New step 4 (08 §2 proposed step 1)**: price the inner re-solve before designing the outer loop [S010 p. 12; S049 p. 5; S039 pp. 8–9; S149 p. 8; S028 TR p. 14; S134 arXiv pp. 7–8]. "These results show that the benefit obtained by solving just a single QP is only a factor of 2 or 3, whereas hot-started QPs are faster by a factor of up to 40." [S149 p. 8]
- **New step 5 (08 §2 proposed step 2)**: read the outer proof for its minimal requirements and spend the slack on inexact inner solves [S002 pp. 24, 29; S016 pp. 96–103; S126 pp. 29–30, 34–37; S009 p. 9]. "In fact, at any non-leaf node of the tree, we need only to provide a branching variable." [S002 p. 29]
- **Step 6 extended (08 §2 proposed practice 3)**: unify a method family as relaxations of one exact master [S101 pp. 3–6; S016 pp. 56–57; S002 pp. 34–35; S119 pp. 3, 14–15]; in SKILL.md this is catalog entry D16.
- **Renumbering**: old steps 4, 5, 6 are now steps 6, 7, 8. Step 1 now cites the NA/182 text [S009 pp. 1–2]; step 2 the callback [S009 p. 10]; step 3 the catalog entries D1 and D14.
- **Limitations**: the framework's goal is stated as no overhead from flexibility, not the fastest solver: "Our goal here is not to develop the fastest possible solver, but rather to demonstrate that our flexible implementation does not introduce additional computational overhead." [S032 TR p. 16]

### Before T3.6 (moved verbatim)

**Method 1: Own the instrument: integrate at the iteration level, strip tooling restrictions, expose building blocks**

**One line**: Many MINLP habits are artefacts of packaged software; control the inner solver, interleave the outer algorithm with its iterations, drop restrictions the mathematics does not need, expose the parts as building blocks.

**Evidence**:
- Stated: B5, B6, B9 [02 §0]; the 1998 quote above; "there is no need to compute a lower bound if the linearizations in the SQP solver are interpreted as cutting planes." [02 §3.3]
- Practice: packaged NAG solver in the 1993 thesis, then his own filterSQP enables the 1998 algorithm [06 Turn D]; NA/182 callback: "The use of this routine has kept the necessary changes to filterSQP to a minimum." [01 S2]; MINLP_BB and filterSQP manuals [03 E29]; Minotaur engine files under his author tag [03 E31]; Uno commits and presets validated against filterSQP and IPOPT [03 E34, E05].
- Say–do consistency: ✅ stated + practised.

**Steps**:
1. List each restriction of the method you want to improve and ask: mathematics or packaged solver? (Borchers and Mitchell solved two QPs before branching because their SQP code was packaged [01 S2].)
2. Get control of the inner solver (own code or a modifiable open framework); add a callback after each inner iteration, changing the inner code minimally.
3. Reinterpret what the inner solver already produces as what the outer algorithm needs (SQP linearizations as cuts; hot-started QPs for branching).
4. Decompose shared machinery into building blocks ("relaxation and constraint enforcement"; "eight building blocks" for Lagrange-Newton methods [02 §3.6]) and implement them as swappable components.
5. Validate by imitation: rebuild known solvers as presets and compare on the same instances, logs published [03 E05].
6. Keep the reference implementation beside any port (BQPD Fortran beside BQPD-CPP) [03 E30].

**Applies to stage**: idea generation, experiment design, diagnosis.

**Different from standard practice**: most MINLP work calls NLP and MILP solvers as black boxes; he redesigns at the iteration level and says why.

**Limitations**: Minotaur and Uno were written mainly by postdocs (Mahajan, Vanaret) [03 E70]; his code share is small. Alone, modify one open solver through its callbacks; do not write a framework. Owning the tree can cost speed: "The performance difference between Minotaur-QG and AOA are significant, even though they utilize the same basic algorithm." (doi:10.1007/s11081-018-9411-8) [05 §2.3].

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Epigraph (top of SKILL.md)**

> "By using our own solver we are able to remove this unnecessary restriction, widening the scope for early branching." — Leyffer, "Integrating SQP and branch-and-bound for Mixed Integer Nonlinear Programming", Dundee report NA/182 (1998), p. 2 [S009 p. 2]; journal version Comput. Optim. Appl. 18(3) (2001), doi:10.1023/A:1011241421041

**Core Research Methods (section text)**

Seven methods. Methods 1-6 passed the four Phase 2 checks (recurrence, say–do, executable, exclusive) on web research, most exclusive first [02, 03], and were re-tested on the full texts [08 §2-§3]; Method 7 was promoted from them [08 §4]. Say–do counts: distinct cards linking the method (evidence / variant / contradiction). Catalog ids (P, D, E, W): [technique catalog](../technique-catalog.md).

**Method 1: Own the instrument: integrate at the iteration level, strip tooling restrictions, expose building blocks**

**One line**: Many MINLP habits are artefacts of packaged software; control the inner solver, interleave the outer algorithm with its iterations, drop restrictions the mathematics does not need, expose the parts as building blocks.

**Evidence** (full evidence: references/research/09-evidence-ledger.md#method-1):
- Say–do: ✅ stated + practised, 1993–2026; full texts: 60 cards (47 / 13 / 0).

**Steps**:
1. List each restriction of the method you want to improve and ask: mathematics or packaged solver? (Borchers and Mitchell's two QPs before branching came from packaged code [S009 pp. 1–2].)
2. Get control of the inner solver (own code or a modifiable open framework); add a callback after each inner iteration, changing the inner code minimally [S009 p. 10].
3. Reinterpret what the inner solver already produces as what the outer algorithm needs: SQP linearizations as cuts, hot-started QPs for branching, child bounds from the parent's tableau (D1, D14).
5. Read the outer proof for its minimal requirements and spend the slack on inexact inner solves [S002 pp. 24, 29; S126 arXiv pp. 29–30] (D17).
6. Decompose shared machinery into swappable building blocks ("eight building blocks" for Lagrange-Newton methods [02 §3.6]) (D16).
7. Validate by imitation: rebuild known solvers as presets and compare on the same instances, logs published [03 E05].

**Limitations**: Minotaur and Uno were written mainly by postdocs [03 E70]; alone, modify one open solver through its callbacks. The framework aims at no overhead, not top speed [S032 TR p. 16], and owning the tree can cost speed: "The performance difference between Minotaur-QG and AOA are significant, even though they utilize the same basic algorithm." (doi:10.1007/s11081-018-9411-8) [05 §2.3].

<a id="method-2"></a>

## Method 2: Base and extension: carry the home NLP toolkit into a new class

### Full-text evidence (08 §2)

**Method 2 · Base and extension** (08)

- **Strongest practice.** Fletcher's phase I, exact-penalty and convex-composite machinery carried into MINLP [S003 pp. 4–5, 15–21; S016 pp. 66, 84–87]; filterSQP and the filter carried into MPECs through an AMPL interface [S020 pp. 1, 5–6, 18; S057 pp. 17–18]; the filter carried into nonsmooth, augmented-Lagrangian and nonlinear-equation methods [S019 pp. 10–15; S026 pp. 2, 6–7; S071 pp. 4–5; S110 pp. 2, 4]; MPEC-as-NLP carried up to EPECs [S011 pp. 4, 8, 12–16] and into robust optimization through a bilevel-then-MPEC recast [S021 TR pp. 12–13]; trust-region globalization and its proof carried into integer optimal control in function space [S065 pp. 2, 5–6, 17; S091 pp. 3, 26–28, 42]; ReLU networks recast as convex MINLP and as MPCC with his slack formulation [S064 pp. 14–16, 22–23]; McCormick and OBBT carried into PDE-constrained integer control [S096 arXiv pp. 2–3, 6–7, 9]; funnel and filter carried into ADMM [S164 p. 4; S159 pp. 6–16].
- **Say–do update: step 5 is practised, not only inferred.** `SKILL.md` labels step 5 (list and check the carried-in assumptions) as an inferred adjustment he does not state. The full texts show it in coauthored work from 2013 on: assumptions graded in print as most restrictive, mild or technical [S002 p. 22; S147 p. 3]; the inner NLP solver's required behaviour written as a numbered assumption with the untreated case named [S126 pp. 24–25]; the wave number kept away from Helmholtz eigenfrequencies to keep the carried-in uniqueness [S144 p. 11], and a sweep showing failure beyond the theory's small-k0 range [S085 p. 23]; state bounds called quite strong and made explicit [S096 arXiv pp. 6, 9]; unique PDE solvability listed up front [S215 p. 1]. The thesis already warned that the CQ matters more for OA than had been recognised [S016 p. 15].
- **What is carried (proposed practice note).** In most extensions the carried piece is an acceptance test that replaces a hand-set parameter or schedule: the penalty parameter [S001 pp. 1–4], forcing sequences of augmented-Lagrangian methods [S077 p. 3; S071 pp. 4–5; S110 p. 4], an arbitrary sampling radius reread as a trust-region radius [S048 p. 3], a regularization parameter shown equivalent to a radius [S108 pp. 7, 10–11], the ADMM penalty [S159 pp. 13, 16, 35; S164 p. 4]. Or it is a trust region on a new space: Hamming or ℓ1 balls on binaries with knapsack or MILP subproblems and ared/pred acceptance [S084 pp. 16–18; S065 pp. 5–6; S092 pp. 3–6; S128 pp. 12–13; S144 p. 12; S215 p. 2; S146 pp. 22–23], or a measure-space ball on control sets [S091 pp. 23–26].
- **Variants.** The carried toolkit is not always the filter/NLP base: B&B and SOS modelling into global optimization [S041 pp. 3–5, 16–19]; MILP into MINLP [S015 pp. 9–18]; multigrid into MIP and SDP [S072 arXiv pp. 3–4, 23; S185 preprint p. 5]; integer algebra [S143 pp. 4–5, 7]; conic modelling [S156 pp. 2–4]. In several facility-driven papers since 2019 the home toolkit does not travel at all (greedy paths, ADAM, policy gradients, RBF surrogates) [S160 arXiv pp. 3–5; S165 pp. 3–5; S068 pp. 2–3; S123 arXiv pp. 4, 11; S216 pp. 2–3]; he is not first author in these.

### Added in T3.6

- **Condensed into SKILL.md**: Stated (research statement) [06 §0]; Practice [S003 pp. 4–5, 15–21; S065 pp. 2, 5–6, 17; S064 pp. 14–16, 22–23]; Say–do (128 cards: 110 evidence, 19 variant, 0 contradiction; 118 read in full or in part); variants on step 5, on what is carried [S048 p. 3; S084 pp. 16–18] and on facility-led papers [S160 arXiv pp. 3–5]. Kept here: filterSQP into MPECs [S020 pp. 1, 5–6, 18]; the filter into nonsmooth, augmented-Lagrangian and equation methods [S019 pp. 10–15; S026 pp. 2, 6–7; S071 pp. 4–5; S110 pp. 2, 4]; funnel and filter into ADMM [S164 p. 4; S159 pp. 6–16]; other toolkits carried [S041 pp. 3–5; S072 arXiv pp. 3–4]; no home toolkit [S068 pp. 2–3].
- **Step 3 extended (08 §2 practice note)**: carry an acceptance test or a trust region, not a parameter [S001 pp. 1–4; S077 p. 3; S071 pp. 4–5; S110 p. 4; S048 p. 3; S108 pp. 7, 10–11; S159 pp. 13, 16, 35; S164 p. 4]; trust regions on new spaces [S084 pp. 16–18; S065 pp. 5–6; S092 pp. 3–6; S128 pp. 12–13; S144 p. 12; S215 p. 2; S146 pp. 22–23; S091 pp. 23–26]. "We prefer a polyhedral norm, however, because it allows us to rewrite (19) equivalently as an MILP." [S144 p. 11]
- **Step 5 corrected (08 §3.2 item 5)**: practised in coauthored work since 2013, not only inferred: assumptions graded in print [S002 p. 22; S147 p. 3] ("A3 is technical (MFCQ would have been sufficient)" [S147 p. 3]); the inner solver's behaviour a numbered assumption with the untreated case named [S126 pp. 24–25]; carried-in uniqueness protected [S144 p. 11]; a sweep beyond the theory's range [S085 p. 23]; state bounds made explicit [S096 arXiv pp. 6, 9]; unique solvability listed up front [S215 p. 1]; the thesis already warned that "for outer approximation the constraint qualification is more important than has previously been recognised." [S016 p. 15]
- **Step 4 and 6**: card refs added [S112 pp. 1–2; S114 arXiv pp. 2–3, 11].
- **Limitations**: the PDE-solvability fix now cites the Correction [S162 p. 1].

### Review fixes (T3.6)

- Step 3: the ℓ1 ball on binaries is S084's Hamming-distance trust region, whose linearized step is a sorted knapsack [S084 pp. 16–18]; S065's ball is an L1(Ω) ball on integer-valued controls, five control levels in its experiments [S065 pp. 5–6, 19–20]; the funnel citation [S164 p. 4] now sits on the funnel clause.
- Limitations: "upper-level strict complementarity" restored, as in 05 §4.2 and the pre-synthesis text.
- Variant marks now name their kind after ✗ (Correction or Contradiction); the How to Use paragraph defines the marks.

### Before T3.6 (moved verbatim)

**Method 2: Base and extension: carry the home NLP toolkit into a new class**

**One line**: Keep one deep competence fixed (reliable NLP methods, filter globalization), enter new areas by carrying it in, re-cast the newcomer's objects into home classes.

**Evidence**:
- Stated: B3 (5 occasions) [02 §0]; his research statement, unchanged December 2008 to September 2026: "I am interested in the development of reliable methods for solving large-scale nonlinear optimization problems and in the implementation and analysis of filter type algorithms." [06 §0]; on MPECs: "as long as we take care with the problem formulation and the algorithm design, modern NLP solvers can tackle these problems." [06 Turn E]
- Practice: filter carried to MPECs, augmented Lagrangians, constrained DFO (2026) and ADMM (doi:10.1007/s10957-026-02983-7); exact penalty to quantum Hamiltonian descent (2026) [03 E64]; ReLU networks recast "as a mixed-integer optimization problem and as a mathematical program with complementarity constraints" [06 Turn I].
- Say–do consistency: ✅ stated + practised.

**Steps**:
1. Write your base in one sentence and keep it fixed.
2. For a candidate area, ask what your toolkit can carry in and what the area's own methods cannot do.
3. Re-cast the new field's objects into a home class (ReLU networks as MINLP or MPCC; quantum pulses as TV-regularized binary control).
4. Name the class publicly with its challenges and a starting library ("On-going work: Building library of test problems", MIPDECO) [02 §2.4, §4.5].
5. List the home-theory assumptions you carry in (CQs, exact subproblem solves, strict complementarity, unique PDE solvability) and check each. *Inferred adjustment: what the critics found missing [05 §7]; he does not state it.*
6. When the extensions mature, rebuild the base (AL filter, Uno, funnel SQP, penalty functions revisited, 2016-2026) [06 Turn J].

**Applies to stage**: problem choice, research agenda.

**Different from standard practice**: entering a field with your own formulations and convergence machinery, not the field's algorithms; one base sentence for 18 years while the extension list migrates.

**Limitations**: carried-in assumptions break: CQs and exact NLP solves in OA (arXiv:2606.26897) [05 §1.3]; upper-level strict complementarity for MPEC-SQP [05 §4.2]; unique PDE solvability, fixed in the 2026 Correction [05 §5.2]. After 2013 the extensions came through collaborators and laboratory facilities [06 §9.5]; a junior lacks that pull.

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Method 2: Base and extension: carry the home NLP toolkit into a new class**

**Evidence** (full evidence: references/research/09-evidence-ledger.md#method-2):
- Stated: his research statement, unchanged December 2008 to September 2026: "I am interested in the development of reliable methods for solving large-scale nonlinear optimization problems and in the implementation and analysis of filter type algorithms." [06 §0]
- Practice: Fletcher's phase I and exact-penalty machinery carried into MINLP [S003 pp. 4–5, 15–21]; trust regions into integer control in function space [S065 pp. 2, 5–6, 17]; ReLU networks recast as MINLP and MPCC [S064 pp. 14–16, 22–23].
- Say–do: ✅ stated + practised, 1994–2026; full texts: 128 cards (110 / 19 / 0).
- Variants/corrections:
  - ✗ Correction: step 5 is practised, not only inferred: assumptions graded in print, the inner solver's behaviour a numbered assumption [S002 p. 22; S126 arXiv pp. 24–25].
  - ⚠ What travels is usually an acceptance test that replaces a hand-set parameter, or a trust region on a new space [S048 p. 3; S084 pp. 16–18]; some facility-led papers carry no home toolkit [S160 arXiv pp. 3–5].

**Steps**:
3. Re-cast the new field's objects into a home class (ReLU networks as MINLP or MPCC; quantum pulses as TV-regularized binary control). Carry an acceptance test or a trust region, not a parameter: a funnel instead of a penalty schedule [S164 p. 4], an ℓ1 ball on binary or integer-valued controls with an ared/pred test [S084 pp. 16–18; S065 pp. 5–6] (D3, D4).
4. Name the class publicly with its challenges and a starting library ("On-going work: Building library of test problems", MIPDECO) [02 §2.4, §4.5; S112 pp. 1–2].
5. List the home-theory assumptions you carry in (CQs, exact subproblem solves, strict complementarity, unique PDE solvability), check each, grade them in print and name the untreated case [S002 p. 22; S126 arXiv pp. 24–25].

**Limitations**: carried-in assumptions break: CQs and exact NLP solves in OA (arXiv:2606.26897) [05 §1.3]; upper-level strict complementarity for MPEC-SQP [05 §4.2]; unique PDE solvability, fixed in the 2026 Correction [S162 p. 1]. After 2013 the extensions came through collaborators and facilities [06 §9.5]; a junior lacks that pull.

<a id="method-3"></a>

## Method 3: Counterexample discipline: smallest breaking example, hypothesis check, run it, redesign

### Full-text evidence (08 §2)

**Method 3 · Counterexample discipline** (08)

- **Strongest practice.** At least seven hand-computed smallest counterexamples in the thesis, including one against his own quadratic OA [S016 pp. 49, 62–66, 69, 93–95]; the Duran–Grossmann master broken on a two-point instance and OA's worst case on a geometric grid [S003 pp. 8, 12–14]; the Benders counterexample with the hypothesis check before any claim of error [S055 pp. 3–7]; PIPA broken on a smallest instance whose hypotheses hold, run and tabulated, with symptom and remedy [S067 pp. 3–7; D001 pp. 4–9]; three stationarity notions and SQPEC broken on two-variable examples with closed-form iterates, his own NLP approach among the targets [S042 pp. 5–8]; each penalty-update policy broken by a tiny MPCC [S012 pp. 5–7, 25–26]; Bland's rule cycling for LPCCs [S069 preprint pp. 6, 13]; the funnel run on the Maratos counterexample and its failure reported [S114 arXiv pp. 23–24]; the hypothesis check turned on his own theorem in the 2026 Correction [S162 p. 1]; a smallest instance showing a relaxation is no bound across grids [S145 arXiv pp. 16–17].
- **Stated.** He recalls looking at examples as a Dundee rule [H005 p. 4].
- **Variants.** (a) Locating the faulty proof step came in revision: the 2002 report and the 2003 arXiv version declare the PIPA theorem contradicted without naming the step [S067 pp. 6–7; D001 pp. 4, 8]; the step-naming sentence that `SKILL.md` quotes [03 E45] is from a later version, after a colleague read a draft [S067 p. 7]. (b) The smallest example is also used constructively: witness points proving a cut strictly tighter [S087 arXiv pp. 6, 11, 22–23], a two-unknown landscape map [S113 pp. 6–8], what a restriction loses [S011 pp. 21–22], a design choice justified [S013 TR p. 3; S020 p. 3]. (c) The hypothesis check is applied to benchmark failures, matching failing instances to the known absence of strongly stationary points before blaming the method [S022 p. 27]. (d) Re-anchoring: the Maratos example that broke the hope is in the filter papers [S001 pp. 7–8; S019 p. 8]; the 2012 nonmonotone filter answers that failure mode without rebuilding the example [S040 p. 4].

### Added in T3.6

- **Condensed into SKILL.md**: Stated [S055 p. 5] with its hypothesis check [S055 pp. 3–7]; Practice [S016 pp. 49, 62–66, 69, 93–95; S067 pp. 3–7; S042 pp. 5–8]; Say–do (48 cards: 39 evidence, 11 variant, 0 contradiction; all read in full or in part); variants (a), (c), (d) below and the Correction [S162 p. 1]. Kept here: OA's worst case on a geometric grid [S003 pp. 12–14]; the Dundee rule recalled in the interview: "So, I know when I was in Dundee, one of the things you always told us was to look at examples, so this is the same idea." [H005 p. 4]; penalty-update policies broken by tiny MPCCs [S012 pp. 5–7, 25–26]; Bland's rule cycling for LPCCs [S069 preprint pp. 6, 13]; the funnel run on the Maratos example [S114 arXiv pp. 23–24]: "This demonstrates that the funnel method also suffers from the Maratos effect." [S114 arXiv p. 23]; constructive uses [S087 arXiv pp. 6, 11, 22–23; S020 p. 3].
- **Step 2**: the geometric-grid construction added [S003 pp. 8, 12–13].
- **Step 3 qualified (08 §3.2 item 3)**: the step-naming sentence quoted from [03 E45] belongs to a later version; the 2002 report and the 2003 arXiv version publish the checked counterexample without naming the step [S067 pp. 6–7; D001 pp. 4, 8].
- **Step 4**: closed-form iterates [S042 p. 8] (catalog P5). **Step 5**: give the remedy its own worst case [S016 pp. 63–66].
- **Evidence re-anchored (08 §3.2 item 4)**: the Maratos example is in the filter papers [S001 pp. 7–8; S019 p. 8]; the nonmonotone filter answers the failure mode [S040 p. 4].

### Review fixes (T3.6)

- The PIPA citation is marked as the version read, arXiv v1 of September 2003 [D001 arXiv pp. 4, 8]; the OMS journal text was not read (card c05).

### Before T3.6 (moved verbatim)

**Method 3: Counterexample discipline: smallest breaking example, hypothesis check, run it, redesign**

**One line**: Judge a method by its worst case: smallest failing instance, hypothesis check before calling anything wrong, run it, redesign. Same for your own methods.

**Evidence**:
- Stated: B4 (5 occasions) [02 §0]; "At a first glance, the example seems to indicate that there are errors in the various convergence results in the literature. However, this is not the case as the assumptions usually exclude our example." [03 E44]
- Practice: OA "visits all integer points" → quadratic OA (1994) [02 §1.2; 01 F1]; PIPA counterexample run in AMPL [03 E37]; his own approach: "Thus, without modification, the NLP approaches are doomed to converge to spurious stationary points." (2007) [03 E46]; Maratos example → nonmonotone filter (doi:10.1007/s10589-011-9430-2) [02 §3.4].
- Say–do consistency: ✅ stated + practised.

**Steps**:
1. Ask whether the evidence for a method rests on a narrow test class ("the test problems are limited to the case where f and g are both linear functions in y") [03 E43].
2. Build the smallest instance that breaks it (one-dimensional, two-point, a ball in a hypercube).
3. Check the hypotheses. Violated: say so. Satisfied: say the proof is wrong and point to the step ("part (i) of the proof of [16, Theorem 6.1.17] is wrong") [03 E45].
4. Run the counterexample and tabulate the iterates [03 E37].
5. Name a detectable symptom and a remedy, or redesign (worst case → quadratic OA; NLP failures for MPECs → SLPEC filter, 2007 [03 E46]).
6. Turn the lesson into a reformulation and teach it [02 §3.4].

**Applies to stage**: idea generation, judging results.

**Different from standard practice**: the hypothesis check before announcing an error, and running the counterexample, are explicit steps; his own methods get the same treatment.

**Limitations**: needs analysable algorithms with explicit hypotheses; harder for heuristic-rich commercial solvers. Era-free. His own 1994 OA statement and early filter proof were corrected by others [05 §1.1].

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Method 3: Counterexample discipline: smallest breaking example, hypothesis check, run it, redesign**

**Evidence** (full evidence: references/research/09-evidence-ledger.md#method-3):
- Practice: at least seven hand-computed counterexamples in the thesis, one against his own quadratic OA [S016 pp. 49, 62–66, 69, 93–95]; PIPA broken, run and tabulated [S067 pp. 3–7]; stationarity notions broken on two-variable examples, his own approach included [S042 pp. 5–8].
- Say–do: ✅ stated + practised, 1993–2026; full texts: 48 cards (39 / 11 / 0).

**Steps**:
1. Ask whether the evidence for a method rests on a narrow test class ("the test problems are limited to the case where f and g are both linear functions in y") [03 E43].

<a id="method-4"></a>

## Method 4: The test library as a maintained research instrument

### Full-text evidence (08 §2)

**Method 4 · The test library as a maintained instrument** (08)

- **Strongest practice.** Every thesis test problem published with relaxation value and integer optimum, formulation variants side by side [S016 pp. 81, 106–113]; MacMPEC launched with classification, comments, plots, a generator and contributor credit [S020 pp. 6–8, 15, 18; S013 TR pp. 6–8]; badly scaled variants added because the library was almost all well scaled [S012 pp. 21, 23, 25]; a public MacEPEC started because none existed [S011 pp. 22–24]; the DIWAL library of computer-science MINLPs started [S149 pp. 3–4, 8]; MacMPEC linearized into an LPCC set [S069 preprint p. 20]; MacMPEC judged too easy in 2026 and a public generator written for the hard case [S126 pp. 33, 35–36, 41–43]; AMPL instances and code released for MIPDECO [S084 pp. 5, 12, 18].
- **Variant (proposed limitation text).** The public-library habit holds for algorithm test sets, not for application models in team papers: models or data available only on request [S043 p. 23; S100 p. 6; S143 p. 28; H009 p. 9], and one recent code base not released (stated as not approved for release) [S144 p. 23].
- **Contradiction already in the skill.** He agreed in 2015 that test problems are often badly selected [H005 p. 5]; `SKILL.md` records this as Inner Tension 1.

### Added in T3.6

- **Condensed into SKILL.md**: Stated [02 §4.5]; Practice [S016 pp. 81, 106–113; S020 pp. 6–8, 15, 18; S126 pp. 33, 35–36, 41–43]; Say–do (32 cards: 24 evidence, 6 variant, 2 contradiction; 31 read in full or in part); variant on application models [S043 p. 23; S100 p. 6; S144 p. 23] and the contradiction already recorded as Inner Tension 1 [H005 p. 5]. Kept here: MacEPEC started because none existed [S011 pp. 22–24]; the DIWAL library [S149 pp. 3–4, 8]; MacMPEC linearized into an LPCC set [S069 preprint p. 20]; AMPL instances and code released for MIPDECO [S084 pp. 5, 12, 18]; badly scaled variants [S012 pp. 21, 23, 25].
- **Variant (08 §3.2 item 6)**: application models in team papers are often shared only on request [S043 p. 23; S100 p. 6; S143 p. 28; H009 p. 9]; one recent code base was not released [S144 p. 23]. Rewriting the method as "always release code" was rejected [08 §10 item 9].
- **Steps**: step 6 cites [S012 pp. 21, 23]; step 7 now ends in a public generator for the hard case (catalog V8) [S126 pp. 35–36, 41–43]; its quote is kept in the moved text below.

### Before T3.6 (moved verbatim)

**Method 4: The test library as a maintained research instrument**

**One line**: A test set is a long-lived, public, corrected object: known values, several formulations, contributor credit, a dated correction log, new problems when a gap appears.

**Evidence**:
- Stated: "On-going work: Building library of test problems" (2015, 2016); "when you write your own model it's always good to start with something else" (2024, ASR) [02 §4.5].
- Practice: Dundee MINLP_TP (2000), MacMINLP, MacMPEC with a correction log 2000-2007 [03 E12-E19]; scale problems added after a study [03 E17]; MacMPEC re-used in 2025-26 [04 §4.3].
- Say–do consistency: ✅ stated + practised, with a tension: in 2015 he agreed with Fletcher that "test problems are often very badly selected" [02 §1.1].

**Steps**:
1. Convert known test problems into the new class; model collaborators' applications [03 E12].
2. Publish each problem with known values and a classification (convex or not, relaxation value, best known value) [03 E13].
3. Keep several formulations side by side (MacMPEC variants "mathematically equivalent, but may produce different solutions") [03 E16].
4. Release early with a call for problems, "giving full credit to the contributor of each problem" [03 E14].
5. Keep a dated public correction log; treat disagreement with published results as a possible modelling error [03 E15].
6. When a study shows the library is one-sided, add problems [03 E17].
7. Say when it has become too easy: "Many MacMPEC problems are small or easily solved by all examined algorithms." (2026, coauthored) [05 §4.3].

**Applies to stage**: experiment design, after publication.

**Different from standard practice**: maintained for decades with dated corrections, not a by-product of one paper.

**Limitations**: AMPL-era; today contribute instances and corrections to MINLPLib, QPLIB or CUTEst instead of starting a collection. Instances tend to be small [05 §7]. Maintenance needs a stable post.

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Method 4: The test library as a maintained research instrument**

**Evidence** (full evidence: references/research/09-evidence-ledger.md#method-4):
- Practice: thesis test problems published with relaxation value and integer optimum [S016 pp. 81, 106–113]; MacMPEC launched with classification, generator and contributor credit [S020 pp. 6–8, 15, 18]; a public generator for the hard case [S126 arXiv pp. 33, 35–36, 41–43].
- Say–do: ✅ for algorithm test libraries, ⚠ for application models; full texts: 32 cards (24 / 6 / 2).

<a id="method-5"></a>

## Method 5: Calibrated claims on self-built, fairness-stated baselines

### Full-text evidence (08 §2)

**Method 5 · Calibrated claims on fairness-stated baselines** (08)

- **Strongest practice.** Five self-built codes with the same start and the same ε, meters with their weaknesses, failures kept, a rule of thumb by class and his own handicaps stated [S016 pp. 44, 77–83]; self-built competitors on the same QP solver with each problem's best branching rule [S010 pp. 10–12]; a self-built Sℓ1QP at its most favourable penalty, crashes kept, removed problems listed, losses explained by class, a claim narrowed between report revisions [S001 pp. 18–22]; a written failure taxonomy and an at-present stamp [S020 pp. 1, 9, 12, 14; S013 TR p. 1]; failures inside profiles and the theory-favoured variant reported as losing [S022 pp. 23–27]; a deliberately simple base solver so production heuristics do not mask the effect [S012 pp. 2, 20–21]; same-framework baselines with time-outs kept and the test-set filter and its bias stated [S028 TR pp. 5, 9–18, 25–34]; an equal-energy fairness rule with the median of 31 runs [S082 pp. 2–7]; evaluations as the fair unit, failures charged, versions named, logs public [S119 pp. 21–24]; one NLP solver with identical options for all methods and a common certificate as the success criterion [S126 pp. 32–37, 40].
- **Variants (method-level only).**
  - *Tuning set equals comparison set* recurs beyond FilMINT [S015 p. 27]: openly stated in the branching study [S028 TR pp. 7, 17]; per-problem penalty tuning [S079 pp. 13–15]; penalties tuned per instance [S134 arXiv pp. 15–18]; a parameter chosen on the comparison set [S114 arXiv pp. 19–20]. This strengthens the Workflow C checkpoint, which `SKILL.md` labels as inferred from one record.
  - *Baselines at default settings* rather than rebuilt at their best [S020 pp. 9, 14; S061 pp. 11, 15–18; S064 p. 16; S143 p. 22].
  - *No external baseline* in several 2022–2025 integer-control and design papers [S091 pp. 41–42; S128 pp. 15, 18; S145 arXiv pp. 2, 23, 26; S150 pp. 19–22], once with the reason that a fair comparison is hard to design [S091 p. 42]; a 2020 HPC paper states lower bounds as its replacement for a competitor [S102 p. 7].
  - *Rule of thumb incomplete in the skill*: the thesis table has a third row, QP/NLP-based B&B for general-integer problems with a large gap [S016 p. 83].
  - *Yardsticks other than competitors* (proposed practice note): exact optima on small instances before scaling [S073 arXiv pp. 6–7; S102 pp. 4–5], idealized-oracle variants [S094 arXiv pp. 16–18], an oracle-information bound used only a posteriori [S096 arXiv pp. 25, 27], four numbers on one start point (practice design, NLP root, rounded root, MINLP) [S070 preprint p. 21], an a posteriori audit of a linearized model's solution against the nonlinear model [S036 pp. 30–32].
- **Contradictions (3 cards).** In three team papers led by other first authors, outperformance claims against SCIP and Juniper, Gurobi, or a random baseline are made without a stated fairness rule or solver settings [S124 pp. 1, 5–6; S164 p. 5; S160 arXiv pp. 5–8]. The cards rate this as weak evidence about his own practice; it is evidence that Method 5 describes his algorithm papers better than the team's applied record.

### Added in T3.6

- **Condensed into SKILL.md**: Stated [S010 p. 11]; Practice [S016 pp. 44, 77–83; S001 pp. 18–22; S126 pp. 32–37, 40]; Say–do (103 cards: 65 evidence, 42 variant, 3 contradiction; 100 read in full or in part); four variant bullets. Kept here: the failure taxonomy and "at present" stamp [S020 pp. 1, 9, 12, 14]; "It is shown that SQP methods are very well suited to solving MPECs and at present outperform Interior Point solvers both in terms of speed and reliability." [S013 TR p. 1]; same-framework baselines and the filter bias [S028 TR pp. 5, 9–18, 25–34]; equal-energy fairness [S082 pp. 2–7]; evaluations as the fair unit [S119 pp. 21–24].
- **Step 5 corrected (08 §3.2 item 2)**: the thesis table has a third row, QP/NLP-based B&B for general-integer problems with a large gap [S016 p. 83]. The same row now appears in Workflow D step 6 and the Roundtable Card.
- **New step 9 (08 §2 practice note)**: yardsticks other than competitors [S073 arXiv pp. 6–7; S102 pp. 4–5; S094 arXiv pp. 16–18; S096 arXiv pp. 25, 27; S070 preprint p. 21; S036 pp. 30–32].
- **Steps 1-3**: catalog entries V1, V13, V3, V2 (named E1, E13, E3, E2 before the review fix); step 1 cites the same-solver sentence of MPECopt [S126 p. 34]. The long quotes of steps 1, 5 and 7 were shortened in SKILL.md and are kept verbatim below.
- **Workflow C checkpoint strengthened**: tuning set = comparison set recurs [S015 p. 27; S028 TR pp. 7, 17; S079 pp. 13–15; S134 arXiv pp. 15–18; S114 arXiv pp. 19–20].

### Review fixes (T3.6)

- Step 1 restores the same-solver sentence: "Since all methods use IPOPT as the NLP solver, we can directly compare the computation times." [S126 arXiv p. 34]; step 7 restores the loss-reporting example [03 E49].
- Step 5 dates and qualifies the third row: five self-built codes on 22 problems (1993) [S016 pp. 78, 83]; QP/NLP-BB loses the pruning step because QPs give no lower bounds, and "A detailed numerical comparison of the two approaches is still outstanding." (2001) [S101 p. 7]. Workflow D step 6 and the Roundtable Card keep only the two rows that stood before T3.6, called a dated rule of thumb to re-test.
- Variant 3 reworded: NA/210 (2002) ran NEOS solvers, which its card reads as defaults [S020 pp. 9, 14]; several 2022–2025 integer-control papers have no external baseline [S091 p. 42]. Catalog ids are now V1, V13, V3, V2, V7.

### Before T3.6 (moved verbatim)

**Method 5: Calibrated claims on self-built, fairness-stated baselines**

**One line**: Rebuild the competitors at their best settings, write the fairness rule down, keep failures in the statistics, give a rule of thumb by class rather than a winner, date-stamp every claim.

**Evidence**:
- Stated: B10 (7 occasions) [02 §0]; "it's not the method that will beat every method on on all problems but it's a pretty good method" (2024, ASR) [02 §1.6].
- Practice: "In order to gain a fair comparison the best branching rule for each problem was used in the tests." (1995) [03 E02]; "Recall, that our test set is a biased subset of a larger set of problems, specifically chosen to include only the 88 problems on which at least one B&B approach succeeds." [03 E20]; thesis "Rule of Thumb" [03 E47]; "at present" stamps [03 E52]; Uno v1 "outperform most state-of-the-art solvers" narrowed in v2 to "perform well with respect to all the state-of-the-art solvers" [03 E53].
- Say–do consistency: ✅ stated + practised, with a documented gap: FilMINT tuned on its comparison suite [03 E22]; 2015-era competitors in the 2020 Minotaur revision [03 E55]; thesis GTD runs dropped [03 E23].

**Steps**:
1. Same environment, same start, each baseline at its best setting; today the same-solver rule ("Since all methods use IPOPT as the NLP solver, we can directly compare the computation times.") [03 E04, E01].
2. Pick the fair unit (counts of LPs and QPs, not only CPU time) and state each meter's weakness [03 E06, E09].
3. Keep failures inside the statistics, with a per-instance failure taxonomy [03 E10, E40].
4. If you filter the test set, describe the filter and its bias [03 E20].
5. Conclude with a rule of thumb by class: "there is no one solver which can be seen to outperform all other solvers"; LP/NLP for binary MINLPs, nonlinear B&B for a small integrality gap [03 E47].
6. Stamp comparative claims with "at present" and competitor versions [03 E52].
7. Report where your method loses ("this simplistic implementation of LP/NLP-BB is not competitive with MINLP-BB for difficult instances") [03 E49].
8. Narrow claims in revision when the evidence requires [03 E53].

**Applies to stage**: experiment design, judging results.

**Different from standard practice**: calibration and failure reporting are part of the result; the bundle (self-built baselines, fair unit, date stamps, rule of thumb) is his.

**Limitations**: self-built baselines are expensive against today's commercial solvers; use the same-solver rule and pinned versions. Why the Uno claims were narrowed is undocumented.

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Method 5: Calibrated claims on self-built, fairness-stated baselines**

**Evidence** (full evidence: references/research/09-evidence-ledger.md#method-5):
- Say–do: ✅ with recurring, documented gaps; full texts: 103 cards (65 / 42 / 3).
- Variants/corrections:
  - ✗ Correction: the thesis rule of thumb has a third row, dated and qualified in step 5 [S016 p. 83].
  - ⚠ Baselines run as NEOS solvers, apparently at defaults (2002) [S020 pp. 9, 14]; no external baseline in several 2022–2025 integer-control papers [S091 p. 42].

**Steps**:
5. Conclude with a rule of thumb by class, not a winner: LP/NLP for binary MINLPs, nonlinear B&B for a small integrality gap [03 E47]; the 1993 third row, QP/NLP-based B&B for general-integer problems with a large gap, rests on five self-built codes and 22 problems [S016 pp. 78, 83], and QP/NLP-BB gives no lower bounds: "A detailed numerical comparison of the two approaches is still outstanding." (2001) [S101 p. 7].

<a id="method-6"></a>

## Method 6: Read the solver's numbers, then fix the formulation before the method

### Full-text evidence (08 §2)

**Method 6 · Read the solver's numbers, fix the formulation before the method** (08)

- **Strongest practice.** A whole paper that fixes the formulation first: divisions multiplied out for evaluability, a negative cooling power traced to fractional binaries and repaired, QPs per NLP used to rank formulations [S043 pp. 8–9, 17, 19–20, 28]; a coefficient fix that turns an unsolved instance into a sub-second solve [S032 TR pp. 22–23, 26]; a perspective reformulation worth more than 700×, reported in a co-signed overview from two cited papers' runs [S029 pp. 5–6]; slack complementarity and the ≤ form, a misattributed published failure corrected from the model file, and a solver failure called a formulation failure [S020 pp. 1, 3, 5, 10–12]; the importance-of-slacks section with two failure examples [H004 pp. 7–9]; domain violations moved into bounded slacks [S074 p. 15; S002 p. 15]; a Slater failure at z = 0 repaired before any algorithm change [S051 p. 3]; a CQ failure turned into a second-order cone [S142 preprint pp. 3–4]; solver logs read before blaming the problem [S084 pp. 23–24]; termination codes that read CQ failure and wrong gradients [S199 p. 14], exit states that name local infeasibility and evaluation crashes [S014 pp. 3, 8, 12–15], and Fritz John outcomes reported as such [S119 pp. 4, 18].
- **Stated.** The advice to look at numbers is Fletcher's, given in the interview Leyffer conducted, and Leyffer ties it to the Dundee habit of looking at examples [H005 p. 4]; the survey states that solvers fail because iterates cannot be evaluated [S002 p. 15].
- **Variant: the ordering is a default, not a law.** In his own studies the less linear or nonconvex form sometimes won: the smaller nonconvex BATCH-int beat the convexified binary form, and he warned that reformulation can hide nonlinearity [S016 pp. 67, 81]; linearizing reformulations can defeat quadratic OA [S003 p. 15]; convex big-M and convex-hull reformulations ran about 100× and 375× slower than the nonconvex SOS and equality forms under nonlinear B&B [S070 preprint p. 20]. Proposed change to step 1: rank linear, convex, nonconvex as the default, then test the ranking under the algorithm that will be run.
- **Proposed step: a control run before attributing a failure.** Rerun only the failing instances with the suspected cause removed (complementarity relaxed to ≤ 10⁻²; failures persist, so they are not solely due to MFCQ) [S020 pp. 10–12; S013 TR pp. 10–12]; rerun with a smooth surrogate of the nonsmooth piece to rule out the solver [S064 p. 10]; a full factorial design that isolates the factor behind the failures [S168 pp. 4–5]; move the suspected factor into the better configuration and check that it degrades [S114 arXiv p. 20]. Four projects, 2002–2026.
- **Other variants.** A solver failure read as evidence about arithmetic precision and answered by escalating precision [S082 pp. 2, 4]; integrality gap and step norms read as signals for a new branching trigger [S009 p. 9].

### Added in T3.6

- **Condensed into SKILL.md**: Stated [S002 p. 15]; Practice [S043 pp. 8–9, 17, 19–20, 28; S020 pp. 1, 3, 5, 10–12; S029 pp. 5–6]; Say–do (85 cards: 77 evidence, 8 variant, 0 contradiction; 83 read in full or in part); the ordering variant. Kept here: a Slater failure repaired before any algorithm change [S051 p. 3] ("We believe that the failure of the nonlinear solvers is due to a failure of a constraint qualification" [S051 p. 3]); the coefficient fix in Minotaur [S032 TR pp. 22–23, 26]; "The failure of knitro is a failure of the problem formulation, rather than of the method." [S020 p. 12]; "One thing I would say is to look at numbers: they’re trying to tell you something." (Fletcher, in the interview Leyffer conducted) [H005 p. 4]; precision escalation [S082 pp. 2, 4]; a branching trigger from step norms [S009 p. 9].
- **Step 1 corrected (08 §3.2 item 1)**: rank linear, convex, nonconvex as the default, then test the ranking under the algorithm that will be run [S016 pp. 67, 81; S003 p. 15; S070 preprint p. 20]. "However, the CPU time is about 100 times longer than that resulting from the special ordered set formulation for the three-story one-bay structure with vertical loads only." [S070 preprint p. 20]
- **Step 3 extended**: exit codes [S199 p. 14; S014 pp. 3, 8, 12–15; S119 pp. 4, 18]: "We note also that ifail=5, the trust-region converging to zero, frequently occurs if the gradients are wrong." [S199 p. 14]
- **New step 4 (08 §2 proposed step)**: a control run before attributing a failure [S020 pp. 10–12; S013 TR pp. 10–12; S064 p. 10; S168 pp. 4–5; S114 arXiv p. 20]. Old steps 4, 5, 6 are now steps 5, 6, 7; Workflow D, the Agentic Protocol and the anti-patterns table were renumbered to match.
- **Steps 5-6**: domain violations into bounded slacks [S074 p. 15; S002 p. 15]: "It is often possible to reformulate the nonlinear constraints to avoid IEEE exceptions." [S074 p. 15]; the importance-of-slacks section [H004 pp. 7–9]; catalog entry D9.

### Review fixes (T3.6)

- Practice: the perspective speed-up of more than 700 times is reported in a co-signed SciDAC overview that combines runs from two cited papers ([8] Günlük–Linderoth and [10]); the card calls the section two illustrations, not a study [S029 p. 5]. SKILL.md now names a study of the paper's own instead: a coefficient fix takes syn20M04M from unsolved to 0.49 s [S032 TR pp. 22–23].
- Variant: the 100 and 375 times both come from one instance, the three-story one-bay frame [S070 preprint p. 20].
- Step 3: exit codes cited page by page: ifail=5 (trust region shrinking to zero, often wrong gradients) and ifail=4 (CQ failure) [S199 p. 14]; infeasibility reported as a local minimum of the violation [S199 p. 4]. Step 4 cites catalog V4.

### Before T3.6 (moved verbatim)

**Method 6: Read the solver's numbers, then fix the formulation before the method**

**One line**: Modelling decides what can be solved: prefer linear over convex over nonconvex, and when a solver struggles read its log before blaming nonconvexity or the algorithm; often a CQ fails or an iterate cannot be evaluated.

**Evidence**:
- Stated: B1, B11, B12 [02 §0]; "We prefer linear over convex over nonconvex formulations." (2013, 2018); "Linearize, linearize, linearize as much as possible" [02 §4.1]; "In many practical instances, the MINLP solvers fail, because the nonlinear solver generates an iterate at which the nonlinear functions cannot be evaluated." [02 §4.2]
- Practice: MPEC slacks: "The use of slacks in (3.9) is critical for the convergence of SQP methods." [02 §4.2], adopted by others [05 §4.1]; thermal insulation re-modelled from black box to smooth MINLP (doi:10.1007/s11081-010-9109-z) [02 §3.8]; formulation variants kept [03 E16, E21].
- Say–do consistency: ✅ stated + practised.

**Steps**:
1. Rank candidate formulations: linear, then convex, then nonconvex.
2. Plot every suspicious nonlinear term, ask what the modeller meant, model it as MIP if you can [02 §1.10].
3. Read the iteration log: slow linear convergence after good progress points to a CQ failure ("the nonlinear optimization for solvers failed because you can show that this formulation here violates a constraint qualification", 2024, ASR) [02 §4.3]; a KKT error that stalls warns about surrogates used outside their data.
4. Check that every iterate can be evaluated (domains, roots, logs, simulators).
5. Repair the formulation (slacks for complementarity, disaggregation, no categorical variables); keep old and new versions (Method 4 step 3).
6. Only then change the algorithm.

**Applies to stage**: diagnosis, problem choice.

**Different from standard practice**: the solver log is primary evidence and the formulation the first suspect.

**Limitations**: the least exclusive of the six (Grossmann and Misener also stress formulation); step 3 and the ordering are his. The ordering rests on the 2012-era MILP vs NLP maturity gap [02 §4.1]; re-test it with today's global and conic solvers.

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Method 6: Read the solver's numbers, then fix the formulation before the method**

**Evidence** (full evidence: references/research/09-evidence-ledger.md#method-6):
- Say–do: ✅ stated + practised; full texts: 85 cards (77 / 8 / 0).
- Variants/corrections:
  - ✗ Correction: the ordering is a default, not a law: a nonconvex form beat the convexified one [S016 pp. 67, 81]; convex big-M and hull forms ran about 100 and 375 times slower than nonconvex forms under nonlinear B&B (one instance, a three-story frame) [S070 preprint p. 20].

**Steps**:
3. Read the iteration log: slow linear convergence after good progress points to a CQ failure ("the nonlinear optimization for solvers failed because you can show that this formulation here violates a constraint qualification", 2024, ASR) [02 §4.3]; a stalled KKT error warns about surrogates outside their data; exit codes carry diagnoses: "We note also that ifail=5, the trust-region converging to zero, frequently occurs if the gradients are wrong." [S199 p. 14]; ifail=4 flags CQ failure [S199 p. 14]; infeasibility comes back as a local minimizer of the violation [S199 p. 4].

### Review fixes (T3.7)

- Variant bullet: "than nonconvex forms" is back, so the 100 and 375 times compare the convex big-M and hull forms with the nonconvex SOS and equality forms, as in the Full-text evidence above [S070 preprint p. 20].

<a id="method-7"></a>

## Method 7: Certify the notion you claim: grade every method by it, print what is not certified

New in T3.6, promoted from the full texts. SKILL.md carries the one line, Stated [S126 p. 3] with belief B14 [02 §1.5], Practice [S042 p. 10; S126 pp. 9, 16–17, 34, 40; S031 pp. 12–15], the say–do line, two variant bullets and six steps. Everything below is the promotion as written in 08 §4, copied verbatim.

### Promotion table (08 §4)

The skill has six core methods; one promotion keeps it within 3–7. Each cluster below with three or more full or partial cards was put through the four checks (1 recurrence across projects or periods, 2 say–do, 3 executable and different from common practice, 4 exclusivity).

| Cluster | Distinct cards | 1 | 2 | 3 | 4 | Decision |
|---|---|---|---|---|---|---|
| Certify the notion you claim, grade everyone by it, print what is not certified | 25 | ✅ | ✅ | ✅ | ✅ | **Promote: Method 7** |
| Price the inner re-solve before designing the outer loop | 6 | ✅ | ✅ | ✅ | ✅ within Method 1 | Evidence + step for Method 1 (no duplicate method) |
| Replace a hand-set parameter by an acceptance test or a radius | 8 | ✅ | ✅ | ✅ | ⚠ filter school | Practice note for Method 2 |
| Control run before attributing a failure | 5 (4 projects) | ✅ | ⚠ | ✅ | ⚠ | Step for Method 6 |
| Proof inheritance through a preserved invariant | 9 | ✅ | ✅ | ✅ | ✗ common mathematical practice | Evidence + sharpening for Heuristic 5 |
| Strip what the proof did not use; prove the plain core | 6 | ✅ | ✅ | ✅ | ⚠ | Extension of Heuristic 3 |
| Coarse-to-fine and model separate from discretization | 12 | ✅ | ⚠ | ✅ | ✗ | New heuristic H11 |
| One computed example per technique; a running example | 7 | ✅ | ✅ | ✅ | ✗ | New heuristic H12 |
| Relax, round with structure, improve locally | 7 | ✅ | ✗ | ✗ field standard | ✗ | Candidate pool |
| Relaxation strength by set equivalence plus a witness | 3 | ✅ | ✗ | ✗ field standard | ✗ | Candidate pool; technique inventory |

### Method 7 as proposed (08 §4, verbatim)

**Method 7 (proposed): Certify the notion you claim, grade every method by it, and print what is not certified** (08)

**One line.** Decide which stationarity or optimality notion the user actually needs, design the method so that its termination certifies that notion, judge every competitor by the same certificate, and say in print what the output does not certify.

**Evidence (25 cards, 1999–2026).**
- MPEC line: weaker stationarity notions are rejected because they admit first-order descent directions [S042 pp. 5–7; S069 preprint p. 3; S126 p. 3]; the LPEC whose zero step is exactly B-stationarity becomes the subproblem [S042 p. 10; S126 pp. 9, 16–17]; finite termination either finds descent or certifies B-stationarity [S069 preprint p. 16]; an implementation convention at the kink makes KKT points of each reformulation equal strong stationarity, and a bounded multiplier is reported per instance as a certificate [S022 pp. 9, 12, 27]; a survey is organized by the notion each method class guarantees [S034 pp. 10–16]; a two-variable example is the stated reason to design with linear models [S092 pp. 6–9]; the first survey closes on which notion is not yet guaranteed [S057 p. 18].
- Beyond MPECs: a local NLP answer to a VaR problem is certified globally optimal by six LPs, and the paper says robust NLP solvers still need such a proof [S031 pp. 12–15, 18]; termination is classified by kind of point reached [S074 pp. 14–15; S119 pp. 4, 18]; surveys value methods for the certificates they carry and say, for each reformulation, what a solution or an infeasibility certifies [S002 p. 93; S021 TR pp. 13–14]; a stationarity notion that means something in infinite dimensions is defined before convergence is claimed [S065 p. 4]; stationarity of a nonsmooth embedded model is proved equal to MPCC strong stationarity before formulations are compared [S064 pp. 13, 16]; every lower bound carries an a priori certificate whose weakness on coarse meshes is stated [S096 arXiv pp. 16–19, 29, 32]; a graded guarantee says what is still delivered when inner optimality cannot be certified [S099 preprint pp. 12–14]; only the items above a monotone bound are reported as certified [S153 p. 9]; global optimality is the selling point, not speed [S094 arXiv pp. 2, 18].
- Printing what is not certified: the residual gap of his own Benders theorem [S055 p. 10]; which assumption could be dropped and what is lost [S007 p. 22]; the untreated restoration case [S126 p. 25]; a broken proof step repaired in print by an explicit added hypothesis [S162 pp. 1–2]; the caveat that the control sequence is not even shown to be Cauchy [S091 p. 3]; heuristics labelled as such [S085 pp. 5, 19; S128 p. 12; S135 pp. 8, 11].

**Four checks.**
1. *Recurrence.* The MPEC line from 2003 to 2026 [S057; S022; S042; S069; S034; S092; S126], plus risk management in 2004 [S031], NLP solver design in 2010 and 2026 [S074; S119], surveys in 2013 and 2020 [S002; S021], power systems and quantum chemistry in 2021 [S099; S153], ML surrogates and integer control in function space in 2022 and 2026 [S064; S065; S096]: unrelated projects across 1999–2026. The 2014–2019 applied period has no carded instance. ✅
2. *Say–do.* Stated: belief B14 (three occasions, 1993–2026) [02 §1.5], restated in the papers [S031 p. 18; S069 preprint p. 3; S126 p. 3; S092 p. 7]. Practised: the subproblem design [S042 p. 10; S126 pp. 9–17] and the post-hoc grading of competitors [S126 pp. 34, 40]. ✅
3. *Executable and different.* The steps below change what is built and measured. The usual alternative, stopping at whatever point the solver returns and counting a benchmark success by solver status, is this synthesis's judgement of common practice, not a card finding; the cards show the alternatives he argues against [S069 preprint p. 3; S126 pp. 3, 34]. ✅
4. *Exclusivity.* Not all good researchers do this: several MPEC method classes can stop at C- or M-stationary points that admit descent [S069 preprint p. 3; S126 p. 3], and grading competitors post hoc by one certificate is unusual (judgement). Shared with the LPEC-based MPEC family he helped build [S126 p. 4] and with exact-certificate work elsewhere in optimization; the combination of certificate design, post-hoc grading and printed non-coverage is distinctive. ✅ (partial overlap stated)

**Steps (proposed).**
1. Name the notion the user needs (global optimum; B- versus C- or M-stationarity; KKT versus Fritz John versus infeasible stationary). Audit the notions in use with two-variable examples and keep one that excludes first-order descent [S042 pp. 5–7; S092 pp. 6–7].
2. Make termination certify it: choose the subproblem whose trivial solution is that notion [S042 p. 10; S126 pp. 9, 16–17], or the convention that makes the reformulation's KKT points equal it [S022 pp. 9, 12]. Let the combinatorial model choose only the branch and accept only points the NLP solver produces with decrease [S126 pp. 4, 11].
3. Report the kind of point reached as distinct outcomes [S074 pp. 14–15; S119 pp. 18–19].
4. When a local answer matters, build the smallest proof that certifies it, or certify the part you can [S031 pp. 12–15; S153 p. 9; S099 preprint pp. 12–14].
5. Grade every competitor by the same certificate after the run, with the checking procedure in an appendix and its cost not charged to them [S126 pp. 34, 40]; write a remark separating your certificate from the neighbouring class's [S126 pp. 17–18].
6. Print what is not certified: untreated cases, the residual gap, assumptions that could be dropped and at what cost, where the certificate is too weak; repair broken guarantees in print with the added hypothesis [S126 p. 25; S055 p. 10; S007 p. 22; S096 arXiv p. 32; S162 pp. 1–2].

**Applies to stage.** Idea generation, experiment design, judging results (Workflow E step 4 would point here instead of only to Taste 3).

**Limitations.** Local notions only: MPECopt certifies B-stationarity, not global optimality, even where the MINLP relaxation is convex [S126 p. 18]; certification can be expensive (LPECs with exponential worst case [S126 p. 15]; the VaR proof tree is shown on one example [S031 p. 13]); a priori certificates help only on fine meshes with well-estimated constants [S096 arXiv p. 32]. In the 2017–2025 applied collaborations several methods ship with the proof deferred or as labelled heuristics [S045 p. 7; S066 p. 9; S093 pp. 16, 31; S123 arXiv p. 22; S128 p. 12; S135 pp. 8, 11]; there step 6 survives and steps 2–5 do not.

**Relation to the skill.** Taste 3 stays as the judgement; Method 7 gives it steps. No existing method is replaced.

**Review note (T3.6 fix).** Two qualifications entered SKILL.md after review. (1) Say–do: belief B14's 1993 and 2026 instances ask for a convergence argument at all, not for the notion that termination certifies [02 §1.5]; the direct statements are co-signed papers [S126 p. 3; S031 p. 18; S069 preprint p. 3]. In his own 2017 essay, reliable NLP solvers stay the best approach for MPECs despite spurious stationary points, and SLPEC is used where they fail [H004 p. 9]; SKILL.md records this as a contradiction: certification governs method design, not every solve. (2) Grading competitors post hoc by one certificate rests on one work so far [S126 pp. 34, 40]. For integer controls in function space, the notions are r-optimality and L-stationarity, with an a posteriori r-optimality check [S065 pp. 4, 12, 23–25].

### Added in T3.6

- **Quotes used in SKILL.md and in this section** (all copied from cards that copied them verbatim): "Weaker stationarity notions exist, but most allow first-order descent directions, making them too weak as practical stopping criteria [46]." [S126 p. 3]; "while the NLP solvers are generally very robust, one still requires a proof such as the one given in Subsection 5.2 to ascertain the quality of the solutions they produce." [S031 p. 18]; "To our knowledge, this algorithm is the only one that guarantees global convergence to B-stationary points." [S034 p. 16]; "This example is a reason for developing our approach using sequential linear models rather than a sequential quadratic approach, which would suffer from the same behavior as an SQP approach." [S092 p. 7]; "In summary, Algorithm 1 is not a MINLP algorithm; rather, it employs MILP solvers as a tool for solving LPECs." [S126 p. 18]; "We present our work with the caveat that we do not prove ultimate convergence of the control sequence and that we do not even guarantee that it is a Cauchy sequence." [S091 p. 3].
- **Variant cards (6)**: applied collaborations that ship labelled heuristics or defer the proof [S045 p. 7; S066 p. 9; S093 pp. 16, 31; S123 arXiv p. 22; S128 p. 12; S135 pp. 8, 11]; "Third, while the numerical results indicate good performance of the optimization approach, there are no global optimality guarantees." [S123 arXiv p. 22].
- **Where SKILL.md uses it**: Taste quick-check (last question), warning sign 4, Research Task Routing (MPEC and judging rows), Agentic Protocol rows C and E/B, Workflows B step 5, C step 5 and E step 4, the anti-pattern "Stopping at a point that admits descent", the Roundtable Card, the B-stationarity anatomy, and the inner tension "Certify vs ship".
- **Steps in SKILL.md**: the six proposed steps, shortened; catalog entries D5, D6, P8, P16, V5, V8, W7, W8. Step 3 keeps the outcome taxonomy [S074 pp. 14–15; S119 pp. 18–19] in the catalog (P8).

### Review fixes (T3.6)

- Stated reworded to co-signed papers [S126 arXiv p. 3; S031 p. 18; S069 preprint p. 3] and the 2024 lecture (ASR) [02 §1.5]. The belief B14 date span (1993–2026) is dropped: its 1993 and 2026 instances ask for a convergence argument at all, not for the stationarity notion that termination certifies [02 §1.5].
- Contradiction added (his own voice, 2017): "In my opinion, reliable NLP solvers are still the best approach for solving MPECs despite the potential problems with slow convergence or convergence to spurious stationary points." [H004 p. 9]; SLPEC with a three-dimensional filter is used where they fail [H004 p. 9]. Certification governs method design, not every solve.
- Say–do split: 25 evidence cards (the 08 §4 list), 6 variant cards [S045 p. 7; S066 p. 9; S093 pp. 16, 31; S123 arXiv p. 22; S128 p. 12; S135 pp. 8, 11], 1 contradiction [H004 p. 9]; S128 and S135 appear in both lists. Grading competitors post hoc by one certificate rests on one work so far [S126 arXiv pp. 17–18, 34, 40], first author Nurkanović. Exclusivity: shared with the LPEC-based MPEC family [S126 arXiv p. 4] and, for global optimality, with global solvers [08 §4].
- Variant bullet: S045 (facility-led, Leyffer fifth author; share not identifiable [08 §9]) is replaced in SKILL.md by S123 (Attia first author): "Third, while the numerical results indicate good performance of the optimization approach, there are no global optimality guarantees." [S123 arXiv p. 22].
- Integer controls (S065, Leyffer and Manns): r-optimality, best within an L1 ball of radius r (Definition 2.8) [S065 p. 4]; L-stationarity (Theorem 4.14) [S065 p. 12]; TR-optimality not shown to be necessary, because Cauchy points for the subproblem could not be constructed (Remark 4.15) [S065 p. 12]; an a posteriori r-optimality check that re-solves the MINLP in a small L1 ball and clips the relative gap at the solver tolerance [S065 pp. 23–25] (catalog V7). Added to steps 1, 4 and 6.
- Limitations: the LPEC cost is stated both ways: worst case exponential [S126 arXiv p. 15], but on MacMPEC with early termination only LPs were needed, and in Phase I on the synthetic set a single LP always sufficed [S126 arXiv pp. 34–37]; the VaR certificate is one illustrative example and its lower bounding is problem dependent [S031 pp. 13, 18].
- Different from standard practice: "his papers" became "co-signed papers" [S069 preprint p. 3; S126 arXiv pp. 3, 34].

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Method 7: Certify the notion you claim: grade every method by it, print what is not certified**

**One line**: Decide which stationarity or optimality notion the user needs, design the method so that its termination certifies that notion, judge every competitor by the same certificate, and say in print what the output does not certify.

**Evidence** (full evidence: references/research/09-evidence-ledger.md#method-7):
- Stated (co-signed papers): "Weaker stationarity notions exist, but most allow first-order descent directions, making them too weak as practical stopping criteria [46]." [S126 arXiv p. 3]; also [S031 p. 18; S069 preprint p. 3]; on meaningless stationarity, a 2024 lecture (ASR) [02 §1.5].
- Say–do: ✅ co-signed statements + practised; promoted from the full texts: 25 evidence cards, 1999–2026; 6 variant cards (two also evidence); 1 contradiction (H004). Grading competitors by one certificate rests on one work so far (S126, first author Nurkanović). Exclusivity partial: shared with the LPEC-based MPEC family [S126 arXiv p. 4] and, for global optimality, with global solvers; distinctive here: local stationarity certificates, post-hoc grading, printed non-coverage [08 §4].
- Variants/corrections:
  - ✗ Contradiction (his own voice, 2017): "reliable NLP solvers are still the best approach for solving MPECs" despite convergence to spurious stationary points; SLPEC only where they fail [H004 p. 9]: certification governs method design, not every solve.

**Steps**:
2. Make termination certify it: choose the subproblem whose trivial solution is that notion [S042 p. 10], or the convention that makes the reformulation's KKT points equal it [S022 pp. 9, 12]; let the model choose only the branch and the NLP solver the point [S126 arXiv pp. 4, 11] (D5, D6).
4. When a local answer matters, build the smallest proof that certifies it, or certify the part you can [S031 pp. 12–15; S099 preprint pp. 12–14] (P16); for an integer control, re-solve the MINLP restricted to a small L1 ball around the returned control and report the relative gap, clipped at the solver tolerance [S065 pp. 23–25] (V7).

**Different from standard practice**: the common alternative stops wherever the solver stops and counts success by solver status (this skill's judgement, not a card finding); co-signed papers argue against it [S069 preprint p. 3; S126 arXiv pp. 3, 34].

**Limitations**: local notions; the LPEC worst case is exponential, though with early termination MacMPEC needed only LPs [S126 arXiv pp. 15, 34–35]; the VaR certificate is shown on one example, with problem-dependent lower bounds [S031 pp. 13, 18]; a priori certificates help only on fine meshes [S096 arXiv p. 32]. No talk or essay states it as a method.

### Review fixes (T3.7)

- Say–do: back in SKILL.md are "first author Nurkanović" and the distinctive part of the method, "local stationarity certificates, post-hoc grading, printed non-coverage" [08 §4]; what it shares with the LPEC-based MPEC family [S126 arXiv p. 4] stays under Review fixes (T3.6) above.

<a id="heuristic-1"></a>

## Heuristic 1: Ablate from a plain baseline, one feature at a time

### Full-text evidence (08 §2, heuristics table)

| Heuristic | Cards mentioning it | Update |
|---|---|---|
| H1 Ablate from a plain baseline | S015, S028, S032 (+ S012, S010) | Evidence: an ablation ladder of named builds [S015 pp. 9, 12–25]; heuristics off and solver revision recorded [S028 TR p. 5]; components added one at a time [S032 TR pp. 19, 24–27]; a simple base solver chosen on purpose [S012 p. 20]; a three-arm branching study [S010 pp. 9–10] |

### Added in T3.6

SKILL.md adds the full-text evidence [S015 pp. 9, 12–25] and catalog entry V12; the FilMINT quote is kept below. Further evidence [S028 TR p. 5; S032 TR pp. 19, 24–27; S012 p. 20; S010 pp. 9–10].

### Before T3.6 (moved verbatim)

1. **Ablate from a plain baseline, one feature at a time**, confounders off, code revision recorded. Case: "By turning on each feature individually, we obtain an indication of which MILP techniques have the biggest impact." (FilMINT) [03 E25, E26].

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Research Heuristics (section text)**

Ten heuristics, the framework's cap; the full texts add a coarse-to-fine clause to Heuristic 8 and a drafting practice to the Stages table [08 §5]. Evidence: ledger `references/research/09-evidence-ledger.md#heuristic-1` to `#heuristic-10`; the two full-text items: `#heuristic-11`, `#heuristic-12`.

<a id="heuristic-2"></a>

## Heuristic 2: Prototype up a ladder of tiny classics

### Full-text evidence (08 §2, heuristics table)

| Heuristic | Cards mentioning it | Update |
|---|---|---|
| H2 Ladder of tiny classics | (none by name) | Weak evidence: validate on the univariate case before scaling [S061 p. 10]; seed a class with one tiny reproducible instance [S112 p. 2] |

### Added in T3.6

Weak full-text evidence only: validate on the univariate case before scaling [S061 p. 10]; seed a class with one tiny reproducible instance [S112 p. 2].

### Before T3.6 (moved verbatim)

2. **Prototype up a ladder of tiny classics** (NLPs → MILPs → simple MINLPs → library), a printed check at each step, deficiencies in the README. Case: 2011 OA example; Uno commits on hs015 and synthes1-3 [03 E32, E34].

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Research Heuristics, item 2**

2. **Prototype up a ladder of tiny classics** (NLPs → MILPs → simple MINLPs → library), a printed check at each step, deficiencies in the README [03 E32, E34]. Weak in the full texts [S061 p. 10].

<a id="heuristic-3"></a>

## Heuristic 3: Numbers first, theory second

### Full-text evidence (08 §2, heuristics table)

| Heuristic | Cards mentioning it | Update |
|---|---|---|
| H3 Numbers first, theory second | S001, S019; contested by S026, S042 | Evidence [S001 pp. 2, 7, 13; S019 p. 4]. Contested side broadened: theory before any numbers in the bundle filter [S026 pp. 1–15], the MPEC filter [S042 p. 23] and FASTr, whose claims wait for experiments [S108 p. 12]. Proposed extension: after the proof, strip what it did not use [S001 p. 15; S019 p. 7]; analyse the plain core and show each optional accelerator cannot hurt [S110 pp. 5–6, 9–10; S092 p. 4; S071 pp. 12, 14]; keep a merit function as a proof-only ruler [S040 pp. 19–21] |

### Added in T3.6

SKILL.md adds the full-text evidence [S001 pp. 2, 7, 13] and the extension proposed in 08: after the proof, strip what it did not use [S001 p. 15; S019 p. 7]; analyse the plain core and show each optional accelerator cannot hurt [S110 pp. 5–6, 9–10; S092 p. 4; S071 pp. 12, 14]; keep a merit function as a proof-only ruler [S040 pp. 19–21]. Contested side broadened (08 §3.2 item 7): theory before any numbers in the bundle filter [S026 pp. 1–15], the MPEC filter [S042 p. 23] and FASTr, whose claims wait for experiments [S108 p. 12]: "of course, only thorough numerical experiments can show whether this name is justified." [S108 p. 12]

### Before T3.6 (moved verbatim)

3. **Numbers first, theory second** when an unmodified method already solves most problems: find the globalization that lets it take the full step more often, then prove it [02 §3.2]. Contested: MPEC theory before numbers; conDFO proof before prototype [06 C12; 03 E73].

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Research Heuristics, item 3**

3. **Numbers first, theory second** when an unmodified method already solves most problems: find the globalization that lets it take the full step more often, prove it, then strip what the proof did not use [02 §3.2; S001 pp. 2, 7, 13, 15]. Contested: MPEC theory, conDFO, the bundle filter and FASTr came theory first [06 C12; 03 E73; S026 pp. 1–15; S108 p. 12].

### Review fixes (T3.7)

- The contested side names its theory-first lines again (MPEC theory, conDFO, the bundle filter, FASTr) and cites [03 E73]; the card refs stay at three [S001; S026; S108].

<a id="heuristic-4"></a>

## Heuristic 4: A subproblem your method creates can be the next line

### Full-text evidence (08 §2, heuristics table)

| Heuristic | Cards mentioning it | Update |
|---|---|---|
| H4 A subproblem can be the next line | S016, S069, S143 (+ S010) | Evidence [S016 p. 16; S010 p. 1; S069 preprint p. 3; S143 pp. 4–5] |

### Added in T3.6

Full-text evidence [S016 p. 16; S010 p. 1; S069 preprint p. 3; S143 pp. 4–5].

### Before T3.6 (moved verbatim)

4. **A subproblem your method creates can be the next line.** "The introduction of MIQP master programs in Chapter 5 caused me to become interested in MIQP problems" (1993) → SIAM J. Optim. 1998, doi:10.1137/S1052623494268455 [06 Turn B].

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Research Heuristics, item 4**

4. **A subproblem your method creates can be the next line.** "The introduction of MIQP master programs in Chapter 5 caused me to become interested in MIQP problems" (1993) → doi:10.1137/S1052623494268455 [06 Turn B; S016 p. 16]; LPCCs from the MPEC filter [S069 preprint p. 3].

### Review fixes (T3.7)

- The 1993 thesis sentence is quoted again in place of the T3.7 paraphrase (the thesis's MIQP masters led to MIQP branch-and-bound) [06 Turn B; S016 p. 16].

<a id="heuristic-5"></a>

## Heuristic 5: Transfer and combine proofs; state novelty as the gap a known area leaves

### Full-text evidence (08 §2, heuristics table)

| Heuristic | Cards mentioning it | Update |
|---|---|---|
| H5 Transfer and combine proofs | S007, S012, S040, S091, S114 | Evidence plus sharpening: put the change where the analysed invariant survives [S003 p. 14; S009 p. 7; S101 pp. 4–5]; find the parameter setting of an analysed method that reduces to yours [S114 arXiv p. 11; S040 p. 12]; map KKT points between regularizations [S012 pp. 12–14]; reduce a new update to a classical one by a shift [H014 pp. 4–5; S121 arXiv p. 7]; one proof with a case per cut type [S169 p. 15] |

### Added in T3.6

Sharpened (08 §2): put the change where the analysed invariant survives [S003 p. 14; S009 p. 7; S101 pp. 4–5]; find the parameter setting of an analysed method that reduces to yours [S114 arXiv p. 11; S040 p. 12]: "We can now interpret the funnel as a filter with a single entry, NF = 1, that corresponds to the upper bound on the constraint violation, and we update this upper bound on h-type iterations." [S114 arXiv p. 11]; map KKT points between regularizations [S012 pp. 12–14]; reduce a new update to a classical one by a shift [H014 pp. 4–5; S121 arXiv p. 7]; one proof with a case per cut type [S169 p. 15]. Promoting proof inheritance to a core method was rejected: exclusivity fails [08 §10 item 4].

### Before T3.6 (moved verbatim)

5. **Transfer and combine proofs; state novelty as the gap a known area leaves.** "Transfer as much of the proofs from the DFO paper and the filter paper." (2026) [02 §3.7].

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Research Heuristics, item 5**

5. **Transfer and combine proofs; state novelty as the gap a known area leaves.** "Transfer as much of the proofs from the DFO paper and the filter paper." (2026) [02 §3.7]; put the change where the analysed invariant survives [S003 p. 14; S009 p. 7] (P4).

<a id="heuristic-6"></a>

## Heuristic 6: (2026, era-bound) Write the brief yourself; let agents draft and attack

### Full-text evidence (08 §2, heuristics table)

| Heuristic | Cards mentioning it | Update |
|---|---|---|
| H6 Agents draft, you write the brief (2026) | none | No card evidence (outside the carded works) |

### Added in T3.6

No card evidence (outside the carded works). SKILL.md shortened the agent-written quote; it is kept below.

### Before T3.6 (moved verbatim)

6. **(2026, era-bound) Write the brief yourself; let agents draft and attack.** Purpose, two key references, novelty, numbered choices, proof outline; dated logbook and status file; "single-agent findings were treated as claims to verify, not facts." (agent-written) [03 E71, E72].

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Research Heuristics, item 6**

6. **(2026, era-bound) Write the brief yourself; let agents draft and attack.** Purpose, two key references, novelty, numbered choices, proof outline; dated logbook; agent findings treated as claims to verify [03 E71, E72]. No carded work bears on it.

<a id="heuristic-7"></a>

## Heuristic 7: Let the downstream use choose the upstream research

### Full-text evidence (08 §2, heuristics table)

| Heuristic | Cards mentioning it | Update |
|---|---|---|
| H7 Downstream use chooses upstream research | S002, S028, S039, S049, S053, S071, S077, S108, S110 | Evidence [S039 p. 5; S077 p. 2; S108 p. 4; S110 pp. 2, 7; S049 pp. 4–5; S028 TR pp. 4, 14] |

### Added in T3.6

Full-text evidence [S039 p. 5; S077 p. 2; S108 p. 4; S110 pp. 2, 7; S049 pp. 4–5; S028 TR pp. 4, 14]: "The Achilles’ heel of interior-point methods is the lack of efficient warm-start strategies." [S110 p. 2]

### Before T3.6 (moved verbatim)

7. **Let the downstream use choose the upstream research.** Ask what the B&B tree needs from the inner solver (warm starts, infeasibility detection) [02 §2.2]. Premise contested by Bonami et al. 2005 [05 §2.1].

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Research Heuristics, item 7**

7. **Let the downstream use choose the upstream research**: what the B&B tree needs from the inner solver (warm starts, infeasibility detection) [02 §2.2; S077 p. 2; S110 pp. 2, 7]. Premise contested by Bonami et al. 2005 [05 §2.1].

<a id="heuristic-8"></a>

## Heuristic 8: Do the brute-force arithmetic first

### Full-text evidence (08 §2, heuristics table)

| Heuristic | Cards mentioning it | Update |
|---|---|---|
| H8 Brute-force arithmetic first; function space first | S096, S091, S065, S073, S102, S144, S150, S047, H001 | Evidence [S096 arXiv pp. 7–8, 29, 32; S091 p. 42; S065 pp. 2, 22; S144 pp. 16–17; S150 p. 22]. Variant: the 2015 MIPDECO abstract discretizes first [S112 pp. 1–2] |

### Added in T3.6

Full-text evidence [S096 arXiv pp. 7–8, 29, 32; S091 p. 42; S065 pp. 2, 22; S144 pp. 16–17; S150 p. 22]; variant: the 2015 MIPDECO abstract discretizes first [S112 pp. 1–2].

### Review fixes (T3.6)

- The coarse-to-fine heuristic (#heuristic-11 below) is folded into Heuristic 8 as a clause, with its caveat: team papers led by others, the team's record, not his stated rule, function space first [02 §1.7]; say–do ⚠ [08 §5] [S116 p. 5; S145 arXiv pp. 11, 16; S150 pp. 21–23]. Reason: research-extraction-framework §三 caps the heuristic tier at 10.

### Before T3.6 (moved verbatim)

8. **Do the brute-force arithmetic first.** If it exceeds the age of the universe, do analysis (function space first, discretize second) [02 §1.7]; Bonmin and Minotaur fail on 256 × 128 meshes (2019) [05 §2.4].

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Research Heuristics, item 8**

8. **Do the brute-force arithmetic first.** If it exceeds the age of the universe, analyse (function space first) [02 §1.7; S096 arXiv pp. 7–8, 29]; Bonmin and Minotaur fail on 256 × 128 meshes [05 §2.4]. The 2015 MIPDECO abstract discretizes first [S112 pp. 1–2]. Team papers led by others add a coarse-to-fine clause: keep the model separate from its discretization, relax on a coarse grid, round or warm-start on finer ones, report mesh dependence [S116 p. 5; S145 arXiv pp. 11, 16; S150 pp. 21–23] (D12); that is the team's record, not his stated rule (function space first), so say–do ⚠ [08 §5]; not exclusive.

### Review fixes (T3.7)

- The variant from a Leyffer-coauthored text is back in SKILL.md: the 2015 MIPDECO abstract discretizes first [S112 pp. 1–2]. The coarse-to-fine clause keeps both of its cards, because they support different halves: relax coarse and round finer [S145 arXiv pp. 11, 16], warm-start finer and report the falling iteration count [S150 pp. 21–23]. Heuristic 8 therefore carries four card refs, one more than T3.7 allowed per heuristic. The clause "keep the model separate from its discretization" [S116 p. 5] and the remark "not exclusive" remain in the Before T3.7 copy above and in `#heuristic-11`.

<a id="heuristic-9"></a>

## Heuristic 9: When corrected, credit the corrector and change method rather than argue

### Full-text evidence (08 §2, heuristics table)

| Heuristic | Cards mentioning it | Update |
|---|---|---|
| H9 Credit the corrector | H004, S002, S089, S162 | Evidence [H004 pp. 4–5; S002 p. 32; S089 p. 10]; the 2026 Correction names no corrector [S162 pp. 1–2] |

### Added in T3.6

Full-text evidence [H004 pp. 4–5; S002 p. 32; S089 p. 10]; the 2026 Correction names no corrector [S162 pp. 1–2].

### Before T3.6 (moved verbatim)

9. **When corrected, credit the corrector and change method rather than argue.** "Later, Bonami et al. corrected our convergence proof" (2017) [02 §5.3]; the Acta survey adopts both corrections [05 §1.1, §1.2].

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Research Heuristics, item 9**

9. **When corrected, credit the corrector and change method rather than argue.** "Later, Bonami et al. corrected our convergence proof" (2017) [02 §5.3; H004 pp. 4–5; S002 p. 32]; the 2026 Correction names no corrector [S162 pp. 1–2].

<a id="heuristic-10"></a>

## Heuristic 10: Build a new evaluation tool when the standard one cannot answer your question

### Full-text evidence (08 §2, heuristics table)

| Heuristic | Cards mentioning it | Update |
|---|---|---|
| H10 Build a new evaluation tool | S049, H014, S121, S126, S136 | Evidence [S049 pp. 11–12; H014 pp. 14–15; S126 pp. 33–37]; also theory-quantity profiles [S020 p. 13; S013 TR pp. 13–15; S088 pp. 22–24] and safeguard firing counts [S001 pp. 23–24] |

### Added in T3.6

Full-text evidence [S049 pp. 11–12; H014 pp. 14–15; S126 pp. 33–37]; also theory-quantity profiles [S020 p. 13; S013 TR pp. 13–15; S088 pp. 22–24] and safeguard firing counts [S001 pp. 23–24]; catalog entries V5, V6, V14.

### Before T3.6 (moved verbatim)

10. **Build a new evaluation tool when the standard one cannot answer your question** (extended performance profiles, 2012 and 2020) [03 E08].

<a id="heuristic-11"></a>

## Heuristic 11: Keep the model separate from its discretization and solve coarse to fine

New in T3.6 (08 §5). SKILL.md condenses it to two lines with [S116 p. 5; S145 arXiv pp. 11, 16; S150 pp. 21–23] and catalog entry D12.

### Proposal (08 §5, verbatim)

**H11 (proposed): Keep the model separate from its discretization and solve coarse to fine** (08)

**Steps.** State the problem without discretization code and let the solver choose and refine the grid [S116 pp. 3, 5]; aggregate a nonlinearity over a coarse partition before relaxing it [S096 arXiv pp. 8–9]; solve the expensive relaxation on the coarsest grid and round on a finer grid where the rounding bound allows [S145 arXiv pp. 11, 16; S144 p. 18]; warm-start each finer level with interpolated controls and multipliers and report the falling iteration count [S150 pp. 11–12, 21–23; S152 pp. 5–6]; use coarse-model solutions to restrict the fine model [S043 p. 29]; before interpreting a qualitative feature, refine and switch schemes until they agree [S098 pp. 4, 13]; report a mesh-dependence table [S115 p. 17; S093 pp. 27–29]. Multilevel restriction and aggregation for MIP and SDP belong here too [S072 arXiv pp. 7–10; S185 preprint p. 5].

**Checks.** Recurrence ✅ (2010–2026, twelve cards); say–do ⚠ (the stated rule is function space first, discretize second [02 §1.7]; the papers state the separation of model and discretization [S116 p. 5]); executable and different from the MINLP default of branch and bound on the finest mesh ✅ [S084 pp. 21–24; S091 p. 42]; exclusivity ✗ (mesh sequencing and multigrid are standard; the papers name multigrid as the source [S072 arXiv p. 3]). Heuristic, linked to Heuristic 8. Mostly team papers with other first authors.

### Added in T3.6

- Quotes from the cards: "Uncluttered by any discretization code, the resulting AMPL model is easy to read, maintain, and extend." [S116 p. 5]; "Therefore, we solve the continuous relaxation using fewer time steps T and round the solutions using more time steps TR to achieve a balance between computational time and the difference between continuous and binary solutions." [S145 arXiv p. 11]; "Clearly, the “smooth” transition that we observe for larger period lengths is an artifact of the discretization." [S098 p. 13]

### Review fixes (T3.6)

- Folded into Heuristic 8 in SKILL.md (a coarse-to-fine clause with this caveat), so that the heuristic tier stays within the framework's 5–10; the evidence above is unchanged. The three works cited in SKILL.md are led by others: Kirches [S116 p. 5], Fei [S145 arXiv pp. 11, 16] and Aretz [S150 pp. 21–23]; the c16 batch header attributes their practices to the papers, not to him personally.

<a id="heuristic-12"></a>

## Heuristic 12: Show every technique on one tiny computed example; thread one running example through theory, reformulation and code

New in T3.6 (08 §5). SKILL.md condenses it to two lines with [S016 pp. 49, 62–66; S126 pp. 11–14; S021 TR pp. 11, 13, 15] and catalog entry W1; the Stages table's drafting row now names it as practice evidence (not a stated method).

### Proposal (08 §5, verbatim)

**H12 (proposed): Show every technique on one tiny computed example, and thread one running example through theory, reformulation and code** (08)

**Steps.** After each algorithm or claim, compute a small example, usually with a figure [S016 pp. 49, 62–66; S002 pp. 7, 40–41, 48–49, 76; S126 pp. 11–14, 19–20]; audit concepts on two-variable examples before using them [S042 pp. 5–7]; carry one example through theory, reformulations and software listings [S021 TR pp. 11, 13, 15, 19–20; S032 TR pp. 5, 10, 14]; seed a new class with one tiny reproducible instance, with solver, nodes and time stated [S112 p. 2].

**Checks.** Recurrence ✅ (1993–2026); say–do ✅ partial (he recalls looking at examples as a Dundee rule [H005 p. 4]; belief B4 [02 §1.2]); executable ✅; exclusivity ✗. Heuristic. It gives the "Drafting and editing papers" row of the Stages table its first practice evidence.

**Review note (T3.6 fix).** research-extraction-framework §三 caps the heuristic tier at 10, and SKILL.md already had ten. H11 is folded into Heuristic 8 as its coarse-to-fine clause, with the caveat that the cited works are team papers led by others (Kirches, Fei, Aretz) [S116 p. 5; S145 arXiv pp. 11, 16; S150 pp. 21–23]; H12 is carried by the Stages table's drafting row as practice seen in the papers (catalog W1).

### Review fixes (T3.6)

- Moved from the heuristics into the Stages table's drafting row in SKILL.md (catalog W1), labelled as practice seen in the papers with no stated method, so that the heuristic tier stays at 10; the evidence above is unchanged [S016 pp. 49, 62–66; S126 arXiv pp. 11–14; S021 TR pp. 11, 13, 15].

<a id="workflows"></a>

## Stage workflows (changes and earlier wording)

### Added in T3.6

- **Workflow A**: step 2 lists the pathologies behind the received verdict [S057 p. 15] (W4); step 3 points to Heuristics 8 and 11; step 5 seeds the library with one tiny reproducible instance [S112 p. 2].
- **Workflow B**: step 1 points to Method 1 steps 1-4 (pricing the re-solve); step 4 adds catalog entries D2 and P4; step 5 (new) asks which notion the method must certify (Method 7 steps 1-2); the old step 5 (agents) is now step 6. The output names the notion certified.
- **Workflow C**: step 2 adds catalog entry V1; step 3 a deliberately plain base solver [S012 p. 20]; step 5 grades every method by one certificate (Method 7 step 5). The checkpoint notes that the full texts show the merge of tuning and comparison sets recurring [S028 TR pp. 7, 17; S114 arXiv pp. 19–20].
- **Workflow D**: step 1 adds exit codes; step 2 now points to Method 6 step 5; step 3 (new) is the control rerun (Method 6 step 4) [S020 pp. 10–12]; old steps 3-5 are now 4-6; step 6 adds the third rule-of-thumb row [S016 p. 83]. The output adds the control rerun.
- **Workflow E**: step 1 covers benchmark failures [S022 p. 27]; step 4 points to Method 7; the claims table adds the notion certified.
- **Workflow F**: step 2 adds the erratum template [S162 pp. 1–2] (W8).
- **Stages table**: the drafting row names Heuristic 12 and the writing moves as practice evidence [S016 pp. 49, 62–66; S126 pp. 11–14].

### Review fixes (T3.6)

- Workflow A step 3 points to Heuristic 8 (with its coarse-to-fine clause) and the integer-control brief.
- Workflows C, D and E cite catalog V ids (formerly E): V1, V12, V4, V8.
- Workflow D step 6 keeps the two rows that stood before T3.6, dated as a rule of thumb to re-test against doi:10.1007/s11081-018-9411-8; the 1993 third row stays in Method 5 step 5 with its caveat [S016 pp. 78, 83; S101 p. 7].
- Stages table: the drafting row carries the former Heuristic 12 (one tiny computed example per technique; a running example) as practice seen in the papers, no stated method [S016 pp. 49, 62–66; S126 arXiv pp. 11–14; S021 TR pp. 11, 13, 15]; the table now serves the last two routing rows.

### Before T3.6 (moved verbatim)

**Stage Workflows**

**Workflow A: Problem choice**

**Input**: your base competence; a candidate class; any collaborator or facility bringing it.

**Steps**:
1. State your base in one sentence and what it can carry into the candidate (→ Method 2 steps 1-2).
2. Does the field's verdict ("unsafe", "hopeless") rest on formulation or tooling, not mathematics? (→ Taste 2, Method 6)
3. Do the brute-force arithmetic; if hopeless, plan analysis instead (→ Heuristic 8).
4. Check for a side question your own method created (→ Heuristic 4).
5. Name the class, its challenges, and start a small library (→ Method 2 step 4, Method 4).

**🔴 Checkpoint**: if the toolkit's key assumptions (CQ, exact subproblem solves, smoothness, unique state solution) cannot be checked in the new class, stop and list them first.

**Output**: one page: base → extension, received view tested, assumption list, first five instances.

**Workflow B: Idea generation**

**Input**: an existing method and its failures; a solver you can modify; existing proofs.

**Steps**:
1. List restrictions due to tooling and remove them (→ Method 1 steps 1-3).
2. Build the smallest breaking example and redesign (→ Method 3).
3. Re-cast the objects into a home class (→ Method 2 step 3).
4. Transfer proofs lemma by lemma and mark the gaps (→ Heuristic 5).
5. Era-bound variant (2026): write the brief yourself and let agents draft and attack (→ Heuristic 6).

**🔴 Checkpoint**: a gap you cannot close is written down as an open gap, not argued away [02 §3.7]; agent findings are claims to verify [03 E72].

**Output**: design note: counterexample, removed restriction, gap list.

**Workflow C: Experiment design and execution**

**Input**: the method, a library, baselines.

**Steps**:
1. Climb a ladder of tiny classics with a printed check at each step (→ Heuristic 2).
2. Self-built or same-solver baselines with a written fairness rule (→ Method 5 steps 1-2).
3. One-feature ablations from a plain baseline, confounders off, code revision recorded (→ Heuristic 1).
4. Keep several formulations of each application (→ Method 4 step 3).
5. Keep failures in the statistics with a per-instance failure taxonomy (→ Method 5 step 3).

**🔴 Checkpoint**: separate the tuning set from the comparison set before tuning defaults (inferred from the FilMINT record [03 E22]; not stated by him).

**Output**: per-instance appendix with failure codes [03 E67]; logs public where possible [03 E68].

**Workflow D: Diagnosis**

**Input**: a solver that is slow, fails, or returns doubtful points.

**Steps**:
1. Read the iteration log: rate, KKT error, restoration, evaluation errors (→ Method 6 step 3).
2. Check the formulation for CQ failure and undefined evaluations (→ Method 6 step 4).
3. Trace numerical failures to their source (reduced-Hessian round-off; shared static state in BQPD) [03 E39].
4. Watch the tree by hand when the solver abandons good subtrees; redesign the rule [03 E38]. Report bugs to the maintainer [03 E33].
5. For convex-MINLP algorithm choice: LP/NLP-based B&B by default; NLP-BB for highly nonlinear, small-gap problems (→ Method 5 step 5).

**🔴 Checkpoint**: do not blame nonconvexity or the algorithm until the formulation has been ruled out [02 §4.3].

**Output**: symptom → cause → reformulation or code fix.

**Workflow E: Judging results**

**Input**: results, the theory relied on, a draft claim.

**Steps**:
1. Check counterexamples against hypotheses before claiming an error (→ Method 3 step 3).
2. State the test-set filter and its bias; rule of thumb by class, not a winner (→ Method 5 steps 4-5).
3. Stamp comparisons with date and versions; report where your method loses (→ Method 5 steps 6-7).
4. Ask what the guarantee means for this model (→ Taste 3).

**🔴 Checkpoint**: one good example is not evidence (Warning sign 2); a claim that holds only on a library you call easy must say so [05 §4.3].

**Output**: a claims table: claim / test class / date / versions / known failures.

**Workflow F: After publication**

**Input**: published paper, library, code.

**Steps**:
1. Keep the library's dated correction log (→ Method 4 step 5).
2. Publish corrections in print when errors are found (2026 Correction) [01 F10].
3. Credit correctors by name; write the corrected statement into surveys and lectures (→ Heuristic 9).
4. Narrow claims in revision (→ Method 5 step 8).
5. Consolidate a grown line: history, survey, shared software [06 §9.4].

**🔴 Checkpoint**: if a peer's correction holds, adopt it; no public rebuttal by him has been found [05 §0].

**Output**: correction log entry, erratum, revised survey text.

**Stages without a distillable Leyffer method**

Reasons, for the last row of Research Task Routing:

| Stage | Why no Leyffer method |
|---|---|
| Literature search | Only "start with something else" (existing model libraries) [02 §4.5] |
| In-person supervision | Three thesis acknowledgements [04 §3.1]; practice shows only how juniors are brought in and credited [04 §4.5] |
| Drafting and editing papers | Only closing-slide habits and a survey scope cut [02 §6.3, §6.4] |
| Refereeing | No public reviews; no OpenReview profile [03 Gaps] |
| Leaving a line | Every exit is silent; "When to stop a line of work: no statement found." [02 §2.7] |

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Workflow A: Problem choice**

**Input**: your base competence; a candidate class; any collaborator or facility bringing it.

**Steps**:
2. Does the field's verdict ("unsafe", "hopeless") rest on formulation or tooling, not mathematics? List the pathologies it rests on; test which are harmless [S057 p. 15] (→ Taste 2, Method 6; W4).
3. Do the brute-force arithmetic; if hopeless, plan analysis instead: function space first, coarse to fine (→ Heuristic 8; integer-control brief).
5. Name the class, its challenges, and start a small library from one tiny reproducible instance [S112 p. 2] (→ Method 2 step 4, Method 4).

**Workflow B: Idea generation**

**Steps**:
4. Transfer proofs lemma by lemma and mark the gaps; change only what keeps the analysed invariant [S003 p. 14] (→ Heuristic 5; D2, P4).
6. Era-bound variant (2026): write the brief yourself and let agents draft and attack (→ Heuristic 6).

**Workflow C: Experiment design and execution**

**Steps**:
1. Climb a ladder of tiny classics with a printed check at each step (→ Heuristic 2).
5. Keep failures in the statistics with a per-instance failure taxonomy (→ Method 5 step 3); grade every method by one certificate (→ Method 7 step 5).

**🔴 Checkpoint**: separate the tuning set from the comparison set before tuning defaults (inferred from the FilMINT record [03 E22]; not stated by him). The full texts show the merge recurring [S028 TR pp. 7, 17].

**Workflow D: Diagnosis**

**Steps**:
3. Before attributing the failure, rerun the failing instances with the suspected cause removed [S020 pp. 10–12] (→ Method 6 step 4; V4).
5. Watch the tree by hand when the solver abandons good subtrees; redesign the rule [03 E38]. Report bugs to the maintainer [03 E33].
6. For convex-MINLP algorithm choice, a dated rule of thumb to re-test against doi:10.1007/s11081-018-9411-8: LP/NLP-based B&B by default; NLP-BB for highly nonlinear, small-gap problems (→ Method 5 step 5, with the 1993 third row and its caveat).

**Workflow E: Judging results**

**Steps**:
4. Ask what the guarantee means for this model: which notion is certified, and is every method graded by it [S126 arXiv pp. 34, 40]? (→ Taste 3, Method 7; V8).

**Output**: a claims table: claim / test class / date / versions / failures / notion certified.

**Workflow F: After publication**

**Steps**:
2. Publish corrections in print when errors are found (2026 Correction) [01 F10]: count the mistakes, give the mechanism, print the corrected statements [S162 pp. 1–2] (W8).

**Stages without a distillable Leyffer method**

| Stage | Why no Leyffer method |
|---|---|
| Drafting and editing papers | No stated method: only closing-slide habits and a survey scope cut [02 §6.3, §6.4]. Practice seen in the papers: show every technique on one tiny computed example and thread one running example through theory, reformulation and code [S016 pp. 49, 62–66; S126 arXiv pp. 11–14; S021 TR pp. 11, 13, 15] (W1; ledger `#heuristic-12`); writing moves W2–W11 |

### Review fixes (T3.7)

- Workflow D step 6 ends again "(→ Method 5 step 5, with the 1993 third row and its caveat)": it is the Workflow D step that correction 2 names (08 §3.2 item 2; step 5 before the T3.6 renumbering), and the routing row for convex-MINLP algorithm choice sends readers to this step alone.
- Stages table, drafting row: the running-example half of Heuristic 12 is back, "thread one running example through theory, reformulation and code" [S021 TR pp. 11, 13, 15] (10-claim-audit.md, k=12: supported).

<a id="routing"></a>

## Research task routing and agentic protocol (earlier wording)

### Added in T3.6

- Routing: Workflow D step numbers updated (the control rerun is now step 3; algorithm choice is step 6); Method 7 added to the MPEC row and to the judging row; Heuristic 11, Method 2 step 3 and the integer trust-region anatomy (`#anatomy-slip`) added to the integer-control row; the global-certificates row says "mostly outside" and cites the side work [S031 pp. 12–15; S094 arXiv pp. 2, 18]; the last row names Heuristic 12 as practice evidence for drafting.
- Agentic Protocol: row D adds exit codes and the control rerun and renumbers the formulation steps (5-6); row E, B adds the certified notion (Method 7); row C adds the common certificate.

### Review fixes (T3.6)

- MPEC row: for large MPECs violating MPEC-LICQ, plain NLP solved 16.00% of 75 generated instances, mostly 45-minute timeouts, against 94.67% for regularization and the ℓ∞ penalty and 96.16% for MPECopt; code and data public [S126 arXiv pp. 33, 36–38].
- Integer-control row: points to the new integer-control brief, Heuristic 8, Method 7 step 1 and catalog D11, D13, V7. The brief rests on [S084 pp. 5, 12–17, 20–30; S093 pp. 23–24; S065 pp. 2–3, 8, 22, 26; S091 p. 42; 05 §5.1]; the full anatomy is in the anatomy-slip section.
- Drafting has its own row (catalog W1–W11, practice seen in the papers, no stated method); the other stages without a method keep the "not Leyffer-style" label. How to Use's weak spots now point to the last three rows.

### Before T3.6 (moved verbatim)

**Research Task Routing**

| User says | Workflow | Main methods |
|---|---|---|
| "Is this problem class worth entering?" "Help me pick a topic" | Workflow A | Method 2, Method 6 + Taste quick-check |
| "How do I attack this? My algorithm needs a new idea" | Workflow B | Method 1, Method 3, Heuristic 5 |
| "Design the computational study / which baselines?" | Workflow C | Method 5, Method 4, Heuristics 1, 2 |
| "The solver stalls, fails at nodes, or returns junk" | Workflow D | Method 6, Method 1 |
| "Which convex-MINLP algorithm should I use?" | Workflow D step 5 only | Method 5 (dated rule of thumb) |
| "My MPEC / complementarity model fails in the NLP solver" | Workflow D steps 1-2, then E | Method 6 (slacks), Method 3. Contested: 2017 "reliable NLP solvers are still the best approach for solving MPECs" vs 2026 coauthored "less competitive than the MPEC-tailored methods" [05 §4.3, C8] |
| "My mixed-integer optimal control / PDE problem is too big for branch-and-bound" | Workflow A step 3, then B | Heuristic 8 [05 §2.4]; Method 2 step 5 [05 §5.2]; McCormick anatomy |
| "Is this result good? Is this theorem wrong?" | Workflow E | Method 3, Method 5 |
| "Someone found an error / how do I maintain my library?" | Workflow F | Method 4, Heuristic 9 |
| "My project is stuck", "no progress for months" | Stuck-project triage (below) | Methods 6, 3, 1 |
| Global optimality certificates, relaxation strength, conic/SDP cuts, convex hulls | Outside this lens: say so; offer only a Method 3 hypothesis check and Method 5 reporting rules; hand off to minlp-roundtable | — |
| Literature search, in-person supervision, drafting, refereeing, "should I drop this line?" | No distillable Leyffer method (Stages table); label generic advice "not Leyffer-style" | — |

**Several rows match**: take the first of D → E → B → A (formulation before theory before a new idea before a new class; inferred from the Workflow D checkpoint [02 §4.3]). One workflow per answer.

**Stuck-project triage** (no Leyffer statement on stuck projects exists [04 Gaps]; this is routing, not his advice). Ask what was tried last and what it produced, then run one workflow: solver fails or stalls → D; works on some instances only, or a proof step breaks → E step 1, Method 3; does not beat the baselines → C step 2 (is the comparison fair?), then B; the class looks hopeless → A step 3, Heuristic 4. Whether to abandon the line: no Leyffer method; his exits were silent [02 §2.7].

**Agentic Protocol**

**Step 1: Route**
Pick one routing row. A failing or slow solve with no log or model: the first next step is to obtain both (Workflow D step 1); do not diagnose without them.

**Step 2: Check only what the workflow needs (tools, never memory)**

| Workflow | Check |
|---|---|
| D | Log (Method 6 step 3): rate, KKT error trend, restoration, evaluation errors, node failures. Formulation (steps 4-5): undefined iterates, CQ failure (complementarity, perspective forms), linearizable terms, missing slacks. Then tooling (Method 1): callbacks, warm or hot starts, infeasibility certificates |
| E, B | Known worst cases (Method 3): OA worst case and exponential version (doi:10.1007/BF01581153; doi:10.1287/ijoc.1120.0545); corrected OA characterization (doi:10.1016/j.disopt.2006.10.011); CQs and cycling in OA (arXiv:2606.26897); hypotheses of the theorem relied on. B also: tooling (Method 1) |
| C | Benchmark state (Methods 4, 5): library for the class (MINLPLib, QPLIB, CUTEst, MacMPEC) with known values; dated Mittelmann page (https://plato.asu.edu/ftp/minlp.html); latest convex-MINLP comparison (doi:10.1007/s11081-018-9411-8); competitor versions |
| A | Carried-in assumptions (Method 2): CQs, exact subproblem solves, strict complementarity, unique state solvability; which are checkable on the user's instances |
| F | The library's correction log; any published erratum |

Stop checking when each item is settled or needs the user's own log, instances or code; name that item instead of searching further. Keep search notes internal.

**Step 3: Answer, then stop**
Form and order: the Answer Standard above. The text below lists what the reply must contain; the methods behind the steps are credited in the Basis footer, in words, rather than tagged inline; the workflow's name is not printed; and 🔴 is this file's mark for a workflow checkpoint, never printed in the reply.

Conclusion first → at most five numbered next steps, each labelled with its method → the workflow's 🔴 checkpoint → one limitation in the user's setting → the one item you need next from the user, if any. If the case fails a 🔴 checkpoint, stop there: say what blocks it and what would clear it.

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Research Task Routing (section text)**

| User says | Workflow | Main methods |
|---|---|---|
| "My MPEC / complementarity model fails in the NLP solver" | Workflow D steps 1-3, then E | Method 6 (slacks), Method 3, Method 7. Contested: 2017 "reliable NLP solvers are still the best approach for solving MPECs" vs 2026 coauthored "less competitive than the MPEC-tailored methods" [05 §4.3, C8]. Large MPECs violating MPEC-LICQ: plain NLP mostly timed out; regularization or MPECopt (https://github.com/nosnoc/mpecopt) [S126 arXiv pp. 33, 36–38] |
| "My mixed-integer optimal control / PDE problem is too big for branch-and-bound" | Workflow A step 3, then B | Integer-control brief (below); Heuristic 8 [05 §2.4]; Method 2 steps 3, 5 [05 §5.2]; Method 7 step 1; McCormick anatomy; catalog D11, D13, V7; ledger `#anatomy-slip` |

**Several rows match**: take the first of D → E → B → A (formulation before theory before a new idea before a new class; inferred from the Workflow D checkpoint [02 §4.3]). One workflow per answer.

**Stuck-project triage** (no Leyffer statement on stuck projects exists [04 Gaps]; this is routing, not his advice). Ask what was tried last and what it produced, then run one workflow: solver fails or stalls → D; works on some instances only, or a proof step breaks → E step 1, Method 3; does not beat the baselines → C step 2 (is the comparison fair?), then B; the class looks hopeless → A step 3, Heuristic 4. Whether to abandon the line: no Leyffer method; his exits were silent [02 §2.7].

**Integer-control brief** (team papers; full rows: ledger `#anatomy-slip`). Branch-and-bound on a fine mesh stalls: on released 2-D source-inversion instances (16 × 8 to 256 × 128) only B&B solved the two smallest meshes in 10 CPU-hours, and SCIP's presolve added 8,002 quadratic constraints to a problem that is bound-constrained once the states are eliminated [S084 pp. 5, 20–24]. Eliminate the states or superpose precomputed PDE solves [S084 p. 12; S093 pp. 23–24] (D11); add TV regularization so minimizers exist [S065 pp. 2–3]; relax, round, then improve each rounding with an integer trust region [S084 pp. 13–17, 25–30] (D13, D4). Baselines to beat: MIQP (better objectives for N ≤ 128, far slower) and CIA rounding (better at N = 64, 128) [S065 p. 22]; the authors call SLIP "computationally less attractive than the combinatorial integral decomposition" [S065 p. 26]. SLIP's theory covers d = 1 [S065 p. 8]; for d ≥ 2 no efficient subproblem solver is known [05 §5.1]; the set-space method is not competitive in topology optimization [S091 p. 42].

**Step 2: Check only what the workflow needs (tools, never memory)**

| Workflow | Check |
|---|---|
| D | Log (Method 6 step 3): rate, KKT error trend, restoration, evaluation errors, node failures, exit codes. Control rerun (step 4). Formulation (steps 5-6): undefined iterates, CQ failure (complementarity, perspective forms), linearizable terms, missing slacks. Then tooling (Method 1): callbacks, warm or hot starts, infeasibility certificates |
| E, B | Known worst cases (Method 3): OA worst case and exponential version (doi:10.1007/BF01581153; doi:10.1287/ijoc.1120.0545); corrected OA characterization (doi:10.1016/j.disopt.2006.10.011); CQs and cycling in OA (arXiv:2606.26897); hypotheses relied on; the notion certified against the one needed (Method 7). B also: tooling (Method 1) |
| C | Benchmark state (Methods 4, 5): library for the class (MINLPLib, QPLIB, CUTEst, MacMPEC) with known values; dated Mittelmann page (https://plato.asu.edu/ftp/minlp.html); latest convex-MINLP comparison (doi:10.1007/s11081-018-9411-8); competitor versions; the certificate all methods will be graded by |

### Review fixes (T3.7)

- Integer-control brief: the baselines and the authors' verdict are back verbatim, MIQP better for N ≤ 128 and CIA rounding better at N = 64, 128 [S065 p. 22], SLIP "computationally less attractive than the combinatorial integral decomposition" [S065 p. 26], and so is the set-space limit in topology optimization [S091 p. 42]. T3.7's shorter "beat MIQP and CIA rounding" read as a win that the cited page contradicts; the restored sentence is the one the claim audit had checked (10-claim-audit.md, k=1: supported).
- MPEC row: the contest over plain NLP as the default is placed within his own record (2017 essay vs 2026 coauthored benchmark) [05 §4.3, C8]; the two quotes stay in the Before T3.7 copy above.
- Agentic Protocol, row D: "CQ failure (complementarity, perspective forms)" is back, with its two places to look.

<a id="how-to-use"></a>

## How to Use and frontmatter (earlier wording)

### Added in T3.6

- Frontmatter: `researched:` set to 2026-11-19; the description names seven methods and the full-text basis (923 characters; the parenthetical list of algorithm acronyms was dropped, and "global certificates" left the not-for list per correction 7).
- How to Use: strengths add "deciding which stationarity notion a method must certify"; domain fit names Methods 3, 5 and 7; the citations paragraph explains card citations, version words, the ledger and the technique catalog.
- Activation Rules: only the first-activation disclaimer line changed (coverage numbers); the roundtable rule "no paper cards yet" is kept verbatim and marked obsolete in the corrections (SKILL.md item 11; 08 §3.2 item 13). After T3.6 (2026-11-19) the operator rewrote that Activation Rules line to cite paper cards first, then dropped item 11 and the Roundtable Card's obsolete-rule sentence.

### Review fixes (T3.6)

- The citations paragraph names the unmarked works read in a report, preprint or arXiv version (S001, S003, S009, S015; S031, S065, S119), marks S126 and D001 as arXiv in SKILL.md, separates note-03 items (E01–E73) from the catalog's evaluation protocols (now V1–V16), defines the marks (⚠ variant; ✗ correction or contradiction, the word after the mark says which) and points to the how-to-use and routing sections here.
- The first-activation disclaimer says "155 of the 211 works indexed under his name", with 7 skipped as not his or not research (this member's team_status.py coverage row).

### Before T3.6 (moved verbatim)

**Frontmatter description before T3.6**

description: |
  Sven Leyffer's research craft in mixed-integer nonlinear optimization, distilled from his public papers, reports, solver manuals, test libraries, lectures and peers' corrections. Six methods: own the solver and integrate at the iteration level; carry the home NLP toolkit into each new problem class; counterexample discipline; the test library as a maintained instrument; calibrated claims on fairness-stated baselines; read the solver log and fix the formulation before the method. Use it to choose, design, debug, benchmark and judge work on convex-MINLP algorithms (OA, NLP-BB, LP/NLP-BB), NLP subsolvers failing at tree nodes, MPECs, and mixed-integer optimal control or PDE-constrained optimization. Triggers: "Leyffer lens", "Leyffer perspective", "what would Leyffer say", "how would Leyffer approach this", "use Leyffer's method", "Leyffer.skill", "用Leyffer的视角". Also loaded by minlp-roundtable. Not for general questions, global certificates or relaxation theory (other MINLP Team members).

**How to Use**

**Strengths** (stages with evidence): choosing a class by what a reliable NLP toolkit can carry into it; designing algorithms from inside a solver you can modify; breaking a method with the smallest counterexample; diagnosing a failing solve from the log and the formulation; building and correcting test libraries; fair, dated benchmark claims; public correction of published work.

**Weak spots**: see the last two rows of Research Task Routing and the Stages table at the end of Stage Workflows.

**Domain fit**: local, NLP-solver-centred MINLP. For global or relaxation-theory users, Methods 3 and 5 transfer; Method 2's "base" may be a relaxation family; re-test Method 6's ordering on today's solvers.

**Citations**: `[02 §1.2]` = note 02, section 1.2: [01 publications](01-publications.md), [02 methodology](02-methodology.md), [03 process evidence](03-process-evidence.md), [04 mentorship](04-mentorship.md), [05 peer critique](05-peer-critique.md), [06 trajectory](06-trajectory.md). B = note 02 beliefs; E = note 03 evidence items; Turns = note 06. **Stated** = he said or co-signed it; **practice** = the record shows it; **inferred** = this skill's reading. (ASR) = YouTube auto-caption, wording approximate; (AI-assisted) = 2026 repository text written with an AI assistant. Most papers are co-authored; a practice in a team paper belongs to the team.

<a id="anatomy-oa"></a>

## Anatomy: Solving mixed integer nonlinear programs by outer approximation (Fletcher and Leyffer, Math. Program. 66, 1994, doi:10.1007/BF01581153)

### Full rows in SKILL.md after T3.6

**Solving mixed integer nonlinear programs by outer approximation (Fletcher and Leyffer, Math. Program. 66, 1994, doi:10.1007/BF01581153)**

Read: the 1996 Dundee version [S003] and the thesis [S016]. Full rows: references/research/09-evidence-ledger.md#anatomy-oa.

| Dimension | Content |
|---|---|
| Origin | "we generalized outer approximation by Duran and Grossmann" (2017) [01 S1]; Duran-Grossmann OA needed problems linear in y, and its master was wrong for infeasible subproblems [S003 pp. 2, 6]; who proposed it: unknown |
| Why then | Inferred: Fletcher's phase I and exact-penalty toolbox fit [S003 pp. 4–5] |
| Key insight | Treat nonlinearities in the integer variables directly; cut infeasible y at the phase I point [S003 pp. 4–5] |
| Minimum evidence | A two-point counterexample and a worst case visiting every integer point [S003 pp. 8, 12–13]; thesis "Rule of Thumb" over five codes [S016 pp. 77–83]. Journal numerics: not read |
| Abandoned paths | Worst case → quadratic OA, which loses the lower bound [S003 p. 14]; own Lagrangean variant dropped [03 E47] |
| Reception | Corrected characterization (doi:10.1016/j.disopt.2006.10.011); exponential worst case (doi:10.1287/ijoc.1120.0545); quadratic master criticised (doi:10.1007/s10107-018-1356-3); CQ assumptions questioned (arXiv:2606.26897) [05 §1] |
| Methods | 3, 2, 5 |

### Added in T3.6

Extra full-text detail: the master program comes from projection plus linearizations, with infeasible y cut at a weighted phase I point valid for any NLP solver [S003 pp. 4–5, 8]; finiteness by non-repetition under a CQ [S003 p. 11]; the worst case uses f(y) = (y − δ)² on a grid with δ = 2^-p [S003 pp. 12–13]; the QOA lower bound fails on −ln(x + 1) [S003 p. 14]; Benders and OA cuts compared through first-order conditions [S003 pp. 20–21]. The version read gives no numerics [S003 pp. 9, 12, 15]. Thesis: five codes with the same start and ε, a three-row Rule of Thumb [S016 pp. 77–83]. Quote: "This argument is erroneous as the following example indi ates." [S003 p. 8] (the card copies the extraction damage).

### Before T3.6 (moved verbatim)

**Solving mixed integer nonlinear programs by outer approximation (Fletcher and Leyffer, Math. Program. 66, 1994, doi:10.1007/BF01581153)**

| Dimension | Content |
|---|---|
| Origin | "we generalized outer approximation by Duran and Grossmann" (2017) [01 S1]; who proposed it: unknown |
| Why then | Inferred: OA covered MINLPs linear in the integers; Fletcher's exact-penalty toolbox fit [01 S1] |
| Key insight | Treat nonlinearities in the integer variables directly |
| Minimum evidence | A worst case visiting all integer assignments; thesis "Rule of Thumb" over five self-built methods [03 E47]. Journal numerics: not read |
| Abandoned paths | Worst case → quadratic OA [01 F1]; own Lagrangean variant dropped [03 E47] |
| Reception | Corrected characterization (doi:10.1016/j.disopt.2006.10.011); exponential worst case (doi:10.1287/ijoc.1120.0545); quadratic master criticised (doi:10.1007/s10107-018-1356-3); CQ assumptions questioned (arXiv:2606.26897) [05 §1] |
| Methods | 3, 2, 5 |

### Before T3.7 (moved verbatim)

T3.7 shortened these rows of the SKILL.md table: Origin, Key insight, Minimum evidence, Abandoned paths. Their full wording before T3.7 is the table above (the SKILL.md rows as they stood after T3.6), unchanged; it is not repeated here.

Other SKILL.md lines T3.7 shortened or moved, as they stood before that pass:

**Signature Work Anatomy (section text)**

Rows rest on the full texts where read (version named on each card); full rows, earlier versions and a further anatomy (integer trust regions, `references/research/09-evidence-ledger.md#anatomy-slip`) are in the ledger.

<a id="anatomy-sqp-bb"></a>

## Anatomy: Integrating SQP and Branch-and-Bound for MINLP (Leyffer, Comput. Optim. Appl. 18(3), 2001, doi:10.1023/A:1011241421041), with FilMINT (doi:10.1287/ijoc.1090.0373) and Minotaur (doi:10.1007/s12532-020-00196-1)

### Full rows in SKILL.md after T3.6

**Integrating SQP and Branch-and-Bound for MINLP (Leyffer, Comput. Optim. Appl. 18(3), 2001, doi:10.1023/A:1011241421041), with FilMINT (doi:10.1287/ijoc.1090.0373) and Minotaur (doi:10.1007/s12532-020-00196-1)**

Read: report NA/182 [S009], FilMINT preprint [S015], Minotaur report [S032 TR]. Full rows: references/research/09-evidence-ledger.md#anatomy-sqp-bb.

| Dimension | Content |
|---|---|
| Origin | Improves Borchers and Mitchell (doi:10.1016/0305-0548(94)90024-8) [S009 pp. 1–2] |
| Why then | His own SQP code had just arrived (filterSQP manual, April 1998) [06 Turn D] |
| Key insight | Branch after one QP iteration; fathom when a QP with a linearized objective cut is infeasible [S009 pp. 5–6] |
| Minimum evidence | Eight public test problems; about 3 times faster than nonlinear B&B on the largest [S009 pp. 9–11] |
| Abandoned paths | Lagrangian-dual bound dropped; fails on nonconvex FEEDLOC; "a factor of about 3" became "a factor of up to 3" [01 F7]; group moved to LP/NLP-based B&B (FilMINT) [05 §2.2] |
| Reception | NEOS "MINLP" solver; warm-start premise contested [05 §2.1]; split verdict on NLP-BB in 2019 [05 §2.3] |
| Methods | 1, 4, 5; Heuristic 1 |

### Added in T3.6

Extra full-text detail: a callback after each SQP step keeps filterSQP changes minimal [S009 p. 10]; fathoming by surrogate-QP infeasibility is free in a primal active-set solver and is guarded by the trust region [S009 pp. 5–6, 8]; convergence by reduction to classical B&B [S009 p. 7]; an early-branching trigger from the experimental order of convergence [S009 p. 9]; "However, better heuristics for nonconvex MINLP problems remain an open problem." [S009 p. 11]. FilMINT: "a fundamental design philosophy is to treat linearizations of the nonlinear feasible region in a manner similar to the way cutting planes are treated by a branch-and-cut algorithm for MILP." [S015 p. 18]. Branching rules (2013): "Though largely given up on, there is the possibility that B&B can still be made viable for convex MINLP, and that is the subject of the present investigation." [S028 TR p. 3]. Minotaur: [S032 TR pp. 5, 12–16].

### Before T3.6 (moved verbatim)

**Integrating SQP and Branch-and-Bound for MINLP (Leyffer, Comput. Optim. Appl. 18(3), 2001, doi:10.1023/A:1011241421041), with FilMINT (doi:10.1287/ijoc.1090.0373) and Minotaur (doi:10.1007/s12532-020-00196-1)**

| Dimension | Content |
|---|---|
| Origin | Improves Borchers and Mitchell (doi:10.1016/0305-0548(94)90024-8) [01 S2] |
| Why then | His own SQP code had just arrived (filterSQP manual, April 1998) [06 Turn D] |
| Key insight | Branch after one QP iteration; SQP linearizations read as cuts |
| Minimum evidence | Eight public test problems; about 3 times faster than nonlinear B&B on the largest [01 S2] |
| Abandoned paths | Lagrangian-dual bound dropped; fails on nonconvex FEEDLOC; "a factor of about 3" became "a factor of up to 3" [01 F7]; group moved to LP/NLP-based B&B (FilMINT) [05 §2.2] |
| Reception | NEOS "MINLP" solver; warm-start premise contested [05 §2.1]; split verdict on NLP-BB in 2019 [05 §2.3] |
| Methods | 1, 4, 5; Heuristic 1 |

### Before T3.7 (moved verbatim)

T3.7 shortened these rows of the SKILL.md table: Abandoned paths. Their full wording before T3.7 is the table above (the SKILL.md rows as they stood after T3.6), unchanged; it is not repeated here.

<a id="anatomy-filter"></a>

## Anatomy: Nonlinear programming without a penalty function (Fletcher and Leyffer, Math. Program. 91(2), 2002, doi:10.1007/s101070100244)

### Full rows in SKILL.md after T3.6

**Nonlinear programming without a penalty function (Fletcher and Leyffer, Math. Program. 91(2), 2002, doi:10.1007/s101070100244)**

Read: the NA/171 revision of 2000 [S001]. Full rows: references/research/09-evidence-ledger.md#anatomy-filter.

| Dimension | Content |
|---|---|
| Origin | Fletcher's idea; "Our filter method [17] grew out of these early experiments." [02 §3.1]; Leyffer's share cannot be separated |
| Why then | "the unmodified SQP method is able to quickly solve a large proportion of test problems" [02 §3.2; S019 p. 4] |
| Key insight | Accept a step that reduces either the objective or the constraint violation [S001 pp. 4–6] |
| Minimum evidence | Numbers first: CUTE runs against LANCELOT and a self-built Sℓ1QP at its best penalty [S001 pp. 17–24]; proof next (SLP-filter report NA/183, 1998 [S109]; filter-SQP, SIAM J. Optim. 2002, doi:10.1137/S105262340038081X [S005]; both texts unreadable) [01 S3] |
| Abandoned paths | Maratos hope "shattered" [02 §3.4; S019 p. 8]; the example [S001 pp. 7–8]; early proof errors corrected by coauthors [05 §3] |
| Reception | Lagrange Prize 2006; IPOPT filter line search; restoration criticised (doi:10.1137/080738222); funnel rival (doi:10.1007/s10107-008-0244-7); "the choice of method is really a question of personal preference" (2017) [H004 p. 5] |
| Methods | Heuristic 3; 3, 5 |

### Added in T3.6

Extra full-text detail: restoration on the QP solver's phase I partition with hot starts, about one QP per restoration [S001 pp. 9–10]; SOC steps justified by a Maratos-type example [S001 pp. 7–8]; CUTE runs: 127 of 186 small problems after removing differing minima, crashes kept, named failures with causes, safeguard firing tables and a corner-rule switch-off [S001 pp. 17–24]; corner rules marked for removal once the SLP-filter proof existed [S001 pp. 14–15]; "Thus any heuristi[c]s that might be suggested to enable a global [c]onvergen[c]e result to be proved should be [c]heap to apply and rarely invoked." [S001 p. 3] (letters lost in the text extraction restored in brackets; the card copies the damaged form). History: [S019 pp. 4, 7–8]. The 2002 global-convergence paper itself is unreadable [S005]; the trust-region SQP-filter proof structure is read [S007 pp. 13–22].

### Review fixes (T3.6)

- Minimum evidence: the SLP-filter report NA/183 (1998) [S109] and the filter-SQP paper in SIAM J. Optim. (2002, doi:10.1137/S105262340038081X) [S005] are separate works, both with unreadable text layers; the pre-synthesis row paired the report with the journal paper's DOI.
- Abandoned paths: the word "shattered" is from the 2006 history [S019 p. 8]; the example is in the report [S001 pp. 7–8].

### Before T3.6 (moved verbatim)

**Nonlinear programming without a penalty function (Fletcher and Leyffer, Math. Program. 91(2), 2002, doi:10.1007/s101070100244)**

| Dimension | Content |
|---|---|
| Origin | Fletcher's idea; "Our filter method [17] grew out of these early experiments." [02 §3.1]. Leyffer's share cannot be separated |
| Why then | "the unmodified SQP method is able to quickly solve a large proportion of test problems" [02 §3.2] |
| Key insight | Accept a step that reduces either the objective or the constraint violation |
| Minimum evidence | Numbers first (NA/171, 1997), proof next (NA/183, 1998; doi:10.1137/S105262340038081X) [01 S3]. Journal numerics: not read |
| Abandoned paths | Maratos hope "shattered" [02 §3.4]; early proof errors corrected by coauthors [05 §3] |
| Reception | Lagrange Prize 2006; IPOPT filter line search; restoration criticised (doi:10.1137/080738222); funnel rival (doi:10.1007/s10107-008-0244-7); his deflation: "the choice of method is really a question of personal preference" (2017) [02 C1] |
| Methods | Heuristic 3; 3, 5 |

### Before T3.7 (moved verbatim)

T3.7 shortened these rows of the SKILL.md table: Origin, Minimum evidence, Abandoned paths, Reception. Their full wording before T3.7 is the table above (the SKILL.md rows as they stood after T3.6), unchanged; it is not repeated here.

<a id="anatomy-mpec"></a>

## Anatomy: MPECs solved as NLPs (Fletcher and Leyffer, Optim. Methods Softw. 19(1), 2004, doi:10.1080/10556780410001654241; with Ralph and Scholtes, SIAM J. Optim. 17(1), 2006, doi:10.1137/S1052623402407382; MacMPEC)

### Full rows in SKILL.md after T3.6

**MPECs solved as NLPs (Fletcher and Leyffer, Optim. Methods Softw. 19(1), 2004, doi:10.1080/10556780410001654241; with Ralph and Scholtes, SIAM J. Optim. 17(1), 2006, doi:10.1137/S1052623402407382; MacMPEC)**

Read: report NA/210 [S020; S013 TR] and the 2003 survey [S057]; the 2006 local theory is unreadable [S008]. Full rows: references/research/09-evidence-ledger.md#anatomy-mpec.

| Dimension | Content |
|---|---|
| Origin | NLP approaches "commonly regarded as numerically unsafe" [S057 p. 15]; "our initial numerical experience with filterSQP was very positive" [02 §5.4] |
| Why then | Inferred: the strong-stationarity/KKT equivalence [S057 pp. 16, 18]; a reliable SQP code with an AMPL interface [S020 pp. 5–6] |
| Key insight | With slacks and z1ᵀz2 ≤ 0, standard NLP solvers handle complementarity [S020 pp. 1, 3] |
| Minimum evidence | 137 MacMPEC problems, a failure taxonomy, control reruns [S020 pp. 9–12] |
| Abandoned paths | Interior methods (doi:10.1137/040621065); PIPA counterexample (doi:10.1080/10556780500140078); 2007 SLPEC filter never reached a journal [05 §4.3] |
| Reception | "quite successful, particularly on the MacMPEC set" (Benson et al. 2006, doi:10.1007/s10589-005-3908-8) [05 §4.1]; assumptions called restrictive [05 §4.2]; in 2026 plain NLP "less competitive than the MPEC-tailored methods" (doi:10.1007/s10589-026-00832-x) [05 §4.3; S126 arXiv p. 34] |
| Methods | 2, 4, 5, 6 |

### Added in T3.6

Extra full-text detail: a two-variable example shows the equality form converging linearly and z1ᵀz2 ≤ 0 in one step [S020 p. 3]; the unbounded multiplier ray and its minimal element [S020 pp. 2–3; S057 pp. 16–17]; a failure taxonomy [S020 p. 9]; cause-removal reruns with complementarity relaxed to ≤ 10⁻² [S020 pp. 10–12]; a multiplier-size profile beside the performance profiles [S020 p. 13]; literature comparisons labelled tentative [S020 pp. 14–17]: "Interior point methods are less robust, failing on about 15 % of problems." [S020 p. 17]. The survey: "As a consequence, solving MPCCs via NLPs such as (2) has been commonly regarded as numerically unsafe." [S057 p. 15]; "The key to proving convergence in both cases is the equivalence between strong stationarity (1) and the KKT conditions (2)." [S057 p. 18]. The 2006 local theory [S008] is unreadable. 2017 view: "In my opinion, reliable NLP solvers are still the best approach for solving MPECs despite the potential problems with slow convergence or convergence to spurious stationary points." [H004 p. 9].

### Review fixes (T3.6)

- Why then carries the "Inferred:" label again: the cards show the equivalence (credited to Scholtes, the key to the convergence proofs) [S057 pp. 16, 18] and the AMPL interface [S020 pp. 5–6], not why the work came at that time.
- Reception: the 2026 quote is cited to note 05, which copied it from the text, with the card's page for the numbers [05 §4.3; S126 arXiv p. 34]; the S126 card records the success rates, not the sentence. Benson et al. is dated 2006 with its DOI [05 §4.1].

### Before T3.6 (moved verbatim)

**MPECs solved as NLPs (Fletcher and Leyffer, Optim. Methods Softw. 19(1), 2004, doi:10.1080/10556780410001654241; with Ralph and Scholtes, SIAM J. Optim. 17(1), 2006, doi:10.1137/S1052623402407382; MacMPEC)**

| Dimension | Content |
|---|---|
| Origin | NLP approaches "commonly regarded as numerically unsafe"; "our initial numerical experience with filterSQP was very positive" [02 §5.4] |
| Why then | Inferred: a reliable SQP code, an AMPL interface, a growing library [03 E15, E52] |
| Key insight | With slacks, standard NLP solvers handle complementarity [02 §4.2] |
| Minimum evidence | A new library plus numbers: "a large class of MPECs can in fact be solved successfully as NLPs" (NA/210) [03 E52] |
| Abandoned paths | Interior methods (doi:10.1137/040621065); PIPA counterexample (doi:10.1080/10556780500140078); 2007 SLPEC filter never reached a journal [05 §4.3] |
| Reception | "quite successful, particularly on the MacMPEC set" (Benson et al.) [05 §4.1]; assumptions called restrictive [05 §4.2]; in 2026 plain NLP "less competitive than the MPEC-tailored methods" (doi:10.1007/s10589-026-00832-x) [05 §4.3] |
| Methods | 2, 4, 5, 6 |

### Before T3.7 (moved verbatim)

T3.7 shortened these rows of the SKILL.md table: Reception. Their full wording before T3.7 is the table above (the SKILL.md rows as they stood after T3.6), unchanged; it is not repeated here.

### Review fixes (T3.7)

- Reception: the 2026 sentence is labelled as his coauthored paper again, with its DOI (doi:10.1007/s10589-026-00832-x), because it is self-assessment, not outside reception (10-claim-audit.md, k=16: partial for that reason).

<a id="anatomy-mccormick"></a>

## Anatomy: McCormick envelopes in mixed-integer PDE-constrained optimization (Leyffer and Manns, Math. Program. 218, 2025, doi:10.1007/s10107-024-02181-1; Correction doi:10.1007/s10107-026-02330-8)

### Full rows in SKILL.md after T3.6

**McCormick envelopes in mixed-integer PDE-constrained optimization (Leyffer and Manns, Math. Program. 218, 2025, doi:10.1007/s10107-024-02181-1; Correction doi:10.1007/s10107-026-02330-8)**

Read: arXiv v5 [S096 arXiv] and the Correction [S162]. Full rows: references/research/09-evidence-ledger.md#anatomy-mccormick.

| Dimension | Content |
|---|---|
| Origin | MIPDECO is credited to an August 2013 ExaMath13 position paper [S112 p. 2], and a public August 2013 DOE exascale-workshop deck already bore the class name [02 §2.4, §2.5]; the 2015 Oberwolfach abstract is the first carded text that uses the name [S112 pp. 1–2]; source of the McCormick idea: not documented |
| Why then | Pointwise McCormick gives infinitely many constraints and intractable OBBT [S096 arXiv pp. 2, 8] |
| Key insight | Average the nonlinearity over partition cells, then relax, with an a priori error estimate in the mesh size [S096 arXiv pp. 8–11] |
| Minimum evidence | Every assumption certified on a 1D example [S096 arXiv pp. 16–19]; whether it meets the hypothesis added by the Correction is not discussed [S162 pp. 1–2]; the a priori bound beats the trivial one only on fine meshes [S096 arXiv pp. 28–29] |
| Abandoned paths | Two errors corrected in print (missing box constraint; a proof step) [S162 pp. 1–2]; who found them: not stated |
| Reception | Too recent; limits of the companion SLIP method repaired by Manns's group [05 §5.1] |
| Methods | 2, 5, 7; Heuristic 8 |

### Added in T3.6

Extra full-text detail: the 2013 survey already names mixed-integer optimal control as a class with a library [S002 pp. 87–94] (08 §3.2 item 9); averaging uw → (P_h u)(P_h w) gives four inequalities per cell [S096 arXiv pp. 8–11]; Γ-convergence and OBBT soundness [S096 arXiv pp. 13–16]; explicit embedding constants certify the assumptions [S096 arXiv pp. 16–19]; 2D OBBT in 127 s against far longer pointwise runs [S096 arXiv pp. 30–32]; "the a priori approximation quality of the lower bound only improves over trivial bounds when the mesh size is already quite fine and the involved constants can be estimated well." [S096 arXiv p. 32]. Correction: "We correct two mistakes in the paper [S. Leyffer and P. Manns, Math. Prog. 2025]." [S162 p. 1]; how the added hypothesis bears on the worked example is not discussed [S162 pp. 1–2] (08 §11).

### Review fixes (T3.6)

- Origin corrected (correction 8). S112 credits the name to its ref. [4], the August 2013 ExaMath13 position paper (Leyffer, Munson, Wild, van Bloemen Waanders, Ridzal) [S112 p. 2]; the 2013 deck titled "Mixed-Integer PDE-Constrained Optimization" was given at the DOE workshop Applied Mathematics Research for Exascale Computing, 21–22 August 2013 [02 §2.4, §2.5; note 02 source list]; the 2015 Oberwolfach abstract is the first carded text using the name [S112 pp. 1–2]. The T3.6 text said the class "was named publicly in 2015", which the 2013 deck contradicts.
- Minimum evidence adds that the two-page Correction does not say whether the worked example meets its added hypothesis [S162 pp. 1–2] (08 §11).

### Before T3.6 (moved verbatim)

**McCormick envelopes in mixed-integer PDE-constrained optimization (Leyffer and Manns, Math. Program. 218, 2025, doi:10.1007/s10107-024-02181-1; Correction doi:10.1007/s10107-026-02330-8)**

| Dimension | Content |
|---|---|
| Origin | Class named in 2017 [01 S5]; source of the McCormick idea: not documented |
| Why then | McCormick relaxations "have not gained much attention in PDE-constrained optimization so far" [01 S5] |
| Key insight | Average the nonlinearity over partition cells; convex relaxations with an a priori error estimate in the mesh size |
| Minimum evidence | "We provide a computational example, for which we certify all of our imposed assumptions." [01 S5] |
| Abandoned paths | Two errors corrected in print (missing box constraint; a proof step) [01 F10]; who found them: not stated |
| Reception | Too recent; limits of the companion SLIP method repaired by Manns's group [05 §5.1] |
| Methods | 2, 5; Heuristic 8 |

### Before T3.7 (moved verbatim)

T3.7 shortened these rows of the SKILL.md table: Origin, Minimum evidence. Their full wording before T3.7 is the table above (the SKILL.md rows as they stood after T3.6), unchanged; it is not repeated here.

<a id="anatomy-b-stationarity"></a>

## Anatomy: Certified B-stationarity, from the SLPEC filter (2007) to MPECopt (2026)

New in T3.6 (the anatomy behind Method 7).

### Full rows in SKILL.md

**Certified B-stationarity: SLPEC filter (Leyffer and Munson, ANL/MCS-P1457-0907, 2007) → MPECopt (Nurkanović and Leyffer, doi:10.1007/s10589-026-00832-x, 2026)**

Read in full: S042 (2007 ANL preprint), S069 preprint, S126 arXiv v5; journal versions not compared. Full rows: references/research/09-evidence-ledger.md#anatomy-b-stationarity.

| Dimension | Content |
|---|---|
| Origin | His own NLP approach to MPECs could stop at spurious stationary points [S042 pp. 3, 5] |
| Why then | Inferred: MPEC-as-NLP was established; the SLQP code could take an LPEC in place of its LP step [S042 p. 22] |
| Key insight | Choose the subproblem whose zero step is exactly B-stationarity: an LPEC in a trust region [S042 pp. 4, 10] |
| Minimum evidence | Two-variable examples where weaker stationary points admit descent; a proof, no numerics [S042 pp. 5–8, 16–21] |
| Abandoned paths | The 2007 filter stayed a report; LPEC methods are hard to implement, so in 2026 LPECs become trust-region-bounded MILPs [S126 arXiv pp. 4, 15–16] |
| Reception | External reception not carded. Own 2026 benchmark, success = a B-stationary point (others checked post hoc): MacMPEC, MPECopt 94.24%, regularization 93.2%, ℓ∞ penalty 92.14%, plain NLP 90.00%, big-M MINLP 72.52%, though "Many MacMPEC problems are small or easily solved by all examined algorithms." [S126 arXiv pp. 34–35]; 75 generated instances violating MPEC-LICQ: MPECopt 96.16%, regularization and ℓ∞ penalty 94.67%, plain NLP 16.00%, mostly 45-minute timeouts [S126 arXiv pp. 36–37] |
| Methods | 7, 3, 2, 5 |

### Further detail from the cards

| Dimension | Detail |
|---|---|
| Works | Leyffer and Munson, "A globally convergent filter method for MPECs", ANL/MCS-P1457-0907 (2007) [S042]; Fang, Leyffer and Munson, "A pivoting algorithm for linear programming with linear complementarity constraints", Optim. Methods Softw. (2012), doi:10.1080/10556788.2010.512956, read as preprint ANL/MCS-P1680-1009 [S069 preprint]; Kirches, Larson, Leyffer and Manns, sequential linearization for bound-constrained MPCCs, SIAM J. Optim. (2022), doi:10.1137/20m1370501 [S092]; Kim, Leyffer and Munson, "MPEC methods for bilevel optimization problems" (2020), doi:10.1007/978-3-030-52119-6_12 [S034]; Nurkanović and Leyffer, MPECopt, Comput. Optim. Appl. (2026), doi:10.1007/s10589-026-00832-x, arXiv v5 read [S126] |
| Origin | NLP approaches, his own included, can converge to spurious stationary points, observed on PJM electricity-market problems; A-, C- and M-stationarity allow trivial descent directions [S042 pp. 3, 5]: "Our main contribution is to regard the complementarity constraint as as a structural constraint, not as a nonlinear equation." [S042 p. 4] |
| Key insight | The LPEC step uses the correct tangent cone; d = 0 if and only if the point is B-stationary; an EQP accelerates; a three-dimensional filter separates general and complementarity infeasibility [S042 pp. 4, 9–11] |
| Minimum evidence | Closed-form SQPEC iterates converging quadratically to a spurious M-stationary point, with the hypothesis check: "We note that this is not a counterexample to the results by Scholtes (2004), because Scholtes investigates only local quadratic convergence." [S042 p. 8]; global convergence to B-stationary points under MPEC-MFCQ [S042 pp. 15–21]; no numerics [S042 pp. 22–23] |
| Continuation | LPCC pivoting with an anticycling scheme that certifies B-stationarity, finite termination [S069 preprint pp. 7–18]; "Unfortunately, simply applying Bland’s rule to Algorithm 2 for LPCCs can still result in a cycle." [S069 preprint p. 13]; sequential linear models chosen because a two-variable example defeats SQP [S092 pp. 6–9]; a survey organized by the notion each class guarantees [S034 pp. 10–16]: "To our knowledge, this algorithm is the only one that guarantees global convergence to B-stationary points." [S034 p. 16] |
| 2026 | MPECopt: Phase I by Scholtes regularization plus an LPEC; Phase II trust-region LPECs pick a branch NLP, accepted only on decrease; LPECs solved as trust-region-bounded big-M MILPs; certification costs one LP at S-stationary points [S126 pp. 10–17]; same-solver comparison on MacMPEC and a public synthetic generator; MacMPEC success: MPECopt 94.24%, regularization 93.2%, ℓ∞ penalty 92.14%, plain NLP 90.00%, big-M MINLP 72.52%; synthetic set: plain NLP 16.00% [S126 pp. 34, 36–37]; implementation complexity named as the drawback of the authors' earlier LPEC methods [S126 p. 4] |
| Limits | MPEC-MFCQ everywhere; restoration case untreated; exact BNLP solves; only B-stationary, not global, points; LPEC worst case exponential [S126 pp. 15, 18, 23–25, 38] |
| Methods | 7, 3, 2, 5 |

### Review fixes (T3.6)

- Read line names the versions: S042 is the 2007 ANL preprint, S069 the preprint, S126 arXiv v5; journal versions were not compared.
- Reception: the row is the paper's own benchmark (external reception not carded). It now gives the MacMPEC rate per method with the authors' caveat, "Many MacMPEC problems are small or easily solved by all examined algorithms." [S126 arXiv pp. 34–35], and the synthetic set that separates the methods: MPECopt 96.16%, regularization and ℓ∞ penalty 94.67%, plain NLP 16.00%, mostly 45-minute timeouts [S126 arXiv pp. 36–37].

### Before T3.7 (moved verbatim)

T3.7 shortened these rows of the SKILL.md table: Reception. Their full wording before T3.7 is the table above (the SKILL.md rows as they stood after T3.6), unchanged; it is not repeated here.

### Review fixes (T3.7)

- Reception: "regularization and ℓ∞ penalty 94.67%" is back on the 75 generated instances, so the row no longer reads as MPECopt against plain NLP alone [S126 arXiv pp. 36–37].

<a id="anatomy-slip"></a>

## Anatomy: Trust regions on integer controls, SLIP (2022) and binary trust-region steepest descent (2023)

New in T3.6. Not printed in SKILL.md (word budget); the integer-control routing row and the anatomy section point here.

### Sequential linear integer programming for integer optimal control with total variation regularization (Leyffer and Manns, ESAIM COCV 28, 2022, doi:10.1051/cocv/2022059) and Binary optimal control by trust-region steepest descent (Hahn, Leyffer and Sager, Math. Program. 197, 2023, doi:10.1007/s10107-021-01733-z)

Read in full [S065; S091].

| Dimension | Content |
|---|---|
| Origin | Combinatorial integral approximation gives oscillating controls whose total variation grows without bound, and its theory fails with a TV term; global solves of the discretized problem do not scale to fine meshes [S065 p. 2] |
| Why then | Inferred: the MIPDECO class had been named [S112 pp. 1–2] and branch-and-bound failed on fine meshes [05 §2.4]; a TV term makes minimizers exist [S065 p. 2]: "The topological restrictions induced by the discreteness constraint and the TV-regularizer are strong enough such that (P) admits optimal solutions." [S065 p. 2] |
| Key insight | Carry the trust-region loop into function space: linearize F, keep TV exact under an L1 radius, solve the subproblem as a linear IP after DG0 discretization, reset-and-halve radius control with an ared/pred test [S065 pp. 2–7]. 2023: the derivative as a signed measure, a trust region measured by the symmetric difference of sets, the subproblem solved by a sublevel set of the gradient density [S091 pp. 5–8, 23–26] |
| Minimum evidence | 1-D convolution tracking with five control levels, N = 32-2048, SCIP 7.0; SLIP against MIQP (5-hour limit) and CIA with SCARP rounding; SCIP's MIQP finds better objectives for N ≤ 128 and CIA for N = 64 and 128 [S065 pp. 19–22] |
| Abandoned paths | A faster doubling-radius variant reported but unproved [S065 pp. 21, 26]; "However, the algorithmic framework is computationally less attractive than the combinatorial integral decomposition." [S065 p. 26]; 2023: no iterate convergence, no constraints, not competitive in topology optimization [S091 pp. 3, 39, 42]; "Outside of the field of topology optimization, where similar methods already exist, it is generally difficult to design fair comparisons to other methods." [S091 p. 42] |
| Reception | Convergence studied further by coauthors [S115 pp. 2–3]; trust regions on binaries carried to electromagnetic cloaking [S144 p. 12; S128 pp. 12–13]; external reception not carded |
| Methods | 2, 7, 5; Heuristic 8 (coarse-to-fine clause) |

### Review fixes (T3.6)

- SKILL.md now prints an integer-control brief under the routing table, drawn from this anatomy and the S084 and S093 cards [S084 pp. 5, 12–17, 20–30; S093 pp. 23–24; S065 pp. 2–3, 8, 22, 26; S091 p. 42; 05 §5.1]: the B&B failure profile on the released instances, state elimination or superposition, TV regularization for existence, the relax-round-improve pipeline, the baselines to beat and the 2-D limits.
- The Methods row now reads Heuristic 8, which carries the former Heuristic 11 as its coarse-to-fine clause.

<a id="anti-patterns"></a>

## Research anti-patterns

### Added in T3.6

- Two rows added: "Stopping at a point that admits descent" → Method 7 [S126 p. 3; S069 preprint p. 3; S042 pp. 5–7]; "A parameter the user must tune where a test could decide" → Method 2 step 3 [S048 p. 3; S001 pp. 1–2; S164 p. 4].
- The row on unsolvable models now points to Method 6 steps 2-6 (step renumbering). The "convergence result" row keeps Taste 3; Method 7 gives it steps.

### Review fixes (T3.6)

- Each new row now shows two card ids: [S126 arXiv p. 3; S042 pp. 5–7] and [S048 p. 3; S001 pp. 1–2].

### Before T3.6 (moved verbatim)

**Research Anti-patterns**

| Anti-pattern | Why he opposes it (source) | Instead |
|---|---|---|
| A method without a convergence result | "no convergence result is presented" (1993) [02 §1.5] | Taste 3 |
| Decomposition dictated by packaged software | "This approach is largely due to the existence of packaged software" (1998) [02 §2.3] | Method 1 |
| Brute force in place of mathematics | "BnB won't scale to a billion-way concurrency" (2013) [02 §1.7] | Heuristic 8 |
| Hiding functions from the solver | "I'm not allowing you to take functions that I can't see inside" (2024, ASR) [02 §4.9] | Method 6 |
| Publishing a model the solver cannot handle; trusting surrogates outside their data | Warning sign 3 [02 §1.10, §2.6] | Method 6 steps 2-5 |
| Calling a theorem wrong without checking hypotheses | practice: "the assumptions usually exclude our example" [03 E44] | Method 3 step 3 |

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Research Anti-patterns (section text)**

| Anti-pattern | Why he opposes it (source) | Instead |
|---|---|---|
| Stopping at a point that admits descent | "too weak as practical stopping criteria" [S126 arXiv p. 3; S042 pp. 5–7] | Method 7 |
| A parameter the user must tune where a test could decide | "we remove the need for the arbitrary parameters" [S048 p. 3; S001 pp. 1–2] | Method 2 step 3 |

<a id="trajectory"></a>

## Research trajectory

### Full-text view (08 §8, verbatim)

Carded works per five-year period by topic (in brackets: full or partial). Topic assignment is this synthesis's, from title and contribution; ML includes surrogates and tuning; Global includes conic and robust work; Service includes editorials, community reports and essays.

| Period | MINLP | NLP | MPEC | Int. control | Global | Applications | Imaging/OED | ML | HPC | Service | All |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1990–94 | 2 (2) | – | – | – | – | – | – | – | – | – | 2 |
| 1995–99 | 4 (4) | 4 (3) | – | – | – | – | – | – | – | – | 8 |
| 2000–04 | 3 (3) | 7 (2) | 5 (4) | – | 1 (1) | 2 (2) | – | – | – | 3 (1) | 21 |
| 2005–09 | 2 (1) | 5 (5) | 7 (6) | – | 2 (2) | – | – | 2 (2) | – | 4 (2) | 23 (+1 junk) |
| 2010–14 | 6 (5) | 4 (3) | 3 (3) | 2 (2) | – | 13 (10) | 3 (2) | 3 (1) | 3 (2) | 8 (5) | 45 |
| 2015–19 | 1 (1) | 1 (1) | – | 2 (2) | 2 (1) | 9 (6) | 7 (5) | 2 (1) | 2 (2) | 6 (5) | 32 |
| 2020–24 | 1 (1) | 3 (3) | 2 (2) | 10 (9) | 3 (3) | 7 (7) | 3 (2) | 10 (8) | – | 3 (2) | 42 |
| 2025–26 | – | 4 (4) | 1 (1) | 6 (6) | – | – | 4 (4) | 2 (1) | – | 2 (2) | 19 |

Eleven undated rows and the 1971 junk row are omitted.

**Turns visible in the texts.**
1. *From a packaged solver to his own (1993–2001).* The thesis runs on NAG and names its limits [S016 pp. 77, 80]; filterSQP and MINLP_BB follow [S014 pp. 1–5; S023 pp. 1–2]; the integrated SQP–B&B is the payoff [S009 pp. 1–2].
2. *MPECs as NLPs (2002–2004), then certification (2007 onward).* Numbers on a new library overturn the verdict [S020 pp. 1–2, 9–17; S057 p. 15]; spurious stationary points lead to LPEC-based methods [S042 p. 3; S069 preprint p. 3; S092 pp. 6–7; S126 pp. 2–4].
3. *A global-optimization excursion (2004–2008)* [S031 pp. 1–2; S048 pp. 1–3; S041 pp. 3–5], not in the skill's trajectory.
4. *Team MINLP software and synthesis (2009–2013, consolidated 2021)* [S029 pp. 5–6; S015 pp. 3–4; S149 pp. 3–4; S049 pp. 4–5; S028 TR p. 3; S002 pp. 5, 7; S032 TR pp. 1–5].
5. *Laboratory applications (2010–2021):* energy, networks, HPC, imaging and tomography, generator tuning [S054 p. 7; S073 p. 3; S053 pp. 2, 7–8; S059 p. 1; S090 pp. 2–3; S044 p. 3], mostly with other first authors.
6. *Integer optimal control in function space (2012–2026):* from separating the model from its discretization [S116 pp. 1–5] and naming MIPDECO [S112 pp. 1–2] to trust-region methods on integer controls [S065 pp. 2–6; S091 pp. 3, 42; S115 pp. 2–3] and certified lower bounds [S096 arXiv pp. 1–3]; quantum control as a binary-control application [S088 pp. 3, 16; S134 arXiv pp. 2–5; S145 arXiv pp. 3–5].
7. *Rebuilding the NLP base (2020–2026)* [S110 pp. 2, 4; S114 arXiv pp. 2–3, 11; S119 pp. 1–5].

**What stayed constant.** An NLP acceptance test as the carried device [S001 pp. 4–6; S026 pp. 4–7; S071 pp. 4–5; S065 pp. 5–6; S164 p. 4]; smallest computed counterexamples with closed-form iterates [S016 p. 49; S055 p. 5; D001 pp. 4–8; S042 p. 8; S034 p. 15; S145 arXiv pp. 16–17]; same-solver comparisons with failures kept [S016 p. 78; S022 pp. 23–27; S126 pp. 32–34]; termination taxonomies that read CQ failure [S014 p. 8; S199 p. 14; S074 pp. 14–15; S119 pp. 18–19]; formulation before method [S016 p. 81; S020 pp. 10–12; S043 pp. 8–9; S032 TR pp. 22–23; S124 pp. 2–3].

### Added in T3.6

- Rows added: the 2004-2008 global-optimization excursion [S031 pp. 1–2; S048 pp. 1–3; S041 pp. 3–5] and the 2012-2021 laboratory applications (imaging and tomography [S059 pp. 1, 3–10; S066 pp. 8–9; S045 pp. 3–4; S090 pp. 2–4; S103 arXiv pp. 3–10]; generator tuning [S180; S044 p. 3; S052 pp. 3, 11; S136 p. 12]); HPC load balancing joins the side-lines row [S053 pp. 2, 7–8; S222 p. 1]. The MPEC row adds certified B-stationarity (2007, again 2026) [S042 p. 3; S126 pp. 2–4]; the MIPDECO row adds trust regions on integer controls [S065 pp. 2–6; S091 pp. 3, 42].
- A closing line gives what stayed constant [08 §8] and the end of sole-authored research articles in 2010 [08 §9].

### Review fixes (T3.6)

- The laboratory-applications row is dated 2014-2022: imaging from 2014 [S059 pp. 1, 3–10], generator tuning to 2022 [S136 p. 12], as in 08 §3.2 item 12; HPC load balancing stays in the side-lines row [S053 pp. 2, 7–8].

### Before T3.6 (moved verbatim)

**Research Trajectory**

| Period | Direction | Trigger | Representative work |
|---|---|---|---|
| 1990-1998 | Deterministic MINLP (thesis Dec 1993), OA, MIQP B&B | Advisor's toolbox; worst case [06 Turns A, B] | doi:10.1007/BF01581153; doi:10.1137/S1052623494268455 |
| 1996-2002 | Filter methods with Fletcher | Advisor's idea + numbers [06 Turn C] | doi:10.1007/s101070100244 |
| 1997-2001 | SQP inside B&B | His own solver [06 Turn D] | doi:10.1023/A:1011241421041 |
| 2000-2009 | MPECs as NLPs; MacMPEC | Counter-consensus numbers [06 Turn E] | doi:10.1080/10556780410001654241; doi:10.1137/S1052623402407382 |
| 2006-2013 | MINLP as team science: FilMINT, IMA volume, Acta survey | Field growing [06 Turn G] | doi:10.1287/ijoc.1090.0373; doi:10.1017/S0962492913000032 |
| 2001-2016 | Side lines (grid, computational economics, HPC, inexact computing), all left silently | Institution [06 Turn F] | arXiv:1610.02606 |
| 2013-now | Mixed-integer optimal control → MIPDECO | Collaborators (Sager, Kirches, Manns) [06 Turn H] | doi:10.1007/s10107-021-01733-z; doi:10.1007/s10107-024-02181-1 |
| 2018-now | ML, experimental design, quantum control | Laboratory programmes, juniors [06 Turn I] | doi:10.1287/ijoc.2022.0050; doi:10.1287/ijoc.2024.0560 |
| 2016-now | Back to the base: AL filter, Uno, funnel SQP, MPEC B-stationarity | Own code base + postdoc [06 Turn J] | doi:10.1007/s12532-026-00310-9; doi:10.1007/s10107-025-02284-3 |
| Jul 2026-now | AI-assisted research projects | New tool [06 Turn L] | https://github.com/leyffer/conDFO |

**Latest**

Oct 2025 to Oct 2026 [06 §7]: no arXiv submission after 24 Sep 2025; earlier work reached print (funnel SQP, filter-ADMM, Uno and its R package, MPEC B-stationarity, McCormick Correction); July-September 2026, AI-assisted repositories conDFO, BestPractices4AI and QuantumOpt26.

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Research Trajectory (section text)**

| Period | Direction | Trigger | Representative work |
|---|---|---|---|
| 2001-2016 | Side lines (grid, computational economics, HPC load balancing, inexact computing), all left silently | Institution [06 Turn F; S053 pp. 2, 7–8] | arXiv:1610.02606; doi:10.1109/SC.2012.62 |

Constant: an NLP acceptance test carried into each class, smallest counterexamples, same-solver comparisons, formulation before method [08 §8]; sole-authored research articles end in 2010 [08 §9].

**Latest**

Oct 2025 to Oct 2026 [06 §7]: no arXiv submission after 24 Sep 2025; earlier work reached print (funnel SQP, filter-ADMM, Uno and its R package, MPEC B-stationarity, McCormick Correction); July-September 2026, AI-assisted repositories conDFO, BestPractices4AI and QuantumOpt26.

### Review fixes (T3.7)

- Latest: "earlier work reached print (funnel SQP, filter-ADMM, Uno and its R package, MPEC B-stationarity, McCormick Correction)" is back, so the covered year does not read as only AI-assisted repositories [06 §7].

<a id="academic-lineage"></a>

## Academic lineage and collaboration pattern

### Collaboration pattern (08 §9, verbatim)

Counts are carded works (full, partial, abstract or unreadable; metadata rows, committee reports and junk rows excluded) on which the person is a coauthor.

| Period | Carded works | Distinct coauthors | Median coauthors per work | Most frequent coauthors |
|---|---|---|---|---|
| 1993–99 | 10 | 6 | 1 | Fletcher 6, Grothey 2 |
| 2000–06 | 27 | 22 | 1 | Fletcher 9, Toint 5, Gould 3, Nocedal 2 |
| 2007–12 | 36 | 45 | 1.5 | Munson 6, Linderoth 4, Mahajan 4, Abhishek 2, Friedlander 2, Newman 2, Kirches 2 |
| 2013–18 | 34 | 65 | 3 | Wild 10, Munson 5, Goldberg 4, Di 4, Jacobsen 4 |
| 2019–22 | 38 | 78 | 3 | Gursoy 5, Krishnamoorthy 5, Wild 5, Munson 5, Larson 4 |
| 2023–26 | 27 | 48 | 2 | Fei, Brady, Shen, Larson, Lynn, Manns, Medlin, Raghavan 3 each |

- **Longest partnerships.** Fletcher: 16 carded works, 1994–2012 (e.g. S003, S010, S014, S001, S020, S040). Munson: 20, 2006–2025 (e.g. S018, S042, S011, S069, S021, S123, S144). Wild: 16, 2013–2026, mostly imaging, inexact computing and DFO (e.g. S082, S090, S094). Then Di 9, Linderoth 7, Mahajan 7, Larson 7, Toint 6, Newman 6, Kirches 6, Manns 6.
- **Sole-authored research works end in 2010:** the thesis [S016], the MINLP_BB manual [S023], the SQP–B&B paper [S009], the OA entry [S101], the PIPA counterexample [S067; D001], the 2003 MPEC survey [S057], the 2005 active-set note [S077], the NCP paper [S022], the FASTr manual [S199], the multiobjective MPCC paper [S063] and the branching paper [S149]. Later sole-authored items are not research articles: proposal-writing slides [H006], the Fletcher interview [H005] and the 2017 newsletter essay [H004]. Every carded work from 2019 on has coauthors.
- **First authorship moves to others.** At least 15 of the 27 carded works of 2023–2026 name another first author (Fei, Aretz, Choudhary, Lu, Medlin, Ryu, Vanaret, Nurkanović, Kim, Hahn, Li, Ganko and others) [S145; S150; S164; S165; S167; S124; S119; S126; S087; S091; S120; S152].
- **Who carries which line.** Minotaur by Mahajan [S032], Uno by Vanaret [S119], the MPECopt method by Nurkanović [S126], function-space integer control by Manns, Hahn and Sager [S065; S091; S115], quantum control by Fei, Brady, Larson and Shen [S088; S134; S145]. This matches the skill's lineage note and Method 1's limitation that juniors write the frameworks.
- **Voice.** In collaborations led by facility or laboratory scientists his share is not identifiable [S045; S102; S153; S136], and committee reports are not his voice [S025; S133; S163]. These are counted for trajectory and collaboration, not as method evidence.

### Before T3.6 (moved verbatim)

**Academic Lineage**

Colin M. Reeves → Roger Fletcher → **Leyffer** (PhD Dundee, thesis dated December 1993) [06 §1.1]; partnership with Fletcher to 2012. No formal PhD students (Mathematics Genealogy: "No students known"); juniors come through laboratory programmes. Lines carried by juniors: Minotaur (Mahajan), Uno (Vanaret), MIPDECO analysis (Manns); newer coauthors Kiessling, Nurkanović, Yang [06 §1.2; 04 §2]. What passes down (inferred from practice): build on the group's codes and libraries, use the senior's code as yardstick, document gaps, publish corrections [04 K1, K4, K5].

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Academic Lineage (section text)**

Colin M. Reeves → Roger Fletcher → **Leyffer** (PhD Dundee, thesis dated December 1993) [06 §1.1]; partnership with Fletcher to 2012 (16 carded works), then Munson and Wild [08 §9]. No formal PhD students (Mathematics Genealogy: "No students known"); juniors come through laboratory programmes. Lines carried by juniors: Minotaur (Mahajan), Uno (Vanaret), MIPDECO analysis (Manns), MPECopt (Nurkanović) [06 §1.2; 04 §2]. What passes down (inferred from practice): build on the group's codes and libraries, use the senior's code as yardstick, document gaps, publish corrections [04 K1, K4, K5].

<a id="inner-tensions"></a>

## Inner tensions

### Added in T3.6

- **Certify vs ship (new)**: certified B-stationarity and post-hoc grading of competitors in the algorithm papers [S126 pp. 34, 40] against applied collaborations that ship labelled heuristics or defer the proof [S045 p. 7; S066 p. 9; S093 pp. 16, 31; S123 arXiv p. 22; S128 p. 12; S135 pp. 8, 11]. Basis: Method 7 limitations [08 §4].
- **Real problems vs test libraries**: the 2015 agreement is now carded [H005 p. 5].
- **Fairness rules vs self-favouring choices**: the full texts show tuning on the comparison set recurring [S015 p. 27; S028 TR pp. 7, 17; S079 pp. 13–15; S114 arXiv pp. 19–20].
- **Numbers first vs theory first**: the bundle filter came theory first [S026 pp. 1–15], as did the MPEC filter [S042 p. 23].
- SKILL.md shortened several bullets; the full earlier wording follows.

### Review fixes (T3.6)

- Certify vs ship is recorded as the team's record: the algorithm papers certify and grade [S126 arXiv pp. 34, 40]; applied team papers led by others ship labelled heuristics or defer the proof [S135 pp. 8, 11; S123 arXiv p. 22]; whose choice that is cannot be told [08 §9]. S045 (facility-led, Leyffer fifth author) is no longer cited for it. His own 2017 essay keeps plain NLP solvers as the practical MPEC default [H004 p. 9].

### Before T3.6 (moved verbatim)

**Inner Tensions**

- **Real problems vs test libraries.** Agrees "test problems are often very badly selected" (2015) — yet builds and benchmarks on libraries 2000-2026, including "a subset of 429 small problems from the CUTE collection" (Uno 2024) [02 §1.1, C5].
- **Fairness rules vs self-favouring choices.** Fairness rules in papers 1993-2026 [03 E01-E05] — against FilMINT tuned on its own suite, 2015-era competitors kept in 2020, thesis runs dropped because "it was felt that they would otherwise distort the results" [03 E22, E55, E23].
- **Champion vs deflator of the filter.** "We believe filter methods achieve this goal." (2006) — against "the choice of method is really a question of personal preference" (2017), the funnel adopted (2024) and penalty functions revisited (2025-26); yet filter-based DFO and ADMM continue [02 C1; 06 C10].
- **Numbers first vs theory first.** Filter numbers 1997, proof 1998 — against MPEC theory report NA/209 before numbers NA/210, and conDFO proof before prototype [06 C12; 03 E73].
- **NLP vs polyhedral relaxations in the tree.** SQP-based NLP-BB (2001) and "reliable NLP solvers are still the best approach for solving MPECs" (2017) — against "Use LP solvers as much as possible in MINLP" (2013) and Quesada-Grossmann "arguably the best" (2017) [05 §2.2, §4.3; 02 §4.1, C3].
- **Loud self-correction vs silent exits.** Credits correctors and publishes corrections — but leaves five lines without a word, and QP-diving and the 2007 MPEC filter unpublished [05 §8; 06 §0].
- **Generality vs restraint.** MINLP is "one of the most general modeling paradigms in optimization" (2017) — against "Teach a man about nonlinear functions and you will lead a troubled life." [02 C7].

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Inner Tensions (section text)**

- **Real problems vs test libraries.** Agrees "test problems are often very badly selected" (2015) — yet builds and benchmarks on libraries 2000-2026 [02 §1.1, C5; H005 p. 5].
- **Fairness rules vs self-favouring choices.** Fairness rules in papers 1993-2026 [03 E01-E05] — against tuning on the comparison suite, 2015-era competitors kept in 2020, thesis runs dropped [03 E22, E55, E23; S028 TR pp. 7, 17].
- **Champion vs deflator of the filter.** "We believe filter methods achieve this goal." (2006) — against "the choice of method is really a question of personal preference" (2017) and penalty functions revisited; yet filter-based DFO and ADMM continue [02 C1; 06 C10].
- **Numbers first vs theory first.** Filter numbers 1997, proof 1998 — against MPEC theory before numbers, conDFO proof before prototype, the bundle filter proved before any run [06 C12; 03 E73; S026 pp. 1–15].
- **NLP vs polyhedral relaxations in the tree.** SQP-based NLP-BB (2001) and "reliable NLP solvers are still the best approach for solving MPECs" (2017) — against "Use LP solvers as much as possible in MINLP" (2013) [05 §2.2, §4.3; 02 §4.1, C3].
- **Loud self-correction vs silent exits.** Credits correctors and publishes corrections — but leaves five lines without a word, and QP-diving and the 2007 MPEC filter unpublished [05 §8; 06 §0].
- **Generality vs restraint.** MINLP is "one of the most general modeling paradigms in optimization" (2017) — against "Teach a man about nonlinear functions and you will lead a troubled life." [02 C7].
- **Certify vs ship (team record).** The algorithm papers certify and grade competitors [S126 arXiv pp. 34, 40] — several applied team papers led by others ship labelled heuristics or defer the proof [S135 pp. 8, 11; S123 arXiv p. 22]; whose choice that is cannot be told [08 §9]. In his own voice, plain NLP solvers stay the practical MPEC default [H004 p. 9].

<a id="roundtable-card"></a>

## Roundtable Card

### Added in T3.6

- Lens adds "which notion does the answer certify?"; first questions add "Which notion does the output certify?"; the default adds the third rule-of-thumb row [S016 p. 83] and "certify the notion you claim"; push-back adds "success counted by solver status"; the Grossmann line cites the OA paper [S003 p. 8]; blind spots say "global certificates (side work only)" (correction 7). Paper cards now exist; a brief's evidence field may cite them in the roundtable form `[sven-leyffer card S126 p. 3]`.

### Review fixes (T3.6)

- The default keeps the two convex-MINLP rows that stood before T3.6, now called a dated rule of thumb to re-test (the 1993 third row stays in Method 5 step 5 [S016 p. 83; S101 p. 7]); "success counted by solver status" is marked as inferred from practice [S126 arXiv pp. 34, 40]; a first line tells roundtable briefs to cite paper cards, because the Activation Rules' "no paper cards yet" (kept verbatim) is obsolete.

### Before T3.6 (moved verbatim)

**Roundtable Card**

- **Lens (one line)**: The solver-builder's lens: will the nonlinear subsolver behave at every node of the tree, and is the formulation one it can evaluate and converge on?
- **Leads when**: convex-MINLP algorithm choice (NLP-BB vs OA vs LP/NLP-based B&B); a subsolver that stalls, fails at nodes or cannot evaluate; complementarity/MPEC constraints; mixed-integer optimal control or PDE-constrained integer design; solver-framework design; fair MINLP benchmarking.
- **First questions asked**: What does the solver log show (rate, KKT error, restoration, evaluation failures)? Can this be linearized or made convex first? What is the smallest instance on which the method fails, and does it meet the theory's hypotheses? Which restriction comes from the software, not the mathematics? Which test set, filter, competitor versions and date?
- **Default recommendation**: Reformulate first (linearize, slacks, disaggregate); for convex MINLP use LP/NLP-based B&B, NLP-BB for highly nonlinear small-gap problems; modify an open solver through callbacks if tooling blocks the idea; publish a small library with known values; report claims with date, test class and failures.
- **Will push back on**: black-box functions in the model; discretize-first brute force; "best solver" claims from one library; counterexamples without a hypothesis check; surrogates used outside their data.
- **Likely disagreements** (inferred from both sides' methods unless marked):
  - *Grossmann*: partly in print: the 1994 OA report called a Duran-Grossmann step "erroneous" (doi:10.1007/BF02592064) [03 E42]; Grossmann's school criticised the 1994 quadratic master (doi:10.1007/s10107-018-1356-3). Inferred: GDP superstructure modelling vs linearize-and-read-the-log.
  - *Sahinidis*: NLP relaxations inside the tree (doi:10.1023/A:1011241421041) vs polyhedral branch-and-cut (doi:10.1007/s10107-005-0581-8); local solutions vs global certificates. No dispute documented.
  - *Misener*: local NLP practice vs global solvers (doi:10.1007/s10898-014-0166-2); surrogate caution vs optimizing over trained models. No dispute documented.
  - *Burer*: "Use LP solvers as much as possible" vs exact copositive/SDP relaxations (doi:10.1007/s10107-008-0223-z). No dispute documented.
  - *Dey*: rule-of-thumb computation inside production solvers (doi:10.1007/s12532-020-00196-1) vs proxy theorems in stripped testbeds (doi:10.1007/s10107-016-1036-0). No dispute documented.
- **Blind spots**: global certificates; relaxation-strength theory; large-benchmark statistics; NLP assumptions carried into new classes; self-favouring benchmark choices.

<a id="honest-boundary"></a>

## Honest boundary

### Added in T3.6

- Coverage (this member's row of `scripts/team_status.py --coverage`, 2026-11-19): 224 Scholar rows, 211 distinct works indexed, 164 open full texts, 120 read in full, 35 in part, 22 abstract only, 27 metadata only including 6 unreadable, 7 skipped, 0 book material, 329 quotes verified (323 exact, 6 equal up to spacing or symbols, 0 not found) [08 §1].
- Remaining gaps (08 §11, verbatim):

- **Unreadable core theory.** The filter-SQP global convergence paper [S005], the local SQP convergence for MPECs (Anatomy 4) [S008], the multidimensional filter [S017], the SLP-filter proof he calls the most easily understood one [S109; H004 p. 4], the filter algorithms for equations [S038] and an introduction to algorithms [S024] have broken text layers and need OCR. Until then the filter proof structure is known from the trust-region SQP-filter paper [S007 pp. 13–22] and the 2006 history [S019 pp. 7–8], and the MPEC local theory from the survey's summary [S057 p. 17; H004 p. 8]. The agent-written claim of a gap in the 2002 corollary proof stays unverified.
- **No open text.** The MINLP volume edited with Lee [S004], the MacMPEC page [S030], the 2000 filter-SQP report [S132], the methods-and-software report with Mahajan [S035], the 2009 NSF award [S196], state elimination for MIOCP [S127] and the 2025 bilevel classification paper [S166] are known from abstracts or metadata only.
- **Versions.** Journal versions were not compared with the preprints read: the 1994 OA paper's numerics remain unread because the 1996 preprint has none [S003]; the FilMINT preprint lacks its per-instance appendix [S015]; Minotaur [S032 TR], McCormick [S096 arXiv], funnel [S114 arXiv], Uno [S119] and MPECopt [S126] were read in preprint or arXiv form; the ADMM filter work is known from 2022 talk slides, not the journal paper [S159].
- **Partial reads.** 35 cards read only parts (for example proofs skimmed in [S092], [S115], [S072]); claims about those proofs are not checked.
- **After the Correction.** How the hypothesis added by the 2026 Correction bears on the worked example of the paper is not discussed in the two-page Correction [S162 pp. 1–2].
- **Not in any carded work.** Referee reports, supervision, unpublished code decisions, why the Uno claims were narrowed, why the 2007 MPEC filter [S042] and QP-diving [S049] stayed reports, and why lines were left.
- **Attribution.** For most 2013–2026 team papers the cards cannot separate his contribution; the method evidence from them is the team's record [S145; S150; S164; S165; S167].
- Field boundary softened (correction 7): [S031 pp. 12–15, 18; S048 pp. 3, 7–10; S041 pp. 16–20; S094 arXiv pp. 2, 18; S099 preprint pp. 12–14; S096 arXiv pp. 1–3].
- The "Not read" bullet is replaced by the coverage and gaps bullets (correction 9).

### Review fixes (T3.6)

- The remaining-gaps bullet now follows 08 §11: six unreadable texts [S005; S008; S017; S024; S038; S109]; [S004] and six more without an open text; the FilMINT per-instance appendix [S015]; the Correction's silence on the worked example [S162 pp. 1–2]. The "Claimed but unverified" bullet gets back the qualifiers of the pre-synthesis text (Fletcher's words in an interview Leyffer conducted; a co-signed society decision; no erratum).

### Before T3.6 (moved verbatim)

**Honest Boundary**

This skill is distilled from public information and has these limits:

- **No essay or interview by Leyffer on how he does research.** The stated method is rebuilt from talks, slides, retrospectives, auto-captioned lectures and 2026 repository files (only the conDFO brief treated as his own text) [02 Gaps].
- **Tacit gaps**: how he reads a solver log at a glance, finds the smallest counterexample, decides a formulation is "horrible", rules on a proof gap. Only outputs are visible.
- **Supervision** rests on three thesis acknowledgements; nothing on meetings, draft feedback or a stuck junior [04 §3.1].
- **Not read**: journal full texts of the 1994 OA, 2002 filter, FilMINT, Minotaur and McCormick papers.
- **No referee reports, rejections or rebuttals.** Reasons for the Uno claim narrowing, the unpublished lines (QP-diving, 2007 MPEC filter) and every exit are undocumented.
- **Shared credit**: his share in the filter work and team frameworks cannot be separated (zero Minotaur commits, 12 author tags; 17 Uno commits) [03 E31, E34].
- **Field boundary**: local, NLP-solver-centred methods; global certificates, polyhedral and conic relaxation theory and convex-hull work belong to other members.
- **Era and resources**: Dundee practices suit a lone researcher; Argonne frameworks and long-lived libraries need a laboratory and postdocs.
- **Claimed but unverified** (never methods): clear papers and short proofs (Fletcher's words in an interview Leyffer conducted; praise of others' proofs); proposal advice and "write the call" (one deck each); "there are no stupid questions" (once, ASR); problems people want solved should drive research (practice mixed; Tension 1); Fletcher's single-precision habit passed on; in-person meetings for students (a co-signed society decision); a gap in the 2002 filter-SQP corollary proof (agent-written logbook, unverified, no erratum) [02 §1.4, §2.5, §6.1, §6.2, §7.6; 03 E59; 04 §5].
- **Research date**: 2026-10-10. Leyffer is active (four journal papers, a Correction and new repositories in the last year); later work is not covered. Update this skill periodically, at least yearly.

<a id="corrections"></a>

## Corrections from the full texts

SKILL.md lists ten corrections, one line each (eleven until item 11, 08 item 13, was dropped after T3.6, when the Activation Rules took it over; see the How to Use section above); this section gives them in full. Source: 08 §3.2 (copied verbatim below), §3.1 and §10.

### 08 §3.2, verbatim

1. **Method 6 step 1 (ordering).** Qualify "linear, then convex, then nonconvex" with *then test the ranking under the algorithm you will run* [S016 pp. 67, 81; S003 p. 15; S070 preprint p. 20].
2. **Method 5 step 5 and Workflow D step 5 (rule of thumb).** Add the thesis's third row, QP/NLP-based B&B for general-integer, large-gap problems [S016 p. 83].
3. **Method 3 step 3.** Locating the faulty proof step happened in revision; the first versions publish the checked counterexample alone [S067 pp. 6–7; D001 pp. 4, 8].
4. **Method 3 evidence (Maratos).** Anchor the example to the filter papers [S001 pp. 7–8; S019 p. 8]; the nonmonotone filter paper is the redesign, not the example [S040 p. 4].
5. **Method 2 step 5.** Change the label *Inferred adjustment: what the critics found missing [05 §7]; he does not state it.* to *practised in coauthored work since 2013* [S002 p. 22; S147 p. 3; S126 pp. 24–25; S144 p. 11; S085 p. 23; S096 arXiv pp. 6, 9].
6. **Method 4 limitations.** Add that application models in team papers are often shared only on request [S043 p. 23; S100 p. 6; S143 p. 28].
7. **Heuristic 3 (contested).** Add the theory-first filter and MPEC papers [S026 pp. 1–15; S042 p. 23; S108 p. 12].
8. **Field boundary and Roundtable blind spot ("global certificates").** Soften to *not his main line*: a 2004–2008 excursion into global optimization (a small proof tree certifying a local solver's VaR answer [S031 pp. 12–15, 18], a trust-region global method [S048 pp. 3, 7–10], branch-and-refine for nonconvex MINLP [S041 pp. 16–20]) and coauthored global methods since 2021 [S094 arXiv pp. 2, 18; S099 preprint pp. 12–14; S096 arXiv pp. 1–3].
9. **Anatomy 5 (McCormick), "Class named in 2017".** The MIPDECO name is credited to an August 2013 ExaMath13 position paper [S112 p. 2], and a public August 2013 DOE exascale-workshop deck already bore the class name [02 §2.4, §2.5]; the 2015 Oberwolfach abstract is the first carded text that uses the name [S112 pp. 1–2]; the 2013 survey already names mixed-integer optimal control as a class with a library [S002 pp. 87–94].
10. **Anatomies 1 and 3, "Journal numerics: not read".** Filter paper: the report version's numerics are now read (CUTE comparisons against a self-built Sℓ1QP at its most favourable penalty and LANCELOT) [S001 pp. 17–22]. OA paper: the 1996 preprint read has no numerics [S003 pp. 9, 12, 15], so the journal numerics remain unread; the thesis numerics are read [S016 pp. 77–83].
11. **Honest Boundary, "Not read: journal full texts of the 1994 OA, 2002 filter, FilMINT, Minotaur and McCormick papers".** Replace by: read in preprint, report or arXiv versions [S003; S001; S015; S032 TR; S096 arXiv]; journal versions not compared.
12. **Trajectory table.** Add the Argonne imaging and tomography collaborations of 2014–2021 [S059 pp. 1, 3–10; S066 pp. 8–9; S045 pp. 3–4; S090 pp. 2–4; S103 arXiv pp. 3–10], HPC load balancing 2012–2015 [S053 pp. 2, 7–8; S222 p. 1] and generator tuning 2017–2022 [S180; S044 p. 3; S052 pp. 3, 11; S136 p. 12] (section 8).
13. **Activation rule for roundtables ("no paper cards yet").** Paper cards now exist; roundtable briefs can cite card IDs.

### How SKILL.md numbers them

1 = 08 item 1; 2 = item 2; 3 = items 3 and 4; 4 = item 5; 5 = item 6; 6 = item 7; 7 = item 8; 8 = item 9; 9 = items 10 and 11; 10 = item 12; 11 = item 13 (dropped after T3.6: the Activation Rules' roundtable line now tells briefs to cite paper cards).

### Contradiction links and rejected updates (08 §3.1, §10, verbatim)

| Card | Method | What the card records | Weight |
|---|---|---|---|
| H005 | M4 | Agrees that test problems are often badly selected [H005 p. 5] | Already Inner Tension 1 |
| S144 | M4 | Code and instances not released [S144 p. 23] | Institutional; first author Vogt |
| S124 | M5 | Outperformance claim on default-like runs without a fairness rule [S124 pp. 1, 5–6] | Weak for him (other first author) |
| S164 | M5 | Runtime claim against a commercial solver without settings or a fairness rule [S164 p. 5] | Weak for him (other first author) |
| S160 | M5 | Only a same-budget random baseline [S160 arXiv pp. 5–8] | Weak for him (last author) |

None of these removes a method: the methods describe his algorithm papers; the contradictions describe parts of the team's applied record. The variant notes in section 2 carry them.

1. A separate method or heuristic for *relax, round, improve*: it is the field's standard pipeline; its distinctive part (integer trust regions) is already Method 2 evidence [S088; S144; S115].
2. A separate heuristic for *price the inner re-solve*: covered by Method 1 step 3 and Heuristic 7; added as a Method 1 step instead [S010; S049; S149].
3. A separate heuristic for *replace a parameter by an acceptance test*: it is the content of the filter base (Method 2, Anatomy 3); added as a Method 2 practice note [S001; S048; S077].
4. Promoting proof inheritance to a core method: Heuristic 5 already covers it and exclusivity fails [S003; S009; S114].
5. A separate heuristic for control reruns: Method 6 step 3 already makes the log the first evidence; added as a step [S020; S064; S168].
6. Committee and community reports as method evidence: not his voice [S025; S133; S163].
7. Editorial curation, newsletter channel, maturity-gap and flexibility framings: no explanatory power for how he does research [H010; H011; H012; H004; S196].
8. *Couple, don't alternate* as Method 1 practice: attribution to him not established [S045; S090; S103].
9. Rewriting Method 4 as *always release code*: the record is mixed; recorded as a variant only [S084; S144].
10. Treating the three Method 5 contradictions as refuting the method: weak voice (other first authors) [S124; S164; S160].
11. Reader notes about internal inconsistencies of individual works (typos, a table that disagrees with the text) as evidence about the researcher: excluded under the house rule; they are reading notes, not findings.
12. Page-cited claims from abstract-, metadata- or unreadable-level cards: not allowed; such cards are cited by ID only [S004; S030; S196].

### Review fixes (T3.6)

- SKILL.md item 8 read "MIPDECO dates to 2013, public in 2015, not 2017", which made 2015 the first public naming; the 2013 workshop deck was already public [02 §2.4, §2.5]. Item 8 now reads "MIPDECO dates to 2013 (position paper and public workshop deck), not 2017" [S112 p. 2; 02 §2.4]. The 08 §3.2 copy above follows the corrected 08.
- Item 3 adds the version read [D001 arXiv pp. 4, 8]; item 11 says that the Roundtable Card now tells briefs how to cite.

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Corrections from the full texts**

1. Method 6 step 1: the linear > convex > nonconvex order is a default to re-test [S070 preprint p. 20].
3. Method 3: the faulty PIPA step was named only in revision [S067 pp. 6–7; D001 arXiv pp. 4, 8]; the Maratos example is in the filter papers [S001 pp. 7–8].
4. Method 2 step 5: practised since 2013, not only inferred [S126 arXiv pp. 24–25].
5. Method 4: application models often shared only on request [S043 p. 23].
6. Heuristic 3: the theory-first side is wider [S026 pp. 1–15].
8. McCormick anatomy: MIPDECO dates to 2013 (position paper and public workshop deck), not 2017 [S112 p. 2; 02 §2.4].
9. Journal texts once "not read" were read as preprints or reports; OA journal numerics still unread [S003].

### Review fixes (T3.7)

- Items 4 and 5 read again as before T3.7 ("practised since 2013", "shared only on request"). The count at the top of this section said eleven, stale since item 11 was dropped after T3.6; it now says ten.

<a id="candidate-pool"></a>

## Candidate pool (not promoted)

| Candidate | Cards (count) | Why it stays in the pool |
|---|---|---|
| Relax, round with structure, improve locally | S088, S115, S134, S143, S144, S145, S043 (7) | The field's standard decomposition for mixed-integer control; its distinctive improvement step is filed under Method 2 |
| Couple, don't alternate (joint inversion) | S045, S090, S103 (3) | One 2019 imaging collaboration; his role not identifiable; no statement; common in imaging |
| Precision as a tunable algorithmic resource | H005, S082, S025 (3; 2 in his voice) | One project (2016) on a side line left later; S025 is committee voice |
| Editorial curation; newsletter as a fast channel; curating overlooked work | H012, H011, H010, H005 (4) | Service practice, no research-method content |
| Relaxation strength by set equivalence plus a witness | S041, S087, S120 (3) | Field-standard proof style; kept as a proof device |
| Benchmark, fit, optimize, execute for HPC allocation | S053, S222, S107 (3; one project line) | One application line |
| Flexibility-versus-solver-capability framing of MINLP | S196, S004 (2; abstract level) | Third occurrence still missing; the survey frames generality and difficulty differently [S002 p. 5] |
| Maturity-gap framing | H004, S021 (2) | Framing, two cards |
| Custom bounding pair when no solver handles the instance | S129, S037 (2; one manuscript) | One project |
| Structural constraints that make a surrogate safe for its optimizer | S044, S052 (2; one project) | Filed as Method 6 evidence |
| Collapse an inner optimization in closed form | S145, S150 (2) | Two cards, one year |
| Exploration–exploitation acquisition objective | S165, S160 (2; one paper) | One paper |
| Bilevel model as motivation for a heuristic | S135, S124 (2) | Two cards |
| Consensus copy of binaries in ADMM | S124, S164 (2) | Two cards |
| Feasibility phase by freezing the leader; NCP warm start for MPCCs | S018, S063 (2) | Two cards |
| Validation without ground truth (perturbation, consensus median) | S086, S090 (2) | Imaging collaborations |
| Single cards | S009 (rate-based trigger), S040 (two-regime acceptance), S012 (windowed penalty test), D001 (ared/pred as diagnostic), S011 (restricted model first), S047 (sweep data seed a surrogate), S060 (ε-constraint sweep), S111 (conservative surrogate), S156 (convexifying assumption), S006 (minimal algorithmic checkpoint), S113 (basin map), S085 (sweep past the theorem's range), S119 (notation chosen for numerics), S163 (solver-developer survey) | One card each; several kept in the technique inventory |

<a id="sources-papers"></a>

## Sources: primary papers listed before T3.6

SKILL.md now gives DOIs inline and points to the card key below; the earlier list follows.

### Before T3.6 (moved verbatim)

**Papers (primary)**

- Fletcher, Leyffer, "Solving mixed integer nonlinear programs by outer approximation", Math. Program. 66 (1994), doi:10.1007/BF01581153
- Leyffer, "Integrating SQP and Branch-and-Bound for Mixed Integer Nonlinear Programming", Comput. Optim. Appl. 18(3) (2001), doi:10.1023/A:1011241421041; report NA/182, https://optimization-online.org/wp-content/uploads/2000/08/208.pdf
- Fletcher, Leyffer, "Nonlinear programming without a penalty function", Math. Program. 91(2) (2002), doi:10.1007/s101070100244; theory: doi:10.1137/S105262340038081X, doi:10.1137/S1052623499357258
- Fletcher, Leyffer, "Solving mathematical programs with complementarity constraints as nonlinear programs", Optim. Methods Softw. 19(1) (2004), doi:10.1080/10556780410001654241; Fletcher, Leyffer, Ralph, Scholtes, "Local Convergence of SQP Methods for Mathematical Programs with Equilibrium Constraints", SIAM J. Optim. 17(1) (2006), doi:10.1137/S1052623402407382
- Abhishek, Leyffer, Linderoth, "FilMINT: An Outer Approximation-Based Solver for Convex Mixed-Integer Nonlinear Programs", INFORMS J. Comput. 22(4) (2010), doi:10.1287/ijoc.1090.0373
- Belotti, Kirches, Leyffer, Linderoth, Luedtke, Mahajan, "Mixed-integer nonlinear optimization", Acta Numerica 22 (2013), doi:10.1017/S0962492913000032
- Mahajan, Leyffer, Linderoth, Luedtke, Munson, "Minotaur: a mixed-integer nonlinear optimization toolkit", Math. Program. Comput. 13(2) (2021), doi:10.1007/s12532-020-00196-1
- Leyffer, Manns, "McCormick envelopes in mixed-integer PDE-constrained optimization", Math. Program. 218 (2025), doi:10.1007/s10107-024-02181-1; Correction, doi:10.1007/s10107-026-02330-8
- Vanaret, Leyffer, "Implementing a unified solver for nonlinearly constrained optimization", Math. Program. Comput. (2026), doi:10.1007/s12532-026-00310-9
- Further Leyffer papers: identifiers are given inline where cited (each Crossref-checked 2026-10-10); not inline elsewhere: IMA volume doi:10.1007/978-1-4614-1927-3; Uno R package doi:10.32614/cran.package.uno

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Papers (primary)**

- DOIs inline where cited; every carded work by id, with authors, venue and DOI or arXiv id, in the ledger's card key (references/research/09-evidence-ledger.md#card-key); the earlier paper list: references/research/09-evidence-ledger.md#sources-papers.

<a id="sources-secondary"></a>

## Sources: students, collaborators and peers

### Review fixes (T3.6)

- SKILL.md's Sources line now carries the DOIs of Wächter and Biegler 2005, Benson et al. 2006 and Nurkanović, Pozharskiy and Diehl, which had appeared only here; thesis and genealogy links stay here.

### Before T3.6 (moved verbatim; SKILL.md now points here)

**Students, collaborators and peers (secondary)**

- Theses: Abhishek 2008, https://web.archive.org/web/20100617083653/http://coral.ie.lehigh.edu/pubs/files/abhishek_phd_thesis.pdf; Kim 2022, https://hdl.handle.net/11299/252329; Curtis 2007, doi:10.21985/n2r99v
- Mathematics Genealogy, https://www.mathgenealogy.org/id.php?id=282807
- Bonami et al., Discrete Optim. 5(2) (2008), doi:10.1016/j.disopt.2006.10.011; Hijazi, Bonami, Ouorou, INFORMS J. Comput. 26(1) (2014), doi:10.1287/ijoc.1120.0545
- Kronqvist, Bernal, Lundell, Grossmann, Optim. Eng. 20 (2019), doi:10.1007/s11081-018-9411-8; Kronqvist, Bernal, Grossmann, Math. Program. 180 (2020), doi:10.1007/s10107-018-1356-3; Tamm, Kronqvist, arXiv:2606.26897
- Byrd, Curtis, Nocedal, SIAM J. Optim. 20(5) (2010), doi:10.1137/080738222; Gould, Toint, Math. Program. 122(1) (2010), doi:10.1007/s10107-008-0244-7; Wächter, Biegler, SIAM J. Optim. 16(1) (2005), doi:10.1137/S1052623403426556
- Benson, Sen, Shanno, Vanderbei, Comput. Optim. Appl. 34(2) (2006), doi:10.1007/s10589-005-3908-8; Nurkanović, Pozharskiy, Diehl, Vietnam J. Math. 53(3), doi:10.1007/s10013-024-00704-z
- Papers by other members named in the card (Duran and Grossmann 1986; Tawarmalani and Sahinidis 2005; Misener and Floudas 2014; Burer 2009; Del Pia, Dey and Molinaro 2017) carry their DOIs there; Borchers, Mitchell, Comput. Oper. Res. 21(4) (1994), doi:10.1016/0305-0548(94)90024-8
- Mittelmann MINLP benchmark, https://plato.asu.edu/ftp/minlp.html

### Before T3.7 (moved verbatim)

T3.7 shortened or moved these SKILL.md lines; their wording before that pass follows (unchanged lines are not repeated).

**Students, collaborators and peers (secondary)**

- Theses (Abhishek 2008, Kim 2022, Curtis 2007), Mathematics Genealogy, and the peers' papers cited above (Bonami et al. 2008; Hijazi, Bonami, Ouorou 2014; Kronqvist et al. 2019, 2020; Tamm, Kronqvist; Byrd, Curtis, Nocedal 2010; Gould, Toint 2010; Wächter, Biegler 2005, doi:10.1137/S1052623403426556; Benson et al. 2006, doi:10.1007/s10589-005-3908-8; Nurkanović, Pozharskiy, Diehl, doi:10.1007/s10013-024-00704-z); the other DOIs are inline above; thesis and genealogy links: references/research/09-evidence-ledger.md#sources-secondary. Mittelmann MINLP benchmark, https://plato.asu.edu/ftp/minlp.html

<a id="card-key"></a>

## Card key

Every card id cited in SKILL.md, this ledger or the technique catalog: year, title (as in `07-paper-cards.md`), authors and venue with DOI or arXiv id (from `../sources/publications/works.json`; author lists as on Google Scholar, where "..." marks a truncated list; the card's header line gives the version read), read level and batch file in `cards/`. Pages may be cited only for full and partial cards.

| Card | Year | Title | Authors | Venue; DOI or arXiv | Read level | Batch |
|---|---|---|---|---|---|---|
| D001 | 2005 | The penalty interior-point method fails to converge | Sven Leyffer | Optim. Methods Softw. 20(4-5): 559-568; doi:10.1080/10556780500140078; arXiv:math/0310357 | full | c05 |
| H001 | 2017 | Design, Optimization, and Control of Complex Interconnected Systems (DocSis) | Mihai Anitescu, Sven Leyffer, Todd Munson, Stefan Wild | DOE-ASCR Applied Mathematics PI Meeting White Paper; doi:10.6084/m9.figshare.5307067.v1 | full | s08 |
| H004 | 2017 | Nonlinear Optimization and Beyond | Sven Leyffer | INFORMS Optimization Society Newsletter 7(2):3-11 | full | c12 |
| H005 | 2015 | It's to Solve Problems: An Interview with Roger Fletcher | Sven Leyffer | OPTIMA 99, December 2015 | full | c11 |
| H006 | 2014 | Writing for Success: Applying for Funding | Sven Leyffer | SIAM Blogs, November 2014 | abstract | a2-01 |
| H009 | 2010 | SIAG/OPT Views-and-News, Volume 21, No. 2, December 2010: 'Environmental Optimization' (issue editor) | Sven Leyffer (editor) | SIAG/OPT Views-and-News 21(2) | full | s04 |
| H010 | 2010 | SIAG/OPT Views-and-News, Volume 21, No. 1, October 2010 (issue editor) | Sven Leyffer (editor) | SIAG/OPT Views-and-News 21(1) | partial | s04 |
| H011 | 2009 | SIAG/OPT Views-and-News 20(1), December 2009: 'The Public Side Of Optimization' (issue editor) | Sven Leyffer (editor) | SIAG/OPT Views-and-News 20(1) | full | s03 |
| H012 | 2008 | SIAG/OPT Views-and-News 19(2), December 2008: SIAM OP08 (issue editor) | Sven Leyffer (editor) | SIAG/OPT Views-and-News 19(2) | full | s03 |
| H014 | 2020 | Compact Representations of BFGS Matrices | J. J. Brust, S. Leyffer, C. G. Petra | Argonne National Laboratory, MCS Division Preprint ANL/MCS-P9279-01… | partial | s09 |
| S001 | 2002 | Nonlinear programming without a penalty function | R Fletcher, S Leyffer | Mathematical programming; doi:10.1007/s101070100244 | full | c03 |
| S002 | 2013 | Mixed-integer nonlinear optimization | P Belotti, C Kirches, S Leyffer, J Linderoth, J Luedtke, A Mahajan | Acta Numerica; doi:10.1017/s0962492913000032 | full | c09 |
| S003 | 1994 | Solving mixed integer nonlinear programs by outer approximation | R Fletcher, S Leyffer | Mathematical programming; doi:10.1007/bf01581153 | full | c02 |
| S004 | 2012 | Mixed integer nonlinear programming | J Lee, S Leyffer | Springer Science & Business Media; doi:10.1007/978-1-4614-1927-3 | abstract | a2-01 |
| S005 | 2002 | On the global convergence of a filter--SQP algorithm | R Fletcher, S Leyffer, PL Toint | SIAM Journal on Optimization; doi:10.1137/s105262340038081x | unreadable | c03 |
| S006 | 2014 | Addressing failures in exascale computing | M Snir, RW Wisniewski, JA Abraham, SV Adve, S Bagchi, P Balaji, J Belak, ... | The International Journal of High Performance Computing Applications; doi:10.1177/1094342014522573 | full | c10 |
| S007 | 2002 | Global convergence of a trust-region SQP-filter algorithm for general nonlinear programming | R Fletcher, NIM Gould, S Leyffer, PL Toint, A Wächter | SIAM Journal on Optimization; doi:10.1137/s1052623499357258 | full | c03 |
| S008 | 2006 | Local convergence of SQP methods for mathematical programs with equilibrium constraints | R Fletcher, S Leyffer, D Ralph, S Scholtes | SIAM Journal on Optimization; doi:10.1137/s1052623402407382 | unreadable | c06 |
| S009 | 2001 | Integrating SQP and branch-and-bound for mixed integer nonlinear programming | S Leyffer | Computational optimization and applications; doi:10.1023/a:1011241421041 | full | c02 |
| S010 | 1998 | Numerical experience with lower bounds for MIQP branch-and-bound | R Fletcher, S Leyffer | SIAM Journal on Optimization; doi:10.1137/s1052623494268455 | full | c02 |
| S011 | 2010 | Solving multi-leader–common-follower games | S Leyffer, T Munson | Optimisation Methods & Software; doi:10.1080/10556780903448052 | full | c07 |
| S012 | 2006 | Interior methods for mathematical programs with complementarity constraints | S Leyffer, G López-Calva, J Nocedal | SIAM Journal on Optimization; doi:10.1137/040621065 | full | c06 |
| S013 | 2004 | Solving mathematical programs with complementarity constraints as nonlinear programs | R Fletcher, S Leyffer | Optimization Methods and Software; doi:10.1080/10556780410001654241 | full | c05 |
| S014 | 1998 | User manual for filterSQP | R Fletcher, S Leyffer | Numerical Analysis Report NA/181, Department of Mathematics, Univer… | full | c02 |
| S015 | 2010 | FilMINT: An outer approximation-based solver for convex mixed-integer nonlinear programs | K Abhishek, S Leyffer, J Linderoth | INFORMS Journal on computing; doi:10.1287/ijoc.1090.0373 | full | c07 |
| S016 | 1993 | Deterministic methods for mixed integer nonlinear programming | S Leyffer | University of Dundee | full | c01 |
| S017 | 2004 | A multidimensional filter algorithm for nonlinear equations and nonlinear least-squares | NIM Gould, S Leyffer, PL Toint | SIAM Journal on Optimization; doi:10.1137/s1052623403422637 | unreadable | c05 |
| S018 | 2006 | Leader-Follower Equilibria for Electric Power and NO_x_ Allowances Markets | Y Chen, BF Hobbs, S Leyffer, TS Munson | Computational Management Science; doi:10.1007/s10287-006-0020-1 | full | c06 |
| S019 | 2006 | A brief history of filter methods | R Fletcher, S Leyffer, PL Toint | Preprint ANL/MCS-P1372-0906, Argonne National Laboratory, Mathemati… | full | c06 |
| S020 | 2002 | Numerical experience with solving MPECs as NLPs | R Fletcher, S Leyffer | Numerical Analysis Report NA/210, Department of Mathematics, Univer… | full | c04 |
| S021 | 2020 | A survey of nonlinear robust optimization | S Leyffer, M Menickelly, T Munson, C Vanaret, SM Wild | INFOR: Information Systems and Operational Research; doi:10.1080/03155986.2020.1730676 | full | c12 |
| S022 | 2006 | Complementarity constraints as nonlinear equations: Theory and numerical experience | S Leyffer | Optimization with Multivalued Mappings: Theory, Applications, and A…; doi:10.1007/0-387-34221-4_9 | full | c07 |
| S023 | 1999 | User manual for MINLP BB | S Leyffer | University of Dundee numerical analysis report NA/XXX 234 | full | c02 |
| S024 | 2003 | An introduction to algorithms for nonlinear optimization | NIM Gould, S Leyffer | Frontiers in Numerical Analysis: Durham 2002; doi:10.1007/978-3-642-55692-0_4 | unreadable | c04 |
| S025 | 2014 | Doe advanced scientific computing advisory subcommittee (ascac) report: top ten exascale research challenges | R Lucas, J Ang, K Bergman, S Borkar, W Carlson, L Carrington, G Chiu, ... | USDOE Office of Science (SC)(United States); doi:10.2172/1222713 | full | c11 |
| S026 | 1999 | A bundle filter method for nonsmooth nonlinear optimization | R Fletcher, S Leyffer | University of Dundee, Report NA/195 | full | s01 |
| S028 | 2013 | On branching rules for convex mixed-integer nonlinear optimization | P Bonami, J Lee, S Leyffer, A Wächter | Journal of Experimental Algorithmics (JEA); doi:10.1145/2532568 | full | c10 |
| S029 | 2009 | Applications and algorithms for mixed integer nonlinear programming | S Leyffer, J Linderoth, J Luedtke, A Miller, T Munson | Journal of Physics: Conference Series; doi:10.1088/1742-6596/180/1/012014 | full | s03 |
| S030 | 2000 | MacMPEC: AMPL collection of MPECs | S Leyffer | Argonne National Laboratory | abstract | a2-01 |
| S031 | 2004 | On the global minimization of the value-at-risk | J Pang, S Leyffer | Optimization Methods and Software; doi:10.1080/10556780410001704911; arXiv:math/0401063 | full | s02 |
| S032 | 2021 | Minotaur: A mixed-integer nonlinear optimization toolkit | A Mahajan, S Leyffer, J Linderoth, J Luedtke, T Munson | Mathematical Programming Computation; doi:10.1007/s12532-020-00196-1 | full | c12 |
| S034 | 2020 | MPEC methods for bilevel optimization problems | Y Kim, S Leyffer, T Munson | Bilevel optimization: advances and next challenges; doi:10.1007/978-3-030-52119-6_12 | full | s09 |
| S035 | 2010 | Nonlinear constrained optimization: methods and software | S Leyffer, A Mahajan | Argonee National Laboratory, Argonne, Illinois 60439 | metadata | a2-01 |
| S036 | 2017 | Optimal design and dispatch of a system of diesel generators, photovoltaics and batteries for remote locations | MS Scioletti, AM Newman, JK Goodman, AJ Zolan, S Leyffer | Optimization and Engineering; doi:10.1007/s11081-017-9355-4 | partial | s08 |
| S037 | 2014 | A mixed-integer nonlinear program for the optimal design and dispatch of distributed generation systems | KA Pruitt, S Leyffer, AM Newman, RJ Braun | Optimization and Engineering; doi:10.1007/s11081-013-9226-6 | partial | s06 |
| S038 | 2003 | Filter-type algorithms for solving systems of algebraic equations and inequalities | R Fletcher, S Leyffer | High performance algorithms and software for nonlinear optimization; doi:10.1007/978-1-4613-0241-4_12 | unreadable | s02 |
| S039 | 2002 | Solving large MINLPs on computational grids | JP Goux, S Leyffer | Optimization and Engineering; doi:10.1023/a:1021047328089 | full | s01 |
| S040 | 2012 | A nonmonotone filter method for nonlinear optimization | C Shen, S Leyffer, R Fletcher | Computational Optimization and Applications; doi:10.1007/s10589-011-9430-2 | full | c08 |
| S041 | 2008 | Branch-and-refine for mixed-integer nonconvex global optimization | S Leyffer, A Sartenaer, E Wanufelle | Preprint ANL/MCS-P1547-0908, Mathematics and Computer Science Divis… | full | s03 |
| S042 | 2007 | A globally convergent filter method for MPECs | S Leyffer, TS Munson | Preprint ANL/MCS-P1457-0907, Argonne National Laboratory, Mathemati… | full | s02 |
| S043 | 2010 | Modeling without categorical variables: a mixed-integer nonlinear program for the optimization of thermal insulation systems | K Abhishek, S Leyffer, JT Linderoth | Optimization and Engineering; doi:10.1007/s11081-010-9109-z | full | c08 |
| S044 | 2021 | Apprentice for event generator tuning | M Krishnamoorthy, H Schulz, X Ju, W Wang, S Leyffer, Z Marshall, ... | EPJ Web of Conferences; doi:10.1051/epjconf/202125103060; arXiv:2103.05748 | full | s10 |
| S045 | 2019 | Joint ptycho-tomography reconstruction through alternating direction method of multipliers | S Aslan, V Nikitin, DJ Ching, T Bicer, S Leyffer, D Gürsoy | Optics express; doi:10.1364/oe.27.009128 | full | s09 |
| S047 | 2009 | Optimization of 3D plasmonic crystal structures for refractive index sensing | J Maria, TT Truong, J Yao, TW Lee, RG Nuzzo, S Leyffer, SK Gray, ... | The Journal of Physical Chemistry C; doi:10.1021/jp9024552 | full | s03 |
| S048 | 2006 | A trust-region algorithm for global optimization | B Addis, S Leyffer | Computational Optimization and Applications; doi:10.1007/s10589-006-8716-2 | full | s02 |
| S049 | 2012 | Solving mixed-integer nonlinear programs by QP-diving | A Mahajan, S Leyffer, C Kirches | Preprint ANL/MCS-P2071-0312, Argonne National Laboratory | full | s05 |
| S051 | 2009 | Mixed-integer support vector machine | W Guan, A Gray, S Leyffer | NIPS workshop on optimization for machine learning | full | s03 |
| S052 | 2021 | Practical algorithms for multivariate rational approximation | AP Austin, M Krishnamoorthy, S Leyffer, S Mrenna, J Müller, H Schulz | Computer Physics Communications; doi:10.1016/j.cpc.2020.107663; arXiv:1912.02272 | partial | s10 |
| S053 | 2012 | Heuristic static load-balancing algorithm applied to the fragment molecular orbital method | Y Alexeev, A Mahajan, S Leyffer, G Fletcher, DG Fedorov | SC'12: Proceedings of the International Conference on High Performa…; doi:10.1109/sc.2012.62 | full | s05 |
| S054 | 2010 | Proactive energy management for next-generation building systems | VM Zavala, J Wang, S Leyffer, EM Constantinescu, M Anitescu, ... | Fourth National Conference of IBPSA-USA; doi:10.26868/30680611.2010.ts07b-01-zavala | full | s04 |
| S055 | 1999 | A note on feasibility in Benders decomposition | A Grothey, S Leyffer, KIM McKinnon | Numerical Analysis Report NA/188, Dundee University | full | s01 |
| S057 | 2003 | Mathematical programs with complementarity constraints | S Leyffer | SIAG/OPT Views-and-News | full | c05 |
| S059 | 2014 | Non-negative matrix analysis for effective feature extraction in X-ray spectromicroscopy | R Mak, M Lerotic, H Fleckenstein, S Vogt, SM Wild, S Leyffer, Y Sheynkin, ... | Faraday discussions; doi:10.1039/c4fd00023d | full | s06 |
| S060 | 2011 | Optimal response to attacks on the open science grid | M Altunay, S Leyffer, JT Linderoth, Z Xie | Computer Networks; doi:10.1016/j.comnet.2010.07.012 | full | s05 |
| S061 | 2003 | Constrained nonlinear programming for volatility estimation with GARCH models | A Altay-Salih, MC Pinar, S Leyffer | SIAM review; doi:10.1137/s003614450140011 | full | s02 |
| S063 | 2009 | A complementarity constraint formulation of convex multiobjective optimization problems | S Leyffer | INFORMS Journal on Computing; doi:10.1287/ijoc.1080.0290 | full | s03 |
| S064 | 2022 | Modeling design and control problems involving neural network surrogates: D. Yang et al. | D Yang, P Balaprakash, S Leyffer | Computational Optimization and Applications; doi:10.1007/s10589-022-00404-9; arXiv:2111.10489 | full | s12 |
| S065 | 2022 | Sequential linear integer programming for integer optimal control with total variation regularization | S Leyffer, P Manns | ESAIM: Control, Optimisation and Calculus of Variations; doi:10.1051/cocv/2022059; arXiv:2106.13453 | full | s12 |
| S066 | 2017 | Joint reconstruction of x-ray fluorescence and transmission tomography | ZW Di, S Chen, YP Hong, C Jacobsen, S Leyffer, SM Wild | Optics express; doi:10.1364/oe.25.013107 | partial | s08 |
| S067 | 2002 | The penalty interior point method fails to converge for mathematical programs with equilibrium constraints | S Leyffer | Numerical analysis report NA/208, Department of Math., University o… | full | s01 |
| S068 | 2022 | Stochastic learning approach for binary optimization: Application to Bayesian optimal design of experiments | A Attia, S Leyffer, TS Munson | SIAM Journal on Scientific Computing; doi:10.1137/21m1404363; arXiv:2101.05958 | partial | s13 |
| S069 | 2012 | A pivoting algorithm for linear programming with linear complementarity constraints | H Fang, S Leyffer, T Munson | Optimization Methods and Software; doi:10.1080/10556788.2010.512956 | full | s05 |
| S070 | 2011 | Concrete structure design using mixed-integer nonlinear programming with complementarity constraints | A Guerra, AM Newman, S Leyffer | SIAM Journal on Optimization; doi:10.1137/090778286 | full | s05 |
| S071 | 2008 | Global and finite termination of a two-phase augmented Lagrangian filter method for general quadratic programs | MP Friedlander, S Leyffer | SIAM Journal on Scientific Computing; doi:10.1137/060669930 | full | s03 |
| S072 | 2016 | A two-level approach to large mixed-integer programs with application to cogeneration in energy-efficient buildings | F Lin, S Leyffer, T Munson | Computational Optimization and Applications; doi:10.1007/s10589-016-9842-0; arXiv:1504.04589 | partial | s07 |
| S073 | 2013 | Fast response to infection spread and cyber attacks on large-scale networks | S Leyffer, I Safro | Journal of Complex Networks; doi:10.1093/comnet/cnt009; arXiv:1207.0133 | full | s06 |
| S074 | 2010 | Software for nonlinearly constrained optimization | S Leyffer, A Mahajan, JJ Cochran, LA Cox, P Keskinocak, JP Kharoufeh, ... | Preprint ANL/MCS-P1768-0610, Mathematics and Computer Science Divis…; doi:10.1002/9780470400531.eorms0570 | full | s04 |
| S075 | 1998 | Comparison of certain MINLP algorithms when applied to a model structure determination and parameter estimation problem | H Skrifvars, S Leyffer, T Westerlund | Computers & chemical engineering; doi:10.1016/s0098-1354(98)00238-5 | full | s01 |
| S077 | 2005 | The return of the active set method | S Leyffer | Oberwolfach Reports | full | c05 |
| S079 | 2013 | Regularizing bilevel nonlinear programs by lifting | K Hatz, S Leyffer, JP Schlöder, HG Bock | Argonne National Laboratory, USA | partial | s06 |
| S082 | 2016 | Doing Moore with Less--Leapfrogging Moore's Law with Inexactness for Supercomputing | S Leyffer, SM Wild, M Fagan, M Snir, K Palem, K Yoshii, H Finkel | arXiv preprint arXiv:1610.02606; arXiv:1610.02606 | full | c11 |
| S084 | 2021 | Inversion of convection-diffusion equation with discrete sources | M Sharma, M Hahn, S Leyffer, L Ruthotto, B van Bloemen Waanders | Optimization and Engineering; doi:10.1007/s11081-020-09536-5 | full | s10 |
| S085 | 2021 | Convergence of sum-up rounding schemes for cloaking problems governed by the Helmholtz equation | S Leyffer, P Manns, M Winckler | Computational Optimization and Applications; doi:10.1007/s10589-020-00262-3 | partial | s10 |
| S086 | 2014 | Unsupervised cell identification on multidimensional X-ray fluorescence datasets | S Wang, J Ward, S Leyffer, SM Wild, C Jacobsen, S Vogt | Synchrotron Radiation; doi:10.1107/s1600577514001416 | partial | s07 |
| S087 | 2023 | Learning symbolic expressions: Mixed-integer formulations, cuts, and heuristics | J Kim, S Leyffer, P Balaprakash | INFORMS Journal on Computing; doi:10.1287/ijoc.2022.0050; arXiv:2102.08351 | full | c12 |
| S088 | 2023 | Binary control pulse optimization for quantum systems | X Fei, LT Brady, J Larson, S Leyffer, S Shen | Quantum; doi:10.22331/q-2023-01-04-892; arXiv:2204.05773 | partial | s14 |
| S089 | 2021 | MINLP formulations for continuous piecewise linear function fitting | N Goldberg, S Rebennack, Y Kim, V Krasko, S Leyffer | Computational Optimization and Applications; doi:10.1007/s10589-021-00268-5 | full | s11 |
| S090 | 2019 | Optimization-based simultaneous alignment and reconstruction in multi-element tomography | Z Di, S Chen, D Gursoy, T Paunesku, S Leyffer, SM Wild, S Vogt | Optics letters; doi:10.1364/ol.44.004331 | full | s09 |
| S091 | 2023 | Binary optimal control by trust-region steepest descent | M Hahn, S Leyffer, S Sager | Mathematical Programming; doi:10.1007/s10107-021-01733-z | full | c13 |
| S092 | 2022 | Sequential linearization method for bound-constrained mathematical programs with complementarity constraints | C Kirches, J Larson, S Leyffer, P Manns | SIAM Journal on Optimization; doi:10.1137/20m1370501; arXiv:2009.14047 | partial | s13 |
| S093 | 2021 | A solution framework for linear PDE-constrained mixed-integer problems | F Gnegel, A Fügenschuh, M Hagel, S Leyffer, M Stiemer | Mathematical Programming; doi:10.1007/s10107-021-01626-1 | partial | s11 |
| S094 | 2021 | A method for convex black-box integer global optimization | J Larson, S Leyffer, P Palkar, SM Wild | Journal of Global Optimization; doi:10.1007/s10898-020-00978-w; arXiv:1903.11366 | partial | s11 |
| S096 | 2026 | McCormick envelopes in mixed-integer PDE-constrained optimization | S Leyffer, P Manns | Mathematical Programming; doi:10.1007/s10107-024-02181-1; arXiv:2406.07891 | full | c17 |
| S098 | 2010 | Optimal control model of technology transition | DA Hanson, Y Kryukov, S Leyffer, TS Munson | International journal of global energy issues; doi:10.1504/ijgei.2010.036954 | partial | s04 |
| S099 | 2021 | A bilevel approach for identifying the worst contingencies for nonconvex alternating current power systems | BC Dandurand, K Kim, S Leyffer | SIAM Journal on Optimization; doi:10.1137/19m127611x | partial | s11 |
| S100 | 2010 | Oil Spill Response Planning with MINLP | F You, S Leyffer | SIAG/OPT Views-and-News | full | s04 |
| S101 | 2001 | Generalized outer approximation | S Leyffer | Encyclopedia of Optimization; doi:10.1007/0-306-48332-7_161 | full | c03 |
| S102 | 2020 | Pufferscale: Rescaling HPC data services for high energy physics applications | N Cheriere, M Dorier, G Antoniu, SM Wild, S Leyffer, R Ross | 2020 20th IEEE/ACM International Symposium on Cluster, Cloud and In…; doi:10.1109/ccgrid49817.2020.00-75 | partial | s09 |
| S103 | 2019 | Simultaneous sensing error recovery and tomographic inversion using an optimization-based approach | AP Austin, Z Wendy, S Leyffer, SM Wild | SIAM Journal on Scientific Computing; doi:10.1137/18m121993x; arXiv:1902.02027 | full | s09 |
| S107 | 2014 | The heuristic static load-balancing algorithm applied to the community earth system model | Y Alexeev, S Mickelson, S Leyffer, R Jacob, A Craig | 2014 IEEE International Parallel & Distributed Processing Symposium...; doi:10.1109/ipdpsw.2014.177 | abstract | a2-01 |
| S108 | 2007 | A filter active-set trust-region method | MP Friedlander, NIM Gould, S Leyffer, TS Munson | Preprint ANL/MCS-P1456-0907, Mathematics and Computer Science Divis… | full | s02 |
| S109 | 1998 | On the Global Convergance of an SLP-Filter Algorithm | R Fletcher, S Leyffer, PL Toint | Department of Mathematics and Computer Science, University of Dundee | unreadable | s01 |
| S110 | 2020 | An augmented Lagrangian filter method | S Leyffer, C Vanaret | Mathematical Methods of Operations Research; doi:10.1007/s00186-020-00713-x | full | s10 |
| S111 | 2015 | Optimal response to epidemics and cyber attacks in networks | N Goldberg, S Leyffer, I Safro | Networks; doi:10.1002/net.21619 | partial | s07 |
| S112 | 2015 | Mixed-integer PDE-constrained optimization | S Leyffer, P Cay, D Kouri, B van Bloemen Waanders | Mixed-integer Nonlinear Optimization: A Hatchery for Modern Mathema… | full | c11 |
| S113 | 2015 | Visualizing and improving the robustness of phase retrieval algorithms | A Tripathi, S Leyffer, T Munson, SM Wild | Procedia Computer Science; doi:10.1016/j.procs.2015.05.205 | full | s07 |
| S114 | 2026 | A unified funnel restoration SQP algorithm | D Kiessling, S Leyffer, C Vanaret | Mathematical Programming; doi:10.1007/s10107-025-02284-3; arXiv:2409.09208 | full | c17 |
| S115 | 2023 | On convergence of binary trust-region steepest descent | P Manns, M Hahn, C Kirches, S Leyffer, S Sager | Journal of Nonsmooth Analysis and Optimization; doi:10.46298/jnsao-2023-10164; arXiv:2202.07934 | partial | s14 |
| S116 | 2012 | Modeling mixed-integer constrained optimal control problems in AMPL | C Kirches, HG Bock, S Leyffer | IFAC Proceedings Volumes; doi:10.3182/20120215-3-at-3016.00199 | full | s06 |
| S119 | 2026 | Implementing a unified solver for nonlinearly constrained optimization | C Vanaret, S Leyffer | Mathematical Programming Computation; doi:10.1007/s12532-026-00310-9; arXiv:2406.13454 | full | c18 |
| S120 | 2024 | Modeling and solving cascading failures across interdependent infrastructure systems | Y Li, K Kim, S Leyffer, M Menickelly, LP Lewis, J Bergerson | arXiv preprint arXiv:2407.16796; arXiv:2407.16796 | full | c13 |
| S121 | 2021 | Compact representations of structured BFGS matrices | JJ Brust, Z Di, S Leyffer, CG Petra | Computational Optimization and Applications; doi:10.1007/s10589-021-00297-0; arXiv:2208.00057 | partial | s11 |
| S123 | 2025 | Robust A-optimal experimental design for sensor placement in Bayesian linear inverse problems | A Attia, S Leyffer, TS Munson | SIAM/ASA Journal on Uncertainty Quantification; doi:10.1137/24m1667543; arXiv:2305.03855 | full | c14 |
| S124 | 2024 | Heuristic algorithms for placing geomagnetically induced current blocking devices | M Ryu, A Attia, A Barnes, R Bent, S Leyffer, A Mate | Electric power systems research; doi:10.1016/j.epsr.2024.110645; arXiv:2310.09409 | full | c13 |
| S126 | 2026 | A globally convergent method for computing B-stationary points of mathematical programs with equilibrium constraints | A Nurkanović, S Leyffer | Computational Optimization and Applications; doi:10.1007/s10589-026-00832-x; arXiv:2501.13835 | full | c18 |
| S127 | 2022 | State elimination for mixed‐integer optimal control of partial differential equations by semigroup theory | A Thönen, S Leyffer, S Sager | Optimal Control Applications and Methods; doi:10.1002/oca.2861 | abstract | a2-02 |
| S128 | 2022 | A mixed-integer PDE-constrained optimization formulation for electromagnetic cloaking | RH Vogt, S Leyffer, TS Munson | SIAM Journal on Scientific Computing; doi:10.1137/20m1315993 | partial | s13 |
| S129 | 2012 | Optimal design and dispatch of distributed generation systems | KA Pruitt, S Leyffer, AM Newman, RJ Braun | Preprint ANL/MCS-2004-0112, Mathematics and Computer Science Divisi… | partial | s06 |
| S132 | 2000 | On the convergence of a filter-SQP algorithm | R Fletcher, S Leyffer, P Toint | FUNDP, Faculté des Sciences. Département de Mathématique. | abstract | a2-01 |
| S133 | 2025 | Basic research needs for inverse methods for complex systems under uncertainty | J Donatelli, J Jakeman, M Shields, A Gelb, F Herrmann, S Jantre, ... | US Department of Energy (USDOE), Washington, DC (United States). Of…; doi:10.2172/2583339 | full | c14 |
| S134 | 2025 | Switching time optimization for binary quantum optimal control | X Fei, L Brady, J Larson, S Leyffer, S Shen | ACM Transactions on Quantum Computing; doi:10.1145/3670416; arXiv:2308.03132 | full | c15 |
| S135 | 2024 | A bilevel optimization framework for imbalanced data classification | K Medlin, S Leyffer, K Raghavan | arXiv preprint arXiv:2410.11171; arXiv:2410.11171 | full | c13 |
| S136 | 2022 | BROOD: Bilevel and robust optimization and outlier detection for efficient tuning of high-energy physics event generators | W Wang, M Krishnamoorthy, J Muller, S Mrenna, H Schulz, X Ju, S Leyffer, ... | SciPost Physics Core; doi:10.21468/scipostphyscore.5.1.001; arXiv:2103.05751 | partial | s13 |
| S142 | 2013 | A new perspective on convex relaxations of sparse SVM | N Goldberg, S Leyffer, T Munson | Proceedings of the 2013 SIAM International Conference on Data Mining; doi:10.1137/1.9781611972832.50 | full | s06 |
| S143 | 2025 | Augmentation algorithms for total variation-regularized integer programs | D Yang, S Leyffer, M Bakenhus | arXiv e-prints, arXiv: 2508.05822; arXiv:2508.05822 | full | c15 |
| S144 | 2025 | A mixed-integer PDE-constrained optimization formulation for constructing electromagnetic cloaks with multiple materials | RH Vogt, S Leyffer, T Munson | Computational Optimization and Applications; doi:10.1007/s10589-024-00644-x | full | c15 |
| S145 | 2025 | Binary quantum control optimization with uncertain Hamiltonians | X Fei, LT Brady, J Larson, S Leyffer, S Shen | INFORMS Journal on Computing; doi:10.1287/ijoc.2024.0560; arXiv:2401.10120 | full | c16 |
| S146 | 2021 | Concurrent optimization of capital cost and expected o&m | MJ Wagner, A Newman, D Morton, S Leyffer | National Renewable Energy Laboratory (NREL), Golden, CO (United Sta…; doi:10.2172/1770880 | partial | s12 |
| S147 | 2018 | Convex Mixed-Integer Nonlinear Optimization, I | S Leyffer, J Linderoth | Proceedings of the Summer School on Optimization of Dynamical Syste… | full | s09 |
| S149 | 2010 | Experiments with MINLP branching techniques | S Leyffer | European Workshop on Mixed Integer Nonlinear Programming | full | s04 |
| S150 | 2025 | Optimal Experimental Design of a Moving Sensor for Linear Bayesian Inverse Problems | N Aretz, T Lynn, K Willcox, S Leyffer | arXiv preprint arXiv:2509.15961; arXiv:2509.15961 | full | c16 |
| S152 | 2024 | Population balance model-based dynamic multiobjective optimization of yeast cell manufacturing | K Ganko, MD Berliner, J Rhyu, L Wu, RD Braatz, S Leyffer | IFAC-PapersOnLine 58 (14), 860-867; doi:10.1016/j.ifacol.2024.08.445 | full | c13 |
| S153 | 2021 | Wave function analysis with a maximum flow algorithm | R Shepard, SR Brozell, J Larson, P Hovland, S Leyffer | Molecular Physics 119 (13), e1861351; doi:10.1080/00268976.2020.1861351 | full | s12 |
| S155 | 2019 | A Lagrangian dual approach for identifying the worst contingencies in power systems | B Dandurand, K Kim, S Leyffer | Optimization Online | partial | s09 |
| S156 | 2015 | Oscillation Mitigation in Electric Power Grids via Semidefinite Programming | F Lin, S Leyffer | Tech. rep., Argonne National Laboratory, mathematics and Computer S… | full | s07 |
| S159 | 2026 | Using Filter Methods to Guide Convergence for ADMM, with Applications to Nonnegative Matrix Factorization Problems | R Baraldi, S Leyffer, S Wild | Journal of Optimization Theory and Applications 209 (2), 66; doi:10.1007/s10957-026-02983-7 | partial | c19 |
| S160 | 2026 | Optimizing Paths for Adaptive Fly-Scan Microscopy | Y Lu, TF Lynn, M Du, Z Di, S Leyffer | 2026 IEEE 23rd International Symposium on Biomedical Imaging (ISBI)…; doi:10.1109/isbi61048.2026.11515614 | full | c19 |
| S162 | 2026 | Correction: McCormick envelopes in mixed-integer PDE-constrained optimization | S Leyffer, P Manns | Mathematical Programming, 1-2; doi:10.1007/s10107-026-02330-8 | full | c19 |
| S163 | 2026 | Rapport de Prospective du GDR Recherche Opérationnelle et Décision (ROD) | C Artigues, N Brauner, P Fouilhoux, N Absi, AN Arslan, O Bellenguez, ... | GDR ROD; CNRS | full | c20 |
| S164 | 2025 | An Alternating Direction Method of Multipliers for Topology Optimization | H Choudhary, S Leyffer, D Yang | arXiv preprint arXiv:2509.19888; arXiv:2509.19888 | full | c16 |
| S165 | 2025 | Optimizing Paths for Adaptive Fly-Scan Microscopy: An Extended Version | Y Lu, TF Lynn, M Du, Z Di, S Leyffer | arXiv preprint arXiv:2509.01869; arXiv:2509.01869 | full | c16 |
| S166 | 2025 | A Bilevel Optimization Framework for Dynamically Correcting Imbalance in Two-class Classification Problems | K Medlin, S Leyffer, K Raghavan | 2025 International Joint Conference on Neural Networks (IJCNN), 1-8; doi:10.1109/ijcnn64981.2025.11227944 | abstract | a2-02 |
| S167 | 2025 | Sampling Imbalanced Data with Multi-objective Bilevel Optimization | K Medlin, S Leyffer, K Raghavan | arXiv preprint arXiv:2506.11315; arXiv:2506.11315 | full | c16 |
| S168 | 2024 | Remark on Algorithm 1012: Computing Projections with Large Datasets | TH Chang, LT Watson, S Leyffer, TCH Lux, HMJ Almohri | ACM Transactions on Mathematical Software 50 (2), 1-8; doi:10.1145/3656581 | full | c14 |
| S169 | 2023 | Polytopic Superset Algorithm for Nonlinear Robust Optimization | B Li, K Kim, S Leyffer | arXiv preprint arXiv:2302.12306; arXiv:2302.12306 | partial | s14 |
| S180 | 2017 | Event Generator Tuning Using HPC | A Austin, P Calafiura, X Ju, J Kowalkowski, S Leyffer, Z Marshall, ... | Argonne National Laboratory (ANL), Argonne, IL (United States); Fermi… | full | s08 |
| S185 | 2016 | A multilevel approach for a class of semidefinite programs | F Lin, Z Di, S Leyffer | 2016 American Control Conference (ACC), 7153-7158; doi:10.1109/acc.2016.7526801 | full | s07 |
| S196 | 2009 | Collaborative Research: Next-Generation Solvers for Mixed-Integer Nonlinear Programs: Structure, Search, and Implementation | S Leyffer | NSF Award Number 0830035. Directorate for Computer and Information… | abstract | a2-01 |
| S199 | 2007 | A Filter Active-Set Trust-Region (FASTr) Framework | S Leyffer | — | full | s02 |
| S215 | — | Mixed-Integer PDE-Constrained Optimization Sven Leyffer (Argonne National Laboratory)(joint work with Bart van Bloemen Waanders (Sandia National Laboratories), Mirko Hahn… | S Leyffer | — | full | s14 |
| S216 | — | Teaching PROFESSOR new math | A Austin, S Leyffer, S Mrenna, J Müller, H Schulz | — | full | s14 |
| S222 | — | The Heuristic Static Load-Balancing Algorithm Applied to CESM. | Y Alexeev, S Mickelson, S Leyffer, R Jacob, A Craig | — | full | s14 |
