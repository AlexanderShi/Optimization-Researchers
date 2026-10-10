# Ruth Misener · 03 Process evidence (what she actually does)

| Field | Value |
|---|---|
| Researcher | Ruth Misener (Imperial College London, Department of Computing; PhD Princeton 2012 with Christodoulos A. Floudas) |
| Dimension | Research agent 03 of 06: process evidence. Behaviour traces in code, experiment sections, review threads, version histories, grant records and abandoned work |
| Research date | 2026-10-10 |
| Sources consulted | 36 (28 primary, 8 secondary). List at the end |
| WebSearch calls used | 2 |
| Local corpus | `references/sources/{papers,talks,essays,software}` held no user-supplied files (only `.gitkeep`), so no finding here is "from user-supplied material". Nothing under `private/` was opened |

## How to read this note

- Tags: **[stated]** what she or her co-authors say about their own way of working; **[practice]** what the papers, code, records and version histories show they did; **[observed]** what others (reviewers, curators, institutions) recorded; **[inferred]** my reading of the evidence, never a fact. **P** = primary source, **S** = secondary.
- Attribution: almost every paper is multi-author. "The group" means the authors of the cited paper, with Misener among them. A behaviour is attributed to Misener personally only where the trace is her own (her GitHub account `rmisener`, her grant record). Princeton-era papers are two-author papers with her doctoral adviser, so their conventions may be Floudas-group conventions as much as hers [inferred].
- Quotes are verbatim from the cited text (original typos kept, marked [sic]); page numbers refer to the PDF pages of the accepted manuscript or preprint that was read.

## Era and resource map (context for every practice below)

| Code | Period and role | Tools and compute seen in the papers | Team | Funding named in the sources |
|---|---|---|---|---|
| E1 | 2008-2013, Princeton PhD and the first solver papers (Floudas group) | C++ library linked to GAMS through the GAMS Modeling Object interface; CPLEX 11.1/12.4, SNOPT 5.3, LAPACK; one Intel Core 2 Quad 2.83 GHz workstation, 4 GB RAM (GloMIQO S4 p.18-19; MIQCQP S6 §4.1) | two-author papers (Misener, Floudas) | NSF Graduate Research Fellowship; NSF CBET-0827907 (S4, S6) |
| E2 | 2013-2017, Imperial; Royal Academy of Engineering Research Fellow (S5 p.1), later Lecturer (S32, undated) | ANTIGONE runs on an Intel Xeon X5650 2.67 GHz, 24 GB RAM, GAMS 24.2.1 (S5 p.10) | small; first PhD students | Royal Academy of Engineering Research Fellowship (S5 p.1) |
| E3 | 2017-2022, EPSRC Early Career Fellowship EP/P016871/1 "GALINI" (GBP 984,062, Aug 2017 to Aug 2022; S30); Senior Lecturer by 2020 (S33) | Python, Pyomo, open-source licences, GitHub; AWS C5 batch runs (S12 p.10); desktop and laptop CPUs (S10 p.16, S11 p.16) | fellowship-funded developer (Ceccon; job title not verified), Newton fellow (Kronqvist), Imperial Research Fellow (Tsay), PhD students | EP/P016871/1; Newton International Fellowship; Imperial College Research Fellowship (S30) |
| E4 | 2019-2026, data-driven optimisation with industry; BASF/RAEng Research Chair in Data-Driven Optimisation 2022-2027 (S30) | Gurobi 9.x+ under academic licence, PyTorch, GitHub Actions CI, NeurIPS/ICLR with OpenReview (S15, S26, S29) | 4-12-author papers; several with Sandia co-developers or BASF-supported authors (S26, S28; individual affiliations not verified) | BASF studentships and grants, EPSRC ADOPT EP/W003317/1 (2022-2026), EPSRC EP/T001577/1 (S30) |

---

## Layer 4 · Experiment and execution

### 4.1 Building and curating test sets

**PE-01 [practice, P] Assemble the largest test suite available, document its provenance, and state the exclusion rule.** ANTIGONE was tested on 2571 problems drawn from eight standard libraries (AMPL Book, Bonmin, GLOBALLib, LINLib, MacMOOPLib, MPLLib, MINLPLib, PrincetonLib), a collection compiled from minlp.org, and MIQCQP classes from the open literature (S5 Table 2, p.9). The paper states the exclusion rule (instances with functional forms ANTIGONE cannot handle, e.g. trigonometric, min/max, errorf, or with unbounded objectives; S5 p.8-9) and freezes the library snapshot: "The standard libraries are dynamic entities; we are using the latest versions as of 11 March 2013." (S5 p.10). The supplement gives, for each library, the access date and URL (e.g. "Table 9: 34 AMPL Book Library Case Studies; Accessed 11 March 2013 at http://www.gamsworld.org/performance/amplbook/amplbooklib.zip"; S5 supplement p.1). Era E1/E2.

**PE-02 [practice, P] When a community test set is unusable, rebuild it rather than skip it.** On the minlp.org library: "this is unfortunately unusable as a test set for solver comparisons" because modeling files contain several problems or need user arguments; the authors "compiled a collection of problems from the minlp.org MINLP Library" (115 problems) and singled it out: "The minlp.org test set is unusually difficult; all 115 problems are less than 5 years old and industrially relevant." (S5 p.10). Era E2.

**PE-03 [practice, P] Collect application models from other groups.** GloMIQO's 399-problem suite mixes process networks, computational geometry and library instances (S4 Table 2, p.20); the acknowledgements thank named colleagues "for giving us their modeling files" (S4 p.27). Era E1.

**PE-04 [practice, P] In the Imperial era, reuse other groups' instance generators and code them into the group's own library.** The pooling study uses classic small instances (Tawarmalani and Sahinidis 2002), sparse instances generated from the Haverly instances (Luedtke et al. 2020) and large dense instances (Dey and Gupte 2015), all built by functions in `pooling_network.instances` (S11 p.17). Era E3.

