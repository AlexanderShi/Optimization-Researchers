# Ruth Misener · 05 Peer critique: blind spots, limits of applicability, contested judgements

| Field | Value |
|---|---|
| Researcher | Ruth Misener. Imperial College London, Department of Computing. PhD Princeton 2012 with Christodoulos A. Floudas. Identifiers from team.json: DBLP 04/8800, Google Scholar `AQxtWHoAAAAJ`, ORCID 0000-0001-5612-5417 |
| Dimension | Research agent 05 of 06: peer critique (framework §二). In scope: failed or partial replications, published disagreements, public reviews, critical passages in rivals' papers, benchmark studies that include her methods, rival schools, plans that did not materialise. Extracted: blind spots, limits of applicability, and judgements shown wrong or left unproven. Each item names the critic, the source, and whether and how the critique was answered |
| Research date | 2026-10-10 |
| Sources consulted | 74 in total (list under "Sources"). Used: 58 (17 primary; 41 secondary, observed or index). Consulted but not used: 16 |
| WebSearch calls used | 2 of 4 |
| Local corpus | No user-supplied material: `references/sources/{papers,essays,software}` hold only `.gitkeep`. `talks/` holds ASR transcripts saved by sibling agents 02 and 04 during this workflow run; they are not user-supplied. Four are quoted here, and every such quote is marked **ASR**. `references/sources/private/` was not opened |
| Language | English (team.json) |

## How to read this note

