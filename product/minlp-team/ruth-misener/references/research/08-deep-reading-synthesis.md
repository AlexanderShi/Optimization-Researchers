# Ruth Misener · Deep-reading synthesis

> Round 1 synthesis, 2026-11-19. No earlier 08 existed, so this is the first version. It aggregates every card in `cards/*.digest.json` (146 entries; index: [07-paper-cards.md](07-paper-cards.md)) under the house rules of `references/paper-reading-card.md` §三 (conservative update) and `references/research-extraction-framework.md` §三 (four-way validation) and §十一 (quality checklist). Every statement points to card ids with file pages (the `[[page N]]` pages of the file the card read), e.g. [S011 p. 9]; abstract- and metadata-level cards are cited by id only. Quotation marks enclose either text copied from a card's verified quote list (`verify_card_quotes.py`, 2026-11-19: 222 quotes, 222 exact, 0 not found) or, where a claim of SKILL.md is discussed, SKILL.md's own wording; proposed wording and pattern names are in italics. Reading notes in the cards about the internal consistency of single works are not carried into this note (§7.4 keeps one neutral lesson). Research notes are cited as in SKILL.md, e.g. [02 C10]. This note proposes changes to `SKILL.md`; it does not edit it.

## 1. Coverage

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

## 2. Evidence per existing method

Counts are distinct cards whose digest links the method; a card can be evidence and variant at once, so rows can exceed the distinct count. Forty card entries (39 works) link no method; 34 of the entries are abstract-, metadata- or unreadable-level, and 6 are read cards of biomedical or demonstration papers [S037; S054; S073; S096; S109; S121].

| Method | Evidence (read in full/part) | Variant | Contradiction | Distinct cards |
|---|---|---|---|---|
| M1 Structure detection as "insider information" | 35 (33) | 19 | 0 | 52 |
| M2 Between formulations | 14 (14) | 21 | 1 [S056] | 33 |
| M3 The partner's trained model is the problem | 27 (25) | 20 | 0 | 44 |
| M4 Judge a component inside the whole solver | 30 (29) | 14 | 1 [S120] | 44 |
| M5 Benchmark like an auditor | 40 (36) | 41 | 6 | 81 |

### M1 · Structure detection as "insider information"

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

### M2 · Between formulations: the parameterised family between two textbook extremes

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

### M3 · The partner's trained model is the problem: constraints, then a toolkit

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

### M4 · Judge a component inside the whole solver; the default follows the evidence

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

### M5 · Benchmark like an auditor

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

### 2.6 Existing heuristics: evidence and variant notes

Digests link only methods; the cards' Method-links text also names heuristics (distinct cards: H1 12, H2 6, H3 5, H4 5, H5 0, H6 3, H7 13, H8 3, H9 3, H10 5).