**PE-05 [practice, P; observed, S] Give instances back to the community, including instances designed to be hard for a specific solver class.**
- `points_in_circles` (Kronqvist and Misener): convex MINLP instances in big-M and convex-hull form; the README says they "are designed to be challenging both due to the nonlinearity and the combinatorial aspects" and are hard for "polyhedral outer approximation-based solvers" (S29). MINLPLib lists 26 `p_ball_*` instances "contributed by Jan Kronqvist and Ruth Misener", added 26 Aug 2020, with the curators changing the perspective-formulation epsilon to 1e-4 [observed] (S31).
- Heat-recovery networks: the award record says "we have collected and made publicly available this test set for the first time. Now researchers will have access to all 51 problems in the open literature." (S30); the repository ships the instances, the code and the results obtained, with the machine stated (Intel Core i7-4790, 15.6 GB RAM, Ubuntu 14.04, Python 2.7.6, Pyomo 4.4.1) (S29, `min_matches_heuristics`).
- A public "concrete" gradient-boosted-tree instance on Zenodo next to the confidential industrial one: "This test instance gives researchers a chance to try our algorithmic approaches." (S30).
- Co-author of QPLIB, whose filter defines "interesting" as "challenging for a significant set of solution methods" (S13 p.2) and drops every instance "solved by at least 30% of the complete solvers within a time limit of 30 seconds" (S13 p.15). Misener's individual role in QPLIB is not documented. Era E3.

**PE-06 [practice, P] Calibrate instance difficulty against the baseline.** NeurIPS 2021: "Perturbations ε1 were selected such that some big-M problems were solvable within 3600s" (S15 v2 p.7); the first 100 test images with randomly chosen adversarial labels, the same 100 for every model on a dataset (S15 v2 §4.1). Era E4.

### 4.2 Choosing baselines and keeping comparisons fair

**PE-07 [practice, P] Compare against every available global solver, at its strongest version, and say that the competitors are moving targets.** GloMIQO was compared with BARON 10.1.2, Couenne 0.4, LindoGLOBAL 6.1.1.588 and SCIP 2.1.0. The BARON version was newer than the commercial release ("Version made available to us 09 January 2012; the latest commercial release is BARON 9.3.1", S4 Table 1, p.19). "Linus Schrage of LINDO Systems has generously given us a particularly high-performing version of LindoGLOBAL 6.1.1.588", which "allows us to access an undocumented quadratic mode option" (S4 p.18). And: "It is very important for the reader to note that all of the excellent solvers that we compare to GloMIQO are subject to active development and under continual improvement." (S4 p.18). ANTIGONE repeated the pattern with BARON 12.7.3, Couenne 0.4, LINDO 8.0 and SCIP 3.0, "the latest versions as of February 2014" (S5 p.10). Era E1/E2.

**PE-08 [practice, P] Harmonise tolerances, otherwise leave defaults, and run solvers back-to-back.** GloMIQO set the feasibility tolerance to 10^-6 for every solver, noting that the defaults differ (10^-5 in BARON, 10^-7 in LindoGLOBAL; S4 p.19). ANTIGONE: "No other parameters were altered from default." and "each of the 5 solvers addressed a test problem successively so as minimize [sic] the effect of fluctuating machine load", following Dolan and Moré (S5 p.10). NeurIPS 2021: Gurobi `MIPFocus = 3` "to ensure consistent solution approaches across formulations" (S15 v2 p.16). Era E1, E2, E4.

**PE-09 [practice, P] Give competitors the benefit of the doubt in post-processing.** When SCIP ran out of memory, the authors parsed the GAMS logs to record its gap at failure; when BARON bounded a problem without a feasible point, "we record the best known bounds on the solution rather than penalizing the solver with dashes" (S4 p.20). Era E1.

**PE-10 [practice, P] Strengthen the baseline with the authors' own components, and separate idea value from overhead with "oracle" runs.** In the 2021 pooling study Gurobi 9.1 is run in six configurations: default, cuts disabled, with the authors' pooling cuts, the same cuts as an oracle ("This test assumes Gurobi had access to an oracle providing a list of valid cuts."), warm-started from the authors' MIP restriction, and the warm start as an oracle (S11 p.17-18). Era E3.

**PE-11 [practice, P; observed, P] Tune the closest competitor's parameter before comparing.** In NeurIPS 2021 the cuts of Anderson et al. were compared at their best cut frequency; a reviewer described the result as "a slight improvement over an implementation of the cuts from Anderson et al. with optimally tuned cut frequency" [observed] (S16, Reviewer Nod7). Era E4.

**PE-12 [practice, P] Use your own earlier solver as a baseline for the new one.** The 2021 GALINI preprint benchmarks against ANTIGONE, BARON, Couenne and SCIP from GAMS 31.1 and a Gurobi 9.1 beta "downloaded on 2020-10-08" (S10 p.16). Era E3.

### 4.3 Checking that results are correct (verification and debugging)

**PE-13 [practice, P] Verify every returned solution independently, and classify failures.** "After solving each of the 2571 test cases using GAMS, a Perl script asserted the feasibility of the solution returned by each solver. Instances where solvers returned infeasible points were automatically relabeled as failures (fl)." (S5 p.10). GloMIQO separates a "benign failure" (no solution returned) from "a troublesome failure (the solver gave an incorrect answer or violated a constraint)" (S4 p.19). ANTIGONE also drops untrustworthy bounds: "Only deterministic lower bounds LB are reported; lower bounds based on guessed variable bounds are discarded." (S5 p.11). Era E1/E2.

**PE-14 [practice, P] Check results against an external record.** Point-packing results were "checked the correctness our [sic] computational results" against packomania.com (S6 p.16). Era E1.

**PE-15 [practice, P] Validate a structure detector against library labels used as an oracle, and list every miss.** SUSPECT was run on all 1527 MINLPLib 2 problems (accessed 13 December 2017) as an AWS batch job; "To increase reproducibility, the SUSPECT command line tool was packaged as a Docker image running Python 3.5." (S12 p.10). The results matched MINLPLib's labels in 1275 of 1392 processed instances, the misses are listed by instance with causes (eigenvalue numerics, square roots of products), and the paper stresses: "SUSPECT does not have false positives on the test set, this gives confidence in the implementation and makes it possible to use it for solver selection." (S12 p.11). Era E3.

**PE-16 [practice, P] Build debugging into the solver itself.** GALINI: "GALINI users can enable Paranoid Mode, when this flag is active the solver will perform extra checks to verify the correctness of every step." A failed check drops the developer into a Python console inside the failing function; tensors are logged to HDF5, every branch-and-bound operation is logged, and a dashboard shows bound evolution, the tree and a time line (S10 p.15; repository `galini-dashboard`, S25). Era E3 (code written by Ceccon, S27).