- **Tags**:
  - [stated]: what Misener, or her co-authors in their own papers, said.
  - [practice]: what the record shows they did (papers, code, issue threads, release notes).
  - [observed]: what others wrote, measured or reported.
  - [inferred]: my reading; no source states it.
  - **P** marks a source that is primary for Misener (her words, her group's papers, her software). **S** marks a secondary source (critics, benchmarkers, indexes).
- **"via S2 context"** means the sentence comes from the Semantic Scholar citation-context index. The API returns verbatim snippets of the citing paper around the citation. I did **not read** the full text of those papers, so treat these quotes as leads with a known source, not as checked readings.
- **Pages** are printed page numbers where the PDF has them. Otherwise they are PDF pages of the named version; arXiv version numbers are given.
- **Quotes** are verbatim, with three conventions:
  - Typos in the original are kept and marked [sic].
  - Hyphens lost at PDF line breaks are restored.
  - ASR quotes reproduce the machine caption track, errors included.
- **Division of labour**: other notes already cover:
  - the NeurIPS 2021 review thread on partition-based ReLU formulations (`03-process-evidence.md` §5.4–5.5);
  - the withdrawn symmetry theorems (03 PE-34);
  - the group's own internal losses: APOGEE's linear-vs-logarithmic result, piecewise relaxations switched off by default in GloMIQO, and GALINI (`01-publications.md` §1.9).

  They are cross-referenced here, not repeated. This note adds what people **outside the group** found and said, and what the group did about it.
- **Each entry gives**:
  - the critic and source;
  - the claim, quoted;
  - the evidence type and era;
  - whether it was answered, how, and the evidence;
  - the research layers it informs (framework §一).

## Era and resource context of the critiques

| Code | Period | What was criticised | Her resources at the time | Who criticised |
|---|---|---|---|---|
| E-A | 2009–2016 | GloMIQO (GAMS 23.8.1, March 2012) and ANTIGONE (GAMS 24.1.1, May 2013), closed C++ solvers sold through GAMS. Piecewise-linear pooling relaxations and APOGEE (2011) | Two-author papers with Floudas, then an RAEng fellowship at Imperial. One workstation per benchmark (01 §1.1) | Rival solver developers: BARON (Sahinidis group) and SCIP (ZIB). Rival relaxation schools: multiparametric disaggregation (Castro, Grossmann), worst-case analysis of MILP relaxations (Dey, Gupte), composite-function relaxations (Tawarmalani). Application users |
| E-B | 2016–2026 | ANTIGONE, frozen at version 1.1, benchmarked against solvers that kept improving | The last new ANTIGONE library appears in GAMS 24.6.1 (18 Jan 2016; §6). After that her solver work moved to open-source Python (SUSPECT, GALINI) | Independent benchmarkers (Mittelmann), application papers, the SCIP team |
| E-C | 2018–2026 | Optimisation over trained ML models: gradient-boosted trees (2018/2021), OMLT (2022), partition-based and P-split formulations (2021–2025). Bayesian optimisation: ENTMOOT (2021), tree kernels (2022), SnAKe (2022) | Python and Pyomo, GitHub, Gurobi academic licence, BASF and EPSRC funding, papers with 4–12 authors, ML venues with public review (03 era map) | Constraint-learning groups in OR, the BO community (movement-cost BO, convergence theory), authors of competing tools, software users on GitHub |

---

## 1. Blind spots: what the methods systematically miss

### PC-01 · ANTIGONE guesses missing variable bounds, and a wrong guess can produce a wrong answer

- **The design assumption** [stated] (P). The GAMS/ANTIGONE manual (Floudas and Misener, dated 16 April 2013, still in the current GAMS documentation) states: "We assume that it is possible to infer finite bounds [x_i^L, x_i^U] on the variables participating in nonlinear terms f_m and that the image of f_m is finite on x". The LaTeX in the original is rendered here as plain text.
  - In the ANTIGONE paper, "lower bounds based on guessed variable bounds are discarded" from reported results. Agent 03 read this quote (PE-13, ANTIGONE manuscript p.11); it was not re-read here.
- **The developers knew bound inference was weak** [practice] (S, GAMS release notes):
  - GloMIQO 2.1 in GAMS 24.0.1 (24 Dec 2012) lists "additional strategies for deterministically inferring missing variable bounds".
  - ANTIGONE 1.1 and GloMIQO 2.3 in GAMS 24.1.3 (26 Jul 2013) list "improve nonlinear term bound inferences".
- **Critic 1: the BARON developers** [observed] (S). Zhang and Sahinidis, *Optim. Lett.* 10(2):325–340, 2016 (online 4 Apr 2015), DOI 10.1007/s11590-015-0880-9. On mathematical programs with complementarity constraints, via S2 context: "Antigone could not deterministically infer bounds on the complementarity expressions and, after guessing (apparently incorrect) bounds, it terminated with a grossly suboptimal solution."
  - Era E-A. The critics develop the main competing solver.
- **Critic 2, ten years later** [observed] (S). Du et al., "A production planning benchmark for real-world refinery-petrochemical complexes", arXiv:2503.22057v1 (28 Mar 2025). Set-up: GAMS 45.5.0, an i7-8700 desktop, an 18,000 s limit, ANTIGONE (1.1 by then) against BARON.
  - pp. 26–27: "Notably, ANTIGONE fails to identify any feasible solution for Cases 2 and 3, prematurely terminating before reaching the maximum runtime and providing only estimated upper bounds. The solver does not provide precise bound information when variable bounds cannot be not [sic] deterministically inferred. ANTIGONE mistakenly claims these cases are infeasible problems, whereas BARON manages to obtain feasible solutions."
  - Their explanation is worded as a guess: "The poor performance of ANTIGONE may stem from its preprocessing strategy, which involves reformulating user-defined MINLP problems before applying linear relaxations [40]."
  - They also report the opposite result, p. 29: "Upon removing the delta-base formulation, ANTIGONE outperforms BARON, delivering a better solution. However, the search process still terminates prematurely, as all nodes in the branch-and-bound tree have been explored."
- **How other solvers handle missing bounds** [observed] (S). The SCIP 8 paper (Bestuzheva et al., *J. Global Optim.* 91(2):287–310, online 14 Dec 2023, DOI 10.1007/s10898-023-01345-1, p. 303) describes three policies:
  - BARON: "BARON also prints a warning and no longer claim [sic] to have solved a problem to global optimality, i.e., it does not return a lower bound".
  - Lindo API and Octeract: they bound the variables and return the lower bound of the restricted problem.

  ANTIGONE is not part of that comparison (PC-08).
- **Answered?** No public answer found, and ANTIGONE stayed at version 1.1 (§6).
  - [inferred] The behaviour follows from a documented assumption, so it is a blind spot of scope, not a bug.
  - Neither critic reports trying user-supplied finite bounds, which the manual's assumption asks for.
- **Layers**: 5 (judging results: when a solver's "infeasible" or "optimal" can be trusted); 4 (benchmark design: bounded vs unbounded models).

### PC-02 · ANTIGONE does not recognise convexity, so convex problems get weak relaxations

- **Critic** [observed] (S). Kronqvist, Bernal, Lundell and Grossmann, "A review and comparison of solvers for convex MINLP", *Optim. Eng.* 20(2):397–455, 2019 (online 3 Dec 2018), DOI 10.1007/s11081-018-9411-8. Read in part.
  - p. 426: "AlphaECP and ANTIGONE seems to be struggling with obtaining a tight lower bound for some of the problems, since they are able to obtain solutions within 0.1% for 300 (AlphaECP) and 275 (ANTIGONE) problems, while only verifying optimality for 276 and 236 instances respectively. Since ANTIGONE is a global solver without a user-selected convex strategy, it might fail to recognize some of the problems as convex, and therefore, generate weaker relaxations."
  - p. 436: "the performance difference of ANTIGONE and Couenne compared to BARON and SCIP, may be explained with the solvers treating some of the convex functions as nonconvex, and therefore, generate unnecessarily weak relaxations."
  - The authors also protected the solver, p. 421: "BARON and ANTIGONE would, without the small perturbation, seem to terminate prematurely on a large number of instances and these would all be marked as failed by PAVER." They adjusted the gap tolerance so that the two solvers' definition of the relative gap would not count against them.
- **Status**: a hypothesis in hedged words ("might", "may be explained"), not a demonstration. Era E-B: ANTIGONE 1.1 in GAMS 25.1.2 against solvers of 2018.
- **Answered?** Not in writing. [practice] Kronqvist later joined her group as a Royal Society Newton International Fellow, 2019–21 (01 §1.1).
  - Her group was already building a convexity detector before the critique appeared: SUSPECT (Ceccon, Siirola, Misener, *Optim. Lett.* 14(4):801–814, DOI 10.1007/s11590-019-01396-y; Git tag v7 dated 18 May 2018, per 03 PE-23).
  - [inferred] This is two sides converging on the same gap, not a reply. SUSPECT is open-source Pyomo, ANTIGONE is closed C++, and the two were never connected.
- **Layers**: 3 (structure detection as a source of ideas); 4 (testing solvers on convex libraries).

### PC-03 · Factorable decomposition throws away the structure of inner functions (APOGEE and the 2012 MIQCQP relaxations; a rival school)

- **Critic** [observed] (S). Taotao He and Mohit Tawarmalani. Tawarmalani co-wrote the convexification theory behind BARON.
  - "Extracting structure from functional expressions for continuous and discrete relaxations of MINLPs", arXiv:2205.01442v1 (3 May 2022), pp. 1–2: "In contrast to our techniques, following the factorable programming paradigm, earlier MIP relaxations decompose composite functions into univariate and multilinear functions and then discretize the multilinear expressions [25, 23, 15]. Unfortunately, the decomposition step abstracts away much of the nonlinear structure." Here [25] is APOGEE (DOI 10.1016/j.compchemeng.2011.01.026) and [23] is Misener and Floudas, *Math. Program.* 2012 (DOI 10.1007/s10107-012-0555-6).
  - "MIP Relaxations in Factorable Programming", *SIAM J. Optim.* 34(3):2856–2882, 2024, DOI 10.1137/22m1515537, read as arXiv:2310.07168v3 (15 Jun 2024).
    - p. 1: "Regardless, solvers arguably ignore much of inner-function structure while relaxing composite functions, particularly while constructing discretized relaxations or if a specialized result is not already available [38, 26, 28, 23, 6]." Here [26] is ANTIGONE.
    - p. 11: "We remark that (4.11) yields tighter relaxations than those in [27, 25, 28, 18] because of the constraints u(x) ≤ s, and this change produces substantially tighter relaxations empirically, see Section 6." Here [27] is APOGEE and [25] the 2012 *Math. Program.* paper.
    - The abstract reports relaxations that "close approximately 60-70% of the gap relative to McCormick relaxations". The computational baselines are:
      - SCIP 8's root relaxation;
      - McCormick envelopes ("MC");
      - a MIP relaxation built with the formulation techniques of Huchette and Vielma ("MIP19").
    - p. 19 places their own discretised relaxation next to hers: "Relaxations similar to MIP have been proposed before [27, 25, 28, 18]. However, MIP differs since it requires fewer continuous variables and uses limited separation rounds."
    - No implementation of APOGEE was run. Their dominance over her formulations therefore rests on a formulation-level argument plus experiments against other baselines.
- **Era**: E-C critics (2022–2024) on E-A methods (2010–2012).
- **Answered?** No reply found.
- **Layers**: 1 (taste: exploit the structure of the model as written, or decompose into standard terms and then discretise); 3.

### PC-04 · Optimising over a learned model leaves its trust region: a PCA penalty against learned trust regions (the gradient-boosted-tree paper)

- **Her method** [practice] (P). Mistry, Letsios, Krennrich, Lee and Misener, *INFORMS J. Comput.* 33(3):1103–1119, 2021 (DOI 10.1287/ijoc.2020.0993), penalise solutions that lie far from a PCA subspace of the training inputs. The method was developed on an industrial BASF instance (01 §1.9 item 8; 03 PE-25).
- **Critic** [observed] (S). Shi, Emadikhiav, Lozano and Bergman, "Constraint Learning to Define Trust Regions in Optimization over Pre-Trained Predictive Models", *INFORMS J. Comput.* 36(6):1382–1399, 2024 (DOI 10.1287/ijoc.2022.0312), read as arXiv:2201.04429v3 (19 Oct 2022).
  - p. 2: "decisions produced by PMO are often unrealistic because they can be very different from what is observed historically in data. This happens because often the existing PMO frameworks ignore the trust region, i.e., ensuring that solutions to the optimization problem are similar to the data used to train the predictive models [Maragno et al., 2021, Mistry et al., 2021, Schweidtmann et al., 2022]."
  - p. 4 describes the same paper as having a trust region (see Contradictions): "Mistry et al. [2021] add a penalty term to the objective function so that solutions that lie far away from the subspace constructed by principle [sic] component analysis (PCA), are penalized."
  - p. 12: "We also run experiments with PCA as a penalty term, the same way as Mistry et al. [2021] propose. We omit these results as they are very similar to the ones reported modeling PCA via constraints."
  - p. 14: trust regions built from Mahalanobis distance and k-nearest neighbours "are better than PCA in 18 cases out of 21".
  - pp. 17–18: "The performance of trust-region constraints based on these two methods is better than two other existing approaches, namely, convex hull constraints and PCA constraints."
  - Scope: two sets of 70 synthetic datasets built from seven global-optimisation benchmark functions (§4). A wine dataset appears only as the motivating example.
- **A rival group's description** [observed] (S). Schweidtmann, Weber, Wende, Netze and Mitsos, *Optim. Eng.* 23(2):855–876, 2022 (online 12 May 2021; DOI 10.1007/s11081-021-09608-0), p. 857, list the approach among alternatives without testing it: "Mistry et al. (2018) penalize deviations from a training data mean in a space that is parameterized using principal component analysis." They propose validity domains learned by a one-class SVM instead.
- **Answered?** No reply found. Misener and Biegler's 2023 perspective, "Formulating data-driven surrogate models for process optimization" (*Comput. Chem. Eng.*, DOI 10.1016/j.compchemeng.2023.108411), does not cite Shi et al. among its 76 references (checked in the S2 reference list; the perspective itself was not read).
- **Layers**: 4 (what the benchmark measures: the true outcome at the optimiser's point); 5.

## 2. Limits of applicability

### PC-05 · Function classes ANTIGONE cannot take (trigonometric terms)

- **Scope as written** [stated] (P). The manual's "typical expressions" cover quadratic, signomial, exponential and logarithmic terms.
- **Critic** [observed] (S). Füllner and Rebennack, "Non-convex nested Benders decomposition", *Math. Program.* 196(1–2):987–1024, 2022 (online 7 Jan 2022), DOI 10.1007/s10107-021-01740-0, p. 1021: "for the valve-point instances we draw on LINDOGlobal [44], as BARON does not support sinusoidal functions. For the same reason, ANTIGONE [32], SCIP [16] and Gurobi [20] cannot be applied to the valve-point instances, so that we refer to LINDOGlobal and Couenne [5] as benchmarks."
- **Answered?** Not applicable: this is scope. Her own scoping sentence was "ANTIGONE derives the core of its strength from quadratic instances" (03 PE-31).
- **Layer**: 2 (which function classes a solver commits to).

### PC-06 · Strong on continuous nonconvex QPs, weak on binary ones (Mittelmann's QPLIB benchmarks, 2026)

All figures are [observed] (S), from the pages' own summary lines, read live on 2026-10-10. Each cell gives the number solved and, in brackets, the scaled shifted geometric mean of run times (lower is faster).

| Benchmark (page date) | Set-up | ANTIGONE 1.1 | Other solvers |
|---|---|---|---|
| Continuous Non-Convex QPLIB (17 May 2026) | 102 problems, 3 h, 8 threads, Xeon Gold 6230 | **35** (1.65) | BARON 25.12.10: 31 (1); COPT 8.0.4: 28 (1.39); MINOTAUR 0.4.1: 22 (3.12); SCIP 10.0.1: 15 (5.28) |
| Binary Non-Convex QPLIB (page header 9 May 2026) | 128 problems, 1 h, 12 threads (except SCIP and Couenne), Ryzen 9 5900X | **16** (66.4) | SHOT 1.1: 91 (1); COPT 8.0.4: 83 (2.42); BARON 25.11.17: 74 (4.03); RAPOSa 4.4.1: 69 (10.6); SCIP 10.0.0: 36 (30.8); COUENNE 0.5: 6 (79.0) |
| Discrete Non-Convex QPLIB, non-binary (12 May 2026) | 160 problems | not included | BARON, SHOT, SCIP, COPT |

- **Check**: recounting the table rows reproduces every column except BARON on the binary page (75 rows with a time, against a summary of 74).
- **Relation to Misener**: Mittelmann co-authored QPLIB with her (Furini et al. 2019; 03 S13). He is a collaborator, not an adversary.
- **Era**: ANTIGONE's code dates from 2013–2016 (§6); the solvers it is compared with were released in 2025–2026.
- **Reading** [inferred]:
  - The pattern fits her own scoping: the quadratic relaxations are the core.
  - It also fits where BARON invested after 2014. Kılınç and Sahinidis, *Optim. Methods Softw.* 33(3):540–562, 2018 (DOI 10.1080/10556788.2017.1350178), state in the abstract (via OpenAlex): "A primary development was the addition of mixed-integer linear programming relaxations to BARON's portfolio of linear and nonlinear programming relaxations". Their ANTIGONE tables were not read.
- **Answered?** No statement found.
- **Layers**: 2, 4.

### PC-07 · On large structured industrial instances, specialised decompositions beat the general solver

All [observed] (S):

- **Refinery planning, 2020.** Uribe-Rodriguez, Castro, Guillén-Gosálbez and Chachuat, *Comput. Chem. Eng.* 140:106883, 2020 (DOI 10.1016/j.compchemeng.2020.106883). Read in the accepted manuscript (Spiral hdl 10044/1/84608). They ran ANTIGONE 1.1 and BARON 18.5.8 for 10 CPU h each.
  - p. 27: "Both ANTIGONE (Plan A) and BARON (Plan B) are able to identify a feasible solution to the problem rather quickly, but no significant improvement is observed in either bounds until the maximum runtime (10 CPU hours)."
  - p. 33: "Overall, the proposed algorithm based on cluster decomposition significantly outperforms the commercial solvers ANTIGONE and BARON for the short-term planning of the IRPC."
  - Chachuat is an Imperial colleague. The GloMIQO paper thanks him for "a long conversation that sparked our reformulation strategies" (03 PE-47).
- **Blend scheduling, 2013.** Kolodziej, Grossmann, Furman and Sawaya, *Comput. Chem. Eng.* 53:122–142, 2013 (DOI 10.1016/j.compchemeng.2013.01.016), via S2 context: "As seen in Table 4, LINDOGlobal was able to converge in 96 minutes, while BARON and GloMIQO were both unable to converge to the global optimum within two hours."
- **MIQCPs, 2017.** Castro, *Optim. Methods Softw.* 32(4):719–737, 2017 (online 13 Dec 2016; DOI 10.1080/10556788.2016.1264397). The abstract (via OpenAlex) states that "the new global optimization algorithm can potentially lead to orders of magnitude reduction in optimality gap when compared to commercial solvers BARON and GloMIQO."
- **Grey-box models, from her doctoral adviser's group.** Boukouvala, Hasan and Floudas, *J. Global Optim.* 67(1–2):3–42, 2017 (online 5 Nov 2015; DOI 10.1007/s10898-015-0376-2), via S2 context: "However, as the problem size increases the required time for reaching global optimality using the recent global optimization solver ANTIGONE [67] increases significantly."
- **Ellipse cutting, a field-wide limit.** Birgin, Lobato and Martínez, *J. Global Optim.* 65(4):709–743, 2016 (DOI 10.1007/s10898-015-0395-z), via S2 context, summarising Kallrath and Rebennack (*J. Global Optim.* 59(2–3):405–437, 2014; DOI 10.1007/s10898-013-0125-3): "the state-of-the-art global optimization solvers BARON [48], LindoGlobal [39], and GloMIQO [43] available within the GAMS platform, were unable to find global solutions for instances with more than 4 ellipses (when restricted to a maximum of 5 hours of CPU time)." This limit is not specific to her solver.
- **Answered?** [practice] Her own papers report the same lesson:
  - APOGEE beat her generic solver on pooling (03 PE-30).
  - The GALINI pooling paper attributes its win to a pooling-specific heuristic (03 PE-32).

  [inferred] The critics and she agree here. Her response was to build structure-specific plug-ins (GALINI) rather than to defend the general solver.
- **Layers**: 2, 4.

### PC-08 · Edge-concave cuts help on random quadratic instances, not on general MINLP (SCIP's re-implementation)

- **The finding** [observed] (S; primary evidence of SCIP's own practice). Bestuzheva, Chmiela, Müller, Serrano, Vigerske and Wegscheider, "Global optimization of mixed-integer nonlinear programs with SCIP 8", *J. Global Optim.* 91(2):287–310, DOI 10.1007/s10898-023-01345-1, p. 296:
  - "This has shown to be particularly useful for randomly generated quadratic instances [45, 46]." [45] is Misener and Floudas, *Math. Program.* 2012. [46] is Misener, Smadbeck and Floudas on GloMIQO 2, *Optim. Methods Softw.* (DOI 10.1080/10556788.2014.916287).
  - "Since the current implementation of edge-concave cuts in SCIP has not shown to be particularly useful for general MINLP, it is disabled for now."
- **ANTIGONE left out of SCIP 8's comparison.** p. 301: GAMS 41.2.0 "includes SCIP 8.0.2, BARON 22.9.30, Lindo API 14.0.5099.162, and Octeract 4.5.1". GAMS still distributed ANTIGONE at the time (01 §1.8; the GAMS 43 and 50 release notes still name it), but it is not in the comparison, and the paper gives no reason.
- **What it shows**: another team transplanted one of her signature relaxations into a different solver, and the gain did not carry beyond the instance class on which it had been shown.
- **Answered?** None found. [inferred] Her habit of class-scoped claims (03 PE-31) already contained the warning; the SCIP team confirmed it independently.
- **Layers**: 5 (which instance classes back a component); 4.

### PC-09 · OMLT: gaps in scope and a large memory footprint (an independent tool comparison and user reports)

- **Independent benchmark** [observed] (S). Atallah, Dankwart, Neider and Yalçıner, "eNNcode: Optimization-Based Analysis of Neural Networks", IJCAI-26 Demonstrations Track, pp. 8358–8362, DOI 10.24963/ijcai.2026/956. Read.
  - p. 8358: "Moreover, unlike OMLT [Ceccon et al., 2022], eNNcode remains lightweight, easy to install, and designed for maximum usability."
  - p. 8359: "Although this promotes solver independence, significant additional effort emerges during model instantiation."
  - p. 8360: "Within the specified time limit, all variants find counterfactual explanations except for OMLT on the MNIST CNN, where approximately 40% of the runs reach time out (excluded from the reported results). Regarding memory consumption, OMLT consistently exhibits by far the highest storage requirements in all test cases, likely due to its more complex internal workflow."
  - The same page also credits OMLT: "To the best of our knowledge, OMLT and Gurobi-ML represent the only publicly available libraries capable of translating neural networks into MILO instances without imposing strong restrictions."
  - Caveat: a demonstration paper by the authors of a competing library, with a small benchmark (counterfactual explanations for a few classifiers).
- **Scope statements by users and co-developers** [observed]/[practice] (public GitHub issues, read 2026-10-10):
  - Issue #107, opened 2023-05-18, multiclass LightGBM. Calvin Tsay replied on 2023-06-12: "OMLT unfortunately does not currently support multi-output GBT models".
  - Issue #183, opened 2026-02-03 and still open, asks whether OMLT can take scikit-learn `MLPRegressor` models.
  - Ovalle, Biegler, Grossmann, Laird and Dulce Rubio, arXiv:2506.03531v1 (NeurIPS 2025 according to S2), p. 10: "We evaluate classification performance using ReLU NNs [9], the only model type readily supported by OMLT for classification tasks [59]." Laird is an OMLT co-author.
- **Answered?** The GitHub issues were answered (R5). No reply to eNNcode was found.
- **Layers**: 7 (software as research output; capacity to maintain it); 4.

### PC-10 · Exact MILP encodings of trained networks do not scale (a rival school using heuristics and gradient methods)

- **Critic** [observed] (S). Tong, Cai and Serra, "Optimization Over Trained Neural Networks: Taking a Relaxing Walk", arXiv:2401.03451v2 (CPAIOR 2024 according to S2). Abstract: "solving these formulations soon becomes difficult as the network size grows due to the weak linear relaxation and dense constraint matrix. We have seen improvements in recent years with cutting plane algorithms, reformulations, and an heuristic based on Mixed-Integer Linear Programming (MILP). In this work, we propose a more scalable heuristic".
  - The S2 context lists Tsay et al. 2021 (her partition-based formulation) among the improving reformulations; it is not the target.
- **A related paper, not read.** Tong, Zhu, Serra and Burer, "Optimization over Trained Neural Networks: Going Large with Gradient-Based Algorithms", LNCS (CPAIOR), pp. 596–613, 2026, DOI 10.1007/978-3-032-27242-3_35 (metadata only). Burer is a member of this team.
- **Her own words** [stated] (P, ASR, Cornell seminar, 17 Feb 2023): "all of this is clearly introducing huge numbers of binary variables right which is sometimes going to be okay and sometimes it's going to be a stupid idea". More concessions are collected in R4.
- **Answered?** Only in the sense that she presents MILP encodings as one option among several and points to complementarity-based nonlinear reformulations. In the same talk she mentions working with Carl Laird on such formulations in OMLT; that passage of the ASR is garbled, and OMLT's feature set was not checked.
- **Layers**: 2, 4.

## 3. Judgements shown wrong, left unproven or contested

### PC-11 · Piecewise-linear relaxations of the pooling problem: good in practice, no better than a factor of n in the worst case

- **The theorem** [observed] (S). Dey and Gupte, "Analysis of MILP Techniques for the Pooling Problem", *Oper. Res.* 63(2):412–427, 2015, DOI 10.1287/opre.2015.1357. Abstract read via Crossref; the Optimization Online preprint 2013/04/3849 read in part. The abstract:
  - "Although there is a significant amount of empirical evidence to show that such piecewise-linear relaxations, which can be written as mixed-integer linear programs (MILPs), yield good bounds for the pooling problem, to the best of our knowledge, no formal result regarding the quality of these relaxations is known."
  - "In this paper, we prove that the ratio of the upper bound obtained by solving piecewise-linear relaxations (objective function is maximization) to the optimal objective function value of the pooling problem is at most n, where n is the number of output nodes. Furthermore for any ϵ > 0 and for any piecewise-linear relaxation, there exists an instance where the ratio of the relaxation value to the optimal value is at least n − ϵ."
- **The consequence that bites** [observed] (S). Gupte, Ahmed, Dey and Cheon, "Relaxations and discretizations for the pooling problem", *J. Global Optim.* 67(3):631–669, 2017 (online 27 Apr 2016), DOI 10.1007/s10898-016-0434-4. Optimization Online preprint 2015/04/4883, p. 16: "Notice that this performance guarantee is independent of the number of and the distance between partitions in each variable domain. They also proved that this approximation factor is tight, i.e. there are problem instances where this ratio gets arbitrarily close to |J| for all piecewise linear relaxations."
  - The same page places her work in context: Gounaris, Misener and Floudas (2009; *Ind. Eng. Chem. Res.*, DOI 10.1021/ie8016048), and "Recently, Misener et al. (2011) implemented a branch-and-bound based solver for pooling problems that uses piecewise linear MILP relaxations".
- **What it shows**: in the worst case, adding partitions gains nothing. The benefit her PhD papers measured is instance-dependent. This does not refute her measurements; it limits what they can promise.
- **Answered?** Yes, by absorbing it [stated + practice] (P):
  - 2016 essay (*SIAG/OPT Views and News* 24(1):12–16, Oct 2016, p. 13): "Subsequent results further unpacked this relationship between the NLP pooling problem and MIP approximations [126], but still Chris would push me: Why did these piecewise approximations work so well? How could we eliminate the computational dependence on parameters?" ([126] is Dey and Gupte.)
  - Baltean-Lugojan and Misener, *J. Global Optim.* 71(4):655–690, 2018 (DOI 10.1007/s10898-017-0577-y), via S2 contexts of their own paper: "Subsequent work used the standard pooling problem topology to develop a state-of-the-art MILP discretization heuristic with a performance bound [21, 27, 28]." Also: "This encourages future research in building disjunctive cuts based on the structures identified to partition feasible space in the non-sparse NP-hard subclasses, an approach taken by the state-of-the-art heuristic developed in [21]."
  - Her answer to "why do they work" is a parametric and complexity characterisation (sparse, strongly polynomial cases vs NP-hard ones). It complements the worst-case bound rather than contesting it.
  - [inferred] Nowhere in the sources read does she present the n-bound as a limitation of her approach.
- **Note**: Dey is a member of this MINLP team.
- **Layers**: 1 (taste: empirical evidence vs worst-case guarantees); 5.

### PC-12 · An independent group saw no advantage for APOGEE

- **The finding** [observed] (S). Dey and Gupte, Optimization Online preprint 2013/04/3849 (submitted version of the *Oper. Res.* paper), p. 21: "We experimented with the specialized global solver APOGEE (Misener et al. 2011) for pooling problems but did not observe any performance benefit compared to BARON." No numbers are given. Whether the sentence survives in the published version was not checked.
- **Context**: APOGEE was distributed free from a Princeton site that no longer answers (01 §1.8). Her 2012 *Math. Program.* paper reported APOGEE beating her own generic MIQCQP solver (03 PE-30), which is a different comparison.
- **Answered?** No reply found.
- **Layer**: 4 (replication; comparing against the strongest general solver rather than one's own generic code).

### PC-13 · Uniform partitioning, and linear vs logarithmic encodings

- **Critic: Nagarajan et al.** [observed] (S). Nagarajan, Lu, Wang, Bent and Sundar, "An adaptive, multivariate partitioning algorithm for global optimization of nonconvex programs", *J. Global Optim.* 74(4):639–675, 2019, DOI 10.1007/s10898-018-00734-1. Read as arXiv:1707.02514v4 (1 Feb 2019).
  - p. 3: "Unfortunately, uniform partitioning, when used in conjunction with a MIP-based approach can lead to MIPs with a large number of binary variables. Thus, uniform partitioning limits MIP based approaches to small- and medium-sized problems. This important issue has motivated the development of piecewise relaxation techniques where the number of binary variables increases logarithmically [36, 52] with the number of partitions". Here [36] is APOGEE.
  - Same page: "none of these approaches address the key limitation of uniform partitioning, partition density, i.e. these methods introduce partitions in unproductive areas of the variable domains."
  - Their concession, p. 33: "an adaptive partitioning of the domains of variables outperforms uniform partitioning, though the latter exhibits better optimality gaps in the first few iterations of the lower-bounding algorithm."
  - Their benchmarks draw on her test libraries: the meyer instances cite Misener and Floudas's generalized pooling problem library on minlp.org, and the wtsM2 instances cite the GloMIQO paper.
- **Support for her 2011 judgement**, from the same paper, p. 38: "Despite fewer variables in the logarithmic formulation, this encoding is only effective on a few problems, generally on problems that require a significant number of partitions. These results suggest that when the logarithmic encoding has nearly the same number of partition variables as the linear encoding, the linear encoding is more effective." This matches APOGEE's decision to keep linear partitioning (01 §1.9 item 1).
- **The other side: the Castro school** [observed] (S).
  - Castro, "Normalized multiparametric disaggregation: an efficient relaxation for mixed-integer bilinear problems", *J. Global Optim.* 64(4):765–784, 2016 (online 30 Jul 2015), DOI 10.1007/s10898-015-0342-z. Via S2 context: "However, even though it increases the chances that the bilinear problem will solve to global optimality within a given time limit, the piecewise relaxation option in GloMIQO is turned off by default [20] since convergence is generally faster that way." Her own default is used as evidence of what MIP relaxations with linearly many binaries cost, and so as motivation for alternatives whose binaries grow logarithmically.
  - Castillo Castillo, Castro and Mahalec, *J. Global Optim.* 71(4):691–716, 2018, DOI 10.1007/s10898-018-0612-7. Via S2 context: "The extensive use of OBBT contrasts with commercial global optimization solvers [37–39], which apply some restricted version of it, always featuring the simplest bilinear envelopes [40]." Here [39] is ANTIGONE 1.1.
  - Castro, "Global Optimization of QCPs Using MIP Relaxations with a Base-2 Logarithmic Partitioning Scheme", *Ind. Eng. Chem. Res.* 62(28):11053–11066, 2023, DOI 10.1021/acs.iecr.3c00191. The abstract (via OpenAlex) says MIP relaxations "take considerably more time to solve than their linear programming counterparts", so "state-of-the art commercial solvers have found limited use for them". It uses "a logarithmic partitioning scheme to ensure tractability and base-2 to minimize the jump in complexity". It reports outperforming "GUROBI 9.5.2 and BARON 22.7.23"; ANTIGONE is not in that comparison.
  - Castro, Liao and Liang, "Comparison of mixed-integer relaxations with linear and logarithmic partitioning schemes for quadratically constrained problems", *Optim. Eng.* 23(2):717–747, 2022 (online 6 Mar 2021), DOI 10.1007/s11081-021-09603-5. This is the direct test of the APOGEE question. **Not read**: no abstract could be retrieved (see Gaps).
- **Answered?** Not by her in anything found. The question is contested and is kept under Contradictions.
- **Layers**: 4, 5.

### PC-14 · The tree-ensemble formulation OMLT ships is not the tightest available

- **What OMLT ships** [stated] (P). The OMLT paper (Ceccon, Jalving, Haddad, Thebelt, Tsay, Laird, Misener; arXiv:2202.02414v2; *JMLR* 23(349):1–8, 2022), p. 3: "The OMLT 1.0 GBTBigMFormulation uses the Mišić (2020) and Mistry et al. (2021) formulation and thereby simplifies our GBT-based black-box optimization tool ENTMOOT (Thebelt et al., 2021, 2022a)."
- **Critic** [observed] (S). Kim, Richard and Tawarmalani, "A Reciprocity Between Tree Ensemble Optimization and Multilinear Optimization", *Oper. Res.* 73(5):2610–2626, 2025, DOI 10.1287/opre.2022.0150.
  - The abstract (Crossref) says the reduction "permits the derivation of new stronger formulations for tree ensemble optimization problems, including ideal formulations for single trees."
  - Via S2 contexts: "We will develop formulations tighter than those in the TEO literature." Their (TEOM) formulation "extends formulation (2) for a tree ensemble proposed in Mǐsić (2020) in a manner similar to Mistry et al. (2021)", and their Table 1 is a "Comparison of tightness of (a) formulation (12) and (b) formulation (2) in Mǐsić (2020) for TEO."
  - The full text was not read.
- **The link** [inferred]: the critique targets the Mišić-type formulation, which OMLT's GBT big-M formulation implements by OMLT's own statement. Whether OMLT has since adopted the tighter formulations was not checked.
- **Answered?** No reply found.
- **Layers**: 3 (choice of formulation); 7 (what a toolkit ships).

### PC-15 · SnAKe (Bayesian optimisation with movement costs): no guarantees and weak convergence

- **Her paper**: Folch, Zhang, Lee, Shafei, Walz, Tsay, van der Wilk and Misener, "SnAKe: Bayesian Optimization with Pathwise Exploration", arXiv:2202.00060v4 (NeurIPS 2022 camera-ready, per the arXiv comment).
- **Critics** [observed] (S):
  - **Ramesh, Sessa, Krause and Bogunovic**, "Movement Penalized Bayesian Optimization with Application to Wind Energy Systems", arXiv:2210.08087v1 (NeurIPS 2022, per the arXiv comment), p. 2: "two recent works [24, 15] consider the problem of switching cost minimization in Bayesian optimization. They both consider the non-contextual setting, and while [24] lacks theoretical guarantees, [15] does not explicitly consider the cost in the regret definition." Here [24] is SnAKe.
  - **Yang, Aitchison and Moss**, "MONGOOSE: Path-wise Smooth Bayesian Optimisation via Meta-learning", arXiv:2302.11533v2.
    - p. 2: "However, as demonstrated empirically by (Folch et al., 2022), SnAKe has several shortcomings including the requirement of an additional heuristic to ensure that it avoids getting stuck in local modes and a drop in performance when considering higher dimensions and/or shorter time horizons."
    - p. 4: "the current state-of-the-art SnAKe (Folch et al., 2022) lacks this flexibility". The flexibility meant is weighting the cost of movement.
    - These shortcomings come from SnAKe's own reported results.
  - **Chen and Al Kontar**, "The Traveling Bandit: A Framework for Bayesian Optimization with Movement Costs", *Technometrics* 68(2):239–250, DOI 10.1080/00401706.2025.2573228; read as arXiv:2410.14533v1.
    - pp. 2–3: "Despite a few attempts to integrate movement costs into BO (Samaniego et al., 2021; Folch et al., 2022; Shi et al., 2023; Liu et al., 2023), these methods fail to be global optimization approaches due to their myopic and greedy nature."
    - p. 4: "SnAKe does not finish the path they planned but switches to a new path when new observations are available. Consequently, SnAKe converges neither theoretically nor empirically."
    - p. 16: "we observe very limited evidence of SnAKe's convergence. Although it does not get stuck like GS, it has difficulties converging on regret and movement costs as the optimization proceeds." They suspect a side effect of SnAKe's heuristic point deletion.
- **Her own remark** [stated] (P, ASR, Manchester, January 2025): see R4.
- **Answered?** [practice] (P), through a follow-up written with the critic's group. Folch, Tsay, Lee, Shafei, Ormaniec, Krause, van der Wilk, Misener and Mutný, "Transition Constrained Bayesian Optimization via Markov Decision Processes", arXiv:2402.08406v3 (accepted to NeurIPS 2024, per the arXiv comment). Krause also co-authored the "lacks theoretical guarantees" critique.
  - p. 5: "Previous work has focused on planning experimental sequences for minimizing switching costs [11, 21, 40, 41] however they are only able adhere [sic] to strict constraints under truncation heuristics [20, 22, 42]."
  - p. 10: "It is important to highlight that SnAKe and LSR are specialist heuristic algorithms for local box-constraints, and therefore it is not surprising they perform strongly. Our method can be applied to more general settings and therefore it is very encouraging that MDP-BO is able to match these SOTA algorithms in their specialist domain."
  - The group now calls SnAKe a "specialist heuristic" and has moved to a planning formulation. Chen and Al Kontar's critique (posted October 2024) came after this follow-up.
- **Layers**: 1 (taste: guarantees vs a practical heuristic); 4; 7 (collaborating with critics).

### PC-16 · How to choose the number of partitions (partition-based ReLU formulations, P-split) is still heuristic

- **A NeurIPS 2021 reviewer** [observed]: "I do wish the authors left us with a clearer story on how N should be selected" (Reviewer 1SxU). Read by agent 03 from the Wayback capture of the OpenReview API (03 §5.5); not re-read here.
- **Her answers to questions at talks** [stated] (P, ASR): see R4.
- **The journal outcome** [practice] (P). P-split, *Math. Program.* 2025 (DOI 10.1007/s10107-025-02232-1; abstract of arXiv:2202.05198v3): "under certain assumptions, the formulations form a hierarchy starting from a big-M equivalent and converging to the convex hull." The abstract gives no rule for choosing P. [inferred] In the public record the selection question is still open.
- **Layers**: 4, 5.

## 4. Independent benchmark record of her solvers (time series)

**Mittelmann's MINLPLib benchmark** [observed] (S). Dates are those printed on the pages. All captures were retrieved on 2026-10-10; the capture timestamp is the one the Wayback Machine actually served. Each cell gives the number solved and, in brackets, the geometric mean as printed (shifted or scaled per page).

| Page date (capture) | Set-up | ANTIGONE | Others | ANTIGONE's rank by solved |
|---|---|---|---|---|
| 28 Apr 2017 (20170717125813) | MINLPLib2, 72 instances, GAMS 24.8.4, 1 thread, 2 h, i7-4790K | 46 (3.14) | BARON 17.4.1: 52 (1); SCIP 4.0: 37 (3.14); COUENNE 0.5: 24 (9.23); LINDO 10.0: 19 (5.83) | 2nd of 5 |
| 15 Aug 2021 (20211220190643) | MINLPLib, 87 instances, GAMS 36.1.0, 1 thread | 53 (4.17) | BARON: 63 (1); SCIP: 55 (2.06); LINDO: 29 (5.93) | 3rd of 4 |
| 24 Jan 2023 (20230127153423) | 87 instances, 1 thread | 53 (5.26) | OCTERACT: 86 (1); BARON: 73 (2.11); SCIP: 64 (2.42); LINDO: 37 (80.8); COUENNE: 24 (460) | 4th of 6 |
| 7 Feb 2024 (20240409181240) | 87 instances, 8 threads | 53 (scaled 39.3) | OCTERACT: 87 (1.0); BARON: 77 (2.4); SCIP: 65 (9.9); SHOT: 54 (6.2); LINDO: 42 (32.8); COUENNE: 24 (89.8) | 5th of 7 |
| 6 Sep 2024 (20240921192253) | 87 instances, 12 threads, 3 h | 52 (26.6) | BARON: 75 (1.0); SCIP: 65 (5.8); SHOT: 53 (1.5; page note: "SHOT can only solve 66/87 instances"); LINDO: 28 (28.1) | 4th of 5 |
| 28 Feb 2025 (20250305061825) | New test set of 200 MINLPLib instances | not included | BARON, Gurobi, SCIP, SHOT, XPRESS | — |
| 18 Aug 2025 (20250819054738) and 26 Feb 2026 (live page) | 200 instances | not included | BARON, Gurobi, LINDO, SCIP, SHOT, XPRESS | — |

- **Reading** [observed + inferred]:
  - ANTIGONE's solved count stayed flat (46, then 53, then 52) while BARON's went from 52 to 77 and SCIP's from 37 to 65.
  - ANTIGONE was dropped when the test set changed in 2025. The pages give no reason.
  - [inferred] The decline tracks a frozen code (§6) more than any weakness of the method.

**Other third-party comparisons that include her solvers** [observed] (S):

| Study | Her solver | Finding, as stated | How read |
|---|---|---|---|
| Buchheim and D'Ambrosio, *J. Global Optim.* 67(4):759–786, 2017, DOI 10.1007/s10898-016-0443-3 | ANTIGONE | "SCIP shows the weakest performance, while ANTIGONE outperforms all other approaches on large instances, however showing a much more volatile behaviour in comparison to integer instances." | Via S2 context. The 2013 preprint (Optimization Online 2013/11/4127) has no ANTIGONE comparison, so it was added in revision |
| Dressler and Murray, *SIAM J. Appl. Algebra Geom.* 6(4):650–684, 2022, DOI 10.1137/21m1462568 (arXiv:2107.00345v1) | ANTIGONE (GAMS 33.2.0) on a signomial reactor-design benchmark, 7200 s, 8 threads | p. 14: "Our methods outperform SCIP, BARON, and ANTIGONE on this problem." p. 19: "SAGE produced the same solution as these solvers, but with an REP that could be solved in half the time as the fastest of these methods. Only LINDO was able to certify its solution as globally optimal." | Read in part. Relevant because ANTIGONE carries her signomial framework (Misener and Floudas, *J. Optim. Theory Appl.* 161(3):905–932, 2014, DOI 10.1007/s10957-013-0396-3) |
| Zhang and Sahinidis, *Comput. Optim. Appl.* 92(3):1123–1161, 2024, DOI 10.1007/s10589-024-00633-0 | ANTIGONE 1.1 | Via S2 context: "The global solvers compared were ANTIGONE 1.1 [63], BARON 23.9 [91], LINDOGLOBAL 14.0 [54], OCTERACT 4.7.1 [45], and SCIP 8.0 [11]." The results were **not read** | S2 context only |
| Kronqvist et al. 2019 (PC-02); Uribe-Rodriguez et al. 2020, Kolodziej et al. 2013, Castro 2017 (PC-07); Du et al. 2025 (PC-01); Mittelmann's QPLIB pages (PC-06) | — | See those entries | — |

## 5. How critique was answered: response patterns

- **R1 · Absorb and reposition** [stated + practice]. Dey and Gupte's worst-case result became "further unpacked this relationship" (2016 essay) and "a state-of-the-art MILP discretization heuristic with a performance bound" (2018 paper). See PC-11.
- **R2 · Work with the critic** [practice; the reading is inferred]:
  - Krause co-authored the "lacks theoretical guarantees" critique of SnAKe (2022) and then the NeurIPS 2024 follow-up with her group (PC-15).
  - Kronqvist co-authored the 2019 hypothesis about ANTIGONE's missed convexity and then joined her group as a fellow (PC-02).
- **R3 · Name your own limits in the next paper** [stated] (P):
  - **Molecular design.** Zhang, Campos, Feldmann, Sandfort, Mathea and Misener, "Augmenting optimization-based molecular design with graph neural networks", arXiv:2312.03613v1, pp. 16–17: "Moreover, there are two main limitations in Zhang et al. (2023): • Problem size: we only solved the optimization problems with up to N = 8 atoms, which are too small for most molecular design applications. • Aromacity [sic]: we only considered double and triple bonds. Aromatic rings are incompatible with (C1) - (C27)." The fix follows: "To circumvent these limitations, instead of assembling atoms to form a molecule, we use the concept of molecular fragmentation". "Zhang et al. (2023)" is the NeurIPS 2023 paper "Optimizing over trained GNNs via symmetry breaking", arXiv:2305.09420.
  - **Tree kernels.** BARK (Boyne, Folch, Lee, Shafei and Misener; arXiv:2503.05574v2, 6 Jun 2025; ICML 2025 according to S2, not checked), p. 1: "Tree kernels for model fitting and BO have previously been explored (Balog et al., 2016; Thebelt et al., 2022a), but they have always used a two-step fitting process: first, a tree model is fitted on the data, and then the GP is trained using the tree kernel defined by the tree model. While this heuristic gives good results in a variety of benchmarks, it is not principled and hence potentially sub-optimal."
    - Thebelt et al. 2022a is her group's NeurIPS 2022 paper (arXiv:2207.00879). Its own abstract had already named "Two well-known challenges in using tree ensembles for black-box optimization are (i) effectively quantifying model uncertainty for exploration and (ii) optimizing over the piece-wise constant acquisition function."
    - BARK also reports a failure of the new method, p. 7: "DiscreteRosenbrock shows a failure case of BARK".
  - **SnAKe.** The NeurIPS 2024 MDP-BO paper (PC-15).
- **R4 · Concede in public, before being asked or when asked** [stated] (P, ASR):
  - **Seminar series "machine learning needs mathematical optimization"**, April 2021. File `../sources/talks/2021-04-sevilla-partition-based-formulations-relu-UcNXm24uQjE.txt`. The questioners are not named in the ASR; she addresses one of them as the author of a "lossless compression paper".
    - "i don't claim that we have the very best partitioning strategies"
    - "if i choose a bad partitioning strategy i'm just gonna do automatically worse than than big m"
    - "we just feel like we're in the dark on this"
    - "i know that it's better than big m i don't know that it's better than you know some other partitioning strategy"
    - On alternatives that failed: "we thought well maybe some of the the inputs things that are close in euclidean distance are going to somehow they should be aggregated no that didn't work"
  - **Cornell seminar**, 17 Feb 2023. File `../sources/talks/2023-02-17-cornell-between-formulations-love-parameters-bC4PDG9EZA8.txt`.
    - "I'm kind of giving you right away the criticism that you might all have which would be very reasonable which students to say good God Ruth you use a lot of parameters um and so that's I've already given you uh one of the the weaknesses of this"
    - "if you just told me to pull out of my hat prove to you what is the best value of N I would have to say no I'm sorry so it's going to be it's going to be heuristic"
    - "there are definitely places you're going to be worse than Big M"
    - "we only have heuristics". Attributed to her from the turn-taking; the ASR has no speaker labels.
  - **Manchester seminar**, January 2025, on SnAKe. File `../sources/talks/2025-01-manchester-autonomous-research-machines-2br7KspcQXk.txt`.
    - "I introduced a parameter I don't like to introduce parameters"
    - "first off I I made up a new metric and I win on the new metric which is you know classic uh um academic right so regret versus cost cost is my metric so if I didn't win on it better you better think I'm an idiot"
    - On the standard metric: "they kind of all look the same to me".
- **R5 · Software bug reports: fast triage on OMLT, slow on ENTMOOT** [practice] (P for the team's replies; S for users' reports). Public GitHub issue threads, read in the raw page data on 2026-10-10:

  | Issue | Report | Response |
  |---|---|---|
  | OMLT #80, opened 2022-06-19 by user viggotw | "The deviation seems to be a static offset, not random." and "I've also been looking for a list of supported models without luck" | Thebelt diagnosed it on 2022-06-20 (the base score of the boosted trees). Misener closed it on 2022-07-06: "@ThebTron fixed the issue. The problem is that each of the different libraries (lightgbm, scikit-learn, etc.) manage the constant value slightly differently. ... We may see issues like this in the future for other tree libraries, it seems that each of them pass the constant value to ONNX slightly differently." |
  | OMLT #98, opened 2022-11-07, same user: wrong value of the decision variable | — | Thebelt, 2022-11-20: "There are a few problems with the notebook and I can see how the OMLT interface is a bit confusing here. I'll address the issues with the team and we'll work on making it more intuitive." Tsay closed it on 2023-05-04 |
  | OMLT #107, opened 2023-05-18: multiclass LightGBM | — | Tsay, 2023-06-12, quoted in PC-09 |
  | OMLT #173, opened 2025-04-17: a bug in the linear-tree formulation (a `TypeError` when unscaled bounds are missing) | — | Acknowledged the same day by project member `bammari` ("You are correct and I will patch this issue immediately"), who linked the patch, PR 175, later that day |
  | ENTMOOT #29, opened 2023-11-28: "ENTMOOT does not work with newest lightgbm version" | — | First diagnosis on 2024-06-21 by Toby Boyne (an undocumented LightGBM change), about seven months later |
  | ENTMOOT #38, opened 2024-06-26 by Boyne himself (internal critique) | "it is unclear to me that this is correct in the exploration setting. Indeed, when using the `gurobi_direct` interface for Pyomo, this test sometimes fails." and "we should consider using random seeds in the testing to ensure that tests are reproducible." | Closed (date not extracted) |

  [inferred] Response speed tracks who is in the group:
  - OMLT, a multi-institution project with fellows, answers within days.
  - ENTMOOT waited until a new student took it on. This is the pattern 04 F6 reports for which tools survive.
- **R6 · No answer found**: PC-01, PC-03, PC-04, PC-08, PC-09 (eNNcode), PC-12, PC-13, PC-14 and Mittelmann's removal of ANTIGONE. [inferred]
  - For critiques of the frozen solver (era E-B), the silence fits a closed product that is no longer developed.
  - For era E-C critiques, it may partly be a matter of time: several date from 2024–2026.
- **R7 · Her stated stance towards reviewers (grant panels)** [stated] (P, ASR, inaugural lecture, 13 Mar 2023, [35:15]), describing her husband's help: "And his ace in the hole is grant rebuttals. He got me out of, um, uh, 346 going into, uh, a a um, a fellowship proposal and, uh, I got the grant. ... the the the key is disappointment. You're disappointed that the the reviewer didn't understand."
  - "346" is as captioned. It probably refers to reviewer scores; not checked.
  - For a documented exchange over a paper review (concede the precise error, defend novelty by restating it), see 03 PE-36 (NeurIPS 2021).

## 6. Failures, frozen lines and plans that did not materialise (new evidence only)

- **The GAMS release notes as a bug ledger** [practice] (S; GAMS documentation, RN pages, read 2026-10-10). Five releases record fixes:
  - GAMS 23.8.2 (5 Apr 2012): "GloMIQO resets OptCR=0 properly to 1e-9 and accepts now Ctrl-C on Windows".
  - 23.9.4 (20 Oct 2012): GloMIQO, "A problem with parsing integer options has been fixed".
  - 24.0.2 (14 Feb 2013): GloMIQO, "fixed bug in reporting of dual bound when optca tolerance is larger in magnitude than optcr".
  - 24.1.1 (30 May 2013): GloMIQO 2.2, "Fixed bug in detecting when aBB cuts should be generated."
  - 24.2.1 (9 Dec 2013): "ANTIGONE Fixed bug where optimality gaps were reported for convex problems."
- **The last ANTIGONE improvements, then the end of development.** GAMS 24.1.3 (26 Jul 2013), with ANTIGONE 1.1 and GloMIQO 2.3, lists:
  - "eliminate constraint on the number of variables (ANTIGONE/GloMIQO was previously limited to 45,000 variables)";
  - "track numerically sensitive variables for possible instability associated with optimality-based bounds tightening".

  GAMS 24.6.1 (18 Jan 2016) reads "ANTIGONE New libraries." This is the last new-library entry for ANTIGONE in release notes 24.x to 54. Later entries concern builds and platforms:
  - 25.0.1 (17 Jan 2018): "Due to the discontinuation of Cplex on Windows 32bit (with Cplex 12.7 in 2016) we are faced with potentially phasing out/dropping solvers depending on Cplex on Windows 32bit with the next major release. The most likely candidate for this is ANTIGONE." ANTIGONE needs a CPLEX licence to run (01 §1.8), so a dependency it does not control limits where it can run.
  - 25.0.2 (31 Jan 2018): "On Linux, removed the MKL libraries that were optimized to certain x86 instruction sets (AVX, etc.) as this resulted in errors when running ANTIGONE or SCIP".
- **GloMIQO dropped.** GAMS 39: "We plan to drop GLOMIQO with the next major release." GAMS 40.1.0 (1 Aug 2022): "As announced, dropped GLOMIQO. The use of ANTIGONE is equivalent." Also recorded in 01 and 06.
- **A plan that did not materialise** [stated → practice]. The 2014 paper says ANTIGONE was "architected" for "further advances in the area of term-specific underestimators" (quoted in 03 PE-29, not re-read here). No later ANTIGONE release adds them.
  - [inferred] The extension point moved to the open-source GALINI, whose general paper stayed a preprint (03 C1; 01 §1.9).
- **Signs of abandonment from outside the group** [observed]:
  - SCIP disabled its edge-concave cut separator (PC-08).
  - SCIP 8 left ANTIGONE out of its comparison (PC-08).
  - Mittelmann dropped ANTIGONE from his MINLP benchmark (§4).
- **Cross-references, not repeated here**:
  - The preprint on NN-scored SDP cuts: the 2019 thesis lists it as "Reviewed and resubmitted, Nov 2019", and no published version exists (04 F1; 03).
  - The withdrawn symmetry theorems (03 PE-34).
- **Context only, not addressed to her.** Dey, Jiang, Kazachkov, Lodi and Muñoz (arXiv:2604.00932v1, 1 Apr 2026), via S2 context, on eigenvector-based cuts for QCQPs: "the main drawback has been repeatedly acknowledged: if (v0, v) are eigenvectors of [...] then the resulting cut will typically be dense, which can cause numerical instability". [inferred] This is the drawback the 2018 cut-selection preprint was built around.

## 7. What the critiques say about her research craft (mapped to the layers) [inferred unless tagged]

| Layer (§一) | What critics value or found | What her record shows | Use in the skill |
|---|---|---|---|
| 1 Taste | Worst-case guarantees (Dey and Gupte). Tight formulations that keep structure (He and Tawarmalani; Kim, Richard and Tawarmalani). Convergence theory (Ramesh et al.; Chen and Al Kontar) | Empirical, library-based evidence first. Theory follows a specific question: the answer to "why do piecewise approximations work" came eight years later, as a complexity characterisation, not a guarantee | When speaking in her voice, name the guarantee a method lacks before citing the benchmark that favours it |
| 2 Problem choice | General solvers lose to structure-specific methods on large industrial instances (PC-07). Some function classes are out of scope (PC-05) | She scopes claims to problem classes and builds structure-specific plug-ins | Ask "which class, which structure?" before "which solver?" |
| 4 Experiment | A frozen code compared with moving targets (§4). A trust-region benchmark on synthetic data only (PC-04). Winning on one's own metric (R4) | Her papers stress that competitors are moving targets and harmonise tolerances (03 PE-07, PE-08) | Date every comparison and say which side is frozen |
| 5 Judging results | Guessed bounds can make "infeasible" untrustworthy (PC-01). Components that win on random instances may not generalise (PC-08) | Techniques are off by default when the evidence is class-specific (03 PE-33) | Treat solver status codes as claims to be checked |
| 7 Organisation | Capacity to maintain decides which tools stay credible: ENTMOOT's lag, ANTIGONE frozen | Multi-institution projects answer quickly; single-student tools stall (04 F6) | Plan maintenance together with the method |

## Contradictions (kept, not reconciled)

1. **Linear vs logarithmic partitioning.**
   - APOGEE (2011) kept linear partitioning.
   - Nagarajan et al. (2019) found linear encoding more effective unless many partitions are needed.
   - Castro's line takes the other side. In 2016, normalised multiparametric disaggregation, whose binaries grow logarithmically with the number of partitions, was motivated by the cost of linear schemes. In 2023, base-2 logarithmic partitioning was reported to beat Gurobi 9.5.2 and BARON 22.7.23.
   - The direct comparison by Castro, Liao and Liang (2022) was not read (PC-13).
2. **ANTIGONE's standing depends on the instance class.**
   - On continuous nonconvex QPLIB in 2026 it solves the most instances (35 of 102, against BARON's 31).
   - On binary nonconvex QPLIB it is second to last (16 of 128).
   - Buchheim and D'Ambrosio report that it "outperforms all other approaches on large instances" but is "much more volatile".
   - Du et al. report that it fails on two refinery cases yet beats BARON on a reformulated one.
3. **Shi et al.'s framing of Mistry et al. 2021.** They count it among frameworks that "ignore the trust region" (p. 2), then describe its PCA penalty as a trust-region method (p. 4) and benchmark it as one.
4. **Her framing of Dey and Gupte vs her critics' framing.** She wrote that it "further unpacked this relationship" (2016 essay). Gupte et al. stress that "this performance guarantee is independent of the number of and the distance between partitions".
5. **APOGEE's value.** Dey and Gupte saw "no performance benefit" from APOGEE over BARON. Her 2012 paper reports APOGEE beating her own generic solver (03 PE-30). The baselines differ.
6. **SnAKe.** Her group's 2024 paper calls it a specialist heuristic that performs "strongly" on box-constrained benchmarks. Chen and Al Kontar report "very limited evidence of SnAKe's convergence". The metrics and benchmarks differ.
7. **The date of Mittelmann's binary QPLIB page.** The page header reads "9 May 2026", but the benchmark index labels it "5-9-2025". The page lists BARON 25.11.17, which suggests the 2026 header is the current one [inferred].
8. **Two hedged explanations of ANTIGONE's weaknesses.** Kronqvist et al. blame missed convexity for its weak lower bounds; Du et al. blame its reformulation step for its failures. Both are guesses about the same closed code, and neither was tested.

## Gaps

- **OpenReview threads: not read.** Affected: NeurIPS 2022 (SnAKe, forum QudXypzItbt; tree kernels, forum -cBZMMTImxT), NeurIPS 2023 (GNN symmetry breaking), NeurIPS 2024 (MDP-BO) and ICLR 2026 (BoGrape).
  - The OpenReview API answered HTTP 403, "Challenge verification required"; I did not try to get around it.
  - The Wayback captures of the SnAKe forum page (2022–2026) contain no review text, because the page is rendered client-side.
  - The forum IDs come from the NeurIPS virtual-site data files.
- **Castro, Liao and Liang (2022)**, the direct comparison of her linear and logarithmic partitioning schemes: the identifier was checked, but neither abstract nor text was obtained. Springer served a client challenge, OpenAlex and Semantic Scholar have no abstract, and one WebSearch found only the bibliographic record.
- **Full texts not read** (paywalled, or the preprint was missing or behind a bot check):
  - Zhang and Sahinidis 2016: one S2 context only.
  - Kılınç and Sahinidis 2018: abstract only; their ANTIGONE tables were not read.
  - Vigerske and Gleixner 2018: the ZIB repository is behind an Anubis bot check.
  - Zhang and Sahinidis 2024: the solver list only.
  - Kim, Richard and Tawarmalani 2025: abstract and S2 contexts.
  - Castillo Castillo et al. 2018 and Castro 2016: S2 contexts.
  - Buchheim and D'Ambrosio 2017, Kolodziej et al. 2013 and Boukouvala et al. 2017: one S2 context each.
- **Bonami, Günlük and Linderoth's BoxQP comparison with GloMIQO** (Optimization Online 2016/06/5488; *Math. Program. Comput.* 10(3):333–382, 2018, DOI 10.1007/s12532-018-0133-x): consulted, but the result tables do not survive text extraction, so no numbers were used.
- **Udell and Boyd, "Maximizing a Sum of Sigmoids"** (Stanford manuscript, 5 May 2014). An S2 context attributes to some version of it the remark that BARON and ANTIGONE are "offered as commercial software with a hefty license fee even for academic use". The version on Boyd's site does not contain it, so it was not used.
- **No published comment, reply, erratum or retraction.** Crossref relation and update fields are empty for 14 of her key DOIs. PubPeer and the Retraction Watch database were not searched directly.
- **No critical essay, blog post or interview** about her work was found. One WebSearch on independent ENTMOOT comparisons returned only her group's own material.
- **Her replies to the era E-C critiques** (trust regions, OMLT's footprint, the tightness of tree formulations, SnAKe's convergence) beyond R3: none found.
- **Journal reviews** (*J. Global Optim.*, *Math. Program.*, *INFORMS J. Comput.*, *Comput. Chem. Eng.*, *JMLR*) are not public.
- **Unstated reasons**: why Mittelmann dropped ANTIGONE in 2025, and why SCIP 8 left it out, is not said in the sources.
- **Dey and Gupte's APOGEE sentence**: whether it survives in the published *Oper. Res.* version was not checked.
- **ASR caveat**: the transcripts used in R4 and PC-10 are machine captions, so the words spoken may differ.

## Sources

One line each: title, author, date, URL or DOI, primary or secondary, and how it was read.

**Primary: Misener, her group, her software (17)**

1. R. Misener, seminar on partition-based formulations, online series "machine learning needs mathematical optimization", April 2021. YouTube UcNXm24uQjE; ASR transcript `../sources/talks/2021-04-sevilla-partition-based-formulations-relu-UcNXm24uQjE.txt`, saved by a sibling agent (Q&A read). Primary, ASR.
2. R. Misener, Cornell seminar ("Between formulations..."), 17 Feb 2023. YouTube bC4PDG9EZA8; ASR transcript `../sources/talks/2023-02-17-cornell-between-formulations-love-parameters-bC4PDG9EZA8.txt` (opening and Q&A read). Primary, ASR.
3. R. Misener, seminar at Manchester, January 2025. YouTube 2br7KspcQXk; ASR transcript `../sources/talks/2025-01-manchester-autonomous-research-machines-2br7KspcQXk.txt` (SnAKe passage read). Primary, ASR.
4. R. Misener, "Just relax, Or: How I'm bad at my own algorithmic advice.", Imperial inaugural lecture, 13 Mar 2023. YouTube dN860HNsAs0; ASR transcript `../sources/talks/2023-03-13-just-relax-inaugural-lecture-asr.md` ([35:15] read). Primary, ASR.
5. R. Misener, "Christodoulos Achilleus Floudas", *SIAG/OPT Views and News* 24(1):12–16, October 2016, https://siagoptimization.github.io/assets/views/ViewsAndNews-24-1.pdf (p. 13 read). Primary.
6. C. A. Floudas, R. Misener, GAMS/ANTIGONE solver manual (dated 16 April 2013), https://www.gams.com/latest/docs/S_ANTIGONE.html (introduction read). Primary.
7. F. Ceccon, J. Jalving, J. Haddad, A. Thebelt, C. Tsay, C. D. Laird, R. Misener, "OMLT: Optimization & Machine Learning Toolkit", arXiv:2202.02414v2; *JMLR* 23(349):1–8, 2022 (p. 3 read). Primary.
8. S. Zhang, J. S. Campos, C. Feldmann, F. Sandfort, M. Mathea, R. Misener, "Augmenting optimization-based molecular design with graph neural networks", arXiv:2312.03613v1, December 2023 (pp. 16–17 read). Primary.
9. J. P. Folch, C. Tsay, R. M. Lee, B. Shafei, W. Ormaniec, A. Krause, M. van der Wilk, R. Misener, M. Mutný, "Transition Constrained Bayesian Optimization via Markov Decision Processes", arXiv:2402.08406v3 (NeurIPS 2024) (pp. 5 and 10 read). Primary.
10. J. P. Folch, S. Zhang, R. M. Lee, B. Shafei, D. Walz, C. Tsay, M. van der Wilk, R. Misener, "SnAKe: Bayesian Optimization with Pathwise Exploration", arXiv:2202.00060v4 (NeurIPS 2022) (metadata). Primary.
11. T. Boyne, J. P. Folch, R. M. Lee, B. Shafei, R. Misener, "BARK: A Fully Bayesian Tree Kernel for Black-box Optimization", arXiv:2503.05574v2, 6 Jun 2025 (pp. 1, 4 and 7 read). Primary.
12. A. Thebelt, C. Tsay, R. M. Lee, N. Sudermann-Merx, D. Walz, B. Shafei, R. Misener, "Tree ensemble kernels for Bayesian optimization with known constraints over mixed-feature spaces", arXiv:2207.00879v3 (NeurIPS 2022; title confirmed in the proceedings listing) (abstract). Primary.
13. C. Tsay, J. Kronqvist, A. Thebelt, R. Misener, "Partition-based formulations for mixed-integer optimization of trained ReLU neural networks", arXiv:2102.04373v2 (abstract). Primary.
14. J. Kronqvist, R. Misener, C. Tsay, "P-split formulations: a class of intermediate formulations between big-M and convex hull for disjunctive constraints", *Math. Program.* 2025, DOI 10.1007/s10107-025-02232-1; arXiv:2202.05198v3 (abstract). Primary.
15. R. Baltean-Lugojan, R. Misener, "Piecewise parametric structure in the pooling problem: from sparse strongly-polynomial solutions to NP-hardness", *J. Global Optim.* 71(4):655–690, 2018, DOI 10.1007/s10898-017-0577-y (citation contexts via the S2 references API; full text not read). Primary.
16. cog-imperial/OMLT GitHub issues #80, #98, #107, #173 and #183, plus filtered issue lists, https://github.com/cog-imperial/OMLT/issues (raw page data, 2026-10-10). Primary for the team's replies; observed for the user reports.
17. cog-imperial/entmoot GitHub issues #29 and #38, plus the issue list, https://github.com/cog-imperial/entmoot/issues (2026-10-10). Primary and observed.

**Secondary and observed: critics, benchmarks, indexes (41)**

18. Y. Zhang, N. V. Sahinidis, "Global optimization of mathematical programs with complementarity constraints and application to clean energy deployment", *Optim. Lett.* 10(2):325–340, 2016, DOI 10.1007/s11590-015-0880-9 (S2 context). Secondary.
19. W. Du, C. Wang, C. Fan, Z. Li, et al., "A production planning benchmark for real-world refinery-petrochemical complexes", arXiv:2503.22057v1, 28 Mar 2025 (pp. 25–29 read). Secondary.
20. J. Kronqvist, D. E. Bernal, A. Lundell, I. E. Grossmann, "A review and comparison of solvers for convex MINLP", *Optim. Eng.* 20(2):397–455, 2019, DOI 10.1007/s11081-018-9411-8 (pp. 421, 426 and 436 read). Secondary.
21. T. He, M. Tawarmalani, "Extracting structure from functional expressions for continuous and discrete relaxations of MINLPs", arXiv:2205.01442v1, 3 May 2022 (pp. 1–2 and 23 read). Secondary.
22. T. He, M. Tawarmalani, "MIP Relaxations in Factorable Programming", *SIAM J. Optim.* 34(3):2856–2882, 2024, DOI 10.1137/22m1515537; arXiv:2310.07168v3 (pp. 1, 11 and 18–19 read). Secondary.
23. S. S. Dey, A. Gupte, "Analysis of MILP Techniques for the Pooling Problem", *Oper. Res.* 63(2):412–427, 2015, DOI 10.1287/opre.2015.1357 (abstract); preprint https://optimization-online.org/2013/04/3849/ (pp. 21 and 28 read). Secondary.
24. A. Gupte, S. Ahmed, S. S. Dey, M. S. Cheon, "Relaxations and discretizations for the pooling problem", *J. Global Optim.* 67(3):631–669, 2017, DOI 10.1007/s10898-016-0434-4; preprint https://optimization-online.org/2015/04/4883/ (pp. 2 and 16 read). Secondary.
25. C. Füllner, S. Rebennack, "Non-convex nested Benders decomposition", *Math. Program.* 196(1–2):987–1024, 2022, DOI 10.1007/s10107-021-01740-0 (p. 1021 read). Secondary.
26. H. Mittelmann, benchmark pages, live on 2026-10-10: https://plato.asu.edu/ftp/cnconv.html (17 May 2026), https://plato.asu.edu/ftp/qplib.html (header 9 May 2026), https://plato.asu.edu/ftp/nonbinary.html (12 May 2026), https://plato.asu.edu/ftp/minlp.html (26 Feb 2026), https://plato.asu.edu/bench.html. Secondary.
27. H. Mittelmann, MINLP benchmark page, Wayback Machine captures 20170717125813, 20211220190643, 20230127153423, 20240409181240, 20240921192253, 20250305061825 and 20250819054738 of http://plato.asu.edu/ftp/minlp.html. Secondary.
28. A. Uribe-Rodriguez, P. M. Castro, G. Guillén-Gosálbez, B. Chachuat, "Global optimization of large-scale MIQCQPs via cluster decomposition: Application to short-term planning of an integrated refinery-petrochemical complex", *Comput. Chem. Eng.* 140:106883, 2020, DOI 10.1016/j.compchemeng.2020.106883; accepted manuscript, Spiral hdl 10044/1/84608 (pp. 2, 27 and 33 read). Secondary.
29. P. M. Castro, "Spatial branch-and-bound algorithm for MIQCPs featuring multiparametric disaggregation", *Optim. Methods Softw.* 32(4):719–737, 2017, DOI 10.1080/10556788.2016.1264397 (abstract via OpenAlex). Secondary.
30. P. M. Castro, "Global Optimization of QCPs Using MIP Relaxations with a Base-2 Logarithmic Partitioning Scheme", *Ind. Eng. Chem. Res.* 62(28):11053–11066, 2023, DOI 10.1021/acs.iecr.3c00191 (abstract via OpenAlex). Secondary.
31. P. M. Castro, "Normalized multiparametric disaggregation: an efficient relaxation for mixed-integer bilinear problems", *J. Global Optim.* 64(4):765–784, 2016, DOI 10.1007/s10898-015-0342-z (S2 contexts). Secondary.
32. P. A. Castillo Castillo, P. M. Castro, V. Mahalec, "Global optimization of MIQCPs with dynamic piecewise relaxations", *J. Global Optim.* 71(4):691–716, 2018, DOI 10.1007/s10898-018-0612-7 (S2 contexts). Secondary.
33. P. M. Castro, Q. Liao, Y. Liang, "Comparison of mixed-integer relaxations with linear and logarithmic partitioning schemes for quadratically constrained problems", *Optim. Eng.* 23(2):717–747, 2022, DOI 10.1007/s11081-021-09603-5 (metadata only; not read). Secondary.
34. S. P. Kolodziej, I. E. Grossmann, K. C. Furman, N. W. Sawaya, "A discretization-based approach for the optimization of the multiperiod blend scheduling problem", *Comput. Chem. Eng.* 53:122–142, 2013, DOI 10.1016/j.compchemeng.2013.01.016 (S2 context). Secondary.
35. F. Boukouvala, M. M. F. Hasan, C. A. Floudas, "Global optimization of general constrained grey-box models: new method and its application to constrained PDEs for pressure swing adsorption", *J. Global Optim.* 67(1–2):3–42, 2017, DOI 10.1007/s10898-015-0376-2 (S2 context). Secondary.
36. C. Buchheim, C. D'Ambrosio, "Monomial-wise optimal separable underestimators for mixed-integer polynomial optimization", *J. Global Optim.* 67(4):759–786, 2017, DOI 10.1007/s10898-016-0443-3 (S2 context); preprint https://optimization-online.org/2013/11/4127/ (checked: no ANTIGONE comparison). Secondary.
37. M. Dressler, R. Murray, "Algebraic Perspectives on Signomial Optimization", *SIAM J. Appl. Algebra Geom.* 6(4):650–684, 2022, DOI 10.1137/21m1462568; arXiv:2107.00345v1 (pp. 3, 14 and 19 read). Secondary.
38. H. Nagarajan, M. Lu, S. Wang, R. Bent, K. Sundar, "An adaptive, multivariate partitioning algorithm for global optimization of nonconvex programs", *J. Global Optim.* 74(4):639–675, 2019, DOI 10.1007/s10898-018-00734-1; arXiv:1707.02514v4 (pp. 3, 33 and 38 read). Secondary.
39. K. Bestuzheva, A. Chmiela, B. Müller, F. Serrano, S. Vigerske, F. Wegscheider, "Global optimization of mixed-integer nonlinear programs with SCIP 8", *J. Global Optim.* 91(2):287–310, online 14 Dec 2023, DOI 10.1007/s10898-023-01345-1 (pp. 296, 301 and 303 read). Secondary.
40. C. Shi, M. Emadikhiav, L. Lozano, D. Bergman, "Constraint Learning to Define Trust Regions in Optimization over Pre-Trained Predictive Models", *INFORMS J. Comput.* 36(6):1382–1399, 2024, DOI 10.1287/ijoc.2022.0312; arXiv:2201.04429v3 (pp. 2, 4, 6, 12, 14 and 17–18 read). Secondary.
41. A. M. Schweidtmann, J. M. Weber, C. Wende, L. Netze, A. Mitsos, "Obey validity limits of data-driven models through topological data analysis and one-class classification", *Optim. Eng.* 23(2):855–876, 2022, DOI 10.1007/s11081-021-09608-0 (p. 857 read). Secondary.
42. J. Kim, J.-P. P. Richard, M. Tawarmalani, "A Reciprocity Between Tree Ensemble Optimization and Multilinear Optimization", *Oper. Res.* 73(5):2610–2626, 2025, DOI 10.1287/opre.2022.0150 (abstract; S2 contexts). Secondary.
43. M. S. F. Atallah, L. Dankwart, D. Neider, M. Yalçıner, "eNNcode: Optimization-Based Analysis of Neural Networks", IJCAI-26 Demonstrations Track, pp. 8358–8362, 2026, DOI 10.24963/ijcai.2026/956 (read). Secondary.
44. D. Ovalle, L. T. Biegler, I. E. Grossmann, C. D. Laird, M. Dulce Rubio, "Conformal Mixed-Integer Constraint Learning with Feasibility Guarantees", arXiv:2506.03531v1, 2025 (p. 10 read). Secondary.
45. S. S. Ramesh, P. G. Sessa, A. Krause, I. Bogunovic, "Movement Penalized Bayesian Optimization with Application to Wind Energy Systems", arXiv:2210.08087v1 (NeurIPS 2022) (p. 2 read). Secondary.
46. A. X. Yang, L. Aitchison, H. B. Moss, "MONGOOSE: Path-wise Smooth Bayesian Optimisation via Meta-learning", arXiv:2302.11533v2 (pp. 2 and 4 read). Secondary.
47. Q. Chen, R. Al Kontar, "The Traveling Bandit: A Framework for Bayesian Optimization with Movement Costs", *Technometrics* 68(2):239–250, DOI 10.1080/00401706.2025.2573228; arXiv:2410.14533v1 (pp. 2–4 and 16 read). Secondary.
48. J. Tong, J. Cai, T. Serra, "Optimization Over Trained Neural Networks: Taking a Relaxing Walk", arXiv:2401.03451v2 (abstract). Secondary.
49. J. Tong, Y. Zhu, T. Serra, S. Burer, "Optimization over Trained Neural Networks: Going Large with Gradient-Based Algorithms", LNCS (CPAIOR), pp. 596–613, 2026, DOI 10.1007/978-3-032-27242-3_35 (metadata; S2 context). Secondary.
50. E. G. Birgin, R. D. Lobato, J. M. Martínez, "Packing ellipsoids by nonlinear optimization", *J. Global Optim.* 65(4):709–743, 2016, DOI 10.1007/s10898-015-0395-z (S2 context). The study it summarises: J. Kallrath, S. Rebennack, "Cutting ellipses from area-minimizing rectangles", *J. Global Optim.* 59(2–3):405–437, 2014, DOI 10.1007/s10898-013-0125-3 (metadata). Secondary.
51. S. S. Dey, N. Jiang, A. Kazachkov, A. Lodi, G. Muñoz, "Chvátal-Gomory Rounding of Eigenvector Inequalities for QCQPs", arXiv:2604.00932v1, 1 Apr 2026 (S2 context). Secondary.
52. Y. Zhang, N. V. Sahinidis, "Solving continuous and discrete nonlinear programs with BARON", *Comput. Optim. Appl.* 92(3):1123–1161, 2024, DOI 10.1007/s10589-024-00633-0 (S2 context). Secondary.
53. M. R. Kılınç, N. V. Sahinidis, "Exploiting integrality in the global optimization of mixed-integer nonlinear programming problems with BARON", *Optim. Methods Softw.* 33(3):540–562, 2018, DOI 10.1080/10556788.2017.1350178 (abstract via OpenAlex). Secondary.
54. GAMS Development Corp., release notes RN_238 to RN_251 (GAMS 23.8 to 25.1) and RN_26 to RN_54, https://www.gams.com/latest/docs/RN_MAIN.html (entries naming GloMIQO and ANTIGONE extracted). Secondary; the distributor's record.
55. Semantic Scholar Graph API: citation contexts for 20 of her works (about 2,000 citing records), reference contexts for 2 works, batch metadata, https://api.semanticscholar.org. Index.
56. Crossref REST API: metadata for 54 DOIs, including the relation and update fields of 14 of her works, https://api.crossref.org. Index.
57. OpenAlex API (abstracts and locations for 17 DOIs), Unpaywall API (27 DOIs; email parameter nuwa-skill@users.noreply.github.com) and arXiv API (metadata for 17 identifiers; title searches). Index.
58. NeurIPS virtual-site data files for 2022–2024 (https://neurips.cc/static/virtual/data/neurips-YYYY-orals-posters.json), used to obtain the OpenReview forum IDs. Index.

**Consulted but not used (16)**

59. OpenReview API (api.openreview.net and api2.openreview.net): HTTP 403, challenge verification required.
60. Wayback captures of https://openreview.net/forum?id=QudXypzItbt (2022–2026): no review text.
61. M. Udell, S. Boyd, "Maximizing a Sum of Sigmoids", manuscript, 5 May 2014, https://web.stanford.edu/~boyd/papers/max_sum_sigmoids.html: the remark attributed to it by S2 is not in this version.
62. P. Bonami, O. Günlük, J. Linderoth, BoxQP preprint https://optimization-online.org/2016/06/5488/ (*Math. Program. Comput.* 10(3):333–382, 2018, DOI 10.1007/s12532-018-0133-x): the tables cannot be extracted.
63. B. Beach, R. Burlacu, A. Bärmann, L. Hager, R. Hildebrand, arXiv:2302.01164v1: no relevant content.
64. P. M. Castro, J. P. Teles, "Comparison of global optimization algorithms for the design of water-using networks", *Comput. Chem. Eng.* 52:249–261, 2013, DOI 10.1016/j.compchemeng.2013.01.013: the repository file is a one-page image.
65. S. Vigerske, A. Gleixner, "SCIP: global optimization of mixed-integer nonlinear programs in a branch-and-cut framework", *Optim. Methods Softw.* 33(3):563–593, 2018, DOI 10.1080/10556788.2017.1335312: abstract only; the ZIB report is behind a bot check.
66. M. Turner, A. Chmiela, T. Koch, M. Winkler, "PySCIPOpt-ML", arXiv:2312.08074v2: a feature table only, no OMLT benchmark.
67. The Sahinidis group website (https://sahinidis.coe.gatech.edu/; no PDFs) and the minlp.com BARON pages (vendor claims, not specific to ANTIGONE).
68. BCS "Needham Debate" podcast, local ASR `../sources/talks/2024-02-26-bcs-needham-debate-podcast-local-asr.md` (low reliability; no critique found).
69. DBLP person page 04/8800: bot check.
70. Springer and ScienceDirect article pages: client challenge or HTTP 403.
71. ULisboa publication record https://biblios.ciencias.ulisboa.pt/detalhes/55524: a JavaScript application with no data in the page.
72. N. Boland, T. Kalinowski, F. Rigterink, *J. Global Optim.* 66(4):669–710, 2016, DOI 10.1007/s10898-016-0404-x, and M. Alfaki, D. Haugland, *J. Global Optim.* 56(3):917–937, 2013, DOI 10.1007/s10898-012-9890-7: their S2 contexts are descriptive only.
73. NeurIPS proceedings abstract pages for the 2022–2024 papers (proceedings.neurips.cc), checked for links to reviews: none.
74. WebSearch, 2 calls: the abstract of Castro, Liao and Liang; independent ENTMOOT comparisons.