- **H1 (choose by broken assumption)**: [S039 pp. 1-3; S086 pp. 1, 6; S082 pp. 2, 16; S083 p. 2; S113 pp. 1-2, 5; S115 p. 2; S097 pp. 2-3; S031 pp. 1-2; S014 pp. 1-3; S152 pp. 97-98]; "However, in an industrial chemistry setting, existing BO and active learning software would require substantial adaptation prior to deployment." [S044 p. 2]. The practitioner's operating constraints become first-class objects of the formulation: cost of moving and delayed observations [S039 pp. 3-4, 7, 9], measurement delay and costly initial-condition switches [S086 pp. 1, 6], transition constraints [S059 pp. 4-7], NChooseK and similar constraint types [S044 pp. 2-3], chemistry rules added after inspecting the optimiser's molecules [S038 pp. 17-18, 20-21]; "However, we emphasise that we cannot fully use both tools simultaneously without asynchronicity arising." [S031 p. 9].
- **H2 (industrial instance first, general class second, public stand-in)**: UCI concrete next to BASF [S020 p. 18; S023 p. 18]; GP posterior samples of anonymised BASF data [S031 pp. 17-18]; partner data withheld with public stand-ins [S066 pp. 6, 11]; partner data released openly [S097 pp. 3, 13]; a Schlumberger case with public data [S055 pp. 1, 3, 13-16]; Royal Mail data first, the general class second [S135 pp. 2, 20]. The arc in her thesis abstract, "Effectively, the arc of this dissertation is to begin with modeling and globally optimizing pooling problems and expand into an optimization framework that broadly addresses MIQCQP and MISO." [S092], and its 2025 form, "This paper aims to distill the fundamental contributions of our recent works [45, 46, 47, 48] and extend them from specific applications to general settings." [S128 p. 2]. Variant: BASF co-authors with a literature model and no stand-in [S113 pp. 1, 13, 21].
- **H3 (calibrate so the baseline wins some; weak controls)**: perturbation sizes set so some big-M problems solve [S013 p. 7]; an ℓ1 budget to keep problems solvable [S046 p. 19]; a solvent-blind floor, "many of these models fail to outperform the baseline model, which does not use any solvent information." [S097 p. 7]; pooled and no-transfer controls plus an uncorrelated synthetic case [S082 pp. 5, 9]; matched controls that differ in one component [S023 p. 22; S047 p. 8; S077 pp. 3, 9; S115 pp. 7, 22; S126 p. 18]. Variant (joint voice): a library calibrated toward hard instances, "Thanks to these extensive preliminary tests, we discarded all instances that are solved by at least 30% of the complete solvers within a time limit of 30 seconds." [S010 p. 15].
- **H4 (prove the hierarchy, experiment for the rest, label it)**: exactness proved, performance shown experimentally [S093 pp. 4, 9, 14-16]; where the theorem's conditions fail, a numerical feasibility check instead, "For the instances considered in this work, the obtained solution always turns out to be feasible." [S055 p. 19]; the failed regret analysis recorded [S081 pp. 23-26]; "We cannot prove that the algorithm will always converge to the same point, but this section demonstrates our computational experience that results of the Appendix D algorithm give answers within 10% of one another." [S065 p. 16]; "While we include some mathematical analysis in Sections 3.6 and 3.7, it is not fully rigorous and it is only meant to illustrate the importance of the Point Deletion heuristic." [S039 p. 14]. Extension in §5.
- **H5 (weakness first; concede precisely; restate novelty)**: no card names it. Related writing evidence: her method's limits listed first [S083 p. 2]; the lost guarantee written next to the gain, "Since the DSA algorithm never uses all of the data, we cannot assert global algorithm convergence." [S029 p. 6]; an appendix arranged as answers to reviewer questions [S067 pp. 20-23]. The review thread behind H5 is not a card.
- **H6 (keep the "why does it work?" question; answer it structurally)**: no longer one instance. The Floudas question [S143 p. 13] answered by the pooling complexity paper [S049 pp. 2, 32]; "The convexity result in this manuscript justifies why the Escobar and Grossmann (2010) model works better with the LMTD term moved to the objective." [S024 p. 16]; complexity tables as structural answers [S069 p. 11]. Merge with H4 proposed in §5.
- **H7 (do-not-use conditions next to the method)**: "Thus, it should be stressed that when a problem can be sufficiently described by a well-posed, explicit MINLP formulation, then CDFO methods are not recommended." [S003 p. 9]; "it is highly relevant to application domains where there is high reward for fractional improvements and sufficient time to explore the search space" [S145 p. 2]; "Problems of this size are, practically speaking, out of the range of current deterministic global optimization technology, so we are left to consider heuristics and gradient-based approaches." [S029 p. 2]; "The method suffers from standard BO challenges where the tree kernel may not be a good prior for the underlying black-box function, e.g., purely continuous feature spaces." [S047 p. 6]; "We therefore recommend BARK for BO settings where the objective is expensive to evaluate, taking at least several minutes, or having a large associated financial cost." [S081 p. 9]; [S046 pp. 10, 26; S077 pp. 1, 14; S086 p. 10; S090 p. 4; S113 p. 21; S126 p. 10; S028 pp. 14-16; S095 p. 5; S034 p. 11]. The habit runs from 2014 [S145 p. 2] to 2026 [S126 p. 10].
- **H8 (collaborate through shared code; recruit critics)**: the SnAKe critic Krause co-authors the transition-constrained BO paper [S059 p. 1]; a verification collaboration begun at a seminar, with OMLT's GNN code used to debug the SCIP implementation [S050 pp. 6, 10]; her group's ENTMOOT plugged into an industry consortium's package [S044 pp. 3-4]; Kronqvist co-authors the 2020 verification paper [S005 p. 1].
- **H9 (release per paper)**: code published with the paper [S068 pp. 2, 6, 12]; a generic and a use-case repository [S082 p. 31]; case studies importable as package examples [S057 p. 14]; benchmark case studies shipped inside the package [S041 pp. 19, 36]; the 2011 solver released with its full test suite preloaded in a GUI [S009 pp. 30-31]; code and data announced [S098 p. 7].
- **H10 (make uncertainty explicit)**: executable steps found; upgraded in §5.

## 3. Variants and contradictions

### 3.1 Variants (recorded, nothing deleted)