**PE-17 [practice, P] Continuous integration, executed notebooks and coverage as standing checks.** OMLT's CI runs ruff, ruff format, mypy and pytest on Python 3.9-3.12, and `tests/notebooks/test_run_notebooks.py` executes the documentation notebooks (S26). Misener merged the pull request that added notebook tests (PR #30, 2022-01-20) and opened issues when coverage fell (see PE-42). Era E4.

### 4.4 Ablations: how components are isolated

**PE-18 [practice, P] Cumulative component ablation inside the full branch-and-bound.** In the MIQCQP paper each of 37 test problems was run four times: McCormick only; plus edge-concave facets; plus piecewise-linear (linear partitioning, N = 4); plus piecewise-linear (logarithmic partitioning, N = 4). N = 2 and 8 were run and plotted but not tabulated "because they are fairly similar to N = 4" (S6 p.16-17). The metrics include root-node gap closed and nodes explored with standard-deviation error bars (S6 Table 2, Fig. 3). The authors chose the in-context design on purpose: "This holistic view makes the comparisons fairly subtle but also allows us to draw better-informed conclusions." (S6 p.17). Era E1.

**PE-19 [practice, P] All combinations of component classes.** GALINI was run with triangle, outer-approximation and SDP cuts individually, in every pair and all three together, on MINLPLib 2 and QPLIB (S10 p.16-17). Era E3.

**PE-20 [practice, P; observed, P] Ablate the formulation parameter and the companion technique together.** NeurIPS 2021 varies the number of partitions, the partitioning strategy and OBBT on/off (S15). A reviewer wrote: "Many ablation studies are provided to see at which point in this trade-off one is able to obtain best computation times and comparison with recent work seems thorough." [observed] (S16, Reviewer cKru, confidence 1 of 5). Era E4.

### 4.5 Reporting conventions

**PE-21 [practice, P] Two performance profiles every time: time to solve, and gap remaining at the time limit.** Seen in the MIQCQP paper (S6 Fig. 1-2), GloMIQO (S4 §4.2), ANTIGONE (S5 Figs. 3-16, panels (a) and (b)), GALINI (S10 Figs. 6-8) and the pooling paper (S11 Figs. 6-10). ANTIGONE explains why the gap panel matters: it is "useful for contexts where globally optimizing a problem is beyond the reach of current technology but there is still a need to understand bounds on the global solution" (S5 p.11). Era E1-E3.

**PE-22 [practice, P] One instance table per class that explains the mechanism.** ANTIGONE walks through the automatic reformulation of GLOBALLib `ex6_2_9` term by term, then reports competitors' behaviour on it ("BARON 12.7.3 mistakes ex6 2 9 for an unbounded problem", S5 p.14). GloMIQO does the same for `waste`, `ex5_2_5`, `congruent_c72` (S4 p.24-26). Era E1/E2.

**PE-23 [practice, P] Exact versions, access dates and hardware in every computational section.** Examples: S4 Table 1; S5 p.10; S10 p.16 (Python 3.8.5, CPLEX 12.8.0.0, Ipopt 3.13.2 with HSL 2014.01.10); S11 p.16; S12 p.10 (SUSPECT Git tag v7 dated 18 May 2018, Pyomo 5.2); S15 v2 p.16 (i7-8700, 16 GB, Gurobi 9.1 academic licence). Era E1-E4.

**PE-24 [practice, P] Averages over commonly solved instances only (made explicit after review).** "Average times were computed as the arithmetic mean of solve times for instances solved by all formulations for a particular problem class. Thus, no time outs are included in the calculation of average solve times." (S15 v2 p.16). The sentence is absent from arXiv v1 and present in v2, after a reviewer asked about time-out artefacts (S16; see PE-36).

### 4.6 Order of work: problem, code, instances, release

**PE-25 [practice, P; inferred] Industrial instance first, general problem class second, public instance added.** The Dagstuhl abstract (February 2018) and arXiv v1 (2 March 2018, "Optimization with Gradient-Boosted Trees and Risk Control", 10 pages) test "on an industrial instance" from BASF (S14 §3.26; S17 v1). The v3 of 25 September 2019 is retitled "Mixed-Integer Convex Nonlinear Optimization with Gradient-Boosted Trees Embedded", claims the problem "broadly applies to optimizing pre-trained regression tree models" and adds "concrete mixture design instance" (S17 v3), later posted on Zenodo (S30). [inferred] the public instance was added because the industrial one could not be shared; the sources do not say why.

**PE-26 [practice, P] Conference paper first, journal extension later, with a long revision tail.** "Between Steps" appeared at CPAIOR 2021 (S19). The extension "P-split formulations" went from arXiv v1 (10 February 2022; 24 pages; 320 test instances) to v3 (17 May 2025; 33 pages; 344 instances; semi-supervised clustering added; results generalised "for the case with nonconvex constraints within the disjuncts") and Mathematical Programming 2025 (S18). Era E3-E4.

**PE-27 [practice, P] Release software together with the paper.** OMLT 1.0 reached PyPI on 2022-02-08, four days after arXiv v1 of the OMLT paper (2022-02-04); 0.1.0 was on PyPI from 2021-10-18 (S26, S24). The software paper went to JMLR's Machine Learning Open Source Software track (S24). GALINI 1.0.0 was pip-installable when its preprint appeared (S10 p.1). Era E3-E4.

**PE-28 [practice, P] One repository per paper, with run scripts for every experiment and figure.** The cog-imperial organisation holds 33 public repositories created from 2017 on, most tied to a single paper; four are described literally as "Repository for paper: ..." (SnAKe, GNN_MIP_CAMD, DCBO, OMLT_CAMD) and others cite their paper in the description or README (S25, S29). SnAKe's README: "The code allows for reproducibility of the results and figures shown in the paper." and maps scripts to figures ("resampling_vs_pd_figure.py : Figure 1 and 10") (S29). `GNN_MIP_CAMD` ships the QM7/QM9 data with their licence (S29). The NeurIPS 2021 submission listed its code repository in the submission form (S16). Era E3-E4.

