# Daniel P. Robinson: process evidence (research agent 03)

| Field | Value |
|---|---|
| Researcher | Daniel P. Robinson (Lehigh University ISE since 2019; Johns Hopkins Applied Mathematics and Statistics 2011-2019; PhD Mathematics, UC San Diego 2007; postdoctoral work at Oxford / RAL with N. I. M. Gould and at Northwestern) |
| Dimension | 03: process evidence, i.e. what he actually DOES (software, experiment sections, baselines, test sets, revisions, errata, rebuttals, abandoned work) |
| Research date | 2026-10-16 |
| Sources consulted | 52 entries in Sources. 48 are primary: 7 git repositories cloned and read, GALAHAD source and documentation files, about 30 full texts or preprint versions read in their experiment sections, 2 corrigenda, NeurIPS reviews and author feedback, his homepage. 4 are secondary: the Optimization Online listing pages, Crossref records, the DBLP SPARQL listing, and one entry covering a WebSearch summary plus the sibling notes 02 and 06, used as leads |
| WebSearch calls used | 1 (of 7 allowed) |
| User-supplied material | none. `references/sources/{papers,talks,essays,software}` held only `.gitkeep`. `private/` was not opened |
| Language | English (team.json) |

**How the evidence was gathered (and what failed).**
- DBLP person pages are behind a bot challenge (Anubis). I listed his 85 DBLP records through the DBLP SPARQL endpoint instead.
- The arXiv API returned HTTP 429. I read the arXiv abstract pages (version histories) and downloaded 14 PDF versions directly.
- I cloned every public repository under the GitHub account `daniel-p-robinson` (3 repositories, created 2016-11-22) and three Curtis repositories that list Robinson as an author (StochasticSQP, TRACE, Utilities). I read READMEs, AUTHORS files, option files, test scripts and full commit histories. I compiled and ran nothing.
- I read the GALAHAD repository on GitHub (`ralna/GALAHAD`, master branch): the package documentation `doc/src/{trs,rqs,cqp,dqp}.tex`, the `src/oblivion` and `src/forthcoming` READMEs, and the headers and inline comments of `s2qp.F90`, `fisqp.F90` and `trace.F90`.
- I read the experiment sections of the papers in author-hosted PDFs (Curtis's Lehigh site), Optimization Online preprints and arXiv versions. Wherever two versions exist, I compared them.
- NeurIPS 2018-2020 reviews and author responses are public on papers.nips.cc, and I read them. OpenReview (TMLR 2023, NeurIPS 2024) answered with a browser-verification challenge to curl, to its API and to WebFetch. I did not try to get past it, so those reviews are **not read**.
- No talk video or transcript was found, so nothing was saved under `sources/talks/`.

**Tags.** [stated] = he or his co-authors wrote it as a claim. [practice] = what was done, visible in code, experiment sections, version histories or errata. [observed] = what others (referees, the GALAHAD maintainer) wrote. [inferred] = my reading, not to be quoted as his view. P = primary, S = secondary.

**The co-authorship caveat applies to almost every item.** Robinson has only one sole-authored paper in DBLP (JOTA 2015). Every practice below comes from a team: Gould (2007-2016), Gill (2008-2020), Curtis (2011 onward, alphabetical author order) and students. Where the repositories show who wrote the code, I say so. Elsewhere a practice belongs to the team. It still shows what Robinson put his name to, again and again, across different teams.

---

## 0. Repeated behaviours (each seen in 3 or more independent places)

| # | Behaviour (short form) | Where it shows (era) | Count |
|---|---|---|---|
| B1 | **Build an in-house twin baseline that differs from the new method in one component only.** The new feature is then isolated, and the twin is calibrated against a mature code | AAL-TR vs BAL-TR, plus Lancelot (MP 2015); six variants in one Matlab package, plus Lancelot with only steering added (OMS 2016); FiSQO vs PenSQO, "the only difference between the two methods is in the step acceptance criteria" (SIOPT 2015 preprint); Algorithm 2(s_k) vs Algorithm 2(s_k, d_k) (MP 2019); exact vs inexact iSQO from the same code (SIOPT 2014); "no reg." twins (SIOPT 2021); exact vs inexact SISQO (IJOO 2024); TRS/RQS polynomial orders T1/T2/P2/P4 (MPC 2013) | 8 |
| B2 | **Run external baselines unmodified, or as their authors ship them, and say so.** When parameters are changed, the reason is given | OBA "made no modifications to their code" (SIOPT 2017); LIBLINEAR and ASA-CG "default parameter settings" (OMS 2018); gglasso "All default settings" (SIOPT 2022); the Julia code of [31] "with the AdapGD option and its default parameter settings" (SIOPT 2024); Bazinga.jl downloaded from GitHub (2024 preprint); Lancelot defaults changed "to have as fair a comparison as possible" (MP 2015) | 6 |
| B3 | **State test-set selection as an explicit filter, with every exclusion named and justified.** The filters often depend on how the algorithms behaved | iSQO: "bqpd did not fail during the run of any of the four algorithm variants" (2014); AAL: problems listed one by one with reasons (2015); OMS 2016: only problems "for which at least one of our six solvers obtained a successful result"; MP 2019 v1: kept only problems where negative curvature was used; SIOPT 2021 (stochastic SQP): "the LICQ held at all iterates in all runs of all algorithms that we ran"; SIOPT 2024: "Gurobi did not report any errors"; FaRSA and FaRSA-Group: LIBSVM filtered by class type, memory and duplicate families | 7 |
| B4 | **Label the implementation "preliminary" or "basic", and present gains as potential rather than as definitive comparisons** | S2QP "preliminary numerical results" (2008); iSQO "a preliminary implementation" (2014); AAL "only preliminary implementations" (2015); FaRSA "a preliminary Matlab implementation" (2017); FiSQO "a basic Matlab implementation" (2015); FaRSA-Group "Preliminary numerical results" (2020); proximal-gradient "Our preliminary numerical results" (2024) | 7 |
| B5 | **Check empirically whether a theoretical worry, or a theory-only assumption, matters in practice** | OMS 2016: safeguarded steering variants built "To test the potential for the penalty parameter to be reduced too quickly"; SIOPT 2021: frequency of event (25), "evidence that the theory offered under the event (25) is relevant in practice"; MP 2019 v3: added cost of negative curvature discussed beside the results; SIOPT 2021 (Newton-CG): the regularization needed for optimal complexity measured as "the price of equipping the approach with optimal complexity guarantees" | 4 |
| B6 | **Disclose heuristics that sit outside the theory, then patch the theory to cover a bounded version of them** | FaRSA-Group: the PG-parameter update "is not covered by our analysis", and a cap of "say 100 times" makes it covered; SIPM: tighter constants used "to have consistency between our analysis and numerical experimentation"; iSQO: termination rule changed from the stated algorithm, with the reason; FiSQO: backtracking in place of "the largest value", argued to keep the guarantees | 4 |
| B7 | **Two-step publication: theory with preliminary numerics first, then a "numerical experience" or "practical issues" paper** | Gould & Robinson 2010 "Global Convergence", then "Local Convergence and Practical Issues"; Curtis-Jiang-Robinson MP 2015, then "...algorithms and practical numerical experience" OMS 2016; FaRSA SIOPT 2017, then "FaRSA ...: local convergence and numerical experience" OMS 2018; Gould-Loh-Robinson 2014 "unified step computation", then "local convergence and numerical results" 2015 | 4 |
| B8 | **Prototype in Matlab (later Python); production code is written by someone else or never finished** | S2QP (his own Fortran, now in GALAHAD "oblivion"); FiSQP "originally written in Matlab by Yueling Loh and Daniel P. Robinson", Fortran translation in GALAHAD "forthcoming"; FaRSA in C written by student T. Chen; StochasticSQP and TRACE Matlab packages written by Curtis; "available upon request" (FaRSA 2017, FaRSA-Group 2020); homepage "Coming soon" list | 6 |

---

## 1. Research taste, as revealed in practice

**1.1 A result counts when the new feature beats its own twin, not when it beats the world.** [practice, P] (B1)
- AAL (Curtis, Jiang, Robinson, *Math. Program.* 152:201-245, 2015, DOI 10.1007/s10107-014-0784-y; author PDF §4.1): "For comparison purposes, we also implemented a trust-region variant of the basic augmented Lagrangian method given by Algorithm 1, which we will refer to as BAL-TR. The components of these two implementations were mostly identical." Lancelot then serves only to show that the in-house twin is not a strawman: "we can compare them to illustrate that our implementation of BAL-TR is roughly on par with Lancelot" (§4.3).
- Filter SQP (Gould, Loh, Robinson, "A Filter SQP Method: Local Convergence and Numerical Results", RAL P-2014-012 / Optimization Online 2014/12/4702; *SIAM J. Optim.* 25(3):1885-1911, 2015, DOI 10.1137/140996677; §5): "Since we have complete control over both algorithms, we are able to isolate any aspect of interest (e.g., the influence of b-pairs), design and perform revealing numerical tests, and confidently present the numerical results."
- Negative curvature (Curtis & Robinson, arXiv:1703.00412; *Math. Program.* 176:69-94, 2019, DOI 10.1007/s10107-018-1335-8): every version compares "Algorithm 2(s_k)" with "Algorithm 2(s_k, d_k)". The stochastic part compares "SG" with "NC", using "the same starting point and initial seeds for the random number generators" (v3 §3.3).
- [inferred] The question he puts to an experiment is narrow: does *this* mechanism (steering, negative curvature, b-pairs, inexactness, regularization) pay for itself? The question is seldom "is this the fastest solver". That fits the stated belief R4 in note 02 ("a design feature is worth it only if computation shows consistent gains").

**1.2 "As reliable as" is an acceptable claim. He refuses to over-claim efficiency.** [practice/stated, P]
- Stochastic SQP (Berahas, Curtis, Robinson, Zhou, arXiv:2007.10525 v1 §4.1; *SIAM J. Optim.* 31(2):1352-1379, 2021, DOI 10.1137/20M1354556): "We do not claim that "SQP Adaptive" is as efficient as "SQP Backtracking" since, as has been verified by others in the literature, the line search scheme is very effective across a broad range of problems."
- DQP (Gould & Robinson, JHU OPT-2016/2b / Optimization Online 2016/02/5332; *Comput. Optim. Appl.* 67(1):1-38, 2017, DOI 10.1007/s10589-016-9886-1; conclusion): "we believe that CQP remains the best solver for solving QP problems when good estimates of the solution are not known in advance." Here CQP, his own earlier solver with Gould and Orban, beats the new one, and the paper says so.
- FaRSA OMS 2018 (Chen, Curtis, Robinson, *Optim. Methods Softw.* 33(2):396-415, DOI 10.1080/10556788.2017.1415336; conclusion): "It should also be mentioned that FaRSA has a greater memory requirement than the other methods primarily because of the memory needed for our reduced space" [-step calculations; the final word is garbled in text extraction].

**1.3 Several flagship papers carry no experiments at all.** [practice, P]
- The interior-point trust funnel (Curtis, Gould, Robinson, Toint, *Math. Program.*, 2017, DOI 10.1007/s10107-016-1003-9; author PDF) has no numerical section. Its conclusion argues viability in words: "each subproblem may be solved approximately using matrix-free iterative methods, which means that the algorithm is viable for solving large-scale barrier subproblems."
- TRACE (Curtis, Robinson, Samadi, *Math. Program.* 162:1-32, 2017, DOI 10.1007/s10107-016-1026-2) has no numerics either. Its conclusion admits idealizations: "For simplicity in revealing the salient features of our algorithm and its theoretical properties, we have assumed that the algorithm uses exact first- and second-order derivative information, and that each iteration involves computing a globally optimal solution of a trust region subproblem."
- Regional complexity (Curtis & Robinson, arXiv:1802.01062 v1 and v2; *Math. Program.* 187:579-615, 2021, DOI 10.1007/s10107-020-01492-3) has no numerical section in either version. Text search found "numerical" only in the references.
- [inferred] Theory-only papers are where he goes after complexity or globalization results. Papers about a design feature always carry experiments. See Contradiction C3.

---

## 2. Problem choice, as revealed in practice

**2.1 Take a working method for the easy class and extend its theory to the hard class, keeping it identical on the easy class.** [practice, P]
- ncBQP (Mohy-ud-Din & Robinson, *SIAM J. Optim.* 25:2385-2407, 2015, DOI 10.1137/15M1022100; Crossref abstract, full text **not read**): "In the strictly convex case, our method is equivalent to the state-of-the-art algorithm by Dostál and Schöberl [...]. Unlike their method, however, we establish a convergence theory for our algorithm that holds even when the problems are nonconvex." Mohy-ud-Din's JHU dissertation (2014) has the same title, with Robinson as advisor, according to the Mathematics Genealogy listing in a WebSearch summary [S].
- PDAS (Curtis, Han, Robinson, *Comput. Optim. Appl.*, 2015, DOI 10.1007/s10589-014-9681-9; author PDF §1): "in our experience, our techniques often leave the auxiliary set empty. This is advantageous as in such cases our instances reduce to the algorithm in [25], which is extremely efficient when it does converge."
- Stochastic SQP 2020 (abstract): "As a starting point for this stochastic setting, an algorithm is proposed for the deterministic setting that is modeled after a state-of-the-art line-search SQP algorithm, but uses a stepsize selection scheme based on Lipschitz constants [...] in place of the line search."

**2.2 Pick test problems that exercise the feature under study, sometimes after running the method.** [practice, P] (B3)
- MP 2019, arXiv v1 (2017-03-01) §2.4: "Second, we ran Algorithm 2 on this subset for 100 iterations and only kept those for which at least one direction of negative curvature was used. This process left us with the 26 test problems listed under the column "Problem" in Table 1." Further: "Such tight tolerances are chosen to allow both variants to reach the iteration limit on nearly all problems."
- v3 (2018-04-04) widened the set to all unconstrained CUTEst problems with n ≤ 500 and second derivatives available: "This left us with a test set of 97 problems". The figures still show only the subset where the feature fired: "Only problems for which at least one negative curvature direction is used are presented." (Fig. 2 caption).
- [inferred] v1 to v3 is the clearest before/after I found. A filter chosen after running the method and a 100-iteration cap gave way to a fixed a-priori test set with standard stopping rules. The plots remain restricted to the problems where the feature is active. The referee reports are not public, so the trigger for the change is unknown.

---

## 3. Idea generation (process traces only)

**3.1 Carry a mechanism from one setting into another and then test exactly that transfer.** [practice, P]
- Steering (from exact-penalty SQP) carried into augmented Lagrangian. OMS 2016 (Curtis, Gould, Jiang, Robinson, *Optim. Methods Softw.* 31(1):157-186, DOI 10.1080/10556788.2015.1071813; §3): "Our only modification to Lancelot was to incorporate a basic form of steering; that is, we did not change other aspects of Lancelot". Conclusion: "we suspect that the steering strategies described in this paper would also likely improve the performance of other AL-based methods".
- Line-search SQP carried into the stochastic setting by replacing the line search with Lipschitz-estimate step sizes (2020, §2-§3), then into rank-deficient Jacobians (Berahas, Curtis, O'Neill, Robinson, arXiv:2106.13015; *Math. Oper. Res.* 2024, DOI 10.1287/moor.2021.0154), inexact subproblems (Curtis, Robinson, Zhou, arXiv:2107.03512; *INFORMS J. Optim.* 2024, DOI 10.1287/ijoo.2022.0008) and inequality constraints (Curtis, Robinson, Zhou, arXiv:2302.14790; *SIAM J. Optim.* 2024, DOI 10.1137/23M1556149). [inferred] Each paper changes one assumption of the previous one.
- I found no account of where any single idea came from (no notebooks, no talk transcripts). Layer 3 stays thin. See Gaps.

---

## 4. Experiments and execution

**4.1 Fairness devices are written into the experiment section.** [practice, P] (B2)
- Same Lipschitz estimates for every method. Stochastic SQP 2020: L and Γ "were estimated using differences of gradients near the initial point and kept fixed for all subsequent iterations. (This process was done so that L and Γ were the same for both methods for each problem.)" (the Greek letter is garbled in extraction; Γ is the constraint-Jacobian constant). The same device appears in arXiv:2106.13015 §5.1: "This procedure was performed in such a way that, for each problem instance, all algorithms used the same values for these estimates."
- Removing a second-order advantage. 2020 §4.2: "we set Hk = I for all k for fairness of comparison with the (first-order) subgradient method."
- Per-instance tuning of the baseline, with its budget disclosed. 2020 §4.2: the subgradient method's parameter was tuned over 11 values for each instance. "Overall, this means that for each problem, "Stochastic Subgradient" was given 110 times the number of iterations that were allowed for "Stochastic SQP.""
- Using the competitor's own code. FaRSA SIOPT 2017 (Chen, Curtis, Robinson, *SIAM J. Optim.* 27(3):1583-1610, DOI 10.1137/16M1062259; §4.3): OBA's "Matlab implementation was graciously provided by the authors", and they "made no modifications to their code". Even where OBA failed with "ascent": "Although simple adaptive strategies could be used to avoid such issues, we made no such attempts because we did not want to make any edits to their code."
- Instrumenting a competitor when needed. Dollar, Gould, Robinson (RAL-TR-2009-003; published as Gould, Robinson, Thorne, *Math. Program. Comput.* 2(1):21-57, 2010, DOI 10.1007/s12532-010-0011-7; §4): "As a comparison, we use the MINPACK-2 package dgqt [...]; we slightly modified this software to record and print required details."
- Unequal budgets, justified by cost per iteration. Dai, Qu, Robinson ("A Proximal-Gradient Method for Constrained Optimization", Optimization Online 2024/04; *SIAM J. Optim.* 35(4):2654-2683, 2025, DOI 10.1137/24M1653586; §4.2): "Fewer maximum iterations was allowed for Bazinga compared to Algorithm 2.1 because each iteration of Bazinga is significantly more expensive compared to Algorithm 2.1."
- Excluding a competitor class on principle. FiSQO (2014/15 preprint §5): "We comment up front that we do not compare FiSQO to methods that use a feasibility restoration phase." The reasons given: restoration phases vary, they include heuristics, and avoiding them is the point of the paper. Similarly arXiv:2106.13015 §5: "We do not compare against the aforementioned method from [14] since, as previously mentioned, that approach may refine stochastic gradient estimates during each iteration as needed by a line search."

**4.2 Simulate a component that does not exist yet, so the theory can be tested now.** [practice, P]
- iSQO (Curtis, Johnson, Robinson, Wächter, *SIAM J. Optim.*, 2014, DOI 10.1137/130918320; §4.1): "Since there does not currently exist a QP solver that satisfies these requirements and provides an interface to readily incorporate our termination tests (so that the computed solutions are not more accurate than necessary), for the purposes of our preliminary experiments we have generated inexact solutions by perturbing the exact solutions provided by a state-of-the-art nonconvex QP solver." The perturbations are uniform random vectors, scaled until a termination test is just met.
- Stochastic SQP on CUTEst. The stochastic setting is created by adding Gaussian noise to exact gradients at four noise levels, with 10 runs each (2020 §4.2). In the public repository, the commit "Added noise to CUTEST problems" (Berahas, 2020-11-02) came after arXiv v1 (2020-07-20). [inferred] The public package was rebuilt after the paper's experiments.

**4.3 Small dense problems first, for inspection. Larger sets are promised.** [practice/stated, P] (Oxford era, 2008)
- S2QP local convergence (Gould & Robinson, Oxford NA Report 08/21 / Optimization Online 2008/12/2192; *SIAM J. Optim.* 20(4):2049-2079, 2010, DOI 10.1137/080744554; §5): "The HS test suite is comprised of generally small and dense problems that are very useful during early stages of code development; the small size of the problems allows for relatively careful inspection of each problem." §6: "Finally, we plan on extensively testing the package on larger problems from the CUTEr [17] test set." I found no later paper that does this. See §7 below for what became of the package.

**4.4 Parameters: "rough tuning", "no fine-tuning", "set by parameter tuning". Each time, the status is said.** [practice, P]
- FiSQO §5: "These choices were made based on our experience of developing other nonlinear optimization algorithms, and no fine-tuning of our choices was attempted for this basic implementation."
- FaRSA OMS 2018 §4.1: the default values "have been chosen based on a rough tuning procedure".
- FaRSA C README v2.0 (2018): parameters "are not recommended to be changed since they are set by parameter tuning."
- MP 2019 v3 §3.3: "we chose L1 ← 80 and σ1 ← 100 as the smallest values that yielded stable algorithm behavior for both algorithms." (The arrows and Greek letter are garbled in extraction.)

**4.5 Debugging is visible as reported failure modes and the safeguard each one led to.** [practice, P]
- MP 2019 v3 §3.3: "In preliminary training runs, we occasionally witnessed instances in which a particularly large stochastic gradient led to a large step, which in turn spoiled all previous progress made by the algorithm." Fix: cap the step norms. Also: "We witnessed similar poor behavior when the Lipschitz constant estimates were initialized to be too small".
- FaRSA-Group (Curtis, Dai, Robinson, arXiv:2007.14951 v1 §5.1; *SIAM J. Optim.* 2022, DOI 10.1137/21M1411111): when N < n the Hessian is singular, "which in practice often led to large CG directions and multiple backtracks in the line search. These ill effects were partly remedied by this scheme for updating" [a parameter].
- S2QP §5: "In particular, steering was essential in solving HS93 for otherwise the merit function converged to minus infinity, the constraints blew up, and the method failed."
- iSQO §4.1: the "infeasible stationary point" exit was restricted because, "in our experience, this would increase the likelihood that the code would terminate with this status, even though it may eventually terminate with the (more desirable) "optimal solution found" status if it were allowed to continue."
- Course code (GitHub `daniel-p-robinson/nonlinear-optimization-course`, ISE 417, Feb-Apr 2021, 17 + 6 commits by Robinson): commit "fixed issue with returning assymetric hessians" [sic]. The fix symmetrizes as `h = 0.5*(h+h')`. Commit "made paths used in test functions relative so that they work for everyone. Must run them from that directory now." [practice, P; teaching code, sole author of most files]

**4.6 Coding conventions in his own hand (2021 course code).** [practice, P]
- `newton.m` and `steepest_descent.m` carry a full header and a "History" block ("February 13, 2021: This is the original version."). They validate every input and set dummy outputs "to prevent errors resulting from bad inputs". Termination codes: `0` success with a *relative* test "||F(x)|| <= tol*max(1,||F(x_0)||)"; `1` step too small; `2` iteration limit; `-1` input error; `-2` "A NaN or Inf was detected"; `-9` "New warning encountered". MATLAB's singular-matrix warnings are caught and printed as a per-iteration column ("sing", "ill-cond", "nearsing").
- One `test_*.m` per solver runs every objective class (Rosenbrock, Genhumps, LeastSquares, LeastSquaresTukey, Logistic, Quadratic, LinearSphere) and writes `.out` files. `test_all.m` concatenates them. The README "To Do" list includes "Add more unconstrained problems from CUTEr." and "Add *equality* constrained problems from CUTEr."
- [inferred] These are the conventions of the stated-algorithm-to-code pipeline he teaches: relative stopping tests, explicit exit statuses, NaN/Inf guards. The same termination style, `max{1, ||·_0||}`, appears in the papers (2020 §4.1; arXiv:2106.13015 §5).

**4.7 Hardware and compute stay modest throughout.** [practice, P]
- 2008: HS problems, BFGS, B0 = I. 2014: Matlab plus bqpd on 309 CUTE/AMPL problems. 2016: Lancelot "compiled with gfortran-4.7 with optimization -O and using Intel MKL BLAS", "a single core of an Intel Xeon E5620". 2017: "a 64-bit machine with an Intel I7 4.0-GHz CPU and 16 GB of main memory". 2017-18: Python 2.7.13, then Matlab and TensorFlow, for MP 2019. 2020: "the cluster in the Computational Optimization Research Laboratory (COR@L) at Lehigh University with an AMD Opteron Processor 6128 2.0 GHz CPU". 2023-24: "the High Performance Computing cluster at Lehigh University with Matlab R2021b" (arXiv:2304.14907). 2023: Gurobi as subproblem solver (arXiv:2302.14790). 2024: Python with PyCUTEst.

---

## 5. Judging results

**5.1 Failures, negative results and inconvenient comparisons are reported.** [practice, P]
- DQP (2016 preprint §5): "This instance of DQP failed on 12 problems". The factorization variant "failed on 25 problems". On cross-over after the interior-point solver CQP: "Our tests showed that DQP was not especially effective in this capacity."
- PDAS (COAP 2015 §3): the authors build a counterexample to their own update: "The following three-dimensional example shows that the strategy may fail if H is positive definite, but not an M-matrix." And: "Indeed, if any of the index partitions that define iterations 0-3 are used as the initial partition, then the updating strategy generates the same cycle."
- FaRSA-Group §5: "Out of the 200 problem instances, FaRSA-Group failed 2 times and gglasso failed 7 times." FaRSA OMS 2018 adds the memory admission (1.2).
- Newton-CG (Curtis, Robinson, Royer, Wright, arXiv:1912.04365; *SIAM J. Optim.* 2021, DOI 10.1137/19M130563X): in v1, the complexity-driven regularization "has a small but noticeable effect on practical performance. This effect could be viewed as the price of equipping the approach with optimal complexity guarantees." v3 extends the test set and adds a "(no reg.)" twin for every variant. Its wording is stronger: "has a noticeable effect on practical performance, mostly in terms of Hessian-vector products".

**5.2 Anomalies get a mechanism-level explanation.** [practice, P]
- OMS 2016 §3.2: "We initially found this observation to be somewhat counterintuitive, but we believe that it can be explained by observing the penalty parameter updating strategy used by lancelot." The explanation is the decrease factors (0.1 vs 0.7). The paragraph closes with a proposed fix for Lancelot.
- OMS 2016 §3.2: "However, in our experiments, it was revealed that using the Newton model typically led to better performance" (better than the model the theory suggests). The reported results use the better-performing model.

**5.3 Theory claimed weaker, practice claimed sufficient.** [stated, P] (B5)
- OMS 2016 conclusion: "We feel confident that these tests clearly show that although our theoretical global convergence guarantee is weaker than some algorithms (i.e. we cannot prove that the penalty parameter will remain bounded under a suitable constraint qualification), this should not be a concern in practice."
- 2020 §4.2: "This provides evidence that the theory offered under the event (25) is relevant in practice."

**5.4 Corrections are published, and their scope is stated precisely.** [practice, P]
- TRACE corrigendum (Curtis's errata page, `CurtRobiSama17_corrigendum.pdf`): "A corrected statement and proof of Lemma 3.19 from the published paper is provided below. [...] This means that the inequality in the published paper is correct, but not as tight as it could have been."
- Stochastic SQP corrigendum (`BeraCurtRobiZhou21_corrigendum.pdf`): "A corrected statement of Corollary 3.14(a) from the published paper is below." No commentary.
- [inferred] Both errata sit on Curtis's site, not Robinson's. Note 06 F3 also lists a 2011 corrigendum report with Gould and Toint.

---

## 6. Expression

**6.1 A shared paper skeleton fixes the order: contributions, notation, analysis, then numerical results.** [practice, P]
- GitHub `frankecurtis/Utilities`: README "This repository contains scripts and other utilities for projects in the research groups of Frank E. Curtis and Daniel P. Robinson. The code is open source, but time has not been spent on documenting it." The `PaperStarter` sub-tool was started by Robinson ("starting paper starter with frank", 2021-07-10). He made 18 of the repository's 24 commits, nearly all in PaperStarter and LaTeX; Curtis made 6, including the CUTEst2Matlab tool. It generates a paper from journal templates (COAP, IMAJNA, MP, OPTLETTERS, SIOPT) and a Lehigh ISE technical-report format.
- `PaperStarter/src/body.tex` sections: Introduction; Contributions; Notation; Assumption; Organization; Analysis; Numerical Results; Conclusion. The sample citation is to TRACE (`CurtRobiSama17`). `LaTeX/dpr_fec.sty` and a shared `dpr_fec.bib` (1,821 entries by count of "@") give the two groups one macro set and one bibliography.
- [inferred] Analysis comes before numerics by default. "Numerical Results" is a section of every paper template, even though several published papers leave it out (1.3).

**6.2 Presentation devices that recur.** [practice, P]
- Dolan-Moré performance profiles (AAL 2015; OMS 2016; stochastic SQP 2020; Newton-CG 2021; CQP 2013; TRS/RQS 2010; FaRSA-Group 2020). Signed "outperforming factor" bar plots per problem (OMS 2016 COPS/OPF; MP 2019 v3 quantities (21)-(23); FaRSA-Group Fig. 3). Box plots of feasibility and KKT errors over noisy runs (2020; 2023). Full per-problem tables in appendices (DQP A.2; CQP A.2-A.5; FaRSA OMS 2018 Table 2 with the best time in red).
- Implementation status given in one phrase: "available upon request" (FaRSA-Group 2020: "We have developed a Python implementation of FaRSA-Group that is available upon request."); "we are happy to provide on request" (FaRSA SIOPT 2017); a GitHub link (FaRSA OMS 2018; arXiv:2106.13015 v2 footnote to `frankecurtis/StochasticSQP`).
- Omissions are stated: "Experiments with diminishing step sizes also showed favorable performance for our algorithm; these results are omitted due to page limit restrictions." (arXiv:2302.14790 §5); "for the sake of brevity, in this section we only present results for SIPM and PSGM" (arXiv:2304.14907 v3 §5).

**6.3 Titles change between report and journal.** [practice, P] (Optimization Online trail, listed by search on 2026-10-16)
- "A second derivative SQP method with imposed descent" (Oxford Computing Laboratory TR 08/09, June 2008) and "A second derivative SQP method: theoretical issues" (2008/10) both appeared alongside the journal paper "A Second Derivative SQP Method: Global Convergence" (*SIOPT* 2010, DOI 10.1137/080744542). Likewise "...: local convergence" (NA 08/21) became "...: Local Convergence and Practical Issues" (*SIOPT* 2010).
- "Subspace accelerated matrix splitting algorithms for bound-constrained quadratic programming and linear complementarity problems" (Northwestern IEMS Report 07-11, 2011) became "Subspace Accelerated Matrix Splitting Algorithms for Asymmetric and Symmetric Linear Complementarity Problems" (Robinson, Feng, Nocedal, Pang, *SIOPT* 2013, DOI 10.1137/110845094). [inferred same work: identical authors] The BQP half dropped out of the title.
- "A Shifted Primal-Dual Interior Method for Nonlinear Optimization" (UCSD CCoM-18-1) became "A Shifted Primal-Dual Penalty-Barrier Method..." (Gill, Kungurtsev, Robinson, *SIOPT* 2020, DOI 10.1137/19M1247425) [inferred same work].
- "A Proximal-Gradient Method for Constrained Optimization" (Optimization Online 2024/04; the file is named `reg_stoch_constrained_paper.pdf`) became "...for Equality Constrained Optimization" (*SIOPT* 2025). [inferred] The scope was narrowed to match what was proved.
- In arXiv:2304.14907 the v1 abstract says the method "can outperform a projected-(stochastic)-gradient method". v3 says it "can outperform projection-based methods". v3 also adds a sentence justifying the deterministic study ("since our experiments show that our algorithm can be competitive with a state-of-the-art projected gradient method in practice--we provide a complete investigation of this setting as well").

---

## 7. Research organization: who writes the code, and what happens to it

**7.1 Postdoc era (2007-2011): his algorithms became Fortran packages inside Gould's GALAHAD, with mixed fates.** [practice, P]
- **Released and maintained**: TRS and RQS (GALAHAD doc: "\galdate October 2008" and "November 2008"; "\galorigin N. I. M. Gould, H. S. Thorne, Rutherford Appleton Laboratory, and D. P. Robinson, Oxford University"); CQP ("\galdate November 2010. \galorigin N. I. M. Gould and D. P. Robinson, Rutherford Appleton Laboratory."); DQP (August 2012; origin "N. I. M. Gould", with the Gould & Robinson COAP 2017 paper as its reference).
- **Abandoned**: S2QP. In 2008 the local-convergence report announced "our evolving and (soon to be) freely available Fortran 95 GALAHAD [18] package S2QP". Today `src/oblivion/s2qp/s2qp.F90` (11,799 lines) carries the header "! Author: Daniel Robinson". The folder's README, signed "Nick Gould (for the GALAHAD team) October 2016", reads: "This is a repository for protoype GALAHAD packages that, honestly, didn't make the grade, or which we ran out of energy, effort or patience to finish. [...] We have cast them into oblivion as a warning to others." [observed, P] The source holds nine inline notes initialled "DPR", e.g. "DPR: fix later.", "DPR: remove later", "DPR: is this okay?", "DPR: What to do with this?" [practice, P].
- **Stalled for over a decade**: FiSQP in `src/forthcoming` ("A collection of packages that *may* appear in GALAHAD."). Header: "Principal authors: Nick Gould, Yueling Loh and Daniel P. Robinson", "originally written in Matlab by Yueling Loh and Daniel P. Robinson", "initial Fortran translation, GALAHAD Version 2.6, November 23th 2014". One inline comment reads "(dpr: below was done in shoddy way. made simple)". `forthcoming/trace/trace.F90` (Gould; "originally released GALAHAD Version 2.6. October 23rd 2014") implements TRACE and names Curtis, Robinson and Samadi in its banner. It is dated within days of the TRACE preprint (Optimization Online 2014/10/4609).
- [inferred] The pipeline is Matlab prototype (Robinson, a student) → Fortran (Gould). The Fortran half depends on Gould's time. The two prototypes not translated by Gould himself (S2QP) or not finished (FiSQP, TRACE) never became released packages.

**7.2 JHU era (2011-2019): a student writes the C library and he hosts it.** [practice, P]
- `daniel-p-robinson/FaRSA-L1-C`: the "Initial upload of files." commit by Robinson (2017-05-05) contains a compiled `farsa.o` and a README copied from the student's private repository. Its links point to `tianyic/FaRSA_private` and it keeps the placeholder "wget someurl.FaRSA.zip". The v2.0 update (2018-05-24, three commits by Tianyi Chen) matches the OMS 2018 paper. README v2.0 labels the status of each objective: "0  generic loss (in test)", "1  logistic loss (well tested)", "2  least square  (in test)".
- [inferred] Robinson shipped code at paper time, at student quality and with student-written documentation. No commits after May 2018.

**7.3 Lehigh era (2019-): Curtis writes the shared Matlab or C++ frameworks; Robinson rarely commits.** [practice, P]
- `frankecurtis/StochasticSQP` (2020-07-31 to 2021-07-23): AUTHORS "The main author of StochasticSQP is: Frank E. Curtis". Contributors: Berahas and Zhou. 15+3 commits by Curtis, one each by Berahas and Zhou, **none by Robinson**. The README still lists him among the "main authors".
- `frankecurtis/TRACE` (2022): README "This software is under development. Please check back later." Its AUTHORS file opens with "The main author of StochasticSQP is:", left over from the template (also noted in Curtis's 03 file), and lists Robinson as a contributor. No Robinson commits.
- `daniel-p-robinson/FaRSA` (C++, created 2020-07-30, the day after arXiv:2007.14951 was posted): the only Robinson commit is "Initial commit". Curtis made 8 commits, the last on 2021-07-20 ("Preliminary implementation of matrices."). README: "This software is under development. Please check back later." and "FaRSA is written in C++ and is released under the ??? License." The only direction option in `exes/farsa.opt` is `direction_computation ProximalGradient`. The reduced-space (subspace) step that defines FaRSA is not in the code (`src/` has only `FaRSADirectionComputationProximalGradient`).
- The homepage software page (fetched 2026-10-16, https://coral.ise.lehigh.edu/danielprobinson/software/) reads in full: "Software Coming soon: PYPDAS Galahad Farsa 2PHASE ncBQP" [practice, P].
- [inferred] Since about 2020 Robinson's software contribution shows in design, papers and documentation (PaperStarter, the course code), not in solver repositories. Repository commits may miss work done off-GitHub, so this is a lower bound on his coding.

**7.4 A published code link now resolves to different code.** [practice, P; mechanism inferred]
- FaRSA OMS 2018 §4.1: "Our implementation may be obtained from our Github repository https://github.com/daniel-p-robinson/FaRSA." The README of the C code (v2.0, 2018) also says "git clone https://github.com/daniel-p-robinson/FaRSA". Today that URL serves the 2020 C++ rewrite, which is unfinished and implements only the proximal-gradient direction. The C code that the paper describes sits under `FaRSA-L1-C` (created 2017-05-05).
- [inferred] The 2017 repository was renamed and its old name reused, which breaks GitHub's redirect. A reader who follows the paper's link does not get the paper's solver.

---

## 8. How criticism is answered (ML venues with public reviews)

| Paper | Lead | What reviewers said | What the authors did | Tag |
|---|---|---|---|---|
| Zhu, Wang, Robinson, Naiman, Vidal, Tsakiris, "Dual Principal Component Pursuit: Improved Analysis and Efficient Algorithms", NeurIPS 2018 (papers.nips.cc, paper ID 1105) | Zhu (postdoc) | R1: "it is necessary that the paper provides comparison with more compelling baselines and state of the art other than RANSAC". R3: "In figure 3, the proposed algorithm seems to take more time and iterations compared to ALP. This does not support the argument made earlier about computation efficiency." | Author feedback is not published for 2018. R3 wrote: "The rebuttal addressed a few minor confusions I had." | [observed] P |
| Zhu, Ding, Robinson, Tsakiris, Vidal, "A Linearly Convergent Method for Non-Smooth Non-Convex Optimization on the Grassmannian with Applications to Robust Subspace and Dictionary Learning", NeurIPS 2019 | Zhu | R3: (4) may not be the Riemannian subdifferential, and the condition is not intrinsic | Conceded: "The reviewer is correct that for a general nonsmooth function, the current (4) may not be the Riemannian subdifferential." Promised: "We will rename our definition as Extrinsic RRC to avoid confusion." **Final paper**: the Clarke-subdifferential definition was added, as promised. The name stayed "Riemannian Regularity Condition (RRC)", with a footnote instead: "Strictly speaking, Definition 1 is extrinsic since we view the Grassmannian as embedded in the Euclidean space". They also pointed reviewers to results already in the supplement ("We do have a deterministic and a statistical analysis for the spectral initialization in the supplementary material") | [practice] P |
| França, Sulam, Robinson, Vidal, "Conformal Symplectic and Relativistic Optimization", NeurIPS 2020 | França (postdoc) | missing related work; vague numerics; questions on relevance to optimization; extra hyperparameters | Pushback: "We are quite aware of this paper and reiterate: our paper is original and the first with such an approach."; "His/her understanding is very accurate, so we are surprised by his/her confidence score." Concession: ""RGD never diverges." This was a misleading "abuse of language" on our part and will be corrected." New ML experiments added in the response, a promise "we will make our code publicly available", and hardware disclosed ("We used Python 3 on a Mac Book Pro, Quad-Core Intel i5, 16 GB RAM") | [practice] P |
| Dai, Chen, Wang, Robinson, TMLR 2023 (OpenReview KBhSyBBeeO); Shinde, Ding, Robinson, Vidal, NeurIPS 2024 (OpenReview nBQHTBVnfr) | Dai; Shinde | **not read** (OpenReview challenge) | — | gap |

- [inferred] The responses differ in tone with the lead author: a conceding, follow-up style with Zhu, a combative one with França. Nothing here isolates Robinson's own voice. His sole-authored *TOP* 2015 discussion (DOI 10.1007/s11750-015-0371-2; read by agent 02, not re-read here) remains the only first-person record of how he argues with other researchers.
- In optimization journals, the referee exchange shows only indirectly, through version changes: MP 2019 v1 → v3 (test set 26 → 97 problems; Python → Matlab; fully connected → convolutional network on the full MNIST; added modified-Newton s_k and cost discussion); arXiv:1912.04365 v1 → v3 (41 → 109 test problems, CUTEst "downloaded July 1, 2020", a new "Practical considerations" section, a "(no reg.)" twin for every variant); arXiv:2106.13015 v1 → v2 (report 21T-013 → "21T-013-R1", 31 → 42 pages); arXiv:2304.14907 v1 → v3 (an extra baseline mentioned but not shown, a reframed abstract). [practice, P; triggers inferred]

---

## 9. Failures, abandoned directions, corrections (summary)

| # | Item | Evidence | Tag |
|---|---|---|---|
| F1 | S2QP: announced as "(soon to be) freely available" in 2008; now in GALAHAD "oblivion" as a prototype that "didn't make the grade" or that the team "ran out of energy, effort or patience to finish". Promised extensive CUTEr tests: none found | NA 08/21 §6; `src/oblivion/README`; `s2qp.F90` | [practice]/[observed] P |
| F2 | FiSQP (filter SQP) and TRACE Fortran ports: in GALAHAD "forthcoming" since Nov / Oct 2014 | `fisqp.F90`, `trace.F90` headers | [practice] P |
| F3 | FaRSA C++ rewrite (2020-21): license "???", only the proximal-gradient direction, inactive since 2021-07-20. FaRSA-Group Python code only "available upon request" | GitHub; arXiv:2007.14951 §5.1 | [practice] P |
| F4 | Homepage "Coming soon: PYPDAS Galahad Farsa 2PHASE ncBQP". [inferred] PYPDAS ↔ PDAS (COAP 2015), ncBQP ↔ SIOPT 2015, 2PHASE ↔ probably the two-phase LCP/BQP line (SIOPT 2013). None of them is released on that page | homepage fetched 2026-10-16 | [practice] P |
| F5 | The FaRSA link published in OMS 2018 now serves a different, unfinished codebase | OMS 2018 §4.1; GitHub creation dates | [practice] P; mechanism [inferred] |
| F6 | Corrigenda: TRACE Lemma 3.19 (a bound not as tight as it could be); stochastic SQP Corollary 3.14(a) | Curtis errata PDFs | [practice] P |
| F7 | Negative results kept in the paper: DQP as a cross-over stage after CQP; PDAS cycling counterexample; failure counts per variant (DQP 12 vs 25) | DQP preprint §5-6; COAP 2015 §3 | [practice] P |
| F8 | A promise made in rebuttal and kept only in part (the RRC was not renamed; a footnote was added instead) | NeurIPS 2019 feedback vs final PDF | [practice] P |
| F9 | Reports whose journal versions I could not match under the same title: Dai & Robinson, "Inexact Proximal-Gradient Methods with Support Identification" (Optimization Online 2022/11). [inferred] Possibly absorbed into Dai & Robinson, *Optim. Methods Softw.* 2024, DOI 10.1080/10556788.2024.2346643 (Crossref top hit). Gill & Robinson, "Regularized sequential quadratic programming methods" (UCSD NA-11-02). Gill, Kungurtsev, Robinson, "A Regularized SQP Method with Convergence to Second-Order Optimal Points" (CCoM-13-4). The matches are unverified | Optimization Online; Crossref | [practice] P; matches [inferred] |
| F10 | A long-promised "matrix-free ... extreme-scale" trust funnel (talk title, 2014, per note 06) appeared in 2017 with no experiments | MP 2017 author PDF | [practice] P |

---

## 10. Era and resource context of the practices

| Era | Seniority and team | Tools and compute | Practices first seen |
|---|---|---|---|
| 2007-2011, Oxford/RAL and Northwestern postdoc | junior, with senior hosts (Gould; Nocedal, Pang) | Fortran 95 inside GALAHAD; CUTEr; Hock-Schittkowski; HSL; Matlab for LCP/BQP | small-dense-first testing (4.3); production code via Gould (7.1); in-house twin comparator (LCP 2013: own two-phase projected-gradient code) |
| 2011-2019, JHU assistant professor | first PhD students (Mohy-ud-Din, Jiang, Chen), co-PI with Vidal; Curtis as main optimization collaborator | Matlab prototypes; bqpd, Cplex as QP solvers; Lancelot modifications; C library written by a student; Python 2.7/TensorFlow for NN tests; workstation scale (16 GB) | twin baselines (B1); unmodified external codes (B2); two-step publication (B7); NeurIPS-style rebuttals with Vidal-group postdocs (§8) |
| 2019-, Lehigh (associate professor, later professor) | shared OptML group with Curtis; students Dai, Qu, Guo, Wang, Zhou | Curtis-written Matlab frameworks (StochasticSQP, TRACE); Python with PyCUTEst; Gurobi subproblems; COR@L cluster and Lehigh HPC; GitHub for group tooling (PaperStarter) | noise-injected CUTEst protocol; per-instance tuned baselines with disclosed budgets; group-wide paper template (6.1) |

---

## Contradictions (kept, not reconciled)

- **C1 Stated "free software" vs practice.** Note 02 (R8) records three statements that his algorithms should be freely available (2009, 2012, the homepage). Against them: S2QP ended in GALAHAD "oblivion"; FiSQP and TRACE-Fortran have sat in "forthcoming" since 2014; the C++ FaRSA has an unfilled license and is incomplete; FaRSA-Group is "available upon request"; the homepage list has said "Coming soon" since at least 2020 (note 02). For the statement: TRS, RQS, CQP and DQP are released GALAHAD packages carrying his name in docs or references, FaRSA C v2.0 is public, and StochasticSQP is public (written by Curtis).
- **C2 Stated R4 (gains must be shown computationally, note 02) vs theory-only flagship papers.** The interior-point trust funnel (MP 2017), TRACE (MP 2017) and regional complexity (MP 2021) contain no experiments. Regional complexity nonetheless rests on the claim that adaptive methods "often perform better in practice" (quoted in note 02).
- **C3 Stated R3 (no assumptions that a solver cannot guarantee, note 02) vs TRACE's assumptions.** TRACE's conclusion assumes "exact first- and second-order derivative information" and "a globally optimal solution of a trust region subproblem". Trust-region subproblems can be solved globally, so this is a tension rather than a direct contradiction. The paper calls relaxing it "the subject of current research".
- **C4 Different budget conventions for baselines.** In 2020 the competitor got 110 times the iterations plus per-instance tuning. In the 2024 proximal-gradient preprint the competitor (Bazinga) got *fewer* iterations, on cost-per-iteration grounds. In 2017 the competitor's code was left untouched even where it failed, while in 2010 dgqt was "slightly modified" to record details. Each choice is disclosed. They follow no single rule.
- **C5 Test-set selection conditioned on the method's own behaviour** (MP 2019 v1: kept only problems where negative curvature was used; the v3 plots are still restricted that way; 2020: LICQ must hold "in all runs of all algorithms") sits beside the claim of general benefit. The papers state the filters openly.
- **C6 Sibling notes disagree.** Note 06 §6 says "The homepage has **no software page** today". Note 02 and my fetch on 2026-10-16 both find `/danielprobinson/software/` live, with the "Coming soon" list.
- **C7 Author-name variants for the MPC 2010 paper.** The preprint (RAL-TR-2009-003) and the GALAHAD references say "H. Sue Dollar / H. S. Dollar, N. I. M. Gould and D. P. Robinson". Crossref and DBLP list "Gould, Robinson, Thorne". The GALAHAD `\galorigin` lines say "H. S. Thorne". [inferred] These are two surnames of one co-author, and the author order differs between the preprint and the journal.
- **C8 Repository authorship vs README authorship.** StochasticSQP and the C++ FaRSA call Robinson a "main author". Their commit histories show none (StochasticSQP) or only the empty initial commit (FaRSA). AUTHORS files name Curtis as main author (StochasticSQP) or list both (FaRSA).
- Audit 2026-10-17: the §5.1 PDAS cycling example is a counterexample to the incumbent Hintermüller–Ito–Kunisch update (with U0 = ∅ the framework "is identical to the algorithm in [25, Sect. 2]"), not to CHR15's new updates, which converge on it (CHR15 §3.1 and Table 2; Curtis corpus txt S024).

## Gaps

- **OpenReview reviews and responses** (TMLR 2023, NeurIPS 2024): blocked by a browser challenge, not read. ICML, CVPR, ICCV, AISTATS reviews are not public.
- **Optimization-journal referee reports and responses**: none public. Changes between versions are the only trace (§8).
- **Full texts not read**: ncBQP (SIOPT 2015; abstract only); the PDAL journal version (COAP 2012; the 2008 report I read has no numerical section, and note 02 cites numerics on COAP pp. 4 and 16); the stabilized-SQP papers with Gill and Kungurtsev (beyond report headers); the shifted penalty-barrier paper (report downloaded, not read); the IJCAI/healthcare and power-systems papers; the CVPR/ICCV subspace-clustering papers and their code.
- **Code of the subspace-clustering line** (SSC-OMP, EnSC, exemplar selection, DPCP): GitHub search found repositories by the student leads (e.g. `tding1/Noisy-DPCP`, `tding1/DPCP-UoH`, `tianjiaoding/DPCP-Homography`). I did not open them. Robinson's role in them is unknown.
- **The original S2QP and FiSQP Matlab prototypes**: not public. The GALAHAD git history starts long after 2016, so when S2QP moved to "oblivion" (on or before Oct 2016) is unknown.
- **How ideas arose** (layer 3): no notebooks, talk transcripts, or interviews found. No talk video exists to transcribe.
- **Rejected or withdrawn submissions**: none found. Venue changes noted in 06 (F7) stay unexplained.
- **Supervision practice** (how students are guided on code and experiments): only indirect traces (student-written FaRSA C code, student commits to the course repository). This is agent 04's remit.

## Sources

1. GitHub account `daniel-p-robinson` (API listing; 3 public repositories; created 2016-11-22), https://github.com/daniel-p-robinson (primary)
2. Repository `daniel-p-robinson/FaRSA` (C++, 2020-07-30 to 2021-07-20; README, AUTHORS, `FaRSAVersion.hpp`, `exes/farsa.opt`, git log), https://github.com/daniel-p-robinson/FaRSA (primary)
3. Repository `daniel-p-robinson/FaRSA-L1-C` (C, 2017-05-05 to 2018-05-24; README v1 and v2.0, `test/FaRSA_t.profile`, git log), https://github.com/daniel-p-robinson/FaRSA-L1-C (primary)
4. Repository `daniel-p-robinson/nonlinear-optimization-course` (MATLAB, ISE 417, 2021-02-09 to 2022-02-14; README, `newton.m`, `steepest_descent.m`, tests, git log), https://github.com/daniel-p-robinson/nonlinear-optimization-course (primary)
5. Repository `frankecurtis/StochasticSQP` (README, AUTHORS, git log 2020-07-31 to 2021-07-23), https://github.com/frankecurtis/StochasticSQP (primary)
6. Repository `frankecurtis/TRACE` (README, AUTHORS, git log 2022-05), https://github.com/frankecurtis/TRACE (primary)
7. Repository `frankecurtis/Utilities` (README, PaperStarter readme/src, `LaTeX/dpr_fec.sty`, git log 2020-10 to 2021-07), https://github.com/frankecurtis/Utilities (primary)
8. GALAHAD documentation `doc/src/trs.tex`, `rqs.tex`, `cqp.tex`, `dqp.tex` (master branch, read 2026-10-16), https://github.com/ralna/GALAHAD (primary)
9. GALAHAD `src/oblivion/README` (N. Gould, Oct 2016) and `src/oblivion/s2qp/s2qp.F90` ("Author: Daniel Robinson"), https://github.com/ralna/GALAHAD/tree/master/src/oblivion (primary)
10. GALAHAD `src/forthcoming/README.forthcoming`, `fisqp/fisqp.F90`, `trace/trace.F90`, https://github.com/ralna/GALAHAD/tree/master/src/forthcoming (primary)
11. Robinson homepage and Software page, fetched 2026-10-16, https://coral.ise.lehigh.edu/danielprobinson/ and https://coral.ise.lehigh.edu/danielprobinson/software/ (primary)
12. Curtis, publications page (author-hosted PDFs), https://coral.ise.lehigh.edu/frankecurtis/publications/ (primary)
13. Optimization Online search results for "Daniel P. Robinson" (pages 1-5), https://optimization-online.org/?s=Daniel+P.+Robinson (secondary listing; the linked preprints are primary)
14. N. I. M. Gould, D. P. Robinson, "A second derivative SQP method: local convergence", Oxford NA Report 08/21, Optimization Online 2008/12/2192; *SIAM J. Optim.* 20(4):2049-2079, 2010, DOI 10.1137/080744554 (§5-6 read) (primary)
15. N. I. M. Gould, D. P. Robinson, "A second derivative SQP method with imposed descent", Oxford Computing Laboratory TR 08/09, 2008, Optimization Online 2008/06/2009; and "...: theoretical issues", Optimization Online 2008/10/2130; *SIAM J. Optim.* 20(4):2023-2048, 2010, DOI 10.1137/080744542 (metadata only) (primary)
16. H. S. Dollar, N. I. M. Gould, D. P. Robinson, "On solving trust-region and other regularised subproblems in optimization", RAL-TR-2009-003, Optimization Online 2009/02/2232; published as Gould, Robinson, Thorne, *Math. Program. Comput.* 2(1):21-57, 2010, DOI 10.1007/s12532-010-0011-7 (§4 read; Crossref authors) (primary)
17. P. E. Gill, D. P. Robinson, "A primal-dual augmented Lagrangian", UCSD NA-08-02, Optimization Online 2008/05/1964; *Comput. Optim. Appl.* 51:1-25, 2012, DOI 10.1007/s10589-010-9339-1 (report searched; no numerical section) (primary)
18. P. E. Gill, D. P. Robinson, "Regularized sequential quadratic programming methods", UCSD NA-11-02, 2011, Optimization Online 2011/10/3222 (header only) (primary)
19. P. E. Gill, V. Kungurtsev, D. P. Robinson, "A regularized SQP method with convergence to second-order optimal points", UCSD CCoM-13-4, 2013, Optimization Online 2013/10/4102 (header only) (primary)
20. P. E. Gill, V. Kungurtsev, D. P. Robinson, "A shifted primal-dual interior method for nonlinear optimization", UCSD CCoM-18-1, Optimization Online 2018/01/6444; *SIAM J. Optim.* 2020, DOI 10.1137/19M1247425 (title only) (primary)
21. N. I. M. Gould, D. Orban, D. P. Robinson, "Trajectory-following methods for large-scale degenerate convex quadratic programming", Optimization Online 2011/09/3147; *Math. Program. Comput.* 5(2):113-142, 2013, DOI 10.1007/s12532-012-0050-3 (§6 read) (primary)
22. D. P. Robinson, L. Feng, J. Nocedal, J.-S. Pang, "Subspace accelerated matrix splitting algorithms for bound-constrained quadratic programming and linear complementarity problems", Northwestern IEMS Report 07-11, Optimization Online 2011/09/3185; *SIAM J. Optim.* 2013, DOI 10.1137/110845094 (§2.3 read) (primary)
23. N. I. M. Gould, Y. Loh, D. P. Robinson, "A filter SQP method: local convergence and numerical results", RAL P-2014-012, Optimization Online 2014/12/4702; *SIAM J. Optim.* 25(3):1885-1911, 2015, DOI 10.1137/140996677 (§5 read) (primary)
24. N. I. M. Gould, D. P. Robinson, "A dual gradient-projection method for large-scale strictly convex quadratic problems", JHU OPT-2016/2b, Optimization Online 2016/02/5332; *Comput. Optim. Appl.* 67(1):1-38, 2017, DOI 10.1007/s10589-016-9886-1 (§5-6 read) (primary)
25. F. E. Curtis, H. Jiang, D. P. Robinson, "An adaptive augmented Lagrangian method for large-scale constrained optimization", *Math. Program.* 152:201-245, 2015, DOI 10.1007/s10107-014-0784-y (author PDF, §4 read) (primary)
26. F. E. Curtis, N. I. M. Gould, H. Jiang, D. P. Robinson, "Adaptive augmented Lagrangian methods: algorithms and practical numerical experience", *Optim. Methods Softw.* 31(1):157-186, 2016, DOI 10.1080/10556788.2015.1071813 (author PDF, §3-4 read) (primary)
27. F. E. Curtis, T. C. Johnson, D. P. Robinson, A. Wächter, "An inexact sequential quadratic optimization algorithm for nonlinear optimization", *SIAM J. Optim.*, 2014, DOI 10.1137/130918320 (author PDF, §4 read) (primary)
28. F. E. Curtis, Z. Han, D. P. Robinson, "A globally convergent primal-dual active-set framework for large-scale convex quadratic optimization", *Comput. Optim. Appl.*, 2015, DOI 10.1007/s10589-014-9681-9 (author PDF, §1, §3, §5 read) (primary)
29. F. E. Curtis, N. I. M. Gould, D. P. Robinson, Ph. L. Toint, "An interior-point trust-funnel algorithm for nonlinear optimization", *Math. Program.*, 2017, DOI 10.1007/s10107-016-1003-9 (author PDF; searched for experiments, conclusion read) (primary)
30. F. E. Curtis, D. P. Robinson, M. Samadi, "A trust region algorithm with a worst-case iteration complexity of O(ε^{-3/2}) for nonconvex optimization", *Math. Program.* 162:1-32, 2017, DOI 10.1007/s10107-016-1026-2 (author PDF; conclusion read) (primary)
31. Corrigendum to Curtis, Robinson, Samadi (2017), Lemma 3.19, http://coral.ise.lehigh.edu/frankecurtis/files/errata/CurtRobiSama17_corrigendum.pdf (primary)
32. Corrigendum to Berahas, Curtis, Robinson, Zhou (2021), Corollary 3.14(a), http://coral.ise.lehigh.edu/frankecurtis/files/errata/BeraCurtRobiZhou21_corrigendum.pdf (primary)
33. T. Chen, F. E. Curtis, D. P. Robinson, "A reduced-space algorithm for minimizing ℓ1-regularized convex functions", *SIAM J. Optim.* 27(3):1583-1610, 2017, DOI 10.1137/16M1062259 (author PDF, §4 read; Crossref abstract) (primary)
34. T. Chen, F. E. Curtis, D. P. Robinson, "FaRSA for ℓ1-regularized convex optimization: local convergence and numerical experience", *Optim. Methods Softw.* 33(2):396-415, 2018, DOI 10.1080/10556788.2017.1415336 (author PDF, §4-5 read) (primary)
35. F. E. Curtis, D. P. Robinson, "Exploiting negative curvature in deterministic and stochastic optimization", arXiv:1703.00412 v1 (2017-03-01) and v3 (2018-04-04); *Math. Program.* 176:69-94, 2019, DOI 10.1007/s10107-018-1335-8 (numerics of both versions read) (primary)
36. F. E. Curtis, D. P. Robinson, "Regional complexity analysis of algorithms for nonconvex smooth optimization", arXiv:1802.01062 v1, v2; *Math. Program.* 187:579-615, 2021, DOI 10.1007/s10107-020-01492-3 (structure compared) (primary)
37. F. E. Curtis, D. P. Robinson, C. W. Royer, S. J. Wright, "Trust-region Newton-CG with strong second-order complexity guarantees for nonconvex optimization", arXiv:1912.04365 v1 (2019-12-09), v3 (2020-11-19); *SIAM J. Optim.* 2021, DOI 10.1137/19M130563X (experiments of v1 and v3 read) (primary)
38. A. S. Berahas, F. E. Curtis, D. P. Robinson, B. Zhou, "Sequential quadratic optimization for nonlinear equality constrained stochastic optimization", arXiv:2007.10525 v1 (2020-07-20); *SIAM J. Optim.* 31(2):1352-1379, 2021, DOI 10.1137/20M1354556 (§4 read) (primary)
39. F. E. Curtis, Y. Dai, D. P. Robinson, "A subspace acceleration method for minimization involving a group sparsity-inducing regularizer", arXiv:2007.14951 v1 (2020-07-29); *SIAM J. Optim.* 2022, DOI 10.1137/21M1411111 (§5 read) (primary)
40. A. S. Berahas, F. E. Curtis, M. J. O'Neill, D. P. Robinson, "A stochastic sequential quadratic optimization algorithm for nonlinear equality constrained optimization with rank-deficient Jacobians", arXiv:2106.13015 v1 (2021-06-24), v2 (2023-03-16); *Math. Oper. Res.* 2024, DOI 10.1287/moor.2021.0154 (§5 of both read) (primary)
41. F. E. Curtis, D. P. Robinson, B. Zhou, "Inexact sequential quadratic optimization for minimizing a stochastic objective function subject to deterministic nonlinear equality constraints", arXiv:2107.03512 v1; published as "A stochastic inexact sequential quadratic optimization algorithm for nonlinear equality-constrained optimization", *INFORMS J. Optim.* 2024, DOI 10.1287/ijoo.2022.0008 (§4 opening read) (primary)
42. F. E. Curtis, D. P. Robinson, B. Zhou, "Sequential quadratic optimization for stochastic optimization with deterministic nonlinear inequality and equality constraints", arXiv:2302.14790 v1; *SIAM J. Optim.* 2024, DOI 10.1137/23M1556149 (§5 read) (primary)
43. F. E. Curtis, V. Kungurtsev, D. P. Robinson, Q. Wang, "A stochastic-gradient-based interior-point algorithm for solving smooth bound-constrained optimization problems", arXiv:2304.14907 v1, v3; *SIAM J. Optim.* 2025, DOI 10.1137/23M1569460 (abstracts and §5 of both read) (primary)
44. Y. Dai, X. Qu, D. P. Robinson, "A proximal-gradient method for constrained optimization", Optimization Online 2024/04; published as "A Proximal-Gradient Method for Equality Constrained Optimization", *SIAM J. Optim.* 35(4):2654-2683, 2025, DOI 10.1137/24M1653586 (§4 read) (primary)
45. Y. Dai, D. P. Robinson, "Inexact proximal-gradient methods with support identification", Optimization Online 2022/11 (abstract only) (primary)
46. NeurIPS 2018 reviews, Zhu, Wang, Robinson, Naiman, Vidal, Tsakiris, "Dual Principal Component Pursuit: Improved Analysis and Efficient Algorithms", https://papers.nips.cc/paper_files/paper/2018/file/af21d0c97db2e27e13572cbf59eb343d-Reviews.html (primary)
47. NeurIPS 2019 author feedback and final paper, Zhu, Ding, Robinson, Tsakiris, Vidal, "A Linearly Convergent Method for Non-Smooth Non-Convex Optimization on the Grassmannian with Applications to Robust Subspace and Dictionary Learning", https://papers.nips.cc/paper_files/paper/2019/hash/aac933717a429f57c6ca58f32975c597-Abstract.html (primary)
48. NeurIPS 2020 author feedback, França, Sulam, Robinson, Vidal, "Conformal Symplectic and Relativistic Optimization", https://papers.nips.cc/paper_files/paper/2020/hash/c4b108f53550f1d5967305a9a8140ddd-Abstract.html (primary)
49. OpenReview forums KBhSyBBeeO (TMLR 2023) and nBQHTBVnfr (NeurIPS 2024): titles and authors only, via the OpenReview search API; content blocked (primary metadata)
50. Crossref records: DOI 10.1137/15M1022100 (abstract), 10.1007/s12532-010-0011-7 (authors), 10.1007/s10589-010-9339-1, 10.1137/16M1062259; title query for the 2022 IPG report, https://api.crossref.org (secondary)
51. DBLP SPARQL listing for pid 20/8222 (85 records), https://sparql.dblp.org (secondary)
52. WebSearch summary (Mathematics Genealogy entry for H. Mohy-ud-Din, JHU 2014, advisor D. P. Robinson), not opened directly (secondary); and sibling notes 02-methodology.md and 06-trajectory.md, used as leads only (secondary)