| Method | Variant | Cards |
|---|---|---|
| M1 | Structure kept exact rather than detected, in data-driven models: model only the unknown part and keep known analytical objectives, kinetics, additivity or conservation laws exact | [S095 pp. 3-4; S034 pp. 2, 5; S075 pp. 2, 4; S059 pp. 4, 9; S086 pp. 6, 9; S115 pp. 1-3, 6; S015 pp. 1-2; S014 pp. 6, 9] |
| M1 | Structure used to map tractability (complexity classes, a P/NP boundary) rather than detected in a solver | [S049 pp. 2-3, 22, 27-28; S069 pp. 5, 11; S135 p. 3] |
| M1 | Structure exploited through a logic solver's cores | [S058 pp. 6-8] |
| M1 | Non-detection by design in a neutral library (joint voice) | [S010 pp. 8, 15] |
| M1 | Detection without exploitation or labelled validation (step 6 absent in all four; step 5 also absent except in S068, which validated against MINLPLib labels [S068 p. 10]) | [S076 p. 5; S120 pp. 16-19; S091 p. 7; S068 p. 11] |
| M2 | Parameter set per topology from experience (2010) or numerically per instance (2021) | [S152 p. 99; S025 p. 24; S020 pp. 11, 20, 24] |
| M2 | A probabilistic knob between the nominal and the fully robust solution, exposed to the user and set by bisection or an outer BO | [S055 pp. 11-12, 21-22; S033 pp. 9-10, 15-16, 27-29] |
| M2 | Nested levels used for warm starts, not a family between extremes | [S088 pp. 8, 10-12] |
| M2 | A knob between two greedy orders fixed by analysis | [S135 pp. 3, 13, 18] |
| M2 | New parameters without a robustness sweep | [S023 pp. 2, 8, 22; S039 p. 7; S083 pp. 3, 5, 11] |
| M3 | The partner's mechanistic (not learned) model as the problem, 2014-2015 | [S085 pp. 1-2; S045 pp. 2-3; S042 pp. 7-8; H002 p. 1] |
| M3 | The model chosen for its encodability (reverse direction) | [S067 p. 20; S047 p. 6; S071 p. 3; S015 p. 1; S028 p. 16] |
| M3 | The trained score dropped: the MIP used as a constrained generator, "Instead of pursuing optimality, this paper exploits the ability of MIP in molecular generation and proposes Limeade as an end-to-end tool from real-world needs to feasible molecules." | [S090 pp. 1, 4, 11] |
| M3 | A learned surrogate fed to a local solver, or a meta-learned prior, instead of an exact encoding | [S080 pp. 8-10; S075 pp. 4-5; S113 p. 10; S086 pp. 6, 8] |
| M3 | The practitioner's trusted estimator kept and wrapped with uncertainty | [S066 pp. 3-6] |
| M3 | The switchable-options design applied outside trained models | [S041 pp. 19-21, 34; S087 pp. 3, 11; S057 pp. 2, 6, 15; S031 pp. 2, 12, 19; S086 pp. 6, 8] |
| M4 | No internal ablation; wins attributed through worked instances or solver profiles | [S004 pp. 8, 24-25; S001 pp. 17-18] |
| M4 | Stability fixed as a default with no user switch | [S032 p. 15] |
| M4 | A portfolio instead of a default; a size-split verdict with no default | [S050 p. 9; S067 pp. 9, 23] |
| M4 | Evidence stopping at the root cut loop, a stand-alone bound or a stripped-down host | [S021 pp. 26, 31-32; S078 pp. 11-12; S063 pp. 12, 14] |
| M4 | The whole-system logic outside solvers: a treatment model, a prediction pipeline, a BO loop, a statistical model | [S070 pp. 17, 24-26; S098 p. 4; S082 pp. 10-13; S115 pp. 7, 22] |
| M5 | Before the protocol (2010-2012): no competitors or independent verification | [S012 pp. 24-28; S025 pp. 26-27; S009 pp. 9, 23, 28-30; S011 pp. 16, 19] |
| M5 | One solver (her own, or one commercial code) or one competitor on one machine | [S048 pp. 15-20; S072 pp. 16-21; S040 p. 11; S046 p. 22] |
| M5 | The BO/ML-venue protocol (seeds, quantiles, matched budgets) | [S081 pp. 7-9, 17; S093 pp. 7, 9, 17-19; S035 pp. 15-16; S023 pp. 14, 17-18, 29; S059 pp. 9, 27] |
| M5 | Own tool tuned per benchmark; single runs | [S005 p. 6] |
| M5 | The baseline is the partner's historical practice | [S079 p. 28] |
| M5 | Instances excluded when a patched competitor returned infeasible points, instead of counted as its failures | [S050 p. 13] |
| M5 | A constructed best case bounds the possible gain, in place of oracle runs | [S077 pp. 9-10] |

### 3.2 Contradictions

Six digest links contradict M5, one M2 and one M4. Each is recorded; nothing is deleted.

1. **M2 ✗** [S056 p. 16]: two extremes (prediction accuracy, robustness) are each optimised and the family between them is left as future work. Method 2 is a formulation habit; in a co-authored chemometrics paper with a black-box optimiser it is not applied. Scope note.
2. **M4 ✗** [S120 p. 19]: value is claimed for detection without any branch-and-bound run. With [S068 p. 11; S091 pp. 7-10] this marks the 2017-2020 detection line as stopping short of M4's stop rule (§2 M1, M4).
3. **M5 ✗** [S091 pp. 7-10]: no benchmark set, no competitor and no detection-cost measurement in the 2019 symmetry paper.
4. **M5 ✗** [S095 pp. 5-6]: a single genetic-algorithm baseline at fixed settings in a six-page conference application, with the exclusion stated: "The computational time required to choose the next query point has not been taken into account since our focus is on applications where evaluating the black-box function is significantly more expensive than optimising for the next query point." [S095 p. 5].
5. **M5 ✗** [S090 pp. 13-19]: a tool paper evaluated by one case study, without baseline or timings.
6. **M5 ✗** [S113 pp. 14, 17-21]: the BO-venue protocol (five repetitions, unequal initial budgets, normalisation from one GP run), partly kept through a strengthened baseline, a second cost axis and a written loss [S113 pp. 14, 18-19, 21].
7. **M5 ✗** [S100 p. 101]: in the supervised MEng report an anomalous bound is attributed to numerical error with no reported re-run, the rule SKILL.md already marks as not always kept; the same report audits the published model and writes its losses in [S100 pp. 99, 116-118].
8. One more M5 contradiction link records a reading note about the internal consistency of a text, not a practice; under the house rule it is not carried forward.

None overturns a method. Together they scope M5 to solver-comparison papers, and M1 step 6 and M4's stop rule to papers whose structure her own code exploits. Proposed M5 Practice wording: *every 2013-2014 solver paper in full; strengthened rivals and profiles in later solver and formulation papers; the venue's protocol in BO and ML papers; none in detection, tool and demonstration papers*.

### 3.3 Claims of SKILL.md that the full texts contradict or correct

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

## 4. Promotions

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

## 5. New heuristics and heuristic updates

### H11 (new) · Spend the expensive relaxation only where a cheap one has failed (resolves U2)

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

### Workflow B step 4 (upgraded; not a new heuristic) · Import one device from a neighbouring community