**PE-29 [practice as self-described, P; code not inspectable] Architect for future plug-ins before the plug-ins exist.** ANTIGONE's term hierarchy "is designed in recognition of an accelerating trend towards developing good underestimators for very specific terms" and "we anticipate further advances in the area of term-specific underestimators and have architected ANTIGONE accordingly." (S5 p.3-4). The same intent recurs in open code: GALINI's branch and cut can be extended at run time with cuts, branching, node selection, heuristics and relaxations (S10 abstract), and SUSPECT lets users register new convexity detectors (S12 §6). The Princeton C++ code is closed, so only the paper's description of ANTIGONE can be checked.

---

## Layer 5 · Judging results

### 5.1 Reporting losses and scoping claims

**PE-30 [practice, P] Losses go in the paper, including losses to the authors' own earlier tools.**
- "Observe in Table 6 that our pooling problem-specific solver APOGEE [65] regurally [sic] outperforms the more generic work presented here." (S6 p.19)
- "For the case of the point packing problems, taking this tradeoff is not advantageous" (piecewise-linear relaxations; S6 p.19)
- "In this case, the GALINI performance is not competitive with Gurobi." (360 sparse pooling instances; S11 p.21)
- "In our results the benefit provided by the pooling cuts is not as strong as in Luedtke et al. (2020) because Gurobi is more performant than the ones used in the original paper." (S11 p.19)
- "This is the result we expected since GALINI is built to be easy to extend and does not focus on performance." (S10 p.16-17)

**PE-31 [practice, P] Claims are scoped to problem classes, and "we do not know" is written down.** "the piecewise-linear underestimation scheme is best applied to specific classes of MIQCQP" (S6 p.20); "ANTIGONE derives the core of its strength from quadratic instances." (S5 p.17); "it does not, at this writing, apply function composition rules or symbolic methods" (S5 p.8). On the trade-off with SCIP: "We do not know if it would be possible for GloMIQO to dynamically abandon its more elaborate approach under circumstances where a SCIP-like algorithm is more effective or if a slower solution time on the smaller problems is a price we pay for addressing the exceptionally large problems." (S4 p.26). On Couenne's failures: "We do not know the source of the problems in Couenne 0.4" (S4 p.26). Era E1-E3.

**PE-32 [practice, P] Explain a win by splitting it into bound components.** To explain why GALINI beats Gurobi on large dense pooling instances, the paper compares lower and upper bounds separately: lower bounds are similar, GALINI's upper bound is on average 28% better on the larger problems, so "GALINI performs better on large scale pooling problems because it's able to exploit the pooling problem structure to compute a feasible solution using a pooling-specific heuristic." (S11 p.21). Era E3.

### 5.2 Turning results into defaults

**PE-33 [practice, P; inferred link] Her own earlier technique is not the default when the evidence is class-specific.** The MIQCQP paper finds piecewise-linear relaxations pay off only on process-network problems (S6 p.19-20). In GloMIQO, released through GAMS, "the GloMIQO default is not to use piecewise-linear underestimators", even though "we have previously shown that these tighter underestimators result in better performance for Meyer10 and Meyer15" (S4 p.23). Piecewise-linear relaxation was the core of her doctoral work (2008-2011 pooling papers, S1). [inferred] the default follows the ablation evidence rather than authorship.

### 5.3 Correcting errors in public

**PE-34 [practice, P] Withdraw incorrect theorems publicly, then replace them with counterexamples.** arXiv 1712.05222 (Kouyialis and Misener): v2 (15 December 2017) states "Theorem 2. The symmetry in the original quadratic problem PQ implies the symmetry in the linearised problem PLQ." (v2 p.6). v3 (23 January 2018) is a withdrawal whose comment reads "Theorem 1,2 are incorrect" (S20). v4 (20 January 2019), retitled "Symmetry Detection for Quadratically Constrained Quadratic Programs Using Binary Layered Graphs", drops both theorems, shows by example that "symmetry in the original problem does not imply the same symmetry in the relaxed problem and vice versa" (v4 p.6), and relies on theorems cited from Ramani and Markov and from Liberti. The journal version (Processes 2019) adds a third author (S20). The withdrawal was filed by the first author (PhD student); the supervisor's role is not recorded. Era E3.

**PE-35 [observed, S] No published erratum, corrigendum or retraction was found** among 151 OpenAlex works and 105 Crossref records with Misener as an author (S1, S3; index search only, 2026-10-10).

### 5.4 Answering reviewers: the NeurIPS 2021 public record (S16)

The full thread of Paper 2618 (13 replies: four reviews, five author comments, three reviewer follow-ups, the decision) was read from a Wayback Machine capture of the OpenReview API (22 December 2021). The responses are signed "Authors" (Tsay, Kronqvist, Thebelt, Misener); who drafted them is not recorded.

**PE-36 [practice, P] How the group answers criticism.**
- *Concede a precisely stated error, keep the core claim, and prove the rest with a worked example.* After Reviewer Nod7 argued that the tightness claim fails with interval-arithmetic bounds: "Your observation is correct, formulation (13)–(17) cannot be tighter than the convex hull formulation presented by Anderson et al. unless we use more “sophisticated” bounds than interval arithmetic bounds." The response then writes out a two-input node (eq1-eq12) to show the claim that does hold, and closes with "The reviewer is correct that there is indeed subtlety in the original claim(s)." The reviewer replied: "Ah, I see my misunderstanding now." The camera-ready keeps "tighter continuous relaxations" and drops the unqualified "are tighter" of v1 (S15 v1 vs v2).
- *Defend novelty by restating it as two specific contributions.* To Reviewer bEy7 ("I think the novelty is not fundamental"): "The fundamental advancements novel to this work are (i) introducing the partitioned terms, as well as partitioning strategies, and (ii) the way optimization-based bounds tightening complements our new idea of partitioning the terms." The reviewer: "I think the bullet 2 comment is convincing enough for me to realize the novelty of this paper. For that reason I decide to raise my score from 6 to 7."
- *Explain the accounting rules instead of changing them.* OBBT time is excluded from the tables: "all methods are tested withand [sic] benefit from OBBT, and OBBT problems for each layer are independent and can be solved in parallel." On averages: "We attempted to avoid “weird artifacts” from time limits by only computing average times for each set of problems on instances solved by all formulations; therefore, no time outs are included in the average times reported."
- *Decline an attractive extra experiment on cost grounds, with a reason.* On applying OBBT to Anderson et al.'s cuts: "an efficient implementation of this strategy is not trivial, as it would involve solving (a large number of) OBBT problems during each solver callback."
- *Point to the code where prose falls short.* "We will try to make the descriptions of partitioning methods clearer, but we note that the code is also provided to help reproduce the results."
- *Attribute an anomaly to run-to-run variability.* "The most likely cause of this discrepancy is variability in computational performance." The thread records no re-run (see Contradiction C2).
- *Keep the promises.* Comparing arXiv v1 with the camera-ready v2: "distinct from each other" added to the proof of Proposition 4, the unclear "second equation" remark removed, "vs." used instead of "or", the separation routine and the averaging rule described (phrase counts, S15). Era E4.

