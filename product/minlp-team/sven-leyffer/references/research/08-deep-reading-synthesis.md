# Sven Leyffer · Deep-reading synthesis (08)

> Synthesis of all paper cards in `cards/` (index: `07-paper-cards.md`), written 2026-11-19 for the team-synthesize stage (T3.6). It is a proposal for a conservative update of `SKILL.md` under the house rules (paper-reading-card.md §3; research-extraction-framework.md §3 and §11): only add; mark contradictions instead of deleting; existing methods get evidence, not duplicates; a new core method needs at least three distinct works plus the four-way validation. `SKILL.md` itself is not edited here.
>
> Citation form: `[S012 p. 9]` is the `[[page N]]` page of the file read for that card (the file listed in `../sources/papers/INDEX.md`). A version word (`TR`, `arXiv`, `preprint`) marks some cards read in a report, preprint or arXiv version, as the card says; other such cards are cited without one (section 1 lists them). SKILL.md marks S126 and D001 as arXiv. Abstract-, metadata- and unreadable-level cards are cited by ID only. Card voices: most works are coauthored, and from about 2013 on Leyffer is often a middle or last author, so a practice in a team paper is evidence about the team's record, not about him alone (the cards say so where it matters, e.g. the c16 batch header for S145, S150, S164, S165, S167).

---

## 1. Coverage

| Item | Count | Source |
|---|---|---|
| Card entries | 204 in 36 batch files: round 1 core c01–c20 (61 cards), supplement s01–s14 (101), round 2 abstract/metadata a2-01, a2-02 (42) | digests; 07 |
| Read level | full 120 · partial 35 · abstract 22 · metadata 21 · unreadable 6 | digests |
| Works with a card | 204 distinct IDs; INDEX.md has 211 rows (the 7 without cards are Role = skip) | INDEX.md after `mark_read_from_cards.py` |
| Coverage row (`team_status.py`) | 224 Scholar rows · 211 distinct works · 164 open full texts · 120 read in full · 35 in part · 22 abstract only · 27 metadata only incl. unreadable · 7 skipped · 329 quotes verified | 07 |
| Quote gate (2026-11-19) | 329 quotes: 323 exact, 6 equal up to spacing/symbols, 0 not found | `verify_card_quotes.py` |
| Method links | 150 of the 155 full/partial cards link to at least one of Methods 1–6; no card links to a Heuristic in `method_links` (heuristic links are in card prose) | digests |
| Pool material | 146 new-pattern candidate entries on 106 cards; 406 proof-device entries; 502 transferable-technique entries | digests |

Rows that are not research evidence: S050, S197, S209, S210, S212, S219 and S221 are junk or masthead rows; S179 is probably misattributed and S200 is unidentified (their cards say so). Committee or community voices, not his: S025, S133, S163, S148, S193. Related texts that count once when projects are counted: S020 and S013 are the same NA/210 report text [S013 TR p. 1]; S129 is the preprint of S037; S067 and D001 are two versions of the PIPA counterexample; H014 is the preprint of S121; S165 is the extended version of S160; S162 corrects S096.

Many core works were read in a preprint, report or arXiv version rather than the journal typesetting (each card says which): S001 (NA/171 revision of 2000), S003 (1996 preprint), S009 (NA/182), S015 (2008 preprint), S028 (2011 TR), S032 (2017 TR), S096 and S114 (arXiv), S119 (arXiv v2), S126 (arXiv v5). Supplement and other cards read in such versions include S010 (1995 preprint), S012 and S048 (preprints), S022 (ANL preprint), S031 and S064 (arXiv v1), S044 (arXiv v1), S065 (arXiv v3), S074 and S077 (ANL preprints), S124 (arXiv/PSCC manuscript) and D001 (arXiv v1 of 2003). Pages cited without a version word are those of the indexed file, which for these works is the version named here, not the journal. Section 11 lists what this leaves open.

---

## 2. Evidence per existing method

Counts are distinct cards whose digest links the method (E = evidence, V = variant, C = contradiction). "By period" counts evidence links per period (1993–99 / 2000–06 / 2007–12 / 2013–18 / 2019–22 / 2023–26).

| Method | Cards (E / V / C) | Full or partial | Evidence by period | Say–do after the full texts |
|---|---|---|---|---|
| M1 Own the instrument | 60 (47 / 13 / 0) | 56 | 4 / 7 / 14 / 11 / 5 / 5 (+1 undated) | ✅ stated + practised, 1993–2026 |
| M2 Base and extension | 128 (110 / 19 / 0) | 118 | 5 / 16 / 17 / 21 / 28 / 21 (+2) | ✅; step 5 moves from inferred to practised |
| M3 Counterexample discipline | 48 (39 / 11 / 0) | 48 | 4 / 9 / 6 / 5 / 7 / 8 | ✅; step 3 qualified |
| M4 Test library as instrument | 32 (24 / 6 / 2) | 31 | 2 / 7 / 8 / 4 / 2 / 1 | ✅ for algorithm test libraries; ⚠ for application models |
| M5 Calibrated claims | 103 (65 / 42 / 3) | 100 | 4 / 9 / 12 / 10 / 19 / 11 | ✅ with recurring, documented gaps |
| M6 Read the numbers, fix the formulation | 85 (77 / 8 / 0) | 83 | 4 / 9 / 16 / 19 / 16 / 12 (+1) | ✅; the linear > convex > nonconvex ordering is qualified |

