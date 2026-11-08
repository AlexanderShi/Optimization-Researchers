# Santanu S. Dey: process evidence (research note 03)

| Field | Value |
|---|---|
| Researcher | Santanu S. Dey (Georgia Institute of Technology, H. Milton Stewart School of Industrial and Systems Engineering; PhD Purdue 2007) |
| Dimension | 03: process evidence. What the record shows he and his co-authors actually do: code, data releases, experiment sections, version histories, answers to referees, dropped and unpublished work |
| Research date | 2026-10-10 |
| Sources consulted | 61 (50 primary, 11 secondary or metadata only), plus 1 attempted source that could not be read (OpenReview). One line each in **Sources** |
| WebSearch calls used | 1 of 4 |
| User-supplied material | None. `references/sources/talks/` holds seven auto-caption transcripts that research agent 02 saved in this workflow on 2026-10-10. They are web-derived, not user-supplied. `papers/`, `essays/` and `software/` hold only `.gitkeep`. `private/` was not opened |
| Language | English (team.json) |

**How this was built.**
- **Code.** I read the code that accompanies his papers:
  - three INFORMS Journal on Computing repositories (README, AUTHORS, driver scripts, solver settings, generators);
  - three repositories on his students' personal GitHub accounts, including one repository's full commit history;
  - one co-author's repository (2016).
- **Data.** I listed seven instance and data archives from his homepage with Python `zipfile`. They were never extracted or executed.
- **Experiment sections.** I read the computational sections of 25 papers and preprints in text extracted with `pdftotext`. A keyword script found the protocol sentences, and I then read each one in context.
- **Version histories.**
  - First and later versions of 12 papers (arXiv v1 against the final arXiv or author version), and a NeurIPS camera-ready against its arXiv v1.
  - Submission histories of 30 arXiv records.
  - A live arXiv listing (71 records), checked against DBLP, Crossref and Semantic Scholar to find preprints with no published version.
- **Errata.** I checked Crossref's `updates` relation for errata, corrections and retractions on 116 DOIs.
- **Transcripts.** The seven transcripts were searched for accounts of how work was done, with timestamps taken from the caption files.
- **Reuse of an earlier attempt.** An earlier, interrupted attempt at this same step on the same day had downloaded PDFs, repository clones and archives into the scratch folder. I reused them only after checking them in this run:
  - the three INFORMSJoC clones match the live HEAD commits;
  - the seven archives match the live `Content-Length`;
  - 25 PDFs match live file sizes, and the pooling preprint is byte-identical to the live Optimization Online file.
  - All metadata (arXiv, DBLP, Crossref, GitHub) was fetched live in this run.