### 5.5 What reviewers observed (S16, all [observed], P)

- "The computational setup appears sound to me and sufficiently detailed for publication. Three classes of problems are investigated, although they are very similar to each other." (Reviewer Nod7)
- "As such, there is not a ton of novelty, but the insight is a worthy contribution to the literature." and "I do wish the authors left us with a clearer story on how N should be selected" (Reviewer 1SxU)
- "Many details and closely related results/reports are contained in the appendix. I think this paper might be a better fit for the full-length journal paper." (Reviewer bEy7)
- Decision (27 September 2021, Accept (Poster)): "The reviews all agreed that the paper introduces an interesting and effective strategy, only expressed minor concerns and suggestions, and recommended acceptance."

---

## Layer 6 · Expression (traces in artefacts)

**PE-37 [stated, P] Contribution framed as integration.** "Section 3 may be read as a type of critical literature review; the intellectual contribution is the way ANTIGONE ties together its many constitutive algorithms." (S5 p.2).

**PE-38 [practice, P] Retitling as the claim matures.** "Optimization with Gradient-Boosted Trees and Risk Control" became "Mixed-Integer Convex Nonlinear Optimization with Gradient-Boosted Trees Embedded" (S17); "Data Structures for Representing Symmetry in Quadratically Constrained Quadratic Programs" became "Symmetry Detection for Quadratically Constrained Quadratic Programs Using Binary Layered Graphs" (S20).

**PE-39 [practice, P] Software credit is written into the repository.** READMEs carry a "Please reference the paper" BibTeX block and a contributor table that names each developer's funding (e.g. "This work was funded by an Engineering & Physical Sciences Research Council Research Fellowship [GrantNumber EP/P016871/1]" for Ceccon in GALINI, OMLT and pooling-network; S26, S27, S29). OMLT asks users of contributed formulations to cite the contributors' own papers as well (S26).

**PE-40 [practice, P] A shared slide deck for the team, proposed through the repository.** Misener opened PR #74 (2022-03-21) to add `OMLT_Slides.pdf`: "These slides are associated with presentations that the OMLT team members are giving in both research and industrial settings." The PR was closed without merging on 2022-04-12, and no slide file is in the current tree (S26). Why it was closed is not recorded.

---

## Layer 7 · Research organisation (traces in repositories and grant records)

### 7.1 The PI's hands-on role in software

**PE-41 [practice, P; inferred role] Maintainer and reviewer, not main coder.** Commit counts by GitHub account: GALINI `franceccon` 547, SUSPECT `franceccon` 306, ENTMOOT `spiralulam` 333 and `thebtron` 245, ROmodel `johwiebe` 225; `rmisener` has 0 in GALINI and SUSPECT, 1 in ROmodel (a merge) and 21 in OMLT (S26, S27, S28). Of the 21 OMLT commits, 20 are pull-request merges and one creates the code of conduct (S26). [inferred] Code is written by students, postdocs and collaborators; her own repository work is gatekeeping, quality control and community rules. Era E3-E4; seniority: Senior Lecturer, then Research Chair.