### Method 1 · Own the instrument

- **Strongest practice.** The thesis names the packaged NAG solver's limits as a cost (one warm-start level, no phase I output) and uses hot starts and final-tableau pricing where he owns the code [S016 pp. 31, 40–42, 77, 80]. MIQP child bounds come from the owned QP solver's final tableau [S010 pp. 3–7]. The 1998 integrated SQP–B&B traces a restriction to the packaged solver, reads SQP linearizations as cuts and attaches through a callback after each SQP step [S009 pp. 1–2, 4–6, 10]. Strong branching reuses stored QP factors; a single QP gains a factor of 2–3, a hot-started QP up to 40 [S149 pp. 6–8; S028 TR pp. 11–14]. QP-diving is designed around the hot-startable QP layer [S049 pp. 4–7]. FilMINT is built through framework callbacks without core changes [S015 pp. 9, 18]. Minotaur and Uno decompose solvers into swappable classes and validate by rebuilding known solvers as presets [S032 TR pp. 5, 12–15, 20–21; S119 pp. 5, 14–15, 21–23]; the funnel is built by modifying the filter component [S114 arXiv pp. 2, 4, 12].
- **Stated.** In the Fletcher interview he links Dundee practice to writing software [H005 p. 4].
- **New practice the cards add (proposed steps).**
  1. *Price the inner re-solve before designing the outer loop.* The ranking of B&B against decomposition is explained by the cost of a child QP (one to two pivots) and predicted to change when nodes need several QPs [S010 p. 12]; parallel tasks were resized because warm-started NLPs took one to two QPs [S039 pp. 8–9, 14]; a timing table of NLP vs cold QP vs hot QP motivates QP-diving [S049 p. 5] and approximate strong branching [S149 p. 8; S028 TR p. 14]; in quantum control the matrix exponentials per greedy decision are counted and precomputed first [S134 arXiv pp. 7–8]. Six works, 1998–2025.
  2. *Read the outer proof for its minimal requirements and spend the slack on inexact inner solves.* The survey states that NLP-BB needs global optimality only at pruned nodes and only a branching variable elsewhere, and uses this for inexact SQP solves and QP-diving [S002 pp. 24, 29]; the thesis budgets the outer tolerance from the inner tolerances [S016 pp. 96–103]; MPECopt proves which MILP solves may stop early and checks the saving with node-count histograms [S126 pp. 29–30, 34–37]; early branching uses a convergence-rate trigger [S009 p. 9].
  3. *Unify a method family as relaxations of one exact master.* The exact but impractical reformulation is stated first and every algorithm derived as its relaxation, so worst cases and strength orders transfer [S101 pp. 3–6; S016 pp. 56–57; S002 pp. 34–35]; the Uno paper generates algorithms as combinations of ingredients and classifies fifteen solvers in one table [S119 pp. 3, 14–15].
- **Variants.** Late works integrate at the iteration level through off-the-shelf solvers' hooks rather than owned code: MILP stopped at the first improving point and LPEC outputs read as active sets, with IPOPT, Gurobi and HiGHS unmodified [S126 pp. 11, 32, 37]; adjoint callbacks of an off-the-shelf integrator [S091 pp. 20, 35]; lazy-constraint callbacks [S093 pp. 25–26; S155 pp. 11, 15]. One recent paper decomposes into separate solver blocks instead [S164 pp. 3–4]. The cost of owning a framework is stated by the Minotaur paper itself: the goal is no overhead from flexibility, not the fastest solver [S032 TR p. 16].

### Method 2 · Base and extension