The cluster passes three checks (§4), but Workflow B step 4 ("Borrow from a neighbour") already carries the stated claim [02 C10; 02 L2.6], so the cards go there as practice and protocol rather than as a duplicate heuristic.
- **Practice**: logarithmic encodings from the MIP community carried into piecewise McCormick relaxations and their claim tested inside the full solver [S009 pp. 3, 19, 29]; SMT in place of constraint programming inside a published decomposition, everything else held fixed [S155 p. 3; S058 pp. 1, 4-7]; approximation ratios for practitioners' heuristics in process systems engineering [S061 pp. 9-12, 35-36; S069 p. 2; S135 pp. 2-3; S079 p. 32]; argumentation as an explanation layer [S017 pp. 1, 4, 8; S073 p. 2]; MILP structure exploitation brought into neural-network verification [S005 pp. 1-2, 6]; a convex relaxation over visitation polytopes brought into BO planning [S059 pp. 4-7].
- **Protocol** (executable): name the neighbour's device and its claim; hold the rest of the published pipeline fixed and swap one component [S155 p. 3]; test the claim inside your own full solver or classes [S009 p. 29]; write where the import loses, "ManyOpt is frequently slower than state-of-the-art MINLP solvers, but it offers the trade-off of a completely different method to address the problem." [S058 p. 13]; [S155 p. 1]; for a position paper, list the intellectual differences, the definitions the other side needs, four uses each with one published example, per-problem complexity tables and numbered open questions [S069 pp. 1-6, 11, 22-23].

### H4 (extended, absorbs H6) · Prove the shape and the ceiling of your construction; label the rest experimental

- **Added step**: before shipping a relaxation or formulation family, prove one negative result about it: a class where it cannot tighten anything, routed to another tool [S011 p. 9]; a ceiling, a class whose hull no member of the family reaches [S046 pp. 12-13]; the smallest example where the hierarchy fails without its hypothesis [S040 pp. 8-9]; a point showing two relaxations are not ordered [S078 p. 12]; the hardness frontier of each restrictive assumption [S049 pp. 22, 27-28, 31]; tight worst-case ratios and integrality gaps [S061 pp. 12, 17-18; S135 p. 6]; symmetry not preserved by a partial relaxation [S120 pp. 6-9]; necessary conditions as tractable certificates when optimality is NP-hard to explain, "We have restricted attention to feasible and efficient (rather than optimal) solutions because answering and explaining why an arbitrary schedule is optimal in polynomial time is ruled out due to NP-hardness of makespan scheduling, unless P=NP." [S017 p. 3].
- **Absorbed H6**: the long-horizon form of the same act, keeping a "why does it work?" question open until a structural result answers it [S143 p. 13; S049 pp. 2, 32; S024 p. 16]. With H11 added and H6 folded into H4, the heuristic list stays at ten, inside the framework's range of 5-10. If H6 is kept separate instead, drop its "One documented instance" qualifier.

### H10 (upgraded) · Make uncertainty explicit and agree its assumptions with the stakeholder: executable steps

1. State why the uncertainty model fits the decision: "Observe here that robust optimisation is, as a conservative method for representing uncertainty, an appropriate choice for optimising a bioreactor where we have to prioritise consistent, effective cellular expansion and require a high degree of certainty that each individual bioreactor will operate." [S085 p. 4].
2. Tabulate each risky modelling assumption with its consequence if violated and how to check or mitigate it [S045 pp. 9-10].
3. Match the optimality tolerance to the parameter uncertainty: "a tight duality gap is meaningless for these uncertain parameters." [S045 p. 30].
4. Calibrate the practitioner's safety-factor baseline to the rigorous answer (the smallest factor that makes the nominal design robustly feasible) [S048 pp. 14-15, 19-20].
5. Report which decisions change under uncertainty and which stay invariant, with the physical reason [S042 p. 8; S060 p. 8]; "uncertainty in mass transfer leads us to design a smaller bioreactor with more hollow fibres." [S085 p. 5].
6. Prove feasibility where you can and measure the rest: "Theorem 1 only guarantees solution feasibility, not optimality." [S033 p. 9]; when a theorem's conditions fail, check the solution a posteriori with an exact solver or sampling [S055 pp. 19-20].
7. Take the robustness parameter off the user by bisection on sampled feasibility or an outer optimisation [S055 pp. 11-12; S033 pp. 15-16, 27-29].
8. Keep more than one analysis type: "we cannot tie ourselves to a single uncertainty analysis method; we want to build consensus between disparate analysis types." [S060 p. 11]; ship rival robust solution approaches behind one model object [S057 pp. 2, 6, 15].

Further cases: lexicographic first-stage plans that recover better after disruptions [S052 pp. 14-17, 21-23; S079 pp. 21-22]; uncertainty wrapped around the practitioner's estimator [S066 pp. 3-6].

## 6. Candidate pool (not promoted)

Counts are distinct cards naming the pattern as a new-pattern candidate (123 candidates on 90 cards), merged by meaning; each candidate is assigned to one cluster, so a card with two candidates can appear in two rows. Cards after a plus sign show the same move where the card states it outside its candidate list (method links, proof devices). *Absorbed* means the cluster became evidence for a method or heuristic above.