**PE-42 [practice, P] What she asks for when she does intervene (OMLT issues she opened, S26).**
- Coverage: "With PR 137 (https://github.com/cog-imperial/OMLT/pull/137), we reduced coverage from 96% to 92%." (#139, 2023-12-04; she merged #137 the same day); "Our code coverage is generally high, but it's low for CNNs." (#48, 2022-02-03)
- Duplication: "This is a problem because anyone adding a new activation function (or debugging an existing activation function) will have to add the new activation function twice." (#125)
- Generalise rather than copy: "Even better: generalize the partition-based formulation for both fully-dense NNs and CNNs and thereby avoid having the same tricky indexing in two places." (#54)
- Documentation she drafts herself and asks the developer to check (#69, docstrings for `write_input_bounds` and `load_input_bounds`); clearer missing-dependency errors (#52); pruning stale examples (#32).
- Turning private notes into tracked issues: "(We discussed this some months ago, but I only had it as a note to myself, just adding it here for completeness)" (#46).
- Merge messages that praise specific qualities: "This neural network formulations notebook is a great addition to OMLT, really clear and nice examples. Thanks, @jalving!" (PR #29).
- Community rules: "Adding a code of conduct, Carl is happy to manage any reporting with me, let me know if anyone else wishes to be added." (PR #61, 2022-02-15)

### 7.2 How funding shaped which tools stayed alive

**PE-43 [practice, P; inferred] Fellowship-funded MINLP software went quiet when the fellowship ended; industry-backed tools kept releasing.** GALINI, SUSPECT and pooling-network credit EP/P016871/1 (Aug 2017 to Aug 2022; S27, S29, S30). The last code commits to GALINI and SUSPECT are dated 2022-07-14, both by a Sandia collaborator (S27). The general GALINI solver paper exists only as an Optimization Online preprint (14 January 2021); the published journal paper is the pooling application (Computers & Chemical Engineering 2022) (S10, S11, S3). OMLT (co-developed with Sandia and Carnegie Mellon) released to 1.2.2 in March 2025 and ENTMOOT (acknowledging "The support of BASF SE") to 2.1.1 in February 2026 (S26, S28). [inferred] continuity of a tool tracks continuing funding and an external co-maintainer, not the PI's original plan (see C1).

**PE-44 [stated, P] Pandemic change in collaboration mode.** "we had planned several in-person secondments, but because everything moved online, we switched to a model of just actively contributing to the same open-source projects" (Sandia; award record, S30). The commit record agrees: Sandia staff commit to GALINI, SUSPECT and OMLT (`michaelbynum`, `jalving`, `carldlaird`; S26, S27).

### 7.3 Industry partners as sources of instances, cases and compute

**PE-45 [stated, P] Partners provide the test material.** Award-record entries (normally written by the award holder; authorship not verified): Royal Mail "have meet [sic] with us for ~5 full days over the course of the last 6 months. Our collaborators also have provided us with test sets to try out our ideas."; "Bayer contributed their time and developed case studies relevant to their business."; "The group of Professor Liesbet Geris provided the application and the computing resources." (S30). The GBT work was tested on "an industrial instance from BASF" (S14 §3.26). Era E3-E4.

### 7.4 Release model: commercial in 2013, open source from 2017

**PE-46 [practice, P/S] From licensed GAMS solvers to permissive open-source code.** ANTIGONE was released on 2 May 2013 as "commercially available through Princeton University and the GAMS Development Corporation as part of GAMS version 24.1" (S9); using it "requires an ANTIGONE license, a CPLEX license, and a CONOPT or SNOPT license" (S7). From the first cog-imperial repositories (2017) on, most carry Apache-2.0, BSD-3-Clause or MIT licences; a few have no licence file, and OMLT's licence is reported as unrecognised by GitHub although its PR template refers to the BSD licence (GitHub licence field, S25, S26). ANTIGONE still ships in the current GAMS documentation as "ANTIGONE 1.1", vendor Princeton University, the same version string as in the 2014 paper's tables (S8, S5). No evidence of later ANTIGONE development was found.

---

## Layers 2-3 · Choosing, generating and dropping directions (process traces only)

**PE-47 [stated, P] Idea sources named in the artefacts.** GloMIQO thanks "Benoit Chachuat for a long conversation that sparked our reformulation strategies" (S4 p.27). In an undated Imperial interview (title "Lecturer in Computational Optimisation") she describes three strands, "(i) novel optimisation algorithms and numerical techniques, (ii) fundamental process systems engineering, and (iii) software tools and protocols", and the import into MINLP of approximation algorithms, Bayesian optimisation and satisfiability modulo theories (S32; wording checked against the raw page HTML; the page carries no date).

**PE-48 [practice, P; inferred] What happened to the imported techniques.** In her OpenAlex record: one SMT paper ("Satisfiability modulo theories for process systems engineering", Computers & Chemical Engineering 2018, DOI 10.1016/j.compchemeng.2018.03.004) and none after; approximation algorithms from 2017 to 2021 with Letsios (e.g. DOI 10.1016/j.compchemeng.2018.03.002; DOI 10.1016/j.compchemeng.2019.106599); Bayesian optimisation from 2015 (arXiv 1511.05385) to a main line in 2022-2026 (S1, S2). [inferred] continuation follows the people and partners (the approximation-algorithm papers are co-authored with Letsios; BASF funds the Bayesian-optimisation work, S30) more than the declared programme.

**PE-49 [practice, P; inferred] Structure detection is a thread that crosses eras.** Special-structure detection inside GloMIQO/ANTIGONE (S4 §3.2, S5 §3.2), named-structure (pooling) recognition by functional programming (AIChE J 2016, DOI 10.1002/aic.15308), SUSPECT (2019), symmetry detection (2017-2019) and the GALINI pooling plug-in (2021-2022) (S1, S11, S12, S20). The continuity is my reading.

### Dropped, dormant or unpublished work

| Item | Evidence | Status on 2026-10-10 | Tag |
|---|---|---|---|
| Piecewise-linear relaxations as solver default | S4 p.23 | kept as an option, off by default | [practice] P |
| "Risk control" framing of the GBT paper | S17 v1 vs v3 | retitled; risk penalties kept as convex penalty terms | [practice] P |
| Theorems 1-2 on symmetry under relaxation | arXiv 1712.05222v3 comment | withdrawn as incorrect; replaced by counterexamples | [practice] P |
| "Detecting Symmetry in Designing Heat Exchanger Networks" (arXiv 1711.02564) | S21, Crossref search (S3) | no published version found | [observed] S |
| "Scoring positive semidefinite cutting planes for quadratic optimization via trained neural networks" (Optimization Online 2018/11/6943; with IBM's Bonami and Tramontani; code `SDPCutSel-via-NN`, last push 2019-10) | S22, S25, Crossref search (S3) | no published version found; the repository README cites the same Optimization Online entry under a different title, "Selecting cutting planes for quadratic semidefinite outer-approximation via trained neural networks" | [observed] S |
| GALINI general-solver paper (Optimization Online 2021/01/8207) | S10, S3 | no journal version found; only the pooling application was published | [observed] S |
| GALINI and SUSPECT code | S27 | no code commits after 2022-07-14 | [practice] P |
| ANTIGONE development | S8, S5 | still distributed as 1.1; no later version found | [observed] S |
| SMT for process systems engineering | S1 | one paper (2018) | [practice] P; dropped [inferred] |

No rejected-paper record was found. The NeurIPS 2021 submission form had fields for previous submission history, but they are empty in the public record (S16). Whether any of the unpublished items above was rejected is unknown.

## Layer 1 · Taste

Not assessed in this note. The behavioural regularities above (fair benchmarks, scoped claims, public instances, extensible software) are inputs for the taste analysis in `01-publications.md` and `02-methodology.md`.

---

## Contradictions (kept, not reconciled)

- **C1 · GALINI: plan and self-report against the repository record.** The 2017 award abstract: "Our approach is to freely release GALINI to users including those in the process industries, publicise the software, demonstrate its utility, and build a user community that will feed back into software development." The end-of-award key findings: "We have achieved what we wrote in the grant proposal" (S30). The record shows GALINI with 45 GitHub stars, no code commits since 2022-07-14, and the general-solver paper still a preprint, while its own preprint says it "does not focus on performance" (S10, S25, S27). The pooling plug-in promised in the proposal was delivered and published (S11).
- **C2 · Permuted-model experiments: seminar conclusion against later practice.** Dagstuhl 18081, co-organised and co-edited by Misener, recorded among its main conclusions "the need to incorporate experimentation on permuted models as has become standard in the MIP community" and that "conducting fair benchmarks between different solvers remains inherently difficult and users of solver software should not rely on simplistic comparisons" (S14 p.85). The NeurIPS 2021 paper does not report repeated runs, seeds or permutations (Appendix A.4 describes one solver configuration per formulation), and the authors explained an inconsistency in Figure 3 by "variability in computational performance"; the thread records no re-run (S15, S16). These were collective conclusions of a working group, not a statement attributed to her.
- **C3 · "OMLT (which can use and extend GALINI)"** (award record, S30) against the OMLT repository: no dependency on and no file referring to GALINI in `pyproject.toml` or the file tree (S26). It may hold only in the loose sense that OMLT emits Pyomo models any Pyomo solver can take; the record does not say.
- **C4 · Mixed-date snapshot inside the ANTIGONE comparison.** Libraries frozen "as of 11 March 2013", solvers "the latest versions as of February 2014" (S5 p.10). [inferred] the solver runs were refreshed during revision while the test suite was not.
- **C5 · Declared programme against continuation.** The interview lists satisfiability modulo theories as one of three imported techniques (S32); the publication record shows one SMT paper (2018) and no follow-up (S1).

## Gaps

- **Review threads other than NeurIPS 2021: not read.** OpenReview's API and pages require a browser challenge. The Wayback Machine has the 2021 API capture (used) but no API capture for NeurIPS 2023 `znW5jNIOED`, whose archived page holds no replies. NeurIPS 2022 (tree-ensemble kernels, arXiv 2207.00879; SnAKe, arXiv 2202.00060), NeurIPS 2024, NeurIPS 2025 (Datasets and Benchmarks) and ICLR 2026 (BoGrape, arXiv 2503.05642) threads were not located or not readable.
- Journal reviews (J. Global Optim., Math. Program., INFORMS J. Comput., Comput. Chem. Eng., JMLR MLOSS) are not public. Not available.
- GloMIQO 2 (Optim. Methods Softw. 2015, DOI 10.1080/10556788.2014.916287): no open copy in Spiral; not read. "Between Steps" (S19) and the published P-split, ENTMOOT and OMLT full texts: not read beyond abstracts and version histories.
- Princeton-era source code (GloMIQO/ANTIGONE C++) is closed: no repository, changelog or test scripts to inspect. ANTIGONE maintenance after 2014 is unknown.
- Talks: the GALINI INFORMS 2020 video and dashboard demo (YouTube), the Cassyni talk "Bayesian optimization and design of experiments" (2022, DOI 10.52843/cassyni.f44xtg; JavaScript-only page) and the NeurIPS 2023 SlidesLive recording: not read. No transcript was saved under `references/sources/talks/`.
- "Novel Global Optimization Methods: Theoretical and Computational Studies on Pooling Problems with Environmental Constraints" (2012, listed in OpenAlex without venue; probably her Princeton dissertation, not confirmed): not read.
- Who drafted the NeurIPS 2021 responses, and her role in QPLIB curation and in the symmetry-preprint withdrawal: not documented.
- Student recollections of lab routines (debugging habits, code review, how experiments are planned) belong to agent 04 and were not searched here.
- Tool limits during this run: DBLP returned a bot challenge; Semantic Scholar was rate-limited; the OpenAlex free daily budget ran out late in the run (the works list had already been retrieved).

## Sources

- S1 · OpenAlex author A5054244566 (ORCID 0000-0001-5612-5417), 151 works with DOIs, queried 2026-10-10 · https://api.openalex.org/authors/A5054244566 · secondary (index)
- S2 · arXiv API author query `au:Misener` (59 entries, incl. an unrelated astrophysicist William Misener), 2026-10-10 · https://export.arxiv.org/api/query?search_query=au:Misener · secondary (index)
- S3 · Crossref REST API queries (author records; errata/correction check; title searches for unpublished preprints), 2026-10-10 · https://api.crossref.org/works · secondary (index)
- S4 · Misener R, Floudas CA, "GloMIQO: Global mixed-integer quadratic optimizer", J. Global Optim. (2013), accepted manuscript and supplement from Spiral 10044/1/19682 · DOI 10.1007/s10898-012-9874-7 · primary
- S5 · Misener R, Floudas CA, "ANTIGONE: Algorithms for coNTinuous / Integer Global Optimization of Nonlinear Equations", J. Global Optim. (2014), accepted manuscript and supplement from Spiral 10044/1/15506 · DOI 10.1007/s10898-014-0166-2 · primary
- S6 · Misener R, Floudas CA, "Global optimization of mixed-integer quadratically-constrained quadratic programs (MIQCQP) through piecewise-linear and edge-concave relaxations", Math. Program. (2012), accepted manuscript from Spiral 10044/1/10938 · DOI 10.1007/s10107-012-0555-6 · primary
- S7 · Floudas CA, Misener R, GAMS/ANTIGONE solver manual (dated 16 April 2013), current GAMS documentation · https://www.gams.com/latest/docs/S_ANTIGONE.html · primary
- S8 · GAMS Development Corp., solver overview (GAMS 54 "latest" documentation) · https://www.gams.com/latest/docs/S_MAIN.html · secondary
- S9 · Princeton CBE news, "Misener and Floudas Release ANTIGONE", 2 May 2013 (Wayback capture 2019-12-16) · https://cbe.princeton.edu/news/misener-and-floudas-release-antigone · secondary
- S10 · Baltean-Lugojan R, Bynum ML, Ceccon F, Li C, Misener R, "GALINI: An extensible mixed-integer quadratically-constrained optimization solver", Optimization Online, 14 January 2021 · https://optimization-online.org/2021/01/8207/ · primary
- S11 · Ceccon F, Misener R, "Solving the pooling problem at scale with extensible solver GALINI", arXiv 2105.01687v1 (4 May 2021); Comput. Chem. Eng. (2022) · DOI 10.1016/j.compchemeng.2022.107660 · primary
- S12 · Ceccon F, Siirola JD, Misener R, "SUSPECT: MINLP special structure detector for Pyomo", Optim. Lett. (2019) · DOI 10.1007/s11590-019-01396-y · primary
- S13 · Furini F, Traversi E, Belotti P, Frangioni A, Gleixner A, Gould N, Liberti L, Lodi A, Misener R, Mittelmann H, Sahinidis N, Vigerske S, Wiegele A, "QPLIB: a library of quadratic programming instances", Math. Program. Comput. (2019), preprint at iris.uniroma1.it · DOI 10.1007/s12532-018-0147-4 · primary (co-authored)
- S14 · Bonami P, Gleixner AM, Linderoth J, Misener R (eds.), "Designing and Implementing Algorithms for Mixed-Integer Nonlinear Optimization (Dagstuhl Seminar 18081)", Dagstuhl Reports 8(2):64-87 (2018) · DOI 10.4230/DagRep.8.2.64 · primary (co-edited)
- S15 · Tsay C, Kronqvist J, Thebelt A, Misener R, "Partition-based formulations for mixed-integer optimization of trained ReLU neural networks", NeurIPS 2021; arXiv 2102.04373 v1 (8 Feb 2021) and v2 (20 Oct 2021, camera-ready) · https://proceedings.neurips.cc/paper/2021/hash/17f98ddf040204eda0af36a108cbdea4-Abstract.html · primary
- S16 · OpenReview forum jhd62iKzRuj (NeurIPS 2021 Paper 2618): 4 reviews, 5 author comments (9-16 Aug 2021), 3 reviewer follow-ups, decision 27 Sep 2021; read from the Wayback capture (22 Dec 2021) of api.openreview.net/notes?forum=jhd62iKzRuj · https://openreview.net/forum?id=jhd62iKzRuj · primary (reviews are others' observations)
- S17 · Mistry M, Letsios D, Krennrich G, Lee RM, Misener R, arXiv 1803.00952 v1 (2 Mar 2018, "Optimization with Gradient-Boosted Trees and Risk Control") and v3 (25 Sep 2019, "Mixed-Integer Convex Nonlinear Optimization with Gradient-Boosted Trees Embedded"); INFORMS J. Comput. · DOI 10.1287/ijoc.2020.0993 · primary (abstracts and version history)
- S18 · Kronqvist J, Misener R, Tsay C, "P-split formulations: A class of intermediate formulations between big-M and convex hull for disjunctive constraints", arXiv 2202.05198 v1 (10 Feb 2022) and v3 (17 May 2025); Math. Program. (2025) · DOI 10.1007/s10107-025-02232-1 · primary (abstracts and version history)
- S19 · Kronqvist J, Misener R, Tsay C, "Between Steps: Intermediate Relaxations Between Big-M and Convex Hull Formulations", CPAIOR 2021, LNCS; arXiv 2101.12708 · DOI 10.1007/978-3-030-78230-6_19 · primary (metadata only)
- S20 · Kouyialis G, Misener R, arXiv 1712.05222 v1-v4 (v3 withdrawn 23 Jan 2018, "Theorem 1,2 are incorrect"); Kouyialis G, Wang X, Misener R, "Symmetry Detection for Quadratic Optimization Using Binary Layered Graphs", Processes 7(11):838 (2019) · DOI 10.3390/pr7110838 · primary
- S21 · Kouyialis G, Misener R, "Detecting Symmetry in Designing Heat Exchanger Networks", arXiv 1711.02564 (7 Nov 2017) · primary (abstract only)
- S22 · Baltean-Lugojan R, Bonami P, Misener R, Tramontani A, "Scoring positive semidefinite cutting planes for quadratic optimization via trained neural networks", Optimization Online, 26 Nov 2018 · https://optimization-online.org/2018/11/6943/ · primary (abstract only)
- S23 · Thebelt A, Kronqvist J, Mistry M, Lee RM, Sudermann-Merx N, Misener R, "ENTMOOT: A framework for optimization over ensemble tree models", arXiv 2003.04774 v1-v3; Comput. Chem. Eng. 151:107343 (2021) · DOI 10.1016/j.compchemeng.2021.107343 · primary (abstracts and version history)
- S24 · Ceccon F, Jalving J, Haddad J, Thebelt A, Tsay C, Laird CD, Misener R, "OMLT: Optimization & Machine Learning Toolkit", JMLR 23(349):1-8 (2022), MLOSS track; arXiv 2202.02414 · https://www.jmlr.org/papers/v23/22-0277.html · primary (metadata)
- S25 · GitHub organisation cog-imperial, repository list (33 public repositories with dates and licences) via the GitHub API, 2026-10-10 · https://github.com/cog-imperial · primary
- S26 · OMLT repository: README, PR template, tests workflow, file tree, `pyproject.toml`, the 21 commits by `rmisener`, the 10 issues/PRs she opened; PyPI release history · https://github.com/cog-imperial/OMLT · primary
- S27 · GALINI and SUSPECT repositories: READMEs, contributor counts, latest commits · https://github.com/cog-imperial/galini ; https://github.com/cog-imperial/suspect · primary
- S28 · ENTMOOT repository README, contributor counts, PyPI release history · https://github.com/cog-imperial/entmoot · primary
- S29 · Per-paper repositories (READMEs): PartitionedFormulations_NN, SnAKe, GNN_MIP_CAMD, tree_kernel_gp, min_matches_heuristics, points_in_circles, pooling-network, SDPCutSel-via-NN · https://github.com/cog-imperial · primary
- S30 · UKRI Gateway to Research, EP/P016871/1 "GALINI: Global ALgorithms for mixed-Integer Nonlinear optimisation of Industrial systems" (abstract, planned impact, outcomes, key findings, further funding, datasets) · https://gtr.ukri.org/projects?ref=EP%2FP016871%2F1 · primary
- S31 · MINLPLib instance list and instance page `p_ball_10b_5p_2d_h` · https://www.minlplib.org/p_ball_10b_5p_2d_h.html · secondary
- S32 · Imperial College London Enterprise, "Five minutes with Dr Ruth Misener" (undated; header "Lecturer in Computational Optimisation") · https://www.imperial.ac.uk/enterprise/business/industry-partnerships-and-commercialisation/industry-partnerships/meet-some-of-our-academics/dr-ruth-misener/ · primary (stated)
- S33 · ESCAPE-30 (2020) plenary speaker biography · https://www.aidic.it/escape30/plenary/misener.pdf · secondary
- S34 · NeurIPS 2023 poster page and archived OpenReview forum znW5jNIOED for "Optimizing over trained GNNs via symmetry breaking" (arXiv 2305.09420); replies not retrievable · https://nips.cc/virtual/2023/poster/69879 · secondary (attempted)
- S35 · Kronqvist J, Misener R, "A disjunctive cut strengthening technique for convex MINLP", Optim. Eng. (2020) · DOI 10.1007/s11081-020-09551-6 · primary (metadata and repository README only)
- S36 · Letsios D, Kouyialis G, Misener R, "Heuristics with performance guarantees for the minimum number of matches problem in heat recovery network design", Comput. Chem. Eng. 113:57-85 (2018) · DOI 10.1016/j.compchemeng.2018.03.002 · primary (metadata and repository README only)