- **Strongest practice.** Fletcher's phase I, exact-penalty and convex-composite machinery carried into MINLP [S003 pp. 4–5, 15–21; S016 pp. 66, 84–87]; filterSQP and the filter carried into MPECs through an AMPL interface [S020 pp. 1, 5–6, 18; S057 pp. 17–18]; the filter carried into nonsmooth, augmented-Lagrangian and nonlinear-equation methods [S019 pp. 10–15; S026 pp. 2, 6–7; S071 pp. 4–5; S110 pp. 2, 4]; MPEC-as-NLP carried up to EPECs [S011 pp. 4, 8, 12–16] and into robust optimization through a bilevel-then-MPEC recast [S021 TR pp. 12–13]; trust-region globalization and its proof carried into integer optimal control in function space [S065 pp. 2, 5–6, 17; S091 pp. 3, 26–28, 42]; ReLU networks recast as convex MINLP and as MPCC with his slack formulation [S064 pp. 14–16, 22–23]; McCormick and OBBT carried into PDE-constrained integer control [S096 arXiv pp. 2–3, 6–7, 9]; funnel and filter carried into ADMM [S164 p. 4; S159 pp. 6–16].
- **Say–do update: step 5 is practised, not only inferred.** `SKILL.md` labels step 5 (list and check the carried-in assumptions) as an inferred adjustment he does not state. The full texts show it in coauthored work from 2013 on: assumptions graded in print as most restrictive, mild or technical [S002 p. 22; S147 p. 3]; the inner NLP solver's required behaviour written as a numbered assumption with the untreated case named [S126 pp. 24–25]; the wave number kept away from Helmholtz eigenfrequencies to keep the carried-in uniqueness [S144 p. 11], and a sweep showing failure beyond the theory's small-k0 range [S085 p. 23]; state bounds called quite strong and made explicit [S096 arXiv pp. 6, 9]; unique PDE solvability listed up front [S215 p. 1]. The thesis already warned that the CQ matters more for OA than had been recognised [S016 p. 15].
- **What is carried (proposed practice note).** In most extensions the carried piece is an acceptance test that replaces a hand-set parameter or schedule: the penalty parameter [S001 pp. 1–4], forcing sequences of augmented-Lagrangian methods [S077 p. 3; S071 pp. 4–5; S110 p. 4], an arbitrary sampling radius reread as a trust-region radius [S048 p. 3], a regularization parameter shown equivalent to a radius [S108 pp. 7, 10–11], the ADMM penalty [S159 pp. 13, 16, 35; S164 p. 4]. Or it is a trust region on a new space: Hamming or ℓ1 balls on binaries with knapsack or MILP subproblems and ared/pred acceptance [S084 pp. 16–18; S065 pp. 5–6; S092 pp. 3–6; S128 pp. 12–13; S144 p. 12; S215 p. 2; S146 pp. 22–23], or a measure-space ball on control sets [S091 pp. 23–26].
- **Variants.** The carried toolkit is not always the filter/NLP base: B&B and SOS modelling into global optimization [S041 pp. 3–5, 16–19]; MILP into MINLP [S015 pp. 9–18]; multigrid into MIP and SDP [S072 arXiv pp. 3–4, 23; S185 preprint p. 5]; integer algebra [S143 pp. 4–5, 7]; conic modelling [S156 pp. 2–4]. In several facility-driven papers since 2019 the home toolkit does not travel at all (greedy paths, ADAM, policy gradients, RBF surrogates) [S160 arXiv pp. 3–5; S165 pp. 3–5; S068 pp. 2–3; S123 arXiv pp. 4, 11; S216 pp. 2–3]; he is not first author in these.

### Method 3 · Counterexample discipline

- **Strongest practice.** At least seven hand-computed smallest counterexamples in the thesis, including one against his own quadratic OA [S016 pp. 49, 62–66, 69, 93–95]; the Duran–Grossmann master broken on a two-point instance and OA's worst case on a geometric grid [S003 pp. 8, 12–14]; the Benders counterexample with the hypothesis check before any claim of error [S055 pp. 3–7]; PIPA broken on a smallest instance whose hypotheses hold, run and tabulated, with symptom and remedy [S067 pp. 3–7; D001 pp. 4–9]; three stationarity notions and SQPEC broken on two-variable examples with closed-form iterates, his own NLP approach among the targets [S042 pp. 5–8]; each penalty-update policy broken by a tiny MPCC [S012 pp. 5–7, 25–26]; Bland's rule cycling for LPCCs [S069 preprint pp. 6, 13]; the funnel run on the Maratos counterexample and its failure reported [S114 arXiv pp. 23–24]; the hypothesis check turned on his own theorem in the 2026 Correction [S162 p. 1]; a smallest instance showing a relaxation is no bound across grids [S145 arXiv pp. 16–17].
- **Stated.** He recalls looking at examples as a Dundee rule [H005 p. 4].
- **Variants.** (a) Locating the faulty proof step came in revision: the 2002 report and the 2003 arXiv version declare the PIPA theorem contradicted without naming the step [S067 pp. 6–7; D001 pp. 4, 8]; the step-naming sentence that `SKILL.md` quotes [03 E45] is from a later version, after a colleague read a draft [S067 p. 7]. (b) The smallest example is also used constructively: witness points proving a cut strictly tighter [S087 arXiv pp. 6, 11, 22–23], a two-unknown landscape map [S113 pp. 6–8], what a restriction loses [S011 pp. 21–22], a design choice justified [S013 TR p. 3; S020 p. 3]. (c) The hypothesis check is applied to benchmark failures, matching failing instances to the known absence of strongly stationary points before blaming the method [S022 p. 27]. (d) Re-anchoring: the Maratos example that broke the hope is in the filter papers [S001 pp. 7–8; S019 p. 8]; the 2012 nonmonotone filter answers that failure mode without rebuilding the example [S040 p. 4].

### Method 4 · The test library as a maintained instrument