**Tags.**
- [stated]: what Dey or his co-authors wrote or said.
- [practice]: what the record shows was done (code, settings, data, versions, experiment design).
- [observed]: what others recorded (students' theses, databases).
- [inferred]: my reading, which no source states.

Each item is also marked primary or secondary. Almost everything is co-authored. A practice therefore belongs to the paper's team, and whoever wrote the code is named where the record shows it.

**Quotes.**
- Quotes are verbatim from the extracted text. I made three kinds of change:
  - re-joined words hyphenated across a line break;
  - restored ligatures and diacritics that the extraction split or dropped (for example "dierent" becomes "different", and "B�eluga" becomes "Béluga");
  - where the extraction lost a mathematical symbol, stopped the quote before it or restored the symbol in [brackets].
- Page numbers that fall inside a sentence are never bridged silently. The quote stops at the page break.
- Talk quotes are machine captions with approximate cue timestamps. Words in [brackets] are my corrections of evident mis-hearings.
- Code is quoted exactly as written, typos included.

---

## 0. Summary for the synthesizer

1. **The controlled experiment is built into the code, not just described** [practice · primary; S13, S14, S26, S30, S34].
   - Branching studies run their own "naive" or "textbook" branch-and-bound in Python or Julia.
   - Full strong branching is called only as an oracle.
   - SCIP runs with presolve, propagation, heuristics and conflict analysis switched off, and its objective limit is set to the known optimum.
   - Three seeds are used even when the code is deterministic.
   - This confirms note 02's belief R7 at code level (§3.3).
2. **Ground truth is computed before a heuristic is designed** [practice · primary; S12, S15, S17, S45].
   - Exact optimal branch-and-bound trees by dynamic programming (instances with at most 20 binary variables).
   - Exhaustive enumeration of 31,465 supports before the sparse-cut algorithm was designed.
   - An "expert method" that measures the possible speedup before a learned heuristic was built (§2).
3. **When public instances are too easy or too favourable, they build harder or adversarial ones** [practice · primary; S1, S6, S7, S17, S42].
   - A radial OPF library on which the SDP relaxation is inexact.
   - A 70-instance pooling suite, because the classical instances "are solved in a matter of seconds by BARON".
   - Larger generalized-pooling and BoxQP instances, made with the original generators.
   - Random generators plant a feasible point and control sparsity. One paper says it draws continuous objective coefficients to avoid dual degeneracy, but its released script does not (§3.1; Contradiction 2).
4. **Baselines are the strongest public code, made comparable, and weaker alternatives are tried and reported** [practice · primary; S3, S6, S16].
   - The competitor's SDP code was modified to include the same angle bounds and was run with two SDP solvers.
   - BARON was given 6 hours against 1 hour for the other methods.
   - A specialised pooling solver was tried and dropped: they "did not observe any performance benefit compared to BARON". Only the strongest SDP solver's bounds are tabulated (§3.2).
5. **What was tried and dropped is usually written into the paper** [stated + practice · primary; S6–S8, S10, S17, S19, S26].
   - The provable feasibility-pump variant "was not competitive" and was replaced by a conservative hybrid (§3.8, §7).
6. **A headline claim was withdrawn silently between preprint versions** [practice · primary; S2].
   - v1 of the award-winning Strong SOCP paper (April 2015) called the cycle-based model "an exact reformulation of the AC OPF problem".
   - v4 (October 2015) calls it a "valid bilinear extended relaxation".
   - No note, erratum or explanation was found (§4.2).
7. **Referee input is absorbed and credited** [stated + practice · primary; S5, S16, S19, S25, S27, S29].
   - A sensitivity-analysis section was added "in particular" at reviewers' suggestion, and a reviewer's objection was turned into named future work.
   - Benchmarks widened between versions: gas networks went from 1 to 5 GasLib networks, the kNN paper from 3 to 7 test networks, and the sparse CCA paper gained a comparison with three published methods (§4.3).
8. **Code appears where a venue requires it or a student publishes it** [practice · primary; S30–S36, S44].
   - His homepage links 7 instance or data archives (papers from 2014 to 2021) and no code.
   - Code appears in three IJOC repositories (2024–2025; commits by the first authors and by the accounts that created or merged the repositories), in a NeurIPS supplement, and on students' personal GitHub accounts (§3.6).
9. **Two discrepancies between the released code and the paper text** [practice · primary; S13, S30]. Not reconciled (Contradictions 2–3).
   - The random-knapsack generator in the released script differs from the distribution described in the preprint.
   - The released results file lacks runs that the protocol says were made.
10. **There is no group platform. Each first author brings a stack** [practice · primary + inferred; §3.5].
    - C# for Kocuk; AMPL, GAMS and NEOS for Gupte; MATLAB with CVX for Santana; Python for Shah; Python and Julia for Gu; Julia for Han, Becu and Xavier.
    - Compute is modest: laptops, a desktop, the ISyE cluster, co-authors' clusters.
    - One student repository shows a reusable branch-and-bound testbed spanning three papers (§6).
11. **Failures on record** [practice · primary; §7].
    - No errata, corrections or retractions are registered in Crossref for any of 116 DOIs.
    - 29 of 56 published arXiv records were never updated after v1.
    - Older preprints with no published version: a kNN heuristic (2020), learning-enhanced branching (2022), a kernel two-sample test paper (2023, revised three times) and a GMI-history paper (2024).
    - A `LearningFromOptimalTrees/` code directory was deleted from a student repository in 2024.
12. **Numerical results guide the work; proofs certify it** [practice · primary; S22, S23].
    - A counterexample is bounded by a "simple and rigorous" box rather than the tighter box seen numerically, because "the non-convex nature of the set can impair solvers in certifying global optimality".
    - Facets found computationally are then shown not to be Eigen-CG "without relying on numerical methods" (§4.4).

---

## 1. Layers 1–2: taste and problem choice, as the record shows them

**1.1 Problems arrive through people who own the data or the application** [practice + stated · primary].
- Sparse CCA. arXiv v1: "The authors would like to thank Rahul Mazumder for introducing the problem to us and for sharing data and references." (S29, Acknowledgements).
- Sparse PCA. "We would like to thank Munmun De Choudhury for providing us with the internet data set." (S16, v3).
- Pooling. Industry-funded, through ExxonMobil (note 01 §2.2).
- Structural model updating. Came through civil-engineering colleague Yang Wang (note 04 H4); his FEM instances recur in S8, S20 and S21.
- Copositive duals for sensitivity analysis. In the talk, the motivation was another group's empirical observation: "they empirically observed that this was always true okay in their paper and so that sort of really motivated us" (S48, about 00:26:19).
- [inferred] Problems typically enter through a collaborator with data or a field observation. The group then generalises them into a structural question.

**1.2 They choose the instances where the accepted method fails, and make those the object of study** [practice · primary; S1].
- In 2014 the group did not use the standard test cases as they were. It turned them into cases on which the relaxation fails: "Given a meshed network, we first find a spanning tree. Then, only load values and generation lower/upper bounds are changed, whenever necessary, to construct examples where the SOCP/SDP relaxation is not exact." (§5.1).
- The same paper still closes with a guard against over-reading: "We remind the reader here that SDP relaxations are very powerful and their importance is definite. Our work only serves to demonstrate the limitations of SDP relaxations" (§7).
- Era: 2014, PhD student Kocuk, one desktop PC (§3.5).

**1.3 Known but untested objects are worth a computational paper of their own** [stated + practice · primary].
- The 2024 IJOC bilinear-cover paper says: "While the lifted bilinear cover inequality was derived in [12], its computational usefulness has not been evaluated." [12] is the group's own IPCO 2021 and Math. Program. 2023 theory paper.
- It names its template: "We are inspired by the classical paper of [7]. This paper is one of the first to highlight the computational importance of lifted cover inequalities in MILP." (S18).
- [7] is Crowder, Johnson, Padberg, Oper. Res. 31(5):803–834, 1983, doi:10.1287/opre.31.5.803 (metadata verified, S58).
- The same pattern holds for the two-row cuts:
  - The IPCO 2010 paper called its random-instance tests "a first step in testing the effectiveness of the triangle cuts" (S9, Springer abstract).
  - The IJOC 2014 paper then carried them to MIPLIB.
- [inferred] A theory result is followed by a separate paper whose only job is to measure it.

**1.4 What the record shows they let go** [practice · primary; details in §7].
- Two lines got as far as public preprints, with no publication found by 2026-10-10:
  - a data-driven kNN heuristic (S27);
  - learning-enhanced branching (S26).
- One line stopped before a preprint: learning from optimal trees (S34, S45).
- [inferred] The lines that stall are the machine-learning-flavoured ones, but three cases are too few to call this a rule.

---

## 2. Layer 3: idea generation, and what is done first

**2.1 Exact or exhaustive computation first, then the practical method** [practice · primary].
- **Sparse-PCA cuts** (S17, §4). Before designing the cut algorithm they enumerated every support on three small BoxQP instances: "We assign a score to each of the 31,465 supports, then select the top 5% of supports (1,574 supports) having the highest score."
  - The section states its purpose: "the enumeration experiments justify how many sparse cuts we should generate at each round, and whether or not we should allow the use of a few dense eigencuts."
  - Only three instances are reported: "While for succinctness we report on only these three instances, we obtained similar outcomes with other instances from the family."
  - Era: C++ with Eigen, Gurobi 9.0 and MOSEK 9.2, 2020–2022, with Montreal co-authors.
- **Strong branching** (S12, §5–6; S45 ch. 4). A dynamic program computes the smallest branch-and-bound tree, against which full strong branching is measured. The thesis states the price: "Note that all of these instances have only up to 20 binary variables since we are unable to run the DP algorithm of Section 4.2.1 for larger instances." (S45, ch. 4, p. 40).
- **GMI closure from history** (S15, §5.3). "Before benchmarking the performance of the learning heuristic, we begin by evaluating a theoretical expert method to gauge what potential speedups are achievable with this approach and to identify which MIPLIB 2017 instances could potentially benefit."
  - The result redirected the project: "However, when accounting for the time required to collect the cuts, most positive instances become negative, which motivates our learning approach."
- **Eigen-CG rounding** (S23).
  - All 116,764 facets of BQP6 were checked: "our computational analysis shows that 3,676 inequalities can be represented as Eigen-CG inequalities (furthermore, BH), while the remaining 113,088 facets are not of the Eigen-CG type".
- Note 04 T1 found the same habit in theses: PORTA computations of small cases before conjecturing (2012–2024).

**2.2 An observation in experiments turns into a theorem** [stated (spoken) · primary, machine captions].
- Sparse PSD approximation (S47, about 00:15:20): "what we observed uh in some sort of experiments and so forth is that actually this bound is decent that this bound seems to be much better when k is small and really this bound is not so nice when k is really large and so we were able to come up with a different bound".

**2.3 Prior work is sometimes found after the result** [stated (spoken) · primary].
- Copositive duality (S48, about 00:25:44): "when we did this we realized actually sort of a year back few months back [name unclear in captions] who's now at Purdue and co-authors actually proved this result for the bounded case but their proof was not constructive".
- [inferred] The literature search is not always complete before the work. He says this in public.

**2.4 Try the obvious version first** [stated (spoken) · primary].
- Lagrangian duals with zero gap (S48, about 00:57:39): "we tried the classical [Lagrangian]. We cannot go to all monomials. So we just tried the first thing that you would try the quadratic".

---

## 3. Layer 4: experiments and execution

### 3.1 How test instances are chosen and built

| Practice | Evidence (verbatim where quoted) | Tag · source | Era |
|---|---|---|---|
| Replace a too-easy public set with a harder suite | "The pooling instances commonly used in literature mostly comprise of small-scale problems proposed many years ago; see for example Tawarmalani and Sahinidis (2002). Since these problems are solved in a matter of seconds by BARON, we created a test suite of 70 medium- to large-scale" instances: 20 from Alfaki and Haugland plus 50 random, with the generator in an appendix | [practice · primary] S6 §5.2 | 2013, Gupte; AMPL/GAMS/NEOS |
| Scale up a published recipe instead of inventing one | GPP archive README: "This set contains 24 instances rondomly generated in the same way the authors of [doi:10.1007/s10898-012-9890-7] have generated instances C2 and D1. The only difference is that we have increased the number of nodes and changed the density of the network to obtain more challenging instances." BoxQP: "we consider all instances available at https://github.com/sburer/BoxQP_instances, and we additionally generate our own larger instances, for n = 200 and n = 250, using the same instance-generation code available in the link." | [practice · primary] S42, S17 §6.2 | 2018–2021 |
| Adversarial instances built from standard ones | Radial OPF library built from MATPOWER cases by spanning trees plus changed loads and bounds (§1.2). Released as `TreeLibrary.zip`: 8 MATPOWER `.m` files dated June 2014 | [practice · primary] S1, S37 | 2014 |
| Real data alongside synthetic | Mining-industry generalized-pooling data, literature sets and random sets (S7 §4.2). Real covariance data for sparse PCA (S43: colon, lymphoma, Eisen, Reddit matrices). UCI and breast-cancer data for sparse CCA (S29 §5.1). GasLib networks (S19). NESTA "Typical, Congested and Small Angle Operating Conditions" (S3 §5) | [practice · primary] | 2015–2024 |
| Plant a feasible point, control sparsity and density | Feasibility pump: "to guarantee feasibility, a 0/1 point is sampled uniformly at random ... and the right-hand sides ci are set to be the smallest ones that make this point feasible" (S10 §5.2). Sparse cuts: "To guarantee that the instances generated are non-trivial, we follow the following steps", sampling a Bernoulli 0/1 vector and adding noise (S11 §3.1.2). Bilinear covers: "Inspired by the classical paper [7] and by the fact most instances in practice are sparse, we generate sparse instances of the above model." (S18 §4.1) | [practice · primary] | 2016–2024 |
| Draw objectives so that degeneracy does not confound the measurement | "By randomly sampling objective coefficients from a continuous distribution, we ensure that almost surely the instances do not exhibit dual degeneracy." (S13 §3.1). Contradiction 2 shows the released script does not do this | [stated · primary] | 2024 |
| A reusable generator library | `src/instance_generator_grb.py` (1,507 lines) defines about 25 generators. Among them: packing and covering, lot-sizing variants including `LotSizingPathological`, chance-constrained power and portfolio models, TSP, matching, p-median, and four under the comment `# Gasse et al instances` (probably from arXiv:1906.01629 [inferred; the code gives no citation]). `generate()` re-draws an instance whenever Gurobi does not return status optimal. The thesis explains why the TSP and matching generators went unused: "graph-based combinatorial problems with “edge variables” such as matching and Traveling Salesman Problem could not be included". It gives the reason across a page break: with at most 20 binary variables, such instances would be too small to be interesting | [practice · primary] S30, S34, S45 | 2021–2025, Shah |
| Benchmark filters written as code | `# filter instances based on ease of solving and number of variables`, keeping MIPLIB 2017 instances with status `"easy"`, at most 500 integer or binary variables, at most 10,000 variables, and not infeasible. Text: "Those instances not solved in 72 hours are discarded. In addition, 1 instance was discarded since it was solved at the root node. This resulted in a final set of 21 instances" | [practice · primary] S30 `scripts/MIPLIB/run_miplib_expt.py`; S13 §3.2 | 2024 |
| Homogeneous families made from MIPLIB | "we generated 55 variations (50 for training, 5 for testing) of each MIPLIB 2017 benchmark instance [31] by perturbing objective coefficients and right-hand-side values". The perturbation was checked, with a reported surprise: "On the contrary we discovered that the variations, on average, became more difficult to solve." | [practice · primary] S15 §5.2 | 2024, workstation |
| Exclusions listed with reasons | Biq Mac: "We do not consider the larger instances in the library due to memory limitations. We also exclude 14 instances for which none of the methods close any gap ... In addition, we remove one instance (bqp50-9)" (S17 §6.2). GMI: 20 MIPLIB instances discarded "due to infeasibility, being very large, or being very difficult"; 48 more "mostly due to the cut collection procedure returning zero cuts, but also due to some memory/time limits and a few numerical errors" (S15 §5.2–5.3). Gas: "In a preliminary study, we concluded that the design problem based on the largest GasLib-4197 network remains challenging to solve with our framework." (S19 §5) | [practice · primary] | 2020–2024 |
| Ideal case first, then the real benchmark, then isolate each difference | Two-row cuts (S9 §4): random "perfect two-row" instances (5) first, then MIPLIB 3.0 ("Note that we did not apply any sophisticated criterion to select MIPLIB instances. We just selected manageable instances"), then designed instances in which "each specific characteristic of the instances ... has been isolated", then "Back to MIPLIB Instances" (§4.5). The same order appears in S10 (random stochastic, then MIPLIB 2010), S13, S14 (random, then MIPLIB 2017) and S21 (random dense instances, then FEM application) | [practice · primary] | 2010–2026 |

### 3.2 How baselines are chosen

- **The strongest available public implementation, made comparable** [practice · primary; S2, S3].
  - Strong SOCP compares with the public SDP package "OPF Solver" and states its limits: "We also note that OPF Solver does not support instances with reactive power cost functions, hence the case9Q and case30Q instances are solved using the standard rectangular SDP formulation." (S2 §5.2.1).
  - In 2017 they edited the competitor's code to match the constraint set: "The OPF Solver code is modified to incorporate the phase angle bounds in NESTA instances by adding the following constraints". They then ran it under two SDP solvers, MOSEK and SDPT3, and reported both (S3 §5).
  - They also benchmark against their own earlier method: "We also compare the three approaches proposed in this paper to our previous paper [27], which utilizes strong SOCP relaxations." (S3).
- **Generic global solver against specialised code, with the asymmetry stated** [practice + stated · primary; S6 §5.1].
  - Pooling: "We experimented with the specialized global solver APOGEE (Misener et al. 2011) for pooling problems but did not observe any performance benefit compared to BARON."
  - BARON got more time, for a stated reason: "it is impossible to know exactly how much time it spent to only find feasible solutions. For this purpose, we gave longer time limits for global optimization." BARON then "was run for 6 hours on the NEOS server", while "FlowAug, SNOPT and our MILPs were given a time limit of 1 hour".
  - A competing heuristic was re-implemented by the authors: "Alfaki and Haugland (2013a)'s heuristic was implemented in GAMS and run on the NEOS server invoking BARON 12.7.3 to solve bilinear subproblems."
  - Tolerances were aligned: "To ensure numerical consistency among the different solvers, we used the following algorithmic parameters".
- **Only the best baseline is tabulated** [practice · primary; S16 v3 §4].
  - "Our conclusion based on our implementation of other algorithms is that when Mosek solves the instance, the best dual bound is obtained from Mosek. For some slightly larger instances, other algorithms might produce dual bounds. Usually, these dual bounds are extremely poor in quality. ... Therefore, we have chosen to present results only from Mosek in Tables 4, 5, 6, 7, 8, 9, 10, 11, 12; and the remaining results are relegated to Appendix J."
- **A ground truth instead of a competitor** [practice · primary; S12, S15].
  - Optimal trees (S12), or an "expert" upper bound (S15); see §2.1.
- **A naive in-house solver on purpose** [practice + stated · primary; S13, S14, S26].
  - In branching studies the main comparison runs inside their own branch-and-bound, not a commercial solver.
  - Learning-enhanced branching: "we did not consider their usage, as they make the analysis of branching rules significantly more difficult" (cutting planes; S26 §4.1).
- **Commercial solvers as reference, sometimes only in a sentence** [practice · primary; S20 §4].
  - Extreme strong branching uses BARON only as a warm start: "we first run the global solver BARON [18] (version 25.3.19) for 60 seconds and pass its best incumbent solution as the initial primal heuristic to our branch-and-bound."
  - On the benchmark QCQPs it does not run Gurobi: "We have not solved these with commercial solvers like Gurobi, as such solvers are highly optimized for standard instances."
  - On the FEM instances it does compare with Gurobi.
  - BARON and Couenne appear without a table: "We have also tested our instances against BARON and Counne [sic] [3], but they did not perform better than the extreme strong branching and achieved only marginal improvements in the lower bounds with their default parameters."
  - [inferred] Baseline reporting is uneven: some baselines are fully tabulated, others are summarised in a sentence.
- **Published methods through existing packages** [practice · primary; S29].
  - The NeurIPS camera-ready adds §5.5, comparing "with the SCCA methods of [10, 37, 41]". The supplement's `SOTA.py` imports `pmd` and `cca_ipls` from the `sparsecca` package, with comments such as `### Implement the algorithm of Witten et al. [41]`.
  - The reported win is partial: "the local search algorithm yields a larger correlation value than these existing methods in 16 out of 22 testing cases".
- **Fair inputs across methods** [practice · primary; S21 §3.6].
  - "For example, reduced bounds are provided to BARON, McCormick relaxation, one-row relaxation and aggregation relaxation."

### 3.3 Controls: how variability and confounders are removed

**SCIP configuration in the IJOC 2026 repository** [practice · primary; S30 `scripts/MIPLIB/get_scip_cuts.py`, `solve_mips.py`]. Code comment: `# Set params to switch off presolve, propogation, heuristics variable permutations, limiting bnb to solve only root node`.
- Cut generation run: `"limits/nodes": 1`, `"randomization/permutevars" : False`, and full strong branching forced with `"branching/vanillafullstrong/priority": 536870911`.
- Tree run:
  - `"conflict/enable": False`, separation off, `setHeuristics(scip.SCIP_PARAMSETTING.OFF)`;
  - `solve_model.setObjlimit(float(objval))`, where `objval` is the MIPLIB optimum.
- Loop: `# Repeat for 3 seeds and upto 10 rounds of cuts`.
- The paper states the aim: "In the absence of dual degeneracy, configuring SCIP to these settings eliminates all sources of performance variability in the number of nodes to the best of our understanding, and enables us to isolate the impact of any change in branching decisions." (S13 §3.2).
- Era: 2024; SCIP 8.0 with PySCIPOpt and Gurobi 10.0.1; a Linux cluster; first author Shah.

**Own branch-and-bound as the instrument** [practice · primary].
- "The experiments were conducted on a Python 3.10-based implementation of the naive branch-and-bound framework to ensure a controlled experiment, unaffected by other sophisticated processes of modern solvers. ... FSB-P was implemented purely as an oracle returning a branching variable, without influencing any other process within branch-and-bound, thus allowing fair node counting [18]." (S13 §3.1).
- Repeated in S14 §1.1.
- The 2022 Julia version, S26 §4.1: "To ensure consistent training data and reproducible experimental results, in this work we implemented, in the Julia programming language, a textbook version of the branch-and-bound algorithm".

**Seeds even when nothing is random** [practice + stated · primary; S14 §5].
- "Every combination of instance, rule and primal gap is solved with 3 different random seeds to account for possible dual degeneracy in the problems, even though our textbook implementations of branch-and-bound algorithm and full strong branching do not use any random processes."
- The feasibility-pump study used "ten different random seeds" and reported seed-by-seed tables (S10 §5.2).

**Isolate the side of the problem being studied** [practice · primary; S15 §5.1].
- "Additionally, since this manuscript focuses on the dual side of the solution process, Gurobi was provided with the optimal solution to all problems during testing."
- Effort is measured in deterministic work units as well as time.

**One round, no cut selection, to see the cuts' own strength** [practice · primary; S9 §4].
- "we decided to evaluate the impact of one round of cuts only".
- Also "without applying any (sophisticated) selection rule" (quoted in note 02, §4.1).

### 3.4 Metrics

- **Percent gap closed is the usual yardstick for cuts** (S9, S17).
  - It is refined by the "relative importance" of each cut family, Imp(X), and the relative standard deviation of gap closed (S9 §4.1).
  - S21 uses a "relative gap improvement" against a named base relaxation.
- **Ratio to a reference bound.**
  - "'ratio' is defined as the lower bound of an SOCP relaxation divided by that of the SDP relaxation" (S2 §5.2.1).
  - The sparse-cut theory is stated as bounds on the ratio of the cut bound to the optimum (S11).
  - Percent gap uses BARON's best relaxation bound (S6 §5.3).
- **For trees**:
  - the ratio of geometric means to the optimal tree (S12 §6.2): "The overall geometric mean of optimal tree size of instances across all problems is 42.65, whereas the same for SB-L, SB-P, most infeasible branching and random branching is 61.47, 61.09, 90.19 and 145.37 respectively.";
  - shifted geometric means with stated shifts (S10, S14);
  - remaining gap at a node limit of 20,000 for unsolved runs (S14 §5).
- **Performance profiles plus breakdown by size.** Profiles are followed by a breakdown by instance size, because the aggregate hid a size effect. For BARON's solutions in pooling: "As the value of n increases (n [≥] 30), the performance of BARON deteriorates." (S6 §5.3).
- **Deliberately not run time** in one study: "We do not focus on total running time since this metric depends heavily on the quality of the software implementation, instead of simply on the fundamental properties of the branching rule." (S26 §5). Contrast Contradiction 5.

### 3.5 Implementation stack and compute, by period

"Coded by" is [inferred] from first authorship unless the record says who wrote the code.

| Years | Paper(s) | Stack (as stated) | Compute (as stated) | Coded by |
|---|---|---|---|---|
| 2010–2012 | Two-row cuts (S9) | "The code has been implemented in C++, using IBM ILOG Cplex 10.0 as LP solver." | not stated | not stated (four-author team) |
| 2013–2015 | Pooling (S6) | AMPL for SLP and AltLP; GAMS on NEOS; Cplex 12.2 "run in single-threaded mode"; BARON 12.7.3 on NEOS | "a Linux machine with 64-bit x86 processor and 32GB RAM" plus the NEOS server | Gupte [inferred] |
| 2014–2017 | OPF line (S1–S5) | "The code is written in C# language and Visual Studio 2010 is used as the compiler." MOSEK 7.1 and later 8; CPLEX 12.x; IPOPT; BARON | Intel Core i5 3.33 GHz with 4 GB RAM (2014); laptop Core i7 2.00 GHz with 8 GB (2015); Core i5 2.50 GHz with 16 GB (2017) | Kocuk [inferred] |
| 2014–2016 | Sparse cuts (S11) | "All the experiments have been carried out using CPLEX12.5." | not stated | Q. Wang [inferred] |
| 2016–2017 | Feasibility pump (S10) | "The code is based on the current version of the Feasibility Pump 2.0 code (the one available on the NEOS servers), which is implemented in C++ and linked to IBM ILOG CPLEX 12.6.3" | "a cluster of identical machines, each equipped with an Intel Xeon CPU E5-2623 V3 running at 3.0GHz and 16 GB of RAM"; half-hour limit | built on co-author Salvagnin's FP code [inferred] |
| 2018 | BBP (S8); rank-one pooling (S7) | "We call MOSEK via CVX from `MATLAB R2015b` to solve SDPs." Gurobi 7.5.1; BARON 15.6.5 called from MATLAB. Generalized-pooling instances shipped as Python pickles (S42) | Windows 10, 2.19 GHz, 32 GB RAM | Santana [inferred] |
| 2018–2021 | Sparse PCA (S16) | Gurobi 7.0.2; Mosek 8.0.0.60 | "MacBookPro13 with 2 GHz Intel Core i5 CPU and 8 GB 1867 MHz LPDDR3 Memory" | G. Wang [inferred] |
| 2020–2022 | Sparse-PCA cuts (S17) | C++, Eigen 3.3.7, Gurobi 9.0, MOSEK 9.2 Fusion API | "Most of the reported results used nodes from the Béluga cluster of Calcul Québec"; a 512 GB shared server | Montreal co-authors' resources [inferred] |
| 2021–2022 | Bilinear covers (S18); learning-enhanced branching (S26) | Python 3.9.7 with Gurobi 9.5.0 (`NonConvex=2`). Julia textbook B&B with scikit-learn via PyCall.jl | the ISyE cluster, "roughly 2,340 cores"; training runs capped at "roughly 2 weeks, due to server limitation" | Gu [inferred] |
| 2023 | Gas networks (S19) | "The framework is coded in Python with Pyomo." Gurobi 9.5.1 chosen after BARON 22.9.1, SCIP 7.0.1 and MOSEK 9.3.10 "tend to be slower" | "Intel i7 CPU (4.20GHz) with 16 GB RAM" | Y. Li [inferred] |
| 2024–2025 | Branching (S13, S14) | Python 3.10 own B&B, Gurobi 10.0.1, SCIP 8 / PySCIPOpt | Linux cluster | **Shah** (commits, S30, S34) |
| 2024 | GMI history (S15) | Julia/JuMP inside MIPLearn; Gurobi 11.0.2 single-threaded, 16 runs in parallel | "a single workstation computer (Ryzen 9 7950x, 16 cores, 32 threads, 128 GB DDR5)" | Becu, with Argonne co-authors [inferred] |
| 2024–2025 | Bipartite bilinear aggregation (S21); extreme strong branching (S20) | Julia 1.7 or 1.11; B&B built on Kim's `BranchAndBound.jl`; Gurobi 10.1; HiGHS 1.11.0; Ipopt 3.14.17; BARON 24.5.8 and 25.3.19 | "a personal laptop with a Windows 64-bit operating system with a 1.8GHz processor and 16GB RAM"; "a personal MacBook Air equipped with an Apple M3 chip (8-core CPU) with 8 gigabytes of RAM" | **Han** (commits, S31, S35) |
| 2024 | Sparse CCA (S29) | Python; `sparsecca` package for the baselines | not checked | first author Yongchun Li; "undergraduate researcher Quill O Healey for his help with the initial version of branch-and-bound codes" (camera-ready acknowledgements) |
| 2026 | Eigen-CG (S23) | Python 3.11.4, Gurobi 12.0.1, MOSEK 11.0.14 | Xeon Gold 6258R, "up to four threads" | not stated |

Reading [inferred]:
- Evidence never rests on large compute. The biggest machines named belong to the department cluster or to co-authors.
- Commercial solvers are subroutines. When the object of study is the solver's own logic, the solver is replaced by in-house code.

### 3.6 Code and data release

**Homepage: data yes, code no** [practice · primary; S44].
- The publication page has 7 "instances" or "data" links and no link labelled code or software. The same page carries 107 "pdf", 96 "doi", 26 "slides" and 3 "video" links.
- Each archive belongs to one paper:

| Archive | Paper |
|---|---|
| TreeLibrary.zip (S37) | Radial OPF library (S1) |
| SwitchInstances.zip (S38) | DC switching (S5) |
| AkshayStandardAMPL.zip (S39) | Pooling (S6) |
| BBP_instances.zip (S40) | BBP (S8) |
| InstancesAndResultsWFP.zip (S41) | Feasibility pump (S10). Holds two result spreadsheets, `DetailedMIP2010Results.xlsx` and `DetailedStochasticResults.xlsx` (not opened), as well as an instance archive |
| Random_GPP_instances.zip (S42) | Rank-one pooling (S7). Holds a README, plus txt and pickle files |
| txt_form_data.zip (S43) | Sparse PCA (S16) |

- Formats follow the student's tools: MATPOWER `.m`, AMPL `.dat`, Python pickle, text.
- **Timing.** The server's Last-Modified dates, checked live, put three archives within days of the arXiv v1. The header shows the last change, not first posting.

| Archive | Last-Modified | arXiv v1 |
|---|---|---|
| BBP_instances.zip | 27 Mar 2018 | 25 Mar 2018 |
| Random_GPP_instances.zip | 3 Feb 2019 | 2 Feb 2019 |
| txt_form_data.zip | 22 Oct 2018 | 22 Oct 2018 |

**Code appears where the venue requires it** [practice · primary; S30–S32].
- Three IJOC papers have repositories in the journal's GitHub organisation and Crossref "Code and Data Repository" DOIs:
  - 10.1287/ijoc.2024.0709.cd
  - 10.1287/ijoc.2024.0771.cd
  - 10.1287/ijoc.2022.0326.cd
- The template file left in one repository describes the mandate: "Once your paper enters the review process, either the Area Editor or the Editor-in-Chief will create a private repository from this template" (S32 `TODO.md`).
- No such repository or `.cd` DOI exists for three other IJOC papers:
  - 2019.0924 (scenario grouping, 2020);
  - 2022.1178 (relay attack, 2022);
  - 2022.0230 (bilinear covers, 2024).
  The record does not say whether those papers fell under the policy.
- Commits:

| Repository | Commit authors | AUTHORS file |
|---|---|---|
| S30 | Prachi Shah; `odow`, `astevenson-informs` | Shah, Dey, Molinaro |
| S31 | Dahye Han; `odow` | Han, Jiang, Dey, Xie |
| S32 | Álinson S. Xavier; `pascalvanhentenryck` (merge) | Xavier, Qiu, Dey |

- **No commit by Dey appears in any repository examined** [practice · primary; Gap].

**Students also publish code themselves** [practice · primary; S34–S36].
- `handahye/esb` was created 27 Oct 2025, four days after arXiv:2510.20650. Its README lists "Julia (1.11.7)", "BARON (25.3.19)" and "Gurobi (12.0.1)", and it ships the FEM instances.
- `handahye/aggregation_bbe` (Sep 2024) holds instances and the formulation only.
- `prachi-shah-opt/BinaryBNBPy` (Sep 2024): "Python-based implementation of binary MILPs including advances made in my thesis." It contains a shared `BranchAndBound/` package, `OptimalTrees/opt_bnb_tree.py` and the non-monotonicity scripts.

**Other channels.**
- The NeurIPS 2024 paper put "necessary codes and data" in a supplementary zip (S29, checklist). The zip holds 20 Python source files (not counting macOS metadata copies), 8 datasets and a separate `BaCtree/sccapy` branch-and-cut package.
- A 2016 co-author repository (S33, Huchette's) has one script per table and figure (`Table-1.jl` … `Figure-4.jl`) for Julia 0.4, JuMP 0.11 and CPLEX.

**Reproducibility limits in the released material** [practice · primary; S30].
- The generator's seed line is commented out: `# np.random.seed(0)`.
- The 100 random knapsack instances are not in the repository; only `results.pkl` is.
- The student's own repository removed them on 10 Sep 2024 (commit "Delete NonMonotonicity/MultiKnapsack/instances directory", S34).
- [inferred] The knapsack experiment can be re-run in kind, but not reproduced exactly.

### 3.7 Debugging and sanity checks

| Check | Evidence | Source |
|---|---|---|
| Check against the known optimum inside the code | `if not(root.int_feasible or abs((self.branching_stats.dual_bound - self.branching_stats.known_opt)/self.branching_stats.known_opt) < 1e-4):` prints the instance and bounds. An earlier hard `assert` against the known optimum is left commented out | [practice · primary] S30 `src/branch_and_bound.py` |
| Check solver output and drop the solver that fails | "We also discovered that Gurobi at times returns solutions with large constraint violations for this MINLP formulation. As a result, we focused on SCIP and BARON and we report the results on solving the MINLP formulation with BARON, which performed better in our tests." | [practice · primary] S19 §5.3 |
| When the reference tool fails, reformulate | MATPOWER "fails to solve the remaining seven instances due to numerical issues". BARON was used instead: "We should note that performance of BARON on rectangular formulation (1) is very poor as it requires hours to prove global optimality. Instead, we use reformulation (2), which is valid for radial networks." | [practice · primary] S1 §5.2 |
| Watch the algorithm's behaviour and change the code | "and then we realized that adding one cut per iteration we were solving far too many [mis-heard in captions as 'algebras'] all right and and and this was becoming expensive so what we did is we revisited both the codes uh and and we started adding multiple sparse [cuts]" | [stated (spoken) · primary] S46, about 00:19:15 |
| Numerical trouble is recorded, not hidden | "on three instances we observed numerical issues during the benchmark procedure after cut collection" (instances listed in a table) | [practice · primary] S15 §5.3 |
| Exact arithmetic where floating point cannot certify | "the reader can verify this claim computationally using exact arithmetic based on the values provided" | [practice · primary] S22 §4 |

### 3.8 Preliminary experiments: what was tried, and what was kept or dropped

| What was tried | Outcome, in the paper's words | Source |
|---|---|---|
| The theoretically motivated WalkSAT perturbation (WFP) | "In preliminary tests, we implemented the algorithm WFP ... However, its performance was not competitive with FP. In hindsight, this can be justified by the following reasons". Replaced by "a more conservative implementation of a perturbation procedure inspired by WalkSAT, which we denote by WFPb" | S10 §5.1 |
| APOGEE instead of BARON | "did not observe any performance benefit compared to BARON" | S6 §5.1 |
| Warm-starting SNOPT | "We did not observe much benefit to warm-starting SNOPT and ran it without any initial values." | S6 §5.1 |
| Tuning CPLEX symmetry handling | "we did not find any obvious benefit of tuning the symmetry parameter in Cplex" | S6 §5.1 |
| A row-wise extended relaxation | "we empirically observed that such a relaxation is consistently weaker and hence omitted from further discussion" | S7 §3 |
| More tangent cuts | "More tangent lines could be added to better approximate conv(S0), but based on our preliminary experience on our instances it does not make significant difference." Also "Our implementation is naive, and we have not tried to fine tune any of these parameters." | S8 §5 |
| LP algorithm for the cut loop | "We conducted extensive preliminary experiments to determine which strategy to choose, and concluded that Barrier always performs better", for both sparse and dense cuts (the sentence continues after a page break) | S17 §6.1.1 |
| Gas: the valve block, the time limits, and the largest network | "Our preliminary studies suggest the use of Valve nl block for valves." "We performed studies to extend the time limit to longer than 10 min and the improvement on the ... returned value is not significant." GasLib-4197 was excluded (§3.1) | S19 §4–5 |
| The expensive branching oracle | "Due to the significant computational cost of RB:100:inf, we omit this method in the following experiments." | S26 §5 |
| Strengthening a weak branch-and-cut variant | "Also, we can see that SEP(S) method is able to provide lower average optimality gap than SEP(M, S) at the end since it processes more nodes." The cheaper separation wins under a time limit | S3 §5 |

[inferred] Negative preliminary results are typically reported in one or two sentences, with the reason when it is known. Tuning effort is admitted to be low ("naive", "not tried to fine tune").

---

## 4. Layer 5: judging results and answering criticism

### 4.1 Mixed and negative outcomes are put in the text

- **OPF cuts sometimes slow BARON down** (S1 §6.2).
  - "For the 9-bus instances (case9, case9Q), BARON's computation time reduces slightly with the addition of cuts. However, the preprocessing time dominates the total computation time, which is larger than the case without cuts."
  - "On the other hand, cuts slightly increases the total computational time in the case of quadratic objective."
- **Their own method loses on harder gas instances** (S19 §5.3).
  - "For the larger stress levels, the framework returns larger gaps."
  - When the method was weak, they combined it with the baseline rather than hide it: "we decide to run BARON for 45 minutes before the binary search phase ... and we report the better lower bound".
- **A preprint reports a finding against its own premise** (S27 v3, abstract and §4).
  - The method "relies on the insight that, for routine operations on a fixed network, the DCOTS solutions for similar load profiles and generation cost profiles will likely turn off similar sets of lines".
  - The results say: "Surprisingly, the best solutions do not tend to be among the closest, with the exception of the 300kocuk case with cardinality 5." (Contradiction 4).
- **Two-row cuts: the verdict is negative and stated** (S9 §1.1, §5).
  - "our initial goal was to show that a small subset of two-row cutting planes ... could, together with one-row cuts, be useful in closing a significant amount of gap for general MIPs. However such a goal was too ambitious and we have had to considerably restrict it."
  - "the experiments in this paper suggest that type 2 triangle cuts are not competitive with split cuts".
- **Warm start does not matter** (S2 §5.2.2). "We observed empirically that independent of the relaxation we use, the method always converges to the same OPF solution."
- **"Preliminary" is kept in the abstract after revision** (S24). Both v1 (Dec 2023) and v2 (May 2025) end with "we present preliminary computational results on sensitivity analysis for MBQPs".

### 4.2 Claims corrected between versions

| Paper | Earlier version | Later version | Note |
|---|---|---|---|
| Strong SOCP (S2) | v1, 25 Apr 2015, §4.1 "A New Cycle-based Formulation of OPF": "This is an exact reformulation of the AC OPF problem." Prop. 4.3: "is a correct bilinear extended formulation of OPF". Abstract: "One of these relaxations is based on a new bilinear extended formulation of the OPF problem." | v4, 31 Oct 2015, §4.1 "A New Cycle-based Relaxation of OPF": "we consider a relaxation that guarantees angle differences sum up to 0" modulo 2π over every cycle. Prop. 4.3: "define a valid bilinear extended relaxation of OPF (2)-(3)". The abstract sentence is deleted | [practice · primary]. No version comment on arXiv and no erratum (Crossref). The reason is not stated anywhere I read. The headline numbers in the abstract (99.96%, 0.13%, 157.20 s) are unchanged |
| OPF inexactness (S1) | v1, 4 Oct 2014, abstract: SDP relaxation "is exact in the absence of generation lower bounds" | v3, 18 Dec 2014, abstract: "is exact under technical conditions such as not including generation lower bounds or allowing load over-satisfaction". The paper grew from 6,498 to 7,894 words, with a longer literature account | [practice · primary]. The characterisation of others' work was made more precise. Title also shortened (note 01, Contradiction 6) |
| Sparse PCA (S16) | arXiv:1712.00800 (Dec 2017), a theory-only ℓ0/ℓ1 constant-factor note of 6.7k words, never published as such | arXiv:1810.09062 v1, Oct 2018, "A convex integer programming approach for optimal sparse PCA" (12.7k words, with experiments). Then v3, Aug 2021, "Using ℓ1-relaxation and integer programming to obtain dual bounds for sparse PCA" (15.7k words). Oper. Res. 2022 | [practice · primary]. A theory result was folded into a method-plus-experiments paper and retitled to name its contribution (dual bounds) |
| Gas networks (S19) | v1, Jul 2023, "A decomposition framework for gas network design". Abstract: "We conduct experiments on a benchmark network". The text uses only Gaslib-582 | v3, Jan 2024, "A reformulation-enumeration MINLP algorithm for gas network design". Abstract: "We conduct experiments on benchmark networks". GasLib-11, -24, -40, -134 and -582, plus BARON comparisons on MINLP formulations | [practice · primary]. Scope widened. The reason, probably review, is not documented [inferred] |
| B&B on random IPs | v1 covered packing IPs; v2 covered general binary IPs (note 01 §1.10). The thesis says the journal version "significantly simplified the proofs" (note 04 H8) | | [practice · primary], cross-reference |

### 4.3 How referees are answered (no reviews could be read; this is the authors' side only)

- **Run the experiment the reviewer asked for, and credit it** [stated + practice · primary; S5 v3].
  - "We would like to thank the reviewers for their constructive comments and in particular suggesting the experiments in Section 6.3. These have helped in significantly improving the paper."
  - §6.3 "Sensitivity Analysis" does not exist in v1 (Dec 2014). It was used to explain a surprising result: optimal solutions switch off far more lines than earlier studies, a "surprising result [that] is a consequence of our observation that there are many optimal or near-optimal topologies for the DC-OTS."
- **Turn an objection into named future work** [stated · primary; S5 v3, Conclusions].
  - "As an example of studying more complicated substructures, one reviewer observed that the substructure we study does not involve flow balance constraints. Stronger relaxations could be obtained by separating cutting-planes using an extended formulation similar to (14) that includes flow balance constraints."
- **Explain large gains with a small worked case** [practice · primary; S4 v3].
  - The AC switching paper gained §6.3 "Discussion" between v1 (Oct 2015) and v3 (Feb 2016). It takes "a closer look at some of the instances with large cost benefits" on the 6-bus case and compares with "a commonly used heuristic based on switching the best line".
- **Generic thanks elsewhere** [stated · primary].
  - "We would like to thank the anonymous reviewers for their constructive comments that significantly improved the presentation of this paper." (S16 v3).
  - "The authors thank the two anonymous referees whose suggestions improved the quality of the paper." (S25 v2).
- **Benchmarks widened late in the cycle** [practice · primary; S27, S29].
  - kNN: v1 (Mar 2020) has "a case study on the IEEE 118 bus system, the 1354 bus PEGASE system, and the 2869 bus PEGASE system"; v3 (May 2021) has "a case study on 7 test networks ranging in size from 118 to 3,375 buses".
  - Sparse CCA:
    - The NeurIPS camera-ready reorders the sections and adds "5.5 Experimental comparison of SCCA algorithms", which is absent from arXiv v1 (Dec 2023).
    - In the supplement, `SOTA.py` carries a file date of 2024-10-30, while the other code files are dated May 2024.
    - [inferred] The comparison with existing methods was added late, plausibly in answer to reviewers. The reviews themselves could not be read (Gap).

### 4.4 Numerical evidence and proof

- **Prefer a rigorous, simple bound over a tighter numerical one** [practice + stated · primary; S22 §4].
  - "While this can be verified numerically (see Figure 2) using a general-purpose solver, the non-convex nature of the set can impair solvers in certifying global optimality. For this reason, we provide a more analytical proof sketch of this claim which involves exact calculations."
  - "We remark that the bounding box [-8, 8]^3 is by no means optimal. Our numerical experiments indicate that it is actually [-1.23, 1.23]^3. We just focus on a box whose validity proof is simple and rigorous." (The extraction flattened the superscript 3, written here as ^3.)
- **Computational facts are re-proved without numerics where they matter** [practice · primary; S23].
  - "These different proof strategies can actually be used to show, without relying on numerical methods, that the aforementioned 113,088 facets are not Eigen-CG."
- **Limits of the small-instance evidence are written down** (cross-reference note 02 §4.1: the strong-branching "word of caution" on "up to 20 binary variables").
  - The same limit drove instance selection (S45; §3.1).

### 4.5 Selection transparency, and its limit

- **Stated.**
  - "for succinctness we report on only these three instances" (S17).
  - "These instances have been selected to cover different patterns observed and the results for all others are included in Appendix A." (S13 §3.2).
  - "While the proposed rule was tested on a diverse set of QCQP instances, it proved especially effective for BBPs such as pooling problems and water management problems, which are the primary focus of our computational analysis." (S20 §4.1).
- **Limit** [inferred]: in S20 the reported benchmark set is the class where the new rule works best. The paper says so, but the other classes are not reported.

---

## 5. Layer 6: expression (papers and versions)

**Results before proofs.** Many papers put all results in an early section before any proof [practice · primary]:
- "2 Main results" (S16; S22; S24 v1);
- "1.2 The nature of results obtained in this paper" plus "2 Main results" (S11);
- "2. Overview of Results" (S6);
- "2 Our results" (S8);
- "2 Main results" with "2.1 Theoretical results" and "2.2 Computational results" (S12).

**A fixed template for computational sections** [practice · primary]:
- software and hardware;
- instances, with the generator described;
- methods compared, with labels;
- results;
- a closing summary (for example "4.4 Summary of enumeration experiments", S17; "4.7 Conclusions and summary of numerical experiments", S16).

**arXiv as announcement, homepage as archive** [practice · primary; S51, S44].
- Of 56 arXiv records with a published version, 29 were never updated after v1 and 27 were.
- Four of Kocuk's five power-systems preprints were updated up to v3 or v4. The fifth (arXiv:1703.03050) was not.
- The homepage sometimes hosts the preprint rather than the revised paper. The non-monotonicity PDF on the homepage matches arXiv v1 (6,859 words in v1, 6,854 in the homepage PDF), not the IJOC 2026 text.
- [inferred] Readers of the free versions may meet superseded text. Contradiction 1 shows that this matters.

**Conference first, journal second** [practice · secondary data (DBLP), primary versions]:
- "Experiments with Two Row Tableau Cuts" (IPCO 2010, doi:10.1007/978-3-642-13036-6_32) became IJOC 2014 (doi:10.1287/ijoc.2013.0559);
- SODA 2021 (doi:10.1137/1.9781611976465.35) became Math. Program. 200, 2023 (doi:10.1007/s10107-022-01895-4);
- IPCO 2021 (doi:10.1007/978-3-030-73879-2_11) became Math. Program. 197, 2023 (doi:10.1007/s10107-021-01759-3);
- IPCO 2024 (doi:10.1007/978-3-031-59835-7_33) became Math. Program. 216, 2026 (doi:10.1007/s10107-025-02265-6).
- Note 04 H8 has students describing the journal versions as rewritten, with new results and redone experiments.

**Retitling is common.** These preprints were retitled before or at publication [practice · primary]:
- rank-one sets (S7);
- sparse PCA (S16);
- gas networks (S19);
- B&B on random IPs (note 01).

**Self-reports in a checklist** [stated · primary; S29, NeurIPS checklist].
- Error bars: answer "[No]", justified as "The paper focus on solving an optimization problem with deterministic data and evaluates the optimality performance of the algorithms. Hence, the paper does not include error bars or other statistical significance measures of the experiments."
- Limitations: answered by pointing to the discussion of each table in §5.

---

## 6. Layer 7: organisation (who does what, shared assets)

**The first author codes; Dey's name is in the AUTHORS file, not in the commits** [practice · primary; S30–S32, S34, S35; §3.6].
- The NeurIPS paper credits an undergraduate with the first branch-and-bound code (S29).
- Dey names a student as the intellectual lead in public: "really the thought leader for a lot of what I'm presenting is [Jingye Xu] who's a PhD student uh in his third year" (S49, about 00:04:43).

**One student's testbed spans several papers** [practice · primary; S34].
- `prachi-shah-opt/BinaryBNBPy` holds one shared `BranchAndBound/` package plus `OptimalTrees/` and `NonMonotonicity/`.
- The initial commit (9 Sep 2024, 3,113 files) also held `ImprovingStrongBranching/` (with `grb_presolve.py`) and `LearningFromOptimalTrees/` (with `feature_collection.py`). Both were deleted the same day.
- [inferred] The full strong-branching paper (S12, Math. Program. 2024), the non-monotonicity paper (S13) and the strong-branching follow-up (S14) ran on one evolving codebase.

**Assets are reused across students and groups** [practice · primary].
- An instance named after a former student appears in a later student's preprint: "the 300kocuk case" (S27; compare note 04 H3).
- Public generators and instances from other groups are reused:
  - Burer's BoxQP generator (S17);
  - Alfaki and Haugland's generalized-pooling recipe (S42);
  - generators labelled "Gasse et al" (S30);
  - Kim's `BranchAndBound.jl` (S20, S21);
  - Argonne's MIPLearn and UnitCommitment.jl through the Argonne co-authors (S15, S26, S32).
- Benchmark data was obtained by asking the author directly: "We wish to thank Dr. Carleton Coffrin of NICTA for providing us NESTA 0.3.0 archive. We really appreciate his prompt help in this matter." (S2, Acknowledgments).

**Implementation follows the collaborator** [inferred, from §3.5].
- C++ with Eigen on a Canadian cluster with Montreal co-authors (S17).
- MIPLearn and Julia with Argonne co-authors (S15, S26).
- FP 2.0 with its author (S10).

**Classic algorithms are re-implemented as comparators** [stated (spoken) · primary; S49].
- "we implemented this algorithm by [Shabbir] which is like scenario decomposition" (about 00:46:06).
- Then: "We ran [Gurobi] on these instances for about an hour and a half. the [gap] was about 9%." (about 00:53:33).

---

## 7. Failures, abandoned directions, rejected and retracted work

| Item | What the record shows | Tag · source |
|---|---|---|
| Retracted claim | The Strong SOCP "exact reformulation" was downgraded to a "relaxation" between arXiv v1 and v4 (§4.2). Not announced. The paper went on to win the INFORMS ENRE award (note 01) | [practice · primary] S2 |
| Scope cut | Two-row cuts: "such a goal was too ambitious and we have had to considerably restrict it" (§4.1) | [stated · primary] S9 |
| Failed design kept in the paper | WFP "was not competitive with FP" and was replaced by WFPb (§3.8) | [stated · primary] S10 |
| Superseded preprint | arXiv:1712.00800 (Dec 2017, v1 only) was absorbed into arXiv:1810.09062 (§4.2) | [practice · primary] S16 |
| Preprints with no published version found (DBLP, Crossref and Semantic Scholar, 2026-10-10) | arXiv:2003.10565, kNN heuristic for DC switching: v1 Mar 2020, v3 May 2021, student-led (Johnson), later reports the surprising null finding (§4.1). arXiv:2208.10028, learning-enhanced branching: v1 only, Aug 2022 (Gu). arXiv:2302.07415, kernel two-sample tests: four versions from Feb 2023 to Dec 2024 (sizes 4.3 MB, 6.9 MB, 2.6 MB, 2.5 MB); v1's "Experimental results demonstrate good performance of our framework" becomes v4's "Experimental results on synthetic and real datasets demonstrate the superior performance of our method". arXiv:2411.15090 (GMI history, Nov 2024) and arXiv:2507.09455 (Jul 2025) are also unpublished, but recent | [practice · primary] S26–S28, S51–S54. Whether any was rejected is **not** documented |
| Unreleased line | `LearningFromOptimalTrees/` (branch-and-bound plus feature collection) existed in the student repository's first commit and was deleted the same day (S34). The 2025 thesis lists the idea as future work: "It would be interesting to see if one can use machine learning techniques to learn from the optimal branch-and-bound trees." (S45, ch. 4). No arXiv record on it exists | [practice · primary]; outcome unknown [inferred] |
| Dropped baselines, variants and instances | APOGEE, SNOPT warm starts, CPLEX symmetry tuning, a row-wise relaxation, extra tangent cuts, GasLib-4197, Biq instances over n = 250, RB:100:inf (§3.1, §3.8) | [practice · primary] |
| Errata and retractions | None. Crossref's `updates` filter returned no correction, erratum or retraction notice for any of 116 DOIs (DBLP 104, ORCID-linked extras, IEEE, Optim. Eng. and the IJOC code DOIs). No arXiv record is withdrawn; the only arXiv comments about changes are "Revision" (arXiv:1605.06686, four versions 2016–2019) and "Hardness proof has been simplified. Accepted for publication at Discrete Optimization" (arXiv:1809.10787) | [practice · secondary] S51, S53 |
| Rejections | Not observable. OpenReview (the NeurIPS 2024 forum) was blocked by a browser challenge | Gap |

Relation to other notes:
- Note 04 found "no rejected papers, retractions or abandoned group projects documented in the 17 theses or on his pages".
- The repository history (S34) and the version history (S2) add one unreleased code line and one silently retracted claim.
- This refines that finding and does not contradict its scope (theses and pages).

---

## 8. Said against done (cross-check with note 02)

| Note 02 belief | What practice shows | Verdict |
|---|---|---|
| R7: controlled studies, one factor at a time; random instances first, then MIPLIB | Confirmed in code: SCIP switches, objective limit at the optimum, seeds, own branch-and-bound (S30). The same order holds across 2010–2026 (§3.1) | Consistent. But the released knapsack generator does not match the stated distribution (Contradiction 2) |
| R9: methods must survive real solver engineering; count all overheads | Feasibility pump built inside FP 2.0 (S10). The GMI study charges all preprocessing to the method ("time includes not only the time Gurobi requires to solve the problem, but also the additional time spent predicting multipliers...", S15 §5.4). Branching studies deliberately leave the solver; one preprint declines to time its method and calls the saving "self-evident" (S26) | Partly. The isolation rationale is stated, so this is a tension rather than inconsistency (Contradiction 5) |
| R4: dual bounds and certificates matter | OPF certifies "within 0.13% of global optimality" (S2). SPCA's subject is dual bounds (S16). Pooling gaps use BARON's relaxation bound (S6). The GMI study gives Gurobi the optimum to study only the dual side (S15). ESB reports remaining optimality gap (S20) | Consistent |
| R8: say plainly what is not known, what is weak, what failed | Done inside papers (§4.1, §3.8). Not done for the Strong SOCP claim change (§4.2) | Mostly consistent, with one silent correction |
| R2: real instances are sparse and structured | Sparse generators "inspired by" Crowder–Johnson–Padberg (S18). Homogeneous perturbed MIPLIB families (S15). Daily-operations SCUC instances (S26) | Consistent |
| R5: data-independent measures, tight bounds | Gap closed, ratio to the SDP bound, ratio to the optimal tree (§3.4) | Consistent |
| Not stated anywhere I found | Release instance libraries with the preprint; make competitors' code comparable; give the generic solver longer time and say so; tabulate only the strongest baseline | Practice without a matching statement [inferred] |

---

## 9. Era and resource context (summary)

**2010–2015.**
- Commercial solvers are licensed on single machines or reached through NEOS: CPLEX 10–12, BARON 12, MOSEK 7.
- Code is in C++, C# and AMPL/GAMS, depending on the student.
- Instance libraries are posted as zip files on the homepage.
- MIPLIB 3.0 is the benchmark (S9), followed by MIPLIB 2010 in 2016 (S10).

**2016–2021.**
- MATLAB with CVX and Python start to appear.
- Gurobi 7–9 replaces CPLEX in most studies.
- A co-author's cluster is used when SDPs are large (S17). Otherwise a single desktop or laptop is enough (S8, S16).

**2022–2026.**
- Python and Julia only. Open-source pieces appear: HiGHS, `BranchAndBound.jl`, PySCIPOpt, MIPLearn, `sparsecca`.
- MIPLIB 2017 is the benchmark.
- IJOC mandates repositories.
- Students keep their own GitHub repositories.
- A laptop (MacBook Air M3, 8 GB) suffices for the October 2025 preprint of an Operations Research Letters paper published in 2026 (S20).

**Throughout.** The group never relies on scale. The binding constraints it names are memory for SDPs and the exponential cost of exact optimal trees, not CPU hours (S16, S17, S45).

---

## Contradictions (kept, not reconciled)

1. **Exact reformulation against relaxation (S2).**
   - arXiv:1504.06770v1 calls the cycle-based model "an exact reformulation of the AC OPF problem" and "a correct bilinear extended formulation of OPF".
   - v4 and the homepage version (15 Dec 2015) call it "a valid bilinear extended relaxation".
   - Both versions remain public on arXiv.
   - No document I found explains the change.
2. **Stated instance distribution against released code (S13 against S30).**
   - The preprint (§3.1): "Weights aij are independent and set to 0 with probability 0.25, else uniformly picked from the set {1, . . . 1000}. ... Prices ci are independently picked from the uniform distribution on the interval [0, 1)."
   - The released driver calls `problem = "PackingIP"`, whose generator draws `weights = np.random.randint(1, 10 * n, (p, n))` and `values = np.random.randint(1, 10 * n + 1, n).astype(float)`: integer prices, and weights up to 199 for n = 20.
   - A sibling function `ContPackingIP` in the same file uses `np.random.random(n)` for prices and weights scaled to 0–1000. It matches the text, but the driver does not call it.
   - The final IJOC text was not read and may describe the instances differently.
3. **Protocol against released results (S13 against S30).**
   - The preprint: "Every instance and seed combination is solved 11 times, while the upper limit on the rounds of cuts is increased from 0 to 10."
   - The released `results/MIPLIB/results.txt` has 664 rows for the 21 instances, where 693 are expected (21 × 3 seeds × 11):
     - 17 instances have all 33 rows;
     - `glass4` has 9;
     - `n5-3` has 30;
     - `markshare_4_0` and `mik-250-20-75-4` have 32 each.
   - Neither the README nor the preprint explains the missing runs.
4. **Premise against finding in the same preprint (S27).**
   - The abstract's "insight" is that similar load and cost profiles "will likely turn off similar sets of lines".
   - The results: "Surprisingly, the best solutions do not tend to be among the closest".
   - The preprint remains unpublished.
5. **Counting overheads (S15 against S26), both with Argonne co-authors Qiu and Xavier.**
   - 2024: time "includes not only the time Gurobi requires to solve the problem, but also the additional time spent predicting multipliers, converting the test problem to standard form, computing multiple tableaux, and generating cuts".
   - 2022: "We do not focus on total running time since this metric depends heavily on the quality of the software implementation" and "It is also self-evident, in our opinion, that all evaluated ML-based branching rules, if carefully implemented, would require significantly less computational effort per node than strong branching".
6. **Treatment of variability (S14 against S29).**
   - Three seeds "even though our textbook implementations ... do not use any random processes" (2025).
   - "[No]" error bars because the data are "deterministic" (NeurIPS 2024).
   - These are different settings, kept as stated.
7. **Free versions against final versions.**
   - The homepage PDF of the non-monotonicity paper is the arXiv v1 text, while the IJOC 2026 version is the record.
   - 29 of 56 published arXiv records were never updated.
   - A reader of the free text can therefore meet a version that differs from the journal's. Contradiction 1 shows this can matter.
8. **Record metadata.**
   - arXiv lists DOI 10.1137/18M1210812 for arXiv:1902.00739.
   - Crossref resolves that DOI to Kocuk and Morán, "On Subadditive Duality for Conic Mixed-integer Programs" (SIAM J. Optim. 2019).
   - The paper's real version is J. Glob. Optim. 77 (2020), doi:10.1007/s10898-019-00844-4. Note 02 also recorded this.

## Gaps

- **Reviews and rebuttals.**
  - The only OpenReview forum found (NeurIPS 2024, id MZ47wPr6C3) returned "ChallengeRequiredError" from the API and a browser-verification page through WebFetch. **Not read.**
  - I found no other public review or rebuttal (one WebSearch, no hits).
  - How Dey answers referees is therefore seen only from the author side: acknowledgments and version differences.
- **Final journal texts.** Most final journal texts are paywalled and **not read**: IJOC 2026 ×2, Oper. Res. 2015 and 2016, MPC 2018, IEEE TPWRS, JOGO.
  - The version comparisons use author-posted versions.
  - The final IJOC text may resolve Contradictions 2–3.
  - The IPCO 2010 two-row paper was read as an abstract only.
- **Code before 2024.**
  - No public code exists for the OPF line (C#), pooling (AMPL/GAMS), sparse PCA, sparse-PCA cuts or the feasibility pump. Only their data archives were inspected.
  - The NeurIPS supplement and student repositories were **listed and partly read, never executed**.
- **Dey's hands-on role.** No commit by Dey appears in any repository examined. Whether he writes code, runs experiments or only designs them is not documented.
- **Reasons.** No source gives the reason for:
  - the Strong SOCP exactness change;
  - the kNN and learning-to-branch preprints remaining unpublished;
  - the deletion of `LearningFromOptimalTrees/`.
  The content of that directory was seen as file names only.
- **Rejections.** Submission and rejection history is not public. "Unpublished" means absent from DBLP, Crossref and Semantic Scholar on 2026-10-10. Semantic Scholar rate-limited two of the five lookups.
- **Working records.** No lab notebooks, group wiki, experiment logs or internal coding guidelines were found.
- **Talks.** Spoken evidence is machine captions only. No recorded Q&A was found in which a critic challenges an experimental result (the Tutte colloquium exchange is in note 02).
- **Theses.** Only Shah's thesis (chapter 4 passages) was read directly here. The other 16 theses' computational chapters were not re-read; see note 04.

## Sources

Group A: papers and preprints. All primary. Text read through `pdftotext`; sections read are noted.
1. **S1** Kocuk, Dey, Sun, "Inexactness of SDP Relaxation and Valid Inequalities for Optimal Power Flow", IEEE Trans. Power Syst. 31(1):642–651, 2016, doi:10.1109/TPWRS.2015.2402640; arXiv:1410.1004 v1 (2014-10-04) and v3 (2014-12-18); author PDF https://www2.isye.gatech.edu/~sdey30/OPF.pdf (v1 text). Read: abstracts, §5–7, version comparison. Primary.
2. **S2** Kocuk, Dey, Sun, "Strong SOCP Relaxations for the Optimal Power Flow Problem", Oper. Res. 64(6):1177–1196, 2016, doi:10.1287/opre.2016.1489; arXiv:1504.06770 v1 (2015-04-25) and v4 (2015-10-31); author PDF https://www2.isye.gatech.edu/~sdey30/OPFCycle.pdf (2015-12-15). Read: abstracts, §4.1, §5 (setup), acknowledgments. Primary.
3. **S3** Kocuk, Dey, Sun, "Matrix minor reformulation and SOCP-based spatial branch-and-cut method for the AC optimal power flow problem", Math. Program. Comput. 10(4):557–596, 2018, doi:10.1007/s12532-018-0150-9; arXiv:1703.03050v1; https://www2.isye.gatech.edu/~sdey30/OPFMinor.pdf. Read: §4.3–§5. Primary.
4. **S4** Kocuk, Dey, Sun, "New Formulation and Strong MISOCP Relaxations for AC Optimal Transmission Switching Problem", IEEE Trans. Power Syst. 32(6):4161–4170, 2017, doi:10.1109/TPWRS.2017.2666718; arXiv:1510.02064 v1 (2015-10-07) and v3 (2016-02-17); https://www2.isye.gatech.edu/~sdey30/ACSwitch.pdf. Read: abstracts, headings, §6.3 (v3), implementation lines. Primary.
5. **S5** Kocuk, Jeon, Dey, Linderoth, Luedtke, Sun, "A Cycle-Based Formulation and Valid Inequalities for DC Power Transmission Problems with Switching", Oper. Res. 64(4):922–938, 2016, doi:10.1287/opre.2015.1471; arXiv:1412.6245 v1 (2014-12-19) and v3 (2015-10-16). Read: §6.3, conclusions, acknowledgment, version comparison. Primary.
6. **S6** Dey, Gupte, "Analysis of MILP Techniques for the Pooling Problem", Oper. Res. 63(2):412–427, 2015, doi:10.1287/opre.2015.1357; preprint https://optimization-online.org/wp-content/uploads/2013/04/3849.pdf. Read: §5–6. Primary.
7. **S7** Dey, Kocuk, Santana, "Convexifications of rank-one-based substructures in QCQPs and applications to the pooling problem", J. Glob. Optim. 77(2):227–272, 2020, doi:10.1007/s10898-019-00844-4; preprint arXiv:1902.00739v1 and https://www2.isye.gatech.edu/~sdey30/RankonePool.pdf. Read: one passage in §3, §4. Primary.
8. **S8** Dey, Santana, Wang, "New SOCP relaxation and branching rule for bipartite bilinear programs", Optim. Eng. 20:307–336, 2019, doi:10.1007/s11081-018-9402-9; arXiv:1803.09266v1; https://www2.isye.gatech.edu/~sdey30/BBPSensor.pdf. Read: §5. Primary.
9. **S9** Dey, Lodi, Tramontani, Wolsey, "On the Practical Strength of Two-Row Tableau Cuts", INFORMS J. Comput. 26(2):222–237, 2014, doi:10.1287/ijoc.2013.0559; preprint (dated 2012-08-12) https://www2.isye.gatech.edu/~sdey30/TwoRowPractical.pdf. Read: §1.1, §4, §5. Plus "Experiments with Two Row Tableau Cuts", IPCO 2010, LNCS pp. 424–437, doi:10.1007/978-3-642-13036-6_32 (abstract only, from the Springer page). Primary.
10. **S10** Dey, Iroume, Molinaro, Salvagnin, "Improving the Randomization Step in Feasibility Pump", SIAM J. Optim. 28(1):355–378, 2018, doi:10.1137/16M1095962; arXiv:1609.08121v1; https://www2.isye.gatech.edu/~sdey30/feaspump11.pdf. Read: §5. Primary.
11. **S11** Dey, Molinaro, Wang, "Analysis of Sparse Cutting Planes for Sparse MILPs with Applications to Stochastic MILPs", Math. Oper. Res. 43(1):304–332, 2018, doi:10.1287/moor.2017.0866; https://www2.isye.gatech.edu/~sdey30/sparsecut_sparseIP.pdf. Read: §3. Primary.
12. **S12** Dey, Dubey, Molinaro, Shah, "A theoretical and computational analysis of full strong-branching", Math. Program. 205:303–336, 2024, doi:10.1007/s10107-023-01977-x; arXiv:2110.10754 v1 and v2; https://www2.isye.gatech.edu/~sdey30/Strongbranching.pdf. Read: §5–6. Primary.
13. **S13** Shah, Dey, Molinaro, "Non-Monotonicity of Branching Rules with Respect to Linear Relaxations", INFORMS J. Comput. 38(1):53–66, 2026, doi:10.1287/ijoc.2024.0709; arXiv:2402.05213v1, identical in substance to https://www2.isye.gatech.edu/~sdey30/NonMonotonicity.pdf. Read: §3. Final IJOC text not read. Primary.
14. **S14** Shah, Dey, "Improving Full Strong Branching Decisions by Incorporating Additional Information", arXiv:2507.09455v1 (2025-07-13); https://www2.isye.gatech.edu/~sdey30/ImproveFSB.pdf. Read: §1.1, §5. Primary.
15. **S15** Becu, Dey, Qiu, Xavier, "Approximating the Gomory Mixed-Integer Cut Closure Using Historical Data", arXiv:2411.15090v1 (2024-11-22); https://www2.isye.gatech.edu/~sdey30/GMIHistory.pdf. Read: §5. Primary.
16. **S16** Dey, Mazumder, Molinaro, Wang, "Sparse principal component analysis and its l1-relaxation", arXiv:1712.00800v1 (2017-12-03). Dey, Mazumder, Wang, "Using ℓ1-Relaxation and Integer Programming to Obtain Dual Bounds for Sparse PCA", Oper. Res. 70(3):1914–1932, 2022, doi:10.1287/opre.2021.2153; arXiv:1810.09062 v1 (2018-10-22) and v3 (2021-08-17). Read: abstracts, §4, acknowledgments. Primary.
17. **S17** Dey, Kazachkov, Lodi, Muñoz, "Cutting Plane Generation through Sparse Principal Component Analysis", SIAM J. Optim. 32(2):1319–1343, 2022, doi:10.1137/21M1399956; https://www2.isye.gatech.edu/~sdey30/SDPviaSPCA.pdf. Read: §4, §6. Primary.
18. **S18** Gu, Dey, Richard, "Solving Sparse Separable Bilinear Programs Using Lifted Bilinear Cover Inequalities", INFORMS J. Comput. 36(3):884–899, 2024, doi:10.1287/ijoc.2022.0230; arXiv:2208.00345; https://www2.isye.gatech.edu/~sdey30/LiftedConvexCutComputation.pdf. Read: introduction, §4. Primary.
19. **S19** Li, Dey, Sahinidis, "A reformulation-enumeration MINLP algorithm for gas network design", J. Glob. Optim. 90(4):931–963, 2024, doi:10.1007/s10898-024-01424-x; arXiv:2307.07648 v1 (2023-07-14) and v3 (2024-01-30); https://www2.isye.gatech.edu/~sdey30/gasnetworkopt.pdf. Read: §4–5, version comparison. Primary.
20. **S20** Dey, Han, Wang, "Extreme strong branching for QCQPs", Oper. Res. Lett. 67:107446, 2026, doi:10.1016/j.orl.2026.107446; arXiv:2510.20650v1; https://www2.isye.gatech.edu/~sdey30/esb.pdf. Read: §3–4. Primary.
21. **S21** Dey, Han, Wang, "Aggregation of bilinear bipartite equality constraints and its application to structural model updating problem", J. Glob. Optim. 94(4):1099–1135, 2026, doi:10.1007/s10898-026-01607-8; arXiv:2410.14163v1; https://www2.isye.gatech.edu/~sdey30/AggregationBounded.pdf. Read: §3. Primary.
22. **S22** Dey, Muñoz, Serrano, "On obtaining the convex hull of quadratic inequalities via aggregations", SIAM J. Optim. 32(2):659–686, 2022, doi:10.1137/21M1428583; arXiv:2106.12629v1. Read: §4 passages. Primary.
23. **S23** Dey, Jiang, Kazachkov, Lodi, Muñoz, "Chvátal-Gomory Rounding of Eigenvector Inequalities for QCQPs", arXiv:2604.00932v1 (2026-04-01). Read: computational passages. Primary.
24. **S24** Cifuentes, Dey, Xu, "Sensitivity analysis for mixed binary quadratic programming", IPCO 2024, doi:10.1007/978-3-031-59835-7_33; Math. Program. 216:379–424, 2026, doi:10.1007/s10107-025-02265-6; arXiv:2312.06714 v1 and v2. Read: abstracts, acknowledgments. Primary.
25. **S25** Dey, Khajavirad, "A second-order cone representable class of nonconvex quadratic programs", Math. Program. 2026, doi:10.1007/s10107-026-02364-y; arXiv:2508.18435 v1 and v2. Read: abstracts, acknowledgments. Primary.
26. **S26** Gu, Dey, Xavier, Qiu, "Exploiting Instance and Variable Similarity to Improve Learning-Enhanced Branching", arXiv:2208.10028v1 (2022-08-22). Read: §4–6. Primary.
27. **S27** Johnson, Ahmed, Dey, Watson, "A K-Nearest Neighbor Heuristic for Real-Time DC Optimal Transmission Switching", arXiv:2003.10565 (v1 abstract; v3 full text, 2021-05-14). Primary.
28. **S28** Wang, Dey, Xie, "Variable Selection for Kernel Two-Sample Tests", arXiv:2302.07415 (v1 and v4 abstract pages, submission history). Primary.
29. **S29** Li, Dey, Xie, "On Sparse Canonical Correlation Analysis", Advances in Neural Information Processing Systems 37 (NeurIPS 2024), pp. 10707–10734, doi:10.52202/079017-0342; arXiv:2401.00308v1. Camera-ready PDF and supplementary zip from https://proceedings.neurips.cc/paper_files/paper/2024/hash/1496b12ccd6c8d2b4fd98f24a12bd438-Abstract-Conference.html. Read: §5, acknowledgments, checklist; supplement listed, `SOTA.py` header read. Primary.

Group B: code and data. All primary. Listed and read, never executed.

30. **S30** GitHub INFORMSJoC/2024.0709 (code and data for S13), https://github.com/INFORMSJoC/2024.0709, code DOI 10.1287/ijoc.2024.0709.cd, HEAD f3c6f5e (2025-01-29). Read: README, AUTHORS, `scripts/MIPLIB/*`, `scripts/MultiKnapsack/run_multiknapsack_expt.py`, `src/branch_and_bound.py`, `src/instance_generator_grb.py`, `results/MIPLIB/results.txt`. Primary.
31. **S31** GitHub INFORMSJoC/2024.0771 (code and data for Han, Jiang, Dey, Xie, "Regularized MIP Model for Integrating Energy Storage Systems and Its Application for Solving a Trilevel Interdiction Problem", INFORMS J. Comput. 38(3):729–744, 2026, doi:10.1287/ijoc.2024.0771), https://github.com/INFORMSJoC/2024.0771, code DOI 10.1287/ijoc.2024.0771.cd, HEAD 95eb83d (2025-03-10). Read: README, AUTHORS, data and results layout. Primary.
32. **S32** GitHub INFORMSJoC/2022.0326 (code and data for Xavier, Dey, Qiu, "Decomposable Formulation of Transmission Constraints for Decentralized Power Systems Optimization", INFORMS J. Comput. 36(6):1562–1578, 2024, doi:10.1287/ijoc.2022.0326), https://github.com/INFORMSJoC/2022.0326, code DOI 10.1287/ijoc.2022.0326.cd, HEAD bf70570 (2024-01-10). Read: README, AUTHORS, `TODO.md` (IJOC template). Primary.
33. **S33** GitHub joehuchette/floor-layout, "Computational materials for 'Strong mixed-integer formulations for the floor layout problem'" (Huchette, Dey, Vielma, INFOR 56(4):392–433, 2018, doi:10.1080/03155986.2017.1346916; paper not read), https://github.com/joehuchette/floor-layout, HEAD 2a95a8c (2016-05-26). Read: README, layout. Primary.
34. **S34** GitHub prachi-shah-opt/BinaryBNBPy, https://github.com/prachi-shah-opt/BinaryBNBPy (created 2024-09-09). Read: README, current tree, commit history, initial-commit tree (file names only). Primary.
35. **S35** GitHub handahye/esb, https://github.com/handahye/esb (created 2025-10-27). Read: README, file list, commits. Primary.
36. **S36** GitHub handahye/aggregation_bbe, https://github.com/handahye/aggregation_bbe (created 2024-09-13). Read: README, file list, commits. Primary.
37. **S37** TreeLibrary.zip, https://www2.isye.gatech.edu/~sdey30/TreeLibrary.zip (8 MATPOWER files; Last-Modified 2014-12-29). Primary.
38. **S38** SwitchInstances.zip, https://www2.isye.gatech.edu/~sdey30/SwitchInstances.zip (case118Blumsack.m, case300New.m, Random Demands.xlsx; Last-Modified 2014-12-29). Primary.
39. **S39** AkshayStandardAMPL.zip, https://www2.isye.gatech.edu/~sdey30/AkshayStandardAMPL.zip (50 AMPL .dat files, randstd11–60; Last-Modified 2016-05-02). Primary.
40. **S40** BBP_instances.zip, https://www2.isye.gatech.edu/~sdey30/BBP_instances.zip (10 txt files; Last-Modified 2018-03-27). Primary.
41. **S41** InstancesAndResultsWFP.zip, https://www2.isye.gatech.edu/~sdey30/InstancesAndResultsWFP.zip (two result spreadsheets plus an instance zip; Last-Modified 2017-06-23). Primary.
42. **S42** Random_GPP_instances.zip, https://www2.isye.gatech.edu/~sdey30/Random_GPP_instances.zip (24 instances in txt and pickle, plus README; Last-Modified 2019-02-03). Primary.
43. **S43** txt_form_data.zip, https://www2.isye.gatech.edu/~sdey30/txt_form_data.zip (covariance matrices for sparse PCA; Last-Modified 2018-10-22). Primary.

Group C: homepage, thesis, talks. All primary.

44. **S44** S. S. Dey, publications page, https://www2.isye.gatech.edu/~sdey30/publications.html, fetched live 2026-10-10 (link labels counted; data links mapped to papers). Primary.
45. **S45** P. Shah, "Closing the Gap: A Theoretical and Practical Exploration of Branch-and-Bound Procedure for Mixed-Integer Programs", PhD dissertation, Georgia Tech, 2025, https://hdl.handle.net/1853/77883 (handle checked live; text from note 04's local copy). Read: chapter 4 passages. Primary (student-authored record).
46. **S46** S. S. Dey, "Solving SDPs by using sparse PCA", IPAM workshop Deep Learning and Combinatorial Optimization, uploaded 2021-03-04, https://www.youtube.com/watch?v=yv0pHyrUZXo (auto-caption transcript in `references/sources/talks/`). Primary (machine transcription).
47. **S47** S. S. Dey, "Sparse PSD approximation of the PSD cone", Discrete Optimization Talks, uploaded 2020-10-24, https://www.youtube.com/watch?v=iIMYzJNCoos (auto-caption transcript). Primary (machine transcription).
48. **S48** S. S. Dey, MIP International 2024 talk on strong duals for integer programs, uploaded 2025-04-29, https://www.youtube.com/watch?v=JPgdFu8fD9U (auto-caption transcript). Primary (machine transcription).
49. **S49** S. S. Dey, "Strong duals for mixed integer programs", UW-Madison ISyE colloquium, uploaded 2025-10-06, https://www.youtube.com/watch?v=0OPWWIzfe4I (auto-caption transcript). Primary (machine transcription).
50. **S50** S. S. Dey, IPCO 2020 Summer School lectures 1–2, uploaded 2020-07-08 (https://www.youtube.com/watch?v=alWp58SW-Hk, https://www.youtube.com/watch?v=lIKaRZY-BTk), and Waterloo Tutte colloquium, 2020-12-11 (https://www.youtube.com/watch?v=4lZdL3GHvgs). Searched for accounts of how work was done; nothing used beyond note 02. Primary (machine transcription).

Group D: databases and metadata. All secondary.

51. **S51** arXiv API, query `au:Dey_Santanu_S` (71 records, fetched 2026-10-10), https://export.arxiv.org/api/query?search_query=au:Dey_Santanu_S. Submission histories for 30 records, from abstract pages cached earlier the same day, plus 4 live abstract pages (two versions each of arXiv:2003.10565 and arXiv:2302.07415). Secondary (records of the versions themselves).
52. **S52** DBLP SPARQL endpoint, pid 13/5858 (105 records), through `scripts/dblp_works.py`, 2026-10-10. Secondary.
53. **S53** Crossref REST API, https://api.crossref.org: DOI metadata for every DOI named here; `filter=updates:{DOI}` on 116 DOIs; `filter=orcid:0000-0003-0294-8287`; title searches for 71 arXiv records. 2026-10-10. Secondary.
54. **S54** Semantic Scholar Graph API, lookups for arXiv:2003.10565, arXiv:2411.15090 and arXiv:2507.09455, none with a venue. Two further lookups (arXiv:2208.10028, arXiv:2302.07415) were rate-limited. 2026-10-10. Secondary.
55. **S55** GitHub REST API (repository metadata, commits, user repositories, code search for paper titles with no hits), 2026-10-10. Secondary.
56. **S56** Optimization Online entry 2013/04/3849, https://optimization-online.org/2013/04/3849/ (used to resolve the preprint PDF of S6). Secondary.
57. **S57** B. Kocuk, personal site, https://sites.google.com/site/burakkocuk/ (link checked live; it is the download location named in S1). Secondary.

Group E: references verified by metadata only, not read. All secondary.

58. **S58** Crowder, Johnson, Padberg, "Solving Large-Scale Zero-One Linear Programming Problems", Oper. Res. 31(5):803–834, 1983, doi:10.1287/opre.31.5.803. Secondary.
59. **S59** Alfaki, Haugland, "A multi-commodity flow formulation for the generalized pooling problem", J. Glob. Optim. (online 2012), doi:10.1007/s10898-012-9890-7 (the recipe cited in S42). Secondary.
60. **S60** Kocuk, Morán R., "On Subadditive Duality for Conic Mixed-integer Programs", SIAM J. Optim. 2019, doi:10.1137/18M1210812 (the DOI attached by mistake to arXiv:1902.00739). Secondary.
61. **S61** Gasse, Chételat, Ferroni, Charlin, Lodi, "Exact Combinatorial Optimization with Graph Convolutional Neural Networks", arXiv:1906.01629 (2019); probable source of the "Gasse et al" generators in S30 [inferred]. Secondary.

Attempted, not readable:
- OpenReview forum for S29, https://openreview.net/forum?id=MZ47wPr6C3. The API returned HTTP 403 "ChallengeRequiredError" and WebFetch received a browser-verification page. Not read.

Cross-references, not counted as sources: research notes 01 (publications), 02 (stated method) and 04 (mentorship) in this folder.