| Cluster (merged by meaning) | Cards | n | Decision |
|---|---|---|---|
| Cheap screen or learned selector before an expensive component | S025, S011, S004, S088, S020, S021, S119, S136 (+S005, S087, S050, S024) | 8 | H11 |
| Prove where your construction cannot help; ceiling; hardness frontier; non-containment; structure lost under relaxation | S011, S049, S078, S046, S017, S120 (+S040, S061, S135) | 6 | H4 extension |
| Import a device or guarantee notion from a neighbouring community | S009, S155, S058, S061, S138, S017, S005, S073, S079, S135, S059 | 11 | Workflow B step 4 |
| Uncertainty: tolerance matched to parameter uncertainty, assumption table, invariant vs sensitive decisions, model error folded in, robust counterpart solved globally, robustified classic benchmark, calibrated safety factor, feasibility proved and the rest measured | S045, S042, S060, S085, S118, S033, S048 (+S055, S057, S066) | 7 | H10 upgrade |
| Keep known structure exact; model only the unknown part | S095, S075, S066, S059, S015, S030 (+S034, S086, S115) | 6 | M1 variant |
| Exact encoding with a correctness proof; generalise, prove, restrict | S128, S067, S093, S051 (+S038) | 4 | M1 step 5, M3 step 2 |
| The encodable model chooses the ML model | S067, S015 (+S047, S071, S028) | 2 | M3 variant |
| Audit the inherited model or instance; codify the regulation | S025, S100, S080, S152, S024 (+S049) | 5 | M5 step 1b |
| Independent ground truth: consensus labels, enumeration, solution counting, a posteriori checks, the uncertainty signal constrained | S050, S056, S051, S055, S047 | 5 | absorbed into M5 step 6 |
| Matched controls: same samples, capacity control, constructed extreme case | S023, S126, S077 | 3 | absorbed into H3, M4 step 2 |
| Locate the win: tie counting, slicing by class, primal vs dual side, anomaly explained by model size | S009, S001, S072 | 3 | absorbed into M5 step 7, M4 step 3; §7.3 |
| Practitioner's operating constraints as first-class objects; a combination that forces a new property | S086, S044, S038, S031 (+S039) | 4 | absorbed into H1 |
| Instance ladders, portfolio-defined difficulty, natural-form instances, off-distribution test ladders | S152, S010, S113 | 3 | absorbed into M5 step 1, H3; §7.3 |
| Architecture or integration as the contribution; models-algorithms-software; release as a PhD commitment; structure carried by the modelling object | S001, S032, S145, S143, S072 | 5 | absorbed into Taste mark 5, Workflow B step 5, M1 step 4 |
| Survey layouts: component map, taxonomy with excluded cells, numbered open questions | S003, S014, S028, S069 (+S145, S015) | 4 | §7.4 WM2; note in the stages table |
| Relaxations in competition; portfolio instead of default; concede the specialised tool's turf; scope against her own core tool | S003, S050, S006, S029 | 4 | absorbed into M3 step 7, M4, H7 |
| Specific-to-general arc; settings learned on small instantiations; a distillation paper after an application run | S092, S152, S128 | 3 | absorbed into H2 |
| Partition the coupling, then tune or refine the partition size N | S013, S020 | 2 | absorbed into M2; §7.2 D1 |
| Negative results published; the failed proof route recorded | S081, S077 | 2 | absorbed into M2 stop rules, H4 |
| Approximation error controlled explicitly (accounted error, C2 extension, composition order, sampling error, dimension cap, LP on worst-case error) | S012, S024, S100, S025, S036 | 5 | §7.1-7.2 only (rejected as heuristic, §10) |
| Retrospective pool-based BO on existing data; dataset as the contribution | S081, S082, S097 | 3 | §7.3; H2 variant |
| Lexicographic first stage as a robustness device | S052, S079 | 2 | pool (one line); H10 case |
| Bilinear-term reduction by reformulation | S016, S018 | 2 | pool (abstract level only) |
| Staged fitting against a degenerate optimum | S115 | 1 | pool (statistics line) |
| Select the set statistically, sequence it combinatorially | S039 (+S031) | 1 | pool (§7.2 D8) |
| Division of labour between complementary relaxations | S011 | 1 | §7.2 D2 |
| Check the solver's own structure feature before building one | S076 | 1 | pool (M1 fact-finding) |
| Industrial line through a student project | S117 (+S100) | 1 | pool; stages-table note |
| Generate, don't optimise; encode cheap, check later | S090 | 1 | pool |
| Disclose own-solver authorship | H002 | 1 | pool: "R.M. is a co-author on the software ANTIGONE used to generate the results in this paper." [H002 p. 1] |
| Modelling advice as part of the solver contribution | S004 | 1 | pool (M1 step 4) |
| Numerical risk isolated behind a swappable interface | S068 | 1 | pool |
| Optimisation-driven data augmentation | S071 | 1 | pool |
| Parametrise and track breakpoints | S049 | 1 | §7.1 P8 |
| Hull decomposed into per-disjunct subproblems | S063 | 1 | pool |
| Reasonable, not optimal, parameters | S065 | 1 | pool (consortium) |
| Worst-case simulation to exclude a physical confounder; global optimisation as one block of a lab loop; blinded-operator validation | S037, S054, S043 | 3 | rejected: consortium practice [S043 p. 15] |

## 7. Technique inventory

### 7.1 Proof devices