- **Strongest practice.** Every thesis test problem published with relaxation value and integer optimum, formulation variants side by side [S016 pp. 81, 106–113]; MacMPEC launched with classification, comments, plots, a generator and contributor credit [S020 pp. 6–8, 15, 18; S013 TR pp. 6–8]; badly scaled variants added because the library was almost all well scaled [S012 pp. 21, 23, 25]; a public MacEPEC started because none existed [S011 pp. 22–24]; the DIWAL library of computer-science MINLPs started [S149 pp. 3–4, 8]; MacMPEC linearized into an LPCC set [S069 preprint p. 20]; MacMPEC judged too easy in 2026 and a public generator written for the hard case [S126 pp. 33, 35–36, 41–43]; AMPL instances and code released for MIPDECO [S084 pp. 5, 12, 18].
- **Variant (proposed limitation text).** The public-library habit holds for algorithm test sets, not for application models in team papers: models or data available only on request [S043 p. 23; S100 p. 6; S143 p. 28; H009 p. 9], and one recent code base not released (stated as not approved for release) [S144 p. 23].
- **Contradiction already in the skill.** He agreed in 2015 that test problems are often badly selected [H005 p. 5]; `SKILL.md` records this as Inner Tension 1.

### Method 5 · Calibrated claims on fairness-stated baselines

- **Strongest practice.** Five self-built codes with the same start and the same ε, meters with their weaknesses, failures kept, a rule of thumb by class and his own handicaps stated [S016 pp. 44, 77–83]; self-built competitors on the same QP solver with each problem's best branching rule [S010 pp. 10–12]; a self-built Sℓ1QP at its most favourable penalty, crashes kept, removed problems listed, losses explained by class, a claim narrowed between report revisions [S001 pp. 18–22]; a written failure taxonomy and an at-present stamp [S020 pp. 1, 9, 12, 14; S013 TR p. 1]; failures inside profiles and the theory-favoured variant reported as losing [S022 pp. 23–27]; a deliberately simple base solver so production heuristics do not mask the effect [S012 pp. 2, 20–21]; same-framework baselines with time-outs kept and the test-set filter and its bias stated [S028 TR pp. 5, 9–18, 25–34]; an equal-energy fairness rule with the median of 31 runs [S082 pp. 2–7]; evaluations as the fair unit, failures charged, versions named, logs public [S119 pp. 21–24]; one NLP solver with identical options for all methods and a common certificate as the success criterion [S126 pp. 32–37, 40].
- **Variants (method-level only).**
  - *Tuning set equals comparison set* recurs beyond FilMINT [S015 p. 27]: openly stated in the branching study [S028 TR pp. 7, 17]; per-problem penalty tuning [S079 pp. 13–15]; penalties tuned per instance [S134 arXiv pp. 15–18]; a parameter chosen on the comparison set [S114 arXiv pp. 19–20]. This strengthens the Workflow C checkpoint, which `SKILL.md` labels as inferred from one record.
  - *Baselines at default settings* rather than rebuilt at their best [S020 pp. 9, 14; S061 pp. 11, 15–18; S064 p. 16; S143 p. 22].
  - *No external baseline* in several 2022–2025 integer-control and design papers [S091 pp. 41–42; S128 pp. 15, 18; S145 arXiv pp. 2, 23, 26; S150 pp. 19–22], once with the reason that a fair comparison is hard to design [S091 p. 42]; a 2020 HPC paper states lower bounds as its replacement for a competitor [S102 p. 7].
  - *Rule of thumb incomplete in the skill*: the thesis table has a third row, QP/NLP-based B&B for general-integer problems with a large gap [S016 p. 83].
  - *Yardsticks other than competitors* (proposed practice note): exact optima on small instances before scaling [S073 arXiv pp. 6–7; S102 pp. 4–5], idealized-oracle variants [S094 arXiv pp. 16–18], an oracle-information bound used only a posteriori [S096 arXiv pp. 25, 27], four numbers on one start point (practice design, NLP root, rounded root, MINLP) [S070 preprint p. 21], an a posteriori audit of a linearized model's solution against the nonlinear model [S036 pp. 30–32].
- **Contradictions (3 cards).** In three team papers led by other first authors, outperformance claims against SCIP and Juniper, Gurobi, or a random baseline are made without a stated fairness rule or solver settings [S124 pp. 1, 5–6; S164 p. 5; S160 arXiv pp. 5–8]. The cards rate this as weak evidence about his own practice; it is evidence that Method 5 describes his algorithm papers better than the team's applied record.

### Method 6 · Read the solver's numbers, fix the formulation before the method

- **Strongest practice.** A whole paper that fixes the formulation first: divisions multiplied out for evaluability, a negative cooling power traced to fractional binaries and repaired, QPs per NLP used to rank formulations [S043 pp. 8–9, 17, 19–20, 28]; a coefficient fix that turns an unsolved instance into a sub-second solve [S032 TR pp. 22–23, 26]; a perspective reformulation worth more than 700×, reported in a co-signed overview from two cited papers' runs [S029 pp. 5–6]; slack complementarity and the ≤ form, a misattributed published failure corrected from the model file, and a solver failure called a formulation failure [S020 pp. 1, 3, 5, 10–12]; the importance-of-slacks section with two failure examples [H004 pp. 7–9]; domain violations moved into bounded slacks [S074 p. 15; S002 p. 15]; a Slater failure at z = 0 repaired before any algorithm change [S051 p. 3]; a CQ failure turned into a second-order cone [S142 preprint pp. 3–4]; solver logs read before blaming the problem [S084 pp. 23–24]; termination codes that read CQ failure and wrong gradients [S199 p. 14], exit states that name local infeasibility and evaluation crashes [S014 pp. 3, 8, 12–15], and Fritz John outcomes reported as such [S119 pp. 4, 18].
- **Stated.** The advice to look at numbers is Fletcher's, given in the interview Leyffer conducted, and Leyffer ties it to the Dundee habit of looking at examples [H005 p. 4]; the survey states that solvers fail because iterates cannot be evaluated [S002 p. 15].
- **Variant: the ordering is a default, not a law.** In his own studies the less linear or nonconvex form sometimes won: the smaller nonconvex BATCH-int beat the convexified binary form, and he warned that reformulation can hide nonlinearity [S016 pp. 67, 81]; linearizing reformulations can defeat quadratic OA [S003 p. 15]; convex big-M and convex-hull reformulations ran about 100× and 375× slower than the nonconvex SOS and equality forms under nonlinear B&B [S070 preprint p. 20]. Proposed change to step 1: rank linear, convex, nonconvex as the default, then test the ranking under the algorithm that will be run.
- **Proposed step: a control run before attributing a failure.** Rerun only the failing instances with the suspected cause removed (complementarity relaxed to ≤ 10⁻²; failures persist, so they are not solely due to MFCQ) [S020 pp. 10–12; S013 TR pp. 10–12]; rerun with a smooth surrogate of the nonsmooth piece to rule out the solver [S064 p. 10]; a full factorial design that isolates the factor behind the failures [S168 pp. 4–5]; move the suspected factor into the better configuration and check that it degrades [S114 arXiv p. 20]. Four projects, 2002–2026.
- **Other variants.** A solver failure read as evidence about arithmetic precision and answered by escalating precision [S082 pp. 2, 4]; integrality gap and step norms read as signals for a new branching trigger [S009 p. 9].

### Heuristics (evidence from card prose)

| Heuristic | Cards mentioning it | Update |
|---|---|---|
| H1 Ablate from a plain baseline | S015, S028, S032 (+ S012, S010) | Evidence: an ablation ladder of named builds [S015 pp. 9, 12–25]; heuristics off and solver revision recorded [S028 TR p. 5]; components added one at a time [S032 TR pp. 19, 24–27]; a simple base solver chosen on purpose [S012 p. 20]; a three-arm branching study [S010 pp. 9–10] |
| H2 Ladder of tiny classics | (none by name) | Weak evidence: validate on the univariate case before scaling [S061 p. 10]; seed a class with one tiny reproducible instance [S112 p. 2] |
| H3 Numbers first, theory second | S001, S019; contested by S026, S042 | Evidence [S001 pp. 2, 7, 13; S019 p. 4]. Contested side broadened: theory before any numbers in the bundle filter [S026 pp. 1–15], the MPEC filter [S042 p. 23] and FASTr, whose claims wait for experiments [S108 p. 12]. Proposed extension: after the proof, strip what it did not use [S001 p. 15; S019 p. 7]; analyse the plain core and show each optional accelerator cannot hurt [S110 pp. 5–6, 9–10; S092 p. 4; S071 pp. 12, 14]; keep a merit function as a proof-only ruler [S040 pp. 19–21] |
| H4 A subproblem can be the next line | S016, S069, S143 (+ S010) | Evidence [S016 p. 16; S010 p. 1; S069 preprint p. 3; S143 pp. 4–5] |
| H5 Transfer and combine proofs | S007, S012, S040, S091, S114 | Evidence plus sharpening: put the change where the analysed invariant survives [S003 p. 14; S009 p. 7; S101 pp. 4–5]; find the parameter setting of an analysed method that reduces to yours [S114 arXiv p. 11; S040 p. 12]; map KKT points between regularizations [S012 pp. 12–14]; reduce a new update to a classical one by a shift [H014 pp. 4–5; S121 arXiv p. 7]; one proof with a case per cut type [S169 p. 15] |
| H6 Agents draft, you write the brief (2026) | none | No card evidence (outside the carded works) |
| H7 Downstream use chooses upstream research | S002, S028, S039, S049, S053, S071, S077, S108, S110 | Evidence [S039 p. 5; S077 p. 2; S108 p. 4; S110 pp. 2, 7; S049 pp. 4–5; S028 TR pp. 4, 14] |
| H8 Brute-force arithmetic first; function space first | S096, S091, S065, S073, S102, S144, S150, S047, H001 | Evidence [S096 arXiv pp. 7–8, 29, 32; S091 p. 42; S065 pp. 2, 22; S144 pp. 16–17; S150 p. 22]. Variant: the 2015 MIPDECO abstract discretizes first [S112 pp. 1–2] |
| H9 Credit the corrector | H004, S002, S089, S162 | Evidence [H004 pp. 4–5; S002 p. 32; S089 p. 10]; the 2026 Correction names no corrector [S162 pp. 1–2] |
| H10 Build a new evaluation tool | S049, H014, S121, S126, S136 | Evidence [S049 pp. 11–12; H014 pp. 14–15; S126 pp. 33–37]; also theory-quantity profiles [S020 p. 13; S013 TR pp. 13–15; S088 pp. 22–24] and safeguard firing counts [S001 pp. 23–24] |