- **P1 Projection identifies the bottom of a family**: Fourier-Motzkin elimination shows the coarsest member is big-M with the smallest valid M, and gives non-extended forms whose constraints double per step [S013 p. 5; S040 pp. 5-8; S046 pp. 6-7, 9-11].
- **P2 Order by aggregation, containment or refinement**: the coarser member is the finer one with blocks summed [S046 pp. 7-8; S040 p. 8; S013 p. 5]; refinement partial orders give monotone bounds [S020 p. 12]; PSD principal minors order an SDP family [S021 p. 7]; nested data matrices make coarse solutions feasible at the next level [S088 pp. 8, 11].
- **P3 A negative result at the boundary of the method**: no equation-wise cut can tighten a sum-decomposable class [S011 p. 9]; a ceiling by a facet midpoint and Jensen's inequality [S046 pp. 12-13]; a worked example where the hierarchy fails without its hypothesis [S040 pp. 8-9]; a numerical counterexample to containment [S078 p. 12]; symmetry not nested between a problem and its relaxation [S120 pp. 6-7]; hardness frontiers [S049 pp. 25-28]; tight ratios and lower bounds [S061 pp. 12, 17-18; S052 p. 14]; integrality gaps [S135 p. 6; S079 p. 8]; a non-terminating cut-loop sequence [S100 p. 80]; a conjecture verified numerically for small n only [S128 pp. 15-16].
- **P4 Exact-encoding proofs**: necessary conditions first, then a bijection by induction on shortest distance [S128 pp. 4-6, 8-9; S093 pp. 14-16; S067 pp. 18-19]; constructive completeness of symmetry breaking, contradiction at the minimal violating index [S051 pp. 4-6; S128 pp. 11-13]; an iff correspondence theorem [S017 p. 4]; a Carathéodory uniqueness count [S012 pp. 5-6].
- **P5 Limits and convexity of a singular function**: polar coordinates and L'Hôpital along the indeterminate line, a C2 extension, Hessian minors after w = e^n [S024 pp. 9-14; S100 pp. 44-62].
- **P6 Counting before building**: simplices per cube [S012 p. 4]; leaf combinations [S020 p. 8]; configurations removed per dependency [S005 p. 3]; permutation counts [S076 p. 6]; matrix-entry crossover [S120 p. 11]; model-size bookkeeping [S048 p. 12; S040 p. 5]; size accounting that explains an anomaly [S009 p. 29]; training and evaluation cost [S077 p. 9].
- **P7 Recognition tests from cited theorems**: sum decomposability and a cheap dominance test [S011 pp. 6-7]; component-wise concavity and a shift to edge-concavity [S025 pp. 23-24]; interval-Hessian classes [S032 pp. 11-12]; closed-form second derivatives [S001 p. 5].
- **P8 Parametrise the complicating variable and track breakpoints** [S049 pp. 7-12].
- **P9 Approximation-ratio template**: a lower bound, a ratio, tightness by a worst-case instance, a reduction for hardness [S061 pp. 9, 12; S069 pp. 3-4; S135 pp. 4-5, 8].
- **P10 Exchange arguments** [S017 p. 3; S055 p. 17; S135 p. 8; S058 pp. 7-8].
- **P11 Duality-based robust counterparts** [S048 pp. 6, 11; S055 pp. 7-8].
- **P12 Keep only the direction that matters**: a variance equality relaxed to a second-order-cone inequality [S047 p. 6; S081 p. 28].
- **P13 Linearise by powers-of-two weights or one-hot count indicators** [S051 pp. 8-9; S093 pp. 16-17; S067 p. 7; S128 pp. 10-15].
- **P14 Degenerate-case check**: a new bound collapses to the known one [S115 p. 5]; a new robustness notion contains the classical one [S117 pp. 85-86].

### 7.2 Design moves

- **D1 Interpolating family by grouping**: P splits, N input partitions, tree-ensemble partitions, an n-dimensional SDP family [S040 pp. 3-4; S013 p. 3; S020 pp. 11-13; S021 pp. 6-8].
- **D2 Division of labour between complementary relaxations**: covered edges removed from one family's selection graph [S011 p. 13]; a relaxation menu per term type [S025 pp. 20-24].
- **D3 Cheap gate before expensive strength** (H11) [S025 p. 24; S004 p. 14; S020 pp. 15-16].
- **D4 One interface, many switchable parts**: a polymorphic term class [S001 pp. 4, 8]; plug-in detectors [S068 pp. 9-10]; class-specific plug-ins in a class-agnostic solver [S072 pp. 2, 6, 15-16]; switchable formulations [S006 p. 4]; the restriction kept a true restriction, failing loudly [S072 p. 16].
- **D5 Keep the optimiser near the data**: PCA penalty [S020 p. 17]; distance penalty with k-means centres [S023 pp. 10-12]; data-set bounds [S051 pp. 8, 25]; a learned failure boundary [S071 pp. 3-4].
- **D6 Model only the unknown part** [S095 pp. 3-4; S075 p. 4; S059 p. 9].
- **D7 Symmetry handling that keeps a representative**: lexicographic constraints on abstract nodes [S051 pp. 3-4]; auxiliaries generated for whole orbits [S120 pp. 8-9]; indicator constraints for inactive layers [S047 p. 19]; an existential requirement moved to node 0 [S038 pp. 18-20].
- **D8 Separate the selection from the sequencing**: a statistically chosen batch ordered by a TSP [S039 p. 7]; input choice separated from fidelity choice [S031 pp. 10, 12-13].
- **D9 Ship rival approaches behind one model object** [S057 pp. 2, 6; H001].

### 7.3 Experiment and evaluation protocols