Research Taste 3 (a result is only as good as its guarantee) is mentioned in 22 cards; it is the basis of the promotion in section 4.

---

## 3. Variants and contradictions

### 3.1 The five contradiction links

| Card | Method | What the card records | Weight |
|---|---|---|---|
| H005 | M4 | Agrees that test problems are often badly selected [H005 p. 5] | Already Inner Tension 1 |
| S144 | M4 | Code and instances not released [S144 p. 23] | Institutional; first author Vogt |
| S124 | M5 | Outperformance claim on default-like runs without a fairness rule [S124 pp. 1, 5–6] | Weak for him (other first author) |
| S164 | M5 | Runtime claim against a commercial solver without settings or a fairness rule [S164 p. 5] | Weak for him (other first author) |
| S160 | M5 | Only a same-budget random baseline [S160 arXiv pp. 5–8] | Weak for him (last author) |

None of these removes a method: the methods describe his algorithm papers; the contradictions describe parts of the team's applied record. The variant notes in section 2 carry them.

### 3.2 Claims of `SKILL.md` that the full texts change (full texts win over web snippets)

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

---

## 4. Promotions

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

### Method 7 (proposed): Certify the notion you claim, grade every method by it, and print what is not certified

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

---

## 5. New heuristics

### H11 (proposed): Keep the model separate from its discretization and solve coarse to fine

**Steps.** State the problem without discretization code and let the solver choose and refine the grid [S116 pp. 3, 5]; aggregate a nonlinearity over a coarse partition before relaxing it [S096 arXiv pp. 8–9]; solve the expensive relaxation on the coarsest grid and round on a finer grid where the rounding bound allows [S145 arXiv pp. 11, 16; S144 p. 18]; warm-start each finer level with interpolated controls and multipliers and report the falling iteration count [S150 pp. 11–12, 21–23; S152 pp. 5–6]; use coarse-model solutions to restrict the fine model [S043 p. 29]; before interpreting a qualitative feature, refine and switch schemes until they agree [S098 pp. 4, 13]; report a mesh-dependence table [S115 p. 17; S093 pp. 27–29]. Multilevel restriction and aggregation for MIP and SDP belong here too [S072 arXiv pp. 7–10; S185 preprint p. 5].

**Checks.** Recurrence ✅ (2010–2026, twelve cards); say–do ⚠ (the stated rule is function space first, discretize second [02 §1.7]; the papers state the separation of model and discretization [S116 p. 5]); executable and different from the MINLP default of branch and bound on the finest mesh ✅ [S084 pp. 21–24; S091 p. 42]; exclusivity ✗ (mesh sequencing and multigrid are standard; the papers name multigrid as the source [S072 arXiv p. 3]). Heuristic, linked to Heuristic 8. Mostly team papers with other first authors.

### H12 (proposed): Show every technique on one tiny computed example, and thread one running example through theory, reformulation and code

**Steps.** After each algorithm or claim, compute a small example, usually with a figure [S016 pp. 49, 62–66; S002 pp. 7, 40–41, 48–49, 76; S126 pp. 11–14, 19–20]; audit concepts on two-variable examples before using them [S042 pp. 5–7]; carry one example through theory, reformulations and software listings [S021 TR pp. 11, 13, 15, 19–20; S032 TR pp. 5, 10, 14]; seed a new class with one tiny reproducible instance, with solver, nodes and time stated [S112 p. 2].

**Checks.** Recurrence ✅ (1993–2026); say–do ✅ partial (he recalls looking at examples as a Dundee rule [H005 p. 4]; belief B4 [02 §1.2]); executable ✅; exclusivity ✗. Heuristic. It gives the "Drafting and editing papers" row of the Stages table its first practice evidence.

**Review note (T3.6 fix).** research-extraction-framework §三 caps the heuristic tier at 10, and SKILL.md already had ten. H11 is folded into Heuristic 8 as its coarse-to-fine clause, with the caveat that the cited works are team papers led by others (Kirches, Fei, Aretz) [S116 p. 5; S145 arXiv pp. 11, 16; S150 pp. 21–23]; H12 is carried by the Stages table's drafting row as practice seen in the papers (catalog W1).

---

## 6. Candidate pool (not promoted)

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

---

## 7. Technique inventory

### 7.1 Proof devices

- **Finiteness by non-repetition:** a strict incumbent bound in the master cuts off every visited assignment; with a CQ there is no feasible descent direction [S016 pp. 61–62; S003 p. 11; S101 pp. 4, 6; S002 pp. 31–34; S147 p. 38]; variants with finitely many binary points [S084 p. 17], pointwise lower bounds [S094 arXiv pp. 10–11] and enumerated leader solutions [S120 p. 12].
- **Cut comparison through the KKT conditions:** OA cuts aggregated with KKT multipliers give the Benders cut, so Benders is never tighter [S016 pp. 56–57; S002 pp. 34–35; S147 pp. 39–40]; substituting first-order conditions shows when the two coincide [S003 pp. 20–21]; aggregating OA linearizations with multipliers gives a valid underestimating cut [S055 p. 9].
- **Filter and trust-region template:** blocked-area counting, a small-radius lemma chain, a split on infinitely versus finitely many filter or h-type iterations, a radius window wider than the reduction factor [S007 pp. 13–22; S026 pp. 9–15; S042 pp. 16–21; S040 pp. 10–15; S110 pp. 11–13; S114 arXiv pp. 14–18; S126 pp. 29–31; S092 p. 9].
- **Reduction to an analysed case** [S009 p. 7; S101 pp. 4–5; S012 pp. 12–14; S040 p. 12; S114 arXiv p. 11; S002 pp. 24, 37–38; H014 pp. 4–5; S134 arXiv pp. 11–12].
- **Closed-form iterates of a smallest counterexample, then a run** [S055 p. 5; S067 pp. 4–6; D001 pp. 4–8; S020 p. 3; S042 p. 8; S034 p. 15; S003 pp. 12–13].
- **Multiplier structure under CQ failure:** the minimal element of the multiplier ray, the on/off-manifold case split, basis-by-basis superlinear convergence [S057 pp. 16–17; S022 pp. 12, 18–22; H004 p. 8].
- **Proof-only ruler:** an exact penalty used only inside the analysis of a penalty-free method [S040 pp. 19–21].
- **Outcome theorems** (KKT / Fritz John / infeasible stationary / restoration failure) [S019 pp. 7–8; S108 p. 19; S110 p. 13; S119 pp. 18–19; S126 pp. 30–31].
- **Function-space devices for integer control:** direct method, Γ-convergence, a signed-measure derivative on set space, weak-* convergence of sum-up rounding [S096 arXiv pp. 7, 13–14, 33–34; S162 p. 2; S091 pp. 6–12; S085 p. 15; S065 pp. 3–5].
- **Relaxation strength with explicit witnesses** [S041 pp. 12–15, 20–21; S087 arXiv pp. 6–11; S120 pp. 8–9; S142 preprint p. 6; S089 p. 8].
- **Rounding-error bounds** by Taylor expansion of propagators and a convex-combination contradiction [S134 arXiv pp. 8–9, 33–36; S088 p. 13; S145 arXiv pp. 14–16].
- **Operation counts before experiments** [S016 pp. 41–42; S010 p. 7; S134 arXiv pp. 7–8; S103 arXiv p. 10; S168 pp. 3–4]; **a tolerance chain** from inner tolerances [S016 pp. 97–98, 102–103]; **a budget-equivalence bound** confronted with one measurement [S082 p. 7].

### 7.2 Design moves

- Reuse what the inner solver already produced (final tableau, KKT factors, active set) [S010 pp. 4–7; S149 pp. 6–8; S028 TR pp. 11–13; S049 pp. 5–7; S001 p. 10].
- Put new information where it cannot break the guarantee (curvature in the master objective, not its constraints) [S101 pp. 4–5; S016 pp. 64–70; S003 p. 14].
- Replace a schedule or arbitrary parameter by an acceptance test or a radius [S048 p. 3; S077 p. 3; S108 pp. 7, 10–11; S110 p. 4; S159 pp. 13, 16; S164 p. 4].
- Trust regions on combinatorial or set spaces with knapsack or MILP subproblems [S084 pp. 16–18; S065 pp. 5–6; S092 pp. 3–6; S128 pp. 12–13; S091 pp. 23–26; S144 p. 12; S088 pp. 17–19].
- The model picks the branch, the NLP solver picks the point [S126 pp. 4, 11]; LP or LPEC for the active set, EQP for speed [S042 pp. 9, 21–22; S108 pp. 6–8].
- Restoration as the same loop with another filter [S199 pp. 8–9; S040 p. 23; S001 pp. 9–12].
- Big-M bounded by the trust region, or valid big-M constants derived before any speed-up [S126 pp. 15–16; S146 pp. 19–21; S064 p. 14; S032 TR p. 23; S002 pp. 41–42].
- Slack and bounded-auxiliary reformulations that keep iterates evaluable and CQs intact [H004 pp. 7–9; S034 p. 11; S074 p. 15; S002 p. 15; S124 pp. 2–3].
- Exact linearization of binary × bounded continuous terms and McCormick for continuous × continuous terms, with the error of each stated [S036 pp. 18–19; S032 TR p. 24; S060 preprint p. 10; S120 pp. 8–9].
- Precompute what does not depend on the decision [S134 arXiv pp. 7–8, 15; S084 pp. 23, 29, 31; S093 pp. 23–24].
- Coarse to fine (H11); relax, round, improve (pool) [S088 pp. 8, 12–19; S143 pp. 18–20].

### 7.3 Experiment and evaluation protocols