- **E1 Re-check every returned answer**: by script [S004 p. 19; S001 pp. 10-11; S032 p. 18]; by hand [S020 p. 39]; against the simulator [S071 pp. 4-5]; by sampling [S055 p. 20; S080 pp. 13-15]; by enumeration [S056 pp. 7, 15]; by consensus across solvers [S050 pp. 9, 13]; against an external record [S011 p. 16].
- **E2 Strengthen the rival**: own components given to the rival, time-counted and as oracle [S072 pp. 17-18]; its own best flag [S040 p. 11]; the fastest of four settings [S078 p. 11]; the best penalty weight [S047 p. 8]; the rival boosted with one's own criterion [S083 p. 3]; a wall-clock-matched grid [S081 p. 17]; feasibility repairs and more candidates [S067 p. 24].
- **E3 Matched controls that differ in one component** [S023 p. 22; S047 p. 8; S077 pp. 3, 9; S115 pp. 7, 22; S126 p. 18; S097 p. 7; S035 p. 24; S039 p. 8; S013 p. 7; S021 p. 18; S020 p. 20].
- **E4 Ablation inside the whole algorithm**: cumulative [S011 pp. 17-19]; every pair and all together [S087 p. 16]; component combinations [S005 p. 7]; inside a custom B&B [S020 pp. 20-26]; every new knob in an appendix, the simplest equal variant kept [S059 pp. 28-30]; stacked one row at a time [S098 p. 4].
- **E5 Calibrate difficulty**: an instance ladder from one superstructure [S152 p. 99]; phase-transition instances [S052 pp. 19, 44-45]; portfolio thresholds (joint voice) [S010 pp. 15-16]; a graded off-distribution ladder [S113 p. 15]; a budget chosen to keep problems solvable [S046 p. 19].
- **E6 Report what locates the result**: gap at the limit and a primal/dual breakdown [S072 p. 21]; time to match [S078 pp. 11, 15]; incumbent trajectories [S061 p. 34; S023 p. 19]; regret against iterations and against cost [S039 p. 8]; both cost axes [S113 p. 19]; BO curve with the MIP gap [S067 pp. 21-22]; time to optimum and to tolerance [S051 pp. 9-10]; 10%-tie win counts [S009 pp. 28-29]; slices by structural class [S001 pp. 17-18].
- **E7 Count solutions to measure symmetry removal** [S051 p. 9; S128 p. 16; S076 pp. 4-5].
- **E8 Audit the inherited model or instance** (M5 step 1b) [S025 p. 3; S100 pp. 116-118; S080 p. 13; S024 p. 24; S049 p. 28; S152 p. 98].
- **E9 Harmonise settings and stopping rules before timing** [S004 p. 19; S040 p. 11; S088 pp. 24-26; S070 pp. 23-24; S052 pp. 20-21]; "The default (automatic) parameter selection in Gurobi caused large variations in the results that were due to different solution strategies rather than differences between formulations." [S040 p. 11].
- **E10 Count set-up and modelling-layer time separately** [S057 p. 16; S078 pp. 13-14; S071 p. 13].
- **E11 Offline benchmarks from existing data when the experiment cannot be run** [S082 p. 11; S081 p. 8; S031 pp. 17-18; S034 pp. 7, 10; S099 p. 3].

### 7.4 Writing moves

Numbered WM1-WM7 (renamed from W on 2026-11-19, so they do not collide with her written statements W1-W14 of note 02).

- **WM1 Losses and scope in the abstract and conclusion** [S155 pp. 1, 6; S072 pp. 1, 21, 23; S001 p. 17; S021 p. 27; S046 p. 26; S115 p. 8; S005 p. 7; S029 pp. 4-5].
- **WM2 Reviews as maps**: one framework figure with a table per algorithmic component and a solver × feature table [S003 pp. 12, 45-55]; a taxonomy with excluded cells, "We do not discuss the low variance, low volume quadrant: such data are likely not useful for machine learning, and engineering methods should be used to generate additional data." [S014 p. 2]; variable types classified before methods [S028 pp. 14-17]; branch and bound as four components with every contribution in one slot [S145 p. 3]; numbered open questions at the end [S003 p. 26; S014 pp. 7-18; S069 pp. 22-23].
- **WM3 The contribution claimed as integration**: "the intellectual contribution is the way ANTIGONE ties together its many constitutive algorithms." [S001 p. 2]; "The primary contribution is to integrate existing ideas into an algorithmic framework for globally optimizing MISO." [S032 p. 2].
- **WM4 A worked toy before each device** [S020 pp. 4, 12, 14, 17; S040 pp. 8-9; S013 pp. 6-7; S011 p. 8; S145 p. 2; S032 p. 8].
- **WM5 Say what is not claimed**: "we do not claim that the warm start method (which we have referred as the multilevel approach) is better than any other IPM or any other alternative to solve POPs" [S088 p. 26]; "We do not claim that these hyperparameters make sense for the particular dataset, the point is to show how tailored branch-and-bound algorithms can be used to make ENTMOOT more scalable." [S023 p. 28]; [S045 p. 31; S090 p. 4; S073 p. 2; S041 pp. 33-34].
- **WM6 Disclose roles**: own-solver authorship [H002 p. 1]; contribution statements [S091 p. 10; S071 p. 13; S082 p. 35].
- **WM7 State which parts repeat an earlier paper** [S041 p. 3].
- A neutral general lesson from the reading notes (not about any one work): in long computational papers, recheck after each revision that summary counts, captions, tables and text agree.

## 8. Trajectory as seen in the full texts

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

## 9. Collaboration pattern