- One solver, one start, one tolerance for every method [S016 p. 78; S010 p. 11; S012 pp. 2, 20–21; S126 pp. 32, 34; S120 p. 14; S169 p. 17].
- Failures kept inside the statistics with a per-instance taxonomy [S020 p. 9; S022 pp. 25–27; S199 p. 14; S110 p. 15; S119 pp. 21–24; S048 pp. 11–13; S011 pp. 27–29].
- Two meters with stated purposes (subproblem counts and time) [S016 p. 78; S010 pp. 10–12; S075 pp. 8–9; S028 TR p. 9; S071 pp. 19–20].
- Control reruns and factorial failure designs [S020 pp. 10–12; S064 p. 10; S168 pp. 4–5; S114 arXiv p. 20].
- Theory-quantity profiles and certificate columns beside performance [S020 p. 13; S022 p. 27; S088 pp. 22–24; S126 pp. 34–37].
- Extended or absolute performance profiles [S049 pp. 11–12; H014 pp. 14–15; S126 p. 33].
- Exact or oracle yardsticks on small instances [S073 arXiv pp. 6–7; S102 pp. 4–5; S094 arXiv pp. 16–18; S123 arXiv pp. 17–20; S068 pp. 22–24]; a posteriori audits against the nonlinear model [S036 pp. 30–32].
- Grade all competitors by one certificate [S126 pp. 34, 40]; public generators for the hard case [S126 pp. 35–36, 41–43]; library variants added when the library is one-sided [S012 pp. 21, 23].
- Equal-budget protocols [S082 pp. 3–6; S045 pp. 10–11; S145 arXiv p. 26].
- Mesh and parameter sweeps that expose dependence [S115 p. 17; S085 p. 23; S150 pp. 21–23; S084 pp. 21–24]; per-component CPU tables [S144 pp. 14, 16; S091 p. 32; S128 pp. 18, 20].
- When methods differ on a minority of instances, show that minority [S114 arXiv p. 21; S012 pp. 23–25].
- Ablation ladders from a plain baseline [S015 pp. 9, 12–25; S028 TR p. 5; S032 TR pp. 19, 24–27].

### 7.4 Writing moves

- One computed example per technique or claim; a running example threaded through theory, reformulation and code (H12) [S016 pp. 49, 62–66; S002 pp. 7, 40–41; S126 pp. 11–14; S021 TR pp. 11–20; S032 TR pp. 5, 10, 14].
- Contribution as a list of improvements over one named predecessor, each tied to a section [S009 p. 2]; contrast paragraphs against named rivals [S040 p. 4]; chapter openings that say what improves on whom [S016 pp. 46, 58].
- Grade your own assumptions in print [S002 p. 22; S147 p. 3; S022 p. 14; S096 arXiv p. 6].
- Open a survey or a class by listing the pathologies the received verdict rests on, then show which are harmless [S057 p. 15; S126 pp. 2–3; S112 p. 1].
- Time-stamp comparisons and label literature comparisons tentative [S013 TR pp. 1, 14, 17; S020 pp. 14–15; S022 p. 29].
- Keep first-person judgements apart from theorems [S016 pp. 13, 75, 105].
- A remark that separates the method from the neighbouring class it uses as a tool [S126 pp. 17–18].
- An erratum that counts the mistakes, gives the mechanism, prints the corrected statements and says which steps are unchanged [S162 pp. 1–2].
- Close each topic with an outlook that names the maturity gap and the infrastructure to build on [H004 pp. 7, 9; S021 TR p. 22].

---

## 8. Trajectory as seen in the full texts

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

---

## 9. Collaboration pattern

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

---

## 10. Rejected updates

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

---

## 11. Open gaps

- **Unreadable core theory.** The filter-SQP global convergence paper [S005], the local SQP convergence for MPECs (Anatomy 4) [S008], the multidimensional filter [S017], the SLP-filter proof he calls the most easily understood one [S109; H004 p. 4], the filter algorithms for equations [S038] and an introduction to algorithms [S024] have broken text layers and need OCR. Until then the filter proof structure is known from the trust-region SQP-filter paper [S007 pp. 13–22] and the 2006 history [S019 pp. 7–8], and the MPEC local theory from the survey's summary [S057 p. 17; H004 p. 8]. The agent-written claim of a gap in the 2002 corollary proof stays unverified.
- **No open text.** The MINLP volume edited with Lee [S004], the MacMPEC page [S030], the 2000 filter-SQP report [S132], the methods-and-software report with Mahajan [S035], the 2009 NSF award [S196], state elimination for MIOCP [S127] and the 2025 bilevel classification paper [S166] are known from abstracts or metadata only.
- **Versions.** Journal versions were not compared with the preprints read: the 1994 OA paper's numerics remain unread because the 1996 preprint has none [S003]; the FilMINT preprint lacks its per-instance appendix [S015]; Minotaur [S032 TR], McCormick [S096 arXiv], funnel [S114 arXiv], Uno [S119] and MPECopt [S126] were read in preprint or arXiv form; the ADMM filter work is known from 2022 talk slides, not the journal paper [S159].
- **Partial reads.** 35 cards read only parts (for example proofs skimmed in [S092], [S115], [S072]); claims about those proofs are not checked.
- **After the Correction.** How the hypothesis added by the 2026 Correction bears on the worked example of the paper is not discussed in the two-page Correction [S162 pp. 1–2].
- **Not in any carded work.** Referee reports, supervision, unpublished code decisions, why the Uno claims were narrowed, why the 2007 MPEC filter [S042] and QP-diving [S049] stayed reports, and why lines were left.
- **Attribution.** For most 2013–2026 team papers the cards cannot separate his contribution; the method evidence from them is the team's record [S145; S150; S164; S165; S167].