- **PhD and postdoc era (2009-2014)**: Floudas co-authors 29 of the works with a card; the solver and pooling papers are two- or three-author papers with him [S012; S011; S004; S001; S032; S123; S152], with Gounaris on pooling [S025] and Thompson on APOGEE [S009]. Two pieces are single-author: the 2014 CPSE newsletter [S145] and the 2016 Floudas essay [S143].
- **Biomedical consortium (2013-2018)**: Panoskaltsis (23 works), Mantalaris (21), Pistikopoulos (19), Fuentes-Garí (19), Velliou (13). She is first and corresponding author on the bioreactor optimisation papers [S045; S085; H002] and a middle author on the others [S054; S042; S037; S096].
- **Students and fellows (2016-2026)**: Tsay (18 works), S. Zhang (12), Mistry (9), Letsios (8), Kronqvist (8), Ceccon (7), Baltean-Lugojan (7), Wiebe (7), Olofsson (7), Thebelt (7), Qing (7), Folch (7), Campos (7), Sedgwick (7), Kouyialis (6), Odgers (5). Two-author papers with a student carry several lines: pooling theory [S049], LMTD convexity [S024], symmetry [S120; S076], SMT [S155], GALINI pooling [S072], ROmodel [S057], graph encodings [S128]. From 2016 the student is first author and she is last or corresponding author [S128; S090; S081; S086; S067].
- **Industry**: BASF (R. M. Lee 15 works, Shafei 10, Walz 8) from the tree paper onward [S020; S023; S047; S081; S113]; Schlumberger [S033; S048; S055]; Royal Mail [S117 p. 3; S135; S079]; Eli Lilly [S066 p. 13; S056]; IBM CPLEX developers [S021; S136]; Bayer [S041]; an Evonik-led consortium [S044].
- **Neighbouring communities at Imperial**: ML with Deisenroth (7 works) and van der Wilk (8) [S029; S075; S039; S059]; verification with Lomuscio [S005] and Huth [S058]; argumentation with Toni [S017; S073]; numerical optimisation with Parpas [S088; S078]; statistics with Filippi [S066; S115; S126]; outside optimisation, air-quality GPs begun at a Dagstuhl seminar [S098 p. 7].
- **Community roles**: Dagstuhl report co-editor [S119]; a 13-author library paper [S010]; a two-author perspective with Biegler [S015].
- **Students' projects as seeds**: two MEng projects she supervised became group papers [S100 p. 13; S024 p. 15; S117 p. 3; S135 p. 20].
- **Frequencies by period** (co-authors on ≥2 works with a card in the period): 2005-09 Floudas 5, Gounaris 4; 2010-14 Floudas 20, Fuentes-Garí 9, Velliou 8, Pistikopoulos 8, Panoskaltsis 8, Mantalaris 7, Brito dos Santos 4, Gounaris 3, Rende 3, J. Li 2, Skjäl 2, Westerlund 2, Pefani 2; 2015-19 Panoskaltsis 15, Mantalaris 14, Pistikopoulos 10, Fuentes-Garí 10, Georgiadis 7, Kouyialis 6, Olofsson 6, Deisenroth 6, Mistry 5, Baltean-Lugojan 5, Allenby 5, Velliou 5, Brito dos Santos 5, Floudas 4, Letsios 4, Kostoglou 4, Pefani 4, Wiebe 3, Cecílio 3, Bonami 3, Geris 3, Mehrian 3, Tahlawi 3, and nine at 2; 2020-24 R. M. Lee 10, Tsay 10, Thebelt 7, Kronqvist 7, Walz 7, S. Zhang 6, Ceccon 5, Shafei 5, Folch 5, Sudermann-Merx 4, Wiebe 4, Mistry 4, van der Wilk 4, Campos 4, Letsios 4, Sedgwick 3, Odgers 3, and eleven at 2; 2025-26 Tsay 8, Qing 7, S. Zhang 6, Shafei 5, R. M. Lee 5, Xie 4, van der Wilk 4, Langdon 4, Kappatou 4, Sedgwick 4, Boyne 3, and six at 2. The counts include abstract- and metadata-level cards (computed from the digests' coauthor fields).

## 10. Rejected updates

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

## 11. Open gaps

- **Abstract only**: the 2009-2012 pooling, gas-lift and crude-oil papers [S007; S008; S016; S018; S022; S027]; GloMIQO 2 [S026]; the αBB generalisation [S036]; the 2016 pooling-detector paper that is the source of SKILL.md Method 1 step 7 [S064; D001]; the 2021 PSE perspective [S002]; robust pooling and ROmodel conference versions [S118; H001]; conference abstracts [S084; S104; S127; S136; S138].
- **Text on disk but not read in full**: the 315-page PhD thesis, carded from its abstract [S092]; two one-page minlp.org problem statements [S150; S151]; the ESCAPE-28 approximation-algorithms paper, whose file held the journal version [S138].
- **Unreadable**: [S116] needs OCR or a new extraction.
- **Metadata only**: 17 works, among them the GloMIQO 2.2 test-suite report [S102], process synthesis [S019], 2009-2010 proceedings papers on pooling and piecewise approximation [S124; S125; S153], the PSE 2018 design-of-experiments paper [S074], PDE-constrained MINLP [S107] and biomedical meeting abstracts [S111; S112; S089; S101; S122].
- **Versions**: journal pagination is not available for most papers (§1); no card compares a preprint with its published version.
- **Authorship shares**: her individual role is stated only where a contribution statement exists [S091 p. 10; S066 p. 12; S071 p. 13; S082 p. 35; S043 p. 15]; section authorship of the reviews is not stated [S003; S015]; company voice in [S044].
- **Partial reads**: 23 works were read in part; for example the approximation proofs [S079; S052] and most appendix proofs of [S061] were not read.
- **Reasons for turns**: no text states why she left C++ solver development, why the detection line stopped at detection, or why the general GALINI paper stayed a preprint; the cards record dates only (§8).
- **SKILL.md items no card touches**: U1 ("fail fast"), U3, U4, U6, U9; the review exchanges behind H5 and the NeurIPS 2021 "variability" remark.
